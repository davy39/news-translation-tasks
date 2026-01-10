---
title: Ma Première Aventure Open Source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-06T15:42:39.000Z'
originalURL: https://freecodecamp.org/news/my-first-open-source-adventure-82a33f89113
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d-pS9aIt4Fywwa0QJGgCvg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Ma Première Aventure Open Source
seo_desc: 'By Anthony Ng

  ✨✨ Inspiration ✨✨

  The idea of open source has always resonated with me. What’s not to like about people
  volunteering their time and knowledge for the common good?

  So after reading Shubheksha’s article Hey newbie open source contributors...'
---

Par Anthony Ng

### ✨✨ Inspiration ✨✨

L'idée de l'open source a toujours résonné en moi. Qu'est-ce qu'il n'y a pas à aimer chez les gens qui offrent leur temps et leurs connaissances pour le bien commun ?

Ainsi, après avoir lu l'article de [Shubheksha](https://www.freecodecamp.org/news/my-first-open-source-adventure-82a33f89113/undefined) [Hey newbie open source contributors: please blog more](https://medium.freecodecamp.com/new-contributors-to-open-source-please-blog-more-920af14cffd#.rwxevlacv), j'ai décidé de me lancer.

On m'a dit que travailler sur des projets open source est l'une des meilleures façons d'apprendre.

* Vous pouvez voir du code écrit par des développeurs plus expérimentés.
* Vous pouvez travailler avec des technologies que vous n'auriez pas autrement utilisées dans vos propres projets personnels.

Contribuer à l'open source est une façon d'exprimer votre nature altruiste. J'imagine un personnage de Robin Hood armé d'un MacBook (que l'on distingue à peine sous ses 20 autocollants), combattant courageusement les logiciels d'entreprise encombrants et propriétaires.

![Image](https://cdn-media-1.freecodecamp.org/images/pXOHlz1kYkryoexWwm9K5JqW2FJtH2z8NWit)
_Imaginez ses flèches comme des commits._

Je voulais être un Robin Hood de l'open source.

### ⚠️⚠️ Craintes ⚠️⚠️

Alors que je fixais mon écran, la première de nombreuses craintes m'est venue à l'esprit. Et si je suis submergé par la complexité de ces projets open source ?

Faire face à un dépôt contenant 2 000 commits était assez intimidant — surtout lorsque mes projets personnels ne dépassaient pas 40 commits.

Alors que je commençais à naviguer à travers la forêt de fichiers aux noms cryptiques que je n'avais jamais entendus (.snyk, .varci.yml, pm2Start.js), des pensées de syndrome de l'imposteur ont rapidement surgi. Je me suis demandé, « Suis-je vraiment qualifié pour toucher à ce code ? »

J'avais entendu des histoires d'horreur sur des communautés impitoyables. Que se passerait-il lorsque j'arriverais à un point où j'aurais besoin de conseils et devrais réellement... parler à une personne ?

La crainte m'a étouffé alors que je pensais à ma première conversation avec un mainteneur open source. Dans ma tête, leurs réponses allaient de « lol, tu es sérieux ? » à « peut-être que le développement web n'est pas fait pour toi ».

Mais je me suis réconforté en me disant que, comme un troll d'internet, je pouvais me cacher (et ma honte) derrière mon ordinateur.

Je craignais aussi que ma pull request ne soit pas fusionnée. Il était possible que mon travail soit si médiocre que les autres mainteneurs ne prennent pas la peine de me guider dans la bonne direction. Vaudrait-il la peine de consacrer des heures — voire des jours — de mon temps à du code qui pourrait ne jamais être utilisé ?

Malgré ces craintes, j'ai décidé de me lancer dans mon aventure open source.

### ?? Trouver un projet ??

La première étape était de trouver un projet open source sur lequel travailler. L'article de [Shubheksha](https://www.freecodecamp.org/news/my-first-open-source-adventure-82a33f89113/undefined) [How to find your first open source bug to fix](https://medium.freecodecamp.com/finding-your-first-open-source-project-or-bug-to-work-on-1712f651e5ba#.q0bt5j41d) recommandait de consulter [Up For Grabs](http://up-for-grabs.net/) pour trouver des projets candidats. Après avoir rapidement parcouru la liste des projets JavaScript, je n'en ai trouvé aucun qui ait attiré mon attention.

Je voulais trouver un projet que j'utilisais personnellement et auquel je croyais. Le problème était que la plupart de ces projets étaient si matures qu'ils étaient trop avancés pour que je puisse les suivre. Par exemple, j'adore React, mais je n'avais aucune idée de la façon de corriger les « méthodes de cycle de vie de sous-arbre/parent entrelacées de manière inattendue ».

J'étais sûr qu'il existait des projets où je pourrais faire une différence significative, mais ils m'étaient encore inconnus.

Puis je me suis souvenu que Free Code Camp est open source. Il a passé mon test en tant que projet que j'utilise et auquel je crois. J'ai suivi des heures de leur programme, et j'adore la façon dont ils aident les nouveaux développeurs et les associations à but non lucratif en même temps. Je recommande également Free Code Camp à quiconque mentionne vouloir apprendre le développement web.

Ainsi, après avoir parcouru leur [liste des problèmes ouverts sur GitHub](https://github.com/FreeCodeCamp/freecodecamp/issues), j'ai choisi Free Code Camp comme mon premier projet open source.

### ?? Trouver un bug ??

L'étape suivante était de trouver un problème sur lequel travailler. En théorie, cela aurait dû être la chose la plus facile et la plus rapide à faire.

Mais, comme regarder un film sur Netflix, parfois vous passez plus de temps à choisir quelque chose à regarder qu'à le regarder réellement.

Avec plus de 300 problèmes ouverts, j'ai décidé de les filtrer par étiquettes. J'en ai trouvé un étiqueté « first-timers-only » qui semblait assez convivial. Mais ce problème avait plus de 80 commentaires. Je n'allais pas toucher à cela.

Je n'ai pas vu de problèmes auxquels je pouvais me lancer et commencer à travailler, alors j'ai continué ma recherche.

J'ai trouvé une autre étiquette appelée « help wanted » et j'ai cherché des problèmes sur lesquels personne n'avait encore commenté, mais rien ne m'a sauté aux yeux.

J'ai décidé de surveiller le dépôt pour de nouveaux problèmes que personne n'avait encore abordés. Après environ 15 minutes, j'ai vu que la plupart des nouveaux problèmes provenaient de campeurs bloqués sur des défis. Ces problèmes n'étaient pas réellement des bugs que je pouvais corriger.

Puis [le problème #10989](https://github.com/FreeCodeCamp/FreeCodeCamp/issues/10989) est entré dans ma vie. Il était lié à un test d'expressions régulières trop rigide dans l'un des défis de codage.

Je me suis dit : « Je connais un peu les regex. »

Puis un mainteneur a commenté que c'était un problème valide et y a ajouté une étiquette « help wanted ». Mon cœur a commencé à battre alors que je relisais le problème 3 fois de plus pour m'assurer de ne rien avoir manqué.

Puis je me suis dit : « Je peux le faire ! »

J'ai commenté le problème et j'ai timidement demandé si je pouvais travailler dessus. Mes genoux étaient faibles et mes bras lourds. Mes paumes transpiraient alors que j'attendais une réponse. Je me sentais aussi nerveux que si je venais d'envoyer un message à une femme pour lui demander un rendez-vous.

Et enfin, quelqu'un a répondu : « tu peux travailler dessus. »

Il était temps de se mettre au travail.

### ??? Commencer ???

J'ai commencé par lire le fichier README.md dans le dépôt. Heureusement, Free Code Camp a des instructions très détaillées sur la façon de contribuer et de créer des pull requests. Ils ont également un canal Gitter juste pour les contributeurs.

J'ai forké le dépôt et j'ai commencé.

### ?? Trébucher ??

Je savais que la configuration de mon environnement serait difficile. Mon mentor m'a dit qu'il lui avait fallu une semaine pour installer tous les programmes nécessaires avant de pouvoir commencer à contribuer à son premier emploi.

C'est difficile parce que vous devez lire ces messages d'erreur cryptiques dans votre terminal lorsque quelque chose ne s'installe pas ou ne s'exécute pas correctement. Et effectivement, il n'a pas fallu longtemps avant que je rencontre un problème.

Lorsque j'ai exécuté « gulp » pour commencer, il y avait une erreur dans le fichier gulp. Il a mis en évidence une ligne de code qui utilisait la syntaxe de flèche ES6 et a dit qu'il ne la reconnaissait pas. J'ai parcouru le reste du fichier et n'ai vu aucune autre utilisation de la syntaxe de flèche ES6. Avais-je oublié une étape dans le processus de construction ?

J'ai cherché une solution sur Google et n'ai rien trouvé d'utile. J'ai donc décidé de bidouiller. J'ai transformé la flèche ES6 en une déclaration de fonction régulière et j'ai vu ce qui se passait. La commande « gulp » ne se plaignait plus et a configuré un localhost.

Grisé par ce succès, il n'a pas fallu longtemps avant que je rencontre un autre obstacle. Je suis allé sur mon localhost et j'ai été accueilli par la page d'accueil de Free Code Camp, sauf qu'elle n'était pas fonctionnelle. Cliquer sur le lien « map » qui affiche normalement tous les défis ne faisait rien. Il y avait un certain nombre d'erreurs dans la console, notamment un fichier « bundle.js » manquant.

Je me suis reproché d'avoir manqué une étape quelque part et j'ai décidé de recommencer depuis le début. J'ai supprimé ma copie locale du dépôt et j'ai réinstallé tout, en faisant attention à être extra vigilant avec chaque frappe. Je suis tombé sur les mêmes erreurs et j'ai décidé qu'il était temps d'utiliser le canal Gitter.

Lorsque je me suis connecté pour la première fois au canal Gitter, j'ai vu beaucoup de messages parlant des nouvelles mises à jour de Free Code Camp. À ma droite, j'ai été accueilli par un résumé de l'activité récente sur ce canal, qui incluait le bannissement de quatre personnes. Ces personnes étaient-elles coupables de ne pas avoir réussi à faire fonctionner leurs fichiers gulp ? Avait-elles demandé négligemment où se trouvait leur fichier bundle.js manquant ?

J'ai décidé de relire le guide de contribution au cas où j'aurais manqué quelque chose d'évident. Je l'avais déjà lu tant de fois que je pouvais pratiquement le réciter. Je n'ai rien trouvé de nouveau qui puisse m'aider, alors j'ai trouvé le courage de finalement demander au canal Gitter à propos de mon problème de syntaxe ES6.

Quelqu'un a répondu immédiatement, mais j'ai vite réalisé qu'ils ne me parlaient pas.

J'ai attendu et attendu jusqu'à ce que le salut arrive. Un mainteneur nommé Dylan m'a dit que je devais mettre à jour mon Node et npm. J'ai regardé à nouveau le guide de contribution et j'ai réalisé qu'il indique clairement la version que je devrais utiliser. Comment avais-je pu passer à côté de cela ?!

J'ai remercié Dylan pour son acte de gentillesse et j'ai silencieusement remercié Gitter de ne pas m'avoir banni.

J'ai promptement installé la dernière version de Node et npm. Les choses semblent déjà plus brillantes.

J'ai décidé de tout supprimer et de recommencer depuis le début. C'était ma troisième fois à ce stade, et la configuration de ce projet était devenue une danse familière. J'ai également récupéré du nouveau code qui avait été validé depuis la veille, ce qui a corrigé certaines des erreurs que je voyais.

Je suis tombé sur la même erreur avec le fichier « bundle.js » manquant et j'ai demandé dans le canal Gitter à ce sujet. Quelqu'un a répondu que la commande « gulp » aurait dû le créer. J'ai créé le fichier « bundle.js » en exécutant moi-même la commande « webpack », et enfin l'environnement semblait fonctionner. Je pouvais enfin commencer à travailler sur le problème réel !

La correction réelle a pris un quart du temps que la configuration de mon projet a pris. J'ai écrit une regex qui vérifiait la présence d'un élément. La partie délicate était de transformer ma regex en une chaîne, puis de me souvenir d'utiliser des barres obliques inverses pour échapper les caractères si nécessaire. J'ai mis à jour une ligne de code et j'ai exécuté mes tests, qui ont réussi.

J'ai lu la documentation pour les instructions de pull request. Free Code Camp a une liste de contrôle pré-remplie géniale lorsque vous soumettez une pull request.

J'ai pris une dernière inspiration et j'ai envoyé ma pull request. Je me sentais comme un parent envoyant son enfant à l'école. Il n'y avait plus rien que je puisse faire sauf attendre.

### ?? Pull Request Fusionnée ! ??

Le lendemain, j'ai reçu un email concernant l'état de ma [pull request](https://github.com/FreeCodeCamp/FreeCodeCamp/pull/11026#event-810810708). Quelqu'un a commenté « LGTM ».

J'ai fait une rapide recherche Google et j'ai découvert que cela signifie « Looks good to me ». Puis j'ai ressenti un grand soulagement. Ils avaient fusionné ma pull request !

Mon premier pas dans l'open source avait été un succès !

### ?? Ce que j'ai appris ??

J'ai appris quelques choses techniques en travaillant sur ce problème. J'ai acquis plus d'expérience avec les regex.

J'ai également appris à utiliser des barres obliques inverses pour échapper certains caractères dans les chaînes. Avant cela, j'avais seulement utilisé des barres obliques inverses pour échapper les guillemets.

L'autre avantage est que je me suis beaucoup plus familiarisé avec GitHub.

### ?? Conseils aux nouveaux contributeurs Open Source ??

Ce fut une expérience incroyable pour moi, et je recommande à d'autres nouveaux développeurs de tenter leur chance. Voici mes conseils pour ceux qui sont intéressés à contribuer.

#### Conseil #1 : Travaillez dur et persévérez

Je dirais que 60 % du temps lorsque vous travaillez, tout fonctionne sans problème. Mais c'est les autres 40 % lorsque tout se casse qui définiront qui vous êtes en tant que développeur.

Embrassez ces obstacles et combattez-les.

J'ai appris plus en corrigeant mes bugs que je n'aurais appris si tout avait fonctionné sans accroc.

Changez votre état d'esprit pour accueillir les erreurs. Voyez-les comme des leçons.

#### Conseil #2 : Communiquez autant de détails que possible.

Cela est particulièrement important lorsque vous posez des questions via un mode de communication asynchrone (comme Gitter ou email).

Imaginez que vous utilisez une API pour demander des informations sur la météo dans votre ville. Vous pourriez faire ceci :
 1. Vous demandez à l'API la météo
 2. L'API répond en demandant un lieu
 3. Vous répondez « New York »
 4. L'API demande si vous la voulez en Celsius, Fahrenheit ou Kelvin
 5. Vous répondez « Fahrenheit »
 6. L'API répond avec « 72 degrés Fahrenheit à New York »

Ou vous pourriez faire ceci :
 1. Vous demandez à l'API la météo à New York en Fahrenheit.
 2. L'API répond avec « 72 degrés Fahrenheit à New York »

Il semble idiot que quelqu'un choisisse la première option lorsqu'il travaille avec une API, mais c'est exactement ce que les gens font lorsqu'ils communiquent avec d'autres personnes. Des conversations simples s'éternisent alors que chaque partie attend des minutes ou des heures pour que l'autre réponde.

#### **Conseil #3 : Ne vous laissez pas intimider par les mainteneurs open source.**

Ils peuvent avoir plus d'expérience que vous, mais réalisez qu'à un moment donné, ils étaient dans votre situation, eux aussi. Ils ont simplement survécu à plus d'erreurs que vous.

Rappelez-vous simplement que tous les développeurs sont sur la même longue route. Certains d'entre nous sont quelques étapes derrière les autres. L'important est de continuer à avancer.

### ?? Mots aux mainteneurs Open Source ??

La communauté Free Code Camp est incroyable et a été super utile lorsque j'en avais besoin.

Je veux remercier tous les mainteneurs qui se donnent la peine d'aider les nouveaux contributeurs. Vous pourriez penser que vous faites quelque chose de petit lorsque vous dites à quelqu'un de mettre à jour son Node et npm. Ce que vous ne réalisez peut-être pas, c'est que vous pourriez être leur bouée de sauvetage, les empêchant de se noyer et d'abandonner.

Continuez ce travail formidable !

De plus, faites attention aux mots que vous choisissez d'utiliser.

J'étais en voyage au Japon et je cherchais un restaurant pour dîner. Je suis passé devant un restaurant prometteur, mais il y avait une enseigne sur la fenêtre qui disait « No English Speaking ». Tout le reste était en japonais.

Comment un étranger comme moi aurait-il interprété cette enseigne ? Est-ce que cela signifie que personne là-bas ne parle anglais ? Est-ce que cela signifie que je devrais jouer à la roulette russe avec ce que je pointerais sur le menu ? Est-ce que cela signifie qu'ils sont xénophobes et peu accueillants envers les étrangers comme moi ? J'ai continué à marcher et je n'ai jamais pris la peine de le découvrir.

En tant que mainteneurs, parfois vous êtes la première personne réelle avec laquelle les nouveaux contributeurs communiquent. Soyez conscient que ces contributeurs sont dans un pays étranger qu'est l'open source. Ils peuvent avoir du mal à parler la langue — sans même essayer de corriger un problème ouvert dans le dépôt.

Je prévois de continuer mon aventure open source. J'espère vous voir autour et entendre vos histoires.