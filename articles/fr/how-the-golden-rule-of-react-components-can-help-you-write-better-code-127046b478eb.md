---
title: Comment la « Règle d'or » des composants React peut vous aider à écrire un
  meilleur code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T21:23:23.000Z'
originalURL: https://freecodecamp.org/news/how-the-golden-rule-of-react-components-can-help-you-write-better-code-127046b478eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KzKoXW7PovSAUUn8htYbnw@2x.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment la « Règle d'or » des composants React peut vous aider à écrire
  un meilleur code
seo_desc: 'By Rico Kahler

  And how hooks come into play

  Recently I’ve adopted a new philosophy that changes the way I make components. It’s
  not necessarily a new idea but rather a subtle new way of thinking.

  The Golden Rule of Components


  Create and define compo...'
---

Par Rico Kahler

#### Et comment les hooks entrent en jeu

Récemment, j'ai adopté une nouvelle philosophie qui change la façon dont je crée des composants. Ce n'est pas nécessairement une nouvelle idée, mais plutôt une nouvelle façon subtile de penser.

#### La Règle d'or des composants

> Créez et définissez des composants de la manière la plus naturelle, en considérant uniquement ce dont ils ont besoin pour fonctionner.

Encore une fois, c'est une déclaration subtile et vous pouvez penser que vous la suivez déjà, mais il est facile d'aller à l'encontre de cela.

Par exemple, disons que vous avez le composant suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nF_5kuYHigZuwdq99vRJ8g.png)
_PersonCard_

Si vous définissiez ce composant « naturellement », vous l'écririez probablement avec l'API suivante :

```js
PersonCard.propTypes = {
  name: PropTypes.string.isRequired,
  jobTitle: PropTypes.string.isRequired,
  pictureUrl: PropTypes.string.isRequired,
};
```

Ce qui est assez simple — en regardant uniquement ce dont il a besoin pour fonctionner, vous avez juste besoin d'un nom, d'un titre de poste et d'une URL de photo.

Mais disons que vous avez une exigence pour afficher une photo « officielle » en fonction des paramètres de l'utilisateur. Vous pourriez être tenté d'écrire une API comme suit :

```js
PersonCard.propTypes = {
  name: PropTypes.string.isRequired,
  jobTitle: PropTypes.string.isRequired,
  officialPictureUrl: PropTypes.string.isRequired,
  pictureUrl: PropTypes.string.isRequired,
  preferOfficial: PropTypes.boolean.isRequired,
};
```

Il peut sembler que le composant a besoin de ces props supplémentaires pour fonctionner, mais en réalité, le composant ne semble pas différent et n'a pas besoin de ces props supplémentaires pour fonctionner. Ce que ces props supplémentaires font, c'est coupler ce paramètre `preferOfficial` avec votre composant et rendre toute utilisation du composant en dehors de ce contexte vraiment peu naturelle.

### Combler l'écart

Donc, si la logique de changement de l'URL de la photo n'appartient pas au composant lui-même, où doit-elle se trouver ?

Et si un fichier `index` ?

Nous avons adopté une structure de dossier où chaque composant va dans un dossier auto-titré où le fichier `index` est responsable de combler l'écart entre votre composant « naturel » et le monde extérieur. Nous appelons ce fichier le « conteneur » (inspiré du concept de composants « conteneur » de [React Redux](https://redux.js.org/basics/usage-with-react#presentational-and-container-components)).

```
/PersonCard
  -PersonCard.js ------ le composant "naturel"
  -index.js ----------- le "conteneur"
```

Nous définissons les **conteneurs** comme le morceau de code qui comble l'écart entre votre composant naturel et le monde extérieur. Pour cette raison, nous appelons parfois ces choses des « injecteurs ».

Votre **composant naturel** est le code que vous créeriez si vous ne voyiez qu'une image de ce que vous deviez faire (sans les détails de la façon dont vous obtiendriez les données ou où elles seraient placées dans l'application — tout ce que vous savez, c'est qu'il devrait fonctionner).

Le **monde extérieur** est un mot-clé que nous utiliserons pour désigner toute ressource que votre application possède (par exemple, le store Redux) qui peut être transformée pour satisfaire les props de votre composant naturel.

**Objectif de cet article :** Comment pouvons-nous garder les composants « naturels » sans les polluer avec des éléments inutiles du monde extérieur ? Pourquoi est-ce mieux ?

> **_Note:_** _Bien qu'inspiré par la terminologie de [Dan Abramov](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) et de [React Redux](https://redux.js.org/basics/usage-with-react#presentational-and-container-components), notre définition des « conteneurs » va légèrement au-delà et est subtilement différente._

> _La seule différence entre le [conteneur de Dan Abramov](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) et le nôtre est seulement au niveau conceptuel. Dan dit qu'il existe deux types de composants : les composants de présentation et les composants conteneurs. Nous allons plus loin et disons qu'il existe des composants et ensuite des conteneurs._

> _Même si nous implémentons des conteneurs avec des composants, nous ne considérons pas les conteneurs comme des composants au niveau conceptuel. C'est pourquoi nous recommandons de mettre votre conteneur dans le fichier `index` — parce que c'est un pont entre votre composant naturel et le monde extérieur et qu'il ne se suffit pas à lui-même._

Bien que cet article soit centré sur les composants, les conteneurs occupent la majeure partie de cet article.

Pourquoi ?

Créer des composants naturels — Facile, amusant même.  
Connecter vos composants au monde extérieur — Un peu plus difficile.

À mon avis, il y a trois raisons majeures pour lesquelles vous pollueriez votre composant naturel avec des éléments inutiles du monde extérieur :

1. Structures de données étranges
2. Exigences en dehors du champ d'application du composant (comme l'exemple ci-dessus)
3. Déclenchement d'événements lors de mises à jour ou de montages

Les prochaines sections tenteront de couvrir ces situations avec des exemples de différentes implémentations de conteneurs.

### Travailler avec des structures de données étranges

Parfois, pour afficher les informations requises, vous devez lier des données et les transformer en quelque chose de plus sensé. Par manque d'un meilleur terme, les structures de données « étranges » sont simplement des structures de données qui sont peu naturelles pour votre composant à utiliser.

Il est très tentant de passer directement des structures de données étranges dans un composant et de faire la transformation à l'intérieur du composant lui-même, mais cela conduit à des composants confus et souvent difficiles à tester.

Je me suis surpris à tomber dans ce piège récemment lorsque j'ai été chargé de créer un composant qui obtenait ses données à partir d'une structure de données particulière que nous utilisons pour supporter un type particulier de formulaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hFOPWOxkedUEb851jdAXjA.gif)
_Le composant lui-même_

```js
ChipField.propTypes = {
  field: PropTypes.object.isRequired,      // <-- la structure de données "étrange"
  onEditField: PropTypes.func.isRequired,  // <-- et un événement étrange aussi
};
```

Le composant prenait cette structure de données étrange `field` en tant que prop. En pratique, cela aurait pu être bien si nous n'avions jamais eu à toucher à cette chose à nouveau, mais cela est devenu un vrai problème lorsque nous avons été invités à l'utiliser à nouveau dans un endroit différent sans rapport avec cette structure de données.

Puisque le composant nécessitait cette structure de données, il était impossible de la réutiliser et il était confus de la refactoriser. Les tests que nous avions initialement écrits étaient également confus car ils simulaient cette structure de données étrange. Nous avons eu du mal à comprendre les tests et à les réécrire lorsque nous avons finalement refactorisé.

Malheureusement, les structures de données étranges sont inévitables, mais l'utilisation de conteneurs est un excellent moyen de les gérer. Une conclusion ici est que l'architecture de vos composants de cette manière vous donne l'_option_ d'extraire et de faire évoluer le composant en un composant réutilisable. Si vous passez une structure de données étrange dans un composant, vous perdez cette option.

> **_Note:_** _Je ne suggère pas que tous les composants que vous créez doivent être génériques dès le début. La suggestion est de réfléchir à ce que fait votre composant à un niveau fondamental et ensuite de combler l'écart. En conséquence, vous êtes plus susceptible d'avoir l'_option_ de faire évoluer votre composant en un composant réutilisable avec un travail minimal._

#### Implémentation de conteneurs utilisant des composants fonctionnels

Si vous mappez strictement des props, une option d'implémentation simple est d'utiliser un autre composant fonctionnel :

```js
import React from 'react';
import PropTypes from 'prop-types';

import getValuesFromField from './helpers/getValuesFromField';
import transformValuesToField from './helpers/transformValuesToField';

import ChipField from './ChipField';

export default function ChipFieldContainer({ field, onEditField }) {
  const values = getValuesFromField(field);
  
  function handleOnChange(values) {
    onEditField(transformValuesToField(values));
  }
  
  return <ChipField values={values} onChange={handleOnChange} />;
}

// external props
ChipFieldContainer.propTypes = {
  field: PropTypes.object.isRequired,
  onEditField: PropTypes.func.isRequired,
};
```

Et la structure de dossier pour un composant comme celui-ci ressemble à quelque chose comme :

```
/ChipField
  -ChipField.js ------------------ la partie "naturelle" du champ de puce
  -ChipField.test.js
  -index.js ---------------------- le "conteneur"
  -index.test.js
  /helpers ----------------------- un dossier pour les helpers/utils
    -getValuesFromField.js
    -getValuesFromField.test.js
    -transformValuesToField.js
    -transformValuesToField.test.js
```

Vous pourriez penser "c'est trop de travail" — et si vous le pensez, je comprends. Il peut sembler qu'il y a plus de travail à faire ici puisque il y a plus de fichiers et un peu d'indirection, mais voici la partie que vous manquez :

```js
import { connect } from 'react-redux';

import getPictureUrl from './helpers/getPictureUrl';

import PersonCard from './PersonCard';

const mapStateToProps = (state, ownProps) => {
  const { person } = ownProps;
  const { name, jobTitle, customPictureUrl, officialPictureUrl } = person;
  const { preferOfficial } = state.settings;
  
  const pictureUrl = getPictureUrl(preferOfficial, customPictureUrl, officialPictureUrl);
  
  return { name, jobTitle, pictureUrl };
};

const mapDispatchToProps = null;

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(PersonCard);
```

C'est toujours la même quantité de travail, que vous transformiez les données à l'extérieur ou à l'intérieur du composant. La différence est que lorsque vous transformez les données à l'extérieur du composant, vous vous donnez un endroit plus explicite pour tester que vos transformations sont correctes tout en séparant les préoccupations.

### Satisfaire les exigences en dehors du champ d'application du composant

Comme dans l'exemple de la carte de personne ci-dessus, il est très probable que lorsque vous adoptez cette « règle d'or » de pensée, vous réalisiez que certaines exigences sont en dehors du champ d'application du composant réel. Alors, comment les satisfaire ?

Vous l'avez deviné : les conteneurs ?

Vous pouvez créer des conteneurs qui font un peu de travail supplémentaire pour garder votre composant naturel. Lorsque vous faites cela, vous obtenez un composant plus ciblé qui est beaucoup plus simple et un conteneur qui est mieux testé.

Implémentons un conteneur PersonCard pour illustrer l'exemple.

#### Implémentation de conteneurs utilisant des composants d'ordre supérieur

React Redux utilise des [composants d'ordre supérieur](https://reactjs.org/docs/higher-order-components.html) pour implémenter des conteneurs qui poussent et mappent les props du store Redux. Puisque nous avons obtenu cette terminologie de React Redux, il n'est pas surprenant que le [connect de React Redux soit un conteneur](https://redux.js.org/basics/usage-with-react#implementing-container-components).

Quoi qu'il en soit, si vous utilisez un composant fonctionnel pour mapper les props, ou si vous utilisez des composants d'ordre supérieur pour vous connecter au store Redux, la règle d'or et le travail du conteneur restent les mêmes. Tout d'abord, écrivez votre composant naturel, puis utilisez le composant d'ordre supérieur pour combler l'écart.

Structure de dossier pour ce qui précède :

```
/PersonCard
  -PersonCard.js ----------------- composant naturel
  -PersonCard.test.js
  -index.js ---------------------- conteneur
  -index.test.js
  /helpers
    -getPictureUrl.js ------------ helper
    -getPictureUrl.test.js
```

> **_Note:_** _Dans ce cas, il ne serait pas trop pratique d'avoir un helper pour `getPictureUrl`. Cette logique a été séparée simplement pour montrer que vous pouvez le faire. Vous avez peut-être aussi remarqué qu'il n'y a pas de différence dans la structure de dossier quelle que soit l'implémentation du conteneur._

Si vous avez déjà utilisé Redux, l'exemple ci-dessus est probablement quelque chose que vous connaissez déjà. Encore une fois, cette règle d'or n'est pas nécessairement une nouvelle idée, mais une nouvelle façon subtile de penser.

De plus, lorsque vous implémentez des conteneurs avec des composants d'ordre supérieur, vous avez également la possibilité de composer fonctionnellement des composants d'ordre supérieur ensemble — en passant des props d'un composant d'ordre supérieur à l'autre. Historiquement, nous avons enchaîné plusieurs composants d'ordre supérieur ensemble pour implémenter un seul conteneur.

> **_Note 2019:_** _La communauté React semble s'éloigner des composants d'ordre supérieur en tant que modèle._

> _Je recommanderais également la même chose. Mon expérience lorsque je travaille avec ceux-ci est qu'ils peuvent être déroutants pour les membres de l'équipe qui ne sont pas familiers avec la composition fonctionnelle et ils peuvent causer ce que l'on appelle l'"enfer des wrappers" où les composants sont enveloppés trop de fois, causant des problèmes de performance significatifs._

> _Voici quelques articles et ressources connexes à ce sujet : [Discours sur les Hooks](https://youtu.be/dpw9EHDh2bM?t=710) (2018) [Discours sur Recompose](https://youtu.be/zD_judE-bXk?t=1101) (2016), [Utilisez une Render Prop !](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce) (2017), [Quand NE PAS utiliser les Render Props](https://blog.kentcdodds.com/when-to-not-use-render-props-5397bbeff746) (2018)._

### Vous m'avez promis des hooks

#### Implémentation de conteneurs utilisant des hooks

Pourquoi les hooks sont-ils présentés dans cet article ? Parce que l'implémentation de conteneurs devient beaucoup plus facile avec les hooks.

Si vous n'êtes pas familier avec les hooks React, alors je vous recommande de regarder [les discours de Dan Abramov et Ryan Florence introduisant le concept lors de la React Conf 2018](https://youtu.be/dpw9EHDh2bM).

L'essentiel est que les hooks sont la réponse de l'équipe React aux problèmes avec les [composants d'ordre supérieur](https://reactjs.org/docs/higher-order-components.html) et les [modèles similaires](https://reactjs.org/docs/render-props.html). Les hooks React sont destinés à être un modèle de remplacement supérieur pour les deux dans la plupart des cas.

Cela signifie que l'implémentation de conteneurs peut être faite avec un composant fonctionnel et des hooks ?

Dans l'exemple ci-dessous, nous utilisons les hooks `useRoute` et `useRedux` pour représenter le « monde extérieur » et nous utilisons le helper `getValues` pour mapper le monde extérieur en `props` utilisables par votre composant naturel. Nous utilisons également le helper `transformValues` pour transformer la sortie de votre composant vers le monde extérieur représenté par `dispatch`.

```js
import React from 'react';
import PropTypes from 'prop-types';

import { useRouter } from 'react-router';
import { useRedux } from 'react-redux';

import actionCreator from 'your-redux-stuff';

import getValues from './helpers/getVaules';
import transformValues from './helpers/transformValues';

import FooComponent from './FooComponent';

export default function FooComponentContainer(props) {
  // hooks
  const { match } = useRouter({ path: /* ... */ });
  // NOTE: `useRedux` does not exist yet and probably won't look like this
  const { state, dispatch } = useRedux();

  // mapping
  const props = getValues(state, match);
  
  function handleChange(e) {
    const transformed = transformValues(e);
    dispatch(actionCreator(transformed));
  }
  
  // natural component
  return <FooComponent {...props} onChange={handleChange} />;
}

FooComponentContainer.propTypes = { /* ... */ };
```

Et voici la structure de dossier de référence :

```
/FooComponent ----------- le composant entier pour que les autres l'importent
  -FooComponent.js ------ la partie "naturelle" du composant
  -FooComponent.test.js
  -index.js ------------- le "conteneur" qui comble l'écart
  -index.js.test.js         et fournit les dépendances
  /helpers -------------- helpers isolés que vous pouvez tester facilement
    -getValues.js
    -getValues.test.js
    -transformValues.js
    -transformValues.test.js
```

### Déclenchement d'événements dans les conteneurs

Le dernier type de scénario où je m'éloigne d'un composant naturel est lorsque je dois déclencher des événements liés à des props changeantes ou au montage de composants.

Par exemple, disons que vous êtes chargé de créer un tableau de bord. L'équipe de design vous remet une maquette du tableau de bord et vous la transformez en un composant React. Vous en êtes maintenant au point où vous devez remplir ce tableau de bord avec des données.

Vous remarquez que vous devez appeler une fonction (par exemple, `dispatch(fetchAction)`) lorsque votre composant est monté pour que cela se produise.

Dans des scénarios comme celui-ci, je me suis retrouvé à ajouter des méthodes de cycle de vie `componentDidMount` et `componentDidUpdate` et à ajouter des props `onMount` ou `onDashboardIdChanged` parce que j'avais besoin que certains événements se déclenchent pour lier mon composant au monde extérieur.

En suivant la règle d'or, ces props `onMount` et `onDashboardIdChanged` sont peu naturelles et doivent donc vivre dans le conteneur.

Le bon côté des hooks est qu'ils rendent le déclenchement d'événements `onMount` ou lors de changements de props beaucoup plus simple !

**Déclenchement d'événements au montage :**

Pour déclencher un événement au montage, appelez `useEffect` avec un tableau vide.

```js
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { useRedux } from 'react-redux';

import fetchSomething_reduxAction from 'your-redux-stuff';
import getValues from './helpers/getVaules';
import FooComponent from './FooComponent';

export default function FooComponentContainer(props) {
  // hooks
  // NOTE: `useRedux` does not exist yet and probably won't look like this
  const { state, dispatch } = useRedux();
  
  // dispatch action onMount
  useEffect(() => {
    dispatch(fetchSomething_reduxAction);
  }, []); // le tableau vide indique à React de ne déclencher qu'au montage
  // https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects

  // mapping
  const props = getValues(state, match);
  
  // natural component
  return <FooComponent {...props} />;
}

FooComponentContainer.propTypes = { /* ... */ };

```

**Déclenchement d'événements lors de changements de props :**

`useEffect` a la capacité de surveiller votre propriété entre les re-rendus et appelle la fonction que vous lui donnez lorsque la propriété change.

Avant `useEffect`, je me retrouvais à ajouter des méthodes de cycle de vie peu naturelles et des props `onPropertyChanged` parce que je n'avais pas de moyen de faire la différenciation des propriétés à l'extérieur du composant :

```js
import React from 'react';
import PropTypes from 'prop-types';

/**
 * Avant `useEffect`, je me retrouvais à ajouter des props "peu naturelles"
 * à mes composants qui ne déclenchaient des événements que lorsque les props différaient.
 *
 * J'ai remarqué que le `render` du composant n'utilisait même pas `id`
 * la plupart du temps
 */
export default class BeforeUseEffect extends React.Component {
  static propTypes = {
    id: PropTypes.string.isRequired,
    onIdChange: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.onIdChange(this.props.id);
  }

  componentDidUpdate(prevProps) {
    if (prevProps.id !== this.props.id) {
      this.props.onIdChange(this.props.id);
    }
  }

  render() {
    return // ...
  }
}
```

Maintenant avec `useEffect`, il existe un moyen très léger de déclencher des événements lors de changements de props et notre composant réel n'a pas à ajouter de props qui sont inutiles à sa fonction.

```js
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { useRedux } from 'react-redux';

import fetchSomething_reduxAction from 'your-redux-stuff';
import getValues from './helpers/getVaules';
import FooComponent from './FooComponent';

export default function FooComponentContainer({ id }) {
  // hooks
  // NOTE: `useRedux` does not exist yet and probably won't look like this
  const { state, dispatch } = useRedux();
  
  // dispatch action onMount
  useEffect(() => {
    dispatch(fetchSomething_reduxAction);
  }, [id]); // `useEffect` surveillera cette prop `id` et déclenchera l'effet lorsqu'elle diffère
  // https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects

  // mapping
  const props = getValues(state, match);
  
  // natural component
  return <FooComponent {...props} />;
}

FooComponentContainer.propTypes = {
  id: PropTypes.string.isRequired,
};

```

> **_Avertissement:_** _Avant `useEffect`, il existait des moyens de faire de la différenciation de props à l'intérieur d'un conteneur en utilisant d'autres composants d'ordre supérieur (comme [lifecycle de recompose](https://github.com/acdlite/recompose/blob/3db12ce7121a050b533476958ff3d66ded1c4bb8/docs/API.md#lifecycle)) ou en créant un composant de cycle de vie comme [react router le fait en interne](https://github.com/ReactTraining/react-router/blob/89a72d58ac55b2d8640c25e86d1f1496e4ba8d6c/packages/react-router/modules/Lifecycle.js), mais ces méthodes étaient soit déroutantes pour l'équipe, soit peu conventionnelles._

### Quels sont les avantages ici ?

#### Les composants restent amusants

Pour moi, créer des composants est la partie la plus amusante et satisfaisante du développement front-end. Vous pouvez transformer les idées et les rêves de votre équipe en expériences réelles et c'est une bonne sensation à laquelle je pense que nous nous identifions tous et partageons.

Il n'y aura jamais de scénario où l'API et l'expérience de votre composant sont gâchées par le « monde extérieur ». Votre composant peut être ce que vous avez imaginé sans props supplémentaires — c'est mon avantage préféré de cette règle d'or.

#### Plus d'opportunités de tester et de réutiliser

Lorsque vous adoptez une architecture comme celle-ci, vous faites essentiellement émerger une nouvelle couche de données à la surface. Dans cette « couche », vous pouvez changer de vitesse où vous êtes plus préoccupé par la justesse des données entrant dans votre composant par rapport à la façon dont votre composant fonctionne.

Que vous en soyez conscient ou non, cette couche existe déjà dans votre application, mais elle peut être couplée avec la logique de présentation. Ce que j'ai trouvé, c'est que lorsque je fais émerger cette couche, je peux faire beaucoup d'optimisations de code et réutiliser beaucoup de logique que j'aurais autrement réécrite sans connaître les points communs.

Je pense que cela deviendra encore plus évident avec l'ajout des [hooks personnalisés](https://reactjs.org/docs/hooks-custom.html). Les hooks personnalisés nous donnent un moyen beaucoup plus simple d'extraire la logique et de s'abonner aux changements externes — quelque chose qu'une fonction helper ne pouvait pas faire.

#### Maximiser le débit de l'équipe

Lorsque vous travaillez en équipe, vous pouvez séparer le développement des conteneurs et des composants. Si vous convenez des API à l'avance, vous pouvez travailler simultanément sur :

1. L'API Web (c'est-à-dire le back-end)
2. La récupération des données de l'API Web (ou similaire) et la transformation des données vers les API des composants
3. Les composants

### Y a-t-il des exceptions ?

Tout comme la vraie Règle d'or, cette règle d'or est également une règle d'or empirique. Il existe certains scénarios où il est logique d'écrire une API de composant apparemment peu naturelle pour réduire la complexité de certaines transformations.

Un exemple simple serait les noms des props. Cela compliquerait les choses si les ingénieurs renommaient les clés de données sous prétexte que c'est plus « naturel ».

Il est définitivement possible de pousser cette idée trop loin où vous finissez par trop généraliser trop tôt, et cela peut aussi être un piège.

### La conclusion

Plus ou moins, cette « règle d'or » est simplement une réinterprétation de l'idée existante des composants de présentation vs. les composants conteneurs sous un nouveau jour. Si vous évaluez ce dont votre composant a besoin à un niveau fondamental, vous finirez probablement avec des parties plus simples et plus lisibles.

Merci !