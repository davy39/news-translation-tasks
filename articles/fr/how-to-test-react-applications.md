---
title: Comment tester les applications React
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-05-25T16:46:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-react-applications
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/reacttesting.png
tags:
- name: React
  slug: react
- name: youtube
  slug: youtube
seo_title: Comment tester les applications React
seo_desc: 'React is one of the most popular frontend JavaScript frameworks. If you
  want to make sure that your React apps work as intended, it is important to write
  comprehensive tests.

  We just published a React testing course on the freeCodeCamp.org YouTube ch...'
---

React est l'un des frameworks frontend JavaScript les plus populaires. Si vous voulez vous assurer que vos applications React fonctionnent comme prévu, il est important d'écrire des tests complets.

Nous venons de publier un cours sur les tests React sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à construire, déployer et tester des applications React.

Nikolay Advolodkin a créé ce cours. Nikolay Advolodkin est un professionnel de l'informatique expérimenté, un expert en automatisation des tests et un instructeur populaire en tests avec Ultimate QA.

Dans ce cours, vous apprendrez à utiliser React Testing Library, à écrire des tests visuels de bout en bout et à développer des stratégies de test complètes. Vous apprendrez également à utiliser des outils de test tels que Happo.io, Cypress et Jest.

Tout d'abord, vous apprendrez à créer une application React de base et à la déployer sur Microsoft Azure. Ensuite, vous apprendrez à créer une application de rappel d'anniversaire avec des tests complets. Enfin, vous apprendrez à construire et à tester un site web de portfolio.

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/8vfQ6SWBZ-U) (2 heures de visionnage).

%[https://youtu.be/8vfQ6SWBZ-U]

## Transcription

(autogénérée)

Dans ce cours en trois parties, vous apprendrez à coder, déployer et tester trois applications React.

Nikolay est le fondateur d'Ultimate QA, et est un instructeur populaire sur les tests logiciels.

Pensez à laisser un commentaire avec des conseils sur les tests React que vous avez appris dans ce cours, nous allons commencer le premier tutoriel en créant une application React très simple en utilisant create-react-app.

Ensuite, nous allons utiliser React Testing Library pour écrire quelques tests unitaires.

Par la suite, nous allons apprendre à écrire des tests visuels de bout en bout.

Et enfin, nous allons prendre cette application et la déployer sur Microsoft Azure.

Dans la deuxième partie du tutoriel, nous allons apprendre à créer une belle application de rappel d'anniversaire avec des données statiques.

Ce sera très simple, mais nous allons construire sur les compétences que nous avons apprises dans le premier tutoriel.

Ensuite, nous allons réfléchir à une stratégie de test complète pour cette application web.

Et enfin, nous allons écrire ces tests et les exécuter contre notre application web de rappel d'anniversaire.

Dans le troisième et dernier tutoriel, qui est en fait mon préféré.

Et je pense que vous allez vraiment l'apprécier aussi, vous allez construire un beau site web de portfolio de développeur que vous pourrez utiliser pour montrer vos compétences de développeur.

Nous allons coder beaucoup de composants différents pour cette application web.

Mais le tutoriel sera principalement axé sur une stratégie de test, vous apprendrez beaucoup d'outils très cool comme POJO, Cypress et Jest pour les tests de composants et les tests unitaires.

Je m'appelle Nikhil Avalon skin, et je suis un architecte de solutions senior et je crée des tutoriels sur la chaîne YouTube Ultimate QA.

C'est là que les développeurs viennent apprendre à tester et que les testeurs viennent apprendre à développer.

Alors, qu'attendez-vous, plongeons directement dans les tutoriels.

D'accord, alors commençons à créer notre application React, vous pouvez voir que je suis ici dans un dossier appelé react web up, nous n'avons qu'une licence et un readme.

Alors, allons-y et faisons un NPM init pour configurer ce répertoire.

Et maintenant nous avons ajouté notre package.json.

Si vous ne l'avez pas déjà installé, assurez-vous d'installer create-react-app, c'est un moyen facile de créer des applications React depuis Facebook.

Une fois que vous avez installé create-react-app, vous pouvez en fait utiliser create-react-app pour créer une nouvelle application React.

Alors, allons-y et faisons cela.

Et nous appelons cette application mon application.

Magnifique.

Une fois que le téléchargement et l'installation sont terminés, vous pouvez voir une série de commandes que create-react-app nous fournit pour commencer et elles nous disent exactement ce que nous pouvons faire, c'est de faire un CD vers mon application.

Et ensuite dans mon application, vous pouvez voir maintenant si nous l'ouvrons, nous avons maintenant un dossier mon application, qui a ses propres modules de nœud, a un tas de code ici que nous explorerons dans un moment.

Alors, allons-y et démarrons notre application et voyons à quoi cela ressemble.

Et voici le début de notre petite application merveilleuse qui tourne sur localhost 3000.

C'est aussi indiqué dans les logs ici.

Alors, la chose vraiment merveilleuse à propos de create-react-app est non seulement qu'il construit une application prête à l'emploi et prête à être modifiée.

Il vient même avec un test que nous pouvons exécuter.

Si nous regardons package.json, nous pouvons voir que si nous exécutons une commande NPM test, elle va exécuter quelques tests.

Et donc ce que nous pouvons faire est d'ouvrir un nouvel onglet ici et de faire NPM test.

Et cela va exécuter un test unitaire ici que nous avons dans app.test.js.

Et ce test utilise en fait React Testing Library.

Mais ce que vous pouvez voir ici, c'est que nous avons un test et qu'il va rendre le lien Learn react.

Ici, nous utilisons une méthode appelée render et nous rendons notre composant d'application et ensuite vous pouvez voir que nous utilisons l'écran pour obtenir un élément par texte appelé Learn react.

Et enfin, nous nous attendons à ce que l'élément de lien soit dans le document.

C'est une simple attente et être dans le document est l'assertion de React Testing Library.

C'est fantastique, car maintenant nous avons un test unitaire qui est déjà prêt pour nous.

Et il peut s'exécuter, que notre application soit en ligne ou non.

Donc, si je ferme notre application, puis que je reviens ici et que je réexécute les tests, ils continueront à fonctionner car ils n'ont pas besoin d'un serveur, nous allons en fait pousser cela dans CI.

Le moyen le plus simple de commencer avec GitHub actions est de venir ici dans l'onglet Actions de votre dépôt GitHub, en vous assurant que vous en avez créé un.

Ensuite, vous pouvez venir et dire, un nouveau workflow.

GitHub actions vous fournira quelques workflows suggérés, et ensuite il remarque qu'il remarque que nous utilisons évidemment no J S.

Et donc il peut nous recommander un workflow potentiel.

Et celui-ci ici semble fantastique.

Alors, allons-y et cliquons dessus, il vient déjà avec une série d'étapes qui ont été configurées pour nous.

Et l'autre chose sympa à propos de la création de votre fichier Yamo ici est que vous obtenez également un petit IDE que vous pouvez utiliser, par exemple, vous pouvez voir que si nous ne faisons pas quelque chose, bien, comme, disons que nous faisons quelque chose comme ceci, l'UI met automatiquement en évidence tout ce qui peut mal tourner.

Et donc il dit que nous manquons d'un runs on ici.

Et donc nous pouvons faire runs on et maintenant il dit que la valeur ne peut pas être nulle, et ensuite c'est là que vous fournissez la valeur.

C'est à quoi notre pipeline CI devrait ressembler.

Et passons-le en revue étape par étape, d'ailleurs, vous pouvez voir qu'il est automatiquement créé dans un dossier dot GitHub slash workflows, et ensuite vous donnez un nom à votre fichier, j'appelle notre CI, pipeline CI, vous pouvez bien sûr l'appeler comme vous voulez.

Et ensuite tout en haut, je définis trois variables d'environnement.

Ces variables d'environnement sont la clé API screener, le nom d'utilisateur sauce et la clé d'accès sauce, elles proviennent d'une variable Secrets qui fait partie de GitHub actions, et ensuite proviennent de la clé appelée clé API screener ici, nom d'utilisateur sauce et clé d'accès sauce, donc la valeur d'ici est récupérée et stockée dans la variable d'environnement du côté gauche.

D'où viennent ces valeurs ? Laissez-moi vous montrer que c'est très intuitif dans GitHub actions, vous allez dans Paramètres.

Faites défiler jusqu'à secrets, vous pouvez voir que j'ai trois clés qui ont été créées ici et à l'intérieur, elles ont les valeurs correspondantes qui seront ensuite définies ici.

D'accord.

Ensuite, nous disons que nous voulons que ce CI s'exécute sur les demandes de push et de pull lorsque nous le faisons sur la branche master, la branche principale.

Ensuite, ici, nous définissons les jobs que nous voulons exécuter, nous disons que nous allons exécuter sur Ubuntu latest, il existe plusieurs types de différentes machines virtuelles disponibles pour vous exécuter.

Et je vais exécuter sur Node version 14, vous pouvez exécuter sur d'autres versions de node si vous le souhaitez, bien sûr, et ensuite nous utilisons les étapes.

Beaucoup de ces étapes nous ont été fournies précédemment.

Et j'ai apporté quelques modifications pour vous aider à démarrer plus rapidement avec votre pipeline CI.

Donc la toute première chose que nous voulons faire est d'installer les dépendances.

Et ici nous faisons exactement ce que nous faisions dans notre ligne de commande pour notre application.

Et donc nous aurions fait CD mon application, bien et ensuite fait un npm install.

Cependant, j'utilise simplement un NPM CI, qui est en fait plus rapide dans GitHub actions car il finit par mettre en cache notre dépendance.

Donc c'est l'action recommandée à prendre dans CI.

Ensuite, nous allons construire l'application, bien, cela consistait simplement à semer mon application et à faire un NPM run build pour nous assurer que nous avons une version de production.

Parce que chaque fois que nous faisons un npm start ici.

Et notre application apparaît ici dans localhost 3000.

Et nous jetons un coup d'œil à nos outils de développement React, nous pouvons voir qu'il est rouge, et il dit que cette page utilise la version de développement de React, que nous ne voulons évidemment pas utiliser pour la production, nous voulons utiliser celle-ci.

Nous voulons utiliser la version de production.

Et c'est ainsi que vous le faites avec NPM run build.

Ensuite, nous exécutons nos tests de composants.

Après que notre application soit construite, nous faisons simplement la même chose en naviguant vers ce répertoire et en exécutant les tests exactement comme vous l'avez vu auparavant.

Et enfin, nous démarrons notre application, nous démarrons en fait le serveur en faisant npm start, puis nous faisons une commande wait on qui attendra que l'application démarre pendant jusqu'à 60 secondes avant de générer une erreur.

Et nous allons développer ce pipeline à mesure que nous développons nos tests.

Une fois qu'il est prêt, la seule raison pour laquelle je recommande que vous utilisiez l'UI était de vous aider avec l'IntelliSense.

Mais en fin de compte, la meilleure façon de le faire est de venir à mon application, et ensuite de nous assurer que nous allons ajouter un dépôt GitHub en allant faire cela GitHub slash workflows.

Oups.

Et ensuite nous allons ajouter un nouveau fichier ici.

Si vous appréciez ce tutoriel et souhaitez soutenir cette chaîne, n'oubliez pas de cliquer sur le bouton pouce vers le haut pour la vidéo.

Et si vous souhaitez être informé chaque fois qu'un nouveau tutoriel est publié, cliquez sur le bouton s'abonner.

Appelons-le CI dot Tamil.

Il ressemblera exactement à ce que je vous ai montré ici, j'ai en fait nommé les deux CI deux afin que nous puissions voir, quittons nos tests et faisons un push.

Et une fois que nous faisons un push, cela devrait commencer à exécuter notre pipeline CI.

Venez et jetons un coup d'œil à cela.

Nous verrons que j'ai cette nouvelle branche ouverte.

Alors, allons-y et faisons une PR avec cette branche.

J'ai fait une erreur ici, j'aurais dû mettre GitHub workflows à la racine, pas à l'intérieur de mon application.

Donc ce que vous verrez, c'est que je l'ai déplacé à l'emplacement correct et j'ai fait un autre push.

Et maintenant nous avons un pipeline CI qui a commencé à s'exécuter, voici le nom appelé CI deux exactement le nom que nous lui avons donné dans le fichier Yamo.

Et il a échoué après neuf secondes.

Alors, allons-y et regardons exactement ce qui s'est passé.

Donc l'erreur dit que nous ne pouvons installer des packages qu'avec un package lock JSON, ou NPM, shrimp crab JSON.

Alors, allons-y et corrigeons cela.

Pour ce faire, ce que nous devons faire est de venir à mon application et de faire un npm install.

Ce qui créera un package lock dot JSON.

Et ensuite, allons-y et ajoutons-le.

Et nous pouvons regarder notre ci rerun.

Ici, vous pouvez voir que nous venons de commettre il y a 14 secondes, voici un petit cercle jaune qui montre que notre pipeline CI est en cours d'exécution.

Allons-y et regardons les détails.

Magnifique, donc voici notre pipeline CI qui non seulement peut construire notre application et la démarrer, mais aussi exécuter des tests de composants contre elle.

Donc si nous regardons où nous en sommes dans notre parcours de test, vous pouvez voir basé sur ce tableau que nous avons en fait un long chemin à parcourir avant que notre application soit entièrement testée.

C'est une application vraiment minuscule que nous n'avons même pas apporté de modifications fonctionnelles.

Et jusqu'à présent, la seule chose que nous savons sur cette application sans la tester manuellement est qu'une URL avec le texte correct existe dans le DOM de l'application.

Nous l'avons validé avec un test de composant, qui est venu avec notre application create react app.

Et nous l'avons fait en utilisant React testing library in jest.

Et si nous connaissions réellement l'URL correcte, n'est-ce pas ? Elle peut être là avec les bonnes balises mais ne va pas au bon endroit.

Alors, allons-y et écrivons un autre test pour cela.

La toute première chose que nous voulons faire est de nous assurer que nous exécutons nos suites de tests ici et ensuite nous pouvons ajouter un test qui ressemble à ceci, où nous disons où nous testons qu'une URL est correcte en rendant notre composant avant d'obtenir notre élément de lien comme avant.

Cependant, maintenant nous allons valider que le href de l'élément de lien contiendra ultimate qa.com, car c'est là que nous voulons que notre URL navigue.

Et une fois que nous avons sauvegardé, regardez cette fenêtre en bas à droite.

Elle va exécuter tous les tests de ce fichier.

Ici, le premier a réussi, ce qui est logique, mais le second a échoué, l'URL est correcte.

Il dit que nous attendions ultimate qa.com.

Mais nous avons obtenu react J s.org.

Et c'est parce que nous devons apporter une mise à jour à notre application pour aller sur ultimate qa.com.

Alors, venons ici et allons à app Jas.

Et nous allons changer l'URL en ultimate qa.com.

Nous allons sauvegarder, nos tests vont se réexécuter, et maintenant les deux ont réussi.

De plus, pendant que nous sommes ici, ce texte de lien n'est plus correct, car nous n'allons pas apprendre react, au lieu de cela, nous allons apprendre les tests.

Alors, mettons apprenons les tests, et le dessus et sauvegardons maintenant.

Et nos tests ont tous les deux échoué.

Et la raison pour laquelle ils ont tous les deux échoué est que nous pouvons regarder nos logs.

Et il semblait qu'il était incapable de trouver un élément avec le texte, apprendre react.

Et ensuite, il crache le DOM pour nous ici en montrant tout ce qui est visible.

Et bien sûr, c'est le texte qui existe.

Cependant, cet exercice nous a également montré que le fait d'avoir du texte comme vérification dans notre test n'est pas vraiment une bonne stratégie car nous pouvons souvent changer le texte de nos liens.

Et donc nous pouvons utiliser une meilleure stratégie comme fournir un attribut data dash.

Et donc ici nous pouvons faire un data dash Test ID.

Et nous pouvons l'appeler un learn link.

Nous allons sauvegarder ici, nous allons revenir à app dot test.

Et maintenant, au lieu d'obtenir par texte, nous pouvons obtenir par ID.

Alors, allons-y et faisons cela.

Donnons-lui un run.

Et maintenant tout passe car nous obtenons notre élément par Test ID.

Et bien sûr, si nous décidons de changer le texte, nos tests continuent de fonctionner.

Allons-y et poussons cela dans notre CI.

Voici notre commit.

Et voici notre vérification.

Nous pouvons vérifier cela dans un moment.

Donc notre pipeline CI s'est exécuté avec succès, ce qui est merveilleux.

Alors, voyons où nous en sommes dans notre parcours de test.

À ce stade, nous avons maintenant testé que l'URL est correcte.

Maintenant, comment s'assurer que notre application s'affiche correctement, ce que nous pouvons faire avec ce test ainsi que de nous assurer que notre application a l'air correcte sur le web et le mobile en utilisant deux technologies différentes.

Nous allons utiliser WebDriver.

Io et shift right en testant notre application rendue plus tard dans la phase du cycle de développement.

Et nous allons utiliser des instantanés visuels pour vérifier notre application dans différentes résolutions dans le navigateur pour nous assurer que notre application est réactive et qu'elle a l'air correcte sur différents types d'appareils.

Et pour cela, nous allons utiliser les leçons de WebDriver IO.

Tout WebDriver IO, configurons WebDriver IO, vous allez obtenir un menu pratique qui vous permet de décider ce que vous allez faire.

Donc nous allons exécuter dans le cloud en utilisant Sauce Labs.

Oui, ce sera notre nom d'utilisateur, et ce sera notre clé d'accès.

Non, nous ne voulons pas faire cela, ce qui est la valeur par défaut.

Une fois que vous avez sélectionné toutes les options, vous allez maintenant attendre que WebDriver IO installe tous les packages appropriés.

Une fois que toute l'installation est terminée, la seule autre chose que vous devrez installer est le service WD IO sync.

Et donc une fois que vous avez tout installé, voici à quoi ressemble notre package json, tout ce que nous avons ajouté.

Si nous regardons la diff, vous pouvez voir que nous avons quelques services WD i o ajoutés à des fins de test.

WebDriver.

Les tests Io par défaut vont dans le répertoire test specs, et ici j'ai créé un fichier visual.spec.js.

Et ici, nous allons avoir notre test visuel.

Ce test visuel utilise un format standard describe it.

Et ensuite les commandes proviennent de l'objet browser qui est un objet global de webdriverio.

Nous naviguons vers une URL, et ensuite nous exécutons deux commandes importantes.

Tout d'abord, nous faisons it, qui fournira un nom pour l'application que nous testons.

Donc nous pouvons dire, par exemple, mon application react.

Et ensuite, nous allons faire un snapshot.

Cela capture un snapshot de la page que nous voulons tester.

Et donc dans ce cas, c'est notre page d'accueil.

Et donc nous l'appelons page d'accueil.

Donc le fichier de configuration pour WebDriver.

Io se trouve ici.

Et il se passe beaucoup de choses ici.

Mais que nous pouvons regarder seulement les composants importants.

Ici, j'ai créé deux constantes appelées visual options et sauce options où je définis certaines clés API.

Ici, je définis la clé API screener, je fournis un nom de projet, je vous montrerai comment cela se corrèle à l'UI réelle.

Et ensuite je dis de faire défiler et assembler les captures d'écran pour activer cela à vrai afin que lorsque mes applications sont ouvertes, toute la page est défilée et assemblée.

Ensuite, j'active une sauce Connect, qui est un proxy HTTPS qui me permet une connexion sécurisée d'un hôte local aux environnements d'exécution cloud pour screener et Sauce Labs.

Cela nous dit où se trouvent les spécifications pour nos tests.

Et enfin, la partie la plus importante de cela, je dirais, est la configuration pour exécuter sur plusieurs navigateurs et systèmes d'exploitation différents.

Donc je l'exécute sur deux des résolutions de navigateur les plus populaires.

La toute première est celle-ci, sur cette taille de viewport, qui est la plus populaire sur desktop et qui s'exécute sur Windows 10 et Chrome, et ensuite l'autre type de navigateur sur lequel nous exécutons est MacOS Safari sur cette résolution, qui est une taille de viewport iPhone X.

Et bien sûr, nous pouvons avoir beaucoup plus de résolutions ici.

Et ce qui va se passer, c'est que notre spécification visuelle va s'exécuter sur ces deux plateformes en même temps.

Nous pouvons bien sûr l'exécuter.

Nous pouvons exécuter nos tests en utilisant cette commande ici.

Mais au lieu de cela, ajoutons un script de test à notre package json.

Nous pouvons venir ici et ajouter.

Et ensuite, en nous assurant que dans un terminal séparé, vous avez l'application qui s'exécute réellement sur localhost 3000, car elle doit être active pour que nous puissions faire des tests visuels de bout en bout, nous pouvons maintenant exécuter notre commande de test visuel.

À ce stade, nous pouvons voir qu'il exécute deux spécifications.

Et bien sûr, ce sont nos spécifications Safari et Chrome.

Allons voir l'interface utilisateur de screener pour voir ce qui se passe là-bas.

Donc nous pouvons voir que voici notre nouvelle application dash deux que nous avons démarrée.

Il y a actuellement des tests en cours d'exécution.

La construction a échoué.

Et la raison pour laquelle elle a échoué est que nous avons deux nouveaux snapshots que nous n'avons jamais acceptés auparavant.

Ce que screener nous dit actuellement, c'est que, hé, j'ai ces deux snapshots de ces résolutions de cette page ici de la page d'accueil.

Et je ne sais pas s'ils sont acceptables pour vous ou non.

Donc nous pouvons ouvrir chacun d'eux et regarder.

Cela a-t-il l'air bien pour Austin ? Correct ? Oui, c'est le cas, nous pouvons venir ici et définir cela comme une référence.

À partir de ce point, chaque test automatisé va valider contre cette version de la référence.

Et c'était la résolution la plus grande ici.

Et celle-ci nous semble également fantastique.

Allons-y et acceptons-la.

Et donc maintenant, à partir de ce point, de nouvelles exécutions seront effectuées par rapport à ces références.

Ajoutons également cette étape visuelle à notre pipeline CI et voyons cela s'exécuter.

Nous sommes de retour dans notre CI Yamo.

Nous avons ajouté une toute nouvelle étape après que l'application a rendu pour exécuter des tests visuels et effectuer les commandes suivantes.

Allons-y et vérifions tout cela dans Ci et voyons ce qui se passe.

Nous avons une nouvelle commande ici pour ajouter un test visuel.

Et voici notre pipeline CI en cours d'exécution.

Donc voici notre pipeline après exécution, nous pouvons voir que nos tests visuels se sont exécutés avec succès avec une coche.

Et si nous faisons défiler tout en bas, nous pouvons voir que deux tests ont réussi.

Donc la version actuelle de notre application, elle est un peu ennuyeuse, n'est-ce pas, rendons-la un peu meilleure, et voyons réellement la puissance des tests visuels.

Donc nous allons remplacer ce logo par un autre logo en venant dans app dot j s.

Et nous pouvons voir qu'en haut, nous pointons vers un SVG, changeons ce SVG.

Et au lieu de cela, nous allons pointer vers me dot jpg, qui est un beau fichier que j'ai téléchargé.

Donc sauvegardons cela et regardons son application ran there.

Et voici le plus mignon petit chien du monde.

Elle s'appelle Mia.

Et bien sûr, nous pouvons même changer ce lien ici pour son canal B, au lieu d'apprendre les tests, nous pouvons le changer en autre chose, nous pouvons dire, apprendre les tests, avec Nikolai, et Mia.

Fantastique, notre application a été reconstruite.

Et voici à quoi cela ressemble.

Et nous pouvons même exécuter nos tests pour nous assurer que tout fonctionne comme avant, nos tests de composants, tous les deux fonctionnent avec succès, car rappelez-vous, nous avons ajouté cet attribut de test ID Beta.

Et maintenant nous pouvons vérifier ces changements et voir ce qui se passe avec notre test visuel.

Voici notre changement dans GitHub.

Voyons ce qui se passe.

Donc maintenant si nous regardons l'interface utilisateur de screener, nous pouvons voir que notre nouvelle application deux a deux changements, cliquons pour voir exactement ce qui s'est passé.

Et donc ce que screener montre, ce sont deux changements visuels qui se sont produits, car screener utilise une réunion hybride intelligente, ce qui signifie qu'il analyse le DOM et les décalages d'éléments, et identifie exactement les deux éléments que nous avons changés.

Et donc maintenant, il faut décider si c'est un changement valide ou non.

Et oui, c'est un changement valide.

Et cela a l'air fantastique.

Et nous voulons utiliser cela comme la nouvelle version de la référence.

Donc nous allons accepter celui-ci.

En regardant cette page ici.

Nous aimons tous les changements ici aussi.

Et nous pouvons accepter cela aussi.

Et avec tout cela dit, nous sommes assez loin dans notre codage et le parcours de test.

Nous avons validé presque tout sur notre application.

Nous avons validé que l'application s'affiche correctement et que l'application a l'air comme prévu sur le web et le mobile en utilisant nos tests de DOM visuel à la base de données, également connus sous le nom de test Antwuan, et nous l'avons fait avec les technologies suivantes.

Alors, à quel point ce serait génial si nous pouvions en fait déployer cette application et ensuite la tester dans un environnement de production réel ? Eh bien, nous pouvons en fait le faire en utilisant Microsoft Azure.

Et nous allons utiliser leur fonctionnalité Azure static web apps, leur fonctionnalité Azure static web apps est essentiellement un moyen simple de déployer des applications sans avoir à se soucier de l'infrastructure et des régions et d'un tas d'autres choses.

Comme vous le verrez, c'est un moyen très facile de rendre cela possible.

Donc nous allons aller de l'avant et faire cela, afin de le faire, vous allez avoir besoin d'un compte Azure, vous pouvez obtenir votre compte Azure en allant sur azure.microsoft.com.

Et c'est absolument gratuit, vous pouvez vous inscrire gratuitement, puis vous pouvez suivre le tutoriel.

Ensuite, vous allez devoir installer une extension Azure static web apps.

Donc ici dans votre Visual Studio code, vous allez venir dans les extensions, et installer l'extension Azure static web apps.

Une fois que vous avez ajouté vos applications web statiques, vous aurez cette petite icône Azure, vous viendrez là, vous viendrez dans les applications web statiques, et vous cliquerez sur le symbole plus pour ajouter une nouvelle application web statique Azure.

Donc ici, on nous demande de fournir un nom, un nom unique pour notre application web, appelons-la mon application web react.

Nexus, il m'a demandé de sélectionner la configuration, nous avons évidemment un projet React.

Ensuite, il demande où se trouve le code source de notre application, et le nôtre n'est pas à la racine, mais il est à l'intérieur de mon application.

C'est là que tout le code va.

Et enfin, en demandant, où votre application sera construite.

Donc quand nous venons ici, et que nous exécutons NPM build, c'est la version finale de production de l'application qui va ici dans le dossier build.

Et donc ceci est correct.

Et c'est ce que nous allons fournir.

À l'intérieur de notre projet GitHub, nous voyons que nous avons une nouvelle action qui a été ajoutée.

Et elle s'appelle Azure static web apps workflow.

Et essentiellement, Microsoft Azure a ajouté un nouveau fichier Yamo, qu'il appelle ici, Azure static web apps, blah, blah, blah.

Et donc cela a une configuration pour construire et déployer notre application.

Et donc une fois que nous l'ouvrons, nous pouvons regarder tout ce qui s'est passé ici, l'étape la plus longue et la plus importante était en fait la construction et le déploiement de notre projet.

Si nous l'ouvrons, nous verrons un tas de choses qui ont été exécutées.

Mais en fin de compte, la partie la plus importante était celle-ci à la fin ici, où notre application web a été déployée à cette URL, qui a été générée dynamiquement pour nous.

Et si nous cliquons sur cette URL, nous verrons que voici notre belle et merveilleuse application en vie en production.

J'ai dû ajouter une autre chose ici, quand j'ai vérifié dans le code, il y avait un settings dot JSON qui est venu avec.

Voyons si je peux le trouver ici.

Cela est venu avec.

Et donc ce qui était très, j'avais besoin de pousser cela dans ma pull request aussi.

Et ce JSON de paramètres a juste ces trois choses configurées aussi.

Et puis une fois que je pousse cela, le projet fonctionne avec succès, nous pouvons aussi parler de ce fichier ici qui a été ajouté pour nous.

Il a beaucoup de choses qui se passent, ce qui n'est vraiment rien d'important.

Ce qui est la partie la plus importante ici est essentiellement que ces trois paramètres parlent de l'endroit où se trouve notre application et où la sortie de construction est créée.

Et donc dans ce cas, il construit et déploie simplement notre travail.

Je n'ai pas configuré tout cela, cela a été fait automatiquement pour moi, ce qui est vraiment fantastique.

Et puis ici à la fin, il y a juste une fermeture de la demande de pull request qui, une fois qu'une demande de pull request est fermée.

Elle fermera essentiellement le travail pour nous.

Donc c'est vraiment tout ce qui a été ajouté ici pour nous, automatiquement en utilisant les applications web statiques Azure.

Maintenant, comment écrivons-nous les tests pour notre environnement de production, allons-y et faisons cela.

Donc la toute première chose que je veux faire ici est en fait mettre à jour notre application.

Donc si vous exécutez npm start, cette image était correcte, elle peut définitivement être meilleure.

Et donc, améliorons-la dans notre application.

Donc ce que nous allons faire ici, c'est venir à mon application dans la source, nous allons changer l'image pour une meilleure.

Donc ici nous avons Mia, je vais renommer celle-ci en me old.

Et renommer celle-ci en meow, vous pouvez voir que celle-ci est beaucoup mieux de mon petit chien mignon étant violemment attaqué par son petit ami.

Fantastique.

Donc évidemment, cela va maintenant se charger dans notre application.

La voici, une image beaucoup meilleure.

Et donc, avec ce changement fait, nous devons également mettre à jour notre pipeline Azure pour pouvoir gérer tous les tests.

Et pour ce faire, nous faisons simplement tout ce que j'ai fait dans ce fichier.

Et donc c'est essentiellement une fusion du fichier Azure que nous avions avant, qui a été automatiquement créé pour nous par Azure static web apps, et le fichier CI que nous avions avant.

Et donc tout cela, vous l'avez déjà vu, la définition des variables d'environnement, tout cela configuré ici, cependant, maintenant, nous avons un travail de déploiement intégré, j'ai gardé une grande partie de la logique qui était là de Microsoft Azure.

Et ensuite nous avons fait tous nos tests locaux ici.

Donc l'installation des dépendances, la construction de l'application, l'exécution des tests de composants, le démarrage de l'application, l'exécution des tests visuels sur localhost, c'est une nouvelle étape que nous faisions avant, mais je l'ai simplement renommée, l'appelant notre exécution de tests visuels sur un hôte local.

Et vous pouvez voir que nous exécutons NPM, run test visual, qui si nous regardons cela, ici vous pouvez voir que NPM run does pointe vers cette configuration ici.

Et nous allons également avoir test visual prod, qui va exécuter la même configuration, va avoir un niveau de journalisation de débogage plus élevé.

Et il va également pointer vers une URL de base.

Donc continuons ici dans notre Azure, Azure Yamo.

Donc voici l'étape de construction et de déploiement que nous avons obtenue d'Azure static web apps, j'ai littéralement copié et collé cela ici, tout est identique.

Et ensuite la seule partie que j'ai dû ajouter était l'ajout de tests visuels à exécuter sur prod.

Et donc c'est ce script que nous utilisions avant, cependant, nous devons pointer vers une URL différente, et quelle URL allons-nous utiliser ? Eh bien, celle-ci, maintenant que nous connaissons notre URL de production, nous pouvons l'utiliser à des fins de test de production.

Donc revenons ici.

Et nous allons aller à notre package json.

Et nous allons mettre à jour notre script.

Donc nous allons changer notre URL de base pour celle-ci.

Et donc si nous utilisons WebDriver IO, c'est ainsi que nous sommes capables de transmettre ce paramètre ici.

Et nous le définissons sur notre URL de production.

Et ensuite ce travail de fermeture de la demande de pull request reste tel quel.

Et donc maintenant, allons-y et exécutons cela.

Arrêtons cela, voyons nos changements.

Et n'oubliez pas que j'ai renommé notre travail en Azure CI.

Et poussons cela.

Si nous revenons ici aux demandes de pull request, nous voyons que certaines vérifications sont en cours d'exécution.

Jetons un coup d'œil à celles-ci.

Donc voici notre pipeline Azure CI que nous venons de créer en mettant à jour le fichier Yamo.

Cliquons sur les détails.

Et maintenant nous allons voir toutes les étapes.

Et regardons-les s'exécuter, puis voyons le résultat final.

Oh, quelque chose est arrivé à notre pipeline CI, il semble que les tests visuels ont échoué sur localhost.

Savez-vous pourquoi ? Nous allons le découvrir dans un moment.

Donc la raison pour laquelle nos tests ont échoué sur localhost est parce que, rappelez-vous, nous avons apporté une modification à l'image.

Et donc maintenant si nous revenons ici à screener, nous voyons que deux ont changé.

Si nous regardons les changements, nous voyons évidemment que l'image a changé.

Donc c'est bien pour nous.

Nous n'avons pas à nous en soucier.

C'est absolument la nouvelle version que nous voulons dans notre application.

Nous allons accepter tout ce qui a été sélectionné.

Et ensuite nous allons simplement réexécuter ce travail et maintenant tout devrait passer avec succès.

Magnifique, notre build s'est terminé avec succès.

Alors, allons-y et regardons tout ce qui s'est passé.

C'était juste quelques actions que nous avons déjà vues.

Nous avons vu l'installation des dépendances, la construction de l'application, l'exécution des tests de composants, le démarrage de l'application.

Et ensuite voici les tests visuels sur localhost.

Ceux-ci ont réussi, car nous avons finalement accepté une nouvelle référence.

Oui, nous pouvons voir que l'un a réussi sur Chrome et windows et l'autre sur macOS.

Ensuite, nous avons la tâche de construction et de déploiement ici qui utilisait l'action Azure static web apps.

Et tout cela a réussi avec succès.

Si nous faisons défiler vers le bas, nous pourrons voir l'URL à laquelle elle a été déployée.

Et enfin, nous exécutons nos tests visuels sur la production, ce qui est à peu près la même chose.

Sauf que nous exécutons simplement un script différent, écrire un test de visual prod.

Et vous pouvez voir la configuration WebDriver i o qui a été activée ici, pointant vers cette URL à laquelle nous avons publié et les tests là ont réussi avec succès.

Et c'est à peu près tout, nous avons créé avec succès un pipeline CI qui non seulement teste notre application, mais la déploie ensuite en production et la reteste, vous pouvez maintenant aller de l'avant et gagner 100 millions de dollars avec cette application.

Donc pour résumer, dans ce tutoriel, nous avons créé une application web react très simple en utilisant create react app.

Nous avons ensuite créé des tests de composants en utilisant React testing library.

Par la suite, nous avons décalé à droite, en créant des tests visuels automatisés, en utilisant screener et WebDriver.

Nous avons ajouté le code à un pipeline CI en utilisant GitHub actions.

Et enfin, nous avons utilisé Azure static web apps pour publier facilement tout ce code dans le cloud Microsoft Azure.

Donc c'est notre application qui vit dans l'environnement de production.

Et nous pouvons la tester.

Je m'appelle Nikolai Bulacan, vous pouvez en apprendre plus sur moi sur ultimate qa.com.

Et ce fut un vrai plaisir de pouvoir vous montrer toutes les compétences pour passer une merveilleuse journée.

Hey, et bienvenue dans la construction d'une application de rappel d'anniversaire avec React js.

Dans ce tutoriel, nous allons coder une application React à partir de zéro.

Ensuite, nous allons considérer une stratégie de test merveilleuse pour l'application.

Et enfin, nous allons implémenter un seul test qui va nous fournir une tonne de couverture sur notre application web.

Je m'appelle Nikolai adelakun.

Et sur cette chaîne, j'aide les développeurs du monde entier à construire, tester et déployer des applications de manière continue.

Si vous voulez plus de contenu amazing comme celui-ci, assurez-vous de cliquer sur le bouton pouce vers le haut, afin que je continue à créer du contenu pour vous.

Alors, prenez votre ordinateur, prenez votre café, et faisons cela.

D'accord, alors vous êtes prêt à commencer, laissez-moi mettre mes lunettes de codage magiques.

Et commençons.

Donc la base de code sur laquelle nous allons travailler va provenir de ce projet ici.

Vous pouvez voir qu'il s'agit d'un fork de ce autre projet qui contient un tas d'applications web React.

Et nous construisons sur celles-ci en enseignant comment les tester et les déployer.

Nous allons travailler sur ce rappel d'anniversaire, il y a deux dossiers ici, il y a un dossier de configuration.

Et il y a un dossier final.

Le dossier final est essentiellement à quoi le code va ressembler à la fin.

Et le dossier de configuration est celui avec lequel vous allez travailler.

C'est un dossier vide pour vous aider à démarrer.

Et il va avoir un peu de code de base dedans.

Et ensuite nous allons coder le reste.

Alors, laissez-moi vous montrer exactement à quoi cela ressemble.

Bien sûr, la première étape, vous allez obtenir le clone.

Vous pouvez, si vous le souhaitez, forker mon projet, puis faire un git clone.

Et une fois que vous avez cela, vous naviguerez vers le répertoire final.

Donc je vais juste faire cela et ensuite je vais faire un npm install et start afin que nous puissions voir à quoi ressemblera la version finale de l'application.

D'accord, donc la voici, vous pouvez voir que notre application est en cours d'exécution, bien sûr, et localhost 3000.

Et voici à quoi cela ressemble.

Il montre l'anniversaire.

Donc nous avons aujourd'hui, les personnes dont c'est l'anniversaire.

Et si vous appuyez sur le bouton Clear All, il efface tous les anniversaires.

C'est à peu près tout, l'application est super simple.

Cependant, nous devons commencer quelque part de simple et construire.

Et en cours de route, nous allons découvrir non seulement comment le coder, mais aussi comment le tester.

Maintenant que nous savons à quoi ressemble l'application, allons-y et implémentons-la ensemble.

Et ensuite, nous parlerons de la stratégie de test.

Donc je vais le mettre ici, et vous allez me suivre.

Donc vous allez naviguer une route hors de, vous allez naviguer dans setup.

Et c'est là que nous allons travailler aussi, je vais changer pour une nouvelle branche.

Nous allons travailler à partir de birthday tutorial.

Et si vous voulez suivre mes commandes, vous verrez celles-ci dans cette branche.

Donc évidemment, nous avons le dossier source.

Si vous êtes dans setup, vous devrez également faire un npm install.

Pendant que cela s'installe, nous pouvons parler de app J S, vous pouvez voir qu'il n'y a rien ici sauf ce h2 qui dit reminder project set up in this data dot j s, vous verrez qu'il s'agit simplement d'un tableau de métadonnées sur chacun de nos utilisateurs, juste encore, en gardant cela simple, sans avoir besoin de le récupérer de quelque part pour l'instant.

Notre index, CSS a déjà tout le style, bien, nous ne voulons pas passer des heures à mettre en place tout le style de notre application.

Donc il est déjà ici et prêt pour vous, tout ce que nous avons à faire est d'implémenter et je préfère passer plus de temps à implémenter des projets et moins de temps à m'inquiéter du CSS dans index.js.

C'est notre point d'entrée pour notre application.

Et ensuite notre list.js contiendra la liste des utilisateurs.

Et nous allons itérer sur eux.

Et vous verrez exactement ce que nous faisons ici.

Mais en attendant, tout devrait être installé et si vous faites npm start, cela ouvrira notre application.

Et je vais en fait l'ouvrir, nous allons le mettre côte à côte avec notre éditeur.

Donc cela rend la vie plus facile.

Et nous allons le mettre ici comme ça.

Donc vous pouvez voir ce que cela montre en ce moment.

C'est juste notre app J S.

C'est juste un simple fond rose avec un en-tête qui dit reminder, Project Setup.

Allons-y et commençons à coder.

D'accord, alors commençons à faire un peu de travail sur cette application.

Nous allons commencer à travailler à partir de app J S.

Laissez-moi fermer la fenêtre de droite juste pour que vous puissiez voir plus d'espace ici.

Et nous allons fermer cela ici aussi.

Avec cela, nous allons nous débarrasser de ceci.

Et nous allons retourner un bloc de code beaucoup plus grand.

Et maintenant nous allons ajouter un élément main et pourquoi c'est main.

Si nous venons dans notre index CSS, nous verrons que le style pour le composant main est ici.

Cela va être l'enveloppe pour la partie principale de notre application.

Et à l'intérieur de cela, nous allons avoir une section et cette section va obtenir un nom de classe.

Et cela va s'appeler container.

Donc dès que je sauvegarde, vous pouvez voir exactement à quoi cela ressemble.

Encore une fois, si nous regardons index, trouver container, vous pouvez voir que le style CSS pour le container est juste là.

À l'intérieur de cette section, qui est la partie blanche, n'est-ce pas ? Qu'allons-nous avoir là-bas ? Eh bien, nous allons avoir un h3 et cela va afficher la quantité d'anniversaires. Pour l'instant, nous allons tout faire de manière statique puis rendre les choses un peu plus dynamiques.

Donc nous allons faire quelque chose comme ceci, l'enregistrer, boom, voir cela apparaître juste là.

Ensuite, nous allons importer nos composants de liste.

Donc vous pouvez voir que l'importation est déjà en haut à la ligne numéro trois.

Et cela va être généré dynamiquement une fois que nous aurons mis la logique dedans.

Donc pour l'instant, c'est tout ce à quoi cela ressemble car si vous regardez les listes, vous pouvez voir que c'est tout ce qu'il a pour l'instant.

Ensuite, nous allons ajouter un bouton.

Donc bouton, et ensuite nous allons faire une méthode on click, n'est-ce pas ? Qu'est-ce qu'il va faire on click ? Donc qu'est-ce qu'il va faire on click pour l'instant, encore une fois, toujours en gardant cela simple, faisons une fonction anonyme.

Et cela ne va rien faire.

Et au lieu de cela, il va simplement faire une console log.

Comme ça.

Et donnons à ce bouton un titre.

Et sauvegardons cela, et boom, voici notre bouton.

Et si nous venons ici et inspectons, faisons défiler vers le bas.

Allons dans la console, et cliquons dessus, vous pouvez voir qu'il dit clicked car c'était la méthode que nous avons codée.

Au fait, si vous vous demandez comment j'ai rapidement créé une fonction anonyme, c'était un raccourci clavier, a NFN.

Donc vous pouvez taper ceci a et a fan.

Et vous pouvez voir que c'est une fonction anonyme.

Et ensuite quand j'appuie sur tab, j'obtiens ceci généré automatiquement.

Et cela vient de là, c'est cette extension juste là.

Magnifique.

Donc App J S jusqu'à présent est opérationnel.

Maintenant, allons-y et remplissons-le avec les vrais utilisateurs.

D'accord, donc l'étape suivante, nous allons travailler à partir de notre composant de liste.

Notre composant de liste va contenir tous les anniversaires qui proviennent de data Jas, n'est-ce pas.

Donc vous pouvez voir qu'il contient le nom, l'âge, l'image, et un ID.

Et cette liste va simplement itérer sur tout cela et lister ces composants.

Cela dit, débarrassons-nous de cet en-tête.

Et au lieu de cela, nous allons garder le fragment ici, nous allons faire une carte.

Et en fait, ce que nous allons vouloir faire à l'intérieur de cette liste, c'est passer un objet que nous allons appeler people, d'accord, en utilisant cet objet, nous allons ensuite faire une carte.

Et à l'intérieur, nous allons faire une autre fonction anonyme.

Et ensuite nous allons mapper sur une personne.

Et pour chaque personne, nous pouvons déstructurer cet objet avoir un objet déstructuré, et cela va prendre chacune des propriétés de notre personne.

Donc nous avons cette déstructuration.

Ensuite, nous allons vouloir retourner le composant.

Cela va être un article et à l'intérieur de cet article, nous allons avoir une image, nous allons avoir une source d'image.

Vous pouvez voir automatiquement comment ces propriétés déstructurées reviennent ici pour lui donner un alt, il va avoir le nom de la personne.

Magnifique.

Et ensuite en dessous, et ensuite nous allons ajouter une div.

Et cette div va avoir un h4.

Et cela va être le nom de la personne.

Et ensuite nous allons avoir un paragraphe.

Et ensuite cela va dire cet âge et années.

Comme ça.

Et ensuite ici dans l'article, nous voulons définitivement avoir une clé pour la carte, donc cela va être l'ID.

Et ensuite nous voulons lui donner un style, qui va être personne.

Donc encore une fois, si nous regardons index dot css, et que nous cherchons personne, voici le style pour la personne.

Revenons, sauvegardons et voyons exactement à quoi cela ressemble.

Oh, cela a échoué.

Voyons ce qui ne va pas ici.

Et je pense que la raison de cela est que nous n'avons passé aucun objet à notre composant de liste.

Et c'est pourquoi il est indéfini.

Et donc maintenant si nous revenons ici, nous pouvons en fait le définir.

Donc la toute première chose dont nous allons avoir besoin est un tableau déstructuré.

Donc faisons cela.

Et cela va être people set the people.

Et cela va faire use state.

Et il va prendre les données que nous obtenons d'ici.

Les voilà.

Et ensuite en utilisant ces informations, ce que nous allons vouloir faire, c'est évidemment mettre à jour celui-ci en une valeur dynamique.

Donc ce sera people dot length.

Donc maintenant nous allons montrer cela dynamiquement.

Et ensuite notre liste, nous allons en fait vouloir passer la valeur de people.

Et cela va être people.

Magnifique.

Et je pense que c'est correct.

Donnons-lui un run, sauvegardons, boom, la voici, voici notre application, vous pouvez voir exactement à quoi elle ressemble, et comment chacun des composants est entré en jeu depuis la liste.

Donc nous avons tout enveloppé dans un article, chacun de ceux-ci est un article.

À l'intérieur de cela, nous avons une image, et ensuite nous avons le nom de la personne, et ensuite l'âge et les années, il ne reste plus qu'à faire fonctionner le bouton, qui actuellement ne fait que du console logging.

Et faire en sorte que cela se produise est extrêmement facile.

Et cela ne prend qu'une seule méthode.

Donc c'est juste définir les people.

Et à l'intérieur de cela, nous allons simplement passer un tableau vide, ce qui va tout effacer, n'est-ce pas.

Donc si nous sauvegardons cela, et maintenant nous devrions être capables de cliquer sur ce bouton.

Et vous pouvez voir que maintenant il dit vos anniversaires aujourd'hui, évidemment le compteur étant mis à jour à partir de cela, la liste des valeurs des personnes étant passée d'ici à ici.

Et ensuite le onclick utilise la méthode Set people d'en haut, en passant un tableau vide.

Notre application est maintenant terminée, comment la testons-nous ? Nous avons maintenant notre application web qui est là et prête.

Et la question est, bien, comment allons-nous réellement la tester ? Quelle est la stratégie la plus optimale, notre application web contient plusieurs composants qui doivent être testés.

Il y a, par exemple, le compteur d'anniversaire dynamique que nous avons codé, la logique de celui-ci doit évidemment être correcte.

Il y a la fonctionnalité Clear all du bouton qui doit s'assurer que la liste est effacée.

Et puis probablement la partie la plus importante est l'apparence de toute l'application sur le web.

Et évidemment, le mobile est également important.

Alors, comment allons-nous tester notre application pour nous assurer que tout fonctionne comme prévu, alors commençons à travailler à travers la période de test.

Amid et voyons quelle approche a du sens.

Nous allons commencer tout en bas, la couche de test unitaire.

Les tests unitaires sont vraiment excellents pour les types de tests de bas niveau, n'est-ce pas ? Si vous avez des fonctions pour ajouter des entiers, par exemple, ou une fonction qui effectue un certain parsing de certaines données, ces types de tests sont vraiment bons pour les tests unitaires.

Et honnêtement, pour la plupart des applications web React, les tests unitaires sont rarement nécessaires, sauf si vous avez une logique JavaScript profonde que vous devez tester.

Donc les tests unitaires ne vont pas s'appliquer ici parce que nous allons avoir besoin de trop de tests unitaires.

Et aussi, ce n'est pas le bon cas d'utilisation ici.

Ce qui est probablement mieux et plus applicable pour les applications web, surtout en React, ce sont les tests de composants, les tests de composants sont un niveau plus élevé, ils s'assurent que l'apparence et la fonctionnalité fonctionnent ensemble, que le composant que nous avons créé, comme le composant de liste, fonctionne correctement lié à tout le code backend.

Donc si nous avions des tests de composants, nous pourrions avoir un test de composant pour une liste.

Et ensuite cela s'assurerait que lorsque nous récupérons les données du fichier data Jas, elles sont correctement récupérées et affichent le compteur correct, nous pourrions également avoir un test de composant pour le bouton et nous assurer que lorsque nous faisons la méthode onClick, que le bouton effectue l'opération correcte.

Mais qu'en est-il de l'apparence de l'application ? Comment vérifions-nous que cela fonctionne et a l'air correct ? Nous pourrions définitivement passer à un niveau supérieur dans les tests de bout en bout, n'est-ce pas ? Et répondre pour nous assurer que tout, du DOM à la base de données, se comporte correctement.

Nous pouvons, oui, cliquer sur un bouton en utilisant un test Antwan et nous assurer que lorsque le bouton est cliqué, il efface effectivement toute la fonctionnalité.

Cependant, comment nous assurons-nous de la justesse visuelle de l'application ? Et si je vous disais qu'il y avait une stratégie vraiment cool que nous pouvons utiliser, qui va être deux points de validation en un seul test, et nous pouvons nous assurer que la fonctionnalité de notre application est à 100% ? Allons-y et faisons-le.

D'accord.

Donc nous n'avons en fait plus besoin de montrer l'application ici.

Donc nous allons simplement l'arrêter pour avoir un écran plein.

Et les technologies que nous allons utiliser pour nos tests sont WebDriver.

I O et screener.

Donc nous allons en fait effectuer un test visuel de bout en bout qui va nous permettre de rendre toute l'application, de nous assurer qu'elle a l'air correcte.

Et ensuite nous allons effacer toute la liste et nous assurer que cela a l'air correct.

Et avec ces deux points de validation, l'ouverture de l'application, nous assurons qu'elle est dans le bon état, l'effacement du bouton, nous assurons qu'elle est dans le bon état, nous assurerons une couverture à 100% de notre application et nous laisserons savoir que nous sommes super à l'aise que rien ne cloche avec notre application.

Donc allons-y et commençons à installer le code.

Donc nous allons faire NP X, WD, I, O, et O.

Et laissez-moi m'assurer que je suis dans le bon répertoire, donc faisons CD vers un.

Et ensuite nous allons faire CD vers setup.

Et ensuite nous allons faire MPX WebDriver i o comme cela, et ensuite il nous guidera à travers un processus d'installation très convivial.

Il nous permettra de choisir un tas de dépendances.

Pendant qu'il s'installe, je vais vous parler un peu de WebDriver.

Io WebDriver.

Io est, comme il est dit ici, un framework de test d'automatisation de navigateur et mobile de nouvelle génération pour No, Jas.

Il est vraiment bon pour les tests de bout en bout avec le navigateur et le mobile.

Donc si vous cherchez une solution qui peut gérer le web et le mobile en même temps, plus il a d'autres capacités comme pouvoir se brancher avec des outils de test visuel de bout en bout tels que screener WebDriver.

Io est l'outil qu'il vous faut.

Ensuite, nous allons répondre à quelques-unes de ces questions.

Où se trouve le backend d'automatisation ? Nous allons utiliser l'exécution dans le cloud en utilisant Sauce Labs parce que Sauce Labs est intégré dans screener et nous allons avoir besoin de Sauce Labs.

J'ai un compte si vous n'en avez pas alors allez-y et inscrivez-vous sur sauce labs.com.

Prenez votre compte gratuit là.

Et je vous montrerai comment le configurer.

Il me demande déjà les variables d'environnement pour mon nom d'utilisateur et ma clé d'accès pour Sauce Labs.

Et oui, les miens sont enregistrés dans sauce username et access key dans mon profil bash comme ça.

Non, nous ne voulons pas exécuter des tests headless.

Dans quelle région allons-nous faire us, quel framework Mocha est bien.

Il y a aussi des options Jasmine et cucumber.

Maintenant, nous n'avons pas de compilateur, vos spécifications sont situées par défaut sur simplement en appuyant sur Entrée pour la plupart de celles-ci.

Oui, laissons WebDriver IO générer quelques fichiers de test pour nous, juste pour que nous puissions voir à quoi ils ressemblent, les objets de page.

Non, merci.

C'est beaucoup trop.

Pour nos besoins de test ici, le rapporteur de spécifications est totalement bon.

Et ensuite les services que nous allons installer, le service sauce, nous n'avons pas besoin du service chrome driver, le service chrome driver est pour exécuter des tests localement, inutile pour nos besoins, car nous allons seulement utiliser un seul test visuel de bout en bout pour résoudre tous nos problèmes.

Et ensuite je vais appuyer sur entrée ici base URL et installer, je ne sais pas ce que c'est à propos de taper à la caméra.

Vous, les gars, me rendez nerveux.

Chaque fois que je dois taper à la caméra, j'oublie comment taper.

D'accord, magnifique.

Donc il dit que le projet a été configuré avec succès.

D'accord, dans le rappel d'anniversaire setup, laissez-moi juste vous montrer quelques-unes des choses qui ont été ajoutées.

Package dot JSON a évidemment été mis à jour avec WebDriver I O.

Nous avons également obtenu la configuration pour WebDriver I O.

Et nous avons obtenu un exemple de test.

Ici, ouvrons-le pour que nous puissions voir à quoi cela ressemble.

C'est un test très simple, naviguer vers cette URL, et ensuite il semble qu'il se connecte.

Donnons-lui un essai en utilisant npm.

Exécuter WD IO.

Et nous verrons exactement à quoi cela ressemble.

Donc cela démarre.

Ouvrons Sauce Labs ici.

D'accord, donc nous voyons qu'il y a une minute, j'ai juste exécuté appelé mon application de connexion.

Et nous pouvons l'ouvrir.

Et la partie la plus cool est de simplement exécuter la vidéo et de voir exactement ce qui s'est passé.

Donc la voici, voici notre test de bout en bout fonctionnel.

Donc nous savons que notre environnement est configuré, l'étape suivante que nous devons faire est de configurer screener afin que nous puissions faire des tests visuels de bout en bout au lieu de tests fonctionnels de bout en bout.

Donc parlons de la configuration pour WebDriver I O et comment l'intégrer avec screener.

Tout en haut, j'ai configuré un objet visual options.

Et il prend une clé API et un nom de projet, la clé API provient de screener, je vous montrerai dans un moment.

Et le nom de projet correspond essentiellement au projet sur lequel nous travaillons.

Et je l'ai nommé birthday reminder, nous avons également des options sauce ici.

Et celles-ci prennent également un nom d'utilisateur et une clé d'accès.

Vous pouvez voir que j'ai trois variables d'environnement ici.

Si vous voulez obtenir vos variables d'environnement dans le compte, les paramètres de l'utilisateur, vous trouverez votre nom d'utilisateur et votre clé d'accès pour sauce et screener, qui est notre outil de test visuel de bout en bout.

Une fois que vous êtes connecté, puis vous allez dans votre compte et cliquez sur my API key.

Vous obtiendrez cette clé API également, sauvegardez-les toutes dans votre profil bash.

Et maintenant nous pouvons facilement faire du CI CD et des tests sur nos machines.

Une grande partie de cela était déjà ici.

Je l'ai simplement nettoyé un peu plus.

Vous pouvez en fait même voir dans ma diff.

Ce que j'ai changé, juste nettoyé, rendu moins verbeux.

Il y a un tas de descriptions qui étaient dans la configuration WebDriver IO pour vous montrer tout ce qui se passait.

Mais les composants les plus importants sont cette partie de service que j'ai ajoutée.

Cela nous permet de créer une connexion sécurisée depuis le cloud screener vers notre machine locale, n'est-ce pas, notre application tourne en localhost.

Et donc ils doivent pouvoir se parler pour effectuer les validations appropriées.

Donc j'ai activé ce service ici, j'ai ajouté ces capacités pour pouvoir pointer vers le hub screener.

Et enfin, j'ai un tableau ici qui me permettra de m'exécuter sur autant de navigateurs et de systèmes d'exploitation que je veux.

Actuellement, je l'ai défini sur deux des résolutions de navigateur les plus populaires.

La toute première est celle-ci, sur cette taille de viewport, qui est la résolution de bureau la plus populaire actuellement.

Et donc je l'ai définie sur cette résolution, définie pour s'exécuter sur Chrome, Windows 10, et la dernière, et ensuite en passant cette taille de viewport, nous pouvons ajouter plus de ces capacités pour nous exécuter sur plus de navigateurs et de systèmes d'exploitation.

Et bien sûr, nous pouvons aussi changer cette partie si nous le voulons.

Donc c'est la configuration, à quoi ressemble le test ? Revenons au test qui m'a montré, laissez-moi vous le montrer ici.

Voici à quoi ressemble le test.

Il est utilisé comme un format standard describe it, je dis décrire mon application de rappel d'anniversaire qu'elle devrait avoir l'air correcte.

Ensuite, nous naviguons vers une URL, ici, je ne spécifie rien, car l'URL de base est définie dans la configuration WebDriver.

Io, laissez-moi vous montrer où cela se trouve, c'est ici en bas.

Ensuite, nous avons une commande init.

Au fait, toute cette documentation est disponible ici dans Docs, visual, et Docs, vous pouvez suivre là-bas, cela vous aidera à vous installer.

Mais bien sûr, je suis ici pour expliquer aussi, cela va simplement démarrer l'exécution pour le test.

Et ensuite, l'une des pièces les plus importantes est la capture de l'instantané.

Donc ici, je capture un instantané et je l'appelle l'état par défaut car il dit initialement lorsque notre application s'ouvre.

Ensuite, après son ouverture, je vais cliquer sur notre bouton.

Ce que j'ai fait ici aussi, c'est ajouter un attribut data Test ID pour rendre notre bouton plus unique.

Et donc pour que cela soit possible, nous devons revenir à app J S.

Et dans notre bouton, nous allons ajouter un attribut data Test ID, en l'appelant clear.

Donc maintenant notre bouton a cet ID de test unique que nous pouvons utiliser à des fins d'identification.

Et nous allons cliquer dessus.

Donc maintenant, cela efface évidemment notre application, et ensuite nous allons capturer un autre instantané de l'application.

Et ensuite nous allons mettre fin à notre test et nous assurer qu'il n'y avait aucun message dans notre objet de résultats.

Donnons-lui un essai.

Et je pense que vous comprendrez exactement ce qui se passe.

Laissez-moi ouvrir le terminal ici.

Donc nous allons simplement faire NPM, run WD IO, cela va démarrer ici.

Si je n'ai rien cassé, cela va commencer à s'exécuter.

Je pense qu'il est déjà en cours d'exécution, mais donnez-lui un moment.

D'accord, le voici, il s'exécute.

Revenons à screener.

Et ce que nous verrons ici, c'est notre rappel d'anniversaire, nous allons voir qu'il y a actuellement une session en cours d'exécution.

Il s'exécute sur cette résolution.

Voici quelques informations à ce sujet.

Et dans un moment, je vous montrerai ce qui sort de cela.

J'ai fait une petite erreur, il devrait y avoir deux nouveaux états.

Laissez-moi vous montrer ce qui s'est passé, vous voyez comment ici il ne peut pas cliquer sur l'élément data Test ID car il n'a pas été trouvé.

Ce que j'ai fait, c'est que j'ai en fait modifié le mauvais app J S.

Donc nous allons prendre cela et le mettre dans le bon app J S dans le dossier de configuration ici.

Les voilà.

Et maintenant nous allons ajouter ce bouton, qui est exactement ce qui s'exécute, sauvegardons cela maintenant réexécutons ces tests.

Et nous serons de retour dans un moment.

D'accord, les voilà.

Deux nouveaux états viennent d'arriver pour notre application.

Qu'est-ce que cela signifie réellement ? Eh bien, ouvrons-le et voyons ce qui s'est passé.

Regardez ici, vous verrez que sur cette résolution, Chrome 95, Windows 10.

J'ai mon application de rappel d'anniversaire, cette application de rappel d'anniversaire a un état par défaut.

Si nous l'ouvrons, nous voyons notre application de rappel d'anniversaire ici.

À quoi cela ressemble-t-il ? Cela a l'air absolument parfait.

Nous avons le bon nombre d'anniversaires.

Nous avons toutes les bonnes personnes et tout le style est absolument correct.

C'est la meilleure et la plus puissante chose à propos des tests visuels de bout en bout, c'est que nous pouvons capturer l'état et l'apparence de toute l'application en une seule commande.

Et c'est exactement ce que nous avons fait ici.

Et donc nous avons validé tout ce que nous aurions pu avoir besoin de valider dans cet état par défaut, n'est-ce pas.

Et donc cela a l'air bien, nous allons accepter cela, cela sera utilisé comme une future itération de notre nouveau code.

Et ensuite, l'étape suivante est le seul autre état possible de notre application, qui est l'état clair.

Et donc vous vous souvenez, j'ai appuyé sur le bouton Clear All.

Et cela a l'air absolument correct ici aussi.

Donc non seulement nous savons que le bouton Clear All fonctionne correctement, ce que nous aurions pu faire avec un certain nombre de types de tests, ce test garantit également que notre application a l'air bien aussi.

Toute cette logique ici est correcte.

Et donc nous pouvons accepter cela aussi.

Et maintenant, ce que cela signifie, c'est que toute future itération de nos tests contre notre application va valider contre ces références et vérifier, hey, cela a-t-il l'air correct ? Ou quelque chose a-t-il changé ? En fait, si nous voulions faire un changement, disons que nous sommes allés dans data, J, s, et peu importe, enlevons notre tout premier élément.

Enregistrez cela, bien sûr, maintenant, nous n'allons pas avoir cinq.

Et nous voulions, nous pouvons exécuter nos tests.

En fait, regardons d'abord notre application.

Et, regardez, il n'a que quatre personnes maintenant.

Oui.

Et donc si nous réexécutons nos tests, laissez-moi vous montrer exactement ce que cela va nous dire.

Réfléchissez-y.

Si nous relisons nos tests, et qu'il compare à la référence, qui fonctionnalité a changé et qui fonctionnalité reste la même ? Eh bien, le clear all reste exactement le même.

Donc ce test va réussir.

Et ensuite l'état par défaut, cette partie est cassée.

Et nous savons que nous l'avons cassée.

Donc je vais voir ces tests individuels dans un moment.

Le voici, regardez cela.

Exactement.

Comme je l'ai mentionné, un changé, une règle acceptée.

Examinons ce qui a changé.

Vous voyez cela ? Regardez, il identifie exactement ce qui s'est passé.

Un élément supprimé.

Et cela, bien sûr, a changé le texte.

Et donc maintenant nous déterminons si c'est l'état correct de notre application ou si nous avons introduit un bug, dans ce cas, nous avons introduit le bug.

Cela a été rejeté.

Et maintenant nous devons aller et corriger notre application et nous assurer qu'elle a l'air et fonctionne correctement.

Merci beaucoup de vous être joint à moi pour ce tutoriel.

J'espère que vous avez apprécié la construction et le test d'une application de rappel d'anniversaire.

J'ai été Nikolai as of Alaskan.

Donc si vous avez apprécié ce contenu, et que vous voulez me voir construire cette application, allez-y et cliquez sur le bouton pouce vers le haut.

Et si vous voulez être informé des futurs tutoriels vidéo, cliquez sur le bouton s'abonner.

Et enfin, si vous voulez apprendre quelque chose de spécifique autour de react, la construction d'applications et leur test, commentez ci-dessous et je m'assurerai d'apporter ces tutoriels à votre flux YouTube.

Merci encore.

Passez une journée incroyable.

À la prochaine.

Aujourd'hui, nous allons construire un beau site web de portfolio personnel next J S.

Voici à quoi il ressemble si vous naviguez vers Nikolai dot tech, vous pourrez voir une version live de l'application.

Vous pouvez voir à quel point il est beau.

Tout ici est fonctionnel.

Ces icônes vous mèneront à différentes ressources que vous voulez que les gens connaissent de vous.

Et si vous faites défiler vers le bas, vous verrez une collection de tous les projets que vous avez réalisés.

Vous pouvez mettre ici vos projets de test, vos projets de développement, tout ce que vous avez fait avec la communauté.

Tout en bas, vous verrez les technologies que vous maîtrisez et vous pourrez les montrer à vos employeurs potentiels.

Il y a une petite section pour vous décrire et qui vous êtes, et même montrer une chronologie de votre expérience et de vos accomplissements.

Et tout en bas, nous verrons une section d'accomplissements personnels qui décrit certaines des choses que vous avez pu réaliser dans votre carrière incroyable.

Il y a même un lien sur lequel vous pouvez cliquer et quelqu'un pourra vous envoyer un email, bien sûr, il est également important que ce site web soit absolument totalement réactif.

Donc dans un monde où le mobile est prioritaire, il est absolument inacceptable aujourd'hui d'avoir un site web qui n'est pas réactif, et vous pouvez voir à quoi ressemble notre vue mobile, tout a l'air merveilleux, c'est facile à lire, facile à voir, vous pouvez interagir avec tout.

Si vous voulez voir une application, vous pouvez cliquer sur l'application, et ensuite elle vous y emmènera.

D'accord, avec tout cela dit, plongeons dans la construction et le test de cette application.

Donc, allons-y et récupérons le code.

Donc vous pourrez trouver le code à ce dépôt.

Et pendant que vous y êtes, veuillez donner une étoile au dépôt.

Et ensuite vous pourrez obtenir la version finale du portfolio ici dans ce dossier dev portfolio.

C'est là que vit tout le code.

Donc si vous le téléchargez et démarrez le serveur, vous pourrez voir une version live de l'application.

Et j'ai même créé une version de départ du code pour nous.

Donc si vous allez dans les branches, et recherchez dev, portfolio, start branch net, et ensuite vous pouvez télécharger ce code, allez dans code et téléchargez zip, vous pourrez obtenir une version de départ de l'application.

Si vous entrez ici, vous verrez qu'elle est basique, elle n'est pas entièrement terminée.

Mais c'est un excellent point de départ pour nous et éviter beaucoup de la configuration de base inutile.

Lorsque vous téléchargez cette branche, vous pouvez démarrer votre propre projet, bien sûr.

Et une fois que vous démarrez ce projet, il suffit de placer tous les dossiers dans votre nouveau projet.

Et c'est exactement à quoi cela va ressembler.

En fait, ce que vous pouvez faire, c'est d'abord faire un npm install.

Et ensuite après avoir fait un NPM, install NPM run Dev.

Et ce que vous verrez, c'est qu'il va en fait démarrer notre application sur localhost 3000.

Donc, ouvrons cela ici.

Et voici notre application de départ, ce que vous pouvez voir, c'est qu'elle a un style basique, et elle a tous les composants que nous allons coder ensemble.

Donc l'en-tête, le héros, et ainsi de suite.

Vous pouvez voir dans notre package json, nous avons toutes les dépendances que nous allons utiliser tout au long du tutoriel déjà configurées.

Et ensuite si nous jetons un coup d'œil au code source, vous verrez que les composants basiques ont été écrits.

Par exemple, voici à quoi ressemble un composant accomplishments.

Déjà, vous pouvez voir qu'il ne contient qu'un Dave qui dit accomplishments.

Et bien sûr, cela correspond à ce composant, et ainsi de suite.

Donc chaque composant est déjà créé ici, juste avec un Dave basique qui affiche le texte.

Et ce que vous remarquerez également, juste pour rendre ce tutoriel beaucoup plus divertissant et avancer plus rapidement, c'est que nous avons déjà créé tous les styles.

Donc vous pouvez voir que les styles pour chacun des composants sont configurés ici via CSS.

Donc tout ce que nous allons avoir à faire, c'est coder l'application réelle et utiliser les styles là où c'est approprié.

Et nous n'allons pas réellement avoir à écrire du CSS.

Je garde également un readme ici pour votre portfolio personnel avec tous les liens et informations pertinents tels que le lien vers un site web personnel, comment commencer et beaucoup d'autres informations qui peuvent être utiles pour votre parcours de développement et de test.

Donc avec tout cela dit, entrons et commençons à construire notre site web de portfolio personnel.

Donc, allons-y et créons notre tout premier composant, qui sera notre composant d'en-tête.

Généralement, il est plus facile de commencer par le composant le plus simple.

Donc nous avons navigué ici vers notre fichier header J.

S file.

Et allons-y et nous allons retourner un conteneur.

Et à l'intérieur de ce conteneur, nous allons déposer une div.

Voici à quoi ressemblera cette div.

Nous allons transformer cela en une span.

Et donc cette div provient de nos composants stylisés ici.

Vous pouvez voir ici le style qui est appliqué à cette div one, et ensuite nous allons avoir un lien ici, le lien pointe vers cette page d'accueil.

Et ensuite nous avons cette icône de vérification CSS gi, qui provient de react icons For slash di, et ensuite nous ajoutons une span qui s'appelle portfolio.

Si nous sauvegardons cela, faites attention à ce qui se passe à droite, nous avons maintenant cette icône qui est cliquable.

Si nous cliquons dessus, elle nous ramène à notre page d'accueil, car c'est là que se trouve notre href.

À côté de ce Dave, nous allons ajouter une div à laquelle, bien sûr, a son propre style, comme vous pouvez le voir ici, et nous allons ajouter plusieurs éléments de ce Dave.

Et nous avons un projet, des technologies, et à propos, chacun d'eux ayant un attribut href ici qui n'existe pas actuellement.

Mais si nous sauvegardons cela, nous voyons maintenant à quoi cela ressemble.

Bien sûr, en vue mobile, en survolant tout le style, vous pouvez voir appliquer là.

Et bien sûr, en cliquant dessus, cela devrait amener chacun à la section appropriée.

Mais nous n'avons pas actuellement les sections activées.

Donc nous devrons revenir et implémenter ces sections à l'avenir.

Et ensuite ce que nous voulons faire, c'est ajouter une chose de plus, nous ajoutons ce composant social Details, le composant va ressembler à ceci.

Sauvegardons-le, ce composant va contenir tous nos détails sociaux, comme nos icônes.

Et vous pouvez voir ici qu'il est enveloppé dans une div trois.

Et ensuite nous avons nos icônes sociales, et ces icônes sociales ont, par exemple, une icône GitHub, une icône LinkedIn, une icône Twitter, une icône YouTube, et ainsi de suite.

Si vous avez d'autres médias sociaux que vous voulez ajouter, vous pouvez simplement obtenir l'une de ces icônes à partir du package react icons.ai, si vous allez sur leur site web, vous verrez tous les différents types d'icônes.

Et bien sûr, si vous vouliez en ajouter d'autres, vous viendriez ici et en ajouteriez plus en fonction du type de médias sociaux que vous avez.

Ensuite, l'autre chose que nous faisons ici, c'est que nous stockons toutes nos URLs sociales à l'intérieur de ce fichier constants.

Laissez-moi vous y emmener.

Donc si vous allez sur social URLs, Jas, vous pouvez voir qu'il s'agit simplement d'un objet qui contient un lien vers chacun de nos profils, puis nous faisons simplement référence à chacun des liens ici, en conséquence.

Et donc maintenant si nous revenons à l'en-tête et que nous faisons défiler vers le bas, et en dessous de cette div, nous ajoutons nos détails sociaux.

Donc vous pouvez voir que cette sélection en bas va automatiquement importer pour moi.

Donc si je fais cela, et ensuite je fais défiler vers le haut, vous pouvez voir que l'importation a été ajoutée pour moi aussi.

Et dès que nous cliquons sur sauvegarder, faites attention à ce qui se passe du côté droit, boom, nous avons nos icônes sociales, vous voyez.

Et si nous les survolons, vous pouvez voir dans le coin inférieur gauche de mon navigateur, il met même en évidence l'URL, laissez-moi agrandir cela.

Donc vous pouvez voir, regardez cela.

Donc voici cette URL, LinkedIn, Twitter, et YouTube.

Magnifique.

Et en fait, ce que je vais faire rapidement, mettre YouTube en avant, prendre cela, le mettre ici, sauvegarder, et le voilà.

Parlons de notre stratégie de test.

Pour un moment.

Bien sûr, nous construisons une application web, et maintenant est un moment parfait pour penser à une stratégie de test pour cette application web.

Et dans un monde d'applications web, il est vraiment important d'être mobile first, toutes nos applications, maintenant elles doivent être réactives, et elles doivent supporter le mobile.

Donc c'est la toute première chose que nous devons vérifier, c'est comment notre application web répond à différentes résolutions d'appareils mobiles.

Et donc une très bonne façon de faire cela est de vérifier cela en réduisant notre navigateur pour voir si nous trouvons des problèmes, et je n'en vois aucun à ce stade, je vois un comportement intéressant à cette résolution où ces trois sont un peu regroupés, n'est-ce pas.

Et ensuite en continuant à faire défiler, je vois un autre problème ici où notre logo est placé sur cet en-tête de projets, ce qui bien sûr n'est pas bon à avoir, ce n'est pas professionnel du tout.

Donc c'est quelque chose que nous allons devoir corriger.

Et bien sûr, nous pouvons en fait entrer dans les tailles réelles des mobiles en cliquant avec le bouton droit de la souris, en faisant inspecter en cliquant sur cet appareil mobile et ensuite vous pouvez sélectionner votre appareil à partir d'ici, je sélectionne iPhone 12 Pro, je vais le mettre à l'échelle à 100% de résolution et voici à quoi il ressemblerait sur un iPhone 12 Pro.

Cela a l'air absolument fantastique.

Il n'y a pas de problèmes que nous devrions voir ici, tout est très lisible.

Et bien sûr, nous n'avons rien d'autre.

Mais à part cela, c'est ce qu'il reste.

Et bien sûr, vous pouvez aussi le vérifier sur un appareil non iPhone.

Donc c'est important.

Et donc ce que nous allons finir par faire en fait, c'est écrire des tests visuels automatisés de bout en bout pour nous assurer que notre application a l'air bien sur différentes résolutions.

Et nous pouvons continuer à tester à travers toutes ces résolutions au fur et à mesure que nous développons notre application en nous assurant qu'il n'y a pas de régressions au fur et à mesure que nous développons notre application.

L'autre chose à retenir est que nous avons ajouté des URL ici dans ces icônes, n'est-ce pas, ce sont les URL que nous avons fournies nous-mêmes.

Et bien sûr, il est très possible que ces URL puissent être mal saisies et incorrectes.

Nous les avons bien sûr testées manuellement déjà pour nous assurer qu'elles sont correctes.

Mais il n'y a aucune raison de penser que cela ne peut pas échouer accidentellement à l'avenir.

Donc nous voulons nous assurer que ces URL sont correctes.

Et aussi qu'elles correspondent à l'icône correcte.

Bien, alors, nous avons une navigation pour chacun de ces éléments aussi que nous avons écrite dans notre en-tête.

Donc si nous jetons un coup d'œil à notre header, JS, bien, nous avons mis un attribut href pour chacun de ceux-ci ici à l'avenir, nous devrons nous assurer qu'ils correspondent à la section appropriée que nous allons coder ici.

Et bien sûr, il y a cette section portfolio qui est censée nous rediriger vers notre page d'accueil, ce qu'elle a cet attribut href.

Et bien sûr, cela doit être vérifié aussi.

Autre que cela, je dirais qu'il n'y a pas d'autres besoins de test réels pour l'instant.

Et donc c'est ce sur quoi nous allons travailler, nous allons écrire des tests automatisés pour rendre tout cela possible.

Donc, allons-y et faisons cela.

Nous allons utiliser deux outils qui vont nous aider dans notre parcours de test automatisé.

Tout d'abord, nous allons utiliser Happo I O, qui est un outil de test visuel de bout en bout qui nous permet de nous assurer que notre application a l'air comme elle le devrait, sur différentes résolutions.

Et vous pouvez même voir ici en fait, c'est un peu ce qui se passe, il permet de prendre des instantanés, et ensuite ces instantanés peuvent être comparés à des références.

Et ensuite nous allons exécuter ces tests avec Cypress i o Cypress I O est un outil de test fonctionnel de bout en bout du navigateur.

Et il nous permettra d'exécuter nos tests.

Et bien sûr, il nous permettra d'écrire nos tests fonctionnels de bout en bout aussi.

Donc, allons-y et faisons en sorte que tout cela se produise.

Donc pour gagner du temps, j'ai en fait déjà installé et configuré un tas d'informations ici.

Cependant, si vous le faites de votre côté, la toute première chose que vous allez vouloir faire est d'ouvrir Cypress, nous l'avons déjà installé, n'est-ce pas, quand nous avons exécuté npm install, cependant, nous allons vouloir exécuter MPX, Cypress open.

Et ensuite, ce que cela va faire, c'est ouvrir une interface utilisateur Cypress qui ressemble à ceci, vous allez avoir beaucoup plus de dossiers et de fichiers qui sortent ici.

Et cela va également créer un dossier Cypress qui vit ici, à l'intérieur du dossier Cypress, il va avoir plusieurs autres dossiers et plusieurs autres fichiers qui sont importants.

Ce que nous allons faire, c'est supprimer tous les dossiers et fichiers qui étaient dans integration.

Et nous allons créer un fichier visual dot spared dot j s, c'est là que nous allons écrire nos tests visuels.

Nous allons en parler dans un moment.

Ensuite, dans les plugins, nous allons vouloir ajouter ce code pour pouvoir utiliser Happo.

Avec nos tests Cypress.

Ensuite, dans le support, nous allons vouloir importer Happo, Cypress dans notre fichier commands js.

Et avec tout cela fait, ce que nous pouvons maintenant enfin faire, c'est aller à Visual spec et écrire un test.

Laissez-moi vous montrer exactement à quoi ressemble ce test.

Donc ici nous avons un bloc describe.

Et nous disons que nos tests visuels vont afficher la page d'accueil correctement.

Tout d'abord, ils vont visiter notre application et s'assurer que notre application est dans un bon état.

Et enfin, nous allons simplement obtenir le corps de notre page et prendre une capture d'écran de la page complète.

Pour configurer tout cela et le faire fonctionner, nous avons besoin d'un fichier Happo J S situé à la racine de notre dossier à la racine de notre projet.

Donc vous pouvez voir ici, il est juste à côté du package json et du Cypress JSON.

Donc ce fichier Happo J S a un certain nombre de choses importantes telles que votre nom d'utilisateur et votre clé d'accès que vous pouvez obtenir de votre profil ici, si vous venez ici et allez dans votre profil utilisateur, et comptables, vous pourrez obtenir ces informations, puis nous fournissons un nom de projet.

Donc ce que nous allons faire, c'est mettre à jour notre nom de projet et l'appeler dev portfolio tutorial.

Et voici la partie la plus utile de cette configuration, la configuration de nos cibles.

Donc nous disons essentiellement que nous donnons un nom aux cibles.

Et ensuite nous disons sur quel navigateur et quelle taille de viewport nous voulons exécuter, il y a plusieurs autres configurations que nous pouvons définir.

Dans ce cas, nous disons d'attendre que la dernière animation soit terminée, auquel cas ensuite nous allons prendre un instantané, n'est-ce pas.

Donc ici nous faisons notre Chrome 10, ADP, Samsung Galaxy S 10, taille de viewport, nous faisons iPhone 12, taille de viewport, et nous faisons la taille de viewport qui a causé notre bug que nous avons vu précédemment, comment j'ai déterminé la taille de viewport était en venant ici.

Et vous pouvez voir en faisant défiler vers le bas et en fait si nous sortons de cette vue, vous verrez que ici dans le coin supérieur droit, il nous montre la taille de viewport que nous faisons défiler, donc vous faites défiler, vous pouvez voir la taille de viewport et ensuite nous allons chercher celle qui pose problème, la voici, la voici, celle qui pose problème.

Donc vous voyez, c'est environ 656 65.

Ce n'est pas important.

Donc j'ai mis 650 par 415.

Et c'est là que nous attrapons ce bug sur lequel nous allons vouloir travailler.

Et ensuite la dernière partie de cela avec la configuration de Cypress est dans le Cypress JSON, nous définissons notre URL de base sur localhost 3000.

Et c'est ainsi que dans notre visual spec, donc si nous venons à visual spec, c'est ainsi que nous pouvons simplement visiter ce slash ici à cause de cela.

Donc maintenant avec tout cela dit, nous avons un script ajouté ici que nous appelons test visual en exécutant la commande suivante.

Allons-y et exécutons-le et voyons ce qui se passe.

Et en regardant ici, nous voyons que nos tests sont terminés.

Et allons jeter un coup d'œil à notre tableau de bord Hafele.

Donc nous allons revenir ici, aller au tableau de bord Happo.

Et ici nous voyons que nous avons ce nouveau rapport appelé dev portfolio tutorial, qui est exactement notre nom de projet, nous allons l'ouvrir et nous pouvons voir nos instantanés ici, n'est-ce pas, vous pouvez voir les différentes résolutions, bien sûr, magnifique, vous pouvez voir notre bug ici recréé à cette résolution.

Et ensuite vous pouvez voir d'autres résolutions et à quoi ressemble notre application.

Et donc dans ceux-ci, tout a l'air bien pour moi.

Aucun problème majeur, bien sûr, sauf cette partie ici.

Et donc maintenant nous définissons essentiellement nos références, et à partir de ce point, lorsque nous exécuterons ces tests visuels, ils seront comparés à cela.

Et nous devrons décider si nous avons cassé quelque chose ou non.

Donc ce sont nos tests visuels, nous assurant que notre application a l'air magnifique sur différents navigateurs et systèmes d'exploitation.

Et les aspects fonctionnels de notre application ? Comment testons-nous ceux-ci ? Que faisons-nous avec tous ces liens ? Attaquons cela ensuite.

Et tous les liens que nous devons vérifier ? Comment allons-nous faire cela, dans le passé, ce que j'aurais fait aurait été d'utiliser des outils de test de bout en bout officiels tels que Cypress, selenium, et je serais allé identifier chacun de ces localisateurs et ensuite cliqué dessus et ensuite m'assurer qu'ils me naviguent vers l'URL correcte.

J'ai appris en cours de route que ce n'est pas l'approche la plus optimale, il y a en fait une meilleure approche pour le faire, la meilleure approche pour le faire, que j'ai apprise en cours de route, serait de faire quelque chose comme un test de composant.

Un test de composant, également connu sous le nom de test unitaire, est quelque chose que nous pouvons faire pour simplement vérifier l'attribut href de chacun de ces éléments, n'est-ce pas.

Si nous venons ici et inspectons chacun de ces localisateurs, ce que nous voyons, c'est que chacun de ceux-ci a un attribut href.

Et donc si nous savons que cette URL est correcte, alors nous savons qu'elle va nous emmener à la page correcte.

Parce que pourquoi ne le ferait-elle pas, la cliquabilité d'une ligue vient en fait de la balise a.

Et donc si la cliquabilité d'un lien à l'intérieur d'une balise a ne fonctionne pas pour vous, elle ne fonctionnera pas pour le reste d'Internet.

Et donc cliquer dessus est en fait inutile.

Ce qui est important, c'est de faire une vérification une fois que l'URL fonctionne réellement.

Et ensuite, après cela, tout ce que nous avons simplement à faire est de vérifier l'attribut href pour sa valeur correcte à l'intérieur de notre test.

Maintenant, nous pouvons, comme je l'ai mentionné, le faire par un test de composant, un test de composant, ce qu'il ferait en fait, c'est que si nous venions à nos détails sociaux, nous voyons que nous passons un tas d'URL par notre objet social URLs ici, n'est-ce pas.

Et donc toutes ces propriétés sont définies.

Et ensuite les URL sociales, elles vivent ici dans les constantes, et ce n'est qu'un objet pointant vers votre droite.

Donc nous pouvons simplement faire quelque chose comme un test de snapshot qui garantit que toutes ces URL sont correctes, ce qui serait en fait merveilleux, il prendrait des millisecondes à exécuter, il capturerait essentiellement un snapshot de ce fichier.

Et ensuite si quelque chose change à propos de ce fichier, il nous le ferait savoir qu'il y a un changement.

Et ensuite c'est à nous de décider si c'est un changement cassant ou non.

Le danger avec cela, et le risque qu'il ne couvre pas, même si vous pouvez avoir ces URL, cela ne signifie pas qu'elles sont correctement connectées à l'icône sociale correcte, n'est-ce pas, nous pourrions très facilement venir ici et faire quelque chose comme GitHub, parce que nous copiions, nous en avons créé un, et ensuite il a été copié et collé le reste.

Et nous avons oublié d'en changer un.

Je l'ai fait un certain nombre de fois dans ma vie, et je suis sûr que vous aussi.

Et donc cette pièce de connexion est en fait ce qui manque.

Et donc dans ce cas, ce que je pense être la meilleure stratégie, celle qui nécessite le moins d'efforts et a la meilleure couverture, est un test fonctionnel de bout en bout.

Et donc un test fonctionnel de bout en bout, bien sûr, comme je l'ai dit, était de venir ici, vérifier l'attribut href, et ensuite s'assurer que celui-ci est correct.

Et pour rendre ce genre de test possible, ce que j'ai écrit ici, c'est ce fichier social details spec J S, si nous le regardons ensemble, et en fait, nous n'avons même pas besoin de l'un ou l'autre de ceux-ci, nous allons le sauvegarder.

Donc ce que vous verrez ici, c'est que nous visitons notre URL comme avant.

Et au lieu de cela, nous disons que nos détails sociaux devraient avoir des liens sociaux corrects.

Et la façon dont nous obtenons ces attributs, c'est que nous regardons chacun de nos localisateurs, vous pouvez voir que j'ai utilisé un attribut data Test ID qui rend chacun de ces propriétés unique.

Et donc encore une fois, si nous venons voir les détails sociaux, J S, nous remarquerons que chacun de ces icônes n'avait rien d'unique, sauf l'attribut href.

Donc avant d'ajouter ces attributs data Test ID, toutes les icônes sociales ressemblaient à ceci.

Et donc comment référencer celle correcte, et s'assurer qu'elle est connectée à l'URL correcte.

Et donc nous faisons cela en ajoutant un attribut data Test ID et j'ai nommé chacun, n'est-ce pas, j'ai dit GitHub, YouTube, LinkedIn, et ainsi de suite correctement, en le faisant correspondre à l'icône correcte.

Et donc avec cela, je peux maintenant obtenir chacun et affirmer que chacun a un href qui correspond à la valeur correcte.

Si nous venons à notre tableau de bord Cypress, et que nous cliquons sur social details, spet, il va s'exécuter pour nous.

Et tout, regardez, il a en fait échoué.

Et si nous regardons, vous pouvez voir que nous obtenons un GitHub et GitHub fonctionne avec succès.

Mais ensuite si vous regardez YouTube, nous voyons qu'il a échoué.

Et pourquoi a-t-il échoué parce que nous attendions YouTube, mais au lieu de cela nous avons obtenu GitHub.

Et c'est bien sûr parce que j'ai fait une erreur, j'ai mal saisi, j'ai copié et collé incorrectement cette URL.

Et donc si nous faisons YouTube, et ensuite nous sauvegardons cela, nous revenons à notre test Cypress, nous le réexécutons, et tout passe correctement, n'est-ce pas, en vérifiant GitHub, YouTube, LinkedIn, et Twitter, tout est réussi.

Et donc en fin de compte, le test ressemble à ceci.

Et je ne vais pas écrire les tests pour les autres propriétés comme celles-ci et même le logo parce que vous savez déjà comment elles devraient se comporter.

Et je vais laisser cela comme un exercice pour vous à faire, envoyez définitivement une pull request au dépôt et partagez avec moi vos solutions et je vous ferai savoir si vous les avez eues correctement ou non.

D'accord, revenons au codage du reste de notre application.

Et maintenant nous allons aller un peu plus vite.

D'accord, j'ai implémenté le reste de l'application dans l'intérêt du temps afin que nous puissions parler davantage des tests et bien sûr, faire la partie la plus amusante, qui est le déploiement en production afin que nous puissions l'afficher fièrement au monde entier.

Donc j'ai implémenté une section technologies ici, comme vous pouvez le voir, c'est juste un tas de texte statique ici qui est écrit qui décrit toutes ces informations.

Si nous naviguons vers la section technologie, vous pouvez voir que tout est presque codé en dur ici dans ce composant.

Bien.

Donc en termes de risques, quels sont les risques avec cette section que nous devons aborder avec de nouveaux tests ? Absolument pas en fait, les tests visuels s'occupent de tous les risques, ils sont pour nous.

C'est la beauté des tests visuels.

Nous les avons écrits une fois.

Et maintenant nous pouvons les utiliser en continu pour vérifier notre application.

En parlant de cela, exécutons-les maintenant.

Pendant que nous continuons à parler de notre application, donc nous avons une section accomplishments.

Nos accomplishments montrent également un tas de données ici, si nous jetons un coup d'œil aux accomplishments, nous verrons qu'il y a ces données qui sont codées en dur ici, ce serait très utile de les déplacer dans notre dossier constants et de les mettre là.

Mais vous verrez comment nous itérons en utilisant une méthode de mappage sur toutes nos données.

Et c'est exactement comment nous l'affichons.

Donc quels sont les risques que nous devons vérifier ici, par exemple, dans ce cas, devons-nous écrire un autre test de bout en bout fonctionnel qui va valider que cette partie de notre UI lit correctement les données dans le backend ? Non, dans ce cas, nous n'avons pas besoin de faire cela.

Parce que ces données sont simplement affichées ici.

Si quelque chose d'étrange sort de cela, comme, par exemple, disons que nous mettons un zéro ici, et la quantité de projets ici, cela apparaîtra dans notre instantané visuel.

Et nous serons en mesure de voir les différences.

Et donc c'est la belle partie des données statiques qui se reflètent ici.

Et nous pouvons la capturer à nouveau, avec un test visuel de bout en bout qui existe déjà, nous protégeant de tous ces risques.

Et ensuite le pied de page ici est également très simple.

Donc, jetons un coup d'œil au pied de page du point de vue du code source.

Donc le pied de page est très simple, vous verrez en fait que nous réutilisons notre composant social Details que nous avons non seulement écrit avant, mais que nous avons également testé.

C'est pourquoi nous l'avons mis dans un composant individuel afin de pouvoir l'utiliser ici.

Et donc bien sûr, si nous l'avons déjà écrit et testé, le retester ici aussi, non, nous ne le faisons pas, c'est le même code source exact que nous avons écrit et testé avant.

Et donc nous sommes bons ici.

Le seul autre risque ici est ce lien qui fera et mail à cela pourrait être double vérifié, nous pourrions nous assurer que cela a la valeur correcte.

Et quelle serait la meilleure façon de le faire, nous pourrions simplement faire un test de composants pour nous assurer que cela a la valeur href correcte.

Et cela serait bien assez, nous pourrions faire un test fonctionnel de bout en bout avec Cypress.

Mais je ne pense pas que dans ce cas, ce soit nécessaire.

Maintenant, j'ai une question intéressante pour vous.

En termes de défi de test, comment nous assurons-nous que ces liens de projets sont corrects ici ? Donc dans la vue de l'application, si nous regardons les projets, bien, ils itèrent sur deux tableaux, dont l'un nous donne la source et la visite de notre fichier de projets ? Voici tous nos projets, bien ? Comment nous assurons-nous que cette URL et cette URL, et ainsi de suite, sont correctes, même lorsque nous modifions ces projets.

Donc une première pensée que je pourrais avoir est de faire des tests fonctionnels de bout en bout comme nous l'avons fait avec Cypress, bien ? Par exemple, si nous venons à notre social details spec, nous avons vérifié toutes nos URL de cette manière, bien ? Dans ce cas, en nous assurant que l'UI est correctement connectée à notre fichier et le lit correctement.

Cependant, qu'est-ce qui va se passer lorsque nous ajouterons un nouveau projet.

Donc maintenant nous devons ajouter un autre test.

Et ensuite l'autre défi de cela est maintenant non seulement nous devons ajouter un nouveau test, nous devons également commencer à ajouter des attributs de données de test uniques pour chaque bouton que nous ajoutons.

Je veux dire, je suppose que cela ne doit pas nécessairement être trop de travail, nous pourrions le rendre dynamique d'une certaine manière.

Mais cela semble être beaucoup d'efforts supplémentaires pour tester, juste le fait de tester ces composants ici.

Donc au lieu de cela, ce que nous pouvons en fait faire est d'utiliser un test de composants, spécifiquement un snapshot de notre composant pour assurer la validité de ces composants ici.

Et laissez-moi vous montrer exactement ce que je veux dire.

Et pour cela, nous allons utiliser just Jess qui est une bibliothèque de test unitaire qui permet également de faire des tests de snapshot avec le code.

Donc, regardons exactement ce que je veux dire.

Donc j'ai configuré ici un test de snapshot.

Vous pouvez voir dans notre dossier constants, j'ai ajouté un projects dot test dot j s La raison pour laquelle il est appelé projects dot test est qu'il teste ce fichier projects qui contient toutes les ressources pertinentes.

Et ce fichier de test de projects dit que nous allons avoir un test.

Et il vérifie que les détails des projets sont corrects.

Et nous importons notre objet projects.

Et ensuite nous nous attendons à ce que notre objet projects corresponde à un snapshot en ligne.

Donc lorsque nous utilisons cette méthode initialement, en fait, je peux même vous le montrer ici, ce que just va faire est de générer un snapshot de ce projet.

Donc bien sûr, nous pouvons accéder à différentes propriétés, et ainsi de suite.

Mais nous voulons vraiment l'objet entier, et je vous montrerai à quoi cela ressemble.

Donc si nous venons ici, et bien sûr, j'ai déjà ajouté un script, qui est appelé NPM, run test jest.

Il va exécuter ce test.

Et ce que vous voyez aussi ici, c'est que just a rempli cet objet entier dans notre code.

Donc il est écrit ici, tout sur nos objets, comme une description, l'ID, l'URL de l'image.

Mais encore mieux, il a capturé nos liens pour s'assurer qu'ils sont corrects.

Donc similaire aux tests visuels, tout ce que nous avons à faire à ce stade est de nous assurer que tout cela est correct.

Une fois manuellement.

Et maintenant à partir de ce point, nous pouvons utiliser le snapshot comme critère d'acceptation pour tout changement futur.

Et à quoi pourrait ressembler un changement futur ? Par exemple, disons que pour une raison quelconque, j'étais ici, et j'ai accidentellement gâché cette valeur.

Et j'ai dit, ou même oui, faisons cela en premier.

Et ensuite si nous réexécutons NPM, run test chest, nous allons obtenir un échec.

Et l'échec va nous dire, hé, vous vous attendiez à ce que cela corresponde à votre snapshot en ligne.

Mais regardez la différence que j'ai trouvée.

Je m'attendais à cela, mais j'ai obtenu cela.

Et donc bien sûr, c'est un bug et nous pouvons le rejeter.

Donc je vais simplement revenir ici et sauvegarder cela et le réexécuter, bien sûr, il va réussir, c'est magnifique.

Mais ensuite bien sûr, même si vous vouliez ajouter une section totalement nouvelle, donnez-nous, donnez-lui un nouvel ID, et ensuite réexécutez juste, nous allons obtenir un échec attendu, parce que bien sûr, il ne correspond pas à notre snapshot.

Et juste va nous dire, hé, je vois cet objet totalement nouveau, c'est cela.

D'accord, donc bien sûr, vous validez manuellement que tout fonctionne ici une fois, et ensuite nous avons maintenant ce test pour nous assurer que rien ne casse à l'avenir.

Et avec cela dit, nous sommes capables de vérifier avec succès tout, toutes les données sur cette section, surtout les URL, qui sont cachées, bien sûr, tout ce qui est visible, peut être capturé par notre test visuel.

Mais les URL sont cachées, mais elles peuvent être vérifiées par notre test de snapshot.

Et donc avec tout cela dit, cela capture ce risque, et ensuite nous n'avons jamais revu notre tableau de bord Happo.

Jetons un coup d'œil à ces tests.

Jetons un coup d'œil à nos nouveaux snapshots.

Nous pouvons voir nos tout nouveaux snapshots.

Voici à quoi ils ressemblent maintenant, n'est-ce pas ? Beaucoup plus grands.

Tout ici a l'air bien.

Tout a l'air merveilleux pour moi ici.

Donc bien sûr, je vais accepter et maintenant tout changement futur, nous pouvons entrer, les passer en revue et nous assurer que rien n'est cassé.

Merci beaucoup de vous être joint à moi ici aujourd'hui.

J'ai été Nikolai Adva lockin, fondateur de ultimate qa.com où je crée des formations sur le codage, les tests et le déploiement d'applications web.

Ce fut un vrai plaisir de traîner avec vous aujourd'hui.

Et si vous avez des commentaires sur ce que vous voulez apprendre la prochaine fois, n'hésitez pas à commenter ci-dessous.

Et si vous voulez en apprendre plus de moi, vous pouvez me suivre sur ma chaîne YouTube.

D'accord, à la prochaine.