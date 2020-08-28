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
os.chmod(path, stat.S_IREAD | stat.S_IWRITE);
