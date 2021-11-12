num = int(input("Sayı giriniz: "))
if num<0:
    print("negatif sayı girdiniz.")
else:
    sum = 0
    while num > 0:
        sum = sum + num
        num = num - 1
    print("toplam:",sum)

# 5 -> 5+4+3+2+1+0 = 15