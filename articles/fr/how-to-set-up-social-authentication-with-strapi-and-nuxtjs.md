---
title: Comment configurer l'authentification sociale avec Strapi et Nuxt.js
subtitle: ''
author: Ashimi0x
co_authors: []
series: null
date: '2025-01-14T15:22:52.761Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-social-authentication-with-strapi-and-nuxtjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736865891246/8be87fdb-c57b-4ae1-91ea-00b6dbffe09b.png
tags:
- name: Strapi
  slug: strapi
- name: social authentication
  slug: social-authentication
- name: Nuxt
  slug: nuxt
seo_title: Comment configurer l'authentification sociale avec Strapi et Nuxt.js
seo_desc: 'Enhancing security is a critical aspect of every development process. But
  it’s crucial to make your apps accessible for users signing up for the application.

  So, creating a seamless experience for users while they sign up and maintaining
  security thr...'
---

Améliorer la sécurité est un aspect critique de chaque processus de développement. Mais il est crucial de rendre vos applications accessibles pour les utilisateurs qui s'inscrivent à l'application.

Ainsi, créer une expérience fluide pour les utilisateurs lors de leur inscription et maintenir la sécurité tout au long du processus est essentiel. C'est pourquoi de nombreux développeurs web adoptent aujourd'hui l'authentification sociale.

Dans cet article, je vais vous guider à travers la configuration de l'authentification sociale sur un projet Strapi en utilisant GitHub. Ensuite, nous l'intégrerons dans une configuration simple de Nuxt.js.

### Voici ce que nous allons couvrir :

* [Qu'est-ce que l'authentification sociale ?](#heading-questce-que-lauthentification-sociale)
    
    * [Qu'est-ce que Strapi ?](#heading-questce-que-strapi)
        
    * [Qu'est-ce que Nuxt.js ?](#heading-questce-que-nuxtjs)
        
    * [Que allez-vous apprendre dans ce guide ?](#heading-que-allez-vous-apprendre-dans-ce-guide)
        
* [Prérequis](#heading-prerequis)
    
* [Comment configurer Strapi pour l'authentification sociale](#heading-comment-configurer-strapi-pour-lauthentification-sociale)
    
    * [Comment configurer les fournisseurs de Strapi](#heading-comment-configurer-les-fournisseurs-de-strapi)
        
    * [Comment créer l'application OAuth de GitHub](#heading-comment-creer-lapplication-oauth-de-github)
        
    * [Comment connecter l'application OAuth GitHub au fournisseur sur Strapi](#heading-comment-connecter-lapplication-oauth-github-au-fournisseur-sur-strapi)
        
    * [Comment tester l'API Strapi](#heading-comment-tester-lapi-strapi)
        
* [Comment configurer Nuxt.js pour l'authentification sociale](#heading-comment-configurer-nuxtjs-pour-lauthentification-sociale)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que l'authentification sociale ?

L'authentification sociale utilise des comptes de médias sociaux familiers afin que les utilisateurs n'aient pas besoin de se souvenir d'une autre combinaison nom d'utilisateur-mot de passe. Au lieu de créer un nom d'utilisateur et un mot de passe uniques pour chaque site web, les utilisateurs peuvent se connecter via leurs comptes sur des plateformes populaires comme Google, Facebook, Twitter ou GitHub.

Vous pouvez configurer cela en utilisant OAuth. C'est un protocole largement adopté qui permet aux sites web d'accéder à des données utilisateur limitées sans exposer des informations d'identification sensibles. Il aide également à éliminer les barrières dans le processus d'inscription ou de connexion, réduisant les chances que les gens abandonnent le site. Les utilisateurs peuvent rapidement se connecter avec quelques clics, rendant l'intégration plus fluide et réduisant la fatigue des formulaires.

L'authentification sociale améliore également la sécurité globale de l'application en déchargeant certaines responsabilités vers des fournisseurs de confiance qui emploient déjà des protocoles de sécurité solides.

### **Qu'est-ce que Strapi ?**

Strapi est un système de gestion de contenu (CMS) open-source sans tête construit avec Node.js. Il permet aux développeurs de gérer et de livrer du contenu via des API (REST ou GraphQL) tout en fournissant une plateforme personnalisable et extensible.

Strapi est populaire pour sa flexibilité (il fonctionne avec divers frameworks front-end) et son système de plugins, ce qui facilite l'ajout de fonctionnalités comme l'authentification sociale.

### **Qu'est-ce que Nuxt.js ?**

Nuxt.js est un framework Vue.js puissant conçu pour construire des applications web modernes avec rendu côté serveur (SSR), génération de sites statiques et routage côté client puissant. Vous pouvez l'utiliser pour créer des applications haute performance, SEO-friendly et scalables.

La structure modulaire de Nuxt et sa facilité d'intégration avec les API en font un choix idéal pour construire des applications front-end complexes, telles que celles nécessitant une authentification sociale.

### **Que allez-vous apprendre dans ce guide ?**

Ce guide vous guidera à travers la mise en œuvre de l'authentification sociale en utilisant **Strapi v5** et **Nuxt.js**. Vous apprendrez comment :

* Configurer OAuth pour les connexions sociales
    
* Configurer Strapi pour gérer l'authentification sociale
    
* Intégrer la fonctionnalité de manière fluide dans un front-end Nuxt.js existant
    

## Prérequis

Avant de plonger dans le tutoriel, assurez-vous d'avoir les connaissances et outils de base nécessaires :

1. **Connaissance de base de Node.js, Vue.js et Nuxt.js** : La familiarité avec ces technologies est cruciale, car Strapi est construit sur Node.js, et Nuxt.js est un framework basé sur Vue.js. Pour naviguer à travers le processus d'intégration, vous aurez besoin d'une compréhension générale de la manière dont Node.js gère la logique côté serveur et comment Vue.js fonctionne sur le front-end.
    
2. **Familiarité avec les API REST ou GraphQL (optionnel mais utile)** : Strapi fournit à la fois des API REST et GraphQL pour gérer les données et l'authentification. Bien que ce guide se concentrera principalement sur les API REST pour l'authentification sociale, savoir comment fonctionnent les API et comment faire des requêtes HTTP est utile. Si vous êtes familier avec GraphQL, vous pourriez optionnellement l'utiliser pour des requêtes et une gestion de l'authentification plus complexes.
    
3. **Comptes de développeur de fournisseurs sociaux** : Pour intégrer l'authentification sociale, vous devez créer des comptes de développeur sur les plateformes sociales que vous souhaitez supporter (comme Google, Facebook ou GitHub). Vous aurez besoin de clés API ou d'ID client de chaque fournisseur. Dans ce tutoriel, vous apprendrez à utiliser GitHub pour cette fonctionnalité.
    

## Comment configurer Strapi pour l'authentification sociale

Si vous n'avez pas encore créé de projet Strapi, commençons par en générer un nouveau.

Vous pouvez créer un nouveau projet Strapi avec **Yarn** (recommandé). Exécutez la commande suivante dans votre terminal :

`yarn create strapi-app@latest my-project`

Ou avec **npm** :

`npx create-strapi-app@latest my-project`

Répondez "yes" à toutes les invites :

![Interface d'installation de Strapi sur Virtual Studio Code](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729719988851_Screenshot+2024-10-23+at+22.23.44.png align="left")

Vous devriez maintenant avoir une nouvelle application Strapi 5 avec une base de données SQLite par défaut. Pour la lancer en mode développement, ouvrez votre projet et exécutez :

`yarn run develop`

![Interface du terminal de VS Code pour un projet Strapi en cours d'exécution](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729722404206_Screenshot+2024-10-23+at+23.26.03.png align="left")

Une fois le projet lancé, Strapi se lancera automatiquement dans votre navigateur à l'adresse http://localhost:1337/admin. La première étape consiste à créer un **compte administrateur** pour accéder au panneau d'administration de Strapi :

![Interface d'enregistrement de l'administrateur Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729722491173_Screenshot+2024-10-23+at+23.28.01.png align="left")

Remplissez les champs requis et créez votre utilisateur administrateur. Une fois connecté, vous aurez accès à l'interface complète d'administration de Strapi, où vous pourrez gérer les types de contenu, les plugins et les paramètres :

![Page d'accueil de Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729722679829_Screenshot+2024-10-23+at+23.28.50.png align="left")

### Comment configurer les fournisseurs de Strapi

Pour l'authentification sociale, le plugin Utilisateurs & Permissions de Strapi est essentiel et est déjà préinstallé avec la configuration par défaut. Cliquez sur Paramètres dans le panneau d'administration de Strapi :

![Aperçu de la page des paramètres de Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729722965788_Screenshot+2024-10-23+at+23.35.39.png align="left")

Faites défiler vers le bas et cliquez sur Fournisseurs dans la section du plugin Utilisateurs & Permissions :

![La page des fournisseurs de Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729723008188_Screenshot+2024-10-23+at+23.36.35.png align="left")

Vous verrez cette liste de fournisseurs parmi lesquels choisir. Pour cet article, sélectionnez GitHub en cliquant sur l'icône du stylo à droite :

![Modification des paramètres du fournisseur GitHub](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729723164437_Screenshot+2024-10-23+at+23.39.11.png align="left")

Par défaut, il est défini sur "false", basculez-le sur True. Prenez note de l'URL de redirection et copiez-la.

### Comment créer l'application OAuth de GitHub

Dans un autre onglet de votre navigateur, connectez-vous à votre compte GitHub et cliquez sur vos paramètres :

![Page d'exploration de GitHub](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729716332697_Screenshot+2024-10-23+at+21.45.06.png align="left")

Puis naviguez vers vos paramètres de développeur :

![Page des paramètres du profil](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729716365753_Screenshot+2024-10-23+at+21.45.18.png align="left")

Sélectionnez OAuth Apps et Nouvelle application OAuth :

![Page des paramètres du développeur](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729716462052_Screenshot+2024-10-23+at+21.46.56.png align="left")

Comme vous pouvez le voir ci-dessous, l'URL de redirection sera collée en tant qu'URL de rappel d'autorisation et l'URL de la page d'accueil sera l'URL de votre application.

![Page d'enregistrement de l'application OAuth](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729716551370_Screenshot+2024-10-23+at+21.48.51.png align="left")

Allez-y et cliquez sur "Register application", et vous verrez votre Client ID. Maintenant, vous devez générer votre Client Secret :

![Application GitHub créée avec succès.](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729723880674_Screenshot+2024-10-23+at+23.49.35.png align="left")

### Comment connecter l'application OAuth GitHub au fournisseur sur Strapi

Une fois votre Client Secret généré, mettez à jour l'application et retournez à votre application Strapi pour les saisir. L'URL de redirection vers votre application front-end sera [http://localhost:3000/connect/github](http://localhost:3000/connect/github).

![Ajout du fournisseur GitHub à Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729723954537_Screenshot+2024-10-23+at+23.52.13.png align="left")

Vous pouvez tout sauvegarder maintenant, et votre fournisseur GitHub devrait être activé.

![Interface du fournisseur Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729724039006_Screenshot+2024-10-23+at+23.53.23.png align="left")

Vous pouvez configurer autant de fournisseurs que vous le souhaitez.

Pour permettre aux utilisateurs de s'authentifier avec des connexions sociales, vous devez mettre à jour le rôle public par défaut dans Strapi.

Cliquez sur Rôles juste au-dessus des Fournisseurs :

![Interface Strapi pour les rôles : Authentifié et Public](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729724464559_Screenshot+2024-10-24+at+00.00.46.png align="left")

Sélectionnez le rôle Public et assurez-vous que les permissions de connexion et de rappel sont activées. Elles sont déjà activées par défaut dans Strapi 5.

![Interface du rôle public de Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729724599165_Screenshot+2024-10-24+at+00.02.09.png align="left")

Cliquez sur Sauvegarder après avoir mis à jour les permissions. À ce stade, vous avez configuré les fournisseurs d'authentification sociale nécessaires. Avant de procéder à l'intégration de Nuxt.js, vous pouvez le tester en faisant une requête API à l'aide d'un outil comme Postman.

### Comment tester l'API Strapi

Envoyez une requête GET à http://localhost:1337//api/connect/github/.

![Interface de Postman pour tester les API.](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729725634296_Screenshot+2024-10-24+at+00.20.16.png align="left")

Vous remarquerez dans la console qu'il atteint un client de connexion GitHub. Copiez l'URL complète et collez-la dans votre navigateur. Vous devriez voir une interface comme celle-ci :

![Interface pour autoriser Strapi](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729725737744_Screenshot+2024-10-24+at+00.22.04.png align="left")

Si vous avez obtenu cela, félicitations ! Vous pouvez maintenant passer à la configuration de votre application front-end Nuxt.Js.

## Comment configurer Nuxt.js pour l'authentification sociale

Dans cette section, vous apprendrez à configurer le **flux d'authentification** entre Nuxt.js et Strapi, à gérer les redirections OAuth et à afficher un bouton de connexion pour que les utilisateurs puissent s'authentifier.

Tout d'abord, vous devrez installer Nuxt.js en exécutant l'une de ces commandes :

`yarn create nuxt-app <project-name> //en utilisant yarn`

`npx create-nuxt-app <project-name> //en utilisant npx`

`npm init nuxt-app <project-name> //en utilisant npm`

Visitez la documentation de Nuxt.js si vous avez besoin d'un rappel.

![Interface de VS code pour l'installation de NUXT](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729732718758_Screenshot+2024-10-24+at+01.52.37.png align="left")

Ouvrez votre projet et exécutez `npm run dev` pour le démarrer :

![Interface pour un projet Nuxt en cours d'exécution.](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729734102247_Screenshot+2024-10-24+at+02.40.17.png align="left")

Une fois lancé, visitez [https://localhost:3000](https://localhost:3000) sur votre navigateur et vous devriez voir une page Nuxt qui ressemble à ceci :

![Interface de l'application Nuxt sur le navigateur.](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1729734185176_Screenshot+2024-10-24+at+02.42.51.png align="left")

Dans votre éditeur de code, supprimez le fichier `Tutorial.vue` dans le dossier des composants et allez dans `index.vue` dans le dossier des pages. Là, vous voudrez ajouter ce qui suit :

```javascript
<template>
<div

 
 class="min-h-screen flex justify-center items-center text-center mx-auto sm:pl-24 bg-yellow-200"

 >

 
 <div class="w-1/2 sm:text-left sm:m-5">


 
 
 <div>


 
 
 
 <h1


 
 
 
 
 class="text-3xl sm:text-6xl font-black sm:pr-10 leading-tight text-blue-900"


 
 
 
 >


 
 
 
 
 Bienvenue


 
 
 
 </h1>


 
 
 </div>


 
 
 <div class="links">


 
 
 
 <NuxtLink to="/login" class="button--blue shadow-xl"> Connexion </NuxtLink>


 
 
 </div>


 
 </div>


 
 <div class="w-1/2 hidden sm:block">


 
 </div>


 </div>

</template>

<script>

export default {}

</script>

<style>

/* Sample apply at-rules with Tailwind CSS

.container {

@apply min-h-screen flex justify-center items-center text-center mx-auto;

}

*/

.container {


 margin: 0 auto;


 min-height: 100vh;


 display: flex;


 justify-content: center;


 align-items: center;


 text-align: center;

}

.title {


 font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,


 
 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;


 display: block;


 font-weight: 300;


 font-size: 100px;


 color: #35495e;


 letter-spacing: 1px;

}

.subtitle {


 font-weight: 300;


 font-size: 42px;


 color: #526488;


 word-spacing: 5px;


 padding-bottom: 15px;

}

.links {


 padding-top: 15px;

}</style>
```

Ce code vous fournit une simple page d'accueil et un lien vers la page de connexion qui mène actuellement à une page 404. Dans votre dossier de pages, créez `login.vue` et ajoutez le code suivant :

```javascript
<template>
<div


 
 
 class="min-h-screen flex justify-center items-center text-center mx-auto sm:pl-24 bg-yellow-200"


 
 >


 
 
 <div class="w-1/2 hidden sm:block m-5 p-6">


 
 
 
 <img src="" />


 
 
 </div>


 
 
 <div class="sm:w-1/2 w-4/5">


 
 
 
 <h2 class="m-5 font-black text-3xl">Connexion sociale</h2>


 
 
 
 <div class="shadow-xl bg-white p-10">


 
 
 
 
 <a


 
 
 
 
 
 href="http://localhost:1337/api/connect/github"


 
 
 
 
 
 class="cursor-pointer m-3 button--blue shadow-xl"


 
 
 
 
 >GitHub 
 
 
 
 
</a>


 
 
 
 </div>


 
 
 </div>


 
 </div>


 </template>


 <script>


 export default {}


 </script>


 <style lang="scss" scoped></style>
```

Aux lignes 11 - 14, l'utilisateur peut cliquer sur le lien et avoir la logique de connexion exécutée. Mais vous devez vous assurer que Nuxt peut gérer les redirections.  
  
Dans votre dossier de pages, créez un dossier appelé `connect`, puis à l'intérieur de celui-ci un fichier nommé `_provider.vue`, et ajoutez le code suivant pour gérer la fonction de rappel :

```javascript
<template>
<div>


 
 <h1>page utilisateur</h1>


 </div>

</template>

<script>


export default {


 data() {


 
 return {


 
 
 provider: this.$route.params.provider,


 
 
 access_token: this.$route.query.access_token,


 
 }


 },


 async mounted() {


 
 const res = await this.$axios.$get(


 
 
 /auth/${this.provider}/callback?access_token=${this.access_token}


 
 )


 




 
 const { jwt, user } = res


 
 // stocker le jwt et l'objet user dans localStorage


 
 this.$auth.$storage.setUniversal('jwt', jwt)


 
 this.$auth.$storage.setUniversal('user', { username: user.username, id: user.id, email: user.email })



 
 this.$router.push(`/users/${user.id}`)


 },

}

</script>

<style lang="scss" scoped></style>
```

Jusqu'à présent, votre structure de fichiers/dossiers devrait ressembler à ceci :

![Structure de fichiers Nuxt sur VScode](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1730069360059_Screen+Shot+2024-10-27+at+11.47.45+PM.png align="left")

Le code dans `_provider.vue` gère les redirections depuis le backend Strapi. Nuxt.js a un modèle de routage qui tire parti de /connect/\*provider où, dans ce cas, le fournisseur est GitHub.

Il obtient un jeton d'accès qui est stocké sous `access_token`, puis fait un appel API au backend dans la méthode de cycle de vie mounted. Cela retourne une réponse qui contient l'utilisateur et un JWT. Il stocke l'utilisateur et le JWT dans les cookies et le localStorage en utilisant un package appelé [@nuxtjs/auth-next](https://auth.nuxtjs.org/), puis redirige l'utilisateur vers la page de compte utilisateur.

Vous devrez installer le module @nuxtjs/auth-next en utilisant la commande suivante :

`npm install @nuxtjs/auth-next //en utilisant npm`

Ou avec yarn :

`yarn add @nuxtjs/auth-next //en utilisant yarn`

Après l'installation, ouvrez votre fichier nuxt.config.js et configurez les modules Auth :

```javascript
export default {
modules: [

 
'@nuxtjs/auth-next',

],
```

Ensuite, vous aurez besoin des packages [@nuxtjs/axios](https://axios.nuxtjs.org/) et [@nuxtjs/strapi](https://strapi.nuxtjs.org/) pour récupérer des données depuis le backend. [@nuxtjs/axios](https://axios.nuxtjs.org/) est déjà intégré lors de l'installation de Nuxt, mais vous devez définir votre baseurl.

Ouvrez votre fichier nuxt.config.js et ajoutez les lignes de code suivantes :

```javascript
// Configuration du module Axios : https://go.nuxtjs.dev/config-axios
axios: {

 
 baseURL: 'http://localhost:1337'
},
```

Puis installez [@nuxtjs/strapi](https://strapi.nuxtjs.org/) en utilisant la commande suivante :

`yarn add @nuxtjs/strapi //en utilisant yarn`

Ou :

`npm install @nuxtjs/strapi //en utilisant npm`

Remplacez le contenu de votre fichier nuxt.config.js par les lignes de code suivantes :

```javascript
export default {
// En-têtes globaux de la page : https://go.nuxtjs.dev/config-head


 head: {


 
 title: 'nuxtstrapi',


 
 htmlAttrs: {


 
 
 lang: 'en'


 
 },


 
 meta: [


 
 
 { charset: 'utf-8' },


 
 
 { name: 'viewport', content: 'width=device-width, initial-scale=1' },


 
 
 { hid: 'description', name: 'description', content: '' },


 
 
 { name: 'format-detection', content: 'telephone=no' }


 
 ],


 
 link: [


 
 
 { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }


 
 ]


 },


 // CSS global : https://go.nuxtjs.dev/config-css


 css: [


 ],


 // Plugins à exécuter avant le rendu de la page : https://go.nuxtjs.dev/config-plugins


 plugins: [


 ],


 // Import automatique des composants : https://go.nuxtjs.dev/config-components


 components: true,


 // Modules pour le développement et la construction (recommandé) : https://go.nuxtjs.dev/config-modules


 buildModules: [


 
 // https://go.nuxtjs.dev/typescript


 
 '@nuxt/typescript-build',


 ],


 // Modules : https://go.nuxtjs.dev/config-modules


 modules: [


 
 '@nuxtjs/auth-next',


 
 '@nuxtjs/axios',


 
 '@nuxtjs/strapi'


 ],


 axios: {


 
 baseURL: 'http://localhost:1337'


 },


 strapi: {


 
 entities: [ "articles', 'users' ],


 
 url: 'http://localhost:1337'

},


 // Configuration de la construction : https://go.nuxtjs.dev/config-build


 build: {


 }

}
```

Exécutez à la fois votre front-end et votre application Strapi pour tester l'authentification de connexion. Lorsque vous allez dans votre admin Strapi et vérifiez Utilisateur sous Content Manager, vous devriez voir le nouvel utilisateur authentifié.

![Interface du Content Manager sur Strapi montrant les utilisateurs](https://paper-attachments.dropboxusercontent.com/s_604FB5A9DF1492F56A770C5B36ABD7454099B52858C205A9399E3B1409CA50D8_1730072300480_Screen+Shot+2024-10-28+at+12.36.40+AM.png align="left")

## **Conclusion**

À ce stade, vous avez configuré avec succès votre application Strapi avec l'authentification sociale. Maintenant, vous pouvez ajouter autant de fournisseurs que vous le souhaitez et personnaliser vos applications pour répondre à vos besoins.

Merci d'avoir lu !