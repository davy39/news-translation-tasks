---
title: Comment créer une application de chat en temps réel avec Nuxt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-10T19:39:17.000Z'
originalURL: https://freecodecamp.org/news/create-a-real-time-chat-application-with-nuxt
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/chat-app-with-nuxt-image.png
tags:
- name: application
  slug: application
- name: Chat
  slug: chat
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
seo_title: Comment créer une application de chat en temps réel avec Nuxt
seo_desc: "By Idorenyin Udoh\nIn a real-time chat application, the recipient can view\
  \ the sender’s message almost immediately. This can either be in a one-on-one conversation\
  \ between two parties or a group conversation. \nAnd that's what we're going to\
  \ build in t..."
---

Par Idorenyin Udoh

Dans une application de chat en temps réel, le destinataire peut voir le message de l'expéditeur presque immédiatement. Cela peut être soit une conversation en tête-à-tête entre deux parties, soit une conversation de groupe. 

Et c'est ce que nous allons construire dans ce tutoriel. Pour cette application, nous allons utiliser [Nuxt](https://nuxtjs.org/), le framework Vue intuitif.

Maintenant que nous savons ce que nous allons construire et la technologie que nous allons utiliser, passons en revue l'API de chat que nous allons utiliser.

Pour cet article, nous allons opter pour [Robin](https://robinapp.io/) en raison de son interface utilisateur minimale et de sa facilité d'intégration dans notre application. Cela étant dit, commençons.

# Étape 1 – Créer l'application Nuxt

Tout d'abord, nous devons créer l'application Nuxt avec l'une des commandes suivantes :

```
yarn create nuxt-app nuxt-chat-app
// OU
npx create-nuxt-app nuxt-chat-app
// OU
npm init nuxt-app nuxt-chat-app
```

# Étape 2 – Créer un compte Robin

Maintenant que notre application est prête, nous devons avoir un compte Robin avant de pouvoir l'utiliser. Rendez-vous sur la [page d'inscription de Robin](https://dashboard.robinapp.co/signup) pour créer un compte d'essai gratuit de 30 jours. 

Robin vous informe 7 jours après la création du compte et vous pouvez retirer votre carte avant la date de facturation. 

Après avoir rempli le formulaire d'inscription, vous serez redirigé vers une page de facturation pour remplir les informations de votre carte. Sur la page suivante, Robin demande le nom de l'application que vous souhaitez créer et son type d'authentification. N'hésitez pas à utiliser le nom de votre choix et l'une des options d'authentification.

![Image](https://paper-attachments.dropbox.com/s_8728EF96CF25BE6F7A46E3619EB658CA92CDD4D1E377FEC5C8707FC59B5068A6_1658071816533_Screenshot+2022-07-17+at+16.29.23.png)

# Étape 3 – Obtenir vos identifiants Robin

Maintenant que nous avons créé une application sur notre tableau de bord Robin, il y a quelque chose que vous devez noter. Il y a plusieurs identifiants dont vous avez besoin lorsque vous utilisez Robin dans votre application Nuxt :

* Clé API,
* Jeton utilisateur,
* Nom d'utilisateur,
* Utilisateurs, et
* Clés

Passons en revue chacun d'eux individuellement.

* Clé API : Robin génère automatiquement la clé API lorsque vous créez une application. Vous pouvez la récupérer soit depuis la page de démarrage, soit depuis la page de configuration de l'API sur votre tableau de bord. Elle est unique pour chaque application.
* Jeton utilisateur : Le jeton utilisateur est un identifiant unique pour chaque utilisateur de votre application Robin. Le jeton qui doit être passé à cette propriété est le vôtre puisque vous êtes celui qui utilise l'application sur votre site. Cependant, il doit être créé par vous, l'utilisateur, généralement sur le serveur, puis utilisé côté client.
* Nom d'utilisateur : Le nom d'utilisateur est le nom de l'utilisateur actuel de votre application Robin. Dans ce cas, ce sera votre nom. Si vous souhaitiez que quelqu'un d'autre inclue votre chat Robin sur son site ou son application web (c'est-à-dire un autre utilisateur de votre application Robin), ce devrait être leur nom.
* Utilisateurs : Les utilisateurs sont une liste des utilisateurs de votre application Robin. Elle contient généralement leurs jetons utilisateur, leurs images de profil et leurs noms d'utilisateur.
* Clés : Cela existe fondamentalement pour nous aider à être flexibles dans la description des jetons utilisateur, des images de profil et des noms d'utilisateur dans notre liste d'utilisateurs. Voici un exemple. Si notre objet keys ressemble à ceci :

```javascript
keys: {
  userToken: 'user_token',
  profileImage: 'profile_image',
  userName: 'user_name'
}
```

Alors notre tableau `users` doit décrire les jetons, les images de profil et les noms des utilisateurs avec les valeurs de l'objet `keys`.

Quels que soient les utilisateurs qui utiliseront votre application Robin, Robin nécessite un `userToken`, `profileImage` et un `userName` de leur part. Robin exige cela pour le nom d'affichage et pour identifier de manière unique chaque expéditeur et destinataire de message sur la plateforme.

```js
users: [
  {
    'user_token': 'ABCDEF098765GH',
    'profile_image': 'https://url-to-image',
    'user_name': 'Lecteur d\'article'
  }
]
```

# Étape 4 – Installer Robin dans votre application Nuxt

Maintenant que nous avons tout ce dont nous avons besoin, nous pouvons procéder à l'installation de Robin.

```
npm i robin-vue
// OU
yarn add robin-vue
```

# Étape 5 – Configurer le plugin Robin

Dans votre répertoire `plugins`, créez un fichier `robin.js` avec la configuration du plugin :

```javascript
import Vue from 'vue'
import RobinChat from 'robin-vue'
import 'robin-vue/dist/style.css'

Vue.use(RobinChat)
```

Notez que nous importons le CSS car le composant `RobinChat` n'inclut aucun CSS lui-même.

# Étape 6 – Enregistrer le plugin

La propriété `plugins` dans le fichier `nuxt.config.js` sert à informer notre application Nuxt des plugins qu'elle doit utiliser. Donc, si nous n'incluons pas notre plugin Robin là-bas, il ne sera pas disponible dans notre application.

```javascript
export default {
  // ...
  plugins: [
    { src: '~/plugins/robin.js', mode: 'client' }
  ]
}
```

# Étape 7 – Utiliser le plugin

Il ne nous reste plus qu'à inclure le composant `RobinChat` n'importe où dans notre application et à passer ces identifiants dont nous avons discuté précédemment en tant que props. 

Encore une fois, les identifiants sont :

* Clé API,
* Jeton utilisateur,
* Nom d'utilisateur,
* Utilisateurs, et
* Clés

Dans cette liste, ce que nous n'avons pas actuellement, ce sont notre jeton utilisateur et les jetons des utilisateurs de notre application. 

Rappelons que ces jetons sont généralement créés sur le serveur. Mais nous n'avons pas ce luxe. Nous pouvons donc aller de l'avant et les créer avec l'aide du [SDK JavaScript de Robin](https://www.npmjs.com/package/robin.io-js). Le SDK Vue que nous avons précédemment installé dépend de ce SDK JavaScript. Nous n'avons donc pas besoin de l'installer puisqu'il existe déjà dans notre application.

## Comment créer les jetons utilisateur

Nous pouvons aller de l'avant et créer les jetons dans la page où nous allons inclure l'interface utilisateur de chat. Puisque c'est à des fins d'apprentissage, nous pouvons aller de l'avant et créer des jetons pour 5 utilisateurs, nous y compris. Nous devons trouver des noms d'utilisateur pour chacun d'eux.

```javascript
<template>
  <!-- ... -->
</template>


<script>
export default {
  data () {
    return {
      users: [
        {
          user_token: '',
          profile_image: '',
          user_name: 'idorenyin'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'ayo'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'elvis'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'favour'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'enoch'
        }
      ],
    }
  }
}
</script>
```

Notez que les clés dans chaque objet utilisateur du tableau `users` doivent être définies dans l'objet `keys` que nous allons passer en tant que prop au composant Robin.

```javascript
keys: {
  userToken: 'user_token',
  profileImage: 'profile_image',
  userName: 'user_name'
},
```

Ensuite, nous utilisons la fonction `createUserToken()` du SDK pour créer les jetons après avoir créé une instance Robin, comme indiqué dans la [documentation de Robin](https://docs.robinapp.co/frontend-sdks/javascript/getting-started).

```javascript
<template>
  <!-- ... -->
</template>

<script>
import { Robin } from 'robin.io-js'

export default {
  data () {
    return {
      keys: {
        userToken: 'user_token',
        profileImage: 'profile_image',
        userName: 'user_name'
      },
      users: [
        // ...
      ]
    }
  },
  created () {
    this.createTokens()
  },
  methods: {
    async createTokens () {
      const robin = new Robin('API_KEY', true)
      for (let i = 0; i < this.users.length; i++) {
        await robin.createUserToken({
          meta_data: {
            username: this.users[i].user_name
          }
        }).then((res) => {
          this.users[i].user_token = res.data.user_token
        })
      }
    }
  }
}
</script>
```

## Comment utiliser les identifiants sur le composant RobinChat

Nous avons maintenant tout ce dont nous avons besoin pour afficher l'interface utilisateur de chat Robin sur notre application. Ouf !  
Nous pouvons maintenant utiliser les jetons et les autres identifiants.

```javascript
<template>
  <!-- ... -->
  <RobinChat
    v-if="tokensAreAvailable"
    :api-key="apiKey"
    :user-token="users[0].user_token"
    user-name="Idorenyin Udoh"
    :keys="keys"
    :users="users"
  />
</template>

<script>
import { Robin } from 'robin.io-js'

export default {
  data () {
    return {
      tokensAreAvailable: false,
      apiKey: 'API_KEY',
      keys: {
        userToken: 'user_token',
        profileImage: 'profile_image',
        userName: 'user_name'
      },
      users: [
        {
          user_token: '',
          profile_image: '',
          user_name: 'idorenyin'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'ayo'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'elvis'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'favour'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'enoch'
        }
      ]
    }
  },
  created () {
    this.createTokens()
  },
  methods: {
    async createTokens () {
      const robin = new Robin(this.apiKey, true)
      for (let i = 0; i < this.users.length; i++) {
        await robin.createUserToken({
          meta_data: {
            username: this.users[i].user_name
          }
        }).then((res) => {
          this.users[i].user_token = res.data.user_token
        })
      }
      this.tokensAreAvailable = true
    }
  }
}
</script>
```

Notez que nous n'affichons le composant `RobinChat` que lorsque tous les jetons des utilisateurs sont disponibles pour éviter les erreurs.

Voici à quoi ressemble le résultat :

![Image](https://paper-attachments.dropbox.com/s_8728EF96CF25BE6F7A46E3619EB658CA92CDD4D1E377FEC5C8707FC59B5068A6_1658311851926_Screenshot+2022-07-20+at+11.10.45.png)

L'application est disponible [ici](https://nuxt-chat-lmqlbq79p-idorenyinudoh.vercel.app/).

Notez que j'ai utilisé des jetons utilisateur précédemment créés pour cette application car vous ne pourriez pas voir les messages si des jetons sont créés à chaque fois que l'application se charge. Les jetons permanents sont ce qui rend les messages sur Robin persistants.

De plus, j'ai créé [une autre application](https://nuxt-chat-app-git-ayo-idorenyinudoh.vercel.app/) pour l'utilisateur Ayo. Vous pouvez également la consulter. De cette façon, vous pouvez tester la communication en temps réel entre Idorenyin et Ayo.

# Conclusion

Vous venez d'apprendre comment implémenter la communication en temps réel sur une application Nuxt avec Robin. 

La facilité d'intégration permet d'implémenter très rapidement un système de chat dans votre application et de vous concentrer sur sa construction/maintenance. 

Si vous veillez à créer les jetons de vos utilisateurs sur le serveur, alors l'implémentation de l'intégration sur le frontend ne sera pas trop difficile.

Bonne construction !