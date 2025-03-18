import os
import numpy as np
from PIL import Image

def create_overlay_image(size, text="", color=(255, 255, 255)):
    """Create an overlay image with text"""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    return img

def generate_random_duration():
    """Generate a random duration between 0.1 and 1.0 seconds"""
    return np.random.uniform(0.1, 1.0)

def get_random_effect():
    """Return a random effect from available effects"""
    effects = ['zoom', 'glow', 'mirror', 'swirl', 'wave', 'speed']
    return np.random.choice(effects)

def ensure_directory(path):
    """Ensure directory exists, create if it doesn't"""
    if not os.path.exists(path):
        os.makedirs(path)