---
title: Comment ajouter des graphiques et des diagrammes à une application Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-07T18:39:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-charts-and-graphs-to-a-vue-js-application-29f943a45d09
coverImage: https://cdn-media-1.freecodecamp.org/images/0*H0zOGll9hkDgaraV
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Comment ajouter des graphiques et des diagrammes à une application Vue.js
seo_desc: 'By Jennifer Bland

  Quick Guide to using echarts and vue-echarts

  The heart of every application is displaying data to users. Sometimes it is very
  challenging to display that data using text. Charts and graphs are a great way to
  provide a visual represe...'
---

Par Jennifer Bland

### Guide rapide pour utiliser echarts et vue-echarts

Le cœur de toute application est l'affichage des données aux utilisateurs. Parfois, il est très difficile d'afficher ces données en utilisant du texte. Les graphiques et les diagrammes sont un excellent moyen de fournir une représentation visuelle de ces données. Dans cet article, je vais vous montrer à quel point il est facile de créer des graphiques visuellement attrayants dans votre application Vue.js.

### Mise en route

Je vais utiliser le Vue CLI pour créer rapidement une application de démarrage. Je vais utiliser à la fois echarts et vue-echarts pour ajouter des graphiques à notre application de démarrage. Alors commençons.

Installez le Vue CLI avec cette commande :

```bash
npm install @vue/cli
```

Ensuite, nous allons utiliser le Vue CLI pour créer une application Vue que nous allons utiliser. Nous allons créer l'application avec cette commande :

```bash
vue create vue-echarts-demo
```

Le Vue CLI vous demandera si vous souhaitez utiliser la configuration par défaut ou sélectionner manuellement les fonctionnalités. Sélectionnez `default`.

Cela créera notre application dans un dossier appelé `vue-echarts-demo`. Changez de répertoire avec cette commande :

```bash
cd vue-echarts-demo
```

#### Installation des packages de graphiques

**eCharts** est l'un des plus grands et des plus largement utilisés programmes de graphiques. Nous allons l'utiliser dans notre application Vue. Pour permettre son utilisation dans Vue, nous allons également utiliser un produit appelé **vue-echarts**. Vue-echarts est un wrapper pour eCharts qui permet de l'utiliser dans l'environnement Vue.

Vous pouvez les installer tous les deux avec cette commande :

```bash
npm install echarts vue-echarts
```

#### Configuration des packages de graphiques

Maintenant que nous avons installé les packages de graphiques, nous devons les installer dans notre application. Ouvrez le répertoire `src` et créez un nouveau répertoire appelé `plugins`. À l'intérieur du nouveau répertoire plugins, créez un fichier appelé `echarts.js`.

Nous allons créer un composant Vue pour eCharts dans ce fichier. Le composant sera globalement disponible dans notre application. Les étapes que nous devons suivre sont d'importer à la fois vue et vue-echarts. Ensuite, nous allons importer les parties de eCharts que nous allons utiliser. Notre premier graphique sera un graphique à barres, nous devons donc l'importer également. Enfin, nous créons un composant global appelé `chart`. Voici à quoi votre fichier echarts.js devrait ressembler :

```js
import Vue from 'vue';
import Echarts from 'vue-echarts';

import 'echarts/lib/chart/bar';

Vue.component('chart', Echarts);
```

#### Importation de notre fichier de plugin

Nous devons faire en sorte que Vue soit conscient du fichier que nous venons de créer. Nous le faisons en l'important dans le fichier `main.js`. Ouvrez le fichier main.js et ajoutez la ligne suivante après la dernière instruction d'importation :

```js
import "@/plugins/echarts";
```

Maintenant, nous sommes prêts à créer notre premier graphique.

### Création d'un graphique à barres

Nous allons créer tous nos graphiques dans le composant HelloWorld. Ce composant a été créé automatiquement lorsque nous avons utilisé le Vue CLI pour créer notre application.

Ouvrez le fichier `HelloWorld.vue` et faites ce qui suit :

* supprimez tout le HTML à l'intérieur des balises de template
* supprimez les props dans les balises de script
* supprimez tout le CSS dans les balises de style

Votre fichier devrait ressembler à ceci :

```html
<template>
</template>

<script>
export default {
  name: 'HelloWorld',
}
</script>

<style scoped>
</style>
```

Dans notre plugin, nous avons appelé notre composant `chart`. Vue-echarts construit des graphiques en utilisant les données que vous lui passez en utilisant une prop appelée `options`. Utilisons cela pour créer le HTML de notre premier graphique. Ajoutez le code suivant à l'intérieur des balises de template :

```js
<chart :options="chartOptionsBar"></chart>
```

#### Définition de notre graphique

Ensuite, nous devons définir les données qui seront utilisées pour créer notre graphique. À l'intérieur des balises de script, créez un nouvel objet de données avec une entrée pour chartOptionsBar. Votre balise de script devrait ressembler à ceci :

```html
<script>
export default {
  name: 'HelloWorld',
  data: () => ({
    chartOptionsBar: {}
  })
}
</script>
```

#### Création des données du graphique

Notre premier graphique à barres contiendra des données de ventes trimestrielles pour une entreprise fictive. Chaque trimestre sera affiché sur l'axe des x du graphique. Le montant des ventes sera affiché sur l'axe des y du graphique.

Définissons d'abord notre xAxis. Nous allons fournir un tableau de données qui contiendra des entrées pour chaque trimestre de l'année. Ajoutez ce qui suit à notre objet `chartOptionsBar` :

```js
chartOptionsBar: {
  xAxis: {
    data: ['T1', 'T2', 'T3', 'T4']
  }
}
```

Notre yAxis n'affichera que la valeur des ventes pour chaque trimestre. Pour cette raison, nous n'avons pas besoin de créer un tableau de données pour cela. Au lieu de cela, nous lui disons qu'il affichera la `valeur`. Ajoutez ce qui suit à notre objet chartOptionsBar :

```js
chartOptionsBar: {
  xAxis: {
    data: ['T1', 'T2', 'T3', 'T4']
  },
  yAxis: {
    type: 'value'
  }
}
```

La dernière étape consiste à fournir les données qui seront affichées dans notre graphique à barres. Vous faites cela en ajoutant un tableau de séries. Series est un tableau d'objets. Chaque objet définit le type de graphique à créer et aura un tableau de données de valeurs à tracer sur le graphique. Vous pouvez l'ajouter avec ceci :

```js
chartOptionsBar: {
  xAxis: {
    data: ['T1', 'T2', 'T3', 'T4']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      type: 'bar',
      data: [63, 75, 24, 92]
    }
  ]
}
```

Vous pouvez démarrer votre serveur avec la commande :

```bash
npm run serve
```

Ensuite, ouvrez votre navigateur à localhost:8080 et vous verrez votre premier graphique qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/TWWSuo33KKtPyqsUSjfnFI4ovWyKQcjYXlGi)
_Notre premier graphique à barres_

#### Ajout de styles à nos graphiques

Par défaut, vue-echarts définit une largeur de 600px pour un graphique. Je préférerais que nos graphiques occupent toute la largeur de leur conteneur. Pour ce faire, je vais placer le graphique à l'intérieur d'une div. Je vais donner à cette div une classe appelée `chart-wrapper`. Mon template ressemble maintenant à ceci :

```html
<template>
  <div class="chart-wrapper">
    <chart :options="chartOptionsBar"></chart>
  </div>
</template>
```

Ensuite, je veux ajouter un peu de style à la nouvelle classe `chart-wrapper`. Je vais faire en sorte que cette classe ait une largeur égale à la taille de l'écran et une hauteur de 700px. Voici le style que j'ai ajouté :

```css
.chart-wrapper {
  width: 100%;
  height: 700px;
}
```

Vue-echarts ajoute une classe appelée `echarts` à tous ses graphiques. Nous allons également styliser cela dans notre CSS. Nous allons dire à cette classe de prendre 100% de la hauteur et de la largeur de son conteneur qui est `chart-wrapper`. Voici le CSS que j'ai ajouté :

```css
.echarts {
  width: 100%;
  height: 100%;
}
```

Pendant que nous ajoutons des styles, je veux remplacer le logo Vue par un titre. Ouvrez le fichier App.vue. Supprimez la balise <img> et remplacez-la par :

```html
<h1>Démonstration Vue eCharts</h1>
```

Maintenant, notre graphique ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/-23-wbjVjVPBD6hxiCbqNuydNgOiFAnS5gKv)
_Graphique à barres mis à jour avec notre style_

#### Ajout d'un titre et d'une couleur

C'est un excellent début pour notre premier graphique. Lorsque les gens visualisent le graphique, ils ne sont pas sûrs de ce qu'ils visualisent. Nous pouvons résoudre ce dilemme en ajoutant un titre à notre graphique.

Chaque composant de eCharts que vous souhaitez utiliser doit être importé. Un titre est un composant, nous devons donc l'importer. Ouvrez le fichier echarts.js et ajoutez la ligne suivante :

```bash
import 'echarts/lib/component/title';
```

Ensuite, nous pouvons ajouter un titre à notre graphique à barres. Dans le composant HelloWorld.vue, ajoutons un titre à notre objet `chartOptionsBar`.

```js
chartOptionsBar: {
  xAxis: {
    data: ['T1', 'T2', 'T3', 'T4']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      type: 'bar',
      data: [63, 75, 24, 92]
    }
  ],
  title: {
    text: 'Résultats des ventes trimestrielles'
  }
}
```

Par défaut, eCharts place le titre sur le côté gauche du graphique à barres. Voici à quoi ressemble notre graphique maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/hLTrJjE2gA9M6vWM-t7VZNmY-uv7DKZXkDcu)
_Ajout d'un titre pour notre graphique_

Je n'aime pas l'apparence de ce titre, alors changeons-le. Je veux que le titre ait une taille de police plus grande et soit centré. Le graphique a une option appelée `x` qui représente le plan horizontal. Je veux que le titre soit centré sur celui-ci. Pour que le titre ait une taille de police plus grande, nous devons ajouter un `textStyle`. Le dernier changement que je veux apporter est de définir la barre pour qu'elle ait une couleur différente. Voici à quoi ressemblent mes options maintenant :

```js
chartOptionsBar: {
  xAxis: {
    data: ['T1', 'T2', 'T3', 'T4']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      type: 'bar',
      data: [63, 75, 24, 92]
    }
  ],
  title: {
    text: 'Résultats des ventes trimestrielles',
    x: 'center',
    textStyle: {
      fontSize: 24
    }
  },
  color: ['#127ac2']
}
```

Voici la version finale de mon graphique à barres :

![Image](https://cdn-media-1.freecodecamp.org/images/EZNtQN-TCxe0SLh8w6fazzRbcDn2i-RemxbG)
_La version finale de notre graphique à barres_

### Création d'un graphique en ligne

Ensuite, je vais vous montrer comment créer un graphique en ligne. Nous allons créer un graphique en ligne montrant les prix mensuels des actions pour une entreprise fictive. Alors commençons.

Tout d'abord, nous devons créer une nouvelle div chart-wrapper et un nouvel élément chart. Le nouvel élément chart obtiendra ses options à partir de l'objet `chartOptionsLine`. Voici à quoi ressemble mon code HTML maintenant :

```html
<div>
  <div class="chart-wrapper">
    <chart :options="chartOptionsBar"></chart>
  </div>
  <hr />
  <div class="chart-wrapper">
    <chart :options="chartOptionsLine"></chart>
  </div>
</div>
```

Ensuite, dans notre objet de données, créez un nouvel objet chartOptionsLine. Au lieu de créer un nouvel objet, copiez l'objet chartOptionsBar existant. Renommez la copie en `chartOptionsLine`. Pour l'instant, nous devons seulement changer le type dans series de bar à line. Voici à quoi ressemble notre objet `chartOptionsLine` :

```js
chartOptionsLine: {
  xAxis: {
    data: ["T1", "T2", "T3", "T4"]
  },
  yAxis: {
    type: "value"
  },
  series: [
    {
      type: "line",
      data: [63, 75, 24, 92]
    }
  ],
  title: {
    text: "Résultats des ventes trimestrielles",
    x: "center",
    textStyle: {
      fontSize: 24
    }
  },
  color: ["#127ac2"]
}
```

Si vous allez dans votre navigateur, vous remarquerez que le graphique en ligne ne s'affiche pas. Cela est dû au fait que nous devons l'importer dans notre plugin comme nous l'avons fait avec le graphique à barres.

Ouvrez echarts.js et ajoutez la ligne suivante :

```js
import 'echarts/lib/chart/line';
```

Nous avons maintenant ce graphique en ligne :

![Image](https://cdn-media-1.freecodecamp.org/images/DQ6Njh5F0SlUcHyXP39oZHhsgfkdYZ3TUGUU)
_Notre graphique en ligne initial_

#### Changer le titre et les données

Nous voulons que le graphique en ligne affiche les prix mensuels des actions pour une entreprise fictive. Nous aurons besoin de plus de quatre points de données. Nous aurons 12 points de données pour notre graphique en ligne. Nous voulons également que le titre affiché sur l'axe des x soit les mois de l'année au lieu des trimestres. Nous devons également changer le titre de notre graphique.

Nous pouvons mettre à jour notre chartOptionsLine avec ces valeurs :

```js
chartOptionsLine: {
  xAxis: {
    data: [
      "Jan",
      "Fév",
      "Mar",
      "Avr",
      "Mai",
      "Juin",
      "Juil",
      "Août",
      "Sep",
      "Oct",
      "Nov",
      "Déc"
    ]
  },
  yAxis: {
    type: "value"
  },
  series: [
    {
      type: "line",
      data: [55, 72, 84, 48, 59, 62, 87, 75, 94, 101, 127, 118]
    }
  ],
  title: {
    text: "Prix mensuels des actions",
    x: "center",
    textStyle: {
      fontSize: 24
    }
  },
  color: ["#127ac2"]
}
```

Maintenant, notre graphique en ligne ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/zpd6HWN5IIoBLkXW3gLFBZe9Jaj6INgRXgMk)
_Graphique en ligne final_

### Accès à la documentation des graphiques

eCharts fournit de nombreux autres types de graphiques en plus des graphiques à barres et en ligne. eCharts fournit une pléthore d'options que vous pouvez ajouter à votre graphique. Vous pouvez ajouter des légendes ou des infobulles par exemple.

Si vous souhaitez en savoir plus sur les autres types de graphiques et les options disponibles, vous pouvez lire leur documentation. Voici un [lien vers la documentation](https://echarts.apache.org/option.html#title).

### Obtenir le code

Tout le code de cet article peut être [trouvé dans mon compte GitHub](https://github.com/ratracegrad/vue-eCharts-demo).

### Conclusion

Il est très facile d'ajouter des graphiques et des diagrammes personnalisés à votre application Vue.js en utilisant eCharts et vue-echarts. Les graphiques fournissent un moyen de visualiser les données pour les utilisateurs.

Si vous avez des commentaires, veuillez laisser un commentaire ci-dessous. Merci d'avoir lu cet article.