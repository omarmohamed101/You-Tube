from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import *
from datetime import timedelta
from googleapiclient.discovery import build
import sys
import os
import re


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(600, 300, 700, 500)
        self.setWindowTitle('Youtube Assistant')
        # youtube icon path if you want to insert icon on the window
        # self.setWindowIcon(QIcon())
        self.setStyleSheet("background-color: black;")

        self.initUi()

    def get_name(self):
        channel = self.textbox.text()

        api_key = os.environ.get('YT_API_KEY')

        youtube = build('youtube', 'v3', developerKey=api_key)

        hours_pattern = re.compile(r'(\d+)H')
        minutes_pattern = re.compile(r'(\d+)M')
        seconds_pattern = re.compile(r'(\d+)S')

        total_seconds = 0
        video_count = 0
        nextPageToken = None
        while True:
            pl_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=channel,
                maxResults=50,
                pageToken=nextPageToken
            )

            pl_response = pl_request.execute()

            vid_ids = []
            for item in pl_response['items']:
                vid_ids.append(item['contentDetails']['videoId'])


            vid_request = youtube.videos().list(
                part="contentDetails",
                id=','.join(vid_ids)
            )

            vid_response = vid_request.execute()

            for item in vid_response['items']:
                duration = item['contentDetails']['duration']

                hours = hours_pattern.search(duration)
                minutes = minutes_pattern.search(duration)
                seconds = seconds_pattern.search(duration)

                hours = int(hours.group(1)) if hours else 0
                minutes = int(minutes.group(1)) if minutes else 0
                seconds = int(seconds.group(1)) if seconds else 0

                video_seconds = timedelta(
                    hours=hours,
                    minutes=minutes,
                    seconds=seconds
                ).total_seconds()

                total_seconds += video_seconds
                video_count += 1

            nextPageToken = pl_response.get('nextPageToken')

            if not nextPageToken:
                break

        total_seconds = int(total_seconds)

        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        self.res.setText(f'Total time: {hours}:{minutes}:{seconds}')
        self.res.adjustSize()

        self.vid_count.setText(f'Videos count: {video_count} video')
        self.vid_count.adjustSize()


    def initUi(self):
        """ contains all the content of the main window """
        self.label = QtWidgets.QLabel(self)
        self.label.move(50, 50)
        self.label.setText('Enter the playlist id:')
        self.label.setFont(QFont('Arial', 20))
        self.label.setStyleSheet("color: #BBD67A;")
        self.label.adjustSize()

        self.vid_count = QtWidgets.QLabel(self)
        self.vid_count.move(200, 200)
        self.vid_count.setStyleSheet("color: #BBD67A;")
        self.vid_count.setFont(QFont('Arial', 20))

        self.res = QtWidgets.QLabel(self)
        self.res.move(200, 250)
        self.res.setStyleSheet("color: #BBD67A;")
        self.res.setFont(QFont('Arial', 20))


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(450, 120, 150, 50)
        # b1.move(500, 120)
        self.b1.setText('search playlist')
        self.b1.setFont(QFont('Arial', 10))
        self.b1.clicked.connect(self.get_name)
        self.b1.setStyleSheet("background-color: #BBD67A;")

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 120, 350, 50)
        self.textbox.setFont(QFont('Arial', 10))
        self.textbox.setStyleSheet("background-color: #BBD67A;")



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()


