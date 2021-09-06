#voorbeeld van opdracht:
# stuks = int(input('geef aantal stuks'))

aantalCroissantjes = int(input('geef aantal croissantjes: '))
prijsCroissantjes = float(input('geef de prijs van de croissantjes: '))
aantalStokbroden = int(input('geef aantal stokbroden: '))
prijsStokbroden = float(input('geef de prijs van de stokbroden: '))
aantalKortingsbonnen = int(input('geef aantal kortingsbonnen: '))
prijsKortingsbonnen = float(input('geef de prijs van de kortingsbonnen: '))

#int = aantalCroissantjes = 17
#float = prijsCroissantjes = 0.39
#int = aantalStokbroden = 2
#float = prijsStokbroden = 2.78
#int = aantalKortingsbonnen = 3
#float = prijsKortingsbonnen = 0.50

totaalPrijs = ((aantalCroissantjes * prijsCroissantjes) + (aantalStokbroden * prijsStokbroden) - (aantalKortingsbonnen * prijsKortingsbonnen))

#zorg voor dit antwoord: ‘De feestlunch kost je bij de bakker 10.69 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!’

print ('De feestlunch kost je bij de bakker ' + str(totaalPrijs) + ' euro' + ' voor de ' + str(aantalCroissantjes) +' croissantjes en de ' + str(aantalStokbroden)
+ ' stokbroden als de ' + str(aantalKortingsbonnen) + ' kortingsbonnen nog geldig zijn')