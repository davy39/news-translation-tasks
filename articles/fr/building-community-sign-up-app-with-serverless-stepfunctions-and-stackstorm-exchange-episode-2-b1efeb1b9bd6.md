---
title: Créer une application d'inscription communautaire avec Serverless, StepFunctions
  et StackStorm Exchange — Épisode 2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T19:41:18.000Z'
originalURL: https://freecodecamp.org/news/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-0KcbVF9M6t_UvLpObeNYw.jpeg
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: lambda
  slug: lambda
- name: Python
  slug: python
- name: serverless
  slug: serverless
seo_title: Créer une application d'inscription communautaire avec Serverless, StepFunctions
  et StackStorm Exchange — Épisode 2
seo_desc: 'By Dmitri Zimine

  Build a real-world serverless application on AWS with Serverless framework and ready-to-use
  functions from StackStorm Exchange open-source catalog.

  Episode One | Episode Two | Episode Three | Episode Four

  In this second episode, I’ll...'
---

Par Dmitri Zimine

Créez une application serverless concrète sur AWS avec le [Serverless framework](https://serverless.com/framework/) et des fonctions prêtes à l'emploi issues du catalogue open-source [StackStorm Exchange](https://exchange.stackstorm.org).

[Épisode Un](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) | Épisode Deux | [Épisode Trois](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a) | [Épisode Quatre](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6)

Dans ce deuxième épisode, j'ajouterai deux actions supplémentaires : créer un contact dans ActiveCampaign et enregistrer un utilisateur dans Dynamo DB. Le code complet de cet épisode est disponible sur Github sur la branche [2-add-more-actions](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/2-add-more-actions).

### Ajouter plus d'actions

Pour passer à l'étape suivante, vous aurez besoin d'un compte [ActiveCampaign](https://www.activecampaign.com). N'ayez crainte : cela prend 2 minutes — je viens d'essayer — ils ne m'ont pas demandé de carte de crédit ou quoi que ce soit de stupide. Juste un e-mail. Une fois connecté, allez dans « My Settings » et sélectionnez « Developer ».

Notez les champs `URL` et `Key` dans la section « API access ». Ajoutez-les dans `env.yml` comme ceci :

```
# Copiez dans env.yml et remplacez par vos valeurs.
# Ne commitez pas sur Github :)
slack:
  admin_token: "xoxs-111111111111-111111111111-..."
  organization: "your-team"
active_campaign:
  url: "https://YOUR-COMPANY.api-us1.com"
  api_key: "1234567a9012a12345z12aa2..."
```

**ASTUCE DE PRO :** Si vous n'êtes pas d'humeur pour Active Campaign ou toute autre inscription, simulez simplement le point de terminaison de l'API avec quelque chose comme [Mocky](https://www.mocky.io/) ou [mockable.io](https://www.mocky.io/) et ajustez les exemples en conséquence. Pour plus de points, créez une autre fonction serverless avec un point de terminaison API Gateway dans votre `serverless.yml` et utilisez-la pour simuler l'appel API ActiveCampaign.

Je suis maintenant prêt à ajouter une fonction Lambda [Active Campaign](https://exchange.stackstorm.org/#activecampaign). Même routine que dans l'[Épisode Un](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) : commencez par trouver une nouvelle action dans un pack avec `sls stackstorm info --pack activecampaign` (indice : l'action que vous recherchez est `contact_sync` qui ajoute et met à jour un contact). Inspectez l'action avec `sls stackstorm info --action activecampaign.contact_sync` :

Beaucoup de paramètres, mais à part la configuration, seul `email` est requis. Je veux aussi utiliser `first_name` et `last_name`. La définition de la fonction dans `serverless.yml` ressemblera à ceci :

```
RecordAC:
    timeout: 10
    memorySize: 128
    stackstorm:
      action: activecampaign.contact_add
      input:
        email: "{{ input.body.email }}"
        first_name: "{{ input.body.first_name }}"
        last_name: "{{ input.body.last_name }}"
      config: ${file(env.yml):activecampaign}
```

J'ai dû augmenter le timeout car l'API ActiveCampaign prend plus de temps que les 6 secondes par défaut de Lambda pendant la période de Noël. Mais je peux récupérer le coût d'invocation en abaissant l'utilisation de la mémoire des 512 Mo par défaut. Cette fois, je ne prends pas la peine de l'exposer à AWS API Gateway - nous pouvons commodément la tester avec `sls`.

La fonction est prête à s'envoler vers AWS. Nous pourrions le faire d'un coup avec `sls deploy` mais ralentissons à nouveau et répétons les étapes de déploiement comme dans l'[épisode 1](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) de ce tutoriel pour bien ancrer le workflow dans votre esprit :

1. Construire et packager le bundle :

```
sls package
```

2. Tester localement (notez que j'utilise `--passthrough` pour tester uniquement les transformations, retirez-le pour effectuer un appel réel) :

```
sls stackstorm docker run --function RecordAC \
--passthrough \
--verbose --data '{"body":{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}}'
```

3. Déployer sur AWS :

```
sls deploy
```

4. Tester sur AWS avec `sls invoke` :

```
sls invoke --function RecordAC --logs \
 --data '{"body":{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}}'
```

5. Vérifier les logs :

```
sls logs --function RecordAC
```

et j'ai vérifié, ça fonctionne : Santa Claus est apparu dans la liste de contacts d'ActiveCampaign. Comment savoir s'il s'agit de notre Lambda ? Parce que je ne crois plus que le Père Noël soit assez réel pour s'inscrire à une communauté sans notre petite fonction Lambda.

**ASTUCE DE PRO :** Si vous rencontrez un bug ou souhaitez une fonctionnalité dans un pack que vous utilisez de [StackStorm Exchange](https://exchagne.stackstorm.org), vous pouvez le corriger sur-le-champ. Les packs sont clonés sous `./~st2/packs`. Trouvez votre action là-bas, modifiez le code et utilisez une exécution locale pour déboguer et valider. 
Un grand bonus pour avoir poussé les corrections vers l'Exchange : chaque pack est déjà un clone git, ce qui facilite naturellement la contribution à la communauté.

Ajoutons l'action finale, RecordDB, qui écrit les informations de contact dans une table DynamoDB. J'aurais pu utiliser l'action `aws.dynamodb_put_item` du [pack AWS sur StackStorm Exchange](https://exchange.stackstorm.org/#aws) - le pack est très utilisé et bien maintenu. Mais j'ai décidé d'en faire une Lambda native : c'est seulement 30 lignes de code, sans dépendances Python supplémentaires, puisque la bibliothèque Boto est déjà présente dans l'environnement AWS Lambda.

Le code de la fonction va dans `./record_db/handler.py` :

Le `serverless.yml` final avec les trois actions ressemble maintenant à ceci :

Wow ! Le fichier a doublé. La fonction elle-même ne fait que 2 lignes (35:36), mais plusieurs ajouts intéressants ont eu lieu. Passons-les en revue :

1. Ligne 9 — Nom de la table généré pour éviter les collisions entre les régions et les environnements.
2. Lignes 10:13 — Rôle IAM créé pour donner à la fonction l'accès à la table DynamoDB.
3. Ligne 39:56 — Modèle AWS CloudFormation définissant la table.

Le dernier point soulève une observation importante : le [Serverless framework](https://www.freecodecamp.org/news/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6/(https://serverless.com/framework)) simplifie principalement la partie FaaS du serverless. Mais parce que le serverless est plus que le FaaS, vous vous retrouverez à écrire pas mal de CloudFormation pour provisionner d'autres services. Le Serverless framework laisse de la place pour les ressources spécifiques au fournisseur. Pour être sérieusement serverless sur AWS, maîtrisez CloudFormation. Vous cherchez du « serverless agnostique au fournisseur » ? Vérifiez bien vos hypothèses.

De plus, j'ai déplacé `memorySize` et `timeout` pour qu'ils s'appliquent à toutes les fonctions (lignes 6:7). Et le point de terminaison API Gateway a disparu de la fonction InviteSlack : il servait de démonstration dans le premier épisode, mais maintenant nous avons appris à tester les fonctions Lambda directement. Nous reviendrons à l'API Gateway plus tard pour invoquer le workflow final StepFunction de bout en bout.

Mettons la fonction RecordDB en service.
Déployez, invoquez, logs. Répétez l'opération.

```
# Déploiement
sls deploy ...
```

```
# Invocation
sls invoke --function RecordDB --logs --data '{"body":{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}}'...
```

```
# Vérification des logs
sls logs --function RecordDB.
```

Maintenant, les trois actions sont là, attendant d'être reliées entre elles dans un workflow final avec une StepFunction. Mais on vient de me rappeler de ne pas faire mon Monsieur Scrooge : c'est la période des fêtes, relaxons-nous et remettons cela au prochain épisode. D'ici là, gardez le moral !

L'exemple de code complet pour cet épisode est sur Github sur la branche [2-add-more-actions](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/2-add-more-actions).

[**Épisode 3**](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a)** : Relier les actions avec une StepFunction**

J'espère que cela vous a aidé à apprendre quelque chose de nouveau, à trouver quelque chose d'intéressant ou a suscité de bonnes réflexions. N'hésitez pas à partager vos impressions dans les commentaires ici, ou envoyez-moi un tweet [@dzimine](https://twitter.com/dzimine).