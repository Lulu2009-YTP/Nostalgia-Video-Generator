from moviepy.editor import *
from moviepy.video.fx.all import *
from moviepy.audio.fx.all import *
import random
import numpy as np

class EffectsProcessor:
    def __init__(self):
        self.video_clip = None
        self.audio_clip = None
        
    def process_video(self, input_path, output_path, effect_config, progress_callback=None):
        # Load video
        self.video_clip = VideoFileClip(input_path)
        self.audio_clip = self.video_clip.audio
        
        # Apply visual effects
        if effect_config['zoom']:
            self.apply_random_zoom()
        if effect_config['glow']:
            self.apply_glow_effect()
        if effect_config['mirror']:
            self.apply_mirror_effect()
        if effect_config['swirl']:
            self.apply_swirl_effect()
            
        # Apply audio effects
        if effect_config['pitch']:
            self.apply_random_pitch()
        if effect_config['echo']:
            self.apply_echo_effect()
        if effect_config['reverb']:
            self.apply_reverb_effect()
            
        # Write final video
        self.video_clip.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            progress_bar=False,
            callback=progress_callback
        )
        
        # Clean up
        self.video_clip.close()
        if self.audio_clip:
            self.audio_clip.close()
            
    def apply_random_zoom(self):
        def zoom_effect(get_frame, t):
            zoom = 1 + 0.3 * np.sin(t)
            frame = get_frame(t)
            return scipy.ndimage.zoom(frame, zoom)
            
        self.video_clip = self.video_clip.fl(zoom_effect)
        
    def apply_glow_effect(self):
        self.video_clip = self.video_clip.fx(vfx.colorx, 1.2)
        
    def apply_mirror_effect(self):
        def mirror(frame):
            return np.hstack([frame, frame[:, ::-1]])
            
        self.video_clip = self.video_clip.fl_image(mirror)
        
    def apply_swirl_effect(self):
        def swirl(frame):
            return scipy.ndimage.swirl(frame, strength=random.uniform(0, 5))
            
        self.video_clip = self.video_clip.fl_image(swirl)
        
    def apply_random_pitch(self):
        if self.audio_clip:
            self.audio_clip = self.audio_clip.fx(afx.pitch, random.uniform(0.5, 1.5))
            self.video_clip = self.video_clip.set_audio(self.audio_clip)
            
    def apply_echo_effect(self):
        if self.audio_clip:
            echo_audio = self.audio_clip.fx(afx.echo, 0.5, 0.7)
            self.video_clip = self.video_clip.set_audio(echo_audio)
            
    def apply_reverb_effect(self):
        if self.audio_clip:
            reverb_audio = self.audio_clip.fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
            self.video_clip = self.video_clip.set_audio(reverb_audio)