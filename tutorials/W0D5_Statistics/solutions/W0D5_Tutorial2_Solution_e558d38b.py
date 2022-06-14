
"""
The first step is to calculute:
P(v+|h0) = P(h0|v+)P(v+)/P(h0) = (1 − 0.1)∗0.3/(1 − 0.4) = 0.45

Then use the property of marginalisation (discrete version)

P(a) = Sum(i*P(a|b=i)P(b=i))

P(v+) = P(v+|h+)P(h+) + P(v+|h0)P(h0) = 0.075∗0.4 + 0.45∗(1 − 0.4) = 0.3

Phew, we recovered the correct value!
""";