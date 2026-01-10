---
title: Une explication simplifiée de la propagation des événements en JavaScript.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-14T09:51:06.000Z'
originalURL: https://freecodecamp.org/news/a-simplified-explanation-of-event-propagation-in-javascript-f9de7961a06e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l9va7pNhLirT_nYfPWFt6w.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une explication simplifiée de la propagation des événements en JavaScript.
seo_desc: 'By Amber Wilkie

  Imagine this scenario:You are building a list of users. You’re displaying their
  names, favorite colors, and emails. When you click on a user (one row in the table),
  you want it to take you to the user record. Except for when you click...'
---

Par Amber Wilkie

Imaginez ce scénario :
Vous construisez une liste d'utilisateurs. Vous affichez leurs noms, leurs couleurs préférées et leurs emails. Lorsque vous cliquez sur un utilisateur (une ligne dans le tableau), vous voulez qu'il vous emmène à l'enregistrement de l'utilisateur. Sauf lorsque vous cliquez sur l'email, alors il devrait faire apparaître une boîte de dialogue d'email.

Vous pourriez écrire un code comme ceci (nous utilisons un tableau ici car c'est facile à comprendre — bien sûr, nous pourrions utiliser quelque chose de beaucoup plus compliqué dans notre projet) :

```html
<Table>
  <thead>
  <tr>
    <th>Nom</th>
    <th>Couleurs</th>
    <th>Email</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>Susie</td>
    <td>Bleu, Rouge</td>
    <td>susie@hello.com</td>
  </tr>
  </tbody>
</Table>
```

Si vous voulez cliquer sur l'une de ces lignes, vous ajouterez probablement une fonction `onClick` à la ligne. Ainsi, si ils cliquent n'importe où dans la ligne, ils peuvent aller directement à l'enregistrement de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/WfjYnhCNEKvHMas6H81NXtfLzxbGod3elFwI)

Pour gérer l'email, nous ferons une balise `<a href>` sur le texte.

Mais attendez ! La boîte de dialogue de l'email s'affiche, mais **nous naviguons également vers l'enregistrement de l'utilisateur**. Ce n'est pas ce que nous voulons ! Comment gérer cela ? Voici la propagation des événements.

### La propagation des événements en bref.

La propagation des événements est un moyen de décrire la "pile" d'événements qui sont déclenchés dans un navigateur web. Dans notre exemple de tableau ci-dessus, cliquer sur la balise `a` est le premier événement que nous allons déclencher, mais il y a aussi d'autres événements.

Pour comprendre ce concept, vous devez comprendre que les éléments d'un navigateur web sont imbriqués. Ils ne se couvrent pas les uns les autres. Ainsi, un clic sur la balise `a` clique également sur la ligne, le tableau, la `div` dans laquelle le tableau est imbriqué, et tout le reste jusqu'à `document`, le conteneur complet qui contient tout dans votre navigateur.

Si nous avons placé d'autres événements `onClick` à l'intérieur de ces autres éléments, ils seront également déclenchés lorsque nous cliquerons sur le lien `a` dans le tableau. C'est pourquoi nous serons dirigés vers l'enregistrement de l'utilisateur lorsque nous cliquerons sur le lien email. Il va exécuter à la fois la fonction `onClick` pour le lien `a` et la fonction `onClick` pour la ligne.

#### Bulles

Le mouvement des événements "vers le haut" de l'élément le plus imbriqué (`a`) vers le moins imbriqué (`document`) est appelé "bubbling". Si les événements commencent dans l'élément "le plus externe" et se déplacent "vers le bas", cela est appelé "capturing". Tout ce qui vous intéresse probablement, c'est le comportement par défaut : le bubbling.

### Comment utiliser la propagation des événements à votre avantage

Honêtement, je n'avais rencontré **aucun** cas d'utilisation pour me soucier de la propagation des événements jusqu'à cette semaine, lorsque j'ai dû construire un tableau avec une case à cocher. Malheureusement pour moi, lorsque j'ai essayé de configurer la fonctionnalité de cocher, cela m'a emmené à l'enregistrement. Heureusement, j'ai suivi une formation plus tôt (voir les références ci-dessous) qui m'a donné un indice sur ce que je devais rechercher sur Google.

Vous savez probablement déjà que lorsque vous créez un événement `onClick`, il est passé à la fonction que vous appelez.

Ainsi, ici, j'ai pu écrire :

```js
handleCheck = e => {
  e.stopPropagation()
  // parler à mon API, définir l'enregistrement comme "terminé" ou non
}
<span onClick={this.handleCheck}>[]</span>
```

Ce `e.stopPropagation()` arrête ce "bubbling" des événements "vers le haut" à travers le DOM. Nous arrêtons tous les autres événements dans la pile. Génial !

Ainsi, toute ma ligne se comporte comme elle le devrait, et cette petite case à cocher peut avoir une fonctionnalité spéciale.

#### `preventDefault` vs. `stopPropagation`

Vous pourriez penser : pourquoi ne pas simplement utiliser `e.preventDefault()` ? C'est en effet la première chose que j'ai essayée, mais il n'y a tout simplement pas de comportement par défaut pour un span (contrairement à un formulaire, dont le comportement de soumission par défaut va rafraîchir la page).

### Exemple à copier-coller

J'écris beaucoup de React, donc je donne un exemple en React. Mais cela fonctionnerait de la même manière en HTML et JavaScript classiques, en utilisant la méthode que vous avez pour ajouter des écouteurs d'événements :

```html
<div onClick={() => console.log('div externe')}>
  <div onClick={() => console.log('div intermédiaire')}>
    <div onClick={() => console.log('div la plus interne')}>
      Cliquez-moi !
    </div>
  </div>
</div>
```

Propagation des événements : des bulles sans le champagne.

![Image](https://cdn-media-1.freecodecamp.org/images/AVtlEJO9vPaFKX4HFoZadcla0fha-4kwghpQ)
_Journal de la console pour l'exemple de propagation des événements_

### Références

* Un grand merci à [Wes Bos](https://www.freecodecamp.org/news/a-simplified-explanation-of-event-propagation-in-javascript-f9de7961a06e/undefined) qui m'a d'abord présenté ce concept dans son cours #Javascript30 [course](http://javascript30.com). Je n'aurais eu aucune idée de ce que je devais rechercher sur Google lorsque j'ai rencontré le problème identifié dans l'exemple de tableau ci-dessus si je ne l'avais pas d'abord vu pendant le cours.
* [Cette réponse Stack Overflow](https://stackoverflow.com/questions/4616694/what-is-event-bubbling-and-capturing), qui résume bien certains des aspects plus nuancés de la capture et de la propagation des événements.