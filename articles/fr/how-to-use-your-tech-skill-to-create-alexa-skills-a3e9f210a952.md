---
title: Comment j'ai programmé ma première compétence Amazon Alexa et gagné un Echo
  Dot gratuit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T23:23:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-your-tech-skill-to-create-alexa-skills-a3e9f210a952
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a0cGkm-EHwR3jcHd7rpkQg.png
tags:
- name: Alexa
  slug: alexa
- name: AWS
  slug: aws
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai programmé ma première compétence Amazon Alexa et gagné un
  Echo Dot gratuit
seo_desc: 'By Lorrie Pearson

  It’s been a year since I began learning to code. I became interested in coding because
  of my desire to work with others in the beauty, fashion and luxury lifestyle world.
  I wanted to create amazing websites with animated elements an...'
---

Par Lorrie Pearson

Cela fait un an que j'ai commencé à apprendre à coder. Je me suis intéressée au codage en raison de mon désir de travailler avec d'autres dans le monde de la beauté, de la mode et du style de vie de luxe. Je voulais créer des sites web incroyables avec des éléments animés et d'autres médias numériques.

J'ai commencé par un cours en ligne et un mois plus tard, j'ai découvert freeCodeCamp. C'est à ce moment-là que l'apprentissage du codage est devenu plus excitant et instructif.

Il y a une communication en temps réel avec d'autres codeurs prêts à vous aider à résoudre des défis interactifs. Ils fournissent des commentaires et des références pour un apprentissage supplémentaire. Cela a aidé ma confiance à grandir et mes compétences en codage à s'améliorer.

Début juin, un ami m'a parlé d'un webinaire en ligne intitulé « Créer des expériences vocales avec Amazon Alexa ». L'idée du webinaire a piqué ma curiosité car à l'époque, je n'avais vu que des publicités, mais je n'avais pas utilisé de produit activé par Alexa. Je me suis inscrite et j'ai été fascinée.

À la fin du webinaire, les participants ont reçu des informations sur une promotion. Si dans les 30 jours vous créiez une compétence et la publiiez, vous étiez éligible pour gagner un Echo Dot gratuit. Je ne savais pas si j'avais assez de connaissances pour réussir, mais j'ai décidé d'essayer pour apprendre.

L'idée de créer ma première application était excitante. À ce moment-là, mon expérience d'apprentissage avec Alexa a commencé.

![Image](https://cdn-media-1.freecodecamp.org/images/GS1YCp8IJi2QrNIMKA71Y2Zj2k-GplgIVH0Y)
_Appareils activés par Amazon Alexa_

### **Qu'est-ce qu'Alexa et comment ça marche ?**

Alexa est un service vocal basé sur le cloud qui alimente des millions d'expériences vocales à la maison. Les appareils alimentés par Alexa incluent Amazon Echo, Echo Dot, Amazon Tap et Amazon Fire TV.

Une compétence est une application vocale pour Alexa.

Alexa fournit des « compétences », qui permettent aux utilisateurs d'interagir avec les appareils. Les compétences peuvent être créées pour faire beaucoup de choses. Elles peuvent répondre à des questions, jouer à des jeux de trivia, jouer de la musique, régler des alarmes, raconter des blagues et plus encore.

Le Alexa Skills Kit (ASK) est une collection d'outils, d'API, de documentation, d'exemples de code et de modèles avec des liens vers GitHub. L'ASK aide les développeurs à créer des compétences pour les appareils activés par Alexa.

Une compétence Alexa a deux composants principaux : un service de compétence et une interface de compétence.

Votre code est écrit en Node.js pour le service de compétence qui réside dans le cloud ([Amazon AWS, Lambda](https://aws.amazon.com/), un service HTTPS). Il reçoit des instructions pour déterminer les actions à prendre en réponse aux demandes de l'utilisateur provenant de l'appareil activé par Alexa.

Le service de compétence implémente des gestionnaires d'événements qui définissent comment la compétence se comportera. L'événement est déclenché lorsque l'utilisateur parle dans un appareil activé par Alexa.

Ensuite, vous configurez l'interface de compétence avec le portail du développeur de compétences. L'interface traite les mots des utilisateurs pour déclencher les événements que le service de compétence gère. Dans cette section, vous déterminez comment appeler votre compétence afin que l'utilisateur puisse l'invoquer par son nom. C'est également là que vous définissez le modèle d'interaction de la compétence. Ainsi, elle sait comment écouter les mots prononcés par les utilisateurs et répondre avec les informations prévues.

C'est l'interaction des deux composants qui fait fonctionner la compétence.

L'équipe Amazon a fourni des liens vers trois modèles de compétences. Ces modèles sont excellents pour vous aider à commencer et à apprendre comment Alexa interagit et répond.

* **Modèle de compétence de fait**
  pour créer quelque chose comme un « fait » ou une « blague » du jour.
* **Modèle d'arbre de décision**
  pour créer des jeux d'aventure simples et des quiz.
* **Modèle Comment faire**
  pour créer des compétences comme du contenu de recettes avec des processus similaires étape par étape.

Et bien d'autres modèles intermédiaires et avancés [disponibles](https://developer.amazon.com/alexa-skills-kit/tutorials).

![Image](https://cdn-media-1.freecodecamp.org/images/lEVAry9so7W9iTBCUgV0-DXV8jTfqNSqPc7i)
_Ma première compétence Alexa publiée, Makeup Facts_

J'ai maintenant trois compétences publiées, [Makeup Facts](https://www.amazon.com/Lorriep-design-studio-makeup-facts/dp/B071XC158S/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1501898705&sr=1-1&keywords=makeup+facts), [Fashion Facts](https://www.amazon.com/Lorriep-design-studio-fashion-facts/dp/B073JY3H83/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1501898748&sr=1-1&keywords=fashion+facts) et [Girls Can Code](https://www.amazon.com/Lorriep-design-studio-Girls-Code/dp/B07487QL3J/ref=sr_1_14?s=digital-skills&ie=UTF8&qid=1501898636&sr=1-14&keywords=lifestyle). Je travaille comme maquilleuse et styliste de mode freelance et j'ai décidé de commencer par ce que je connais le mieux.

Pour créer ces « compétences de fait », j'ai passé en revue le sujet et les informations sur la création d'une compétence. Ensuite, j'ai créé ma liste de faits qui seraient intégrés dans le modèle de compétence de fait. Toutes les compétences ont été acceptées et publiées en quelques jours.

### **Comment j'ai créé ma première compétence**

Allez sur le [Portail des développeurs Amazon](https://developer.amazon.com/), connectez-vous, cliquez sur Alexa en haut de l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/TT4LjkFjJet75UKwzdQ1hQr2cp1vBP4WzOtu)
_Console du développeur Amazon_

Sur la page Alexa, choisissez « Commencer » pour le Alexa Skills Kit.

![Image](https://cdn-media-1.freecodecamp.org/images/ohZJBwb18S7r8sWbEWBbgZH91cgV3JfvvJzN)
_Bouton commencer du Alexa Skills Kit_

Sur la page suivante, sélectionnez « Ajouter une nouvelle compétence ».

![Image](https://cdn-media-1.freecodecamp.org/images/3DFuU4utTQ71Xj11vR7Rt0e834fdmWDyaRO9)
_Du tutoriel Alexa Skills Kit d'Amazon_

Ensuite, remplissez la page **Informations**.

Type de compétence : **Personnalisée**

Langue : **Anglais**

Nom : **Makeup Facts**

Nom d'invocation : (ce que votre utilisateur devra dire pour démarrer la compétence) **Makeup Facts**

![Image](https://cdn-media-1.freecodecamp.org/images/wQGWluVqdyMHNE8XWfhOJHgeukyv8opdfnAE)
_ma page d'informations sur la compétence_

Cliquez sur suivant pour accéder à la page **Modèle d'interaction**. C'est ici que vous créez des **intentions** ou ce que les utilisateurs demanderont à Alexa de faire. Ensuite, créez des **énoncés** ou des façons possibles dont l'utilisateur demandera à Alexa à propos de la compétence que vous avez créée. J'ai trouvé ce [dépôt GitHub](https://github.com/Lorrie01/alexacourse/tree/master/1_spaceGeek/speechAssets) utile. Les exemples incluent : donne-moi un fait, dis-moi un fait.

![Image](https://cdn-media-1.freecodecamp.org/images/YUBk843RK0lgoRBCAm782NwTo0WVkj5OarEW)
_Du cours Alexacourse GitHub_

Mes **intentions** dans le **modèle interactif** pour **Makeup Facts**

```
{ "intents": [ { "intent": "GetNewFactIntent" }, { "intent": "AMAZON.HelpIntent" }, { "intent": "AMAZON.StopIntent" }, { "intent": "AMAZON.CancelIntent" } ] }
```

Mes **énoncés** dans le **modèle interactif** pour **Makeup Facts**.

```
GetNewFactIntent un fait
GetNewFactIntent dis-moi un fait
GetNewFactIntent dis-moi un fait de maquillage
GetNewFactIntent donne-moi un fait
GetNewFactIntent donne-moi un fait de maquillage
GetNewFactIntent dis-moi une anecdote
GetNewFactIntent donne-moi une anecdote
GetNewFactIntent donne-moi quelques informations
GetNewFactIntent dis-moi quelque chose
GetNewFactIntent donne-moi quelque chose
```

Maintenant, il est temps de configurer Lambda. Allez sur [https://aws.amazon.com/](https://aws.amazon.com/) et connectez-vous à la console. Ensuite, allez dans **services-Lambda**.

![Image](https://cdn-media-1.freecodecamp.org/images/crBOkgDgYQiljGUSDxaNIHzVUF2FzRmCoDaY)
_Du tutoriel Alexa Skills Kit d'Amazon_

En haut à droite de votre page, assurez-vous que votre **région AWS** est **N. Virginie**.

![Image](https://cdn-media-1.freecodecamp.org/images/H5yeHkDP00jQLrJBD0VvE7R8kCHkuAcJsNQW)
_Du tutoriel Alexa Skills Kit d'Amazon_

Ensuite, cliquez sur le bouton bleu pour créer une fonction Lambda.

Choisissez le modèle qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/mddxNVvNk2T2m8M26n1VKTimgXoUKKwENBXF)
_Du tutoriel Alexa Skills Kit d'Amazon_

Configurez votre déclencheur. Assurez-vous de choisir **Alexa Skills Kit** dans le menu déroulant.

![Image](https://cdn-media-1.freecodecamp.org/images/ro9RU5ptijwhlJOraZgjYab3ggfdHcqnEViv)
_Du tutoriel Alexa Skills Kit d'Amazon_

Configurez votre fonction. Assurez-vous que le nom de votre fonction est écrit en camelCase. Vous pouvez laisser la description vide, mais vous construisez cela en Node.js.

Ajoutez votre code mis à jour.

Il y a un fichier [AlexaSkill.js](https://github.com/Lorrie01/alexacourse/tree/master/1_spaceGeek/src) écrit avec des gestionnaires d'événements spécifiques. Il spécifie la sortie, l'invite et la parole. Il y a aussi un fichier Index.js que vous personnalisez pour répondre aux besoins de votre compétence.

```
Girls Can Code (index.js)
```

```
'use strict';
var Alexa = require('alexa-sdk');
```

```
var APP_ID = "amzn1.ask.skill.1f2c85a9-b1b6-49a8-b94d-8a795d545d98";
```

```
var SKILL_NAME = "Girls Can Code";
var GET_FACT_MESSAGE = "Voici votre fait : ";
var HELP_MESSAGE = "Vous pouvez dire, dis-moi un fait de code, ou, vous pouvez dire exit… Comment puis-je vous aider ?";
var HELP_REPROMPT = "Comment puis-je vous aider ?";
var STOP_MESSAGE = "Au revoir !";
```

```
var data = [ "Coder, c'est génial.", "Vous pouvez créer des outils qui changeront le monde.", "Coder, c'est créatif.", "Coder, c'est comme résoudre une énigme.", "Le travail de codage peut être fait à distance", "Apprendre à coder, c'est autonomisant.", "La technologie et le codage aident à créer l'avenir.", "Les filles qui savent coder ont un avantage", "N'importe qui peut coder. Vous découvrirez quelque chose de nouveau.", "Le codage favorise la pensée critique", "Les femmes font de grandes codeuses", "Les filles qui codent sont des modèles pour toutes les femmes.", "Les filles qui codent savent que la technologie n'est pas seulement pour les garçons.", "Les emplois dans la tech sont en demande.", "Le codage est la langue du 21e siècle", "Les filles qui codent aident à réduire l'écart entre les sexes.", "Le codage peut être fait n'importe où, n'importe quand", "Travailler dans la tech peut être un choix de carrière très lucratif", "Le codage ne consiste pas seulement à construire des robots et des sites web, vous apprenez à créer des choses qui n'existent pas", "Une fille qui code pourrait créer la prochaine nouvelle application de médias sociaux", "Une fille avec des compétences tech peut changer la façon dont les entreprises communiquent", "Les filles qui codent aiment apprendre."];
```

```
exports.handler = function(event, context, callback) { 
  var alexa = Alexa.handler(event, context);
  alexa.APP_ID = APP_ID;
  alexa.registerHandlers(handlers);
  alexa.execute();
};
```

```
var handlers = { 
  'LaunchRequest': function () { 
    this.emit('GetNewFactIntent'); 
  }, 
  'GetNewFactIntent': function () { 
    var factArr = data; 
    var factIndex = Math.floor(Math.random() * factArr.length); 
    var randomFact = factArr[factIndex]; 
    var speechOutput = GET_FACT_MESSAGE + randomFact; 
    this.emit(':tellWithCard', speechOutput, SKILL_NAME, randomFact) 
  }, 
  'AMAZON.HelpIntent': function () { 
    var speechOutput = HELP_MESSAGE; 
    var reprompt = HELP_REPROMPT; 
    this.emit(':ask', speechOutput, reprompt); 
  }, 
  'AMAZON.CancelIntent': function () { 
    this.emit(':tell', STOP_MESSAGE); 
  }, 
  'AMAZON.StopIntent': function () { 
    this.emit(':tell', STOP_MESSAGE); 
  }
};
```

Créez un fichier compressé avec les deux fichiers ci-dessus et téléchargez le fichier zip dans Lambda.

Passez les paramètres avancés.

Copiez le numéro ARN dans le coin supérieur droit de votre écran.

![Image](https://cdn-media-1.freecodecamp.org/images/kcR-r2rJSGnwpihGWoZOMJS4ygixgZ285t5x)
_Du tutoriel Alexa Skills Kit d'Amazon_

Retournez à la page **Développeur Amazon**. Sélectionnez votre compétence et cliquez sur l'onglet **Configuration** situé dans le menu de la barre latérale gauche.

Sélectionnez l'option **AWS Lambda**. Cochez la case **Amérique du Nord**. Collez le **numéro arn** que vous avez copié depuis votre tableau de bord Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/1E2xx0KBWCGXaRMvLaOYhKqdWncQfYAkGU6u)
_ma page de configuration_

**Testez votre compétence. Si nécessaire, mettez-la à jour pour qu'elle fonctionne correctement.** Ce [dépôt GitHub](https://github.com/Lorrie01/alexacourse/tree/master/1_spaceGeek/src) vous donne le code exemple pour créer une compétence de fait. Vérifiez-le, clonez-le et mettez-le à jour pour écrire le vôtre.

Vous pouvez tester votre code dans la console du développeur, dans les fonctions Lambda, sur votre Echo et sur [Echoism.io](https://echosim.io/welcome).

Entrez vos informations de publication et de confidentialité.

Félicitations… vous êtes prêt à soumettre pour la certification.

Cela prend quelques jours pour avoir des nouvelles de l'équipe des développeurs Amazon. Si votre compétence est approuvée, alors tout fonctionne et toutes les informations sont conformes. Votre compétence sera certifiée et publiée et disponible pour que les autres l'utilisent.

Sinon, vous recevrez des commentaires et des suggestions sur ce que vous devez faire pour résoudre les problèmes afin que vous puissiez la soumettre à nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/0-f8xzlFh9-a56n5XRPSfu6jFzvBCznqYYEU)
_Ma deuxième compétence Alexa publiée, Fashion Facts_

### **Ce que j'ai appris**

* Il est utile d'avoir une certaine familiarité avec JavaScript et Node.js.
* Vous aurez besoin d'un compte AWS (Amazon Web Services) et d'un compte développeur Amazon pour compléter et soumettre des compétences.
* Passez en revue les mots que vous ne pouvez pas utiliser et qui entreront en conflit avec la façon dont Alexa répond.
* Écoutez l'aperçu de votre compétence. Il est extrêmement utile de connaître le flux de vos informations.
* C'est très différent de créer quelque chose qui est activé par la voix d'un utilisateur final par rapport à la lecture sur un écran.
* Faites semblant d'être l'utilisateur final lorsque vous écrivez votre compétence. Cela m'a aidé à comprendre comment l'utilisateur demanderait à Alexa des informations.
* Si votre compétence n'est pas acceptée, passez en revue les commentaires de l'équipe Alexa Skills. Ils fournissent de grandes informations qui vous aideront à préparer votre compétence pour la certification.
* Si vous apportez des améliorations à l'une de vos compétences existantes, la compétence améliorée doit passer par le même processus.
* Vous avez besoin d'une icône ou d'une image pour votre compétence à télécharger avec la soumission.
* Une fois votre compétence acceptée et certifiée, elle est en ligne sur Amazon.

Je travaille actuellement sur deux compétences. L'une utilise le « modèle d'arbre de décision » et l'autre utilise le « modèle Comment faire ». Celles-ci sont un peu plus complexes à construire, mais je suis confiante de les publier bientôt.

J'ai aussi mon Echo Dot gratuit. Interagir avec cet appareil m'a donné des idées pour développer plus de compétences.

![Image](https://cdn-media-1.freecodecamp.org/images/ECUurYe7GuES-qtlriyhtOYaHxZ3so4Lp093)
_Ma troisième compétence Alexa publiée, Girls Can Code_