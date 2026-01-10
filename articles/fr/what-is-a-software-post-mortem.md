---
title: Qu'est-ce qu'un post-mortem logiciel et comment en rédiger un ?
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2020-12-09T01:52:05.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-software-post-mortem
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/untitled--3-.png
tags:
- name: debugging
  slug: debugging
- name: software development
  slug: software-development
seo_title: Qu'est-ce qu'un post-mortem logiciel et comment en rédiger un ?
seo_desc: 'Every company has their own name for the highest priority bugs. Priority
  one, emergencies, critical fixes or urgent fixes.

  There are software bugs that can end up crippling companies if they aren''t dealt
  with rapidly.

  The Knight Capitol Group was an ...'
---

Chaque entreprise a son propre nom pour les bugs de la plus haute priorité. Priorité un, urgences, corrections critiques ou corrections urgentes.

Il existe des bugs logiciels qui peuvent finir par paralyser les entreprises s'ils ne sont pas traités rapidement.

[The Knight Capitol Group](https://en.wikipedia.org/wiki/Knight_Capital_Group#2012_stock_trading_disruption) était une société américaine de services financiers. Un technicien a oublié de copier un nouveau code sur un serveur informatique, et cette mise à jour logicielle leur a coûté 440 millions de dollars. Cela s'est produit parce que l'un des serveurs informatiques a commencé à acheter rapidement des actions (il a effectué plus de 4 millions d'achats et de ventes) sur une période de 45 minutes.

Tous les bugs logiciels ne sont pas aussi dramatiques. Mais il y a des moments, en tant que développeur logiciel, où vous devez résoudre des bugs aussi vite que possible.

J'ai récemment découvert que des entreprises publiaient des post-mortems accessibles au public sur leurs bugs d'urgence, et je me suis plongé tête la première dans ces documents.

# Qu'est-ce qu'un post-mortem ?

Un post-mortem est un moment où une équipe réfléchit à ce qui a mal tourné dans quelque chose qu'elle a fait, le documente et/ou modifie son processus pour éviter que cela ne se reproduise.

Une mise à jour logicielle a-t-elle mal tourné ? Décomposons une chronologie de l'endroit où les choses ont commencé à mal tourner, et réfléchissons à la manière dont nous aurions pu le détecter plus tôt.

Voici le point le plus important : les post-mortems **NE SONT PAS** destinés à attribuer des blâmes. Si nous examinons l'exemple de The Knight Capitol Group, il n'aurait **JAMAIS** dû être possible pour une seule personne d'oublier quelque chose et de paralyser l'entreprise.

Où était le processus d'assurance qualité où quelqu'un vérifiait le travail du technicien ? L'ont-ils testé avant de passer en production ? N'y avait-il aucun test automatique qui s'exécutait avant le déploiement en production ?

Vous devriez trouver des **défaillances de processus** et non des **défaillances personnelles**.

# Pourquoi devrions-nous faire un post-mortem ?

Pour éviter de répéter les mêmes erreurs encore et encore !

En apprenant de nos échecs passés, nous fournissons des logiciels plus robustes, sans bugs et stables.

Plus important encore, nous pouvons détecter des bugs dont nous ne savons même pas qu'ils existent. Et si nous corrigeons les processus qui étaient susceptibles de causer des problèmes tôt, alors ces erreurs ne se produiront même pas.

Nous voulons tirer toutes les leçons possibles des pannes et des urgences pour nous assurer qu'elles ne se reproduisent jamais. Rien n'est plus précieux que l'expérience.

# Examinons ensemble quelques post-mortems

Je voulais un peu de variété dans les entreprises et les langages, alors examinons quelques exemples de Google, Microsoft et Flowdock.

Un [modèle de post-mortem courant](https://gist.github.com/adhorn/e76339b2050d468d318336c8bf6d7d6d#file-postmortem) contiendra certains détails clés comme :

* quand cela s'est produit
* qui est responsable du post-mortem (et qui effectuera l'analyse)
* quelques leçons apprises
* une chronologie approximative du bug d'urgence et quelques actions issues du post-mortem

Alors, plongeons-nous dans le sujet.

## Google

Si vous avez effectué une recherche Google entre 6h30 et 7h25 PST le 31 janvier 2009, vous avez vu le message "Ce site peut nuire à votre ordinateur" accompagner chaque résultat.

### Que s'est-il passé ?

Google marque les résultats de recherche avec ce message si le site est connu pour installer des logiciels malveillants. Il s'agit d'un avertissement pour protéger les utilisateurs de Google, compilé avec les algorithmes automatiques de Google, la saisie manuelle de données et une organisation à but non lucratif appelée [StopBadWare.com](https://www.stopbadware.org/).

L'un des développeurs avait mis à jour la liste et avait accidentellement entré un `/`, qui s'est résolu pour chaque site !

Nous savons que celui-ci était une erreur humaine, et à cause de cela, Google a mis en place des tests et des vérifications chaque fois que ce fichier est modifié. (Et je n'ai pas vu cela se reproduire depuis 2009 !)

Le post-mortem complet peut être trouvé [ici](https://googleblog.blogspot.com/2009/01/this-site-may-harm-your-computer-on.html).

## Microsoft

Microsoft a connu une panne de 12 heures le 29 février 2012.

### Que s'est-il passé ?

Microsoft dispose de **Fabric Controllers**, qui sont des ordinateurs contrôlant environ 1 000 serveurs. Ils gèrent leurs cycles de vie, surveillent leur santé et redémarrent les serveurs lorsqu'ils tombent en panne.

Isoler tous ces serveurs en clusters de 1 000 serveurs les aide à maintenir la modularité et à localiser les défaillances à un seul **Fabric Controller** (plutôt que tous leurs serveurs tombent en panne).

Chaque serveur du cluster possède quelque chose appelé un **Host Agent**, utilisé par le **Fabric Controller** pour effectuer le travail qu'il juge nécessaire. L'une des choses qu'il gère est le déploiement des certificats SSL pour maintenir les serveurs utilisant HTTPS, une méthode de chiffrement des données.

Pour savoir quand ces certificats SSL doivent être régénérés, ils prennent le lendemain à minuit et ajoutent un an. Ainsi, si le **Fabric Controller** crée un nouveau certificat pour un serveur le 19 mars 1990, il expirera le 20 mars 1991.

Voyez-vous où cela mène ? Ces serveurs ont tenté de générer un certificat d'un an pour un serveur lors d'une année bissextile. Ils essayaient de définir les certificats pour qu'ils expirent le **30 février 2020**.

Lorsque les certificats échouent à se générer pour le serveur, il se termine. Et s'il se termine trois fois de suite, il est considéré comme une défaillance matérielle, puis indique au **Fabric Controller** qu'il est défectueux.

Le **Fabric Controller**, dans une tentative de "réparer" le serveur défaillant, transférera le travail à un autre serveur. Un par un, tous les serveurs généreront une erreur en essayant de générer ces certificats. Et cela finit par éteindre le **Fabric Controller** (avec ses 1000 serveurs !).

Ce désastre est le résultat d'un code défectueux. Il existe de meilleures façons de gérer les problèmes de date comme les années bissextiles et les différences de fuseaux horaires.

Le post-mortem complet peut être trouvé [ici](https://azure.microsoft.com/en-us/blog/summary-of-windows-azure-service-disruption-on-feb-29th-2012/).

## Google, deuxième partie

Du jeudi 13 août 2015 au lundi 17 août 2015, il y a eu des erreurs sur les services Google Cloud, ainsi qu'une perte de données permanente sur 0,000001 % de certains disques durs.

### Que s'est-il passé ?

Il y a eu quatre impacts de foudre successifs sur le réseau électrique local qui alimentait les ordinateurs de Google alimentant les services Google Cloud.

Il y avait des systèmes qui ont commencé à remplacer immédiatement l'énergie qui avait été coupée en utilisant une batterie de secours. Avec l'intervention manuelle des employés de Google, le service a été restauré avec une perte permanente minimale.

Google a un programme continu de mise à niveau de son infrastructure afin qu'elle soit moins susceptible de rencontrer des problèmes comme celui-ci. Après cela, ils ont effectué une analyse couvrant la distribution électrique, le logiciel contrôlant les services Cloud et le matériel Cloud utilisé.

Le post-mortem complet peut être trouvé [ici](https://status.cloud.google.com/incident/compute/15056#5719570367119360).

## Flowdock

La messagerie instantanée Flowdock est devenue indisponible pendant environ 32 heures entre le 21 et le 22 avril 2020. Un comportement étrange a également été observé, comme certains utilisateurs ne pouvant pas se connecter. De plus, certaines personnes ont trouvé des utilisateurs d'une autre organisation dans leur organisation (comme des employés d'Amazon contaminant Microsoft, par exemple).

### Que s'est-il passé ?

Le coronavirus a provoqué une augmentation soudaine du nombre de personnes travaillant depuis chez elles, ce qui a entraîné une utilisation plus élevée que d'habitude de Flowdock. Cela a causé une utilisation très élevée du CPU et a fait planter la base de données tout en essayant de gérer la charge. Il y a également eu une certaine perte de données permanente.

Le post-mortem complet peut être trouvé [ici](https://flowdock-resources.s3.amazonaws.com/legal/Flowdock-RCA-For-Incident-On-2020-04-21.pdf).

# Points à garder à l'esprit lors de la rédaction d'un post-mortem

J'ai lu un article fantastique d'Adrian Hornsby, un Principal Developer Advocate d'Amazon. Dans cet article, [il a discuté](https://medium.com/the-cloud-architect/incident-postmortem-template-7b0e0a04f7a8) de certaines choses à éviter et de points à souligner afin de rédiger le meilleur post-mortem possible si vous êtes un jour responsable de l'un d'eux.

Voici quelques-unes de ses suggestions :

* Ne faites pas de post-mortems pour blâmer des personnes, des équipes ou des organisations. Concentrez-vous plutôt sur le ou les **processus** qui ont échoué et permis à ces erreurs de causer des problèmes. Ne faites jamais de post-mortem pour punir quelqu'un. Cela n'a aucune valeur et vous ne trouverez pas d'améliorations.
* Ne supposez pas que les événements qui se sont produits étaient plus prévisibles qu'ils ne l'étaient. Ce n'est que parce qu'ils se sont produits qu'ils sont maintenant évidents. (**[Biais de rétrospection](https://en.wikipedia.org/wiki/Hindsight_bias)**)
* Assurez-vous d'aller suffisamment en profondeur. Ne vous contentez pas de dire que nous avons vu une erreur dans le code frontal. Creusez vraiment pour comprendre l'erreur spécifique et les conditions qui y ont conduit. Comment le processus peut-il détecter cela la prochaine fois ? Un meilleur processus de QA ? Plus de revues par les pairs ? Une meilleure journalisation des erreurs ?
* Si vos étapes de résolution pour empêcher que cela ne se reproduise sont vraiment vagues comme "améliorer la documentation" ou "mieux former", vous ne comprenez pas clairement assez pour être plus spécifique. Rendez ces étapes de résolution actionnables et concrètes.
* Essayez de garder vos étapes de résolution à des choses qui peuvent être faites à **court terme**. Nous essayons d'empêcher que cela ne se reproduise dès que possible. Les post-mortems peuvent engendrer des changements de processus à plus long terme, mais ce n'est pas sur cela que vous vous concentrez pour le moment. N'essayez pas de réarchitecturer quelque chose de fondamental ou d'essayer de changer le langage dans lequel un énorme codebase est écrit.
* Laissez votre post-mortem remettre en question ce que votre équipe croit actuellement être vrai. Ne supposez pas que quelque chose est vrai simplement parce que tout le monde le croit ([**Sophisme de la croyance commune](https://en.wikipedia.org/wiki/Argumentum_ad_populum)**)

## Comment en apprendre davantage

Si vous avez aimé cela, vous pouvez trouver plus de post-mortems publics [ici](https://github.com/danluu/post-mortems). Ceux-ci incluent des post-mortems des entreprises que nous avons déjà discutées ainsi que des exemples d'Amazon, GitHub, Linux, Heroku, Spotify, Valve, Cloudfare, Etsy, GoCardless, Travis CI et plus encore.

## Conclusion

J'espère que cela a expliqué ce qu'est un post-mortem dans le cycle de vie du développement logiciel, comment en rédiger un efficacement et les erreurs courantes qui se produisent lorsque vous en rédigez vos premiers.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.