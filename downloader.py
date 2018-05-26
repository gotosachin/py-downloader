from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

import urllib.request

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        
        layout = QVBoxLayout()
        
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        browse = QPushButton("Browse")
        self.progress = QProgressBar()
        download = QPushButton("Download")
        
        #close button
        #close_button = QPushButton("Close")
        #close_button.clicked.connect(self.close)
        
        #set placeholder for text
        self.url.setPlaceholderText("Url")
        self.save_location.setPlaceholderText("File save location")
        #self.save_location.setReadOnly(True)
        
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)
        
        #put all widgets into layout
        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)
        #layout.addWidget(close_button)
        
        self.setLayout(layout)
        #set window title
        self.setWindowTitle("Sachin-Downloader")
        #self.setGeometry(100, 100, 200, 50)
        self.resize(600,300)
        self.setFocus()
        self.show()
        
        # calling downlad method on click of download button
        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)
        
        
        
    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save file as", directory=".", filter="All Files(*.*)")
        self.save_location.setText(QDir.toNativeSeparators(str(save_file[0])))
        #print(save_file)
        #self.save_location.setText(save_file)
        
    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        
        #start downloading
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except:
            QMessageBox.warning(self, "warning", "Download Failed!!")
            return
        
        QMessageBox.information(self, "Information", "The downlaod is complete")
        
        self.url.setText("")
        self.save_location.setText("")
        self.progress.setValue(0)
        
        
    def report(self, chunkNumber, chunkSize, totalsize):
        readsofar = chunkNumber*chunkSize
        if readsofar > 0:
            percentage = readsofar * 100/totalsize
            self.progress.setValue(int(percentage))
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #dialog = QDialog()
    #dialog.show()
    #app.exec_()
    dw = Downloader()
    sys.exit(app.exec_())
