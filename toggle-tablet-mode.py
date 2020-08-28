#!/usr/bin/env python3

import os
import re

def main() -> None:
	keyboard_id = get_keyboard()
	touchpad_id = get_touchpad()
	toggle_device(keyboard_id)
	toggle_device(touchpad_id)

def get_keyboard(device: str = 'AT Translated Set 2 keyboard'):
	meta = run('xinput --list | grep "%s"' % device)
	m = re.search('id=(\d+)', meta)
	return m.group(1)

def get_touchpad(device: str = 'Touchpad'):
	meta = run('xinput --list | grep "%s"' % device)
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

def run(command: str) -> str:
	return os.popen(command).read()

if __name__ == '__main__':
    main()
