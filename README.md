# ❤️ Heartbeat Retina

## Webcam-Based Real-Time Heart Rate Monitoring using rPPG

Heartbeat Retina is a real-time, contactless heart rate monitoring system that estimates a user's heart rate using a standard webcam. The project utilizes Remote Photoplethysmography (rPPG), a computer vision technique that detects subtle skin color variations caused by blood circulation beneath the skin.

The system combines MediaPipe Face Mesh, OpenCV, and advanced signal processing techniques to continuously monitor heart rate without requiring wearable sensors or physical contact.

---

## 🚀 Features

### Real-Time Heart Rate Estimation
- Contactless heart rate monitoring through a webcam.
- Continuous BPM (Beats Per Minute) calculation.
- Live pulse signal extraction from facial skin regions.

### Face Detection & Tracking
- MediaPipe Face Mesh facial landmark detection.
- Stable facial tracking during moderate movements.
- Forehead Region of Interest (ROI) extraction for signal acquisition.

### Eye Blink Detection
- Eye Aspect Ratio (EAR) based eye state detection.
- Automatically pauses measurements when eyes are closed.
- Improves signal quality and reduces noise.

### Signal Processing Pipeline
- Green channel signal extraction.
- Signal detrending for baseline drift removal.
- Butterworth Bandpass Filtering.
- Fast Fourier Transform (FFT) based frequency analysis.
- Accurate BPM estimation from processed signals.

### Interactive GUI
- Real-time camera feed visualization.
- Live pulse waveform display.
- FFT spectrum visualization.
- Start/Stop monitoring controls.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| OpenCV | Video Processing & GUI |
| MediaPipe | Facial Landmark Detection |
| NumPy | Numerical Computations |
| SciPy | Signal Processing |
| FFT | Frequency Analysis |
| rPPG | Contactless Heart Rate Detection |

---

## 📂 Project Structure

```text
HEARTBEAT_RETINA/
│
├── analyze_camera.py      # Main application
├── webcam.py              # Webcam handling
├── face_detection.py      # Face mesh detection
├── face_utilities.py      # Landmark utilities & EAR calculation
├── signal_processing.py   # rPPG signal processing
├── graph_plot.py          # Signal and FFT visualization
├── gui.py                 # GUI components
├── requirements.txt       # Dependencies
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/HEARTBEAT_RETINA.git
cd HEARTBEAT_RETINA
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:

```text
opencv-python
mediapipe
numpy
scipy
```

---

## ▶️ Running the Project

Start the application:

```bash
python analyze_camera.py
```

### Steps

1. Click **Open** to start the webcam.
2. Position your face clearly in front of the camera.
3. Click **Start** to begin heart rate monitoring.
4. Keep your face steady for accurate measurements.
5. View BPM and signal graphs in real time.

---

## 🔬 How It Works

1. Webcam captures facial video frames.
2. MediaPipe detects facial landmarks.
3. Forehead ROI is extracted.
4. Average green-channel intensity is calculated.
5. Signal processing removes noise and drift.
6. FFT identifies the dominant pulse frequency.
7. BPM is computed and displayed in real time.

---

## 📊 Applications

- Contactless health monitoring
- Telemedicine systems
- Fitness and wellness tracking
- Human-computer interaction research
- Biomedical signal processing education
- Remote patient monitoring

---

## 🎯 Future Enhancements

- Heart Rate Variability (HRV) analysis
- Multi-person monitoring
- Blood oxygen estimation
- Mobile application support
- Deep Learning-based signal enhancement
- Cloud-based health analytics

---

## 👨‍💻 Author

**Akshaya Yarraguntla**

GitHub: https://github.com/Akshaya44372

---

## 📜 License

This project is developed for educational, research, and portfolio purposes.

---

### Keywords

Remote Photoplethysmography (rPPG) • Heart Rate Monitoring • OpenCV • MediaPipe Face Mesh • Computer Vision • Signal Processing • FFT • Biomedical Engineering • Python