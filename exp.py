import matplotlib.pyplot as plt

# Programme de calcul de croissance exponentielle pour la bourse.
# Rendement en pourcentage ajoutez au capital avec une limite à atteindre.

def exp():
  print("\nMontant du capital investi :\n")
  capital = int(input())
  print("\nRendement en pourcentage prévu :\n")
  pourcentage = int(input())
  print("\nObjectif à atteindre :\n")
  objectif = int(input())

  bénéfice = objectif - capital
  bénéfice_euro = bénéfice * 0.84

  boucle = 0
  capital_de_départ = capital

  x = []
  y = []

  print("\nSuivi du capital :\n")

  while capital < objectif:
    capital += (capital/100) * pourcentage
    print(str(boucle) +". " + str(capital))
    x.append(boucle)
    y.append(capital)
    boucle += 1

  print("\nAvec un capital de départ de {}$ et un rendement en pourcentage de {}%, il faudra {} rendement avant d'atteindre l'objectif de {}$.\nLe bénéfice sera de {}$ soit {}€ avec un taux de change de 0,84.\n".format(capital_de_départ, pourcentage, boucle -1, objectif, bénéfice, bénéfice_euro))

  plt.plot(x, y)
  plt.axis([0, x[-1], 0, objectif])
  plt.title(label="Calcul du capital/rendement")
  plt.xlabel("Nombre de rendement")
  plt.ylabel("Capital")
  plt.show()

exp()
