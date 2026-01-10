---
title: Donc, un chef de produit vous demande de corriger un bug…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-29T15:27:21.000Z'
originalURL: https://freecodecamp.org/news/youre-asked-to-make-a-fix-e156b802ad92
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BB7rhYkn_Nk1DRMICcC-Qw.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Donc, un chef de produit vous demande de corriger un bug…
seo_desc: 'By Anup Cowkur

  You’ve been here before.

  Your code is elegant.

  You have the just right amount of abstractions.

  Your modules are modular.

  Your system deals with the outside world through thoughtful interfaces, and has
  no direct dependencies on external...'
---

Par Anup Cowkur

Vous avez déjà été dans cette situation.

Votre code est élégant.

Vous avez juste la bonne quantité d'abstractions.

Vos modules sont modulaires.

Votre système interagit avec le monde extérieur à travers des interfaces réfléchies et n'a pas de dépendances directes aux systèmes externes.

Vos tests sont au vert. Votre rapport de couverture de code prend une minute entière à se charger. 97 % indique-t-il…

La vie est belle.

Et puis cela arrive.

Un chef de produit arrive en courant et vous dit qu'il y a un bug dans la mise à jour que vous avez livrée la semaine dernière. Chaque fois qu'un utilisateur ajoute un article à son panier, le compteur qui est censé afficher le nombre d'articles dans son panier prend quelques secondes à se mettre à jour. Il se mettait à jour instantanément avant.

Le chef de produit vous dit que les plaintes affluent de la part des utilisateurs. Il vous demande : Pouvez-vous y jeter un coup d'œil ?

Bien sûr que vous pouvez y jeter un coup d'œil. Après tout, c'est vous qui l'avez construit. C'est probablement la faute de quelqu'un d'autre. Mais vous allez le corriger. C'est juste le genre d'employé dévoué que vous êtes.

Vous récupérez le hash Git du dernier commit de la version et plongez dans le journal des modifications. Vous avez mis à jour la bibliothèque de requêtes HTTP vers la dernière version dans la dernière version. Cela était en attente depuis longtemps. Vous vous souvenez du commit exact qui l'a fait. C'était un bon jour.

Vous basculez vers ce commit, puis simulez la requête qui met à jour le panier. Heureusement que vous avez une séparation si nette des préoccupations. Vous pouvez facilement tester contre les serveurs de staging et de production avec un simple changement de flag de build.

Vous avez trouvé le coupable. Il semble que la bibliothèque HTTP que vous avez mise à jour ait une régression. Pour certains types de requêtes, elle prend un peu trop de temps pour analyser la charge utile JSON entrante. Votre application ne peut mettre à jour l'interface utilisateur du compteur du panier qu'une fois la charge utile de la requête analysée. L'infrastructure n'est pas encore configurée pour gérer la cohérence éventuelle et l'ajouter serait un projet en soi. Vous ne pouvez pas simplement mettre à jour le compteur localement et synchroniser plus tard.

Vous saviez que c'était la faute de quelqu'un d'autre. C'est la vie.

Vous dites au chef de produit ce qui se passe. Il vous donne une tape dans le dos. Il savait qu'il pouvait compter sur vous. Savez-vous comment le corriger ?

Évidemment.

Vous avez considéré vos options.

Vous ne pouvez pas revenir en arrière sur les changements. Un tas de nouveau code et de corrections de bugs dépendent de la nouvelle version de la bibliothèque. Vous perdriez tout cela aussi si vous deviez tout annuler.

Simplement forker la bibliothèque et maintenir votre propre copie ne semble pas intelligent non plus. Les mainteneurs du projet original ont une énorme infrastructure de test qui testera votre correction sur des milliers d'appareils. Vous avez 3 appareils dont 2 ont des versions de système d'exploitation obsolètes. Il est préférable d'obtenir également leurs commentaires. C'est leur bibliothèque après tout et ils auront des informations sur ses entrailles que vous n'avez pas.

Donc vous allez :

* Forker la bibliothèque
* Implémenter la correction
* Envoyer une pull request au dépôt original
* Avoir un peu d'échange entre vous et les mainteneurs
* Enfin les convaincre que votre idée est la meilleure solution
* Fusionner en amont
* Attendre une version corrective de la bibliothèque
* Mettre à jour la bibliothèque dans votre code
* Pousser une nouvelle version

Facile comme bonjour.

« Super », dit le chef de produit. « Combien de temps pensez-vous que cela prendra ? »

Vous connaissez la réponse. Les gens disent que les ingénieurs ne peuvent pas estimer. Vous n'êtes pas l'un de ces ingénieurs.

« 2 semaines », dites-vous sans cligner des yeux. « Cela dépend de la rapidité avec laquelle la PR est acceptée et les mainteneurs publient une nouvelle version. »

La couleur quitte le visage du chef de produit. « 2 semaines ? 2 semaines ?! » Il continue de répéter la phrase comme si cela allait changer quelque chose. Mais vous restez calme. Les chefs de produit sont connus pour s'énerver. Rien à craindre.

« Nos utilisateurs nous quittent ! Ils n'achètent rien parce qu'ils ne voient pas leurs paniers se mettre à jour ! Nous sommes une entreprise de commerce électronique ! C'est inacceptable ! »

Vous le regardez passer par les 5 étapes du deuil. Vous attendez que l'acceptation arrive à tout moment. Cela ne vient pas. Il semble coincé en mode négociation.

« N'y a-t-il aucun moyen de le corriger plus rapidement ? Quelque chose de temporaire ? Allez ! C'est important ! »

« Bon, d'accord », dites-vous en vous enfonçant dans votre chaise pivotante. « Laissez-moi voir. »

Vous allez l'humourer un peu. Peut-être qu'ensuite il vous laissera tranquille. Vous avez d'autres choses à faire, vous savez.

Vous plongez à nouveau dans le source. Vous êtes dans votre élément. Vos doigts naviguent dans les raccourcis de l'IDE comme Poséidon lui-même chevauchant les vagues de l'océan.

Aha ! Vous l'avez trouvé. Il y a un moyen non documenté de s'accrocher au code d'analyse JSON et de le remplacer par votre propre implémentation !

Mais attendez. Cela semble moche. C'est une API non publique. Possiblement une erreur de l'exposer comme cela. Vous ne voulez pas dépendre de cela. Et s'ils la suppriment dans la prochaine version ? Vous devrez tout refaire. Qui veut faire cela ? C'est plus rapide que de maintenir votre propre fork non testé de la bibliothèque. Mais c'est toujours moche.

Non.

Vous ne laisserez pas des décisions commerciales malavisées ruiner votre temple de pureté. Vous êtes le gardien de tout ce qui est sacré contre les masses ignorantes. C'est pour cela qu'ils vous paient grassement. C'est votre devoir de refuser.

Vous faites irruption dans le bureau du chef de produit. « La réponse est non. Il n'y a pas de moyen propre de le faire, et je ne crois pas aux solutions de contournement moches. Je suis désolé. »

Il réagit comme prévu.

« Vous me dites qu'il y a un moyen de le faire, mais vous ne le ferez pas parce que ce n'est pas _propre_ ? Nos utilisateurs nous crient littéralement dessus et menacent de passer à notre concurrent, et vous ne le corrigerez pas parce que ce n'est pas _propre_ ?! »

Vous perdez votre sang-froid.

Que sait ce type de l'ingénierie ? Vous avez construit des mondes fantastiques à partir de simples bits. Des systèmes hautement scalables qui peuvent résister aux attaques DDoS de tous les black hats que l'ancien bloc soviétique peut vous lancer. Vous êtes un artiste et le silicium est votre toile. Vous avez lu _Clean Code_ tellement de fois que vous le connaissez mieux que votre propre mot de passe GitHub.

« Oui ! » criez-vous. « Je ne souillerai pas notre base de code avec cette merde ! J'ai passé des mois à construire cette chose ! Chaque ligne de code est le produit de ma sueur et de mon sang ! La seule raison pour laquelle quoi que ce soit fonctionne du tout, ce n'est pas grâce à vous — c'est malgré vous ! Ce sont des gens comme moi qui maintiennent ce logiciel en marche, et ce sont des gens comme moi qui devront nettoyer ce gâchis longtemps après que vous et vos "fonctionnalités commerciales" serez partis ! »

Vous sortez de là en trombe. Vous avez besoin d'un verre. Des gens comme lui sont le fléau de notre industrie. Ils pensent que leurs MBA fantaisistes leur donnent un aperçu de la construction de grands logiciels que nous, développeurs, avons d'une manière ou d'une autre négligé. Qu'ils aillent tous se faire voir.

Vous vous dirigez vers la cafétéria. Celle où vous obtenez des repas gastronomiques tous les jours. Et du café. Du café illimité, délicieux et nourrissant pour l'âme. Vous méritez cela parce que vous êtes un _travailleur du savoir_.

Vous prenez une tasse de java et cherchez un endroit pour vous asseoir.

C'est alors que vous le remarquez.

L'ingénieur le plus senior de votre entreprise.

Ce type est un ingénieur pur et dur, du genre je-peux-écrire-un-compilateur-sur-ma-pause-toilette. Il était un hacker avant qu'il y ait des hackers. Vous voulez être ce type. Il est un peu comme Gandalf. Respecté et craint par tout le monde en même temps. Mais il est gentil et aide toujours les enfants. Il aimerait entendre comment vous avez remis ce chef de produit à sa place. Après tout, il est l'un des vôtres.

Alors vous vous asseyez à côté de lui. Il sirote son café et lit quelque chose sur les types de données abstraits en Haskell.

Oui. Juste la personne à qui parler.

Vous lui racontez votre grande histoire. Il écoute patiemment. Il hoche la tête et pose des questions à plusieurs reprises. Son langage corporel est détendu. Il a déjà été dans cette situation. Vous pouvez le voir dans ses yeux.

Vous avez enfin terminé.

C'était épuisant.

Vos épaules se sentent plus légères.

Il semble profondément pensé, comme s'il choisissait ses mots avec soin.

Vous attendez le grand rire. Il s'exclamera « C'est mon garçon ! » et ensuite vous prendrez un autre café ensemble. Il vous régalera avec une histoire d'une similaire remise à sa place qu'il a infligée à un chef de produit ignorant à l'époque.

Vous avez rêvé de ce jour. Vous frapperez vos tasses de café ensemble comme le font les hommes après avoir remporté la victoire au combat. Au moins, c'est ce qu'ils font dans les films. Bien sûr, c'est généralement de l'ale, pas du café.

C'est le sentiment qui compte.

Vous attendez…

Et vous attendez encore…

Il vous regarde droit dans les yeux. Ils percent votre âme. Toutes ces années de lutte avec les machines ont rendu son regard dur. Mais il exerce un pouvoir envoûtant. Vous ne pouvez pas détourner le regard.

Il ne dit qu'une seule chose.

« Notre travail n'est pas de boire du café et de pondre du code. Notre travail est de faire des logiciels qui fonctionnent. »

Puis il s'éloigne.

Vous prenez une minute. Il y a une sensation dans le creux de votre estomac. Une sensation vide et détestable. Vous commencez à reconnaître cette sensation. Vous ressentez de la honte.

Vous avez déçu les personnes à qui vous devez le plus. Vos clients.

Alors vous retournez à votre bureau. Vous tapez la solution de contournement, puis vous publiez une nouvelle version.

Vous présentez vos excuses au chef de produit. Les choses ont un peu dérapé. Il dit que c'est bon. Tout est bien qui finit bien.

Vous fork également la bibliothèque, implémentez la correction appropriée et envoyez une PR en amont. Lorsque la nouvelle version de la bibliothèque sortira avec la solution appropriée, [vous pourrez toujours refactoriser](https://medium.com/@anupcowkur/leave-it-a-little-better-than-you-found-it-isnt-good-enough-652d4be673cb#.taxjttayy).

*Si cela vous a plu, cliquez sur le ? ci-dessous. Je remarque chacun d'eux et je suis reconnaissant pour chacun d'eux.*

*Pour plus de réflexions sur la programmation, suivez-moi afin d'être informé lorsque j'écris de nouveaux articles.*