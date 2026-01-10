---
title: 'React.js : implémenter la fonctionnalité de glisser-déposer sans utiliser
  de bibliothèques externes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T08:16:04.000Z'
originalURL: https://freecodecamp.org/news/reactjs-implement-drag-and-drop-feature-without-using-external-libraries-ad8994429f1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hPLhe5cqPbyE8Hi4CGQMYg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: 'React.js : implémenter la fonctionnalité de glisser-déposer sans utiliser
  de bibliothèques externes'
seo_desc: 'By Rajesh Pillai

  Get into the details of implementing drag and drop features in React from scratch.


  So, easy even your dog can drag it :)

  Let’s first see the result of what we will be building. I am trying out .gif — hopefully
  it works everywhere as...'
---

Par Rajesh Pillai

#### Entrez dans les détails de l'implémentation des fonctionnalités de glisser-déposer dans React à partir de zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hPLhe5cqPbyE8Hi4CGQMYg.png)
_Ainsi, même votre chien peut le glisser :)_

Voyons d'abord le résultat de ce que nous allons construire. J'essaie le format .gif — espérons qu'il fonctionne partout comme prévu. J'ai utilisé [Camtasia](https://discover.techsmith.com/camtasia-brand-desktop-features-logos-april/?gclid=EAIaIQobChMIn67LrPXp2gIVk7rACh0hjgr7EAAYASAAEgJWa_D_BwE) avec une licence personnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y11YSJEJ9A4JFGllOQSroQ.gif)
_Ignorez l'UI/les styles, s'il vous plaît !_

Les points clés à apprendre sont les suivants :

1. rendre un élément glissable en ajoutant l'attribut « draggable »
2. rendre une zone déposable en implémentant l'événement « dragover »
3. capturer les données de glisser en implémentant l'événement « dragstart »
4. capturer le dépôt en implémentant l'événement « drop »
5. implémenter l'événement « drag » qui est déclenché lorsque l'élément est en cours de glisser
6. stocker les données intermédiaires dans l'objet dataTransfer

Pour les apprenants visuels, regardez la vidéo ci-dessous.

### Étape 1 — créer l'application racine pour la démonstration

Tout le code pour le glisser-déposer ira dans le composant AppDragDropDemo.js.

```
import React from 'react';
import ReactDOM from 'react-dom';
import '.index.css';
import AppDragDropDemo from './AppDragDropDemo';
```

```
ReactDOM.render(<AppDragDropDemo />, document.getElementById("root"));
```

Le point d'entrée pour AppDragDropDemo ressemble au code ci-dessous.

```
import React, { Component } from 'react';
```

```
export default class AppDragDropDemo extends Component {
  render () {
    return (
      <div className="container-drag">
        DÉMO GLISSER-DÉPOSER
      </div>
    );
  }
}
```

Si vous exécutez maintenant l'application, vous verrez cet écran impressionnant (jeu de mots intentionnel)

![Image](https://cdn-media-1.freecodecamp.org/images/1*16qtjJ6Bh53hsY2z4oi2gw.png)

### Étape 2 — créer l'objet d'état pour stocker certaines tâches

Créons quelques tâches pour simuler une application simple. Ce que nous voulons faire, c'est glisser-déposer ces tâches dans différentes catégories comme `wip`, `complete`, et ainsi de suite.

```
export default class AppDragDropDemo extends Component {
      state = {
            tasks: [
              {
                name:"Learn Angular",
                category:"wip",
                bgcolor: "yellow"
              },
              {
                name:"React",
                category:"wip",
                bgcolor:"pink"
              },
              {
                name:"Vue",
                category:"complete",
                bgcolor:"skyblue"
              }
            ]
      }
```

```
  render () {
    return (
      <div className="container-drag">
        DÉMO GLISSER-DÉPOSER
      </div>
    );
  }
}
```

### Étape 3 — organiser nos données en catégories

Implémentons le code ci-dessous dans la méthode render, pour regrouper les tâches dans leurs catégories respectives, `wip` et `complete`. N'hésitez pas à ajouter plus de catégories et à jouer avec le code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u7edSd4vxCBW_JMnA1qbYA.png)

Vous pouvez copier-coller le code ci-dessus à partir du snippet ci-dessous.

```
render() {
          var tasks = {
            wip: [],
            complete: []
          }
          this.state.tasks.forEach ((t) => {
            tasks[t.category].push(
              <div
                key={t.name}
                onDragStart={(e)=>this.onDragStart(e, t.name)}
                draggable
                className="draggable"
                style={{backgroundColor: t.bgcolor}}
              >
                {t.name}
              </div>
            );
          });
```

Dans le code ci-dessus, nous parcourons toutes les tâches et créons un div pour chaque élément de tâche et le stockons dans les catégories respectives.

Ainsi, le `wip[]` contient toutes les tâches dans la catégorie wip et `complete[]` contient toutes les tâches terminées.

### Étape 4 — rendre l'élément de tâche glissable

Ajoutez l'attribut draggable à la <div> ou à n'importe quel élément pour rendre un élément glissable. Reportez-vous au bloc de code ci-dessus pour le format texte du code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UZ8KT2yWKAQBv_wvvuZNLA.png)

### Étape 5 — créer un conteneur déposable

Pour créer un conteneur déposable, implémentez l'événement `dragover`. Maintenant, puisque nous voulons désactiver l'événement dragover par défaut, nous appelons simplement `event.preventDefault()` à partir de l'événement dragover.

Nous allons également rendre `{tasks.wip}` et `{tasks.complete}` dans leurs éléments div correspondants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*muabAA2HIbX14VtSFvKG6g.png)

```
return (
  <div className="container-drag">
    <h2 className="header">DÉMO GLISSER-DÉPOSER</h2>
    <div className="wip"
      onDragOver={(e)=>this.onDragOver(e)}
      onDrop={(e)=>{this.onDrop(e, "wip")}}>
      <span className="task-header">EN COURS</span>
      {tasks.wip}
    </div>
    <div className="droppable"
      onDragOver={(e)=>this.onDragOver(e)}
      onDrop={(e)=>this.onDrop(e, "complete")}>
      <span className="task-header">TERMINÉ</span>
      {tasks.complete}
    </div>
  </div>
);
```

```
Implémentons maintenant le gestionnaire d'événements onDragOver().
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*hNDl0tztfkDNddbIN4cVew.png)

Le résultat jusqu'à présent ressemblera à la figure ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fHaKQZ_1Iw0J1bFlIufbTw.png)

### Étape 6 — capturer l'état de l'élément en cours de glisser

Modifions le code où nous créons la catégorie pour chaque tâche. Ajoutez un gestionnaire d'événements `ondragstart` et passez l'id/nom ou toute information que vous devez conserver pendant le glisser-déposer.

J'utilise `name` comme valeur unique pour identifier la tâche. N'hésitez pas à utiliser l'ID ou toute autre clé unique que vous avez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nX-KfIY37q0S_mRELKu1Hg.png)

Implémentons maintenant le gestionnaire d'événements `onDragStart`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TkXlaYt3owLXnQKhSp-yVw.png)

Dans le gestionnaire onDragStart, nous récupérons le paramètre et le stockons dans l'objet dataTransfer. (Ne vous laissez pas confondre par le nom du paramètre, car je suppose que j'étais dans un monde de nommage différent en codant cela :) .)

**Note IE** : cela peut ne pas fonctionner avec IE. Pour IE, la meilleure pratique est de donner le format comme clé comme montré ci-dessous.

```
Au lieu de
```

```
ev.dataTransfer.setData("id", id)
```

```
UTILISEZ
```

```
ev.dataTransfer.setData("text/plain",id)
```

Le gestionnaire ci-dessus garantira que l'élément en cours de glisser est stocké dans l'objet d'événement et est disponible pour une utilisation lorsque cela est nécessaire. Il peut être nécessaire lors du dépôt sur une cible.

Maintenant, si vous exécutez l'application et glissez les éléments, les logs suivants seront produits.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T9eejIeJ6gZJGWFoLxXxgg.png)

### Étape 7 — gérer l'événement de dépôt.

Ouvrons la méthode render et ajoutons l'événement `onDrop` à la div avec un className de `droppable`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ww-IahlxEBq5Y6LTSsbZjw.png)

Dans le code ci-dessus, nous ajoutons le gestionnaire d'événements `drop`, et passons la catégorie requise `complete` comme argument. Cela indique que nous déposons l'élément de l'état `wip` à l'état `complete` (catégorie). N'hésitez pas à changer les noms, si nécessaire.

Implémentons maintenant le gestionnaire d'événements `onDrop()`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hLHULfBCgIXe2f9XeWnrGw.png)

Voici le code que vous pouvez copier/coller :

```
onDrop = (ev, cat) => {
  let id = ev.dataTransfer.getData("id");
  let tasks = this.state.tasks.filter((task) => {
    if (task.name == id) {
      task.category = cat;
    }
    return task;
  });
  this.setState({
    ...this.state,
    tasks
  });
}
```

Dans le gestionnaire d'événements `onDrop`, nous récupérons la tâche en cours de glisser en utilisant la méthode getData sur l'objet dataTransfer de l'événement.

Nous créons ensuite un nouveau tableau de tâches en utilisant la méthode filter, et changeons la catégorie de la tâche en cours de glisser.

`setState()` déclenchera le rendu, et les tâches seront rendues dans les bonnes zones.

**Note IE** : Pour le faire fonctionner dans IE, utilisez la méthode getData ci-dessous.

Au lieu de

**var id = ev.dataTransfer.getData("id")**

utilisez

**var id = ev.dataTransfer.getData("text")**

### Étape 8 — pour implémenter le dépôt de « complete » à « wip », ajoutez le gestionnaire onDrop

Le gestionnaire `onDrop()` reste le même que précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZtINZCL07rVeEsYYogmVg.png)

Enfin, exécutez le code et admirez votre création :) et amusez-vous en codant.

Vous pouvez récupérer le code source [ici](https://github.com/rajeshpillai/youtube-react-components/blob/master/src/AppDragDropDemo.js).

**Note :** pour que cela fonctionne sur tous les navigateurs, changez le type setData en string. Par exemple, pour définir les données, utilisez `**ev.dataTransfer.setData("text/plain",id)**`. Pour lire les données, utilisez `**var id = ev.dataTransfer.getData("text")**`

Puisque mon objectif était de démontrer les fonctionnalités principales de glisser-déposer, le code n'a pas été optimisé pour des facteurs tels que la conception et les conventions de nommage.

Apprenez avec moi @Learner + Fullstack Coach (@rajeshpillai) : [https://twitter.com/rajeshpillai](https://twitter.com/rajeshpillai)

Promotion : Coupon spécial de 10 $ pour les lecteurs de Medium pour mon prochain cours en direct [ReactJS-Beyond the basics](https://www.udemy.com/reactjs-beyond-the-basics/?couponCode=MEDIUM_500) sur Udemy au cas où vous souhaiteriez soutenir notre programme open source [Mastering frontend engineering in 12 to 20 weeks](https://codeburst.io/mastering-front-end-engineering-in-12-to-20-weeks-for-beginners-and-experienced-alike-6dc5172e3295).

Je viens de publier mon cours en accès anticipé [Javascript Deep Dive

Code your own React](https://www.udemy.com/javascript-deep-dive-code-your-own-react-library/?couponCode=SOCIAL1000)