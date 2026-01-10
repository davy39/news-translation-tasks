---
title: Les fondamentaux de React – JSX, composants et props expliqués
subtitle: ''
author: Tanishka Makode
co_authors: []
series: null
date: '2023-04-07T16:32:00.000Z'
originalURL: https://freecodecamp.org/news/react-fundamentals
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Blog-1-Cover--2-.png
tags:
- name: React
  slug: react
seo_title: Les fondamentaux de React – JSX, composants et props expliqués
seo_desc: 'React is a popular JavaScript library for building user interfaces. And
  in order to create complex and efficient web applications, you''ll need to understand
  its fundamental concepts.

  In this tutorial, we will be covering three essential concepts of R...'
---

React est une bibliothèque JavaScript populaire pour construire des interfaces utilisateur. Et afin de créer des applications web complexes et efficaces, vous devez comprendre ses concepts fondamentaux.

Dans ce tutoriel, nous allons couvrir trois concepts essentiels de React – JSX, composants et props.

Pour commencer, vous devriez être familiarisé avec :

1. Les bases de JavaScript
   
2. La déstructuration des tableaux et des objets
   
3. Les modules ES6
   

Alors, si vous êtes nouveau dans React ou souhaitez vous rafraîchir les bases, continuez votre lecture.

Avant de commencer avec les concepts de React, apprenons un peu sur JSX – qui est ce que vous utilisez pour écrire du code React.

## Qu'est-ce que JSX ?

JSX signifie JavaScript XML. C'est une extension du langage JavaScript basée sur ES6. Il est traduit en JavaScript régulier à l'exécution.

JSX nous permet d'écrire du HTML dans React, ce qui rend le processus d'écriture de HTML dans vos applications React beaucoup plus facile.

### Pourquoi utiliser JSX ?

JSX n'est pas obligatoire. Il est totalement à vous de décider d'utiliser du HTML simple ou JSX. Mais les blocs de code que je vais partager ci-dessous clarifieront la différence entre le HTML simple et JSX et lequel est préférable.

```JavaScript
// HTML simple
const myElement = React.createElement('h1', { style:{color:"green"} }, 'Je n'utilise pas JSX !');

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(myElement);
```

```JavaScript
// JSX
const myElement = <h1>J'adore JSX !</h1>;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(myElement);
```

Comme vous pouvez le voir dans le premier exemple, l'utilisation de HTML simple rend la création d'éléments un peu plus difficile. Nous devons utiliser une méthode createElement, puis passer l'élément avec son style et sa valeur.

D'autre part, JSX facilite grandement les choses en utilisant simplement la balise de l'élément comme nous écrivons du HTML et en passant sa valeur.

En raison de ces avantages, je recommande fortement d'utiliser JSX.

### Règles JSX

Il y a quelques règles à garder à l'esprit lors de l'utilisation de JSX :

1. Un nom de composant React doit être en majuscule. Les noms de composants qui ne commencent pas par une majuscule sont traités comme des composants intégrés.
   
2. JSX vous permet de retourner un seul élément à partir d'un composant donné. Cela est connu comme un élément parent.
   

Si vous souhaitez retourner plusieurs éléments HTML, enveloppez-les simplement tous dans une seule `<div></div>`, `<React.fragments><React.fragments/>`, `<></>` ou toute balise sémantique.

```JavaScript
const App = () => {
  return
    <div>
      <h1>Bonjour le monde !</h1>
      <p>Tanishka ici !</p>
    </div>
}
```

Mais cela ne fonctionnera pas, car `return` serait interprété comme une instruction de retour simple. Pour éviter cela, vous devez encapsuler tout dans `( )`.

```JavaScript
const App = () => {
  return (
    <div>
      <h1>Bonjour le monde !</h1>
      <p>Tanishka ici !</p>
    </div>
  );
}
```

Maintenant, cela fonctionnera parfaitement !

3. Dans JSX, chaque balise, y compris les balises auto-fermantes, doit être fermée. Dans le cas des balises auto-fermantes, vous devez ajouter un slash à la fin (par exemple `<img/>`, `<hr/>`, et ainsi de suite).
   

```JavaScript
const App = () => {
  return (
    <>
      <img src="./assets/react.svg" alt="" />
    </>
  );
}
```

4. Puisque JSX est plus proche de JavaScript que de HTML, le DOM React utilise la convention de nommage camelCase pour les noms d'attributs HTML. Par exemple : `tabIndex`, `onChange`, et ainsi de suite.
   
5. "class" et "for" sont des mots réservés en JavaScript, donc utilisez "className" et "htmlFor" à la place, respectivement.
   

### Comment utiliser CSS dans JSX

Lors de l'utilisation de JavaScript, nous avons généralement un fichier HTML, un fichier CSS et un fichier JavaScript, n'est-ce pas ? Simple. Mais lors de l'utilisation de React, nous utilisons HTML (JSX) et JavaScript dans le même fichier.

Pour ajouter du style à nos composants, nous pouvons utiliser soit du CSS en ligne, soit du CSS externe.

Commençons par voir comment fonctionne le CSS en ligne dans React.

JSX représente des objets, c'est-à-dire des paires clé-valeur – comme un nom de propriété et sa valeur. Écrivez toujours la valeur dans `" "` comme nous le faisons dans les objets.

Ainsi, lorsque nous ajoutons des styles en ligne aux éléments JSX, nous devons ajouter { } pour la représentation de l'objet (les { } extérieurs sont la convention).

```JavaScript
const App = () => {
  return (
    <>
      <h1 style={ { color: "Red" } }>Bonjour le monde !</h1>
      <p style={ { fontSize: "20px" } }>Tanishka ici !</p>
    </>
  );
}
```

Ici, si vous regardez le style isolément, vous verrez qu'il ressemble à un objet :

```JavaScript
{
    color: "Red"
}
```

En gros, utilisez { } pour ajouter des styles, utilisez des paires clé-valeur et écrivez toujours la valeur dans " ".

Maintenant, voyons comment utiliser un fichier CSS externe.

Nous créons simplement un fichier .css et l'importons dans notre fichier .jsx comme ceci :

```JavaScript
import './style.css'

/* 
    Votre code ici
*/
```

### Comment utiliser JS dans JSX

Nous pourrions avoir besoin d'utiliser du JavaScript simple pour ajouter de la logique à la programmation du rendu des composants. Et pour ajouter du code JavaScript simple dans JSX, nous devons l'écrire à l'intérieur d'accolades.

Cependant, tout ce que nous écrivons à l'intérieur des accolades doit être une expression. Les instructions ne sont pas autorisées.

```JavaScript
const App = () => {
  return (
    <>
      <h1>Mon nom est {const name = "Tanishka"}</h1>
    </>
  );
}
```

Le code ci-dessus est invalide.

Maintenant, vous pourriez penser que `{const name = "Tanishka"}` est aussi du JavaScript. Comment ce bloc de code n'est-il pas valide ? Parce qu'il s'agit d'une initialisation de `name` qui est une instruction et nous ne pouvons pas écrire d'instructions à l'intérieur des accolades.

Nous pouvons apporter quelques modifications au bloc de code ci-dessus et il sera valide :

```JavaScript
const App = () => {
  return (
  const name = "Tanishka";
    <>
      <h1>Mon nom est {name}</h1>
    </>
  );
}
```

Nous avons initialisé la valeur de `name` en dehors du bloc return et avons simplement utilisé la variable incluse `name` à l'intérieur des accolades, où name a la valeur assignée de `"Tanishka"`. Donc maintenant c'est une expression et c'est valide.

Maintenant que nous savons comment écrire du code dans React, apprenons ce qu'il faut écrire – c'est-à-dire, les concepts de base de React.

## Qu'est-ce que les composants dans React ?

Les composants sont des blocs de code indépendants et réutilisables qui fonctionnent de manière isolée. Le principal avantage des composants est qu'ils aident à réduire la redondance.

Vous pouvez penser à un composant comme à une brique Lego. Lorsque vous construisez un site web, vous assemblez de nombreuses briques pour créer le tout.

![Img1-1](https://www.freecodecamp.org/news/content/images/2023/03/Img1-1.png align="left")

Nous pouvons classer les composants en deux types : les composants de classe et les composants fonctionnels. Je ne vais pas entrer dans les détails ici, car c'est un sujet pour un autre tutoriel.

Sachez simplement que les inconvénients de l'utilisation des composants de classe sont qu'ils viennent avec un tas de choses préchargées à l'intérieur, que vous le vouliez ou non. Cela les rend un peu plus difficiles à gérer.

L'équipe React recommande que les nouvelles applications soient construites avec des composants fonctionnels et des hooks. Donc, vous devriez vraiment envisager l'approche des composants fonctionnels lorsque vous travaillez sur un nouveau projet React. C'est donc ce sur quoi nous allons nous concentrer ici.

### Comment créer un composant fonctionnel dans React

```JavaScript
function Greet() {
  return <h1>Bonjour le monde !</h1>;
}
```

OU

```JavaScript
const Greet = () => <h1>Bonjour le monde !</h1>
```

Attendez, mais ne sont-ce pas simplement des fonctions JavaScript ? OUI ! Les composants sont essentiellement des fonctions JavaScript qui retournent un seul élément HTML. Par convention, les fonctions fléchées sont largement utilisées.

Et quelles sont ces balises qui ont l'air étranges ? Cela s'appelle JSX, que vous apprendrez davantage dans un instant.

### Comment imbriquer des composants dans React

Dans React, nous pouvons imbriquer des composants les uns dans les autres. Cela aide à créer des interfaces utilisateur plus complexes. Cela aide également à se débarrasser du code redondant. Les composants qui sont imbriqués dans les composants parents sont appelés composants enfants.

Par exemple :

```JavaScript
const Book = () => {
  return (
    <div>
      <h1>Nom du livre : Cracking The Coding Interview</h1>
      <h2>Auteur : Gayle Laakmann McDowell</h2>
    </div>
  );
};
```

Ici, nous avons créé un composant Book. Que faire si nous voulons créer plusieurs instances de ce composant livre ? C'est à ce moment-là que nous pouvons utiliser des composants imbriqués.

```JavaScript
const BookList = () => {
  return (
    <div>
      <Book />
      <Book />
    </div>
  );
};

const Book = () => {
  return (
    <div>
      <h1>Nom du livre : Cracking The Coding Interview</h1>
      <h2>Auteur : Gayle Laakmann McDowell</h2>
    </div>
  );
};
```

Dans le bloc de code ci-dessus, nous avons créé deux composants, Book et BookList. `Book` retourne une div qui contient `Nom du livre` et `nom de l'auteur` tandis que `BookList` retourne une div qui contient deux `Book`.

De cette manière, l'imbrication nous aide à créer plusieurs instances d'un composant pour créer des interfaces utilisateur complexes facilement.

## Comment fonctionnent les Props dans React

Props signifie propriétés. Les props sont comme des arguments de fonction, et vous les envoyez dans le composant comme des attributs.

Lorsque nous voulons créer plusieurs instances d'un seul composant avec diverses valeurs différentes, nous devons utiliser des props.

Prenons notre exemple précédent de Book et BookList :

Par exemple :

```JavaScript
const BookList = () => {
  return (
    <div>
      <Book />
      <Book />
    </div>
  );
};

const Book = () => {
  return (
    <div>
      <h1>Nom du livre : Cracking The Coding Interview</h1>
      <h2>Auteur : Gayle Laakmann McDowell</h2>
    </div>
  );
};
```

Dans ce bloc de code, nous avons codé en dur les valeurs du nom du livre et de l'auteur, mais ce n'est pas vraiment utile pour d'autres livres.

Nous pouvons penser à un composant comme à une fonction et aux props comme aux arguments de cette fonction. Nous fournissons simplement des valeurs spécifiques pour chaque composant et utilisons ces valeurs dans le corps du composant.

Commençons par voir comment passer des props :

```JavaScript
const BookList = () => {
  return (
    <div>
      <Book bookName = "Cracking The Coding Interview"
      author = "Gayle Laakmann McDowell"/>
      <Book bookName = "The Road to Learn React"
      author = "Robert Wieruch"/>
    </div>
  );
};
```

Ici, nous avons simplement créé des structures de type variable (bookName, author) et leur avons assigné leurs valeurs respectives. C'est tout ! Ce sont des props.

Maintenant, voyons comment nous pouvons y accéder, c'est-à-dire les utiliser dans le corps du composant :

```JavaScript
const Book = (props) => {
  return (
    <div>
      <h1>Nom du livre : {props.bookName}</h1>
      <h2>Auteur : {props.author}</h2>
    </div>
  );
};
```

Tout d'abord, nous devons utiliser le mot-clé `'props'` dans le paramètre d'une fonction fléchée qui agira comme un objet. Maintenant, nous pouvons accéder aux valeurs des props comme nous accédons aux valeurs des objets – `object.property`.

C'est pourquoi nous avons utilisé `'props.bookName'` et `'props.author'`. Chaque livre obtiendra sa valeur respective en faisant cela, créant ainsi parfaitement plusieurs instances du composant livre.

Vous pouvez utiliser les props comme ceci, mais il y a une autre façon d'accéder aux props. Pour cette méthode, vous devez être familiarisé avec le concept de déstructuration, c'est-à-dire accéder à chaque élément d'un objet.

```JavaScript
const Book = (props) => {
  const {bookName, author} = props;
  return (
    <div>
      <h1>Nom du livre : {bookName}</h1>
      <h2>Auteur : {author}</h2>
    </div>
  );
};
```

Nous avons déstructuré `'bookName'` et `'author'` et nous les avons utilisés comme variables au lieu de `'props.bookName'` et `'props.author'`.

Nous aurions pu déstructurer directement les props dans la section des paramètres. Cela aurait ressembler à ceci :

```JavaScript
const Book = ({bookName, author}) => {
  return (
    <div>
      <h1>Nom du livre : {bookName}</h1>
      <h2>Auteur : {author}</h2>
    </div>
  );
}
```

Cela fonctionne de la même manière que la méthode précédente, mais nous déstructurons simplement le contenu des props dans la section des paramètres au lieu de le faire par des déclarations.

### Children props

Parfois, nous pouvons rencontrer des situations dans lesquelles nous devons ajouter un élément spécifique à une instance particulière d'un composant uniquement. Nous passons l'élément spécifique entre les balises d'ouverture et de fermeture du composant. Dans ces cas, nous utilisons les children props.

```JavaScript
const BookList = () => {
  return (
    <div>
      <Book bookName = "Cracking The Coding Interview"
      author = "Gayle Laakmann McDowell">
          <button> Lire maintenant ! <button/>
      < Book />
      <Book bookName = "The Road to Learn React"
      author = "Robert Wieruch"/>
    </div>
  );
}
```

Dans le bloc de code ci-dessus, nous voulons afficher un bouton uniquement pour la première instance de livre. C'est pourquoi nous avons utilisé un composant enfant en passant le bouton entre les balises d'ouverture et de fermeture.

Voyons comment y accéder :

```JavaScript
const Book = ({bookName, author, children}) => {
  return (
    <div>
      <h1>Nom du livre : {bookName}</h1>
      <h2>Auteur : {author}</h2>
      {children}
    </div>
  );
}
```

Nous avons simplement ajouté `'children'` dans la section des paramètres et utilisé `'{children}'` dans les composants où nous voulons placer les child props. Dans ce cas, je voulais placer ce bouton sous les informations, donc j'ai utilisé `'{children}'` après `'bookName'` et `'author'`.

Cela place un child prop entre les balises d'ouverture et de fermeture uniquement lorsqu'il est spécifié. Cela sert notre objectif.

Lorsque nous voulons qu'un élément soit présent uniquement pour une seule instance du composant, nous pouvons utiliser les children props entre les balises du composant. Ensuite, nous pouvons soit utiliser `props.children`, soit le déstructurer et l'utiliser directement.

Permettez-moi de vous montrer à quoi cela ressemblera :

![ChildrenProps](https://www.freecodecamp.org/news/content/images/2023/03/ChildrenProps.png align="left")

Comme vous pouvez le voir, seule la première instance a obtenu le bouton sous ses informations. C'est ainsi que les children props sont utiles.

### Key Props

Une clé est un attribut spécial que vous devez inclure lors de la création de listes d'éléments dans React. Nous utilisons des clés pour donner une identité aux éléments dans les listes. Nous devons spécifier un id ou une valeur unique à chaque instance d'un composant pour suivre leur ajout ou suppression.

Lorsque vous choisissez une clé pour les éléments dans les listes, essayez d'utiliser un id unique pour chaque instance. Si un id n'est pas fourni ou pour une raison quelconque vous ne pouvez pas utiliser l'id, nous pouvons utiliser l'index de la liste.

```JavaScript
const App = () => {
  const numbers = [1, 2, 3, 4, 5];
  return (
    <>
      {numbers.map((number) => {
        return <li>{number}</li>;
      })}
    </>
  );
}
```

![keyError](https://www.freecodecamp.org/news/content/images/2023/03/keyError.png align="left")

Dans le bloc de code ci-dessus, nous itérons simplement sur une liste de nombres. Tout fonctionne bien jusqu'à ce que nous ouvrions la console. Elle est pleine de texte rouge - un avertissement qui dit - `'Avertissement : Chaque enfant dans une liste doit avoir une prop "key" unique.'`

Dans ce cas, nous n'avons aucun id spécifié, donc nous pouvons utiliser l'index de la liste en accédant au deuxième argument de la fonction map, c'est-à-dire l'index.

```JavaScript
const App = () => {
  const numbers = [1, 2, 3, 4, 5];
  return (
    <>
      {numbers.map((number, index) => {
        return <li key={index}> {number} </li>;
      })}
    </>
  );
}
```

![keyNoError](https://www.freecodecamp.org/news/content/images/2023/03/keyNoError.png align="left")

Ce bloc de code fonctionne bien et tous les avertissements ont disparu maintenant.

---

## Conclusion

J'espère que ce tutoriel vous a été utile pour commencer votre voyage avec React. Bon codage ! 👩🏻 0200d💻 2728