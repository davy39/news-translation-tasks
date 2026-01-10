---
title: Meilleures pratiques pour utiliser TypeScript avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T16:40:28.000Z'
originalURL: https://freecodecamp.org/news/effective-use-of-typescript-with-react-3a1389b6072a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qLgLDFCPLeZZlJ4v00jIOw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: TypeScript
  slug: typescript
seo_title: Meilleures pratiques pour utiliser TypeScript avec React
seo_desc: 'By Christopher Diggins

  There are numerous tools and tutorials to help developers start writing simple React
  applications with TypeScript. The best practices for using TypeScript in a larger
  React application are less clear, however.

  This is especiall...'
---

Par Christopher Diggins

Il existe de nombreux outils et tutoriels pour aider les développeurs à commencer à écrire des applications React simples avec TypeScript. Les meilleures pratiques pour utiliser TypeScript dans une application React plus grande sont cependant moins claires.

C'est particulièrement le cas lors de l'intégration avec un écosystème de bibliothèques tierces utilisées pour répondre à des préoccupations telles que : le thème, le style, l'internationalisation, la journalisation, la communication asynchrone, la gestion d'état et la gestion des formulaires.

Chez [Clemex](http://www.clemex.com), nous développons des applications de microscopie computationnelle. Nous avons récemment migré un front-end React pour l'une de nos applications de JavaScript à TypeScript. Dans l'ensemble, nous sommes très satisfaits du résultat final. Le consensus est que notre base de code est maintenant plus facile à comprendre et à maintenir.

Cela dit, notre transition n'a pas été sans quelques défis. Cet article plonge dans certains des défis auxquels nous avons été confrontés et comment nous les avons surmontés.

Les défis sont principalement liés à la compréhension des signatures de type de l'API React, et particulièrement celles des composants d'ordre supérieur. Comment pouvons-nous résoudre les erreurs de type correctement, tout en conservant les avantages de TypeScript ?

Cet article tente de répondre à la manière d'utiliser TypeScript avec React et l'écosystème des bibliothèques de support de la manière la plus efficace. Nous aborderons également quelques domaines courants de confusion.

### Trouver des définitions de type pour une bibliothèque

Un programme TypeScript peut facilement importer n'importe quelle bibliothèque JavaScript. Mais sans déclarations de type pour les valeurs et fonctions importées, nous n'obtenons pas tous les avantages de l'utilisation de TypeScript.

Heureusement, TypeScript facilite la définition d'annotations de type pour les bibliothèques JavaScript, sous la forme de [fichiers de déclaration de type](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html).

Seuls quelques projets aujourd'hui offrent des définitions de type TypeScript directement avec le projet. Cependant, pour de nombreuses bibliothèques, vous pouvez généralement trouver un fichier de définition de type à jour dans l'espace de noms de l'organisation `@types`.

Par exemple, si vous regardez dans le `package.json` du modèle React TypeScript, vous pouvez voir que nous utilisons les fichiers de définition de type suivants :

```
"@types/jest": "^22.0.1",
"@types/node": "^9.3.0",
"@types/react": "^16.0.34",
"@types/react-dom": "^16.0.3",
"@types/redux-logger": "^3.0.5"
```

Le seul inconvénient de l'utilisation de déclarations de type externes est qu'il peut être un peu ennuyeux de traquer les bugs dus à une incompatibilité de version, ou à des bugs subtils dans les fichiers de déclaration de type eux-mêmes. Les fichiers de déclaration de type ne sont pas toujours supportés par les auteurs originaux de la bibliothèque.

### Validation à la compilation des propriétés et des champs d'état

L'un des principaux avantages de l'utilisation de TypeScript dans une application React est que le compilateur (et l'IDE, si configuré correctement) peut valider toutes les propriétés nécessaires fournies à un composant.

Il peut également vérifier qu'elles ont le type correct. Cela remplace le besoin d'une validation à l'exécution comme fourni par la bibliothèque `[prop-types](https://www.npmjs.com/package/prop-types)`.

Voici un exemple simple d'un composant avec deux propriétés requises :

```
import * as React from 'react';
```

```
export interface CounterDisplayProps {
  value: number;
  label: string;
}
```

```
export class CounterDisplay extends React.PureComponent<CounterDisplayProps> {
  render(): React.ReactNode {
    return (
      <div>
        The value of {this.props.label} is {this.props.value}
      </div>
    );
  }
}
```

### Composants en tant que classes ou fonctions

Avec React, vous pouvez définir un nouveau composant de deux manières : en tant que fonction ou en tant que classe. Les types de ces deux types de composants sont :

1. Classes de composants :: `React.ComponentClass<P>`
2. Composants fonctionnels sans état (SFC) :: `React.StatelessComponent<P>`

#### Classes de composants

Un type de classe est un nouveau concept pour les développeurs issus d'un contexte C++/C#/Java. Une classe a un type spécial, qui est séparé du type d'instance d'une classe. Il est défini en termes de fonction constructeur. Comprendre cela est clé pour comprendre les signatures de type et certaines des erreurs de type qui peuvent survenir.

Une `ComponentClass` est le type d'une fonction constructeur qui retourne un objet qui est une instance d'un `Component`. Avec certains détails omis, l'essence de la définition de type `ComponentClass` est :

```
interface ComponentClass<P = {}> {
  new (props: P, context?: any): Component<P, ComponentState>;
}
```

#### Composants sans état (SFC)

Un `StatelessComponent` (également connu sous le nom de `SFC`) est une fonction qui prend un objet de propriétés, une liste facultative de composants enfants et un objet de contexte facultatif. Il retourne soit un `ReactElement`, soit `null`.

Malgré ce que le nom peut suggérer, un `StatelessComponent` n'a pas de relation avec un type `Component`.

Une version simplifiée de la définition du type d'un `StatelessComponent` et de l'alias `SFC` est :

```
interface StatelessComponent<P = {}> {
  (props: P & { children?: ReactNode }, context?: any): ReactElement<any> | null;
}
```

```
type SFC<P = {}> = StatelessComponent<P>;
```

Avant React 16, les SFC étaient assez lents. [Apparently this has improved with React 16](https://medium.com/missive-app/45-faster-react-functional-components-now-3509a668e69f). Cependant, en raison du désir d'un style de codage cohérent dans notre base de code, nous continuons à définir les composants en tant que classes.

#### Composants purs et non purs

Il existe deux types différents de `Component` : purs et non purs.

Le terme "pur" a une signification très spécifique dans le framework React, sans rapport avec le terme en informatique.

Un `PureComponent` est un composant qui fournit une implémentation par défaut de la fonction `shouldComponentUpdate` (qui fait une comparaison superficielle de `this.state` et `this.props`).

Contrairement à une idée reçue, un `StatelessComponent` n'est pas pur, et un `PureComponent` peut avoir un état.

#### Les composants avec état peuvent (et doivent) dériver de React.PureComponent

Comme indiqué ci-dessus, un composant React avec état peut toujours être considéré comme un `Pure component` selon le jargon de React. En fait, c'est une bonne idée de dériver des composants, qui ont un état interne, de `React.PureComponent`.

Ce qui suit est basé sur [le guide TypeScript populaire de Piotr Witek](https://github.com/piotrwitek/react-redux-typescript-guide), mais avec les petites modifications suivantes :

1. La fonction `setState` utilise un rappel pour mettre à jour l'état en fonction de l'état précédent comme le précise la documentation React.
2. Nous dérivons de `React.PureComponent` car il ne remplace pas les fonctions de cycle de vie.
3. Le type `State` est défini comme une classe afin qu'il puisse avoir un initialiseur.
4. Nous n'assignons pas les propriétés à des variables locales dans la fonction de rendu car cela viole le principe DRY et ajoute des lignes de code inutiles.

```
import * as React from 'react';
export interface StatefulCounterProps {
  label: string;
}
```

```
// En faisant de state une classe, nous pouvons définir des valeurs par défaut.
class StatefulCounterState {
  readonly count: number = 0;
};
```

```
// Un compteur avec état peut être un React.PureComponent
export class StatefulCounter extends React.PureComponent<StatefulCounterProps, StatefulCounterState> {
  // Définir l'état en lecture seule
  readonly state = new StatefulCounterState();
```

```
  // Les rappels doivent être définis comme des champs en lecture seule initialisés avec des fonctions fléchées, afin de ne pas avoir à les lier
  // Notez que la définition de l'état en fonction de l'état précédent est effectuée à l'aide d'un rappel.
  readonly handleIncrement = () => {
    this.setState((prevState) => {
      return { count: prevState.count + 1 } as StatefulCounterState;
    });
  }
```

```
  // Nous incluons explicitement le type de retour
  render(): React.ReactNode {
    return (
      <div>
        <span>{this.props.label}: {this.state.count} </span>
        <button type="button" onClick={this.handleIncrement}>
          {`Increment`}
        </button>
      </div>
    );
  }
}
```

#### Les composants fonctionnels sans état de React ne sont pas des composants purs

Contrairement à une idée reçue, les composants fonctionnels sans état (SFC) ne sont pas des composants purs, ce qui signifie qu'ils sont rendus à chaque fois, indépendamment du fait que les propriétés aient changé ou non.

### Typage des composants d'ordre supérieur

De nombreuses bibliothèques utilisées avec les applications React fournissent des fonctions qui prennent une définition de composant et retournent une nouvelle définition de composant. Ceux-ci sont appelés **composants d'ordre supérieur** (ou **HOC** en abrégé).

Un composant d'ordre supérieur peut retourner un `StatelessComponent` ou un `ComponentClass` selon la manière dont il est défini.

#### La confusion de l'export par défaut

Un modèle courant dans les applications React JavaScript consiste à définir un composant, avec un nom particulier (disons `MyComponent`) et à le garder local à un module. Ensuite, exporter par défaut le résultat de son enveloppe avec un ou plusieurs HOC.

Le composant anonyme est importé dans toute l'application en tant que `MyComponent`. Cela est trompeur car le programmeur réutilise le même nom pour deux choses très différentes !

Pour fournir des types appropriés, nous devons réaliser que le composant retourné par un composant d'ordre supérieur n'est généralement pas du même type que le composant défini dans le fichier.

Dans notre équipe, nous avons trouvé utile de fournir des noms à la fois pour le composant défini qui est conservé localement dans le fichier (par exemple, `MyComponentBase`) et de nommer explicitement une constante avec le composant exporté (par exemple, `export const MyComponent = injectIntl(MyComponentBase);`).

En plus d'être plus explicite, cela évite le problème d'aliasing de la définition, ce qui facilite la compréhension et le refactoring du code.

#### HOCs qui injectent des propriétés

La majorité des HOCs injectent des propriétés dans votre composant qui n'ont pas besoin d'être fournies par le consommateur de votre composant. Voici quelques exemples que nous utilisons dans notre application :

* De material-ui : `withStyles`
* De redux-form : `reduxForm`
* De react-intl : `injectIntl`
* De react-redux : `connect`

#### Propriétés internes, externes et injectées

Pour mieux comprendre la relation entre le composant retourné par la fonction HOC et le composant tel qu'il est défini, essayez ce modèle mental utile :

Pensez aux propriétés attendues pour être fournies par un client du composant comme des _propriétés externes_, et à l'ensemble des propriétés visibles par la définition du composant (par exemple, les propriétés utilisées dans la fonction de rendu) comme les _propriétés internes_. La différence entre ces deux ensembles de propriétés sont les _propriétés injectées_.

#### L'opérateur d'intersection de types

Dans TypeScript, nous pouvons combiner des types de la manière dont nous le souhaitons pour les propriétés en utilisant un opérateur de niveau de type appelé l'[opérateur d'intersection](http://www.typescriptlang.org/docs/handbook/advanced-types.html) (`&`). L'opérateur d'intersection combinera les champs d'un type avec les champs d'un autre type.

```
interface LabelProp {
  label: string;
}
```

```
interface ValueProp {
  value: number;
}
```

```
// A à la fois un champ label et un champ value
type LabeledValueProp = LabelProp & ValueProp;
```

Pour ceux d'entre vous qui sont familiers avec la théorie des ensembles, vous vous demandez peut-être pourquoi cela n'est pas considéré comme un opérateur d'union. C'est parce qu'il s'agit d'une intersection des ensembles de toutes les valeurs possibles qui satisfont les deux contraintes de type.

### Définition des propriétés pour un composant enveloppé

Lors de la définition d'un composant qui sera enveloppé avec un composant d'ordre supérieur, nous devons fournir les propriétés internes au type de base (par exemple, `React.PureComponent<P>`).

Cependant, nous ne voulons pas définir tout cela dans une seule interface exportée, car ces propriétés ne concernent pas le client du composant : ils ne veulent que les propriétés externes.

Pour minimiser le code répétitif, nous avons opté pour l'utilisation de l'opérateur d'intersection, au point unique où nous devons nous référer au type de propriétés internes, qui est lorsque nous le passons en tant que paramètre générique à la classe de base.

```
interface MyProperties {
  value: number;
}
```

```
class MyComponentBase extends React.PureComponent<MyProperties & InjectedIntlProps> {
  // Maintenant, intl est une propriété
  // ...
}
```

```
export const MyComponent = injectIntl(MyComponentBase); // A le type React.Component<MyProperties>;
```

### La fonction connect de React-Redux

La fonction `connect` de la bibliothèque React-Redux est utilisée pour récupérer les propriétés requises par un composant à partir du store Redux, et pour mapper certaines des fonctions de rappel au dispatcher (qui déclenche des actions qui déclenchent des mises à jour du store).

Ainsi, en ignorant l'argument facultatif de la fonction de fusion, nous avons potentiellement deux arguments pour connecter :

1. `mapStateToProps`
2. `mapDispatchToProps`

Ces deux fonctions fournissent leur propre sous-ensemble des propriétés internes à la définition du composant.

Cependant, la signature de type de `connect` est un cas spécial en raison de la manière dont le type a été écrit. Il peut déduire un type pour les propriétés qui sont injectées et également déduire un type pour les propriétés qui restent.

Cela nous laisse avec deux options :

1. Nous pouvons diviser l'interface en les propriétés internes de `mapStateToProps` et une autre pour `mapDispatchToProps`.
2. Nous pouvons laisser le système de types déduire le type pour nous.

Dans notre cas, nous avons dû convertir environ 50 composants _connectés_ de JavaScript à TypeScript.

Ils avaient déjà des interfaces formelles générées à partir de la définition PropTypes originale (grâce à un [outil open-source que nous avons utilisé de Lyft](https://github.com/lyft/react-javascript-to-typescript-transform)).

La valeur de séparer chacune de ces interfaces en propriétés externes, propriétés d'état mappées et propriétés de dispatch mappées ne semblait pas l'emporter sur le coût.

En fin de compte, l'utilisation correcte de `connect` a permis aux clients de déduire les types correctement. Nous sommes satisfaits pour l'instant, mais nous pourrions revisiter ce choix.

#### Aider la fonction connect de React-Redux à déduire les types

Le moteur d'inférence de type de TypeScript semble parfois nécessiter une touche délicate. La fonction `connect` semble être l'un de ces cas. Maintenant, espérons que ce n'est pas un cas de programmation cargo culte, mais voici les étapes que nous suivons pour nous assurer que le compilateur peut déterminer le type.

* Nous ne fournissons pas de type aux fonctions `mapStateToProps` ou `mapDispatchToProps`, nous laissons simplement le compilateur les déduire.
* Nous définissons `mapStateToProps` et `mapDispatchToProps` comme des fonctions fléchées assignées à des variables `const`.
* Nous utilisons `connect` comme le composant d'ordre supérieur le plus externe.
* Nous ne combinons pas plusieurs composants d'ordre supérieur en utilisant une fonction `compose`.

Les propriétés qui sont connectées au store dans `mapStateToProps` et `mapDispatchToProps` ne doivent pas être déclarées comme facultatives, sinon vous pouvez obtenir des erreurs de type dans le type déduit.

### Mots finaux

En fin de compte, nous avons constaté que l'utilisation de TypeScript rendait nos applications plus faciles à comprendre. Cela a aidé à approfondir notre compréhension de React et de l'architecture de notre propre application.

L'utilisation correcte de TypeScript dans le contexte de bibliothèques supplémentaires conçues pour étendre React a nécessité des efforts supplémentaires, mais cela en vaut définitivement la peine.

Si vous commencez tout juste avec TypeScript dans React, les guides suivants seront utiles :

* [Microsoft TypeScript React Starter](https://github.com/Microsoft/TypeScript-React-Starter)
* [Guide de conversion Microsoft TypeScript React](https://github.com/Microsoft/TypeScript-React-Conversion-Guide)
* [Convertisseur Lyft React JavaScript vers TypeScript](https://github.com/lyft/react-javascript-to-typescript-transform)

Après cela, je recommande de lire les articles suivants :

* [React Higher-Order Component Patterns in TypeScript](https://medium.com/@jrwebdev/react-higher-order-component-patterns-in-typescript-42278f7590fb) par James Ravenscroft
* [Guide React-Redux TypeScript de Piotr Witek](https://github.com/piotrwitek/react-redux-typescript-guide)

#### Remerciements

Un grand merci aux membres de l'équipe Clemex pour leur collaboration à cet article, travaillant ensemble pour comprendre comment utiliser TypeScript à son meilleur potentiel dans les applications React, et développant le projet open-source [TypeScript React Template](https://github.com/Clemex/typescript-react-template) sur GitHub.