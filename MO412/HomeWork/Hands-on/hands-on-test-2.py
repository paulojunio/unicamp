import networkx
import scipy
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    N = 10000
    k = networkx.utils.random_sequence.powerlaw_sequence(N, 2.5)
    print('minimum: ', min(k))
    print('maximum: ', max(k))
    kmin = math.floor(min(k))
    print('Take kmin= ', kmin)
    kmax = math.ceil(max(k))
    print('Take kmax= ', kmax)
    npk = np.array(k)
    upper = math.floor(kmax * 0.9)
    gamma = np.zeros(upper + 1)
    for Kmin in range(kmin, upper + 1):
        npKmin = npk[npk >= Kmin]
        sum_ln = np.sum(np.log(npKmin / (Kmin - 0.5)))
        NKmin = npKmin.size
        gamma[Kmin] = 1 + NKmin / sum_ln
    plt.plot(np.arange(kmin, upper + 1), gamma[kmin:upper + 1])

    plt.show()

    P = [[]] * (upper + 1)
    for Kmin in range(kmin, upper + 1):
        P[Kmin] = np.zeros(kmax - Kmin + 1)
        denom = scipy.special.zeta(gamma[Kmin], Kmin)
        if denom > 0:
            for k in range(Kmin, kmax + 1):
                P[Kmin][k - Kmin] = 1 - scipy.special.zeta(gamma[Kmin], k) / denom
        else:
            for k in range(Kmin + 1, kmax + 1):
                P[Kmin][k - Kmin] = 1
    plt.plot(np.arange(kmax - kmin + 1), P[kmin])
    plt.plot(np.arange(kmax - upper + 1), P[upper])

    plt.show()

    freq = np.zeros(kmax + 1)
    for ki in np.ceil(np.sort(npk)).astype(int):
        freq[ki] += 1
    S = np.zeros(kmax + 1)
    for ki in range(kmin, kmax):
        S[ki + 1] = S[ki] + freq[ki + 1]
    D = np.zeros(upper + 1)
    for Kmin in range(kmin, upper + 1):
        D[Kmin] = np.max(np.abs((S[Kmin:kmax + 1] - S[Kmin]) / (S[kmax] - S[Kmin]) - P[Kmin]))

    plt.subplot(2, 1, 1)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(np.arange(kmin + 1, kmax), freq[kmin + 1:kmax] / N)
    plt.title('Degree distribution')
    plt.ylabel('p_k')

    plt.subplot(2, 1, 2)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(np.arange(kmin + 1, upper), D[kmin + 1:upper])
    plt.title('D')
    plt.ylabel('D')

    plt.show()