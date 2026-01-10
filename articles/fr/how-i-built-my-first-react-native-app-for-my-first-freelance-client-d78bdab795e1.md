---
title: Comment j'ai construit ma première application React Native pour mon premier
  client freelance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T16:43:57.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-first-react-native-app-for-my-first-freelance-client-d78bdab795e1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AIm6deWAohMF1yWEEkEoKw.jpeg
tags:
- name: Freelancing
  slug: freelancing
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
- name: technology
  slug: technology
seo_title: Comment j'ai construit ma première application React Native pour mon premier
  client freelance
seo_desc: 'By Charlie Jeppsson

  I recently launched my first native mobile app built with React Native. As it happens,
  it was also the first app I’ve built for a client as a freelancing developer. Here’s
  the bumpy ride, all the way from react-native init to app ...'
---

Par Charlie Jeppsson

_J'ai récemment lancé ma première application mobile native construite avec React Native. Comme il se trouve, c'était aussi la première application que j'ai construite pour un client en tant que développeur freelance. Voici le parcours semé d'embûches, depuis react-native init jusqu'à la publication sur l'app store._

#### Table des matières

1. Pourquoi le freelance ?
2. Pourquoi React Native ?
3. Spécifications de l'application
4. Apprendre des meilleurs
5. Environnement de développement
6. Navigation
7. Écran de démarrage
8. Gestion d'état
9. Sessions
10. Listes
11. Images
12. Temps
13. Polices et icônes personnalisées
14. CI/CD et monitoring
15. Ajout du support pour Android
16. Parce qu'Apple
17. Résumé

#### Pourquoi le freelance ?

En mai dernier, je suis tombé sur cette opportunité freelance passionnante. À l'époque, je travaillais comme développeur web full stack pour une startup basée à Stockholm. C'était mon premier emploi en tant que développeur, et je l'avais obtenu à peine un an plus tôt (ce que vous pouvez lire plus en détail dans [cet article](https://medium.freecodecamp.org/how-i-landed-a-full-stack-developer-job-without-a-tech-degree-or-work-experience-6add97be2051)).

L'été approchait rapidement, et le rythme de travail, autrement assez soutenu, ralentissait de jour en jour. Pendant une semaine, lorsque le tour de support technique de l'équipe produit m'est revenu, je me sentais un peu ennuyé et frustré par certains des bugs qui m'avaient été assignés.

C'est dans cet état d'esprit morose que mon père m'a contacté pour me parler de son intention de créer une application mobile pour les clients de son entreprise. Bien qu'il sache que mon travail me tenait occupé et ne s'attendait pas à un engagement à temps plein, il m'a demandé si je voulais participer au projet dans un rôle plus consultatif. Un peu intellectuellement affamé, j'ai dit oui. Bien que ce ne soit pas mon intention initiale, ce rôle consultatif a finalement abouti à ce que je prenne en charge le développement de l'application en tant que développeur principal.

Maintenant, vous pourriez vous demander — pourquoi tenter de se lancer dans le domaine des applications mobiles après seulement un peu moins d'un an d'expérience professionnelle en développement web ? Ne serait-il pas plus judicieux de continuer à se spécialiser dans ce domaine tout en ajoutant quelques années d'expérience à votre CV ?

Absolument. Mais, étant le généraliste désespéré que je suis, je me suis engagé il y a plusieurs années à prendre des décisions de carrière non basées sur la stratégie de carrière, mais plutôt sur ce qui me rend heureux. En d'autres termes : mon CV est déjà un désastre qui ne pourrait probablement pas être plus dispersé et incohérent.

Bien sûr, la stratégie de carrière et le bonheur au travail ne sont pas nécessairement mutuellement exclusifs. En fait, j'étais très heureux avec mon ancien emploi et mon employeur. J'ai simplement eu l'occasion de trouver un autre projet pour lequel je ressentais encore plus de passion.

Alors, qu'est-ce qui a rendu ce projet particulier si excitant ? Encore plus excitant que de travailler sur un produit en hyper-croissance utilisé par des milliers d'entreprises dans une équipe avec certaines des personnes les plus géniales que j'ai rencontrées ? En trois mots : **liberté, défi et développement personnel.**

#### Pourquoi React Native ?

Lorsque j'ai rejoint le projet, mon client avait déjà reçu quelques offres de la part de certaines agences digitales locales. Avant même que je ne considère construire l'application moi-même, on m'a demandé de les examiner en tant que service amical. Et j'ai été simplement surpris par la faible qualité des propositions.

L'une d'entre elles avait envoyé quelques croquis de design qui étaient vraiment négligés et pas du tout en ligne avec la marque présentée sur le site web du client. Une autre agence a proposé un prix ridicule avec des frais récurrents encore plus ridicules. Et une troisième n'avait même pas semblé faire le moindre travail de préparation de pitch. Et elles partageaient toutes une chose : elles voulaient construire l'application avec le framework hybride Cordova.

Et ce n'était pas tout. Bien que Cordova soit complètement gratuit et open-source, l'une d'entre elles avait même essayé de cacher le fait que c'était la technologie qu'elles utilisaient. Au lieu de cela, elles ont promu leur plateforme interne d'applications mobiles "propre" — apparemment juste une fine couche autour de Cordova — pour justifier un verrouillage leur donnant des droits exclusifs de maintenance de l'application et rendant un éventuel transfert futur compliqué et coûteux. Des propositions de faible qualité.

Maintenant, je ne garde aucune rancune contre les frameworks hybrides. J'utilise des applications construites avec eux tout le temps. Gmail, Slack, Atom et Figma pour n'en nommer que quelques-uns. Mais à l'époque, j'entendais parler de React Native depuis un certain temps. Comment il permettait de construire des applications mobiles multiplateformes en utilisant JavaScript — qui n'étaient pas hybrides !

Quoi maintenant ? iOS et Android avaient-ils somehow discrètement introduit le support pour écrire des applications natives en JavaScript ? Parce que la dernière fois que j'ai vérifié, les applications iOS devaient être construites avec Objective-C ou Swift, et les applications Android avec Java ou Kotlin.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5nLrR721EKdCW9AQ.jpg)

Bien sûr que non. Alors comment les applications React Native pouvaient-elles être appelées de vraies _applications natives_ ? Réponse courte : les API. Il m'a fallu plus de temps pour comprendre cela que je n'ose l'admettre, mais la manière dont les applications React Native peuvent s'exécuter nativement sur votre smartphone n'est pas en exécutant JavaScript, ni en compilant votre JavaScript en code natif, mais en faisant des requêtes à des API qui rendent des composants natifs en Objective-C sur iPhone et en Java sur Android.

Si vous voulez en savoir plus sur les fondamentaux de React Native, je recommande vraiment [cette réponse super pédagogique sur Quora](https://www.quora.com/How-does-React-Native-work), cette [conférence React Conf](https://www.youtube.com/watch?v=UcqRXTriUVI) par l'incroyable Parashuram N et la [présentation originale de RN au monde](https://code.fb.com/android/react-native-bringing-modern-web-techniques-to-mobile/).

Bien que je ne connaissais pas ce secret derrière le tour de magie de React Native à l'époque, je savais qu'il exécutait en fait du code natif — ce qui était aussi mon principal argument pour ne pas opter pour l'une des solutions Cordova suggérées par les agences. J'ai estimé que s'ils voulaient une application mobile, ils devraient construire une application native. Et s'ils voulaient une application HTML/CSS/JS, leur argent serait mieux dépensé en améliorant simplement l'expérience mobile de leur application web.

Lorsque j'ai partagé cela avec le client, ils m'ont demandé si je connaissais quelqu'un qui pourrait construire une telle application. Je leur ai dit que non. Ils m'ont demandé si je pouvais le faire. Je leur ai dit que non. Pourtant, la graine avait été plantée, et je ne pouvais tout simplement pas m'empêcher de m'amuser avec React Native en fonction des spécifications de leur application.

Et avant que je ne m'en rende compte, une base pour leur application était déjà en place. Donc, d'une manière ou d'une autre, quelques semaines après cette conversation, nous avions convenu que je construirais l'application pour eux.

#### Spécifications de l'application

Avant de plonger dans les détails plus techniques, une brève description du type d'application dont nous parlons ici semble de mise.

Le client est une entreprise basée à Stockholm qui gère des espaces de coworking. En d'autres termes, des hôtels d'espaces de travail pour les entreprises. Ils ont actuellement environ 10 espaces actifs où environ 400 entreprises avec environ 1 400 employés louent des bureaux. Ces locataires sont le groupe cible de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K2_Mqp7r1JE88TGco7QhxQ.jpeg)
_Le salon dans l'un des espaces de coworking du client_

Après quelques discussions avec le chef de projet, quelques spécifications de l'application ont cristallisé :

* Authentification de connexion/déconnexion et réinitialisation du mot de passe. Note : tous les comptes utilisateurs sont créés par les administrateurs, donc les inscriptions ne sont pas possibles dans l'application. Par conséquent, si vous décidez de télécharger l'application, vous ne pourrez essentiellement rien faire avec ?
* Visualisation et édition d'un profil utilisateur, incluant le nom, l'email, le mot de passe et l'image d'avatar.
* Notifications push.
* Une destination Accueil où les utilisateurs peuvent lire les événements récents autour de l'entreprise en général et de leur espace de coworking en particulier.
* Une destination Communauté où les utilisateurs peuvent parcourir les différents espaces de coworking, entrer en contact avec le gestionnaire de chaque espace et voir les autres entreprises résidentes.
* Une destination Conférence où les utilisateurs peuvent réserver des salles de réunion et gérer leurs réservations.
* Une destination Sélection où les utilisateurs peuvent accéder à des réductions et offres exclusives pour les membres.
* Construire d'abord la version iOS, puis ajouter le support pour Android.
* Une application web d'administration backend pour gérer le contenu de l'application RN. Bien que je me concentrerai sur les aspects frontend dans ce texte, il pourrait être pertinent de savoir qu'elle a été construite sur Ruby on Rails, Postgres et Heroku.

Comme vous pouvez le constater, il s'agit d'un ensemble de fonctionnalités assez restreint. Ce qui est exactement ce que vous voulez pour votre première application avec une nouvelle technologie. Si vous voulez savoir comment le résultat final s'est avéré (et si le reste de ce texte vaut votre temps ou non), voici un aperçu de la version 1.0 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lr7nBvw3Tm1KDoyB54Ndyg.png)

Vous êtes toujours là ? Super, alors continuons.

#### Apprendre des meilleurs

Imaginez que vous avez promis à un ami de lui construire une maison. Mais vous n'avez aucune idée de comment construire une maison. À peine où commencer. Quelle est la première chose que vous feriez ?

Vous vous trouvez un charpentier.

C'est donc ce que j'ai essayé de faire. Et j'ai touché le jackpot. Après seulement quelques heures de recherche des ressources d'apprentissage React Native disponibles, j'ai trouvé un [cours vidéo en 13 parties de Harvard](https://www.youtube.com/playlist?list=PLhQjrBD2T382gdfveyad09Ierl_3Jh_wR) sur YouTube (complètement gratuit). Chaque conférence approfondissant son propre sujet pendant 90 à 120 minutes chacune. Donc environ 23 heures de matériel de haute qualité au total.

Immédiatement, j'ai commencé à consommer les conférences vidéo comme possédé. Et après seulement quelques semaines de codage en parallèle pendant les nuits et les week-ends, j'avais terminé le cours et m'étais mis en place avec une base d'application assez décente.

En rétrospective, c'est sans aucun doute l'une des meilleures ressources d'apprentissage que j'ai trouvées, toutes catégories confondues. Le programme chargé et toujours pertinent a absolument joué un grand rôle, mais l'enseignant Jordan Hayashi était définitivement le grand gagnant ici. Je décrirais son style d'enseignement comme rapide, hyper-pratique et direct. Pas de temps perdu en mauvaises blagues et anecdotes personnelles distractives. Contrairement à vous-même...

Quoi qu'il en soit, d'une manière ou d'une autre, chaque conférence semblait toujours compresser une quantité d'informations qui aurait pris à la plupart des autres enseignants au moins deux fois plus de temps. En d'autres termes, un style très similaire à celui de l'enseignant de Harvard CS50, David J Malan.

Donc, si vous cherchez un point de départ pour votre première application RN, ce serait ma recommandation numéro 1. Un bémol cependant : dans le cours, Jordan utilise l'[outil Expo](https://expo.io/), qui est un excellent outil pour la plupart des applications simples car il fait beaucoup du travail fastidieux pour vous. Mais si vous, comme moi, construisez la base de ce qui pourrait devenir une application assez grande et complexe plus tôt que tard, où vous valorisez la liberté de configuration totale, react-native init pourrait être une solution plus appropriée.

La deuxième meilleure ressource d'apprentissage à laquelle j'ai eu accès était en fait mes collègues. Par une coïncidence heureuse, nous venions de commencer un projet React Native dans l'entreprise où j'ai travaillé jusqu'à il y a quelques mois. Bien que je ne faisais pas partie du projet moi-même, j'ai appris énormément en parlant simplement aux gars du projet et en examinant leurs PR.

Maintenant que nous avons réglé toutes les choses contextuelles, nous pouvons enfin passer aux aspects plus techniques !

#### **Environnement de développement**

Après avoir mis en place la base de l'application en utilisant react-native init, l'un des premiers défis était de se familiariser avec un nouvel environnement de développement.

Si vous venez de l'environnement de développement web moyen, beaucoup de choses resteront les mêmes. Pour moi, cela incluait garder Atom comme mon éditeur de texte, iTerm comme mon terminal et GitUp comme mon interface git (aux utilisateurs de Vim qui grognent : les haters vont hater). Mais à part cela, React Native nécessitait quelques ajouts à mon flux de travail habituel.

Se familiariser avec le simulateur iOS, par exemple. Bien que l'exécution de "react-native run-ios" depuis votre ligne de commande semble trompeusement simple, au début, cela ne suffisait rarement à faire fonctionner le simulateur. Comme de nouveaux packages npm étaient ajoutés au projet presque quotidiennement (et plus tard aussi quelques modules natifs CocoaPod), j'ai dû me familiariser plus que je ne l'aurais préféré avec le rituel douloureux de vider watchman, de supprimer le cache haste, de supprimer le répertoire node_modules, de réinstaller tous les modules node et de réinitialiser le cache Metro Bundler. La commande suivante fera tout cela pour vous :

```
watchman watch-del-all && rm -rf tmp/haste-map-react-native-packager && rm -rf node_modules && yarn && npm start --reset-cache
```

9 fois sur 10, cette danse suffisait à relancer le simulateur. Et parfois, il fallait plonger profondément dans divers problèmes GitHub et fils de discussion Stackoverflow.

La racine de certaines autres douleurs était que pendant longtemps, je pensais que l'ouverture de Xcode était nécessaire pour accomplir certaines choses. Et croyez-moi, vous voulez passer le moins de temps possible dans cette maison de l'horreur qu'est cet IDE (plus sur cela plus tard).

Comme dire au simulateur d'exécuter une certaine version d'iPhone. Si quelqu'un m'avait dit que la ligne ci-dessous faisait exactement cela pour moi, directement depuis la ligne de commande, j'aurais probablement été une personne légèrement plus heureuse pendant ces premiers mois.

```
react-native run-ios --simulator='iPhone X'
```

Un autre exemple serait la [fusée à 3 étages](https://facebook.github.io/react-native/docs/running-on-device#building-your-app-for-production) requise lors du passage du mode Release (pour déployer l'application sur l'App Store ou une destination CI comme Visual Studio App Center ou Firebase) au mode Debug (mode dev). Peut-être évident pour beaucoup, ces changements pouvaient également être faits directement depuis votre éditeur de texte de choix. Quoi qu'il en soit, juste deux petites choses qui ont eu un impact surprenant sur mon flux de travail lorsque je travaillais en mode dev.

Enfin, il a fallu un certain temps pour s'habituer à devoir constamment sauter entre différentes applications macOS pour faire des choses que je faisais normalement dans Chrome lorsque je travaillais avec des applications web.

Pour inspecter mes logs de console JavaScript et la sortie HTML/CSS pour le débogage de style, je me suis tourné vers [React Native Debugger](https://github.com/jhen0409/react-native-debugger). Et pour suivre l'état de l'application, les actions dispatchées et les requêtes/responses API, j'ai utilisé [Reactotron](https://infinite.red/reactotron). Bien que j'ai trouvé ces deux applications extrêmement utiles, je ne pouvais m'empêcher de regretter mon flux de travail Ember.js correspondant, où je pouvais faire toutes ces choses au même endroit où mon application s'exécutait réellement (avec l'aide du plugin Ember Inspector Chrome).

#### Navigation

La navigation/le routage a apparemment été un problème assez difficile à résoudre dans React Native. Quatre ans plus tard, il existe de nombreuses solutions différentes, mais toujours aucun consensus évident sur celle qui est la meilleure. J'ai décidé d'opter pour react-navigation, mais surtout parce que c'était la solution utilisée à la fois dans le cours de Harvard et dans le projet sur lequel mes collègues travaillaient.

Cependant, si j'avais pris le temps de faire quelques recherches appropriées, j'aurais peut-être fait les découvertes suivantes :

* Le [dépôt react-navigation](https://github.com/react-navigation/react-navigation) compte ~15 000 étoiles et 86 problèmes ouverts. Il est entièrement basé sur JavaScript et possède également la documentation la plus complète de toutes les solutions de navigation que j'ai vues.
* Le [dépôt react-native-navigation](https://github.com/wix/react-native-navigation) compte ~10 000 étoiles et 162 problèmes ouverts. Il est également important de noter qu'il n'est pas entièrement basé sur JavaScript (c'est-à-dire qu'il nécessite l'édition de fichiers natifs).
* Le [dépôt react-router](https://github.com/ReactTraining/react-router) compte ~35 000 étoiles et 36 problèmes ouverts. Cependant, ces chiffres ne sont pas vraiment comparables aux autres puisque le dépôt inclut également des packages de routage pour React.js.
* Le [dépôt native-navigation](https://github.com/airbnb/native-navigation) compte ~3 000 étoiles et 55 problèmes ouverts. Cependant, le fait que cette solution soit encore en bêta, non entièrement basée sur JavaScript et maintenue par Airbnb doit être sérieusement considéré avant d'y investir beaucoup de temps ([Airbnb a décidé d'abandonner React Native](https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a)).

En tenant compte de ce qui précède, j'aurais probablement encore choisi react-navigation, car je n'aurais pas eu le temps de les tester toutes, comme l'a fait par exemple [Kurtis Kemple chez MLS](https://www.youtube.com/watch?v=42ogpJVwtw0&t=1676s). Enfin, comme il l'explique dans sa conférence, choisir une solution de navigation n'est pas vraiment une question de savoir laquelle est la meilleure, mais plutôt laquelle répond le mieux à vos besoins particuliers.

Après avoir travaillé avec react-navigation pendant environ 9 mois, je dois dire que je n'ai pas vraiment grand-chose à redire. Étant donné que ma principale référence était la bibliothèque [router.js](https://github.com/tildeio/router.js) utilisée dans [Ember.js](https://www.emberjs.com/), c'était une expérience de routage entièrement nouvelle.

Se familiariser avec les trois principaux types de navigateurs de react-navigation était la partie facile (StackNavigator, TabNavigator et DrawerNavigator). La partie difficile était de comprendre comment les navigateurs devaient être imbriqués les uns dans les autres pour obtenir le flux utilisateur souhaité.

Par exemple, le fait que mon DrawerNavigator devait être à la racine de la navigation (un niveau au-dessus de ma TabNavigation principale) n'était pas du tout évident pour moi. Si cela est difficile à imaginer, voici le DrawerNavigator en action (beaucoup plus fluide en réalité que dans le gif) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oxzcKc-9giPJUKW5qY3eUg.gif)
_DrawerNavigator de react-navigation en action_

Comme vous pouvez le voir, je voulais une barre latérale qui pouvait être ouverte avec un glissement du pouce depuis n'importe où dans l'application.

Étant donné qu'une barre latérale est plus un composant secondaire dans une application par rapport à la barre d'onglets principale en bas, mon premier instinct ici était que le [DrawerNavigator](https://reactnavigation.org/docs/en/drawer-navigator.html) devait être placé sous ou en parallèle avec la position centrale du [BottomTabNavigator](https://reactnavigation.org/docs/en/bottom-tab-navigator.html) dans l'arbre des routes (voir l'image ci-dessous).

Cependant, après m'être cogné la tête contre le mur en essayant de forcer l'insertion de la barre latérale, j'ai découvert que la méthode react-navigation serait en fait de placer le DrawerNavigator un niveau au-dessus du BottomTabNavigator, c'est-à-dire à la racine de l'arbre des routes. Espérons que ce conseil permettra à quelqu'un d'économiser le nombre d'heures que j'ai passées dans la documentation et les fils de discussion GitHub pour obtenir cette information.

Voici une autre illustration avec le DrawerNavigator à la racine :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yfWBx8ZlkLbdtwfHspxwtw.png)
_L'arbre de navigation final de la version 1.0 de l'application_

Une question que vous pourriez vous poser est : pourquoi un StackNavigator et un TabNavigator pour Community et Conference ? Pourquoi ne pas simplement sauter la couche de pile et aller directement aux onglets ?

Eh bien, parce que je voulais un en-tête au-dessus de chacun des deux TabNavigators. Ces gars-là :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7QcXH_IjIdtK-HsdqPFxYw.png)

Encore une fois, mon intuition et la méthode react-navigation divergeaient. Étant donné que le [createMaterialTopTabNavigator](https://reactnavigation.org/docs/en/material-top-tab-navigator.html) doit être un composant de navigation assez standard, j'ai pensé qu'il devrait avoir une configuration d'en-tête intégrée simple dans ses navigationOptions. Il s'avère qu'il n'en a pas, ce qui m'a forcé à utiliser un StackNavigator entre les deux, ajoutant ainsi une autre couche de complexité à l'infrastructure pour un but purement superficiel.

Ce défaut dans react-navigation m'a également causé quelques problèmes plus sérieux. Notamment, faire en sorte que les images d'en-tête se replient/disparaissent lorsqu'un utilisateur fait défiler vers le bas dans l'une des deux [FlatLists](https://facebook.github.io/react-native/docs/flatlist). Puisque les en-têtes de Home et Selection sont rendus dans le même StackNavigator que leurs listes, ici ce problème pouvait facilement être résolu en laissant simplement l'en-tête défiler vers le haut avec le reste de la liste.

Mais avec Community et Conference — puisque les en-têtes sont rendus dans des StackNavigators, et les listes dans des TabNavigators un niveau en dessous dans l'arbre — je n'ai trouvé aucun moyen d'appliquer la même solution à eux. Je suis donc laissé avec cette asymétrie douloureuse :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3bOHVBDrF1QdKyUgSoQeHw.gif)
_Défilement dans TabNavigator vs StackNavigator_

Cela peut ne pas sembler un problème sur l'iPhone X s'exécutant dans le simulateur ci-dessus, mais sur des écrans plus petits, cet en-tête peut prendre environ 20 % de la surface précieuse de l'écran. Si quelqu'un a une idée pour contourner cela, je suis tout ouïe !

Le même problème de TabNavigator a également causé un problème dans la destination Communauté. Comme démontré ci-dessous, je voulais mettre un autre TabNavigator à l'intérieur de l'onglet Espaces de coworking, pour obtenir les trois onglets supérieurs Info, Membres et Contact visibles sur le côté droit du gif.

Cependant, comme TabNavigator rendait très difficile la mise en place d'un diaporama d'images au-dessus sans ajouter une tonne de complexité causant toutes sortes d'autres maux de tête de navigation (principalement liés aux paramètres de navigation), j'ai dû recourir à un package JS appelé [react-native-swiper](https://github.com/leecade/react-native-swiper) pour gérer ces trois onglets à la place. Et j'aurais en fait été totalement satisfait de cela, si ce n'était pour les animations de glissement assez peu fluides des soulignements des onglets. Quoi qu'il en soit, j'ai jugé que c'était un prix équitable pour éviter les autres maux de tête de navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2nrIBpSOyp9_DPdhBaphEQ.gif)
_TabNavigator de react-navigation vs react-native-swiper (remarquez les différentes animations du soulignement doré lors du balayage)_

Pour résumer mon expérience avec la navigation dans React Native :

* Il existe de nombreuses solutions bien documentées, parmi lesquelles j'ai trouvé que react-navigation répondait le mieux à mes besoins.
* React-navigation a rendu très facile de commencer sans savoir grand-chose sur le fonctionnement de la navigation purement native.
* React-navigation a quelques dimensions non intuitives (pour un développeur web), mais aucune qui ne puisse être surmontée avec quelques contournements.

#### Écran de démarrage

Lorsque vous exécutez une nouvelle application react-native init sur votre simulateur, en rechargeant l'application encore et encore à chaque fois que vous faites une modification, vous prendrez rapidement conscience de la nécessité d'un écran de lancement joli (également appelé écran de démarrage).

Et comme il existe déjà un [guide vraiment génial pour savoir comment y parvenir](https://medium.com/handlebar-labs/how-to-add-a-splash-screen-to-a-react-native-app-ios-and-android-30a3cec835ae), je ne perdrai pas notre temps à répéter les mots de l'auteur. Je n'ai rencontré qu'un seul problème ici que le guide ne couvrait pas :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8TBnxIdPGAh0Tni3F2cHOQ.jpeg)

C'est un cas limite iOS, mais toujours quelque chose qui dérangera probablement les quelques utilisateurs exposés. Je l'ai découvert pour la première fois lorsque je travaillais quelque part où je ne pouvais pas accéder au wifi, et donc je partageais le 4G de mon téléphone avec mon ordinateur portable. Comme les utilisateurs d'iPhone le savent, la barre d'état sur l'appareil devient bleue et sa hauteur augmente pendant le partage d'Internet. Et cela a complètement cassé mon image d'écran de démarrage lors de l'exécution sur l'appareil. Le même problème est apparu lors d'un appel.

Donc, après avoir fouillé pendant un certain temps dans le dépôt [react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen) sans trouver rien d'utile, j'ai décidé de contourner le problème en masquant complètement la barre d'état pendant que l'écran de démarrage était visible.

C'est super facile, tout ce que vous avez à faire est d'ajouter une clé UIStatusBarHidden avec la valeur booléenne true à votre fichier info.plist, puis de définir la propriété "hidden" du composant React Native StatusBar sur false après que SplashScreen.hide() a été appelé.

#### Gestion d'état

"Convention over configuration" est un mantra que j'ai l'impression d'avoir entendu tous les jours depuis deux ans. Notamment chez mon ancien employeur. Pas très surprenant, puisque nous utilisions Ruby on Rails côté serveur et Ember.js côté client — deux frameworks essentiellement synonymes de cette expression. Je pensais savoir ce que ces mots signifiaient, mais le processus d'apprentissage de la gestion d'état dans React Native leur a donné un tout nouveau sens.

Bien que j'aie joué avec la bibliothèque React "configuration over convention" pour le web dans quelques applications démos très simples, je n'avais jamais construit quelque chose d'assez grand pour justifier l'introduction d'un conteneur d'état comme [Redux](https://redux.js.org/) ou [MobX](https://mobx.js.org/). Au lieu de cela, la plupart de mon expérience de gestion d'état JS provenait de [Ember Data](https://github.com/emberjs/data) (la bibliothèque de gestion d'état et de persistance des données intégrée à Ember).

Puisque Redux était la solution de référence dont j'entendais parler depuis des années sur les podcasts, les blogs et dans les vidéos (y compris Jordan dans le cours YouTube RN), je n'ai jamais vraiment considéré ses concurrents. Je voulais simplement mettre en place la meilleure infrastructure de gestion d'état possible avec le moins d'efforts possible.

Dans Ember, vous obtenez essentiellement 90 % de cette infrastructure gratuitement. Je ne savais pas que j'allais devoir accepter le ratio inverse dans mon projet actuel. Non seulement React ne vous fournira rien d'utile pour gérer l'état global, mais Redux — la solution la plus populaire sur le marché — est si léger que vous devrez essentiellement tirer 90 % du poids vous-même pour obtenir une solution d'état égale.

Maintenant que le moi légèrement plus jeune a sorti cela de son système, la partie difficile était en fait de se familiariser avec ce nouveau flux de travail fonctionnel et immutable. Une fois que j'avais accepté la quantité surprenante de nouvelle complexité nécessaire pour simplement récupérer ou poster des données depuis/vers mon serveur, tout se résumait à 7 étapes assez simples :

1. Ajoutez les trois SOME_ACTION_REQUEST, SOME_ACTION_FAILED, SOME_ACTION_SUCCEEDED à votre fichier de constantes.
2. Ajoutez le créateur d'action à votre fichier d'actions.
3. Gérez les trois actions dans le réducteur approprié, et si nécessaire, ajoutez un nouveau réducteur et incluez ce réducteur dans votre réducteur racine.
4. Ajoutez des workers à la saga appropriée, et si nécessaire, ajoutez une nouvelle saga et incluez cette saga dans votre saga racine (j'utilise [redux-saga](https://github.com/redux-saga/redux-saga) pour les actions asynchrones).
5. Ajoutez une fonction pour gérer toute éventuelle requête API.
6. Mappez l'état nécessaire aux props dans les composants React appropriés.
7. Dispatch l'action SOME_ACTION_REQUEST depuis les composants React appropriés.

Redux et redux-saga ont certainement beaucoup plus à offrir, mais en ce qui me concerne actuellement, les 7 étapes ci-dessus sont essentiellement ce que Redux représente pour moi.

#### Sessions

Nous avons donc notre environnement de développement React Native configuré, un arbre de navigation cartographié et une infrastructure de gestion d'état en place. Quelle serait une bonne prochaine étape ? Eh bien, pour moi, le choix naturel était l'authentification des utilisateurs, entrant ainsi dans les sessions.

Si vous venez de React Native avec un arrière-plan web, traiter avec les sessions ne nécessitera pas beaucoup de puissance de calcul cérébral. Si vous êtes familier avec le concept de [LocalStorage](https://developer.mozilla.org/en-US/docs/Web/API/Storage/LocalStorage), vous devez simplement le remplacer par [AsyncStorage](https://facebook.github.io/react-native/docs/asyncstorage) : une couche d'abstraction qui vous permettra de persister des paires clé-valeur à travers les sessions. En d'autres termes, parfait pour stocker un jeton d'authentification généré par votre serveur lorsqu'un utilisateur se connecte.

#### Listes

Dans l'ensemble, mon impression est que les listes sont un problème assez bien résolu dans React Native. Basiquement, vous avez trois options à portée de main : Si vous traitez avec une liste statique dont les données ne changent pas, [ScrollView](https://facebook.github.io/react-native/docs/scrollview) suffira probablement. Si vous traitez avec une liste plus grande et dynamique, [FlatList](https://facebook.github.io/react-native/docs/flatlist) est ce que vous voulez. Et si vous voulez une liste plus grande et dynamique qui est également divisée en différentes sections, [SectionList](https://facebook.github.io/react-native/docs/sectionlist) est votre réponse.

J'ai exclusivement utilisé FlatList pour mes listes dynamiques. Et bien que je l'aime intuitivement ainsi que son vaste ensemble d'options de configuration, j'ai vécu quelques situations assez douloureuses. Ci-dessous, je vais les passer en revue une par une.

**Rafraîchissement par glissement**  
FlatList possède une propriété appelée refreshControl, à laquelle vous pouvez passer un composant que vous souhaitez utiliser pour rafraîchir le contenu de la liste, déclenché lorsque l'utilisateur tire vers le bas depuis le haut de la liste. Heureusement pour nous, React Native possède un composant spécialement conçu à cet effet — [RefreshControl](https://facebook.github.io/react-native/docs/refreshcontrol). Tout est très intuitif et facile à configurer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gQlE94nbzguoi2_wqPul-A.gif)
_RefreshControl en action_

Cependant, je suis tombé sur une situation étrange, où la propriété refreshControl et/ou le composant RefreshControl semblaient être les coupables. Un peu de contexte :

Dans mes listes, je veux que les utilisateurs puissent a) faire défiler vers le haut pour rafraîchir la liste, déclenchant une fonction que j'ai nommée handleRefresh() et b) faire défiler vers le bas pour charger plus d'éléments dans la liste, alias. "défilement infini" (plus d'informations à ce sujet plus bas). Des choses assez standard.

Cependant, après un certain temps, j'ai commencé à rencontrer ces situations où le spinner de rafraîchissement se figeait et continuait à tourner indéfiniment, sans afficher les nouveaux éléments récupérés depuis le serveur. Après un certain temps de recherche, j'ai trouvé la raison de mon problème dans [cette réponse à un problème GitHub](https://github.com/facebook/react-native/issues/5839#issuecomment-354442067).

Le problème était que les propriétés refreshControl et onEndReached (pour le défilement infini) utilisaient toutes deux la même propriété booléenne : "fetching". Et pour une raison étrange, lorsque cette propriété fetching passait de false à true puis revenait à true, dans un intervalle de temps inférieur à 250 ms, RefreshControl se cassait et le spinner de chargement se figeait.

Pour tester cette théorie, j'ai essayé d'ajouter un setTimeout(), fixant un intervalle de temps minimum de 350 ms entre le changement de la valeur du booléen fetching. Et cela a résolu le problème. Mais comme l'utilisation de setTimeout me semblait un peu trop bricolée à mon goût, j'ai finalement opté pour la solution consistant à utiliser simplement deux propriétés différentes pour les fonctions handleRefresh() et handleLoadMore() : "refreshing" et "loadingMore". Je ne sais pas à quel point ce problème est courant, mais j'espère que mon contournement pourra faire gagner du temps et éviter des frustrations à quelqu'un.

Notez que la documentation officielle recommande d'utiliser onRefresh et refreshing au lieu de la propriété refreshControl. La raison pour laquelle j'ai opté pour refreshControl est que je ne voyais pas d'autre moyen de pouvoir personnaliser le style du spinner.

**Défilement infini**  
Comme mentionné ci-dessus, je voulais également donner à mes utilisateurs l'impression que la liste était complètement fluide. Cela signifie ne pas avoir à appuyer sur un bouton "Charger plus" en bas pour charger plus d'éléments, et ne pas avoir à obtenir un spinner de chargement bloquant ou des espaces réservés de chargement couvrant également les éléments de liste déjà chargés pendant la récupération de plus d'éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lNPuWakcdvtPd43jR0GhCg.gif)
_Défilement infini avec FlatList (remarquez comment la valeur de seuil de 2 déclenche onEndReached lorsque nous sommes à 2 hauteurs d'écran de la liste des éléments du bas)_

À cette fin, onEndReached avait essentiellement tout ce dont j'avais besoin. J'ai eu deux problèmes lors de sa mise en œuvre.

Le premier était de comprendre la propriété onEndReachedThreshold, qui indiquera à votre FlatList quand déclencher la fonction passée à onEndReached. Après quelques essais et erreurs, mon explication serait la suivante :

Si vous avez 100 éléments chargés dans votre liste et que l'écran affiche 10 éléments à la fois, une valeur onEndReachedThreshold de 1 signifierait que la fonction onEndReached sera appelée lorsque vous faites défiler au-delà du 90e élément de votre liste. Si la valeur est 2, la fonction sera appelée dès que vous êtes à 2 hauteurs d'écran de la fin, c'est-à-dire au 80e élément, et ainsi de suite.

Le deuxième problème que j'ai rencontré avec le défilement infini est ce que je ne peux supposer être qu'un bug de FlatList. À savoir, que chaque fois que je faisais défiler vers le bas au-delà du seuil, ma fonction handleLoadMore() passée à la propriété onEndReached était appelée à plusieurs reprises, souvent plus de 10 fois de suite.

Coïncidence, une fois de plus la solution pouvait être trouvée en utilisant la propriété loadingMore, en ajoutant une instruction if dans la fonction handleLoadMore() pour s'assurer que l'action de récupération n'était dispatchée que si !loadingMore. Naturellement, vous voudriez également vérifier dans cette même instruction if que vous n'êtes pas sur la dernière page de votre pagination serveur.

**Espaces réservés de chargement**  
Quelque chose qui n'aurait pas nécessairement d'effet sur l'expérience utilisateur, mais qui m'aurait certainement rendu plus heureux en tant que développeur, serait la présence d'une propriété ListLoadingComponent dans FlatList, tout comme il y a un ListHeaderComponent, un ListEmptyComponent et un ListFooterComponent.

Comme il n'y en a pas, j'ai été contraint de m'appuyer sur des instructions if maladroites pour gérer le rendu des espaces réservés dans de nombreuses fonctions render().

**Retour en haut**  
Le dernier sujet de liste que j'aimerais aborder est le retour en haut de la liste en appuyant sur un bouton. Dans mon application, j'ai actuellement ces boutons dans les en-têtes, mais un autre emplacement courant pour eux est dans les boutons d'onglets du bas.

Pour y parvenir, j'ai utilisé la méthode scrollToOffset de FlatList, qui est assez simple à comprendre à partir de la documentation. Cependant, un détail crucial que je n'ai pas trouvé dans la documentation est que vous devez également utiliser la propriété ref dans le composant FlatList, comme suit :

```
<FlatList  ref={(ref) => { this.newsListRef = ref; }}  .../>
```

Ce que cela fait, c'est essentiellement donner à votre FlatList un identifiant, afin qu'il puisse être appelé depuis une fonction ailleurs. Dans mon cas, cela m'a permis d'appeler la fonction ScrollToOffset depuis ma fonction `handleScrollToTop()`, et par exemple de la passer en tant que paramètre à mon objet de navigation react-navigation, permettant de l'appeler depuis n'importe quelle route à laquelle le paramètre est passé.

```
componentDidMount() {  this.props.navigation.setParams({    scrollToTop: this.handleScrollToTop,  });}
```

```
handleScrollToTop = () => {  this.newsListRef.ScrollToOffset({    x: 0, y: 0, animated: true,  });};
```

Notez qu'après la mise à niveau vers react-navigation 3, la chose ref n'était plus nécessaire puisque les boutons createBottomTabNavigator géreront désormais le retour en haut par défaut.

#### Images

Les images, j'ai appris, courent le plus grand risque de devenir la seule chose qui fait que votre application mobile est mauvaise. Naturellement, une gestion efficace des images est également importante sur le web, mais comme les téléphones fonctionnent sur 4G (ou 3G, Dieu nous en préserve) dans une bien plus grande mesure, une vitesse de téléchargement moyenne plus faible doit être supposée, ce qui à son tour pourrait faire paraître votre application lente.

Les images prendront également probablement une plus grande partie de l'écran du téléphone par rapport à l'écran de l'ordinateur, c'est pourquoi elles devraient également être accordées une priorité plus élevée d'un point de vue cosmétique. Donc, bien que cela ne soit peut-être pas la partie la plus amusante de tout cela, investir un peu de temps dedans en vaudra probablement la peine.

Mon application s'est avérée assez lourde en contenu d'images. Elle totalise 7 listes avec des éléments de liste avec des propriétés d'image qui ne sont pas seulement affichées dans les éléments de liste réels, mais aussi sur les "détails" de chaque élément (l'écran auquel un utilisateur est redirigé lorsqu'il appuie sur un élément de liste).

**Téléchargement d'images**  
Sur l'écran d'édition du compte utilisateur, l'application permettait également aux utilisateurs de télécharger une image d'avatar. Pour cela, j'ai utilisé la bibliothèque [react-native-image-picker](https://github.com/react-community/react-native-image-picker), ainsi que Cloudinary et Carrierwave sur mon backend Rails.

Au début, j'ai mis toute la logique de téléchargement côté client, en utilisant l'API Node de Cloudinary et le module [react-native-fetch-blob](https://github.com/wkh237/react-native-fetch-blob). Mais après un certain temps, comme je voulais un peu plus de flexibilité dans ma logique de téléchargement et ne voulais pas mettre trop de logique complexe côté React Native, je l'ai tout déplacé vers le backend Rails.

Cependant, j'ai rencontré quelques problèmes en essayant de poster les images sur mon serveur en utilisant react-native-fetch-blob. Par conséquent, la complexité supplémentaire et le statut de maintenance très incertain du dépôt à l'époque m'ont fait choisir l'API [JS FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) intégrée. Notez cependant que le dépôt react-native-fetch-blob, qui n'est plus maintenu, a depuis été déplacé vers [rn-fetch-blob](https://github.com/joltup/rn-fetch-blob), où il est activement maintenu.

**Affichage d'images**  
En vérité, la balise [React Native Image](https://facebook.github.io/react-native/docs/image), avec ses propriétés style, source et resizeMode, vous mènera loin. Si vous ne vous souciez pas de la mise en cache, de l'affichage de plusieurs images ou d'un autre cas spécial, vous n'aurez probablement pas besoin d'ajouter d'autres dépendances.

Cependant, j'ai trouvé deux cas où j'ai jugé utile d'ajouter à ma liste de dépendances. Le premier était les images au format avatar circulaire affichées dans certaines des cartes de liste et les écrans de profil utilisateur. Pour cela, l'[Avatar de react-native-elements](https://react-native-training.github.io/react-native-elements/docs/0.19.1/avatar.html) s'est avéré utile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gghgp4BhT_f8djNLHqnypQ.gif)
_react-native-slideshow forké en action_

Cependant, ce composant ne fait rien que vous ne puissiez réaliser vous-même avec un peu de style supplémentaire sur le composant Image par défaut. Donc, à moins que vous n'ayez déjà intégré la bibliothèque pour d'autres raisons, je ne recommanderais pas d'ajouter cette dépendance uniquement pour le formatage des avatars.

L'autre cas où j'ai décidé de sous-traiter était l'affichage de plusieurs images dans un diaporama (voir le gif). Pour cela, j'ai utilisé la bibliothèque [react-native-slideshow](https://github.com/haqiqiw/react-native-slideshow), qui faisait exactement ce que je voulais.

Mais attention, comme elle est mal entretenue, je recommande fortement de la forker et de réduire un peu le code plutôt que de l'utiliser telle quelle depuis vos node_modules.

**Espaces réservés de chargement**  
Avec 7 listes à défilement infini affichant des images, l'utilisateur est destiné à attendre pendant que toutes ces données sont récupérées depuis le serveur. Comme nous le savons tous, attendre est probablement l'expérience la plus frustrante de la technologie moderne. Donc, naturellement, nous voulons la rendre aussi supportable que possible.

Entrez les espaces réservés.

Je ne suis pas vraiment sûr pourquoi, mais chaque fois que j'attends que du contenu se charge, je suis un milliard de fois plus frustré si tout ce que j'obtiens est un spinner de chargement (ou pire encore — rien du tout), que si je vois des espaces réservés dynamiques et brillants à la manière du fil d'actualité de Facebook. C'est donc ce que je visais.

Heureusement, je n'étais pas le premier à avoir cette idée dans React Native. Il n'a pas fallu beaucoup de recherches avant que je puisse me décider en toute confiance sur deux bibliothèques : [react-native-loading-placeholder](https://github.com/zeljkoX/react-native-loading-placeholder) (pour les espaces réservés réels) et [react-native-linear-gradient](https://github.com/react-native-community/react-native-linear-gradient) (pour les animations brillantes). J'étais vraiment satisfait du résultat, même si j'ai peut-être un peu trop poussé le bouchon avec celui de droite...

![Image](https://cdn-media-1.freecodecamp.org/images/1*InMsoswwjKEHgAhWvDvO7A.gif)
_Espaces réservés de chargement avec react-native-loading-placeholder et react-native-linear-gradient_

**Mise en cache**  
Oui, la mise en cache est également une chose dans le monde natif. Étrangement, il n'y a toujours pas de support intégré pour cela dans la balise Image RN par défaut. Au lieu de cela, vous devrez utiliser la balise CachedImage de cette excellente bibliothèque : [react-native-cached-image](https://github.com/kfiroo/react-native-cached-image).

En gros, tout ce que vous avez à faire est d'installer le package npm et d'échanger toutes les balises Image par défaut que vous souhaitez mettre en cache avec CachedImage. Vous pouvez ensuite vérifier votre timeline Reactotron pour confirmer que les images sont effectivement stockées.

Comparé à l'effort minimal requis pour configurer la mise en cache des images, le retour sur investissement est énorme. Voir ma bande passante Cloudinary passer d'un lourd 95 % du quota mensuel gratuit à environ 4 % était si satisfaisant.

Astuce pro : ajoutez la propriété activityIndicatorProps={{ animating: false }} et créez votre propre espace réservé de chargement plutôt que le spinner de chargement standard lors du chargement des images.

#### Temps

**Sélecteur de temps**  
React Native possède en fait un composant [Picker](https://facebook.github.io/react-native/docs/picker) multiplateforme. Cependant, en raison de sa nature très configurable (et de mon impatience), j'ai cherché une bibliothèque JS qui avait déjà fait une partie du travail pour moi. Heureusement, j'ai trouvé [react-native-picker-select](https://github.com/lawnstarter/react-native-picker-select), qui émule les interfaces natives <select> pour iOS et Android pour presque exactement mes besoins.

Puisqu'il s'agit essentiellement d'un seul fichier JavaScript utilisant des composants React Native intégrés (et un peu de [lodash](https://lodash.com/), qui était déjà une dépendance pour moi), j'ai décidé de simplement voler le code — avec quelques petits ajustements — et de le mettre dans mon propre composant picker. À partir de ce moment, je l'utilise non seulement pour mes sélecteurs de temps pour toutes les listes d'entrée sauf pour le sélecteur de date.

**Sélecteur de date**  
J'ai décidé d'opter pour la bibliothèque [react-native-calendars](https://github.com/wix/react-native-calendars) de Wix pour quelques raisons :

* Je n'aime pas le sélecteur de date natif iOS, car il donne un mauvais aperçu du mois et de l'année. Peut-être que je suis simplement brisé par le développement web, mais c'est mon opinion.
* React Native nécessite actuellement deux implémentations séparées pour les deux plateformes ; DatePickerIOS et DatePickerAndroid, ce qui aurait nécessité beaucoup de duplication de code faisant la même chose.
* Je voulais que le sélecteur ait plus de personnalité et reflète la marque de l'entreprise cliente plutôt que celle d'Apple et de Google.

Aimez-le ou détestez-le, voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BCqHRMZxr1Li_PK8ETn6qg.gif)
_react-native-calendars et react-native-picker-select en action_

**Fuseaux horaires**  
Fuseaux horaires. Si simples en théorie, si difficiles en réalité.

Vers la fin du projet, j'intégrais le backend de l'application avec un SaaS tiers que le client utilise pour ses réservations de salles. Je venais d'avoir le plaisir de me familiariser avec le bon vieux protocole SOAP pour configurer les requêtes API nécessaires pour la section Conférence de l'application. Et lorsque j'ai enfin eu toutes les pièces en place, j'ai commencé à remarquer des comportements temporels étranges du côté React Native.

L'entreprise cliente avait clairement indiqué qu'elle ne voulait pas que les utilisateurs puissent effectuer de nouvelles réservations à la date du jour après 17h ce jour-là, pour des raisons. Mais en raison du [strict fuseau horaire UTC par défaut de l'objet Date JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date), générer cette valeur maximale pour le sélecteur de temps s'est avéré assez délicat. En fait, si délicat que la logique a alourdi mon composant avec trop de complexité à mon goût. Qu'il y ait une bibliothèque pour cela, je me suis dit.

Mes prières ont été exaucées par [moment-js](https://momentjs.com/), qui non seulement était totalement compatible avec React Native, mais avait également un [module de fuseau horaire](https://momentjs.com/timezone/) spécifique qui a généré le booléen parfait pour moi en une seule ligne :

```
const timeSthlmAfterFive = moment().isAfter(moment.tz('17:00:00', 'HH:mm:ss', 'Europe/Stockholm'), 'second');
```

#### Polices et icônes personnalisées

Polices et icônes personnalisées — deux petits détails avec un énorme impact sur l'UI et la marque de votre application. Venant d'un milieu web, je m'attendais à ce que ce soit un casse-tête proportionnel à la danse de conversion de fichiers et d'assemblage de fichiers CSS font-face à laquelle j'étais habitué.

Mais le travail des autres avant moi a rendu cela beaucoup moins douloureux que je ne l'avais prévu. En suivant [ce tutoriel](https://medium.com/react-native-training/react-native-custom-fonts-ccc9aacf9e5e), il m'a fallu environ 10 minutes pour importer les polices personnalisées de l'entreprise cliente. Et la vaste bibliothèque d'icônes de [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons), ainsi que quelques imports personnalisés, m'a jusqu'à présent fourni tout ce dont j'ai besoin en termes d'icônes.

#### Intégration continue, déploiement et monitoring

Passons à la CI/CD — le gagne-pain des gens devops, et le cauchemar de configuration numéro 1 de tous les développeurs solitaires cherchant à gagner rapidement de l'argent.

Puisque j'étais (et je suis toujours) le seul à travailler sur cette application, cela peut sembler un peu excessif pour certains. Comme il n'y a pas de collaboration de code, toutes les nouvelles versions proviendront du même ordinateur, et je pourrais tout aussi facilement construire et tester l'application localement avant de la pousser vers le dépôt GitHub et de soumettre une nouvelle version aux app stores. Cependant, pour quelques raisons simples, j'ai toujours considéré une solution CI comme nécessaire :

* L'entreprise cliente est sur le point de mettre en place une équipe de développeurs en interne. Et lorsqu'ils le feront, ils voudront que l'infrastructure rende aussi facile que possible l'ajout de nouvelles personnes à l'équipe.
* Bien que l'exécution de vos tests localement ne prenne qu'une seule ligne sur la ligne de commande, il est toujours souhaitable d'automatiser tout ce qui peut être automatisé.

J'étais donc déterminé à mettre en place une solution CI. Mais jusqu'à ce point, j'avais supposé que cela se limiterait à la construction et aux tests, et que je devrais trouver des solutions séparées pour, par exemple, les rapports d'erreurs, l'analyse et les notifications push. Sans parler des déploiements continus, qui ne semblaient même pas exister dans le monde du natif.

Et puis j'ai trouvé [Visual Studio App Center](https://visualstudio.microsoft.com/app-center/). Cette [conférence Chain React 2017](https://www.youtube.com/watch?v=f_-S0ZhVmvQ) de Parashuram N (encore) a complètement soufflé mon esprit. Ce qu'il a présenté semblait inclure tous les différents services devops que j'avais envisagé d'ajouter un par un, dans une seule solution : construction, test, diagnostics (rapports d'erreurs), analyse, notifications push ET déploiement continu avec [Codepush](http://microsoft.github.io/code-push/). Sans parler de la distribution vers les app stores et les bêta-testeurs. Et le meilleur de tout, cela permettrait de gérer toutes ces choses pour mon application iOS et Android au même endroit. Et le meilleur du meilleur, cela serait probablement gratuit jusqu'à ce que l'application grandisse, environ un an plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ll8O9KJ5qxAd6qUVcjOg_g.gif)
_Aperçu de VSAC emprunté à : [https://blogs.msdn.microsoft.com/vsappcenter/introducing-visual-studio-app-center/](https://blogs.msdn.microsoft.com/vsappcenter/introducing-visual-studio-app-center/" rel="noopener" target="_blank" title=")_

"C'est trop beau pour être vrai", me suis-je dit avec des yeux larmoyants, haletant d'excitation. C'était juste si beau. Si fluide. Si convivial pour les développeurs (API-first). Et pourtant avec une interface utilisateur si conviviale, au point que même les employés non techniques de mon client pouvaient en comprendre une partie.

Comment tout cela était-il possible, vous demandez-vous ? Eh bien, il s'avère que Microsoft a fait une frénésie d'achats récemment. Pour assembler le sac de bonbons que VSAC est, ils ont acquis un tas de solutions indépendantes existantes comme Codepush (déploiements RN continus) et HockeyApp (distribution de tests et rapports de plantage), ainsi que construit et étendu des produits Microsoft existants. La célèbre éthique "développeurs, développeurs, développeurs, développeurs" signée Steve Balmer semble vraiment plus vraie que jamais dans le sang de l'entreprise.

Alors, avais-je entendu assez pour faire un pari éclairé sur cette technologie relativement nouvelle, en écartant des services concurrents comme [Fastlane](https://fastlane.tools/), [BuddyBuild](https://www.buddybuild.com/) et [Firebase](https://firebase.google.com/) ? Eh bien, si c'était vraiment aussi bon que Parashuram le prétendait, cela me ferait économiser des semaines d'installations et de configurations, et probablement d'innombrables heures de maintenance future de tous les services dispersés nécessaires pour obtenir un résultat similaire. Dans tous les cas, cela valait définitivement le coup d'essayer.

Et environ une semaine plus tard, l'application était entièrement configurée avec toutes les fonctionnalités de VSAC. À l'exception de quelques maladies infantiles, les docs ainsi que le chat de support m'ont fourni toutes les réponses dont j'avais besoin.

Un tel problème était le fait qu'ils ne supportaient pas encore l'intégration avec les comptes Apple Developer utilisant l'authentification à deux facteurs (que Apple a commencé à imposer juste à temps pour que je configure mon compte...). Cela a été incroyablement frustrant pour moi à l'époque, mais quelques semaines seulement après que je l'aie signalé, ils ont ajouté le support officiel pour cela.

Si vous trouvez mes éloges de VSAC un peu unilatéraux, et que vous souhaitez entendre l'opinion de quelqu'un avec une perspective de grande application, je recommande cette revue plus sceptique de [CI/CD](https://hackernoon.com/top-ci-cd-tools-for-your-android-and-ios-projects-8d356b983b3b).

#### Ajout du support pour Android

Avec tout le travail de base iOS en place, j'ai trouvé l'ajout du support pour Android très indolore. Après avoir configuré l'environnement de développement Android Studio et fait fonctionner l'application sur un émulateur Android, la plupart des problèmes pouvaient être résolus avec le [module React Native Platform](https://facebook.github.io/react-native/docs/platform-specific-code.html). Pour le style spécifique à la plateforme, il offre la méthode Platform.select(). Et pour tout autre code spécifique à la plateforme, Platform.OS fera l'affaire.

De plus, la soumission et l'approbation de l'application sur le Google Play Store était BEAUCOUP plus facile que pour l'App Store. Pourquoi ?

#### Parce qu'Apple

Évidemment, aborder React Native en tant que développeur web est susceptible de causer quelques maux de tête. Mais pour moi, le pire mal de tête de loin a été le processus de développement imposé par Apple. Je ne me souviens honnêtement pas avoir déjà vécu autant de goulots d'étranglement et de reports de planning causés par une seule source. Projet technique ou autre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5QrdyGzNrRD-QjE4H4QwUw.jpeg)
_TL;DR_

Principalement, je dirais que le degré inexplicablement élevé de bureaucratie est à blâmer. Si il y a une chose sur laquelle vous pouvez compter lorsque vous développez votre première application iOS, c'est que vous vous ferez un tas de nouveaux amis en cours de route.

Les gars et les filles du Support Apple, par exemple. Vous devrez peut-être les convaincre que l'entreprise derrière votre application existe réellement. Vous pourriez également vous faire quelques amis chez Dun & Bradstreet, leur partenaire d'identification d'entreprise. Et pendant que vous y êtes, vous pourriez même vous faire quelques amis au registre des entreprises gouvernemental local, afin de mettre à jour l'adresse de votre entreprise dans un format que Apple supporte (ils ne supportent pas les entreprises enregistrées dans une boîte postale, ce qui est une pratique très courante au moins ici en Scandinavie).

Et puis vous pourriez passer encore plus de temps avec les gens du Support Apple, puisque ils ne pourront toujours pas approuver votre enregistrement de développeur Apple étant donné que vous êtes juste un consultant, et non un employé réel de l'entreprise cliente. Le processus entier pourrait prendre plus d'un mois. Mais qui s'en soucie quand on se fait de nouveaux amis, n'est-ce pas ?

Et le plaisir ne s'arrête pas là.

Vous avez votre compte d'entreprise de développeur Apple tout configuré. Vous avez terminé la version 1.0 de votre application. Maintenant, vous mourez d'envie de la lancer dans la nature.

Eh bien, vous ne pouvez pas encore. D'abord, vous avez du travail administratif numérique à faire. Vous devrez générer un profil de provisionnement, un certificat iOS, un identifiant, un certificat de notification push Apple .p12 et le bon vieux fichier dSym. Et une fois que vous avez généré, configuré et téléchargé tous ces fichiers aux bons endroits, vous pouvez commencer le processus de révision de l'application.

Selon eux, 50 % de toutes les applications sont approuvées/rejetées dans les 24 heures, et 90 % dans les 48 heures. Mais préparez-vous au pire, puisque le rejet est apparemment juste une partie normale de la vie d'un développeur Apple.

Heureusement, mon application n'a été rejetée qu'une seule fois. C'était pour des raisons de "Métadonnées rejetées". Et j'aurais été tout à fait d'accord avec cela si j'avais simplement oublié de remplir certaines informations requises. Mais comme les métadonnées manquantes étaient apparemment 5 questions très spécifiques (aucune d'entre elles n'étant incluse dans les [Directives de révision de l'App Store](https://developer.apple.com/app-store/review/guidelines/)), cela m'a honnêtement rendu triste.

Triste de vivre dans un monde où seulement deux entreprises contrôlent l'ensemble du pipeline de distribution des applications mobiles natives. Triste qu'au moins l'une d'entre elles se soucie si peu du client qu'elle s'autorise à prendre arbitrairement le temps des autres, causant des mois de retards coûteux dans le lancement des applications. Et si heureux que la même chose ne s'applique pas au web (pour l'instant).

Évidemment, le développement de ma première application React Native pour iOS a inclus des couches et des couches de processus de filtrage bureaucratiques. S'il existe un équivalent d'un démenteur dans le monde du développement mobile, c'est définitivement cela. Il aspirera littéralement l'âme ainsi que tout bonheur éventuel du développeur hors de votre corps.

Voilà. Fin de la tirade. Cela a fait du bien.

#### Résumé

Comme noté précédemment, ce projet a été lancé au début de l'été. En tant que tel, le rythme de travail plus lent de l'été à mon emploi m'a permis de jongler avec les deux pendant quelques mois. Mais finalement, l'échéance d'octobre/novembre approchait simplement trop vite, et je me suis rendu compte que je devrais faire un choix entre rester dans l'emploi ou terminer l'application à temps. Après quelques semaines de réflexion, j'ai choisi cette dernière option.

Bien que ce soit une décision vraiment difficile, en rétrospective, je pense que c'était la bonne. La liberté, le défi et le développement personnel que je cherchais ont été trouvés, et bien plus encore.

En ce qui concerne la liberté, la laisse lâche du client m'a essentiellement permis de travailler de n'importe où je veux, à n'importe quel moment je veux. Ce qui a eu un impact positif sur de nombreux aspects de ma vie. Cela m'a permis de dormir mes 8 heures plus ou moins chaque nuit. Cela m'a permis de trouver une routine d'entraînement plus constante. Cela m'a permis de trouver plus de temps pour les personnes qui comptent pour moi. Et de travailler tout en voyageant.

Cependant, du côté négatif, cette liberté a souvent rendu le processus assez solitaire. Même en travaillant parmi des gens dans des cafés et des espaces de coworking, l'absence de véritables coéquipiers pour partager les hauts et les bas a été cristalline.

En termes de défi et de développement personnel, je trouve que le projet m'a appris en seulement 6-7 mois ce qui m'aurait probablement pris au moins quelques années dans n'importe quel emploi normal. Il m'a essentiellement rendu meilleur développeur dans tous les domaines, y compris :

* Qu'il a ouvert une porte non seulement à une, mais à deux nouvelles plateformes numériques (iOS et Android), se traduisant par une augmentation de 3x des plateformes de ma ceinture à outils de développeur.
* Une connaissance approfondie de JavaScript. De nombreux concepts que je tenais pour acquis dans les confins conventionnels d'Ember.js ont dû être réappris.
* Avec peu d'expérience dans React.js avant cela, je sens maintenant que j'ai la plupart des pièces du puzzle en place pour construire de plus grandes applications React ciblant le DOM. Ce qui signifierait une augmentation de 2x des frameworks/bibliothèques JS de ma ceinture à outils de développeur.
* Une introduction à la programmation fonctionnelle et à la philosophie d'immuabilité associée à la gestion d'état avec Redux.
* Des connaissances massives en devops et en gestion de projet.
* De meilleures compétences d'investigation de dépôt lors de la tentative de comprendre des technologies avec une documentation médiocre.
* De meilleures compétences en conception UI/UX.
* Le meilleur de tout, une confiance plus forte que je peux m'enseigner indépendamment n'importe quelle technologie que je veux, et trouver des moyens de contourner tout obstacle qui pourrait apparaître dans cette quête.

Puisque je n'ai aucune expérience ni avec d'autres outils JS natifs mobiles comme [Flutter](https://flutter.io/) ou [NativeScript](https://www.nativescript.org/), ni avec Objective-C, Swift, Java ou Kotlin, je ne tenterai pas de faire une quelconque affirmation sur le fait que React Native est meilleur ou pire que la concurrence.

Mais ce que je peux dire, c'est qu'en tant que développeur web, React Native a rendu la transition vers le mobile très stimulante, enrichissante et globalement fluide. Admettons, la technologie est jeune et loin d'être parfaite. Mais pour ma part, je n'hésiterais pas à l'utiliser à nouveau.

_Merci d'avoir lu ! Comme toujours, si vous avez des questions ou des commentaires, vous êtes les bienvenus pour me contacter dans les commentaires, à charlie.jeppsson1[at]gmail[dot]com ou sur [LinkedIn](https://www.linkedin.com/in/charlie-jeppsson-71315661/). Et si vous êtes un développeur Rails/React expérimenté et intéressé à travailler dans une startup de coworking basée à Stockholm, [Convendum recrute](https://career.convendum.se/jobs/207256-software-development-manager?promotion=84919-trackable-share-link-medium-app-article) !_