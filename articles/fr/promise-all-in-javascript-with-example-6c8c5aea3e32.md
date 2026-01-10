---
title: Tout ce que vous devez savoir sur Promise.all
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T20:47:50.000Z'
originalURL: https://freecodecamp.org/news/promise-all-in-javascript-with-example-6c8c5aea3e32
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oPnpG64cvwTL8DHiaYSFew.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Tout ce que vous devez savoir sur Promise.all
seo_desc: 'By Srebalaji Thirumalai

  Promises in JavaScript are one of the powerful APIs that help us to do Async operations.

  Promise.all takes Async operations to the next new level as it helps you to aggregate
  a group of promises.

  In other words, I can say that...'
---

Par Srebalaji Thirumalai

Les promesses en JavaScript sont l'une des API puissantes qui nous aident à effectuer des opérations asynchrones.

Promise.all porte les opérations asynchrones à un nouveau niveau, car il vous permet d'agréger un groupe de promesses.

En d'autres termes, je peux dire qu'il vous aide à effectuer des opérations concurrentes (parfois gratuitement).

#### Prérequis :

Vous devez savoir ce qu'est une **Promise** en JavaScript.

#### Qu'est-ce que Promise.all ?

Promise.all est en fait une promesse qui prend un tableau de promesses en entrée (un itérable). Elle est résolue lorsque toutes les promesses sont résolues ou qu'une d'entre elles est rejetée.

Par exemple, supposons que vous avez dix promesses (opération asynchrone pour effectuer un appel réseau ou une connexion à une base de données). Vous devez savoir quand toutes les promesses sont résolues ou vous devez attendre que toutes les promesses soient résolues. Vous passez donc les dix promesses à Promise.all. Ensuite, Promise.all, en tant que promesse, sera résolue une fois que les dix promesses seront résolues ou qu'une des dix promesses sera rejetée avec une erreur.

**Voyons cela en code :**

```
Promise.all([Promise1, Promise2, Promise3])
 .then(result) => {
   console.log(result)
 })
 .catch(error => console.log(`Error in promises ${error}`))
```

Comme vous pouvez le voir, nous passons un tableau à Promise.all. Et lorsque les trois promesses sont résolues, Promise.all est résolue et le résultat est affiché dans la console.

**Voyons un exemple :**

```js
// Une promesse simple qui se résout après un temps donné
const timeOut = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(`Completed in ${t}`)
    }, t)
  })
}

// Résolution d'une promesse normale.
timeOut(1000)
 .then(result => console.log(result)) // Completed in 1000

// Promise.all
Promise.all([timeOut(1000), timeOut(2000)])
 .then(result => console.log(result)) // ["Completed in 1000", "Completed in 2000"]
```

Dans l'exemple ci-dessus, Promise.all est résolue après 2000 ms et le résultat est affiché dans la console sous forme de tableau.

Une chose intéressante à propos de Promise.all est que l'ordre des promesses est maintenu. La première promesse du tableau sera résolue en premier élément du tableau de sortie, la deuxième promesse sera le deuxième élément du tableau de sortie, et ainsi de suite.

**Voyons un autre exemple :**

```js
// Une promesse simple qui se résout après un temps donné
const timeOut = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(`Completed in ${t}`)
    }, t)
  })
}

const durations = [1000, 2000, 3000]

const promises = []

durations.map((duration) => {
  // Dans la ligne ci-dessous, deux choses se produisent.
  // 1. Nous appelons la fonction asynchrone (timeout()). À ce stade, la fonction asynchrone a démarré et entre dans l'état "pending".
  // 2. Nous ajoutons la promesse en attente à un tableau.
  promises.push(timeOut(duration)) 
})

console.log(promises) // [ Promise { "pending" }, Promise { "pending" }, Promise { "pending" } ]

// Nous passons un tableau de promesses en attente à Promise.all
// Promise.all attendra que toutes les promesses soient résolues avant de se résoudre.
Promise.all(promises)
.then(response => console.log(response)) // ["Completed in 1000", "Completed in 2000", "Completed in 3000"]

```

Dans l'exemple ci-dessus, il est clair que Promise.all attend que toutes les promesses soient résolues.

Voyons ce qui se passe si l'une des promesses est rejetée.

```js
// Une promesse simple qui se résout après un temps donné
const timeOut = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (t === 2000) {
        reject(`Rejected in ${t}`)
      } else {
        resolve(`Completed in ${t}`)
      }
    }, t)
  })
}

const durations = [1000, 2000, 3000]

const promises = []

durations.map((duration) => {
  promises.push(timeOut(duration)) 
})

// Nous passons un tableau de promesses en attente à Promise.all
Promise.all(promises)
.then(response => console.log(response)) // Promise.all ne peut pas être résolue, car l'une des promesses passées a été rejetée.
.catch(error => console.log(`Error in executing ${error}`)) // Promise.all génère une erreur.

```

Comme vous pouvez le voir, si l'une des promesses échoue, alors toutes les autres promesses échouent. Ensuite, Promise.all est rejetée.

Pour certains cas d'utilisation, vous n'en avez pas besoin. Vous devez exécuter toutes les promesses même si certaines ont échoué, ou peut-être pouvez-vous gérer les promesses échouées plus tard.

Voyons comment gérer cela.

```js
const durations = [1000, 2000, 3000]

promises = durations.map((duration) => {
  return timeOut(duration).catch(e => e) // Gestion de l'erreur pour chaque promesse.
})

Promise.all(promises)
  .then(response => console.log(response)) // ["Completed in 1000", "Rejected in 2000", "Completed in 3000"]
  .catch(error => console.log(`Error in executing ${error}`))
view raw
```

#### Cas d'utilisation de Promise.all

Supposons que vous devez effectuer un grand nombre d'opérations asynchrones comme l'envoi d'e-mails marketing en masse à des milliers d'utilisateurs.

Un simple pseudo-code serait :

```
for (let i=0;i<50000; i += 1) {
 sendMailForUser(user[i]) // Opération asynchrone pour envoyer un e-mail
}
```

L'exemple ci-dessus est simple. Mais il n'est pas très performant. La pile deviendra trop lourde et à un moment donné, JavaScript aura un grand nombre de connexions HTTP ouvertes qui peuvent tuer le serveur.

Une approche performante simple serait de le faire par lots. Prenez les 500 premiers utilisateurs, déclenchez l'envoi des e-mails et attendez que toutes les connexions HTTP soient fermées. Puis prenez le lot suivant pour le traiter, et ainsi de suite.

Voyons un exemple :

```js
// Fonction asynchrone pour envoyer un e-mail à une liste d'utilisateurs.
const sendMailForUsers = async (users) => {
  const usersLength = users.length
  
  for (let i = 0; i < usersLength; i += 100) { 
    const requests = users.slice(i, i + 100).map((user) => { // La taille du lot est de 100. Nous traitons par ensemble de 100 utilisateurs.
      return triggerMailForUser(user) // Fonction asynchrone pour envoyer l'e-mail.
       .catch(e => console.log(`Error in sending email for ${user} - ${e}`)) // Attrape l'erreur si quelque chose ne va pas. Ainsi, cela ne bloquera pas la boucle.
    })
    
    // requests contiendra 100 promesses en attente ou moins. 
    // Promise.all attendra que toutes les promesses soient résolues avant de prendre les 100 suivantes.
    await Promise.all(requests)
     .catch(e => console.log(`Error in sending email for the batch ${i} - ${e}`)) // Attrape l'erreur.
  }
}


sendMailForUsers(userLists)
```

Considérons un autre scénario : vous devez construire une API qui récupère des informations à partir de plusieurs API tierces et agrège toutes les réponses des API.

Promise.all est le moyen idéal pour le faire. Voyons comment.

```js
// Fonction pour récupérer les informations GitHub d'un utilisateur.
const fetchGithubInfo = async (url) => {
  console.log(`Fetching ${url}`)
  const githubInfo = await axios(url) // Appel API pour obtenir les informations de l'utilisateur depuis GitHub.
  return {
    name: githubInfo.data.name,
    bio: githubInfo.data.bio,
    repos: githubInfo.data.public_repos
  }
}

// Parcourt tous les utilisateurs et retourne leurs informations GitHub.
const fetchUserInfo = async (names) => {
  const requests = names.map((name) => {
    const url = `https://api.github.com/users/${name}`
    return fetchGithubInfo(url) // Fonction asynchrone qui récupère les informations de l'utilisateur.
     .then((a) => {
      return a // Retourne les informations de l'utilisateur.
      })
  })
  return Promise.all(requests) // Attend que toutes les requêtes soient résolues.
}


fetchUserInfo(['sindresorhus', 'yyx990803', 'gaearon'])
 .then(a => console.log(JSON.stringify(a)))

/*
Output:
[{
  "name": "Sindre Sorhus",
  "bio": "Full-Time Open-Sourcerer ·· Maker ·· Into Swift and Node.js ",
  "repos": 996
}, {
  "name": "Evan You",
  "bio": "Creator of @vuejs, previously @meteor & @google",
  "repos": 151
}, {
  "name": "Dan Abramov",
  "bio": "Working on @reactjs. Co-author of Redux and Create React App. Building tools for humans.",
  "repos": 232
}]
*/

```

En conclusion, Promise.all est le meilleur moyen d'agréger un groupe de promesses en une seule promesse. C'est l'une des façons d'atteindre la concurrence en JavaScript.

J'espère que vous avez aimé cet article. Si c'est le cas, applaudissez et partagez-le.

Même si ce n'était pas le cas, ce n'est pas grave, vous pouvez le faire quand même :P