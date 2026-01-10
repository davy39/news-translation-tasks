---
title: Pourquoi les Promesses Nues ne sont pas Sûres pour le Travail - et Que Faire
  à la Place
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-15T19:01:58.000Z'
originalURL: https://freecodecamp.org/news/naked-promises-are-not-safe-for-work
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0d5740569d1a4ca4b14.jpg
tags:
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Pourquoi les Promesses Nues ne sont pas Sûres pour le Travail - et Que
  Faire à la Place
seo_desc: 'By swyx

  This article goes through my personal journey of discovery and struggle adopting
  the conventional wisdom as it pertains to asynchronous work on the frontend. With
  any luck, you will come away with at least a deeper appreciation of 3 tricky ca...'
---

Par swyx

Cet article retrace mon parcours personnel de découverte et de lutte pour adopter la sagesse conventionnelle en ce qui concerne le travail asynchrone sur le frontend. Avec un peu de chance, vous repartirez avec au moins une appréciation plus profonde de 3 cas délicats à gérer lors du passage de la frontière synchrone à asynchrone. Et nous conclurons peut-être même que vous ne voudrez plus jamais gérer manuellement ces cas particuliers.

Mes exemples sont en React, mais je crois qu'ils sont des principes universels qui ont des parallèles dans toutes les applications frontend.

## Qu'est-ce qu'une "Promesse Nue" de toute façon ?

Pour faire quoi que ce soit d'intéressant dans notre application, nous utiliserons probablement une API asynchrone à un moment donné. En JavaScript, les Promesses ont dépassé les callbacks pour devenir l'API asynchrone de choix (surtout depuis que chaque plateforme a adopté `async`/`await`). Elles font même partie de la "plateforme Web" - voici un exemple typique utilisant l'API `fetch` basée sur les Promesses dans tous les navigateurs modernes :

```js
function App() {
  const [msg, setMsg] = React.useState('cliquez sur le bouton')
  const handler = () =>
    fetch('https://myapi.com/')
      .then((x) => x.json())
      .then(({ msg }) => setMsg(msg))

  return (
    <div className="App">
      <header className="App-header">
        <p>message : {msg}</p>
        <button onClick={handler}> cliquez-moi</button>
      </header>
    </div>
  )
}
```

Ici, la fonction `handler` de notre bouton retourne une Promesse "nue" - elle n'est enveloppée par rien, elle est simplement invoquée pour récupérer des données et définir l'état. C'est un modèle extrêmement courant enseigné dans toutes les introductions. Cela convient pour les applications de démonstration, cependant dans le monde réel, les utilisateurs rencontrent souvent de nombreux cas particuliers que ce modèle oublie commodément de prendre en compte.

## Les Promesses Échouent : L'État d'Erreur

Les Promesses échouent. Il est trop facile de ne coder que pour le "chemin heureux" où votre réseau fonctionne toujours et votre API retourne toujours un résultat réussi. La plupart des développeurs sont trop familiers avec les exceptions non capturées qui apparaissent uniquement en production et font sembler que votre application ne fonctionne pas ou est bloquée dans un état de chargement. Il existe [des règles ESlint pour s'assurer que vous écrivez des gestionnaires `.catch`](https://github.com/xjamundx/eslint-plugin-promise/blob/HEAD/docs/rules/catch-or-return.md) sur vos promesses.

Cela n'aide que pour les promesses que vous enchaînez avec un `.then`, mais n'aide pas lorsque vous passez une promesse à une bibliothèque que vous ne contrôlez pas, ou lorsque vous appelez simplement la promesse directement.

Dans tous les cas, la responsabilité d'afficher l'état d'erreur vous incombera finalement et ressemblera à ceci :

```js
function App() {
  const [msg, setMsg] = React.useState('cliquez sur le bouton')
  const [err, setErr] = React.useState(null)
  const handler = () => {
    setErr(null)
    fetch('https://myapi.com/')
      .then((x) => x.json())
      .then(({ msg }) => setMsg(msg))
      .catch((err) => setErr(err))
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>message : {msg}</p>
        {err && <pre>{err}</pre>}
        <button onClick={handler}>cliquez-moi</button>
      </header>
    </div>
  )
}
```

Nous avons maintenant deux états à gérer pour chaque opération asynchrone dans notre application !

## Promesses en Cours : L'État de Chargement

Lorsque vous pingez vos API sur votre machine locale ([par exemple, avec Netlify Dev](https://alligator.io/nodejs/solve-cors-once-and-for-all-netlify-dev/)), il est assez courant d'obtenir des réponses rapides. Cependant, cela ignore le fait que la latence de l'API peut être beaucoup plus lente dans le monde réel, en particulier dans les environnements mobiles. Lorsque le bouton est cliqué, la promesse est déclenchée, mais il n'y a aucun retour visuel dans l'interface utilisateur pour indiquer à l'utilisateur que le clic a été enregistré et que les données sont en transit. Les utilisateurs cliquent donc souvent à nouveau, au cas où ils auraient mal cliqué, et génèrent encore plus de requêtes API. C'est une terrible expérience utilisateur et il n'y a aucune raison d'écrire des gestionnaires de clics de cette manière, sauf que c'est le comportement par défaut.

Vous pouvez rendre votre application plus réactive (et moins frustrante) en offrant une forme d'état de chargement :

```js
function App() {
  const [msg, setMsg] = React.useState('cliquez sur le bouton')
  const [loading, setLoading] = React.useState(false)
  const handler = () => {
    setLoading(true)
    fetch('https://myapi.com/')
      .then((x) => x.json())
      .then(({ msg }) => setMsg(msg))
      .finally(() => setLoading(false))
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>message : {msg}</p>
        {loading && <pre>chargement...</pre>}
        <button onClick={handler} disabled={loading}>
          cliquez-moi
        </button>
      </header>
    </div>
  )
}
```

Nous avons maintenant **trois** états à gérer pour chaque opération asynchrone dans notre application : résultat, chargement et état d'erreur ! Oh là là.

## Les Promesses sont stupides : L'État du Composant

Une fois que les promesses sont déclenchées, elles ne peuvent pas être annulées. Ce fut une [décision controversée](https://medium.com/@benlesh/promise-cancellation-is-dead-long-live-promise-cancellation-c6601f1f5082) à l'époque, et bien que des solutions spécifiques à la plateforme comme [abortable fetch](https://developers.google.com/web/updates/2017/09/abortable-fetch) existent, il est clair que nous n'aurons jamais de promesses annulables dans le langage lui-même. Cela pose des problèmes lorsque nous déclenchons des promesses et que nous n'en avons plus besoin, par exemple lorsque le composant qu'elles sont censées mettre à jour a été démonté (parce que l'utilisateur a navigué ailleurs).

Dans React, cela provoque une erreur de développement uniquement comme :

```bash
Avertissement : Impossible de mettre à jour un composant monté ou en cours de montage. Cela signifie généralement que vous avez appelé setState, replaceState ou forceUpdate sur un composant démonté. Cela n'a aucun effet.

# ou

Avertissement : Impossible d'appeler setState (ou forceUpdate) sur un composant démonté. Cela n'a aucun effet, mais cela indique une fuite de mémoire dans votre application. Pour corriger cela, annulez tous les abonnements et les tâches asynchrones dans la méthode componentWillUnmount.
```

Vous pouvez éviter cette fuite de mémoire en suivant l'état de montage d'un composant :

```js
function App() {
  const [msg, setMsg] = React.useState('cliquez sur le bouton')
  const isMounted = React.useRef(true)
  const handler = () => {
    setLoading(true)
    fetch('https://myapi.com/')
      .then((x) => x.json())
      .then(({ msg }) => {
        if (isMounted.current) {
          setMsg(msg)
        }
      })
  }
  React.useEffect(() => {
    return () => (isMounted.current = false)
  })

  return (
    <div className="App">
      <header className="App-header">
        <p>message : {msg}</p>
        <button onClick={handler}>cliquez-moi</button>
      </header>
    </div>
  )
}
```

Nous avons utilisé une Ref ici, car [elle est plus proche du modèle mental d'une variable d'instance](https://medium.com/@pshrmn/react-hook-gotchas-e6ca52f49328), mais vous ne remarquerez pas trop de différence si vous utilisez `useState` à la place.

Les utilisateurs de React de longue date se souviendront également que [isMounted est un anti-modèle](https://reactjs.org/blog/2015/12/16/ismounted-antipattern.html), cependant le suivi de `_isMounted` en tant que variable d'instance est toujours recommandé si vous n'utilisez pas de promesses annulables. (Ce qui est TOUT. LE. TEMPS.)

Pour ceux qui comptent, nous en sommes maintenant à **quatre** états à suivre pour une seule opération asynchrone dans un composant.

## Solution : Il suffit de l'envelopper

Le problème devrait être assez clair maintenant :

Dans une simple démonstration, les promesses "nues" fonctionnent bien.

Dans une situation de production, vous allez vouloir implémenter tous ces états de gestion d'erreur, de chargement et de suivi de montage. Encore et encore.

Cela semble être un bon endroit pour utiliser une bibliothèque, n'est-ce pas ?

Heureusement, il en existe plusieurs.

Le hook `useAsync` de `react-async` vous permet de passer une `promiseFn`, ainsi que plusieurs options pratiques pour ajouter des callbacks et d'autres cas d'utilisation avancés :

```js
import { useAsync } from 'react-async'

const loadCustomer = async ({ customerId }, { signal }) => {
  const res = await fetch(`/api/customers/${customerId}`, { signal })
  if (!res.ok) throw new Error(res)
  return res.json()
}

const MyComponent = () => {
  const { data, error, isLoading } = useAsync({ promiseFn: loadCustomer, customerId: 1 })
  if (isLoading) return 'Chargement...'
  if (error) return `Quelque chose s'est mal passé : ${error.message}`
  if (data)
    return (
      <div>
        <strong>Données chargées :</strong>
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </div>
    )
  return null
}
```

Il inclut également un hook `useFetch` pratique que vous pouvez utiliser à la place de l'implémentation native de `fetch`.

`react-use` offre également [une implémentation simple de `useAsync`](https://github.com/streamich/react-use/blob/master/docs/useAsync.md), où vous passez simplement une promesse (aka une fonction `async`) :

```js
import { useAsync } from 'react-use'

const Demo = ({ url }) => {
  const state = useAsync(async () => {
    const response = await fetch(url)
    const result = await response.text()
    return result
  }, [url])

  return (
    <div>
      {state.loading ? (
        <div>Chargement...</div>
      ) : state.error ? (
        <div>Erreur : {state.error.message}</div>
      ) : (
        <div>Valeur : {state.value}</div>
      )}
    </div>
  )
}
```

Enfin, le `react-hooks-async` de Daishi Kato offre également un très bon contrôleur `abort` pour les promesses :

```js
import React from 'react'

import { useFetch } from 'react-hooks-async'

const UserInfo = ({ id }) => {
  const url = `https://reqres.in/api/users/${id}?delay=1`
  const { pending, error, result, abort } = useFetch(url)
  if (pending)
    return (
      <div>
        Chargement...<button onClick={abort}>Annuler</button>
      </div>
    )
  if (error)
    return (
      <div>
        Erreur : {error.name} {error.message}
      </div>
    )
  if (!result) return <div>Aucun résultat</div>
  return <div>Prénom : {result.data.first_name}</div>
}

const App = () => (
  <div>
    <UserInfo id={'1'} />
    <UserInfo id={'2'} />
  </div>
)
```

Vous pouvez également choisir [d'utiliser des Observables](https://medium.com/@benlesh/promise-cancellation-is-dead-long-live-promise-cancellation-c6601f1f5082), soit en enveloppant votre Promesse dans un Observable, soit en les utilisant directement.

Dans tous les cas, vous pouvez voir le modèle émergent selon lequel **vous voudrez toujours envelopper vos promesses** pour les utiliser en toute sécurité dans un environnement de production. À un niveau méta, ce qui se passe ici est que JavaScript vous permet d'appeler du code synchrone et asynchrone avec la même API exacte, ce qui est une contrainte de conception malheureuse. Cela signifie que nous avons besoin d'enveloppes pour traduire en toute sécurité l'exécution asynchrone en variables synchrones qui nous intéressent, en particulier dans un paradigme de rendu en mode immédiat comme React. Nous devons choisir soit de les écrire nous-mêmes à chaque fois, soit d'adopter une bibliothèque.

Si vous avez d'autres commentaires et cas particuliers auxquels je n'ai pas pensé, n'hésitez pas à [me contacter !](https://twitter.com/swyx)