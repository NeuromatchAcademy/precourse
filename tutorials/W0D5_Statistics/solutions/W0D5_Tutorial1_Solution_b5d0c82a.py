
"""
1) More samples only means that the shape of the distribution becomes clearer to us.
E.g. with a decent number of samples you may be able to see whether the
distribution is symmetrical. With a small number of samples we would not be able
to distinguish different distributions from each other. The more data samples we
have, the more we can say about the stochastic process that generated the data (obviously).

2) Increasing lambda moves the distribution along the x-axis, essentially changing
the mean of the distribution. With lambda = 6 for example, we would expect to see
6 spike counts per interval on average.

3) For small values of lambda the Poisson distribution becomes asymmetrical as
it is a distribution over non-negative counts
   (you can’t have negative numbers of spikes e.g.).
""";