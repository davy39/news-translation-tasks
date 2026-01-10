---
title: Comment construire et déployer un portfolio avec Vue.js Axios, l'API REST GitHub
  et Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-12T20:53:20.000Z'
originalURL: https://freecodecamp.org/news/build-a-portfolio-with-vuejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/VUE.JS-_-Article-Cover.jpg
tags:
- name: axios
  slug: axios
- name: GitHub
  slug: github
- name: Netlify
  slug: netlify
- name: portfolio
  slug: portfolio
- name: projects
  slug: projects
- name: Vue.js
  slug: vuejs
seo_title: Comment construire et déployer un portfolio avec Vue.js Axios, l'API REST
  GitHub et Netlify
seo_desc: "By Fabio Pacific\nIn this free book, we will build two simple projects\
  \ and deploy them on Netlify. We will use Vue.js as our front-end framework, and\
  \ use different technologies to build our projects. \nIf you follow this tutorial\
  \ to the end, you will b..."
---

Par Fabio Pacific

Dans ce livre gratuit, nous allons construire deux projets simples et les déployer sur Netlify. Nous utiliserons Vue.js comme framework front-end et différentes technologies pour construire nos projets.

Si vous suivez ce tutoriel jusqu'au bout, vous construirez une version simplifiée de Twitter et une application monopage (SPA) pour un portfolio utilisant l'API GitHub.

## Ce que vous devez savoir pour suivre ce tutoriel

Pour suivre ce guide, vous aurez besoin d'au moins quelques connaissances de base en HTML, CSS et JavaScript.

La connaissance de Vue.js n'est pas requise, car vous apprendrez d'abord les bases, puis nous passerons à la construction des projets ensemble.

À la fin de chaque section, vous trouverez ces informations sous forme de vidéo via un lien/intégration YouTube. De cette façon, vous pourrez regarder les vidéos pour consolider les connaissances que vous venez de lire.

## Table des matières

* [Introduction](#heading-introduction)
* [Comment installer Vue](#heading-comment-installer-vue)
* [Comment créer une instance Vue](#heading-comment-creer-une-instance-vue)
* [Comment travailler avec les templates dans Vue](#heading-comment-travailler-avec-les-templates-dans-vue)
* [Directives Vue](#heading-directives-vue)
* [Méthodes](#heading-methodes-dans-vue)
* [Conditionnels](#heading-conditionnels-dans-vue-v-ifv-else-ifv-elsev-show)
* [Boucles](#heading-boucles-dans-vue)
* [Comment gérer les entrées utilisateur avec la gestion des événements](#heading-comment-gerer-les-entrees-utilisateur-avec-la-gestion-des-evenements-v-on-dans-vue)
* [Liaison de modèle bidirectionnelle (v-model)](#heading-liaison-de-modele-bidirectionnelle-v-model-dans-vue)
* [Propriétés calculées et méthodes](#heading-proprietes-calculees-et-methodes)
* [**Projet** : Clone simple de Twitter](#heading-comment-creer-un-clone-simple-de-twitter)
* [Les bases des composants](#heading-les-bases-des-composants-vue)
* [Mise à jour du projet : Clone simple de Twitter avec des composants](#heading-comment-mettre-a-jour-votre-projet-simpletwitter-avec-des-composants)
* [Axios et RestAPI](#heading-comment-effectuer-des-appels-api-avec-axios)
* [Routage avec VueRouter](#heading-comment-gerer-le-routage-avec-vuerouter)
* [**Projet final** : construire un portfolio avec VueJS, VueRouter, Axios, API GitHub](#heading-projet-final-comment-construire-un-portfolio-avec-vuejs-vuerouter-axios-api-github-et-deployer-sur-netlify)
* [**Déploiement** Déploiement continu avec BitBucket et Netlify](#heading-deploiement-continu-avec-bitbucket-et-netlify)

## Introduction
VueJS est un framework JavaScript qui est devenu très populaire ces dernières années.

Dans ce guide, nous commencerons par examiner les fondamentaux, avec un aperçu rapide de deux bibliothèques : VueRouter et Axios. Nous les utiliserons pour construire un projet de portfolio sympa à la fin.

%[https://youtu.be/CzgP6GamIMc]

Cliquez pour voir la vidéo sur [YouTube](https://youtu.be/CzgP6GamIMc).

## Comment installer Vue

Vous pouvez utiliser Vue dans vos projets en l'installant via un gestionnaire de paquets comme NPM ou en utilisant son CDN. Si vous n'avez jamais utilisé Vuejs auparavant, je vous suggère d'utiliser le CDN, car ce sera plus facile si vous voulez coder en même temps que moi.

Cliquez pour voir le [Dépôt](https://bitbucket.org/fbhood/how-to-vuejs/src/master/1-installation/)

Cliquez pour voir la [Vidéo-YouTube](https://youtu.be/enz0Vi3NuDA) ou retrouvez-la à la fin de cette section pour renforcer ce que vous avez appris.

### Le CDN Vue
Pour le CDN, nous avons seulement besoin d'inclure la balise script ci-dessous à l'intérieur de notre fichier HTML :

```html
<!-- Version de développement pour le prototypage et l'apprentissage -->
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.js"></script>
```
Alternativement, vous pouvez utiliser un script prêt pour la production qui utilise une version stable spécifique, comme ceci :

```html
<!-- Version de production -->
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>
```

En production, Vue suggère d'utiliser la version optimisée en remplaçant vue.js par vue.min.js.

Il existe également une version compatible avec les modules ES :
```html
<script type="module">
  import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.esm.browser.js'
</script>
```

### Comment installer Vue via NPM
Si vous prévoyez de construire des applications à grande échelle, je recommande l'installation via NPM comme ceci :

```bash
npm install vue
```

Comme je l'ai dit plus haut, nous utiliserons le CDN Vue pour que tout le monde puisse suivre ce guide. Notre fichier HTML final ressemblera donc à ceci :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutoriel VueJS</title>
    
    <!-- version de développement vue, inclut des avertissements utiles en console -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

</head>
<body>



    <script src="./main.js"></script>
</body>
</html>

```

Décortiquons ce code. Tout d'abord, nous avons ajouté un balisage de base pour un fichier HTML. Ensuite, nous avons inclus la balise script pour le framework VueJs.

À la fin, avant de fermer la balise body, nous avons ajouté notre script main.js où nous avons placé tout le code JavaScript de notre application.

Passons maintenant à l'étape suivante et ajoutons notre première instance Vue à l'intérieur du fichier main.js.


%[https://youtu.be/enz0Vi3NuDA]

## Comment créer une instance Vue

Une fois que vous avez installé Vue ou que vous l'avez inclus via son CDN, vous pouvez créer une instance Vue. Vous pouvez le faire en utilisant la fonction `new Vue()`. Cette fonction accepte un objet d'options.

Si vous lisez la documentation, vous verrez que l'instance vue est souvent stockée dans une variable appelée `vm`, mais vous pouvez l'appeler comme vous le souhaitez. Je l'appellerai `app` tout au long de ce guide.

Alors maintenant, à l'intérieur du fichier main.js, vous devez créer une variable et y stocker l'instance Vue comme ceci :
```js
let app = new Vue({
    // toutes les options vont ici
})
```
L'objet que vous passez à l'instance Vue est appelé l'objet d'options.
À l'intérieur de l'objet d'options, vous pouvez ajouter toutes les options décrites dans les pages de référence de l'API Vue pour construire notre application.

L'objet d'options a des propriétés divisées en plusieurs sections :
- Données (Data)
- DOM
- Hooks de cycle de vie (Life Cycle Hooks)
- Assets
- Composition
- Catégories diverses

La première propriété dont vous avez besoin pour construire votre application Vue est utilisée pour connecter Vue avec un élément DOM racine. Ensuite, vous aurez besoin de certaines options de données pour travailler.

Commençons par connecter l'instance Vue avec un élément DOM racine.

Vous pouvez cliquer pour voir le [Dépôt](https://bitbucket.org/fbhood/how-to-vuejs/src/master/2-create-vue-instance/) ici.

Et vous pouvez cliquer pour voir la [Vidéo-YouTube](https://youtu.be/gBJaL7Jqh4w) ou la trouver à la fin de cette section pour revoir ce que vous avez appris.

### Options/DOM : Comment sélectionner l'élément DOM racine

L'API Options/DOM vous donne une propriété `el` que vous pouvez utiliser pour sélectionner un élément DOM existant que Vue utilisera pour monter votre instance d'application.

La propriété `el` accepte une chaîne de caractères qui contient un sélecteur CSS pour l'élément ou directement un élément DOM.

NOTE : Vue déconseille d'utiliser les balises body ou HTML et suggère d'utiliser un élément différent comme point de montage.

Faisons-le. À l'intérieur du body du fichier index.html, vous devez mettre le code suivant :

```html
    <div id="app">
    </div> 
```
Vous avez maintenant un élément racine que vous pouvez utiliser pour connecter l'instance Vue.
De retour dans le fichier main.js, sélectionnons cet élément à l'intérieur de l'objet d'options.

Vous pouvez maintenant utiliser la propriété `el` pour sélectionner l'élément que vous avez créé avec un id `app`.

```js
let app = new Vue({
    // toutes les options vont ici
    el: "#app",
})
```

Vous avez maintenant un élément avec lequel travailler. Vous pouvez passer à l'étape suivante et ajouter l'objet data à l'objet d'options.

Vous pouvez en savoir plus dans la documentation ici : [https://vuejs.org/v2/api/#Options-DOM]


### Options/Data : Comment ajouter l'objet data (ou une fonction lorsqu'il est utilisé dans un composant)

Lorsqu'une nouvelle instance est créée, elle ajoute toutes les propriétés trouvées dans son objet data au système de réactivité de Vue. Et lorsqu'une valeur dans l'objet data change, la vue reflétera ces changements. C'est la base du système de réactivité de VueJS.

Pour l'expliquer, voyons un exemple pratique.

#### Créer un objet data
À l'intérieur du fichier main.js, vous pouvez créer une propriété data qui a un objet comme valeur, comme ceci :
```js

let app = new Vue({
    // toutes les options vont ici
    el: "#app",
    data: {}
})
```
L'objet data peut être défini directement à l'intérieur de l'instance Vue comme dans le code ci-dessus, ou à l'extérieur de l'instance comme dans le code ci-dessous.

```js
let dataObject = {}
let app = new Vue({
    // toutes les options vont ici
    el: "#app",
    data: dataObject
})
```

Vous pouvez choisir celui que vous préférez.

#### Ajouter des propriétés à l'objet Data
Puisque VueJs est un framework JavaScript, il est utile de se rappeler que ce que vous savez sur JavaScript est toujours précieux ici.

Vue est juste un objet JavaScript qui possède un certain nombre de méthodes et de propriétés que vous pouvez utiliser pour simplifier et accélérer votre flux de travail.

Ajoutons quelques propriétés à l'objet data pour voir comment cela fonctionne.
```js
// Créer un objet data
let app = new Vue({
    el:"#app",
    // créer une instance vue, ajouter la propriété data et le dataObject créé
    data: {
        alert: "Ceci est un message d'alerte ! ",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "épicerie", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "script d'automatisation", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ];
    }
})
```
Avec le code ci-dessus, vous ajoutez simplement deux propriétés à l'objet data : une propriété `alert` et une propriété `projects`.

La propriété alert est juste une chaîne de caractères tandis que la propriété projects est un tableau d'objets.

Maintenant que vous avez des données avec lesquelles travailler, voyons comment vous pouvez accéder à leurs valeurs et les modifier.

#### Manipuler les propriétés dans l'objet data
Vous pouvez accéder et manipuler les propriétés d'un objet data en utilisant la variable qui contient l'instance Vue `app`. Ensuite, vous pouvez référencer les propriétés en utilisant la notation par points, comme `app.alert`.

Dans le navigateur, si vous ouvrez la console, vous pouvez voir que lorsque vous écrivez `app`, vous obtenez l'objet de l'instance Vue. Ainsi, comme tout autre objet avec la notation par points, vous obtenez ses propriétés et méthodes.

Essayons cela dans la console :
```js
// Accéder à la propriété alert dans l'objet data
app.alert // Ceci est un message d'alerte !
// mettre à jour la valeur d'une propriété de données
app.alert = "Ceci est un nouveau message d'alerte !" 
app.projects
```
Le code ci-dessus fait trois choses simples :
- la première ligne accède à la propriété `alert` et affiche son contenu "ceci est un message d'alerte"
- la deuxième ligne assigne une nouvelle valeur à la propriété `alert` avec l'opérateur d'égalité
- enfin, la troisième ligne renvoie la valeur du tableau projects.

Vous pouvez également accéder à l'intégralité de l'objet data en utilisant les raccourcis $data ou _data

De retour dans la console :
```js
// Accéder à l'intégralité de l'objet data
app.$data // {__ob__: Observer} option 1
app._data // {__ob__: Observer} option 2

```

Vous pouvez en savoir plus à ce sujet dans la documentation ici : [https://vuejs.org/v2/api/#Options-Data]

### Méthodes de données des options
L'instance Vue vous donne accès à un certain nombre de propriétés et de méthodes.
Vous pouvez accéder aux méthodes et propriétés par défaut en utilisant le signe `$`. Il est utilisé pour différencier les méthodes définies par Vue de celles définies par l'utilisateur.

Il existe un certain nombre de méthodes et de propriétés d'instance prédéfinies et divisées en quatre catégories différentes :

- Propriétés d'instance
- Méthodes d'instance / Données
- Méthodes d'instance / Événements
- Méthodes d'instance / hooks de cycle de vie

Par exemple, avec le code suivant, vous pouvez obtenir les objets `data` et `options` ou accéder aux méthodes `watch` ou `on`.

```js
app.$data // renvoie l'objet data
app.$options // renvoie l'objet options
app.$watch() // fonction qui surveille les changements sur l'instance vue
app.$on() // écoute un événement personnalisé sur l'instance vue
```

Je n'approfondirai pas davantage car cela sort du cadre de ce guide. Mais si vous êtes intéressé et souhaitez en savoir plus, voici la [documentation](https://vuejs.org/v2/api/#Instance-Properties).

### Hooks de cycle de vie
Vue vous donne accès à une série de fonctions appelées hooks de cycle de vie. Ils vous permettent d'exécuter du code à des étapes spécifiques de l'initialisation de Vue.

À l'intérieur de tous les hooks de cycle de vie, vous avez accès à leur variable `this` qui pointe vers l'instance Vue.

Vous verrez comment cela fonctionne plus en détail dans les sections futures. Mais pour l'instant, voici un court résumé des hooks disponibles et de ce qu'ils vous permettent de faire :

- beforeCreate (vous pouvez exécuter du code avant la création de l'instance Vue)
- created (vous pouvez exécuter du code après la création de l'instance Vue)
- beforeMount (vous pouvez exécuter du code avant que votre élément ne soit monté dans le DOM)
- mounted (vous pouvez exécuter du code lorsque l'élément est monté dans le DOM)
- beforeUpdate (vous pouvez exécuter du code avant que les valeurs ne soient mises à jour dans le DOM)
- updated (vous pouvez exécuter du code après que les valeurs dans le DOM ont été mises à jour)
- beforeDestroy (vous pouvez exécuter du code avant qu'une instance ne soit détruite)
- destroyed (vous pouvez exécuter du code lorsqu'une instance est détruite)

Pendant le cours, nous utiliserons souvent le hook mounted. Si vous êtes curieux d'en savoir plus sur ce sujet, je vous suggère de regarder d'abord le diagramme dans la documentation. Trouvez le [diagramme](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram) des hooks de cycle de vie ici.


%[https://youtu.be/gBJaL7Jqh4w]

## Comment travailler avec les templates dans Vue

VueJS utilise la syntaxe mustache `{{ }}` pour afficher les données de l'instance Vue à l'intérieur de l'élément HTML.

En utilisant cette syntaxe, vous pouvez récupérer les propriétés et méthodes définies dans l'instance Vue. La propriété est ensuite analysée et rendue sur la page.

Vous pouvez cliquer pour voir le [Dépôt ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/3-work-with-templates/).

Et vous pouvez cliquer pour voir la [Vidéo-YouTube ici](https://youtu.be/pDj3SQ8TNzs) ici, ou la trouver à la fin de cette section pour revoir ce que vous venez d'apprendre.

### Liaison de données texte
C'est ce qu'on appelle la liaison de données texte (text data binding). Voyons un exemple de la façon dont vous pouvez lier des données entre l'instance Vue et votre fichier de template.

```html

<div id="app">
    <h1>{{ title }}</h1>
</div>
```
Le code ci-dessus contient une balise `h1` à l'intérieur de l'élément racine avec un id `app` que nous avons défini dans le chapitre précédent.

À l'intérieur de la balise `h1`, vous utilisez la syntaxe des doubles accolades pour afficher sur la page la valeur d'une propriété dans l'objet data que vous avez appelée `title`.

Vous n'avez pas encore de propriété `title` à l'intérieur de votre objet data, alors ajoutons-la.

À l'intérieur du fichier main.js
```js

let app = new Vue({
    el: "#app",
    data: {
        title: "Portfolio de John Doe",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "épicerie", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "script d'automatisation", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ]
    }
})

```

Maintenant, avec le code ci-dessus, vous pouvez afficher le contenu de la propriété `title` à l'intérieur de la balise `h1` dans votre template. Le résultat final sera quelque chose comme ceci :

```html
<h1>Portfolio de John Doe</h1>
```

Cependant, avec cette méthode, vous ne pouvez passer qu'une chaîne de caractères. Si vous voulez utiliser des balises HTML à l'intérieur de la chaîne, celles-ci ne seront pas analysées mais seront affichées comme de simples chaînes.

Par exemple, si vous assignez la chaîne suivante à la propriété `title` :
```js
    title: "John Doe <span class='badge'>Portfolio</span>"
```
Et que vous essayez ensuite de l'afficher dans notre HTML comme ceci :
```html
<h1 class="title">{{title}}</h1>
```
La propriété `title` sera affichée comme une chaîne brute incluant les balises HTML
c'est-à-dire ```John Doe <span class='badge'>Portfolio</span>```

Bien sûr, vous pouvez aussi analyser le HTML.

### Comment analyser le HTML brut
Pour afficher un élément HTML brut, nous devons introduire un autre concept important de Vue appelé les directives.

Dans ce cas, vous utiliserez la directive v-html à l'intérieur de votre balise HTML en tant qu'attribut et lui passerez la propriété title.

Lorsque vous utilisez des directives Vue, le texte à l'intérieur des guillemets est considéré comme une expression JavaScript. Cela signifie qu'il est calculé et que son résultat est affiché.

Créons une propriété séparée pour le titre avec des balises HTML à l'intérieur afin que vous puissiez voir comment les deux s'affichent sur la page.

```js
let app = new Vue({
    el: "#app",
    data: {
        title: "Portfolio de John Doe", 
        titleHTLM : "John Doe <span class='badge'>Portfolio</span>",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "épicerie", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "script d'automatisation", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ]
    }
})

```
Maintenant, à l'intérieur de votre fichier HTML, vous utiliserez cette syntaxe `{{}}` pour afficher la propriété `title`. Mais sur la balise où vous voulez afficher du HTML brut, avec la propriété `titleHTML`, vous utilisez la directive v-html à la place.

```html
<div id="app">
    <div class="title">{{ title }}</div>
    <div v-html="titleHTML"></div>
</div>
```
Les deux éléments s'afficheront désormais correctement, y compris la deuxième propriété qui contient des balises HTML.

NOTE : L'affichage du HTML peut exposer à des vulnérabilités XSS. N'utilisez jamais cette approche sur du contenu fourni par l'utilisateur.

Maintenant que vous savez comment afficher des données sur la page, approfondissons les directives.

Si vous voulez en savoir plus, visitez la documentation
[ici](https://vuejs.org/v2/guide/syntax.html#Using-JavaScript-Expressions).


%[https://youtu.be/pDj3SQ8TNzs]



## Directives Vue 

À l'intérieur de vos fichiers HTML, vous pouvez utiliser des directives pour interagir avec les attributs HTML. Une directive applique des effets au DOM lorsque son expression change.

Vous pouvez cliquer pour voir le [Dépôt ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/4-Directives/)

And you can click to view the [YouTube-Video here](https://youtu.be/LICvNmhsTEs), or you can find it at the end of this section to review what you've learned.

### La directive v-bind sur les attributs HTML
Jusqu'à présent, vous avez utilisé la syntaxe `{{}}` pour afficher quelque chose entre les balises HTML d'ouverture et de fermeture. Mais à l'intérieur d'une balise HTML, vous ne pouvez pas utiliser la syntaxe {{ }}.

Alors, comment connectez-vous un attribut HTML à l'instance Vue ? Vous utilisez la directive v-bind à la place, qui vous permet d'accéder aux propriétés de l'objet data comme vous l'avez fait auparavant.

La directive v-bind est l'une des directives qui prennent des arguments spécifiés après les deux-points. Dans notre cas ici, ce qui est spécifié après les deux-points est le nom de l'attribut HTML comme id, class, href, src, etc.

Si vous avez besoin d'assigner dynamiquement un attribut comme href ou même une classe, vous pouvez le lier à l'instance Vue en utilisant la directive v-bind. Elle pourra alors récupérer ce qui se trouve dans l'objet options, comme les propriétés de l'objet data.

Voyons v-bind en action et commençons par connecter les attributs `id` et `class` afin de pouvoir leur assigner des valeurs dynamiquement avec Vue.

À l'intérieur de notre fichier index.html :
```html
<div id="app">
    <div v-bind:class="dynamicClass" v-bind:id="dynamicId">Assigner dynamiquement une classe et un id au div</div>
</div>
```
Décortiquons le code ci-dessus et voyons ce qu'il fait.

Tout d'abord, vous avez une balise `div` à l'intérieur de l'élément racine. Ensuite, vous utilisez la directive v-bind sur les attributs class et id.

À l'intérieur des guillemets, vous spécifiez deux propriétés que vous définirez plus tard à l'intérieur de l'objet data de votre instance Vue.

N'oubliez pas que lors de l'utilisation des directives Vue, le contenu entre guillemets est traité comme une expression JavaScript.

Définissons ces deux propriétés à l'intérieur de l'instance Vue.
```js
let app = new Vue({
    el: "#app",
    data: {
        title: "Portfolio de John Doe", 
        titleHTLM : "John Doe <span class='badge'>Portfolio</span>",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "épicerie", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "script d'automatisation", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ],
        dynamicId : "projects_section",
        dynamicClass : "projects"
    }
})


```
Vous avez donc défini les propriétés `dynamicId: "projects_section"` et `dynamicClass: "projects"` et leur avez assigné deux valeurs.

Grâce à la liaison de données sur les attributs, votre balise HTML sera rendue comme suit (et vous pouvez maintenant changer dynamiquement les valeurs de vos attributs et les voir changer de manière réactive) :

```html
<div id="projects_section" class="projects">Assigner dynamiquement une classe et un id au div</div>
```

### V-bind avec des valeurs booléennes
Avec les attributs utilisant une valeur booléenne, la directive v-bind fonctionne différemment. Elle affichera l'attribut uniquement si la valeur de la propriété est vraie. Dans tous les autres cas, elle n'affichera pas l'attribut et son contenu.

Pour l'exemple suivant, vous utiliserez un bouton avec l'attribut disabled.

À l'intérieur de votre élément HTML racine :
```html
    <div id="app">
        <button v-bind:disabled="disabled">Vous ne pouvez pas cliquer sur ce bouton</button>
    </div>
```
À l'intérieur d'une instance Vue :
```js
let app = new Vue({
    el: '#app',
    data: {
    //disabled: false, // n'affichera pas l'attribut
    //disabled: null, // n'affichera pas l'attribut
    //disabled: undefined, // n'affichera pas l'attribut
    disabled: true // affiche l'attribut
}
})

```

Ce n'est que si la propriété disabled est définie sur true que l'attribut devient visible et affiche le contenu de sa propriété.
```html
    <button disabled>Vous ne pouvez pas cliquer sur ce bouton</button>
```
C'est quelque chose à garder à l'esprit lors de l'utilisation de tels attributs.

Une autre chose à considérer est que les liaisons peuvent inclure une seule expression JavaScript, avec quelques restrictions :
- seules les expressions sont autorisées
- une seule expression
- pas d'instructions (statements)
- pas d'outils de contrôle de flux, mais l'opérateur ternaire fonctionne.

Si vous voulez en savoir plus, visitez la documentation
ici : [https://vuejs.org/v2/guide/syntax.html#Using-JavaScript-Expressions]

Jusqu'à présent, nous n'avons vu que deux directives Vue, v-html et v-bind. Mais il existe de nombreuses directives disponibles, et en voici quelques autres (pour n'en citer que quelques-unes) :
- v-html
- v-bind
- v-if
- v-else-if
- v-else
- v-for
- v-on
Toutes les directives ont un préfixe v-, mais il existe des raccourcis pour v-bind (:) et v-on (@).

Elles fonctionnent de la même manière. Voici une référence rapide pour les directives v-bind et v-on :
```html
<!-- Syntaxe longue -->
<a v-bind:href="url">Un lien</a>
<!-- Syntaxe courte -->
<a :href="url">Un lien</a>
<!-- Syntaxe longue avec arguments dynamiques -->
<a v-bind:[attribute_name]="url">Un lien</a>
<!-- Syntaxe courte avec arguments dynamiques -->
<a :[attribute_name]="url">Un lien</a>
```
Raccourci pour v-on
```html
<!-- Syntaxe longue -->
<a v-on:click="runFunction">Un lien</a>
<!-- Syntaxe courte -->
<a @click="runFunction">Un lien</a>
<!-- Syntaxe longue avec arguments dynamiques -->
<a v-on:[attribute_name]="runFunction">Un lien</a>
<!-- Syntaxe courte avec arguments dynamiques -->
<a @:[attribute_name]="runFunction">Un lien</a>

```
Voyons maintenant ce que sont les arguments dynamiques et comment ils fonctionnent.

### Arguments dynamiques dans Vue
Les directives peuvent avoir des arguments dynamiques depuis Vue 2.6.0. Vous pouvez utiliser une expression JavaScript dans l'argument de la directive si vous l'enveloppez entre crochets.

Mais il y a quelques restrictions :
- les expressions doivent s'évaluer en une chaîne de caractères
- les espaces et les guillemets sont invalides

Voyons un exemple pratique
```html
    <a v-bind:[attribute_name]="url">Visitez mon site Web</a>
```
À l'intérieur de votre objet data, vous pouvez définir les arguments de la directive comme s'il s'agissait de propriétés, où la valeur de la propriété est le nom de votre attribut HTML comme `href` dans l'exemple suivant :

```js
let app = new Vue({
    el: '#app',
    data: {
        attribute_name: 'href',
        url: 'https://fabiopacifici.com'
    }
})

```
Le code ci-dessus affiche le nom de l'attribut `href` et sa valeur dynamiquement lorsque vous le liez en utilisant la directive v-bind.

Le résultat sera celui-ci :
```html
<a href="https://fabiopacifici.com">Visitez mon site Web</a>
```

### Événements dynamiques dans Vue
Vous pouvez appliquer le même concept aux directives d'événements comme v-on. Cette directive fait le travail de l'écouteur d'événements JavaScript.

v-on accepte un argument comme click, par exemple `v-on:click="doSomething"`.

Pour appliquer le concept de dynamicité, créons une directive v-on et utilisons les crochets après elle pour spécifier un événement dynamique.

À l'intérieur du fichier index.html, vous placerez le code suivant :
```html
    <div id="app">
        <a v-on:[event_name]="runFunction">Un lien</a>
    </div>
```
Décortiquons le code ci-dessus.

Tout d'abord, vous avez votre élément racine, le `div` avec un `id` `app`. À l'intérieur de l'élément racine, vous ajoutez une balise d'ancre `<a>Un lien</a>`.

La balise d'ancre contient une directive `v-on`. Après la directive, vous spécifiez un argument dynamique `v-on:[event_name]` où `event_name` sera une propriété à l'intérieur de votre instance Vue que vous pourrez modifier selon vos besoins.

La directive v-on fonctionne comme n'importe quel écouteur d'événements, donc entre guillemets, vous devez spécifier le nom de la fonction que vous voulez exécuter lorsque l'événement est déclenché, ici `runFunction`.

Maintenant, à l'intérieur de votre fichier main.js :
```js
let app = new Vue({
    el: '#app',
    data: {
    event_name: "click"
    },
    methods: {
        runFunction() {
            console.log("test de la fonction click");
        }
    }
})
```
Passons en revue ce que fait le code ci-dessus.

Tout d'abord, vous créez l'instance Vue. Ensuite, vous ajoutez la propriété `event_name` à l'intérieur de l'objet data et vous lui assignez une valeur de `click`. C'est l'événement que vous allez écouter.

Enfin, nous avons dit que la directive v-on exécute une fonction lorsque l'événement est déclenché, vous devez donc écrire une méthode à l'intérieur de votre instance Vue. Ainsi, à l'intérieur de l'objet methods, créez une nouvelle fonction appelée `runFunction` qui affichera simplement un message dans la console.

La puissance des événements dynamiques est évidente lorsque vous remplacez la valeur de la propriété `event_name` par un nom d'événement différent.


%[https://youtu.be/LICvNmhsTEs]

## Méthodes dans Vue

Jusqu'à présent, nous avons appris à lier des données en utilisant la directive v-bind à l'intérieur de votre template. Dans la section suivante, vous apprendrez d'autres directives – mais avant d'aborder cela, parlons rapidement de la façon de stocker vos fonctions.

Vous pouvez consulter le [Dépôt ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/5-Methods/)

Et vous pouvez voir la version vidéo de cette section sur [YouTube](https://youtu.be/dESmaEvkZ2I) si vous souhaitez revoir ce que vous apprenez.

Puisque vous travaillez dans un grand objet, la fonction de l'instance Vue prendra le nom des méthodes. Et comme vous pouvez le deviner, l'objet Options possède une propriété appelée `methods` où vous pouvez stocker vos fonctions comme vous le faites pour vos données.

À l'intérieur de votre instance Vue, définissez une méthode que vous pouvez appeler comme vous le souhaitez – n'oubliez pas d'utiliser une convention de nommage qui décrit clairement votre code.

```js

let app = new Vue({
    el: '#app',
    data: {
        firstName: "Fabio",
        lastName: "Pacific"
    },
    methods: {
        // syntaxe es6
        getFullName(){
            return this.firstName + " " + this.lastName;
        }
        // syntaxe es5
    /* getFullName: function(){

        } */
    }
});

```
Dans le code ci-dessus, vous avez créé une méthode à l'intérieur de l'objet methods. Vous l'avez appelée `getFullName`. À l'intérieur d'une méthode, vous avez accès au mot-clé `this` qui fait référence à l'instance de l'objet, vous pouvez donc l'utiliser pour accéder depuis une méthode aux propriétés stockées dans l'objet data.

Lorsque vous appelez la méthode `getFullName`, la méthode renverra une seule chaîne de caractères contenant à la fois le prénom et le nom.

Maintenant, à l'intérieur de votre fichier HTML, vous pouvez simplement appeler la méthode comme vous le faisiez lorsque vous aviez besoin d'accéder aux propriétés de l'objet data `{{ getFullName() }}`

```html
<div>{{ getFullName() }}</div>
```
Maintenant que vous savez comment créer une méthode et où la placer dans l'instance Vue, avançons et apprenons-en plus sur les directives.


%[https://youtu.be/dESmaEvkZ2I]

## Conditionnels dans Vue (v-if/v-else-if/v-else/v-show)
 
Il est maintenant temps d'en apprendre davantage sur les directives. Nous commencerons par examiner le fonctionnement des conditionnels dans VueJS. La première directive de cette section est le `v-if`, qui vous permet de rendre des blocs de code basés sur une certaine condition.

Vous pouvez cliquer pour voir le [Dépôt ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/6-Conditionals/]).

Et vous pouvez cliquer pour voir la vidéo sur [YouTube ici](https://youtu.be/VNaCsloA1ZU) ou l'utiliser pour réviser à la fin de la section.

Comme les instructions `if-else` en JavaScript pur, le v-if vérifiera si la valeur renvoyée par une expression conditionnelle s'évalue à vrai. Si c'est le cas, il affichera l'élément HTML et tout ce que vous placez à l'intérieur.

Puisqu'il s'agit d'une directive, elle fonctionne sur un seul élément (balise HTML). Si vous souhaitez étendre son comportement à plusieurs éléments, vous devez les envelopper dans une balise `<template>`.

La directive v-if fonctionne de la même manière que la directive v-bind : elle a accès aux propriétés de l'objet data et accepte une expression entre ses guillemets.

Si la valeur renvoyée par l'expression ou la valeur de la propriété de données que vous utilisez s'évalue à `true`, alors la directive affiche l'élément HTML. Sinon, elle ne le fait pas.

Bien sûr, vous pouvez vérifier plusieurs conditions et finir par afficher un élément si aucune d'entre elles ne s'évalue à vrai. Vous le faites en utilisant v-if avec les directives v-else-if et v-else.

Voyons un exemple simple et écrivons du code à l'intérieur de votre fichier main.js pour afficher ou masquer un élément.

La première chose à noter est que si vous avez une propriété qui renvoie une valeur booléenne, il suffit de l'utiliser à l'intérieur de la directive v-if pour afficher/masquer un élément, comme ceci :

```html
<h1 v-if="showTitle">{{movieTitle}}</h1>
```
Et une instance vue avec une propriété showTitle définie sur true.
```js

let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        showTitle: true,
    }
})
```
Dans un tel cas, vous dites d'afficher la propriété title uniquement si la valeur de `showTitle` est `true`. Si vous la changez en false, le titre ne s'affichera pas.

Vous pouvez mettre une expression simple à l'intérieur des guillemets d'une directive v-if qui, une fois calculée, s'évalue en un booléen.
```html
<h2 v-if="age >= 18">{{movieTitle}}</h2>

```
À l'intérieur de votre fichier main.js
```js 
let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        age: 18,
    }
})
```
Dans le code ci-dessus, nous avons écrit une expression sur la directive v-if qui vérifie si la propriété `age` est supérieure ou égale à 18. Si le résultat est vrai, alors le `h2` sera affiché sur la page.

Passons maintenant à un exemple plus complexe et ajoutons une autre condition en utilisant le v-else-if.

#### v-if/v-else-if
Dans l'exemple suivant, vous allez d'abord créer une condition v-if similaire à celle ci-dessus – mais cette fois vous vérifierez si l'utilisateur a plus de 18 ans mais moins de 21 ans en utilisant l'opérateur `&&`.

Si c'est vrai, vous afficherez l'heure avec une note supplémentaire. Si c'est faux, et que l'utilisateur a plus de 21 ans, alors nous afficherons simplement le titre du film.
```html
<h2 v-if="age > 21">{{movieTitle}}</h2>
<h2 v-else-if="age > 18 && age < 21"> {{ movieTitle }} | À regarder avec un adulte</h2>
```
À l'intérieur de l'instance Vue, vous pourriez avoir une propriété `age`. Mais pour rendre votre programme simple dynamique, vous pouvez à la place utiliser un prompt pour demander l'âge de l'utilisateur.

```js
let userAge = Number(prompt("Quel est votre âge ?"))
let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        age: userAge,
    }
})
```
Le code ici demande d'abord à l'utilisateur son âge, puis stocke le résultat sous forme de nombre dans la variable `userAge`.

Vous utiliserez plus tard la variable `userAge` à l'intérieur de l'objet data pour assigner une valeur à la propriété `age` afin qu'en fonction de sa valeur, vous affichiez un élément ou l'autre.

Avançons et utilisons la directive v-else pour afficher un message différent au cas où l'utilisateur aurait moins de 18 ans.

#### directive v-else :
La directive `v-else` fonctionne différemment. Vous n'avez rien à lui passer. Elle entre simplement en action lorsqu'aucune des conditions précédentes ne s'évalue à une valeur vraie.

Le nouvel élément HTML est donc assez simple :

```html
    <div id="app">
        <h2 v-if="age > 21">{{movieTitle}}</h2>
        <h2 v-else-if="age > 18 && age < 21"> {{ movieTitle }} | À regarder avec un adulte</h2>
        <p v-else> Désolé, vous êtes trop jeune pour voir ce film</p>
    </div>

```

Ici, nous avons une balise `p` avec une directive v-else attachée. Comme vous pouvez le voir, cela ressemble à un attribut sans valeurs (comme les attributs HTML disabled ou required).

Votre fichier JavaScript n'a pas changé.
```js

let userAge = Number(prompt("Quel est votre âge ?"))
let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        age: userAge,
    }
})
```

C'est tout ce que vous devez savoir sur le rendu conditionnel pour pouvoir avancer avec votre premier projet. Mais si vous voulez en savoir plus, voici la documentation : [https://vuejs.org/v2/guide/conditional.html]

Vous devez apprendre encore quelques choses avant de pouvoir construire votre premier projet, qui est un clone simplifié de Twitter. Le sujet suivant concerne les boucles.


%[https://youtu.be/VNaCsloA1ZU]

## Boucles dans Vue

Revenons à l'exemple précédent et apprenons à utiliser la directive v-for pour afficher chaque projet du tableau sur la page.

Vous pouvez cliquer pour voir le Dépôt [ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/7-loops/)

Et vous pouvez cliquer pour voir la Vidéo-YouTube [ici](https://youtu.be/aViHg80-7Bs), ou vous pouvez la trouver à la fin de cette section pour revoir ce que vous avez appris.

Pour notre prochaine tâche, il serait utile de pouvoir utiliser une boucle, et la directive v-for est là pour nous aider.

Sa syntaxe n'a pas grand-chose en commun avec une boucle `for` classique en JavaScript, mais plutôt avec une boucle `for in` Python ou avec la boucle `for in` JavaScript utilisée pour itérer sur des objets.

Avec cette directive, vous spécifiez les éléments du tableau et l'élément unique entre guillemets en utilisant la syntaxe `project in projects`. Ici, projects est la propriété à l'intérieur de l'objet data qui contient un tableau d'objets, et project est l'élément unique du tableau.

Vous pouvez appeler cela comme vous le souhaitez, mais gardez à l'esprit que ce qui suit le mot-clé `in` doit être un itérable de votre objet data tandis que ce qui précède peut être tout ce que vous voulez pour vous référer à chaque élément de l'itérable.

Dans votre cas, project semble le choix le plus approprié puisque vous avez un tableau de projets.

Votre fichier JavaScript ressemblera à ceci :
```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "épicerie", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "script d'automatisation", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ],
        
    }

});
```
Maintenant, à l'intérieur du fichier HTML, utilisons le v-for pour afficher le titre de chaque projet.
```html
    <div id="app">
        <h1>{{name}} {{title}}</h1>
        <ul>
            <li v-for="project in projects">{{project.title}}</li>
        </ul>
    </div>
```
Dans le code ci-dessus, vous avez utilisé `{{name}} {{title}}` pour afficher le titre principal de votre portfolio. Ensuite, vous avez utilisé la directive v-for et spécifié à l'intérieur des guillemets que vous voulez assigner chaque élément de l'itération à une variable project `v-for="project in projects"`.

Maintenant, à chaque itération, la variable `project` contient un objet à partir duquel vous pouvez récupérer ses propriétés en utilisant la notation par points comme ceci : `{{ project.title }}`.

Une chose à noter est que la directive v-for vous donne également accès à l'index de l'élément à chaque itération. Vous pouvez le stocker dans une variable comme vous l'avez fait avec l'élément unique que vous avez appelé project.

Pour ce faire, vous devez les envelopper entre parenthèses et séparer l'élément et son index par une virgule, comme ceci `v-for="(project, index) in projects"`.

Notez également que lors de l'utilisation d'objets, Vue peut afficher une alerte pour vous informer que l'utilisation d'une clé est recommandée. Cela signifie qu'il attend une clé pour identifier chaque élément lorsqu'il est rendu.

Vous pouvez le faire en utilisant l'attribut `key` et en le liant, par exemple à une propriété id sur l'objet ou à une autre propriété différente, comme ceci

```html

<div id="app">
    <h1>{{name}} {{title}}</h1>
    <ul>
        <li v-for="project in projects" :key="project.title">{{project.title}}</li>
    </ul>
</div>
```
Ici, vous avez utilisé la directive raccourcie v-bind pour lier l'attribut key à la propriété project.id si elle existe ou à une autre propriété sinon.

```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "épicerie", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "script d'automatisation", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ],
        
    }

});

```

v-for peut également être utilisé pour itérer sur des objets. Dans ce cas, vous avez accès à la valeur, à la clé, ainsi qu'à l'index comme ceci `v-for="(value, key, index) in object"` où 'object' est une propriété dans l'objet data.

Si vous voulez en savoir plus, visitez la documentation ici : [https://vuejs.org/v2/guide/list.html]

Passons maintenant à une autre fonctionnalité importante de Vue : comment gérer les entrées utilisateur et les événements.


%[https://youtu.be/aViHg80-7Bs]



## Comment gérer les entrées utilisateur avec la gestion des événements (v-on) dans Vue
 
Pour rendre l'application réactive à une entrée de l'utilisateur, Vue fournit une directive simple appelée `v-on`. C'est l'une des directives qui acceptent des arguments, similaire à la directive v-bind.

Avec une telle directive, il est facile d'écouter les événements déclenchés par un utilisateur.

La directive v-on vous permet d'exécuter une fonction qui exécute un bloc de code lorsque l'utilisateur effectue une action, comme lorsqu'il clique sur un bouton, survole un élément ou appuie sur une touche spécifique du clavier.

Vous pouvez consulter le [Dépôt ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/8-user-inputs-events-handling/).

Et vous pouvez voir la vidéo sur [YouTube ici](https://youtu.be/9_U1eagqOJY) ou à la fin de cette section pour revoir ce que vous avez appris.

### Syntaxe et événements V-on
Il existe deux types de syntaxe que nous pouvons utiliser, la forme longue ou la courte. Elles sont équivalentes, alors choisissez celle que vous préférez. Ce qui suit n'est qu'une représentation de la syntaxe, et je l'expliquerai en détail dans une minute.

Syntaxe longue : `v-on:EventName='doSomething' `
Syntaxe courte : `@EventName='doSomething'`

Il existe de nombreux événements que vous pouvez écouter, tels que :
- click
- submit
- mouseover
- mouseenter
- mouseleave
- keyup
- keydown
- keypress

Mais vous pouvez aussi créer des événements personnalisés (que vous verrez lorsque vous atteindrez la section des composants).

Prenons la syntaxe de forme longue : `v-on:EventName='doSomething`. Je vais l'expliquer davantage maintenant.

Tout d'abord, vous avez la directive `v-on`. Ensuite, vous avez un argument qui est le nom de l'événement que vous voulez écouter, comme `click`. Après cela, le `doSomething` peut être n'importe quelle méthode que vous avez définie à l'intérieur de l'objet methods de l'instance Vue.

Cette méthode est comme toute autre fonction que vous définissez à l'intérieur d'un objet JavaScript. Elle peut avoir des paramètres ou non. Si elle en a, vous pouvez appeler la méthode et lui passer des paramètres comme d'habitude comme ceci : `doSomething(param, param_2, param3)`.

Vous pouvez avoir quelque chose comme ceci `<div v-on:click="likeProject">J'aime</div>` et lorsque l'utilisateur clique sur cet élément, cela déclenchera une méthode et exécutera du code pour augmenter un compteur de likes à l'intérieur d'un projet.

Créons d'abord le HTML dont vous avez besoin pour cela :
```html
<div class="projects" v-for="(project,index) in projects">
    <h1>{{project.title.toUpperCase()}}</h1>
    <p>Lorem ipsum dolor sit amet.</p>
    <div>J'aime
        <i class="fas fa-heart fa-lg fa-fw" @click="likeProject(index)">
        </i>
        {{project.likes}}
    </div>
</div>

```
Dans le code ici, vous utiliserez d'abord la directive v-for pour boucler sur le tableau de projets. Notez que vous devez utiliser la syntaxe `(project, index) in projects` car vous devrez passer l'index à la méthode like que vous avez définie précédemment.

Après cela, vous affichez des données sur la page (comme le nom du projet en lettres majuscules) puis la description, et une balise `div` avec une icône pour les likes (n'oubliez pas d'ajouter font awesome pour obtenir l'icône).

Sur l'icône du cœur, ajoutez la directive v-on en utilisant la syntaxe courte `@click="likeProject(index)"` entre guillemets que vous avez utilisée pour invoquer votre méthode `likeProject(index)`. Passez-lui ensuite l'index en paramètre afin de pouvoir trouver le projet actuel sur lequel l'utilisateur a cliqué.

Enfin, vous afficherez les likes sur la page pour le projet actuel en utilisant la syntaxe `{{project.likes}}`.


Il est maintenant temps d'aller dans l'instance Vue et d'écrire votre méthode.
```js

let app = new Vue({
    el:"#app",
    data: {
        projects: [
            {title: "Mon premier projet", description: "Un clone de Twitter simplifié", likes: 0},
            {title: "Mon second projet", description: "Portfolio de projets avec GitHub", likes: 0},
        ]
    },
        methods: {
            likeProject(index){
                const project = this.projects[index]
                project.likes++
                console.log(project.likes)
            }
        
    }
});

```
Comme je l'ai dit plus tôt, vous deviez définir une méthode à appeler lorsque l'utilisateur clique sur un lien. Vous créez donc la méthode `likeProject`, qui accepte un paramètre qui sera l'index de l'élément sur lequel l'utilisateur a cliqué.

Vous pouvez ensuite ajouter une propriété likes à l'intérieur de votre tableau projects et y accéder pour le projet actuel afin d'incrémenter sa valeur chaque fois que l'utilisateur clique sur votre lien.


### Comment accéder à l'événement original
Si pour une raison quelconque vous avez besoin d'accéder à l'événement DOM original, vous auriez pu utiliser la variable spéciale `$event` à l'intérieur de la méthode comme ceci sur la directive v-on : `doSomething(param1, param2, $event)`. Voyons un exemple de cela maintenant.

Vous devez ajouter la variable spéciale dans l'appel de la méthode sur votre directive v-on comme ceci :
```html
<i class="fas fa-heart fa-lg fa-fw" @click="likeProject(index, $event)">
        </i>
```
Ensuite, vous pouvez accéder à l'événement original à l'intérieur de votre méthode comme ceci :
```js
likeProject(index, event){
    console.log(event); // obtenir l'événement original
    const project = this.projects[index]
    project.likes++
    console.log(project.likes)
}
```

Maintenant que vous savez comment fonctionne la directive v-on, améliorons notre exemple de Likes et mettons-y quelque chose de plus. Nous utiliserons des modificateurs de touches dans l'exemple suivant, alors voyons rapidement ce qu'ils sont et ce que vous pouvez faire avec eux.

### Modificateurs d'événements dans Vue
Avec les événements, Vue permet d'accéder à un certain nombre de modificateurs d'événements. Ils sont divisés en 4 groupes principaux. Vous pouvez ajouter ces modificateurs à une directive pour changer la façon dont votre événement se comporte. Ils sont comme des suffixes et vous pouvez les chaîner en utilisant la notation par points.

Ci-dessous se trouve une référence rapide.

Catégories :
- modificateurs d'événements
- modificateurs de touches
- touches de modificateurs système
- modificateurs de boutons de souris

Modificateurs d'événements :
.stop
.prevent 
.capture
.self
.once
.passive

Modificateurs de touches :
Vous pouvez ajouter ces modificateurs à l'écouteur @keyup pour écouter quand ces touches sont pressées ou les utiliser en combinaison avec l'événement @click pour écouter un clic+espace, par exemple. `@click.enter="doSomething"`

.enter
.tab
.delete (capture à la fois les touches "Suppr" et "Retour arrière")
.esc
.space
.up
.down
.left
.right

Modificateurs système :
Avec ces modificateurs, vous pouvez déclencher des écouteurs d'événements de souris ou de clavier lorsque la touche correspondante est pressée.
.ctrl 
.alt
.shift
.meta
.exact (permet de contrôler la combinaison exacte de modificateurs système nécessaires pour déclencher un événement)

Modificateurs de boutons de souris :
Ces modificateurs vous permettent de déclencher un écouteur d'événement de souris si le bouton de souris correspondant est cliqué.

.left
.right
.middle

Si vous voulez en savoir plus, lisez la documentation [ici](https://vuejs.org/v2/guide/events.html#Event-Modifiers).


### Comment aimer un projet avec des modificateurs de touches
Dans l'exemple précédent, vous avez utilisé la directive v-on:click pour déclencher un écouteur d'événement de souris qui visait à simuler un like sur un projet.

Mais l'utilisateur pouvait ajouter autant de likes qu'il le souhaitait en cliquant sur l'icône.

Dans l'exemple suivant, vous allez faire les choses un peu différemment.
- Tout d'abord, vous empêcherez l'utilisateur d'ajouter plus d'un like à chaque projet,
- Ensuite, vous permettrez à l'utilisateur de supprimer un like
- Enfin, vous conserverez les likes sur la page même après que l'utilisateur a rafraîchi la page.

Commençons. Cette fois, vous utiliserez des modificateurs de boutons de souris pour écouter les clics. Le clic gauche de la souris déclenchera le comportement d'ajout de like et le clic droit de la souris déclenchera le comportement de suppression.

À l'intérieur de votre fichier HTML :
```html
<div id="app">
    
    <!-- Les utilisateurs peuvent aimer un projet avec un clic gauche et ne plus l'aimer avec un clic droit -->

        <div class="projects" v-for="project in projects">
            <h1>{{project.title.toUpperCase()}}</h1>
            <p>Lorem ipsum dolor sit amet.</p>
            <div>J'aime 
                <i class="fas fa-heart fa-lg fa-fw" 
                    @click.left="addLike(project)" 
                    @click.right="removeLike(project, $event)">
                </i> 
               {{project.likes}}
            </div>
        </div>


</div>
```

Dans le code ci-dessus, vous avez repris ce que vous aviez auparavant et avez simplement ajouté un modificateur de touche de bouton gauche de la souris à l'événement click `@click.left`. Ensuite, vous avez invoqué la méthode `addLike`. Cela fera augmenter le compteur de likes de votre projet de un comme nous l'avons vu auparavant.

Ensuite, vous avez ajouté un autre écouteur d'événement au même élément, mais cette fois vous avez utilisé le modificateur de touche de bouton droit de la souris `.right` pour écouter quand l'utilisateur clique sur notre icône en utilisant le bouton droit `@click.right="removeLike()"`.

Dans la méthode remove like, vous avez également passé la variable spéciale $event afin de pouvoir utiliser l'événement original plus tard dans votre méthode pour empêcher son comportement par défaut et ouvrir le menu contextuel.

Mais nous avons dit plus tôt que vous pouvez également chaîner les modificateurs de touches et qu'il existe en effet un modificateur de touche `.prevent` que vous pouvez utiliser ici au lieu de la variable `$event`. Vous pourriez faire la même chose comme ceci : `@click.right.prevent="removeLike(project)"`

Voyons comment structurer votre fichier main.js :
 
```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "Mon premier projet", description: "Un clone de Twitter simplifié", likes: 0},
            {title: "Mon second projet", description: "Portfolio de projets avec GitHub", likes: 0},
        ]
    },
    methods: {
        addLike(project){
           console.log(project)  
        },
        removeLike(project, event){
            console.log(project)
            console.log(event)
        }
    }

});
```
Ainsi, dans l'objet data, vous avez une propriété `projects` qui est un tableau d'objets. Chaque objet possède une propriété likes que vous incrémenterez ou décrémenterez selon le bouton de souris sur lequel l'utilisateur clique.

À l'intérieur de l'objet `methods`, vous avez créé les deux méthodes que vous avez référencées dans vos directives v-on `addLike()` et `removeLike()`. Pour l'instant, vous ne faites qu'enregistrer dans la console la valeur du paramètre project et la valeur de l'événement. Vous implémenterez la logique dans une minute.

Commençons par la méthode d'ajout de likes – elle pourrait ressembler à ceci :
```js
addLike(project){
    const projectTitle = project.title;
    if(!localStorage.getItem(projectTitle)) {
        project.likes++;
        localStorage.setItem(projectTitle, true);
    }              
}
```
Il se passe quelques choses ici. Dans la première ligne, vous stockez le titre du projet dans la variable `projectTitle`. Ensuite, vous avez dit que vous vouliez que les données persistent si vous rafraîchissez la page, vous utilisez donc l'API `localStorage` pour stocker des informations dans le navigateur du client.

Vous incrémentez le compteur de likes de un, mais vous le faites en fonction d'une valeur à l'intérieur du stockage local.

Vous pouvez le faire en vérifiant d'abord s'il existe une clé dans le `localStorage` correspondant au titre de votre projet, `if(!localStorage.getItem(projectTitle))`.

Si cela s'évalue à faux, alors vous exécuterez le code à l'intérieur du bloc if et incrémenterez d'abord les likes `project.likes++`.

Deuxièmement, utilisez la méthode `.setItem()` de l'API de stockage local pour définir une paire clé-valeur avec le titre du projet comme clé et une valeur booléenne comme valeur `localStorage.setItem(projectTitle, true)`.

Pour mettre un élément dans le stockage local, vous utiliserez `localStorage.setItem()`. La méthode set item accepte une paire clé-valeur. Votre clé sera le titre que vous avez enregistré dans la variable `projectTitle` et la valeur sera la valeur booléenne `true`.

Voyons maintenant si cela fonctionne.

```js
removeLike(project, event){
    event.preventDefault(); // Ceci peut être omis si nous utilisons le modificateur de touche prevent
    const projectTitle = project.title;
    if(project.likes > 0 && localStorage.getItem(projectTitle)) {
        project.likes--;
        localStorage.removeItem(projectTitle);
    }
}
```
Cette fonction fait le contraire de la précédente. Lorsque l'utilisateur clique sur le bouton droit de sa souris, la méthode `removeLikes()` est exécutée et vous faites ce qui suit :

Tout d'abord, vous devez empêcher son comportement par défaut. Sinon, lorsque l'utilisateur fait un clic droit sur l'icône, le menu contextuel apparaîtra et nous ne voulons pas cela. Ainsi, vous utiliserez la méthode `event.preventDefault()` sur l'événement original qui est représenté par le paramètre `event` sur votre méthode.

Alternativement, vous pouvez omettre cela si vous utilisez le modificateur de touche prevent dans la directive v-on `@click.right.prevent="removeLike(project)`.

L'étape suivante consiste à récupérer le titre du projet. Puisque vous avez également passé un paramètre à la méthode pour représenter l'objet du projet actuel `removeLike(project, event)`, vous pouvez stocker le titre du projet dans une variable `projectTitle`.

Ensuite, vous devez effectuer quelques vérifications. Tout d'abord, vous voulez décrémenter les likes uniquement si sa valeur est supérieure à zéro. Ensuite, vous voulez vous assurer que le titre du projet est dans le stockage local en tant que clé avec une valeur.

Ainsi, dans votre condition, vous avez effectué les deux vérifications `if(project.likes > 0 && localStorage.getItem(projectTitle))`. Maintenant, si les deux conditions s'évaluent à vrai, le code à l'intérieur du bloc if peut s'exécuter.

Tout d'abord, vous supprimez le like en décrémentant sa valeur `project.likes--`. Ensuite, vous supprimez le titre du projet du stockage local en utilisant la méthode `removeItem` et lui passez la clé que vous souhaitez supprimer (qui est le titre du projet `localStorage.removeItem(projectTitle)`).

Pour tout mettre ensemble, vous devriez maintenant avoir le code suivant :

```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "Mon premier projet", description: "Un clone de Twitter simplifié", likes: 0},
            {title: "Mon second projet", description: "Portfolio de projets avec GitHub", likes: 0},
        ]
    },
        methods: {
        addLike(project)
        {
            //console.log(project, "like");
            const projectTitle = project.title;
            // vérifier si le projet actuel n'est pas dans le stockage local
            if(!localStorage.getItem(projectTitle)) {
                // définir l'élément dans le stockage et augmenter le compteur de likes
                project.likes++;
                localStorage.setItem(projectTitle, true);
            }
          
        },
        removeLike(project){ 
            const projectTitle = project.title;
            console.log(project, "dislike");  
            if(project.likes > 0 && Boolean(localStorage.getItem(projectTitle))) {
                project.likes--;
                localStorage.removeItem(projectTitle);
            }
            
        }
    },
    mounted(){
        this.projects.forEach(project => {
            if(localStorage.getItem(project.title) !== null) {
                project.likes = 1; 
            }
        });
    }

});

```

Pour faire fonctionner le code, vous devez également ajouter un hook de cycle de vie appelé mounted. Cela vous permettra d'exécuter du code lorsque l'élément racine est monté sur l'instance Vue. Avec lui, vous pouvez vérifier si le localStorage possède une clé correspondant au titre de votre projet et, si c'est le cas, mettre à jour la valeur du compteur de likes.

Et votre HTML est toujours le même :
```html
<div id="app">
    <!-- Les utilisateurs peuvent aimer un projet avec un clic gauche et ne plus l'aimer avec un clic droit -->

    <div class="projects" v-for="project in projects">
        <h1>{{project.title.toUpperCase()}}</h1>
        <p>Lorem ipsum dolor sit amet.</p>
        <div>J'aime 
            <i class="fas fa-heart fa-lg fa-fw" 
                @click.left="addLike(project)" 
                @click.right="removeLike(project, $event)">
            </i> 
            {{project.likes}}
        </div>
    </div>
</div>
```
N'oubliez pas que vous pouvez vous débarrasser de la variable `$event` passée à la méthode `removeLike` en utilisant le modificateur de touche d'événement comme ceci : `@click.right.prevent="removeLike(project)"`


Vous avez appris beaucoup de choses jusqu'à présent ! Et maintenant que vous avez vu les modificateurs de touches en action, nous pouvons passer au sujet suivant : la liaison de modèle bidirectionnelle et la directive v-model. Ensuite, nous commencerons à construire notre clone de Twitter.


%[https://youtu.be/9_U1eagqOJY]




## Liaison de modèle bidirectionnelle (v-model) dans Vue

Très bien, jusqu'à présent nous avons vu comment lier des propriétés de l'objet data à nos balises HTML et à l'intérieur des attributs,
comment boucler sur une séquence d'éléments et, comment afficher conditionnellement des éléments sur notre template avec des conditionnels.

Nous avons vu comment définir des méthodes à l'intérieur de l'objet methods afin de pouvoir effectuer des opérations plus complexes sur nos données et,
nous avons appris à travailler avec les événements en utilisant la directive v-on.

Dans la section suivante, nous verrons comment Vue ouvre un canal de communication bidirectionnel entre l'entrée d'un formulaire et une propriété définie
à l'intérieur de l'objet data. Ensuite, nous utiliserons ces connaissances pour construire notre premier projet ensemble.

Vous pouvez consulter le [Dépôt ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/9-two-way-binding/).

And you can view the video on [YouTube here](https://youtu.be/pBUXTUvDRCo) or at the end of the section if you want to review what you've learned.

### Comment fonctionne la directive v-model ?
Le v-model est une autre directive Vue. Vous pouvez l'utiliser directement, et elle est utile pour simplifier la façon dont une balise input peut communiquer
avec une propriété de l'instance Vue dans l'objet data.

Elle fonctionne comme toutes les autres directives. La principale différence est que lorsqu'elle est implémentée, votre application écoutera les changements
à l'intérieur de l'input avec cette directive v-model et mettra à jour la valeur de la propriété attachée immédiatement à l'intérieur de l'objet data et vice-versa.

C'est effectivement un canal de communication bidirectionnel entre votre template et l'instance Vue. C'est la manière de Vue d'interagir avec l'entrée utilisateur et de vous simplifier la vie en tant que développeur.

Regardons un exemple simple.

### Comment utiliser le v-model sur une balise input
Tout d'abord, vous avez besoin d'une balise input à l'intérieur de l'élément que vous avez défini comme élément racine dans l'instance Vue, le div avec un id `app`.
```html
<div id="app">
    <h2>De quoi voulez-vous tweeter aujourd'hui ?</h2>
    <input type="text" v-model="tweet" placeholder="Que se passe-t-il aujourd'hui ?">
</div>
```
Dans le HTML, vous avez une balise input, à laquelle est attachée la directive v-model en tant qu'attribut HTML. Tout ce qui se trouve entre guillemets est calculé comme une expression JavaScript, vous écrivez donc le nom d'une propriété `tweet` que vous créerez à l'intérieur de l'objet data de Vue.

Alors faisons-le.

```js
let app = new Vue({
    el: '#app',
    data: {
        tweet: ""
    }
});
```
Vous avez donc maintenant une instance Vue et, à l'intérieur, vous avez un objet data avec une propriété tweet qui a une chaîne vide comme valeur.

Si vous ouvrez la console et inspectez l'élément Vue, vous pouvez voir la liaison de données bidirectionnelle en action.

En changeant la valeur de la propriété tweet, vous mettrez immédiatement à jour la valeur à l'intérieur de la balise input et vice-versa.

Vous avez cette propriété `tweet` dans l'objet data et vous savez déjà comment afficher son contenu sur la page. Vous pouvez donc maintenant mettre à jour votre balisage et ajouter un paragraphe sous la balise input pour voir la valeur changer dynamiquement pendant que vous tapez.

```html
<div id="app">
    <h2>De quoi voulez-vous tweeter aujourd'hui ?</h2>
    <input type="text" v-model="tweet" placeholder="Que se passe-t-il aujourd'hui ?">
    <p>{{tweet}}<p>
</div>
```
C'est génial, n'est-ce pas ? Vous pouvez maintenant voir la propriété tweet changer en temps réel pendant que vous tapez.

C'est la liaison de données bidirectionnelle. Si vous modifiez directement le contenu de la propriété tweet, cela sera également reflété dans votre template.

Si vous voulez en savoir plus, assurez-vous de lire également la [Documentation](https://vuejs.org/v2/guide/forms.html) officielle.

### Comment construire une boîte de tweet 
Maintenant, montons un peu la barre et construisons quelque chose ensemble.

- Nous allons créer un simple `textarea` avec un bouton de soumission,
- Nous afficherons le nombre de caractères restants à l'utilisateur pendant qu'il tape afin qu'il puisse soumettre le formulaire sans dépasser le nombre maximum de caractères autorisés.
- Comme dans un tweet, le nombre maximum de caractères sera de 200.

#### Comment définir le balisage initial
Vous devez maintenant définir un balisage. Donc, à l'intérieur de notre fichier index.html, écrivez le code suivant :
```html
<div id="app">
    <h2>De quoi voulez-vous tweeter aujourd'hui ?</h2>
    <form v-on:submit.prevent="submitData">
       <!-- Code ici -->

    </form>
    <!-- Plus de code ici -->
</div>
```
Tout d'abord, vous avez créé votre élément racine pour l'instance Vue afin qu'elle puisse surveiller le balisage et faire sa magie.

Ensuite, vous avez créé une balise form avec un écouteur d'événement utilisant la directive v-on, qui écoute l'événement submit et exécute une fonction `submitData` que vous devez encore créer.

Vous avez également ajouté le modificateur `.prevent` afin que la page ne se rafraîchisse pas lorsque vous soumettez le formulaire.

#### Comment définir l'instance Vue et les méthodes
Définissons notre instance Vue et créons la méthode `submitData` afin de pouvoir l'utiliser plus tard lorsque vous en aurez besoin.
```js

let app = new Vue({
    el: '#app',
    data: {
        // propriétés de l'objet data ici
    },
    
    methods: {
          submitData(){
             // Code ici
        }
    },

});
```

#### Comment ajouter une zone de texte et un bouton de soumission
Maintenant, retour au HTML : ajoutons la zone de texte à l'intérieur de votre formulaire.

```html
<div id="app">
    <h2>De quoi voulez-vous tweeter aujourd'hui ?</h2>
    <form v-on:submit.prevent="submitData">
       <!-- Code ici -->
        <div class="form_group">
            <label for="tweet">Tweet</label>
            <textarea name="tweet" id="tweet" cols="80" rows="10" v-model="tweet" maxlength="200"></textarea>
            
        </div>

        <button type="submit">Tweeter</button>

    </form>
    <!-- Plus de code ici -->
</div>

```
À l'intérieur de la balise form, vous créez un label et un `textarea` pour votre boîte de tweet.
Sur le `textarea`, vous utilisez la directive v-model pour lier la valeur du `textarea` à une propriété `tweet` et vice-versa. Ainsi, quand l'un change, l'autre change aussi.

NOTE : La directive v-model est utilisée sur les éléments de formulaire comme les inputs, les zones de texte, les cases à cocher, et plus encore.

Après le `textarea`, vous placez un bouton de type submit afin que lorsqu'un utilisateur clique dessus, les données du formulaire soient envoyées à la méthode `submitData()` de votre application et que vous puissiez les traiter.

#### Comment ajouter des propriétés à l'instance Vue
Maintenant, à l'intérieur de votre fichier JavaScript, vous devez créer la propriété tweet dans l'objet data et faire quelque chose avec cette information afin de pouvoir afficher plus tard une liste de tweets envoyés.

Nous avons également dit que nous voulions limiter les caractères à 200 et afficher une erreur lorsqu'ils sont en excès.

Ajoutons donc quelques propriétés supplémentaires ici comme :
- `tweet` pour le message de tweet actuel que l'utilisateur saisit dans la zone de texte
- `tweets` pour la liste des tweets
- `max_length` pour la limite de caractères

```js

let app = new Vue({
    el: '#app',
    data: {
        tweets: [],
        tweet: "",
        max_length: 200,  
    },
    
    methods: {
          submitData(){
              /* Gérer le tweet */
        }
    },

});
```

Ainsi, avec la propriété tweets sous forme de tableau et en utilisant la liaison bidirectionnelle entre la propriété tweet et le `textarea`, vous pouvez pousser tous les tweets à l'intérieur du tableau `tweets` lorsque l'utilisateur soumet le formulaire en déclenchant la
méthode `submitData`.

#### Comment implémenter le compteur de caractères
Avant d'implémenter la méthode `submitData`, vous pouvez afficher un compteur de caractères pendant que l'utilisateur tape dans le textarea.

Implémentons cette fonctionnalité afin que l'utilisateur sache s'il peut soumettre le tweet ou non.

De retour dans le fichier HTML, vous pouvez ajouter un div avec quelques éléments span et utiliser une directive v-if pour vérifier la longueur du caractère. Il affichera le compteur tant que l'utilisateur respecte la limite de caractères, sinon il affichera un message d'erreur.

```html
<div id="app">
    <h2>De quoi voulez-vous tweeter aujourd'hui ?</h2>
    <form v-on:submit.prevent="submitData">
        <div class="form_group">
            <label for="tweet">Tweet</label>
            <textarea name="tweet" id="tweet" cols="80" rows="10" v-model="tweet"></textarea>        
        </div>

        <button type="submit">Tweeter</button>

    </form>
    <!-- Afficher les limites de caractères ici -->
    <div>
        <span v-if="tweet.length < max_length"> {{ `Max : ${tweet.length} sur ${max_length} caractères` }}
        </span>
        <span class="errorMessage" v-else>{{`Limite de caractères atteinte ! caractères en excès : ${max_length - tweet.length}`}}</span>
    </div>
    
</div>

```
Le code ci-dessus utilise la liaison de données bidirectionnelle entre la propriété tweet et le `textarea` pour savoir si l'utilisateur a atteint la limite de caractères que vous avez définie comme propriété `max_length`.

Puisque la propriété tweet est connectée au `textarea`, vous pouvez utiliser la directive `v-if` combinée avec les propriétés `tweet.length` et `max_length` pour effectuer la comparaison.

Maintenant, chaque fois que l'utilisateur tape quelque chose dans le `textarea`, la chaîne enregistrée dans la propriété `tweet` augmente d'un caractère. Ensuite, vous pouvez utiliser la propriété `.length` pour voir quelle est la longueur de la chaîne entière et la comparer à votre propriété `max_length`.

Vous utilisez la directive `v-if="tweet.length <= max_length"` pour effectuer votre comparaison. Lorsque cette comparaison renvoie vrai, l'utilisateur verra la balise span avec son contenu, le compteur.

À l'intérieur de la balise span, vous avez utilisé la syntaxe mustache pour montrer à l'utilisateur la longueur actuelle de la propriété `tweet` et la limite de caractères.

```html
<span v-if="tweet.length < max_length"> {{ `Max : ${tweet.length} sur ${max_length} caractères` }}</span>
```

Après la directive `v-if`, une directive `v-else` gère le message d'erreur que vous montrez à l'utilisateur lorsqu'il n'y a plus de caractères à utiliser.

Ici, le contenu de l'élément span affiche un message qui indique combien de caractères sont en excès en soustrayant la longueur du tweet de la propriété `max_length`.

```html
<span class="errorMessage" v-else>{{`Limite de caractères atteinte ! caractères en excès : ${max_length - tweet.length}`}}</span>
```

#### Comment soumettre le formulaire
Il ne reste plus qu'à ajouter le tweet à la liste des tweets et à les afficher sur la page lorsque l'utilisateur soumet le formulaire.

Complétons la méthode `submitData` afin que chaque fois qu'elle est exécutée, elle pousse un nouvel objet dans le tableau tweets.

À l'intérieur de l'objet methods, la méthode `submitData` ressemble maintenant à ceci :
```js
 submitData(){
    if (this.tweet.length <= this.max_length) {
        this.tweets.unshift(this.tweet);
        this.tweet = "";
    } 
}

```
La méthode ci-dessus vérifie d'abord si la longueur de la propriété `tweet` est inférieure ou égale à la propriété `max_length`. Si la condition s'évalue à vrai, vous pouvez alors ajouter le contenu du `tweet` au tableau en utilisant la méthode `unshift` (qui l'ajoute au début du tableau).

Enfin, vous devez effacer la valeur de la propriété `tweet`. Vous pouvez le faire en lui assignant à nouveau une chaîne vide.

NOTEZ que puisque vous êtes à l'intérieur d'une méthode, vous devez utiliser le mot-clé `this` pour récupérer les propriétés et éventuellement les méthodes à l'intérieur de l'instance Vue.

#### Comment afficher une liste de tweets
Maintenant, vous pouvez également afficher une liste de tweets dans votre template.

Pour ce faire, vous utiliserez une directive `v-for` et bouclerez sur le tableau `tweets` pour afficher chaque tweet.

```html
<ul>
    <li v-for="text in tweets">{{text}}</li>
</ul>

```

### Tout mettre ensemble
Le code final ressemble maintenant à ceci :

```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJs v-model</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!-- CDN Fontawesome -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <!-- CDN VueJS -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.js"></script>
    <style>

    </style>
</head>

<body>
    <div id="app" class="container">

        <h2>De quoi voulez-vous tweeter aujourd'hui</h2>

        <!-- Formulaire de tweet -->
        <form v-on:submit.prevent="submitData">

            <div class="form-group">
                <label>Tweet</label>
                <textarea class="form-control" cols="30" rows="5" v-model="tweet"></textarea>
            </div>

            <button type="submit" class="btn btn-primary">Tweeter</button>
        </form>

        <!-- Alerter l'utilisateur -->
        <div class="my-3">
            <span v-if="tweet.length < max_length">
                {{ ` Max : ${tweet.length} sur ${max_length} caractères` }}
            </span>
            <span class="alert alert-danger" v-else> {{ `Limite de caractères atteinte ! caractères en excès : ${max_length -
                tweet.length} ` }}</span>

        </div>

        <!-- Message des tweets -->
        <ul>

            <li v-for="tweet in tweets">
                {{tweet}}
            </li>
        </ul>

    </div>

    <script src="./main.js"></script>

</body>

</html>

```
Notre fichier javascript final

```js 

let app = new Vue({
    el: '#app',
    data: {
        tweet: "",
        tweets: [],
        max_length: 200        
    }, 
    methods: {
        submitData(){
            // Gérer la soumission du tweet
            if(this.tweet.length <= this.max_length){
                this.tweets.unshift(this.tweet);
                this.tweet = "";
            }
        }
    }
})


```

### Améliorations possibles

Si vous prenez ce morceau de code de votre fichier index.html, il y a quelque chose que vous pouvez faire pour nettoyer notre code...

```html
<!-- Afficher les messages de caractères max -->
<div>
    <span v-if="tweet.length < max_length"> {{ `Max : ${tweet.length} sur ${max_length} caractères` }}
    </span>
    <span class="errorMessage" v-else>{{`Limite de caractères atteinte ! caractères en excès : ${max_length - tweet.length}`}}</span>

</div>
```
Pour nettoyer ce fichier de template, nous pouvons suivre deux approches qui sont exactement les mêmes, sauf que l'une est mise en cache et l'autre non.
- Propriétés calculées (mises en cache)
- Méthodes (non mises en cache)

Dans la section suivante, nous apprendrons ce que sont les propriétés calculées et en quoi elles diffèrent des méthodes.


%[https://youtu.be/pBUXTUvDRCo]




## Propriétés calculées et méthodes

Vous devriez utiliser des propriétés calculées au lieu d'expressions dans le template pour une logique complexe qui a pour but de changer la présentation de nos données, et non les données elles-mêmes.

Si nous devons modifier les données, vous devriez utiliser des méthodes à la place. Les propriétés calculées sont mises en cache en fonction de leurs dépendances, ce qui signifie qu'elles ne seront réévaluées que lorsque leurs dépendances auront changé.

Avec les propriétés calculées, le résultat de la fonction précédemment exécutée est renvoyé si les dépendances n'ont pas changé.

Vous pouvez consulter le [Dépôt ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/10-computed-properties/) et regarder la vidéo sur [YouTube ici](https://youtu.be/VxFT6cgTHhw). La vidéo est également répertoriée à la fin de cette section afin que vous puissiez revoir ce que vous avez appris.

Dans l'exemple suivant, nous utiliserons des propriétés calculées mais nous pourrions également utiliser des méthodes. D'une manière générale, nous utilisons des propriétés calculées lorsque nous avons une opération coûteuse que nous voulons exécuter et mettre en cache afin que la prochaine fois nous n'ayons pas à l'exécuter à nouveau, sauf si quelque chose a changé.

Implémentons une propriété calculée pour les messages suivants. Notre fichier HTML passera de ceci :

```html
<!-- Afficher les messages de caractères max -->
<div>
    <span v-if="tweet.length < max_length"> {{ `Max : ${tweet.length} sur ${max_length} caractères` }}
    </span>
    <span class="errorMessage" v-else>{{`Limite de caractères atteinte ! caractères en excès : ${max_length - tweet.length}`}}</span>

</div>

```

à cette version beaucoup plus propre :

```html
<!-- Afficher les messages de caractères max -->
<div>
    <span v-if="tweet.length < max_length"> {{ maxCharsText }}
    </span>
    <span class="errorMessage" v-else>{{errorMessage}}</span>
    
</div>

```
Nous avons remplacé le contenu des deux spans par deux nouvelles propriétés qui seront placées en tant que méthodes à l'intérieur de notre objet computed.

Maintenant, à l'intérieur de notre instance Vue, nous allons créer un nouvel objet appelé `computed` où nous définirons deux méthodes qui renverront les messages que nous avions auparavant.

```js
let app = new Vue({
    el: '#app',
    data: {
        tweets: [],
        tweet: "",
        max_length: 200,  
        error: ""
    },
    // Propriétés calculées
 computed: {
        maxCharsText: function(){
            return `Max : ${this.tweet.length} sur ${this.max_length} caractères`;
        },
        errorMessage: function(){
            return `Limite de caractères atteinte ! caractères en excès : ${this.max_length - this.tweet.length}`
        }
    },
    // Méthodes
 methods: {
          submitData(){
              if (this.tweet.length <= this.max_length) {
                  this.tweets.unshift(this.tweet);
                  this.tweet = "";
              } 
        }
    },

});
```
La première méthode `maxCharsText` renvoie exactement la même chaîne que celle que nous avions auparavant dans notre fichier HTML. La seule différence est que nous utilisons le mot-clé `this` pour référencer les propriétés que nous devions récupérer à l'intérieur de l'instance Vue `this.tweet.length` et `this.max_length`.

La deuxième méthode fonctionne exactement de la même manière et utilise également le mot-clé `this` pour choisir les propriétés définies dans l'instance Vue `this.max_length` et `this.tweet.length`.


### Tout ensemble
```html
<div id="app">
    <h2>De quoi voulez-vous tweeter aujourd'hui ?</h2>
    <form v-on:submit.prevent="submitData">
        <div class="form_group">
            <label for="tweet">Tweet</label>
            <textarea name="tweet" id="tweet" cols="80" rows="10" v-model="tweet"></textarea>

        </div>

        <button type="submit">Suivant</button>

    </form>

    <div>
        <span v-if="tweet.length < max_length"> {{ maxCharsText }}
        </span>
        <span class="errorMessage" v-else>{{errorMessage}}</span>
       
    </div>
    <ul>
        <li v-for="text in tweets">{{text}}</li>
    </ul>
</div>

```
Fichier JavaScript

```js
let app = new Vue({
    el: '#app',
    data: {
        tweets: [],
        tweet: "",
        max_length: 200,  
        error: ""
    },
    // Propriétés calculées
 computed: {
        maxCharsText: function(){
            return `Max : ${this.tweet.length} sur ${this.max_length} caractères`;
        },
        errorMessage: function(){
            return `Limite de caractères atteinte ! caractères en excès : ${this.max_length - this.tweet.length}`
        }
    },
    // Méthodes
 methods: {
          submitData(){
              if (this.tweet.length <= this.max_length) {
                  this.tweets.unshift(this.tweet);
                  this.tweet = "";
              } 
        }
    },

});


```


Si nous voulons utiliser des méthodes au lieu de propriétés calculées, nous pouvons simplement déplacer les deux méthodes de l'objet `computed` à l'intérieur de l'objet `methods` et les invoquer avec des parenthèses à l'intérieur de notre fichier HTML comme ceci :

```html
<div>
    <span v-if="tweet.length < max_length"> {{ maxCharsText() }}
    </span>
    <span class="errorMessage" v-else>{{errorMessage() }}</span>
    
</div>

```
N'oubliez pas que les propriétés calculées sont mises en cache alors que les méthodes ne le sont pas.
Si vous voulez en savoir plus, assurez-vous de lire la [documentation](https://vuejs.org/v2/guide/computed.html) officielle.

%[https://youtu.be/VxFT6cgTHhw]

## Comment créer un clone simple de Twitter

Maintenant, rassemblons tout ce que nous avons appris jusqu'à présent et construisons notre tout premier projet. Ce sera une application Web de type Twitter minimaliste et simplifiée.

Nous voulons créer une application simple qui possède une sorte de formulaire d'inscription, une boîte pour ajouter de nouveaux tweets et une section où nous pouvons afficher tous les tweets. Nous voulons également pouvoir supprimer des tweets.

Toutes les données doivent être persistantes afin qu'après le rafraîchissement de la page, la liste des tweets soit toujours visible tandis que le formulaire d'inscription sera masqué.

Vous pouvez regarder la vidéo sur [YouTube ici](https://youtu.be/v1j_bDDd6jI) ou à la fin de cette section si vous voulez réviser.

You can also view the repository [here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/11-project-simple-twitter-cone/).

### Définir nos tâches
Décomposons cela en grandes tâches d'abord. Ensuite, nous verrons ce que nous devons faire pour accomplir chacune d'elles.
- créer un formulaire d'inscription
- créer un formulaire de boîte de tweets
- créer une section de tweets

Pour réaliser notre projet, nous devons rechercher les outils dont nous avons besoin pour atteindre nos objectifs, alors notons-les :
- VueJS (logique d'application)
- localStorage (rendre les données persistantes)
- font awesome (icônes)

Cette application n'a pas de base de données, nous ne pouvons donc pas enregistrer plusieurs utilisateurs et leurs tweets. C'est juste une preuve de concept, quelque chose que nous construisons pour utiliser nos nouvelles connaissances.

### Créer la structure du projet
Maintenant que nous savons quoi faire, commençons par créer la structure de notre projet et importer les outils dont nous avons besoin pour accomplir la première tâche, le formulaire d'inscription.

```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clone simple de Twitter</title>
    <!-- CDN Fontawesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
    
    <!-- version de développement VueJS, inclut des avertissements utiles en console -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Feuille de style -->
    <link rel="stylesheet" href="style.css">
</head>

<body>
<div id="app">
    <!-- Créer un compte -->

    <!-- Ajouter un tweet -->

    <!-- Afficher tous les tweets -->
    
</div>
<!-- Lien vers notre fichier main.js -->
<script src="./main.js"></script>
</body>

</html>

```

Maintenant que notre fichier HTML est prêt, créons le fichier main.js et créons une instance Vue.

```js

let app = new Vue({
    el: '#app',
    data: {
        
    },
    methods: {
          
    }

});

```

Enfin, nous devons créer un fichier style.css que nous placerons pour l'instant dans le dossier racine de notre projet.

Nous utiliserons un fichier CSS que j'ai déjà écrit, et vous pouvez le télécharger [ici](https://bitbucket.org/fbhood/simple-tweet-app/src/master/style.css).

OK, notre structure de base est prête. À l'intérieur de notre fichier HTML, nous avons quelques commentaires qui reflètent nos 3 tâches principales : créer un formulaire d'inscription, créer une boîte d'ajout de tweet et afficher une liste de tweets.

Commençons par la première tâche et simulons un formulaire d'inscription.

### Comment simuler un formulaire d'inscription - HTML

À l'intérieur de l'élément racine `<div id="app"></div>`, nous devons créer un formulaire d'inscription avec les champs suivants : nom, email, mot de passe et un bouton de soumission. Le formulaire est contenu dans une carte, nous allons donc tout envelopper dans un div et lui assigner une classe card.

Le formulaire ne soumettra pas de données à un serveur, mais simulera simplement une inscription et mettra à jour une propriété dans l'objet data de l'instance Vue.

Nous placerons le code suivant à l'intérieur de notre fichier HTML :
```html
<!-- Créer un compte -->
<div class="card">
    <i class="fab fa-twitter fa-lg fa-fw"></i>
        
    <h2>Créez votre compte</h2>
    <form v-on:submit.prevent="registerAccount">
        <div class="form_group">
            <label for="name">Nom</label>
            <input type="text" v-model="name" maxlength="25" required>
        </div>
        <div class="form_group">
            <label for="email">Email</label>
            <input type="email" v-model="email" maxlength="25" required>
        </div>
        <div class="form_group">
            <label for="password">Mot de passe</label>
            <input type="password" v-model="password" maxlength="16" required>
        </div>
        <button type="submit">S'inscrire</button>
    </form>

</div>
```
Décortiquons cela. Tout d'abord, la balise form possède une directive `v-on` avec un argument `submit` afin qu'elle écoute un événement de soumission. Elle possède également un modificateur d'événement `.prevent` afin que lorsque nous cliquons sur le bouton de soumission, la page ne se rafraîchisse pas.

À l'intérieur de la directive `v-on`, il y a une méthode appelée `registerAccount` que nous devons créer à l'intérieur des méthodes de l'instance Vue.

À l'intérieur du formulaire, nous avons les trois champs de saisie : nom, email et mot de passe avec des labels. Nous avons enveloppé chaque champ dans un div avec une classe `form_group`. Plus tard, nous pourrons reproduire le style des champs d'inscription de Twitter et afficher un compteur de caractères.

Chaque champ de saisie possède une directive `v-model` qui lie l'entrée à sa propriété de données.

### Comment simuler un formulaire d'inscription - Vue
Passons à l'instance Vue pour effectuer la liaison entre le formulaire et les propriétés de l'objet data.

Ici, nous avons également besoin d'un endroit où nous pouvons stocker les détails que l'utilisateur soumet, nous allons donc créer une autre propriété pour cela.

En regardant les champs de saisie, nous avons également mis une propriété `maxlength` sur eux, qui est de 25 pour le nom et l'email et de 16 pour le mot de passe.

Comme nous l'avons fait précédemment lorsque nous avons appris le v-model, nous pouvons créer une propriété pour ces limites afin de pouvoir l'utiliser pour montrer à l'utilisateur combien de caractères il lui reste.

L'instance Vue ressemblera à ceci :

```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {}
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16
    },
    methods: {
        registerAccount(){
            // enregistrer les détails de l'utilisateur
            // ajouter l'inscription au localStorage
            // effacer les champs d'inscription

        }
    }

});
```
Décortiquons cela. Tout d'abord, à l'intérieur de l'objet `data:{}`, nous avons défini un objet pour stocker et récupérer les `userData`. Ensuite, nous avons ajouté les propriétés `name`, `email` et `password` pour faire fonctionner la liaison de données bidirectionnelle.
Enfin, nous avons ajouté les propriétés `max_length` et `max_pass_length`.

### Comment afficher le compteur de caractères de saisie
OK, maintenant que nous avons une liaison entre les champs de saisie et nos propriétés, nous pouvons afficher un compteur de caractères à l'utilisateur pendant qu'il tape.

C'est assez simple – il suffit d'afficher la longueur de chaque propriété de saisie et de la comparer aux propriétés de longueur maximale que nous avons définies dans l'instance Vue.

```html
<div class="form_group">
    <label for="name">Nom
        <span> {{ name.length + '/' + max_length }}</span>
    </label>
    <input type="text" v-model="name" :maxlength="max_length" required>
</div>

```
Ici, nous avons créé une chaîne de caractères en utilisant une expression dans le template. Nous avons affiché la longueur de la propriété `name` et la valeur de `max_length` afin que pendant que l'utilisateur tape, nous affichions quelque chose comme ceci : 13/25.

Nous avons également utilisé une directive `v-bind` sur l'attribut `maxlength` afin que sa valeur soit liée à la valeur de la propriété que nous avons définie dans l'instance Vue. Ainsi, au cas où nous voudrions la changer, nous pouvons le faire à un seul endroit.

Nous ferons de même pour les autres champs.

```html
<form id="register" v-on:submit.prevent="registerAccount">
    <div class="form_group">
        <label for="name">Nom
            <span> {{ name.length + '/' + max_length }}</span>
        </label>
        <input type="text" v-model="name" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="email">Email
            <span> {{ email.length + '/' + max_length }}</span>
        </label>
        <input type="email" v-model="email" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="password">Mot de passe
            <span> {{ password.length + '/' + max_pass_length }}</span>
        </label>
        <input type="password" v-model="password" :maxlength="max_pass_length" required>
    </div>
    <button type="submit">S'inscrire</button>

</form>

```

### Comment ajouter la logique à la méthode `registerAccount`
Il est maintenant temps de travailler sur la logique de soumission du formulaire. Nous allons simplement remplir l'objet stocké dans la propriété `userData` lorsque l'utilisateur soumet le formulaire.

À l'intérieur de la méthode `registerAccount`, nous ajouterons les détails que l'utilisateur transmet et construirons notre objet.

```js
 registerAccount(){
            // enregistrer les détails de l'utilisateur
            this.userData.name = this.name,
            this.userData.email = this.email,
            this.userData.password = this.password
            
            // ajouter l'inscription au localStorage

            // effacer les champs d'inscription
            this.name = "";
            this.email = "";
            this.password = "";
        }

```
Ici, nous avons pris la valeur des propriétés nom, email et mot de passe et les avons assignées aux propriétés que nous avons créées dans l'objet `userData`.

Cela semble correct pour la plupart car nous avons mis l'attribut `required` sur nos champs de saisie – mais si nous le supprimons, nous pourrons soumettre un formulaire vide, et nous ne voulons pas cela.

Ajoutons donc une forme de validation très basique pour vérifier au moins si l'utilisateur a tapé quelque chose dans notre formulaire, sinon nous affichons une erreur.

Pour ce faire, nous devons ajouter un bloc if à l'intérieur de la méthode et également une propriété error à l'objet data. Notre fichier ressemble maintenant à ceci :

```js


let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
      
    },  
    methods: {
        registerAccount(){
            if (this.name !== "" && this.email !== "" && this.password !== "" ) 
            {
                this.userData.id = ++this.usersID,
                this.userData.name = this.name,
                this.userData.email = this.email,
                this.userData.password = this.password
                 
            } else {
                this.error = "Remplissez tous les champs du formulaire"
            }
        
        /* Ajouter les données d'inscription au stockage local */

        
        /* Effacer les entrées d'inscription */
        this.name = "";
        this.email = "";
        this.password = "";
        }

    }
    
});
```
Ici, dans `registerAccount`, nous avons écrit une condition qui vérifie si la longueur de la propriété name n'est pas vide, si la propriété email n'est pas vide et si le mot de passe n'est pas vide `this.name !== "" && this.email !== "" && this.password !== ""`.

Si toutes ces vérifications s'évaluent à une valeur vraie, alors nous exécutons le code à l'intérieur du bloc. Sinon, nous exécutons le code dans le bloc `else` qui met à jour la valeur de la propriété `error` que nous utiliserons maintenant dans notre template pour afficher le message d'erreur.

Nous avons également ajouté une nouvelle propriété `usersID: 0,` que nous avons utilisée à l'intérieur du bloc if pour assigner une propriété id à l'objet `userData`, juste pour rendre notre application plus réaliste. Mais bien sûr, c'est inutile, car nous n'aurons pas de base de données où nous stockons tous les détails de l'utilisateur. Nous stockerons simplement un seul utilisateur dans le stockage local de son navigateur.

```html
<form id="register" v-on:submit.prevent="registerAccount">
    <div class="form_group">
        <label for="name">Nom
            <span> {{ name.length + '/' + max_length }}</span>
        </label>
        <input type="text" v-model="name" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="email">Email
            <span> {{ email.length + '/' + max_length }}</span>
        </label>
        <input type="email" v-model="email" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="password">Mot de passe
            <span> {{ password.length + '/' + max_pass_length }}</span>
        </label>
        <input type="password" v-model="password" :maxlength="max_pass_length" required>
    </div>
    <button type="submit">S'inscrire</button>
</form>


<div v-if="error.length > 0"> {{error}}</div>
```
Maintenant, notre formulaire est complet et nous affichons également un message d'erreur à l'utilisateur si les attributs requis sont supprimés de notre balisage.

Mais nos données ne persistent pas et lorsque la page est rafraîchie – tout disparaît. Réglons cela en utilisant l'API localStorage.

À l'intérieur de notre instance Vue, nous devons définir un élément dans le stockage local. Mais nous devons également enregistrer l'intégralité de l'objet `userData` afin de pouvoir utiliser ses données plus tard pour afficher un message à l'utilisateur inscrit.

```js
/* Ajouter les données d'inscription au stockage local */
localStorage.setItem('simple_tweet_registered', true)
/* Ajouter l'objet userData entier sous forme de chaîne JSON */
localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))

```
Ici, nous utilisons la méthode `setItem` de l'API Local Storage pour ajouter un élément au stockage local afin de pouvoir l'utiliser plus tard pour vérifier si l'utilisateur est inscrit ou non.

Ensuite, nous devons également stocker l'intégralité de l'objet `userData` sous forme de chaîne de caractères. Pour ce faire, nous utilisons la méthode `JSON.stringify` qui transformera l'objet en une chaîne JSON pouvant être enregistrée dans le localStorage.

Notre fichier JS est maintenant le suivant :
```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
    },  
    methods: {
        registerAccount(){
            if (this.name !== ""  && this.email !== "" && this.password !== "" ) {
                this.userData.id = ++this.usersID,
                this.userData.name = this.name,
                this.userData.email = this.email,
                this.userData.password = this.password
                 
            } else {
                this.error = "Remplissez tous les champs du formulaire"
            }
        
        /* Ajouter les données d'inscription au stockage local */
        localStorage.setItem('simple_tweet_registered', true)
        /* Ajouter l'objet userData entier sous forme de chaîne JSON */
        localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))

        
        /* Effacer les entrées d'inscription */
        this.name = "";
        this.email = "";
        this.password = "";
        }

    }
    
});
```

Maintenant, lorsque l'utilisateur visite la page de notre application, nous devons vérifier à l'intérieur du stockage local du navigateur s'il existe une clé appelée `simple_tweet_registered`. Si c'est le cas, nous pouvons supposer que l'utilisateur est inscrit et nous pouvons afficher la section suivante, la boîte de tweet. Sinon, nous affichons le formulaire d'inscription.

Nous ferons cela en créant une propriété `registered: false` dans l'objet data et en l'utilisant pour afficher ou masquer le formulaire d'inscription.

```js

data: {
    userData: {},
    usersID: 0,
    name: "",
    email: "",
    password: "",
    max_length: 25,
    max_pass_length: 16,
    error: "",
    registered: false,      
}

```
Enveloppez le formulaire dans un div avec une directive `v-if="!registered"` comme ceci :

```html
<div class="register" v-if="!registered">
    // ici va le formulaire
</div>

<div v-else> Boîte de tweet </div>
```

Notre fichier HTML final ressemble maintenant à ceci :

```html
    <div class="card">
        <i class="fab fa-twitter fa-lg fa-fw"></i>
        <!-- Créer un compte -->
        <div class="register" v-if="!registered">
            <button form="register" type="submit">S'inscrire</button>
            <h2>Créez votre compte</h2>
            <form id="register" v-on:submit.prevent="registerAccount">
                <div class="form_group">
                    <label for="name">Nom
                        <span> {{ name.length + '/' + max_length }}</span>
                    </label>
                    <input type="text" v-model="name" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="email">Email
                        <span> {{ email.length + '/' + max_length }}</span>
                    </label>
                    <input type="email" v-model="email" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="password">Mot de passe
                        <span> {{ password.length + '/' + max_pass_length }}</span>
                    </label>
                    <input type="password" v-model="password" :maxlength="max_pass_length" required>
                </div>
            </form>


            <div v-if="error.length > 0"> {{error}}</div>
        </div>
        <!-- Ajouter un tweet -->
        <div class="tweetBox" v-else>
            <h2>Bienvenue nom_utilisateur_ici écrivez votre premier Tweet</h2>
        </div>

    </div>

```

Maintenant, pour faire fonctionner cela, nous utiliserons le hook de cycle de vie que nous avons créé qui nous permet d'injecter notre code lorsque l'instance Vue a été créée. C'est parce que nous voulons vérifier cela avant de monter notre élément racine.

Ajoutons donc un hook de cycle de vie à l'instance Vue. Nous vérifierons si notre clé est présente, et si c'est le cas, nous mettrons à jour la valeur de la propriété `registered` à `true`.

Nous avons également stocké l'objet `userData` complet dans le stockage local afin de pouvoir l'utiliser pour repeupler l'objet `userData` lorsque la page est rafraîchie avec les détails que l'utilisateur a soumis.

```js
created(){
    /* Vérifier si l'utilisateur est inscrit et définir registered sur true */
    if(localStorage.getItem("simple_tweet_registered") === 'true'){
        this.registered = true;
    }
    // repeupler l'objet userData
     if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }

}
```
Pour transformer une chaîne JSON en objet, nous pouvons utiliser la méthode `JSON.parse`.

Maintenant, tout est prêt pour la tâche suivante – afficher un formulaire de tweet à l'utilisateur après l'inscription.

Notre code jusqu'à présent ressemble à ceci :

Le fichier main.js :
```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
        registered: false,
    },
    
    methods: {
          registerAccount(){
      
              if (this.name.length > 0 && this.name.length <= this.max_length && this.email !== "" && this.password !== "" ) {
                  
                    this.userData.id = ++this.usersID,
                    this.userData.name = this.name,
                    this.userData.email = this.email,
                    this.userData.password = this.password
                    this.registered=true;
                
                  
                 
              } else {
                  this.error = "Remplissez tous les champs du formulaire"
              }
            
            /* Ajouter les données d'inscription au stockage local */
            localStorage.setItem('simple_tweet_registered', true)
            /* Ajouter l'objet userData entier sous forme de chaîne JSON */
            localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))
            
            /* Effacer les entrées d'inscription */
            this.name = "";
            this.email = "";
            this.password = "";
        }
        
    },
    created(){
        /* Vérifier si l'utilisateur est inscrit et définir registered sur true */
        if(localStorage.getItem("simple_tweet_registered") === 'true'){
            this.registered = true;
        }
        // repeupler l'objet userData
        if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }
       
    }

});
```
Et le HTML à l'intérieur de l'élément `app` :

```html
<div class="card">
    <i class="fab fa-twitter fa-lg fa-fw"></i>
    <!-- Créer un compte -->
    <div class="register" v-if="!registered">
        <button form="register" type="submit">S'inscrire</button>
        <h2>Créez votre compte</h2>
        <form id="register" v-on:submit.prevent="registerAccount">
            <div class="form_group">
                <label for="name">Nom
                    <span> {{ name.length + '/' + max_length }}</span>
                </label>
                <input type="text" v-model="name" :maxlength="max_length" required>
            </div>
            <div class="form_group">
                <label for="email">Email
                    <span> {{ email.length + '/' + max_length }}</span>
                </label>
                <input type="email" v-model="email" :maxlength="max_length" required>
            </div>
            <div class="form_group">
                <label for="password">Mot de passe
                    <span> {{ password.length + '/' + max_pass_length }}</span>
                </label>
                <input type="password" v-model="password" :maxlength="max_pass_length" required>
            </div>
        </form>


        <div v-if="error.length > 0"> {{error}}</div>
    </div>
    <!-- Ajouter un tweet -->
    <div class="tweetBox" v-else>
        <h2>Bienvenue {{ userData.name }} écrivez votre premier Tweet</h2>

    </div>

</div>

```
Ici, dans le HTML, puisque nous avons utilisé le `v-else` sur la section d'ajout de tweet et utilisé le stockage local pour récupérer les données soumises par l'utilisateur, nous pouvons utiliser une expression dans le template pour récupérer le nom de l'utilisateur afin d'afficher un message de bienvenue.

Dans la section suivante, nous allons créer un formulaire de boîte de tweet afin qu'après l'inscription, l'utilisateur puisse écrire un tweet.

%[https://youtu.be/v1j_bDDd6jI]

### Comment créer un formulaire de boîte de tweet - HTML

Il est maintenant temps de construire notre formulaire d'ajout de tweet. Nous avons fait quelque chose de très similaire plus tôt dans cet article, mais nous allons maintenant devoir stocker et rendre les données persistantes. Cela nous permet d'afficher une liste de tweets même lorsque la page se rafraîchit.

```html
<div class="tweetBox" v-else>
    <h2>Bienvenue {{ userData.name }} écrivez votre premier Tweet</h2>
    <form v-on:submit.prevent="sendTweet">
        <div class="form_group">
            <label for="tweet">
                Envoyez votre tweet
                <span> {{ tweetMsg.length + '/' + max_tweet }}</span>
            </label>
            <textarea name="tweet" id="tweet" cols="30" rows="10" v-model="tweetMsg" maxlength="200"></textarea>
        </div>
        <button type="submit">Tweeter</button>
    </form>

</div>
```
Ce n'est rien de nouveau pour nous maintenant. À l'intérieur de l'élément `tweetBox`, nous ajoutons un formulaire avec la directive v-on habituelle et une méthode `sendTweet` que nous devrons définir à l'intérieur de l'objet methods. Cela prendra le tweet et l'enregistrera quelque part, peut-être dans une propriété de l'objet data.

À l'intérieur du formulaire, il y a un `textarea` qui possède une directive `v-model` qui le lie à une propriété `tweetMsg` que nous devons créer.

Enfin, un bouton de soumission.

Nous avons également un span à l'intérieur du label du tweet qui affiche un compteur de caractères à l'utilisateur comme nous l'avons fait auparavant dans le formulaire d'inscription.

Ici, nous avons une nouvelle propriété `max_tweet` qui est utilisée pour montrer la limite et le `tweetMsg.length` est utilisé pour montrer le nombre actuel de caractères insérés.

Vous pouvez regarder la vidéo sur [YouTube ici](https://youtu.be/xFwfrIciFt0) si vous voulez revoir ce que vous avez appris.

### Créer un formulaire de boîte de tweets - Vue
Allons dans l'instance Vue et ajoutons les propriétés et les méthodes `sendTweet`.

Notre objet data possède maintenant trois propriétés supplémentaires, le `max_tweet` défini sur `200`, le `tweetMsg` qui se lie au `textarea`, et un tableau `tweets` que nous utiliserons pour stocker tous les tweets que l'utilisateur envoie.
```js
data: {
    userData: {},
    usersID: 0,
    name: "",
    email: "",
    password: "",
    max_length: 25,
    max_pass_length: 16,
    max_tweet: 200, // longueur max des tweets
    error: "",
    registered: false,
    tweetMsg: "", // tweet actuel
    tweets: [] // liste des tweets
}
```
À l'intérieur des méthodes, nous avons une nouvelle méthode qui sera invoquée par la directive v-on lorsque le formulaire sera soumis :

```js

sendTweet(){
    /* Stocker le tweet dans la propriété tweets */
    this.tweets.unshift(
        {
            text: this.tweetMsg,
            date: new Date().toLocaleTimeString()
        }

    );
    /* Vider la propriété tweetMsg */
    this.tweetMsg = "";
    //console.log(this.tweets);

    /* Transformer l'objet en chaîne de caractères */
    stringTweets = JSON.stringify(this.tweets)
    //console.log(stringTweets);

    /* Ajouter au stockage local l'objet tweet stringifié */
    localStorage.setItem('simple_tweet_tweets', stringTweets)
},
```

Le code ci-dessus fait quatre choses :

- prend le tableau tweets et y ajoute un objet pour représenter un seul tweet avec les propriétés text et date. À la propriété text, nous assignons la valeur du `tweetMsg` qui est lié au `textarea`. Pour la date, nous créons un nouvel objet date avec la méthode `new Date().toLocaleTimeString()`.
- nous vidons la valeur du `tweetMsg`
- nous transformons la propriété tweets en une chaîne de caractères en utilisant la méthode `JSON.stringify(this.tweets)`
- Ensuite, nous l'ajoutons au stockage local.

Notre fichier main.js final ressemble maintenant à ceci :

```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
        registered: false,
    },
    
    methods: {
          registerAccount(){
      
              if (this.name.length > 0 && this.name.length <= this.max_length && this.email !== "" && this.password !== "" ) {
                  
                    this.userData.id = ++this.usersID,
                    this.userData.name = this.name,
                    this.userData.email = this.email,
                    this.userData.password = this.password
                    this.registered=true;
                
                  
                 
              } else {
                  this.error = "Remplissez tous les champs du formulaire"
              }
            
            /* Ajouter les données d'inscription au stockage local */
            localStorage.setItem('simple_tweet_registered', true)
            /* Ajouter l'objet userData entier sous forme de chaîne JSON */
            localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))
            
            /* Effacer les entrées d'inscription */
            this.name = "";
            this.email = "";
            this.password = "";
        },
        sendTweet(){
            /* Stocker le tweet dans la propriété tweets */
            this.tweets.unshift(
                {
                    text: this.tweetMsg,
                    date: new Date().toLocaleTimeString()
                }

            );
            /* Vider la propriété tweetMsg */
            this.tweetMsg = "";
            //console.log(this.tweets);

            /* Transformer l'objet en chaîne de caractères */
            stringTweets = JSON.stringify(this.tweets)
            //console.log(stringTweets);

            /* Ajouter au stockage local l'objet tweet stringifié */
            localStorage.setItem('simple_tweet_tweets', stringTweets)
        },

        
    },
    created(){
        /* Vérifier si l'utilisateur est inscrit et définir registered sur true */
        if(localStorage.getItem("simple_tweet_registered") === 'true'){
            this.registered = true;
        }
        // repeupler l'objet userData
        if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }
       
    }

});
```
Maintenant que nous avons terminé cette partie, nous pouvons afficher une liste de tweets et également gérer le rafraîchissement de la page, et le stockage local contient notre objet de tweets. Nous devrons le ré-analyser et ajouter son contenu à la propriété `tweets` pour voir la liste.

Ensuite, nous apprendrons comment afficher la liste des tweets en utilisant une directive v-for.

%[https://youtu.be/xFwfrIciFt0]

### Comment afficher une liste de tweets - HTML

À l'intérieur de notre élément racine, ajoutez le code suivant :

```html
 <!-- Afficher tous les tweets -->
    <div class="card_tweets">
        <section class="tweets" v-if="tweets.length > 0">
            <h2>Tweets</h2>
            <div class="tweetMsg" v-for="(tweet, index) in tweets">
                <p>
                    {{tweet.text}}
                </p>

                <div class="tweetDate">
                    <i class="fas fa-calendar-alt fa-sm fa-fw"></i>{{tweet.date}}
                </div>
 
            </div>

        </section>
        <div v-else>Aucun tweet à afficher</div>
    </div>
```

Ici, nous enveloppons tout dans un div avec une classe `card_tweets`. Ensuite, nous utilisons une directive v-if à l'intérieur d'une section enfant pour vérifier s'il y a des tweets dans le tableau `tweets` `v-if="tweets.length > 0"`.

À l'intérieur de cette section, nous pouvons boucler sur le tableau tweets en utilisant une directive `v-for="(tweet, index) in tweets"`. Après cela, nous utilisons des expressions dans le template pour afficher la propriété text du tweet `{{tweet.text}}` et les données `{{tweet.date}}`.

Après la `section`, nous pouvons utiliser une directive `v-else` pour afficher un message au cas où il n'y aurait pas de tweets stockés dans le tableau tweets `<div v-else>Aucun tweet à afficher</div>`. C'est fait.

Maintenant, il reste une dernière chose à faire, et c'est de comprendre quoi faire pour supprimer des tweets de la liste.

Mais lorsque l'utilisateur rafraîchit la page, tout disparaît. Nous devons donc travailler à nouveau avec le `localStorage` pour repeupler notre tableau tweets à partir de celui-ci avant de rendre l'élément racine.

À l'intérieur du hook de cycle de vie `created`, nous allons maintenant écrire du code pour analyser les tweets et les enregistrer à nouveau dans la propriété `tweets` :

```js
/* Analyser tous les tweets du stockage local */
if(localStorage.getItem("simple_tweet_tweets")) {
    console.log("Il y a une liste de tweets");
    this.tweets = JSON.parse(localStorage.getItem('simple_tweet_tweets'))
}else {
    console.log("Pas de tweets ici");
}
```

Ici, nous avons utilisé l'API `localStorage` pour vérifier d'abord s'il existait une clé appelée `simple_tweet_tweets`. Si c'est le cas, nous récupérons la propriété tweets en utilisant `this.tweets` et lui assignons le contenu du `localStorage`. Mais nous analysons la chaîne en `JSON` avec `JSON.parse`, donc nous écrivons `this.tweets = JSON.parse(localStorage.getItem('simple_tweet_tweets'))`.

Maintenant, tout fonctionne. Après avoir rafraîchi la page, les tweets sont toujours là. Avançons. Dans l'étape suivante, nous ajouterons une méthode pour supprimer des tweets de la liste.

Vous pouvez regarder la vidéo sur [YouTube ici](https://youtu.be/3DzBkUHH3bU) ou à la fin de cette section pour revoir ce que vous avez appris.

### Comment supprimer des tweets
À l'intérieur du div qui contient le message du tweet, nous pouvons ajouter un autre div pour afficher un lien et une icône de corbeille. Cela permet à l'utilisateur de cliquer dessus et de supprimer ce tweet.

```html
<div class="tweet_remove" @click="removeTweet(index)">
    <span class="remove">Supprimer ce tweet <i class="fas fa-trash fa-xs fa-fw"></i></span>
</div>
```
Ici, nous avons simplement utilisé une directive raccourcie v-on sur le div et invoqué une méthode `removeTweet(index)`, en passant à la méthode l'index de l'élément afin de savoir quoi supprimer.

Construisons notre méthode `removeTweet` maintenant :

```js
removeTweet(index){
    let removeIt = confirm("Êtes-vous sûr de vouloir supprimer ce tweet ?")
    if(removeIt) {
        this.tweets.splice(index, 1);
        /* Supprimer l'élément également du stockage local */
        localStorage.simple_tweet_tweets = JSON.stringify(this.tweets)
    }
}
```
Ce morceau de code est assez simple. Notre méthode accepte un index qui représente la position de l'objet tweet dans le tableau obtenu à partir de la directive v-for lorsque la méthode est invoquée.

Nous créons ensuite une variable pour demander à l'utilisateur de confirmer qu'il souhaite supprimer le tweet. Nous avons utilisé la fonction `confirm` pour cela.

Si la valeur de la variable `removeIt` est vraie, alors nous exécutons le code et utilisons `this.tweets.splice(index, 1)` pour supprimer le tweet du tableau en utilisant son index.

Enfin, nous mettons à jour la valeur du `localStorage` en lui assignant le nouveau tableau en utilisant `localStorage.simple_tweet_tweets = JSON.stringify(this.tweets)`.

### Code final
Notre code est maintenant complet. Vous pouvez trouver le code final ci-dessous ou à l'intérieur du dépôt ici : [https://bitbucket.org/fbhood/simple-tweet-app/src/master/].

```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue 2 Hello World</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <!-- Axios CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.0/axios.min.js"
        integrity="sha512-DZqqY3PiOvTP9HkjIWgjO6ouCbq+dxqWoJZ/Q+zPYNHmlnI2dQnbJ5bxAHpAMw+LXRm4D72EIRXzvcHQtE8/VQ=="
        crossorigin="anonymous"></script>
    <!-- version de développement, inclut des avertissements utiles en console -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
</head>

<body>
<div id="app">
    <div class="card">
        <i class="fab fa-twitter fa-lg fa-fw"></i>
        <!-- Créer un compte -->
        <div class="register" v-if="!registered">
            <button form="register" type="submit">S'inscrire</button>
            <h2>Créez votre compte</h2>
            <form id="register" v-on:submit.prevent="registerAccount">
                <div class="form_group">
                    <label for="name">Nom
                        <span> {{ name.length + '/' + max_length }}</span>
                    </label>
                    <input type="text" v-model="name" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="email">Email
                        <span> {{ email.length + '/' + max_length }}</span>
                    </label>
                    <input type="email" v-model="email" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="password">Mot de passe
                        <span> {{ password.length + '/' + max_pass_length }}</span>
                    </label>
                    <input type="password" v-model="password" :maxlength="max_pass_length" required>
                </div>
            </form>


            <div v-if="error.length > 0"> {{error}}</div>
        </div>
        <!-- Ajouter un tweet -->
        <div class="tweetBox" v-else>
            <h2>Bienvenue {{ userData.name }} écrivez votre premier Tweet</h2>
            <form v-on:submit.prevent="sendTweet">
                <div class="form_group">
                    <label for="tweet">
                        Envoyez votre tweet
                        <span> {{ tweetMsg.length + '/' + max_tweet }}</span>
                    </label>
                    <textarea name="tweet" id="tweet" cols="30" rows="10" v-model="tweetMsg" maxlength="200"></textarea>
                </div>
                <button type="submit">Tweeter</button>
            </form>

        </div>

    </div>
    <!-- Afficher tous les tweets -->
    <div class="card_tweets">
        <section class="tweets" v-if="tweets.length > 0">
            <h2>Tweets</h2>
            <div class="tweetMsg" v-for="(tweet, index) in tweets">
                <p>
                    {{tweet.text}}
                </p>

                <div class="tweetDate">
                    <i class="fas fa-calendar-alt fa-sm fa-fw"></i>{{tweet.date}}
                </div>
                <div class="tweet_remove" @click="removeTweet(index)">
                    <span class="remove">Supprimer ce tweet <i class="fas fa-trash fa-xs fa-fw"></i></span>
                </div>
                
            </div>

        </section>
        <div v-else>Aucun tweet à afficher</div>
    </div>
</div>
<script src="./main.js"></script>
</body>

</html>

```

Fichier JavaScript

```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        max_tweet: 200,
        error: "",
        registered: false,
        tweetMsg: "",
        tweets: []
    },
    
    methods: {
          registerAccount(){
      
              if (this.name.length > 0 && this.name.length <= this.max_length && this.email !== "" && this.password !== "" ) {
                  
                    this.userData.id = ++this.usersID,
                    this.userData.name = this.name,
                    this.userData.email = this.email,
                    this.userData.password = this.password
                    this.registered=true;
                
                  
                 
              } else {
                  this.error = "Remplissez tous les champs du formulaire"
              }
            
            /* Ajouter les données d'inscription au stockage local */
            localStorage.setItem('simple_tweet_registered', true)
            /* Ajouter l'objet userData entier sous forme de chaîne JSON */
            localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))
            
            /* Effacer les entrées d'inscription */
            this.name = "";
            this.email = "";
            this.password = "";
        }, 
        sendTweet(){
            this.tweets.unshift(
                {
                    text: this.tweetMsg,
                    date: new Date().toLocaleTimeString()
                }

            );
            this.tweetMsg = "";
            
            //console.log(this.tweets);
            stringTweets = JSON.stringify(this.tweets)
            //console.log(stringTweets);
            localStorage.setItem('simple_tweet_tweets', stringTweets)
        },
        removeTweet(index){
            let removeIt = confirm("Êtes-vous sûr de vouloir supprimer ce tweet ?")
            if(removeIt) {
                this.tweets.splice(index, 1);
                /* Supprimer l'élément également du stockage local */
                localStorage.simple_tweet_tweets = JSON.stringify(this.tweets)
            }
        }
    },
    created(){
        /* Vérifier si l'utilisateur est inscrit et définir registered sur true */
        if(localStorage.getItem("simple_tweet_registered") === 'true'){
            this.registered = true;
        }

        if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }
        /* Analyser tous les tweets du stockage local */
        if(localStorage.getItem("simple_tweet_tweets")) {
            console.log("Il y a une liste de tweets");
            this.tweets = JSON.parse(localStorage.getItem('simple_tweet_tweets'))

        }else {
            console.log("Pas de tweets ici");
        }
    }

});

```

Nous sommes prêts à poursuivre notre voyage avec Vue. Il est maintenant temps d'en apprendre davantage sur les composants.

%[https://youtu.be/3DzBkUHH3bU]

## Les bases des composants Vue

Un composant est un bloc de code réutilisable qui représente un élément spécifique sur la page.

Chaque page Web et chaque application Web ou mobile peut être divisée en composants. En partant des sections principales, nous pouvons ensuite les diviser en morceaux plus petits et créer des sous-composants.

Chaque composant est réutilisable et est composé de code HTML, CSS et JavaScript dédié.

Nous pouvons utiliser des composants pour organiser notre code et construire des mises en page complexes qui sont facilement maintenables.

Si l'on regarde une page Web simple, elle est généralement composée d'un en-tête, de la zone de contenu principal et d'un pied de page. Mais chacune de ces trois pièces peut être subdivisée en parties plus petites.

Par exemple, un en-tête peut avoir le menu de navigation principal, un menu secondaire et une image hero. Il en va de même pour les zones principales et de pied de page.

Vous pouvez regarder la vidéo sur [YouTube ici](https://youtu.be/wrqjPka7puo) ou à la fin de cette section pour réviser. Vous pouvez également consulter le dépôt [ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/12-components-basics/).

Pour commencer avec les composants, nous devons d'abord apprendre à les enregistrer, à leur transmettre des données, puis nous devons apprendre à les utiliser. Voici quelques excellents aperçus de ces sujets pour vous aider à démarrer :

- Enregistrer un composant (https://vuejs.org/v2/guide/components-registration.html)
- Comment utiliser les Props (https://vuejs.org/v2/guide/components-props.html)
- Comment utiliser les Slots (https://vuejs.org/v2/guide/components-slots.html)
- Comment fonctionne l'objet Data à l'intérieur d'un composant
- Événements des composants enfants (https://vuejs.org/v2/guide/components-custom-events.html)
- Composants dynamiques ( https://vuejs.org/v2/guide/components-dynamic-async.html)


### Comment enregistrer un composant dans Vue
Pour enregistrer un composant, nous devons utiliser la méthode `component` sur l'objet `Vue()`. Après avoir appelé cette fonction, nous devons définir une propriété template avec un balisage spécifique au composant.
```js
Vue.component('component-name', {
    // propriétés du composant ici
});
```
Chaque composant doit avoir au moins une propriété template – sans elle, un composant n'a pas beaucoup de sens.

L'étape suivante consiste donc à définir une propriété template et à lui passer un littéral de chaîne avec une balise HTML :
```js
Vue.component('test-component', {
    // propriétés du composant ici
    template: `<p>Je suis un composant</p>`

});
```
Maintenant, nous pouvons utiliser notre composant plusieurs fois à l'intérieur de notre fichier HTML principal en utilisant son nom comme s'il s'agissait d'une balise HTML standard.

```html
<div id="app">
  <test-component></test-component>
</div>

```
Cependant, notre composant affichera toujours le même contenu, `Je suis un composant`. Rendons-le plus utile et, en suivant notre exemple de tweets, construisons un composant de message de tweet.

```js

Vue.component('tweet-message', {
   
    template: `
       <div>
           <p> Le texte du tweet va ici </p>
           <p> La date du tweet va ici</p>
       </div>
    `
});
```

OK, maintenant que nous avons la base de notre composant, nous devons lui transmettre des données.

Une chose à remarquer ici est que chaque composant nécessite un seul élément racine à l'intérieur de la propriété template. Ainsi, puisque nous avons deux paragraphes, nous les avons enveloppés dans un div qui sera considéré comme l'élément racine de notre composant.

À l'intérieur, nous pouvons mettre tout ce que nous voulons pour construire notre composant personnalisé.

Passons à l'étape suivante et transmettons des données au composant.

### Comment utiliser les props dans Vue

Maintenant, compte tenu de ce que nous avons appris jusqu'à présent, nous voulons transmettre des données à notre composant comme nous l'avons fait précédemment pour lier des données entre l'instance Vue et le fichier de balisage via la syntaxe mustache.

Cependant, avec les composants, les choses fonctionnent un peu différemment. Nous utilisons les props pour créer une liaison entre notre composant et son template.

La propriété `props` peut être définie comme un tableau ou comme un objet.
Lorsqu'elle est utilisée comme un tableau, nous pouvons spécifier les propriétés sous forme de chaînes de caractères à l'intérieur du tableau et celles-ci pourront plus tard être utilisées à l'intérieur du composant comme nous le faisons habituellement.

Lorsque nous utilisons un objet, nous pouvons passer la prop comme clé et son type comme valeur. Cela aidera à s'assurer que le type de données exact est transmis à notre composant.

Voyons un exemple de cela.

Exemple de props sous forme de tableau :
```js
Vue.component('tweet-message', {
    props: ['text', 'date']
    template: `
       <div>
           <p> {{text}} </p>
           <p> {{date}}</p>
       </div>
    `
});

```
Utiliser les props comme un objet où la clé est la propriété et la valeur est son type :
```js
Vue.component('tweet-message', {
    props: {
        text: String,
        date: String
    }
    template: `
       <div>
           <p> {{text}} </p>
           <p> {{date}}</p>
       </div>
    `
});
```

Une fois que nous avons défini nos propriétés, nous pouvons les utiliser comme attributs HTML et leur passer les données que nous voulons que notre composant affiche sur la page.

Par exemple, nous pouvons utiliser le composant ci-dessus pour afficher une série de tweets en utilisant notre composant nouvellement créé.

```html
    <!-- Passer manuellement les données au composant tweet-message -->
    <tweet-message text="Ceci est un composant" date="25/12/2020"></tweet-message>
    <tweet-message text="Ceci est un autre composant" date="26/12/2020"></tweet-message>
    <tweet-message text="Ceci est un autre composant" date="27/12/2020"></tweet-message>
    <!-- Passer une expression javascript à la propriété date du composant tweet-message -->
    <tweet-message text="Ceci est un autre composant" :date="new Date().toLocaleString()"></tweet-message>
```
Les premiers exemples rendront la chaîne que nous avons passée entre guillemets. Mais pour afficher le résultat calculé de la nouvelle instance `Date()`, nous devrons utiliser la directive v-bind afin que son contenu soit interprété comme du code JavaScript.

Vous pouvez revoir tout cela dans la documentation ici : [https://vuejs.org/v2/guide/components-props.html].

### La propriété data à l'intérieur des composants
Jusqu'à présent, nous avons vu que nous pouvons lier des données en définissant des propriétés à l'intérieur de l'objet `data` sur une instance Vue.

Lorsque l'on travaille avec des composants, l'objet data n'est pas disponible en tant qu'objet mais en tant que fonction. Cette fonction peut renvoyer un objet avec des propriétés. Cela rendra chaque instance de composant unique et indépendante des autres.

En suivant notre exemple précédent, ajoutons quelques classes CSS à notre composant.

Tout d'abord, nous allons modifier notre template de composant et lier l'attribut class à une propriété de données. Ensuite, nous créerons notre objet data.

```js
Vue.component('tweet-message', {
    props: {
        text: String,
        date: String
    }
    template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass"> {{date}}</p>
       </div>
    `
});
```
Maintenant, notre template cherchera deux propriétés de données, `tweetBoxWrapper` et `dateClass`, que nous pourrons utiliser plus tard dans notre CSS pour ajouter du style à nos éléments. Ajoutons la fonction data maintenant.
 
```js
Vue.component('tweet-message', {
    props: {
        text: String,
        date: String
    }
    template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass"> {{date}}</p>
       </div>
    `,
    data(){
        return {
            // Les propriétés de données vont ici
            tweetBoxWrapper: "tweet-message",
            dateClass: "tweet-date",
        }
    }
});
```
Une autre chose que nous pouvons faire est de définir une propriété de données et de l'utiliser à l'intérieur de notre template, par exemple, pour afficher dynamiquement la date actuelle. Nous pouvons définir une propriété `now` et l'utiliser dans le template comme nous l'avons fait précédemment avec la propriété `date` :

```js

Vue.component('tweet-message', {
    props: {
        'text': String,
        
    },
     template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass">{{now}}</p>
           
       </div>
       
    `,
    data(){
        return {
            tweetBoxWrapper: "tweet-message",
            dateClass: "tweet-date",
            now: new Date().toDateString(), // 3 
            
        }
    }

    
});
```
Dans l'exemple ci-dessus, nous avons utilisé à la fois `props` et `data`. Nous pouvons utiliser la prop `text` comme attribut lorsque nous utilisons notre composant `<tweet-message text="Ceci est un composant"></tweet-message>`. Les propriétés que nous avons renvoyées dans la méthode `data` sont liées au template et afficheront les informations que nous spécifions directement dans la méthode data.

À l'intérieur de la méthode data, nous devons nous rappeler que les props définies ici sont accessibles en utilisant le mot-clé `this`.

Ainsi, si nous voulons stocker la valeur de la prop text dans une propriété de l'objet data, nous pouvons la récupérer comme ceci :

```js
Vue.component('tweet-message', {
    props: {
        'text': String,
        
    },
     template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass">{{now}}</p>
           
       </div>
       
    `,
    data(){
        return {
            tweetBoxWrapper: "tweet-message",
            dateClass: "tweet-date",
            now: new Date().toDateString(), 
            message: this.text
        }
    }

    
});
```
Ensuite, nous allons apprendre les slots.

### Comment utiliser les slots
Il y a des situations où nous ne savons pas ou ne voulons pas définir strictement ce qui va à l'intérieur d'un composant. Ou nous pourrions vouloir laisser l'utilisateur décider de son contenu lorsqu'il utilise notre composant.

Dans de tels cas, nous pouvons utiliser des slots lorsque nous déclarons le template de notre composant.

Imaginons que nous ayons un autre composant que nous voulons utiliser pour diviser les tweets en différentes sections.

```js
Vue.component('tweet-section', {
    props: {
        'title': String,
        
    },
     template: `
        <div class="tweet_section">
            <h2>{{title}}</h2>
           <slot></slot>
       </div>  
    `    
});
```
Notre nouveau composant peut être aussi simple que cela, un div avec une classe `tweet_section`, un `h2` qui se lie à une prop, et un slot. Le slot signifie qu'à l'intérieur de notre composant, nous pouvons mettre ce que nous voulons, comme imbriquer d'autres éléments et même d'autres composants.

```html

<tweet-section title="Derniers Tweets">
    <tweet-message text="Ceci est mon premier tweet"></tweet-message>
    <tweet-message text="Ceci est mon deuxième tweet"></tweet-message>
    <tweet-message text="Ceci est mon troisième tweet"></tweet-message>
    <tweet-message text="Ceci est mon quatrième tweet"></tweet-message>

</tweet-section>
<tweet-section title="Les plus populaires">
    <h3>Tendances en informatique</h3>
    <tweet-message text="Ceci est un tweet très populaire"></tweet-message>
    <tweet-message text="Ceci est un autre tweet populaire"></tweet-message>
</tweet-section>

```
Nous n'avons fait qu'effleurer la surface ici, mais avec ce que nous savons, nous pouvons déjà modifier notre application `simple_twitter` pour utiliser des composants. En cours de route, nous apprendrons également comment fonctionnent les événements à l'intérieur des composants.


%[https://youtu.be/wrqjPka7puo]


## Mise à jour du projet : Clone simple de Twitter avec des composants

Maintenant que nous avons une compréhension de base des composants, nous pouvons mettre à jour le projet Twitter simple que nous avons construit dans les vidéos précédentes et utiliser des composants pour améliorer notre code.

Nous devons faire quelques choses pour que cela se produise et créer un composant :

 1. Nous devons décider quel composant nous voulons construire
 2. Nous devons extraire le code du balisage et le placer dans la propriété template
 3. Nous devons refactoriser notre code pour faire fonctionner le composant.

Vous pouvez regarder le tutoriel sur [YouTube ici](https://youtu.be/HanHyGFC6Sc)
ou consulter le dépôt [ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/13-simple-twitter-components/).


Disons que nous voulons créer un composant pour le message du tweet.

### Comment créer le composant
Créons un composant pour un message de tweet comme ceci :
```js
Vue.component('tweet-message',{
    template: ``
});
```
### Comment déplacer l'élément tweetMsg
Ensuite, nous devons déplacer l'élément `tweetMsg` à l'intérieur de la propriété `template` de notre composant :
```js

Vue.component('tweet-message',{
    template: `
    <div class="tweetMsg" v-for="(tweet, index) in tweets">
        <p>
            {{ tweet.text}}
        </p>
        <div class="tweetDate">
            <i class="fas fa-calendar fa-sm fa-fw"></i>{{ tweet.date }}
        </div>
        <div class="tweet_remove" @click="removeTweet(index)">
            <span class="remove">Supprimer ce tweet <i class="fas fa-trash fa-sm fa-fw"></i></span>
        </div>
    </div>
    `
});
```
Après cela, nous devons mettre à jour le template car la directive v-for est maintenant inutile. Nous allons donc la supprimer et la rajouter plus tard lorsque nous serons prêts à utiliser le composant.

Étant donné que nous n'aurons pas de directive v-for à ce stade, nous voulons toujours utiliser la variable tweet pour récupérer le tweet, nous la passerons donc comme `props`.


```js
Vue.component('tweet-message',{
    props: {
        'tweet': Object,
    },
    template: `
    <div class="tweetMsg">
        <p>
            {{ tweet.text}}
        </p>
        <div class="tweetDate">
            <i class="fas fa-calendar fa-sm fa-fw"></i>{{ tweet.date }}
        </div>
        <div class="tweet_remove" @click="removeTweet(index)">
            <span class="remove">Supprimer ce tweet <i class="fas fa-trash fa-sm fa-fw"></i></span>
        </div>
    </div>
    `
});
```
### Comment émettre un événement personnalisé
Il y a aussi un écouteur d'événement qui doit changer pour permettre à notre application de fonctionner comme prévu.

```html
<div class="tweet_remove" @click="removeTweet(index)">
    <span class="remove">Supprimer ce tweet <i class="fas fa-trash fa-sm fa-fw"></i></span>
</div>
```

Le code ici `<div class="tweet_remove" @click="removeTweet(index)">` écoute les événements de clic afin que l'utilisateur puisse supprimer un tweet en cliquant dessus.

Cela devra disparaître, et nous devons le remplacer par une méthode spéciale de l'instance Vue appelée `$emit()`. Notre instance de composant devra communiquer avec l'instance parente et lui dire qu'elle souhaite déclencher la méthode de suppression de tweet.

Pour résoudre ce problème, Vue fournit un système d'événements personnalisés. Il nous permet d'utiliser la directive v-on pour écouter non seulement les événements DOM natifs mais aussi les événements personnalisés définis au niveau du composant.

Nous devons mettre à jour cette ligne de code :
```html
<div class="tweet_remove" @click="removeTweet(index)">
```
et la changer comme ceci :
```html
<div class="tweet_remove" @click="$emit('remove-tweet', 'index')">
```

Décortiquons cela : nous continuons à utiliser la directive v-on dans sa forme courte `@`. Ensuite, nous utilisons la méthode Vue `$emit` pour définir un événement personnalisé que notre composant émettra lorsque nous cliquons sur cet élément.

À la méthode `$emit`, nous passons deux paramètres, le premier est le nom de l'événement personnalisé `remove-tweet`, et le second est un paramètre que nous voulons passer à l'écouteur d'événement lorsque nous utilisons `index`. Ce sera l'index de l'élément que nous voulons supprimer.

Ainsi, l'instance parente peut écouter notre événement, déclencher la méthode `removeTweet` que nous avons définie dans l'instance Vue principale et supprimer le bon tweet.


### Tout mettre ensemble
Notre composant final ressemble maintenant à ceci :
```js

Vue.component('tweet-message',{
    props: {
        'tweet': Object,
    },
    template: `
    <div class="tweetMsg">
        <p>
            {{tweet.text}}
        </p>

        <div class="tweetDate">
            <i class="fas fa-calendar-alt fa-sm fa-fw"></i>{{tweet.date}}
        </div>
        <div class="tweet_remove" @click="$emit('remove-tweet', 'index')">
            <span class="remove">Supprimer ce tweet <i class="fas fa-trash fa-xs fa-fw"></i></span>
        </div>
        
    </div>
    `
});
```

Et nous allons changer notre fichier index.html comme suit :

```html
<!-- Afficher tous les tweets -->
<div class="card_tweets">
    <section class="tweets" v-if="tweets.length > 0">
        <h2>Tweets</h2>
        <tweet-message v-for="(tweet, index) in tweets"  v-bind:tweet="tweet" :key="index" @remove-tweet="removeTweet(index)"></tweet-message>
    </section>
    <div v-else>Aucun tweet à afficher</div>
</div>
```

Maintenant que nous avons terminé notre premier projet, apprenons à effectuer une requête API et à utiliser l'API GitHub pour construire notre portfolio final.


%[https://youtu.be/HanHyGFC6Sc]

## Comment effectuer des appels API avec Axios

Pour notre prochain projet, j'ai créé un design simple mais agréable en utilisant Figma que nous utiliserons pour lancer notre portfolio.

Notre portfolio utilisera l'API REST de GitHub pour récupérer des projets et remplir le design.

Vous pouvez regarder la vidéo sur [YouTube ici](https://youtu.be/XJEmPr89HA8)
et consulter le dépôt sur [BitBucket](https://bitbucket.org/fbhood/how-to-vuejs/src/master/14-axios/).

### Qu'est-ce qu'une API REST ?

Pour citer Wikipédia :

>"Une API REST est un style d'architecture logicielle qui permet au système demandeur d'accéder et de manipuler une représentation textuelle des ressources Web."

Ce que cela signifie, c'est que notre application Vue (le système demandeur) demandera à GitHub une représentation textuelle de nos dépôts que nous pourrons utiliser plus tard et manipuler pour présenter nos projets à l'intérieur de notre portfolio.

Pour notre projet final, nous utiliserons une bibliothèque appelée Axios qui nous aidera à effectuer des requêtes HTTP vers l'API GitHub.

Nous pouvons installer Axios dans notre projet de plusieurs manières. Pour notre exemple, nous allons rester simples et utiliser le CDN.

Il existe également d'autres méthodes que vous pouvez utiliser pour installer Axios. La documentation officielle d'Axios est disponible [ici](https://www.npmjs.com/package/axios)
et vous pouvez lire comment consommer l'API dans la [documentation ici](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html#Base-Example).

### Comment installer Axios via CDN

Commençons donc et installons Axios via le CDN. Nous utiliserons le CDN UNPKG et insérerons une balise script à l'intérieur de notre fichier HTML principal.

Ce CDN fournira toujours la version la plus à jour d'Axios. Alternativement, nous pouvons également spécifier un numéro de version différent.

Commençons par insérer le script suivant dans un fichier index.html que nous utiliserons pour envoyer notre première requête HTTP à l'API GitHub.


```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

Notre fichier HTML final ressemblera à ceci maintenant :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJS / API GitHub</title>
    

</head>
<body>
    <div id="app"> </div>

    <!-- CDN dernière version Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

    <!-- Version de développement VueJS -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="./main.js"></script>
</body>
</html>
```

Le code ci-dessus n'est pas nouveau, mais regardons-le pièce par pièce.

Nous avons une structure HTML de base. Avant la balise body fermante, nous avons placé deux balises script, une pour Axios et une pour VueJs.

Dans le body, nous avons créé un élément racine pour l'application Vue que nous avons appelé `#app`.

Enfin, avant la fin de la balise body, nous avons placé une nouvelle balise script qui pointe vers le fichier où nous écrirons notre code, le fichier main.js.

Nous avons maintenant tous les éléments de base pour effectuer notre premier appel API et demander des données à l'API GitHub.

Mais avant cela, voyons rapidement ce qu'est réellement une requête HTTP et quel genre de requêtes nous pouvons faire.

### Qu'est-ce qu'une requête HTTP ?
HTTP signifie Hypertext transfer protocol (Protocole de transfert hypertexte). C'est un protocole de couche application conçu pour les communications entre deux points :

1. un client Web (le navigateur)
2. un serveur Web

Ce protocole permet la transmission de données comme des fichiers HTML. Il définit des verbes également connus sous le nom de méthodes que vous pouvez utiliser pour effectuer des actions spécifiques sur une ressource donnée.

La méthode ou le verbe que nous utiliserons pour notre projet est la méthode `GET`, qui, comme vous l'avez peut-être deviné, est utilisée pour obtenir ou récupérer
une ressource du serveur Web.

Nous avons également d'autres méthodes :
- GET (récupère des données)
- POST (envoie des données)
- PUT (met à jour la représentation entière des données)
- PATCH (similaire à put mais utilisé pour mettre à jour partiellement les données)
- DELETE (supprime des données)

Chacune de ces requêtes effectue une action spécifique sur une ressource, mais il existe également d'autres verbes comme HEAD, OPTIONS, CONNECT et TRACE.

Je ne couvrirai pas le HTTP en détail ici car cela sort du cadre de ce guide. Mais ci-dessous se trouvent quelques liens vers des pages de documentation
liées à ce sujet si vous voulez en savoir plus.

Je vous suggère de lire au moins les éléments suivants :

- [Introduction au HTTP](https://www.freecodecamp.org/news/how-the-internet-works/)
- [Méthodes HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)


### Comment effectuer une requête GET

Nous utiliserons la méthode GET pour effectuer des requêtes de récupération à partir de l'API GitHub. Toutes les données que nous voulons demander sont accessibles publiquement (les dépôts publics d'un utilisateur), nous n'avons donc pas besoin d'authentifier notre application.

Mais les requêtes non authentifiées sont limitées. Pour la portée de ce tutoriel, c'est parfaitement correct. Si vous prévoyez de mettre cela en production, vous voudrez peut-être regarder comment effectuer des requêtes authentifiées et obtenir une clé API de GitHub.

GitHub fournit une documentation claire et approfondie sur son API REST, y compris une liste de ressources que vous pouvez demander avec leurs points de terminaison. Nous utiliserons les ressources "List repositories for a user" disponibles [ici](https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#list-repositories-for-a-user).

Regardons la documentation. La première chose que nous remarquons est que GitHub nous donne un point de terminaison GET où nous pouvons envoyer nos requêtes HTTP `/users/{username}/repos`.

L'espace réservé `{username}` doit être remplacé par le nom d'utilisateur réel de l'utilisateur dont nous voulons demander la liste des dépôts publics.

D'après la documentation, nous voyons également qu'il existe d'autres paramètres que nous pouvons utiliser pour affiner notre requête. Nous utiliserons `username` qui va dans le chemin et doit être une chaîne de caractères comme décrit dans le tableau des paramètres sous Type.

Nous pouvons également utiliser les paramètres `per_page` et `page` pour paginer nos résultats.

Faisons la première requête et voyons ce que nous obtenons.

À l'intérieur de notre fichier main.js, nous allons créer une nouvelle instance Vue et ajouter un hook de cycle de vie `mounted` où nous effectuerons la requête HTTP en utilisant Axios.

```js
let app = new Vue({
    el:'#app',
    data:{
        projects: [],
        perPage: 20,
        page: 1
    },
    mounted(){
        
         axios
         .get(`https://api.github.com/users/fabiopacifici/repos?per_page=${this.perPage}&page=${this.page}`)
         .then(
            response => {
                console.log(response);
                this.projects = response.data;
            }
        )
        .catch(error=> {console.log(error);})
    }
});
```

Décortiquons ce code. Tout d'abord, nous avons créé une nouvelle instance Vue. Ensuite, nous avons utilisé la propriété `el` et lui avons assigné un élément HTML racine.

Ensuite, nous avons défini un objet `data` et les propriétés que nous utiliserons plus tard pour effectuer la requête HTTP et gérer la réponse.

Après l'objet data, nous avons défini un hook de cycle de vie que nous utiliserons pour exécuter notre code une fois que l'élément racine aura été monté.

À l'intérieur de la méthode `mounted`, il est temps d'utiliser Axios et d'effectuer une requête HTTP.

Axios est un client HTTP basé sur les promesses. Lorsque nous utilisons la méthode get pour demander nos données à l'API GitHub, elle renverra une promesse qui doit être gérée.

Nous faisons cela en utilisant la syntaxe `axios.get()` pour effectuer la requête, puis nous gérons sa réponse en utilisant la méthode `.then()` sur la promesse.

Si notre requête échoue, la méthode `.catch()` gérera l'erreur et, dans ce cas, affichera le message d'erreur sur la console.

Les promesses sortent du cadre de ce guide, mais si vous voulez en savoir plus, vous pouvez consulter [cet article détaillé ici](https://www.freecodecamp.org/news/javascript-promise-tutorial-how-to-resolve-or-reject-promises-in-js/).

À l'intérieur de la méthode `.get()`, nous avons mis l'URL incluant une chaîne de requête qui utilise les paramètres `per_page` et `page` pour soumettre notre requête. À l'intérieur de la méthode `.then()`, nous avons géré la réponse. Le paramètre response nous est donné par la promesse et nous utilisons une fonction fléchée pour le gérer.

```js 
response => {
                console.log(response);
                this.projects = response.data;
            }
```

La méthode get renvoie une promesse. Ici, nous avons simplement géré sa `response` avec une fonction fléchée où `response` est la valeur de retour que nous avons obtenue en appelant `axios.get()`.

Nous avons enregistré l'objet de réponse dans la console. Ensuite, nous avons assigné son contenu, le `response.data`, à notre propriété `projects` afin de pouvoir plus tard récupérer chaque projet et les afficher sur la page comme d'habitude avec une directive `v-for`.

### Comment afficher chaque projet 

Il est maintenant temps d'afficher nos projets à l'intérieur du portfolio. Nous pouvons le faire avec la directive v-for.

La propriété projects dans ce cas contient un tableau d'objets. Chaque objet a ses propriétés que nous pouvons utiliser pour remplir notre template.

```html
<div id='app'>

    <div v-for="project in projects">
        <h2 class="title">{{project.full_name}}</h2>
        
        <div class="author">
            <img width="50px" :src="project.owner.avatar_url" alt="moi">
        </div>
        <div class="view">
            <a :href="project.html_url">Voir</a>
        </div>
    </div>

</div>
```

Ici, nous utilisons la directive v-for pour boucler sur le tableau de projets.
Maintenant, la variable `project` contient un objet qui représente un seul dépôt du compte GitHub.

En regardant l'objet de réponse, nous savons que nous pouvons récupérer un certain nombre de propriétés. Nous avons donc choisi `full_name`, le nom complet du dépôt, `owner.avatar_url`, l'URL de l'avatar du profil, et `html_url` qui est l'URL réelle de notre dépôt. C'est tout ce dont nous avons besoin pour l'instant.

Si nous regardons maintenant la page, nous verrons immédiatement tous les dépôts de notre compte.

Maintenant que nous savons comment effectuer une requête HTTP avec Axios et obtenir des données de GitHub, nous sommes presque prêts à commencer à construire notre portfolio.

Dans la section suivante, nous allons examiner une autre bibliothèque Vue appelée Vue-router que nous utiliserons dans notre projet final.


%[https://youtu.be/XJEmPr89HA8]


## Comment gérer le routage avec VueRouter

Notre portfolio aura sûrement plus d'une page, nous avons donc besoin d'un système qui comprenne où envoyer l'utilisateur lorsque, par exemple, il clique sur un lien dans la barre de navigation pour une page spécifique.

Pour cela, Vue dispose d'un package de routage officiel qui peut nous aider à faire exactement cela et à construire une application monopage (SPA).

Une application monopage est une application qui ne rafraîchit pas la page lorsqu'un utilisateur visite une nouvelle page afin que l'expérience utilisateur soit plus fluide.

Comme pour Vue et Axios, nous devons installer cette bibliothèque et nous le faisons via son CDN. Mais comme toujours, il existe également d'autres méthodes selon vos besoins. Je veux juste garder les choses simples pour l'instant, alors commençons par placer la balise script du CDN à l'intérieur du fichier HTML et apprenons les bases de cette nouvelle bibliothèque.

Vous pouvez regarder le tutoriel sur [YouTube ici](https://youtu.be/T_avTRFAEAg)
et consulter le dépôt sur [BitBucket](https://bitbucket.org/fbhood/how-to-vuejs/src/master/15-routing/).

Vous pouvez également consulter la documentation de Vue Router [ici](https://router.vuejs.org/installation.html#direct-download-cdn).

### Comment installer Vue Router via CDN

Prenons notre exemple précédent index.html et après le CDN VueJS, pointons vers le routeur `https://unpkg.com/vue-router@3.4.9/dist/vue-router.js`.

```html

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJS / API GitHub</title>
  
</head>
<body>
    <div id="app"> 
        <div v-for="project in projects">
            <h2 class="title">{{project.full_name}}</h2>
            
            <div class="author">
                <img width="50px" :src="project.owner.avatar_url" alt="moi">
            </div>
            <div class="view">
                <a :href="project.html_url">Voir</a>
            </div>
        </div>

    </div>
      <!-- CDN dernière version Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

    <!-- Version de développement VueJS -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    
    <!-- CDN Vue Router -->
    <script src="https://unpkg.com/vue-router@3.4.9/dist/vue-router.js"></script>
    
    <!-- Fichier script principal -->
    <script src="./main.js"></script>
</body>
</html>
```

### Comment utiliser Vue Router

Maintenant, notre application a accès au système de routeur et nous pouvons ajouter quelques routes pour notre application.

Nous pouvons le faire en utilisant le composant `router-link` fourni par la bibliothèque et son attribut `to` pour pointer le lien vers une page spécifique.

```html
<!-- Créer un lien de routeur en utilisant le composant 'router-link' et définir le chemin en utilisant l'attribut 'to' -->
<header>
    <nav>
        <router-link to="/">Accueil</router-link>
        <router-link to="/projects">Projets</router-link>
    </nav>
</header>

<!-- Afficher le composant pour la route correspondante -->
<router-view></router-view>
```

Nous avons également utilisé le composant router-view qui affichera un composant spécifique pour chaque route.

Maintenant, nous devons faire quelque chose à l'intérieur de notre fichier JavaScript pour que cela fonctionne.

Voyons les étapes que nous devons suivre :
- Définir les composants de route
- Définir les routes
- Créer une instance de routeur Vue
- Créer et monter l'instance racine Vue.

Tout d'abord, nous devons définir nos composants que nous utiliserons pour chaque route afin d'afficher le contenu de la page.

Nous créerons deux composants, un pour la page d'accueil et un pour la page des projets.

Pour simplifier les étapes, nous garderons tout dans le même fichier et nous refactoriserons plus tard.

Créons les deux premiers composants de base pour voir si le routeur fonctionne :

```js
// Créer les composants de route
const Home = {template: '<div>Mon Portfolio</div>'} 
const Projects = {template: '<div> Projets </div>'} 
```

Maintenant, suivons les étapes restantes et définissons les routes, créons l'instance du routeur vue, et créons et montons l'instance racine Vue.

```js

// Définir quelques routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects}
];
// Créer l'instance du routeur et lui passer les routes
const router = new VueRouter({
routes: routes
});
// Créer et monter l'instance racine.

let app = new Vue({
    router 
}).$mount('#app');
```

C'est tout. Si vous visitez la page d'accueil, vous verrez deux liens de navigation et le contenu du site changera en conséquence.

Rassemblons tout cela et commençons à construire notre portfolio.

Dans l'exemple précédent de la section Axios, nous avons demandé à l'API GitHub tous les dépôts publics d'un utilisateur et affiché le nom, l'avatar de l'utilisateur et l'URL du projet sur la page.

Déplaçons une partie de cette logique à l'intérieur de notre application qui utilise des routes.

Les principaux changements que nous devons apporter ici sont :
- déplacer le balisage HTML à l'intérieur de la propriété `template` du composant des projets
- déplacer les propriétés `data` à l'intérieur de l'objet `data` du composant
- déplacer le code que nous avons écrit dans le hook mounted à l'intérieur de notre composant.

Le code final ressemble à quelque chose comme ceci :
```js
// Définir les composants de route

const Home = {template: '<div>Mon Portfolio</div>'} 
const Projects = {
    
    template: `<div> 
         <div v-for="project in projects">
            <h2 class="title">{{project.full_name}}</h2>
            
            <div class="author">
                <img width="50px" :src="project.owner.avatar_url" alt="moi">
            </div>
            <div class="view">
                <a :href="project.html_url">Voir</a>
            </div>
        </div>
    </div>`,
    data(){
        return {
            projects: [],
            perPage: 20,
            page: 1
        }
    }, 
    mounted(){
        
         axios
         .get(`https://api.github.com/users/fabiopacifici/repos?per_page=${this.perPage}&page=${this.page}`)
         .then(
            response => {
                //console.log(response);
                this.projects = response.data;
            }
        )
        .catch(error=> {console.log(error);})
    }
} 

// Définir quelques routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects}
];
// Créer l'instance du routeur et lui passer les routes
const router = new VueRouter({
routes: routes
});
// Créer et monter l'instance racine.

let app = new Vue({
    router 
}).$mount('#app');
```

Le fichier HTML reste le même :

```html
<div id='app'>
  <header>
            <nav>
                <router-link to="/">Accueil</router-link>
                <router-link to="/projects">Projets</router-link>
            </nav>
        </header>

        <router-view></router-view>
</div>
```

Maintenant que nous avons une base sur laquelle travailler, améliorons-la. Nous utiliserons un prototype de design que j'ai réalisé avec Figma et ajouterons quelques fonctionnalités à notre portfolio pour le rendre agréable.

%[https://youtu.be/T_avTRFAEAg]

## Projet final – Comment construire un portfolio avec VueJS, VueRouter, Axios, API GitHub et déployer sur Netlify 

Nous sommes prêts à construire notre projet final ! Pour notre Vue-folio, nous allons repartir de là où nous nous sommes arrêtés dans la section précédente.

Nous allons construire une application monopage qui possède deux routes, une pour la page d'accueil et une pour la page des projets.

Voici les éléments constitutifs :
- Vuejs 
- Vue router
- Axios
- API REST GitHub
- Design de portfolio

Vous pouvez regarder ce tutoriel sur [YouTube ici](https://youtu.be/I6hQnWQU4rQ) et consulter le dépôt sur [BitBucket ici](https://bitbucket.org/fbhood/how-to-vuejs/src/master/16-final-project-portfolio/).

### Structure du projet

Pour accélérer les choses, nous allons simplement copier le code que nous avons écrit dans la section précédente.

La structure du projet sera la suivante :
```
|-- index.html
|-- assets/
    |-- css/
        |-- style.css
    |-- js/
        |-- main.js
    |-- img/
```

### Fichier index.html
Le fichier index.html est un peu différent de ce que nous avions dans la section précédente. Ici, nous placerons uniquement le composant router-view qui est responsable de l'affichage du composant correspondant à une route donnée.

Ensuite, nous placerons les `router-links` réels à l'intérieur de chaque composant pour nous assurer d'avoir le résultat souhaité conformément au design.

```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vuefolio</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100;300;400;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <link rel="stylesheet" href="./assets/css/style.css">
</head>

<body>

    <div id="app">

        <!-- Afficher le composant pour la route correspondante -->
        <router-view></router-view>

    </div>
    <footer> © Développé par <a href="https://fabiopacifici.com">Fabio Pacific</a> </footer>
    <!-- Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <!-- Version de développement VueJS -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- Vue Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
    <!-- Fichier Main Js -->
    <script src="./assets/js/main.js"></script>
</body>

</html>
```

### Fichier style.css
Puisqu'il ne s'agit pas d'un tutoriel CSS, pour la partie CSS, vous pouvez simplement copier le code du fichier du dépôt si vous suivez.
```css

    /* Classes utilitaires */
    .d_none {
        display: none;
    }
    .d_flex {
        display: flex;
    }
    .container {
        max-width: 1170px;
        margin: auto;
    }
    a {
        color: white;
    } 
    a:hover {
        color:#DB5461;
        
    }
    .loading {
        font-size: 2rem;
    }
    /* FIN Classes utilitaires */
    /* Composants */
    .bio__media {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        text-align: left;
    }
    .bio__media img {
        height: 120px;
    }
    .bio__media__text {
        padding: 1rem;
    }
    .bio__media__text h1{
        font-size: 36px;
        font-weight: 900;
        color: #DB5461;

    }
    .bio__media__text p {
        font-weight: 100;
        font-size: 16px;
        line-height: 1.5rem;
        
    }

    .card__custom {
        position: relative;
        display: flex;
        max-width: 400px;
        height: 300px;
        min-height: 300px;
        padding: 0.5rem;
        margin-bottom: 3rem;
        flex-grow: 1;
        flex-basis: calc(100% /2);
        align-items: center;
        justify-content: space-between;
    }
    .card__custom > .card__custom__text {
        max-width: calc((100% / 3) *2);
        text-align: right;
        height: 80%;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        overflow: hidden;

    }
    .card__custom__img {
        
        position: absolute;
        width: 70%;
        height: 100%;
        background-image: url(../img/cards_bg_img.svg);
        background-position: center;
        background-repeat: no-repeat;
        background-size: contain;
        display: inline-block;
        z-index: -1;
        left: 60%;
        transform: translateX(-50%);
        border-radius: 85px 0 100px 25px;

    }
    .card_custom__button a, .btn_load_more {
        background: #F1EDEE;
        border: 5px solid #3D5467;
        box-sizing: border-box;
        border-radius: 54px;
        padding: 0.5rem 1rem;
        font-weight: 900;
        color: #3D5467;
    }
    .card_custom__button a:hover, .btn_load_more:hover {
        cursor: pointer;
        background: #324555;
        color: white;
        border-color: #DB5461;
        transition: 1s;
    }
    .card__custom__text h3 {
        text-transform: uppercase;
        font-size: 1.5rem;
    }
    /* FIN Composant */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body{
        font-family: 'Raleway', Arial, Helvetica, sans-serif;
        color: white;
        background: linear-gradient(116.82deg, #3D5467 0%, #1A232B 99.99%, #333333 100%);

    }
    a {
    text-decoration: none;   
    }

    /* Page d'accueil */
    main#home {
        width: 100%;
        height: 100vh;
        min-height: 600px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #home > .about__me {
        text-align: center;
        width: 80%;
        line-height: 1.5rem;
    }
    #home > .about__me > h1 {
        margin: 20px 0 0;
        font-size: 36px;
        font-weight: 900;
        color: #DB5461;
    }
    #home > .about__me > h3 {
        font-size: 28px;
        font-weight: 500;

    }
    #home > .about__me > h1, #home > .about__me > h3  {
        font-style: normal;
        line-height: 42px;
        letter-spacing: 0.115em;

    }
    #home > .about__me p {
        font-weight: 100;
        font-size: 22px;
        padding: 2rem;
    }
    .skills_projects_link {
        position: relative;
    }
    .skills_projects_link > a {
        text-transform: uppercase;
        color: white;
        font-weight: 900;
        font-size: 18px;
        line-height: 21px;

    }
    .skills_projects_link > a:hover {
        color: #DB5461;
        transition: all 0.5s ease-in-out;

    }
    .skills_projects_link > a:hover::after {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        margin: auto;
        text-align: center;
        content: "";
        width: 30px;
        height: 2px;
        background-color: #DB5461;
        transition: background-color 0.5s ease-in-out;

    }

    /* En-tête */
    #site_header {
        text-align: center;
        padding: 2rem 0;
        justify-content: space-between;
        align-items: center;
    }
    #site_header > h1 {
        text-transform: uppercase;
    }
    nav a {
            color: #e2e2e2;
        text-transform: uppercase;
        font-weight: 900;
    }
    nav a:hover {
        color: #DB5461;
    }
    /* Section Page Portfolio */

    #portfolio {
        margin-top: 4rem;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-around;
    }
    .btn_load_more {

    }
    /* Compétences */

    #skills_section {
        margin-top: 4rem;
        min-height: 300px;
        background-image: url(../img/skills_bg.svg);
        background-repeat: no-repeat;
        background-size: contain;
        background-position: top left;
    }
    #skills_section h2 {
        margin-left: 180px;
        font-size: 44px;
        color: #F1EDEE;
        line-height: 2rem;

    }
    #skills_section ul {
        list-style: none;
        margin: 20px 120px;
        display: flex;
        flex-wrap: wrap;

    }
    #skills_section ul  li {
        padding: 1rem;
        margin: 0.5rem;
        background-color: #DB5461;
        border: 5px solid #3D5467;
        border-radius: 35px;
    }



    .avatar {
        width: 30px;
        height: auto;
        border-radius: 50%;
            margin: 0 1rem;

    }




    .card__back {
        display: none;
    }
    .rotate__card {
        transform: rotate3d(360,0,0,180deg);
    }
    /* Pied de page du site */

    footer {
        text-align: center;
        padding: 2rem 0;
    }



    /* Requête média */

    @media screen and (max-width: 475px) {
        .card {
            flex-basis: 100%;
            width: 100%;
        }
    }
```

## Structure de base du fichier Main.js
À l'intérieur du fichier main.js, nous avons le cœur de notre application monopage.
Ici, nous définirons les composants de route qui doivent être rendus pour chaque vue/page, la page d'accueil et les composants de projets.

Ensuite, nous définirons deux routes, une pour la page d'accueil et une pour la page des projets, créerons une instance de routeur et la passerons aux routes. Enfin, nous créerons une nouvelle instance Vue et lui passerons l'instance de routeur et monterons l'élément HTML racine.

Commençons par les composants de route.

### Comment définir des composants pour chaque vue
Le composant de la page d'accueil est assez simple.

```js
// Composant Page d'accueil
const Home = {
    template: 
    `<main id="home">
        <div class="about__me">
            <img src="./assets/img/avatar.svg" alt="">
            <h1>John Doe</h1>
            <h3>Expert Python</h3>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
    
            <div class="skills_projects_link">
                <router-link to="/projects">Projets/Compétences</router-link> 
            </div>
        </div>
    </main>`
}
```
Décortiquons cela. Tout d'abord, nous créons une constante Home qui contiendra l'objet du composant du routeur.

À l'intérieur de l'objet, la seule chose que nous mettrons est la propriété template avec un balisage pour rendre notre page. La chose principale à remarquer ici est le composant router-link qui pointera vers la route /projects depuis la page d'accueil.

Ensuite, créons un composant de route pour la page des projets. Nous avons beaucoup à faire ici, alors pour l'instant, ajoutons simplement du code passe-partout – nous y reviendrons plus tard et écrirons étape par étape toute la logique.

```js
const Projects = {
    template: 
    `<div>
        <h1>Projets</h1>
    </div>`,
    data() { 
        return {
                // Objet data ici
            }
    },
    methods: {
        // Toutes les méthodes ici
    },
    mounted(){  
        // Hook de cycle de vie      
        
    }
}
```
Les composants de route Projects ont une propriété `template` qui, pour l'instant, contient un balisage de base qui n'affiche qu'un titre `h1`.

Après cela, il y a la méthode data du composant qui renvoie un objet vide, puis un objet methods vide et un hook de cycle de vie vide.

C'est tout ce dont nous avons besoin, pour l'instant, alors passons à la suite et définissons le reste des éléments constitutifs, les routes, le routeur et les instances Vue.


### Comment définir les routes, le routeur et l'instance Vue
Maintenant que nous avons deux composants à afficher sur nos pages principales, nous pouvons passer aux étapes suivantes :
- définir les routes
- créer l'instance du routeur
- créer et monter l'instance Vue

Tout d'abord, définissons nos deux routes et lions les composants.
```js

// Définir les routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects},
];
```
Dans le code, nous avons défini une nouvelle constante appelée routes. À l'intérieur, nous avons défini deux routes sous forme de tableau d'objets.

Chaque objet possède deux propriétés :
- path
- component

Le premier objet est pour la page d'accueil. Son chemin répondra aux requêtes faites à l'URL de base de notre site Web, comme https://fabiopacifici.com/.

Ensuite, la propriété component lie cette page au composant de la route appelé `Home` que nous avons défini à l'étape précédente.

Le deuxième objet est pour la page des projets. Le chemin répond aux requêtes faites à `/projects` et il est lié au composant de route `Projects`.

Maintenant que nous avons nos routes :

```js

// créer l'instance du routeur
const router = new VueRouter({
    routes
})
```
Ci-dessus, nous avons utilisé la syntaxe ES6 qui nous permet de mettre simplement le nom de la variable contenant les routes puisqu'il est égal au nom de la propriété que nous devions utiliser. C'est en fait la même chose que d'écrire `routes: routes`.

Maintenant, nous créons une instance Vue. Injectons l'instance du routeur à l'intérieur et montons enfin l'élément racine.

```js

// créer et monter l'instance vue
const app = new Vue({
    router
}).$mount('#app');
```

C'est fait ! Nous avons maintenant tout en place pour commencer à construire notre portfolio et compléter le composant de route Projects.

## Comment construire le composant principal de la route Projets
Nous allons commencer à travailler sur l'objet data. Ici, nous devons définir des propriétés qui contiendront tous nos projets une fois que nous aurons récupéré les données de l'API GitHub.

### L'objet data
Pour faciliter les choses, j'ai intentionnellement limité les résultats à 20. Si vous estimez que ce n'est pas suffisant, vous pouvez modifier le code comme vous le souhaitez.

Vous pouvez implémenter la pagination pour vos résultats en augmentant la propriété page qui sera transmise à la chaîne de requête ou renvoyer plus de résultats par page en augmentant la valeur de la propriété `perPage`.

```js
data() { 
    return {
        projects: [],
        projectsList: null,
        skills: [],
        projectsCount: 5,
        perPage: 20,
        page: 1,
        loading: true,
        errors: false,
        }
    },
```

Comme nous l'avons appris dans la section où nous avons utilisé Axios pour récupérer des données de l'API REST GitHub, il y a quelques propriétés que nous devons définir.

La fonction data du composant renvoie un objet avec une propriété `projects` où nous stockerons tous les projets que nous récupérons de GitHub.

Ensuite, nous ajoutons une propriété `projectsList` qui ne contient que quelques projets à la fois. Nous utiliserons cette propriété plus tard pour implémenter une fonctionnalité de chargement supplémentaire très simple en combinaison avec la propriété `projectsCount`.

Ensuite, nous avons une propriété `skills` où nous stockerons tous les langages utilisés pour construire nos projets.

Nous utiliserons les propriétés `perPage: 20` et `page: 1` pour construire la chaîne de requête utilisée pour récupérer les données de GitHub. Elle prendra 20 projets et ne renverra que la première page de résultats, à moins que nous ne changions ces valeurs.

Enfin, nous avons une propriété `loading: true` que nous utiliserons pour vérifier si la page récupère des données et une propriété `errors: false` qui affiche un message d'erreur au cas où nous ne parviendrions pas à nous connecter au serveur GitHub.

Dans l'étape suivante, nous commencerons à travailler sur toutes les méthodes requises pour faire fonctionner notre application.

### La méthode de récupération de toutes les données

La première méthode est celle que nous utiliserons pour récupérer les données de GitHub.

Cette méthode effectuera l'appel Ajax vers l'API REST GitHub en utilisant Axios et stockera la réponse dans une propriété de l'instance Vue :
```js

 fetchData: function(){
            axios
            .get(`https://api.github.com/users/fbhood/repos?per_page=${this.perPage}&page=${this.page}`)
            .then(
                response => {
                    
                    this.projects = response.data;
                    this.projects.forEach(project =>{
                        if (project.language !== null && ! this.skills.includes(project.language)) { 
                            this.skills.push(project.language)
                        };
                    });
                }
            )
            .catch(error=> {
                console.log(error);
                this.errors = true;
            })
            .finally(() => { 
                this.loading = false
                this.getProjects();
            })
        }, 
```

Décortiquons cela. Tout d'abord, nous avons défini une méthode appelée `fetchData: function(){}`. Cette méthode utilise Axios pour effectuer un appel API vers l'API REST.

Dans la méthode `.get()`, nous avons construit l'URL en utilisant également les propriétés `perPage` et `page` comme faisant partie de la chaîne de requête.

La méthode get renvoie une promesse, nous avons donc utilisé la méthode `.then()` sur la promesse pour gérer la réponse en utilisant une fonction fléchée `response => {}`.

À l'intérieur de la fonction fléchée, nous avons stocké les données de réponse à l'intérieur de la propriété projects de l'instance Vue en utilisant ` this.projects = response.data;`.

Ensuite, nous avons utilisé une boucle `forEach` pour itérer sur chaque projet et stocker le langage utilisé dans le dépôt en tant que compétence en utilisant le code ci-dessous :

```js
this.projects.forEach(project =>{
    if (project.language !== null && ! this.skills.includes(project.language)) { 
        this.skills.push(project.language)
    };
});
```

Nous avons enchaîné une méthode `.catch` pour gérer une erreur au cas où nous ne parviendrions pas à nous connecter à l'API REST et à récupérer les données. Nous enregistrerons l'erreur dans la console et mettrons à jour la valeur de la propriété `errors` à true afin de pouvoir afficher un message d'erreur personnalisé à l'utilisateur plus tard.

Enfin, nous avons enchaîné la méthode `.finally()` qui sera exécutée après la gestion de la réponse. Nous avons également mis à jour la propriété `loading` et l'avons définie sur false afin de pouvoir afficher les résultats à l'utilisateur.

À l'intérieur de la méthode `finally`, nous pouvons également appeler une méthode (que nous devons encore créer) et que nous utiliserons pour découper les résultats plus tard.

Construisons-la.

### La méthode de récupération des projets
Cette méthode prend une partie des projets que nous avons réellement stockés dans la propriété `projects`. Nous pouvons utiliser la propriété `projectsList` pour stocker la tranche et implémenter plus tard une méthode pour les incrémenter avec un bouton d'affichage supplémentaire.
```js

getProjects: function(){

    this.projectsList = this.projects.slice(0, this.projectsCount);
    return this.projectsList;

},
```
La méthode getProjects prend une partie de tous les projets stockés dans la propriété `projects` en utilisant la méthode slice de tableau en conjonction avec la propriété `projectsCount` qui est définie sur cinq. Elle n'y stockera donc que les cinq premiers résultats et les renverra.

Pour ajouter cinq projets supplémentaires à la propriété `projectsList`, nous aurons également besoin d'une méthode que l'utilisateur peut appeler lorsqu'il clique sur le bouton de chargement supplémentaire. Créons-la.

### La méthode de chargement de plus de projets
La méthode load more vérifiera d'abord si la longueur du tableau `projects` est inférieure ou égale à la longueur du tableau `projectsList`. Ensuite, si ce n'est pas le cas, elle incrémentera la valeur de la propriété `projectsCount` de cinq et prendra ensuite une tranche plus grande de la propriété `projects`.

```js

loadMore(){
            
    if(this.projectsList.length <= this.projects.length){
        this.projectsCount += 5;
        this.projectsList = this.projects.slice(0, this.projectsCount)
    }
    

}
```

### Construire le template
Dans la propriété template du composant `Projects`, nous pouvons commencer par la section d'en-tête. Nous y mettrons également deux composants `router-link` pour la navigation dans les pages :

```html
`<div>
        <header id="site_header" class="container d_flex">
            <div class="bio__media">
                <img src="./assets/img/avatar.svg" alt="">
                <div class="bio__media__text">
                    <h1>John Doe</h1>
                    <h3>Expert Python</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
                </div>
            </div>
            <nav>
                <router-link to='/'>Accueil</router-link>
                <router-link to="/projects">Projet</router-link>
                <a href="https://">
                    <i class="fab fa-github fa-lg fa-fw"></i>
                </a>
            </nav>
        </header>

</div>
```
Ensuite, nous pouvons continuer à travailler sur le template et créer la section principale.
Nous placerons le balisage suivant toujours dans le div principal du template, juste sous la balise fermante de l'en-tête.

Commençons par placer le conteneur principal :

```html
<main class="container">
    <!-- Afficher un message d'erreur si l'API REST ne fonctionne pas -->
    <!-- Sinon afficher une section pour nos projets de portfolio et la section des compétences -->
</main>
```

À l'intérieur du conteneur, utilisons les directives v-if-else pour afficher un message d'erreur ou la section des projets :

```html
 <!-- Afficher les erreurs si l'api rest ne fonctionne pas -->
    <div class="error" v-if="errors"> 
        Désolé ! Il semble que nous ne puissions pas récupérer les données pour le moment 😥
    </div>
    <!-- Sinon afficher la section portfolio -->
    <section id="portfolio" v-else></section>
```
Pour faire fonctionner le code, nous avons utilisé la directive v-if et lui avons passé la propriété `errors`. Cette propriété sera définie sur `true` s'il y a une erreur pendant que nous récupérons les données de GitHub ou sera définie sur `false` si tout va bien. Ainsi, la directive v-else affichera la section portfolio.

Ensuite, nous devons afficher un message 'chargement...' pendant que nous récupérons les données. Une fois terminé, nous pouvons utiliser la directive v-for pour boucler sur les résultats. Donc, juste dans la section portfolio, nous écrirons une autre directive v-if-else.

```html
<section id="portfolio" v-else>
 <!-- Utiliser une directive v-if pour afficher le message de chargement -->
        <div class="loading" v-if="loading">😴 Chargement ... </div>

        <!-- utiliser une directive v-for pour boucler sur le tableau projectsList -->
        <div v-for="project in projectsList" class="card__custom" v-else></div>

</section>
```

Ici, nous utilisons la directive v-if `<div class="loading" v-if="loading">😴 Chargement ... </div>` pour afficher un message de chargement. Après cela, le `<div v-for="project in projectsList" class="card__custom" v-else></div>` possède deux directives, la directive v-for que nous utilisons pour boucler sur la propriété `projectsList` et une directive v-else qui affichera cet élément lorsque nous aurons fini de récupérer les données de GitHub.

Nous pouvons maintenant utiliser la variable `project` pour afficher tous les détails du projet dans notre balisage :

```html
<!-- utiliser une directive v-for pour boucler sur le tableau projectsList -->
<div v-for="project in projectsList" class="card__custom" v-else>
    <div class="card__custom__text">
        <div>
            <!-- Créer une méthode personnalisée pour tronquer le nom du projet afin qu'il ne casse pas le design -->
            <h3>{{project.name}}</h3>
            <!-- Créer un trimmedText personnalisé pour tronquer la description -->
            <p>{{project.description}}</p>                        
        </div>

        <div class="meta__data d_flex">
            <div class="date">
                <h5>Mis à jour le</h5>
                <div>{{new Date(project.updated_at).toDateString()}}</div>
            </div>
            <img class="avatar" :src="project.owner.avatar_url">

        </div>
    </div>
    <div class="card__custom__img"></div>
    <div class="card_custom__button">
        <a :href="project.html_url" target="_blank">
            Code
        </a>
    </div>

</div>
```
Pour afficher le titre et la description du projet, nous avons utilisé les propriétés `project.name` et `project.description`. Mais la description et le titre casseront notre design à moins que nous ne les tronquions à un moment donné.

Ensuite, dans l'élément avec la classe `date`, nous avons affiché les données du projet dans un format lisible en utilisant la méthode ` new Date().toDateString()`.

Pour afficher l'avatar de l'utilisateur `<img class="avatar" :src="project.owner.avatar_url">`, nous avons utilisé le raccourci de la directive v-bind afin de pouvoir utiliser la propriété `project.owner.avatar_url` pour récupérer l'URL de l'avatar.

Enfin, pour afficher un bouton qui, une fois cliqué, redirige l'utilisateur vers la page du dépôt, nous avons lié l'attribut `href` à la propriété `project.html_url` `<a :href="project.html_url" target="_blank">Code</a>`.

Notre carte de projet est complète. La prochaine chose que nous devons faire est d'afficher un bouton de chargement supplémentaire pour montrer plus de projets.

Nous travaillons toujours à l'intérieur de la section `projects`. Juste après la carte du projet, nous pouvons écrire le balisage suivant

```html
<!-- Afficher un bouton de chargement supplémentaire -->
<div style="text-align: center; width:100%" v-if="!loading" >
    <div v-if="projectsList.length < projects.length">
        <button class="btn_load_more" v-on:click="loadMore()">Charger plus</button>
    </div>
    <div v-else>
        <a href="" target="_blank" rel="noopener noreferrer">Visitez mon GitHub</a>
    </div>

</div>
```
La directive v-if vérifie d'abord si la propriété loading est définie sur false.
Si c'est le cas, nous utiliserons une autre directive v-if pour vérifier si la longueur de la propriété `projectsList` est inférieure à la longueur de la propriété `projects`.

Si c'est le cas, elle affichera un bouton qui utilise une directive v-on pour écouter les clics
`<button class="btn_load_more" v-on:click="loadMore()">Charger plus</button>` et déclencher une méthode `loadMore()`. Sinon, nous affichons un lien vers le compte GitHub.

Après cela, nous pouvons afficher une liste de compétences liées à tous les projets :

```html
<!-- Afficher une section de compétences -->
<div id="skills_section">
    <h2>Compétences de développement</h2>
    <ul class="skills">
        <!-- Boucler sur la propriété skills -->
        <li v-for="skill in skills">{{skill}}</li>
    </ul>
</div>
```
Notre balisage est complet, mais nous devons améliorer un peu notre code car le titre du projet et sa description cassent notre design !

Créons deux méthodes, une pour tronquer le titre et une pour le texte de description.

### Les méthodes trimText et trimTitle
La méthode `trimTitle` remplacera tous les `-` et `_` par un espace, et limitera le nombre de caractères à 12. La méthode `trimText` quant à elle réduit seulement le nombre de caractères de la description au-delà de 100 caractères.

```js
trimTitle: function(text){
    let title = text.replaceAll("-", " ").replace("_", " ")
    if(title.length > 15) {
        return title.slice(0, 12) + ' ...'
    } return title;

},
trimText: function(text){
    //console.log(text.slice(0, 100));
    if(text.length > 100) {
        return text.slice(0, 100) + ' ...'
    } return text;
},
```

Avec ces deux méthodes, nous pouvons maintenant mettre à jour le balisage et les utiliser pour nous assurer que rien ne casse le design.

Mettons à jour ces deux lignes qui passeront de ceci :
```html
<!-- Créer une méthode personnalisée pour tronquer le nom du projet afin qu'il ne casse pas le design -->
<h3>{{project.name}}</h3>
<!-- Créer un trimmedText personnalisé pour tronquer la description -->
<p>{{project.description}}</p>   
```

À ceci :
```html
<h3>{{trimedTitle(project.name)}}</h3>
<p>{{trimedText(project.description)}}</p>   
```


Mettons tout ensemble. Le balisage final sera le suivant :

```html
<div>
    <header id="site_header" class="container d_flex">
        <div class="bio__media">
            <img src="./assets/img/avatar.svg" alt="">
            <div class="bio__media__text">
                <h1>John Doe</h1>
                <h3>Expert Python</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
            </div>
        </div>
        <nav>
            <router-link to='/'>Accueil</router-link>
            <router-link to="/projects">Projet</router-link>
            <a href="https://">
                <i class="fab fa-github fa-lg fa-fw"></i>
            </a>
        </nav>
    </header>

        <main class="container">
        <div class="error" v-if="errors"> 
            Désolé ! Il semble que nous ne puissions pas récupérer les données pour le moment 😥
        </div>

        <section id="portfolio" v-else>
            <div class="loading" v-if="loading">😴 Chargement ... </div>
            <div class="projects" v-else>
                    <div v-for="project in projectsList" class="card__custom" >
                    <div class="card__custom__text">
                        <div>
                            <h3>{{trimedTitle(project.name)}}</h3>
                            <p>{{trimedText(project.description)}}</p>                        
                        </div>
                
                        <div class="meta__data d_flex">
                            <div class="date">
                                <h5>Mis à jour le</h5>
                                <div>{{new Date(project.updated_at).toDateString()}}</div>
                            </div>
                            <img class="avatar" :src="project.owner.avatar_url">
                
                        </div>
                    </div>
                    <div class="card__custom__img"></div>
                    <div class="card_custom__button">
                        <a :href="project.html_url" target="_blank">
                            Code
                        </a>
                    </div>
                
                
                </div>


                <div style="text-align: center; width:100%" v-if="!loading" >
                    <div v-if="projectsList.length < projects.length">
                        <button class="btn_load_more" v-on:click="loadMore()">Charger plus</button>
                    </div>
                    <div v-else>
                        <a href="" target="_blank" rel="noopener noreferrer">Visitez mon GitHub</a>
                    </div>

                </div>

                <div id="skills_section">
                    <h2>Compétences de développement</h2>
                    <ul class="skills">
                        <li v-for="skill in skills">{{skill}}</li>
                    </ul>
                </div>
            </div>
        </section>  
    </main>
</div>
```

Il reste une dernière chose à faire. Étant donné que la récupération des données de GitHub est très rapide, nous ne voyons pas vraiment le message de chargement. Définissons un délai d'attente et retardons-le de quelques secondes – vous pourrez ensuite l'ajuster comme vous le souhaitez.

### Le hook de cycle de vie mounted

```
 mounted(){  

        setTimeout(this.fetchData, 3000 );
        
    }
```
À l'intérieur du hook de cycle de vie mounted, nous avons utilisé `setTimeout()` et appelé la méthode `fetchData` comme premier paramètre. Ensuite, pour le deuxième paramètre, nous avons spécifié que cette méthode devait être exécutée après 3000 millisecondes (3 secondes).


## Voyons notre code final tout ensemble
Le fichier Index.html ressemble à ce qui suit :

```html

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vuefolio</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100;300;400;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <link rel="stylesheet" href="./assets/css/style.css">
</head>

<body>

    <div id="app">

        <!-- Afficher le composant pour la route correspondante -->
        <router-view></router-view>

    </div>
    <footer> © Développé par <a href="https://fabiopacifici.com">Fabio Pacific</a> </footer>
    <!-- Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <!-- Version de développement VueJS -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- Vue Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
    <!-- Fichier Main Js -->
    <script src="./assets/js/main.js"></script>
</body>

</html>
```

Et voici le fichier main.js :

```js
// Créer les composants de route
const Home = {
    template: 
    `<main id="home">
        <div class="about__me">
            <img src="./assets/img/avatar.svg" alt="">
            <h1>John Doe</h1>
            <h3>Expert Python</h3>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
    
            <div class="skills_projects_link"><router-link to="/projects">Projets/Compétences</router-link> </div>
        </div>
    </main>`
}
const Projects = {
    template: 
    `<div>
        <header id="site_header" class="container d_flex">
            <div class="bio__media">
                <img src="./assets/img/avatar.svg" alt="">
                <div class="bio__media__text">
                    <h1>John Doe</h1>
                    <h3>Expert Python</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
                </div>
            </div>
            <nav>
                <router-link to='/'>Accueil</router-link>
                <router-link to="/projects">Projet</router-link>
                <a href="https://">
                    <i class="fab fa-github fa-lg fa-fw"></i>
                </a>
            </nav>
        </header>
    
         <main class="container">
            <div class="error" v-if="errors"> 
                Désolé ! Il semble que nous ne puissions pas récupérer les données pour le moment 😥
            </div>

            <section id="portfolio" v-else>
                <div class="loading" v-if="loading">😴 Chargement ... </div>
                <div class="projects" v-else>
                     <div v-for="project in projectsList" class="card__custom" >
                        <div class="card__custom__text">
                            <div>
                                <h3>{{trimedTitle(project.name)}}</h3>
                                <p>{{trimedText(project.description)}}</p>                        
                            </div>
                    
                            <div class="meta__data d_flex">
                                <div class="date">
                                    <h5>Mis à jour le</h5>
                                    <div>{{new Date(project.updated_at).toDateString()}}</div>
                                </div>
                                <img class="avatar" :src="project.owner.avatar_url">
                    
                            </div>
                        </div>
                        <div class="card__custom__img"></div>
                        <div class="card_custom__button">
                            <a :href="project.html_url" target="_blank">
                                Code
                            </a>
                        </div>
                    
                    
                    </div>


                    <div style="text-align: center; width:100%" v-if="!loading" >
                        <div v-if="projectsList.length < projects.length">
                            <button class="btn_load_more" v-on:click="loadMore()">Charger plus</button>
                        </div>
                        <div v-else>
                            <a href="" target="_blank" rel="noopener noreferrer">Visitez mon GitHub</a>
                        </div>

                    </div>

                    <div id="skills_section">
                        <h2>Compétences de développement</h2>
                        <ul class="skills">
                            <li v-for="skill in skills">{{skill}}</li>
                        </ul>
                    </div>
                </div>
            </section>
        
           
        </main>
    </div>`,
data() { 
    return {
        data: [],
        projects: [],
        projectsList: null,
        skills: [],
        projectsCount: 5,
        perPage: 20,
        page: 1,
        loading: true,
        errors: false,
        }
    },
    methods: {
        trimedTitle: function(text){
            let title = text.replaceAll("-", " ").replace("_", " ")
            if(title.length > 15) {
                return title.slice(0, 12) + ' ...'
            } return title;
        
        },
        trimedText: function(text){
            //console.log(text.slice(0, 100));
            if(text === null) {
                return 'Ce projet n\'a pas encore de description !';
            } else if(text.length > 100) {
                return text.slice(0, 100) + ' ...'
            } 
            return text;
        
        },
        getProjects: function(){

            this.projectsList = this.projects.slice(0, this.projectsCount);
            return this.projectsList;
        
        },
        fetchData: function(){
            axios
            .get(`https://api.github.com/users/fbhood/repos?per_page=${this.perPage}&page=${this.page}`)
            .then(
                response => {
                    this.projects = response.data;
                    this.projects.forEach(project =>{
                        if (project.language !== null && ! this.skills.includes(project.language)) { 
                            this.skills.push(project.language)
                        };
                    });
                }
            )
            .catch(error=> {
                console.log(error);
                this.errors = true;
            })
            .finally(() => { 
                this.loading = false
                this.getProjects();
            })
        }, 
        loadMore(){
            
            if(this.projectsList.length <= this.projects.length){
                this.projectsCount += 5;
                this.projectsList = this.projects.slice(0, this.projectsCount)
            }
            
        
        }
        
    },
    mounted(){  

        setTimeout(this.fetchData, 3000 );
        
    }
}

// Définir les routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects},
];


// créer l'instance du routeur
const router = new VueRouter({
    routes
})

// créer et monter l'instance vue
const app = new Vue({
    router
}).$mount('#app');
```

Côté CSS, voici ce que nous avons :

```css

/* Classes utilitaires */
.d_none {
    display: none;
}
.d_flex {
    display: flex;
}
.container {
    max-width: 1170px;
    margin: auto;
}
a {
    color: white;
} 
a:hover {
    color:#DB5461;
    
}
.loading {
    font-size: 2rem;
}
/* FIN Classes utilitaires */
/* Composants */
.bio__media {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    text-align: left;
}
.bio__media img {
    height: 120px;
}
.bio__media__text {
    padding: 1rem;
}
.bio__media__text h1{
    font-size: 36px;
    font-weight: 900;
    color: #DB5461;

}
.bio__media__text p {
    font-weight: 100;
    font-size: 16px;
    line-height: 1.5rem;
    
}

.card__custom {
    position: relative;
    display: flex;
    max-width: 400px;
    height: 300px;
    min-height: 300px;
    padding: 0.5rem;
    margin-bottom: 3rem;
    flex-grow: 1;
    flex-basis: calc(100% /2);
    align-items: center;
    justify-content: space-between;
}
.card__custom > .card__custom__text {
    max-width: calc((100% / 3) *2);
    text-align: right;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    overflow: hidden;

}
.card__custom__img {
    
    position: absolute;
    width: 70%;
    height: 100%;
    background-image: url(../img/cards_bg_img.svg);
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    display: inline-block;
    z-index: -1;
    left: 60%;
    transform: translateX(-50%);
    border-radius: 85px 0 100px 25px;

}
.card_custom__button a, .btn_load_more {
    background: #F1EDEE;
    border: 5px solid #3D5467;
    box-sizing: border-box;
    border-radius: 54px;
    padding: 0.5rem 1rem;
    font-weight: 900;
    color: #3D5467;
}
.card_custom__button a:hover, .btn_load_more:hover {
    cursor: pointer;
    background: #324555;
    color: white;
    border-color: #DB5461;
    transition: 1s;
}
.card__custom__text h3 {
    text-transform: uppercase;
    font-size: 1.5rem;
}
/* FIN Composant */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    font-family: 'Raleway', Arial, Helvetica, sans-serif;
    color: white;
    background: linear-gradient(116.82deg, #3D5467 0%, #1A232B 99.99%, #333333 100%);

}
a {
 text-decoration: none;   
}

/* Page d'accueil */
main#home {
    width: 100%;
    height: 100vh;
    min-height: 600px;
    display: flex;
    justify-content: center;
    align-items: center;
}
#home > .about__me {
    text-align: center;
    width: 80%;
    line-height: 1.5rem;
}
#home > .about__me > h1 {
    margin: 20px 0 0;
    font-size: 36px;
    font-weight: 900;
    color: #DB5461;
}
#home > .about__me > h3 {
    font-size: 28px;
    font-weight: 500;

}
#home > .about__me > h1, #home > .about__me > h3  {
    font-style: normal;
    line-height: 42px;
    letter-spacing: 0.115em;

}
#home > .about__me p {
    font-weight: 100;
    font-size: 22px;
    padding: 2rem;
}
.skills_projects_link {
    position: relative;
}
.skills_projects_link > a {
    text-transform: uppercase;
    color: white;
    font-weight: 900;
    font-size: 18px;
    line-height: 21px;

}
.skills_projects_link > a:hover {
    color: #DB5461;
    transition: all 0.5s ease-in-out;

}
.skills_projects_link > a:hover::after {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    margin: auto;
    text-align: center;
    content: "";
    width: 30px;
    height: 2px;
    background-color: #DB5461;
    transition: background-color 0.5s ease-in-out;

}

/* En-tête */
#site_header {
    text-align: center;
    padding: 2rem 0;
    justify-content: space-between;
    align-items: center;
}
#site_header > h1 {
    text-transform: uppercase;
}
nav a {
        color: #e2e2e2;
    text-transform: uppercase;
    font-weight: 900;
}
nav a:hover {
    color: #DB5461;
}
/* Section Page Portfolio */

#portfolio {
    margin-top: 4rem;
    
}


#portfolio .projects {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-around;
}
/* Compétences */

#skills_section {
    margin-top: 4rem;
    min-height: 300px;
    background-image: url(../img/skills_bg.svg);
    background-repeat: no-repeat;
    background-size: contain;
    background-position: top left;
}
#skills_section h2 {
    margin-left: 180px;
    font-size: 44px;
    color: #F1EDEE;
    line-height: 2rem;

}
#skills_section ul {
    list-style: none;
    margin: 20px 120px;
    display: flex;
    flex-wrap: wrap;

}
#skills_section ul  li {
    padding: 1rem;
    margin: 0.5rem;
    background-color: #DB5461;
    border: 5px solid #3D5467;
    border-radius: 35px;
}



.avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
        margin: 0 1rem;

}


.card__back {
    display: none;
}
.rotate__card {
    transform: rotate3d(360,0,0,180deg);
}
/* Pied de page du site */

footer {
    text-align: center;
    padding: 2rem 0;
}



/* Requête média */

@media screen and (max-width: 475px) {
    .card {
        flex-basis: 100%;
        width: 100%;
    }
}
```

C'est tout ! Nous sommes prêts à déployer notre code en production.


%[https://youtu.be/I6hQnWQU4rQ]

## Déploiement continu avec BitBucket et Netlify

La dernière étape consiste à déployer nos projets afin que d'autres puissent les voir. Pour ce faire, nous utiliserons deux services :

- BitBucket, un dépôt de code source basé sur git pour l'hébergement (vous pouvez utiliser GitHub si vous préférez)
- Netlify, une société d'hébergement Web qui fournit l'hébergement pour les sites Web dont les fichiers de code source sont stockés dans un système de contrôle de version Git.

Vous pouvez regarder cette vidéo finale sur [YouTube ici](https://youtu.be/BH5I68DzcYQ).

Vous pouvez également consulter les dépôts finaux sur BitBucket :
- [SimpleTwitter](https://bitbucket.org/fbhood/simple-twitter/src/master/)
- [VuePortfolio](https://bitbucket.org/fbhood/vue-folio/src)


### Créer les dossiers du projet et copier tous les fichiers
Tout d'abord, créez deux dossiers – un pour chaque projet :
- vue-folio
- simple-twitter
puis copiez tous les fichiers des projets dans le dossier correspondant.

### Initialiser un dépôt git
Ensuite, nous devons initialiser le dépôt git localement.

```
cd vue-folio 
git init
git add .
git commit -m"Initial Commit"
```
Vous devez exécuter les commandes ci-dessus dans un terminal, vous devez donc avoir git installé sur votre système. Si ce n'est pas le cas, vous pouvez lire comment faire [ici](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Avec la première commande, nous naviguons vers le dossier du projet appelé `vue-folio`. Ensuite, nous initialisons un dépôt git, ajoutons tous les fichiers à la zone de staging et effectuons le commit des fichiers.

Répétez les étapes ci-dessus pour les deux dossiers de projets.

### Créer un dépôt BitBucket ou GitHub
Je suppose que vous avez déjà un compte sur GitHub ou BitBucket. Mais si ce n'est pas le cas, allez-y et créez-en un.

Suivez les étapes de la vidéo pour créer les dépôts et les connecter à vos dépôts locaux.


### Créer un compte sur Netlify et créer un site
Vous pouvez utiliser le plan gratuit de Netlify pour les projets privés, les sites Web de loisirs et les expériences. C'est un choix parfait pour notre tutoriel.

Suivez les étapes de la vidéo pour y déployer vos projets.



%[https://youtu.be/BH5I68DzcYQ]

## Et après ?
Dans un prochain tutoriel, je vous montrerai également comment tester votre code, passer à Vue3, et plus encore.

### Merci de m'avoir lu !

J'espère que vous avez apprécié ce tutoriel et les vidéos qui l'accompagnent. Si c'est le cas, n'hésitez pas à partager l'article et à cliquer sur le bouton "j'aime" des vidéos. Vous pouvez également activer les notifications en cliquant sur l'icône de la cloche pour savoir quand ma prochaine vidéo sera en ligne.

Si vous avez des questions, n'hésitez pas à me contacter. Je réponds à tous les commentaires YouTube.

N'oubliez pas de vous abonner à ma chaîne YouTube [ici](https://youtube.com/channel/UCTuFYi0pTsR9tOaO4qjV_pQ).