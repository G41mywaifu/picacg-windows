import os
import re

from PySide2 import QtWidgets, QtGui  # 导入PySide2部件
from PySide2.QtCore import QTimer, QUrl
from PySide2.QtGui import QIcon, QPixmap, QDesktopServices
from PySide2.QtWidgets import QMessageBox

from conf import config
from resources import resources
from src.qt.menu.qtabout import QtAbout
from src.qt.read.qtbookinfo import QtBookInfo
from src.qt.com.qtbubblelabel import QtBubbleLabel
from src.qt.main.qtcategory import QtCategory
from src.qt.download.qtdownload import QtDownload
from src.qt.read.qtepsinfo import QtEpsInfo
from src.qt.user.qtfavorite import QtFavorite
from src.qt.user.qthistory import QtHistory
from src.qt.com.qtloading import QtLoading
from src.qt.user.qtlogin import QtLogin
from src.qt.main.qtrank import QtRank
from src.qt.read.qtreadimg import QtReadImg
from src.qt.user.qtregister import QtRegister
from src.qt.main.qtsearch import QtSearch
from src.qt.menu.qtsetting import QtSetting
from src.qt.util.qttask import QtTask
from src.qt.user.qtuser import QtUser
from src.server import Server, req
from src.util import Log
from ui.main import Ui_MainWindow
import waifu2x


class BikaQtMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.userInfo = None
        self.setupUi(self)
        self.setWindowTitle("哔咔漫画")
        self.msgForm = QtBubbleLabel(self)

        self.qtTask = QtTask()

        icon = QIcon()
        pic = QPixmap()
        pic.loadFromData(resources.DataMgr.GetData("logo_round"))
        icon.addPixmap(pic, QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.aboutForm = QtAbout(self)

        self.searchForm = QtSearch(self)
        self.favoriteForm = QtFavorite(self)
        self.downloadForm = QtDownload(self)
        self.categoryForm = QtCategory(self)
        self.loadingForm = QtLoading(self)
        self.rankForm = QtRank(self)

        self.loginForm = QtLogin(self)
        self.registerForm = QtRegister(self)

        self.historyForm = QtHistory(self)

        self.qtReadImg = QtReadImg(self)

        self.userForm = QtUser(self)
        self.bookInfoForm = QtBookInfo(self)

        self.epsInfoForm = QtEpsInfo(self)

        self.task = QtTask()
        self.task.SetOwner(self)
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        # self.timer.timeout.connect(self.OnTimeOut)
        # self.timer.start()

        self.stackedWidget.addWidget(self.loginForm)
        self.stackedWidget.addWidget(self.userForm)

        self.settingForm = QtSetting(self)
        self.settingForm.LoadSetting()

        self.resize(self.settingForm.mainSize)
        self.bookInfoForm.resize(self.settingForm.bookSize)
        self.qtReadImg.resize(self.settingForm.readSize)

        self.loginForm.userIdEdit.setText(self.settingForm.userId)
        self.loginForm.passwdEdit.setText(self.settingForm.passwd)

        self.menusetting.triggered.connect(self.OpenSetting)
        self.menuabout.triggered.connect(self.OpenAbout)

    # def ClearExpiredCache(self):
    #     try:
    #         toPath = os.path.join(config.SavePath, config.CachePathDir)
    #         for root, dirs, names in os.walk(toPath):
    #             for name in names:
    #                 isDel = False
    #                 filename = os.path.join(root, name)
    #                 with open(filename, "rb") as f:
    #                     nameSize = int().from_bytes(f.read(2), byteorder='little')
    #                     timeTick = int().from_bytes(f.read(4), byteorder='little')
    #                     # if int(time.time()) - timeTick >= config.CacheExpired:
    #                     #     isDel = True
    #
    #                 if isDel:
    #                     os.remove(filename)
    #
    #     except Exception as es:
    #         Log.Error(es)


    # def OnTimeOut(self):
    #     self.task.run()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        userId = self.loginForm.userIdEdit.text()
        passwd = self.loginForm.passwdEdit.text()
        self.bookInfoForm.close()
        self.settingForm.ExitSaveSetting(self.size(), self.bookInfoForm.size(), self.qtReadImg.size(), userId, passwd)

    def Init(self):
        # config.UpdateIos()
        # self.ClearExpiredCache()
        waifu2x.Set(config.Waifu2xThread, config.Encode, getattr(config, "Model"+str(config.Model)))
        stat = waifu2x.Init()
        if stat < 0:
            self.msgForm.ShowError("waifu2x初始化错误")

        Log.Info("waifu2x初始化: " + str(stat) + " encode: " + str(config.Encode))
        gpuInfo = waifu2x.GetGpuInfo()
        self.settingForm.SetGpuInfos(gpuInfo)

        self.InitUpdate()
        self.loginForm.Init()
        return

    def OpenSetting(self):
        self.settingForm.show()
        pass

    def OpenAbout(self):
        self.aboutForm.show()
        pass

    def InitUpdate(self):
        self.qtTask.AddHttpTask(lambda x: Server().Send(req.CheckUpdateReq(), bakParam=x), self.InitUpdateBack)

    def InitUpdateBack(self, data):
        try:
            r = QMessageBox.information(self, "更新", "当前版本{} ,检查到更新，是否前往更新\n{}".format(config.UpdateVersion,
                                                                                        data),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if r == QMessageBox.Yes:
                QDesktopServices.openUrl(QUrl("https://github.com/tonquer/picacg-windows/releases"))
        except Exception as es:
            Log.Error(es)