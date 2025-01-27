# battery-alert
A Python script that alerts users with a dialog box and sound when their laptop battery is above 90% while charging or below 25% while not charging. Perfect for battery health management!

# Battery Alert 🚨

A Python script that alerts users with a dialog box and sound when their laptop battery is:
- **Above 90% while charging** (to unplug the charger).
- **Below 25% while not charging** (to plug in the charger).

---

## Features ✨
- **Dialog Box Alerts**: Displays a styled dialog box with a message when the battery level crosses the threshold.
- **Sound Notifications**: Plays custom sounds (`more.wav` and `less.wav`) to grab your attention.
- **Windows Compatibility**: Built for Windows using `winsound` for audio and `tkinter` for the GUI.
- **Customizable**: Easily adjust the battery percentage thresholds and sound files.

---

## Why I Made This? 🤔
I created this script to help users maintain their laptop battery health. Constantly overcharging or draining the battery can reduce its lifespan. This tool ensures you are alerted at the right time to take action.

---

## How Can This Help You? 💡
- **Improve Battery Health**: Avoid overcharging or deep discharging your laptop battery.
- **Stay Alert**: Get notified with both visual and sound alerts.
- **Customizable Alerts**: Change the sound files or thresholds to suit your needs.

---

## Prerequisites 🛠️
- **Python 3.x**: Install Python from [python.org](https://www.python.org/).
- **Required Libraries**: Install the `psutil` library.
  ```bash
  pip install psutil
