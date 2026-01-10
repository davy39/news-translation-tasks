---
title: Comment améliorer le flux de conversation de votre compétence Alexa
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-26T14:57:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-the-conversation-flow-of-your-alexa-skill-1b6c6556f9a3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uQl2sV1anCMlYWFd
tags:
- name: Alexa Skills
  slug: alexa-skills
- name: development
  slug: development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment améliorer le flux de conversation de votre compétence Alexa
seo_desc: 'By Garrett Vargas

  Natural conversations are fluid. That’s one of the joys of face to face human conversation,
  you never know how the dialog will evolve. But sometimes, there is a natural flow
  to the conversation. Ask someone where they want to eat, a...'
---

Par Garrett Vargas

Les conversations naturelles sont fluides. C'est l'un des plaisirs de la conversation humaine en face à face, on ne sait jamais comment le dialogue va évoluer. Mais parfois, il y a un flux naturel à la conversation. Demandez à quelqu'un où il veut manger, et vous vous attendez à entendre un restaurant ou un type de nourriture, pas une réponse sur un film préféré.

L'une des frustrations que les gens ont avec les assistants vocaux est qu'ils font parfois un mauvais travail de compréhension de ce qu'ils disent. Amazon dispose d'un outil pour aider les développeurs tiers à fournir une meilleure reconnaissance. **Dialog Management** vous permet de demander des valeurs pour remplir une requête avec une précision accrue.

Par exemple, si vous créez une compétence qui recherche une location de voiture, Alexa peut demander à l'utilisateur une ville et des dates de voyage après qu'il ait dit « trouver une voiture ». La fonctionnalité intégrée d'Alexa améliore la précision de la reconnaissance vocale dans ce cas, car elle écoute des valeurs spécifiques.

Le problème est que l'utilisateur doit prononcer les mots appropriés pour déclencher une intention contrôlée par Dialog. Amazon a récemment annoncé [l'enchaînement d'intentions](https://developer.amazon.com/blogs/alexa/post/9ffdbddb-948a-4eff-8408-7e210282ed38/intent-chaining-for-alexa-skill) comme solution à ce problème.

Dans ce blog, je vais vous montrer comment j'utilise cette fonctionnalité avec une compétence qui permet à l'utilisateur d'effectuer une recherche de voiture. Tout d'abord, examinons comment Dialog Management fonctionne dans Alexa. Examinons une CarSearchIntent qui collecte les informations nécessaires pour lancer une recherche de voiture.

![Image](https://cdn-media-1.freecodecamp.org/images/fLRkwma7n9QfRGu2wv6bqzUZkahywAXANe-3)
_CarSearchIntent avec des slots pour le lieu et les dates de voyage_

Comme vous pouvez le voir, nous avons plusieurs variations sur la manière dont un utilisateur peut trouver une voiture, y compris des slots pour Location, PickUpDate et DropOffDate. Nous voulons nous assurer que l'utilisateur fournit ces trois slots avant de commencer à traiter la demande. Nous utilisons Dialog Management pour laisser Alexa demander à l'utilisateur de fournir ces informations.

![Image](https://cdn-media-1.freecodecamp.org/images/FCtaQRUn465AgEwF8Tyl0XcYk8UIVnOSS-O7)
_Lieu en tant que slot requis avec une invite_

En mode Dialog, Alexa a une meilleure chance de précision car elle essaie de remplir les slots pour cette intention. Mais pour entrer dans ce mode, l'utilisateur doit déclencher cette intention en disant « Trouver une voiture » ou une phrase similaire. Idéalement, nous placerions l'utilisateur dans ce mode dès qu'il lance la compétence.

Voici l'enchaînement d'intentions ! Nous pouvons ajouter une directive **Dialog Delegate** à notre réponse qui place l'utilisateur dans le flux de dialogue de CarSearchIntent.

```
canHandle(handlerInput) {  const request = handlerInput.requestEnvelope.request;  return handlerInput.requestEnvelope.session.new ||    (request.type === 'LaunchRequest');},handle: function(handlerInput) {  return handlerInput.responseBuilder    .addDelegateDirective({      name: 'CarSearchIntent',      confirmationStatus: 'NONE',      slots: {}    })    .speak("Bienvenue dans la recherche de voiture.")    .getResponse();}
```

La directive de dialogue nous permet de pré-remplir certains des slots (par exemple, nous pourrions définir par défaut le lieu à la dernière localisation de recherche utilisée). Ce qui est intéressant à noter, c'est que nous ne spécifions que « Bienvenue dans la recherche de voiture » comme réponse pour ce gestionnaire. Nous ne spécifions pas de nouvelle invite. Alexa ajoute l'invite de dialogue pour CarSearchIntent à notre réponse et l'utilise comme nouvelle invite. Donc, dans ce cas, ce que l'utilisateur entendra est « Bienvenue dans la recherche de voiture. Où souhaitez-vous récupérer la voiture ? » S'ils ne répondent pas, ils entendront une nouvelle invite « Où souhaitez-vous récupérer la voiture ? »

Vous avez également la possibilité de diriger l'utilisateur pour remplir un slot spécifique lorsqu'il est placé dans un dialogue. Supposons que nous voulons guider l'utilisateur pour qu'il spécifie d'abord la date de prise en charge de sa voiture. Nous pouvons le faire en utilisant une directive **Elicit Slot**, comme le montre le code suivant.

```
canHandle(handlerInput) {  const request = handlerInput.requestEnvelope.request;  return handlerInput.requestEnvelope.session.new ||    (request.type === 'LaunchRequest');},handle: function(handlerInput) {  return handlerInput.responseBuilder    .addElicitSlotDirective('PickUpDate', {      name: 'CarSearchIntent',      confirmationStatus: 'NONE',      slots: {}    })    .speak("Bienvenue dans la recherche de voiture. Quand souhaitez-vous récupérer votre voiture ?")    .reprompt("Quand souhaitez-vous récupérer votre voiture ?")    .getResponse();}
```

Dans ce cas, nous devons épeler tout le discours et la nouvelle invite que l'utilisateur entendra. Nous devons faire cela puisque nous contrôlons comment nous plaçons l'utilisateur dans le flux de gestion de dialogue.

L'enchaînement d'intentions vous permet de gérer le flux de conversation de manière plus naturelle. Utilisez-le pour rendre votre compétence plus utilisable pour vos utilisateurs !