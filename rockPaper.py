import random
user_wins = 0
computer_wins = 0
options = ["taş","kağıt","makas"]
while True:
    user_input = input("Taş/Kağıt/Makas yazın çıkmak için Q yazın: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Bilgisayarın Seçimi: ",computer_pick)
    if user_input == "taş" and computer_pick == "makas":
        print("Kazandın!")
        user_wins += 1
    elif user_input == "kağıt" and computer_pick == "taş":
        print("Kazandın!")
        user_wins += 1
    elif user_input == "makas" and computer_pick == "kağıt":
        print("Kazandın!")
        user_wins += 1
    else:
        print("Kaybettin!")
        computer_wins += 1
print("Sen", user_wins, "defa kazandın.")
print("Bilgisayar", computer_wins, "defa kazandı.")
print("Güle güle!")