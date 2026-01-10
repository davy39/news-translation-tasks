---
title: Vue vs React – Comment passer d'un Framework à l'autre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-22T21:59:39.000Z'
originalURL: https://freecodecamp.org/news/vue-vs-react-comparison-of-frameworks
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-ryutaro-tsukata-5472355.jpg
tags:
- name: framework
  slug: framework
- name: React
  slug: react
- name: vue
  slug: vue
seo_title: Vue vs React – Comment passer d'un Framework à l'autre
seo_desc: "By Yiğit Kemal Erinç\nThese days, a new trending front-end framework is\
  \ released every now and then. But React and Vue.js still stand as the most popular\
  \ among all the other alternatives. \nAnd although both are performant, elegant,\
  \ and arguably easy t..."
---

Par Yiğit Kemal Erinç

De nos jours, un nouveau framework front-end tendance est publié de temps en temps. Mais React et Vue.js restent les plus populaires parmi toutes les autres alternatives. 

Et bien qu'ils soient tous deux performants, élégants et relativement faciles à apprendre, ils ont des opinions différentes sur la manière dont certaines choses doivent être faites, et des façons différentes d'atteindre le même résultat final.

Je pense que devenir à l'aise et efficace avec un framework front-end consiste surtout à apprendre les motifs pour faire des choses régulières.

Vous savez, comment écouter les changements d'un paramètre/données et effectuer une action sur celui-ci. Et comment lier un écouteur d'événement ou des données à un objet d'action (bouton, case à cocher, etc.) et ainsi de suite. 

Alors que je travaillais sur un projet parallèle avec React, j'ai remarqué que mon esprit était comme : "Oui, je pourrais le faire comme ça dans Vue, j'émettrais un événement depuis l'enfant, puis je l'écouterais dans le parent et mettrais à jour ces données". Et puis je cherchais sur Google comment faire quelque chose comme ça dans React.

Dans cet article, je vais vous montrer comment appliquer certains motifs courants dans React et Vue que vous rencontrerez dans votre travail front-end quotidien. Ensuite, vous pourrez utiliser ces recettes pour passer facilement d'un framework à l'autre.

Cela sera utile que vous soyez un développeur Vue expérimenté qui doit travailler sur un projet React ou inversement. J'utiliserai React moderne avec des hooks et l'API Options de Vue (Vue 2). 

Je suggère de cloner le [dépôt](https://github.com/yigiterinc/VueVsReact) qui contient tout le code que j'utilise dans cet article et de rendre les composants respectifs dans chaque section et de jouer avec eux pour vraiment comprendre comment ils fonctionnent. 

Après avoir cloné, vous devez exécuter **npm install** dans les dossiers React et Vue. Ensuite, vous pouvez démarrer le projet React avec **npm start** et le projet Vue avec **npm run serve**.

```
https://github.com/yigiterinc/VueVsReact
```

### Table des matières

* [Structure des composants dans React vs Vue](#heading-structure-des-composants)
* [Comment utiliser l'état dans React et Vue](#heading-comment-utiliser-letat)
* [Comment utiliser les Props dans Vue et React](#heading-comment-utiliser-les-props)
* [Comment créer des méthodes/fonctions dans Vue et React](#heading-comment-creer-des-methodesfonctions)
* [Options de style](#heading-options-de-style)
* [Comment lier la saisie de formulaire aux données (État)](#heading-comment-lier-la-saisie-de-formulaire-aux-donnees-etat)
* [Comment gérer les événements (Saisie utilisateur)](#heading-gestion-des-evenements-saisie-utilisateur)
* [Style conditionnel](#heading-style-conditionnel)
* [Rendu conditionnel](#heading-rendu-conditionnel)
* [Rendu des tableaux (Listes)](#heading-rendu-des-tableaux-listes)
* [Communication enfant vers parent](#heading-communication-enfant-vers-parent)
* [Réagir aux changements de données/état](#heading-reagir-aux-changements-de-donneesetat)
* [Propriétés calculées vs useMemo](#heading-proprietes-calculees-vs-usememo)
* [Slots Vue vs Render Props](#heading-vue-slots-vs-render-props)

<h2 id=1>Structure des composants</h2>

Prenons un aperçu général de certains composants très basiques dans les deux frameworks. Nous allons étendre cela dans les sections suivantes.

Dans Vue, un composant à fichier unique contient 3 parties : le template, le script et le style.

Le template est la partie qui sera rendue. Il contient le HTML du composant et a accès aux données (et méthodes) dans les scripts et les styles.

Vous pouvez trouver tout ce qui concerne un composant à l'intérieur de ces sections dans Vue.

```javascript
<template>
  <div id="structure">
    <h1>Bonjour depuis Vue</h1>
  </div>
</template>

<script>
export default {}
</script>

<!-- Utilisez des préprocesseurs via l'attribut lang ! par exemple <style lang="scss"> -->
<style>
#structure {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

Pour obtenir ce composant rendu sans routeur ou autres choses compliquées, vous pouvez l'ajouter à **App.vue.** Je suggère de rendre chaque composant au fur et à mesure que vous suivez pour que vous puissiez les voir en action :

```js
<template>
  <div id="app">
    <structure />
  </div>
</template>

<script>
import Structure from './Structure/Structure.vue'

export default {
  name: 'App',
  components: { Structure },
}
</script>

```

Vous allez changer le composant d'importation à l'intérieur de la section **components** et le nom de la balise dans la section **template**.

Dans React, un composant fonctionnel est une fonction qui retourne du [JSX](https://reactjs.org/docs/introducing-jsx.html) (une extension de JavaScript qui permet d'utiliser des balises HTML à l'intérieur du code JS). Vous pouvez penser qu'il retourne du HTML pour simplifier les choses. La partie qui sera rendue était écrite à l'intérieur de la fonction `render()` dans React basé sur les classes, si vous êtes plus familier avec cela. 

Au fur et à mesure que vous progressez dans ce tutoriel, dans chaque section, vous pouvez mettre les composants respectifs à l'intérieur de App.js pour les rendre comme ceci :

```js
import React from 'react'

function Structure() {
  return <div>Rendre moi App</div>
}

export default Structure

```

```js
import './App.css'

import Structure from './Structure/Structure'

function App() {
  return (
    <div className="App">
      <Structure />
    </div>
  )
}

export default App

```

Donc, vous allez changer l'importation et le composant à l'intérieur de la div.

<h2 id=2>Comment utiliser l'état</h2>

Dans Vue, nous avons appris que la balise script contient les données et méthodes liées au composant. L'API Options de Vue a des mots-clés spéciaux (options) tels que _data, methods, props, computed, watch,_ et _mixins_ que nous pouvons utiliser, ainsi que des méthodes de cycle de vie telles que _created_ et _mounted_. 

Nous allons utiliser l'option `data` pour utiliser l'état dans notre composant. Les données doivent être définies comme une fonction qui retourne un objet contenant nos états. 

Pour accéder à l'état à l'intérieur de notre HTML (template), nous devons utiliser des doubles accolades et écrire le nom de notre variable. Gardez à l'esprit que tout changement dans les variables de données entraînera un rendu si cette variable est utilisée (référencée) dans le HTML.

```javascript
<template>
  <div>
    <h1>Bonjour {{ currentFramework }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentFramework: ' Vue !',
      alternative: ' React !',
    }
  },
}
</script>

<!-- Utilisez des préprocesseurs via l'attribut lang ! par exemple <style lang="scss"> -->
<style></style>

```

Dans React, les composants fonctionnels étaient sans état. Mais grâce aux hooks, nous avons maintenant le hook `useState` pour stocker l'état à l'intérieur de notre composant. Pour utiliser le hook useState, nous devons l'importer, et la syntaxe est :

```javascript
import React, { useState } from 'react';


function App() {
    const [stateName, setStateName] = useState('default value'); 
}
```

Nous définissons le nom de la variable d'état et le nom de sa fonction setter à l'intérieur des crochets, puis nous passons la valeur par défaut de notre variable au hook useState. 

Vous pouvez imaginer le hook comme ceci pour mieux comprendre la syntaxe : C'est comme une fonction qui crée une variable, définit sa valeur à la valeur passée, puis retourne un tableau qui contient la variable et sa fonction setter. 

Notez que vous devez utiliser une seule paire de parenthèses pour passer à la portée JavaScript et imprimer une variable à l'intérieur de votre JSX, au lieu de doubles parenthèses, qui était le cas avec Vue.

```javascript
import { React, useState } from 'react'

function TestUseState() {
  const [frameworkName, setFrameworkName] = useState('React')

  return (
    <div>
      <h1>useState API</h1>
      <p>Framework actuel : {frameworkName}</p>
    </div>
  )
}

export default TestUseState

```

<h2 id=3>Comment utiliser les Props</h2>

Dans Vue, nous définissons les props en ajoutant l'option props à l'intérieur de l'objet que nous exportons à l'intérieur du champ script comme nous l'avons fait avec l'option data. Il est une bonne pratique de définir les props comme des objets afin que nous ayons plus de contrôle sur la manière dont elles sont utilisées. 

Par exemple, spécifiez leurs types, leurs valeurs par défaut, et rendez-les obligatoires si nécessaire. Vue affichera un avertissement si vous utilisez le composant de manière incorrecte, comme l'appeler sans passer une prop obligatoire. 

Disons que nous avons un composant enfant Address qui sera appelé depuis le composant parent `UserInfo`.

```javascript
<template>
  <div class="address">
    <p>Ville : {{ city }}</p>
    <p>Rue : {{ street }}</p>
    <p>Numéro de maison : {{ houseNumber }}</p>
    <p>Code postal : {{ postalCode }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  props: {
    city: {
      type: String,
      default: 'Munich',
    },
    street: {
      type: String,
      required: true,
    },
    houseNumber: {
      type: Number,
      required: true,
    },
    postalCode: {
      type: Number,
      required: true,
    },
  },
}
</script>

<style></style>

```

Nous pouvons accéder à nos props de la même manière que nos variables de données – en utilisant les doubles accolades à l'intérieur du template. Et nous pouvons passer les props depuis le parent comme ceci :

```javascript
<template>
  <div class="address">
    <p>Nom : Yigit</p>
    <Address
      street="randomStrasse"
      :postalCode="80999"
      :houseNumber="32"
    ></Address>
  </div>
</template>

<script>
import Address from '@/components/Address.vue'

export default {
  data() {
    return {}
  },
  components: {
    Address,
  },
}
</script>

<style></style>

```

Remarquez comment nous utilisons le raccourci v-bind `:` et écrivons `:postalCode` et `:houseNumber` pour indiquer que ce ne sont pas des chaînes mais des objets de type Number. Nous devons utiliser cette syntaxe chaque fois que nous devons passer autre chose qu'une chaîne (tableau, objet, nombre, etc.). 

Cela peut vous confondre si vous venez de React, donc vous pourriez vouloir lire plus sur [v-bind](https://vuejs.org/v2/guide/class-and-style.html) pour mieux comprendre comment cela fonctionne.

Dans React, nous n'avons pas besoin de définir explicitement quelles props seront passées dans le composant enfant. Nous pouvons soit utiliser la déstructuration d'objet pour assigner les props à des variables, soit y accéder en utilisant l'objet props. Nous accédons à nos props à l'intérieur de JSX, de la même manière que nous accédons à l'état.

```javascript
import React from 'react'

function Address({ city, street, postalCode, houseNumber }) {
  return (
    <div>
      <p>Ville : {city}</p>
      <p>Rue : {street}</p>
      <p>Code postal : {postalCode}</p>
      <p>Numéro de maison : {houseNumber}</p>
    </div>
  )
}

export default Address

```

Et nous pouvons passer les props depuis le parent comme ceci :

```javascript
import React from 'react'

function UserInfo() {
  return (
    <div>
      <p>Nom : Yigit</p>
      <Address
        city="Istanbul"
        street="Ataturk Cad."
        postalCode="34840"
        houseNumber="92"
      ></Address>
    </div>
  )
}

export default UserInfo
```

<h2 id=4>Comment créer des méthodes/fonctions</h2>

Dans Vue, nous définissons les méthodes de manière similaire aux données – nous pouvons simplement mettre une option méthodes sous les données et définir la méthode. Nous pouvons appeler ces méthodes depuis le template et les méthodes peuvent accéder/modifier nos données.

```javascript
<template>
  <div>
    {{ sayHello() }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      to: 'Méthodes',
    }
  },
  methods: {
    sayHello() {
      return 'Bonjour ' + this.to
    },
  },
}
</script>

<style></style>

```

Faites attention lorsque vous essayez d'accéder aux méthodes ou propriétés de données du composant depuis l'intérieur de l'objet exporté (code à l'intérieur de la balise script). Si vous n'incluez pas le mot-clé `this`, Vue affichera une erreur disant qu'il ne sait pas où se trouve cette propriété/méthode.

Dans React, les choses sont un peu plus simples. Ce n'est que la définition de fonction JS régulière, avec la syntaxe ES6, si vous le souhaitez.

```javascript
import React from 'react'

function HelloFunctions() {
  const to = 'Fonctions'

  function sayHello() {
    return 'Bonjour ' + to
  }

  const sayHelloModern = () => 'Bonjour ' + to

  return (
    <div>
      {sayHello()}
      <br />
      {sayHelloModern()}
    </div>
  )
}

export default HelloFunctions

```

<h2 id=5>Options de style</h2>

Le style des composants Vue est vraiment simple. Nous devons simplement écrire nos bonnes vieilles classes CSS et sélecteurs à l'intérieur de la balise `style`. 

Vue supporte également le CSS scopé en utilisant le mot-clé `scoped`. Il aide à éviter les bugs visuels causés par l'assignation du même nom de classe à l'intérieur de différents composants. Par exemple, vous pourriez nommer le conteneur principal dans tous vos composants `main-container` et seules les styles dans ce fichier de composant seraient appliqués à chaque main-container. 

```javascript
<template>
  <div class="main-container">
    <h3 class="label">Je suis une étiquette stylée</h3>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
}
</script>

<style scoped>
.main-container {
  position: absolute;
  left: 50%;
  top: 45%;
  margin: 0;
  transform: translate(-50%, -50%);
  text-align: center;
}

.label {
  font-size: 30px;
  font-weight: 300;
  letter-spacing: 0.5rem;
  text-transform: uppercase;
}
</style>

```

Dans React, cependant, nous avons plus d'options en termes de style et c'est principalement une question de préférence personnelle puisque il y a plusieurs façons de styliser vos composants. Je vais suggérer quelques bonnes options ici.

### 1) Écrire du CSS régulier dans un fichier .css et l'importer

C'est probablement l'approche la plus basique et directe pour appliquer des styles à vos composants React. Cela ne signifie pas que c'est une mauvaise approche, car elle permet d'écrire du bon vieux CSS. C'est une bonne méthode si vous êtes un guru CSS qui commence tout juste avec React. 

```javascript
import React from 'react'
import './styles.css'

function Styled() {
  return (
    <div>
      <h3 class="title">Je suis rouge</h3>
    </div>
  )
}

export default Styled

```

```css
.title {
  color: red;
  font-size: 30px;
}

```

### 2) Utiliser Material UI (useStyles/makeStyles)

Material UI est un framework CSS qui a tant de composants réutilisables. Il fournit également un moyen de styliser vos composants, qui utilise le CSS dans JS et a donc ses avantages tels que le CSS scopé. 

Le hook `makeStyles` reçoit une liste de classes dans un objet, puis vous pouvez utiliser ces classes en les assignant à des objets. 

```javascript
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles({
  root: {
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
    border: 0,
    borderRadius: 3,
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
    color: 'white',
    height: 48,
    padding: '0 30px',
  },
});

export default function Hook() {
  const classes = useStyles();
  return <Button className={classes.root}>Hook</Button>;
}

```

### 3) Utiliser les composants stylisés (CSS dans JS)

Les [composants stylisés](https://styled-components.com/) sont modernes et faciles à utiliser et permettent de tirer parti de toutes les fonctionnalités du CSS classique. 

À mon avis, ils sont plus faciles à utiliser et plus puissants que MaterialUI (vous pouvez également styliser les composants MaterialUI avec cela, au lieu d'utiliser `makeStyles`). C'est aussi mieux que d'importer un fichier CSS puisque c'est scopé et les composants stylisés sont réutilisables.

```javascript
import React from 'react'
import styled, { css } from 'styled-components'

// Utilisez Title et Wrapper comme n'importe quel autre composant React – sauf qu'ils sont stylisés !
const Title = styled.h1`
  font-size: 2em;
  text-align: center;
  color: palevioletred;
`

// Créez un composant Wrapper qui rendra une balise <section> avec quelques styles
const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
  height: 100vh;
`

function StyledComponent() {
  return (
    <Wrapper>
      <Title>Bonjour le monde !</Title>
    </Wrapper>
  )
}

export default StyledComponent

```

<h2 id=6>Comment lier la saisie de formulaire aux données (État)</h2>
    

Nous avons appris comment avoir un état à l'intérieur de nos composants, mais nous avons également besoin d'un moyen de lier les entrées utilisateur à cet état. Par exemple, dans les formulaires de connexion, nous aurons probablement besoin de stocker l'entrée du nom d'utilisateur et du mot de passe de l'utilisateur dans l'état du composant. React et Vue ont des façons différentes de garder les entrées utilisateur synchronisées avec l'état.

Dans Vue, nous avons une directive spéciale pour cette opération appelée [v-model](https://vuejs.org/v2/guide/forms.html). Pour l'utiliser, vous devez créer un état en utilisant la propriété `data` comme nous l'avons appris auparavant. Ensuite, vous ajoutez le mot-clé v-model à votre entrée et spécifiez quelle variable de données est responsable du stockage de cette entrée (cela est applicable aux éléments de saisie de formulaire, textarea et select). 

C'est une manière de haut niveau et propre de connecter les données, supprimant le besoin de créer des fonctions lambda ou des gestionnaires supplémentaires. 

```javascript
<template>
  <div>
    <input v-model="inputState" type="text" />
    <br />
    {{ inputState }}
    <br />
    <button @click="changeInputState()">Cliquez pour dire au revoir</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputState: 'Bonjour',
    }
  },
  methods: {
    changeInputState: function () {
      this.inputState = 'Au revoir'
    },
  },
}
</script>

<style></style>

```

Voici un petit exemple : nous avons une entrée de texte, et nous la connectons à la variable `inputState` en utilisant le mot-clé v-model. Ainsi, chaque fois que l'utilisateur saisit du texte, la variable `inputState` reflétera les changements automatiquement. 

Cependant, il y a une chose spéciale que vous devez savoir : v-model implémente le **liage de données bidirectionnel** contrairement au **liage unidirectionnel** dans React. 

Cela signifie que, non seulement lorsque vous changez l'entrée, les données changent, mais aussi, si vous changez les données, la valeur de l'entrée change également. 

Pour démontrer cela, j'ai créé un bouton et l'ai connecté à une méthode. Ne vous inquiétez pas pour la gestion des événements pour l'instant, nous verrons cela dans la section suivante. Lorsque le bouton est cliqué, la valeur de la variable inputState est changée et l'entrée change également lorsque cela se produit. 

Je vous encourage à essayer vous-même en exécutant le code. De plus, remarquez que la valeur initiale de votre zone de saisie est 'Bonjour' – elle n'est pas initialisée à une chaîne vide ou nulle parce que nous avons défini la variable `inputState` à 'Bonjour'.

Maintenant, voyons cela dans React :

```javascript
import { React, useState } from 'react'

function FormInputBinding() {
  const [userInput, setUserInput] = useState('Bonjour')

  return (
    <div>
      <input type="text" onChange={(e) => setUserInput(e.target.value)} />
      <button onClick={() => setUserInput('Au revoir')}>
        Cliquez pour dire au revoir
      </button>
      {userInput}
    </div>
  )
}

export default FormInputBinding

```

Ce sujet chevauche la gestion des événements utilisateur, donc si vous ne comprenez pas quelque chose, attendez de terminer la section suivante. Ici, nous gérons l'événement `onChange` manuellement et appelons la fonction `setUserInput` pour définir l'état à la valeur de l'événement. 

Comme nous l'avons mentionné précédemment, React utilise un modèle de **liage unidirectionnel**. Cela signifie que le changement de l'état userInput n'affectera pas la valeur que nous voyons à l'intérieur de la zone de texte – nous ne verrons pas Bonjour à l'intérieur de la zone de saisie initialement. De plus, lorsque nous cliquons sur le bouton, il mettra à jour l'état mais l'entrée à l'intérieur de la zone maintiendra sa valeur.

<h2 id=7>Gestion des événements (Saisie utilisateur)</h2>

Regardons un autre formulaire qui est plus proche des cas réels dans Vue et React :

```javascript
<template>
  <div>
    <input
      v-model="username"
      id="outlined-basic"
      label="Nom d'utilisateur"
      variant="outlined"
    />
    <input
      v-model="password"
      id="outlined-basic"
      type="password"
      label="Mot de passe"
      variant="outlined"
    />

    <input
      v-model="termsAccepted"
      id="outlined-basic"
      type="checkbox"
      label="Mot de passe"
      variant="outlined"
    />

    <Button variant="contained" color="primary" @click="submitForm">
      Soumettre
    </Button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      termsAccepted: false,
    }
  },
  methods: {
    submitForm: function () {
      console.log(this.username, this.password, this.termsAccepted)
    },
  },
}
</script>

<style></style>

```

Comme vous pouvez le voir, nous utilisons la propriété v-model que nous venons d'apprendre pour connecter toutes nos entrées à des propriétés de données (état). Ainsi, chaque fois que les entrées changent, Vue met automatiquement à jour la variable correspondante. 

Pour voir comment nous gérons un événement de clic sur un bouton, vérifiez le bouton Soumettre. Nous utilisons le mot-clé [v-on](https://vuejs.org/v2/guide/events.html) pour gérer l'événement de clic. `@click` est simplement un raccourci pour `v-on:click`.

Chaque fois qu'un événement de clic se produit, il appelle simplement la méthode `submitForm`. Vous pouvez vous familiariser avec la liste des événements possibles en parcourant la documentation liée.

Dans React, nous pouvons avoir un formulaire comme ceci :

```javascript
import { React, useState } from 'react'

import {
  TextField,
  Checkbox,
  FormControlLabel,
  Button,
} from '@material-ui/core'

function EventHandling() {
  let [username, setUsername] = useState('')
  let [password, setPassword] = useState('')
  let [termsAccepted, setTermsAccepted] = useState(false)

  const submitForm = () => {
    console.log(username, password, termsAccepted)
  }

  const formContainer = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '20px',
  }

  return (
    <div style={formContainer}>
      <TextField
        onInput={(e) => setUsername(e.target.value)}
        id="outlined-basic"
        label="Nom d'utilisateur"
        variant="outlined"
      />
      <TextField
        onInput={(e) => setPassword(e.target.value)}
        id="outlined-basic"
        type="password"
        label="Mot de passe"
        variant="outlined"
      />

      <FormControlLabel
        control={
          <Checkbox
            type="checkbox"
            checked={termsAccepted}
            onChange={(e) => setTermsAccepted(e.target.checked)}
          />
        }
        label="Accepter les termes et conditions"
      />

      <Button variant="contained" color="primary" onClick={() => submitForm()}>
        Soumettre
      </Button>
    </div>
  )
}

export default EventHandling
```

Nous créons nos variables d'état pour chaque entrée. Nous pouvons ensuite écouter les événements sur les entrées et l'événement sera accessible à l'intérieur de la fonction de gestionnaire. Nous appelons les setters d'état pour mettre à jour notre état en réponse à ces événements. 

<h2 id=8>Style conditionnel</h2>

Le style conditionnel signifie lier une classe ou un style à un élément si une condition est vraie. 

Dans Vue, cela peut être réalisé comme ceci :

```javascript
<template>
  <div>
    <button @click="toggleApplyStyles"></button>
    <p :class="{ textStyle: stylesApplied }">
      Cliquez sur le bouton pour {{ stylesApplied ? 'désactiver le style' : 'styliser' }} moi
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stylesApplied: false,
    }
  },
  methods: {
    toggleApplyStyles: function () {
      this.stylesApplied = !this.stylesApplied
    },
  },
}
</script>

<style>
.textStyle {
  font-size: 25px;
  color: red;
  letter-spacing: 120%;
}
</style>

```

Nous créons un paragraphe et voulons appliquer la classe `textStyle` uniquement lorsque la valeur de la propriété de données `stylesApplied` est vraie. Nous pouvons utiliser v-bind pour y parvenir. Le deux-points est le raccourci pour v-bind donc `:class` est identique à `v-bind:class`. 

Nous utilisons la syntaxe d'objet v-bind pour lier les classes. Nous passons un objet à la propriété de classe : {textStyle: stylesApplied}, ce qui signifie appliquer la classe `textStyle` si `stylesApplied` est vrai. 

C'est un peu compliqué au début, mais cela nous aide à éviter plusieurs instructions if enchaînées pour déterminer quelle classe sera appliquée et gère les liaisons de style de manière propre : noms de classe à gauche (clés de l'objet), conditions à droite (valeurs de l'objet).

Dans React, nous devons faire les choses de manière plus primitive.

```javascript
import { React, useState } from 'react'
import './styles.css'

function ConditionalStyling() {
  let [stylesApplied, setStylesApplied] = useState(false)

  return (
    <div>
      <button onClick={() => setStylesApplied(!stylesApplied)}>Cliquez sur moi</button>
      <p style={{ color: stylesApplied ? 'red' : 'green' }}>Rouge ou Vert</p>
      <p className={stylesApplied ? 'styleClass' : ''}>Rouge avec classe</p>
    </div>
  )
}

export default ConditionalStyling

```

Ici, nous utilisons du JavaScript simple pour lier soit un objet de styles, soit un nom de classe à l'élément. Je pense que cela complique un peu le code, et je ne suis pas un grand fan de cette syntaxe.

<h2 id=9>Rendu conditionnel</h2>

Parfois, nous voulons rendre un composant après qu'une opération – comme la récupération de données depuis une API – est terminée. Ou peut-être voulons-nous afficher un message d'erreur s'il y a une erreur ou un message de succès sinon. 

Pour de telles situations, nous utilisons le rendu conditionnel pour changer le HTML à rendre de manière programmatique. 

Dans Vue, il existe également des [directives spéciales](https://vuejs.org/v2/guide/conditional.html) pour cela. Nous pouvons utiliser `v-if` et `v-else` ou même `v-else-if` pour rendre des templates basés sur des conditions.

```javascript
<template>
  <div>
    <h2 v-if="condition1">condition1 est vraie</h2>
    <h2 v-else-if="condition2">condition2 est vraie</h2>
    <h2 v-else>toutes les conditions sont fausses</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      condition1: false,
      condition2: false,
    }
  },
}
</script>

<style></style>
```

Cette syntaxe nous permet de créer des chaînes complexes de rendu conditionnel sans compliquer notre code de template avec des instructions if else.

Voici l'une des façons d'accomplir le même résultat avec React :

```javascript
import React from 'react'

function ConditionalRendering() {
  const condition1 = false
  const condition2 = false

  function getMessage() {
    let message = ''

    if (condition1) {
      message = 'condition1 est vraie'
    } else if (condition2) {
      message = 'condition2 est vraie'
    } else {
      message = 'toutes les conditions sont fausses'
    }

    return <h1>{message}</h1>
  }

  return <>{getMessage()}</>
}

export default ConditionalRendering

```

Ce n'est que du JS et du JSX, pas de magie ici.

<h2 id=10>Rendu des tableaux (Listes)</h2>

Maintenant, voyons comment nous pouvons rendre des données de liste. Dans Vue, il y a le mot-clé `v-for` pour faire cela. La syntaxe **name in names** signifie que la variable name contiendra toujours le nom actuel. À mesure que l'index change, si l'index est 0, c'est `names[0]` et ainsi de suite. Nous pouvons également accéder à l'index en le spécifiant à l'intérieur des parenthèses. La directive **v-for** nécessite également une clé.

```javascript
<template>
  <div>
    <h1>Noms</h1>
    <ul>
      <li v-for="(person, index) in people" :key="index">{{ person.name }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      people: [
        {
          id: 0,
          name: 'Yigit',
        },
        {
          id: 1,
          name: 'Gulbike',
        },
        {
          id: 2,
          name: 'Mete',
        },
        {
          id: 3,
          name: 'Jason',
        },
        {
          id: 4,
          name: 'Matt',
        },
        {
          id: 5,
          name: 'Corey',
        },
      ],
    }
  },
}
</script>
```

Notez que nous pouvons également utiliser la directive **v-for** pour itérer sur les propriétés d'un objet. Rappelez-vous que, en JS, les tableaux sont juste un sous-ensemble spécial d'objets avec des clés numériques. 

Dans React, nous allons utiliser la fonction `Arrays.map` pour itérer sur le tableau et retourner une balise JSX pour chaque élément.

```javascript
import React from 'react'

function RenderingLists() {
  const cities = [
    'Istanbul',
    'Munich',
    'Los Angeles',
    'London',
    'San Francisco',
  ]

  return (
    <div>
      <h1>Villes</h1>
      {cities.map((city, index) => (
        <h4 key={index}>{city}</h4>
      ))}
    </div>
  )
}

export default RenderingLists

```

<h2 id=11>Communication enfant vers parent</h2>

Imaginez que vous avez un composant de formulaire et un sous-composant de bouton à l'intérieur. Et vous voulez effectuer une action lorsque ce bouton est cliqué, comme appeler une API pour soumettre des données – mais vous n'avez pas accès aux données du formulaire dans le composant bouton puisque elles sont stockées dans le parent. Que faites-vous ?

Eh bien, si vous êtes dans Vue, vous voulez émettre un événement personnalisé depuis l'enfant et agir sur celui-ci dans le parent. Dans React, vous créeriez la fonction qui sera exécutée (lorsque le bouton est cliqué) dans le parent, où la fonction a accès aux données du formulaire et la passez au composant bouton afin qu'il puisse appeler la fonction du parent. 

Voyons un exemple dans Vue :

```javascript
<template>
  <div>
    <button @click="buttonClicked">Soumettre</button>
  </div>
</template>

<script>
export default {
  methods: {
    buttonClicked: function () {
      this.$emit('buttonClicked') // Émet un événement buttonClicked vers le parent
    },
  },
}
</script>

<style></style>

```

Dans notre composant enfant, nous avons le bouton et au clic, nous émettons un événement `buttonClicked`. Nous pourrions également envoyer des données dans cet appel. Par exemple, si c'était une zone de texte au lieu d'un bouton et qu'elle avait ses propres données, nous pourrions envoyer ces données au parent avec emit. 

Dans le composant parent, nous devons écouter l'événement personnalisé `buttonClicked` que nous venons de créer.

```javascript
<template>
  <form action="#">
    <input v-model="username" type="text" />
    <child @buttonClicked="handleButtonClicked" />
  </form>
</template>

<script>
import Child from './Child.vue'

export default {
  components: { Child },
  data() {
    return {
      username: '',
    }
  },
  methods: {
    handleButtonClicked: function () {
      console.log(this.username)
    },
  },
}
</script>

<style></style>

```

Nous venons d'ajouter un événement `@buttonClicked` à notre appel de composant enfant pour gérer cet événement personnalisé. 

Dans React, nous pourrions obtenir les mêmes résultats en passant une fonction de gestionnaire au composant enfant. Le concept était un peu compliqué pour moi au début, mais la syntaxe est plus facile que l'exemple Vue et il n'y a pas de magie.

```javascript
import React from 'react'

function Child({ handleButtonClicked }) {
  return (
    <div>
      <button onClick={() => handleButtonClicked()}>Soumettre</button>
    </div>
  )
}

export default Child

```

Nous accédons à la prop `handleButtonClicked` et l'appelons lorsque le bouton est cliqué.

```javascript
import { React, useState } from 'react'

import Child from './Child.js'

function Parent() {
  const [username, setUsername] = useState('')

  const submitForm = () => {
    console.log(username)
    // Poster les données du formulaire à l'API...
  }

  return (
    <div>
      <input onChange={(e) => setUsername(e.target.value)} type="text" />
      <Child handleButtonClicked={submitForm} />
    </div>
  )
}

export default Parent

```

Dans le parent, nous passons la fonction `submitForm` en tant que prop `handleButtonClicked` qui fera le travail.

<h2 id=12>Réagir aux changements de données/état</h2>

Dans certains cas, nous devons réagir aux changements de données. Par exemple, lorsque vous souhaitez effectuer des opérations asynchrones ou coûteuses en réponse à un changement de données.

 Dans Vue, nous avons des propriétés `watch` ou des observateurs pour cela. Si vous êtes familier avec `useEffect` dans React, c'est la chose la plus proche que vous pouvez trouver dans Vue et leurs cas d'utilisation sont plus ou moins les mêmes.

Voyons un exemple :

```javascript
<template>
  <div>
    <input v-model="number1" type="number" name="number 1" />
    <input v-model="number2" type="number" name="number 2" />
    {{ sum }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      number1: 0,
      number2: 0,
      sum: 0,
    }
  },
  watch: {
    number1: function (val) {
      this.sum = parseInt(val) + parseInt(this.number2)
    },
    number2: function (val) {
      this.sum = parseInt(this.number1) + parseInt(val)
    },
  },
}
</script>

<style></style>

```

Ici, nous avons `number1` et `number2` définis dans nos propriétés de données. Nous avons 2 entrées respectives et nous imprimons la somme de ces nombres et nous voulons que la somme soit mise à jour lorsque l'une des entrées change. 

À l'intérieur de la propriété `watch`, nous écrivons le nom de la variable que nous voulons **observer**. Dans ce cas, nous voulons observer number1 et number2. Si l'utilisateur entre une entrée, `v-model` changera la variable de données correspondante et lorsque cela se produira, la fonction **watch** pour cette variable sera déclenchée et la valeur de la somme sera recalculée.

Notez que, dans une application réelle, vous n'auriez pas besoin d'utiliser watch pour cette chose simple et vous mettriez simplement la somme à l'intérieur de `computed` à la place. C'est un exemple inventé pour démontrer comment `watch` fonctionne. 

Avant d'utiliser `watch` avec des choses plus compliquées comme des objets, des tableaux et des structures imbriquées, je suggère de lire [cet article](https://michaelnthiessen.com/how-to-watch-nested-data-vue/) car vous devrez probablement apprendre certaines options `watch` comme `deep` et `immediate`.

Dans React, nous utilisons le hook intégré `useEffect` pour observer les changements.

```javascript
import { React, useState, useEffect } from 'react'

function ReactToDataChanges() {
  const [number1, setNumber1] = useState(0)
  const [number2, setNumber2] = useState(0)
  const [sum, setSum] = useState(0)

  useEffect(() => {
    console.log('Je suis ici !')
    setSum(parseInt(number1) + parseInt(number2))
  }, [number1, number2])

  return (
    <div>
      <input
        onChange={(e) => setNumber1(e.target.value)}
        type="number"
        name="number 1"
      />
      <input
        onChange={(e) => setNumber2(e.target.value)}
        type="number"
        name="number 2"
      />
      {sum}
    </div>
  )
}

export default ReactToDataChanges

```

`useEffect` attend une fonction à exécuter lorsqu'une dépendance change comme premier argument et une liste de dépendances comme deuxième argument. 

Gardez à l'esprit que c'est aussi un exemple inventé pour démontrer `useEffect` (nous pourrions obtenir le même résultat sans `useEffect` en sortant la variable sum de l'état).

Je veux montrer un cas d'utilisation très courant pour ce hook : récupérer des données depuis une API après le chargement du composant :

```javascript
useEffect(() => {
    fetchUserData()
}, [])

const fetchUserData = async () => {
    const url = '';
    const response = await axios.get(url);
    const user = response.data;
    setUser(user);
}
```

Nous pouvons spécifier un tableau vide pour exécuter `useEffect` une fois lorsque le composant est rendu. Dans Vue, nous ferions la même opération à l'intérieur d'un hook de cycle de vie, tel que `created` ou `mounted`.

<h2 id=13>Propriétés calculées vs useMemo</h2>

Vue a un concept appelé propriétés calculées, qui servent à mettre en cache des calculs plutôt complexes et à réévaluer leurs valeurs chaque fois que l'une des dépendances change (similaire à `watch`). 

C'est également utile pour garder nos templates propres et concis en déplaçant la logique vers **JavaScript**. Dans ce cas, ils agissent comme des variables régulières que nous ne voulons pas être un état.

```javascript
<template>
  <div>
    <h3>Les villes préférées de Yigit sont :</h3>
    <p v-for="city in favCities" :key="city">{{ city }}</p>
    <h3>Les villes préférées de Yigit aux États-Unis sont :</h3>
    <p v-for="town in favCitiesInUS" :key="town">{{ town }}</p>
    <button @click="addBostonToFavCities">
      Pourquoi Boston n'est-il pas là ? Cliquez pour ajouter
    </button>
  </div>
</template>

<script>
export default {
  computed: {
    favCitiesInUS: function () {
      return this.favCities.filter((city) => this.usCities.includes(city))
    },
  },
  data() {
    return {
      favCities: [
        'Istanbul',
        'Munich',
        'Los Angeles',
        'Rome',
        'Florence',
        'London',
        'San Francisco',
      ],
      usCities: [
        'New York',
        'Los Angeles',
        'Chicago',
        'Houston',
        'Phoenix',
        'Arizona',
        'San Francisco',
        'Boston',
      ],
    }
  },
  methods: {
    addBostonToFavCities() {
      if (this.favCities.includes('Boston')) return
      
      this.favCities.push('Boston')
    },
  },
}
</script>

<style></style>

```

Ici, nous ne voulons pas mettre la fonction `favCitiesInUS` à l'intérieur de notre template car c'est trop de logique. 

Pensez-y comme à une fonction dont la sortie sera mise en cache. La fonction sera réévaluée uniquement si `favCities` ou `usCities` (ses dépendances) changent. Pour essayer cela, vous pouvez cliquer sur le bouton et voir comment le template change. Gardez à l'esprit que les fonctions calculées ne reçoivent aucun argument.

Nous pouvons utiliser le hook `useMemo` pour obtenir le même résultat dans React. Nous enveloppons la fonction dans le hook useMemo et fournissons la liste des dépendances dans le deuxième argument. Chaque fois que l'une de ces dépendances change, React exécutera à nouveau la fonction.

```java
import { React, useMemo, useState } from 'react'

function UseMemoTest() {
  const [favCities, setFavCities] = useState([
      'Istanbul',
      'Munich',
      'Los Angeles',
      'Rome',
      'Florence',
      'London',
      'San Francisco',
    ]),
    [usCities, setUsCities] = useState([
      'New York',
      'Los Angeles',
      'Chicago',
      'Houston',
      'Phoenix',
      'Arizona',
      'San Francisco',
      'Boston',
    ])

  const favCitiesInUs = useMemo(() => {
    return favCities.filter((city) => usCities.includes(city))
  }, [favCities, usCities])

  return (
    <div>
      <h3>Les villes préférées de Yigit sont :</h3>
      {favCities.map((city) => (
        <p key={city}>{city}</p>
      ))}
      <h3>Les villes préférées de Yigit aux États-Unis sont :</h3>
      {favCitiesInUs.map((town) => (
        <p key={town}>{town}</p>
      ))}
      <button onClick={() => setFavCities([...favCities, 'Boston'])}>
        Cliquez-moi pour ajouter
      </button>
    </div>
  )
}

export default UseMemoTest

```

<h2 id=14>Slots Vue vs Render Props</h2>

Nous voulons parfois créer des composants génériques qui peuvent afficher d'autres composants à l'intérieur, comme un composant de grille qui affiche n'importe quel type d'élément à l'intérieur.

À cette fin, Vue a un mécanisme appelé [slots](https://twitter.com/caglarcilara/status/1448905192045531143?s=20). La logique derrière les slots est vraiment simple : vous ouvrez un slot dans le composant qui doit recevoir un autre composant à rendre (appelons-le consommateur, car il consomme les éléments qui sont fournis). 

Dans le producteur, vous passez les composants que le consommateur doit rendre à l'intérieur de ses balises – vous pouvez les considérer comme remplissant les slots que vous avez ouverts dans le consommateur. Le premier élément sera rendu dans le premier slot, le deuxième dans le deuxième slot, et ainsi de suite. 

S'il y a plus d'un slot, vous devez également définir les noms. Voyons un exemple :

```javascript
<template>
  <div>
    <h3>Composant dans le slot 1 :</h3>
    <slot name="slot1"></slot>
    <h3>Bonjour slot1</h3>
    <slot name="slot2"></slot>
    <h3>Composant dans le slot 3 :</h3>
    <slot name="slot3"></slot>
  </div>
</template>

<script>
export default {}
</script>

<style></style>

```

Voici notre composant consommateur. Il peut créer une mise en page ou une composition à partir de plusieurs composants. Nous créons les slots et leur donnons des noms distincts.

```javascript
<template>
  <div>
    <consumer>
      <custom-button
        text="Je suis un bouton dans le slot 1"
        slot="slot1"
      ></custom-button>
      <h1 slot="slot2">Je suis dans le slot 2, youpi</h1>
      <custom-button text="Je suis dans le slot 3" slot="slot3"></custom-button>
    </consumer>
  </div>
</template>

<script>
import CustomButton from './CustomButton.vue'
import Consumer from './Consumer.vue'

export default {
  components: {
    CustomButton,
    Consumer,
  },
}
</script>

<style></style>

```

Et voici le producteur passant les composants aux slots du consommateur en spécifiant leur nom de slot comme attribut.

Et voici le simple composant `CustomButton` si vous êtes intéressé par cela :

```javascript
<template>
  <button>{{ text }}</button>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: 'Je suis un composant bouton',
    },
  },
}
</script>

<style></style>

```

Pouvez-vous deviner la sortie sans exécuter le code ? Cela pourrait être un bon exercice pour vous assurer de comprendre les slots.

Dans React, c'est beaucoup plus simple. Je pense que les slots compliquent beaucoup les choses. Comme React utilise JSX, nous pouvons simplement nous en sortir en passant le composant à rendre comme une prop.

```js
import React from 'react'
import Child from './Child'

function Parent() {
  const compToBeRendered = (
    <div>
      <h1>Bonjour</h1>
      <button>Je suis un bouton</button>
    </div>
  )

  return (
    <div>
      <Child compToBeRendered={compToBeRendered}></Child>
    </div>
  )
}

export default Parent

```

```js
import React from 'react'

function Child({ compToBeRendered }) {
  return (
    <div>
      <h1>Dans l'enfant :</h1>
      {compToBeRendered}
    </div>
  )
}

export default Child

```

## Réflexions finales

Dans cette dernière section de l'article, je voudrais partager mes deux cents sur ces frameworks. 

Comme nous l'avons vu tout au long de l'article, Vue a généralement sa propre manière de faire les choses et a des constructions différentes pour la plupart des choses. Parfois, cela le rend un peu plus difficile à prendre en main à mon avis. 

D'un autre côté, React est comme du JS pur, mélangé avec JSX : pas beaucoup de magie et pas beaucoup de mots-clés spéciaux à apprendre. 

Bien qu'il ne soit peut-être pas le framework le plus adapté aux débutants, je crois que les abstractions/mots-clés que Vue fournit (comme v-for, v-if et l'API Options) vous permettent d'écrire du code à un niveau d'abstraction plus élevé (pensez à ajouter une simple instruction pour itérer sur des composants par rapport à une fonction map de bas niveau et multi-lignes).

Ces fonctionnalités rendent également votre code Vue plus structuré et propre car le framework est opinionné. Il a donc ses propres façons de faire les choses, et si vous faites les choses de cette manière, vous finirez avec un code facile à lire et à comprendre.

React, en revanche, n'est pas très opinionné sur les choses et offre aux développeurs beaucoup de liberté pour décider de la structure de leur projet eux-mêmes.

Mais cette liberté a un coût : si vous êtes un débutant qui n'est pas conscient des meilleures pratiques, il est facile de finir avec un code désordonné et un projet mal structuré. 

Une autre différence importante à mon avis est la suivante : si vous allez construire un projet non fondamental avec React, vous devrez utiliser beaucoup de bibliothèques externes pour développer à une vitesse normale, ce qui signifie que vous devrez également apprendre comment ces choses fonctionnent.

## Conclusion

Merci d'avoir lu et j'espère que cette comparaison a été utile. Si vous souhaitez entrer en contact, poser des questions ou discuter davantage, n'hésitez pas à m'envoyer un message sur [LinkedIn](https://www.linkedin.com/in/yigit-erinc/).