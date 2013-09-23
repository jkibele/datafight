../configure --prefix=/usr/local/prad_test --with-qtdir=/usr --with-mocpath=/usr/bin/moc-qt4 --with-uicpath=/usr/bin/uic-qt4 --with-qtlibdir=/usr/lib

#QT_IS_DYNAMIC=`ls $QTDIR 2> /dev/null` 
QT_IS_DYNAMIC=`ls $QTDIR/lib/*.so 2> /dev/null`
