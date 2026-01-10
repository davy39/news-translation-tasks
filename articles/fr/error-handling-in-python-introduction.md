---
title: Gestion des erreurs en Python – try, except, else et finally expliqués avec
  des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-04-11T00:09:53.000Z'
originalURL: https://freecodecamp.org/news/error-handling-in-python-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/game-over-screen.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: Gestion des erreurs en Python – try, except, else et finally expliqués
  avec des exemples de code
seo_desc: 'By Gage Schaffer

  Just recently, my manager tasked me to create an automatic report. I designed the
  report to be simple. It included a few numbers from a database and some basic mathematical
  operations. I was excited to finally be able to show off my ...'
---

Par Gage Schaffer

Récemment, mon responsable m'a chargé de créer un rapport automatique. J'ai conçu le rapport pour qu'il soit simple. Il comprenait quelques chiffres d'une base de données et des opérations mathématiques de base. J'étais excité à l'idée de enfin pouvoir montrer mes compétences _incroyables_ en Python à l'entreprise.

J'ai terminé et livré le produit. Tout était parfait. Du moins, jusqu'à environ deux semaines plus tard. Mon rapport a commencé à échouer aléatoirement en raison d'une erreur de division par zéro. Cue la piste de rire.

Mon histoire courte manque de détails, mais elle devrait souligner l'importance de gérer les cas limites et les erreurs lors de la composition de programmes. Ce rapport aurait dû être une opportunité de montrer ma maîtrise de Python. Pourtant, cela s'est transformé en un moment un peu embarrassant, où je me suis retrouvé le visage contre terre.

Alors, prenons un moment pour apprendre les bases de la gestion des erreurs en utilisant la bibliothèque standard de Python. Je vais mettre en évidence certaines des choses dont vous avez besoin pour commencer.

Avant de commencer à gérer les exceptions, vous devriez avoir une bonne maîtrise des fondamentaux de Python. Vous devrez savoir pourquoi les exceptions sont levées pour pouvoir les gérer !

### Voici ce que nous allons couvrir :

1. [Les instructions Try et Except en Python](#heading-installation-des-instructions-try-et-except-en-python)
2. [Exécution conditionnelle avec la clause Else](#heading-execution-conditionnelle-avec-la-clause-else)
3. [Exceptions intégrées](#heading-exceptions-integrees)
4. [Exceptions personnalisées](#heading-exceptions-personnalisees)
5. [Considérations de performance](#heading-considerations-de-performance)

## Les instructions Try et Except en Python

Les instructions `try` et `except` sont la méthode principale pour gérer les exceptions. Elles ressemblent à ceci :

```python
x = 0
try:
    print(5 / x)
except ZeroDivisionError:
    print("Quelque chose s'est mal passé")
    
# Quelque chose s'est mal passé
```

Revue du code ci-dessus pour que nous soyons sur la même page :

1. La ligne 1 assigne la valeur 0 à une variable `x`
2. Les lignes 2 et 3 ouvrent une clause `try` et tentent de diviser 5 par la variable `x`
3. Les lignes 4 et 5 ouvrent une clause `except` pour toute `ZeroDivisionError` et instruisent le programme d'imprimer un message si nous essayons de diviser quelque chose par 0

Vous avez probablement remarqué le problème. Ma variable `x` a la valeur 0, et j'essaie de diviser 5 par `x`. Les meilleurs mathématiciens du monde ne peuvent pas diviser par 0, et Python non plus. Alors, que se passe-t-il ?

Si nous ne gérons pas l'erreur, le programme se terminera immédiatement en essayant de diviser 5 par `x`. Comme les programmes ne savent pas quoi faire avec les exceptions sans instructions explicites, nous avons créé la clause `except` à la ligne 4 et fourni les étapes pour que le programme suive en cas de division de quelque chose par 0.

C'est toute l'idée derrière la gestion des exceptions : vous devez dire au programme quoi faire lorsqu'il rencontre une erreur qu'il ne peut pas simplement ignorer. Regardons comment les clauses `try` et `except` fonctionnent.

### Décomposition de l'instruction Try

Les instructions `Try` et `Except` suivent un modèle qui vous permet de gérer de manière fiable les problèmes dans votre code. Passons en revue le modèle.

La première étape qui se produit est que le code dans la clause `try` tente de s'exécuter.

Après cela, nous avons trois possibilités :

#### Aucune erreur dans la clause Try

Si le code dans la clause `try` s'exécute **sans aucune erreur**, le programme :

1. Exécutera la clause `try`
2. Ignorera toutes les clauses `except`
3. Continuera à s'exécuter normalement

```python
x = 1
try:
    print(5 / x)
except ZeroDivisionError:
    print("Quelque chose s'est mal passé")

print("Je m'exécute après la clause try !")

# 5.0
# Je m'exécute après la clause try !
```

Vous pouvez voir que, dans cet exemple modifié, il n'y a aucun problème dans la clause `try` (lignes 3 et 4). Le code s'exécutera, la clause `except` sera ignorée, et le programme reprendra l'exécution après la conclusion des instructions `try` et `except`.

#### Erreurs dans la clause Try et l'exception est spécifiée

Si le code dans la clause `try` **lève une exception** et **le type d'exception est spécifié après un mot-clé `except`**, le programme :

1. Ignorera le reste du code dans la clause `try`
2. Exécutera tout code dans la clause `except` correspondante
3. Continuera à s'exécuter normalement

```python
x = 0
try:
    print(5 / x)
except:
    print("Quelque chose s'est mal passé")
    
print("Je m'exécute après la clause try !")

# Quelque chose s'est mal passé
# Je m'exécute après la clause try !
```

De retour à mon premier exemple, j'ai changé notre variable `x` pour qu'elle ait à nouveau la valeur 0 et j'ai essayé de diviser 5 par `x`. Cela produit une `ZeroDivisionError`. Puisque mon instruction `except` spécifie ce type d'exception, le code dans cette clause s'exécute avant que le programme ne reprenne son exécution normale.

#### Erreurs dans la clause Try et l'exception n'est pas spécifiée

Enfin, si le programme lève une exception dans la clause `try`, **mais que l'exception n'est pas spécifiée dans une instruction `except`**, alors le programme :

1. Arrêtera l'exécution du programme et lèvera l'erreur

```python
x = 0
try:
    print(5 / y)
except:
    print("Quelque chose s'est mal passé")

print("Je m'exécute après la clause try !")

# NameError: name 'y' is not defined
```

Dans l'exemple ci-dessus, j'essaie de diviser 5 par la variable `y`, qui n'existe pas. Cela lève une `NameError`. Je ne spécifie pas au programme comment gérer les `NameError`, donc la seule option est de se terminer.

### Nettoyage

`Try` et `except` sont les principaux outils pour gérer les erreurs, mais une clause optionnelle que vous pouvez utiliser s'appelle `finally`. La clause `finally` s'exécutera toujours, qu'il y ait une erreur ou non.

```python
x = 0
try:
    print(5 / x)
except ZeroDivisionError:
    print("Je suis la clause except !")
finally:
    print("Je suis la clause finally !")

print("Je m'exécute après la clause try !")

# Je suis la clause except !
# Je suis la clause finally !
# Je m'exécute après la clause try !
```

Dans cet exemple, j'ai créé notre célèbre `ZeroDivisionError`. Vous pouvez voir que l'ordre d'exécution est :

1. La clause `except`
2. La clause `finally`
3. Tout code ensuite

Une fois que nous corrigeons la clause `try` pour qu'elle ne lève plus d'erreur, vous verrez toujours un ordre d'exécution similaire. Au lieu que la clause `except` s'exécute, la clause `try` s'exécutera.

```python
x = 1
try:
    print(5 / x)
except ZeroDivisionError:
    print("Je suis la clause except !")
finally:
    print("Je suis la clause finally !")

print("Je m'exécute après la clause try !")

# 5.0
# Je suis la clause finally !
# Je m'exécute après la clause try !
```

Vous remarquerez que la seule différence est que la clause `try` est exécutée avec succès car il n'y a pas d'exceptions levées. La clause `finally` et le code ensuite s'exécutent comme vous vous y attendez.

Cela est utile pour certains cas où vous souhaitez nettoyer quoi qu'il arrive, quel que soit le résultat de vos clauses `try` et `except`. Des actions telles que la fermeture de connexions, la fermeture de fichiers et la journalisation sont de bons candidats pour la clause `finally`.

## Exécution conditionnelle avec la clause Else

L'autre clause optionnelle est la clause `else`. La clause `else` est simple : si le code dans la clause `try` s'exécute sans lever d'erreur, alors le code dans la clause `else` s'exécutera également.

```python
x = 1
try:
    print(5 / x)
except ZeroDivisionError:
    print("Je suis la clause except !")
else:
    print("Je suis la clause else !")
finally:
    print("Je suis la clause finally !")

print("Je m'exécute après la clause try !")

# 5.0
# Je suis la clause else !
# Je suis la clause finally !
# Je m'exécute après la clause try !
```

L'ordre d'exécution pour cet exemple est :

1. La clause `try`
2. La clause `else`
3. La clause `finally`
4. Tout code ensuite

Si nous devions rencontrer une exception ou une erreur dans la clause `try`, la clause `else` serait ignorée.

```python
x = 0
try:
    print(5 / x)
except ZeroDivisionError:
    print("Je suis la clause except !")
else:
    print("Je suis la clause else !")
finally:
    print("Je suis la clause finally !")

print("Je m'exécute après la clause try !")

# Je suis la clause except !
# Je suis la clause finally !
# Je m'exécute après la clause try !
```

## Exceptions intégrées

Vous m'avez vu écrire sur deux exceptions nommées différentes jusqu'à présent : `NameError` et `ZeroDivisionError`. Que faire si j'avais besoin d'autres exceptions ?

Il existe une liste complète des exceptions de Python qui accompagnent la bibliothèque standard. Celles-ci conviendront probablement à presque tous les besoins que vous avez pour gérer les erreurs ou exceptions.

En voici quelques-unes qui pourraient être importantes :

* `KeyError` – Une clé ne peut pas être trouvée dans un dictionnaire
* `IndexError` – L'index est hors limites sur un objet itérable
* `TypeError` – Une fonction ou une opération a été utilisée sur le mauvais type d'objet
* `OSError` – Erreurs générales du système d'exploitation

Il y en a beaucoup d'autres, que vous pouvez trouver dans la documentation Python. Je vous encourage à y jeter un coup d'œil. Non seulement vous serez meilleur dans la gestion des erreurs, mais vous explorerez également ce qui peut _réellement_ mal se passer avec vos programmes Python.

## Exceptions personnalisées

Si vous avez besoin de fonctionnalités étendues, vous pouvez également définir des exceptions personnalisées.

```python
class ForError(Exception):
    def __init__(self, message):
        self.message = message
    
    def foo(self):
        print("bar")
```

Dans l'exemple ci-dessus, je crée une nouvelle classe et l'étend à partir de la classe Exception. Maintenant, je peux écrire des fonctionnalités personnalisées et traiter cette exception comme n'importe quel autre objet.

```python
try:
    raise FooError("Ceci est une erreur de test")
except FooError as e:
    e.foo()

# bar
```

Ici, je lève mon nouveau `FooError` intentionnellement. Je capture le `FooError` et lui donne un alias `e`. Maintenant, je peux accéder à ma méthode `foo()` que j'ai intégrée dans la classe que j'ai créée.

Cela ouvre un grand nombre de possibilités lors de la gestion des erreurs. Journalisation personnalisée, suivi plus approfondi, ou tout ce dont vous avez besoin peut être codé et créé.

## Considérations de performance

Maintenant que vous comprenez les bases de `try`, `except` et des objets d'exception, vous pouvez commencer à envisager de les utiliser dans votre code pour gérer les erreurs de manière élégante. Y a-t-il des impacts considérables sur les performances du code, cependant ?

La réponse courte est non. Avec la sortie de Python 3.11, il n'y a pratiquement aucune réduction de vitesse due à l'utilisation des instructions `try` et `except` lorsqu'il n'y a pas d'exceptions levées.

La capture des erreurs causait certains ralentissements. Mais généralement, capturer ces erreurs est préférable à ce que l'ensemble du programme plante et brûle.

Dans les versions antérieures de Python, l'utilisation des clauses `try` et `except` causait un temps d'exécution supplémentaire. Gardez cela à l'esprit si vous n'êtes pas à jour.

## Pour résumer

Merci d'avoir lu jusqu'ici. Votre futur vous et vos clients vous remercieront pour votre gestion des erreurs.

Nous avons passé en revue les clauses `try`, `except`, `else` et `finally` et leur ordre d'exécution ainsi que les circonstances dans lesquelles elles sont exécutées. Nous avons également révisé les bases de la création d'exceptions personnalisées.

La chose la plus importante à retenir est que les clauses `try` et `except` sont les moyens principaux de capturer les erreurs, et vous devriez les utiliser chaque fois que vous avez un code risqué, sujet aux erreurs.

De plus, gardez à l'esprit que la capture des erreurs rendra votre code plus résilient et vous fera paraître comme un bien meilleur codeur.