import pyautogui
import pyperclip
import keyboard
import time
import sys
import os

# =========================
# CLIPLOOP V1
# Own App Message Tester
# =========================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.005


# =========================
# CONSOLE / HEADER
# =========================

def setup_console():
    """
    Fix Unicode printing error on Windows terminals.
    """
    try:
        if os.name == "nt":
            os.system("chcp 65001 > nul")
    except Exception:
        pass

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def print_header():
    setup_console()

    green = "\033[92m"
    red = "\033[91m"
    blue = "\033[94m"
    yellow = "\033[93m"
    reset = "\033[0m"

    try:
        print(f"{green}╔════════════════════════════════╗")
        print(f"║    𝑫 𝒐 𝒏  𝑪 𝒓 𝒚 𝒑 𝒕 𝒊 𝒄 𝒐      ║")
        print(f"╚════════════════════════════════╝{reset}")
        print(f"{red}@doncryptico{reset}")
        print(f"{red}𝚅𝚒𝚜𝚒𝚝: http://doncryptico.gt.tc/{reset}")
        print()
        print(f"{blue}𝗖𝗹𝗶𝗽𝗟𝗼𝗼𝗽 𝗩𝟭{reset}")
        print(f"{yellow}Use only on your own app/test textbox.{reset}")
        print()

    except UnicodeEncodeError:
        print(f"{green}+================================+")
        print("|        Don Cryptico            |")
        print(f"+================================+{reset}")
        print(f"{red}@doncryptico{reset}")
        print(f"{red}Visit: http://doncryptico.gt.tc/{reset}")
        print()
        print(f"{blue}ClipLoop V1{reset}")
        print(f"{yellow}Use only on your own app/test textbox.{reset}")
        print()


# =========================
# INPUT HELPERS
# =========================

def ask_text(prompt, default=None):
    if default is None:
        return input(prompt).strip()

    value = input(f"{prompt} [{default}]: ").strip()

    if value == "":
        return str(default)

    return value


def ask_float(prompt, default, minimum=None):
    while True:
        value = ask_text(prompt, default)

        try:
            number = float(value)

            if minimum is not None and number < minimum:
                print(f"Value too low. Minimum allowed is {minimum}.")
                continue

            return number

        except ValueError:
            print("Invalid number. Try again.")


def ask_int(prompt, default, minimum=None):
    while True:
        value = ask_text(prompt, default)

        try:
            number = int(value)

            if minimum is not None and number < minimum:
                print(f"Value too low. Minimum allowed is {minimum}.")
                continue

            return number

        except ValueError:
            print("Invalid number. Try again.")


def ask_yes_no(prompt, default=True):
    default_text = "Y" if default else "N"

    while True:
        value = input(f"{prompt} [{default_text}/n]: ").strip().lower()

        if value == "":
            return default

        if value in ["y", "yes"]:
            return True

        if value in ["n", "no"]:
            return False

        print("Please enter y or n.")


# =========================
# CORE FUNCTIONS
# =========================

def stop_requested():
    try:
        return keyboard.is_pressed("esc")
    except Exception:
        return False


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def countdown(seconds):
    print()
    print(f"Open your own app textbox. Starting in {seconds} seconds.")
    print("Press ESC anytime to stop.")
    print("Move mouse to TOP-LEFT corner for emergency stop.")
    print()

    for remaining in range(seconds, 0, -1):
        if stop_requested():
            print("Stopped before starting.")
            sys.exit(0)

        print(f"Starting in {remaining}...")
        time.sleep(1)


def send_message(send_with_enter):
    pyautogui.hotkey("ctrl", "v", interval=0)

    if send_with_enter:
        pyautogui.press("enter")


def get_user_settings():
    message = input("Enter message to send: ").strip()

    if not message:
        print("Error: message cannot be empty.")
        sys.exit(1)

    print()
    print("Speed examples:")
    print("1.0  = stable")
    print("0.5  = fast")
    print("0.25 = very fast, only if your own app can handle it")
    print()

    interval = ask_float(
        prompt="Enter interval in seconds",
        default=0.5,
        minimum=0.2
    )

    runtime_input = ask_text(
        prompt="Enter runtime hours, example 13, or type unlimited",
        default="13"
    ).lower()

    if runtime_input in ["unlimited", "none", "0", "u"]:
        run_hours = None
    else:
        try:
            run_hours = float(runtime_input)

            if run_hours <= 0:
                run_hours = None

        except ValueError:
            print("Invalid runtime. Using unlimited mode.")
            run_hours = None

    send_with_enter = ask_yes_no(
        prompt="Press Enter after every message?",
        default=True
    )

    countdown_seconds = ask_int(
        prompt="Countdown seconds before start",
        default=5,
        minimum=1
    )

    status_every = ask_int(
        prompt="Show status after how many messages",
        default=100,
        minimum=1
    )

    return {
        "message": message,
        "interval": interval,
        "run_hours": run_hours,
        "send_with_enter": send_with_enter,
        "countdown_seconds": countdown_seconds,
        "status_every": status_every,
    }


def print_summary(settings):
    print()
    print("Current Settings")
    print("----------------")
    print(f"Message length : {len(settings['message'])} characters")
    print(f"Interval       : {settings['interval']} seconds")

    if settings["run_hours"] is None:
        print("Runtime        : Unlimited until ESC")
    else:
        print(f"Runtime        : {settings['run_hours']} hours")

    print(f"Enter sending  : {settings['send_with_enter']}")
    print(f"Status every   : {settings['status_every']} messages")
    print()


# =========================
# MAIN PROGRAM
# =========================

def main():
    print_header()

    settings = get_user_settings()
    print_summary(settings)

    old_clipboard = ""

    try:
        try:
            old_clipboard = pyperclip.paste()
        except Exception:
            old_clipboard = ""

        pyperclip.copy(settings["message"])

        countdown(settings["countdown_seconds"])

        start_time = time.perf_counter()
        next_send_time = start_time
        sent = 0

        if settings["run_hours"] is None:
            end_time = None
        else:
            end_time = start_time + (settings["run_hours"] * 60 * 60)

        print()
        print("Running...")
        print("Press ESC to stop.")
        print("Move mouse to TOP-LEFT corner for emergency stop.")
        print()

        while True:
            now = time.perf_counter()

            if stop_requested():
                print("\nStopped by ESC key.")
                break

            if end_time is not None and now >= end_time:
                print("\nFinished scheduled runtime.")
                break

            send_message(settings["send_with_enter"])
            sent += 1

            if sent % settings["status_every"] == 0:
                elapsed = time.perf_counter() - start_time
                print(f"Sent: {sent} | Runtime: {format_time(elapsed)}")

            next_send_time += settings["interval"]

            while True:
                now = time.perf_counter()
                remaining = next_send_time - now

                if stop_requested():
                    print("\nStopped by ESC key.")
                    elapsed = time.perf_counter() - start_time
                    print(f"Total sent: {sent}")
                    print(f"Runtime: {format_time(elapsed)}")
                    return

                if remaining <= 0:
                    break

                time.sleep(min(0.03, remaining))

        elapsed = time.perf_counter() - start_time

        print()
        print("Done.")
        print(f"Total sent: {sent}")
        print(f"Runtime: {format_time(elapsed)}")

    except pyautogui.FailSafeException:
        print("\nEmergency stopped: mouse moved to top-left corner.")

    except KeyboardInterrupt:
        print("\nStopped manually with Ctrl + C.")

    finally:
        try:
            pyperclip.copy(old_clipboard)
        except Exception:
            pass


if __name__ == "__main__":
    main()
