# ClipLoop V1

**ClipLoop V1** is a lightweight Python clipboard loop tester for sending repeated text into your own app, textbox, form field, or controlled testing environment.

It uses `pyautogui` for keyboard automation, `pyperclip` for clipboard handling, and `keyboard` for ESC stop detection.

> Use only on systems, apps, and text fields you own or have permission to test.

---

## Features

* Clipboard-based fast paste
* Custom message input
* Custom interval/speed
* Optional `Enter` after each paste
* Runtime limit or unlimited mode
* Countdown before start
* Status updates
* ESC stop support
* PyAutoGUI fail-safe support
* Clipboard restore after exit
* Windows Unicode console support

---

## Requirements

* Python 3.9+
* `pyautogui`
* `pyperclip`
* `keyboard`

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/doncryptico/cliploop.git
cd cliploop
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run the tool:

```bash
python cliploop.py
```

On Windows, you can also use:

```bash
py cliploop.py
```

---

## Kali Linux Setup

If Kali shows `externally-managed-environment`, use a virtual environment:

```bash
sudo apt update
sudo apt install python3-venv python3-pip python3-tk xclip xsel scrot -y

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python cliploop.py
```

---

## Usage

After running the script, enter:

```text
Enter message to send
Enter interval in seconds
Enter runtime hours
Press Enter after every message
Countdown seconds before start
Show status after how many messages
```

Then open your own textbox before the countdown ends.

Example settings:

```text
Interval: 1.0
Runtime: 1
Press Enter: Yes
Countdown: 5
Status every: 100
```

For unlimited mode, enter:

```text
unlimited
```

or:

```text
0
```

---

## Controls

Stop the script using:

```text
ESC
```

or:

```text
Ctrl + C
```

Emergency stop:

```text
Move mouse to the top-left corner
```

---

## Important Notes

ClipLoop is not a background sender. It works only on the currently focused textbox.

The target textbox must be active, visible, and able to receive `Ctrl + V`.

Very low intervals may cause lag. Recommended stable values:

```text
0.5
1.0
2.0
```

---

## Ethical Use

ClipLoop is made for:

* Personal testing
* Local app testing
* UI input testing
* Form testing
* Controlled automation testing

Do not use ClipLoop for:

* Spam
* Harassment
* Flooding chats
* Sending unwanted messages
* Bypassing platform limits
* Automating abuse on third-party services

You are responsible for how you use this tool.

---

## License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

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

ClipLoop is provided as-is. The author is not responsible for misuse, damage, account restrictions, or consequences caused by improper use of this software.
