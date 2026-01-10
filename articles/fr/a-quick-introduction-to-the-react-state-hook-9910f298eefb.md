---
title: Une introduction rapide au Hook d'État React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T18:46:23.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-the-react-state-hook-9910f298eefb
coverImage: https://cdn-media-1.freecodecamp.org/images/0*aZznaKKUdQFDwl-1
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: Une introduction rapide au Hook d'État React
seo_desc: 'By Jake Wiesler

  The React Hooks proposal comes with some built-in hooks that focus on doing one
  thing, such as providing state or context to a function component. You can also
  use these as building blocks to create your own.

  In a recent post, I share...'
---

Par Jake Wiesler

La proposition [React Hooks](https://reactjs.org/docs/hooks-intro.html) vient avec quelques [hooks intégrés](https://reactjs.org/docs/hooks-reference.html) qui se concentrent sur une seule chose, comme fournir un état ou un contexte à un composant fonctionnel. Vous pouvez également utiliser ceux-ci comme blocs de construction pour créer [les vôtres](https://reactjs.org/docs/hooks-custom.html).

Dans [un récent article](https://www.jakewiesler.com/blog/on-react-hooks), j'ai partagé quelques réflexions personnelles sur la proposition des hooks. Cet article sera plus technique, car je vais plus loin dans le détail sur ce que je considère être le hook le plus important : `useState`.

Au moment d'écrire ces lignes, les hooks sont toujours une **proposition expérimentale**. Rien dans cet article ne doit être considéré comme final. Veuillez garder cela à l'esprit. Il y a actuellement un [RFC ouvert](https://github.com/reactjs/rfcs/pull/68) où vous pouvez rester informé de la proposition, et même exprimer vos préoccupations si vous en avez.

Les hooks sont disponibles dans la version `v16.7.0-alpha` de React. J'ai configuré un [CodeSandbox](https://codesandbox.io/s/1z16jj9y24) qui vous permettra de commencer rapidement si vous souhaitez suivre l'exemple de cet article.

### L'état React aujourd'hui

Si vous voulez un composant avec état dans React, votre seule option pour le moment est d'écrire ce composant sous forme de classe. Cela a été une source de frustration pour moi. Souvent, je me surprends à passer une bonne partie de mon énergie mentale à me demander si je veux ou non refactoriser un composant fonctionnel _parfaitement acceptable_ en une classe simplement pour contenir un état.

Je me convaincreai que éviter une telle refactorisation est dans mon meilleur intérêt. Finalement, je me retrouverai à tomber dans un terrier de stratégies de gestion d'état, de bibliothèques et d'_"autres solutions"_.

Si les choses _vont vraiment mal_, je commencerai à me demander si le composant a même _besoin_ d'un état en premier lieu, comme si c'était quelque chose à éviter.

Cela semble excessif, et ça l'est probablement. Mais c'est arrivé. Et si vous avez passé une quantité significative de temps à travailler avec React, vous avez peut-être vous aussi trouvé votre chemin dans cette chasse à l'oie sauvage (ou peut-être que c'est juste moi ?).

**Ajouter un état à un composant devrait sembler naturel, mais il est difficile de se sentir naturel lorsque j'écris une classe.**

### Voici le hook `useState`

Avec le hook `useState`, les composants fonctionnels peuvent maintenant contenir un état local.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RDvwWcUggOXWjzK8z7FotQ.png)
_Créé avec [carbon.now.sh](https://carbon.now.sh" rel="noopener" target="_blank" title=")_

`useState` est une fonction qui accepte un état initial et retourne un tableau avec 2 éléments :

1. L'état actuel
2. Une fonction qui peut être appelée pour mettre à jour l'état

En raison du fonctionnement de la destructuration de tableau, nous pouvons nommer les éléments retournés par `useState` comme nous le souhaitons. Il n'y a aucune contrainte imposée par l'API. Par convention, il semble que l'écosystème React adopte la syntaxe `[value, setValue]`.

Dans l'exemple ci-dessus, `color` est la valeur de l'état et est initialisée à `'GREEN'`. La fonction `setColor` peut être appelée pour mettre à jour cette valeur.

Notez que, contrairement à un composant de classe, l'état dans un composant fonctionnel **n'a pas** besoin d'être un objet. Ici, ce n'est qu'une chaîne de caractères.

Une autre note importante est que la fonction de mise à jour, dans ce cas `setColor`, ne _fusionne_ pas le nouvel état avec l'état actuel, mais le _remplace_ complètement. Cela diffère de la manière dont `this.setState` fonctionne dans les composants de classe.

### Mise à jour de l'état

La valeur de `color` sera préservée entre les re-rendus (plus d'informations à ce sujet ci-dessous), _sauf_ si la fonction `setColor` est appelée avec une nouvelle valeur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VUq_gZRRYjXsildlK1hohQ.png)
_Créé avec [carbon.now.sh](https://carbon.now.sh" rel="noopener" target="_blank" title=")_

Lorsque le bouton est cliqué, la fonction `slow` appellera `setColor` avec une valeur de `'YELLOW'`. Cela provoquera le re-rendu du composant `StreetLight`. Lorsqu'il le fera, la variable `color` sera mise à jour à `'YELLOW'`.

#### Attendez, quoi ?

À première vue, vous pourriez penser que chaque fois que `StreetLight` est rendu, il appelle `useState` avec une valeur de `'GREEN'`. Alors comment `color` peut-il être autre chose que vert ?

Une question logique. Voici quelques lignes des [docs React](https://reactjs.org/docs/hooks-state.html#declaring-a-state-variable) qui peuvent vous aider à vous _familiariser_ avec ce concept :

> « Normalement, les variables 'disparaissent' lorsque la fonction se termine, mais les variables d'état sont préservées par React. »

> « React se souviendra de sa valeur actuelle entre les re-rendus et fournira la plus récente à notre fonction. »

> « Vous pourriez vous demander : pourquoi _useState_ n'est-il pas nommé _createState_ ? 'Créer' ne serait pas tout à fait exact car l'état n'est créé que la première fois que notre composant est rendu. Lors des rendus suivants, _useState_ nous donne l'état actuel. »

#### Mais comment ?

**Ce n'est pas de la magie, c'est du JavaScript !**

En termes simples, React [garde une trace](https://reactjs.org/docs/hooks-faq.html#how-does-react-associate-hook-calls-with-components) des appels à `useState` pour chaque composant en interne. Il créera également une correspondance entre la fonction de mise à jour et la valeur de l'état qu'elle met à jour.

La valeur initiale passée à `useState` est retournée lors du premier rendu, mais à partir de là, React retournera la valeur correcte en fonction de la correspondance. Il utilise également la carte pour savoir quelle partie de l'état muté lorsque la fonction de mise à jour est appelée.

Cela peut vous sembler déconcertant, et vous n'êtes pas seul. J'ai été perplexe quant à la manière dont cela pouvait fonctionner. Ma confusion n'a fait qu'augmenter lorsque j'ai découvert que [vous pouvez avoir plusieurs appels](https://reactjs.org/docs/hooks-overview.html#declaring-multiple-state-variables) à `useState` dans le même composant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*M398xaKY5fQLcc6deYrvcQ.png)
_Créé avec [carbon.now.sh](https://carbon.now.sh" rel="noopener" target="_blank" title=")_

Oui, vous pouvez faire cela à votre guise.

### Comment React garde-t-il une trace de l'état ?

Pour que tout cela fonctionne, React s'attend à ce que vous suiviez [quelques règles](https://reactjs.org/docs/hooks-rules.html#explanation) :

1. N'appeler les hooks qu'au niveau supérieur d'une fonction
2. N'appeler les hooks que depuis des composants fonctionnels et des [hooks personnalisés](https://www.jakewiesler.com/blog/the-react-state-hook/#writing-a-custom-hook)

React impose ces règles car il [dépend de l'ordre d'appel des hooks](https://reactjs.org/docs/hooks-rules.html#explanation) pour gérer correctement les données. Cela peut sembler capricieux au premier abord, mais ces règles ne sont pas difficiles à suivre. Et franchement, je ne peux pas imaginer un scénario où vous voudriez les enfreindre.

Pour internaliser comment React gère les hooks dans vos composants, je vous _recommande vivement_ de lire [cet article Medium](https://medium.com/@ryardley/react-hooks-not-magic-just-arrays-cd4f1857236e) de [Rudi Yardley](https://medium.com/@ryardley). Il a été crucial dans mon processus d'apprentissage. ?

Et voici une [pseudo-implémentation](https://gist.github.com/gaearon/62866046e396f4de9b4827eae861ff19) de la manière dont React gère les hooks, initialement publiée par [jamiebuilds](https://mobile.twitter.com/jamiebuilds/status/1055538414538223616) sur Twitter.

### Conclusion

Je considère `useState` comme un bloc de construction. Vous pouvez l'utiliser _tel quel_ pour fournir un état à vos composants fonctionnels, ou vous pouvez l'utiliser pour abstraire la logique avec état dans des [hooks personnalisés](https://reactjs.org/docs/hooks-custom.html) !

Je crois que les hooks personnalisés seront le plus grand superpouvoir que les développeurs React gagneront lorsque la version `v16.7` sera publiée, et `useState` en est le fondement. La communauté partage déjà des [choses incroyables](https://github.com/rehooks/awesome-react-hooks) avec des hooks personnalisés et ce modèle ne fera que croître de manière exponentielle.

J'espère que vous avez trouvé cet article utile. N'hésitez pas à me contacter sur [Twitter](https://twitter.com/jakewies) si vous avez des questions, et comme toujours, bon codage !

_Originalement publié sur [www.jakewiesler.com](https://www.jakewiesler.com/blog/the-react-state-hook/)._

_Hé ami, merci d'avoir lu ! Je m'appelle [Jake](https://twitter.com/jakewies). J'adore construire des interfaces utilisateur et [j'écris à ce sujet](https://www.jakewiesler.com/) chaque semaine. Je gère également une petite newsletter appelée [**Original Copy**](https://www.jakewiesler.com/mail)**.** C'est une affaire décontractée et légère. Si cela vous semble intéressant, envisagez de vous abonner !_