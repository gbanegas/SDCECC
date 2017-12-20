import random
import math
from itertools import product
from ecc_types import *


def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

class AttackECC():

    def __init__(self, ecc, gen_ed25519):
        self.ecc = ecc
        self.gen_data = gen_ed25519
        self.to_divide = float(2**self.ecc.get_k())
        self.m_0 = 5

    def d_solve(self):
        w = 0
        w_prime = 10
        while(w < self.ecc.get_k()):
            a_j , b_j = self.generate_aj_bj(w,w_prime)
            #d_candidates = self.select_candidates(pairs_aj_bj)



    def generate_aj_bj(self, w, w_prime):
        a_j =[]
        b_j =[]
        for i in range(self.ecc.N):
            a = math.floor(float(float(self.gen_data.generate_v_values()[i]) / self.to_divide)) % (2**w)
            b = self.gen_data.generate_v_values()[i] % (2**w)
            if self.__diff__(a,b,w_prime):
                print("storing ")
                a_j.append(a)
                b_j.append(b)
        return a_j, b_j

    def select_candidates(self, pairs):
        raise NotImplementedError()

    def __diff__(self, a,b, w_prime):
        bit_a = bitfield(a)
        bit_b = bitfield(b)
        print ("a = ", a)
        print ("bit_a = ", bit_a)
        print ("b = ", a)
        print ("bit_b = ", bit_b)
        if len(bit_a) > len(bit_b):
            bit_b = bit_b + [0]*(len(bit_a)-len(bit_b))
        else:
            bit_a = bit_a + [0]*(len(bit_b)-len(bit_a))
        diff = 0
        for i in range(w_prime):
            if( i < len(bit_a) and i < len(bit_b)):
                if bit_a[i] != bit_b[i]:
                    diff+=1

        return self.m_0 > diff
