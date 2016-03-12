#!/usr/bin/env python
import gtk, webkit, sys, getopt, argparse

webpage = 'www.messenger.com'



#INIT
class Go():
    def __init__(self):



       # Create window
        for arg in sys.argv:
            webpage = str(sys.argv[1])


        self._window = gtk.Window()
        self._window.set_icon_from_file('icon.png')
        self._window.connect('destroy', lambda w: gtk.main_quit())
        self._window.set_default_size(560, 900)

        # Create navigation bar
        self._navigation = gtk.HBox()

        #self._back = gtk.ToolButton(gtk.STOCK_GO_BACK)
        #self._forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        #self._refresh = gtk.ToolButton(gtk.STOCK_REFRESH)
        #self._address_bar = gtk.Entry()

        #self._back.connect('clicked', self.go_back)
        #self._forward.connect('clicked', self.go_forward)
        #self._refresh.connect('clicked', self.refresh_page)
        #self._address_bar.connect('activate', self.load_page)

        #self._navigation.pack_start(self._back, False)
        #self._navigation.pack_start(self._forward, False)
        #self._navigation.pack_start(self._refresh, False)
        #self._navigation.pack_start(self._address_bar)

        # Create view for webpage
        self._view = gtk.ScrolledWindow()
        self._webview = webkit.WebView()
        self._webview.open('http://www.messenger.com/login')
        #self._webview.open(str(webpage))
        print 'requested site: ',webpage
        self._webview.connect('title-changed', self.change_title)
        self._webview.connect('load-committed', self.change_url)
        self._view.add(self._webview)

        # Add everything and initialize
        self._container = gtk.VBox()
        self._container.pack_start(self._navigation, False)
        self._container.pack_start(self._view)

        self._window.add(self._container)
        self._window.show_all()
        gtk.main()

    def load_page(self, widget):
        _add = self._address_bar.get_text()
        if _add.startswith('http://') or _add.startswith('https://'):
            self._webview.open(_add)
        else:
            _add = 'http://' + _add
            self._address_bar.set_text(_add)
            self._webview.open(_add)

    def change_title(self, widget, frame, title):
        self._window.set_title(':: ' + webpage)

    def change_url(self, widget, frame):
        uri = frame.get_uri()
        self._address_bar.set_text(uri)

    def go_back(self, widget):
        self._webview.go_back()

    def go_forward(self, widget):
        self._webview.go_forward()

    def refresh_page(self, widget):
        self._webview.reload()

init = Go()
#Need to get screen res and do /4 width and set screen as height at init
#self.much_window.set_default_size((gtk.gdk.screen_width()/4,gtk.gdk.screen_height())
