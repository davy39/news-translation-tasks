---
title: Créer une application Android avec Kotlin et Jetpack Compose
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-24T15:43:51.000Z'
originalURL: https://freecodecamp.org/news/create-an-android-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/maxresdefault.jpeg
tags:
- name: Android
  slug: android
- name: Java
  slug: java
- name: youtube
  slug: youtube
seo_title: Créer une application Android avec Kotlin et Jetpack Compose
seo_desc: 'Jetpack Compose is Android''s modern toolkit for building native UI. It
  simplifies and accelerates UI development on Android.

  We just released a course on the freeCodeCamp.org YouTube channel that will teach
  you how to create a Sudoku Android app with...'
---

Jetpack Compose est le kit d'outils moderne d'Android pour créer des interfaces utilisateur natives. Il simplifie et accélère le développement d'interfaces utilisateur sur Android.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer une application Android Sudoku avec Kotlin et Jetpack Compose.

En cours de route, vous apprendrez également les structures de données de graphes et les algorithmes.

Ryan M. Kay a développé ce cours. Ryan est un développeur et enseignant extrêmement expérimenté.

Voici les sections couvertes dans ce cours :

* Approche de conception d'application : minimalisme de bibliothèque tierce et architecture MV-Whatever
* Package Domain : Repository Pattern, Enum, Data Class, Sealed Class, Hash Code, Interfaces
* Package Common : Extension Functions & Variables, Open-Closed Principle (OCP), Abstract Class, Singleton
* Package Persistence (Storage) : Clean Architecture Back End avec Java File System Storage, Jetpack Proto Datastore
* Package UI : bases de l'UI Jetpack Compose, Styles, Typography, Thèmes Clair & Sombre
* Package UI Components : Modifiers, Toolbar réutilisable & écrans de chargement
* Package UI Active Game Feature : Logique de présentation & ViewModel avec Coroutines, Kotlin Function Types
* Package UI Active Game Feature : Jeu Sudoku avec UI Jetpack Compose & Activity Container
* Package Computation Logic : Vue d'ensemble, conception et test des structures de données de graphes et algorithmes pour les Sudokus *carrés* de taille n

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=bo_LP6QOUio) (3,5 heures de visionnage).

%[https://www.youtube.com/watch?v=bo_LP6QOUio]

## Transcription

(générée automatiquement)

Dans ce cours, vous apprendrez à créer une application Android en utilisant la bibliothèque d'interface utilisateur jetpack compose.

En cours de route, vous apprendrez les algorithmes de graphes et les structures de données.

Ryan M. Kay enseigne ce cours.

Il est un développeur et instructeur très expérimenté.

Salut tout le monde ? C'est Ryan ici, et je voudrais vous souhaiter la bienvenue dans ma série de tutoriels sur l'application graph Sudoku.

C'est une application que j'ai écrite principalement pour affiner ma compréhension des structures de données de graphes et des algorithmes, et de la nouvelle bibliothèque d'interface utilisateur sur Android jetpack compose.

Dans cette partie de la série, je vais donner un aperçu des principaux objectifs et sujets de la série et discuter de quelques décisions de conception qui pourraient vous surprendre.

Je vais essayer de garder la version publique du code source du projet à jour.

Et ce sera votre responsabilité de regarder ce code source si quelque chose devient obsolète ou cesse de fonctionner.

Le format de cette série est un style de code le long, ce qui implique que la meilleure façon d'apprendre est d'écrire le code avec moi pendant que je l'explique.

Pour les développeurs avancés, la source complète est disponible pour un apprentissage direct, mais vous pouvez regarder les vidéos pour combler les lacunes dans vos connaissances.

J'utilise certaines fonctionnalités assez avancées du langage kotlin et les principes intemporels de l'architecture logicielle, donc vous pourriez apprendre une ou deux choses.

Pour les débutants, il est très important que vous me suiviez dans le code mais à votre propre rythme.

Vous pourriez ne pas avoir l'impression de faire des progrès au début, mais comprenez que vous pratiquerez la compétence d'écrire du code même si vous ne comprenez pas encore ce que vous écrivez.

Je vais aussi secrètement vous apprendre à écrire du code qui est facile à écrire, lire, corriger, améliorer et tester.

Mais au lieu de vous demander de mémoriser les principes intemporels de la conception logicielle, vous les apprendrez et les utiliserez en pratique alors que nous construisons cette application.

Il y a quatre sujets généraux que ce didacticiel démontrera : les structures de données de graphes et les algorithmes, jetpack compose, les architectures UI propres, et les fonctionnalités du langage kotlin.

Nous explorerons le sujet des graphes colorés dirigés et mes expériences dans l'écriture d'algorithmes pour générer, résoudre et non résoudre des énigmes Sudoku de taille n.

Nous construirons toute l'interface utilisateur en utilisant jetpack compose, ce qui nous permet de créer notre UI entièrement en kotlin.

Contrairement aux vues et styles XML.

Je vais vous montrer comment connecter une application simple en utilisant des principes communément exposés dans les architectures solides et propres.

Cependant, j'enseigne ces sujets à ma manière, donc ne vous attendez pas à un tas de jargon ou de sur-ingénierie.

Je vais également démontrer comment et quand utiliser les fonctionnalités de base et avancées de ce beau langage de programmation.

Cette partie de la vidéo est plus destinée aux développeurs intermédiaires et avancés.

Comprendre cette décision de conception n'est pas nécessaire pour compléter le tutoriel.

Tout au long de ce tutoriel, vous remarquerez que, à part compose et proto data store, j'utilise presque aucune bibliothèque d'Android jetpack. En fait, très peu de bibliothèques tierces en général, en me basant sur les bibliothèques standard de kotlin et Java et le SDK Android, mon code devient plus résistant aux obsolescences et aux changements dans les bibliothèques.

C'est parce que le SDK Android et les bibliothèques standard tendent à changer moins fréquemment que les bibliothèques tierces, comme celles que vous voyez dans Android jetpack.

Cela signifie également que certaines choses que des bibliothèques comme jetpack viewmodel, jetpack, navigation ou help pourraient gérer doivent être écrites à la main par nous.

J'aime bien cela, mais vous pourriez avoir un système de valeurs différent.

Et mon objectif ici n'est pas de vous décourager d'apprendre ces outils si vous êtes intéressé par eux.

Cela dit, vous pourriez être surpris de voir à quel point il est facile d'écrire votre propre viewmodel, navigation ou code d'injection de dépendances sans eux dans une petite application comme celle-ci.

Cette application utilise l'architecture Model View whatever, ce qui est ma façon de dire que je ne suis personne d'autre.

Ayant étudié ce sujet pendant de nombreuses années, je laisse les exigences du projet et ma compréhension des principes de bonne conception logicielle guider mon architecture.

Dans ce cas, je trouve que compose est fait pour une approche basée sur MVVM, mais j'ai ajouté une classe de logique de présentation pour une raison spécifique.

Cette raison s'appelle passive view ou humble object.

Au lieu d'avoir la vue ou le view model gérer le flux de contrôle de chaque écran, j'ai extrait cette logique dans une classe séparée.

Cette classe est super facile à écrire et à tester car elle n'a aucune dépendance tierce.

Et elle empêche mon view model de devenir un objet Dieu laid.

Vous devriez l'essayer un jour.

J'ai conçu cette architecture simplement en appliquant le principe le plus important de l'architecture logicielle, la séparation des préoccupations.

C'est tout pour cette partie de la série.

Maintenant, nous commençons à coder.

Le package de domaine représente deux choses, les morceaux d'information les plus généraux, tels que les classes de données, les constantes, et assez que le programme doit représenter virtuellement.

Aussi, les choses les plus générales que ce programme doit faire, que le programme représente en utilisant des fonctions et des interfaces.

En essence, c'est la fondation de tout nouveau programme que je crée et j'utilise un processus répétable pour concevoir mon package ou module de domaine.

Pour une introduction claire et simple à ce processus.

Consultez cette vidéo sur ma chaîne, comment concevoir des systèmes d'information et des applications.

Cette vidéo est un enregistrement d'une conférence que j'ai donnée à des ingénieurs logiciels en Égypte sur ce sujet particulier.

En tout cas, la plupart du code dans ce package est simple, mais il inclut un modèle de conception, que je vais introduire maintenant.

Ce package contient plusieurs interfaces, qui sont utilisées pour employer le modèle de conception de dépôt.

Ce modèle est également connu sous le nom de modèle de façade.

Et le but général du modèle est plus simple que sa définition technique.

La définition technique du modèle de façade ou de dépôt est de cacher les détails d'un sous-système, dans ce cas, les mécanismes de stockage de données derrière une abstraction, dans ce cas, une interface.

Regardons un exemple pratique.

Pour donner un sens à cette définition, nos classes de logique de présentation tiendront des références à ces interfaces de dépôt, au lieu des classes qui implémentent les interfaces.

Cela donne plusieurs avantages à nos classes de logique de présentation.

Elles peuvent être construites indépendamment les unes des autres sans causer d'erreur de compilation, elles peuvent être testées avec une implémentation factice de l'interface sans nécessiter de changer de code dans la classe de logique de présentation.

De plus, si nous décidons d'utiliser une implémentation différente de l'interface, comme passer du stockage de fichiers à une base de données room, nous pouvons aussi le faire sans nécessiter de changements dans la classe de logique de présentation.

Ces avantages sont le résultat de la construction de systèmes logiciels qui sont faiblement couplés.

Et le modèle de dépôt ou de façade est un moyen facile de promouvoir un couplage lâche.

En fait, les interfaces en général tendent à promouvoir un couplage lâche.

Maintenant, ne sentez pas le besoin d'utiliser ce modèle partout.

Une bonne règle générale est de les utiliser dans des limites architecturales significatives.

Dans ce cas, je les utilise comme une frontière entre le front-end et le back-end de cette application.

Pour commencer, cliquez avec le bouton droit sur le package de domaine, allez dans Nouveau fichier kotlin et créez un fichier appelé difficulté.

Et cela va être une classe enum.

Les classes enum en kotlin, Java et divers autres langages sont utiles pour créer un ensemble restreint de valeurs.

Comme nous le verrons plus tard, vous pouvez utiliser des classes scellées en kotlin pour créer un ensemble restreint de types.

Dans tous les cas, le principal avantage en dehors de la création de cet ensemble de valeurs restreintes est que les enums peuvent grandement améliorer la lisibilité de votre programme.

Comme nous le verrons dans un instant, ajoutons nos entrées enum.

Assez évidemment, cet enum représentera la difficulté d'un puzzle Sudoku donné.

Cependant, nous devons ajouter une chose de plus avant de continuer, nous utiliserons en fait certaines valeurs pour chacune de ces entrées dans les algorithmes pour dicter essentiellement la difficulté du puzzle Sudoku.

Donc, afin d'ajouter une valeur à un enum en kotlin, nous devons lui donner une propriété ou certaines propriétés.

Comme vous pouvez le voir, nos entrées sont maintenant lues, donc évidemment, nous devons leur donner quelques doubles.

Et c'est tout ce que nous devons faire ici.

Cliquez avec le bouton droit sur le package principal, allez dans Nouveau fichier kotlin pour la classe.

Et nous allons créer une classe de données appelée paramètres.

Les paramètres sont notre premier modèle de données, comme j'aime l'appeler, ou un ancien objet kotlin.

Et comme nous le verrons dans un instant, il contiendra à la fois la difficulté et la frontière, qui est la taille du puzzle Sudoku.

Donc, un puzzle Sudoku de quatre par quatre aura une frontière de quatre, un neuf par neuf aura une frontière de neuf.

Le mot-clé data, lorsqu'il est placé devant un mot-clé de classe, ajoute ou génère essentiellement quelques méthodes d'assistance, telles que equals hash code ou copy.

Nous utiliserons définitivement copy plus tard, peut-être pas dans cette classe, mais dans certaines d'entre elles et d'autres.

À un certain point, nous utiliserons également la fonction de code de hachage générée.

En tout cas, c'est une classe vraiment simple, nous allons simplement ajouter deux propriétés.

Et c'est tout.

Cliquez avec le bouton droit sur le package de domaine, allez dans Nouvelle classe ou fichier kotlin.

Et cette fois, nous allons créer une classe appelée statistiques utilisateur.

Et ce sera une classe de données.

Maintenant, le but de cette classe est de représenter les temps les plus courts / meilleurs de l'utilisateur pour résoudre un puzzle Sudoku de difficulté ou de taille particulière.

Donc, nous allons essentiellement ajouter un tas de propriétés qui sont presque les mêmes.

Maintenant, une chose que vous pouvez faire dans IntelliJ IDEA ou Android Studio est de cliquer là et d'appuyer sur Ctrl D autant de fois que nécessaire et cela copiera une nouvelle ligne.

C'est essentiellement tout pour cette classe.

Maintenant, vous vous demandez peut-être pourquoi nous utilisons long ici, nous stockons en fait le temps qu'il faut à l'utilisateur pour compléter un jeu particulier en millisecondes.

Donc, c'est pourquoi nous voulons la valeur entière longue.

Encore une fois, cliquez avec le bouton droit sur le package de domaine, allez dans Nouveau fichier kotlin, et ce sera une classe de données nommée Sudoku note.

Maintenant, c'est là que les choses commencent à devenir un peu plus compliquées et intéressantes avec nos modèles de données.

Donc, ce que je fais ici, c'est que je représente un nœud individuel dans une structure de données de graphe, nous allons en parler beaucoup plus sur les structures de données de graphe plus tard lorsque nous arriverons à la partie du tutoriel qui lui est dédiée.

Mais juste pour vous donner une idée, nous allons en fait construire un graphe coloré dirigé.

Et une chose importante à noter ici est que dans ce cas particulier, ce terme couleur fait vraiment référence à un nombre, c'est juste une valeur que nous associons à un type de nœud.

Et encore, pour vous donner un aperçu, lorsque je dis structure de données de graphe, un meilleur nom pour cela serait une structure de données de réseau, car c'est essentiellement ce que c'est.

C'est une collection de nœuds et d'arêtes, qui sont essentiellement comme des lignes entre les nœuds, des relations entre les nœuds.

En tout cas, cette structure de nœud particulière dans notre structure de données aura une couleur ou une valeur, qui est juste un entier de un à neuf ou de un à quatre, incluant également 00 représente comme une tuile Sudoku vide, mais c'est plus une préoccupation du front-end.

Ces notes incluront également une coordonnée X et Y, donc le coin supérieur gauche sera x zéro y zéro, le coin inférieur droit sera x huit, y huit, et nous allons utiliser l'indexation basée sur zéro.

Donc au lieu de commencer de x un à x neuf, nous soustrayons simplement cela par un.

Donc c'est tout pour ce préambule, commençons à écrire le code.

Nous commencerons donc par les valeurs x et y.

Ensuite, nous ajouterons la couleur qui sera une variable car elle peut changer au cours de l'exécution.

Ensuite, nous ajouterons un booléen appelé read only et je vais expliquer ce que c'est après l'avoir écrit.

Maintenant, le but du booléen read only ici est assez simple.

Lorsque nous générons essentiellement puis résolvons un puzzle Sudoku, ce qui est une autre façon de dire que nous créons un nouveau puzzle Sudoku puis supprimons un certain nombre d'indices pour rendre le jeu réellement jouable et amusant.

Certains de ces nombres sur le tableau Sudoku ou dans la structure de données de graphe Sudoku seront en lecture seule, ce sont comme les indices donnés que l'utilisateur ne devrait pas pouvoir changer lui-même.

Comme nous le verrons plus tard.

Cela affectera également l'interface utilisateur car nous dessinerons les nœuds ou tuiles Sudoku en lecture seule différemment de ceux que l'utilisateur peut éditer.

Maintenant, nous n'avons pas tout à fait terminé, nous devons remplacer la fonction de code de hachage qui a été fournie par le mot-clé de classe de données comme je l'ai discuté précédemment, puis nous devons également ajouter une fonction pour obtenir un code de hachage.

D'accord, donc le code de hachage aura une implémentation par défaut, qui est basée sur les valeurs fournies ici dans les différentes propriétés, nous allons en fait faire quelque chose de différent.

Donc nous allons taper get hash, comme ça.

Et c'est en fait une fonction que nous allons créer aussi, nous allons ajouter deux paramètres ici pour x et y.

D'accord, nous allons maintenant ajouter la fonction get hash, et elle sera de niveau supérieur, ce qui signifie qu'elle se trouve en dehors des crochets de notre classe Sudoku node.

D'accord, implémentons simplement cette fonction, puis j'expliquerai ce que nous faisons ici.

D'accord, alors laissez-moi commencer par expliquer ce qu'est exactement un code de hachage ou une valeur de hachage.

C'est essentiellement une sorte de clé générée ou d'identifiant unique basé sur un certain type d'algorithme.

Dans ce cas, j'ai un algorithme très simple, tout ce que je fais est multiplier la valeur x par 100.

Et je laisse la valeur y seule.

Et je combine essentiellement ces deux valeurs ensemble en un entier.

Maintenant, la raison pour laquelle je multiplie x par 100 est que si je ne le faisais pas dans un puzzle Sudoku de neuf par neuf, il y aurait certains cas limites où, même si les valeurs X et Y sont techniquement différentes, le code de hachage résultant ne serait pas unique pour plusieurs nœuds différents.

En termes simples, je multiplie par 100 pour rendre les codes de hachage uniques pour chaque tuile individuelle dans le puzzle Sudoku.

Quant à pourquoi nous utilisons le code de hachage, en général, je vais essayer de le garder assez simple.

Essentiellement, nous allons stocker chaque nœud dans le graphe dans une linked hash map.

Donc les valeurs de hachage représenteront la clé pour cette hash map.

Une hash map a des paires clé-valeur, au cas où vous ne le sauriez pas, nous allons le voir dans un instant.

Mais cela s'avère être vraiment utile car notre interface utilisateur également représentera les choses de cette manière en termes de style de coordonnées X et Y.

Donc prenez simplement ma parole.

Les codes de hachage sont assez pratiques dans les situations où vous avez un grand nombre d'éléments, et vous ne voulez pas nécessairement avoir à maintenir une référence pour chaque élément individuel.

Au lieu de cela, nous pouvons simplement récupérer une référence en obtenant un code de hachage.

Oh, et avant de partir, nous devons ajouter une chose de plus ici, nous allons faire en sorte que cette chose implémente serializable.

Maintenant, essentiellement, ce que cela fait, c'est qu'il nous permet de lire et d'écrire nos nœuds Sudoku et également le puzzle entier dans un fichier.

Puisque nous ne allons stocker qu'un seul puzzle à la fois, je ne voulais vraiment pas utiliser quelque chose comme une base de données, cela avait plus de sens d'utiliser le système de fichiers, et serializable le rend plus facile à faire, essentiellement.

D'accord, nous avons un dernier modèle de données à créer dans ce package particulier, encore une fois, cliquez avec le bouton droit sur Nouveau fichier kotlin, notre classe, celui-ci va s'appeler Sudoku puzzle.

Et encore une fois, ce sera une classe de données.

Une bonne façon de penser aux modèles de données, comme je les appelle, est qu'ils sont des représentations virtuelles d'un objet du monde réel, dans ce cas, un puzzle Sudoku.

La façon dont j'ai initialement conçu cette classe est en posant des questions critiques sur ce qui constitue un puzzle Sudoku.

Des choses comme les frontières, donc y a-t-il quatre tuiles par ligne ou colonne ou y a-t-il neuf tuiles par exemple, nous avons la difficulté.

Et surtout, nous avons la structure de données de graphe elle-même.

Il y a aussi le temps écoulé que l'utilisateur a pris pour résoudre un puzzle particulier.

Alors, allons-y et ajoutons ces propriétés et ensuite j'expliquerai certaines d'entre elles, celles qui doivent être expliquées par la suite.

De plus, avant que j'oublie, ajoutons l'implémentation serializable ici.

D'accord, vous vous demandez probablement ce que build new Sudoku est.

Donc, ce que nous allons faire, c'est que nous allons en fait appeler une longue série de fonctions de niveau supérieur, qui formeront tous nos différents algorithmes, qui sont nécessaires pour construire et générer un nouveau puzzle Sudoku, basé sur une taille donnée, qui est ce que boundary représente et une difficulté donnée.

De plus, si vous vous demandez ce qui se passe avec la linked hash map, qui est pleine de linked lists, c'est une façon de représenter une liste d'adjacence.

Encore une fois, je vais entrer dans ces détails sur les structures de données de graphes et les différentes façons dont vous pouvez les représenter, ou au moins comment je les représente dans cette application particulière plus tard lorsque nous arriverons à ce package et à ce sujet.

Mais pour l'instant, comprenez que cela représente notre puzzle Sudoku virtuel, la dernière chose que nous allons faire est simplement ajouter une petite méthode, qui rend un peu plus évident et lisible comment obtenir le graphe lui-même, du moins à mon avis.

Et nous allons utiliser la syntaxe d'expression unique.

Donc je vais simplement taper equals graph.

Créons une nouvelle interface appelée I game repository.

J'aime utiliser cette convention de nommage qui consiste à mettre un I majuscule devant les interfaces.

Et ensuite, comme nous le verrons plus tard, dans le package de persistance, j'ajouterai un suffixe de IMPL, qui signifie implémentation pour naturellement les classes qui implémentent cette interface.

Lors de la conception d'une application de petite à moyenne échelle, une chose que vous pouvez faire est de penser conceptuellement aux fonctions dans vos interfaces de dépôt.

Comme des cas d'utilisation eux-mêmes, les choses que nous allons écrire ici seront appelées comme save game update game update node, ce qui est très similaire si vous faites des histoires d'utilisateurs dans le type de conception d'application de cas d'utilisation.

Je voulais juste lancer cela.

Dans une application plus compliquée, où j'aurais besoin de faire plus de coordination de multiples sources de données et dépôts différents, j'aurais probablement un interactor, ou un cas d'utilisation, comme on en parle communément, entre Martin Fowler ou Robert Martin, Uncle Bob.

Mais dans ce cas particulier, dans des applications plus simples, en général, le cas d'utilisation en tant que classe lui-même est généralement une couche d'abstraction supplémentaire inutile.

Donc ici, nous allons directement avec notre présentateur, ou view model ou autre, parlant directement à un dépôt.

Et c'est une quantité suffisante d'abstraction pour une application de cette taille.

Maintenant, comment fonctionne une interface, c'est que c'est très similaire à une classe sauf que, comme nous le verrons dans un instant, nous ne sommes pas autorisés à implémenter ou à donner un corps aux fonctions que nous allons écrire, nous écrivons simplement ce que l'on appelle communément des fonctions abstraites ou des stubs de fonctions.

Maintenant, il y a deux points importants ici.

Premièrement, le mot-clé suspend est appliqué là, car ces fonctions seront en fait appelées à partir de portées de co-routines, qui existent dans la classe de logique ou le présentateur qui référencera cette interface particulière.

Donc c'est tout ce que nous devons faire pour établir la concurrence pour l'instant.

Maintenant, au cas où vous ne seriez pas familier, ce que j'utilise ici est ce qu'on appelle un type de fonction.

Et donc ce que nous allons faire, c'est que nous allons en fait passer une référence à deux fonctions qui existent dans la classe de logique, la logique de présentation passera ces fonctions.

Et ensuite, dans les implémentations du dépôt, les choses qui implémentent cette interface particulière, c'est ainsi qu'elles rappelleront avec un certain type de résultat, soit un résultat réussi, soit un échec.

Maintenant, vous vous demandez peut-être pourquoi avons-nous unit et ensuite il retourne unit, ce que signifie cette flèche, dans ce cas particulier ? C'est quelque chose que nous devons faire pour que le compilateur kotlin comprenne exactement ce que nous lui demandons de faire.

Donc cela serait équivalent à passer void ou rien dans cette fonction particulière, et ensuite à retourner rien de cette fonction particulière.

Mais ce qu'elle fera, c'est qu'elle signalera quelque chose comme un oncomplete si vous avez une expérience avec RX Java, où nous voulons simplement reprendre l'application avec succès lorsque cette fonction est appelée.

Mais cette fonction particulière n'a pas besoin de retourner quoi que ce soit.

Plus tard, nous verrons des exemples où nous devons retourner une valeur à travers notre fonction de type onsuccess.

Encore une fois, vous vous demandez peut-être quelle est la différence entre sauvegarder un jeu et mettre à jour un jeu ? Eh bien, essentiellement, dans la fonction de mise à jour du jeu, nous allons écrire intégralement un puzzle Sudoku entier, qui inclut un temps écoulé, bien qu'il y ait des situations où tout ce que nous devons faire est simplement mettre à jour le temps écoulé du jeu, comme lorsque l'utilisateur navigue loin de l'application.

Donc ce que je fais ici, c'est que je crée des fonctions spécialisées en fonction de ce que nous voulons atteindre du point de vue de l'utilisateur.

Maintenant, je vais démontrer quand nous voulons réellement retourner une valeur à partir de ces types de fonctions particuliers.

D'accord, donc pour onsuccess, ce que nous disons effectivement ici, c'est que cette fonction particulière doit être appelée avec une sorte de valeur booléenne, évidemment, soit vraie soit fausse lorsqu'elle est appelée dans l'implémentation de cette fonction de suspension particulière.

Maintenant, essentiellement, ce que nous faisons ici, c'est que lorsque l'utilisateur met à jour un seul nœud ou une seule tuile dans un puzzle Sudoku, il est possible que ce soit la tuile finale du puzzle.

Et dans ce cas particulier, en supposant que le puzzle est correct, et que l'utilisateur a entré la tuile finale, cela signalerait que le gain est complet.

Donc cela pourrait être un peu confus ici.

Mais onsuccess ne signifie pas nécessairement que le jeu lui-même a été complété.

C'est pourquoi je fais la distinction.

D'accord, maintenant, dans ce cas particulier, ce que nous faisons, c'est que lorsque l'utilisateur revient à un jeu actif, nous voulons évidemment obtenir un jeu actuel.

Et il y a en fait un cas limite où l'utilisateur complète le jeu, navigue loin de l'application, puis redémarre l'application.

Et c'est pourquoi nous transmettons toujours ce drapeau is complete.

Ici, nous allons retourner évidemment un objet settings.

Créons une autre interface.

Et elle va s'appeler I game data storage.

Et c'est évidemment une interface.

Maintenant, avant d'écrire l'interface elle-même, nous allons faire quelque chose d'un peu différent.

Nous allons créer un wrapper de résultat ou disons simplement qu'il est inspiré d'un monad soit d'un programmeur fonctionnel, mais personne ne se soucie vraiment de ce que les programmeurs fonctionnels pensent ou disent de toute façon.

Les classes scellées sont vraiment l'une de mes fonctionnalités simples préférées du langage de programmation kotlin.

Cela nous permet de créer un ensemble restreint de types, et ces types peuvent contenir des valeurs particulières.

Et essentiellement, ce que cela va faire, et comme nous le verrons dans un instant, c'est qu'il permet de retourner un objet à partir d'une fonction particulière de I game data storage.

Et cet objet particulier est capable de représenter plusieurs états différents.

Comme je vous l'ai montré avant dans AI game repository, ici, nous représentons un état d'erreur et un état de succès comme deux références de fonction séparées.

Dans cet exemple, nous allons représenter ces deux états à travers un seul objet.

Un dernier point, avant de continuer, si vous avez, par exemple, une situation où vous voulez représenter juste un cas de succès, donc équivalent à retourner simplement unit dans onsuccess, ce que vous pouvez faire, c'est que vous pouvez en fait utiliser un objet, donc vous pourriez dire comme objet on complete, etc.

Mais nous ne faisons pas cela dans cette application.

Donc vous n'avez pas besoin de l'ajouter.

Maintenant, terminons l'interface.

Créez une autre interface appelée I settings storage.

Maintenant, nous allons également utiliser des wrappers de résultat ici.

Donc je vais en fait copier et coller cela.

Et nous allons simplement renommer quelques choses.

D'accord, et maintenant nous pouvons écrire l'interface.

Une interface de plus à faire pour ce package.

Celle-ci va s'appeler pi statistics si je peux l'écrire repository, et évidemment, ce sera une interface.

Maintenant, un dernier point, encore une fois, est record qui va en fait affecter quelque chose dans l'interface utilisateur en fonction du fait qu'une statistique qui est mise à jour est un record, c'est-à-dire le temps le plus court possible de complétion pour une frontière ou une taille particulière de puzzle Sudoku, et une difficulté particulière.

Le package commun contient du code qui est réutilisé dans une variété de classes et de fonctions différentes.

Dans cette partie du tutoriel, nous apprendrons de nombreuses fonctionnalités différentes du langage kotlin, qui sont conçues pour partager du code de manière intelligente et efficace.

Les sujets abordés incluent les fonctions d'extension et les problèmes, ces classes abstraites, le principe ouvert-fermé, l'objet, le Singleton, et les dispatchers de co-routine.

Avant d'écrire le code, parlons du principe ouvert-fermé.

Le OCP est un concept relativement confus, mais je vais essayer de l'expliquer de la manière la plus claire possible pour vous donner ma propre définition verbale, que nous décomposerons plus tard.

Toute entité logicielle couramment réutilisée, qui est censée changer, devrait avoir une interface publique fixe et un moyen de changer son implémentation.

Pour que cette définition particulière ait du sens, il y a quelques choses que je dois déballer.

Tout d'abord, lorsque je dis entité logicielle, je parle généralement d'une classe ou d'une fonction, mais cela pourrait être quelques autres choses.

Examinons donc ce que je veux dire par interface publique et pourquoi je soutiens qu'elle devrait être fixe si elle est couramment réutilisée.

Par interface publique, je ne parle pas d'une interface Java ou kotlin spécifiquement, mais plutôt de tout aspect publiquement visible d'une classe ou d'une fonction.

Puisque c'est un tutoriel Android, prenons l'exemple de la classe d'activité.

Une activité répond à mon exigence d'être couramment réutilisée et censée changer au fil du temps.

C'est donc un cas parfait pour réfléchir au OCP.

Chaque sous-classe d'activité doit inclure la fonction onCreate, qui fait partie de l'interface publique, qu'elle rend disponible aux classes qui la référencent.

La raison pour laquelle nous voulons que cette interface publique ne change pas est très simple.

Supposons que les développeurs de la plateforme Android décident soudainement de déprécier et de supprimer les bundles d'état d'instance sauvegardés de toutes les fonctions de cycle de vie.

Parce que cette interface publique est utilisée par presque tous les programmes Android autour de cette mise à jour de la plateforme, cela casserait le code de tout le monde.

Ce que je veux dire spécifiquement, c'est que toutes les sous-classes d'activité dans toutes les bases de code qui n'ont pas supprimé ce paramètre ne pourraient pas compiler.

C'est pourquoi je parle spécifiquement des entités logicielles couramment réutilisées comme l'activité, et pourquoi il est important que leurs interfaces publiques changent le moins possible.

Puisque nous avons établi pourquoi les interfaces publiques fixes sont vraiment importantes.

La question suivante est simple.

Comment fournissons-nous alors un mécanisme ou un moyen pour que l'implémentation de l'interface publique change ? Il s'avère que kotlin vous donne de nombreuses options pour résoudre ce problème.

Plutôt que de les expliquer toutes verbalement, je vais vous apprendre à les utiliser en code.

Alors que nous construisons cette application, cliquez avec le bouton droit sur le package commun, et allez dans Nouveau fichier ou classe kotlin.

Et cela sera en fait une classe abstraite, pour laquelle ils ne donnent pas d'option ici.

Donc ce que nous allons faire, c'est taper base logic, nous ajouterons le mot-clé abstract.

Malheureusement, je n'ai pas le temps d'expliquer la différence entre une classe abstraite et une interface dans l'héritage classique.

Dans ce cours particulier, c'est quelque chose que j'aborde et que j'explique très clairement dans mes autres cours vidéo.

Mais ce que je vais faire, c'est expliquer pourquoi nous utilisons une classe abstraite ici au lieu d'une interface.

La raison pour laquelle nous voudrions utiliser une classe abstraite est pour les situations où nous voulons partager un comportement.

Par exemple, nous allons écrire un stub de fonction ou une fonction abstraite, que je veux partager à travers toute classe qui hérite de base logic.

Et je veux aussi partager une variable, mais cette variable particulière devra être protégée plutôt que publique.

Et si nous devions essayer de faire cela en utilisant une interface, alors nécessairement cette valeur particulière serait publique, nous allons aussi utiliser un type générique.

Donc je vais vous montrer comment faire cela.

Donc la syntaxe pour un type générique est d'utiliser simplement des chevrons.

Et puis vous pourriez prendre littéralement ce que vous voulez entre ces chevrons.

Mais ma suggestion pour vous est de ne pas utiliser quelque chose qui est déjà utilisé, c'est pourquoi j'utilise ce EVENT tout en majuscules.

Maintenant, si cela n'a pas de sens pour vous, cela aura plus de sens lorsque nous écrirons les classes qui héritent de base logic.

Allons-y et terminons cela.

Pour expliquer brièvement l'intention de cette classe abstraite.

Essentiellement, je dis que je veux un ensemble de classes, celles qui hériteront de base logic, toutes ayant cette fonction on event.

En d'autres termes, ces classes géreront les événements de l'interface utilisateur.

Et comme nous le verrons, nous allons utiliser cet objet job qui provient de l'API des coroutines comme moyen d'annuler les coroutines enfants.

Et aussi pour faire de chacune de ces classes de logique sa propre portée de coroutine.

Je vais expliquer cela lorsque nous arriverons à cette partie particulière du tutoriel, cliquez avec le bouton droit sur le package commun et créez un nouveau fichier kotlin, qui sera simplement un ancien fichier, et il s'appellera extensions.

Les fonctions d'extension et les propriétés d'extension de Kotlin font partie de mes fonctionnalités préférées du langage dans son ensemble.

Sans entrer dans les détails techniques ici, les extensions vous permettent d'appliquer le principe ouvert-fermé, qui stipule que les entités logicielles doivent être ouvertes à l'extension, mais fermées à la modification.

Si cela n'a pas de sens, ne vous en souciez pas, c'est une définition un peu confuse.

Mais cela nous permet d'ajouter de nouvelles fonctionnalités au code source existant sans avoir à modifier le code source original.

Maintenant, ce fichier particulier extensions.kt est une sorte de remplacement pour les utilitaires statiques que nous aurions pu utiliser en Java ou quelque chose de ce genre.

C'est vraiment juste un endroit où vous mettez du code utilitaire qui est utilisé dans toute l'application.

Écrivons notre première fonction d'extension pour voir comment cela fonctionne.

Le but de cette fonction d'extension particulière, évidemment elle sera utilisée dans les activités, est vraiment juste du sucre syntaxique, c'est une façon de faire en sorte que je n'aie pas à taper toast dot make text et fournir ce message toast dot length long et dot show.

Au lieu de cela, dans l'activité où nous allons utiliser les activités, je devrais dire où nous allons utiliser cette fonction d'extension particulière, nous pouvons simplement taper make toast, lui donner n'importe quelle chaîne que nous voulons afficher, et c'est géré comme ça.

En faisant de cela une fonction d'extension de la classe d'activité, je peux l'utiliser de manière transparente dans n'importe quelle activité.

Écrivons une autre fonction utilitaire d'extension beaucoup plus laide.

Le but de cette petite fonction laide ici est de prendre le temps écoulé du puzzle donné sur lequel l'utilisateur travaille actuellement, et d'essayer de le convertir en une valeur basée sur les minutes et les secondes ou une chaîne à afficher basée sur les minutes et les secondes.

Maintenant, si cela prend à l'utilisateur plus d'une heure, alors nous finissons par afficher quelque chose comme plus de 5959.

Maintenant, si vous pensez que ce code est laid, en kotlin, je vous mets au défi de l'écrire en Java.

Maintenant, pour les débutants, cela pourrait ne pas avoir de sens intuitivement, mais il est important de comprendre à quoi cela fait référence.

Cela fait en fait référence à l'objet long, sur lequel nous allons appeler dot two time.

Cela pourrait avoir un peu plus de sens lorsque nous utiliserons effectivement cette fonction d'extension particulière.

Il ne reste qu'une seule extension à ajouter, et ce sera en fait une propriété d'extension cette fois.

Donc ce que je fais ici, c'est que j'appuie sur alt, entrer sur cette chose rouge particulière, et ensuite je vais appuyer sur Add remaining branches.

Je vais appuyer sur alt enter, encore une fois, pour importer nos, ce sont évidemment des ressources de chaîne.

C'est une chose, nous ne allons pas l'écrire à la main.

Donc, espérons que ce que vous avez fait, c'est que vous êtes allé chercher le code source du point de départ, qui inclut des choses comme les ressources de chaîne, cliquez avec le bouton droit sur le package commun à nouveau, et nous allons créer une nouvelle interface kotlin, qui va s'appeler dispatcher provider.

Cette interface est très petite, ce que nous allons faire, c'est que nous allons écrire le code et ensuite je vais brièvement expliquer ce qu'elle fait.

Maintenant, malheureusement, je ne peux pas brièvement expliquer ce qu'est un contexte de co-routine.

Mais je peux expliquer le but de cette classe particulière et comment nous allons utiliser ces contextes de co-routine.

Donc dans la plupart des situations, la plupart du travail que nous allons faire dans le domaine des co-routines va avoir lieu sur le thread principal ou le thread UI.

Maintenant, cela dit, il y a quelques opérations comme l'écriture dans un fichier, que nous ne voulons pas réellement voir se produire sur le thread principal.

Et ce serait une situation où nous allons fournir le contexte IO.

Maintenant, le but réel de cette interface particulière est vraiment clé ici.

Ce que nous allons faire, c'est que si nous voulions hypothétiquement tester une classe qui a besoin d'utiliser ces contextes de co-routine, dans un environnement JVM, donc pas une application en cours d'exécution réelle, alors ce que nous pourrions faire, c'est que nous pourrions retourner un type particulier de contexte de co-routine, qui nous permet de tester dans cet environnement particulier.

Je sais que c'est beaucoup de détails techniques, mais je ne peux pas vraiment le rendre beaucoup plus simple que cela.

Cependant, en utilisant cette interface ici, lorsque nous voulons utiliser nos co-routines dans l'environnement de production, nous pouvons fournir le contexte réel de l'UI du thread principal pour le front-end, puis nous pouvons fournir un dispatcher réel pour le thread IO.

Pour rendre cela encore plus simple, nous rendons vraiment le code plus facile à tester.

Cliquez avec le bouton droit sur le package commun, allez dans Nouveau fichier ou classe kotlin, cette fois, ce sera un objet.

Et j'espère pouvoir l'écrire correctement production dispatcher provider.

Encore une fois, ce que nous allons faire, c'est écrire le code ici puis je vais expliquer comment cela fonctionne ensuite.

Je vais appuyer sur Alt Entrée à nouveau.

Et c'est là que nous allons retourner les dispatchers réels que nous allons utiliser en production comme le nom de cet objet particulier.

Maintenant, il y a un certain nombre de raisons pour lesquelles j'utilise le mot-clé object ici.

Donc, essentiellement, les objets en kotlin sont dans ce cas particulier des Singletons.

Donc, cela signifie essentiellement que nous n'aurons jamais qu'un seul de ces fournisseurs de dispatchers de production, ces trucs logiciels, qui traînent dans l'espace mémoire à un moment particulier.

Ils sont également thread-safe, ce qui est important car, bien que la coroutine ne soit pas nécessairement un thread, nos dispatchers dot main et dispatchers.io ont quelque chose à voir avec le threading.

Et l'autre chose qu'un objet peut faire, c'est qu'il peut en fait hériter d'une interface.

Maintenant, nous n'allons pas réellement écrire de tests unitaires dans cette application particulière, qui nécessitent les dispatchers, mais juste pour vous montrer ce que vous feriez si vous vouliez tester une classe qui a besoin d'utiliser ces contextes de coroutine, ce que vous pouvez faire, c'est simplement retourner dispatchers dot unconfined, et ensuite vous retourneriez cela pour le contexte IO et le contexte UI.

Et ensuite, c'est ce que vous utiliseriez dans un environnement de test JVM j unit.

Le package de persistance contient des classes et des fonctions qui ont pour rôle de persister ou de stocker des données au-delà du cycle de vie d'un processus Android.

Si vous ne savez pas ce qu'est un processus, cela signifie simplement un programme qui s'exécute sur un appareil.

En termes pratiques, nous allons stocker les progrès que l'utilisateur a réalisés dans le jeu Sudoku actuel, ainsi que les paramètres de ce jeu, et les records personnels ou statistiques de l'utilisateur, comme je les appelle.

Voici un aperçu rapide de l'architecture du package de persistance.

Le dépôt de jeu dans cette situation fonctionne comme un décideur de back-end pour les deux sources de données, qui coordonne les sources de données elles-mêmes.

Essayez simplement de garder les choses ensemble, ce qui a du sens à être gardé ensemble, de séparer ce qui n'a pas besoin d'être gardé ensemble, et d'utiliser également une abstraction ou une interface.

Dans tout endroit où l'implémentation pourrait changer, je pourrais décider d'arrêter d'utiliser le stockage de fichiers local ou proto data store.

Donc, cacher ces détails du dépôt n'est pas de la sur-ingénierie, mais plutôt une décision calculée.

En parlant de sources de données ou de mécanismes de stockage, nous utiliserons deux mécanismes différents pour stocker nos données.

Tout d'abord, nous allons stocker les paramètres de jeu préférés de l'utilisateur et leurs statistiques personnelles dans les données de protro data store. Data store fournit un moyen léger et efficace de stocker ce type de données en utilisant des protocoles buffers.

Protocol Buffers est un langage de sérialisation similaire à JSON.

Cependant, je le trouve plus facile à lire que JSON.

Et heureusement, la bibliothèque que nous allons utiliser vient également avec son propre compilateur protobuf qui générera une partie du code standard que nous devrions sinon écrire nous-mêmes.

Nous utilisons également le stockage de fichiers de l'appareil pour stocker les progrès de l'utilisateur dans le jeu actuellement actif.

Chaque application Android dispose d'un espace mémoire pour stocker des fichiers, que nous allons utiliser.

Cela est fait en faisant en sorte que tous les modèles de domaine implémentent serializable.

Et en utilisant Java comme flux d'entrée et de sortie pour lire et écrire des objets à partir du langage kotlin.

Donc, au cas où vous ne suivriez pas le tutoriel et que vous n'auriez pas téléchargé le dépôt de point de départ, ce que vous allez vouloir faire, c'est que vous allez vouloir ajouter un répertoire appelé pro tau dans le jeu de sources principal, le dépôt de point de départ devrait déjà avoir ce répertoire.

Donc, allez-y et cliquez avec le bouton droit dessus, et allez dans nouveau fichier.

Et ce fichier va s'appeler gain underscore settings, dot proto, et assurez-vous qu'il est tout en minuscules.

Allez-y et tapez ceci en haut du fichier.

Donc, les protocoles buffers sont essentiellement comme un langage de sérialisation.

C'est très similaire à JSON.

Si vous voulez en savoir plus, vous pouvez consulter les avantages et les inconvénients de l'utilisation de quelque chose comme JSON.

Mais personnellement, ce projet étant le seul dans lequel j'ai utilisé les protocoles buffers jusqu'à présent, j'en suis assez satisfait.

D'accord, donc ajoutons deux lignes de plus.

Et je vais expliquer un peu plus à partir de là.

D'accord, donc nous allons parler un peu plus de cela dans un instant.

Mais essentiellement, ce qui va se passer ici, c'est que nous allons définir ce message de protocole buffer, comme on l'appelle, qui est une sorte de type de données, faute de mieux.

Et ce que nous pouvons faire, c'est que ce fichier sera consommé par quelque chose appelé le compilateur de protocole buffer.

Et dans ce cas, ce que nous lui disons essentiellement, c'est que nous allons générer des fichiers Java.

Maintenant, dans les fichiers de classe générés.

Le compilateur de protocole buffer va essentiellement ajouter ce que nous mettons dans le package Java en tant que package pour le fichier de classe Java généré.

C'est juste utile pour ne pas mélanger vos espaces de noms et autres.

Et pour la deuxième option, ici, Java, plusieurs fichiers.

Si vous ne l'avez pas activé, alors ce qui peut se passer, c'est que les fichiers Java générés seront tous dans un seul fichier.

Nous ne voulons pas vraiment cela, bien que je ne sois pas sûr que ce soit absolument intégral pour faire fonctionner cette application.

Comme je le dis, nous allons passer par cela de manière assez pratique et je ne suis pas un expert en protocoles buffers.

D'accord, maintenant, nous allons faire une ligne de message qui est une sorte de l'un des principaux types de données, faute de mieux, dans ce langage particulier.

D'accord, parlons de ce que nous venons de faire ici.

Donc, nous avons défini un message, qui dans les protocoles buffers est une sorte de type de données ou une collection de champs.

Et nous avons fait deux choses.

Donc, dans le message des paramètres de jeu, nous avons des entiers 32 bits, comme une sorte de petit entier pour représenter la frontière d'un puzzle Sudoku.

Donc, lorsque je dis frontière, je veux dire comme un puzzle Sudoku de quatre par quatre aura une frontière de quatre, un puzzle Sudoku de neuf par neuf aura une frontière de neuf, évidemment.

Et l'autre chose que nous avons faite ici, c'est que nous avons défini un enum dans les protocoles buffers.

Maintenant, lorsque vous créez ces enums, vous avez besoin d'une valeur par défaut inconnue.

Et puis vous avez les autres valeurs que l'enum peut potentiellement être.

Remarquez également comment dans la frontière et la difficulté, les champs au-dessus de l'enum, je leur donne des valeurs par défaut, naturellement, celles-ci seront comme les valeurs que le protocole buffer obtient préchargées, comme la première fois que vous y accédez.

Maintenant, la chose importante à comprendre ici est que, en supposant que vous avez ajouté le support pour les protocoles buffers dans votre configuration build Gradle, le compilateur proto buffer va en fait générer certains fichiers ou classes Java à partir de ce message particulier.

D'accord, donc ce que je fais ici, c'est que j'ai ouvert le projet terminé, et je regarde simplement le fichier qui a été généré par le compilateur de protocole buffer.

Et tout ce que je veux vraiment que vous remarquiez ici, c'est que lorsque vous utilisez proto data store, ce qui va se passer, c'est qu'il va en fait générer une classe Java pour vous.

Évidemment, vous pouvez voir que nous avons nos paramètres de jeu en camel case, ce que nous avons défini comme notre message.

Et puis nous avons aussi cet enum défini ci-dessous.

Donc, qu'est-ce que cela fait pour nous, essentiellement, cela va nous permettre de sérialiser ou de traduire du Java dans le langage de protocole buffer et vice versa.

Et cela signifie aussi que nous n'avons pas besoin de créer notre propre objet Java classique pour le faire.

La bibliothèque va le générer pour nous.

Mais nous pouvons toujours l'utiliser dans notre code, ce que nous ferons dans un instant, nous allons ajouter un autre fichier proto.

Donc, allez-y et ouvrez le répertoire protobuf, cliquez à nouveau avec le bouton droit, allez dans fichier.

Et celui-ci va s'appeler user statistics dot Proto.

D'accord, donc j'ai simplement copié et collé les trois premières lignes de l'autre protocole car nous allons les réutiliser.

Et nous allons créer un autre message ici.

Maintenant, lorsque je dis statistiques, c'est une façon de parler des records personnels de l'utilisateur.

Donc, quels sont les temps les plus courts pour compléter qu'un utilisateur a fait en résolvant une taille et une difficulté particulière dans un puzzle Sudoku particulier ? C'est assez simple.

Donc, écrivons-le simplement.

Et le voilà.

Maintenant, vous vous demandez peut-être pourquoi j'utilise des entiers 64 bits ici.

Donc, ces valeurs réelles seront stockées en millisecondes, c'est pourquoi je veux le stockage d'entiers 64 bits au lieu de l'entier 32 bits.

Je ne suis pas sûr à 100% si c'est nécessaire, mais je l'ai fait juste pour être sûr, et réalistement, cela ne va pas vraiment consommer beaucoup de mémoire supplémentaire.

D'accord, donc c'est tout pour nos fichiers de protocole buffer.

Maintenant, nous allons devoir créer des protocole buffer data stores, qui est la façon dont nous allons en fait créer et accéder à nos protocole buffers.

Allez-y et cliquez avec le bouton droit sur le package de persistance, allez dans Nouveau fichier ou classe kotlin et celui-ci sera simplement un fichier appelé data stores.

D'accord, donc avant de procéder, vous allez vouloir aller dans build et make project.

Maintenant, la construction va probablement échouer, mais tout ce que nous voulions vraiment faire, c'est générer la classe Java appropriée à partir du protocole buffer.

Mais si pour une raison quelconque cela ne fonctionne pas pour vous, suivez simplement et cela fonctionnera éventuellement.

D'accord, donc pour chaque source de données basée sur le protocole buffer, nous allons devoir fournir un moyen de l'obtenir ou de la créer à partir du contexte, puis l'autre chose dont nous aurons besoin est un sérialiseur.

Allez-y et importez tout.

Et il y a deux choses que nous devons ajouter dans le délégué ici.

D'accord, donc ne vous inquiétez pas qu'il apparaisse en rouge, nous allons en fait écrire ce sérialiseur.

Ensuite, je voulais simplement expliquer ce qui se passe ici.

Donc nous créons un objet data store, et il prend la classe Java générée par le protocole buffer, qui s'appelle Game Settings.

Et essentiellement, ce que cela fait, c'est qu'il crée une référence que nous pouvons utiliser pour stocker ou récupérer notre protocole buffer.

Maintenant, vous vous demandez peut-être ce qu'est game underscore setting.pb, et pourquoi il a une extension de fichier différente de nos fichiers proto, à ma connaissance, game underscore settings.

PB est quelque chose qui est généré après coup par le compilateur, tandis que le proto est quelque chose que nous écrivons pour que le compilateur le consomme.

Mais au cas où j'aurais tort sur ce point, n'hésitez pas à me critiquer sur Twitter.

L'autre chose dont nous aurons besoin est un sérialiseur, qui s'occupe de la sérialisation, assez évidemment.

Après cela, vous pouvez simplement cliquer ici, appuyer sur alt insert, override methods, et nous n'avons besoin que des méthodes de l'interface serializer.

Donc encore une fois, lisons le code et ensuite j'expliquerai ce que je dois expliquer après coup.

D'accord, donc je vais garder les détails ici assez légers.

Donc, évidemment, lorsque nous créons notre data store, il est donné le game setting serializer ici.

Et ce que fait le serializer, c'est qu'il nous aide à lire et à écrire à partir de flux d'entrée.

Donc, en d'autres termes, nous allons évidemment lire à partir d'un fichier de protocole buffer, et ensuite cela sera sérialisé, ou plutôt désérialisé en Java, et vice versa.

Donc, essentiellement, ce que l'équipe Android a fait pour nous ici, c'est qu'ils ont rendu beaucoup plus facile la gestion des choses comme la gestion des erreurs et le traitement des flux d'entrée.

Parce que si vous avez déjà travaillé avec des flux d'entrée en Java, alors vous pouvez dire qu'il y a, vous savez, vous êtes probablement familier avec beaucoup de code standard à faire avec cela.

Donc, essentiellement, nous faisons un peu de travail standard ici.

Et cela se traduit par une API très simple, lorsque nous voulons réellement lire et écrire avec cet outil particulier dans le back-end, ce que nous allons faire dans un instant.

D'accord, maintenant, évidemment, nous devons écrire un autre data store et aussi un serializer pour l'autre type de données.

Donc, ce sera l'un de ces scénarios rares où je vais en fait simplement copier et coller parce qu'il n'y a absolument rien de nouveau, nous allons simplement changer quelques mots.

Donc, ce serait l'un des points où je vous encourage à avoir le code source complet ouvert sur le côté et ensuite vous pouvez faire un peu d'action de copier-coller, comme je vais le faire maintenant.

Et c'est notre fichier data stores complet.

Maintenant, évidemment, si vous aviez un tas de ceux-ci, vous voudriez probablement utiliser des fichiers séparés, mais puisque je n'ai que les deux, j'ai décidé de les mettre dans le même fichier, cliquez avec le bouton droit sur le package de persistance et allez dans Nouvelle classe kotlin.

Celui-ci va s'appeler local game storage ample.

Tout d'abord, nous allons créer une constante qui représentera le nom du fichier texte dans lequel nous allons lire et écrire les données du jeu.

Ensuite, nous créerons le constructeur.

Donc, vous vous demandez peut-être d'où vient un répertoire de stockage de fichiers.

Lorsque nous créons la logique de construction de cette application, qui est une sorte d'inversion de contrôle, de type injection de dépendances, ce qui va se passer, c'est que nous allons appeler cette fonction au système Android, qui nous retournera le répertoire spécifique du système où nous pouvons lire et écrire des choses comme des fichiers.

Allons-y et implémentons l'interface.

Maintenant, je vais essayer de passer cela relativement rapidement.

Mais une chose que je veux expliquer, c'est que vous remarquerez que je fais un usage assez extensif des fonctions d'assistance.

La raison en est simplement d'éviter d'écrire du code redondant.

De plus, comme pour les autres implémentations, nous allons utiliser le constructeur de co-routine avec contexte pour faire ce genre de travail d'E/S hors du thread principal.

Donc, ce que nous allons faire, c'est appeler une fonction d'assistance appelée update game data, et nous allons lui passer les données du jeu.

Et si cette opération se déroule avec succès, alors nous allons en fait simplement retourner le même objet de jeu qui a été passé car il devrait être cohérent.

D'accord, maintenant nous pouvons créer l'assistant.

Donc, ici, nous allons lancer l'exception afin qu'elle soit effectivement interceptée par le bloc catch dans les fonctions que nous allons appeler cet assistant.

Maintenant, nous allons utiliser des flux d'entrée et de sortie, qui font partie de la bibliothèque standard Java afin de noter nos données vers et depuis le fichier.

Si vous vous demandez ce que signifie ce mot flux, en fin de compte, ce que nous faisons réellement à bas niveau, c'est que nous allons prendre notre objet de jeu ou puzzle Sudoku, et nous allons le sérialiser en un flux ou une séquence très longue de caractères textuels.

Et c'est ce que nous allons réellement lire et écrire depuis le fichier.

D'accord, donc deux points, vous devez toujours fermer vos flux.

De plus, vous vous demandez peut-être comment se fait-il que nous puissions dire dot write object et passer notre puzzle Sudoku, mais vérifions simplement les paramètres ici.

Donc je vais appuyer sur Ctrl p dans les parenthèses des paramètres, et comme vous pouvez le voir, il accepte n'importe quel type.

Maintenant, l'important est que si nos différentes classes comme Sudoku puzzle et Sudoku node n'étendaient pas serializable, nous ne pourrions pas faire cela sans erreurs.

Donc pour update node, c'est un peu différent, nous mettons simplement à jour un nœud individuel.

Donc, comment cela va fonctionner, c'est que nous allons obtenir les anciennes données et ensuite nous allons simplement mettre à jour ce nœud individuel.

Et ensuite, nous réécriremos le résultat dans le stockage.

Donc get game sera un autre assistant que nous écrivons, et ce que je vais faire, c'est que je vais en fait l'écrire tout de suite.

Sinon, l'autocomplétion et la gestion des erreurs seront partout.

D'accord, c'est ce que nous devons faire là.

Maintenant, juste un petit rappel ici, lorsque nous disons couleur, et vraiment, chaque fois que quelqu'un parle d'une couleur dans une structure de données de graphe, ils parlent vraiment d'un nombre.

Donc dans ce cas, le nombre représente la valeur réelle placée dans un carré Sudoku particulier.

Donc ce sera quelque chose de un à neuf, ou de un à quatre, selon la frontière du Sudoku, nous mettrons également à jour le temps écoulé.

Après sa mise à jour, nous écrivons ce résultat dans le stockage, espérons-le.

Et juste pour garder le front-end synchronisé avec tout le reste, nous retournerons cet objet de jeu.

Maintenant, il vient de m'arriver que j'ai oublié d'ajouter un entier particulier appelé couleur à cette fonction particulière lorsque je l'ai écrite, alors allons-y et corrigeons cela maintenant.

Le voilà.

Et j'ai réussi à garder le plus facile pour la fin.

Et c'est tout pour ce fichier.

Cliquez avec le bouton droit sur le package de persistance, allez dans Nouvelle classe kotlin, celle-ci va s'appeler game repository info.

Au cas où vous auriez sauté en avant, et que vous ne seriez pas familier avec le modèle de dépôt, je l'ai en fait déjà expliqué dans la partie deux de cette série où j'ai construit le package de domaine.

Dans tous les cas, laissez-moi simplement réitérer, réitérer le but de ces classes particulières, c'est essentiellement comme un pont et un décideur pour le back-end.

Parfois, vous aurez plusieurs dépôts ou ensembles de données différents.

Dans le back-end, et il pourrait être une bonne idée de les garder séparés.

La raison pour laquelle je ne l'ai pas fait dans ce cas particulier est que le stockage de jeu et le stockage de paramètres sont en fait inextricablement liés.

Ils sont par nature étroitement liés.

Sur la base de cela, et du fait que ce n'est pas une application très grande, j'ai choisi de les mettre ensemble dans ce dépôt.

Et ensuite, comment cela fonctionnera, c'est que le dépôt coordonnera ces deux sources de données différentes.

Commençons par le constructeur et l'interface du dépôt de jeu.

D'accord, comme vous pouvez le voir, nous avons notre travail coupé pour nous.

Donc ce que je vais faire, c'est que je vais essayer d'écrire le code relativement rapidement.

Et après qu'il soit écrit, je vais expliquer ce qu'il fait.

Donc il ne devrait pas y avoir de nouveauté dans cette fonction particulière, sauf pour le fait que nous faisons une instruction d'affectation dans une instruction de contrôle, Val current game result equals etc.

Nous sommes autorisés à faire cela parce que kotlin est un langage beau et idiomatique.

Celui-ci est en fait assez simple.

Vous savez, pour la vie de moi, je ne comprends pas pourquoi il continue à mettre on air en haut.

Je vais expliquer cette fonction dans un instant.

Donc puzzle is complete est en fait une fonction qui existe dans le package de logique de calcul, que nous allons écrire plus tard, bien sûr, et tout ce qu'elle fait est exactement ce qu'elle dit.

Mais elle retournera soit vrai soit faux en fonction de si le puzzle est complet ou non.

D'où is complete.

D'accord, donc ce que j'ai fait ici, c'est que j'ai copié et collé le cas d'utilisation en langage clair qui décrit cette fonction particulière.

Maintenant, comme vous pouvez le voir, c'est assez compliqué de donner une explication de base de ce qui se passe.

Et pourquoi avons-nous fait cela lorsque nous demandons le jeu actuel, c'est-à-dire lorsque l'application démarre, il y a un certain nombre de choses différentes qui pourraient se produire.

Donc pour commencer, l'utilisateur pourrait avoir un jeu actuellement actif et il veut simplement le récupérer.

Il pourrait s'agir du premier lancement de l'application, donc aucun jeu n'existe actuellement dans le stockage.

Et puis il y a différentes situations où des erreurs pourraient se produire en cours de route.

C'est quelque chose qui arrive lorsque vous coordonnez plusieurs sources de données différentes.

Maintenant, j'ai mon propre système de suivi de ces différents flux d'événements, j'utilise essentiellement des lettres et des chiffres pour désigner les étapes et les différents flux d'événements potentiels.

Mais quoi que vous fassiez, ma suggestion pour vous est de l'écrire d'abord en langage clair puis de passer à l'écriture du code.

C'est ce que j'ai fait avec ce commentaire ci-dessus que vous voyez ici, je l'ai écrit avant d'écrire le code.

En tout cas, commençons.

D'accord, donc pour notre premier flux d'événements, nous tentons de récupérer le jeu actuel, et cela a été retourné avec succès.

Et puis nous voulons aussi savoir si le jeu actuel est complet ou non.

Nous pouvons simplement nous débarrasser de oncomplete.

Et nous y voilà à nouveau.

Donc, c'est évidemment le cas où l'utilisateur a chargé l'application pour la première fois et nous voulons créer un tout nouveau jeu.

Et il semble que je vais devoir le faire manuellement cette fois.

L'autocomplétion ne m'aide pas ici.

Mais pour être juste, nous n'avons pas encore écrit cette fonction.

D'accord, je vais juste vérifier que je l'ai écrit correctement.

Maintenant, avant de vouloir continuer, je veux expliquer une chose sur ma perspective de l'architecture logicielle.

Alors que parfois dans une application plus simple, nous pouvons faire quelque chose comme avoir le présentateur coordonner différents dépôts ou sources de données back-end.

Dans ce cas particulier, il y avait suffisamment de logique back-end compliquée pour que je veuille avoir aussi une classe de décideur, qui s'est avérée être cette implémentation de dépôt de jeu sur le back-end, et une partie du but de cette classe est de s'occuper de la logique de coordination de ces différentes sources de données back-end, afin que je puisse garder la classe de logique de présentation à faire ce qu'elle est censée faire, gérer la logique de présentation, et ensuite j'ai cette classe qui s'occupe de cette logique de type presque métier ici.

En tout cas, nous n'avons pas encore terminé.

D'accord, il vient de me venir à l'esprit que j'ai manqué une fonction dans l'interface d'un dépôt de jeu.

Donc, allons-y et ajoutons cela maintenant.

Donc, ce que je vais faire, c'est que je vais copier update game, le coller ci-dessous.

Et ce que nous allons appeler, c'est create new game.

Et il va prendre un objet settings et c'est tout.

Donc, c'est en fait une fonction d'assistance que j'ai créée principalement pour la lisibilité, allons-y et ajoutons cela maintenant.

Juste une autre note rapide ici, vous remarquerez que j'aime les noms incroyablement longs et descriptifs de tout ce qui se passe.

C'est en grande partie parce que je n'ai pas une grande mémoire pour les détails fins.

En rendant ces choses super longues et descriptives, je n'ai pas besoin de les mémoriser, je peux simplement lire mon code et comprendre ce qu'il fait.

Même dans ces situations compliquées où nous avons tous ces différents flux d'événements et interactions qui se produisent, d'accord, seulement deux fonctions courtes de plus à faire.

Et c'est tout pour notre back-end.

Au niveau supérieur du package UI, nous avons quatre petits fichiers que nous utiliserons pour créer et appliquer des styles, des couleurs, des polices, et ainsi de suite.

L'un de ces fichiers est le thème global de notre application.

Et je vais vous montrer comment créer à la fois un thème clair et un thème sombre pour l'application en seulement quelques lignes de code supplémentaires.

Restez à l'écoute pour la fin de cette section, car je vais faire une démonstration en direct des différents thèmes.

Cliquez avec le bouton droit sur le package UI et créez un nouveau fichier kotlin, qui s'appellera color dot Katie.

Ce fichier sera essentiellement un remplacement pour colors dot XML, si vous êtes habitué à travailler avec l'ancien système de ressources, qui était basé sur XML, créons un objet color.

Assurez-vous d'importer la classe Compose color.

D'accord, avant de procéder, la chose la plus importante à comprendre ici est comment lire ces valeurs particulières.

Donc, les deux premiers caractères ici 0x.

Cela indique essentiellement au compilateur, qui est le programme qui lira ce code, qu'il s'agit en fait d'un nombre hexadécimal.

Les deux chiffres suivants ici indiquent la valeur alpha en pourcentage.

Alpha est une autre façon de dire transparence ou à quel point quelque chose est opaque.

Les trois paires restantes sont les valeurs rouge, bleu et vert ou RVB, à nouveau en pourcentage hexadécimal, et c'est à peu près tout ce qu'il y a à savoir sur ces différentes valeurs de couleur.

J'ai copié et collé le reste des valeurs car il n'y a absolument aucun intérêt à taper tout cela.

Mais gardez également à l'esprit qu'ils ont certaines valeurs prédéfinies telles que flack, par exemple, que vous pouvez également utiliser. Cliquez avec le bouton droit sur le package UI, et nous allons créer un autre nouveau fichier kotlin.

Et celui-ci va s'appeler shape.

Donc, dans l'ancien système de vue, lorsque vous vouliez faire quelque chose comme créer un arrière-plan avec des coins arrondis, ou un bouton ou un widget ou quelque chose de ce genre, vous deviez créer habituellement quelque chose à l'intérieur du dossier drawable, qui était basé sur XML.

Encore une fois, puisque c'est compose, nous pouvons simplement aller de l'avant et faire cela en kotlin.

Au lieu de cela, hé, je vais simplement utiliser quelques paramètres par défaut.

Maintenant, ce pourrait être votre première fois en voyant l'extension .dp, jetons un rapide coup d'œil au code source.

Comme vous pouvez le voir, vous pouvez simplement l'ajouter à un entier, un double et divers types de nombres.

La chose importante à comprendre ici est que cela indique essentiellement au framework Compose que nous voulons utiliser des pixels indépendants de la densité.

Si vous voulez une explication plus profonde de ce que sont exactement ces pixels, je vous suggère fortement de vous renseigner à ce sujet car c'est un peu compliqué.

Il suffit de dire que l'idée ici est de permettre au framework de créer des valeurs pour les hauteurs et les largeurs et autres choses qui fonctionneraient sur une variété de tailles d'écran et de facteurs de forme.

Cliquez avec le bouton droit sur le package UI, et nous allons créer un autre fichier kotlin, celui-ci va s'appeler type.

Maintenant, au cas où vous vous poseriez la question, lorsque nous disons type, nous ne parlons pas vraiment d'un système de types, ou de quoi que ce soit ayant trait à la théorie des types, cela a trait à la typographie ou au texte et à la manière dont ce texte est stylisé ou présenté.

Donc encore une fois, c'est exactement le genre de chose que nous faisions dans styles dot XML, nous allons essentiellement créer un tas de styles de texte différents, que nous utiliserons dans toute l'application.

Et ensuite, nous allons les regrouper dans un objet de typographie.

Et ensuite, nous verrons comment ajouter cet objet de typographie à notre thème compose global.

Tout d'abord, créons un style de texte.

Parfois, nous avons une situation où nous voulons garder un tas de valeurs par défaut, mais nous voulons peut-être une ou deux valeurs, qui sont en fait passées en tant que paramètre pour créer l'objet de style de texte.

Donc, je vais vous montrer une autre façon de créer ces styles de texte en utilisant une fonction.

Je vais faire un peu de copier-coller rapide ici.

Et ensuite, nous pouvons remplacer la couleur.

Donc encore une fois, ce que je vais faire pour le reste de ces textiles maintenant que nous avons vu tout ce qu'il y a à voir ici, c'est que je vais les copier et les coller.

Mais il y a une chose de plus qui est nouvelle que nous devons créer dans ce fichier particulier.

D'accord, comme vous pouvez le voir, nous avons quelques textiles différents ici.

Donc, la dernière chose que nous devons faire est de créer un objet de typographie.

Donc, essentiellement, cela signifie que nous allons attribuer certains des styles de texte que nous avons créés ci-dessous, qui sont utilisés dans des choses courantes comme le texte du corps d'une fonctionnalité particulière de l'application, des boutons, des titres, ce genre de choses.

Si cela n'a pas de sens.

Écrivons simplement le code.

Assurez-vous de sélectionner compose dot material, pas kotlin dot txt.

D'accord, nous allons simplement en faire deux de plus.

Très bien, et la seule autre chose que nous devons faire est de configurer notre thème graphique Sudoku.

Cliquez avec le bouton droit sur le package UI, et nous avons, vous l'avez deviné, un autre fichier kotlin.

Et il va s'appeler graph Sudoku themed.

Donc, l'une des petites fonctionnalités pratiques de jetpack compose est qu'il est incroyablement facile de créer un thème pour les modes clair et sombre.

En tant que personne qui utilise généralement le mode sombre presque toujours, j'apprécie vraiment cette fonctionnalité particulière de compose.

La première étape de ce processus est de créer deux palettes de couleurs différentes.

Commençons par la palette de couleurs claire.

Donc, certaines de ces propriétés devraient probablement être familières à la plupart des développeurs Android, comme avoir une couleur primaire.

C'est ainsi que nous le faisions aussi dans l'ancien système XML avec les couleurs, ou du moins c'était une convention de nommage courante.

Maintenant, une chose que je veux souligner ici, c'est qu'il y a un degré auquel certaines de ces plus obscures comme la variante primaire, la surface sur la primaire et ainsi de suite, je les utilise vraiment juste parce que c'est pratique, elles ne doivent pas nécessairement signifier quelque chose de particulier.

Mais la chose importante à comprendre ici est que si une couleur est différente entre un thème clair et un thème sombre, nous voulons la définir quelque part ici, et ensuite l'utiliser de manière appropriée dans le composable, ce que nous apprendrons à faire plus tard.

D'accord, cela était en fait censé être en majuscules là par convention.

Et remarquez aussi que j'ai copié-collé la palette de couleurs sombres, car encore une fois, il ne se passe rien de nouveau là.

L'étape suivante, cependant, est très importante, nous allons créer notre thème, et cela va être vraiment, vraiment facile.

Voici un petit raccourci que j'ai appris d'un ami, si vous voulez créer une fonction composable vraiment rapidement, commencez à taper comp, puis appuyez sur entrer, cela vous fait gagner un peu de temps.

Maintenant, ce thème va avoir deux paramètres ici.

Avant d'écrire le corps de cette fonction, je voulais simplement discuter de ces deux paramètres.

Comme vous pouvez le voir, nous faisons en fait un appel de fonction is system in dark theme, ce qui va se passer, c'est que cet appel système va retourner un booléen, qui nous dira si l'utilisateur a spécifié si l'application est censée être en mode sombre ou en mode clair.

Et ensuite le contenu représente tout ce qui sera enveloppé à l'intérieur de ce thème.

Ce qui est important à comprendre ici, c'est que tout ce que nous mettons à l'intérieur de ce composable, c'est-à-dire le contenu, aura accès à toutes ces différentes couleurs, styles et informations de typographie à partir du thème lui-même.

L'utilité réelle de cela aura beaucoup plus de sens lorsque nous écrivons réellement le composable.

Juste pour terminer les choses, nous allons créer un thème de matériel composable.

Et nous n'aurons pas besoin de l'expression lambda.

Donc, le voilà, il n'a fallu que quelques minutes pour créer les ressources de couleur et les styles et les informations de typographie nécessaires pour rendre à la fois une palette de couleurs sombre et une palette de couleurs claire pour différents modes.

Ce que je vais faire, c'est vous montrer une démonstration rapide de ce à quoi cela ressemble réellement dans une application.

Ici, je vais démarrer l'application dans le thème clair.

Ensuite, je vais naviguer vers les paramètres du système d'exploitation et le définir en mode sombre préféré.

Et en revenant, nous voyons immédiatement que l'application utilise maintenant le thème sombre.

Nous sommes maintenant prêts à commencer à construire notre interface utilisateur.

Le package UI components contient des éléments réutilisables de l'interface utilisateur.

Puisque c'est une très petite application, les seuls deux éléments sont une barre d'outils et un écran de chargement.

L'une des grandes fonctionnalités de compose est que nous pouvons rendre nos composants réutilisables de différentes manières.

Tout d'abord, si un composant doit être positionné selon l'endroit où il s'adapte dans différents composables parents ou écrans parents, nous pouvons passer un modificateur au lieu de créer un modificateur dans le composable enfant.

Cela vaut la peine d'expérimenter si vous ne l'avez pas déjà fait.

Deuxièmement, il est possible de passer des composables en tant qu'arguments, ce qui permet également la réutilisation et l'extension de la fonctionnalité.

Dans cette application, nous voulons différentes icônes de barre d'outils pour les deux écrans UI différents.

Et nous pouvons y parvenir en passant les icônes composables.

À partir de ces écrans UI parents, vous verrez plus tard comment nous pouvons spécifier et gérer différentes icônes et différents événements de clic.

L'utilisation de la même barre d'outils créera également cet écran de chargement réutilisable et plus tard, je vous montrerai comment l'animer, cliquez avec le bouton droit sur le package UI et allez dans nouveau package.

Et celui-ci va s'appeler components.

Juste une brève explication ici, j'ai adopté cette convention particulière à partir du dépôt des échantillons composés.

Donc, ce qui ira dans ce dossier particulier sont les composables, qui finiront par être réutilisables dans une variété d'éléments UI différents et d'écrans différents.

Dans ce cas, nous allons créer une barre d'outils réutilisable, ainsi qu'un écran de chargement réutilisable, cliquez avec le bouton droit sur le dossier des composants, et allez dans Nouveau fichier kotlin, et celui-ci va s'appeler app toolbar.

Créons notre fonction de stub, ce que je vais faire, c'est taper co MP et ensuite l'autocomplétion créera une fonction composable.

Celui-ci va s'appeler app toolbar.

Tout d'abord, écrivons la liste des paramètres et je vais l'expliquer un peu.

Assurez-vous de sélectionner le modificateur compose.ui.

Commençons par parler un peu des modificateurs.

Donc, les modificateurs sont essentiellement la façon dont vous pouvez créer la plupart de ces styles, tailles et données de position pour un composable particulier.

Maintenant, il y a deux façons principales de faire cela.

Nous pourrions bien sûr créer ce modificateur et l'utiliser dans ce widget.

Mais ce serait pour une situation où le widget lui-même va décider de ce type d'information.

Puisque nous utilisons un composant réutilisable ici, une app toolbar, que nous prévoyons d'utiliser à plusieurs endroits différents.

Dans cette situation particulière, nous allons passer le modificateur dans cette fonction, ce qui est une façon de dire que le composable parent décidera en fait où positionner et comment dimensionner cet élément UI particulier.

Le titre est assez explicite, mais ce qui est un peu plus compliqué, c'est l'icône.

Et encore une fois, cela sera dicté par quelque chose dans le composable parent.

C'est ainsi que je rends cette chose réutilisable et lui permet de gérer différentes icônes ou différentes actions lorsqu'elle est cliquée.

Après avoir terminé ce composable particulier, je vais vous montrer un aperçu rapide de l'icône réelle que nous allons utiliser.

Donc, espérons que cela aura un peu plus de sens.

La première chose que nous voulons faire est de remplacer le composable de la barre d'applications supérieure.

Faisons une pause un instant et parlons des différentes couleurs.

Donc, une façon de résoudre ce problème serait de coder en dur une sorte de couleur ici.

Mais dans la section précédente de ce tutoriel, nous avons pris la peine de configurer à la fois un thème clair et un thème sombre.

Donc, ce que nous faisons ici, c'est que nous allons en fait utiliser une couleur qui est basée sur le thème.

Rappelons que dans le composable graph Sudoku theme, il y avait un appel à une fonction qui était his system and dark theme ou quelque chose de ce genre.

Et cela va en fait dicter quelle palette de couleurs nous sélectionnons.

Donc, en utilisant material theme colors dot primary, il héritera automatiquement de la couleur appropriée en fonction du fait que nous soyons en mode clair ou sombre.

Et ce serait une raison d'éviter de coder en dur quelque chose ici.

Dans ce cas, nous avons une couleur qui sera la même, qu'il s'agisse du mode clair ou sombre.

Donc, nous allons simplement ajouter un composable de texte qui est effectivement une vue supplémentaire.

Mais si vous vouliez ajouter quelque chose comme un logo pour l'application avant ou après le texte du titre, et ce que vous pourriez faire, c'est que vous pourriez ajouter une ligne ici et ensuite simplement ajouter à la fois l'icône et ensuite le composable de texte.

Et ensuite vous seriez prêt à partir.

Allez-y et importez cela.

Cela est probablement assez explicite.

Mais lorsque nous voulons hériter des données de style pour des polices particulières et autres, alors c'est ainsi que nous pouvons le faire.

Encore une fois, c'est quelque chose de super pratique.

Et vous ne voyez cela qu'en kotlin, certainement pas en Java.

Donc, ce que nous faisons ici, c'est que nous demandons explicitement si l'application est actuellement en mode clair, puis nous choisissons une couleur de texte en fonction de cela.

C'est vraiment juste une autre façon de gérer cette logique d'interface utilisateur conditionnelle sans avoir à assigner quelque chose à un thème spécifiquement.

Ensuite, nous allons gérer l'alignement.

Et c'est tout pour le composable de texte dans notre barre d'outils.

Donc, action bar est probablement quelque chose qui sera plus familier aux anciens développeurs Android.

Mais pensez simplement à cela comme les icônes dans la barre d'outils.

Généralement, elles sont utilisées pour des actions très importantes dans l'interface utilisateur, comme naviguer vers une nouvelle fonctionnalité, indiquer que vous avez terminé de faire quelque chose.

Et notez surtout que cette fonction lambda particulière est de type row scope.

Donc, essentiellement, ce que cela signifie, c'est que si vous avez plusieurs boutons d'action, vous pouvez les placer dans ces deux crochets ici, et ils seront automatiquement alignés comme une rangée.

Maintenant, tout ce que nous devons faire, c'est taper icon et ensuite ajouter les parenthèses ici.

Et c'est parce que nous allons en fait passer cette icône depuis le composable parent.

Comme je l'ai dit il y a un instant, je voulais simplement vous donner un aperçu de l'icône elle-même.

Nous ne allons pas l'écrire encore, mais nous le ferons plus tard.

La chose importante à comprendre ici est que nous décidons de la manière de gérer le clic et de ce à quoi ressemble cette chose dans le composable parent, nous ne le faisons pas réellement dans la barre d'outils.

Et en retirant cette responsabilité de la barre d'outils, c'est ainsi que nous obtenons la réutilisabilité que nous voulons.

Cliquez avec le bouton droit sur le package des composants, allez dans Nouveau fichier kotlin, et celui-ci va s'appeler loading screen.

Créons notre composable de chargement.

La première chose dont nous aurons besoin est une surface.

Donc, vous vous demandez peut-être pourquoi nous utilisons une surface ici en particulier, dans ce cas, je veux vraiment une surface de l'interface utilisateur qui a une couleur et des dimensions spécifiques.

Ici, j'ai défini Phil max height à une fraction de point huit F, ce qui signifie essentiellement que je veux qu'il occupe la plupart de la largeur, ou désolé, la plupart de la hauteur de l'interface utilisateur.

Mais je pourrais vouloir un espace pour quelque chose comme une bannière publicitaire ou quelque chose de ce genre.

En tout cas, je veux essentiellement une icône ou une image qui est empilée sur une barre de progression qui sera empilée sur un texte.

Donc pour ce genre de situation, évidemment, nous allons vouloir utiliser une colonne.

Évidemment, nous allons centrer les choses.

Allez-y et importez cela.

Maintenant, je remarque qu'il ne s'importe pas correctement, je pense qu'il y a quelque chose dans les bibliothèques Compose qui imite notre importation, alors laissez-moi simplement corriger ces imports avant de continuer.

Comme vous pouvez le voir ici, je viens de copier et collé notre importation.

Et maintenant, nous sommes prêts à partir.

C'est notre logo.

Voici votre barre de progression.

D'accord, donc vous vous demandez peut-être ce que signifie cette chose de peintre.

Donc, essentiellement, dans la version alpha de compose, nous devions spécifier s'il s'agissait d'un actif vectoriel ou d'un actif bitmap et autres.

Donc, nous pouvons simplement utiliser cette chose de ressource de peintre générique et la pointer vers n'importe quoi dans notre drawable.

Et il déterminera en fait s'il s'agit d'un bitmap ou d'un actif vectoriel.

De plus, je voulais souligner la fonction de copie ici.

Supposons que vous avez une couleur et que vous voulez changer légèrement la valeur alpha ou que vous avez un de ces objets textiles et que vous voulez y apporter une sorte de changement.

La fonction de copie est super pratique pour cela.

Dans cette partie du tutoriel, nous allons créer la classe sealed event, le view model et le présentateur pour la fonctionnalité de jeu actif.

Avant de faire cela, examinons quelques décisions de conception impliquées dans cette architecture.

Le but de notre classe de logique de présentation, que j'appelle logique pour faire court, est exactement comme le nom l'indique, elle gère le travail de coordination du view model du conteneur et des dépôts backend.

Si elle est notifiée d'un événement non stop, elle annulera également toutes les co-routines, elle ne possède aucun code de plateforme Android, ce qui la rend faiblement couplée et très facile à tester.

Je pourrais également envisager de la réutiliser pour une version de bureau de cette application.

Mais nous verrons.

Le but du view model est également de faire exactement ce que le nom implique, c'est une représentation virtuelle de l'interface utilisateur, que la vue observe.

En termes plus simples, c'est un modèle de la vue, il expose des types de fonction, qui est une compréhension très simple et facile pour le modèle d'observateur.

Dans les situations où nous n'avons pas besoin de plusieurs observateurs.

Chaque fois que notre classe de logique met à jour le view model, le view model publiera automatiquement les nouvelles données à la vue.

Une autre décision de conception avec ce view model est qu'il n'étend pas le view model jetpack.

Il y a plusieurs raisons à cette décision, certaines simples, d'autres assez techniques.

La raison simple est que l'utilisation du view model jetpack crée un couplage serré avec la plateforme Android.

Et il a son propre ensemble de code standard et de dépendances, dont je ne suis pas un grand fan.

En bref, il ne résout pas plus de problèmes qu'il n'en crée dans cette application particulière.

Et je voulais pratiquer la création de view models qui pourraient être utilisables pour kotlin desktop ou kotlin.

j s.

La raison technique est que dans cette application, nous n'avons pas besoin de persister les données à travers les instances d'activité ou la mort du processus afin d'avoir une bonne expérience utilisateur.

Au lieu de cela, nous faisons simplement un appel assez bon marché au système de fichiers Android et rechargeons les données à partir de là si de tels événements se produisent.

Maintenant, avant d'appliquer ce raisonnement dans chaque situation, comprenez que le rechargement des données à partir d'un système de fichiers fonctionne bien dans cette application, mais ne doit pas être considéré comme un remplacement approprié pour l'état d'instance non sauvegardé dans chaque application que vous écrivez.

Si vous aimez les modèles dans le handle d'état sauvegardé, allez-y et utilisez-le.

Nous employons également le modèle de stratégie pour nettoyer l'interface que notre classe de logique expose au conteneur et à la vue.

Chaque sous-classe de la classe scellée représente une action qui peut se produire dans la vue ou le conteneur.

Plutôt que d'avoir une fonction pour chaque événement UI.

Nous avons une fonction qui accepte un seul objet qui peut représenter plusieurs chemins d'exécution différents.

C'est le modèle de stratégie.

Cliquez avec le bouton droit sur le package UI, et allez dans un nouveau package appelé active game, cliquez avec le bouton droit sur ce nouveau package, allez dans Nouveau fichier ou classe kotlin, et nous allons créer une interface, et elle va s'appeler active game container.

Ce mot conteneur est un terme technique.

La façon dont je l'utilise ici est de signifier quelque chose qui contient une grande partie d'une application ou une application entière.

À mon avis, un conteneur ne traite généralement pas beaucoup de la logique métier de l'application.

Il relie essentiellement les choses ensemble et construit les choses et sert de point d'entrée.

Dans la prochaine partie de ce tutoriel, j'expliquerai ce que nous allons utiliser comme conteneur.

Mais en utilisant une interface ici, je dis assez explicitement que je pourrais changer d'avis sur ce que nous utilisons comme conteneur.

En tout cas, il ne contient que deux fonctions abstraites.

Cliquez à nouveau avec le bouton droit sur le package active game, et nous allons créer une classe scellée cette fois.

Et elle va s'appeler active game event.

Donc, comme je l'ai expliqué dans le commentaire ci-dessus, la classe scellée active game event représente chaque type d'interaction utilisateur d'une fonctionnalité donnée, dans ce cas, la fonctionnalité de jeu actif.

C'est un modèle très courant que j'utilise et nous verrons comment il fonctionne avec notre classe abstraite base logic que nous avons créée dans le package commun.

D'accord, nous allons maintenant créer notre view model.

Tout d'abord, créons une petite classe ici qui sera comme une représentation virtuelle d'une seule tuile dans un puzzle Sudoku.

Donc, évidemment, x&y représentent les coordonnées x&y de la tuile Sudoku particulière, la valeur représentera ce dont nous avons parlé dans les structures de données de graphes comme la couleur, encore une fois, c'est littéralement juste un nombre, je ne sais pas pourquoi nous devons l'appeler une couleur.

Maintenant, has focused indique que l'utilisateur a cliqué sur une tuile particulière, après quoi il peut cliquer sur l'un des boutons d'entrée pour changer ce nombre particulier.

Et enfin, une tuile en lecture seule peut être considérée comme une tuile qui est comme un indice donné dans le puzzle.

Par conséquent, l'utilisateur n'est pas autorisé à changer les tuiles en lecture seule.

Avant de commencer à lire ce view model, je voulais simplement mentionner quelques points ici.

Comme discuté dans l'introduction de cette section particulière, je ne voulais pas utiliser les bibliothèques jetpack pour réaliser une relation éditeur-abonné entre le view model et la vue.

Il s'avère que cette relation éditeur-abonné ou ce modèle est en fait assez facile à implémenter.

Mais dans ce cas, j'ai en fait trouvé plus simple d'utiliser les types de fonction kotlin pour réaliser ce que j'appellerais un modèle éditeur-abonné de pauvre ou un modèle observateur.

Donc, cela signifie vraiment quelque chose de simple en pratique, bien que cela puisse sembler un peu compliqué pour ceux qui ne sont pas vraiment familiers avec le travail avec les types de fonction.

Notre view model possédera ces références de type de fonction nulles.

Comme nous le verrons dans un instant, ce que nous pouvons faire, c'est que chaque fois que nous mettons à jour le view model à partir de la classe de logique de présentation, nous pouvons ensuite mettre à jour la vue par extension en invoquant ces types de fonction à partir du view model.

Maintenant, la raison pour laquelle nous utilisons des nuls ici est que, à partir du view model.

Je ne peux jamais être sûr à 100% s'il y a effectivement quelque chose qui écoute.

Mais cela dit, j'ai l'impression que si je jouais avec cette classe particulière pendant quelques heures, je pourrais probablement rationaliser un peu et peut-être rendre certaines de ces variables internes privées ou quelque chose de ce genre.

Donc, ce que je dis vraiment ici, c'est que vous pouvez prendre cette idée générale d'avoir un view model qui n'est pas fortement couplé à Android jetpack, mais aussi vous pouvez expérimenter avec et voir si vous pouvez l'optimiser.

Avec cela en tête, créons quelques types de fonction.

Donc, tous ces types de fonction seront préfixés avec sub pour assurer une bonne lisibilité.

Active game screen state est en fait quelque chose que nous allons créer dans la prochaine partie de ce tutoriel.

Donc, allez-y et laissez-le briller en rouge ici.

D'accord, laissez-moi simplement expliquer brièvement ces différents types de fonction.

Donc, le board state est essentiellement une représentation virtuelle du tableau Sudoku.

Évidemment, le content state signifie simplement trois états différents.

Donc, soit nous chargeons les données, l'utilisateur a un jeu actuellement actif qu'il résout, ou l'utilisateur a complété un jeu particulier, nous utiliserons cela pour animer entre différents états dans l'interface utilisateur.

Maintenant, le timer state a à voir avec le compteur de temps, qui enregistre essentiellement combien de temps il faut à l'utilisateur pour compléter un jeu Sudoku donné.

Donc, juste pour espérer clarifier toute confusion ici, le timer state sera la valeur longue réelle en millisecondes représentant le temps et ensuite sub timer state est la façon dont nous mettons à jour l'interface utilisateur après avoir mis à jour le nouveau timer state.

Terminons le reste de ces variables.

Ce sont des valeurs par défaut assez évidentes.

Ensuite, nous écrirons une fonction pour initialiser ce view model.

D'accord, faisons une pause un instant.

Ce que nous faisons ici, c'est que nous prenons l'état des données tel qu'il existait dans le stockage, nous le donnons au view model, et ensuite ce que nous faisons, c'est que nous construisons la propre représentation virtuelle de cet état par le view model.

Maintenant, les représentations internes du view model auront des choses comme has focus, qui sont spécifiquement concernées par l'interface utilisateur et pas nécessairement quelque chose que j'inclurais dans le modèle de domaine original.

De plus, au cas où vous vous poseriez la question, la valeur clé est essentiellement créée à partir du hachage de la valeur x et de la valeur y.

C'est quelque chose que nous avons couvert très tôt dans ce tutoriel, au cas où vous auriez sauté en avant.

Encore une fois, active gain screen state est quelque chose que nous allons créer dans la partie Compose du tutoriel.

Ici, nous liaisons ces données au view model.

Et ensuite, nous invoquerons nos types de fonction pour mettre à jour la vue en supposant qu'elle écoute.

Et c'est tout pour notre fonction init.

Maintenant, nous avons juste quelques fonctions de plus, qui seront appelées par notre présentateur pour faire diverses choses avec l'état du view model.

Donc, ici, nous mettons simplement à jour une tuile individuelle.

Donc, ce que nous faisons ici, c'est que lorsque l'utilisateur clique sur une tuile particulière, cela envoie un message au présentateur, qui aura une coordonnée x et y particulière, puis le présentateur appellera cette fonction particulière.

Et donc, ce qu'il fera, c'est qu'il cherchera la tuile sur laquelle l'utilisateur a cliqué en fonction de cette valeur X et Y, et la définira à has focus equals true.

Et ensuite, pour chaque autre tuile, nous voulons la définir à false.

Sinon, nous pourrions avoir une situation où l'utilisateur a sélectionné plusieurs tuiles différentes, ce que notre application n'est pas censée permettre de faire, et ce serait la situation où notre back-end a déterminé que le puzzle actuel est complet.

Cliquez avec le bouton droit sur le package active game.

Et créons une nouvelle classe kotlin, qui va s'appeler active game logic.

D'accord, donc avant de procéder, c'est définitivement l'une de ces situations où je suggère fortement d'avoir le code source complet ouvert sur le côté pendant que vous suivez ici.

Évidemment, je vais faire de mon mieux pour ne pas faire d'erreurs, mais il est possible que j'en fasse.

Active game logic représente la logique de présentation de cette fonctionnalité particulière de l'application.

Comme nous le verrons, elle coordonne entre le conteneur, le view model, et par extension, la vue, ainsi que le back-end de l'application.

Commençons par le constructeur.

D'accord, juste un peu de révision avant de continuer, pour l'instant le conteneur sera en fait une activité.

Mais il y a une possibilité dans le futur, je pourrais passer à l'utilisation de fragments comme conteneurs à la place, à ce stade, je ne veux pas vraiment le faire, mais nous verrons si cela a du sens dans le futur.

Mais c'est toute la raison pour laquelle j'ai inclus une interface ici afin que je puisse changer ce qui se cache derrière l'interface très facilement.

Le view model est assez clair, nous venons de l'écrire.

Game repo est l'endroit où nous stockons les données de jeu.

Donc, cela inclut les paramètres de jeu ainsi que la progression actuelle du jeu de l'utilisateur.

Repple est l'endroit où nous stockons les records pour les temps les plus courts de complétion de chaque difficulté et taille de puzzle différente.

Et si vous vous demandez ce qu'est le dispatcher, revenez en arrière et regardez le package commun lorsque nous l'avons créé, nous avons créé ce fournisseur de dispatcher et j'ai essentiellement expliqué quel est son but.

Base logic est aussi quelque chose que nous avons créé dans le package commun.

Et nous verrons la fonction que nous héritons de cette classe dans un instant.

D'accord, commençons par parler des co-routines.

Donc, une façon de penser aux portées, que nous parlions de la portée des co-routines, ou de dagger ou autre chose, est de considérer simplement qu'il s'agit d'un cycle de vie.

Maintenant, vous vous demandez probablement, pourquoi ne faisons-nous pas quelque chose comme un view model ou un fragment ou une activité, notre classe de cycle de vie ? Eh bien, au cas où vous ne l'auriez pas remarqué jusqu'à présent, je n'aime pas les couplages serrés avec la plateforme Android, si je peux l'éviter.

Il y a un certain nombre d'autres raisons.

Mais l'une des principales est que, parce que cette classe contient toute la logique de présentation, dans un sens, c'est le principal décideur pour cette fonctionnalité de l'application, alors, à mon avis, il est logique de la rendre responsable de l'annulation de toute co-routine qui se trouve être en cours d'exécution, en ce qui concerne cette fonction on event, que nous héritons de base logic.

Eh bien, essentiellement, c'est une implémentation du modèle de stratégie.

Je ne vais pas vous donner une longue et technique explication ici.

C'est en fait un modèle très simple.

Mais essentiellement, il fournit une sorte de point d'entrée unique dans cette classe particulière.

Donc, au lieu d'avoir une seule fonction pour chaque événement, nous avons une fonction qui prend un argument, notre active game event, qui est capable de représenter tous les différents événements, et je trouve que cela nettoie vraiment les interfaces entre les différentes classes, les interfaces sont utilisées dans le sens général dans cette déclaration.

D'accord, implémentons d'abord notre contexte de co-routine.

Rappelons que jobtracker existe dans base logic, mais nous devons aussi l'initialiser. D'accord, maintenant avant de procéder, il y a quelque chose de vraiment important que nous devons implémenter, qui est un minuteur de co-routine.

Comme je l'ai mentionné auparavant, l'écran de jeu actif dispose d'un minuteur de compte à rebours.

Maintenant, certains d'entre vous se demandent probablement pourquoi je n'ai pas utilisé la classe Java Timer ou le minuteur de compte à rebours d'Android ou quelque chose de ce genre.

En fait, j'ai essayé d'utiliser ces choses.

Et elles ont présenté différents problèmes de rupture d'application.

Et il s'est avéré que c'était plus facile de créer ce genre de minuteur de co-routine.

D'accord, donc cela nécessite un peu d'explication, évidemment.

Donc, nous allons remarquer deux mots-clés différents ici, qui pourraient être inconnus pour certains d'entre vous, nous avons les mots-clés inline et cross inline.

Donc, chaque fois que vous voyez le mot-clé inline, la manière la plus simple de le comprendre est de comprendre que cela signifie simplement copier, coller.

Et si vous voulez savoir ce que cela signifie en code, alors je vous suggère de décompiler un peu de votre code kotlin qui utilise le modificateur inline, et vous verrez comment la fonction inline est en fait copiée et collée dans le site d'appel.

Maintenant, nous avons quelque chose d'autre qui se passe ici, qui est une fonction de type cross inline.

Donc, avant d'expliquer ce que fait l'action cross inline, parlons de ce que fait cette fonction.

Donc, ici nous avons une boucle de spin assez standard, while true.

Donc, c'est une boucle qui va simplement s'exécuter indéfiniment, elle va invoquer ce type de fonction, et ensuite elle va retarder de 1000 millisecondes.

Maintenant, il y a quelques choses différentes qui se passent ici.

Numéro un, vous devez comprendre que nous allons retarder cette co-routine, mais elle ne va pas réellement bloquer le thread sur lequel elle se trouve, ce qui est bien sûr un grand avantage.

Maintenant, l'autre chose qui se passe ici, c'est que l'action va être une expression lambda que nous allons passer dans cette fonction particulière.

Vraiment, la seule chose que fait cross inline, c'est qu'elle fait en sorte que dans la fonction lambda que nous allons passer dans cette fonction ici, nous ne soyons pas autorisés à écrire une instruction return dans cette fonction.

Donc, dans le sens le plus général ici, ce que nous faisons, c'est que nous prenons une mesure préventive, pour éviter une situation où nous pourrions accidentellement retourner de la lambda que nous passons ici, causant un comportement inattendu.

Maintenant, vous vous demandez probablement, puisque nous avons cette boucle sans fin, comment arrêtons-nous cette co-routine particulière ? Eh bien, ce que nous allons faire, c'est que nous allons créer un job.

Faisons cela maintenant.

Et ce que nous allons faire bientôt, c'est que nous allons en fait attribuer cette variable de job à notre start co-routine timer, et cela nous permettra de l'annuler.

Écrivons simplement une autre fonction d'extension rapide concernant cette affaire de timer et ensuite j'expliquerai ce qu'elle fait.

En expérimentant avec l'interface utilisateur, comment rendre le timer le moins saccadé ou le plus précis possible, il s'est avéré que soustraire un de la valeur chaque fois que nous l'écrivons dans le back-end créait un timer plus cohérent.

Mais un cas particulier est si la valeur est égale à zéro, alors évidemment nous ne voulons pas soustraire un de celle-ci.

Sinon, le timer dira moins un au début et cela ne semble pas très bien.

D'accord, donc avec tout cela fait, nous pouvons passer à l'implémentation du reste de la logique de présentation. D'accord, donc lorsque l'utilisateur appuie sur un bouton d'entrée, nous pouvons avoir deux situations différentes qui pourraient se produire.

Dans une situation, l'utilisateur a déjà sélectionné une tuile, qui deviendrait la tuile de focus.

Ou il pourrait être qu'ils ont simplement appuyé sur un bouton d'entrée sans avoir réellement mis au point une tuile, auquel cas, nous ne voulons vraiment rien faire.

D'accord, donc si vous vous demandez les détails de game repo, vous pouvez revenir à la partie du tutoriel où nous l'avons effectivement construit.

Essentiellement, nous allons créer une lambda pour représenter le cas de succès, puis une autre lambda pour représenter un cas d'erreur ou d'exception, pour rendre cela un peu plus lisible.

Je vais simplement ajouter un commentaire ici.

D'accord, donc si vous vous demandez encore comment nous annulons effectivement le timer, c'est exactement comment nous le faisons, nous annulons l'objet job.

Maintenant, nous allons écrire cette autre fonction dans un instant.

Essentiellement, si c'est un nouveau record, alors nous voulons rendre l'interface utilisateur légèrement différente de ce qu'elle était si ce n'était pas un record.

Mais avant de faire cela, terminons le cas d'erreur.

Donc, afin de savoir si c'est un record, nous devons en fait passer la valeur dans le stats repo juste pour vérifier cela.

Donc, je vais être honnête, la gestion des erreurs dans cette application n'est pas la meilleure, ni la pire. Montrer l'erreur. Eh bien, pour l'instant, il suffit d'afficher un message toast expliquant qu'une erreur s'est produite.

D'accord, juste une petite correction.

Cela est en fait censé être le temps écoulé et non l'état du timer.

Ensuite, nous avons on new game clicked.

Vous remarquerez un thème récurrent ici, qui est qu'à tout moment nous voulons effectuer des opérations concurrentes.

Donc, chaque fois que nous travaillons avec le back-end, nous allons envelopper cela dans une co-routine de lancement.

Il y a beaucoup de façons différentes de travailler avec les co-routines.

C'est juste l'une des façons les plus simples et directes de le faire.

À mon avis.

D'accord, donc ce que nous faisons ici, c'est que nous demandons d'abord au view model si l'utilisateur a complété le jeu actuel, s'il ne l'a pas fait, nous voulons en fait stocker les progrès que l'utilisateur a réalisés dans son jeu actuel, lorsqu'il clique sur on new game clicked, car peut-être qu'il l'a fait par accident, ou il veut pouvoir revenir et terminer le jeu ou une raison de ce genre.

C'est bien, la fonction update with time.

Encore une fois, nous avons des cas de succès et d'erreur.

Espérons que cela est assez clair à ce stade.

Ensuite, nous allons implémenter cette fonction.

Ensuite, nous allons écrire la fonction cancel stuff.

Donc, essentiellement, la fonction cancel stuff annule chaque co-routine.

Ensuite, nous allons écrire on start.

J'ai oublié de mentionner plus tôt, la raison pour laquelle nous avions un soulignement dans l'une des fonctions pour is complete.

C'est juste une sorte de convention pour un argument ou un paramètre lambda qui n'est pas utilisé.

Dans ce cas, nous allons l'utiliser.

D'accord, donc évidemment, c'est là que nous démarrons le timer de co-routine, et nous ne voulons le faire que lorsque on start est appelé.

Maintenant, encore une fois, j'ai l'impression que j'aurais pu gérer cela un peu mieux, cela va à l'encontre de mes règles de considérer le flux standard de l'application comme une exception.

Mais essentiellement, ce que nous allons faire ici, c'est que dans le cas où nous demandons au stockage un jeu actuel, et qu'il ne récupère en fait rien, généralement, cette situation se produira lorsque l'utilisateur a exécuté l'application pour la première fois, et donc, il n'y aurait en fait aucune donnée stockée.

Donc, dans ce cas particulier, nous voudrions faire cela.

Nous pourrions également nous retrouver ici à cause d'une sorte d'exception légitime, mais dans ce cas particulier, je pense toujours que naviguer vers la fonctionnalité de nouveau jeu est toujours une bonne façon de gérer cela, bien que peut-être pas la meilleure.

Ensuite, nous avons on stop.

D'accord, donc onstop est en fait lié au cycle de vie de l'activité ou du fragment Android auquel il est lié.

Donc, lorsque cette fonction est appelée, cela signifie essentiellement que nous voulons sauvegarder les progrès actuels de l'utilisateur et ensuite tout arrêter.

Enfin, nous avons on tile focus.

Donc, ce serait lorsque l'utilisateur sélectionne une tuile Sudoku particulière.

Maintenant, cette fonction est incroyablement compliquée, alors préparez-vous.

D'accord, j'ai menti.

C'est en fait tout ce que nous devons faire.

Dans cette partie du tutoriel, nous allons créer l'interface utilisateur pour la fonctionnalité de jeu actif.

Avant de continuer, je vous suggère fortement de regarder ma vidéo intitulée Comment comprendre jetpack compose, un guide pour débutants sur les composables et la recomposition.

Nous allons écrire de nombreux composables et configurer la recomposition également.

Mais cette vidéo est faite pour les personnes qui commencent tout juste avec compose.

Elle explique ce qu'est un composable, ce qu'est la recomposition, et comment éviter de faire la recomposition de la mauvaise manière.

Et croyez-moi, il est assez facile de tout gâcher si vous n'êtes pas conscient de son fonctionnement.

Je vais lier cette vidéo dans le commentaire épinglé ci-dessous.

Cette vidéo est remplie d'une tonne d'informations, alors s'il vous plaît, consultez les horodatages dans la boîte de description ci-dessous.

Les sujets incluent les widgets de base, tels que le texte, le bouton de texte, l'image, l'icône, l'espaceur et le diviseur, les dispositions, telles que la boîte, la colonne, la ligne, la boîte avec contraintes et mon préféré, la disposition de contrainte.

Les animations de transition simples pour animer entre un écran de chargement, un jeu actif et un jeu complet.

Je vous montre également comment communiquer avec notre logique de présentation et notre view model en utilisant des types de fonction et des expressions lambda.

Avant d'écrire le code composé, cependant, je vous montre comment configurer une activité comme conteneur pour les composables.

Le processus pour le faire est presque identique pour les fragments si vous les préférez, je vous montre également comment écrire une fonction d'extension d'injection de dépendance très simple, qui cache les détails du backend du frontend.

Cliquez avec le bouton droit sur le package active game et allez dans nouvelle activité et choisissez une activité vide.

Et assurez-vous de décocher générer un fichier de disposition.

Et cette activité s'appellera active game activity.

Ce sera l'activité de lancement.

Maintenant, au cas où vous vous demandez pourquoi nous utilisons cet assistant au lieu de simplement créer un fichier de classe.

La raison est simplement qu'en utilisant l'assistant, il ajoutera une entrée dans le manifeste afin que nous n'ayons pas à le faire.

Juste pour résumer brièvement le but de cette activité ici est en tant que conteneur spécifique à une fonctionnalité.

Commençons par créer une référence à notre classe active game logic.

Ensuite, implémentons l'interface active game container.

Cliquez sur le rouge et appuyez sur alt enter.

Pour show error, nous allons utiliser la fonction d'extension que nous avons créée il y a longtemps dans ce tutoriel.

Allez-y et importez.

De plus, au cas où vous vous poseriez la question, il s'agit ici de la syntaxe d'expression unique, elle remplace essentiellement les accolades et l'instruction return par un simple signe égal.

Ensuite, implémentez on new game click.

Maintenant, évidemment, nous n'avons pas encore créé new game activity, donc cela apparaîtra en rouge jusqu'à ce que nous le fassions.

Nous devons également remplacer deux méthodes de cycle de vie supplémentaires.

Ici, nous dirons à la classe de logique que tout est prêt à partir, et ensuite nous remplacerons également on stop.

Et cela signalera évidemment à la classe de logique qu'il est temps d'annuler les choses et de tout arrêter.

Enfin, nous devons simplement ajouter quelques lignes à on create.

Tout d'abord, créez le view model.

Maintenant, c'est une partie très importante, ce que nous allons faire ensuite, c'est que nous allons essentiellement ancrer nos composables que nous allons créer dans la prochaine partie de ce tutoriel, à l'activité ici.

C'est aussi quelque chose que vous pouvez appeler à l'intérieur d'un fragment.

Allez-y et importez cela.

Naturellement, nous allons envelopper tout dans notre thème compose.

Maintenant, c'est une chose très importante à comprendre et un modèle très important.

Donc, lorsque nous créons active game screen, nous allons passer un type de fonction, qui servira de gestionnaire d'événements, ce qui est essentiellement ma façon de dire que c'est la manière dont nous allons transmettre les événements, les événements onClick et autres, qui se produisent dans le composable à notre classe de logique de présentation.

Donc, assurez-vous de prêter attention à ce que je dis ici, car c'est une partie vraiment importante, même si vous n'utilisez pas de présentateurs en bois ou autre chose.

Les types de fonction sont un excellent moyen de gérer les événements onClick, surtout si vous les combinez avec le modèle de stratégie, que nous avons discuté dans la section précédente.

D'accord, maintenant, si vous n'avez jamais vu de référence de fonction, je crois que c'est ce que l'on appelle, essentiellement ce que nous faisons ici, c'est que nous pointons vers la fonction on event de la classe de logique.

C'est vraiment une référence de fonction.

Donc, espérons que vous pouvez comprendre de quoi je parle ici.

Nous allons également passer le view model.

Enfin, nous devons en fait construire notre classe de logique.

Donc, ce que nous allons faire, c'est que nous allons écrire ce code dans une fonction d'extension, mais ce que nous pouvons faire en premier, c'est le lire ici.

Et c'est tout ce que nous devons faire dans notre activité.

Cliquez avec le bouton droit sur active game, allez dans nouveau package, et ce package s'appellera build logic.

Cliquez avec le bouton droit sur ce package et allez dans Nouveau fichier ou classe kotlin, ce sera un fichier.

Et il s'appellera build active game logic.

Si vous avez regardé ma chaîne ou mes streams en direct depuis un certain temps, vous savez que je parle beaucoup d'injection de dépendances et de localisateurs de services.

Et l'une des choses que je dis tout le temps, c'est que dans une petite application, vous n'avez pas vraiment besoin d'utiliser un conteneur DI comme hilt, dagger, ou autre, vous pouvez l'utiliser.

Mais ce que je conseille toujours aux débutants, c'est d'écrire le code que ces choses génèrent pour vous, vous-même d'abord, afin que vous compreniez ce que ces frameworks font pour vous.

Donc, c'est exactement ce que nous allons faire.

Nous allons écrire le genre de chose que ces frameworks génèrent pour vous.

Et dans une petite application, c'est en fait un code très simple à écrire.

Et, bien sûr, il va retourner active game logic.

D'accord, faisons une pause juste un instant ici.

Donc, au cas où vous vous demandez comment nous obtenons le chemin vers le répertoire de stockage que nous pouvons utiliser pour cette application, vous pouvez appeler context dot files dir dot path.

Enfin, notre dispatcher.

Et c'est tout ce que nous devons faire.

Cliquez avec le bouton droit sur la fonctionnalité active game, et créez un nouveau fichier kotlin appelé active game screen.

Tout d'abord, créons un enum.

Cet enum représente différents états que cette fonctionnalité de l'interface utilisateur peut posséder.

L'état réel est détenu dans le view model, mais nous verrons comment nous pouvons mettre à jour notre UI composable en le liant aux types de fonction du view model que nous avons créés dans la partie précédente de ce tutoriel.

Active game screen représente le composable racine.

Dans cette hiérarchie de composables, il a la responsabilité de configurer les éléments principaux de l'UI, ainsi que d'animer entre eux.

La référence de type de fonction event handler est la manière dont nous rappelons la logique de présentation.

Lorsque l'utilisateur interagit avec l'application, elle doit être transmise à tout composable qui a de telles interactions, nous passons également le view model, qui est la manière dont nous donnons les données à notre UI.

En termes très simples, chaque fois que nous avons un type de données ou d'état qui peut changer à l'exécution, nous voulons envelopper ces données dans un délégué remember.

Cela indique à la bibliothèque Compose sous le capot de surveiller les changements et de redessiner l'UI si un changement se produit.

Maintenant, mutable transition state est utilisé spécifiquement pour les animations ici, donc ne l'utilisez pas partout.

Nous verrons un exemple plus général de l'état rappelé plus tard.

Remember, le délégué prépare compose pour les mises à jour, mais nous avons également besoin d'un moyen de mettre à jour la valeur.

Nous faisons cela en liant une expression lambda à l'un des types de fonction que possède notre view model.

Lorsque l'une de ces fonctions est invoquée dans le view model, le programme saute automatiquement et exécute ce code dans notre composable.

C'est ce qui déclenche réellement la recomposition.

Nous avons un état de transition rappelé et un moyen de mettre à jour cet état à partir du view model.

Maintenant, nous devons configurer les animations de transition elles-mêmes.

C'est là que vous pouvez être aussi créatif que vous le souhaitez.

Dans cette application.

Chaque état de contenu a son propre composable associé.

Nous animons entre eux simplement en changeant la valeur alpha ou la transparence.

Maintenant, il était vraiment rouge il y a un instant, la façon dont je l'ai corrigé était d'importer manuellement le Compose runtime.

Donc, la spécification de transition indique à compose les détails de ce à quoi l'animation devrait ressembler.

Essentiellement, cela signifie que nous n'avons pas à écrire nos propres instructions mathématiques, ce qui est génial pour quelqu'un comme moi qui est nul en arithmétique.

Une option pour compose est d'utiliser le composable scaffold comme squelette pour votre UI.

Je préfère personnellement le faire moi-même, puisque ce n'est pas vraiment si difficile, et cela ne me cache rien.

Tout d'abord, nous avons notre app toolbar.

Allons-y et créons cette nouvelle icône de jeu.

Ces icônes proviennent de la bibliothèque de matériel Compose, je vous recommande fortement de l'utiliser.

C'est ainsi que nous déclenchons réellement un événement on click.

Comme expliqué dans une partie précédente du tutoriel, en créant notre icône de toolbar ici et en la passant dans le composable app toolbar, nous rendons le app toolbar réutilisable.

En dessous de la toolbar, nous avons le contenu principal de cet écran, qui peut avoir trois états différents.

Chaque fois qu'une recomposition se produit, cette instruction sera exécutée à nouveau.

La valeur alpha de l'acte changera lorsque l'animation de transition se produira, faisant ainsi disparaître l'état de contenu précédent et apparaître le nouveau.

Évidemment, nous allons les créer dans un instant.

Et c'est tout pour notre composable racine, la partie la plus complexe de notre UI provient d'un jeu Sudoku actif.

Un puzzle de neuf par neuf a 81 composables de texte différents, ce qui est un grand nombre de widgets.

La façon dont j'ai écrit ce composable était de penser à chaque partie du jeu Sudoku comme un élément ou une couche particulière.

Assurez-vous d'éviter d'écrire des composables Dieu en utilisant des fonctions d'assistance qui décomposent l'UI en les plus petites parties raisonnables.

La boîte avec contraintes est une sorte d'enveloppe composable qui nous donne des informations sur la hauteur, la largeur et d'autres mesures, nous pouvons utiliser ces informations dans son expression lambda.

Nous devons connaître la largeur de l'écran afin de déterminer la largeur et la hauteur du tableau Sudoku.

Ici, nous avons demandé la largeur maximale de cette disposition de contrainte.

Ici, nous demandons la largeur maximale de ce composable de disposition.

Mais nous avons besoin que cette valeur soit en pixels indépendants de la densité, et elle doit également être relative à la densité de l'écran actuel.

C'est là que la fonction d'extension two dp intervient.

Et elle utilise la densité locale pour déterminer cette valeur.

La marge du tableau doit également changer en fonction de la densité de l'écran.

Je suis arrivé à ces valeurs simplement en testant l'application sur diverses densités en utilisant l'émulateur.

Ensuite, nous allons écrire une disposition de contrainte, qui est une façon totalement géniale de gérer les dispositions dynamiques.

Maintenant, afin de contraindre les composables les uns aux autres, nous avons besoin d'un moyen pour qu'ils se référencent mutuellement.

Cela équivaut à définir des ID pour les vues XML.

Tout d'abord, nous créons ces références et vous verrez comment les lier plus tard.

Créons un conteneur de disposition pour le tableau de puzzle.

D'accord, donc c'est vraiment important, voyez comment nous passons cette référence dans le paramètre constrain as là.

C'est ainsi que nous associons un composable particulier à une référence particulière.

Ce composable de boîte sera associé au nom board.

Ensuite, nous allons créer le tableau Sudoku lui-même.

Encore une fois, la frontière est comme la taille du puzzle.

Donc, c'est soit un puzzle de quatre par quatre ou un puzzle de neuf par neuf.

Donc, la frontière serait soit quatre soit neuf.

Cela est censé dire taille.

Donc, le décalage ici est utilisé pour répartir uniformément l'espace réel de l'écran pour chaque tuile et ligne de grille Sudoku.

Voici une façon de créer un état mutable qui n'est pas associé à une sorte d'animation de transition.

Donc, c'est l'approche à usage plus général.

Donc, le premier argument ici view model dot board state peut être considéré comme la valeur initiale, la politique never equal garantit que même les changements mineurs dans l'état comme has focus déclenchent réellement une recomposition.

Encore une fois, c'est ainsi que nous mettons à jour la valeur une fois que le view model est mis à jour.

Comme vous pouvez le voir, ici, encore une fois, je fais un usage intensif de nombreuses fonctions d'assistance pour décomposer les choses.

Ici, nous rendons les champs de texte qui représentent les tuiles dans le puzzle, ils peuvent être en lecture seule ou mutables, ce qui signifie que nous devons les rendre légèrement différents.

Donc, ici, nous disons que si l'utilisateur définit une tuile particulière à une valeur de zéro, nous voulons en fait la rendre comme une tuile vide.

L'idée principale ici est que nous utilisons les valeurs x et y de chaque tuile individuelle ainsi que le décalage afin de positionner uniformément chaque tuile. Donc, lorsque l'utilisateur sélectionne une tuile, elle deviendra focalisée et nous voulons rendre cette tuile évidemment un peu différente d'une tuile non focalisée.

Maintenant, nous allons rendre les carrés en lecture seule.

Ensuite, nous allons créer la grille du tableau.

Donc, Sq RT est une extension, qui est en fait définie dans la logique de calcul.

En rétrospective, j'aurais probablement dû définir cela dans le package commun, mais c'est assez évident ce qu'il fait.

Donc, cette fonction ici, nous allons dessiner les lignes de grille qui séparent les puzzles Sudoku.

Pour rendre plus évident pour l'utilisateur quelles sous-grilles sont lesquelles, nous dessinons différentes bordures pour séparer les sous-grilles de quatre par quatre ou de neuf par neuf.

C'est pourquoi nous utilisons modulo ici.

Donc, cela dessine à la fois les lignes verticales et horizontales.

D'accord, donc nous revenons dans le composable game content pour le terminer.

En dessous de notre tableau Sudoku, nous avons différentes icônes pour indiquer la difficulté du puzzle.

Ensuite, nous avons besoin d'un conteneur de disposition pour le compteur de temps, c'est super, le composable timer texts.

Maintenant, la valeur par défaut, c'est juste vide.

D'accord, nous sommes de retour dans le composable game content.

La dernière chose que nous devons faire est simplement ajouter un conteneur de disposition pour les boutons d'entrée.

Maintenant, nous allons coder en dur certaines valeurs ici et ce n'est pas une bonne pratique.

Mais la raison est que l'équipe Compose a déprécié flow row, ce qui m'a toujours contrarié, et cela fonctionnait parfaitement pour cette situation, et j'ai été trop paresseux pour implémenter flow moi-même.

Hé, au moins je suis honnête.

Au cas où vous vous poseriez la question, 0.4 et cinq dot dot neuf vont émettre une plage inclusive de ces valeurs.

Créons ce composable, un espaceur est assez explicite, il prend simplement un peu de place dans la disposition.

Ensuite, nous avons les boutons eux-mêmes.

Ce wrapper de bouton de texte nous permet de styliser un bouton bien conçu au lieu de simplement ajouter un clic sur un composable de texte.

D'accord, c'est tout pour le contenu du jeu.

Maintenant, nous devons faire l'écran de contenu de jeu terminé, qui est évidemment lorsque l'utilisateur termine un jeu.

Donc, c'est essentiellement deux images empilées l'une sur l'autre, mais nous ne allons en rendre qu'une si c'est en fait un nouveau record que l'utilisateur a établi.

Puisque nous ne créons pas réellement les icônes d'événements emoji, nous pouvons changer leur couleur en utilisant cette chose de filtre de couleur.

Assez pratique.

Ensuite, nous avons deux composables de texte.

Et c'est tout.

Félicitations.