from gi.repository import Gtk
from console import read_grub, write_grub
import settings


class GrubbitrMainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grubbitr")
        self.connect("delete-event", Gtk.main_quit)        

        self.main_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        self.add(self.main_box)

        read_button = Gtk.Button(label="Read grub.cfg")
        read_button.connect("clicked", self.read_button_click)
        self.main_box.pack_start(read_button, True, True, 30)


        # TreeView list of operatings systems start.
        self.os_names = []

        self.os_list = Gtk.ListStore(str)
        for os_name in self.os_names: self_os_list.append([os_name])
        
        self.os_view = Gtk.TreeView(model=self.os_list)

        renderer_os_text = Gtk.CellRendererText()
        renderer_os_text.set_property("editable", True)
        renderer_os_text.connect("edited", self.rename)
        
        os_names_column = Gtk.TreeViewColumn("Operating Systems", renderer_os_text, text=0)
        self.os_view.append_column(os_names_column)
        
#       renderer_os_text.connect("edited", self.os_rename)

        self.main_box.pack_start(self.os_view, True, True, 30)
        # TreeView list of operating systems end.

        
        # Write Button
        write_button = Gtk.Button(label="Save Changes")
        write_button.connect("clicked", self.write_button_click)
        self.main_box.pack_start(write_button, True, True, 30)

    def read_button_click(self, widget):
        if len(self.os_list) != 0:
            self.os_list.clear()
            self.os_names = []
            self.os_lines = []
            self.os_dictionary = {}

        os_token = read_grub.get_full_info(settings.grub_directory + "test.cfg")
        self.os_lines, self.os_names, self.os_dictionary = os_token
        self.os_lines = write_grub.create_clean_config(self.os_lines)



        # Updating self.os_view to display changes.
        for os_name in self.os_names: self.os_list.append([os_name])


    def rename(self, widget, path, text):
        old_name = self.os_list[path][0]
        self.os_list[path][0] = text
        self.os_names[int(path)] = text 
        # For some reason, path is a string of the index, not ana int.

        self.os_dictionary[text] = self.os_dictionary.pop(old_name)
        self.os_dictionary[text].change_name(text)
         
    def write_button_click(self, widget):
        write_grub.write_to_file(self.os_lines, self.os_names,
                 self.os_dictionary, settings.grub_directory + "test.cfg")

if __name__ == "__main__":
    main_window = GrubbitrMainWindow()
    main_window.show_all()
    Gtk.main()
