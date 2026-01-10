---
title: Comment utiliser les fichiers HAR pour analyser les performances au fil du
  temps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/using-har-files-to-analyze-performance-over-time
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/william-daigneault-oWrZoAVOBS0-unsplash.jpg
tags:
- name: browser
  slug: browser
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: Comment utiliser les fichiers HAR pour analyser les performances au fil
  du temps
seo_desc: 'By Leonardo Faria

  When I consider the performance of a website, several things come to mind. I think
  about looking at the requests of a page, understanding what resources are being
  loaded, and how long these resources take to be available to users.


  ...'
---

Par Leonardo Faria

Lorsque je considère la performance d'un site web, plusieurs choses me viennent à l'esprit. Je pense à examiner les requêtes d'une page, à comprendre quelles ressources sont chargées et combien de temps ces ressources mettent à être disponibles pour les utilisateurs.

![Onglet Réseau de Chrome](https://leonardofaria.net/wp-content/uploads/2020/06/chrome-network.jpg)

L'onglet réseau vous donnera un tableau contenant tous les actifs chargés sur la page. Il vous montrera également des informations pertinentes sur l'origine de ces actifs (domaine, code de statut HTTP, taille), qui a initié la requête et l'ordre dans lequel ils ont été chargés dans une représentation en cascade.

Vous pouvez ajouter plus d'informations à ce tableau en cliquant avec le bouton droit sur l'un des en-têtes du tableau et en choisissant d'autres colonnes.

Les colonnes taille, temps et cascade seront cruciales pour comprendre la performance d'une page. La valeur de taille présentera la taille gzippée de la ressource (lorsque cela est applicable), tandis que la colonne temps montre la durée totale depuis le début de la requête jusqu'à la réception du dernier octet dans la réponse.

Enfin, mais non des moindres, la colonne cascade démontre quand l'actif est chargé ainsi que les autres requêtes.

Les améliorations de performance sont perceptibles par les changements dans votre code/environnement. Alors, comment garder une trace de ce qui est analysé par l'onglet Réseau ? En exportant la page au format HAR.

## Qu'est-ce qu'un fichier HAR ?

Un fichier HAR (abréviation de HTTP Archive) est un fichier JSON contenant toutes les informations sur les interactions d'un navigateur avec une page. Il contiendra le document HTML et ses fichiers JS et CSS respectifs.

Avec ce contenu, un fichier HAR contiendra également toutes les informations d'en-tête et les métadonnées du navigateur (c'est-à-dire le temps de chaque requête).

Il est important de mentionner ici que les cookies et les données de formulaire seront également enregistrés dans le fichier, alors faites attention à ne pas inclure d'informations sensibles (détails personnels, mots de passe, numéros de carte de crédit) lors de l'audit des pages.

De plus, vous devriez auditer les pages dans des fenêtres privées, ce qui évite les extensions du navigateur. Il est important d'éviter les extensions d'un navigateur car elles peuvent modifier les temps de chargement d'une page.

## Génération de fichiers HAR

### Google Chrome

* Fermez toutes les fenêtres de navigation privée dans Google Chrome.
* Ouvrez une nouvelle fenêtre de navigation privée dans Google Chrome.
* Allez dans Affichage > Développeur > Outils de développement.
* Dans le panneau Outils de développement, choisissez l'onglet Réseau.
* Cochez les cases Conserver le journal et Désactiver le cache pour enregistrer toutes les interactions.
* Actualisez la page.
* Cliquez sur Exporter HAR (icône de flèche vers le bas) pour exporter le fichier HAR.
* Enregistrez le fichier HAR.

### Firefox

* Fermez toutes les fenêtres privées dans Firefox.
* Ouvrez une nouvelle fenêtre privée dans Firefox.
* Allez dans Outils > Développeur > Réseau ou ctrl-shift-E.
* Actualisez la page.
* Dans l'icône d'engrenage (côté supérieur droit de la page), choisissez Enregistrer tout en tant que Har.
* Enregistrez le fichier HAR.

![Onglet Réseau de Firefox](https://leonardofaria.net/wp-content/uploads/2020/06/firefox-network.jpg)

### Safari

* Assurez-vous que la case Afficher le menu Développeur dans la barre de menus est cochée sous Safari > Préférences > Avancé.
* Choisissez Fichier > Nouvelle fenêtre privée.
* Visitez la page web où le problème se produit.
* Choisissez Développeur > Afficher l'inspecteur web. La fenêtre de l'inspecteur web apparaît.
* Actualisez la page.
* Cliquez sur Exporter dans le coin supérieur droit du panneau.
* Enregistrez le fichier HAR.

![Onglet Réseau de Safari](https://leonardofaria.net/wp-content/uploads/2020/06/safari-network.jpg)

## Lecture des fichiers HAR

Une fois que vous avez un fichier HAR, vous pouvez essayer quelques visionneuses HAR en ligne. Ma préférée est celle créée par [Jan Odavarko](http://www.softwareishard.com/har/viewer/).

![Visionneuse HAR](https://leonardofaria.net/wp-content/uploads/2020/06/har-viewer.jpg)

Ce que j'aime particulièrement dans cette visionneuse, c'est le fait que vous pouvez avoir plusieurs fichiers ouverts en même temps, ce qui facilite leur comparaison.

## Utilisation des fichiers HAR pour analyser la performance d'une page

Les fichiers HAR peuvent être utiles pour collecter des informations sur les actifs d'une page. Puisque vous avez des informations détaillées sur leur contenu, vous pouvez comparer ce qui s'est amélioré (ou dans certains cas, ne s'est pas amélioré) après le lancement d'une nouvelle fonctionnalité ou la finalisation d'une refonte, par exemple.

Lors de mon flux de travail, j'aime garder une trace des valeurs finales de taille/temps de quelques pages du produit sur lequel je travaille.

## Plus d'informations

* [Mesurer les temps de chargement des ressources](https://developers.google.com/web/tools/chrome-devtools/network/resource-loading#view-network-timing-details-for-a-specific-resource)
* [Code source de la visionneuse HAR](https://github.com/janodvarko/harviewer)

Également publié sur [mon blog](https://bit.ly/2zbBPud). Si vous aimez ce contenu, suivez-moi sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria). Photo de couverture par [William Daigneault/Unsplash](https://unsplash.com/photos/oWrZoAVOBS0)