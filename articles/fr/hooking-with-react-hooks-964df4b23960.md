---
title: 'React Hooks : une nouvelle façon de travailler avec l''état de React'
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2018-11-08T15:54:15.000Z'
originalURL: https://freecodecamp.org/news/hooking-with-react-hooks-964df4b23960
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UNln2JsoPZEVzgGPJhs98w.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'React Hooks : une nouvelle façon de travailler avec l''état de React'
seo_desc: 'Updated: With React 16.8, React Hooks are available in a stable release!

  Outdated: Hooks are still an experimental proposal. They’re currently in React v16.7.0-alpha

  TL;DRIn this article we will attempt to understand what are React Hooks and how
  to u...'
---

**Mis à jour : Avec React 16.8,** [**React Hooks**](https://reactjs.org/docs/hooks-intro.html) **sont disponibles dans une version stable !**

Obsolète : Les Hooks sont encore une proposition expérimentale. Ils sont actuellement dans React v16.7.0-alpha

**TL;DR**  
Dans cet article, nous allons essayer de comprendre ce que sont les [React Hooks](https://reactjs.org/docs/hooks-intro.html) et comment les utiliser à notre avantage. Nous allons implémenter différents exemples et voir les différences (gains) que les Hooks nous apportent. Si vous souhaitez sauter la lecture, [ici](https://mihailgaberov.github.io/react-hooks/) vous pouvez trouver une version plus courte en quelques diapositives. Et [ici](https://github.com/mihailgaberov/react-hooks) ? vous pouvez obtenir les exemples et les essayer vous-même.

### Qu'est-ce que les *React Hooks* ?

> Des fonctions simples pour s'interfacer avec l'état et les fonctionnalités du cycle de vie de React depuis des composants fonctionnels.

Cela signifie que les hooks nous permettent de manipuler facilement l'état de notre composant fonctionnel sans avoir besoin de les convertir en composants de classe. Cela nous évite d'avoir à gérer tout le code boilerplate impliqué.

Les Hooks ne fonctionnent pas à l'intérieur des classes — ils vous permettent d'utiliser React sans classes. Et aussi, en les utilisant, nous pouvons totalement éviter d'utiliser les méthodes de cycle de vie, telles que *componentDidMount*, *componentDidUpdate*, etc. À la place, nous utiliserons des hooks intégrés comme *useEffect*, *useMutationEffect* ou *useLayoutEffect*. Nous verrons comment dans un instant.

Les Hooks sont des fonctions JavaScript, mais elles imposent deux règles supplémentaires :

⚠️ N'appeler les Hooks **qu'au niveau supérieur**. N'appeler pas les Hooks à l'intérieur des boucles, des conditions ou des fonctions imbriquées.

⚠️ N'appeler les Hooks **qu'à partir de composants fonctionnels React**. N'appeler pas les Hooks à partir de fonctions JavaScript régulières. Il n'y a qu'un seul autre endroit valide pour appeler les Hooks — vos propres Hooks personnalisés. Nous les verrons plus tard dans cet article.

### Pourquoi sont-ils *une bonne chose* ?

? **Réutilisation de la logique**  
Jusqu'à présent, si nous voulions réutiliser une certaine logique dans React, nous avions deux options : les [composants d'ordre supérieur](https://tylermcginnis.com/react-higher-order-components/) ou les [props de rendu](https://www.robinwieruch.de/react-render-props-pattern/). Avec les React Hooks, nous avons une alternative, qui vient avec une syntaxe et un flux logique beaucoup plus faciles à comprendre (à mon avis personnel !).

? **Composants géants**  
En évitant le code boilerplate que nous devons écrire lors de l'utilisation de classes ou en supprimant le besoin de plusieurs niveaux de nesting (qui pourraient survenir lors de l'utilisation des props de rendu), les React Hooks résolvent le problème des composants géants (qui sont vraiment difficiles à maintenir et à déboguer).

? **Classes confuses**  
Encore une fois, nous permettre de NE PAS utiliser de classes ou de composants de classe dans nos applications facilite la vie des développeurs (surtout des débutants). Cela est dû au fait que nous n'avons pas à utiliser le mot-clé 'this' et nous n'avons pas besoin de comprendre comment les liaisons et les portées fonctionnent dans React (et JavaScript).

Cela ne signifie PAS que nous (les développeurs) n'avons pas à apprendre ces concepts — au contraire, nous devons en être conscients. Mais dans ce cas, lorsque nous utilisons les hooks React, nos soucis sont un de moins ?.

> ***Donc, après avoir souligné les problèmes que les hooks résolvent, quand les utiliserions-nous ?***

> *Si vous écrivez un composant fonctionnel et réalisez que vous devez ajouter un état, auparavant vous deviez le convertir en classe. Maintenant, vous pouvez utiliser un Hook à l'intérieur du composant fonctionnel existant. Nous allons faire cela dans les prochains exemples.*

### Comment utiliser les *React Hooks* ?

Les React Hooks nous sont proposés sous forme de [hooks intégrés](https://reactjs.org/docs/hooks-overview.html) et de [hooks personnalisés](https://reactjs.org/docs/hooks-custom.html). Ces derniers sont ceux que nous pouvons utiliser pour partager la logique entre plusieurs composants React.

Comme nous l'avons déjà appris, les hooks sont des fonctions JavaScript simples, ce qui signifie que nous allons écrire juste cela, mais dans le contexte des composants *fonctionnels* React. Auparavant, ces composants étaient appelés *stateless*, un terme qui n'est plus valide, car les *hooks* nous donnent un moyen d'utiliser l'état dans de tels composants ?.

> *Une chose importante à retenir est que nous pouvons utiliser à la fois les hooks intégrés et personnalisés plusieurs fois dans nos composants. Nous devons simplement suivre les* [*règles des hooks*](https://reactjs.org/docs/hooks-rules.html)*.*

Les exemples suivants tentent de l'illustrer.

#### Hooks intégrés de base

* [useState](https://github.com/mihailgaberov/react-hooks/blob/master/src/components/Counter/CounterHooked.js) hook — retourne une valeur avec état et une fonction pour la mettre à jour.
    
* [useEffect](https://reactjs.org/docs/hooks-effect.html) hook — accepte une fonction qui contient du code impératif, éventuellement effectif (par exemple, récupérer des données ou s'abonner à un service). Ce hook pourrait retourner une fonction qui est exécutée chaque fois avant que l'effet ne s'exécute et lorsque le composant est démonté — pour nettoyer la dernière exécution.
    
* [useContext](https://github.com/mihailgaberov/react-hooks/blob/master/src/components/Counter/CounterHooked.js) hook — accepte un objet [contexte](https://reactjs.org/docs/context.html) et retourne la valeur [contexte](https://github.com/mihailgaberov/react-hooks/blob/master/src/ColorContext.js) actuelle, telle que donnée par le fournisseur de contexte le plus proche pour le contexte donné.
    

#### Hooks personnalisés

**Un Hook personnalisé est une fonction JavaScript dont le nom commence par «**`use`**» et qui peut appeler d'autres Hooks. Par exemple, [useFriendName](https://github.com/mihailgaberov/react-hooks/blob/master/src/useFriendName.jshttps://github.com/mihailgaberov/react-hooks/blob/master/src/useFriendName.js) ci-dessous est notre premier Hook personnalisé :

```js
export default function useFriendName(friendName) {
  const [isPresent, setIsPresent] = useState(false);
  
  useEffect(() => {
    const data = MockedApi.fetchData();
    data.then((res) => {
      res.forEach((e) => {
        if (e.name === friendName) {
          setIsPresent(true);
        }
     });
    });
  });
    
  return isPresent;
}
```

Créer vos propres hooks personnalisés vous permet d'extraire la logique des composants dans des fonctions réutilisables. Cela pourrait être la fonctionnalité partagée de votre application que vous pouvez importer partout où vous en avez besoin. Et aussi, nous ne devons pas oublier que nos hooks personnalisés sont les autres endroits autorisés ([voir les règles](https://reactjs.org/docs/hooks-rules.html#only-call-hooks-from-react-functions)) pour appeler les hooks intégrés.

### Conclusion

Les React Hooks ne sont pas vraiment une nouvelle fonctionnalité qui vient d'apparaître. Ils sont une autre (meilleure ✳️) façon de faire des composants React qui doivent avoir un *état* et/ou des méthodes de *cycle de vie*. En fait, ils utilisent la même logique interne qui est actuellement utilisée par les composants de classe. Les utiliser ou non — c'est la question à laquelle l'avenir donnera la meilleure réponse.

> *Mon opinion personnelle ? Que ce sera l'avenir de tout développement React impliquant l'utilisation d'état et de cycle de vie.*

Voyons comment la communauté réagira à la proposition ? et espérons que nous les verrons polies et pleinement fonctionnelles dans les prochaines versions de React. ?

? Merci pour la lecture ! ?

### Références

Voici les liens vers les ressources que j'ai trouvées utiles lors de la rédaction de cet article :

* [https://github.com/mihailgaberov/react-hooks](https://github.com/mihailgaberov/react-hooks)/ — lien vers le dépôt GitHub avec les exemples et la présentation.
    
* [https://mihailgaberov.github.io/react-hooks/](https://mihailgaberov.github.io/react-hooks/#0) — lien vers les diapositives de la présentation.
    
* [https://reactjs.org/docs/hooks-intro.html](https://reactjs.org/docs/hooks-intro.html) — blog officiel ReactJS.
    
* [https://youtu.be/dpw9EHDh2bM](https://youtu.be/dpw9EHDh2bM) — Introduction aux Hooks, React Conf 2018
    
* [https://medium.com/@dan\_abramov/making-sense-of-react-hooks-fdbde8803889](https://medium.com/@dan_abramov/making-sense-of-react-hooks-fdbde8803889) — Un article explicatif de Dan Abramov.
    
* [https://daveceddia.com/useeffect-hook-examples/](https://daveceddia.com/useeffect-hook-examples/) — Un article très utile expliquant différents cas d'utilisation du hook useEffect.
    
* [https://ppxnl191zx.codesandbox.io/](https://ppxnl191zx.codesandbox.io/) — Un exemple de bibliothèque d'animation React expérimentant avec les Hooks.
    
* [https://dev.to/oieduardorabelo/react-hooks-how-to-create-and-update-contextprovider-1f68](https://dev.to/oieduardorabelo/react-hooks-how-to-create-and-update-contextprovider-1f68) — Un article court et intéressant montrant comment créer et mettre à jour un fournisseur de contexte avec les React Hooks.