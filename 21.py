    print("-//-//-//-//-//-//-//-//-//-//-//")
    print(" Bem vindo ao jogo de BlackJack! ")
    print("-//-//-//-//-//-//-//-//-//-//-//")


    baralho = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    card_possible = random.randrange(0, baralho)
    dealer_cards = []
    player_cards = []


    lost = False
    hit = False
    stand = False

    while(not lost):

        escolha = input("Hit or Stand:".lower())
        escolha = escolha.strip()

        if(hit == True):
            player_cards.append(card_possible)
            print("You have ", player_cards)
        elif(stand == True):
            while len(dealer_cards) != 2:
                dealer_cards.append(card_possible)
                if len(dealer_cards) == 2:
                    print("Dealer has: _ and", dealer_cards[1])
                    
                    
