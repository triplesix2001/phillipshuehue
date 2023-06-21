import tkinter as tk
import requests as r
baseURL = "http://192.168.10.17/api/sNDipGkVt7TdC4dWd7AU6DwXM0uw5prYyPgWVetI/"

def off():
    for i in range(1, 6):
        url = baseURL + "lights/{}/state".format(i)
        payload = {"on": False}
        response = r.put(url, json=payload)
        print(response.json())


def on():
    for i in range(1, 6):
        url = baseURL + "lights/{}/state".format(i)
        payload = {"on": True}
        response = r.put(url, json=payload)
        print(response.json())

root = tk.Tk()
root.title("lyskontroll")

off_button = tk.Button(root, text="OFF", command=off)
off_button.pack()

on_button = tk.Button(root, text="ON", command=on)
on_button.pack()

root.mainloop()

# 1 = Spisebord
# 2 = Over trapp 1
# 3 = Over trapp 2
# 4 = Anders
# 5 = Preben - OK

