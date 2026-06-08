import cv2
import numpy as np

def draw_signal_graph(ui_frame, sig, x, y, w, h, active=True):
    """
    Draw the green waveform of the signal (Time Domain) with X and Y axes.
    """
    if len(sig) < 2:
        cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (15, 15, 15), -1)
        cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (50, 50, 50), 1)
        cv2.putText(ui_frame, "No Signal Data", (x + int(w/3), y + int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 1)
        return
        
    cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (25, 25, 25), -1)
    cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (50, 50, 50), 1)
    
    # Layout dimensions
    margin_l, margin_r = 45, 15
    margin_t, margin_b = 25, 30
    pw = w - margin_l - margin_r
    ph = h - margin_t - margin_b
    
    # Draw Grid Lines
    cv2.line(ui_frame, (x + margin_l, y + margin_t + ph // 2), (x + w - margin_r, y + margin_t + ph // 2), (40, 40, 40), 1)
    cv2.line(ui_frame, (x + margin_l + pw // 2, y + margin_t), (x + margin_l + pw // 2, y + h - margin_b), (40, 40, 40), 1)
    
    # Draw Axes
    cv2.line(ui_frame, (x + margin_l, y + margin_t), (x + margin_l, y + h - margin_b), (150, 150, 150), 1) # Y-axis
    cv2.line(ui_frame, (x + margin_l, y + h - margin_b), (x + w - margin_r, y + h - margin_b), (150, 150, 150), 1) # X-axis
    
    # Axis Labels
    # Y-axis ticks
    cv2.putText(ui_frame, "1.0", (x + 10, y + margin_t + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "0.5", (x + 10, y + margin_t + ph // 2 + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "0.0", (x + 10, y + h - margin_b + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    
    # X-axis ticks (Time representing 5 seconds at 30 fps)
    cv2.putText(ui_frame, "-5.0s", (x + margin_l - 15, y + h - margin_b + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "-2.5s", (x + margin_l + pw // 2 - 15, y + h - margin_b + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "0.0s", (x + w - margin_r - 15, y + h - margin_b + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    
    # Plot data
    sig_np = np.array(sig)
    sig_norm = (sig_np - np.min(sig_np)) / (np.max(sig_np) - np.min(sig_np) + 1e-6)
    
    for i in range(len(sig_norm) - 1):
        x1 = x + margin_l + int(i * (pw / len(sig_norm)))
        y1 = y + h - margin_b - int(sig_norm[i] * ph)
        x2 = x + margin_l + int((i+1) * (pw / len(sig_norm)))
        y2 = y + h - margin_b - int(sig_norm[i+1] * ph)
        cv2.line(ui_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
    if not active:
        cv2.putText(ui_frame, "PAUSED", (x + w - 70, y + margin_t - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

def draw_fft_graph(ui_frame, freqs, fft_vals, x, y, w, h, active=True):
    """
    Draw the frequency domain graph (FFT Peaks) with X and Y axes.
    """
    if freqs is None or len(freqs) < 2:
        cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (15, 15, 15), -1)
        cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (50, 50, 50), 1)
        cv2.putText(ui_frame, "No Frequency Data", (x + int(w/4), y + int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 1)
        return
        
    cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (25, 25, 25), -1)
    cv2.rectangle(ui_frame, (x, y), (x + w, y + h), (50, 50, 50), 1)
    
    # Layout dimensions
    margin_l, margin_r = 45, 15
    margin_t, margin_b = 25, 30
    pw = w - margin_l - margin_r
    ph = h - margin_t - margin_b
    
    # Draw Grid Lines
    cv2.line(ui_frame, (x + margin_l, y + margin_t + ph // 2), (x + w - margin_r, y + margin_t + ph // 2), (40, 40, 40), 1)
    cv2.line(ui_frame, (x + margin_l + pw // 2, y + margin_t), (x + margin_l + pw // 2, y + h - margin_b), (40, 40, 40), 1)
    
    # Draw Axes
    cv2.line(ui_frame, (x + margin_l, y + margin_t), (x + margin_l, y + h - margin_b), (150, 150, 150), 1) # Y-axis
    cv2.line(ui_frame, (x + margin_l, y + h - margin_b), (x + w - margin_r, y + h - margin_b), (150, 150, 150), 1) # X-axis
    
    # Axis Labels
    # Y-axis ticks
    cv2.putText(ui_frame, "1.0", (x + 10, y + margin_t + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "0.5", (x + 10, y + margin_t + ph // 2 + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "0.0", (x + 10, y + h - margin_b + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    
    # X-axis ticks (BPM Frequency: 50 BPM, 80 BPM, 110 BPM)
    cv2.putText(ui_frame, "50 bpm", (x + margin_l - 15, y + h - margin_b + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "80 bpm", (x + margin_l + pw // 2 - 15, y + h - margin_b + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.putText(ui_frame, "110 bpm", (x + w - margin_r - 20, y + h - margin_b + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    
    # Plot data
    fft_norm = (fft_vals - np.min(fft_vals)) / (np.max(fft_vals) - np.min(fft_vals) + 1e-6)
    
    for i in range(len(fft_norm) - 1):
        x1 = x + margin_l + int(i * (pw / len(fft_norm)))
        y1 = y + h - margin_b - int(fft_norm[i] * ph)
        x2 = x + margin_l + int((i+1) * (pw / len(fft_norm)))
        y2 = y + h - margin_b - int(fft_norm[i+1] * ph)
        cv2.line(ui_frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
        
    if not active:
        cv2.putText(ui_frame, "PAUSED", (x + w - 70, y + margin_t - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)


