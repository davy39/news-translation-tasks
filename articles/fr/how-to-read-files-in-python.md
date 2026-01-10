---
title: Python Lire un Fichier – Comment Ouvrir, Lire et Écrire dans des Fichiers en
  Python
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-05-31T14:29:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-files-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/read-write-files-python--1-.png
tags:
- name: Python
  slug: python
seo_title: Python Lire un Fichier – Comment Ouvrir, Lire et Écrire dans des Fichiers
  en Python
seo_desc: 'Reading and writing files is a common operation when working with any programming
  language. You can program your code to read data or instructions from a file and
  then write the data as well. This increases efficiency and reduces manual effort.

  Pytho...'
---

La lecture et l'écriture de fichiers sont des opérations courantes lors de l'utilisation de n'importe quel langage de programmation. Vous pouvez programmer votre code pour lire des données ou des instructions à partir d'un fichier, puis écrire les données également. Cela augmente l'efficacité et réduit l'effort manuel.

Python dispose d'une méthodologie bien définie pour ouvrir, lire et écrire des fichiers. Certaines applications de la manipulation de fichiers en Python incluent : la lecture de données pour l'entraînement et le test d'algorithmes, la lecture de fichiers pour créer de l'art génératif, la génération de rapports et la lecture de fichiers de configuration.

Dans ce tutoriel, vous apprendrez :

1. Comment charger des fichiers dans la mémoire principale et créer un gestionnaire de fichier.
2. Comment utiliser le gestionnaire de fichier pour ouvrir des fichiers en lecture et en écriture.
3. La gestion des exceptions lors de la manipulation de fichiers.

Prérequis :

* Assurez-vous d'avoir la dernière version de Python installée.
* Familiarité avec un éditeur de texte compatible avec Python de votre choix.
* Une certaine familiarité avec la syntaxe de base de Python.

Pour un accès rapide à un IDE Python, consultez [Replit](https://replit.com/~). Vous pouvez également cloner [ce](https://github.com/zairahira/read-files-python) dépôt et l'exécuter sur Replit.

## Persistance et Comment Charger des Fichiers dans la Mémoire Principale

Les fichiers résident dans la mémoire secondaire de l'ordinateur. La mémoire secondaire est persistante, ce qui signifie que les données ne sont pas effacées lorsque l'ordinateur est éteint. Une fois que vous apportez des modifications à un fichier et que vous l'enregistrez, les modifications sont écrites et enregistrées de manière permanente dans la mémoire secondaire.

Pour travailler avec des fichiers, nous devons d'abord les charger dans la mémoire principale. La mémoire principale est la mémoire cache temporaire qui contient les données demandées pendant un bref intervalle. Les données sont perdues lorsque l'ordinateur est éteint.

![Les fichiers sont chargés de la mémoire secondaire vers la mémoire principale, puis traités par le CPU. Une fois le traitement terminé, les données sont réécrites dans la mémoire secondaire.](https://www.freecodecamp.org/news/content/images/2022/05/image-175.png)
*Les fichiers sont chargés de la mémoire secondaire vers la mémoire principale, puis traités par le CPU. Une fois le traitement terminé, les données sont réécrites dans la mémoire secondaire.*

Python interagit avec les fichiers chargés dans la mémoire principale via des "**gestionnaires de fichiers**". Examinons les gestionnaires de fichiers en détail.

### Comment Fonctionnent les Gestionnaires de Fichiers

Lorsque nous voulons lire ou écrire un fichier, nous devons d'abord l'_ouvrir_. L'ouverture d'un fichier signale au système d'exploitation de rechercher le fichier par son nom et de s'assurer qu'il existe.

Le système d'exploitation retourne un gestionnaire de fichier si l'_ouverture_ est réussie. Ensuite, nous pouvons interagir avec notre fichier via le gestionnaire de fichier.

Le gestionnaire de fichier ne contient pas les données elles-mêmes, il fournit simplement une interface pour gérer les opérations sur le fichier.

![Un gestionnaire de fichier fournit à votre programme l'accès aux données dans la mémoire secondaire.](https://www.freecodecamp.org/news/content/images/2022/05/image-176.png)
*Un gestionnaire de fichier fournit à votre programme l'accès aux données dans la mémoire secondaire.*

### Comment Ouvrir un Fichier

Dans cet exemple, nous allons ouvrir le fichier `daffodils.txt`. Notez que ce fichier doit être stocké dans le même dossier que votre programme Python. Vous pouvez télécharger le fichier `daffodils.txt` depuis [ce](https://github.com/zairahira/read-files-python/blob/main/daffodils.txt) lien GitHub.

Jetez un coup d'œil au fichier, car nous travaillerons avec son contenu dans nos prochains exemples.

**Exemple :**

```python
fhand = open('daffodils.txt')
print(fhand)
```

Dans l'exemple ci-dessus, le système d'exploitation retournera le gestionnaire de fichier dans la variable `fhand` si l'_ouverture_ est réussie. Par défaut, vous ne pouvez que lire le fichier.

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-177.png)
*La sortie d'un gestionnaire de fichier.*

Dans la sortie, nous avons reçu un gestionnaire de fichier où `name` est le nom du fichier et `mode` est la permission qui est `r` (pour `read`) dans notre cas. `encoding` est le mécanisme d'encodage pour le jeu de caractères Unicode. Vous pouvez en apprendre plus sur l'UTF-8 [ici](https://www.freecodecamp.org/news/what-is-utf-8-character-encoding/).

**Exception :**

Si le fichier n'existe pas, nous obtenons une exception comme celle-ci :

![Exception lorsque le fichier n'est pas trouvé.](https://www.freecodecamp.org/news/content/images/2022/05/image-178.png)
*Exception lorsque le fichier n'est pas trouvé.*

### Comment Imprimer le Fichier

Maintenant que nous avons le gestionnaire de fichier, cela signifie que nous pouvons accéder au fichier. Imprimons le fichier et voyons son contenu.

**Exemple :**

```python
# Obtenir le gestionnaire de fichier
fhand = open('daffodils.txt')

# Parcourir chaque ligne via le gestionnaire de fichier
for line in fhand:
  print(line) 

```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-179.png)
*Impression du contenu d'un fichier.*

Nous sommes en mesure d'accéder et d'imprimer le fichier avec succès. Mais, avez-vous remarqué que nous obtenons des lignes vides supplémentaires entre chaque ligne ? Il y a une explication à cela. Voyons cela dans la section suivante.

### Comment Gérer les Espaces de Ligne Supplémentaires

Le caractère de nouvelle ligne est représenté en Python par `\n`. Ce caractère ajoute une nouvelle ligne lorsqu'il est placé n'importe où dans une chaîne.

Il y a un caractère de nouvelle ligne à la fin de chaque ligne qui imprime la sortie à la ligne suivante. Nous pouvons le visualiser en utilisant la méthode `repr`.

Selon la [documentation](https://docs.python.org/3/library/functions.html#repr) de Python, la méthode `repr()` retourne une chaîne contenant une représentation imprimable d'un objet. Cela signifie que nous pouvons voir n'importe quel caractère spécial comme un `\t` ou un `\n` qui apparaît dans une chaîne.

Exécutons un exemple ci-dessous et voyons la sortie.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-180.png)
*Représentation des chaînes en utilisant `repr()`.*

**Exemple :**

Revenons à notre fichier, nous pouvons utiliser `repr()` pour vérifier les caractères spéciaux.

```python
# Obtenir le gestionnaire de fichier
fhand = open('daffodils.txt')

# Parcourir chaque ligne via le gestionnaire de fichier
for line in fhand:
  print(repr(line)) 

```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-181.png)
*Ici, nous pouvons voir ce qui se passe en coulisses.*

De plus, la méthode print ajoute une nouvelle ligne par défaut. Cela signifie qu'en utilisant print, nous obtenons une autre nouvelle ligne dans la sortie. Nous pouvons gérer cette ligne supplémentaire en utilisant deux approches.

#### Approche #1 : Changer la valeur par défaut de fin de print

L'extrait ci-dessous montre les arguments de la fonction `print`. Nous pouvons voir que par défaut la valeur de `end` est `\n`. Cela signifie que chaque instruction print se terminera par un `\n`.

![image-22](https://www.freecodecamp.org/news/content/images/2022/03/image-22.png)
*Source : Documentation [Python](https://docs.python.org/3/library/functions.html#:~:text=print(*objects%2C%20sep%3D%27%20%27%2C%20end%3D%27%5Cn%27%2C%20file%3Dsys.stdout%2C%20flush%3DFalse)).*

Nous pouvons changer la valeur par défaut `end='\n'` en une valeur vide afin de ne pas obtenir de nouvelle ligne à la fin de chaque ligne. Voyons l'exemple ci-dessous pour mieux comprendre.

```python
# Par défaut, la sortie irait sur des lignes séparées
print("Hello")
print("World")

# Imprimer sur la même ligne car end = ' '
# ajouté un espace unique
print("Hello", end = ' ') 
print("World")

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-182.png)
*Imprimer sur la même ligne et des lignes différentes en utilisant `print()`.*

Revenons à notre fichier principal, modifions un peu le code pour obtenir la sortie sans lignes vides supplémentaires.

```python
# Obtenir le gestionnaire de fichier
fhand = open('daffodils.txt')

# Parcourir chaque ligne et modifier la valeur par défaut de 'end'
for line in fhand:
  print(line, end = '')
```

**Sortie :**

Et voici notre sortie souhaitée !

![Imprimer sans lignes supplémentaires en utilisant print().](https://www.freecodecamp.org/news/content/images/2022/05/image-183.png)
*Imprimer sans lignes supplémentaires en utilisant `print()`.*

#### Approche #2 : Utiliser la méthode rstrip()

Nous pouvons supprimer certains caractères autour d'une chaîne en utilisant la méthode `strip()`.

Maintenant, nous savons que par défaut, chaque ligne d'un fichier a `"\n"` à la fin. Comme nous nous intéressons uniquement au caractère à droite, nous utiliserons `rstrip()` qui signifie right-strip. Nous discuterons d'un exemple de `rstrip()` ensuite.

Vous pouvez en apprendre plus sur la méthode `strip()` dans cet article de blog [post](https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/).

```python
# Obtenir le gestionnaire de fichier
fhand = open('daffodils.txt')

# Parcourir chaque ligne et supprimer le caractère de ligne supplémentaire avec rstrip()
for line in fhand:
  line = line.rstrip()
  print(line)

```

Sortie :

![Imprimer sans lignes supplémentaires en utilisant rstrip().](https://www.freecodecamp.org/news/content/images/2022/05/image-184.png)
*Imprimer sans lignes supplémentaires en utilisant rstrip`()`.*

### Comment Laisser l'Utilisateur Choisir un Fichier

Au lieu de coder en dur un nom de fichier, nous pouvons rendre le code dynamique en laissant l'utilisateur choisir un fichier.

Demandons à l'utilisateur d'entrer un nom de fichier. Ensuite, nous calculerons le nombre de lignes dans le fichier.

**Exemple :**

```python
fname = input('Entrez le nom du fichier : ')
fhand = open(fname)
count = 0
for line in fhand:
     count = count + 1
print('Il y a', count, 'lignes dans', fname)
```

**Sortie :**

![Demander à l'utilisateur d'entrer le nom du fichier.](https://www.freecodecamp.org/news/content/images/2022/05/image-186.png)
*Demander à l'utilisateur d'entrer le nom du fichier.*

### Comment Écrire dans un Fichier en Python

Par défaut, le gestionnaire de fichier ouvre un fichier en mode lecture. Nous pouvons écrire dans un fichier si nous ouvrons le fichier avec l'un des modes suivants :

* `w`- (Écrire) écrit dans un fichier existant mais efface le contenu existant.
* `a`- (Ajouter) ajoute à un fichier existant.
* `x` - (Créer) crée un fichier et retourne une erreur si le fichier existe.

#### Comment écrire dans un fichier

Notez que si nous essayons d'ouvrir un fichier déjà existant avec le drapeau `w`, le contenu est écrasé.

```
# Ouvrir le fichier avec le mode 'w'
fout = open('flower.txt', 'w')
fout.write("Ce contenu sera ajouté et le contenu existant sera supprimé")
fout.close()


```

#### Comment ajouter à un fichier

Le drapeau `a` ajoute au contenu existant et préserve le contenu existant.

```
# Ouvrir le fichier avec le mode 'a'
fout = open('flower.txt', 'a')
fout.write("Maintenant le fichier a plus de contenu à la fin !")
fout.close()


```

#### Comment créer un fichier et écrire dedans

Le mode `x` crée un fichier et ajoute du contenu. 

```
# Ouvrir le fichier avec le mode 'x'
fout = open('new-file.txt', 'x')
fout.write("Maintenant le nouveau fichier a du contenu !")
fout.close()


```

Si le fichier existe, nous obtiendrons une exception comme celle-ci : 

```
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    fout = open('flower.txt', 'x')
FileExistsError: [Errno 17] File exists: 'flower.txt'
```

### Gestion des Exceptions

Il est possible que le fichier que nous demandons n'existe pas. Cela fait planter le programme en raison de l'exception :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-189.png)

Afin de rendre le programme plus convivial, nous pouvons gérer cette exception dans un bloc `try-except`.

La partie risquée du programme qui est susceptible de planter est écrite dans un bloc `try`. Si le code s'exécute sans exception, le bloc `except` est ignoré et le programme continue à s'exécuter. Si une exception est trouvée, le bloc `except` s'exécute et ferme le programme proprement avec la commande `exit`.

```python
fname = input('Entrez le nom du fichier : ')
try:
  fhand = open(fname)
except:
  print('Fichier non trouvé et ne peut pas être ouvert :', fname)
  exit()
count=0
for line in fhand:
  count = count + 1
print('Il y a', count, 'lignes dans', fname)
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-188.png)
*Gestion des exceptions en utilisant un bloc try-except.*

## Conclusion

Savoir comment travailler avec des fichiers est un concept essentiel en programmation. Dans ce tutoriel, vous avez appris comment ouvrir des fichiers pour la lecture et l'écriture en Python en utilisant des gestionnaires de fichiers.

Pour référence, j'ai inclus tous les extraits de code et les fichiers d'exemple dans [ce](https://github.com/zairahira/read-files-python) dépôt GitHub.

J'espère que vous avez trouvé ce tutoriel utile.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez également lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Crédits de la bannière :

* [Vecteur Php créé par svstudioart - www.freepik.com](https://www.freepik.com/vectors/php)
* [Vecteur de thème de site web créé par freepik - www.freepik.com](https://www.freepik.com/vectors/website-theme)