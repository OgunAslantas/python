import random
top_of_range = input("Tahmin aralığı için bir sayı giriniz: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Lütfen 0'dan büyük bir sayı giriniz.")
        quit()
else:
    print("Lütfen bir sayı yazınız.")
    quit()
random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Tahmin et: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Lütfen bir sayı yazınız.")
        continue
    if user_guess == random_number:
        print("Doğru tahmin.")
        break
    elif user_guess > random_number:
        print("Daha küçük bir sayı")
    else:
        print("Daha büyük bir sayı")
print("Kazandın", guesses , "tahminler")