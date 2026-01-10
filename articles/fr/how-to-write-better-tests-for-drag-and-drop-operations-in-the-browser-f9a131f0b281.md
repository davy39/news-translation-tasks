---
title: Comment écrire de meilleurs tests pour les opérations de glisser-déposer dans
  le navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T15:41:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-better-tests-for-drag-and-drop-operations-in-the-browser-f9a131f0b281
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0QbvXqleQASAZ0oaAfY66w.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: Comment écrire de meilleurs tests pour les opérations de glisser-déposer
  dans le navigateur
seo_desc: 'By Ronald Rey

  While keeping it framework-agnostic


  _Photo by [Unsplash](https://unsplash.com/photos/SHCViKw3edE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Ash Edmonds on <a href="https:...'
---

Par Ronald Rey

#### Tout en restant agnostique vis-à-vis des frameworks

![Image](https://cdn-media-1.freecodecamp.org/images/1*0QbvXqleQASAZ0oaAfY66w.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/SHCViKw3edE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ash Edmonds</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

En ce qui concerne les interactions courantes entre un utilisateur et une application web, il est généralement assez simple de simuler ces actions dans un environnement de test pour vérifier le bon fonctionnement d'une application. Je fais référence à des choses comme cliquer sur des boutons, remplir des formulaires, naviguer entre les routes... les trucs habituels. Cependant, il existe certaines expériences moins courantes sur le Web qui sont beaucoup plus difficiles à tester. L'une d'entre elles est la fonctionnalité de glisser-déposer.

Cela est en partie dû au fait que l'API HTML5 Drag and Drop est particulièrement cassée et incohérente. Cela a conduit de nombreux auteurs de bibliothèques à proposer leurs propres approches uniques du problème, souvent très différentes les unes des autres. Cela signifie que la mise en œuvre de telles fonctionnalités dans votre application peut être assez difficile, et pour un développeur inexpérimenté, il peut être encore plus difficile d'écrire les tests automatisés appropriés.

> Après avoir passé environ une journée et demie en test, je suis contraint de conclure que le module HTML5 drag and drop n'est pas seulement un désastre, c'est un putain de désastre.  
>   
> - [Peter-Paul Koch](https://www.quirksmode.org/blog/archives/2009/09/the_html5_drag.html)

À mon grand désespoir, l'application sur laquelle je travaille actuellement à temps plein comporte de nombreuses fonctionnalités de glisser-déposer partout. Heureusement, grâce à l'écosystème riche des bibliothèques qui ont déjà résolu ce problème et semblent l'avoir maîtrisé, cela a été relativement facile.

Cependant, tester automatiquement ces fonctionnalités peut être non trivial, et je souhaite partager certaines des leçons que j'ai apprises. J'utilise React, et beaucoup des extraits et exemples vont être centrés sur React. Mais en réalité, les mêmes concepts pourraient être appliqués à n'importe quelle stack, ce qui est la beauté de tout cela.

### L'approche initiale

D'accord, donc disons que je dois construire un tableau avec des lignes que l'on peut glisser et déposer, ressemblant à ceci (au fait, ne vous laissez pas trop distraire par l'implémentation) :

<iframe src="https://codesandbox.io/embed/github/reyronald/react-dnd-integration-testing-sample/tree/3f90cacea9f99fe7868daf00ffbccaa2611c87e3/?fontsize=14" title="react-dnd-integration-testing-sample" allow="geolocation; microphone; camera; midi; vr; accelerometer; gyroscope; payment; ambient-light-sensor; encrypted-media" style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;" sandbox="allow-modals allow-forms allow-popups allow-scripts allow-same-origin"></iframe>

![Image](https://cdn-media-1.freecodecamp.org/images/1*U6CwIMHmeOqoMJxOZke4sQ.gif)

Comme vous pouvez le voir, j'utilise la bibliothèque classique `react-dnd` du désormais célèbre Dan Abramov. La fonctionnalité est terminée, alors comment pourrions-nous la tester à ce stade ? Si vous consultez la documentation, vous trouverez une section "[Testing](http://react-dnd.github.io/react-dnd/docs-testing.html)" qui fera probablement briller vos yeux.

Il est suggéré d'utiliser le "test backend". Basiquement, vous enveloppez le composant décoré en utilisant ce backend au lieu du backend HTML5 habituel qu'ils fournissent. Cela vous permettra de le tester en dehors d'un environnement de navigateur, c'est-à-dire sans accès au DOM.

Dans cette dernière phrase du paragraphe précédent, je vous ai lancé beaucoup de concepts étranges : composant décoré, backend, backend de test, backend HTML5... quoi ? Ce sont tous des concepts internes sous-jacents de `react-dnd` et `dnd-core`, tous liés à son fonctionnement interne. Le guide lié lui-même admet cela, et indique que c'est la partie la moins documentée de la bibliothèque pour cette raison.

Cela signifie-t-il que je dois être compétent et familier avec le fonctionnement de cette bibliothèque en particulier pour pouvoir la tester ? Eh bien, pour moi, c'est ce que suggère la documentation. C'est délicat, car cela peut être trompeur pour les développeurs inexpérimentés.

En résumé, j'ai quelques griefs concernant leur approche suggérée :

1. Pour tester cette fonctionnalité, je dois être familier avec le fonctionnement interne de cette bibliothèque en particulier et ses détails d'implémentation.
2. Pour tester cette fonctionnalité, je dois également être familier avec le fonctionnement du "backend de test", ce qui est quelque chose que je n'ai pas besoin de connaître au départ pour construire une fonctionnalité de glisser-déposer en utilisant cette bibliothèque. Cela signifie que j'ai encore un autre ensemble de documentation à consulter, et une toute autre dimension de problèmes que je pourrais rencontrer et qui ne sont pas nécessairement partagés avec le backend HTML5 régulier que j'utiliserais pour mon application.
3. Le fait que j'ai une suite de tests complète et réussie en utilisant cette approche ne garantit pas nécessairement pour moi qu'elle fonctionne réellement comme je l'attends du point de vue de l'utilisateur. Réfléchissez-y : dans mes tests et dans la nature, la fonctionnalité fonctionnerait avec des internes complètement différents. Et malgré les meilleures intentions des mainteneurs, cette approche ne se généralise pas nécessairement bien au reste de l'écosystème JS, et peut vous donner un faux sentiment de sécurité.
4. Si je décide un jour de changer l'approche de la fonctionnalité et d'utiliser une autre bibliothèque à la place, ou de l'écrire moi-même, tous mes tests deviendront soudainement obsolètes et je devrai tous les réécrire.

Maintenant, ne vous méprenez pas - c'est génial qu'ils aient fait tant d'efforts pour créer un "backend de test" afin que la fonctionnalité puisse être testée sans le DOM. C'est certainement utile et a sa place. Mais ce n'est pas quelque chose que je recommanderais en raison des problèmes que je viens de lister.

Ce que je recherche, c'est ce qui suit :

1. Une suite de tests qui garantira dans la plus grande mesure que la fonctionnalité fonctionne comme prévu (il n'est pas possible d'atteindre 100% de certitude sans des tests de bout en bout, ce n'est pas sur quoi je me concentre pour le moment). Cela signifie que je veux vérifier le comportement exact de la fonctionnalité du point de vue de l'utilisateur dans mes tests.
2. Je peux échanger ou changer l'implémentation de la fonctionnalité (ce qui inclut toute bibliothèque utilisée en dessous) à tout moment avec un impact minimal sur les tests.
3. Je n'ai pas besoin d'être familier avec l'implémentation de la fonctionnalité pour écrire les tests.
4. Je n'ai qu'à utiliser mes connaissances déjà existantes et familières du Web et des API Web en général pour écrire ces tests.

### Avancer

Que recommanderais-je alors ? Eh bien, il suffit d'émuler dans vos tests ce qu'un utilisateur ferait en utilisant l'application. En gros, je préconise que vous écriviez des tests d'intégration complets pour cette fonctionnalité au lieu de tests unitaires / isolés, comme le suggère la documentation.

De nos jours, nous avons [jsdom](https://github.com/jsdom/jsdom) qui nous permet de lancer un environnement de navigateur haute fidélité en mémoire, sans utiliser un navigateur réel. Franchement, `jsdom` est devenu si bon au fil des ans que je ne vois presque aucune raison d'écrire des tests d'application web qui tentent de ne pas utiliser ou accéder au DOM. Virtuellement tout ce que vous pouvez faire dans une console de développement de navigateur peut être fait en mémoire avec `jsdom`, avec quelques exceptions et mises en garde, bien sûr, que nous verrons sous peu.

_AVERTISSEMENT : Je ne dis pas que vous ne devriez jamais écrire de tests unitaires, ou des tests de cette manière. Certes, chaque scénario et problème est différent. Mettez votre casque de réflexion et décidez ce qui est le mieux au cas par cas !_

D'accord, alors, comment faisons-nous cela ? C'est simple, posez-vous la question : que ferait l'utilisateur avec mon application pour utiliser la fonctionnalité de glisser-déposer, et comment le navigateur se comporte-t-il lorsque cela se produit ? Lorsque vous avez cette réponse, codez cela dans un test en utilisant les API DOM régulières rendues accessibles par `jsdom` ! Voyons à quoi ressemblerait un test pour une action de glisser vers le bas pour notre exemple particulier en utilisant `jest` :

```js
const getTableCells = () =>
  Array.from(mountNode.querySelectorAll("tr td:nth-of-type(1)"));
const createBubbledEvent = (type, props = {}) => {
  const event = new Event(type, { bubbles: true });
  Object.assign(event, props);
  return event;
};
const tableCells = getTableCells();
const startingNode = tableCells[0];
const endingNode = tableCells[2];
startingNode.dispatchEvent(
  createBubbledEvent("dragstart", { clientX: 0, clientY: 0 })
);
endingNode.dispatchEvent(
  createBubbledEvent("drop", { clientX: 0, clientY: 1 })
);
expect(getTableCells().map(cell => cell.textContent)).toEqual([
  "Bob",
  "Clark",
  "Alice",
]);
```

Il n'y a absolument rien de spécifique à `react-dnd` ou même à React dans cet extrait, et il n'utilise même pas React Test Utils' Simulate. Cela signifie que je pourrais même changer ma bibliothèque/framework UI pour quelque chose comme Angular (bon sang, même Backbone, quelqu'un ?) et ce test aura toujours du sens et fonctionnera comme prévu.

Cela seul est suffisant pour tester correctement ce sous-ensemble de la fonctionnalité, cependant, il y a beaucoup d'autres événements qui se produisent dans un navigateur réel (`mousedown`, `mousemove`, `dragend`, etc.) qui n'ont pas joué de rôle dans notre implémentation. Cela signifie qu'avec une implémentation différente, il est possible que le test nécessite quelques ajouts ou suppressions.

(En passant, l'utilisation de Simulate est ouvertement découragée par les experts de l'industrie. De plus, si vous avez passé plus de 5 minutes sur l'un des problèmes GitHub liés au système d'événements d'Enzyme, vous verrez la même opinion des auteurs eux-mêmes. [Il y a même eu des commentaires sur sa suppression dans les prochaines versions](https://github.com/airbnb/enzyme/issues/1357#issuecomment-404673556)).

%[https://twitter.com/dan_abramov/status/980807288444383232?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdan_abramov%2Fstatus%2F980807288444383232%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F906557353549598720%25252FoapgW_Fp_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Les quelques choses qui ne sont pas nécessairement évidentes sont :

* Les événements doivent se propager, ce qui n'est pas le cas par défaut lorsque nous les créons manuellement avec le constructeur - nous devons donc le définir explicitement. Cela est lié au fonctionnement du système de délégation d'événements de React. Vous pourriez penser que c'est un détail d'implémentation, mais ce n'est pas nécessairement le cas. Les événements se propagent dans le navigateur lorsqu'ils sont déclenchés par une interaction réelle.
* Nous devons définir les propriétés `clientX` et `clientY` de l'événement, car elles sont utilisées pour déterminer la direction du glisser. Encore une fois, avec une autre implémentation, il pourrait y avoir d'autres propriétés sur les événements ou d'autres méthodes que vous devrez corriger pour que cela fonctionne (comme `.getBoundingClientRect()`). Par exemple, si l'implémentation utilisait quelque chose comme `.offsetX`, `.movementX`, `.top` ou toute autre propriété liée à la taille, à la position et au mouvement.

Et c'est à peu près tout. Nous avons abordé tous mes problèmes et atteint tous les objectifs que nous nous étions fixés. Avec quelques lignes de code supplémentaires, il est possible d'atteindre une couverture de test de 100 % pour ce dépôt assez facilement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*86rgI6XsYdNw7lRs16Fz_w.png)
_N'est-ce pas magnifique ?_

### Réflexions finales

N'hésitez pas à explorer l'ensemble de la suite de tests [ici](https://codesandbox.io/s/github/reyronald/react-dnd-integration-testing-sample). Quelques éléments supplémentaires sont en place pour obtenir une couverture de 100 %, alors assurez-vous de le vérifier. Notez que j'ai tout écrit dans un seul test juste pour la brièveté.

Une autre chose que je voudrais mentionner. Un nouveau développeur pourrait arriver dans le code des tests et savoir exactement ce qui se passe. Imaginez si les tests utilisaient les tests orientés `react-dnd`, utilisant toutes sortes de concepts et de détails internes... ce serait un énorme mur devant eux et pourrait poser un obstacle substantiel à leur capacité à contribuer aux tests dans un délai raisonnable. À ce moment-là, ils devraient aller lire la documentation de `react-dnd`, `dnd-core` et le code source de `react-testing-backend`... aïe !

Je veux vous laisser avec cet article de blog de Sophie Alpert, manager de l'équipe React Core chez Facebook, décrivant comment ils ont pu livrer une réécriture complète compatible avec l'API des internes de React de la version 15 à la version 16 en toute sécurité sans une seule rupture. Spoiler : les suites de tests complètes ont vérifié la fonctionnalité de la bibliothèque du point de vue d'un outsider, au lieu de se concentrer sur les détails d'implémentation ou les tests unitaires isolés.

Ce qui est vraiment drôle, c'est qu'en juillet 2018, tous les extraits de la documentation officielle de React utilisaient une version 0.14 obsolète, et il s'est avéré qu'ils fonctionnaient exactement de la même manière dans la version 16.x. Cela montre simplement le excellent travail qu'ils ont fait pour maintenir la compatibilité ascendante, et cela n'aurait pas été possible sans ces tests bien écrits et ciblés !

[**React 16 : Un regard à l'intérieur d'une réécriture compatible avec l'API de notre bibliothèque UI frontend**](https://code.fb.com/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/)  
[_PUBLIÉ SUR TO Web React 16 : Un regard à l'intérieur d'une réécriture compatible avec l'API de notre bibliothèque UI frontend React rend simple de..._](https://code.fb.com/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/)  
[code.fb.com](https://code.fb.com/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/)

%[https://twitter.com/dan_abramov/status/1017409804308905986?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdan_abramov%2Fstatus%2F1017409804308905986%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F906557353549598720%25252FoapgW_Fp_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

### Bonus : Quelques conseils pour comprendre comment émuler le comportement du navigateur

Si vous souhaitez tester une autre fonctionnalité de cette manière, mais que vous n'êtes pas sûr du comportement exact du navigateur lors de son exécution, je vous suggère de consulter l'API `monitorEvents` de [Google Chrome](https://developers.google.com/web/tools/chrome-devtools/console/events). Elle est incroyablement utile dans ces scénarios, surtout lorsque vous n'êtes pas sûr de ce qui se passe. Je l'ai moi-même utilisée pour explorer la forme des événements déclenchés lors du glisser-déposer :

```
monitorEvents(document.body, [
  'mousedown',

  'mousemove',

  'dragstart',

  'dragenter',

  'dragover',

  'drop',

  'dragend',

  'mouseup',
  
  // 
  
])
```

En général, il serait extrêmement bénéfique de simplement ouvrir une console de développement de navigateur et de commencer à jouer avec le système d'événements jusqu'à ce que vous vous sentiez confiant de savoir comment il fonctionne. Créez des éléments, déclenchez des événements, déplacez-les, attachez-les au DOM, détachez-les, etc. ... tout ce qu'il faut ! Investir une ou quelques heures avec cela vous servira pour le reste de votre carrière en tant que développeur web. Une affaire plutôt intéressante à mes yeux :)