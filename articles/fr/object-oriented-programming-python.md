---
title: La programmation orientée objet en Python – Expliquée en français simple
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2023-09-07T18:39:52.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--524-.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: La programmation orientée objet en Python – Expliquée en français simple
seo_desc: '“Any fool can know. The point is to understand.” - Albert Einstein


  Object-oriented programming is a popular way to write computer programs.

  Because of this, all programmers should understand what OOP is, what languages you
  can use to program this wa...'
---

> « Tout le monde peut savoir. L'important, c'est de comprendre. » - Albert Einstein

La programmation orientée objet est une méthode populaire pour écrire des programmes informatiques.

Pour cette raison, tous les programmeurs devraient comprendre ce qu'est la POO, quels langages peuvent être utilisés pour programmer de cette manière, et pourquoi c'est important.

Lorsqu'on lui a demandé [en termes simples ce qu'est exactement un logiciel orienté objet](https://fossbytes.com/steve-jobs-tells-the-best-definition-of-object-oriented-programming/), Steve Jobs a répondu :

> *Les objets sont comme des personnes. Ce sont des choses vivantes qui ont des connaissances à l'intérieur sur la façon de faire les choses et une mémoire à l'intérieur pour qu'elles puissent se souvenir des choses.*
>
> *Et plutôt que d'interagir avec eux à un niveau très bas, vous interagissez avec eux à un niveau très élevé d'abstraction, comme nous le faisons ici même.*

Cependant, que signifie cela réellement en code ?

Ce guide couvrira les bases, y compris certains concepts que la plupart des tutoriels ne traitent pas, comme :

* Qu'est-ce que "__init__" ?
* Comment les méthodes et les fonctions diffèrent-elles ?
* Que signifie le paramètre "self" en Python ?

Le but de ce guide est de vous aider à comprendre les bases de la programmation orientée objet en Python. Alors, plongeons-nous dedans.

### Ce que nous allons couvrir :

1. [Qu'est-ce que la POO](#heading-quest-ce-que-la-poo) ?
2. [Qu'est-ce que les classes et les instances de classes](#heading-quest-ce-que-les-classes-et-les-instances-de-classes-ou-objets) ?
3. [Comment créer des classes avec "__init__"](#heading-comment-creer-des-classes-avec-init)
4. [Qu'est-ce que le mot-clé self](#heading-quest-ce-que-le-mot-cle-self) ?
5. [Variables d'instance vs variables de classe](#heading-variables-dinstance-vs-variables-de-classe)
6. [Méthodes en POO – Correction de l'exemple de prix d'inflation](#heading-methodes-en-poo-correction-de-lexemple-de-prix-dinflation)
7. [Où aller à partir d'ici](#heading-ou-aller-a-partir-dici)

Ce tutoriel suppose que vous connaissez [les bases de la programmation Python](https://www.youtube.com/watch?v=rfscVS0vtbw).

N'hésitez pas à utiliser le code et les images des articles dans le dépôt GitHub ci-dessous.

## Qu'est-ce que la POO ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/pexels-binyamin-mellish-106399.jpg)
_Photo par [Binyamin Mellish de Pexels](https://www.pexels.com/photo/house-lights-turned-on-106399/)_

Supposons que vous dirigez une entreprise de construction. Votre entreprise se développe. Votre objectif est de construire 100 nouvelles maisons.

Vous décidez que toutes les maisons auront plus ou moins la même structure.

En procédant ainsi, vous pouvez réduire les coûts et mieux gérer toutes les complexités impliquées dans la construction de maisons.

Chaque maison sera construite en utilisant le même plan de maison, conçu par un architecte.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/pexels-jeshootscom-834892.jpg)
_Photo par [JESHOOTS.com](https://www.pexels.com/photo/floor-plan-on-table-834892/)_

Au lieu de concevoir chaque maison à partir de zéro, toutes les maisons que vous construisez auront un plan de sol similaire.

Dans ce cas, vous pouvez dire que votre entreprise construit des maisons de manière orientée maison.

Dans cette analogie :

* Un dessin = une classe
* La maison = une instance de classe ou un objet
* Construction orientée maison = Programmation orientée objet

De la même manière que la construction orientée maison est une méthode efficace pour construire de nouvelles maisons, la programmation orientée objet est une méthode efficace pour écrire des programmes informatiques.

Pour vous assurer que tout s'est bien passé lors de la construction de votre première maison, vous avez commencé à donner des instructions aux gens sur la façon de faire les choses.

De même, la programmation commence par l'écriture de programmes qui donnent des instructions pour faire certaines choses d'une certaine manière.

En programmation orientée objet, cependant, vous créez des plans pour gérer et créer des données.

Avec la construction orientée maison, vous dessinez un plan de maison et décidez de quel matériel est nécessaire pour la construire.

Et en codage, l'utilisation de plans pour créer des objets vous permet de réutiliser votre code et de le développer facilement.

Il est plus facile de gérer la logistique de la construction de maisons lorsque vous avez un plan de maison à choisir, et vous pouvez ajuster le nombre de maisons à n'importe quel nombre que vous souhaitez. Il en va de même pour le code et la programmation orientée objet.

### Les principaux principes de la POO

Tout comme il existe diverses bonnes pratiques pour construire des maisons, il existe également de bonnes pratiques en programmation orientée objet.

Pour écrire un excellent code, la POO suit quatre piliers :

* Polymorphisme – Capacité d'un objet à prendre de nombreuses formes
* Héritage – Les classes enfants acquièrent des propriétés des classes parents
* Encapsulation – Protège les données et les méthodes contre les mauvaises utilisations externes en les liant ensemble
* Abstraction – Gère la complexité en masquant les détails inutiles à l'utilisateur.

Pour relier cela à notre exemple de construction orientée maison :

* Polymorphisme – La capacité d'une maison à avoir différents types de toits, de fenêtres, de portes, etc.
* Héritage – Une maison gagnant une nouvelle fonctionnalité, comme un garage.
* Encapsulation – Garder les enfants hors du garage en utilisant une clé de garage.
* [Abstraction](https://www.freecodecamp.org/news/what-is-abstraction-in-programming/) – Ignorer les matériaux de construction et la structure de la maison, et considérer simplement l'apparence du produit final.

Dans les exemples ci-dessus, nous avons parlé des concepts généraux – pas du code derrière chaque concept. Et nous ne couvrirons pas le code ici. Même ainsi, vous pouvez vous faire une idée de ce que chaque concept est et pourquoi il est important.

Si vous souhaitez en savoir plus sur le code, [vous pouvez lire ce tutoriel](https://www.freecodecamp.org/news/object-oriented-programming-in-python/).

### Peut-on écrire du code orienté objet dans différents langages ?

Utiliser la programmation orientée objet (POO) dans différents langages de programmation est possible, mais vous pouvez utiliser différentes techniques en fonction du langage et du type de programme que vous créez.

Par exemple, prenons Java. Il est conçu spécifiquement pour la POO. En Java, vous créez des classes et des objets pour structurer votre code.

C'est comme créer des plans puis construire avec ces plans.

Mais certains langages, comme C, fonctionnent de manière plus procédurale. Ils sont comme suivre une recette étape par étape au lieu d'utiliser des plans.

Dans le cas de Python, c'est un langage de programmation très flexible. Vous pouvez utiliser la POO en Python, où vous faites ces plans avec des classes.

Il peut également être utilisé pour la programmation procédurale, où vous donnez des instructions simples comme une liste de tâches.

L'utilisation de la POO peut être super utile lorsque vous travaillez sur des projets logiciels complexes.

Cela vous aide à garder les choses organisées, facilite la mise à jour de votre code et vous permet de réutiliser des parties de votre code dans différents endroits.

## Qu'est-ce que les classes et les instances de classes (ou objets) ?

Les instances sont créées sur la base d'une classe. Les classes sont des plans qui montrent à quoi ressemblera une instance de classe.

Les variables d'instance ont des données uniques à cette instance qui ne sont pas partagées entre toutes les classes.

Chaque instance a des attributs uniques, tout comme chaque maison.

Mais, à quoi ressemble tout cela en code réel ?

### Comment créer des classes manuellement :

```python
class maison():
    pass

maison1 = maison()
maison2 = maison()

maison1.adresse = 1234;
maison1.etat = "californie"
maison1.alarme = False;
maison1.prix = 300000;

maison2.adresse = 5678;
maison2.etat = "texas"
maison2.alarme = True;
maison2.prix = 100000;

print(maison1.etat)
print(maison2.prix)

>>> californie
>>> 100000
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/manually.png)

Dans la première ligne, nous avons créé un plan pour la maison sans rien de prédéfini.

C'est la même chose que lorsqu'un architecte a une feuille de papier blanche qui est le plan pour une maison – la feuille existe, mais elle ne contient rien.

Nous avons ensuite créé 2 maisons avec les mêmes caractéristiques :

* Adresse de la maison
* État de la maison
* Si elle a une alarme ou non
* Prix de la maison

Mais pour ajouter chaque caractéristique, nous avons dû insérer la valeur manuellement.

Mais, que faire si vous vouliez créer 100 maisons avec les caractéristiques individuelles remplies pour chaque maison ?

Ajouter tous ces attributs de classe manuellement est assez ennuyeux et chronophage.

Voyons comment nous pouvons simplifier cela :

### Comment créer des classes avec "__init__" :

```python
class maison():
    def __init__(self, adresse, etat, alarme, prix):
        self.adresse = adresse
        self.etat = etat
        self.alarme = alarme
        self.prix = prix


maison1 = maison(1234, "californie", False , 300000)

maison2 = maison(5678, "texas", True , 100000)

print(maison1.etat)
print(maison2.prix)

>>> californie
>>> 100000
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/automatic.py-1.png)

Les résultats de ce bloc de code et de celui de la section précédente sont les mêmes.

Le premier a 18 lignes et créer une maison est difficile. Le second a 14 lignes et une maison peut être facilement créée.

C'est l'essence de la programmation – automatiser les choses et les rendre plus faciles.

Vous pourriez avoir quelques questions sur le code ci-dessus. Examinons-le plus en détail.

### Qu'est-ce que "__init__" ?

`__init__` est le constructeur Python. Il indique à l'interpréteur Python que vous souhaitez **créer** une classe avec **certains attributs**, tels que le prix, l'état, etc., dans ce cas.

Il a les doubles underscores pour que l'interpréteur puisse distinguer entre les variables de code et les [méthodes spéciales Python](https://docs.python.org/3/reference/datamodel.html#special-method-names).

L'[utilisation des underscores](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name) est hors de portée pour cet article, alors sachez simplement ce qu'ils font ici.

Les attributs que vous souhaitez sont à côté du constructeur.

Mais, pourquoi y a-t-il une variable "self" ? Et que signifie self ?

## Qu'est-ce que le mot-clé `self` ?

Le mot-clé `self` vous indique simplement qu'un certain attribut change d'objet en objet.

Voici un exemple de ce que je veux dire :

```py
self.adresse = adresse
```

Est la même chose que d'écrire :

```py
maison1.adresse = 1234;
```

Cependant, en écrivant :

```python
  def __init__(self, adresse, etat, alarme, prix):
        self.adresse = adresse
        self.etat = etat
        self.alarme = alarme
        self.prix = prix
```

Vous dites que vous voulez **créer une maison** (`__init__`) avec quatre caractéristiques : adresse, état, alarme et prix.

Ensuite, vous dites que, dans toute instance de la classe, la **caractéristique** d'une maison est la même que celle des paramètres.

Ainsi, lorsque vous écrivez :

```python
maison1 = maison(1234, "californie", False , 300000)
```

Il pensera :

```
maison1.adresse = 1234
maison1.etat = "californie"
maison1.alarme = False
maison1.prix = 300000
```

Note : Au lieu d'utiliser self, vous pouvez utiliser n'importe quelle variable que vous voulez. C'est juste par convention de référencer l'instance de la classe que nous utilisons.

De plus, de cette manière, vous donnez une valeur à chaque attribut d'une classe très facilement.

### Pourquoi toute cette confusion ?

De cette manière, vous pouvez créer des attributs basés sur d'autres attributs qui doivent être déclarés à nouveau :

```python
class maison():
    def __init__(self, adresse, rue , etat):
        self.adresse = adresse
        self.rue = rue
        self.etat = etat

        self.adresseComplete = str(adresse) + " " + etat


maison = maison(1234, "californie", "route géniale")

print(maison.adresseComplete)

>>>1234 route géniale
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/completeAddress.py.png)

Avec self, nous pouvons créer d'autres attributs basés sur les paramètres de `__init__`.

La fonction `__init__` n'a pas de paramètre `adresseComplete`.

Il a été construit sur la base des valeurs d'adresse, de rue et d'état.

(Notez que ceci est une adresse aléatoire et n'est pas réelle.)

### Variables d'instance vs variables de classe

Jusqu'à présent, nous avons vu que nous pouvons construire de nombreuses maisons sur la base d'un seul plan de maison.

Mais nous n'avons pas encore terminé. Supposons que vous souhaitiez que chaque maison ait un grand tapis de salon.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/pexels-pixabay-carpet.jpg)
_Photo par [Pixabay de Pexels](https://www.pexels.com/photo/apartment-carpet-floor-furniture-276666/)_

Chaque pièce aura le **même** tapis dans chaque maison. D'autres choses dans la maison, comme le canapé, peuvent être **différentes**.

Supposons également que toutes les maisons auront un canapé.

Ainsi, en POO, le canapé est une **variable d'instance**, car chaque instance de la classe aura sa propre valeur pour cet attribut.

Par exemple, les attributs :

* adresse
* état
* alarme
* prix

sont tous des variables d'instance, car ils sont uniques à chaque instance.

Ainsi, le canapé est une **variable d'instance** – mais le tapis est une **variable de classe**.

Parce que c'est une variable de classe, toutes les instances de la classe auront cette variable.

Un autre exemple de variable de classe est le nom de l'entreprise qui construit les maisons :

```python
class maison():

    nom_entreprise = "Entreprise de construction géniale"

    def __init__(self, adresse, etat, alarme, prix):
        self.adresse = adresse
        self.etat = etat
        self.alarme = alarme
        self.prix = prix


maison1 = maison(1234, "californie", False , 300000)

maison2 = maison(5678, "texas", True , 100000)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/automaticV2.py.png)

La variable de classe ici est le nom de l'entreprise : "Entreprise de construction géniale".

Encore une fois, une variable contenant des données spécifiques à l'instance est appelée une variable d'instance – elle n'est pas partagée entre les classes.

Des variables telles que l'état ou le prix sont des variables d'instance.

* Variables d'instance = caractéristiques particulières de chaque maison (différentes)
* Variables de classe = Nom de l'entreprise qui construit la maison (identique)

Toutes les instances des classes contiennent des variables de classe, et chaque instance d'une classe a ses propres variables d'instance.

### Que se passe-t-il si les variables changent avec le temps ?

Les prix des maisons et l'inflation sont vraiment élevés en 2023. Si élevés que les prix des maisons ne reflètent plus leur valeur réelle. Le prix de la maison – ou de tout article – peut changer avec le temps en fonction de divers facteurs.

Par exemple, avec le temps, une maison qui était évaluée à 50 000 dollars coûtera maintenant 54 000 dollars en raison d'une inflation de 8 %.

Le prix a augmenté. Vous avez donc un problème :

Comment allez-vous mettre à jour le nouveau prix d'une maison, étant donné que l'inflation est actuellement de 8 % ?

L'une des réponses à cette question est d'utiliser une méthode pour mettre à jour le prix.

Une méthode est, en termes simples, une fonction à l'intérieur d'une classe. Ce n'est qu'une fonction, mais elle est associée à une classe lorsque nous l'utilisons.

## Méthodes en POO – Correction de l'exemple de prix d'inflation

Nous allons maintenant examiner 3 façons de corriger le prix :

1. Construire une méthode d'instance à l'intérieur de la classe pour corriger le prix
2. Utiliser la méthode de classe pour corriger le prix
3. Utiliser une fonction pour corriger le prix

Toutes ces méthodes effectuent la même opération, mais de manière différente.

### Comment construire une méthode d'instance à l'intérieur de la classe pour corriger le prix

Dans ce premier exemple, nous allons créer une méthode d'instance à l'intérieur de la classe `maison` pour corriger le prix appelée `correctPriceMethod()` :

```python
class maison():

    nom_entreprise = "Entreprise de construction géniale"

    coefficient_inflation = 1.08

    def __init__(self, adresse, etat, alarme, prix):
        self.adresse = adresse
        self.etat = etat
        self.alarme = alarme
        self.prix = prix

    def correctPriceMethod(self):
        self.prix = self.prix * self.coefficient_inflation
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/ray-so-export.png)

Dans ce code, j'ai créé une méthode appelée `correctPriceMethod()` :

```python
    def correctPriceMethod(self):
        self.prix = self.prix * self.coefficient_inflation
```

Ainsi, toutes les maisons créées avec la classe maison auront une méthode pour mettre à jour leurs prix.

Par exemple, supposons que nous avons un appartement avec les informations suivantes :

```
appartement1 = maison(1234, "californie", False , 300000)

appartement1.correctPriceMethod()

print(appartement1.prix)


```

Dans la ligne suivante :

```
 appartement.correctPriceMethod():
```

La méthode met à jour le prix de 300 000 $ à 324 000 $ pour refléter l'inflation.

Voici le même code à nouveau, mais avec deux autres appartements pour montrer deux autres façons de mettre à jour le prix. Regardons la première méthode ici :

```python
class maison():

    nom_entreprise = "Entreprise de construction géniale"

    coefficient_inflation = 1.08

    def __init__(self, adresse, etat, alarme, prix):
        self.adresse = adresse
        self.etat = etat
        self.alarme = alarme
        self.prix = prix

    def correctPriceMethod(self):
        self.prix = self.prix * self.coefficient_inflation
        
#----------------------------------------------------------------

appartement1 = maison(1234, "californie", False , 300000)
appartement2 = maison(1234, "californie", False , 300000)
appartement3Prix = 300000

print(appartement1.prix)

appartement1.correctPriceMethod()
print(appartement1.prix)

>>> 300000
>>> 324000
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2-1.png)

J'ai mis à jour le prix de l'appartement 1 avec la `correctPriceMethod`.

J'ai donc mis à jour le prix avec une méthode dans une instance de classe.

### Comment utiliser la méthode de classe pour corriger le prix

Dans cet exemple, au lieu d'utiliser une méthode d'instance, je vais utiliser une méthode de classe pour corriger l'inflation afin de mettre à jour l'appartement 2.

En d'autres termes, au lieu d'appeler la méthode `appartement1.correctPriceMethod()`, je vais utiliser `maison.correctPriceMethod(appartement2)` :

```
class maison():

    nom_entreprise = "Entreprise de construction géniale"

    coefficient_inflation = 1.08

    def __init__(self, adresse, etat, alarme, prix):
        self.adresse = adresse
        self.etat = etat
        self.alarme = alarme
        self.prix = prix

    def correctPriceMethod(self):
        self.prix = self.prix * self.coefficient_inflation

#-----------------------------------------------------------

appartement1 = maison(1234, "californie", False , 300000)
appartement2 = maison(1234, "californie", False , 300000)
appartement3Prix = 300000

appartement1.correctPriceMethod()

#-----------------------------------------------------------
print(appartement2.prix)

maison.correctPriceMethod(appartement2)
print(appartement2.prix)

>>> 300000
>>> 324000
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/3-1.png)

Cette fois, j'ai mis à jour le prix avec la méthode de classe au lieu de la méthode d'instance.

En d'autres termes, `maison.correctPriceMethod(appartement2)` et `appartement2.correctPriceMethod()` sont la même chose.

La première obtient la méthode de la classe, tandis que la seconde obtient la méthode de l'instance de la classe.

### Comment utiliser une fonction pour corriger le prix

Nous avons donc vu comment mettre à jour le prix avec une méthode d'instance et une méthode de classe.

Dans cet exemple final, nous allons simplement utiliser une fonction pour mettre à jour l'inflation.

Maintenant, je vais mettre à jour le prix pour un troisième appartement, mais cette fois avec une fonction :

```
def correctPricefunction(appartement):
    return appartement * 1.08
```

Ajoutons cela au code :

```
class maison():

    nom_entreprise = "Entreprise de construction géniale"

    coefficient_inflation = 1.08

    def __init__(self, adresse, etat, alarme, prix):
        self.adresse = adresse
        self.etat = etat
        self.alarme = alarme
        self.prix = prix

    def correctPriceMethod(self):
        self.prix = self.prix * self.coefficient_inflation

#-----------------------------------------------------------

appartement1 = maison(1234, "californie", False , 300000)
appartement2 = maison(1234, "californie", False , 300000)
appartement3Prix = 300000

appartement1.correctPriceMethod()

#-----------------------------------------------------------

maison.correctPriceMethod(appartement2)

#-----------------------------------------------------------

def correctPricefunction(appartement):
    return appartement * 1.08

print(appartement3Prix)

appartement3Prix = correctPricefunction(appartement3Prix)
print(appartement3Prix)

>>> 300000
>>> 324000
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/4.png)

Nous faisons la même chose avec juste le prix de l'appartement3 – mais nous utilisons une fonction cette fois.

C'est exact, nous avons la même chose. Il n'y a pas de changement.

Une méthode est simplement une fonction associée à une classe, tandis qu'une fonction est juste une fonction par elle-même.

En utilisant une méthode, vous isolez la fonction qui change les données de la classe au lieu des données qui ne proviennent pas de la classe.

En Python, il y a certains cas où il est [mieux d'utiliser une fonction qu'une méthode](https://stackoverflow.com/questions/8108688/in-python-when-should-i-use-a-function-instead-of-a-method).

## Où aller à partir d'ici ?

Cet article effleure la surface de la programmation orientée objet.

Pour la comprendre pleinement, il est bon d'apprendre la même chose sous différents angles.

Il y a beaucoup de choses que vous pouvez faire pour en savoir plus sur la programmation orientée objet :

1. Vous pouvez plonger et en apprendre davantage avec ce cours YouTube de la chaîne freeCodeCamp :

%[https://www.freecodecamp.org/news/learn-object-oriented-programming-with-python/]

2. Apprenez et écrivez le code réel derrière les 4 piliers principaux de la POO en Python :

* Polymorphisme
* Encapsulation
* Héritage
* Abstraction

3. Appliquez et faites des [projets en POO en Python](https://www.freecodecamp.org/news/python-projects-for-beginners/) et dans un [autre langage de programmation](https://www.freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners/).

4. Plus avancé : Apprenez les principaux [modèles de conception logicielle](https://www.freecodecamp.org/news/the-basic-design-patterns-all-developers-need-to-know/).

## Conclusion

Voici ce que nous avons couvert dans ce tutoriel :

* Ce que sont les classes
* Ce que le mot-clé self est et pourquoi il est facile à comprendre
* Ce que sont les variables de classe
* Différence entre fonctions et méthodes

Vous avez également appris quelques bonnes pratiques à suivre en programmation orientée objet.

Merci d'avoir lu !