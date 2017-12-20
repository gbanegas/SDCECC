from ecc_attack import AttackECC
from generate_data import Data_Generator

n = 50
N = 500
def main():
    print("dummy")
    gen_ed25519 = Data_Generator(N,0)
    attack = AttackECC(gen_ed25519.get_ecc(), gen_ed25519)
    attack.d_solve()


if __name__ == "__main__":
    main()
