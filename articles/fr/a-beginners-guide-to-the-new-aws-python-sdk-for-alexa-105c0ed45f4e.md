---
title: Guide du débutant pour le nouveau SDK Python AWS pour Alexa
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-06T16:39:05.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-the-new-aws-python-sdk-for-alexa-105c0ed45f4e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KXhtoJEi5p_7jsgXFPxZwA.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Guide du débutant pour le nouveau SDK Python AWS pour Alexa
seo_desc: 'By Ralu Bolovan

  Amazon Web Services (AWS) recently added a new Python SDK to their Alexa family.
  It is currently in beta, but that should not stop us from getting some exposure.

  What we’ll build: a very simple voice app that can say 10 facts about ca...'
---

Par Ralu Bolovan

Amazon Web Services (AWS) a récemment ajouté un nouveau [SDK Python](https://github.com/alexa-labs/alexa-skills-kit-sdk-for-python) à leur famille Alexa. Il est actuellement en version bêta, mais cela ne devrait pas nous empêcher de nous y exposer.

**Ce que nous allons construire :** une application vocale très simple qui peut dire 10 [faits sur les chats](https://www.factretriever.com/cat-facts).

**Pourquoi nous allons la construire :** Le concept de l'application est suffisamment simple pour que nous puissions nous concentrer sur la manière de travailler avec le SDK et sur la manière d'utiliser DynamoDB pour persister les données les plus importantes de notre application.

**À la fin de ce tutoriel, vous repartirez avec :**

1. Ce que chaque type de requête principal d'Alexa fait et comment construire le vôtre.
2. Une compréhension de la manière dont vous pouvez persister les données de votre application dans DynamoDB et éviter les pièges.
3. Voir les deux styles Python pour Alexa en action et choisir votre préféré.
4. Des conseils Python.
5. Des conseils pour la console Alexa.

**Prérequis :**

1. [Compte AWS](https://aws.amazon.com/free/)

2. [Compte développeur AWS](https://developer.amazon.com/alexa) (si vous souhaitez tester sur votre appareil enregistré, par exemple un Echo, inscrivez-vous avec la même adresse e-mail que votre compte Amazon)

3. Python 3.6

Si vous êtes toujours avec moi, commençons !

### **Alexa : ce qui se passe derrière les scènes (vue d'ensemble)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*omv7_w5zSLPlZp5rdAYCZA.png)

Pour illustrer l'idée principale derrière une interaction avec Alexa, regardons le lancement d'une compétence fictive appelée « My example ».

Lorsque l'utilisateur dit : « Open My example », le terme « My example » est le **nom d'invocation** de la compétence, que Alexa utilise pour communiquer. L'appareil de l'utilisateur transmet ce que l'utilisateur a dit à la compétence « My example ».

À ce stade, Alexa utilise le **modèle d'interaction** de la compétence pour comprendre ce que l'utilisateur a demandé. Le modèle d'interaction est un fichier JSON qui mappe ce que l'utilisateur dit à un type de requête. Dans ce cas, il le mappera à la requête intégrée `AMAZON.LaunchRequest`.

Ensuite, il appelle son backend, une **fonction AWS Lambda**, qui reçoit la requête identifiée.

La Lambda recherche une fonction qui peut gérer la LaunchRequest et l'exécute.

Cette fonction retourne ensuite une réponse qui est envoyée jusqu'à l'appareil de l'utilisateur. À ce stade, la compétence « My example » les saluera et sera en mesure d'accepter d'autres requêtes de l'utilisateur.

**Passons aux choses sérieuses !**

### **Aperçu de l'architecture**

![Image](https://cdn-media-1.freecodecamp.org/images/1*yzOlEyRRn39ieFNx8e7pgQ.png)

Maintenant que nous avons compris l'idée principale derrière l'invocation d'une compétence Alexa, explorons comment nous allons créer notre compétence d'exemple « Cat Facts ».

L'architecture est similaire à celle que nous avons discutée : une compétence Alexa qui invoque une fonction Lambda pour traiter la requête identifiée et retourne une réponse à dire à l'utilisateur.

Nous avons deux ajouts : **DynamoDB** et **IAM.**

#### DynamoDB

Notre compétence va suivre l'index du dernier fait que notre utilisateur a entendu de notre liste de dix faits sur les chats. Elle utilise DynamoDB pour persister l'index et le nombre de fois où l'utilisateur a ouvert notre compétence.

#### **IAM**

Nous en aurons besoin à deux endroits :

* Tout d'abord, un rôle pour notre Lambda afin qu'elle puisse interagir avec DynamoDB pour persister les données de nos utilisateurs. Nous devons également lui accorder des permissions CloudWatchLogs pour écrire des détails importants sur les requêtes que nous recevons.
* Ensuite, nous aurons besoin d'une permission Lambda pour permettre à notre compétence Alexa d'invoquer notre Lambda comme son backend.

### **Implémentation**

#### Compétence Alexa

Allez dans votre console développeur Alexa et cliquez sur « Create Skill ». Nommez la compétence « Cat Facts » et choisissez votre locale anglais préféré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EDYm5NiDGnMdDE3b4NySWQ.png)

Ajoutez le nom d'invocation : « cat facts ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*cw6hvxU48PW_rLQd7IfNmg.png)

Ajoutez le modèle d'interaction suivant à l'éditeur JSON de la console :

```
{    "interactionModel": {        "languageModel": {            "invocationName": "cat facts",            "intents": [                {                    "name": "AMAZON.CancelIntent",                    "samples": []                },                {                    "name": "AMAZON.HelpIntent",                    "samples": []                },                {                    "name": "AMAZON.StopIntent",                    "samples": []                },                {                    "name": "AMAZON.StartOverIntent",                    "samples": [                        "start",                        "start a new game",                        "restart",                        "restart game"                    ]                },                {                    "name": "AMAZON.YesIntent",                    "samples": []                },                {                    "name": "AMAZON.NoIntent",                    "samples": []                },                {                    "name": "AMAZON.FallbackIntent",                    "samples": []                },                {                    "name": "FactNumberIntent",                    "slots": [                        {                            "name": "fact_number",                            "type": "AMAZON.NUMBER"                        }                    ],                    "samples": [                        "{fact_number}",                        "I want {fact_number}",                        "I want fact {fact_number}",                        "I want fact number {fact_number}",                        "Tell me {fact_number}",                        "Tell me fact {fact_number}",                        "Tell me fact number {fact_number}"                    ]                }            ],            "types": []        }    }}
```

Cliquez sur le bouton « Save Model ».

#### **Conseil :**

Pour les ressources AWS, utilisez une [région supportée par Alexa](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#about-lambda-functions-and-custom-skills) :

* Asie Pacifique (Tokyo)
* UE (Irlande)
* US East (N. Virginie)
* US West (Oregon)

#### Table DynamoDB

Dans la console, allez dans DynamoDB et créez une nouvelle table appelée « cat_facts ». Nommez la clé de partition : « id ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*liDporQWoAV9Xyc8QldeLQ.png)

#### IAM

Nous allons maintenant créer la politique IAM que nous attacherons au rôle de notre Lambda.

Allez dans « Services » -> « IAM » -> « Policies » et cliquez sur « Create policy ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*yDu-BZuwSrTqPoirOzFtTw.png)

Ensuite, collez la politique suivante dans l'éditeur JSON et cliquez sur « Review policy ».

```
{    "Version": "2012-10-17",    "Statement": [        {            "Sid": "",            "Effect": "Allow",            "Action": [                "dynamodb:BatchGetItem",                "dynamodb:BatchWriteItem",                "dynamodb:PutItem",                "dynamodb:ListTables",                "dynamodb:DeleteItem",                "dynamodb:Scan",                "dynamodb:ListTagsOfResource",                "dynamodb:Query",                "dynamodb:UpdateItem",                "dynamodb:DescribeTimeToLive",                "dynamodb:CreateTable",                "dynamodb:DescribeTable",                "dynamodb:GetItem",                "dynamodb:DescribeLimits",                "dynamodb:UpdateTable",                "logs:CreateLogGroup",                "logs:PutLogEvents",                "logs:CreateLogStream"            ],            "Resource": "*"        }    ]}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QsZqQan1OhmKIPG7wYAGfg.png)

Nommez la politique « Cat_Facts_Policy » et terminez en sélectionnant « Create policy ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*u4EUtDigRajvVONH7P2VLA.png)

Nous voulons ensuite attacher cette politique à un rôle Lambda. Retournez dans « IAM » -> « Roles » et choisissez « Create role ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*gcn724g5JUYWHdnF02aYHg.png)

Ensuite, nous choisissons le service « Lambda » et cliquons sur « Next: Permissions ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*uv9YLK9Tho0Eh6SseZd-6Q.png)

Nous attachons la politique « Cat_Facts_Policy » et cliquons sur « Next: Review ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*nwxv6_eVvFV1CkWRrQcZkQ.png)

Nous terminons en donnant à notre rôle le nom « Cat_Facts_Lambda_Role » et en cliquant sur « Create role ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*-o2ynvixuzuWohGiFR6oIA.png)

#### Code Lambda

Dans votre terminal, créez un nouveau dossier :

`mkdir alexa_cat_facts_skill`

Dans ce dossier, créez un nouveau répertoire pour la Lambda :

```
cd alexa_cat_facts_skill/mkdir lambda
```

Dans le dossier lambda, créez un nouvel environnement virtuel. L'environnement virtuel nous permet de garder les bibliothèques de notre compétence séparées de celles de tout autre projet Python.

```
cd lambdapython3 -m venv catfactsenvsource catfactsenv/bin/activatepip install ask-sdkdeactivate
```

**Conseil pour Windows** : Pour activer l'environnement virtuel, exécutez ce qui suit : `catfactsenv\Scripts\activate.bat`

### **Styles Python de classe et de décorateur**

Le SDK Python nous offre deux façons d'écrire nos interactions Alexa : soit en utilisant des classes, soit en utilisant des décorateurs.

Nous allons maintenant faire une comparaison entre les deux styles tout en regardant les requêtes que nous voulons supporter dans le cadre de notre application. Nous atteindrons la même fonctionnalité exacte.

Créez deux nouveaux fichiers Python, un pour chaque style :

```
touch catfacts_classes_lambda.pytouch catfacts_decorators_lambda.py
```

#### **Imports**

Dans les deux cas, nous importons le module « os » pour récupérer les variables d'environnement que nous passons à notre Lambda — dans ce cas, le nom de la table DynamoDB pour persister les données de nos utilisateurs.

Les [SkillBuilders](https://alexa-skills-kit-python-sdk.readthedocs.io/en/latest/SKILL_BUILDERS.html) sont des classes qui nous facilitent l'attachement de composants capables de gérer les requêtes de nos utilisateurs et de générer des réponses appropriées.

Nous importons le « StandardSkillBuilder », qui offre un support DynamoDB prêt à l'emploi. Il s'intègre également avec le client API par défaut, obtenant des détails de base sur l'appareil de l'utilisateur.

Nous créons une nouvelle instance à laquelle nous passons le nom de la table DynamoDB. Nous voulons utiliser l'**ID utilisateur** qu'Alexa nous donne comme clé de partition de notre table. Nous faisons cela en spécifiant une fonction d'assistance intégrée appelée `user_id_partition_keygen`, qui extrait l'ID de l'utilisateur des requêtes entrantes.

Nous incluons les fonctions `is_request_type, is_intent_name` pour nous aider à déterminer plus tard les requêtes que la compétence a envoyées.

Nous importons `ask_sdk_dynamodb` pour extraire des informations de nos données Dynamo.

#### **Classes**

Dans le cas des classes, nous introduisons quatre classes abstraites que nous allons implémenter pour que notre compétence fonctionne :

* `AbstractRequestHandler` — cette classe est capable de traiter les requêtes de l'utilisateur et de retourner une réponse appropriée
* `AbstractExceptionHandler` — pour gérer les exceptions
* `AbstractRequestInterceptor` — s'exécute avant une requête
* `AbstractResponseInterceptor` — s'exécute après une requête

#### Décorateurs

#### Conseil

Nous aurions pu créer notre table DynamoDB dans la Lambda en définissant `auto_create_table=True`. Le problème est que cela est une fonction asynchrone, donc le premier utilisateur de l'application aurait rencontré des erreurs pendant l'initialisation de la table.

### **Données**

![Image](https://cdn-media-1.freecodecamp.org/images/1*geeTCtC8oyP7hndU6bc-5g.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/VvO8e8n0Ffg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Tucker Good</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Nous stockons les dix faits sur les chats dans une **liste** pour les deux versions du code.

Nous allons examiner chaque classe abstraite que nous devons implémenter une fois, puis nous concentrer sur le code, car la syntaxe reste la même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uRp--u-it_aiPppRR8a1Bg.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/E_mHYosg98k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Rahul Chakraborty</a> sur <a href="https://unsplash.com/search/photos/alexa?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### **HandlerInput**

Chaque fois que nous devons traiter une requête, une exception, ou intercepter une requête avant ou après l'avoir traitée, ce qui rend cela possible est un objet **HandlerInput** (dans le code, `handler_input`). Il contient tout ce dont nous avons besoin pour comprendre l'état de notre compétence.

Le HandlerInput offre les attributs suivants pour que nous puissions les utiliser :

* `request_envelope` : le corps entier de la requête
* `attributes_manager` : un moyen facile d'accéder aux attributs de requête, de session et persistants
* `service_client_factory` : construit des clients API qui peuvent effectuer des fonctions pour nous comme récupérer le nom et l'adresse de l'utilisateur, ou faire des achats
* `response_builder` : moyen de construire la réponse que nous voulons passer à notre utilisateur
* `context` : un objet optionnel qui est passé par le service qui exécute le code de la compétence. Pour un backend Lambda, il s'agit de l'objet context qui nous donne des informations comme le temps restant jusqu'à ce qu'AWS termine notre Lambda.

### **LaunchRequest**

![Image](https://cdn-media-1.freecodecamp.org/images/1*_9sfjL1W97gNTdMVbAh_hw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/OHOU-5UVIYQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">SpaceX</a> sur <a href="https://unsplash.com/search/photos/launch?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### **_Classes_**

Pour tous les types de requêtes qui mappent à une intention, nous devons implémenter les méthodes de classe `AbstractRequestHandler` `can_handle` et `handle`.

Nous déterminons d'abord si la classe peut traiter la requête entrante. Pour cela, nous utilisons la fonction `is_request_type`. Celle-ci prend un type de requête — dans notre cas, **LaunchRequest** — et retourne une fonction prédicat. Nous passons ensuite le `handler_input` à ce prédicat, qui vérifie si la requête entrante lance l'application ou non.

Si c'est une **LaunchRequest**, nous pouvons la traiter. Comme le lancement est la porte d'entrée de notre application, nous voulons voir si cet utilisateur a déjà utilisé notre application afin que nous puissions personnaliser son expérience. Nous faisons cela en utilisant l'attribut `attributes_manager` de `handler_input` pour récupérer les `persistent_attributes` de notre table DynamoDB cat_facts.

En arrière-plan, il appelle la fonction `partition_keygen` que nous avons utilisée pour créer l'instance `StandardSkillBuilder`.

Dans notre cas, nous sommes intéressés par le fait que l'**identifiant de l'utilisateur** soit la clé de partition. Une fois qu'il a récupéré l'ID utilisateur en utilisant cette fonction à partir de l'enveloppe de la requête, il interroge ensuite la colonne « id » de la table DynamoDB pour voir s'il y a une entrée pour cet utilisateur dans notre table. Si c'est le cas, il retourne un dictionnaire contenant tous les noms et valeurs des attributs, sinon un dictionnaire vide.

S'il n'y a pas de correspondance, nous enregistrons que cet utilisateur n'a pas joué à notre jeu auparavant. De plus, nous ajoutons l'index du fait actuel de notre liste cat_facts, qui est -1 car l'utilisateur n'a écouté aucun fait.

Nous pointons le contenu des `persistent_attributes` vers `session_attributes`. Nous utiliserons les attributs de session tout au long de l'application, chaque fois que nous modifions un champ. Cela nous aidera non seulement à maintenir l'état de notre application, mais aussi à éviter de faire des appels inutiles à notre table DynamoDB.

Pour démontrer la fonctionnalité, nous supposons que l'utilisateur peut jouer tant qu'il n'a pas écouté tous les dix faits.

S'ils ont écouté tous les faits, nous leur demandons s'ils veulent recommencer. S'ils veulent redémarrer, nous commençons à jouer les faits dans l'ordre croissant du premier au dernier.

Nous utilisons ensuite le `response_builder` pour créer notre réponse. Nous utilisons sa fonction `speak` pour faire dire la réponse par l'appareil de l'utilisateur. S'ils n'ont pas répondu en huit secondes, la commande « ask » les relancera automatiquement pour une réponse.

#### Décorateurs

Le code du gestionnaire est le même que pour la version avec classes. La syntaxe diffère en ce sens que nous utilisons la fonction `request_handler` de l'objet `StandardSkillBuilder` pour décorer notre fonction. Nous devons lui passer un paramètre `can_handle_func`, qui doit mapper à une fonction. Nous utilisons la même méthode `is_request_type`, qui nous retourne la fonction nécessaire pour que ce décorateur fonctionne.

#### **Conseils Python :**

Nous avons utilisé `attr.set_default("facts_index", -1)` qui vérifie s'il y a une clé `facts_index` dans notre dictionnaire « attr » et la définit à -1 si ce n'est pas le cas. Sinon, la valeur n'est pas modifiée.

Pour Python 3.6, nous pouvons utiliser des chaînes « f » ou des chaînes formatées, qui sont des expressions évaluées à l'exécution. Elles sont plus rapides et plus lisibles que d'autres façons de formater.

### **FactNumberIntent**

Il s'agit d'un type de requête **personnalisé** que nous définissons. Nous voulons permettre à notre utilisateur de demander un numéro de fait de 1 à 10, en plus de parcourir la liste des faits dans l'ordre.

#### Classes

Le point intéressant ici est que cette requête nous passera le numéro du fait que l'utilisateur veut via un slot. Un slot est un argument donné à une intention.

Dans notre **modèle d'interaction** que nous avons défini dans notre console Alexa, nous disons à Alexa que nous pouvons supporter un utilisateur disant un nombre et qu'il doit être mappé à un via le `Amazon.NUMBER` intégré :

```
{                    "name": "FactNumberIntent",                    "slots": [                        {                            "name": "fact_number",                            "type": "AMAZON.NUMBER"                        }                    ],                    "samples": [                        "{fact_number}",                        "I want {fact_number}",                        "I want fact {fact_number}",                        "I want fact number {fact_number}",                        "Tell me {fact_number}",                        "Tell me fact {fact_number}",                        "Tell me fact number {fact_number}"                    ]                }
```

Du côté Lambda, nous savons que nous allons recevoir un nombre. Nous obtenons tous les slots de l'intention, puis transformons cette valeur en un entier.

Nous nous assurons que le nombre peut être mappé à un index, et nous retournons le fait. Sinon, nous demandons à l'utilisateur un autre nombre que nous supportons.

Nous utilisons la fonction `is_intent_name` pour déterminer que nous traitons le `FactNumberIntent`.

#### **_Décorateurs_**

### **StartOverIntent**

Il s'agit d'une intention intégrée AMAZON utilisée pour redémarrer des jeux, des pistes audio ou des transactions. Dans notre cas, redémarrer signifie réinitialiser le `facts_index`.

#### **_Classes_**

#### **_Décorateurs_**

### HelpIntent:

Une intention intégrée AMAZON pour guider l'utilisateur.

#### **_Classes_**

#### **_Décorateurs_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*eAdqKoWkI9p3NnQdx94yHw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/dJdcb11aboQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">John Matychuk</a> sur <a href="https://unsplash.com/search/photos/stop?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### StopOrCancelIntent

Ici, nous avons combiné le traitement des intentions intégrées `AMAZON.StopIntent` et `AMAZON.CancelIntent` pour **mettre fin explicitement** à la session de l'utilisateur en définissant `set_should_end_session` sur « True » dans le `response_builder`.

#### **_Classes_**

Nous persistons les `session_attributes` collectés dans DynamoDB en appelant notre fonction d'assistance `persist_user_attributes`. Nous augmentons également le nombre de fois où cet utilisateur a interagi avec notre application.

La fonction `save_persistent_attributes` sauvegardera les attributs dans DynamoDB. Cela utilise la fonction `partition_keygen` de l'instance du constructeur de compétences pour obtenir l'userId à utiliser comme clé de partition. Cela est fait en arrière-plan.

#### **_Décorateur_** :

Pour le `can_handle_func`, nous créons notre propre fonction en ligne, en utilisant l'opérateur lambda de Python, où nous passons le `handler_input` à vérifier contre le `StopIntent` et le `CancelIntent`. Dans ce cas, nous devons invoquer explicitement la fonction `is_intent_name` avec ces deux entrées, ce qui retournera un booléen. Parce que nous utilisons lambda, le résultat sera une **fonction prédicat**, qui est ce dont le `can_handle_func` a besoin.

### **SessionEndedRequest**

Nous utilisons la fonction `is_request_type` pour déterminer si la session a été terminée. Cela se produit lorsque l'utilisateur dit « Exit » — nous ne recevons pas de réponse qui peut être mappée à une intention, ou une erreur se produit. Cela **n'est pas** invoqué lors de la fin explicite de la session en utilisant `set_should_end_session`, donc nous devons **nous assurer** que nous persistons les attributs dans les deux cas.

#### **_Classes_**

#### **_Décorateurs_**

### YesIntent

![Image](https://cdn-media-1.freecodecamp.org/images/1*m6ZnbHd-WYfoCK_qmGazmQ.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/qAZO-wu3tik?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jon Tyson</a> sur <a href="https://unsplash.com/search/photos/yes?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Il s'agit d'une intention intégrée pour les réponses affirmatives à une question oui/non. Nous gardons les choses très basiques. Nous vérifions si un nouveau fait peut être récupéré et, si ce n'est pas le cas, nous demandons à l'utilisateur de redémarrer le jeu. Sinon, nous lui disons le fait et lui demandons s'il veut en entendre un autre.

#### **Classes**

#### **_Décorateurs_**

### **_NoIntent_**

Il s'agit d'une intention intégrée pour les réponses négatives à une question oui/non. Nous choisissons de mettre fin à la session et de persister les attributs de session dans DynamoDB.

#### **_Classes_**

#### **_Décorateurs_**

### **FallbackIntent**

Une autre intention intégrée AMAZON qui est supportée au moment de l'écriture en locales anglaises.

Elle fournit un mécanisme de repli lorsque l'utilisateur dit quelque chose qui ne correspond à aucune des intentions de notre compétence.

#### **_Classes_**

#### **_Décorateurs_**

### AllException

![Image](https://cdn-media-1.freecodecamp.org/images/1*YTUHn_RHY5DtEKj8siWBNA.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/tEMU4lzAL0w?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">FuYong Hua</a> sur <a href="https://unsplash.com/search/photos/angry-cat?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Pour garder les choses simples, nous voulons utiliser ce gestionnaire pour gérer chaque exception possible.

#### **_Classes_**

Nous devons implémenter la méthode `can_handle` à laquelle nous passons le `handler_input` et l'`exception`. Nous voulons que cette fonction gère toutes les exceptions, mais pour des cas plus spécialisés, nous pourrions examiner les classes d'exception et avoir des moyens spécifiques de les gérer.

Dans la fonction `handle`, nous passons le `handler_input` et l'`exception` et nous retournons un message simple.

#### **_Décorateur_**

Pour la version décorateur, nous devons passer à `can_handle_func` une fonction qui prend en entrée le `handler_input` et l'`exception` et retourne un booléen. La fonction qui est décorée reçoit ces deux paramètres.

### **GlobalRequestInterceptor**

Nous utilisons l'intercepteur de requête global pour exécuter du code avant que le gestionnaire de chaque requête ne soit invoqué. Dans notre cas, nous voulons enregistrer la requête que nous avons reçue. Nous voulons également journaliser l'ID de l'utilisateur et l'ID de son appareil.

#### **_Classes_**

#### **_Décorateurs_**

Pour les décorateurs, l'intercepteur de requête global est invoqué directement en tant que fonction. Il a besoin de l'instance du constructeur de compétences pour enregistrer l'intercepteur en notre nom.

#### Fonctions d'assistance

Les fonctions `get_device_id` et `get_user_id` sont deux fonctions d'assistance pour montrer comment extraire le **deviceId** et le **userId** de la requête en utilisant le package `ask_dynamo_db`.

Nous pouvons utiliser `ask_sdk_dynamodb.partition_keygen.device_id_partition_keygen` et `ask_sdk_dynamodb.partition_keygen.user_id_partition_keygen` comme les getters de clé de partition pour notre table. Lorsque nous avons créé notre instance de constructeur de compétences, nous avons utilisé la deuxième fonction.

### **GlobalResponseInterceptor**

Similaire à l'intercepteur de requête global, l'intercepteur de réponse global est utilisé pour exécuter du code après que le gestionnaire de toute requête ait été invoqué. Ici, nous allons simplement journaliser la réponse que nous renvoyons à l'utilisateur.

#### **_Classes_**

#### **_Décorateurs_**

### **Enregistrement et appel de nos gestionnaires :**

Les intercepteurs de requête et de réponse sont exécutés dans le **même ordre** que celui dans lequel ils sont enregistrés.

#### **_Classes_**

Nous devons explicitement enregistrer chaque gestionnaire de requête, chaque gestionnaire d'exception, et les intercepteurs de requête et de réponse globaux.

Nous créons ensuite un `lambda_handler` qui peut être utilisé par notre Lambda comme la passerelle pour invoquer tous les gestionnaires supportés.

#### **_Décorateurs_**

Nous n'avons pas besoin d'enregistrer explicitement les gestionnaires car cela est fait directement par les décorateurs. Mais nous devons faire attention à l'ordre dans lequel nous avons écrit les gestionnaires car c'est l'ordre dans lequel ils seront exécutés.

**Nous avons officiellement terminé avec la partie syntaxe et la compréhension de ce qui entre dans notre code.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*CrV7P6lwXSHU7X9XA8M_Dg.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/lpgAlv8I7V8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Nine K6pfer</a> sur <a href="https://unsplash.com/search/photos/happy-cat?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### **Emballage de notre code Python**

Parce que nous utilisons des bibliothèques Python non standard comme le SDK Python AWS, nous devons les emballer avec notre code Lambda.

La façon dont nous y parvenons est en créant un script bash qui fera le travail pour nous. Dans le répertoire « alexa_cat_facts_skill », créez un nouveau fichier bash : « create_lambda_package.sh »

```
cd ..touch create_lambda_package.sh
```

Ajoutez ce qui suit au nouveau fichier bash. Cela va zipper les bibliothèques Python ainsi que les deux versions de notre code dans un package appelé « lambda_package.zip ».

```
#!/bin/bash
```

```
BASEDIR=$(pwd)rm -rf $BASEDIR/lambda_package.zipcd  $BASEDIR/lambda/catfactsenv/lib/python3.6/site-packages/zip -r9 $BASEDIR/lambda_package.zip *cd $BASEDIR/lambda/catfactsenv/lib64/python3.6/site-packages/zip -r9 $BASEDIR/lambda_package.zip *cd $BASEDIR/lambda
```

```
zip -r9 $BASEDIR/lambda_package.zip catfacts_classes_lambda.py catfacts_decorators_lambda.py
```

Exécutez le script bash : `bash -x create_lambda_package.sh`

#### Conseil pour Windows

Les bibliothèques Python se trouveront plutôt sous `catfactsenv\Lib\site-packages`.

### Configuration de la Lambda

Commencez par aller dans la « console AWS » -> « Services » -> « Lambda »

![Image](https://cdn-media-1.freecodecamp.org/images/1*-6tNDJs_PPLV9BujEWUknA.png)

Nous allons créer à partir de zéro. Nommez la Lambda : « cat_facts_lambda ». Sélectionnez le runtime pour qu'il soit « Python 3.6 » et pour le rôle, choisissez le « Cat_Facts_Lambda_Role » que nous avons créé ci-dessus. Cliquez sur « Create function ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*A-pHeK-uOwZ1_72istedvQ.png)

Ajoutez la variable d'environnement « skill_persistence_table » avec la valeur `cat_facts`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQplJgz11GKCp70I5FQigw.png)

Augmentez le « Timeout ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*kQD88zEX6U51Sct7veVhzw.png)

Importez le code en téléchargeant le fichier « lambda_package.zip ». Ajoutez le gestionnaire de la Lambda pour qu'il soit : « catfacts_decorators_lambda.handler ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*bAqOTUtQRyJ5PRdZN4AwTA.png)

Enregistrez la fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MUP9AG3eCIpL25MSN8UxCg.png)

### Ajouter le déclencheur Alexa

Dans le menu « Designer » de la fonction, choisissez « Alexa Skills Kit ». Ensuite, cliquez sur le bouton avec le même nom pour corriger la configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*unM6u7JQlXJGuZB7UO3sYw.png)

Allez dans la **console développeur Alexa**, dans « Endpoint » et vous verrez l'**ID de la compétence**. Copiez-le dans votre presse-papiers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u4NWKYo5iPkgFTeMnDonlw.png)

Collez l'ID de la compétence dans la console Lambda, puis cliquez sur « Add ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*PgcHcn3bFkUdGj6abbCS7Q.png)

Enregistrez la fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qOX6XoSdEgGn65fC2g1dbg.png)

Ensuite, copiez l'**ARN de la Lambda** dans le coin supérieur droit de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pugX0mJFfgYOgL4VnwTtdQ.png)

### Fin de la configuration de la console Alexa

Sélectionnez « AWS Lambda ARN » dans « Endpoint », et collez l'ARN de la Lambda dans le champ « Default Region ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qz-FcVBQvEuks_cSAw9vlA.png)

Ensuite, allez dans « Build » -> « JSON Editor » -> « Save Model ». Une fois le modèle enregistré, cliquez sur « Build Model » pour que toutes nos modifications prennent effet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RH4TtKi2JxSbr4WgbrZQOg.png)

**Nous avons officiellement terminé notre configuration ! Félicitations pour être arrivé jusqu'ici !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*zeoEy9CP2sW_eh5boiQTgw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/mcLpPD36-2k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com/search/photos/success?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Test

Interagissons avec notre compétence directement depuis la console Alexa. Allez dans « Test » et activez le test pour que la compétence exécute le simulateur Alexa.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p3XkYN-2timIjfjQoMDTGw.png)

#### **Conseil pour la console Alexa**

Lors du test de FactNumberIntent, écrivez les nombres en caractères, par exemple « two » au lieu de « 2 ». Sinon, l'intention sera mappée à FallbackIntent.

#### Testons la version Décorateurs

Exécutons un scénario simple pour voir comment notre compétence se comporte. Nous sommes particulièrement intéressés par le test de l'intention de numéro de fait et de ses limites. N'hésitez pas à dire les commandes en cliquant et en maintenant l'icône du micro ou en les écrivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eSaa7uI33_6_nlIOQ5Njpw.png)

Voir les résultats dans DynamoDB en allant dans votre console AWS vers « Services »-> « DynamoDB » -> « Tables » -> « cat_facts ». Vous verrez un élément similaire, avec votre ID utilisateur comme clé de partition.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9XFx7vHaV_euCYhja0NwIw.png)

#### Testons la version Classes

Pour passer à la version classes de notre code, allez dans « Services » -> « Lambda » -> « cat_facts_lambda ». Le changement simple **est de** renommer le Handler de « catfacts_decorators_lambda.handler » à « catfacts_classes_lambda.handler ». « Enregistrez » la fonction et le changement se fait automatiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ifViBQbtOWV2FfAIxupuQ.png)

Faisons un autre test avec notre compétence Alexa, où nous voulons tester le comportement de redémarrage. Même si nous avons changé le code, le comportement est le même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UOs-a_jzDqHaMLX9aIzOdA.png)

Retournons à notre table DynamoDB et rafraîchissons notre page. Notre Lambda a réussi à enregistrer l'index du dernier fait entendu et que l'utilisateur a interagi avec la compétence deux fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XcfCBui8NpmEVdeY21-tng.png)

**Félicitations** ! Vous avez créé avec succès votre première compétence Alexa en utilisant le SDK Python. Vous savez maintenant comment persister les attributs pertinents dans DynamoDB, comment créer l'infrastructure de votre compétence, ce que font les principales intentions, comment créer les vôtres et comment faire répondre Lambda à toutes les intentions.

### **Améliorations possibles**

Nous **nous sommes spécifiquement** pas concentrés sur l'infrastructure telle que le code, git, les langues multiples, CI/CD, les tests et les APIs pour nos faits sur les chats. Cela aurait rendu le tutoriel beaucoup plus complexe et aurait détourné l'attention du sujet principal. Dans un environnement réel, ces éléments facilitent grandement notre vie.

Même si l'ajout de telles améliorations augmenterait notre productivité, savoir comment commencer et comment s'y prendre peut être accablant. Combiner les nouvelles tendances technologiques comme **l'IA**, **Serverless** et **DevOps**, nécessite de remplir de nombreux rôles en même temps, ce qui peut sembler insurmontable.

#### Obtenir plus d'aide

Mais que se passerait-il s'il existait un moyen de surmonter cet obstacle et d'être habilité à construire vos propres applications en utilisant ces concepts ? J'ai créé un cours qui démystifie ce processus. Vous pouvez le trouver [**ici**](http://pluralsight.pxf.io/c/1289732/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Faws-polly-voice-enabled-serverless-website), avec un essai gratuit en allant [**ici**](http://pluralsight.pxf.io/c/1289732/431405/7490).

Merci d'avoir pris le temps de lire cet article. Puisse-t-il être une pierre d'achoppement dans votre parcours pour créer quelque chose de grand !