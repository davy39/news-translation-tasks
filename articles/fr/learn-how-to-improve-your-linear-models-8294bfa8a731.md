---
title: Comment utiliser des modèles de régression linéaire pour prédire des fonctions
  quadratiques, racines et polynomiales
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-11T16:00:41.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-improve-your-linear-models-8294bfa8a731
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GsSExG8KXYBd6rk7assRTQ.png
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: R Language
  slug: r
seo_title: Comment utiliser des modèles de régression linéaire pour prédire des fonctions
  quadratiques, racines et polynomiales
seo_desc: 'By Björn Hartmann

  When reading articles about machine learning, I often suspect that authors misunderstand
  the term “linear model.” Many authors suggest that linear models can only be applied
  if data can be described with a line. But this is way too ...'
---

Par Björn Hartmann

Lorsque je lis des articles sur l'apprentissage automatique, je soupçonne souvent que les auteurs comprennent mal le terme « modèle linéaire ». De nombreux auteurs suggèrent que les modèles linéaires ne peuvent être appliqués que si les données peuvent être décrites avec une ligne. Mais cela est beaucoup trop restrictif.

Les modèles linéaires **supposent que la forme fonctionnelle est linéaire — et non la relation entre vos variables**.

Je vais vous montrer comment vous pouvez améliorer vos régressions linéaires avec des fonctions quadratiques, racines et exponentielles.

![Image](https://cdn-media-1.freecodecamp.org/images/3hDIpUpiqmEqht4LpuzcXCnSIvUHGAUlruxI)

### Alors, quelle est la forme fonctionnelle ?

La forme fonctionnelle est **l'équation que vous souhaitez estimer**.

Commençons par un exemple et réfléchissons à la manière dont nous pourrions décrire les salaires des data scientists. Supposons qu'un data scientist moyen (`i`) reçoit un salaire de niveau d'entrée (`entry_level_salary`) plus un bonus pour chaque année de son expérience (`experience_i`).

Ainsi, son salaire (`salary_i`) est donné par la forme fonctionnelle suivante :

```
salary_i = entry_level_salary + beta_1 * experience_i
```

Maintenant, nous pouvons interpréter le coefficient `beta_1` comme le bonus pour chaque année d'expérience. Et avec ce coefficient, nous pouvons commencer à faire des prédictions en connaissant simplement le niveau d'expérience.

Comme votre modèle d'apprentissage automatique prend en charge le coefficient `beta_1`, tout ce que vous devez entrer dans R ou tout autre logiciel est :

```
model_1 <- lm(salary ~ entry_level_salary + experience)
```

La linéarité dans la forme fonctionnelle nécessite que nous additionnions chaque déterminant du côté droit de l'équation.

Imaginez que nous avons raison avec nos hypothèses. Chaque point indique un data scientist avec son niveau d'expérience et son salaire. Enfin, la ligne rouge représente nos prédictions.

![Image](https://cdn-media-1.freecodecamp.org/images/wQDyE0LxhC8MjRfFhYJUckvRjMxaAf-761dG)

De nombreux aspirants data scientists exécutent déjà des prédictions similaires. Mais souvent, c'est tout ce qu'ils font avec les modèles linéaires...

### Comment estimer des modèles quadratiques ?

Lorsque nous voulons estimer un modèle quadratique, nous ne pouvons pas taper quelque chose comme ceci :

```
model_2 <- lm(salary ~ entry_level_salary + experience^2)
```

```
>> Cela rejettera un message d'erreur
```

La plupart de ces fonctions ne s'attendent pas à devoir transformer vos variables d'entrée. Par conséquent, elles rejettent un message d'erreur si vous essayez. De plus, vous n'avez plus de somme du côté droit de l'équation.

**Note :** Vous devez calculer `experience^2` avant de l'ajouter à votre modèle. Ainsi, vous exécuterez :

```
# D'abord, calculez les valeurs au carré de l'expérience
experience_2 <- experience^2
```

```
# Ensuite, ajoutez-les à votre régression
model_2 <- lm(salary ~ entry_level_salary + experience_2)
```

En retour, vous obtenez une belle fonction quadratique :

![Image](https://cdn-media-1.freecodecamp.org/images/2MNxj09K-gnrnxKAJspCA84cUFOQB1CSbCBA)

### Estimer des fonctions racines avec des modèles linéaires

Souvent, nous observons des valeurs qui augmentent rapidement au début et s'alignent sur un certain niveau par la suite. Modifions notre exemple et estimons une courbe d'apprentissage typique.

Au début, une courbe d'apprentissage tend à être très raide et ralentit après quelques années.

Il existe une fonction qui présente une telle tendance, la fonction `racine`. Nous utilisons donc la `racine carrée` de `experience` pour capturer cette relation :

```
# D'abord, calculez les valeurs de la racine carrée de l'expérience
sqrt_experience <- sqrt(experience)
```

```
# Ensuite, ajoutez-les à votre régression
model_3 <- lm(knowledge ~ sqrt_experience)
```

Assurez-vous à nouveau de calculer la racine carrée avant de l'ajouter à votre modèle :

![Image](https://cdn-media-1.freecodecamp.org/images/ZKh8gvc9V8Wz-9Hht1PJHA67-n6PJh6cP6Mm)

Ou vous pourriez vouloir utiliser la fonction logarithmique car elle décrit une tendance similaire. Mais ses valeurs sont négatives entre zéro et un. Assurez-vous donc que cela ne pose pas de problème pour vous et vos données.

### Maîtriser les modèles linéaires

Enfin, vous pouvez même estimer des fonctions polynomiales d'ordres supérieurs ou des fonctions exponentielles. Tout ce que vous avez à faire est de calculer toutes les variables avant de les ajouter à votre modèle linéaire :

```
# D'abord, calculez les polynômes
experience_2 <- experience^2
experience_3 <- experience^3
```

```
# Ensuite, ajoutez-les à votre régression
model_4 <- lm(salary ~ experience + experience_2 + experience_3)
```

![Image](https://cdn-media-1.freecodecamp.org/images/91UHlbibDwztx9AAcMQMPFqKA9Ub5zLpekOu)

### Deux cas où vous devriez utiliser d'autres modèles

Bien que les modèles linéaires puissent être appliqués à de nombreux cas, il existe des limitations. Les plus populaires peuvent être divisés en deux catégories :

#### 1. Probabilités :

Si vous souhaitez estimer la probabilité d'un événement, il est préférable d'utiliser des modèles Probit, Logit ou Tobit. Lorsque vous estimez des probabilités, vous utilisez des distributions que les fonctions linéaires ne peuvent pas capturer. Selon la distribution que vous supposez, vous devez choisir entre le modèle Probit, Logit ou Tobit.

#### 2. Variables de comptage

Enfin, lorsque vous estimez une variable de comptage, vous souhaitez utiliser un modèle de Poisson. Les variables de comptage sont des variables qui ne peuvent être que des entiers tels que `1, 2, 3, 4`.

Par exemple, comptez le nombre d'enfants, le nombre d'achats qu'un client effectue ou le nombre d'accidents dans une région.

### Ce qu'il faut retenir de cet article

Il y a deux choses que je veux que vous reteniez :

1. Améliorez vos modèles linéaires et essayez des fonctions quadratiques, racines ou polynomiales.
2. Transformez toujours vos données **avant** de les ajouter à votre régression.

J'ai téléchargé le code R pour tous les exemples sur [GitHub](https://github.com/bjoernhartmann/examples_linear_models). N'hésitez pas à les télécharger, à jouer avec eux ou à les partager avec vos amis et collègues.

![Image](https://cdn-media-1.freecodecamp.org/images/Er55BWHmZF-gxXl1HofpZX2znuPqRM7eIf88)

Si vous avez des questions, écrivez un commentaire ci-dessous ou [contactez-moi](https://www.bjoern-hartmann.de/?utm_source=medium&utm_medium=link&utm_campaign=Linear_Models&utm_term=Linear_Models). J'apprécie vos retours.