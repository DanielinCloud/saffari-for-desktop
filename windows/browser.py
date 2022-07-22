from gi.repository import Gtk, Gio, GLib, Gdk, GObject, WebKit2

class Browser(Gtk.Window):
    def __init__(self):
        super().__init__(title="Saffari for Decstopp")
        self.set_size_request(200, 100)
        self.set_border_width(10)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        self.set_titlebar(hb)

        topbar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        backbtnbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(backbtnbox.get_style_context(), "linked")

        button = Gtk.Button()
        button.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        backbtnbox.add(button)

        button = Gtk.Button()
        button.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT, shadow_type=Gtk.ShadowType.NONE)
        )
        backbtnbox.add(button)

        topbar.pack_start(backbtnbox, True, True, 0)

        urlbar = Gtk.Entry()
        urlbar.set_text("Hello World")
        topbar.pack_start(urlbar, True, True, 0)

        hb.pack_start(topbar)

        webView = WebKit2.WebView()
        self.add(webView)
        GLib.idle_add(webView.load_uri, 'http://www.google.com')