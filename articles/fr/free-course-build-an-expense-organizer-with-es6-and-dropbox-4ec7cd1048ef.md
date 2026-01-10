---
title: 'Cours gratuit : Créez un organisateur de dépenses avec ES6 et Dropbox'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-27T18:37:32.000Z'
originalURL: https://freecodecamp.org/news/free-course-build-an-expense-organizer-with-es6-and-dropbox-4ec7cd1048ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e-tlgkX_3RVuHm5CRth_tA.png
tags:
- name: dropbox
  slug: dropbox
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Cours gratuit : Créez un organisateur de dépenses avec ES6 et Dropbox'
seo_desc: 'By Per Harald Borgen

  In my previous startup, we used the Dropbox API heavily in our production process.
  Our products were children’s book apps for iPad, and each book was simply a collection
  of Dropbox folders containing all the visuals, music and vo...'
---

Par Per Harald Borgen

Dans ma précédente startup, nous utilisions fortement l'API Dropbox dans notre processus de production. Nos produits étaient des applications de livres pour enfants sur iPad, et chaque livre était simplement une collection de dossiers Dropbox contenant toutes les images, la musique et les voix off pour le livre. Cela avait deux grands avantages : cela fournissait à tout le monde une interface qu'ils savaient déjà utiliser, et c'était moins cher que de construire une interface personnalisée.

Ainsi, lorsque Dropbox a demandé à Scrimba si nous serions intéressés à créer un cours sponsorisé sur leur API, il n'y avait aucun doute dans nos esprits, car nous savions à quel point leur API peut être utile.

Deuxièmement, ce sponsoring nous permet également de créer encore plus de cours pour notre communauté tout au long de 2019. Nous sommes donc très reconnaissants à Dropbox de s'intéresser à soutenir Scrimba.

Maintenant, jetons un coup d'œil au [cours lui-même](https://scrimba.com/g/gdropbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gdropbox_launch_article).

### Introduction

L'instructeur de ce cours est [Christian Jensen](https://twitter.com/cbejensen), un développeur front-end basé dans l'Utah. Certains d'entre vous le connaissent peut-être grâce aux tutoriels React Hooks qu'il a créés sur Scrimba l'année dernière, et que beaucoup de gens ont appréciés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V4RAOA69TS3rFbjT5kqK2g.png)

Christian commence le cours en vous donnant un aperçu de ce que vous devriez savoir avant de commencer, et de ce que vous pouvez vous attendre à apprendre tout au long du cours.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E5solf68782pbf9pTyNozA.png)

En tant que prérequis pour le cours, il serait bon de connaître, mais ce n'est pas nécessaire, quelques bases de HTML et de JavaScript. Si vous n'êtes pas vraiment familier avec JS, vous pouvez toujours suivre ce cours, car l'API se traduit très bien dans d'autres langues.

L'objectif final du cours est de vous rendre capable de construire une application sur la base de dossiers Dropbox, illustrée par l'application d'organisateur de dépenses que Christian construit tout au long des leçons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_x-1lvglq1tezlSP1SUQAg.png)

C'est un exemple parfait de quelque chose qui est une source de beaucoup de tracas pour de nombreuses entreprises et freelances, à savoir le suivi des reçus !

### Installation

Avant de plonger dans le code, Christian nous donne un bref aperçu optionnel de l'installation pour ceux qui souhaitent exécuter l'application de ce tutoriel sur leur propre machine.

La première chose à faire est de [se rendre sur Dropbox](https://www.dropbox.com/developers). Sur le site web de Dropbox, allez dans **_Mes applications_** et choisissez **_API Dropbox_** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*AEdK8mMCUAFzP-ad5tvDaw.png)

Ensuite, nous choisissons le type d'accès **_Dossier d'application_**, juste pour voir comment cela fonctionne, et enfin, nous allons nommer notre application.

Après avoir cliqué sur le bouton **_Créer une application_** et après que notre application soit générée, nous voyons l'écran des paramètres.

Dans les paramètres, nous avons vraiment besoin uniquement de la section **_OAuth 2_** et sous **_Jeton d'accès généré_**, cliquez sur le bouton **_Générer_** pour obtenir un jeton d'accès que nous utiliserons dans la prochaine partie de notre tutoriel.

C'est tout !

### Importer le SDK

Dans ce cast, Christian nous montre comment importer le SDK et commencer à l'utiliser.

Une rapide note : même si dans ce cours le SDK JavaScript pour l'API Dropbox est utilisé, le SDK lui-même est essentiellement le même dans tous les langages de programmation.

Commençons par importer le SDK JavaScript.

```js
// notez que l'import est nommé  
import { Dropbox } from 'dropbox';

```

La classe est instanciée avec un objet de configuration, qui nécessite `accessToken` et une bibliothèque de récupération. Nous allons utiliser `fetch` dans le cours et vous pouvez obtenir votre `accessToken`, si vous le souhaitez, dans votre compte développeur Dropbox.

```js
import { Dropbox } from 'dropbox';

const dbx = new Dropbox({  
  accessToken: 'aeOL1E1HS0AAAAAAAAAALX6z1ogWy75HGE_HBN-NNpJNfhnEa1kjF1vsJ_t7Wf8k', 
  fetch  
})

```

Note : le `accessToken` ci-dessus a été révoqué, donc il est inutile d'essayer de l'utiliser dans votre propre code.

### Obtenir des fichiers

Jusqu'à présent, Christian nous a montré comment instancier une classe.

Une liste complète des méthodes de la classe peut être trouvée sur [la page de documentation officielle](https://dropbox.github.io/dropbox-sdk-js/Dropbox.html).

Dans ce cast, nous allons apprendre la méthode `filesListFolder()`. Elle accepte un dossier et commence à retourner le contenu du dossier.

```js
dbx.filesListFolder({  
  path: ''  
}).then(res => console.log(res))

// pour des résultats complets de console.log, visitez :  
// [https://scrimba.com/p/pnyeEhr/cGvvanuy](https://scrimba.com/p/pnyeEhr/cGvvanuy)

```

Il y a quelques choses à garder à l'esprit lorsque nous utilisons `filesListFolder()` :

* elle retourne une promesse.
* pour spécifier un chemin racine, nous devons spécifier une chaîne vide `''` et non `'/'`

### Rendre les fichiers

Dans cette leçon, Christian va nous montrer comment rendre les fichiers que nous obtenons de `filesListFolder()` du cast précédent. Il nous fournira un code de base en JavaScript vanilla pour nous aider à démarrer, afin que nous puissions nous concentrer sur la partie la plus intéressante de cette leçon : le rendu des fichiers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ej_T0WlW-8dYdh-jtfnrdg.png)

Écrivons la fonction `renderFiles()`, ensemble avec Christian.

Nous devons ajouter à `fileListElem.innerHTML` tous les fichiers triés par ordre alphabétique, en veillant à ce que nous placions les dossiers en premier. Nous mappons ensuite chaque dossier et fichier à un `<li>` et les joignons en utilisant `join('')` pour éviter de rendre un tableau au lieu d'une chaîne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jdGqIdyndF809yZP8HVb0Q.png)

Et voilà, notre liste de fichiers rendue !

![Image](https://cdn-media-1.freecodecamp.org/images/1*pf1rF4OQIMIOsnrMGefL6w.png)

### Rendre les miniatures

Dans ce screencast, Cristian va se concentrer sur le rendu des miniatures et nous allons voir comment obtenir des miniatures réelles de Dropbox dans la leçon suivante.

Nous allons modifier notre fonction `renderFiles()`. Dans la partie `.map`, nous pouvons vérifier si la miniature existe pour un fichier et l'utiliser, sinon, utiliser une miniature par défaut. Gardez à l'esprit que les dossiers n'ont pas de miniatures.

Les images par défaut seront fournies sous forme de chaînes base64, et si vous suivez le cours dans votre propre éditeur, [vous pouvez visiter le cast pour les copier](https://scrimba.com/p/pnyeEhr/ckMP6DTN?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gdropbox_launch_article).

![Image](https://cdn-media-1.freecodecamp.org/images/1*KqXU3cTOh2nPjM2ZhuKBgw.png)

Super, maintenant nous avons des miniatures par défaut rendues et dans le prochain cast, Christian va nous montrer comment rendre des miniatures réelles que nous pouvons obtenir de l'API Dropbox.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m6HDdcAVA7de0O2G_FN7CQ.png)

### Obtenir des miniatures

Comme Christian l'a promis dans la dernière leçon, nous allons maintenant rendre des miniatures réelles que nous pouvons obtenir de l'API Dropbox pour les fichiers qui en ont.

Nous allons ajouter et créer `getThumbnails()` à notre méthode `updateFiles()`.

```js
const updateFiles = files => {  
  state.files = [...state.files, ...files]  
  renderFiles()  
  getThumbnails(files)  
}

```

Pour obtenir des miniatures, nous pouvons utiliser un point de terminaison API existant :

```js
// [http://dropbox.github.io/dropbox-sdk-js/Dropbox.html](http://dropbox.github.io/dropbox-sdk-js/Dropbox.html)

dbx.filesGetThumbnailBatch({  
  entries: [{  
    path: '',  
    // taille préférée pour une miniature  
    size: 'w32h32'  
  }]  
})

```

Et voici la fonction `getThumbnails()` terminée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*J2wKfqbHgBRZeXh9HCWoag.png)

Si vous êtes intéressé par une visite détaillée ou souhaitez copier le code, n'hésitez pas à sauter dans [le cast lui-même](https://scrimba.com/p/pnyeEhr/cyNpzJAe?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gdropbox_launch_article).

### Async / Await

Jusqu'à présent, nous avons utilisé deux appels API qui retournent des promesses. Nous les avons résolus en utilisant `.then()` et dans ce screencast, Christian va nous montrer comment nous pouvons les refactoriser en utilisant `async/await`.

Pour utiliser `async/await`, nous déclarons `async` devant notre fonction et `await` avant notre appel API.

Regardons comment nous pouvons refactoriser notre fonction `init()`.

```js
const init = async () => {  
  const res = await dbx.filesListFolder({  
    path: '',  
    limit: 20  
  })  
  updateFiles(res.entries)  
}

```

Et maintenant, refactorisons `getThumbnail()` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yAvMbGfaT4c-g4Ir-eYtMA.png)

### Le curseur

Dans ce cast, nous allons apprendre le concept de curseur de Dropbox.

En termes d'API simples, le curseur est une indication de l'endroit où nous en sommes parmi nos fichiers.

Par exemple, vous avez 100 fichiers, et vous avez demandé les 20 premiers. Le curseur se déplacera vers le 21ème fichier et vous indiquera que vous avez plus de fichiers à télécharger via le champ `has_more: true`. Plus vous demandez de fichiers, plus le curseur avance jusqu'à ce qu'il vous indique qu'il n'y a plus de fichiers restants avec `has_more: false`.

Voici à quoi cela ressemblerait en réalité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pzE5UO7M7OlYYFjJkXwoaQ.png)

Vous pouvez utiliser la chaîne de curseur pour indiquer à l'API où se trouve le curseur, afin de ne pas recevoir les fichiers que vous avez déjà.

Dans la prochaine leçon, Christian nous montrera comment nous pouvons appliquer ce concept à notre application et utiliser le curseur pour obtenir plus de fichiers.

### Obtenir plus de fichiers

Mettons à jour la méthode `init()` pour charger d'autres fichiers s'il y en a, en vérifiant la propriété `has_more` sur notre réponse.

```js
const init = async () => {  
  const res = await dbx.filesListFolder({  
    path: '',  
    limit: 20  
  })  
  updateFiles(res.entries)  
  if (res.has_more) {  
    getMoreFiles(res.cursor, more => updateFiles(more.entries))  
  }  
}

```

Nous pouvons améliorer l'expérience utilisateur en ajoutant un message de chargement lorsque d'autres fichiers doivent être chargés.

```js
const loadingElem = document.querySelector('.js-loading')

const init = async () => {  
  const res = await dbx.filesListFolder({  
    path: '',  
    limit: 20  
  })  
  updateFiles(res.entries)  
  if (res.has_more) {  
    loadingElem.classList.remove('hidden')  
    getMoreFiles(res.cursor, more => updateFiles(more.entries))  
    loadingElem.classList.add('hidden')  
  } else {  
    loadingElem.classList.add('hidden')  
  }  
}

```

Maintenant, nous pouvons implémenter la fonction `getMoreFiles()`.

```js
const getMoreFiles = async (cursor, cb) => {  
  const res = await dbx.filesListFolderContinue({ cursor })

// nous vérifions si le callback est fourni et si oui - nous l'appelons  
  if (cb) cb(res)

if (res.has_more) {  
    // s'il y a plus de fichiers, appelez getMoreFiles de manière récursive,  
    // en fournissant le même callback.  
    await getMoreFiles(res.cursor, cb)  
  }  
}

```

### Changer le chemin du fichier

Wow, nous avons écrit un code vraiment amazing jusqu'à présent.

Une chose qui serait vraiment cool, c'est si nous n'étions pas si restreints au chemin racine tout le temps.

C'est exactement ce que nous allons apprendre dans ce cast.

Pour nous aider à démarrer, Christian a apporté quelques modifications au HTML et au CSS de notre application et le principal changement est le champ `Chemin du dossier`. C'est là que l'utilisateur peut spécifier le dossier auquel il souhaite accéder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gZAp61MtyVaDI0cXtRMwHg.png)

Nous pouvons faire fonctionner cela en écoutant l'événement de soumission sur `rootPathForm`, lorsque l'utilisateur nous indique où il veut aller. Nous vérifions ensuite leur entrée et empêchons les erreurs de base, comme l'utilisation de la mauvaise casse pour le nom d'un dossier. Nous devons également stocker la valeur de `rootPathInput` dans notre `state` pour pouvoir la réutiliser dans le reste de notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*03zOVoz5trfXiSOr2Zqitw.png)

### Déplacer des fichiers

Dans cette leçon, nous allons implémenter la fonction principale de notre application : la capacité à organiser nos fichiers dans des dossiers, en fonction de la date de modification.

Tout d'abord, nous devons ajouter un peu de code organisationnel, pour nous assurer que notre fonctionnalité principale est agréable pour nos utilisateurs avant d'implémenter `moveFilesToDatedFolders()`.

```js
const organizeBtn = document.querySelector('.js-organize-btn')

organizeBtn.addEventListener('click', async e => {  
  const originalMsg = e.target.innerHTML  
  e.target.disabled = true  
  e.target.innerHTML = 'Working...'  
  await moveFilesToDatedFolders()  
  e.target.disabled = false  
  e.target.innerHTML = originalMsg  
})

```

Ensuite, implémentons `moveFilesToDatedFolders()` qui utilisera `filesMoveBatchV2()` de Dropbox.

```js
// Implémentation de base de l'API.   
dbx.filesMoveBatchV2({  
  entries: [{  
    from_path: 'some_folder',  
    to_path: 'some_other_folder'  
  }]  
})

```

Bien sûr, nous n'allons pas utiliser de valeurs codées en dur dans notre application et Christian nous montrera comment générer le tableau `entries`, organisé par la valeur de la date de modification, afin que les noms des dossiers soient basés sur ces dates.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WiYmVjk9fjXrwCRezKGO8g.png)

### Afficher les fichiers déplacés

Dans le screencast précédent, Christian nous a montré comment déplacer des fichiers dans leurs propres dossiers en fonction de la date de modification et dans ce cast, nous apprenons comment affiner la fonctionnalité existante.

`filesMoveBatchV2()` retourne l'une des deux choses : `success` si l'appel a immédiatement réussi, et cela peut arriver si nous demandons à déplacer un ou deux fichiers. Cependant, il est plus probable qu'il retourne un objet avec une propriété `async_job_id`, et cela signifie que votre appel est en cours d'exécution.

Dans ce cas, nous pouvons utiliser `filesMoveBatchCheckV2()` pour vérifier l'achèvement de notre travail jusqu'à ce qu'il soit complet, ou en d'autres termes, qu'il ne soit pas `in_progress`.

C'est là que Christian nous aide à réécrire `moveFilesToDatedFolders()` en utilisant une boucle `do while`, dont la caractéristique clé est qu'elle est garantie d'être exécutée au moins une fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*46QxT5lsz3I1MQR4329fEA.png)

Il y a maintenant une chose de plus que nous devons faire : après que l'utilisateur ait déplacé les fichiers, nous voulons lui montrer à quoi ressemble le nouvel état, sans qu'il ait à actualiser la page.

Nous voulons essentiellement réutiliser ce morceau de fonctionnalité :

```js
state.files = []  
loadingElem.classList.remove('hidden')  
init()

```

Et extrayons-le dans une nouvelle méthode `reset()`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FA9mBlGKoqQ2jSCi_rQHwA.png)

Nous pouvons maintenant voir la fonctionnalité en action. Cliquez sur _'Organiser'_ et regardez tous nos fichiers être magiquement placés dans des dossiers. Voici un gif de son fonctionnement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mHskcCs411DZp9GVdFPj9Q.gif)

### Conclusion

C'est la fin du cours, alors félicitations pour l'avoir terminé ! Vous devriez maintenant être familier avec la façon d'obtenir des fichiers et des miniatures, et comment déplacer des fichiers en utilisant l'API Dropbox. De plus, vous aurez appris plusieurs concepts ES6.

Enfin, je tiens à remercier Dropbox pour avoir sponsorisé et payé cet article et le cours lui-même. Cela aide Scrimba à garder les lumières allumées et nous permet de créer plus de contenu gratuit pour notre communauté tout au long de 2019.

Bonne programmation :)