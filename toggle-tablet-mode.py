#!/usr/bin/env python3

import os
import re
from sys import argv

def main() -> None:
    orientation = None if (len(argv) < 2) else argv[1]

    # toggling from inverted to right should not re-enable the input devices
    if orientation is None:
        # default behavior
        toggle_input()
        reset_display_orientation()
    else:
        # we are already in this orientation: reset OR the keyboard is enabled and needs to be disabled
        if is_in_orientation(orientation) or is_input_enabled():
            toggle_input()
        toggle_display_orientation(orientation)

def is_input_enabled() -> bool:
    keyboard_id = get_keyboard()
    return is_enabled(keyboard_id)

def toggle_input() -> None:
    keyboard_id = get_keyboard()
    touchpad_id = get_touchpad()
    toggle_device(keyboard_id)
    toggle_device(touchpad_id)

def get_keyboard(device: str = 'AT Translated Set 2 keyboard'):
    meta = run('xinput --list | grep "%s"' % device)
    m = re.search('id=(\d+)', meta)
    return m.group(1)

def get_touchpad(device: str = 'Touchpad'):
    meta = run('xinput --list | grep -i "%s"' % device)
    m = re.search('id=(\d+)', meta)
    return m.group(1)

def toggle_device(device: str) -> None:
    state = is_enabled(device)
    new_state = state ^ 1
    run('xinput set-prop "%s" "Device Enabled" "%d"' % (device, new_state))

def is_enabled(device: str) -> int:
    meta = run('xinput list-props "%s" | grep "Device Enabled"' % device)
    m = re.search(':\s*(\d+)', meta)
    value = m.group(1)
    return int(value)

def is_in_orientation(orientation: str) -> bool:
    current_orientation = get_orientation()
    return current_orientation == orientation

def toggle_display_orientation(orientation: str) -> None:
    set_display_orientation('normal' if is_in_orientation(orientation) else orientation)

def get_orientation() -> str:
    return run('xrandr --query --verbose | grep "eDP" | cut -d " " -f 6').strip()

def set_display_orientation(orientation: str) -> None:
    run('xrandr -o %s' % orientation)

def reset_display_orientation() -> int:
    set_display_orientation('normal')

def run(command: str) -> str:
    return os.popen(command).read()

if __name__ == '__main__':
    main()
