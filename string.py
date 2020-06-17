str = 'X-DSPAM-Confidence:0.8475'
x = str.find(':')
print(str[x + 1:] * 2)
print(float(str[x + 1:]) * 2)
