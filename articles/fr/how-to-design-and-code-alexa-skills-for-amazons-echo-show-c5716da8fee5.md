---
title: Comment concevoir et coder des compétences Alexa pour l'Echo Show d'Amazon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-03T04:46:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-and-code-alexa-skills-for-amazons-echo-show-c5716da8fee5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HXEEbWxI_dUUCM3JoTDUAA.jpeg
tags:
- name: amazon echo
  slug: amazon-echo
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Comment concevoir et coder des compétences Alexa pour l'Echo Show d'Amazon
seo_desc: 'By Terren Peterson

  I’m an Amazon Alexa Developer Champion, and have published more than a dozen skills
  on the Alexa platform. This includes award winning skills like Hurricane Center,
  Scavenger Hunt, and Robot Roxie.

  The latest device added to the Am...'
---

Par Terren Peterson

Je suis un [Amazon Alexa Developer Champion](https://developer.amazon.com/alexa/champions/terren-peterson) et j'ai publié plus d'une douzaine de compétences sur la plateforme Alexa. Cela inclut des compétences primées comme [Hurricane Center](https://read.acloud.guru/amazon-alexa-analytics-2355c359933b), [Scavenger Hunt](https://devpost.com/software/scavenger-hunt-ebvrck) et [Robot Roxie](https://www.hackster.io/contests/alexa-raspberry-pi).

Le dernier appareil ajouté à la famille Amazon Echo dispose d'un écran qui complète son expérience audio. Il s'appelle l'Echo Show, et [voici les spécifications matérielles](https://www.amazon.com/dp/B01J24C0TI#tech). Il dispose d'un écran tactile de 7", d'une caméra de 5 mégapixels et de deux haut-parleurs stéréo de 2 pouces.

Dans cet article, je vais vous montrer comment concevoir et coder une nouvelle compétence Alexa qui tire parti de ce nouveau matériel.

### Mises à jour majeures de la plateforme logicielle

Ces améliorations matérielles ont nécessité une mise à niveau du logiciel sous-jacent qui fait fonctionner la plateforme. Le kit de développement des compétences Alexa (ASK) a introduit une version majeure pour alimenter les nouvelles fonctionnalités de l'écran. Il s'agit du plus grand ensemble d'améliorations apportées à l'ASK depuis le lancement de la plateforme.

#### Contexte sur la création de compétences

Si vous n'êtes pas familier avec le développement d'applications Alexa — appelées « compétences » — voici un bref aperçu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l8Rl3UtrzvTagkgOYJZnEw.png)

* Une application vocale personnalisée interface avec le moteur de traitement du langage naturel. Cela interprète les commandes audio fournies par l'utilisateur. Chaque application inclut un modèle d'intention personnalisé pour diriger les messages de la compétence. Un ensemble d'énoncés d'exemple entraîne les modèles de reconnaissance vocale qui utilisent l'intention dans le modèle.
* Une API unique reçoit tous les messages pour la compétence personnalisée. Alexa nécessite une interface RESTful spécifiée dans l'application vocale personnalisée. L'auteur de la compétence écrit l'API et choisit la plateforme d'hébergement. La plateforme d'hébergement préférée est le service AWS Lambda. Cela est dû à la compatibilité fluide du modèle de sécurité à travers Amazon et aux faibles coûts d'hébergement. L'appel API contient un ensemble standard d'attributs relatifs à l'appel effectué par l'appareil. Cela contient des données sur l'invocation actuelle de la compétence.

Voici un exemple de demande à l'API de la compétence Hurricane Center :

```
{  "session": {    "sessionId": "SessionId.5725be2d-99f8-4afd-909f-1f1d3882067a",    "application": {      "applicationId": "amzn1.echo-sdk-ams.app.709xxx"    },    "attributes": {},    "user": {      "userId": "amzn1.ask.account.AFP3xxx"    },    "new": true  },  "request": {    "type": "LaunchRequest",    "requestId": "EdwRequestId.260fd856-668f-4dd2-af9d-60d80e4cc8e0",    "locale": "en-US",    "timestamp": "2017-07-02T00:54:57Z"  },  "version": "1.0"}
```

L'API pour la compétence personnalisée traite la demande et répond avec des valeurs pour l'appareil Alexa. Le modèle de message retourné est un ensemble standard d'attributs, écrit en JSON. La voix Alexa sur l'appareil lit l'attribut outputSpeech.

Voici un exemple correspondant à l'appel fait à la compétence Hurricane Center ci-dessus :

```
{ "version": "1.0", "sessionAttributes": {} "response": {     "outputSpeech": {         "type": "PlainText",         "text": "Bienvenue au Hurricane Center, la meilleure source d'informations liées aux tempêtes tropicales, passées ou présentes. Il n'y a pas de tempêtes tropicales actives pour le moment, mais si vous souhaitez en savoir plus sur les tempêtes, veuillez dire quelque chose comme, dites-moi un fait sur une tempête."     },     "card": {         "content": "Aucune tempête actuelle dans l'océan Atlantique ou Pacifique.",         "title": "Bienvenue au Hurricane Center",         "type": "Simple"     },     "reprompt": {         "outputSpeech": {             "type": "PlainText",             "text": "Veuillez me dire comment je peux vous aider en disant des phrases comme, lister les noms de tempêtes ou l'historique des tempêtes pour 2013."         }     }, }, "shouldEndSession": false }}
```

### Qu'est-ce qui a changé pour l'Echo Show ?

Pour tirer parti des nouvelles fonctionnalités visuelles du Show, le modèle de réponse a été étendu. Le modèle inclut désormais de nouveaux attributs pour utiliser les nouvelles fonctionnalités matérielles. L'API personnalisée pour la compétence inclut ces attributs dans sa réponse.

Les nouveaux modèles prenant en charge différents cas d'utilisation de l'écran sont centraux. Ces modèles permettent au Show d'augmenter l'expérience vocale. Des détails complets sur ces changements sont disponibles sur le [site web des développeurs Amazon](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/display-interface-reference).

![Image](https://cdn-media-1.freecodecamp.org/images/1*HXEEbWxI_dUUCM3JoTDUAA.jpeg)

#### Six modèles visuels parmi lesquels choisir

Il y a six modèles disponibles avec le lancement initial du nouvel ASK. Chaque modèle offre la possibilité de tirer parti de l'écran tactile sur l'Echo Show. Il existe deux types de modèles. Quatre d'entre eux fournissent une utilisation de base de l'écran, les deux autres modèles ajoutent la possibilité de gérer des listes de données. Le développeur de compétences sélectionne le modèle le plus applicable pour chaque cas d'utilisation.

#### L'Echo Show prend en charge les balises HTML de base

La plateforme Alexa dispose déjà d'une option visuelle avant ces changements. Cela se trouve dans l'application mobile sur votre appareil qui s'apparie avec — nommée l'application compagnon. Cela effectuait la configuration initiale et la configuration en s'appariant avec l'appareil. Certaines compétences l'utilisent pour compléter l'expérience utilisateur d'abord vocale. Voici à quoi cela ressemble pour Hurricane Center.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AZ5Cu5hXnLC3wLgo2K030Q.png)

L'application compagnon a des limites dans la manière dont elle peut rendre les informations. Tous les mots à l'écran sont en texte brut. Elle ne prend pas en charge le HTML, y compris le changement de type de police, de taille de police, de soulignement, etc.

Une petite image facultative s'affiche à l'écran qui change avec chaque réponse vocale. L'utilisabilité de l'application est mauvaise lors du rendu d'une grande quantité de données étant donné la contrainte de texte clair. L'utilisabilité est également mauvaise lors du rendu de listes de données qui peuvent être importantes pour le récit de la compétence.

Dans les modèles du nouvel ASK, le texte simple et la syntaxe HTML de base sont désormais pris en charge. L'associer au modèle de liste offre un tout nouveau niveau d'expérience utilisateur.

#### Nouveaux intents pour gérer les événements tactiles

L'écran de l'Echo Show ne se contente pas d'agir comme un affichage, il dispose également de capteurs tactiles. Interagir avec l'écran crée des événements ainsi que des énoncés audibles. Ceux-ci incluent, bouton retour, droite, gauche, etc. car l'utilisateur peut gesticuler avec du texte et des listes à l'écran.

L'appareil gère la plupart des nouveaux intents standard. Ils peuvent être incorporés dans votre compétence lors du rendu des listes.

### Les compétences existantes fonctionnent sur le nouvel appareil

Les 15 000 compétences existantes sur la plateforme fonctionnent avec l'Echo Show. Elles utiliseront les informations actuellement rendues sur l'application compagnon. Voici un exemple avec la compétence Hurricane Center.

La compétence fonctionne, mais l'utilisabilité de l'écran est mauvaise car la police est trop grande. L'écran montre les mêmes informations que celles partagées avec l'application compagnon. Sans modifications, il n'utilise pas de modèle, donc il n'y a pas de défilement activé au cas où l'utilisateur souhaite lire le texte complet.

Pour référence, voici le dépôt GitHub qui contient l'ensemble du code source de cette compétence.

[**terrenjpeterson/hurricane**](https://github.com/terrenjpeterson/hurricane)  
[_Compétence Alexa pour fournir des mises à jour sur les ouragans_github.com](https://github.com/terrenjpeterson/hurricane)

### Rénovation extrême — Édition Echo Show

Voici les étapes nécessaires pour tirer parti des nouvelles fonctionnalités de l'ASK. Ces changements exploiteront les capacités matérielles pour les utilisateurs avec un Echo Show.

#### Étape 1 — Activer la fonctionnalité de modèle pour la compétence

L'activer pour une compétence nécessite de sélectionner un bouton radio sur une nouvelle compétence ou une compétence existante. Il y a un nouvel indicateur pour « Render Template ». Une fois qu'il est défini, la compétence peut désormais tirer parti des capacités supplémentaires de l'Echo Show.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IocU0ynDy34VsyFyEXZq0Q.png)

#### Étape 2 — Sélectionner un modèle, puis ajouter des attributs à la réponse de l'API

L'ASK contient désormais des modèles décrivant les motifs visuels pris en charge par l'Echo Show. Ceux-ci correspondent à différents motifs d'interface utilisateur, y compris l'affichage d'images et de listes. Il y a une bonne [documentation de référence](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/display-interface-reference) sur le site web des développeurs Amazon.

Pour ma compétence Hurricane Center, j'ai choisi d'utiliser le « BodyTemplate1 » pour l'affichage principal. Cela tire parti de la capacité à afficher une image de fond sur le Show. Il rend également une expérience utilisateur améliorée pour la réponse textuelle. Voici les nouveaux attributs à inclure dans la réponse JSON existante.

```
directives: [ {   type: "Display.RenderTemplate",   template: {       type: "BodyTemplate1",       token: "T123",       backButton: "HIDDEN",       backgroundImage: {           contentDescription: "StormPhoto",           sources: [               {                  url: "https://s3.amazonaws.com/hurricane-data/hurricaneBackground.png"               }           ]      },      title: "Hurricane Center",      textContent: {          primaryText: {              text: cardInfo,              type: "PlainText"          }      }  }}],
```

L'image de fond utilisée correspond aux dimensions de l'Echo Show — 1024 x 600 pixels. L'hébergement des images suit le même modèle que celui de l'application compagnon. L'objet image doit être accessible depuis Internet sans aucune authentification.

#### Étape 3 — Publier une nouvelle version de la compétence

Le rendu des modèles modifie la compétence, nécessitant de passer à nouveau par le processus de certification. Il n'est pas nécessaire de publier une compétence séparée pour le nouvel appareil. Cela signifie que toutes les évaluations précédentes et les utilisateurs qui l'ont activée sur leurs comptes seront conservées. Testez la compétence sur d'autres appareils pour vous assurer que rien n'est cassé.

### Nouvelle version de la compétence

Voici à quoi ressemble la compétence ouragan après le travail décrit ci-dessus.

La photo apparaît désormais comme une image de fond plutôt que comme la toile par défaut. Le texte destiné à l'application compagnon est rendu sur l'écran de l'Echo Show. La taille de la police est appropriée, dans un format lisible. Il s'agit d'une amélioration majeure de l'utilisabilité, avec un effort de codage peu significatif.

### Compatibilité ascendante pour tous les appareils

Nous voulons que la compétence continue de fonctionner pour les appareils existants étant donné que l'Echo Show est nouveau. Cela nécessite une logique supplémentaire lors de la mise en forme de la réponse dans l'API. Le contrat d'interface nécessite que l'API ne fournisse que des attributs lisibles par l'appareil. Cela signifie que les attributs supplémentaires destinés à l'Echo Show créent des erreurs lorsqu'ils sont envoyés à un Echo précédent.

Arrêter cette erreur nécessite d'interpréter la section de contexte de l'objet de demande natif. Cette section fournit des informations sur l'appareil, y compris s'il contient un écran. Cet attribut n'est présent qu'avec un Echo Show. Si cet attribut n'est pas présent, l'API exclut l'attribut directives. Voici un exemple de demande de la compétence Hurricane Center générée par un Echo Show.

```
"context": {     "AudioPlayer": {         "playerActivity": "STOPPED"     },     "Display": {         "token": "T123"     },     "System": {         "application": {             "applicationId": "amzn1.echo-sdk-ams.app.709xxx"         },         "user": { "userId": "amzn1.ask.account.AFP3xxx" },         "device": {             "deviceId": "amzn1.ask.device.AFAQxxx",            "supportedInterfaces": {                 "AudioPlayer": {},                 "Display": {                     "templateVersion": "1.0",                     "markupVersion": "1.0"                 },             "VideoApp": {}         }     },}
```

Dans l'exemple ci-dessus, l'attribut System.device.supportedInterfaces.Display existe, indiquant que la demande est originaire d'un Echo Show. Voici la demande de la même compétence générée par un Echo Dot.

```
"context": {     "AudioPlayer": {        "playerActivity": "IDLE"     },     "System": {         "application": {            "applicationId": "amzn1.echo-sdk-ams.app.709xxx"         },         "user": { "userId": "amzn1.ask.account.AFP3xxx" },         "device": {             "deviceId": "amzn1.ask.device.AFAQxxx",             "supportedInterfaces": {                 "AudioPlayer": {}             }         },         "apiEndpoint": "https://api.amazonalexa.com"     } }
```

Dans le deuxième exemple, il n'y a pas d'attributs d'affichage. C'est facile à reconnaître, et cela est maintenant reflété dans ma compétence.

### Qu'est-ce qui suit ?

C'est incroyable la vitesse à laquelle la plateforme se développe. Il y a maintenant 15 000 compétences personnalisées disponibles pour les utilisateurs à essayer. Les options matérielles permettent des expériences utilisateur encore plus profondes. Je vais passer les prochains mois à porter mes compétences sur la nouvelle plateforme. J'espère que cela aidera à mettre à jour les vôtres !