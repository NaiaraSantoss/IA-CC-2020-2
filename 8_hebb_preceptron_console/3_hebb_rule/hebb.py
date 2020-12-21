# Inputs
x1 = [-1, 1, -1, 1]
x2 = [-1, -1, 1, 1]

# Output
target = [-1, -1, -1, 1]

# inicialização dos pesos - deltas
w1o = []
w2o = []
bo = []

ke = 0
for i in x1:
    w1o.append(i*target[ke])
    ke = ke + 1

ke = 0
for i in x2:
    w2o.append(i * target[ke])
    ke = ke + 1

# Pesos
w1 = []
w2 = []
bo = []

w1.append(w1o[0])
w2.append(w2o[0])
bo.append(target[0])

# pesos
ke = 0
while ke != 3:
    w1.append(w1o[ke+1] + w1[ke])
    w2.append(w2o[ke+1] + w2[ke])
    bo.append(bo[ke] + target[ke+1])
    ke = ke +1

#pesos após o treinamento
print("Inputs")
print(x1)
print(x2)

print ("Target")
print(target)

print("w0 =", w1[3])
print("w1 =", w2[3])
print("w2 =", bo[3])