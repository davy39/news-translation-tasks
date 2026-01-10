---
title: Python Print sans saut de ligne – Imprimer sur la même ligne
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-10T18:11:21.000Z'
originalURL: https://freecodecamp.org/news/python-print-without-new-line-print-on-the-same-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Copy-of-pip.png
tags:
- name: Python
  slug: python
seo_title: Python Print sans saut de ligne – Imprimer sur la même ligne
seo_desc: "The print function is an important function in Python, as it is used to\
  \ redirect output to the terminal. The output can also be redirected to a file.\
  \ \nThe print function, by default, prints on a new line every time. This is due\
  \ to the definition of p..."
---

La fonction `print` est une fonction importante en Python, car elle est utilisée pour rediriger la sortie vers le terminal. La sortie peut également être redirigée vers un fichier. 

La fonction `print`, par défaut, imprime sur une nouvelle ligne à chaque fois. Cela est dû à la définition de `print()` dans la [documentation](https://docs.python.org/3/library/functions.html#:~:text=print(*objects%2C%20sep%3D%27%20%27%2C%20end%3D%27%5Cn%27%2C%20file%3Dsys.stdout%2C%20flush%3DFalse)) de Python.

## Pourquoi la fonction `print` de Python imprime-t-elle sur une nouvelle ligne par défaut ?

Dans l'extrait ci-dessous, nous pouvons voir que par défaut la valeur de `end` est `\n`. Cela signifie que chaque instruction print se terminerait par un `\n`. Notez que `\n` représente un caractère de saut de ligne.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-22.png)
_Source : [documentation](https://docs.python.org/3/library/functions.html#:~:text=print(*objects%2C%20sep%3D%27%20%27%2C%20end%3D%27%5Cn%27%2C%20file%3Dsys.stdout%2C%20flush%3DFalse)) de Python._

Voyons un exemple de la fonction print.

**Exemple de code :**

```
# utilisation de Print avec les paramètres par défaut

print("This will be printed")
print("in separate lines")
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-23.png)

Dans l'exemple ci-dessus, les lignes seraient imprimées séparément en raison de la définition : `end='\n'`.

## Comment imprimer sur la même ligne en Python

Parfois, nous avons besoin d'imprimer des chaînes sur la même ligne. C'est particulièrement utile lorsque nous lisons des fichiers en Python. Lorsque nous lisons des fichiers, nous obtenons un espace vide entre les lignes par défaut.

Voyons un exemple. Nous avons un fichier nommé `rainbow.txt` dont le contenu est illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-41.png)
_Contenu du fichier rainbow.txt_

**Code :**

```
fhand = open('rainbow.txt')
for line in fhand:
  print(line)

```

Dans le code ci-dessus, nous avons utilisé un gestionnaire de fichier `fhand` pour accéder au fichier. Ensuite, nous parcourons les lignes à l'aide d'une boucle `for`.

**Sortie :**

Lorsque nous imprimons le contenu, les résultats ressemblent à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-42.png)

La ligne vide supplémentaire est due à la présence de `\n` à la fin de chaque ligne du fichier, ce qui déplace le curseur vers la ligne suivante. Enfin, la ligne vide est ajoutée en raison du comportement de la fonction `print` comme nous l'avons vu dans la section précédente.

Disons que nous voulons les supprimer. Pour ce faire, nous pouvons apporter quelques modifications. Pour cela, nous devons changer le comportement par défaut de `print`. Nous verrons comment faire cela en détail dans les sections suivantes.

### Option #1 – Comment modifier la valeur de `end` dans une fonction `print`

Personnalisons la valeur de `end` dans la fonction `print`. Nous allons la définir sur `' '` qui est un espace.

**Exemple de code :**

```
# Personnalisation de la valeur de 'end'

print("This is string 1 same line", end=' ')
print("This is string 2 different line")

```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-32.png)

Maintenant, nous pouvons voir qu'au lieu d'une nouvelle ligne `(\n)`, nous disons à la fonction print d'ajouter un caractère d'espace à la fin.

Nous pouvons également fournir un autre caractère au lieu d'un espace comme ceci :

```
# Personnalisation de la valeur de 'end' avec un séparateur personnalisé

print("This is string 1 same line", end=';')
print("This is string 2 different line")

```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-33.png)

_Utilisation :_ L'exemple ci-dessus est juste une façon d'imprimer sur la même ligne avec le caractère de séparation de votre choix.

Voyons un autre exemple. Nous pouvons parcourir une liste d'éléments et les imprimer sur la même ligne avec `end = ' '` .

```
# itération de listes

list_fruits = ['red','blue', 'green', 'orange']  
for i in list_fruits:  
    print(i, end = ' ')  
    
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-34.png)

### Option #2 – Supprimer les espaces blancs en utilisant `rstrip()` dans les fichiers

Nous pouvons supprimer certains caractères autour d'une chaîne en utilisant `strip()`. Par défaut, chaque ligne d'un fichier a `"\n"` à la fin. Comme nous ne sommes concernés que par le caractère à droite, nous utiliserons `rstrip()` qui signifie "right-strip". Nous verrons un exemple de `rstrip()` ensuite.

Vous pouvez en savoir plus sur la méthode `strip()` dans cet [article](https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/) de blog.

## Retour à notre exemple d'impression de fichier

Rappelez-vous, nous avons discuté d'un exemple d'impression de fichier où des lignes supplémentaires étaient imprimées :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-43.png)

Modifions un peu le code en utilisant `rstrip()`.

```
print("1. Removing extra blank line")

fhand = open('rainbow.txt')
for line in fhand:
  line=line.rstrip()
  print(line)

print("\n")

print("2. Printing all in the same line")
fhand = open('rainbow.txt')
for line in fhand:
  line=line.rstrip("\n")
  print(line, end = ' ')


```

#### Sortie

Tout d'abord, nous avons supprimé l'espace blanc supplémentaire avec `rstrip()`. Dans l'étape suivante, nous avons à nouveau supprimé la ligne de fin avec `rstrip("\n")` et `end=' '` pour obtenir la sortie sur une seule ligne.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-48.png)

## Conclusion

Nous avons vu comment nous pouvons imprimer en Python sans saut de ligne. Nous avons également vu comment nous pouvons imprimer des lignes dans un fichier sans lignes de fin supplémentaires. J'espère que vous avez trouvé ce tutoriel utile.

Partagez vos réflexions avec moi sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).