---
title: Vous voulez apprendre Python ? Voici notre cours interactif gratuit de 4 heures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-03T13:06:34.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-python-heres-our-free-4-hour-interactive-course
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/gpython.jpg
tags:
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Vous voulez apprendre Python ? Voici notre cours interactif gratuit de
  4 heures
seo_desc: 'By Per Harald Borgen

  Python is a popular, versatile and easy-to-learn language. It''s the go-to language
  for AI, Machine Learning and Data Science. Some say it''s also the easiest programming
  language to get started with.

  If this sounds like a programm...'
---

Par Per Harald Borgen

Python est un langage populaire, polyvalent et facile à apprendre. C'est le langage de prédilection pour l'IA, le Machine Learning et la Data Science. Certains disent que c'est aussi le langage de programmation le plus facile pour commencer.

Si cela ressemble à un langage de programmation que vous voulez apprendre, continuez à lire ! Dans les prochains paragraphes, je vais vous guider à travers [le cours interactif gratuit de 4 heures sur Python](https://scrimba.com/g/gpython?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) que nous avons lancé aujourd'hui. 

%[https://twitter.com/scrimba/status/1234834344461643778]

Ce cours vise à vous donner une base solide en Python et en programmation de base en général. Il est idéal pour les débutants qui cherchent une manière interactive et engageante d'apprendre à coder.

Le cours a été créé par notre brillant enseignant [Olof Paulson](https://twitter.com/OlofPaulson), qui est l'un des défenseurs de la Khan Academy en suédois. Olof a un passé dans la finance, est expérimenté dans l'écriture d'algorithmes, et a une passion pour l'éducation ouverte et accessible.

Maintenant, jetons un coup d'œil à la structure du cours !

## 1. Introduction au cours

Ce cours couvre tous les sujets dont vous avez besoin pour passer d'un débutant à un développeur Python intermédiaire. Il aborde :

* L'affichage de données et le flux de programme
* Les chaînes de caractères, les variables
* Les opérations arithmétiques et les comparaisons
* Les listes, les tuples, les ensembles et les dictionnaires
* Les conditionnelles, if et elif
* Les boucles while et for
* Les fonctions / les instructions return
* Les objets, les classes et l'héritage
* Les comprehensions de liste / dictionnaire et les fonctions lambda
* Les modules

## 2. Exécuter Python sur Scrimba avec Brython

Pour faire fonctionner un langage back-end comme Python sur une plateforme front-end comme Scrimba, nous utilisons le plugin Brython dans le fichier `index.html` pour recompiler le code Python en JavaScript.

Généralement, nous utiliserons la version minimale JS (`brython.min.js`) mais pour plus de fonctionnalités, il suffit de décommenter la version standard lib (`brython_stdlib.js`).

```html
<head>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.8.0/brython.min.js"></script>
	<!--<script type="text/javascript"
     src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.8.0/brython_stdlib.js"></script>-->
</head>

```

Il est également utile de noter quelques particularités de Brython dans Scrimba :

1. La boîte `input()` est la boîte de dialogue JS et n'est pas visible dans le cast mais fonctionne lorsque vous exécutez le code localement.
2. Le mini-navigateur Scrimba flotte parfois dans le coin pendant certains tutoriels - vous n'avez pas à vous en soucier.

## 3. Instruction Print et flux de programme

Lorsque nous écrivons en Python, nous voulons souvent tester que cela fonctionne comme prévu. Pour ce faire, nous utilisons la commande `print()` pour afficher des données dans la console.

```python
print('Bienvenue à Python 101 !')

```

**Note :** L'ordinateur lit le code de haut en bas, donc il exécute les commandes près du haut en premier.

## 4. Variables

Les variables sont utilisées pour sauvegarder des données pour une utilisation ultérieure. Nous déclarons des variables en utilisant leur nom en minuscules suivi de l'opérateur d'affectation de base (`=`). Notez que si le nom de la variable se compose de plus d'un mot, ils doivent être séparés par un trait de soulignement (`_`).

```python
failed_subjects="6"

```

Nous utilisons des variables dans notre code en les précédant d'un signe plus (`+`).

```python
print('Votre fils Eric échoue' + failed_subjects + ' matières.')

```

## 5. Types de données et transtypage

Les types de données de base de Python sont :

* **Chaînes de caractères** - celles-ci sont entourées de deux guillemets (peuvent être des guillemets doubles ou simples).
* **Entiers** - ce sont des nombres entiers.
* **Flottants** - nombres avec des points décimaux.
* **Booléens** - ceux-ci prennent la valeur `true` ou `false`.

Pour savoir quel type de données vous utilisez, utilisez `type()`

```python
print(type('hello'))

```

**Note :** Si vous voulez utiliser des guillemets ou une apostrophe dans une chaîne de caractères, entourez toute la chaîne de guillemets doubles. Alternativement, vous pouvez utiliser le caractère d'échappement de Python, qui est l'antislash (`\`)

```python
a="it's"
b='it\'s'

```

Il existe des règles concernant le mélange des types de données, par exemple vous ne pouvez pas mettre des nombres à l'intérieur d'une chaîne de caractères. Le `transtypage`, ou changement de type, résout ce problème.

* `str()` change les données en une chaîne de caractères.
* `int()` change les données en un entier.
* `float()` change les données en un flottant.

```python
print('Votre fils ' + name + ' échoue ' + str(failed_subjects) + ' matières.')

```

## 6. Variables et types de données - Exercice

Il est temps pour votre tout premier défi Scrimba Python ! Dans ce cast, vous pouvez mettre à l'épreuve vos nouvelles connaissances sur les variables et les types de données. Essayez de résoudre le défi par vous-même, puis [consultez la solution d'Olof](https://scrimba.com/p/pNpZMAB/cZPZ6wSb?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour voir si vous êtes sur la bonne voie.

## 7. Opérations arithmétiques

Ici, nous apprenons que les opérations arithmétiques de base en Python sont l'addition, la soustraction, la multiplication, la division flottante (qui retourne un nombre à virgule flottante), la division entière (qui arrondit le résultat à l'entier inférieur le plus proche), le modulo (qui retourne le reste du calcul) et l'exponentiation (qui multiplie un nombre par la puissance d'un autre nombre).

```python
a=10
b=3
print('Addition : ', a + b)
print('Soustraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (flottante) : ', a / b)
print('Division (entière) : ', a // b)
print('Modulo : ', a % b)
print('Exponentiation : ', a ** b)

```

## 8. Chaînes de caractères - Bases / Découpage

Dans ce cast, nous apprenons quelques concepts de base concernant l'utilisation des chaînes de caractères.

* Multiplier les chaînes de caractères nous permet d'imprimer une chaîne plusieurs fois. Il y a trois façons de faire cela (la dernière insère un espace entre les chaînes) :

```python
print(msg+msg)
print(msg*2)
print(msg,msg)

```

Nous pouvons changer la casse des chaînes de plusieurs manières :

* `upper()` change la chaîne en majuscules.
* `lower()` change la chaîne en minuscules.
* `capitalize()` met en majuscule le premier mot d'une chaîne.
* `title()` met en majuscule chaque mot d'une chaîne.

```python
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())

```

Nous pouvons utiliser les fonctions suivantes pour obtenir des informations sur une chaîne :

* `print(len(msg))` nous indique combien de caractères la chaîne contient (dans ce cas, `msg`).
* `print(msg.count('Python'))` compte le nombre d'instances d'un mot ou d'une lettre - notez que cela est sensible à la casse.

Nous accédons aux chaînes avec des crochets (`[]`).

```
print(msg[0])

```

**Note :** Les chaînes de caractères Python sont indexées à partir de 0, c'est-à-dire que le premier caractère est compté comme 0 et non 1. L'utilisation d'index négatifs commence le compte à partir de la fin de la chaîne.

Le retour de parties d'une chaîne est connu sous le nom de _découpage_. Olof nous montre comment découper avec quelques exemples :

* `print(msg[a:])` retourne tout après le caractère à la position spécifiée.
* `print(msg[a:b])` retourne tout entre les positions spécifiées, sans inclure la position de fin.
* `print(msg[:b])` retourne tout jusqu'à la position spécifiée, encore une fois, sans inclure la position de fin.

## 9. Exercice - Chaînes de caractères - Bases / Découpage

Il est temps pour un exercice sur les chaînes de caractères. En plus de nous permettre de pratiquer les compétences que nous avons apprises dans les casts précédents, ce défi nous fait également réfléchir à une compétence qu'Olof ne nous a pas explicitement enseignée :

![Portée de Python 101](https://dev-to-uploads.s3.amazonaws.com/i/jvrzvgqn5zmn0fx82b87.png)

  
_Cliquez sur l'image pour accéder au défi._

C'est une excellente introduction à la vie en tant que programmeur à part entière - n'oubliez pas que Google est votre ami ! Consultez [le reste du cast](https://scrimba.com/p/pNpZMAB/c8rPnyCa?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour voir comment Olof l'a fait.

## 10. Chaînes de caractères - 2 Rechercher/remplacer, Formatage de chaîne

Ce cast nous enseigne encore plus sur le travail avec les chaînes de caractères.

* Nous pouvons créer des chaînes de caractères multi-lignes avec des triples guillemets :

```python
msg="""Cher Terry,,
Tu dois abattre le plus puissant
arbre de la forêt avec...
un hareng ! <3"""

```

Olof nous montre quelques exemples de travail avec des chaînes de caractères :

`print(msg.find('Python'))` retourne la position des mots ou caractères que nous recherchons (dans ce cas, 'Python').

`print(msg.replace('Python','Java'))` nous permet de remplacer des mots ou des caractères dans une chaîne. Notez que les chaînes sont immuables en Python, donc pour utiliser le résultat de cette fonction, vous devez l'enregistrer dans une variable.

```python
msg1=msg.replace('Python','C')

```

`print('Python' in msg)` nous indique si un mot ou un caractère existe dans une chaîne en retournant `true` ou `false`.

`msg1 = f'[{name}] loves the color {color}!'` nous permet de formater des chaînes pour qu'elles soient plus lisibles.

## 11. Saisie utilisateur

En Python, nous capturons la saisie utilisateur et l'affichons comme ceci :

```python
name= input('Quel est votre nom ? : ')
print(name)

```

Cela fait apparaître un champ de saisie utilisateur qui ressemble à ceci :

![Champ de saisie utilisateur en Python](https://dev-to-uploads.s3.amazonaws.com/i/rgz3kqhih93de1z2vk08.png)

## 12. Saisie utilisateur - Exercice

Il est temps de faire travailler nos muscles de programmation avec un exercice de saisie utilisateur ! Dans ce cast, vous allez créer un convertisseur de distance en utilisant les indices ci-dessous :

![Indices du défi des saisies utilisateur](https://dev-to-uploads.s3.amazonaws.com/i/hkdtyr6irt83v1vjd9m6.png)

  
_Cliquez sur l'image pour accéder au défi._

Comme d'habitude, essayez le défi par vous-même et vérifiez ensuite [la solution d'Olof](https://scrimba.com/p/pNpZMAB/ceMDmvTB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour voir si vous avez réussi.

## 13. Listes - Bases

Alors qu'une variable contient une seule donnée, une liste en contient plusieurs.

```py
friends = ['John','Michael','Terry','Eric','Graham']

```

Les listes sont également indexées à partir de zéro, et peuvent être accédées avec des crochets, tout comme les chaînes de caractères :

```py
print(friends[1])

```

Nous pouvons également utiliser les mêmes commandes que nous avons utilisées avec les chaînes de caractères pour trouver la longueur d'une chaîne, trouver certaines données dans une chaîne, etc.

```py
print(friends[1],friends[4])
print(len(friends))
print(friends.coun('Eric'))

```

## 14. Listes - suite

Ce cast nous montre quelques compétences essentielles pour utiliser les listes, telles que le tri (`sort()`), trouver la somme (`print(sum()`), ajouter de nouvelles données (`append('')`), ajouter deux listes ensemble (`.extend()`), supprimer des éléments (`.remove('')`), extraire des éléments (qui supprime un élément mais permet toujours de le retourner) (`.pop()`), et vider la liste (`.clear()`).

## 15. Listes - Exercice

Dans cet exercice, nous allons manipuler des listes.

![Description du défi](https://dev-to-uploads.s3.amazonaws.com/i/1nyb5f534aqwugnws457.png)

  
_Cliquez sur l'image pour vérifier la solution._

Essayez par vous-même et consultez ensuite [la solution d'Olof](https://scrimba.com/p/pNpZMAB/cLpzgpSy?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour vérifier comment cela s'est passé.

## 16. Split et Join

Ce cast examine la division et la jonction de parties de chaînes de caractères.

```py
print(msg.split())
print('-'.join(friends_list))

```

## 17. Split et Join - Exercice

Ici, vous utiliserez ce que vous savez maintenant sur la division et la jonction pour créer une liste d'amis à partir d'une chaîne de caractères.

Comme d'habitude, essayez par vous-même et consultez ensuite [la solution d'Olof](https://scrimba.com/p/pNpZMAB/cJp2gEcW?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour vérifier votre travail.

## 18. Tuples

Les tuples sont des listes que vous ne pouvez pas changer. Ils ressemblent aux listes mais sont entourés de parenthèses au lieu de crochets.

```py
friends_tuple = ('John','Michael','Terry','Eric','Graham')

```

Vous devriez utiliser des tuples au lieu de listes lorsque vous voulez vous assurer que vos données ne changeront pas au cours de l'exécution de votre programme.

## 19. Ensembles

Les ensembles sont similaires aux listes et aux tuples mais ils sont non ordonnés et suppriment les doublons à l'intérieur. Ils sont également très rapides. Les ensembles sont entourés d'accolades.

```py
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}

```

Dans ce cast, Olof nous montre quelques astuces et conseils pour utiliser les listes. **Note :** Créer un ensemble vide fonctionne différemment de la création d'une liste ou d'un tuple vide :

```py
#listes vides
empty_list = []
empyt_list = list()

#tuple vide
empty_tuple = ()
empty_tuple = tuple()

#ensemble vide
empty_set = {} # ceci est incorrect, c'est un dictionnaire
empty_set = set()

```

## 20. Ensembles - Exercice

Ici, nous allons mettre à l'épreuve nos nouvelles connaissances sur les ensembles. Jetez un coup d'œil à [la fin du cast](https://scrimba.com/p/pNpZMAB/caqBRLsW?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour vérifier votre réponse.

## 21. Commentaires

Les commentaires sont du texte dans le code que Python ignore. Ils sont principalement utilisés pour la communication entre humains, par exemple des notes sur le code, le débogage ou les tests, et la documentation du code. Les commentaires sont précédés du signe dièse (`#`) :

```py
#Caché dans les commentaires

```

## 22. Fonctions - Appel, Paramètres, Arguments, Valeurs par défaut

Dans ce cast, Olof nous présente les fonctions - des ensembles de code que nous pouvons réutiliser plus tard.

Les fonctions sont créées (définies) avec `def` et appelées avec le nom de la fonction plus des parenthèses `()` :

```py
def greeting():
    print("Hello Friend!")

greeting()

```

Nous examinons également les chaînes de caractères formatées, et comment leur utilisation rend le code plus lisible et plus efficace.

```py
def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")

```

## 23. Fonctions - Exercice

Ici, Olof nous donne la tâche de modifier et d'étendre la fonctionnalité d'une fonction existante. Essayez et regardez ensuite [le reste du cast](https://scrimba.com/p/pNpZMAB/c67dzEAV?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour voir si vous êtes sur la bonne voie.

## 24. Fonctions - Notation nommée

La notation nommée est la pratique de nommer les arguments lors de l'appel d'une fonction afin que la définition de la fonction comprenne quel argument est lequel, même s'ils apparaissent dans un ordre différent.

```py
Profile(yob=1995,weight=83.5,height=192,eye_color="blue")

```

## 25. Instructions return

Ce cast nous montre les instructions return. Une instruction return nous permet de récupérer nos données après avoir effectué une fonction.

```py
def value_added_tax(amount):
    tax = amount * 0.25
    return tax

```

Olof nous montre également quelques façons pratiques de manipuler nos données retournées, y compris la création de chaînes, d'ensembles et de tuples avec elles.

## 26. Comparaisons et booléens

Ce tutoriel passe rapidement en revue quelques façons de comparer des données, y compris égal (`==`), n'est pas égal (`!=`), supérieur à (`>`), supérieur ou égal à (`>=`), inférieur à (`<`), inférieur ou égal à (`<=`), dans (`in`), pas dans (`not in`), est (`is`) et n'est pas (`is not`).

Nous examinons également quelques propriétés booléennes et apprenons que `false` évalue à 0 et `true` évalue à 1. Les objets vides et les zéros évaluent à false et tout le reste (chaînes de caractères, nombres sauf 0, etc.) évalue à true.

## 27. Conditionnelles : If, Else, Elif

Les conditionnelles nous permettent d'exécuter différents codes pour différentes circonstances. Les instructions `if` s'exécutent si la fonction retourne true, les instructions `elif` (else if) s'exécutent si les fonctions retournent true après qu'une autre instruction a retourné false, et les instructions `else` s'exécutent si aucune des instructions précédentes n'a retourné true, c'est-à-dire dans toutes les autres éventualités.

```py
is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Shirt is fine!")

```

## 28. If/Elif/Else - Exercice

Il est temps de faire travailler nos muscles conditionnels avec un exercice. Nous avons également l'occasion d'essayer une fonctionnalité étendue avec un convertisseur de température.

Comme d'habitude, allez-y et voyez si vous pouvez le résoudre vous-même et vérifiez votre réponse par rapport à [la solution d'Olof](https://scrimba.com/p/pNpZMAB/c2PWdWCN?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

## 29. Conditionnelles - Exercice d'amélioration

Le cast nous donne l'occasion d'essayer une optimisation en raccourcissant le code et en réduisant le nombre de conditionnelles qu'il contient. 

Il existe de nombreuses façons différentes d'y parvenir, alors essayez par vous-même et comparez ensuite votre réponse à la manière dont Olof s'y prend à la [fin du cast](https://scrimba.com/p/pNpZMAB/cPJDRNcr?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

## 30. Boucles While

Les boucles While sont du code qui s'exécute de manière répétée jusqu'à ce qu'une condition lui dise de s'arrêter. Pour créer une boucle, commencez par vous poser ces questions :

Qu'est-ce que je veux répéter ?

Qu'est-ce que je veux changer à chaque fois ?

Combien de temps devons-nous répéter ?

Dans l'exemple ci-dessous, nous voulons répéter l'ajout de un, nous voulons changer `i`, et nous voulons que cela se répète jusqu'à ce que le nombre cinq soit atteint :

```py
i=0
while i < 5:
    i+=1
    print(f"{i}."+ "*"*i + "Les boucles sont géniales" + "*"*i)

```

## 31. Boucles While - Exercice

Il est temps pour un exercice sur les boucles. Dans ce défi, nous allons créer un jeu de devinettes amusant. N'oubliez pas de considérer les trois questions sur les boucles du chapitre précédent avant de commencer, puis vérifiez la solution à la [fin du cast](https://scrimba.com/p/pNpZMAB/cV8WmMcM?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour voir comment cela s'est passé.

## 32. Boucles For et imbrication

Les boucles For nous permettent d'exécuter une instruction pour chaque élément d'une chaîne, liste, tuple ou ensemble. Par exemple, le code suivant imprime chaque nombre entre deux et huit :

```py
for number in range(2,8):
    print(number)

```

Il est également possible d'imbriquer des boucles à l'intérieur d'autres boucles. Le code ci-dessous imprime chacun des nombres 1, 2 et 3 pour chaque ami (John 1, John 2, John 3, Terry 1, Terry 2, Terry 3, etc.)

```py
friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

```

Dans ce cast, nous apprenons également quelques mots-clés pratiques pour les boucles for, tels que `break` et `continue`.

## 33. Boucles For - Exercice

Il est temps de tester ce que nous avons appris sur les boucles for avec un exercice. Cette fois, nous allons créer des invitations à une fête personnalisées. Nous avons également un mini-défi consistant à inclure une capitalisation appropriée

![description de l'exercice sur les boucles for](https://dev-to-uploads.s3.amazonaws.com/i/f8sfknbcdahv4r3s75zv.png)

  
_Cliquez sur l'image pour accéder au défi._

Comme d'habitude, voyez comment cela se passe par vous-même et vérifiez ensuite [la solution](https://scrimba.com/p/pNpZMAB/czkEGktv?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) pour comparer votre réponse.

## 34. Dictionnaires

Ce cast nous présente les dictionnaires. Les dictionnaires sont utilisés en Python pour stocker des paires clé-valeur, et ils fonctionnent de manière similaire à un dictionnaire physique. Vous cherchez un mot (la clé) et obtenez une définition ou une traduction (la valeur) en retour.

```py
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

```

Olof nous montre également comment changer les entrées dans un dictionnaire et en ajouter de nouvelles, ainsi que comment gérer le message d'erreur causé par les utilisateurs qui cherchent des entrées qui n'existent pas et comment exécuter des boucles for sur les données du dictionnaire.

```py
for key, value in movie.items():
    print(key, value)

```

## 35. Sort() et Sorted()

Ici, nous apprenons la différence entre `sort()` et `sorted()`. Bien que les deux fonctions trient le contenu d'une liste, seule `sorted()` retourne les résultats.

Nous examinons également le comportement des dictionnaires, des tuples et des chaînes lorsqu'ils sont triés et voyons une brève introduction aux _fonctions lambda_ - des fonctions jetables pratiques en une ligne, que nous verrons plus en détail dans un tutoriel ultérieur. L'exemple lambda ci-dessous trie la liste selon les premières entrées :

```py
my_list=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list, key = lambda item :item[0]))

```

## 36. Exceptions : Try/Except, Raise

Dans ce cast, Olof nous montre quelques techniques pour gérer les erreurs. Nous le faisons avec des blocs `try-except`, qui ressemblent à ceci :

```py
#try:
    #code que vous voulez exécuter
#except:
    #exécuté si une erreur se produit
#else:
    #exécuté si aucune erreur
#finally:
    #toujours exécuté

```

## 37. Classes et Objets

Ensuite, Olof nous montre les classes et les objets. Il y a quatre concepts principaux à comprendre en ce qui concerne les classes. Ce sont les classes, les objets, les attributs et les méthodes.

Les classes sont des plans qui nous montrent la structure des données requises. Les objets contiennent les données réelles que nous utilisons. Les attributs sont des variables au sein d'une classe et les méthodes sont des fonctions au sein d'une classe.

Nous initialisons une classe avec l'instruction d'initialisation `init` :

```py
class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

```

**Note :** Par convention, nous utilisons le mot-clé `self` lors de la nomination des attributs.

Ayant fait cela, nous pouvons maintenant créer des instances de la classe, comme ci-dessous :

```py
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("The Holy Grail",1975,8.2,True)

```

Les méthodes sont définies dans les classes comme suit :

```py
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)

```

Il y a deux façons d'appeler des méthodes (la sortie est la même) :

```py
film_2.nice_print()
Movie.nice_print(film_2)

```

## 38. Héritage

Dans ce cast, Olof nous montre le concept d'héritage. L'héritage nous permet d'utiliser les méthodes d'une classe dans une autre classe sans répéter tout le code. Nous pouvons ensuite ajouter d'autres méthodes pour différencier les classes les unes des autres.

```py
class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")
class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")

```

Une classe peut hériter de plusieurs autres classes. Si les classes ont des sorties différentes pour la même méthode, la classe choisira la méthode héritée qui est déclarée en premier. 

Dans l'exemple ci-dessous, la classe Wizard héritera de toute méthode partagée du Doctor et non du Fighter.

```py
class Wizard(Doctor,Fighter):
    def cast_spell(self):
        print("Turns invisble")
    def heal(self):
        print("Heals 15 health points")

```

## 39. Modules

Maintenant, il est temps de regarder les modules. Les modules sont des extraits de code que vous pouvez importer et utiliser dans le code. Certains modules couramment utilisés fournis par Python sont `datetime`, `random`, `string`, `os`, `math`, `browser` et `platform`

Pour utiliser les modules, nous devons d'abord importer la version standard lib de Brython :

```html
<head>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.7.0/brython.min.js"></script>
	<script
		type="text/javascript"
		src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.7.0/brython_stdlib.js"
	></script>
	-->
</head>

```

Les modules sont importés avec le mot-clé `import` et peuvent recevoir un alias plus facile à utiliser avec `as` :

```py
import platform as pl

print(pl.python_version())

```

## 40. Zip / Unzip

Dans ce cast, Olof nous montre comment zipper et dézipper des objets. Le zippage nous permet de combiner deux ou plusieurs objets itérables (chaînes de caractères, tuples, listes, etc.).

```py
nums = [1,2,3,4]
letters = ['a','b','c','d']
combo = list(zip(nums,letters))
print(combo)

```

L'exemple ci-dessus transforme les itérables combinés en une liste, mais nous pourrions également le transformer en un tuple, un ensemble ou un dictionnaire. **Note :** Un dictionnaire n'est pas adapté pour zipper plus de deux objets.

Le dézippage nous permet d'assigner les résultats dans des variables séparées, dans ce cas `num`, `let` et `nam`.

```py
num,let,nam =zip(*combo)

```

## 41. Fonctions Lambda partie 1

Ici, nous examinons de plus près les lambdas, ou fonctions anonymes, qui vous permettent d'écrire des définitions de fonctions jetables en une seule ligne, que vous pourriez utiliser une seule fois. Comparez ce qui suit :

**Fonction standard :**

```py
def square(x):
    return x*x
print(square(3))

```

**Lambda :**

```py
square1 = lambda x: x*x

```

**Note :** La valeur de retour dans un lambda est implicite.

## 42. Fonctions Lambda Partie 2

Dans ce cast, nous approfondissons les lambdas. Bien que nous puissions toujours répliquer un lambda avec une fonction standard, il existe certaines instances où les lambdas sont significativement meilleurs.

Dans cet exemple, la valeur de retour du lambda est une fonction, ce qui nous donne la capacité de réutiliser le lambda pour plusieurs tâches différentes. Dans le code ci-dessous, nous utilisons un seul lambda pour multiplier par deux et cinq :

```py
def func(n):
    return lambda a: a*n
# a*2
doubler = func(2)
print(doubler(3))
quintipler = func(5)
print(quintipler(3))
print(type(func(3)))

```

Ce cast explique également que nous pouvons appeler les lambdas dès que nous les créons.

```py
print((lambda a,b,c: a+b+c)(2,3,4))

```

## 43. Fonctions Lambda - Exercice

Maintenant, il est temps de pratiquer la création de quelques-unes de nos propres lambdas.

Voyez comment vous vous en sortez et vérifiez vos réponses par rapport aux [solutions d'Olof](https://scrimba.com/p/pNpZMAB/cKpNKbuQ?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) au fur et à mesure.

## 44. Comprehensions - Listes

Les comprehensions Python nous permettent de créer des listes, des tuples, des ensembles et des dictionnaires avec moins de code. **Note :** Tout ce qui peut être créé dans une compréhension peut également être créé avec une boucle for, cependant la boucle for nécessite plus de code.

Olof fournit également une diapositive pratique pour donner une comparaison visuelle des boucles for et des comprehensions dans deux cas différents.

![comparaison des boucles for et des comprehensions](https://dev-to-uploads.s3.amazonaws.com/i/ifdzdxg0tux7n3u9llrq.png)

  
_Cliquez sur la diapositive pour accéder au cast._

## 45. Comprehensions - Dictionnaire

Olof nous montre maintenant comment créer un nouveau dictionnaire en utilisant une compréhension. Si nous devions faire cela avec une boucle for, le code ressemblerait à ceci :

```py
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

```

Avec une compréhension, cela ressemble à ceci :

```py
new_dict = {movie:yr for movie,yr in zip(movies,year)}
print(new_dict)

```

Beaucoup plus concis et lisible !

## 46. Aléatoire

Ce cast nous montre le module `random` et nous apprend à générer des événements pseudo-aléatoires. Pour utiliser le module, nous l'importons d'abord :

```py
import random

```

Nous pouvons ensuite utiliser le module pour générer des nombres pseudo-aléatoires :

```py
for i in range(5):
    print(random.random()*6)

```

Olof nous montre également une variété de fonctions que nous pouvons utiliser avec `random`.

L'utilisation de `random` n'est pas limitée aux nombres. Nous pouvons également l'utiliser avec des itérables :

```py
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))

```

Enfin, Olof nous montre les modules `string` et nous apprenons à créer des mots pseudo-aléatoires.

```py
import random, string

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
word = ''
for i in range(7):
    word += random.choice(letters_numbers)
word1 = ''.join(random.sample(letters_numbers,7))
word = random.choices(letter_numbers, k=7)
print(word)
print(word1)

```

**Note :** Ces mots ne sont pas vraiment aléatoires et ne doivent donc pas être utilisés pour générer des mots de passe.

## 47. Projet - Machine de cryptage

Maintenant que nous approchons de la fin du cours, Olof nous donne un grand projet pour nous mettre sous la dent. Jetez un coup d'œil aux instructions, suivez-les et essayez de faire chaque étape par vous-même, avant de vérifier [la solution d'Olof](https://scrimba.com/p/pNpZMAB/cEK2WJtd?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

## 48. Projet - Tuteur de maths

Notre deuxième projet est de créer un tuteur de maths qui nous aide à apprendre les tables de multiplication. Jetez un coup d'œil aux instructions ci-dessous, essayez le projet et consultez ensuite [comment Olof le fait](https://scrimba.com/p/pNpZMAB/cdNBZVh9?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

![Instructions du projet Math Tutor](https://dev-to-uploads.s3.amazonaws.com/i/i4tlk2xmd7rymmap0q3r.png)

  
_Cliquez sur l'image pour accéder au défi._

## 49. Résumé du cours

Félicitations pour être arrivé à la fin du cours Python 101 ! Nous avons abordé l'affichage de données et le flux de programme, les chaînes de caractères, les variables, les opérations arithmétiques, les comparaisons, les listes, les tuples, les ensembles, les dictionnaires, les conditionnelles, les boucles, les fonctions, les objets, les classes, l'héritage, les comprehensions, les lambdas et les modules - vous pouvez donc être fier de vous !

![Félicitations !](https://dev-to-uploads.s3.amazonaws.com/i/lzhvvngzvjy9fjvk1bjd.png)

N'oubliez pas que vous pouvez toujours [vous référer au cours](https://scrimba.com/g/gpython?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) si nécessaire, ou refaire les exercices que vous n'avez pas bien compris (ou que vous avez particulièrement appréciés !)

Lorsque vous serez prêt à passer à autre chose, [Scrimba](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=gpython_launch_article) propose une gamme de cours pour vous enseigner votre prochaine compétence en codage, alors consultez-les !

![Allez-y](https://dev-to-uploads.s3.amazonaws.com/i/p3okn1zuv00xn11kge2x.png)

  
_Cliquez sur l'image pour voir la gamme de cours de Scrimba_

Bon codage ! :)

%[https://www.youtube.com/watch?v=ECW8t3Djfsg]