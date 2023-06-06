import PySimpleGUI as sg

sg.theme('LightGrey')  

layout = [ 
            [sg.Text('IMC')],
            [sg.Text('Massa:'),sg.Input(key= '-MASS-', size=(5,1))],
            [sg.Text('Altura:'),sg.Input(key= '-HEIGHT-', size=(5,1))],
            [sg.Button('Calcular')]
         ]

window = sg.Window('IMC', layout=layout, font='Monaco 26', element_justification='center')

while True:
    event, values = window.read() 
    print(event, values)
    Massa = float(values['-MASS-'])
    Altura = float(values['-HEIGHT-'])
    IMC = Massa/(Altura**2)
    sg.Popup(f'Seu IMC é {IMC:.2f}', font='22')
    if event == 'QUIT' or event == sg.WIN_CLOSED:     
      break
