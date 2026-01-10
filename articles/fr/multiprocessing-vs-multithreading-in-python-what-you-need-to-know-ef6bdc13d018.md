---
title: 'Multiprocessing vs Multithreading en Python : Ce que vous devez savoir.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T16:57:16.000Z'
originalURL: https://freecodecamp.org/news/multiprocessing-vs-multithreading-in-python-what-you-need-to-know-ef6bdc13d018
coverImage: https://cdn-media-1.freecodecamp.org/images/0*lQy3P5ykmIM4G4Oa
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Threading
  slug: threading
seo_title: 'Multiprocessing vs Multithreading en Python : Ce que vous devez savoir.'
seo_desc: 'By Timber.io

  What Is Threading? Why Might You Want It?

  Python is a linear language. However, the threading module comes in handy when you
  want a little more processing power.

  Threading in Python cannot be used for parallel CPU computation. But it is ...'
---

Par Timber.io

#### Qu'est-ce que le Threading ? Pourquoi pourriez-vous en avoir besoin ?

Python est un langage linéaire. Cependant, le module threading s'avère utile lorsque vous souhaitez un peu plus de puissance de traitement.

Le threading en Python ne peut pas être utilisé pour le calcul parallèle sur CPU. Mais il est parfait pour les opérations d'I/O telles que le web scraping, car le processeur reste inactif en attendant les données.

Le threading est révolutionnaire, car de nombreux scripts liés au réseau ou aux données I/O passent la majorité de leur temps à attendre des données d'une source distante.

Comme les téléchargements peuvent ne pas être liés (par exemple, si vous scrapez des sites web séparés), le processeur peut télécharger à partir de différentes sources de données en parallèle et combiner le résultat à la fin.

Pour les processus intensifs en CPU, il y a peu d'avantages à utiliser le module threading.

![Image](https://cdn-media-1.freecodecamp.org/images/ovUCmUeZrbYCgom4gc3TcPP9EZtq4INvmwTa)

Le threading est inclus dans la bibliothèque standard :

```
import threading
from queue import Queue
import time
```

Vous pouvez utiliser `target` comme objet appelable, `args` pour passer des paramètres à la fonction, et `start` pour démarrer le thread.

```
def testThread(num):
    print(num)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=testThread, args=(i,))
        t.start()
```

Si vous n'avez jamais vu `if __name__ == '__main__':` auparavant, c'est essentiellement une manière de s'assurer que le code qui est imbriqué à l'intérieur ne s'exécutera que si le script est exécuté directement (et non importé).

#### Le Verrou (Lock)

Vous voudrez souvent que vos threads puissent utiliser ou modifier des variables communes entre les threads. Pour ce faire, vous devrez utiliser ce qu'on appelle un `lock` (verrou).

Chaque fois qu'une fonction souhaite modifier une variable, elle verrouille cette variable. Lorsqu'une autre fonction souhaite utiliser une variable, elle doit attendre que cette variable soit déverrouillée.

![Image](https://cdn-media-1.freecodecamp.org/images/7tzH0eWzoj2WDCWtQ4ofrUxBXhFBjcQ2eZVW)

Imaginez deux fonctions qui incrémentent toutes deux une variable de 1. Le verrou vous permet de vous assurer qu'une fonction peut accéder à la variable, effectuer des calculs et écrire dans cette variable avant qu'une autre fonction ne puisse accéder à la même variable.

Vous pouvez utiliser un verrou d'impression pour vous assurer qu'un seul thread peut imprimer à la fois. Cela empêche le texte de se mélanger (et de causer une corruption de données) lorsque vous imprimez.

Dans le code ci-dessous, nous avons dix tâches que nous voulons accomplir et cinq travailleurs qui travailleront sur ces tâches :

```
print_lock = threading.Lock()

def threadTest():
    # lorsque cela se termine, le print_lock est libéré
    with print_lock:
        print(worker)

def threader():
    while True:
        # obtenir la tâche depuis le début de la file d'attente
        threadTest(q.get())
        q.task_done()

q = Queue()

for x in range(5):
    thread = threading.Thread(target=threader)
    # cela garantit que le thread mourra lorsque le thread principal mourra
    # peut définir t.daemon à False si vous voulez qu'il continue à fonctionner
    t.daemon = True
    t.start()

for job in range(10):
    q.put(job)
```

#### Le Multithreading n'est pas toujours la solution parfaite

Je trouve que de nombreux guides tendent à omettre les inconvénients de l'utilisation de l'outil qu'ils viennent de vous enseigner. Il est important de comprendre qu'il y a des avantages et des inconvénients associés à l'utilisation de tous ces outils. Par exemple :

1. Il y a un surcoût associé à la gestion des threads, donc vous ne voulez pas l'utiliser pour des tâches basiques (comme dans l'exemple)
2. Le threading augmente la complexité du programme, ce qui peut rendre le débogage plus difficile

### Qu'est-ce que le Multiprocessing ? En quoi est-il différent du threading ?

Sans le multiprocessing, les programmes Python ont du mal à maximiser les spécifications de votre système à cause du `GIL` (Global Interpreter Lock). Python n'a pas été conçu en tenant compte du fait que les ordinateurs personnels pourraient avoir plus d'un cœur (ce qui montre à quel point le langage est ancien).

Le GIL est nécessaire car Python n'est pas thread-safe, et il y a un verrou globalement appliqué lors de l'accès à un objet Python. Bien que ce ne soit pas parfait, c'est un mécanisme assez efficace pour la gestion de la mémoire. *Que pouvons-nous faire ?*

Le multiprocessing vous permet de créer des programmes qui peuvent s'exécuter concurrentiellement (en contournant le GIL) et d'utiliser la totalité de votre cœur CPU. Bien qu'il soit fondamentalement différent de la bibliothèque threading, la syntaxe est assez similaire. La bibliothèque multiprocessing donne à chaque processus son propre interpréteur Python, et à chacun son propre GIL.

En raison de cela, les problèmes habituels associés au threading (tels que la corruption de données et les interblocages) ne sont plus un problème. Comme les processus ne partagent pas la mémoire, ils ne peuvent pas modifier la même mémoire concurrentiellement.

#### Commençons

```
import multiprocessing

def spawn():
    print('test!')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn)
        p.start()
```

Si vous avez une base de données partagée, vous voulez vous assurer que vous attendez que les processus pertinents se terminent avant d'en démarrer de nouveaux.

```
for i in range(5):
    p = multiprocessing.Process(target=spawn)
    p.start()
    p.join() # cette ligne vous permet d'attendre les processus
```

Si vous souhaitez passer des arguments à votre processus, vous pouvez le faire avec `args` :

```
import multiprocessing

def spawn(num):
    print(num)

if __name__ == '__main__':
    for i in range(25):
        ## ici
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
```

Voici un exemple intéressant, car les nombres n'arrivent pas dans l'ordre auquel vous vous attendez (sans le `p.join()`).

#### Inconvénients

Comme pour le threading, il y a encore des inconvénients avec le multiprocessing... vous devez choisir votre poison :

1. Il y a un surcoût d'I/O dû au transfert de données entre les processus
2. La mémoire entière est copiée dans chaque sous-processus, ce qui peut représenter un surcoût important pour les programmes plus significatifs

### Conclusion

Quand devez-vous utiliser le multithreading vs le multiprocessing ?

* Si votre code comporte beaucoup d'I/O ou d'utilisation de réseau, le multithreading est votre meilleur choix en raison de son faible surcoût.
* Si vous avez une interface graphique, utilisez le multithreading pour que votre thread UI ne soit pas bloqué.
* Si votre code est lié au CPU, vous devriez utiliser le multiprocessing (si votre machine a plusieurs cœurs)

*Juste une mise en garde : nous sommes une entreprise de journalisation ici @ Timber. Nous serions ravis que vous essayiez [notre produit](https://timber.io/) (il est vraiment génial !), mais c'est tout ce que nous allons en dire.*

Si vous êtes intéressé à recevoir plus de publications de Timber dans votre boîte de réception, n'hésitez pas à vous inscrire [ici](http://eepurl.com/dxWQxr). Nous promettons qu'il n'y aura pas de spam, juste du bon contenu sur une base hebdomadaire.

![Image](https://cdn-media-1.freecodecamp.org/images/TfypoIZnTArPPIDyCyeOzyDi8ybZKDcqnaq6)

*Publié à l'origine sur [timber.io](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/).*
