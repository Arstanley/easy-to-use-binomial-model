from model import binomial_model, Node

if __name__ == "__main__":
    bm = binomial_model(8, 2, 0.5, 0.25)
    res = bm.calc_v0(22, 2)
    print(res)
