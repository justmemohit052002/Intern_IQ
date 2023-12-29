import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import threading
import tkinter as tk

# Function to start recording
def start_recording():
    global recording
    recording = True
    threading.Thread(target=record_screen).start()

# Function to stop recording
def stop_recording():
    global recording
    recording = False

# Function to handle screen recording
def record_screen():
    global recording
    try:
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        dim = (width, height)
        fcc = cv2.VideoWriter_fourcc(*'mp4v')
        output = cv2.VideoWriter('test.mp4', fcc, 20.0, dim)
        
        start_time = time.time()
        dur = 10  # Duration in seconds
        end_time = start_time + dur
        
        while recording:
            image = pyautogui.screenshot()
            frame = np.array(image)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output.write(frame)
            
            current_time = time.time()
            if current_time > end_time:
                break
        
        output.release()
        print("--- Video recording complete ---")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        output.release()

# Create the GUI
def create_gui():
    global recording
    recording = False
    
    root = tk.Tk()
    root.title("Screen Recorder")
    
    start_button = tk.Button(root, text="Start Recording", command=start_recording)
    start_button.pack()
    
    stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
    stop_button.pack()
    
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
