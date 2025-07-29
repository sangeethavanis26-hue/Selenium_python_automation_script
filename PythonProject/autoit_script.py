import autoit
import time

# autoit.run("notepad.exe")
# time.sleep(1)
# # autoit.win_activate("Untitled - Notepad")
# # autoit.send("Hello from AutoIt!")
# autoit.win_wait("Untitled - Notepad",4)
autoit.control_send("Untitled - Notepad", "RichEditD2DPT1", "Sangeetha from AutoIt!", 0)
# autoit.win_close("Untitled - Notepad")

import autoit
import time

autoit.run("notepad.exe")
autoit.win_wait_active("Untitled - Notepad", 10)
autoit.send("This file was saved automation.")
time.sleep(1)

autoit.send("^s")  # Ctrl + S to open Save dialog
# autoit.win_wait_active("Save As", 5)
autoit.control_set_text("Save As", "Edit1", "C:\\Users\\nithi\\Documents\\my_autoit_file.txt")
time.sleep(1)
autoit.control_click("Save as", "", "Button2")  # Click Save
time.sleep(1)
autoit.win_close("my_autoit_file.txt - Notepad")
