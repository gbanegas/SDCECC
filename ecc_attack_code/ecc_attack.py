import random
from itertools import product
from ecc_types import *


m_0 = 3
class AttackECC():

    def __init__(self, ecc, gen_ed25519):
        self.ecc = ecc
        self.gen_data = gen_ed25519;

    def d_solve(self):
        w = 0
        w_prime = 10
        while(w < self.ecc.get_k()):
            pairs_aj_bj = self.generate_aj_bj()



    def generate_aj_bj(self):
        raise NotImplemented()
