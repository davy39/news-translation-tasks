---
title: 'Firebase Cloud Functions : le bon, le moyen et le mauvais'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T18:24:33.000Z'
originalURL: https://freecodecamp.org/news/firebase-cloud-functions-the-great-the-meh-and-the-ugly-c4562c6dc65d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*P7XjBh6QtYZ5z7wJ.
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: '#firebase-cloud-functions'
  slug: firebase-cloud-functions
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: 'Firebase Cloud Functions : le bon, le moyen et le mauvais'
seo_desc: 'By Pier Bover

  When I reviewed Firebase last year, I complained that it wasn’t completely serverless.
  A Node server was still needed for common functionalities such as sending emails
  or creating thumbnails.

  Firebase Cloud Functions were announced a fe...'
---

Par Pier Bover

Lorsque [j'ai évalué Firebase](https://medium.freecodecamp.org/firebase-the-great-the-meh-and-the-ugly-a07252fbcf15) l'année dernière, je me suis plaint qu'il n'était pas complètement serverless. Un serveur Node était toujours nécessaire pour des fonctionnalités courantes telles que l'envoi d'e-mails ou la création de miniatures.

Les Firebase Cloud Functions ont été annoncées quelques mois plus tard. Le service est toujours en bêta, mais je l'utilise avec bonheur depuis quelques mois en production.

Voyons comment cela se passe.

### Qu'est-ce que les Firebase Cloud Functions ?

Si vous n'avez jamais entendu parler des cloud functions auparavant, le concept est assez simple. Déployez une logique concise sur un serveur sous forme de fonctions et des elfes diligents peuvent être magiquement invoqués depuis les limbes pour effectuer une tâche pour vous. Tout cela sans se soucier de l'infrastructure et en ne payant que pour les ressources d'exécution.

Dans de nombreux cas, ce nouveau paradigme peut simplifier l'écriture, la maintenance et l'exécution du code backend.

Les Firebase Cloud Functions en particulier sont comme des blocs Lego que vous pouvez connecter à n'importe quel service Firebase. Par exemple, une fonction peut être déclenchée lorsqu'une image est téléchargée sur Firebase Storage pour créer une miniature, ou peut-être nettoyer certaines données utilisateur lorsqu'un nœud est supprimé dans la Realtime Database. Pratiquement tout ce qui se passe dans Firebase peut déclencher une fonction.

Si cela ne suffit pas, vous pouvez également utiliser HTTP pour déclencher des fonctions avec GET, POST, etc. Consultez cette vidéo incroyable sur la façon de combiner Firebase Hosting avec Cloud Functions pour créer une application Express complète :

### Le Bon

#### L'infrastructure ne devient pas plus facile que cela

L'infrastructure est complètement abstraite pour vous, tout comme le reste de Firebase. Chaque fois qu'une fonction est déclenchée, un nouveau serveur virtuel prend vie, fait son travail et retourne dans les limbes. La magie de Google Cloud continuera à déclencher vos fonctions et à mettre à l'échelle l'infrastructure en fonction de la charge de travail automatiquement.

#### Tarification

Les cloud functions en général sont très rentables. Il est difficile de comparer les prix des fournisseurs de cloud, mais je peux dire que, selon mon expérience, les Firebase Cloud Functions ont été ridiculement bon marché. Il est difficile de croire que Google gagne de l'argent avec cela.

#### Facile à utiliser

Comme d'habitude avec Firebase et Google, la documentation est excellente et vous n'aurez pas à faire des acrobaties mentales pour comprendre. Il y a aussi [des tonnes d'exemples sur Github](https://github.com/firebase/functions-samples) pour vous aider à démarrer. L'authentification de déploiement est gérée par l'interface de ligne de commande Firebase, donc obtenir un hello world opérationnel est littéralement :

```
firebase init functions
firebase deploy
```

Je pense que la simplicité d'utilisation de Firebase et de Google Cloud en général est tout simplement géniale, surtout par rapport à la concurrence.

#### Flexible

Comme je l'ai écrit précédemment, ces fonctions peuvent être déclenchées par toutes sortes d'événements. Je parie que vous ne manquerez pas d'idées sur la façon de les intégrer à votre projet Firebase ou même au reste de votre stack.

Voici quelques problèmes que nous avons résolus en utilisant Firebase Cloud Functions :

* Générer des PDF pour un service de facturation en ligne en utilisant Phantom.js, et signer ces factures avec un service gouvernemental
* Connecter un service Go avec un fournisseur SOAP tiers (beurk)
* Envoyer des e-mails via HTTP depuis n'importe où dans notre stack

### Le Moyen

#### Démarrages à froid

La scalabilité est excellente, mais le temps d'exécution peut fluctuer considérablement. Une simple fonction hello world peut prendre 3 ms pour faire son travail, ou 100 ms.

```
functions.https.onRequest((request, response) => {
    response.send("Hello from Firebase!");
});
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7oLzO7vAtNeEChBQrYMpiA.png)

Ces fluctuations sont causées par les temps de démarrage des serveurs virtuels. Si le serveur virtuel qui exécute votre fonction est réveillé, la fonction se déclenchera instantanément. Mais si le serveur doit être démarré depuis les limbes, il aura évidemment besoin de plus de temps pour commencer à travailler. Dans le jargon des cloud functions, cela est appelé démarrages à chaud et à froid.

En pratique, vous ne pouvez pas compter sur des temps de réponse cohérents à moins de mettre en cache vos données, comme décrit dans la vidéo précédente, ou d'utiliser des astuces pour garder vos fonctions actives.

Malheureusement, les démarrages à froid sont un aspect inévitable de la gestion des cloud functions (de n'importe quel fournisseur). Vous devrez en tenir compte lorsque vous déciderez d'utiliser une cloud function pour résoudre quelque chose.

#### Pas de planificateur (cron)

Les cloud functions sont parfaites pour effectuer des tâches à faible trafic comme la génération de rapports ou la réalisation de sauvegardes périodiques à 2h du matin, mais avec Firebase ou Google Cloud, il n'y a pas de moyen facile de déclencher vos fonctions en fonction d'un calendrier.

L'équipe [Firebase recommande](https://github.com/firebase/functions-cron) de créer un projet App Engine pour orchestrer ces déclencheurs. Le service a vraiment besoin de quelque chose comme le [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler).

#### JavaScript uniquement

Eh bien, je suis d'accord avec JavaScript, mais Azure et AWS supportent beaucoup plus de langues. Il est ironique que Google ne supporte pas Go dans son service de cloud function, mais AWS le fait.

#### Node 6

Encore une fois, la concurrence fait mieux. AWS Lambda et Azure Functions fonctionnent déjà sur Node 8. Le plus gros inconvénient ici est de revenir aux promesses sans async/await ou de devoir configurer Babel sur votre projet.

### Le Mauvais

#### Workflow de développement

À l'exception des [fonctions déclenchées par HTTP](https://firebase.google.com/docs/functions/local-emulator#use_firebase_serve_for_https_functions), vous ne pouvez pas exécuter vos fonctions localement. Les fonctions déclenchées par un service Firebase doivent être déployées dans le cloud.

Cela a de nombreuses implications désagréables :

* Les petites erreurs finissent par coûter beaucoup de temps, car les nouvelles fonctions prennent quelques minutes à commencer à fonctionner.
* Les fonctions déployées n'ont pas de versions évidentes. Tous les logs de la même fonction semblent provenir de la même version. Il n'est jamais clair quand les nouvelles fonctions fonctionnent réellement, donc votre seul choix est de déclencher manuellement les fonctions et de voir ce qui se passe.
* Pas de retour en arrière

#### Environnements

En plus des points précédents, la gestion des environnements est... compliquée.

Vous pouvez ajouter des variables d'environnement à vos projets de fonctions en utilisant l'[interface de ligne de commande Firebase](https://firebase.google.com/docs/functions/config-env), mais, comme d'autres aspects de Firebase, cette approche est naïve et ne s'adapte pas bien.

Vous aurez besoin d'identifiants pour accéder à presque tout en dehors du bac à sable Firebase. Pour les autres services Google Cloud, ces identifiants se présentent sous la forme de fichiers `.json`. Multipliez cela par chaque environnement (développement, production, staging) et vous pouvez finir avec un royal bordel.

J'ai fini par renommer manuellement les fichiers d'identifiants avant le déploiement, ou pire, déployer tous les identifiants et sélectionner celui approprié à l'exécution. S'il vous plaît, faites-moi savoir dans les commentaires si vous avez trouvé un moyen de contourner cela.

J'adorerais voir un onglet _Environnement_ dans la console Firebase où je pourrais facilement gérer ces paramètres pour l'ensemble du projet Firebase. Le passage entre les environnements devrait être aussi facile que `firebase use production`.

### Conclusion

Mis à part quelques frictions pendant la phase de développement, mon expérience avec Firebase Cloud Functions a été positive. Une fois déployées, ces choses sont fiables et ne nécessitent aucune maintenance comme promis. Donc oui, Firebase est enfin complètement serverless. Hourra !

Si vous utilisez déjà Firebase, c'est vraiment une évidence. Les Firebase Cloud Functions sont un excellent complément pour votre projet, même si le service est encore en bêta.

D'un autre côté, il est juste de dire que la concurrence a un produit plus mature. Si vous n'êtes pas investi dans Firebase ou Google Cloud, et que vous envisagez d'utiliser des cloud functions dans votre stack, vous devriez probablement regarder ce que AWS ou Azure ont à offrir également.

Pour être complètement honnête, je suis un peu inquiet que le service soit encore en bêta. Cela fait plus d'un an qu'il a été annoncé et les progrès semblent douloureusement lents. La concurrence semble bien plus engagée dans ses produits cloud, même si, selon Diane Greene, PDG des entreprises cloud de Google, Google Cloud est le ["cloud à la croissance la plus rapide"](https://techcrunch.com/2018/02/01/googles-diane-greene-says-billion-dollar-cloud-revenue-already-puts-them-in-elite-company/).

C'est tout.

**Note :** Dans une version précédente de cet article, j'ai affirmé qu'il n'était pas possible d'écrire des tests pour les fonctions non HTTP. C'est faux, et [voici la documentation](https://firebase.google.com/docs/functions/unit-testing#testing_background_non_http_functions) sur la façon de le faire.