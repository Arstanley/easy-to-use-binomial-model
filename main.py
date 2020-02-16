from model import binomial_model

if __name__ == "__main__":
    bm = binomial_model(400, 1.5, 0.3, 0.02)
    res = bm.calc_v0(400, 1, "EPO")
    print(res)
