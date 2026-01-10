---
title: Comment React fonctionne sous le capot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-05T00:55:10.000Z'
originalURL: https://freecodecamp.org/news/react-under-the-hood
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/New-Project--24-.jpg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: Comment React fonctionne sous le capot
seo_desc: "By Mehul Mohan\nReact is a very popular JavaScript library. With over 5.5\
  \ million weekly downloads, React is enjoying great popularity. But not a lot of\
  \ React developers know how React works under the hood. \nIn this post, I'll try\
  \ to uncover some inte..."
---

Par Mehul Mohan

React est une bibliothèque JavaScript très populaire. Avec plus de 5,5 millions de téléchargements par semaine, React jouit d'une grande popularité. Mais peu de développeurs React savent comment React fonctionne sous le capot. 

Dans cet article, je vais essayer de révéler quelques choses intéressantes sur React que vous, en tant que développeur React, pourriez trouver fascinantes. Commençons par le début.

Mais avant de commencer, si vous êtes un développeur React, j'ai une excellente nouvelle pour vous ! Une fois que vous aurez terminé cet article, vous pourrez développer quelque chose de cool avec React et gagner des prix en cours de route :)

## Que fait React ?

À sa base, React maintient essentiellement un arbre pour vous. Cet arbre est capable d'effectuer des calculs de diff efficaces sur les nœuds. 

Imaginez votre code HTML comme un arbre. En fait, c'est exactement ainsi que le navigateur traite votre DOM (votre HTML rendu dans le navigateur). React vous permet de reconstruire efficacement votre DOM en JavaScript et de pousser uniquement les modifications qui ont réellement eu lieu vers le DOM.

## JSX est du sucre syntaxique

Il n'y a rien de tel que JSX - ni pour JavaScript, ni pour le navigateur. JSX est simplement du sucre syntaxique pour créer des objets JavaScript très spécifiques.

Lorsque vous écrivez quelque chose comme :

```
const tag = <h1>Bonjour</h1>
```

ce que vous faites essentiellement, c'est ceci :

```
const tag = React.createElement("h1", {}, "Bonjour")
```

Vous voyez, lorsque vous commencez à écrire des éléments imbriqués, non seulement cela devient difficile à coder, mais cela devient également très inconfortable à maintenir. JSX vous aide ainsi à apporter la propreté du HTML à la puissance de JavaScript.

Mais que fait React.createElement lui-même ? Il crée un simple objet JavaScript. En fait, vous pouvez l'appeler manuellement et voir par vous-même !

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-05-at-5.19.08-am.png)

Vous voyez, nous avons un objet comme ceci :

```js
{
    $$typeof: Symbol(react.element),
    key: null,
    props: {children: "Bonjour"},
    ref: null,
    type: "div"
}
```

Et si nous commençons à imbriquer des éléments comme ceci :

```js
React.createElement('div', { }, 
React.createElement('p', {}, 'Un p dans un div')
)

```

Nous commencerions à obtenir des objets imbriqués :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-05-at-5.22.49-am.png)

Maintenant, vous savez que, une fois que tout le JSX est analysé et que tous les appels React.createElement ont été résolus, nous obtenons un énorme objet imbriqué comme ci-dessus.

## React Renderer

Maintenant, si vous revenez au point où nous démarrons notre application, vous verrez que dans votre fichier index.js, vous trouverez la ligne suivante :

```jsx
// .. code précédent

ReactDOM.render(<App />, container)
```

D'après ce qui précède, nous savons que lorsque `<App />` a été analysé, ce n'est qu'un énorme objet d'éléments React. Alors, comment React est-il capable de construire des divs et des balises p réelles à partir de celui-ci ? Rencontrez ReactDOM.

ReactDOM, à son tour, crée récursivement des nœuds en fonction de leur propriété 'type' et les ajoute finalement au DOM.

Il devrait être clair à ce stade pourquoi découpler React des renderers est en fait une excellente idée ! Ce que React fait, c'est simplement construire un arbre d'UI qui pourrait être utilisé non seulement sur le web, mais aussi sur des environnements comme le mobile, à condition qu'un renderer soit disponible et capable de communiquer avec le système d'exploitation hôte. C'est là que React Native entre en jeu. Vous voyez, React Native utilise la bibliothèque React, mais pas ReactDOM comme renderer. Au lieu de cela, le package react-native lui-même est un renderer.

Nous faisons cela dans une application react native pour démarrer l'application :

```js
const { AppRegistry } = require('react-native')
AppRegistry.registerComponent('app', () => MainComponent)
```

Regardez ! Pas de ReactDOM. Pourquoi pas ? Parce que nous n'avons pas de méthodes comme appendChild, ni un environnement de type DOM. Au lieu de cela, pour les mobiles, nous avons besoin d'un support pour l'UI directement depuis le système d'exploitation. Mais la bibliothèque React n'a pas besoin de le savoir, le renderer (React Native) s'en charge.

## Réconciliation React

Lorsque nous disons que React maintient une copie du DOM en utilisant le DOM virtuel en JavaScript, et qu'il l'utilise pour différencier les changements et les appliquer au DOM réel, nous ne voulons pas que React utilise la force brute. React, en fait, fait une réconciliation très paresseuse. React effectuera le moins de changements possible, c'est-à-dire qu'il essaiera de réutiliser les éléments, les attributs, et même les styles si possible !

Prenons cet exemple :

```jsx
<img className="class-1" alt="truc" />
```

Supposons que vous changiez cette expression JSX en celle ci-dessous en utilisant une condition ou un état :

```jsx
<img className="class-1" alt="quelque chose d'autre" />
```

Maintenant, lors de la différenciation, React verra que la balise img utilise la même className dans les anciens et nouveaux arbres, donc pourquoi la modifier. Et il modifiera simplement votre attribut alt et passera à autre chose.

Cependant, il y a un piège. Parce que nous ne voulons pas que React effectue beaucoup de calculs sur la partie différenciation, React supposera que si un parent a changé, son sous-arbre contenu a définitivement changé. Par exemple :

```jsx
<div className="class-1">
	<p>Je n'ai pas changé</p>
</div>
```

Si vous changez ce JSX en celui ci-dessous en utilisant une condition/état :

```jsx
<p className="class-1">
	<p>Je n'ai pas changé</p>
</p>
```

Bien que vous puissiez voir que nous n'avons pas besoin de recréer la balise p intérieure, React n'a aucun moyen de le savoir lors de la traversée de l'arbre depuis le haut (sauf, bien sûr, si vous effectuez une différenciation lourde de l'arbre, qui sont des algorithmes beaucoup plus coûteux que l'heuristique O(n) que React suit pour la différenciation). Donc, React décide de détruire tous les enfants (c'est-à-dire d'appeler leurs fonctions de nettoyage dans useEffect, ou componentWillUnmount dans les composants basés sur les classes) et de recréer les enfants à partir de zéro. 

## Clés React

Lors de l'ajout/suppression d'éléments dans un nœud, React bouclerait simplement sur les enfants dans l'ancien arbre et les enfants dans le nouvel arbre du nœud et marquerait les endroits où il doit effectuer une addition/suppression. Mais cela présente un inconvénient sans l'aide supplémentaire du développeur. Prenons cet exemple :

```jsx
<ul>
    <li>A</li>
    <li>B</li>
</ul>
```

Supposons que cela soit changé en ce qui suit par condition/état :

```jsx
<ul>
    <li>Z</li>
    <li>A</li>
    <li>B</li>
<ul>
```

Maintenant, lorsque React commencerait à comparer les deux listes pour trouver les différences, il trouverait la différence au nœud enfant 1, muteraient l'ancien A en nouveau Z, puis à nouveau au nœud enfant 2, le muteraient de l'ancien B en nouveau A, et enfin ajouteraient le nouveau nœud B.

Cependant, une meilleure façon aurait été de préserver les nœuds A et B existants et de simplement préfixer le nœud Z. Mais comment React le saurait-il ? Les clés React aideraient.

Les clés fournissent simplement un moyen à React de savoir quels éléments ont changé ou non lors de la différenciation. Maintenant, au lieu de comparer l'élément entier, React comparera les clés des enfants pour voir quel élément doit être ajouté/supprimé. La manière suivante est une façon efficace d'effectuer la même chose :

```jsx
<ul>
    <li key="A">A</li>
    <li key="B">B</li>
</ul>
```

Maintenant, si cela devient :

```jsx
<ul>
    <li key="Z">Z</li>
    <li key="A">A</li>
    <li key="B">B</li>
</ul>
```

React saura maintenant que les clés 'A' et 'B' existent déjà, donc nous devons simplement ajouter le nouvel élément avec la clé 'Z'.

_Êtes-vous un développeur React ? Montrez vos **compétences React** en développant un jeu interactif de 3 minutes en React et **gagnez des hoodies, des t-shirts et des tasses à café** ! Participez à **codecomp** en rejoignant le serveur Discord de codedamn **[ici](http://bit.ly/codedamn-discord)**_

Voici donc quelques concepts importants que je crois être vraiment utiles pour vous en tant que développeurs React afin de commencer à comprendre le cœur de React et comment il fonctionne réellement. N'hésitez pas à transmettre vos suggestions ou questions à ce sujet. 

Vous pouvez [me suivre sur Twitter](https://twitter.com/mehulmpt) pour plus de tweets sur JS/codage et autres. Paix !