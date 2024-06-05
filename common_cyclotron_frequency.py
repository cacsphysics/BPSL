import cyclotron_frequency as cf


B = 100
wci = cf.ion_cyclotron(B)
wce = cf.e_cyclotron(B)

print(f"Wcp = {wci:0.2f} and Wce = {wce:0.2f}")
print(f"The ratio is {wce/wci:0.2f}")
