---
title: Comment maintenir la scalabilité dans votre code Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-20T17:51:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-scalable-apps-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/python-coding.jpg
tags:
- name: Productivity
  slug: productivity
- name: Python
  slug: python
- name: scalability
  slug: scalability
seo_title: Comment maintenir la scalabilité dans votre code Python
seo_desc: "By Shifa Martin\nAny application that processes data can start to perform\
  \ slowly or even start to corrupt or break. It is better if developers are able\
  \ to program quickly and add more value to coding. \nAs developers, we should have\
  \ tools to prototype ..."
---

Par Shifa Martin

Toute application qui traite des données peut commencer à fonctionner lentement ou même commencer à corrompre ou à planter. Il est préférable que les développeurs soient capables de programmer rapidement et d'ajouter plus de valeur au codage. 

En tant que développeurs, nous devrions avoir des outils pour prototyper rapidement. C'est pourquoi nous devrions investir des efforts dans la création d'une application scalable. Globalement, il est possible de construire une application substantielle et scalable avec le langage de programmation Python.

Python est un langage de programmation de haut niveau qui est également orienté objet. Avec ses qualités telles que les structures de données intégrées, la liaison dynamique et la typage dynamique, nous pouvons l'utiliser pour développer des applications aussi rapidement que possible. 

Python peut également être utilisé comme un langage de script collé qui intègre les composants existants et nous aide à construire des applications scalables.

Python est l'un des pionniers des langages de programmation que les développeurs peuvent utiliser pour effectuer tout le travail de mise à l'échelle. 

Voici quelques conseils que vous pouvez consulter pour développer des applications scalables en Python.

## Apprendre à utiliser intelligemment les 'Collections'

Python supporte des structures de données/conteneurs riches et puissantes pour les 'collections' telles que [dict](https://docs.python.org/3.6/library/stdtypes.html#dict), [list](https://docs.python.org/3.6/library/stdtypes.html#list), [set](https://docs.python.org/3.6/library/stdtypes.html#set), et [tuple](https://docs.python.org/3.6/library/stdtypes.html#tuple). Elles sont si précieuses dans la construction d'applications scalables. Cependant, leur surutilisation peut impacter la scalabilité du code. Il est facile de repérer quand les collections ont été surutilisées. 

```python2
# notebooks.csv contient des méta-informations sur une collection de notebooks :
# titre, auteur, année de publication, etc.


# load_from_file retourne une liste de dictionnaires.


notebooks = load_from_file('notebooks.csv')


notebook_summaries = dict()
for notebook in notebooks:


   notebook_summaries[notebook["heading"]] = notebook["summary"]


for heading, summary in notebook_summaries.items():


   # Faire quelque chose d'intéressant avec le résumé.


   print(heading, summary)

```

À partir du code ci-dessus, vous pouvez clairement voir qu'il crée un tableau de mappage des titres après avoir lu les données des notebooks depuis le fichier CSV. Si vous le voyez du point de vue de l'utilisation de la mémoire, il n'y a rien de mal si notebooks.csv contient des centaines de titres. 

Cependant, ce n'est pas correct si cela est lié à l'inventaire de toutes les boutiques de notebooks avec des dizaines de titres. Vous pouvez avoir un ou deux problèmes avec votre codage, ce qui dépend également de la version que vous utilisez, Python 2 ou Python 3.

Cela crée un problème de goulot d'étranglement avec la scalabilité de la mémoire du code. Créer une structure de données appelée notebook_summaries est inutile ici mais cela améliore la lisibilité. La ligne "for" vous aide à savoir immédiatement qu'une boucle est en cours d'exécution ici à travers les résumés. 

La nouvelle structure de données contient le résumé complet de chaque notebook, ce qui est susceptible de consommer plus de mémoire que tous les autres champs. Supposons qu'un notebook consomme N octets de mémoire, alors le bloc complet consommera au moins 1,5 * N octets. 

**Cela sera mieux scalable en Python 3**

```python
notebooks = load_from_file('notebooks.csv')


for notebook in notebooks.items():


   print(notebook["title"], notebook["summary"])

```

Je recommande de créer des variables bien nommées car cela aide à améliorer la maintenabilité de votre code Python.

## Itération intelligente des codes Python

Lors du développement d'applications de grande taille avec Python, la scalabilité n'est pas la seule chose à laquelle vous devriez penser. Vous pouvez rencontrer plusieurs autres problèmes. Par exemple, le problème d'itération est le plus courant. 

Parfois, la ligne for dans votre codage itère sur notebook_summaries.items() et crée une autre copie de notebooks. Cette itération de code peut être responsable des faibles performances du code dans lequel le code Python commence à se bloquer avant d'initier la boucle for.      

Cela se produit parce que notebook_summaries.items() forme une très grande liste qui consomme plus de mémoire. De plus, c'est parce que le code Python exécute le bytecode après la boucle for. 

Il commencera à allouer plus de mémoire pour cette liste. Encore une fois, le problème d'itération affecte Python 2 ainsi que les items() de Python 3 et fait une copie supplémentaire du contenu de notebooks_summaries. Les développeurs peuvent utiliser iteritems au lieu de items dans Python 2 :

**En Python 2, utilisez "iteritems" au lieu de "items"**

```python
notebooks = load_from_file('notebooks.csv')


    for notebook in notebooks.iteritems():


      print(notebook["title"], notebook["summary"])
```

Donc, le point ici est de remarquer la différence entre l'utilisation d'un itérateur dans toutes les versions de Python et la création d'une liste. C'est la responsabilité du développeur de justifier le bon modèle selon le contexte de codage.

## Utiliser les 'Générateurs' pour la scalabilité dans le code Python

La fonction générateur vous permet de créer des itérateurs de manière plus simple. Imaginez que vous travaillez sur la construction d'un programme logiciel comme Grammarly qui prend du texte, analyse les phrases et effectue une sorte d'analyse grammaticale. Chaque ligne de phrase sera divisée par un point suivi d'un ou plusieurs caractères.

**Voir le codage** 

```python
import re
text = '''Corps complet de texte. Il a de nombreuses phrases.
 
Certaines ont des erreurs grammaticales et d'autres sont correctes.'''
 
sentences = re.analyzed(r'\.\s+', text)
 
for sentence in sentences:
 
   print(sentence)
```

**Exécuter la liste**

```python
Ceci est un corps de texte
Il a de nombreuses phrases
 
Certaines ont des erreurs grammaticales et d'autres sont correctes.
```

```python
import random
def weathermaker(volatility, days):
    '''
    Génère une série de messages donnant la météo du jour et des commentaires occasionnels
    volatility - un float entre 0 et 1 ; plus ce nombre est grand, plus
  la probabilité que le temps change chaque jour est grande
    days - nombre de jours pour lesquels générer la météo
    '''
    # Toujours commencer comme si hier était ensoleillé
    current_weather = 'sunny'
    # Le premier élément est la probabilité que le temps reste le même
    # Le deuxième élément est la probabilité que le temps change
    # Plus la volatilité est élevée, plus la probabilité de changement est grande
    weights = 1.0 - volatility, volatility    # Pour le fun, suivre combien de jours ensoleillés consécutifs il y a eu
    sunny_run = 1
    # Combien de jours de pluie consécutifs il y a eu
    rainy_run = 0
    for day in range(days):
        # Déterminer le contraire de la météo actuelle
        other_weather = 'rainy' if current_weather == 'sunny' else 'sunny'
        # Préparer le choix de la météo du lendemain. D'abord, préparer les choix
        choose_from = current_weather, other_weather        # random.choices retourne une liste de choix aléatoires basés sur les poids
        # Par défaut, une liste de 1 élément, donc nous prenons cet élément unique avec 0 current_weather = random.choices(choose_from, weights)0        yield 'aujourd\'hui il fait ' + current_weather
        if current_weather == 'sunny':
            # Vérifier les séries de trois jours ensoleillés ou plus
            sunny_run += 1
            rainy_run = 0
            if sunny_run >= 3:
                yield "Oh oh ! Nous avons soif !"
        else:
            # Vérifier les séries de trois jours de pluie ou plus
            rainy_run += 1
            sunny_run = 0
            if rainy_run >= 3:
                yield "Pluie, pluie, va-t-en !"
    return
 
# Créer un objet générateur et imprimer sa série de messages
for msg in weathermaker(0.2, 10):
    print(msg)

```

**Sortie**

```python
$ python weathermaker.py
today it is sunny
today it is sunny
Uh oh! We're getting thirsty!
today it is sunny
Uh oh! We're getting thirsty!
today it is sunny
Uh oh! We're getting thirsty!
today it is rainy
today it is sunny
today it is rainy
today it is rainy
today it is rainy
Rain, rain go away!
today it is rainy
Rain, rain go away!
```

À partir du code ci-dessus, il est clair que les [générateurs Python](https://wiki.python.org/moin/Generators) sont un excellent moyen de créer rapidement des itérateurs. Ils ont de nombreux avantages et allouent de la mémoire pour chaque phrase une à la fois. Ils facilitent également la modification du code par les développeurs sans tout gâcher. 

Un autre avantage que les générateurs fournissent est l'[encapsulation](https://pythonspot.com/encapsulation/) qui offre de nouvelles façons utiles de packager et d'isoler les dépendances internes du code. C'est pourquoi vous pouvez utiliser des générateurs dans les boucles for.

**Vous pouvez ajouter plusieurs instructions yield dans un générateur**

```python
def nums3():
   n = 0
 
   while n < 6:
 
  yield n
       n += 1
   yield 63 # Deuxième yield
for num in nums3():
   print(num)
```

**Sortie**

```python
0
1
2
3
63
```

**Explication du code ci-dessus**

Ici, le deuxième yield est complété après la sortie de la boucle while. Lorsque la fonction atteint le return implicite à la fin, l'itération s'arrête.

## Mots de la fin

Donc, si vous n'utilisez pas encore les générateurs dans votre code Python, apprenez à le faire. Je sais que vous serez content de l'avoir fait. Ils font partie intégrante du codage Python et peuvent être utiles pour votre prochain développement d'application sur Python.

Sans aucun doute, Python est un langage très utile, diversifié et bien maintenu, et il n'y a pas de limite aux fonctionnalités. Cependant, j'ai partagé les idées que j'utilise dans mon processus de codage quotidien pour simplifier les choses. 

**ValueCoders est une entreprise expérimentée de [développement logiciel](https://www.valuecoders.com/). Au cas où vous auriez besoin de services de développement Python, n'hésitez pas à [nous contacter](https://www.valuecoders.com/contact).**