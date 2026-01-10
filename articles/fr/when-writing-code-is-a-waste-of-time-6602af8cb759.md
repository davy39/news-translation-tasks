---
title: Quand écrire du code est une perte de temps.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T10:37:34.000Z'
originalURL: https://freecodecamp.org/news/when-writing-code-is-a-waste-of-time-6602af8cb759
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EX0zEmU2JgcNjGoIeHEnIQ.jpeg
tags:
- name: open source
  slug: open-source
- name: Product Management
  slug: product-management
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Quand écrire du code est une perte de temps.
seo_desc: 'By Jonathan Solórzano-Hamilton

  Knowing what not to build is the most crucial part of modern software development.

  One of the most prominent mistakes made by development teams is doing too much work.

  Last time you were in crunch mode on a project, did...'
---

Par Jonathan Solórzano-Hamilton

#### Savoir ce qu'il ne faut pas construire est la partie la plus cruciale du développement logiciel moderne.

L'une des erreurs les plus courantes commises par les équipes de développement est de faire trop de travail.

La dernière fois que vous étiez en mode rush sur un projet, avez-vous pensé « cela se passe bien » ? Le rush est la pénitence que nous payons pour les mauvaises décisions prises plus tôt dans le projet. En particulier, la décision de faire trop de travail.

J'ai passé de nombreuses années à concevoir et à développer des logiciels d'entreprise. J'ai fait mes armes avec un stage chez HP et [survécu à un passage éprouvant dans une start-up en implosion](https://blog.usejournal.com/the-4-red-flags-i-missed-as-the-startup-imploded-around-me-be120dc390cb) avant de passer à une carrière plus stable. J'ai passé plusieurs années à travailler à l'Université de Stanford et je suis depuis devenu le Directeur Adjoint de l'Architecture à UCLA Research Information Systems.

Dans ce rôle, je dirige les efforts de développement de logiciels d'entreprise, en particulier la mise en œuvre de micro-services, pour soutenir les processus d'administration de la recherche. J'ai appris beaucoup, à travers l'école des coups durs, sur ce qui ne **fonctionne pas** dans un processus de développement logiciel collaboratif.

#### Éviter le travail m'a sauvé la mise

Il y a des années, je me suis retrouvé [à diriger une réécriture de 6 mois d'un projet de 5 ans](https://medium.freecodecamp.org/we-fired-our-top-talent-best-decision-we-ever-made-4c0a99728fde). À la fin des six mois, nous aurions soit une sortie réussie, soit l'occasion de mettre à jour nos CV.

Nous avions deux options : travailler dix fois plus vite que l'équipe précédente — qui travaillait déjà 70+ heures par semaine — ou éviter la plupart du travail. Nous avons évité la plupart du travail.

![Image](https://cdn-media-1.freecodecamp.org/images/YhEt22lS0VPShY5fmOskxkyeR5FQZKuj4gG8)
_Bacon. (Photo par [Unsplash](https://unsplash.com/photos/It0bkN5ClD8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Andrew Ridley</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

Nous avons réussi cela en limitant agressivement la portée. Le client, cependant, ne tolérerait qu'une réduction de fonctionnalités limitée. Ils avaient attendu cinq ans et n'allaient pas accepter un squelette de produit.

Le reste de la restriction de portée est venu de l'intérieur. L'équipe a restructuré l'architecture du produit pour réutiliser des packages tiers partout où nous le pouvions. Le logger sur mesure a été abandonné. Le framework d'arbres d'expressions personnalisé a disparu. Adieu, le mapper objet-relationnel maison. Bonjour, le logiciel libre open-source.

Je n'ai pas eu à mettre à jour mon CV.

#### Tracer la voie garantit que vous trouverez tous les pièges

Commençons par le problème le plus grave d'une approche complète de bricolage pour le développement d'applications : la sécurité. La définition littérale d'un piège est une fosse qui est couverte pour piéger les imprudents.

La route vers des applications sécurisées est parsemée de pièges.

![Image](https://cdn-media-1.freecodecamp.org/images/TMsBjMFpOfXnbIjKvHZ4mE9VBMOBQ-J8rAh5)
_Ici se trouvent des dragons. (Photo par [Unsplash](https://unsplash.com/photos/7FLh300YONc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Orlova Maria</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

Les hackers jouent à un jeu de chat et de souris avec les développeurs d'applications depuis l'aube de la discipline. Ils sont devenus très, très bons pour craquer les sauvegardes de sécurité. Ils ont construit un arsenal entier de méthodes, de techniques et de vulnérabilités à exploiter. Voulez-vous les combattre en partant de zéro ?

Il est **possible** que vous anticipiez chaque exploit qu'un attaquant pourrait utiliser contre votre application. Il est **possible** que vous suiviez les derniers développements et assuriez que votre sécurité frontale personnalisée soit à la hauteur. Il est **beaucoup plus probable** qu'un jour vous manquiez un trou et que votre patron apparaisse pour poser une boîte en carton vide sur votre bureau.

#### Vous allez perdre du temps

En mettant de côté les préoccupations de sécurité des applications, vous ne voulez pas non plus perdre de temps. Reconstruire des fonctionnalités courantes déjà supportées par des packages publics populaires est une perte de temps complète. Si vous ne pouvez pas étendre ces packages, vous devriez au moins les fork.

Mais attendez, vous pourriez penser. Ce sera un exercice utile pour moi d'apprendre à construire cette fonctionnalité. Apprendre n'est pas une perte de temps !

Cela n'est que partiellement vrai. Oui, apprendre sur le tas n'est pas une perte de **votre** temps. Soumettre l'équipe plus large à votre implémentation « d'apprentissage » à moitié cuite et sous-par d'une fonctionnalité commune est une énorme perte de **temps de vos collègues**.

Il est utile d'investir dans votre propre apprentissage. Passez du temps sur [freeCodeCamp](https://www.freecodecamp.org/) pour développer vos compétences dans un environnement à faible risque. D'autres écoles en ligne et [extensions universitaires](https://bootcamp.uclaextension.edu/coding/) offrent également des cursus de codage.

Peut-être n'avez-vous du temps que pour apprendre sur le tas. Vous pourriez sentir que vous devez utiliser vos contributions à l'équipe comme un exercice d'apprentissage indépendant. Si c'est le cas, abstrayez au moins votre tentative derrière une [interface](https://guide.freecodecamp.org/java/interfaces) pour faciliter son remplacement ultérieur.

#### Autres avantages de la consommation ostentatoire

Consommer un package gratuit (ou autre tiers) offre de nombreux avantages immédiats. Cela porte également ses fruits à long terme.

![Image](https://cdn-media-1.freecodecamp.org/images/cK6XUH9wRLhG5D1vkUQw-Rula7yuVCgrHtwx)
_Packages gratuits. (Photo par [Unsplash](https://unsplash.com/photos/PGrp_5aJLC0?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">NeONBRAND</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

Premièrement, vous aurez accès à plus de fonctionnalités rapidement. Un package qui résout votre problème immédiat abordera probablement également des problèmes courants et connexes. Les mainteneurs ont probablement rencontré des problèmes similaires et ont étendu les fonctionnalités du package. Vous pouvez même vous inspirer de ces fonctionnalités « supplémentaires » pour des idées sur la direction à donner à votre produit.

Deuxièmement, vous vous inscrivez pour des améliorations et de nouvelles fonctionnalités automatiques à leur sortie. Les packages publics évoluent rarement : leurs développeurs rencontrent des besoins supplémentaires, leur communauté grandit, leurs utilisateurs doivent mettre à niveau les frameworks de base. Tous ces facteurs motivent la mise en œuvre de nouvelles fonctionnalités. Ils motivent également la sortie de mises à jour qui garantissent que le code reste compatible avec la dernière version du langage ou du framework sous-jacent.

Troisièmement, si c'est un package open-source, vous avez l'opportunité de redonner à la communauté. Devenez l'un des mainteneurs. Vous aurez votre mot à dire sur la direction du package. D'autres mainteneurs pourraient adopter vos extensions comme fonctionnalités principales dans la base de code. En bonus, vous gagnerez en visibilité personnelle en tant que développeur, et vous aurez également l'opportunité d'améliorer vos compétences en apprenant de vos pairs.

Vous accumulerez également beaucoup moins de [dette technique](https://guide.freecodecamp.org/agile/technical-debt/). Même le meilleur code entraîne certains frais de maintenance, qui grignoteront la productivité future de votre équipe. Réduire la quantité de code que vous écrivez aujourd'hui augmentera le nombre de fonctionnalités que vous pourrez publier demain.

#### Alors, quand faut-il le construire soi-même ?

Étant donné les avantages déjà énumérés et les risques atténués, il pourrait sembler que coder est toujours une perte de temps. De nombreuses fonctionnalités d'application sont déjà disponibles dans des packages tiers. Alors, que reste-t-il au développeur à faire ? Les assembler ?

Vous pouvez assurément créer un produit minimum viable en assemblant des packages pré-construits. Il a toujours besoin d'au moins une fonctionnalité de différenciation pour être viable. Si cet élément est suffisamment convaincant, il ouvrira la voie pour que vous itériez vers la grandeur.

![Image](https://cdn-media-1.freecodecamp.org/images/zbwe98TiVWFnA2nIy6318Ntc3xyP4G4DVKpo)
_Je suppose que ce gars n'a probablement pas fabriqué toute cette armature. (Photo par [Unsplash](https://unsplash.com/photos/4zwozQxDbD4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Guilherme Cunha</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

J'ai déjà [écrit sur Tesla](https://medium.freecodecamp.org/how-to-run-a-successful-development-process-even-if-youre-not-technical-185d0558c89a) dans mon article sur le développement durable, mais c'est une bonne analogie. Le premier véhicule Tesla était une voiture électrique complètement pré-construite. Tesla n'a fourni que leur nouvelle batterie lithium-ion disruptive. La deuxième itération a fusionné la transmission électrique et la batterie Tesla sur mesure de cette voiture dans une voiture de sport de production respectée.

Maintenant, Tesla a itéré vers des SUV cinq portes et des véhicules grand public. Ils différencient leurs produits actuels via des portes à ouverture verticale et une capacité de conduite autonome.

Avec chaque itération de produit, Tesla a élargi la portée de leur différenciation. Ils ont identifié ce que leurs clients voulaient ensuite et ont étendu leur développement pour maintenir leur avantage.

Trouvez votre différenciation essentielle et construisez-la. Créez-la avec tout l'amour et le soin possibles. Le reste du produit peut recycler ce qui existe déjà jusqu'à ce que vous ayez suffisamment grandi pour élargir votre proposition de valeur.

#### Parcourir les packages

Vous avez identifié le produit que vous avez l'intention de construire. Vous avez décrit ses fonctionnalités et défini la portée minimum viable. Vous avez identifié les différenciateurs, donc le reste dépend des packages.

Comment trouver et identifier les packages à utiliser ?

Tout d'abord, vous aurez besoin d'une source. [GitHub](https://github.com/) est une destination populaire pour les logiciels libres open-source. [Stack Overflow](https://stackoverflow.com/) compte de nombreux fils de suggestion, et vous pouvez demander conseil à la communauté. Ce sont également des communautés précieuses à rejoindre, car elles construiront votre profil public en tant que développeur.

Il existe également des dépôts de packages spécifiques à chaque langage, notamment [NPM](https://www.npmjs.com/) pour JavaScript, [RubyGems.org](https://rubygems.org/) pour Ruby et Rails, et [NuGet.org](https://www.nuget.org/) pour le développement .NET.

En parcourant la source, vous devrez identifier les packages viables pour votre produit. Le premier indicateur que j'examine est la fraîcheur continue. Quand a eu lieu la dernière mise à jour ? Combien de personnes aident à maintenir le dépôt ? Combien d'entre eux sont actifs ?

![Image](https://cdn-media-1.freecodecamp.org/images/USnWkVVtN-bdgL2B3k12B7iCW1REEwUg7JpE)
_Mmmm. Des packages frais. (Photo par [Unsplash](https://unsplash.com/photos/vnNFWKY7Tj4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jakub Kapusnak</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

Ensuite, vous devez vous assurer que la licence est compatible avec votre produit. Certaines licences peuvent imposer des obligations supplémentaires en tant qu'utilisateur du package. La licence MIT et la licence Apache 2.0 sont généralement des choix sûrs. Elles imposent peu d'engagements (mais vous devez toujours vous conformer à la licence, aussi minimale soit-elle).

Il y a d'autres considérations pour sélectionner le bon package. Est-il officiellement supporté par une entreprise, en particulier une grande entreprise ? Ceux-ci ont un risque plus faible de tomber en désuétude. [Bootstrap](https://getbootstrap.com/) (par Twitter) et [React](https://reactjs.org/) (par Facebook) sont de bons exemples.

Est-il de la bonne taille pour votre projet ? Certains packages sont grands et encombrants. Il peut prendre plus de temps pour apprendre et implémenter le package que pour construire une petite solution personnalisée.

Combien d'utilisateurs l'ont téléchargé au total, et combien récemment ? Ces métriques donnent des indices sur les packages que la communauté soutient, et ceux qui pourraient être en voie de disparition.

Votre langage ou plateforme de choix est-il en plein milieu d'un déploiement de version majeure ? Vérifiez et voyez comment le dépôt se comporte. Les mainteneurs ont-ils déjà commencé l'intégration à la nouvelle version ? Ont-ils rencontré des obstacles ? Comment se présente le support pour la prochaine version par rapport à la version actuelle ?

Choisir le bon package est un exercice d'analyse des risques. Vous devez effectuer une diligence raisonnable pour vous assurer que le package sera capable de supporter votre produit suffisamment longtemps.

#### Alors, que signifie cela pour vous ?

Soyez humble. Gardez votre équipe humble aussi. Vous n'êtes pas les meilleurs développeurs jamais nés. Vous n'avez pas le temps de refaire le monde entier à votre image et de rester compétitif. Même si vous le pouviez, vous gaspillez un avantage compétitif à moins de réinventer avec un but.

Utilisez des packages qui existent déjà. Redonnez à la communauté si vous le pouvez en devenant un mainteneur.

Concentrez vos efforts sur le changement que vous voulez apporter à votre marché. Créez quelque chose de vraiment nouveau. Cela en vaudra toujours la peine.

J'ai récemment eu une [conversation sur ce sujet](http://www.developingup.com/28) avec Michael Miles sur son excellent podcast, Developing Up. Cliquez sur le lien pour écouter !

Merci de ❤️ si vous avez aimé cet article !