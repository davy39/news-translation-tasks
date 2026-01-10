---
title: Comment configurer une recherche UI réactive dans Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T16:55:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-responsive-ui-search-in-vue-js-bf6007b7fc0f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*557yKFY9udPu1QV2_bW9Kw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: Comment configurer une recherche UI réactive dans Vue.js
seo_desc: 'By Honey Thakuria

  Are you thinking of building something awesome with one of the popular modern frameworks
  out there right now, but don’t know how to get started?

  If yes, then this post will help you get a kick started and build something awesome.


  W...'
---

Par Honey Thakuria

Pensez-vous à construire quelque chose d'awesome avec l'un des frameworks modernes populaires actuels, mais ne savez pas comment commencer ?

Si oui, alors cet article vous aidera à démarrer et à construire quelque chose d'awesome.

> **Que allons-nous construire ?**

Nous allons construire une recherche côté client réactive des 7 merveilles du monde avec les fonctionnalités suivantes :

1. **Recherche de texte** et **filtres** basés sur les évaluations et les likes.
2. 2 éléments par ligne pour **Tablette** et **Desktop**, 1 élément par ligne pour **Mobile**.
3. Récupération des données de manière asynchrone à partir d'une API externe côté client.
4. Vue réactive comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/NAceF0rPfr0FHFAl-m0NW-BDBQrR-6YNcDG-)

![Image](https://cdn-media-1.freecodecamp.org/images/3bxyozgrAJ45A1n9pRysRELj3cweirUBIdTu)
_À gauche, vue Desktop / Tablette et à droite, vue Mobile_

**Démonstration en direct** : [https://vue-responsive-search.herokuapp.com](https://vue-responsive-search.herokuapp.com/)

**Code source** : [https://github.com/honey93/VueSearchExample](https://github.com/honey93/VueSearchExample)

#### **Architecture technique**

Nous travaillerons avec les technologies suivantes :

1. [**Vue.js**](https://vuejs.org/) : Le Framework JavaScript Progressif
2. [**BootstrapVue**](https://bootstrap-vue.js.org/) : Il fournit l'une des implémentations les plus complètes des composants Bootstrap V4 et du système de grille disponibles pour Vue.js 2.5+, avec une accessibilité WAI-ARIA extensive et automatisée.
3. [**Vue Cli 3**](https://cli.vuejs.org/) : Outil standard pour le développement Vue.js

#### **Structure du projet**

Pour commencer avec notre projet Vue, nous devons configurer de nombreuses choses comme Vue, Bootstrap, Vue Router, Vuex, etc.

Vue Cli nous fournit la commande pour créer le projet avec la plupart des configurations nécessaires.

```
npm install -g @vue/cli
vue create nom-du-projet
```

Pour les autres choses comme BootstrapVue, vue-star-rating, etc., nous pouvons utiliser la commande npm install.

Le projet par défaut créé avec vuecli a la structure suivante :

```
/Dossier Racine 
 
 Public/

 src/
  
  assets/  /* Les assets statiques comme les images vont ici */
  components/ /* Petite partie d'une vue */
  views/  /* Une vue représente une page composée de plusieurs composants*/
  App.vue /* La vue principale dans laquelle la logique de routage est placée */
  main.js  /* L'initialisation de l'application se fait ici  */
  router.js /* La logique du routeur est définie ici */
  store.js /* Bibliothèque optionnelle de gestion d'état Vuex */

 package.json /* Il contient toutes les dépendances du projet. */
 ......
```

Les éléments ci-dessus sont là pour vous expliquer l'architecture du projet et la manière de l'initialiser.

Nous pouvons commencer en clonant le [**dépôt**](https://github.com/honey93/VueSearchExample) et en écrivant les commandes suivantes :

```
npm install 
npm run serve 
```

Quelques composants importants expliqués :

**components/Header.vue**

L'en-tête a été créé sous la forme d'un composant indépendant unique afin qu'il puisse être réutilisé sur plusieurs pages, évitant ainsi la duplication du code.

```
/* Style Vue d'écriture de composant : template, script et style*/
<template>
  <div class="pad-15-hor pad-15-ver header">
    <div>
      <img src="@/assets/logo.png" width="25px"> Recherche Réactive
    </div>
    <div>
      <i class="fas fa-bars"></i>
    </div>
  </div>
</template>
<script>
export default {
  name: "Header"
};
</script>
<style scoped>
.header {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
}
</style>
```

**components/Main.vue**

Ce composant contient toute la logique de recherche / filtres et d'affichage des résultats récupérés depuis l'API.

Ce composant utilise l'en-tête ci-dessus en l'important dans le script.

```
<template>
  <div>
    <Header/>
    <div class="pad-15-hor pad-15-ver search-parent">
      <div class="search-bar">
        <b-form-input
          @input="search_text()"
          v-model="search.text"
          type="text"
          placeholder="Rechercher par Nom"
        ></b-form-input>
        <span class="search-icon">
          <i class="fas fa-search"></i>
        </span>
      </div>
      <div>
        <span class="bold">Total Likes :</span>
        {{likes.count}}
        <span class="bold">Hits :</span>
        {{likes.hit}}
      </div>
      <div>
        <b-form-select @input="sort()" v-model="search.filter" :options="options"/>
      </div>
    </div>
<div class="container-fluid">
      <div class="row">
        <div class="col-md-6 pad-15-ver" v-for="wonder in wonders_data" :key="wonder.id">
          <div
            class="card-inner"
            @mouseover="show_hover(true,wonder.id)"
            @mouseout="show_hover(false,0)"
          >
            <img class="card-img" :src="wonder.imageURL">
<div class="card-bottom pad-15-hor" v-show="!hover_flag || active_id != wonder.id">
              <div class="min-width-160">
                <span class="bold">Évaluations :</span>
                <star-rating
                  :rating="wonder.ratings"
                  :show-rating="false"
                  :inline="true"
                  :star-size="15"
                ></star-rating>
              </div>
              <div class="max-width-160">
                <span class="bold">{{wonder.place}}</span>
              </div>
            </div>
<div :class="{'card-hover':1}" v-show="hover_flag && active_id == wonder.id">
              <span
                @click="make_active(wonder.id)"
                :class="{'fas':1, 'fa-heart':1, 'absolute-star':1, 'green':check_active(wonder.id)}"
              >{{wonder.likes}}</span>
              <h5>{{wonder.place}}</h5>
              <p>{{wonder.description}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
/* Importation de Header pour l'utiliser dans ce composant */ 
import Header from "@/components/Header.vue";
/* Importation d'axios pour les appels REST asynchrones */
import axios from "axios";
export default {
  name: "Main",
/* mounted est appelé lorsque le composant est monté. Les appels AJAX sont préférés dans la méthode de cycle de vie mounted */
  mounted() {
    this.hover_flag = false;
var inside = this;
axios
      .get("https://www.mocky.io/v2/5c7b98562f0000c013e59f07")
      .then(function(response) {
        //console.log(response);
inside.wonders_data_actual = response.data.data;
response.data.data.map(function(wonder) {
          inside.likes.count += wonder.likes;
        });
inside.wonders_data_actual = inside.wonders_data_actual.map(function(
          wonder
        ) {
          wonder.active_like = false;
          return wonder;
        });
        inside.wonders_data = response.data.data;
      })
      .catch(function(error) {
        // console.log(error);
      });
  },
/* Toutes les déclarations de variables de données sont faites ici :  */
  data() {
    return {
      hover_flag: false,
      wonders_data_actual: [],
      wonders_data: [],
      active_id: 0,
      options: [
        { value: null, text: "Trier Par" },
        { value: "a", text: "Évaluations" },
        { value: "b", text: "Likes" }
      ],
      search: { filter: null, text: "" },
      likes: { count: 0, hit: 0 }
    };
  },
/* Les méthodes sont définies ici */
  methods: {
    show_hover(flag, active_id) {
      this.hover_flag = flag;
      this.active_id = active_id;
    },
    sort() {
      //console.log(this.search.filter);
      this.search.filter == "b"
        ? this.wonders_data.sort(function(a, b) {
            return b.likes - a.likes;
          })
        : this.wonders_data.sort(function(a, b) {
            return b.ratings - a.ratings;
          });
    },
    search_text() {
      //console.log(this.search.text);
var inside = this;
this.wonders_data = this.wonders_data_actual.filter(function(wonder) {
        if (
          wonder.place
            .toLowerCase()
            .indexOf(inside.search.text.toLowerCase()) != "-1"
        ) {
          return wonder;
        }
      });
    },
    check_active(id) {
      var flag = false;
      this.wonders_data_actual.map(function(wonder) {
        if (wonder.id == id) {
          flag = wonder.active_like;
        }
      });
      return flag;
    },
    make_active(id) {
      this.likes.hit++;
      this.wonders_data_actual = this.wonders_data_actual.map(function(wonder) {
        if (wonder.id == id) {
          wonder.active_like = !wonder.active_like;
          wonder.active_like ? wonder.likes++ : wonder.likes--;
        }
return wonder;
      });
      var inside = this;
inside.likes.count = 0;
      this.wonders_data_actual.map(function(wonder) {
        inside.likes.count += wonder.likes;
      });
    }
  },
  components: {
    Header
  }
};
</script>
<style scoped> /* Les styles sont limités à ce composant uniquement.*/
/* Style pour Desktop/Tablette  */
.search-parent {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  background-color: lightgray;
}
.card-inner {
  position: relative;
  overflow: hidden;
  box-shadow: 2px 2px 8px grey;
}
.card-img {
  width: 100%;
}
.card-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 30px;
  width: 100%;
  background-color: white;
  opacity: 0.7;
  display: flex;
  justify-content: space-between;
}
.card-hover {
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
  bottom: 15px;
  background-color: white;
  opacity: 0.7;
  display: flex;
  flex-flow: column wrap;
  justify-content: center;
  align-items: center;
}
.absolute-star {
  position: absolute;
  top: 10px;
  right: 10px;
}
.card-hover p {
  font-size: 10px;
  text-align: center;
}
.bold {
  font-weight: 500;
}
.rating-div {
  width: 200px;
}
.search-bar {
  position: relative;
}
.search-bar input {
  padding-left: 30px;
}
.search-icon {
  position: absolute;
  top: 8px;
  left: 8px;
}
/* Pour les appareils mobiles, nous allons utiliser l'approche column wrap */
@media screen and (max-width: 550px) {
  .search-parent {
    display: flex;
    flex-flow: column wrap;
    justify-content: center;
    align-items: center;
    background-color: lightgray;
  }
.search-parent div {
    width: 100%;
    text-align: center;
  }
}
</style>
```

J'espère que vous avez une meilleure compréhension de la manière de commencer avec Vue et de créer quelque chose d'awesome.

Si vous avez trouvé cela utile, **applaudissez** ci-dessous, donnez des **étoiles** au projet [**dépôt**](https://github.com/honey93/VueSearchExample) et partagez avec vos amis également.