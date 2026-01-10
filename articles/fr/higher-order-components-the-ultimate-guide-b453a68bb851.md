---
title: 'Composants d''ordre supérieur : Le guide ultime'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-28T15:42:02.000Z'
originalURL: https://freecodecamp.org/news/higher-order-components-the-ultimate-guide-b453a68bb851
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ocK9Z4_zq2X0Y1uqvhWMEg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: 'Composants d''ordre supérieur : Le guide ultime'
seo_desc: 'By David Kopal

  The maintainable component structure is a crucial prerequisite for a stable React
  application. You can achieve this by writing your code in a functional way using
  higher-order components (HoCs). If you stick to this pattern, you’ll end...'
---

Par David Kopal

La structure des composants maintenables est un préalable crucial pour une application React stable. Vous pouvez y parvenir en écrivant votre code de manière fonctionnelle en utilisant des composants d'ordre supérieur (HoCs). Si vous respectez ce modèle, vous obtiendrez des composants réutilisables qui sont à la fois lisibles et faciles à tester, car chaque composant n'est responsable que d'une seule tâche.

Dans cet article, j'aimerais partager mon expérience afin que vous puissiez facilement utiliser cette approche dans vos propres applications. Non seulement vous apprendrez à améliorer vos composants de présentation en utilisant un ou plusieurs HoCs, mais vous comprendrez également les principes derrière ce modèle.

### Pourquoi cet article est-il si long ?

Lorsque j'ai commencé à apprendre les HoCs moi-même, je n'ai eu aucun problème à trouver des ressources traitant de ce sujet. Cependant, beaucoup d'entre elles supposaient certaines connaissances préalables de sujets complexes, tels que les principes de la programmation fonctionnelle (FP). Par conséquent, il était difficile pour moi de comprendre ce qui se passait sous le capot et comment la composition de plusieurs HoCs fonctionne.

C'est cette expérience qui m'a motivé à écrire cet article de manière plus large et plus adaptée aux débutants. Il couvre donc non seulement les HoCs, mais aussi les principes de la FP et les idées fondamentales que l'on doit comprendre pour pouvoir libérer la puissance des composants d'ordre supérieur.

Cet article est également basé sur [ma première conférence technique](https://www.codinglawyer.io/posts/my-first-tech-talk) que j'ai donnée à la International JavaScript Conference (iJS) 2017 à Munich. Vous pouvez trouver tout le code source sur [Github](https://github.com/codinglawyer/international-javascript-conference-2017).

### Pour commencer

Commençons par regarder un peu de code :

```
const starWarsChars = [   { name:'Luke', side:'light' },   { name:'Darth Vader', side:'dark' },   { name:'Obi-wan Kenobi', side:'light'},   { name:'Palpatine', side:'dark'},]
```

```
class FilteredList extends React.Component {   constructor(props) {      super(props)      this.state = { value: this.props.defaultState }   }   updateState(value) {      this.setState({ value })   }   render() {      const otherSide = this.state.value === 'dark' ? 'light' : 'dark'      const transformedProps = this.props.list.filter(char => char.side === this.state.value)      return (         <div>            <button onClick={() => this.updateState(otherSide)}>Switch</button>            {transformedProps.map(char =>               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render (   <FilteredList defaultState='dark' list={starWarsChars} />,   document.getElementById('app'))
```

`FilteredList` est un énorme composant qui fait tant de choses. Il maintient l'état et filtre la `list` des personnages de Star Wars selon leur côté. De plus, il rend la liste des personnages avec un bouton à l'écran.

Il s'occupe de toute la logique et de la présentation, et à cause de cela, il est rarement réutilisable.

Si vous décidez de réutiliser ce composant ailleurs, vous devrez toujours utiliser toute la logique et l'UI du composant. Vous ne pouvez pas simplement choisir la fonctionnalité dont vous avez vraiment besoin pour un scénario particulier. Au lieu de cela, vous serez obligé de réécrire un morceau de comportement déjà existant en tant que composant différent.

![Image](https://cdn-media-1.freecodecamp.org/images/pjwdpoNQlgtziUpuadP7bbgc-l8oFK73vay9)

En conséquence, un tel code répété serait difficile à maintenir, surtout dans une application plus grande.

À la fin de cet article, nous serons en mesure d'écrire une version entièrement réutilisable de ce code en utilisant les principes de la programmation fonctionnelle (FP).

Restez à l'écoute.

### Goûtez aux principes de la programmation fonctionnelle

Pour vous montrer pourquoi vous devriez respecter les principes de la FP dans une application React, je dois parler un peu des principes fondamentaux de la FP elle-même.

L'idée est de décomposer un programme en fonctions **réutilisables** simples.

Donc, tout est une question de fonctions. Pour être plus précis, tout est une question de **fonctions simples**. Cela signifie que chaque fonction ne doit être responsable que d'une seule tâche. Plus la fonction est simple, plus elle est réutilisable.

#### Fonctions d'ordre supérieur

En JavaScript, vous pouvez utiliser une fonction comme n'importe quelle autre valeur. Elle peut être passée en argument à une fonction ou elle peut être retournée par celle-ci. Une fonction qui **retourne ou crée une nouvelle fonction** est appelée une fonction d'ordre supérieur.

```
const numbers = [1, 5, 8, 10, 21]const createAddingFunction = number => arr => arr.map(num => num + number)const numbersPlusOne = createAddingFunction(1)console.log(numbersPlusOne(numbers))  // [2, 6, 9, 11, 22]
```

`createAddingFunctions` est une fonction d'ordre supérieur. Elle prend un `number` et crée une nouvelle fonction attendant que le tableau soit passé. Dans l'exemple, nous lui passons `1` et obtenons une nouvelle fonction attendant un tableau. Nous la stockons sous `numbersPlusOne`. Ensuite, nous lui passons le tableau `numbers`. La fonction parcourt alors les éléments du tableau et augmente chacun d'un.

Comme vous pouvez le voir, nous disons au moteur JavaScript **ce** que nous voulons faire — nous voulons mapper les éléments du tableau. Ce code est auto-explicatif. Vous voyez simplement le code et vous savez immédiatement ce qui se passe. Un tel code est appelé **déclaratif**. La programmation fonctionnelle est tout au sujet du code déclaratif.

![Image](https://cdn-media-1.freecodecamp.org/images/wSxQZsAuLdO-eZ1CMEyYXxYdn6MzAUVNI8WO)

#### Éviter les effets secondaires

En tant que programmeur fonctionnel, vous voulez éviter les effets secondaires dans vos fonctions autant que possible. En d'autres termes, une fonction ne devrait pas changer quoi que ce soit qui n'est pas local à la fonction elle-même. Vous pouvez réutiliser une telle fonction facilement, n'importe où dans votre application. Les fonctions sans effets secondaires sont appelées **pures**. Elles retournent toujours la même sortie, étant donné les mêmes arguments.

Si vous voulez écrire des fonctions pures, vous devez également éviter de muter vos valeurs. Cela s'appelle le principe de **l'immuabilité**. Cependant, cela ne signifie pas que vous ne changez pas vos valeurs. Cela signifie que lorsque vous voulez changer une valeur, vous en créez une nouvelle plutôt que de muter l'originale.

Cependant, en JavaScript, des valeurs telles que les objets et les tableaux sont mutables. Afin de respecter le principe d'immuabilité, nous pouvons traiter les valeurs comme immuables.

Par exemple, en adhérant à ce principe, vous ne pourrez pas muter accidentellement un objet qui a été passé à une fonction en tant que paramètre.

```
// fonction pureconst numbers = [1, 5, 8, 10, 21]const createAddingFunction = number => arr => arr.map(num => num + number)const numbersPlusOne = createAddingFunction(1)console.log(numbersPlusOne(numbers))  //[2, 6, 9, 11, 22]console.log(numbers)  // [1, 5, 8, 10, 21]
```

```
// fonction impureconst numbers = [1, 5, 8, 10, 21]const numbersPlusOne = numbers => {   for(let i = 0; i < numbers.length; i++) {      numbers[i] = numbers[i] + 1   }   return numbers}numbersPlusOne(numbers) // [2, 6, 9, 11, 22]console.log(numbers) // [2, 6, 9, 11, 22]
```

Ici, nous avons un exemple de fonction pure (identique à celui d'un exemple précédent) et de fonction impure. Dans le premier cas, le fait que nous ayons passé un tableau à la fonction pure n'a pas affecté le tableau `numbers` de quelque manière que ce soit.

Cependant, dans le deuxième scénario, le tableau a été muté à l'intérieur de la fonction impure. Un tel comportement peut rendre votre code assez imprévisible. Et surtout dans le domaine de la programmation fonctionnelle, nous voulons éviter cela.

#### Composition

Jusqu'à présent, nous savons que nous devons créer des fonctions pures simples. Cependant, que faire si nous avons besoin d'un comportement si complexe qu'il ne peut pas être stocké dans une seule fonction ? Nous pourrions y parvenir en combinant plusieurs fonctions en une nouvelle fonction composée à l'aide de la composition.

```
const number = 15const increment = num => num + 5const decrement = num => num - 3const multiply = num => num * 2
```

```
const operation = increment(decrement(multiply(number)))console.log(operation)  //32
```

La composition signifie que nous passons la sortie du premier appel de fonction comme entrée au deuxième appel de fonction, sa sortie au troisième appel de fonction et ainsi de suite. En conséquence, nous obtenons une fonction composée.

Dans notre exemple, nous avons un `number` et trois fonctions. Nous les enveloppons toutes les unes dans les autres, et nous obtenons une fonction composée attendant l'argument `number`. En utilisant la composition, nous n'avons pas besoin de créer des variables pour stocker le résultat des fonctions individuelles.

#### Combiné

Pour vraiment voir les avantages de tous ces principes de FP, vous devez les combiner ensemble.

Idéalement, votre application devrait être composée de **fonctions pures** dont les données sont traitées comme **immuables**. Cela signifie qu'elles ne modifient pas leur portée supérieure et que vous êtes donc libre de les réutiliser dans n'importe quelle partie de votre programme. Chaque fonction devrait être responsable d'une seule tâche et devrait être séparée des autres. Vous pouvez les utiliser telles quelles ou vous pouvez les **composer** ensemble pour obtenir un comportement plus complexe.

En respectant les principes de la FP, vous obtiendrez des fonctions simples et réutilisables qui peuvent être composées ensemble.

![Image](https://cdn-media-1.freecodecamp.org/images/e3godfqlWfBBv2VvlpjzA4LfUVmnMPOl-sTX)

### Programmation fonctionnelle et React

Maintenant que nous sommes familiers avec les principes de base de la FP, nous pouvons examiner comment les utiliser à notre avantage dans React.

Les applications React sont composées de composants. Mais qu'est-ce qu'un composant exactement ?

```
// Composant basé sur une classeclass Button extends React.Component {   render(){      return <button>{this.props.title}</button>   }}
```

```
// Composant fonctionnelconst Button = (props) =>   <button>{props.title}</button>
```

Puisque la classe n'est que du sucre syntaxique sur les fonctions et que le composant fonctionnel est essentiellement une fonction, **les composants sont juste des fonctions**. C'est une fonction qui prend des données d'entrée (props) et retourne un arbre d'éléments React (UI) qui est rendu à l'écran. Cependant, il n'a pas besoin de retourner de l'UI tout le temps. Il peut retourner un composant ainsi que nous allons le voir plus tard.

Donc, l'UI React est juste une **composition de fonctions**. Cela ressemble terriblement à la FP, n'est-ce pas ?

#### Composants intelligents et de présentation

Un composant est généralement composé de logique et de présentation. Cependant, si nous décidons d'écrire tous nos composants de cette manière, nous finirons avec des dizaines de composants n'ayant qu'un seul but. D'un autre côté, si nous essayons de [séparer ces préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns), nous serons en mesure de créer des composants simples et réutilisables. En suivant cette idée, nous devrions préférer définir nos composants comme intelligents (logique) et de présentation (UI).

![Image](https://cdn-media-1.freecodecamp.org/images/ZY1YlmlV6sbafDF3tYlxfAsmpef81Qj3bPtF)

Le composant de **présentation** s'occupe de toute l'UI. Il aura généralement la forme d'un composant **fonctionnel**, qui est juste une méthode de rendu. Vous pouvez les considérer comme des fonctions.

Le composant contenant principalement de la logique est appelé **intelligent**. Il gère généralement les manipulations de données, les appels API et les gestionnaires d'événements. Il sera souvent défini comme une **classe** puisqu'il nous offre plus de fonctionnalités (comme l'état interne et le cycle de vie).

Chaque composant doit être responsable d'une seule tâche et écrit de manière si générale qu'il peut être réutilisé dans toute l'application. Une telle tâche doit être soit de la logique (composant intelligent) soit de la présentation (composant de présentation). La combinaison des deux dans un seul composant doit être minimisée.

* **composant de classe intelligent**

```
class DisplayList extends Component {   constructor(props) {      super(props)      this.state = {         starWarsChars: [            { name:'Luke Skywalker', side:'light' },            { name:'Darth Vader', side:'dark' },            { name:'Obi-wan Kenobi', side:'light' },            { name:'Palpatine', side:'dark' },         ]      }   }   render() {      return (         <div>            {this.state.starWarsChars.map(char =>               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render(   <DisplayList />,   document.getElementById('app'))
```

* **composant fonctionnel de présentation**

```
const starWarsChars = [   { name:'Luke', side:'light' },   { name:'Darth Vader', side:'dark' },   { name:'Obi-wan Kenobi', side:'light'},   { name:'Palpatine', side:'dark'},]
```

```
const DisplayList = ({ list }) =>   <div>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>
```

```
ReactDOM.render (   <DisplayList list={starWarsChars} />,   document.getElementById('app'))
```

Regardons le composant fonctionnel. Il est assez réutilisable puisqu'il ne s'occupe que de l'UI. Donc, si vous voulez afficher une liste de personnages de Star Wars ailleurs dans votre application, vous pouvez facilement réutiliser ce composant. Il n'a également aucun effet secondaire puisqu'il n'affecte pas sa portée externe de quelque manière que ce soit.

Vous pouvez voir que le composant fonctionnel est juste une **fonction pure** qui prend un objet props et retourne la même UI étant donné les mêmes props.

Non seulement cette application React est une composition de fonctions en général, mais elle peut aussi être une **composition de fonctions pures**.

Comme nous l'avons déjà appris, les fonctions pures sont les blocs de construction de base de la FP. Donc, si nous préférons utiliser des composants fonctionnels, nous serons en mesure d'**appliquer diverses techniques de FP** telles que les composants d'ordre supérieur dans notre code.

![Image](https://cdn-media-1.freecodecamp.org/images/akA76VKyKkf2fR6ELKTOTK5S74uV92gPRP-p)

#### Ajout de plus de logique

Regardons à nouveau notre composant fonctionnel. Il prend une liste de personnages de Star Wars en tant que prop et les rend à l'écran. Il est assez réutilisable puisqu'il ne contient aucune logique.

Maintenant, que faire si nous voulions afficher uniquement les personnages appartenant au côté obscur ? La solution la plus simple sera de filtrer la prop `list` à l'intérieur du composant.

```
const FilteredList = ({ list, side }) => {   const filteredList = list.filter(char => char.side === side)   return (      <div>         {filteredList.map(char =>            <div key={char.name}>               <div>Character: {char.name}</div>               <div>Side: {char.side}</div>            </div>         )}      </div>   )}
```

```
ReactDOM.render (   <FilteredList side='dark' list={starWarsChars}/>,   document.getElementById('app'))
```

Cela fera l'affaire. Nous avons renommé `DisplayList` en `FilteredList` puisqu'il contient maintenant une fonctionnalité de filtrage. Nous passons également maintenant la prop `side` selon laquelle la liste sera filtrée.

Cependant, est-ce la solution idéale ? Comme vous pouvez le voir, le composant `FilteredList` n'est plus réutilisable. À cause de la fonction de filtrage intégrée à l'intérieur, ce composant peut rarement être réutilisé.

Si nous voulions afficher des personnages ailleurs dans notre application sans aucun filtrage, nous devrions créer un autre composant. De plus, si nous voulions utiliser la fonction de filtrage dans d'autres composants, nous devrions également dupliquer ce comportement.

Heureusement, il existe une **solution plus élégante et déclarative** qui nous permet de garder notre composant de présentation réutilisable. Nous sommes en mesure de filtrer la liste des personnages avant qu'elle ne soit passée en tant que prop au composant `DisplayList`.

```
const withFilterProps = BaseComponent => ({ list, side }) => {   const transformedProps = list.filter(char => char.side === side)   return <BaseComponent list={transformedProps} />}
```

```
const renderDisplayList = ({ list }) =>   <div>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>
```

```
const FilteredList = withFilterProps(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList side='dark' list={starWarsChars} />,   document.getElementById('app'))
```

Nous avons renommé notre composant fonctionnel `renderDisplayList` pour rendre évident qu'il n'est responsable que du rendu de l'UI.

Tout d'abord, regardons le composant `FilteredList`. Ce composant est créé en passant notre composant fonctionnel `renderDisplayList` à la fonction d'ordre supérieur `withFilterProps`. Lorsque cela se produit, nous obtenons un composant fonctionnel et le stockons sous `FilteterdList` en attendant que l'objet props soit passé.

Nous rendons le composant `FilteredList` à la fin de l'exemple en passant les props. Il filtre la liste des personnages à partir des props selon la prop `side`. La liste filtrée est ensuite passée en tant que props à `renderDisplayList`, qui rend ensuite la liste des personnages à l'écran.

### Introduction aux composants d'ordre supérieur

![Image](https://cdn-media-1.freecodecamp.org/images/BZQLvTD70AGyVbm5WxLfeoJfyMIm4RaMUjrU)

Parlons maintenant de la nature de la fonction d'ordre supérieur `withFilterProps`. Dans le vocabulaire de React, une telle fonction est appelée un composant d'ordre supérieur (HoC). Tout comme la fonction d'ordre supérieur crée une nouvelle fonction, le HoC crée un nouveau composant.

HoC est une **fonction** qui **accepte** **un composant** et **retourne un nouveau composant qui rend le passé**. Ce nouveau composant est amélioré avec une fonctionnalité supplémentaire.

```
const HoC = BaseComponent => EnhancedComponent
```

Dans notre exemple, le HoC `withFilterProps` prend le composant `renderDisplayList` et retourne un nouveau composant fonctionnel qui rend le `renderDisplayList`. Le composant `renderDisplayList` est amélioré avec la logique des props de filtrage.

Parce que nous avons abstrait toute la logique dans le HoC, notre composant fonctionnel de base ne s'occupe que du rendu de l'UI et est réutilisable à nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/zwq70rgYR7Ne9yoFWhFPgutiaSx-LztiBCDM)

Le HoC est un type spécial de fonction qui enveloppe le composant de présentation et l'améliore avec une fonctionnalité avancée. Considérez-les comme les **enveloppes pour vos composants fonctionnels**.

Grâce au modèle HoC, vous pouvez améliorer vos simples composants fonctionnels avec la logique que vous voulez. C'est la puissance du modèle HoC. Vous pouvez éditer/mettre à jour/transformer les props, maintenir l'état interne, ou affecter le rendu du composant en dehors de votre composant de présentation.

En respectant ce modèle, vous pourrez utiliser uniquement des composants fonctionnels comme vos composants de base dans toute votre application et vous débarrasser de tous les composants de classe.

Si nous considérons à nouveau la distinction entre les composants intelligents et de présentation, le composant de base sera toujours celui de présentation (puisqu'il s'agit d'une fonction pure). D'un autre côté, le HoC prendra le rôle d'un composant **intelligent** puisqu'il ne traite que de la logique, qui est ensuite transmise au composant de présentation. Cependant, si vous n'avez pas besoin du comportement spécifique à la classe, vous pouvez également définir le HoC comme un composant fonctionnel (comme vous venez de le voir).

Puisque vous êtes arrivé jusqu'ici, ralentissons un peu et parlons de nourriture :)

#### Pain de viande ou Pancake

Au début de cet article, nous avons vu ce composant difficile à réutiliser qui s'occupe de toute la logique et de la présentation.

```
class FilteredList extends React.Component {   constructor(props) {      super(props)      this.state = { value: this.props.defaultState }   }   updateState(value) {      this.setState({ value })   }   render() {      const otherSide = this.state.value === 'dark' ? 'light' : 'dark'      const transformedProps = this.props.list.filter(char => char.side === this.state.value)      return (         <div>            <button onClick={() => this.updateState(otherSide)}>Switch</button>            {transformedProps.map(char =>               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render (   <FilteredList defaultState='dark' list={starWarsChars} />,   document.getElementById('app'))
```

Vous pouvez penser à ce composant comme à un **pain de viande**.

![Image](https://cdn-media-1.freecodecamp.org/images/kLsEptFbZS0hA6sgb1wfhSwQDGFdZiUHzxQK)

Lorsque vous préparez un pain de viande, vous prenez la viande, la chapelure, l'ail, l'oignon et les œufs, vous les mélangez ensemble, vous mettez le pain de viande cru dans le four et vous attendez qu'il soit cuit. Il n'y a aucun moyen de prendre les œufs ou l'oignon du pain de viande, puisque tout est irrévocablement combiné ensemble.

C'est la même chose qu'un composant qui est un mélange de logique et d'UI. Vous ne pouvez simplement pas prendre quelque chose de celui-ci. **Vous devez l'utiliser tel quel ou pas du tout.**

Essayez de penser aux composants de présentation comme à des **pancakes**.

![Image](https://cdn-media-1.freecodecamp.org/images/nokhg0VKb67G3lVvbA5Mv4wfCGAJ4iUtpsxG)

Cependant, des pancakes simples sans aucune décoration sont assez ennuyeux, et personne ne les mange comme ça de toute façon. Donc, vous voulez les décorer. Vous pouvez verser du sirop d'érable dessus ou mettre quelques baies ou du chocolat sur le dessus. Tant de couches de décoration possibles à utiliser !

![Image](https://cdn-media-1.freecodecamp.org/images/D9QHuPyjOO7sbx4xWIOSAkL4SFiEsyZfDKIE)

Dans l'application React, ces couches de décoration sont représentées par les HoCs. Donc, tout comme vous décorez un pancake selon vos goûts, vous décorez également le composant de présentation en utilisant le HoC avec la fonctionnalité que vous voulez. En conséquence, **vous pouvez réutiliser un composant de présentation particulier dans différentes parties de votre application** et le décorer avec le HoC que vous voulez pour un cas particulier.

Cependant, vous ne pouvez pas faire cela avec le composant qui est responsable de toute la logique et de la présentation, puisque tout est irrévocablement combiné ensemble.

J'espère que cette métaphore vous a donné une meilleure compréhension du modèle HoC. Si ce n'est pas le cas, au moins je vous ai rendu affamé :).

### Rendre tous les composants réutilisables à nouveau

Maintenant que nous savons comment créer un HoC, nous allons voir comment le rendre réutilisable.

Rendre les composants réutilisables signifie **les découpler des données**. Cela signifie qu'ils ne doivent pas dépendre d'une structure de props particulière. En utilisant des composants réutilisables, vous évitez les duplications inutiles. Vous passez simplement un ensemble différent de props à chaque fois.

En utilisant le modèle HoC dans l'exemple précédent, nous avons déplacé toute la logique vers le HoC, et avons simplement laissé le composant de base rendre l'UI. En conséquence, notre **composant de présentation est devenu réutilisable** puisqu'il reçoit simplement des données en tant que props et les rend à l'écran.

Mais il serait assez difficile de réutiliser notre HoC également, puisqu'il est trop spécifique.

```
const withFilterProps = BaseComponent => ({ list, side }) => {   const transformedProps = list.filter(char => char.side === side)   return <BaseComponent list={transformedProps} />}
```

Il ne peut être appliqué que dans les cas où les props `list` et `side` sont présentes. Vous ne voulez pas ce genre de spécificité dans votre application puisque vous voulez des HoCs réutilisables qui peuvent être utilisés dans divers scénarios.

Rendons le HoC réutilisable.

![Image](https://cdn-media-1.freecodecamp.org/images/-j5TCVnvuAmfoAfTmPX2WrVTRabraGpWDaRs)

```
const withTransformProps = transformFunc => {   const ConfiguredComponent = BaseComponent => {      return baseProps => {         const transformedProps = transformFunc(baseProps)         return <BaseComponent {...transformedProps} />      }   }   return ConfiguredComponent}
```

```
const renderDisplayList = ({ list }) =>   <div>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>
```

```
const FilteredList = withTransformProps(   ({ list, side }) => ({      list: list.filter(FilteredListchar =>         char.side === side)   }))(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList      side='dark'      list={starWarsChars}   />,   document.getElementById('app'))
```

Ce code fait toujours la même chose que l'exemple précédent de HoC. Nous filtrons les props en utilisant le composant HoC, puis nous les passons au composant de base. Cependant, l'ancien nom serait trompeur, puisque le HoC n'est plus limité uniquement à la logique de filtrage, nous l'avons donc renommé `withTransformProps`.

Nous ne nous soucions plus de la structure des props. Nous passons maintenant une `transformFunc` en tant que **fonction de configuration** à `withTransformProps`. Cette fonction est responsable de la transformation des props.

Regardons le composant amélioré `FilteredList`. Il est créé lorsque nous passons la fonction de configuration (responsable de la transformation des props) à `withTransformProps`. Nous obtenons un HoC spécialisé avec la fonction de transformation stockée à l'intérieur de la fermeture. Nous le stockons sous `ConfiguredComponent`. Il attend que le `BaseComponent` soit passé. Lorsque `renderDisplayList` lui est passé, nous obtenons un composant fonctionnel qui attend que les props soient passés. Nous stockons ce composant amélioré sous `FilteredList`.

Les props sont passés lorsque nous rendons le composant `FilteredList`. Ensuite, la fonction de transformation que nous avons passée précédemment prend les props et filtre les personnages selon le côté. La valeur retournée est ensuite passée en tant que props au composant de base `renderDisplayList` qui rend les personnages filtrés de Start Wars à l'écran.

Cependant, notre syntaxe HoC est assez verbeuse. Nous n'avons pas besoin de stocker le HoC spécialisé sous `ConfiguredComponent` à l'intérieur d'une variable.

```
const withTransformProps = mapperFunc =>   BaseComponent => baseProps => {      const transformedProps = mapperFunc(baseProps)      return <BaseComponent {...transformedProps} />   }
```

Cette solution est beaucoup plus propre.

L'idée derrière cette approche est d'**avoir un HoC réutilisable qui peut être configuré pour n'importe quel scénario** dans lequel nous voulons faire quelque chose avec les props avant qu'ils ne soient passés au composant de base. C'est une abstraction puissante, n'est-ce pas ?

Dans notre exemple, nous avons passé une fonction de filtrage personnalisée qui pourrait être différente pour chaque cas d'utilisation. Et si nous décidons plus tard que nous voulons changer certains comportements du HoC, nous devons simplement le changer dans un seul composant réutilisable et non dans de nombreux endroits différents de notre application.

```
const HoC = config => BaseComponent => EnhancedComponent
```

Le HoC et le composant de base sont tous deux **réutilisables** et **indépendants** l'un de l'autre. Le HoC ne sait pas où vont ses données et le composant de présentation n'a aucune idée d'où viennent ses données.

L'écriture de HoCs et de composants de présentation réutilisables vous aidera à éviter les répétitions inutiles et vous forcera à écrire des composants plus simples. **En conséquence, vous écrirez un code plus propre, maintenable et lisible.**

![Image](https://cdn-media-1.freecodecamp.org/images/HzHa3iKWnGZHjcNm7c0aTQTANWUUkIEqQDFy)

Félicitations ! À ce stade, vous devriez être capable d'écrire vous-même des composants d'ordre supérieur réutilisables.

Dans les sections suivantes, vous apprendrez la différence entre un HoC de classe et un HoC fonctionnel. Nous passerons également beaucoup de temps à comprendre comment fonctionne la composition de plusieurs composants d'ordre supérieur. Tout cela nous permettra d'améliorer nos composants de base avec encore plus de comportements qui peuvent être facilement réutilisés dans toute notre application.

### HoCs fonctionnels ou basés sur des classes ?

![Image](https://cdn-media-1.freecodecamp.org/images/bfxSr1qSfYN01qO-eUZjwJmJyDhuFuytOmOr)

Parlons un peu de la différence entre les HoCs fonctionnels et ceux basés sur des classes. Quand est-il plus pratique de s'en tenir aux premiers et quand devriez-vous opter pour les seconds ?

Puisque nous voulons suivre les principes de la programmation fonctionnelle, nous devrions utiliser des **composants fonctionnels** autant que possible. Nous le faisons déjà avec les composants de présentation comme nous l'avons vu ci-dessus. Et nous devrions faire de même avec les HoCs.

#### HoC fonctionnel

Un HoC fonctionnel enveloppe simplement le composant de base, lui injecte de nouvelles props ainsi que les originales, et retourne un nouveau composant. Il ne modifie pas le composant original en modifiant son prototype comme le font les classes. Nous avons vu un tel HoC ci-dessus. Voici un rappel rapide :

```
const withTransformProps = mapperFunc =>   BaseComponent => baseProps => {      const transformedProps = mapperFunc(baseProps)      return <BaseComponent {...transformedProps} />   }
```

Ce HoC n'a aucun effet secondaire. Il ne mute rien. C'est une fonction pure.

Lors de la création d'un HoC, nous devrions le définir comme un composant fonctionnel si possible.

#### HoCs basés sur des classes

Cependant, tôt ou tard, vous aurez besoin d'accéder à l'état interne ou aux méthodes du cycle de vie dans votre composant. Vous ne pouvez pas y parvenir sans classes puisque ce comportement est hérité de [React.Component](https://facebook.github.io/react/docs/react-component.html), qui ne peut pas être accessible dans le composant fonctionnel. Donc, définissons un HoC basé sur une classe.

```
const withSimpleState = defaultState => BaseComponent => {   return class WithSimpleState extends React.Component {      constructor(props) {         super(props)         this.state = { value: defaultState }         this.updateState = this.updateState.bind(this)      }      updateState(value) {         this.setState({ value })      }      render() {         return (            <BaseComponent               {...this.props}               stateValue={this.state.value}               stateHandler={this.updateState}            />         )      }   }}
```

```
const renderDisplayList = ({ list, stateValue, stateHandler })=&gt; {   const filteredList = list.filter(char => char.side === stateValue)   const otherSide = stateValue === 'dark' ? 'light' : 'dark'   return (      <div>         <button onClick={() => stateHandler(otherSide)}>Switch</button>         {filteredList.map(char =>            <div key={char.name}>               <div>Character: {char.name}</div>               <div>Side: {char.side}</div>            </div>         )}      </div>   )}
```

```
const FilteredList = withSimpleState('dark')(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Notre nouveau HoC basé sur une classe `withSimpleState` attend un paramètre de configuration `defaultState` qui est assez explicite. Il maintient également un état nommé `value` et définit un gestionnaire d'événements `updateState` qui peut définir la valeur de l'état. Enfin, il transmet les utilitaires d'état ainsi que les props originales au composant de base.

`renderDisplayList` contient maintenant la logique de filtrage qui était précédemment stockée dans le HoC `withTransformProps`, donc il n'est plus réutilisable.

Regardons le composant `FilteredList`. Tout d'abord, nous passons la chaîne de configuration `dark` à `withSimpleState` et obtenons un HoC spécialisé attendant le composant de base. Donc, nous lui passons le composant `renderDisplayList` et obtenons un composant de classe attendant que les props soient passés. Nous stockons ce composant sous `FilteredList`.

À la fin de l'exemple, nous rendons le composant en lui passant les props. Lorsque cela se produit, le composant de classe définit l'état `value` sur `dark` et transmet l'état et son gestionnaire au composant `renderDisplayList` ainsi que la prop `list`.

`renderDisplayList` filtre ensuite la prop `list` selon la valeur d'état passée et définit la variable `otherSide`. Enfin, il rend la liste filtrée à l'écran ainsi que le bouton avec le gestionnaire d'état attaché. Lorsque le bouton est cliqué, l'état est défini sur la variable `otherSide`.

#### Est-ce que cela compte ?

![Image](https://cdn-media-1.freecodecamp.org/images/7SyB4ye4uAKg6cBt-EwR-3Oyu0nmQzJp3S2k)

Comme vous venez de le voir, notre nouveau HoC `withSimpleState` retourne une classe, au lieu d'un composant fonctionnel. Vous pourriez dire qu'il ne ressemble pas à une **fonction pure** puisqu'il contient un comportement impur spécifique à la classe (état). Cependant, regardons de plus près.

`withSimpleState` n'a aucun effet secondaire. Il ne mute rien. Il prend simplement le composant de base et en retourne un nouveau. Bien qu'il contienne le code impur lié à la classe, le HoC lui-même est toujours une fonction pure puisque « la pureté d'une fonction est jugée de l'extérieur, [indépendamment de ce qui se passe à l'intérieur](https://github.com/getify/Functional-Light-JS/blob/master/manuscript/ch5.md#containing-effects) ». Nous cachons essentiellement le code impur spécifique à la classe à l'intérieur de la fonction pure du HoC.

Le HoC (fonction pure) nous permet d'encapsuler le code impur lié à la classe à l'intérieur de celui-ci.

Si vous vous trouvez dans une situation où vous ne pouvez tout simplement pas écrire un composant fonctionnel parce que vous avez besoin d'un comportement lié à la classe, enveloppez le code impur à l'intérieur du HoC, qui est la fonction pure à la place, comme nous l'avons fait dans l'exemple.

#### Qu'est-ce qui suit ?

Si vous vérifiez à nouveau notre exemple, vous verrez que nous avons un nouveau problème. Le composant `renderDisplayList` n'est plus réutilisable puisque nous avons déplacé la logique de filtrage à l'intérieur.

Pour le rendre réutilisable à nouveau, nous devons déplacer la logique vers le HoC `withTransformProps`. Pour y parvenir, nous devons comprendre comment utiliser les HoCs `withTransformProps` et `withSimpleState` avec le composant de base en même temps et permettre à `renderDisplayList` de n'être responsable que de la présentation à nouveau. Nous pouvons obtenir ce comportement en utilisant la composition.

### Composition

![Image](https://cdn-media-1.freecodecamp.org/images/gC0gCeSTZ7mCgox08iZAMbPCLKJ9if38K1mg)

Nous avons déjà parlé du principe de composition au début. Il nous permet de combiner plusieurs fonctions en une nouvelle fonction composée. Voici un rappel rapide :

```
const number = 15const increment = num => num + 5const decrement = num => num - 3const multiply = num => num * 2
```

```
const operation = increment(decrement(multiply(number)))console.log(operation)  //32
```

Nous avons un nombre et trois fonctions. Nous les enveloppons toutes les unes dans les autres, et nous obtenons une fonction composée à laquelle nous passons le nombre.

Cela fonctionne bien. Cependant, la lisibilité pourrait s'aggraver si nous voulions composer encore plus de fonctions. Heureusement, nous pouvons définir une fonction de programmation fonctionnelle `compose` pour nous aider. Gardez à l'esprit qu'elle compose les fonctions de **droite à gauche**.

```
const compose = (...funcs) => value =>   funcs.reduceRight((acc, func) => func(acc)      , value)
```

```
const number = 15const increment = num => num + 5const decrement = num => num - 3const multiply = num => num * 2
```

```
const funcComposition = compose(   increment,   decrement,   multiply)
```

```
const result = funcComposition(number)console.log(result)  //32
```

Nous n'avons plus besoin d'envelopper explicitement les fonctions les unes dans les autres. Au lieu de cela, nous les passons toutes en tant qu'arguments à la fonction `compose`. Lorsque nous faisons cela, nous obtenons une nouvelle fonction composée attendant que l'argument `value` soit passé. Nous la stockons sous `funcComposition`.

Enfin, nous passons le `number` en tant que `value` à la fonction `funcComposition`. Lorsque cela se produit, `compose` passe la `value` à la fonction `multiply` (la plus à droite). La valeur retournée est ensuite passée en tant qu'entrée à la fonction `decrement` et ainsi de suite jusqu'à ce que toutes les fonctions de la composition aient été appelées. Nous stockons la valeur finale sous `result`.

#### Composition de HoCs

![Image](https://cdn-media-1.freecodecamp.org/images/b5c02CoroaWSkzvTh9sXCjy5A09qbP3lxdof)

Regardons comment nous pourrions `composer` plusieurs HoCs. Nous avons déjà appris que nos HoCs réutilisables ne doivent être responsables que d'une seule tâche. Cependant, que faire si nous avions besoin d'implémenter une logique complexe qui ne peut pas être stockée dans un seul HoC ? Pour y parvenir, nous voulons être en mesure de **combiner plusieurs HoCs ensemble et les envelopper autour du composant de base.**

Tout d'abord, regardons la composition de HoC sans un helper `compose` puisque c'est plus facile à comprendre ce qui se passe.

```
const withTransformProps = mapperFunc =>   BaseComponent => baseProps => {      const transformedProps = mapperFunc(baseProps)      return <BaseComponent {...transformedProps} />   }
```

```
const withSimpleState = defaultState => BaseComponent => {   return class WithSimpleState extends React.Component {      constructor(props) {         super(props)         this.state = { value: defaultState }         this.updateState = this.updateState.bind(this)      }      updateState(value) {         this.setState({ value })      }      render() {         return (            <BaseComponent               {...this.props}               stateValue={this.state.value}               stateHandler={this.updateState}            />         )      }   }}
```

```
const renderDisplayList = ({ list, stateHandler, otherSide }) => (   <div>      <button onClick={() => stateHandler(otherSide)}>Switch</button>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

```
const FilteredList = withTransformProps(({ list, stateValue, stateHandler }) => {   const otherSide = stateValue === 'dark' ? 'light' : 'dark'   return {      stateHandler,      otherSide,      list: list.filter(char => char.side === stateValue),   }})(renderDisplayList)
```

```
const ToggleableFilteredList = withSimpleState('dark')(FilteredList)
```

```
ReactDOM.render (   <ToggleableFilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Rien de nouveau ici. Nous avons déjà vu tout ce code. La nouveauté est que nous composons deux HoCs — `withSimpleState` qui nous fournit les utilitaires d'état et `withTransformProps` qui nous donne la fonctionnalité de transformation des props.

Nous avons deux composants améliorés ici : `FilteredList` et `ToggleableFilteredList`.

Tout d'abord, nous améliorons le composant `renderDisplayList` avec le HoC `withTransformProps` et le stockons sous `FilteredList`. Deuxièmement, nous améliorons le nouveau composant `FilteredList` en utilisant le HoC `withSimpleState` et le stockons sous `ToggleableFilteredList`.

`ToggleableFilteredList` est un composant amélioré par deux HoCs qui ont été composés ensemble.

Voici une description détaillée de la composition de HoC :

1. Nous passons une fonction de transformation de props au HoC `withTransformProps` et obtenons un HoC spécialisé attendant que le composant de base soit passé.
2. Nous lui passons le composant de présentation `renderDisplayList` et obtenons un nouveau composant fonctionnel attendant l'argument props.
3. Nous stockons ce composant amélioré sous `FilteredList`.
4. Nous passons la chaîne `dark` au HoC `withSimpleState` et obtenons un HoC spécialisé attendant que le composant de base soit passé.
5. Nous lui passons notre composant amélioré `FilteredList` en tant que composant de base et obtenons un composant de classe attendant les props.
6. Nous stockons cette **composition de composants d'ordre supérieur** sous `ToggleableFilteredList`.
7. Nous rendons le composant `ToggleableFilteredList` en lui passant les props `list`.
8. `ToggleableFilteredList` est le composant `FilteredList` amélioré par le HoC `withSimpleState`. Donc, les props sont d'abord passés au composant de classe qui a été retourné par ce HoC. À l'intérieur, les props sont améliorés avec un état et son gestionnaire. Ces props, ainsi que les originaux, sont ensuite passés à `FilteredList` en tant que composant de base.
9. `FilteredList` est un composant `renderDisplayList` amélioré par le HoC `withTransformProps`. Donc, les props sont d'abord passés au composant fonctionnel qui a été retourné par ce HoC. À l'intérieur, la prop `list` passée est filtrée en utilisant la fonction de transformation. Ces props, ainsi que les autres props, sont ensuite passés au composant de base `renderDisplayList`.
10. Enfin, le composant `renderDisplayList` rend la liste des personnages avec le bouton de bascule à l'écran.

La composition nous permet d'améliorer notre composant de base avec la fonctionnalité agrégée de plusieurs HoCs.

Dans notre exemple, nous avons passé le nouveau comportement des HoCs `withSimpleState` et `withTransformProps` au composant de base `renderDisplayList`.

Comme vous venez de le voir, **les props sont le seul langage que les HoCs utilisent pour communiquer entre eux à l'intérieur d'une composition**. Chaque HoC effectue une action spécifique qui résulte en une amélioration ou une modification de l'objet props.

![Image](https://cdn-media-1.freecodecamp.org/images/WYe3UGjzTTBQqd-jPngl3i5fQeNOhFF2oMES)

#### Refactorisation

Bien que notre composition de HoC fonctionne, la syntaxe elle-même est assez verbeuse. Nous pouvons la simplifier en nous débarrassant de la variable `ToggleableFilteredList` et en enveloppant simplement les HoCs les uns dans les autres.

```
const FilteredList = withSimpleState('dark')(   withTransformProps(({ list, stateValue, stateHandler }) => {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   })(renderDisplayList))
```

Ce code est un peu meilleur. Cependant, nous enveloppons toujours manuellement tous les composants. Imaginez que vous vouliez ajouter encore plus de HoCs à cette composition. Dans un tel cas, notre composition deviendra difficile à lire et à comprendre. Imaginez simplement toutes ces parenthèses !

#### Utilisation de compose

Puisque cette discussion porte sur les principes de la programmation fonctionnelle, utilisons l'assistant `compose`.

```
const compose = (...hocs) => BaseComponent =>   hocs.reduceRight((acc, hoc) => hoc(acc)      , BaseComponent)
```

```
const enhance = compose(   withSimpleState('dark'),   withTransformProps(({ list, stateValue, stateHandler }) => {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }))
```

```
const FilteredList = enhance(renderDisplayList)
```

Nous n'avons plus besoin d'envelopper explicitement les HoCs les uns dans les autres. Au lieu de cela, nous les passons tous en tant qu'arguments à la fonction `compose`. Lorsque nous faisons cela, nous obtenons une nouvelle fonction composée attendant que l'argument `BaseComponent` soit passé. Nous stockons cette fonction sous `enhance`. Ensuite, nous passons simplement `renderDisplayList` en tant que composant de base, et `compose` fera tout l'enveloppement des composants pour nous.

#### Pancakes encore

J'aimerais revenir à notre **analogie des pancakes**. Auparavant, nous décorions nos pancakes avec une seule couche savoureuse. Mais comme nous le savons tous, les pancakes ont beaucoup meilleur goût lorsque vous combinez plusieurs saveurs ensemble. Comment un pancake avec du chocolat fondu et de la banane ou avec de la crème et du caramel ? Vous savez de quoi je parle...

Tout comme vous pouvez décorer votre pancake en utilisant une ou plusieurs couches de décoration selon vos goûts, vous pouvez décorer votre composant de présentation avec un ou plusieurs HoCs pour obtenir la combinaison de logique que vous voulez pour votre cas d'utilisation particulier.

![Image](https://cdn-media-1.freecodecamp.org/images/2kpZubt4-blpyzuNxiiuNYSJlTqG914ojayU)

Si vous avez besoin d'une logique complexe pour votre composant de présentation, vous n'avez pas besoin de tout stocker à l'intérieur d'un seul composant ou dans un seul HoC. Au lieu de cela, vous composez simplement plusieurs HoCs simples ensemble et améliorez votre composant de présentation avec eux.

### Recompose

Jusqu'à présent, vous avez vu quelques HoCs simples. Cependant, ce modèle est si puissant qu'il a été utilisé dans de nombreuses bibliothèques basées sur React (comme React-Redux, React router, Recompose).

J'aimerais parler davantage de la [bibliothèque Recompose](https://github.com/acdlite/recompose), qui nous fournit des dizaines de HoCs. Elle utilise des HoCs pour tout, de l'état et du cycle de vie à la gestion conditionnelle et à la manipulation des props.

Réécrivons notre exemple de composition de HoC en utilisant les HoCs prédéfinis de Recompose.

```
import { withState, mapProps, compose } from 'recompose';
```

```
const enhance = compose(   withState('stateValue', 'stateHandler', 'dark'),   mapProps(({ list, stateValue, stateHandler }) => {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }),)
```

```
const FilteredList = enhance(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Nos deux HoCs personnalisés `withSimpleState` et `withTransformProps` sont déjà prédéfinis dans Recompose sous les noms `withState` et `mapProps`. De plus, la bibliothèque nous fournit également une fonction `compose` prédéfinie. Il est donc vraiment facile d'utiliser ces implémentations existantes, plutôt que de définir les nôtres.

La version Recompose de la composition de HoC n'est pas si différente de la nôtre. Seule la HoC `withState` est maintenant plus réutilisable puisqu'elle prend trois arguments, où vous pouvez définir la valeur par défaut de l'état, le nom de l'état et le nom de son gestionnaire. `mapProps` fonctionne de la même manière que notre implémentation. Nous devons simplement passer la fonction de configuration.

En conséquence, nous n'avons pas besoin de définir des HoCs qui nous fournissent un comportement général.

#### Plus d'améliorations

Nous pouvons améliorer notre composition en utilisant Recompose encore plus puisque nous n'avons pas encore abordé un problème.

```
const renderDisplayList = ({ list, stateHandler, otherSide }) => (   <div>      <button onClick={() => stateHandler(otherSide)}>Switch</button>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

Si nous vérifions à nouveau le composant `renderDisplayList`, nous pouvons voir que sa fonction de gestionnaire de clic est recréée chaque fois que le composant est réaffiché. Et nous voulons éviter toute recréation inutile car cela pourrait nuire à la performance de notre application. Heureusement, nous pouvons ajouter le HoC `withHandlers` à notre composition pour résoudre ce problème.

```
import { withState, mapProps, withHandlers, compose } from 'recompose';
```

```
const renderDisplayList = ({ list, handleSetState }) => (   <div>      <button onClick={handleSetState}>Switch</button>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

```
const enhance = compose(   withState('stateValue', 'stateHandler', 'dark'),   mapProps(({ list, stateValue, stateHandler }) => {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }),   withHandlers({      handleSetState: ({ stateHandler, otherSide }) => () => stateHandler(otherSide)   }))
```

```
const FilteredList = enhance(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Le HoC `withHandlers` prend un objet de fonctions comme argument de configuration. Dans notre exemple, nous passons un objet avec une seule fonction `handleSetState`. Lorsque cela se produit, nous obtenons un HoC attendant que le composant de base et les props soient passés. Lorsque nous les passons, la fonction externe dans chaque clé de l'objet passé reçoit l'objet props comme argument.

Dans notre cas, la fonction `handleSetState` reçoit les props `stateHandler` et `otherSide`. Nous obtenons une nouvelle fonction qui est ensuite injectée dans les props et est transmise au composant `renderDisplayList`.

Le `handleSetState` est ensuite attaché au bouton de manière à ne pas nécessiter sa recréation lors de chaque réaffichage du composant, car `withHandlers` s'assure que l'identité de ses gestionnaires est préservée à travers les rendus. En conséquence, les gestionnaires sont recréés **uniquement** lorsque les props passés à `withHandlers` changent.

Bien sûr, la recréation possible de notre simple fonction de gestionnaire de clic n'entrave pas beaucoup la performance. `withHandlers` est beaucoup plus utile lorsque vous devez optimiser un nombre plus élevé de gestionnaires complexes.

Cela signifie également que c'est un bon endroit pour stocker tous les gestionnaires utilisés à l'intérieur de votre composant de présentation. De cette façon, il est immédiatement évident pour quiconque regarde votre composant, quels gestionnaires sont utilisés à l'intérieur. En conséquence, il est assez simple pour un développeur d'ajouter ou de supprimer un gestionnaire particulier. C'est beaucoup mieux que de rechercher manuellement tous les gestionnaires à l'intérieur d'un composant.

En nous fournissant de nombreux HoCs réutilisables, Recompose facilite la composition de HoC et l'utilisation des HoCs en général, puisque nous n'avons pas besoin d'écrire tous les HoCs nous-mêmes.

Dans les applications réelles, vous utiliserez souvent ces HoCs prédéfinis puisqu'ils couvrent la plupart des cas d'utilisation typiques. Et dans le cas où vous avez besoin d'une logique spécifique qui doit être partagée entre plusieurs composants, vous définirez vous-même un HoC.

![Image](https://cdn-media-1.freecodecamp.org/images/NR5prIzyMKBd0LMf14ciCMvy0mIcfKpvRhKh)

### Conclusion

Grâce aux principes de la programmation fonctionnelle, nous avons pu transformer ce composant énorme et non réutilisable du début...

```
class FilteredList extends React.Component {   constructor(props) {      super(props)      this.state = { value: this.props.defaultState }   }   updateState(value) {      this.setState({ value })   }   render() {      const otherSide = this.state.value === 'dark' ? 'light' : 'dark'      const transformedProps = this.props.list.filter(char => char.side === this.state.value)      return (         <div>            <button onClick={() => this.updateState(otherSide)}>Switch</button>            {transformedProps.map(char =>               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render (   <FilteredList defaultState='dark' list={starWarsChars} />,   document.getElementById('app'))
```

...en cette composition de composants réutilisables, lisibles et maintenables.

```
import { withState, mapProps, withHandlers, compose } from 'recompose';
```

```
const renderDisplayList = ({ list, handleSetState }) => (   <div>      <button onClick={handleSetState}>Switch</button>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

```
const enhance = compose(   withState('stateValue', 'stateHandler', 'dark'),   mapProps(({ list, stateValue, stateHandler }) => {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }),   withHandlers({      handleSetState: ({ stateHandler, otherSide }) => () => stateHandler(otherSide)   }))
```

```
const FilteredList = enhance(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Nous utilisons ces principes lors du développement d'applications assez souvent. Notre objectif est d'utiliser des composants simples et réutilisables autant que possible. Le modèle HoC nous aide à y parvenir puisque son idée est de déplacer la logique vers le HoC et de laisser le composant fonctionnel de présentation s'occuper du rendu de l'UI. En conséquence, nous n'avons plus besoin d'utiliser des classes pour nos composants de présentation, seulement pour les HoCs si nous avons besoin d'un comportement spécifique à la classe.

En conséquence, notre application est composée d'un ensemble de composants de présentation que nous pouvons réutiliser dans toute notre application, et nous pouvons les améliorer en utilisant un ou plusieurs HoCs réutilisables pour obtenir la logique dont nous avons besoin pour un scénario particulier (comme un HoC dédié à la récupération de données).

Une caractéristique intéressante de notre approche est que, si vous regardez une composition de HoC particulière, vous savez immédiatement quel type de logique elle utilise. Vous devez simplement vérifier la fonction `compose` où vous pouvez voir toute la logique contenue dans les HoCs. Si vous décidez d'ajouter plus de logique, vous insérez simplement un nouveau HoC dans la fonction `compose`. De plus, si vous vouliez voir quels gestionnaires le composant utilise, vous devez simplement vérifier le HoC `withHandlers`.

Une autre chose intéressante à propos des HoCs est qu'ils ne sont pas liés à React. Cela signifie que vous pouvez les utiliser dans vos autres applications qui n'ont pas été écrites en React.

![Image](https://cdn-media-1.freecodecamp.org/images/1AAlmR3SlqLaDv3vQYJuqayzeRcdOlZi7Sn4)

Félicitations ! Vous avez réussi.

Si vous avez aimé cet article, donnez-lui quelques applaudissements. Je l'apprécierais grandement et plus de gens pourront voir cet article également.

Cet article a été [publié à l'origine sur mon blog](https://www.codinglawyer.io/).

Si vous avez des questions, des critiques, des observations ou des conseils pour l'amélioration, n'hésitez pas à écrire un commentaire ci-dessous ou à me contacter via [Twitter](https://twitter.com/coding_lawyer).

[**David Kopal (@coding_lawyer) | Twitter**](https://twitter.com/coding_lawyer)  
[_Les derniers Tweets de David Kopal (@coding_lawyer). programmeur passionné, conférencier, ancien avocat, aime apprendre de nouvelles choses..._twitter.com](https://twitter.com/coding_lawyer)