import numpy as np
import math
import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox
import os

# Definições dimensões
w = 8 
h = 10 
input_size = w * h
es = np.zeros((w, h))

# pesos e bias

weights = {} #peso
bias = {}
threshold = 0
TA = 1 #taxa de aprendizado
max_iterations = 10 #epoch

#arquivo

def open_file(file):
    result = np.zeros((w,h))
    lines = [line.rstrip('\n') for line in open(file)]
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            result[x, y] = 1 if ch == '*' else 0
    return result

#treinamento

def train(input):
    weights = {}   # peso
    bias = {}      # bias

    # inicia valores com 0
    for key in input:
        weights[key] = np.zeros(input_size)
        bias[key] = 0

    # treinando os dados
    trained = False
    for epoch in range(max_iterations):  # iterações - épocas
        trained = True

        for key, samples in input.items():        # percorre todos os caracteres
            target = {}                           #início
            for num in input:
                target[num] = 1 if num == key else -1

            for sample_index, sample in enumerate(samples):  
                for num, t in target.items():            # todos os valores
                    y_in = bias[num]                     # dá o valor das bias
                    for i in range(input_size):
                        y_in += sample[i] * weights[num][i]  # matrix valor

                    if y_in > threshold: 
                        y = 1
                    elif y_in < -threshold:
                        y = -1
                    else:
                        y = 0
                    if y != t:
                        error = t - y
                        bias[num] = bias[num] + TA * error
                        for i in range(input_size):
                            weights[num][i] = weights[num][i] + TA * sample[i] * error
                        trained = False
        if trained: 
            break
    return (trained, weights, bias, epoch)

def train_folder():
    global weights, bias
    
    
    dir_path = os.getcwd() + '/dados_treinamento/'
    data = {}
    for file in os.listdir(dir_path):
        if file.endswith('.txt'):   # arquivos em txt
            ch = str(file[0])
            if not ch in data:
                data[ch] = []
            matrix = open_file(dir_path + file) # load arquivo para  matrix
            matrix = matrix.reshape(input_size) # mudar para dimensão única
            matrix[matrix == 0] = -1     # update
            data[ch].append(matrix)      # insere dados do treino no dicionário
    trained, weights, bias, epoch = train(data)
    print('Resultado do treinamento: %s, Iterações: %d'%(trained,epoch))
    return (trained, epoch)

def test(input):
    found = []
    input[input == 0] = -1  # update
    for num, weight in weights.items():
        y_in = bias[num]
        for s, w in zip(input, weight):
            y_in += s * w
        if y_in > threshold:
            found.append(num)
    return found 




# GUI - INTERFACE
from tkinter import *
root = Tk()
root.title('Reconhecimento de Caracteres')

frame = Frame()
frame.pack(padx=10, pady=10)
#root.geometry("700x550")

toolbar = Frame(frame)
toolbar.pack(fill=X)

# Botão
def load_callback():
    global es
    file = fdialog.askopenfilename()
    if file != '':
        es = open_file(file)
    print_grid()

Button(toolbar, text="Load", command = load_callback).pack(side=LEFT)

# Botão salvar
def save_callback():
    file = fdialog.asksaveasfile(mode='w', defaultextension=".txt")

    for y in range(h):
        for x in range(w):
            file.write('.' if es[x,y] == 0 else '*')
        file.write('\n')
    file.close()

#Button(toolbar, text="Salvar", command = save_callback).pack(side=LEFT)

def clear_callback():
    np.ndarray.fill(es, 0)
    print_grid()

Button(toolbar, text="Limpar", command = clear_callback).pack(side=LEFT)
    
Label(toolbar, text='Taxa de aprendizado').pack(side=LEFT, padx = 10)
learning_rate_field = Entry(toolbar, textvariable=StringVar(root, value=TA), width=8)
learning_rate_field.pack(side=LEFT)

Label(toolbar, text='Threshold').pack(side=LEFT, padx = 10)
threshold_field = Entry(toolbar, textvariable=StringVar(root, value=threshold), width=8)
threshold_field.pack(side=LEFT)

Label(toolbar, text='Max. Iterations').pack(side=LEFT, padx = 10)
max_iterations_field = Entry(toolbar, textvariable=StringVar(root, value=max_iterations), width=8)
max_iterations_field.pack(side=LEFT)

def train_callback():
    global weights, bias, threshold, TA, max_iterations
    threshold = float(threshold_field.get())
    TA = float(learning_rate_field.get())
    max_iterations = int(max_iterations_field.get())
    trained, epoch = train_folder()
    

Button(toolbar, text="TRAIN", command = train_callback).pack(side=LEFT)
    
def weights_and_bias_callback():
    window = Toplevel(root)
    window.title('Pesos & Bias')
    text = Text(window, width=100, height=50)
    weights_value = ''
    for num, value in weights.items():
        weights_value += '%s\n%s\n' %(num, value)
    text.insert(END, 'Learning Rate: %s, Threshold: %s,\nWEIGHTS\n%s\nBIAS\n%s' %(TA, threshold, weights_value, bias))
    text.pack()

Button(toolbar, text="Pesos & Bias", command = weights_and_bias_callback).pack(side=LEFT)

# GRID
def mouseClick(event):
    x = math.floor(event.x / rect_size)
    y = math.floor(event.y / rect_size)
    if x < w and y < h: es[x, y] = 0 if es[x, y] > 0 else 1 # zero e um
    print_grid()
    
rect_size = 50  # grid tamanho do retângulo
canvas = Canvas(frame, width=rect_size*w, height=rect_size*h)
canvas.bind("<Button-1>", mouseClick)
canvas.pack(fill=X, pady=2)

# Desenho GRID
def print_grid():
    for i in range(w):
        for j in range(h):
            color = 'black' if es[i, j] > 0 else 'white'
            canvas.create_rectangle(i * rect_size, j * rect_size, (i + 1) * rect_size, (j + 1) * rect_size, outline="black", fill=color)
print_grid();

# BOTTOM 
bottom_bar = Frame(frame, height=50)
bottom_bar.pack(fill=X)

def test_callback():
    input = es.copy().reshape(input_size)
    found = test(input)
    
    if len(found) > 0:
        test_result_field_value.set(', '.join(found))
    else:
        test_result_field_value.set('???')
    
Button(bottom_bar, text="RUN", command = test_callback).pack(side=LEFT)

Label(bottom_bar, text='Resultado').pack(side=LEFT, padx = 20)
test_result_field_value = StringVar()
test_result_field = Entry(bottom_bar, width=20, textvariable=test_result_field_value)
test_result_field.pack(side=LEFT, padx = 10)


    

root.mainloop()

