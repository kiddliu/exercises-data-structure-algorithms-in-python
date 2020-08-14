'''
R-3.1 Graph the functions 8n, 4nlogn, 2n^2, n^3, and 2^n using a logarithmic scale for the x- and y-axes;
that is, if the function value f (n) is y, plot this as a point with x-coordinate at logn and y-coordinate at logy.
'''
import math
import matplotlib.pyplot as plt
import numpy as np

def main31():
    n = np.arange(0., 17.)
    fig, ax = plt.subplots()

    ax.set_xscale('log')
    plt.plot(n, 8 * n, 'b')
    plt.plot(n, 4 * n * np.log(n), 'g')
    plt.plot(n, 2 * np.power(n, 2), 'r')
    plt.plot(n, np.power(n, 3), 'c')
    plt.plot(n, np.power(2, n), 'm')
    plt.show()

'''
R-3.2 The number of operations executed by algorithms A and B is 8nlogn and 2n2, respectively.
Determine n0 such that A is better than B for n ≥ n0.

Answer: n0 = 0
'''

'''
R-3.3 The number of operations executed by algorithms A and B is 40n2 and 2n3, respectively.
Determine n0 such that A is better than B for n ≥ n0.

Answer: n0 = 20
'''

'''
R-3.4 Give an example of a function that is plotted the same on a log-log scale as it is on a standard scale.

Answer: f(x) = x
'''

'''
R-3.5 Explain why the plot of the function nc is a straight line with slope c on a log-log scale.

Answer: Taking the logarithm of the equation (with any base) yields: logy = clogn.
        Setting X = logn and Y = logy, which corresponds to using a log–log graph, yields the equation:
        Y = cX
        where c is the slope of the line.
'''

'''
R-3.6 What is the sum of all the even numbers from 0 to 2n, for any positive integer n?

Answer: n * (n + 1)
'''

'''
R-3.7 Show that the following two statements are equivalent:
      (a) The running time of algorithm A is always O(f(n)).
      (b) In the worst case, the running time of algorithm A is O(f(n)).

Answer: An algorithm may run faster on some inputs than it does on others of the same size.
Thus, we may wish to express the running time of an algorithm as the function of the input size
obtained by taking the average over all possible inputs of the same size. Unfortunately,
such an average-case analysis is typically quite challenging. An average-case analysis usually
requires that we calculate expected running times based on a given input distribution,
which usually involves sophisticated probability theory. Worst-case analysis is much easier than
average-case analysis, as it requires only the ability to identify the worst-case input, which is
often simple. Making the standard of success for an algorithm to perform well in the worst case
necessarily requires that it will do well on every input.
'''

'''
R-3.8 Order the following functions by asymptotic growth rate.
                4nlogn+2n   2^10    2^logn
                3n+100logn  4n      2^n
                n^2+10n     n^3     nlogn

Answer: 2^10, 3n+100logn, 4n, nlogn, 4nlogn+2n, n^2+10n, n^3, 2^logn, 2^n
'''

if __name__ == "__main__":
    main()
