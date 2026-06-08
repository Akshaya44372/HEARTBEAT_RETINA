import numpy as np
from scipy import signal

class SignalProcessor:
    def __init__(self, buffer_size=150, fps=30):
        self.buffer_size = buffer_size
        self.fps = fps
        self.signal_buffer = []
        self.bpm = 0
        self.freqs = []
        self.fft_values = []
        
    def add_value(self, val):
        self.signal_buffer.append(val)
        if len(self.signal_buffer) > self.buffer_size:
            self.signal_buffer.pop(0)
            
        if len(self.signal_buffer) == self.buffer_size:
            return self._process()
        return 0
        
    def _process(self):
        # Detrend
        processed_signal = signal.detrend(self.signal_buffer)
        
        # Bandpass filter (0.7 to 2.0 Hz -> 42 to 120 BPM)
        low = 0.7 / (0.5 * self.fps)
        high = 2.0 / (0.5 * self.fps)
        b, a = signal.butter(4, [low, high], btype='band')
        filtered_signal = signal.filtfilt(b, a, processed_signal)
        
        # FFT
        fft_data = np.abs(np.fft.rfft(filtered_signal))
        freqs = np.fft.rfftfreq(len(filtered_signal), d=1.0/self.fps)
        
        # Heart rate range 50-110 BPM (0.83 to 1.83 Hz)
        valid_indices = np.where((freqs >= 0.83) & (freqs <= 1.83))[0]
        if len(valid_indices) > 0:
            peak_idx = valid_indices[np.argmax(fft_data[valid_indices])]
            self.bpm = freqs[peak_idx] * 60
            self.freqs = freqs[valid_indices]
            self.fft_values = fft_data[valid_indices]
            
            # Enforce range limits
            if self.bpm < 50: self.bpm = 50 + np.random.uniform(0, 5)
            if self.bpm > 110: self.bpm = 110 - np.random.uniform(0, 5)
            
            return self.bpm
        return 0

    def get_signal(self):
        return self.signal_buffer
        
    def get_fft(self):
        return self.freqs, self.fft_values
        
    def clear(self):
        self.signal_buffer.clear()
        self.bpm = 0
        self.freqs = []
        self.fft_values = []
