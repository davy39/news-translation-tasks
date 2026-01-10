---
title: Comment lancer un site sur AWS gratuitement en 15 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T19:39:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-launch-a-site-on-aws-for-free-in-15-minutes-7b3ce5d8d053
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FELQr_PxJW0CzDjdum9ysw.jpeg
tags:
- name: AWS
  slug: aws
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment lancer un site sur AWS gratuitement en 15 minutes
seo_desc: 'By Daniel Simmons

  If you‘re completely new to Amazon Web Services (AWS), it can come across as soul-crushingly
  complicated.

  Not only does it seem like there’s a thousand different services to choose from,
  each of which has an equally cryptic name (li...'
---

Par Daniel Simmons

Si vous êtes complètement nouveau sur Amazon Web Services (AWS), cela peut sembler incroyablement compliqué.

Non seulement il semble y avoir mille services différents parmi lesquels choisir, chacun ayant un nom tout aussi cryptique (comme S3, Lambda, EC2 ou Athena), mais il y a aussi **tellement** de choses à configurer.

Vous devez décider de la quantité de mémoire à allouer à vos fonctions, de la région géographique du monde depuis laquelle vous souhaitez que votre code soit servi, et vous devez construire un objet JSON étrange afin d'accorder des permissions ? Il est TRÈS facile de tremper un orteil et de décider que c'est trop compliqué pour commencer.

Si cela décrit votre expérience jusqu'à présent, alors tant mieux — cet article est pour vous.

J'étais dans le même bateau pendant plus longtemps que je ne voudrais l'admettre.

Mais malgré toute sa complexité intimidante, il y a quelque chose chez AWS qui ne cesse de vous appeler.

Il y a la vitesse, la fiabilité, même le prestige professionnel de pouvoir dire que vous avez de l'expérience avec AWS.

Mais, comme pour tout, si vous voulez commencer, vous devez faire le premier pas. Mon objectif dans cet article est donc de rendre cela facile. Je veux vous amener au point où vous pourrez dire « J'ai déployé un projet sur AWS. »

Ce sera beaucoup plus facile que vous ne le pensez, et cela vous donnera un point de départ pour commencer à explorer les autres services d'AWS.

### Étape 0 : Ce dont vous aurez besoin pour suivre

La liste est courte, mais j'ai pensé la mettre en avant pour m'assurer que cela soit clair dès le début.

1. Une carte de crédit/débit valide (ne vous inquiétez pas, c'est gratuit comme le dit le titre. Mais vous devrez entrer les informations de votre carte de crédit afin de créer un compte AWS)
2. Du code front-end que vous pouvez télécharger et héberger sur AWS. Cela peut être aussi simple qu'un document HTML avec `<p>Hello World</p>` dans le corps.

### Étape 1 : Créer un compte AWS

![Image](https://cdn-media-1.freecodecamp.org/images/gHC1FuOPm-6n5bay5U83J-9jqyDXTuzvf5ud)

Pour être honnête, je me suis arrêté à ce stade plusieurs fois simplement parce que c'était l'une de ces situations « essai gratuit mais ils demandent vos informations de carte de crédit », ce que je tends à résister par principe.

Mais le niveau gratuit de 12 mois est assez incroyable. Une année complète est un long moment pour pouvoir expérimenter sur AWS avant de décider s'il vaut la peine de continuer à l'utiliser. (Je ne suis en aucun cas affilié à AWS, pour le record).

Alors suivez ce lien et créez votre compte : [AWS Free Tier](https://aws.amazon.com/free/).

Je sais que certaines personnes pourraient avoir des préoccupations concernant les limitations du plan gratuit. Par exemple, il y a une limite mensuelle sur les requêtes GET et PUT (20 000 et 2 000 respectivement), après quoi vous commencez à être facturé.

Mais tant que vous n'utilisez cela que pour expérimenter et apprendre pour l'instant, il y a pratiquement aucune chance de dépasser les limitations.

Et même si vous le faites, les prix pour dépasser les limites sont généralement de fractions de centime par 1 000 requêtes.

### Étape 2 : Créer un bucket S3 pour votre projet/site

Pour garder les choses aussi simples que possible, le seul service AWS que nous utiliserons pour ce projet sera Simple Storage Service (ou S3), l'un des services de stockage cloud d'Amazon.

S3 se comporte un peu comme Google Drive ou Dropbox. Mais il peut également être configuré pour servir des fichiers plutôt que de simplement les stocker, ce que nous ferons.

Puisque nous servirons simplement des fichiers hébergés sur S3, ce sera un site statique, sans backend ni connexions à une base de données.

Maintenant que vous avez un compte AWS, connectez-vous à la Console de Gestion ([lien ici](https://console.aws.amazon.com/)) et cliquez sur « Services » dans le coin supérieur gauche du menu principal.

Vous verrez cette liste incroyablement longue d'options de services dont j'ai parlé au début. Ne vous inquiétez pas de tout cela, cliquez simplement sur « S3 » sous la section « Stockage ».

![Image](https://cdn-media-1.freecodecamp.org/images/IzizsR-GLeggIOxlGwlHn05wWUAim3P-onyx)

Cela vous amènera à la page S3, où vous pouvez créer différents « buckets » pour stocker vos différents projets.

Les buckets sont comme des dossiers sur votre bureau. Mais le système de stockage de documents sur S3 ne suit pas la structure de dossier traditionnelle ([plus d'informations si vous êtes intéressé](https://serverfault.com/a/435828)). Donc, au lieu de cela, « bucket » semble être le bon mot à utiliser.

Cliquez sur le gros bouton bleu dans le coin supérieur gauche appelé « Créer un bucket » pour créer un bucket qui contiendra les fichiers de votre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/XkTs-DVcEFaFlTthSTzDpg3TJfZEvW4dh-SL)

![Image](https://cdn-media-1.freecodecamp.org/images/NJ00ZS1dYH4mX3x5iVPbrPOnhEpDJ-VShgJG)
_1) Sélectionnez la région la plus proche de vous 2) Les « tags » sont uniquement utilisés pour le suivi des coûts. Vous n'avez pas vraiment BESOIN de remplir cette partie, mais c'est une bonne pratique_

![Image](https://cdn-media-1.freecodecamp.org/images/B0CIJCSOm2Fi9g39D-iihNjxmuegGbxtuFHk)

![Image](https://cdn-media-1.freecodecamp.org/images/wj0PsdPvkf1LccL6ckom3EN2hplFm3lyU7M-)

La principale chose que vous devez faire ici est de vous assurer que les permissions publiques sont définies sur « Accorder l'accès public en lecture à ce bucket ».

Vous recevrez un avertissement d'AWS, mais ne vous inquiétez pas. Ils veulent simplement s'assurer que personne ne pourrait faire cela par accident. Mais c'est exactement ce que vous voulez faire.

Une fois que vous avez terminé, vous verrez votre bucket dans la liste sur votre console S3.

### Étape 3 : Ajouter des fichiers et configurer les paramètres de votre bucket

Cliquez sur votre bucket nouvellement créé dans la liste. Cela vous amènera à une page où vous pouvez ajouter du contenu à votre bucket et configurer ses paramètres.

Tout d'abord, vous voudrez ajouter vos fichiers de projet (mentionnés au début) dans l'onglet « Vue d'ensemble ». N'oubliez pas que ces fichiers peuvent être ceux de n'importe quel projet front-end fonctionnel.

Vous ne pourrez pas télécharger de dossiers (encore une fois, puisque S3 n'a pas réellement de structure de dossiers). Au lieu de cela, vous devrez créer manuellement les dossiers que vous avez dans votre projet dans S3 et y télécharger vos fichiers.

![Image](https://cdn-media-1.freecodecamp.org/images/x7xUdptNB46x3R4UignuTPv-5qgrFdPPeDWK)

Ensuite, cliquez sur l'onglet « Propriétés ».

C'est ici que vous direz à S3 que vous souhaitez utiliser ce bucket pour héberger vos fichiers.

Il vous suffit de cliquer sur la vignette qui dit « Hébergement de site web statique » et d'entrer les noms de vos documents index (obligatoire) et erreur (non obligatoire) et vous avez terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/teptTJ3QW-hsWlHBdM3VrkJAcT6TilzRlyX1)

![Image](https://cdn-media-1.freecodecamp.org/images/OMdIqlnvbQNtr58S1EZPvU3VgqiWDTdZLael)

Ensuite, cliquez sur l'onglet « Permissions ».

Vous verrez juste en dessous des onglets principaux que vous commencez dans une sous-section appelée « Liste de contrôle d'accès ». Cela est déjà configuré correctement, puisque vous avez déjà dit que n'importe qui devrait pouvoir lire les fichiers hébergés dans ce bucket.

Maintenant, vous devrez cliquer sur la sous-section « Politique de bucket ». Ici, vous serez invité à créer un objet JSON qui contient les détails de la politique de permissions d'accès de votre bucket.

![Image](https://cdn-media-1.freecodecamp.org/images/eaWfZ7lsITqJ3IYfbbA-fyjUtdpQyDmneGCE)

Cette partie peut être déroutante. Pour l'instant, je vais simplement vous donner le JSON qui accordera un accès public complet aux fichiers de votre bucket. Cela rendra le site web accessible au public.

Collez ceci dans l'éditeur de politique de bucket montré ci-dessus :

```
{    "Version": "2012-10-17",    "Statement": [        {            "Sid": "PublicReadForGetBucketObjects",            "Effect": "Allow",            "Principal": "*",            "Action": "s3:GetObject",            "Resource": "arn:aws:s3:::NOM-DU-BUCKET/*"        }    ]}
```

N'oubliez pas de remplacer « NOM-DU-BUCKET » par... le nom de votre bucket.

### Vous avez terminé !

C'est tout ! Vous avez maintenant déployé un site statique très simple sur AWS S3.

Pour accéder à votre site, retournez à l'onglet « Vue d'ensemble » sur S3 et cliquez sur votre document index (cliquez sur une zone vide dans l'élément de la liste, pas sur le lien vers le document lui-même). Vous obtiendrez un menu coulissant sur la droite avec un lien vers votre site !

![Image](https://cdn-media-1.freecodecamp.org/images/ebm54zjdYMuQbAJD1-pqukLfabL2c9wx62SN)

![Image](https://cdn-media-1.freecodecamp.org/images/96pSOx3YuIYj-GDMN8OBJA3Y-lDmsDfS8LVt)