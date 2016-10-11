# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\realpro\picdeal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(579, 389)
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(dialog)
        self.radioButton.setGeometry(QtCore.QRect(30, 70, 89, 16))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 100, 89, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 130, 89, 16))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 160, 89, 16))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 190, 89, 16))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 220, 89, 16))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayoutWidget = QtGui.QWidget(dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 70, 171, 161))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.pushButton_4)
        self.pushButton_6 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_8)
        self.pushButton_5 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pushButton_5)
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(380, 40, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(410, 70, 61, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_4 = QtGui.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(380, 70, 21, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(380, 100, 21, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_2 = QtGui.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 100, 61, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_6 = QtGui.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(380, 130, 21, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_9 = QtGui.QPushButton(dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 300, 75, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 300, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(490, 130, 75, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(490, 70, 75, 23))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.toolButton = QtGui.QToolButton(dialog)
        self.toolButton.setGeometry(QtCore.QRect(410, 130, 37, 18))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", u"图像处理", None))
        self.label.setText(_translate("dialog", u"保存格式", None))
        self.radioButton.setText(_translate("dialog", "Bpm", None))
        self.radioButton_2.setText(_translate("dialog", "Gif", None))
        self.radioButton_3.setText(_translate("dialog", "GPEG", None))
        self.radioButton_4.setText(_translate("dialog", "Png", None))
        self.radioButton_5.setText(_translate("dialog", "Tiff", None))
        self.radioButton_6.setText(_translate("dialog", "Wmf", None))
        self.label_2.setText(_translate("dialog", u"图像处理", None))
        self.pushButton.setText(_translate("dialog", u"黑白处理", None))
        self.pushButton_2.setText(_translate("dialog", u"模糊滤镜", None))
        self.pushButton_3.setText(_translate("dialog", u"浮雕滤镜", None))
        self.pushButton_4.setText(_translate("dialog", u"左右逆反", None))
        self.pushButton_6.setText(_translate("dialog", u"平滑处理", None))
        self.pushButton_7.setText(_translate("dialog", u"轮廓滤镜", None))
        self.pushButton_8.setText(_translate("dialog", u"边界滤镜", None))
        self.pushButton_5.setText(_translate("dialog", u"锐化处理", None))
        self.label_3.setText(_translate("dialog", u"几何变换", None))
        self.label_4.setText(_translate("dialog", "PX", None))
        self.label_5.setText(_translate("dialog", "PY", None))
        self.label_6.setText(_translate("dialog", u"角度变化", None))
        self.pushButton_9.setText(_translate("dialog", u"预览图像", None))
        self.pushButton_10.setText(_translate("dialog", u"保存", None))
        self.pushButton_11.setText(_translate("dialog", u"查看几何变化", None))
        self.pushButton_12.setText(_translate("dialog", u"关于XY", None))
        self.toolButton.setText(_translate("dialog", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

