---
title: Comment être un bon propriétaire de projet open source – Le guide ultime
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-15T13:50:21.000Z'
originalURL: https://freecodecamp.org/news/ultimate-owners-guide-to-open-source
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/mark-konig-fbKMKNVJjwo-unsplash.jpeg
tags:
- name: community
  slug: community
- name: open source
  slug: open-source
- name: project management
  slug: project-management
- name: projects
  slug: projects
seo_title: Comment être un bon propriétaire de projet open source – Le guide ultime
seo_desc: "By JeB Barabanov\nHave you ever thought about having your own open source\
  \ project? I bet you have — you’re reading this article. \nMaybe you are thinking\
  \ about it right now. Maybe you came here to learn what to expect, what challenges\
  \ you’re going to f..."
---

Par JeB Barabanov

Avez-vous déjà pensé à avoir votre propre projet open source ? Je parie que oui – vous lisez cet article.

Peut-être y pensez-vous en ce moment. Peut-être êtes-vous venu ici pour apprendre à quoi vous attendre, quels défis vous allez rencontrer et comment les surmonter. Eh bien, vous êtes au bon endroit.

Le guide suivant est basé sur mon expérience personnelle en tant que **propriétaire** d'un projet open source. Et je veux bien dire propriétaire – pas seulement contributeur – d'un projet open source. Il y a une grande différence, et nous allons apprendre pourquoi.

### Alors, commençons avec... Le Guide Ultime du Propriétaire pour l'Open Source

![Image](https://www.freecodecamp.org/news/content/images/2021/03/mark-konig-fbKMKNVJjwo-unsplash-1.jpeg)

## Table des matières

* [Intro](#heading-d'abord-un-peu-sur-moi)
* [Qu'est-ce que l'Open Source](#heading-alors-qu-est-ce-que-l-open-source)
* [Pourquoi démarrer un projet Open Source](#heading-pourquoi-demarrer-un-projet-open-source)
* [Comment démarrer un projet Open Source](#heading-comment-demarrer-un-projet-open-source)
* [Comment rédiger une documentation](#heading-comment-rediger-une-documentation-pour-votre-projet-open-source)
* [Comment publiciser votre projet Open Source](#heading-comment-publiciser-votre-projet-open-source)
* [Comment gérer les problèmes et les pull requests](#heading-comment-gerer-les-problemes-et-les-pull-requests-dans-votre-projet-open-source)
* [Comment automatiser votre processus](#heading-comment-automatiser-votre-processus)
* [Gestion des versions](#heading-gestion-des-versions)

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_now0_4liLR7fJcvvnWWStQ.jpeg)

## D'abord, un peu sur moi

Je m'appelle Jeb et je maintiens quelques projets open source depuis quelques années. Le plus populaire et celui dont j'ai le plus appris est [@angular-builders](https://github.com/just-jeb/angular-builders). Au moment de l'écriture, il a ~900 étoiles sur Github et environ 1M de téléchargements mensuels.

Oui, ce n'est même pas proche des grands projets comme Angular ou React – mais je pense avoir assez d'expérience à partager avec vous pour vous aider à éviter les mêmes erreurs que j'ai faites. Et plus important encore, pour vous aider à comprendre le coût de la possession d'un projet open source.

## Alors, qu'est-ce que l'Open Source ?

Établissons d'abord un langage commun et alignons-nous sur les termes et définitions clés. 
Qu'est-ce que l'open source ? Voici une définition très générique d'une encyclopédie bien connue de l'_Open Source_ (aka Wikipedia) :

> [Open source](https://en.wikipedia.org/wiki/Open_source) est le concept d'information permettant la réplication ou la modification de quelque chose étant ouvert au public.

ou, en termes de modèles de [développement de logiciels](https://en.wikipedia.org/wiki/Open-source_model) :

> Le modèle open-source est un modèle de [développement de logiciels](https://en.wikipedia.org/wiki/Software_development) décentralisé qui encourage la [collaboration ouverte](https://en.wikipedia.org/wiki/Open_collaboration).  
>   
> Un principe principal du [développement de logiciels open-source](https://en.wikipedia.org/wiki/Open-source_software_development) est la [production par les pairs](https://en.wikipedia.org/wiki/Peer_production), avec des produits tels que le code source, les [plans](https://en.wikipedia.org/wiki/Blueprint), et la documentation librement disponibles pour le public.

Dans le cas de Wikipedia, nous avons ceux qui éditent les articles (contributeurs) et ceux qui approuvent les modifications (membres plus expérimentés, modérateurs). 

Si nous projetons cela sur le monde du logiciel, les éditeurs formeraient une équipe centrale d'un projet open source et les contributeurs seraient, eh bien, des contributeurs.

Wikipedia est un énorme projet open source mais tout a commencé par [quelque chose de petit](https://en.wikipedia.org/wiki/History_of_Wikipedia). Wikipedia est né de Nupedia et il a été créé pour une raison :

> Malgré sa liste de diffusion d'éditeurs intéressés, et la présence d'un rédacteur en chef à temps plein, [Larry Sanger](https://en.wikipedia.org/wiki/Larry_Sanger), un étudiant diplômé en [philosophie](https://en.wikipedia.org/wiki/Philosophy) engagé par Wales, la rédaction de contenu pour Nupedia était extrêmement lente, avec seulement 12 articles écrits pendant la première année.

Alors voici où la première question entre en jeu...

### Pourquoi devriez-vous vous soucier de l'Open Source ?

Comme vous pouvez l'imaginer, l'une des principales raisons d'ouvrir quelque chose à un public plus large est _de gagner des collaborateurs._

> Ensemble nous sommes forts.  
> (Zarya, 2016)

Au moment de la rédaction de cet article, Wikipedia [a](https://en.wikipedia.org/wiki/Wikipedia:Wikipedians) 37 899 499 comptes enregistrés dont 134 022 éditent activement.

Pensez-y... **134 022 collaborateurs actifs.** Oh, et il [a 6M de pages de contenu](https://en.wikipedia.org/wiki/Special:Statistics) !

Les nombres auraient-ils été les mêmes si Nupedia n'avait pas adopté un modèle open source ? J'en doute fortement.

Rien n'est différent en ce qui concerne les logiciels. Pour résoudre un certain problème, vous devez écrire du code. Pour résoudre un gros problème, vous devez écrire beaucoup de code. Et pour le résoudre correctement, vous devez écrire du code de haute qualité, faire une conception de haute qualité, et ainsi de suite. 

Tout cela nécessite des ressources_,_ que, soyons honnêtes, vous n'avez probablement pas. Vous avez un loyer à payer, après tout.

## Pourquoi démarrer un projet Open Source ?

Bien que gagner des collaborateurs soit une incitation raisonnable, presque personne ne démarre un nouveau projet open source uniquement pour cette raison. Vos raisons peuvent être différentes, mais parlons des plus populaires.

### #1 Vous voulez résoudre un problème pour lequel aucune solution gratuite n'existe

Vous êtes confronté à un problème, mais il n'y a rien qui le résout pour vous (ou il y a quelque chose, mais cela coûte de l'argent), donc vous devez le résoudre vous-même. Vous parvenez à le résoudre, vous êtes vraiment excité par votre travail, et vous pensez que d'autres peuvent en bénéficier. Alors vous ouvrez le projet en open source.

### #2 Vous voulez être un fondateur

Vous voulez être reconnu comme le fondateur d'un projet open source, et vous voulez cette ligne impressionnante dans votre CV. Vous avez un ego (nous sommes tous humains, après tout). Si c'est la _raison principale_ pour vous, alors je vous promets – après avoir lu ce guide, vous allez réfléchir à deux fois. Cela ne vaut probablement pas la peine.

### #3 Vous voulez résoudre un problème mieux que quelqu'un d'autre

Vous êtes confronté à un problème, et il existe un projet open source qui le résout pour vous, mais il n'est pas assez bon (à votre avis) ou n'a pas la fonctionnalité exacte dont vous avez besoin. 

Si vous créez un nouveau projet open source uniquement pour cette raison, alors _très probablement_ vous êtes au #2 (ego). Faites de vous un contributeur, et créez une PR pour le projet existant à la place.

Si le projet existant a une vision différente et que faire une PR n'est pas une option, vous devriez envisager soit de l'étendre en réutilisant sa fonctionnalité dans votre projet, soit de le [forker](https://help.github.com/en/github/getting-started-with-github/fork-a-repo). Cela peut vous éviter beaucoup de maux de tête plus tard.

### #4 Vous voulez résoudre un problème en créant un projet open source

Vous êtes confronté à un problème et il n'y a rien qui le résout pour vous. Alors vous pensez que commencer la solution en open source dès le début est une très bonne idée.

À mon avis, ce n'est pas le cas.

Résolvez le problème, assurez-vous qu'il fonctionne pour vous, et après cela, allez au #1.

Ce sont les quatre incitations que je rencontre le plus souvent pour les personnes créant un nouveau projet open source. Mais dans ce guide, nous allons nous concentrer principalement sur le scénario #1.

La raison est simple – je crois que si votre _raison principale_ de démarrer un projet open source est autre chose que l'envie de partager et de contribuer ce que vous avez fait, alors cela ne tiendra pas.

Pendant assez longtemps, le fait que vous aidez quelqu'un pourrait être la seule récompense que vous obtenez. Et si ce n'est pas le genre de satisfaction que vous recherchez, alors peut-être devriez-vous vous arrêter ici et ne pas perdre votre temps.

Il y a un autre scénario assez populaire qui mérite d'être mentionné : il y a des entreprises qui ouvrent une partie de leur code à la communauté. Des exemples de cela sont Angular (maintenu par Google), React (maintenu par Facebook), VSCode (maintenu par Microsoft) et plus encore.

Leurs raisons peuvent varier, mais gagner des collaborateurs et contribuer à la communauté sont certainement parmi elles.

Bien que je ne puisse pas contester l'importance de cette pratique, ce scénario est assez différent des autres parce que les employés qui maintiennent de tels projets **sont payés** pour leur travail.

Si vous travaillez dans une entreprise qui envisage la possibilité de créer un projet open source, la majorité du contenu ici sera toujours pertinent pour vous, cependant les incitations peuvent être différentes.

### Alors, devriez-vous créer un projet open source ?

Si je devais résumer cette partie en une phrase, ce serait :

> Assurez-vous que vos intentions correspondent à vos attentes.

Croire que vous voulez avoir un projet open source n'est pas la même chose que d'en avoir un, comme vous le verrez dans les chapitres suivants.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_6OX0spWqVQZxG3ue5D_EBA.jpeg)

## Comment démarrer un projet Open Source

Donc, vous êtes dans le scénario #1 – vous avez une solution pour un problème spécifique et vous êtes impatient de la partager avec le monde. Soulignons-le à nouveau :

1. Ce n'est pas une question d'ego
2. Vous n'espérez pas en tirer profit
3. Vous voulez vraiment aider les autres avec le même problème

Si vous avez répondu oui à toutes ces choses, alors voici une liste de contrôle rapide pour vous assurer que vous faites la bonne chose :

1. Assurez-vous que l'open source est le bon format. Si c'est quelque chose de petit que vous voulez partager avec le monde, alors un article de blog pourrait suffire.
2. Vérifiez bien qu'un projet similaire n'existe pas déjà. Peut-être que votre solution fait une PR parfaite pour un projet open source établi.

### Préparez-vous à ce qui va suivre

Comme je l'ai mentionné, posséder un projet open source comporte de nombreux défis.

L'un d'eux est qu'il nécessite beaucoup de votre temps. Tout ce que vous faites pour votre projet nécessite du temps, qu'il s'agisse d'écrire du code, de gérer les problèmes, de mettre à jour les dépendances, de parler aux gens, de répondre aux questions, et ainsi de suite. 

Chaque minute que vous investissez dans votre open source est une minute que vous auriez pu mais n'avez pas investie dans votre famille, votre hobby, votre santé et autres.

La seule chose que vous pouvez faire pour améliorer cela est de commencer à déléguer. Lorsque (ou devrais-je dire « si ») vous avez suffisamment de collaborateurs, vous pouvez externaliser une partie de vos responsabilités aux personnes en qui vous avez confiance.

### Séparation du code

Alors, vous avez une solution pour votre problème spécifique et vous pensez que d'autres peuvent en bénéficier. Il est encore intégré dans votre base de code et vous ne voulez probablement pas rendre toute la base de code open source (sauf si vous le souhaitez).

Tout d'abord, vous devez séparer ce code du reste de votre base de code.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/idigomnotoya-refactoring.jpg)

...ce qui signifie finalement que tout le code qui sera ouvert résidera dans un répertoire séparé.

### Rendre le code générique

Assurez-vous que le code dans le nouveau répertoire est générique et n'est pas lié à votre problème spécifique. Créez une couche d'abstraction si nécessaire.

Par exemple, j'ai commencé [angular-builders](https://github.com/just-jeb/angular-builders) avec un besoin très spécifique (venant de [l'un de mes autres projets open source](https://github.com/just-jeb/electron-angular-native)) d'ajouter un chargeur personnalisé pour les modules natifs à la construction Angular.

J'aurais pu créer _native-module-builder_ qui ne servirait que ce seul but. Cependant, j'ai réalisé qu'à un coût relativement faible, je pouvais créer une solution plus générique qui résoudrait des problèmes similaires (mais pas les mêmes !).  
  
C'est ainsi que le [custom-webpack](https://github.com/just-jeb/angular-builders/tree/master/packages/custom-webpack) builder est né.

### Gardez-le simple

Générique, c'est bien, mais attention à ne pas trop vous enthousiasmer.

L'optimisation prématurée et la sur-généralisation sont deux problèmes très connus en ingénierie logicielle. Vous devez trouver ce point idéal où votre solution résout des problèmes autres que les vôtres mais _pas tous les problèmes du monde._

Si vous construisez une échelle où la solution pour votre problème spécifique est 1 et une solution pour tous les problèmes du monde est 100, alors vous devriez commencer par 2.

_Votre code générique doit être capable de résoudre quelques problèmes de plus que votre code spécifique._

### [Mangez votre propre nourriture pour chien](https://en.wikipedia.org/wiki/Eating_your_own_dog_food)

Continuez à utiliser ce code générique dans votre base de code à chaque étape – cela garantit que vous éliminez les parties inutiles et ne gardez que ce qui est nécessaire. Cela garantit également que le code que vous allez ouvrir fonctionne correctement.

_Rappelez-vous, vous êtes le tout premier utilisateur de votre projet open source._

### Ne vous faites pas poursuivre en justice

Si vous extrayez le code de la base de code de votre entreprise, consultez vos supérieurs et, si nécessaire, le département juridique. Assurez-vous qu'ils soutiennent votre initiative et que le code que vous allez ouvrir n'est pas soumis à la PI (propriété intellectuelle) de votre entreprise. 

Cela vous aidera également à décider quelle [licence open source](https://opensource.org/licenses) est la plus adaptée à votre projet.

Lorsque tout fonctionne, que le code est séparé et suffisamment générique, et que vous avez toutes les approbations (si nécessaire), alors il est temps de l'ouvrir au monde.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_oT-ftfrBJ_BvmaZk2zumpg.jpeg)

Une fois que votre code open source est séparé et généralisé, il est temps de le déconnecter complètement de votre base de code.

### Rendez votre code public

Tout d'abord, vous devez ouvrir le code source de votre projet (après tout, c'est ce qui en fait un projet open source !).

Il existe [différentes options](https://stackify.com/source-code-repository-hosts/) pour héberger du code source en ligne, mais nous allons opter pour le choix par défaut – GitHub.

1. [Créez un nouveau dépôt](https://help.github.com/en/github/getting-started-with-github/create-a-repo) sur GitHub
2. Clonez le dépôt
3. Déplacez les sources du répertoire que vous avez précédemment créé (ne supprimez pas encore le répertoire).
4. Validez et poussez – voilà, c'est maintenant un projet open source.

_Ou est-ce le cas ?_

### Créez un package

Votre projet est disponible publiquement, mais personne ne l'utilise (y compris vous, puisque vous utilisez une copie de ce code dans votre base de code plus large). Et personne n'est conscient de son existence.

De plus, le seul format dans lequel votre projet est disponible publiquement sur le web est le _code source_. Et le seul moyen de le consommer est de copier-coller le code dans une base de code. Pas très pratique, n'est-ce pas ?

Pour distribuer correctement votre projet, vous devez :

1. Créer un package à partir du code source
2. Rendre ce package disponible sur l'un des registres de packages publics (selon votre écosystème, par exemple, pour Java, il pourrait s'agir du [Maven Central Repository](https://search.maven.org/), dans le cas de JavaScript, il pourrait s'agir du [Npm Package Registry](https://www.npmjs.com/) et ainsi de suite)

C'est à ce moment-là que vous ajoutez une chaîne de construction à votre nouveau dépôt, définissez le nom de votre projet, et plus encore.

Je ne vais pas décomposer tout le processus car il dépend fortement de votre écosystème, de l'ensemble d'outils et du langage que vous utilisez.

Vous pourriez être une personne polyvalente pour qui définir un nouveau projet ainsi qu'ajouter une chaîne de construction et publier le package est un jeu d'enfant. Si c'est le cas – tant mieux pour vous !

Vous pourriez aussi être une personne habituée à écrire uniquement du code mais qui n'a jamais été confrontée à toutes ces définitions, configurations, artefacts et autres. Cela pourrait être un tout nouveau monde pour vous.

Si vous êtes cette personne, il est temps d'apprendre. Cela ne sera pas rapide, je vous le promets, mais nous y arriverons.

### Dans tous les cas...

Lorsque vous avez terminé de remplir toutes les pièces manquantes du puzzle dans votre tête, que vous avez tout appris sur le registre de packages pertinent, et que votre package est effectivement publié, _alors et seulement alors_ pouvez-vous vraiment considérer votre projet comme open source.

_À ce stade, vous pouvez effectivement dire aux gens : « Hé, j'ai déjà une solution à votre problème, il suffit d'ajouter ce package à votre projet et de l'utiliser ! »_

### Effectuez une vérification de bon sens

Avant que votre projet ne devienne viral, assurez-vous qu'il fonctionne.

Une vérification de bon sens pour votre package serait de supprimer effectivement le répertoire générique de votre base de code plus large et d'utiliser le package disponible publiquement à la place.  
Après tout, _vous êtes le tout premier utilisateur de votre projet open source_.

### Comment gérer le développement ultérieur de votre base de code

Lorsque vous commencez à utiliser le package dans votre base de code, le flux de développement est susceptible de changer. Auparavant, le code maintenant open-source faisait partie de votre base de code – vous pouviez consommer les changements immédiatement. 

Mais maintenant, c'est autant un package externe que n'importe quel autre package tiers utilisé dans votre code.

Ainsi, lorsque vous développez une nouvelle fonctionnalité dans votre nouveau projet open source, vous devrez d'abord la publier afin de pouvoir la consommer dans votre base de code plus large. Cependant, vous ne pouvez pas la publier si vous n'êtes pas sûr qu'elle fonctionne, car une fois publiée, elle pourrait affecter d'autres utilisateurs.

Voici donc quelques choses que vous pouvez faire afin d'éviter de publier des versions défectueuses :

1. Couvrez votre code avec des tests, à la fois des tests unitaires et des tests de bout en bout.  
_Je ne pense pas avoir à vous convaincre de l'importance des tests._
2. Empaquetez et installez la nouvelle version du package localement, dans votre base de code plus large.  
_Une fois vérifié que tout fonctionne comme prévu_, _vous pouvez la publier._
3. Publiez une version bêta qui est disponible uniquement pour ceux qui la veulent explicitement plutôt que pour le monde entier.  
_Par exemple dans_ le _registre de packages npm, il existe des_ [_balises de distribution_](https://docs.npmjs.com/cli/dist-tag) _qui peuvent être utilisées à cette fin._  
_La balise par défaut est_ `_latest_` _et lorsque vous exécutez_ `_npm install mypackage_` _il exécute effectivement_ `_npm install mypackage@latest_`_. Lorsque vous publiez une nouvelle version sous une autre balise, par exemple_ `_beta_`_,_ les utilisateurs _devront explicitement installer à partir de cette balise afin d'obtenir la dernière version :_  
`_npm install mypackage@beta_` _._

### Conclusion

Contrairement à la partie précédente, qui était complètement théorique, cette partie nécessite réellement un certain travail de votre part. Selon votre expérience et vos capacités d'apprentissage, cela peut vous prendre quelques jours ou même quelques semaines pour compléter cette étape obligatoire. Et nous n'avons même pas encore commencé.

C'est pourquoi c'est mon devoir de vous demander à nouveau :

> Êtes-vous pleinement préparé à donner une quantité décente de votre temps précieux à la communauté ?

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_z5sGJuWoz02x3uSBaF4tLg.jpeg)

## Comment rédiger une documentation pour votre projet Open Source

Les deux premières parties de cet article s'adressaient à ceux qui envisagent de créer un projet open source. Je voulais leur faire savoir à quoi s'attendre et leur donner un bon départ dans le monde de l'open source.

Cette partie, ainsi que les suivantes, seront également pertinentes pour les personnes qui maintiennent déjà un projet open source et souhaitent améliorer ce qu'elles font.

### La base pour cette partie :

> Vous avez déjà un projet open source, il est disponible sur GitHub, et il peut être facilement consommé via l'un des registres de packages.

### Pourquoi avez-vous besoin d'une documentation, et que doit-elle contenir ?

> Un projet open source sans documentation est un projet mort

Il est mort parce que personne ne plongera dans votre code pour découvrir comment il doit être utilisé. Et même avant le _comment_, personne ne saura même _quoi_ votre code est censé faire.

Donc, ce sont essentiellement les deux choses que votre documentation doit contenir – _quoi_ et _comment_. Ce sont les pierres angulaires, les incontournables de la documentation.

### Comment rédiger une description de votre projet

La description est la première chose que tout le monde voit lorsqu'il entre dans un dépôt GitHub. Par conséquent, une bonne description doit répondre de manière courte et informative à la question _quoi_. Par exemple :

[React](https://github.com/facebook/react) :

> _Une bibliothèque JavaScript déclarative, efficace et flexible pour construire des interfaces utilisateur. [https://reactjs.org](https://reactjs.org/)_

[Moment.js :](https://github.com/moment/moment)

> _Analyser, valider, manipuler et afficher des dates en_ J_ava_Sc_ript. [http://momentjs.com](http://momentjs.com/)_

[Angular builders](https://github.com/just-jeb/angular-builders) (celui-ci est le mien) :

> _Extensions de façade de construction Angular (Jest et configuration webpack personnalisée)_

Vous pouvez modifier la description dans la section `À propos` de votre dépôt :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-11-at-10.20.43-1.png)

### Comment rédiger un fichier README.MD

README.MD est un fichier dans le répertoire racine de votre projet, écrit avec la [syntaxe Markdown](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax), qui contient toutes les informations dont quelqu'un a besoin pour connaître votre projet.

Le fichier README doit contenir une description détaillée (qui développe la question _quoi_) et des instructions très détaillées sur _comment_ utiliser votre projet.  
Les instructions doivent couvrir chaque partie de l'_API publique_, de préférence avec des exemples d'utilisation.

Voici quelques points pour rédiger une bonne documentation d'API :

* **Gardez-le simple** – Plus l'API et l'exemple sont simples, plus il est facile pour un utilisateur de comprendre ce qu'il fait et comment l'utiliser
* **Gardez-le structuré** – Utilisez le même modèle et la même structure visuelle pour chaque méthode d'API. De cette façon, vous définirez votre propre langage pour communiquer l'API à l'utilisateur.
* **Soyez un utilisateur** – Rédigez toujours la description de l'API du point de vue de l'utilisateur. Supposez que vous ne savez rien des détails internes et que cette documentation est tout ce que vous avez.
* **Gardez-le à jour** – Au fur et à mesure que votre projet évolue, les API peuvent changer. Assurez-vous que votre fichier README contient toujours les API et les exemples les plus récents.

Le README peut (mais n'est pas obligé de) contenir les éléments suivants :

* Lien vers un guide de contribution
* Liste des contributeurs
* Lien vers un journal des modifications
* Dernière version
* Licence
* Statut de construction
* Compteur de téléchargements
* Lien vers un chat pour un retour rapide

[Voici](https://github.com/aws-amplify/amplify-js) un exemple de ce à quoi un bon README pourrait ressembler.

### Que sont les badges ?

Les badges sont un moyen assez efficace d'exposer visuellement les informations essentielles sur votre projet, telles que : statut de construction, version, licence et divers outils utilisés par votre projet.

Il existe plusieurs options, mais je vous recommande d'utiliser les badges [shields.io](https://shields.io/).  
Ils ont un badge pour littéralement tout.

Ajouter un badge à votre fichier README est vraiment simple :

1. Allez sur [shields.io](https://shields.io/)
2. Choisissez la catégorie appropriée
3. Cliquez sur un badge que vous aimeriez ajouter à votre README
4. Remplissez les informations requises (si nécessaire)
5. Choisissez Copier Markdown dans le menu déroulant
6. Collez le markdown dans votre fichier README

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-141342.png)

Les badges sont généralement placés en haut du fichier README juste avant la description détaillée. Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_hgG8kurYMkdAsMXxji4iVg.png)

### Assurez-vous d'avoir des tests

La référence de l'API est géniale, mais rien ne vaut un vrai code utilisant vos API publiques.

L'un des meilleurs moyens de compléter votre documentation est d'avoir une bonne couverture de code avec des tests descriptifs. Parfois, les tests expliquent le code mieux que toute documentation.

### Conclusion

Dans cette partie, nous n'avons couvert que les bases de la documentation. Il y a beaucoup plus qu'un simple README ou une description, par exemple. À mesure que votre projet grandit et que des problèmes surviennent, ils deviennent une partie intégrale de la documentation.

> Cependant, avoir un fichier README qui couvre l'API publique est le minimum pour tout projet open source décent

![Image](https://www.freecodecamp.org/news/content/images/2021/03/david-menidrey-16ep3TGZR-0-unsplash.jpeg)

## Comment publiciser votre projet Open Source

Nous avons déjà discuté de ce que signifie démarrer un projet, comment le faire de manière optimale, et comment rédiger une bonne documentation pour celui-ci.

Maintenant, parlons d'attirer l'attention du public sur votre projet et de l'optimiser pour attirer et gérer correctement les contributions.

### La base pour cette partie est :

> _Vous avez déjà un projet open source, il est disponible sur GitHub, il est bien documenté et peut être facilement consommé via l'un des registres de packages._

### Comment faire connaître votre projet

Abordons l'éléphant dans la pièce : à mesure que votre projet grandit, vous ne pourrez tout simplement pas tout gérer vous-même. Vous aurez donc besoin de plus de personnes pour travailler sur le projet si vous voulez qu'il vive longtemps et prospère.

Pour impliquer plus de personnes dans votre projet, vous avez besoin de plus de personnes pour le connaître et, par-dessus tout, pour y croire.

D'après mon expérience, la meilleure façon d'exposer votre projet open source au bon public est d'utiliser l'une des ressources bien connues et de rédiger un article de blog sur votre projet.

La ressource peut être purement orientée dev (comme dev.to_)_ ou non (comme Medium).

Un point commun entre toutes ces ressources est qu'elles ont un public établi et c'est le public pertinent.

Vous pouvez également [cross-poster](https://en.wikipedia.org/wiki/Crossposting) votre article entre diverses ressources en ligne afin de couvrir un public encore plus large. Mais soyez conscient – le cross-posting a quelques inconvénients :

* Chacune de ces plateformes peut avoir un langage de balisage différent et vous devrez refaire tout le formatage
* Maintenance – si quelque chose change (et les choses _vont_ changer), vous devrez mettre à jour votre article de blog sur toutes les ressources.

Si vous optez pour Medium, je vous recommande vivement de soumettre votre article à l'une des [grandes publications](https://getgist.com/top-50-medium-publications/). Cela nécessitera un effort supplémentaire de votre part, puisque vous devrez aligner votre article avec les exigences de la publication. Mais cela garantira également que votre article est exposé à un large public et, ce qui est encore plus important, à un public _pertinent_.

Vous pouvez également décider de passer derrière un [paywall mesuré](https://help.medium.com/hc/en-us/articles/360018834314-Stories-that-are-part-of-the-metered-paywall) (vous pouvez gagner de l'argent en faisant cela !) :

> _Les histoires qui font partie du paywall sont également éligibles pour une distribution aux lecteurs de Medium via des sujets, qui alimentent les recommandations sur Medium sur notre page d'accueil, sur nos pages de sujets, dans notre Digest Quotidien et dans nos applications_

Je ne peux pas vous dire lequel est le meilleur, mais ma préférence personnelle va aux publications car cela garantit que votre article est exposé, au lieu du terme vague « éligible pour distribution ».

Si votre article de blog devient viral, il peut créer un effet de cascade et ajouter encore plus de prospects à votre projet open source. 

Par exemple, si après la publication de l'article, votre projet Github a reçu quelques dizaines d'étoiles en un jour, il peut atteindre la page [Trending](https://github.com/trending) de Github, qui est en elle-même une autre source d'exposition.

Quelques points pour rendre votre article de blog génial :

* Commencez par un énoncé de problème. Cela peut même être le titre de l'article de blog.  
_Généralement, les gens cherchent une solution à un problème spécifique et avant de décider_ d'investir _le temps de lire votre article, ils devraient avoir une idée de ce qu'ils recherchent._ [Voici un exemple](https://medium.com/angular-in-depth/customizing-angular-cli-build-an-alternative-to-ng-eject-v2-c655768b48cc) d'un article que j'ai écrit.  
_Comme vous pouvez le voir, il indique clairement le problème qu'il résout dans le titre._  
_Si vous googlez « Customizing Angular build », c'est_ l'un des premiers _résultats_ que vous obtiendrez et dès la page de recherche, vous pouvez voir quel problème il aborde._
* Décrivez pourquoi et comment exactement votre projet résout ce problème
* Fournissez un guide étape par étape détaillé, commençant par l'installation et se terminant par un exemple fonctionnel.
* Créez un projet d'exemple qui utilise votre open source et liez les sources dans l'article de blog.  
_Il y a beaucoup de développeurs qui préfèrent un exemple fonctionnel à tout article de blog._
* Obtenez des retours avant de le publier.  
_Faites en sorte que vos amis le parcourent sans leur dire de quoi il s'agit et voyez s'ils peuvent le comprendre par eux-mêmes. S'ils ne peuvent pas, alors probablement ce n'est pas très clair et vous devez élaborer._

Après avoir publié votre article de blog, assurez-vous de le partager sur les réseaux sociaux, avec vos amis, votre famille et même des inconnus dans la rue.

Cela augmentera l'exposition de votre projet – mais vous devez aussi donner envie aux gens de contribuer à votre projet.

### Comment rendre votre projet attractif pour les contributeurs

La meilleure chose est de démarrer un projet open source avec d'autres personnes. De cette façon, dès le début, vous avez une équipe avec laquelle vous pouvez partager le fardeau.

Cependant, ce n'est pas toujours le cas.

Si vous avez commencé seul, vous devez attirer des contributeurs. Et d'après mon expérience, il en existe deux types :

1. Quelqu'un qui veut avoir un impact et cherche un projet auquel contribuer (ceux-ci sont rares mais existent encore).
2. Quelqu'un qui utilise votre package et a trouvé soit un bug, soit un manque de certaines fonctionnalités.

Dans les deux cas, le simple fait de partager votre code source sur Github et d'avoir un seul article de blog sur la façon de l'utiliser ne suffit pas. Voici quelques éléments qui peuvent inciter les gens à contribuer :

#### Avoir une liste d'implémentations en attente. 

Elle peut contenir des bugs connus, des fonctionnalités planifiées, ou autre chose. Cette liste simplifiera pour les contributeurs de type #1 le choix du bon élément et l'émission d'une PR.  
Elle peut être une liste autonome ou vous pouvez (et devriez probablement) utiliser des issues et des labels sur GitHub.

#### Avoir un [guide des contributeurs](https://help.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors).

Un guide des contributeurs très basique devrait expliquer la structure du dépôt et avoir un guide étape par étape pour construire et exécuter votre projet et les tests. Le guide étendu peut contenir l'architecture, les décisions de conception, le code de conduite et plus encore.

Un bon exemple est le [guide des contributeurs d'Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md). Ne sous-estimez pas sa valeur ! C'est quelque chose qui prend un temps décent à faire lorsque le projet a grandi, et j'aurais souhaité l'avoir créé dès le début et l'avoir mis à jour progressivement au fur et à mesure que le projet évoluait.

Malheureusement, je n'avais personne pour souligner son importance, et aujourd'hui [mon projet](https://github.com/just-jeb/angular-builders) n'a pas de guide des contributeurs. C'est toujours sur ma liste de choses à faire, mais il y a toujours quelque chose de plus urgent.

#### Reconnaître vos contributeurs.

Lister vos contributeurs sur la page principale du projet leur donnera une incitation supplémentaire à faire une contribution.

Ajouter simplement des noms d'utilisateurs peut suffire, mais je recommande d'utiliser [All Contributors](https://github.com/all-contributors/all-contributors). En plus de créer une section élégante avec des images de profil et des badges pour tous vos contributeurs, il automatise l'ajout de nouveaux contributeurs en créant des PR qui ajoutent des contributeurs à cette section.

### Conclusion

Dans cette partie, nous avons discuté de plusieurs choses qui augmenteront l'exposition de votre projet et fourniront aux gens une incitation initiale à ouvrir une PR ou une issue.

> Mais cela ne les gardera pas en tant que contributeurs, ni ne garantira qu'ils termineront le travail qu'ils ont commencé.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_tyzBkDXaXjRW4UIEWBikzQ.jpeg)

## Comment gérer les problèmes et les pull requests dans votre projet Open Source

Maintenant que nous avons exploré le partage d'informations et rendu votre projet open source plus attractif, parlons des _contributions_, le saint graal de tout projet open source. 

### Qu'est-ce que les contributions open source ?

Une contribution à un projet open-source est tout changement effectué par une personne autre que le propriétaire. En pratique, cela se présente sous deux formes :

#### Problèmes

Voici ce que dit Github à propos des [problèmes](https://help.github.com/en/github/managing-your-work-on-github/about-issues) :

> _Vous pouvez collecter les retours des utilisateurs, signaler des bugs logiciels et organiser les tâches que vous souhaitez accomplir avec les problèmes dans un dépôt. Les problèmes peuvent servir à plus que simplement signaler des bugs logiciels._

En résumé, un problème est toute information nécessitant une sorte d'action.

#### Pull requests (PRs)

Voici ce que dit Github à propos des [pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) :

> _Les pull requests vous permettent d'informer les autres des changements que vous avez poussés vers une branche dans un dépôt sur GitHub. Une fois une pull request ouverte, vous pouvez discuter et examiner les changements potentiels avec les collaborateurs et ajouter des commits de suivi avant que vos changements ne soient fusionnés dans la branche de base._

En résumé, une pull request est un changement réel apporté au projet.

### Comment travailler avec les problèmes et les PRs

Alors, comment travaillez-vous réellement avec les problèmes et les PRs, et comment abordez-vous les problèmes et les PRs créés par les contributeurs ?

#### Utilisez un exemple personnel

Le meilleur conseil que je puisse vous donner est d'_utiliser un exemple personnel_ pour incorporer une certaine méthode de travail. Cela signifie que lorsque vous travaillez sur une nouvelle fonctionnalité, vous devez créer une PR pour celle-ci et la fusionner une fois qu'elle répond à toutes vos normes.

Et lorsque vous trouvez un bug ou pensez à une fonctionnalité manquante, vous devez créer un problème. 

Non seulement cette méthode organisera votre travail et apportera de l'ordre à votre projet, mais elle fournira également aux contributeurs une référence à partir de laquelle ils peuvent apprendre et adapter leurs problèmes et PRs en conséquence.

De plus, si vous avez des normes élevées (ce qui signifie que vous pensez que chaque PR doit être accompagné d'une documentation appropriée, d'une couverture de test, etc.), alors vous devez vous traiter vous-même comme n'importe quel autre contributeur. Vous ne pouvez pas exiger des autres quelque chose que vous ne faites pas vous-même. 

De plus, parfois vous devriez être encore plus indulgent envers les contributeurs qu'envers vous-même. Surtout si votre projet est à un stade précoce et n'a pas beaucoup de contributeurs. Cela nous amène au point suivant.

#### Tout travail est apprécié

Collaborer avec les autres, c'est avant tout du respect mutuel. Vous devez respecter vos contributeurs. Soyez patient lorsque vous répondez à leurs questions (même celles qui semblent simples) et soyez poli lorsque vous fournissez des _critiques constructives_. 

Rappelez-vous : il est vital d'apprécier le travail de vos contributeurs. Si quelqu'un a simplement créé un problème (même sans recherche approfondie, même sans reproduction) – remerciez-le. Ils se sont donné la peine de rapprocher leur chaise de la table, ils se sont assis bien droit et ont tapé quelque chose qu'ils pensaient pouvoir vous être bénéfique. Remerciez-les et, si nécessaire, demandez des détails supplémentaires de manière polie et respectueuse.

Si quelqu'un a créé une PR qui ne répond pas à vos normes élevées – remerciez-le. Remerciez-le et demandez poliment de faire des modifications de code/écrire des tests/ajouter de la documentation, etc. Donnez-leur un lien vers l'une de vos PRs pour référence ou fournissez-leur un lien vers le guide de contribution. 

Une conversation constructive et positive donnera à ces contributeurs une incitation supplémentaire à continuer leur travail. Ou pas...

#### Qualité contre quantité

Finalement, il y a presque toujours un compromis (sauf si vous possédez un énorme projet open source, comme Angular ou React). Vous pouvez décider que vous ne relâchez pas vos normes, pas même un peu, et très probablement vous finirez par implémenter tout le travail vous-même.

Ou, vous pouvez décider que vous abaissez les normes pour les contributeurs (mais cela rendrait vos normes futiles car elles ne sont pas appliquées).

J'ai appris que chaque contributeur nécessite une approche différente. Cela dépend vraiment de la personne et de son intérêt personnel pour sa contribution.

Vous devez prendre en compte des facteurs tels que l'urgence du problème, l'expérience du contributeur, la complexité de votre code, la complexité de la correction ou de la fonctionnalité requise, la motivation du contributeur, et plus encore. 

Habituellement, je demande poliment des changements, j'attends quelques jours, et si rien ne se passe, je fais les changements moi-même, à condition bien sûr que le problème soit suffisamment important.  
En ce qui concerne les corrections ou fonctionnalités moins importantes (agréables à avoir), je les laisse généralement entièrement à la communauté.

Avec le temps, à mesure que le nombre de problèmes et de PRs augmente, il devient une tâche ambitieuse de les suivre, de les prioriser et de les catégoriser. Cela signifie que les labels deviennent incroyablement importants.

#### Utilisez des labels utiles

Les [labels Github](https://help.github.com/en/github/managing-your-work-on-github/about-labels) sont un excellent outil pour garder vos problèmes et PRs priorisés et organisés. Bien que cela vous permette de rechercher et de filtrer par labels, ce que je trouve le plus utile ici, c'est sa capacité à aider à la visualisation de l'état général de votre projet. 

Ainsi, vous pouvez entrer dans la page « Issues » et voir que la plupart de vos problèmes sont étiquetés comme `bug` (ce qui signifie que vous devriez arrêter de pousser et vous concentrer plutôt sur leur correction.) 

Alternativement, vous pouvez voir que la plupart des problèmes sont étiquetés comme `enhancement` ou nécessitent des `features`. `priority` est un autre label utile qui vous aide à vous concentrer sur les choses significatives en premier.

De plus, vos contributeurs peuvent (et le feront) bénéficier de votre utilisation des labels. Par exemple, en revenant à **Obtenir des collaborateurs**, quelqu'un peut entrer dans la page « Issues » et identifier visuellement les problèmes qui nécessitent l'aide de la communauté (`help-wanted`, `pr-welcome`, et ainsi de suite.) 

En plus des labels à responsabilité unique (comme `bug` ou `enhancement`), je recommande d'utiliser des labels pour délimiter un problème/PR ou le placer sur une certaine échelle. Par exemple :

* `priority:low`, `priority:high`
* `required:investigation`, `required:tests`, `required:docs`
* Ou dans le cas d'un mono dépôt : `packages:package1`, `packages:package2` etc.

Voici un exemple de la page des problèmes étiquetés de mon projet :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-141634.png)

Les labels rendent assez facile de distinguer d'un coup d'œil quels sont les problèmes qui nécessitent votre attention (ou celle de vos contributeurs), à quel composant ces problèmes sont liés, et ce qui est requis pour avancer.

#### Utilisez des modèles de PR et d'Issue

Je vous recommande vivement de prendre quelques minutes de votre temps et de définir des modèles pour les [Issues](https://help.github.com/en/github/building-a-strong-community/configuring-issue-templates-for-your-repository) et les [PRs](https://help.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository).

> _Avec les modèles d'issues et de pull requests, vous pouvez personnaliser et standardiser les informations que vous souhaitez que les contributeurs incluent lorsqu'ils ouvrent des issues et des pull requests dans votre dépôt._

Cela vous fera gagner beaucoup de temps puisque vous n'aurez pas à répondre à chaque issue ou PR avec une demande d'informations ou de modifications supplémentaires. Vous devrez encore le faire parfois (parce qu'il y a des contributeurs qui ne prêtent simplement pas attention aux modèles) mais cela arrivera beaucoup moins souvent que si vous n'aviez pas créé de modèles.

Voici un exemple d'une issue par défaut que vous voyez lorsque le modèle correspondant est défini dans votre dépôt :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-141725.png)

#### Utilisez des applications et actions GitHub

Il existe plusieurs [applications et actions GitHub](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/about-actions#comparing-github-actions-to-github-apps) qui peuvent vous aider à gérer les PRs et les Issues. La liste ne cesse de s'allonger, mais je trouve personnellement celles-ci les plus utiles :

* [Stale bot](https://github.com/marketplace/stale)
* [WIP](https://github.com/marketplace/wip)
* [Autoapproval](https://github.com/dkhmelenko/autoapproval)
* [PR labeler](https://github.com/actions/labeler)

#### Assurez-vous d'être réactif 

Si j'ouvre une issue ou une PR pour un autre projet open-source et qu'il faut une éternité pour obtenir une réponse, alors je passe à autre chose. [Voici](https://github.com/greenkeeperio/monorepo-definitions/pull/24) un exemple :

* La réponse initiale a été assez rapide, prenant seulement deux jours
* La discussion a été assez fructueuse
* La PR est toujours ouverte sans mises à jour sur ce qui manque exactement/est incorrect

En conséquence, je suis passé à un autre package.

Il en sera de même pour votre projet si vous n'êtes pas réactif : si cela vous prend deux semaines pour répondre aux PRs qui vous attendent, au lieu d'attendre les changements requis par le contributeur, alors vous perdrez des utilisateurs (c'est-à-dire des contributeurs potentiels). 

Alors faites-vous une faveur – soyez réactif. Cela n'a pas besoin d'être une solution immédiate au problème de quelqu'un, mais même le fait de laisser l'utilisateur savoir que vous examinerez son problème la semaine prochaine lui donne déjà une certaine certitude et des délais.

La mauvaise nouvelle est que vous devez tenir vos promesses. Si celles-ci vous échappent de temps en temps, ne vous inquiétez pas – nous avons tous une vie personnelle et il est compréhensible que vous ayez eu des affaires urgentes qui ont reporté votre travail sur l'open-source. 

Si cela se produit, donnez une brève mise à jour – ce n'est pas grave, écrivez simplement un mot ou deux pour faire savoir aux gens que la fonctionnalité qu'ils attendaient a été reportée.

### Comment prioriser vos problèmes

Il existe plusieurs méthodes qui peuvent vous aider à prioriser vos problèmes les plus importants. 

Tout d'abord, comment quelqu'un peut-il identifier les problèmes les plus importants ? À mon avis, les problèmes les plus importants sont ceux que les utilisateurs veulent le plus, qu'il s'agisse d'une nouvelle fonctionnalité, d'une correction de bug ou autre chose. 

Parfois, un utilisateur exprimera son intérêt pour le problème, mais la plupart du temps, il ne le fera pas. Par conséquent, je vous présente une méthode assez simple pour savoir ce qui intéresse les utilisateurs :

Chaque projet sur Github a un onglet « Insights », avec une section « Traffic » :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-142214.png)

En bas de cette section, vous pouvez trouver le tableau Popular Content qui vous donne des informations sur les pages les plus consultées par vos visiteurs :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-142309.png)

Les problèmes listés dans ce tableau sont les problèmes les plus visités et donc les plus susceptibles d'être importants pour les utilisateurs.

Lorsque vous avez identifié les problèmes les plus importants, vous devez les mettre en évidence sur la page des problèmes. Voici quelques façons de le faire :

#### Épingler le problème

Vous pouvez avoir jusqu'à trois problèmes épinglés par dépôt. Les problèmes épinglés apparaissent en haut de votre page de problèmes, il est donc presque impossible de les manquer :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-142429.png)

#### Ajouter un label

Nous avons déjà parlé de l'_utilisation_ des labels, et voici un excellent exemple pour _appliquer_ les labels `help-wanted` ainsi que `priority:high`. Ces labels permettront aux contributeurs potentiels de savoir que ce problème est important et que toute aide est appréciée.

#### Intégration Continue

Avoir chaque Pull Request construite et testée avant qu'elle ne soit fusionnée dans la branche principale vous donnera une certaine confiance dans le code que vous êtes sur le point de fusionner dans votre branche principale (en fonction de la couverture des tests). 

Bien que je ne puisse pas m'empêcher de le mentionner comme faisant partie du processus de gestion des PR, il s'agit d'une _automatisation_ d'une tâche que vous devriez sinon faire vous-même, donc elle n'est pas directement liée à la gestion des PR. 

Vous pouvez toujours vérifier chaque PR, le construire localement, exécuter les tests et fusionner si tout est vert (donc l'Intégration Continue n'est pas directement liée à la gestion des PR). Ne vous inquiétez pas, nous le couvrirons en détail dans la section suivante.

### Conclusion

Il est très important de garder votre projet propre et organisé car – comme nous le savons tous – la propreté est proche de la divinité. Non seulement cela rend le processus de gestion plus efficace, mais cela améliore également l'impression générale de votre projet.

> Les PRs et les issues (ainsi que la base de code) sont des parties intégrantes de la façade de vos projets open source. Ne sous-estimez pas leur valeur.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_n8_iSirZKBjHRufT6silGw.jpeg)

## Comment automatiser votre processus

Une partie naturelle de la gestion des contributions (c'est-à-dire des issues et des PRs) est l'automatisation – probablement l'un des aspects les plus importants de la gestion de projet OSS.

### Pourquoi automatiser ?

Si j'ai appris une chose au fil des années en tant que propriétaire d'un système open-source, c'est que moins vous avez de travail de routine à faire vous-même, plus vous avez de temps libre pour le travail réel (comme corriger des bugs et développer de nouvelles fonctionnalités). Par conséquent, je cherche à **automatiser tout ce que je peux.**

Voici comment j'aimerais que nous abordions cet objectif : examinons d'abord les deux flux de travail, (le non automatisé et le entièrement automatisé) pour voir combien de votre temps est réellement consacré aux tâches de routine. Nous verrons ensuite comment nous pouvons atteindre un flux de travail amélioré conduisant à plus de temps pour corriger les bugs.

### Pire cas – pas d'automatisation

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-142749.png)

Comme vous pouvez le voir, dans un cas où rien n'est automatisé, vous faites tout le travail. C'est beaucoup de travail pour une simple correction de bug, et en plus de cela, c'est le travail que _vous_ devrez faire _chaque fois_ qu'il y a une correction de bug ou une nouvelle fonctionnalité ! 

Maintenant, regardons un scénario alternatif.

### Meilleur cas – tout est automatisé

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-142807.png)

Dans ce cas, vous ne faites que ce que vous devez faire – inspecter le code et (parfois) approuver la pull request. Tout le reste est fait automatiquement.

Science-fiction ? Non, cela s'appelle **l'intégration continue** et le **déploiement continu**. Nous n'allons pas entrer dans les détails des scripts de construction et des configurations spécifiques au système ici. Au lieu de cela, nous allons passer en revue les outils dont vous avez besoin pour le faire fonctionner et je vous laisserai décider des spécificités vous-même.

### Qu'est-ce que l'intégration continue (CI) ?

> _L'intégration continue (CI) est la pratique consistant à automatiser l'intégration des changements de code de plusieurs contributeurs dans un seul projet logiciel. Le processus CI est composé d'outils automatiques qui vérifient la justesse du nouveau code avant l'intégration._

Une exécution CI très basique inclurait **build** et **unit tests**, mais elle n'est pas limitée à ces deux éléments. Elle peut également inclure toutes sortes d'outils d'analyse statique de code, de linters, et ainsi de suite. C'est là que vous définissez vos normes.

### Pourquoi vous devriez utiliser des tests de bout en bout

Les tests de build et unitaires vous fournissent un retour rapide pour les changements de code, prennent un temps relativement court et échouent rapidement si quelque chose ne va pas. Mais les tests de bout en bout (E2E) ont une place spéciale dans la CI. 

Les tests E2E doivent couvrir non seulement la justesse du code, mais aussi votre flux de déploiement, l'intégrité du package, et ainsi de suite. 

Je m'en suis rendu compte lorsque j'ai accidentellement publié une nouvelle version d'un package qui ne contenait aucun code. La construction a réussi, les tests unitaires étaient verts ainsi que les tests E2E (ceux à l'époque étaient installés en liant le répertoire de sortie de la construction depuis le projet de test). Où a-t-il échoué ? Dans la phase d'empaquetage. 

Un point clé à retenir ici : les tests E2E doivent tester vos packages comme s'ils étaient utilisés par un utilisateur réel.

Pour y parvenir, je recommande ce qui suit :

1. Lors de votre exécution CI, démarrez un registre de packages local. Chaque langage/écosystème a quelques options, par exemple pour les projets Java ou Scala, vous avez le [Nexus Repository](https://blog.sonatype.com/using-nexus-3-as-your-repository-part-1-maven-artifacts), et pour JavaScript, il y a [Verdaccio](https://github.com/verdaccio/verdaccio) (que j'utilise dans [@angular-builders](https://github.com/just-jeb/angular-builders))
2. Ayez un projet séparé qui utilise votre package (celui-ci peut résider dans le même dépôt). Les tests de ce projet doivent tester la fonctionnalité de votre package.
3. Configurez ce projet pour utiliser le registre de packages local.
4. Après que votre package soit construit, publiez-le dans le registre de packages local (démarré dans votre système CI).
5. Installez la dernière version du package (que vous venez de publier) dans votre projet de test.
6. Exécutez les tests.

Non seulement cela testera l'intégrité et la fiabilité de votre package, mais cela vous fera également gagner du travail en matière de déploiement continu.

### Comment fonctionne un système CI

Il existe de nombreux systèmes CI qui ont un plan gratuit pour les projets open source, parmi eux [Travis CI](https://travis-ci.com/), [CircleCI](https://circleci.com/), [AppVeyor](https://www.appveyor.com/), [Github Actions](https://github.com/features/actions), et d'autres. 

Ils sont tous plus ou moins les mêmes et font essentiellement la même chose : ils extraient votre code vers une machine virtuelle, exécutent un script que vous définissez (généralement exécuter build et tests), puis signalent soit un succès, soit un échec à GitHub.

Tous ces systèmes ont une [application](https://github.com/marketplace?category=continuous-integration&type=apps) pour l'intégration avec GitHub et le flux d'intégration est assez similaire dans tous :

1. Inscrivez-vous sur la plateforme.
2. Installez l'application correspondante dans votre compte GitHub.
3. [Configurez l'accès](https://github.com/settings/installations) aux dépôts sélectionnés.
4. Créez un fichier de configuration (comme `travis.yaml`) qui définit la matrice de build, la chaîne de build requise et le script CI.
5. Poussez-le vers la branche principale

Cela fera fonctionner votre CI sur chaque PR et signalera le statut à GitHub – mais ce n'est pas suffisant. Ce que vous voulez vraiment, c'est bloquer la fusion vers la branche principale jusqu'à ce que la PR ait passé tous les contrôles.

Cela se fait en définissant les règles de protection des branches. Pour les définir, vous devez aller dans la section **« Branches »** dans les **« Paramètres »** de votre dépôt et appuyer sur le bouton **« Ajouter une règle »** :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-142547.png)

Ensuite, cochez la case **« Exiger que les vérifications de statut réussissent avant la fusion »** :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-142635.png)

Comme vous pouvez le voir, les cases à cocher des applications GitHub correspondantes apparaissent déjà ici, donc la seule chose qui reste est de les activer. 

Le script de build exact dépend vraiment de votre écosystème, du langage dans lequel votre projet est écrit, des frameworks que vous utilisez, et plus encore. Par conséquent, nous ne le couvrirons pas ici – vous devrez consulter la documentation du système CI vous-même pour obtenir des détails. Cependant, vous avez maintenant une assez bonne idée de ce qu'est la CI et de la manière dont elle automatise vos PRs, alors passons à la suite.

### Comment fonctionne le déploiement continu (CD)

> _Le déploiement continu (CD) est un processus de publication de logiciels qui utilise des tests automatisés pour valider si les modifications apportées à une base de code sont correctes et stables pour un déploiement autonome immédiat dans un environnement de production._

Dans notre cas, l'environnement de production est lorsque un package est publiquement disponible dans un registre de packages. C'est une phase de non-retour, car une fois que vous l'avez publié, vous ne pouvez pas le désactiver puisqu'il est publiquement disponible (et donc potentiellement en cours d'utilisation).

Il existe plusieurs stratégies pour le déploiement continu qui dépendent vraiment du projet et de sa complexité. Mais à mon avis, les versions doivent être faites uniquement à partir d'une branche principale car cela rend le flux de travail assez facile. Voici comment :

1. Chaque PR représente soit une correction de bug, soit une nouvelle fonctionnalité.
2. Le code est testé (y compris E2E) avant même d'atteindre la branche principale.
3. La branche principale est une branche protégée, donc tant que vous ne fusionnez pas de PRs défaillants, la branche principale reste stable.
4. Chaque fusion de PR vers une branche principale déclenche une exécution CI de la branche principale qui finit par publier une nouvelle version.

Cela garantira que toutes les versions sont séquentielles et rendra très facile l'association de certaines PRs avec des versions spécifiques.

Pour automatiser les versions de packages, nous aurons besoin de quelques éléments :

1. Avancement automatique de la version basé sur les messages de commit.
2. Mises à jour automatiques du CHANGELOG basées sur les messages de commit.
3. Publication automatique du package dans un dépôt de packages public.
4. Version automatique sur Github.

Bonne nouvelle pour tous : toutes ces fonctionnalités sont déjà prises en charge par [semantic-release](https://github.com/semantic-release/semantic-release). Mauvaise nouvelle : vous devrez investir un peu de temps pour le faire fonctionner (mais cela en vaut finalement la peine).

### Comment fonctionne Semantic-release

> _semantic-release automatise l'ensemble du flux de travail de publication de packages, y compris : la détermination du prochain numéro de version, la génération des notes de publication et la publication du package._  
>   
> _Cela supprime le lien immédiat entre les émotions humaines et les numéros de version, en suivant strictement la spécification de [Versioning Sémantique](http://semver.org/)._

Nous ne couvrirons pas ici l'ensemble du processus d'intégration, car ils ont une très bonne documentation et il n'y a pas de raison de la résumer ici. Je mentionnerai cependant quelques points :

* Assurez-vous de comprendre la spécification de [versioning sémantique](https://semver.org/) et le format des [commits conventionnels](https://www.conventionalcommits.org/en/v1.0.0/) avant de commencer avec Semantic Release.
* Pour que semantic-release fonctionne bien, vous devez imposer certains formats de messages de commit. Pour ce faire, vous pouvez exécuter [commitlint](https://github.com/conventional-changelog/commitlint) en tant que hook de pré-commit [husky](https://github.com/typicode/husky). Il imposera les commits conventionnels lorsqu'une personne crée un commit local, mais il ne peut rien faire contre les commits qui sont effectués directement depuis l'interface web de GitHub (ce qui arrive souvent lorsqu'une personne veut apporter une correction rapide à sa PR). Par conséquent, je vous recommande de le sauvegarder par [commitlint Github Action](https://github.com/marketplace/actions/commit-linter).

Après avoir configuré la version sémantique dans le cadre de votre flux de travail, vous avez pratiquement terminé et vous n'avez plus à consacrer votre temps à ces processus de routine. Bien qu'il y ait une autre optimisation que vous pouvez faire.

### Comment garder le projet à jour

Si votre projet n'a pas de dépendances externes – passez cette partie. Cependant, la plupart des projets dépendent d'autres packages, et ces packages ont tendance à changer. 

Garder votre projet à jour avec ses dépendances est important mais _c'est chronophage_. Heureusement pour nous, il existe une solution. En fait, il en existe plusieurs, comme [Greenkeeper](https://greenkeeper.io/), [Renovate](https://renovate.whitesourcesoftware.com/), et [Dependabot](https://dependabot.com/). 

L'idée est à peu près la même pour tous, donc je vais simplement citer la section « Comment cela fonctionne » de Dependabot :

> _**1. Dependabot vérifie les mises à jour**_  
> _Dependabot télécharge vos fichiers de dépendances et recherche les exigences obsolètes ou non sécurisées._

> _2._ **_Dependabot ouvre des pull requests_**  
> _Si l'une de vos dépendances est obsolète, Dependabot ouvre des pull requests individuelles pour mettre à jour chacune d'entre elles._

> _3._ **_Vous passez en revue et fusionnez_**  
> _Vous vérifiez que vos tests passent, parcourez le journal des modifications et les notes de version inclus, puis fusionnez en toute confiance._

Comme vous l'avez peut-être remarqué, cela n'a de sens que lorsque vous avez une CI fonctionnelle.

### Conclusion

Si vous avez un cycle CI/CD entièrement automatisé et qu'une nouvelle issue est ouverte dans votre dépôt OSS, vous pouvez fournir une correction de bug en quelques minutes. 

En fait, vous pouvez entrer dans la version mobile de Github depuis votre téléphone, corriger la ligne de code boguée ou les deux, et valider le code. Le reste est fait automatiquement, et vos clients reçoivent une nouvelle version immédiatement. 

J'ai moi-même pu obtenir rapidement et sans douleur une version corrigée pour mes clients à plusieurs reprises.

> _Avoir une excellente automatisation ne consiste pas à libérer_ du temps pour les loisirs, il s'agit de consacrer votre temps à des choses vraiment importantes et d'augmenter votre réactivité._

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_6k7J2Dj1iz0c901UExzjWg.jpeg)

## Gestion des versions

Pour conclure le guide, j'aimerais parler de la gestion des versions, un aspect qui devient toujours pertinent pour tout projet OSS ayant un nombre décent d'utilisateurs.  
Vous apprendrez les notations de version, les changements de rupture, les back-ports, et plus encore.

### Qu'est-ce que la versioning des logiciels ?

Voyons ce que Wikipedia a à dire sur la versioning des logiciels.

> _**La versioning des mises à jour logicielles**_ est le processus d'attribution de noms de version uniques ou de numéros de version uniques à des états uniques de [logiciels informatiques](https://en.wikipedia.org/wiki/Computer_software).  
>   
> _Les logiciels informatiques modernes sont souvent suivis en utilisant deux schémas de versioning de logiciels différents - [numéro de version interne](https://en.wikipedia.org/wiki/Software_versioning#Internal_version_numbers) qui peut être incrémenté plusieurs fois en une seule journée, comme un numéro de contrôle de révision, et une _version de publication_ qui change généralement beaucoup moins souvent, comme la versioning sémantique[[1]](https://en.wikipedia.org/wiki/Software_versioning#cite_note-semver-1) ou un [nom de code de projet](https://en.wikipedia.org/wiki/Code_name#Project_code_name)._

En effet, il existe plusieurs façons d'identifier de manière unique la version de votre produit logiciel.

La manière la plus connue est de lui donner un nom.

La grande majorité des personnes sur Terre, même celles indirectement connectées à la technologie, ont probablement entendu parler d'Android Ice Cream Sandwich et Marshmallow ou de Mac OS Leopard, de son cousin gelé Snow Leopard, et de Big Sur.

Les programmeurs ont probablement entendu parler d'Eclipse avec ses corps célestes Luna, Mars et Photon.

Tous ceux-ci sont des versions majeures de produits logiciels.

Bien que les noms soient excellents pour le marketing, ils peuvent aussi être parfois déroutants.  
En fait, Google a abandonné l'utilisation de bonbons dans les noms de version d'Android parce qu'ils :

> _Ont entendu des retours au fil des ans de la part des utilisateurs selon lesquels les noms n'étaient pas toujours intuitivement compréhensibles par tous dans la communauté mondiale_

Et à juste titre, mais peut-être que nous n'avons tout simplement pas assez évolué pour extrapoler les numéros de version à partir des espèces animales, même si Snow Leopard est beaucoup plus cool que Leopard.

Les corps célestes et les bonbons sont des concepts un peu plus faciles à saisir, mais seulement si vous les nommez par ordre alphabétique (comme le font Android et Eclipse). Mais une chose est certaine – il n'y a pas de meilleure façon de déterminer la succession que les nombres.

Ainsi, si vous nommez la première version de votre produit logiciel « Produit 1 » et la deuxième version « Produit 2 », il est assez intuitif de dire que la deuxième version est la plus récente, n'est-ce pas ?

Cependant, contrairement aux produits logiciels autonomes qui n'exposent pas d'API, les logiciels qui sont consommés par d'autres logiciels (comme la majorité des produits OSS) ont besoin d'une meilleure gestion des versions qu'une simple séquence de nombres.

Par exemple, si nous utilisions une simple séquence de nombres pour la gestion des versions, comment l'utilisateur distinguerait-il entre une correction de bug et un changement qui casse l'API existante ?

La réponse est... la gestion sémantique des versions.

### Qu'est-ce que la gestion sémantique des versions ?

La version sémantique (également connue sous le nom de SemVer) est un schéma de version largement adopté qui utilise une séquence de 3 chiffres au format suivant : `MAJOR.MINOR.PATCH`.  
Les règles sont simples – étant donné un numéro de version `MAJOR.MINOR.PATCH`, incrémentez le :

* numéro de version `MAJOR` lorsque vous apportez des modifications incompatibles à l'API
* numéro de version `MINOR` lorsque vous ajoutez des fonctionnalités de manière rétrocompatible
* numéro de version `PATCH` lorsque vous apportez des corrections de bugs rétrocompatibles.

Des étiquettes supplémentaires pour les pré-versions et les métadonnées de build sont disponibles en tant qu'extensions au format `MAJOR.MINOR.PATCH`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/versioning.png)

Il fournit un moyen clair et concis de communiquer les changements dans votre produit logiciel à vos utilisateurs.

Mais surtout, il est largement adopté par toutes sortes de gestionnaires de packages et d'outils de build (comme [NPM](https://docs.npmjs.com/about-semantic-versioning#using-semantic-versioning-to-specify-update-types-your-package-can-accept) et [Maven](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN8903)), ce qui permet aux utilisateurs de dépendre d'une **plage de versions** spécifique plutôt que d'une version spécifique.

Par exemple, spécifier la plage de versions `^2.2.1` plutôt qu'une version explicite `2.2.1` permettrait à l'utilisateur d'accepter toute correction de bug rétrocompatible ou de nouvelles fonctionnalités qui seront publiées sur la version `2.2.1`.

Cela dit, les outils de build et les gestionnaires de packages s'appuient sur un contrat entre un utilisateur et un propriétaire de package – un contrat qui est défini par SemVer.

Cela signifie que la responsabilité vous incombe – vous êtes celui qui définit ce qu'est un changement de rupture et ce qu'est un changement mineur. Vous pouvez accidentellement publier un changement de rupture en tant que correction de bug (version de patch) et cela _cassera_ les builds qui dépendent d'une plage.

Casser les builds est une chose horrible à faire, donc je vous recommande d'utiliser `semantic-release` avec un format de message prédéfini ainsi qu'un outil d'application du format des commits.

Vous pouvez trouver plus d'informations sur la gestion sémantique des versions sur le site officiel, [semver.org](https://semver.org/).

Maintenant que nous avons appris à _identifier_ les changements de rupture, parlons de les _introduire_.

### Comment gérer les changements de rupture

Les changements de rupture sont des modifications de votre API publique qui suppriment, renomment ou modifient vos contrats avec l'utilisateur de manière incompatible.

Idéalement, vous maintiendriez la compatibilité ascendante dans votre code et n'introduiriez jamais de changements de rupture. Mais ensuite, vous vous réveillez face à une réalité difficile.

Les logiciels évoluent et il en va de même pour votre code. Les besoins des utilisateurs changent et il en va de même pour votre API. Vous grandissez en tant que développeur et il en va de même pour votre produit.

Par conséquent, surtout en tant que développeur open-source qui n'est pas payé pour son travail, vous ne pouvez tout simplement pas vous permettre de maintenir tout le code hérité qui existe dans votre projet. Parfois, vous devez vous en débarrasser.

La question est comment ?

Comme toujours, c'est un compromis. Vous saurez mieux comment ce changement ou un autre impacte les utilisateurs.

Vous n'_avez_ pas à maintenir la compatibilité ascendante à tout prix, ni à implémenter toutes les nouvelles fonctionnalités dans chaque ancienne version. Mais c'est certainement quelque chose que vous _devriez_ prendre en compte.

Si le coût de migration est relativement faible pour l'utilisateur, alors il est acceptable de faire un changement de rupture et il est tout à fait raisonnable de ne pas supporter cette fonctionnalité dans les anciennes versions.

Cependant, si le coût de migration est élevé et que la grande majorité des utilisateurs ne peuvent pas se permettre cet effort, vous devriez probablement envisager de rendre ce changement rétrocompatible au début et de publier un avertissement de dépréciation.

Un avertissement de dépréciation est souvent publié en même temps qu'une nouvelle API, tandis que l'ancienne API est toujours supportée. De cette façon, les utilisateurs ont le temps de migrer. Une fois qu'ils l'ont fait, dans la prochaine version majeure, l'avertissement de dépréciation et l'ancienne API peuvent être supprimés en toute sécurité.

Dans tous les cas, lorsque vous introduisez un changement de rupture, assurez-vous d'avoir un guide de migration qui contient des instructions étape par étape pour la migration.

De plus, par courtoisie, il serait très gentil de votre part de _donner du temps aux utilisateurs_ pour se préparer à un changement de rupture, surtout s'il n'a pas de période de grâce (où les anciennes et nouvelles API sont supportées). 

Un petit avertissement qui explique le changement de rupture, la raison derrière celui-ci et le délai prévu est très utile. Cela peut être un tweet, un article de blog, ou même une nouvelle version mineure de votre produit avec un avertissement de dépréciation.

Rappelez-vous que bien qu'un changement de rupture soit essentiellement une expérience négative, un changement de rupture _soudain_ est une expérience _extrêmement_ négative.

### Migration automatique

Nous pouvons diviser les changements de rupture en deux catégories – non déterministes et déterministes.

Les changements non déterministes sont ceux dans lesquels vous ne pouvez pas prédire le résultat de l'effort de migration, par exemple lorsque vous supprimez complètement une certaine partie d'une API.

Dans ce cas, c'est à l'utilisateur de décider s'il veut la remplacer par une autre bibliothèque tierce, l'implémenter lui-même, ou la déprécier également.

Les changements déterministes sont ceux qui, étant donné le code `X` et l'entrée utilisateur `I`, vous permettent de le transformer en code `Y`. Par exemple, changer le nom d'une fonction ou une instruction d'importation.

Si vous introduisez un changement de rupture déterministe, vous pouvez écrire une automatisation qui modifiera la base de code de l'utilisateur et l'ajustera à la nouvelle API. 

Avec cette automatisation en place, vous n'aurez pas à vous soucier de la compatibilité ascendante et des guides de migration détaillés. Vous fournissez à l'utilisateur un moyen de mettre à niveau son code avec un effort nul de sa part, ce qui est crucial dans les mises à jour logicielles.

Cependant, il y a aussi un compromis inhérent ici. Écrire du code prend du temps, tout comme écrire un guide de migration. Et naturellement, écrire du code qui migre un flux de code complexe vers une nouvelle API prendra plus de temps que d'écrire du code qui remplace un nom de fonction par un nouveau.

Parfois, vous ne pouvez tout simplement pas vous permettre ce genre d'effort.

Dans le cas où vous décidez de vous lancer, il existe des outils qui peuvent vous aider à atteindre ce que vous voulez.

Le plus connu et indépendant du langage est [Codemode](https://github.com/facebook/codemod) de Facebook.

> _codemod est un outil/bibliothèque pour vous aider avec des refactorisations à grande échelle de la base de code qui peuvent être partiellement automatisées mais nécessitent encore une supervision humaine et une intervention occasionnelle._

Il existe également des outils plus sophistiqués qui utilisent [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) et peuvent être utilisés pour des tâches plus compliquées que le simple Rechercher & Remplacer.

Par exemple, une autre bibliothèque de Facebook (spécifique à JS/TS) appelée [JSCodeShift](https://github.com/facebook/jscodeshift).  
Ou [code-migrate](https://github.com/ranyitz/code-migrate) – un outil (à nouveau spécifique à JS/TS) qui vous permet d'écrire une migration guidée relativement facile et fournit à l'utilisateur des invites basées sur une belle interface en ligne de commande.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_aFlF8Vx0-thA0EutbBgiUA.png)

Certains grands projets OSS ont même une solution qui leur est propre. Un exemple de cette solution est [Angular schematics](https://angular.io/guide/schematics) – un générateur de code basé sur des modèles qui supporte une logique complexe.

La migration automatique de code peut être publiée en tant que package séparé (comme `my-cool-oss-migrate-v4-v5`) et mentionnée comme une étape dans le guide de migration. 

Alternativement, la migration peut faire partie de votre version majeure qui contient des changements de rupture et être exécutée lors de l'installation de cette version dans la base de code de l'utilisateur. Le choix vous appartient.

### Back-porting

Une autre pratique courante consiste à back-porter des changements importants aux versions précédentes. Par exemple, un bug critique a été découvert après une version majeure (avec un changement de rupture) mais il s'applique également à une version précédente.

Dans ce cas, vous ne pouvez pas vous attendre à ce que vos utilisateurs effectuent une migration fastidieuse à cause d'un seul bug. D'un autre côté, extraire l'ancienne révision, implémenter la correction par-dessus et la publier en tant que version mineure d'une ancienne version peut être fastidieux.

> _La solution : avoir une branche protégée par version majeure._

Chaque fois que vous prévoyez de publier une version majeure, vous créez une branche à partir de la branche principale nommée `c.x.x` où `c` est le numéro de version majeure actuel.  
Vous rendez toutes ces branches protégées (comme la branche principale) afin de ne pas les casser accidentellement. Ensuite, chaque fois que vous devez back-porter une fonctionnalité ou une correction de bug d'une version majeure plus récente, vous la réimplémentez sur cette branche ou (si possible) vous sélectionnez les commits de la branche principale.

De plus, une stratégie qui mérite d'être mentionnée est d'avoir une branche séparée pour la _prochaine_ version majeure également (par opposition à n'avoir que des branches pour les versions majeures précédentes).

Cela est généralement pertinent pour les grands projets (comme Webpack ou Babel) qui ont beaucoup de changements dans chaque nouvelle version majeure.

Avoir une branche séparée pour la prochaine version majeure permet de travailler dessus et de la publier pour des tests, tout en gardant la version la plus pertinente (et en travaillant dessus) dans la branche principale.

Une fois la nouvelle version majeure publiée, sa branche devient une branche principale et une nouvelle branche est créée pour la prochaine version majeure.

## Réflexions finales

J'espère que vous avez apprécié ce guide et que vous avez maintenant une assez bonne compréhension de ce que signifie posséder un projet open source. 

À la fin, j'aimerais partager avec vous une chose que vous devriez toujours garder à l'esprit en tant que propriétaire d'un projet open-source.

### Écoutez vos utilisateurs

Cela peut sembler contre-intuitif, mais c'est la vérité – vous n'êtes pas le seul à définir la feuille de route, les utilisateurs la définissent aussi. En fait, les utilisateurs définissent la majeure partie de celle-ci.  
Si vous possédez un projet open-source, c'est pour aider les autres, pas vous-même.

Ayez plusieurs canaux de feedback. Il y a des utilisateurs qui n'ont qu'une question rapide à laquelle vous pouvez répondre en une seconde. 

Il y a des contributeurs potentiels qui aimeraient discuter de la feuille de route mais ne veulent pas le faire en public. Donnez-leur un moyen de vous contacter. Fournissez un lien vers Slack ou Discord, partagez votre compte Twitter, et ainsi de suite. Plus il y a de canaux, mieux c'est.

En parlant de canaux, vous êtes toujours le bienvenu pour m'envoyer un message direct sur [Twitter](https://twitter.com/_Just_JeB_) si vous avez des questions ou des réflexions.

Vous pouvez également [lire plus d'articles comme celui-ci sur mon blog](https://www.justjeb.com/).