---
title: Guide de manipulation des chaînes Python – Apprenez à manipuler les chaînes
  Python pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T22:52:42.000Z'
originalURL: https://freecodecamp.org/news/python-string-manipulation-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-from-2021-03-22-15-59-14.png
tags:
- name: Python
  slug: python
seo_title: Guide de manipulation des chaînes Python – Apprenez à manipuler les chaînes
  Python pour débutants
seo_desc: "By Renan Moura Ferreira\nString manipulation is one of those activities\
  \ in programming that we, as programmers, do all the time.  \nIn many programming\
  \ languages, you have to do a lot of the heavy lifting by yourself.  \nIn Python,\
  \ on the other hand, yo..."
---

Par Renan Moura Ferreira

La manipulation de chaînes est l'une de ces activités en programmation que nous, en tant que programmeurs, faisons tout le temps. 

Dans de nombreux langages de programmation, vous devez faire beaucoup de travail vous-même. 

En Python, en revanche, vous avez plusieurs fonctions intégrées dans la bibliothèque standard pour vous aider à manipuler les chaînes de nombreuses manières différentes. 

Dans cet article, je vais vous montrer comment travailler avec des chaînes spécifiquement ainsi que quelques astuces sympas. 

Info rapide : [Vous pouvez télécharger une version PDF de ce Guide de manipulation des chaînes Python ici](https://renanmf.com/python-string-manipulation-handbook/). 

Prêt à plonger ?

## Table des matières

1. [Bases des chaînes Python](#heading-installation)
2. [Comment diviser une chaîne en Python](#heading-comment-diviser-une-chaine-en-python)
3. [Comment supprimer tous les espaces blancs dans une chaîne en Python](#heading-comment-supprimer-tous-les-espaces-blancs-dans-une-chaine-en-python)
4. [Comment gérer les chaînes multilingues en Python](#heading-comment-gerer-les-chaines-multilingues-en-python)
5. [lstrip() : Comment supprimer les espaces et les caractères du début d'une chaîne en Python](#heading-lstrip-comment-supprimer-les-espaces-et-les-caracteres-du-debut-dune-chaine-en-python)
6. [rstrip() : Comment supprimer les espaces et les caractères de la fin d'une chaîne en Python](#heading-rstrip-comment-supprimer-les-espaces-et-les-caracteres-de-la-fin-dune-chaine-en-python)
7. [strip() : Comment supprimer les espaces et les caractères du début et de la fin d'une chaîne en Python](#heading-strip-comment-supprimer-les-espaces-et-les-caracteres-du-debut-et-de-la-fin-dune-chaine-en-python)
8. [Comment mettre une chaîne entière en minuscules en Python](#heading-comment-mettre-une-chaine-entiere-en-minuscules-en-python)
9. [Comment mettre une chaîne entière en majuscules en Python](#heading-comment-mettre-une-chaine-entiere-en-majuscules-en-python)
10. [Comment utiliser la casse de titre en Python](#heading-comment-utiliser-la-casse-de-titre-en-python)
11. [Comment utiliser la casse d'échange en Python](#heading-comment-utiliser-la-casse-dechange-en-python)
12. [Comment vérifier si une chaîne est vide en Python](#heading-comment-verifier-si-une-chaine-est-vide-en-python)
13. [rjust() : Comment justifier à droite une chaîne en Python](#heading-rjust-comment-justifier-a-droite-une-chaine-en-python)
14. [ljust() : Comment justifier à gauche une chaîne en Python](#heading-ljust-comment-justifier-a-gauche-une-chaine-en-python)
15. [isalnum() : Comment vérifier les caractères alphanumériques uniquement dans une chaîne en Python](#heading-isalnum-comment-verifier-les-caracteres-alphanumeriques-uniquement-dans-une-chaine-en-python)
16. [isprintable() : Comment vérifier les caractères imprimables dans une chaîne en Python](#isprintableverificationcaracteresimprimablesdanschaineenpython)
17. [isspace() : Comment vérifier les espaces blancs uniquement dans une chaîne en Python](#heading-isspace-comment-verifier-les-espaces-blancs-uniquement-dans-une-chaine-en-python)
18. [startswith() : Comment vérifier si une chaîne commence par une certaine valeur en Python](#heading-startswith-comment-verifier-si-une-chaine-commence-par-une-certaine-valeur-en-python)
19. [capitalize() : Comment définir uniquement le premier caractère en majuscule dans une chaîne en Python](#heading-capitalize-comment-definir-uniquement-le-premier-caractere-en-majuscule-dans-une-chaine-en-python)
20. [isupper() : Comment vérifier les majuscules uniquement dans une chaîne en Python](#heading-isupper-comment-verifier-les-majuscules-uniquement-dans-une-chaine-en-python)
21. [join() : Comment joindre les éléments d'un itérable en une seule chaîne en Python](#heading-join-comment-joindre-les-elements-dun-iterable-en-une-seule-chaine-en-python)
22. [splitlines() : Comment diviser une chaîne aux sauts de ligne en Python](#heading-splitlines-comment-diviser-une-chaine-aux-sauts-de-ligne-en-python)
23. [islower() : Comment vérifier les minuscules uniquement dans une chaîne en Python](#heading-islower-comment-verifier-les-minuscules-uniquement-dans-une-chaine-en-python)
24. [isnumeric() : Comment vérifier les numériques uniquement dans une chaîne en Python](#heading-isnumeric-comment-verifier-les-numeriques-uniquement-dans-une-chaine-en-python)
25. [isdigit() : Comment vérifier les chiffres uniquement dans une chaîne en Python](#heading-isdigit-comment-verifier-les-chiffres-uniquement-dans-une-chaine-en-python)
26. [isdecimal() : Comment vérifier les décimaux uniquement dans une chaîne en Python](#heading-isdecimal-comment-verifier-les-decimaux-uniquement-dans-une-chaine-en-python)
27. [isalpha() : Comment vérifier les lettres uniquement dans une chaîne en Python](#isalphaverificationlettresuniquementdanschaineenpython)
28. [istitle() : Comment vérifier si chaque mot commence par un caractère en majuscule dans une chaîne en Python](#heading-istitle-comment-verifier-si-chaque-mot-commence-par-un-caractere-en-majuscule-dans-une-chaine-en-python)
29. [expandtabs() : Comment définir le nombre d'espaces pour une tabulation dans une chaîne en Python](#heading-expandtabs-comment-definir-le-nombre-despaces-pour-une-tabulation-dans-une-chaine-en-python)
30. [center() : Comment centrer une chaîne en Python](#heading-center-comment-centrer-une-chaine-en-python)
31. [zfill() : Comment ajouter des zéros à une chaîne en Python](#heading-zfill-comment-ajouter-des-zeros-a-une-chaine-en-python)
32. [find() : Comment vérifier si une chaîne contient une certaine sous-chaîne en Python](#findverificationcommentverifiersichainecontientcertainesouschaineenpython)
33. [Comment supprimer un préfixe ou un suffixe dans une chaîne en Python](#heading-comment-supprimer-un-prefixe-ou-un-suffixe-dans-une-chaine-en-python)
34. [lstrip() vs removeprefix() et rstrip() vs removesuffix()](#heading-lstrip-vs-removeprefix-et-rstrip-vs-removesuffix)
35. [Comment fonctionne le découpage en Python](#heading-comment-fonctionne-le-decoupage-en-python)
36. [Comment inverser une chaîne en Python](#heading-comment-inverser-une-chaine-en-python)
37. [Conclusion](#heading-conclusion)

## Bases des chaînes Python

Le type `text` est l'un des types les plus courants et est souvent appelé _string_ ou, en Python, simplement `str`.

```python
my_city = "New York"
print(type(my_city))

#Les guillemets simples ont exactement
#la même utilisation que les guillemets doubles
my_city = 'New York'
print(type(my_city))

#Définir explicitement le type de variable
my_city = str("New York")
print(type(my_city))
```

```
<class 'str'>
<class 'str'>
<class 'str'>
```

### Comment concaténer des chaînes

Vous pouvez utiliser l'opérateur `+` pour concaténer des chaînes.

La concaténation est lorsque vous avez deux chaînes ou plus et que vous souhaitez les joindre en une seule.

```python
word1 = 'New '
word2 = 'York'

print(word1 + word2)
```

```
New York
```

### Comment sélectionner un caractère

Pour sélectionner un caractère, utilisez `[]` et spécifiez la position du caractère.

La position 0 fait référence à la première position.

```python
>>> word = "Rio de Janeiro"
>>> char=word[0]
>>> print(char)
R
```

### Comment obtenir la taille d'une chaîne

La fonction `len()` retourne la longueur d'une chaîne.

```python
>>> len('Rio')
3
>>> len('Rio de Janeiro')
14
```

### Comment remplacer une partie d'une chaîne

La méthode `replace()` remplace une partie de la chaîne par une autre. Par exemple, remplaçons 'Rio' par 'Mar'.

```python
>>> 'Rio de Janeiro'.replace('Rio', 'Mar')
'Mar de Janeiro'
```

Rio signifie fleuve en portugais et Mar signifie mer – juste pour que vous sachiez que je n'ai pas choisi ce remplacement si aléatoirement.

### Comment compter

Spécifiez ce que vous voulez compter comme argument.

Dans ce cas, nous comptons combien d'espaces existent dans "Rio de Janeiro", qui est 2.

```python
>>> word = "Rio de Janeiro"
>>> print(word.count(' '))
2
```

### Comment répéter une chaîne

Vous pouvez utiliser le symbole `*` pour répéter une chaîne.

Ici, nous multiplions le mot "Tokyo" par 3.

```python
>>> words = "Tokyo" * 3 
>>> print(words)
TokyoTokyoTokyo
```


## Comment diviser une chaîne en Python

Diviser une chaîne en parties plus petites est une tâche très courante. Pour ce faire, nous utilisons la méthode `split()` en Python.

Voyons quelques exemples sur la façon de procéder.

### Exemple 1 : utiliser les espaces blancs comme délimiteurs

Dans cet exemple, nous divisons la phrase par des espaces blancs en créant une liste nommée **my_words** avec cinq éléments correspondant à chaque mot de la phrase.

```python
my_phrase = "let's go to the beach"
my_words = my_phrase.split(" ")

for word in my_words:
    print(word)
#output:
#let's
#go
#to
#the
#beach

print(my_words)
#output:
#["let's", 'go', 'to', 'the', 'beach']
```

Remarquez que, par défaut, la méthode `split()` utilise tout nombre consécutif d'espaces blancs comme délimiteurs. Nous pouvons changer le code ci-dessus en :

```python
my_phrase = "let's go to the beach"
my_words = my_phrase.split()

for word in my_words:
    print(word)

#output:
#let's
#go
#to
#the
#beach
```

La sortie est la même puisque nous n'avons qu'un seul espace blanc entre chaque mot.

### Exemple 2 : passer différents arguments comme délimiteurs

Lorsque vous travaillez avec des données, il est très courant de lire certains fichiers CSV pour en extraire des informations.

Ainsi, vous pourriez avoir besoin de stocker certaines données spécifiques d'une certaine colonne.

Les fichiers CSV ont généralement des champs séparés par un point-virgule ";" ou une virgule ",".

Dans cet exemple, nous allons utiliser la méthode `split()` en passant comme argument un délimiteur spécifique, ";" dans ce cas.

```python
my_csv = "mary;32;australia;mary@email.com"
my_data = my_csv.split(";")

for data in my_data:
    print(data)

#output:
#mary
#32
#australia
#mary@email.com

print(my_data[3])
#output:
# mary@email.com
```

## Comment supprimer tous les espaces blancs dans une chaîne en Python

Si vous voulez vraiment supprimer tout espace dans une chaîne, ne laissant que les caractères, la meilleure solution est d'utiliser une expression régulière.

Vous devez importer le module `re` qui fournit des opérations d'expressions régulières.

Remarquez que `\s` représente non seulement l'espace `' '`, mais aussi le saut de page `\f`, le saut de ligne `\n`, le retour chariot `\r`, la tabulation `\t`, et la tabulation verticale `\v`.

En résumé, `\s = [ \f\n\r\t\v]`.

Le symbole `+` est appelé un quantificateur et se lit comme 'un ou plusieurs'. Cela signifie qu'il considérera, dans ce cas, un ou plusieurs espaces blancs puisqu'il est positionné juste après le `\s`.

```python
import re

phrase = ' Do   or do    not   there    is  no try   '

phrase_no_space = re.sub(r'\s+', '', phrase)

print(phrase)
# Do   or do    not   there    is  no try   

print(phrase_no_space)
#Doordonotthereisnotry
```

La variable originale `phrase` reste la même. Vous devez assigner la nouvelle chaîne nettoyée à une nouvelle variable, `phrase_no_space` dans ce cas.

## Comment gérer les chaînes multilingues en Python

### Guillemets triples

Pour gérer les chaînes multilingues en Python, vous utilisez des guillemets triples, simples ou doubles.

Ce premier exemple utilise des guillemets doubles.

```python
long_text = """This is a multiline,

a long string with lots of text,

I'm wrapping it in triple quotes to make it work."""

print(long_text)
#output:
#This is a multiline,
#
#a long string with lots of text,
#
#I'm wrapping it in triple quotes to make it work.
```

Maintenant, la même chose qu'avant, mais avec des guillemets simples :

```python
long_text = '''This is a multiline,

a long string with lots of text,

I'm wrapping it in triple quotes to make it work.'''

print(long_text)
#output:
#This is a multiline,
#
#a long string with lots of text,
#
#I'm wrapping it in triple quotes to make it work.
```

Remarquez que les deux sorties sont les mêmes.

### Parentheses

Voyons un exemple avec des parenthèses.

```python
long_text = ("This is a multiline, "
"a long string with lots of text "
"I'm wrapping it in brackets to make it work.")
print(long_text)
#This is a multiline, a long string with lots of text I'm wrapping it in triple quotes to make it work.
```

Comme vous pouvez le voir, le résultat n'est pas le même. Pour obtenir de nouvelles lignes, je dois ajouter `\n`, comme ceci :

```python
long_text = ("This is a multiline, \n\n"
"a long string with lots of text \n\n"
"I'm wrapping it in brackets to make it work.")
print(long_text)
#This is a multiline, 
#
#a long string with lots of text 
#
#I'm wrapping it in triple quotes to make it work.
```

### Backslashes

Enfin, les backslashes sont également une possibilité.

Remarquez qu'il n'y a pas d'espace après le caractère `\`, car cela générerait une erreur.

```python
long_text = "This is a multiline, \n\n" \
"a long string with lots of text \n\n" \
"I'm using backlashes to make it work."
print(long_text)
#This is a multiline, 
#
#a long string with lots of text 
#
#I'm wrapping it in triple quotes to make it work.
```

## lstrip() : Comment supprimer les espaces et les caractères du début d'une chaîne en Python

Utilisez la méthode `lstrip()` pour supprimer les espaces du début d'une chaîne.

```python
regular_text = "   This is a regular text."

no_space_begin_text = regular_text.lstrip()

print(regular_text)
#'   This is a regular text.'

print(no_space_begin_text)
#'This is a regular text.'
```

Remarquez que la variable originale `regular_text` reste inchangée, vous devez donc assigner le retour de la méthode à une nouvelle variable, `no_space_begin_text` dans ce cas.

### Comment supprimer les caractères

La méthode `lstrip()` accepte également des caractères spécifiques pour la suppression en tant que paramètres.

```python
regular_text = "$@G#This is a regular text."

clean_begin_text = regular_text.lstrip("#$@G")

print(regular_text)
#$@G#This is a regular text.

print(clean_begin_text)
#This is a regular text.
```

## rstrip() : Comment supprimer les espaces et les caractères de la fin d'une chaîne en Python

Utilisez la méthode `rstrip()` pour supprimer les espaces de la fin d'une chaîne.

```python
regular_text = "This is a regular text.   "

no_space_end_text = regular_text.rstrip()

print(regular_text)
#'This is a regular text.   '

print(no_space_end_text)
#'This is a regular text.'
```

Remarquez que la variable originale `regular_text` reste inchangée, vous devez donc assigner le retour de la méthode à une nouvelle variable, `no_space_end_text` dans ce cas.

La méthode `rstrip()` accepte également des caractères spécifiques pour la suppression en tant que paramètres.

```python
regular_text = "This is a regular text.$@G#"

clean_end_text = regular_text.rstrip("#$@G")

print(regular_text)
#This is a regular text.$@G#

print(clean_end_text)
#This is a regular text.
```

## strip() : Comment supprimer les espaces et les caractères du début et de la fin d'une chaîne en Python

Utilisez la méthode `strip()` pour supprimer les espaces du début et de la fin d'une chaîne.

```python
regular_text = "  This is a regular text.   "

no_space_text = regular_text.strip()

print(regular_text)
#'  This is a regular text.   '

print(no_space_text)
#'This is a regular text.'
```

Remarquez que la variable originale `regular_text` reste inchangée, vous devez donc assigner le retour de la méthode à une nouvelle variable, `no_space_text` dans ce cas.

La méthode `strip()` accepte également des caractères spécifiques pour la suppression en tant que paramètres.

```python
regular_text = "AbC#This is a regular text.$@G#"

clean_text = regular_text.strip("AbC#$@G")

print(regular_text)
#AbC#This is a regular text.$@G#

print(clean_text)
#This is a regular text.
```

## Comment mettre une chaîne entière en minuscules en Python

Utilisez la méthode `lower()` pour transformer une chaîne entière en minuscules.

```python
regular_text = "This is a Regular TEXT."

lower_case_text = regular_text.lower()

print(regular_text)
#This is a Regular TEXT.

print(lower_case_text)
#this is a regular text.
```

Remarquez que la variable originale `regular_text` reste inchangée, vous devez donc assigner le retour de la méthode à une nouvelle variable, `lower_case_text` dans ce cas.

## Comment mettre une chaîne entière en majuscules en Python

Utilisez la méthode `upper()` pour transformer une chaîne entière en majuscules.

```python
regular_text = "This is a regular text."

upper_case_text = regular_text.upper()

print(regular_text)
#This is a regular text.

print(upper_case_text)
#THIS IS A REGULAR TEXT.
```

Remarquez que la variable originale `regular_text` reste inchangée, vous devez donc assigner le retour de la méthode à une nouvelle variable, `upper_case_text` dans ce cas.

## Comment utiliser la casse de titre en Python

Utilisez la méthode `title()` pour transformer la première lettre de chaque mot en majuscule et le reste des caractères en minuscules.

```python
regular_text = "This is a regular text."

title_case_text = regular_text.title()

print(regular_text)
#This is a regular text.

print(title_case_text)
#This Is A Regular Text.
```

Remarquez que la variable originale `regular_text` reste inchangée, vous devez donc assigner le retour de la méthode à une nouvelle variable, `title_case_text` dans ce cas.

## Comment utiliser la casse d'échange en Python

Utilisez la méthode `swapcase()` pour transformer les caractères en majuscules en minuscules et vice versa.

```python
regular_text = "This IS a reguLar text."

swapped_case_text = regular_text.swapcase()

print(regular_text)
#This IS a reguLar text.

print(swapped_case_text)
#tHIS is A REGUlAR TEXT.
```

Remarquez que la variable originale `regular_text` reste inchangée, vous devez donc assigner le retour de la méthode à une nouvelle variable, `swapped_case_text` dans ce cas.

## Comment vérifier si une chaîne est vide en Python

La manière pythonique de vérifier si une `string` est vide est d'utiliser l'opérateur `not`.

```python
my_string = ''
if not my_string:
  print("My string is empty!!!")
```

Pour vérifier le contraire et voir si la chaîne n'est **pas** vide, faites ceci :

```python
my_string = 'amazon, microsoft'
if my_string:
  print("My string is NOT empty!!!")
```

## rjust() : Comment justifier à droite une chaîne en Python

Utilisez `rjust()` pour justifier à droite une chaîne.

```python
word = 'beach'
number_spaces = 32

word_justified = word.rjust(number_spaces)

print(word)
#'beach'

print(word_justified)
#'                           beach'
```

Remarquez les espaces dans la deuxième chaîne. Le mot 'beach' a 5 caractères, ce qui nous donne 27 espaces à remplir avec de l'espace vide.

La variable originale `word` reste inchangée, nous devons donc assigner le retour de la méthode à une nouvelle variable, `word_justified` dans ce cas.

`rjust()` accepte également un caractère spécifique comme paramètre pour remplir l'espace restant.

```python
word = 'beach'
number_chars = 32
char = '$'

word_justified = word.rjust(number_chars, char)

print(word)
#beach

print(word_justified)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$beach
```

Similaire à la première situation, j'ai 27 signes `$` pour en faire un total de 32 lorsque je compte les 5 caractères contenus dans le mot 'beach'.

## ljust() : Comment justifier à gauche une chaîne en Python

Utilisez `ljust()` pour justifier à gauche une chaîne.

```python
word = 'beach'
number_spaces = 32

word_justified = word.ljust(number_spaces)

print(word)
#'beach'

print(word_justified)
#'beach                           '
```

Remarquez les espaces dans la deuxième chaîne. Le mot 'beach' a 5 caractères, ce qui nous donne 27 espaces à remplir avec de l'espace vide.

La variable originale `word` reste inchangée, nous devons donc assigner le retour de la méthode à une nouvelle variable, `word_justified` dans ce cas.

`ljust()` accepte également un caractère spécifique comme paramètre pour remplir l'espace restant.

```python
word = 'beach'
number_chars = 32
char = '$'

word_justified = word.ljust(number_chars, char)

print(word)
#beach

print(word_justified)
#beach$$$$$$$$$$$$$$$$$$$$$$$$$$$
```

Similaire à la première situation, j'ai 27 signes `$` pour en faire un total de 32 lorsque je compte les 5 caractères contenus dans le mot 'beach'.

## isalnum() : Comment vérifier les caractères alphanumériques uniquement dans une chaîne en Python

Utilisez la méthode `isalnum()` pour vérifier si une chaîne ne contient que des caractères alphanumériques.

```python
word = 'beach'
print(word.isalnum())
#output: True

word = '32'
print(word.isalnum())
#output: True

word = 'number32' #remarquez qu'il n'y a pas d'espace
print(word.isalnum())
#output: True

word = 'Favorite number is 32' #remarquez l'espace entre les mots
print(word.isalnum())
#output: False

word = '@number32$' #remarquez les caractères spéciaux '@' et '$'
print(word.isalnum())
#output: False
```

## isprintable() : Comment vérifier les caractères imprimables dans une chaîne en Python

Utilisez la méthode `isprintable()` pour vérifier si les caractères d'une chaîne sont imprimables.

```python
text = '' # remarquez que ceci est une chaîne vide, il n'y a pas d'espace blanc ici
print(text.isprintable())
#output: True

text = 'This is a regular text'
print(text.isprintable())
#output: True

text = ' ' #un espace
print(text.isprintable())
#output: True

text = '                        '  #beaucoup d'espaces
print(text.isprintable())
#output: True

text = '\f\n\r\t\v'
print(text.isprintable())
#output: False
```

Remarquez que dans les 4 premiers exemples, chaque caractère prend de la place, même s'il s'agit d'un espace vide comme vous pouvez le voir dans le premier exemple.

Le dernier exemple retourne `False`, montrant 5 types de caractères qui ne sont pas imprimables : saut de page `\f`, saut de ligne `\n`, retour chariot `\r`, tabulation `\t`, et tabulation verticale `\v`.

Certains de ces caractères 'invisibles' peuvent perturber votre impression, vous donnant une sortie inattendue, même lorsque tout 'semble' correct.


## isspace() : Comment vérifier les espaces blancs uniquement dans une chaîne en Python

Utilisez la méthode `isspace()` pour vérifier si les caractères d'une chaîne sont tous des espaces blancs.

```python
text = ' '
print(text.isspace())
#output: True

text = ' \f\n\r\t\v'
print(text.isspace())
#output: True

text = '                        '
print(text.isspace())
#output: True

text = '' # remarquez que ceci est une chaîne vide, il n'y a pas d'espace blanc ici
print(text.isspace())
#output: False

text = 'This is a regular text'
print(text.isspace())
#output: False
```

Remarquez dans le deuxième exemple que l'espace blanc n'est pas seulement `' '`, mais aussi le saut de page `\f`, le saut de ligne `\n`, le retour chariot `\r`, la tabulation `\t`, et la tabulation verticale `\v`.

## startswith() : Comment vérifier si une chaîne commence par une certaine valeur en Python

Utilisez la méthode `startswith()` pour vérifier si une chaîne commence par une certaine valeur.

```python
phrase = "This is a regular text"

print(phrase.startswith('This is'))
#output: True

print(phrase.startswith('text'))
#output: False
```

Vous pouvez également définir si vous voulez commencer la correspondance à une position spécifique et la terminer à une autre position spécifique de la chaîne.

```python
phrase = "This is a regular text"

print(phrase.startswith('regular', 10)) #le mot regular commence à la position 10 de la phrase
#output: True

print(phrase.startswith('regular', 10, 22)) #recherche dans 'regular text'
#output: True

print(phrase.startswith('regular', 10, 15)) ##recherche dans 'regul'
#output: False
```

Enfin, vous pourriez vouloir vérifier plusieurs chaînes à la fois. Au lieu d'utiliser une sorte de boucle, vous pouvez utiliser un tuple comme argument avec toutes les chaînes que vous voulez faire correspondre.

```python
phrase = "This is a regular text"

print(phrase.startswith(('regular', 'This')))
#output: True

print(phrase.startswith(('regular', 'text')))
#output: False

print(phrase.startswith(('regular', 'text'), 10, 22)) #recherche dans 'regular text'
#output: True
```

## capitalize() : Comment définir uniquement le premier caractère en majuscule dans une chaîne en Python

Utilisez la méthode `capitalize()` pour convertir uniquement le premier caractère d'une chaîne en majuscule.

Le reste de la chaîne est converti en minuscules.

```python
text = 'this is a regular text'
print(text.capitalize())
#This is a regular text

text = 'THIS IS A REGULAR TEXT'
print(text.capitalize())
#This is a regular text

text = 'THIS $ 1S @ A R3GULAR TEXT!'
print(text.capitalize())
#This $ 1s @ a r3gular text!

text = '3THIS $ 1S @ A R3GULAR TEXT!'
print(text.capitalize())
#3this $ 1s @ a r3gular text!
```

Remarquez que n'importe quel caractère compte, comme un nombre ou un caractère spécial. Donc dans le dernier exemple, `3` est le premier caractère et ne subit aucune altération tandis que le reste de la chaîne est converti en minuscules.

## isupper() : Comment vérifier les majuscules uniquement dans une chaîne en Python

Utilisez la méthode `isupper()` pour vérifier si les caractères d'une chaîne sont tous en majuscules.

```python
text = 'This is a regular text'
print(text.isupper())
#output: False

text = 'THIS IS A REGULAR TEXT'
print(text.isupper())
#output: True

text = 'THIS $ 1S @ A R3GULAR TEXT!'
print(text.isupper())
#output: True
```

Si vous remarquez le dernier exemple, les nombres et les caractères spéciaux comme `@` et `$` dans la chaîne ne font aucune différence et `isupper()` retourne toujours `True` parce que la méthode ne vérifie que les caractères alphabétiques.


## join() : Comment joindre les éléments d'un itérable en une seule chaîne en Python

Utilisez la méthode `join()` pour joindre tous les éléments d'un itérable en une chaîne.

La syntaxe de base est : `string.join(iterable)`

Selon la syntaxe ci-dessus, une chaîne est requise comme séparateur.

La méthode retourne une nouvelle chaîne, ce qui signifie que l'itérateur original reste inchangé.

Puisque la méthode `join()` n'accepte que les chaînes, si un élément de l'itérable est d'un type différent, une erreur sera générée.

Voyons quelques exemples avec : chaîne, liste, tuple, ensemble et dictionnaire

### join() : Chaînes

La méthode `join()` place le signe `$` comme séparateur pour chaque caractère de la chaîne.

```python
my_string = 'beach'

print('$'.join(my_string))
#output: b$e$a$c$h
```

### join() : Listes

J'ai une liste simple de trois éléments représentant des marques de voitures.

La méthode `join()` va utiliser le signe `$` comme séparateur.

Elle concatène tous les éléments de la liste et place le signe `$` entre eux.

```python
my_list = ['bmw', 'ferrari', 'mclaren']

print('$'.join(my_list))
#output: bmw$ferrari$mclaren
```

Cet exemple vous rappelle que `join()` ne fonctionne pas avec des éléments non-chaines.

Lorsque vous essayez de concaténer les éléments `int`, une erreur est générée.

```python
my_list = [1, 2, 3]

print('$'.join(my_list))
#output:
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: sequence item 0: expected str instance, int found
```

### join() : Tuples

Le tuple suit la même logique que l'exemple de liste expliqué précédemment.

Encore une fois, j'utilise le signe `$` comme séparateur.

```python
my_tuple = ('bmw', 'ferrari', 'mclaren')

print('$'.join(my_tuple))
#output: bmw$ferrari$mclaren
```

### join() : Ensembles

Puisque l'ensemble est également le même que le tuple et la liste, j'ai utilisé un séparateur différent dans cet exemple.

```python
my_set = {'bmw', 'ferrari', 'mclaren'}
print('|'.join(my_set))
#output: ferrari|bmw|mclaren
```

### join() : dictionnaires

Le dictionnaire a une particularité lorsque vous utilisez la méthode `join()` : il joint les clés, pas les valeurs.

Cet exemple montre la concaténation des clés.

```python
my_dict = {'bmw': 'BMW I8', 'ferrari': 'Ferrari F8', 'mclaren': 'McLaren 720S'}

print(','.join(my_dict))
#output: bmw,ferrari,mclaren
```

## splitlines() : Comment diviser une chaîne aux sauts de ligne en Python

Utilisez la méthode `splitlines()` pour diviser une chaîne aux sauts de ligne.

Le retour de la méthode est une liste des lignes.

```python
my_string = 'world \n cup'

print(my_string.splitlines())
#output: ['world ', ' cup']
```

Si vous voulez conserver le saut de ligne, `splitlines()` accepte un paramètre qui peut être défini sur *True*, la valeur par défaut est *False*.

```python
my_string = 'world \n cup'

print(my_string.splitlines(True))
#output: ['world \n', ' cup']
```

## islower() : Comment vérifier les minuscules uniquement dans une chaîne en Python

Utilisez la méthode `islower()` pour vérifier si les caractères d'une chaîne sont tous en minuscules.

```python
text = 'This is a regular text'
print(text.islower())
#output: False

text = 'this is a regular text'
print(text.islower())
#output: True

text = 'this $ 1s @ a r3gular text!'
print(text.islower())
#output: True
```

Si vous remarquez dans le dernier exemple, les nombres et les caractères spéciaux comme `@` et `$` dans la chaîne ne font aucune différence et `islower()` retourne toujours `True` parce que la méthode ne vérifie que les caractères alphabétiques.

## isnumeric() : Comment vérifier les numériques uniquement dans une chaîne en Python

Utilisez la méthode `isnumeric()` pour vérifier si une chaîne ne contient que des caractères numériques.

Les numériques incluent les nombres de 0 à 9 et leurs combinaisons, les chiffres romains, les exposants, les indices, les fractions et d'autres variations.

```python
word = '32'
print(word.isnumeric())
#output: True

print("\u2083".isnumeric()) #unicode pour l'indice 3
#output: True

print("\u2169".isnumeric()) #unicode pour le chiffre romain X
#output: True

word = 'beach'
print(word.isnumeric())
#output: False

word = 'number32'
print(word.isnumeric())
#output: False

word = '1 2 3' #remarquez l'espace entre les caractères
print(word.isnumeric())
#output: False

word = '@32$' #remarquez les caractères spéciaux '@' et '$'
print(word.isnumeric())
#output: False
```

`isdecimal()` est plus strict que `isdigit()`, qui à son tour est plus strict que `isnumeric()`.

## isdigit() : Comment vérifier les chiffres uniquement dans une chaîne en Python

Utilisez la méthode `isdigit()` pour vérifier si une chaîne ne contient que des chiffres.

Les chiffres incluent les nombres de 0 à 9 ainsi que les exposants et les indices.

```python
word = '32'
print(word.isdigit())
#output: True

print("\u2083".isdigit()) #unicode pour l'indice 3
#output: True

word = 'beach'
print(word.isdigit())
#output: False

word = 'number32'
print(word.isdigit())
#output: False

word = '1 2 3' #remarquez l'espace entre les caractères
print(word.isdigit())
#output: False

word = '@32$' #remarquez les caractères spéciaux '@' et '$'
print(word.isdigit())
#output: False
```

`isdecimal()` est plus strict que `isdigit()`, qui à son tour est plus strict que `isnumeric()`.

## isdecimal() : Comment vérifier les décimaux uniquement dans une chaîne en Python

Utilisez la méthode `isdecimal()` pour vérifier si une chaîne ne contient que des décimaux, c'est-à-dire uniquement des nombres de 0 à 9 et des combinaisons de ces nombres.

Les indices, exposants, chiffres romains et autres variations seront retournés comme `False`.

```python
word = '32'
print(word.isdecimal())
#output: True

word = '954'
print(word.isdecimal())
#output: True

print("\u2083".isdecimal()) #unicode pour l'indice 3
#output: False

word = 'beach'
print(word.isdecimal())
#output: False

word = 'number32'
print(word.isdecimal())
#output: False

word = '1 2 3' #remarquez l'espace entre les caractères
print(word.isdecimal())
#output: False

word = '@32$' #remarquez les caractères spéciaux '@' et '$'
print(word.isdecimal())
#output: False
```

`isdecimal()` est plus strict que `isdigit()`, qui à son tour est plus strict que `isnumeric()`.

## isalpha() : Comment vérifier les lettres uniquement dans une chaîne en Python

Utilisez la méthode `isalpha()` pour vérifier si une chaîne ne contient que des lettres.

```python
word = 'beach'
print(word.isalpha())
#output: True

word = '32'
print(word.isalpha())
#output: False

word = 'number32'
print(word.isalpha())
#output: False

word = 'Favorite number is blue' #remarquez l'espace entre les mots
print(word.isalpha())
#output: False

word = '@beach$' #remarquez les caractères spéciaux '@' et '$'
print(word.isalpha())
#output: False
```

## istitle() : Comment vérifier si chaque mot commence par un caractère en majuscule dans une chaîne en Python

Utilisez la méthode `istitle()` pour vérifier si le premier caractère de chaque mot dans une chaîne est en majuscule et les autres caractères sont en minuscules.

```python
text = 'This is a regular text'
print(text.istitle())
#output: False

text = 'This Is A Regular Text'
print(text.istitle())
#output: True

text = 'This $ Is @ A Regular 3 Text!'
print(text.istitle())
#output: True
```

Si vous remarquez dans le dernier exemple, les nombres et les caractères spéciaux comme `@` et `$` dans la chaîne ne font aucune différence et `istitle()` retourne toujours `True` parce que la méthode ne vérifie que les caractères alphabétiques.

## expandtabs() : Comment définir le nombre d'espaces pour une tabulation dans une chaîne en Python

Utilisez la méthode `expandtabs()` pour définir le nombre d'espaces pour une tabulation.

Vous pouvez définir n'importe quel nombre d'espaces, mais lorsqu'aucun argument n'est donné, la valeur par défaut est 8.

### Utilisation de base

```python
my_string = 'B\tR'

print(my_string.expandtabs())
#output: B       R
```

Remarquez les 7 espaces entre les lettres B et R.

La `\t` est à la position deux après un caractère, donc elle sera remplacée par 7 espaces.

Regardons un autre exemple.

```python
my_string = 'WORL\tD'

print(my_string.expandtabs())
#output: WORL    D
```

Puisque `WORL` a quatre caractères, la `\t` est remplacée par 4 espaces pour en faire un total de 8, la taille de tabulation par défaut.

Le code ci-dessous nous donne *4* espaces pour la première tabulation après quatre caractères 'WORL' et *7* espaces pour la deuxième tabulation après un caractère 'D'.

```python
my_string = 'WORL\tD\tCUP'

print(my_string.expandtabs())
#output: WORL    D       CUP
```

### Taille de tabulation personnalisée

Il est possible de définir la taille de tabulation selon les besoins.

Dans cet exemple, la taille de tabulation est *4*, ce qui nous donne 3 espaces après le caractère 'B'.

```python
my_string = 'B\tR'

print(my_string.expandtabs(4))
#output: B   R
```

Ce code a une taille de tabulation définie à *6*, ce qui nous donne 5 espaces après le caractère 'B'.

```python
my_string = 'B\tR'

print(my_string.expandtabs(6))
#output: B     R
```

## center() : Comment centrer une chaîne en Python

Utilisez la méthode `center()` pour centrer une chaîne.

```python
word = 'beach'
number_spaces = 32

word_centered = word.center(number_spaces)

print(word)
#'beach'

print(word_centered)
##output: '              beach              '
```

Remarquez les espaces dans la deuxième chaîne. Le mot 'beach' a 5 caractères, ce qui nous donne 28 espaces à remplir avec de l'espace vide, 14 espaces avant et 14 après pour centrer le mot.

La variable originale `word` reste inchangée, nous devons donc assigner le retour de la méthode à une nouvelle variable, `word_centered` dans ce cas.

La méthode `center()` accepte également un caractère spécifique comme paramètre pour remplir l'espace restant.

```python
word = 'beach'
number_chars = 33
char = '$'

word_centered = word.center(number_chars, char)

print(word)
#beach

print(word_centered)
#output: $$$$$$$$$$$$$$beach$$$$$$$$$$$$$$
```

Similaire à la première situation, j'ai 14 `$` de chaque côté pour en faire un total de 33 lorsque je compte les 5 caractères contenus dans le mot 'beach'.

## zfill() : Comment ajouter des zéros à une chaîne en Python

Utilisez `zfill()` pour insérer des zéros `0` au début d'une chaîne.

Le nombre de zéros est donné par le nombre passé comme argument moins le nombre de caractères dans la chaîne.

Le mot 'beach' a 5 caractères, ce qui nous donne 27 espaces à remplir avec des zéros pour en faire un total de 32 comme spécifié dans la variable `size_string`

```python
word = 'beach'
size_string = 32

word_zeros = word.zfill(size_string)

print(word)
#beach

print(word_zeros)
#000000000000000000000000000beach
```

La variable originale `word` reste inchangée, nous devons donc assigner le retour de la méthode à une nouvelle variable, `word_zeros` dans ce cas.

Remarquez également que si l'argument est inférieur au nombre de caractères dans la chaîne, rien ne change.

Dans l'exemple ci-dessous, 'beach' a 5 caractères et nous voulons ajouter des zéros jusqu'à ce qu'il atteigne la `size_string` de 4, ce qui signifie qu'il n'y a rien à faire.

```python
word = 'beach'
size_string = 4

word_zeros = word.zfill(size_string)

print(word)
#beach

print(word_zeros)
#'beach'
```


## find() : Comment vérifier si une chaîne contient une certaine sous-chaîne en Python

Utilisez la méthode `find()` pour vérifier si une chaîne contient une certaine sous-chaîne.

La méthode retourne l'index de la première occurrence de la valeur donnée.

Rappelez-vous que le compte des index commence à 0.

```python
phrase = "This is a regular text"

print(phrase.find('This'))

print(phrase.find('regular'))

print(phrase.find('text'))
```

```
0
10
18
```

Si la valeur n'est pas trouvée, elle retournera `-1`.

```python
phrase = "This is a regular text"

print(phrase.find('train'))
```

```
-1
```

Vous pouvez également choisir de commencer la recherche à une position spécifique et de la terminer à une autre position spécifique de la chaîne.

```python
phrase = "This is a regular text"

#recherche dans 'This is', le reste de la phrase n'est pas inclus
print(phrase.find('This', 0, 7))

#recherche dans 'This is a regular'
print(phrase.find('regular', 0, 17))

#recherche dans 'This is a regul'
print(phrase.find('a', 0, 15))
```

```
0
10
8
```


## Comment supprimer un préfixe ou un suffixe dans une chaîne en Python

À partir de Python 3.9, le type String aura deux nouvelles méthodes.

Vous pouvez spécifiquement supprimer un préfixe d'une chaîne en utilisant la méthode `removeprefix()` :

```python
>>> 'Rio de Janeiro'.removeprefix("Rio")
' de Janeiro'
```

Ou supprimer un suffixe en utilisant la méthode `removesuffix()` :

```python
>>> 'Rio de Janeiro'.removesuffix("eiro")
'Rio de Jan'
```

Il suffit de passer en argument le texte à considérer comme préfixe ou suffixe à supprimer et la méthode retournera une nouvelle chaîne comme résultat.

Je recommande de lire le [PEP 616](https://www.python.org/dev/peps/pep-0616/) dans la documentation officielle si vous êtes curieux de savoir comment ces fonctionnalités sont ajoutées au langage.

Celle-ci est un changement assez simple et très convivial pour les débutants pour s'habituer à lire la documentation officielle.


## lstrip() vs removeprefix() et rstrip() vs removesuffix()

Cela cause de la confusion pour beaucoup de gens.

Il est facile de regarder `lstrip()` et `removeprefix()` et se demander quelle est la réelle différence entre les deux.

Lorsque vous utilisez `lstrip()`, l'argument est un ensemble de caractères de début qui seront supprimés autant de fois qu'ils se produisent :

```python
>>> word = 'hubbubbubboo'
>>> word.lstrip('hub')
'oo'
```

Alors que `removeprefix()` supprimera uniquement la correspondance exacte :

```python
>>> word = 'hubbubbubboo'
>>> word.removeprefix('hub')
'bubbubboo'
```

Vous pouvez utiliser la même logique pour distinguer entre `rstrip()` et `removesuffix()`.

```python
>>> word = 'peekeeneenee'
>>> word.rstrip('nee')
'peek'
```

```python
>>> word = 'peekeeneenee'
>>> word.removesuffix('nee')
'peekeenee'
```

Et en bonus, au cas où vous n'auriez jamais travaillé avec des expressions régulières auparavant, soyez reconnaissant d'avoir `strip()` pour trimer les ensembles de caractères d'une chaîne au lieu d'une expression régulière :

```python
>>> import re
>>> word = 'amazonia'
>>> word.strip('ami')
'zon'
>>> re.search('^[ami]*(.*?)[ami]*$', word).group(1)
'zon'
```

## Comment fonctionne le découpage en Python

Le découpage est l'un des outils les plus utiles du langage Python.

À ce titre, il est important d'avoir une bonne compréhension de son fonctionnement.

### Notation de découpage de base

Disons que nous avons un tableau appelé 'list'.

```
list[start:stop:step]
```

- start : où vous voulez que le découpage commence
- stop : jusqu'où vous voulez que le découpage aille, mais rappelez-vous que la valeur de *stop* n'est pas incluse
- step : si vous voulez sauter un élément, la valeur par défaut étant 1, donc vous passez par tous les éléments du tableau

### Indexes

Lors du découpage, les indices sont des points *entre* les caractères, pas sur les caractères.

Pour le mot 'movie' :

```
 +---+---+---+---+---+
 | m | o | v | i | e |
 +---+---+---+---+---+
 0   1   2   3   4   5 
-5  -4  -3  -2  -1  
```

Si je découpe de 0 jusqu'à 2, j'obtiens 'mo' dans l'exemple ci-dessus et *pas* 'mov'.

Puisqu'une chaîne est juste une liste de caractères, la même chose s'applique avec une liste :

```
my_list = [1, 2 , 3, 4, 5]
```

Devient :

```
 +---+---+---+---+---+
 | 1 | 2 | 3 | 4 | 5 |
 +---+---+---+---+---+
 0   1   2   3   4   5 
-5  -4  -3  -2  -1  
```

### Exemples de découpage en Python

Nous avons une variable contenant la chaîne 'movie' comme suit :

```python
word = 'movie'
```

Tous les exemples ci-dessous seront appliqués à ce mot.

#### Exemple 1

Pour obtenir les deux premiers caractères :

```python
sliced = word[:2]
print(sliced)
mo
```

Remarquez que nous aurions pu utiliser 0 pour désigner le début, mais ce n'est pas nécessaire.

#### Exemple 2

Le dernier élément :

```python
sliced = word[-1]
print(sliced)
e
```

#### Exemple 3

Sauter des lettres avec un pas de 2 :

```python
sliced = word[::2]
print(sliced)
mve
```

## Comment inverser une chaîne en Python

Pour inverser une chaîne, utilisez la syntaxe de découpage :

```python
my_string = "ferrari"

my_string_reversed = my_string[::-1]

print(my_string)

print(my_string_reversed)
```

```
ferrari

irarref
```

La syntaxe de découpage vous permet de définir un pas, qui est `-1` dans l'exemple.

Le pas par défaut est `1`, c'est-à-dire avancer d'un caractère de la chaîne à la fois.

Si vous définissez le pas à `-1`, vous avez l'inverse, reculer d'un caractère à la fois.

Ainsi, vous commencez à la position du dernier caractère et vous vous déplacez vers l'arrière jusqu'au premier caractère à la position 0.


# Conclusion

C'est tout !

Félicitations pour être arrivé à la fin.

Je tiens à vous remercier d'avoir lu cet article.

Si vous voulez en savoir plus, consultez mon blog [renanmf.com](https://renanmf.com/).

N'oubliez pas [de télécharger une version PDF de ce Guide de manipulation des chaînes Python](https://renanmf.com/python-string-manipulation-handbook/).

Vous pouvez également me trouver sur Twitter : [@renanmouraf](https://twitter.com/renanmouraf).