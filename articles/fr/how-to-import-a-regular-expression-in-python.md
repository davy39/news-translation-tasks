---
title: Python RegEx – Comment importer une expression régulière en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-01T17:28:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-import-a-regular-expression-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/regexpy.png
tags:
- name: Python
  slug: python
- name: Regex
  slug: regex
seo_title: Python RegEx – Comment importer une expression régulière en Python
seo_desc: 'Virtually all the programming languages out there support regular expressions.
  Regex is built into languages like JavaScript and Pearl, while others like Java
  and Python have standard libraries for working with it.

  In this article, we’ll look at how ...'
---

Presque tous les langages de programmation supportent les expressions régulières. Regex est intégré dans des langages comme JavaScript et Perl, tandis que d'autres comme Java et Python ont des bibliothèques standard pour travailler avec.

Dans cet article, nous verrons comment importer des expressions régulières en Python et les utiliser. Nous examinerons également quelques méthodes que Python fournit pour travailler avec les expressions régulières.

## Ce que nous allons couvrir
- [Comment importer des expressions régulières en Python](#heading-comment-importer-des-expressions-regulieres-en-python)
- [Comment utiliser le module `re` de Python avec RegEx](#heading-comment-utiliser-le-module-re-de-python-avec-regex)
  - [Exemple RegEx avec la méthode `match()`](#regexexampleaveclemethodematch)
  - [Exemple RegEx avec la méthode `search()`](#regexexampleaveclemethodesearch)
  - [Exemple RegEx avec la méthode `findall()`](#regexexampleaveclemethodefindall)
  - [Exemple RegEx avec la méthode `split()`](#regexexampleaveclemethodesplit)
  - [Exemple RegEx avec la méthode `sub()`](#regexexampleaveclemethodesub)
- [Conclusion](#heading-conclusion)

## Comment importer des expressions régulières en Python

Python fournit le module `re` pour utiliser les expressions régulières. Il s'agit d'un module standard intégré à Python, donc si vous avez la dernière version de Python, vous n'avez pas besoin de l'installer séparément avec des gestionnaires de paquets.

Pour importer le module `re` en Python, vous le faites avec le mot-clé import :

```py
import re
```

## Comment utiliser le module `re` de Python avec RegEx

Python fournit certaines méthodes que vous pouvez utiliser pour travailler avec des expressions régulières telles que `match()`, `search()`, `findall()`, `split()`, et `sub()`.

Pour utiliser ces méthodes avec RegEx, vous devez les préfixer avec le module `re` et un point (`.`) comme ceci :

```py
re.match(pattern, string) # pour utiliser la méthode match
re.findall(pattern, string) # pour utiliser la méthode findall
re.sub(pattern, string) # pour utiliser la méthode sub
re.search(pattern, string) # pour utiliser la méthode search
re.split(pattern, string) # pour utiliser la méthode split
```

Les exemples RegEx que j'ai fournis utiliseront ces méthodes.

### Exemple RegEx utilisant la méthode `match()`

La méthode `match()` prend une expression régulière et la chaîne, puis vérifie si la chaîne correspond au motif de l'expression régulière.

Voici un exemple :

```py
import re

my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt)
print(res) # retourne None
```

Dans l'exemple ci-dessus :
- J'ai une variable `my_txt` définie sur `freeCodeCamp` et une variable `my_regex_1` définie sur le motif `^freecodecamp$`. C'est ainsi que vous écrivez des expressions régulières en Python — vous les mettez entre guillemets.
- Pour vérifier si le texte correspond au motif, j'ai utilisé la méthode `match()` et j'ai mis les variables `my_regex_1` et `my_txt`.

La chaîne est `freeCodeCamp`, et le motif est `^freecodecamp$`, alors pourquoi la méthode match a-t-elle retourné `None` ? C'est parce qu'elle ne trouve pas de correspondance.

Il y a des lettres majuscules dans la variable `my_txt`, mais le motif recherche des lettres minuscules.

Si vous êtes familier avec RegEx en JavaScript ou Perl, vous pouvez utiliser le drapeau `i` pour correspondre à toutes les lettres majuscules ou minuscules dans une chaîne.

Donc, ce que nous devons faire pour avoir une correspondance est d'utiliser le drapeau `i`. Mais l'utilisation d'un drapeau avec les expressions régulières en Python est différente de la manière dont nous l'utilisons en JavaScript.

Pour utiliser des drapeaux avec les expressions régulières en Python, le module `re` fournit les options `IGNORECASE`, `ASCII`, `MULTILINE`, `VERBOSE`, `DOTALL`, et `LOCALE`.

Voici comment vous utiliseriez un drapeau avec les expressions régulières en Python :

```py
re.match(pattern, string, re.ASCII) # pour effectuer uniquement une correspondance ASCII
re.findall(pattern, string, re.DOTALL) # pour correspondre à n'importe quel caractère — y compris une nouvelle ligne.
re.sub(pattern, string, re.IGNORECASE) # pour effectuer une correspondance insensible à la casse
re.search(pattern, string, re.LOCALE) # pour effectuer une correspondance insensible à la casse dépendant de la locale actuelle
re.search(pattern, string, re.VERBOSE) # pour permettre des commentaires dans regex
re.split(pattern, string, re.MULTILINE) # pour effectuer une correspondance sur plusieurs lignes. Communément utilisé avec des métacaractères (^ et $)
```

Pour notre exemple, le drapeau que nous pouvons utiliser est `IGNORECASE`. Utilisons-le pour obtenir une correspondance :

```py
import re

my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt, re.IGNORECASE)
print(res) # Sortie : <re.Match object; span=(0, 12), match='freeCodeCamp'>
```

Maintenant nous avons une correspondance !

### Exemple RegEx utilisant la méthode `search()`

La fonction `search()` prend une regex et une chaîne, puis retourne la première occurrence dans un objet de correspondance. Si elle ne trouve pas de correspondance, elle retourne `None`.

```py
import re

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

res = re.search(my_regex, my_txt, re.IGNORECASE)
print(res) # <re.Match object; span=(6, 12), match='Friday'>
```

Vous pouvez voir qu'elle retourne la première occurrence du texte `Friday`, située entre l'index `6` et `12`.

Vous pouvez obtenir cet index avec la méthode `start()` :

```py
res = re.search(my_regex, my_txt, re.IGNORECASE)
print("La première occurrence est située à l'index", res.start()) # La première occurrence est située à l'index 6
```

Vous pouvez obtenir les index de début et de fin de l'occurrence comme ceci :

```py
res = re.search(my_regex, my_txt, re.IGNORECASE)
print("La première occurrence est située entre l'index", res.start(), "et l'index", res.end()) # La première occurrence est située entre l'index 6 et l'index 12
```

Vous pouvez également utiliser `match()` avec une instruction `if...else` :

```py
import re

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

if re.search(my_regex, my_txt, re.IGNORECASE):
    print("Correspondance trouvée !") # Sortie : Correspondance trouvée !
else:
    print("Aucune correspondance trouvée")

res = re.search(my_regex, my_txt, re.IGNORECASE)
```

### Exemple RegEx utilisant la méthode `findall()`

La méthode `findall()` prend une regex et une chaîne, puis parcourt la chaîne et trouve toutes les occurrences qui correspondent à la regex. Elle place toutes ces occurrences à l'intérieur d'une liste.

Voici un exemple :

```py
import re

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'
res = re.findall(my_regex, my_txt, re.IGNORECASE)

print(res) # Sortie : ['Friday', 'Friday', 'Friday', 'Friday']
```

Remarquez que la regex que j'utilise contient le texte `friday`, qui ne correspond à aucune occurrence de « Friday ». Le drapeau `IGNORECASE` est ce qui a permis de correspondre à ces occurrences.

### Exemple RegEx utilisant la méthode `split()`

La méthode `split()` fait ce que le nom implique — elle divise une chaîne par le motif passé. 

Cette méthode pourrait être utile si vous voulez filtrer certains mots que vous ne voulez pas dans une chaîne.

```py
import re

my_txt = "Python and JavaScript and C# and Java and Golang and F#"
my_regex = 'and'

res = re.split(my_regex, my_txt)
print(res) # ['Python ', ' JavaScript ', ' C# ', ' Java ', ' Golang ', ' F#']
```

### Exemple RegEx utilisant la méthode `sub()`

La méthode `sub()` fonctionne comme la méthode `replace()` de JavaScript. Elle remplace le caractère qui correspond à l'expression régulière passée.

La méthode `sub()` est un peu différente des autres méthodes — elle prend jusqu'à 5 paramètres :

```py
re.sub(pattern, replacement, string, count, flags)
```

Donc, si vous voulez spécifier un drapeau mais que vous ne spécifiez pas le `count`, cela ne fonctionnera pas comme prévu.

Personne ne fait de réunion debout le vendredi, alors utilisons la méthode `sub` sur la chaîne que nous avons utilisée pour les exemples `search()` et `findall()` :

```py
import re

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

res = re.sub(my_regex, "Monday", my_txt, 4, re.IGNORECASE)
print(res) # Sortie : Every Monday, we have a standup meeting. The only reason why we might not have a meeting on a Monday is public holiday. That Monday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Monday.
```

Il y a 4 occurrences de `Friday` dans la chaîne `my_txt`. C'est pourquoi j'ai spécifié 4 comme compte.

## Conclusion

Dans cet article, nous avons vu comment importer des expressions régulières via le module `re`. Mais nous ne nous sommes pas arrêtés là, car je vous ai également montré comment utiliser le module avec les méthodes pour travailler avec les expressions régulières en Python.

De plus, nous avons également jeté un bref coup d'œil à l'utilisation des drapeaux dans les expressions régulières Python.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.