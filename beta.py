import tkinter as tk
import cv2
import numpy as np
import pyaudio

# Create a Tkinter window
root = tk.Tk()
root.title("iCho")

# Create a canvas to display the video feed
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Create a label to display the tilt direction
label = tk.Label(root, text="Tilt Direction: ")
label.pack()

# Create a PyAudio object to control the volume
p = pyaudio.PyAudio()

# Create a function to update the video feed and tilt direction
def update():
    # Capture a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the face in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If a face is detected, calculate the tilt direction
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        center_x = x + w / 2
        center_y = y + h / 2
        tilt = (center_y - 240) / 240

        # Set the volume based on the tilt direction
        volume = p.get_master_volume()
        p.set_master_volume(volume * (1 - abs(tilt)))

        # Display the tilt direction on the label
        label.config(text="Tilt Direction: " + str(tilt))

    # Display the video feed on the canvas
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = np.transpose(img, (1, 0, 2))
    img = np.flip(img, 0)
    img = tk.PhotoImage(data=img.tobytes())
    canvas.create_image(0, 0, anchor=tk.NW, image=img)

    # Schedule the next update
    root.after(10, update)

# Create a video capture object
cap = cv2.VideoCapture(0)

# Load the face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start the update loop
update()

# Start the Tkinter main loop
root.mainloop()