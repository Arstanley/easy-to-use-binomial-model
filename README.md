# Binomial Pricing Model for Options

My implementation of the multi-period binomial option pricing model. The model is able to calculate the present price of an option in a fixed time periods (Not suitable for perpetuity). Detailed parameters are discussed below. 

# Instruction

To use the easy-to-use binomial model, download the model.py file to your target directory. Then you can import and use it!
```
from model import binomial_model

bm = binomial_model(8, 2, 0.5, 0.25)
res = bm.calc_v0(22, 2)
```
## Parameters
```
binomial_model(s_0, u, d, r)
```
**s_0**: Stock price at time t0. (Current price of stock)
**u**: Up factor
**d**: Down factor
**r**: Riskless interest rate

```
binomial_model.calc_v0(k, t)
```
**k**: Strike price
**t**: Periods that you want to consider

# Acknowledgement

**Bo Ni** - _Initial Commit_
