---
title: Comment j'ai construit ma première application mobile multiplateforme en utilisant
  JavaScript et XDK
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-29T02:40:06.000Z'
originalURL: https://freecodecamp.org/news/intel-xdk-or-how-i-finally-built-my-first-multi-platform-app-bc4ca181cbb5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JPG9MEIETXS4prNXFzxifw.png
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: mobile
  slug: mobile
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit ma première application mobile multiplateforme en
  utilisant JavaScript et XDK
seo_desc: 'By Rob Welan

  I have to admit up-front: I have a over a decade of experience developing applications.

  I’ve written applications largely for enterprise businesses. This meant that I used
  commercial software programs and proprietary programming language...'
---

Par Rob Welan

Je dois admettre d'emblée : j'ai plus d'une décennie d'expérience dans le développement d'applications.

J'ai principalement écrit des applications pour des entreprises. Cela signifiait que j'utilisais des logiciels commerciaux et des langages de programmation propriétaires — principalement dictés par la politique de l'organisation pour laquelle je développis, ou pour laquelle je travaillais, ou les deux.

Entre-temps, les langages open source ont évolué. Et, bien que j'avais quelques notions de JavaScript, CSS et HTML, mes compétences dans ces domaines n'étaient pas suffisantes pour migrer directement vers un emploi en développement web. Ce que j'ai récemment choisi comme option de carrière parce que :

* quelqu'un a caché mon fromage, donc la reconversion est devenue nécessaire
* il y a beaucoup de gens qui veulent des sites web et des trucs comme ça
* il y a cette promesse de développement d'applications multiplateformes pour les appareils intelligents

Alors, j'ai commencé à me reconvertir. J'ai choisi [Free Code Camp](http://www.freecodecamp.com), ou, finalement, c'est lui qui m'a choisi. Je ne suis honnêtement pas sûr. Le "comment" je me suis lancé dans les eaux de Free Code Camp n'est pas important pour cette histoire. C'est cependant une information de fond importante.

L'autre élément important de cette histoire est cette promesse de développement d'applications multiplateformes.

J'ai essayé pendant deux ans, ou peut-être plus, de trouver un outil décent qui tienne la promesse du développement d'applications multiplateformes. Je suis sûr que si je m'étais accroché à certains des outils que j'ai essayés dans le passé, peut-être que quelque chose d'utile en serait sorti.

Mais, voici le hic : je suis très pressé. Je n'ai pas le temps d'apprendre. J'ai vraiment besoin d'un outil de développement qui fonctionne directement, avec un effort minimal. Je suppose que je suis habitué aux produits commerciaux à cet égard.

Retour à Free Code Camp. Tout ce que je vais dire, c'est que j'ai atteint les Ziplines. Et je les ai terminées. Je suis aussi un peu déficitaire de l'attention. Une fois que j'avais terminé les Ziplines, j'ai réalisé que : "Waouh, je peux maintenant construire des applications basées sur le web". J'étais maintenant compétent dans les langages open source : les langages de balisage et de script comme HTML, CSS et JavaScript. Et j'avais besoin d'une pause avec l'école à ce stade.

Alors, j'ai regardé autour de moi pour des outils qui pourraient tenir la promesse du développement d'applications multiplateformes. Et, après quelques essais, j'ai renoué avec Intel XDK (oui, je l'avais installé sur ma machine depuis environ 6 mois, sans l'utiliser). Pour être honnête, mes compétences en script étaient quelque peu manquantes lorsque je l'ai installé il y a longtemps (malgré ma compréhension approfondie de VBA, de la programmation orientée objet et de l'intégration de bases de données relationnelles).

Intel XDK s'était également beaucoup amélioré, et avant de construire ma première application avec lui, j'ai mis à niveau vers la version alors actuelle.

Alors, pourquoi ai-je choisi Intel XDK plutôt que ses concurrents. Au fil des ans, j'ai testé et jeté environ une dizaine d'outils différents. Voici un résumé de mes expériences :

* Un produit concurrent ne permettait pas à l'utilisateur final (moi) de modifier ma propre application. Je pouvais commencer à en construire une, mais il n'y avait aucun moyen connu de la modifier. Ce n'est pas un problème auquel on s'attend — jamais. Vous savez, après une pause, comme, je ne sais pas, éteindre mon ordinateur pour pouvoir aller dormir, puis revenir le lendemain pour continuer à construire mon application — mais aucun moyen d'accéder à mon travail sur ma machine ? Devinez combien de temps cet outil de développement est resté sur ma machine... Oui, j'ai cherché de l'aide. Les réponses que j'ai trouvées m'ont déçu encore plus que de ne pas pouvoir modifier mon propre code. Grrr...
* Documentation : J'ai essayé un autre outil où la documentation datait de 12 mois environ (selon la date de publication). Entre-temps, Cordova avait évolué à des années-lumière de là où cette documentation obsolète était restée. Et, comme tant de choses couvertes de poussière, les instructions sur la façon d'utiliser cet outil particulier auquel je pense n'étaient vraiment pas pertinentes ou utiles. À la poubelle il est allé.
* D'autres outils basés sur serveur me rendent nerveux. Que se passe-t-il si le serveur tombe en panne ou si l'organisation responsable fait faillite ? Comment récupérer mon code ? Je n'aime pas autant de risque. Le monde tourne trop vite. Les choses tombent tout le temps. Je n'ai pas besoin que ma propriété intellectuelle soit jetée hors du monde à cause d'un mauvais choix d'hôtes d'application de ma part. Et les solutions basées uniquement sur serveur tendent à coûter beaucoup plus que je ne peux me permettre. Et qui possède vraiment la propriété intellectuelle lorsque le code que j'écris est hébergé sur la machine de quelqu'un d'autre ?

### Plus sur Intel XDK

Lorsque j'ai joué avec cette version d'Intel XDK, j'ai découvert, agréablement, que je pouvais faire fonctionner mon application. Dès la première fois. Et ce n'est pas une application simple — elle utilise la géolocalisation pour rechercher des trucs. Et d'autres choses astucieuses. Je savais à l'avance que j'aurais besoin de certains plugins. Jouer avec PhoneGap plus tôt dans la pièce m'a introduit à Cordova (PhoneGap était gratuit, maintenant propriété d'Adobe, plus si gratuit). C'était il y a des mois. Regarder Intel XDK suggérait que certaines choses pouvaient être faites par le code propriétaire d'Intel, et peut-être que certaines devraient être gérées par des plugins tiers (par Cordova par exemple).

Il s'avère, lorsque j'ai commencé, que certains du code propriétaire d'Intel était en train de devenir obsolète (mais cela n'était pas clair pour moi, l'utilisateur final, à l'époque). Le morceau de code que j'ai choisi (on.device.ready — ce n'est pas son nom complet — parce que je l'ai déjà oublié) était sur le point de disparaître.

J'adore Intel XDK — parce que ça marche — mais, comme beaucoup d'outils de nos jours, la documentation ne suit pas la fonctionnalité. Et ce n'est pas que la documentation soit nécessairement loin derrière. Dans le cas d'Intel XDK, la documentation est complète — et précise (youpi), mais, un peu difficile à trouver (oh).

Alors, oui, j'essaie d'utiliser cet appel, et mon application fonctionne plus ou moins. Et je ne me souviens pas — ai-je mis à niveau vers la prochaine version et mon application s'est cassée, ou est-ce que mon code ne fonctionnait simplement pas parfaitement et j'ai aussi mis à niveau vers la prochaine version (oui, Intel sort une mise à niveau pour Intel XDK environ une à deux fois par mois — essayez de suivre ce rythme en tant que travailleur indépendant).

En vérité, j'ai presque abandonné Intel XDK. Mais, je me suis dit : "Zut alors" (je suis Australien). Et : "J'ai presque terminé cette application. Je vais tenir bon." Et donc, j'ai trouvé quelques informations indiquant que l'appel 'on.device.ready' n'était pas encore mort, mais, sa famille d'amis était morte et enterrée (obsolète, en lettres bleues majuscules). Pas la peine de pleurer sur les êtres chers. Il est temps de changer de vitesse et d'avancer agressivement.

Alors, j'ai rapidement appris à connaître les plugins Cordova, et comment les utiliser dans Intel XDK. Pas si difficile en fin de compte. Dans ma première application, j'utilise des plugins assez bien utilisés et bien connus.

Et oui, la bonne nouvelle est que une fois que j'avais compris comment utiliser les plugins Cordova, je n'ai pas regardé en arrière.

Alors, voici quelques raccourcis pour construire une application avec Intel XDK. Mes perles de sagesse pour vous aider, le lecteur, à éviter les chemins plus sombres que j'ai pris, et rester bien dans la lumière :

* Peu importe l'application que vous essayez de développer, dites à Intel XDK de construire une version Cordova. Au cas où vous auriez besoin d'utiliser un plugin. Et, oui, vous aurez probablement besoin de StatusBar. À cause d'iOS.
* Vous aurez besoin, au minimum, de compétences en HTML et CSS. Plus un peu de JavaScript afin d'utiliser correctement les plugins. Oui, vous pouvez utiliser JQuery à la place si c'est votre truc. La quantité de JavaScript ou JQuery dépend de l'application que vous construisez. Vous devrez être capable de construire des sites web afin d'utiliser quelque chose comme Intel XDK. Vous ne savez pas encore comment construire un site web ? Voici la solution : rejoignez [Free Code Camp](http://www.freecodecamp.com), et apprenez jusqu'aux Ziplines incluses. Une fois que vous avez fait cela, vous êtes prêt à jouer avec Intel XDK. Oui, vous l'êtes.
* Pour votre première application, dites à Intel XDK de construire en utilisant l'un de leurs modèles. Cela vous donnera un peu de code prêt à l'emploi, ce qui aidera à raccourcir la partie "attendez, maintenant quoi ?".
* index.html : c'est la première interface utilisateur à laquelle l'utilisateur final éventuel de votre application (client) est présenté. Vos connaissances en développement de sites web que vous avez acquises jusqu'aux Ziplines de Free Code Camp incluses vous aideront à comprendre quoi faire avec ce fichier.
* GitHub : vous voudrez suivre les instructions pour chaque plugin que vous utilisez. Pour trouver la documentation de votre plugin, recherchez sur Google "github cordova [plugin]", où "[plugin]" est le nom du plugin que vous recherchez. Par exemple, la recherche "github cordova statusbar" devrait vous mener facilement au plugin statusbar. La documentation des plugins cordova sur github est excellente.
* StackOverflow : posez vos questions "bêtes" ici. N'oubliez pas de rechercher les réponses à votre question en premier. La vaste communauté de mentors sur StackOverflow fait un effort particulier pour souligner que votre question a déjà été posée (et répondue).
* [Forum du produit Intel XDK](https://software.intel.com/en-us/forums/app-framework) : posez vos questions "bêtes" spécifiques à Intel XDK ici. Les gars chez Intel sont vos amis (heureusement). Et les autres développeurs utilisant Intel XDK sont également heureux de vous aider s'ils le peuvent.
* Intel XDK construit trois packages lors de la construction pour les appareils Windows. Je tente toujours de comprendre pourquoi il en construit trois, mais je n'ai besoin d'en télécharger qu'un seul sur le Windows Store. Vérifiez les forums Intel XDK pour la réponse. J'ai demandé. [C'est documenté maintenant](https://software.intel.com/en-us/xdk/docs/xdk-doc-quick-links). Pas la réponse complète. Juste la réponse dont vous aurez besoin pour continuer. C'est suffisant.

### Gardez cela simple, stupide

OK, voici le conseil de base que votre mère et votre père auraient dû vous donner avant que vous ne quittiez la maison :

* créez le moins de code possible.
* cela inclut les fichiers d'actifs. Ma première application avait trop de fichiers CSS et trop de fichiers JS. Sérieusement. Le "oh, snap" que j'avais avec "on.device.ready" m'a donné l'opportunité de consolider ma propriété intellectuelle en moins de fichiers et de jeter les morceaux qui n'étaient pas réellement utilisés quelque part. C'est une question de meilleure pratique.
* Utilisez le code des autres (pas dans le sens du plagiat) — utilisez les modèles prêts à l'emploi que fournit Intel XDK pour raccourcir la courbe d'apprentissage. Au moins pour votre toute première application.
* Bloqué sur un "comment faire" ? Demandez à Google et vous trouverez la réponse sur StackOverflow. Modifiez l'apprentissage pour vos besoins, puis passez au problème suivant. Vous saurez pour la prochaine fois.
* Lisez des livres. Ha ha ha. Comme si j'avais le temps. Sérieusement. Trouvez le temps.
* Je lis toujours sur le langage de programmation Swift... Ce n'est même pas lié. Mais c'est au moins à propos du code.
* Utilisez les actifs des autres. Pour ma première application, j'ai trouvé une bibliothèque d'animations CSS, et une bibliothèque de polices sympa. J'ai fait en sorte que mon application attribue ces bibliothèques dans la page d'informations "À propos" de mon application. Selon les conditions de la licence. Et parce que c'est la bonne chose à faire.

### Utilisation d'Intel XDK pour créer votre première application

Téléchargez et installez Intel XDK.

Dans Intel XDK :

1. Cliquez sur "Démarrer un nouveau projet".
2. Choisissez "Modèles" puis "Dispositions et interfaces utilisateur".
3. Choisissez l'application Tab View (ou vous pouvez choisir un autre type de modèle si vous le souhaitez). Cochez "Utiliser App Designer" (cela installera un peu de code prêt à l'emploi pour construire et commencer — youpi).
4. Cliquez sur Continuer.
5. Dans la fenêtre du projet, cliquez sur le bouton Mettre à niveau vers Cordova.
6. Lorsque le projet est créé, ajoutez le plugin Cordova suivant (retour au menu du projet) :
Barre d'état

Les plugins que vous choisissez dépendront entièrement de ce que vous construisez. Les plugins vous aident à utiliser les fonctionnalités des appareils sur lesquels votre application s'exécutera. Il est probable que vous en aurez besoin d'au moins un. À cause d'iOS.

### Construction de votre application

À part les cerceaux de exigences sur-ingénierées d'Apple (quel certificat ai-je besoin encore ?) et le "choix de trois packages Windows", le processus de construction en lui-même est simple. Allez dans l'onglet Build. Téléchargez votre code, construisez votre package, téléchargez votre package.

Je ne sais pas pour vous. Je suis pauvre. Je peux tester mon package iOS. Je ne peux pas tester mes packages Android ou Windows. Un jour, j'espère pouvoir tester sur plus d'une plateforme. Désolé, cobayes de test (c'est-à-dire tous mes clients sur les appareils Google et Windows).

Pour vous, le développeur : l'émulateur dans Intel XDK devrait être considéré comme un guide seulement. Vous comprendrez. Avancez. Ne faites pas de prisonniers. Ce n'est pas le moment d'avoir peur de : "et si ça ne marche pas". Ayez un peu de foi. Soyez damné pour avoir essayé. Ne soyez pas damné pour avoir échoué.

Pour Android, vous voudrez construire en utilisant l'option "Crosswalk pour Android". Deux mots pour savoir pourquoi : "flex box". Si vous avez besoin d'en savoir plus, vérifiez la documentation. Flex box a une façon de s'immiscer dans chaque projet (dans mon expérience limitée).

### Que ne puis-je pas vous aider avec ?

* La façon de faire d'Apple est fortement sur-ingénierée. Vous devez créer votre propre certificat en utilisant une méthode compliquée. Tout le monde se trompe. Au moins une fois. Persévérez.
* La période de révision d'Apple est longue. Environ 7 jours (ce n'est pas une faute de frappe, cela prend des jours !). C'est une première expérience angoissante. Et si l'application est rejetée ? Saurai-je quoi faire si elle est rejetée ? Pourquoi cela prend-il si longtemps ? Est-ce que ce statut de révision signifie qu'Apple va la réviser ou que je suis censé le faire ? Aaaargh ! Est-ce prêt ? Que se passe-t-il ? Oh, et les nuits sans sommeil. Et la vérification minute par minute de l'email. Qui n'arrive jamais.
* Google prend quelques heures. La même application sera révisée et déployée dans les 24 heures. Peut-être un peu plus longtemps. Moins de 48. Cela dit, si vous écrivez une application monstrueusement compliquée, peut-être plus longtemps.
* Windows prend quelques heures. Et puis environ un jour pour devenir disponible au téléchargement dans le Windows Store. Mais, vous n'aurez aucun client. Donc c'est un point discutable. Construisez pour les téléphones Windows quand même. Cela arrondira votre CV.

### Que fais-je maintenant ?

Je construis une autre application.

*Cet article est initialement paru sur [creatureoftech.com](http://creatureoftech.com/).*