---
title: Comment ajouter l'authentification Supabase à une application Vue
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2022-02-10T16:40:00.000Z'
originalURL: https://freecodecamp.org/news/add-supabase-authentication-to-vue
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Getting-Started-with-supabase-blog@2x.jpg
tags:
- name: authentication
  slug: authentication
- name: supabase
  slug: supabase
- name: vue
  slug: vue
seo_title: Comment ajouter l'authentification Supabase à une application Vue
seo_desc: "In this post we will walk through getting authentication set up using Supabase\
  \ and Vue 3. \nThis will also work with Vue 2, but you'll need to move things around\
  \ to work with the options API. I am using Vue 3 as it is now the default version.\
  \ \nJust a ..."
---

Dans cet article, nous allons passer en revue la configuration de l'authentification en utilisant Supabase et Vue 3. 

Cela fonctionnera également avec Vue 2, mais vous devrez réorganiser certaines choses pour qu'elles fonctionnent avec l'API des options. J'utilise Vue 3 car c'est [désormais la version par défaut](https://blog.vuejs.org/posts/vue-3-as-the-new-default.html). 

Juste un petit avertissement – il n'y aura pas beaucoup de style impliqué ici afin que l'accent reste sur l'authentification Supabase. 

## Prérequis

Vous devriez être familier avec JavaScript et avoir une certaine expérience avec Vue 3. Avoir une certaine expérience avec Supabase aidera, mais ce n'est pas nécessaire. 

Si vous avez besoin d'une révision rapide de Supabase, vous pouvez consulter [un précédent article](https://developers.deepgram.com/blog/2021/11/getting-started-with-supabase/) où je passe en revue comment commencer à l'utiliser. 

Vous aurez également besoin de [Node.js](https://nodejs.org/en/) et de NPM installés sur votre machine.

## Démarrage

Commençons par construire une partie du frontend avant de commencer à construire la base de données en utilisant Supabase. 

La première chose que nous devons faire est de configurer notre projet. Dans votre terminal et dans le dossier où vous souhaitez que ce projet soit situé, exécutez cette commande :

```bash
npm init vite@latest vue-supabase-auth --template vue
```

Cela initialisera un nouveau projet Vite avec Vue 3 dans un dossier appelé `vue-supabase-auth`. 

Ouvrez ce projet dans votre éditeur de code préféré et ouvrez le fichier `App.vue` à l'intérieur du dossier `src`. Lorsque j'ai initialisé le projet, Vite a placé la balise script au-dessus de la balise template. Ma préférence personnelle est de déplacer la balise template en haut, mais ce n'est pas nécessaire.

## Ajouter l'authentification à l'application

L'étape suivante consiste à ajouter l'authentification à notre application. Supabase nous donne la possibilité d'authentifier un utilisateur de plusieurs manières différentes. 

Nous allons passer en revue comment configurer l'authentification de base par e-mail/mot de passe, et l'authentification avec un "lien magique". Un "lien magique" est simplement un lien envoyé à l'e-mail d'un utilisateur qui, lorsqu'il est cliqué, les amènera à votre application et les connectera. 

### Obtenir un compte Supabase

Si vous ne l'avez pas déjà fait, vous devrez vous inscrire pour un compte sur [Supabase](https://app.supabase.io). Il vous demande de vous inscrire avec GitHub, donc si vous n'avez pas de compte GitHub, vous devriez également vous inscrire pour en obtenir un.

Une fois connecté, vous cliquerez sur le bouton vert qui dit "Nouveau Projet" et sélectionnerez l'organisation par défaut qui a été créée lorsque vous vous êtes connecté. La mienne s'appelait "briancbarrow's Org." 

Cela fera apparaître une boîte où vous fournissez quelques informations sur le projet. Je vais le nommer `basic-auth`, lui donner un mot de passe fort, et ensuite je vais sélectionner la région `Ouest des États-Unis (Nord de la Californie)` car c'est la plus proche de moi.

Une fois le projet configuré, allez dans Authentication -> Settings et désactivez "Enable email confirmations." Cela rend simplement les choses un peu plus fluides pour ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/disable-email-confirmations.png)
_Montrant le paramètre "Enable email confirmations" désactivé_

### Configurer Supabase dans le projet Vue

Tout d'abord, nous devons exécuter `npm install @supabase/supabase-js` pour obtenir le package JavaScript pour intégrer avec Supabase.

Ensuite, nous devons créer un fichier `supabase.js` dans le dossier `src` du projet. Celui-ci doit contenir ce qui suit :

```js
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseAnonKey)
```

Comme vous pouvez le voir dans le code ci-dessus, nous devons configurer certaines variables d'environnement qui contiennent nos clés Supabase. Créez un fichier `.env.local` à la racine du projet et ajoutez `VITE_SUPABASE_URL` et `VITE_SUPABASE_ANON_KEY`. Vous pouvez trouver votre URL et votre clé anonyme sur le tableau de bord de votre projet Supabase. 

Votre fichier `.env.local` ressemblera à ceci :

```
VITE_SUPABASE_URL=VOTRE_SUPABASE_URL
VITE_SUPABASE_ANON_KEY=VOTRE_SUPABASE_ANON_KEY
```

Nous voulons également créer un magasin central pour les données nécessaires dans toute l'application, comme les informations utilisateur. Créez un fichier `store.js` dans le dossier `src` et remplissez-le avec ce code :

```js
import { reactive } from "vue";

export const store = {
  state: reactive({
    user: {},
  }),
};
```

### Créer les composants SignIn et SignUp

L'authentification Supabase sépare les processus `signIn` et `signUp`, nous devons donc les gérer différemment. J'ai décidé de créer deux composants séparés juste pour clarifier les choses dans ma tête.

Créez un fichier `SignUp.vue` dans le dossier des composants et ajoutez le code suivant :

```js
<template>
  <div>
    <h2>Inscription pour un compte</h2>
    <form @submit.prevent="handleSignup">
      <div>
        <label for="email">Email</label>
        <input id="email" type="email" v-model="email" />
      </div>
      <div>
        <label for="password">Mot de passe</label>
        <input id="password" type="password" v-model="password" />
      </div>
      <div>
        <button type="submit">S'inscrire</button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../supabase";

export default {
  setup() {
    const email = ref("");
    const password = ref("");

    const handleSignup = async () => {
      try {
        // Utilisez la méthode fournie par Supabase pour gérer l'inscription
        const { error } = await supabase.auth.signUp({
          email: email.value,
          password: password.value,
        });
        if (error) throw error;
      } catch (error) {
        alert(error.error_description || error.message);
      }
    };

    return {
      email,
      password,
      handleSignup,
    };
  },
};
</script>

```

Maintenant, créez un fichier `SignIn.vue` et ajoutez le code ci-dessous. Les seules différences sont les noms des méthodes appelées, et le texte est légèrement différent dans le balisage.

```js
<template>
  <div>
    <h2>Connectez-vous à votre compte</h2>
    <form @submit.prevent="handleSignin">
      <div>
        <label for="email">Email</label>
        <input id="email" type="email" v-model="email" />
      </div>
      <div>
        <label for="password">Mot de passe</label>
        <input id="password" type="password" v-model="password" />
      </div>
      <div>
        <button type="submit">Se connecter</button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../supabase";

export default {
  setup() {
    const email = ref("");
    const password = ref("");

    const handleSignin = async () => {
      try {
        // Utilisez la méthode fournie par Supabase pour gérer la connexion
        const { error } = await supabase.auth.signIn({
          email: email.value,
          password: password.value,
        });
        if (error) throw error;
      } catch (error) {
        alert(error.error_description || error.message);
      }
    };

    return {
      email,
      password,
      handleSignin,
    };
  },
};
</script>

```

Maintenant, nous voulons créer un composant wrapper pour ces deux-là. Créez un fichier nommé `Auth.vue` avec le code ci-dessous :

```js
<template>
  <div>
    <sign-up v-if="isSignUp" />
    <sign-in v-else />
    <button @click="isSignUp = !isSignUp">
      {{
        isSignUp
          ? "Vous avez déjà un compte ? Connectez-vous"
          : "Vous n'avez pas encore de compte ? Inscrivez-vous"
      }}
    </button>
  </div>
</template>

<script>
import { ref } from "vue";
import SignUp from "./SignUp.vue";
import SignIn from "./SignIn.vue";
export default {
  components: { SignUp, SignIn },
  setup() {
    const isSignUp = ref(true);

    return {
      isSignUp,
    };
  },
};
</script>

<style scoped></style>

```

Cela permet simplement à l'utilisateur de basculer entre les vues `SignIn` et `SignUp`. Maintenant, ouvrez à nouveau `App.vue` et mettez à jour le code comme suit :

```js
<template>
  <!-- Vérifiez si l'utilisateur est disponible dans le store, sinon affichez le composant auth -->
  <Auth v-if="!store.state.user" />
  <!-- Si l'utilisateur est disponible, affichez le composant Hello World -->
  <HelloWorld v-else msg="Hello Vue 3 + Vite" />
</template>

<script>
import Auth from "./components/Auth.vue";
import HelloWorld from "./components/HelloWorld.vue";

import { store } from "./store";
import { supabase } from "./supabase";

export default {
  components: {
    HelloWorld,
    Auth,
  },
  setup() {
    // nous vérifions initialement si un utilisateur est connecté avec Supabase
    store.state.user = supabase.auth.user();
    // nous configurons ensuite un écouteur pour mettre à jour le store lorsque l'utilisateur change, soit en se connectant, soit en se déconnectant
    supabase.auth.onAuthStateChange((event, session) => {
      if (event == "SIGNED_OUT") {
        store.state.user = null;
      } else {
        store.state.user = session.user;
      }
    });

    return {
      store,
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

Cela affichera le composant `Auth` si un utilisateur n'est pas connecté, sinon il affichera le `HelloWorld.vue` comme nous l'avions initialement configuré.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-09-at-10.14.27-AM.png)
_Formulaire d'inscription_

Inscrivez-vous en utilisant votre e-mail et un mot de passe que vous créez, et vous devriez alors voir à nouveau le composant HelloWorld.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-09-at-10.18.58-AM.png)
_Composant Hello World affiché après l'inscription_

### Comment se déconnecter

Se déconnecter est relativement simple. À l'intérieur du composant HelloWorld, ajoutez ce qui suit en bas de la balise template :

```html
<button @click="signOut">Se déconnecter</button>
```

Ensuite, mettez à jour la balise script sur HelloWorld comme suit :

```html
<script setup>
import { ref } from "vue";
import { supabase } from "../supabase";

defineProps({
  msg: String,
});

const count = ref(0);
async function signOut() {
  const { error } = await supabase.auth.signOut();
}
</script>
```

Vous pouvez voir que nous importons maintenant le fichier `supabase` que nous avons créé précédemment et que nous créons ensuite une méthode `signOut` qui est appelée lors d'un clic sur un bouton. 

### Authentification utilisant le lien magique

Supabase offre également la possibilité d'envoyer aux utilisateurs un lien magique à leur e-mail, qu'ils cliquent, et cela les amène à l'application et les connecte. Le lien qu'il envoie les redirigera vers votre site, nous devons donc nous assurer que nous avons l'URL de redirection correcte dans notre configuration Supabase. 

Accédez à la page Auth -> Settings dans le tableau de bord Supabase de votre projet et assurez-vous que l'URL localhost est dans la case `Site URL`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-09-at-10.24.13-AM.png)
_Assurez-vous que l'URL de votre site correspond à l'endroit où il doit rediriger lors de la connexion_

#### Créer le composant MagicLink

Créez un nouveau fichier dans le dossier des composants appelé `MagicLink.vue` et ajoutez le code suivant :

```js
<template>
  <div>
    <h2>Se connecter avec un lien magique</h2>
    <form @submit.prevent="handleMagicLink">
      <div>
        <label for="email">Email</label>
        <input id="email" type="email" v-model="email" />
      </div>
      <div>
        <button type="submit">Se connecter</button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../supabase";

export default {
  setup() {
    const email = ref("");

    const handleMagicLink = async () => {
      try {
        // Nous appelons la méthode signIn de Supabase pour envoyer le lien magique. Nous ne lui passons que l'e-mail.
        const { error } = await supabase.auth.signIn({
          email: email.value,
        });
        if (error) throw error;
      } catch (error) {
        alert(error.error_description || error.message);
      }
    };

    return {
      email,
      handleMagicLink,
    };
  },
};
</script>

```

Ce composant est très similaire au composant `SignIn`. Il utilise la même méthode, mais pour obtenir le lien magique, nous ne passons que l'e-mail. 

Maintenant, nous devons mettre à jour `Auth.vue` pour utiliser également le composant `MagicLink`. Mettez à jour `Auth.vue` comme suit :

```js
<template>
  <div>
    <!-- Logique v-if pour déterminer quel composant d'authentification afficher -->
    <sign-up v-if="isSignUp && !useMagicLink" />
    <sign-in v-else-if="!isSignUp && !useMagicLink" />
    <magic-link v-else />
    <div v-if="!useMagicLink">
      <button v-if="!useMagicLink" @click="isSignUp = !isSignUp">
        {{
          isSignUp
            ? "Vous avez déjà un compte ? Connectez-vous"
            : "Vous n'avez pas encore de compte ? Inscrivez-vous"
        }}
      </button>
      <p>Ou</p>
    </div>
    <button @click="toggleMagicLink">
      {{
        useMagicLink
          ? "Se connecter avec e-mail et mot de passe"
          : "Se connecter avec un lien magique"
      }}
    </button>
  </div>
</template>

<script>
import { ref } from "vue";
import SignUp from "./SignUp.vue";
import SignIn from "./SignIn.vue";
import MagicLink from "./MagicLink.vue";
export default {
  components: { SignUp, SignIn, MagicLink },
  setup() {
    const isSignUp = ref(true);
    const useMagicLink = ref(false);

    function toggleMagicLink() {
      useMagicLink.value = !useMagicLink.value;
    }

    return {
      isSignUp,
      useMagicLink,

      toggleMagicLink,
    };
  },
};
</script>

<style scoped></style>

```

Maintenant, la page Auth devrait ressembler à ceci par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-09-at-10.50.35-AM.png)
_Vue Auth par défaut_

Et elle devrait ressembler à ceci si l'utilisateur clique sur le bouton "Se connecter avec un lien magique" :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-09-at-10.50.42-AM.png)
_Vue Auth lors de la connexion avec un lien magique_

Si vous entrez votre e-mail et cliquez sur "Se connecter", vous devriez recevoir un e-mail avec le lien magique. Cliquez sur ce lien, et vous devriez être redirigé vers l'application en tant qu'utilisateur connecté, où vous verrez la vue HelloWorld. 

## Résumé

Supabase rend la configuration de l'authentification relativement facile. Ils offrent également une authentification utilisant plusieurs fournisseurs sociaux comme Google, Apple, Github, et bien d'autres. 

Pour mes projets de base, j'aime garder les choses simples et rester avec la connexion par e-mail/mot de passe ou simplement laisser Supabase envoyer un lien magique pour les connecter.