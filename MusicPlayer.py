import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x150")

        pygame.init()
        pygame.mixer.init()

        self.playlist = []
        self.current_song = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Play button
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        # Pause button
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        # Stop button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        # Add music button
        self.add_button = tk.Button(self.root, text="Add Music", command=self.add_music)
        self.add_button.pack()

        # Label to display the current song name
        self.song_label = tk.Label(self.root, textvariable=self.current_song)
        self.song_label.pack()

    def play_music(self):
        if len(self.playlist) == 0:
            return

        song_path = self.playlist[0]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.current_song.set(os.path.basename(song_path))

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    def add_music(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3",filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")])

        if file_path:
            self.playlist.append(file_path)
            self.current_song.set(os.path.basename(file_path))

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
