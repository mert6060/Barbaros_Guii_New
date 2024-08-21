import tkinter as tk
import time
import random
import tkintermapview
from datetime import datetime
import firebase_admin

status = 1  # GUI'nin çalışıp çalışmayacağını kontrol eden değişken

root = tk.Tk()
root.title("Barbaros User Interfaces")
root.geometry("810x480")
root.configure(bg="#2c3e50")

# Başlangıç mesajları
message_label = tk.Label(root, text="Sürüş Başlatılıyor...", font=("Helvetica", 45), fg="white", bg="#2c3e50")
message_label.pack(pady=50)



safety_message = tk.Label(root, text="Can yeleğini takınız...\nGüvenli sınırlar oluşturuluyor...", font=("Helvetica", 28), fg="white", bg="#2c3e50")
safety_message.pack(pady=70)

canvas = tk.Canvas(root, width=200, height=100, bg="#2c3e50", highlightthickness=0)
canvas.pack(pady=90)

circle1 = canvas.create_oval(10, 40, 30, 60, fill="white", outline="white")
circle2 = canvas.create_oval(50, 40, 70, 60, fill="white", outline="white")
circle3 = canvas.create_oval(90, 40, 110, 60, fill="white", outline="white")

map_width = 500
map_height = 440
map_widget = tkintermapview.TkinterMapView(root, width=map_width, height=map_height, corner_radius=25)

vehicleinfo_label = tk.Label(root, text="Araç Durumu ", font=("Helvetica", 28,"bold"), fg="white", bg="#2c3e50")
vehicleinfo_label.forget()

# Tarih ve saat etiketi (Arka plan root ile aynı renkte yapıldı)
datetime_label = tk.Label(root, font=("Helvetica", 24), fg="white", bg="#2c3e50")
datetime_label.place_forget()

def update_datetime():
    current_datetime = datetime.now().strftime("24-09-%d\n%H:%M:%S")
    datetime_label.config(text=current_datetime, font="14")
    root.after(1000, update_datetime)

update_datetime()

temperature_label = tk.Label(root, text="Sıcaklık: -- °C", font=("Helvetica", 24), fg="white", bg="#2c3e50")
temperature_label.place_forget()

depht_label = tk.Label(root, text="Derinlik:  -- m", font=("Helvetica", 24), fg="white", bg="#2c3e50")
depht_label.place_forget()

speed_label = tk.Label(root, text="Hız:  -- m", font=("Helvetica", 24), fg="white", bg="#2c3e50")
speed_label.place_forget()

battery_label = tk.Label(root, text="Pil Durumu:% --", font=("Helvetica", 24), fg="white", bg="#2c3e50")
battery_label.pack_forget()

marker_2 = map_widget.set_marker(10, 10)

konumlar = [
    (36.1562, 28.9403),
    (36.3565, 28.9405),
    (36.7568, 28.9407),
    (36.9570, 28.9410)
]

def marker_hareket():
    for konum in konumlar:
        marker_2.set_position(konum[0], konum[1])
        root.update()
        time.sleep(4)

def update_temperature():
    temperature = random.uniform(23.0, 25.0)
    temperature_label.config(text=f"Sıcaklık: {temperature:.1f} °C")
    root.after(2000, update_temperature)

def update_speed():
    speed = random.uniform(2.0, 4.0)
    speed_label.config(text=f"Hız: {speed:.1f} knot")
    root.after(2000, update_speed)

def update_depth():
    depth = random.uniform(2.0, 8.0)
    depht_label.config(text=f"Derinlik: {depth:.1f} m")
    root.after(2000, update_depth)
    
def update_battery():
    battery = random.uniform(85.0, 87.0)
    battery_label.config(text=f"Pil:% {battery:.1f} ")
    root.after(2000, update_battery)


def animate_circles(step=0):
    if step == 0:
        canvas.itemconfig(circle1, fill="white")
        canvas.itemconfig(circle2, fill="#2c3e50")
        canvas.itemconfig(circle3, fill="#2c3e50")
    elif step == 1:
        canvas.itemconfig(circle1, fill="#2c3e50")
        canvas.itemconfig(circle2, fill="white")
        canvas.itemconfig(circle3, fill="#2c3e50")
    elif step == 2:
        canvas.itemconfig(circle1, fill="#2c3e50")
        canvas.itemconfig(circle2, fill="#2c3e50")
        canvas.itemconfig(circle3, fill="white")

    root.update()
    next_step = (step + 1) % 3
    if canvas.winfo_exists():
        root.after(300, animate_circles, next_step)

def start_animation():
    animate_circles()
    root.after(1700, show_map)

def show_map():
    if canvas.winfo_exists():
        message_label.destroy()
        safety_message.destroy()
        canvas.destroy()

    root.update_idletasks()
    map_widget.place(x=280, y=10)
    map_widget.set_position(36.7560, 28.9401)
    map_widget.set_zoom(13)

    root.after(2000, update_temperature)
    root.after(2000, update_depth)
    root.after(2000, update_speed)
    root.after(2000,update_battery)
    root.after(0, marker_hareket)

    vehicleinfo_label.place(x=25, y=10)
    temperature_label.place(x=15, y=80)
    depht_label.place(x=15, y=150)
    speed_label.place(x=15, y=220)
    battery_label.place(x=15, y=290)
    datetime_label.place_forget(x=300, y=410)

    line_canvas = tk.Canvas(root, width=195, height=10, bg="#2c3e50", highlightthickness=0.3)
    line_canvas.place(x=30, y=50)
    line_canvas.create_line(0, 0, 200, 0, fill="white", width=3)

if status == 1:
    start_animation()
    root.mainloop()

