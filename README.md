# Toggle Tablet Mode -- Ubuntu on an ENVY x360

## What's this?
This is a script for 2-in-1 laptops. It allows one to disable/reenable the keyboard and touchpad. It was specifically designed to run on an HP ENVY x360; however, it should work on any HP 2-in-1 running Ubuntu 20+. Your mileage may vary!

## Installation
```bash
mkdir -p ~/git; cd ~/git; git clone git@github.com:tagadvance/toggle-tablet-mode.git
cd toggle-tablet-mode
# create shortcut
./install-desktop.py
```

Finally, add the toggle button to your dock/favorites. Tap the icon to disable or reenable your keyboard and touchpad.

![toggle icon](toggle.png)

## Inspiration
The following two Ask Ubuntu questions served as the inspiration for this script.
 
* [Switch into tablet mode (in Gnome)](https://askubuntu.com/questions/716501/switch-into-tablet-mode-in-gnome/739091)
* [Can I make my keyboard disable / enter tablet mode when folding back my display?](https://askubuntu.com/questions/867350/can-i-make-my-keyboard-disable-enter-tablet-mode-when-folding-back-my-display)
