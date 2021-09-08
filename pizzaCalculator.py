# pizza calculator opdracht
# Steph Poleij 99033734

print ('------------------------------')
print ('small pizza         $6')
print ('medium pizza        $10')
print ('large pizza         $14')
print ('------------------------------')

# ^ laat de pizza prijzen aan de gebruiker zien

pizza = input ('welke size pizza wil je? ')
aantalPizzas = int (input ('hoeveel pizzas wil je? '))

# ^ vraag gebruiker om de size (small/medium/large) en de hoeveelheid pizzas
# ^ maak aantalPizzas een integer

prijsSmall =  6
prijsMedium = 10
prijsLarge = 14

# ^ pizza variables

if pizza == 'small':
    resultSmall = ('dat wordt dan $') + str(aantalPizzas * prijsSmall)
    print (resultSmall)
if pizza == 'medium':
    resultMedium = ('dat wordt dan $') + str(aantalPizzas * prijsMedium)
    print (resultMedium)
if pizza == 'large':
    resultLarge = ('dat wordt dan $') + str(aantalPizzas * prijsLarge)
    print (resultLarge)

# ^ multiply aantal x prijs, maak dit een string
