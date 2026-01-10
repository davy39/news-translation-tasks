---
title: La règle de Bayes – Expliquée pour les débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-29T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/bayes-rule-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-21-at-23.44.38-1.png
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Data Science
  slug: data-science
- name: Math
  slug: math
seo_title: La règle de Bayes – Expliquée pour les débutants
seo_desc: 'By Peter Gleeson

  Bayes'' Rule is the most important rule in data science. It is the mathematical
  rule that describes how to update a belief, given some evidence. In other words
  – it describes the act of learning.

  The equation itself is not too complex...'
---

Par Peter Gleeson

La règle de Bayes est la règle la plus importante en science des données. C'est la règle mathématique qui décrit comment mettre à jour une croyance, étant donné certaines preuves. En d'autres termes, elle décrit l'acte d'apprentissage.

L'équation elle-même n'est pas trop complexe :

![Probabilité de l'événement A étant donné l'événement B égale Probabilité a priori de l'événement A multipliée par la probabilité de l'événement B étant donné A, divisée par la probabilité marginale de l'événement B](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-19-at-22.58.48.png)
_L'équation : Postérieure = A priori x (Vraisemblance sur Probabilité marginale)_

Il y a quatre parties :

* **Probabilité postérieure** (probabilité mise à jour après que la preuve est considérée)
* **Probabilité a priori** (la probabilité avant que la preuve ne soit considérée)
* **Vraisemblance** (probabilité de la preuve, étant donné que la croyance est vraie)
* **Probabilité marginale** (probabilité de la preuve, dans n'importe quelle circonstance)

La règle de Bayes peut répondre à une variété de questions de probabilité, ce qui nous aide (ainsi que les machines) à comprendre le monde complexe dans lequel nous vivons.

Elle porte le nom de Thomas Bayes, un théologien et mathématicien anglais du 18ème siècle. Bayes a initialement écrit sur le concept, mais cela n'a pas reçu beaucoup d'attention de son vivant.

Le mathématicien français [Pierre-Simon Laplace](https://www.freecodecamp.org/news/will-the-sun-rise-tomorrow-255afc810682/) a publié indépendamment la règle dans son œuvre de 1814 [_Essai philosophique sur les probabilités_](https://ia801407.us.archive.org/35/items/essaiphilosophiq00lapluoft/essaiphilosophiq00lapluoft_bw.pdf).

Aujourd'hui, la règle de Bayes a de nombreuses applications, de l'analyse statistique à l'apprentissage automatique.

Cet article expliquera la règle de Bayes en langage simple.

## Probabilité conditionnelle

Le premier concept à comprendre est la [probabilité conditionnelle](https://www.mathsisfun.com/data/probability-events-conditional.html).

Vous êtes peut-être déjà familier avec la [probabilité](https://en.wikipedia.org/wiki/Probability) en général. Elle vous permet de raisonner sur des événements incertains avec la précision et la rigueur des mathématiques.

La probabilité conditionnelle est le pont qui vous permet de parler de la manière dont plusieurs événements incertains sont liés. Elle vous permet de parler de la manière dont la probabilité d'un événement peut varier sous différentes conditions.

Par exemple, considérons la probabilité de gagner une course, étant donné que vous n'avez pas dormi la nuit précédente. Vous pourriez vous attendre à ce que cette probabilité soit plus faible que la probabilité de gagner si vous aviez eu une nuit complète de sommeil.

![La probabilité de gagner la course, étant donné une nuit complète de sommeil est de 30 %. La probabilité de gagner la course, sans sommeil est seulement de 5 %.](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-22-at-22.51.41.png)

Ou, considérons la probabilité qu'un suspect ait commis un crime, étant donné que ses empreintes digitales sont trouvées sur la scène. Vous vous attendriez à ce que la probabilité qu'il soit coupable soit plus grande, comparée à si ses empreintes digitales n'avaient pas été trouvées.

La notation pour la probabilité conditionnelle est généralement :

![P parenthèse ouverte A barre verticale B parenthèse fermée](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-19-at-23.42.22.png)
_P(A|B)_

Ce qui se lit comme "la probabilité que l'événement A se produise, étant donné que l'événement B se produit".

Une chose importante à retenir est que les probabilités conditionnelles ne sont [pas les mêmes que leurs inverses](https://en.wikipedia.org/wiki/Confusion_of_the_inverse#:~:text=Confusion%20of%20the%20inverse%2C%20also,about%20the%20same%20as%20the\).

C'est-à-dire, la "probabilité de l'événement A étant donné l'événement B" n'est pas la même chose que la "probabilité de l'événement B, étant donné l'événement A".

Pour vous en souvenir, prenez l'exemple suivant :

> La probabilité de nuages, étant donné qu'il pleut (100 %) n'est **pas** la même que la probabilité qu'il pleuve, étant donné qu'il y a des nuages.

(Insérer une blague sur le temps britannique).

## La règle de Bayes en détail

La règle de Bayes vous indique comment calculer une probabilité conditionnelle avec les informations que vous avez déjà.

Il est utile de penser en termes de deux événements – une hypothèse (qui peut être vraie ou fausse) et une preuve (qui peut être présente ou absente).

Cependant, elle peut être appliquée à tout type d'événements, avec n'importe quel nombre de résultats [discrets ou continus](https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/discrete-vs-continuous-variables/).

![Probabilité que l'hypothèse soit vraie, étant donné que la preuve est présente égale à la probabilité a priori que l'hypothèse soit vraie multipliée par la vraisemblance que la preuve soit présente étant donné que l'hypothèse est vraie, divisée par la probabilité marginale que la preuve soit présente dans n'importe quelle circonstance](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-22-at-23.44.18.png)

La règle de Bayes vous permet de calculer la **probabilité postérieure (ou "mise à jour")**. Il s'agit d'une probabilité conditionnelle. C'est la probabilité que l'hypothèse soit vraie, si la preuve est présente.

Considérez la **probabilité a priori (ou "précédente")** comme votre croyance dans l'hypothèse avant de voir la nouvelle preuve. Si vous aviez déjà une forte croyance dans l'hypothèse, la probabilité a priori sera grande.

L'a priori est multiplié par une fraction. Considérez cela comme la "force" de la preuve. La probabilité postérieure est plus grande lorsque la partie supérieure (numérateur) est grande et la partie inférieure (dénominateur) est petite.

Le numérateur est la **vraisemblance**. Il s'agit d'une autre probabilité conditionnelle. C'est la probabilité que la preuve soit présente, étant donné que l'hypothèse est vraie.

Ce n'est pas la même chose que la postérieure !

Rappelez-vous, la "probabilité que la preuve soit présente étant donné que l'hypothèse est vraie" n'est pas la même que la "probabilité que l'hypothèse soit vraie étant donné que la preuve est présente".

Maintenant, regardez le dénominateur. Il s'agit de la **probabilité marginale** de la preuve. C'est-à-dire, c'est la probabilité que la preuve soit présente, que l'hypothèse soit vraie ou fausse. Plus le dénominateur est petit, plus la preuve est "convaincante".

## Exemple détaillé de la règle de Bayes

Voici un exemple simple.

Votre voisin regarde son équipe de football (ou de soccer) favorite. Vous l'entendez crier et voulez estimer la probabilité que son équipe ait marqué.

**Étape 1** – écrire la probabilité postérieure d'un but, étant donné les cris

**Étape 2** – estimer la probabilité a priori d'un but à 2%

**Étape 3** – estimer la probabilité de vraisemblance des cris, étant donné qu'il y a un but à 90 % (peut-être que votre voisin ne célébrera pas si son équipe perd fortement)

**Étape 4** – estimer la probabilité marginale des cris – cela pourrait être dû à :

* un but a été marqué (2 % du temps, fois 90 % de probabilité)
* ou toute autre raison, comme l'autre équipe manquant un penalty ou ayant un joueur expulsé (98 % du temps, fois peut-être 1 % de probabilité)

Maintenant, assemblez tout :

![Probabilité de but, étant donné les cris égale à la probabilité a priori de but fois la probabilité de cris étant donné un but, divisée par la probabilité de cris étant donné un but plus la probabilité de cris étant donné aucun but. Égale à 0,02 fois 0,9 sur 0,02 fois 0,9 plus 0,98 fois 0,01 = 64,7 pour cent](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-23-at-22.05.25.png)

## Cas d'utilisation de la règle de Bayes et prochaines étapes

La règle de Bayes a des cas d'utilisation dans de nombreux domaines :

* Comprendre les problèmes de probabilité (y compris ceux de la recherche médicale)
* Modélisation statistique et inférence
* Algorithmes d'apprentissage automatique (comme Naive Bayes, Expectation Maximisation)
* Modélisation quantitative et prévision

Ensuite, vous découvrirez comment la règle de Bayes peut être utilisée pour quantifier l'incertitude et modéliser des problèmes réels. Ensuite, comment raisonner sur les "probabilités de probabilités".

La dernière étape couvrira comment divers trucs computationnels vous permettent d'utiliser la règle de Bayes pour résoudre des problèmes non triviaux.