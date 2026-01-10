---
title: Comment le serverless permet de passer d'une idée à 100K utilisateurs mensuels
  — à coût zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-31T23:34:09.000Z'
originalURL: https://freecodecamp.org/news/how-serverless-scales-an-idea-to-100k-monthly-users-at-zero-cost-160b41557b94
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7I28RRWH2pQEZsb2ETArAQ.png
tags:
- name: Alexa
  slug: alexa
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: Comment le serverless permet de passer d'une idée à 100K utilisateurs mensuels
  — à coût zéro
seo_desc: 'Eliminate friction to move closer to the customer experience — and closer
  to the functional value of technology


  Developing an Amazon Alexa skill within an AWS Lambda function is a simple way to
  demonstrate the power of ‘serverless’.

  Within an hour, ...'
---

#### Éliminer les frictions pour se rapprocher de l'expérience client — et de la valeur fonctionnelle de la technologie

![Image](https://cdn-media-1.freecodecamp.org/images/1*7I28RRWH2pQEZsb2ETArAQ.png)

Développer une compétence Amazon Alexa dans une fonction AWS Lambda est un moyen simple de démontrer la puissance du 'serverless'.

En une heure, vous pouvez concevoir, développer et déployer une compétence Alexa sur le marché Amazon.com — avec un accès instantané à des millions de consommateurs.

Au cours des dernières années, j'ai développé plusieurs compétences Alexa simples pour expérimenter avec AWS Lambda et explorer l'Alexa Skills Kit. En cours de route, certaines de ces compétences ont même généré suffisamment de clients pour qualifier un paiement mensuel du programme d'incitation d'Amazon.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lAMDxr20puXolqT-x7uKKA.png)

La majorité du travail consiste à coder une fonction AWS Lambda qui exprime la logique métier — en utilisant votre choix de langages populaires tels que Node.js ou Python. Pour commencer, l'équipe Amazon Alexa facilite grandement les choses avec une variété de [modèles d'exemple dans leurs dépôts GitHub](https://github.com/alexa/).

Avec une grande partie de l'infrastructure non différenciée prise en charge par AWS, vous pouvez vous concentrer sur le produit réel, le marketing et l'acquisition de clients. Pour une compétence Alexa, vos résultats sont facilement mesurés par le volume de clients uniques et leur nombre d'interactions.

#### Métriques Amazon Alexa

Au cours du mois de décembre, plusieurs de mes compétences Alexa personnalisées — qui sont toutes basées sur des fonctions AWS Lambda s'exécutant dans un seul compte — ont collectivement atteint plus de 100K utilisateurs en seulement 30 jours.

Ci-dessous se trouvent les métriques sur 30 jours pour quelques-unes de ces compétences, y compris Merry Christmas et Santa Claus — et le favori culte de l'informatique en nuage [Simon Says](https://www.amazon.com/Drew-Firment-Simon-Says/dp/B01NBLMM84/). Les données pour chaque compétence sont accessibles directement dans la console de développement Alexa.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8PwGrCFkupdy16pnCk3gvA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*1RPqAecU0Vwjjw3i6Y1nfw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AI7OW96ytXYSIp8ZsateLw.png)

#### Métriques AWS Lambda

Alors, comment un grand volume de clients, de sessions et d'interactions se traduit-il par l'utilisation sous-jacente des fonctions AWS Lambda ?

Sur la même période de 30 jours, les compétences Alexa ont invoqué les fonctions AWS Lambda associées plus de 1M de fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P4ymhlrZtYk8TIXbZCdJDw.png)

Toutes les fonctions Lambda partagent le même compte AWS — et chaque fonction est allouée avec 512 Mo de mémoire et configurée avec un délai d'attente de 7 secondes. Si nécessaire, AWS fournit de nombreux [leviers pour préparer votre compétence Alexa à l'échelle](https://developer.amazon.com/blogs/alexa/post/546ab5a1-1d1a-49c2-85a5-92ada3e6e907/best-practices-for-scaling-your-alexa-skill-using-amazon-web-services).

Pendant la période de 30 jours, aucune fonction n'a été limitée en raison de taux d'invocation dépassant les limites de concurrency. La durée moyenne d'invocation des fonctions était de 25 millisecondes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oSup3lk2BY94n1w6n3n57A.png)

#### Le coût du serverless

Combien coûte l'hébergement d'une douzaine de compétences Alexa qui se connectent à plus de 100K utilisateurs uniques en 30 jours avec 1M d'invocations de fonctions ? _Zéro. Rien. Nada._

AWS offre aux développeurs l'accès à 1M de requêtes et 400 000 GB-secondes de temps de calcul par mois — sans frais. Avec la taille de mémoire de mes fonctions définie à 512 Mo, cela équivaut à 800K secondes de niveau gratuit par mois.

Voici la facture de décembre pour mon compte AWS personnel :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kP2SyUQtX6msXgdpC2aNdA.png)

Le seul coût encouru pendant la même période était un montant impressionnant de 0,02 $ — le coût élevé de [l'expérimentation avec le nouveau service AWS Kinesis Video Streams](https://twitter.com/drewfirment/status/939567539734175744).

Alors, que se passe-t-il si vos compétences Alexa deviennent virales et dépassent 1M de requêtes pour le service AWS Lambda ? Pour chaque 1M de requêtes supplémentaires, vous recevrez une facture de 0,20 $ — facilement absorbée par les [100 $ de crédits promotionnels](https://developer.amazon.com/alexa-skills-kit/alexa-aws-credits) fournis aux développeurs Alexa.

L'économie de la technologie serverless s'applique également aux compétences Alexa les plus utilisées. Par exemple — même avec plus de 50 millions de requêtes Lambda servant 175K utilisateurs _par jour_, les applications de [sleep sound](http://invokedapps.com/) développées par [Nick Schwab](https://twitter.com/nickschwab) génèrent une facture mensuelle frugale de moins de 30 $.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_FGyTGcHzhH8t8jlcUlJgg.png)

#### La valeur de l'innovation sans friction

Les ingénieurs logiciels des startups et entreprises leaders déploient des architectures serverless pour convertir des idées de produits innovants en valeur consommable — avec un minimum de friction et un coût négligeable.

Les technologies serverless comme les fonctions AWS Lambda sont des facilitateurs clés de l'innovation sans friction — vous permettant de déployer et de mettre à l'échelle plus facilement des produits et services entre les mains d'une base de clients mondiale.

Malgré les avantages commerciaux évidents, il semble encore y avoir beaucoup de débats et de peur concernant la valeur de l'adoption de la technologie serverless. Ne croyez pas le FUD — peur, incertitude et doute.

%[https://twitter.com/drewfirment/status/791913696918286336]

Alors que l'abstraction des services de plateforme mûrit avec le serverless, l'élimination des couches utilitaires peut vous rapprocher de l'expérience client — et de la valeur fonctionnelle de la technologie.

_Drew est un AWS Community Hero, Alexa Champion, et créateur de blagues de papa._
_Suivez-le sur Twitter [@drewfirment](https://twitter.com/drewfirment). [#WePowerTech](https://info.acloud.guru/we-power-tech)_