---
title: Python String.Replace() – Fonction en Python pour la substitution de sous-chaînes
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-24T16:59:25.000Z'
originalURL: https://freecodecamp.org/news/python-string-replace-function-in-python-for-substring-substitution
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/sarah-dorweiler-QeVmJxZOv3k-unsplash-1.jpg
tags:
- name: Python
  slug: python
seo_title: Python String.Replace() – Fonction en Python pour la substitution de sous-chaînes
seo_desc: 'In this article you''ll see how to use Python''s .replace() method to perform
  substring substiution.

  You''ll also see how to perform case-insensitive substring substitution.

  Let''s get started!

  What does the .replace() Python method do?

  When using the .r...'
---

Dans cet article, vous verrez comment utiliser la méthode `.replace()` de Python pour effectuer une substitution de sous-chaînes.

Vous verrez également comment effectuer une substitution de sous-chaînes insensible à la casse.

Commençons !

## Que fait la méthode `.replace()` de Python ?

Lorsque vous utilisez la méthode `.replace()` de Python, vous pouvez remplacer chaque instance d'un caractère spécifique par un nouveau. Vous pouvez même remplacer une chaîne de texte entière par une nouvelle ligne de texte que vous spécifiez.

La méthode `.replace()` retourne une copie d'une chaîne. Cela signifie que l'ancienne sous-chaîne reste la même, mais une nouvelle copie est créée – avec tout le texte ancien ayant été remplacé par le nouveau texte.

### Comment fonctionne la méthode `.replace()` de Python ? Une analyse de la syntaxe

La syntaxe de la méthode `.replace()` ressemble à ceci :

```python
string.replace(old_text, new_text, count)
```

Décomposons-la :

- `old_text` est le premier paramètre requis que `.replace()` accepte. C'est l'ancien caractère ou texte que vous souhaitez remplacer. Enclosez ceci entre guillemets.
- `new_text` est le deuxième paramètre requis que `.replace()` accepte. C'est le nouveau caractère ou texte avec lequel vous souhaitez remplacer l'ancien caractère/texte. Ce paramètre doit également être enfermé entre guillemets.
- `count` est le *troisième* paramètre *optionnel* que `.replace()` accepte. Par défaut, `.replace()` remplacera **toutes** les instances de la sous-chaîne. Cependant, vous pouvez utiliser `count` pour spécifier le nombre d'occurrences que vous souhaitez remplacer.

## Exemples de code de la méthode `.replace()` de Python

### Comment remplacer toutes les instances d'un seul caractère

Pour changer **toutes** les instances d'un seul caractère, vous feriez ce qui suit :

```python
phrase = "I like to learn coding on the go"

# remplacer toutes les instances de 'o' par 'a'
substituted_phrase = phrase.replace("o", "a")

print(phrase)
print(substituted_phrase)

#output

#I like to learn coding on the go
#I like ta learn cading an the ga
```

Dans l'exemple ci-dessus, chaque mot contenant le caractère `o` est remplacé par le caractère `a`.

Dans cet exemple, il y avait quatre instances du caractère `o`. Plus précisément, il a été trouvé dans les mots `to`, `coding`, `on`, et `go`.

Et si vous vouliez changer seulement deux mots, comme `to` et `coding`, pour contenir `a` au lieu de `o` ?

### Comment remplacer seulement un certain nombre d'instances d'un seul caractère

Pour changer seulement deux instances d'un seul caractère, vous utiliseriez le paramètre `count` et le définiriez à deux :

```python
phrase = "I like to learn coding on the go"

# remplacer seulement les deux premières instances de 'o' par 'a'
substituted_phrase = phrase.replace("o", "a", 2)

print(phrase)
print(substituted_phrase)

#output

#I like to learn coding on the go
#I like ta learn cading on the go
```

Si vous vouliez changer seulement la première instance d'un seul caractère, vous définiriez le paramètre `count` à un :

```python
phrase = "I like to learn coding on the go"

# remplacer seulement la première instance de 'o' par 'a'
substituted_phrase = phrase.replace("o", "a", 1)

print(phrase)
print(substituted_phrase)

#output

#I like to learn coding on the go
#I like ta learn coding on the go
```

### Comment remplacer toutes les instances d'une chaîne

Pour changer plus d'un caractère, le processus est similaire.

```python
phrase = "The sun is strong today. I don't really like sun."

# remplacer toutes les instances du mot 'sun' par 'wind'
substituted_phrase = phrase.replace("sun", "wind")

print(phrase)
print(substituted_phrase)

#output

#The sun is strong today. I don't really like sun.
#The wind is strong today. I don't really like wind.
```

Dans l'exemple ci-dessus, le mot `sun` a été remplacé par le mot `wind`.

### Comment remplacer seulement un certain nombre d'instances d'une chaîne

Si vous vouliez changer seulement la première instance de `sun` en `wind`, vous utiliseriez le paramètre `count` et le définiriez à un.

```python
phrase = "The sun is strong today. I don't really like sun."

# remplacer seulement la première instance du mot 'sun' par 'wind'
substituted_phrase = phrase.replace("sun", "wind", 1)

print(phrase)
print(substituted_phrase)

#output

#The sun is strong today. I don't really like sun.
#The wind is strong today. I don't really like sun.
```

## Comment effectuer une substitution de sous-chaîne insensible à la casse en Python

Examinons un autre exemple.

```python
phrase = "I am learning Ruby. I really enjoy the ruby programming language!"

# remplacer le texte "Ruby" par "Python"
substituted_text = phrase.replace("Ruby", "Python")

print(substituted_text)

#output

#I am learning Python. I really enjoy the ruby programming language!
```

Dans ce cas, ce que je voulais vraiment faire, c'était remplacer toutes les instances du mot `Ruby` par `Python`.

Cependant, il y avait le mot `ruby` avec un `r` minuscule, que je voudrais également changer.

Parce que la première lettre était en minuscule, et non en majuscule comme je l'ai spécifié avec `Ruby`, elle est restée la même et n'a pas changé en `Python`.

La méthode `.replace()` est *sensible à la casse*, et donc elle effectue une substitution de sous-chaîne sensible à la casse.

Pour effectuer une substitution de sous-chaîne *insensible à la casse*, vous devriez faire quelque chose de différent.

Vous devriez utiliser la fonction `re.sub()` et utiliser le drapeau `re.IGNORECASE`.

Pour utiliser `re.sub()`, vous devez :

- Utiliser le module `re`, via `import re`.
- Spécifier une expression régulière `pattern`.
- Mentionner par quoi vous voulez remplacer le `pattern`.
- Mentionner la `string` sur laquelle vous voulez effectuer cette opération.
- Optionnellement, spécifier le paramètre `count` pour rendre le remplacement plus précis et spécifier le nombre maximum de remplacements que vous voulez effectuer.
- Le drapeau `re.IGNORECASE` indique à l'expression régulière d'effectuer une correspondance insensible à la casse.

Ainsi, la syntaxe ressemble à ceci :

```python
import re

re.sub(pattern, replace, string, count, flags)
```

Prenons l'exemple précédent :

```python
phrase = "I am learning Ruby. I really enjoy the ruby programming language!"
```

Voici comment je remplacerais à la fois `Ruby` et `ruby` par `Python` :

```python
import re

phrase = "I am learning Ruby. I really enjoy the ruby programming language!"

phrase = re.sub("Ruby", "Python", phrase, flags=re.IGNORECASE)

print(phrase)

#output

#I am learning Python. I really enjoy the Python programming language!
```

## Conclusion

Et voilà - vous connaissez maintenant les bases de la substitution de sous-chaînes. J'espère que vous avez trouvé ce guide utile.

Pour en savoir plus sur Python, consultez la [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !