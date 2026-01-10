---
title: Comment créer un composant Callout pour votre blog Astro
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2024-10-22T13:19:49.536Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-callout-component-for-your-astro-blog
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728900397885/4c9f906f-e531-4588-9e45-7b56920d676e.png
tags:
- name: JavaScript
  slug: javascript
- name: Astro
  slug: astro
- name: Web Development
  slug: web-development
seo_title: Comment créer un composant Callout pour votre blog Astro
seo_desc: 'Earlier this year, I became really interested in learning about Astro,
  so I completely rebuilt my blog using it. The results have been amazing since then:
  I can easily handle automatic sitemap generation and SEO, and integrating other
  tools became a ...'
---

Plus tôt cette année, je me suis vraiment intéressé à apprendre Astro, alors j'ai complètement reconstruit mon blog en l'utilisant. Les résultats ont été incroyables depuis : je peux facilement gérer la génération automatique de sitemap et le SEO, et l'intégration d'autres outils est devenue un jeu d'enfant. Grâce à ces avantages, j'ai été inspiré pour publier un article chaque semaine.

Astro est incroyable pour les sites web axés sur le contenu – tellement que depuis, je fais une blague : il devrait être interdit de construire un blog et un site de documentation avec un autre framework frontend qu'Astro.

Une autre chose notable que j'ai pu faire sur mon blog a été de construire un composant callout. Ce sont les petites boîtes tangentielles que vous voyez sur les sites de documentation et certains blogs de développeurs avancés.

Voici un exemple dans la documentation de freeCodeCamp :

![freeCodeCamp docs callout](https://cdn.hashnode.com/res/hashnode/image/upload/v1728898968834/da8175de-6380-4094-bf96-1c0d14f51625.png align="center")

Et voici un exemple dans la documentation d'Astro :

![Astro documentation callout box](https://cdn.hashnode.com/res/hashnode/image/upload/v1728898998665/981f943b-d138-4f52-9e3f-627ab83526d8.png align="center")

Un peu unique, voici un exemple sur le blog de Josh Comeau :

![Josh Comeau blog callout box](https://cdn.hashnode.com/res/hashnode/image/upload/v1728899020675/a1199846-e851-4438-81dd-17a3da759d97.png align="center")

Continuez à lire pour que je puisse vous montrer comment construire un composant callout pour votre blog Astro.

Vous pouvez également utiliser la même technique pour en créer un pour un blog construit avec un autre framework frontend.

## Prérequis

Pour tirer le meilleur parti de cet article, vous avez besoin des éléments suivants :

* des connaissances de base sur Astro

* une connaissance des slots et fragments Astro

* une familiarité avec JSX et le prop-drilling

* une compréhension de l'architecture basée sur les composants

Les slots et fragments Astro peuvent sembler un peu étranges. Si c'est le cas, ne vous inquiétez pas, je ferai de mon mieux pour rendre les choses aussi claires que possible pour vous.

## Comment construire un composant Callout pour votre blog

L'approche que nous allons utiliser consiste à avoir un **composant parent** qui gérera tout le rendu pour la boîte de callout : le type, l'icône, le texte et le style.

Ce qui suivra, ce sont les composants respectifs qui indiquent une note, un conseil, une mise en garde, une erreur et d'autres boîtes de callout.

Voici un diagramme qui simplifie l'approche :

![Callout parent and children components diagram](https://cdn.hashnode.com/res/hashnode/image/upload/v1728934365025/93fe73ce-5781-47bd-a9f1-02519c22776a.png align="center")

Chacun des composants enfants est ce que vous allez utiliser chaque fois que vous voulez afficher un callout lié à eux.

Pour commencer, créez un dossier, nommez-le comme vous voulez (je l'appelle astro-callout de mon côté), et installez Astro.

Ce qui suit est une série de prompts. Voici les choix que j'ai faits pendant les prompts :

![Astro installation prompt choices](https://cdn.hashnode.com/res/hashnode/image/upload/v1728899147064/9d3f33ba-5b56-44de-a700-b3652fbefaec.png align="center")

Voici à quoi ressemble la structure du dossier du projet après avoir installé Astro et choisi le modèle de blog :

![Astro blog template folder structure](https://cdn.hashnode.com/res/hashnode/image/upload/v1728899305440/93267555-d761-4759-b666-037c9ff13738.png align="center")

### Comment construire le composant parent `Callout`.

Rendez-vous dans le répertoire `src/component` et créez un dossier nommé `callout`. Ensuite, à l'intérieur du dossier, créez un fichier `Callout.astro`.

Le composant callout est un élément `aside` qui prendra les props suivantes :

* `type` : le type de callout (note, caution, error, tip, et autres)

* `icon` : l'icône qui signifiera le type de callout. Cela pourrait être un emoji ou une icône d'une bibliothèque d'icônes.

* `backgroundColor` : la couleur de fond différente de chaque type de callout

* `borderLeftColor` : la couleur de la bordure gauche de chaque type de callout

Destructurez ces props à partir de `Astro.props` dans le bloc de code du composant `Callout.astro` :

```javascript
const { icon, type, backgroundColor, borderLeftColor } = Astro.props
```

N'oubliez pas que l'élément `aside` doit également avoir un contenu textuel. Astro a un moyen de gérer cela en utilisant l'élément `<slot />`.

`<slot />` vous permet d'insérer du contenu enfant écrit entre les balises d'ouverture et de fermeture dans n'importe quel composant.

Voici comment j'ai rempli tout dans l'élément `aside` :

```xml
<aside
 class="callout-box"
 style={{backgroundColor, borderLeftColor}}
 >
 <div class="callout-icon-and-type">
   {icon}
   {type}
 </div>
 <div class="callout-content">
  <slot />
 </div>
</aside>
```

La prop `icon` remplace toute icône que vous souhaitez utiliser, qu'il s'agisse d'un emoji ou d'une bibliothèque d'icônes comme Ionicons ou Font Awesome.

Le problème est que tous les emojis ne seront pas rendus de manière présentable, car différents systèmes d'exploitation rendent les emojis à leur manière. Vous devez donc trouver un moyen d'accepter à la fois les emojis et une bibliothèque d'icônes.

La bibliothèque d'icônes que j'ai choisie pour ce projet est ionicons. Allez dans le fichier de mise en page (dans ce cas `layouts/BlogPost.astro`) et insérez les scripts suivants juste avant la balise de fermeture du body :

```xml
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
```

Voici la fonction qui vous permettra de rendre une icône, qu'il s'agisse d'un emoji ou d'une icône ionicons :

```javascript
function renderIcon(icon:any) {
 if (typeof icon === 'string') {
   return icon;
 } else if (typeof icon === 'object' && icon.name) {
   return `<ion-icon name="${icon.name}"></ion-icon>`;
 }
 return '';
}
```

Cette fonction vérifie si l'`icon` que vous passez est un emoji ou une icône de la bibliothèque Ionicons.

Un emoji correspond à une chaîne. Donc, si vous passez un emoji, l'`icon` est retourné. Si vous passez une icône de la bibliothèque Ionicons, la fonction recherchera le nom de l'icône et affichera cette icône.

Vous devez modifier légèrement le contenu de l'élément `aside` pour que l'icône soit rendue de la bonne manière :

```xml
<aside
 class="callout-box"
 style={{backgroundColor, borderLeftColor}}
 >
 <div class="callout-icon-and-type">
   <!-- Nouveau rendu d'icône -->
   <Fragment set:html={renderIcon(icon)} />
   {type}
 </div>
 <div class="callout-content">
  <slot />
 </div>
</aside>
```

Si vous vous demandez ce qu'est `set:html`, c'est un répertoire de modèle Astro similaire au `element.innerHTML` de JavaScript.

Le composant `Fragment` lui-même est un composant que vous pouvez utiliser avec les directives `set:*` pour rendre le contenu HTML.

Voici le CSS pour le composant `Callout` :

```xml
<style>
 .callout-box {
   color: #fff;
   flex-direction: column;
   padding: 1rem;
   border-left-width: 4px;
   border-left-style: solid;
   margin: 1.5rem 0;
   border-top-right-radius: 4px;
   border-bottom-right-radius: 4px;
 }

 .callout-icon-and-type {
   font-size: 1.5rem;
   display: flex;
   gap: 0.4rem;
 }

 .icon {
   margin-right: 4rem;
 }

 .callout-content {
   font-size: 1.2rem;
 }
</style>
```

Cela aura plus de sens lorsque nous commencerons à utiliser le composant parent `Callout` dans les composants enfants de callout.

### Comment construire les composants enfants Callout

Démontrons comment faire cela avec un exemple de boîte de callout de note.

Créez un fichier `NoteCallout.astro` à l'intérieur du répertoire `components/callout`.

Importez le composant parent `Callout` à l'intérieur du bloc de code du fichier `NoteCallout.astro` :

```javascript
import CallOutBox from "./Callout.astro";
```

Pour rendre les choses moins confuses, vous pouvez renommer CalloutBox en `NoteCalloutBox` :

```javascript
import NoteCallOutBox from "./Callout.astro";
```

Après cela, utilisez le `NoteCalloutBox` comme une balise et passez toutes les props que le composant parent `Callout` accepte :

```xml
<NoteCallOutBox
 icon='<ion-icon style="color: #3347ff;" size="large" name="information-circle"></ion-icon>'
 type="Note"
 backgroundColor="#171d4f"
 borderLeftColor="#3347ff"
>

</NoteCallOutBox>
```

Pour tenir compte du contenu du NoteCalloutBox à passer lorsqu'il est finalement utilisé, passez `<slot />` comme contenu du `NoteCallOutBox` :

```xml
<NoteCallOutBox
 icon='<ion-icon style="color: #3347ff;" size="large" name="information-circle"></ion-icon>'
 type="Note"
 backgroundColor="#171d4f"
 borderLeftColor="#3347ff"
>
 <slot />
</NoteCallOutBox>
```

Vous pouvez suivre ce processus pour créer des composants enfants de callout d'erreur, de mise en garde, d'avertissement et de conseil. Tout ce que vous avez à faire est de remplir les valeurs de props appropriées.

## Comment utiliser les composants enfants Callout

Pour utiliser les composants enfants de callout dans un fichier MDX par exemple, importez le `NoteCallout` :

```javascript
import NoteCallout from '../../components/callout/NoteCallout.astro';
```

Ensuite, utilisez-le comme une balise et passez la note que vous voulez communiquer à l'utilisateur :

```xml
<NoteCallout>
 Vous ne pouvez utiliser ce composant que dans un fichier MDX, pas dans un fichier Markdown régulier
 avec une extension .md.
</NoteCallout>
```

Voici le résultat dans le navigateur :

![NoteCallout component](https://cdn.hashnode.com/res/hashnode/image/upload/v1728899862999/7c6624f9-5d29-44eb-b283-f57e31663ee8.png align="center")

Voici d'autres composants enfants que j'ai créés en utilisant la même approche :

![Caution, Tip, Error, and Success Callout components](https://cdn.hashnode.com/res/hashnode/image/upload/v1728899912952/5c19e264-fed6-483f-94b9-afd2b761424a.png align="center")

## Conclusion

J'espère que cet article vous a montré tout ce dont vous avez besoin pour construire un composant callout pour votre blog.

N'oubliez pas que vous pouvez utiliser la même technique pour construire un callout pour un blog construit avec un autre framework frontend.

Si vous trouvez l'article utile, vous pouvez lire plus d'articles comme celui-ci sur [mon blog](https://www.koladechris.com/blog). J'ai également des articles sur PHP, JavaScript, React, Python, et plus encore.

Continuez à coder...