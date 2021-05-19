
from gui_view import GuiView





gui = GuiView()
window = gui.window


def next_card():
    gui.check_button_handler()


window.mainloop()