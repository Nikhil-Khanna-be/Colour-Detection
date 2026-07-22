# Colour-Detection
# 🎨 Real-Time Color Detection using OpenCV 📷

Detect **🔴 Red**, **🟢 Green**, and **🔵 Blue** objects in real time using **Python** and **OpenCV**. This project captures live video from your webcam, converts each frame from **BGR** to **HSV** color space, and detects colored objects by applying predefined HSV ranges. Each detected object is highlighted with a bounding box and labeled with its corresponding color.

---

# ✨ Features

* 📷 Real-time webcam video processing
* 🔴 Detects **Red** objects
* 🟢 Detects **Green** objects
* 🔵 Detects **Blue** objects
* 🎯 Accurate color detection using the HSV color space
* 📦 Draws bounding boxes around detected objects
* 🏷️ Displays the detected color name
* 🧹 Reduces noise using image processing techniques
* ⚡ Fast and lightweight implementation using OpenCV
* ❌ Press **Q** to exit the application

---

# 🛠️ Technologies Used

* 🐍 Python 3
* 👁️ OpenCV (`cv2`)
* 🔢 NumPy

---

# 🌈 HSV Color Ranges

### 🔴 Red

```python
red_L1 = np.array([0,120,70], np.uint8)
red_U1 = np.array([10,255,255], np.uint8)

red_L2 = np.array([170,120,70], np.uint8)
red_U2 = np.array([180,255,255], np.uint8)
```

### 🟢 Green

```python
green_L = np.array([40,40,40], np.uint8)
green_U = np.array([80,255,255], np.uint8)
```

### 🔵 Blue

```python
blue_L = np.array([95,100,100], np.uint8)
blue_U = np.array([140,255,255], np.uint8)
```

> **📝 Note**
>
> The HSV values used in this project are optimized for **my webcam and lighting conditions**.
>
> Since every webcam, camera sensor, and lighting environment is different, you may need to **adjust the HSV ranges** for accurate detection on your system.
>
> * 📷 Different webcams may produce different HSV values.
> * 💡 Indoor, outdoor, or low-light environments can affect color detection.
> * 🎨 Different shades of the same color may require slight modifications to the HSV range.
>
> Feel free to experiment with the **Lower** and **Upper HSV values** according to your camera quality and environment for the best results.

---

# 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Nikhil-Khanna-be/Colour-Detection.git
```

### 2️⃣ Navigate to the project folder

```bash
cd Colour-Detection
```

### 3️⃣ Install the required libraries

```bash
pip install opencv-python numpy
```

### 4️⃣ Run the project

```bash
python colour_detection.py
```

---

# ⚙️ How It Works

1. 📷 Opens the default webcam.
2. 🎥 Captures video frames continuously.
3. 🔄 Converts each frame from **BGR** to **HSV**.
4. 🎨 Creates masks for **🔴 Red**, **🟢 Green**, and **🔵 Blue** colors.
5. 🧹 Applies image processing to reduce noise.
6. 🔍 Detects contours of colored objects.
7. 📦 Draws bounding boxes around detected objects.
8. 🏷️ Displays the detected color name.
9. ❌ Press **Q** to stop the program.

---

# 💡 Applications

* 🤖 Robotics
* 👁️ Computer Vision
* 🎯 Object Tracking
* 🦾 Human–Computer Interaction
* 🎓 OpenCV Learning Projects
* 📹 Real-Time Image Processing
* 🏭 Industrial Color-Based Object Detection

---

# 🚀 Future Enhancements

* 🟡 Add Yellow color detection
* 🟠 Add Orange color detection
* 🟣 Add Purple color detection
* ⚪ Add White and Black color detection
* 🎚️ HSV adjustment using OpenCV trackbars
* 📍 Display object coordinates and area
* 📊 Detect multiple objects simultaneously
* 🌞 Improve detection under different lighting conditions
* 💾 Capture and save detected frames

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub. It motivates me to create more projects and helps others discover this repository.

---

# 📄 License

This project is open-source and available for **educational and personal use**.
