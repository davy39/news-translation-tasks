---
title: Pourquoi React16 est une bénédiction pour les développeurs React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T15:11:39.000Z'
originalURL: https://freecodecamp.org/news/why-react16-is-a-blessing-to-react-developers-31433bfc210a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YG3-T77xGBfKDn5SfE6P8w.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi React16 est une bénédiction pour les développeurs React
seo_desc: 'By Harsh Makadia

  Just like how people are excited about updating their mobile apps and OS, developers
  should also be excited to update their frameworks. The new version of the different
  frameworks come with new features and tricks out of the box.

  Bel...'
---

Par Harsh Makadia

Tout comme les gens sont excités à l'idée de mettre à jour leurs applications mobiles et leur système d'exploitation, les développeurs devraient également être enthousiastes à l'idée de mettre à jour leurs frameworks. Les nouvelles versions des différents frameworks arrivent avec de nouvelles fonctionnalités et astuces prêtes à l'emploi.

Voici quelques-unes des bonnes fonctionnalités à considérer lors de la migration de votre application existante vers React 16 depuis React 15.

> _Temps de dire adieu à React15 ?_

### Gestion des erreurs

![Image](https://cdn-media-1.freecodecamp.org/images/1*UH_OYTog9NJi3o3kooA_vg.gif)
_Gestion des erreurs, c'est comme ça :)_

React 16 introduit le nouveau concept de _limite d'erreur_.

Les limites d'erreur sont des composants React qui **attrapent les erreurs JavaScript n'importe où dans leur arbre de composants enfants. Ils enregistrent ces erreurs et affichent une UI de secours** au lieu de l'arbre de composants planté. Les limites d'erreur attrapent les erreurs pendant le rendu, dans les méthodes de cycle de vie et dans les constructeurs de tout l'arbre en dessous d'eux.

Un composant de classe devient une limite d'erreur s'il définit une nouvelle méthode de cycle de vie appelée `componentDidCatch(error, info)` :

Ensuite, vous pouvez l'utiliser comme un composant régulier.

```
<ErrorBoundary>     <MyWidget /></ErrorBoundary>
```

La méthode `componentDidCatch()` fonctionne comme un bloc `catch {}` JavaScript, mais pour les composants. Seuls les composants de classe peuvent être des limites d'erreur. En pratique, la plupart du temps, vous voudrez déclarer un composant de limite d'erreur une fois. Ensuite, vous l'utiliserez dans toute votre application.

Notez que **les limites d'erreur n'attrapent que les erreurs dans les composants en dessous d'eux dans l'arbre**. Une limite d'erreur ne peut pas attraper une erreur en elle-même. Si une limite d'erreur échoue en essayant de rendre le message d'erreur, l'erreur se propagera à la limite d'erreur la plus proche au-dessus d'elle. Cela aussi est similaire à la façon dont le bloc `catch {}` fonctionne en JavaScript.

Consultez la démonstration en direct :

Pour plus d'informations sur la gestion des erreurs, rendez-vous [ici](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html).

### Nouveaux types de retour de rendu : fragments et chaînes

Débarrassez-vous de l'emballage du composant dans une div lors du rendu.

Vous pouvez maintenant retourner un tableau d'éléments depuis la méthode `render` d'un composant. Comme avec les autres tableaux, vous devrez ajouter une clé à chaque élément pour éviter l'avertissement de clé :

```
render() {  // Pas besoin d'emballer les éléments de liste dans un élément supplémentaire !  return [    // N'oubliez pas les clés :)    <li key="A">Premier élément</li>,    <li key="B">Deuxième élément</li>,    <li key="C">Troisième élément</li>,  ];}
```

[À partir de React 16.2.0](https://reactjs.org/blog/2017/11/28/react-v16.2.0-fragment-support.html), il prend en charge une syntaxe de fragment spéciale pour JSX qui ne nécessite pas de clés.

Prise en charge du retour de chaînes :

```
render() {  return 'Regarde maman, pas de spans !';}
```

### Portails

Les portails fournissent un moyen de première classe pour rendre les enfants dans un nœud DOM qui existe en dehors de la hiérarchie DOM du composant parent.

```
ReactDOM.createPortal(child, container)
```

Le premier argument (`child`) est n'importe quel [enfant React renderable](https://reactjs.org/docs/react-component.html#render), tel qu'un élément, une chaîne ou un fragment. Le deuxième argument (`container`) est un élément DOM.

#### **Comment l'utiliser**

Lorsque vous retournez un élément depuis la méthode de rendu d'un composant, il est monté dans le DOM en tant qu'enfant du nœud parent le plus proche :

```
render() {  // React monte une nouvelle div et rend les enfants dedans  return (    <div>      {this.props.children}    </div>  );}
```

Parfois, il est utile d'insérer un enfant à un autre endroit dans le DOM :

```
render() {  // React ne crée *pas* de nouvelle div. Il rend les enfants dans `domNode`.  // `domNode` est n'importe quel nœud DOM valide, indépendamment de son emplacement dans le DOM.  return ReactDOM.createPortal(    this.props.children,    domNode  );}
```

Un cas d'utilisation typique pour les portails est lorsqu'un composant parent a un style `overflow: hidden` ou `z-index`, mais que vous avez besoin que l'enfant se "détache" visuellement de son conteneur. Par exemple, les dialogues, les cartes de survol et les infobulles.

### Attribut DOM personnalisé

![Image](https://cdn-media-1.freecodecamp.org/images/1*6h94cJ7rOVdaykMmyhOvhg.png)

React15 ignorait tous les attributs DOM inconnus. Il les ignorait simplement car React ne les reconnaissait pas.

```
// Votre code :<div mycustomattribute="something" />
```

Avec React 15, cela rendait une div vide dans le DOM :

```
// Sortie React 15 :<div />
```

Dans React16, la sortie sera la suivante (_les attributs personnalisés seront affichés et ne seront pas ignorés du tout_) :

```
// Sortie React 16 :<div mycustomattribute="something" />
```

### Éviter le re-rendu en définissant NULL dans l'état

![Image](https://cdn-media-1.freecodecamp.org/images/1*mDNqHOCtoVeKTPR4gtfP2Q.png)

Avec React16, vous pouvez empêcher les mises à jour d'état et les re-rendus directement depuis `setState()`. Vous devez simplement faire en sorte que votre fonction retourne `null`.

```
const MAX_PIZZAS = 20;function addAnotherPizza(state, props) {  // Arrêter les mises à jour et les re-rendus si j'ai eu assez de pizzas.  if (state.pizza === MAX_PIZZAS) {    return null;  }  // Sinon, continuez à faire venir les pizzas ! :D  return {    pizza: state.pizza + 1,  }}this.setState(addAnotherPizza);
```

Lisez plus [ici](https://x-team.com/blog/react-render-setstate/).

### Création de Refs

La création de refs avec React16 est maintenant beaucoup plus facile. Pourquoi vous devez utiliser des refs :

* Gérer le focus, la sélection de texte ou la lecture de médias.
* Déclencher des animations impératives.
* Intégration avec des bibliothèques DOM tierces.

Les refs sont créés en utilisant `React.createRef()` et sont attachés aux éléments React via l'attribut `ref`. Les refs sont généralement assignés à une propriété d'instance lors de la construction d'un composant afin qu'ils puissent être référencés dans tout le composant.

```
class MyComponent extends React.Component {  constructor(props) {    super(props);    this.myRef = React.createRef();  }  render() {    return <div ref={this.myRef} />;  }}
```

#### **Accéder aux Refs**

Lorsque une ref est passée à un élément dans `render`, une référence au nœud devient accessible à l'attribut `current` de la ref.

```
const node = this.myRef.current;
```

La valeur de la ref diffère en fonction du type de nœud :

* Lorsque l'attribut `ref` est utilisé sur un élément HTML, la `ref` créée dans le constructeur avec `React.createRef()` reçoit l'élément DOM sous-jacent comme propriété `current`.
* Lorsque l'attribut `ref` est utilisé sur un composant de classe personnalisé, l'objet `ref` reçoit l'instance montée du composant comme `current`.
* **Vous ne pouvez pas utiliser l'attribut `ref` sur des composants fonctionnels** car ils n'ont pas d'instances.

### API de Contexte

Le contexte fournit un moyen de transmettre des données à travers l'arbre des composants sans avoir à passer manuellement les props à chaque niveau.

#### `React.createContext`

```
const {Provider, Consumer} = React.createContext(defaultValue);
```

Crée une paire `{ Provider, Consumer }`. Lorsque React rend un `Consumer` de contexte, il lira la valeur actuelle du contexte depuis le `Provider` correspondant le plus proche au-dessus dans l'arbre.

L'argument `defaultValue` est **uniquement** utilisé par un `Consumer` lorsqu'il n'a pas de `Provider` correspondant au-dessus dans l'arbre. Cela peut être utile pour tester des composants en isolation sans les envelopper. Note : passer `undefined` comme valeur de `Provider` ne fait pas que les `Consumers` utilisent `defaultValue`.

#### `Provider`

```
<Provider value={/* une valeur */}>
```

Un composant React qui permet aux `Consumers` de s'abonner aux changements de contexte.

Accepte une prop `value` à passer aux `Consumers` qui sont des descendants de ce `Provider`. Un `Provider` peut être connecté à de nombreux `Consumers`. Les `Providers` peuvent être imbriqués pour remplacer les valeurs plus profondément dans l'arbre.

#### `Consumer`

```
<Consumer>  {value => /* rendre quelque chose basé sur la valeur du contexte */}&lt;/Consumer>
```

Un composant React qui s'abonne aux changements de contexte.

Nécessite une [fonction comme enfant](https://reactjs.org/docs/render-props.html#using-props-other-than-render). La fonction reçoit la valeur actuelle du contexte et retourne un nœud React. L'argument `value` passé à la fonction sera égal à la prop `value` du `Provider` le plus proche pour ce contexte au-dessus dans l'arbre. S'il n'y a pas de `Provider` pour ce contexte au-dessus, l'argument `value` sera égal à la `defaultValue` qui a été passée à `createContext()`.

### `static getDerivedStateFromProps()`

`getDerivedStateFromProps` est invoqué juste avant d'appeler la méthode de rendu. À la fois lors du montage initial et lors des mises à jour suivantes. Il doit retourner un objet pour mettre à jour l'état, ou null pour ne rien mettre à jour.

Cette méthode existe pour des [cas d'utilisation rares](https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#when-to-use-derived-state) où l'état dépend des changements dans les props au fil du temps. Par exemple, cela peut être pratique pour implémenter un composant `<Transition>` qui compare ses enfants précédents et suivants pour décider lesquels animer en entrée et en sortie.

Dériver l'état conduit à un code verbeux et rend vos composants difficiles à comprendre.

[Assurez-vous d'être familier avec des alternatives plus simples :](https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html)

* Si vous devez **effectuer un effet secondaire** (par exemple, récupérer des données ou une animation) en réponse à un changement de props, utilisez le cycle de vie `[componentDidUpdate](https://reactjs.org/docs/react-component.html#componentdidupdate)` à la place.
* Si vous voulez **re-calculer certaines données uniquement lorsqu'une prop change**, [utilisez un helper de mémoisation à la place](https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#what-about-memoization).
* Si vous voulez **"réinitialiser"** un état lorsqu'une prop change, envisagez soit de rendre un composant [totalement contrôlé](https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#recommendation-fully-controlled-component) ou [totalement non contrôlé avec une `key`](https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#recommendation-fully-uncontrolled-component-with-a-key) à la place.

Cette méthode n'a pas accès à l'instance du composant. Si vous le souhaitez, vous pouvez réutiliser du code entre `getDerivedStateFromProps()` et les autres méthodes de classe en extrayant des fonctions pures des props et de l'état du composant en dehors de la définition de la classe.

Notez que cette méthode est déclenchée à _chaque_ rendu, indépendamment de la cause. Cela contraste avec `UNSAFE_componentWillReceiveProps`. Elle ne se déclenche que lorsque le parent provoque un re-rendu et non à la suite d'un `setState` local.

Nous comparons `nextProps.someValue` avec `this.props.someValue`. Si les deux sont différents, nous effectuons une opération, `setState`

```
static getDerivedStateFromProps(nextProps, prevState){   if(nextProps.someValue!==prevState.someValue){        return { someState: nextProps.someValue};  } else return null;}
```

Elle reçoit deux paramètres `nextProps` et `prevState`. Comme mentionné précédemment, vous ne pouvez pas accéder à `this` à l'intérieur de cette méthode. Vous devrez stocker les props dans l'état pour comparer les `nextProps` avec les props précédents. Dans le code ci-dessus, `nextProps` et `prevState` sont comparés. Si les deux sont différents, un objet sera retourné pour mettre à jour l'état. Sinon, `null` sera retourné indiquant que la mise à jour de l'état n'est pas nécessaire. Si l'état change, alors `componentDidUpdate` est appelé où nous pouvons effectuer les opérations souhaitées comme nous l'avons fait dans `componentWillReceiveProps`.

### Bonus : Événements du cycle de vie de React

![Image](https://cdn-media-1.freecodecamp.org/images/1*6sVjMFCtW_dS_2MserkyQw.jpeg)

Crédits du cycle de vie — [https://twitter.com/dceddia](https://twitter.com/dceddia)

Eh bien, ce sont quelques-unes des fonctionnalités que vous devriez définitivement essayer en travaillant avec React16 !

Bon codage 😊 😊