import numpy as np

p = np.poly1d([1.0, -3.0, 2.0, 0.0])
t = np.poly1d([1.0, -3.0, 2.0])


############
## p = t * h
############

'''
verifier samples a random secret s and calc their encrypted powers
'''
s = np.random.randint(low=0, high=20)
alpha = np.random.randint(low=0, high=20)
g = 5
n = 7

vec_E = np.vectorize(lambda v: (g ** v) % n)

enc_s = vec_E(np.power(s, np.arange(0, 4)))
shift_enc_s = vec_E(alpha*np.power(s, np.arange(0, 4)))

ts = t(s)

'''
prover receives encrypted powers of s and evals them on h and p
'''


enc_ps = np.prod(np.power(enc_s[:len(p.coef)], list(reversed(p.coef))))
shift_enc_ps = np.prod(
    np.power(shift_enc_s[:len(p.coef)], list(reversed(p.coef))))

'''
verifier checks if p(s) = t(s) * h(s) (encoded)  
... prover deliveres encoded p(s) and h(s)
'''
print(f'is valid {shift_enc_ps == enc_ps ** alpha }')

print('fin')
