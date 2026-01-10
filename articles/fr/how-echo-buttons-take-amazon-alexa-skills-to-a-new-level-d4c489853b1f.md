---
title: Comment les boutons Echo font passer les compétences Amazon Alexa à un niveau
  supérieur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T23:49:51.000Z'
originalURL: https://freecodecamp.org/news/how-echo-buttons-take-amazon-alexa-skills-to-a-new-level-d4c489853b1f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F6CHpSv0t3e2ntNu0iDygw.jpeg
tags:
- name: amazon echo
  slug: amazon-echo
- name: baseball
  slug: baseball
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment les boutons Echo font passer les compétences Amazon Alexa à un
  niveau supérieur
seo_desc: 'By Terren Peterson

  I’m recognized as an Amazon Alexa Champion and have published more than twenty custom
  skills on the platform. I continue to look for new ways to stretch this technology,
  create more robust skills, and share with the community.

  Last...'
---

Par Terren Peterson

Je suis reconnu comme un [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson) d'Amazon et j'ai publié plus de vingt compétences personnalisées sur la plateforme. Je continue de chercher de nouvelles façons d'étendre cette technologie, de créer des compétences plus robustes et de partager avec la communauté.

En [septembre](https://developer.amazon.com/blogs/alexa/post/402fd908-f8d7-4a2b-ab5e-4099222ad974/introducing-alexa-gadgets-new-tools-for-developers-to-create-fun-sign-up-to-stay-tuned), Amazon a lancé un nouveau produit pour Alexa appelé Echo Buttons. Ces dispositifs matériels étendent les capacités pour les millions de clients qui possèdent déjà un Alexa. Ils sont relativement peu coûteux, actuellement vendus à [$20/2 pack](https://www.amazon.com/dp/B072C4KCQH/).

En [avril](https://developer.amazon.com/blogs/alexa/post/705a0ac1-940d-4128-b35e-7085274eca6a/gadgets-skill-api-beta-is-now-available-developers-can-build-games-for-echo-buttons) de cette année, Amazon a ouvert la plateforme aux développeurs comme moi pour commencer à les intégrer dans des compétences personnalisées. Voici mon expérience jusqu'à présent en programmant avec eux.

![Image](https://cdn-media-1.freecodecamp.org/images/CyYLDlEogrNXnrYiXgOAfMnPLr-EHMGF5S87)
_Bouton Echo à l'état inactif._

### Commencer avec les boutons Echo

![Image](https://cdn-media-1.freecodecamp.org/images/rD-kqpmupIZML-HuI46qqn97rNmfe2CmT7fx)
_Connectivité réseau des boutons Echo_

Les boutons sont appariés avec les dispositifs Alexa via une connexion Bluetooth, devenant une extension physique de l'enceinte. Tout le trafic réseau du bouton pour utiliser les services Amazon passe par le dispositif apparié. N'achetez pas de boutons si vous n'avez pas déjà un Alexa, car ils ne font rien seuls.

Si vous avez plusieurs enceintes associées à votre compte, le bouton ne fonctionnera qu'avec le dispositif avec lequel il est actuellement apparié. L'appariement peut être annulé en quelques étapes sur votre téléphone. Pour désappairer un dispositif, utilisez simplement l'application Alexa et allez dans la section des paramètres. Sélectionnez le bouton qui a déjà été apparié, et il le libérera. Puis, refaites les étapes pour le réappairer à un autre dispositif.

![Image](https://cdn-media-1.freecodecamp.org/images/hivuzrSwuf4WcMXDB25tWOKDBXz6qIeQHMiy)
_Capture d'écran de l'application Alexa sur un dispositif mobile_

Cela rend les boutons un ajout facile pour les passionnés d'Alexa, et les rend flexibles pour ceux qui ont plusieurs dispositifs.

### Comment les boutons interagissent avec les compétences personnalisées

Alexa est une architecture pilotée par événements. Les événements sont créés par les sons entrant dans l'enceinte qui sont traduits via un service basé sur le Cloud. Normalement, ces événements sont initiés après que le réseau de microphones capte une commande d'un utilisateur. Ces commandes sont ensuite traduites par les modèles ASR (Reconnaissance Automatique de la Parole) selon la compétence personnalisée utilisée.

Avec les boutons, un nouveau type d'événement est créé qui suit un schéma similaire. Lorsque le bouton est pressé, un événement est créé et envoyé à la compétence qui s'exécute dans le Cloud. Lorsque le bouton est relâché, un événement séparé est créé. Ces événements sont créés indépendamment de tout ce qui est capté par les microphones de l'enceinte Echo et passent par un service basé sur le Cloud appelé Game Engine.

![Image](https://cdn-media-1.freecodecamp.org/images/xn54u0QFvTYWHG-5EBh2IwBAYKiYXRMUVCAY)
_Architecture des événements Alexa incluant les boutons_

La fonction Lambda qui contient la logique de la compétence personnalisée doit traiter ces événements ainsi que ceux déclenchés par la voix existants. La traduction des objets de requête est facilitée par le SDK Alexa installé dans la fonction Lambda. Des exemples de fonctionnement sont fournis dans le [dépôt Alexa](https://github.com/alexa/skill-sample-nodejs-buttons-hellobuttons).

Cela ouvre de nouvelles possibilités pour le gameplay, car un utilisateur peut utiliser à la fois sa voix et ses mains pour interagir avec la compétence. Engager plus de sens élargit l'expérience et permet des jeux plus complexes. Par exemple, dans la compétence [Seventh Inning Stretch](https://www.amazon.com/Seventh-Inning-Stretch-Baseball-Game/dp/B071FF8WCN), un utilisateur peut jouer à un jeu de baseball en écoutant sur son enceinte tout en appuyant sur le bouton pour balancer la batte.

### Comment les compétences utilisent l'API Gadgets

L'utilisation de boutons dans une compétence personnalisée nécessite l'API Gadgets. La documentation est actuellement sur ce [site web](https://developer.amazon.com/docs/gadget-skills/understand-gadgets-skill-api.html), et notez qu'elle est encore en version bêta. Les boutons ne sont qu'un type de gadget et offrent un aperçu de ce qui est possible avec le matériel activé.

La connectivité entre les systèmes est facilitée par des interfaces à travers Internet. L'API dont les boutons ont besoin est invoquée en ajoutant des attributs de directive à un objet de réponse Alexa standard. Cela permet au SDK de gérer les détails explicites de l'appel HTTPS (c'est-à-dire encoder l'en-tête, définir les attributs, gérer les erreurs, etc.)

Voici un exemple d'ajout d'une directive pour régler les lumières d'un bouton en même temps que l'enceinte Echo lit une introduction à l'utilisateur.

```
"response": {               "shouldEndSession": false,               "outputSpeech": {                     "type": "SSML",                     "ssml": "<speak> Bienvenue à nouveau dans Seventh Inning Stretch.<break time=\"1s\"/>Nous avons trouvé un jeu précédent en cours. Souhaitez-vous le reprendre ? </speak>"                 },               "reprompt": {                     "outputSpeech": {                           "type": "SSML",                           "ssml": "<speak> Dites oui pour reprendre le jeu en cours, ou non pour le supprimer.  </speak>"                     }               },               "directives": [    {                           "type": "GadgetController.SetLight",                            "version": 1,                           "targetGadgets": [],                           "parameters": {                      "animations": [               {                         "repeat": 1,                            "targetLights": ["1"],              "sequence": [                          {                    "durationMs": 30000,                                                               "color": "FFFF00",                  "blend": false                                                     }              ]                      }           ],      "triggerEvent": "buttonDown",                                "triggerEventTimeMs": 0    }}
```

Le Game Engine crée des événements tout comme l'enceinte Echo. La même taxonomie est utilisée, et les attributs dans la requête identifient les détails de l'événement. Voici un exemple de requête indiquant qu'un bouton a été pressé.

```
"request": {   "type": "GameEngine.InputHandlerEvent",   "requestId": "amzn1.echo-api.request.xxx",   "timestamp": "2018-07-21T21:33:25Z",   "locale": "en-US",   "originatingRequestId": "amzn1.echo-api.request.xxx",   "events": [     {       "name": "button_down_event",       "inputEvents": [ {         "gadgetId": "amzn1.ask.gadget.xxxx",         "timestamp": "2018-07-21T21:33:25.374Z",         "color": "000DD6",         "feature": "press",         "action": "down"       } ]     }   ] }
```

### Économiser la batterie grâce à l'appel nominal

Les boutons Echo fonctionnent sur batterie, ce qui rend la gestion de l'énergie importante. Lorsqu'une compétence personnalisée nécessite un bouton, elle doit initier une connexion et réveiller le bouton. Cela se fait via un processus appelé "appel nominal" dans la compétence personnalisée.

Pour initier un appel nominal dans une compétence personnalisée, ajoutez une directive à l'objet de réponse fournissant les paramètres pour effectuer la tâche. En parallèle, des instructions audio doivent être incluses dans l'objet de réponse. Celles-ci encourageront un utilisateur à faire quelque chose avec les boutons. Par exemple, demandez à l'utilisateur d'appuyer sur chaque bouton pour commencer.

Pour les détails sur ce à quoi ressemble une directive, voici la directive d'appel nominal que j'utilise pour ma compétence Seventh Inning Stretch. Il s'agit d'une série d'attributs dans un grand objet JSON. Cela définit le paramètre de délai d'attente pour que les boutons puissent retourner en veille s'ils ne sont pas utilisés (la valeur 300 000 est en millisecondes — cela se traduit par cinq minutes), et recherche uniquement l'événement de pression du bouton.

```
"directives": [  {     "type": "GameEngine.StartInputHandler",     "timeout": 300000,     "recognizers": {       "button_down_recognizer": {         "type": "match",         "fuzzy": false,         "anchor": "end",         "pattern": [{ "action": "down" }]       }    },     "events": {       "button_down_event": {         "meets": ["button_down_recognizer"],         "reports": "matches",         "shouldEndInputHandler": false       },       "timeout": {         "meets": ["timed out"],         "reports": "history",         "shouldEndInputHandler": true       }     }  }]
```

Les boutons gèrent le minuteur pour savoir quand s'éteindre. Cela minimise le risque de décharge de la batterie lorsque l'utilisateur termine sa session. Les compétences qui utilisent des boutons doivent également faire une demande pour éteindre le dispositif si la compétence est quittée.

### Traduction des événements du Game Engine

Le Game Engine peut créer des événements tout comme l'enceinte une fois qu'il est réveillé. La requête utilise la même taxonomie, et les attributs identifient les détails de l'événement. Voici un exemple de requête indiquant qu'un bouton a été pressé.

```
"request": {   "type": "GameEngine.InputHandlerEvent",   "requestId": "amzn1.echo-api.request.xxx",   "timestamp": "2018-07-21T21:33:25Z",   "locale": "en-US",   "originatingRequestId": "amzn1.echo-api.request.xxx",   "events": [     {       "name": "button_down_event",       "inputEvents": [ {         "gadgetId": "amzn1.ask.gadget.xxxx",         "timestamp": "2018-07-21T21:33:25.374Z",         "color": "000DD6",         "feature": "press",         "action": "down"       } ]     }   ] }
```

La logique dans la fonction Lambda pour la compétence doit répondre à ces événements et traiter la fonctionnalité en conséquence.

### Les boutons peuvent changer de couleur

À l'intérieur des boutons se trouve une série de LED qui peuvent être allumées et éteintes. Elles sont brillantes et la couleur est très riche.

![Image](https://cdn-media-1.freecodecamp.org/images/9gmdYm6OjjrrCzjeM0DLTLJ-RDtTdnB3gfKd)

Les boutons peuvent également changer de couleur en modifiant la façon dont les différentes LED sont illuminées.

![Image](https://cdn-media-1.freecodecamp.org/images/fr7rACZlz0hBY5apboKduTEjVd7cK8tlXGDz)

Le changement de couleur des boutons se fait également via des directives dans un objet de réponse. Si vous commencez votre compétence en utilisant le [dépôt pour les boutons](https://github.com/alexa/skill-sample-nodejs-buttons-hellobuttons), il y a des fonctions d'aide qui rendent cela facile à intégrer dans votre compétence.

### Conclusion

Si vous êtes intéressé à essayer un jeu qui les utilise, veuillez tester mon jeu de simulation de baseball sur Alexa. Il s'appelle "Seventh Inning Stretch" et est une tentative de recréer le plaisir des anciens jeux portables des années 80. C'est un bon exemple de ce qui est possible en utilisant ces nouveaux accessoires.

![Image](https://cdn-media-1.freecodecamp.org/images/ACXMJEoX78nZezIBRNITH7S5eSIsL0Jka5z6)
_Exemple de compétence Alexa qui utilise des boutons_