---
title: React 18 Nouveautés – Rendu Concurrent, Regroupement Automatique, et Plus
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2022-04-14T21:58:00.000Z'
originalURL: https://freecodecamp.org/news/react-18-new-features
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/featured.jpg
tags:
- name: features
  slug: features
- name: React
  slug: react
- name: 'update '
  slug: update
seo_title: React 18 Nouveautés – Rendu Concurrent, Regroupement Automatique, et Plus
seo_desc: "React 18 was released in March 2022. This release focuses on performance\
  \ improvements and updating the rendering engine. \nReact 18 sets the foundation\
  \ for concurrent rendering APIs that future React features will be built on top\
  \ of. \nIn this tutorial..."
---

React 18 a été publié en mars 2022. Cette version se concentre sur les améliorations de performance et la mise à jour du moteur de rendu. 

React 18 pose les bases des API de rendu concurrent sur lesquelles les futures fonctionnalités de React seront construites. 

Dans ce tutoriel, je vais donner un guide rapide des fonctionnalités publiées dans React 18, et expliquer quelques concepts majeurs tels que le rendu concurrent, le regroupement automatique et les transitions.

### Guide Rapide des Fonctionnalités de React 18

<table>
<thead>
<tr>
<th>Catégorie</th>
<th>Fonctionnalité</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concept</td>
<td>React Concurrent</td>
</tr>
<tr>
<td>Fonctionnalités</td>
<td>Regroupement Automatique, Transitions, Suspense sur le serveur</td>
</tr>
<tr>
<td>APIs</td>
<td>createRoot, hydrateRoot, renderToPipeableStream, renderToReadableStream</td>
</tr>
<tr>
<td>Hooks</td>
<td>useId, useTransition, useDeferredValue, useSyncExternalStore, useInsertionEffect</td>
</tr>
<tr>
<td>Mises à jour</td>
<td>Mode Strict</td>
</tr>
<tr>
<td>Obsolète/découragé</td>
<td>ReactDOM.render, renderToString</td>
</tr>
</tbody>
</table>

Maintenant, examinons chacune de ces mises à jour plus en détail. Mais d'abord, si vous ne l'avez pas déjà fait, apprenons comment mettre à jour React.

## Comment passer à React 18

Installez React 18 et React DOM depuis npm ou yarn, comme ceci :

`npm install react react-dom`

Ensuite, vous voudrez utiliser `createRoot` au lieu de `render`.

Dans votre index.js, mettez à jour `ReactDOM.render` vers `ReactDOM.createRoot` pour créer une racine, et rendez votre application en utilisant root.

Voici à quoi cela ressemblerait dans React 17 :

```jsx
import ReactDOM from 'react-dom';
import App from 'App';

const container = document.getElementById('app');

ReactDOM.render(<App />, container);

```

Et voici à quoi cela ressemble dans React 18 :

```jsx
import ReactDOM from 'react-dom';
import App from 'App';

const container = document.getElementById('app');

// créer une racine
const root = ReactDOM.createRoot(container);

// rendre l'application à la racine
root.render(<App />);

```

## Concurrence dans React 18

Pour comprendre la concurrence, considérons [cet exemple](https://github.com/reactwg/react-18/discussions/46) de Dan Abramov issu des discussions du groupe de travail React 18.

Supposons que nous devons appeler deux personnes – Alice et Bob. Dans un contexte non concurrent, nous ne pouvons avoir qu'un seul appel à la fois. Nous appellerions d'abord Alice, mettrions fin à l'appel, puis appellerions Bob. 

Cela va bien lorsque les appels sont courts, mais si l'appel avec Alice a une longue période d'attente (comme une mise en attente), cela peut être une perte de temps.

![Appel non concurrent](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/io6s64j30dt3na6yxzp4.png)
_Image montrant que dans une conversation téléphonique non concurrente typique, vous devez attendre qu'un appel soit terminé avant de commencer un nouvel appel._

Dans un contexte concurrent, nous pourrions appeler Alice et, une fois mis en attente, nous pourrions alors appeler Bob. 

Cela ne signifie pas que nous parlons à deux personnes en même temps. Cela signifie simplement que nous pouvons avoir deux appels ou plus simultanément et décider quel appel est le plus important.

![Appel concurrent](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v4zgvausl6go1ur769cd.png)
_Image montrant une conversation téléphonique entre Alice et Bob qui peut être concurrente, en mettant un appel en attente et en répondant à un appel plus urgent avec Bob en premier._

De même, dans React 18 avec le rendu concurrent, React peut interrompre, mettre en pause, reprendre ou abandonner un rendu. Cela permet à React de répondre rapidement à l'interaction de l'utilisateur même s'il est au milieu d'une tâche de rendu lourde. 

Avant React 18, le rendu était une transaction unique, ininterrompue et synchrone, et une fois le rendu commencé, il ne pouvait pas être interrompu.

La concurrence est une mise à jour fondamentale du mécanisme de rendu de React. La concurrence permet à React d'interrompre le rendu. 

React 18 introduit les bases du rendu concurrent et de nouvelles fonctionnalités telles que suspense, le rendu serveur en streaming, et les transitions sont alimentées par le rendu concurrent.

## Nouvelles Fonctionnalités de React 18

### Regroupement Automatique

React 18 propose le regroupement automatique. Pour comprendre le regroupement, considérons l'exemple des courses issu de la [même discussion du groupe de travail React](https://github.com/reactwg/react-18/discussions/46#discussioncomment-846694). 

Supposons que vous préparez des pâtes pour le dîner. Si vous deviez optimiser votre voyage à l'épicerie, vous créeriez une liste de tous les ingrédients dont vous avez besoin, iriez à l'épicerie, et obtiendriez tous vos ingrédients en un seul voyage. 

C'est le regroupement. Sans regroupement, vous commenceriez à cuisiner, vous rendriez compte que vous avez besoin d'un ingrédient, iriez à l'épicerie et achèteriez l'ingrédient, reviendriez et continueriez à cuisiner, pour vous rendre compte que vous avez besoin d'un autre ingrédient, iriez à l'épicerie... et vous rendriez fou.

Dans React, le regroupement aide à réduire le nombre de re-rendus qui se produisent lorsqu'un état change, lorsque vous appelez `setState`. Auparavant, React regroupait les mises à jour d'état dans les gestionnaires d'événements, par exemple :

```jsx
const handleClick = () => {
setCounter();
setActive();
setValue();
}

// re-rendu une fois à la fin.

```

Cependant, les mises à jour d'état qui se produisaient en dehors des gestionnaires d'événements n'étaient pas regroupées. Par exemple, si vous aviez une promesse ou si vous faisiez un appel réseau, les mises à jour d'état ne seraient pas regroupées. Comme ceci :

```jsx
fetch('/network').then( () => {
setCounter(); // re-rendu 1 fois
setActive();  // re-rendu 2 fois
setValue();   // re-rendu 3 fois
});

// Total 3 re-rendus

```

Comme vous pouvez le constater, ce n'est pas performant. React 18 introduit le regroupement automatique qui permet à toutes les mises à jour d'état – même au sein des promesses, des setTimeouts et des rappels d'événements – d'être regroupées. Cela réduit considérablement le travail que React doit faire en arrière-plan. React attendra qu'une micro-tâche soit terminée avant de re-rendre.

Le regroupement automatique est disponible directement dans React, mais si vous souhaitez vous désinscrire, vous pouvez utiliser `flushSync`.

### Transitions

Les transitions peuvent être utilisées pour marquer les mises à jour de l'interface utilisateur qui n'ont pas besoin de ressources urgentes pour la mise à jour. 

Par exemple, lors de la saisie dans un champ de typeahead, deux choses se produisent : un curseur clignotant qui montre un retour visuel de votre contenu en cours de saisie, et une fonctionnalité de recherche en arrière-plan qui recherche les données saisies.

Montrer un retour visuel à l'utilisateur est important et donc urgent. La recherche n'est pas si urgente, et peut donc être marquée comme non urgente. 

Ces mises à jour non urgentes sont appelées transitions. En marquant les mises à jour non urgentes de l'interface utilisateur comme "transitions", React saura quelles mises à jour prioriser. Cela facilite l'optimisation du rendu et l'élimination du rendu obsolète.

Vous pouvez marquer les mises à jour comme non urgentes en utilisant `startTransition`. Voici un exemple de ce à quoi ressemblerait un composant typeahead lorsqu'il est marqué avec des transitions :

```jsx
import { startTransition } from 'react';

// Urgent : Montrer ce qui a été saisi
setInputValue(input);

// Marquer les mises à jour d'état non urgentes à l'intérieur comme transitions
startTransition(() => {
  // Transition : Montrer les résultats
  setSearchQuery(input);
});

```

#### En quoi les transitions sont-elles différentes du debouncing ou du setTimeout ?

1. startTransition s'exécute immédiatement, contrairement à setTimeout.
2. setTimeout a un délai garanti, alors que le délai de startTransition dépend de la vitesse de l'appareil et d'autres rendus urgents.
3. Les mises à jour de startTransition peuvent être interrompues contrairement à setTimeout et ne gèleront pas la page.
4. React peut suivre l'état en attente pour vous lorsqu'il est marqué avec startTransition.

### Suspense sur le serveur

React 18 introduit :

1. Le fractionnement de code sur le serveur avec suspense
2. Le rendu en streaming sur le serveur

#### Rendu côté client vs rendu côté serveur

Dans une application rendue côté client, vous chargez le HTML de votre page depuis le serveur ainsi que tout le JavaScript nécessaire pour exécuter la page et la rendre interactive. 

Cependant, si votre bundle JavaScript est énorme, ou si vous avez une connexion lente, ce processus peut prendre beaucoup de temps et l'utilisateur devra attendre que la page devienne interactive, ou voir un contenu significatif.

![Illustration du flux de rendu côté client. Source : React Conf 2021 Streaming Server Rendering with Suspense par Shaundai Person https://www.youtube.com/watch?v=pj5N-Khihgc](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ccfllg117u8ycgnl5mv7.png)
_Dans un flux de rendu côté client, un utilisateur doit attendre longtemps avant que la page ne devienne interactive. [Source](https://www.youtube.com/watch?v=pj5N-Khihgc) : React Conf 2021 **Streaming Server Rendering with Suspense** par Shaundai Person_

Pour optimiser l'expérience utilisateur et éviter que l'utilisateur ne doive attendre devant un écran vide, nous pouvons utiliser le rendu côté serveur. 

Le rendu côté serveur est une technique où vous rendez la sortie HTML de vos composants React sur le serveur et envoyez le HTML depuis le serveur. Cela permet à l'utilisateur de voir une partie de l'interface utilisateur pendant que les bundles JS se chargent et avant que l'application ne devienne interactive. 

Pour un aperçu détaillé du rendu côté client vs côté serveur, [consultez la conférence de Shaundai Person à React Conf 2021](https://www.youtube.com/watch?v=pj5N-Khihgc).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/4.jpeg)
_Dans un flux de rendu côté serveur, nous pouvons afficher des données significatives à l'utilisateur beaucoup plus rapidement en envoyant du HTML depuis le serveur. [Source](https://www.youtube.com/watch?v=pj5N-Khihgc) : React Conf 2021 **Streaming Server Rendering with Suspense** par Shaundai Person_

Le rendu côté serveur améliore davantage l'expérience utilisateur de chargement de la page et réduit le temps d'interactivité.

Maintenant, que se passe-t-il si la plupart de votre application est rapide sauf une partie ? Peut-être que cette partie charge des données lentement, ou peut-être qu'elle doit télécharger beaucoup de JS avant de devenir interactive.

Avant React 18, cette partie était souvent le goulot d'étranglement de l'application, et augmentait le temps nécessaire pour rendre le composant. 

Un composant lent peut ralentir toute la page. Cela est dû au fait que le rendu côté serveur était tout ou rien – vous ne pouviez pas dire à React de différer le chargement d'un composant lent et ne pouviez pas dire à React d'envoyer du HTML pour d'autres composants.

React 18 ajoute la prise en charge de Suspense sur le serveur. Avec l'aide de suspense, vous pouvez envelopper une partie lente de votre application dans le composant Suspense, indiquant à React de retarder le chargement du composant lent. Cela peut également être utilisé pour spécifier un état de chargement qui peut être affiché pendant son chargement.

Dans React 18, un composant lent n'a pas à ralentir le rendu de toute votre application. Avec Suspense, vous pouvez dire à React d'envoyer du HTML pour d'autres composants en premier, ainsi que le HTML pour le placeholder, comme un spinner de chargement. Ensuite, lorsque le composant lent est prêt et a récupéré ses données, le rendu serveur insérera son HTML dans le même flux.

![Vous pouvez ajouter suspense à un composant rendu côté serveur lent dans React 18](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/taxrh7y9ylx0l68u2btx.png)
_Image montrant que suspense sur le serveur peut permettre à un composant lent d'afficher un état de chargement tandis que les autres sont entièrement rendus._

De cette façon, l'utilisateur peut voir le squelette de la page le plus tôt possible et le voir révéler progressivement plus de contenu à mesure que d'autres morceaux de HTML arrivent. 

Tout cela se produit avant que le JS ou React ne se charge sur la page, ce qui améliore considérablement l'expérience utilisateur et la latence perçue par l'utilisateur.

### Mode Strict

Le mode strict dans React 18 simulera le montage, le démontage et le re-montage du composant avec un état précédent. Cela pose les bases pour un état réutilisable à l'avenir où React pourra immédiatement monter un écran précédent en remontant des arbres en utilisant le même état de composant avant le démontage. 

Le mode strict garantira que les composants sont résilients aux effets étant montés et démontés plusieurs fois.

## Conclusion

En résumé, React 18 pose les bases des futures versions et se concentre sur l'amélioration de l'expérience utilisateur. 

La mise à niveau vers React 18 devrait être simple et votre code existant ne devrait pas se casser après la mise à jour. Le processus de mise à niveau ne devrait pas prendre plus d'un après-midi. 

Essayez-le et faites-moi savoir ce que vous en pensez !

Sources :

1. [React RFC](https://github.com/reactjs/rfcs/blob/react-18/text/0000-react-18.md)
2. [Mon précédent article sur React 18](https://dev.to/shrutikapoor08/what-s-new-in-react-18-1713)
3. [Blog React V18](https://reactjs.org/blog/2022/03/29/react-v18.html)
4. [React Conf 2021 - React pour les développeurs d'applications](https://www.youtube.com/watch?v=ytudH8je5ko)
5. [React Conf 2021 - Streaming Server Rendering with Suspense](https://www.youtube.com/watch?v=pj5N-Khihgc)

Si vous avez aimé cet article, donnez-lui un ❤️ pour que d'autres puissent le trouver aussi.

* Pour des conseils plus fréquents, [restez en contact sur Twitter](http://twitter.com/shrutikapoor08)
* [Vous voulez des articles comme celui-ci directement dans votre boîte mail ?](http://tinyletter.com/shrutikapoor)