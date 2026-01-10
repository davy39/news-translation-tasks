---
title: Comment intégrer ApexCharts avec Vue.js – un guide détaillé
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-15T23:14:04.000Z'
originalURL: https://freecodecamp.org/news/a-detailed-guide-to-integrating-apexcharts-with-vuejs
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vueApex-1.png
tags:
- name: charts
  slug: charts
- name: Vue.js
  slug: vuejs
seo_title: Comment intégrer ApexCharts avec Vue.js – un guide détaillé
seo_desc: 'By Oluwaseyi Bello

  Charts and graphs are a great way to display information/data to your app''s users.
  In this article I will show you exactly how to do that with vue-apexcharts.

  Getting Started

  Using the Vue CLI we can easily create a starter applica...'
---

Par Oluwaseyi Bello

Les graphiques et les diagrammes sont un excellent moyen d'afficher des informations/données aux utilisateurs de votre application. Dans cet article, je vais vous montrer exactement comment faire cela avec vue-apexcharts.

## Prise en main

En utilisant le CLI de Vue, nous pouvons facilement créer une application de démarrage. Tout d'abord, nous devons installer le CLI de Vue avec la commande ci-dessous. Vous pouvez sauter cette étape si vous l'avez déjà installé.

Note : Pour utiliser le CLI, vous aurez besoin de [Node.js](https://nodejs.org/) version 8 ou supérieure installée (8.10.0+ est recommandé).

Pour installer le CLI, exécutez cette commande dans votre terminal :

```
npm install @vue/cli
```

Maintenant, nous pouvons l'utiliser pour créer notre projet. Nous allons créer le projet en utilisant cette commande :

```
vue create vue-apexcharts-demo
```

Nous serons alors invités à choisir une configuration par défaut ou à sélectionner manuellement des fonctionnalités. Sélectionnez `**default**`.

Un nouveau répertoire de projet sera créé, et vous pouvez y naviguer en utilisant cette commande :

```
cd vue-apexcharts-demo
```

## Installation d'ApexCharts

Avant de continuer, vous vous demandez peut-être...

**Qu'est-ce qu'ApexCharts ?!**

ApexCharts est une bibliothèque moderne de graphiques qui aide les développeurs à créer de belles visualisations interactives pour les pages web. Vous pouvez voir leur démonstration [ici](https://apexcharts.com/javascript-chart-demos/).

Nous pouvons facilement utiliser ApexCharts avec notre application Vue en intégrant son composant wrapper pour Vue appelé **vue-apexcharts**.

Pour installer le composant vue-apexcharts dans notre application, utilisez cette commande :

```
npm install --save apexcharts 
npm install --save vue-apexcharts
```

## Configuration de vue-apexcharts

Maintenant que nous avons installé vue-apexcharts, nous devons l'installer dans notre application. Ouvrez le répertoire `src` et créez un nouveau répertoire appelé `plugins`. À l'intérieur du nouveau répertoire plugins, créez un fichier appelé `apexcharts.js`.

Ensuite, nous allons créer un composant Vue pour apexcharts dans notre fichier `apexcharts.js`. Cela rendra le composant globalement disponible dans notre application.

Pour ce faire, nous allons importer à la fois Vue et vue-apexcharts. Ensuite, nous allons créer un composant global appelé `apexchart`. Voici à quoi votre fichier `apexcharts.js` devrait ressembler :

```
import Vue from 'vue'
import VueApexCharts from 'vue-apexcharts'

Vue.component('apexchart', VueApexCharts)
```

## Importation de notre fichier plugin

Nous devons faire en sorte que Vue soit conscient du fichier que nous venons de créer. Pour cela, nous l'importons dans le fichier `main.js`. Ouvrez le fichier main.js et ajoutez la ligne suivante après la dernière instruction d'importation :

```
import '@/plugins/apexcharts'
```

Maintenant, nous sommes prêts à créer notre premier graphique.

## Création de notre premier graphique

Nous allons créer nos graphiques dans le composant HelloWorld. Ce composant a été créé automatiquement lorsque nous avons utilisé le CLI de Vue pour créer notre application.

Ouvrez le fichier `HelloWorld.vue` et supprimez tout le code de démonstration qui s'y trouve.

Votre fichier devrait ressembler à ceci :

```
<template>
</template>
<script>  
export default {
 name: 'HelloWorld'
}
</script>
<style scoped>
</style>
```

Rappelons que dans notre plugin, nous avons appelé notre composant `apexchart`.

Vue-Apexcharts construit des graphiques en utilisant les données que vous lui passez via des props, comme le montre le code ci-dessous. Nous allons utiliser cela pour créer le HTML de notre premier graphique. Dans le premier exemple, nous allons commencer par un graphique en barres très basique.

```
<template>
  <div>
   <apexchart 
     width="500" type="bar" 
     :options="options" :series="series">
   </apexchart>  
  </div>
</template>
```

Comme vous pouvez le voir dans le modèle ci-dessus, le composant `apexchart` contient 4 props. Maintenant, passons à la partie script.

```
<script>
export default {
  name: 'HelloWorld',
  data: () => ({
    options: {
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        categories: [
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec"
        ]
      }
    },
    series: [{
      name: 'series-1',
      data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
    }]
  })
}
</script>
```

## Explication des données du graphique

Notre graphique en barres contient les prix mensuels des actions pour une organisation fictive. Nous avons 12 points de données dans notre graphique en barres. Chaque mois sera affiché sur l'axe des x du graphique. Leurs prix sont affichés sur l'axe des y du graphique.

Pour fournir les données qui seront affichées dans notre graphique en barres, nous allons ajouter un tableau de séries. Une série est un tableau d'objets. Chaque objet définit le type de graphique à créer et aura un tableau de données de valeurs à tracer sur le graphique.

Vous pouvez démarrer votre serveur avec la commande :

```
npm run serve
```

Maintenant, ouvrez votre navigateur à localhost:8080 et vous devriez voir votre graphique :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/firstapexchart.png)

### Stylisation de nos graphiques

Nous pouvons placer notre graphique au centre de la page. Pour ce faire, je vais ajouter une classe `chart-wrapper` à l'intérieur de notre div. Je veux également augmenter la largeur du graphique à 800px. Mon modèle ressemble maintenant à ceci :

```
<template>
  <div class="chart-wrapper">
    <apexchart 
      width="800" type="bar" 
      :options="options" :series="series">
    </apexchart>
</div>
</template>
```

Ensuite, ajoutons un peu de style à la nouvelle classe `chart-wrapper` qui placera notre graphique au centre de la page. Voici le style que j'ai ajouté :

```
<style scoped>
div.chart-wrapper {
  display: flex;
  align-items: center;
  justify-content: center
}
</style>
```

Pendant que nous ajoutons des styles, je veux remplacer le logo Vue par un titre. Ouvrez le fichier App.vue. Supprimez la balise <img> et remplacez-la par :

```
<h1>Démonstration de Vue Apexcharts</h1>
```

Nos graphiques ressemblent maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/firsapexchart.png)

### Ajout d'un titre et changement de la couleur du graphique

Nous pouvons ajouter un titre à notre graphique en barres pour ajouter un contexte supplémentaire et une explication de ce que représente le graphique.

Pour ajouter un titre à notre graphique en barres, retournez à votre composant HelloWorld.vue et ajoutez un titre à l'objet `options`.

```
options: {
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        categories: [
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec"
        ]
      },
      title: {
        text: 'Prix mensuel des actions'
      }
 },
 series: [{
   name: 'series-1',
   data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
 }]
```

Par défaut, le titre est placé sur le côté gauche du graphique en barres. Voici à quoi ressemble notre graphique maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/firapexchart.png)

Changeons le comportement par défaut en ajoutant notre propre style personnalisé. Je veux que le titre ait une taille de police plus grande et soit centré. L'objet titre a une propriété appelée `align` qui représente le plan horizontal. Je veux que le titre soit centré sur celui-ci. Pour que le titre ait une taille de police plus grande, nous devons ajouter une option `style`.

De plus, nous pouvons définir le graphique en barres pour qu'il ait une couleur différente. Voici à quoi ressemble `options` maintenant :

```
options: {
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        categories: [
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec"
        ]
      },
      title: {
        text: 'Prix mensuel des actions',
        align: 'center',
        style: {
          fontSize:  '20px',
        },
      },
      colors: ['#00897b']
 },
 series: [{
   name: 'series-1',
   data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
 }]
```

Voici à quoi ressemble le graphique en barres maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/fiapexchart.png)
_Version finale de notre graphique en barres_

### Création d'un graphique en ligne

Tout d'abord, nous devons créer une nouvelle div chart-wrapper et un nouvel élément apexchart. Le nouvel élément apexchart contiendra des props comme dans l'exemple précédent. Mais l'élément intéressant ici est que tout ce que vous avez à faire est de changer la prop `type` dans le modèle en `line`.

Voici à quoi ressemble mon code HTML maintenant :

```
<template>
  <div>  
    <div class="chart-wrapper">
      <apexchart 
        width="800" type="bar" 
        :options="options" :series="series">
      </apexchart>
    </div>
    <hr>
    <div class="chart-wrapper">
      <apexchart 
        width="800" type="line" 
        :options="options" :series="series">
      </apexchart>
    </div>
  </div>
</template>
```

Nous avons maintenant ce graphique en ligne :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/fapexchart.png)
_Graphique en ligne_

## Documentation d'ApexCharts

ApexCharts propose différents types de graphiques parmi lesquels vous pouvez choisir, autres que les barres et les lignes. Ils disposent également de diverses options que vous pouvez ajouter à votre graphique. Vous pouvez ajouter des légendes ou des marqueurs, et des infobulles par exemple.

Si vous souhaitez en savoir plus sur les autres types de graphiques et options disponibles, vous pouvez lire leur documentation [ici](https://apexcharts.com/docs/installation/)

### Dépôt

Vous pouvez trouver le code de cet article dans [mon compte github](https://github.com/Seybel/vue-apexcharts-demo).

## Conclusion

Les graphiques nous aident à visualiser les données et aident les utilisateurs à les visualiser et à interagir avec elles. Intégrer ApexCharts à votre application Vue est aussi facile que vous l'avez vu ci-dessus.

Les commentaires sont les bienvenus ! Et veuillez partager cet article si vous l'avez trouvé utile.

Merci d'avoir lu !