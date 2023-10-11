# Import wxPython library
import wx
import initialize_data

airports, routes = initialize_data.initialize_data()
locations = sorted(airports['IATA'].tolist())


# Frame Class
class Flight_Frame(wx.Frame):

    # Sets up GUI on initialization
    def __init__(self, *args, **kw):
        super(Flight_Frame, self).__init__(*args, **kw)

        # Creates main GUI panel and vertical sizer
        main_panel = wx.Panel(self)
        main_panel.SetBackgroundColour(wx.Colour(0, 0, 0))
        vbox = wx.BoxSizer(wx.VERTICAL)
        main_panel.SetSizer(vbox)

        # Specifies main GUI font
        font = wx.Font(15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        # Specifies header font
        header_font = wx.Font(24, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Sets up horizontal sizer for second row
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Window title
        window_title = wx.StaticText(main_panel, label="Airport Route Finder")
        window_title.SetFont(font)
        window_title.SetForegroundColour(wx.Colour(255,255,255))
        hbox1.Add(window_title, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Sets up horizontal spacer for third row
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Buffer space
        hbox2.Add((1, 1), 1)

        # Source entry label
        source_entry_label = wx.StaticText(main_panel, label="Enter Source:")
        source_entry_label.SetFont(font)
        source_entry_label.SetForegroundColour(wx.Colour(255, 255, 255))
        hbox2.Add(source_entry_label, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Source entry box
        self.source_selector = wx.ComboBox(main_panel, value="", choices=locations, style=wx.TE_PROCESS_ENTER)
        #self.source_selector.Bind(wx.TE_PROCESS_ENTER, self.enter_source_box)
        self.source_selector.SetFont(font)
        self.source_selector.SetForegroundColour(wx.Colour(255, 255, 255))
        self.source_selector.SetBackgroundColour(wx.Colour(0, 0, 0))
        hbox2.Add(self.source_selector, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Buffer space
        hbox2.Add((1,1), 1)

        # Destination entry label
        dest_entry_label = wx.StaticText(main_panel, label="Enter Destination:")
        dest_entry_label.SetFont(font)
        dest_entry_label.SetForegroundColour(wx.Colour(255, 255, 255))
        hbox2.Add(dest_entry_label, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Buffer space
        hbox2.Add((1, 1), 1)

        # Destination entry box
        self.dest_selector = wx.ComboBox(main_panel, value="", choices=locations, style=wx.TE_PROCESS_ENTER)
        # self.dest_selector.Bind(wx.TE_PROCESS_ENTER, self.enter_dest_box)
        self.dest_selector.SetFont(font)
        self.dest_selector.SetForegroundColour(wx.Colour(255, 255, 255))
        self.dest_selector.SetBackgroundColour(wx.Colour(0, 0, 0))
        hbox2.Add(self.dest_selector, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Buffer space
        hbox2.Add((1, 1), 1)

        # Sets up horizontal spacer for fourth row
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Find button
        find_button = wx.Button(main_panel, label="Find")
        find_button.SetFont(font)
        find_button.SetForegroundColour(wx.Colour(255, 255, 255))
        find_button.SetBackgroundColour(wx.Colour(0,0,0))
        find_button.Bind(wx.EVT_BUTTON, self.click_find_button_wx)
        hbox3.Add(find_button, 1,wx.ALIGN_CENTER_VERTICAL, 100)

        # Sets up horizontal spacer for fifth row
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox4, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Output label
        self.output_label = wx.StaticText(main_panel, label="Awaiting Route...")
        self.output_label.SetFont(font)
        self.output_label.SetForegroundColour(wx.Colour(255, 255, 255))
        hbox4.Add(self.output_label, 1, wx.ALIGN_CENTER_VERTICAL)




    # Event handler for encrypt button
    def click_find_button_wx(self, event):
        self.output_label.SetLabel("Finding Route...")
        self.Layout()
        return

    # Event handler for source box, may be unneccessary
    def enter_source_box(self, event):
        return

    # Event handler for dest box, may be unneccessary
    def enter_dest_box(self, event):
        return


# Creates and starts application Object
front_end = wx.App()
main_frame = Flight_Frame(None, title="Airport Route Finder", size=(800, 600))
main_frame.Show()

# Starts main loop
front_end.MainLoop()

