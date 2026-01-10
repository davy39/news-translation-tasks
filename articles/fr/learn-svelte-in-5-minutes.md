---
title: Apprendre Svelte en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T20:49:08.000Z'
originalURL: https://freecodecamp.org/news/learn-svelte-in-5-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-06-at-16.10.39.png
tags:
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: Svelte
  slug: svelte
seo_title: Apprendre Svelte en 5 minutes
seo_desc: "By Leanne Rybintsev\nThis article gives you a lightning-speed overview\
  \ of Svelte - a Javascript framework which lets you write less code, use no virtual\
  \ DOM, and create truly reactive apps. \nAs if that's not enough, Svelte is super-intuitive\
  \ too! Buil..."
---

Par Leanne Rybintsev

Cet article vous donne un aperçu éclair de Svelte - un framework JavaScript qui vous permet d'écrire moins de code, de ne pas utiliser de DOM virtuel et de créer des applications vraiment réactives. 

Comme si cela ne suffisait pas, Svelte est également super-intuitif ! Conçu avec les développeurs à l'esprit, il est conçu pour faciliter le codage, accélérer la correction des bugs et rendre la vie professionnelle d'un développeur généralement plus heureuse. 

Si cela vous semble tout à fait adapté, alors lisez la suite !

Bien que 5 minutes ne suffisent pas pour vous enseigner Svelte en profondeur, cela permet une solide vue d'ensemble des bases, y compris :

- Composants
- Importation et exportation
- Modèles
- Gestion des événements
- Dispatching des événements
- Réactivité

Si vous souhaitez en savoir plus sur Svelte après avoir lu cet article, consultez [le cours complet](https://scrimba.com/course/glearnsvelte?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) sur Scrimba. Là, vous en apprendrez davantage sur les fonctionnalités de Svelte et aurez l'occasion de tester vos nouvelles compétences avec une série de défis interactifs. 

Pour l'instant, commençons par les bases !

## Composants

[![DOM affichant un composant Svelte](https://dev-to-uploads.s3.amazonaws.com/i/e8ej7929dpa3u9tzsm0u.png)](https://scrimba.com/p/pG6X6UG/cNDg9yHB?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Cliquez sur l'image pour accéder au cours.)*

Tout d'abord, nous allons voir comment construire un composant Svelte, qui peut contenir trois parties ; `<script>`, qui contient du JavaScript, `<style>`, qui contient du CSS et le HTML, qui utilise le JS de la balise `<script>`. 

```js
<script>
    let say = 'hi';
</script>

<style>
    div {
        color: red;
    }
</style>

<div>
    Say: {say}
</div>
``` 
**Note :** Le strict minimum nécessaire pour un composant Svelte est le HTML, donc l'application fonctionnera toujours sans les balises `<script>` et `<style>`.

## Importation et exportation

Un grand avantage de l'utilisation des frameworks est la possibilité de modulariser le code en le divisant en composants séparés. Les composants sont ensuite importés dans l'application principale en utilisant le mot-clé `import` : 

```js
  import Face from './Face.svelte';
```

Contrairement à d'autres frameworks, le mot-clé `export` n'est pas requis pour utiliser un composant ailleurs dans une application. Au lieu de cela, il est utilisé pour passer des paramètres, ou props, des éléments parents à leurs enfants. 

Par exemple, nous pouvons définir une prop de taille avec une taille par défaut dans notre composant :
```js
<script>
    export let size = 1;
</script>

<div style="font-size: {size}em">=)</div>
```

Cela nous permet d'ajuster facilement la taille du composant importé dans notre fichier `App.svelte` : 
```js
<script>
    import Face from './Face.svelte';
</script>

<Face size="4" />
<Face size="10" />
<Face />
```
Les différentes tailles apparaissent sur le DOM comme suit :

[![composant importé avec diverses tailles utilisant des props](https://dev-to-uploads.s3.amazonaws.com/i/3aecnw1qq3xpcck19agr.png)](https://scrimba.com/p/pG6X6UG/cbDNVncg?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Cliquez sur l'image pour accéder au cours.)*

Rendez-vous sur [le cours sur Scrimba](https://scrimba.com/p/pG6X6UG/cbDNVncg?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) pour consulter et jouer avec le code complet. 

## Modèles

La syntaxe de [modélisation Svelte](https://scrimba.com/p/pG6X6UG/cMZrQds2?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) est une excellente fonctionnalité qui nous permet d'ajouter des instructions if et des boucles for à notre HTML.

La syntaxe pour une instruction if ressemble à ceci :
```js
<Container>
    {#if say}
        <div>
            Hi!
        </div>
    
    {/if}
</Container>
```

Tandis qu'une boucle for est comme suit :
```js
{#each [2,1,0] as faceIndex}
        <Face index={faceIndex} />
    {/each}
```

## Gestion des événements
Pour permettre à l'utilisateur d'interagir avec notre application, nous avons besoin de gestionnaires d'événements. Dans [ce scrim](https://scrimba.com/p/pG6X6UG/caZ3J6U3?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article), nous voyons comment ajouter un simple `on:click` à un `<button>` pour afficher l'en-tête de notre application :
```js
<button on:click={() => {showHeader = true}}>show</button>
```
Et quel en-tête c'est..!
[![en-tête rendu visible sur le DOM avec un gestionnaire d'événements](https://dev-to-uploads.s3.amazonaws.com/i/czgdba1dpkzu552kq2hq.png)](https://scrimba.com/p/pG6X6UG/caZ3J6U3?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Cliquez sur l'image pour accéder au cours.)*

Il y a un piège avec cela, cependant - cela ne fonctionne qu'avec la balise HTML native `<button>` et non avec les composants importés appelés `<Button>`. 

Heureusement, nous pouvons contourner cela en utilisant **la transmission d'événements**, c'est-à-dire en ajoutant un `on:click` à la balise native `<button>` dans son fichier de composant :
```js
<button on:click>
        <slot></slot>
</button>
```

## Dispatching des événements

[![Boutons masquer et afficher créés avec un dispatcher d'événements](https://dev-to-uploads.s3.amazonaws.com/i/w203a2wxgn1brk5ss6i4.png)](https://scrimba.com/p/pG6X6UG/cD4bKDuD?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Cliquez sur l'image pour accéder au cours.)*
Le dispatching des événements est une excellente fonctionnalité de Svelte qui augmente l'utilisabilité du code en nous permettant d'utiliser le même élément pour plus d'une action.

Dans [ce scrim](https://scrimba.com/p/pG6X6UG/cD4bKDuD?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article), nous apprenons comment utiliser un composant `<Button>` pour à la fois afficher et masquer un élément. 

Nous créons un dispatcher d'événements dans le fichier du composant `<Button>` comme ceci :
```js
<script>
    import {createEventDispatcher} from 'svelte';
    const dispatch = createEventDispatcher();    
</script>
```
Nous ajoutons ensuite le dispatcher à notre balise HTML native `<button>` comme ceci :
```js
<button on:click={() => dispatch('show')}>
    Show
</button>
<button on:click={() => dispatch('hide')}>
    Hide
</button>
```
Enfin, nous déclarons les options de fonctionnalité du bouton dans le fichier `App.svelte` comme suit : 
```js
<Buttons on:show={() => {showHeader = true}} on:hide={() => {showHeader = false}} />
```
Nous pouvons refactoriser cela en passant des valeurs à travers le dispatch en utilisant la variable d'événement (`e`). Dans ce cas, le `<Button>` dans notre fichier `App.svelte` ressemble à ceci :
```js
<Buttons on:click={(e) => {showHeader = e.detail}} />
```
Tandis que les balises HTML natives `<button>` dans notre fichier de composant ressemblent à ceci :
```js
<button on:click={() => dispatch('click', true)}>
    Show
</button>
<button on:click={() => dispatch('click', false)}>
    Hide
</button>
```

## Réactivité
Si vous voulez qu'un morceau de code soit réexécuté chaque fois que sa variable associée est mise à jour, alors la fonctionnalité unique de Svelte, [l'instruction réactive](https://scrimba.com/p/pG6X6UG/caZ3yBAB?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article), est faite pour vous. Nous déclarons une instruction réactive avec `$:` comme suit : 
```js
let score = 0;
    $: smileySays = 'Hi there, your score is: ' + score;
```

Il est également possible d'exécuter des instructions if à l'intérieur des instructions réactives. Le code pour le faire ressemble à ceci :
```js
let score = 0;
    $: smileySays = 'Hi there, your score is: ' + score;
    $: if (score < -4) smileySays = 'Wow your score is low!'
```

C'est à peu près toutes les fonctionnalités que nous pouvons entasser dans notre tour de 5 minutes de Svelte. J'espère que vous l'avez trouvé utile et que vous êtes inspiré pour essayer le framework par vous-même et tester vos nouvelles compétences. 

N'oubliez pas de consulter le cours complet [sur Scrimba](https://scrimba.com/course/glearnsvelte?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) pour découvrir encore plus de fonctionnalités de Svelte et essayer les défis de codage. 

Où que votre voyage de codage vous mène ensuite, bon apprentissage 😊