# Architecture

HandVision-AirMouse uses a modular architecture:

Camera
  ↓
OpenCV
  ↓
MediaPipe Hand Detection
  ↓
Gesture Recognition
  ↓
Cursor Controller
  ↓
Windows API


## Modules

- detector.py
  - Detects hand landmarks.

- gestures.py
  - Recognizes hand gestures.

- cursor.py
  - Controls the system cursor.

- smoothing.py
  - Reduces cursor jitter.

- calibration.py
  - Maps camera coordinates to screen coordinates.