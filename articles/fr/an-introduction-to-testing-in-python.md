---
title: Une introduction aux tests unitaires en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-06T09:18:01.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-testing-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/image-45-1.png
tags:
- name: Python
  slug: python
- name: Testing
  slug: testing
seo_title: Une introduction aux tests unitaires en Python
seo_desc: "By Goran Aviani\nYou just finished writing a piece of code and you are\
  \ wondering what to do. Will you submit a pull request and have your teammates review\
  \ the code? Or will you manually test the code? \nYou should do both of these things,\
  \ but with an a..."
---

Par Goran Aviani

_Vous venez de terminer d'écrire un morceau de code et vous vous demandez quoi faire. Allez-vous soumettre une pull request et faire réviser le code par vos coéquipiers ? Ou allez-vous tester le code manuellement ?_

_Vous devriez faire ces deux choses, mais avec une étape supplémentaire : vous devez tester unitairement votre code pour vous assurer que le code fonctionne comme prévu._

Les tests unitaires peuvent réussir ou échouer, ce qui en fait une excellente technique pour vérifier votre code. Dans ce tutoriel, je vais démontrer comment écrire des tests unitaires en Python et vous verrez à quel point il est facile de les mettre en place dans votre propre projet.

# Installation

La meilleure façon de comprendre les tests est de les faire de manière pratique. À cette fin, dans un fichier nommé name_function.py, je vais écrire une fonction simple qui prend un prénom et un nom de famille, et retourne un nom complet :

```py
# Générer un nom complet formaté
def formatted_name(first_name, last_name):
   full_name = first_name + ' ' + last_name
   return full_name.title()
```

La fonction formatted_name() prend le prénom et le nom de famille et les combine avec un espace entre les deux pour former un nom complet. Elle met ensuite en majuscule la première lettre de chaque mot. Pour vérifier que ce code fonctionne, vous devez écrire du code qui utilise cette fonction. Dans names.py, je vais écrire un code simple qui permet aux utilisateurs de saisir leur prénom et leur nom de famille :

```py
from name_function import formatted_name

print("Veuillez entrer le prénom et le nom de famille ou entrer x pour [Q]uitter.")

while True:
   first_name = input("Veuillez entrer le prénom : ")
   if first_name == "x":
       print("Au revoir.")
       break

   last_name = input("Veuillez entrer le nom de famille : ")
   if last_name == "x":
       print("Au revoir.")
       break

   result = formatted_name(first_name, last_name)
   print("Le nom formaté est : " + result + ".")
```

Ce code importe formatted_name() depuis name_function.py et, lors de l'exécution, permet à l'utilisateur de saisir une série de prénoms et de noms de famille et affiche les noms complets formatés.

# Test unitaire et cas de test

Il existe un module dans la bibliothèque standard de Python appelé unittest qui contient des outils pour tester votre code. Le test unitaire vérifie si toutes les parties spécifiques du comportement de votre fonction sont correctes, ce qui facilitera leur intégration avec d'autres parties.

Un cas de test est une collection de tests unitaires qui, ensemble, prouve qu'une fonction fonctionne comme prévu, dans une gamme complète de situations dans lesquelles cette fonction peut se trouver et qu'elle est censée gérer. Un cas de test doit prendre en compte tous les types possibles d'entrées qu'une fonction pourrait recevoir des utilisateurs, et doit donc inclure des tests pour représenter chacune de ces situations.

# Réussir un test

Voici un scénario typique pour écrire des tests :

Tout d'abord, vous devez créer un fichier de test. Ensuite, importer le module unittest, définir la classe de test qui hérite de unittest.TestCase, et enfin, écrire une série de méthodes pour tester tous les cas du comportement de votre fonction.

Il y a une explication ligne par ligne sous le code suivant :

```py
import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):

   def test_first_last_name(self):
       result = formatted_name("pete", "seeger")
       self.assertEqual(result, "Pete Seeger")
```

Tout d'abord, vous devez importer unittest et la fonction que vous souhaitez tester, formatted_name(). Ensuite, vous créez une classe, par exemple NamesTestCase, qui contiendra les tests pour votre fonction formatted_name(). Cette classe hérite de la classe unittest.TestCase.

NamesTestCase contient une seule méthode qui teste une partie de formatted_name(). Vous pouvez appeler cette méthode test_first_last_name().

> N'oubliez pas que chaque méthode qui commence par « test_ » sera exécutée automatiquement lorsque vous exécutez test_name_function.py.

Dans la méthode de test test_first_last_name(), vous appelez la fonction que vous souhaitez tester et stockez une valeur de retour. Dans cet exemple, nous allons appeler formatted_name() avec les arguments « pete » et « seeger », et stocker le résultat dans la variable result.

Dans la dernière ligne, nous allons utiliser la méthode assert. La méthode assert vérifie qu'un résultat que vous avez reçu correspond au résultat que vous attendiez. Et dans ce cas, nous savons que la fonction formatted_name() retournera le nom complet avec des majuscules aux premières lettres, donc nous attendons le résultat « Pete Seeger ». Pour vérifier cela, la méthode assertEqual() de unittest est utilisée.

```py
self.assertEqual(result, "Pete Seeger")
```

Cette ligne signifie essentiellement : Comparez la valeur dans la variable result avec « Pete Seeger » et si elles sont égales, c'est OK, mais si elles ne le sont pas, faites-le moi savoir.

En exécutant test_name_function.py, vous devriez obtenir un OK, ce qui signifie que le test a réussi.

```
Ran 1 test in 0.001s

OK
```

# Échec d'un test

Pour vous montrer à quoi ressemble un test qui échoue, je vais modifier la fonction formatted_name() en incluant un nouvel argument pour le deuxième prénom.

Je vais donc réécrire la fonction pour qu'elle ressemble à ceci :

```py
# Générer un nom complet formaté incluant un deuxième prénom
def formatted_name(first_name, last_name, middle_name):
   full_name = first_name + ' ' + middle_name + ' ' + last_name
   return full_name.title()
```

Cette version de formatted_name() fonctionnera pour les personnes ayant un deuxième prénom, mais lorsque vous la testerez, vous verrez que la fonction est cassée pour les personnes qui n'ont pas de deuxième prénom.

Ainsi, lorsque vous exécutez test_name_function.py, vous obtiendrez une sortie qui ressemble à ceci :

```
Error
Traceback (most recent call last):

File "test_name_function.py", line 7, in test_first_last_name
    result = formatted_name("pete", "seeger")

TypeError: formatted_name() missing 1 required positional argument: 'middle_name'

Ran 1 test in 0.002s

FAILED (errors=1)
```

Dans la sortie, vous verrez des informations qui vous diront tout ce que vous devez savoir sur l'endroit où le test échoue :

* Le premier élément de la sortie est l'Error qui vous indique qu'au moins un test dans le cas de test a abouti à une erreur.
* Ensuite, vous verrez le fichier et la méthode dans lesquels l'erreur s'est produite.
* Après cela, vous verrez la ligne dans laquelle l'erreur s'est produite.
* Et le type d'erreur, dans ce cas, il nous manque 1 argument « middle_name ».
* Vous verrez également le nombre de tests exécutés, le temps nécessaire pour que les tests se terminent, et un message textuel qui représente le statut des tests avec le nombre d'erreurs survenues.

# Que faire lorsque le test a échoué

> Un test réussi signifie que la fonction se comporte conformément à ce qui est attendu d'elle. Cependant, un test échoué signifie qu'il y a plus de travail à faire.

J'ai vu quelques programmeurs qui préfèrent changer le test plutôt que d'améliorer le code — mais ne faites pas cela. Passez un peu plus de temps à corriger le problème, car cela vous aidera à mieux comprendre le code et à gagner du temps à long terme.

Dans cet exemple, notre fonction formatted_name() nécessitait d'abord deux paramètres, et maintenant, telle qu'elle est réécrite, elle en nécessite un de plus : un deuxième prénom. L'ajout d'un deuxième prénom à notre fonction a cassé le comportement souhaité. Puisque l'idée n'est pas de faire des changements aux tests, la meilleure solution est de rendre le deuxième prénom facultatif.

Après avoir fait cela, l'idée est de faire passer les tests lorsque le prénom et le nom de famille sont utilisés, par exemple « Pete Seeger », ainsi que lorsque le prénom, le nom de famille et le deuxième prénom sont utilisés, par exemple « Raymond Red Reddington ». Modifions donc une fois de plus le code de formatted_name() :

```py
# Générer un nom complet formaté incluant un deuxième prénom
def formatted_name(first_name, last_name, middle_name=''):
   if len(middle_name) > 0:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
   else:
       full_name = first_name + ' ' + last_name
   return full_name.title()
```

Maintenant, la fonction devrait fonctionner pour les noms avec et sans deuxième prénom.

Et pour vous assurer qu'elle fonctionne toujours avec « Pete Seeger », exécutez le test à nouveau :

```
Ran 1 test in 0.001s

OK
```

> Et c'est ce que je voulais vous montrer : il est toujours préférable d'apporter des modifications à votre code pour qu'il corresponde à vos tests plutôt que l'inverse. Maintenant, il est temps d'ajouter un nouveau test pour les noms qui ont un deuxième prénom.

# Ajout de nouveaux tests

Écrivez une nouvelle méthode dans la classe NamesTestCase qui testera les deuxièmes prénoms :

```py
import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        result = formatted_name("pete", "seeger")
        self.assertEqual(result, "Pete Seeger")

    def test_first_last_middle_name(self):
        result = formatted_name("raymond", "reddington", "red")
        self.assertEqual(result, "Raymond Red Reddington")
```

Après avoir exécuté le test, les deux tests devraient réussir :

```
Ran 2 tests in 0.001s

OK
```

> Bra gjort!  
> Bien joué !

Vous avez écrit vos tests pour vérifier si la fonction fonctionne en utilisant des noms avec ou sans deuxième prénom. Restez à l'écoute pour la partie 2 où je parlerai davantage des tests en Python.

---

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci sur mon profil freeCodeCamp : [https://www.freecodecamp.org/news/author/goran/](https://www.freecodecamp.org/news/author/goran/) et d'autres choses amusantes que je construis sur ma page GitHub : [https://github.com/GoranAviani](https://github.com/GoranAviani)