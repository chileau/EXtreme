s=input()
ns=''
for i in s:
    if i.isupper():
        if ord(i)<77:
            ns+=chr(ord(i)+14)
        elif ord(i)>76 and ord(i)<91:
            ns+=chr(ord(i)-12)
    elif i.islower():
        if ord(i)<109:
            ns+=chr(ord(i)+14)
        elif ord(i)>108 and ord(i)<123:
            ns+=chr(ord(i)-12)
    else:
        ns+=i
print(ns)