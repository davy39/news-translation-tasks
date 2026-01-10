---
title: Comment utiliser l'aperçu CSS dans les outils de développement Chrome
subtitle: ''
author: Cess
co_authors: []
series: null
date: '2022-02-07T14:52:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-overview-in-chrome-developer-tools
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/HTML-Best-Practices
seo_title: Comment utiliser l'aperçu CSS dans les outils de développement Chrome
---

How-to-Build-a-Better-HTML-Based-Website-1.png
tags:
- name: Google Chrome
  slug: chrome
- name: CSS
  slug: css
- name: Developer Tools
  slug: developer-tools
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Si vous êtes un développeur web, vous appréciez probablement un site web bien conçu et attrayant. \nEt vous pouvez voir un schéma de couleurs ou une police sur un site spécifique que vous souhaitez incorporer dans votre blog ou votre application web. Mais vous aurez besoin d'une extension de navigateur pour ..."
---

Si vous êtes un développeur web, vous appréciez probablement un site web bien conçu et attrayant. 

Et vous pouvez voir un schéma de couleurs ou une police sur un site spécifique que vous souhaitez incorporer dans votre blog ou votre application web. Mais vous aurez besoin d'une extension de navigateur pour voir le schéma de couleurs du site et d'autres fonctionnalités CSS.

La fonction **CSS overview** dans les outils de développement Chrome vous permet de voir ces propriétés CSS.

Dans cet article, nous allons passer en revue comment utiliser la fonction **CSS overview** dans les outils de développement Chrome. Nous allons également apprendre comment utiliser **CSS overview** pour obtenir les couleurs et autres propriétés CSS que vous souhaitez utiliser pour créer une page web.

Commençons. 💡

## Qu'est-ce que le panneau d'aperçu CSS ?

Le **panneau d'aperçu CSS** est l'une des nouvelles fonctionnalités des outils de développement Chrome. Il sert d'outil de prévisualisation qui vous permet de voir les différentes propriétés CSS utilisées pour créer une page web.

Il affiche des propriétés CSS telles que :

* Les couleurs utilisées sur une page web.
* La hauteur de ligne de chaque élément utilisé sur une page web.
* La taille de police de chaque élément utilisé sur une page web.
* Les familles de polices de chaque élément sur une page web.
* Les poids de police de chaque élément utilisé sur une page web.

## Qu'est-ce que les outils de développement Chrome ?

**Les outils de développement Chrome** sont également connus sous le nom de Chrome Dev Tools.

**Les outils de développement Chrome** sont une suite d'outils pour les développeurs web qui sont préinstallés dans le navigateur Chrome. 

Consultez cet article pour en savoir plus sur les [outils de développement Chrome](https://developer.chrome.com/docs/devtools/).

Voici quelques-uns des avantages de l'utilisation des **outils de développement Chrome** :

* Ils vous permettent de créer de meilleurs sites web en moins de temps.

* Ils vous permettent d'apporter des modifications à votre code, de le tester et de l'inspecter.

* Les outils de développement Chrome donnent aux développeurs plus de contrôle sur leurs applications web et leurs navigateurs. 

* Ils vous permettent d'évaluer les performances générales d'un site web. 

## Comment accéder aux outils de développement Chrome dans votre navigateur

Vous pouvez accéder aux outils de développement Chrome de trois manières différentes :

1. **Menu de Chrome** :

* Cliquez sur les trois points verticaux situés dans le coin supérieur droit de votre navigateur Chrome. Cela fera apparaître un menu déroulant avec `plus d'outils` en bas de l'écran. 

* Cliquez sur plus d'outils.

* Cliquez sur outils de développement.

![Untitled-design](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design.png)

2. **Inspecter** : 

* Faites un clic droit sur le navigateur Chrome.

* Cliquez sur inspecter.

![Untitled-design--1--2](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design--1--2.png)

3. **Raccourcis** : 

* Pour Windows - `CTRL` + `Shift` + `I` OU `F12`. 

* Pour Mac - `CMD` + `Shift` + `I`. 

Une fois que vous cliquez sur les touches de raccourci, les outils de développement s'ouvrent.

Lorsque vous appuyez sur `CTRL` + `Shift` + `I`, il affiche le dernier panneau que vous avez ouvert par défaut. Il montre l'élément, la console, le réseau ou le panneau de performance, entre autres.

`CTRL` + `Shift` + `C` ouvre le **panneau d'élément** en premier par défaut.

## Comment utiliser l'aperçu CSS dans les outils de développement Chrome

Les étapes ci-dessous vous guideront à travers l'utilisation de la fonction d'aperçu CSS pour obtenir les propriétés CSS utilisées sur une page web.


## Étape 1 - Ouvrir les outils de développement Chrome

Nous avons déjà couvert les différentes méthodes pour accéder aux outils de développement Chrome. Vous devriez maintenant être familier avec elles.

Pour rappel, vous pouvez ouvrir les outils de développement Chrome en appuyant sur `Ctrl` + `Shift` + `I` sur Windows et Linux. Utilisez `CMD` + `Option` + `I` sur Mac.

## Étape 2 - Cliquer sur Plus d'outils


Cliquez sur les trois points verticaux situés en haut à droite des outils de développement Chrome.

Sélectionnez "Plus d'outils" dans le menu déroulant. 

Vous découvrirez une variété d'options lorsque vous cliquez sur "Plus d'outils". Parmi les différentes options, sélectionnez la fonction **CSS overview**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design--1--3.png)

## Étape 3 - Cliquer sur Capturer l'aperçu

Lorsque vous cliquez sur **CSS Overview**, vous verrez une liste de ses fonctions.

Fonctions telles que :
* Capturer un aperçu du CSS de votre page.

* Identifier les améliorations potentielles du CSS.

* Localiser les éléments affectés dans le panneau d'éléments.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design--2-.png)

Cliquez sur le **bouton Capturer l'aperçu**.

Un menu avec cinq sections apparaît après avoir cliqué sur le bouton Capturer l'aperçu.

Les cinq sections sont :
* Résumé de l'aperçu
* Couleurs
* Informations sur les polices
* Déclarations inutilisées
* Requêtes média

Passons en revue chacune des cinq sections une par une pour voir comment elles fonctionnent.

## Résumé de l'aperçu CSS

Le **Résumé de l'aperçu** contient une liste des éléments CSS utilisés pour construire la page web.

Le Résumé de l'aperçu affiche un résumé du CSS sur votre site web, tel que :
* Le nombre d'éléments utilisés sur la page web.
* Les différents types de sélecteurs utilisés pour créer la page web.
* Le nombre d'éléments de style en ligne utilisés sur la page web.
* Le nombre de feuilles de style externes utilisées sur la page web.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/overview-summary.png)
_Une illustration du résumé de l'aperçu._

L'exemple ci-dessus montre les différents éléments CSS utilisés pour construire la page web.

## Couleurs

Le panneau des couleurs affiche toutes les couleurs utilisées pour créer la page web. Il dispose d'une palette de couleurs pour l'arrière-plan, le texte, le remplissage et les bordures. Il met également en évidence les problèmes de texte à faible contraste sur la page web.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/color-ya-boy.png)
_Une illustration du panneau des couleurs._

L'image ci-dessus vous montre les différentes couleurs utilisées pour créer la page web.

La beauté du panneau des couleurs est que chaque couleur est cliquable. Si vous cliquez sur une couleur particulière dans le panneau des couleurs, une liste d'éléments qui utilisent cette couleur apparaît. Lorsque vous cliquez sur chaque élément, il vous emmène au panneau d'éléments pour inspection.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design--6-.png)

J'ai cliqué sur la couleur `#49FCD4` dans l'image ci-dessus, et cela a fait apparaître une liste d'éléments avec cette couleur.

Vous pouvez également survoler un élément dans les listes d'éléments affichés. Lorsque vous déplacez votre curseur sur l'élément, il met en surbrillance l'élément sur la page web.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design--7-.png)

Lorsque je survole la souris sur l'élément `header` dans l'image ci-dessus, il met en surbrillance l'en-tête sur la page web.

Juste une petite note : le survol fait référence au déplacement de votre curseur sur quelque chose. Cela signifie placer un curseur sur du texte, une image ou d'autres objets à l'écran sans cliquer dessus.

## Informations sur les polices

Le panneau d'informations sur les polices affiche les types de caractères utilisés dans le développement du site web. Il vous montre la `taille de police`, la `hauteur de ligne`, le `poids de police` et les `familles de polices` utilisés pour créer le site web. Si vous cliquez sur les **occurrences**, vous verrez une liste des éléments affectés.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/use-this-one-for-header.png)
_Une illustration du panneau d'informations sur les polices._

L'image ci-dessus vous montre les différents types de caractères utilisés pour créer la page web. 

## Déclarations inutilisées

Vous pouvez trouver des styles CSS qui n'affectent pas la page web en utilisant les **déclarations inutilisées**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/declare-my-boy.png)
_Une illustration du panneau des déclarations inutilisées._

L'image ci-dessus montre le nombre de déclarations inutilisées sur la page web. L'alignement vertical appliqué à l'élément qui n'est pas en ligne ou une cellule de tableau n'affectera pas la page.

Vous pouvez également cliquer sur les **occurrences** pour voir une liste des éléments affectés, comme le **panneau d'informations sur les polices** et le **panneau des couleurs**.

## Requêtes média

Le panneau des requêtes média affiche une liste de toutes les requêtes média utilisées pour créer la page web. Vous pourrez examiner les différentes largeurs et résolutions d'écran utilisées pour créer la page web.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/media-query-my-boy.png)
_Une illustration du panneau des requêtes média._

L'exemple ci-dessus affiche le nombre de requêtes média utilisées pour créer la page web. Il liste les résolutions d'écran utilisées par ordre d'occurrence, du plus haut au plus bas. Si vous cliquez sur les **occurrences**, vous verrez une liste des éléments affectés.

## Conclusion

Lorsque vous évaluez les attributs CSS sur une page web, l'outil **CSS overview** se révèle très utile. Il permet aux développeurs front-end et aux designers d'inspecter les propriétés CSS sur une page web.

Merci d'avoir lu 💡. Si vous souhaitez discuter ou avez des questions, n'hésitez pas à me contacter à tout moment sur Twitter : [@cessss_](https://twitter.com/Cessss_) et LinkedIn : [Success](https://www.linkedin.com/in/success-eriamiantoe/).

De plus, suivez mon blog pour lire d'autres articles [@cesscode](https://cesscode.hashnode.dev).

Bon codage ! 💡