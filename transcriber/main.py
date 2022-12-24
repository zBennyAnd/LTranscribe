'''
LTranscribe 

Copyright (C) 2022  zBennyAnd

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import os
import tkinter
from os.path import isfile
from tkinter import filedialog
import customtkinter as tk
from datetime import timedelta
import keyboard
import transcriber.timer
from transcriber.player_manager import Player_manager
from PIL import Image, ImageTk

try:
    import vlc
except FileNotFoundError:
    print("----------------------------------------------")
    print("**ERROR** Dependency error: please be sure to had vlc player *64 bit* installed on your computer.")
    print("----------------------------------------------")
    input("Press enter...")

tk.set_appearance_mode("light")
tk.set_default_color_theme("blue")

app = tk.CTk()
app.geometry("500x400")
app.resizable(False, False)
app.title("LTranscribe")

logo = tk.CTkImage(light_image=Image.open("transcriber\logo.png"), size=(30, 30))

ico = Image.open("transcriber\logo.png")
photo = ImageTk.PhotoImage(ico)
app.wm_iconphoto(False, photo)

# -------------Grid Config--------------
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)

app.grid_rowconfigure(1, weight=1)

# ---VLC Player-----
instance = vlc.Instance()
media_player = instance.media_player_new()

# ---Player manager---
p_manager = Player_manager()

# --------------------Function--------
bar_value = 0

# ---Load files----
v_filename = ""
audio_duration = 0

# ---Writing timer
timer = transcriber.timer.Timer(0)


def loadFiles():
    file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                      title="Select audio File",
                                      filetypes=(("MP3 Audio", "*.mp3"),
                                                 ("WAV Audio files", "*.wav"),
                                                 ("all files", "*.*")))
    return startonopen(file)


def startonopen(audio):
    if isfile(audio):
        a = vlc.Media(str(audio))  # create an instance of media
        media_player.set_media(a)
        media_player.play()
        p_manager.audio_loaded_setter(True)
        name_label.configure(text=str(audio.title()))
        a.parse()  # analyse audio to get duration
        duration = a.get_duration()
        slider.set(0)
        update_time()


# Selecting time from time bar
def slider_callback(selected_time):
    media_player.set_time(
        int(selected_time * media_player.get_length())) if selected_time != 0 else media_player.set_position(0)


# Audio jumps 5 seconds behind
def back():
    media_player.set_time(media_player.get_time() - 5000)
    slider.set(slider.get() - (1 / (media_player.get_length() / 1000)) * 5)
    time = timedelta(seconds=media_player.get_time() // 1000)
    time_label.configure(text=time)


# Audio jumps 5 seconds forward
def skip():
    media_player.set_time(media_player.get_time() + 5000)
    slider.set(slider.get() + (1 / (media_player.get_length() / 1000)) * 5)
    time = timedelta(seconds=media_player.get_time() // 1000)
    time_label.configure(text=time)


# ----------Menu------------
menubar_frame = tk.CTkFrame(master=app, height=50)
menubar_frame.grid(row=0, column=1, sticky="new", padx=5, pady=5, ipadx=2, columnspan=2)
menubar_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
open_btn = tk.CTkButton(master=menubar_frame, text="Open File", command=lambda: audio_duration == loadFiles())
open_btn.grid(row=0, column=0, sticky="nw", pady=2, padx=2)
pause_btn = tk.CTkButton(master=menubar_frame, text="⏯", command=lambda: pause())
pause_btn.grid(row=0, column=1, sticky="nw", pady=2, padx=2)
back_btn = tk.CTkButton(master=menubar_frame, text="«", command=back)
back_btn.grid(row=0, column=2, sticky="nw", pady=2, padx=2)
skip_btn = tk.CTkButton(master=menubar_frame, text="»", command=skip)
skip_btn.grid(row=0, column=3, sticky="nw", pady=2, padx=2)
# -----------------Frames----------
logo_btn = tk.CTkButton(master=app, image=logo, text="", fg_color="transparent", hover=False)
logo_btn.grid(row=0, column=0, sticky=tk.NSEW, padx=0, pady=0)
left_frame = tk.CTkFrame(master=app)
right_frame = tk.CTkFrame(master=app)
left_frame.grid(row=1, column=0, sticky=tk.NSEW, padx=0, pady=0)
right_frame.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=0)

name_label = tk.CTkLabel(right_frame, text="")
name_label.place(relx=0.42, rely=0.05, anchor=tkinter.CENTER)
time_label = tk.CTkLabel(right_frame, text="0:00:00")
time_label.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)
# ------------Slider----------------------
slider = tk.CTkSlider(right_frame, from_=0, to=1, command=slider_callback, width=300)
slider._button_corner_radius = 2
slider.set(0)
slider.place(relx=0.42, rely=0.1, anchor=tkinter.CENTER)


def combobox_callback(choice):
    media_player.set_rate(float(choice))


def update_time():
    step = (1 / (media_player.get_length() / 1000)) * float(speed_cb.get())
    time = timedelta(seconds=media_player.get_time() // 1000)
    time_label.configure(text=time)
    if media_player.is_playing():
        slider.set(slider.get() + step)
    app.after(1000, lambda: update_time())


speed_label = tk.CTkLabel(left_frame, text="Speed:")
speed_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
speed_cb = tk.CTkComboBox(left_frame, width=58, values=['0.5', '1.0', '1.2', '1.4'], command=combobox_callback)
speed_cb.set('1.0')
speed_cb.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)

pause_label = tk.CTkLabel(left_frame, text="Pause on\n typing:")
pause_label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

pause_on_typing_sw = tk.StringVar(value="on")


def switch_event():
    if pause_on_typing_sw.get() == "1":
        p_manager.pause_on_typing_setter(True)
    else:
        p_manager.pause_on_typing_setter(False)


pause_switch = tk.CTkSwitch(left_frame, text="", command=switch_event, variable=pause_on_typing_sw, )
pause_switch.place(relx=0.8, rely=0.35, anchor=tkinter.CENTER)
pause_switch.select()


def pause():
    p_manager.pause_on_typing_setter(not p_manager.pause_on_typing_getter())
    media_player.pause()


def back_from_keyboard(event):
    if not app.state() == "iconic":
        back()


def skip_from_keyboard(event):
    if not app.state() == "iconic":
        skip()


def suspend(callback):
    if media_player.is_playing() and p_manager.pause_on_typing_getter():
        media_player.pause()
        timer.time_adder(3000 - timer.time_getter())


def restart_if_not_playing():
    if not media_player.is_playing():
        media_player.pause()


def loop():
    keyboard.on_press(suspend)
    if not timer.time_getter() <= -900 and p_manager.pause_on_typing_getter():
        timer.time_adder(-350)
    elif p_manager.pause_on_typing_getter():
        restart_if_not_playing()
    app.after(200, loop)


def on_closing(self, event=0):
    media_player.stop()
    self.destroy()


app.bind("<Left>", back_from_keyboard)
app.bind("<Right>", skip_from_keyboard)
loop()
app.mainloop()
