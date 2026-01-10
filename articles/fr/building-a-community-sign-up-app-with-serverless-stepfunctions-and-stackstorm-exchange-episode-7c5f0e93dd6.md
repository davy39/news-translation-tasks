---
title: Création d'une application d'inscription communautaire avec Serverless, StepFunctions
  et StackStorm Exchange — Épisode…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-03T02:03:56.000Z'
originalURL: https://freecodecamp.org/news/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jiZOQLvfX2257LHxe3n4cg.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: AWS Step Functions
  slug: aws-step-functions
- name: Devops
  slug: devops
- name: FaaS
  slug: faas
- name: serverless
  slug: serverless
seo_title: Création d'une application d'inscription communautaire avec Serverless,
  StepFunctions et StackStorm Exchange — Épisode…
seo_desc: 'By Dmitri Zimine

  Build a real-world serverless application on AWS with Serverless framework and ready-to-use
  functions from StackStorm Exchange open-source catalog.

  Episode One | Episode Two | Episode Three | Episode Four

  It took us three exciting ep...'
---

Par Dmitri Zimine

Construisez une application serverless réelle sur AWS avec le [Framework Serverless](https://serverless.com/framework/) et des fonctions prêtes à l'emploi provenant du catalogue open-source [StackStorm Exchange](https://exchange.stackstorm.org).

[Épisode Un](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) | [Épisode Deux](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6) | [Épisode Trois](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a) | Épisode Quatre

Il nous a fallu trois épisodes passionnants pour créer une application serverless non triviale. Le back-end fonctionne maintenant, mais deux choses manquent encore : une interface Web et une discussion finale pour résumer les leçons. Continuons… après un rapide récapitulatif des épisodes précédents :

* Dans l'[Épisode Un](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419), j'ai décrit l'application que nous construisons, je vous ai guidé à travers la configuration de l'environnement de développement et la création d'un projet Serverless, et j'ai montré comment construire votre première fonction Lambda à partir d'une action [StackStorm Exchange](https://exchange.stackstorm.org) avec le [Framework Serverless](https://serverless.com/framework).
* Dans l'[Épisode Deux](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6), nous avons ajouté plus d'actions : une Lambda native pour enregistrer les informations utilisateur dans DynamoDB, et une autre provenant de StackStorm Exchange pour effectuer un appel au système CRM ActiveCampaign. Vous avez appris davantage sur la syntaxe de `serverless.yml` et pratiqué le flux de développement avec les fonctions Lambda.
* Dans l'[Épisode Trois](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a), nous avons connecté les actions avec StepFunctions, appris des astuces pour passer les données entre les étapes, lutté pour déboguer les exécutions de StepFunction, et finalement obtenu le backend fonctionnant de bout en bout.

Vous pouvez obtenir le code final pour cet épisode depuis [GitHub](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/3-add-stepfunction).

### Ajouter une interface Web

Nous avons besoin d'un formulaire web qui prend les noms et emails des utilisateurs, et les envoie à notre point de terminaison API Gateway StepFunction. J'ai simplement copié celui que j'ai utilisé lors de l'exploration de Serverless avec Python, StepFunctions et le front-end web Serverless. Ce que, je l'avoue, j'ai pris de l'ancien projet [Serverless Slack Invite](https://github.com/serverless-london/serverless-slack-invite).

Ceux d'entre vous qui sont développeurs Web peuvent sûrement créer quelque chose de plus élégant avec ReactJS — les PR sont les bienvenus ! Que vous construisiez le vôtre ou que vous preniez le mien, faites ceci : créez un répertoire `web` et placez le contenu statique là.

J'utilise `[http-server](https://www.npmjs.com/package/http-server)` pour un aperçu rapide de mon formulaire statique :

```
cd webhttp-serverDémarrage de http-server, servant ./Disponible sur : http://127.0.0.1:8080
```

Ouvrez un navigateur, vérifiez le formulaire à l'adresse [http://127.0.0.1:8080](http://127.0.0.1:8080), voyez qu'il est correct, et passons à l'étape suivante.

Comment déployer un front-end web serverless sur AWS ? Typiquement, vous placez le contenu statique sur S3, vous le configurez pour servir le web, vous faites en sorte que votre application web appelle votre point de terminaison backend, et vous n'oubliez pas d'activer CORS sur le point de terminaison API Gateway.

Alternativement, vous ajoutez un chemin à votre ressource API Gateway pour servir votre contenu web statique depuis le bucket S3.

**Avantages :** 1) pas de problème avec CORS, 2) pas besoin d'ajuster votre application web pour pointer vers le bon point de terminaison backend. Bonus supplémentaire : facilement fait avec le plugin [serverless-apig-s3](https://github.com/sdd/serverless-apig-s3).

**Inconvénients :** 1) payer les frais API Gateway pour les requêtes web 2) le plugin est un peu instable : bien pour les exemples et les petites applications, mais je ne l'utiliserais pas pour quoi que ce soit ressemblant à de la production.

**ASTUCE PRO :** Pour les front-ends web sérieux avec des charges élevées : déployez-les sur CloudFront. Ou utilisez quelque chose comme Netlify — consultez le récent article « [Comment construire un site Serverless statique avec Netlify](https://serverless.com/blog/how-built-static-serverless-website-netlify/) » de serverless.com.

Je vais utiliser l'approche API Gateway avec le plugin [serverless-apig-s3](https://github.com/sdd/serverless-apig-s3) ici : nous ne prévoyons pas de charge massive. Et c'est simple. Regardez :

Installez le plugin (déjà fait, fait) :

```
npm install --save-dev serverless-apig-s3
```

Modifiez `serverless.yml`. Ajoutez le plugin (déjà fait, fait). Ajoutez les [configurations du plugin](https://github.com/sdd/serverless-apig-s3) :

```
...custom:  private: ${file(env.yml):private}  stage: ${opt:stage, self:provider.stage}  region: ${opt:region, self:provider.region}  apigs3:    dist: web    topFiles: true
```

```
...
```

```
plugins:  - serverless-plugin-stackstorm  - serverless-step-functions  - serverless-apig-s3
```

Nous disons au plugin de prendre notre répertoire `web` et de le mettre sur S3. Le drapeau `topFiles` indique à API Gateway d'exposer notre `index.html` et `formsubmit.js` à notre point de terminaison, sous `/web/`

Maintenant, déployez le service, et, séparément, le côté client, avec deux commandes :

```
sls deploy
```

```
sls client deploy
```

Le déploiement du service mettra à jour l'API Gateway avec les chemins pour accéder à notre contenu web. Le déploiement du client met le contenu web sur un bucket S3. Maintenant, vous pouvez raisonner que si vous ajoutez ou supprimez des fichiers web et que le déploiement client n'est pas suffisant, un `sls deploy` complet est requis. Mais si vous ne changez que les fichiers web, un rapide `sls client deploy` les mettra sur AWS.

C'est tout !   
Allez sur `https://YOUR-ENDPOINT.amazonaws.com/dev/web/index.html`. Le formulaire est là. Le bouton est orange. Vous tapez les informations utilisateur et l'email, vous cliquez sur le bouton orange. Le message vert vous dit que tout est OK. Bientôt, vous recevez une invitation de Slack. Vous vérifiez les exécutions de StepFunction dans la console AWS et voyez que tout est vert.

![Image](https://cdn-media-1.freecodecamp.org/images/P7X4oec6ilXzVayCaauhg-KqdJAwkcRIMI1w)

**Non ?!** Très probablement, vous avez rencontré ce [bug apig-s3](https://github.com/sdd/serverless-apig-s3/issues/16), tout comme moi. Et tout comme moi, vous devez faire une petite étape finale manuellement.

Ouvrez la console AWS -> API Gateway -> Ressources -> Actions -> Déployer l'API.   
Ou utilisez AWS CLI :

```
# Découvrez d'abord votre rest-api-idaws apigateway get-rest-apis
```

```
# Déployez les changements sur le stage# Ne COPIEZ-PAS, il faut VOTRE ID !aws apigateway create-deployment --rest-api-id  YOUR_API_ID  --stage-name dev
```

**Maintenant, cela fonctionne pour moi.**

**ASTUCE PRO :** Le plugin fonctionne lorsque tout est déployé à partir de zéro. Mais si vous êtes tenté de faire `sls remove` et de redéployer, vous rencontrez au moins un [autre bug du plugin](https://github.com/sdd/serverless-apig-s3/issues/11) lors de la suppression de la stack. Voir les astuces et conseils à la fin de l'article sur la façon de nettoyer correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/AxHuvaj3Gp0QWiqDinSqS43JfK1RsrcQJsVw)

Félicitations ! Vous l'avez fait. Vous avez peut-être suivi et construit votre propre application. Vous avez peut-être abandonné à un moment donné par frustration ou fatigue. Vous avez peut-être simplement parcouru le texte et les exemples. Mais si vous êtes arrivé à la fin, vous avez appris suffisamment sur le serverless pour être dangereux.

### Réflexion

Après avoir lutté à travers les 4 épisodes, vous l'avez probablement senti : le serverless n'est pas simple. De nombreuses choses peuvent mal tourner lorsque vous construisez une application serverless.

Vous pouvez m'en attribuer certaines : j'ai sûrement fait quelques erreurs et omissions (d'ailleurs, les rapports et commentaires sont très appréciés !)

Mais la complexité du serverless n'est pas entièrement de ma faute. Nous connectons ensemble de nombreux services différents — AWS et tiers — avec de nombreux fils différents — frameworks et outils. Les services sont de qualité et de [in]convenance différentes (ne me lancez pas sur l'interface de ligne de commande AWS StepFunction). Les frameworks et outils sont encore en maturation (quel plugin serverless vous a fait le plus lutter ?).

Pourquoi se lancer dans le serverless ? Parce que pour certaines classes d'applications, c'est substantiellement moins cher. Cette inscription communautaire en est un exemple : nous utilisions StackStorm avec StackStorm. C'était simple à construire et solide comme un rocher, mais cela nécessitait une instance `m3.large` à 100 $/mois, sans même atteindre la fiabilité multi-zone. Avec le serverless, cela fonctionne à moins de 1 $/mois, grâce au modèle de charge occasionnelle. 100 $ nous permettraient d'avoir ~5 000 000 d'inscriptions — c'est plus que nous n'en aurons jamais besoin !

À l'autre extrême, les applications à fort volume avec des exigences de fiabilité élevées pourraient également être mieux en serverless, tirant parti de l'élasticité « infinie » qui peut être coûteuse à construire et à exploiter soi-même. J'utilise soigneusement « pourrait » et « serait », car l'équation varie considérablement d'un cas à l'autre. Faites vos calculs à l'avance, surveillez vos modèles de charge, explorez votre facture.

En ce qui concerne la maîtrise de la complexité, le [Framework Serverless](https://serverless.com/framework) aide. Pour l'apprécier pleinement, essayez de refaire la même application sans lui. Rendez-la fiable, répétable, infrastructure-as-code révisable. Bien que le Framework Serverless ne soit pas le seul jeu en ville, je l'apprécie particulièrement pour son architecture pluggable et l'écosystème de plugins.

Les plugins aident, en couvrant les domaines non couverts par le Framework Serverless de base. En utilisant les plugins, nous avons apprécié la simplicité de la construction de StepFunctions et de l'ajout de front-ends web simples (et si vous ne l'avez pas fait, essayez de le refaire sans les plugins). Il y en a plus : parcourez et marquez la [liste des plugins officiels](https://github.com/serverless/plugins) pour les garder à l'esprit pour votre prochain projet.

[StackStorm Exchange](https://exchange.stackstorm.org) — la récente addition à l'écosystème serverless — apporte un catalogue d'intégrations réutilisables. Bien qu'il ne soit pas difficile de scraper les API pour ActiveCampaign ou de trouver et d'utiliser des appels d'API Slack non documentés, c'est un travail de faible valeur qui détourne de la construction de la logique de l'application.

Explorez ce qui est déjà là : bien que les intégrations DevOps dominent en raison des racines de StackStorm dans l'automatisation IT, je m'attends à ce que la variété augmente maintenant que la communauté Serverless rejoint pour contribuer et copiloter le catalogue.

Avec cela, **nous avons officiellement terminé**. Profitez-en !

### Quelques astuces et conseils supplémentaires

* La suppression de tout ne supprimera pas la table DynamoDB. Un défaut raisonnable, mais lorsque vous essayez de redéployer le service, il se plaindra que la table ne peut pas être créée car elle existe déjà. Supprimez-la : `aws dynamodb delete-table --table-name signup-stormless-dev`
* En raison d'un bug apig-s3, `sls remove` échouera en se plaignant que le bucket n'est pas vide. Supprimez manuellement le bucket s3 web lors de la suppression d'une stack. `aws s3 rb s3://bucketname --force`
* La suppression de la stack ne supprime pas la table DynamoDB. Si vous voulez vraiment repartir de zéro, supprimez-la manuellement (exportez les données d'abord) :  
 `aws dynamodb delete-table --table-name slack-signup-dev`
* Parfois, `sls delete` échoue à nettoyer. Les raisons peuvent être variées, mais l'endroit où chercher est le même. Est-ce que je vous ai dit de maîtriser CloudFormation ? Allez-y, trouvez une stack qui n'a pas pu être supprimée, trouvez la raison, corrigez et supprimez la stack.

J'espère que cela vous a aidé à apprendre quelque chose de nouveau, à trouver quelque chose d'intéressant, ou à provoquer de bonnes réflexions. Veuillez partager vos pensées dans les commentaires ici, ou tweetez-moi [@dzimine](https://twitter.com/dzimine).