---
title: L'architecture des mathématiques – Et comment les développeurs peuvent l'utiliser
  dans le code
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2025-05-23T15:06:16.766Z'
originalURL: https://freecodecamp.org/news/the-architecture-of-mathematics-and-how-developers-can-use-it-in-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748012748947/1df613bf-93e7-4f03-b0f0-47ff49f38504.png
tags:
- name: Mathematics
  slug: mathematics
- name: Math
  slug: math
- name: Machine Learning
  slug: machine-learning
- name: history
  slug: history
- name: MathJax
  slug: mathjax
- name: General Programming
  slug: programming
seo_title: L'architecture des mathématiques – Et comment les développeurs peuvent
  l'utiliser dans le code
seo_desc: '"To understand is to perceive patterns." - Isaiah Berlin


  Math is not just numbers. It is the science of finding complex patterns that shape
  our world. This means that to truly understand it, we need to see beyond numbers,
  formulas, and theorems and ...'
---

> "Comprendre, c'est percevoir des motifs." - Isaiah Berlin

Les mathématiques ne sont pas seulement des nombres. C'est la science qui consiste à trouver des motifs complexes qui façonnent notre monde. Cela signifie que pour vraiment les comprendre, nous devons voir au-delà des nombres, des formules et des théorèmes et comprendre leurs structures.

L'objectif principal de cet article est de montrer comment les mathématiques sont comme un arbre d'idées en croissance. Je veux montrer que les mathématiques sont un système vivant de logique, et non pas seulement des formules à mémoriser. Avec des analogies, de l'histoire et des exemples de code, je veux vous aider à comprendre les mathématiques plus profondément et comment vous pouvez les appliquer à la programmation.

J'ai également inclus quelques exemples de code ici pour vous aider à connecter la théorie et la pratique. Je les montre pour démontrer comment les idées mathématiques sont appliquées à des problèmes réels. Que vous soyez nouveau dans les mathématiques plus avancées ou plus expérimenté, ces exemples de code vous aideront à comprendre comment appliquer les mathématiques en programmation.

Ce lien entre théorie et application reflète mes propres études. Je suis finaliste d'une licence en génie électrique et informatique à la NOVA FCT, l'une des meilleures facultés d'ingénierie du Portugal.

Mon diplôme en ingénierie est celui qui comprend plus de mathématiques et de physique. Cela est dû au fait qu'il est essentiel d'avoir une solide compréhension des mathématiques pour comprendre l'électronique, les télécommunications, la théorie du contrôle et d'autres domaines de l'ingénierie.

Voici un bref aperçu de certains des sujets de mathématiques et de physique que j'ai appris :

* **Équations différentielles partielles (EDP) :** Ces équations modélisent des phénomènes du monde réel, de la diffusion de la chaleur à l'économie d'un pays.

* **Analyse harmonique (Fourier & Laplace) :** Les transformations intégrales comme la transformée de Fourier et de Laplace nous permettent de comprendre les problèmes dans de nouveaux domaines.

* **Analyse complexe :** Étendre le calcul dans le plan complexe donne naissance à des outils puissants utilisés en physique et en ingénierie.

* **Analyse numérique :** Lorsque les solutions analytiques sont impossibles ou inefficaces, les méthodes numériques fournissent des approximations basées sur ordinateur. Cela est crucial pour les applications du monde réel.

* **Théorie du contrôle et des signaux :** Ces domaines nous montrent comment concevoir des systèmes stables comme des fusées, des trains et des robots.

* **Physique :** Les cours de mécanique classique et d'électromagnétisme ont aidé à relier les mathématiques théoriques aux lois physiques.

Au cours de mes années d'étude, en plus des compétences techniques, j'ai développé une compréhension plus profonde du fonctionnement du monde et de la structure du domaine des mathématiques. Et j'ai commencé à trouver des motifs dans la façon dont les mathématiques sont un cadre de logique interconnectée.

### Dans cet article, nous explorerons :

* [Analogie simple : L'arbre des mathématiques](#heading-installation)

* [La structure et l'histoire des mathématiques](#heading-la-structure-et-lhistoire-des-mathematiques)

* [Un exemple d'arbre : Les fondements de la relativité par Albert Einstein](#heading-un-exemple-darbre-les-fondements-de-la-relativite-par-albert-einstein)

* [Le plus grand paradoxe des mathématiques, découvert par Kurt Gödel](#heading-le-plus-grand-paradoxe-des-mathematiques-decouvert-par-kurt-godel)

* [Et les mathématiques appliquées et l'ingénierie ?](#heading-et-les-mathematiques-appliquees-et-lingenierie)

* [Exemples de code – Approches analytiques et numériques](#heading-exemples-de-code-approches-analytiques-et-numeriques)

* [L'impact d'une grande théorie unifiée des mathématiques](#heading-limpact-dune-grande-theorie-unifiee-des-mathematiques)

* [Une leçon finale de l'histoire](#heading-une-lecon-finale-de-lhistoire)

## Analogie simple : L'arbre des mathématiques

![Photo de deux arbres par Johannes Plenio : https://www.pexels.com/photo/two-brown-trees-1632790/](https://cdn.hashnode.com/res/hashnode/image/upload/v1747518175609/78838825-d872-42df-9dc8-736fa012a630.jpeg align="center")

Imaginez les mathématiques comme un vaste arbre qui pousse pour toujours.

Les racines de l'arbre sont les fondements des mathématiques : la logique et la théorie des ensembles. De cette fondation émergent les principaux champs de base des mathématiques : l'arithmétique, l'algèbre, la géométrie et l'analyse.

À mesure que l'arbre se divise de plus en plus en branches, de nouveaux sous-domaines plus complexes commencent à apparaître, comme la topologie, l'algèbre abstraite et l'analyse complexe. Parfois, les branches sont connectées les unes aux autres.

Et n'oubliez pas : cet arbre est toujours en croissance dans de nombreuses directions. Des branches créant de nouvelles branches aux branches se connectant à d'autres branches. Petit à petit, il grandit.

Au cours de l'histoire, il y a eu des moments où, en raison de certaines grandes découvertes scientifiques, des parties de l'arbre des mathématiques ont commencé à croître très rapidement. D'autres fois, des décennies, voire des siècles, se sont écoulés sans que de nombreuses nouvelles branches apparaissent. C'est le cas des nombres imaginaires, par exemple.

Et vous pourriez vous demander : Combien de nouvelles branches et de connexions entre elles continueront à apparaître ?

## La structure et l'histoire des mathématiques

![Photo d'un bureau et d'un cahier sur Pixabay : https://www.pexels.com/photo/brown-wooden-desk-159618/](https://cdn.hashnode.com/res/hashnode/image/upload/v1747518363058/9911acd4-ad4f-4da2-a62b-9fa87e219c35.jpeg align="center")

Les premières idées mathématiques sont apparues indépendamment dans les anciennes civilisations. Par exemple :

* L'invention du zéro en Inde

* Les avancées algébriques islamiques

* La rigueur géométrique grecque

Au fil du temps, de nombreux grands mathématiciens ont créé et partagé ces idées en écrivant et en donnant des conférences.

Finalement, ces nouvelles idées ont été largement partagées avec de nouvelles générations et ces nouvelles générations ont créé de nouvelles mathématiques basées sur les anciennes.

C'est ainsi que de nouvelles branches naissent continuellement des branches précédentes de l'arbre des mathématiques.

Et c'est pourquoi Isaac Newton a écrit, dans une lettre à Robert Hooke en 1675 :

> Si j'ai vu plus loin, c'est en me tenant sur les épaules de géants

Il voulait dire qu'en travaillant à partir de connaissances précédentes, il a été capable de créer et de (re)découvrir de nouvelles idées.

Pourtant, le vrai pouvoir des mathématiques réside dans leur pratique répétée et leur compréhension de plus en plus profonde. Comme l'un de mes professeurs l'a un jour expliqué :

> *Plus important que de connaître les théorèmes est de connaître les idées derrière eux et l'histoire de leur création.*

Très souvent, pour résoudre des problèmes, il est nécessaire de penser en termes de premiers principes et de construire à partir de là. Les mathématiques enseignent exactement cela. De cette manière, les mathématiques ne sont pas seulement une matière académique. C'est une langue parlée par les scientifiques et les ingénieurs du monde entier.

En les ayant bien préservées et partagées, il est encore possible de créer de nouvelles mathématiques à partir d'idées précédentes. Et il est possible pour le grand arbre de continuer à croître sur la base de branches ou de nœuds précédents.

## Un exemple d'arbre : Les fondements de la relativité par Albert Einstein

![Albert Einstein, l'un des plus grands géants de la physique de l'histoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1747518865627/e84ff108-b383-405b-8bb0-73ffb50b4dcf.jpeg align="center")

Albert Einstein a créé les théories de la relativité générale et spéciale. Celles-ci ont de grandes conséquences de nos jours :

* GPS et communication globale

* Avancées en télécommunications par satellite

* Exploration spatiale et lancements de satellites

Mais cela n'a été possible que grâce à l'unification de la géométrie avec le calcul, appelée **géométrie différentielle**. L'évolution de la géométrie différentielle s'est produite sur des siècles, grâce à de nombreux grands mathématiciens. Voici quelques-uns d'entre eux, mais cette liste n'est pas exhaustive :

* **Euclide (vers 300 av. J.-C.) :** A contribué à la géométrie, posant les bases des systèmes mathématiques ultérieurs

* **Archimède (vers 287–212 av. J.-C.) :** A été un pionnier dans la compréhension du volume, de la surface et des principes de la mécanique

* **René Descartes (1596–1650) :** A développé les coordonnées cartésiennes et la géométrie analytique

* **Isaac Newton (1642–1727) & Gottfried Wilhelm Leibniz (1646–1716) :** Les lois du mouvement et de la gravitation de Newton, ainsi que le développement du calcul par Leibniz, ont formé la base de la mécanique classique que Einstein a cherché à étendre et à modifier dans sa théorie de la relativité.

* **Leonhard Euler (1707–1783) :** A contribué au développement des équations différentielles, essentielles dans les fondements mathématiques de la physique.

* **Gaspard Monge (1746–1818) :** Le père de la géométrie différentielle et pionnier en géométrie descriptive

* **Carl Friedrich Gauss (1777–1855) :** A réalisé des avancées révolutionnaires en géométrie, y compris le concept de surfaces courbes.

* **Bernhard Riemann (1826–1866) :** A introduit la géométrie riemannienne, une branche de la géométrie différentielle.

Une fois de plus, comme l'a écrit Isaac Newton, dans une lettre à Robert Hooke en 1675 :

> Si j'ai vu plus loin, c'est en me tenant sur les épaules de géants.

Albert Einstein a vu ce que personne d'autre de son temps n'a vu, grâce à ces grands géants des mathématiques et à d'innombrables autres.

## Le plus grand paradoxe des mathématiques, découvert par Kurt Gödel

![Kurt Gödel, l'un des plus grands géants des mathématiques de l'histoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1747518411126/df53f84c-f920-4b42-9081-5aeb1017f543.jpeg align="center")

Le plus grand paradoxe des mathématiques, à mon avis, est ce que Kurt Gödel a découvert. Ses recherches du début du 20ème siècle ont révélé une limitation au sein de ce cycle.

Ce paradoxe – c'est-à-dire [ses théorèmes d'incomplétude](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems) – montre que dans tout système formel cohérent capable d'exprimer une arithmétique simple, il y aura toujours des énoncés mathématiques vrais qui ne peuvent être prouvés au sein du système lui-même.

Cela signifie que dans TOUS les systèmes, il y a des limites à ce que vous pouvez réellement prouver comme étant vrai ou faux. Pour les mathématiciens, cela signifie que l'arbre ne sera jamais complété. Il existe des vérités qui vont au-delà des vérités formelles, et pourtant nous supposons toujours qu'elles sont vraies (bien que non prouvées).

Ainsi, cela prouve que peu importe combien de mathématiciens travaillent dans le domaine ou combien d'IA est utilisée pour trouver de nouvelles mathématiques, il existera toujours des limitations. Certaines choses sont impossibles à prouver qu'elles sont vraies, et nous savons simplement qu'elles le sont grâce à des estimations d'approximation et à d'autres méthodes non logiques exactes.

## Et les mathématiques appliquées et l'ingénierie ?

![Photo par JESHOOTS.com : https://www.pexels.com/photo/person-holding-a-chalk-in-front-of-the-chalk-board-714699/](https://cdn.hashnode.com/res/hashnode/image/upload/v1747518581076/606f3bce-d7db-4ac3-9322-833673a734b0.jpeg align="center")

Les mathématiques appliquées et l'ingénierie impliquent l'interprétation des mêmes idées de mathématiques pures dans des scénarios du monde réel. En fait, dans de nombreux cas, c'est la combinaison de nombreuses idées mathématiques. Considérons quelques exemples :

L'analyse en composantes principales (PCA) est un outil largement utilisé en science des données. Pourtant, c'est un mélange d'algèbre linéaire (dans la PCA, valeurs propres) avec l'optimisation (ordonner les valeurs propres qui représentent plus de données avec moins de données) afin de rendre les ensembles de données plus courts.

En apprentissage automatique, la régression logistique est un mélange de calcul avec des statistiques et des probabilités.

En analyse harmonique, les transformées de Laplace, de Fourier et Z sont un moyen de voir la même chose dans un nouveau domaine pour obtenir de nouvelles perspectives. Dans ce cas, des intégrales sont utilisées pour faire cette cartographie.

En apprentissage profond, les réseaux de neurones ne sont que de nombreuses matrices qui se multiplient et se mettent à jour pour s'adapter à un ensemble de données représentant un système. Cette optimisation des valeurs de la matrice se fait avec des fonctions d'activation, une méthode d'optimisation basée sur la descente de gradient (indique de combien les valeurs doivent changer) et la rétropropagation (applique ces altérations à toutes les valeurs de la matrice).

J'ai en fait écrit un article où j'enseigne [pourquoi les fonctions d'activation sont importantes](https://www.freecodecamp.org/news/activation-functions-in-neural-networks/) si vous voulez le consulter.

Mais le meilleur exemple de cette fusion des mathématiques avec l'ingénierie se trouve dans [la théorie du contrôle](https://www.freecodecamp.org/news/basic-control-theory-with-python/).

La théorie du contrôle est l'étude de l'architecture des systèmes. Des trains aux voitures en passant par les avions, tout est basé sur la théorie du contrôle. Elle est partout dans presque tous les dispositifs électroniques modernes. Dans les circuits électriques, la théorie du contrôle est également largement utilisée pour garantir la stabilité du circuit face aux perturbations électriques.

Ainsi, comme vous pouvez probablement commencer à le voir, beaucoup des outils que nous avons maintenant ne sont qu'un mélange de nombreuses idées de mathématiques pures. Juste de nombreuses combinaisons et recettes d'idées de mathématiques pures. En essence, les mathématiques appliquées sont l'application des mathématiques pures en tant qu'"ingrédients" dans des "recettes" pour résoudre des problèmes.

Nous avons donc exploré la structure et l'évolution des mathématiques. Pourtant, il est important de voir comment ces idées peuvent être appliquées dans la vie réelle. Les mathématiques pures constituent le cadre, et les mathématiques appliquées appliquent ce cadre pour résoudre des problèmes. Pour comprendre cela, nous examinerons deux exemples de code qui montrent comment vous pouvez utiliser les idées mathématiques comme outils de programmation.

## Exemples de code – Approches analytiques et numériques

Ces exemples de code démontrent quelques façons dont vous pouvez utiliser Python pour résoudre des équations mathématiques.

Dans le premier exemple de code, nous résoudreons le problème de la même manière que les enfants à l'école résolvent les exercices de mathématiques : essentiellement, à la main avec un crayon. En déplaçant les variables de gauche à droite pour trouver leurs valeurs. Dans le deuxième exemple, nous résoudreons le problème en utilisant l'analyse numérique.

### Exemple 1 : Résoudre un problème de manière analytique

Lorsque nous résolvons des problèmes de mathématiques de manière analytique, comme nous l'avons fait à l'école, nous manipulons des symboles pour obtenir des valeurs exactes. Souvent, ces symboles sont x, y et z. En Python, nous pouvons faire cela en utilisant la bibliothèque SymPy :

```python
from sympy import symbols, Eq, solve

x, y = symbols('x y')
eq1 = Eq(2*x + 3*y, 6)
eq2 = Eq(-x + y, 1)

solution = solve((eq1, eq2), (x, y))
print(solution)
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1747160359386/7a21cddc-f4ba-4f9f-afa0-d1cc11fb27d6.png align="center")

Essentiellement, nous trouvons x et y en fonction de cette équation :

$$\begin{align*} 2x + 3y &= 6 \\ -x + y &= 1 \end{align*}$$

Ce qui nous donne le résultat suivant :

```python
{x: 3/5, y: 8/5}
```

Ou :

* x= 0,6

* y = 1,6

Lorsque nous disons que nous résolvons cela de manière analytique, cela signifie que nous trouvons une solution mathématique exacte en utilisant des formules ou des équations.

Mais de nombreuses fois, les problèmes sont plus difficiles et peuvent être résolus en ajoutant des symboles à droite ou à gauche de l'équation.

Parfois, il peut y avoir tellement de symboles et de versions transformées de ceux-ci, avec des choses comme des dérivées et des intégrales, que cela peut devenir très difficile à gérer et prendre beaucoup de temps.

Pour cette raison, il existe un domaine des mathématiques consacré à la recherche d'approximations de formules mathématiques déjà créées, appelé analyse numérique. Cela rend la résolution de ces problèmes plus rapide. Et c'est la méthode que nous allons explorer ensuite.

### Exemple 2 : Résoudre numériquement (Approximation)

Nous allons maintenant utiliser SciPy pour résoudre le même système avec des méthodes numériques :

```python
import numpy as np
from scipy.linalg import solve

A = np.array([[3, 2, -1, 4, 5],
              [1, 1, 3, 2, -2],
              [4, -1, 2, 1, 0],
              [5, 3, -2, 1, 1],
              [2, -3, 1, 3, 4]])

b = np.array([12, 5, 7, 9, 10])

solution = solve(A, b)

print(solution)
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1747160347486/d1f17aa6-b288-4e41-9be7-0810c45e778c.png align="center")

Dans cet exemple de code, cette ligne de code :

```python
solution = solve(A, b)
```

Utilise la méthode [solve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html) de la bibliothèque Python [SciPy](https://scipy.org/) :

```python
from scipy.linalg import solve
```

C'est une méthode qui vous aide à trouver les valeurs de x dans une équation Ax=b, où a est une grille carrée de nombres et b est une liste de nombres. Ce qui nous donne ce qui suit :

```python
[ 1.35022026 -0.79955947 -1.17180617  3.14317181 -0.83920705]
```

Maintenant, imaginez, dans ce cas simple, qu'une matrice comme A pourrait représenter le **flux de trafic** entre des villes ou des intersections, et b pourrait représenter le **trafic entrant ou sortant** de chaque ville.

En résolvant le système, cela pourrait nous aider à déterminer la distribution du trafic entre les villes pour répondre aux conditions de trafic souhaitées.

Bien sûr, ces types de problèmes sont beaucoup plus complexes dans la vie réelle. Mais pour comprendre et résoudre les grands problèmes, vous devez d'abord comprendre les petits problèmes.

Et au fait, un système d'équations est la même chose qu'une matrice. Nous représentons simplement les systèmes d'équations sous forme de matrices pour faciliter la compréhension des propriétés et la clarté.

Le problème est qu'en utilisant des matrices, il est plus facile de faire des calculs et d'effectuer des mathématiques d'algèbre linéaire pour vérifier les caractéristiques de la matrice et mieux la comprendre.

En essence, une matrice représente un système d'équations. De plus, les systèmes d'équations peuvent représenter des phénomènes de la vie réelle comme l'économie d'un pays ou la météo.

Si vous voulez en savoir plus, j'ai écrit un [article entier sur l'analyse numérique](https://www.freecodecamp.org/news/numerical-analysis-explained-how-to-apply-math-with-python/) que vous pouvez consulter.

## L'impact d'une grande théorie unifiée des mathématiques

![Photo par Porapak Apichodilok : https://www.pexels.com/photo/person-holding-world-globe-facing-mountain-346885/](https://cdn.hashnode.com/res/hashnode/image/upload/v1747518681068/54a9556c-2a79-441c-a6d6-27ff38e1f4ff.jpeg align="center")

Malgré le plus grand paradoxe des mathématiques, que se passerait-il avec une [Grande Théorie Unifiée des Mathématiques](https://www.scientificamerican.com/article/the-evolving-quest-for-a-grand-unified-theory-of-mathematics/) ?

Rappelez-vous qu'une telle théorie nous dit qu'il existe des choses qui sont vraies mais impossibles à prouver formellement, et nous devons simplement l'accepter. Mais même avec cette hypothèse, il est toujours possible d'unifier toutes les mathématiques.

C'est ce que [le programme de Langlands](https://en.wikipedia.org/wiki/Langlands_program) essaie de résoudre. Une sorte de tentative pour interconnecter les plus grandes parties du grand arbre des mathématiques afin de découvrir de nouveaux motifs en mathématiques.

Avec une Grande Théorie Unifiée des Mathématiques, nous serions en mesure de comprendre comment chaque branche de l'arbre se connecte avec les autres et toutes les relations entre elles.

### Quelle est la valeur de cette grande unification pour la société ?

En étudiant l'histoire, nous pouvons trouver des motifs. L'unification de divers domaines a créé de nombreux impacts massifs sur la société, tels que :

* Au 19ème siècle, James Clerk Maxwell a uni les domaines de *l'électricité* et du *magnétisme* avec ses célèbres équations de Maxwell. Cela a permis la création de radios et de réseaux électriques dans le monde entier. À son tour, cela a servi de fondation à tous les progrès technologiques des 20ème et 21ème siècles.

* Au 20ème siècle, l'unification de *l'algèbre* avec la *logique* a conduit à l'essor des systèmes numériques. À leur tour, les systèmes numériques ont donné naissance aux processeurs et à l'évolution des ordinateurs vers l'ordinateur portable moderne.

* Également au 20ème siècle, l'unification de la *probabilité* et de la *communication* a conduit à la théorie de l'information. Cela est devenu la fondation de l'internet. Cette unification a été réalisée par un grand mathématicien nommé Claude Shannon.

En fin de compte, une Grande Théorie Unifiée des Mathématiques pourrait être l'une des plus grandes réalisations de la société moderne.

Elle pourrait conduire à de nouvelles découvertes en physique, comme dans la théorie des cordes ou la gravité quantique, où des structures mathématiques profondes sont nécessaires pour créer une nouvelle physique. En IA, elle pourrait aider à unifier tous les modèles d'apprentissage automatique dans une architecture commune. Cela aiderait à accélérer le développement de nouveaux modèles d'IA. Elle pourrait également ouvrir la porte à de nouvelles méthodes cryptographiques et à des avancées en science des matériaux, révélant, avec les mathématiques, les motifs profonds encore non trouvés dans ces domaines.

Tout comme l'unification de l'électricité et du magnétisme a conduit à la technologie moderne, un cadre mathématique unifié conduirait à une vague d'innovation.

## Une leçon finale de l'histoire

De la géométrie grecque à l'IA, les mathématiques ont grandi comme un arbre au fil des siècles. En comprenant sa structure, il est possible de voir son rôle dans la découverte des motifs de notre univers. J'espère avoir pu vous faire voir les mathématiques de cette manière.

De plus, nous pouvons conclure que l'unification des domaines scientifiques crée les fondations pour la création de nouvelles innovations afin d'aider la société à avancer. De nombreuses transformations sociétales profondes n'ont vu le jour que grâce à des idées mathématiques abstraites. Lorsque celles-ci sont partagées et affinées, elles deviennent l'architecture cachée du progrès dans la société. L'innovation commence lorsque des idées déconnectées sont unies, bien liées et largement partagées.

Trouvez le code complet [ici](https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code).