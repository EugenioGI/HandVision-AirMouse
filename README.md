# 🖐️ HandVision Air Mouse

Real-time virtual mouse controlled by hand gestures using computer vision.

HandVision Air Mouse transforms your webcam into a touchless mouse interface by tracking hand movements and recognizing gestures with MediaPipe.

The project allows users to move the cursor, click, right click and drag objects using only their hand.

---

## 🚀 Features

✅ Real-time hand tracking  
✅ Cursor movement using index finger position  
✅ Left click gesture  
✅ Right click gesture  
✅ Drag and drop gesture  
✅ Cursor smoothing to reduce jitter  
✅ Real-time FPS monitoring  
✅ Modular architecture  

---

## 🎥 Demo
<img width="257" height="492" alt="hand" src="https://github.com/user-attachments/assets/dfb7c111-23b4-437a-95a9-9fc407880f95" />
<img width="216" height="216" alt="example" src="https://github.com/user-attachments/assets/85ff0fb3-f8a5-428d-bf15-71a943008b85" />

---

## 🧠 How it works

The system follows this pipeline:


Webcam
|
v
OpenCV Frame Processing
|
v
MediaPipe Hand Detection
|
v
21 Hand Landmarks Extraction
|
v
Gesture Recognition
|
v
Windows Cursor Control


---

## ✋ Supported Gestures

| Gesture | Action |
|---|---|
| ☝️ Index finger | Move cursor |
| 🤏 Pinch | Left click |
| ✌️ Two fingers | Right click |
| ✊ Closed fist | Drag and drop |

---

## 🏗️ Project Structure


HandVision-AirMouse
│
├── src
│ ├── main.py
│ ├── detector.py
│ ├── cursor.py
│ ├── gestures.py
│ ├── smoothing.py
│ ├── calibration.py
│ └── config.py
│
├── tests
│
├── docs
│ ├── architecture.md
│ └── gestures.md
│
├── assets
│
├── requirements.txt
├── README.md
└── LICENSE


---

## 🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- NumPy
- PyWin32
- Computer Vision
- Human Computer Interaction

---

## 📋 Requirements

- Python 3.10+
- Webcam
- Windows OS

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/EugenioGI/HandVision-AirMouse.git

Move into the project:

cd HandVision-AirMouse

Create a virtual environment:

python -m venv venv

Activate it:

Windows PowerShell
.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run the application:

python src/main.py
🎯 Configuration

The project allows adjustment of:

Detection confidence
Tracking confidence
Cursor smoothing
Camera resolution

These values can be modified inside the configuration files.

📚 Architecture

The project is divided into independent modules:

Detector

Responsible for:

Capturing hand landmarks
Processing MediaPipe results
Returning hand coordinates
Gesture Recognition

Responsible for:

Detecting user gestures
Translating gestures into actions
Cursor Controller

Responsible for:

Moving the system cursor
Executing mouse events
Smoothing

Responsible for:

Reducing cursor instability
Improving user experience
🔮 Future Improvements
 Scroll gesture
 Double click gesture
 Automatic calibration
 Configuration interface
 Multi-platform support
 Executable release (.exe)


👨‍💻 Author

Eugenio Gonzalez Vera

Computer Vision / Software Development Project



