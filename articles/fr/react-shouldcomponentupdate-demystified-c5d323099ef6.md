---
title: React shouldComponentUpdate démystifié
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-30T21:15:20.000Z'
originalURL: https://freecodecamp.org/news/react-shouldcomponentupdate-demystified-c5d323099ef6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_4NojzFjpzBM4vGMiAoYPw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: React shouldComponentUpdate démystifié
seo_desc: 'By Jean-Paul Delimat

  While developing in React have you ever wondered when and why a component’s render()
  method is run? Or when to use less obvious lifecycle methods shouldComponentUpdate()?

  If the answer is yes your app might have performance issue...'
---

Par Jean-Paul Delimat

En développant avec React, vous êtes-vous déjà demandé quand et pourquoi la méthode [render](https://facebook.github.io/react/docs/react-component.html#render)() d'un composant est exécutée ? Ou quand utiliser les méthodes de cycle de vie moins évidentes comme [shouldComponentUpdate](https://facebook.github.io/react/docs/react-component.html#shouldcomponentupdate)() ?

Si la réponse est oui, votre application pourrait avoir des problèmes de performance. Lisez ce qui suit et vous pourrez les résoudre facilement.

Tout cela dépend de la manière dont React fonctionne sous le capot. La grande promesse de React est qu'il est extrêmement rapide pour rendre les éléments sur une page.

Pour ce faire, React conserve en mémoire deux versions du DOM :

* la version du DOM actuellement affichée
* la prochaine version du DOM à afficher

Il compare les deux et met à jour le DOM affiché uniquement avec les parties qui ont changé. Ce processus est appelé [réconciliation d'arbre](https://facebook.github.io/react/docs/reconciliation.html). La racine de l'arbre évaluée pour la réconciliation est un composant dont les [props](https://facebook.github.io/react/docs/components-and-props.html) ont changé.

Bien. Que vous l'ayez prévu ou non, votre application web suit dans une certaine mesure la division des composants conteneurs/présentationnels. Voir [ici](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) et [ici](https://medium.com/@learnreact/container-components-c0e67432e005) pour les définitions. Cela signifie que chaque vue complexe de votre application est composée d'un composant conteneur qui contient la logique et a beaucoup de [composants d'affichage uniquement](https://www.fullstackreact.com/30-days-of-react/day-11/) comme enfants.

C'est un très bon modèle. Si vous regardez de plus près, cela signifie que toute interaction de l'utilisateur sur la vue affectera le conteneur lui-même et déclenchera un rendu de celui-ci et de tous ses enfants. Supposons que vous avez une liste d'éléments avec une affichage sophistiqué de texte, d'image et un bouton en forme d'étoile jaune "Ajouter aux favoris". Le modèle minimal pour un élément de liste pourrait être :

```js
product = { 
    imageUrl: '...', 
    title: '...', 
    isFavourite: false
}
```

La liste des favoris pourrait provenir d'une autre source de données. Peu importe, l'organisation de vos composants ressemble probablement à ceci :

```js
<Container>
    <ListOfElements
        elements={this.props.elements} 
        onElementChanged={this.props.onElementChanged} 
    />
</Container>
```

Le gestionnaire est appelé lors du clic de l'utilisateur et sauvegarde les informations côté serveur (ou persiste dans un store ou autre) et déclenche un changement dans this.props.elements.

Le résultat d'un seul clic déclenche le rendu du conteneur et de toutes les lignes de la liste juste pour mettre à jour une seule case à cocher.

C'est là que shouldComponentUpdate() entre en jeu. Vous pouvez dire à React de ne pas rendre les lignes qui n'ont pas besoin d'être mises à jour en utilisant cette méthode.

```js
class ListItem extends Component {
    shouldComponentUpdate(nextProps, nextState) {
        return nextProps.isFavourite != this.props.isFavourite;
    }
    ...
}
```

Voici un cas concret : sur un projet d'application de marketplace, nous avions une vue de gestion des produits pour les vendeurs. La liste avait un modèle de "chargement de plus d'éléments à mesure que l'utilisateur fait défiler vers le bas" et des actions en ligne "afficher/masquer" pour définir la visibilité de chaque produit. Tout allait bien lorsque les vendeurs géraient moins de 100 produits dans leur tableau de bord. Ensuite, un vendeur a commencé à entrer et à promouvoir plus de 300 produits...

Il y avait un décalage d'environ 600 ms avant que l'interface utilisateur ne se mette à jour après qu'un utilisateur ait cliqué sur l'icône "activer/désactiver". Le décalage était définitivement visible par l'utilisateur final. En utilisant le [profileur Chrome](https://developers.google.com/web/tools/chrome-devtools/rendering-tools/), nous avons vu que React mettait environ 2 ms pour rendre une seule ligne. Multiplié par 300... nous avons obtenu jusqu'à 600 ms. Nous avons ajouté les vérifications shouldComponentUpdate() pour les conditions appropriées. Le temps de rendu après le clic de l'utilisateur est passé sous les 10 ms...

**J'ai mis en place un petit projet qui permet de reproduire ce cas [ici](https://github.com/jpdelima/react-should-component-update-demystified). Exécutez-le et lisez les commentaires du code pour voir la magie opérer.**

### Avertissement pour les utilisateurs de Redux

Le problème décrit ci-dessus peut se produire plus souvent si vous utilisez [Redux](https://github.com/reactjs/react-redux) et [reselect](https://github.com/reactjs/reselect) (ou des bibliothèques similaires de "pipelines d'actions basées sur le store").

Avec Redux et reselect, vous poussez des actions vers le store et vous branchez des écouteurs aux changements du store, alias les sélecteurs. Les sélecteurs sont globalement disponibles dans l'application et dans une grande application, il est assez facile pour de nombreux composants de mapper les mêmes sélecteurs. Les changements dans le store peuvent déclencher des changements de props et ainsi des rendus qui sont complètement irrélevants pour certains composants.

Voici le conseil déroutant : **n'utilisez pas** shouldComponentUpdate() pour prévenir les rendus dans de tels cas. La logique à l'intérieur de shouldComponentUpdate ne doit regarder que ce qui est pertinent pour le composant. Elle ne doit jamais anticiper les contextes dans lesquels le composant est utilisé. La raison est simplement que votre code deviendrait rapidement ingérable.

Si vous avez ce genre de problèmes, cela signifie que la structure de votre store est incorrecte ou que les sélecteurs ne sont pas assez spécifiques. Vous devez passer à une nouvelle phase de modélisation.

Je recommande [ce modèle de base génial](https://github.com/react-boilerplate/react-boilerplate). Il promeut l'encapsulation du store par conteneur de haut niveau avec une zone globale pour les structures de données clés qui s'étendent sur toute l'application. C'est une approche assez sûre pour éviter les erreurs de modélisation du store.

**Merci d'avoir lu ! Si vous avez aimé, cliquez sur le bouton d'applaudissements ci-dessous. Cela aide les autres à voir l'histoire.**