
import sys
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QAction
from numpy import array, transpose, dot, matrix
from numpy.linalg import inv, lstsq
from matplotlib.pyplot import show, plot

from DataContainer import *
from Compute import *

class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = loadUi('mainwindow.ui')
        self.ui.openInputFile.clicked.connect(self.openInputFileClicked)
        self.ui.compute.clicked.connect(self.compute)
        self.ui.plotGraph.clicked.connect(self.plotGraphic)

    def openInputFileClicked(self):
        filename = QFileDialog.getOpenFileName(self, "Input file", "")
        self.ui.inputFile.setText(filename)

    def compute(self):
        # read configuration data
        Dim_x1 = int(self.ui.DimX1.text())
        Dim_x2 = int(self.ui.DimX2.text())
        Dim_x3 = int(self.ui.DimX3.text())
        Dim_y = int(self.ui.DimY.text())
        selection_range = int(self.ui.lineEdit_10.text())

        inputfile = self.ui.inputFile.text()

        pol_pow_x1 = int(self.ui.PolX1.text())
        pol_pow_x2 = int(self.ui.PolX2.text())
        pol_pow_x3 = int(self.ui.PolX3.text())

        bq0AsAvg = self.ui.b0AsAvg.isChecked()
        lambda_separate = self.ui.oneLambda.isChecked()

        if self.ui.chebish.isChecked():
            polynom_type = "cheb_value_in_point"
        elif self.ui.lagger.isChecked():
            polynom_type = "Lag_value_in_point"
        elif self.ui.ermit.isChecked():
            polynom_type = "Ermit_value_in_point"
        elif self.ui.legandr.isChecked():
            polynom_type = "Lejan_value_in_point"

        self.ui.plotFunc.clear()
        self.ui.plotFunc.addItems(["Y" + str(i) for i in range(0, Dim_y)])

        # read data from input
        self.data = DataContainer(inputfile, Dim_x1, Dim_x2, Dim_x3, Dim_y, selection_range)
        if self.data.ERROR:
            exit(1)

        result = []
        result.append(self.data.data_x1)
        result.append(self.data.data_x2)
        result.append(self.data.data_x3)
        result.append(self.data.data_y)

        self.computation = Compute(self.data, polynom_type, pol_pow_x1, pol_pow_x2, pol_pow_x3, bq0AsAvg, lambda_separate)
        # self.computation = Computation(polynom_type, pol_pow_x1, pol_pow_x2, pol_pow_x3, bq0AsAvg=bq0AsAvg, lambdaInOneSystem=lambda_separate) # should changed

        # output data
        #results = self.computation.formOutput()
        self.ui.output.setText(str(result))
        #file = open(self.ui.outputFile.text(), "w+")
        #file.write(results)
        #file.close()

# should be changed
    def plotGraphic(self):
        var_num = self.ui.plotFunc.currentIndex()
        self.computation.plotVar(var_num)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.ui.show()
    sys.exit(app.exec_())