---
title: Comment gérer l'état dans vos applications – useState() vs Redux
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2023-07-31T21:35:43.000Z'
originalURL: https://freecodecamp.org/news/usestate-vs-redux-state-management
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/cover-react-redux.png
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'State Management '
  slug: state-management
seo_title: Comment gérer l'état dans vos applications – useState() vs Redux
seo_desc: "State management is crucial for handling an application's data, how users\
  \ interact with it, and how different parts of the app behave. \nAnd it's not something\
  \ you'll use only in React.js, but also in other popular tools like Angular.js,\
  \ Vue.js, and N..."
---

La gestion d'état est cruciale pour gérer les données d'une application, la manière dont les utilisateurs interagissent avec elle et le comportement des différentes parties de l'application. 

Et ce n'est pas quelque chose que vous n'utiliserez que dans [React.js](https://react.dev/), mais aussi dans d'autres outils populaires comme [Angular.js,](https://angularjs.org/) [Vue.js,](https://vuejs.org/) et [Next.js](https://nextjs.org/).

Il existe deux méthodes courantes pour gérer un état : useState et Redux. Mais il existe également d'autres options comme [MobX](https://mobx.js.org/README.html), [Zustand](https://www.npmjs.com/package/zustand), et [Recoil](https://recoiljs.org/).

Dans cet article, nous allons apprendre la gestion d'état et pourquoi elle est importante. Nous allons également explorer les méthodes courantes de gestion d'état et comprendre comment elles fonctionnent.

Après avoir lu cet article, vous serez en mesure de choisir la meilleure méthode de gestion d'état pour votre application.

### Prérequis

* Avoir une compréhension de React.
* Assurez-vous d'installer [Node.js](https://nodejs.org/en) sur votre système.

## Qu'est-ce que la gestion d'état et pourquoi est-elle importante ?

La gestion d'état est une partie cruciale du développement d'applications. Elle permet aux programmeurs de contrôler comment l'application répond à différents événements et actions de l'utilisateur. 

Elle vous aide à créer des interfaces dynamiques et interactives, améliorant ainsi l'expérience utilisateur.

### Quels types de sites/applications utilisent la gestion d'état ?

La gestion d'état est utilisée dans de nombreux sites web et applications, des plus simples aux plus complexes. 

React et des frameworks comme Angular.js, Vue.js et Next.js utilisent souvent la gestion d'état pour gérer les données et contrôler le comportement des composants.

### Que faut-il considérer lors du choix d'une stratégie de gestion d'état ?

1. **La complexité de l'application** : Pour les applications simples avec peu de composants, utilisez `useState()`. Pour les applications complexes avec des interactions d'état étendues, choisissez `Redux`.
2. **La taille de l'équipe et le niveau de compétence** : `useState()` est adapté aux petites équipes ou aux développeurs nouveaux dans la gestion d'état car il est facile à comprendre. `Redux` peut être bon pour les grandes équipes avec des développeurs expérimentés.
3. **Partage de l'état** : La gestion d'état centralisée de `Redux` est plus facile à utiliser dans certains cas que `useState()`.
4. **Évolutivité** : `Redux` offre des fonctionnalités avancées qui aident à gérer des états complexes.

## Exemples de gestion d'état : `useState()` vs `Redux`

Pour mieux comprendre la gestion d'état, examinons un exemple pratique qui montre comment `useState()` et `Redux` fonctionnent dans React.

### Installation du projet

Tout d'abord, allez dans le dossier du projet. Créez un modèle React en utilisant la commande create-react-app ou l'outil Vite.

Je préfère **[vite](https://vitejs.dev/)** (et c'est ce que la documentation React recommande actuellement), car il est plus rapide pour le développement et plus facile à configurer. Vite est également plus polyvalent et supporte d'autres frameworks front-end comme Svelte. Mais si vous préférez, create-react-app est toujours une option.

Ensuite, dans le terminal de votre éditeur, tapez cette commande :

```javascript
npx create-react-app ./ ou npx create-vite@latest ./
```

`./` crée le modèle React pour vous directement dans le dossier ou répertoire créé.

![Création du modèle React (template)](https://www.freecodecamp.org/news/content/images/2023/07/Code_Vp1nLXqZqd.gif)
_Création du modèle React (template)_

### Option 1 : Gestion de l'état avec `useState()`

`useState()` est un hook intégré dans React. Il gère l'état des applications React **localement.** 

`useState()` introduit des capacités de gestion d'état dans les composants fonctionnels. Cela signifie que vous pouvez maintenant utiliser une logique d'état dans les composants fonctionnels.

Dans React, vous avez accès à divers autres hooks que vous pouvez importer et utiliser dans vos applications. Ces hooks rendent votre application plus dynamique et efficace.

Consultez cet article pour en savoir plus : [Simplifiez votre programmation React sans effort avec ces 8 hooks incroyables](https://ijaycent.hashnode.dev/simplify-your-react-programming-effortlessly-with-these-8-amazing-hooks).

Pour plus d'informations sur le hook `useState()`, [vous pouvez consulter ce tutoriel](https://www.freecodecamp.org/news/usestate-hook-3-different-examples/). Il vous fournira des informations détaillées et des exemples liés à `useState()` dans React.

### Avantages de l'utilisation du hook `useState()` dans une application React

1. `useState()` a une empreinte plus petite que les bibliothèques externes de gestion d'état comme `Redux`. Cela réduit la taille du bundle de l'application et améliore les performances.
2. Il permet une gestion d'état plus claire et intuitive dans les composants fonctionnels.

### Inconvénients de l'utilisation du hook `useState()` dans une application React

1. Il est fastidieux de gérer l'état des composants complexes avec de nombreuses variables.
2. En raison de ses capacités limitées, il entraîne des problèmes comme le prop drilling, ce qui peut être un peu confus si ce n'est pas bien compris.
3. Il déclenche un re-rendu du composant, ce qui impacte les performances.

### Comment utiliser `useState()` dans les applications React

Alors, créons une application qui change la couleur en fonction de l'entrée de l'utilisateur.

L'utilisation de `useState()` implique un processus simple :

* Importez le hook `useState()` de la bibliothèque 'react'.
* Définissez une variable d'état et sa valeur initiale en utilisant la destructuration de tableau.
* Ensuite, définissez une autre variable d'état qui prend en compte le choix de couleur de l'utilisateur lorsqu'il est saisi.
* Utilisez la variable d'état et sa fonction de mise à jour correspondante dans la logique du composant pour lire ou mettre à jour l'état.

Voici à quoi cela ressemble en code :

```js
import React, { useState } from 'react';

const State = () => {
  const [text, setText] = useState('black');
  const [color, setColor] = useState('black'); // Un autre état pour stocker la couleur choisie par l'utilisateur

  const handleInputChange = (e) => {
    setText(e.target.value);
  };

  // Une fonction est déclarée
  const handleButtonClick = () => {
    setColor(text); // elle met à jour la couleur choisie lorsque le bouton est cliqué
  };

  return (
    <div>
      <p style={{ color: color }}>
        Ressources progressivement efficaces via des métriques commerciales.
      </p>
      <br />
      <div className='inputBtn-container'>
        <input
          type='text'
          className='input'
          value={text}
          onChange={handleInputChange}
        />
        <button className='btn' onClick={handleButtonClick}>
          Changer la couleur du texte
        </button>
      </div>
    </div>
  );
};

export default State;


```

Dans le code ci-dessus, la variable d'état `text` est définie sur l'état initial (couleur) en utilisant `useState()`. La fonction `setText` est définie pour mettre à jour la valeur de la couleur lorsque le bouton est cliqué.

Le deuxième état défini est pour stocker la mise à jour de la couleur par l'utilisateur. Ainsi, la couleur du `text` reste inchangée jusqu'à ce que le bouton soit cliqué. Une fois le bouton cliqué, l'état de la couleur est mis à jour avec la valeur de `text`, changeant la couleur du `text` en ce que l'utilisateur tape.

![état modifié d'une application utilisant useState()](https://www.freecodecamp.org/news/content/images/2023/07/chrome_bJlWaFiHPQ.gif)
_Résultat_

### Option 2 : Gestion de l'état avec `Redux`

`Redux` est une bibliothèque JavaScript pour gérer les états dans les applications. Elle fonctionne avec React et d'autres frameworks. 

`Redux` vous aide à gérer l'état **global** de votre application. Il améliore également les performances de votre application.

Pensez à `Redux` comme un contrôleur de trafic pour les données de l'application. Il s'assure que les bonnes informations vont aux bons endroits, afin que tout fonctionne sans accroc.

### Avantages de l'utilisation de `Redux` dans votre application

`Redux` peut sembler complexe au premier abord, mais il présente plusieurs avantages qui rendent son apprentissage utile :

1. `Redux` peut être utilisé avec d'autres frameworks front-end, pas seulement dans les applications React (par exemple Angular.js, Vue.js et Next.js).
2. `Redux` vous permet de stocker tous les états dans un magasin central, au lieu de disperser les états dans de nombreux composants. Cela facilite la compréhension, le suivi et la gestion de l'état de l'application.
3. De nombreuses grandes entreprises utilisent `Redux` pour gérer l'état de leur application.

### Inconvénients de l'utilisation de `Redux` dans votre application

1. L'utilisation de `Redux` peut rendre votre application plus compliquée, surtout si vous êtes nouveau dans ce domaine. Vous devrez apprendre de nouveaux concepts et écrire plus de code, ce qui peut prendre du temps à comprendre et à utiliser.
2. `Redux` nécessite plus de code par rapport à `useState()`.
3. Si votre application est petite ou n'a pas de besoins d'état complexes, l'utilisation de `Redux` peut être inutile.
4. Le débogage peut être difficile dans une configuration Redux complexe.

### Comment utiliser `Redux` dans votre application :

Tout d'abord, vous devrez installer le package Redux :

![comment redux est installé dans votre terminal](https://www.freecodecamp.org/news/content/images/2023/06/Code_jSqM9Qi2Oc.gif)
_Installation de redux dans votre éditeur de code_

Le gif ci-dessus montre que j'ai exécuté trois commandes ensemble dans le terminal. C'est une préférence personnelle. 

**Que font ces commandes :**

* `npm install redux` installe la bibliothèque `Redux`.
* `react-redux` signifie que `Redux` est utilisé dans une application React. Il fournit une intégration.
* `@reduxjs/toolkit` simplifie `Redux`, surtout pour les débutants. Il offre des outils et des abstractions utiles qui rendent le travail avec Redux plus facile et moins complexe pour les nouveaux développeurs.

Ensuite, vérifiez que `Redux` a bien été ajouté à vos dépendances. Regardez votre fichier `package.json`. Il contient des informations importantes sur les packages utilisés dans votre projet.

![react-dependencies](https://www.freecodecamp.org/news/content/images/2023/06/redux-depency2.png)
_react-dependencies_

Ensuite, importez {configureStore} depuis `@reduxjs/toolkit` dans le fichier `main.js` ou `index.js`.

Utilisez la balise provider pour envelopper le composant principal de notre application. Fournissez le `store` en tant qu'attribut (props) au provider. Cela rend le store accessible globalement dans toute notre application.

![import du store et du provider dans le fichier main.js ou index.js](https://www.freecodecamp.org/news/content/images/2023/07/image-136.png)
_import du store et de la balise provider_

Passons en revue quelques termes clés utilisés dans `Redux` :

**Store** : Un "conteneur" dans notre application est comme une unité de stockage. À l'intérieur du store, nous allons définir le **reducer**. 

`Redux` fonctionne sur la base des principes d'un store centralisé. Il agit comme un store central qui contient l'état entier de l'application. Lorsque n'importe quel composant a besoin d'accéder à l'état ou doit être mis à jour, il interagit avec le store. Le store gère ensuite les données et propage les changements aux parties pertinentes de l'application.

**Reducer** : Un reducer est un objet qui prend deux entrées : l'état précédent et une action. Il retourne l'état mis à jour en fonction des actions dispatchées. Il examine l'activité et décide comment mettre à jour l'état de l'application. 

Les reducers dans Redux contrôlent comment notre application réagit à l'entrée de l'utilisateur. Cette flexibilité rend facile la maintenance et le changement de notre code lorsque nécessaire. Nous pouvons utiliser les imports de store et Provider pour mettre à jour notre application.

### Exemple `Redux`

Alors, créons une application qui change la couleur en fonction de l'entrée de l'utilisateur et utilisons Redux pour gérer l'état cette fois.

Tout d'abord, créez un dossier appelé `components`. À l'intérieur de ce dossier, créez un fichier nommé `ChangeColor.jsx`.

![État initial](https://www.freecodecamp.org/news/content/images/2023/07/image-137.png)
_État initial de l'application_

Voici le résultat :

![output](https://www.freecodecamp.org/news/content/images/2023/06/static-redux.png)
_sortie statique_

Dans votre répertoire de projet, créez un dossier nommé `features`. À l'intérieur de ce dossier, créez un fichier appelé `Color.js` pour contenir la logique Redux de votre application.

![Color.js](https://www.freecodecamp.org/news/content/images/2023/06/color-redux.png)
_color.js_

Ensuite, nous voulons permettre aux utilisateurs de saisir leur couleur souhaitée. Pour cela, importez le hook useState() comme ceci :

**`ChangeColor.jsx`**

```js
import { useState } from 'react';   // hook useState()

const ChangeColor = () => {
  const [color, setColor] = useState(''); 
  return (
    <div>
      <p>Ressources progressivement efficaces via des métriques commerciales.</p>
      <br />
      <div className='inputBtn-container'>
        <input
          type='text'
          className='input'
        />
        <button className='btn'>changer la couleur du texte</button>
      </div>
    </div>
  );
};

export default ChangeColor;

```

Dans le fichier `color.js`. Ce fichier contient la logique Redux de votre application.

```js

// Importer les fonctions nécessaires depuis Redux Toolkit
import { createSlice } from "@reduxjs/toolkit";// Créer une slice pour la fonctionnalité est essentiel.

// Définir l'état initial pour la slice
const initialState = "black"


// Créer une slice en utilisant la fonction createSlice
const themeSlice = createSlice({
  name: 'theme', // Nom de la slice
  initialState: { value: initialState},// État initial pour la slice
  reducers: {
    changeColor: (state, action)=>{
      state.value=action.payload // Mettre à jour la valeur de la couleur en fonction de l'action dispatchée
    },
    }
  }
})
```

Voyons ce qui se passe dans ce code :

* `createSlice` est une fonction de Redux Toolkit qui permet aux développeurs de créer des reducers de manière claire et organisée. Elle simplifie la division de la logique et l'accès à celle-ci dans toute l'application. Avec createSlice, changer les valeurs et comprendre le code deviennent plus faciles.
* `name` est une chaîne qui définit le nom de la slice. Ce nom est utilisé comme préfixe pour les chaînes de type d'action générées.
* `initialState` est la valeur d'état initiale pour la slice.
* `reducers` sont des objets qui prennent deux entrées – l'état précédent et une action. Le reducer retourne l'état mis à jour en fonction des actions dispatchées. Il examine l'activité et décide comment mettre à jour l'état de l'application. Les reducers dans Redux contrôlent comment notre application réagit à l'entrée de l'utilisateur. Cette flexibilité rend facile la maintenance et le changement de notre code lorsque nécessaire. Nous pouvons utiliser les imports de store et Provider pour mettre à jour notre application. En utilisant le reducer, nous pouvons gérer et mettre à jour l'application de manière structurée. Il nous aide à suivre les changements selon notre logique souhaitée.
* `state` fait référence aux données stockées et gérées par l'application. Il contient les valeurs actuelles des variables, propriétés ou champs qui déterminent le comportement et l'apparence de l'application.
* `action` est un objet JavaScript simple qui décrit une intention de changer l'état. C'est ainsi que nous communiquons avec les reducers pour initier les mises à jour d'état.

Après avoir défini la logique du reducer, nous pouvons la rendre réutilisable en l'exportant depuis le fichier et en l'important là où nous avons besoin de gérer l'état. Par exemple, dans le fichier `changeColor.jsx`.

```js
import { createSlice } from "@reduxjs/toolkit";

const initialState="black"
export const themeSlice = createSlice({
  name: 'theme',
  initialState: { value: initialState},
  reducers: {
    changeColor: (state, action)=>{
      state.value=action.payload
    }
  }
})
// Exporter la fonction reducer
export const { changeColor } = themeSlice.actions
export default themeSlice.reducer
```

Voyons ce qui se passe dans ce code :

* Nous allons importer le hook `useSelector` depuis `react-redux` pour obtenir des données depuis le store Redux. Cela nous aide à obtenir la valeur actuelle de la couleur depuis l'état.
* Nous allons importer le hook `useDispatch` depuis `react-redux` pour envoyer des actions au store Redux. Cela nous permet de mettre à jour la valeur de la couleur dans l'état.
* Et enfin, importer le fichier `Color.js`, qui contient la logique Redux, y compris le reducer et l'action pour changer la couleur.

Ensuite :

1. Nous obtenons la couleur actuelle depuis le store Redux en utilisant le hook `useSelector`.
2. Nous rendons un élément d'entrée où les utilisateurs peuvent taper leur couleur souhaitée.
3. Nous définissons un gestionnaire d'événements pour gérer les changements de la valeur d'entrée. Lorsque l'utilisateur tape une couleur dans l'entrée, ce gestionnaire d'événements sera appelé.
4. Lorsque l'utilisateur clique sur le bouton "Changer la couleur", le gestionnaire d'événements envoie une action au store Redux avec la valeur de couleur mise à jour.

Avec ces changements, le composant `ChangeColor` utilise maintenant Redux pour gérer l'état. Les utilisateurs peuvent changer la couleur du texte affiché en tapant leur couleur souhaitée dans le champ d'entrée et en cliquant sur le bouton "Changer la couleur du texte".

```js
import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { changeColor } from '../features/Color';

const ChangeColor = () => {
  // État pour contenir la couleur sélectionnée
  const [color, setColor] = useState('');

  // Accéder à la fonction dispatch depuis react-redux
  const dispatch = useDispatch();

  // Accéder à la valeur de couleur du thème depuis le store Redux
  const themeColor = useSelector((state) => state.theme.value);

  // Gestionnaire d'événements pour le changement d'entrée
  const handleColorChange = (e) => {
    setColor(e.target.value);
  };

  // Gestionnaire d'événements pour le clic sur le bouton
  const handleButtonClick = () => {
    // Dispatch de l'action changeColor avec la couleur sélectionnée
    dispatch(changeColor(color));
  };

  return (
    <div style={{ color: themeColor }}>
      <p>Ressources progressivement efficaces via des métriques commerciales.</p>
      <br />
      <div className='inputBtn-container'>
        <input type='text' className='input' onChange={handleColorChange} />
        <button className='btn' onClick={handleButtonClick}>
          Changer la couleur du texte
        </button>
      </div>
    </div>
  );
};

export default ChangeColor;
```

Voici le résultat :

![État modifié en utilisant Redux](https://www.freecodecamp.org/news/content/images/2023/07/chrome_LDhsOmTm5O-1.gif)
_État modifié en utilisant Redux_

## Conclusion

L'article couvre deux solutions de gestion d'état : le hook `useState()` pour les applications petites à moyennes et `Redux` pour les plus grandes. 

Lors du choix de celle à utiliser, prenez en compte des facteurs comme la complexité de l'application, la taille de l'équipe et les besoins en performance. Comprendre les deux approches vous aidera à faire le bon choix.

Vous pouvez lire la [documentation Redux](https://redux.js.org/) pour en savoir plus.

Si vous avez trouvé cet article utile, partagez-le avec d'autres qui pourraient également le trouver intéressant. 

Vous pouvez également rester informé de mes derniers projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples) et [LinkedIn](https://https//www.linkedin.com/in/ijeoma-igboagu/).

Merci d'avoir lu 💖.