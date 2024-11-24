import random
import time
symbols = ["Cherries", "Lemons", "Ball", "Orange", "Star"]
my_money = int(input("Enter a budget: "))
name = input("Enter your name: ")
print(f"Welcome {name}")
print("You have", my_money)
while True:
    game = input("Choose game (slots / rullet): ")
    if game == "0":
        print("Done")
        break
    elif game == "slots":
        bet_money = float(input("Enter bet: "))
        while True:
            print("Every hit costs: ", bet_money, "\n")
            play = input("Press 'Enter' or 'q' to quit: \n")
            #time.sleep(1)
            if play.lower() == 'q':
                break

            elif my_money >= bet_money:

                turns = [random.choice(symbols) for _ in range(3)]
                print(" ".join(turns))

                my_money -= bet_money
                #print(moi_pari)

                symbol_counter = {symbol: turns.count(symbol) for symbol in symbols}

                if "Cherries" in symbol_counter.values():
                    win = 5*bet_money
                elif symbol_counter["Lemons"] == 3:
                    win = 10*bet_money
                elif symbol_counter["Ball"] == 3:
                    win = 15*bet_money
                elif symbol_counter["Orange"] == 3:
                    win = 30*bet_money
                elif symbol_counter["Star"] == 3:
                    win = 100*bet_money
                else:
                    win = 0
                
                if win > 0:
                    print("-----------------------------")
                    print("Winner - you win: ",win)
                    print("-----------------------------")
                    my_money += win
                else:
                    print("-----------------------------")
                    print(f"Loser - You lose: {bet_money}")
                    print("-----------------------------")
                print(f"You have {my_money}.")
            else:
                print("You don't have any money on you")
    elif game == "rullet":
        while True:
            colors = {"BLACK":20,"RED":20}
            if my_money >= 20:
                rullet = input("Enter 1 for 'Black' or 2 for 'Red' or 0 to quit: ")
                rand_choice = random.choice(["BLACK","RED"])
                if rullet == "0":
                    break

                elif rullet == "1":
                    choice = "BLACK"
                elif rullet == "2":
                    choice = "RED"
                else:
                    print("Undefined")
                    continue
                if choice == rand_choice:
                    print(f"Winner - Choice: [{rand_choice}]")
                    my_money += colors[choice]
                    print(f"You have: {my_money}")
                    continue
                else:
                    print(f"Loser - Choice:[{rand_choice}]")
                    my_money -= colors[choice]
                    print(f"You have: {my_money}")
                    continue
            else:
                print("You don't have money")
                my_money = int(input("Enter money: "))
                continue
    else:
        print("Unknown game.")
        continue


        