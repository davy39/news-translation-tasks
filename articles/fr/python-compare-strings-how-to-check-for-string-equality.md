---
title: Comparer des chaînes en Python – Comment vérifier l'égalité des chaînes
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-18T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/python-compare-strings-how-to-check-for-string-equality
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/compare1.jpg
tags:
- name: Python
  slug: python
seo_title: Comparer des chaînes en Python – Comment vérifier l'égalité des chaînes
seo_desc: "When crafting the logic in your code, you may want to execute different\
  \ commands depending on the similarities or differences between two or more strings.\
  \ \nIn this article, we'll see various operators that can help us check if strings\
  \ are equal or no..."
---

Lors de l'élaboration de la logique de votre code, vous souhaiterez peut-être exécuter différentes commandes en fonction des similitudes ou des différences entre deux ou plusieurs chaînes de caractères.

Dans cet article, nous verrons divers opérateurs qui peuvent nous aider à vérifier si des chaînes sont égales ou non. Si deux chaînes sont égales, la valeur renvoyée sera `True`. Sinon, elle renverra `False`.

## Comment vérifier l'égalité des chaînes en Python

Dans cette section, nous verrons des exemples de comparaison de chaînes à l'aide de quelques opérateurs.

Mais avant cela, vous devez garder à l'esprit les points suivants :

* Les comparaisons sont sensibles à la casse. **G** n'est pas la même chose que **g**.
* Chaque caractère d'une chaîne a une [valeur ASCII](https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/) (American Standard Code for Information Interchange), ce que les opérateurs recherchent, et non le caractère lui-même. Par exemple, **G** a une valeur ASCII de 71 alors que **g** a une valeur de 103. Lorsqu'ils sont comparés, **g** devient supérieur à **G**.

### Comment comparer des chaînes à l'aide de l'opérateur `==`

L'opérateur `==` vérifie si deux chaînes sont égales. Voici un exemple :

```python
print("Hello" == "Hello")
# True
```

Nous avons obtenu une valeur `True` car les deux chaînes ci-dessus sont égales.

Rendons cela un peu plus élégant en utilisant une logique conditionnelle :

```python
string1 = "Hello"
string2 = "Hello"

if string1 == string2:
    print("Les deux chaînes sont égales")
else:
    print("Les deux chaînes ne sont pas égales")
    
# Les deux chaînes sont égales
```

Dans le code ci-dessus, nous avons créé deux chaînes et les avons stockées dans des variables. Nous avons ensuite comparé leurs valeurs. Si ces valeurs sont les mêmes, un message s'affiche dans la console, et si elles ne sont pas les mêmes, un message différent s'affiche.

Dans notre cas, les deux chaînes étaient égales, donc "Les deux chaînes sont égales" a été affiché. Si nous avions changé la première chaîne en "hello", nous aurions eu un message différent.

Notez que l'utilisation de `=` amènerait l'interpréteur à supposer que vous voulez affecter une valeur à une autre. Assurez-vous donc d'utiliser `==` pour la comparaison.

### Comment comparer des chaînes à l'aide de l'opérateur `!=`

L'opérateur `!=` vérifie si deux chaînes ne sont **pas** égales.

```python
string1 = "Hello"
string2 = "Hello"

if string1 != string2:
    print("Les deux chaînes ne sont pas égales") # retourne si vrai
else:
    print("Les deux chaînes sont égales") # retourne si faux
    
# Les deux chaînes sont égales
```

Nous utilisons le même exemple mais avec un opérateur différent. Le `!=` indique que les chaînes ne sont pas égales, ce qui est `False`, donc un message est imprimé en fonction de ces conditions.

J'ai commenté le code pour vous aider à mieux comprendre.

### Comment comparer des chaînes à l'aide de l'opérateur `<`

L'opérateur `<` vérifie si une chaîne est plus petite qu'une autre.

```python
print("Hello" < "hello")

# True
```

Cela renvoie `True` car même si tous les autres index de caractères dans les deux chaînes sont égaux, **H** a une valeur (ASCII) plus petite que **h**.

Nous pouvons également utiliser des instructions conditionnelles ici comme nous l'avons fait dans les sections précédentes.

### Comment comparer des chaînes à l'aide de l'opérateur `<=`

L'opérateur `<=` vérifie si une chaîne est inférieure ou égale à une autre chaîne.

```python
print("Hello" <= "Hello")

# True
```

Rappelez-vous que cet opérateur vérifie deux choses – si une chaîne est inférieure ou si les deux chaînes sont identiques – et renverra `True` si l'une ou l'autre est vraie.

Nous avons obtenu `True` parce que les deux chaînes sont égales.

### Comment comparer des chaînes à l'aide de l'opérateur `>`

L'opérateur `>` vérifie si une chaîne est plus grande qu'une autre chaîne.

```python
print("Hello" > "Hello")

# False
```

Comme la chaîne de gauche n'est pas plus grande que celle de droite, nous avons obtenu un retour `False`.

### Comment comparer des chaînes à l'aide de l'opérateur `>=`

L'opérateur `>=` vérifie si une chaîne est supérieure ou égale à une autre chaîne.

```python
print("Hello" >= "Hello")

# True
```

Puisque l'une des deux conditions de l'opérateur est vraie (les deux chaînes sont égales), nous avons obtenu une valeur `True`.

## Conclusion

Dans cet article, nous avons découvert les différents opérateurs que vous pouvez utiliser pour vérifier l'égalité des chaînes en Python avec des exemples. Nous avons également vu comment la sensibilité à la casse peut modifier l'égalité des chaînes.

Bon codage !