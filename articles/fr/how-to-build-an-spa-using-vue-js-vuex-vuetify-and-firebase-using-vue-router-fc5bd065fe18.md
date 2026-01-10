---
title: 'Comment créer une SPA avec Vue.js, Vuex, Vuetify et Firebase : utiliser Vue
  Router'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-24T17:28:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-spa-using-vue-js-vuex-vuetify-and-firebase-using-vue-router-fc5bd065fe18
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_oxBC3QDl02cB2MDOzGXZg.png
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: vue
  slug: vue
- name: Vue.js
  slug: vuejs
seo_title: 'Comment créer une SPA avec Vue.js, Vuex, Vuetify et Firebase : utiliser
  Vue Router'
seo_desc: 'By Jennifer Bland

  Part 2: learn how to use Vue Router with your SPA


  Meal Prep application

  Learn how to create a meal delivery website using Vue.js, Vuex, Vue Router, and
  Firebase.

  This is part two of my four-part series on building a Vue application...'
---

Par Jennifer Bland

#### Partie 2 : apprendre à utiliser Vue Router avec votre SPA

![Image](https://cdn-media-1.freecodecamp.org/images/E1pvqQ1jnZas610gycuziZk7Tu8KaK6uygz8)
_Application Meal Prep_

Apprenez à créer un site web de livraison de repas en utilisant Vue.js, Vuex, Vue Router et Firebase.

Ceci est la deuxième partie de ma série en quatre parties sur la création d'une application Vue. Voici la liste de toutes les parties :

[Partie 1 : Installation de Vue et création d'une SPA en utilisant Vuetify et Vue Router](https://medium.freecodecamp.org/how-to-build-a-single-page-application-using-vue-js-vuex-vuetify-and-firebase-838b40721a07)

[Partie 2 : Utilisation de Vue Router](https://medium.com/p/fc5bd065fe18)

[Partie 3 : Utilisation de Vuex et accès à l'API](https://medium.com/p/f8036aa464ad)

[Partie 4 : Utilisation de Firebase pour l'authentification](https://medium.com/p/d9932d1e4365)

### Récapitulatif

Dans la première partie de cette série, nous avons créé notre application Vue en utilisant le CLI Vue. De plus, nous avons ajouté Vuetify à l'application. J'utilise Vuetify pour styliser l'application. Je vais également profiter des nombreux composants d'interface utilisateur qu'il offre.

Après avoir tout installé, nous avons stylisé la page d'accueil de notre application.

### Utilisation de Vue Router

Vue Router fournit la navigation pour notre application. Lorsque vous cliquez sur le bouton _SE CONNECTER_, il vous redirige vers la page de connexion. Lorsque vous cliquez sur le bouton _MENU_, il vous redirige vers la page qui affiche les plans de repas disponibles.

Le fichier `router.js` contient la configuration du routage. Ouvrez ce fichier. Dans ce fichier, vous verrez deux routes. L'une affiche le composant Home.vue lorsque vous accédez à la route `'/'`. L'autre affiche le composant about.vue lorsque vous accédez à la route 'about'.

Nous devrons créer des routes pour chaque page de notre application. Notre application aura besoin des routes suivantes :

* /
* /menu
* /sign-in
* /join

Lorsque nous avons utilisé le CLI Vue pour créer l'application, nous avons sélectionné l'installation de Vue Router. Par défaut, cela a créé des routes pour `'/'` qui est la page d'accueil et `'/about'` pour la page à propos. Dans la partie 4, nous utiliserons la page à propos pour afficher toutes les recettes que l'utilisateur a commandées.

Nous devons ajouter trois nouvelles routes au tableau des routes. Après avoir ajouté ces nouvelles routes, voici à quoi ressemble notre fichier `router.js` :

```
import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
```

```
Vue.use(Router);
```

```
export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('./views/About.vue')
        },
        {
            path: '/menu',
            name: 'menu',
            component: () => import('./views/Menu.vue')
        },
        {
            path: '/sign-in',
            name: 'signin',
            component: () => import('./views/Signin.vue')
        },
        {
            path: '/join',
            name: 'join',
            component: () => import('./views/Join.vue')
        }
    ]});
```

#### Vue vs Composants

Dans notre première leçon, nous avons créé plusieurs nouveaux composants Vue. J'ai placé ces composants dans le dossier des composants. Pour ces trois nouveaux composants, nous ne les créerons pas dans le dossier des composants. Au lieu de cela, nous les placerons dans le dossier des vues. La raison est que tout ce qui est accessible via une URL comme `/menu` appartient au dossier des vues. Tout le reste doit être dans le dossier des composants.

#### Création de nouvelles vues

Nous devons créer de nouvelles vues pour chacune des trois nouvelles routes. Dans le dossier des vues, créez les trois fichiers suivants :

* Menu.vue
* Signin.vue
* Join.vue

À l'intérieur de chaque fichier, ajoutez un <v-container> avec un <v-layout>. À l'intérieur du layout, ajoutez une balise <h1> avec le nom de la page.

Voici le fichier `Menu.vue` :

```
<template>
    <v-container fluid>
        <v-layout>
            <h1>Page Menu</h1>
        </v-layout>
    </v-container>
</template>
```

```
<script>
export default {
    name: 'Menu'
};
</script>
```

```
<style scoped></style>
```

Voici le fichier `signin.vue` :

```
<template>
    <v-container fluid>
        <v-layout>
            <h1>Page de Connexion</h1>
        </v-layout>
    </v-container>
</template>
```

```
<script>
export default {
    name: 'Signin'
};
</script>
```

```
<style scoped></style>
```

Voici le fichier `Join.vue` :

```
<template>
    <v-container fluid>
        <v-layout>
            <h1>Page d'Inscription</h1>
        </v-layout>
    </v-container>
</template>
```

```
<script>
export default {
    name: 'Join'
};
</script>
```

```
<style scoped></style>
```

#### Rendre les éléments du menu cliquables

Dans notre menu <v-toolbar>, nous avons quatre éléments sur lesquels un utilisateur peut cliquer. Ce sont :

* Menu
* Profil
* Se Connecter
* S'inscrire

Nous voulons configurer chacun de ces éléments afin que, lorsque l'utilisateur clique dessus, il soit redirigé vers la page appropriée. Ouvrez le fichier AppNavigation.vue. Dans la section <v-toolbar>, trouvez le <v-btn> pour le Menu. Tout ce que nous devons faire est d'ajouter `to="/menu"`. Nous ferons cela pour les quatre entrées, mais assurez-vous de spécifier la route correcte que nous avons définie dans le fichier router.js.

Nous n'avons pas d'option de menu pour revenir à la page d'accueil. Nous pouvons résoudre ce problème en faisant en sorte que le nom de l'application redirige vers la page d'accueil. Mais le titre n'est pas un bouton, donc ajouter `to="/menu"` ne fonctionnera pas. Vue Router fournit l'option d'entourer un lien avec `<router-link to="/">`. Nous ferons cela pour le titre de notre application.

Voici à quoi ressemble mon AppNavigation maintenant :

```
<template>
    <span>
        <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>
            <v-list>
                <template v-for="(item, index) in items">
                    <v-list-tile :key="index">
                        <v-list-tile-content>
                            {{item.title}}
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-divider :key="`divider-${index}`"></v-divider>
                </template>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar app color="brown darken-4" dark>
            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>
            <v-spacer class="hidden-md-and-up"></v-spacer>
            <router-link to="/">
                <v-toolbar-title>{{appTitle}}</v-toolbar-title>;
            </router-link>
            <v-btn flat class="hidden-sm-and-down" to="/menu">Menu</v-btn>
            <v-spacer class="hidden-sm-and-down"></v-spacer>
            <v-btn flat class="hidden-sm-and-down" to="/sign-in">SE CONNECTER</v-btn>
            <v-btn color="brown lighten-3" class="hidden-sm-and-down" to="/join">S'INSCRIRE</v-btn>
        </v-toolbar>
    </span>
</template>
```

```
<script>
export default {
    name: 'AppNavigation',
    data() {
        return {
            appTitle: 'Meal Prep',
            drawer: false,
            items: [
                { title: 'Menu' },
                { title: 'Profil' },
                { title: 'Se Connecter' },
                { title: 'S\'inscrire' }
            ]
        };
    }
};
</script>
```

```
<style scoped>
</style>
```

Lorsque nous faisons cela, nous avons un léger problème avec le titre de notre application dans le menu. Il est passé de texte blanc à texte bleu avec un soulignement. C'est le style par défaut d'une balise d'ancrage. Nous pouvons surmonter cela en ajoutant le style suivant :

```
a {
    color: white;
    text-decoration: none;
}
```

Maintenant, nous sommes revenus à notre point de départ. Si vous cliquez sur tous les éléments du menu, ils vous redirigeront vers la page appropriée. Nous avons seulement un léger problème avec le fichier About.vue. Ce fichier affiche le contenu différemment. Pour avoir une cohérence, mettez à jour le fichier About.vue pour qu'il soit comme ceci :

```
<template>
    <v-container fluid>
        <v-layout>
            <h1>Page À Propos</h1>
        </v-layout>
    </v-container>
</template>
```

```
<script>
export default {
    name: 'About'
};
</script>
```

```
<style scoped></style>
```

### Obtenez le code

Bien que ce soit une série en 4 parties, vous pouvez obtenir le [code final dans mon compte GitHub](https://github.com/ratracegrad/meal-prep). Aidez-moi et **étoilez le dépôt** lorsque vous obtenez le code.

### Résumé

Dans cette partie de la série, vous avez appris :

* comment fonctionne Vue Router
* comment charger de nouvelles routes
* comment configurer le menu pour charger chaque page

### Qu'est-ce qui suit

Dans la prochaine partie de cette série, nous aborderons l'utilisation de Firebase pour l'authentification. Vuex vous permet de fournir un "état" dans votre application. Nous allons nous inscrire pour accéder à une API de recettes. À partir de cette API, nous obtiendrons des recettes à afficher aux utilisateurs pour notre page de menu.

Si vous avez aimé cet article, applaudissez-le. Si vous pensez que quelqu'un d'autre pourrait bénéficier de cet article, partagez-le avec lui.

Si vous avez des questions ou si vous trouvez quelque chose qui ne va pas avec le code, laissez un commentaire. Si vous avez d'autres sujets que vous aimeriez que j'aborde, laissez un commentaire.

#### Plus d'articles

Voici quelques autres articles que j'ai écrits et que vous pourriez vouloir lire.

[**Vous voulez un emploi dans la tech ? Voici comment utiliser le principal marché en ligne pour les chercheurs d'emploi pour obtenir cet emploi.**](https://medium.freecodecamp.org/want-a-job-in-tech-here-is-how-to-use-the-top-online-marketplace-for-job-seekers-to-get-that-job-878391456a2)

[**Les modèles d'instanciation en JavaScript**](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)

[**Contribuer à l'Open Source n'est pas si difficile : mon parcours pour contribuer au projet Node.js**](https://medium.freecodecamp.org/contributing-to-open-source-is-not-hard-here-is-my-journey-to-contributing-to-nodejs-d10760e31194)

[**Suivez-moi sur Twitter !**](https://twitter.com/ratracegrad)