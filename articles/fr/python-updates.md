---
title: Mises à jour de Python 3.9 expliquées avec des exemples de code pratiques
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2020-10-16T16:08:47.000Z'
originalURL: https://freecodecamp.org/news/python-updates
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Frame-19--2-.png
tags:
- name: Python
  slug: python
seo_title: Mises à jour de Python 3.9 expliquées avec des exemples de code pratiques
seo_desc: 'The latest stable release of Python is out!

  Open-source enthusiasts from all over the world have been working on new, enhanced,
  and deprecated features in Python for the past year.

  Though the beta versions have been rolling out for quite some time, t...'
---

La dernière version stable de Python est sortie !

Les passionnés d'open source du monde entier ont travaillé sur de nouvelles fonctionnalités améliorées et obsolètes dans Python au cours de l'année écoulée.

Bien que les versions bêta soient disponibles depuis un certain temps, la sortie officielle de Python 3.9.0 a eu lieu le **5 octobre 2020**.

%[https://twitter.com/llanga/status/1313207780954828808]

La documentation officielle contient tous les détails des dernières fonctionnalités et du journal des modifications. Tout au long de cet article, je vais vous présenter quelques fonctionnalités intéressantes qui pourraient vous être utiles dans vos tâches de programmation quotidiennes.

## Nous allons examiner les éléments suivants :

* **Indications de type génériques et annotations flexibles pour les fonctions et variables**

* **Opérateurs d'union dans les dictionnaires**

* `**zoneinfo**` **— Accès et calcul des fuseaux horaires**

* **Méthodes de chaîne pour supprimer les préfixes et suffixes**

* **Autres points forts de la version**

Pour me suivre ou pour essayer les nouvelles fonctionnalités, vous devez avoir Python 3.9 installé.

J'ai utilisé un gestionnaire d'environnement appelé [pyenv](https://github.com/pyenv/pyenv) (alternativement, vous pouvez utiliser conda) pour installer la dernière version aux côtés de ma version actuelle. Vous pouvez également l'exécuter en utilisant l'[image docker officielle](https://hub.docker.com/_/python/).

# Annotations flexibles pour les fonctions et variables

Les annotations de fonction existent depuis Python 3.0 et elles nous permettent d'ajouter des métadonnées aux fonctions Python. Alors, qu'y a-t-il de nouveau dans Python 3.9 ?

Python 3.9 a ajouté [**PEP 593**](https://www.python.org/dev/peps/pep-0593). Il a introduit un mécanisme pour étendre les annotations de type de [**PEP 484**](https://www.python.org/dev/peps/pep-0484) qui fournit la sémantique standard pour les annotations et suggérait que les annotations soient utilisées pour les indications de type.

Maintenant, il peut y avoir de nombreux autres cas d'utilisation pour les annotations en plus des indications de type. Ainsi, PEP 593 a introduit `typing.Annotated` qui vous permet d'ajouter plus de détails aux métadonnées.

Essayons de mieux comprendre cela via un exemple pour Python 3.8 et 3.9.

**Python 3.8**

```javascript
def currency_exchange(eur: "euros", rate: "taux de change") -> "euro vers USD":
    """Conversion d'euros en USD en utilisant le taux de change"""
    return eur * rate
```

Il s'agit d'une fonction simple qui convertit des euros en USD en utilisant le taux de change. Nous avons utilisé les annotations pour servir de documentation pour l'utilisateur.

**Python 3.9**

```javascript
from typing import Annotated
def currency_exchange(eur: Annotated[float, "euros"], rate: Annotated[float, "taux de change"]) -> Annotated[float, "euro vers dollars"]:
    """Conversion d'euros en dollars en utilisant le taux de change"""
    return eur * rate
```

Ici, nous utilisons le nouvellement introduit `Annotated` qui prend au moins deux arguments. Le premier argument (`float` dans l'exemple) établit l'indication de type, et le reste des arguments sont des métadonnées arbitraires de la fonction.

L'utilisateur/développeur peut également vérifier ces annotations en utilisant l'attribut `__annotations__` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/1-4.png align="left")

Nous pouvons également vérifier le type en utilisant la fonction `get_type_hint()` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/2-5.png align="left")

## Indications de type génériques dans les collections standard

Les types de données de base comme `int`, `str` ou `bool` sont simples à annoter.

La typographie statique précédente était construite de manière incrémentielle sur le runtime Python existant et contrainte par celui-ci. Cela a conduit à une hiérarchie de collections dupliquée dans le module de typage en raison des génériques — c'est-à-dire que nous avions à la fois `typing.List` et la liste intégrée.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/3-3.png align="left")

Avec les génériques, nous avons le problème de paramétrisation en raison de leur structure de stockage (qui est un conteneur). Et pour ces raisons, nous n'avons pas pu utiliser `list(float)` ou `list[float]` comme indications de type directement. Au lieu de cela, nous avions besoin d'un module de typage pour y parvenir.

Dans **Python 3.9**, cette hiérarchie dupliquée n'est plus nécessaire. Nous pouvons les annoter directement :

```javascript
scores: list(float)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/4-3.png align="left")

# Comment fusionner et mettre à jour des dictionnaires

Deux des fonctionnalités les plus cool et les plus utiles de Python 3.9 sont les opérateurs de fusion (|) et de mise à jour (|=) ajoutés à la classe `dict` intégrée.

Les méthodes existantes (3.8) de fusion de deux dictionnaires ont de nombreuses lacunes :

**Python 3.8**

* Le déballage de dictionnaire est laid et n'est pas facilement découvrable.

```javascript
python = {2000: "2.0.1", 2008: "2.6.9", 2010: "2.7.18"}
python3 = {2008: "3.0.1", 2009: "3.1.5", 2016: "3.6.12", 2020: "3.9.0"}

##fusion de deux dictionnaires
{**python, **python3}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/5-3.png align="left")

* Une autre méthode est dict.update qui modifie le dictionnaire original en place :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/6-3.png align="left")

**Python 3.9**

[**PEP 584**](https://www.python.org/dev/peps/pep-0584) a introduit deux nouveaux opérateurs pour les dictionnaires :

* **(|) union —** pour fusionner deux dictionnaires. Il préserve les dictionnaires originaux.

* **(|=) mise à jour —** cela est pour la fusion en place des dictionnaires.

```javascript
python = {2000: "2.0.1", 2008: "2.6.9", 2010: "2.7.18"}
python3 = {2008: "3.0.1", 2009: "3.1.5", 2016: "3.6.12", 2020: "3.9.0"}

##fusion de deux dictionnaires
python | python3
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/7-2.png align="left")

Dictionnaires originaux préservés :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/8-2.png align="left")

```javascript
python |= python3
python
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/9-2.png align="left")

L'opérateur de mise à jour fusionne les dictionnaires et met à jour le dictionnaire à gauche de l'opérateur tout en **conservant les dernières valeurs** pour les clés qui se chevauchent dans les deux dictionnaires.

# Comment travailler avec les fuseaux horaires — ZoneInfo

Les dates et l'heure jouent un rôle central dans de nombreuses applications. Python offre un support complet via le module `datetime` dans la bibliothèque standard. Mais il y a toujours eu un manque en ce qui concerne l'intégration des fuseaux horaires à ces timestamps.

Jusqu'à présent, nous avions des bibliothèques tierces comme dateutil pour implémenter de telles règles spécifiques aux fuseaux horaires.

Mais maintenant, Python 3.9 a ajouté un nouveau module `**zoneinfo**` qui vous permet d'accéder et d'utiliser l'ensemble de la base de données des fuseaux horaires de l'Internet Assigned Numbers Authority (IANA).

**Python 3.8**

Jusqu'à présent, nous avons accédé aux timestamps conscients des fuseaux horaires en utilisant l'argument `tzinfo` comme suit :

```javascript
from datetime import datetime, timezone

datetime.now(tz=timezone.utc)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/10-1.png align="left")

**Python 3.9**

Mais avec l'ajout de zoneinfo, nous avons maintenant accès à la [Base de données des fuseaux horaires de l'IANA](https://www.iana.org/time-zones).

```javascript
from zoneinfo import ZoneInfo

ZoneInfo("Asia/Kolkata")
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/11-1.png align="left")

Nous pouvons effectuer un ensemble d'opérations avec les fuseaux horaires, et l'interconversion est devenue très facile :

```javascript
from datetime import datetime
from zoneinfo import ZoneInfo

post_date = datetime(2020, 10, 10, 18, 10, tzinfo=ZoneInfo("America/Vancouver"))

post_date.astimezone(ZoneInfo("Asia/Kolkata"))
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/12-1.png align="left")

# **Méthodes de chaîne pour supprimer les préfixes et suffixes**

[**PEP 616**](https://www.python.org/dev/peps/pep-0616) a introduit de nouvelles méthodes pour supprimer les préfixes et suffixes des chaînes. Les nouvelles méthodes sont :

* **removeprefix()**

* **removesuffix()**

De nombreux problèmes récurrents ont été signalés sur tous les principaux forums (comme StackOverflow) concernant les méthodes `lstrip()` et `rstrip()`.

**Python 3.8**

Nous avons supprimé les caractères des deux extrémités de la chaîne en utilisant la méthode strip() comme suit :

```javascript
"Python 3.9 est sorti".strip(" Python")
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/13.png align="left")

Cela a supprimé la sous-chaîne présente aux extrémités de la chaîne. Si vous regardez attentivement, cela a supprimé les caractères individuels dans « python » c'est-à-dire « », « p », « y », « t », « h », « o » et « n ».

**Python 3.9**

Pour se débarrasser du préfixe d'une chaîne, nous avons maintenant `removeprefix()` :

```javascript
"Python 3.9 est sorti".removeprefix("Python ")
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/14.png align="left")

Vous pouvez vérifier cela avec un certain nombre d'autres permutations et combinaisons avec la méthode `removesuffix()` également.

# Autres points forts de la version

Outre ceux-ci, un certain nombre d'autres fonctionnalités ont également été introduites. Voici la liste avec les identifiants PEP :

* [**PEP 617**](https://www.python.org/dev/peps/pep-0617)**,** C**Python utilise maintenant un nouvel analyseur basé sur PEG —** Python dispose maintenant d'un nouvel analyseur aux côtés de l'ancien analyseur LL(1). Vous pouvez choisir d'exécuter votre programme en utilisant l'un des analyseurs avec la commande :

```javascript
python -X oldparser script_name.py
```

Les analyseurs PEG sont plus robustes et puissants selon les recherches de Guido van Rossum (il est le créateur de Python). Le but de l'analyseur PEG serait de produire le même **arbre de syntaxe abstraite (AST)** que l'ancien analyseur LL(1).

* **Initialisation multiphase** est maintenant disponible pour une utilisation dans un certain nombre de modules Python (`[audioop](https://docs.python.org/3/library/audioop.html#module-audioop)`, `_bz2`, `_codecs`, `_contextvars`, `_crypt`, `_functools`, `_json`, `_locale`, `[math](https://docs.python.org/3/library/math.html#module-math)`, `[operator](https://docs.python.org/3/library/operator.html#module-operator)`, `[resource](https://docs.python.org/3/library/resource.html#module-resource)`, `[time](https://docs.python.org/3/library/time.html#module-time)`, `_weakref`)

Voici un exemple de calcul du PGCD/PPCM de plus de deux nombres en utilisant la bibliothèque math :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/15.png align="left")

* [**PEP 602**](https://www.python.org/dev/peps/pep-0602) **CPython adopte maintenant un nouveau cycle de publication annuel** — Ils seront plus cohérents avec leurs publications et sortiront de nouvelles versions chaque octobre.

* [**PEP 614**](https://www.python.org/dev/peps/pep-0614), restrictions de grammaire assouplies sur les décorateurs — une syntaxe plus flexible est maintenant disponible pour les personnes travaillant sur des frameworks GUI comme PyQT. Cela lève la limitation sur les décorateurs consistant en un nom pointé. Plus de détails peuvent être lus [ici](https://www.python.org/dev/peps/pep-0614/).

Pour en savoir plus sur les détails de chacune de ces fonctionnalités, consultez la [documentation officielle](https://docs.python.org/3/whatsnew/3.9.html).

# Conclusion

3.9.0 marque une étape importante dans le développement de Python et pour la communauté. De nouvelles améliorations sont ajoutées en ce moment même et 3.10 aura également des fonctionnalités prometteuses.

Pour l'instant, vous devriez essayer ces fonctionnalités bientôt largement utilisées introduites dans **Python 3.9**.

Essayez d'exécuter vos programmes existants en utilisant Python 3.9 et voyez si la mise à jour en vaudrait la peine pour vous.

Vous devriez également essayer le nouveau parseur, qui promet d'être prometteur. Mais nous ne le saurons avec certitude qu'après des tests considérables dans plusieurs cas d'utilisation.

## [Data Science avec Harshit](https://www.youtube.com/c/DataSciencewithHarshit?sub_confirmation=1)

%[https://youtu.be/yapSsspJzAw]

Avec cette chaîne, je prévois de lancer quelques [séries couvrant tout l'espace de la science des données](https://towardsdatascience.com/hitchhikers-guide-to-learning-data-science-2cc3d963b1a2?source=---------8------------------). Voici pourquoi vous devriez vous abonner à la [chaîne](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) :

* Ces séries couvriront tous les tutoriels de qualité requis/demandés sur chacun des sujets et sous-sujets comme [Python fundamentals for Data Science](https://towardsdatascience.com/python-fundamentals-for-data-science-6c7f9901e1c8?source=---------5------------------).

* [Mathématiques et dérivations](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea?source=---------9------------------) expliquées de pourquoi nous faisons ce que nous faisons en ML et Deep Learning.

* [Podcasts avec des Data Scientists et Ingénieurs](https://www.youtube.com/watch?v=a2pkZCleJwM&t=2s) chez Google, Microsoft, Amazon, etc., et PDG de grandes entreprises axées sur les données.

* [Projets et instructions](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb?source=---------2------------------) pour implémenter les sujets appris jusqu'à présent. Apprenez les nouvelles certifications, Bootcamp, et ressources pour obtenir ces certifications comme cet [**Examen de certification TensorFlow Developer par Google.**](https://youtu.be/yapSsspJzAw)

Si ce tutoriel était utile, vous devriez consulter mes cours de data science et de machine learning sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une base solide de travail à présenter.