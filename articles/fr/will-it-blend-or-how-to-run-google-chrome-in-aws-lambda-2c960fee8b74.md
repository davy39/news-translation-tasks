---
title: Va-t-il mixer ? Ou comment exécuter Google Chrome dans AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-25T19:06:52.000Z'
originalURL: https://freecodecamp.org/news/will-it-blend-or-how-to-run-google-chrome-in-aws-lambda-2c960fee8b74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o58rXhdseqahhKzAsNvGiA.jpeg
tags:
- name: AWS
  slug: aws
- name: Google Chrome
  slug: chrome
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: Va-t-il mixer ? Ou comment exécuter Google Chrome dans AWS Lambda
seo_desc: 'By Slobodan Stojanovic

  Yes, you read that right: this article is about running Google Chrome (the browser)
  in AWS Lambda (the serverless computing platform). Why would anyone run a browser
  on the server[less] side? Is this some web version of “Will I...'
---

Par Slobodan Stojanovic

Oui, vous avez bien lu : cet article parle de l'exécution de Google Chrome (le navigateur) dans AWS Lambda (la plateforme de calcul serverless). Pourquoi quelqu'un exécuterait-il un navigateur côté serveur[less] ? Est-ce une version web de « [Will It Blend ?](https://en.wikipedia.org/wiki/Will_It_Blend%3F) » ?

Autant j'adorerais voir (ou faire) une série serverless « Will It Blend ? » qui exécute des choses étranges dans AWS Lambda, ce n'est pas le cas.

Mais alors, qu'est-ce que cet article ? Bon, c'est l'heure de l'histoire !

Il était une fois chez [Cloud Horizon](https://cloudhorizon.com), nous travaillons avec un client qui avait des SVGs étranges qui devaient être convertis en PNGs. Aucun des outils SVG-to-PNG ne fonctionnait, car les SVGs contenaient des éléments [`<foreignObject>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/foreignObject).

Ce problème aurait pu être résolu de nombreuses manières différentes. La solution optimale aurait été d'analyser pourquoi ils avaient des éléments HTML intégrés dans des fichiers SVG. Mais, comme c'est souvent le cas dans les projets réels, la raison était cachée derrière une pile de code hérité et de décisions héritées. Et, bien sûr, une solution était requise dès que possible.

La quête de la solution parfaite est devenue la quête de la solution décente la plus rapide dans les circonstances données.

Les objets étrangers dans les SVGs étaient des éléments HTML, et le meilleur outil pour afficher des éléments HTML est un navigateur. Mais comment pourrions-nous utiliser le navigateur pour résoudre ce problème ?

Manuellement, nous ouvririons un SVG dans le navigateur et prendrions une capture d'écran. Nous aurions dû pouvoir faire de même avec [PhantomJS](http://phantomjs.org), un WebKit sans tête scriptable avec une API JavaScript. Nous avons essayé, mais cela n'a pas fonctionné, en raison du manque de support pour les objets étrangers SVG dans PhantomJS.

Que pourrions-nous utiliser d'autre ? Imaginez utiliser Chrome de la manière dont nous utiliserions PhantomJS. Attendez ! Nous pourrions être capables de le faire. Quelqu'un de l'équipe avait récemment lu à propos de [Chrome sans tête](https://chromium.googlesource.com/chromium/src/+/master/headless/README.md). Cela semblait être l'outil parfait pour notre problème étrange. Nous avons essayé d'utiliser Chrome sans tête et cela a fonctionné !

### Résoudre le problème sans nuire à votre futur moi

Enfin, nous avions une solution viable. Mais nous devions trouver comment intégrer cette solution dans l'application du client sans ajouter une couche supplémentaire de code hérité futur.

Notre client utilisait AWS, et les fichiers SVG étaient dans le bucket Amazon S3. Cela nous a donné l'opportunité d'utiliser le **serverless** pour le convertisseur SVG en PNG.

Les solutions serverless sont économiques, et pour ce type de convertisseur, c'était gratuit, donc nous n'avions pas besoin de permission pour l'utiliser. Cela, et le fait que l'infrastructure n'avait besoin d'aucune configuration, nous a permis de nous déplacer rapidement. Une autre grande victoire était l'isolation, qui nous a permis de travailler sans comprendre le code hérité. De plus, notre convertisseur serverless serait facile à supprimer à l'avenir.

Une note rapide : **Serverless** est une méthode de déploiement et d'exécution d'applications sur une infrastructure cloud, sur une base de paiement à l'usage, et sans louer ou acheter de serveurs. Pour en savoir plus sur le serverless et son fonctionnement avec AWS, voir le premier chapitre gratuit de notre nouveau livre « Serverless Applications with Node.js » [ici](https://livebook.manning.com/#!/book/serverless-apps-with-node-and-claudiajs/chapter-1/v-5).

Comme le montre le diagramme ci-dessous, notre plan était le suivant :

1. Le client télécharge les SVGs dans le bucket S3 comme il le faisait auparavant.
2. S3 déclenche une fonction AWS Lambda.
3. À l'intérieur de la fonction Lambda, Node.js télécharge le SVG depuis le bucket S3 et démarre Chrome sans tête.
4. Chrome sans tête charge le SVG et prend la capture d'écran.
5. L'application Node.js télécharge ensuite l'image PNG de la capture d'écran dans le bucket S3.
6. Le client utilise l'image PNG depuis le bucket S3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lihQa40m17DpT8gSal35Cw.jpeg)
_Flux de l'application de captures d'écran serverless_

### Montrez-moi le code

Nous avons décidé d'utiliser Node.js, donc la première étape était de vérifier si Google Chrome pour AWS Lambda existait dans NPM. Nous n'avons pas été déçus : un package appelé [serverless chrome](https://github.com/adieuadieu/serverless-chrome) nous couvrait.

**Note** : AWS Lambda s'exécute sur Amazon Linux. Pour exécuter une bibliothèque tierce, telle que Google Chrome, vous devez la compiler en tant que binaire statique en utilisant Amazon Linux. Pour en savoir plus sur ce processus, consultez comment compiler et exécuter Pandoc sur AWS Lambda [ici](https://claudiajs.com/tutorials/pandoc-lambda.html).

Une autre pièce manquante était un moyen d'interagir avec Google Chrome dans AWS Lambda. La bibliothèque la plus populaire, [Puppeteer](https://github.com/GoogleChrome/puppeteer), semblait assez grande pour la tâche, donc nous avons utilisé [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface).

Reconstruisons le projet ensemble. Mais avant de faire cela, il y a deux prérequis :

* Vous devrez avoir Node.js avec npm installé.
* Vous devrez avoir un compte AWS et configurer les identifiants (voir comment faire [ici](https://claudiajs.com/tutorials/installing.html#configuring-access-credentials)).

Pour installer les deux dépendances, vous devez initier un nouveau projet Node.js et exécuter la commande suivante dans votre terminal :

```
npm install @serverless-chrome/lambda chrome-remote-interface --save
```

Cette fonction Lambda n'est pas grande, et vous pouvez la faire tenir dans un seul fichier et moins de 100 lignes de code. Mais, pour rendre notre fonction testable, nous utiliserons la structure montrée dans la figure ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XFrZhDzUvyviMlkqTxtg-w.jpeg)
_Structure des dossiers du projet_

**Comment testez-vous les fonctions serverless** ? Le concept est similaire à toute autre application Node.js : vous devez appliquer une [architecture hexagonale](http://alistair.cockburn.us/Hexagonal+architecture), et ensuite vous pouvez utiliser votre outil Node.js préféré pour les tests. Notre choix est [Jasmine](https://jasmine.github.io). Si vous voulez en savoir plus sur les tests des applications serverless, vous pouvez consulter le chapitre sur les tests de notre livre [ici](https://livebook.manning.com/#!/book/serverless-apps-with-node-and-claudiajs/chapter-11).

Dans notre structure, le fichier index.js gère simplement l'événement, le transmet à la fonction de conversion et répond. Ce fichier devrait ressembler à ce snippet de code :

Encore une fois, à des fins de test, la logique de conversion se trouve dans les fichiers suivants :

* `convert.js` : un fichier principal qui relie tous les autres fichiers.
* `download-from-s3.js` : une fonction qui télécharge le SVG depuis le bucket S3.
* `save-svg-and-get-dimensions.js` : une fonction qui sauvegarde le fichier SVG dans le dossier `/tmp` et lit ses dimensions.
* `screenshot-with-headless-chrome.js` : une fonction qui charge le fichier dans Chrome sans tête et prend la capture d'écran.
* `upload-to-s3.js` : une fonction qui télécharge une capture d'écran (fichier PNG) dans S3.

La plupart des fichiers sont simples, avec seulement quelques lignes de code. Mais pour garder cet article court, voyons les plus importants : `convert.js` et `screenshot-with-headless-chrome.js`.

Comme vous pouvez le voir dans le prochain snippet de code, la fonction de conversion fait ce qui suit :

1. Télécharge le fichier SVG depuis S3, en utilisant la fonction du fichier `download-from-s3.js`.
2. Prépare le chemin pour le fichier SVG dans le dossier `/tmp`, et invoque la fonction pour sauvegarder le fichier SVG et obtenir ses dimensions par défaut.
3. Ouvre le fichier SVG local dans Chrome sans tête et prend une capture d'écran en utilisant la fonction du fichier `screenshot-with-headless-chrome.js`.
4. Télécharge la capture d'écran dans le bucket S3 en utilisant la fonction du fichier `upload-to-s3.js`.

#### Exécution de Chrome sans tête

La dernière pièce importante de ce puzzle est l'exécution de Chrome sans tête. Pour ce faire, nous lancerons Chrome en utilisant le module `@serverless-chrome/lambda`, puis interagirons avec lui en utilisant le module `chrome-remote-interface`.

L'interface distante de Chrome obtient la liste de tous les onglets et se connecte au premier. Ensuite, elle active Page et Network pour le client.

Lorsque Page et Network sont prêts, l'interface distante de Chrome navigue vers l'URL que vous avez fournie (chemin local `file://` vers le fichier SVG), attend qu'il soit chargé et prend la capture d'écran.

Le code du fichier `screenshot-with-headless-chrome.js` devrait ressembler au snippet de code suivant :

Maintenant que le code est prêt, il est temps de le déployer sur AWS Lambda. Mais parce que Google Chrome est plus grand que la limite de 50 Mo sur AWS Lambda, le déploiement n'est pas aussi fluide que vous pourriez vous y attendre.

### Comment pouvons-nous faire entrer l'éléphant dans le coffre de la voiture ?

Avec les applications serverless, vous finissez souvent avec plus de code pour automatiser le déploiement que pour la logique métier de votre application. C'est un signe que le risque s'est déplacé vers le déploiement. Et donc, le processus de déploiement doit être bien testé et quelque chose en quoi vous pouvez avoir confiance.

Pour éviter les imprévus, nous utilisons [Claudia.js](https://claudiajs.com) pour le déploiement des applications serverless Node.js vers AWS Lambda et API Gateway.

Avec Claudia.js, nous ferions normalement simplement `claudia create --region eu-central-1 --handler index.handler`. Mais dans le cas de Chrome sans tête, cette commande échoue en raison de la taille du package que vous essayez de déployer.

AWS Lambda a une limite de 50 Mo sur la taille du package de déploiement pour les fichiers compressés. Heureusement, il y a aussi une limite de 250 Mo pour le code non compressé, que vous pouvez utiliser via un bucket S3. Le code est téléchargé dans le bucket S3 puis transféré vers la fonction AWS Lambda non compressé depuis là.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UTUBeVU8_brt6BHVtPeJRQ.jpeg)
_Comment pouvons-nous faire entrer l'« éléphant » dans le coffre de la voiture ?_

Pour ce faire avec Claudia, exécutez la commande suivante :

```
claudia create --region eu-central-1 --handler index.handler --memory 1024 --timeout 60 --use-s3-bucket S3_BUCKET_NAME
```

Notes importantes pour la commande précédente :

* Remplacez `S3_BUCKET_NAME` par le nom d'un bucket S3 que vous possédez. Vous pouvez en créer un nouveau et l'utiliser simplement comme assistant de déploiement.
* Choisissez n'importe quelle région qui vous est la plus proche, assurez-vous simplement que votre fonction Lambda est dans la même région que le bucket S3 d'assistance. Voir toutes les régions prises en charge [ici](https://docs.aws.amazon.com/general/latest/gr/rande.html#lambda_region).
* Si votre fichier principal est nommé différemment, vous devrez mettre à jour le gestionnaire dans la commande avec le nom du fichier avec `.handler` au lieu de l'extension `.js`. Par exemple, si le nom du fichier est `main.js`, votre gestionnaire serait `main.handler`.
* Augmentez un peu la mémoire par défaut, car même un Chrome sans tête a besoin de plus que les 128 Mo par défaut.
* Augmentez le délai d'attente (quelques secondes devraient suffire). Mais comme vous ne payez pas pour le délai d'attente, mais plutôt juste le temps d'exécution réel, vous pouvez mettre un peu plus, même autour de 5 minutes (max).

Quelques instants plus tard (selon votre vitesse Internet), vous devriez voir la confirmation que tout a été déployé avec succès.

**Note** : En cas de mise à jour de votre code, exécutez la commande `claudia update --use-s3-bucket S3_BUCKET_NAME`. Pour apprendre à utiliser Claudia.js, consultez la section tutoriel sur le [site web](https://claudiajs.com/tutorials/).

La dernière étape avant le test est de définir le déclencheur S3 pour votre fonction Lambda. Claudia vous couvre également pour cela. Exécutez simplement la commande suivante depuis votre terminal :

```
claudia add-s3-event-source --bucket S3_BUCKET --suffix svg
```

Encore une fois, remplacez `S3_BUCKET` par le nom du bucket S3 qui sera utilisé pour les fichiers SVG et PNG. Par défaut, le PNG sera sauvegardé dans le même dossier où se trouve le fichier SVG.

Et lorsque la commande s'exécute avec succès, c'est tout. Votre convertisseur de fichiers serverless est prêt.

### Test

Il est temps pour un [test](http://carhumor.net/wp-content/uploads/2011/11/car-joke-funny-humor-hatchback-cow-golf-trunk.jpg) !

Alors, comment testez-vous un convertisseur serverless ? Tout simplement en téléchargeant un fichier SVG dans votre bucket S3. Et ensuite ? Actualisez le bucket quelques secondes plus tard et vous verrez un fichier PNG avec le même nom. Vous serez surpris de la rapidité avec laquelle cela fonctionne ! Chrome sans tête semble être plus rapide que le navigateur Chrome sur ma machine. Peut-être devrais-je naviguer sur le web en mode sans tête à partir de maintenant. ?

### Conclusion

Donc, c'est ainsi que nous avons résolu le problème de notre client sans nuire à nos futurs moi. Ce n'est pas la meilleure solution, mais c'était la meilleure solution que nous avons pu trouver dans un court laps de temps et étant donné les circonstances.

Mais quel est le but de cette histoire ? Pourquoi devriez-vous vous soucier d'exécuter Chrome dans AWS Lambda si vous n'avez pas un client similaire ?

Il y a de nombreux cas d'utilisation potentiels. Si vous vous souvenez de la [pyramide de test](https://martinfowler.com/bliki/TestPyramid.html), les tests UI sont lents et coûteux. Mais que se passerait-il si vous pouviez exécuter quelques centaines ou même milliers d'entre eux en parallèle et ne payer que pour le temps d'exécution ? Il existe certains outils de test UI qui travaillent déjà sur une intégration similaire, tels que [Appraise](https://appraise.com).

![Image](https://cdn-media-1.freecodecamp.org/images/1*nbpelcvDBxIz7KJM6fJr9Q.jpeg)

J'espère que vous avez apprécié l'histoire. Attendez-vous à en voir plus bientôt !

_Comme toujours, un grand merci à mes amis [Aleksandar Simović](https://twitter.com/simalexan) pour leur aide et leurs commentaires sur l'article._

> _Toutes les illustrations sont créées à l'aide de l'application [SimpleDiagrams4](https://www.simplediagrams.com/)._

Aucune vache n'a été blessée lors de la rédaction de cet article.

Si vous voulez en savoir plus sur la construction et les tests d'applications serverless en utilisant Node.js et AWS, consultez « Serverless Applications with Node.js », le livre que j'ai écrit avec [Aleksandar Simovic](https://www.freecodecamp.org/news/will-it-blend-or-how-to-run-google-chrome-in-aws-lambda-2c960fee8b74/undefined) pour Manning Publications :

[**Serverless Applications with Node.js**](https://www.manning.com/books/serverless-applications-with-nodejs)
[_Une introduction convaincante aux déploiements serverless utilisant Claudia.js._www.manning.com](https://www.manning.com/books/serverless-applications-with-nodejs)

Le livre vous apprendra davantage sur les applications serverless, avec des exemples de code. Vous apprendrez comment construire et déboguer une API serverless réelle (avec base de données et authentification) en utilisant Node et Claudia.js. Et vous apprendrez comment construire des chatbots, pour Facebook Messenger et SMS (en utilisant Twilio), et des compétences Alexa.