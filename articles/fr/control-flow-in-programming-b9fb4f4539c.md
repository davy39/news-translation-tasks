---
title: 'Comment Python prend des décisions : une introduction au contrôle de flux
  en programmation'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T05:01:32.000Z'
originalURL: https://freecodecamp.org/news/control-flow-in-programming-b9fb4f4539c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4AwPR5QPsXwvCaIR3oczxg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Comment Python prend des décisions : une introduction au contrôle de flux
  en programmation'
seo_desc: 'By Ivan Leo

  What is control flow?

  I find it easy to think of control flow in 3 different categories


  Loops ( While, Do while, for )

  Decision-Making ( if-else)

  Exception Handling (Continue, Try-Except, Pass, Break)


  These 3 categories roughly sum up t...'
---

Par Ivan Leo

Qu'est-ce que le contrôle de flux ?

Je trouve qu'il est facile de penser au contrôle de flux en 3 catégories différentes

1. Boucles ( While, Do while, for )
2. Prise de décision ( if-else)
3. Gestion des exceptions (Continue, Try-Except, Pass, Break)

Ces 3 catégories résument grossièrement les différentes options disponibles pour nous lorsque nous parlons de contrôle de flux dans la plupart des langages de programmation.

Alors, plongeons directement dans le sujet.

### Boucles

> _Les boucles sont essentiellement un ensemble simple d'instructions qui se répète jusqu'à ce qu'une condition soit remplie._

Une bonne analogie à utiliser pour une boucle est de battre la pâte à gâteau :

Basé sur cette [recette](https://thecakeblog.com/2014/08/mixing-up-the-perfect-cake.html), si nous utilisons un batteur moderne, 3 minutes est le temps parfait pour mélanger la pâte. Si vous deviez donner des instructions à quelqu'un utilisant cette recette, cela ressemblerait probablement à ceci.

1. Mélanger les œufs, la farine et la recette secrète
2. Démarrer un chronomètre et commencer à mélanger la pâte
3. Mélanger la pâte jusqu'à ce que le chronomètre affiche 3 minutes

Si nous devions traduire cela en pseudo-code, cela ressemblerait probablement à ceci

```
#Démarrer le chronomètre<....code....>time = 0
```

```
While(time != 3 minutes):    time = newvalue    mix batter
```

Dans ce cas, nous utilisons **time** pour déterminer si nous continuons à mélanger notre pâte. Mais cela ne nous aide pas vraiment à prendre en compte des situations spécifiques lorsque nous utilisons différents ingrédients.

Dans ce cas, nous avons quelques options

1. Nous pourrions surveiller la consistance de la pâte
2. OU nous pourrions expérimenter avec un tas d'ingrédients, enregistrer les meilleurs temps pour chacun et ensuite nous référer à cet enregistrement chaque fois que nous mélangeons les gâteaux.

Arrêtez-vous un moment et réfléchissez, quand utiliserions-nous la première option et quand utiliserions-nous la deuxième option ?

< Espace intentionnellement laissé vide. Arrêtez-vous et réfléchissez un moment :) >

La première option est plus adaptée aux situations où nous pourrions rencontrer beaucoup de combinaisons imprévisibles. Il est donc logique de ne pas seulement vérifier le temps, mais aussi d'ajouter la protection d'un paramètre supplémentaire.

La deuxième option est adaptée aux situations où nous rencontrons des instances répétées de multiples combinaisons. C'est communément appelé la programmation dynamique.

En programmation dynamique, chaque valeur est calculée une fois puis stockée dans une table de consultation pour un accès futur. Cela aide à réduire le temps d'exécution des opérations futures en réduisant le temps de consultation, puisque la valeur n'a pas à être recalculée, il suffit de la consulter et de la retourner.

Maintenant, convertissons ce que nous avons appris en code et examinons ce que nous pouvons implémenter en python :)

### Code

En python, nous avons deux outils principaux à utiliser pour les boucles

1. Boucles While
2. Boucles For

#### **Boucles While**

Les boucles While nous permettent d'exécuter une commande indéfiniment.

```
x = 1y = 2
```

```
while(x=2):    print("x est en boucle")
```

```
while(y=2):    print("Y est en boucle")
```

Dans le code ci-dessus, seule la deuxième boucle while sera évaluée tandis que la première ne le sera pas. Lorsque nous exécutons le code, nous obtiendrons la sortie suivante

```
>>>python runapp.pyY est en boucleY est en boucleY est en boucleY est en boucle....
```

Voici ce qui se passe pour la première variable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*icabgqLnTLvv5Jlr7Ogmhw.png)

Comme on peut le voir ci-dessus, la boucle while n'imprime pas x car elle ne remplit pas la condition stipulée dans la première boucle while.

Et la deuxième condition ? Eh bien, cela suit quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WORh1EJzN6GGPeziMn4pEw.png)

Comme nous pouvons le voir, la boucle while vérifie constamment si une condition est vraie et ne s'exécute que si la condition spécifiée est vraie.

Voici quelques implémentations courantes en python :

```
#Demander une entrée utilisateurwhile True:    userinput = input("Veuillez entrer votre nom : ")    if userinput.isalpha():       break;
```

```
print("Bonjour %s"%(userinput))
```

```
#Traiter des variables dynamiques (c'est-à-dire des paramètres qui peuvent changer )no = int(input("Veuillez entrer le nombre de boucles : "))i = 0
```

```
while(i<n):    print(i)
```

Examinons les deux exemples.

#### Exemple 1

Ce code d'exemple (voir ci-dessus) est un échantillon de code que nous pourrions utiliser pour obtenir une entrée utilisateur. À mesure que vous codez des programmes plus avancés, vous serez en mesure de coder des programmes plus avancés qui peuvent vérifier l'entrée utilisateur ou faire plus de choses avec l'entrée utilisateur, mais pour l'instant, nous allons imprimer « Bonjour <userinput> » :

```
While True:
```

Puisque True est toujours vrai (je sais que c'est un peu contre-intuitif, mais suivez-moi), cette boucle s'exécutera pour toujours. **True ne peut jamais ne pas être True**.

```
userinput = input("Veuillez entrer votre nom : ")
```

Cela nous permet d'obtenir une entrée de l'utilisateur et de la stocker sous forme de chaîne. Nous créons une variable appelée userinput et stockons une référence à cette chaîne stockée en mémoire. (Si vous n'êtes pas sûr de ce qui se passe ici, j'ai écrit un [article](https://medium.com/@ivanleomk/a-crash-course-in-python-variables-cbad43b4efef) sur les variables en python, allez le consulter !)

```
if userinput.isalpha():       break;
```

Voici la magie. La méthode .isalpha() nous permet de vérifier si une chaîne est uniquement composée de caractères.

```
#Sortie d'exemple"12a".isalpha() #Cela retourne False"12".isalpha() #Cela retourne False"abc".isalpha() #Cela retourne True
```

L'utilisation de cette fonction nous permet de vérifier si l'utilisateur a entré un nom correct composé uniquement de caractères de l'alphabet.

Si l'utilisateur a entré un nom correct, la fonction break nous permet alors de sortir de la boucle.

```
print("Bonjour %s"%(userinput))
```

Cela nous permet ensuite d'exécuter la dernière ligne de code, imprimant la chaîne « bonjour <userName> ».

#### **Exemple 2 : Boucler pour un nombre de boucles**

```
no = int(input("Veuillez entrer le nombre de boucles : "))
```

Cette première ligne de code permet à l'utilisateur d'entrer une certaine valeur depuis la ligne de commande avant de la convertir en entier. Cela est fait en utilisant la valeur int().

```
i = 0
```

```
while(i<n):    print(i)
```

Ensuite, nous initialisons une variable i à 0 pour suivre le nombre de boucles que nous voulons exécuter, imprimant la valeur de i à chaque fois :

```
#Sortie d'exempleVeuillez entrer le nombre de boucles : 501234
```

Il est utile de penser à une boucle while comme suit

```
while(test_expression):    <code>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kHHhyQObLXAP3SmoVMqA0A.png)

**Boucles For**

Les boucles For fonctionnent un peu différemment des boucles While. Examinons la syntaxe

```
#Boucle For normaleFor i in range(1,6,1):    <code>
```

```
#Boucle d'itérationfor i in [1,2,3,4,5]:    <code>
```

Qu'est-ce qui se passe ici ?

Lorsque vous déclarez une boucle For comme vu dans le premier cas, vous invoquez ce que l'on appelle un générateur. Cela génère une liste de nombres en utilisant les paramètres que vous avez spécifiés.

Il est utile de penser au générateur comme à une fonction qui appelle une liste pour l'instant. Bien que ce ne soit pas exactement ainsi que cela fonctionne, c'est une approximation proche. Plus à venir sur ce sujet !

```
#Cela génère une liste avec les valeurs [1,2,3,4,5]For i in range(1,6,1):    <code>
```

Cette liste générée peut ensuite être itérée en utilisant la fonction d'itération intégrée en python. Cela signifie simplement que nous pouvons appeler chaque élément de cette liste dans l'ordre où ils sont stockés.

Le deuxième exemple fonctionne de manière similaire. Dans ce cas cependant, nous spécifions explicitement la liste à itérer au lieu de la générer avec la fonction range.

```
for i in [1,2,3,4,5]:    <code>
```

**Quelques cas utiles**

```
#Imprimer les éléments d'une liste
```

```
x = [...values...]for i in x:   print(i)
```

```
#Itérer sur les éléments d'une listey = [x**2 for i in x] #Cela est également connu sous le nom de compréhension de liste
```

Examinons ces cas plus en détail !

**Exemple 1**

```
x = [....values...]for i in x:
```

Dans ce cas, nous initialisons une liste appelée x avec un certain nombre de variables. Nous procédons ensuite à l'itération sur chaque valeur dans x.

```
print(i) #Cela imprime chaque valeur de x dans son ordre spécifié
```

Nous appelons chaque valeur dans x, dans ce cas appelée i, et l'imprimons.

```
#Sortie d'exemplex  = [1,2,3,4]for i in x:     print(i)
```

```
>>>python app.py1234
```

**Exemple 2**

```
y = [x**2 for i in x]
```

Essayons de réécrire cela sous une autre forme

```
for i in x:    y.append(x**2)
```

```
y = [x**2 for i in x]
```

Ces 2 sont la même chose ! Cependant, les compréhensions de liste tendent à être plus rapides.

### Prise de décision

À quoi pensez-vous lorsque vous pensez à la prise de décision lors de l'écriture d'un programme ? Pour moi, ce sont définitivement les arbres de décision et les organigrammes.

Bien que certains de ceux-ci (comme celui ci-dessous) soient définitivement ridicules, je pense qu'ils offrent toujours un cadre mental utile pour visualiser le flux de votre programme :

![Image](https://cdn-media-1.freecodecamp.org/images/0*V7qQs8M52EamG3zx)

Je vais utiliser une analogie pour parler de cela avant de montrer comment implémenter cela en utilisant la syntaxe if-else et break-continue.

#### Temps d'analogie

Imaginez que vous essayez de trouver le restaurant parfait pour une soirée en amoureux. Vous voulez trouver quelque chose qui est abordable et chic

Pendant que vous parcourez trip advisor, votre processus de pensée serait quelque chose comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S2cZhcS1mOIqMJMTu3SMdA.png)

Vous ne considéreriez que les choses qui sont bon marché et chics. Donc chaque fois que vous regardez un restaurant, vous vérifiez s'il correspond à vos critères et éliminez ceux qui ne correspondent pas.

De même, la prise de décision dans un programme fonctionne de la même manière. Vous définissez un ensemble de scénarios possibles et votre programme réagit en conséquence.

#### code

Examinons un programme simple pour trouver des nombres qui sont des multiples de deux.

```
import random
```

```
x = random.randint(0,1000)
```

```
if x%2==0:
```

```
    print(str(x)+" est un multiple de 2")
```

```
else:
```

```
    print(str(x)+" n'est pas un multiple de 2")
```

Comment fonctionne ce programme ?

1. Nous générons d'abord un nombre aléatoire de 0 à 1000
2. Nous divisons ensuite ce nombre aléatoire, x, par 2 et vérifions s'il y a un reste. ( % retourne le reste d'une division )
3. S'il n'y a pas de reste, nous imprimons l'énoncé « X est un multiple de 2 »
4. s'il y a un reste, nous imprimons l'énoncé « x n'est pas un multiple de 2 »

Nous savons que tous les multiples de 2 suivent la formule 2i où i est un entier. Par conséquent, tous les multiples de 2 doivent être divisibles par 2. Par conséquent, nous utilisons cela comme moyen d'évaluer si un nombre est un multiple de 2.

Cela peut être visualisé comme un arbre de décision, comme on peut le voir ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1PJI_rd7EMG5HVr6MFayig.png)

Comme nous pouvons le voir, une boucle de décision if-else nous permet de prendre en compte les valeurs de nos variables, permettant à notre programme de retourner une sortie différente en fonction de leurs valeurs.

Nous pouvons également utiliser une boucle if-else pour prendre en compte le type de variables en modifiant légèrement la syntaxe ci-dessus.

```
def checking(n):
```

```
    if type(n) == str:
```

```
        print("Chaîne !")
```

```
    elif type(n) == int:
```

```
        print("Entier !")
```

```
    else:
```

```
        print("nous ne sommes pas sûrs de ce qu'est n....")
```

```
x = [1,2,3,'a','bac',2.12]for i in x:    checking(i)
```

Points à noter :

1. Nous avons utilisé l'instruction elif dans ce contexte pour ajouter un cas possible supplémentaire de n que nous voulons prendre en compte.
2. Nous avons également utilisé le type comme condition pour évaluer la variable au lieu de l'utilisation originale de la valeur de la variable.

### Gestion des exceptions

Parfois en python, vous constaterez que vous devrez prendre en compte les exceptions. Il peut s'agir d'opérations invalides (par exemple, essayer de diviser par 0 ou un débordement de pile) ou d'une classe de valeurs qui ne vous intéressent tout simplement pas.

Dans ces cas, nous pouvons utiliser

1. Continue
2. Pass
3. Try-except
4. Break

Je vais essayer de donner un aperçu rapide de l'utilisation de ces opérations de gestion des exceptions.

#### Continue

Regardez le code ci-dessous et essayez de deviner ce que fait continue :

```
y = [1,2,3,4,5,6,6,7,8]
```

```
x = []
```

```
for i in y:
```

```
     if i in x:
```

```
         continue
```

```
     else:
```

```
         x.append(i)     print(i)
```

```
print(x)
```

Si vous avez deviné qu'il saute essentiellement le reste du bloc de code, vous avez raison ! Continue fait exactement cela.

Dans le code ci-dessus, nous essayons de supprimer les valeurs en double dans y. Nous le faisons dans le code en utilisant ce processus

1. Nous vérifions si la variable, i, que nous évaluons est dans la nouvelle liste x.
2. Si elle est dans la nouvelle liste x, nous « continuons » et procédons à l'évaluation de la variable suivante dans la liste y.
3. si elle n'est pas dans la nouvelle liste x, nous ne « continuons » pas et procédons plutôt à l'ajout de la variable à la liste x.

Cela nous aide finalement à supprimer toutes les variables en double dans x.

#### Pass

```
y = [1,2,3,4,5,6,6,7,8]
```

```
x = []
```

```
for i in y:
```

```
    if i in x:
```

```
         pass
```

```
    else:
```

```
         x.append(i)    print(i)
```

```
print(x)
```

Si vous deviez exécuter le code, vous remarqueriez également que toutes les variables en double ont été imprimées ! C'est une différence clé entre pass et continue.

Cette différence devient utile si vous essayez d'exécuter des opérations supplémentaires sur les variables non dupliquées (par exemple, obtenir une somme).

#### Break

Break fait ce qu'il dit. Il interrompt votre programme ou sous-programme lorsque vous rencontrez une exception.

Voici un exemple utile de break :

```
x = [1,3,5,7,2,3,5,7]
```

```
count = 0
```

```
for i in range(len(x)):
```

```
if x[i]%2==0:
```

```
    print("Il y a un nombre pair à l'index " + str(i))
```

```
    break
```

```
else:
```

```
    continue
```

Dans cet exemple, nous essayons de trouver l'index du premier nombre pair dans notre liste x. Break nous permet de le faire en sortant de la boucle prématurément !

#### Try-Except

La syntaxe Try-Except est particulièrement utile lorsqu'il s'agit de gérer les erreurs de lecture de fichiers ou d'évaluation de syntaxe. Certaines des erreurs d'exception courantes sont

1. IOError : Une incapacité à ouvrir le fichier
2. ImportError : Python ne peut pas trouver et ouvrir le module que vous souhaitez importer
3. ValueError : Lorsque vous passez une valeur dans une fonction avec le mauvais type ou valeur
4. KeyboardInterrupt : Lorsque vous terminez prématurément votre programme
5. EOFerror : Lorsque vous avez atteint la fin du fichier

Voici un exemple de nous essayant de vérifier une ValueError :

```
try:
```

```
    x = int(input("Veuillez entrer quelques nombres : "))
```

```
    print(x)
```

```
except ValueError as ve:
```

```
    print("Veuillez entrer des nombres. DES NOMBRES, pas des lettres")
```

Ce programme fonctionne parce que les chaînes et les lettres ne peuvent pas être converties en entiers. (Sauf s'il s'agit d'entiers qui ont été stockés sous forme de chaînes, c'est-à-dire "2", "3", etc.)

Pour ceux qui travaillent avec l'importation de fichiers, vous êtes peut-être familier avec les ImportErrors. Ceux-ci peuvent être pris en compte en utilisant la syntaxe suivante :

```
try:
```

```
    f = open('nofile.txt')
```

```
except FileNotFoundError:
```

```
    print("Erm...il n'y a pas de tel fichier, mon ami")
```

La syntaxe Try-except peut être pensée comme suit.

```
try:    <code à exécuter dans un monde parfait>except <Nom de l'erreur la plus probable>:    <code à exécuter en cas d'erreur 1>except <Autre erreur probable>:    <code à exécuter en cas d'une autre erreur improbable>
```

### Conclusion

Cela résume à peu près la prise de décision de base en Python et dans de nombreux autres langages de programmation. Bien que la syntaxe exacte diffère certainement, les principes de base sont à peu près les mêmes.

Une fois que vous aurez compris le contrôle de flux, vous serez en mesure de créer des programmes qui feront une grande différence et pourront fonctionner comme vous le souhaitez ! :)

Si vous souhaitez lire davantage sur les variables en Python, consultez un article que j'ai écrit à leur sujet [ici](https://medium.com/@ivanleomk/a-crash-course-in-python-variables-cbad43b4efef) !