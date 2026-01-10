---
title: Apprendre l'API Dropbox en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-29T14:51:41.000Z'
originalURL: https://freecodecamp.org/news/learn-the-dropbox-api-in-5-minutes-fd4626a0df18
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KOiao8Wi7g8KSNP2HfxssA.png
tags:
- name: coding
  slug: coding
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Apprendre l'API Dropbox en 5 minutes
seo_desc: 'By Per Harald Borgen

  This article will teach you the bare minimum you need to know in order to start
  creating apps on top of the Dropbox API.

  Once you’ve read it, you can also check out our free course on the Dropbox API if
  you’re interested in learn...'
---

Par Per Harald Borgen

Cet article vous apprendra le strict minimum que vous devez savoir pour commencer à créer des applications sur la base de l'API Dropbox.

Une fois que vous l'aurez lu, vous pourrez également consulter notre [cours gratuit sur l'API Dropbox](https://scrimba.com/g/gdropbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gdropbox_5_minute_article) si vous êtes intéressé à en apprendre davantage. Dans ce cours, vous apprendrez à construire une application d'organisation des dépenses en utilisant JavaScript moderne.

![Cliquez sur l'image pour accéder à notre cours Dropbox](https://cdn-media-1.freecodecamp.org/images/1*J97tYIXjM5UqL14D6t5o_g.png)
_[Cliquez ici pour accéder au cours](https://scrimba.com/g/gdropbox?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gdropbox_5_minute_article)_

Cet article utilise JavaScript pour ses exemples, cependant, les SDK sont très similaires entre les langues, donc même si vous êtes par exemple un développeur Python, cela devrait toujours être pertinent.

### L'installation

Pour construire sur la base de Dropbox, vous avez d'abord besoin d'un compte Dropbox. Après vous être inscrit, rendez-vous dans la [section développeur](https://www.dropbox.com/developers). Choisissez **Mes applications** sur le côté gauche du tableau de bord et cliquez sur **Créer une application**.

Choisissez les paramètres suivants et donnez à votre application un nom unique.

![Paramètres préférés pour ce tutoriel](https://cdn-media-1.freecodecamp.org/images/1*yHT0o6DHnogmyF_V52H6kA.png)

  
Paramètres préférés pour ce tutoriel

Dans le tableau de bord, allez dans la section **OAuth 2** sous **Generated access token** et cliquez sur le bouton `Generate` pour obtenir un `accessToken` d'API, que nous sauvegarderons pour plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1*clo0wTB3M1kbKx03_P94mg.png)

Maintenant, installons [l'application de bureau Dropbox](https://www.dropbox.com/install). Connectez-vous à l'application avec vos nouvelles informations d'identification de développeur et vous devriez pouvoir voir un dossier portant le même nom que votre application nouvellement créée. Dans mon cas, c'est `LearnDbxIn5Minutes`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wavpsStgCIFOS8KMCYLQ9g.png)

Déposez quelques fichiers et images dans le dossier, afin que nous puissions y accéder via notre API.

### Installation et classe Dropbox initiale

Maintenant, installons la bibliothèque Dropbox dans notre projet.

`npm install dropbox`

# ou

`yarn add dropbox`

Importez Dropbox et créez `dbx` avec notre token et la bibliothèque de récupération passée dans notre instantiation de classe. Si vous préférez `axios` ou toute autre bibliothèque de récupération, n'hésitez pas à la passer à la place.

```js
import { Dropbox } from 'dropbox';

const accessToken = '<votre-token-du-tableau-de-bord>';

const dbx = new Dropbox({  
  accessToken,  
  fetch  
});

```

Notez que Dropbox est une importation nommée. La raison est qu'il existe d'autres sous-bibliothèques dans `'dropbox'`, par exemple, `DropboxTeam`, mais nous nous concentrerons uniquement sur `Dropbox` dans ce tutoriel.

### Obtenir des fichiers

La première méthode que nous allons examiner est celle pour obtenir des fichiers.

```js
dbx.filesListFolder({  
  path: ''  
}).then(response => console.log(response))

```

`filesListFolder()` prend un chemin vers le dossier cible et liste tous les fichiers à l'intérieur. Cette méthode retourne une promesse.

De plus, il est bon de garder à l'esprit que vous fournirez une chaîne vide `''` et non une barre oblique `'/'` pour accéder à la racine de notre application. Maintenant, la racine est **_la racine de notre dossier d'application_** et non celle du compte Dropbox. Nous pouvons toujours changer cette option dans les paramètres de notre application.

Lorsque nous exécutons notre code, la console doit enregistrer les entrées de notre dossier Dropbox :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xo3oiFNP0yOsaM5lf3oV5w.png)

### Obtenir plus de fichiers

Dans cette partie, nous allons examiner le chargement de fichiers supplémentaires, avec la possibilité d'implémenter une pagination ou une fonctionnalité de défilement infini.

À cette fin, Dropbox a un concept de `cursor`, qui indique notre position actuelle entre les fichiers que nous avons reçus et ceux qui doivent être envoyés.

Par exemple, nous avons un dossier avec 10 fichiers, et nous en avons demandé 5. Le curseur nous indiquera qu'il y a plus de fichiers à télécharger via la propriété `has-more: true` sur la `response`. Nous pouvons continuer à demander des fichiers en utilisant `filesListFolderContinue()` en passant `cursor` jusqu'à ce qu'il n'y ait plus de fichiers et que nous obtenions `has_more: false`.

```js
const getFiles = async () => {  
  const response = await dbx.filesListFolder({  
    path: '',   
    limit: 5  
  })

console.log(response)  
}

getFiles()

```

Lorsque nous examinons la réponse que nous avons obtenue dans la console, nous pouvons voir `has_more: true`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6McdcPYagsxhIxudRyaSxA.png)

Mettons à jour notre code pour gérer les cas où nous avons plus de fichiers à recevoir.

```js
const getFiles = async () => {  
  const response = await dbx.filesListFolder({  
    path: '',   
    limit: 5  
  })

// Nous pouvons effectuer une action personnalisée avec les fichiers reçus  
  processFiles(response.entries)

if (response.has_more) {  
    // fournir un rappel pour les nouvelles entrées reçues   
    // à traiter  
    getMoreFiles(response.cursor, more => processFiles(more.entries))  
  }  
}

getFiles()

```

Nous fournissons le curseur pour informer l'API des entrées que nous avons reçues, afin de ne pas recevoir les mêmes fichiers à nouveau.

```js
const getMoreFiles = async (cursor, callback) => {  
  // demander d'autres fichiers à partir de l'endroit où l'appel précédent s'est terminé  
  const response = await dbx.filesListFolderContinue({ cursor })

// si un rappel est fourni, nous l'appelons  
  if (callback) callback(response)

if (response.has_more) {  
    // s'il y a plus de fichiers, appeler getMoreFiles de manière récursive,  
    // en fournissant le même rappel.  
    await getMoreFiles(response.cursor, callback)  
  }  
}

```

Notez le rappel que nous fournissons à la fonction `getMoreFiles()`. C'est une astuce vraiment ingénieuse pour s'assurer que nos fichiers nouvellement reçus reçoivent le même traitement que leurs prédécesseurs.

En fin de compte, lorsqu'il n'y a plus de fichiers à obtenir, nous recevons `has_more: false`

![Image](https://cdn-media-1.freecodecamp.org/images/1*j3GUyu0YQZyNjSpSyivbSw.png)

Il est également intéressant de noter que l'appel récursif est implémenté ici pour la simplicité du tutoriel, plutôt que pour la performance de la fonction. Si vous avez de grandes quantités de données à charger, veuillez refactoriser cela dans une fonction plus performante.

### Obtenir des miniatures

La troisième méthode que nous allons étudier est celle pour obtenir des miniatures pour nos fichiers.

Pour demander des miniatures pour les fichiers téléchargés, nous pouvons appeler `filesGetThumbnailBatch()`.

```js
dbx.filesGetThumbnailBatch({  
  entries: [{  
    path: '',  
    size: 'w32h32',  
    format: 'png',  
  }]  
});

```

Ce point de terminaison est optimisé pour obtenir plusieurs miniatures et il accepte un tableau d'objets, où chaque objet peut avoir plusieurs propriétés spécifiées.

La propriété essentielle est `path`, qui présente les mêmes mises en garde que dans `filesListFolder()`.

Dans notre réponse, nous pouvons accéder à nos images via les propriétés `thumbnail`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HgcHIy5rGTmIGmCNL7THHA.png)

Vous pouvez voir que les miniatures ne sont pas retournées sous forme de liens, mais sous forme de chaînes très longues

c'est une image base64. Vous pourriez utiliser la chaîne dans votre HTML pour définir `src` de `<img>` à `"data:image/jpeg;base64, ${file.thumbnail}"`.

Et si je rendais ma réponse, j'obtiendrais ces chats incroyables !

![Image](https://cdn-media-1.freecodecamp.org/images/1*MgdZ4_iXNYjI70140uM9ag.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-GftuqkejQjWa4LqfbY1-Q.jpeg)

![Crédits image : Max Pixel (1, 2, 3)](https://cdn-media-1.freecodecamp.org/images/1*IiNGTxm4jlavgIEDm_PSMg.jpeg)

  
Crédits image : Max Pixel ([1](https://www.maxpixel.net/Tiger-Cat-Cat-Funny-Cat-Face-Domestic-Cat-Mieze-2306185), [2](https://www.maxpixel.net/Playful-Cat-Head-Young-Cat-Cat-Face-Pet-Black-Cat-205757), [3](https://www.maxpixel.net/Exhausted-Sleep-Cat-Cat-Face-Pet-White-Cat-1551783))

### Déplacer des fichiers

Enfin, nous allons couvrir le déplacement de nos fichiers d'un dossier à un autre.

Nous pouvons utiliser `filesMoveBatchV2()` pour déplacer nos fichiers par lots d'un dossier à un autre. Cette méthode fonctionne mieux lorsqu'elle est implémentée dans le cadre d'une fonction `async`.

La méthode accepte un tableau `entries` d'objets, qui se composent des propriétés `from_path` et `to_path`.

`filesMoveBatchV2()` retourne soit `success` si l'appel a immédiatement réussi, dans le cas où il n'y a que quelques fichiers à traiter. Cependant, pour des charges de travail plus importantes, il va retourner un objet avec une propriété `async_job_id`, et cela signifie que votre appel est en cours d'exécution et que nous devrons vérifier son état à une date ultérieure.

Nous pouvons utiliser `filesMoveBatchCheckV2()` pour continuer à vérifier l'achèvement de notre travail jusqu'à ce qu'il soit complet et ne soit plus `in_progress`.

```js
const entries = {  
  from_path: 'dossier_origine',  
  to_path: 'dossier_destination  
}

const moveFiles = async () => {  
  let response = await dbx.filesMoveBatchV2({ entries })  
  const { async_job_id } = response  
  if (async_job_id) {  
    do {  
      response = await dbx.filesMoveBatchCheckV2({ async_job_id })  
      // C'est ici que nous effectuons la mise à jour de l'état ou toute autre action.  
      console.log(res)  
    } while (response['.tag'] === 'in_progress')  
  }  
}

```

### Conclusion

Félicitations ! Vous avez maintenant une compréhension très basique de l'API Dropbox et de son SDK JavaScript.

Si vous souhaitez en savoir plus sur l'API Dropbox et construire une application sur celle-ci avec Vanilla JavaScript, assurez-vous de consulter notre [cours gratuit sur Scrimba](https://scrimba.com/g/gdropbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gdropbox_5_minute_article). Ce cours, ainsi que cet article, a été sponsorisé et payé par Dropbox. Ce parrainage aide Scrimba à garder les lumières allumées et permet de continuer à créer du contenu gratuit pour notre communauté tout au long de 2019. Un grand merci à Dropbox pour cela !

Bon codage :)