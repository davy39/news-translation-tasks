---
title: Comment créer un générateur d'ombre de boîte avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-19T20:21:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-box-shadow-generator-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Cover-Image-6.png
tags:
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer un générateur d'ombre de boîte avec React
seo_desc: "By David Uzondu\nCSS is a powerful language for styling web pages. But\
  \ when you're designing a website, things like box shadows can be particularly difficult\
  \ to get right. \nIn this guide, you will learn how to create your own box shadow\
  \ generator with..."
---

Par David Uzondu

CSS est un langage puissant pour styliser les pages web. Mais lors de la conception d'un site web, des éléments comme les ombres de boîte peuvent être particulièrement difficiles à obtenir correctement. 

Dans ce guide, vous apprendrez à créer votre propre générateur d'ombre de boîte avec React et Vite. Voici un [aperçu](https://shadowgen.vercel.app/) de ce que vous allez construire aujourd'hui. Commençons.

# Installation du projet

Pour installer les choses, vous aurez besoin des éléments suivants :

* Node.js installé sur votre ordinateur. (Si vous n'avez pas Node.js installé, vous pouvez l'obtenir sur le site officiel [Node.js](https://nodejs.org)). Node.js est livré avec un gestionnaire de paquets appelé NPM.
* Connaissance de HTML, CSS, JavaScript et React (vous n'avez pas besoin d'être un expert).

Si vous avez tous les éléments mentionnés ci-dessus installés sur votre ordinateur, alors vous pouvez procéder à l'installation :

* Sur votre terminal, exécutez `npm create vite@latest` ou `yarn add vite`. Cette commande vous aidera à échafauder un nouveau projet Vite.
* Lorsque la commande s'exécute, vous serez invité à nommer votre projet. Tapez le nom de votre projet et appuyez sur Entrée. Lorsque vous êtes invité à sélectionner un framework, sélectionnez "React" et définissez la variante comme "JavaScript".
* Maintenant, exécutez `cd <votre_nom_de_projet>`, en veillant à remplacer `<votre_nom_de_projet>` par le nom réel de votre projet. Ensuite, exécutez `npm i` ou `yarn`. Cela installera toutes les dépendances nécessaires dont votre projet a besoin.
* Après l'installation de vos dépendances, exécutez `npm i react-colorful`. [react-colorful](https://www.npmjs.com/package/react-colorful) est le package NPM que nous utiliserons dans ce projet pour rendre un sélecteur de couleur.
* Après l'installation de react-colorful, vous pouvez démarrer le serveur de développement en tapant `yarn dev` ou `npm run dev`.

## Structure du projet

Notre projet sera structuré de cette manière : un fichier CSS est utilisé pour styliser l'ensemble de l'application, et la disposition de l'application consistera en une grille avec trois colonnes.

La première colonne abritera nos 'contrôles'. C'est là que vivront tous les composants nécessaires pour générer l'ombre de la boîte. La colonne suivante sera utilisée pour prévisualiser l'ombre de la boîte actuellement générée. La dernière colonne contiendra notre sortie.

## Structure des dossiers

Une dernière chose que vous devez faire est de structurer votre dossier. Suivez les étapes décrites ci-dessous pour voir comment vous pouvez le faire.

* Ouvrez le projet dans VSCode (ou votre éditeur de texte préféré) et effacez le contenu des fichiers `Index.css` et `App.css`.
* Rendez-vous sur ce [dépôt Github du projet](https://github.com/daviduzondu/Shadowgen/blob/main/src/App.css), puis copiez et collez le contenu du fichier `App.css` dans votre propre fichier `App.css`.
* Modifiez le fichier `App.jsx` pour qu'il ressemble à ceci à la fin :

```jsx
import './App.css'

function App() {
  return (
    <div className="App">
      <Header />
      <div className='mainApp'>
        <Container />
      </div>
    </div>
  )
}
export default App

```

* Dans le dossier `src`, créez un dossier `components`. Dans le dossier `components`, créez quatre fichiers : `Header.jsx`, `Control.jsx`, `CodeOutput.jsx` et `Container.jsx`.  
Maintenant que votre dossier est organisé, vous pouvez passer à la partie suivante.

# Comment construire l'en-tête

Commençons par la partie 'la plus simple' de ce projet : l'en-tête. Pour construire l'en-tête, naviguez vers le fichier `Header.jsx` et créez un composant qui retourne une div avec le nom de classe "Header". Votre fichier devrait ressembler à ceci à la fin :

```jsx
import React from 'react'

function Header() {
    return (
        <div className='Header'>
            <div>SHADOWGEN</div>
        </div>
    )
}
export default Header

```

# Comment créer les contrôles

Les contrôles sont des composants que nous pouvons utiliser pour ajuster les paramètres de l'ombre de la boîte. Dans ce tutoriel, nous aurons six contrôles : 

* un contrôle pour contrôler la couleur 
* quatre contrôles qui contrôlent les valeurs `offsetX`, `offsetY`, `spread` et `blur` en `px`
* et le dernier contrôle sera une case à cocher qui vous permet de changer le style de l'ombre de la boîte en `inset` si elle est cochée.

En CSS, la syntaxe commune pour la propriété `box-shadow` est :

```css
box-shadow: offsetXpx offsetYpx blur* spread* inset* #330303f5*;

```

⚠️ **Notez** que les paramètres optionnels sont marqués d'un astérisque.

Dans le fichier `Control.jsx`, importez `HexAlphaColorPicker` du package `react-colorful`.

```jsx
import React from 'react'
import { HexAlphaColorPicker } from 'react-colorful'

```

Ensuite, créez un composant fonctionnel nommé `Control` et exportez-le par défaut. Votre composant fonctionnel devrait retourner une div parent. Le composant devrait accepter cinq props, à savoir : `label`, `type`, `onChangeHandler`, `value` et `children`.

```jsx
import React from 'react'
import { HexAlphaColorPicker } from 'react-colorful'
function Control({ label, type, onChangeHandler, value, children }) {
    return (
        <div className={`paneChild ${type}`}>
        </div>
    )
}
export default Control

```

## Comment créer l'étiquette pour chaque contrôle

![Image](https://www.freecodecamp.org/news/content/images/2023/04/label-value.png)
_La structure d'un contrôle d'exemple._

À l'intérieur de la div parent, créez une autre div avec la classe "label".

```jsx
<div className="label">

</div>

```

Dans cette div, créez un élément `label` et définissez l'attribut "for" sur la prop `label`. L'élément `label` devrait contenir la prop `label` :

```jsx
<div className="label">
    <label htmlFor={label}>{label}</label>
</div>

```

Ensuite, rendons conditionnellement une valeur, juste à côté de l'étiquette. Pour cela, nous devons vérifier si l'étiquette n'est pas 'Inset'. Si cette condition est remplie, nous rendons simplement un élément `span` qui contient la prop `value`. 

À la fin, le code devrait ressembler à ceci :

```jsx
<div className="label">
    <label htmlFor="{label}">{label}</label>     
    {label !== "Inset" && 
    <span className="value">{value}</span>}  
</div>

```

Maintenant, pour rendre conditionnellement un sélecteur de couleur ou un élément d'entrée, ajoutez les lignes de code suivantes :

```jsx
{
  type === 'color' ? <HexAlphaColorPicker color={value} onChange={onChangeHandler} /> :
  <input type={type} name={label} value={value} min={(label === 'Spread' || label === "Blur") ? 0 : -350} max={(label === 'Spread' || label === "Blur") ? 100 : 350} onChange={onChangeHandler} />
}

```

Ce code utilise une instruction conditionnelle pour rendre différents composants JSX en fonction de la valeur de la prop `type`. Si `type` est `'color'`, un `HexAlphaColorPicker` est rendu avec les props `color` et `onChange` passées.

Si `type` n'est pas `'color'`, un élément `input` est rendu avec les props `type`, `name`, `value`, `min`, `max`, et `onChange` passées. Les valeurs de `min` et `max` dépendent de la valeur de la prop `label`. Dans les deux cas, la fonction `onChangeHandler` est passée en tant que prop pour gérer les changements dans la valeur de l'entrée ou du sélecteur de couleur.

Maintenant, le code terminé devrait ressembler à ceci :

```jsx
import React from 'react'
import { HexAlphaColorPicker, HexColorInput } from 'react-colorful'
function Control({ label, type, onChangeHandler, value }) {
    return (
        <div className={`paneChild ${type}`}>
            <div className='label'>
                <label htmlFor={label}>{label}</label>
                {label !== "Inset"
                    &&
                    <span className='value'>{value}</span>}
            </div>
            {
                type === 'color' ? <HexAlphaColorPicker color={value} onChange={onChangeHandler} />
                    :
                    <input type={type} name={label} value={value} min={(label === 'Spread' || label === "Blur") ? 0 : -350} max={(label === 'Spread' || label === "Blur") ? 100 : 350} onChange={onChangeHandler} />
            }
        </div>
    )
}
export default Control

```

# Comment créer le composant de sortie

Maintenant que vous avez créé le composant `Control`, rendez-vous dans le fichier `CodeOutput.jsx` et ajoutez les lignes de code suivantes :

```jsx
import React from 'react'
function CodeOutput({ shadow }) {
    return (
        <div className='paneChild'>
            <div className='label'>
                <span>Sortie CSS</span>
            </div>
            <div className='codeOutput'>
                box-shadow: {
                    shadow.map((element) => {
                        if (typeof element === 'number') {
                            return element + "px";
                        }
                        return `${element}`;
                    }).join(" ")
                };
            </div>
        </div>
    )
}
export default CodeOutput

```

Le composant CodeOutput prend une seule prop appelée `shadow`, qui est un tableau représentant les valeurs de la propriété CSS `box-shadow`. Le composant retourne du JSX qui affiche la sortie CSS basée sur la prop `shadow` passée.

Le JSX contient deux divs : une avec le nom de classe `paneChild`, et l'autre avec le nom de classe `codeOutput`. À l'intérieur de la div `codeOutput`, le composant mappe chaque élément de la prop `shadow` et génère le code CSS correspondant.

Si l'élément est un nombre, il ajoute "px" à la valeur, sinon il ajoute l'élément en tant que chaîne. Le tableau résultant de valeurs CSS est joint en une seule chaîne avec un espace entre chaque valeur.

# Tout rassembler

Nous avons presque terminé. Rassemblons tout dans le fichier `Container.jsx`. Importez le hook `useState`, les composants `Control`, et `CodeOutPut` respectivement comme suit :

```jsx
import React, { useState } from 'react'
import Control from './Control'
import CodeOutput from './CodeOutput'

```

Créez un composant fonctionnel appelé `Container`. Dans ce composant, utilisez le hook `useState` pour créer une variable `boxShadow` et définissez sa valeur initiale sur un tableau avec six éléments : `[23, 23, 0, 10, " ", "#00000045"]`.

```jsx
function Container(){
  const [boxShadow, setBoxShadow] = useState([23, 23, 0, 10, " ", "#00000045"])
}

export default Container

```

⚠️ **Notez** que les quatre premiers éléments du tableau (`[23, 23, 0, 10]`) représentent respectivement le décalage horizontal, le décalage vertical, le rayon de flou et le rayon de propagation de l'ombre. Le cinquième élément (`" "`) est un espace réservé pour la propriété inset de l'ombre, qui n'est pas utilisée dans ce cas. Enfin, le sixième élément (`"#00000045"`) représente la couleur de l'ombre au format HEX.

Votre composant devrait retourner trois divs enveloppées dans un fragment React. La première div devrait avoir des noms de classe "controlPane" et "controls". La dernière div devrait avoir le nom de classe "controlPane".

```jsx
function Container(){
  const [boxShadow, setBoxShadow] = useState([23, 23, 0, 10, " ", "#00000045"])
  return(
    <>
      <div className="controlPane controls"></div>
      <div></div>
      <div className="controlPane"></div>
    </>
  )
}

```

## Travaillons sur la première div

Dans la première div, ajoutez six composants `Control` :

```jsx
    <div className='controlPane controls'>
        <Control label="Couleur" type="color" value={boxShadow[5]} onChangeHandler={e => onChangeHandler(e, 5)} />
        <Control label="Décalage X" type="range" value={boxShadow[0]} onChangeHandler={e => onChangeHandler(e, 0)} />
        <Control label="Décalage Y" type="range" value={boxShadow[1]} onChangeHandler={e => onChangeHandler(e, 1)} />
        <Control label="Flou" type="range" value={boxShadow[2]} onChangeHandler={e => onChangeHandler(e, 2)} />
        <Control label="Propagation" type="range" value={boxShadow[3]} onChangeHandler={e => onChangeHandler(e,3)} />
        <Control label="Inset" type="checkbox" value={boxShadow[4]} onChangeHandler={e => onChangeHandler(e, 4)} />
    </div>

```

Chaque composant `Control` représente un élément dans le tableau `boxShadow`. Chacun a une prop `label`, une prop `type`, une prop `value` définie sur la valeur de l'index de l'élément dans le tableau `boxShadow`, et une prop `onChangeHandler` qui appelle une fonction `onChangeHandler` avec l'événement et l'index de la valeur à changer.

### Comment déclarer la fonction `onChangeHandler`

Juste au-dessus de l'instruction `return`, créez une fonction qui prend deux paramètres, `e` et `index`.

```jsx
function onChangeHandler(e, index) {
    switch (index) {
        case 5:
            setBoxShadow(boxShadow.map((c, i) => i === index ? e : c));
            break;
        case 4:
            setBoxShadow(boxShadow.map((c, i) => i === index ? e.target.checked ? 'inset' : '' : c));
            break;
        default:
            setBoxShadow(boxShadow.map((c, i) => i === index ? +e.target.value : c));
            break;
    }
}

```

La fonction `onChangeHandler` prend deux arguments : `e` qui est un objet événement, et `index` qui est une valeur d'index numérique.

La fonction utilise une instruction switch pour déterminer quelle logique exécuter en fonction de la valeur de `index`. Si `index` est 5, la fonction met à jour l'état `boxShadow` en mappant le tableau existant et en remplaçant la valeur à l'index `5` par `e`.

Si `index` est 4, la fonction met à jour l'état `boxShadow` en mappant le tableau existant et en remplaçant la valeur à l'index `4` par la chaîne `'inset'` ou une chaîne vide (`''`) selon que `e.target.checked` est vrai ou faux, respectivement.

Sinon, si `index` est une autre valeur, la fonction met à jour l'état `boxShadow` en mappant le tableau existant et en remplaçant la valeur à l'index spécifié par la valeur numérique de `e.target.value`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Controls-1.png)
_La première div devrait ressembler à ceci._

## Travaillons sur la deuxième div

Dans la deuxième div, ajoutez une autre div avec le nom de classe "square". Rappelez-vous que la deuxième div est l'endroit où un aperçu de l'ombre de la boîte sera placé.

```jsx
  <div>
    <div className='square'></div>
  </div>

```

Définissez l'attribut `style` de la div avec le nom de classe "square" comme suit :

```css
{
  boxShadow: boxShadow.map(shadowArrayToString).join(" "),
  backgroundColor: "#ffffff",
  border: "solid 0.2px"
}

```

La propriété `boxShadow` est définie sur le résultat de la méthode `map` appelée sur le tableau `boxShadow`. La méthode `map` retourne un nouveau tableau où chaque élément du tableau original est converti en une chaîne en utilisant la fonction `shadowArrayToString`, puis les chaînes résultantes sont jointes avec un caractère d'espace.

Maintenant, le code complet pour la deuxième div devrait ressembler à ceci :

```jsx
<div>
  <div className='square' style={{
    boxShadow: boxShadow.map(shadowArrayToString).join(" "),
    backgroundColor: "#ffffff",
    border: "solid 0.2px"
  }}></div>
</div>

```

Juste en dessous de la fonction `useChangeHandler`, ajoutez le code suivant :

```javascript
const shadowArrayToString = (element) => {
    if (typeof element === "number") {
        return element + "px";
    }
  return element;
}

```

La fonction `shadowArrayToString` prend un argument appelé `element`. Le but de cette fonction est de convertir les éléments du tableau `boxShadow` (qui peut contenir des valeurs numériques représentant des tailles de pixels) en un format de chaîne avec un suffixe "px". Si l'argument `element` n'est pas un nombre, la fonction retourne la valeur `element` inchangée.

![La div complétée.](https://www.freecodecamp.org/news/content/images/2023/04/Second-Div.png)
_La deuxième div._

## Travaillons sur la dernière div

La dernière div devrait avoir le nom de classe "controlPane" et `CodeOutput` comme composant enfant. Le `ChildOutput` devrait avoir une prop `shadow` définie sur l'état `boxShadow`.

```jsx
<div className='controlPane'>
  <CodeOutput shadow={boxShadow} />
</div>

```

Le fichier `Container.jsx` devrait ressembler à ceci :

```jsx
import React, { useState } from 'react'
import Control from './Control'
import CodeOutput from './CodeOutput'
function Container() {
    const [boxShadow, setBoxShadow] = useState([23, 23, 0, 10, " ", "#00000045"])
    function onChangeHandler(e, index) {
        switch (index) {
            case 5:
                setBoxShadow(boxShadow.map((c, i) => i === index ? e : c));
                break;
            case 4:
                setBoxShadow(boxShadow.map((c, i) => i === index ? e.target.checked ? 'inset' : '' : c));
                break;
            default:
                setBoxShadow(boxShadow.map((c, i) => i === index ? +e.target.value : c));
                break;
        }
    }
    const shadowArrayToString =
        (element) => {
            if (typeof element === "number") {
                return element + "px";
            }
          return element;
    }
    return (
        <>
            <div className='controlPane controls'>
                <Control label="Couleur" type="color" value={boxShadow[5]} onChangeHandler={e => onChangeHandler(e, 5)} />
                <Control label="Décalage X" type="range" value={boxShadow[0]} onChangeHandler={e => onChangeHandler(e, 0)} />
                <Control label="Décalage Y" type="range" value={boxShadow[1]} onChangeHandler={e => onChangeHandler(e, 1)} />
                <Control label="Flou" type="range" value={boxShadow[2]} onChangeHandler={e => onChangeHandler(e, 2)} />
                <Control label="Propagation" type="range" value={boxShadow[3]} onChangeHandler={e => onChangeHandler(e,3)} />
                <Control label="Inset" type="checkbox" value={boxShadow[4]} onChangeHandler={e => onChangeHandler(e, 4)} />
            </div>
            <div>
                <div className='square'
                    style={{
                        boxShadow: boxShadow.map(shadowArrayToString).join(" "),
                        backgroundColor: "#ffffff",
                        border: "solid 0.2px"
                    }}></div>
            </div>
            <div className='controlPane'>
                <CodeOutput shadow={boxShadow} />
            </div>
        </>
    )
}
export default Container

```

Dans le fichier `App.jsx`, importez les composants `Header` et `Container` et modifiez le composant fonctionnel de sorte que le code final ressemble à ceci :

```jsx
import './App.css'
import Header from './components/Header'
import Container from './components/Container'
function App() {
  return (
    <div className="App">
      <Header />
      <div className='mainApp'>
        <Container />
      </div>
    </div>
  )
}
export default App

```

Le projet terminé devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/AppShot-2.png)

# Conclusion

C'est tout ! Vous avez créé avec succès un générateur d'ombre de boîte. Faisons un récapitulatif de certains des concepts que nous avons couverts ici :

1. **Vite :** Nous avons appris comment échafauder un projet React de base avec Vite. Vite est une excellente alternative à create-react-app et vous pouvez en apprendre plus à ce sujet [ici](https://www.freecodecamp.org/news/get-started-with-vite/). Vous pouvez construire ce projet avec `yarn build` ou `npm run build`. 
2. **React-colourful :** React-Colourful est une bibliothèque pour rendre les composants de sélecteur de couleur avec React. Dans ce tutoriel, nous avons utilisé le `HexAlphaColorPicker`, mais React-Colorful offre différents types de sélecteurs de couleur. Le [package NPM](https://www.npmjs.com/package/react-colorful) est super populaire, recevant jusqu'à 1,9 million de téléchargements par semaine.
3. **Comment mettre à jour l'état d'un tableau :** Nous avons exploré comment utiliser la méthode JavaScript `map` pour mettre à jour l'état de notre générateur d'ombre de boîte, le rendant plus dynamique et interactif. Vous pouvez en apprendre plus sur les états à partir de la documentation officielle [React Documentation](https://react.dev/learn/state-a-components-memory).

N'oubliez pas de consulter ce projet sur [GitHub](https://github.com/daviduzondu/Shadowgen) et de me suivre sur [Twitter](https://twitter.com/daveuzondu). J'espère que vous avez trouvé ce tutoriel utile. Merci d'avoir lu.