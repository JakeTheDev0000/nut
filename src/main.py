import PySimpleGUI as sg
import webbrowser as web

sg.theme('DarkAmber')
layout = [
    [sg.Button('Nut'),] 
    ]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == "Nut":
        web.open("https://www.youtube.com/watch?v=w0AOGeqOnFY")

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()