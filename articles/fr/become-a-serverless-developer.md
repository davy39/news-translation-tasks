---
title: Comment devenir un développeur Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-19T20:57:22.000Z'
originalURL: https://freecodecamp.org/news/become-a-serverless-developer
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/sls_talks_3_B.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: serverless
  slug: serverless
- name: serverless framework
  slug: serverless-framework
seo_title: Comment devenir un développeur Serverless
seo_desc: 'By Sam Williams

  Serverless Development has been around since the release of AWS Lambda in 2014,
  but in the last few years things have exploded.

  Startups and smart tech companies have started taking advantage of the scalability,
  reliability, and power...'
---

Par Sam Williams

Le développement Serverless existe depuis la sortie d'AWS Lambda en 2014, mais ces dernières années, les choses ont explosé.

Les startups et les entreprises technologiques intelligentes ont commencé à tirer parti de la scalabilité, de la fiabilité et de la puissance du serverless pour croître rapidement – et maintenant, elles ont besoin de plus de développeurs serverless que jamais.

Être un "développeur Serverless" signifie que vous construisez des solutions avec des services gérés par des plateformes comme AWS, Google Cloud (GCP) ou Azure. Vous construisez des solutions en assemblant différents services et en exécutant toute votre logique métier dans AWS Lambda ou les fonctions cloud de GCP au lieu de le faire sur un serveur.

Avec votre plateforme cloud qui gère presque toutes les opérations (sécurité, redondance, scalabilité et réseau), vous pouvez vous concentrer sur la construction des meilleures solutions possibles. Cela signifie que les fonctionnalités peuvent être construites plus rapidement et que les entreprises n'ont pas besoin d'embaucher des spécialistes des opérations.

Cet article couvrira les 5 étapes pour apprendre à devenir un développeur serverless afin que vous puissiez construire des produits exceptionnels.

## En résumé

1. Avoir de solides compétences en JavaScript ou Python. Vous n'avez pas besoin d'être un magicien, mais être à l'aise pour écrire un serveur Express ou Flask rendra le reste beaucoup plus facile.

2. Choisissez votre framework – optez pour [The Serverless Framework](https://www.serverless.com/) ou [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html).

3. Suivez un tutoriel pour commencer à apprendre à construire avec votre framework. Commencez par construire une API avec API Gateway et Lambda.

4. Apprenez-en plus sur les services que vous utilisez. Quels sont les avantages, les limitations, les bons cas d'utilisation et les mauvais ?

5. Intégrez ce que vous avez appris dans les tutoriels dans votre propre projet.

Maintenant que vous avez appris à construire une API, ajoutez d'autres services, en répétant les étapes 3 à 5 à chaque fois. Un bon ordre pourrait être :

* DynamoDB – obtenir et écrire des données

* S3 – lire et écrire des fichiers

* DynamoDB – avec des index secondaires et des requêtes

* Cognito – Autorisation pour votre API

* AppSync – API GraphQL

%[https://youtu.be/u-UaP8XONgg]

## 1. Solides compétences en JavaScript ou Python

Avant d'essayer de construire des systèmes serverless, vous devez vraiment maîtriser les bases de l'un des langages de programmation courants. Vous n'avez pas besoin d'être un magicien, mais être à l'aise avec votre langage choisi est essentiel.

La raison pour laquelle vous devez être à l'aise pour écrire du bon code est que cela a un impact énorme sur le logiciel que vous construisez. Le serverless, c'est comme des blocs de construction et le code Lambda est comme la colle. Dans ce code, vous écrivez la logique pour connecter chaque partie.

> Vous pourriez avoir l'architecture parfaite, mais si votre code Lambda est bogué, votre solution le sera aussi.

Je recommande soit JavaScript (TypeScript) soit Python. La raison pour laquelle je recommande ces deux langages est que la plupart des entreprises qui utiliseront l'architecture Serverless utiliseront l'un de ces deux langages. Heureusement, ce sont aussi les deux langages enseignés ici sur FreeCodeCamp 🎉.

Étant les plus largement utilisés, ils ont également plus de tutoriels et une communauté plus grande pour vous aider lorsque vous êtes bloqué.

Une autre raison pour laquelle je recommande ces langages est que vous pouvez écrire le code du framework avec le même langage que celui avec lequel vous écrivez le code Lambda. Vous allez constamment passer du code lambda à la configuration du framework. Ne pas avoir à changer de langage vous fera économiser beaucoup d'énergie mentale 🧠.

## 2. Choisissez votre Framework

Avec une bonne maîtrise de votre langage, vous avez besoin d'un outil pour vous aider à créer les composants serverless dans AWS.

Il y en a beaucoup, mais je dirais que vous devriez choisir soit le Serverless Framework soit AWS CDK. J'ai une préférence pour le Serverless Framework car j'ai une [chaîne YouTube](https://www.youtube.com/CompleteCoding) avec plus de 50 vidéos sur la construction avec celui-ci. Si vous êtes un développeur Python, alors peut-être que l'AWS CDK pourrait être mieux adapté pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/slsVsCdk.png align="left")

### Pourquoi utiliser un framework ?

Lors de la construction d'une solution, il est possible de tout faire dans la console AWS. C'est ainsi que j'ai commencé mon voyage AWS.

Le problème est que ce n'est pas contrôlable, gérable ou scalable. Si vous voulez copier cette configuration dans un autre compte (comptes de développement et de production séparés), vous devez vous souvenir de toutes les étapes que vous avez faites. Travailler avec plusieurs membres de l'équipe peut devenir compliqué.

C'est pourquoi il est utile d'utiliser un framework pour nous permettre d'écrire de l'Infrastructure-as-Code (IaC). Cela nous permet d'utiliser Git pour le contrôle de version. Cela rend le travail en équipe beaucoup plus facile, permet des déploiements multi-environnements, voire l'intégration et le déploiement continus. Toutes choses nécessaires lors de l'exécution de charges de travail de production.

### The Serverless Framework

* Prouvé dans des charges de travail de production importantes

* Facile à démarrer

* Grande communauté

* Beaucoup de tutoriels

* Beaucoup de plugins pour faciliter de nombreuses tâches

* Pas aussi facile lorsque vous faites des choses qui ne sont pas serverless

* Si vous utilisez Python, vous devrez le configurer avec YAML

### AWS CDK

* D'AWS et est activement développé par eux

* Bon support pour presque tout dans AWS

* Certaines façons cool de créer des constructs réutilisables

* Communauté et pool de tutoriels en croissance

* Peut définir la configuration en utilisant Python

* Pas le même écosystème de 'Plugins' que le Serverless Framework

### Autres Frameworks

Certains d'entre vous pourraient dire "Et tous les autres frameworks ?" et je vais aborder ceux-ci.

#### AWS SAM & AWS Amplify

![Image](https://www.freecodecamp.org/news/content/images/2022/01/SAM-AMPLIFY.png align="left")

Ces frameworks sont conçus pour être très faciles à utiliser pour des choses simples. Si vous lisez ceci, vous pourriez probablement utiliser ceux-ci pour créer une API et un site web rapidement et facilement.

C'est génial si c'est tout ce que vous voulez faire. Mais si vous voulez plus de contrôle sur **comment** ils sont déployés ou si vous voulez déployer **des systèmes plus complexes**, alors vous allez avoir du mal.

#### Terraform & Ansible

Ces frameworks existent depuis longtemps et sont utilisés en entreprise comme leur outil d'Infrastructure as Code (IaC).

Les raisons pour lesquelles je ne les recommanderais pas comme premier framework sont :

1. Vous devez apprendre un nouveau langage. Terraform utilise HCL (Hashcorp Language) et Ansible utilise YAML. Apprendre un nouveau langage tout en essayant de comprendre l'architecture Serverless n'est pas idéal. De plus, passer à ce langage lorsque vous devez créer une infrastructure est épuisant pour le cerveau.

2. Ils sont opinés et stricts. Une petite chose mal configurée ne fonctionnera tout simplement pas, souvent avec une erreur difficile à comprendre.

3. Ils ne sont pas aussi flexibles ou puissants que CDK ou Serverless Framework.

#### Webiny & Serverless Cloud

Ce sont des frameworks très nouveaux qui tentent de rendre l'IaC aussi simple mais aussi puissant que possible.

La raison pour laquelle je les éviterais pour l'instant est qu'ils sont tout simplement trop nouveaux. Cela a deux inconvénients :

1. La communauté n'est pas aussi grande. Cela signifie moins de tutoriels et moins de personnes à qui demander si vous êtes bloqué.

2. Les choses changent rapidement. Les meilleures pratiques et la structure commune, mais parfois aussi les API, les méthodes et les paramètres. Lorsque vous apprenez un framework, vous ne voulez pas avoir à gérer ce genre de choses.

Si vous avez une fonctionnalité que vous devez absolument utiliser et que vous avez quelqu'un qui est très expérimenté avec ce framework spécifique, alors cela pourrait fonctionner. Je recommanderais toujours l'un des deux principaux.

## 3. Suivez un tutoriel

Avec votre framework choisi, vous pouvez maintenant commencer à construire des choses avec lui.

La première chose que vous devriez construire est une API en utilisant uniquement Lambda et API Gateway. C'est très simple mais vous donnera de la pratique avec les fondamentaux du framework. Comprendre les fondamentaux rendra l'apprentissage de choses plus avancées beaucoup plus facile.

### Pourquoi suivre un tutoriel

Lors de l'apprentissage d'un nouveau service, il peut être tentant d'essayer de l'apprendre en l'ajoutant directement à un projet existant. Je recommanderais toujours d'essayer de suivre un tutoriel la première fois que vous travaillez avec un nouveau service ou outil.

Lorsque vous suivez un tutoriel, cela devrait fonctionner sans aucun problème. Cela signifie que vous pouvez vous concentrer sur l'apprentissage du service et sur la façon dont il s'intègre avec tout le reste.

L'ajouter à votre propre projet signifie que si quelque chose ne fonctionne pas, vous devez le déboguer vous-même. Vous ne saurez peut-être pas si vous avez mal utilisé le service ou s'il y a un bug le connectant à votre système existant.

## 4. Apprenez-en plus sur les services que vous utilisez

Maintenant que vous avez utilisé le nouveau service, il est bon d'en apprendre un peu plus à son sujet. Les choses clés que je voudrais savoir sur un service que j'utilise sont :

1. Quels sont ses points forts, ses faiblesses et ses limitations ?

2. Quels sont les cas d'utilisation idéaux pour utiliser le service ?

3. Quels sont les cas d'utilisation où vous devriez éviter d'utiliser ce service ?

En connaissant ces trois choses, vous serez beaucoup mieux à même de décider si un service sera adapté à la solution que vous construisez actuellement.

Vous pouvez apprendre à partir de diverses sources : tutoriels, articles, et même la documentation AWS.

Par exemple, AWS Lambda est idéal pour la plupart des API, mais ne peut pas fonctionner pendant plus de 15 minutes. Si je dois construire une API qui fait du traitement par lots prenant 10 à 20 minutes, elle dépasserait le temps imparti la moitié du temps. Par conséquent, je dois trouver une autre solution.

Encore une fois, vous n'avez pas besoin de comprendre chaque petit détail sur chaque service, juste assez pour savoir quand il est bon de l'utiliser et quand ne pas le faire.

## 5. Construisez vos propres projets

Maintenant que vous savez comment construire avec le nouveau service (grâce aux tutoriels) et que vous avez une bonne compréhension de quand utiliser le service.

À partir de là, il est temps d'utiliser ces services dans vos propres projets.

Je recommanderais de commencer par un projet personnel que vous utilisez juste pour pratiquer l'utilisation de nouveaux services. Ainsi, vous n'avez pas à vous soucier de casser des choses et vous pouvez vous concentrer sur le fonctionnement du service.

Vous pouvez maintenant commencer à l'utiliser dans des applications de production et c'est là que vous apprendrez beaucoup sur les détails d'un service. Vous apprenez comment le faire répondre aux exigences commerciales et comment il fonctionne avec d'autres services. Si vous pouvez le faire dans le cadre de votre travail, c'est encore mieux. Sinon, avez une application déployée que vous traitez avec le même soin.

## Répétez les étapes 3 à 5

Félicitations ! Vous avez appris à construire une API en utilisant un framework.

Ce n'est pas la fin, car il y a toujours plus à apprendre et une façon de devenir un meilleur développeur serverless. Choisissez un nouveau sujet, service ou modèle de conception et répétez les étapes 3 à 5.

Si vous venez de créer votre première API serverless, voici les prochains sujets et services que j'apprendrais pour continuer votre voyage.

* DynamoDB – créer une table simple, obtenir et écrire des données

* S3 – créer un bucket S3, lire et écrire des fichiers

* DynamoDB – avec des index secondaires et des requêtes

* Cognito – Autorisation pour votre API

* AppSync – API GraphQL

Après cela, concentrez-vous sur la création de fonctionnalités pour vos solutions et utilisez cela pour guider ce que vous devez apprendre ensuite.

Si vous êtes un développeur JavaScript souhaitant utiliser le Serverless Framework, alors un bon point de départ est ma [chaîne YouTube](https://www.youtube.com/CompleteCoding) où nous créons des tutoriels pour devenir le meilleur développeur Serverless que vous puissiez être.