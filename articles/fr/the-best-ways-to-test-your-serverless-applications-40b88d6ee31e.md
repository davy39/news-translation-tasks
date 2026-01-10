---
title: Les meilleures façons de tester vos applications serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-15T22:22:18.000Z'
originalURL: https://freecodecamp.org/news/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c3lCL2XzL9qOYV-kj4G2GA.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Les meilleures façons de tester vos applications serverless
seo_desc: 'By Slobodan Stojanovic

  Serverless is more than a cloud computing execution model. It changes the way we
  plan, build, and deploy apps. But it also changes the way we test our apps.

  Meet Alex. Alex is an ordinary JavaScript developer, focused on Node.j...'
---

Par Slobodan Stojanovic

Serverless est plus qu'un modèle d'exécution de cloud computing. Cela change la façon dont nous planifions, construisons et déployons des applications. Mais cela change aussi la façon dont nous testons nos applications.

Rencontrez Alex. Alex est un développeur JavaScript ordinaire, récemment concentré sur Node.js.

![Image](https://cdn-media-1.freecodecamp.org/images/MtalllczKaCqHXoYLjhWS-dsCuadSW0CSYJ4)
_Ceci est Alex_

Au cours des derniers mois, ses bons amis, Anna et Jeff, parlent toujours de cette chose serverless. Même s'ils sont parfois ennuyeux, il aime l'idée des applications serverless. Il a même déployé quelques fonctions simples sur AWS Lambda et Azure à un moment donné.

![Image](https://cdn-media-1.freecodecamp.org/images/W4arHIFaqZutDUYabYBKCAMZsnyVvctmT4G5)
_Anna et Jeff parlent toujours de cette chose serverless_

À un moment donné, Alex et son équipe ont obtenu un nouveau projet. Après une analyse, Alex a pensé que ce serait le cadre parfait pour serverless. Il a présenté l'idée à son équipe. Certains membres de l'équipe étaient excités, l'un d'eux n'aimait pas cela, mais la plupart n'avaient pas d'avis tranché. Ils ont donc décidé d'essayer - le projet n'était pas trop grand et le risque était faible.

![Image](https://cdn-media-1.freecodecamp.org/images/4SH3bquVOC81aS03e6CJcUwGSvaRHI7illvN)
_L'équipe d'Alex discute de l'utilisation de serverless sur leur nouveau projet_

L'équipe a lu sur serverless et ils ont eu une idée de la façon de structurer leur nouvelle application. Mais personne n'était sûr de la façon dont ils devaient intégrer serverless dans leur processus de développement commun.

À ce moment-là, leur processus ressemble à ceci :

1. Ils analysent une nouvelle fonctionnalité.
2. Pour les fonctionnalités moins complexes, ils commencent par le code, puis l'exécutent localement et ajoutent quelques tests à la fin.
3. Pour les fonctionnalités plus complexes, ils font leur version de TDD : ils commencent par les tests, puis écrivent le code et le testent localement.
4. Lorsque la fonctionnalité est prête, elle passe à l'outil CI qui la déploie dans l'environnement de test.
5. Ensuite, l'équipe QA prend une nouvelle fonctionnalité pour une autre série de tests manuels. Si tout semble bon, l'application passe par CI en production.

![Image](https://cdn-media-1.freecodecamp.org/images/3FiH7yO9EWUI6fIo0JG8IQppAbm-a2AvDfCq)
_Le processus de développement commun de l'équipe d'Alex_

Ils ont décidé de commencer étape par étape, puis de résoudre les problèmes au fur et à mesure qu'ils les rencontraient.

Ils ont choisi une petite fonctionnalité, et comme elle était simple, ils ont commencé par le code. Lorsque la partie codage était prête, ils ont rencontré le premier obstacle : comment exécuter des applications serverless localement ?

### Tests locaux

Avec les applications serverless, vous ne gérez pas l'infrastructure. Cela semble génial, mais comment exécuter votre application localement ? Pouvez-vous même faire cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/nS02sQWyNQjiJZN9R71AMMVYZ04rQSku9fes)
_Premier obstacle : comment exécuter une application serverless localement ?_

Selon votre application et le fournisseur serverless, vous pouvez exécuter certaines parties de votre application localement. Pour ce faire, vous pouvez utiliser certains des outils et techniques suivants :

* [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools) (pour les fonctions Azure)
* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli) (pour les applications AWS Lambda construites avec AWS SAM)
* Outils tiers (par exemple, [localstack](https://localstack.cloud))
* [docker-lambda](https://github.com/lambci/docker-lambda) pour la simulation locale d'AWS Lambda
* Exécuter une fonction Node.js localement

Bien sûr, la liste n'est pas exhaustive - il y a plus d'outils, et nous voyons de nouveaux outils presque tous les jours maintenant.

La plupart de ces outils ont certaines limitations. Ils peuvent simuler des fonctions serverless et quelques autres services, tels que API Gateway. Mais qu'en est-il des permissions, de la couche d'authentification et des autres services ?

Les tests locaux aident à valider rapidement que votre fonction fonctionne. Mais existe-t-il une meilleure façon de s'assurer que votre application serverless fonctionne comme prévu ? Oui, il y en a une. La première et plus importante étape est : écrire des tests.

Alex et son équipe ont donc essayé leur première fonction localement, et comme elle semblait fonctionner. Ensuite, ils sont passés à l'étape suivante.

### Tests automatisés

Alex et son équipe viennent de passer à [Jest](https://facebook.github.io/jest/) pour tester leurs applications Node.js. Ils font encore beaucoup de développement front-end, donc ils veulent utiliser les mêmes outils pour le full stack chaque fois qu'ils le peuvent. Peuvent-ils utiliser Jest pour tester les applications serverless aussi ? Et que devraient-ils tester ?

![Image](https://cdn-media-1.freecodecamp.org/images/fFyCbvZfkRQsbC-Pjse6tUul8djTl6hTstHt)
_Deuxième obstacle : comment serverless affecte-t-il les tests automatisés ?_

Après une rapide investigation, ils se sont rendu compte qu'ils pouvaient utiliser leurs outils de test Node.js préférés. Jest, Jasmine, Mocha et autres fonctionnent bien avec serverless.

#### Que devriez-vous tester dans une application serverless ?

Avec leurs applications Node.js, Alex et son équipe suivent la pyramide de test automatisé à trois niveaux. La pyramide de test a été mentionnée pour la première fois par Mike Cohn dans son livre « [Succeeding with Agile](https://www.amazon.com/gp/product/0321579364?ie=UTF8&tag=martinfowlerc-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0321579364) ».

Comme le définit la pyramide de test, ils ont :

* Beaucoup de tests unitaires, car ils sont les moins chers (les plus rapides à écrire et à exécuter)
* Moins de tests d'intégration, car ils sont plus coûteux et prennent plus de temps à exécuter
* Peu de tests UI, car ils sont les plus coûteux (nécessitent un outil GUI) et les plus lents à exécuter

En plus de ceux-ci, ils ont également des tests manuels basés sur des sessions, effectués par leur équipe QA.

![Image](https://cdn-media-1.freecodecamp.org/images/4mPvNp-TQMmpeAofZQdp5xnU4vSNZldSlqHn)
_[pyramide de test](https://martinfowler.com/bliki/TestPyramid.html" rel="noopener" target="_blank" title=") avec tests manuels_

Comment serverless affecte-t-il la pyramide de test automatisé ?

La réponse dépend du niveau. Mais la pyramide de test ressemble moins aux [pyramides égyptiennes](https://en.wikipedia.org/wiki/Egyptian_pyramids), et plus aux [pyramides mayas](https://en.wikipedia.org/wiki/Mesoamerican_pyramids#Mayan_pyramids).

Le niveau des tests unitaires n'est pas beaucoup affecté. Les tests unitaires sont toujours les moins chers à écrire et à exécuter, mais les unités peuvent être plus petites.

Le niveau des tests d'intégration devient plus important que jamais, car les applications serverless dépendent fortement des intégrations. C'est aussi moins cher, car avoir une base de données serverless juste pour les tests est bon marché. Donc, dans une pyramide de test « serverless », vous devez avoir plus de tests d'intégration.

Le niveau des tests GUI est aussi moins cher et plus rapide, grâce à une parallélisation moins chère.

Le niveau des tests manuels reste le même. Mais serverless peut vous aider à l'améliorer légèrement. Nous entrerons dans les détails plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/j0kvLDW4Tykdab9y8ZQMZ10gBAe81GmDLipn)
_Pyramide de test « serverless »_

Alex et son équipe avaient enfin une idée de là où se concentrer. Le problème suivant était comment écrire une fonction pour les tester plus facilement.

#### Comment écrire des fonctions serverless testables

Vous devez penser aux risques suivants lors de l'écriture d'une fonction serverless :

* **Risques de configuration** La base de données et la table sont-elles correctes ? Ou, avez-vous les droits d'accès ?
* **Risques de flux de travail technique** Analysez-vous et utilisez-vous la requête entrante comme vous le devriez ? Ou, gérez-vous les réponses réussies et les erreurs correctement ?
* **Risques de logique métier** Avez-vous suivi toutes les règles de logique métier que votre application a ?
* **Risques d'intégration** Lisez-vous correctement la structure de la requête entrante ? Ou stockez-vous correctement la commande dans la base de données ?

Pour confirmer que votre fonction serverless fonctionne correctement, vous devez tester tous ces risques.

Vous pourriez tester chacun de ceux-ci comme vous l'avez fait pour les tests d'intégration. Mais configurer et configurer le service chaque fois que vous voulez tester l'un de ces risques n'est pas optimal. Comme mon ami [Aleksandar Simovic](https://www.freecodecamp.org/news/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e/undefined) aime à dire :

> Imaginez si le test des automobiles était fait de cette manière. Cela signifierait que chaque fois que vous voulez tester une seule vis ou même un miroir dans une voiture, vous devriez assembler puis désassembler toute la voiture.

Pour rendre l'application plus testable, la solution claire est de diviser votre fonction en plusieurs fonctions plus petites.

L'une des meilleures façons de le faire est d'appliquer l'[Architecture Hexagonale](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjF8vPNsMnbAhXBVywKHSTxAskQFggmMAA&url=http%3A%2F%2Falistair.cockburn.us%2FHexagonal%252Barchitecture&usg=AOvVaw3e6eQDT3ptDvw8FnumhByp) à vos fonctions serverless.

L'Architecture Hexagonale, ou **Ports et Adapteurs**, est une forme d'architecture d'application qui promeut la séparation des préoccupations à travers des couches de responsabilité. Comme l'explique son créateur, [Alistair Cockburn](http://alistair.cockburn.us) :

> Permettre à une application d'être également pilotée par des utilisateurs, des programmes, des tests automatisés ou des scripts batch, et d'être développée et testée en isolation de ses dispositifs et bases de données d'exécution finaux.

Alors, comment cela s'applique-t-il aux fonctions serverless ?

Comme Alex et son équipe utilisent AWS, ils ont fini avec une structure comme suit :

* La logique métier de la fonction expose quelques « ports » (ou attend quelques arguments). Par exemple, un pour un événement entrant, un pour le stockage permanent, et un pour les notifications.
* Ils ont deux adapteurs pour l'événement qui déclenche une fonction, un pour le déclencheur AWS Lambda réel et un autre pour les tests locaux.
* Ils ont plusieurs adapteurs pour le stockage permanent et les notifications. Par exemple, un adapteur de table DynamoDB et un adapteur en mémoire.

![Image](https://cdn-media-1.freecodecamp.org/images/chFxK8htCl5K2QOkoBOCnXv18f4xCI47okvJ)
_Architecture hexagonale d'une fonction AWS Lambda_

Alex et son équipe étaient heureux de progresser. Mais avant de continuer, voyons comment l'Architecture Hexagonale affecte chaque niveau de la pyramide de test.

#### Tests unitaires

Les tests unitaires sont restés les mêmes. Mais il est plus facile d'écrire des tests unitaires grâce à l'Architecture Hexagonale. Ils peuvent simplement utiliser un adapteur local ou un mock comme adapteur pour tester la couche métier de la fonction en isolation.

#### Tests d'intégration

Les tests d'intégration ont grandement bénéficié de l'Architecture Hexagonale. Ils ont pu tester pleinement les intégrations qu'ils possèdent. Les intégrations tierces sont simulées avec d'autres adapteurs.

Comment cela fonctionne-t-il en pratique ?

Chacune de leurs fonctions serverless a des fichiers _lambda.js_ et _main.js_. Le fichier principal contient la logique métier d'une fonction serverless. Et le fichier _lambda.js_ est responsable de la connexion des adapteurs et de l'invocation du fichier _main.js_.

Le fichier principal a ses propres tests unitaires et d'intégration. Mais ses tests d'intégration ne testent pas l'intégration complète avec les services finaux, tels qu'AWS S3, car cela les ralentirait. Au lieu de cela, ils utilisent un adapteur en mémoire pour tester la fonction avec l'intégration de stockage de fichiers.

L'intégration AWS S3 est effectuée via le _FileRepository_, qui a ses propres tests unitaires et d'intégration. Les tests d'intégration vérifient l'utilisation d'AWS S3 pour être sûr que l'intégration finale fonctionne réellement.

Contrairement à _main.js_, le fichier _lambda.js_ n'a pas de tests, car la plupart du temps il n'a que quelques lignes de code.

![Image](https://cdn-media-1.freecodecamp.org/images/eokIvJ-PIBMhzLPIoNFu7qThfVsmwQjiGtWS)
_Représentation visuelle d'une seule fonction AWS Lambda avec des tests_

Cette approche est similaire à la technique que l'équipe [MindMup](https://www.mindmup.com) utilise pour tester les fonctions serverless. Avec elle, vous pouvez facilement tester les intégrations de vos fonctions, et rendre vos tests d'intégration plus rapides.

#### Tests GUI

Comme Alex et son équipe construisaient un back-end pour l'application, le niveau des tests GUI n'était pas pertinent. Mais à mesure qu'ils en apprenaient davantage sur serverless, ils se sont rendu compte qu'ils pouvaient l'utiliser pour améliorer le niveau des tests GUI pour les autres applications sur lesquelles ils travaillaient.

Les tests UI sont coûteux et lents, car ils s'exécutent dans le navigateur. Mais serverless est bon marché et il se met à l'échelle rapidement.

S'ils pouvaient exécuter un navigateur dans AWS Lambda, ils gagneraient une parallélisation bon marché. Cela rendrait leurs tests UI moins chers et plus rapides.

Mais peut-on exécuter un navigateur, comme Chrome, à l'intérieur d'une fonction serverless ?

Oui ! Et c'est facile avec l'aide d'outils tels que [Serverless Chrome](https://github.com/adieuadieu/serverless-chrome), [Chromeless](https://github.com/prismagraphql/chromeless), et [Puppeteer](https://github.com/GoogleChrome/puppeteer).

![Image](https://cdn-media-1.freecodecamp.org/images/5eoKemm0zOuNq3KphM3a6exI-WwjZxffmFe6)
_Utilisation des fonctions AWS Lambda pour la parallélisation des tests UI_

Une combinaison de serverless et de navigateurs sans tête peut nous apporter une nouvelle génération d'outils de test UI. Nous pouvons déjà voir et essayer certains d'entre eux, comme [Appraise](http://appraise.qa).

### CI / CD

Alors qu'Alex et son équipe testaient leur première fonction serverless, il était temps de déployer le code dans l'environnement de test. Cela a soulevé une nouvelle question : comment peuvent-ils utiliser des outils CI/CD pour déployer leur application serverless ?

![Image](https://cdn-media-1.freecodecamp.org/images/t2czuwldXzmq1WQJyz9z4bcH-zcEHjvtRPAX)

La réponse est simple : ils peuvent utiliser un outil CI pour exécuter les tests et déployer l'application. Pour déployer l'application, utilisez n'importe quel outil populaire, tel que [Claudia.js](https://claudiajs.com), [AWS SAM](https://github.com/awslabs/serverless-application-model), et [Serverless Framework](https://serverless.com).

Vous pouvez toujours utiliser votre outil CI préféré (comme [Jenkins](https://jenkins.io), [TravisCI](https://travis-ci.org) ou [SemaphoreCI](https://semaphoreci.com)), ou si vous voulez rester avec AWS, vous pouvez essayer [AWS CodeBuild](https://aws.amazon.com/codebuild/).

### Tests manuels

Même si les tests manuels ne sont pas directement affectés par serverless, l'équipe a trouvé un moyen d'améliorer leur processus QA.

![Image](https://cdn-media-1.freecodecamp.org/images/iKbkUkU7K9X0TFyMDArE3df68GjSG-3peTgK)

Les étapes et les déploiements des applications serverless sont bon marché et souvent rapides à configurer. De plus, avec serverless, vous ne payez pas pour l'application si personne ne l'utilise.

Cela signifie que avoir un environnement de test n'a jamais été aussi bon marché !

De plus, avec serverless, vous pouvez souvent _promouvoir_ la fonction d'une étape à une autre. Cela signifie que votre équipe QA peut tester une fonction, et lorsqu'ils confirment qu'elle fonctionne, vous pouvez promouvoir la même fonction en production.

### Au-delà des tests

Alex et son équipe ont livré leur première fonction serverless en pré-production, et l'équipe était heureuse d'avoir appris à tester les applications serverless.

![Image](https://cdn-media-1.freecodecamp.org/images/5ctT2IR50soRZdzNTojzOv-07ddy6ThSKsS2)

Ils ont continué à utiliser serverless sur le projet, et l'ont introduit dans quelques autres projets. Alex a rejoint ses amis Anna et Jeff, en tant que troisième, parfois ennuyeux, prédicateur serverless. Et ils vécurent heureux pour toujours.

![Image](https://cdn-media-1.freecodecamp.org/images/fkvnvW6w0JSsdN1R6HrDbzkBgviZ12wNHI3e)
_L'équipe des prédicateurs serverless a un nouveau membre_

### Post-scriptum

Mais même si leur application était bien testée, quelque chose s'est passé pendant la nuit.

Après une investigation, ils ont découvert qu'une des intégrations avait changé. Ils ont appris que les tests sont importants pour les applications serverless, mais que ce n'est pas suffisant.

Comme les applications serverless dépendent fortement des intégrations, le risque se déplace de votre code vers les intégrations. Et, pour pouvoir détecter les changements d'intégration et réagir rapidement, votre application a besoin d'une surveillance appropriée.

Heureusement, il y a de plus en plus d'outils de surveillance serverless sur le marché chaque jour. Certaines des bonnes et populaires options sont [IOpipe](https://www.iopipe.com), [Thundra](https://www.thundra.io), [Dashbird](https://dashbird.io), et [Epsagon](https://www.epsagon.com).

Mais, les applications serverless ont souvent un client épais, ce qui signifie que la surveillance du back-end n'est pas suffisante. Vous avez besoin d'un outil similaire pour votre front-end. Ce marché a aussi beaucoup de bons outils, comme [Sentry](https://sentry.io) et [Rollbar](https://rollbar.com).

Mais dans l'esprit de serverless, nous avons créé une application open source de suivi des erreurs appelée [Desole](https://desole.io). C'est une application serverless que vous pouvez installer dans votre compte AWS. Elle permet aux organisations de suivre les exceptions et les erreurs des applications sans avoir à choisir entre la commodité du logiciel en tant que service et la sécurité d'une solution auto-hébergée. Vous pouvez la consulter ici : [https://desole.io](https://desole.io).

![Image](https://cdn-media-1.freecodecamp.org/images/g874CpDwSRlIUinEuRFszzJVYRxy9G75Ewrp)
_[Desole](https://desole.io" rel="noopener" target="_blank" title="), suivi des erreurs open source, étroitement intégré avec AWS_

> _Toutes les illustrations sont créées avec l'application [SimpleDiagrams4](https://www.simplediagrams.com)._

Si vous voulez en savoir plus sur les tests et la construction d'applications serverless en utilisant Node.js et AWS, consultez « Serverless Applications with Node.js », le livre que j'ai écrit avec [Aleksandar Simovic](https://www.freecodecamp.org/news/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e/undefined) pour Manning Publications :

[**Serverless Applications with Node.js**](https://www.manning.com/books/serverless-applications-with-nodejs)
[_Une introduction convaincante aux déploiements serverless utilisant Claudia.js._www.manning.com](https://www.manning.com/books/serverless-applications-with-nodejs)

Le livre vous apprendra davantage sur les tests serverless, avec des exemples de code, mais vous apprendrez également à construire et déboguer une API serverless réelle (avec base de données et authentification) en utilisant Node et Claudia.js. Et vous apprendrez à construire des chatbots, pour Facebook Messenger et SMS (en utilisant Twilio), et des compétences Alexa.