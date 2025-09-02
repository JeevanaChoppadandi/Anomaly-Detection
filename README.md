# Anomaly-Detection
Project Description This project implements a real-time anomaly detection system for surveillance videos using brightness-based analysis. The system monitors video feeds and flags abnormal activities when frames become extremely dark (brightness < 50) or bright (brightness > 200). Detected anomalies trigger on-screen alerts, making it useful for detecting camera tampering, sudden lighting changes, or power failures.

Key Features ✅ Real-time processing (~30 FPS on standard hardware) ✅ Simple & lightweight (OpenCV + Tkinter) ✅ Visual anomaly alerts (on-screen text overlay) ✅ Easy-to-use GUI (upload videos, view results)

Limitations ❌ Only detects lighting-based anomalies ❌ Misses complex threats (violence, intrusions, objects) ❌ Moderate accuracy (~60-70%) with some false alarms

Future Improvements 🔹 YOLO object detection (weapons, suspicious objects) 🔹 Optical flow motion analysis (unusual movements) 🔹 Edge deployment (Jetson Nano, Raspberry Pi) 🔹 Cloud alerts (SMS/email notifications)

Installation pip install opencv-python numpy Usage Run the script:

python anomaly_detection.py Upload a video file via the GUI

View real-time anomaly alerts
