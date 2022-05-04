# Recognition

Be prepared for many hours of compiling on the Raspberry Pi.

[PyImage Search - Raspberry Pi Face Recognition][1]

## Table Of Contents

- [Recognition](#recognition)
  - [Table Of Contents](#table-of-contents)
  - [Setup](#setup)
    - [Raspbian Stretch Desktop](#raspbian-stretch-desktop)
    - [Install Python 3.6.6 on Raspberry Pi](#install-python-366-on-raspberry-pi)
    - [Install OpenCV4 on Raspberry Pi](#install-opencv4-on-raspberry-pi)
  - [Install dlib and face_recognition](#install-dlib-and-face_recognition)
  - [Backup your image NOW](#backup-your-image-now)
  - [Ready for Raspberry Pi](#ready-for-raspberry-pi)
  - [References](#references)

## Setup

Setting up the necessary software on the Raspberry Pi took a very long time.  Hours.. many hours.

What I did was installed Python 3.6.6, OpenCV 4.0.1, dlib, face_recognition, numpy, scipy, scikit-image, various required Python modules.

### Raspbian Stretch Desktop

Start with the Raspbian Stretch Desktop image.

For the next few hours, you just ssh into the Rpi and run everything from you your laptop if you like.  Not until you actually do face recognition do you need to run on Raspberry Pi.

### Install Python 3.6.6 on Raspberry Pi

I recommend [this Gist][2], but change the `3.6.5` to `3.6.6`. The script for this is in the `install_py` policy in the `Makefile`. You can run it by executing, `make install_py`.

### Install OpenCV4 on Raspberry Pi

I highly recommend [this PyImageSearch Blog][3].

That blog installs `4.0.0` and the script here in the `py_install_cv2` policy of the `Makefile` is the one used to install `4.0.1`.

## Install dlib and face_recognition

To get this project to work on the Raspberry Pi you will need *dlib* and *face_recognition*.

You also need *scipy* and *sklearn-image* - both of these also take a long time to compile on the Raspberry Pi.

1. [PyImageSearch 2018 Blog - Install dlib (the easy, complete guide)][4]
2. [PyImageSearch 2017 Blog - How to install dlib][5]

I did a pip install, and waited forever, but Adrian also recommends building from source. You can decide which is better for you.

The script is in the `py_install_imagelib` in the `Makefile`.

## Backup your image NOW

You just spent hours getting that image just the way you need it.  I would recommend you backup that image so you can just reburn a new image with all of the software already installed.

## Ready for Raspberry Pi

After you have all of that installed, you can then encode_faces on your laptop to get the encodings pickle file, and then transfer that to your raspberry pi and run pi_face_recognition.py.

Keep in mind that you have to comment/uncomment one line of code:

```python
#vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
```

And enable the camera on your Pi.

You might also want to adjust the threshold in this line:

```python
matches = face_recognition.compare_faces(data["encodings"],
    encoding, tolerance=0.46)
```

as I have done to 0.46 ( default value is 0.6 ) if you are finding too many false positives.

Good luck - its a super fun project once you get it running.

## References

1. [1]: https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/
2. [2]: https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f
3. [3]: https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
4. [4]: https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
5. [5]: https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/
