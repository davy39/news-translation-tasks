---
title: Vous voulez apprendre Svelte ? Voici un cours gratuit en 16 parties par Noah
  Kaufman
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-14T22:09:51.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-svelte-heres-our-free-15-part-course-by-noah-kaufman
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/jm6s35gtdtf5rijq0uqm.png
tags:
- name: Scrimba
  slug: scrimba
- name: Svelte
  slug: svelte
seo_title: Vous voulez apprendre Svelte ? Voici un cours gratuit en 16 parties par
  Noah Kaufman
seo_desc: 'By Per Harald Borgen

  If you''re looking to learn a new Javascript framework which allows you to write
  less code, use no virtual DOM, and create truly reactive apps, then Svelte is for
  you.

  What is Svelte?

  Svelte is a Javascript framework, a compiler, ...'
---

Par Per Harald Borgen

Si vous cherchez à apprendre un nouveau framework Javascript qui vous permet d'écrire moins de code, de ne pas utiliser de DOM virtuel et de créer des applications vraiment réactives, alors Svelte est fait pour vous.

## Qu'est-ce que Svelte ?

Svelte est un framework Javascript, un compilateur et un langage. Contrairement à d'autres frameworks comme React et Vue qui font une grande partie de leur travail dans le navigateur, Svelte fait son travail lors de l'étape de compilation. Cela permet d'obtenir un code très efficace et un temps d'exécution potentiellement plus rapide côté client.

Svelte offre un développement plus rapide, des pages web plus rapides et une meilleure expérience développeur - les créateurs de Svelte l'ont créé en pensant aux autres développeurs). 

En plus de cela, connaître Svelte vous aidera à vous démarquer auprès des employeurs potentiels et montre que vous vous intéressez aux nouvelles technologies.

## Super ! Parlez-moi de Svelte.

Cet article vous guide à travers le tout nouveau [cours Svelte en 16 parties de Scrimba](https://scrimba.com/playlist/pG6X6UG?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) qui couvre les sujets essentiels suivants pour vous mettre sur la bonne voie pour devenir un maître de Svelte :

- Composants
- Importation/exportation
- Slots
- Template
- Gestion des événements
- Dispatching d'événements
- Boutons
- Réactivité
- Binding

Le cours est dispensé à travers une série de screencasts interactifs, vous permettant de pratiquer vos nouvelles compétences et d'ancrer véritablement votre apprentissage.

Se terminant par un projet final approfondi qui consolide toutes les compétences apprises en cours de route, le cours vous aide à construire la mémoire musculaire nécessaire pour devenir un développeur Svelte efficace. 

Il est dirigé par Noah Kaufman, un développeur frontend senior de San Francisco, Californie, avec un M.S en linguistique computationnelle.

Si cela vous semble intéressant, [rendez-vous sur le cours](https://scrimba.com/g/glearnsvelte?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) sur Scrimba et continuez à lire pour en savoir plus.

## Composants

Dans Svelte, tout existe à l'intérieur d'un composant, et le premier cast montre à quoi ressemble l'anatomie de ces composants. 

Le composant a trois parties optionnelles ; `<script>`, qui contient du Javascript, `<style>` qui contient du CSS, et enfin du HTML, qui est capable d'utiliser le JS de la balise `<script>`.

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

## Importation et Exportation

Ici, nous jetons un rapide coup d'œil à la façon d'importer et d'exporter des composants afin qu'ils puissent être utilisés ailleurs dans notre application.

Les composants sont importés avec le mot-clé `import` :

```js
import Face from "./Face.svelte";
```

Tandis que le mot-clé `export` permet à d'autres composants de modifier des composants à l'importation :

```js
<script>
    export let size;
</script>

<div style="font-size: {size}em">=)</div>
```

## Défi 1

Dans ce cast, Noah nous met au défi de tester nos nouvelles compétences en Svelte. Pas de spoilers ici, alors [cliquez sur le cours](https://scrimba.com/p/pG6X6UG/cvdpNRU8?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) pour essayer le défi et vérifier la solution.

## Slots

Les slots nous permettent de placer des éléments à l'intérieur des composants. Par exemple, insérer un `<slot>` dans un `<div>` avec la classe `Container` nous permet de placer autant d'éléments que nous voulons dans le composant `<Container>` :

```js
<div class="Container">
  <slot></slot>
</div>
```

Les éléments nouvellement placés sont des enfants du composant :

```js
<Container>
  <div>Say: {say}</div>

  <Face index={0} />
  <Face />
  <Face index={2} />
</Container>
```

## Templating

La syntaxe de templating de Svelte nous permet d'ajouter des instructions if et des boucles for à notre HTML. C'est exact, à notre HTML !

Une instruction if ressemble à ceci :

```js
<Container>
    {#if say}
        <div>
            Hi!
        </div>

    {/if}
</Container>
```

Tandis qu'une boucle for ressemble à ceci :

```js
{#each [2,1,0] as faceIndex}
        <Face index={faceIndex} />
    {/each}
```

## Création de Header - Défi 2

Dans ce défi, nous utilisons ce que nous venons d'apprendre sur le templating Svelte pour ajouter un Header à notre application. [Consultez le cours](https://scrimba.com/p/pG6X6UG/cGmeLzsR?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) pour l'essayer vous-même et vérifier votre réponse.

## Gestion des événements

Ensuite, Noah nous montre un simple gestionnaire d'événements en ligne, qui permet à l'utilisateur d'afficher l'en-tête de l'application au clic d'un bouton.

```js
<button
  on:click={() => {
    showHeader = true;
  }}
>
  show
</button>
```

Cependant, si nous utilisons un composant `<Button>` plutôt qu'un bouton HTML natif, ce type de gestionnaire `on:click` ne fonctionnera pas. Nous pouvons corriger cela avec **le transfert d'événements**, c'est-à-dire en ajoutant un `on:click` simple au bouton natif `<button>` dans le fichier du composant :

```js
<button on:click>
  <slot></slot>
</button>
```

## Dispatching d'événements

Le dispatching d'événements permet à un composant d'émettre plus d'un type d'événement, par exemple, le même composant `<Button>` peut être utilisé à la fois pour afficher un élément et pour le masquer.

Nous créons un dispatcher d'événements comme ceci :

```js
<script>
  import {createEventDispatcher} from 'svelte'; const dispatch =
  createEventDispatcher();
</script>
```

Nous l'ajoutons ensuite au bouton HTML natif `<button>` comme ceci :

```js
<button on:click={() => dispatch('show')}>
    Show
</button>
<button on:click={() => dispatch('hide')}>
    Hide
</button>
```

Enfin, nous définissons les options de fonctionnalité du `<Button>` dans le fichier `App.svelte` comme ceci :

```js
<Buttons
  on:show={() => {
    showHeader = true;
  }}
  on:hide={() => {
    showHeader = false;
  }}
/>
```

Le même résultat peut également être obtenu en passant des valeurs (dans ce cas `true` et `false`) à travers le dispatch. Les valeurs peuvent ensuite être accessibles via la variable d'événement `e`.

```
<button on:click={() => dispatch('click', true)}>
    Show
</button>
<button on:click={() => dispatch('click', false)}>
    Hide
</button>
```

```js
<Container>
  <Buttons
    on:click={(e) => {
      showHeader = e.detail;
    }}
  />
</Container>
```

## Boutons - Défi 3

Notre troisième défi est plus impliqué que les deux précédents et met à l'épreuve nos nouvelles connaissances sur les dispatchers d'événements. Pour nous aider, Noah divise le défi en morceaux plus petits :

```js
<!-- Défi 3 -
1. ajouter une prop dans Buttons.svelte appelée buttons qui est une liste d'objets comme :
[{value: '', text: ''}, ...etc]
2. utiliser #each pour transformer tous les objets en boutons qui :
    a. ont innerHTML égal à .text de l'objet.
    b. dispatch un événement click qui passe .value de l'objet.
3. Gérer l'événement dans App.svelte pour mettre à jour le score.
-->
```

[Rendez-vous sur le cours](https://scrimba.com/p/pG6X6UG/cp342mTV?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) maintenant pour l'essayer et voir la solution.

## Réactivité

Les déclarations réactives sont une fonctionnalité unique de Svelte qui indique à un morceau de code de s'exécuter à chaque fois qu'une variable dans ce code est mise à jour. 

Par exemple, le code ci-dessous s'exécutera à chaque fois que la variable score est modifiée (notez que nous déclarons une déclaration réactive avec `$:`).

```js
let score = 0;
$: smileySays = "Hi there, your score is: " + score;
```

Nous pouvons également exécuter des instructions if à l'intérieur des déclarations réactives :

```js
let score = 0;
$: smileySays = "Hi there, your score is: " + score;
$: if (score < -4) smileySays = "Wow your score is low!";
```

## Défi Réactif - Défi 4

Nous pouvons maintenant tester nos nouvelles compétences en complétant le Défi Réactif, qui nous rapproche d'un pas de plus pour être prêts pour le projet final.

Une fois de plus, Noah divise le défi en parties plus petites pour nous aider en cours de route :

```js
<!-- Défi 4 -
1. ajouter happyScore et storyIndex (tous deux égaux à 0)
2. smileySays et buttons se mettent à jour chaque fois que storyIndex change
3. ajouter la fonction clickHandler qui incrémente storyIndex et ajoute e.detail.value à happyScore -->
```

[Cliquez sur le cours](https://scrimba.com/p/pG6X6UG/cgKqRDt9?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) pour l'essayer et vérifier votre réponse.

## Un peu plus de réactivité

Ensuite, Noah nous donne un autre exemple d'utilisation des déclarations réactives, un visage emoji qui change selon la variable `happyScore` actuelle :

```js
const faceList = [
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
];
$: index = happyScore + 5;
```

De manière similaire aux exemples précédents, le code s'exécute à chaque fois que la variable 'happyScore' change, donc une déclaration réactive est simplement l'outil idéal pour le travail.

## Binding

Le binding permet à un utilisateur de mettre à jour une variable (dans ce cas appelée `name`) en entrant une valeur dans un champ `<input>`. Comme le binding est un processus à double sens, changer la variable met également à jour la valeur de l'`<input>` :

Nous bindons les valeurs comme ceci :

```js
<script>
    import Face from './Face.svelte';
    import Container from './Container.svelte';
    import story from './story';

    let showHeader = false;
    let storyIndex = 0;
    $: smileySays = story[storyIndex].smileySays;
    //nom de la variable ci-dessous :
    let name = '';
</script>

<Container>
    //binding déclaré ci-dessous :
    <input type="text" bind:value={name}>
    <h1>{name}, {smileySays}</h1>
</Container>
```

En plus de binder des variables, il est également possible de binder des valeurs provenant d'objets, de listes ou de composants.

## Projet Final

[![Projet Final](https://dev-to-uploads.s3.amazonaws.com/i/mzg89uwkqt4yd0t4ghdz.png)](https://scrimba.com/p/pG6X6UG/cgKK4yhG?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article)
_Cliquez sur l'image pour accéder au projet final._

Félicitations pour avoir suivi le cours ! Nous concluons avec un projet final qui rassemble toutes les compétences que nous avons apprises en cours de route. 

Une fois de plus, Noah le divise en morceaux plus petits pour nous aider :

```js
<!-- Défi Final
1. L'en-tête apparaît si l'utilisateur choisit la réponse Svelte
(INDICE : happyScore sera supérieur à 0 s'ils répondent Svelte)
2. Afficher le message final en fonction de happyScore
3. Implémenter la fonctionnalité Reset
-->
```

[Consultez le cast](https://scrimba.com/p/pG6X6UG/cgKK4yhG?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) pour tester vos nouvelles compétences Svelte et voir la solution.

## Outro

Cela nous amène à la fin du cours. Bravo pour l'avoir terminé ! Et si vous êtes impatient d'en apprendre plus sur Svelte, consultez la documentation officielle sur [svelte.dev](https://svelte.dev/) pour des sujets comme : `Context`, `Stores`, `Lifecycle methods`, `Actions`, `Sapper` et plus encore.

Vous pouvez également suivre ma [chaîne YouTube SvelteMaster](https://www.youtube.com/channel/UCg6SQd5jnWo5Y70rZD9SQFA) et vous inscrire au [Scrimba Svelte Bootcamp](https://rebrand.ly/sveltebootcamp) pour être le premier informé du lancement et des éventuelles réductions.

J'espère que vous l'avez trouvé utile et que vous pourrez mettre vos toutes nouvelles connaissances à bon escient très bientôt.

En attendant, pourquoi ne pas [vous rendre sur Scrimba](https://scrimba.com/?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) pour voir quels autres cours sont proposés pour vous aider à atteindre vos objectifs de codage ?

Si vous souhaitez également traîner avec vos camarades apprenants ou discuter avec des personnes plus expérimentées et les créateurs des cours Scrimba, rejoignez notre [serveur Discord Scrimba](https://discord.gg/mF6PcNU).

Bon apprentissage :)


%[https://www.youtube.com/watch?v=SU25upz4WCI]