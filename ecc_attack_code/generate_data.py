import random
from itertools import product
from ecc_types import *

class Data_Generator():

    def __init__(self, N, random_bits):
        self.N = N
        self.ecc = ECC_ed25519(N, random_bits);
        self.r_j = []


    def generate_r_js(self):
        if(len(self.r_j) == 0):
            self.r_j = self.ecc.generate_r_js()
        return self.r_j

    def generate_alpha_js(self):
        return self.ecc.generate_alpha_js()

    def generate_v_values(self):
        return self.ecc.generate_v_values()

    def get_ecc(self):
        return self.ecc
