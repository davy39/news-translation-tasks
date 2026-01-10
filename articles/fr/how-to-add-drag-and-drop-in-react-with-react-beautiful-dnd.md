---
title: Comment ajouter le glisser-déposer dans React avec React Beautiful DnD
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-10-05T16:38:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-drag-and-drop-in-react-with-react-beautiful-dnd
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/drag-and-drop-1.jpg
tags:
- name: React
  slug: react
- name: user experience
  slug: user-experience
- name: ux design
  slug: ux-design
seo_title: Comment ajouter le glisser-déposer dans React avec React Beautiful DnD
seo_desc: "Drag and Drop is a common interaction technique added to allow people to\
  \ intuitively move things around on a page. This could be reordering a list or even\
  \ putting together a puzzle. \nHow can we add that interaction when building a React\
  \ app with Reac..."
---

Le glisser-déposer est une technique d'interaction courante ajoutée pour permettre aux gens de déplacer intuitivement des éléments sur une page. Cela peut consister à réorganiser une liste ou même à assembler un puzzle. 

Comment pouvons-nous ajouter cette interaction lors de la création d'une application React avec React Beautiful DnD ?

* [Qu'est-ce que le glisser-déposer ?](#heading-quest-ce-que-le-glisser-deposer)
* [Qu'est-ce que React Beautiful DnD ?](#heading-quest-ce-que-react-beautiful-dnd)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Créer une nouvelle application React.js](#heading-etape-0-creer-une-nouvelle-application-reactjs)
* [Étape 1 : Installer React Beautiful DnD](#heading-etape-1-installer-react-beautiful-dnd)
* [Étape 2 : Rendre une liste glissable et déposable avec React Beautiful DnD](#heading-etape-2-rendre-une-liste-glissable-et-deposable-avec-react-beautiful-dnd)
* [Étape 3 : Enregistrer l'ordre de la liste après avoir réorganisé les éléments avec React Beautiful DnD](#heading-etape-3-enregistrer-lordre-de-la-liste-apres-avoir-reorganise-les-elements-avec-react-beautiful-dnd)

%[https://www.youtube.com/watch?v=aYZRRyukuIw]

## Qu'est-ce que le glisser-déposer ?

Le glisser-déposer est exactement ce à quoi cela ressemble — c'est une interaction permettant à quelqu'un de cliquer et de faire glisser un élément, puis de le déposer ailleurs, ayant souvent un effet secondaire dans l'application.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/react-beautiful-dnd-board.gif)
_Déplacer des éléments sur un tableau_

Cet effet est assez courant dans des applications comme les listes de tâches ou les tableaux de bord de gestion de projet, où vous devez prioriser et créer un ordre pour la façon dont les choses doivent être faites.

Bien que le glisser-déposer puisse avoir des cas d'utilisation avancés, nous nous en tiendrons à la fonctionnalité de liste de base pour notre guide.

## Qu'est-ce que React Beautiful DnD ?

React Beautiful DnD est une bibliothèque de glisser-déposer accessible d'Atlassian. Si vous ne connaissez pas Atlassian, ils sont l'équipe derrière Jira. Si vous n'êtes pas familier avec Jira, c'est probablement le plus grand outil Agile sur internet en ce moment.

Les objectifs de l'équipe étaient de fournir des capacités de glisser-déposer en gardant à l'esprit l'accessibilité, en plus de le garder léger et performant avec une API puissante.

## Que allons-nous construire ?

Nous allons commencer avec une simple liste et ajouter la capacité de glisser-déposer.

Dans ce guide, nous ne passerons pas de temps à construire la liste elle-même. La liste que nous utiliserons utilise une liste non ordonnée standard (`<ul>`) et des éléments de liste (`<li>`) pour créer une liste avec un peu de CSS pour la faire ressembler à des cartes.

Nous nous concentrerons sur l'ajout de la capacité de glisser-déposer pour réorganiser la liste en utilisant React Beautiful DnD.

## Étape 0 : Créer une nouvelle application React.js

Pour commencer, nous voulons une application simple qui inclut une liste d'éléments. Cela peut être un projet existant ou un tout nouveau projet utilisant votre framework préféré comme [Create React App](https://create-react-app.dev/).

J'ai commencé avec une nouvelle application en utilisant Create React App et j'ai ajouté une simple liste de personnages de [Final Space](https://www.tbs.com/shows/final-space).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/list-of-final-space-characters-1.jpg)
_Liste des personnages de Final Space_

Si vous voulez commencer au même endroit, vous pouvez cloner mon dépôt de démonstration à cette branche et commencer directement avec moi.

Cette commande clonera [la branche spécifique](https://github.com/colbyfayock/my-final-space-characters/tree/part-0-starting-point) pour commencer :

```
git clone --single-branch --branch part-0-starting-point git@github.com:colbyfayock/my-final-space-characters.git

```

Sinon, vous pouvez cloner [le dépôt](https://github.com/colbyfayock/my-final-space-characters) normalement et consulter la branche `part-0-starting-point`.

Si vous voulez suivre juste le code, j'ai d'abord créé un tableau d'objets :

``` js
const finalSpaceCharacters = [
  {
    id: 'gary',
    name: 'Gary Goodspeed',
    thumb: '/images/gary.png'
  },
  ...

```

Et ensuite, j'ai bouclé à travers eux pour créer ma liste :

```
<ul className="characters">
  {finalSpaceCharacters.map(({id, name, thumb}) => {
    return (
      <li key={id}>
        <div className="characters-thumb">
          <img src={thumb} alt={`${name} Thumb`} />
        </div>
        <p>
          { name }
        </p>
      </li>
    );
  })}
</ul>

```

[Suivez avec le commit !](https://github.com/colbyfayock/my-final-space-characters/commit/8bfa61c32c1bdace7515a93a14427108056f3814)

## Étape 1 : Installer React Beautiful DnD

La première étape consiste à installer la bibliothèque via npm.

À l'intérieur de votre projet, exécutez ce qui suit :

```
yarn add react-beautiful-dnd
# ou
npm install react-beautiful-dnd --save

```

Cela ajoutera la bibliothèque à notre projet et nous serons prêts à l'utiliser dans notre application.

## Étape 2 : Rendre une liste glissable et déposable avec React Beautiful DnD

Avec notre bibliothèque installée, nous pouvons donner à notre liste la capacité de glisser-déposer.

### Ajouter le contexte de glisser-déposer à notre application

En haut du fichier, importez `DragDropContext` de la bibliothèque avec :

```jsx
import { DragDropContext } from 'react-beautiful-dnd';

```

[DragDropContext](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/drag-drop-context.md) va donner à notre application la capacité d'utiliser la bibliothèque. Il fonctionne de manière similaire à l'API de contexte de React, où la bibliothèque peut maintenant avoir accès à l'arborescence des composants.

_Note : Si vous prévoyez d'ajouter le glisser-déposer à plus d'une liste, vous devez vous assurer que votre DragDropContext enveloppe tous ces éléments, comme à la racine de votre application. Vous ne pouvez pas imbriquer DragDropContext._

Nous voudrons envelopper notre liste avec DragDropContext :

```jsx
<DragDropContext>
  <ul className="characters">
  ...
</DragDropContext>

```

À ce stade, rien n'aura changé avec l'application et elle devrait encore se charger comme avant.

### Faire de notre liste une zone déposable

Ensuite, nous voulons créer une zone déposable, ce qui signifie que cela nous permettra de fournir une zone spécifique où nos éléments peuvent être déplacés à l'intérieur.

Tout d'abord, ajoutez `Droppable` à notre import en haut du fichier :

```js
import { DragDropContext, Droppable } from 'react-beautiful-dnd';

```

Pour notre usage, nous voulons que notre liste non ordonnée entière (`<ul>`) soit notre zone de dépôt, donc nous voudrons à nouveau l'envelopper avec ce composant :

```jsx
<DragDropContext>
  <Droppable droppableId="characters">
    {(provided) => (
      <ul className="characters">
        ...
      </ul>
    )}
  </Droppable>
</DragDropContext>

```

Vous remarquerez que nous l'avons enveloppé un peu différemment cette fois-ci. Tout d'abord, nous avons défini un `droppableId` sur notre composant `<Droppable>`. Cela permet à la bibliothèque de suivre cette instance spécifique entre les interactions.

Nous créons également une fonction immédiatement à l'intérieur de ce composant qui passe l'argument `provided`.

Note : Cette fonction peut passer deux arguments incluant un argument `snapshot`, mais nous ne l'utiliserons pas dans cet exemple.

L'argument [provided](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/droppable.md#1-provided-droppableprovided) inclut des informations et des références au code dont la bibliothèque a besoin pour fonctionner correctement.

Pour l'utiliser, sur notre élément de liste, ajoutons :

```jsx
<ul className="characters" {...provided.droppableProps} ref={provided.innerRef}>

```

Cela va créer une référence (`provided.innerRef`) pour que la bibliothèque accède à l'élément HTML de l'élément de liste. Elle applique également des props à l'élément (`provided.droppableProps`) qui permet à la bibliothèque de suivre les mouvements et le positionnement.

À nouveau, à ce stade, il n'y aura aucune fonctionnalité noticeable.

### Rendre nos éléments glissables

Maintenant, la partie amusante !

La dernière étape pour rendre nos éléments de liste glissables et déposables est d'envelopper chaque élément de liste avec un composant similaire à ce que nous venons de faire avec la liste entière.

Nous utiliserons le composant [Draggable](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md), qui, de manière similaire au composant Droppable, inclura une fonction où nous passerons des props à nos composants d'éléments de liste.

Tout d'abord, nous devons importer Draggable avec le reste des composants.

```
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

```

Ensuite, à l'intérieur de notre boucle, enveloppons l'élément de liste retourné avec le composant `<Draggable />` et sa fonction de niveau supérieur.

```jsx
{finalSpaceCharacters.map(({id, name, thumb}) => {
  return (
    <Draggable>
      {(provided) => (
        <li key={id}>
          ...
        </li>
      )}
    </Draggable>

```

Parce que nous avons maintenant un nouveau composant de niveau supérieur dans notre boucle, déplaçons la prop `key` de l'élément de liste à Draggable :

```jsx
{finalSpaceCharacters.map(({id, name, thumb}) => {
  return (
    <Draggable key={id}>
      {(provided) => (
        <li>

```

Nous devons également définir deux props supplémentaires sur `<Draggable>`, un `draggableId` et un `index`.

Nous voudrons ajouter `index` comme argument dans notre fonction `map` puis inclure ces props sur notre composant :

```jsx
{finalSpaceCharacters.map(({id, name, thumb}, index) => {
  return (
    <Draggable key={id} draggableId={id} index={index}>

```

Enfin, nous devons définir quelques props sur l'élément de liste lui-même.

Sur notre élément de liste, ajoutons cette `ref` et étalons des props supplémentaires de l'argument `provided` :

```jsx
<Draggable key={id} draggableId={id} index={index}>
  {(provided) => (
    <li ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>

```

Maintenant, si nous actualisons notre page et survolons nos éléments de liste, nous pouvons maintenant les faire glisser !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-items-revert-state-1.gif)
_Déplacer des éléments sur une liste_

Cependant, vous remarquerez que lorsque vous commencez à déplacer un élément, le bas de la page semble un peu désordonné. Il y a des problèmes de débordement avec nos éléments de liste et notre pied de page.

Vous remarquerez également que dans la console de développement, React Beautiful DnD nous donne un message d'avertissement indiquant qu'il manque quelque chose appelé un placeholder.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/react-beautiful-dnd-warning-placeholder.jpg)
_Avertissement de la console - le placeholder n'a pas pu être trouvé_

### Ajouter un placeholder de React Beautiful DnD

Une partie des exigences de React Beautiful DnD est que nous incluions également un élément placeholder.

C'est quelque chose qu'ils fournissent prêt à l'emploi, mais cela est utilisé pour remplir l'espace que l'élément que nous faisons glisser occupait précédemment.

Pour l'ajouter, nous voulons inclure `provided.placeholder` en bas de notre composant de liste de niveau supérieur Droppable, dans notre cas en bas du `<ul>` :

```jsx
<Droppable droppableId="characters">
  {(provided) => (
    <ul className="characters" {...provided.droppableProps} ref={provided.innerRef}>
      ...
      {provided.placeholder}
    </ul>
  )}
</Droppable>

```

Et si nous commençons à déplacer des choses dans notre navigateur, nous pouvons voir que notre flux de page n'a pas de problèmes et que le contenu reste où il devrait être !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-items-revert-fixed-spacing.gif)
_Déplacer des éléments avec un espacement fixe_

Le dernier problème, cependant, est que lorsque vous déplacez quelque chose, cela ne reste pas, alors comment pouvons-nous enregistrer l'ordre de nos éléments ?

[Suivez avec le commit !](https://github.com/colbyfayock/my-final-space-characters/commit/5ec5ee6c3e7de5b67a8fd46fdfbf157312bc8c00)

## Étape 3 : Enregistrer l'ordre de la liste après avoir réorganisé les éléments avec React Beautiful DnD

Lorsque nous déplaçons nos éléments, ils restent où ils atterrissent pendant une fraction de seconde. Mais après que React Beautiful DnD ait terminé son travail, notre arborescence de composants se rerend.

Lorsque les composants se rerendent, nos éléments retournent au même endroit qu'avant, car nous n'avons jamais enregistré cela en dehors de la mémoire de DnD.

Pour résoudre ce problème, `DragDropContext` prend en charge une prop `onDragEnd` qui nous permettra d'exécuter une fonction après que le glisser-déposer soit terminé. Cette fonction passe des arguments qui incluent le nouvel ordre de nos éléments afin que nous puissions mettre à jour notre état pour le prochain cycle de rendu.

### Enregistrer nos éléments de liste dans l'état

Tout d'abord, stockons nos éléments dans l'état afin que nous ayons quelque chose à mettre à jour entre les cycles.

En haut du fichier, ajoutez `useState` à l'import de React :

```
import React, { useState } from 'react';

```

Ensuite, nous allons créer notre état en utilisant notre liste d'éléments par défaut.

Ajoutez ce qui suit en haut de notre composant App :

```js
const [characters, updateCharacters] = useState(finalSpaceCharacters);

```

Parce que nous allons mettre à jour notre nouvel état `characters` pour fournir nos éléments de liste et leur ordre, nous allons maintenant vouloir remplacer le tableau que nous parcourons par notre nouvel état :

```jsx
<ul className="characters" {...provided.droppableProps} ref={provided.innerRef}>
  {characters(({id, name, thumb}, index) => {

```

Et si nous enregistrons et actualisons notre page, rien ne devrait changer !

### Mettre à jour l'état lors du glisser-déposer des éléments

Maintenant que nous avons notre état, nous pouvons mettre à jour cet état chaque fois que nos éléments de liste sont glissés.

Le composant `DragDropContext` que nous avons ajouté à notre page prend en charge une prop `onDragEnd`. Comme son nom l'indique, cela déclenchera une fonction chaque fois que quelqu'un arrête de faire glisser un élément dans la liste.

Ajoutons une fonction `handleOnDragEnd` comme notre prop :

```
<DragDropContext onDragEnd={handleOnDragEnd}>

```

Ensuite, nous avons besoin que cette fonction existe réellement.

Nous pouvons définir une fonction sous notre état :

```js
function handleOnDragEnd(result) {
}

```

Notre fonction prend un argument appelé `result`.

Si nous ajoutons `console.log(result)` à la fonction et déplaçons un élément dans notre liste, nous pouvons voir qu'il inclut des détails sur ce qui devrait être l'état mis à jour après notre action de déplacement.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/react-beautiful-dnd-ondragend-result.jpg)
_Résultat de l'élément glissé_

En particulier, nous voulons utiliser la valeur `index` dans les propriétés `destination` et `source`, qui nous indiquent l'index de l'élément déplacé et quel devrait être le nouvel index de cet élément dans le tableau des éléments.

Alors, en utilisant cela, ajoutons ce qui suit à notre fonction :

```js
const items = Array.from(characters);
const [reorderedItem] = items.splice(result.source.index, 1);
items.splice(result.destination.index, 0, reorderedItem);

updateCharacters(items);

```

Voici ce que nous faisons :

* Nous créons une nouvelle copie de notre tableau `characters`
* Nous utilisons la valeur `source.index` pour trouver notre élément dans notre nouveau tableau et le supprimer en utilisant la méthode `splice`
* Ce résultat est déstructuré, donc nous obtenons un nouvel objet `reorderedItem` qui est notre élément glissé
* Nous utilisons ensuite notre `destination.index` pour ajouter cet élément à nouveau dans le tableau, mais à son nouvel emplacement, en utilisant à nouveau `splice`
* Enfin, nous mettons à jour notre état `characters` en utilisant la fonction `updateCharacters`

Et maintenant, après avoir enregistré notre fonction, nous pouvons déplacer nos personnages et ils enregistrent leur emplacement !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-drop-save-state.gif)
_Déplacer un élément avec l'état enregistré_

### Prévenir les erreurs de glisser-déposer hors des limites

Un problème avec notre implémentation est que si quelqu'un ne fait pas glisser l'élément exactement dans nos conteneurs définis, nous obtenons une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-out-of-container-error.gif)
_Erreur lors du glisser-déposer hors du conteneur_

Le problème est que lorsque nous le faisons glisser en dehors du conteneur défini, nous n'avons pas de destination.

Pour éviter cela, nous pouvons simplement ajouter une instruction au-dessus du code qui déplace notre élément et qui vérifie si la destination existe, et si elle n'existe pas, sortir de la fonction :

```js
function handleOnDragEnd(result) {
  if (!result.destination) return;

```

Et si nous rechargeons la page et essayons à nouveau de faire glisser notre élément en dehors, notre élément revient à l'emplacement d'origine sans erreur !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-out-of-container-snap-back.gif)
_Retour à l'emplacement d'origine lors du glisser-déposer hors du conteneur_

[Suivez avec le commit !](https://github.com/colbyfayock/my-final-space-characters/commit/ad4f4733a974a27f5a2cfc8e366c2390809b74ca)

## Que pouvons-nous faire d'autre avec React Beautiful DnD ?

### Styles personnalisés lors du glisser-déposer

Lors du déplacement d'éléments, DnD fournira un instantané de l'état donné. Avec ces informations, nous pouvons appliquer des styles personnalisés afin que lorsque nous déplaçons nos éléments, nous puissions montrer un état actif pour la liste, l'élément que nous déplaçons, ou les deux !

[https://react-beautiful-dnd.netlify.app/?path=/story/single-vertical-list--basic](https://react-beautiful-dnd.netlify.app/?path=/story/single-vertical-list--basic)

### Glisser-déposer entre différentes listes

Si vous avez déjà utilisé Trello ou un outil similaire, vous devriez être familier avec le concept de différentes colonnes entre lesquelles vous pouvez faire glisser des cartes afin de prioriser et organiser vos tâches et idées.

Cette bibliothèque vous permet de faire la même chose, offrant la possibilité de faire glisser et déposer des éléments d'une zone glissable à une autre.

[https://react-beautiful-dnd.netlify.app/?path=/story/multiple-vertical-lists--stress-test](https://react-beautiful-dnd.netlify.app/?path=/story/multiple-vertical-lists--stress-test)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4E83FB Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsorisez-moi</a>
    </li>
  </ul>
</div>