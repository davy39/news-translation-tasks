---
title: Python Bytes to String – Comment convertir une chaîne d'octets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-10T22:52:41.000Z'
originalURL: https://freecodecamp.org/news/python-bytes-to-string-how-to-convert-a-bytestring
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Bytes-to-String
seo_title: Python Bytes to String – Comment convertir une chaîne d'octets
---

How-to-Convert-a-Bytestring.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Par Shittu Olumide

  Dans cet article, vous apprendrez à convertir une chaîne d'octets. Je sais que le terme chaîne d'octets
  peut sembler technique et difficile à comprendre. Mais faites-moi confiance – nous allons décomposer
  le processus et comprendre tout ce qui concerne les chaînes d'octets avant d'écrire le code Python qui convertit les octets en une chaîne de caractères.

Alors commençons par définir une chaîne d'octets.

## Qu'est-ce qu'une chaîne d'octets ?

Une chaîne d'octets est une séquence d'octets, qui est un type de données fondamental en informatique. Elles sont généralement représentées à l'aide d'une séquence de caractères, chaque caractère représentant un octet de données.

Les octets sont souvent utilisés pour représenter des informations non basées sur des caractères, telles que des images, de l'audio, de la vidéo ou d'autres types de données binaires.

En Python, une chaîne d'octets est représentée comme une séquence d'octets, qui peut être encodée en utilisant divers encodages de caractères tels que UTF-8, ASCII ou Latin-1. Elle peut être créée en utilisant les fonctions `bytes()` ou `bytearray()`, et peut être convertie en chaînes de caractères et vice versa en utilisant les méthodes `encode()` et `decode()`.

Notez que dans Python 3.x, les chaînes d'octets et les chaînes de caractères sont des types de données distincts et ne peuvent pas être utilisés de manière interchangeable sans encodage ou décodage.

Cela est dû au fait que Python 3.x utilise l'encodage Unicode pour les chaînes de caractères par défaut, alors que les versions précédentes de Python utilisaient l'encodage ASCII. Ainsi, lors de la manipulation de chaînes d'octets dans Python 3.x, il est important d'être conscient de l'encodage utilisé et d'encoder et de décoder correctement les données selon les besoins.

## Comment convertir des octets en une chaîne de caractères en Python

Maintenant que nous avons une compréhension de base de ce qu'est une chaîne d'octets, voyons comment nous pouvons convertir des octets en une chaîne de caractères en utilisant les méthodes, constructeurs et modules Python.

### Utilisation de la méthode `decode()`

`decode()` est une méthode que vous pouvez utiliser pour convertir des octets en une chaîne de caractères. Elle est couramment utilisée lors de la manipulation de données textuelles encodées dans un encodage de caractères spécifique, tel que UTF-8 ou ASCII. Elle fonctionne simplement en prenant une chaîne d'octets encodée en entrée et en retournant une chaîne décodée.

Syntaxe :

```py
chaine_decodee = chaine_octets.decode(encodage)

```

Où `chaine_octets` est la chaîne d'octets d'entrée que nous voulons décoder et `encodage` est l'encodage de caractères utilisé par la chaîne d'octets.

Voici un exemple de code qui montre comment utiliser la méthode `decode()` pour convertir une chaîne d'octets en une chaîne de caractères :

```py
# Définir une chaîne d'octets
chaine_octets = b"hello world"

# Convertir la chaîne d'octets en une chaîne de caractères en utilisant la méthode decode()
chaine_decodee = chaine_octets.decode("utf-8")

# Afficher la chaîne décodée
print(chaine_decodee)

```

Dans cet exemple, nous définissons une chaîne d'octets `b"hello world"` et la convertissons en une chaîne de caractères en utilisant la méthode `decode()` avec l'encodage de caractères UTF-8. La chaîne décodée résultante est `"hello world"`, qui est ensuite affichée dans la console.

Notez que la méthode `decode()` peut également prendre des paramètres supplémentaires, tels que `errors` et `final`, pour contrôler la manière dont les erreurs de décodage sont gérées et si le décodeur doit s'attendre à plus d'entrée.

### Utilisation du constructeur `str()`

Vous pouvez utiliser le constructeur `str()` en Python pour convertir une chaîne d'octets (objet bytes) en un objet chaîne de caractères. Cela est utile lorsque nous travaillons avec des données qui ont été encodées dans un format de chaîne d'octets, comme lors de la lecture de données à partir d'un fichier ou de la réception de données via une socket réseau.

Le constructeur `str()` prend un seul argument, qui est la chaîne d'octets que nous voulons convertir en une chaîne de caractères. Si la chaîne d'octets n'est pas un ASCII ou UTF-8 valide, nous devrons spécifier le format d'encodage en utilisant le paramètre `encoding`.

Exemple :

```py
# Définir une chaîne d'octets
chaine_octets = b"Hello, world!"

# Convertir la chaîne d'octets en une chaîne de caractères en utilisant le constructeur str()
chaine = str(chaine_octets, encoding='utf-8')

# Afficher la chaîne de caractères
print(chaine)

```

Sortie :

```bash
Hello, world!

```

Dans cet exemple, nous définissons une chaîne d'octets `b"Hello, world!"` et utilisons le constructeur `str()` pour la convertir en un objet chaîne de caractères. Nous spécifions le format d'encodage comme `utf-8` en utilisant le paramètre `encoding`. Enfin, nous affichons la chaîne résultante dans la console.

### Utilisation du constructeur `bytes()`

Nous pouvons également utiliser le constructeur `bytes()`, une fonction intégrée de Python utilisée pour créer un nouvel objet `bytes`. Il prend un itérable d'entiers en entrée et retourne un nouvel objet `bytes` qui contient les octets correspondants. Cela est utile lorsque nous travaillons avec des données binaires, ou lors de la conversion entre différents types de données qui utilisent des octets comme représentation sous-jacente.

Exemple :

```py
# Définir une chaîne de caractères
chaine = "Hello, world!"

# Convertir la chaîne de caractères en un objet bytes
objet_bytes = bytes(chaine, 'utf-8')

# Afficher l'objet bytes
print(objet_bytes)

# Convertir l'objet bytes en une chaîne de caractères
chaine_decodee = objet_bytes.decode('utf-8')

# Afficher la chaîne décodée
print(chaine_decodee)

```

Sortie :

```bash
b'Hello, world!'
Hello, world!

```

Dans cet exemple, nous commençons par définir une variable de chaîne `chaine`. Nous utilisons ensuite le constructeur `bytes()` pour convertir la chaîne en un objet bytes, en passant la chaîne et l'encodage (`utf-8`) comme arguments. Nous affichons l'objet bytes résultant dans la console.

Ensuite, nous utilisons la méthode `decode()` pour convertir l'objet bytes en une chaîne de caractères, en passant le même encodage (`utf-8`) qu'auparavant. Nous affichons également la chaîne décodée dans la console.

### Utilisation du module `codecs`

Le module `codecs` en Python fournit un moyen de convertir des données entre différents encodages, tels que entre des chaînes d'octets et des chaînes Unicode. Il contient un certain nombre de classes et de fonctions que vous pouvez utiliser pour effectuer diverses opérations d'encodage et de décodage.

Pour pouvoir convertir des octets Python en une chaîne de caractères, nous pouvons utiliser la méthode `decode()` fournie par le module `codecs`. Cette méthode prend deux arguments : le premier est la chaîne d'octets que nous voulons décoder, et le second est l'encodage que nous voulons utiliser.

Exemple :

```py
import codecs

# chaîne d'octets à convertir
chaine_octets = b'\xc3\xa9\xc3\xa0\xc3\xb4'

# décodage de la chaîne d'octets en chaîne Unicode
chaine_unicode = codecs.decode(chaine_octets, 'utf-8')

print(chaine_unicode)

```

Sortie :

```bash
éàô

```

Dans cet exemple, nous avons une chaîne d'octets `chaine_octets` qui contient certains caractères non-ASCII. Nous utilisons la méthode `codecs.decode()` pour convertir cette chaîne d'octets en une chaîne Unicode.

Le premier argument de cette méthode est la chaîne d'octets à décoder, et le second argument est l'encodage utilisé dans la chaîne d'octets (dans ce cas, il s'agit de `utf-8`). La chaîne Unicode résultante est stockée dans `chaine_unicode`.

Pour convertir une chaîne Unicode en une chaîne d'octets en utilisant le module `codecs`, nous utilisons la méthode `encode()`. Voici un exemple :

```py
import codecs

# chaîne Unicode à convertir
chaine_unicode = 'This is a test.'

# encodage de la chaîne Unicode en chaîne d'octets
chaine_octets = codecs.encode(chaine_unicode, 'utf-8')

print(chaine_octets)

```

Sortie :

```bash
b'This is a test.'

```

Dans cet exemple, nous avons une chaîne Unicode `chaine_unicode`. Nous utilisons la méthode `codecs.encode()` pour convertir cette chaîne Unicode en une chaîne d'octets. Le premier argument de cette méthode est la chaîne Unicode à encoder, et le second argument est l'encodage à utiliser pour la chaîne d'octets (dans ce cas, il s'agit de `utf-8`). La chaîne d'octets résultante est stockée dans `chaine_octets`.

## Conclusion

Comprendre les chaînes d'octets et la conversion de chaînes de caractères est important car c'est un aspect fondamental de la manipulation des données textuelles dans n'importe quel langage de programmation.

En Python, cela est particulièrement pertinent en raison de la popularité croissante des applications de science des données et de traitement du langage naturel, qui impliquent souvent la manipulation de grandes quantités de données textuelles.

Pour aller plus loin, consultez ces ressources utiles :

1. [La différence entre bytes et str en Python](https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string)
2. [Ce que tout développeur devrait savoir sur l'encodage](https://www.freecodecamp.org/news/everything-you-need-to-know-about-encoding/)
3. [Documentation Python sur le module codecs](https://docs.python.org/3/library/codecs.html)
4. [Documentation Python sur les méthodes bytes](https://docs.python.org/3/library/stdtypes.html#bytes-methods)
5. [Documentation Python sur les méthodes string](https://docs.python.org/3/library/stdtypes.html#string-methods)

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !