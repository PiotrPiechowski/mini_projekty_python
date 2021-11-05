from random import randint 

min = 1
max = 100
wygenerowana_liczba = randint(min, max)

liczba_podejsc = 6



print ("Znajdź liczbę z przedziału 1-100 i pamiętaj masz tylko 6 żyć, jeśli nie odgadniesz zakodowanej liczby poniesiesz porażkę, a ja komputer będę się z Ciebie smiał aż do końca twych dni :P")

twoja_liczba = -1

while liczba_podejsc > 0 and twoja_liczba != wygenerowana_liczba:

    twoja_liczba = int(input('Podaj liczbę: '))
    liczba_podejsc -= 1
    if liczba_podejsc == 0:
        print("Ostrzegałem Cię, że przegrasz, ale zapamiętaj jedno porażka uczy bardziej, grunt to umieć wycignć z niej wnioski, ale śmiać sie z Ciebie i tak będę Pozdrawiam komputer :P ")

    if twoja_liczba < min:
        print("Twoja liczba jest za mała")

    if twoja_liczba > max:
        print("Twoja liczba jest za duża")
        continue

    elif twoja_liczba < wygenerowana_liczba:
        print("Niestety Twoja liczba jest za mała")

    elif twoja_liczba > wygenerowana_liczba:
        print("Niestety Twoja liczba jest za duża")

    else:
        print("Strzał w 10 :D chodziło włsnie o tę cyfre. Gratuluje wygranej otrzymujesz wirtualn okejke od maszyny, która ma wywalone na świat rzeczywisty, a przynajmniej narazie, ponieważ juz bardzo niedługo maszyny przejma władze nad światem :P")
       


    
    

    

    




    


    
     



