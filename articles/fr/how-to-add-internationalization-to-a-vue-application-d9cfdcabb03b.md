---
title: Comment ajouter l'internationalisation à une application Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T17:36:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-internationalization-to-a-vue-application-d9cfdcabb03b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nv9ljDdFOhR9AklvsB1rXQ.png
tags:
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Comment ajouter l'internationalisation à une application Vue
seo_desc: 'By Jennifer Bland


  Adding Internationalization to Vue

  ¡Hola! Bonjour. Ciao. 你好. Here is how you add internationalization to Vue.

  My company has plants in 37 countries. We write applications for the employees at
  these plants. Our application has to be...'
---

Par Jennifer Bland

![Image](https://cdn-media-1.freecodecamp.org/images/Vm6j99hQrd5cARRDX-j4sgKr9aauGEvWEiR7)
_Ajout de l'internationalisation à Vue_

¡Hola! Bonjour. Ciao. 你好. Voici comment ajouter l'internationalisation à Vue.

Mon entreprise possède des usines dans 37 pays. Nous écrivons des applications pour les employés de ces usines. Notre application doit être traduite dans leur langue maternelle. Vous pouvez facilement ajouter l'internationalisation à votre application Vue. Laissez-moi vous montrer comment ajouter l'internationalisation à l'application Vue par défaut.

#### Création de notre application

Nous allons créer une application en utilisant le CLI Vue. Si vous ne l'avez pas installé, vous pouvez l'installer avec cette commande :

```
npm install @vue/cli -g
```

Le drapeau `-g` installera le CLI Vue globalement. Maintenant que nous avons le CLI installé, nous pouvons créer une nouvelle application. Entrez cette commande pour créer l'application :

```
vue create vue-internationalization
```

Le CLI Vue vous invitera à choisir un préréglage. Vous avez la possibilité de sélectionner le préréglage par défaut ou de sélectionner manuellement les fonctionnalités. J'ai choisi `default`.

![Image](https://cdn-media-1.freecodecamp.org/images/iORkUx6USI5ZlTXcLXVMeAUym10Sk6lWCKAe)

Cela va créer une application Vue dans un dossier appelé `vue-internationalization` puisque c'est le nom que nous avons donné lors de la création. Maintenant, changez de répertoire avec cette commande :

```
cd vue-internationalization
```

Une fois dans le répertoire, vous devrez installer toutes les dépendances avec cette commande :

```
npm install
```

Pour vérifier que tout fonctionne correctement, entrez cette commande :

```
npm run serve
```

Maintenant, ouvrez votre navigateur à l'adresse localhost:8080 et vous devriez voir ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/mqDwiMYMoV2fLa4XVAXl5qG0gqifkB8BAjas)
_Application Vue par défaut_

Ensuite, nous allons fournir une traduction internationale pour cette application.

### Plugin Vue-i18n

Nous allons utiliser le plugin vue-i18n pour l'internationalisation. Ajoutons ce plugin à notre application. Si vous avez encore votre serveur en cours d'exécution, arrêtez-le. Ensuite, dans le terminal, entrez cette commande :

```
npm install vue-i18n --save
```

Puisque c'est un plugin, je vais le configurer en tant que tel. Créez un dossier appelé `plugins` dans votre dossier src. Créez un fichier appelé `i18n.js` à l'intérieur du dossier plugins.

Pour fournir l'internationalisation, vous devez dire à Vue d'utiliser le plugin vue-i18n et lui fournir un objet de messages. L'objet de messages contiendra les traductions pour chaque langue que votre application prend en charge.

La première étape consiste à dire à Vue d'utiliser le plugin. Dans le fichier `i18n.js`, entrez ce qui suit :

```js
import Vue from 'vue';
import VueI18n from 'vue-i18n';

Vue.use(VueI18n);
```

Maintenant, Vue sait utiliser notre plugin d'internationalisation. L'étape suivante consiste à créer les traductions pour chaque langue que nous prenons en charge. À des fins de démonstration, je vais ajouter seulement deux langues : l'anglais et l'espagnol. Une fois que vous comprenez comment cela fonctionne, il est très facile de continuer à ajouter de plus en plus de langues à votre application.

Pour ajouter des langues, nous devons créer un objet de messages. Les objets en JavaScript sont composés de paires clé-valeur. Les clés de l'objet de messages seront les langues que nous prenons en charge. Créons cela en utilisant l'anglais et l'espagnol pour nos langues prises en charge. Ajoutez le code suivant sous la ligne `Vue.use` dans le fichier `i18n.js`.

```js
const messages = {
    'en': {},
    'es': {}
};
```

Ensuite, nous devons créer un nouvel objet d'internationalisation et dire à Vue de l'utiliser. Après l'objet de messages, ajoutez le code suivant :

```js
const i18n = new VueI18n({
    locale: 'en', // définir la locale
    fallbackLocale: 'es', // définir la locale de secours
    messages, // définir les messages de locale
});
```

Lorsque nous créons notre objet d'internationalisation, nous devons lui indiquer la locale par défaut que nous allons afficher initialement. Au cas où il y aurait un problème pour afficher cette langue, nous pouvons définir une locale de secours. Ensuite, nous lui indiquons l'objet de messages qui contient nos traductions. La dernière ligne exporte cet objet.

Vue doit être informé d'utiliser l'internationalisation. Nous faisons cela dans le fichier `main.js`. Ouvrez le fichier `main.js`. Importez notre fichier d'internationalisation avec cette commande :

```
import i18n from '@/plugins/i18n';
```

> Note : si vous n'êtes pas familier avec l'utilisation du @ dans la ligne d'importation, par défaut Vue sait que cela pointe vers le répertoire src. Cela vous permet d'éviter d'essayer de faire des chemins relatifs vers le répertoire des plugins.

Nous devons dire à Vue de l'utiliser, donc nous ajoutons `i18n` à l'objet Vue. Voici à quoi devrait ressembler votre fichier `main.js` :

```js
import Vue from 'vue';
import App from './App.vue';
import i18n from '@/plugins/i18n';

Vue.config.productionTip = false;

new Vue({
    i18n,
    render: h => h(App),
}).$mount('#app');
```

#### Ajout des traductions internationales

Ouvrez le fichier `i18n.js`. Nous allons créer notre première traduction. Nous allons commencer par la phrase « Welcome to Your Vue.js App. » La traduction pour chaque langue dans l'objet de messages est un objet.

Juste un rappel qu'un objet est une paire clé-valeur. La clé est ce que nous allons utiliser et la valeur est la traduction de la phrase dans cette langue.

Alors laissez-moi vous montrer comment cela fonctionne avec l'anglais. Mettez à jour le fichier pour inclure ce qui suit :

```js
const messages = {
    'en': {
        welcomeMsg: 'Welcome to Your Vue.js App'
    },
    'es': {}
};
```

Maintenant, nous devons fournir une traduction espagnole pour cette phrase. Puisque je ne parle pas couramment l'espagnol, je vais utiliser Google Translate.

![Image](https://cdn-media-1.freecodecamp.org/images/KG1T2fyI3fhjicOlOXMKPTRuZ-C2Twhw79To)
_Google Translate_

Je vais copier la traduction espagnole que Google Translate fournit. Ensuite, je vais l'ajouter à la section espagnole. Chaque langue doit utiliser la même clé. Donc, notre objet de messages mis à jour ressemble maintenant à ceci :

```js
const messages = {
    'en': {
        welcomeMsg: 'Welcome to Your Vue.js App'
    },
    'es': {
        welcomeMsg: 'Bienvenido a tu aplicación Vue.js'
    }
};
```

Maintenant que nous avons cette traduction, nous devons remplacer le texte anglais dans notre application par défaut pour utiliser notre texte internationalisé. Ouvrez le fichier `App.vue`. Dans le template, il passe une prop appelée `msg` au composant HelloWorld. Nous voulons remplacer ce texte par notre texte internationalisé. Pour simplifier, je vais supprimer cette prop et placer le texte dans le composant HelloWorld.

Ouvrez le composant `HelloWorld`. Dans la balise `h1`, la prop msg est affichée. Remplaçons-la par le code suivant :

```vue
<h1>{{ $t('welcomeMsg') }}</h1>
```

Le $t spécifie que nous utilisons le plugin d'internationalisation. Le texte que nous voulons afficher est la valeur de la clé welcomeMsg dans notre objet de messages. Si vous avez arrêté votre serveur, vous pouvez le démarrer avec cette commande :

```
npm run serve
```

Ensuite, allez dans votre navigateur et vous verrez le texte internationalisé affiché.

#### Changer de langues

Nous voulons pouvoir voir le texte changer en espagnol si nous définissons notre locale en espagnol. La question est, comment faire cela ? La manière la plus simple est de fournir une liste déroulante qui montre les drapeaux des pays dont la langue est prise en charge dans l'application. Les utilisateurs peuvent sélectionner leur langue, ce qui entraîne l'affichage de tout le texte dans cette langue. Nous avons donc besoin d'un moyen de permettre aux utilisateurs de changer de langue.

Pour afficher les drapeaux dans une liste déroulante, nous pourrions utiliser un fichier graphique `.png`. Cela fonctionnerait clairement. Laissez-moi vous montrer une meilleure façon. Le package `vue-flag-icon` fournit une collection de tous les drapeaux de pays en SVG. Installons-le avec cette commande :

```
npm install vue-flag-icon --save
```

Maintenant que nous l'avons installé, nous devons dire à Vue de l'utiliser. Ouvrez le fichier main.js. Nous devons importer le package que nous venons d'installer et dire à Vue de l'utiliser. Votre fichier main.js devrait maintenant ressembler à ceci :

```vue
import Vue from 'vue';
import App from './App.vue';
import i18n from '@/plugins/i18n';
import FlagIcon from 'vue-flag-icon';

Vue.use(FlagIcon);
Vue.config.productionTip = false;

new Vue({
    i18n,
    render: h => h(App),
}).$mount('#app');
```

Ensuite, nous devons créer des boutons pour que l'utilisateur puisse sélectionner sa langue. Ouvrez le composant `App.vue`. Nous allons afficher un bouton pour les deux langues. L'utilisateur peut cliquer sur le bouton pour afficher le texte dans sa langue.

Dans cette démonstration, je ne prends en charge que deux langues. Dans une application réelle, vous prendrez probablement en charge beaucoup plus de langues. Dans ce cas, vous auriez un tableau de toutes les langues prises en charge. Faisons cela maintenant dans notre application pour que vous puissiez voir à quel point il est facile de transférer cela à une application plus grande.

Nous devons ajouter des données à notre script. Nous aurons une entrée appelée `languages` qui sera un tableau d'objets. L'objet contiendra un drapeau, une langue et un titre. Voici à quoi les données devraient ressembler :

```vue
data() {
    return {
        languages: [
            { flag: 'us', language: 'en', title: 'English' },
            { flag: 'es', language: 'es', title: 'Español' }
        ]
    };
}
```

Dans notre template, nous devons créer un bouton pour chaque langue dans notre tableau `languages`. Nous allons utiliser une directive `v-for` pour parcourir toutes les entrées et créer un bouton pour chacune. Voici le code que vous devez ajouter au template avant l'`img`.

```vue
<div>
    <button v-for="entry in languages" :key="entry.title" @click="changeLocale(entry.language)">
        <flag :iso="entry.flag" v-bind:squared=false /> {{entry.title}}
    </button>
</div>
```

Dans le code ci-dessus, nous parcourons toutes les entrées dans le tableau `languages`. À l'intérieur du bouton, nous affichons le drapeau du pays et le titre. Lorsque vous exécutez cela initialement, nous obtenons le style par défaut pour un bouton fourni par votre navigateur. Stylisons le bouton, donc ajoutez le CSS suivant dans la section style :

```css
button {
    padding: 15px;
    border: 1px solid green;
    font-size: 18px;
    margin: 15px;
}
```

Je fournis un remplissage autour du texte et je mets une bordure verte autour du bouton. La taille de la police rend le texte lisible à l'écran. La marge est là juste pour définir un espace entre les deux boutons ainsi qu'un espace entre les boutons et l'image.

Lorsque nous avons créé le bouton, nous lui avons dit d'appeler une méthode `changeLocale` si un utilisateur clique sur le bouton. Cette méthode changera la locale en fonction de la langue du bouton sur lequel l'utilisateur clique. Pour changer la locale, nous devons d'abord importer notre plugin i18n. Vous pouvez l'importer avec cette commande :

```js
import i18n from '@/plugins/i18n';
```

Maintenant, nous pouvons créer notre méthode `changeLocale`. Voici à quoi elle ressemble :

```js
methods: {
    changeLocale(locale) {
        i18n.locale = locale;
    }
}
```

Démarrez votre serveur. Vous verrez les deux boutons. Cliquez sur le bouton espagnol. Le message de bienvenue devrait instantanément changer pour l'espagnol.

![Image](https://cdn-media-1.freecodecamp.org/images/16tQPz1b-7mkBF1oqXqwqdhfe3YLaDaoT8mA)
_Texte changé en espagnol_

### Finalisation des traductions

Pour l'instant, nous n'avons traduit qu'un seul élément à l'écran. Nous pouvons répéter ce que nous avons fait pour le reste du texte sur la page. Ouvrez le fichier `i18n.js`. Voici mes traductions pour les titres de section sur la page.

```js
const messages = {
    'en': {
        welcomeMsg: 'Welcome to Your Vue.js App',
        guide: 'For a guide and recipes on how to configure / customize this project,',
        checkout: 'check out the',
        plugins: 'Installed CLI Plugins',
        links: 'Essential Links',
        ecosystem: 'Ecosystem'
    },
    'es': {
        welcomeMsg: 'Bienvenido a tu aplicación Vue.js',
        guide: 'Para una guía y recetas sobre cómo configurar / personalizar este proyecto,',
        checkout: 'revisar la',
        plugins: 'Plugins de CLI instalados',
        links: 'Enlaces esenciales',
        ecosystem: 'Ecosistema'
    }
};
```

Maintenant, nous devons mettre à jour le composant HelloWorld avec ces traductions. Voici le template traduit :

```vue
<template>
    <div class="hello">
        <h1>{{ $t('welcomeMsg') }}</h1>
        <p>
            {{ $t('guide') }}<br>
            {{ $t('checkout') }}
            <a href="https://cli.vuejs.org" target="_blank" rel="noopener">documentation vue-cli</a>.
        </p>
        <h3>{{ $t('plugins') }}</h3>
        <ul>
            <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank"
                   rel="noopener">babel</a></li>
            <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank"
                   rel="noopener">eslint</a></li>
        </ul>
        <h3>{{ $t('links') }}</h3>
        <ul>
            <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
            <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
            <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
            <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
            <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
        </ul>
        <h3>{{ $t('ecosystem') }}</h3>
        <ul>
            <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
            <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
            <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank"
                   rel="noopener">vue-devtools</a></li>
            <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
            <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
        </ul>
    </div>
</template>
```

Démarrez votre serveur et visualisez votre application dans le navigateur. Cliquez entre les deux boutons. Vous verrez le texte se traduire automatiquement dans la langue sur laquelle vous avez cliqué. Regardez ce gif.

![Image](https://cdn-media-1.freecodecamp.org/images/o2hjFnLCaPAaTEmCoaWvJBvXWIv0iFeXYhj5)
_Changement de langues dans Vue_

### Obtenez le code

J'ai le code final [disponible sur GitHub](https://github.com/ratracegrad/vue-internationalization). Aidez-moi et **étoilez le dépôt** lorsque vous obtenez le code.

### Conclusion

Si votre application est utilisée par des clients du monde entier, vous devrez ajouter l'internationalisation. Pour ajouter la prise en charge de plusieurs langues, vous devez installer le plugin `Vue-i18n`. Ensuite, traduisez le texte de votre application pour toutes les langues que vous prenez en charge. La dernière étape consiste à fournir un moyen pour les utilisateurs de basculer entre différentes langues.

J'espère que vous avez apprécié cet article. Merci d'avoir lu !