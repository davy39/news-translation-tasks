---
title: Introduction aux tests basés sur les propriétés en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T18:11:37.000Z'
originalURL: https://freecodecamp.org/news/intro-to-property-based-testing-in-python-6321e0c2f8b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tMpDMEqLKd5ApfTbLlPvAQ.jpeg
tags:
- name: automation
  slug: automation
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Introduction aux tests basés sur les propriétés en Python
seo_desc: 'By Shashi Kumar Raja

  In this article we will learn a unique and effective approach to testing called
  property-based testing. We will use Python , pytest and Hypothesis to implement
  this testing approach.

  The article is going to use basic pytest conce...'
---

Par Shashi Kumar Raja

Dans cet article, nous allons apprendre une approche unique et efficace des tests appelée test basé sur les propriétés. Nous allons utiliser [**Python**](https://www.python.org/), [**pytest**](https://docs.pytest.org/en/latest/) et [**Hypothesis**](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python) pour implémenter cette approche de test.

L'article va utiliser des **concepts de base de pytest** pour expliquer le test basé sur les propriétés. Je recommande de [lire cet article](https://medium.com/testcult/intro-to-test-framework-pytest-5b1ce4d011ae) pour rafraîchir rapidement vos connaissances sur pytest.

Nous allons commencer par la méthode conventionnelle de test unitaire/fonctionnel connue sous le nom de **test basé sur des exemples** — que la plupart d'entre nous utilisons. Nous essayons d'en trouver les lacunes, puis nous passons à l'approche basée sur les propriétés pour éliminer ces lacunes.

**Tout grand tour de magie se compose de trois parties ou actes.** La première partie est appelée « The Pledge ». **Le magicien vous montre quelque chose d'ordinaire** : un jeu de cartes, un oiseau ou un homme. Il vous montre cet objet. Peut-être vous demande-t-il de l'inspecter pour voir s'il est bien réel, inchangé, normal. Mais bien sûr… il ne l'est probablement pas.

### **Partie 1 : Test basé sur des exemples**

L'approche du test basé sur des exemples comprend les étapes suivantes :

* donné une entrée de test **I**
* lorsqu'elle est passée à la fonction sous test
* doit retourner une sortie **O**

Donc, en gros, nous donnons une entrée fixe et attendons une sortie fixe.

Pour comprendre ce concept en termes simples :

![Image](https://cdn-media-1.freecodecamp.org/images/m7FH-CRisIZWzUnoc1EPe-iVBnlnsPq7v5oO)
_Une machine sous test_

Supposons que nous avons une machine qui prend du plastique de n'importe quelle forme et de n'importe quelle couleur en entrée et produit une balle en plastique parfaitement ronde de la même couleur en sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/zckP-x7-ih8gEOlOA297GY96segy4DzSr7R-)
_Photo par [Unsplash](https://unsplash.com/photos/9IBqihqhuHc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Greyson Joralemon</a> sur <a href="https://unsplash.com/search/photos/ball?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Maintenant, pour tester cette machine en utilisant le test basé sur des exemples, nous allons suivre l'approche ci-dessous :

1. prendre un plastique brut de couleur bleue (**données de test fixes**)
2. alimenter le plastique dans la machine
3. attendre une balle en plastique de couleur bleue en sortie (**sortie de test fixe**)

Voyons la même approche de manière programmatique.

**Prérequis :** assurez-vous d'avoir **Python** (version 2.7 ou supérieure) et **pytest** installés.

Créez une structure de répertoire comme ceci :

```
- demo_tests/    - test_example.py
```

Nous allons écrire une petite fonction `sum` dans le fichier `test_example.py`. Celle-ci accepte deux nombres — `num1` et `num2` — comme paramètres et retourne l'addition des deux nombres comme résultat.

```
def sum(num1, num2):    """Elle retourne la somme de deux nombres"""    return num1 + num2
```

Maintenant, écrivons un test pour tester cette fonction sum en suivant la méthode conventionnelle.

```
import pytest
```

```
# assurez-vous de commencer le nom de la fonction par test
def test_sum():    assert sum(1, 2) == 3
```

Ici, vous pouvez voir que nous passons les deux valeurs `1` et `2` et attendons que la somme retourne `3`.

Exécutez les tests en vous rendant dans le dossier `demo_tests` puis en exécutant la commande suivante :

```
pytest test_example.py -v
```

![Image](https://cdn-media-1.freecodecamp.org/images/L75EB0a6hV88U5YPPBZO6IMDgu76N9WrT8Ue)
_1 cas de test réussi_

**Ce test est-il suffisant** pour vérifier la fonctionnalité de la fonction `sum` ?

Vous pensez peut-être, bien sûr que non. Nous allons écrire plus de tests en utilisant la fonctionnalité `[pytest parametrize](https://docs.pytest.org/en/latest/reference.html#pytest-mark-parametrize-ref)` qui exécutera cette fonction `test_sum` pour toutes les valeurs données.

```
import pytest
```

```
@pytest.mark.parametrize('num1, num2, expected',[(3,5,8),              (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)])def test_sum(num1, num2, expected):        assert sum(num1, num2) == expected
```

![Image](https://cdn-media-1.freecodecamp.org/images/hKA2-UFjpR4kcxp3zl3Qwdzci0JGihG37Qel)
_Tous les 5 tests réussis_

L'utilisation de cinq tests a donné plus de confiance quant à la fonctionnalité. Les voir tous réussir est un vrai bonheur.

**Mais**, si vous regardez de plus près, nous faisons la même chose que précédemment mais pour un plus grand nombre de valeurs. Nous ne couvrons toujours pas plusieurs cas limites.

Nous avons donc découvert le premier point faible de cette méthode de test :

#### Problème 1 : L'exhaustivité des tests dépend de la personne qui écrit le test

Elle peut choisir d'écrire 5, 50 ou 500 cas de test mais reste toujours incertaine d'avoir couvert la plupart, sinon tous, les cas limites.

Cela nous amène à notre deuxième point faible :

#### Problème 2 — Tests non robustes en raison d'une compréhension floue/ambiguë des exigences

Lorsque nous avons été invités à écrire notre fonction `sum`, quelles détails spécifiques nous ont été communiqués ?

Nous a-t-on dit :

* quel type d'entrée notre fonction devrait-elle attendre ?
* comment notre fonction devrait-elle se comporter dans des scénarios d'entrée inattendus ?
* quel type de sortie notre fonction devrait-elle retourner ?

Pour être plus précis, si vous considérez la fonction `sum` que nous avons écrite ci-dessus :

* savons-nous si `num1`, `num2` doivent être un `int` ou `float` ? Peuvent-ils également être envoyés comme type `string` ou tout autre type de données ?
* quelle est la valeur **minimale** et **maximale** de `num1` et `num2` que nous devons supporter ?
* comment la fonction doit-elle se comporter si nous obtenons des entrées `null` ?
* la sortie retournée par la fonction sum doit-elle être `int` ou `float` ou `string` ou tout autre type de données ?
* dans quels scénarios doit-elle afficher des messages d'erreur ?

De plus, le **pire scénario** de l'approche d'écriture de cas de test ci-dessus est que ces cas de test peuvent être **trompés pour réussir par des fonctions boguées**.

Réécrivons notre fonction `sum` de manière à introduire des erreurs mais les tests que nous avons écrits jusqu'à présent réussissent toujours.

```
def sum(num1, num2):    """Logique boguée"""       if num1 == 3 and num2 == 5:        return 8    elif num1 == -2 and num2  == -2 :        return -4    elif num1 == -1 and num2 == 5 :        return 4    elif num1 == 3 and num2 == -5:        return -2    elif num1 == 0 and num2 == 5:        return 5
```

![Image](https://cdn-media-1.freecodecamp.org/images/bSc5z1g7bA-MNwjrH10rpeMLT0cFfdxWJLRJ)
_Tous les tests réussissent toujours_

Maintenant, plongeons dans le test basé sur les propriétés pour voir comment ces points faibles sont atténués.

Le deuxième acte est appelé « The Turn ». **Le magicien prend quelque chose d'ordinaire et le fait faire quelque chose d'extraordinaire.** Maintenant, vous cherchez le secret… mais vous ne le trouverez pas, car bien sûr vous ne cherchez pas vraiment. Vous ne voulez pas vraiment savoir. Vous voulez être trompé.

### **Partie 2 : Test basé sur les propriétés**

#### Introduction et génération de données de test

Le test basé sur les propriétés a été introduit pour la première fois par le **framework [QuickCheck](https://en.wikipedia.org/wiki/QuickCheck)** dans [**Haskell**](https://en.wikipedia.org/wiki/Haskell_(programming_language)). Selon la documentation de [fast-check](https://github.com/dubzzz/fast-check), qui est une autre bibliothèque de test basée sur les propriétés-

> Les frameworks de test basés sur les propriétés vérifient la véracité des propriétés. Une propriété est une déclaration comme :

> _pour tous (x, y, …)_

> _tels que la précondition(x, y, …) est respectée_

> _la propriété(x, y, …) est vraie_.

Pour comprendre cela, revenons à notre exemple de machine générant des balles en plastique.

L'approche de test basée sur les propriétés de cette machine sera :

1. prendre une grande sélection de plastiques en entrée (`all(x, y, …)`)
2. s'assurer qu'ils sont tous colorés (`precondition(x, y, …)`)
3. la sortie satisfait la propriété suivante (`property(x, y, …)`) -

![Image](https://cdn-media-1.freecodecamp.org/images/i4FIwt-tprqcH2nPnlQCVEyJySg96QqnHRSB)
_Photo par [Unsplash](https://unsplash.com/photos/wJ0tVIs09N8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Melanie Magdalena</a> sur <a href="https://unsplash.com/search/photos/ball?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

* **la sortie est ronde/sphérique en forme**
* **la sortie est colorée**
* **la couleur de la sortie est l'une des couleurs présentes dans la bande de couleur**

Remarquez comment, à partir de valeurs fixes d'entrée et de sortie, nous avons **généralisé** nos données de test et notre sortie de manière à ce que **la propriété doive être vraie** pour toutes les entrées valides. C'est le test basé sur les propriétés.

De plus, remarquez que lorsque nous pensons en termes de propriétés, nous devons réfléchir plus profondément et différemment. Par exemple, lorsque nous avons eu l'idée que puisque notre sortie est une balle, elle doit être ronde, une autre question vous viendra à l'esprit — **la balle doit-elle être creuse ou solide** ?

Ainsi, en nous faisant réfléchir plus profondément et en nous posant plus de questions sur les exigences, l'approche de test basée sur les propriétés rend notre implémentation des exigences robuste.

Maintenant, revenons à notre fonction sum et testons-la en utilisant l'approche basée sur les propriétés.

La **première question** qui se pose ici est : quelle doit être l'entrée de la fonction `sum` ?

Pour les besoins de cet article, nous supposerons que toute **paire** d'**entiers** de l'ensemble des entiers est une entrée valide.

![Image](https://cdn-media-1.freecodecamp.org/images/WGD85QpyuDvVBb271y3upv6d1NmegJxoYk6y)
_**Système de coordonnées cartésien**_

Ainsi, tout ensemble de valeurs entières situé dans le système de coordonnées ci-dessus sera une entrée valide pour notre fonction.

La **question suivante** est : comment obtenir de telles données d'entrée ?

La **réponse** à cela est : une bibliothèque de test basée sur les propriétés vous fournit la fonctionnalité de générer un grand ensemble de données d'entrée souhaitées suivant une précondition.

En Python, [**Hypothesis**](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python) est une bibliothèque de test de propriétés qui vous permet d'écrire des tests avec pytest. Nous allons utiliser cette bibliothèque.

Toute la documentation de Hypothesis est magnifiquement écrite et disponible 🔗 [**ici**](https://hypothesis.readthedocs.io/en/latest/quickstart.html) et je vous recommande de la parcourir.

Pour installer Hypothesis :

```
pip install hypothesis
```

et nous sommes prêts à utiliser hypothesis avec pytest.

Maintenant, réécrivons la fonction `test_sum` — que nous avons écrite précédemment — avec de nouveaux ensembles de données générés par Hypothesis.

```
from hypothesis import given
```

```
import hypothesis.strategies as st
```

```
import pytest
```

```
@given(st.integers(), st.integers())def test_sum(num1, num2):    assert sum(num1, num2) == num1 + num2
```

* La première ligne importe simplement `given` depuis Hypothesis. Le décorateur `[**@given**](https://hypothesis.readthedocs.io/en/master/details.html#hypothesis.given)` prend notre fonction de test et la transforme en une fonction paramétrée. Lorsqu'elle est appelée, cela exécutera la fonction de test sur une large gamme de données correspondantes. C'est le point d'entrée principal vers Hypothesis.
* La deuxième ligne importe `[**strategies**](https://hypothesis.readthedocs.io/en/master/data.html#module-hypothesis.strategies)` depuis Hypothesis. **strategies fournit la fonctionnalité de générer des données de test**. Hypothesis fournit des stratégies pour la plupart des types intégrés avec des arguments pour contraindre ou ajuster la sortie. De plus, des stratégies d'ordre supérieur peuvent être composées pour générer des types plus complexes.
* Vous pouvez générer n'importe lequel ou un mélange des éléments suivants en utilisant des stratégies :

```
'nothing','just', 'one_of','none','choices', 'streaming','booleans', 'integers', 'floats', 'complex_numbers', 'fractions','decimals','characters', 'text', 'from_regex', 'binary', 'uuids','tuples', 'lists', 'sets', 'frozensets', 'iterables','dictionaries', 'fixed_dictionaries','sampled_from', 'permutations','datetimes', 'dates', 'times', 'timedeltas','builds','randoms', 'random_module','recursive', 'composite','shared', 'runner', 'data','deferred','from_type', 'register_type_strategy', 'emails'
```

* Ici, nous avons généré un ensemble `integers()` en utilisant des stratégies et l'avons passé à `@given`.
* Ainsi, notre fonction `test_sum` devrait s'exécuter pour toutes les itérations de l'entrée donnée.

Exécutons-la et voyons le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/FZs22eokZCjGPk5g5NclIA5gxGkVa3CFGNT6)

Vous pensez peut-être, je ne vois aucune différence ici. **Qu'y a-t-il de si spécial dans cette exécution ?**

Eh bien, pour voir la différence magique, nous devons exécuter notre test en définissant l'option `verbose`. Ne confondez pas ce verbose avec l'option `-v` de pytest.

```
from hypothesis import given, settings, Verbosity
```

```
import hypothesis.strategies as stimport pytest
```

```
@settings(verbosity=Verbosity.verbose)@given(st.integers(), st.integers())def test_sum(num1, num2):    assert sum(num1, num2) == num1 + num2
```

`[settings](https://hypothesis.readthedocs.io/en/latest/settings.html?highlight=verbosity#hypothesis.settings)` nous permet de modifier le comportement de test par défaut de Hypothesis.

Maintenant, réexécutons les tests. Incluez également `-s` cette fois pour capturer la sortie du flux dans pytest.

```
pytest test_example.py -v -s
```

![Image](https://cdn-media-1.freecodecamp.org/images/ng0wZl-aean3O9L9AzRXMC04nMD-LScmNhnp)

![Image](https://cdn-media-1.freecodecamp.org/images/Vsa1HdRqp7hm9Igr-65fbg8iOj68EhcTwqXH)
_Zoomez et voyez les cas générés_

Regardez le nombre impressionnant de cas de test générés et exécutés. Vous pouvez trouver toutes sortes de cas ici, comme 0, de grands nombres et des nombres négatifs.

Vous pensez peut-être, c'est impressionnant, mais je ne trouve pas ma paire de cas de test préférée **(1,2)** ici. Que faire si je veux l'exécuter ?

Eh bien, ne craignez rien, Hypothesis vous permet d'exécuter un ensemble donné de cas de test à chaque fois si vous le souhaitez en utilisant le décorateur `@[example](https://hypothesis.readthedocs.io/en/latest/reproducing.html#hypothesis.example)`.

```
from hypothesis import given, settings, Verbosity, example
```

```
import hypothesis.strategies as stimport pytest
```

```
@settings(verbosity=Verbosity.verbose)@given(st.integers(), st.integers())@example(1, 2)def test_sum(num1, num2):    assert sum(num1, num2) == num1 + num2
```

![Image](https://cdn-media-1.freecodecamp.org/images/qZ5ExSZ0IPNnBb7Tmgn4nlfWgj15DMI-UpxT)
_Un exemple est toujours inclus dans l'exécution du test._

De plus, remarquez que chaque exécution générera **toujours** un nouveau cas de test mélangé suivant la stratégie de génération de test, randomisant ainsi l'exécution du test.

Ainsi, cela résout notre premier point faible — l'exhaustivité des cas de test.

#### Réfléchir profondément pour trouver des propriétés à tester

Jusqu'à présent, nous avons vu une magie du test basé sur les propriétés qui génère des données de test souhaitées à la volée.

Maintenant, passons à la partie où nous devons réfléchir profondément et différemment pour créer des tests qui sont valides pour toutes les entrées de test **mais** uniques à la fonction `sum`.

```
1 + 0 = 10 + 1 = 15 + 0 = 5-3 + 0 = -38.5 + 0 = 8.5
```

C'est intéressant. Il semble que l'ajout de `0` à un nombre donne le même nombre comme somme. Cela s'appelle la **propriété d'identité de l'addition.**

En voici une autre :

```
2 + 3 = 53 + 2 = 5
```

```
5 + (-2) = 3-2 + 5 = 3
```

Il semble que nous avons trouvé une autre propriété unique. Dans l'addition, l'ordre des paramètres n'a pas d'importance. Placés à gauche ou à droite du signe +, ils donnent le même résultat. Cela s'appelle la **propriété commutative de l'addition.**

Il y en a une autre, mais je veux que vous la trouviez.

Maintenant, nous allons réécrire notre `test_sum` pour tester ces propriétés :

```
from hypothesis import given, settings, Verbosity
```

```
import hypothesis.strategies as stimport pytest
```

```
@settings(verbosity=Verbosity.verbose)@given(st.integers(), st.integers())def test_sum(num1, num2):    assert sum(num1, num2) == num1 + num2
```

```
    # Test de la propriété d'identité    assert sum(num1, 0) = num1     #Test de la propriété commutative      assert sum(num1, num2) == sum(num2, num1)
```

![Image](https://cdn-media-1.freecodecamp.org/images/D8jFAkd4rmmU2oJ33Aph8rzg4L45XCEJVeG-)
_Tous les tests réussis._

Notre test est maintenant exhaustif — nous avons également converti les tests pour les rendre plus robustes. Ainsi, nous avons résolu notre deuxième point faible : **les cas de test non robustes**.

Par simple curiosité, essayons de tromper ce test avec ce code bogué que nous avons utilisé auparavant.

![Image](https://cdn-media-1.freecodecamp.org/images/U-MgU3hJg89yCZ2RPORm7Debvp6IECmVesSF)
_Pas de tromperie cette fois-ci._

> Comme le dit un vieux proverbe — trompe-moi une fois, honte à toi, trompe-moi deux fois, honte à moi.

Vous pouvez voir qu'il a attrapé une erreur. `Falsifying example: test_sum(num1=0, num2=0)`. Cela signifie simplement que notre propriété attendue n'était pas vraie pour ces paires de cas de test, d'où l'échec.

Mais vous n'applaudiriez pas encore. Parce que faire disparaître quelque chose ne suffit pas ; vous devez le faire revenir. **C'est pourquoi chaque tour de magie a un troisième acte, la partie la plus difficile, celle que nous appelons « The Prestige ».**

### **Partie 3 : Réduction des échecs**

La [**réduction**](https://hypothesis.readthedocs.io/en/master/data.html?highlight=shrink) est le processus par lequel Hypothesis essaie de produire des exemples lisibles par l'homme lorsqu'il trouve un échec. Il prend un exemple complexe et le transforme en un exemple plus simple.

Pour démontrer cette fonctionnalité, ajoutons une autre propriété à notre fonction `test_sum` qui dit que `num1` doit être inférieur ou égal à `30`.

```
from hypothesis import given, settings, Verbosity
```

```
import hypothesis.strategies as stimport pytest
```

```
@settings(verbosity=Verbosity.verbose)@given(st.integers(), st.integers())def test_sum(num1, num2):    assert sum(num1, num2) == num1 + num2
```

```
    # Test de la propriété d'identité    assert sum(num1, 0) = num1     #Test de la propriété commutative      assert sum(num1, num2) == sum(num2, num1)    assert num1 <= 30
```

Après avoir exécuté ce test, vous obtiendrez un journal de sortie intéressant sur le terminal ici :

```
collected 1 item
```

```
test_example.py::test_sum Trying example: test_sum(num1=0, num2=-1)Trying example: test_sum(num1=0, num2=-1)Trying example: test_sum(num1=0, num2=-29696)Trying example: test_sum(num1=0, num2=0)Trying example: test_sum(num1=-1763, num2=47)Trying example: test_sum(num1=6, num2=1561)Trying example: test_sum(num1=-24900, num2=-29635)Trying example: test_sum(num1=-13783, num2=-20393)
```

```
#Jusqu'à présent, tous les cas de test ont réussi mais le suivant va échouer
```

```
Trying example: test_sum(num1=20251, num2=-10886)assert num1 <= 30AssertionError: assert 20251 <= 30
```

```
#Maintenant, la fonctionnalité de réduction entre en jeu et elle va essayer de trouver la valeur la plus simple pour laquelle le test échoue toujours
```

```
Trying example: test_sum(num1=0, num2=-2)Trying example: test_sum(num1=0, num2=-1022)Trying example: test_sum(num1=-165, num2=-29724)Trying example: test_sum(num1=-14373, num2=-29724)Trying example: test_sum(num1=-8421504, num2=-8421376)Trying example: test_sum(num1=155, num2=-10886)assert num1 <= 30AssertionError: assert 155 <= 30
```

```
# Jusqu'à présent, elle l'a réduit à 155
```

```
Trying example: test_sum(num1=0, num2=0)Trying example: test_sum(num1=0, num2=0)Trying example: test_sum(num1=64, num2=0)assert num1 <= 30AssertionError: assert 64 <= 30
```

```
# Réduit à 64
```

```
Trying example: test_sum(num1=-30, num2=0)Trying example: test_sum(num1=0, num2=0)Trying example: test_sum(num1=0, num2=0)Trying example: test_sum(num1=31, num2=0)
```

```
# Réduit à 31
```

```
Trying example: test_sum(num1=-30, num2=0)Falsifying example: test_sum(num1=31, num2=0)FAILED
```

```
# Et il conclut finalement que (num1=31, num2=0) est la donnée de test la plus simple pour laquelle notre propriété n'est pas vraie.
```

![Image](https://cdn-media-1.freecodecamp.org/images/UTMWf7wFBjnjqlrXX9CLUz0Df6zeVr6IiffK)
_Réduction en action._

Une autre bonne fonctionnalité — **elle va se souvenir de cet échec** pour ce test et inclura cet ensemble particulier de cas de test dans les exécutions futures pour s'assurer que la même régression ne se glisse pas à nouveau.

C'était une introduction en douceur à la magie du test basé sur les propriétés. Je recommande à tous d'essayer cette approche dans vos tests quotidiens. Presque tous les principaux langages de programmation prennent en charge le test basé sur les propriétés.

Vous pouvez trouver l'ensemble du code utilisé ici dans mon ? g[ithub repo.](https://github.com/shashikumarraja/pytest_tutorial/blob/master/src/tests/test_with_hypothesis.py)

Si vous avez aimé le contenu, montrez un peu ❤️