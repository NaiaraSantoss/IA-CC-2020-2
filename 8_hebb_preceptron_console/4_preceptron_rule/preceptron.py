import numpy as np

class Preceptron:
    def __int__(self):
        self.pesosbias = 0
        self.theta = 0
        self.taxaaprendizado = 1
        self.numentrada = 0
        self.net = 0
        self.w_peso = []
        self.training_data = []

    def up (self, training_data, bias, theta, taxaaprendizado):
        self.training_data = training_data
        self.pesosbias = bias
        self.theta = theta
        self.taxaaprendizado = taxaaprendizado
        self.w_peso = []
        self.numepoch = -1
        self.numentrada = len(self.training_data[0][0])
        self.init_w_peso()
    def init_w_peso(self):
        for i in range(self.numentrada):
            self.w_peso.append(0)
    def calculanet(self, inputs):
        net = 0.0
        for i in range(len(inputs)):
            net += inputs[i] * self.w_peso[i]
        net += self.pesosbias
        return net
    def calculodesaida (self, net):
        if net > self.theta:
            return 1
        elif net < 1 - self.theta:
            return -1
        else:
            return 0
    def checkandbreak(self, old_weight, old_pesosbias):
        for i in range(len(self.w_peso)):
            if self.w_peso[i] != old_weight[i]:
                return False
        if self.pesosbias != old_pesosbias:
            return False
        return True
    def train(self):
        old_weights = list(self.w_peso)
        old_pesosbias = self.pesosbias
        for training_t in self.training_data:
            inputs = training_t[0]
            target = training_t[1]
            output = self.calculodesaida(self.calculanet(inputs))
            if output != target:
                for i in range(self.numentrada):
                    self.w_peso[i] = self.w_peso[i] + self.taxaaprendizado * inputs[i] * target
                    self.pesosbias = self.pesosbias + self.taxaaprendizado * inputs[i] * target
                self.pesosbias = self.pesosbias + self.taxaaprendizado * target
        if self.checkandbreak(old_weights, old_pesosbias):
            self.numepoch += 1
            return self.w_peso
        else:
            self.numepoch += 1
            return self.train()
    def print(self):
        print("Inputs\t\t Target")
        for x1 in self.training_data:
            print(x1[0], "\t\t", x1[1])
        print("\nWeights: ")
        for w in range(len(self.w_peso)):
            print("\tw0 = " + str(w) + "\n\tw1 =" + str(self.w_peso[w]))
            print("\twb = " + str(self.pesosbias))
            print("epochs: " + str(self.numepoch))

if __name__ == "__main__":
    x1 = [([1, 1], 1),
          ([1, -1], -1),
          ([-1, 1], -1),
          ([-1, -1], -1)
          ]

    preceptron_ = Preceptron()
    preceptron_.up(x1, 0, 0, 1)
    preceptron_.train()
    preceptron_.print()