#!/usr/bin/env python
import gtk, webkit, sys, getopt, argparse
#
### Thanks go to
#
# Eugene for the argparse hint, it helped me out.  (13/03/2016)
#
###




#INIT
class Go():
    def __init__(self):


    #Defaults for the app
        webpage = 'www.messenger.com'

    #Get metrics
        width = gtk.gdk.screen_width() /4
        height = gtk.gdk.screen_height()
	print width, height

	#Don't show the Browser UI
	showBrowser = False

	#Arguments, before window creation
	#Eugene inspired this monstrosity...

	parser = argparse.ArgumentParser(description='A SSB Python script.')
	parser.add_argument('-s','--site', help='The website to load.',required=True)
	parser.add_argument('-w','--width',help='The display width.', required=False)
	parser.add_argument('-e','--height',help='The display height.', required=False)
	parser.add_argument('-b','--browser',help='Show the Browser UI.', required=False)
	
	args = parser.parse_args()

	## show values ##
	if args.site is not None:
            webpage = args.site
            print webpage
	if args.width is not None:
            width = int(args.width)
            print width
	if args.height is not None:
            height = int(args.height)
            print height
	if args.browser is not None:
		showBrowser == True

       # Create window
        self._window = gtk.Window()
        self._window.set_icon_from_file('icon.png')
        self._window.connect('destroy', lambda w: gtk.main_quit())
	self._window.set_default_size(width, height)

        # Create navigation bar
        self._navigation = gtk.HBox()
	
	#add in code for showing the Browser UI here .. from the command line.
	#default = off


	#This is NOT the right way to do this... but i am tired.
	#Will fix soon.
	if args.browser is not None:
        	self._back = gtk.ToolButton(gtk.STOCK_GO_BACK)
        	self._forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        	self._refresh = gtk.ToolButton(gtk.STOCK_REFRESH)
        	self._address_bar = gtk.Entry()

        	self._back.connect('clicked', self.go_back)
        	self._forward.connect('clicked', self.go_forward)
        	self._refresh.connect('clicked', self.refresh_page)
        	self._address_bar.connect('activate', self.load_page)

        	self._navigation.pack_start(self._back, False)
	        self._navigation.pack_start(self._forward, False)
	        self._navigation.pack_start(self._refresh, False)
        	self._navigation.pack_start(self._address_bar)

        # Create view for webpage
        self._view = gtk.ScrolledWindow()
        self._webview = webkit.WebView()

	#I was not taking in the lack of 'http/s' hence the page would not load
	#re-used code form below, need to make in to a normal sub and call it

        if webpage.startswith('http://') or webpage.startswith('https://'):
            self._webview.open(webpage)
        else:
            webpage = 'http://' + webpage
            self._webview.open(webpage)

        #self._webview.open('webpage')
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