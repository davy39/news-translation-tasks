---
title: Comment lire un tableau de régression
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-31T20:25:40.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-sharadvm-how-to-read-a-regression-table-661d391e9bd7-708e75efc560
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kiLhwgfqplmsa9QgUfXjKQ.jpeg
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: predictive analytics
  slug: predictive-analytics
- name: '#Regression'
  slug: regression
- name: 'tech '
  slug: tech
seo_title: Comment lire un tableau de régression
seo_desc: 'By Sharad Vijalapuram

  What is regression?

  Regression is one of the most important and commonly used data analysis processes.
  Simply put, it is a statistical method that explains the strength of the relationship
  between a dependent variable and one or...'
---

Par Sharad Vijalapuram

### **Qu'est-ce que la régression ?**

La régression est l'un des processus d'analyse de données les plus importants et les plus couramment utilisés. En termes simples, il s'agit d'une méthode statistique qui explique la force de la relation entre une variable dépendante et une ou plusieurs variable(s) indépendante(s).

Une variable dépendante pourrait être une variable ou un champ que vous essayez de prédire ou de comprendre. Une variable indépendante pourrait être les champs ou les points de données que vous pensez pourraient avoir un impact sur la variable dépendante.

Ce faisant, elle répond à quelques questions importantes :

* Quelles variables comptent ?
* Dans quelle mesure ces variables comptent-elles ?
* À quel point sommes-nous confiants à propos de ces variables ?

### Prenons un exemple...

Pour mieux expliquer les chiffres dans le tableau de régression, j'ai pensé qu'il serait utile d'utiliser un ensemble de données d'exemple et de passer en revue les chiffres et leur importance.

J'utilise un petit ensemble de données qui contient les scores GRE (un test que les étudiants passent pour être considérés pour l'admission dans les écoles supérieures aux États-Unis) de 500 étudiants et leurs chances d'admission dans une université.

Parce que `chance d'admission` dépend du `score GRE`, `chance d'admission` est la variable dépendante et `score GRE` est la variable indépendante.

![Image](https://cdn-media-1.freecodecamp.org/images/gEmYfLngh9iyyI1iWPkIHT2H4VGekxpIxUHY)
_Nuage de points des scores GRE et des chances d'admission_

#### Ligne de régression

Tracer une ligne droite qui décrit le mieux la relation entre les scores GRE des étudiants et leurs chances d'admission nous donne la **ligne de régression linéaire**. Cela est connu sous le nom de **ligne de tendance** dans divers outils BI. L'idée de base derrière le tracé de cette ligne est de minimiser la distance entre les points de données à une coordonnée x donnée et la coordonnée y à travers laquelle la ligne de régression passe.

![Image](https://cdn-media-1.freecodecamp.org/images/ZKNDJUJRHA0Es0khr8RpLkbot3QmMPxsMc8Z)
_Nuage de points avec une ligne de régression._

La ligne de régression nous permet de représenter plus facilement la relation. Elle est basée sur une équation mathématique qui associe le coefficient x et l'ordonnée à l'origine.

**L'ordonnée à l'origine** est le point où la ligne intersecte l'axe des y à x = 0. C'est aussi la valeur que le modèle prendrait ou prédirait lorsque x est 0.

**Les coefficients** fournissent l'impact ou le poids d'une variable sur l'ensemble du modèle. En d'autres termes, ils fournissent la quantité de changement dans la variable dépendante pour un changement unitaire dans la variable indépendante.

#### Calcul de l'équation de la ligne de régression

Pour trouver l'ordonnée à l'origine du modèle, nous prolongeons la ligne de régression suffisamment loin jusqu'à ce qu'elle intersecte l'axe des y à x = 0. C'est notre ordonnée à l'origine et elle est d'environ -2,5. Le nombre ne fait peut-être pas vraiment sens pour l'ensemble de données sur lequel nous travaillons, mais l'intention est de montrer uniquement le calcul de l'ordonnée à l'origine.

![Image](https://cdn-media-1.freecodecamp.org/images/Qr8R9PGFVxf8VnwyQrmaVCpU0PqnAeW3FH9i)
_Calcul de l'ordonnée à l'origine_

Le coefficient pour ce modèle sera simplement la pente de la ligne de régression et peut être calculé en obtenant le changement dans l'admission sur le changement des scores GRE.

![Image](https://cdn-media-1.freecodecamp.org/images/r8Xzo0fzjJ4HeM-cHz66kST-aW-gTdcqde05)
_Calcul de la pente_

Dans l'exemple ci-dessus, le coefficient serait simplement

> m = (y2-y1) / (x2-x1)

Et dans ce cas, il serait proche de 0,01.

La formule y = m*x + b nous aide à calculer l'équation mathématique de notre ligne de régression. En substituant les valeurs de l'ordonnée à l'origine et de la pente que nous avons obtenues en prolongeant la ligne de régression, nous pouvons formuler l'équation -

> y = 0.01x — 2.48

-2.48 est une valeur d'ordonnée à l'origine plus précise que j'ai obtenue à partir du tableau de régression comme montré plus tard dans cet article.

Cette équation nous permet de prévoir et de prédire la chance d'admission d'un étudiant lorsque son score GRE est connu.

Maintenant que nous avons les bases, passons à la lecture et à l'interprétation d'un tableau de régression.

### Lire un tableau de régression

Le tableau de régression peut être grossièrement divisé en **trois composants** —

* **Analyse de la variance (ANOVA)** : fournit l'analyse de la variance dans le modèle, comme le suggère le nom.
* **statistiques de régression** : fournissent des informations numériques sur la variation et la manière dont le modèle explique la variation pour les données/observations données.
* **sortie résiduelle** : fournit la valeur prédite par le modèle et la différence entre la valeur observée réelle de la variable dépendante et sa valeur prédite par le modèle de régression pour chaque point de données.

### **Analyse de la variance (ANOVA)**

![Image](https://cdn-media-1.freecodecamp.org/images/qcL1FHAqajHQ3fk2Qnp2wMjSNDzWAf5vMNYP)
_Tableau ANOVA_

#### Degrés de liberté (df)

**df de régression** est le nombre de variables indépendantes dans notre modèle de régression. Puisque nous ne considérons que les scores GRE dans cet exemple, il est de 1.

**df résiduel** est le nombre total d'observations (lignes) de l'ensemble de données soustrait par le nombre de variables étant estimées. Dans cet exemple, le coefficient de score GRE et la constante sont estimés.

df résiduel = 500 — 2 = 498

**df total** — est la somme des degrés de liberté de régression et résiduels, qui est égale à la taille de l'ensemble de données moins 1.

#### **Somme des carrés (SS)**

![Image](https://cdn-media-1.freecodecamp.org/images/9E4FVD77xkpB9bZ2Npwa-Y7jwhlEH6-qzDlh)
_Ligne de régression avec la moyenne de l'ensemble de données en rouge._

**SS de régression** est la variation totale de la variable dépendante qui est expliquée par le modèle de régression. C'est la somme du carré de la différence entre la valeur prédite et la moyenne de la valeur de tous les points de données.

> ∑ (ŷ — ȳ)²

D'après le tableau ANOVA, le SS de régression est de 6,5 et le SS total est de 9,9, ce qui signifie que le modèle de régression explique environ 6,5/9,9 (environ 65%) de toute la variabilité dans l'ensemble de données.

**SS résiduel** — est la variation totale de la variable dépendante qui reste inexpliquée par le modèle de régression. Il est également appelé **Somme des carrés des erreurs** et est la somme du carré de la différence entre les valeurs réelles et prédites de tous les points de données.

> ∑ (y — ŷ)²

D'après le tableau ANOVA, le SS résiduel est d'environ 3,4. En général, plus l'erreur est petite, mieux le modèle de régression explique la variation dans l'ensemble de données et donc nous voudrions généralement minimiser cette erreur.

**SS total** — est la somme des SS de régression et résiduels ou de la variation des chances d'admission si les scores GRE ne sont **PAS** pris en compte.

**Erreurs quadratiques moyennes (MS)** — sont la moyenne de la somme des carrés ou la somme des carrés divisée par les degrés de liberté pour la régression et les résidus.

> MS de régression = ∑ (ŷ — ȳ)²/df de régression

> MS résiduel = ∑ (y — ŷ)²/df résiduel

**F** — est utilisé pour tester l'hypothèse que la pente de la variable indépendante est nulle. Mathématiquement, il peut également être calculé comme

> F = MS de régression / MS résiduel

Cela est autrement calculé en comparant la statistique F à une distribution F avec les df de régression en degrés du numérateur et les df résiduels en degrés du dénominateur.

**Signification F** — n'est rien d'autre que la valeur p pour l'hypothèse nulle que le coefficient de la variable indépendante est nul et, comme pour toute valeur p, une faible valeur p indique qu'une relation significative existe entre les variables dépendantes et indépendantes.

![Image](https://cdn-media-1.freecodecamp.org/images/QeNjs4oji3peiiodEnLof0wx4NSJlu5imm9C)

**Erreur standard** — fournit l'écart-type estimé de la distribution des coefficients. C'est la quantité par laquelle le coefficient varie selon les différents cas. Un coefficient beaucoup plus grand que son erreur standard implique une probabilité que le coefficient ne soit pas 0.

**t-Stat** — est la statistique t ou la valeur t du test et sa valeur est égale au coefficient divisé par l'erreur standard.

> t-Stat = Coefficients/Erreur standard

Encore une fois, plus le coefficient est grand par rapport à l'erreur standard, plus le t-Stat est grand et plus la probabilité que le coefficient soit éloigné de 0 est élevée.

**p-value** — La statistique t est comparée à la distribution t pour déterminer la p-value. Nous considérons généralement uniquement la p-value de la variable indépendante qui fournit la probabilité d'obtenir un échantillon aussi proche de celui utilisé pour dériver l'équation de régression et vérifier si la pente de la ligne de régression est réellement nulle ou si le coefficient est proche du coefficient obtenu.

Une p-value inférieure à 0,05 indique une confiance de 95% que la pente de la ligne de régression n'est pas nulle et donc qu'il existe une relation linéaire significative entre les variables dépendantes et indépendantes.

Une p-value supérieure à 0,05 indique que la pente de la ligne de régression peut être nulle et qu'il n'y a pas suffisamment de preuves au niveau de confiance de 95% qu'une relation linéaire significative existe entre les variables dépendantes et indépendantes.

Puisque la p-value du score GRE de la variable indépendante est très proche de 0, nous pouvons être extrêmement confiants qu'il existe une relation linéaire significative entre les scores GRE et la chance d'admission.

**Inférieur et Supérieur 95%** — Puisque nous utilisons principalement un échantillon de données pour estimer la ligne de régression et ses coefficients, ils sont principalement une approximation des vrais coefficients et, à leur tour, de la vraie ligne de régression. Les limites inférieure et supérieure à 95% donnent l'intervalle de confiance à 95% des limites inférieure et supérieure pour chaque coefficient.

Puisque l'intervalle de confiance à 95% pour les scores GRE est de 0,009 et 0,01, les limites ne contiennent pas zéro et donc, nous pouvons être confiants à 95% qu'il existe une relation linéaire significative entre les scores GRE et la chance d'admission.

Veuillez noter qu'un niveau de confiance de 95% est largement utilisé, mais un niveau autre que 95% est possible et peut être configuré lors de l'analyse de régression.

### **Statistiques de régression**

![Image](https://cdn-media-1.freecodecamp.org/images/7zaL2AUSPsdw2T8imw5bAqr6kCOy3nKOeHGk)
_Tableau des statistiques de régression_

**R² (R carré)** — représente la puissance d'un modèle. Il montre la quantité de variation dans la variable dépendante que la variable indépendante explique et se situe toujours entre les valeurs 0 et 1. À mesure que le R² augmente, plus de variation dans les données est expliquée par le modèle et mieux le modèle devient pour la prédiction. Un R² faible indiquerait que le modèle ne s'adapte pas bien aux données et qu'une variable indépendante n'explique pas bien la variation dans la variable dépendante.

> R² = Somme des carrés de régression / Somme totale des carrés

Cependant, le R carré _ne peut pas_ déterminer si les estimations des coefficients et les prédictions sont biaisées, c'est pourquoi vous devez évaluer les graphiques résiduels, qui sont discutés plus tard dans cet article.

Le R carré n'indique pas non plus si un modèle de régression est adéquat. Vous pouvez avoir une valeur R carré faible pour un bon modèle, ou une valeur R carré élevée pour un modèle qui ne s'adapte pas aux données.

R², dans ce cas, est de 65 %, ce qui implique que les scores GRE peuvent expliquer 65 % de la variation dans la chance d'admission.

**R² ajusté** — est le R² multiplié par un facteur d'ajustement. Cela est utilisé lors de la comparaison de différents modèles de régression avec différentes variables indépendantes. Ce nombre est utile lors de la décision des bonnes variables indépendantes dans les modèles de régression multiple.

**R multiple** — est la racine carrée positive de R²

**Erreur standard** — est différente de l'erreur standard des coefficients. Il s'agit de l'écart-type estimé de l'erreur de l'équation de régression et est une bonne mesure de la précision de la ligne de régression. Il s'agit de la racine carrée des erreurs quadratiques moyennes résiduelles.

> Erreur standard = √(MS résiduel)

### **Sortie résiduelle**

Les résidus sont la différence entre la valeur réelle et la valeur prédite du modèle de régression et la sortie résiduelle est la valeur prédite de la variable dépendante par le modèle de régression et le résidu pour chaque point de données.

Et comme le suggère le nom, un graphique résiduel est un nuage de points entre le résidu et la variable indépendante, qui dans ce cas est le score GRE de chaque étudiant.

Un graphique résiduel est important pour détecter des choses comme **l'hétéroscédasticité**, la **non-linéarité** et les **valeurs aberrantes**. Le processus de détection de ces éléments n'est pas discuté dans le cadre de cet article, mais le fait que le graphique résiduel de notre exemple ait des données dispersées aléatoirement nous aide à établir le fait que la relation entre les variables de ce modèle est linéaire.

![Image](https://cdn-media-1.freecodecamp.org/images/svhwHtrkIYoNwy323YB8jPS-OxeWmvmpPAyH)
_Graphique résiduel_

### **Intention**

L'intention de cet article n'est pas de construire un modèle de régression fonctionnel, mais de fournir un guide de toutes les variables de régression et de leur importance lorsque cela est nécessaire avec un ensemble de données d'exemple dans un tableau de régression.

Bien que cet article fournisse une explication avec une régression linéaire à une seule variable comme exemple, veuillez noter que certaines de ces variables pourraient avoir plus d'importance dans les cas de régression à plusieurs variables ou dans d'autres situations.

### **Références**

* [Ensemble de données sur les admissions en cycle supérieur](https://www.kaggle.com/mohansacharya/graduate-admissions)
* [10 choses à savoir sur la lecture d'un tableau de régression](https://egap.org/methods-guides/10-things-know-about-reading-regression-table)
* [Un rappel sur l'analyse de régression](https://hbr.org/2015/11/a-refresher-on-regression-analysis)