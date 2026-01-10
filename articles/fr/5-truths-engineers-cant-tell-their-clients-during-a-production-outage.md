---
title: 5 Vérités que les ingénieurs ne peuvent pas dire à leurs clients pendant une
  panne de production
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2020-10-06T05:01:00.000Z'
originalURL: https://freecodecamp.org/news/5-truths-engineers-cant-tell-their-clients-during-a-production-outage
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9850740569d1a4ca1957.jpg
tags:
- name: Devops
  slug: devops
- name: Freelancing
  slug: freelancing
- name: software development
  slug: software-development
seo_title: 5 Vérités que les ingénieurs ne peuvent pas dire à leurs clients pendant
  une panne de production
seo_desc: "My birthday present this year was a production outage. \nSome people go\
  \ for cake and ice cream. Others plan a fun outing. I got an outage instead of an\
  \ outing. And it was anything but fun.\nIn the midst of it, my colleague and I vacillated\
  \ between tria..."
---

Mon cadeau d'anniversaire cette année a été une panne de production. 

Certaines personnes optent pour un gâteau et de la crème glacée. D'autres planifient une sortie amusante. J'ai eu une panne au lieu d'une sortie. Et ce n'était pas du tout amusant.

Au milieu de tout cela, mon collègue et moi avons oscillé entre le triage du problème et la frustration de ne pas pouvoir trouver sa source. 

Et alors que je reprenais mon souffle pour me connecter avec ma femme patiente et perspicace, je lui ai partagé mon sentiment d'inadéquation et je l'ai consultée sur la manière de communiquer efficacement avec le client affecté.

Ils devaient savoir que nous allions le réparer. Ils avaient besoin que cette réparation soit rapide. Ils devaient savoir que la réparation durerait. 

Nous avons soigneusement rédigé des e-mails et eu des appels téléphoniques rassurants avec eux. Nous les avons tenus informés et leur avons donné la bonne quantité de transparence et d'informations techniques.

Mais voici les vérités que nous ne pouvions pas leur dire.

## 1. Nous n'étions pas préparés à cela

Comme c'est souvent le cas pour de nombreux ingénieurs sur de nombreux projets, nous avons hérité de cette application. Nous avons été laissés avec peu de documentation et de mauvais outils pour déboguer la production. Et il y a trop de parties mobiles à compter. 

C'est comme si nous prenions un extincteur dans un incendie de forêt.

Notre temps et votre budget financier ne permettaient pas de préparations extensives pour une panne de production, et maintenant nous affrontons la chaleur. À plus d'un titre, nous n'étions pas préparés à cela.

## 2. La cause de la panne pourrait être l'une de 20 choses

La cause ? Cela pourrait être le serveur. Cela pourrait être le code. Cela pourrait être la base de données ou un package tiers. Cela pourrait être une intoxication alimentaire. Cela pourrait être de notre faute. Cela pourrait être de la vôtre.

La solution ? Cela pourrait simplement nécessiter un redémarrage. Cela pourrait nécessiter un index sur cette table de base de données. Cela pourrait nécessiter une mise à jour de ce package ou de ce paramètre de configuration. Cela pourrait nécessiter du Pepto-Bismol. Cela pourrait nécessiter de tout brûler et de recommencer.

## 3. Nous n'avons absolument aucune idée du temps que cela va prendre pour le réparer

Un redémarrage du serveur pourrait prendre dix minutes. Une reconstruction du serveur pourrait prendre de dix heures à dix jours. Nous pourrions être en mesure de traquer le bug en quelques minutes, ou nous pourrions ne jamais découvrir ce qui s'est réellement passé. 

Tout dépend de l'identification de la cause, et nous avons déjà établi que cela pourrait être l'une de 20 (ou plus) choses.

Nous avons également établi que nous n'étions pas préparés à cela. Autant nous laisser seuls et faire confiance à notre volonté de résoudre le problème le plus rapidement possible. 

En attendant, nous vous suggérons de reconsidérer votre définition de "rapide".

## 4. Nous avons besoin que le problème se manifeste à nouveau avant de pouvoir en déterminer la cause

Parce que nous avons si peu d'outils et de documentation, nous volons essentiellement à l'aveugle. Heureusement, nous avons installé quelques outils de surveillance pour nous aider. 

Le problème est que ces outils ne peuvent surveiller que les choses à venir. Nous avons donc besoin que ce problème intermittent se manifeste à nouveau avant de pouvoir diagnostiquer le problème.

Nous pourrions certainement essayer cela dans un environnement de staging ou de test, et nous l'avons fait, mais il ne succombe pas aux mêmes problèmes que la production. Et, en fait, c'est une configuration entièrement différente de celle de la production. 

Notre seule option à ce stade est de faire tomber la production à nouveau. Dites à votre équipe de se tenir prête pendant que nous frappons la production, non pas pour essayer de la réparer, mais simplement pour reproduire le problème afin que nos outils puissent capturer ce qui se passe.

## 5. Vous devriez vraiment nous payer plus pour ce niveau de stress

Nous ne dormons pas. Nous mangeons à peine. Nos familles ne nous ont pas vus depuis des jours. Nous passons tout notre temps devant un ordinateur, sauf pour de courtes pauses devant le réfrigérateur, dans la salle de bain ou dans un coin en position fœtale.

Ces niveaux de stress méritent un double salaire, au moins. Mais nous réalisons que ce n'est pas le moment de négocier un nouveau contrat. Nous sommes tous en mode survie, et apparemment, la santé de la production est plus importante que la nôtre. 

Et c'est la raison pour laquelle vous devriez nous payer (beaucoup) plus pendant une panne d'urgence.

## Réflexions finales

Ce sont des vérités que les ingénieurs ne peuvent vraiment pas communiquer à leurs clients pendant la crise d'une panne de production. 

Si vous avez pensé à certaines de ces choses, sachez que beaucoup d'entre nous y ont pensé. Si vous vous reconnaissez dans ces sentiments, beaucoup d'entre nous ont ressenti cela. Les pannes de production causent des quantités immenses de pression et de stress. 

Si vous vous demandez quelles étaient les circonstances réelles de ma panne d'anniversaire, le problème était une réponse intermittente et inattendue d'un service de messagerie tiers. Cela a causé une erreur d'application, mais cette erreur n'a pas été interceptée. 

Au lieu de cela, la demande a été réessayée. Et encore. Et encore quelques centaines (mille ?) de fois jusqu'à ce qu'elle mette le serveur à genoux. Nous redémarrions le serveur et une heure plus tard, il était à nouveau en panne.

Il a fallu des jours pour identifier la cause réelle, car nos outils de surveillance et de débogage n'étaient pas affûtés. Nous avons vu des pics d'utilisation du CPU et de la RAM, mais aucun lien clair avec des processus voyous. Nous ne pouvions pas reproduire le problème dans un autre environnement que la production. Et le code fautif était abstrait et utilisait des bibliothèques avec lesquelles nous n'étions pas familiers.

La prochaine fois, nous serons mieux préparés. Nous avons installé des outils pour nous donner des capacités de profilage et de traçage de pile pour les requêtes en production. Nous allons être plus prudents dans la mise en œuvre d'outils tiers et nous assurer que notre application peut gérer leur échec de manière élégante. 

Personnellement, je prévois de négocier un taux plus élevé (probablement 1,5 ou 2 fois mon taux normal) pour les pannes qui me font abandonner toutes mes autres responsabilités.

Notre préparation devrait également inclure un engagement à rester calme et à faire taire le doute. Paniquer nous fait courir après les symptômes au lieu de nous concentrer sur la source. Le doute essaie de nous convaincre que nous ne pouvons pas résoudre le problème et que nous ne pourrons jamais le faire. 

Opérer à partir d'un lieu de calme et de confiance apportera cette assurance nécessaire à nos clients et nous aidera à naviguer efficacement dans les pannes de production. Et à avoir plus de plaisir lors de nos anniversaires.