# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 681)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(750, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(750, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_settings.setMinimumSize(QtCore.QSize(0, 230))
        self.groupBox_settings.setMaximumSize(QtCore.QSize(16777215, 230))
        self.groupBox_settings.setObjectName("groupBox_settings")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_settings)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_settings = QtWidgets.QTabWidget(self.groupBox_settings)
        self.tabWidget_settings.setObjectName("tabWidget_settings")
        self.tab_files_source = QtWidgets.QWidget()
        self.tab_files_source.setObjectName("tab_files_source")
        self.label_report_type = QtWidgets.QLabel(self.tab_files_source)
        self.label_report_type.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.label_report_type.setObjectName("label_report_type")
        self.checkBox_report_scan = QtWidgets.QCheckBox(self.tab_files_source)
        self.checkBox_report_scan.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.checkBox_report_scan.setObjectName("checkBox_report_scan")
        self.checkBox_report_host = QtWidgets.QCheckBox(self.tab_files_source)
        self.checkBox_report_host.setGeometry(QtCore.QRect(160, 30, 61, 20))
        self.checkBox_report_host.setObjectName("checkBox_report_host")
        self.checkBox_report_vulnerabilities = QtWidgets.QCheckBox(self.tab_files_source)
        self.checkBox_report_vulnerabilities.setGeometry(QtCore.QRect(310, 30, 121, 20))
        self.checkBox_report_vulnerabilities.setObjectName("checkBox_report_vulnerabilities")
        self.checkBox_report_noncompliance = QtWidgets.QCheckBox(self.tab_files_source)
        self.checkBox_report_noncompliance.setGeometry(QtCore.QRect(500, 30, 131, 20))
        self.checkBox_report_noncompliance.setObjectName("checkBox_report_noncompliance")
        self.groupBox_options_scan = QtWidgets.QGroupBox(self.tab_files_source)
        self.groupBox_options_scan.setGeometry(QtCore.QRect(10, 50, 141, 91))
        self.groupBox_options_scan.setObjectName("groupBox_options_scan")
        self.checkBox_debug_data_scan = QtWidgets.QCheckBox(self.groupBox_options_scan)
        self.checkBox_debug_data_scan.setGeometry(QtCore.QRect(10, 25, 121, 20))
        self.checkBox_debug_data_scan.setObjectName("checkBox_debug_data_scan")
        self.groupBox_options_host = QtWidgets.QGroupBox(self.tab_files_source)
        self.groupBox_options_host.setGeometry(QtCore.QRect(160, 50, 141, 91))
        self.groupBox_options_host.setObjectName("groupBox_options_host")
        self.checkBox_debug_data_host = QtWidgets.QCheckBox(self.groupBox_options_host)
        self.checkBox_debug_data_host.setGeometry(QtCore.QRect(10, 25, 121, 20))
        self.checkBox_debug_data_host.setObjectName("checkBox_debug_data_host")
        self.groupBox_options_vulnerabilities = QtWidgets.QGroupBox(self.tab_files_source)
        self.groupBox_options_vulnerabilities.setGeometry(QtCore.QRect(310, 50, 181, 91))
        self.groupBox_options_vulnerabilities.setObjectName("groupBox_options_vulnerabilities")
        self.checkBox_debug_data_vulnerabilities = QtWidgets.QCheckBox(self.groupBox_options_vulnerabilities)
        self.checkBox_debug_data_vulnerabilities.setGeometry(QtCore.QRect(10, 25, 121, 20))
        self.checkBox_debug_data_vulnerabilities.setObjectName("checkBox_debug_data_vulnerabilities")
        self.checkBox_vulnerabilities_none_filter_out = QtWidgets.QCheckBox(self.groupBox_options_vulnerabilities)
        self.checkBox_vulnerabilities_none_filter_out.setGeometry(QtCore.QRect(10, 45, 161, 20))
        self.checkBox_vulnerabilities_none_filter_out.setObjectName("checkBox_vulnerabilities_none_filter_out")
        self.checkBox_vulnerabilities_none_skip = QtWidgets.QCheckBox(self.groupBox_options_vulnerabilities)
        self.checkBox_vulnerabilities_none_skip.setGeometry(QtCore.QRect(10, 65, 161, 20))
        self.checkBox_vulnerabilities_none_skip.setObjectName("checkBox_vulnerabilities_none_skip")
        self.groupBox_options_noncompliance = QtWidgets.QGroupBox(self.tab_files_source)
        self.groupBox_options_noncompliance.setGeometry(QtCore.QRect(500, 50, 171, 91))
        self.groupBox_options_noncompliance.setObjectName("groupBox_options_noncompliance")
        self.checkBox_debug_data_noncompliance = QtWidgets.QCheckBox(self.groupBox_options_noncompliance)
        self.checkBox_debug_data_noncompliance.setGeometry(QtCore.QRect(10, 25, 121, 20))
        self.checkBox_debug_data_noncompliance.setObjectName("checkBox_debug_data_noncompliance")
        self.tabWidget_settings.addTab(self.tab_files_source, "")
        self.tab_files_target = QtWidgets.QWidget()
        self.tab_files_target.setObjectName("tab_files_target")
        self.label_target_directory = QtWidgets.QLabel(self.tab_files_target)
        self.label_target_directory.setGeometry(QtCore.QRect(10, 8, 120, 21))
        self.label_target_directory.setMinimumSize(QtCore.QSize(110, 0))
        self.label_target_directory.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_target_directory.setObjectName("label_target_directory")
        self.lineEdit_target_directory = QtWidgets.QLineEdit(self.tab_files_target)
        self.lineEdit_target_directory.setGeometry(QtCore.QRect(130, 8, 441, 21))
        self.lineEdit_target_directory.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_target_directory.setMaximumSize(QtCore.QSize(450, 16777215))
        self.lineEdit_target_directory.setReadOnly(True)
        self.lineEdit_target_directory.setObjectName("lineEdit_target_directory")
        self.pushButton_target_dir_change = QtWidgets.QPushButton(self.tab_files_target)
        self.pushButton_target_dir_change.setGeometry(QtCore.QRect(590, 3, 80, 32))
        self.pushButton_target_dir_change.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_target_dir_change.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_target_dir_change.setObjectName("pushButton_target_dir_change")
        self.lineEdit_suffix_custom_value = QtWidgets.QLineEdit(self.tab_files_target)
        self.lineEdit_suffix_custom_value.setEnabled(True)
        self.lineEdit_suffix_custom_value.setGeometry(QtCore.QRect(160, 98, 150, 21))
        self.lineEdit_suffix_custom_value.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_suffix_custom_value.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_suffix_custom_value.setClearButtonEnabled(False)
        self.lineEdit_suffix_custom_value.setObjectName("lineEdit_suffix_custom_value")
        self.checkBox_suffix_timestamp = QtWidgets.QCheckBox(self.tab_files_target)
        self.checkBox_suffix_timestamp.setGeometry(QtCore.QRect(10, 68, 300, 21))
        self.checkBox_suffix_timestamp.setMinimumSize(QtCore.QSize(300, 0))
        self.checkBox_suffix_timestamp.setMaximumSize(QtCore.QSize(300, 16777215))
        self.checkBox_suffix_timestamp.setObjectName("checkBox_suffix_timestamp")
        self.checkBox_suffix_custom = QtWidgets.QCheckBox(self.tab_files_target)
        self.checkBox_suffix_custom.setGeometry(QtCore.QRect(10, 98, 150, 21))
        self.checkBox_suffix_custom.setMinimumSize(QtCore.QSize(150, 0))
        self.checkBox_suffix_custom.setMaximumSize(QtCore.QSize(150, 16777215))
        self.checkBox_suffix_custom.setObjectName("checkBox_suffix_custom")
        self.checkBox_set_source_directory_as_target_directory = QtWidgets.QCheckBox(self.tab_files_target)
        self.checkBox_set_source_directory_as_target_directory.setGeometry(QtCore.QRect(10, 30, 281, 20))
        self.checkBox_set_source_directory_as_target_directory.setObjectName("checkBox_set_source_directory_as_target_directory")
        self.label_target_file_name = QtWidgets.QLabel(self.tab_files_target)
        self.label_target_file_name.setGeometry(QtCore.QRect(10, 130, 121, 16))
        self.label_target_file_name.setObjectName("label_target_file_name")
        self.label_target_file_name_value = QtWidgets.QLabel(self.tab_files_target)
        self.label_target_file_name_value.setGeometry(QtCore.QRect(130, 130, 431, 16))
        self.label_target_file_name_value.setText("")
        self.label_target_file_name_value.setObjectName("label_target_file_name_value")
        self.tabWidget_settings.addTab(self.tab_files_target, "")
        self.verticalLayout_3.addWidget(self.tabWidget_settings)
        self.verticalLayout.addWidget(self.groupBox_settings)
        self.groupBox_action = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_action.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox_action.setObjectName("groupBox_action")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_action)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_action)
        self.pushButton_start.setEnabled(True)
        self.pushButton_start.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_start.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_start.setToolTipDuration(-1)
        self.pushButton_start.setStatusTip("")
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 0, 0, 1, 1)
        self.pushButton_target_dir_open = QtWidgets.QPushButton(self.groupBox_action)
        self.pushButton_target_dir_open.setEnabled(True)
        self.pushButton_target_dir_open.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_target_dir_open.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_target_dir_open.setObjectName("pushButton_target_dir_open")
        self.gridLayout.addWidget(self.pushButton_target_dir_open, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_action)
        self.groupBox_progress = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_progress.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_progress.setObjectName("groupBox_progress")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_progress)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_progress = QtWidgets.QTextEdit(self.groupBox_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_progress.sizePolicy().hasHeightForWidth())
        self.textEdit_progress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.textEdit_progress.setFont(font)
        self.textEdit_progress.setReadOnly(True)
        self.textEdit_progress.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_progress.setObjectName("textEdit_progress")
        self.horizontalLayout.addWidget(self.textEdit_progress)
        self.verticalLayout.addWidget(self.groupBox_progress)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_directory.setObjectName("actionOpen_directory")
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionStart_analysis = QtWidgets.QAction(MainWindow)
        self.actionStart_analysis.setObjectName("actionStart_analysis")
        self.actionChange_separator = QtWidgets.QAction(MainWindow)
        self.actionChange_separator.setObjectName("actionChange_separator")
        self.actionChange_target_directory = QtWidgets.QAction(MainWindow)
        self.actionChange_target_directory.setObjectName("actionChange_target_directory")
        self.actionOpen_target_directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_target_directory.setObjectName("actionOpen_target_directory")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionOpen_directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAction.addAction(self.actionStart_analysis)
        self.menuAction.addSeparator()
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionChange_target_directory)
        self.menuAction.addAction(self.actionOpen_target_directory)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_settings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_settings.setTitle(_translate("MainWindow", "Settings"))
        self.label_report_type.setText(_translate("MainWindow", "Select one or more report type:"))
        self.checkBox_report_scan.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get spreadsheet with <span style=\" font-weight:600;\">scan sum-up</span>.</p></body></html>"))
        self.checkBox_report_scan.setText(_translate("MainWindow", "scan"))
        self.checkBox_report_host.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get spreadsheet with <span style=\" font-weight:600;\">host sum-up</span>.</p></body></html>"))
        self.checkBox_report_host.setText(_translate("MainWindow", "host"))
        self.checkBox_report_vulnerabilities.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get spreadsheet with <span style=\" font-weight:600;\">vulnerabilities sum-up</span>.</p></body></html>"))
        self.checkBox_report_vulnerabilities.setText(_translate("MainWindow", "vulnerabilities"))
        self.checkBox_report_noncompliance.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get spreadsheet with <span style=\" font-weight:600;\">noncompliance sum-up</span>.</p></body></html>"))
        self.checkBox_report_noncompliance.setText(_translate("MainWindow", "noncompliance"))
        self.groupBox_options_scan.setTitle(_translate("MainWindow", "Scan tab options"))
        self.checkBox_debug_data_scan.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get additional columns for selected report type like source file name with path, policy name and more. </p><p><span style=\" font-style:italic;\">Note: Debug columns name are marked in </span><span style=\" font-style:italic; color:#0000ff;\">blue color</span><span style=\" font-style:italic;\">.</span></p></body></html>"))
        self.checkBox_debug_data_scan.setText(_translate("MainWindow", "add debug data"))
        self.groupBox_options_host.setTitle(_translate("MainWindow", "Host tab options"))
        self.checkBox_debug_data_host.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get additional columns for selected report type like source file name with path, policy name and more. </p><p><span style=\" font-style:italic;\">Note: Debug columns name are marked in </span><span style=\" font-style:italic; color:#0000ff;\">blue color</span><span style=\" font-style:italic;\">.</span></p></body></html>"))
        self.checkBox_debug_data_host.setText(_translate("MainWindow", "add debug data"))
        self.groupBox_options_vulnerabilities.setTitle(_translate("MainWindow", "Vulnerabilities tab options"))
        self.checkBox_debug_data_vulnerabilities.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get additional columns for selected report type like source file name with path, policy name and more. </p><p><span style=\" font-style:italic;\">Note: Debug columns name are marked in </span><span style=\" font-style:italic; color:#0000ff;\">blue color</span><span style=\" font-style:italic;\">.</span></p></body></html>"))
        self.checkBox_debug_data_vulnerabilities.setText(_translate("MainWindow", "add debug data"))
        self.checkBox_vulnerabilities_none_filter_out.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to automatically filter out plugins results with None Risk Factor and see in final report only these which Risk Factor is equal Low, Medium, High or Critical.</p><p><span style=\" font-style:italic;\">Note: Plugins results with None Risk Factor are not removed from report, to see them use filter in column Risk Factor.</span></p></body></html>"))
        self.checkBox_vulnerabilities_none_filter_out.setText(_translate("MainWindow", "filter out None results"))
        self.checkBox_vulnerabilities_none_skip.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to completely skip plugins results with None Risk Factor and see in final report only these which Risk Factor is equal Low, Medium, High or Critical.</p><p><span style=\" font-style:italic;\">Note: To see plugins results with None Risk Factor in report you need disable this option and analyze selected files again.</span></p></body></html>"))
        self.checkBox_vulnerabilities_none_skip.setText(_translate("MainWindow", "skip None results"))
        self.groupBox_options_noncompliance.setTitle(_translate("MainWindow", "Noncompliance tab options"))
        self.checkBox_debug_data_noncompliance.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to get additional columns for selected report type like source file name with path, policy name and more. </p><p><span style=\" font-style:italic;\">Note: Debug columns name are marked in </span><span style=\" font-style:italic; color:#0000ff;\">blue color</span><span style=\" font-style:italic;\">.</span></p></body></html>"))
        self.checkBox_debug_data_noncompliance.setText(_translate("MainWindow", "add debug data"))
        self.tabWidget_settings.setTabText(self.tabWidget_settings.indexOf(self.tab_files_source), _translate("MainWindow", "Source files"))
        self.label_target_directory.setText(_translate("MainWindow", "Target directory:"))
        self.lineEdit_target_directory.setToolTip(_translate("MainWindow", "<html><head/><body><p>Current target directory for output file.</p></body></html>"))
        self.pushButton_target_dir_change.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to <span style=\" font-weight:600;\">change target directory</span> for output file.</p></body></html>"))
        self.pushButton_target_dir_change.setText(_translate("MainWindow", "Change"))
        self.lineEdit_suffix_custom_value.setToolTip(_translate("MainWindow", "<html><head/><body><p>Key-in text here and than mark checkbox on the left if you want to add suffix taken from this field into target filename.</p><p><span style=\" font-style:italic;\">Note: Take a look below to see target filename example received that way.</span></p></body></html>"))
        self.checkBox_suffix_timestamp.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to add suffix with &quot;_YYYYMMDD_HHMMSS&quot; into target filename.</p><p><span style=\" font-style:italic;\">Note: Take a look below to see target filename example received that way.</span></p></body></html>"))
        self.checkBox_suffix_timestamp.setText(_translate("MainWindow", "add suffix with \"_YYYYMMDD_HHMMSS\""))
        self.checkBox_suffix_custom.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to add suffix taken from field on the right into target filename.</p><p><span style=\" font-style:italic;\">Note: Take a look below to see target filename example received that way.</span></p></body></html>"))
        self.checkBox_suffix_custom.setText(_translate("MainWindow", "add custom suffix"))
        self.checkBox_set_source_directory_as_target_directory.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mark this checkbox if you want to automatically change target directory each time when you select new source file/-s and set target directory to be the same as source file/-s directory.</p><p><span style=\" font-style:italic;\">Note: If you use Open directory to open source files this directory will be use as target directory for all files including these from subdirectories.</span></p></body></html>"))
        self.checkBox_set_source_directory_as_target_directory.setText(_translate("MainWindow", "set source directory as target directory"))
        self.label_target_file_name.setText(_translate("MainWindow", "Target filename:"))
        self.label_target_file_name_value.setToolTip(_translate("MainWindow", "<html><head/><body><p>Target filename example.</p><p><span style=\" font-style:italic;\">Note: Use two checkboxes above interchangeably to change the order in target filename.</span></p></body></html>"))
        self.tabWidget_settings.setTabText(self.tabWidget_settings.indexOf(self.tab_files_target), _translate("MainWindow", "Target files"))
        self.groupBox_action.setTitle(_translate("MainWindow", "Action"))
        self.pushButton_start.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to <span style=\" font-weight:600;\">start </span>analysis of selected *.nessus files.</p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_target_dir_open.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to <span style=\" font-weight:600;\">open target directory</span>.</p></body></html>"))
        self.pushButton_target_dir_open.setText(_translate("MainWindow", "Open"))
        self.groupBox_progress.setTitle(_translate("MainWindow", "Progress preview"))
        self.textEdit_progress.setToolTip(_translate("MainWindow", "<html><head/><body><p>Here you will see whole progress preview for any action taken.</p><p><span style=\" font-style:italic;\">Note: You can mark and copy text from this field.</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAction.setTitle(_translate("MainWindow", "Action"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_directory.setText(_translate("MainWindow", "Open directory"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file\\-s"))
        self.actionStart_analysis.setText(_translate("MainWindow", "Start analysis"))
        self.actionChange_separator.setText(_translate("MainWindow", "Change separator"))
        self.actionChange_target_directory.setText(_translate("MainWindow", "Change target directory"))
        self.actionOpen_target_directory.setText(_translate("MainWindow", "Open target directory"))
        self.actionAbout.setText(_translate("MainWindow", "About"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
