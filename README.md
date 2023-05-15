
# icho - Intelligent Head Tracking Audio Experience

<p align="center">
  <img src="https://user-images.githubusercontent.com/95145136/221834389-86a8884f-b594-4877-88cd-8976637acc73.gif" alt="animated" />
</p>


Introducing the volume adjustment assistant that adapts to your every move! Our software uses facial recognition to track your face and adjust the volume of your device intelligently. Don't settle for outdated volume adjustment systems. Upgrade to our intelligent and intuitive technology today and enjoy a listening experience like no other!

- [Features](#features)
- [Run Locally](#run-locally)
- [Demo](#demo)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

## Features

- Tracks the head movements of the user accurately
- Adjusts the volume according to those movements
- Lowers the volume when the user needs to focus on his surrounding conversations
- Sets the volume back to normal when user focuses on the screen
- Controls volume balance of individual left-right channels corresponding to the orientation of user's face

Show some ❤️ by starring the repository! ⭐️
## Run Locally
Recommended Interpreter: Python 3.10

- Install Dependencies

```bash
pip install comtypes
pip install pycaw
pip install opencv-python
pip install mediapipe
pip install numpy
```

- Clone the project

```bash
  git clone https://github.com/adivishnu-a/icho
```

- Go to the project directory

```bash
  cd icho
```

- Run the program

```bash
  python main.py
```

## Demo

[Kumar Sashank](https://github.com/KumarSashank) with the Video Demo


https://user-images.githubusercontent.com/95145136/221878529-505616e4-d0dc-4538-8dd9-0dd630e65e57.mp4

<br>


[Adi Vishnu's](https://github.com/adivishnu-a) post on [LinkedIn](https://www.linkedin.com/posts/adi-vishnu-avula_nexttechlab-9hacks-scienceexpo-activity-7036301316339470337-Kcjz)



## FAQ

#### How does the product work?

This program uses the webcam to track our face and is hence based on computer vision to detect and track human faces in a video stream or image sequence.

Here's a general overview of how our face tracking tool works:   
- Create a face_mesh instance from the mediapipe library that is responsible for detecting the landmarks on the face.
- Create a VideoCapture instance from OpenCV to capture the video from the camera.
- Read each frame from the video and convert it to the RGB color space.
- Detect the landmarks on the face using the face_mesh instance.
- Get the 2D and 3D coordinates of the detected landmarks.
- Solve Perspective-n-Point (PnP) to estimate the pose of the head.
- Calculate the rotational matrix and use it to calculate the Euler angles of the head pose.
- Display the resulting frame with the head direction and the text showing where the person is looking.

And here's how our volume adjustment mechanism works:
- Get the speakers' device and set the interface to control the volume from the pycaw library.
- Get the current master volume level using GetMasterVolumeLevel().
- Based on the head movement, adjust the volume level using the SetMasterVolumeLevel or SetChannelVolumeLevel methods.

#### Where can I run this? Can I use it on my smartphone?
You can run this software on any PC with an integrated or discrete webcam, and you can do it by following the instructions provided in the above section. This requires the webcam to be run continuously for the program to function. And this does not work on a smartphone.

#### What are the current limitations of this project?
At its current stage, the program functions properly when detecting a single face in front of the camera. However, there are ongoing developments aimed at enhancing the project's capabilities to function effectively in crowded scenarios.

#### How can I report a bug or suggest a new feature for this project?
You can report a bug or suggest a new feature by opening an issue on the project's GitHub repository.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License  

This project is licensed under the [MIT License](LICENSE).

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/adivishnu-a-icho/count.svg" />
</p>
