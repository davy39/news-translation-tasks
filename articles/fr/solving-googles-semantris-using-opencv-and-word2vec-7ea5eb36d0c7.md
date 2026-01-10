---
title: Comment résoudre le jeu Semantris de Google en utilisant OpenCV et Word2Vec
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-24T22:30:58.000Z'
originalURL: https://freecodecamp.org/news/solving-googles-semantris-using-opencv-and-word2vec-7ea5eb36d0c7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FYMv5pI8NInQAp1jQK6EIg.jpeg
tags:
- name: Computer Vision
  slug: computer-vision
- name: Data Science
  slug: data-science
- name: nlp
  slug: nlp
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment résoudre le jeu Semantris de Google en utilisant OpenCV et Word2Vec
seo_desc: 'By Pravendra Singh

  Writing a program to play Google Semantris



  Automation is good, so long as you know exactly where to put the machine. — Eliyahu
  Goldratt

  Semantris is a set of word association games by Google that use semantic search
  to predict a ...'
---

Par Pravendra Singh

#### Écrire un programme pour jouer à Google Semantris

![Image](https://cdn-media-1.freecodecamp.org/images/1*FYMv5pI8NInQAp1jQK6EIg.jpeg)

> L'automatisation est bonne, tant que vous savez exactement où placer la machine. — Eliyahu Goldratt

> [Semantris](https://research.google.com/semantris/) est un ensemble de jeux d'association de mots par Google qui utilisent la recherche sémantique pour prédire un mot pertinent dans le jeu en fonction de l'entrée du joueur.

Il y a 2 modes disponibles dans le jeu.

**ARCADE**

Le mode Arcade nécessite que le joueur trouve des mots associés à certains mots. Vous devez penser et entrer aussi vite que possible avant qu'une liste croissante de mots ne remplisse votre écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ASVWg8hkhtBHdtdpJMiqLQ.gif)
_Mode ARCADE de Semantris_

**BLOCKS**

Blocks est un mode de jeu basé sur des tours. Vous pouvez prendre votre temps pour trouver différents types d'indices et voir lesquels le jeu comprend le mieux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-CEfzr_8hsgBC3dGNBSFhQ.gif)
_Mode BLOCKS de Semantris_

Après avoir joué pendant un certain temps, j'ai réalisé que les deux modes de jeu utilisent [la reconnaissance de motifs comme principal mécanisme de jeu](http://www.peachpit.com/articles/article.aspx?p=98123&seqNum=2). C'est alors que j'ai commencé à me demander si cela pouvait être automatisé.

### Il s'avère que c'est possible

Semantris-Solver utilise la procédure suivante pour jouer au jeu :

* **Capturer l'état actuel du jeu en utilisant des techniques de vision par ordinateur**
* **Identifier le mot à entrer pour une récompense plus élevée/un jeu plus long**
* **Trouver le mot associé en utilisant des plongements de mots**

Dans les sections suivantes, nous allons plonger dans le fonctionnement de Semantris-Solver pour les deux modes de jeu.

### ARCADE

Un joueur humain utilisera les mouvements suivants pour jouer au mode arcade :

* Trouver un ou plusieurs mots mis en évidence dans le jeu
* Obtenir ces mots dans la zone mise en évidence en entrant le mot associé pour eux
* Continuer à faire cela avant de manquer d'espace sur votre écran pour de nouveaux mots

> _De plus, il y a trois types de couleurs de thème en mode arcade._

![Image](https://cdn-media-1.freecodecamp.org/images/1*FYMv5pI8NInQAp1jQK6EIg.jpeg)
_Couleurs de thème du mode ARCADE de Semantris_

Vous réaliserez que la couleur du thème ne joue aucun rôle ici — le mécanisme de jeu restera le même si nous changeons la couleur du thème. Ce qui change, c'est la définition du mot mis en évidence.

> _Un mot est **mis en évidence** s'il a une forme de pointeur à gauche de lui, (▶ **Ship**) dans ce cas._

#### Conversion de l'espace colorimétrique

Le mode ARCADE de Semantris-Solver commence par capturer une capture d'écran de l'écran de l'ordinateur portable et la convertir en une image en niveaux de gris, indépendamment de la couleur réelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gP7jPgkVTBZz21TG5yu-7w.png)
_Mode ARCADE de Semantris (niveaux de gris)_

#### Correspondance de modèle

Notre prochaine étape sera de trouver le mot mis en évidence dans l'image capturée. OpenCV fournit une méthode appelée [Template Matching](https://docs.opencv.org/3.3.0/d4/dc6/tutorial_py_template_matching.html) pour rechercher et trouver l'emplacement d'une image modèle dans une image plus grande.

Nous utiliserons une version recadrée de la forme du pointeur (▶) comme image modèle, pour trouver son emplacement dans l'écran capturé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zEAmRMZ4gbh392Yq_rlZpQ.png)
_Sélection du mot mis en évidence dans le mode ARCADE de Semantris_

#### Reconnaissance optique de caractères (OCR)

![Image](https://cdn-media-1.freecodecamp.org/images/1*DzR7dHo936cLxjeCdPNqRw.png)
_Image du mot mis en évidence_

En fonction de l'emplacement du pointeur, une section est recadrée juste à côté de celui-ci, avec le mot mis en évidence.

L'image recadrée est convertie en texte en utilisant [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) ; dans ce cas, cela nous donnera **Ship**.

> En cas de plus d'un mot mis en évidence, ils sont entrés l'un après l'autre pour garder le jeu en mouvement.

#### Sélection du mot associé (en utilisant les plongements de mots)

[Word2Vec pré-entraîné sur le corpus Google News](https://github.com/mmihaltz/word2vec-GoogleNews-vectors) est utilisé comme modèle de plongement de mots pour trouver les mots [les plus similaires](https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.Word2Vec.most_similar) (associés) pour un mot donné.

Dans ce cas, il retournera « **vessel** » à entrer comme mot associé pour « **ship** » (_après avoir supprimé les mots morphologiquement similaires_).

> _Le programme entrera ce mot associé et capturera l'écran de jeu mis à jour pour continuer._

### BLOCKS

Dans ce mode, il y a des blocs de mots avec quatre couleurs possibles pour un thème donné. Les blocs de mots peuvent ou non contenir un mot.

Entrer le mot associé pour un bloc de mots supprimera les blocs de même couleur connectés à celui-ci, comme le bon vieux **Tetris**.

Un joueur humain utilisera les mouvements suivants pour jouer au mode arcade :

* Entrer le mot associé pour un bloc de mots, connecté avec le plus de blocs de mots de même couleur (si possible)
* Continuer à faire cela avant de manquer d'espace sur votre écran pour de nouveaux mots

![Image](https://cdn-media-1.freecodecamp.org/images/1*3zS9PmEJFX47g2q4hfdDhg.png)
Écran capturé du mode BLOCKS de Semantris

Vous réaliserez que la couleur d'un bloc de mots joue un rôle significatif cette fois. Vous devrez entrer le mot associé pour un bloc de mots connecté avec plus de blocs de même couleur pour marquer plus de points.

> _En plus de cela, il y a trois types de couleurs de thème en mode blocs._

![Image](https://cdn-media-1.freecodecamp.org/images/1*jHXOeWmDiepucJyO9eP-OQ.jpeg)
_Couleurs de thème du mode BLOCKS de Semantris_

#### Génération de la palette de couleurs

Cette fois, nous ne pouvons pas convertir l'image capturée en sa version en niveaux de gris. Nous devons connaître les attributs de couleur pour pouvoir distinguer entre différents blocs de mots.

L'exécution du **clustering K-means** sur les pixels de l'écran capturé nous donnera toutes les couleurs proéminentes de l'image après avoir exclu les couleurs de fond telles que le blanc (couleur du texte), le noir (couleur de fond) et le gris (saisie de texte).

![Image](https://cdn-media-1.freecodecamp.org/images/1*I4GFZLlX2n1wLWM0UJgw4Q.png)
_Palette de couleurs de thème du mode BLOCKS de Semantris_

#### Détection de contour

Maintenant que nous avons toutes les quatre couleurs du thème actuel, nous devons savoir quel bloc de mots choisir pour obtenir le maximum de points.

En d'autres termes, si nous calculons la surface de chaque groupe de blocs de mots connectés (_blocs de mots de la même couleur connectés les uns aux autres_) et sélectionnons celui avec la surface maximale, nous obtiendrons le groupe de blocs de mots connectés souhaité.

> [_Contour_](https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html) _est une courbe reliant tous les points continus le long d'une frontière, ayant la même couleur ou intensité._

Un groupe de blocs de mots peut être considéré comme un contour de cette couleur ; s'il est connecté à plus de blocs de la même couleur, la surface du contour sera la somme des blocs de mots connectés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*POkYHfLEMRfRwMVKV0KnVQ.png)
_Mode BLOCKS de Semantris avec le contour de surface maximale mis en évidence_

Les contours sont calculés (en utilisant la fonction [findCountours](https://docs.opencv.org/3.3.1/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a) d'OpenCV) pour toutes les couleurs de blocs de mots séparément et celui avec la surface maximale est sélectionné.

Nous pouvons sélectionner le contour de surface maximale en effectuant une opération bitwise-and entre l'écran capturé et le masque de contour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S5XyET4u8aBTd64IU5m-aw.png)
_Contour de surface maximale_

#### Détection de mot (en utilisant Tesseract et Word2Vec)

L'image du contour est convertie en texte en utilisant [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) ; dans ce cas, cela nous donnera **Garden**.

Similaire au mode arcade, nous utiliserons Word2Vec pour trouver le mot le plus similaire, qui sera **Flower beds** cette fois.

### Améliorations

![Image](https://cdn-media-1.freecodecamp.org/images/1*tIgIoMSbvcmKj2yTXDuk1g.png)
_Contour avec OCR défaillant_

Dans certains scénarios, le processus OCR actuel ne reconnaît pas correctement le mot.

Par exemple, il retournerait « **Eloctrlclty** » pour ce contour au lieu de « **Electricity** ».

Étant donné que c'est une suggestion de mot invalide, le modèle Word2Vec ne retournera aucun mot similaire pour celui-ci. Dans ce cas, le mot suggéré lui-même est entré comme mot associé, juste pour garder le jeu en mouvement.

> Un modèle de correction orthographique peut aider ici, corrigeant **Eloctrlclty** en **Electricity**.

> _J'ai créé un [problème](https://github.com/pravj/semantris-solver/issues/7) sur le dépôt GitHub pour cela, n'hésitez pas à contribuer si vous le souhaitez. ?_

### Code source

#### [Semantris-Solver](https://github.com/pravj/semantris-solver) (GitHub)

Il est implémenté comme un outil CLI qui vous permet de basculer entre les modes de jeu. Vous pouvez consulter les **cahiers IPython** implémentant les deux modes.

* [Mode ARCADE](https://github.com/pravj/semantris-solver/blob/master/notebooks/Semantris%20Arcade%20Mode.ipynb)
* [Mode BLOCKS](https://github.com/pravj/semantris-solver/blob/master/notebooks/Semantris%20Block%20Mode.ipynb)

#### Dépendances

Il n'aurait pas été possible de construire Semantris-Solver sans les outils logiciels suivants.

* OpenCV
* Word2Vec (gensim)
* pyautogui (prise de la capture d'écran et entrée des mots associés)
* Tesseract (OCR)

J'espère que vous avez aimé mon histoire de hack de week-end. N'hésitez pas à fournir vos commentaires.

Suivez-moi sur Twitter [Pravendra Singh](https://www.freecodecamp.org/news/solving-googles-semantris-using-opencv-and-word2vec-7ea5eb36d0c7/undefined) ou consultez mon site personnel [hackpravj.com](https://hackpravj.com).