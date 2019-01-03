'''
class:      AnalogClock
Author(s):  Sam Badger
Date:       January 3, 2018
Description:
            The python adaptation of the example given at:
            http://doc.qt.io/qt-5/qtwidgets-widgets-analogclock-example.html
'''

import sys

from PySide2.QtWidgets import *
from PySide2.QtCore    import *
from PySide2.QtGui     import *

class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        
        self.setWindowTitle("AnalogClock")
        self.resize(200,200)
        
    def paintEvent(self, event):
        # define clock hand shapes
        hourHand = [
            QPoint( 7 , 8 ),
            QPoint(-7 , 8 ),
            QPoint( 0 ,-40)
        ]
        minuteHand = [
            QPoint( 7 , 8 ),
            QPoint(-7 , 8 ),
            QPoint( 0 ,-70)
        ]
        secondHand = [
            QPoint( 3 , 8 ),
            QPoint(-3 , 8 ),
            QPoint( 0 ,-90)
        ]
        
        # define clock hand colors
        hourColor = QColor(127, 0, 127)
        minuteColor = QColor(0, 127, 127, 191)
        secondColor = QColor(127, 127, 0, 127)
        
        # get size of widget and current time
        side = min(self.width(), self.height())
        time = QTime.currentTime()
        
        # set up painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2, self.height()/2)
        painter.scale(side/200.0, side/200.0)
        
        
        # ---------- Draw hours ---------- #
        painter.setPen(Qt.NoPen)
        painter.setBrush(hourColor)
        
        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute()/60 + time.second()/3600)))
        painter.drawConvexPolygon(hourHand)
        painter.restore()
        
        painter.setPen(hourColor)
        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)
            
        # ---------- Draw minutes ---------- #
        painter.setPen(Qt.NoPen)
        painter.setBrush(minuteColor)
        
        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second()/60))
        painter.drawConvexPolygon(minuteHand)
        painter.restore()
        
        painter.setPen(minuteColor)
        for i in range(60):
            if i%5 != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)
            
        # ---------- Draw seconds ---------- #
        painter.setPen(Qt.NoPen)
        painter.setBrush(secondColor)
        
        painter.save()
        painter.rotate(6.0 * (time.second()))
        painter.drawConvexPolygon(secondHand)
        painter.restore()
        
        painter.setPen(secondColor)
        for i in range(60):
            if i%5 != 0:
                painter.drawLine(95, 0, 96, 0)
            painter.rotate(6.0)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = AnalogClock()
    widget.show()
    
    sys.exit(app.exec_())
        
        
        
