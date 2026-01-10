---
title: 'Comment créer une SPA avec Vue.js, Vuex, Vuetify et Firebase : utiliser Vuex
  et accéder à l''API'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-26T17:35:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-spa-using-vue-js-vuex-vuetify-and-firebase-use-vuex-and-access-the-api-f8036aa464ad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_oxBC3QDl02cB2MDOzGXZg.png
tags:
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: vue
  slug: vue
- name: Vue.js
  slug: vuejs
- name: Vuex
  slug: vuex
seo_title: 'Comment créer une SPA avec Vue.js, Vuex, Vuetify et Firebase : utiliser
  Vuex et accéder à l''API'
seo_desc: 'By Jennifer Bland

  Part 3: learn how to use Vuex and access the API to get your recipes


  Meal Prep application

  Learn how to create a meal delivery website using Vue.js, Vuex, Vue Router, and
  Firebase.

  This is part three of my four-part series on build...'
---

Par Jennifer Bland

#### Partie 3 : apprenez à utiliser Vuex et à accéder à l'API pour obtenir vos recettes

![Image](https://cdn-media-1.freecodecamp.org/images/lOmsmx05ec8WAJBTU8q3WNVuDZpRrQvfJ3wr)
_Application de préparation de repas_

Apprenez à créer un site web de livraison de repas en utilisant Vue.js, Vuex, Vue Router et Firebase.

Ceci est la troisième partie de ma série en quatre parties sur la création d'une application Vue. Voici la liste de toutes les parties :

[Partie 1 : Installation de Vue et création d'une SPA avec Vuetify et Vue Router](https://medium.com/p/838b40721a07)

[Partie 2 : Utilisation de Vue Router](https://medium.com/p/fc5bd065fe18)

[Partie 3 : Utilisation de Vuex et accès à l'API](https://medium.com/p/f8036aa464ad)

[Partie 4 : Utilisation de Firebase pour l'authentification](https://medium.com/p/d9932d1e4365)

### Récapitulatif

Dans la première partie de cette série, nous avons créé notre application Vue à l'aide de la CLI Vue. De plus, nous avons ajouté Vuetify à l'application. Nous avons utilisé Vuetify pour styliser notre page d'accueil.

Dans la deuxième partie, nous avons utilisé Vue Router pour ajouter la navigation entre les différentes pages de notre application. Nous avons ajouté des composants pour toutes les pages de notre application.

### Accès à l'API

Nous construisons un site e-commerce SPA qui vend des services de livraison de repas. Pour que ce site fonctionne, nous avons besoin de recettes pour créer nos repas. Pour générer nos recettes, nous utiliserons l'[API d'Edamam](https://www.edamam.com/). L'API de recettes Edamam contient plus de 1,7 million de recettes analysées sur le plan nutritionnel. L'API vous permet de filtrer les recettes par régime. C'est ce dont nous avons besoin puisque nous voudrons afficher des recettes en fonction du régime sélectionné par l'utilisateur.

#### Créer un compte sur Edamam

La première étape consiste à créer votre compte sur Edamam. Ils proposent un compte gratuit et c'est celui auquel vous voulez vous inscrire. Cliquez sur ce lien pour aller sur le site d'Edamam. Cliquez sur le bouton `sign up` pour l'API Recipe Search.

![Image](https://cdn-media-1.freecodecamp.org/images/o9BfUZEWOVODUChoaEo2CYOyFjFZarFOmHfY)
_Page d'accueil de l'API Edamam_

Ensuite, on vous présentera trois niveaux différents auxquels vous pouvez vous inscrire. Nous allons utiliser le niveau gratuit Developer. Cliquez sur le bouton `start now` dans l'option developer.

![Image](https://cdn-media-1.freecodecamp.org/images/ii1jZHksVpG738nDLymTnVNzw3SN27ZeG6G1)
_Inscription au compte gratuit Developer_

Un formulaire d'inscription vous sera présenté. Remplissez le formulaire.

![Image](https://cdn-media-1.freecodecamp.org/images/R80fRLGgShgTjiBleULB4ShCqda8p5vhRtBi)
_Formulaire d'inscription_

Après avoir rempli le formulaire, vous serez invité à vous connecter à votre compte. Une fois connecté, on vous demandera de choisir l'API dont vous avez besoin. Au lieu de cliquer sur l'une des sélections, allez plutôt dans le menu et sélectionnez `Get an API key now!`

Vous devriez voir votre clé API Recipe Search. _(REMARQUE : si vous n'avez pas de clé, cliquez sur le bouton `create a new application` pour en créer une.)_ Cliquez sur le bouton view pour voir les détails de votre clé API. Vous aurez un Application ID et des Application Keys. Vous en aurez besoin pour accéder à l'API pour votre site web.

![Image](https://cdn-media-1.freecodecamp.org/images/wO28Vq5Uy3LHNuYngzH2BIT5BqiSGdHl6Lay)
_Clés API nécessaires pour accéder à Edamam_

#### Création de la page Menu

La page menu est l'endroit où nous afficherons les recettes pour chacun des trois régimes que nous prenons en charge. Ces recettes seront récupérées via le service API d'Edamam.

La première chose que nous voulons, c'est que l'utilisateur sélectionne un régime. Nous pouvons le faire en réutilisant le composant HomePlans. Nous allons modifier le composant pour ajouter un bouton à chaque régime pour que les utilisateurs puissent le sélectionner. Lorsque les visiteurs du site cliquent sur un bouton, ils verront les recettes de ce régime. **Mais** nous ne voulons pas que ces boutons soient affichés lorsque le composant est affiché sur la page d'accueil. Nous allons donc nous en occuper.

Ouvrez le composant HomePlans. Sous la section `v-card-text`, nous allons ajouter une section `v-card-actions`. Cette section contiendra le bouton permettant aux utilisateurs de sélectionner le plan. Voici ce que nous ajoutons à chaque `v-card` dans ce composant.

```
<v-card-actions v-if="['menu'].includes($route.name)">    &lt;v-btn outline block color="green" @click="showRecipes('vegan')">Sélectionner ce plan</v-btn></v-card-actions>
```

Pour chaque section `v-card-actions`, nous aurons un bouton. Le bouton a les props outline et block définies. Le bouton appellera la méthode `showRecipes` lors du clic. La méthode reçoit un paramètre avec le texte du régime sélectionné. Assurez-vous de modifier cela pour refléter le régime choisi. Voici à quoi ressemble maintenant le template du composant `HomePlans` :

```
<template>    <v-container grid-list-lg>        &lt;v-layout row>            &lt;v-flex xs12 class="text-xs-center display-1 font-weight-black my-5">Plans de repas disponibles</v-flex>        </v-layout>        <v-layout row wrap>            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/hjCA3ecCXAQ" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">KETO</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>
```

```
                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Keto</h3>                            <div>Le régime Keto est un régime riche en graisses, modéré en protéines et pauvre en glucides. Le régime force le corps à brûler des graisses plutôt que des glucides en mettant le corps en cétose.                            </div>                        </div>                    </v-card-text>
```

```
                    <v-card-actions>                        &lt;v-btn outline block color="green" @click="showRecipes('keto')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card>            </v-flex>
```

```
            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/6S27S6pZ6o0" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">PALEO</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>
```

```
                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Paléo</h3>                            <div>Le régime Paléo exige la consommation exclusive ou prédominante d'aliments présumés avoir été les seuls aliments disponibles ou consommés par les humains pendant l'ère paléolithique.                            </div>                        </div>                    </v-card-text>
```

```
                    <v-card-actions>                        &lt;v-btn outline block color="green" @click="showRecipes('paleo')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card>            </v-flex>
```

```
            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/1SPu0KT-Ejg" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">VEGAN</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>
```

```
                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Vegan</h3>                            <div>Le régime végétalien s'abstient de l'utilisation de produits d'origine animale. Le régime végétalien ne consomme pas de viande, de produits laitiers, d'œufs ou tout autre ingrédient d'origine animale.                            </div>                        </div>                    </v-card-text>
```

```
                    <v-card-actions>                        &lt;v-btn outline block color="green" @click="showRecipes('vegan')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card>            </v-flex>
```

```
        </v-layout>    </v-container></template>
```

![Image](https://cdn-media-1.freecodecamp.org/images/421O0SuqauyfGkdPCpuDfGAhNVhZ0ChvI-Bm)
_Bouton Sélectionner ce plan ajouté au composant HomePlans_

Maintenant que nous avons ajouté le bouton, nous voulons le masquer sur la page d'accueil et l'afficher sur la page menu. Pour ce faire, nous allons combiner la directive `v-if` et le nom que nous avons attribué à chaque route.

Dans le fichier `router.js`, nous avons ajouté nos routes. Routes est un tableau d'objets. Chaque objet possède un `path`, un `name` et un `component`. Nous pouvons utiliser la méthode de tableau `includes` pour vérifier si la route actuelle est home. Voici ce que nous ajouterons à chaque section `v-card-actions` :

```
<v-card-actions v-if="['menu'].includes($route.name)">    &lt;v-btn outline block color="green" @click="showRecipes('vegan')">Sélectionner ce plan</v-btn></v-card-actions>
```

Voici à quoi ressemble maintenant le template du composant HomePlans :

```
<template>    <v-container grid-list-lg>        &lt;v-layout row>            &lt;v-flex xs12 class="text-xs-center display-1 font-weight-black my-5">Plans de repas disponibles</v-flex>        </v-layout>        <v-layout row wrap>            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/hjCA3ecCXAQ" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">KETO</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>
```

```
                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Keto</h3>                            <div>Le régime Keto est un régime riche en graisses, modéré en protéines et pauvre en glucides. Le régime force le corps à brûler des graisses plutôt que des glucides en mettant le corps en cétose.                            </div>                        </div>                    </v-card-text>
```

```
                    <v-card-actions v-if="['menu'].includes($route.name)">                        &lt;v-btn outline block color="green" @click="showRecipes('keto')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card>            </v-flex>
```

```
            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/6S27S6pZ6o0" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">PALEO</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>
```

```
                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Paléo</h3>                            <div>Le régime Paléo exige la consommation exclusive ou prédominante d'aliments présumés avoir été les seuls aliments disponibles ou consommés par les humains pendant l'ère paléolithique.                            </div>                        </div>                    </v-card-text>
```

```
                    <v-card-actions v-if="['menu'].includes($route.name)">                        &lt;v-btn outline block color="green" @click="showRecipes('paleo')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card>            </v-flex>
```

```
            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/1SPu0KT-Ejg" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">VEGAN</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>
```

```
                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Vegan</h3>                            <div>Le régime végétalien s'abstient de l'utilisation de produits d'origine animale. Le régime végétalien ne consomme pas de viande, de produits laitiers, d'œufs ou tout autre ingrédient d'origine animale.                            </div>                        </div>                    </v-card-text>
```

```
                    <v-card-actions v-if="['menu'].includes($route.name)">                        &lt;v-btn outline block color="green" @click="showRecipes('vegan')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card>            </v-flex>
```

```
        </v-layout>    </v-container></template>
```

#### Récupération des recettes

Lorsqu'un utilisateur clique sur le bouton `Sélectionner ce plan`, cela appelle la méthode `showRecipes`. Créons cette méthode maintenant. Cette méthode récupérera les recettes de l'API Edamam. Tout d'abord, nous devons installer axios en saisissant cette commande dans le terminal :

```
npm install axios
```

Pour utiliser axios, nous devrons l'importer. Dans la section script du composant HomePlans, importez-le avec cette commande :

```
import axios from 'axios';
```

Ensuite, dans la section export default du composant HomePlans, nous ajouterons notre méthode.

_REMARQUE : Je vais vous montrer comment utiliser axios dans un composant pour obtenir des données d'une API. MAIS ensuite, nous allons abandonner ce code et utiliser Vuex. Donc, d'ici jusqu'au titre **Utilisation de Vuex**, c'est du code que nous n'utiliserons pas dans la version finale de notre application — mais je voulais le montrer pour que vous le compreniez._

La méthode s'appelle `showRecipes` et prend un paramètre appelé `plan`. Dans cette méthode, j'utiliserai axios pour obtenir 10 recettes d'Edamam basées sur le plan de régime sélectionné. L'appel axios sera un GET vers l'URL `[https://api.edamam.com/search](https://api.edamam.com/search.)`[.](https://api.edamam.com/search.)

Selon la documentation de l'API Edamam, nous sommes tenus d'utiliser un paramètre appelé `q` qui contient notre chaîne de requête. Nous définirons cette valeur sur le paramètre plan qui est passé à notre méthode. La documentation exige également que nous fournissions des paramètres pour app_id et app_key. Vous devrez définir ces valeurs avec les clés qui vous ont été attribuées lors de votre inscription à l'API Edamam.

Il y a deux autres paramètres que nous utiliserons. Ce sont `to` et `from`. Ces paramètres spécifient le début et la fin du nombre de recettes renvoyées. Pour les besoins de la démo, nous limiterons le retour aux 10 premières recettes.

Notre appel axios réussira ou échouera. Axios fournit une promesse afin que nous puissions utiliser `.then` et `.catch` pour gérer à la fois le succès et l'échec. Si l'appel réussit, nous voulons définir la valeur des données recipes égale au tableau `hits` renvoyé par Edamam. Toutes les réponses d'axios sont contenues dans l'objet `data`. Nous en tenons compte en assignant d'abord response à response.data. Ensuite, nous assignons recipes à `response.hits`.

Et si l'appel axios échoue ? Eh bien, nous utilisons le `.catch` de la promesse pour gérer un échec. Dans ce cas, tout ce que nous voulons faire est de définir recipes sur un tableau vide.

Voici à quoi ressemble la méthode :

```
export default {    name: 'HomePlans',    data() {        return {            recipes: []        };    },    methods: {        showRecipes(plan) {            axios                .get('https://api.edamam.com/search', {                    params: {                        q: plan,                        app_id: '5b6623d5',                        app_key: '46674aa2193dbb7b88ffd897331e661a',                        from: 0,                        to: 9                    }                })                .then(response => {                    response = response.data;                    this.recipes = response.hits;                })                .catch(() => {                    this.recipes = [];                });        }    }};
```

### Utilisation de Vuex

Maintenant, nous nous sommes mis dans l'embarras avec notre code. Nous avions initialement un composant qui affichait une image, un titre et une courte description d'un régime. Nous y avons ajouté un bouton pour obtenir des recettes. Maintenant, si nous continuons, nous devrons ajouter des fonctionnalités pour afficher les recettes que nous avons récupérées de l'API Edamam.

Je ne veux vraiment pas que toutes ces fonctionnalités soient placées dans ce composant. Je veux qu'il affiche simplement l'image, le titre, la courte description et le bouton. Mais en ayant le bouton dans le composant, j'ai besoin d'un moyen de gérer le clic de l'utilisateur. J'ai aussi besoin d'un moyen d'afficher les recettes. Pour ce faire, je vais déplacer la fonctionnalité de gestion du clic sur le bouton vers Vuex.

Vuex est une bibliothèque de gestion d'état pour les applications Vue.js. Elle sert de magasin centralisé pour tous les composants d'une application, avec des règles garantissant que l'état ne peut être muté que de manière prévisible. Vuex se compose de :

* L'état (state), qui est la source de vérité qui pilote notre application ;
* Les mutations, qui modifient la valeur de l'état ;
* Les actions, qui sont les moyens possibles de modifier l'état en réaction aux entrées de l'utilisateur depuis la vue.

Lorsque nous avons créé notre application à l'aide de la CLI Vue 3, nous avons spécifié que nous utiliserions Vuex. En conséquence, la CLI a créé le fichier `store.js` dans le dossier src pour nous.

`State` contiendra les recettes. Nous utiliserons une `actions` pour effectuer l'appel API afin de récupérer les recettes. Une `mutations` sera utilisée pour mettre à jour la variable `recipe` dans `state` avec les recettes renvoyées par l'appel `actions`.

Ouvrez le fichier `store.js`. Tout d'abord, ajoutez une nouvelle variable recipes dans state et assignez-lui un tableau vide. Ajoutez également une variable appelée apiUrl. Cette variable contiendra l'url pour notre appel API. Cela devrait ressembler à ceci :

```
export default new Vuex.Store({    state: {        recipes: [],        apiUrl: 'https://api.edamam.com/search'    },    mutations: {},    actions: {}});
```

Ensuite, nous allons créer une action appelée `getRecipes`. Cette action utilisera axios pour obtenir des recettes de l'API. Pour utiliser axios, nous devrons l'importer. En haut du fichier, il y a deux commandes d'importation. Placez ceci après elles :

```
import axios from 'axios';
```

Plus tôt, je vous ai montré l'utilisation des promesses avec l'appel axios. Maintenant, je vais vous montrer comment faire le même appel en utilisant async / await. La méthode getRecipes devra être préfixée par `async`. À l'intérieur de la méthode, nous avons un bloc try catch. À l'intérieur du bloc try, nous définirons une variable `response` sur les données renvoyées par l'appel axios. Nous mettons await devant l'appel axios. Si l'appel réussit, nous appellerons la mutation `setRecipes`. SetRecipes modifiera l'état pour définir recipes sur le tableau de recettes renvoyé par l'appel API.

Si l'appel API échoue, il finira dans le bloc catch. Dans ce scénario, nous appelons la même mutation mais lui passons un tableau vide. Voici à quoi devrait ressembler store.js :

```
import Vue from 'vue';import Vuex from 'vuex';import axios from 'axios';Vue.use(Vuex);export default new Vuex.Store({    state: {        recipes: [],        apiUrl: 'https://api.edamam.com/search'    },    mutations: {        setRecipes(state, payload) {            state.recipes = payload;        }    },    actions: {        async getRecipes({ state, commit }, plan) {            try {                let response = await axios.get(`${state.apiUrl}`, {                    params: {                        q: plan,                        app_id: '<votreAppIdIci>',                        app_key: '<votreAppKeyIci>',                        from: 0,                        to: 9                    }                });                commit('setRecipes', response.data.hits);            } catch (error) {                commit('setRecipes', []);            }        }    }});
```

#### Mise à jour du composant HomePlans

Revenons à notre composant HomePlans et nettoyons-le. Nous pouvons supprimer la ligne de code import axios. Nous pouvons supprimer l'objet `data()`. Dans la méthode `showRecipes`, vous pouvez supprimer tout le code. Nous n'avons plus besoin que d'une seule ligne de code pour appeler notre action dans notre store Vuex. Pour appeler une action dans Vuex, vous utilisez un `dispatch`. Voici la ligne de code pour notre méthode `showRecipes` :

```
this.$store.dispatch('getRecipes', plan);
```

Voici à quoi ressemble notre composant HomePlans :

```
<template>    <v-container grid-list-lg>        &lt;v-layout row>            &lt;v-flex xs12 class="text-xs-center display-1 font-weight-black my-5">Plans de repas disponibles</v-flex>        </v-layout>        <v-layout row wrap>            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/hjCA3ecCXAQ" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">KETO</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Keto</h3>                            <div>Le régime Keto est un régime riche en graisses, modéré en protéines et pauvre en glucides. Le régime force le corps à brûler des graisses plutôt que des glucides en mettant le corps en cétose.                            </div>                        </div>                    </v-card-text>                    <v-card-actions v-if="['menu'].includes($route.name)">                        <v-btn outline block color="green" @click="showRecipes('keto')">Sélectionner ce plan</v-btn>                    &lt;/v-card-actions>                </v-card&gt;            </v-flex>            <v-flex xs12 sm12 md4>                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/6S27S6pZ6o0" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">PALEO</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Paléo</h3>                            <div>Le régime Paléo exige la consommation exclusive ou prédominante d'aliments présumés avoir été les seuls aliments disponibles ou consommés par les humains pendant l'ère paléolithique.                            </div>                        </div&gt;                    </v-card-text>                    <v-card-actions v-if="['menu'].includes($route.name)">                        <v-btn outline block color="green" @click="showRecipes('paleo')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card&gt;            </v-flex>            <v-flex xs12 sm12 md4&gt;                <v-card>                    <v-responsive>                        <v-img src="http://source.unsplash.com/1SPu0KT-Ejg" height="500px">                            <v-container fill-height fluid>                                <v-layout fill-height>                                    <v-flex xs12 align-end flexbox>                                        <span class="headline white--text">VEGAN</span>                                    </v-flex>                                </v-layout>                            </v-container>                        </v-img>                    </v-responsive>                    <v-card-text>                        <div>                            <h3 class="headline mb-0">Vegan</h3>                            <div>Le régime végétalien s'abstient de l'utilisation de produits d'origine animale. Le régime végétalien ne consomme pas de viande, de produits laitiers, d'œufs ou tout autre ingrédient d'origine animale.                            </div>                        </div>                    </v-card-text>                    <v-card-actions v-if="['menu'].includes($route.name)">                        <v-btn outline block color="green" @click="showRecipes('vegan')">Sélectionner ce plan</v-btn>                    </v-card-actions>                </v-card>            </v-flex>        </v-layout>    </v-container></template><script>export default {    name: 'HomePlans',    methods: {        showRecipes(plan) {            this.$store.dispatch('getRecipes', plan);        }    }};</script><style scoped></style>
```

#### Affichage des recettes

Nous avons utilisé Vuex pour obtenir des recettes de l'API. Nous stockons le tableau de recettes dans le store Vuex. Maintenant, nous avons besoin d'un nouveau composant qui sera utilisé pour afficher les recettes. Dans votre dossier components, créez un nouveau fichier appelé `MealRecipes.vue`.

Dans ce nouveau composant, nous ajouterons une valeur calculée (computed) pour les recettes. Cette variable calculée obtiendra sa valeur du store Vuex. Sa valeur sera définie sur la valeur de `recipes` dans `state`. Voici à quoi cela ressemble :

```
<script>export default {    name: 'MealRecipes',    computed: {        recipes() {            return this.$store.state.recipes;        }    }};</script>
```

Nous devons mettre à jour le template dans ce composant pour afficher nos recettes. Vuetify fournit une grid-list qui crée un espacement entre les éléments affichés sur la page. Nous utiliserons cette fonctionnalité en la plaçant sur le v-container qui est l'élément racine de notre template. Comme ceci :

```
<v-container grid-list-lg>
```

```
</v-container>
```

À l'intérieur du `v-container`, nous aurons un `v-layout`. À l'intérieur du `v-layout`, nous aurons un `v-flex`. Nous définissons la disposition sur le v-layout en `row`. Nous ajouterons également `wrap`. Sur le `v-flex`, nous bouclerons sur toutes les recettes du tableau et les afficherons. Nous avons donc besoin d'un `v-for`. Vue exige désormais que vous ayez un index pour chaque boucle v-for. Nous ajoutons un `idx` et le définissons sur la `key`. Voici à quoi ressemble notre composant MealRecipes jusqu'à présent.

```
<v-container grid-list-lg>    <v-layout row wrap>        <v-flex xs12 sm6 md6 lg4 v-for="(item, idx) in recipes" :key="idx">        </v-flex>    </v-layout><v-container>
```

Nous utiliserons la `v-card` de Vuetify pour afficher chaque recette. C'est très similaire à la mise en page que nous avons utilisée pour le composant `HomePlans`. Nous afficherons une image pour la recette, un titre et une liste d'ingrédients.

L'appel API renvoie un tableau de recettes. Si vous regardez une entrée dans le tableau, vous remarquerez qu'elle possède un objet recipe. À l'intérieur de cet objet, nous trouverons une URL pour l'image de la recette, le titre et la liste des ingrédients. L'API renvoie deux tableaux différents pour les ingrédients. Celui que nous utiliserons est celui du tableau ingredientLines.

Voici à quoi ressemble le composant `MealRecipes` :

```
<template>    <v-container grid-list-lg>        <v-layout row wrap>            <v-flex xs12 sm6 md6 lg4 v-for="(item, idx) in recipes" :key="idx">                <v-card>                    <v-responsive>                        <v-img :src="item.recipe.image"></v-img>                    </v-responsive>                    <v-card-text>                        <div class="title"&gt;{{item.recipe.label}}</div>                        <div class="subheading">Ingrédients</div>                        <ul&gt;                            <li v-for="(ingredient, i) in item.recipe.ingredientLines" :key="i">{{ingredient}}</li>                        </ul>                    </v-card-text>                </v-card>            </v-flex>        </v-layout>    </v-container></template><script>export default {    name: 'MealRecipes',    computed: {        recipes() {            return this.$store.state.recipes;        }    }};</script><style scoped></style>
```

Maintenant que nous avons terminé le composant, nous devons l'utiliser à l'intérieur du composant `Menu.vue`. Ouvrez le composant `Menu.vue`. Importez le composant MealRecipes avec cette commande :

```
import MealRecipes from '@/components/MealRecipes';
```

Ajoutez-le aux composants comme ceci :

```
export default {    name: 'Menu',    components: {        HomePlans,        MealRecipes    }};
```

Dans le template, ajoutez mealRecipes sous homePlans. Voici à quoi devrait ressembler `Menu.vue` :

```
<template>    <div>        <home-plans></home-plans>        <meal-recipes></meal-recipes&gt;    </div&gt;&lt;/template><script>import HomePlans from '@/components/HomePlans';import MealRecipes from '@/components/MealRecipes';export default {    name: 'Menu',    components: {        HomePlans,        MealRecipes    }};</script><style scoped></style>
```

Lancez l'application avec la commande `npm run serve` dans le terminal. Ouvrez votre navigateur sur [http://localhost:8080](http://localhost:8080) et vous verrez l'application s'exécuter. Cliquez sur menu dans la navigation. Cliquez ensuite sur l'un des plans de régime. Vous devriez voir une liste de recettes comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/jN9C9yDOw9ebushF2n2yYuksBX4jEAD4PLmR)
_Liste de recettes_

Je veux apporter deux modifications rapides au style des recettes. Premièrement, je veux ajouter un peu plus d'espacement entre le titre de la recette et les ingrédients. Deuxièmement, je veux ajouter un bouton au bas de chaque recette pour qu'une personne puisse commander.

Ouvrez donc le composant `MealRecipes`. Pour le titre, j'ai déjà une classe `title`. Je vais y ajouter une valeur de `my-3`. C'est l'équivalent d'ajouter margin-top et margin-bottom au titre. Cela permet au titre de se détacher de l'image et des ingrédients.

Dernière modification que je souhaite apporter : ajouter un bouton. À l'intérieur de la `v-card` et sous le `v-card-text`, nous ajouterons un `v-card-actions`. À l'intérieur, nous ajouterons un bouton. Nous utiliserons le bouton par défaut avec une couleur verte. Par défaut, Vuetify rend le texte des boutons en noir. Nous pouvons changer cela en blanc en ajoutant la directive `dark`. Voici notre bouton :

```
<v-card-actions>    &lt;v-btn color="green" dark>Commander</v-btn></v-card-actions>
```

Voici notre composant MealRecipes :

```
<template>    <v-container grid-list-lg>        <v-layout row wrap>            <v-flex xs12 sm6 md6 lg4 v-for="(item, idx) in recipes" :key="idx">                <v-card>                    <v-responsive>                        <v-img :src="item.recipe.image"></v-img>                    </v-responsive>                    <v-card-text>                        <div class="title my-5"&gt;{{item.recipe.label}}</div>                        <div class="subheading">Ingrédients</div>                        <ul&gt;                            <li v-for="(ingredient, i) in item.recipe.ingredientLines" :key="i">{{ingredient}}</li>                        </ul&gt;                    </v-card-text>                    <v-card-actions>                        <v-btn color="green" dark>Commander</v-btn>                    </v-card-actions>                </v-card>            </v-flex>        </v-layout>    </v-container></template>&lt;script>export default {    name: 'MealRecipes',    computed: {        recipes() {            return this.$store.state.recipes;        }    }};</script><style scoped></style>
```

### Obtenir le code

Même s'il s'agit d'une série en 4 parties, vous pouvez obtenir le [code final sur mon compte GitHub.](https://github.com/ratracegrad/meal-prep) S'il vous plaît, aidez-moi et **donnez une étoile au repo** quand vous récupérez le code.

### Résumé

Dans cette partie de la série, vous avez appris :

* Ce qu'est Vuex
* Comment obtenir des recettes à partir d'une API
* Comment utiliser Axios avec les promesses et async / await
* Comment appeler des actions dans le store Vuex
* Comment muter l'état dans Vuex

### Et ensuite ?

Dans la prochaine partie de cette série, nous aborderons Firebase pour l'authentification. Firebase vous permet de développer une application sans avoir à écrire de code côté serveur.

Si vous avez apprécié cet article, n'hésitez pas à applaudir. Si vous pensez que quelqu'un d'autre pourrait bénéficier de cet article, partagez-le avec lui.

Si vous avez des questions ou si vous trouvez une erreur dans le code, laissez un commentaire. S'il y a d'autres sujets sur lesquels vous aimeriez que j'écrive, laissez un commentaire.

#### Autres articles

Voici d'autres articles que j'ai écrits et que vous pourriez vouloir lire.

[**Voici 5 mises en page que vous pouvez réaliser avec FlexBox**](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)  
[_Le CSS Flexible Box Layout — Flexbox — fournit une solution simple aux problèmes de conception et de mise en page que les designers et... hackernoon.com_](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)

[**Pensez hors de la boîte avec CSS shape-outside**](https://hackernoon.com/mastering-css-series-shape-outside-44d626270b25)  
[_Le CSS est basé sur un modèle de boîte. Si vous avez une image en forme de cercle autour de laquelle vous voulez envelopper du texte, il s'enveloppera... hackernoon.com_](https://hackernoon.com/mastering-css-series-shape-outside-44d626270b25)

[**Pourquoi la culture d'entreprise est importante pour votre carrière d'ingénieur logiciel**](https://medium.freecodecamp.org/why-company-culture-is-important-to-your-career-as-a-software-engineer-5a590bc44621)  
[_L'impact de la culture d'une entreprise se reflète dans sa capacité à atteindre ses objectifs et ses niveaux de productivité... medium.freecodecamp.org_](https://medium.freecodecamp.org/why-company-culture-is-important-to-your-career-as-a-software-engineer-5a590bc44621)

[**Suivez-moi sur Twitter !**](https://twitter.com/ratracegrad)