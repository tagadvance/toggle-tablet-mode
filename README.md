# @[toggle icon](toggle.png) Toggle Tablet Mode -- Ubuntu on an ENVY x360

## What's this?
This is a script for 2-in-1 laptops. It disables the keyboard and touchpad on my HP Envy x360 by tapping an icon in my dock.

## Installation
```bash
mkdir -p ~/git; cd ~/git; git clone git@github.com:tagadvance/envy-x360.git
cd envy-x360
# create shortcut
./install-desktop.py
```

Finally, add the toggle button to your dock/favorites. Tap the icon to disable or reenable your keyboard and touchpad.

## Inspiration
The following two Ask Ubuntu questions served as the inspiration for this script.
 
* [Switch into tablet mode (in Gnome)](https://askubuntu.com/questions/716501/switch-into-tablet-mode-in-gnome/739091)
* [Can I make my keyboard disable / enter tablet mode when folding back my display?](https://askubuntu.com/questions/867350/can-i-make-my-keyboard-disable-enter-tablet-mode-when-folding-back-my-display)
