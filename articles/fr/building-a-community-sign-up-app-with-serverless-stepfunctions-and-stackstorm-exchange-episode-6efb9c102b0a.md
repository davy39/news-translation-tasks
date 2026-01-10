---
title: Créer une application d'inscription communautaire avec Serverless, StepFunctions
  et StackStorm Exchange — Épisode…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T07:06:59.000Z'
originalURL: https://freecodecamp.org/news/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0xq8ywxkBv-oIe6b-6H9ug.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: AWS Step Functions
  slug: aws-step-functions
- name: FaaS
  slug: faas
- name: serverless
  slug: serverless
seo_title: Créer une application d'inscription communautaire avec Serverless, StepFunctions
  et StackStorm Exchange — Épisode…
seo_desc: 'By Dmitri Zimine

  Build a real-world serverless application on AWS with Serverless framework and ready-to-use
  functions from StackStorm Exchange open-source catalog.

  Episode One | Episode Two | Episode Three | Episode Four

  We are at Episode Three. Qui...'
---

Par Dmitri Zimine

Créez une application serverless concrète sur AWS avec le [Serverless framework](https://serverless.com/framework/) et des fonctions prêtes à l'emploi issues du catalogue open-source [StackStorm Exchange](https://exchange.stackstorm.org).

[Épisode Un](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) | [Épisode Deux](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6) | Épisode Trois | [Épisode Quatre](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6)

Nous en sommes à l'Épisode Trois. Bref récapitulatif :

* Dans l'[Épisode Un](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419), j'ai décrit l'application que nous construisons, je vous ai guidé dans la configuration de l'environnement de développement et la création d'un projet Serverless, et je vous ai montré comment construire votre première fonction Lambda à partir d'une action [StackStorm Exchange](https://exchange.stackstorm.org) avec le [Serverless Framework](https://serverless.com/framework).
* Dans l'[Épisode Deux](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6), nous avons ajouté d'autres actions : une Lambda native pour enregistrer les informations utilisateur dans DynamoDB, et une autre de StackStorm Exchange pour appeler le système CRM ActiveCampaign. Vous en avez appris davantage sur la syntaxe `serverless.yml` et avez pratiqué le flux de travail de développement avec les fonctions Lambda.

Dans ce troisième épisode, je vais vous montrer comment utiliser AWS StepFunction pour relier les actions dans un workflow.

Vous pouvez obtenir le code final de cet épisode sur [GitHub](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/3-add-stepfunction).

### Relier les fonctions entre elles avec StepFunction

Maintenant que nos blocs de construction — les fonctions Lambda — sont tous alignés, il est temps de les enchaîner. Une [AWS StepFunction](https://aws.amazon.com/step-functions/) définira la séquence d'appels, maintiendra l'état du workflow d'inscription et transportera les données entre les étapes. J'utiliserai le plugin `[serverless-step-functions](https://github.com/horike37/serverless-step-functions)` du Serverless Champion @horike37, donnez-lui un cœur :

Au travail. Installez le plugin :

```
npm install --save-dev serverless-step-functions
```

Ajoutez le plugin au fichier `serverless.yml` :

```
plugins:  - serverless-plugin-stackstorm  - serverless-step-functions
```

La définition de la Step Function nécessitera mon `accountID`. Comme c'est une information que je souhaite garder pour moi, je l'ajoute à `env.yml`, qui ressemble maintenant à ceci :

```
# ./env.yml# Ne pas commit sur Github :)
```

```
slack:  admin_token: "xoxs-111111111111-..."  organization: "your-team"active_campaign:  url: "https://YOUR-COMPANY.api-us1.com"  api_key: "1234567a9012a12345z12aa2aaa..."private:  accountId: "000000000000"
```

Retournez dans `serverless.yml` et ajoutez les deux blocs suivants :

```
# ./serverless.yml......custom:  private: ${file(env.yml):private}  stage: ${opt:stage, self:provider.stage}  region: ${opt:region, self:provider.region}
```

```
stepFunctions:  stateMachines:    signup:      events:        - http:            path: signup            method: POST            cors: true      definition: ${file(stepfunction.yml)}
```

Dans le bloc `custom`, j'ai assigné l'objet `private` à partir de la clé `private` dans `env.yml`. J'ai également défini des variables pour `stage` et `region` afin que les valeurs soient récupérées depuis les options de la CLI, si elles sont fournies, ou par défaut à partir des paramètres AWS actuels.

Le bloc `stepFunctions` est là pour définir — vous l'avez déjà deviné — les StepFunctions. La mienne s'appelle "`signup` ".

La section `events` ici fait exactement ce que les sections `events` font dans les définitions de fonctions : elle configure un point de terminaison API Gateway pour invoquer la StepFunction depuis l'extérieur d'AWS. Nous l'utiliserons plus tard pour appeler le back-end depuis un formulaire Web.

La `definition` peut être écrite en YAML directement ici dans `serverless.yml`, mais je préfère l'inclure depuis un fichier séparé, en gardant la logique séparée de la configuration. Le voici :

Les définitions de StepFunction sont écrites en [Amazon States Language](https://states-language.net/spec.html). La spécification est courte, bien écrite et mérite d'être lue. Utiliser YAML au lieu de JSON est un avantage appréciable du plugin — c'est plus lisible et permet les commentaires. Mais si vous voulez du JSON — pas de problème, servez-vous.

* `Resource` fait référence aux fonctions Lambda par leur ARN. J'ai utilisé les variables que nous avons définies précédemment pour construire les ARN correspondant à l'ID du compte, à la région et à l'étape avec le nom de la fonction : `arn:aws:lambda:${self:custom.region}:${self:custom.private.accountId}:function:${self:service}-${self:custom.stage}-RecordDB`
* `ResultPath` est utilisé pour passer des données entre les étapes. Par défaut, les StepFunctions fonctionnent sur la base du « besoin d'en connaître » : l'étape en aval ne reçoit que la sortie de l'étape directement en amont. Si vous pensez que c'est logique, détrompez-vous : si seul RecordDB reçoit l'entrée du workflow, comment RecordAC et InviteSlack l'obtiendront-ils ? RecordDB pourrait simplement renvoyer "200 OK", pas l' `email`. Modifier le code des fonctions pour qu'elles renvoient leur entrée les rendrait [inappropriately intimate](https://refactoring.guru/smells/inappropriate-intimacy) (trop intimes). L'astuce consiste à utiliser `ResultPath` pour écrire la sortie de la fonction sous une clé spécifique à la fonction, comme `ResultPath: $results.RecordDB`. Cela préserve l'entrée initiale du workflow dans la sortie de l'étape pour les étapes Lambda en aval, tout en ajoutant la sortie de chaque Lambda. Comme ceci :

```
{  "body": {    "name": "Vasili Terkin",    "email": "dmitri.zimine+terkin@gmail.com",    "first_name": "Vasili",    "last_name": "Terkin"  },  "results": {    "RecordDB": {      "statusCode": 200    },    "RecordAC": ...    ...  }}
```

Pour bien le comprendre, lisez la [section « Input and Output »](https://states-language.net/spec.html#filters) dans la spécification. Et divertissez-vous avec une vidéo du « [AWS Step Functions Tutorial](https://foobar123.com/aws-step-functions-tutorial-76b9f5a7b9c8) » par [Marcia Villalba](https://www.freecodecamp.org/news/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a/undefined).

**CONSEIL DE PRO :** J'ai rendu le workflow séquentiel pour démontrer l'astuce du passage de données. Il est plus approprié d'exécuter les trois étapes en parallèle : c'est plus rapide et plus résilient : l'échec d'une étape n'empêchera pas les autres invocations de fonctions. Allez-y, passez les StepFunctions en parallèle.

C'est tout. C'est le moment d'essayer. Déployez, invoquez, vérifiez les logs.

Vous, les fans de CURL, savez quoi faire avec le nouveau point de terminaison API Gateway pour notre StepFunction. Si vous avez oublié le point de terminaison, `sls info` à la rescousse. Je vais encore frimer avec [httpie](https://httpie.org) :

```
# NE PAS COPIER ! Utilisez VOTRE POINT DE TERMINAISON !
```

```
http POST https://YOUR.ENDPOINT.amazonaws.com/dev/signup \body:='{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}'
```

Ok, `http` ou `curl`, dans les deux cas, cela renvoie l'ARN d'exécution de la StepFunction afin que nous puissions vérifier comment notre StepFunction est exécutée. Comment vérifier ? J'ai bien peur que vous deviez ouvrir un navigateur et vous connecter à votre console AWS. Si vous voulez d'abord utiliser l'AWS CLI, très bien, ne dites pas que je ne vous ai pas montré comment :

```
aws stepfunctions describe-execution --execution-arn arn:aws:states:us-east-1:00000000000:execution:SignupStepFunctionsStateMac-seo9CrijATLU:cbeda709-e530-11e7-86d3-49cbe4261318 --output json{    "status": "FAILED",     "startDate": 1513738340.18,     "name": "cbeda709-e530-11e7-86d3-49cbe4261318",     "executionArn": "arn:aws:states:us-east-1:00000000000:execution:SignupStepFunctionsStateMac-seo9CrijATLU:cbeda709-e530-11e7-86d3-49cbe4261318",     "stateMachineArn": "arn:aws:states:us-east-1:00000000000:stateMachine:SignupStepFunctionsStateMac-seo9CrijATLU",     "stopDate": 1513738370.481,     "input": "{\"body\":{\"email\":\"santa@mad.russian.xmas.com\",\"first_name\":\"Santa\",\"last_name\":\"Claus\"}}"}
```

C'est la sortie d'une exécution qui a échoué car la fonction RecordAC a expiré (timeout). Pouvez-vous le déduire de la sortie ? La seule information précieuse ici est `FAILED`. Sans blague ! Je dois dire qu'AWS ne donne pas à StepFunction l'amour qu'elle mérite. Pas dans la CLI. Si vous pensez que j'ai raté quelque chose, consultez [la documentation de la CLI](http://docs.aws.amazon.com/cli/latest/reference/stepfunctions/index.html), trouvez-le et dites-le moi.

La partie la plus irritante est que la CLI ne me dit pas quelle étape a échoué. Ils m'obligent à appeler les logs sur chaque Lambda, une par une. Heureusement, je n'ai que 3 fonctions, et s'il y en avait plus ?

Ou alors, ouvrez un navigateur et rendez-vous sur la console AWS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0xq8ywxkBv-oIe6b-6H9ug.png)

Même là, déboguer certains échecs Lambda, comme les timeouts, est délicat. Le rapport d'« Exception » d'exécution de StepFunction indique `"The cause could not be determined because Lambda did not return an error type."` Allez dans les logs de la lambda pour voir ce qui s'y est passé.

J'y trouve la ligne que j'aurais aimé voir dans l'exception StepFunction :

```
2017-12-20T04:21:44.298Z 4230a73b-e53d-11e7-be6b-bff82b9b3572 Task timed out after 6.00 seconds
```

**CONSEIL DE PRO :** Pour le débogage, invoquez la StepFunction avec `sls invoke stepf` : cela crée l'exécution, attend la fin et affiche la sortie dans le terminal. Trois commandes AWS CLI en une.

```
sls invoke stepf --name signup \--data  '{"body": {"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Clause"}}'
```

Vos exécutions de StepFunction pourraient fonctionner parfaitement — nous avons déjà ajusté les timeouts. Je vous ai emmené dans ce détour de débogage pour vous donner un aperçu du dépannage de StepFunction, certes un peu amer. Du côté positif, une fois déboguées, les StepFunctions fonctionnent de manière fiable comme des voitures Toyota.

En tant que développeur back-end, je suis tenté d'en rester là. Mais pour en faire un « exemple complet », nous avons besoin d'une chose de plus. **Le front-end Web.**

Arrêtons-nous là pour aujourd'hui et gardons la partie web et les conclusions pour le prochain et dernier épisode.

[**Épisode 4**](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6)** : Ajout du front-end Web, réflexion et résumé**

J'espère que cela vous a aidé à apprendre quelque chose de nouveau, à trouver quelque chose d'intéressant ou a suscité de bonnes réflexions. N'hésitez pas à partager vos réflexions dans les commentaires ici, ou à me tweeter [@dzimine](https://twitter.com/dzimine).