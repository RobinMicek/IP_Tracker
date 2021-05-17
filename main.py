from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import socket
from ip2geotools.databases.noncommercial import DbIpCity


class IPTracker(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(280,300)
        self.setWindowTitle("IP Tracker")

        #Widgets - Labels
        self.labelIP = QLabel("IP Address:")
        self.labelIPx = QLabel(self)

        self.labelURL = QLabel("URL Address:")
        self.labelURLx = QLabel(self)

        self.labelCITY = QLabel("City:")
        self.labelCITYx = QLabel(self)

        self.labelREGION = QLabel("Region:")
        self.labelREGIONx = QLabel(self)

        self.labelCOUNTRY = QLabel("Country:")
        self.labelCOUNTRYx = QLabel(self)

        self.spacer = QLabel(self)

        #Widgets - Buttons
        self.buttonURL = QPushButton("Find by URL")
        self.buttonURL.clicked.connect(self.FindByUrl)
        self.buttonIP = QPushButton("Find by IP")
        self.buttonIP.clicked.connect(self.FindByIp)

        #Widgets - Text Lines
        self.inputIP = QLineEdit(self)
        self.inputURL = QLineEdit(self)


        self.ui()

    def ui(self):
        layoutHorizontalIP = QHBoxLayout()
        layoutHorizontalURL = QHBoxLayout()
        layoutHorizontalCITY = QHBoxLayout()
        layoutHorizontalREGION = QHBoxLayout()
        layoutHorizontalCOUNTRY = QHBoxLayout()
        layoutHorizontalFINDURL = QHBoxLayout()
        layoutHorizontalFINDIP = QHBoxLayout()
        layoutHorizontalSPACER = QHBoxLayout()
        layoutVertical = QVBoxLayout()

        #Layout IP
        layoutHorizontalIP.addWidget(self.labelIP)
        layoutHorizontalIP.addWidget(self.labelIPx)

        #Layout URL
        layoutHorizontalURL.addWidget(self.labelURL)
        layoutHorizontalURL.addWidget(self.labelURLx)

        #Layout City
        layoutHorizontalCITY.addWidget(self.labelCITY)
        layoutHorizontalCITY.addWidget(self.labelCITYx)

        #Layout Region
        layoutHorizontalREGION.addWidget(self.labelREGION)
        layoutHorizontalREGION.addWidget(self.labelREGIONx)

        #Layout Country
        layoutHorizontalCOUNTRY.addWidget(self.labelCOUNTRY)
        layoutHorizontalCOUNTRY.addWidget(self.labelCOUNTRYx)

        #Layout Find by URL
        layoutHorizontalFINDURL.addWidget(self.inputURL)
        layoutHorizontalFINDURL.addWidget(self.buttonURL)

        #Layout Find by IP
        layoutHorizontalFINDIP.addWidget(self.inputIP)
        layoutHorizontalFINDIP.addWidget(self.buttonIP)

        #Layout Spacer
        layoutHorizontalSPACER.addWidget(self.spacer)

        #Compile layouts
        layoutVertical.addLayout(layoutHorizontalIP)
        layoutVertical.addLayout(layoutHorizontalURL)
        layoutVertical.addLayout(layoutHorizontalSPACER)
        layoutVertical.addLayout(layoutHorizontalCITY)
        layoutVertical.addLayout(layoutHorizontalREGION)
        layoutVertical.addLayout(layoutHorizontalCOUNTRY)
        layoutVertical.addLayout(layoutHorizontalFINDIP)
        layoutVertical.addLayout(layoutHorizontalFINDURL)


        self.setLayout(layoutVertical)
        self.show()



    def FindByIp(self):
        # Get IP
        IP = self.inputIP.text()
        response = DbIpCity.get(IP, api_key='free')

        # Return
        self.inputIP.setText("")

        self.labelIPx.setText(IP)
        self.labelURLx.setText("Not found...")

        self.labelCITYx.setText(response.city)
        self.labelREGIONx.setText(response.region)
        self.labelCOUNTRYx.setText(response.country)

    def FindByUrl(self):
        self.labelURLx.setText("Working...")

        #Get IP
        url = self.inputURL.text()
        IP = socket.gethostbyname(url)
        response = DbIpCity.get(IP, api_key='free')

        #Return
        self.inputURL.setText("")

        self.labelIPx.setText(IP)
        self.labelURLx.setText(url)

        self.labelCITYx.setText(response.city)
        self.labelREGIONx.setText(response.region)
        self.labelCOUNTRYx.setText(response.country)





while __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IPTracker()
    sys.exit(app.exec())