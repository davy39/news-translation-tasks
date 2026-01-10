---
title: Compréhension de dictionnaire en Python – Expliquée avec des exemples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-08-24T17:34:03.000Z'
originalURL: https://freecodecamp.org/news/dictionary-comprehension-in-python-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/dict_comprehension.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Compréhension de dictionnaire en Python – Expliquée avec des exemples
seo_desc: 'Dictionaries are powerful built-in data structures in Python that store
  data as key-value pairs. Dictionary Comprehension can be super helpful in creating
  new dictionaries from existing dictionaries and iterables.

  In this tutorial, we''ll learn how di...'
---

Les dictionnaires sont des structures de données intégrées puissantes en Python qui stockent les données sous forme de paires clé-valeur. La compréhension de dictionnaire peut être très utile pour créer de nouveaux dictionnaires à partir de dictionnaires et d'itérables existants.

Dans ce tutoriel, nous allons apprendre comment fonctionnent les compréhensions de dictionnaire en Python en codant quelques exemples simples.

## Qu'est-ce qu'un dictionnaire en Python ?

Les dictionnaires en Python nous permettent de stocker une série de _mappages_ entre deux ensembles de valeurs, à savoir, les _clés_ et les _valeurs_.

* Tous les éléments du dictionnaire sont enfermés dans une paire d'accolades `{}`.
* Chaque élément d'un dictionnaire est un mappage entre une clé et une valeur - appelé une paire _clé-valeur_.
* Une paire clé-valeur est souvent appelée un élément de dictionnaire.
* Vous pouvez accéder à ces valeurs en utilisant les clés respectives.

Voici un exemple générique d'un dictionnaire :

```
my_dict = {"key1":<value1>,"key2":<value2>,"key3":<value3>,"key4":<value4>}
```

Dans l'exemple ci-dessus,

* Le dictionnaire `my_dict` contient 4 paires clé-valeur (éléments).
* `"key1"` à `"key4"` sont les 4 clés.
* Vous pouvez utiliser `my_dict["key1"]` pour accéder à `<value1>`, `my_dict["key2"]` pour accéder à `<value2>`, et ainsi de suite.

Maintenant que nous savons ce qu'est un dictionnaire Python, passons à l'apprentissage de la _compréhension de dictionnaire_.

## Comment utiliser la compréhension de dictionnaire pour créer un dictionnaire Python à partir d'un itérable

Dans cette section, utilisons la compréhension de dictionnaire pour créer un dictionnaire Python à partir d'un itérable, par exemple, une liste ou un tuple.

Nous pouvons créer un nouveau dictionnaire Python en utilisant un seul itérable si nous choisissons de générer soit les clés, soit les valeurs à la volée.

> Lorsque nous choisissons de générer les valeurs à la volée, nous pouvons utiliser les éléments de l'itérable comme clés et vice versa.

La syntaxe générale est présentée ci-dessous. Veuillez noter que les noms entre <> sont des espaces réservés pour les noms de variables réels.

```
<dict_name> = {<new_key>:<new_value> for <item> in <iterable>}
```

Analysons la syntaxe ci-dessus.

* `{}` indique que nous peuplons un dictionnaire.
* Pour chaque élément de l'itérable, nous générons une paire clé-valeur dans le dictionnaire.

➡️ Il est temps pour un exemple rapide.

## Compréhension de dictionnaire Python - Exemple 1

Supposons que nous avons une liste de clients qui visitent notre magasin, et nous aimerions offrir une réduction aléatoire à chaque client. Nous aimerions que la valeur de la réduction soit comprise entre 1 $ et 100 $.

> En Python, `random.randint(i,j)` retourne un entier aléatoire entre `i` et `j`, où les deux points de fin sont inclus.

Ainsi, nous pouvons utiliser la fonction `randint()` du module random de Python pour générer une réduction entre 1 $ et 100 $ pour chaque client de notre liste.

L'extrait de code suivant montre comment nous pouvons créer `discount_dict`, un nouveau dictionnaire, à partir de la liste de clients.

```python
import random
customers = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
discount_dict = {customer:random.randint(1,100) for customer in customers}
print(discount_dict)

#Output

{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}
```

L'exemple ci-dessus fait ce qui suit :

* Parcourt la liste des clients (`customers`),
* Utilise le nom de chaque client comme clé, et
* Génère une réduction aléatoire entre 1 $ et 100 $ comme valeur contre la clé.

## Comment utiliser la compréhension de dictionnaire pour créer un dictionnaire Python à partir de deux itérables

Que se passe-t-il si nous avons déjà des itérables prédéfinis qui contiennent les clés et les valeurs ? Supposons que vous avez deux listes, `list_1` et `list_2` – avec `list_1` contenant les _clés_ et `list_2` contenant les _valeurs_ correspondantes.

Nous pouvons maintenant utiliser la fonction `zip()` de Python pour ziper ces deux listes afin de générer les paires clé-valeur.

> Note : La fonction `zip` prend une séquence d'itérables comme argument et retourne un itérateur de tuples, comme montré dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-95.png)

Ainsi, le premier tuple est la première paire clé-valeur, le deuxième tuple est la deuxième paire clé-valeur, et en général, le i-ème tuple est la i-ème paire clé-valeur.

Dans ce cas, la compréhension de dictionnaire prend la forme suivante :

```
<dict_name> = {<new_key>:<new_value> for (key,value) in zip(list1,list2)}
```

L'analyse de la syntaxe ci-dessus est assez simple.

* Les clés et les valeurs sont disponibles sous forme de tuples, car nous les avons zippées ensemble en utilisant la fonction `zip()`.
* Maintenant, nous parcourons cet itérateur de tuples pour obtenir les paires clé-valeur de notre dictionnaire.

➡️ Il est temps pour un autre exemple rapide.

## Compréhension de dictionnaire Python - Exemple 2

Supposons que nous aimerions créer un dictionnaire des températures hebdomadaires dans notre ville. Les jours doivent être les clés, et les températures (en Celsius) correspondant aux jours doivent être les valeurs.

Supposons que nous avons les jours et les températures dans deux listes comme montré ci-dessous.

```python
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
```

Nous pouvons maintenant procéder à l'utilisation de la compréhension de dictionnaire pour créer un dictionnaire des températures hebdomadaires.

```python
# Creating a dictionary of weekly tempertaures
# from the list of temperatures and days

weekly_temp = {day:temp for (day,temp) in zip(days,temp_C)}

print(weekly_temp)

# Output
{'Sunday': 30.5, 'Monday': 32.6, 'Tuesday': 31.8, 'Wednesday': 33.4, 'Thursday': 29.8, 'Friday': 30.2, 'Saturday': 29.9}
```

Dans l'exemple ci-dessus, nous avons utilisé la fonction `zip()` pour ziper ensemble les listes de jours et de températures. Nous pouvons maintenant accéder au dictionnaire en utilisant n'importe quel jour comme clé pour obtenir la température de ce jour, comme montré ci-dessous :

```python
weekly_temp["Thursday"]
# Output
29.8
```

## Comment utiliser la méthode items() sur un dictionnaire Python

Jusqu'à présent, nous avons vu comment utiliser les clés pour accéder aux valeurs. Comment accéder à toutes les paires clé-valeur dans le dictionnaire ?

Pour ce faire, nous pouvons appeler la méthode `items()` sur le dictionnaire pour obtenir toutes les paires clé-valeur, comme montré dans l'extrait de code ci-dessous.

```python
discount_dict.items()

# Output
dict_items([('Alex', 16), ('Bob', 26), ('Carol', 83), ('Dave', 21), ('Flow', 38), ('Katie', 47), ('Nate', 89)])
```

## Comment utiliser la compréhension de dictionnaire pour créer un dictionnaire Python à partir d'un dictionnaire existant

Supposons que nous avons déjà un dictionnaire Python. 📚

Cependant, nous aimerions créer un _nouveau_ dictionnaire qui ne contient que les éléments de notre dictionnaire qui satisfont une condition particulière. La compréhension de dictionnaire peut être très pratique pour cela.

```
<dict_name> = {<new_key>:<new_value> for (key,value) in <dict>.items() if <condition>}
```

Analysons la syntaxe ci-dessus. Nous utilisons la méthode `items()` et obtenons toutes les paires clé-valeur dans un dictionnaire existant.

* Nous accédons au premier élément du dictionnaire et vérifions si la `condition` évalue à `True`.
* Si la condition est `True`, nous ajoutons le premier élément à notre nouveau dictionnaire.
* Nous répétons ensuite ces étapes pour tous les éléments du dictionnaire existant.

➡️ Prenons un exemple pour voir comment cela fonctionne.

## Compréhension de dictionnaire Python - Exemple 3

Développons l'exemple précédent de réduction où nous avons créé le dictionnaire `discount_dict`. Regardons à nouveau notre dictionnaire `discount_dict`.

```python
{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}

```

Nous voyons que certains clients ont eu la chance d'obtenir une réduction plus élevée que les autres. Adressons cette disparité et rendons tous nos clients heureux. 😀

Nous aimerions maintenant offrir aux clients qui ont reçu une réduction inférieure à 30 $, une réduction de 10 % sur leur prochain achat. ✨

Dans ce cas, nous créons un nouveau dictionnaire `customer_10` à partir de notre dictionnaire `discount_dict`.

```python
customer_10 = {customer:discount for (customer, discount) in discount_dict.items() if discount<30}

print(customer_gifts)

# Output
{'Alex': 16, 'Bob': 26, 'Dave': 21}
```

Le code ci-dessus fait ce qui suit :

* Pour chaque élément de notre `discount_dict`, il accède à la valeur de la réduction.
* Si la réduction est inférieure à 30 $, il ajoute la paire `customer:discount` correspondante à notre nouveau dictionnaire `customer_10`.

Remarquez comment `Alex`, `Bob` et `Dave` qui ont obtenu une réduction inférieure à 30 $ ont été ajoutés au nouveau dictionnaire.

## Conclusion

Récapitulons ce que nous avons appris dans ce tutoriel. Nous avons vu comment utiliser la compréhension de dictionnaire pour créer des dictionnaires Python à partir de :

* un seul itérable,
* deux itérables, et
* un dictionnaire existant en utilisant des conditions pour filtrer les éléments.

Merci d'avoir lu. Bon apprentissage ! 🎉

### Articles connexes

Voici un article expliquant le fonctionnement de la [fonction zip() de Python](https://www.freecodecamp.org/news/the-zip-function-in-python-explained-with-examples/).