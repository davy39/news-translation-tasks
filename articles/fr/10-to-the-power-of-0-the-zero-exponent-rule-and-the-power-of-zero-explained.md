---
title: '10 à la puissance 0 : la règle de l''exposant zéro et la puissance de zéro
  expliquées'
date: '2021-01-26T16:34:45.000Z'
author: Eric Leung
authorURL: https://www.freecodecamp.org/news/author/erictleung/
originalURL: https://freecodecamp.org/news/10-to-the-power-of-0-the-zero-exponent-rule-and-the-power-of-zero-explained
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/pexels-katerina-holmes-5905857.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: MathJax
  slug: mathjax
seo_desc: 'Exponents are important in the financial world, in scientific notation,
  and in the fields of epidemiology and public health. So what are they, and how do
  they work?

  Exponents are written like (3^2) or (10^3).

  But what happens when you raise a number ...'
---


Les exposants sont importants dans le monde de la finance, en notation scientifique, ainsi que dans les domaines de l'épidémiologie et de la santé publique. Alors, que sont-ils et comment fonctionnent-ils ?

<!-- more -->

Les exposants s'écrivent sous la forme (3^2) ou (10^3).

Mais que se passe-t-il lorsque vous élevez un nombre à la puissance (0) comme ceci ?

$$10^0 = \\text{?}$$

Cet article abordera :

-   les bases des exposants,
    
-   leur signification, et
    
-   il démontrera que (10^0) est égal à (1) en utilisant les exposants négatifs.
    

Je suppose simplement que vous avez une compréhension de base de la multiplication et de la division.

## Les exposants sont composés d'une base et d'un exposant (ou puissance)

Commençons d'abord par les parties d'un exposant.

Un exposant comporte deux parties :

1.  la base
    
2.  l'exposant ou la puissance
    

Au début, nous avions l'exposant (3^2). Le « 3 » ici est la **base**, tandis que le « 2 » est **l'exposant ou la puissance**.

Nous lisons cela comme :

> Trois est élevé à la puissance deux.

ou

> Trois puissance deux.

Plus généralement, les exposants s'écrivent (a^b), où (a) et (b) peuvent être n'importe quelle paire de nombres.

## Les exposants sont des multiplications pour les « paresseux »

Maintenant que nous comprenons comment parler des exposants, comment trouver le nombre auquel cela correspond ?

En utilisant notre exemple ci-dessus, nous pouvons écrire et développer « trois puissance deux » ainsi :

$$3^2 = 3 \\times 3 = 9$$

Le nombre le plus à gauche dans l'exposant est le nombre que nous multiplions de manière répétée. C'est pourquoi vous voyez plusieurs 3. Le nombre le plus à droite dans l'exposant est le nombre de multiplications que nous effectuons. Ainsi, pour notre exemple, le nombre 3 (la base) est multiplié deux fois (l'exposant).

Voici d'autres exemples d'exposants :

$$10^3 = 10 \\times 10 \\times 10 = 1000$$

$$2^{10} = 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 = 1024$$

Plus généralement, nous pouvons écrire ces exposants comme suit :

$$\\textcolor{orange}{b}^\\textcolor{blue}{n} = \\underbrace{\\textcolor{orange}{b} \\times \\dots \\times \\textcolor{orange}{b}}\_{\\textcolor{blue}{n} \\textrm{ fois}}$$

où la (\\textcolor{orange}{\\text{lettre « b » est la base}}\) que nous multiplions de manière répétée et la \(\textcolor{blue}{\text{lettre « n » est la puissance}}) ou (\\textcolor{blue}{\\text{exposant}}), qui est le nombre de fois que nous multiplions la base par elle-même.

Pour ces exemples ci-dessus, les valeurs des exposants sont relativement petites. Mais vous pouvez imaginer que si les puissances sont très grandes, il devient redondant d'écrire les nombres encore et encore en utilisant des signes de multiplication.

**En résumé, les exposants permettent d'écrire ces longues multiplications de manière plus efficace.**

## Les nombres à la puissance zéro sont égaux à un

Les exemples précédents montrent des puissances supérieures à un, mais que se passe-t-il lorsqu'elle est égale à zéro ?

La réponse rapide est que n'importe quel nombre, (b), à la puissance zéro est égal à un.

$$b^0 = 1$$

Sur la base de nos définitions précédentes, nous avons simplement besoin de zéro fois la valeur de base. Ici, prenons 10 comme nombre de base.

$$10^0 = ? = 1$$

Mais que signifie un nombre « zéro » de nombres de base ? Pourquoi cela arrive-t-il ?

**Nous pouvons le comprendre en divisant plusieurs fois pour diminuer la valeur de la puissance jusqu'à atteindre zéro.**

Commençons par :

$$10^3 = 10 \\times 10 \\times 10 = 1000$$

Pour diminuer les puissances, nous devons brièvement comprendre les concepts de :

-   combinaison d'exposants
    
-   puissances de un
    

Dans notre quête pour réduire l'exposant de (10^3) (« dix à la puissance trois ») à (10^0) (« dix à la puissance zéro »), nous allons continuer à faire l'inverse de la multiplication, c'est-à-dire la division.

$$\\frac{10^3}{10} = \\frac{10 \\times 10 \\times 10}{10} = \\frac{1000}{10} = 100$$

Les parties les plus à droite de cette équation sont probablement logiques. Mais comment écrire les exposants lorsque nous avons (10^3) divisé par (10) ?

### Comment fonctionnent les puissances de un

Premièrement, tous les (\\textcolor{orange}{\\text{exposants avec une puissance de un}}) sont égaux au (\\textcolor{blue}{\\text{nombre de base}}) lui-même.

$$\\textcolor{orange}{b^1} = \\textcolor{blue}{b}$$

Il n'y a qu'une seule valeur « multipliée », nous obtenons donc la valeur elle-même.

Nous avons besoin de cette définition de la « puissance de un » pour pouvoir réécrire la fraction avec des exposants.

$$\\frac{10^3}{10} = \\frac{10^3}{10^1}$$

### Comment réduire les exposants à zéro

Pour rappel, une façon de comprendre pourquoi (10^0) est égal à 1 est de continuer à diviser par 10 jusqu'à obtenir un exposant de zéro.

Nous savons, d'après le côté droit de l'équation ci-dessus, que nous devrions obtenir 100 à partir de (\\frac{10^3}{10^1}).

$$\\frac{10^3}{10} = \\frac{10^3}{10^1} = \\frac{10 \\times 10 \\times 10}{10^1}$$

Avant de finir de diviser par un 10, nous pouvons multiplier le haut et le bas par 1 comme valeurs de substitution lorsque nous simplifions les nombres.

$$\\frac{10 \\times 10 \\times 10}{10^1} = \\frac{10 \\times 10 \\times 10 \\times 1}{10^1 \\times 1} = \\frac{10 \\times 10 \\times \\cancel{10} \\times 1}{\\cancel{10^1} \\times 1} = \\frac{10 \\times 10 \\times 1}{1}$$

À partir de là, nous voyons que nous obtenons à nouveau 100.

$$\\frac{10 \\times 10 \\times 1}{1} = \\frac{10 \\times 10}{1} = \\frac{10^2}{1} = \\frac{100}{1}$$

Nous pouvons diviser par 10 encore deux fois pour arriver enfin à (10^0).

$$\\frac{10^2 \\times 1}{10 \\times 10 \\times 1} = \\frac{\\cancel{10} \\times \\cancel{10} \\times 1}{\\cancel{10} \\times \\cancel{10} \\times 1} = \\frac{10^0 \\times 1}{1} = \\frac{1}{1} = 1$$

Parce que nous avons divisé par deux 10 alors que nous n'avions que deux 10 au numérateur de la fraction, nous avons zéro dix en haut. Avoir zéro dix signifie concrètement que nous obtenons (10^0).

### Comment fonctionnent les exposants négatifs

Maintenant, le (10^0) semble sortir de nulle part, alors explorons cela davantage en utilisant les « exposants négatifs ».

Plus généralement, cette division répétitive par la même base revient à multiplier par des « exposants négatifs ».

Un exposant négatif est une façon de réécrire une division.

$$\\frac{1}{\\textcolor{purple}{b^n}}= \\textcolor{green}{b^{-n}}$$

Un (\\textcolor{green}{\\text{exposant négatif}}) peut être réécrit sous forme de fraction avec le dénominateur (le bas de la fraction) ayant le (\\textcolor{purple}{\\text{même exposant mais avec une puissance positive}}) (le côté gauche de cette équation).

Désormais, en utilisant les exposants négatifs, nous pouvons montrer la division précédente d'une autre manière.

$$\\frac{10^2 \\times 1}{10 \\times 10 \\times 1} = \\frac{10^2}{10^2} = 10^2 \\times \\frac{1}{10^2} = 10^2 \\times 10^{-2}$$

**Note** : une règle des exposants est que lorsque vous multipliez des exposants avec le même nombre de base (rappelez-vous, notre nombre de base ici est 10), vous pouvez additionner les exposants.

$$10^2 \\times 10^{-2} = 10^{2 + (-2)} = 10^{2 - 2} = 10^{0}$$

### Synthèse

Sachant cela, nous pouvons combiner chacune de ces équations ci-dessus pour résumer notre résultat.

$$\\textcolor{purple}{\\frac{10^2}{10^2}} = 10^2 \\times 10^{-2} = 10^{2 + (-2)} = 10^{2 - 2} = \\textcolor{blue}{10^{0}} \\textcolor{orange}{= 1}$$

Nous savons que (\\textcolor{purple}{\\text{diviser un nombre par lui-même}}) sera (\\textcolor{orange}{\\text{égal à un}}). Et nous avons montré que (\\textcolor{purple}{\\text{diviser un nombre par lui-même}}) est également égal à (\\textcolor{blue}{\\text{dix à la puissance zéro}}). Les mathématiques disent que les choses qui sont égales à une même chose sont également égales entre elles.

Ainsi, (\\textcolor{blue}{\\text{dix à la puissance zéro}}) est (\\textcolor{orange}{\\text{égal à un}}). Cet exercice ci-dessus se généralise à n'importe quel nombre de base, **donc n'importe quel nombre à la puissance zéro est égal à un.**

## En résumé

Les exposants sont des moyens pratiques d'effectuer des multiplications répétitives.

Généralement, les exposants suivent le modèle ci-dessous, avec un (\\textcolor{orange}{\\text{nombre de base}}) multiplié encore et encore (\\textcolor{blue}{\\text{« n » fois}}).

$$\\textcolor{orange}{b}^\\textcolor{blue}{n} = \\underbrace{\\textcolor{orange}{b} \\times \\dots \\times \\textcolor{orange}{b}}\_{\\textcolor{blue}{n} \\textrm{ fois}}$$

En utilisant des exposants négatifs, nous pouvons utiliser ce que nous savons de la multiplication et de la division (comme pour la fraction 10 sur 10, (\\frac{10}{10})) pour montrer que (b^0) est égal à un pour n'importe quel nombre (b) (comme (10^0 = 1)).

Suivez-moi sur [Twitter][1] et consultez mon [blog personnel][2] où je partage d'autres réflexions et ressources utiles pour la programmation, les statistiques et le machine learning.

Merci de m'avoir lu !

[1]: https://twitter.com/erictleung
[2]: https://erictleung.com