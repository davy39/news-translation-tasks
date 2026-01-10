---
title: Comment être un joueur d'équipe en tant qu'ingénieur logiciel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-29T23:50:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-be-a-team-player
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99fd740569d1a4ca22e3.jpg
tags:
- name: 'self-improvement '
  slug: self-improvement
- name: Software Engineering
  slug: software-engineering
- name: teamwork
  slug: teamwork
seo_title: Comment être un joueur d'équipe en tant qu'ingénieur logiciel
seo_desc: "By Moshe Siegel\nIn my first software engineering role at an eCommerce\
  \ brand, I often secretly worked on tasks outside of my core responsibilities. And\
  \ many times I felt isolated from my teammates. \nTherefore, when I was invited\
  \ to participate in a pr..."
---

Par Moshe Siegel

Dans mon premier rôle d'ingénieur logiciel pour une marque de commerce électronique, je travaillais souvent en secret sur des tâches en dehors de mes responsabilités principales. Et beaucoup de fois, je me sentais isolé de mes coéquipiers. 

Par conséquent, lorsque j'ai été invité à participer à un cours basé sur un projet pour améliorer mes compétences en communication, j'ai saisi l'opportunité. 

Pour le programme, j'ai été assigné à une équipe avec deux autres ingénieurs et un chef d'équipe pour construire une application full stack en utilisant React, Python et Flask. Maintenant que le cours est terminé, j'ai pensé partager les leçons que j'ai apprises sur la façon d'être un meilleur joueur d'équipe. 

## Leçon 1 : Ne sous-estimez pas le niveau de difficulté potentiel d'un projet

Puisque le cours était destiné aux ingénieurs de niveau débutant, je pensais avoir une longueur d'avance car j'avais déjà une certaine expérience professionnelle avec Node.js. Certes, notre stack technique utiliserait un backend Python Flask, mais je pensais que Python et Flask ne seraient pas trop difficiles à apprendre. 

Le premier jour de notre projet, on nous a montré ce que nous allions construire. Wow, je me sentais soudainement très mal préparé. Notre projet était significativement plus difficile que je ne l'avais prévu.

Mes deux autres coéquipiers semblaient assimiler le matériel facilement. À la fin de notre première semaine, j'étais le membre de l'équipe qui contribuait le moins. 

Je connaissais assez bien React, donc notre frontend n'était pas trop difficile pour moi. Mais notre backend utilisait PostgresSQL et Python, que je ne connaissais pas bien. Il est rapidement devenu clair que les tâches attendues de nous seraient particulièrement difficiles pour quelqu'un avec peu d'expérience en Python.

## Leçon 2 : Demandez des retours sur le travail en cours

Au début, je me suis souvent retrouvé à perdre du temps en faisant du travail inutile. Par exemple, une fois, je créais un formulaire de profil utilisateur modifiable, sans réaliser que mon coéquipier était en train de construire un composant de dialogue Material UI réutilisable que j'aurais pu utiliser. 

Une autre fois, j'ai passé du temps à lire un tutoriel sur la façon d'obtenir l'identité d'un utilisateur authentifié, sans réaliser que mon coéquipier avait déjà trouvé la solution. 

Réalisant combien de temps je passais à faire du travail inutile, j'ai commencé à poster dans notre tableau de messages Slack ce sur quoi je travaillais et à demander des retours. Mes coéquipiers étaient rapides à répondre. En ayant mes collègues donner leur avis sur mes conceptions inachevées, j'ai pu éviter de dupliquer le travail.

## Leçon 3 : Lorsque vous êtes pressé par le temps, priorisez ce qu'il faut éviter d'apprendre

Étant donné que j'avais du mal à suivre la charge de travail, je devais mieux prioriser mon temps. Chaque fois que quelqu'un créait une nouvelle fonctionnalité, il créait une Pull Request (PR) Git pour demander que le code soit révisé. Au début, je révisais chaque PR et leur accordais toute mon attention. Cependant, cela s'est rapidement avéré impraticable. 

Je me souviens avoir passé beaucoup de temps à réviser la PR pour ajouter des cookies et des tokens pour l'authentification. Pour faire une révision appropriée, j'ai d'abord lu beaucoup d'informations de fond sur les problèmes de sécurité tels que les cookies, le stockage local et les attaques de cross-site scripting. Lorsque j'ai terminé toute cette lecture, j'ai lu la PR, pour découvrir que tout le code avait du sens et qu'il n'y avait rien à commenter. 

Avec le recul, étant donné à quel point j'étais en retard avec mes propres tâches, j'aurais dû ignorer une grande partie de la documentation sur les cookies et au lieu de cela, faire simplement une révision rapide de la PR pour gagner du temps. 

Acquérir une connaissance approfondie du fonctionnement interne de notre authentification par cookie était de peu d'utilité pour ma productivité globale. En revanche, d'autres PR, comme celle qui a configuré React Context pour passer l'état à travers notre application, affectaient directement presque toutes les fonctionnalités sur lesquelles je travaillais. 

Prioriser l'acquisition d'une compréhension approfondie de cette PR aurait été une utilisation bien plus précieuse de mon temps.

## Leçon 4 : Construisez de nouvelles fonctionnalités en allant de morceau en morceau

Pour m'organiser davantage, j'ai dû apprendre à parcourir rapidement la documentation technique. J'ai appelé un ami ingénieur senior, Sean Ellison-Chen, et lui ai demandé son processus pour aborder une nouvelle fonctionnalité qui nécessite une technologie qui lui est totalement nouvelle. 

Il a expliqué qu'il essaie d'abord de comprendre au maximum 70 % de ce qui se passe, puis commence immédiatement à construire la fonctionnalité par morceaux. Chaque morceau est commit dans git. 

Par exemple, s'il doit configurer des web sockets, il pourrait mettre en place une structure de base pour les web sockets, la commiter dans git, puis travailler sur le morceau suivant de la configuration des événements de socket corrects, et ainsi de suite. 

En travaillant par morceaux, il assure une progression fluide, passant de la gestion des minimums nécessaires à l'obtention d'une fonctionnalité entièrement opérationnelle.

## Leçon 5 : Demandez des retours à votre chef d'équipe

À mi-parcours du programme, j'ai reçu des retours de notre chef d'équipe, Shums Kassam. On m'a dit de demander de l'aide plus souvent, de parcourir rapidement la documentation et de tirer parti de mes coéquipiers. 

J'ai pris les conseils à cœur et j'ai augmenté le nombre de fois où je postais dans notre tableau de messages. J'ai commencé à avoir des appels vidéo avec des coéquipiers pour réviser les fonctionnalités que je construisais. J'ai parcouru plus rapidement la documentation technique et j'ai évité les zones moins critiques. En mettant en œuvre ces changements, mon taux de contributions s'est accéléré.

## Leçon 6 : Évitez de faire un travail parfait sur des tâches dont les exigences pourraient changer

Par pure chance, j'ai appris l'importance de procrastiner sur les tâches dont les exigences pourraient changer. 

L'une de mes premières tâches était de construire un formulaire frontend qui permet aux utilisateurs de changer leurs informations de profil. Lorsque j'ai soumis mon code pour révision, on m'a dit que l'apparence du formulaire devait être corrigée car certaines des longueurs d'entrée ne correspondaient pas. 

Normalement, j'aurais passé les 45 minutes à le corriger sur-le-champ. Mais j'étais très en retard dans mes contributions, alors au lieu de cela, j'ai simplement commenté un "todo" sur la correspondance des longueurs d'entrée et j'ai fusionné mon code. 

Une semaine plus tard, un coéquipier a souligné qu'il serait préférable pour l'expérience utilisateur de combiner les entrées séparées 'rue', 'ville', 'état' et 'pays' en une seule entrée 'adresse'. Lorsque il a simplifié les entrées, mon "todo" commenté n'était plus applicable. 

En procrastinant sur le travail du formulaire, je m'étais évité de faire un travail inutile.

## Leçon 7 : Soyez à l'aise de soumettre du code non refactorisé

Vers la fin de notre projet, notre équipe se précipitait pour terminer toutes nos fonctionnalités avant une date fixe où nous présenterions notre projet à un public. Nous avions prévu de soumettre toutes les fonctionnalités bien à l'avance pour nous donner suffisamment de temps pour pratiquer et répéter. 

Mais j'ai fini par soumettre ma dernière fonctionnalité avec à peine une heure avant notre démonstration et nous avons dû nous dépêcher de l'ajouter. Bien que notre présentation se soit bien passée, j'étais troublé d'avoir soumis la fonctionnalité si tard, car cela a sévèrement réduit la capacité de notre équipe à répéter notre démonstration à l'avance. 

Avec le recul, je réalise que, au lieu de soumettre un code optimisé et propre, j'aurais pu économiser au moins deux heures de temps en ajoutant simplement des commentaires sur la refactorisation plus tard.

Au cours des derniers mois, j'ai appris de nombreuses leçons sur la façon d'être un meilleur joueur d'équipe. Plus important encore, j'ai appris que le travail d'équipe est une compétence qui peut être améliorée comme toute autre.

Le programme auquel j'ai participé était dirigé par [Hatchways](https://hatchways.io/), une entreprise qui aide les ingénieurs logiciels à obtenir leur premier emploi. Au moment de la rédaction de cet article, ils desservent les ingénieurs et les entreprises en Amérique du Nord. Si vous êtes un employeur cherchant à embaucher des stagiaires ou des ingénieurs de niveau débutant, voir [Hatchways - Employeurs](https://hatchways.io/employers).