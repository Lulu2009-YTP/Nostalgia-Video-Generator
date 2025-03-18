import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from moviepy.editor import *
from effects_processor import EffectsProcessor
import random
from PIL import Image, ImageTk

class NostalgiaVideoGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nostalgia Video Generator")
        self.root.geometry("800x600")
        
        self.input_video = None
        self.output_path = None
        self.effects_processor = EffectsProcessor()
        
        self.setup_ui()
    
    def setup_ui(self):
        # File Selection Frame
        file_frame = ttk.LabelFrame(self.root, text="File Selection", padding="10")
        file_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(file_frame, text="Select Video", command=self.select_video).pack(side="left", padx=5)
        ttk.Button(file_frame, text="Select Output Location", command=self.select_output).pack(side="left", padx=5)
        
        # Effects Frame
        effects_frame = ttk.LabelFrame(self.root, text="Effects", padding="10")
        effects_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Visual Effects
        visual_frame = ttk.LabelFrame(effects_frame, text="Visual Effects")
        visual_frame.pack(fill="x", padx=5, pady=5)
        
        self.zoom_var = tk.BooleanVar()
        self.glow_var = tk.BooleanVar()
        self.mirror_var = tk.BooleanVar()
        self.swirl_var = tk.BooleanVar()
        
        ttk.Checkbutton(visual_frame, text="Random Zoom/Pan", variable=self.zoom_var).pack(side="left", padx=5)
        ttk.Checkbutton(visual_frame, text="Glow Effect", variable=self.glow_var).pack(side="left", padx=5)
        ttk.Checkbutton(visual_frame, text="Mirror Effect", variable=self.mirror_var).pack(side="left", padx=5)
        ttk.Checkbutton(visual_frame, text="Swirl Effect", variable=self.swirl_var).pack(side="left", padx=5)
        
        # Audio Effects
        audio_frame = ttk.LabelFrame(effects_frame, text="Audio Effects")
        audio_frame.pack(fill="x", padx=5, pady=5)
        
        self.pitch_var = tk.BooleanVar()
        self.echo_var = tk.BooleanVar()
        self.reverb_var = tk.BooleanVar()
        
        ttk.Checkbutton(audio_frame, text="Random Pitch Shift", variable=self.pitch_var).pack(side="left", padx=5)
        ttk.Checkbutton(audio_frame, text="Echo Effect", variable=self.echo_var).pack(side="left", padx=5)
        ttk.Checkbutton(audio_frame, text="Reverb", variable=self.reverb_var).pack(side="left", padx=5)
        
        # Generate Button
        ttk.Button(self.root, text="Generate Video", command=self.generate_video).pack(pady=10)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, length=300, mode='determinate')
        self.progress.pack(pady=10)
        
    def select_video(self):
        self.input_video = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
        )
        
    def select_output(self):
        self.output_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("MP4 files", "*.mp4")]
        )
        
    def generate_video(self):
        if not self.input_video or not self.output_path:
            messagebox.showerror("Error", "Please select input video and output location")
            return
            
        try:
            # Create effect configuration
            effect_config = {
                'zoom': self.zoom_var.get(),
                'glow': self.glow_var.get(),
                'mirror': self.mirror_var.get(),
                'swirl': self.swirl_var.get(),
                'pitch': self.pitch_var.get(),
                'echo': self.echo_var.get(),
                'reverb': self.reverb_var.get()
            }
            
            # Process video with effects
            self.effects_processor.process_video(
                self.input_video,
                self.output_path,
                effect_config,
                progress_callback=self.update_progress
            )
            
            messagebox.showinfo("Success", "Video generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def update_progress(self, value):
        self.progress['value'] = value
        self.root.update_idletasks()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NostalgiaVideoGenerator()
    app.run()