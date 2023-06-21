import tkinter as tk
import tkinter.messagebox
import requests as re
from tkinter import colorchooser
import json

baseURL = "http://192.168.10.17/api/sNDipGkVt7TdC4dWd7AU6DwXM0uw5prYyPgWVetI/"

root = tk.Tk()
root.title("Lyskontroll")

default = re.get(baseURL)
if default.status_code == 200:
    pass
if default.status_code == 400:
    tk.messagebox.showerror("Feil!", "Ingen svar fra Phillips Hub")
    exit

def off():
    for i in range(1, 6):
        url = baseURL + "lights/{}/state".format(i)
        payload = {"on": False}
        response = re.put(url, json=payload)
        print(response.json())

def rgb2cie(r, g, b):
    X = 0.412453 * r + 0.357580 * g + 0.180423 * b
    Y = 0.212671 * r + 0.715160 * g + 0.072169 * b
    Z = 0.019334 * r + 0.119193 * g + 0.950227 * b

    if (X + Y + Z) == 0:
        x = y = 0
    else:
        x = X / (X + Y + Z)
        y = Y / (X + Y + Z)
    
    return (x, y)

def velg_farge(kilde, popup):
    popup.destroy()
    color_code = colorchooser.askcolor(title ="Velg en farge")
    rgb, hex = color_code
    r, g, b = rgb
    result = rgb2cie(r, g, b)
    x, y = result
    if kilde == "preben":
        url = baseURL + "lights/5/state"
        payload = {"xy": [x, y]}
        if x + y == 0:
            payload = {"on": False}
        re.put(url, json=payload)

        if kilde == "anders":
            url = baseURL + "lights/4/state"
            payload = {"xy": [x, y]}
            if x + y == 0:
                payload = {"on": False}
                re.put(url, json=payload)

            if kilde == "spisebord":
                url = baseURL + "lights/1/state"
                payload = {"xy": [x, y]}
                if x + y == 0:
                    payload = {"on": False}
                    re.put(url, json=payload)        

                    if kilde == "Lys1":
                        url = baseURL + "lights/2/state"
                        payload = {"xy": [x, y]}
                        if x + y == 0:
                            payload = {"on": False}
                            re.put(url, json=payload)

                        if kilde == "Lys2":
                            url = baseURL + "lights/3/state"
                            payload = {"xy": [x, y]}
                            if x + y == 0:
                                payload = {"on": False}
                                re.put(url, json=payload)
                            else:
                                tk.messagebox.showerror("Feil!", "Ugyldig referanse")

def lyspå(kilde):
    if kilde == "preben":

        print("Preben")
    if kilde == "anders":

        print("Anders")
    if kilde == "spisebord":

        print("Spisebord")
    if kilde == "Lys1":

        print("lys1")
    if kilde == "Lys2":

        print("lys2")

def lysav(kilde):
    if kilde == "preben":
        url = baseURL + "lights/5/state"
        payload = {"on": False}
        re.put(url, json=payload)



        if kilde == "anders":

            print("Anders")
            if kilde == "spisebord":

                print("Spisebord")
                if kilde == "Lys1":

                    print("lys1")
                    if kilde == "Lys2":

                        print("lys2")
                    else:
                        tk.messagebox.showerror("Feil!", "Ugyldig referanse")
        
def lysfarge(kilde):
    if kilde == "preben":
        url = baseURL + "lights/5/state"

        # Kode her

        if kilde == "anders":
            url = baseURL + "lights/4/state"

            # Kode her

            if kilde == "spisebord":
                url = baseURL + "lights/1/state"
                
                # Kode her

                if kilde == "Lys1":
                    url = baseURL + "lights/2/state"

                    # kode her

                    if kilde == "Lys2":
                        url = baseURL + "lights/3/state"
                        
                        # KODE HER

                    else:
                        tk.messagebox.showerror("Feil!", "Ugyldig referanse")

def on():
    for i in range(1, 6):
        url = baseURL + "lights/{}/state".format(i)
        payload = {"on": True}
        response = re.put(url, json=payload)
        print(response.json())

def anders():
    tk.Button(root)
    
def spisebord():
    tk.Button(root)

def lys1():
    tk.Button(root)

def lys2():
    tk.Button(root)

"""
def lysstyrke(Meter, kilde):
    Nivå = Meter.get()
    if kilde == "preben":
        print("Trigget fra Preben")
        url = baseURL + "lights/5/state"
        Nivå = int(Nivå)
        payload = {"bri": Nivå}
        r = re.put(url, payload)
        print(r.content)
        print(payload)
        print(type(payload))

    
    if kilde == "anders":
        print("Trigget fra Anders")
        url = baseURL + "lights/4/state"
        print("Anders fn")

    if kilde == "anders":
        url = baseURL + "lights/4/state"
        print("Anders fn")

    if kilde == "anders":
        url = baseURL + "lights/4/state"
        print("Anders fn")

    if kilde == "anders":
        url = baseURL + "lights/4/state"
        print("Anders fn")

    if kilde == "anders":
        url = baseURL + "lights/4/state"
        print("Anders fn")
"""

def preben():
    popup = tk.Tk()

    På = tk.Button(popup, text="På", command=lambda: lyspå("preben"))
    På.grid(row=0, column=0)

    Av = tk.Button(popup, text="Av", command=lambda: lysav("preben"))
    Av.grid(row=0, column=1)

    Farge = tk.Button(popup, text="Velg farge", command=lambda: velg_farge("preben", popup))
    Farge.grid(row=1, column=0, columnspan=2)

    Meter = tk.Scale(popup, from_=254, to=-254, orient="vertical")
    Meter.grid(row=1, column=3)

    # Ok = tk.Button(popup, text="OK", width=8, command=lambda: lysstyrke(Meter, "preben"))
    # Ok.grid(row=0, column=3, columnspan=2)

on_button = tk.Button(root, text="Alle på", command=on)
on_button.grid(row=0, column=4, rowspan=2)

off_button = tk.Button(root, text="Alle av", command=off)
off_button.grid(row=0, column=6, rowspan=2)

preben_button = tk.Button(root, text="Preben", command=preben)
preben_button.grid(row=5, column=6, rowspan=1)

anders_button = tk.Button(root, text="Anders", command=anders)
anders_button.grid(row=4, column=6, rowspan=1)

spisebord_button = tk.Button(root, text="Spisebord", command=spisebord)
spisebord_button.grid(row=4, column=5, rowspan=1)

lys1_button = tk.Button(root, text="Tak 1", command=lys1)
lys1_button.grid(row=4, column=4, rowspan=1)

lys2_button = tk.Button(root, text="Tak 2", command=lys2)
lys2_button.grid(row=5, column=4, rowspan=1)

root.mainloop()

# 1 = Spisebord
# 2 = Over trapp 1
# 3 = Over trapp 2
# 4 = Anders
# 5 = Preben - OK

