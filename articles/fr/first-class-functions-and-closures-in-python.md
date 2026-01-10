---
title: Fonctions de première classe, fonctions d'ordre supérieur et fermetures en
  Python – Expliqué avec des exemples de code
subtitle: ''
author: Samyak Jain
co_authors: []
series: null
date: '2024-06-17T21:19:47.000Z'
originalURL: https://freecodecamp.org/news/first-class-functions-and-closures-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/first-class-functions-high-order-functions-and-closures-in-python.png
tags:
- name: Python
  slug: python
seo_title: Fonctions de première classe, fonctions d'ordre supérieur et fermetures
  en Python – Expliqué avec des exemples de code
seo_desc: 'In modern programming, it''s important to understand concepts like first-class
  functions, higher-order functions, and closures. These ideas help us write flexible
  and efficient code and serve as building blocks for many advanced coding techniques.

  Fir...'
---

En programmation moderne, il est important de comprendre des concepts comme les fonctions de première classe, les fonctions d'ordre supérieur et les fermetures. Ces idées nous aident à écrire du code flexible et efficace et servent de blocs de construction pour de nombreuses techniques de codage avancées.

Les fonctions de première classe et les fonctions d'ordre supérieur nous permettent de traiter les fonctions comme des citoyens de première classe. Nous étudierons ce qu'elles sont, mais pour l'instant, sachez simplement qu'elles rendent notre code plus puissant et réutilisable. Les fermetures vont plus loin en permettant aux fonctions de se souvenir des variables de leur portée contenante.

Ce tutoriel plongera dans ces concepts et expliquera comment ils s'interconnectent, avec des exemples de codage pratiques pour illustrer leur utilisation.

## **Table des matières**

1. [Fonctions de première classe](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#first-class-functions)  
– [Assignation de fonctions à des variables](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#assigning-functions-to-variables)  
– [Passage de fonctions en tant qu'arguments](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#passing-functions-as-arguments)  
– [Retour de fonctions depuis d'autres fonctions](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#returning-functions-from-other-functions)
2. [Fonctions d'ordre supérieur](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#higher-order-functions)  
– [Fonctions Lambda](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#lambda-functions)  
– [Fonction d'ordre supérieur prenant une fonction comme argument](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#example-a-higher-order-function-that-takes-a-function-as-an-argument-first-class-function-)  
– [Fonction d'ordre supérieur retournant une autre fonction](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#example-a-higher-order-function-that-returns-another-function-first-class-function-)
3. [Fermetures](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#closures)  
– [Fermeture basique (Fonction imbriquée basique avec exécution immédiate)](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#basic-nested-function-with-immediate-execution)  
– [Retour de la fonction interne](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#returning-the-inner-function)  
– [Utilisation de fermetures avec des paramètres](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#using-closures-with-parameters)
4. [Applications réelles](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#real-world-applications-of-closures)
5. [Conclusion](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#conclusion)

Pour bien comprendre les fermetures, il est essentiel de d'abord comprendre les concepts de fonctions de première classe et de fonctions d'ordre supérieur. Ces concepts sont la pierre angulaire de nombreux modèles de programmation avancés et sont fondamentaux pour le fonctionnement des fermetures. Plongeons dans ces concepts et voyons comment ils s'interconnectent.

## **Fonctions de première classe**

En programmation, un langage est dit avoir des fonctions de première classe s'il traite les fonctions comme des citoyens de première classe. Cela signifie que les fonctions dans un tel langage peuvent être :

1. **Assignées à des variables**
2. **Passées comme arguments à d'autres fonctions**
3. **Retournées depuis d'autres fonctions**

En termes plus simples, les fonctions de première classe peuvent être manipulées comme n'importe quelle autre variable ou objet dans le langage. Explorons ces capacités avec quelques exemples de code.

### **Assignation de fonctions à des variables**

Typiquement, nous appelons une fonction et assignons son résultat à une variable. Par exemple :

```python
def add(a, b):
    return a + b

result = add(3, 4)

print(add)  # Affiche l'objet fonction
print(result)  # Affiche 7
```

Ici, `add` est une fonction qui retourne la somme de deux nombres. Lorsque nous appelons `add(3, 4)`, elle retourne `7`, qui est assigné à la variable `result`. La sortie de ce code serait :

```
<function add at 0x...>
7
```

Maintenant, assignons la fonction `add` à une variable `sum_function` sans l'appeler (c'est-à-dire sans parenthèses).

```python
sum_function = add
```

L'affichage de `add` et `sum_function` montre qu'ils référencent tous les deux le même objet fonction :

```python
print(add)   # Sortie : <function add at 0x...>
print(sum_function)   # Sortie : <function add at 0x...>
```

Cela démontre que les fonctions peuvent être assignées à des variables comme n'importe quel autre type de données. Nous pouvons maintenant utiliser `sum_function` comme la fonction `add` originale et même supprimer le nom de la fonction originale `add`, et la fonction sera toujours accessible via `sum_function`.

```python
del add
print(sum_function(3, 4))  # Sortie : 7
```

### **Passage de fonctions en tant qu'arguments**

Un autre aspect des fonctions de première classe est la capacité de les passer comme arguments à d'autres fonctions. Cela permet une plus grande flexibilité et modularité en permettant aux fonctions d'opérer sur d'autres fonctions.

Illustrons cela avec une fonction `map` personnalisée. Une fonction `map` applique une fonction donnée à chaque élément d'une liste (ou tableau) et retourne une nouvelle liste avec les résultats.

```python
def double(n):
    return n * 2

def map_function(func, values):
    result = []
    for value in values:
        result.append(func(value))
    return result

# utilisation de la fonction map personnalisée
doubled_values = map_function(double, [3, 6, 9, 12, 15])
print(doubled_values)  # Sortie : [6, 12, 18, 24, 30]
```

Dans cet exemple, la fonction `double` prend un nombre `n` et retourne son double. La fonction `map_function` prend une fonction `func` et une liste de `values`, applique `func` à chaque élément dans `values`, et retourne une nouvelle liste avec les résultats.

Lorsque `map_function` est appelée avec `double` et la liste `[3, 6, 9, 12, 15]`, elle applique la fonction `double` à chaque élément de la liste, résultant en `[6, 12, 18, 24, 30]`. Cela démontre comment les fonctions peuvent être passées comme arguments pour créer des motifs de code flexibles et réutilisables.

Notez que lorsque vous passez la fonction, vous n'incluez pas de parenthèses (c'est-à-dire `double` au lieu de `double()`), indiquant que vous passez la fonction elle-même et non le résultat de l'appel de la fonction.

### **Retour de fonctions depuis d'autres fonctions**

Retourner des fonctions depuis d'autres fonctions est une autre caractéristique importante des fonctions de première classe. Ce concept permet la création de code plus complexe et modulaire, souvent utilisé dans des scénarios comme la création de fonctions configurables ou de fermetures.

Pour illustrer davantage, regardons un exemple pratique où une fonction retourne une autre fonction :

```python
def create_multiplier(factor):
    """Retourne une fonction qui multiplie son entrée par le facteur donné."""
    def multiplier(x):
        return x * factor
    return multiplier

# Créer des fonctions de multiplication spécifiques
double = create_multiplier(2)
triple = create_multiplier(3)

# Utiliser les fonctions créées
print(double(5))  # Sortie : 10
print(triple(5))  # Sortie : 15
```

Dans cet exemple, la fonction `create_multiplier` prend un paramètre `factor` et retourne une autre fonction `multiplier`. Cette fonction `multiplier`, lorsqu'elle est appelée avec un argument `x`, retourne le produit de `x` et `factor`.

Lorsque `create_multiplier` est appelée avec `2`, elle retourne une fonction qui multiplie son argument par `2`. De même, lorsqu'elle est appelée avec `3`, elle retourne une fonction qui multiplie son argument par `3`. Ces fonctions retournées (`double` et `triple`) peuvent ensuite être appelées avec des arguments pour effectuer la multiplication. Par exemple, `double(5)` retourne `10` et `triple(5)` retourne `15`.

C'est l'essence d'une fermeture – où la fonction retournée (`multiplier`) conserve l'accès à la variable (`factor`) de sa portée englobante, même après que la fonction externe (`create_multiplier`) a terminé son exécution. Cela permet aux fonctions créées (`double` et `triple`) de se souvenir et d'utiliser la valeur `factor` avec laquelle elles ont été créées.

## **Fonctions d'ordre supérieur**

Les fonctions d'ordre supérieur tirent leur puissance de la capacité à traiter les fonctions comme des citoyens de première classe. Cela signifie que les fonctions peuvent être passées comme arguments à d'autres fonctions ou retournées comme valeurs depuis celles-ci.

Une fonction d'ordre supérieur peut :

* Prendre une ou plusieurs fonctions comme arguments
* Retourner une fonction comme résultat

Nous avons déjà vu des exemples des deux :

* Dans notre exemple "[Passage de fonctions en tant qu'arguments](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#passing-functions-as-arguments)", `map_function` est une fonction d'ordre supérieur car elle prend une fonction (`double`) comme argument.
* Dans notre exemple "[Retour de fonctions depuis d'autres fonctions](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/#returning-functions-from-other-functions)", `create_multiplier` est une fonction d'ordre supérieur car elle retourne une autre fonction (`multiplier`) comme résultat.

Avant de passer aux fermetures, discutons rapidement des fonctions Lambda, car elles ajoutent une autre couche de flexibilité et permettent un code plus concis et expressif.

### **Fonctions Lambda**

Les fonctions Lambda en Python, également connues sous le nom de fonctions anonymes, sont de petites fonctions définies en utilisant le mot-clé `lambda`. Elles sont souvent utilisées pour des tâches de courte durée qui ne nécessitent pas une définition de fonction complète avec `def`. Leur syntaxe est :

```python
lambda arguments: expression
```

La raison pour laquelle nous les discutons est qu'elles peuvent être passées comme arguments à des fonctions d'ordre supérieur ou retournées depuis celles-ci, ce qui en fait des outils polyvalents en programmation fonctionnelle.

#### **Exemple : Utilisation de fonctions Lambda dans une fonction Map personnalisée**

Nous avons précédemment discuté de l'exemple `map_function`. Voyons comment nous pouvons atteindre la même fonctionnalité en utilisant une fonction lambda :

```python
def map_function(func, values):
    return [func(value) for value in values]

# Utilisation d'une fonction lambda comme argument
doubled_values = map_function(lambda n: n * 2, [3, 6, 9, 12, 15])
print(doubled_values)  # Sortie : [6, 12, 18, 24, 30]
```

Dans cet exemple, la fonction lambda `lambda n: n * 2` est passée directement à `map_function`, éliminant le besoin d'une définition de fonction `double` séparée.

#### **Exemple : Création de fonctions de multiplication avec des Lambdas**

En revisitant l'exemple `create_multiplier`, nous pouvons utiliser une fonction lambda pour `multiplier` :

```python
def create_multiplier(factor):
    return lambda x: x * factor

# Créer des fonctions de multiplication spécifiques
double = create_multiplier(2)
triple = create_multiplier(3)

# Utiliser les fonctions créées
print(double(5))  # Sortie : 10
print(triple(5))  # Sortie : 15
```

Ici, `create_multiplier` retourne une fonction lambda qui multiplie son entrée par le `factor` spécifié. C'est une manière compacte et expressive de définir la même fonctionnalité.

Pour une compréhension plus approfondie des fonctions lambda, vous pouvez consulter ce tutoriel [ici](https://www.freecodecamp.org/news/p/8926a586-a677-442f-8fa9-6ba325286250/).

#### L'interdépendance des fonctions d'ordre supérieur et des fonctions de première classe :

Les fonctions d'ordre supérieur sont fondamentalement liées au concept de fonctions de première classe. Sans le support de Python pour traiter les fonctions comme des citoyens de première classe, les fonctions d'ordre supérieur ne seraient pas possibles.

Nous pouvons dire - Sans fonctions de première classe, nous ne pouvons pas avoir de fonctions d'ordre supérieur, car elles reposent intrinsèquement sur la capacité à traiter les fonctions comme des entités de première classe, en opérant sur elles en les prenant comme arguments ou en les retournant comme résultats.

Comprenons avec plus d'exemples :

#### **Exemple : Une fonction d'ordre supérieur qui prend une fonction comme argument (Fonction de première classe)**

```python
def apply_operation(operation, x, y):
    return operation(x, y)

# Fonctions à passer comme arguments
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Utilisation de la fonction d'ordre supérieur
result_add = apply_operation(add, 3, 4)
result_multiply = apply_operation(multiply, 3, 4)

print(result_add)       # Sortie : 7
print(result_multiply)  # Sortie : 12
```

Dans cet exemple, `apply_operation` est une fonction d'ordre supérieur car elle prend une autre fonction (`operation`) comme argument. Les fonctions `add` et `multiply` sont des fonctions de première classe car elles peuvent être passées comme arguments à d'autres fonctions.

La fonction `apply_operation` prend trois paramètres : une fonction (`operation`) et deux entiers (`x` et `y`). Elle retourne le résultat de l'application de la fonction `operation` à `x` et `y`.

En appelant `apply_operation(add, 3, 4)`, elle retourne 7, le résultat de l'addition de 3 et 4. De même, en appelant `apply_operation(multiply, 3, 4)`, elle retourne 12, le résultat de la multiplication de 3 et 4. Cela démontre la flexibilité et la réutilisabilité des fonctions d'ordre supérieur, montrant comment nous pouvons effectuer différentes opérations sur le même ensemble d'entrées.

#### **Exemple : Une fonction d'ordre supérieur qui retourne une autre fonction (Fonction de première classe)**

```python
def discount_applier(discount_rate):
    def apply_discount(price):
        return price - (price * discount_rate / 100)
    return apply_discount

# Création de fermetures avec différents taux de réduction
holiday_discount = discount_applier(20)
member_discount = discount_applier(15)

# Application des réductions
print(holiday_discount(100))  # Sortie : 80.0
print(member_discount(100))   # Sortie : 85.0
```

Dans cet exemple, `discount_applier` prend un paramètre `discount_rate` et retourne une nouvelle fonction `apply_discount`. Cela en fait une "fonction d'ordre supérieur" et `apply_discount` est considérée comme une "fonction de première classe" car elle est définie à l'intérieur de `discount_applier` et retournée pour être utilisée plus tard.

Cette fonction `apply_discount`, lorsqu'elle est appelée avec un argument `price`, retourne le prix réduit calculé en utilisant le `discount_rate`.

Lorsque `discount_applier` est appelée avec un taux de réduction de 20, elle retourne une fonction qui applique une réduction de 20 % à son argument. De même, lorsqu'elle est appelée avec un taux de réduction de 15, elle retourne une fonction qui applique une réduction de 15 %. Ces fonctions retournées (`holiday_discount` et `member_discount`) peuvent ensuite être utilisées pour appliquer les réductions respectives.

En appelant `holiday_discount(100)`, elle retourne 80.0, appliquant une réduction de 20 % à 100. En appelant `member_discount(100)`, elle retourne 85.0, appliquant une réduction de 15 %.

Ces exemples illustrent comment les fonctions d'ordre supérieur permettent la création de motifs de code flexibles, réutilisables et modulaires en exploitant les capacités des fonctions de première classe. Elles forment la base de nombreuses techniques de programmation avancées, y compris les fermetures, et sont essentielles pour écrire du code expressif et puissant.

## **Fermetures**

Une fermeture est une caractéristique de nombreux langages de programmation, y compris Python, qui permet à une fonction de se souvenir et d'accéder à des variables d'une portée englobante même après que la fonction externe a terminé son exécution.

En termes plus simples, une fermeture est une fonction interne qui a accès à des variables de sa fonction contenante (ou externe), même après que cette fonction externe a terminé son exécution.

Regardons quelques exemples pour comprendre comment les fermetures fonctionnent en Python :

### **Fonction imbriquée basique avec exécution immédiate**

```python
def outer_scope():
    name = 'Sam'
    city = 'New York'

    def inner_scope():
        print(f"Bonjour {name}, Salutations de {city}")

    return inner_scope()
    
outer_scope()
```

Dans cet exemple, la fonction `outer_scope` définit deux variables locales : `name` et `city`. Elle définit ensuite et appelle immédiatement `inner_scope`, qui affiche un message de salutation en utilisant les variables `name` et `city` de la portée englobante.

Lorsque `outer_scope` est appelée, la fonction imbriquée `inner_scope` s'exécute, produisant le message de salutation : "Bonjour Sam, Salutations de New York".

### **Retour de la fonction interne**

Maintenant, modifions l'exemple pour retourner la fonction interne sans l'exécuter immédiatement :

```python
def outer_scope():
    name = 'Sam'
    city = 'New York'

    def inner_scope():
        print(f"Bonjour {name}, Salutations de {city}")

    return inner_scope
    
# Assignation de la fonction interne à une variable
greeting_func = outer_scope()

# Appel de la fonction interne
greeting_func()
```

Ici, `outer_scope` définit `name` et `city` comme variables de manière similaire à l'exemple ci-dessus. Elle définit ensuite et retourne la fonction `inner_scope` mais cette fois sans l'appeler (c'est-à-dire `inner_scope` au lieu de `inner_scope()`),

Lorsque `greeting_func = outer_scope()` est exécuté, il assigne la fonction `inner_scope` retournée par `outer_scope` à `greeting_func`.

Maintenant, `greeting_func` contient une référence à la fonction `inner_scope`. L'appel de `greeting_func()` exécute `inner_scope`, qui affiche : "Bonjour Sam, Salutations de New York".

Même si `outer_scope` a terminé son exécution au moment où nous appelons `greeting_func()`, la fonction `inner_scope` (maintenant référencée par `greeting_func`) conserve l'accès aux variables `name` et `city` de sa portée englobante. C'est ce qui en fait une fermeture – elle "ferme" les variables de sa portée contenante.

### **Utilisation de fermetures avec des paramètres**

Pour démontrer la puissance des fermetures, créons un exemple plus dynamique en ajoutant des paramètres à la fonction `outer_scope` :

```python
def outer_scope(name, city):

    def inner_scope():
        print(f"Bonjour {name}, Salutations de {city}")

    return inner_scope

# Création de fermetures avec différents noms et lieux
greet_priyanshu = outer_scope('Dr Priyanshu', 'Jaipur')
greet_sam = outer_scope('Sam', 'New York')

# Exécution des fermetures
greet_priyanshu()    # Sortie : Bonjour Dr Priyanshu, Salutations de Jaipur
greet_sam()     # Sortie : Bonjour Sam, Salutations de New York
```

Maintenant, la fonction `outer_scope` prend `name` et `city` comme paramètres. À l'intérieur de `outer_scope`, la fonction `inner_scope` est définie pour afficher un message de salutation en utilisant `name` et `city`. Au lieu d'appeler `inner_scope`, `outer_scope` retourne la fonction `inner_scope` elle-même.

Lorsque `outer_scope` est appelée avec des arguments spécifiques, elle crée et retourne une fermeture qui capture ces arguments. Par exemple, `greet_priyanshu` est une fermeture qui se souvient de `Dr Priyanshu` et `Jaipur`, tandis que `greet_sam` se souvient de `Sam` et `New York`. Lorsque ces fermetures sont appelées, elles produisent les messages de salutation respectifs.

Même si `outer_scope` a terminé son exécution dans les deux cas, les fonctions `inner_scope` (maintenant `greet_priyanshu` et `greet_sam`) conservent l'accès à leurs variables `name` et `city` respectives de leurs portées englobantes, démontrant le comportement de fermeture.

Si vous le souhaitez, vous pouvez également utiliser une fonction lambda à la place de notre fonction interne (`inner_scope`) comme ceci :

```python
def outer_scope(name, city):
    return lambda: print(f"Bonjour {name}, Salutations de {city}")

greet_priyanshu = outer_scope('Dr Priyanshu', 'Jaipur')
greet_sam = outer_scope('Sam', 'New York')

greet_priyanshu()    # Sortie : Bonjour Dr Priyanshu, Salutations de Jaipur
greet_sam()           # Sortie : Bonjour Sam, Salutations de New York
```

En utilisant une fonction lambda, nous obtenons le même résultat mais de manière plus concise. Les fermetures créées par `outer_scope` conservent toujours l'accès aux variables `name` et `city`, démontrant le même comportement de fermeture.

## **Applications réelles des fermetures**

Maintenant, voyons quelques applications pratiques des fermetures en programmation réelle. Voici quelques scénarios où les fermetures sont couramment utilisées :

### **Gestionnaires d'événements en développement web (un exemple en js mais un cas d'utilisation important)**

En JavaScript, les fermetures sont souvent utilisées pour gérer les événements, tels que les clics sur des boutons.

```html
<html>
<head>
    <title>Exemple de gestionnaire de bouton</title>
</head>
<body>
    <button id="button1">Bouton 1</button>
    <button id="button2">Bouton 2</button>

    <script>
        function createButtonHandler(buttonName) {
            return function() {
                alert(`Bouton ${buttonName} cliqué !`);
            };
        }

        const button1 = document.getElementById('button1');
        const button2 = document.getElementById('button2');

        button1.onclick = createButtonHandler('Bouton 1');
        button2.onclick = createButtonHandler('Bouton 2');
    </script>
</body>
</html>
```

**Explication** :

* `createButtonHandler` est une fonction d'ordre supérieur qui prend un `buttonName` comme argument et retourne une fonction (la fermeture).
* La fonction retournée (fermeture) capture la variable `buttonName` de sa portée lexicale.
* Lorsqu'un bouton est cliqué, la fermeture correspondante est invoquée, et elle a accès au `buttonName` qui a été passé lorsque le gestionnaire a été créé.

### **Maintien de l'état dans les applications GUI**

En Python, les fermetures peuvent être utilisées pour maintenir l'état dans les applications d'interface graphique (GUI), telles que celles créées avec [Tkinter](https://github.com/theSamyak/Tkinter-V3).

```python
import tkinter as tk

def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        print(f'Bouton cliqué {count} fois')
    return counter

root = tk.Tk()
root.title('Exemple de compteur')

counter = create_counter()
button = tk.Button(root, text='Cliquez-moi', command=counter)
button.pack(pady=20)

root.mainloop()
```

**Explication** :

* `create_counter` est une fonction d'ordre supérieur qui initialise `count` à 0 et définit une fonction imbriquée `counter`.
* La fonction `counter` est une fermeture qui capture la variable `count` de la portée englobante.
* Le mot-clé `nonlocal` permet à la fermeture de modifier la variable `count`.
* Chaque fois que le bouton est cliqué, la fonction `counter` est invoquée, et elle incrémente et affiche le `count`.

Quelques autres applications incluent :

### **Création de décorateurs**

Les décorateurs en Python sont un outil puissant pour modifier ou étendre le comportement des fonctions et des méthodes. Les fermetures sont le mécanisme sous-jacent pour implémenter les décorateurs.

Vous pouvez lire [cet article sur les décorateurs](https://www.freecodecamp.org/news/decorators-in-python-tutorial/) pour en apprendre davantage sur eux si vous le souhaitez.

### **Masquage de données et encapsulation**

Les fermetures peuvent être utilisées pour créer des variables et méthodes privées dans une fonction, qui ne peuvent être accédées et modifiées que par la fonction interne. Cela fournit un moyen d'atteindre l'encapsulation en Python.

## **Conclusion**

Les **fonctions de première classe** vous permettent de traiter les fonctions comme n'importe quel autre objet ou type de données, offrant la flexibilité de :

1. Les assigner à des variables
2. Les passer comme arguments à d'autres fonctions
3. Les retourner depuis d'autres fonctions

D'autre part, les **fonctions d'ordre supérieur** ne vous permettent pas seulement de traiter les fonctions comme des données, mais elles vous permettent également d'utiliser des fonctions pour créer de nouvelles fonctions ou pour changer le comportement d'autres fonctions, permettant des opérations telles que :

1. Accepter des fonctions comme arguments/paramètres
2. Retourner des fonctions comme résultats

Cette capacité permet des motifs de code dynamiques et réutilisables, essentiels pour la programmation fonctionnelle.

Les **fermetures**, en résumé, permettent aux fonctions internes d'accéder à des variables de leur portée englobante.

L'utilisation pratique des fermetures inclut des scénarios où vous avez besoin que les fonctions se souviennent de l'état même après que la fonction externe a terminé son exécution.

**Merci d'avoir lu !** Si vous avez des commentaires, des critiques ou des questions, n'hésitez pas à tweeter ou à me contacter à @[OGsamyak](https://x.com/OGsamyak). Vos retours m'aident à m'améliorer !