---
title: Comment fonctionne l'équation de Black-Scholes – Expliqué avec des exemples
  de code Python
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-06-17T16:42:59.000Z'
originalURL: https://freecodecamp.org/news/how-the-black-scholes-equation-works-python-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/dan-cristian-padure-h3kuhYUCE9A-unsplash.jpg
tags:
- name: finance
  slug: finance
- name: MathJax
  slug: mathjax
- name: Python
  slug: python
seo_title: Comment fonctionne l'équation de Black-Scholes – Expliqué avec des exemples
  de code Python
seo_desc: 'The Black-Scholes Equation is probably one of the most influential equations
  that nobody has heard about.

  It''s particularly important in finance, especially in these areas:


  Securitized debt

  Exchange-traded options

  Credit default swaps

  Over-the-count...'
---

L'équation de Black-Scholes est probablement l'une des équations les plus influentes que personne n'a jamais entendue.

Elle est particulièrement importante en finance, surtout dans ces domaines :

* Dette titrisée
* Options négociées en bourse
* Swaps de défaut de crédit
* Titres dérivés de gré à gré

Dans cet article, vous apprendrez pourquoi l'équation de Black-Scholes est si importante en finance, quels problèmes elle résout et les industries qu'elle a créées.

### Voici ce que nous allons couvrir :

* [Connaissances préalables en finance](#heading-connaissances-prealables-en-finance)
* [Analogie : Prédire le prix d'un billet pour un concert](#heading-analogie-predire-le-prix-dun-billet-pour-un-concert)
* [Explication en anglais simple avec exemple de code](#heading-black-scholes-en-anglais-simple-avec-un-exemple-de-code)
* [Implications dans le monde réel](#heading-implications-dans-le-monde-reel)

Note : Dans l'exemple de code, nous travaillerons avec des options d'achat et de vente européennes.

<h2 id='pre'>Connaissances préalables en finance</h2>

Pour tirer le meilleur parti de cet article et comprendre l'équation de Black-Scholes, vous devez simplement savoir ce que sont les **dérivés financiers** et les **options** en finance.

Essentiellement, les dérivés financiers sont des outils que les investisseurs utilisent pour gérer les risques et améliorer les rendements.

Il existe de nombreux types de dérivés financiers. L'un d'eux s'appelle les options.

Les options sont comme des choix financiers. Avec les options, vous pouvez obtenir le droit d'acheter ou de vendre quelque chose à un certain moment et à un certain prix, mais seulement si vous le souhaitez.

L'idée principale est qu'elles aident à gérer le risque afin que vous puissiez faire de meilleurs investissements à l'avenir.

<h2 id='analogy'>Analogie : Prédire le prix d'un billet pour un concert</h2>

Imaginez que vous prévoyez d'acheter un billet pour un concert.

Les prix des billets changent en fonction de la popularité de l'artiste, de la demande et du temps restant jusqu'au concert.

En fonction de cela, vous prendrez la meilleure décision possible pour acheter le billet au prix le plus bas.

Tout comme vous pensez au **risque** d'acheter le billet à un certain moment, les investisseurs utilisent l'équation de Black-Scholes pour estimer la valeur équitable des dérivés financiers.

De cette façon, ils s'assurent de faire des choix d'investissement judicieux dans des marchés en constante évolution.

<h2 id='plain'>Black-Scholes en anglais simple – avec un exemple de code</h2>

Essentiellement, l'équation de Black-Scholes a résolu le problème de [comment prix les options correctement sur les marchés financiers.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=500303)

Cela est très important, car cela aide les banques et les institutions financières à gérer efficacement les risques.

Cependant, ce n'était pas toujours le cas. Avant 1973, lorsque l'équation a été créée ([ses créateurs ont remporté un prix Nobel](https://www.nobelprize.org/prizes/economic-sciences/1997/press-release/)), la détermination du prix des options était beaucoup plus compliquée et difficile.

Avant la création de l'équation de Black-Scholes, il n'existait pas de méthode mathématique standardisée pour prédire les prix des options.

Les traders s'appuyaient souvent sur l'expérience personnelle et les conditions du marché, ce qui conduisait à des prix d'options peu fiables.

Et les méthodes mathématiques antérieures ne prenaient pas pleinement en compte des facteurs comme la volatilité, la décote temporelle et les taux d'intérêt. Il y avait donc beaucoup d'erreurs lors de la tarification des options.

### Voici l'équation de Black-Scholes :

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV - r S \frac{\partial V}{\partial S}$$

Bien que nous n'examinerons pas très profondément l'équation elle-même, nous en décriremos ses principaux composants et implications.

Essentiellement, l'équation de Black-Scholes prédit comment la valeur d'une option change au fil du temps en fonction de plusieurs variables :

* V - Prix de l'option en fonction du prix de l'action _S_ et du temps _t_
* S – Prix de l'actif sous-jacent
* t – Temps
* σ – Volatilité
* r – Taux d'intérêt.

Le côté gauche de l'équation explique comment la valeur de l'option change au fil du temps et comment les hauts et les bas du marché l'affectent.

Le côté droit de l'équation montre comment la valeur de l'option augmente en raison des taux d'intérêt et comment les changements dans le prix de l'actif l'impactent.

En rendant ces deux côtés égaux, nous déterminons le prix équitable de l'option.

### Exemple de code Python

Dans cet exemple de code, nous allons trouver, en fonction de nombreux paramètres, la valeur théorique du marché d'une option.

Pour notre exemple, supposons ce qui suit :

* Prix actuel de l'action (S) = 100 $. C'est le prix de l'action en ce moment.
* Prix d'exercice (K) = 105 $. C'est le prix spécifique auquel le détenteur de l'option peut acheter (call) ou vendre (put) l'actif sous-jacent.
* Temps jusqu'à l'expiration (T) = 1 an (ou 1,0 lorsqu'il est exprimé en années). C'est le temps restant jusqu'à l'expiration de l'option.
* Taux d'intérêt sans risque (r) = 0,05 % (ou 0,0005 lorsqu'il est exprimé en décimal). C'est le taux d'intérêt sur un investissement sans risque.
* Volatilité (sigma) = 20 % (ou 0,2 lorsqu'il est exprimé en décimal). C'est la fluctuation attendue du prix de l'action.

```
from blackscholes import BlackScholesCall, BlackScholesPut

def calculate_option_prices(S, K, T, r, sigma, q):
    """
    Calculer les prix des options Black-Scholes pour les options d'achat et de vente européennes en utilisant le package 'blackscholes'.

    Paramètres :
    S : float - prix actuel de l'action
    K : float - prix d'exercice de l'option
    T : float - temps jusqu'à l'échéance (en années)
    r : float - taux d'intérêt sans risque (annuel en décimal)
    sigma : float - volatilité de l'action sous-jacente (annuelle en décimal)
    q : float - rendement annuel des dividendes (en décimal)

    Retourne :
    tuple - (prix de l'option d'achat, prix de l'option de vente)
    """
    # Création d'instances de BlackScholesCall et BlackScholesPut
    call_option = BlackScholesCall(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    put_option = BlackScholesPut(S=S, K=K, T=T, r=r, sigma=sigma, q=q)

    # Obtenir les prix des options d'achat et de vente
    call_price = call_option.price()
    put_price = put_option.price()

    return call_price, put_price


call_price, put_price = calculate_option_prices(100, 105, 1, 0.0005, 0.20, 0.0)
print("Prix de l'option d'achat : {:.6f}, Prix de l'option de vente : {:.6f}".format(call_price, put_price))

```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/1.png)

Maintenant, examinons le code plus en détail et voyons ce qui se passe vraiment ici :

#### Étape 1 : Importer la bibliothèque

Voici la bibliothèque Python que nous utilisons dans cet article :

%[https://pypi.org/project/blackscholes/]

```
from blackscholes import BlackScholesCall, BlackScholesPut

```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/2.png)
_Importation des fonctions_

#### Étape 2 : Créer la fonction pour calculer les prix des options

Dans le code ci-dessous, nous importons la fonction dont nous avons besoin pour calculer les prix des options d'achat et de vente.

```
def calculate_option_prices(S, K, T, r, sigma, q):

    call_option = BlackScholesCall(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    put_option = BlackScholesPut(S=S, K=K, T=T, r=r, sigma=sigma, q=q)

    call_price = call_option.price()
    put_price = put_option.price()

    return call_price, put_price
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/3.png)
_Fonction pour calculer les prix des options d'achat et de vente_

Les principaux paramètres de la fonction sont :

* S : float – prix actuel de l'action
* K : float – prix d'exercice de l'option
* T : float – temps jusqu'à l'échéance (en années)
* r : float – taux d'intérêt sans risque (annuel en décimal)
* sigma : float – volatilité de l'action sous-jacente (annuelle en décimal)
* q : float – rendement annuel des dividendes (en décimal)

Et elle retourne :

* tuple – (prix de l'option d'achat, prix de l'option de vente)

Tout d'abord, nous calculons les options d'achat et de vente. Ensuite, nous en extrayons le prix. Nous pouvons également obtenir d'autres caractéristiques comme le charme ou le delta de ces contrats financiers selon la documentation de la bibliothèque.

#### Étape 3 : Calculer les prix des options

Les prix des options d'achat et de vente sont les coûts pour acheter les contrats d'options respectifs.

```
call_price, put_price = calculate_option_prices(100, 105, 1, 0.0005, 0.20, 0.0)
print("Prix de l'option d'achat : {:.6f}, Prix de l'option de vente : {:.6f}".format(call_price, put_price))
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/4.png)
_Application de la fonction_

Nous utilisons comme exemples :

* Prix actuel de l'action : 100 $
* Prix d'exercice : 105 $
* Temps jusqu'à l'échéance : 1 an
* Taux d'intérêt sans risque : 0,05 % (en décimal : 0,0005)
* Volatilité : 20 % (en décimal : 0,20)
* Rendement des dividendes : 0 %

Sur la base de ces facteurs, nous tarifons :

* Prix de l'option d'achat : 5,924799
* Prix de l'option de vente : 10,872312

Ce qui signifie que, étant donné ces paramètres :

* Le prix auquel vous avez le droit, mais non l'obligation, d'acheter est de 5,924799 dollars
* Le prix auquel vous avez le droit, mais non l'obligation, de vendre est de 10,872312 dollars

<h2 id='implications'>Implications dans le monde réel</h2>

L'équation a eu un impact massif dans le monde de la finance.

Voici quelques-unes des industries que l'équation de Black-Scholes a grandement changées :

### Dette titrisée

En termes simples, la dette titrisée fait référence à la transformation de prêts en quelque chose qui peut être acheté et vendu.

L'équation de Black-Scholes a changé la manière dont les banques tarifient les dettes regroupées, comme les hypothèques.

Avant l'équation de Black-Scholes, il était très difficile de connaître la valeur de ces dettes. Mais avec l'équation, les banques peuvent comprendre leur valeur beaucoup mieux. Cela a facilité l'achat et la vente de ces dettes tout en connaissant les avantages et les risques potentiels.

De cette façon, le marché de ces dettes hypothécaires a grandi. Ce qui, à son tour, a aidé à faire croître le marché du logement.

### Options négociées en bourse

Le trading d'options était une activité très incertaine. Il n'y avait aucun moyen de vraiment savoir comment les tarifer correctement.

Cependant, avec l'équation de Black-Scholes, la tarification des options est devenue beaucoup plus facile. Elle a permis aux gens de calculer une option en fonction du prix de l'actif sous-jacent, de la volatilité, du temps jusqu'à l'expiration et des taux d'intérêt.

La nouvelle précision a aidé à faire croître le marché des options.

### Swaps de défaut de crédit

Les swaps de défaut de crédit sont comme des polices d'assurance pour les prêts. Avec un swap de défaut de crédit, vous êtes protégé si l'emprunteur ne rembourse pas.

Les swaps de défaut de crédit sont très importants dans la gestion du risque de crédit. Mais ce n'est qu'après la création de l'équation de Black-Scholes qu'ils ont été tarifés avec précision.

De cette façon, les swaps de défaut de crédit sont devenus un outil très important pour les institutions financières pour la gestion des risques financiers.

### Titres dérivés de gré à gré

Les dérivés de gré à gré (OTC) sont des accords privés conclus entre deux parties sans une bourse.

Avant Black-Scholes, la négociation des termes et des prix des dérivés OTC était très difficile. Mais ensuite, l'équation de Black-Scholes a offert une méthode standard de trouver le prix des dérivés.

Cela a permis aux participants du marché de négocier des contrats plus efficacement et avec plus de précision.

## Conclusion

L'équation de Black-Scholes a aidé à créer plus de précision dans la manière dont certaines choses sont tarifées.

Cette précision a aidé à créer des institutions plus stables, ce qui, à son tour, a aidé à créer une économie plus résiliente.

Si vous êtes intéressé à en apprendre davantage, regardez cette vidéo :

%[https://www.youtube.com/watch?v=A5w-dEgIU1M]

Si vous êtes intéressé à en apprendre davantage sur la finance :

%[https://www.freecodecamp.org/news/fundamentals-of-finance-economics-for-businesses/]

## Code complet

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]