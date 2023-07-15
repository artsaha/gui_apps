from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("BMI")

root.geometry("500x600")


meter = ImageTk.PhotoImage(Image.open("meter.png"))
meter_img = Label(root,image=meter, bd=0)
meter_img.pack(pady=20)

h_entry = customtkinter.CTkEntry(master=root,
                                 placeholder_text="Height in inches",
                                 width=200,
                                 height=30,
                                 border_width = 1,
                                 corner_radius = 10)
h_entry.pack(pady = 20)

w_entry = customtkinter.CTkEntry(master=root,
                                 placeholder_text="Height in inches",
                                 width=200,
                                 height=30,
                                 border_width = 1,
                                 corner_radius = 10)
w_entry.pack(pady = 20)

button1 = customtkinter.CTkButton(master=root,
                                 text="Calculate",
                                 width=200,
                                 height=40,
                                    compound='top')
button1.pack(pady = 20)

button2 = customtkinter.CTkButton(master=root,
                                 text="Clear Screen",
                                 width=200,
                                 height=40,
                                    fg_color='#FF5733',
                                  hover_color='#C77C78')
button2.pack(pady = 20)



root.mainloop()