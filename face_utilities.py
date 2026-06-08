import numpy as np
import cv2

# MediaPipe Indices
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
FOREHEAD = [10, 338, 297, 332, 284, 251, 389, 446, 261, 26, 226, 159, 103, 54, 67]

def calculate_ear(landmarks):
    """
    Calculate Eye Aspect Ratio (EAR) for blink detection.
    """
    if landmarks is None:
        return 0.0
    try:
        # Left Eye (MediaPipe landmarks: 382 to 374, 381 to 373, 362 to 263)
        v1_l = np.linalg.norm(landmarks[382] - landmarks[374])
        v2_l = np.linalg.norm(landmarks[381] - landmarks[373])
        h_l = np.linalg.norm(landmarks[362] - landmarks[263])
        ear_l = (v1_l + v2_l) / (2.0 * h_l)
        
        # Right Eye (MediaPipe landmarks: 7 to 154, 163 to 153, 33 to 133)
        v1_r = np.linalg.norm(landmarks[7] - landmarks[154])
        v2_r = np.linalg.norm(landmarks[163] - landmarks[153])
        h_r = np.linalg.norm(landmarks[33] - landmarks[133])
        ear_r = (v1_r + v2_r) / (2.0 * h_r)
        
        return (ear_l + ear_r) / 2.0
    except:
        return 0.0

def extract_roi_color(frame, landmarks, indices):
    """
    Extract the average BGR color from a landmark polygon ROI.
    """
    if landmarks is None:
        return (0, 0, 0)
    try:
        points = np.array([landmarks[idx] for idx in indices], dtype=np.int32)
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [points], 255)
        avg_color = cv2.mean(frame, mask=mask)[:3]
        return avg_color # BGR
    except:
        return (0, 0, 0)
