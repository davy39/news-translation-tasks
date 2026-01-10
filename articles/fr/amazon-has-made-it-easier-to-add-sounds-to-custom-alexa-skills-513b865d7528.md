---
title: Amazon a facilité l'ajout de sons aux compétences Alexa personnalisées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T08:06:57.000Z'
originalURL: https://freecodecamp.org/news/amazon-has-made-it-easier-to-add-sounds-to-custom-alexa-skills-513b865d7528
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iXOMQlmW4OqiYidOPVfatw.jpeg
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Amazon a facilité l'ajout de sons aux compétences Alexa personnalisées
seo_desc: 'By Terren Peterson

  I’m recognized as an Amazon Alexa Champion and have published more than twenty custom
  skills on the platform. I continue to look for new ways to stretch this technology,
  and one of the best ways I’ve found to improve the user exper...'
---

Par Terren Peterson

Je suis reconnu comme un [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson) d'Amazon et j'ai publié plus de vingt compétences personnalisées sur la plateforme. Je continue de chercher de nouvelles façons d'exploiter cette technologie, et l'une des meilleures méthodes que j'ai trouvées pour améliorer l'expérience utilisateur est d'ajouter des sons. Grâce à [l'amélioration récente](https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html) de la plateforme Amazon Alexa, cela est devenu encore plus facile. Voici un bref aperçu de la manière dont vous pouvez tirer parti de cette nouvelle fonctionnalité.

### Comment fonctionne Amazon Alexa

La plateforme Alexa permet d'activer des compétences personnalisées créées par des développeurs tiers. Il en existe désormais plus de 30 000 disponibles, et les millions d'utilisateurs d'Alexa peuvent les activer sur leurs appareils. Ces compétences vont de la commande d'une pizza auprès d'une chaîne populaire à la lecture de sons pour aider à dormir.

L'architecture de ces compétences personnalisées comporte deux composants. Le premier est le composant vocal qui utilise les modèles de machine learning de la plateforme Alexa. C'est ce qui traduit les requêtes vocales en un ensemble d'instructions.

L'autre composant est la logique si/sinon qui décide de la réponse à renvoyer à l'utilisateur. Cela est hébergé sur une fonction AWS Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/uktbt4NNJPyLIOzMTI0SWzAgriH5OMiOVhAc)

Pour améliorer les compétences, des services AWS supplémentaires peuvent être utilisés, ainsi que des outils tiers. Cela inclut l'enregistrement de sons MP3 personnalisés et de graphiques qui peuvent être utilisés par la fonction Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/5Iwg4WP1zl0gepFBIRJU70TyWHQeHhksGibI)

Pour ajouter des sons, des fichiers MP3 sont téléchargés dans un bucket S3, et la politique d'accès appropriée est appliquée afin qu'ils puissent être lus par un appareil Alexa.

### Défis liés à l'ajout de sons personnalisés

L'un des obstacles à l'inclusion de sons dans les compétences personnalisées a été la capacité d'enregistrer des sons de haute qualité. Ces sons doivent correspondre aux normes exactes de la plateforme, y compris le débit binaire et les taux d'échantillonnage. Cela peut être fait grâce à une expertise en édition sonore en utilisant des logiciels comme Audacity, mais cela ajoute du temps au développement de la compétence.

L'enregistrement de sons de haute qualité peut également être un défi. Il existe des applications pour appareils mobiles qui permettent l'enregistrement, mais l'accès à une grande variété de sons est difficile. Par exemple, enregistrer le rugissement d'un avion ou le son qu'un éléphant fait.

Alternativement, un développeur Alexa peut rechercher des sons qui ont été enregistrés par d'autres. Il existe quelques dépôts sur Internet qui en contiennent, mais la plupart coûtent de l'argent pour être licenciés et nécessitent un rééchantillonnage avec des logiciels comme Audacity pour obtenir les bons attributs sonores.

### Contenu MP3 gratuit

Amazon a maintenant publié un catalogue de centaines de sons déjà enregistrés selon les normes exactes requises par la plateforme. Tout comme dans le diagramme d'architecture ci-dessus, ils sont publiés dans un bucket S3 sur AWS et peuvent être utilisés par n'importe quelle compétence personnalisée.

La liste complète est fournie sur la [page développeur](https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html), et voici les principales catégories.

![Image](https://cdn-media-1.freecodecamp.org/images/3fgPZrn6W9hhJIGCrXOYgH6bTs2pYm82ZH8e)

La gamme est vaste. Des moteurs de moto, des bruits de feux d'artifice et le rugissement d'un ours sont tous à portée de main. Aucune redevance n'est requise pour utiliser ceux-ci, et le coût de téléchargement des extraits sonores n'est pas facturé à votre compte AWS.

### Comment utiliser le son dans une compétence de base

Si vous débutez avec Amazon Alexa, commencez par les modèles de base de la [page GitHub d'Alexa](https://github.com/alexa). Cela inclut la création d'une compétence de trivia, d'une compétence de faits ou de simples jeux de devinettes. Par exemple, j'ai récemment publié une compétence amusante pour enfants appelée Easter Egg Hunt. [Voici le dépôt complet](https://github.com/terrenjpeterson/eastereggskill) sur GitHub, incluant à la fois la fonction Lambda et le modèle d'intention.

Avec n'importe quelle réponse de message, vous pouvez ajouter la syntaxe SSML pour inclure le lien vers le fichier MP3 dans le bucket S3. Voici un exemple du Welcome Handler pour la compétence Easter Egg.

```js
// Ceci est le message de bienvenue initial
var welcomeMessage = "<audio src='https://s3.amazonaws.com/ask-soundlibrary/musical/amzn_sfx_trumpet_bugle_03.mp3'/>Bienvenue dans le jeu de cache-cache de l'œuf de Pâques du lapin de Pâques. Je vais vous poser plusieurs questions auxquelles vous devez répondre par oui ou non. En fonction de vos choix, je vais faire une recommandation sur l'endroit où cacher un œuf. Êtes-vous prêt à commencer ?";

this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
```

Lorsque l'utilisateur invoque cette compétence personnalisée pour la première fois, l'appareil Alexa lit l'extrait sonore pour la trompette, puis lit la syntaxe avec la voix standard.

### Prêt à commencer ?

Allez-y et inscrivez-vous pour un [compte développeur gratuit](https://developer.amazon.com) sur Amazon, et commencez à construire votre première compétence dès aujourd'hui ! Le blog des développeurs Amazon propose quelques excellentes ressources à exploiter sur ce sujet, y compris ce [récent article](https://developer.amazon.com/blogs/alexa/post/c202ca98-ed68-440b-adb3-73ae9d8f36da/how-to-enhance-your-alexa-skill-with-audio-clips-from-the-ask-sound-library) donnant des idées sur la façon d'utiliser ce nouveau contenu.