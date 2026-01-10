---
title: Comment ajouter progressivement Flow à une application React existante
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T17:18:04.000Z'
originalURL: https://freecodecamp.org/news/incrementally-add-flow-type-checking-react-261fee015f80
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rvRslS4L3DF-46j0LVBQ4w.png
tags:
- name: flow
  slug: flow
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment ajouter progressivement Flow à une application React existante
seo_desc: 'By Dominic Fraser

  Flow is a static type checker for Javascript. This post is intended for those who
  have heard of Flow, but have not yet tried to use it within a React app. If this
  is the first time you have heard of Flow then I can recommend these f...'
---

Par Dominic Fraser

[Flow](https://flow.org/) est un vérificateur de types statique pour JavaScript. Cet article s'adresse à ceux qui ont _entendu_ parler de Flow, mais qui ne l'ont pas encore essayé dans une application React. Si c'est la première fois que vous entendez parler de Flow, je peux recommander [ces quatre articles](https://medium.freecodecamp.org/why-use-static-types-in-javascript-part-1-8382da1e0adb) de Preethi Kasireddy comme une excellente introduction.

Une chose formidable à propos de Flow est qu'il est possible de l'utiliser de manière incrémentielle. Vous n'avez pas besoin de refactoriser complètement un projet existant pour commencer à l'utiliser. Il peut être ajouté uniquement aux nouveaux fichiers, ou progressivement essayé dans les fichiers existants pour voir s'il apporte des bénéfices à votre projet spécifique avant de vous engager pleinement.

Comme la configuration d'un nouvel outil peut souvent être la partie la plus difficile, dans cet article nous allons prendre un projet existant et parcourir la configuration pour ajouter Flow. Une introduction générale à la syntaxe est couverte dans le deuxième article de Preethi, et la [documentation de Flow](https://flow.org/en/docs/) est également très lisible.

Nous allons utiliser ce [dépôt d'exemple](https://github.com/dominicfraser/FlowExamples), avec deux répertoires pour avant et après Flow. Il utilise le script personnalisé [Skyscanner](https://github.com/Skyscanner/backpack-react-scripts) `backpack-react-scripts` pour Create React App, associé à leurs composants personnalisés [Backpack](https://backpack.github.io/). Cela vise à créer des exemples plus complexes que de simples extraits de code, tout en restant lisibles même si vous ne les connaissez pas.

La nature exacte de l'application est moins importante que de voir la différence entre son implémentation [sans](https://github.com/dominicfraser/FlowExamples/tree/master/without_flow) et [avec](https://github.com/dominicfraser/FlowExamples/tree/master/with_flow) Flow. Très peu de fichiers changent ici, mais ils sont souvent les plus frustrants à corriger !

Parcourons chaque étape, puis examinons la conversion des composants d'exemple.

### Installer les dépendances principales

En plus de Flow lui-même, installez `babel-cli` et `babel-preset-flow` afin que Babel puisse supprimer les annotations de type lors de la compilation.

```
npm install flow-bin babel-cli babel-preset-flow --save-dev
```

#### Configurer Babel

Pour que ces modifications prennent effet, créez un fichier `.babelrc`, ou ajoutez à votre `.babelrc` existant la [configuration suivante](https://github.com/dominicfraser/FlowExamples/blob/master/with_flow/.babelrc) :

```js
{
  "presets": ["flow"]
}
```

#### Configurer les scripts

Si vous utilisez des hooks, comme un script de pré-test, vous pouvez vouloir les mettre à jour ainsi qu'ajouter le script de base de Flow à votre `package.json` :

```js
"scripts": {
  "flow": "flow",
  "pretest": "npm run flow && npm run lint"
}
```

### Générer un flowconfig

Si vous exécutez Flow pour la première fois, vous pouvez générer un modèle `.flowconfig` en exécutant `npm run flow init`. Dans notre exemple, nous pouvons voir que nous [l'étendons](https://github.com/dominicfraser/FlowExamples/blob/master/with_flow/.flowconfig) pour ajouter ce qui suit :

#### Ignorer les motifs

Pour éviter que Flow n'analyse vos modules de nœuds et la sortie de construction, ceux-ci peuvent facilement être ignorés.

```
[ignore].*/node_modules/*.*/build/*
```

#### Ajouter la prise en charge des modules CSS

Si vous utilisez des modules CSS, leur type doit être spécifié afin que Flow puisse les comprendre, sinon vous recevrez cette erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/4BB7saOoBeFHLr8pkslCECfAmSAdWmSavyN5)
_Erreur : [flow] Impossible de résoudre le module `CSSModule`._

Cela se fait en deux étapes. Tout d'abord, ce qui suit est ajouté à votre `.flowconfig` :

```
[libs]
./src/types/global.js  // ce peut être n'importe quel chemin et nom de fichier que vous souhaitez
[options]
module.name_mapper='^\\(\\.\\*\\)\\.scss$' -> 'CSSModule'
module.system=haste
```

Et deuxièmement, un type de module CSS est créé dans [le fichier référencé](https://github.com/dominicfraser/FlowExamples/blob/master/with_flow/src/types/global.js) dans `[libs]`.

```js
// @flow
declare module CSSModule {
  declare var exports: { [key: string]: string };
  declare export default typeof exports;
}
```

### Synchroniser avec d'autres linters utilisés

Dans le projet d'exemple, ESLint est déjà utilisé pour fournir un linting standard. Il y a quelques étapes de configuration initiales nécessaires pour que ESLint fonctionne bien avec Flow, et quelques étapes supplémentaires en raison des types spécifiques utilisés dans ce projet.

Pour la configuration générale, ce qui suit est [ajouté](https://github.com/dominicfraser/FlowExamples/blob/master/with_flow/.eslintrc) à notre `.eslintrc` :

```js
"extends": [
  "plugin:flowtype/recommended"
],
"plugins": [
  "flowtype"
]
```

Les extensions spécifiques à cet exemple, et les erreurs qu'elles évitent, seront couvertes à la fin de cet article.

### Définitions de types Flow

La dernière partie de la configuration consiste à se préparer à utiliser les `libdefs` créées à l'aide du package NPM `flow-typed`. Cela est utilisé pour créer des définitions pour les modules de nœuds installés, et par défaut crée ces fichiers dans un répertoire `flow-typed/`.

Nous **voulons** commiter ce fichier, mais nous ne voulons pas que ESLint le linte. Cela crée un problème, car précédemment notre script de linting dans notre `package.json` est configuré pour utiliser notre `.gitignore` pour savoir quels fichiers ESLint doit également ignorer :

```
"lint:js": "eslint . --ignore-path .gitignore --ext .js,.jsx",
```

Nous voulons maintenant changer cela, car nous voulons que ESLint ignore également le répertoire `flow-typed/` qui sera créé. Nous pouvons modifier notre script en :

```
"lint:js": "eslint . --ext .js,.jsx",
```

Cela signifie qu'il reviendra maintenant à utiliser un fichier `.eslintignore`, nous devons donc créer ce fichier, dupliquer ce qui se trouve dans notre `.gitignore`, et [ajouter le répertoire supplémentaire à ignorer](https://github.com/dominicfraser/FlowExamples/blob/master/with_flow/.eslintignore).

Enfin, nous devons installer `flow-typed`. Nous le faisons globalement.

```
npm install flow-typed -g
```

Les `libdefs` peuvent être des définitions complètes ou des stubs qui acceptent n'importe quel type. Une liste de [définitions complètes](https://github.com/flow-typed/flow-typed/tree/master/definitions/npm) est maintenue. Pour voir si une définition est disponible pour un package que vous utilisez, utilisez :

```
flow-typed install my-dependency@<version.being.used>
```

et cela ajoutera soit la définition à votre répertoire `flow-typed`, soit vous invitera à créer un stub en utilisant :

```
flow-typed create-stub my-dependency@<version.being.used>
```

Si vous souhaitez créer une définition complète, vous pouvez le faire, et également la contribuer au dépôt afin qu'elle soit disponible pour d'autres développeurs.

Un processus simple à suivre consiste à ne créer des `libdefs` que lorsqu'elles sont spécifiquement requises. Pour chaque composant que vous convertissez pour utiliser Flow, ajoutez ses imports en utilisant `flow-typed` à ce moment-là, il n'est pas nécessaire d'ajouter des types pour toutes les dépendances si elles ne sont pas utilisées dans des fichiers où Flow est également utilisé.

### Convertir les composants existants

C'est toute la configuration générale terminée, maintenant nous pouvons examiner la conversion de nos composants d'exemple !

Nous en avons deux, un composant avec état et un composant fonctionnel. Globalement, ceux-ci créent une bannière qui contient du texte et un bouton. Le texte sur la bannière peut être cliqué pour ouvrir un popover, contenant une liste à puces.

![Image](https://cdn-media-1.freecodecamp.org/images/HxnnMVP2vZDNJXdZPN8ndoa1iUBv-0AhriGB)
_Bannière avec un bouton de fermeture et un popover d'information_

#### Ajouter des définitions flow-typed

Pour tout composant, la première étape consiste à créer des définitions `flow-typed` pour toutes les imports dans le composant sur lequel nous travaillons.

Par exemple, si nous n'avions que les imports suivants :

```
import React from 'react';
import BpkButton from 'bpk-component-button';
```

alors nous essayerions :

`flow-typed install bpk-component-button@<its.installed.version>`

si ce n'était pas disponible, et ce n'est actuellement pas le cas, alors nous créerions un stub de sa définition :

`flow-typed create-stub bpk-component-button@latest`

Dans le dépôt d'exemple, nous pouvons voir la [liste de toutes les définitions créées](https://github.com/dominicfraser/FlowExamples/tree/master/with_flow/flow-typed/npm) pour les composants que nous avons convertis pour utiliser Flow. Celles-ci ont été ajoutées une à la fois au fur et à mesure que chaque composant intégrait Flow.

#### Composants Fonctionnels

Dans notre exemple [sans Flow](https://github.com/dominicfraser/FlowExamples/blob/master/without_flow/src/components/ListPopover/ListPopover.jsx), nous utilisons `PropTypes` pour une vérification de type limitée et leur capacité à définir `defaultProps` pour une utilisation en développement.

Cela peut sembler un peu complexe au premier abord, mais il y a relativement peu de choses que nous devons changer pour ajouter Flow.

![Image](https://cdn-media-1.freecodecamp.org/images/zD8GKbnXI-x7GFWHalX0uDJ3loHnt74ZVDKv)
_Composant avant l'ajout de Flow_

Pour transformer cela pour utiliser Flow, nous pouvons d'abord supprimer l'import et les définitions de `PropTypes`. L'annotation `// @flow` peut ensuite être ajoutée à la première ligne.

Pour ce composant, nous allons uniquement vérifier les types des props passées. Pour ce faire, nous allons d'abord créer un type Props, beaucoup plus propre que de définir chaque prop individuellement en ligne.

```js
type Props = {
  strings: { [string_key: string]: string },
  onClose: Function,
  isOpen: boolean,
  target: Function,
};
```

Ici, les trois derniers types sont explicites. Comme `strings` est un objet de chaînes, un [objet en tant que map](https://flow.org/en/docs/types/objects/#toc-objects-as-maps) a été utilisé, vérifiant chaque clé et valeur dans l'objet reçu pour vérifier que leurs types correspondent, sans avoir à spécifier leurs clés de chaîne exactes.

Les définitions de prop-types peuvent ensuite être supprimées ainsi que leur import. Comme defaultProps ne sont pas liés à cette importation, ils peuvent et doivent rester. *Voir les commentaires de clôture ESLint pour toute erreur signalée à ce stade.*

Le composant devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/-we8sa2SWafDHveReVxt53eDA-RfWvwZ1W8r)
_Composant après l'ajout de Flow_

#### Composants avec État

Les composants avec état suivent des déclarations légèrement différentes. Comme ce composant est plus complexe, nous allons également examiner la déclaration de types pour certains aspects supplémentaires.

Comme précédemment, commencez par examiner [le composant avant l'ajout de Flow](https://github.com/dominicfraser/FlowExamples/blob/master/without_flow/src/components/Banner/Banner.jsx).

**Props et État**

Comme dans le composant fonctionnel, nous supprimons d'abord la définition et l'import de `propTypes`, et ajoutons l'annotation `// @flow`.

Tout d'abord, nous allons examiner l'ajout de types pour les Props et l'État. Nous allons à nouveau créer des types pour ceux-ci :

```js
type Props = {
  strings: { [string_key: string]: string },
  hideBannerClick: Function,
}; 
type State = {
  popoverIsOpen: boolean,
};
```

et spécifions que le composant les utilisera :

```
class Banner extends Component<Props, State> {
  constructor(props: Props) {
    super(props);    
    this.state = {
      popoverIsOpen: false,
    };
  ...
  };
...
};
```

Ensuite, nous rencontrons notre première différence entre les composants Fonctionnels et avec État, `defaultProps`. Dans un composant Fonctionnel, ceux-ci étaient déclarés comme nous en avons l'habitude, dans les composants avec État, la syntaxe externe `Banner.defaultProps` est supprimée, et à la place les valeurs par défaut sont déclarées dans la classe :

```js
class Banner extends Component<Props, State> {
  static defaultProps = {
    strings: defaultStrings,
  };
constructor(props: Props) {
...
// le code suivant est supprimé
// Banner.defaultProps = {
//  strings: defaultStrings,
// };
```

**Déclarations du Constructeur**

`stringWithPlaceholder` est déclaré dans le constructeur. Ici, nous ne cherchons pas à savoir _pourquoi_ il est déclaré là (nous supposerons qu'il y a une bonne raison), mais plutôt à voir si Flow peut être ajouté sans aucun changement au code existant.

Si exécuté dans son état actuel, nous rencontrerions l'erreur `Cannot get this.stringWithPlaceholder because property stringWithPlaceholder is missing in Banner [1]`.

Pour corriger cela, nous devons ajouter une seule ligne à l'intérieur du bloc de classe Banner, juste en dessous et à l'extérieur du constructeur :

```js
class Banner extends Component<Props, State> {
  constructor(props: Props) {
    super(props);    
    this.state = {
      popoverIsOpen: false,
    };
    this.stringWithPlaceholder = ...
  };
  stringWithPlaceholder: string;
...
};
```

Cette variable est créée dans le constructeur mais n'est pas passée en tant que props. Comme nous utilisons Flow pour vérifier les types des props passées dans le constructeur, il nécessite que **tout ce qui est à l'intérieur du constructeur** soit vérifié. Il est [connu](https://github.com/facebook/flow/issues/4376) que Flow exige cela, et cela peut être fait en spécifiant leur type dans le bloc de classe.

À ce stade, Props et State sont complets. Examinons quelques exemples supplémentaires de vérification de type dans ce composant. *Voir les commentaires de clôture ESLint pour toute erreur signalée à ce stade.*

**Types de Retour, Événement et Nœud**

`togglePopover` ne prend aucun argument, donc un exemple simple de spécification de l'absence de valeur de retour peut être vu :

```js
togglePopover = (): void => {
  ...
};
```

`keyboardOnlyTogglePopover` ne retourne rien, mais a un seul paramètre. Il s'agit d'un événement, spécifiquement un événement de pression de touche. `SyntheticKeyboardEvent` est utilisé [comme](https://flow.org/en/docs/react/events/)

> _React utilise son propre système d'événements, il est donc important d'utiliser les types SyntheticEvent au lieu des types DOM tels que Event, KeyboardEvent et MouseEvent._

```js
keyboardOnlyTogglePopover = (e: SyntheticKeyboardEvent<>): void => {
  ...
};
```

`Popover` est défini dans `render()` et retourne une instance du composant fonctionnel `ListPopover` que nous avons examiné précédemment. Nous pouvons spécifier son type de retour comme un nœud React `Node`. Cependant, pour pouvoir le faire, nous devons d'abord l'importer, car il n'est [pas accessible par défaut](https://flow.org/en/docs/react/types/). Il existe plus d'une façon de l'importer, l'une d'entre elles est montrée ci-dessous :

```
import React, { Component } from 'react';
import type { Node } from 'react';
...
const Popover: Node = (
  <ListPopover
    onClose={this.togglePopover}
    isOpen={this.state.popoverIsOpen}
    strings={this.props.strings}
    target={() => document.getElementById('ListPopoverLink')}
  />
);
```

### **Vérification des types des composants React importés**

Lorsque les types de props ont été déclarés dans un composant, ils peuvent être utilisés lors de l'utilisation de ce composant dans un autre. Cependant, si vous utilisez un `index.js` pour exporter le premier composant, alors le flux, `// @flow` devra être ajouté à l'index.

[Par exemple](https://github.com/dominicfraser/FlowExamples/blob/master/with_flow/src/components/ListPopover/index.js) :

```
// @flow
import ListPopover from './ListPopover';
export default ListPopover;
```

### Marquer les props comme optionnelles

Une prop peut être marquée comme optionnelle en utilisant la syntaxe `prop?: type`, par exemple :

```
type Props = {  
  strings: { [string_key: string]: string },  
  hideBannerClick?: Function,
};
```

Cela est pris en charge, mais n'est plus recommandé par Flow. Au lieu de cela, toutes les props doivent être laissées comme requises, sans `?`, même si elles sont optionnelles, car Flow [détecte automatiquement](https://github.com/facebook/flow/issues/1660#issuecomment-434549520) les defaultProps et marque les props avec une valeur par défaut comme optionnelles en interne.

Dans la section ci-dessous, nous pouvons voir comment le marquage manuel des props comme optionnelles peut causer des conflits avec d'autres outils dans certains cas.

### Extensions ESLint, props par défaut et solutions d'erreurs de validation des props

Deux ajouts sont faits à notre `.eslintrc`. Pour ce projet spécifique, vous pouvez simplement accepter leur utilisation, ou lire les détails ci-dessous si vous voyez l'une des trois erreurs :

* `x missing in props validation`
* `error defaultProp "x" defined for isRequired propType`
* `Cannot get strings.xxx because property xxx is missing in undefined`

Les règles ajoutées, avec leur raisonnement, sont :

```js
"react/default-props-match-prop-types": [
  "error", { "allowRequiredDefaults": true }
]
```

Lorsque des objets sont utilisés comme des maps (dans ce cas pour la prop 'strings'), une erreur `missing in props validation` se produit. Il s'agit d'un [bug](https://github.com/yannickcr/eslint-plugin-react/issues/1280) et est donc explicitement [ignoré](https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/prop-types.md) ici.

```
"react/default-props-match-prop-types": [  "error", { "allowRequiredDefaults": true }]
```

Lorsque des objets sont utilisés comme des maps, des complexités entre ESLint, Flow et prop-types entrent en jeu.

`strings` est une prop requise, passée sous forme d'objet de chaînes. Le type Flow vérifie que pour chaque entrée dans l'objet, la clé de chaîne est une chaîne et la valeur est une chaîne. Cela est beaucoup plus maintenable que de devoir lister le type de prop de chaque clé spécifique.

Si la prop est marquée comme requise dans Flow, alors ESLint générera une erreur indiquant : `error defaultProp "strings" defined for isRequired propType`.

Si la prop est manuellement marquée comme optionnelle, alors Flow générera une erreur avec `Cannot get strings.xxx because property xxx is missing in undefined [1]`.

Cela est [connu](https://github.com/facebook/flow/issues/6350) et est dû à [l'invalidation de l'affinage](https://flow.org/en/docs/lang/refinements/#toc-refinement-invalidations) car JSX peut transformer les appels de méthode de sorte que Flow ne peut pas être sûr que xxx n'a pas été redéfini.

Cela nous laisse avec la correction de l'erreur ESLint. La règle ci-dessus permet de définir defaultProps tandis que le type Flow n'est **pas** marqué comme optionnel. Flow comprendra cela et le convertira en optionnel. ESLint est marqué avec `"allowRequiredDefaults": true`, ce qui signifie que bien qu'ESLint voie la prop comme requise, il ne générera pas d'erreur.

### Réflexions finales

Une fois l'obstacle initial de l'installation surmonté, Flow est assez simple à utiliser. La possibilité de l'ajouter de manière incrémentielle aide définitivement, plutôt que de devoir refactoriser un projet entier en une seule fois.

Espérons que les instructions de configuration et les exemples ici s'avèrent utiles si vous cherchez à essayer Flow vous-même.

Merci d'avoir lu 😊

Vous pourriez également aimer :

* [Testing React with Jest and Enzyme I](https://medium.com/@dfrase/testing-react-with-jest-and-enzyme-20505fec4675)
* [A beginner’s guide to Amazon’s Elastic Container Service](https://medium.com/p/807d8c4960fd?source=user_profile---------11------------------)
* [Using Pa11y CI and Drone as accessibility testing gatekeepers](https://medium.com/p/a8b5a3415227?source=user_profile---------7------------------)