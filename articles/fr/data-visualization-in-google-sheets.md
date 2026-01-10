---
title: Visualisation de données dans Google Sheets pour les débutants
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-03-16T20:55:12.000Z'
originalURL: https://freecodecamp.org/news/data-visualization-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/FCC-Data-Visualization-in-Google-Sheets
seo_title: Visualisation de données dans Google Sheets pour les débutants
---

Bar-and-Pie-Charts.jpg
tags:
- name: guide pour débutants
  slug: guide-pour-debutants
- name: visualisation de données
  slug: visualisation-de-donnees
- name: google sheets
  slug: google-sheets
seo_title: null
seo_desc: "Les feuilles de calcul sont la ressource originale pour visualiser les données avec des graphiques... à moins que vous ne comptiez les tableaux noirs, je suppose. Les feuilles de calcul sont conçues pour traiter des tonnes de données. Et en utilisant quelques outils intégrés simples, vous pouvez tirer des informations précieuses de..."
---

Les feuilles de calcul sont la ressource originale (OG) pour visualiser les données avec des graphiques... à moins que vous ne comptiez les tableaux noirs, je suppose.

Les feuilles de calcul sont conçues pour traiter des tonnes de données. Et en utilisant quelques outils intégrés simples, vous pouvez tirer des informations précieuses de gros blocs de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/og.gif)
_gif de l'illustration \"OG\"_

Lorsque vous traitez de petits ensembles de données, vous pouvez souvent trouver des réponses et des idées d'un seul coup d'œil. Mais lorsque vos feuilles de calcul commencent à atteindre des centaines et des milliers de lignes, les graphiques peuvent aider à condenser tous ces chiffres en informations exploitables... surtout si vous faites une présentation à des personnes qui ne sont pas à l'aise avec les chiffres !

## Aperçu vidéo

En parlant de visuels :

* [Voici un lien](https://docs.google.com/spreadsheets/d/1kJ5vDDtb8B7SDQDBK-WxgK-Tc2Dk9KlF29qxjjxz65Y/edit#gid=370701475) vers la feuille de calcul de démonstration avec toutes nos données et nos graphiques.
* Et voici la vidéo explicative de tout ce qui est couvert ci-dessous :

%[https://youtu.be/QYc1gUWnhS4]

## Comment obtenir les données

Kaggle est une ressource merveilleuse pour trouver des ensembles de données intéressants. Nous utilisons cet ensemble de données sur les ventes de jeux vidéo. Pour l'importer dans une feuille Google Sheets, il suffit de créer une nouvelle feuille de calcul en tapant `sheets.new` dans la barre d'adresse de notre navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-140.png)
_capture d'écran de la barre d'adresse web_

Ensuite, sélectionnez `Fichier, Importer` dans le menu.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-141.png)
_capture d'écran du menu fichier dans google sheets_

Vous pouvez maintenant télécharger le fichier .csv que vous avez récupéré sur Kaggle.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-142.png)
_capture d'écran des options d'importation dans google sheets_

Cela vous donnera plusieurs options d'importation. Si vous suivez ce tutoriel en utilisant une feuille de calcul entièrement vierge, sélectionnez simplement `Remplacer la feuille de calcul` et tout sera importé automatiquement.

Si les données sont bien nettoyées, et les ensembles de données Kaggle le sont généralement, vous pouvez laisser le séparateur sur `Détecter automatiquement`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-143.png)
_capture d'écran des options d'importation de fichier_

Cela nous donnera une superbe feuille de calcul de plus de 16 000 lignes remplie de données sur les jeux vidéo. 😁

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-145.png)
_capture d'écran du jeu de données dans la feuille de calcul_

## Comment insérer des graphiques

À partir de là, nous devons sélectionner `Insertion - Graphique` dans la barre d'outils.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-146.png)
_capture d'écran d'insertion de graphique dans google sheets_

Nous serons confrontés à un graphique vide au milieu de l'écran et à un éditeur de graphique dans la barre latérale droite.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-147.png)
_capture d'écran de l'éditeur de graphique_

Assurons-nous maintenant que nous référençons la bonne plage de données. Google Sheets est assez intelligent, et si vous cliquez sur la petite icône de graphique à droite du formulaire de plage de données, il suggérera des plages à utiliser. Dans notre cas, la plage dont nous avons besoin est suggérée : `A1:K16600`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/selectrange.png)

Nous allons chercher les _ventes par genre_ (sales by genre), donc sélectionnons ensuite `Genre` pour notre axe X :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-148.png)
_capture d'écran des options de graphique_

Parfois, Google Sheets ne sera pas aussi intelligent. S'il y a une tonne de séries répertoriées et un graphique bizarre, vous pouvez simplement supprimer toutes les séries et ajouter manuellement ce dont vous avez besoin :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-149.png)
_capture d'écran des séries de graphiques_

Cliquez maintenant sur le bouton `Agrégat` pour regrouper toutes les données de vente pour chaque genre, et sélectionnez `NA-Sales` comme Série pour afficher les ventes en millions de dollars sur l'axe Y.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-150.png)
_capture d'écran des options de série de graphique_

Et voilà ! Nous avons un graphique à barres standard. Mais nous pouvons faire mieux. En haut à droite de notre éditeur de graphique, nous pouvons `Personnaliser` le graphique davantage en changeant l'apparence, la police, le quadrillage et les titres.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-151.png)
_capture d'écran de l'éditeur de graphique_

## Comment personnaliser le graphique

Depuis l'onglet de personnalisation, nous avons beaucoup d'options. Nous pouvons styliser notre graphique en changeant la couleur de fond et la police. Nous pouvons le mettre en 3D, et nous pouvons choisir de maximiser ou non le graphique dans la fenêtre.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-152.png)
_capture d'écran du style de graphique_

Nous pouvons ensuite ajouter des titres de graphique, des sous-titres et des titres d'axes, et également modifier la couleur et les polices.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-153.png)
_capture d'écran des titres de graphique_

Ensuite, nous pouvons éditer individuellement chaque `Série`. Dans notre exemple, nous n'utilisons qu'une seule série, mais s'il y en avait plus, vous pourriez modifier le style de chacune indépendamment.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-154.png)
_capture d'écran des options de personnalisation de série_

Si vous avez une légende, vous pouvez modifier ces options dans la fenêtre déroulante suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-155.png)

Ensuite, il y a des options de personnalisation pour les axes horizontal et vertical.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-156.png)
_capture d'écran des options d'axes_

Et le dernier bloc d'options de personnalisation concerne le quadrillage et les graduations. Ceux-ci peuvent être activés ou désactivés, et nous pouvons changer la couleur et la fréquence des lignes de grille et des graduations.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-157.png)

Une fois terminé, nous avons maintenant un graphique plus stylisé :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-158.png)
_capture d'écran du graphique à colonnes dans Google Sheets_

Si nous souhaitons déplacer ce graphique, nous pouvons le faire glisser n'importe où dans la feuille de calcul actuelle. Ou, nous pouvons le mettre sur sa propre feuille dédiée en cliquant sur les trois points en haut à droite et en sélectionnant `Déplacer vers une propre feuille`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-159.png)

## Comment publier le graphique

Voici un bonus supplémentaire : vous pouvez réellement publier le graphique (ou toute la feuille de calcul) sur le Web. Sélectionnez l'option `Publier le graphique` dans le menu déroulant du graphique illustré ci-dessus, ou sélectionnez `Fichier, Partager, Publier sur le Web` :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-16-at-10.46.55-AM.png)
_capture d'écran des options de publication sur le Web_

De là, vous pourrez sélectionner ce que vous souhaitez publier et comment vous voulez que ce soit affiché. Pour cet exemple, nous sélectionnerons le graphique `Sales by Platform` pour qu'il soit partagé en tant que graphique interactif.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-16-at-10.49.29-AM.png)
_capture d'écran des options de publication dans google sheets_

Cela générera un lien partageable vers le graphique. Le chargement peut prendre quelques secondes, mais une fois terminé, vous aurez un joli graphique interactif à partager facilement. Lorsque vous survolez les segments, il affichera le pourcentage de ventes de la part du gâteau.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-16-at-10.52.14-AM.png)
_capture d'écran d'un graphique publié_

[Voici le lien vers le graphique que nous venons de créer.](https://docs.google.com/spreadsheets/d/e/2PACX-1vRZ-uidgV1M_YVX6qvEi5RSGddmUvRRl3a7ehHfGx9VX3JI7dP-NVX2teVlwBbhmg7ChXsp37Ss0zDt/pubchart?oid=1851187878&format=interactive) 

## Conclusion

Merci de m'avoir lu ! J'espère que vous avez appris quelque chose dans ce tutoriel pour débutants sur la visualisation de données dans Google Sheets.

Vous pouvez vraiment accomplir beaucoup de choses en utilisant les graphiques intégrés de base disponibles dans Google Sheets ainsi que dans Microsoft Excel. Les graphiques restent un moyen extrêmement utile d'interpréter de grands ensembles de données.

N'hésitez pas à consulter ma [chaîne YouTube ici](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) et ma [page LinkedIn ici](https://www.linkedin.com/in/eamonncottrell/).

Bonne continuation !