---
title: Flexbox vs Grid en CSS – Lequel utiliser ?
subtitle: ''
author: Mabel Obadoni
co_authors: []
series: null
date: '2024-02-16T11:02:00.000Z'
originalURL: https://freecodecamp.org/news/flexbox-vs-grid-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pankaj-patel-6JVlSdgMacE-unsplash.jpg
tags:
- name: css flex
  slug: css-flex
- name: CSS Grid
  slug: css-grid
- name: layout
  slug: layout
seo_title: Flexbox vs Grid en CSS – Lequel utiliser ?
seo_desc: 'Have you ever had issues with replicating a particular user interface from
  a Figma design? Do you find it difficult displaying elements in different sections
  of your browser screen?

  A major cause of rift between user interface (UI) designers and fron...'
---

Avez-vous déjà eu des problèmes à reproduire une interface utilisateur particulière à partir d'un design Figma ? Trouvez-vous difficile d'afficher des éléments dans différentes sections de l'écran de votre navigateur ?

Une cause majeure de désaccord entre les concepteurs d'interface utilisateur (UI) et les développeurs frontend est le problème de devoir traduire un design UI génial en fonctionnalités réelles.

Presque tous les développeurs frontend ont rencontré des craintes similaires à certains moments de leur parcours de codage. Cet article vous aidera à comprendre comment les affichages CSS fonctionnent en ce qui concerne le flexbox et la mise en page en grille.

## Table des matières :

* [Origine du CSS](#heading-origin-of-css)
* [Structure de base du CSS](#heading-basic-structure-of-css)
* [Mise en page CSS (Flex et Grid)](#heading-css-layout-flex-and-grid)
* [Comment utiliser la mise en page Flex en CSS](#heading-how-to-use-the-flex-layout-in-css)
* [Comment utiliser la mise en page Grid en CSS](#heading-how-to-use-the-grid-layout-in-css)
* [Similitudes entre Flex et Grid](#heading-similarities-between-flex-and-grid)
* [Quand utiliser Flex](#heading-when-to-use-flex)
* [Quand utiliser Grid](#heading-when-to-use-grid)
* [Conclusion](#heading-conclusion)

## Origine du CSS

Les premiers sites web n'étaient pas seulement statiques, mais aussi basés sur du texte. Pendant les premières années du World Wide Web, les pages web étaient écrites dans des langages de balisage tels que XHTML et similaires.

Voici à quoi ils ressemblaient :

![Image](https://lh5.googleusercontent.com/Wx0Au7mNXzu7gi_nFVSJ1T-CRXYiBBcaXBMEEWYJ_GNvm7e3vsN1UTdkPXmGGuKicXmdl60JjMEm2mJQT4vUmJc4oAxTfMiwV-MoK8tMIwhNcQZo58ziVlONzkRc9CrkAMYfz2GaxQykIOacs9-vAv4)
_[https://www.history.com/news/the-worlds-first-web-site](https://www.history.com/news/the-worlds-first-web-site)_

Avec les avancées dans diverses technologies, les passionnés de technologie étaient intéressés à rendre les sites web plus agréables en ajoutant du design. Cela a conduit au développement des Cascading Style Sheets, mieux connues sous le nom de CSS.

Bien que le CSS ait subi plusieurs évolutions, il est responsable de l'esthétique des sites web. Imaginez un site web ou une application logicielle avec juste du texte et aucun design.

Hé ! Cet article ne parle pas d'histoire, alors passons directement au sujet.

En tant que développeur logiciel spécialisé dans les applications côté client (souvent appelé développement frontend), vous serez d'accord avec moi que le CSS est ce compagnon adorable qui semble simple mais sophistiqué.

Le CSS peut vous tenir éveillé la nuit en essayant de comprendre pourquoi votre page ne s'aligne pas comme prévu ou pourquoi le contenu de votre page est coupé sur certains écrans et non réactif.

L'une des raisons pour lesquelles les débutants en développement logiciel abandonnent souvent le frontend pour se spécialiser dans le backend est le "stress" qui accompagne l'écriture du code CSS, surtout avec le CSS vanilla où vous devez saisir manuellement pratiquement chaque règle de style. Cela est dû au fait que le CSS nécessite un certain niveau de calcul mélangé avec une attention aux détails les plus minimes.

Un aspect majeur du CSS qui crée souvent de la confusion est la mise en page CSS – écrire la règle CSS pour la mise en page peut être un peu déroutant pour un débutant.

Dans les sections qui suivent, nous nous concentrerons sur :

* Les similitudes entre les affichages flex et grid.
* Quand utiliser flex ou grid.

## **Structure de base du CSS**

Avant de discuter en détail de l'affichage CSS, examinons brièvement la structure CSS.

Pour commencer, la structure CSS est un modèle de boîte. Cela signifie que chaque page web est traitée comme une boîte, similaire à avoir une pizza dans une boîte à pizza.

La boîte à pizza ici représente la page du navigateur tandis que la pizza représente le contenu de votre site web ou application, qui peut être du texte, des graphiques ou des multimédias.

![Image](https://lh7-us.googleusercontent.com/EJbG9BG5EZ7CU9sBtOQJVBWo7cbc8nwG8pjYxqQ6kgll7lTN7wH8XQYy35zZFgbMhiQhZLy3BqnEA-brNtaS8NBcB-XPLMzk0zBvAr-frniqSogpYmDWs7qqgiloBjXuNK2mWZIIymLfpfa880m1HjU)
_Une boîte de pizza_

![Image](https://lh7-us.googleusercontent.com/lxBLqGMf-ZhMcZwKDpCPRHmax_Y3ZBst69uUF0pmZBZdmuRnh_woEy48OzbqXBwGAy5I38HAZ5SFW5fU-3LwsJArJNX3KBk0E2K6d2nH7SoXZKGHwJpQlLtxZrlbxwIWnjO9kLSfyi-wHf7u1WWAy4A)
_Modèle de boîte CSS_

## **Mise en page CSS (Flex et Grid)**

Maintenant que vous savez comment le CSS structure le contenu de chaque page web ou d'application, un aspect vital du CSS que vous devriez maîtriser est la mise en page, qui est le cœur de cet article.

En architecture, chaque bâtiment a sa structure. La structure d'un bâtiment commercial peut différer de celle d'un bâtiment résidentiel. Il en va de même pour le développement frontend.

Le but de l'application joue un rôle important dans la sélection d'une mise en page. Par exemple, un site web de commerce électronique opterait pour une mise en page en grille pour un arrangement et un affichage appropriés de leurs produits.

La mise en page de chaque site web ou application détermine comment le contenu de la page sera organisé : soit en piles de lignes et de colonnes, soit simplement en colonnes sur diverses tailles d'écran.

Il est également important de noter que vous pouvez utiliser plus d'un affichage sur une page web particulière. Cela signifie que vous pouvez afficher une `div` particulière comme une grille et une autre `div` comme un flexbox. Tout dépend du contenu de chaque `div` et de la manière dont vous souhaitez qu'ils apparaissent.

Il existe deux façons de concevoir la mise en page du contenu d'une page web en CSS :

* Flex
* Grid

### Comment utiliser la mise en page Flex en CSS

La mise en page flex utilise une méthode d'organisation du contenu web en lignes (axe principal) ou en colonnes (axe perpendiculaire). Cela implique qu'il s'agit d'une mise en page unidimensionnelle. L'axe principal peut se déplacer dans l'ordre inverse, de droite à gauche.

La direction du flex peut être définie sur :

* Ligne
* Ligne-inverse
* Colonne
* Colonne-inverse

L'utilisation du flexbox ne divise pas l'écran ou le contenu en parties égales. Il est important de noter que le flexbox ne considère pas la division du contenu en colonnes égales sur la ligne ou l'empilement des colonnes dans le même alignement. Au contraire, il étend ou réduit le contenu pour contenir l'espace disponible à l'écran.

Ci-dessous se trouve un diagramme d'un affichage flex utilisant des lignes :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Flex-1.png)
_Une représentation graphique d'un affichage défini sur flex_

#### Comment définir l'affichage sur Flex

Pour créer une mise en page flex :

* Donnez à l'élément parent une règle de style d'affichage flex
* Donnez aux éléments enfants une certaine marge et un certain remplissage pour une meilleure apparence
* Spécifiez la direction du flex si nécessaire

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title> Définir l'affichage sur Flex</title>
<style>
    .fl{
        display: flex;
        flex-wrap: wrap;
    }
    .ex {
        flex-direction:row;
        flex: 1 0 100px; 
        margin: 5px; 
        padding: 10px; 
        background-color: #0000FF; 
        border: 1px solid #ffff; /* J'ai ajouté une bordure tout autour de chaque colonne pour une meilleure visibilité et séparation des colonnes */
    }
</style>
</head>
<body>

<div class="fl">
    <div class="ex">Contenu 1</div>
    <div class="ex">Contenu 2</div>
    <div class="ex">Contenu 3</div>
    <div class="ex">Contenu 4</div>
    <div class="ex">Contenu 5</div>
</div>

</body>
</html>
```

Le code ci-dessus style le corps en sélectionnant le conteneur parent et en lui attribuant une mise en page de `flex`. Ensuite, la direction des éléments enfants est définie sur `row` en utilisant la règle `flex-direction`.

### Comment utiliser la mise en page Grid en CSS

La mise en page grid, en revanche, divise une page web en 12 colonnes égales. Ces colonnes peuvent être divisées en les lignes et colonnes souhaitées.

L'écran entier (100 %) divisé en 12 donne environ 3,33 % par colonne. L'écran peut également être stylé en utilisant le nombre de colonnes en multiples de 2. C'est-à-dire : 2, 4, 6, 8, 10 et 12, chaque nombre spécifiant le nombre de colonnes ou la largeur que l'élément est censé occuper.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-120.png)

#### Comment définir l'affichage sur Grid

* Définissez l'affichage de l'élément parent sur grid
* Spécifiez la dimension (c'est-à-dire les lignes ou les colonnes) de la grille en utilisant la propriété grid-template
* Donnez un certain espacement (marge, remplissage, row-gap, etc.) à l'élément enfant pour que la grille soit plus visible

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Définir l'affichage sur Grid</title>
<style>
    .fl{
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* Cela affichera les éléments enfants en trois colonnes égales de largeur égale */
        gap: 5px; /* Pour définir un écart entre les éléments de la grille */
    }
    .gr {
        padding: 20px; 
        background-color: #0000FF; 
        border: 1px solid #ffff; /* J'ai ajouté une bordure tout autour de chaque colonne pour une meilleure visibilité et séparation des colonnes */
    }
</style>
</head>
<body>

<div class="gr">
    <div class="gr">Contenu 1</div>
    <div class="gr">Contenu 2</div>
    <div class="gr">Contenu 3</div>
    <div class="gr">Contenu 4</div>
    <div class="gr">Contenu 5</div>
</div>

</body>
</html>
```

## Similitudes entre Flex et Grid

* **Ce sont tous deux des mises en page réactives** : Peu importe la mise en page que vous décidez d'utiliser pour votre application, à condition de styliser correctement les propriétés, les deux types de mise en page sont réactifs aux différentes tailles d'écran.

* **Définir d'abord la mise en page de l'élément parent** : Dans le stylage d'une mise en page flex ou grid, l'élément parent est celui qui est stylisé avec la mise en page exacte en question.

## **Quand utiliser Flex**

Le flex CSS est populaire pour sa capacité d'ordre (row-reverse, column-reverse), qui permet au développeur de réorganiser le contenu sans avoir à changer manuellement le contenu HTML. Il existe plusieurs cas d'utilisation du flex CSS, tels que :

* **Construire des mises en page unidimensionnelles** : Pour les pages web ou sections avec une seule mise en page, il est préférable d'utiliser flex car il aide à l'arrangement correct du contenu.
* **Alignement et distribution du contenu** : Grâce à justify-content, `align-self` et autres propriétés, l'alignement et la distribution du contenu sont facilités avec flex.
* **Afficher des colonnes de hauteurs égales** : En utilisant la propriété `align-items` et en la définissant sur une valeur de `stretch`, c'est-à-dire : `align-items:stretch`, le flex CSS garantit que les colonnes dans un flexbox sont de hauteurs égales.
Cela implique que si une colonne est plus haute, les autres colonnes seront étirées pour atteindre la colonne la plus haute. Vous pouvez utiliser le flex CSS pour afficher vos colonnes de hauteur égale indépendamment de la hauteur du contenu.

## **Quand utiliser Grid**

La mise en page grid est la plus couramment utilisée par les développeurs frontend car elle permet de placer des éléments sur différentes sections de la page du navigateur tout en maintenant un alignement correct. Vous pouvez utiliser la mise en page grid lorsque :

* **Construire un design réactif** : Souvent, les interfaces utilisateur sont développées pour être adaptables à n'importe quel écran sur lequel elles sont affichées. Dans de tels cas, la mise en page grid est votre meilleur choix car elle offre de la flexibilité et un redimensionnement de l'élément.
* **Contrôle de l'espace blanc** : Contrairement à l'affichage flex qui laisse un espace blanc à l'extrême, le grid CSS contrôle l'espace blanc en distribuant les éléments de manière égale le long de la ligne et également en fonction de l'espace de colonne alloué.
* **Cohérence dans la mise en page du design** : Le grid CSS offre un motif cohérent dans la structure d'une page web. Cet arrangement des éléments facilite l'édition future de la page.

## **Conclusion**

Un conseil qui s'avère très utile lors du stylage d'une page est de choisir quel mode d'affichage employer.

Une fois que cela est réglé, les différentes sections de la page peuvent suivre en gardant à l'esprit ce que contient l'ensemble du corps.

Bien que ce ne soit pas un conseil, les pratiques récentes ont vu les développeurs utiliser grid plus souvent que flexbox. Dans tous les cas, assurez-vous de ne pas mélanger le code des affichages respectifs pour éviter les erreurs.

Bon codage !