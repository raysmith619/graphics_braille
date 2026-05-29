#sinewave_numpy.py    29Mar2023  crs
""" Lower level substitute for pysinewave
    Not a direct substitute but for lower level operations
"""
import time
import copy
import numpy as np
import sounddevice as sd
from pysinewave import utilities

from graphics_braille.select_trace import SlTrace

class SineWaveNumPy:
    """ Gathers and plays stereo sine wave
    """
    @classmethod
    def concatinate(cls, sinewave_nps):
        """ Concatinate a list of SineWaveNumPy wave forms
        :sinewave_nps: List of SineWaveNumPy waves
        :returns: SineWaveNumPy waveform
        """
        sample_rate = sinewave_nps[0].sample_rate       # Use first entry
        duration = sinewave_nps[0].duration 
        wfs_ndarr = [swnp.wf_ndarr for swnp in sinewave_nps]  # Get the waveforms
        wfc_ndarr = np.concatenate(wfs_ndarr)
        swnp = SineWaveNumPy(wf_ndarr=wfc_ndarr, sample_rate=sample_rate,
                           duration=duration)
        return swnp
        
    def __init__(self, pitch=0, decibels_left=0, decibels_right=0,
                sample_rate=44100, duration=None, delay=None,
                wf_ndarr=None):
        """ Setup waves
        :pitch: user tone level default: 0
        :decibels_left: left volume in decibels default: 0
        :decibels_right: right volume in decibels default: 0
        :samplerate: samples per second default: 44100
        :duration: play duration(seconds) default:calculated from len, sample_rate
        :wf_ndarr: if present, BYPASS calculation and use as waveform (ndarray)
        """
        if wf_ndarr is not None:
            self.sample_rate = sample_rate
            self.duration = duration
            self.wf_ndarr = wf_ndarr
            self.delay = delay
            
        else:
            freq_hz = utilities.pitch_to_frequency(pitch)
            atten_left = utilities.decibels_to_amplitude_ratio(decibels_left) 
            atten_right = utilities.decibels_to_amplitude_ratio(decibels_right) 
            self.sample_rate = sample_rate
            if duration is None:
                SlTrace.lg(f"SineWaveNumPy duration is {duration} treat as .1")
                duration = .1
            self.duration = duration
            self.delay = delay
            # NumpPy magic to calculate the waveform
            each_sample_number = np.arange(duration * sample_rate)
            base_waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sample_rate)
            left_waveform = base_waveform.reshape(-1,1)*atten_left
            right_waveform = base_waveform.reshape(-1,1)*atten_right
            wf_ndarr = np.hstack((left_waveform, right_waveform))
            self.wf_ndarr = copy.deepcopy(wf_ndarr)
        
    def play(self):
        """ Start playing tone
        """
        sd.play(self.wf_ndarr, self.sample_rate)
        
        
    def stop(self):
        """ Stop playing tone
        """
        sd.stop()

if __name__ == "__main__":
    pitch = -40
    pitch_sep = 6
    decibels_sep = -50
    decibels_left = -50
    decibels_right = decibels_left
    duration = 1
    tone_sep = 1
    print(f"Starting with pitch:{pitch} duration:{duration} sec")
    for i in range(10):
        pitch += pitch_sep
        decibels_left += decibels_sep
        sw_left = SineWaveNumPy(pitch=pitch,
                    decibels_left=decibels_left,
                    decibels_right=0,
                    duration=duration)
        sw_left.play()
        time.sleep(duration)
        sw_right = SineWaveNumPy(pitch=pitch,
                    decibels_right=decibels_left,
                    decibels_left=0,
                    duration=duration)
        sw_right.play()
        time.sleep(duration)
    '''
    time.sleep(duration)
    sw1.stop()
    print("End of sw1")
    time.sleep(duration)
    sw2.play()
    time.sleep(duration)
    sw2.stop()
    print("End of sw2")
    '''