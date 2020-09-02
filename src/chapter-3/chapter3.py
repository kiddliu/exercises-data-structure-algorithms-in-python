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

'''
R-3.9 Show that if d(n) is O(f(n)), then ad(n) is O(f(n)), for any constant a > 0.

Answer: We say that d(n) is O(f(n)) if there is a real constant c > 0 and an integer constant n0 >= 1
such that d(n) <= cf(n), for n >= n0. Then for n >= n0, ad(n) <= acf(n) = c'f(n) still holds,
therefore it's still O(f(n)).
'''

'''
R-3.10 Show that if d(n) is O(f(n)) and e(n) is O(g(n)),then the product d(n)e(n) is O(f(n)g(n)).

Answer: We say that d(n) is O(f(n)) if there is a real constant c1 > 0 and an integer constant n0 >= 1
such that d(n) <= cf(n), for n >= n0; and e(n) is O(g(n)) if there is a real constant c' > 0 and
an integer constant n0' >= 1 such that e(n) <= c'g(n), for n >= n0'.
Therefore, there would always be a n0'' >= 1 that for n >= n0'', d(n)e(n) <= cf(n)c'g(n) = Cf(n)g(n),
then we say that d(n)e(n) is O(f(n)g(n)).
'''

'''
R-3.11 Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n) + e(n) is O(f(n) + g(n)).

Answer: We say that d(n) is O(f(n)) if there is a real constant c1 > 0 and an integer constant n0 >= 1
such that d(n) <= cf(n), for n >= n0; and e(n) is O(g(n)) if there is a real constant c' > 0 and
an integer constant n0' >= 1 such that e(n) <= c'g(n), for n >= n0'.
Therefore, there would always be a n0'' >= 1 that for n >= n0'',
d(n) + e(n) <= cf(n) + c'g(n) <= max(c, c')(f(n) + g(n)), then we say that d(n) + e(n) is O(f(n) + g(n)).
'''

'''
R-3.12 Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n) − e(n) is not necessarily O(f(n) − g(n)).

Answer: It's not possible for us to conclude the relationship between d(n) - e(n) = cf(n) - c'g(n) and
 f(n) - g(n). Therefore we cannot say d(n) − e(n) is O(f(n) − g(n))
'''

'''
R-3.13 Show that if d(n) is O(f(n)) and f(n) is O(g(n)), then d(n) is O(g(n)).

Answer: We say that d(n) is O(f(n)) if there is a real constant c1 > 0 and an integer constant n0 >= 1
such that d(n) <= cf(n), for n >= n0; and f(n) is O(g(n)) if there is a real constant c' > 0 and
an integer constant n0' >= 1 such that f(n) <= c'g(n), for n >= n0'.
Then, there would always be a n0'' >= 1 that for n >= n0'', d(n) <= cf(n) <= cc'g(n) = Cg(n), then d(n) is O(g(n)).
'''

'''
R-3.14 Show that O(max{f(n), g(n)}) = O(f(n) + g(n)).

Answer: As there is a real constant c = 1 and an integer constant n0 such that
max{f(n), g(n)} <= 1 * (f(n) + g(n)), then we say O(max{f(n), g(n)}) = O(f(n) + g(n)).
'''

'''
R-3.15 Show that f(n) is O(g(n)) if and only if g(n) is Ω(f(n)).

Answer: Big O notation means the asymptotic upper bound, and big omega notation means the asymptotic
lower bound. Therefore, f(n) is O(g(n)) if and only if g(n) is Ω(f(n)), otherwise it contradicts with 
either statement.
'''

'''
R-3.16 Show that if p(n) is a polynomial in n, then log p(n) is O(log(n)).

Answer: Let say p(n) has degree D, then there's a constant C such that p(n) <= Cn^D, and
log(p(n)) <= log(Cn^D) = logC + Dlog(n), therefore log(p(n)) is O(log(n)).
'''

'''
R-3.17 Show that (n + 1)^5 is O(n^5).

Answer: (n + 1) ^ 5 = n^5 + 5n^4 + 10n^3 + 10n^2 + 5n + 1 <= Cn^5 for some integer constant n = n0.
Then we say (n + 1)^5 is O(n^5).
'''

'''
R-3.18 Show that 2^n+1 is O(2^n).

Answer: 2^n+1 = 2 * 2^N for some integer constant n = n0. Then we say 2^n+1 is O(2^n).
'''

'''
R-3.19 Show that n is O(nlogn).

Answer: As n = n * 1 <= n * log(n) for n0 >= 10, we say n is O(nlogn).
'''

'''
R-3.20 Show that n^2 is Ω(nlogn).

Answer: As n^2 = n * n > n * log(n) for n0 >= 0, we say n^2 is Ω(nlogn).
'''

'''
R-3.21 Show that nlogn is Ω(n).

Answer: As nlogn > n for n0 > 10, we say nlogn is Ω(n).
'''

'''
R-3.22 Show that ⌈f(n)⌉ is O(f(n)), if f(n) is a positive nondecreasing function that is always greater than 1.

Answer: As ⌈f(n)⌉ < 2 * f(n) for any n0 as the function is always greater than 1, we say ⌈f(n)⌉ is O(f(n)).
'''

''' Code Fragment 3.10
def example1(S):
    ”””Return the sum of the elements in sequence S.”””
    n = len(S)
    total = 0
    for j in range(n):                  # loop from 0 to n-1
        total += S[j]
    return total

def example2(S):
    ”””Return the sum of the elements with even index in sequence S.”””
    n = len(S)
    total = 0
    for j in range(0, n, 2):            # note the increment of 2
        total += S[j]
    return total

def example3(S):
    ”””Return the sum of the prefix sums of sequence S.”””
    n = len(S)
    total = 0
    for j in range(n):                  # loop from 0 to n-1
        for k in range(1+j):            # loop from 0 to j
            total += S[k]
    return total

def example4(S):
    ”””Return the sum of the prefix sums of sequence S.”””
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total

def example5(A, B):                     # assume that A and B have equal length
    ”””Return the number of elements in B equal to the sum of prefix sums in A.”””
    n = len(A)
    count = 0
    for i in range(n):                  # loop from 0 to n-1
        total = 0
        for j in range(n):              # loop from 0 to n-1
            for k in range(1+j):        # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count
'''

'''
R-3.23 Give a big-Oh characterization, in terms of n, of the running time of the example1 function
shown in Code Fragment 3.10.

Answer: O(n)

R-3.24 Give a big-Oh characterization, in terms of n, of the running time of the example2 function
shown in Code Fragment 3.10.

Answer: O(n)

R-3.25 Give a big-Oh characterization, in terms of n, of the running time of the example3 function
shown in Code Fragment 3.10.

Answer: O(nlog(n))

R-3.26 Give a big-Oh characterization, in terms of n, of the running time of the example4 function
shown in Code Fragment 3.10.

Answer: O(n)

R-3.27 Give a big-Oh characterization, in terms of n, of the running time of the example5 function
shown in Code Fragment 3.10.

Answer: O(n^2log(n))

R-3.28 For each function f(n) and time t in the following table, determine the largest size n of
a problem P that can be solved in time t if the algorithm for solving P takes f(n) microseconds
(one entry is already completed).

                1 Second        1 Hour              1 Month                 1 Century
log(n)          ≈10^300000      ≈10^(10^9)          ≈10^(10^12)             ≈10^(10^15)
n               ≈300000         ≈1.08 * 10^9        ≈7.776 * 10^11          ≈9.3312 * 10^14
nlogn           ≈62549          ≈1.32 * 10^8        ≈7.16 * 10^10           ≈6.75 * 10^13
n2              ≈550            ≈32863              ≈881816                 ≈3.05 * 10^7
2^n             ≈18             ≈30                 ≈40                     ≈50
'''

'''
R-3.29 Algorithm A executes an O(logn)-time computation for each entry of an n-element sequence. 
What is its worst-case running time?

Answer: O(nlog(n))
'''

'''
R-3.30 Given an n-element sequence S, Algorithm B chooses logn elements in S at random and
executes an O(n)-time calculation for each. What is the worst-case running time of Algorithm B?

Answer: O(nlog(n))
'''

'''
R-3.31 Given an n-element sequence S of integers, Algorithm C executes an O(n)-time computation
for each even number in S, and an O(logn)-time computation for each odd number in S.
What are the best-case and worst-case running times of Algorithm C?

Answer: The best case is that in S there are all odd numbers: it's O(nlog(n))
        The worst case is that in S there are all even numbers: it's O(n^2)
'''

'''
R-3.32 Given an n-element sequence S, Algorithm D calls Algorithm E on each element S[i].
Algorithm E runs in O(i) time when it is called on element S[i].
What is the worst-case running time of Algorithm D?

Answer: O(n^2)
'''

'''
R-3.33 Al and Bob are arguing about their algorithms. Al claims his O(nlogn)-time method is
always faster than Bob’s O(n2)-time method. To settle the issue, they perform a set of experiments.
To Al’s dismay, they find that if n < 100, the O(n^2)-time algorithm runs faster,
and only when n ≥ 100 is the O(nlog(n))-time one better. Explain how this is possible.

Answer: The constant factors of both algorithms matter in this case. To be specific, given C1
the constant factor of Al's algorithm, and C2 the constant factor of Bob's algorithm, when n = 100,
C1 * n^2 == C2 * nlog(n), then as long as C1 = 500 * C2, the claim holds.
'''

'''
R-3.34 There is a well-known city (which will go nameless here) whose inhabitants have the reputation of
enjoying a meal only if that meal is the best they have ever experienced in their life.
Otherwise, they hate it. Assuming meal quality is distributed uniformly across a person’s life,
describe the expected number of times inhabitants of this city are happy with their meals?

Answer: E(0, N) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
'''

'''
C-3.35 Assuming it is possible to sort n numbers in O(nlogn) time, show that it is possible to solve the
three-way set disjointness problem in O(nlogn) time.

Answer: Just merge these sets and sort the merged array in O(nlogn) time, then traverse the array and check if
there are 3 identical numbers in it. It's O(nlogn + cn), which is O(nlogn).
'''

'''
C-3.36 Describe an efficient algorithm for finding the ten largest elements in a sequence of size n. 
What is the running time of your algorithm?

Answer: https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
'''

'''
C-3.37 Give an example of a positive function f(n) such that f(n) is neither O(n) nor Ω(n).

Answer: f(n) = n^2 * sin^2(n)
'''

'''
C-3.38 Show that ∑ni=1 i^2 is O(n3).

Answer: 1^2 + 2^2 + ... + n^2 <= n^2 + n^2 + ... + n^2 = n^3, for n > 0, then we say it's O(n^3)
'''

'''
C-3.39 Show that ∑ni=1 i/2^i < 2. (Hint: Try to bound this sum term by term with a geometric progression.)

Answer: https://math.stackexchange.com/a/2172734
'''

'''
C-3.40 Show that logbf(n) is Θ(logf(n)) if b > 1 is a constant.

Answer logbf(n) = log(f(n)) / log(b), where log(b) is a constant decreasing number, then we say it's Θ(logf(n))
'''

if __name__ == "__main__":
    main()
