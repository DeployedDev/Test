# 🟢 Windows Top-Screen Classification Banner

A lightweight Python utility that displays a persistent, always-on-top banner docked to the top of your screen — useful for marking desktops with labels like "Confidential", "Secret", or any custom notice.

This app uses the Windows AppBar API to behave like a taskbar and integrates seamlessly with your desktop.

---

## ✅ Features

- Fixed-height, full-width green banner
- Uses Windows AppBar API to dock like a taskbar
- Always-on-top window (non-intrusive)
- Only closes with `Escape` after click (intentional shutdown)
- Clean GUI built with `tkinter`
- Minimal dependencies and fast startup

---

## 🖼️ Preview

> ![Screenshot](https://github.com/user-attachments/assets/4e31c218-06a7-4877-b065-52d843c6b368)




## 💻 Requirements

- **Operating System:** Windows 10/11
- **Package:** `pywin32`

Install dependencies:

```bash
pip install pywin32
