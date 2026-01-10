---
title: Apprendre Vuetify en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-12T16:38:26.000Z'
originalURL: https://freecodecamp.org/news/learn-vuetify-in-5-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-12-at-17.19.31--2-.png
tags:
- name: Scrimba
  slug: scrimba
- name: vue
  slug: vue
- name: Vuetify
  slug: vuetify
seo_title: Apprendre Vuetify en 5 minutes
seo_desc: 'By Leanne Rybintsev

  Welcome to a whistle-stop tour of Vuetify - a popular component library for Vue.js.
  It allows you to create attractive, accessible apps with 80 elements ready to use
  from the get-go, plus it gives you the option to customize eleme...'
---

Par Leanne Rybintsev

Bienvenue dans ce tour d'horizon express de Vuetify - une bibliothèque de composants populaire pour Vue.js. Elle vous permet de créer des applications attrayantes et accessibles avec 80 éléments prêts à l'emploi dès le départ, et vous offre également la possibilité de personnaliser les éléments pour un design sur mesure.

Dans les cinq prochaines minutes, je vais vous montrer les éléments suivants de Vuetify :

- Typographie
- Espacement
- Boutons
- Navigation
- Grille
- Carte

Et à la fin de cet article, vous vous sentirez confiant pour créer des applications époustouflantes avec seulement quelques lignes de code.

Pendant votre lecture, rendez-vous sur le [cours de 2 heures sur Vuetify de Scrimba](https://scrimba.com/course/gvuetify?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour en savoir plus et explorer le code dans l'environnement interactif de la plateforme. De plus, vous pourrez tester vos nouvelles compétences avec des défis de codage interactifs. C'est parti !

## Création d'un objet Vuetify
Pour utiliser Vuetify, nous commençons par importer Vue et Vuetify depuis leurs CDN.

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
```

Cela nous permet d'instancier une application Vue avec une propriété Vuetify et de créer un nouvel objet Vuetify :
```js
new Vue({ 
    el: '#app',
    vuetify: new Vuetify({}),
    data: {
        message: 'Utilisation de composants à fichier unique'
    }
});
```
[Cliquez ici](https://scrimba.com/p/pP4xZu3/ckPbepSM?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour voir cela en détail.

## Typographie

[![Typographie Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/uey76nlf4hxjttq9krzh.png)](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article)
*Cliquez sur l'image pour accéder au cast.*

Vuetify offre de nombreuses options pour créer une typographie époustouflante, des titres de différentes tailles aux titres, sous-titres et texte de corps :
```vue
<h1 class="display-4">Titre 1</h1>
<h2 class="display-3">Titre 2</h2>
<h3 class="display-2">Titre 3</h3>
<h4 class="title">Titre</h4>
<h5 class="subtitle-1">Sous-titre</h5>
<p class="body-1">Corps</p>
```

Changer la couleur du texte et la couleur de fond est également facile avec Vuetify. Pour la couleur de fond, ajoutez simplement le nom de la couleur requise à la classe de l'élément. Pour la couleur du texte, ajoutez simplement le nom de la couleur suivi de `--text`.

Cela fonctionne pour environ 20 couleurs standard et peut être personnalisé en utilisant des classes accompagnatrices telles que `lighten` et `darken`.
```vue
<h1 class="display-4 purple yellow--text text--darken-2">Titre 1</h1>
```

Vuetify offre également des classes pour changer le poids et le style de la police, ainsi que pour tronquer et transformer le texte. [Rendez-vous sur le cast](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour en savoir plus.

## Espacement

Quiconque a déjà utilisé CSS sait que les marges et le remplissage peuvent être délicats. Pas avec Vuetify ! Pour ajouter et ajuster l'espacement entre les éléments, utilisez simplement des classes avec les abréviations suivantes :

`m` = marge
`p` = remplissage
`t` = haut
`r` = droite
`b` = bas
`l` = gauche
`x` = droite + gauche
`y` = haut + bas
`a` = tout

La taille de l'espacement est ajustée en utilisant les nombres de 1 à 12, qui correspondent à des incréments de quatre pixels. Par exemple, `ml-5` désigne une marge gauche de 20 pixels.

```vue
<h3 class="ml-5">Espacement</h3>
```

Centrer les éléments est également facile avec Vuetify. Il suffit d'envelopper l'élément dans un conteneur qui s'étend sur la page, puis de lui donner une marge droite et gauche de `auto` :
```vue
<v-row>
     <h3 class="mx-auto">Espacement</h3>
</v-row>
```

Ce n'est pas tout ce que Vuetify a à offrir en termes d'astuces et de conseils pratiques pour l'espacement des éléments. [Cliquez ici](https://scrimba.com/p/pP4xZu3/cD7pnzSw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour voir le cast et découvrir plus de fonctionnalités !

## Boutons

Vuetify offre des dizaines d'options pour styliser les boutons, y compris des boutons cliquables réguliers, des boutons de contour avec des icônes pré-positionnées, et des boutons avec icônes uniquement.

Continuez à lire pour voir certaines des options disponibles directement, ou [cliquez ici](https://scrimba.com/p/pP4xZu3/crmrBwtP?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour voir comment personnaliser les boutons.

**Grand bouton de contour :**

![Grand bouton de contour](https://dev-to-uploads.s3.amazonaws.com/i/uobelihs9l8ab86duimx.png)

```vue
<v-btn large outlined>Submit</v-btn>
```

**Bouton avec icône :**

![Bouton avec icône](https://dev-to-uploads.s3.amazonaws.com/i/zbs74uvuqnyfyrg529yq.png)
```vue
<v-btn tile outlined color="success">
     <v-icon left>mdi-pencil</v-icon> Edit
</v-btn>
```

**Bouton d'action flottant avec icône :**
![Bouton d'action flottant avec icône](https://dev-to-uploads.s3.amazonaws.com/i/39p0zcaeyr8plveu2tjj.png)
```vue
<v-btn class="mx-2" fab dark color="indigo">
     <v-icon dark>mdi-plus</v-icon>
</v-btn>
```

## Navigation

[![Barre de navigation Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/z4iz7cjvdttvdk31227f.png)](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article)
*Cliquez sur l'image pour accéder au cast.*

Les deux principales options de navigation disponibles dans Vuetify sont `<v-app-bar>` et `<v-toolbar>`.

```vue
<v-app-bar
     color="deep-purple accent-4"
     dense
     dark
>
```

Bien que les deux éléments soient interchangeables dans une certaine mesure, `<v-app-bar>` est conçu pour être utilisé comme navigation principale d'un site et inclut des fonctionnalités telles que des animations de défilement et une gamme de props et d'options.

`<v-toolbar>` est un composant plus petit et plus polyvalent, conçu pour fournir des fonctionnalités à d'autres zones d'une application. Par exemple, il pourrait être utilisé pour les fonctionnalités d'édition de base sur un petit éditeur de texte.

Les deux éléments de navigation gèrent les listes déroulantes et redimensionnent automatiquement les icônes et les boutons de navigation.

## Grille

Vuetify dispose d'un système de grille intégré qui simplifie le dimensionnement et le positionnement des éléments dans une application. La grille est divisée en 12 colonnes et comporte cinq points de rupture média pour gérer une variété de tailles d'écran.

Bien que la largeur par défaut d'un élément soit de 12 colonnes, il est facile de l'ajuster en changeant la valeur de la colonne. Par exemple, un élément avec une valeur de colonne de 6 occupe la moitié de la largeur de la page. Les éléments peuvent être positionnés en utilisant la propriété `offset`.
```vue
<v-col sm="6" offset-sm="3">
    <v-card
    class="pa-2"
    outlined
    tile
    >
    Colonne
    </v-card>
</v-col>
```

Les colonnes dans Vuetify viennent avec un espacement pré-établi. [Cliquez ici](https://scrimba.com/p/pP4xZu3/cWKBnPSV?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour voir comment cela affecte l'élément et comment le personnaliser.

## Carte

[![Carte personnalisée Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/mvxtqa1l2dfze9mu8acv.png)](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article)
*Cliquez sur la carte pour accéder au scrim.*

Ajouter des cartes à votre application est simple avec l'élément `<v-card>` de Vuetify, qui est facilement personnalisable avec ses quatre éléments imbriqués optionnels : `<v-card-title>`, `<v-card-text>`, `<v-card-actions>` et `<v-list-item-content>`.

J'ai joué avec la carte fournie [dans le cast](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour créer ma propre Carte Café. Pourquoi ne pas y aller et voir où votre imagination vous mène, vous aussi ?

```vue
 <v-card class="mx-auto" color="brown" dark >
    <v-card-title>
    <v-icon large left> mdi-coffee</v-icon>
    <span class="title font-weight-light">Carte Café</span>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">"Le café, c'est génial !"</v-card-text>

    <v-card-actions>
    <v-list-item class="grow">
        <v-list-item-content>
        <v-list-item-title>Mlle C Bean</v-list-item-title>
        </v-list-item-content>

        </v-row>
    </v-list-item>
    </v-card-actions>
</v-card>
```

C'est tout pour notre tour hyper-rapide des fonctions de base de Vuetify. Pour explorer davantage, rendez-vous [sur le cours](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) et consultez le fichier Playground.vue, où vous pouvez tester le code et voir plus de ce qu'il peut faire.

Le cours comprend également une série de défis interactifs pour mettre à l'épreuve vos nouvelles connaissances et vous aider à devenir un pro de Vuetify. Une fois que vous avez terminé, pourquoi ne pas jeter un œil à [l'éventail des autres sujets de Scrimba](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) pour continuer votre parcours d'apprentissage ?

Quel que soit votre choix pour la suite, bon codage :)