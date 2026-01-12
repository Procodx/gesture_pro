# 🖱️ GesturePro: AI-Powered Virtual Mouse

GesturePro is a high-performance, "No-Hardware" virtual mouse solution built using Python, OpenCV, and MediaPipe. It allows users to control their Windows PC entirely through hand gestures via a standard webcam.

Designed for developers and power users who want a "Stealth Mode" or a hands-free navigation experience.

## ✨ Features

- **Precision Mouse Tracking:** Smooth cursor movement using a weighted moving average algorithm.
- **Joystick Scrolling:** Proportional scrolling speed based on hand height—move higher to scroll faster.
- **Stealth Mode (Boss Key):** Quickly minimize all windows with a full-palm spread gesture.
- **Smart Zoom:** Rockstar sign (🤘) triggers a virtual zoom lens (Ctrl +/-) for browsers and IDEs.
- **Screenshot Peace Sign:** Capture your screen instantly with a peace sign gesture.
- **Dual-Click Support:** - Index + Thumb pinch = **Left Click**
  - Middle + Thumb pinch = **Right Click**

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Computer Vision:** OpenCV
- **Hand Tracking:** Google MediaPipe (Landmark detection)
- **Automation:** PyAutoGUI

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/Procodx/gesture_pro.git](https://github.com/Procodx/gesture_pro.git)
cd gesture_pro
```
###Remember to open your python in a Venv
## 2. Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

## 3. Run the Script

```bash
python main.py
```

# 🖱️ GesturePro

## 📦 Creating a Standalone Executable (.exe)

To use GesturePro as a background app without having Python open:

1. **Install PyInstaller:** `pip install pyinstaller`
2. **Build:** `pyinstaller --noconsole --onefile gesture_mouse.py`
3. **Find your app:** Look in the `dist/` folder.

## 🕹️ Gesture Guide

| Gesture | Action |
| :------ | :----- |

## 🕹️ Gesture Guide

| Gesture                     | Action          | Emoji |
| :-------------------------- | :-------------- | :---- |
| **Index Finger Up**         | Move Mouse      | ☝️    |
| **Index + Thumb Pinch**     | Left Click      | 👌    |
| **Middle + Thumb Pinch**    | Right Click     | 🤌    |
| **Index + Middle (Closed)** | Joystick Scroll | 🤞    |
| **Index + Middle (Open)**   | Take Screenshot | ✌️    |
| **Rockstar Sign**           | Zoom In/Out     | 🤘    |
| **Full Palm Spread**        | Stealth Mode    | 🖐️    |

## ⚠️ Failsafe

If the mouse behaves unexpectedly, slam your physical mouse cursor into the **Top-Left Corner** of your screen to instantly kill the process.

---

**Developed by Codex** - Built with ☕ and Python.
