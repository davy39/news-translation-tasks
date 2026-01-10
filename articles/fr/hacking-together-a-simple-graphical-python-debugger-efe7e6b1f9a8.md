---
title: Comment bricoler un débogueur graphique pour Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-01T01:46:38.000Z'
originalURL: https://freecodecamp.org/news/hacking-together-a-simple-graphical-python-debugger-efe7e6b1f9a8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aOUY9bnxHsfHrZgyDz8_XA.jpeg
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment bricoler un débogueur graphique pour Python
seo_desc: 'By Cristian Medina

  Zero-to-Debugging in 15 mins

  You don’t realize the value of a debugger until you’re stuck working on a hard-to-visualize
  problem. But once you fire up a development environment with decent debugging capabilities,
  you’ll never look ...'
---

Par Cristian Medina

#### De zéro au débogage en 15 minutes

Vous ne réalisez pas la valeur d'un débogueur jusqu'à ce que vous soyez coincé sur un problème difficile à visualiser. Mais une fois que vous lancez un environnement de développement avec de bonnes capacités de débogage, vous ne reviendrez jamais en arrière.

Vous voulez savoir où vous en êtes dans l'exécution du code ? Ce qui prend tant de temps ? Il suffit de le mettre en pause et de vérifier.

Vous vous demandez quelle valeur est assignée à cette variable ? Passez la souris dessus.

Vous voulez sauter un tas de code et continuer à exécuter à partir d'une autre section ? Allez-y.

Parfois, `print(nom_de_variable)` n'est tout simplement pas suffisant pour vous donner une idée de ce qui se passe avec votre projet. C'est là qu'un bon débogueur peut vous aider à comprendre les choses.

Python vous offre déjà un débogueur intégré sous la forme de _pdb_ (un outil en ligne de commande). Mais grâce à la formidable communauté Python, il existe d'autres options qui disposent d'interfaces graphiques. Et il existe une tonne d'environnements de développement intégrés (IDE) qui fonctionnent avec Python, tels que [JetBrain's PyCharm](https://www.jetbrains.com/pycharm/), [Wingare's WingIDE](https://wingware.com/), et même [Microsoft's Visual Studio Community](https://beta.visualstudio.com/vs/community/).

Mais vous n'êtes pas ici pour entendre comment un débogueur est meilleur qu'un autre, ou lequel est plus joli, ou plus élégant. Vous êtes ici pour apprendre à quel point il est simple d'écrire un débogueur Python qui parcourt votre code. Cela vous donne un aperçu des internes de Python.

Je vais vous montrer comment vous pouvez en construire un, et ce faisant, satisfaire une curiosité que j'ai eue depuis longtemps.

Maintenant, passons à l'action.

### Un petit rappel sur la façon dont le code Python est organisé et traité

Contrairement à la croyance populaire, Python est en fait un langage compilé. Lorsque vous exécutez du code, votre module est passé à travers un compilateur qui génère du _bytecode_ qui est mis en cache sous forme de fichiers _.pyc_ ou ___pycache___. Le bytecode lui-même est ce qui est exécuté ligne par ligne.

En fait, le code CPython réel qui exécute un programme n'est rien de plus qu'une gigantesque instruction switch case exécutée dans une boucle. C'est une instruction if-else qui regarde le bytecode d'une instruction, puis la dispose en fonction de ce que cette opération est censée faire.

Les instructions de bytecode exécutables sont référencées en interne sous le nom de _code objects_, et les modules _dis_ et _inspect_ sont utilisés pour les produire ou les interpréter. Ce sont des structures immuables, qui, bien que référencées par d'autres objets — comme les fonctions — ne contiennent elles-mêmes aucune référence.

Vous pouvez facilement regarder le bytecode qui représente une source donnée via `dis.dis()`. Il suffit de l'essayer avec une fonction ou une classe aléatoire. C'est un petit exercice sympa qui vous aidera à visualiser ce qui se passe. La sortie ressemblera à quelque chose comme ceci :

```python
>>> def sample(a, b):
...     x = a + b
...     y = x * 2
...     print('Sample: ' + str(y))
...
>>> import dis
>>> dis.dis(sample)
2       0 LOAD_FAST                0 (a)
        3 LOAD_FAST                1 (b)
        6 BINARY_ADD
        7 STORE_FAST               2 (x)
3      10 LOAD_FAST                2 (x)
       13 LOAD_CONST               1 (2)
       16 BINARY_MULTIPLY
       17 STORE_FAST               3 (y)
4      20 LOAD_GLOBAL              0 (print)
       23 LOAD_CONST               2 ('Sample: ')
       26 LOAD_GLOBAL              1 (str)
       29 LOAD_FAST                3 (y)
       32 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
       35 BINARY_ADD
       36 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
       39 POP_TOP
       40 LOAD_CONST               0 (None)
       43 RETURN_VALUE
```

Remarquez que chaque ligne en bytecode référence sa position respective dans le code source sur la colonne de gauche, et que ce n'est pas une relation un-à-un. Il pourrait y avoir plusieurs opérations plus petites — on pourrait même dire atomiques — qui composent une instruction de niveau supérieur.

Un _frame object_ en Python est ce qui représente un cadre d'exécution. Il contient une référence à l'objet de code qui est actuellement en cours d'exécution, les variables locales avec lesquelles il fonctionne, les noms globaux (variables) qui sont disponibles et les références à tous les cadres associés (comme le parent qui l'a engendré).

Il y a beaucoup plus de détails sur ces objets à discuter ici, mais espérons que cela suffira à aiguiser votre appétit. Vous n'aurez pas besoin de beaucoup plus pour les besoins de notre débogueur, bien que vous devriez consulter la section Plonger plus profondément pour des liens sur où regarder ensuite.

### Entrée du module sys

Python fournit un certain nombre d'utilitaires dans sa bibliothèque standard via le module _sys_. Non seulement il y a des choses comme _sys.path_ pour obtenir le chemin Python ou _sys.platform_ pour aider à trouver des détails sur le système d'exploitation dans lequel vous exécutez, mais il y a aussi `sys.settrace()` et `sys.setprofile()` pour aider à écrire des outils de langage.

Oui, vous avez bien lu. Python dispose déjà de crochets intégrés pour aider à analyser le code et interagir avec l'exécution du programme. La fonction `sys.settrace()` vous permettra d'exécuter un rappel chaque fois que l'exécution avance vers un nouvel objet de cadre et nous donne une référence à celui-ci, qui à son tour fournit l'objet de code avec lequel vous travaillez.

Pour un exemple rapide de ce à quoi cela ressemble, réutilisons la fonction de tout à l'heure :

```py
def sample(a, b):
    x = a + b
    y = x * 2
    print('Sample: ' + str(y))
```

En supposant que chaque fois qu'un nouveau cadre est exécuté, vous voulez un rappel qui imprime l'objet de code et le numéro de ligne qu'il exécute, vous pouvez le définir comme suit :

```py
def trace_calls(frame, event, arg):
    if frame.f_code.co_name == "sample":
        print(frame.f_code)
```

Maintenant, il suffit simplement de le définir comme notre rappel de trace :

```py
sys.settrace(trace_calls)
```

Et l'exécution de _sample(3,2)_ devrait produire

```
$ python debugger.py
<code object sample at 0x0000000000B46C90, file ".\test.py", line 123>
Sample: 10
```

Vous avez besoin de l'instruction if pour filtrer les appels de fonction. Sinon, vous verrez un tas de choses qui ne vous intéressent pas, surtout lorsque vous imprimez à l'écran. Essayez.

Les objets de code et de cadre ont assez de champs pour décrire ce qu'ils représentent. Cela inclut des choses comme le fichier en cours d'exécution, la fonction, les noms de variables, les arguments, les numéros de ligne, et la liste est longue. Ils sont fondamentaux pour l'exécution de tout code Python et vous pouvez parcourir la documentation du langage pour plus de détails.

### Que faire si vous voulez déboguer chaque ligne ?

Le mécanisme de trace définira des rappels ultérieurs en fonction de la valeur de retour du premier rappel. Retourner _None_ signifie que vous avez terminé, tandis que retourner une autre fonction l'établit effectivement comme la fonction de trace à l'intérieur de ce cadre.

Voici à quoi cela ressemble :

```
5    def sample(a, b):
6        x = a + b
7        y = x * 2
8        print('Sample: ' + str(y))
9
10   def trace_calls(frame, event, arg):
11       if frame.f_code.co_name == "sample":
12           print(frame.f_code)
13           return trace_lines
14       return
15
16   def trace_lines(frame, event, arg):
17       print(frame.f_lineno)
```

Maintenant, si vous exécutez le même code qu'avant, vous pouvez voir qu'il imprime les numéros de ligne au fur et à mesure que vous progressez :

```
$ python .\test.py
<code object sample at 0x00000000006D4DB0, file ".\test.py", line 5>
6
7
8
Sample: 10
8
```

### Mettre une interface utilisateur devant

En utilisant le module Python [_sofi_](https://github.com/tryexceptpass/sofi), vous pouvez facilement produire une application web qui interagit directement avec notre code Python.

Voici ce que vous feriez :

1. Afficher le fichier, le nom de la fonction et le numéro de ligne en cours d'exécution.
2. Afficher le code pour le cadre actuel avec un pointeur identifiant la ligne.
3. Afficher la valeur des variables locales.
4. Fournir une exécution pas à pas, ce qui signifie que vous devez bloquer avant d'exécuter une ligne jusqu'à ce que l'utilisateur clique sur un bouton.
5. Ajouter une fonctionnalité de pas à pas.
6. Ajouter un mécanisme de sortie pas à pas.
7. Fournir une méthode pour arrêter l'exécution.

Du point de vue de l'interface utilisateur, #1, #2 et #3 peuvent tous être gérés via un _Panel_ Bootstrap où #1 est le titre, et #2 et #3 font partie du corps enveloppé dans des balises _samp_ pour montrer l'espacement approprié.

Puisque l'interface bloquera essentiellement en attendant l'entrée de l'utilisateur, et que le débogueur attend les commandes stop/go, il est bon de séparer ces boucles d'événements en utilisant notre vieil ami _multiprocessing_. Vous pouvez ensuite implémenter une _queue_ pour envoyer des commandes de débogage à un processus, et une queue d'application différente pour les mises à jour de l'interface utilisateur dans l'autre.

Via les queues de multiprocessing, il est facile de bloquer le débogueur en attendant les commandes de l'utilisateur dans la fonction _trace_lines_ en utilisant la méthode _.get()_.

Si la commande est donnée pour passer à la ligne de code suivante (#4), tout reste le même, tandis que la sortie pas à pas (#6) changera la valeur de retour à la fonction _trace_calls_ — supprimant effectivement les appels ultérieurs à _trace_lines_ — et stop (#7) lèvera une exception personnalisée qui interrompra l'exécution.

```py
# Bloquer jusqu'à ce que vous receviez une commande de débogage
cmd = trace_lines.debugq.get()
if cmd == 'step':
    # continuer à parcourir les lignes, retourner ce rappel
    return trace_lines
elif cmd == 'stop':
    # Arrêter l'exécution
    raise StopExecution()
elif cmd == 'over':
    # sortir ou passer par-dessus le code, donc pointer vers trace_calls
    return trace_calls
class StopExecution(Exception):
    """Exception personnalisée utilisée pour interrompre l'exécution du code"""
    pass
```

La fonctionnalité de pas à pas (#5) est implémentée au niveau de _trace_calls_ en ne retournant jamais le rappel trace_lines.

```py
cmd = trace_lines.debugq.get()
if cmd == 'step':
    return trace_lines
elif cmd == 'over':
    return
```

Oui, j'ai attaché les objets de queue en tant que propriétés des fonctions de trace pour simplifier le passage des choses. Les fonctions étant des objets est une excellente idée, bien que vous ne devriez pas en abuser non plus.

Maintenant, il suffit simplement de configurer les widgets pour afficher les données et les boutons pour contrôler le flux.

Vous pouvez extraire le code source de l'objet de code du cadre en cours d'exécution en utilisant le module inspect.

```
source = inspect.getsourcelines(frame.f_code)[0]
```

Maintenant, il s'agit de le formater ligne par ligne dans des balises _div_ et _samp_, en ajoutant un indicateur de couleur différente à la ligne actuelle (disponible via `f_lineno` et `co_firstline`) et en collant cela dans le corps d'un widget _panel_, ainsi que la représentation sous forme de chaîne des locaux du cadre (qui est un simple dictionnaire de toute façon) :

```py
def formatsource(source, firstline, currentline):
    for index, item  in enumerate(source):
        # Créer un div pour chaque ligne pour mieux contrôler le format
        div = Div()
        # Vérification extrêmement simplifiée de l'index de tabulation pour ajouter un espace vide
        if item[0:1] == '\t' or item[0:1] == ' ':
            div.style ='margin-left:15px;'
        # Si cette ligne est actuellement en cours d'exécution, ajouter une marque rouge
        if index == lineno - firstlineno:
            div.addelement(Bold('> ', style="color:red"))
        # Ajouter le code formaté au div
        div.addelement(Sample(item.replace("\n", "")))
        # Sortir le html qui représente ce div
        source[index] = str(div)
    return "".join(source)
```

La seule chose restante à faire est d'enregistrer quelques rappels d'événements pour les clics de boutons qui contrôlent le flux d'exécution en ajoutant leurs commandes respectives à la file d'attente de débogage. Vous faites cela à l'intérieur d'un gestionnaire d'événements _load_ qui se déclenche après que le contenu initial a fini de charger

```py
@asyncio.coroutine
def load(event):
    """Appelé lorsque le html initial finit de charger"""
    # Démarrer le processus de débogage
    debugprocess.start()
    # Enregistrer les fonctions de clic
    app.register('click', step, selector="#code-next-button")
    app.register('click', stop, selector="#code-stop-button")
    app.register('click', over, selector="#code-over-button")
    # Assurer la mise à jour de l'affichage
    yield from display()
@asyncio.coroutine
def step(event):
    debugq.put("step")
    # Assurer la mise à jour de l'affichage
    yield from display()
@asyncio.coroutine
def stop(event):
    debugq.put("stop")
@asyncio.coroutine
def over(event):
    debugq.put("over")
```

À quoi cela ressemblerait-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*oV3Gp3r2-5XjhrnV2nvKcw.png)

Pour une vue de tout le code assemblé, consultez le projet sofi-debugger sur GitHub :

[**tryexceptpass/sofi-debugger**](https://github.com/tryexceptpass/sofi-debugger)  
[_Contribute to sofi-debugger development by creating an account on GitHub._github.com](https://github.com/tryexceptpass/sofi-debugger)

#### Quelques notes sur ce que vous venez de faire

Les fonctions du module _sys_ mentionnées ici sont implémentées dans CPython et peuvent ne pas être disponibles dans d'autres versions ou interpréteurs. Assurez-vous de garder cela à l'esprit lorsque vous expérimentez.

Elles sont également spécifiquement destinées à être utilisées avec des débogueurs, des profileurs ou des outils de trace similaires. Cela signifie que vous ne devriez pas les manipuler dans le cadre d'un programme normal, sinon vous pourriez rencontrer des conséquences imprévues, surtout lorsque vous interagissez avec d'autres modules qui peuvent cibler spécifiquement ces mêmes interfaces (comme les débogueurs réels).

### Plonger plus profondément

Pour une plongée plus profonde dans les constructions du langage Python, les cadres, les objets de code et le module dis, je vous recommande vivement de prendre le temps et de suivre les conférences sur les internes de CPython de Phillip Guo (@pgbovine).

%[https://youtu.be/LhadeL7_EIU]

---

Si vous avez aimé l'article et que vous souhaitez en lire plus sur Python et les pratiques logicielles, veuillez visiter [tryexceptpass.org](https://tryexceptpass.org). Restez informé avec leur dernier contenu en vous abonnant à [la liste de diffusion](https://tinyurl.com/tryexceptpass-signup).