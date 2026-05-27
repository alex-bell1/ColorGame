👻 Desktop Horror Prank Simulator

A fullscreen desktop prank application built with Python, Tkinter, and PyAutoGUI. The program captures a screenshot of the user’s desktop, overlays animated horror-style images and sound effects, and creates an immersive jumpscare experience with timed visual transitions.

✨ Features
🖥️ Captures the current desktop as a fake background
👻 Fullscreen horror animation effects
🔊 Real-time sound playback using system audio
🎞️ Image transition sequence with timed effects
🖱️ Mouse-triggered animation start
⌨️ Keyboard blocking for immersion
⚡ Lightweight prank-style application
🛠️ Requirements
Python 3.x
Tkinter
Pillow
PyAutoGUI

Install dependencies:

pip install pillow pyautogui

winsound comes built into Windows Python installations.

🚀 Usage

Run the application:

python prank_simulator.py

The app will:

Minimize to the desktop
Capture a screenshot of the desktop
Open a fullscreen fake desktop overlay
Start the horror animation when clicked
⌨️ Controls
Key / Action	Function
Left Mouse Click	Start animation sequence
Up Arrow	Exit application
⚙️ How It Works

The application creates a fullscreen Tkinter window and places a screenshot of the current desktop as the background.

Workflow

Hide open windows using:

pyautogui.hotkey('win', 'd')

Capture a desktop screenshot:

pyautogui.screenshot('desktop.png')
Display the screenshot in a borderless fullscreen window
Load horror images dynamically using Pillow

Play sound effects asynchronously using:

winsound.PlaySound()
Trigger rapid image transitions to simulate jumpscare effects
📂 Project Structure
.
├── prank_simulator.py
├── desktop.png
├── images/
│   ├── img1.png
│   ├── img2.png
│   ├── img3.png
│   ├── img4.png
│   ├── img5.png
│   └── img6.png
├── noise1.wav
├── noise2.wav
├── noise3.wav
└── README.md
🧠 Technologies Used
Tkinter — GUI window management
PyAutoGUI — desktop control and screenshots
Pillow — image loading and rendering
winsound — Windows audio playback
🔮 Possible Improvements
Add random scare sequences
Add webcam-triggered activation
Add animated GIF support
Add multi-monitor support
Add fade transitions and visual glitches
Package as an executable with PyInstaller
⚠️ Disclaimer

This project is intended for educational and entertainment purposes only. Use responsibly and avoid causing distress or disrupting other users.

📜 License

This project is licensed under the MIT License.
