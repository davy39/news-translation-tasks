---
title: Conseils pour améliorer les performances de votre application React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-27T13:46:33.000Z'
originalURL: https://freecodecamp.org/news/tips-to-enhance-the-performance-of-your-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/react.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: React
  slug: react
- name: React context
  slug: react-context
- name: react testing library
  slug: react-testing-library
- name: Reactive Programming
  slug: reactive-programming
- name: React
  slug: reactjs
seo_title: Conseils pour améliorer les performances de votre application React
seo_desc: 'By Shifa Martin

  ReactJS is an open-source framework that facilitates the development of UI interfaces
  for web and mobile applications. Developers globally use the framework to build
  state-of-the-art applications which subsequently generate revenues a...'
---

Par Shifa Martin

ReactJS est un framework open-source qui facilite le développement d'interfaces utilisateur pour les applications web et mobiles. Les développeurs du monde entier utilisent ce framework pour créer des applications de pointe qui génèrent ensuite des revenus et élargissent l'audience des entreprises. 


Cependant, construire une excellente interface utilisateur avec React n'est pas suffisant. Vous devez ajouter cette touche supplémentaire pour rendre l'application plus polie, fonctionnelle et remarquablement meilleure que la concurrence. 

C'est exactement ce que je vais vous aider à faire en décrivant quelques méthodes clés pour augmenter les performances des applications React.

### 1. Bien utiliser les identités

Lors de la création d'applications mobiles avec React, il est possible d'envelopper des fonctions et des variables avec React.useMemo. Cela permet de les mémoriser afin qu'elles restent identiques pour les rendus futurs. 


Lorsque les fonctions et les variables ne sont pas mémorisées, toute référence à celles-ci peut disparaître des rendus futurs. La mémorisation aide à éviter les processus et opérations inutiles dans chaque situation où vous utiliseriez des fonctions et des variables.

_**Exemple :**_ 

Supposons que nous préparons un hook personnalisé pour une liste d'URL en tant qu'arguments. En utilisant ce hook, nous pouvons les collecter dans un tableau d'objets de promesse et les résoudre avec Promise.all. Les résultats de cette accumulation entreront dans l'état et seront passés au composant de l'application une fois terminés. La liste des promesses mappe maintenant le tableau des URL à partir duquel elle récupère les URL.

```react
import React from 'react'
import axios from 'axios'

export const useApp = ({ urls }) => {
  const [results, setResults] = React.useState(null)

  const promises = urls.map(axios.get)

  React.useEffect(() => {
    Promise.all(promises).then(setResults)
  }, [])

  return { results }
}

const App = () => {
  const urls = [
    'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=a',
    'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=b',
    'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=c',
  ]

  useApp({ urls })

  return null
}

export default App

```

Puisque nous voulons obtenir des données à partir de 3 URL ici, seulement 3 requêtes devraient être envoyées, une pour chaque URL. Cependant, en regardant cela à travers la fonctionnalité d'inspection d'élément sur Google Chrome, nous trouvons que 6 requêtes sont envoyées au lieu des 3 prévues. 
Cela se produit parce que l'argument des URL n'a pas conservé son identité précédente. Lorsque l'application est réaffichée, elle instancie un nouveau tableau à chaque fois, car React le traite comme une valeur différente. 


![Image](https://lh5.googleusercontent.com/XE6rCdOL110eYARSgVTgcwiecF2qNAT96yBYn_-FbQ2_ffjdRAplLqRxu4eQh-NniyF0doEPRtsT3X0lYxeHcSu35UN0giiteCsIJTrVP9tw1mITk5-P5hH3PmdWd2ss5R0E2pb3)

Pour résoudre ce problème, nous pouvons utiliser React.useMemo comme mentionné précédemment. Lorsque vous utilisez React.useMemo, le tableau d'objets de promesse ne sera pas recalculé à chaque nouveau rendu, sauf si le tableau contenant la liste des URL change. Tant qu'il reste le même, les identités restent.

**Voici ce qui se passe lorsque vous appliquez React.useMemo à cet exemple :**

```react
const useApp = ({ urls }) => {
  const [results, setResults] = React.useState(null)

  const promises = urls.map((url) => axios.get(url))

  React.useEffect(() => {
    Promise.all(promises).then(setResults)
  }, [])

  return { results }
}

const App = () => {
  const urls = React.useMemo(() => {
    return [
      'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=a',
      'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=b',
    ]
  }, [])

  const { results } = useApp({ urls })

  return null
}
```

Il enverra toujours 6 requêtes puisque nous n'avons mémorisé que le tableau des URL. Les variables de promesses sont également instanciées lors de l'exécution du hook. Donc, pour envoyer seulement 3 requêtes, nous devons également mémoriser les variables de promesses.

```react
const promises = React.useMemo(() => {
  return urls.map((url) => axios.get(url))
}, [urls])
```

> Après avoir mémorisé à la fois le tableau des URL et les variables de promesses, voici ce que nous obtenons : 

![Image](https://lh4.googleusercontent.com/P-8qvsq_Nu229Eod2_FIlqLtY1_lAxkPXZfw3a9D7P25VIyGrw--kTnOuTF4rmXPsA3vxGRifwprsI_VGGDU9pFIafOAsfPKiQE3L3Zv1MHXzPH25e2g39MaCikn2AActzgJlftr)

### 2. Fusion des props avec les enfants

Parfois, les développeurs se retrouvent dans des situations où ils préfèrent fusionner une prop avec les enfants avant le rendu. Pour faciliter cela, React permet de visualiser les props de tous les éléments React, y compris les autres, et permet également d'exposer leur clé.

Ainsi, les développeurs peuvent choisir d'envelopper l'élément enfant avec un nouvel élément et insérer de nouvelles props là, ou ils peuvent simplement fusionner les props avec React.

Supposons que nous avons un composant d'application qui utilise un useModal et offre la possibilité de gérer les modales en utilisant des contrôles tels que open, close, opened et activated. Avant de fusionner les props avec les enfants, nous pouvons les passer à un composant VisbilityControl qui fournit une fonctionnalité supplémentaire.

```react
import React from 'react'

const UserContext = React.createContext({
  user: {
    firstName: 'Kelly',
    email: 'frogLover123@gmail.com',
  },
  activated: true,
})

const VisibilityControl = ({ children, opened, close }) => {
  const ctx = React.useContext(UserContext)
  return React.cloneElement(children, {
    opened: ctx.activated ? opened : false,
    onClick: close,
  })
}

export const useModal = ({ urls } = {}) => {
  const [opened, setOpened] = React.useState(false)
  const open = () => setOpened(true)
  const close = () => setOpened(false)

  return {
    opened,
    open,
    close,
  }
}

const App = ({ children }) => {
  const modal = useModal()

  return (
    <div>
      <button type="button" onClick={modal.opened ? modal.close : modal.open}>
        {modal.opened ? 'Fermer' : 'Ouvrir'} la modale
      </button>
      <VisibilityControl {...modal}>{children}</VisibilityControl>
    </div>
  )
}

const Window = ({ opened }) => {
  if (!opened) return null
  return (
    <div style={{ border: '1px solid teal', padding: 12 }}>
      <h2>Je suis une fenêtre</h2>
    </div>
  )
}

export default () => (
  <App>
    <Window />
  </App>
)
```

L'utilisation du contrôle de visibilité permet aux développeurs de vérifier si le contrôle activé est vrai avant de permettre au contrôle ouvert d'être utilisé par les enfants. Dans le cas où la fonctionnalité de contrôle de visibilité est utilisée via une route secrète, il existe une option pour empêcher les utilisateurs non activés d'accéder au contenu. 


### 3. Créer un réducteur plus grand

Il est possible de combiner deux ou plusieurs réducteurs pour en faire un seul, beaucoup plus grand, qui peut aider à améliorer une application React.

Supposons que vous pensez à construire une grande application qui donne accès à une grande variété de petits services. Comment vous y prendriez-vous pour développer une telle application ? 

**Il y a deux options :**

1. Nous pouvons donner à chaque microservice au sein de l'application une partie séparée de son propre état et contexte qui peut être géré directement. 


2. Ou nous pouvons combiner tous les états en un seul grand état et les gérer tous dans le même environnement. 


> La première approche semble très fastidieuse, donc évidemment, la deuxième est la voie à suivre. 
> 

**Nous avons maintenant trois réducteurs à combiner -** 

frogsreducer.js, authreducer.js et enfin, ownersreducer.js. 


**Commençons par authReducer.js**

```react
const authReducer = (state, action) => {
  switch (action.type) {
    case 'set-authenticated':
      return { ...state, authenticated: action.authenticated }
    default:
      return state
  }
}

export default authReducer

ownersReducer.js
```

**ownersReducer.js**

```react
const ownersReducer = (state, action) => {
  switch (action.type) {
    case 'add-owner':
      return {
        ...state,
        profiles: [...state.profiles, action.owner],
      }
    case 'add-owner-id':
      return { ...state, ids: [...state.ids, action.id] }
    default:
      return state
  }
}

export default ownersReducer
```

**frogsReducer.js**

```react
const frogsReducer = (state, action) => {
  switch (action.type) {
    case 'add-frog':
      return {
        ...state,
        profiles: [...state.profiles, action.frog],
      }
    case 'add-frog-id':
      return { ...state, ids: [...state.ids, action.id] }
    default:
      return state
  }
}

export default frogsReducer
```

> Maintenant, nous pouvons mettre les trois dans le fichier principal de l'application et définir leur état : 
> 

**App.js**

```react
import React from 'react'
import authReducer from './authReducer'
import ownersReducer from './ownersReducer'
import frogsReducer from './frogsReducer'

const initialState = {
  auth: {
    authenticated: false,
  },
  owners: {
    profiles: [],
    ids: [],
  },
  frogs: {
    profiles: [],
    ids: [],
  },
}

function rootReducer(state, action) {
  return {
    auth: authReducer(state.auth, action),
    owners: ownersReducer(state.owners, action),
    frogs: frogsReducer(state.frogs, action),
  }
}

const useApp = () => {
  const [state, dispatch] = React.useReducer(rootReducer, initialState)

  const addFrog = (frog) => {
    dispatch({ type: 'add-frog', frog })
    dispatch({ type: 'add-frog-id', id: frog.id })
  }

  const addOwner = (owner) => {
    dispatch({ type: 'add-owner', owner })
    dispatch({ type: 'add-owner-id', id: owner.id })
  }

  React.useEffect(() => {
    console.log(state)
  }, [state])

  return {
    ...state,
    addFrog,
    addOwner,
  }
}

const App = () => {
  const { addFrog, addOwner } = useApp()

  const onAddFrog = () => {
    addFrog({
      name: 'giant_frog123',
      id: 'jakn39eaz01',
    })
  }

  const onAddOwner = () => {
    addOwner({
      name: 'bob_the_frog_lover',
      id: 'oaopskd2103z',
    })
  }

  return (
    <>
      <div>
        <button type="button" onClick={onAddFrog}>
          ajouter une grenouille
        </button>
        <button type="button" onClick={onAddOwner}>
          ajouter un propriétaire
        </button>
      </div>
    </>
  )
}
export default () => <App />

C'est à cela que ressemble la combinaison des trois réducteurs en un seul grand réducteur, avec rootReducer

function rootReducer(state, action) {
  return {
    auth: authReducer(state.auth, action),
    owners: ownersReducer(state.owners, action),
    frogs: frogsReducer(state.frogs, action),
  }
```

C'est à cela que ressemble la combinaison des trois réducteurs en un seul grand réducteur, avec rootReducer.

### Utilisation de Sentry pour analyser les erreurs

![Image](https://lh5.googleusercontent.com/ySh7MjcCdU2XUVc1GASq8HBz0ym9Yn3mQt8xP0fygcYWqf-UoSkOAV1gOxUSgOQ3o79FJb7R3P9iwIYngWY8MtNB6uAqHBh-UXY5gf_G-C9kN_Nuxx73iYllkPSqKKOSjDTXWvmb)

Tout projet de développement d'applications mobiles peut grandement bénéficier de [Sentry](https://sentry.io/welcome/). Il fournit tout ce dont un développeur a besoin pour gérer les erreurs et les exceptions lors de la création d'applications avec React. Sentry identifie toutes les erreurs et les affiche à un emplacement central afin qu'elles puissent être consultées et analysées en une seule fois.

Commencer avec Sentry sur React est facile. Il suffit d'utiliser npm install @sentry/browser et de le configurer. Une fois cela fait, les développeurs peuvent se connecter à sentry.io et analyser tous les rapports d'erreurs d'un projet sur un seul tableau de bord.

Les rapports d'erreurs de Sentry sont incroyablement détaillés. Ils fournissent toutes sortes d'informations importantes, y compris les informations sur l'appareil de l'utilisateur, le navigateur, l'URL, la trace de la pile, la manière dont l'erreur a été gérée, le code source, l'adresse IP, les traces pour retracer la source de l'erreur, le nom de la fonction d'erreur et bien plus encore. 


### 5. Utilisation d'Axios pour les requêtes HTTP

Bien que [Axios](https://github.com/axios/axios) soit couramment utilisé pour les requêtes HTTP, je pensais qu'il était important de mentionner ce point car il n'est en fait pas courant pour les développeurs d'utiliser d'autres bibliothèques de requêtes telles que fetch pour les applications React. 


Windows.fetch ne prend pas en charge Internet Explorer 11 (la plupart ne s'en soucient pas vraiment). Mais pour ce qu'il vaut, Axios fonctionne également là-bas et offre la possibilité d'annuler les requêtes en cours d'exécution. 


### Mots de la fin

Les 5 méthodes mentionnées peuvent grandement aider à accélérer votre application React. Cela aide les développeurs, l'entreprise dans laquelle vous êtes et, bien sûr, ceux qui l'utiliseront éventuellement. Mais honnêtement, le succès de votre application React dépend principalement de ceux qui travaillent dessus. 

En tant que consommateur, vous voulez de meilleures performances de votre application, donc c'est ce qui dénote le succès. En tant que développeur, ces méthodes pourraient rendre votre application plus facile à développer, et l'efficacité est la clé pour être plus productif. 

**ValueCoders est une entreprise experte en [externalisation informatique](https://www.valuecoders.com/) pour le développement de logiciels. Si vous cherchez des programmeurs React offshore ou [embaucher des développeurs Android](https://www.valuecoders.com/hire-developers/hire-android-developers), n'hésitez pas à nous contacter.** 

De plus, j'espère que cet article vous aide à apprendre de nouvelles choses et à obtenir une compréhension plus approfondie de ce qui entre dans la création de l'application React parfaite.