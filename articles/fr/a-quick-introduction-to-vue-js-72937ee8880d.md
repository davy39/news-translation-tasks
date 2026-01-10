---
title: Une introduction rapide à Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T15:30:55.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-vue-js-72937ee8880d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*RqZwiPYCVDIz5bLA
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Une introduction rapide à Vue.js
seo_desc: 'By Aditya Sridhar

  Are you interested in Front End Development?

  If so, then this post is for you!

  To get started with Vue.js, you need to know HTML, CSS, JavaScript, rocket science,
  nuclear physics, quantum theory etc…

  Hmm ?…

  Well, not really. Just HT...'
---

Par Aditya Sridhar

Êtes-vous intéressé par le développement Front End ?

Si c'est le cas, alors cet article est pour vous !

Pour commencer avec Vue.js, vous devez connaître HTML, CSS, JavaScript, la science des fusées, la physique nucléaire, la théorie quantique, etc...

Hmm ?...

Eh bien, pas vraiment. Juste **HTML, CSS et JavaScript** suffisent pour commencer avec Vue.js.

Cet article expliquera comment créer facilement une application simple avec Vue.js et expliquera la structure des dossiers de l'application créée. De plus, nous allons créer un composant simple avec Vue.js.

Alors, commençons.

### Prérequis

#### Installer Node.js si ce n'est pas déjà fait

Vous avez besoin de Node.js, car les bibliothèques nécessaires pour Vue sont téléchargées en utilisant le gestionnaire de paquets node (npm). Référez-vous à [https://nodejs.org/en/](https://nodejs.org/en/) pour installer Node.js.

#### Installer Vue CLI

Installez Vue CLI en utilisant la commande suivante :

```bash
npm install -g @vue/cli
```

Vue CLI aide à créer un projet Vue.js facilement. Bien qu'il soit appelé un CLI, il dispose également d'une interface utilisateur pour créer le projet, que je vais couvrir ci-dessous.

### Créer le Projet

Tapez la commande suivante dans l'invite de commande :

```bash
vue ui
```

Cela ouvrira l'écran suivant dans le navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/rfgbX3M9aMopUeCZRs8WwtzFP48KYi6RBBrF)

Cliquez sur **Créer**. Ensuite, entrez la destination où le projet doit être créé.

![Image](https://cdn-media-1.freecodecamp.org/images/Xb15ogPO7H-Jsc5FBMuEBnuTQorapmb-l-3i)

Ensuite, cliquez sur **Créer un nouveau projet ici.**

![Image](https://cdn-media-1.freecodecamp.org/images/fnBTkAXVu6hnbB6pOHAqJmJMEfEy6wIybudU)

Cela ouvrira l'écran suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1mj4fs5LmCW3pPZcfAiPUoEhH4hWontbKW1h)

Entrez le dossier du projet comme **sample-vue-app** et cliquez sur **Suivant.**

Dans l'écran suivant, sélectionnez **default preset**, comme montré dans l'image ci-dessous. Pour cet article, **default-preset** est le plus simple pour commencer.

![Image](https://cdn-media-1.freecodecamp.org/images/ur0DriId-ztQjrIpQRET7Bp-NkXoET9Auv87)

Enfin, cliquez sur **Créer le Projet**

Afin de tester si le projet est bien configuré, allez dans le dossier du projet et démarrez l'application en utilisant les commandes suivantes :

```bash
cd sample-vue-app
npm run serve
```

L'application s'exécute sur **localhost:8080**. L'image ci-dessous montre comment l'application apparaît dans le navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/tW0nCLS-biGCrqfJDhZxb2V7qTIt1UPphIFs)

Félicitations, vous avez créé votre premier projet Vue.js !

Mais attendez une minute, le projet a de nombreux fichiers et dossiers qui ont été créés automatiquement.

**Est-il vraiment nécessaire de savoir ce que ces fichiers signifient ?**

Les connaître aidera définitivement lorsque le code se comporte de manière étrange, ce qui arrive souvent dans le monde du développement.

### Structure des dossiers de l'application

![Image](https://cdn-media-1.freecodecamp.org/images/EzwWJBGY-Sd2mZipUtkt1D1GsA3L5sr-aB8d)

1. **package.json** : Ce fichier contient toutes les dépendances node.
2. **public/index.html** : C'est le premier fichier qui se charge lorsque l'application démarre. De plus, ce fichier contient le snippet de code suivant `<div id="app"></div>`. Tous les composants sont chargés dans ce **div** avec l'id app.
3. **src/main.js** : C'est le fichier où l'instance Vue est créée. Ce fichier contient le snippet de code suivant `new Vue({ render: h => h(App)}).$mount('#app')`. Ce snippet indique que le composant App doit être chargé dans un élément avec l'**id** app (qui est l'élément div).
4. **src/App.vue** : Ce fichier correspond au composant **App** qui agit comme un conteneur pour tous les autres composants. Il a un **template** pour le code **HTML**, il a un **script** pour le code **JavaScript**, et il a un **style** pour le **CSS**.
5. **src/components** : C'est ici que tous les composants que vous développez seront stockés. Tous les composants auront des balises template, script et style pour le code HTML, JavaScript et CSS respectivement.
6. **dist** : C'est le dossier où les fichiers compilés sont stockés. Pour obtenir ce dossier, exécutez la commande `npm run build`. Lorsque cette commande est exécutée, le code est minifié et bundlé et stocké dans le dossier dist. Le code de ce dossier est généralement déployé en production.

### Créer votre premier composant

Créez un fichier appelé **First.vue** dans **src/components**. Ce fichier contiendra HTML, JavaScript et CSS. Ajoutons-les un par un. Tout le code de cette section appartient au fichier **First.vue**. **First.vue** sera notre **composant Vue**

#### CSS

```html
<style scoped>
.demo {
    background-color: cyan;
}
</style>
```

C'est du CSS basique. Le paramètre **scoped** dans `<style scoped>` signifie que le CSS s'applique uniquement à ce composant.

#### JavaScript

```html
<script>
export default {
    name: 'First',
    props: {
    msg: String
    }
}
</script>
```

Le paramètre **name** indique le nom du composant qui est **First**.

Le paramètre **props** indique l'**entrée** de ce composant. Ici, nous aurons une entrée appelée **msg** qui est de type **String**.

#### HTML

```html
<template>
    <div class="demo">
    <h1>{{ msg }}</h1>
    </div>
</template>
```

`{{msg}}` est la manière dont le paramètre d'entrée du composant **Vue** peut être accessible dans le code **HTML**.

#### Code complet pour le premier composant

Voici le contenu du fichier **First.vue** :

```html
<template>
    <div class="demo">
    <h1>{{ msg }}</h1>
    </div>
</template>

<script>
export default {
    name: 'First',
    props: {
    msg: String
    }
}
</script>

<style scoped>
.demo {
    background-color: cyan;
}
</style>
```

Super, le composant est maintenant créé ! 🎉

Exécutez l'application maintenant en utilisant `npm run serve` et vous verrez l'écran suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/L4i403i-y4N4Po5arAH42K7PbJGt1U9OsZH1)

Attendez une minute, n'est-ce pas la même sortie qu'avant ? Où est le composant que nous venons de créer ?

Le problème est que nous avons créé le composant mais que nous ne l'avons jamais utilisé nulle part. Utilisons maintenant ce composant.

### Utiliser le composant

Ajoutons ce composant au composant principal **App**. Voici le code mis à jour pour **App.vue** :

```html
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <First msg="First Component"/>
  </div>
</template>
<script>
import HelloWorld from './components/HelloWorld.vue'
import First from './components/First.vue'
export default {
  name: 'app',
  components: {
    First
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

1. **First**, le composant doit être importé dans le composant **App**. Cela se fait avec la commande `import First from './components/First.vue'`
2. Ensuite, en JavaScript, nous devons mentionner que le composant **App** utilisera le composant **First**. Cela se fait par le snippet de code `components: {First}`
3. Enfin, nous devons utiliser le composant **First** dans le composant **App**. Cela se fait dans le template HTML en utilisant le snippet de code `<First msg="First Component"/>`
4. Ici, **msg** est le paramètre d'entrée du composant **First** et la **valeur de msg** est envoyée depuis le composant **App**

Maintenant, exécutez l'application en utilisant `npm run serve` et vous verrez la sortie suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/J-YsiOP4ZoY4WxlEVjaJwAvHeRt4PzFKQSyB)

### Code

[Cliquez ici](https://github.com/aditya-sridhar/vuejs-blog-demo-part1) pour obtenir le code montré ici depuis le dépôt GitHub. Le dépôt GitHub contient les instructions pour cloner et exécuter le code.

[Cliquez ici](https://aditya-sridhar.github.io/vuejs-blog-demo-part1/) pour voir à quoi ressemble l'application. Elle a été déployée en utilisant GitHub Pages.

### Félicitations 🎉

Vous avez maintenant réussi à construire votre première application Vue.js. Vous avez également appris à créer un composant très simple. Dans mon prochain article sur Vue.js, je couvrirai plus de concepts. Restez à l'écoute !

### **Références**

Vue.js : [https://vuejs.org/v2/guide/](https://vuejs.org/v2/guide/)

Vue CLI : [https://cli.vuejs.org/guide/](https://cli.vuejs.org/guide/)

### À propos de l'auteur

J'aime la technologie et je suis les avancées technologiques. J'aime aussi aider les autres avec les connaissances que j'ai dans le domaine de la technologie.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

### Autres articles de moi

[Un guide rapide pour vous aider à comprendre et créer des applications Angular 6](https://medium.freecodecamp.org/quick-guide-to-understanding-and-creating-angular-6-apps-2f491dffca1c)

[Un guide rapide pour vous aider à comprendre et créer des applications ReactJS](https://medium.freecodecamp.org/quick-guide-to-understanding-and-creating-reactjs-apps-8457ee8f7123)