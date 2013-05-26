from gi.repository import Gtk
from console import read_grub, write_grub
import settings


class GrubbitrMainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grubbitr")
        self.connect("delete-event", Gtk.main_quit)        

        read_button = Gtk.Button(label="Read grub.cfg")
        read_button.connect("clicked", self.read_button_click)

        # TreeView list of operatings systems start.
        self.os_names = ["","","","", ""]

        self.os_list = Gtk.ListStore(str)
        for os_name in self.os_names: self.os_list.append([os_name])
        
        self.os_view = Gtk.TreeView(model=self.os_list)

        renderer_os_text = Gtk.CellRendererText()
        renderer_os_text.set_property("editable", True)
        renderer_os_text.connect("edited", self.rename)
        
        self.os_names_column = Gtk.TreeViewColumn("Operating Systems", 
                                                   renderer_os_text, text=0)
        self.os_view.append_column(self.os_names_column)
    
        # Allows multiple rows to be selected.
        self.selection = self.os_view.get_selection()
        self.selection.set_mode(Gtk.SelectionMode.MULTIPLE)
        # TreeView list of operating systems end.

        # Write Button
        write_button = Gtk.Button(label="Save Changes")
        write_button.connect("clicked", self.write_button_click)
        # END

            
        # Up Switch Button
        up_switch_button = Gtk.Button(label="Move Up")
        up_switch_button.connect("clicked", self.switch_up)
    
        # Down Switch Button
        down_switch_button = Gtk.Button(label="Move Down")
        down_switch_button.connect("clicked", self.switch_down)

        test_button = Gtk.Button(label="Test Something!")
        test_button.connect("clicked", self.test)

        # Placing everything in a grid.
        grid = Gtk.Grid()
        grid.insert_column(0)
        grid.attach(read_button, 1, 0, 1, 1)
        grid.attach(self.os_view, 1, 1, 1, 1)
        grid.attach(write_button, 1, 6, 1, 1)
    
        left_column = Gtk.Box()
        grid.attach(left_column, 0, 0, 1, 3)
        self.add(grid)
        # Grid placement end.

        grid.attach(up_switch_button, 2, 1, 1, 1)
        grid.attach(down_switch_button, 2, 2, 1, 1)
        grid.attach(test_button, 2, 3, 1, 1)
        
    def read_button_click(self, widget):
        if len(self.os_list) != 0:
            self.os_list.clear()
            self.os_names = []
            self.os_lines = []
            self.os_dictionary = {}

        os_token = read_grub.get_full_info(settings.grub_directory + "test.cfg")
        self.os_lines, self.os_names, self.os_dictionary = os_token

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


    def switch_up(self, widget):
        currently_selected = self.selection.get_selected_rows()
        current_path = currently_selected[1][0]

        print self.os_list[current_path][0]
        if self.os_names[current_path][0] != self.os_names[0][0]:
            print "yeah"
            above_path = current_path + 1
            print self.os_list[above_path][0]

    def switch_down(self, widget):
        pass
    
    def test(self, widget):
        currently_selected = self.selection.get_selected_rows()

        if len(currently_selected[1]) == 2:
            current_path = currently_selected[1][0]
            above_path = currently_selected[1][1]

            current_iter = self.os_list.get_iter(current_path)
            above_iter = self.os_list.get_iter(above_path)       

            self.os_list.swap(current_iter, above_iter)
            i, j  = int(str(current_path)), int(str(above_path))
            self.os_names[i], self.os_names[j] = self.os_names[j], self.os_names[i]

        elif len(currently_selected[1]) == 1:
            current_path = currently_selected[1][0]
            print current_path





if __name__ == "__main__":
    main_window = GrubbitrMainWindow()
    main_window.show_all()
    Gtk.main()
