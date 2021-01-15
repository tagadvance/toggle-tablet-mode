#!/usr/bin/env python3

import os, stat

dir_path = os.path.dirname(os.path.realpath(__file__))

path = os.path.expanduser('~/.local/share/applications/toggle.desktop')
with open(path, 'w') as w:
	w.write("""\
#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=%s/toggle-tablet-mode.py
Name=Toggle Tablet Mode
Comment=Toggle Tablet Mode
Icon=%s/toggle.png
""" % (dir_path, dir_path))
os.chmod(path, stat.S_IREAD | stat.S_IWRITE)

path = os.path.expanduser('~/.local/share/applications/toggle-left.desktop')
with open(path, 'w') as w:
	w.write("""\
#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=%s/toggle-tablet-mode.py left
Name=Toggle Tablet Mode and Rotate Left
Comment=Toggle Tablet Mode and Rotate Left
Icon=%s/toggle-left.png
""" % (dir_path, dir_path))
os.chmod(path, stat.S_IREAD | stat.S_IWRITE)

path = os.path.expanduser('~/.local/share/applications/toggle-right.desktop')
with open(path, 'w') as w:
	w.write("""\
#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=%s/toggle-tablet-mode.py right
Name=Toggle Tablet Mode and Rotate Right
Comment=Toggle Tablet Mode and Rotate Right
Icon=%s/toggle-right.png
""" % (dir_path, dir_path))
os.chmod(path, stat.S_IREAD | stat.S_IWRITE)

path = os.path.expanduser('~/.local/share/applications/toggle-inverted.desktop')
with open(path, 'w') as w:
	w.write("""\
#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=%s/toggle-tablet-mode.py inverted
Name=Toggle Tablet Mode and Invert Display
Comment=Toggle Tablet Mode and Invert Display
Icon=%s/toggle-inverted.png
""" % (dir_path, dir_path))
os.chmod(path, stat.S_IREAD | stat.S_IWRITE)


