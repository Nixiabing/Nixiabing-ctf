import base64

ciphertext = [
 '96', '65', '93', '123', '91', '97', '22', '93', '70', '102', '94', '132', '46', '112', '64', '97', '88', '80', '82', '137', '90', '109', '99', '112']
c = ciphertext[::-1]
s = ""
for i in range(24):
    if i % 2 == 0:
        s += chr((int(c[i]) - 10)^i)
    else:
        s += chr((int(c[i]) + 10)^i)
print(s)