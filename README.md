# ClipLoop V1

**ClipLoop V1** is a simple Python-based message loop tester built for sending repeated clipboard-based text into your **own app, test textbox, local chat UI, form field, or automation testing environment**.

It uses `pyautogui` to paste text, `pyperclip` to manage clipboard content, and `keyboard` to detect the `ESC` stop key.

> This project is designed for personal testing, UI testing, and controlled automation only.

---

## Important Notice

ClipLoop must only be used on:

* Your own application
* Your own local textbox
* Your own test chat UI
* Your own form/input field
* A controlled testing environment where you have permission

Do **not** use this tool for spam, harassment, flooding chats, bypassing platform limits, or sending unwanted messages to other people or services.

The developer is not responsible for misuse of this tool.

---

## Features

* Clipboard-based message sending
* Fast paste method using `Ctrl + V`
* Optional automatic `Enter` after every message
* Custom message input
* Custom interval/speed
* Runtime limit in hours
* Unlimited mode until stopped
* Countdown before starting
* Status counter after a selected number of messages
* ESC key stop support
* PyAutoGUI emergency fail-safe
* Clipboard restore after script ends
* Windows Unicode console setup
* Simple terminal-based interface
* MIT licensed

---

## How It Works

ClipLoop copies your selected message to the clipboard, waits for a countdown, then repeatedly pastes that message into the currently active textbox.

The script does **not** send messages in the background by itself. It works on the currently focused input field.

For example:

1. Run the script.
2. Enter your message.
3. Select interval and runtime.
4. Open your own app textbox.
5. Wait for countdown.
6. ClipLoop starts pasting and optionally pressing Enter.

---

## Project Name

Current name:

```text
ClipLoop V1
```

Meaning:

* **Clip** = clipboard
* **Loop** = repeated loop sending/testing

---

## Requirements

You need Python installed on your system.

Recommended Python version:

```text
Python 3.9+
```

Required Python packages:

```text
pyautogui
pyperclip
keyboard
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/doncryptico/cliploop.git
cd cliploop
```

---

### 2. Install Dependencies

```bash
pip install pyautogui pyperclip keyboard
```

On some systems, use:

```bash
python -m pip install pyautogui pyperclip keyboard
```

or:

```bash
py -m pip install pyautogui pyperclip keyboard
```

---

## Usage

Run the script:

```bash
python cliploop.py
```

or on Windows:

```bash
py cliploop.py
```

The script will ask you for:

```text
Enter message to send:
Enter interval in seconds:
Enter runtime hours:
Press Enter after every message?
Countdown seconds before start:
Show status after how many messages:
```

After entering all settings, open your own textbox before the countdown ends.

---

## Example Settings

### Stable Testing

```text
Interval: 1.0
Runtime: 1
Press Enter: Yes
Countdown: 5
Status every: 100
```

This sends one message every second for one hour.

---

### Faster Testing

```text
Interval: 0.5
Runtime: 2
Press Enter: Yes
Countdown: 5
Status every: 100
```

This sends one message every half second for two hours.

---

### Unlimited Mode

For unlimited mode, enter:

```text
unlimited
```

or:

```text
0
```

when asked for runtime hours.

The script will keep running until you stop it with `ESC`, `Ctrl + C`, or PyAutoGUI fail-safe.

---

## Controls

### Stop with ESC

Press:

```text
ESC
```

to stop the script.

---

### Emergency Stop

Move your mouse to the **top-left corner** of the screen.

This triggers PyAutoGUI fail-safe and stops the script.

---

### Manual Stop

You can also stop from the terminal using:

```text
Ctrl + C
```

---

## Settings Explanation

### Message

The text that will be copied to your clipboard and pasted repeatedly.

Example:

```text
Hello, this is a test message.
```

---

### Interval

The delay between each message.

Examples:

```text
1.0  = one message every second
0.5  = two messages per second
0.25 = very fast
```

The script has a minimum allowed interval of:

```text
0.2 seconds
```

This helps prevent accidental system lag.

---

### Runtime Hours

How long the script should run.

Examples:

```text
1    = 1 hour
2.5  = 2 hours and 30 minutes
13   = 13 hours
```

For unlimited mode, use:

```text
unlimited
none
0
u
```

---

### Press Enter After Every Message

When enabled, the script does this:

```text
Paste message
Press Enter
Wait interval
Repeat
```

When disabled, it only pastes the message but does not press Enter.

---

### Countdown Seconds

This gives you time to open your own textbox before the loop starts.

Default:

```text
5 seconds
```

---

### Status Every

This controls how often the script prints progress.

Example:

```text
Status every: 100
```

means the terminal will show a status update after every 100 sent messages.

Example output:

```text
Sent: 100 | Runtime: 00:01:40
Sent: 200 | Runtime: 00:03:20
```

Using a higher number can reduce terminal output and improve smoothness.

---

## Safety Features

ClipLoop includes multiple safety features:

### 1. ESC Stop

The script checks if `ESC` is pressed and stops safely.

---

### 2. PyAutoGUI Fail-Safe

This line enables the emergency mouse fail-safe:

```python
pyautogui.FAILSAFE = True
```

Move the mouse to the top-left corner of the screen to stop instantly.

---

### 3. Runtime Limit

You can set a fixed runtime so the script does not run forever.

---

### 4. Clipboard Restore

Before starting, ClipLoop saves your old clipboard content.

After the script ends, it tries to restore your old clipboard.

---

### 5. Minimum Interval

The script blocks extremely low intervals below `0.2` seconds to avoid accidental lag.

---

## Recommended Usage

Use ClipLoop for:

* Local UI testing
* Chat input testing
* Form input testing
* Clipboard paste testing
* Your own desktop app testing
* Your own Python/PySide/Tkinter app testing
* Repeated message behavior testing
* Button/input stress testing in controlled environments

Do not use ClipLoop for:

* Spamming people
* Flooding WhatsApp, Telegram, Discord, Instagram, Facebook, or other platforms
* Sending unwanted messages
* Bypassing rate limits
* Harassment
* Automated abuse
* Any activity without permission

---

## Known Limitations

### It Is Not a True Background Sender

ClipLoop uses `pyautogui`, so it works with the currently active window.

That means:

* The textbox must be focused
* The target app must be visible or active
* It cannot directly send messages to minimized apps
* It cannot safely control multiple apps at once

---

### It Uses Clipboard

The script copies your message to the clipboard.

During runtime, your clipboard will contain the message being sent.

After stopping, the script tries to restore your old clipboard content.

---

### ESC May Need Permissions

The `keyboard` module may require extra permissions on some systems.

On Windows, it usually works normally.

On Linux, it may require running with permission depending on your environment.

---

### Very Fast Speed Can Cause Lag

Intervals like:

```text
0.2
0.25
0.3
```

can be heavy depending on your system and target app.

For stable use, prefer:

```text
0.5
1.0
2.0
```

---

## Troubleshooting

### ANSI Color Codes Showing Like `[91m`

Some terminals do not support ANSI color escape codes.

Example problem:

```text
[91m@doncryptico[0m
```

This usually happens in terminals that do not render colors properly, such as some Code Runner output panels.

Recommended fix:

Run the script in a real terminal instead of the VS Code output panel.

In VS Code:

1. Open the file.
2. Right-click inside the file.
3. Choose **Run Python File in Terminal**.

Do not use only the Code Runner output window if it shows escape codes.

---

### Cannot Edit in Read-Only Editor

This is usually a VS Code issue, not a Python issue.

Possible fixes:

1. Open the actual `.py` file from your project folder.
2. Do not edit the output/log panel.
3. Use **File > Open Folder** and open your project folder.
4. Save the script as:

```text
cliploop.py
```

5. Edit the file from Explorer sidebar.

---

### Script Does Not Stop with ESC

Try these alternatives:

```text
Ctrl + C
```

or move your mouse to the top-left corner.

If `ESC` still does not work, try running the terminal as administrator on Windows.

---

### Message Is Not Pasting

Check these things:

* The textbox is focused.
* Clipboard permission is working.
* You are not clicking somewhere else during countdown.
* The target app accepts `Ctrl + V`.
* Try increasing the interval.

---

### Messages Are Too Fast

Increase interval.

Example:

```text
1.0
```

or:

```text
2.0
```

---

### Terminal Shows Unicode Error

The script already tries to fix Unicode output on Windows using:

```python
chcp 65001
```

and:

```python
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
```

If your terminal still has problems, use a normal ASCII header instead of special Unicode text.

---



```bash
pip install -r requirements.txt
```

---

## Example Terminal Output

```text
ClipLoop V1
Use only on your own app/test textbox.

Enter message to send: Hello test
Enter interval in seconds [0.5]: 1
Enter runtime hours, example 13, or type unlimited [13]: 1
Press Enter after every message? [Y/n]: y
Countdown seconds before start [5]: 5
Show status after how many messages [100]: 100

Current Settings
----------------
Message length : 10 characters
Interval       : 1.0 seconds
Runtime        : 1.0 hours
Enter sending  : True
Status every   : 100 messages

Open your own app textbox. Starting in 5 seconds.
Press ESC anytime to stop.
Move mouse to TOP-LEFT corner for emergency stop.

Running...
Press ESC to stop.
Move mouse to TOP-LEFT corner for emergency stop.
```

---

## Development Notes

ClipLoop is intentionally simple.

Main modules used:

```python
pyautogui
pyperclip
keyboard
time
sys
os
```

Main functions:

```python
setup_console()
print_header()
ask_text()
ask_float()
ask_int()
ask_yes_no()
stop_requested()
format_time()
countdown()
send_message()
get_user_settings()
print_summary()
main()
```

---

## Future Improvements

Possible future versions may include:

* GUI version
* Dark theme interface
* Save/load presets
* Safer test mode
* Logs export
* Dry-run mode
* Better terminal color handling
* Config file support
* One-click start/stop button
* Custom hotkey support
* Better Linux compatibility
* App-specific testing mode

---

## Legal and Ethical Use

This project is for educational and testing purposes only.

You are responsible for how you use this software.

By using ClipLoop, you agree that:

* You will only use it where you have permission.
* You will not use it for spam.
* You will not use it to harass people.
* You will not use it to abuse online services.
* You will follow the rules of the platforms and systems you interact with.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## MIT License Notice

```text
MIT License

Copyright (c) 2026 Don Cryptico

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
---

## Author

**Don Cryptico**

Website:

```text
http://doncryptico.gt.tc/
```

GitHub:

```text
https://github.com/doncryptico
```

---

## Disclaimer

ClipLoop is provided as-is.

The author does not support or encourage misuse of this software. This tool should only be used for legal, ethical, and permitted testing purposes.

If you use this tool on third-party platforms or people without permission, you are fully responsible for the consequences.
