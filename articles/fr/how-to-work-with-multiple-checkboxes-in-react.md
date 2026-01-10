---
title: Tutoriel React – Comment travailler avec plusieurs cases à cocher
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-05-13T18:17:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-multiple-checkboxes-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/checkbox_selection.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Tutoriel React – Comment travailler avec plusieurs cases à cocher
seo_desc: 'Handling multiple checkboxes in React is completely different from how
  you use regular HTML checkboxes.

  So in this article, we''ll see how to work with multiple checkboxes in React.

  You will learn:


  How to use a checkbox as a Controlled Input in React...'
---

La gestion de plusieurs cases à cocher dans React est totalement différente de l'utilisation des cases à cocher HTML classiques.

Ainsi, dans cet article, nous verrons comment travailler avec plusieurs cases à cocher dans React.

Vous apprendrez :

* Comment utiliser une case à cocher comme une Entrée Contrôlée (Controlled Input) dans React
* Comment utiliser les méthodes d'array map et reduce pour des calculs complexes
* Comment créer un tableau d'une longueur spécifique pré-rempli avec une valeur spécifique

et bien plus encore.

Cet article fait partie de mon cours [Mastering Redux](https://master-redux.yogeshchavan.dev/). Voici un [aperçu de l'application](https://www.youtube.com/watch?v=izSw74H08Bc) que nous allons construire dans le cours.

Alors, commençons.

## Comment travailler avec une seule case à cocher

Commençons par la fonctionnalité d'une seule case à cocher avant de passer aux cases à cocher multiples.

Dans cet article, j'utiliserai la syntaxe des React Hooks pour créer des composants. Si vous n'êtes pas familier avec les React Hooks, consultez mon article [Introduction to React Hooks](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54).

Jetez un œil au code ci-dessous :

```js
<div className="App">
  Select your pizza topping:
  <div className="topping">
    <input type="checkbox" id="topping" name="topping" value="Paneer" />Paneer
  </div>
</div>

```

Voici une [démo Code Sandbox](https://codesandbox.io/s/young-snow-lzplh?file=/src/App.js).

Dans le code ci-dessus, nous avons juste déclaré une seule case à cocher, ce qui est similaire à la façon dont nous déclarons une case à cocher HTML.

Ainsi, nous pouvons facilement cocher et décocher la case comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/check_uncheck-1.gif)

Mais pour afficher à l'écran si elle est cochée ou non, nous devons la convertir en Entrée Contrôlée (Controlled Input).

Dans React, une Entrée Contrôlée est gérée par l'état (state), de sorte que la valeur d'entrée ne peut être modifiée qu'en changeant l'état lié à cette entrée.

Jetez un œil au code ci-dessous :

```js
export default function App() {
  const [isChecked, setIsChecked] = useState(false);

  const handleOnChange = () => {
    setIsChecked(!isChecked);
  };

  return (
    <div className="App">
      Select your pizza topping:
      <div className="topping">
        <input
          type="checkbox"
          id="topping"
          name="topping"
          value="Paneer"
          checked={isChecked}
          onChange={handleOnChange}
        />
        Paneer
      </div>
      <div className="result">
        Above checkbox is {isChecked ? "checked" : "un-checked"}.
      </div>
    </div>
  );
}

```

Voici une [démo Code Sandbox](https://codesandbox.io/s/dazzling-oskar-qcil8?file=/src/App.js).

Dans le code ci-dessus, nous avons déclaré l'état `isChecked` dans le composant avec la valeur initiale `false` en utilisant le hook `useState` :

```js
const [isChecked, setIsChecked] = useState(false);

```

Ensuite, pour la case à cocher d'entrée, nous avons ajouté deux props supplémentaires `checked` et `onChange` comme ceci :

```js
<input
  ...
  checked={isChecked}
  onChange={handleOnChange}
/>

```

Chaque fois que nous cliquons sur la case à cocher, la fonction de gestion `handleOnChange` sera appelée, laquelle nous utilisons pour définir la valeur de l'état `isChecked`.

```js
const handleOnChange = () => {
  setIsChecked(!isChecked);
};

```

Ainsi, si la case est cochée, nous définissons la valeur `isChecked` sur `false`. Mais si la case est décochée, nous définissons la valeur sur `true` en utilisant `!isChecked`. Ensuite, nous passons cette valeur dans la case à cocher d'entrée pour la prop `checked`.

De cette façon, la case à cocher d'entrée devient une entrée contrôlée dont la valeur est gérée par l'état.

Notez que dans React, il est toujours recommandé d'utiliser des Entrées Contrôlées pour les champs de saisie, même si le code semble compliqué. Cela garantit que le changement d'entrée se produit uniquement à l'intérieur du gestionnaire `onChange`.

L'état de l'entrée ne sera modifié d'aucune autre manière et vous obtiendrez toujours la valeur correcte et mise à jour de l'état de l'entrée.

Ce n'est que dans de rares cas que vous pouvez utiliser React ref pour utiliser l'entrée de manière non contrôlée.

## Comment gérer plusieurs cases à cocher

Maintenant, voyons comment gérer plusieurs cases à cocher.

Jetez un œil à [cette démo Code Sandbox](https://codesandbox.io/s/mystifying-tu-xlpgb?file=/src/App.js).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/multiple_checkboxes-2.png)

Ici, nous affichons une liste de garnitures (toppings) et leur prix correspondant. En fonction des garnitures sélectionnées, nous devons afficher le montant total.

Précédemment, avec la case à cocher unique, nous n'avions que l'état `isChecked` et nous changions l'état de la case à cocher en fonction de cela.

Mais maintenant nous avons beaucoup de cases à cocher, il n'est donc pas pratique d'ajouter plusieurs appels `useState` pour chaque case.

Déclarons donc un tableau dans l'état indiquant l'état de chaque case à cocher.

Pour créer un tableau égal à la longueur du nombre de cases à cocher, nous pouvons utiliser la méthode `fill` de l'array comme ceci :

```js
const [checkedState, setCheckedState] = useState(
    new Array(toppings.length).fill(false)
);

```

Ici, nous avons déclaré un état avec une valeur initiale sous forme de tableau rempli de la valeur `false`.

Donc si nous avons 5 garnitures, le tableau d'état `checkedState` contiendra 5 valeurs `false` comme ceci :

```js
[false, false, false, false, false]

```

Et une fois que nous cochons/décochons la case, nous changerons le `false` correspondant en `true` et le `true` en `false`.

Voici une [démo Code Sandbox finale](https://codesandbox.io/s/wild-silence-b8k2j?file=/src/App.js).

Le code complet de `App.js` ressemble à ceci :

```js
import { useState } from "react";
import { toppings } from "./utils/toppings";
import "./styles.css";

const getFormattedPrice = (price) => `$${price.toFixed(2)}`;

export default function App() {
  const [checkedState, setCheckedState] = useState(
    new Array(toppings.length).fill(false)
  );

  const [total, setTotal] = useState(0);

  const handleOnChange = (position) => {
    const updatedCheckedState = checkedState.map((item, index) =>
      index === position ? !item : item
    );

    setCheckedState(updatedCheckedState);

    const totalPrice = updatedCheckedState.reduce(
      (sum, currentState, index) => {
        if (currentState === true) {
          return sum + toppings[index].price;
        }
        return sum;
      },
      0
    );

    setTotal(totalPrice);
  };

  return (
    <div className="App">
      <h3>Select Toppings</h3>
      <ul className="toppings-list">
        {toppings.map(({ name, price }, index) => {
          return (
            <li key={index}>
              <div className="toppings-list-item">
                <div className="left-section">
                  <input
                    type="checkbox"
                    id={`custom-checkbox-${index}`}
                    name={name}
                    value={name}
                    checked={checkedState[index]}
                    onChange={() => handleOnChange(index)}
                  />
                  <label htmlFor={`custom-checkbox-${index}`}>{name}</label>
                </div>
                <div className="right-section">{getFormattedPrice(price)}</div>
              </div>
            </li>
          );
        })}
        <li>
          <div className="toppings-list-item">
            <div className="left-section">Total:</div>
            <div className="right-section">{getFormattedPrice(total)}</div>
          </div>
        </li>
      </ul>
    </div>
  );
}

```

Comprenons ce que nous faisons ici.

Nous avons déclaré la case à cocher d'entrée comme indiqué ci-dessous :

```js
<input
  type="checkbox"
  id={`custom-checkbox-${index}`}
  name={name}
  value={name}
  checked={checkedState[index]}
  onChange={() => handleOnChange(index)}
/>

```

Ici, nous avons ajouté un attribut `checked` avec la valeur correspondante `true` ou `false` provenant de l'état `checkedState`. Ainsi, chaque case à cocher aura la valeur correcte de son état coché.

Nous avons également ajouté un gestionnaire `onChange` et nous passons l'index (`index`) de la case à cocher qui est cochée/décochée à la méthode `handleOnChange`.

La méthode de gestion `handleOnChange` ressemble à ceci :

```js
const handleOnChange = (position) => {
  const updatedCheckedState = checkedState.map((item, index) =>
    index === position ? !item : item
  );

  setCheckedState(updatedCheckedState);

  const totalPrice = updatedCheckedState.reduce(
    (sum, currentState, index) => {
      if (currentState === true) {
        return sum + toppings[index].price;
      }
      return sum;
    },
    0
  );

  setTotal(totalPrice);
};

```

Ici, nous bouclons d'abord sur le tableau `checkedState` en utilisant la méthode `map` de l'array. Si la valeur du paramètre `position` passé correspond à l'index (`index`) actuel, alors nous inversons sa valeur. Ensuite, si la valeur est `true`, elle sera convertie en `false` en utilisant `!item` et si la valeur est `false`, elle sera convertie en `true`.

Si l'index ne correspond pas au paramètre `position` fourni, nous n'inversons pas sa valeur mais nous retournons simplement la valeur telle quelle.

```js
const updatedCheckedState = checkedState.map((item, index) =>
  index === position ? !item : item
);

// le code ci-dessus est le même que le code ci-dessous

const updatedCheckedState = checkedState.map((item, index) => {
  if (index === position) {
    return !item;
  } else {
    return item;
  }
});

```

J'ai utilisé l'opérateur ternaire `?:` car il rend le code plus court, mais vous pouvez utiliser n'importe quelle méthode d'array.

Si vous n'êtes pas familier avec le fonctionnement des méthodes d'array comme `map` ou `reduce`, consultez [cet article](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/) que j'ai écrit.

Ensuite, nous définissons le tableau `checkedState` sur le tableau `updatedCheckedState`. C'est important car si vous ne mettez pas à jour l'état `checkedState` à l'intérieur du gestionnaire `handleOnChange`, vous ne pourrez pas cocher/décocher la case.

C'est parce que nous utilisons la valeur `checkedState` pour la case à cocher afin de déterminer si elle est cochée ou non (car c'est une entrée contrôlée comme indiqué ci-dessous) :

```js
<input
  type="checkbox"
  ...
  checked={checkedState[index]}
  onChange={() => handleOnChange(index)}
/>

```

Notez que nous avons créé une variable `updatedCheckedState` séparée et que nous passons cette variable à la fonction `setCheckedState`. Nous utilisons la méthode `reduce` sur `updatedCheckedState` et non sur le tableau `checkedState` original.

C'est parce que, par défaut, la fonction `setCheckedState` utilisée pour mettre à jour l'état est asynchrone.

Le simple fait d'appeler la fonction `setCheckedState` ne garantit pas que vous obtiendrez la valeur mise à jour du tableau `checkedState` à la ligne suivante.

Nous avons donc créé une variable séparée et l'avons utilisée dans la méthode `reduce`.

Vous pouvez lire [cet article](https://www.freecodecamp.org/news/what-is-state-in-react-explained-with-examples/) si vous n'êtes pas familier avec le fonctionnement de l'état dans React.

Ensuite, pour calculer le prix total, nous utilisons la méthode `reduce` de l'array :

```js
const totalPrice = updatedCheckedState.reduce(
  (sum, currentState, index) => {
    if (currentState === true) {
      return sum + toppings[index].price;
    }
    return sum;
  },
  0
);

```

La méthode `reduce` de l'array reçoit quatre paramètres, dont nous n'en utilisons que trois : `sum`, `currentState` et `index`. Vous pouvez utiliser des noms différents si vous le souhaitez car ce ne sont que des paramètres.

Nous passons également `0` comme valeur initiale, également connue sous le nom de valeur `accumulator` pour le paramètre `sum`.

Ensuite, à l'intérieur de la fonction reduce, nous vérifions si la valeur actuelle du tableau `checkedState` est `true` ou non.

Si c'est `true`, cela signifie que la case est cochée, nous ajoutons donc la valeur du prix correspondant en utilisant `sum + toppings[index].price`.

Si la valeur du tableau `checkedState` est `false`, nous n'ajoutons pas son prix mais retournons simplement la valeur précédente calculée de `sum`.

Ensuite, nous définissons cette valeur `totalPrice` dans l'état `total` en utilisant `setTotal(totalPrice)`.

De cette façon, nous sommes en mesure de calculer correctement le prix total pour les garnitures sélectionnées comme vous pouvez le voir ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/toppings-1.gif)

Voici un [lien d'aperçu](https://b8k2j.csb.app/) de la démo Code Sandbox ci-dessus pour essayer par vous-même.

### Merci de m'avoir lu !

La plupart des développeurs ont du mal à comprendre le fonctionnement de Redux. Mais chaque développeur React devrait savoir comment travailler avec Redux, car les projets industriels utilisent majoritairement Redux pour gérer des projets de plus grande envergure.

Ainsi, pour vous faciliter la tâche, j'ai lancé un cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

Dans ce cours, vous apprendrez Redux depuis le tout début et vous construirez également une [application de commande de nourriture](https://www.youtube.com/watch?v=izSw74H08Bc) complète à partir de zéro en utilisant Redux.

Cliquez sur l'image ci-dessous pour rejoindre le cours, profiter de l'offre de réduction à durée limitée et obtenir gratuitement mon livre populaire Mastering Modern JavaScript.

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>

**Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**