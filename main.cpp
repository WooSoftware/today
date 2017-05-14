#include "mainwindow.h"
#include <QApplication>
#include <QtGui>
#include <QDesktopWidget>


int main(int argc, char *argv[]){

   QApplication::setStyle("cleanlooks");

   QApplication a(argc, argv);
   MainWindow w;
   w.setWindowFlags(Qt::FramelessWindowHint | Qt::WindowStaysOnBottomHint);
   w.setWindowOpacity(0);
//   w.setWindowFlags(Qt::FramelessWindowHint|Qt::WindowStaysOnTopHint|Qt::Tool);
   w.setAttribute(Qt::WA_TranslucentBackground);
   w.show();

   QPropertyAnimation *animation = new QPropertyAnimation(&w, "windowOpacity");
   animation->setDuration(1500);
   animation->setStartValue(w.windowOpacity());
   animation->setEndValue(0.6);
   animation->start();
   QDesktopWidget * d = qApp->desktop();
   int sw = d->width();
   int sh = d->height();
   int tw = w.width();
   int th = w.height();
   w.move(sw - tw - 10, sh - th - 70);

   return a.exec();
}
