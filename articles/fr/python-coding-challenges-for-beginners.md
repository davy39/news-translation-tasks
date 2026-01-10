---
title: Défis de codage Python pour les développeurs débutants – Code et explications
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2024-06-04T20:18:55.000Z'
originalURL: https://freecodecamp.org/news/python-coding-challenges-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/pexels-pixabay-139392.jpg
tags:
- name: coding challenge
  slug: coding-challenge
- name: Python
  slug: python
seo_title: Défis de codage Python pour les développeurs débutants – Code et explications
seo_desc: 'Learning Python can be challenging, especially if you''re not actually
  writing enough code. As a beginner, you may go through lessons and tutorials without
  practicing on your own – and this makes it harder to learn the language.

  The truth is, you cann...'
---

Apprendre Python peut être difficile, surtout si vous n'écrivez pas assez de code. En tant que débutant, vous pouvez suivre des leçons et des tutoriels sans pratiquer par vous-même – et cela rend l'apprentissage de la langue plus difficile.

La vérité est que vous ne pouvez pas vraiment apprendre la programmation sans écrire de code. C'est à travers ce processus que vous apprenez de nouvelles choses et découvrez comment de petites erreurs, comme oublier une guillemet ou un espace, peuvent vous frustrer pendant des heures.

Aucun cours ne peut vous enseigner les subtilités de Python comme le fait de trouver et de résoudre des erreurs.

C'est pourquoi les défis de codage sont importants si vous commencez votre parcours en codage. Ils vous aident à mettre en pratique vos connaissances et à renforcer votre confiance.

Alors, pour vous aider à coder davantage, voici huit défis Python que vous pouvez essayer en tant que débutant.

**Et voici un conseil** : essayez vraiment de résoudre le défi par vous-même après avoir lu la question/invitation. Si vous êtes bloqué, vous pouvez alors regarder le code ci-dessous et l'explication pour vous aider à le comprendre.

## Voici les défis :

1. [Défis Python #1 : Vérifier si une liste est triée](#heading-defi-python-1-verifier-si-une-liste-est-triee)
2. [Défis Python #2 : Convertir un nombre binaire en décimal](#heading-defi-python-2-convertir-un-nombre-binaire-en-decimal)
3. [Défis Python #3 : M'aime, m'aime pas](#heading-defi-python-3-maime-maime-pas)
4. [Défis Python #4 : Le défi de la séquence Tribonacci](#heading-defi-python-4-le-defi-de-la-sequence-tribonacci)
5. [Défis Python #5 : Masquer un numéro de carte de crédit](#heading-defi-python-5-masquer-un-numero-de-carte-de-credit)
6. [Défis Python #6 : SpongeCase](#heading-defi-python-6-spongecase)
7. [Défis Python #7 : Chiffrement de César](#heading-defi-python-7-chiffrement-de-cesar)
8. [Défis Python #8 : Le produit est-il divisible par la somme ?](#heading-defi-python-8-le-produit-estil-divisible-par-la-somme)

Tous ces défis vous aident à améliorer vos compétences en résolution de problèmes et en pensée algorithmique. Vous acquerrez également de l'expérience avec l'écriture et le test de code pour garantir la justesse et l'efficacité.

## Défis Python #1 : Vérifier si une liste est triée

Le défi : Écrire une fonction qui vérifie si une liste donnée de nombres est triée en ordre croissant ou décroissant.

Voici la solution de code :

```python
def is_sorted(lst):
    asc, desc = True, True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            asc = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            desc = False
    return asc or desc
```

### Explication du code :

Dans le code ci-dessus, nous définissons une fonction `is_sorted` qui prend une `liste` en tant que paramètre. Nous initialisons deux booléens, `asc` (pour croissant) et `desc` (pour décroissant) à `True`.

Nous parcourons ensuite la liste. Si le `i`ème élément de la liste est supérieur au `(i+1)`ème élément, le drapeau `asc` est défini à `False`, indiquant que la liste n'est pas triée en ordre croissant.

Ensuite, nous parcourons à nouveau la liste. Si le `i`ème élément de la liste est inférieur au `i+1`ème élément, le drapeau `desc` est défini à `False`, indiquant que la liste n'est pas triée en ordre décroissant.

Si un élément est trouvé supérieur à l'élément suivant, le drapeau `asc` est défini à `False`. Dans la boucle, nous vérifions si le `i`ème élément de la liste est supérieur au `i+1`ème élément.

```python
for i in range(len(lst) - 1):
    if lst[i] < lst[i + 1]:
        desc = False
```

Nous retournons `True` si `asc` ou `desc` est `True`. Cela signifie que la liste est triée, soit en ordre croissant, soit en ordre décroissant.

## Défis Python #2 : Convertir un nombre binaire en décimal

Le défi : Écrire une fonction qui convertit un nombre binaire en son équivalent décimal.

Voici la solution de code :

```python
def binary_to_decimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
```

### Explication du code :

Dans le code ci-dessus, nous définissons une fonction `binary_to_decimal` qui prend un nombre `binaire` en tant que paramètre. Nous initialisons ensuite les variables `decimal` et `i` à `0`.

La variable `decimal` est utilisée pour stocker la valeur décimale résultante et la variable `i` représente la position actuelle lors du traitement d'un nombre binaire, commençant à `0`.

Nous parcourons chaque chiffre binaire jusqu'à ce que tous les chiffres du nombre binaire deviennent `0`.

```python
while binary != 0:
```

Maintenant, nous extrayons le chiffre le moins significatif du nombre binaire actuel en utilisant l'opérateur modulo.

```python
dec = binary % 10
```

Et ensuite, nous convertissons le chiffre extrait en son équivalent décimal en le multipliant par 2 à la puissance `i`.

```python
decimal = decimal + dec * pow(2, i)
```

Ensuite, nous supprimons le chiffre traité :

```python
Binary = binary // 10
```

Et nous incrémentons la position `i` pour traiter le chiffre binaire suivant :

```python
i += 1
```

Enfin, nous retournons la valeur décimale calculée.

## Défis Python #3 : M'aime, m'aime pas

Le défi : Étant donné un entier n, imprimer une chaîne qui alterne entre les phrases "M'aime" et "M'aime pas" pour chaque nombre de 1 à n.

La séquence doit commencer par "M'aime" et alterner en conséquence.

Voici la solution de code :

```python
def phrase_loves_me_not(n):
    phrases = []
    for i in range(1,n+1):
        if i % 2 != 0:
            phrases.append("M'aime")
        else:
            phrases.append("M'aime pas")
    return ", ".join(phrases)
```

### Explication du code :

Nous définissons une fonction `phrase_loves_me_not` qui prend un seul paramètre `n`.

Ensuite, nous initialisons une liste vide, `phrases`, qui stocke le résultat pour chaque nombre de `1` à `n`.

Nous itérons de `1` à `n` inclus :

```python
for i in range(1, n+1):
```

Nous vérifions ensuite les indices impairs. Si le nombre est impair, nous ajoutons "M'aime" à la liste 'phrases'.

```python
if i % 2 != 0:
    phrases.append("M'aime")
```

Pour les indices pairs, nous ajoutons "M'aime pas" dans la liste 'phrases'.

```python
else:
    phrases.append("M'aime pas")
```

Nous utilisons ensuite la méthode `join` pour concaténer tous les éléments de la liste 'phrases' en une seule chaîne et retournons cette chaîne.

Enfin, nous retournons la chaîne résultante.

```python
return ", ".join(phrases)

```

## Défis Python #4 : Le défi de la séquence Tribonacci

Le défi de la "séquence Tribonacci" est une variante de la célèbre séquence de Fibonacci, où chaque nombre est la somme des trois nombres précédents.

Par exemple, 0, 1, 1, 2, 4, 7 …

Le défi : Écrire une fonction qui retourne le n-ième nombre dans la séquence Tribonacci.

Voici la solution de code :

```python
def find_nth_tribonacci(n):
    # Cas de base pour n = 0, 1, 2
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    # Initialiser les trois premiers termes de la séquence Tribonacci
    a, b, c = 0, 1, 1
    for i in range(3, n + 1):
        next_term = a + b + c
        a, b, c = b, c, next_term
    return c
```

### Explication du code :

Tout d'abord, nous définissons une fonction nommée `find_nth_tribonacci` qui prend un nombre `n` en tant que paramètre.

Nous définissons ensuite les cas de base comme suit :

* Si `n` est `0`, la fonction retourne `0`.
* Si `n` est `1` ou `2`, la fonction retourne `1`.

Note : Ces conditions gèrent les valeurs de départ de la séquence Tribonacci.

Nous initialisons ensuite les trois premières valeurs de la séquence Tribonacci, de `n` = `0` à `n` = `2`.

```python
a, b, c = 0, 1, 1
```

Ensuite, nous itérons de `3` au nombre `n`, où nous calculons le terme suivant en additionnant les trois termes précédents (`a`, `b` et `c`). Nous mettons également à jour les valeurs de `a`, `b` et `c` pour le prochain ensemble de trois termes dans la séquence.

```python
for i in range(3, n + 1):
    next_term = a + b + c
    a, b, c = b, c, next_term
```

À la fin de la boucle, `c` contient la valeur du n-ième terme dans la séquence Tribonacci, donc nous retournons `c`.

```python
return c
```

## Défis Python #5 : Masquer un numéro de carte de crédit

Écrire une fonction qui prend un numéro de carte de crédit et le transforme en une chaîne où tous les chiffres sauf les quatre derniers sont remplacés par des astérisques.

Voici la solution de code :

```python
def mask_credit_card(card_number):
    card=str(card_number)
    return "*"*(len(card) - 4) + (card[-4:])
```

### Explication du code :

Nous définissons une fonction `mask_credit_card` qui prend `card_number` en tant que paramètre.

Tout d'abord, nous convertissons le numéro en une chaîne.

```python
card = str(card_number)
```

Ensuite, pour masquer le numéro de carte, nous générons une chaîne d'astérisques avec une longueur égale au nombre total de chiffres dans la carte de crédit moins quatre. Cela masque tous les chiffres sauf les quatre derniers.

```python
"*"*(len(card) - 4)
```

Ensuite, nous utilisons l'opération de découpage pour récupérer les quatre derniers chiffres du numéro de carte de crédit.

```python
card[-4:]
```

Enfin, nous retournons le résultat concaténé de la chaîne d'astérisques et des quatre derniers chiffres du numéro de carte.

```python
return "*"*(len(card) - 4) + card[-4:]
```

## Défis Python #6 : SpongeCase

SpongeCase est un style de texte où les lettres apparaissent alternativement en minuscules et en majuscules. Par exemple, le mot en SpongeCase serait sPoNgEcAsE.

Le défi : Écrire une fonction qui convertit la chaîne donnée en SpongeCase.

Voici la solution de code :

```python
def to_spongecase(text):
    result = []
    i = 0
    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                result.append(char.lower())
            else:
                result.append(char.upper())
            i += 1
        else:
            result.append(char)
           
    return "".join(result)

```

### Explication du code :

Nous définissons une fonction `to_spongecase` qui prend une chaîne `text` en tant que paramètre.

Ensuite, nous initialisons une liste vide `result`, et un compteur `i` à `0`.

Nous itérons la fonction sur chaque caractère `char` dans la chaîne d'entrée et vérifions si le caractère actuel est alphabétique.

```python
for char in text:
    if char.isalpha():
```

Si le caractère à l'index `i` (ajusté uniquement pour les caractères alphabétiques) est pair, nous ajoutons au résultat le caractère converti en minuscule.

```python
if i % 2 == 0:
    result.append(char.lower())
```

Si l'index est impair, nous ajoutons au résultat le caractère converti en majuscule.

```python
else:
    result.append(char.upper())
```

Après avoir traité un caractère alphabétique, l'index `i` est incrémenté.

Dans le cas de caractères non alphabétiques, nous les ajoutons à la liste de résultats tels qu'ils apparaissent, sans alterner leur casse.

Après que tous les caractères ont été traités, nous les combinons à nouveau en une chaîne en utilisant `join`.

```python
return "".join(result)

```

## Défis Python #7 : Chiffrement de César

Le chiffrement de César (également connu sous le nom de chiffre de César) est une technique de chiffrement simple qui fonctionne en décalant les lettres du message en clair d'un certain nombre de positions.

Le défi : Créer une fonction qui a deux paramètres – une chaîne à encoder et un entier représentant le nombre de positions dont chaque lettre doit être décalée.

Voici la solution de code :

```python
def caesar_encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

```

### Explication du code :

Nous définissons une fonction `caesar_encryption` qui prend deux paramètres : une chaîne `text` et un entier `shift`.

Ensuite, nous initialisons une chaîne vide pour accumuler les caractères encodés.

```python
result = ""
```

Ensuite, nous parcourons chaque caractère dans la chaîne de texte d'entrée.

Pour les caractères alphabétiques, nous calculons le nouveau caractère après avoir appliqué le décalage.

Ensuite, nous ajoutons les caractères non alphabétiques comme les nombres au résultat sans changement.

```python
for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
    shifted = (ord(char) - start + shift) % 26 + start
```

Alors, comment calculons-nous le nouveau caractère ?

Nous déterminons la valeur ASCII de 'A' pour les majuscules ou 'a' pour les minuscules.

Tout d'abord, convertissez le caractère en son code ASCII, normalisez-le à une plage de 0-25 en soustrayant le début et en ajoutant le décalage, puis enveloppez-le en utilisant modulo 26 pour vous assurer qu'il reste dans les limites de l'alphabet.

Enfin, nous ajoutons le début pour le mapper à la plage ASCII correcte.

Convertissez la valeur décalée en un caractère en utilisant `chr()` et ajoutez-la au résultat.

```python
result += chr(shifted)
```

Après que tous les caractères ont été traités, retournez la chaîne encodée.

```python
return result
```

## Défis Python #8 : Le produit est-il divisible par la somme ?

Le défi : Créer une fonction qui prend une liste d'entiers et retourne si le produit de ces entiers est divisible par leur somme ou non.

La fonction doit retourner `True` si le produit de tous les entiers dans la liste est divisible par leur somme et `False` sinon.

Voici la solution de code :

```python
def is_product_divisible_by_sum(numbers):
    if not numbers:
        return False
    
    product = 1
    summation = 0
    for num in numbers:
        product *= num
        summation += num

    if summation == 0:
        return False

    return product % summation == 0

```

### Explication du code :

Tout d'abord, nous définissons une fonction `is_product_divisible_by_sum`, qui prend une liste d'entiers, `numbers`, en tant que paramètre.

Ensuite, nous vérifions si la liste d'entrée `numbers` est vide. Si elle est vide, nous retournons `False`.

```python
if not numbers:
    return False
```

Sinon, nous initialisons deux variables : `product` à `1` et `summation` à `0`.

```python
product = 1
summation = 0
```

Nous itérons sur chaque nombre dans la liste pour calculer le produit total et la somme de tous les nombres dans la liste.

```python
for num in numbers:
    product *= num
    summation += num
```

Après avoir calculé la somme, nous vérifions si la somme est nulle. Diviser par zéro est indéfini en mathématiques et provoquerait une erreur en programmation, donc nous retournons `False`.

```python
if summation == 0:
    return False
```

Enfin, nous vérifions si le produit est divisible par la somme en utilisant l'opérateur modulo `%`.

Ici, si le reste est zéro, c'est-à-dire que le produit est parfaitement divisible par la somme, nous retournons `True`. Sinon, nous retournons `False`.

```python
return product % summation == 0
```

## Conclusion

Ce ne sont là que quelques défis qui peuvent vous aider à développer vos compétences en résolution de problèmes. Je vous suggère d'essayer ces défis par vous-même.

Si vous souhaitez résoudre plus de défis, vous pouvez essayer les plateformes suivantes :

* [Leetcode](https://leetcode.com/)
* [Programiz PRO Community Challenges](https://app.programiz.pro/community-challenges)
* Exercism

Ils sont gratuits et vous aident à développer vos compétences logiques avec une expérience pratique.

Bon codage !