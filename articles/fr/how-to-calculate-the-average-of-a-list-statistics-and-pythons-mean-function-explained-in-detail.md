---
title: Comment Calculer la Moyenne d'une Liste — Statistiques et Fonction Mean de
  Python Expliquées en Détail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-09T07:59:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-the-average-of-a-list-statistics-and-pythons-mean-function-explained-in-detail
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99ca740569d1a4ca21bb.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: Python
  slug: python
- name: statistics
  slug: statistics
seo_title: Comment Calculer la Moyenne d'une Liste — Statistiques et Fonction Mean
  de Python Expliquées en Détail
seo_desc: "By Armstrong Subero\nMathematics and programming go hand in hand. If you\
  \ are a programmer, at some point you will have to use mathematics. \nData science,\
  \ machine learning, artificial intelligence, and cryptocurrencies are all based\
  \ on complex underlyi..."
---

Par Armstrong Subero

Les mathématiques et la programmation vont de pair. Si vous êtes programmeur, à un moment donné, vous devrez utiliser les mathématiques. 

La science des données, l'apprentissage automatique, l'intelligence artificielle et les cryptomonnaies reposent toutes sur des principes mathématiques complexes sous-jacents. 

Cependant, l'utilisation des fonctions mathématiques n'a pas à être complexe ! Python abstrait tout, donc une fois que vous comprenez les concepts, vous n'aurez pas besoin de comprendre tous les détails de l'implémentation.

## Les mathématiques n'ont pas à faire peur

Il existe de nombreuses fonctions mathématiques que vous rencontrerez. Si vous travaillez avec des données ou des analyses, il est important que vous compreniez certains principes et fonctions mathématiques. 

L'une de ces fonctions que vous devez comprendre est la fonction `mean`.

Ne vous laissez pas rebuter par le nom — il n'y a rien de méchant (jeu de mots intentionnel) à propos de la fonction `mean` en Python. 

Cet article est autonome, mais je suppose que vous avez une certaine expérience de travail avec Python et que vous savez ce qu'est une liste Python. Si ce n'est pas le cas, consultez [cet article](https://www.freecodecamp.org/news/python-lists-explained-len-pop-index-and-list-comprehension/) avant de continuer. 

Une fois que vous aurez terminé, revenez et rejoignez-moi pour une plongée en profondeur dans la fonction `mean`.

## **Statistiques** 

Donc, vous voulez en savoir plus sur la fonction `mean`. C'est génial ! Mais avant d'examiner cette fonction, il est important de regarder la discipline dont elle provient : les statistiques. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/stat_graph.png)
_Les statistiques ont des outils comme celui-ci_

Sur l'image ci-dessus, nous voyons un graphique. Un graphique est une représentation picturale qui montre la relation d'une variable par rapport à une autre. 

Les graphiques sont utiles car ils nous permettent d'organiser les données afin que nous puissions voir rapidement les tendances et les relations entre les données. Un graphique n'est qu'un outil parmi tant d'autres que nous pouvons utiliser pour visualiser et analyser les données. 

Les statistiques sont une branche des mathématiques qui nous permet d'avoir une méthode systématique pour classer, analyser et interpréter les données. Cela est important car avec les statistiques, nous avons une collection d'outils prêts à l'emploi pour faire chacune de ces choses. 

Imaginez si vous deviez réinventer une scie chaque fois que vous aviez besoin de couper un morceau de bois. Nous aurions beaucoup de gens appelant les scies par différents noms, même si elles font la même chose. Pour éviter ce problème, nous avons donné à la scie un nom auquel tout le monde peut se référer. 

Il en va de même pour les statistiques — nous avons des outils bien connus que tout le monde connaît. L'un de ces outils est la moyenne.

## Mode, Médiane et Moyenne

Bien que la moyenne soit parfaitement capable de se suffire à elle-même, elle est généralement enseignée dans le cadre d'un trio, qui inclut le mode, la médiane et la moyenne. 

Examinons un groupe de nombres pour que vous compreniez ce qui se passe ici. Imaginez que vous avez les nombres suivants :

 <h2 style="text-align:center;">1, 2, 3, 3, 4, 6, 9</h2
     >

Disons que nous voulions exprimer quel nombre se produit le plus de fois. Ce serait 3, et le nom que nous donnons à cette propriété est le mode. Le mode est le nombre le plus fréquent dans un ensemble que nous examinons.

Le nombre au milieu d'un ensemble ordonné est appelé la médiane. Pour trouver la médiane d'un ensemble numérique, disposez les nombres du plus petit au plus grand, puis regardez le nombre au milieu. L'ensemble de nombres ci-dessus est déjà disposé du plus petit au plus grand, donc le nombre médian est également 3.

Enfin, la moyenne est une autre façon de se référer à la moyenne de l'ensemble. Pour trouver la moyenne, il suffit d'additionner tous les nombres ensemble et de diviser par le nombre total d'éléments dans l'ensemble. Dans le cas des nombres ci-dessus, si nous les additionnons tous ensemble, nous obtenons 28. Le nombre total d'éléments dans l'ensemble est de 7, donc notre moyenne est de 4. 

## Pourquoi Avons-Nous Besoin de la Moyenne ?

À ce stade, vous vous demandez peut-être pourquoi nous aurions besoin de trouver la moyenne d'un nombre de toute façon. 

Le fait est que même les statistiques elles-mêmes sont subdivisées en plusieurs groupes. Tout comme vous avez des outils qui sont utilisés pour travailler le bois et d'autres pour travailler le métal, certains outils en statistiques sont regroupés en classes puisqu'ils sont utilisés à des fins similaires. 

L'un de ces groupes en statistiques est appelé statistiques sommaires. L'une des choses pour lesquelles les statistiques sont utilisées est de décrire les données, et les statistiques sommaires sont une collection d'outils utilisés à cette fin. L'un des éléments de cette classe d'outils est la moyenne.

La moyenne est importante car elle nous aide à analyser ce que l'on appelle une distribution. En statistiques, une distribution est une méthode que nous utilisons pour examiner une variable sur laquelle nous voulons des informations. En utilisant une distribution, nous examinerons les valeurs de cette variable et la fréquence à laquelle elle se produit. 

Si nous collectons des données, un type courant de distribution que nous voyons est la distribution normale qui prend la forme de la courbe en cloche :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/bell_curve.png)
_La distribution normale_

C'est-à-dire que la variable aura une valeur commune vers laquelle elle tend, ainsi qu'un point de départ et un point final. 

Ce que fait la moyenne, c'est qu'elle nous permet de prendre une distribution comme celle-ci et de regarder la tendance centrale de la variable, qui est le point auquel les valeurs de la variable tendent à se regrouper. 

Ainsi, nous pouvons dire que la moyenne décrit la tendance centrale de la distribution. 

## Calcul de la Moyenne en Python 

Nous pouvons calculer manuellement la moyenne si nous avons un petit ensemble de données numériques avec lequel travailler. Cependant, lorsque nous avons des centaines ou des milliers de valeurs dans un ensemble de données, il devient impossible de le calculer à la main.

Puisque Python est un langage "tout compris", la façon dont nous pouvons faire cela est d'utiliser la fonction `mean` du module statistics dans Python. 

Utilisons la fonction `mean` pour calculer la moyenne de l'ensemble de données numériques que nous avions plus tôt dans l'article :

<pre><code>
# 1. importer le module statistics
import statistics

# 2. liste contenant notre ensemble de données numériques
numerical_data_set = [1, 2, 3, 3, 4, 6, 9]

# 3. calculer la moyenne
calc_mean = statistics.mean(numerical_data_set)

# 4. afficher notre moyenne calculée
print("La moyenne est : ", calc_mean)
</code></pre>

Notre code se compose d'une séquence en 4 étapes que nous pouvons utiliser pour calculer la moyenne :

1. Nous importons le module statistics qui contient notre fonction mean
2. Nous créons une liste Python contenant l'ensemble de données numériques dont nous souhaitons calculer la moyenne
3. Nous calculons la moyenne et stockons le résultat dans une variable, `calc_mean`
4. Nous affichons notre moyenne calculée afin d'obtenir un retour visuel

Lorsque nous exécutons le code, nous obtenons le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/mean.png)
_Notre résultat_

Le programme affiche la même valeur que nos calculs manuels. Lorsque nous travaillons avec de grands ensembles de données, cette fonction sera capable de s'adapter à tout ce que nous pouvons lui lancer. 

## Conclusion

Dans cet article, nous avons examiné la fonction `mean` en Python. Nous avons commencé par discuter des statistiques dans leur ensemble, puis nous avons plongé en profondeur dans la moyenne.

Maintenant que vous avez une solide compréhension des statistiques et de la fonction `mean` en Python, vous pouvez l'utiliser dans vos propres programmes.

Si vous avez aimé cet article, alors vous pourriez également être curieux d'en savoir plus sur les structures de données et les algorithmes. Si vous voulez un guide simple, clair, étape par étape pour apprendre les structures de données et les algorithmes sans avoir à écrire une seule ligne de code, alors vous pouvez consulter le livre Codeless Data Structures and Algorithms. 

Lisez le livre ici :

%[https://www.apress.com/gp/book/9781484257241]