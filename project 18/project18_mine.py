import random

cards=[11,1,2,3,4,5,6,7,8,9,10,10,10]
print("Welcome to the blackjack game")
wanna_play_question=input("Do you wanna play blackjack game? y/n: ").lower()


my_cards=[]
computer_cards=[]
game_over=True


while game_over:
    computer_card_greater=True

    if wanna_play_question=="y":
        my_card1=random.choice(cards)
        my_cards.append(my_card1)
        my_card2=random.choice(cards)
        my_cards.append(my_card2)
        my_cards_total1=my_card1+my_card2

        computer_card1=random.choice(cards)
        computer_cards.append(computer_card1)
        computer_card2=random.choice(cards)
        computer_cards.append(computer_card2)
        computer_cards_total=computer_card1+computer_card2

        print(f"\nmy cards: {my_cards}","     ",f"total: {my_cards_total1} ")
        print(f"computer's first card is: {computer_card1}")
        print(computer_cards)

        new_card_question1=input("Do you wanna take a new card?  y/n: ").lower()

        while computer_card_greater:
            if computer_cards_total<17:
                computer_card10=random.choice(cards)
                computer_cards.append(computer_card10)
                computer_total1=computer_cards_total+computer_card10
                if computer_total1<17:
                    computer_card11=random.choice(cards)
                    computer_cards.append(computer_card11)
                    computer_total1=computer_cards_total+computer_card10+computer_card11
                    if computer_total1<17:
                        computer_card12=random.choice(cards)
                        computer_cards.append(computer_card12)
                        computer_total1=computer_cards_total+computer_card10+computer_card11+computer_card12
                    else:
                        computer_card_greater=False
                else:
                    computer_card_greater=False



        if new_card_question1=="y":
            my_card3=random.choice(cards)
            my_cards.append(my_card3)
            my_cards_total2=my_cards_total1+my_card3

            if computer_total1>21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total2}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I win\n")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    game_over=False
                    print("\n"*50)
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
            elif my_cards_total2>21 and computer_total1>21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total2}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("draw")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    game_over=False
                    print("\n"*50)
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
            elif computer_total1==21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total2}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I lost")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
            elif my_cards_total2>21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total2}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I lost")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
            elif my_cards_total2==21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total2}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I win")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)

            elif my_cards_total2<21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total2}")
                new_card_question2=input("do you wanna take a new card? y/n: ").lower()
                if new_card_question2=="y":
                    my_card4=random.choice(cards)
                    my_cards.append(my_card4)
                    my_cards_total3=my_cards_total2+my_card4
                    if my_cards_total3>21:
                        print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total3}")
                        print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                        print("I lost")
                        wanna_cont=input("Do you wanna play again? y/n: ").lower()
                        if wanna_cont=="n":
                            print("\n"*50)
                            game_over=False
                            print("          ********** Game over **********")
                            print("\n*10")
                        else:
                            my_cards.clear()
                            computer_cards.clear()
                            print("\n"*30)
                    elif my_cards_total3==21:
                        print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total3}")
                        print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                        print("I win")
                        wanna_cont=input("Do you wanna play again? y/n: ").lower()
                        if wanna_cont=="n":
                            print("\n"*50)
                            game_over=False
                            print("          ********** Game over **********")
                            print("\n"*10)
                        else:
                            my_cards.clear()
                            computer_cards.clear()
                            print("\n"*30)
                        input("Do you wanna take a new card? y/n: ")
                        new_card_question3=input("do you wanna take a new card? y/n: ").lower()
                        my_card5=random.choice(cards)
                        my_cards.append(my_card5)
                        my_cards_total4=my_cards_total3+my_card5
                        if my_cards_total3>21:
                            print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total3}")
                            print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                            print("I lost")
                            wanna_cont=input("Do you wanna play again? y/n: ").lower()
                            if wanna_cont=="n":
                                print("\n"*50)
                                game_over=False
                                print("          ********** Game over **********")
                                print("\n"*10)
                            else:
                                my_cards.clear()
                                computer_cards.clear()
                                print("\n"*30)
                        elif my_cards_total3==21:
                            print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total3}")
                            print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                            print("I win")
                            wanna_cont=input("Do you wanna play again? y/n: ").lower()
                            if wanna_cont=="n":
                                print("\n"*50)
                                game_over=False
                                print("          ********** Game over **********")
                                print("\n"*10)
                            else:
                                my_cards.clear()
                                computer_cards.clear()
                                print("\n"*30)
        else:

            if my_cards_total1==21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total1}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I win")
                wanna_cont=input("Do you wanna play again? y/n").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
                    
            if my_cards_total1==21 and computer_total1==21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total1}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("draw")

            if computer_total1>21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total1}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I win")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
            elif computer_total1==21:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total1}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I lost")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
            elif computer_total1<21:
                if my_cards_total1>computer_total1:
                    print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total1}")
                    print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                    print("I win")
                    wanna_cont=input("Do you wanna play again? y/n: ").lower()
                    if wanna_cont=="n":
                        print("\n"*50)
                        game_over=False
                        print("          ********** Game over **********")
                        print("\n"*10)
                    else:
                        my_cards.clear()
                        computer_cards.clear()
                        print("\n"*30)

            if my_cards_total1==computer_total1:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total1}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("draw")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
            if my_cards_total1<computer_total1:
                print(f"my cards are: {my_cards}","     ",f"total: {my_cards_total1}")
                print(f"computer's cards are: {computer_cards}","     ",f"total: {computer_total1}")
                print("I lost")
                wanna_cont=input("Do you wanna play again? y/n: ").lower()
                if wanna_cont=="n":
                    print("\n"*50)
                    game_over=False
                    print("          ********** Game over **********")
                    print("\n"*10)
                else:
                    my_cards.clear()
                    computer_cards.clear()
                    print("\n"*30)
        

    else:
        print("\n"*50)
        print("                 ************** Game over *****************")
        print("\n"*10)
        break
                    


    
            

        
    


            
    

