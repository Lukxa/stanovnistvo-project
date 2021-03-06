import numpy
import PySimpleGUI as sg


layout = [
    [sg.Text("Stanovnistvo", background_color=("#FFFFFF"), text_color=("#000000"),font = (", 30"))],
    #[sg.Text("",background_color=("#FFFFFF"))],
    [sg.Text("Unesite podatke:", background_color=("#FFFFFF"), text_color=("#000000"), font=(", 15"))],
    [sg.Text("Unesite pocetnu populaciju (n0)", background_color=("#FFFFFF"), text_color=("#000000"),font = (", 13")),sg.Input(key = "n0")],
    [sg.Text("Unesite trenutnu populaciju (n1)", background_color=("#FFFFFF"), text_color=("#000000"),font = (", 13")),sg.Input(key = "n1")],
    [sg.Text("Unesite vremenski interval (t)", background_color=("#FFFFFF"), text_color=("#000000"),font = (", 13")),sg.Input(key = "t")],
    [sg.Button("Continue", key = "-CONTINUE-")],
    [sg.Text("", key = "-RESULT-", background_color=("#FFFFFF"), text_color=("#000000"),font = (", 15"))]
]

window = sg.Window("Stanovnistvo", layout, background_color='#FFFFFF', size=(650,270))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONTINUE-":
        n0 = values["n0"]
        n1 = values["n1"]
        t = values["t"]

        if "," in n0:
            n0 = n0.replace(",", ".")
        if "," in n1:
            n1 = n1.replace(",", ".")
        if "," in t:
            t = t.replace(",", ".")

        n0 = eval(n0)
        n1 = eval(n1)
        t = eval(t)

        c = n1 / n0
        k = numpy.log(c)
        k = k / t
        t1 = numpy.log(0.5)
        t1 = t1 / k
        result = f't={t1}'

        window["-RESULT-"].update(result)

