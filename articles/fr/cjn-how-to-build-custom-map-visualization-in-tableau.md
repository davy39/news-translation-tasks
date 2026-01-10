---
title: Comment créer une visualisation de carte personnalisée dans Tableau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-11T18:52:50.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-build-custom-map-visualization-in-tableau
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/NBA_injuries_Tableau.png
tags:
- name: data
  slug: data
- name: data visualization
  slug: data-visualization
- name: excel
  slug: excel
- name: tableu
  slug: tableu
seo_title: Comment créer une visualisation de carte personnalisée dans Tableau
seo_desc: 'By Clark Jason Ngo

  Sometime last year, I got fascinated with bubble charts when I saw a data visualization
  video, Han''s Rosling''s 200 Countries, 200 Years, 4 Minutes - The Joy of Stats
  from BBC.


  Data Visualization used as an effective communication ...'
---

Par Clark Jason Ngo

L'année dernière, je me suis passionné pour les graphiques à bulles après avoir vu une vidéo de visualisation de données, [Han's Rosling's 200 Countries, 200 Years, 4 Minutes - The Joy of Stats from BBC](https://www.youtube.com/watch?v=jbkSRLYSojo ).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-34.png)
_La visualisation de données utilisée comme un outil de communication efficace ! Génial !_

### Qu'est-ce qu'un graphique à bulles ?

> "Un graphique à bulles est un type de graphique qui affiche trois dimensions de données. Chaque entité avec son triplet de données associées est tracée sous forme de disque qui exprime deux des valeurs par l'emplacement xy du disque et la troisième par sa taille." [Wikipedia](https://en.wikipedia.org/wiki/Bubble_chart)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-12.png)
_Un exemple de graphique à bulles_

En janvier 2019, j'examinais Tableau Desktop, un logiciel de visualisation de données, et leurs tutoriels de base incluaient une carte thermique des États-Unis.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-13.png)

### Qu'est-ce qu'une carte thermique ?

> "Une carte thermique est une représentation graphique des données où les valeurs individuelles contenues dans une matrice sont représentées par des couleurs. "Carte thermique" est un terme plus récent, mais les matrices d'ombrage existent depuis plus d'un siècle."[Wikipedia](https://en.wikipedia.org/wiki/Heat_map)

En suivant le tutoriel Tableau, je me suis souvenu des graphiques à bulles et j'ai commencé à chercher une inspiration. J'ai cherché des silhouettes d'images sur Google et j'ai obtenu le résultat ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-14.png)

Cela m'a conduit à mon court essai de visualisation de données. J'ai cherché un ensemble de données et j'ai trouvé les blessures de la NBA de 2010 à 2018 sur [Kaggle](https://www.kaggle.com/ghopkins/nba-injuries-2010-2018). J'ai modifié l'ensemble de données pour le rendre simple à utiliser.

J'ai fini par abandonner l'utilisation de Tableau et créer ma propre visualisation de données dans Microsoft Powerpoint. Pourtant, mes amis étaient émerveillés et pensaient que j'avais utilisé un outil de visualisation de données.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image.png)
_Créé avec Microsoft Powerpoint_

En août 2019, je suis revenu à l'étude du tutoriel Tableau. Regardez simplement le résultat ci-dessous ! =)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-1.png)
_Créé avec Tableau_

## Comment ai-je fait cela ?

J'ai utilisé Excel, Tableau et un peu de créativité.

N'hésitez pas à suivre et à créer le même ensemble de données et la même visualisation.

**Étapes**

1. Créez un fichier Excel. La colonne B et la colonne C serviront de localisation sur l'axe X et l'axe Y d'un élément dans Tableau. Count représente le nombre de joueurs ayant eu une blessure particulière de 2010 à 2018.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-8.png)



2. Téléchargez Tableau Desktop [ici](https://www.tableau.com/).

3. Ouvrez l'application Tableau Desktop

4. Cliquez sur **Se connecter à un fichier** > **Microsoft Excel**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-2.png)

4. Faites glisser une feuille du volet de gauche vers le volet de droite

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-3.png)

5. En bas, cliquez sur la feuille.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-4.png)

6. Dans le menu, cliquez sur **Images de fond** > **Feuille**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-5.png)

7. Cliquez sur **Ajouter une image**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-6.png)

8. Parcourez une image et définissez X Field : Right à 500 et Y Field : Top à 500.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-7.png)



9. Dans Colonnes et Lignes, ajoutez **SUM(X)** et **SUM(Y)**, respectivement.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-9.png)

10. Pour les marques, ajoutez **SUM(COUNT)** dans Couleur, **SUM(Count)** dans Taille, et **Position** dans Étiquette.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-10.png)

Tableau générera alors cette visualisation pour vous :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-11.png)

L'un des super pouvoirs de la visualisation de données est de traiter les données et de les comprendre simplement en regardant l'image. Avec cette visualisation, je peux vous communiquer clairement et facilement que les blessures à la **cheville** et au **genou** sont les blessures sportives les plus courantes pour un joueur de la NBA, et que les **vertiges** et les blessures au **nez** sont les moins courants.

Et voilà ! J'espère que vous avez apprécié cette simple expérience =)