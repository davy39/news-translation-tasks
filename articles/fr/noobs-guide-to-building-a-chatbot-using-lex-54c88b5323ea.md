---
title: Guide du débutant pour construire un chatbot avec Lex
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-22T08:13:12.000Z'
originalURL: https://freecodecamp.org/news/noobs-guide-to-building-a-chatbot-using-lex-54c88b5323ea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mMawypMnD9wpQ0wPEnls-A.jpeg
tags:
- name: aws lambda
  slug: aws-lambda
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Guide du débutant pour construire un chatbot avec Lex
seo_desc: 'By Srinivasan C

  Recently, we built a chat bot for the AWS ChatBot Challenge using Amazon Lex. I
  learned a ton of things from that experience, and thought I would put up a tutorial
  so that people can get started easily with building a basic bot. Let’s...'
---

Par Srinivasan C

Récemment, nous avons construit un chatbot pour le AWS ChatBot Challenge en utilisant Amazon Lex. J'ai appris énormément de choses grâce à cette expérience et j'ai pensé mettre en place un tutoriel pour que les gens puissent commencer facilement à construire un bot de base. Plongeons-nous directement dedans.

### Premières étapes

Amazon Lex est un moteur qui analyse le langage naturel (ce que l'utilisateur dit) et le convertit en actions que le bot peut exécuter. Donc, lorsque vous dites « Je veux commander une pizza », Lex comprend que cette commande est une **action** que l'utilisateur souhaite effectuer. Il informe ensuite le bot afin qu'il puisse passer une commande de pizza.

La première étape consiste à comprendre les différentes parties mobiles impliquées dans Amazon Lex.

#### Intention

L'intention est un objectif particulier que l'utilisateur souhaite atteindre. Lorsque l'utilisateur dit « Je veux commander une pizza », **commander** est l'**intention**, c'est-à-dire l'action que l'utilisateur veut voir se produire. Il existe deux types d'intentions :

* [Intentions intégrées](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents) — Ce sont des intentions de base fournies par Lex. Vous pouvez les utiliser pour effectuer des actions standard comme permettre à un utilisateur d'annuler, d'obtenir de l'aide, etc.
* Intentions personnalisées — Les intentions personnalisées sont fournies par les développeurs pour effectuer un ensemble spécifique d'actions. Nous discuterons de la création d'une intention personnalisée en détail dans la seconde partie de cet article.

#### Énoncés

Les énoncés sont les phrases utilisées pour invoquer une intention. « Je veux commander une pizza » est l'énoncé utilisé pour invoquer OrderIntent.

#### Emplacements

Les emplacements sont les entrées que l'utilisateur doit fournir pour réaliser l'intention. Vous pouvez vouloir connaître le **type de pizza** pour OrderIntent, qui est un emplacement. Vous pouvez soit créer des types d'emplacements personnalisés pour votre usage, soit utiliser les types intégrés. Les types intégrés fournissent des valeurs pour des énumérations standard comme la date, le nom, le nom du pays, etc., que vous pouvez vouloir obtenir de l'utilisateur.

#### Invites

Les invites sont les questions posées pour obtenir une entrée de l'utilisateur. Elles sont utilisées pour **demander des valeurs pour les emplacements** à l'utilisateur. Elles attendent la réponse de l'utilisateur et remplissent l'emplacement avec la réponse donnée par l'utilisateur. Une invite peut être « Quel type de pizza souhaitez-vous commander ? » pour OrderIntent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZ6O8hsOzEaL5CpP1OXI7w.png)
_Composants d'un chatbot_

### Pratique

Si vous n'avez pas de compte Amazon, créez-en un et allez à Lex dans votre console Amazon.

Maintenant, construisons un petit bot de salutation. Le bot de salutation demande votre nom et vous salue par votre nom. Assez simple, n'est-ce pas ? Commençons à construire un bot fonctionnel.

1. Créez un nouveau bot et nommez-le « Greeter » ou ce que vous voulez.
2. Allez dans le bot que vous avez créé et créez une nouvelle **intention personnalisée**.
3. Lorsque vous créez une intention personnalisée, vous devez fournir des **énoncés** pour invoquer l'intention. Pour notre bot de salutation, les énoncés peuvent être **Salut, hey, bonjour**, etc.
4. Maintenant, nous devons fournir un **emplacement** pour obtenir le nom de l'utilisateur. Nous pouvons utiliser le type d'emplacement intégré **AMAZON.US_FIRST_NAME** à cet effet. Donnez le nom comme « Name » (la casse compte pour que le code fourni plus tard fonctionne) et l'**invite** comme « Quel est votre nom ? » ou ce que vous voulez, et sauvegardez l'emplacement.
5. Fournissez la réalisation comme **Retourner les paramètres au client** pour l'instant et sauvegardez l'intention.

L'intention devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*AMeUTAawohKlO5ZadWyCDQ.png)
_Intention de salutation_

Vous pouvez maintenant **construire** votre bot et le tester. Vous pouvez l'invoquer en disant **salut** et il vous demandera votre nom et attendra votre entrée. Si vous fournissez le nom, il imprimera **ReadyForFulfillment** et le nom que vous avez donné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0jDVTCsHoA1dw5Glcv2xuw.png)
_Test initial du bot_

#### Réponses JSON et actions de dialogue

Ce que nous avons fait jusqu'à présent est suffisant si votre bot veut simplement lire votre nom. Mais nous voulons que le bot vous rappelle par votre nom, nous devons donc fournir une réponse au bot dans le format qu'il comprend. Lex définit un format JSON qu'il attend pour la conversation du bot. Le format de base est quelque chose comme celui donné ci-dessous :

```js
{
    "sessionAttributes": {
    "key1": "value1",
    "key2": "value2"
    ...
  },
  "
dialogAction": {
    "type": "ElicitIntent, ElicitSlot, ConfirmIntent, Delegate, or Close"    
  }
}
```

L'action de dialogue vous permet de décider de la prochaine action pour votre bot. Nous avons besoin de l'action de dialogue de type **Close** pour accomplir notre tâche prévue. Vous pouvez lire plus sur les autres actions de dialogue et leurs formats de réponse [ici](http://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html#using-lambda-response-format).

L'action Close vous permet de terminer la conversation avec ou sans envoyer une réponse à l'utilisateur. Nous pouvons donc l'utiliser pour appeler l'utilisateur par son nom et terminer la conversation. Notre réponse ressemblera à ceci :

```js
{
 "dialogAction":
 {
  "fulfillmentState":"Fulfilled",
  "type":"
Close",
  "message":{
   "contentType":"PlainText","content": "Salut "+ 
name +", content de te voir !"
  }
 }
}
```

Vous avez peut-être remarqué que nous devons lire le **nom** à partir de la réponse de l'utilisateur. Nous devons donc écrire un peu de code et obtenir le nom à partir des paramètres et envoyer la réponse ci-dessus au bot. C'est là qu'intervient Lambda.

#### Présentation de Lambda

AWS Lambda vous permet d'exécuter du code sans provisionner ni gérer de serveurs. Vous pouvez donc écrire une fonction Lambda et la connecter à votre intention pour envoyer la réponse spécifique que vous attendez pour cette intention.

Créons la Lambda dont nous avons besoin.

1. Allez dans la console Lambda et cliquez sur **Créer une nouvelle fonction Lambda**.
2. Sélectionnez **Fonction vide** et cliquez sur suivant.
3. Nous n'avons pas besoin de déclencheurs, cliquez donc sur suivant.
4. Fournissez un nom pour la lambda et choisissez le runtime comme **Python 2.7**.
5. Copiez-collez le code ci-dessous dans l'éditeur :

```js
def lambda_handler(event, context):
    name = event["currentIntent"]["slots"]["Name"].title()
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close","message":
                        {
                          "contentType":"PlainText",
                          "content": "Salut "+name+", content de te voir !"
                        }
                    }
                }
    return response
```

6. Fournissez un rôle existant ou créez un nouveau rôle pour la Lambda et créez la Lambda.

Maintenant que notre Lambda est créée, la seule chose que nous devons faire est de la connecter pour servir notre intention.

#### Connexion de Lambda et de l'intention

1. Allez dans la console Lex et sélectionnez le bot.
2. Allez dans l'intention Greeter que nous avons créée.
3. Sélectionnez le menu déroulant de la version près du nom de l'intention comme **latest** pour l'éditer.
4. Changez le **type de réalisation en fonction AWS Lambda**.
5. Sélectionnez la Lambda que nous avons créée dans le menu déroulant et sauvegardez l'intention.

C'est tout ! Notre bot est maintenant prêt. Vous pouvez **construire** le bot et le tester, et la conversation devrait se dérouler comme suit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7PG-0D-lAJxvsw19L_FCgA.png)
_Bot de salutation !_

Merci d'avoir lu mon article. J'espère que vous avez appris quelque chose. Je prévois d'écrire une suite à cela, qui nous permettra d'intégrer ce bot avec Facebook ou Slack. N'hésitez pas à laisser vos commentaires et vos retours.

Si vous avez aimé cet article, n'hésitez pas à me contacter à l'adresse suivante : https://kaizencoder.com/contact.