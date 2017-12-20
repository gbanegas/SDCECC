import random
from itertools import product
from ecc_types import *

class Data_Generator():

    def __init__(self, N, random_bits):
        self.ecc = ECC_ed25519(N, random_bits);


    def generate_r_js(self):
        return self.ecc.generate_r_js()

    def generate_alpha_js(self):
        return self.ecc.generate_alpha_js()

    def generate_v_values(self):
        return self.ecc.generate_v_values()
