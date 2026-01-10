---
title: Comment coder des jeux sportifs pour Amazon Alexa, plus quelques jeux amusants
  que j'ai créés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-30T20:34:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-sports-games-for-amazon-alexa-and-some-fun-games-i-built-8179d2142f02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2MZNttNYjigeKtg43OiPZA.jpeg
tags:
- name: Alexa
  slug: alexa
- name: amazon echo
  slug: amazon-echo
- name: sports
  slug: sports
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Comment coder des jeux sportifs pour Amazon Alexa, plus quelques jeux amusants
  que j'ai créés
seo_desc: 'By Terren Peterson

  I’m both a sports nut and a software engineer. I’m also recognized as an Amazon
  Alexa Champion. I continue to look for new ways to stretch this technology.

  Over the past two years, I’ve won hackathons for skills on the Alexa platfo...'
---

Par Terren Peterson

Je suis à la fois un passionné de sport et un ingénieur logiciel. Je suis également reconnu comme un [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson). Je continue de chercher de nouvelles façons d'exploiter cette technologie.

Au cours des deux dernières années, j'ai remporté des [hackathons](https://en.wikipedia.org/wiki/Hackathon) pour des compétences sur la plateforme Alexa.

Les compétences sont la partie du service vocal Alexa qui active ses capacités. Dans Alexa, le terme _compétence_ est utilisé pour désigner des capacités qui rendent une expérience plus personnelle. Vous pouvez les activer ou les désactiver selon vos préférences. Et, avec l'Alexa Skills Kit, vous pouvez créer et personnaliser vos propres compétences.

### Les jeux sportifs sont un marché énorme

Les jeux vidéo sont un marché énorme, avec des revenus annuels projetés à plus de [100 milliards de dollars dans le monde](https://newzoo.com/insights/articles/the-global-games-market-will-reach-108-9-billion-in-2017-with-mobile-taking-42/). Les jeux de tir et d'action sont les plus populaires, [suivis par les jeux sportifs](http://marketrealist.com/2016/06/action-and-sports-genres-dominate-the-video-gaming-space/).

Les plateformes vocales connaissent une croissance fantastique. La plateforme populaire Amazon Alexa a quadruplé au cours de l'année dernière. Il existe désormais 20 000 compétences personnalisées sur la plateforme Alexa. Pourtant, aucun jeu sportif n'est plus complexe que des questions de trivia.

Voici un exemple de mon nouveau jeu de football appelé _End Zone Football_. Cela montre comment un jeu avancé peut fonctionner sur la plateforme Alexa.

### Commencez la conception du jeu avec des Storyboards

La conception de la compétence nécessite l'écriture de [storyboards](https://en.wikipedia.org/wiki/Storyboard) pour scripter l'action. Commencez par la manière dont le jeu va débuter. Ensuite, écrivez le récit pour le [gameplay](https://en.wikipedia.org/wiki/Gameplay) de base.

Considérez-vous comme un dramaturge ou un réalisateur de film. Demandez-vous : Que devrait dire la voix native d'Alexa ? Quels sons peuvent être joués dans le cadre du jeu ?

Voici ce que j'ai appris en publiant un jeu de Baseball et de Football sur Alexa. Ces conseils amélioreront l'utilisabilité de votre jeu :

* Gardez l'interaction simple
les réponses oui ou non et 1/2/3/4 fonctionnent le mieux
* Identifiez les sons qui peuvent rendre le gameplay plus excitant
Acclamations de la foule, sifflets, ou le craquement d'une batte
* Simplifiez le jeu
Les compétences du jeu de Baseball devraient inclure les balles hors limites
Les compétences du jeu de Football devraient simuler les pénalités
Cela aide à garder l'utilisateur engagé
* Ne vous fiez pas aux visuels
Une image de fond pour l'Echo Show est agréable, mais les images sur l'application compagnon devraient être secondaires
* Limitez le jeu à 2–5 minutes
Les utilisateurs peuvent jouer encore et encore s'ils ont le temps
* Créez une fonction d'aide qui explique le jeu en détail
Donnez des exemples de phrases à utiliser pour jouer
* Par-dessus tout
Rendez-le amusant !

### Apprenez le SSML pour inclure des sons avec la voix

Le [Speech Synthesis Markup Language](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/speech-synthesis-markup-language-ssml-reference) (SSML) intègre le son avec la voix. Il est utilisé pour créer l'audio pour l'appareil Alexa.

Voici comment je définis l'attribut de réponse principal pour appeler l'API Alexa. Après avoir épissé les chaînes en JavaScript, le code ressemble à ceci :

```
var speechOutput = "Bienvenue dans End Zone Football. " +   "<audio src=\"" + bucketLoc + "BandMusicIntro.mp3\" />" +  "Le jeu qui vous permet de faire avancer le " +   "ballon sur le terrain en utilisant uniquement votre voix. " +   "<break time=\"1s\" />" +   "Vous êtes en charge des Blackbears, et êtes menés " +  sessionAttributes.away + " à " + sessionAttributes.home + ". " +   "<break time=\"1s\" />" + "Le ballon est sur la " +   yardline + " yardline. " +   "Lorsque vous êtes prêt, appelez simplement la joue que vous voulez exécuter, et le jeu commencera. " +   "Pour une liste de joues à tout moment, dites, Lire le Playbook. ";
```

Voici quelques exemples de l'utilisation du SSML dans ce contexte :

* Pour créer une pause
<break time=1s/>
* Pour insérer un extrait sonore
<audio src="https://s3.amazonaws.../file.mp3">

Je recommande d'utiliser un [S3 bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) pour stocker les fichiers multimédias. C'est un moyen peu coûteux de stocker des données. Et ils peuvent être accessibles à Alexa.

### La gestion d'état suit la progression du jeu

Alexa a la capacité de stocker l'état du gameplay. Utilisez cette fonctionnalité pour simplifier le codage et les tests de votre compétence.

Dans le [Node.js SDK](https://aws.amazon.com/sdk-for-node-js/), un attribut de session est passé avec les attributs de requête et de réponse. Vous pouvez utiliser l'attribut de session pour l'état du gameplay. Stockez les informations critiques du jeu dans ce champ. Vous pouvez inclure n'importe quoi, comme le numéro de jeu ou le nombre enregistré de retraits.

Voici un exemple utilisé dans le jeu de Football

```
// sauvegarder les attributs du jeu pour la prochaine joue    if (session.attributes) {          sessionAttributes = session.attributes;    }...
```

```
// règles de gameplay pour la passeif (offensivePlaybook[i].playType === "pass" &&    offensivePlaybook[i].playNumber.toString() ===     intent.slots.playNumber.value) {       console.log("Numéro de jeu correspondant");       // calculer la distance de passe en fonction de la joue sélectionnée      passDistance = Math.round(Math.random() *         (offensivePlaybook[i].maxYardage            — offensivePlaybook[i].minYardage)            + offensivePlaybook[i].minYardage);       // s'assurer que la distance de la joue ne peut pas être plus longue que       // le terrain restant       if (passDistance > sessionAttributes.yardline) {         passDistance = sessionAttributes.yardline;       }       playDesc = offensivePlaybook[i].playDesc;       speechOutput = speechOutput + playDesc + ". ";       // en fonction de la joue sélectionnée, déterminer le taux de       // réussite relatif       passCompletion = offensivePlaybook[i].completionRate;)...// renvoyer la réponse à Alexa et sauvegarder l'état du jeu
callback(sessionAttributes,                 buildSpeechletResponse(cardTitle, speechOutput,       cardOutput, repromptText, device, shouldEndSession));
```

Stocker ces données dans un tableau pour l'analyse est utile, mais n'est pas nécessaire dans une version initiale. Laissez la plateforme Alexa faire ce travail pour vous.

### Faites la publicité de votre compétence sur les réseaux sociaux

Les gens ne réalisent pas encore tout ce qu'une Alexa peut faire. Lorsque je fais des démonstrations de ces compétences, je reçois systématiquement des commentaires comme "Je ne pensais pas qu'Alexa pouvait faire cela."

Toutes les compétences doivent être certifiées avant leur publication sur l'Amazon Store. Lorsque votre compétence passe le processus de certification, prenez le temps d'enregistrer une vidéo de celle-ci en action. C'est le meilleur moyen de prouver ce dont la plateforme est capable.

Merci d'avoir lu, et profitez bien de ces jeux — ils sont gratuits !