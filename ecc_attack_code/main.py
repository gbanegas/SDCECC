import ecc_attack
from generate_data import Data_Generator

n = 50
N = 500
def main():
    print("dummy")
    gen_ed25519 = Data_Generator(N,0)
    print (gen_ed25519.generate_r_js())


if __name__ == "__main__":
    main()
