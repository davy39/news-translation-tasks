---
title: Erreurs courantes commises par les développeurs React – et comment les corriger
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-05-03T16:40:08.000Z'
originalURL: https://freecodecamp.org/news/common-mistakes-react-developers-make-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/christin-hume-mfB1B1s4sMc-unsplash-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Erreurs courantes commises par les développeurs React – et comment les
  corriger
seo_desc: 'In this article, we''ll see some of the common mistakes that React developers
  make, and how you can avoid them.

  So let''s get started.

  Don''t Forget that Every Route Change Mounts and Unmounts a Component

  Whenever you''re using routing in a React applica...'
---

Dans cet article, nous verrons certaines des erreurs courantes que commettent les développeurs React, et comment vous pouvez les éviter.

Alors, commençons.

## N'oubliez pas que chaque changement de route monte et démonte un composant

Chaque fois que vous utilisez le routage dans une application React, vous déclarez des routes à l'intérieur du composant `Switch`. Cela signifie qu'un seul composant avec la route correspondante est affiché à la fois.

Par conséquent, chaque fois que vous passez d'une route à une autre, le composant précédemment affiché est démonté et le composant avec la nouvelle route correspondante est monté.

Si vous avez besoin de faire persister certaines données lors d'un changement de route, vous devez les déclarer dans le composant qui encapsule les routes. Il peut s'agir du composant `App` dans le Code Sandbox suivant, ou d'un autre moyen de persister des données comme l'utilisation du [local storage ou du session storage](https://javascript.plainenglish.io/everything-you-need-to-know-about-html5-local-storage-and-session-storage-479c63415c0a?source=friends_link&sk=f429aa5008683a3b0359db43f976efb3)

%[https://codesandbox.io/s/hopeful-faraday-hqz9x?file=/src/App.js]

Comme vous pouvez le voir dans le Code Sandbox ci-dessus, chaque fois que nous changeons de route en cliquant sur les liens, le `console.log` correspondant s'affiche sur la console. Cela indique que le composant précédent est démonté et qu'un nouveau composant est monté.

## N'utilisez pas la mauvaise syntaxe setState

Chaque fois que vous déclarez un état à l'intérieur d'un composant basé sur une classe, il s'agit toujours d'un objet comme ceci :

```js
this.state = {
 counter: 0
}

```

Ainsi, chaque fois que vous utilisez la forme de mise à jour de la syntaxe setState pour mettre à jour l'état, cela ressemble à ceci :

```js
this.setState((prevState) => {
  return {
    counter: prevState.counter + 1
  };
});

```

Puisque l'état est un objet, `prevState` est également un objet – vous accédez donc au `counter` en utilisant `prevState.counter`.

Mais lorsque vous utilisez des composants fonctionnels avec les React Hooks, l'état peut être un objet ou une valeur non-objet comme indiqué ci-dessous :

```js
const [counter, setCounter] = useState(0);

```

Ici, la valeur de `counter` n'est pas un objet mais un nombre. Donc, pour mettre à jour l'état en utilisant la syntaxe de mise à jour, vous écrirez le code comme ceci :

```js
setCounter((prevCounter) => prevCounter + 1);

```

Ici, le `prevCounter` est un nombre. Vous n'utilisez donc pas `prevCounter.counter` – juste `prevCounter`. Ou vous pouvez le simplifier comme indiqué ci-dessous :

```js
setCounter((counter) => counter + 1);

```

> Consultez [mon article ici](https://www.freecodecamp.org/news/what-is-state-in-react-explained-with-examples/) pour une introduction complète à l'état (state) dans React.

## N'appelez pas de Hooks depuis des composants de classe

À partir de la version 16.8.0, React a introduit les Hooks. Ils vous permettent d'écrire un meilleur code React et d'utiliser l'état et les méthodes de cycle de vie des composants à l'intérieur des composants fonctionnels.

> Consultez [mon article ici](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) pour une introduction aux React hooks.

Pour faciliter le codage, React fournit de nombreux hooks comme :

* Le hook `useParams` pour accéder aux paramètres d'URL lors de l'utilisation du routage React
* Le hook `useHistory` pour accéder à l'API d'historique à l'intérieur de n'importe quel composant
* Le hook `useRef` pour accéder à l'élément DOM

et bien d'autres hooks.

Mais tous ces hooks (qui commencent généralement par le mot-clé `use`) ne fonctionnent qu'à l'intérieur des composants fonctionnels.

Si vous avez un composant basé sur une classe, vous ne pouvez pas utiliser ces hooks. Vous devez refactoriser votre code pour le convertir en composants fonctionnels. Si vous ne le faites pas, vous pourriez obtenir une erreur comme celle de la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/hook_error.png)

## N'oubliez pas d'ajouter une prop Key lors de l'utilisation de la méthode Array `map` 

Jetez un œil à [cette démo Code Sandbox](https://codesandbox.io/s/quirky-shockley-bjd6z?file=/src/index.js).

Ici, pour afficher une liste d'éléments, vous pouvez utiliser le code suivant :

```js
const Items = ({ items }) => (
  <ol>
    {items.map((item) => (
      <Item item={item} />
    ))}
  </ol>
);

```

Dans React, vous utiliserez généralement la méthode `map` de l'array pour afficher une liste d'éléments stockés dans un tableau.

Mais dès que vous ajoutez un élément à la liste dans le Code Sandbox ci-dessus, vous verrez un avertissement de clé manquante s'afficher dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/missing-key.gif)

C'est parce que chaque fois que vous utilisez la méthode `map` de l'array pour boucler sur les éléments, vous devez fournir une prop `key` unique. React utilise cela pour identifier quels éléments à l'écran doivent être re-rendus, donc l'ajout de la prop `key` vous aide à éviter les re-rendus inutiles dans votre application.

Voici une [démo Code Sandbox mise à jour](https://codesandbox.io/s/boring-greider-olko7?file=/src/index.js) avec la prop `key` ajoutée.

Ici, j'ai fourni une prop `key` unique à chaque élément sur lequel nous bouclons comme ceci :

```js
<Item item={item} key={index} />

```

Maintenant, si vous essayez d'ajouter des éléments, vous n'aurez aucun avertissement dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/added-key.gif)

> Remarque : Dans le code ci-dessus, comme les éléments ne sont pas réordonnés ou supprimés, l'utilisation de `index` comme `key` fonctionne bien. Mais si vous supprimez ou modifiez l'ordre des éléments affichés, vous devez alors fournir une clé unique au lieu d'utiliser `index`.

## N'utilisez pas les fonctions inline de la mauvaise manière

Jetez un œil à [cette démo Code Sandbox](https://codesandbox.io/s/stupefied-breeze-66nyr?file=/src/index.js).

Ici, j'ai ajouté quelques éléments à l'état :

```js
const [items, setItems] = useState(["one", "two"]);

```

et nous bouclons sur eux pour les afficher à l'écran :

```jsx
{items.map((item, index) => (
  <li key={index}>
    {item} <button onClick={handleRemoveItem(item)}>Remove</button>
  </li>
))}

```

Si vous vérifiez l'application, vous verrez qu'aucun élément n'est affiché à l'écran. L'ajout de nouveaux éléments ne fonctionne pas non plus comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/wrong_inline.gif)

C'est à cause du gestionnaire `onClick` pour le bouton :

```jsx
<button onClick={handleRemoveItem(item)}>Remove</button>

```

Ici, nous appelons la méthode `handleRemoveItem` lorsque l'utilisateur clique sur le bouton – mais la façon dont nous appelons la méthode est incorrecte.

Donc, si vous n'avez pas besoin de passer de paramètres, vous utilisez la syntaxe suivante :

```jsx
<button onClick={handleRemoveItem}>Remove</button>

```

Mais plus tard, si vous décidez de passer un paramètre à la fonction, vous devez appeler le gestionnaire à l'intérieur de la fonction inline comme ceci :

```jsx
<button onClick={() => handleRemoveItem(item)}>Remove</button>

```

La plupart des développeurs React oublient d'ajouter une fonction inline et il faut ensuite des heures de débogage pour comprendre pourquoi quelque chose ne fonctionne pas.

Voici une [démo Code Sandbox fonctionnelle mise à jour](https://codesandbox.io/s/polished-moon-02iug?file=/src/index.js).

### **Merci de m'avoir lu !**

Depuis ES6, il y a de nombreux ajouts utiles à JavaScript comme :

* La déstructuration ES6
* La syntaxe d'importation et d'exportation
* Les fonctions fléchées
* Les promesses
* Async/await
* L'opérateur d'enchaînement optionnel et bien plus encore.

**Vous pouvez tout apprendre sur toutes les fonctionnalités d'ES6+ en détail dans mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/).**

> Consultez le contenu de l'aperçu gratuit du livre [ici](https://www.freecodecamp.org/news/learn-modern-javascript/).

De plus, vous pouvez consulter mon cours **gratuit** [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>