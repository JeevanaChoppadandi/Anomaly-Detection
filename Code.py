import tkinter as tk
from tkinter import filedialog
import cv2
import threading

# Placeholder function for anomaly detection
def detect_anomaly(frame):
    """
    Replace this with your actual anomaly detection logic.
    For now, it simulates detection of abnormal activities like fighting, running, or throwing.
    """
    # Example: Check if the frame is mostly dark (simulating abnormal activity)
    if frame.mean() < 50:
        return "Abnormal Activity Detected"
    elif frame.mean() > 200:
        return "Abnormal Activity Detected"
    else:
        return "No Abnormal Activity Detected"

# Function to process the video and detect anomalies
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect anomaly
        anomaly_status = detect_anomaly(frame)

        # Display the anomaly status on the video frame
        cv2.putText(frame, anomaly_status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the video frame
        cv2.imshow("Intelligent Surveillance - Anomaly Detection", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to handle video upload
def upload_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov")])
    if file_path:
        status_label.config(text="Processing video...", fg="blue")
        # Run video processing in a separate thread to avoid freezing the GUI
        threading.Thread(target=process_video, args=(file_path,)).start()

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main GUI window
root = tk.Tk()
root.title("Intelligent Surveillance - Anomaly Detection")
root.geometry("400x200")

# Title label
title_label = tk.Label(root, text="Intelligent Surveillance Anomaly Detection", font=("Arial", 16))
title_label.pack(pady=10)

# Upload button
upload_button = tk.Button(root, text="Upload Video", command=upload_video, font=("Arial", 12))
upload_button.pack(pady=20)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=exit_app, font=("Arial", 12))
exit_button.pack(pady=10)

# Run the GUI
root.mainloop()
