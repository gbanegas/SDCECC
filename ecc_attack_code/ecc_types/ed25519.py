from .ECC import ECC
import random
import math


d = 123983737618
q = 2**252 + 27742317777372353535851937790883648493
k = 252
t = 124
g = 127
r = []
v = []
alpha = []

class ECC_ed25519(ECC):

    def __init__(self, N, random_bits):
        self.N = N;
        self.n = random_bits;

    def generate_v_values(self):
        if(len(alpha) == 0):
            self.generate_alpha_js();
        for i in range(0, self.N):
            value = d + (alpha[i]*q)
            v.append(value)
        return v

    def  generate_alpha_js(self):
        if(len(r) == 0):
            self.generate_r_js();
        for i in range(1, self. N+1):
            al = r[i] - r[0]
            alpha.append(int(math.fabs(al)))
        return alpha

    def  generate_r_js(self):
        for i in range(0, self.N+1):
            a = 1
            if(self.n != 0):
                a = random.getrandbits(self.n)
            r.append(int(math.fabs(a)))
        return r

    def get_k(self):
        return k

    def get_g(self):
        return g

    def get_t(self):
        return t
