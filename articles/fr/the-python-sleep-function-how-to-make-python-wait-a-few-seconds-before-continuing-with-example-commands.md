---
title: La fonction Python Sleep – Comment faire attendre Python quelques secondes
  avant de continuer, avec des exemples de commandes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-24T16:24:24.000Z'
originalURL: https://freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/pexels-pixabay-280254.jpg
tags:
- name: Productivity
  slug: productivity
- name: Python
  slug: python
seo_title: La fonction Python Sleep – Comment faire attendre Python quelques secondes
  avant de continuer, avec des exemples de commandes
seo_desc: "By Amy Haddad\nYou can use Python’s sleep() function to add a time delay\
  \ to your code. \nThis function is handy if you want to pause your code between\
  \ API calls, for example. Or enhance the user’s experience by adding pauses between\
  \ words or graphics.\n..."
---

Par Amy Haddad

Vous pouvez utiliser la fonction `sleep()` de Python pour ajouter un délai temporel à votre code. 

Cette fonction est pratique si vous souhaitez mettre en pause votre code entre des appels API, par exemple. Ou améliorer l'expérience de l'utilisateur en ajoutant des pauses entre les mots ou les graphiques.

```python
from time import sleep
sleep(2)   
print("hello world")
```

Lorsque j'exécute le code ci-dessus, il y a un délai d'environ deux secondes avant que "hello world" ne s'affiche. 

Je subis un délai car `sleep()` arrête "[l'exécution du thread appelant](https://docs.python.org/3/library/time.html#time.sleep)" pendant un nombre de secondes fourni (bien que le temps exact soit approximatif). Ainsi, l'exécution du programme est suspendue pendant environ deux secondes dans l'exemple ci-dessus.

Dans cet article, vous apprendrez comment mettre votre code Python en pause.

# Les détails de Sleep

Le [module time](https://docs.python.org/3/library/time.html#time) de Python contient de nombreuses fonctions liées au temps, dont `sleep()`. Pour utiliser sleep(), vous devez l'importer.

```python
from time import sleep
```

sleep() prend un argument : seconds. Il s'agit de la durée (en secondes) pendant laquelle vous souhaitez retarder votre code.

```python
seconds = 2
sleep(seconds)
```

## Sleep en action

Utilisons maintenant `sleep()` de différentes manières. 

Après avoir importé sleep du module `time`, deux lignes de texte s'afficheront. Cependant, il y aura un délai d'environ deux secondes entre l'affichage de chaque ligne.  

```python
from time import sleep
 
print("Bonjour")
sleep(2)  
print("Monde")
```

Voici ce qui s'est passé lorsque j'ai exécuté le code :

**`"Bonjour"`** Cette ligne s'est affichée immédiatement.

Ensuite, il y a eu un délai d'environ deux secondes.

**`"Monde"`** Cette ligne s'est affichée environ deux secondes après la première.

### Vous pouvez être précis

Rendez votre délai temporel spécifique en passant un nombre à virgule flottante à `sleep()`.

```python
from time import sleep
 
print("S'affiche immédiatement.")
sleep(0.50)
print("S'affiche après un léger délai.")
```

Voici ce qui s'est passé lorsque j'ai exécuté le code :

**`"S'affiche immédiatement."`** Cette ligne s'est affichée immédiatement.

Ensuite, il y a eu un délai d'environ 0,5 seconde.

**`"S'affiche après un léger délai."`** Cette ligne s'est affichée environ 0,5 seconde après la première.

## Créer un horodatage

Voici un autre exemple à considérer.

Dans le code ci-dessous, je crée cinq horodatages. J'utilise `sleep()` pour ajouter un délai d'environ une seconde entre chaque horodatage.

```python
import time
 
for i in range(5):
   current_time = time.localtime()
   timestamp = time.strftime("%I:%m:%S", current_time)
   time.sleep(1)
   print(timestamp)
```

Ici, j'importe le module time entier pour pouvoir accéder à plusieurs fonctions, y compris sleep().

```python
import time
```

Ensuite, je crée une boucle for qui s'exécutera cinq fois.

```python
for i in range(5):
...
```

À chaque itération, je récupère l'heure actuelle.

```python
current_time = time.localtime()
```

Je récupère un horodatage en utilisant une autre fonction du module time, `strftime()`.

```python
timestamp = time.strftime("%I:%m:%S", current_time)
```

La fonction sleep() suit, ce qui provoquera un délai à chaque itération de la boucle.

```python
time.sleep(1)
```

Lorsque j'exécute le programme, j'attends environ une seconde avant que le premier horodatage ne s'affiche. Ensuite, j'attends environ une seconde pour que l'horodatage suivant s'affiche, et ainsi de suite jusqu'à la fin de la boucle.

La sortie ressemble à ceci :

```python
04:08:37
04:08:38
04:08:39
04:08:40
04:08:41
```

### sleep() et l'expérience utilisateur

Une autre façon d'utiliser `sleep()` est d'améliorer l'expérience utilisateur en créant un peu de suspense. 

```python
from time import sleep
 
story_intro = ["Il", "faisait", "une", "nuit", "sombre", "et", "orageuse", "..."]
for word in story_intro:
   print(word)
   sleep(1)
```

Ici, je parcours la liste de mots dans **`story_intro`**. Pour ajouter du suspense, j'utilise la fonction sleep() pour retarder d'environ une seconde après que chaque mot est affiché.

```python
time.sleep(1)
```

Bien que la vitesse d'exécution soit souvent au premier plan de nos pensées, il est parfois utile de ralentir et d'ajouter une pause dans notre code. Lorsque ces occasions se présentent, vous savez quoi utiliser et comment cela fonctionne.

_J'écris sur l'apprentissage de la programmation et les meilleures façons de s'y prendre sur [amymhaddad.com](http://amymhaddad.com/)._ Je tweete sur la programmation, l'apprentissage et la productivité : [@amymhaddad](https://twitter.com/amymhaddad).