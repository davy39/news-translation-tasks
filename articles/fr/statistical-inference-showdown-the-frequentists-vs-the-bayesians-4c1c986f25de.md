---
title: 'Affrontement de l''inférence statistique : Les Fréquentistes contre les Bayésiens'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T19:40:55.000Z'
originalURL: https://freecodecamp.org/news/statistical-inference-showdown-the-frequentists-vs-the-bayesians-4c1c986f25de
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ldKLrcBj56-wh0zbEBzgLw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Life lessons
  slug: life-lessons
- name: Mathematics
  slug: mathematics
- name: technology
  slug: technology
seo_title: 'Affrontement de l''inférence statistique : Les Fréquentistes contre les
  Bayésiens'
seo_desc: 'By Kirill Dubovikov

  Inference

  Statistical Inference is a very important topic that powers modern Machine Learning
  and Deep Learning algorithms. This article will help you to familiarize yourself
  with the concepts and mathematics that make up inferenc...'
---

Par Kirill Dubovikov

### Inférence

L'inférence statistique est un sujet très important qui alimente les algorithmes modernes d'apprentissage automatique et d'apprentissage profond. Cet article vous aidera à vous familiariser avec les concepts et les mathématiques qui constituent l'inférence.

Imaginez que nous voulons tromper quelques amis avec une pièce de monnaie truquée. Nous avons 10 pièces et voulons juger si l'une d'entre elles est truquée — ce qui signifie qu'elle tombera plus souvent sur pile que sur face, ou vice versa.

Nous prenons donc chaque pièce, la lançons plusieurs fois — disons 100 — et enregistrons les résultats. Le problème est que nous avons maintenant un sous-ensemble de mesures provenant d'une vraie distribution (un échantillon) pour chaque pièce. Nous avons considéré l'état de nos pouces et conclu que collecter plus de données serait très fastidieux.

Il est rare de connaître les paramètres de la vraie distribution. Fréquemment, nous voulons inférer les vrais paramètres de la population à partir de l'échantillon.

Nous voulons donc maintenant estimer la probabilité qu'une pièce tombe sur pile. Nous nous intéressons à la **moyenne de l'échantillon**.

À ce stade, vous avez probablement pensé : « Comptez simplement le nombre de piles et divisez par le nombre total de lancers ! » Oui, c'est la façon de trouver une pièce truquée, mais comment pourrions-nous élaborer cette formule si nous ne la connaissions pas au départ ?

### Inférence Fréquentiste

Rappelons que les lancers de pièces sont mieux modélisés par une distribution de Bernoulli, nous sommes donc sûrs qu'elle représente bien nos données. La fonction de masse de probabilité (PMF) pour la distribution de Bernoulli ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*813KZNbPdfe9XG3udKPN1A@2x.png)

_x_ est une variable aléatoire qui représente une observation d'un lancer de pièce (supposons 1 pour pile et 0 pour face) et _p_ est un paramètre — la probabilité de pile. Nous désignerons tous les paramètres possibles par _θ_ par la suite. Cette fonction représente la probabilité de chaque valeur de _x_ selon la loi de distribution que nous avons choisie.

Lorsque _x_ est égal à 1, nous obtenons _f(1; p) = p_, et lorsqu'il est zéro, _f(0; p) = 1-p_. Ainsi, la distribution de Bernoulli répond à la question « Quelle est la probabilité d'obtenir pile avec une pièce qui tombe sur pile avec une probabilité _p_ ? ». En fait, c'est l'un des exemples les plus simples d'une [distribution de probabilité discrète](https://www.khanacademy.org/math/ap-statistics/random-variables-ap/discrete-random-variables/v/discrete-probability-distribution).

Nous sommes donc intéressés à déterminer le paramètre _p_ à partir des données. Un statisticien fréquentiste suggérera probablement d'utiliser une procédure d'estimation par maximum de vraisemblance (MLE). Cette méthode adopte l'approche de maximisation de la vraisemblance des paramètres étant donné l'ensemble de données _D_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nEqieIwL1sDmYjKqsFUS6A@2x.png)

Cela signifie que la **vraisemblance** est définie comme une probabilité des données étant donné les paramètres du modèle. Pour maximiser cette probabilité, nous devrons trouver des paramètres qui aident notre modèle à correspondre aux données aussi étroitement que possible. Cela ne ressemble-t-il pas à de l'**apprentissage** ? Le maximum de vraisemblance est l'une des méthodes qui font fonctionner l'apprentissage supervisé.

Supposons maintenant que toutes les observations que nous faisons sont indépendantes. Cela signifie que la probabilité conjointe dans l'expression ci-dessus peut être simplifiée en un produit par [les règles de base de la probabilité](http://ais.informatik.uni-freiburg.de/teaching/ss10/robotics/etc/probability-rules.pdf) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aXUE5iM7Oz58Urc8S0Hqfw@2x.png)

Voici la partie principale : comment maximiser une fonction de vraisemblance ? Nous faisons appel au calcul différentiel, différencions la fonction de vraisemblance par rapport aux paramètres du modèle _θ_, la mettons à 0 et résolvons l'équation. Il existe un astuce qui facilite la différentiation la plupart du temps — les logarithmes ne changent pas les extrema (minimum et maximum) de la fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wFoINBwvJyTCMAZ9sZuSQw@2x.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*6xkNcW1ltUfaBHg00D-TNQ@2x.png)

L'estimation par maximum de vraisemblance a une immense importance et presque tous les algorithmes d'apprentissage automatique l'utilisent. C'est l'une des méthodes les plus populaires pour formuler un processus d'apprentissage mathématiquement.

Et maintenant, appliquons ce que nous avons appris et jouons avec nos pièces. Nous avons effectué _n_ essais de Bernoulli indépendants pour évaluer l'équité de notre pièce. Ainsi, toutes les probabilités peuvent être multipliées et la fonction de vraisemblance ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jqqF7zzB2jtQB_nV-QASKA@2x.png)

Prendre la dérivée de l'expression ci-dessus ne sera pas agréable. Nous devons donc trouver la log-vraisemblance :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5Pcer6gm99HzNm4aDTalYg@2x.png)

Cela semble plus facile. Passons à la différentiation

![Image](https://cdn-media-1.freecodecamp.org/images/1*FKGmv94wVppsPochgwgXtQ@2x.png)

Ici, nous divisons les dérivées en utilisant la règle standard _d(f + g) = df + dg_. Ensuite, nous sortons les constantes et différencions les logarithmes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5c_gleOBnbON9aEOifPCxA@2x.png)

La dernière étape peut sembler amusante à cause du changement de signe. La cause est que _log(1-p)_ est en fait une composition de deux fonctions et nous devons utiliser la règle de la chaîne ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GdAgind4qDeCIz90VITXHw@2x.png)
_En passant, essayez de vous familiariser avec la règle de la chaîne. C'est un outil très utile. Et il a une grande importance dans les réseaux de neurones._

Voilà, nous avons terminé avec la log-vraisemblance ! Nous sommes maintenant proches de trouver la statistique de maximum de vraisemblance pour la moyenne de la distribution de Bernoulli. La dernière étape est de résoudre l'équation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4saiV4bcBBL4I4OvJPMBpg@2x.png)

En multipliant tout par _p(1-p)_ et en développant les parenthèses, nous obtenons

![Image](https://cdn-media-1.freecodecamp.org/images/1*ks1Z0tD4199AumbVWqmsYg@2x.png)

En annulant les termes et en réarrangeant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QiYT1ZG4SPWtqFBvbm_zGA@2x.png)

Ainsi, voici la dérivation de notre formule intuitive ?. Vous pouvez maintenant jouer avec la distribution de Bernoulli et son estimation MLE de la moyenne dans la visualisation ci-dessous

> Félicitations pour votre nouvelle compétence impressionnante d'estimation par maximum de vraisemblance ! Ou simplement pour avoir rafraîchi vos connaissances existantes.

### Inférence Bayésienne

![Image](https://cdn-media-1.freecodecamp.org/images/1*_i4uVp43apgOMpHRw6WG-w.jpeg)

Rappelons qu'il existe une autre approche de la probabilité. La statistique bayésienne a sa propre façon de faire l'inférence probabiliste. Nous voulons trouver la distribution de probabilité des paramètres THETA étant donné un échantillon — _P(THETA | D)_. Mais comment pouvons-nous inférer cette probabilité ? Le théorème de Bayes vient à la rescousse :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zI33Ra8qZLy_6IVC8y8JDw@2x.png)

* _P(θ)_ est appelée distribution a priori et incorpore nos croyances sur les paramètres possibles avant d'avoir vu aucune donnée. La capacité à énoncer des croyances a priori est l'une des principales différences entre l'estimation par maximum de vraisemblance et l'inférence bayésienne. Cependant, c'est aussi le principal point de critique pour l'approche bayésienne. Comment pouvons-nous énoncer la distribution a priori si nous ne savons rien sur le problème qui nous intéresse ? Et si nous choisissons une mauvaise distribution a priori ?
* _P(D | θ)_ est une vraisemblance, nous l'avons rencontrée dans l'estimation par maximum de vraisemblance
* _P(D)_ est appelée évidence ou vraisemblance marginale

_P(D)_ est également appelée **constante de normalisation** car elle garantit que les résultats que nous obtenons sont une distribution de probabilité valide. Si nous réécrivons _P(D)_ comme

![Image](https://cdn-media-1.freecodecamp.org/images/1*mEf7zSyRZ2NmsbnwgUmBMg@2x.png)

Nous verrons qu'elle est similaire au numérateur dans le théorème de Bayes, mais la sommation porte sur tous les paramètres possibles _θ_. De cette façon, nous obtenons deux choses :

* La sortie est toujours une distribution de probabilité valide dans le domaine de [0, 1].
* Des difficultés majeures lorsque nous essayons de calculer _P(D)_ car cela nécessite d'intégrer ou de sommer sur tous les paramètres possibles. Cela est impossible dans la plupart des problèmes du monde réel.

Mais est-ce que la vraisemblance marginale _P(D)_ rend toutes les choses bayésiennes impraticables ? La réponse n'est pas tout à fait. La plupart du temps, nous utiliserons l'une des deux options pour nous débarrasser de ce problème.

La première consiste à approximer _P(D)_ d'une manière ou d'une autre. Cela peut être réalisé en utilisant diverses méthodes d'échantillonnage comme l'échantillonnage par importance ou l'échantillonnage de Gibbs, ou une technique appelée inférence variationnelle (qui est un nom cool, soit dit en passant ?).

La seconde consiste à l'éliminer complètement de l'équation. Explorons cette approche plus en détail. Et si nous nous concentrions sur la recherche d'une combinaison de paramètres la plus probable (c'est-à-dire la meilleure possible) ? Cette procédure est appelée estimation a posteriori maximale (MAP).

![Image](https://cdn-media-1.freecodecamp.org/images/1*J02gkJjkZ4sswuzUmfo4Gw@2x.png)

L'équation ci-dessus signifie que nous voulons trouver _θ_ pour lequel l'expression à l'intérieur de **arg max** prend sa valeur maximale — l'_arg_ument d'un **max**imum. La principale chose à remarquer ici est que _P(D)_ est indépendante des paramètres et peut être exclue de **arg max** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vd3XqDoE6-YNloVCdif5Qw@2x.png)

En d'autres termes, _P(D)_ sera toujours constante par rapport aux paramètres du modèle et sa dérivée sera égale à _1_.

Ce fait est si largement utilisé qu'il est courant de voir le théorème de Bayes écrit sous cette forme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*G_fcxKqJ2ptsrX8G-yLmjw@2x.png)

Le signe d'infini incomplet dans l'expression ci-dessus signifie « proportionnel à » ou « égal à une constante près ».

Ainsi, nous avons supprimé la partie la plus lourde en calcul de la MAP. Cela a du sens puisque nous avons essentiellement écarté toutes les valeurs de paramètres possibles de la distribution de probabilité et simplement extrait la meilleure et la plus probable.

### Un lien entre MLE et MAP

Et maintenant, considérons ce qui se passe lorsque nous supposons que la distribution a priori est uniforme (une probabilité constante).

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ZpopxplQiSUyc-ryOAfbQ@2x.png)

Nous avons sorti la constante _C_ de l'**arg max** puisque elle n'affecte pas le résultat comme c'était le cas avec l'évidence. Cela ressemble certainement à une estimation par maximum de vraisemblance ! En fin de compte, l'écart mathématique entre l'inférence fréquentiste et bayésienne n'est pas si grand.

Nous pouvons également construire le pont de l'autre côté et voir l'estimation par maximum de vraisemblance à travers les lunettes bayésiennes. En particulier, il peut être démontré que les distributions a priori bayésiennes ont des liens étroits avec les termes de régularisation. Mais ce sujet mérite un autre article (voir cette [question SO](https://stats.stackexchange.com/questions/163388/l2-regularization-is-equivalent-to-gaussian-prior) et le [livre ESLR](https://web.stanford.edu/~hastie/Papers/ESLII.pdf) pour plus de détails).

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/1*PD1lBchCtkx_aE3WJezudw.png)
_Bande dessinée XKCD sur les Fréquentistes contre les Bayésiens_

Ces différences peuvent sembler subtiles au premier abord, mais elles donnent naissance à deux écoles de statistiques. Les approches fréquentiste et bayésienne diffèrent non seulement par le traitement mathématique, mais aussi par les vues philosophiques sur les concepts fondamentaux en statistiques.

Si vous adoptez un chapeau bayésien, vous voyez les inconnues comme des distributions de probabilité et les données comme des observations fixes non aléatoires. Vous incorporez des croyances a priori pour faire des inférences sur les événements que vous observez.

En tant que fréquentiste, vous croyez qu'il existe une seule valeur vraie pour les inconnues que nous cherchons et ce sont les données qui sont aléatoires et incomplètes. Le fréquentiste échantillonne aléatoirement les données d'une population inconnue et fait des inférences sur les vraies valeurs des paramètres inconnus en utilisant cet échantillon.

En fin de compte, les approches bayésienne et fréquentiste ont leurs propres forces et faiblesses. Chacune a les outils pour résoudre presque tous les problèmes que l'autre peut résoudre. Comme différents langages de programmation, elles doivent être considérées comme des outils de force égale qui peuvent être mieux adaptés à un certain problème et moins adaptés à un autre. Utilisez-les toutes les deux, utilisez-les judicieusement, et ne tombez pas dans la fureur d'une guerre sainte entre les deux camps de statisticiens !

Appris quelque chose ? Cliquez sur le ? pour dire « merci ! » et aider les autres à trouver cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BmeMhlgcVf1kU7eqlP0Ndg.jpeg)