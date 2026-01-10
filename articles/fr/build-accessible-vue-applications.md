---
title: Comment créer des applications Vue accessibles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-08T16:23:19.000Z'
originalURL: https://freecodecamp.org/news/build-accessible-vue-applications
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Article-Poster-.png
tags:
- name: Accessibility
  slug: accessibility
- name: vue
  slug: vue
seo_title: Comment créer des applications Vue accessibles
seo_desc: "By Abiola Farounbi\nDeveloping web pages used to involve writing HTML,\
  \ CSS, and a little scripting code like JavaScript for functionality. \nBut over\
  \ time, we've developed new and more advanced technologies and frameworks to create\
  \ webpages. We now use..."
---

Par Abiola Farounbi

Le développement de pages web consistait autrefois à écrire du HTML, du CSS et un peu de code de script comme JavaScript pour la fonctionnalité. 

Mais avec le temps, nous avons développé de nouvelles technologies et frameworks plus avancés pour créer des pages web. Nous utilisons désormais des choses comme des composants réutilisables, le routage et le rendu vers le modèle d'objet de document (DOM). 

Ces nouveaux frameworks ont aidé les développeurs à faire de l'accessibilité web une partie intégrante de leurs applications. 

Dans cet article, nous examinerons le concept d'accessibilité web, explorerons certaines fonctionnalités accessibles pour les applications Vue et construirons un projet Vue de démonstration qui incorpore toutes ces fonctionnalités d'accessibilité. 

Pour suivre la partie tutoriel de cet article, vous devez avoir une certaine expérience avec Vue et JavaScript. 

## Qu'est-ce que l'accessibilité web ?

L'accessibilité web est la pratique de la conception et du développement d'applications et d'outils web accessibles aux personnes ayant tout type de handicap. 

En termes simples, l'accessibilité web signifie rendre le web disponible et accessible à tous. Le web doit être accessible à tous pour fournir un accès égal aux utilisateurs, afin que chacun puisse bénéficier pleinement des avantages et de la capacité du web. 

Un avantage de rendre votre application web accessible est d'améliorer le SEO (optimisation pour les moteurs de recherche) de votre site. Cela le rend plus facile à trouver dans différents moteurs de recherche.

Les [Règles pour l'accessibilité des contenus Web (WCAG)](https://www.w3.org/WAI/WCAG21/quickref/) fournissent un ensemble international de principes pour l'accessibilité web. Vous pouvez l'utiliser pour guider votre développement afin de rendre le web accessible à tous. 

## Principes d'accessibilité web 
Les WCAG se composent de quatre principes connus sous le nom de POUR : 

P - Perceptible 

O - Utilisable 

U - Compréhensible 

R - Robuste 

### Rendre votre site perceptible 

Le principe perceptible signifie que les utilisateurs doivent être capables d'identifier les contenus et d'interagir avec l'interface en utilisant un ou plusieurs de leurs sens (vision, toucher et ouïe) via le navigateur ou via des technologies d'assistance comme les lecteurs d'écran. 

### Rendre votre site utilisable 

Rendre votre site utilisable signifie que les utilisateurs peuvent interagir avec tous les contrôles et éléments interactifs en utilisant une souris, un clavier ou un dispositif d'assistance.
Le focus doit également être activé dans les différentes sections de la page.

### Rendre votre site compréhensible 

Pour rendre un site web compréhensible, nous devons utiliser un langage clair et concis. Nous devons essayer d'éliminer les erreurs d'orthographe et la grammaire complexe. Le contenu et les fonctions doivent tous être faciles à comprendre. 

### Rendre votre site robuste 

Pour être robuste, votre site doit être compatible sur toutes les plateformes, tous les appareils et tous les navigateurs. Le contenu web doit être compatible avec les logiciels et outils actuels et futurs. Une large gamme de technologies doit pouvoir accéder au contenu des pages web sans limitations. 

## Fonctionnalités d'accessibilité à implémenter dans vos applications Vue 

Lorsque vous développez une application Vue.js, vous devez mettre en place certaines fonctionnalités importantes pour rendre votre application web accessible à tous. 

### Définir le titre de la page pour chaque page 

Le titre de la page donne aux utilisateurs un aperçu de la page. Les moteurs de recherche s'appuient également sur lui pour déterminer si une page est pertinente pour leur recherche. 

Lorsque vous fournissez un titre unique et concis, cela aide les utilisateurs de technologies d'assistance à comprendre de quoi parle la page web. 

Dans une application Vue, vous pouvez faire cela en déclarant des balises meta dans vos routes : 

```   routes: [ 

    { 

      path: '/', 

      name: 'home', 

      component: HomePage, 

      meta: { 

        title: 'Accueil' 

      } 

    }, 

   { 

      path: '/login', 

      name: 'login', 

      component: LoginPage, 

      meta: { 

        title: 'Connexion' 

      } 

    },  

]
```


Pour que les balises meta s'affichent, utilisez le hook `beforeEach` fourni par Vue-router : 

 
```
router.beforeEach((to, from, next) => { 

  document.title = to.meta.title 

  next() 

}) 
```
 

Pour en savoir plus sur le package router, consultez le [site officiel de vue router](https://router.vuejs.org/guide/essentials/dynamic-matching.html#reacting-to-params-changes)

Avec le temps, les membres de la communauté Vue ont développé des packages tels que [vue-head](https://github.com/ktquez/vue-head) et [vue-meta](https://github.com/declandewet/vue-meta) pour ajouter des métadonnées lors de l'instanciation d'un composant. 


### Spécifier la langue du contenu textuel 

Lorsque vous utilisez l'attribut lang HTML, il est facile pour les lecteurs d'écran d'identifier la langue du contenu textuel. L'attribut lang prend un code de [langue ISO](https://www.loc.gov/standards/iso639-2/php/code_list.php) comme valeur.

Vous pouvez implémenter cela dans le fichier index.html : 

```  
<html lang="fr"> 
```

Si l'application ne spécifie pas de langue, le lecteur d'écran utilise sa langue par défaut. Cela pose un problème si la page n'est pas réellement dans la langue par défaut. Le lecteur d'écran pourrait ne pas annoncer correctement le texte de la page. 

### Utiliser des repères pour aider les utilisateurs à naviguer vers les sections

Les repères fournissent un accès facile aux sections d'une application Vue. Les utilisateurs de technologies d'assistance peuvent naviguer vers chaque section de l'application et sauter le contenu. 

Vous pouvez activer cela en utilisant des éléments sémantiques HTML5 ou des rôles Accessible Rich Internet Applications (ARIA). 

Voici les éléments sémantiques HTML5 et les ARIA alternatifs que vous pouvez utiliser dans votre application : 

![Repères](https://www.freecodecamp.org/news/content/images/2021/07/Landmarks.png)

### Utiliser les titres dans l'ordre hiérarchique approprié 

Votre application web doit inclure des titres tels que : 

```
<h1></h1> 

<h2></h2> 

<h3></h3> 

<h4></h4> 

<h5></h5> 

<h6></h6> 
```

Pour structurer votre contenu pour une accessibilité facile, vos titres doivent suivre l'ordre hiérarchique approprié, de H1 potentiellement jusqu'à H6, si nécessaire. De plus, vos titres doivent être brefs, clairs, informatifs et uniques. 

### Utiliser un contraste de couleur adéquat dans votre application 

![boncontraste](https://www.freecodecamp.org/news/content/images/2021/07/goodcontrast.png)

Il est important de s'assurer que les couleurs de votre application ont un contraste adéquat. Le contraste entre les couleurs du texte et de l'arrière-plan doit être distinct pour rendre le contenu lisible.

### Utiliser un texte alternatif pour les images 

Dans le code d'image comme ci-dessous, l'ajout de la section "alt" vous permet de décrire l'image. 

```
<img src="image-url" alt=" description de l'image"> 
```
 
L'inclusion d'un texte alternatif pour une image facilite la compréhension de l'image pour les personnes qui ne peuvent pas voir en utilisant un lecteur d'écran. 

Utilisez la balise `<img>` uniquement pour afficher des images de contenu, telles que des photos ou des illustrations, qui sont significatives pour le contenu. De plus, utilisez un texte alt nul sur les images purement décoratives. 

### Créer des formulaires accessibles 

La création de formulaires d'application Vue accessibles peut impliquer : 

- L'utilisation d'éléments sémantiques HTML5 pour les éléments de formulaire, comme : 

  ```<form>, <label>,<input>, <textarea>, et <button> ```

- L'inclusion de libellés pour les éléments de formulaire : 

```
<label for="name">Nom</label>  
  <input type="text" name="name" id="name" v-model="name"  />
 ```
 
L'attribut "for" d'un champ de saisie doit être le même que son attribut "id" pour les lier ensemble, comme montré ci-dessus. Cela permet au lecteur d'écran de notifier l'utilisateur lorsqu'il clique sur le champ de texte associé au nom. 

### Utiliser les attributs ARIA 

Les Applications Internet Riches Accessibles (ARIA) sont une extension de la syntaxe HTML qui transmet des informations supplémentaires aux technologies d'assistance. Vous pouvez utiliser les attributs ARIA pour décrire des éléments personnalisés. 

```
<button aria-label="fermer"  @click="modalClose" > X </button> 
```

Dans l'exemple ci-dessus, l'aria-label fournit une description pour aider les technologies d'assistance à savoir que l'application se fermera lorsque vous cliquerez sur le bouton X. 

### Utiliser les gestionnaires de clavier 

Pour chaque gestionnaire d'événements de souris, il doit y avoir un gestionnaire de clavier correspondant. Cela est important pour les utilisateurs qui préfèrent naviguer sur la plateforme avec leur clavier. Par exemple : 

```
<button type="submit"  

            @keydown.enter="displayMessage" 

            @click.prevent="displayMessage" > 

             Soumettre 
</button> 
```
Vous pouvez faire cela en ajoutant simplement la directive "Vue-directive" keyup et le modificateur ".enter" comme démontré ci-dessus. 

### Gérer le focus et rendre les éléments focusables
Les personnes qui utilisent des lecteurs d'écran utilisent également le clavier pour accéder aux informations. Vous devez rendre votre application accessible au clavier en rendant les éléments focusables. 

Donner le focus aux éléments fonctionne de différentes manières, telles que : 

- Utiliser les refs Vue : 
Pour focaliser un élément dans Vue, nous utilisons l'attribut ref, qui vous permet d'accéder directement aux nœuds DOM sous-jacents. 

```
<template> 
          <ul> 
             <li ref='projectList'> Projet Vue   </li> 
          </ul> 
</template> 
<script> 
    mounted() { 
       const projectListRef = this.$refs.projectList; 
        projectListRef.focus(); 
       } 

</script> 
```

Dans l'extrait de code ci-dessus, nous sommes capables d'ajouter le focus à l'élément de liste une fois que le composant est monté dans le DOM. 

- Utiliser tabindex : 
Vous pouvez également utiliser tabindex pour ajouter le focus à un élément. Pour utiliser tabindex : 
1) Si une valeur de 0 est donnée, l'élément peut être focalisé via le clavier et fait partie du flux de tabulation de la page. 

2) Si une valeur de ""-1"" est donnée, l'élément ne peut pas être tabulé. 

3) Les valeurs supérieures à 1 créent un niveau de priorité, 1 étant le plus important.

```
<input type='search"   id='searchBar' tabindex="0"  /> 
```

Dans les pages web où il y a plusieurs liens, il est bon d'ajouter un lien pour sauter au contenu principal. Cela fait gagner du temps à l'utilisateur et lui donne la possibilité de se concentrer sur le contenu principal. Les liens de saut sont généralement cachés jusqu'à ce qu'ils soient focalisés. 

Voici l'extrait de code pour implémenter les liens de saut dans Vue : 












 


%[https://codepen.io/coded_fae/pen/MWppaBG]

## La bibliothèque Vue Announcer 

Pour les grandes applications Vue composées de diverses pages, la [bibliothèque vue announcer](https://announcer.vue-a11y.com/) fournit un moyen facile pour les personnes utilisant des lecteurs d'écran de savoir ce qui se passe dans votre application. 

Pour utiliser la bibliothèque : 

 
```
import Vue from 'vue' 

import VueAnnouncer from '@vue-a11y/announcer' 

Vue.use(VueAnnouncer) 
```

Vous pouvez explorer le [guide de documentation officiel](https://announcer.vue-a11y.com/) pour en savoir plus.

---

## Projet de démonstration Vue 
![rapport-accessibilite-lighthouse](https://www.freecodecamp.org/news/content/images/2021/07/lighthouse-accessibilty-report.png)

Dans cette section, nous allons construire une application monopage en suivant toutes les fonctionnalités et principes d'accessibilité. Consultez la [démonstration](https://accessibile-vue-app.netlify.app/) et le dépôt de code sur [Github](https://github.com/Abiola-Farounbi/Accessibile-vue-app). 

Cette application est simple. Elle est divisée en différents composants et nous construirons chaque composant en suivant les normes d'accessibilité. 

Pour construire l'application, suivez ces étapes : 

### Créer un projet Vue 

Tout d'abord, installez l'interface de ligne de commande (CLI) de Vue : 

```npm install -g @vue/cli```
 

Ensuite, créez l'application Vue en utilisant cette commande : 

```vue create accessibile-vue-app``` 

cd dans accessible-vue-app, et exécutez la commande suivante pour démarrer l'application : 

```npm run serve```

### Comment créer les différents composants 

La page est divisée en différents composants et rendue dans le fichier App.vue.

- [Composant Header](https://github.com/Abiola-Farounbi/Accessible-vue-app/blob/master/src/components/Header.vue)
- [Composant welcomeCard](https://github.com/Abiola-Farounbi/Accessible-vue-app/blob/master/src/components/welcomeCard.vue)
- [Composant Form](https://github.com/Abiola-Farounbi/Accessible-vue-app/blob/master/src/components/Form.vue)
- [Composant Footer](https://github.com/Abiola-Farounbi/Accessible-vue-app/blob/master/src/components/Footer.vue)

Pour chaque composant, le HTML sémantique définit la structure. Ensuite, nous les rendons tous dans `App.vue` comme un seul. 

App.vue:

```<template> 
  <Header></Header> 
  <main> 
<section class='pageOptions'> 
   <button @click="selectedComponent = 'WelcomeCard'" > Message de bienvenue </button> 
  <button @click="selectedComponent = 'Form'" > Formulaire de contact </button>  
</section> 
  <!-- liaison du composant actuel à la propriété  --> 
  <component :is="selectedComponent"></component> 
 </main> 
  <Footer></Footer> 
</template> 
```

Vous pouvez explorer la démonstration sur [Netlify](https://accessible-vue-app.netlify.app/) ici.
 

## Outils d'accessibilité pour tester les applications Vue 
Il existe de nombreux outils différents que vous pouvez utiliser pour tester si votre contenu web respecte les directives d'accessibilité. 

Voici quelques outils et sites web que vous pouvez utiliser pour vérifier si un site web est accessible : 

* Lighthouse dans les outils de développement Chrome 
* [Outil d'évaluation de l'accessibilité web (WAVE)](https://wave.webaim.org/) 
* Lecteurs d'écran sur [Chrome Vox](https://chrome.google.com/webstore/detail/screen-reader/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en) 
* [Liste de contrôle d'accessibilité](https://www.a11yproject.com/checklist/#global-code) 
* Audit d'accessibilité pour les applications Vue.js sur [Vue axe](https://axe.vue-a11y.com/#links)
* Outil de vérification du contraste des couleurs sur [WebAIM](https://webaim.org/resources/contrastchecker/).
    
    
## Conclusion 

Dans cet article, nous avons appris ce qu'est l'accessibilité web et pourquoi il est important de rendre nos pages web accessibles. 

Nous avons également examiné différentes fonctionnalités d'accessibilité à ajouter à vos applications Vue.js et appris comment les implémenter. 

En utilisant ces informations, vous pouvez construire avec succès une application Vue que tout le monde peut utiliser. 

Pour en savoir plus sur la manière de rendre vos applications Vue plus accessibles, explorez le [site web de Vue.js](https://v3.vuejs.org/guide/a11y-standards.html). 

Vous pouvez également me contacter sur [Twitter](https://twitter.com/abiolaesther_?s=08) pour toute question. Merci d'avoir lu !