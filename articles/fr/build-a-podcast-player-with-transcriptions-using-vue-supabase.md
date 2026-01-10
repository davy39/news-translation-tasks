---
title: Comment créer un lecteur de podcast avec transcriptions en utilisant Vue et
  Supabase
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2022-02-28T23:05:43.000Z'
originalURL: https://freecodecamp.org/news/build-a-podcast-player-with-transcriptions-using-vue-supabase
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Build-Podcast-Player-app-w-transcriptions-using-Vue-Supabase@2x.jpg
tags:
- name: audio
  slug: audio
- name: projects
  slug: projects
- name: supabase
  slug: supabase
- name: vue
  slug: vue
seo_title: Comment créer un lecteur de podcast avec transcriptions en utilisant Vue
  et Supabase
seo_desc: "In this post we will walk through setting up a Podcast Player app using\
  \ Supabase and Vue 3, including getting transcriptions for the podcasts. \nThis\
  \ is a continuation of my previous post on setting up Authentication using Supabase.\
  \ If you aren't fami..."
---

Dans cet article, nous allons passer en revue la configuration d'une application de lecteur de podcast en utilisant Supabase et Vue 3, y compris l'obtention de transcriptions pour les podcasts. 

Ceci est la suite de mon précédent article sur [la configuration de l'authentification en utilisant Supabase](https://www.freecodecamp.org/news/add-supabase-authentication-to-vue/). Si vous n'êtes pas familier avec la configuration de Supabase dans votre projet, je vous recommande vivement de suivre cet article. 

## Le dépôt de code de départ

Voici le dépôt de mon précédent article qui vous permettra de commencer là où cet article commence. Vous devrez simplement configurer Supabase et ajouter vos identifiants/clé API à un fichier `.env.local` pour commencer. Ce dépôt contient également des styles appliqués qui n'étaient pas inclus dans l'article précédent.

%[https://github.com/briancbarrow/vue-supabase-auth]

## Prérequis

Vous devriez être familier avec JavaScript, avoir une certaine expérience avec Vue 3, et vous devriez avoir Node.js et NPM installés sur votre machine. 

Si vous avez suivi l'article précédent sur l'authentification Supabase ou cet autre article sur [Getting Started with Supabase](https://developers.deepgram.com/blog/2021/11/getting-started-with-supabase/) vous serez prêt à commencer.

Vous aurez également besoin d'une [clé API gratuite de Deepgram](https://console.deepgram.com/signup) pour la section sur les transcriptions. 

## Pour commencer

Une fois que vous avez téléchargé le [dépôt ci-dessus](https://github.com/briancbarrow/vue-supabase-auth), exécutez `npm install` pour installer les packages du projet. 

Ajoutez vos variables d'environnement `VITE_SUPABASE_URL` et `VITE_SUPABASE_ANON_KEY` depuis le tableau de bord de votre propre projet Supabase.

Exécutez `npm run dev` pour démarrer le serveur de développement local.

Connectez-vous à l'application en utilisant soit le formulaire de connexion soit le formulaire de lien magique. Une fois connecté, vous devriez voir le composant/page HelloWorld avec un bouton de déconnexion en haut. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-18-at-2.20.26-PM.png)
_Composant Hello World_

## Comment récupérer un flux RSS de podcast

La première chose que nous devons faire est d'ajouter une fonctionnalité pour obtenir un flux de podcast dans notre application. Créez un nouveau composant dans le dossier des composants appelé `PodcastFeed.vue`. 

La plupart des podcasts ont un flux RSS public que nous pouvons utiliser pour obtenir les informations dont nous avons besoin avec une simple requête fetch. 

À l'intérieur du composant `PodcastFeed.vue`, créez le formulaire suivant qui prend une URL de flux RSS et se connecte à un bouton qui déclenche la requête fetch.

Note : J'ai essayé d'ajouter des commentaires dans le code pour vous aider à comprendre ce que fait chaque partie.

```js
<template>
  <div class="podcast-input-feed">
    <label for="email">URL du flux RSS du podcast</label>
    <div class="">
      <!-- liaison du champ d'entrée d'URL à la propriété de données 'url' -->
      <input
        type="url"
        name="url"
        id="url"
        v-model="url"
        placeholder="https://rss.your-org.org/feed/"
        aria-describedby="rss-url"
      />
    </div>
    <!-- connexion du clic sur le bouton à la méthode 'getRssFeed' -->
    <button @click="getRssFeed()" type="button" class="">Obtenir le flux</button>
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../supabase";
import { store } from "../store";
export default {
  setup() {
    // J'initialise l'URL avec une URL que je sais fonctionner, afin de ne pas avoir à saisir une URL à chaque fois que je développe.
    // n'hésitez pas à changer cela par une URL de votre choix
    const url = ref("https://anchor.fm/s/3e9db190/podcast/rss");
    // initialisation de l'état du podcast à un objet vide
    const podcast = ref({});

    function getRssFeed() {
      const feedUrl = url.value;
      return (
        fetch(feedUrl)
          // cela retourne une promesse, nous devons donc la convertir en une chaîne
          .then((response) => response.text())
          // cette ligne suivante est pour analyser la réponse XML
          .then((str) =>
            new window.DOMParser().parseFromString(str, "text/xml")
          )
          // analyse des données de la réponse XML et définition dans l'état du podcast
          .then((data) => {
            console.log("Data: ", data);
            podcast.value.image_url = data
              .querySelector("image")
              .querySelector("url").innerHTML;
            podcast.value.title = data.querySelector("title").textContent;
            podcast.value.description =
              data.querySelector("description").textContent;
            podcast.value.rss_url = feedUrl;
          })
          .catch((err) => {
            console.log("ERROR: ", err);
          })
      );
    }
    return {
      url,
      podcast,
      store,

      getRssFeed,
    };
  },
};
</script>

```

Avec cela configuré, remplacez le composant HelloWorld dans le fichier `App.vue` par ce nouveau composant `PodcastFeed.vue` :

```js
<template>
  <button v-if="store.state.user" class="signout-button" @click="signOut">Se déconnecter</button>
  <!-- Vérifiez si l'utilisateur est disponible dans le store, sinon affichez le composant d'authentification -->
  <Auth v-if="!store.state.user" />
  <!-- Si l'utilisateur est disponible, affichez l'application -->
  <div v-else class="app">
    <PodcastFeed />
  </div>
</template>

<script>
import Auth from "./components/Auth.vue";
import PodcastFeed from "./components/PodcastFeed.vue";

import { store } from "./store";
import { supabase } from "./supabase";

export default {
  components: {
    PodcastFeed,
    Auth,
  },
  setup() {
    // nous vérifions initialement si un utilisateur est connecté avec Supabase
    store.state.user = supabase.auth.user();
    // nous configurons ensuite un écouteur pour mettre à jour le store lorsque l'utilisateur change, soit en se connectant soit en se déconnectant
    supabase.auth.onAuthStateChange((event, session) => {
      if (event == "SIGNED_OUT") {
        store.state.user = null;
      } else {
        store.state.user = session.user;
      }
    });

    async function signOut() {
      const { error } = await supabase.auth.signOut();
    }

    return {
      store,

      signOut,
    };
  },
};
</script>

<style></style>

```

Ainsi, l'application devrait maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-18-at-2.38.40-PM.png)
_Application après l'ajout de PodcastFeed.vue_

Lorsque vous cliquez sur le bouton, les données qui reviennent de la requête fetch s'afficheront dans la console. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/xml-data-from-rss.png)
_Données XML analysées_

Dans la méthode `getRssFeed`, nous analysons ces données puis prenons les informations dont nous avons besoin et les ajoutons aux données d'état `podcast`. Nous devons afficher ces données pour que l'utilisateur sache que la requête a réussi. Nous voulons également ajouter de meilleurs messages d'erreur au cas où la requête échoue. 

Créez un nouveau composant appelé `PodcastInfo.vue` et ajoutez le code suivant :

```js
<template>
  <div class="podcast-info">
    <div class="image-container">
      <img :src="podcast.image_url" alt="" class="" />
    </div>
    <div class="podcast-text">
      <div class="title-desc">
        <p class="title">
          {{ podcast.title }}
        </p>
        <p class="desc">
          {{ podcast.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { store } from "../store";
import { supabase } from "../supabase";

export default {
  props: {
    podcast: {
      type: Object,
      required: true,
    },
  },
  computed: {},
  methods: {},
  setup() {},
};
</script>

<style scoped></style>

```

```js
<template>
  <div class="info-error">
    <h3 class="">Une erreur est survenue avec votre requête</h3>
    <p class="">Vérifiez l'URL de votre flux RSS et réessayez.</p>
  </div>
</template>

<script>
export default {};
</script>

```

Ensuite, mettez à jour le fichier `PodcastFeed.vue` comme suit afin d'importer le composant :

```js
<template>
  <div class="podcast-input-feed">
    <label for="email">URL du flux RSS du podcast</label>
    <div class="">
      <!-- liaison du champ d'entrée d'URL à la propriété de données 'url' -->
      <input
        type="url"
        name="url"
        id="url"
        v-model="url"
        placeholder="https://rss.your-org.org/feed/"
        aria-describedby="rss-url"
      />
    </div>
    <!-- connexion du clic sur le bouton à la méthode 'getRssFeed' -->
    <button @click="getRssFeed()" type="button" class="">Obtenir le flux</button>
	<!-- Ajout de ces deux nouveaux composants -->
    <podcast-info v-if="podcast.title && !requestError" :podcast="podcast" />
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../supabase";
import { store } from "../store";

import PodcastInfo from "./PodcastInfo.vue";

export default {
  components: {
    PodcastInfo,
  },

  setup() {
    // J'initialise l'URL avec une URL que je sais fonctionner, afin de ne pas avoir à saisir une URL à chaque fois que je développe.
    // n'hésitez pas à changer cela par une URL de votre choix
    const url = ref("https://anchor.fm/s/3e9db190/podcast/rss");
    // initialisation de l'état du podcast à un objet vide
    const podcast = ref({});
    const requestError = ref(false);

    function getRssFeed() {
      const feedUrl = url.value;
      return (
        fetch(feedUrl)
          // cela retourne une promesse, nous devons donc la convertir en une chaîne
          .then((response) => response.text())
          // cette ligne suivante est pour analyser la réponse XML
          .then((str) =>
            new window.DOMParser().parseFromString(str, "text/xml")
          )
          // analyse des données de la réponse XML et définition dans l'état du podcast
          .then((data) => {
            console.log("Data: ", data);
            podcast.value.image_url = data
              .querySelector("image")
              .querySelector("url").innerHTML;
            podcast.value.title = data.querySelector("title").textContent;
            podcast.value.description =
              data.querySelector("description").textContent;
            podcast.value.rss_url = feedUrl;
          })
          .catch((err) => {
            requestError.value = true;
          })
      );
    }
    return {
      url,
      podcast,
      store,
      requestError,

      getRssFeed,
    };
  },
};
</script>

```

Maintenant, lorsque vous cliquez sur le bouton "Obtenir le flux", vous devriez voir ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-18-at-3.05.15-PM.png)

Maintenant que nous pouvons afficher les informations, nous pouvons configurer l'application pour sauvegarder les informations dans Supabase. 

## Comment ajouter une table à la base de données Supabase

La première chose que nous devons faire est d'ajouter une table à notre base de données Supabase. Dans le tableau de bord de votre projet sur Supabase, sélectionnez l'éditeur de table et cliquez sur le bouton `Nouvelle table`. Je nomme la nouvelle table `podcasts`. Activez la sécurité au niveau des lignes (cela rend notre base de données plus sécurisée) et ajoutez les colonnes suivantes :

* id (cette colonne doit être remplie pour vous lorsque vous créez une nouvelle table)
* created_at
* name
* image_url
* description
* rss_url
* user_id (pour celui-ci, nous voulons le lier via une clé étrangère à notre table d'utilisateurs créée par le service d'authentification. Cliquez sur l'icône de chaîne pour configurer cela et le lier à la table `users` sur la colonne `id`.)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-01-19-at-9.08.50-AM.png)
_configuration de la table podcasts_

Parce que nous avons activé la sécurité au niveau des lignes, la table n'autorisera pas l'insertion de quoi que ce soit jusqu'à ce que nous mettons à jour les politiques pour celle-ci. 

Sous l'onglet Authentification, il y a une section appelée 'Politiques'. Vous devriez y voir la table `podcasts` et un bouton pour créer une nouvelle politique. Lorsque vous cliquez dessus, il vous donnera l'option de créer une politique à partir d'un modèle. Choisissez le modèle appelé 'Activer l'accès d'insertion pour les utilisateurs authentifiés uniquement'. Maintenant, seuls les utilisateurs authentifiés ont accès pour insérer quoi que ce soit dans la table. 

Lorsque Supabase exécute la commande `insert`, il exécutera automatiquement une commande `select` et retournera la ligne nouvellement insérée. À cause de cela, nous devons également ajouter une politique à la table permettant à l'utilisateur un accès `SELECT`. 

Créez une nouvelle politique avec le nom `Activer la sélection basée sur l'ID utilisateur` et dans la section `expression USING`, mettez `(uid() = user_id)`. Cela empêchera les utilisateurs de lire les informations d'autres utilisateurs, tout en leur donnant accès à leurs propres podcasts dans la table.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/select-user-policy.png)
_Politique de sélection basée sur l'ID utilisateur_

## Comment relier l'interface utilisateur à la base de données pour que l'utilisateur puisse sauvegarder des podcasts

Pour ajouter un podcast à notre base de données, nous allons d'abord ajouter un bouton au composant `PodcastInfo`. Ajoutez ce code en bas de la `<div class="podcast-info">` :

```html
<button @click="addPodcast">Ajouter à Mes Podcasts</button>
```

Maintenant, ajoutez une méthode appelée `addPodcast` à la fonction de configuration du composant comme ceci. N'oubliez pas d'ajouter les `props` à l'argument de la fonction de configuration.

```js
setup(props) {
    function addPodcast() {
      // Configuration de l'objet podcast à envoyer à supabase
      const podcast = {
        name: props.podcast.title,
        image_url: props.podcast.image_url,
        description: props.podcast.description,
        rss_url: props.podcast.rss_url,
        user_id: store.state.user.id,
      };
      // appel de la méthode supabase pour insérer dans la base de données
      supabase
        .from("podcasts")
        .insert(podcast)
        .then(({ body }) => {
          store.addPodcastToStore(body[0]);
        })
        .catch((err) => {
          console.log(err);
        });
    }

    return {
      addPodcast,
    };
  },
```

Vous pouvez voir dans l'instruction `.then` que nous appelons une méthode du store global. Mettez à jour le fichier `store.js` comme suit :

```js
import { reactive } from "vue";

export const store = {
  state: reactive({
    user: {},
    // ajout du tableau de podcasts au store global
    podcasts: [],
  }),

  // ajout de la méthode addPodcastToStore à l'objet store
  addPodcastToStore(podcast) {
    this.state.podcasts.push(podcast);
  },
};
```

Maintenant, lorsque nous cliquons sur le bouton "Ajouter à Mes Podcasts", l'application fait un appel à Supabase puis prend le résultat de cet appel et l'ajoute au tableau de podcasts dans le store global. (Si vous obtenez une erreur 403, assurez-vous d'avoir configuré correctement les politiques. Essayez peut-être de redémarrer le serveur de développement.)

Si un podcast est déjà dans la liste des podcasts d'un utilisateur, nous ne voulons pas qu'il puisse cliquer à nouveau sur le bouton d'ajout. Pour éviter cela, nous devons d'abord appeler Supabase pour obtenir tous les podcasts de l'utilisateur, puis vérifier si le podcast qu'il consulte est dans cette liste.

Cette méthode ne sera pas spécifique à un seul composant, nous voulons donc la créer à l'intérieur du store global. Ainsi, tout composant y a accès. Ajoutez cette méthode au fichier `store.js` sous la méthode `addPodcastToStore` :

```js
getPodcastsFromDB() {
    supabase
        .from("podcasts")
        .select("*")
        .then(({ body }) => {
            this.state.podcasts = body;
        });
},
```

Ensuite, nous voulons mettre à jour la méthode pour qu'elle soit appelée chaque fois qu'un utilisateur se connecte. À l'intérieur de `App.vue`, changez le gestionnaire `onAuthStateChange` comme suit :

```js
supabase.auth.onAuthStateChange((event, session) => {
    if (event == "SIGNED_OUT") {
        store.state.user = null;
    } else {
        // faire un appel à supabase pour obtenir les podcasts de l'utilisateur
        store.getPodcastsFromDB();
        store.state.user = session.user;
    }
});
```

Maintenant, mettez à jour le fichier `PodcastInfo.vue` comme suit afin d'indiquer à l'utilisateur si un podcast est déjà dans sa bibliothèque.

```js
<template>
  <div class="podcast-info">
    <div class="image-container">
      <img :src="podcast.image_url" alt="" class="" />
    </div>
    <div class="podcast-text">
      <div class="title-desc">
        <p class="title">
          {{ podcast.title }}
        </p>
        <p class="desc">
          {{ podcast.description }}
        </p>
      </div>
    </div>
    <!-- Ajout d'une vérification dans le balisage pour supprimer le bouton si le podcast existe déjà dans la liste de l'utilisateur -->
    <div v-if="isInUserPodcasts" class="in-podcasts">Dans Vos Podcasts</div>
    <button v-else class="" @click="addPodcast">Ajouter à Mes Podcasts</button>
  </div>
</template>

<script>
// importation de computed
import { ref, computed } from "vue";
import { store } from "../store";
import { supabase } from "../supabase";

export default {
  props: {
    podcast: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    // ajout d'une propriété calculée vérifiant si le podcast est dans les podcasts de l'utilisateur
    const isInUserPodcasts = computed(() => {
      return store.state.podcasts.some(
        (podcast) => podcast.rss_url === props.podcast.rss_url
      );
    });

    function addPodcast() {
      // vérification si le podcast est déjà dans les podcasts de l'utilisateur
      if (isInUserPodcasts.value) {
        alert("Vous avez déjà ce podcast dans votre liste !");
      } else {
        const podcast = {
          name: props.podcast.title,
          image_url: props.podcast.image_url,
          description: props.podcast.description,
          rss_url: props.podcast.rss_url,
          user_id: store.state.user.id,
        };
        supabase
          .from("podcasts")
          .insert(podcast)
          .then(({ body }) => {
            store.addPodcastToStore(body[0]);
          })
          .catch((err) => {
            console.log(err);
          });
      }
    }

    return {
      // exposition de la propriété calculée isInUserPodcasts
      isInUserPodcasts,
      addPodcast,
    };
  },
};
</script>

<style scoped></style>

```

Ensuite, nous voulons afficher une liste de podcasts que l'utilisateur a ajoutés à sa bibliothèque. Nous avons la liste dans le store global, donc nous devons simplement parcourir celle-ci pour afficher les informations nécessaires. 

Ajoutez ce qui suit en bas du modèle `PodcastFeed.vue` :

```html
<!-- Parcourir les podcasts et les afficher -->
  <div class="feeds">
    <h2 class="">Vos flux de podcasts</h2>
    <ul class="">
      <li v-for="pod in store.state.podcasts" :key="pod.id" class="">
        <a :href="`/podcast/${pod.id}`" class="">
          <img :src="pod.image_url" :alt="`logo pour ${pod.name}`" class="" />
          <p class="">{{ pod.name }}</p>
        </a>
      </li>
    </ul>
  </div>
```

## Comment configurer les autres pages pour notre application de podcast

Maintenant que nous avons la liste des podcasts affichée dans l'application, nous avons besoin d'un moyen de naviguer vers un podcast individuel. Nous avons le balisage configuré pour lier à un chemin comme `/podcast/{podcast_id}`. Maintenant, nous devons mettre à jour notre application pour gérer les routes comme celle-ci. 

Tout d'abord, installez vue-router en utilisant `npm i vue-router`.

Ensuite, créez un fichier appelé `router.js` avec le code suivant :

```js
// Importation de Vue Router
import * as VueRouter from "vue-router";

// Importation des composants qui s'afficheront sur les différentes routes
import PodcastFeed from "./components/PodcastFeed.vue";
import PodcastDetail from "./components/PodcastDetail.vue";

// Configuration des routes
const routes = [
  { path: "/", component: PodcastFeed },
  { path: "/podcast/:id", component: PodcastDetail },
];

// Initialisation du routeur
const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
});

// Exportation du routeur
export default router;

```

Mettez à jour `main.js` pour utiliser le routeur dans l'application Vue :

```js
import { createApp } from "vue";
import router from "./router";
import App from "./App.vue";
import "./index.css";

const app = createApp(App);
app.use(router);
app.mount("#app");
```

Mettez à jour `App.vue` pour afficher le composant `router-view` fourni par Vue Router :

```html
<template>
  <button v-if="store.state.user" class="signout-button" @click="signOut">Se déconnecter</button>
  <!-- Vérifiez si l'utilisateur est disponible dans le store, sinon affichez le composant d'authentification -->
  <Auth v-if="!store.state.user" />
  <!-- Si l'utilisateur est disponible, affichez l'application -->
  <div v-else class="app">
    <router-view></router-view>
  </div>
</template>
```

Maintenant, créez un fichier `PodcastDetail.vue` qui affichera les informations sur les épisodes du podcast :

```js
<template>
  <nav class="">
    <a href="/" class="">Accueil</a>
  </nav>
  <!-- Disposition de base pour afficher les informations sur le podcast -->
  <div class="podcast-detail">
    <img :src="podcast.image_url" :alt="podcast.name" class="" />
    <h1 class="">{{ podcast.name }}</h1>
    <p>{{ podcast.description }}</p>
    <h2 class="">Épisodes</h2>
    <!-- Boucle à travers chaque épisode d'un podcast et affichage des informations sur l'épisode -->
    <ul class="">
      <li
        v-for="episode in episodes"
        :key="episode.guid || episode.link"
        class=""
      >
        <div class="info">
          <h3>{{ episode.title }}</h3>
          <audio class="" controls>
            <source :src="episode.url" type="audio/mpeg" />
            Afficher
          </audio>          
        </div>        
      </li>
    </ul>
  </div>
</template>

<script>
// Importation des méthodes nécessaires
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { supabase } from "../supabase";

export default {
  setup() {
    const route = useRoute();
    const podcast = ref({});
    const episodes = ref([]);

    // Obtention des informations sur le podcast à partir de la base de données
    async function getPodcastData() {
      const {
        data: [podcastinfo],
      } = await supabase.from("podcasts").select().eq("id", route.params.id);
      podcast.value = podcastinfo;

      // Appel à l'URL de l'épisode pour obtenir les informations sur l'épisode
      getEpisodes(podcastinfo.rss_url);
    }

    function getEpisodes(url) {
      fetch(url)
        .then((response) => response.text())
        .then((str) => new window.DOMParser().parseFromString(str, "text/xml"))
        .then((data) => {
          // Recherche de toutes les balises "item" dans la réponse XML qui contiendront les informations sur l'épisode
          const items = data.querySelectorAll("item");
          // Boucle à travers chaque élément et obtention des informations sur l'épisode et ajout à la liste 'episodes'
          items.forEach((item) => {
            let url;

            // Tous les épisodes de podcast n'auront pas la balise `enclosure`, nous devons donc vérifier si elle existe
            try {
              url = item.querySelector("enclosure").getAttribute("url");
            } catch (e) {
              console.log("error", e);
              url = item.querySelector("link").innerHTML;
            }

            episodes.value.push({
              // cette propriété `title` et la propriété `guid` semblent un peu différentes car le titre contient des balises CDATA qui doivent être récupérées avec la propriété 'childNodes'
              title: item.querySelector("title").childNodes[0].textContent,
              link: url,
              url: url,
              description: item.querySelector("description").innerHTML,
              pubDate: item.querySelector("pubDate").innerHTML,
              guid: item.querySelector("guid").childNodes[0].textContent,
            });
          });
        })
        .catch((err) => {
          alert("Impossible d'obtenir les épisodes", err);
        });
    }

    onMounted(() => {
      // Obtention des informations sur le podcast à partir de la base de données une fois le composant monté
      getPodcastData();
    });

    return {
      podcast,
      episodes,
    };
  },
};
</script>

<style scoped></style>

```

Avec ces modifications, nous pouvons maintenant voir les épisodes individuels du podcast et les lire en utilisant la balise HTML `<audio>`. 

## Comment obtenir les transcriptions des podcasts

La dernière étape consiste à obtenir les transcriptions des podcasts, puis à les sauvegarder dans notre base de données.

Si vous ne l'avez pas encore fait, vous devrez obtenir une [clé API gratuite de Deepgram](https://console.deepgram.com/signup) afin de traiter l'audio et d'obtenir les transcriptions. 

Une fois que vous avez obtenu la clé API, ajoutez-la à votre fichier `.env.local` en tant que `VITE_DEEPGRAM_KEY`. Assurez-vous de redémarrer votre serveur de développement ici, sinon vous obtiendrez probablement une erreur 403 Forbidden lorsque nous appellerons enfin l'API.

Ensuite, ajoutez ce code à un fichier deepgram.js dans le dossier `src`.

```js
const deepgramKey = import.meta.env.VITE_DEEPGRAM_KEY;

async function deepgram(url) {
  const response = await fetch(
    "https://api.deepgram.com/v1/listen?punctuate=true&diarize=true&utterances=true",
    {
      method: "POST",
      headers: {
        Authorization: `Token ${deepgramKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        url: url,
      }),
    }
  );
  const json = await response.json();
  return json.results;
}

export default deepgram;

```

Cela nous donne une fonction utilitaire que nous pouvons importer dans notre application dans d'autres fichiers pour appeler l'API Deepgram afin d'obtenir les transcriptions. Nous avons ajouté la ponctuation, la diarisation et les énoncés à l'URL en tant que paramètres pour obtenir une transcription plus propre et plus facile à lire. 

Maintenant que nous avons cela, nous devons ajouter quelques fonctionnalités au fichier `PodcastDetail.vue`. Je vais passer en revue les modifications et mettre ensuite le code final du fichier.

Tout d'abord, nous devons avoir un état pour suivre les transcriptions que nous obtenons, ainsi qu'un état de chargement une fois que nous cliquons sur un bouton pour obtenir une transcription. Nous allons donc ajouter ces deux lignes à notre fonction de configuration :

```js
let transcriptions = ref({});
const episodeTranscriptionLoading = ref([]);
```

N'oubliez pas de les ajouter à l'objet de retour de la fonction `setup`.

Ensuite, ajoutez cette fonction pour faire la demande à Deepgram, puis ajoutez la transcription à l'objet local `transcriptions`.

```js
// Fonction pour obtenir une transcription de Deepgram, en passant l'URL de l'épisode
async function getTranscription(episode) {
    // définition de l'état de chargement à vrai pour l'épisode
    episodeTranscriptionLoading.value.push(episode.guid);
    const transcription = await deepgram(episode.url);
    // définition d'un identifiant unique pour la transcription de l'épisode
    transcriptions.value[`${podcast.value.id}---${episode.guid}`] =
        transcription;
    // suppression de l'état de chargement pour l'épisode
    episodeTranscriptionLoading.value.splice(
        episodeTranscriptionLoading.value.indexOf(episode.guid),
        1
    );
}
```

Assurez-vous d'importer la fonction deepgram depuis `deepgram.js` en haut de la balise script.

Ensuite, mettez à jour le modèle comme suit :

```html
<template>
  <nav class="">
    <a href="/" class="">Accueil</a>
  </nav>
  <!-- Disposition de base pour afficher les informations sur le podcast -->
  <div class="podcast-detail">
    <img :src="podcast.image_url" :alt="podcast.name" class="" />
    <h1 class="">{{ podcast.name }}</h1>
    <p>{{ podcast.description }}</p>
    <h2 class="">Épisodes</h2>
    <!-- Boucle à travers chaque épisode d'un podcast et affichage des informations sur l'épisode -->
    <ul class="">
      <li
        v-for="episode in episodes"
        :key="episode.guid || episode.link"
        class=""
      >
        <div class="info">
          <h3>{{ episode.title }}</h3>
          <audio class="" controls>
            <source :src="episode.url" type="audio/mpeg" />
            Afficher
          </audio>
            <!-- bouton pour obtenir les transcriptions -->
          <button
            v-if="!transcriptions[`${podcast.id}---${episode.guid}`]"
            @click.prevent="getTranscription(episode)"
            class=""
          >
            {{
              episodeTranscriptionLoading.includes(episode.guid)
                ? "Chargement..."
                : "Obtenir la transcription"
            }}
          </button>
        </div>
          <!-- boîte pour afficher la transcription -->
        <div
          v-if="transcriptions[`${podcast.id}---${episode.guid}`]"
          class="transcription"
        >
          <p>
            {{
              transcriptions[`${podcast.id}---${episode.guid}`].channels[0]
                .alternatives[0].transcript
            }}
          </p>
        </div> 
      </li>
    </ul>
  </div>
</template>
```

## Comment sauvegarder les transcriptions

Maintenant que nous pouvons obtenir les transcriptions, nous devons ajouter la fonctionnalité pour les sauvegarder dans Supabase. 

Tout d'abord, allez créer une table dans Supabase comme nous l'avons fait ci-dessus, mais cette fois nommez la table `transcriptions`. Vous voudrez les éléments suivants comme colonnes :

* **id** – varchar (primaire) Supprimez également la case à cocher "Is Identity" dans les paramètres de cette colonne
* **podcast_id** – int8
* **episode_guid** – varchar
* **transcript** – text
* **user_id** – uuid (Vous devrez lier cela à la table des utilisateurs en cliquant sur l'icône de lien)
* **created_at** – timestamptz

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-22-at-4.40.52-PM.png)
_colonnes pour la table des transcriptions_

Une fois que cette table est configurée, nous pouvons ajouter une propriété réactive appelée `savedTranscriptions` au composant, puis ajouter le code suivant pour sauvegarder les transcriptions dans Supabase. Ensuite, nous les stockerons dans l'objet `savedTranscriptions`.

```js
function saveTranscription(podcastId, episodeGuid) {
    supabase
        .from("transcriptions")
        .insert({
        id: `${podcastId}---${episodeGuid}`,
        podcast_id: podcastId,
        episode_guid: episodeGuid,
        transcript:
        transcriptions.value[`${podcastId}---${episodeGuid}`].channels[0]
        .alternatives[0].transcript,
        user_id: store.state.user.id,
    })
        .then(({ data: [transcriptObject] }) => {
        savedTranscriptions.value[transcriptObject.id] =
            transcriptObject.transcript;
    });
}
```

Une fois qu'un utilisateur a une transcription sauvegardée, nous devons l'afficher chaque fois qu'il revisite une page. Ajoutez cette fonction pour obtenir ces données de Supabase :

```js
async function getTranscriptions() {
    const { data: transcriptions } = await supabase
    .from("transcriptions")
    .select()
    .eq("podcast_id", podcast.value.id);
    console.log("Transcriptions", transcriptions);
    transcriptions.forEach((transcript) => {
        console.log("id", transcript.id);
        savedTranscriptions.value[transcript.id] = transcript.transcript;
    });
}
```

Nous voulons que cela soit appelé chaque fois qu'un utilisateur accède à cette page, mais pas avant d'avoir obtenu les informations sur le podcast. Ajoutez un appel à `getTranscriptions` à la fin de la fonction `getPodcastData` pour faire cela.

La dernière chose à faire est de mettre à jour le modèle pour inclure les boutons de sauvegarde et pour afficher les transcriptions si elles sont dans les objets sauvegardés. Le code final pour `PodcastDetail.vue` devrait alors ressembler à ceci :

```js
<template>
  <nav class="">
    <a href="/" class="">Accueil</a>
  </nav>
  <!-- Disposition de base pour afficher les informations sur le podcast -->
  <div class="podcast-detail">
    <img :src="podcast.image_url" :alt="podcast.name" class="" />
    <h1 class="">{{ podcast.name }}</h1>
    <p>{{ podcast.description }}</p>
    <h2 class="">Épisodes</h2>
    <!-- Boucle à travers chaque épisode d'un podcast et affichage des informations sur l'épisode -->
    <ul class="">
      <li
        v-for="episode in episodes"
        :key="episode.guid || episode.link"
        class=""
      >
        <div class="info">
          <h3>{{ episode.title }}</h3>
          <audio class="" controls>
            <source :src="episode.url" type="audio/mpeg" />
            Afficher
          </audio>
          <button
            v-if="savedTranscriptions[`${podcast.id}---${episode.guid}`]"
            disabled
          >
            Transcription sauvegardée
          </button>
          <button
            v-else-if="
              !transcriptions[`${podcast.id}---${episode.guid}`] &&
              !savedTranscriptions[`${podcast.id}---${episode.guid}`]
            "
            @click.prevent="getTranscription(episode)"
            class=""
          >
            {{
              episodeTranscriptionLoading.includes(episode.guid)
                ? "Chargement..."
                : "Obtenir la transcription"
            }}
          </button>
          <button
            v-if="
              transcriptions[`${podcast.id}---${episode.guid}`] &&
              !savedTranscriptions[`${podcast.id}---${episode.guid}`]
            "
            class="save"
            @click.prevent="saveTranscription(podcast.id, episode.guid)"
          >
            Sauvegarder la transcription
          </button>
        </div>
        <div
          v-if="savedTranscriptions[`${podcast.id}---${episode.guid}`]"
          class="transcription"
        >
          <p>
            {{ savedTranscriptions[`${podcast.id}---${episode.guid}`] }}
          </p>
        </div>
        <div
          v-else-if="transcriptions[`${podcast.id}---${episode.guid}`]"
          class="transcription"
        >
          <p>
            {{
              transcriptions[`${podcast.id}---${episode.guid}`].channels[0]
                .alternatives[0].transcript
            }}
          </p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
// Importation des méthodes nécessaires
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { supabase } from "../supabase";
import { store } from "../store";
import deepgram from "../deepgram";

export default {
  setup() {
    const route = useRoute();
    const podcast = ref({});
    const episodes = ref([]);
    let transcriptions = ref({});
    let savedTranscriptions = ref({});
    const episodeTranscriptionLoading = ref([]);

    // Obtention des informations sur le podcast à partir de la base de données
    async function getPodcastData() {
      const {
        data: [podcastinfo],
      } = await supabase.from("podcasts").select().eq("id", route.params.id);
      podcast.value = podcastinfo;

      // Appel à l'URL de l'épisode pour obtenir les informations sur l'épisode
      getEpisodes(podcastinfo.rss_url);
      await getTranscriptions();
    }

    function getEpisodes(url) {
      fetch(url)
        .then((response) => response.text())
        .then((str) => new window.DOMParser().parseFromString(str, "text/xml"))
        .then((data) => {
          // Recherche de toutes les balises "item" dans la réponse XML qui contiendront les informations sur l'épisode
          const items = data.querySelectorAll("item");
          // Boucle à travers chaque élément et obtention des informations sur l'épisode et ajout à la liste 'episodes'
          items.forEach((item) => {
            let url;

            // Tous les épisodes de podcast n'auront pas la balise `enclosure`, nous devons donc vérifier si elle existe
            try {
              url = item.querySelector("enclosure").getAttribute("url");
            } catch (e) {
              console.log("error", e);
              url = item.querySelector("link").innerHTML;
            }

            episodes.value.push({
              // cette propriété `title` et la propriété `guid` semblent un peu différentes car le titre contient des balises CDATA qui doivent être récupérées avec la propriété 'childNodes'
              title: item.querySelector("title").childNodes[0].textContent,
              link: url,
              url: url,
              description: item.querySelector("description").innerHTML,
              pubDate: item.querySelector("pubDate").innerHTML,
              guid: item.querySelector("guid").childNodes[0].textContent,
            });
          });
        })
        .catch((err) => {
          alert("Impossible d'obtenir les épisodes", err);
        });
    }

    // Fonction pour obtenir une transcription de Deepgram, en passant l'URL de l'épisode
    async function getTranscription(episode) {
      // définition de l'état de chargement à vrai pour l'épisode
      episodeTranscriptionLoading.value.push(episode.guid);
      const transcription = await deepgram(episode.url);
      // définition d'un identifiant unique pour la transcription de l'épisode
      transcriptions.value[`${podcast.value.id}---${episode.guid}`] =
        transcription;
      // suppression de l'état de chargement pour l'épisode
      episodeTranscriptionLoading.value.splice(
        episodeTranscriptionLoading.value.indexOf(episode.guid),
        1
      );
    }

    function saveTranscription(podcastId, episodeGuid) {
      console.log(
        "sauvegarde de la transcription",
        transcriptions.value[`${podcastId}---${episodeGuid}`]
      );
      supabase
        .from("transcriptions")
        .insert({
          id: `${podcastId}---${episodeGuid}`,
          podcast_id: podcastId,
          episode_guid: episodeGuid,
          transcript:
            transcriptions.value[`${podcastId}---${episodeGuid}`].channels[0]
              .alternatives[0].transcript,
          user_id: store.state.user.id,
        })
        .then(({ data: [transcriptObject] }) => {
          console.log("sauvegardé", transcriptObject);
          savedTranscriptions.value[transcriptObject.id] =
            transcriptObject.transcript;
        });
    }

    async function getTranscriptions() {
      const { data: transcriptions } = await supabase
        .from("transcriptions")
        .select()
        .eq("podcast_id", podcast.value.id);
      console.log("Transcriptions", transcriptions);
      transcriptions.forEach((transcript) => {
        console.log("id", transcript.id);
        savedTranscriptions.value[transcript.id] = transcript.transcript;
      });
    }

    onMounted(() => {
      // Obtention des informations sur le podcast à partir de la base de données une fois le composant monté
      getPodcastData();
    });

    return {
      podcast,
      episodes,
      transcriptions,
      savedTranscriptions,
      episodeTranscriptionLoading,

      getTranscription,
      saveTranscription,
    };
  },
};
</script>

<style scoped></style>

```

## Conclusion

Si vous avez suivi les étapes ci-dessus, vous devriez avoir une application fonctionnelle. [Voici le code final](https://github.com/briancbarrow/vue-supabase-auth/tree/final-podcast-feed-transcriptions) si vous souhaitez vérifier par rapport à ce que j'ai écrit.

Je sais que j'ai apprécié la création de l'application. Supabase rend vraiment facile la mise en place d'une base de données/backend. N'hésitez pas à me contacter sur [Twitter](https://twitter.com/the_BrianB) si vous avez des questions !