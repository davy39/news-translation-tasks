---
title: Comment planifier une tâche avec les Firebase Scheduled Cloud Functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-30T17:14:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-schedule-a-task-with-firebase-cloud-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/how-to-schedule-a-task-with-firebase-cloud-functions-1.png
tags:
- name: Cloud
  slug: cloud
- name: Firebase
  slug: firebase
seo_title: Comment planifier une tâche avec les Firebase Scheduled Cloud Functions
seo_desc: 'By Dragos Ivanov

  I work on an app that removes the background of any image.

  The app will have a freemium plan, which means that I will offer a free number of
  credits to all users, and if they need more credits, they will need to buy more.

  My Android ...'
---

Par Dragos Ivanov

Je travaille sur une application qui supprime l'arrière-plan de n'importe quelle image.

L'application aura un forfait freemium, ce qui signifie que j'offrirai un nombre gratuit de crédits à tous les utilisateurs, et s'ils ont besoin de plus de crédits, ils devront en acheter davantage.

Mes applications Android et iOS utilisent Firebase et les services Google Cloud comme App Engine et Google Storage.

L'une des questions que je me suis posées pendant le développement était : **« Comment pourrai-je réinitialiser les crédits gratuits chaque mois le 1er ? »**.

J'étais inquiet parce que je n'avais pas de plan – mais j'ai fini par trouver quelque chose.

Heureusement, Firebase propose des Scheduled Cloud Functions qui m'ont sauvé la mise.

Avant d'expliquer comment créer une fonction cloud planifiée, je veux vous parler de mon cas d'utilisation :

> _Le 1er de chaque mois, interroger tous les utilisateurs non payants de Firestore et mettre à jour leur nombre de crédits à un certain seuil, par exemple 20._

## De quoi avez-vous besoin pour créer une Firebase Scheduled Cloud Function ?

1. Un projet Firebase
2. [Installer la Firebase CLI](https://firebase.google.com/docs/cli) ou consulter les instructions ci-dessous
3. Node.js installé
4. Votre IDE préféré

Et voici une bonne nouvelle : vous n'avez besoin d'aucune expérience en développement backend pour suivre ce tutoriel et mettre cela en œuvre.

Commençons.

## Configuration du projet

Créez un nouveau dossier. Je l'appellerai `functions` pour cette démo. Il peut être à l'extérieur de votre projet actuel, ou vous pouvez créer un autre dossier à l'intérieur de votre projet déjà existant.

Pour installer les dépendances requises, dans votre nouveau dossier de projet, lancez la commande suivante :

`npm install -g firebase-tools`

La commande ci-dessus installera la Firebase CLI. Si vous n'êtes pas déjà connecté à un projet Firebase, vous pouvez lancer dans votre terminal `firebase login`.

Après vous être connecté à votre projet Firebase, depuis le terminal, lancez `firebase init`.

Cela créera tous les fichiers requis (.gitignore, index.js et package.json).

À l'intérieur du .gitignore, vous trouverez le dossier .node_modules ignoré.

Nous travaillerons à l'intérieur du fichier index.js.

Dans le package.json, nous trouverons quelques scripts que nous utiliserons plus tard.

Ci-dessous, vous pouvez voir la structure du dossier après la commande `firebase init`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-22.14.53.png)
_Structure du dossier après l'exécution de la commande firebase init_

## Codons !

Ouvrez votre fichier index.js et ajoutez le code suivant. Je suggère de ne pas copier le code, mais de l'écrire ligne par ligne pour mieux le comprendre.

```js
const functions = require("firebase-functions");
const firebase = require("firebase-admin");
firebase.initializeApp()
var firestore = firebase.firestore()

exports.resetCreditsForFreeUsers = functions.pubsub
    .schedule('0 0 1 * *')
    .onRun(async (context) => {
        const users = firestore.collection('users')
        const user = await users.where('isPayingUser', '==', false).get()
        user.forEach(snapshot => {
            snapshot.ref.update({ credits: 10 })
        })
        return null;
    })
```

Je pense que les quatre premières lignes sont explicites, mais laissez-moi vous expliquer un peu.

Les deux premières sont des imports. Dans la troisième, nous initialisons l'application Firebase, et dans la quatrième, nous accédons à l'objet Firestore.

`exports.resetCreditsForFreeUsers` est notre fonction.

```js
functions.pubsub
  .schedule('0 0 1 * *')
  .onRun(async (context) => {
  // ....
  return null; 
})
```

La partie ci-dessus nous aide à planifier notre code le 1er de chaque mois. Vous pouvez le configurer pour qu'il s'exécute chaque minute, toutes les 10 minutes ou quand vous le souhaitez. C'est incroyable !

### Comment trouver une expression de planification cron

J'ai trouvé un site Web appelé [crontab.guru](https://crontab.guru), qui vous aide et vous donne l'expression de planification dont vous avez besoin.

En jouant avec, j'ai trouvé que le moyen le plus simple de l'utiliser est d'aller sur Google, de rechercher votre expression, par exemple, « crontab every 20 minutes », et le premier résultat sera celui dont vous avez besoin.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-22.23.02.png)
_Le premier résultat Google était celui dont j'avais besoin._

Copiez la valeur que vous obtenez sur le site crontab.guru, */20 * * * * et passez-la dans la fonction .schedule.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-22.23.48.png)
_crontab guru peut vous aider à obtenir votre expression de planification_

Cela peut sembler confus car, au départ, j'ai parlé de faire une tâche planifiée le 1er de chaque mois, mais maintenant je mentionne toutes les 20 minutes.

Vous pouvez remplacer la valeur par n'importe quel cas d'utilisation que vous avez.

### Code qui s'exécute à l'intérieur de la fonction onRun

Le code ci-dessous, qui se trouve dans le callback onRun, interroge la collection Firestore « users » et recherche les utilisateurs ayant le champ `isPayingUser` à false, puis met à jour leurs crédits à 10. Plutôt simple, non ?

```js
const users = firestore.collection('users')
const user = await users.where('isPayingUser', '==', false).get()
user.forEach(snapshot => {snapshot.ref.update({ credits: 10 })})
```

Et c'est tout ce dont vous avez besoin côté code.

Maintenant, nous voulons déployer la cloud function.

## Déployer la Firebase Scheduled Cloud Function

Vous vous souvenez du package.json ? Vous y trouverez le script « deploy » grâce à la commande `firebase init` effectuée précédemment.

Dans votre terminal, lancez la commande : `npm run deploy`.

Une fois votre fonction déployée avec succès, vous devriez la voir disponible dans l'onglet Firebase appelé Functions.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-22.30.46.png)

Félicitations. Votre fonction planifiée est maintenant en ligne et s'exécutera chaque fois que vous en aurez besoin.

## Comment déboguer une Firebase Scheduled Cloud Function

Il existe peut-être de meilleures façons, mais voici une méthode simple que j'ai utilisée.

À l'intérieur de votre fonction onRun, vous pouvez ajouter le morceau de code suivant :

`functions.logger.info("Hello logs!");`

C'est l'équivalent de `console.log()` ou `println()`, mais pour les Firebase Cloud Functions.

Après avoir déployé votre fonction avec succès, vous verrez un certain nombre de logs dans l'onglet Firebase Logs.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-22.34.17.png)

Lorsque votre fonction s'exécute, et si elle contient l'appel functions.logger à l'intérieur de onRun, vous le verrez à chaque exécution de votre fonction.

## Conclusion

Nous sommes à la fin de ce tutoriel, et j'espère qu'il vous a été utile. Les Firebase Scheduled Cloud Functions m'ont aidé à réaliser ce que je voulais pour mon application.

J'écris du contenu technique pendant mon parcours pour atteindre 1000 $ de revenus passifs récurrents mensuels. Si vous voulez me soutenir ou lire ce que j'écris, [veuillez me suivre sur Twitter](https://twitter.com/dragos_ivanov).