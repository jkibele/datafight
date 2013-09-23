Title: KDE Widgets in QT Designer
Date: 2013-09-23
Category: Python
Tags: python, pyqt, qt designer, kde
Slug: kde-widgets-in-qt-designer
Author: Jared Kibele
Summary: I wanted to use a KDE KEditListWidget in a PyQT4 GUI I'm building with QT Designer. I could add the widget just fine but I was getting an import error when tried to run the generated code. I had a bit of difficulty tracking down a solution but it was simple once I figure it out.

I wanted to use a KDE KEditListWidget in a PyQT4 GUI I'm building with QT Designer. I could add the widget just fine but I was getting an import error when tried to run the generated code. I had a bit of difficulty tracking down a solution but it was simple once I figure it out.

The normal procedure here is to use QT Designer to build the GUI, save the .ui file, and then use pyuic4 to convert the file to Python code as described [here](http://pyqt.sourceforge.net/Docs/PyQt4/designer.html). I did that after generating my `.ui` file but the resulting `.py` file had incorrect import statements. It had something like:
```python
    from keditlistwidget import KEditListWidget
```

When it should have had:
```python
    from PyKDE4.kdeui import KEditListWidget
```

After much digging, I found that an older version of pykdeuic4 apparently had [a bug](https://bugs.kde.org/show_bug.cgi?id=183205) that caused this problem. So I did: `sudo apt-get install python-kde4`

Followed by: `sudo apt-get install python-kde4-dev`

Then, `pykdeuic4 -o outfile.py input.ui` rendered the import statements correctly and, magically, so did `pyuic4 -o outfile.py input.ui`. At first, I thought I just had an old version of python-kde4-dev but, I think I may just have not had it at all. I'm a little confused because the QT Designer preview deal worked fine before (and after) and it was just the code generation that was broken. At any rate, using apt-get to install those two packages fixed the problem.
