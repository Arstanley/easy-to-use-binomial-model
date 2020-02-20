# Binomial Pricing Model for Options

My implementation of the multi-period binomial option pricing model. The model is able to calculate the present price of an option in a fixed time periods (Not suitable for perpetuity). Detailed parameters are discussed below. 

## Instruction

To use the easy-to-use binomial model, download the model.py file to your target directory. Then you can import and use it!
```
from model import binomial_model

bm = binomial_model(8, 2, 0.5, 0.25)
res = bm.calc_v0(22, 2， model="ECO") # Returns 1.6
```
### Parameters
```
binomial_model(s_0, u, d, r)
```
**s_0**: Stock price at time ![equation](http://latex.codecogs.com/gif.latex?t_0)  (Current price of stock)
<br />
**u**: Up factor <br />
**d**: Down factor <br />
**r**: Riskless interest rate <br />

```
binomial_model.calc_v0(k, t, model="ECO")
```
**k**: Strike price <br />
**t**: Periods that you want to consider <br />
**model**: You can choose to calculate European Call Option(ECO) or European Put Option(EPO) <br />

## Acknowledgement

**Bo Ni** - _Initial Commit_
