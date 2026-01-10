---
title: 'Tourner autour du bloc : un débutant rencontre AWS Lambda'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-24T09:25:24.000Z'
originalURL: https://freecodecamp.org/news/running-around-the-block-a-beginner-meets-aws-lambda-560a1f2849ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nLepY9uWSldyknEje0Dm7A.jpeg
tags:
- name: beginner
  slug: beginner
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: 'Tourner autour du bloc : un débutant rencontre AWS Lambda'
seo_desc: 'By Janaka Bandara

  Computing! It sure has a very long, vivid (and sometimes awkward) history. Some
  key milestones include:


  The Egyptians, who slid a few marbles on a wooden frame to ease up a bit on their
  brains (and sweated the rest of their day ove...'
---

Par Janaka Bandara

L'informatique ! Elle a certainement une histoire très longue, vivante (et parfois maladroite). Voici quelques étapes clés :

* Les Égyptiens, qui [faisaient glisser quelques billes sur un cadre en bois](https://www.ee.ryerson.ca/~elf/abacus/history.html) pour soulager un peu leur cerveau (et [transpiraient le reste de leur journée](https://www.livescience.com/32616-how-were-the-egyptian-pyramids-built-.html) sur des tonnes de granit solide)
* Les Grecs et leur [Mécanisme d'Anticythère](https://simple.wikipedia.org/wiki/Antikythera_mechanism) qui pouvait suivre le mouvement des planètes avec une précision de [deux degrés par millénaire](http://mentalfloss.com/article/81445/15-intriguing-facts-about-antikythera-mechanism).
* La [Machine analytique](https://www.britannica.com/technology/Analytical-Engine) de Charles Babbage.
* Le [déchiffreur Enigma](https://www.iwm.org.uk/history/how-alan-turing-cracked-the-enigma-code) d'Alan Turing.
* La [calculatrice de poche de la NASA](http://www.computerweekly.com/feature/Apollo-11-The-computers-that-put-man-on-the-moon) qui a mis l'homme sur la lune.
* Deep Blue [battant](http://theconversation.com/twenty-years-on-from-deep-blue-vs-kasparov-how-a-chess-match-started-the-big-data-revolution-76882) Garry Kasparov, le Grand Maître des échecs.

![Image](https://cdn-media-1.freecodecamp.org/images/hoYHWyXUX5ppgnDovNpEddn3A3KXHcRr5f66)
_DSKY : l'ordinateur de guidage Apollo de la NASA_

Conformément à tout cela, les paradigmes des applications logicielles ont également évolué de manière spectaculaire. Partant de la programmation purement basée sur le matériel, en passant par les monolithes, la modularité, le SOA, le cloud, et maintenant... **serverless**.

À ce stade, « serverless » signifie généralement FaaS (functions-as-a-service). Et FaaS signifie littéralement [AWS Lambda](https://aws.amazon.com/lambda/), tant en termes de popularité que d'adoption.

Par conséquent, il n'est pas exagéré de prétendre que la popularité du développement serverless peut être liée à la facilité d'utilisation des Lambdas. Ou pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/dEyp2I-t39wUc79cPSMfjjCeJZFx-yZKUjkI)
_Lambda : à la tête de la révolution Serverless_

Eh bien, Lambda existe [depuis 2015](https://techcrunch.com/2014/11/13/amazon-launches-lambda-an-event-driven-compute-service/). Il est déjà intégré à une grande partie de l'écosystème AWS et est utilisé en production par des centaines (sinon des milliers) d'entreprises. Donc, Lambda devrait être assez intuitif et facile à utiliser, non ?

Eh bien, dans mon cas, il semblait que non.

Et puisque « mon cas » était l'un des exemples officiels d'AWS, je ne suis pas tout à fait convaincu que Lambda soit suffisamment convivial pour les nouveaux venus.

Pour commencer, je voulais implémenter le cas d'utilisation de création de vignettes d'AWS _sans_ suivre [leur propre guide](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-create-test-manually.html), pour voir jusqu'où je pourrais aller.

En tant que programmeur, j'ai naturellement commencé avec la [console de gestion Lambda](https://console.aws.amazon.com/lambda/home?region=us-east-1). Le code avait [déjà été écrit](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#Node.js) par les généreux développeurs d'AWS, alors pourquoi réinventer la roue ? Copier, coller, sauvegarder, exécuter. Voici !

Hmm, il semble que je doive grandir un peu.

L'assistant « Create function » était accrocheur, avec tant de modèles prêts à l'emploi. Dommage qu'il n'ait pas déjà l'exemple de génération de vignettes S3, sinon cette histoire aurait pu se terminer ici !

J'ai donc simplement continué avec l'option « Author from scratch », en utilisant le nom `s3-thumbnail-generator`.

Oh attendez, qu'est-ce que ce truc « Role » ? Il est également requis. Heureusement, il y a une option « Create new role from template(s) », qui sauvera ma journée.

Prenez-le facilement. « Role name » : `s3-thumbnail-generator-role`. Mais qu'en est-il du « policy template » ?

Peut-être devrais-je trouver quelque chose lié à S3, puisque mon Lambda est tout-S3.

Surprise ! La seule chose que j'obtiens lorsque je recherche S3 est « S3 object read-only permissions ». N'ayant pas d'autre option, je l'ai simplement prise. Voyons jusqu'où je peux aller avant de tomber à plat ventre !

Il est temps de cliquer sur « Create function ».

![Image](https://cdn-media-1.freecodecamp.org/images/XdeQrkR8r8OAwSBszA5z8p8skAQRtoOdmgF7)
_Assistant de création de fonction_

Wow, leur concepteur Lambda a l'air vraiment cool !

![Image](https://cdn-media-1.freecodecamp.org/images/2hFWFUF2f8ES5o0jh3FT74gRGCmBXweaiOg5)
_Éditeur AWS Lambda_

> « Félicitations ! Votre fonction Lambda 's3-thumbnail-generator' a été créée avec succès. Vous pouvez maintenant changer son code et sa configuration. Cliquez sur le bouton 'Test' pour entrer un événement de test lorsque vous êtes prêt à tester votre fonction. »

D'accord, il est temps pour ma mission copier-coller. « Copier » sur le [code source exemple](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#Node.js), `Ctrl+A` et `Ctrl+V` sur l'éditeur de code Lambda. Simple !

Tout est vert (pas de rouge). Bon à savoir.

« Sauvegarder », et « Test ».

![Image](https://cdn-media-1.freecodecamp.org/images/rc48wc7TF-bUFZrHVxrHZTMR1Khe9YXmiKmw)
_Configurer l'événement de test_

Oh, j'aurais dû savoir mieux. Oui, si je veux « Tester », j'ai besoin d'une « Entrée de test ». Évidemment.

Je savais que tester ma toute nouvelle Lambda ne serait pas aussi simple que cela. Mais je ne m'attendais pas à devoir mettre ensemble un événement sérialisé JSON _à la main_.

Heureusement, les développeurs d'AWS avaient également fait un excellent travail ici, en fournissant un modèle d'événement « S3 Put » prêt à l'emploi. Alors que pourrais-je sélectionner d'autre ?

![Image](https://cdn-media-1.freecodecamp.org/images/2Lr9YKQQT2Rctf-j5NCF2kKbE4FK1bHXhyOv)
_Événement de test S3 Put_

Comme prévu, la première exécution a été un échec :

```
{  "errorMessage": "Cannot find module 'async'",  "errorType": "Error",  "stackTrace": [    "Function.Module._load (module.js:417:25)",    "Module.require (module.js:497:17)",    "require (internal/module.js:20:19)",    "Object. (/var/task/index.js:2:13)",    "Module._compile (module.js:570:32)",    "Object.Module._extensions..js (module.js:579:10)",    "Module.load (module.js:487:32)",    "tryModuleLoad (module.js:446:12)",    "Function.Module._load (module.js:438:3)"  ]}
```

Damné, j'aurais dû remarquer ces lignes `require`.

Et, dans tous les cas, c'est de ma faute. La page où j'ai copié le code exemple avait un gros titre « Create a Lambda **Deployment Package** », et expliquait clairement comment regrouper l'exemple dans un zip déployable Lambda.

J'ai donc créé un répertoire local contenant mon code et le `package.json`, et j'ai exécuté un `npm install` (bonne chose que j'avais `node` et `npm` préinstallés !).

La construction, la compression et le téléchargement de l'application ont été assez faciles, et j'espérais ne pas avoir à passer par un million et un cycles pour faire fonctionner mon Lambda.

(En passant, je souhaite pouvoir faire cela dans leur éditeur intégré. Dommage que je n'ai pas pu trouver un moyen d'ajouter les dépendances.)

Quoi qu'il en soit, il est temps pour mon deuxième test.

```
{  "errorMessage": "Cannot find module '/var/task/index'",  "errorType": "Error",  "stackTrace": [    "Function.Module._load (module.js:417:25)",    "Module.require (module.js:497:17)",    "require (internal/module.js:20:19)"  ]}
```

`index` ? D'où cela vient-il ?

Attendez... ma faute, ma faute.

![Image](https://cdn-media-1.freecodecamp.org/images/sLDKR-O5FjrSBwAJ5L-daSbmVbaLgwpt-cTe)
_Avertissement 'index.js non trouvé'_

Il semble que le paramètre **Handler** conserve toujours la valeur par défaut `index.handler`. Dans mon cas, il devrait être `CreateThumbnail.handler` (`nomdefichier.méthode`).

Essayons à nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/WtyzRR53Dw1APp5Yv-qOF-cm76Gn4eWrhW7N)
_Succès !?_

Sérieusement ? Non, impossible !

Ah, oui. _Les logs ne mentent pas._

```
2018-02-04T17:00:37.060Z	ea9f8010-09cc-11e8-b91c-53f9f669b596  Impossible de redimensionner sourcebucket/HappyFace.jpg et de télécharger vers sourcebucketresized/resized-HappyFace.jpg en raison d'une erreur : AccessDenied: Accès refuséEND RequestId: ea9f8010-09cc-11e8-b91c-53f9f669b596
```

C'est juste. Je n'ai pas `sourcebucket` ou `sourcebucketresized`, mais probablement quelqu'un d'autre l'a. D'où le refus d'accès. Cela a du sens.

J'ai donc créé mes propres buckets, `s3-thumb-input` et `s3-thumb-inputresized`, j'ai édité mon entrée d'événement (grâce au menu déroulant « Configure test event ») et j'ai réessayé.

```
2018-02-04T17:06:26.698Z	bbf940c2-09cd-11e8-b0c7-f750301eb569  Impossible de redimensionner s3-thumb-input/HappyFace.jpg et de télécharger vers s3-thumb-inputresized/resized-HappyFace.jpg en raison d'une erreur : AccessDenied: Accès refusé
```

Accès refusé ? Encore ?

Heureusement, en me basant sur l'entrée de l'événement, j'ai compris que le 403 pourrait en fait indiquer une erreur 404 (non trouvé), puisque mon bucket ne contenait pas vraiment de fichier `HappyFace.jpg`.

Attendez, cher lecteur, pendant que je me précipite vers la console S3 et télécharge mon visage souriant dans mon nouveau bucket. Juste une minute !

D'accord, prêt pour le prochain tour de test.

```
2018-02-04T17:12:53.028Z	a2420a1c-09ce-11e8-9506-d10b864e6462  Impossible de redimensionner s3-thumb-input/HappyFace.jpg et de télécharger vers s3-thumb-inputresized/resized-HappyFace.jpg en raison d'une erreur : AccessDenied: Accès refusé
```

La même erreur exacte ? Encore ? Allons !

Cela n'avait pas de sens pour moi. Pourquoi diable mon propre Lambda, s'exécutant dans mon propre compte AWS, n'aurait-il pas accès à mon propre bucket S3 ?

Attendez, cela pourrait-il être lié à ce rôle d'exécution ? La partie où j'ai assigné aveuglément des permissions S3 en **lecture seule** ?

Un peu de recherche sur Google m'a conduit à la documentation extrêmement complète [AWS IAM pour Lambda](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html). Là, j'ai appris que Lambda s'exécute sous son propre rôle IAM. Je devrais configurer manuellement le rôle en fonction des services AWS que j'utiliserais.

Pire encore, pour configurer le rôle, je dois aller jusqu'à la [console de gestion IAM](https://console.aws.amazon.com/iam/home?#/roles). Heureusement, cela est déjà lié à partir du menu déroulant du rôle d'exécution. Plus important encore, cela s'ouvre dans un nouvel onglet.

![Image](https://cdn-media-1.freecodecamp.org/images/aednBBq8WoMpscVnm-pqURKv5yJyHOL6hxVj)
_Option de menu déroulant de rôle personnalisé_

Les doigts croisés, jusqu'à ce que la page de rôle personnalisé se charge.

![Image](https://cdn-media-1.freecodecamp.org/images/c1cXURfAUkhYWFo2mgOwKAu35Ce18aT2zUlq)
_Création de rôle personnalisé_

Oh non... Encore de l'édition JSON ?

Dans le guide original, les développeurs d'AWS semblaient avoir [réglé la partie rôle d'exécution](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-create-iam-role.html). Mais il était étrange qu'il n'y ait aucune mention de S3 (sauf dans le nom). Ont-ils oublié quelque chose ?

D'accord, pour la première fois de l'histoire, je vais créer mon propre rôle IAM !

Bénis soient ces ingénieurs AWS, une recherche rapide sur Google a révélé leur [générateur de politiques](https://awspolicygen.s3.amazonaws.com/policygen.html). Juste ce dont j'ai besoin.

Mais se débarrasser de la syntaxe JSON ne résout qu'une petite partie du problème. Comment puis-je savoir quelles permissions j'ai besoin ?

Google, mon ami ? Quelque chose ?

Ohh... Retour dans la documentation AWS ? Super...

Eh bien, ce n'était pas si mal, grâce au [guide des permissions S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html).

Bien que ce soit un peu écrasant, j'ai deviné que j'avais besoin de certaines permissions pour les « opérations sur les objets ». Heureusement, le document avait un joli tableau suggérant que j'avais besoin de `s3:GetObject` et `s3:PutObject` (cohérent avec les appels `s3.getObject(...)` et `s3.putObject(...)` dans le code).

![Image](https://cdn-media-1.freecodecamp.org/images/alTqcEqaCt7u9pAwTYGk2e8IzYS9GjowaKZu)
_Générateur de politiques AWS_

Après quelques réflexions, j'ai terminé avec une « IAM Policy » avec les permissions ci-dessus sur mon bucket (nommé avec la syntaxe fastidieuse `arn:aws:s3:::s3-thumb-input`) :

```
{  "Version": "2012-10-17",  "Statement": [    {      "Sid": "Stmt1517766308321",      "Action": [        "s3:PutObject"      ],      "Effect": "Allow",      "Resource": "arn:aws:s3:::s3-thumb-inputresized"    },    {      "Sid": "Stmt1517766328849",      "Action": [        "s3:GetObject"      ],      "Effect": "Allow",      "Resource": "arn:aws:s3:::s3-thumb-input"    }  ]}
```

Je l'ai collé et sauvegardé dans l'éditeur de rôle IAM (qui m'a automatiquement ramené à la page de la console Lambda — comme c'est gentil !)

Essayons à nouveau...

La même erreur ?!

En regardant à nouveau la documentation des permissions S3, j'ai remarqué que les permissions d'objet semblent impliquer un astérisque (`/*` suffixe, indiquant probablement les fichiers) sous le nom de la ressource. Essayons donc cela également, avec une nouvelle politique personnalisée :

```
{  "Version": "2012-10-17",  "Statement": [    {      "Sid": "Stmt1517766308321",      "Action": [        "s3:PutObject"      ],      "Effect": "Allow",      "Resource": "arn:aws:s3:::s3-thumb-inputresized/*"    },    {      "Sid": "Stmt1517766328849",      "Action": [        "s3:GetObject"      ],      "Effect": "Allow",      "Resource": "arn:aws:s3:::s3-thumb-input/*"    }  ]}
```

Encore ! (cela commence à ressembler à [Whiplash](https://www.youtube.com/watch?v=xDAsABdkWSc)) :

```
2018-02-04T17:53:45.484Z	57ce3a71-09d4-11e8-a2c5-a30ce229e8b7  Redimensionnement réussi de s3-thumb-input/HappyFace.jpg et téléchargement vers s3-thumb-inputresized/resized-HappyFace.jpg
```

WOO-HOO !!!

Croyez-le ou non, un fichier `resized-HappyFace.jpg` venait d'apparaître dans mon bucket `s3-thumb-inputresized` ! Oh yeah !

Maintenant, comment puis-je configurer mon Lambda pour qu'il s'exécute automatiquement lorsque je dépose un fichier dans mon bucket ?

Heureusement, la console Lambda (avec sa disposition intuitive « trigger-function-permissions ») a rendu cela très clair : ce que je voulais était un déclencheur S3. J'en ai donc ajouté un, avec « Object Created (All) » comme « Event Type » et « jpg » comme suffixe, j'ai tout sauvegardé et j'ai immédiatement déposé un fichier JPG dans mon bucket.

![Image](https://cdn-media-1.freecodecamp.org/images/R0zipGO8gM3-2mPVxuy1w4TiUHqjLP7U5F8N)
_Déclencheur ajouté_

Oui, cela fonctionne comme un charme.

Pour voir combien de temps le processus entier a pris (en exécution réelle, par opposition aux « tests »), j'ai cliqué sur le lien « logs » dans le panneau des résultats d'exécution (précédent), et je suis entré dans le « log stream » le plus récent affiché là. Rien !

Et plus suspect encore, le dernier log dans le flux de logs le plus récent était un log « access denied », bien que j'aie dépassé ce point et même réussi un redimensionnement.

Peut-être que mon dernier changement a cassé la capacité de journalisation du Lambda ?

Grâce à Google et [StackOverflow](https://stackoverflow.com/questions/37382889/cant-get-aws-lambda-function-to-log-text-output-to-cloudwatch), j'ai découvert que mon rôle d'exécution devait également contenir certaines permissions liées à la journalisation.

Maintenant, je me souviens qu'il y avait certaines permissions dans la zone de texte de l'éditeur de permissions lorsque j'ai commencé à créer mon rôle personnalisé. Une fois de plus, j'ai été assez ignorant pour coller mes politiques S3 directement par-dessus.

Un autre tour d'édition de politique :

```
{  "Version": "2012-10-17",  "Statement": [    {      "Sid": "Stmt1517766308321",      "Action": [        "s3:PutObject"      ],      "Effect": "Allow",      "Resource": "arn:aws:s3:::s3-thumb-inputresized/*"    },    {      "Sid": "Stmt1517766328849",      "Action": [        "s3:GetObject"      ],      "Effect": "Allow",      "Resource": "arn:aws:s3:::s3-thumb-input/*"    },    {      "Action": [        "logs:CreateLogGroup",        "logs:CreateLogStream",        "logs:PutLogEvents"      ],      "Effect": "Allow",      "Resource": "arn:aws:logs:*:*:*"    }  ]}
```

Un autre dépôt de fichier, et cette fois, le redimensionnement et les logs ont fonctionné sans faille... Enfin !

Maintenant que tout est réglé et que ma vignette m'attend dans mon bucket de destination, j'ai lancé mon navigateur, j'ai tapé `http://s3-thumb-inputresized.s3.amazonaws.com/resized-HappyFace.jpg` (conformément à la [documentation sur l'hébergement virtuel S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html)). J'ai appuyé sur Entrée, en attendant une belle vignette en retour.

```
<Error>  <Code>AccessDenied</Code>  <Message>Access Denied</Message>  <RequestId>C8BAC3D4EADFF577</RequestId>  <HostId>PRnGbZ2olpLi2eJ5cYCy0Wqliqq5j1OHGYvj/          HPmWqnBBWn5EMrfwSIrf2Y1LGfDT/7fgRjl5Io=</HostId></Error>
```

Déjà fatigué de ce message « AccessDenied » !

Apparemment, bien que mon code génère le fichier, il ne le rend pas accessible au public (mais à quoi servirait une vignette privée, hein ?)

En fouillant dans la documentation AWS, j'ai rapidement découvert le [paramètre `ACL`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#putObject-property) de l'opération `putObject`, qui permet au fichier téléchargé S3 d'être public. Espérant que cela résoudreait tous les problèmes de la planète, j'ai rapidement mis à jour mon code pour définir l'ACL du fichier sur `public-read` :

```
                s3.putObject({                  Bucket: dstBucket,                  Key: dstKey,                  Body: data,                  ContentType: contentType,                  ACL: 'public-read'                },                next);              }
```

J'ai sauvegardé la fonction et j'ai cliqué sur Test :

```
2018-02-04T18:06:40.271Z	12e44f61-19fe-11e8-92e1-3f4fff4227fa  Impossible de redimensionner s3-thumb-input/HappyFace.jpg et de télécharger vers s3-thumb-inputresized/resized-HappyFace.jpg en raison d'une erreur : AccessDenied: Accès refusé
```

Encore ?? Vous me faites marcher ?!

Heureusement, cette fois, je savais assez pour aller directement dans le [guide des permissions S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html), qui a rapidement révélé que je devais également avoir la permission `s3:PutObjectAcl` dans ma politique, afin d'utiliser le paramètre `ACL` dans mon appel `putObject`.

Un autre aller-retour vers l'éditeur de politiques, vers le tableau de bord IAM, et retour à la console Lambda.

```
2018-02-04T18:15:09.670Z	1d8dd7b0-19ff-11e8-afc0-138b93af2c40  Redimensionnement réussi de s3-thumb-input/HappyFace.jpg et téléchargement vers s3-thumb-inputresized/resized-HappyFace.jpg
```

Et cette fois, à ma grande satisfaction, le navigateur m'a joyeusement montré ma vignette de visage souriant lorsque j'ai saisi l'URL d'hébergement `http://s3-thumb-inputresized.s3.amazonaws.com/resized-HappyFace.jpg`.

Dans l'ensemble, je suis satisfait d'avoir finalement réussi à résoudre l'énigme par moi-même, en mettant toutes les pièces éparses ensemble.

Mais je ne peux m'empêcher d'imaginer à quel point ce serait cool si je pouvais construire mon Lambda en freestyle, avec AWS qui s'occupe des rôles, des permissions et autres, tout seul, sans me faire courir autour du bloc.

Peut-être aurais-je dû suivre ce guide officiel, dès le départ...

... mais, après tout, où est le plaisir dans tout cela ?! 😊