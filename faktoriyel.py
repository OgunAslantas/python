def FirstFactorial(num):
  if num == 1:
    print(num)
  else:
    sum = 1
    while num > 0:
        sum *= num          
        num -= 1
  return sum                

a= int(input("Sayı giriniz: "))
print(FirstFactorial(a))