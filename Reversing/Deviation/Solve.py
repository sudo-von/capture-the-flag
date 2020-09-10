y = [104,97,99,107,100,101,102,123]
x = [47,86,107,101,83,41,80,82,]
eMessage = "Index wa"

user = ''
for i in range(0,8):
    user += chr((ord(eMessage[i])^y[i])+x[i])

print(user)