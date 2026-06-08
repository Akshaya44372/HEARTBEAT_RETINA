import cv2
import numpy as np

class GUI:
    def __init__(self, width=1200, height=800):
        self.width = width
        self.height = height
        self.frame = np.zeros((height, width, 3), dtype=np.uint8)
        
    def reset(self):
        self.frame.fill(0)
        
    def draw_window_frame(self, title, x, y, w, h):
        # Background
        cv2.rectangle(self.frame, (x, y), (x + w, y + h), (20, 20, 20), -1)
        # Border
        cv2.rectangle(self.frame, (x, y), (x + w, y + h), (100, 100, 100), 2)
        # Header bar
        cv2.rectangle(self.frame, (x, y), (x + w, y + 25), (50, 50, 50), -1)
        cv2.putText(self.frame, title, (x + 10, y + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    def place_video(self, img, x, y, w, h):
        if img is not None and img.size > 0:
            resized = cv2.resize(img, (w - 4, h - 29))
            self.frame[y + 27:y + h - 2, x + 2:x + w - 2] = resized
            
    def draw_button(self, text, x, y, w, h, bg_color=(100, 100, 100)):
        cv2.rectangle(self.frame, (x, y), (x + w, y + h), bg_color, -1)
        cv2.rectangle(self.frame, (x, y), (x + w, y + h), (150, 150, 150), 1)
        cv2.putText(self.frame, text, (x + int(w/4), y + int(h*0.65)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
    def draw_text(self, text, x, y, scale=0.7, color=(255, 255, 255), thickness=1):
        cv2.putText(self.frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness)
        
    def get_frame(self):
        return self.frame
