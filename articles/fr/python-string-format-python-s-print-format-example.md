---
title: Formatage de chaînes Python – Exemple de format d'impression S Python
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-07T23:20:34.000Z'
originalURL: https://freecodecamp.org/news/python-string-format-python-s-print-format-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/federico-burgalassi-t2zKLI9MQnw-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Formatage de chaînes Python – Exemple de format d'impression S Python
seo_desc: "In Python, you have a few options to format your strings. In this article,\
  \ I will go over str.format(), formatted string literals, and template strings.\
  \ \nBut first, let's take a look at what is considered to be the \"old way\" of\
  \ formatting strings. \nW..."
---

En Python, vous avez plusieurs options pour formater vos chaînes de caractères. Dans cet article, je vais passer en revue `str.format()`, les littéraux de chaîne formatés et les chaînes de modèle. 

Mais d'abord, examinons ce qui est considéré comme l'« ancienne méthode » de formatage des chaînes de caractères. 

## Qu'est-ce que le formatage de chaînes % en Python ? 

L'une des anciennes méthodes pour formater des chaînes en Python consistait à utiliser l'opérateur `%`. 

Voici la syntaxe de base :

```py
"Ceci est une chaîne %s" % "valeur de la chaîne ici"
```

Vous pouvez créer des chaînes et utiliser `%s` à l'intérieur de cette chaîne qui agit comme un espace réservé. Ensuite, vous pouvez écrire `%` suivi de la valeur réelle de la chaîne que vous souhaitez utiliser. 

Voici un exemple de base utilisant le formatage de chaînes `%`.

```py
print("Salut, mon nom est %s" % "Jessica")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-10.31.53-PM.png)

Cette méthode est souvent appelée l'« ancienne » méthode car Python 3 a introduit `str.format()` ainsi que les littéraux de chaîne formatés. 

## Qu'est-ce que la méthode `str.format()` en Python ?

Voici la syntaxe de base pour la méthode `str.format()` :

```py
"chaîne de modèle {}".format(arguments)
```

À l'intérieur de la chaîne de modèle, nous pouvons utiliser `{}` qui agissent comme des espaces réservés pour les arguments. Les arguments sont des valeurs qui seront affichées dans la chaîne. 

Dans cet exemple, nous voulons imprimer `"Bonjour, mon nom est Jessica. Je suis une musicienne devenue programmeuse."` 

Dans la chaîne, nous allons avoir un total de trois `{}` qui serviront d'espaces réservés pour les valeurs de Jessica, musicienne et programmeuse. Ce sont ce qu'on appelle des champs de format. 

```py
"Bonjour, mon nom est {}. Je suis une {} devenue {}."
```

À l'intérieur de ces parenthèses pour `str.format()`, nous allons utiliser les valeurs "Jessica", "musicienne" et "programmeuse". 

```py
.format("Jessica", "musicienne", "programmeuse")
```

Voici le code complet et la phrase imprimée :

```py
print("Bonjour, mon nom est {}. Je suis une {} devenue {}.".format("Jessica", "musicienne", "programmeuse"))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-10.32.14-PM.png)

### Arguments positionnels 

Vous pouvez accéder à la valeur de ces arguments en utilisant un numéro d'index à l'intérieur des `{}`.

Dans cet exemple, nous avons deux arguments `"trompette"` et `"batterie"` à l'intérieur du `.format()`. 

```py
.format("trompette", "batterie")
```

Nous pouvons accéder à ces valeurs à l'intérieur de la chaîne en faisant référence aux numéros d'index. `{0}` fait référence au premier argument `"trompette"` et `{1}` fait référence au deuxième argument `"batterie"`.

```py
"Steve joue de {0} et de {1}."
```

Voici le code complet et la phrase imprimée :

```py
print("Steve joue de {0} et de {1}.".format("trompette", "batterie"))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-11.04.33-PM.png)

Nous pouvons modifier cet exemple et échanger les numéros d'index dans la chaîne. Vous remarquerez que la phrase a changé et que le placement des arguments est inversé. 

```py
print("Steve joue de {1} et de {0}.".format("trompette", "batterie"))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-11.06.17-PM.png)

### Arguments de mots-clés

Ces arguments se composent d'une paire `clé` `valeur`. Nous pouvons accéder à la `valeur` de l'argument en utilisant la `clé` à l'intérieur des `{}`.

Dans cet exemple, nous avons deux clés appelées `organisation` et `adjectif`. Nous allons utiliser ces clés à l'intérieur de la chaîne.

```py
"{organisation} est {adjectif} !"
```

À l'intérieur du `.format()`, nous avons les paires `clé` `valeur`.

```py
.format(organisation="freeCodeCamp", adjectif="génial")
```

Voici le code complet et la phrase imprimée. 

```py
print("{organisation} est {adjectif} !".format(organisation="freeCodeCamp", adjectif="génial"))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-11.44.14-PM.png)

### Comment mélanger les arguments de mots-clés et positionnels

Dans `str.format()`, vous pouvez mélanger les arguments de mots-clés et positionnels.

Dans cet exemple, nous allons créer une courte histoire sur une visite à Disneyland.

Nous allons d'abord créer quelques variables pour le nom, le nombre, l'adjectif et une attraction de Disneyland.

```py
nom = "Sam"
adjectif = "incroyable"
nombre = 200
attraction_disney = "Space Mountain"
```

Nous voulons ensuite créer notre chaîne en utilisant des arguments de mots-clés et positionnels. Je vais ajouter `\n` pour indiquer à l'ordinateur de créer une nouvelle ligne après chaque phrase.

```py
"Je suis allé à {0} avec {nom}.\nC'était {adjectif}.\nNous avons attendu {heures} heures pour monter sur {attraction}."
```

À l'intérieur des parenthèses pour `str.format()`, nous allons assigner nos variables aux clés `nom`, `adjectif`, `heures` et `attraction_disney`. `{0}` aura la valeur `"Disneyland"`.

```py
.format("Disneyland", nom=nom, adjectif=adjectif, heures=nombre, attraction=attraction_disney)
```

Voici le code complet et la phrase imprimée :

```py
nom = "Sam"
adjectif = "incroyable"
nombre = 200
attraction_disney = "Space Mountain"

print("Je suis allé à {0} avec {nom}.\nC'était {adjectif}.\nNous avons attendu {heures} heures pour monter sur {attraction}."
      .format("Disneyland", nom=nom, adjectif=adjectif, heures=nombre, attraction=attraction_disney))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-04-at-12.20.41-AM.png)

## Qu'est-ce que les littéraux de chaîne formatés ? 

Les littéraux de chaîne formatés (ou f-strings) vous permettent d'inclure des expressions à l'intérieur de vos chaînes. Juste avant la chaîne, vous placez un `f` ou `F` qui indique à l'ordinateur que vous souhaitez utiliser une `f-string`. 

Voici la syntaxe de base :

```py
variable = "une valeur"
f"ceci est une chaîne {variable}"
```

Voici un exemple de base qui imprime la phrase `Maria et Jessica sont amies depuis l'école primaire.`

```py
nom = "Jessica"
print(f"Maria et {nom} sont amies depuis l'école primaire.")
```

Cela fonctionne de la même manière si j'utilise un `F` majuscule avant la chaîne.

```py
nom = "Jessica"
print(F"Maria et {nom} sont amies depuis l'école primaire.")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-6.21.48-PM.png)

Vous pouvez également utiliser une `f-string` pour formater les données d'un dictionnaire.

Dans cet exemple, nous avons un dictionnaire qui représente les classements des meilleures équipes de basket-ball universitaire masculin et le nombre de matchs qu'elles ont gagnés sur 32.

```py
classements = {"Gonzaga": 31, "Baylor": 28, "Michigan": 25, "Illinois": 24, "Houston": 21}

```

Nous pouvons utiliser une boucle `for` et la méthode `items()` pour parcourir chaque paire `clé valeur` du dictionnaire `classements`.

```py
for équipe, score in classements.items():

```

À l'intérieur de la boucle `for`, nous pouvons utiliser une `f-string` pour formater les résultats imprimés.

L'utilisation du `:` pour `{équipe:10}` et `{score:10d}` indique à l'ordinateur de créer un champ de 10 caractères de large. Cela créera des colonnes uniformes pour les données.

Le `d` à l'intérieur de `{score:10d}` fait référence à un entier décimal.

```py
 print(f"{équipe:10} ==> {score:10d}")
```

Voici le code complet et la sortie imprimée :

```py
classements = {"Gonzaga": 31, "Baylor": 28, "Michigan": 25, "Illinois": 24, "Houston": 21}

for équipe, score in classements.items():
    print(f"{équipe:10} ==> {score:10d}")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-9.48.53-PM.png)

## Qu'est-ce que les chaînes de modèle ?

Les chaînes de modèle sont des chaînes Python qui utilisent des espaces réservés pour les valeurs réelles.

Voici la syntaxe de base :

```py
Template("$espace_réservé").substitute(espace_réservé="valeur réelle")
```

Examinons un exemple pour mieux comprendre comment cela fonctionne.

Dans cet exemple, nous voulons imprimer `J'adore apprendre avec freeCodeCamp !` en utilisant des chaînes de modèle.

Pour utiliser des chaînes de modèle, vous devez d'abord importer la classe `Template` de la bibliothèque standard.

```py
from string import Template

```

Vous pouvez ensuite utiliser la classe `Template` et fournir une chaîne à l'intérieur des parenthèses. Nous allons placer un `$` devant `nom` qui sera remplacé plus tard par la valeur réelle.

```py
Template("J'adore apprendre avec $nom !")
```

Nous ajoutons ensuite `.substitute` au modèle et assignons la valeur `freeCodeCamp` à `nom`.

```py
.substitute(nom="freeCodeCamp")
```

Voici le code complet et la sortie imprimée :

```py
from string import Template

print(Template("J'adore apprendre avec $nom !").substitute(nom="freeCodeCamp"))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-10.11.27-PM.png)

## Conclusion

Il existe de nombreuses façons de formater vos chaînes en Python.

L'ancienne méthode de formatage de vos chaînes consisterait à utiliser l'opérateur `%`.

```py
"Ceci est une chaîne %s" % "valeur de la chaîne ici"

```

`%s` agit comme un espace réservé pour la valeur réelle. Vous placez la valeur réelle après l'opérateur `%`.

Cette méthode est souvent appelée l'« ancienne » méthode car Python 3 a introduit `str.format()` et les littéraux de chaîne formatés (f-strings).

Dans la méthode `str.format()`, vous utilisez `{}` pour les espaces réservés et placez les valeurs réelles à l'intérieur des parenthèses. Cette méthode peut prendre des arguments positionnels et de mots-clés.

```py
"chaîne de modèle {}".format(arguments)
```

Les littéraux de chaîne formatés (ou f-strings) vous permettent d'inclure des expressions à l'intérieur de vos chaînes. Juste avant la chaîne, vous placez un `f` ou `F` qui indique à l'ordinateur que vous souhaitez utiliser une `f-string`.

```py
variable = "une valeur"
f"ceci est une chaîne {variable}"
```

Vous pouvez également utiliser des chaînes de modèle en important la classe `Template` de la bibliothèque standard. Les chaînes de modèle sont des chaînes Python qui utilisent des espaces réservés pour les valeurs réelles.

```py
Template("$espace_réservé").substitute(espace_réservé="valeur réelle")
```

J'espère que vous avez trouvé cet article utile et je vous souhaite bonne chance dans votre parcours Python.