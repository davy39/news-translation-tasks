---
title: 'Apprendre la réactivité JavaScript : Comment construire des Signaux à partir
  de zéro'
subtitle: ''
author: Rahul gupta
co_authors: []
series: null
date: '2024-07-18T21:17:44.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-reactivity-build-signals-from-scratch
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727437093214/d99314da-415e-4a4b-8d7e-f00aaf3db9a8.png
tags:
- name: JavaScript
  slug: javascript
seo_title: 'Apprendre la réactivité JavaScript : Comment construire des Signaux à
  partir de zéro'
seo_desc: 'If you''re learning JavaScript, you may have heard the terms reactivity
  or signals. But perhaps you haven''t gotten to use them in practice yet. If so –
  or if you just want to learn more about these concepts – you''re in the right place.

  In this article...'
---

Si vous apprenez JavaScript, vous avez peut-être entendu les termes réactivité ou signaux. Mais peut-être que vous n'avez pas encore eu l'occasion de les utiliser en pratique. Si c'est le cas – ou si vous voulez simplement en apprendre plus sur ces concepts – vous êtes au bon endroit.

Dans cet article, vous apprendrez ce que signifie la réactivité, ce que sont les signaux, puis vous construirez votre propre implémentation de Signaux à partir de zéro.

## Ce que nous allons couvrir

* [Qu'est-ce que la réactivité ?](#heading-quest-ce-que-la-reactivite)
    
* [Qu'est-ce que les signaux ?](#heading-quest-ce-que-les-signaux)
    
* [Comment construire vos propres signaux](#heading-comment-construire-vos-propres-signaux)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que la réactivité ?

Voici une définition générique de la réactivité :

> "La réactivité est la manière dont un système réagit aux changements de données."

Au cœur de la réactivité dans les applications UI, cela fait référence aux changements dans l'UI en réponse aux changements dans les données.

Avoir une compréhension de la manière dont la réactivité fonctionne en coulisses vous donne une compréhension plus approfondie de certains des paradigmes courants que vous utilisez déjà lors du développement d'applications web. Mais cela aide également à approfondir votre compréhension des frameworks/librairies avec lesquels vous travaillez au quotidien et qui utilisent la réactivité sous le capot.

Voici quelques paradigmes courants où la réactivité entre en jeu en coulisses, avec quelques exemples :

* **Réagir aux données récupérées depuis une API** : Afficher des indicateurs de chargement/erreur/succès en fonction de l'état des données en cours de récupération.
    
* **Donnée unique, plusieurs éléments UI réactifs** : Dans un site web de commerce électronique, lorsqu'un article est ajouté au panier, il doit être marqué comme ajouté et le badge du panier doit également s'incrémenter.
    
* **Réagir à l'achèvement d'une tâche** : Afficher une coche lorsque l'utilisateur a terminé le téléchargement d'une image.
    
* **Réagir à des événements** : Afficher une bannière promotionnelle lorsque l'utilisateur est en bas de la page.
    
* **Réactivité en CSS** : Recalculer l'espacement en fonction de la hauteur du composant via `calc(--height)`.
    

Voici quelques frameworks/librairies populaires et comment ils dépendent de la réactivité à leur cœur :

**React** vous permet de sauvegarder des données sous forme d'état via des hooks comme `useState`, chaque fois que cet état change, l'élément UI correspondant où l'état est utilisé est également mis à jour de manière réactive.

Sous le capot, React y parvient en reconstruisant et en comparant le DOM virtuel lorsque certains états sont mis à jour afin qu'il ne met à jour que la partie pertinente de l'élément UI à l'écran.

**RxJS** utilise des observables pour produire des données et des observateurs pour consommer ces données, les notifiant chaque fois que de nouvelles valeurs sont produites. Vous pouvez [en lire plus ici](https://rxjs.dev/guide/observable).

**Vue** utilise des objets et des [proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) pour fournir de la réactivité via `ref()`. Proxy, en résumé, permet à Vue d'intercepter lorsqu'une propriété d'un objet est accédée ou définie, ce qui est la base de son système de réactivité. [Vous pouvez en lire plus ici](https://vuejs.org/guide/extras/reactivity-in-depth.html).

**SolidJS** utilise des *Signaux* pour atteindre une réactivité fine. Cela signifie qu'il peut mettre à jour des parties spécifiques du DOM lorsque les données changent, sans avoir besoin d'un DOM virtuel.

## Qu'est-ce que les signaux ?

Les signaux sont un concept important dans la réactivité en JavaScript. Les signaux peuvent contenir une valeur et permettre à un morceau de code de réagir à celle-ci lorsque cette valeur change.

Les signaux vous permettent de gérer l'état de manière plus contrôlée. Ils permettent également une réactivité fine où les composants peuvent se mettre à jour de manière sélective en fonction des changements d'état spécifiques, plutôt que de se re-rendre entièrement.

Différents frameworks ont leurs propres implémentations de signaux comme je l'ai mentionné précédemment (par exemple, Vue les appelle `ref`, tandis que [Angular](https://angular.io/guide/signals), [Preact](https://preactjs.com/guide/v10/signals/), [Qwik](https://qwik.builder.io/docs/components/state/#usesignal) les appellent signaux) et ils diffèrent légèrement dans leurs implémentations.

Dans cet article, nous allons essayer de reconstruire des signaux à partir de zéro tels qu'ils existent dans le framework [SolidJS](https://docs.solidjs.com/concepts/signals).

### Signaux dans SolidJS

Commençons par comprendre comment fonctionnent les signaux dans SolidJS. Ensuite, nous allons recréer la même chose avec juste JavaScript.

`**createSignal**` est utilisé pour créer un signal, prend `initialValue` comme argument, et retourne une paire de `getter`s et `setter`s. Voici à quoi cela ressemble :

```javascript
const [count, setCount] = createSignal(0);
        ^ Getter   ^ Setter
```

Ici :

* `count()` est utilisé pour accéder à la valeur dans le signal
    
* `setCount(newValue)` est utilisé pour définir une nouvelle valeur dans le signal
    

La fonction `**createEffect**` permet à un code arbitraire ("effets secondaires") d'être réactif et de s'exécuter à nouveau chaque fois que ses dépendances changent. Elle accepte une fonction de rappel et réexécute cette fonction chaque fois que les dépendances du signal accessibles dans le rappel changent.

Contrairement aux [effets dans React](https://react.dev/reference/react/useEffect#useeffect), il n'est pas nécessaire de lister explicitement les dépendances dans un tableau. **createEffect** détermine automatiquement les dépendances du signal en suivant quels getters de signal sont accessibles dans le rappel.

```javascript
const [count, setCount] = createSignal(0);

// S'exécute une fois avec la valeur à ce moment-là
// Affiche 0
console.log(count());

createEffect(() => {
    // Affiche 0
    // Affiche 1
    console.log(count());
});


// Met à jour le compte à 1
setCount(1);
```

Dans l'exemple ci-dessus, le premier `console.log` n'est affiché qu'une seule fois, car SolidJS exécute tout une seule fois, tandis que le rappel dans l'effet s'exécute chaque fois que la valeur du signal "count" est modifiée.

## Comment construire vos propres signaux

Essayons de reconstruire une implémentation plus simple des signaux SolidJS démontrés ci-dessus en les décomposant :

* **Implémenter** la classe `Signal` – qui gère un mécanisme Pub-Sub pour alimenter `createSignal`
    
* **Implémenter** `**createSignal**` – utilise la classe Signal pour implémenter cette fonction, qui doit accepter une valeur initiale et retourner des getters et setters.
    
* **Implémenter** `createEffect` – exécute le rappel fourni une fois, et le réexécute lorsqu'une valeur de signal change
    

### Implémenter la classe `Signal`

Cette classe utilisera le modèle Pub-Sub, ce qui signifie qu'elle doit :

* Maintenir une valeur et fournir un getter pour accéder à cette valeur
    
* Maintenir une liste d'abonnés sous forme de tableau et une méthode pour s'abonner
    
* Fournir un setter pour définir une nouvelle valeur et communiquer la valeur mise à jour à tous les abonnés
    

```javascript
class Signal {
  constructor(value) {
    this.value = value;
    this.subscribers = [];
  }

  getValue() {
    return this.value;
  }

  setValue(newValue) {
    this.value = newValue;
    this.emit();
  }

  emit() {
    this.subscribers.forEach((subscriber) => subscriber(this.value));
  }

  subscribe(callback) {
    this.subscribers.push(callback);
  }
}
```

Un cas d'utilisation pour ce qui précède peut ressembler à ceci :

```javascript
const signal = new Signal(0);

// La fonction de rappel de l'abonné est réexécutée par la classe lorsque la valeur change
signal.subscribe((value) => console.log(value));

// Il peut y avoir autant d'abonnés
signa.subscribe(...);

// Met à jour la valeur dans la classe
// Émet la valeur à tous les abonnés
signal.setValue(1);
```

La méthode `subscribe` pousse les fonctions de rappel fournies dans un tableau de `subscribers` tandis que `setValue` appelle la méthode `emit` qui parcourt ces abonnés et exécute chaque fonction de rappel d'abonné avec la `newValue`.

### Implémenter la méthode `createSignal`

Essayons d'utiliser ce qui précède pour implémenter une méthode `createSignal` qui doit :

* Accepter une valeur initiale comme argument
    
* Retourner un tableau de méthodes getter et setter
    

```javascript
export const createSignal = (value) => {
  const signal = new Signal(value);

  return [
    function value() {
      return signal.getValue();
    },
    function setValue(newVal) {
      signal.setValue(newVal);
    },
  ];
};

const [value, setValue] = createSignal(0);

// Affiche 0
console.log(value());

setValue(1);

// Affiche 1
console.log(value());
```

Le `createSignal` ci-dessus crée une nouvelle instance de la classe `Signal` avec la valeur initiale fournie.

Il retourne actuellement un getter et un setter qui appellent respectivement le getter et le setter de l'instance du signal.

Vous remarquerez que nous écrivons toujours `console.log(value())` deux fois manuellement lorsque nous voulons accéder à la dernière `value()` car il n'y a pas encore d'abonnements au signal.

Nous allons y parvenir avec l'implémentation de `createEffect`.

### Implémenter `createEffect`

Notre `createEffect` doit :

* Recevoir un rappel comme argument
    
* Exécuter le rappel une fois, immédiatement
    
* S'abonner aux signaux utilisés dans le rappel
    

```javascript
export const createEffect = (callback) => {    
  // Exécutons le rappel
  callback();
    
  // Attendez, comment puis-je m'abonner ?
};
```

Vous vous demandez peut-être : comment puis-je savoir si ce rappel utilise un getter de signal ou non ?

La réponse courte est, vous ne pouvez pas. Comme `createEffect` est une méthode générique, elle ne peut pas savoir quels signaux sont utilisés dans le rappel qui lui est passé. Elle ne peut exécuter ce rappel avec différents arguments au mieux.

Si nous réfléchissons différemment, il existe encore un moyen pour que cette fonction *communique* avec le code dans le rappel (getter).

Introduisons une nouvelle variable, `effectCallback`, qui est une variable intermédiaire utilisée pour communiquer entre l'effet et la méthode getter du signal. Cette variable doit contenir le rappel qu'un effet reçoit.

Un effet enregistre un abonnement de rappel basé sur le `getter` du signal qui a été accédé dans celui-ci.

Modifions notre code `createSignal` pour gérer cela :

```javascript
export const createSignal = (value) => {
  const signal = new Signal(value);

  return [
    function value() {
      // S'abonne à effectCallback si elle existe
      if (effectCallback) {
        signal.subscribe(effectCallback);
      }

      return signal.getValue();
    },
    function setValue(newVal) {
      signal.setValue(newVal);
    },
  ];
};
```

Voyons quand nous pouvons définir `effectCallback`. Nous savons que `createEffect` doit exécuter le rappel immédiatement une fois, ce qui signifie que nous pouvons capturer le rappel dans cette variable avant de l'exécuter et la nettoyer après avoir terminé l'exécution du rappel.

```javascript
export const createEffect = (callback) => {
   effectCallback = callback;
   callback();
   effectCallback = null;
};
```

En mettant tout ensemble :

```javascript
let effectCallback = null;

export const createEffect = (callback) => {
   effectCallback = callback;
   callback();
   effectCallback = null;
};

export const createSignal = (value) => {
  const signal = new Signal(value);

  return [
    function value() {
      if (effectCallback) {
        signal.subscribe(effectCallback);
      }

      return signal.getValue();
    },
    function setValue(newVal) {
      signal.setValue(newVal);
    },
  ];
};
```

Voici un [CodeSandbox](https://codesandbox.io/p/sandbox/solidjs-reactivity-diy-f5zh8x?file=%2Fsrc%2Fsignal.js%3A35%2C26-35%2C40&layout=%257B%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522rootPanelGroup%2522%253A%257B%2522direction%2522%253A%2522horizontal%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522id%2522%253A%2522ROOT_LAYOUT%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522clyac8qxx00063b6kcdj0r3jb%2522%252C%2522sizes%2522%253A%255B100%252C0%255D%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522EDITOR%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522id%2522%253A%2522clyac8qxx00023b6kg4nyqgiz%2522%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522SHELLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522id%2522%253A%2522clyac8qxx00033b6krfbo5b6p%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522DEVTOOLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522id%2522%253A%2522clyac8qxx00053b6kv5v81n4d%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%252C%2522sizes%2522%253A%255B50%252C50%255D%257D%252C%2522tabbedPanels%2522%253A%257B%2522clyac8qxx00023b6kg4nyqgiz%2522%253A%257B%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522clyac8qxx00013b6kq57p479j%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252Fsrc%252Findex.js%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%252C%257B%2522id%2522%253A%2522clyagpsv900023b6jketxf2fz%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522initialSelections%2522%253A%255B%257B%2522startLineNumber%2522%253A35%252C%2522startColumn%2522%253A26%252C%2522endLineNumber%2522%253A35%252C%2522endColumn%2522%253A40%257D%255D%252C%2522filepath%2522%253A%2522%252Fsrc%252Fsignal.js%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%255D%252C%2522id%2522%253A%2522clyac8qxx00023b6kg4nyqgiz%2522%252C%2522activeTabId%2522%253A%2522clyagpsv900023b6jketxf2fz%2522%257D%252C%2522clyac8qxx00053b6kv5v81n4d%2522%253A%257B%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522clyac8qxx00043b6k34nafcmv%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522UNASSIGNED_PORT%2522%252C%2522port%2522%253A0%252C%2522path%2522%253A%2522%252F%2522%257D%255D%252C%2522id%2522%253A%2522clyac8qxx00053b6kv5v81n4d%2522%252C%2522activeTabId%2522%253A%2522clyac8qxx00043b6k34nafcmv%2522%257D%252C%2522clyac8qxx00033b6krfbo5b6p%2522%253A%257B%2522tabs%2522%253A%255B%255D%252C%2522id%2522%253A%2522clyac8qxx00033b6krfbo5b6p%2522%257D%257D%252C%2522showDevtools%2522%253Atrue%252C%2522showShells%2522%253Afalse%252C%2522showSidebar%2522%253Atrue%252C%2522sidebarPanelSize%2522%253A18.53200883002208%257D) où vous pouvez jouer avec ce code.

L'ordre d'exécution serait quelque chose comme ceci :

* `createEffect` est exécuté avec une fonction de rappel, et celle-ci est stockée dans `effectCallback`.
    
* Le rappel est exécuté et invoquera toutes les méthodes de getter de signal utilisées dans celui-ci.
    
* La méthode getter `value` dans `createSignal` est exécutée et entre dans la condition qui vérifie si le getter est accédé depuis un rappel d'effet.
    
* Le rappel est abonné pour tout changement de valeur ultérieur et réexécuté lorsque le setter est appelé.
    

Voici quelque chose pour vous aider à visualiser ce processus :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-38.png align="left")

*Diagramme illustrant l'ordre d'exécution de la solution finale*

Ceci était bien sûr une implémentation rudimentaire du concept.

SolidJS fait beaucoup de choses sous le capot qui peuvent inclure :

* Optimisations : un signal maintiendra ses observateurs jusqu'à ce qu'ils soient manuellement supprimés. Cela peut devenir complexe dans les applications web où l'imbrication est courante.
    
* Permettre un moyen de regrouper les mises à jour
    
* Prise en charge des abonnés asynchrones
    

et bien plus encore.

## Conclusion

Dans cet article, nous avons exploré le concept de réactivité et son rôle dans les applications web. Nous avons examiné comment divers frameworks implémentent la réactivité, beaucoup utilisant des signaux comme mécanisme fondamental.

En décomposant l'implémentation des signaux de SolidJS, nous avons créé notre propre version à partir de zéro en utilisant le modèle Pub-Sub.

J'espère que cela vous a fourni des informations précieuses sur la réactivité, les signaux, et a amélioré votre compréhension de JavaScript.