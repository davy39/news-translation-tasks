---
title: Comment fonctionnent les réseaux de neurones – Expliqué à l'aide de l'équation
  de la ligne droite y = ax + b
subtitle: ''
author: Samyukta Hegde
co_authors: []
series: null
date: '2026-01-08T00:02:44.243Z'
originalURL: https://freecodecamp.org/news/neural-networks-explained-using-y-ax-b
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767800625537/5bb99a58-d247-4933-b60b-fd2c14651542.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Data Science
  slug: data-science
seo_title: Comment fonctionnent les réseaux de neurones – Expliqué à l'aide de l'équation
  de la ligne droite y = ax + b
seo_desc: 'Did you know that every data scientist who builds a complex neural network
  starts with a fundamental question, “How does the output change when the input changes?“

  A straight line equation y = ax+b answers it in the simplest way possible. y can
  incre...'
---

Saviez-vous que chaque scientifique des données qui construit un réseau neuronal complexe commence par une question fondamentale, « Comment la sortie change-t-elle lorsque l'entrée change ? »

Une équation de ligne droite `y = ax+b` y répond de la manière la plus simple possible. `y` peut augmenter, diminuer ou rester le même lorsque `x` change.

D'autre part, un réseau neuronal profond tente d'y répondre de manière flexible. Ce n'est possible que grâce à plusieurs couches de calculs de lignes droites empilées les unes sur les autres, ainsi qu'à des ajustements non linéaires pour aider le réseau à s'adapter et à produire le résultat souhaité.

Puisqu'une ligne droite est l'essence des réseaux neuronaux, je pense qu'il est temps d'essayer de comprendre les détails subtils de `y = ax+b`, que j'appelle l'**équation magique**. Nous passerons également en revue les bases de la régression et de la classification linéaires, ce qui devrait vous aider à comprendre la progression d'une simple ligne droite à un réseau neuronal profond complexe.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [y=ax+b](#heading-yaxb)
    
* [Régression linéaire](#heading-regression-lineaire)
    
* [Classification linéaire](#heading-classification-lineaire)
    
* [Comparaison](#heading-comparaison)
    
* [Ajouts clés pour aider à construire des réseaux neuronaux profonds](#heading-ajouts-cles-pour-aider-a-construire-des-reseaux-neuronaux-profonds)
    
    * [Couches](#heading-couches)
        
    * [Non-linéarité](#heading-non-linearite)
        
* [Modélisation d'un réseau neuronal profond](#heading-modelisation-dun-reseau-neuronal-profond)
    
    * [Étape #1 - Définir clairement le problème](#heading-etape-1-definir-clairement-le-probleme)
        
    * [Étape #2 - Définir la couche d'entrée](#heading-etape-2-definir-la-couche-dentree)
        
    * [Étape #3 - Définir la première couche cachée](#heading-etape-3-definir-la-premiere-couche-cachee)
        
* [Réflexions finales](#heading-reflexions-finales)
    

## Prérequis

* Une compréhension de base de l'algèbre linéaire, en particulier `y=ax+b`.
    
* Une idée générale de la régression et de la classification linéaires.
    
* Familiarité avec le concept des réseaux neuronaux profonds.
    

## y=ax+b

Une ligne droite signifie simplement que la sortie change de manière régulière lorsque l'entrée change. Il n'y a pas de surprises (c'est-à-dire pas de non-linéarité). Analysons cela correctement.

```plaintext
y => Variable de sortie
x => Variable d'entrée
a => Montant par lequel y change lorsque x change (pente)
b => Valeur de y lorsque x est 0 (ordonnée à l'origine)
```

Nous pouvons prendre un exemple et le modéliser sous la même forme pour mieux le comprendre.

Mme Poly est une enseignante en mathématiques qui souhaite élaborer un plan d'études pour ses élèves afin qu'ils excellent à un examen final à venir. Pour simplifier, elle crée une règle de base en utilisant un seul facteur : le nombre d'heures étudiées par semaine. Cela a un impact direct sur les notes obtenues par un élève.

Avant de commencer, elle fait certaines hypothèses :

* Chaque élève est capable d'obtenir au moins 30 sans étudier.
    
* Pour chaque heure qu'un élève étudie, 3 points supplémentaires peuvent être obtenus.
    

Elle arrive ensuite à l'équation suivante basée sur ses idées : `y = 3x+30`

```plaintext
y => Notes obtenues.
x => Nombre d'heures étudiées.
a=3 => Augmentation des notes pour chaque heure étudiée
b=30 => Notes minimales
```

![Graphique de y=3x+30](https://cdn.hashnode.com/res/hashnode/image/upload/v1764650083131/997f2a53-78ac-4b6f-a0c1-b995fb515075.png align="center")

Dans le graphique ci-dessus, elle trace les points en fonction des résultats de l'équation. Comme prévu, c'est une ligne droite. Si elle a besoin des notes obtenues pour `9` heures d'étude, elle peut les obtenir en substituant simplement `x=9` dans `y=3x+30`. Notez que les données (`x` et `y`) sont basées sur son intuition et ne sont pas réelles.

Mais Mme Poly veut guider ses élèves sur la manière de se préparer à l'examen final en fonction de données réelles. Elle organise donc un quiz surprise et le note. Afin d'élaborer un plan d'études, elle interroge ses élèves et collecte des informations sur le nombre d'heures qu'ils étudient les mathématiques par semaine. Elle crée un tableau avec deux colonnes : le nombre d'heures étudiées (`x`) par semaine et les notes obtenues (`y`). Elle essaie sa vieille formule `y=3x+30`, mais cela ne semble pas fonctionner. Ainsi, elle n'a aucune équation sensée décrivant la relation entre `x` et `y`.

Supposons qu'un nouvel élève qui n'a passé aucun examen (aucun `y` disponible) rejoigne la classe le lendemain, et que Mme Poly ne connaisse que le nombre d'heures dédiées par semaine (`x`). Comment peut-elle répondre à la question suivante ?

*Si le nouvel élève étudie pendant un certain nombre d'heures (*`x`*), quelles peuvent être les notes obtenues (*`y`*) à l'examen ?*

C'est impossible à moins qu'il n'y ait une équation définissant les données d'échantillon. Sa tâche est donc d'en trouver une qui s'adapte aux points donnés. Ce processus est appelé ajustement de courbe ou régression.

## Régression linéaire

L'idée centrale de la régression linéaire est de trouver une ligne droite qui capture la tendance des données existantes pour faciliter les prédictions pour de nouvelles données d'entrée. Maintenant, plongeons directement dans l'exemple pour mieux comprendre le concept.

Mme Poly est déterminée à trouver une solution. Elle trace les données collectées sur un graphique pour avoir une meilleure image.

![Données d'entrée](https://cdn.hashnode.com/res/hashnode/image/upload/v1764651274954/0aa2dfc2-d846-40e6-872d-e7d5abe598a8.png align="center")

Elle n'a absolument aucune idée de la manière dont `x` et `y` sont liés. Elle doit donc trouver une formule, par essai et erreur, qui s'adapte approximativement aux points. Elle doit commencer par une supposition intuitive, essayer de l'améliorer dans les étapes suivantes, puis arriver à la meilleure solution possible.

**Essai 1** : Mme Poly commence avec son équation de ligne droite précédente.

`y = 3x+30`

Elle substitue différentes valeurs de `x` et les trace à côté des données d'entrée collectées. De cette manière, elle peut avoir une image claire des différences entre son hypothèse et la réalité.

![Régression linéaire-Essai 1](https://cdn.hashnode.com/res/hashnode/image/upload/v1764651323645/a3e79765-99bc-42be-8836-82119d7fbf66.png align="center")

**Essai 2** : Elle observe que la ligne a besoin d'un peu plus de pente. Cela signifie simplement que, dans la réalité, plus de notes sont obtenues pour chaque heure supplémentaire d'étude. En la changeant de `3` à `4`, l'équation devient :

`y = 4x+30`

Le graphique suivant représente la nouvelle ligne à côté des données d'échantillon :

![Régression linéaire-Essai 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1764651379913/42a8fc61-7927-46de-aadf-b691544b9a1b.png align="center")

**Essai 3** : Cela semble mieux, mais elle pense qu'il est nécessaire de déplacer toute la ligne vers le haut. Cela signifie que des notes plus élevées sont obtenues même si un élève ne consacre aucun temps aux mathématiques dans une semaine. Elle décide de conserver la pente précédente mais change les notes de départ de `10`, arrivant ainsi à :

`y = 4x+40`

![Régression linéaire-Essai 3](https://cdn.hashnode.com/res/hashnode/image/upload/v1764651454435/5fea2d39-8254-48e6-be14-69c803982ec7.png align="center")

Cette ligne particulière couvre la plupart des points et peut être considérée comme la meilleure solution possible.

Maintenant, si elle souhaite déterminer les notes obtenues par le nouvel élève qui a étudié pendant `3,5` heures, elle insère la valeur dans la formule et calcule la réponse : `y = 4*(3,5)+40=54`

Nous avons vu comment Mme Poly est arrivée à une équation de ligne droite pour prédire la sortie pour une entrée inconnue. Maintenant, elle peut élaborer un plan d'études pour sa classe basé sur l'équation.

Ici, une expression est formulée pour déterminer le changement de sortie lorsque l'entrée change. Il semble que Mme Poly pense comme une scientifique des données. Elle a en fait modélisé un réseau neuronal très simple pour la régression. L'équation `y=4x+40` peut être considérée comme le seul neurone (unité de traitement) à l'intérieur. Elle a ajusté les paramètres `a` (poids) et `b` (biais) pour arriver à la formule finale qui couvre la plupart des points (minimisant ainsi la perte).

Voici une décomposition de l'équation `y = 4x+40` :

```plaintext
y => Notes obtenues.
x => Nombre d'heures étudiées.
a=4 => Augmentation des notes pour chaque heure étudiée
b=40 => Notes minimales
```

Actuellement, c'est un réseau neuronal rudimentaire qui n'a ni couche ni non-linéarité.

Maintenant, tournons notre attention vers un scénario complètement différent. Mme Poly, en tant qu'enseignante, veut s'assurer que tous ses élèves réussissent l'examen. En supposant, comme résultat final, qu'elle n'est pas intéressée par la prédiction des notes obtenues. Elle veut simplement savoir :

*Si un élève étudie pendant un certain nombre d'heures (*`x`*), l'élève réussira-t-il/échouera-t-il (y) l'examen ?*

Cela la conduit au processus de classification.

## Classification linéaire

Le processus de classification linéaire utilise une simple ligne droite pour diviser les données en catégories ou classes. La ligne agit comme une frontière de sorte que les classes se trouvent de chaque côté de celle-ci. Tout d'abord, Mme Poly définit la condition de frontière pour la réussite et l'échec.

*Si les notes obtenues >=50, réussite*

*Si les notes obtenues <50, échec*

Selon le tableau de données, `x=3` correspond à `y=52` (condition de frontière). Par conséquent, elle considère `x=3` comme la ligne de classification***.***

![Classification linéaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1764651531018/e669ed7b-1c86-4093-b7e5-feb06464ebfe.png align="center")

`x=3` semble bien séparer les points en catégories. Elle essaie de le confirmer en substituant une autre valeur. Ainsi, si un élève a étudié pendant `9` heures, le score se situerait du côté droit de `x=3`. Ils réussiraient donc selon l'équation de classification.

Encore une fois, elle est arrivée à une expression pour déterminer le changement de sortie lorsque l'entrée change. Mais ici, elle a modélisé un réseau neuronal de base pour la classification. L'équation x=3 est le seul neurone à l'intérieur. Il peut être considéré comme ayant deux parties comme expliqué ci-dessous.

1. **Partie Pré-Activation** : Cette portion du neurone calcule une valeur intermédiaire qui est utile pour un traitement ultérieur. Elle a déterminé les paramètres `a` (poids) et `b` (biais) pour arriver à la formule suivante : `z = x-3`
    
    ```plaintext
    z => Valeur intermédiaire.
    x => Nombre d'heures étudiées.
    a=1 => Influence du nombre d'heures étudiées sur les notes obtenues
    b=-3 => Nombre minimum d'heures à étudier pour réussir l'examen = 3
    ```
    
2. **Partie Activation** : Cette portion déclenche le neurone pour prendre des décisions basées sur une valeur seuil. L'équation suivante sépare les points en deux classes.
    
    ```plaintext
    y = 1 (Réussite) si z>=0
    y = 0 (Échec) si z<0
    ```
    

C'est un réseau neuronal très simple qui n'a ni couche ni non-linéarité, mais qui a des parties de pré-activation et d'activation à l'intérieur d'un neurone.

## Comparaison

Nous avons examiné les exemples de régression et de classification linéaires utilisés par Mme Poly. La **régression** aide à prédire une valeur tandis que la **classification** aide à la prise de décision. Dressons un petit tableau pour résumer les différences.

![Comparaison entre la régression linéaire et la classification](https://cdn.hashnode.com/res/hashnode/image/upload/v1764652317811/f4411011-fcd3-4a53-b116-a3c8a27c81d8.png align="center")

Après une observation attentive, nous remarquons que les deux répondent à la question de savoir comment le changement d'entrée affecte la sortie.

Mais à un niveau de complexité légèrement supérieur à celui d'une ligne droite. Parce que dans le cas de la régression et de la classification, nous essayons de déterminer les paramètres de l'équation par essai et erreur.

Ici, puisque les exigences sont simples, Mme Poly utilise simplement une ligne droite pour résoudre les deux problèmes. Une équation linéaire simple ne peut gérer qu'une seule tendance régulière. Mais dans la vie réelle, les problèmes à résoudre sont beaucoup plus difficiles et imprévisibles. Voici quelques exemples :

**Classification d'images** : Une étiquette de sortie est produite en fonction des images d'entrée.

**Traduction de texte** : Une phrase en anglais peut être donnée en entrée pour être traduite, par exemple, en espagnol.

**Chatbots** : Une invite textuelle est tapée par un utilisateur et une sortie significative et pertinente est générée.

Elle devrait probablement utiliser un réseau neuronal profond si les données et la tâche étaient complexes. Cela soulève une autre question : **Comment construit-on un réseau neuronal profond ?**

Nous allons l'explorer davantage en étendant le même exemple à une version plus réaliste.

## Ajouts clés pour aider à construire des réseaux neuronaux profonds

Dans les sections précédentes, nous avons noté que Mme Poly était intéressée par la prédiction des résultats d'examen d'un élève en utilisant un seul facteur : le nombre d'heures étudiées. Cependant, en pratique, ce facteur unique est-il suffisant pour déterminer les notes obtenues ou si l'élève réussit l'examen ?

Non. Ce n'est pas suffisant. Elle doit prendre en compte de nombreux aspects tels que :

* Nombre d'heures étudiées
    
* Nombre d'heures de sommeil/repos
    
* Épuisement dû à une étude excessive
    
* Niveau de difficulté des sujets en mathématiques
    
* Modèle de l'examen, et ainsi de suite.
    

Tous les éléments ci-dessus n'agissent pas indépendamment et n'ont pas non plus une relation linéaire simple avec les notes obtenues. Elle doit donc résoudre ce problème en empilant les facteurs contributeurs les uns au-dessus des autres en couches et en ajoutant également l'élément de non-linéarité. Examinons chacun d'eux en détail.

### Couches

L'épuisement conduit à un score plus bas, tandis qu'un bon sommeil augmente le score. Mais l'épuisement peut être réduit si l'élève est bien reposé. L'impact sur le score final lorsque ces deux facteurs interagissent doit donc être pris en compte. Cela n'est possible que lorsque le système le résout en couches. La première couche peut traiter la manière dont ils influencent indépendamment le score, la couche suivante peut explorer l'interaction entre eux.

### Non-linéarité

Si le nombre d'heures étudiées augmente, le score peut augmenter, mais lorsque l'épuisement surpasse l'effet des heures d'étude, le score diminue. L'effet combiné entraîne un graphique non linéaire. Il y a une hausse puis une baisse du score en fonction du nombre d'heures étudiées. Il est évident que la relation n'est pas aussi simple que celle d'une ligne droite. C'est là qu'il devient nécessaire d'ajouter de la non-linéarité dans les calculs. Cela aide le système à répondre différemment selon les conditions, permettant une flexibilité dans le traitement des données et des conditions du monde réel.

Ainsi, Mme Poly devrait étendre l'idée de la régression/classification linéaire en incluant des couches et de la non-linéarité pour construire un réseau neuronal entièrement fonctionnel afin d'aider à élaborer un plan d'études pratique.

## Modélisation d'un réseau neuronal profond

Mme Poly devrait commencer le travail de modélisation d'un réseau neuronal profond en suivant les étapes mentionnées ci-dessous :

### **Étape #1 - Définir clairement le problème**

Les facteurs suivants doivent être pris en compte avant qu'elle ne commence le processus de modélisation :

* Quelles sont les caractéristiques d'entrée ?
    
* Quelles sont les caractéristiques de sortie ?
    
* Quel type de problème est-ce (régression/classification) ?
    

### **Étape #2 - Définir la couche d'entrée**

Les caractéristiques d'entrée forment la première couche. Il n'y a pas de calcul à ce stade. Elles sont représentées comme suit :

```plaintext
x1: Nombre d'heures étudiées
x2: Nombre d'heures de sommeil/repos
x3: Épuisement dû à une étude excessive
x4: Niveau de difficulté des sujets en mathématiques
x5: Modèle de l'examen
```

### **Étape #3 - Définir la première couche cachée**

Cette étape se compose de deux parties :

**Appliquer une transformation linéaire** : L'apprentissage réel commence ici. Une équation de ligne droite est utilisée pour comprendre l'effet combiné des entrées. La formule générale est `z=Wx+b`.

```plaintext
z: Valeur intermédiaire ou pré-activation
W: Matrice de poids qui consiste en des valeurs correspondant à l'impact de
t chaque caractéristique d'entrée
x: Matrice constituée de caractéristiques d'entrée, [x1, x2, x3, x4, x5]
b: Biais qui représente les hypothèses initiales de l'enseignante (lorsque x=0)
```

Cela ressemble à une équation de régression/classification linéaire. Au début, `W` et `b` sont initialisés à des valeurs aléatoires. Ensuite, dans les étapes suivantes, ils sont ajustés comme cela a été fait dans les exemples précédents. Nous pouvons considérer les combinaisons suivantes en supposant que nous avons deux neurones dans cette couche :

**Neurone 1** : Il peut se concentrer sur les heures d'étude, l'épuisement et le repos, les autres caractéristiques contribuant de manière moins significative.

**Neurone 2** : Il peut mettre l'accent davantage sur le niveau de difficulté du sujet et le type d'examen par rapport aux autres entrées.

Il est important de noter que cette couche ne calcule pas les interactions entre les caractéristiques, mais seulement la manière dont différentes combinaisons linéaires fonctionnent ensemble mais indépendamment. Pour être plus clair, la manière dont elles contribuent indépendamment est additionnée. Nous ne savons pas comment une caractéristique d'entrée influence l'autre. Par exemple, nous savons que le sommeil augmente le score et que l'épuisement réduit le score, mais ce que nous ne savons pas à ce stade, c'est si le sommeil réduit l'épuisement, ce qui peut à son tour influencer le score final.

**Ajouter de la non-linéarité** : Cette étape, également appelée activation, aide à capturer les complexités dans différentes combinaisons des caractéristiques. Peu d'étude entraîne de mauvaises notes, et trop d'épuisement entraîne également de mauvaises notes. Cela signifie qu'il y a une courbe dans le graphique des scores qui ne peut pas être représentée par une équation linéaire. La fonction d'activation est appliquée à la valeur intermédiaire et peut être exprimée comme suit :

**a = g(z)**

```plaintext
a: Sortie d'activation
g: Fonction d'activation
z: Valeur intermédiaire ou pré-activation
```

Par exemple : `ReLU` est une fonction d'activation qui produit `z` uniquement si `z` est positif, sinon `0`.

**y = ReLU(z)=max(0,z)**

Nous pouvons voir qu'elle n'a pas de pente régulière et est une fonction d'activation non linéaire. Elle peut convenir à ce scénario car elle laisse la valeur passer à la couche suivante uniquement si l'effet combiné des caractéristiques est supérieur à 0. Le neurone 1 laissera sa sortie passer à la couche suivante uniquement si la valeur intermédiaire (`z`) résultant des heures d'étude, de l'épuisement et du repos est suffisamment grande pour influencer la décision finale, sinon elle est ignorée. Il existe plusieurs options pour les fonctions d'activation non linéaires parmi lesquelles on peut choisir.

1. **Empiler les couches les unes au-dessus des autres** : Cette étape aide à apprendre les interactions mutuelles entre les inférences apprises de la première couche cachée. Le réseau tente de comprendre les détails complexes des facteurs influents et de construire un système stable. C'est ici que les détails de savoir si le sommeil réduit l'épuisement sont déterminés. Chaque couche se compose de transformations linéaires et non linéaires appliquées à l'entrée, qui sont des valeurs obtenues de la couche précédente. De même, plusieurs couches peuvent être empilées les unes sur les autres en fonction des exigences. Dans cet exemple, pour la représentation, nous avons pris deux couches cachées avec deux neurones chacune. Le nombre de couches et de neurones peut varier en fonction des exigences.
    
2. **Définir les caractéristiques de sortie** : Cela semble être l'étape finale dans un réseau neuronal profond. Mme Poly peut décider ce qu'elle veut pour la sortie : prédire les notes obtenues par un élève ou prédire si l'élève réussit/échoue à l'examen. Si elle veut les notes finales obtenues, elle doit simplement appliquer une transformation linéaire dans le neurone de la couche finale pour produire la sortie. Si elle veut le statut de réussite/échec, elle doit appliquer à la fois des transformations linéaires et non linéaires pour obtenir les résultats souhaités.
    

Le diagramme ci-dessous montre une représentation abstraite du réseau neuronal profond.

![Représentation abstraite d'un réseau neuronal profond](https://cdn.hashnode.com/res/hashnode/image/upload/v1766153114888/1e513840-483a-43cf-b062-ce5af886a04e.png align="center")

Les prochaines étapes sont :

**Entraînement du modèle** : Le réseau est entraîné de la manière suivante : des poids et des biais aléatoires sont attribués aux parties de transformation linéaire du réseau. Ensuite, le réseau fait une prédiction qui est comparée au résultat attendu. S'il y a des écarts entre le résultat réel et le résultat prédit, des corrections sont apportées aux poids et aux biais (cette étape est similaire à ce qui a été fait dans la régression et la classification linéaires). Cela est répété jusqu'à ce que les résultats s'améliorent.

**Utilisation du modèle** : Après que le modèle a été entraîné, il est capable de produire des résultats pour de nouvelles valeurs d'entrée.

## **Réflexions finales**

Dans cet article, nous avons commencé par les bases d'une équation de ligne droite. Ensuite, nous avons progressivement navigué à travers des concepts légèrement plus élaborés comme la régression et la classification linéaires. Ils ont jeté les bases pour plonger dans les réseaux neuronaux profonds, apparemment mystérieux. Mais en fait, ils sont construits en empilant des couches de transformations linéaires et d'activations non linéaires, qui aident à comprendre des motifs sophistiqués du monde réel.

Malgré toutes les complexités et les couches, nous pouvons voir que la ligne droite reste la fondation sur laquelle les réseaux neuronaux sont construits. Comme nous l'avons vu précédemment, l'équation avec laquelle un réseau neuronal profond commence est notre *équation magique* : `y = ax+b`.