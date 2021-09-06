#int = aantalPersonen = 4
#float = prijsTicket = 7.45
#int = tijdGameSeat = 45
#int = verhoudingGameSeat = 5
#float = prijsGameSeat = 0.37

aantalPersonen = int(input('geef aantal personen: '))
prijsTicket = float(input('geef de prijs van een ticket: '))
tijdGameSeat = int(input('hoeveel minuten wil je een game seat?: '))
verhoudingGameSeat = int(input('per hoeveel minuten rekent de game seat?: '))
prijsGameSeat = float(input('Hoe duur is een gameseat?:  '))

totaalPrijs = ((aantalPersonen * prijsTicket) + (tijdGameSeat / verhoudingGameSeat * prijsGameSeat * aantalPersonen))

# zorg voor dit antwoord: ‘Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 43.12 euro’

print ('Dit geweldige dagje-uit met ' +str(aantalPersonen) +' mensen in de Speelhal met ' + str(tijdGameSeat) + ' minuten VR kost je maar ' + str(round(totaalPrijs, 2)) + ' euro')