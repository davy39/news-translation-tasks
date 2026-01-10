---
title: Comment utiliser les générateurs Python – Expliqué avec des exemples de code
subtitle: ''
author: Rochdi Khalid
co_authors: []
series: null
date: '2024-07-10T19:05:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-python-generators
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/SERIE-1.png
tags:
- name: generators
  slug: generators
- name: Python
  slug: python
seo_title: Comment utiliser les générateurs Python – Expliqué avec des exemples de
  code
seo_desc: 'Python generators are a powerful feature that allow lazy iteration through
  a sequence of values.

  They produce items one at a time and only when needed, which makes them the best
  choice for working with large datasets or streams of data where it would...'
---

Les générateurs Python sont une fonctionnalité puissante qui permet une itération paresseuse à travers une séquence de valeurs.

Ils produisent des éléments un à la fois et uniquement lorsque cela est nécessaire, ce qui en fait le meilleur choix pour travailler avec de grands ensembles de données ou des flux de données où il serait inefficace et peu pratique de tout charger en mémoire à la fois.

## Comment définir et utiliser les générateurs

Pour définir un générateur, vous pouvez utiliser le mot-clé `def` comme vous le feriez avec une fonction normale. Cependant, au lieu de retourner une valeur avec `return`, nous utilisons `yield`.

Ici, le mot-clé `yield` est utilisé pour produire une valeur et suspendre l'exécution de la fonction génératrice. Lorsque la fonction est reprise, elle continue l'exécution immédiatement après l'instruction `yield`.

### Exemple : Générateur simple

Voici un générateur simple qui produit les `n` premiers nombres :

```python
def simple_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1
        
# Utilisation du générateur
gen = simple_generator(5)
for number in gen:
    print(number)
```

Sortie :

```terminal
0
1
2
3
4
```

Lorsque la fonction `simple_generator()` est appelée, elle n'exécute pas son code. Au lieu de cela, elle retourne un objet générateur qui contient une méthode interne nommée `__next__()`, qui est créée lorsque la fonction génératrice est appelée.

L'objet générateur utilise implicitement cette méthode comme protocole d'itérateur lorsque nous itérons sur le générateur.

## Avantages de l'utilisation des générateurs

Les générateurs Python offrent plusieurs avantages qui améliorent considérablement l'efficacité et la lisibilité du code. En produisant des éléments à la volée, les générateurs optimisent l'utilisation de la mémoire et améliorent les performances par rapport aux méthodes itérables traditionnelles.

Explorons certains de ces avantages en détail, en mettant en évidence comment les générateurs simplifient le développement Python et améliorent la qualité du code.

### Optimisation de la mémoire

Comparés aux listes qui chargent tous les éléments en mémoire à la fois, les générateurs sont des optimiseurs d'utilisation de la mémoire. Ils produisent des éléments un à la fois et uniquement lorsque cela est nécessaire.

Voici un exemple qui considère un scénario où nous devons générer une grande liste de nombres :

```python
# Utilisation d'une liste
numbers = [i for i in range(1000000)]

# Utilisation d'un générateur
def number_generator():
    for i in range(1000000):
        yield i
        
gen_numbers = number_generator()
```

Avec la liste, les 1000000 nombres sont stockés en mémoire à la fois, mais avec le générateur, les nombres sont produits un à la fois, réduisant ainsi l'utilisation de la mémoire.

### Performance améliorée

Puisque les générateurs produisent des éléments à la volée, ils améliorent les performances, en particulier en termes de vitesse et d'efficacité. Ils peuvent commencer à produire des résultats immédiatement sans attendre de traiter un ensemble de données complet.

Dans cet exemple, supposons que nous devons traiter chaque nombre dans une séquence :

```python
# Utilisation d'une liste
numbers = [i for i in range(1000000)]
squared_numbers = [x**2 for x in numbers]

# Utilisation d'un générateur
def number_generator():
    for i in range(1000000):
        yield i
        
def squared_gen(gen):
    for num in gen:
        yield num**2
        
gen_numbers = number_generator()
squared_gen_numbers = squared_gen(gen_numbers)
```

Lorsque nous utilisons la liste, nous générons tous les nombres puis les traitons, ce qui prend plus de temps. Cependant, avec le générateur, chaque nombre est traité dès qu'il est généré, rendant le processus plus efficace.

### Simplicité et lisibilité du code

Les générateurs aident à écrire un code propre et lisible. Ils nous permettent de définir un algorithme itératif de manière simple, sans avoir besoin de code standard pour gérer l'état de l'itération. Considérons un scénario où nous devons lire des lignes d'un grand fichier :

```python
# Utilisation d'une liste
def read_large_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines
    
lines = read_large_file('large_file.txt')

# Utilisation d'un générateur
def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line
           
lines_gen = read_large_file('large_file.txt')
```

Avec l'approche par liste, nous lisons toutes les lignes en mémoire à la fois. Avec le générateur, nous lisons et produisons une ligne à la fois, ce qui rend le code plus simple et plus lisible tout en contribuant à économiser de la mémoire.

## Cas d'utilisation pratiques

Cette section explore quelques cas d'utilisation pratiques où les générateurs Python excellent, découvrant comment les générateurs simplifient les tâches complexes tout en optimisant les performances et l'utilisation de la mémoire.

### Traitement de flux

Les générateurs sont excellents pour gérer des flux continus de données, comme les données de capteurs en temps réel, les flux de journaux ou les flux en direct provenant d'API. Ils fournissent un traitement efficace des données dès qu'elles deviennent disponibles, sans avoir besoin de stocker de grandes quantités de données en mémoire.

```python
import time

def data_stream():
    """Simule un flux de données."""
    for i in range(10):
        time.sleep(1) # Simule l'arrivée de données chaque seconde
        yield 1
        

def stream_processor(data_stream):
    """Traite les données du flux."""
    for data in data_stream:
        processed_data = data * 2 # Exemple d'étape de traitement
        yield processed_data
        
        
# Utilisation
stream = data_stream()
processed_stream = stream_processor(stream)
for data in processed_stream:
	print(data)
```

Dans cet exemple, la méthode `data_stream()` génère des données à intervalles, simulant un flux de données continu. Le `stream_processor()` traite chaque morceau de données dès qu'il arrive, démontrant comment les générateurs peuvent gérer les données de flux efficacement sans avoir besoin de charger toutes les données en mémoire à la fois.

### Algorithmes itératifs

Les générateurs fournissent un moyen simple de définir et d'exécuter des algorithmes itératifs qui impliquent des calculs et des simulations répétitifs. Ils nous permettent de maintenir l'état de l'itération sans gérer manuellement les variables de boucle, ce qui peut améliorer la clarté et la maintenabilité du code.

```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
   
# Utilisation
fib_gen = fibonacci_generator()
for i in range(10):
	print(next(fib_gen))
```

Dans l'exemple ci-dessus, la méthode `fibonacci_generator()` définit un générateur qui produit des nombres de Fibonacci indéfiniment. Il retourne chaque nombre de Fibonacci un à la fois, en commençant par 0 et 1.

Ici, la boucle `for` itère 10 fois pour imprimer les 10 premiers nombres de Fibonacci, démontrant comment les générateurs peuvent générer et gérer efficacement des séquences sans les précharger en mémoire.

### Simulateur en temps réel

Dans cet exemple, nous allons simuler des mises à jour en temps réel du prix d'une action. Le générateur produira un nouveau prix d'action à chaque étape, basé sur le prix précédent et une fluctuation aléatoire.

```python
import random
import time

def stock_price_generator(initial_price, volatility, steps):
    """Génère des prix d'actions à partir de initial_price avec une volatilité donnée."""

    price = initial_price
    for _ in range(steps):
        # Simule le changement de prix
        change_percent = random.uniform(-volatility, volatility)
        price += price * change_percent
        yield price
        time.sleep(1) # Simule un délai en temps réel
        
# Crée le générateur de prix d'actions
initial_price = 100.0 # Prix de départ de l'action
volatility = 0.02 # Volatilité en pourcentage
steps = 10 # Nombre d'étapes (mises à jour) à simuler
 
stock_prices = stock_price_generator(initial_price, volatility, steps)
 
# Simule la réception et le traitement des prix d'actions en temps réel
for price in stock_prices:
    print(f"Nouveau prix de l'action : {price:.2f}")
```

Cet exemple génère chaque prix d'action à la volée basé sur le prix précédent et ne stocke pas tous les prix générés en mémoire, ce qui le rend efficace pour les simulations de longue durée.

Le générateur fournit un nouveau prix d'action à chaque étape avec un minimum de calcul. Le `time.sleep(1)` simule un délai en temps réel, permettant au système de gérer d'autres tâches simultanément si nécessaire.

## Résumé

En résumé, les générateurs Python offrent une gestion efficace de la mémoire et des performances améliorées, simplifiant le code tout en abordant diverses tâches comme le traitement de flux, les algorithmes itératifs et la simulation en temps réel.

Leur capacité à optimiser les ressources en fait un outil précieux pour les développeurs Python modernes recherchant des solutions élégantes et évolutives.

Espérons que cette exploration des générateurs Python vous fournit les informations nécessaires pour exploiter leur plein potentiel. Si vous avez des questions ou souhaitez discuter davantage, n'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/rochdi-khalid/). De plus, vous pouvez vous abonner à [ma chaîne YouTube](https://www.youtube.com/channel/UCF8iZXSsjgc8kE8hITp5rdQ) où je partage des vidéos sur les techniques de codage et les projets sur lesquels je travaille.