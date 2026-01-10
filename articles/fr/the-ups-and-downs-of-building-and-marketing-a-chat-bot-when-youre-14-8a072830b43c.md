---
title: Ce que c'est de construire et de commercialiser un chatbot quand on n'a que
  14 ans
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-26T05:08:14.000Z'
originalURL: https://freecodecamp.org/news/the-ups-and-downs-of-building-and-marketing-a-chat-bot-when-youre-14-8a072830b43c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_GOaInCDqke1b_hpbQTflQ.jpeg
tags:
- name: bots
  slug: bots
- name: Entrepreneurship
  slug: entrepreneurship
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: teens
  slug: teens
seo_title: Ce que c'est de construire et de commercialiser un chatbot quand on n'a
  que 14 ans
seo_desc: 'By Alec Jones

  I’m going to tell you everything I learned while coding a popular Facebook Messenger
  bot, and my crazy first week of marketing it (which involved a tweet from one of
  the Jonas Brothers, a viral Facebook post in Thailand, and an intervie...'
---

Par Alec Jones

Je vais vous raconter tout ce que j'ai appris en codant un bot Facebook Messenger populaire, et ma folle première semaine de marketing (qui a impliqué un tweet de l'un des **Jonas Brothers**, un post Facebook viral en **Thaïlande**, et une interview avec la **BBC**).

### Il s'avère que construire quelque chose d'utile est bien plus difficile que cela n'y paraît

Comme beaucoup de développeurs de logiciels, ma mission de créer quelque chose d'utile a commencé par une décision de [**résoudre mon propre problème**](https://gettingreal.37signals.com/ch02_Whats_Your_Problem.php)_._

Mon problème : J'oubliais toujours quels devoirs je devais finir le soir.

En classe de 8ème, il y avait beaucoup de matins où je devais arriver très tôt à l'école pour les terminer.

Je savais que cela ne fonctionnerait pas pour mes 4 années restantes de lycée car il n'était pas question que je puisse gérer d'arriver à l'école à 6h30 du matin régulièrement pour finir mes devoirs de maths. 😯

J'ai donc décidé de construire un chatbot qui me rappellerait à la fin de chaque cours de lui dire quels devoirs j'avais à faire. J'espérais que beaucoup d'autres étudiants avaient le même problème.

Pourquoi un chatbot ? Certes, il y a beaucoup de buzz autour des bots en ce moment, mais surtout parce que **les étudiants ne sont jamais loin de leurs smartphones** (surtout en classe)... et ils sont déjà familiers avec les SMS. 📱

J'ai commencé par construire un chatbot utilisant les SMS, mais j'ai rapidement appris qu'il y avait un coût à envoyer des messages texte depuis un service SMS basé aux États-Unis (comme Twilio). Et même si j'utilisais un numéro de téléphone canadien, cela serait très cher pour les gens d'utiliser mon bot dans d'autres pays.

Mais Facebook Messenger était gratuit.

En classes de 6ème et 7ème, j'avais appris une quantité raisonnable de PHP, et j'avais créé quelques applications web simples. Mais construire un chatbot utilisant Facebook Messenger était entièrement nouveau, et je pensais que ce serait une grande opportunité d'apprendre Ruby on Rails.

Je devais aussi apprendre l'API de Facebook Messenger et comment créer un site web derrière un login pour gérer les classes et les horaires des étudiants. Ces deux choses à elles seules impliquaient une **courbe d'apprentissage abrupte**, mais je me suis dit qu'il n'y avait rien de plus excitant et satisfaisant que de transformer une idée en quelque chose que les étudiants du monde entier peuvent utiliser.

### « C'est un garçon ! »

Près de 9 mois après avoir commencé à travailler sur mon chatbot, [Christopher Bot](https://www.christopherbot.co/) est né.

Ce n'est pas comme si je travaillais à temps plein sur sa construction. Entre les vacances d'été (pas d'ordinateurs portables autorisés), _l'école_, le football, _l'école_, et plusieurs moments déprimants de « recommencer à zéro », il n'y avait pas tant de périodes de **codage ininterrompu**.

Même avec des rafales sporadiques de temps de développement, CB (comme je l'appelle) s'est avéré exactement comme je l'espérais. C'est un bot Facebook Messenger fiable mais légèrement espiègle qui est dédié à aider les étudiants.

Voici comment il fonctionne...

Après avoir envoyé un message initial à CB et configuré votre emploi du temps, il vous enverra un message vers la fin de chaque cours, vous demandant si vous avez des devoirs ou non. À la fin de chaque journée, CB vous **enverra une liste bien organisée des devoirs** que vous devez terminer.

Simple et utile.

Je pense qu'il fonctionne si bien parce qu'il élimine le besoin pour les étudiants de se souvenir d'écrire les choses. CB se souvient pour eux.

Quand vous partez en vacances, vous pouvez mettre CB en pause et il vous demandera de choisir une date pour reprendre les messages. Si vous oubliez de lui dire vos devoirs juste après le cours, vous pouvez le rattraper plus tard.

Il n'y a pas une tonne de commandes compliquées. Et puisque tant d'étudiants ont leur téléphone dans leur poche toute la journée, Christopher Bot est toujours avec eux.

**Fait amusant :** Christopher est le nom qu'Alan Turing a donné à sa machine pendant la Seconde Guerre mondiale qui a craqué le [code Enigma](https://en.wikipedia.org/wiki/Enigma_machine), et c'est la raison pour laquelle j'ai nommé mon bot _Christopher_.

### Concevoir un bot convivial est encore plus difficile que de trouver l'idée originale

Pour moi, la partie la plus importante de CB est sa mémoire « parfaite ». Il se souvient d'envoyer un message à l'étudiant et non l'inverse.

Des questions simples avec des réponses simples rendent la conversation plus rapide. Christopher Bot n'est peut-être pas le bot le plus intelligent qui existe, mais il sait comment aller droit au but. 🎯

Pour que CB fasse la plupart du travail, il doit avoir des informations sur les cours d'un étudiant. Et obtenir ces informations **nécessite un formulaire web**.

Je me suis dit que si les utilisateurs devaient taper la même chose encore et encore pour chaque jour de cours, ils pourraient s'ennuyer ou se distraire (ou les deux) et partir. Donc, pour accélérer les choses, j'ai décidé de **créer un formulaire à remplissage automatique**, basé sur les données de cours qu'un étudiant entre la veille.

Ainsi, un utilisateur entre ses cours pour le lundi, puis lorsqu'il passe à la création de ces mêmes cours pour le mardi, les données sont déjà là dans le formulaire — prêtes à être acceptées telles quelles ou ajustées. Pour la plupart des étudiants, entrer les données de cours prendra moins de 30 secondes. ⚡

![Image](https://cdn-media-1.freecodecamp.org/images/e8NTV9E46RrvjpDzvRH3zFeLQhnIJiuiNapY)

Je voulais aussi que les conversations avec Christopher Bot avancent rapidement car il n'y a pas beaucoup de temps entre les cours.

Les [Bitmojis](https://www.bitmoji.com/) et les GIF peuvent être cool, mais je voulais que la conversation soit nette et propre, pour que les étudiants n'aient pas à passer beaucoup de temps à parler à Christopher Bot.

Ma prochaine grande décision de conception a donc été d'ajouter des **« réponses rapides » de Messenger**.

Ce sont de petits boutons qui se trouvent juste au-dessus du clavier, donc un utilisateur n'a pas à taper une réponse complète. Utiliser des réponses préenregistrées pour « Oui » et « Non » fait gagner du temps à l'utilisateur, et cela **contrôle aussi l'ensemble des réponses**, donc je n'ai pas à m'inquiéter des gens qui répondent avec ouais, yep, nan, nope, etc. 🎯

![Image](https://cdn-media-1.freecodecamp.org/images/lOLk5JUQ2YSFnAcddqx4BhkK5NAfQsQywQRW)

Enfin, je voulais que Christopher Bot ait un côté « humain » sans prétendre _être humain_. Pour y parvenir, j'ai ajouté un délai de frappe pour la plupart des réponses automatiques, imitant ainsi une vraie conversation.

Si CB répond en moins de 1 ms, certains utilisateurs pourraient ne pas réaliser qu'un nouveau message a été livré... cela se passe juste trop vite.

Les délais de frappe sont une belle fonctionnalité supplémentaire de Facebook Messenger — l'une des plusieurs outils intelligents pour aider les bots à paraître plus humains, mais **sans essayer de tromper les gens**.

### Sérieusement, combien y a-t-il de fuseaux horaires ?

L'un de mes plus grands défis dans le développement de Christopher Bot a été de **gérer les fuseaux horaires** dans le monde. J'ai bien compris le concept, mais trier les horaires des cours et des messages dans 24+ fuseaux horaires nécessitait une compréhension plus approfondie.

Les horaires des cours sont tous stockés dans le fuseau horaire local de l'utilisateur, et chaque fois que CB envoie un message à un utilisateur, cela est basé sur ce même fuseau horaire local.

Assez simple, mais Christopher Bot (c'est-à-dire le serveur) « vit » dans un seul fuseau horaire.

Ainsi, lorsque CB vérifie la base de données pour décider d'envoyer ou non un message à ce moment-là, il doit d'abord vérifier si l'heure du serveur correspond à l'heure de fin de cours _dans le fuseau horaire de l'utilisateur_.

J'ai trouvé que la meilleure façon de gérer cette situation compliquée était de convertir toutes les heures en [**Temps Universel Coordonné**](https://www.timeanddate.com/time/aboututc.html) **(UTC)**. Ensuite, tout ce que j'avais à faire était de stocker le décalage UTC (UTC +/-) avec les heures de fin de cours des étudiants, pour m'assurer que tout était aligné.

### Les modèles de page d'accueil sont la meilleure invention jamais (une fois que vous les connaissez)

Lorsque les utilisateurs visitent [https://www.christopherbot.co/](https://www.christopherbot.co/), ils sont accueillis par une belle page d'accueil. Ce n'est pas moi qui l'ai conçue, cependant.

Je ne suis pas un magicien HTML/CSS, alors j'ai décidé d'**acheter un modèle Bootstrap** à incorporer dans mon application.

Je pensais que sa mise en place se ferait en 3 étapes simples :

1. Acheter un modèle
2. Ajouter les différentes pièces à mon répertoire
3. Me détendre en sachant que j'ai un **site web sexy**

J'avais TORT. _Tellement_ tort !

L'application qui « alimente » Christopher Bot est construite sur Ruby on Rails.

Le problème était que mon modèle Bootstrap ne savait pas que j'utilisais Ruby on Rails.

J'ai donc passé des jours à apprendre comment Rails utilise les fichiers Javascript, référence les images, etc. Et environ une semaine plus tard, j'ai enfin réussi à tout faire fonctionner. Les images se chargeaient, et tout avait l'air magnifique.

Mais j'ai commencé à remarquer quelques problèmes. Les animations d'icônes Javascript étaient trop.

La barre de navigation était cassée.

Et surtout, la **fonctionnalité de défilement du navigateur avait été altérée**, faisant défiler la page trop rapidement sur Chrome — et pas du tout sur Safari et Firefox !

Frustré par les variations entre les navigateurs... au point de vouloir jeter mon moniteur par la fenêtre de ma chambre... j'ai décidé qu'il serait préférable de résoudre le problème plutôt que d'expliquer à mes parents comment mon moniteur avait soudainement « disparu ».

Il était clair que le Javascript était mon plus gros problème, et j'ai essayé une approche extrême pour le résoudre.

**J'ai supprimé chaque morceau de Javascript** dans le modèle de mon application. En m'attendant à ce que tout se casse, j'ai été choqué de voir que l'inverse s'était produit.

Non seulement la vitesse de défilement et les problèmes de compatibilité entre navigateurs étaient résolus, mais la navigation aussi, et les effets visuels ennuyeux avaient disparu.

Je n'arrivais pas à croire que j'avais réussi à tout réparer en essayant de tout casser.

Essayer de ruiner votre application n'est pas une bonne solution pour résoudre les problèmes de codage. Mais j'ai réalisé que **certains résultats sont totalement inattendus**. J'ai essayé quelque chose qui semblait être un coup de dés, et cela m'a appris que vous devriez tout essayer avant d'abandonner.

### Un utilisateur et plus...

Comment faire grandir un chatbot d'un utilisateur à de nombreux utilisateurs ? Idéalement par le bouche-à-oreille. Peut-être même _viral_.

Les gens sont toujours curieux des nouvelles choses que leurs amis utilisent. J'espérais que les étudiants verraient leurs amis utiliser Christopher Bot et demanderaient ce que c'est. C'est organique, et c'est aussi du marketing gratuit (parfait, puisque je n'ai pas d'argent pour les publicités PPC !).

J'ai construit un **bouton de partage** dans CB pour aider à faire avancer les choses. Après 1 semaine d'utilisation, Christopher Bot demande poliment aux utilisateurs de partager Christopher Bot sur Facebook. Tout ce qu'un utilisateur a à faire est de cliquer sur le lien, et il peut facilement partager CB avec ses amis.

Mais avec seulement une poignée d'amis utilisant Christopher Bot au début du mois de février, je devais trouver un moyen d'obtenir plus de visibilité.

### Bienvenue sur la page d'accueil d'Internet

Avant d'essayer de commercialiser CB de manière importante, j'avais besoin d'obtenir des retours supplémentaires de mon public cible.

Où les lycéens et les étudiants se retrouvent-ils en ligne ? Il s'avère que c'est assez difficile de trouver de grandes communautés de lycéens sur le web, mais [**Reddit**](https://www.reddit.com/) **est un excellent endroit pour trouver des étudiants**.

J'ai posté sur quelques sous-reddits pour des universités spécifiques, en commençant par quelques-unes dans ma province natale, la Colombie-Britannique — demandant des retours sur le concept général et si Christopher Bot pourrait fonctionner pour les étudiants.

Les utilisateurs de Reddit ont été assez utiles dans l'ensemble, partageant leurs opinions et offrant des retours utiles sur les différences de « devoirs » entre le lycée et l'université.

Mais il y avait aussi un tas de sceptiques qui insistaient sur le fait que je n'avais pas 14 ans...

Voici un commentaire d'un **vrai sceptique** :

« Être un 'petit entrepreneur' est une excellente tactique de marketing. Ce garçon de 14 ans ? Il est en fait un homme plus âgé, mais il se déguise en jeune garçon pour plaire à tout le monde. Voir un petit enfant capable de faire autant est beau, attrayant et tout le monde se sent incité à soutenir ce petit enfant simplement parce qu'il est bien... petit. »

Et un autre de quelqu'un qui pense **que je suis un marketeur désespéré** :

« Cela n'a certainement pas été fait par cet enfant et est certainement conduit et commercialisé par quelqu'un qui a beaucoup d'expérience. Comme ils ont même eu la prévoyance de mettre un marqueur 'ref=reddit' dans l'URL. Ils font du spam pour leurs analyses. »

Donc quelqu'un qui a 14 ans ne peut pas comprendre comment créer un simple paramètre d'URL ? Boo.

### Atteindre le grand public : Product Hunt et Kevin Jonas

Mon objectif numéro 1 pour février était de lancer sur [Product Hunt](https://www.producthunt.com/), et après que mon père ait posté un message sur son compte Facebook à propos de Christopher Bot, j'ai entendu parler d'Andrew Wilkinson de [Metalab](http://metalab.co/) (et Dribbble et Designer News)... qui a gentiment offert de « chasser » CB le 16 février (merci Andrew). Andrew vit aussi à Victoria !

Andrew a posté CB sur Product Hunt peu après minuit, alors que je dormais profondément (pas _vraiment_).

Malheureusement pour moi, de nouveaux produits de Google et Facebook ont également été postés ce jour-là. 😬

Même avec la forte concurrence, **CB a tout de même réussi à obtenir 300+ votes positifs**, des tonnes de commentaires encourageants, et a terminé à la 6ème place globale de la journée. 🎉

![Image](https://cdn-media-1.freecodecamp.org/images/RJ7AVU1LSwv0N2rhsyW1eW0oZU2f5WZNlPUy)

C'était très amusant de regarder CB sur Product Hunt, et cela m'a beaucoup appris sur le monde de l'entrepreneuriat — y compris l'importance de simplement mettre quelque chose devant les gens.

Des gens comme Kevin Jonas. 😮

C'était probablement en partie à cause de mon âge, mais je pense que Kevin Jonas a tweeté à propos de CB ce jour-là (**à ses 5,1 millions de followers !**) parce qu'il a vu que cela serait utile pour d'autres étudiants.

![Image](https://cdn-media-1.freecodecamp.org/images/SY1QwGAlKq0zL2stVvu0wTrAEw8OEU2CCjZp)

Quelqu'un d'autre a remarqué CB sur Product Hunt... [BBC News](http://www.bbc.com/news) journaliste, Dave Lee.

### Mon interview excitante et légèrement effrayante avec BBC News

Le jeudi — jour de lancement de Product Hunt — Dave Lee de BBC News m'a contacté pour écrire un article sur CB :

![Image](https://cdn-media-1.freecodecamp.org/images/vUG2AMYHnuHB-DPWXVCCXoX5culgaWGTH0Mw)

Le vendredi après-midi, mon père et moi avons rejoint Dave via Skype et j'ai partagé toute mon histoire. J'étais super nerveux avant l'appel, mais Dave m'a mis à l'aise (_merci, Dave_).

Dave nous a dit qu'il travaillerait sur l'article bien dans la soirée du vendredi, mais il n'était pas en ligne quand je suis allé me coucher à minuit. Mais dès le lendemain matin, j'ai vérifié les inscriptions à Christopher Bot... et il y avait plus de 1 000 nouveaux comptes créés pendant la nuit.

[**L'article était en ligne.**](http://www.bbc.com/news/technology-39013950)

Et avec 1 000 nouveaux comptes sont arrivés un tas de rapports de bugs et des dizaines de nouvelles demandes de fonctionnalités. J'ai dû quitter le mode marketing et **entrer en mode support à plein temps**.

Seulement 72 heures plus tard, Dave Lee a envoyé un email à mon père :

« Alec m'a demandé combien de lecteurs nos articles ont tendance à avoir, [et] je lui ai dit que nous considérons 500 000 visites uniques comme un succès. Je suis heureux de dire que l'article sur Christopher Bot a eu 1 000 000 de vues uniques depuis sa publication samedi. »

### Boom ! Devenir viral... en Thaïlande

Selon les analyses de Facebook, un tas de nouveaux comptes provenaient de Grande-Bretagne (ce qui est logique, étant donné l'article de la BBC).

Mais un pays dépassait le Royaume-Uni en nouveaux comptes : **la Thaïlande**.

Wha ?!?!

Ensuite, l'un des nouveaux utilisateurs de CB m'a envoyé ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/4B1gQ99DGCXmFbL2PSrYvkBKH27-lssq04Gj)

Quelqu'un avait posté un petit texte sur Christopher Bot sur Facebook en Thaïlande.

Et oui, c'est **11 000 likes**... 3 800 partages... et 205 commentaires (aucun que je n'ai pu comprendre — même _avec_ Google Translate).

### Qu'est-ce qui attend Christopher Bot

Construire Christopher Bot a été une grande expérience pour moi pour apprendre sur les bots et comment rendre les interactions d'un bot **bien fonctionner pour ses utilisateurs**.

En plus d'ajuster la façon dont les cours sont planifiés (une demande courante des nouveaux utilisateurs), mon objectif pour l'avenir est d'améliorer les compétences conversationnelles de CB.

Je veux qu'il soit capable de « comprendre » davantage pour qu'il puisse être encore plus utile pour les étudiants. Je veux qu'il soit capable de comprendre plus de variations dans les réponses ainsi que de reconnaître les fautes d'orthographe comme « textbok work » ou « stdy for my quiz ».

Christopher Bot peut toujours être rendu plus intelligent.

Une nouvelle fonctionnalité que j'envisage de construire est les « analytics de devoirs » — par exemple, pour suivre quels cours ont le plus de devoirs assignés. Christopher Bot collecte beaucoup de données chaque jour (individuellement et en agrégat), et ce serait cool de partager ce qu'il apprend avec les utilisateurs.

J'ai eu beaucoup de plaisir à créer et à commercialiser Christopher Bot — et il y a eu **beaucoup plus de hauts que de bas** dans ce voyage.

J'espère qu'il m'emmènera dans des endroits encore plus intéressants à l'avenir.

Si vous êtes arrivé jusqu'ici et que vous avez aimé mon histoire, je serais sincèrement reconnaissant d'un clic sur le **bouton Recommander**. 😊