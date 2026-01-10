---
title: Apprenez à créer un système de design dans Figma
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-06-28T13:50:35.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-create-a-design-system-in-figma
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/designsystem.png
tags: []
seo_title: null
seo_desc: 'Un système de design est un ensemble de normes, de composants réutilisables et de motifs utilisés pour créer une cohérence visuelle à travers différents projets et pages. Figma est un éditeur graphique vectoriel et un outil de prototypage.

  Nous venons de publier un cours sur la chaîne freeCodeCamp....'
---

Un système de design est un ensemble de normes, de composants réutilisables et de motifs utilisés pour créer une cohérence visuelle à travers différents projets et pages. Figma est un éditeur graphique vectoriel et un outil de prototypage.

Nous venons de publier un cours sur la chaîne freeCodeCamp.org qui vous apprendra à construire un système de design dans Figma.

Tim Sullivan a créé ce cours. Tim est un ancien designer chez Airbnb et c'est un excellent professeur.

Si vous voulez que votre projet ait une allure professionnelle, il est important de créer un système de design afin d'avoir un style cohérent.

Voici les sujets abordés dans ce cours :

*   [Introduction](#introduction)
*   [Création d'un système de couleurs](#creation-dun-systeme-de-couleurs)
*   [Construction d'un système typographique dans Figma](#construction-dun-systeme-typographique-dans-figma)
*   [Élévation](#elevation)
*   [Icônes produit et système](#icones-produit-et-systeme)
*   [Lisibilité du texte](#lisibilite-du-texte)
*   [États](#etats)
*   [Sélection (Interaction)](#selection-interaction)
*   [Comprendre la mise en page](#comprendre-la-mise-en-page)
*   [Densité de pixels](#densite-de-pixels)
*   [Méthodes d'espacement](#methodes-despacement)
*   [Mise en page en grille responsive](#mise-en-page-en-grille-responsive)
*   [App Bar - Inférieure](#app-bar-inferieure)
*   [App Bar - Supérieure](#app-bar-superieure)
*   [Backdrop (Toile de fond)](#backdrop-toile-de-fond)
*   [Bannières](#bannieres)
*   [Navigation inférieure](#navigation-inferieure)
*   [Boutons - Bouton d'action flottant](#boutons-bouton-daction-flottant)
*   [Boutons](#boutons)
*   [Cartes](#cartes)
*   [Chips (Puces)](#chips-puces)
*   [Boîtes de dialogue](#boites-de-dialogue)
*   [Sélecteurs de date](#selecteurs-de-date)
*   [Séparateurs](#separateurs)

Regardez ci-dessous ou sur la [chaîne YouTube de freeCodeCamp.org](https://www.youtube.com/watch?v=RYDiDpW2VkM) (durée de 8 heures).

%[https://www.youtube.com/watch?v=RYDiDpW2VkM]

## Transcription vidéo

(Généré automatiquement)

Un système de design est un ensemble de normes, de composants réutilisables et de motifs utilisés pour créer une cohérence visuelle à travers les pages et les projets.

Figma est un éditeur graphique vectoriel et un outil de prototypage. Dans ce cours, Tim Sullivan vous apprendra à créer un système de design en utilisant Figma.

Salut tout le monde, ici Tutorial Tim.

Et aujourd'hui, je vais vous donner un bref aperçu de ce que nous allons couvrir dans la série à venir : je vais créer un système de design.

Et ce système de design sera le système Material Design dans Figma.

Et je ferai de mon mieux pour traduire ce qui est actuellement affiché sur ce site web en un système de design dans Figma.

Donc, nous passerons en revue, premièrement, les fondations.

Et les fondations impliquent des choses telles que la mise en page (layout), et ce qu'est la mise en page, comme une réponse à la création de ces mises en page en grille responsive de styles et Figma.

Comprendre comment les construire en utilisant des méthodes d'espacement appropriées, et comment les composants seront disposés dessus.

Donc nous passerons cela en revue.

Et nous verrons également comment appliquer un système de couleurs en utilisant le système de couleurs de Material Design et en l'implémentant dans Figma, ainsi que les styles de couleurs.

Et aussi, nous allons aborder la typographie et construire le système typographique spécifié ici dans Material Design.

Mais dans Figma, comment faire cela et traduire cela dans Figma.

Aussi, nous aborderons l'iconographie.

Et avec l'iconographie dans Figma, nous allons essentiellement appliquer la structure pour la lettre spécifiée dans les icônes produit.

J'aurai cet ensemble d'icônes déjà dans Figma lorsque nous passerons en revue, mais je vais vous montrer comment l'organiser et y accéder via le menu déroulant d'instance.

Ainsi, vous pourrez basculer entre les composants communs et d'autres icônes de composants, qui sont également des composants.

Et aussi, nous allons aborder une partie de l'interaction, qui concerne les états (states) pour certains composants.

Donc, dans cette partie de la construction du système de design, nous passerons en revue les fondations.

Et ensuite, à partir de là, nous passerons aux composants.

Et nous construirons littéralement chaque composant de cette page à partir de zéro et en utilisant les fondations que nous avons créées dans Figma.

Donc, nous commencerons par les barres d'application (App bars), barres inférieures, barres supérieures, jusqu'au tout dernier composant qui sont les infobulles (tooltips).

Et nous verrons comment, disons, les construire via leur anatomie, n'est-ce pas.

Donc nous avons toutes ces informations, comment les utiliser, le placement et le comportement.

Et essentiellement, je vais vous apprendre à voir ce fichier et à le construire dans Figma, à partir de zéro et à appliquer les contraintes appropriées.

Donc c'est responsive, juste au cas où les designers auraient besoin de le modifier.

Et ce sera essentiellement le système de design que nous construirons dans Figma, qui est le Material Design.

Et c'est le bref aperçu.

Je vais commencer par un système de couleurs. Ouais, donc ça va un peu commencer par référencer le site web pour vous donner, les gars, une compréhension de ce que nous allons construire dans Figma.

Et ce que nous allons faire dans Figma, c'est essentiellement traduire, je vais vous donner un bref aperçu maintenant de ce que nous allons faire tout au long de la vidéo, pour vous donner une compréhension générale.

Donc nous allons commencer par le système de couleurs, implémenter les couleurs, puis ajouter cela dans Figma en tant que bibliothèque, afin que vous puissiez les voir ici.

Pour ceux d'entre vous qui ont, pour ceux d'entre vous qui sont capables d'utiliser les bibliothèques, vous pouvez voir cette palette de couleurs ici.

Et tous les styles qui ont été créés dans cette bibliothèque.

Donc avec mon fichier de couleurs du système Material Design et renommer cela très vite Material Design.

Et nous avons Material Design ici.

Et maintenant, si je vais ici, nous allons pouvoir l'ajouter à cette bibliothèque que nous publierons éventuellement, avec toutes ces couleurs, mais ce fichier actuel est déjà publié.

Mais ce que je vais faire, c'est supprimer tout ça très vite.

D'accord, donc nous avons ces couleurs, nous avons des styles de couleurs, mais nous ne les avons pas ajoutés dans la bibliothèque, je vais vous montrer comment faire cela.

Mais je vais vous montrer comment faire cela en développant, en créant ce système de couleurs, nous allons utiliser le thème de couleur de base de Material pour montrer comment construire ces couleurs en tant que styles dans Figma pour que toute votre équipe puisse les utiliser.

Si vous travaillez pour une organisation, par exemple, ou juste une équipe, c'est une manière de travailler beaucoup plus efficace.

Donc essentiellement, ce que je vais faire est de faire une capture d'écran de ceci pour avoir toutes ces valeurs, pour ne pas avoir à faire des allers-retours entre les navigateurs.

Et une fois que c'est fait, je vais juste tout supprimer ici.

Pas besoin de ça.

Pas besoin de ça.

Et je vais commencer, c'est comme un fichier tout neuf pour que vous puissiez suivre.

Suivez-moi depuis le début.

J'ai déjà une page et je vais en fait l'étiqueter primitives parce que ceci, ce composant est un composant primitif.

Donc la façon dont nous allons structurer tous ces composants, en termes de complexité, va de sa forme la plus simple, étiquetée comme primitive, jusqu'aux composants, puis aux motifs (patterns), qui sont composés de plusieurs composants.

Et nous entrerons plus en détail là-dessus plus tard.

Mais commençons simplement avec les couleurs.

Donc maintenant, j'ai la capture d'écran collée ici.

Et ce que je vais faire est essentiellement de traduire toutes ces couleurs en styles.

Donc sans plus tarder, je vais juste créer quelques rectangles.

Et en fait, je vais appuyer sur Ctrl+C, pour copier cette valeur ici.

Remarquez que lorsque j'utilise Ctrl+C, la valeur hexadécimale n'est pas ce qui est indiqué dans la capture d'écran que j'ai sélectionnée pour copier la valeur et l'appliquer au rectangle.

Donc je devrai saisir manuellement cette valeur qui est indiquée là.

Et je vais juste continuer à faire cela jusqu'à ce que j'aie complété toutes les valeurs de couleur.

Et je vous verrai quand ce sera fait.

D'accord, j'ai maintenant terminé de créer tous ces blocs de couleur pour vous dans Figma, juste pour vous montrer visuellement et appliquer les bonnes lignes de couleur, parce qu'en fait, ce que je voulais faire à l'origine était d'utiliser un sélecteur de contrôle et d'appliquer ces valeurs, mais cela ne reproduit pas exactement les valeurs hexadécimales exactes spécifiées dans l'image, à cause de la capture d'écran que j'ai prise.

Et de toute façon, pour faire court, faisons de ceux-ci des styles de couleur maintenant.

Donc maintenant, nous allons ajouter ceci dans notre système de couleurs.

Actuellement, nous n'avons rien dans notre système de couleurs.

Donc essentiellement, ce que, ce que vous pouvez faire est, nous avons déjà la convention de nommage définie pour nos styles de couleur.

Donc nous pouvons aller à notre couleur et sélectionner le style, ajouter un nouveau style, et il saisira essentiellement la valeur hexadécimale du rectangle que nous avons sélectionné, et ensuite nous pouvons l'étiqueter comme primaire (primary).

Et quand vous cliquez sur Créer un style, cela créera ce style.

Et quand vous passez la souris dessus, une infobulle apparaîtra en dessous.

Et elle indiquera le nom du style que vous essayez de chercher.

Et aussi, si vous voulez ajouter un étiquetage sur, disons, si nous créons une variante primaire (primary variant), oups, et nous sélectionnons cette petite, ces quatre petites icônes, et ensuite cliquons sur Ajouter un style.

Et ensuite nous faisons primary / variant, cela ajoutera en fait un étiquetage.

Donc nous irons et cela, vous commencerez à voir qu'avec l'utilisation du slash dans le nom de votre style de couleur, ce slash crée en fait cette étiquette pour vous permettre d'analyser très facilement les informations dans vos styles de couleur, ce qui est très bon pour, comme la facilité d'utilisation, par opposition à juste générer toutes ces couleurs.

Et ensuite les avoir juste côte à côte et passer la souris, pour accéder au nom de la couleur que vous cherchez exactement.

Et au moins les diviser en sections pour vous rapprocher d'un pas de la couleur dont vous avez besoin.

Et je vais dissocier cela, parce que ce n'est pas exactement comme ça que je veux l'aborder.

Je vais en fait aller ici, et si vous, si vous remarquez aussi, et vos styles de couleur, si vous ne les avez pas publiés, ils seront sous styles locaux.

Et ensuite vous pouvez accéder à votre bibliothèque en allant à, si vous appuyez sur Command+Shift+point d'interrogation, vous pouvez taper library, et ensuite cela vous basculera vers Team library (Bibliothèque d'équipe).

Il y a aussi une touche de raccourci, Option+3, qui vous y amènera et aussi une touche de raccourci Option+Command+O pour accéder aux bibliothèques.

Et vous remarquerez que j'ai 19 changements non publiés à publier.

Et je peux les publier, mais nous publierons cela une fois que nous aurons terminé ceci.

Et je vais continuer à créer le reste des couleurs au fur et à mesure et les étiqueter en conséquence.

Secondary (Secondaire), créer le style.

Et ensuite je vais créer ceci comme une variante primaire.

Créer le style.

Et une chose que vous pouvez faire aussi dans les styles de couleur est que vous pouvez en fait glisser-déposer pour réorganiser les styles.

Donc je vais en fait faire un clic droit sur celui-ci et supprimer le style.

Et une chose que vous pouvez faire avec les styles de couleur aussi est que vous pouvez aller dans modifier et ajouter une description et dire que cette couleur secondaire est utilisée pour le composant x, x signifiant le nom du composant ou le ou comme aussi sur les surfaces pour le composant x comme exemple.

Et ensuite une fois que vous avez, une fois que vous avez terminé cela, vous pouvez appuyer sur retour et cela enregistrera vos changements.

Et ensuite vous pouvez retourner dans les composants comme ce style et vous remarquerez que ces changements sont maintenant là.

Ce qui est une autre chose agréable à propos des couleurs pour avoir une compréhension des usages derrière elles lors de leur utilisation à travers, disons que vous concevez pour un produit, par exemple. Je vais mettre cette vidéo en pause et générer le reste de ces couleurs.

Et je vous verrai dans un instant.

Donc maintenant j'ai tout terminé.

Vous pouvez voir que mes styles de couleur ont des styles locaux.

Donc j'ai la base du thème Material dans ses couleurs, d'accord, et je les ai tous étiquetés ici.

D'après la capture d'écran, j'ai capturé depuis le site web.

Et j'ai essentiellement traduit cela dans Figma.

Et ensuite j'ai appliqué ces styles tout du long, du primaire à la surface d'erreur (on error), beaucoup d'entre eux sont très similaires.

Mais une chose que je n'aime pas dans cette approche que je vais vous montrer.

Et la prochaine approche d'application des styles de couleur avec une convention de nommage cohérente qui étiquette clairement tout, quand vous essayez d'y accéder via le menu déroulant, c'est que ce n'est pas très clair ce que j'essaie de changer comme couleur, n'est-ce pas, je dois juste passer la souris pour trouver les valeurs.

Et une description apparaîtra pour les composants qui ont une description là, ce qui est la raison pour laquelle cette infobulle était plutôt large pour ce style de couleur dans cette instance, juste pour fournir un peu de contexte derrière cela.

Et de toute façon, ce n'est tout simplement pas assez clair pour moi pour ajouter des styles de couleur.

Donc ce que je vais faire est dans Material Design 2014 établi juste ici en 2014, leur palette de couleurs, et elle est juste composée de couleurs pour travailler ensemble harmonieusement.

Et essentiellement, c'est là que je vais utiliser comme une convention de nommage cohérente et une structure basée sur les, les couleurs données ici avec, avec ce que j'aime appeler les variables et leurs valeurs hexadécimales, que je vais ensuite appliquer dans Figma.

Et je vais vous montrer comment faire cela avec les trois premières.

Donc je vais retourner dans Figma.

Et je vais vous montrer avant, je vais vous montrer, je vais enlever tout ça, parce que je ne veux plus de ça, je vais en fait juste le laisser.

Et ainsi vous pouvez voir la différence entre comment naviguer dans les couleurs avec une convention de nommage cohérente, en utilisant le slash lors du nommage de ces couleurs et les styles lors de leur création de styles.

Et de toute façon, je vais aller ici, attraper mon rectangle.

Et je vais littéralement juste copier ce bloc ici sur l'arrière-plan étiqueter Red (Rouge), red, red 50 pour imiter un peu la mise en page que nous avons ici.

Et ensuite je vais appuyer sur Command+D pour dupliquer et ensuite Option+D pour aligner cela à droite, et ensuite taper cette valeur hexadécimale.

Et tout ce processus que vous voyez de ma part est, je vais le faire une fois et ensuite je vais mettre la vidéo en pause et le faire pour le reste.

Et ensuite je vous montrerai comment étiqueter correctement tout en tant que style de couleur dans Figma, et, et ensuite je reviendrai.

Très bien, donc j'ai maintenant reproduit cette capture d'écran que j'ai prise du site web avec la palette de couleurs qui contient une portion de la palette de couleurs que Material Design a à offrir ou à utiliser.

Et j'ai juste fait le rouge, le rose et le violet.

Donc maintenant ce que je vais faire est de commencer à vous montrer la différence et à quel point cela peut être utile en appliquant cette convention de nommage cohérente à tous les styles de couleur que nous sommes sur le point de créer pour le rouge, le rose et le violet, que vous pouvez appliquer à votre système.

Donc je vais commencer avec le rouge, nous avons cette valeur red 50, donc nous avons red 50, nous avons déjà la valeur hexadécimale, je vais cliquer sur ajouter un style de couleur, je vais l'étiqueter red parce que nous allons avoir une section de rouges, allant de valeurs de 1 à 900, du clair au foncé, et ensuite aussi un 100 à un 700.

Pas exactement sûr de ce que ces valeurs représentent.

Mais euh, vous voyez où nous allons avec ça.

Et je vais faire red 100, et ensuite spécifier la valeur hexadécimale aussi.

Et le style de couleur, ce qui est toujours utile, donc vous n'avez pas à aller manuellement appliquer le style et ensuite le dissocier pour voir la valeur hexadécimale, ce que je trouve assez ennuyeux.

Donc nous avons ce format, je vais cliquer sur Créer un style, appuyer sur Entrée.

Maintenant nous avons red 1.

Donc au survol, nous verrons red 100 et ensuite la valeur hexadécimale.

Et ensuite si vous cliquez ailleurs, vous voyez aussi la façon dont nous l'avons nommé est red / 100 - la valeur hexadécimale, ce qui est agréable et facile à analyser.

Et encore une fois, c'est à vous et votre équipe de décider comment vous étiquetez cela en termes de faire cela pour une organisation pour que les équipes l'utilisent.

Maintenant je vais aller et créer le reste de ces pour, pour le rouge.

C'est le même processus.

Donc nous avons, qu'est-ce que nous avons, nous avons créé red 100 qui était en fait supposé être étiqueté red 50 en fait j'ai écrit la mauvaise valeur hexadécimale aussi.

Donc je vais juste éditer ça.

Et c'est red 50 prêt à l'emploi appuyer sur Entrée tab, revenir en arrière.

Maintenant nous voyons que c'est affiné et reflète la valeur réelle.

Ok je vais faire quelques autres, pour que vous ayez l'idée de comment nommer vos styles de couleur.

Maintenant, je vais mettre en pause et finir les rouges et ensuite faire quelques roses et ensuite faire quelques violets pour voir à quel point l'utilisation du slash dans vos styles de couleur peut être efficace pour analyser l'information en essayant d'accéder aux couleurs à appliquer à vos composants à l'avenir, quand nous continuerons à implémenter plus de ce système à mesure qu'il deviendra plus dense.

Donc nous avons red 100 ici, je vais ajouter un style de couleur.

Red 100, prêt à l'emploi créer des styles de couleur.

Et nous en avons deux qui tombent sous la catégorie rouge, parce que nous utilisons red espace slash en gardant la convention de nommage cohérente.

Donc je vais juste copier cette valeur hexadécimale, Command+clic sur mon rectangle avec la couleur que je veux être un style.

Et ensuite je vais coller red 100.

Mais changer cela en 200 et ensuite réappliquer la valeur hexadécimale pour red 200 et créer ce style.

Donc maintenant je vais passer à la création d'une autre catégorie qui est le rose (pink).

Nous avons, je vais copier ceci encore, Command+clic, ajouter un style de couleur.

Et je vais y aller avec pink espace slash espace 50 et ensuite tiret et ensuite la valeur hexadécimale.

Créer ce style.

Et vous remarquerez dans les styles de couleur maintenant, nous avons notre nouvelle notre propre section rose pour refléter ce que nous aimerions imiter visuellement, mais dans nos styles de couleur, qui seront accessibles à tout le monde une fois que vous publierez ceci, parce qu'actuellement ce sont des styles locaux.

Comme vous pouvez le voir, quand vous cliquez quelque part au hasard sur le canevas, le canevas vide, vous verrez les styles de couleur ici.

Mais ils sont assis là seulement en local mais nous les pousserons une fois que nous aurons fini de faire ceci.

Et je vais faire le violet (purple) maintenant, parce que je suis assez sûr qu'à ce moment-là vous savez déjà comment faire ceci.

Comme je l'ai fait plusieurs fois, je vais copier cette valeur hexadécimale, sélectionner l'arrière-plan, ajouter le style de couleur, et je vais aller purple espace slash ajouter la valeur hexadécimale là et ensuite taper 50.

Fait ça.

Ok, Entrée.

Maintenant nous avons nos sections de rouge, rose et violet.

Les autres sections que nous n'avons pas implémentées depuis le site web Material Design, ce que je ferai de mon côté sont, sont les suivantes.

Comme vous pouvez le voir, j'ai défilé à travers beaucoup d'entre elles, cela prendra beaucoup de temps, mais c'est le même processus exact.

Mais je vais mettre cette vidéo en pause et compléter cela et vous montrer et ensuite nous le publierons une fois que j'aurai fini.

Et ce sera la fin de la vidéo à tout de suite.

Très bien, très bien.

Très bien, j'ai fini de créer le reste des styles de couleur en utilisant la méthode que j'ai spécifiée pour mettre cette vidéo en pause.

Et vous pouvez voir à quel point c'est dense, les styles sont devenus.

Donc chacun de ceux-ci est maintenant un style de couleur organisé ici du rouge, rose et violet.

Et il y en a plein d'autres à venir, je les aurai tous créés pour que vous puissiez les référencer aussi, dans ce, par là je veux dire toutes celles-ci, qui sont des captures d'écran que nous convertirons dans ce fichier Figma.

Prendre un peu de temps, mais euh, ce n'est pas un problème.

Donc maintenant, l'étape finale est de publier ceci.

Donc qu'est-ce que nous quoi ? Comment faisons-nous cela ? Eh bien, il y a quelques façons que je vais vous montrer, nous pouvons sélectionner assets (actifs), nous pouvons cliquer sur cette icône de bibliothèque et ce petit, cette petite icône bleue juste là dans le coin supérieur droit indique qu'il y a des publications à faire des changements, des publications à faire ou quoi que ce soit, vous pouvez le sélectionner et vous pouvez voir que vous pouvez publier 69 changements, les 69 changements étant tous les styles de couleur que nous avons appliqués à cette bibliothèque.

Une chose que je veux vous montrer est la différenciation entre la façon dont nous avons étiqueté ces couleurs au début et ensuite la façon dont nous avons étiqueté ces trois sections d'une manière beaucoup plus organisée et claire et concise.

Donc si nous allons ici, créons un rectangle et appliquons un style de couleur à celui-ci.

Nous cliquons juste sur cette petite icône ici et vous verrez que nous avons ces couleurs n'est-ce pas La seule façon dont vous pouvez vraiment dire ce qu'elles sont étiquetées est si nous passons la souris dessus, attendre de voir cette infobulle apparaître aussi.

Et ce que nous avons fait avec les couleurs c'est que nous avons utilisé le slash pour indiquer ce qu'était l'étiquette, à gauche du slash étant le Rouge, et ensuite la valeur étant appliquée au style, qui est rouge 50.

Et ensuite aussi au survol, pouvoir voir la valeur hexadécimale aussi.

Et nous avons fait cela et divisé rouge, rose et violet d'une manière beaucoup plus claire et concise pour que l'utilisateur puisse naviguer et utiliser.

Et encore une fois, c'est encore un peu gênant à cause de la densité de cette palette de couleurs.

Mais c'est la meilleure solution que je pense que Figma a créée pour cela et moi-même.

S'il y a d'autres meilleures façons de faire cela, s'il vous plaît laissez-moi savoir dans la section des commentaires ci-dessous.

J'espère que vous avez trouvé cette vidéo extrêmement utile.

Merci pour votre temps, s'il vous plaît laissez un j'aime, un commentaire, et abonnez-vous et suivez-moi sur GitHub.

Sinon, je vous retrouverai dans la prochaine.

Salut tout le monde, j'ai presque oublié, nous devons encore publier la bibliothèque.

Donc je vous ai montré plusieurs façons de comment la publier et utiliser Aller à Voir basculer vers la bibliothèque d'équipe ou vous pouvez sélectionner cette icône dans le panneau des actifs.

Et une autre façon est mes favoris.

Mon raccourci clavier est Option+Command+zéro.

Et ensuite vous pouvez sélectionner Publier les changements.

Et ensuite vous pouvez voir chaque style qui a été soit modifié.

Donc dans ce cas, il y en a un tas de supprimés, vous savez, des couleurs qui n'étaient pas très explicites.

Et ensuite les couleurs que nous avons ajoutées, bien sûr, et je vais appuyer sur et ensuite vous pouvez aussi ajouter une description quant à ce que vous avez ajouté.

Donc je vais juste être c'est comme un sorte de message comme un message de commit git d'une certaine manière, qui s'affichera dans l'historique de contrôle de version, une fois que vous publiez ceci.

Donc j'ajoute des couleurs, ajout d'une portion de couleur dans le système de couleurs du design material à la bibliothèque.

Et ensuite vous avez un message, expliquant un peu ce que vous avez fait, et ensuite publier.

Et ensuite cela ajoutera ceci à votre bibliothèque, une petite barre de notification indiquant le processus mis à jour avec succès.

Et ensuite vous pouvez voir vos actifs.

Et la chose agréable à ce sujet est que vous pouvez voir maintenant si vous allez à Material Design, vous pouvez voir toutes vos couleurs ici.

Et au survol, vous pouvez tout voir.

Ce n'est pas aussi bien disposé que le panneau des couleurs ici.

Mais ouais, c'est comme ça que vous publiez les couleurs dans votre bibliothèque.

C'est l'étape finale.

Aujourd'hui, je vais vous montrer comment créer un système typographique dans Figma spécifiquement le système typographique de Material Design, le lien sera dans la description pour référencer le système typographique que Material a créé.

Et essentiellement je vais juste vous donner une idée générale de comment vraiment développer un système typographique qui est utilisé pour votre contenu, spécifiquement vos composants et les motifs que nous créerons ici dans Figma.

Je recommande également de jouer avec ce générateur d'échelle typographique (type scale generator), ils ont ce petit élément interactif agréable sur la page web qui vous permet de voir vraiment l'échelle typographique et différentes polices spécifiquement peut-être plus que probablement une famille de polices que vous utilisez, vous pourriez voir à quoi cela ressemble à l'échelle.

Et si c'est une excellente ressource, je me suis dit que je la partagerais.

Et encore une fois, je recommande de parcourir tout cela.

Donc essentiellement, nous allons passer en revue la création de ceci à partir de zéro et les développer en styles de texte dans Figma qui sont facilement raisonnables pour casser le système de design et celui que nous construirons.

Alors commençons.

Donc j'ai Figma ouvert ici, et vous pouvez aussi accéder à ce fichier d'exercice si vous ne voulez pas le faire et voulez juste saisir les valeurs, j'aurai ce fichier Figma, un lien dans la description.

Donc nous avons nos exemples des propriétés résumées ici pour tous nos en-têtes ou sous-titres, corps et contenu, tels que bouton, légende et surlignement (overline), et nous allons essentiellement appliquer toutes ces propriétés à notre style de texte.

Donc sans plus tarder, commençons.

D'accord, donc maintenant que nous avons ceci, je vais ouvrir mon outil texte ici, et je vais juste sélectionner taper h1.

Je vais régler ceci sur largeur automatique parce que je n'aime pas tout espace hors ligne inutile autre que ce qui est spécifié pour le type.

Et je vais juste régler cette taille à 96, ce qu'elle est déjà, la hauteur de ligne est réglée sur auto, mais l'espacement des lettres nous allons le modifier à -1.5 comme spécifié.

Quand je m'assure de sélectionner cela ici, sélectionner mon type, et ensuite taper -1.5.

Appuyer sur Entrée cela resserre ici, le crénage et ou notre espacement des lettres meilleur mot pour cela, comme indiqué ici.

Mais de toute façon, je vais continuer à construire ces styles de type ici.

Je vais taper h2, sélectionner ma typographie, m'assurer que j'ai le bon espacement des lettres pour ne pas oublier et régler cela à -0.5.

Appuyer sur Entrée Et, encore une fois, si vous êtes confus avec quoi que ce soit et voulez comprendre les propriétés davantage, vous pouvez cliquer sur cette icône ici avec votre texte sélectionné, l'icône plus, et voir toutes les propriétés que cette police a à offrir.

Et une chose importante à noter c'est que si vous utilisez une police différente, mais en créant ce système typographique, il y a des fonctionnalités et des polices spécifiques qui sont offertes et ne sont pas offertes.

Donc si vous voyez certaines fonctionnalités ici, qui ne sont pas offertes dans une police séparée que vous utilisez dans le contexte de cette vidéo, c'est probablement parce qu'elle n'offre pas la fonctionnalité.

Donc notez juste cela.

Je recommande aussi de lire un peu tout cela c'est une très bonne information.

Mais c'est pour une autre vidéo, si vous souhaitez que je la fasse, laissez un commentaire dans la section des commentaires ci-dessous.

Et de toute façon, nous avons notre espacement des lettres spécifié, nous devons changer le dimensionnement ici.

Et la graisse est bonne.

Et donc la hauteur de ligne, et vous pouvez commencer à voir un peu ce processus, très simple.

Et vous répétez cela, en avançant.

Les seuls détails complexes je dirais, avant que je ne file à travers cela est la propriété du bouton.

Donc si je vais de l'avant et tape tout en minuscules, je peux en fait appliquer la casse de phrase tout en majuscules dans les propriétés de texte, ce qui est fantastique.

Je vais faire cela en sélectionnant la propriété majuscule.

Et il y a d'autres propriétés telles que minuscules, casse de titre, petites capitales, et pour petites capitales.

Et je veux juste noter cela, parce que je pense que c'est très important pour ces textiles, pour vraiment les optimiser.

Donc nous allons aller à l'espacement des lettres, et implémenter ajouter 1.25, nous avons l'espacement des lettres réglé.

Maintenant nous allons juste changer la taille et la graisse réglée sur medium.

Et maintenant nous avons nos majuscules dans le bouton, nous n'avons même pas à maintenir Shift enfoncé, ce qui est fantastique.

Et un autre changement mineur ici.

Pour ces textiles, nous allons bien sûr, changer la taille et la graisse.

Mais surtout, nous allons aux propriétés de texte nous allons changer la casse pour que les petites capitales soient en ligne avec la casse ici, juste parce que la taille de police est si petite réglée à 10.

Et à part ça vous pouvez aller de l'avant et faire le reste de ceux-ci aussi aura ce fichier et la description ci-dessous.

Donc je reviendrai tout de suite avec tous ces textiles.

D'accord, donc maintenant je sais que j'ai tous les textiles créés avec les propriétés appropriées.

J'espère que vous avez fait cet exercice aussi.

Et de toute façon, maintenant nous allons organiser nos styles et ensuite les publier, et ce sera le reste de la vidéo.

Donc nous allons utiliser la façon dont Figma structure l'accès aux textiles, il y a une façon vraiment agréable de, séparer minutieusement tout le contenu des en-têtes des sous-titres du corps ainsi que les textiles pour d'autres types de contenu, tels que les boutons, et les légendes et les surlignements.

Donc je vais juste aller ici, sélectionner mon textile, cliquer sur cette icône, cliquer sur le bouton plus pour créer un style.

Et je vais taper headers /.

Et avec la convention de nommage avec slash, cela va en fait me permettre de séparer mes textiles par catégorie.

Donc nous allons avoir nos en-têtes et sous-titres et corps et séparés ainsi que le contenu tel que boutons, légendes ou surlignements.

Donc je vais spécifier ce h1 ici.

Et ensuite cela va ajouter ce petit point ici pour le séparer.

Donc j'ai mon h1.

Et vous pouvez aussi spécifier la graisse de la police, qui est ce h1 est un h1 léger (light) au cas où vous auriez des variantes de h1 plus tard sur la route pour des raisons spécifiques.

Et une chose que nous pouvons aussi spécifier est la taille ici nos tailles 96.

Et j'aime bien ce que vous pouvez faire est d'utiliser ce diviseur et spécifier la hauteur de ligne par rapport à la taille de votre police, ce qui est aussi très important.

Mais j'ai tout cela réglé sur auto ici dans Figma.

Mais par exemple, vous pourriez écrire auto ou spécifier la hauteur de ligne.

Et encore une fois, quand vous créez ce style, il apparaîtra maintenant sous en-têtes (headers) chaque fois que vous essayez d'appliquer un style.

Disons que je veux appliquer un style maintenant.

C'est sous ce nom de catégorie headers.

Et une fois que c'est plus étoffé, ce sera beaucoup plus facile de voir l'organisation du contenu.

Donc je vais aller de l'avant ici et créer la même chose exacte pour mes en-têtes, le reste de mes en-têtes encore en utilisant la convention slash, spécifiant que c'est un h2.

Et il utilise la graisse légère (light).

Et la taille de police est 60.

Et la hauteur de ligne est réglée sur auto.

Et encore une fois, pour vos systèmes sont probablement plus spécifiques à la hauteur de ligne, mais dans cet exemple, je ne vais pas aller dans les détails à cet égard.

Donc créer ce style, vous remarquez qu'il se met à jour ici, nous allons peupler cela à nouveau, obtenu ce h3, spécifier la graisse encore, et spécifier la taille.

Et bien sûr, la hauteur de ligne.

Donc vous pouvez voir que ça continue de se peupler.

Et maintenant je vais aller de l'avant et finir le reste de ceci.

Je vais créer un sous-titre aussi pour que vous puissiez voir la différenciation de catégorisation entre deux catégories différentes, qui seront nos en-têtes et sous-titres.

Donc je vais aller chercher ici, ajouter le style, étiquette, subtitle, subtitle et 1, spécifier la graisse, juste regular.

Et ensuite bien sûr, la taille de cette police.

Et je ne sais pas, de tête, mais je vais le laisser réglé à six sous-titre réglé à 16, ce qu'il est, et la hauteur de ligne réglée sur auto.

Donc ici vous pouvez voir maintenant que vos textiles sont organisés.

Ici, clairement, et je vais aller de l'avant et finir le reste de ceci.

Et je reviens tout de suite.

D'accord, donc maintenant nous avons tout notre contenu configuré et organisé.

Donc vous pouvez voir que j'ai maintenant épissé ceux-ci en quoi est-ce 344 catégories, nous avons les en-têtes avec les sous-titres, et nous avons le corps et le contenu.

Et un textile qu'il me manque en fait est ce sous-titre qu'est-ce qui se passe ici, laissez-moi juste au-dessus de ça très vite.

Nous avons subtitle, subtitle, subtitle voulait, oh, voilà.

Je vais juste organiser ça très vite.

Voilà.

Donc dans l'ordre dans lequel vous créez vos textiles est comment cela apparaîtra dans la hiérarchie.

Donc vous devrez peut-être organiser cela.

Et maintenant quand nous allons de l'avant et créons un textile, je veux dire créer, quand nous avons besoin d'appliquer un textile, nous pouvons aller ici, regarder nos textiles.

Et maintenant ils sont magnifiquement organisés d'une manière claire, concise.

Et non seulement ils sont organisés, chaque textile nommé de telle manière qu'il est facile de spécifier la taille, et la hauteur de ligne aussi.

Et encore une fois, j'ai juste cela réglé sur auto.

Euh, vous pourriez aussi faire cela l'espacement des lettres ici si vous vouliez cela dépend à quel point vous avez vraiment besoin d'être technique.

Et c'est comme ça que vous faites cela.

Et maintenant notre dernière étape est de publier ceci dans notre bibliothèque.

Donc maintenant j'ai 26 changements à publier ici.

Et pour ceux qui ne savent pas comment utiliser ceci, c'est essentiellement comme un commit git.

Pour ceux d'entre vous qui sont développeurs ignorez tous ces textiles supprimés, ce sont des vieux.

Et ici, vous pourrez voir tous les changements que vous avez créés, qui sont tous les textiles que vous avez ajoutés.

Et nous pouvons écrire une description.

ajout de styles de texte au système de design.

C'est très vague, mais vous donne une idée générale de comment faire cela.

Et encore une fois, vous pouvez voir tous les changements faits, et tout ce qui est inchangé ici en dessous.

Et ensuite et vous pouvez publier.

Et la chose agréable à propos de laisser des commentaires est que cela laisse une trace pour suivre tout historique.

Donc si nous allons à afficher l'historique des versions ici, en cliquant sur ce chevron, cliquer sur Afficher l'historique des versions, nous pouvons voir que nous venons de publier nos textiles et nous avons laissé ce message.

Donc nous pouvons en fait aller à ce moment précis en cliquant dessus.

Et cela nous y amènera.

Ou nous pourrions aller encore plus loin en arrière à un moment où ceux-ci n'étaient même pas créés.

Donc si je clique sur 18h47, ça va charger et je vois le moment où cette sauvegarde automatique à 18h47.

Et vous pouvez voir qu'il n'y a pas de textiles ici.

Et vous ne pouvez pas éditer cette version.

Mais disons que vous en aviez besoin, vous pourriez dupliquer ceci et ensuite aller à ce fichier dupliqué et saisir ce dont vous avez besoin et ensuite l'apporter dans la version actuelle.

Et si vous appuyez sur échap, vous pouvez revenir à votre version actuelle ou vous pouvez cliquer sur le bouton éditer la version actuelle.

Et si vous êtes perdu, je taperais deux sous les claviers la touche de raccourci pour ajuster tout, tout dans votre canevas à votre cadre et Maintenant nous nous sommes retrouvés ici, avec tous nos textiles ici, plus locaux maintenant.

Maintenant publiés.

Donc maintenant les designers peuvent en fait accéder à cela dans leur panneau ici, nous allons à, j'ai le mien réglé sur material design ici avec toutes mes couleurs publiées et mes textiles.

Aujourd'hui nous parlons de l'élévation et du material design et comment c'est utilisé.

Donc nous ferons un aperçu de l'élévation, qui impliquera l'élévation représentant, comprendre représenter l'élévation, la hiérarchie d'élévation, et l'élévation par défaut définie pour les composants.

Et j'ai de la documentation que j'ai saisie sur le site web de material design, à laquelle vous pouvez aussi accéder en cliquant sur ceci et le fichier d'exercice et en cliquant sur ouvrir le lien.

Et ensuite vous aurez alors accès à la page d'élévation dans material design, où il discute de tout cela, et comme couvert dans le contenu ici en profondeur.

Et essentiellement, l'élévation est la distance relative entre deux surfaces le long de l'axe z.

Donc qu'est-ce que l'axe z ? Eh bien, nous allons de l'avant et faisons une recherche Google là-dessus.

Et pour ceux d'entre vous qui sont débutants à ce sujet et ne comprennent pas l'axe z, c'est le troisième accès représentant généralement la profondeur sur une grille tridimensionnelle.

Il peut être utilisé dans des diagrammes ou des graphiques, et ainsi de suite, typiquement, dans un système de coordonnées cartésiennes, et l'axe z est perpendiculaire aux deux axes x et y, et est utilisé pour tracer la valeur de z, la troisième et inconnue en mathématiques, ce qui est, ce qui est bon à savoir.

Et de toute façon, comment cela se traduit dans Figma est essentiellement la hiérarchie.

Et dans les dans les calques, vous pouvez penser à comme la hiérarchie dans le panneau Calques, disons, par exemple, j'ai un cadre ici.

Et ensuite j'ai quelques formes.

Et je vais décaler cette couleur ici.

Et actuellement, les formes utilisent essentiellement l'index Z.

Et vous remarquez cela parce que ce rectangle, quand je le chevauche sur le rectangle au-dessus visuellement, ce rectangle gris, et j'ajoute ce rectangle rouge là, vous remarquerez que ce rectangle rouge est plus haut sur l'index Z et aussi vous pouvez penser à cela dans l'ordre des calques aussi, je peux même changer cela et le glisser en dessous de ce rectangle gris, signifiant qu'il est maintenant plus bas sur l'index Z le rectangle rouge, et vous pouvez aller de l'avant et déplacer cela autour et comprendre que c'est l'index Z qui représente l'ordre des calques ici.

Et essentiellement, ce que fait material design est qu'il a un ensemble de composants.

Et ici vous pouvez voir un ensemble de valeurs d'élévation par défaut pour toutes sortes de composants.

Et ici, nous avons toutes les élévations.

Valeurs qui se transformeront en styles car elles sont déjà dans ce fichier Figma localement.

Et nous allons aller de l'avant et créer quelques-unes d'entre elles à partir de zéro pour que vous compreniez comment elles sont construites en tant que styles.

Et nous allons aussi aller de l'avant et faire un bref aperçu sur comment celles-ci sont faites sur la base de la lecture de la documentation.

Donc ici, encore une fois, l'élévation est mesurée en dips.

Et en élévation l'élévation material design mesure la distance entre les surfaces.

Comme vous pouvez le voir ici, ils vous donnent une représentation de ce à quoi ressemble cet index z, en utilisant ce graphique ici, ce format pour indiquer à quelle distance une surface est d'une autre.

Mais encore une fois, pour nous, cela semble horrible pour nous visuellement c'est nous voyons ce cheval sur cette surface plate sur l'écran.

Mais si vous deviez incliner cette vue latéralement, vous pourriez dire, c'est à quoi cela ressemblerait dans le scénario où cet exemple numéro deux indique qu'il y a une surface qui est à un dip d'élévation, et ensuite l'autre surface est réglée à huit dip d'élévation, comme vu de la vue latérale ici.

Et la différence entre les deux surfaces est de sept dips comme vu de l'angle latéral.

Et vous pouvez représenter cela en utilisant une ombre portée.

Et cela indiquera l'élévation et la distance entre ces deux surfaces.

Donc voici le un dip ici dans ce rectangle, et ensuite qui est représenté de la vue latérale.

Et ensuite voici l'élévation étant exprimée à une élévation plus élevée, en utilisant huit dips avec beaucoup plus d'emphase visuelle sur l'ombre portée comme vous pouvez le voir, et c'est aussi représenté ici de côté.

Et il y a cette distance exprimée là.

Et il y a un autre exemple plus compliqué sont les deux surfaces A et B sont à la même élévation a nBw sont réglés à huit dip d'élévation, et elles projettent des ombres différentes parce que la surface B est devant une autre surface qui a déjà une élévation.

Comme vous pouvez le voir, la surface c a déjà une élévation réglée à quatre dips.

Et ensuite par-dessus cela la surface B est réglée à huit dips, comme vous pouvez le voir comme représenté de côté, tandis que la surface a est juste n'a rien d'autre en dessous.

Et elle est réglée à huit dips d'élévation.

Donc a et b sont essentiellement sur la même élévation d'axe, c'est juste qu'il n'a pas d'autre surface en dessous.

Et vous pouvez comprendre le système d'élévation, encore une fois, est utilisé dans les composants et toutes les surfaces material design et composants ont des valeurs d'élévation, et les surfaces à différentes élévations font différentes choses.

Et ces choses étant permettre aux surfaces de se déplacer devant et derrière d'autres surfaces telles que le contenu défilant derrière les barres d'application, et reflétant les relations spatiales telles que comment l'ombre d'un bouton d'action flottant indique qu'il est séparé d'une carte et concentrant l'attention sur l'élévation la plus élevée.

Ceci est couramment vu dans les composants tels que les dialogues, qui apparaissent temporairement devant d'autres surfaces.

Et nous allons aller de l'avant et regarder quelques excellents exemples de comment ces composants sont dans quelques exemples de mouvement.

Mais voici un excellent exemple d'élévation au repos, où par défaut, ce composant carte ici a une élévation par défaut réglée à un dip.

Et ensuite une fois qu'il est une fois qu'il y a une action prise dessus, parfois l'élévation peut changer.

Donc il est important de savoir donc par exemple avec un bouton, l'élévation changera en fonction de quand vous appuyez dessus.

Donc ici dans cet exemple, quand quand quelqu'un appuie sur ce bouton, vous verrez que de côté, il passe de deux dips à huit dips basé sur cette action qui le soulève à la surface, rendant cela une expérience beaucoup plus immersive et interactive, transmettant aussi certaines interactions clés et progression à l'utilisateur alors qu'ils communiquent avec leur produit, qui est construit sur le dessus de material design, par exemple.

Et ici vous pouvez parler vous pouvez voir d'autres exemples d'élévation ici avec cette carte, alors qu'elle est glissée, elle passe de un dip d'élévation à huit, et est ensuite revisitée et ensuite s'élève au-dessus de la carte précédente car elle est au-dessus dans l'index Z.

Et voici un autre exemple de quand vous utiliseriez l'élévation où ces cartes défilent.

Et étant sur ce système basé sur l'élévation est autorisé à défiler sur la surface au-dessus de laquelle il est actuellement que vous pouvez voir là.

Et vous pouvez aussi lire d'autres choses importantes, telles que comprendre les chevauchements de surface sur le dessus d'autres surfaces, et quand les utiliser, ce qui est vraiment important.

Et aussi quand utiliser un arrière-plan scrim dans l'UI pour exprimer que le contenu au-dessus est à une élévation plus élevée aussi pour fournir plus d'emphase sur les appels à l'action les plus primaires à ce moment précis.

Et encore une fois, plus d'excellentes analyses approfondies sur l'élévation.

Et quand quand vous pouvez utiliser le mouvement et l'élévation ensemble, comme par exemple, montrer des changements dans l'ombre ou afficher le chevauchement, ou pousser le contenu autour ou mettre à l'échelle ce contenu ou utiliser le défilement parallaxe.

Et ce à quoi nous allons arriver maintenant est de comprendre la hiérarchie d'élévation.

Et essentiellement passer en revue le diagramme des valeurs d'élévation par défaut, ce qui est super important.

Et nous avons cela dans Figma.

Maintenant que nous avons passé en revue tout cela.

Donc nous avons cet ensemble de valeurs d'élévation, qui nous dit exactement quels composants ont des valeurs d'élévation par défaut.

Et ce sera super important à implémenter dans nos styles de couleur.

Donc dans ce fichier Figma que j'ai déjà créé.

J'ai déjà créé un ensemble de valeurs d'élévation et ce sont déjà des styles d'effet dans dans votre fichier Figma, ce fichier d'exercice.

Et encore une fois, c'est le résultat final de ce que nous allons cuisiner, mais je ne veux pas juste vous remettre ceci et en fait vous montrer comment créer ces styles d'effet.

Donc nous allons aller de l'avant et créer quelques-uns d'entre eux et ensuite et ensuite je mettrai cette vidéo en pause et vous ferai construire le reste par vous-même.

Donc d'abord je dois vous apprendre comment réellement évaluer les valeurs à l'intérieur de chacune de ces ombres portées.

Donc ici vous pouvez voir ce sont toutes les valeurs d'élévation utilisées dans material design.

Et encore une fois, celle-ci n'est pas.

Celle-ci est au niveau de la surface, cela n'utilise pas d'élévation comme vous pouvez le voir, réglé à 00 dip.

Et cela alors ne peut pas être un style d'effet parce que cela n'utilise aucun effet.

C'est juste le plat la ligne de base, pensez juste à 00 comme la ligne de base.

Et ensuite, bien sûr, un dip est utilisé pour les cartes de barre de recherche à un état d'élévation au repos par défaut, ainsi que la barre de recherche à un état d'élévation au repos.

Et aussi les composants switch.

Et les boutons texte sont réglés à zéro et les composants standard side sheet sont réglés à zéro aussi.

Donc allons-y et faisons ceci je vais copier ceci.

Et vous remarquerez qu'il est attaché au style, je vais aller de l'avant et détacher cela.

Et vous remarquerez que ces styles sont tous des ombres portées.

Donc je vais aller de l'avant et supprimer tout ça.

Donc maintenant c'est plat ici à droite, et une chose que nous pouvons faire est que nous pouvons manuellement aller et cliquer sur ces styles individuels, ce qui est très fastidieux.

Et nous pouvons aller de l'avant et le faire de cette façon.

Donc si je clique sur cette valeur, donc par exemple, je pourrais faire une capture d'écran de tout cela, parce que je ne voudrais pas faire des allers-retours, en cliquant sur toutes ces ombres portées, et copiant, collant ces propriétés.

Donc je vais vous montrer la manière longue de faire cela.

Et ensuite je vais vous montrer la manière rapide, pour que vous ne fassiez plus jamais cette approche.

Donc laissez-moi juste annuler cela là.

Ensuite je vais coller ceci, voilà.

Donc je vais saisir ce dernier style d'ombre portée.

Et ensuite avec ce style d'ombre portée réglé, j'ai les trois ombres portées, et je vais recréer l'élévation réglée pour 01 dips.

Donc je vais aller de l'avant et cliquer sur effets.

Oups, je vais cliquer sur l'icône Créer un style d'effet j'ai par défaut, il sélectionne l'ombre portée, et il vous donnera quelques valeurs par défaut.

Donc je vais aller de l'avant et créer celui-ci ici.

Donc je vais changer le flou à un, et ceci et cela, je vais régler la valeur de l'axe y à un ici.

Et ensuite je vais garder la propagation à zéro et changer l'opacité à 14%.

Et il utilise une couleur noire, qui est 000000.

Et ensuite maintenant j'ai ce premier style d'ombre portée créé, vous pouvez commencer à voir que cette ombre portée est appliquée ici, mais c'est très clair dans la couleur de l'ombre portée comparé à celle-ci où c'est beaucoup plus net et sombre sur les bords du rectangle.

Et je vais aller de l'avant et créer cette seconde ombre portée.

Et avec cela, je vais juste imiter les propriétés dans cette ombre portée.

Et c'est réglé à un sur le flou, zéro sur la propagation, et deux sur l'axe y et une opacité de 12% je vais appuyer sur Entrée, je sais que cette seconde propriété d'ombre portée est appliquée, ensuite je vais aller de l'avant et supprimer ces deux, pour ne pas être confus et créer mon dernier effet, qui est un autre ensemble d'ombre portée, je vais aller de l'avant et appliquer ces valeurs à nouveau.

Donc un sur l'axe y, trois sur le flou, zéro propagation et 20% d'opacité.

Une fois que j'ai créé cela, vous remarquerez que j'ai maintenant une réplique exacte de l'ombre portée.

Ici.

La seule différence est que cette ombre portée est toute neuve, c'est toujours l'ombre portée du système material design.

C'est juste qu'elle n'est pas attachée à un style à des fins d'apprentissage, spécifiquement, pour que vous sachiez comment créer ces ombres portées.

Et nous pouvons aller de l'avant et transformer cela en un style.

Mais avant de transformer cela en un style, allons-y et montrons-vous la manière facile de faire cela.

Donc si nous maintenant que nous avons ce style, peut-être que nous allons de l'avant et dupliquons la version basée sur huit dip de ceci, et c'est toujours attaché à un, un style d'effet.

Donc je vais détacher ce style.

Je vais dupliquer ce rectangle.

Et je vais supprimer toutes ces ombres portées.

Et ce que je vais faire est de m'assurer que j'ai mon rectangle sélectionné, et je vais maintenir Option+Command+C.

Et ce que cela me permet de faire est de copier tous les styles associés à l'objet que j'ai sélectionné, qui est le rectangle et ensuite je peux coller ces styles sur mon nouveau style nouvel objet en cliquant sur ce rectangle et ensuite en appuyant sur Option+Command+V.

Et cela colle ces valeurs exactes d'ombre portée.

Vous remarquerez que quand je l'ai collé, cela a implémenté ces nouvelles valeurs d'ombre portée.

Et c'est beaucoup plus rapide que d'aller et de les implémenter manuellement comme je l'ai fait, et de référencer des captures d'écran.

Donc je n'ai pas eu à cliquer individuellement sur chaque panneau de propriété d'ombre portée et ensuite faire cela un par un.

C'est très ennuyeux.

Donc avec cela étant dit, utilisons cette approche maintenant.

Donc ici, nous pouvons juste copier, je commande clique sur tout le commande clique pour sélectionner le rectangle spécifiquement, et ensuite maintenir Shift+Command+clic sur tous ces rectangles ici.

Et essentiellement ce que je fais est de saisir tout cela, et ensuite je vais maintenir Option et glisser ceux-ci pour copier tout cela.

Et vous remarquerez ce que nous avons ici est toutes ces valeurs d'élévation, ou effets, tous ces rectangles sont attachés à des styles d'effets.

Mais nous ne voulons pas faire cela nous voulons utiliser la méthode de création d'ombres portées rapidement faire des copies de propriétés et les coller.

Et pour faire cela, nous devons aller de l'avant et dissocier détacher tous ces styles d'ombre portée.

Donc voilà, nous allons continuer à détacher ces styles, je sélectionne juste chacun individuellement, car vous ne pouvez pas sélectionner en masse ceux-ci et détacher, malheureusement pour les styles d'effet.

Mais vous pouvez faire cela avec les styles de couleur.

Donc maintenant que nous avons cela appliqué, je sais que ceux-ci sont tous dans un ordre séquentiel ou ordre approprié.

Donc ça va de un dip, élévation, 234-689-1216, et 24.

Donc tout ce que je vais faire est de dupliquer ceci très vite.

Et avant de détacher toutes ces valeurs d'ombre portée, et je vais dupliquer cela encore, et continuer à les dupliquer sur les rectangles que je n'ai pas créés.

ombres portées pour encore.

Et vous remarquerez qu'ils sont tous très plats, ce qui signifierait qu'ils utilisent l'élévation zéro dip essentiellement.

Et je vais juste aller de l'avant et cliquer sur ces options de commande, option C, et ensuite sélectionner l'objet auquel je veux coller l'ombre portée et ensuite cliquer sur Command+Option+V.

Et vous remarquerez que je suis maintenant juste essentiellement en train de copier et coller ces propriétés de style d'effets.

Donc maintenir option, Command+C, sélectionner le nouvel objet et ensuite faire option Command+V.

Et je saisis juste toutes ces propriétés d'ombre portée et les colle très rapidement.

Et c'est quelque chose que vous pouvez utiliser pour les couleurs aussi.

Donc si je change la couleur de ceci, cela copierait cette valeur de couleur, cela a toujours l'ombre portée, mais si je option Command+C, et ensuite sélectionner mon nouvel objet, et ensuite option Command+V, cela copie aussi cette valeur de remplissage.

Donc cela copie toutes les propriétés pas juste les styles d'effet, qui sont les ombres portées dans notre cas.

Donc prenez note de cet objet, Command+C, sélectionnez menu objet objet, Command+V, et ensuite faites la même chose pour le dernier ensemble d'élévation.

Et c'est très important à noter.

Et maintenant que nous avons construit tout cela, nous pouvons aller de l'avant et créer des styles d'effet à partir de ceux-ci.

Et comme vous pouvez le voir, nous les avons déjà créés.

Donc nous pouvons aller de l'avant et imiter un couple.

Et je vais aller de l'avant et c'est notre style d'effet zéro à deux dip.

Donc je vais aller de l'avant et cliquer sur mon icône de style et cliquer sur ajouter un nouveau style.

Et ensuite je vais taper zéro à deux dip.

Et c'est notre nouveau style d'effet.

Et nous aurons maintenant deux variantes de cela.

Et ensuite il est créé et il est réglé en bas.

Les styles les plus récents sont alors générés en bas de cette liste dans les styles d'effet et le panneau Propriétés, je peux même aller de l'avant et juste en créer un autre, vous remarquerez que ceci est maintenant lié à un style.

Et ceux-ci ne le sont pas encore parce que je n'ai pas créé les styles de couleur.

Je vais aller de l'avant et cliquer sur un autre, et cliquer sur l'icône de style et créer un nouveau style.

Et c'est ma valeur de base d'élévation 24 dip.

Donc j'ai 24 dip là, nous cliquerons sur Créer un style, j'ai maintenant zéro à deux dip et 24 dip créés.

Mais c'est uniquement pour vous montrer comment créer des styles à partir de ces valeurs d'élévation parce que vous allez les réutiliser maintes et maintes fois.

Donc je vais juste en fait supprimer ceux-ci puisque nous les avons déjà dans notre fichier.

Maintenant que vous savez comment créer des styles d'effet dans Figma.

Et avec cela étant dit, la seule chose manquant à ces styles d'effets est la documentation.

Et essentiellement ce que je référence est que dans ces styles d'effets, nous pouvons aller de l'avant et étiqueter où cette élévation s'appliquerait.

Donc je vais cliquer sur 24 dip et puisque nous avons le tableau des valeurs d'élévation par défaut, il me dit où quels composants ont cet ensemble d'élévation.

Donc je peux aller de l'avant et cliquer sur cette icône éditer le style et ajouter une description.

Vous et je peux taper utiliser pour les composants de dialogue et je vais appuyer sur tab et cela enregistrera ce changement, je vais appuyer sur retour, je vais aller de l'avant et sélectionner mon 16 dip, le style fixe, cliquer sur Éditer le style.

Et je vais continuer à ajouter la description.

Et actuellement rencontré les composants navigation drawer et modal bottom sheet.

Et les composants modal side sheet utilisent cette valeur d'élévation par défaut.

Donc je vais en fait aller de l'avant et saisir cela utilisé pour ces composants et avoir été le tiroir de navigation.

Et modal bottom sheet et modal side sheet.

Et maintenant que j'ai cette entrée, cela enregistrera cela et vous pouvez même retourner dans votre, votre style et l'éditer et vérifier si cela a enregistré la description.

Je vais continuer à saisir la description de sorte que lorsque vous publierez ceci et que d'autres designers commenceront à utiliser ces styles, ils pourront aller de l'avant et et cliquer sur cette description comprendre où vous appliqueriez réellement ce style d'élévation, ce qui est un excellent outil utile pour communiquer à votre designer, surtout quand vous ne les designers ne se souviennent pas où ces styles sont utilisés.

Et ici vous pouvez voir que beaucoup de composants utilisent la valeur d'élévation par défaut de huit dips.

Et je vais aller de l'avant et mettre cette vidéo en pause et je veux que vous alliez de l'avant et pour le reste de ceux-ci pour les styles d'effets de fonte huit dips 64321 dip, je veux que vous alliez de l'avant et référenciez ce tableau ici et saisissiez cela dans la description comme nous venons de le faire pour pour les styles d'effets suivants.

Je vais mettre cette vidéo en pause et je vous retrouverai quand ce sera fait.

Donc maintenant j'ai terminé de saisir toutes les descriptions pour le reste des valeurs d'élévation.

Comme vous pouvez le voir ici, c'est un reflet direct de ce qui est étiqueté dans le tableau des valeurs d'élévation par défaut et material design.

Et encore une fois, j'ai obtenu ces captures d'écran de la page d'élévation material design, qui est aussi un lien ici et fichier d'exercice si vous voulez vérifier les choses, et aussi s'imprégner de plus d'informations sur l'élévation elle-même.

Parce que ce n'est pas seulement applicable au système de design de material designs, mais d'excellents principes pour vous à utiliser comme fondation pour implémenter de nouveaux systèmes.

Donc c'est aussi quelque chose d'important à prendre en considération.

Et ici encore, si je vais à l'édition des styles, je vérifie juste toutes mes descriptions ici.

Et tout est prêt à l'emploi.

Aujourd'hui, nous allons parler des icônes produit et système et parler de pourquoi elles sont différentes.

Et les distinctions entre elles.

Et nous passerons en revue aussi les principes autour de comment les icônes sont faites dans material design, juste nous allons brièvement passer en revue cela.

Et ensuite nous allons aussi utiliser un outil que vous utiliserez tout au long du cours où si je vais de l'avant et sélectionne sur ce lien ici dans notre fichier d'exercice Material Design icons, je peux aller de l'avant et cliquer sur cette case à cocher et cliquer sur le lien.

Et vous remarquerez que nous avons cette ressource pour accéder réellement à ces icônes.

Donc pour dans ce fichier d'exercice, je suis allé de l'avant et importé certaines mais pas toutes les icônes système dans material design.

Et j'ai fait cela exprès, parce que je veux que vous soyez capable de faire cela vous-même.

Et non seulement faire cela vous-même, mais comprendre comment utiliser deux façons de le faire.

Donc dans vos fichiers d'exercice, vous aurez un dossier zip appelé Material Design icons.

Et dans ce dossier, il y a un ensemble d'icônes pour Android, pour développer pour Android.

Donc si vous concevez pour Android, vous avez ces icônes ici disponibles dans leur format approprié, comme vous pouvez le voir dans le format de fichier .XML.

Et aussi, nous avons la version basée sur la police de ces icônes.

Et ensuite nous avons les versions basées sur iOS.

Et ensuite nous les avons aussi exportées en tant que PNG à toutes les tailles, toutes les différentes tailles et de 18 dips, 2436 et 48 dips à 1x et 2x respectif à chaque taille, comme vous pouvez le voir là.

Et c'est très utile.

Mais aussi c'est beaucoup de matériel dans ce fichier.

Donc si cela semble être trop pour vous, vous pouvez en fait aller de l'avant et utiliser cette ressource ici.

Encore une fois, cette ressource peut être accédée en cliquant sur ce lien material design icons dans Figma.

Et en ouvrant cela et cela vous donnera accès à cette ressource incroyable que nous utiliserons tous les deux alors que nous construisons des composants dans ce cours juste au cas où nous aurions manqué quelques icônes ici dans Figma.

De mon exportation initiale comme vous pouvez le voir, j'ai ces icônes catégorisées visuellement.

Et non seulement cela dans le panneau Calques elles sont comme elles sont exportées.

Ce sont les Les noms de chaque icône, ce qui est génial, donc nous n'avons pas à aller de l'avant et étiqueter ceux-ci nous-mêmes.

Mais nous pouvons aussi peaufiner le nommage plus tard, si nous le souhaitons.

Peut-être que nous voulons nous débarrasser de ces traits de soulignement.

Et nous y arriverons quand nous publierons réellement ces composants pour les utiliser à travers nos designs.

Et ici nous avons un ensemble de 10 catégories, actions utilisateur, icône, icônes de police, icône spécifique aux appareils.

Donc ici, vous pouvez voir que ceci est définitivement lourdement utilisé dans les appareils Android et iOS ici indiquant l'état des batteries, mode avion, s'il est allumé ou éteint, ou si vous avez réglé des alarmes, ou si votre Bluetooth est activé, connecté ou désactivé, et d'autres choses de cette nature.

Et c'est cette catégorie d'appareil.

Et ensuite nous avons quelques autres catégories, telles que quelques icônes d'éditeur, que l'on peut voir couramment utilisées et d'autres produits Google comme Google Docs, comme certaines de celles-ci sont des options, quand vous sélectionnez du texte et les éditez en termes d'alignement ici, quelques icônes d'alignement et ainsi de suite.

Aussi quelques icônes matérielles, icônes de contenu, icônes de fichier, et quelques autres icônes telles que des icônes d'alerte de communication.

Et encore une fois, c'est seulement toucher à la surface des icônes, parce que dans cet outil, il y a une fonctionnalité importante.

Sous cette catégorie thèmes.

Et en haut à gauche, vous verrez qu'il y a différentes variantes de toutes ces icônes.

Donc il y a la version remplie.

Et il y a la version contour là.

Et vous remarquerez que cette version remplie, la est définitivement différente de la version contour, vous pouvez utiliser ces deux versions de la même icône pour indiquer l'état.

Et il y a aussi une version arrondie de ces icônes où les coins sont beaucoup plus arrondis, comme vous pouvez le voir ici, comparé à la variante contour, les éléments deviennent plus arrondis, et lisses vous pourriez dire, nous avons aussi cette variante deux tons, vous remarquerez qu'il y a ce second ton de couleur implémenté, qui est une sorte de gris clair, comme la couleur d'arrière-plan sur plusieurs éléments dans l'interface.

Et ensuite nous avons notre variante pointue (sharp) d'icônes, où les coins sont très certainement très pointus sur les bords, et ainsi de suite.

Donc avec ces variantes en tête, nous pouvons aussi basculer les catégories spécifiques spécifiquement actions ou si je veux seulement que les alertes apparaissent, ou seulement que les icônes a V apparaissent, ou seulement que les icônes de communication apparaissent.

Donc essentiellement avoir la capacité de voir toutes ces icônes individuellement ou voir toutes à la fois comme il y a une tonne d'icônes, je vous recommande de juste parcourir ceci comprendre ce que vous pensez que vous ferez et ne ferez pas utiliser et pourquoi pas serait un bon test, un ment à votre compréhension de material design, et les icônes nécessaires quand nous développons la bibliothèque de composants à l'avenir.

Et encore une fois, si nous n'avons pas celles-ci fichier Figma interne, ne vous en faites pas.

Si ce n'est pas ici déjà, nous pouvons aller de l'avant et juste créer une nouvelle catégorie ici.

Et bien sûr, disons que je n'ai pas d'icônes dans la catégorie sociale, comme il y a beaucoup d'icônes sociales, c'est aussi simple que de juste cliquer sur cette icône.

Et ensuite dans le coin inférieur gauche dans votre navigateur, vous remarquerez que vous avez la capacité d'exporter réellement cette icône.

Et cela vous dit quelle taille vous l'exporteriez et quel format donc c'est le format basé sur SVG de cette icône.

Et je peux aussi cliquer sur cela, pour ouvrir ce, ce panneau.

Et vous pouvez soit télécharger le format SVG, ou le format basé sur PNG, nous allons nous en tenir aux formats basés sur SVG.

Et il y a aussi quelques instructions sur comment styliser vos icônes en utilisant CSS, cela vous donne un petit exemple ici.

Et vous pouvez aussi changer la taille, laquelle vous téléchargez ce, SVG nous les téléchargerons en 24 dips.

Donc et vous pouvez aussi obtenir la version noire de l'icône ou la version blanche de l'icône, nous allons nous en tenir à la version noire de l'icône.

Comme nous allons concevoir pour le thème clair dans notre contenu, tel que la typographie, et les icônes seront sombres par opposition à claires.

Et vous pouvez aussi télécharger la version basée sur iOS, la version Android de ceci.

Et encore une fois, vous avez toutes ces icônes déjà dans votre votre fichier dans vos fichiers d'exercice que vous avez téléchargés sous, vous pouvez les obtenir sous source ou quel que soit l'appareil pour lequel vous concevez vous avez toutes ces icônes ici dans tous les formats, le contour rond aiguiser et variantes deux tons et la variante remplie aussi.

Donc avec cela étant dit, nous pouvons aller de l'avant et parler de maintenant que nous avons parlé de toutes les icônes système, ce qui est ce que nous venons de couvrir, nous venons de couvrir toutes les icônes système, encore une fois, qui est aussi dans cette documentation ici qui sera accessible dans le fichier Figma aussi.

Je m'assurerai que c'est là-dedans.

Donc vous pouvez cliquer sur ce lien.

Donc essentiellement, cela symbolise des actions communes pour les fichiers, appareils et répertoires.

Et tout le concept est d'être simple, moderne, amical, et parfois excentrique car chaque icône est réduite à sa forme minimale exprimant des caractéristiques essentielles pour l'action que vous essayez de prendre avec cet élément de design auquel l'icône est associée.

Et vous pouvez voir, si vous deviez créer vos propres icônes aussi, cela vous apprend comment même créer des icônes avec les paramètres appropriés en ce qui concerne la construction du fichier, utilisant les spécifications de la grille et des formes de lignes clés ici, et comment les utiliser sur des mises en page denses sont, et juste la mise en page de l'icône elle-même, ce qui est vraiment intéressant.

Et aussi juste d'autres spécifications aussi en ce qui concerne la décomposition de ce en quoi consiste une icône, et discuter de la couleur aussi, et les états pour une icône.

Et nous avons ces icônes, états sur fonds clairs spécifiés ici, ce qui est génial, et nous pouvons incorporer cela dans notre système à l'avenir.

Et cela parle des variantes aussi.

Les thèmes d'icônes, que nous avions passés en revue dans l'outil ici, les thèmes étant rempli, contour, arrondi deux tons et pointu.

Et cela est tout discuté ici dans les icônes système.

Et nous avons maintenant nous pouvons aussi jouer avec elles dans Figma.

Si vous voulez allez-y et cliquez dessus, copiez, collez-les, jetez-les dans des composants.

Mais nous ferons cela avec beaucoup plus d'attention à l'avenir quand nous commencerons à construire notre bibliothèque de composants.

Et je vous recommande de parcourir ceci et de le lire prendre des notes car cela vous informera certainement sur comment utiliser les icônes d'une manière systématique.

Et aussi juste augmenter votre jeu en tant que designer.

Donc avec cela étant dit, nous pouvons aller de l'avant et discuter des icônes produit maintenant.

Donc les icônes produit sont séparées des icônes système.

Parce que celles-ci sont c'est l'expression visuelle du produit d'une marque et les services et outils qu'ils offrent.

Donc par exemple, dans Google Chrome, si vous avez un compte Google ou un compte Gmail, vous remarquerez que ce sont des icônes produit, ce ne sont pas des icônes système, comme comme, comme dans ce navigateur.

Ce sont des icônes système, qui sont conçues pour des actions communes et des éléments sur une interface.

Tandis que ces icônes produit ici représentent le produit lui-même, le service ou l'outil.

Donc c'est quelque chose d'important à, à noter ou à appliquer une distinction.

Parce que si nous retournons en arrière et parlons des icônes produit, cela parle de comment cela exprime ce produit et comment c'est associé à l'entreprise par laquelle c'est fait donc ici vous pouvez voir cela étant parlé ici, où les icônes à cet égard Gmail, Google Calendar, et et quelques autres icônes communiquent l'idée centrale et l'intention d'un produit et elles simple, audacieuse et amicale manière, tandis que chaque icône est toujours distincte.

Et toutes les icônes produit pour une marque devraient être unifiées à travers ces concepts et et dans son exécution.

Et ici vous pouvez voir l'approche où ils voient réellement leur design comme du matériel étant une qualité physique, telle que le papier, où, où chaque pièce a été coupée, pliée, et éclairée.

Et cela utilise la lumière aussi en association à l'icône et représenté dans ce format numérique, pour vraiment faire ressortir ces surfaces pour interagir avec la lumière.

Et vous pouvez voir les reflets subtils ici et l'ombrage cohérent appliqué dans ces icônes produit.

Donc si nous allons de l'avant et retournons à la suite d'icônes produit de Google ici, vous pouvez voir que dans l'icône Gmail, et vous pouvez voir les ombres étant appliquées ici sur ces bords, et l'éclairage vraiment étant implémenté, exécuté de manière cohérente dans toutes les icônes produit.

Et vous pouvez obtenir des spécifications sur comment ces icônes sont construites et ainsi de suite.

Mais ce n'est pas super spécifique à ce que nous ferons mais je recommande fortement que vous parcouriez cela.

Si vous voulez jamais développer vos propres icônes dans le futur, c'est très utile parle de comment traiter les icônes, et comment elles devraient être au niveau de la surface d'un élément, etc, etc.

et comment appliquer une attention appropriée à une icône en ne convoluant pas l'icône avec des plis en accordéon excessifs.

Par exemple dans ce scénario où vous voyez ces plis en accordéon ou cela ressemble à ce papier pliant ou cette icône pliant par opposition à avoir trop de plis en accordéon n'utilisez pas plus de deux plis en accordéon ou juste un.

Deux fournissent vraiment un point focal clair à votre icône.

Et bien sûr ne pas déformer ou transformer vos icônes qu'elles soient icônes produit ou système.

Car cela n'est pas une approche intentionnelle du design.

Donc c'est à peu près tout ce que j'ai pour vous aujourd'hui sur les icônes produit.

Je vous recommande de juste sorte de pratiquer cliquer sur l'une de celles-ci, la télécharger en tant que SVG, et ensuite l'enregistrer dans un dossier quelque part qui a du sens pour vous.

Et encore une fois, vous avez déjà ces icônes.

Mais je recommande d'entrer dans l'habitude de cela aussi, parce que peut-être qu'il me manque une icône ici.

Et nous pouvons enregistrer ce SVG, je peux aller de l'avant et ouvrir Figma et accéder au dossier Téléchargements, mon finder, et juste glisser cette icône sur le canevas.

Et maintenant que j'ai cette icône, qui est en fait déjà ici, vous remarquerez que j'ai la version remplie de cette icône, comme il est indiqué ici.

Donc j'ai obtenu l'icône de rotation 3d à une taille de cadre de 24 par 24, la largeur et la hauteur réglées à 24 dips, ou dans ce cas pixels.

Ou, comme thigma l'appelle points, mais pour ne pas vous confondre là, appelez-les juste dips ici, et référencez la terminologie de mesure de material designs.

Et c'est tout vous venez d'ajouter vous pouvez l'ajouter dans votre bibliothèque et l'organiser en conséquence.

Et je vais aller de l'avant et continuer à construire cette bibliothèque aussi alors que nous avançons dans ce cours.

Mais c'est tout ce que j'ai pour vous quand il s'agit de parler d'iconographie.

Aujourd'hui, nous allons parler de la construction des fondations et spécifiquement passer en revue la lisibilité du texte et à quel point c'est vraiment important pour s'assurer que nous utilisons les bonnes valeurs de couleur.

Donc dans ce tutoriel, nous ferons un aperçu de la lisibilité du texte sur le site web de material designs.

Donc ici, il discute des normes de lisibilité.

Et dans notre précédent dans la vidéo précédente, nous avons passé en revue l'outil couleur Leonardo, et nous avons discuté brièvement de régler les ratios de contraste, ou utiliser cet outil pour obtenir les bons ratios de contraste.

Et nous allons parler de pourquoi c'est important en profondeur.

Et ici nous avons un article très important que je vous recommande de lire.

Et cet article relator est sur le site web de material designs couvrant l'accessibilité en général, je recommande fortement que nous, vous parcouriez cela, et dans son intégralité.

Donc ici parle de contraste de couleur, peut être utilisé pour aider les utilisateurs à voir et interpréter le contenu des applications et comment c'est utilisé lourdement à travers n'importe quelle et chaque interface pour les applications que vous construirez.

Et non seulement la couleur et le contraste, mais aussi parler de la mise en page et la typographie aussi.

Je recommande que vous lisiez à travers cela par vous-même.

Et nous toucherons aux normes WCAG et WCAG signifie Web Content Accessibility Guidelines (Règles pour l'accessibilité des contenus Web).

Et pour ceux d'entre vous qui ne savent pas, cela nécessite une conformité double a pour être ca g conformité double a pour avec un ratio 4.5 à un contraste de couleur entre le texte et les arrière-plans sur la typographie normale, typographie normale étant votre copie de corps, telle que la copie de corps dans, dans ce site web que je surligne.

Et aussi, un ratio de trois à un en utilisant de grands textes, un grand texte pourrait être ces en-têtes, s'assurant qu'ils ont un ratio de contraste de trois à un.

Et ici vous pouvez voir que c'est pratiquement noir sur un fond blanc.

Donc ces ratios de contraste seront très, très forts.

Et nous allons aller de l'avant et juste un peu passer par texte sur fond puisque c'est essentiellement sur quoi notre typographie sera.

Ce sera sur un fond sur une variété de composants.

Comme vous pouvez le voir ici dans cette image, ce texte est sur une barre d'application, et c'est sur la couleur de fond des barres d'application.

Et vous remarquerez aussi, ici nous avons une bannière de notification de sortes, où la typographie est superposée sur la couleur de fond de la notification.

Et une chose à couvrir qui est très importante est de parler de comment l'opacité du texte est appliquée dans material design car ils comptent lourdement dessus pour indiquer les états.

Donc encore une fois, le texte noir est recommandé pour une utilisation sur des fonds clairs et le texte blanc sur des fonds sombres.

Ce qui est important à noter, surtout si vous construisez votre application pour un thème clair ou un thème sombre.

Assurez-vous juste que le texte est disponible avec des ratios de contraste appropriés comme indiqué ci-dessus.

Et nous allons aller de l'avant et parler de la construction de certains de cela quelques exemples.

Et maintenant que nous avons un peu passé en revue l'utilisation de l'opacité du texte, ou sur comment c'est utilisé dans la capture d'écran et comment éviter de l'utiliser.

Ici vous pouvez voir que cette typographie ne change pas l'opacité de la couleur du texte.

Mais ici vous pouvez voir que l'opacité a été modifiée, par conséquent, dégageant une couleur grise opaque, qui n'est pas lisible et très difficile à voir sur des surfaces colorées, comme vous pouvez le voir.

Et ensuite nous parlerons de texte sombre sur fonds clairs.

Donc material utilise ces principes.

Donc pour le, vous pouvez penser à ceci comme l'état actif si vous voulez, ou si vous voulez appliquer une haute emphase sur certaines informations, peut-être que vous voulez appliquer une haute emphase sur les en-têtes, par exemple, tels que ce site web, utiliser la couleur noire, avec une opacité de 87%.

Et ensuite si vous voulez appliquer une emphase moyenne, qui pourrait être une emphase moyenne, telle que la typographie, ou un état par défaut pour, pour le type plus haut payant au sein d'un composant, vous utilisez la couleur noire à une opacité de 60%.

Et ensuite l'état désactivé utilise une opacité de 30 38% avec la couleur noire.

Et nous allons aller de l'avant et parler de comment utiliser avec parcimonie les textes colorés sur le dessus des arrière-plans.

Donc le texte coloré n'est généralement pas utilisé partout.

Et c'est utilisé sélectivement pour attirer l'attention et appliquer.

très sélective emphase est idéalement le texte de couleur devrait être réservé pour les éléments de texte tels que les titres, boutons, et liens.

Et ici vous pouvez voir une utilisation prudente de, de couleur.

À travers la typographie.

Ici vous pouvez voir jaune et noir et ce fond rose violet est juste fortement non recommandé.

Je ne recommanderais même pas cela, par opposition à être prudent.

Soyez juste conscient, si si vous remettez en question certains éléments de design tels que ceci, il vaut mieux ne pas utiliser cela, et s'en tenir aux normes.

Et ici vous pouvez voir de grands titres et de courts extraits techniques sont les meilleurs pour le texte couleur.

Et ensuite nous allons aller de l'avant et parler du texte d'aide (helper text).

Et le texte d'aide donne essentiellement un contexte sur une entrée de champ, tel que comment l'entrée sera utilisée, et il peut adopter les couleurs de la marque aussi mais devrait être lisible.

Par tous les moyens, selon les normes WCAG.

Et encore une fois, cela utilise les mêmes principes.

Les seules différences sont le texte d'aide utilise une opacité de 60% de la couleur noire, et ensuite le texte d'erreur utilise 100% d'opacité de la couleur rouge.

Et vous pouvez voir cette valeur hexadécimale juste là.

Donc où verriez-vous réellement cela ? Eh bien, vous pouvez voir cela dans le champ de saisie de texte de material designs.

Donc si nous allons réellement aux composants ici, et allons à oups, et nous cherchons une entrée de texte.

Voyons si nous pouvons trouver ce champ de texte ici champs de texte.

Et nous pouvons sélectionner les spécifications, vous remarquerez qu'il y a un message d'erreur ici pour cette image pour ce champ de saisie de texte, qui utilise le texte d'erreur ici cette propriété de couleur appliquée à la typographie pour donner un contexte sur cette entrée de champ, qui est juste ici.

Donc c'était la mauvaise entrée par l'utilisateur dans cet exemple, et il y a un message d'erreur qui apparaît.

Et ensuite dans ce champ de texte, il a du texte d'aide qui est indiqué juste là, qui est reflété juste ici.

Et ce type de texte cette variante de texte d'aide, qui est très importante.

Et nous pouvons aussi discuter du texte sélectionné ensuite, donc le texte sélectionné peut refléter votre marque.

Et il peut utiliser un accent de votre couleur primaire ou secondaire et cela devrait être lisible contre la couleur de sélection et la couleur de sélection devrait contraster la couleur de fond.

Donc c'est quelque chose d'important à noter ici vous pouvez voir que material design utilise la couleur variante primaire pour le surlignage pour la couleur de sélection de texte, surlignant tout le texte sélectionné.

Et aussi, une autre chose importante à noter est que les icônes et autres symboles utilisent les mêmes principes pour représenter les icônes et autres symboles que la typographie.

Et quand je dis typographie, je fais référence aux textes sombres sur fonds clairs et texte clair sur fonds sombres utilise les mêmes principes.

Et il adhère juste à des niveaux d'opacité spécifiques.

Et ce sont les mêmes niveaux d'opacité où ils utilisent tous la même couleur noire à différents niveaux d'opacité.

Donc l'état actif est un ensemble à un noir de 87% et actif est 60%.

Et l'état désactivé est 38%.

Et une chose que vous pourriez vous demander est comment vous appliquez réellement cet état à votre typographie.

Donc une chose que nous pouvons faire est de saisir ces captures d'écran ici.

Donc je peux saisir une capture d'écran de ceci et ensuite aller de l'avant et ouvrir notre fichier d'exercice.

La lisibilité du texte soudaine va aller de l'avant et aussi référencer les types de texte ici.

Et essentiellement avec toutes ces captures d'écran, nous allons justifier combien de types de styles de couleur nous aurons besoin pour fournir l'emphase appropriée dans les composants alors que nous les créons, et ensuite les construire en tant que styles de couleur, que nous publierons ensuite pour réutiliser.

donc ici nous pouvons voir, j'ai dit itérateur avant.

Les icônes et les symboles ont les mêmes principes pour le texte sombre sur fonds clairs et les textes clairs sur fonds sombres.

Cela utilise les mêmes principes et niveaux d'opacité.

Donc, signifiant que nous n'avons besoin en fait de créer que trois styles ici.

C'est l'actif, inactif et désactivé pour les icônes et les symboles, excusez-moi.

Aussi, juste fournir la haute emphase, emphase moyenne et état désactivé pour le texte sombre sur fond clair.

Donc ce que nous pouvons faire est de laisser tout cela vivre sous une section de contenu de styles de couleur aussi.

Donc nous pouvons aller de l'avant et définir cela comme étendre l'iconographie.

Donc c'est essentiellement ce qui est couvert dans toutes ces trois captures d'écran.

Donc ce que nous pouvons faire est juste de créer un textile, donc nous pouvons commencer avec cette capture d'écran, je vais déplacer celles-ci hors des chemins, pour ne pas confondre aucun d'entre vous.

Puisqu'il y a beaucoup d'informations dans cette zone, je vais en fait juste saisir un textile et material design utilise juste Roboto.

Peu importe ce que sont les paramètres de type.

Je vais juste changer ça très vite.

Et et maintenant, tout ce que nous allons vouloir faire est de définir la couleur.

Et cet état actif est réglé à 87%.

Actuellement, la couleur est réglée à 100.

Donc je vais juste changer ce champ de saisie, ce que nous pouvons faire est juste de sélectionner cette icône de style.

Et vous remarquerez que nous pouvons aller de l'avant et cliquer sur Créer un style.

Et ensuite je vais taper text, and iconography.

Et ça va être cette convention de nommage va être l'en-tête.

Donc nous savons comment utiliser cela dans le panneau de couleur.

Donc je vais juste sélectionner active active ici.

Et ensuite vous pouvez aussi spécifier le pourcentage si vous voulez que les designers soient capables de lire cela d'emblée alors qu'ils regardent le nom du style de couleur, ou vous pouvez l'enlever, je vais juste l'enlever et sélectionner Créer un style, j'ai maintenant créé ce style de texte, ce qui est exactement ce que je veux pour toute icône active ou autres symboles.

Et ensuite nous allons aller de l'avant et dupliquer ceci.

Et une fois que c'est dupliqué, je vais détacher le style.

Et juste spécifier l'état inactif, ce qui est très simple.

Tout ce que nous avons à faire est de changer la ville du chemin une fois de plus à 60%.

Et cela représente l'état inactif de toutes icônes ou autres symboles.

Et je vais aller de l'avant et créer un autre style.

Et encore une fois, j'ai juste étiqueté ce text and iconography, la catégorie utilise la convention de nommage flash.

Et maintenant je vais spécifier inactive.

Et ensuite nous pouvons aussi spécifier que cet état inactif est si je clique sur cette icône éditer le style, je peux ajouter une description et aller de l'avant et déclarer que utilisé pour les icônes et autres symboles comme spécifié ici.

Au cas où les designers veulent savoir à quoi sert ce style de couleur s'ils ne sont pas sûrs comment l'utiliser.

C'est très important.

Vous pouvez aller de l'avant et modifier ces propriétés aussi plus tard sur la route aussi.

Je vais aller de l'avant et dupliquer ceci et détacher le style et régler cela à l'opacité de 38%.

Et nous avons maintenant l'état désactivé pour notre non seulement icônes et autres symboles, mais nous avons l'état désactivé pour notre typographie aussi.

Donc je vais aller de l'avant et cliquer sur l'icône de style à nouveau, créer ce style, et l'étiqueter text and iconography.

Et maintenant que nous avons cela, nous pouvons aller de l'avant et étiqueter ceci disabled (désactivé).

Et maintenant nous avons nos trois styles de couleur.

Si je vais de l'avant et sélectionne du texte à nouveau, et je vais à mes styles de couleur, vous remarquerez que j'ai la section text and iconography et entendez cela non seulement me donne le nom de ce style de couleur, mais cela me donnera aussi la description s'il y a une description, comme vous pouvez le voir ici dans l'infobulle, alors que vous passez la souris sur le style de couleur, afin que vous puissiez comprendre ce qu'est l'utilisation, ou la description pour ce style de couleur.

Donc c'est génial.

Et maintenant que nous avons cet état actif ici, cela pourrait être une question de, nous pourrions faire un divers, il y a diverses décisions que vous pouvez prendre avec votre équipe alors que vous construisez votre système de design car la nomenclature est extrêmement importante quand vous commencez à implémenter ces éléments fondateurs dans votre système de design.

Donc une question que je pose, et que vous pourriez vous poser aussi en ce moment est que si ce sont les mêmes valeurs, mêmes valeurs hexadécimales, même opacité, et pour tout, voici du texte sombre sur des fonds clairs et icônes et autres symboles, devrais-je recréer d'autres styles ? Eh bien, la réponse est non, vous n'avez pas à le faire, ce que vous pourriez faire est d'aller de l'avant, éditer ceci et spécifier que ceci dans la description, vous pourriez spécifier que c'est aussi une haute emphase, n'est-ce pas.

Donc vous pourriez spécifier que c'est une haute emphase pour pour le texte sombre sur fonds clairs.

Ou, mieux encore, ce que nous pouvons faire est, au lieu d'avoir les utilisateurs aller à la description du style de couleur pour identifier exactement ce qu'est l'utilisation, pour ce style de couleur, je vais aller de l'avant et juste modifier le nom de ceci.

Donc ce que je vais faire est de spécifier que c'est une haute emphase.

Et je vais aller de l'avant et mettre entre parenthèses, l'état actif, ou vous pourriez le faire vice versa.

Et ensuite je vais juste enregistrer cela, maintenant cela a été enregistré, c'est une haute emphase, je vais aller de l'avant et sélectionner l'état inactif et m'assurer que j'édite le nom aussi.

Et ensuite spécifier une emphase moyenne.

Et une fois que j'ai spécifié cela, je sauverai cela.

Et maintenant je vais aller de l'avant et sélectionner ceci, et désactivé est juste désactivé.

Donc c'est fantastique.

Nous n'avons même pas à renommer cela en fait.

Et ce sont des décisions importantes à prendre et à comprendre, comme vous pouvez voir que rapidement un système de design pourrait être très pollué en termes de comment vous nommez les choses, non seulement dans votre système de design ou designs, mais aussi dans le développement, c'est très important de vraiment synchroniser avec vos ingénieurs et comprendre ce qu'ils ont implémenté dans leur dans leur palette de couleurs, ou ce où que soit ce fichier CSS ce fichier sass less, où que soit cette palette de couleurs dans react par exemples, c'est un cadre très populaire en ce moment, essayant vraiment de comprendre où ces valeurs hexadécimales se trouvent.

Si ce sont même des valeurs hexadécimales ou la base RGBA.

Base.

Ce sont des questions très importantes à poser à vos développeurs si vous ne l'avez pas déjà fait, et pour vraiment commencer à aligner votre système avec ce qui est actuellement en développement pour vraiment améliorer le flux de travail parmi les designers et ingénieurs et vraiment commencer à solidifier et créer un langage unifié à travers le design et l'ingénierie.

Donc c'est tout pour le texte sombre sur fonds clairs et icônes et autres symboles.

Ensuite, nous allons aller de l'avant et parler des des types de texte.

Donc une chose que nous avons manquée est que nous avons étiqueté cette emphase moyenne et inactif pour cet pour cet état ici, emphase moyenne.

Et inactif, nous pouvons aussi spécifier dans la description que ceci est utilisé pour le texte d'aide.

Donc je peux aller de l'avant et spécifier cela là.

Et cela résout mon problème.

Et ensuite nous pouvons le dernier style de couleur de texte dont nous avons besoin est le texte d'erreur.

Donc nous devons aller de l'avant et dupliquer ceci.

Détacher le style, régler l'opacité de retour à 100%.

Et ensuite aller de l'avant et régler cette couleur au rouge.

Et maintenant que nous avons la couleur réglée à lire, nous sommes prêts à partir.

Tout ce que nous avons à faire est de cliquer sur l'icône de style Cliquez sur Créer un style, et ensuite s'assurer qu'il est sous la même catégorie que le reste des styles de couleur et taper air (error), text et créer un style.

Et nous sommes en train de déchirer les gars, nous avons créé tous les styles de couleur dont nous aurons besoin pour utiliser alors que nous continuons à construire la fondation de notre système de design material.

Donc si nous allons de l'avant et vérifions ces styles de couleur localement, et disons que je sors comme un rectangle, et vais et regarde ma palette de couleurs.

Tout vit sous text and iconography et mon panneau de styles de couleur Et glissez cela par-dessus.

Et vous pouvez voir que maintenant j'ai ce texte, haute emphase, style de couleur, l'emphase moyenne, qui est aussi l'état inactif.

Nous avons aussi la haute emphase, qui est l'état actif pour les icônes et symboles et haute emphase concernant le texte sombre sur fonds clairs.

Donc nous nous assurons que tout ce contenu est réutilisé et simplifié.

Donc il n'y a pas de duplication de styles de couleur, ce qui n'est pas nécessaire, ni Est-ce nécessaire en développement non plus, si vous pouvez solidifier cela et le simplifier, et nous avons notre texte d'erreur aussi, et notre texte désactivé, qui est tout couvert ici, et c'est tout ce que j'ai pour vous dans la lisibilité du texte.

Et je recommande que vous passiez en revue les directives d'accessibilité du contenu web pour vraiment juste comprendre ceci, je sais beaucoup d'informations.

Mais plus vous lisez ceci et prenez des notes dessus, plus cela paiera et vous donnera un avantage en tant que designer, car l'accessibilité est extrêmement importante.

Nous allons couvrir les États sous la portion interaction de cette section dans la fondation.

Alors que nous continuons à construire notre fondation, nous allons passer en revue voir les états, si vous allez de l'avant et cliquez sur ce lien dans ce fichier d'exercice pour ouvrir un lien et vous donner accès à ces états ici.

Et une fois que vous avez cette page visible, vous pouvez voir que les états sont des représentations visuelles utilisées pour communiquer le statut d'un composant ou un élément interactif.

Et nous allons couvrir le nous allons faire un aperçu des contenus au sein de cette page et comment cela se traduit dans Figma.

Cela est traduit ici.

Et ensuite nous allons couvrir l'utilisation des états et quand les appliquer, obtenir une compréhension de cela.

Et nous allons passer en revue tous les types d'états aussi.

Et ensuite nous allons décomposer l'anatomie d'un état et comprendre l'utilisation et quelques directives fondatrices à suivre.

Et aussi, encore une fois, implémenter des états et Figma, et comment ils sont utilisés comme styles de couleur ou Oui, styles de couleur dans Figma.

Et je passerai en revue dans ces exemples que j'ai créés pour vous comment les implémenter.

Et nous allons aller de l'avant et en construire quelques-uns aussi.

Et sans plus tarder, commençons sur l'utilisation des états.

Donc les états communiquent le statut des éléments UI.

Ici, vous pouvez voir un état de survol sur ce composant, qui est une rangée d'onglets.

Ici, vous pouvez voir l'état pressé sur un bouton ici.

Et ici vous pouvez voir l'état glissé d'un composant puce.

Et ici vous pouvez voir l'état focus d'un bouton.

Et ici vous pouvez voir l'état sélectionné d'un élément de ligne.

Et il y a d'autres états, bien sûr, ici aussi.

Et encore une fois, cela communique le statut des éléments UI à l'utilisateur.

Et chaque état de statut devrait être visuellement similaire et ne pas modifier radicalement un composant, mais doit avoir des affordances claires qui le distinguent des autres états et de la mise en page environnante.

Donc avec cela en tête avec pour accomplir cela le material design adhère à ces trois principes distinction, s'assurer que ces états sont ont un principe additif à cela, où les états se produisent à la fois, tels que la sélection et le survol.

Et les deux indicateurs d'état sont affichés lors de la prise de ces actions, que ce soit une sélection ou un survol.

Et bien sûr, la cohérence est un autre principe où les états devraient être appliqués de manière cohérente à travers les composants afin d'augmenter l'utilisabilité.

Et bien sûr, ils les états sont distincts, ou ils ont des affordances claires, les distinguant les uns des autres.

En ce qui concerne l'UI environnante, c'est associé à l'accentuation selon leur niveau, leurs niveaux de priorité.

Et maintenant nous allons couvrir tous ces types d'états.

Donc ici vous pouvez voir qu'il y a un état activé.

Et cela utilise un exemple de bouton pour les quatre premiers états où un état activé communique un composant ou élément interactif.

Donc essentiellement, un état activé est juste l'état par défaut d'un composant.

Donc vous pouvez penser à activé comme par défaut.

Communique juste des trucs, ceci est un bouton sur lequel vous pouvez cliquer.

Et le désactivé ici est un état désactivé d'un bouton, qui déclare juste qu'un c'est un composant ou élément non interactif, donc vous ne pouvez pas réellement cliquer dessus car il est désactivé.

Et ici, nous avons un état de survol pour un bouton.

Et cela communique quand un utilisateur a placé un curseur au-dessus d'un élément interactif.

Et nous avons aussi un état focus où cela communique quand un utilisateur a surligné un élément en utilisant une méthode d'entrée telle qu'un clavier ou la voix.

Donc si j'appuie sur tab, vous remarquerez que je peux tabuler à travers cette interface ici.

Je tabule vers ce ce lien d'ancrage et je tabule Vers ce bouton ici.

C'est l'état focus sur ce bouton.

Donc c'est un exemple de cela.

Si nous retournons ici aux types d'états oups, une seconde.

Donc si nous retournons à ces types d'états, ici, nous avons l'état sélectionné, qui communique le choix d'un utilisateur où ils ont sélectionné un, un élément de ligne, ou vous appelez cela un élément de liste aussi.

Et ici, nous avons un état activé, qui communique une surbrillance une destination, qu'elle soit initiée par l'utilisateur ou par défaut.

Et ici nous avons un état pressé qui communique un tap d'utilisateur.

Et vous pouvez voir un effet d'ondulation, qui est ce que ce cercle est appelé une ondulation, qui est créé quand vous utilisez quand vous appuyez sur un bouton ou un élément.

Et un état pressé, cela communique juste un clic ou un tap d'utilisateur.

Et ici nous avons un état glissé, qui communique quand un utilisateur appuie et déplace un élément.

Et nous avons aussi l'état on (activé), qui est typiquement utilisé pour les boutons, cases à cocher, et radios, ou interrupteurs, radios et cases à cocher, excusez-moi.

Et cet état on communique une bascule entre deux options, qui est et les deux options sont on et off.

Et off est l'autre état, qui communique juste une bascule entre deux options ici, vous pouvez voir que l'état off est indiqué dans l'interrupteur, radio et composant case à cocher.

Et aussi, nous avons des états d'erreur.

Et l'état d'air communique une erreur d'utilisateur ou de système, comme vous pouvez le voir, qui est indiqué avec la couleur rouge.

Et l'étiquette dans cette icône, cette icône informative et le soulignement rouge de ce champ de saisie de texte et aussi du texte d'aide pour indiquer l'air si un utilisateur a créé fait l'air ou le système avait créé une erreur.

Donc comment ces états sont-ils communiqués ? C'est une question importante.

Maintenant que nous avons passé en revue tous les types d'états, nous allons décomposer l'anatomie.

Donc les états dans Figma, sont communiqués par une superposition (overlay).

Donc vous pouvez voir ces états ici.

Et dans cette section, cela représente les états pour le contenu sur la surface sur la couleur de surface.

Et aussi les états hérités du contenu.

Et c'est essentiellement une superposition est juste une couverture semi-transparente sur un élément qui indique son état.

Et les superpositions fournissent une approche systématique pour visualiser les états en utilisant l'opacité.

Donc ici, vous pouvez voir que cet état utilise une superposition noire.

Et c'est l'état focus.

Et cela vous donne les superpositions, la valeur de base en pourcentage, l'opacité, et cela utilise la couleur noire ici pour cette superposition d'état focus pour le contenu sur la surface.

Et la structure de la superposition vit juste entre le conteneur, que vous pourriez juste penser comme la surface.

Donc ceci est la surface ici.

Et ensuite la superposition vit juste entre le contenu et le conteneur.

Donc cela commence avec le contenu étant au-dessus, et ensuite la superposition, qui est où l'état est représenté, qui est juste au milieu.

Et ensuite tout en bas est le conteneur sur lequel la Superposition et le contenu reposent.

Donc c'est important à noter.

Et cette même structure dans ce diagramme est appliquée à travers le reste de ces conteneurs.

Ici vous pouvez voir les états de conteneur de surface, que ce soit sur le contenu primaire, à quoi cet état ressemblerait, et à quoi cet état ressemble hérité du contenu, et ensuite la surface elle-même et à quoi cet état ressemblerait quand il est sélectionné.

Et vous remarquerez que dans l'état désactivé.

Malgré le conteneur de surface, qu'il soit sur la surface primaire, ou sur la surface générique, la surface blanche, vous remarquerez que le contenu, le contenu étant la typographie est l'état qui est réellement manipulé, pas les arrière-plans eux-mêmes dans l'état désactivé.

Donc dans pour cela, ce texte est réglé sur désactivé.

Et encore une fois, juste pour continuer à décomposer l'anatomie de la superposition qui représente l'état dans nos designs.

Cela fournit une approche systématique pour visualiser les états en utilisant l'opacité et peut être appliqué à un élément entier ou dans une forme circulaire.

Comme vous pouvez le voir ici, c'est appliqué dans la forme circulaire l'état lors d'être pressé, et la couleur de superposition correspond à la couleur du texte ou de l'icône sur l'élément auquel c'est appliqué.

Donc ici vous pouvez voir dans le troisième exemple que la liste radio qui est sélectionnée utilise la couleur primaire qui est réglée à un bleu violet et ensuite L'état associé avec, est un non utilise la même couleur, mais une valeur opaque opaque de cette couleur.

Et comme vous pouvez voir cela ici aussi dans Figma, où le calque d'état utilise la superposition primaire la couleur primaire comme une superposition, et utilise différentes opacités pour indiquer les états survolé focalisé pressé glissé et sélectionné de cette couleur.

Et vous pouvez voir que le dépendant du type de composant et d'état, donc dans cet élément de ligne, la case à cocher sélectionnée utilise la couleur primaire.

Et vous remarquerez que l'état sélectionné de cet élément de ligne utilise aussi cette couleur, mais une valeur opaque de cette couleur.

Donc c'est important à savoir.

Et vous remarquerez la même chose exacte dans cette case à cocher, où ceci utilise le le contour de la case à cocher elle-même et l'état activé est réglé à noir.

Et ensuite l'état de survol de cette case à cocher utilise une valeur opaque de noir.

Et vous pouvez voir cela ici dans Figma, où au survol cela utilise une superposition de 4%, qui est juste une superposition noire au survol, ce qui est ce que nous voyons ici dans cette case à cocher.

Ce qui est très important à noter, et seulement un calque d'état est appliqué à la fois.

Comme vous pouvez le voir ici, par exemple, si un élément est d'abord focalisé et ensuite survolé, le calque d'état de survol sera montré seulement jusqu'à ce que le survol soit complet, retournant ensuite au calque d'état de focus si l'élément est toujours focalisé.

Donc vous ne pouvez pas faire deux choses à la fois ou deux états à la fois.

Et avec cela étant dit, il y a aussi des valeurs d'opacité de superposition appliquées ici, que nous pouvons implémenter nous-mêmes dans Figma.

Donc je pourrais même refaire les surfaces, aller à Figma coller la capture d'écran.

Et avec la capture d'écran, je peux en fait recréer les états comme des calques ici, je peux aller de l'avant et créer un rectangle, par exemple.

Et je sais que l'état de survol utilise une la couleur noire réglée à 4% d'opacité, donc je peux aller de l'avant et appliquer la couleur noire, qui est une valeur hexadécimale de 0000, régler l'opacité de 4%.

Je peux alors transformer cela en un cadre et étiqueter cela l'état de survol l'état de survol sur surface.

Et ce rectangle représente exactement cela.

Peut-être que je peux dégrouper ce cadre en fait et appliquer ce nom au rectangle lui-même, nous avons cela nous pouvons ajouter du texte ici, juste taper hover, aller de l'avant et augmenter la taille de cela.

Et une fois que tout cela est fait, je peux aller de l'avant et en fait juste grouper cela dans un cadre.

Encore une fois, aligner verticalement ce texte et aller de l'avant et spécifier l'opacité et je pourrais spécifier la valeur hexadécimale aussi, juste pour que personne ne soit confus.

Donc les utilisateurs sauront que c'est un état de superposition état de survol, mais quelle est la couleur réelle d'abord, les designers devraient en fait cliquer sur le la forme rectangle pour comprendre la valeur hexadécimale et l'Opacité appliquée à celle-ci.

Ou nous pourrions le spécifier ici.

Et juste l'avoir étiqueté comme tel, si vous le souhaitez.

Et je vais aller de l'avant et étirer ceci.

Donc c'est un bon exemple.

Ici.

C'est un exemple de comment vous pourriez indiquer vos états, je peux aller de l'avant et même dupliquer ceci, changer cela à l'état focus et ensuite ajouter la Superposition de 12% et utilise la même couleur de noir encore.

Et ensuite il y a un état sélectionné.

Donc je peux même faire l'état sélectionné où le utilise la valeur de couleur sur primaire, la valeur de couleur primaire, mais je vais détacher ce style.

Et il utilise seulement 8% d'opacité de la valeur de couleur primaire comme vous pouvez le voir là.

Et je pourrais, je vais vouloir copier cela.

Coller cette valeur hexadécimale juste ici.

Et vous commencerez à voir que nous spécifions les états ici dans notre système, ce qui est Fantastique.

Et ensuite nous pouvons aller de l'avant et faire la même chose exacte pour l'état activé.

Donc vous commencez à voir comment nous créons exactement nos états pour nos composants ici dans Figma, ce qui est génial.

Non, vous mettre dans l'habitude.

Donc l'état activé, je peux aller de l'avant et changer l'opacité à 12%, teinte légèrement plus sombre.

Et je peux même aller de l'avant et représenter l'état pressé, qui est en fait un effet d'ondulation.

Donc ce que nous pouvons faire pour l'effet d'ondulation est juste de créer un cercle.

Donc sur l'état prostate, la couleur est juste réglée à, à blanc à 100% d'opacité.

Mais le, nous allons utiliser le, nous allons créer un cercle ici, une ellipse pour représenter, je vais mettre cela derrière la typographie ici et m'assurer que cela vit dans ce calque, je vais rogner le contenu pour que le cercle ne sorte pas des limites des cadres.

Il est caché, s'il dépasse les limites des cadres.

Et avec ce cercle, je vais juste aller de l'avant et changer cette couleur à noir, et ensuite régler l'opacité à 12%.

Et ici nous avons notre état pressé, ce qui est génial.

Et ensuite nous pouvons même faire un état glisser vers où l'état glissé utilise une superposition de 8%.

Tandis que les états focus et survol ont différents survol, utilisent une superposition de 4% dans le focus, utilisent une superposition de 12%.

Je vais aller de l'avant et créer cette superposition glissée, changer l'opacité à 8%.

Appuyer sur Entrée et est maintenant une teinte plus sombre.

Et je vais juste spécifier cela m'assurer que c'est précis dans le texte ici.

Et j'ai maintenant créé tous mes états.

Et la prochaine chose que vous voudrez faire est en fait de commande clics pour désélectionner et sélectionner le triangle avec l'état réel que vous essayez de créer.

Vous pouvez aller à l'icône de style et cliquer sur Créer un style.

Et ce que vous voudriez faire est de vous assurer que vous étiquetez correctement ceux-ci.

Et vous pouvez soit vérifier cette documentation s'assurer que vous créez le bon état.

Ou vous pouvez référencer comment j'ai déjà construit tous ces états.

Donc vous remarquerez que cela commence par states.

Et ensuite cela utilise la convention de nommage slash pour catégoriser ces états en conséquence.

Et il a ces ces états noirs étiquetés comme superposition noire.

Et ensuite il a ces états primaires qui sont violets, étiquetés comme superpositions primaires.

Et ensuite nous avons les superpositions blanches pour quand vous utilisez quand vous créez des états sur le dessus de pri sur le contenu primaire, qui utilise le fond violet.

Donc c'est important à noter, qui est où ces états de superposition blanche sont utilisés.

Et je vous recommande d'aller de l'avant et de construire le reste de ces états en exercice, je vais mettre cette vidéo en pause et les créer moi-même.

Et je vous mets au défi de les créer pour vous-même aussi.

Notez qu'il me manque l'état activé.

Donc allez-y et ajoutez cet état activé ici pour celui-ci.

Et ensuite pour le sur primaire aussi pour cette section, créant ceux-ci aussi.

Et mettre cette vidéo en pause et je vais les créer et je vous verrai quand j'aurai fini.

Donc maintenant que j'ai créé tous ces états pour quand vous êtes sur quand votre contenu est sur la surface sur primaire utilisant cette couleur ici de 62 double zéro double e x phi, qui est juste comme cette variante violette comme couleur de violet.

Et de toute façon, le fait est que vous remarquerez ce que je ce que j'ai fini par faire.

Si vous atteignez un résultat similaire finissez en fait par copier tout cela et ensuite les coller juste ici, j'ai ajouté un arrière-plan pour représenter à quoi cela ressemble sur la surface sur primaire.

Et une fois que j'ai fait cela, tout ce que j'avais à faire était en fait de changer ces valeurs à blanc et vous remarquerez quelques choses qui sont sont différentes dans le système quand il s'agit d'utiliser l'opacité pour les états sur la surface sur primaire par opposition à la surface sur a, qui est juste un fond blanc sur surface étant le fond blanc sur primaire utilisant cette couleur violette que les opacités sont beaucoup plus fortes quand il s'agit de l'état activé dans les états sur primaire pour activé impressionné et aussi l'état glissé vous remarquerez qu'il y a j'ai doublé ici et l'état glissé de 8% d'opacité à 16 utilisant une superposition de couleur blanche par opposition à une noire et est réglé à 32% ici Et 24% là, ce qui est quelque chose d'important à noter.

Et c'est à peu près tout, j'ai fini par créer ces styles de couleur ici, je vous mets au défi de créer ces styles de couleur en sélectionnant ces rectangles et en cliquant sur style, créer un style.

Et la convention de nommage, vous utiliserez un states et ensuite espace slash espace.

Et ensuite c'est une superposition blanche.

Et le le type de superposition blanche que c'est comme l'état focus.

Donc je pourrais juste frapper focus, frapper Créer un style, et j'ai créé le style d'état focus, je vais en fait faire un clic droit et supprimer ce style de mes styles locaux, qui apparaîtra tout en bas puisque c'est un nouveau style créé.

Et cela apparaît dans cet ordre basé sur quand il a été créé.

Clic droit et le supprimer, puisque je l'ai déjà.

Et encore une fois, vous avez ces styles à référencer je vous recommande d'aller dedans et de faire ceux-ci et ensuite de les créer au besoin.

Nous allons passer en revue la sélection, cela devrait être bref, nous allons principalement juste discuter et négliger des exemples du site web de material designs, parce que la sélection sera discutée lourdement une fois que nous commencerons à parler des états, qui est notre prochaine vidéo dans la portion interaction de la section fondation de ce cours.

Donc si nous allons de l'avant et cliquons sur dans notre fichier d'exercice sélection, c'est un lien auquel nous pouvons accéder.

Et essentiellement dans sélection, cela parle juste de comment cela se réfère à comment les utilisateurs indiquent des éléments spécifiques sur lesquels ils ont l'intention de prendre action.

Et quand ils prennent action sur un élément, il y a plusieurs façons de prendre une action sur un élément.

Et nous couvrirons cela profondément dans la portion états, qui est la prochaine vidéo dans ce cours, que vous regarderez ensuite.

Donc nous allons juste faire un bref aperçu maintenant.

Et vous remarquerez que beaucoup de cette documentation couvre l'interaction sur les appareils mobiles, mais nous allons spécifiquement parler de la portion bureau.

Mais je le ferai dans dans Figma quand nous développons quand nous créons nos composants.

Mais ici vous remarquerez que je touche aux deux parlant de sélection dans mobile et sur bureau.

Et je ferais très attention à la portion bureau, bien que la portion mobile soit tout aussi importante, sinon plus importante.

Et de toute façon, commençons.

Donc sur les appareils tactiles, sélectionner des éléments nécessite que vous fassiez soit une pression longue tactile sur votre appareil ou une touche à deux doigts.

Ou vous pouvez utiliser un raccourci de sélection si cela est disponible, tel que taper un avatar.

Et sur les éléments de bureau avec case à cocher.

les cases à cocher ne devraient pas afficher leurs cases à cocher par défaut, ou de façon permanente à moins que la sélection de l'élément soit l'activité principale dans l'UI.

Au lieu de cela, ces cases à cocher ne devraient être affichées qu'au survol comme une seule case à cocher pour cet élément, ou lors de la sélection du premier élément après quoi les cases à cocher sont affichées pour les éléments restants dans cet ensemble.

donc ici nous pouvons voir que l'utilisateur tape, et ensuite ils font une, ils tapent pour sélectionner un élément.

Comme vous pouvez le voir ici, ils sélectionnaient ce premier élément ici.

Et ils entraient dans un mode de sélection, où ils sélectionnaient un élément entrer en mode de sélection.

Et ensuite était alors tapé à nouveau pour sortir de ce mode.

Et voici quelques autres exemples aussi.

C'est juste l'utilisateur sélectionnant plusieurs cartes.

Et une fois que chaque élément est sélectionné, ils peuvent les taper pour basculer son état de sélection.

Donc l'utilisateur sélectionne toutes les cartes individuellement, une à la fois.

Et ensuite ils les sélectionnent à nouveau pour ensuite D sélectionner ces éléments.

Donc ce sont toutes des sélections.

Et ensuite c'est un autre exemple ici nous pouvons voir un autre exemple de sélection où les utilisateurs font une pression longue et glissent à travers plusieurs éléments pour sélectionner rapidement plusieurs éléments à la fois.

Et vous remarquerez qu'ils sélectionnent plusieurs éléments, parce que dans le coin supérieur gauche et la barre d'application, il met ensuite à jour la sélection alors que l'utilisateur utilise la sélection.

En faisant une pression longue et en glissant à travers plusieurs éléments, les éléments étant des photos, et cet exemple ici.

Donc c'est un excellent exemple.

Et ensuite sur bureau, ce qui est très important.

Il où vous verrez des variantes beaucoup plus compliquées d'états, vous verrez que l'utilisateur fait une sélection sur, et vous verrez qu'au survol, cela révélera cette case à cocher.

Donc il là maintenant D sélectionnant et vous remarquerez que quand l'utilisateur survole à nouveau, que l'élément révèle une case à cocher, et la case à cocher peut alors être cliquée et cliquée une fois de plus pour D sélectionner cette ligne, cet élément de ligne.

Et c'est très important à noter et nous pouvons aussi voir qu'il y a d'autres variantes de de ceci ici documentées.

C'est un article court et doux.

Je vous recommande fortement de lire tout cela juste brièvement Comprendre la sélection.

Aujourd'hui nous allons parler de comprendre la mise en page dans material design.

Et nous allons passer en revue quelques principes très simples que nous allons utiliser tout au long de l'intégralité de ce cours à l'avenir.

Et nous allons passer en revue quelques exemples et composants.

Et ici j'ai quelques liens.

Donc nous allons commencer par aller de l'avant et ouvrir ce lien, si vous souhaitez lire à travers les informations, ou vous pouvez juste suivre avec moi, j'ai déjà ces liens ouverts, et essentiellement material design afin de s'assurer de la cohérence à travers toutes les plateformes ou environnements, et tailles d'écran pour lesquels ils conçoivent, ils adhèrent à trois principes simples.

S'assurer que quand vous implémentez une mise en page qui est prévisible, cohérente et responsive à travers toutes ces plateformes.

Et ici, vous pouvez voir ces définitions.

Donc ils s'assurent qu'ils sont prévisibles en utilisant des mises en page intuitives et prévisibles avec des régions UI cohérentes et une organisation spatiale en utilisant ces mesures ici, et bien sûr des mises en page cohérentes, tout en utilisant les grilles, lignes clés, et le remplissage (padding).

Donc nous utiliserons lourdement les grilles, et le remplissage, bien sûr, et bien sûr, s'assurer que ces mises en page sont adaptatives.

Et elles réagissent à l'entrée d'un utilisateur, que ce soit un appareil, ou d'autres éléments d'écran.

Donc ici vous pouvez voir certaines des mesures de base, material utilise et les mises en page material lines sont visuellement équilibrées.

Et pour atteindre cet équilibre, la plupart de leurs mesures sont des composants quand ils sont conçus, s'alignent sur une grille de huit dip qui est appliquée, qui aligne à la fois l'espacement, et s'aligne sur la mise en page globale aussi.

Et de plus petits composants, tels que des icônes ou typographie peuvent s'aligner sur une grille de quatre dip.

Et aussi penser à cela comme quatre pixels.

Donc qu'est-ce que c'est exactement ? Donc si nous allons à Figma, nous pouvons aller de l'avant et construire un cadre, peut-être que nous voulons choisir une mise en page d'écran générique MacBook Pro, je choisis juste la mise en page d'écran macro pro pro, je vais aller de l'avant et ajouter une grille.

Et typiquement la plupart du contenu s'aligne sur une grille de huit pixels ou grille de huit dip.

Donc je peux faire cela en choisissant juste d'avoir ce type de grille ici pour ma grille de laboratoire et régler cette taille à huit.

Et c'est mon huit.

C'est ma grille de base grille ici réglée à huit dips, ou huit pixels vous pourriez dire.

Donc il y a un huit, voici votre grille de huit pixels ici, et vous pouvez commencer à concevoir votre quel que soit ce que c'est à la grille, ce qui est très essentiel.

Et nous utiliserons cela au besoin.

Et bien sûr, quand vous concevez plusieurs éléments, donc nous avons du texte ici, c'est de très bas niveau et pas précis, juste ceci est juste pour vous donner une idée générale, cette typographie de s'alignera bien sûr sur la grille ici.

Et ensuite je peux m'assurer de l'espacer de huit pixels, comme vous pouvez le voir ici.

Et ensuite si je duplique dans cet espace par huit pixels, et notez que quand vous concevez et vous décomposez l'espacement, et comme vous concevez des composants, ce sera toujours divisible par huit ou quatre.

Donc ici, nous avons quelques mesures ici commençant à zéro, et, et ensuite incrémentant par quatre dips à chaque fois.

Donc 04 812, jusqu'à 80.

Et le plus souvent, vous allez utiliser l'espacement ici en haut l'espacement supérieur, qui est soit réglé à 816 20 430-240-4856 647 à une annonce, et de temps en temps vous utiliserez probablement pour quand vous avez besoin d'appliquer un espacement plus serré à de plus petits composants tels que des icônes ou typographie.

Donc avec cela étant couvert, nous allons aller de l'avant et parler de ces mesures dans la dans la page suivante.

Mais juste avant cela, nous allons parler de la route de connexion responsive.

Donc la grille de mise en page responsive de mature designs est un guide global pour le placement des composants et éléments afin qu'ils s'adaptent aux tailles d'écran et orientation, assurant la cohérence à travers les mises en page.

Et les trois choses qu'ils implémentent dans leur grille de mise en page responsive est bien sûr, colonnes gouttières et marges.

Donc ici, vous pouvez voir que les marges sont à l'extrême droite et extrême gauche de l'écran dans cette dans cette couleur verte ici.

Et ensuite nous avons nos colonnes, qui sont cette teinte de rouge ici qui n'est pas rouge, je dois être daltonien, donc je m'excuse.

Et c'est notre étiquette de colonne là.

Et ensuite nos gouttières, bien sûr, est l'espacement entre les colonnes, qui sont sur l'extrême droite extrême gauche de l'écran, qui sont de la marge de cours.

Donc je vais en fait construire un exemple de cela dans Figma ici vraiment vite, donc nous avons cette grille de base de huit dip ici, donc je vais juste étiqueter ce cadre.

Donc nous avons la grille de base de huit dip, et ensuite je vais aller de l'avant et dupliquer cela.

C'est sur un Mac Book.

Écran Pro.

Et je vais aller de l'avant et créer une grille de mise en page responsive, je vais enlever ceci, je pourrais garder ceci si je voulais ajouter une autre grille de mise en page, et changer cela en colonnes.

Et ce que nous pouvons faire est de nous assurer que ce type de grille est réglé sur étirer parce que cela signifie que ce sera une grille de mise en page responsive ou vous pourriez appeler cela adaptatif.

Ou vous pourriez dire fluide.

C'est un autre terme courant.

Je vais ajouter 12 colonnes ici, ou nous pourrions vérifier combien de colonnes ont été implémentées dans cette grille 368 colonnes, quand on dirait qu'ils conçoivent potentiellement pour une tablette, ici nous avons une grilles, vous remarquerez que toutes les colonnes ici sont réglées sur lire.

Et je peux changer l'opacité de cela pour vraiment souligner cela.

Donc nous avons huit colonnes ici, mais nous n'avons pas en fait de marges encore ceci, ce que nous essayons d'atteindre ici est d'ajouter ces marges, qui sont étiquetées en vert ici.

Et nous réglerons cela à 24 pixels, nous avons le paramètre de marge et Figma là.

Donc j'ai réglé cela à 24 pixels.

Et vous remarquerez que cela a un peu écrasé ces colonnes dedans.

Donc j'ai écrasé ces colonnes dedans.

Et maintenant je vais changer cette gouttière du 20 pixels par défaut ou points à 16.

Parce que c'est couramment utilisé aussi.

Et cela s'aligne aussi parfaitement avec notre notre grille notre grille de base de huit pixels aussi.

Donc c'est un exemple de comment construire cela.

Mais maintenant, je vais en fait étirer l'écran parce que c'est responsive.

Donc vous remarquerez alors que je déplace ce cadre, essentiellement, les composants que vous concevez qui seront attachés sur l'écran, et adhérant à la mise en page de colonne ou la mise en page de grille sur l'écran seront aussi responsive alors que vous commencez à l'étirer.

Parce que comme vous le savez tous, nous avons des navigateurs web et nous pouvons les étirer et cela devient responsive Figma lui-même, l'outil est responsive, comme vous pouvez le voir.

Mais c'est un exemple là une grille de mise en page responsive.

Donc maintenant que nous avons cela spécifié, c'est fantastique.

Nous allons aller de l'avant et commencer à voir comment les mesures sont implémentées dans les composants.

Donc dans notre dans notre fichier d'exercice, si nous cliquons sur les composants de la barre d'application, nous pouvons aller de l'avant et ouvrir ce lien, qui ouvrira une page material design.

Et si vous allez de l'avant et me suivez et cliquez sur les spécifications ici dans la catégorie contenus, vous verrez que nous avons un tas de barres d'application inférieures, qui sont des composants mobiles uniquement.

Et ce qu'il faut retenir d'important de ceci est que nous voyons un tas de spécifications fournies sur comment concevoir ces éléments.

Donc ici vous pouvez voir que ce ce menu hamburger est enveloppé dans un cadre 24 par 24.

Et nous avons un bouton d'action flottant qui est réglé à 56 par 56, dips en largeur et hauteur, qui utilise l'élévation sur l'index Z pour s'élever au-dessus de cette barre d'application inférieure comme vous pouvez le voir ici, et ensuite vous pouvez voir l'espacement entre ces icônes aussi est tel 24 dips, et ensuite il a un peu de remplissage ou vous pourriez dire des marges à droite réglées à 16 dips.

Et la hauteur des de ces éléments, qui sont ces icônes sont centrées au sein de cette barre d'application inférieure.

Et la hauteur de cela est réglée à 24 dips.

Donc il y a quelques mesures là.

Et vous pouvez continuer à défiler vers le bas et voir d'autres variations de ce bouton d'action flottant.

Comme vous pouvez le voir ici, il y a d'autres variations avec plus de spécifications fournies ici.

Donc il y a huit dips entre ce bouton d'action flottant et l'espace blanc là à l'arrière-plan de la barre d'application inférieure.

Encore une fois, plus, notez que tout ceci est divisible par huit ou quatre.

Donc comprendre que ceci est tout très cohérent à un très bas niveau.

Donc tout commence à partir de la base.

Ou vous pourriez dire un niveau très primitif, comme ce sont des primitives, telles que des icônes, tout est divisible par huit ou quatre.

Et aussi l'espacement parmi tous ces éléments est divisible par huit ou quatre.

Et aussi bien que le dimensionnement d'autres composants qui sont superposés sur le dessus de cette barre d'application inférieure, ce qui est fantastique et une excellente source d'information pour vous à s'imprégner.

Et nous y arriverons très bientôt.

Et c'est tout ce que j'ai pour vous dans la compréhension des mises en page.

Nous allons parler de la densité de pixels.

Et ce que c'est exactement.

Donc nous allons avoir un aperçu de cela et ensuite comprendre la densité de pixels à travers différentes plateformes telles que iOS, Android, et pour le web.

Et ce que cela signifie pour chaque plateforme.

Et j'ai la ressource ici, nous pouvons cliquer sur ce lien et juste l'ouvrir.

Et une fois que vous l'avez ouvert, vous remarquerez qu'il vous emmène à la documentation de material designs.

Et nous allons juste lire à travers ceci et je vous expliquerai ceci et certains scénarios dans lesquels vous auriez besoin de comprendre ceci et aussi pour tous élargir vos horizons en tant que designer si vous ne comprenez pas déjà la densité de pixels.

Donc une fois que vous devez concevoir pour une plateforme spécifique, vous savez exactement comment communiquer des mesures, par exemple.

Donc disons, communiquer des mesures pour Android est complètement différent de communiquer des mesures pour des développeurs sur le web, vous savez, ou iOS, ou Android.

Donc comprendre comment faire des conversions, par exemple, vous pourriez avoir, disons, par exemple, je construisais un Splunk.

produit pour, qui est l'entreprise pour laquelle je travaillais, et ce produit a déjà été publié.

Et c'était une application expédiée pour iOS.

Et je, moi-même avais été un designer pour le web.

Et je n'étais pas conscient de comment traduire la densité de pixels du web à iOS à l'époque.

Et essentiellement, c'est un scénario où vous auriez besoin de comprendre ceci.

Donc je fournissais cet exemple.

Donc plongeons.

Et nous entrerons dans le reste plus tard.

Donc qu'est-ce que la densité de pixels de Hanks, la densité de pixels d'écran et la résolution varient selon la plateforme et la densité de pixels est juste le nombre de pixels qui tiennent dans un pouce est appelé densité de pixels.

Donc c'est les pixels par pouce.

Combien de pixels par pouce.

Donc vous avez peut-être vu, si vous avez imprimé du papier avant, ou imprimé quelques graphiques ou quelque chose, cela vous demande dans les paramètres avant d'imprimer de spécifier combien de pixels par pouce, vous voulez que cela soit imprimé à.

Donc plus le montant de pixels par pouce est bas, plus la densité est basse.

Et plus il y a de pixels par pouce, plus la densité est élevée, quand vous voyez cela imprimé, ou si quand vous voyez sur un affichage, et ils vous donnent ici dans cette documentation, une formule essentiellement sur comment calculer la densité de pixels.

Et c'est juste cette équation où votre densité d'écran égale la largeur ou hauteur d'écran en pixels divisée par la largeur ou hauteur d'écran en pouces.

Et si vous faites cela, vous obtiendrez votre densité de pixels.

Donc il y a un exemple ici visuellement, qui est un vraiment bon exemple où cet affichage à haute densité a plus de pixels par pouce que l'affichage à basse densité ici, et il zoome dessus.

Et vous remarquerez que vous cet élément UI, comme les dimensions de pixels apparaissent plus grandes sur les écrans à basse densité, et plus petites sur les écrans à haute densité.

Donc plus vous avez de pixels, plus cela apparaîtra petit sur les écrans à haute densité.

Et plus les dimensions de pixels sont basses, plus cela apparaîtra grand.

Donc avec cela étant dit, nous pouvons sauter sur parler de l'indépendance de densité, qui se réfère à l'affichage uniforme des éléments UI, sur des écrans avec différentes densités, et l'indépendance de densité.

Dans material design est communément prononcé comme dips, qui est l'abréviation dp ici écrit comme dp, et prononce Dips, ce sont des unités flexibles qui s'échelonnent pour avoir des dimensions uniformes sur n'importe quel écran.

Et elles peuvent fournir un moyen flexible d'accommoder un design à travers les plateformes.

Donc par exemple, Material Design ne conçoit pas seulement pour le web, mais aussi Android et iOS.

Donc ils utilisent cette terminologie dips, qui est leur façon d'avoir un langage commun en design et ingénierie pour accommoder les designs à travers plusieurs plateformes.

Et material, l'utilisation sage de l'UI de pixels indépendants de la densité, est d'afficher les éléments de manière cohérente à travers les écrans, avec différentes densités sur ces différentes plateformes.

Donc ici, vous pouvez voir un écran à basse densité affiché avec indépendance de densité ici, où la basse densité rend cela beaucoup plus apparent, où vous pouvez voir tous ces pixels ici, qui sont tous les carrés, c'est beaucoup plus apparent sur la basse densité.

Et c'est moins, c'est toujours apparent, mais c'est plus difficile de voir sur la haute densité, tous les carrés dus à l'écran à haute densité affiché.

Et nous maintenant nous pouvons commencer à parler de la densité de pixels sur un sur une base par plateforme où cette densité de pixels sur Android quand vous développez sur Android, ou concevez pour Android utilisez dips pour afficher les éléments uniformément sur des écrans avec différentes densités.

Donc c'est comme ça que vous le mesureriez.

Et un dip est, est égal à un pixel physique sur un écran avec une densité de 160.

Et essentiellement ce que cela et il y a l'équation ici, encore une fois, étant utilisée.

So essentiellement, un dip est un dip est un pixel.

Donc ne me laissez pas vous confondre.

Vous pourriez penser à cela aussi simple que cela.

Un dip est un pixel.

Mais les dips sont utilisés pour mesurer sur Android.

Donc c'est important à noter.

Et aussi les pixels échelonnables.

L'abréviation pour cela comme SP sert la même fonction que les pixels indépendants de la densité qui sont des dips.

Mais pour les polices, la valeur par défaut d'un pixel échelonnable est la même que la valeur par défaut pour un dip.

Mais pour les polices, la différence primaire entre un pixel échelonnable et un pixel indépendant de la densité est que les pixels d'échelle préservent le réglage de police d'un utilisateur, ce qui est super important.

les utilisateurs qui ont de plus grands paramètres de texte pour l'accessibilité verront les tailles de police correspondre à leurs préférences de taille de texte.

Et encore une fois, la densité de pixels sur iOS.

La plateforme basée sur iOS détermine la densité en utilisant la résolution logique, ce qui signifie qu'elle mesure juste ses unités en points par opposition aux pixels ou dips, elle utilise des points pour la mesure.

Et ici, avec leur résolution logique, les points sont échelonnés en utilisant un facteur d'échelle natif, qui est un peu de connaissance technique pour vous à comprendre si vous aimez, qui mappe juste à la résolution native d'un appareil.

Donc par exemple, si vous concevez pour l'iPhone x, vous concevriez pour une résolution logique de 375 points par 112 points.

Et quand c'est rendu les éléments sont traités par le matériel graphique.

Maintenant en utilisant cette fonctionnalité de facteur d'échelle natif pour remplir les dimensions de l'iPhone Xs, puisque l'écran est beaucoup plus grand.

Donc il a les capacités de comprendre ces points et de les échelonner en conséquence à l'appareil sur lequel il est affiché.

Et les unités, encore une fois, pour iOS utilisent des points, dont se souvenir et ensuite, bien sûr, la densité de pixels sur le web s'échelonne à la résolution d'écran des appareils, mais quand vous concevez pour le web, remplacez les dips par des pixels.

Donc vous pouvez quand vous concevez des produits sur le web, sauf spécification contraire, par disons des ingénieurs avec qui vous travaillez et ainsi de suite, vous pouvez juste mesurer les choses en pixels.

Nous allons passer en revue quelques méthodes d'espacement, une fois de plus dans material design, entendre comment ils abordent l'espacement, leurs éléments, et ils utilisent une terminologie qui est très utile que nous allons passer en revue dans la documentation.

Et dans notre fichier d'exercice ici, nous pouvons aller de l'avant et cliquer sur ce lien dans Figma, où nous aurons accès à l'ouverture de la page des méthodes d'espacement dans Figma.

Et nous allons passer en revue tout dans le contenu ici.

Et les méthodes d'espacement sont essentiellement juste l'utilisation de grilles de base, lignes clés, remplissage, et espacement incrémentiel pour ajuster certains ratios, conteneurs et cibles tactiles.

Beaucoup de cela est très important.

Je sais, cela pourrait être légèrement ennuyeux.

Mais c'est très, c'est une excellente ressource pour nous apprenant, non seulement l'espacement pour le système de design de materials, mais aussi appliquant cela à tout autre système que nous créons ou produits que nous arrivons à concevoir à l'avenir.

Et ici nous avons notre grille de base, où il discute juste comment tous les composants s'alignent sur une grille de base carrée de huit dip pour mobile tablette, et bureau.

Donc nous pouvons aller de l'avant et reproduire cela ici.

Donc ici, vous pouvez voir que le carré est huit par huit dips, ce qui est essentiellement juste huit par huit pixels.

Si vous deviez concevoir pour le web, et ici dans Figma, nous allons aller de l'avant et créer un écran qui est réglé à la taille d'un écran MacBook Pro.

Et je vais juste étiqueter ceci une grille de base dip.

Donc et ensuite je vais appliquer une grille de mise en page.

Donc et ensuite régler la taille à huit ici et j'ai maintenant une grille de base de huit dip que je peux toujours que je peux utiliser pour mesurer mes éléments ici sur ce cadre.

Donc c'est très important à noter.

Et c'est génial à avoir.

Donc c'est une traduction directe de comment c'est écrit dans la documentation, comment créer cela dans Figma.

Et nous avons aussi une grille de quatre dip, où cela est utilisé dans des zones plus denses telles que les icônes type, et quelques éléments avec des composants qui peuvent s'aligner sur une grille de quatre dip.

Et si nous voulions créer une grille de quatre dip, honnêtement, tout ce que nous avons à faire est de dupliquer celle-ci, je peux renommer cela en quatre dips.

Et ensuite à partir de là, j'aurais besoin de Oups, j'avais cela réglé à 18 qui devrait être à huit.

Donc maintenant que dit huit, mes excuses.

Et maintenant que c'est réglé à huit, je peux aller de l'avant et changer celui-ci à quatre.

Et maintenant nous avons une grille de base de quatre dip et la grille de base de huit dip.

Et les usages pour ceux pour ceux sont spécifiés ici.

Donc la typographie s'aligne sur la grille de base de quatre chiffres.

Et cette typographie peut être placée en dehors de la grille de quatre dip quand elle est centrée au sein d'un composant, tel qu'un bouton ou élément de liste.

Quand c'est placé en dehors de la grille, mais centré au sein d'un composant le texte peut toujours apparaître aligné au centre verticalement.

Comme dans ce scénario, vous pouvez voir cela aussi, c'est un aligné verticalement au centre de cet élément de liste juste ici.

Tout bien que le type soit placé en dehors de la grille de quatre dip, donc c'est quelque chose d'important à noter là.

Et ensuite nous allons parler de quelque terminologie que nous utiliserons fréquemment tout au long du cours quand nous construisons ces composants à partir de zéro.

Donc ils utilisent ces boutons comme exemples.

Donc les méthodes d'espacement sont plus granulaires que la grille de mise en page responsive, où c'est un ensemble de règles autour de comment placer des éléments au sein de mises en page et composants.

Donc le remplissage se réfère à l'espacement ici, entre les éléments au sein d'un composant.

Donc vous pouvez voir qu'il y a du remplissage à gauche et à droite sur cette icône, et il y a du remplissage à gauche et à droite de ce bouton à droite.

Et que et qu'il a un alignement qui est verticalement centré au sein de ce bouton, ce qui est exprimé dans cet exemple.

Et cet exemple de méthode d'espacement d'alignement où le bouton avec l'icône plus est aligné verticalement au centre au sein du composant bouton.

Et bien sûr, nous avons deux dimensions de maille, que nous passerons en revue très bientôt, où cela décrit la largeur et la hauteur des éléments du composant.

Donc nous saurons exactement comment dimensionner nos composants et les éléments en leur sein en conséquence, en utilisant les dimensions, et ensuite maintenant cela parle spécifiquement du remplissage, et comment cela se réfère à l'espace entre les éléments UI et comment c'est une méthode d'espacement alternative aux lignes clés et comme mesuré par incréments de huit dips, ou quatre.

Donc encore une fois, vous remarquerez que c'est toujours divisible par huit ou quatre.

Et le remplissage peut être mesuré à la fois verticalement et horizontalement, et n'a pas besoin de s'étendre sur toute la hauteur de la mise en page.

Et bien sûr, nous avons la dimension spécifiée ici pour le composant, la hauteur ici est réglée à huit comme vous pouvez le voir, et il vous donne les spécifications pour la hauteur de la barre d'application, qui est réglée à 56 dips, et ensuite la hauteur de la barre d'état est réglée à 24 dips.

Et bien sûr ces éléments de liste à 88 dips.

Donc c'est important de se référer à quand nous avons vraiment besoin de s'assurer que nos éléments sont parfaits au pixel près, ou dans ce cas densité indépendante pixel parfait.

Et ensuite, bien sûr, nous avons l'alignement, qui est le placement des éléments ici, cela vous donne juste des exemples d'éléments étant surlignés et discutant comment ils sont centrés.

Donc c'est génial.

Et ensuite nous avons aussi des lignes clés.

Et c'est un outil qui permet un placement cohérent des éléments en dehors d'une grille de mise en page.

Et ce sont des lignes verticales qui montrent où les éléments sont placés quand ils ne s'alignent pas à la grille les lignes clés vous aident à déterminer la distance entre les éléments depuis le bord de l'écran.

Et vous pouvez aussi mesurer par incréments de huit et ensuite aussi déplacer vous aide beaucoup dans Figma.

Donc si j'ouvre Figma, et je crée du texte ici.

Et une fois que j'ai ce texte créé, je peux aller de l'avant et même créer un rectangle.

Ici, si je maintiens Option, vous remarquerez que des lignes clés apparaissent.

Et je vois que c'est 240 pixels de distance à la gauche et ce texte.

Et je peux mesurer depuis les bords de l'écran.

Depuis le bord supérieur, la distance entre et le bord gauche et le bord inférieur et même le bord très loin à droite, ainsi que ce deux en maintenant juste Option.

Ou Alt sur Windows option sur Mac.

Et ce sont mes lignes clés qui m'aident à spécifier la distance entre les éléments.

Et nous allons utiliser cette touche de raccourci tout le temps que nous construisons des composants pour s'assurer qu'ils sont parfaits au pixel près.

Donc c'est ce que sont les lignes clés.

Et vous pouvez aussi utiliser des règles dans Figma.

Si j'appuie sur Shift+R, vous remarquerez que dans le canevas ceci, cet ensemble de règles apparaît et vous pouvez mesurer jusqu'à la distance entre les règles aussi.

Et vous pouvez créer une verticale ou horizontale en glissant juste depuis l'intérieur de la règle et sur le canevas.

Et vous pouvez mesurer la distance entre aussi longtemps que vous maintenez option survoler au-dessus de cette lecture cette ligne de règle ou lignes clés, nous pourrions l'appeler et vous pouvez les cacher en appuyant sur shift+R.

Et c'est comme ça que nous utiliserons les lignes clés.

Et ensuite nous parlerons de conteneurs et ratios.

Et essentiellement les conteneurs un terme qui se réfère à une zone fermée.

Et essentiellement les conteneurs sont composés d'éléments UI, tels que des images, icônes ou surfaces.

Donc ici nous avons un conteneur d'image.

Ici nous avons un conteneur d'icône et nous avons bien sûr un conteneur de surface, qui encapsule un bouton et les conteneurs peuvent Être rigides et restreindre la taille de, ou le recadrage des éléments en leur sein.

Donc vous pouvez utiliser des conteneurs pour recadrer des images si elles étaient dans un conteneur d'image, ou même un conteneur d'icône.

Mais que, mais c'est typiquement utilisé plus souvent avec des conteneurs d'image où vous aurez besoin de recadrer une image.

Mais ils peuvent être flexibles et grandir pour supporter la taille du contenu qu'il détient.

Comme vous pouvez le voir, dans ces exemples, nous avons un conteneur d'image rigide, et exemple numéro un, qui recadre la taille originale de l'image, ou nous avons un conteneur d'image flexible.

Et exemple numéro deux, qui détient la taille d'image originale alors qu'elle s'échelonne.

Et ensuite il y a quelques choses importantes à comprendre ici où nous avons parlé de ratios d'aspect où le ratio d'aspect est une proportion d'un élément, sa largeur à sa hauteur.

Et son ratio d'aspect est écrit comme telle largeur à hauteur.

Et pour maintenir la cohérence, et votre mise en page material design utilise un ensemble cohérent de ratios d'aspect sur des éléments comme images, surfaces et tailles d'écran.

Et il est recommandé pour nous d'utiliser cet ensemble de ratios d'aspect à travers notre UI.

Et vous pouvez les voir ici.

Donc vous pouvez voir quelques formats paysage où ce ratio est noté.

Et ensuite quelques quelques formats portrait aussi.

Et cela parle de ratios flexibles, qui est déterminé par la grille de mise en page, où la largeur de conteneur est déterminée par la mise en page d'écran et grandit pour remplir l'espace maximum disponible.

Donc cela se réfère juste à un écran responsive.

Et une hauteur de conteneur est déterminée par la hauteur de l'image dans le conteneur avec ces principes de ratio flexible, et vous pouvez utiliser un ratio flexible pour permettre au contenu de forme déterminer la hauteur du conteneur, ce qui est très courant.

Et une des choses les plus importantes à comprendre sont les cibles tactiles, et comment les cibles tactiles s'appliquent à tout appareil qui reçoit à la fois une entrée tactile et non tactile.

Et ceci est ces principes sont utilisés pour équilibrer la densité d'information et l'utilisabilité tout en un.

Et les cibles tactiles devraient au moins être une taille de 48 par 48 dips, ou 48 par 48 pixels avec au moins huit dips d'espace entre chaque cible.

Donc vous voyez que la dimension spécifiée ici.

Bien que voir ce conteneur d'icône est réglé à 40.

Par 40 dips, la cible tactile est réglée à 48 par 48 dips.

Donc c'est très important.

Et si vous deviez avoir un autre conteneur d'icône à côté ou tout ou un bouton, par exemple, il devrait au moins avoir un espacement de huit dips entre la cible, donc je peux aller de l'avant et faire cela.

Donc disons que j'avais une icône ici réglée à 40 par 40.

Je peux je peux spécifier cela je peux créer un cadre et ensuite maintenir option command pour échelonner cela à 48 par 48.

Et ensuite je peux centrer cela et vous remarquerez que je changerai l'arrière-plan ici à blanc, peut-être un petit rouge léger.

Et ce rouge réf références la cible tactile.

Et l'icône ici est ce cercle et la cible tactile réglée à 48 ou 48.

Mais l'icône elle-même est 40 par 40.

Donc ce sont les dimensions pour la cible tactile.

Et ensuite si vous deviez créer un autre élément à côté, vous auriez au moins à avoir un espacement de huit dips.

Donc c'est essentiellement ce que ceci référence ici.

Et vous pouvez voir que ce bouton a une hauteur de 36 dips, mais la hauteur des cibles tactiles est réglée à 48 tips.

Donc c'est très important.

Et vous pouvez voir dans le second exemple qu'il y a une icône réglée à 24 par 24 dips, mais la cible tactile est réglée à 48 par 48 dips.

Donc c'est un principe standard pour l'accessibilité, juste pour s'assurer que vous pouvez réellement taper ces éléments sur l'interface correctement, et adhère à non seulement équilibrer l'information sur votre écran et l'utilisabilité, surtout pour les utilisateurs handicapés, mais cela permet juste un design plus cohérent.

Aujourd'hui, nous allons passer en revue les mises en page de grille responsive dans material design.

Et nous allons les créer dans Figma et comme des styles afin que nous puissions systématiquement les réutiliser à travers tous nos designs au besoin et les implémenter dans notre système.

Donc ici vous pouvez voir que j'ai pris quelques captures d'écran du site web de material designs, qui référence tous les les points de rupture, donc il discute du système de point de rupture ici et aussi les points de rupture pour comment ils ont conçu pour les appareils iOS.

Et nous passerons en revue non seulement la création de Ces istyles et Figma.

Mais avant de sauter là-dedans, nous allons parler de quelques concepts clés et trucs à appliquer à notre modèle mental et créer des grilles et concevoir.

Et certaines de ces choses étant colonnes, marges et gouttières quand vous créez votre grille, que nous connaissons déjà et avons couvert.

Et nous passerons en revue cela, encore une fois, pour réitérer cela, et ingrainer cela dans votre cerveau, et aussi quelques façons de personnaliser la grille, que ce soit horizontalement ou verticalement, personnaliser sur la mise en page de grille sur ces accès, et discuter ce que vous pouvez et ne pouvez pas faire, ou au moins quelques bonnes meilleures pratiques et pratiques pas si bonnes.

Et ensuite bien sûr, créer les styles, comprendre le comportement de la grille, principalement les différences entre une mise en page de grille fixe et une mise en page de grille responsive, et ensuite discuter des régions UI.

Et ce que sont quelques exemples sur leur page web, et ensuite ce que sont les cadres blancs (white frames), donc nous pouvons aller de l'avant et cliquer sur cette ressource ici, ouvrir le lien, et cela ouvrira cette page de grille de mise en page responsive sur le site web de material designs.

Et essentiellement, cette grille de mise en page responsive permet à nos designs de s'adapter à plusieurs tailles d'écran et orientations, assurant la cohérence à travers toutes les mises en page.

Et le diagramme général décrit ce qu'une grille de mise en page responsive ou juste une mise en page de grille en général consiste en.

et cela consiste en colonnes, comme vous pouvez le voir ici, et gouttières qui sont qui est l'espacement entre les colonnes.

Et ensuite les marges, qui sont sur l'extrême gauche et extrême droite de l'écran disposées en vert ici.

Ce sont les marges.

Et cela parle en profondeur des colonnes, et comment le contenu est placé dans les zones de l'écran qui contenaient une colonne.

Donc vous remarquerez que généralement, quand vous concevez sur une mise en page de grille que vos designs ou vos composants, s'alignent sur ces colonnes.

Comme vous pouvez le voir, ici, cela s'aligne sur les bords gauche et droit de ces deux colonnes.

Donc cette, vous pourriez dire que cette carte prend deux colonnes, ainsi que celle à sa droite.

Et elle utilise cet espacement entre, et les gouttières pour fournir cet espacement cohérent.

Et donc les choses sont catégorisées de manière organisée.

Donc la largeur de colonne est définie en utilisant des pourcentages plutôt que des valeurs fixes, ce qui permet au contenu de s'adapter de manière flexible à n'importe quelle taille d'écran.

Donc vous remarquerez quand nous créons jusqu'à créer ces grilles ici dans Figma, elles vont être très responsive.

Et le nombre de colonnes affichées dans la grille est déterminé par la plage de point de rupture.

Et la plage de point de rupture ici est spécifiée.

Donc de zéro dips à 359 tips, ou vous pourriez appeler ceux-ci pixels si vous concevez pour le web.

Et vous pouvez voir que nous avons des plages tout le long pour les appareils mobiles ici tout le long jusqu'aux écrans massifs.

Et nous allons créer tout cela.

Et ici, nous allons créer toutes ces mises en page de grille iOS aussi.

Et c'est ça pour les colonnes, et voici quelques exemples sur mobile à un point de rupture de 360 dip utilisant une mise en page de grille de quatre colonnes ici, comme vous pouvez le voir quatre colonnes, Scott scoters, et marge spécifiés aussi.

Et vous pouvez voir que sur une tablette à un point de rupture de 600 dips de large, cela utilise une grille de mise en page de huit colonnes.

Donc alors que cet écran s'étend, il passe de quatre colonnes à huit colonnes, ce qui permet aussi à plus de contenu d'être implémenté sur cet écran.

Donc vous pouvez voir que cette rangée n'a que deux cartes.

Et ensuite quand s'étend à une taille d'écran plus large, qui est 600 dips dans cet exemple, il passe de deux cartes à quatre cartes sur cette rangée.

Et ici où il discute des gouttières, et ce sont les espaces entre les colonnes comme c'est surligné ici, et elles aident à séparer le contenu.

Et ces largeurs de gouttière sont des valeurs fixes à chaque point de rupture.

Et pour mieux s'adapter à la taille de l'écran.

la largeur de gouttière peut changer à différents points de rupture.

Donc des gouttières plus larges sont plus appropriées pour des écrans plus grands car elles créent plus d'espace blanc entre les colonnes.

Ainsi l'information sur l'écran n'est pas aussi n'est pas aussi dense et encombrée qu'elle peut l'être s'il n'y a pas assez de larges gouttières à de plus grandes tailles d'écran.

Donc ici vous pouvez voir sur un sur un appareil mobile au point de rupture de 360 dips.

Cette grille de mise en page utilise des gouttières de 16 dip et sur tablette sur le point de rupture 600 dips de large.

La grille de mise en page utilise des gouttières de 24 dip spécifiées ici, et elle utilise ces gouttières de 24 dip pour séparer le contenu.

Et maintenant nous pouvons discuter des marges, qui est un espace entre le contenu sur les bords gauche et droit de l'écran comme surligné en vert ici sur la gauche et la droite et ces largeurs de marge sont définies comme des valeurs fixes à chaque pause.

point.

Et cela vous permet de mieux vous adapter à l'écran et la largeur de marge peut changer à différents points de rupture.

Des marges plus larges sont plus appropriées pour des écrans plus grands car elles créent plus d'espace blanc autour du périmètre du contenu, comme vous pouvez le voir ici.

Donc voici un exemple de marges sur mobile sur un petit appareil utilisant une grille de mise en page de 16, marges de dip.

Et ensuite sur une tablette sur un lot légèrement plus grand appareil, le mobile, vous remarquerez que la marge augmente de 16 à 24, dips ici sur les marges gauche et droite.

Et maintenant nous pouvons aller de l'avant et parler de la personnalisation de la grille et des façons dont vous pouvez la personnaliser, ce qui vous permet de répondre aux besoins à la fois de votre produit et des différentes tailles d'appareil pour lesquelles vous concevez.

Donc parfois, vous pourriez avoir besoin de personnaliser les gouttières pour avoir plus d'espace entre le contenu pour créer plus de juste pour créer plus de cohérence.

Si l'espacement devient trop serré par moments, ou, ou s'il y a trop d'espacement, comme vous pouvez le voir ici, dans cette grille de labo, cela utilise des gouttières de huit dip ici, espacement très serré, l'espacement plus serré peut suggérer que les images sont étroitement liées les unes aux autres de sorte qu'elles sont perçues comme une partie d'une collection.

Et ici vous pouvez voir que cette grille de mise en page utilise des gouttières beaucoup plus larges réglées à 32 dips pour créer plus de séparation entre les colonnes.

Et cet espace supplémentaire aide l'album à être perçu comme des entités individuelles au sein d'une collection.

Et une chose que vous ne devriez pas faire qui est recommandée est de ne pas rendre les gouttières trop grandes, telles que la même largeur que les colonnes trop d'espace ne laisse pas assez de place pour le contenu et empêche qu'il apparaisse unifié, et cela semble juste bizarre.

Tout l'espacement est juste bien trop.

Et aussi vous pouvez personnaliser les marges, les marges peuvent être ajustées pour créer plus ou moins d'espace entre le contenu.

Et le bord de l'écran marges utilisent une valeur fixe pour chaque point de rupture.

Et cela donne un exemple de typographie texte ici, la longueur idéale pour la copie de corps est de 40 à 60 caractères par ligne.

Donc si vous allez au-delà de ce nombre de caractères par ligne, cela pourrait être une indication que vous devez ajouter plus de profondeur à vos marges, augmentant l'espace de marge.

Et ne rendez pas les marges si grandes qu'il n'y ait pas assez de place pour le contenu.

Donc vous devez trouver cet équilibre.

Donc voici un exemple sur mobile sur une taille de point de rupture mobile 64 marges de dip pour limiter la largeur et le contenu semble toujours proportionné, mais ne ne submerge pas l'utilisateur.

Tandis que ceci est très dense et mince, juste pas une bonne utilisation de l'espace blanc et trop d'espace dans les marges.

Cet exemple.

Et ici, nous pouvons parler aussi de l'utilisation de grilles horizontales où les grilles de mise en page Material Design peuvent être personnalisées pour les interfaces tactiles vous les yeux qui défilent horizontalement.

Donc si vous êtes par exemple, regardant à travers un album photo ou juste défilant sur un navigateur sur une tablette, ou appareil mobile, colonnes, gouttières et marges sont disposées de gauche à droite, plutôt que de haut en bas, quand vous créez une grille de mise en page horizontale.

Ici, vous pouvez voir que les marges sont en haut et en bas de la mise en page de grille horizontale, et les colonnes ici réglées à quatre colonnes avec une hauteur de 400 en profondeur 400 dips en hauteur, ce qui est génial, nous avons cela spécifié.

Et ensuite nous avons les gouttières aussi, ces mêmes principes juste une orientation différente.

Et les grilles horizontales peuvent être positionnées pour accommoder différentes hauteurs permettant de l'espace pour les barres d'application et autres régions UI ou autre contenu qui est fixe sur l'écran pour commencer.

Donc vous pouvez presser cela là-dedans.

Et maintenant que nous avons discuté de tout cela, nous allons parler de la construction de points de rupture dans Figma.

À la toute fin, quelques choses de plus à couvrir sont les régions UI.

Et essentiellement, les régions UI sont une mise en page, qui est faite de plusieurs régions UI telles que la navigation latérale qui est fixe.

Donc les régions UI sont typiquement du contenu fixe, comme la navigation latérale, la zone de contenu, et cette barre d'application.

Ces régions peuvent afficher des actions, du contenu ou des destinations de navigation.

Et ces régions UI devraient être cohérentes à travers les appareils.

Et vous remarquerez qu'il vous donne un exemple de cela alors qu'il s'échelonne vers le bas.

Donc cela commence comme une mise en page de bureau, et ensuite une mise en page de tablette, et ensuite une mise en page mobile, et cela parle de cela vous montre comment cela isole les régions UI alors que cela s'échelonne vers le bas, ce qui est très important pour augmenter la familiarité de comment cela est fait à travers les appareils alors que vous échelonnez vers le haut et le bas.

Quand vous concevez afin que vous puissiez vous assurer que vous vous adaptez correctement aux différents points de rupture ont différentes tailles d'écran.

Et, encore une fois, je toucherai à comment ces régions UI sont fixes.

Vous pouvez penser à elles comme des régions UI permanentes qui peuvent être affichées en dehors de la grille responsive aussi, comme le tiroir de navigation, où ces régions ne peuvent pas être effondrées.

Comme vous pouvez le voir ici, dans cet exemple ci-dessus.

Et ensuite nous avons des régions UI persistantes qui peuvent être affichées sur une commande telle qu'un menu hamburger où un menu glisse quand vous appuyez dessus, et elles peuvent rester visibles, ou elles peuvent être basculées on ou off pour apparaître disparaître.

Et quand elles apparaissent, elles condensent à la fois le contenu.

Elles condensent à la fois le contenu et la grille.

Donc vous remarquerez que cela condense cette grille une fois que cette région UI persistante est basculée on, l'utilisateur appuie dessus dans cet exemple, et ensuite le contenu est condensé.

Et qui adhère à la grille, ce qui est pourquoi le contenu est condensé.

Et ensuite il y a des régions UI temporaires, qui n'affectent pas la grille responsive.

Donc ceci est un exemple de superposition, quand c'est visible, elles peuvent être cachées en tapant un élément dans la région, ou tout espace en dehors de la région.

Donc cette région temporaire n'apparaît que temporairement et n'affecte pas la grille responsive.

Et ensuite nous avons ce concept de cadres blancs (white frames), qui sont des mises en page structurées qui fournissent une approche cohérente à la mise en page, et la superposition et les ombres.

Et c'est un excellent point de départ destiné à être modifié pour répondre aux besoins spécifiques d'un produit.

Donc par exemple, vous pourriez penser à cela comme un modèle.

Donc vous n'avez pas à concevoir toute la structure d'os nus d'un design, vous pouvez juste saisir un cadre blanc pour commencer.

Ou cela vous donne juste un vraiment bon départ pour concevoir votre produit, par opposition à construire tout cela à partir de zéro.

Donc ici vous pouvez voir un exemple mobile d'un cadre blanc, que vous pouvez penser comme un modèle, où vous pouvez alors aller et brancher ce dont vous avez besoin dans cette interface.

C'est déjà construit pour vous à partir de la structure d'os nus, et aussi un exemple de bureau de cela.

Donc maintenant avec tout cela étant dit, et permet beaucoup à couvrir, nous pouvons aller de l'avant et ouvrir Figma et commencer à créer ces ces styles de grille.

Donc nous pouvons commencer par, je peux saisir cette capture d'écran, et nous en ferons un couple ensemble.

Et ensuite le reste de cet exercice, vous implémenterez ceux-ci par vous-même aussi.

Donc ici nous avons le premier point de rupture, qui est réglé de zéro à 359, dips, je vais créer un cadre spécifier que la largeur est réglée à 359, ce qui est vraiment mince taille est réglée à portrait.

Et je ne me soucie pas vraiment de la hauteur maintenant, parce que c'est la nous développons juste la mise en page de grille pour cette largeur, pas la hauteur.

Donc je vais cliquer sur Créer un style ici, ce style de grille, cliquer sur cette icône de paramètres de grille de mise en page et changer cela en colonnes.

Et vous pouvez voir que c'est réglé à quatre colonnes.

Et les marges et gouttières sont réglées à 16.

Et ça va être responsive.

Donc je vais régler ce type à étirer (stretch).

Donc je vais régler la marge à 16.

Et notez que mes marges ont maintenant augmenté, il y a maintenant des marges, et ensuite changer les gouttières à 16 aussi ce qui épaissit les colonnes et resserre l'espacement entre le contenu quand nous l'alignons sur ce lab de grille.

Donc maintenant nous avons cette mise en page de grille pour cette plage de point de rupture.

Et je peux aller de l'avant et maintenant je peux en fait transformer cela en un style.

Donc avec ce groupe de laboratoire créé, je peux cliquer sur cette icône de style et cliquer sur le Créer un style.

Et ce que je peux faire est de spécifier que c'est une mise en page de grille extra petite (extra small).

Et je peux même spécifier extra small à zéro à 359 dip.

Et je peux même spécifier je peux catégoriser cela parce qu'ici vous pouvez voir que nous avons une gamme de tailles d'écran de extra small dans cette colonne à small à medium à large.

Donc je vais spécifier cela comme extra small x small est une convention de nommage slash pour catégoriser cela.

Et maintenant je peux aller de l'avant et nommer cela comme tel, donc maintenant c'est extra small, et c'est le premier point de rupture de zéro à 359 dips.

Ceci est ce à quoi la grille ressemblera je peux créer ce style.

Je peux même aller dans modifier et ajouter une description et discuter que ceci est utilisé pour les petits combinés (hands sets).

Et ouais, c'est toute l'information dont j'ai vraiment besoin pour communiquer aux designers qui ont besoin de comprendre à quoi sert cette mise en page de grille.

Donc maintenant j'ai cette mise en page de grille appliquée.

Maintenant je vais dupliquer ce cadre et enlever cette grille de mise en page et m'assurer que j'ai ceci réglé à 360 pixels ou donc je peux avoir un cadre n'importe quelle largeur, n'importe où de 360 à 399 dips.

Donc je peux même juste changer ceci de 359 à 360.

Et largeur, ou je peux juste l'augmenter à 399 peu importe tant que c'est dans cette plage.

Et parce que puisque c'est une mise en page fluide, cela maintiendra et calculera automatiquement les quatre colonnes entre cette plage de point de rupture d'appât et s'assurera que ces marges et gouttières sont réglées à 16 à tout moment, et aussi quatre colonnes pour cette plage de point de rupture.

Donc je peux aller de l'avant et créer un autre style de grille de mise en page, cliquer sur les paramètres de grille, spécifier la colonne, sélectionner les colonnes, m'assurer qu'il y en a quatre, je peux même changer la couleur de ceci, si je voulais, je pourrais changer cela en un bleu et m'assurer que le type est réglé sur étirer à 16.

pixels ou 16 dips à ma marge et gouttières et j'ai maintenant cela spécifié.

Et je peux aller de l'avant et fermer cela et créer ceci comme un autre style de grille sous la catégorie extra small en utilisant cette convention de nommage slash.

Et ensuite à partir de là, je vais aller de l'avant et spécifier la plage de point de rupture, qui est 360 à 399.

Et je vais écrire dp.

Donc les gens comprennent que c'est le format pour material design, qui est dips, densité pixels indépendants, je vais créer ce style, j'ai maintenant deux styles de grille ici.

Et je vais aller de l'avant et en créer un de plus avec vous.

Et ensuite je vais vous mettre au défi d'en faire un autre le reste par vous-même.

Donc je vais dupliquer ceci et détacher ce style, en créer un à partir de zéro, changer cela deux colonnes.

Et ici, j'ai besoin de spécifier la largeur n'importe où de 400 dips à forme 79.

Donc je vais juste sélectionner 479 lipsi 479 sur la largeur.

Maintenant que j'ai 479 spécifié, je vais cliquer sur mes paramètres de grille, et m'assurer qu'il y a quatre colonnes, changer la couleur de cette grille encore, à une autre teinte de bleu, juste parce que j'aime le bleu, et ensuite changer la marge de 16 et les gouttières à 16 aussi.

Et c'est réglé sur étirer.

Donc ce sera responsive.

Et maintenant je peux transformer cela en un style de grille, et spécifier que c'est un extra small, oups, style de grille extra small.

Et ensuite je peux spécifier la plage de point de rupture.

Donc c'est 400 dips à 479.

Et arrêt rapide, super.

Et je peux même aller de l'avant et ajouter une description.

Donc celui-ci est typiquement utilisé pour les grands combinés, signifiant grands appareils, grand combiné.

Et ensuite maintenant que j'ai cette description là, j'ai mes trois styles.

Et maintenant je vous mets au défi d'aller de l'avant et de faire le reste de ces styles ici de 480 dips vers le bas.

Et je vais faire mettre cette vidéo en pause et les faire moi-même.

Donc je reviendrai tout de suite.

Très bien, donc maintenant que j'ai créé tous les styles, vous pouvez comparer ce que vous avez créé avec moi, comparé aux styles de grille.

Ici, j'ai tout le format spécifié ici dans cette capture d'écran.

Et toutes ces plages de point de rupture sont clairement reflétées directement dans le fichier unique comme styles de grille, vous pouvez voir que tous ces points de rupture sont divisés par taille de fenêtre.

Donc nous avons quatre tailles de point de rupture extra small spécifiées comme tailles de grille avec les colonnes et marges appropriées.

Et bien sûr, ceci est déjà dans le fichier d'exercice pour vous à voir.

Et si vous ne les avez pas faits à partir de zéro, je recommande fortement que vous le fassiez c'est une excellente façon de pratiquer la construction de styles de grille.

Et je peux presque vous garantir qu'au moment où vous finissez de créer autant de styles de grille, vous saurez comment faire cela.

Et ce sera juste quelque chose de très, très simple pour vous à faire et vous avez cette compétence en tant que designer d'ici à ce que ce soit très utile.

Vous savez, c'est comme le dos de votre main.

Et comme vous pouvez le voir ici, j'ai tous ces styles tout le long jusqu'à la taille extra large souhaits pour tous points de rupture à la taille, la largeur de neuf 1920 pixels ou plus large.

Et nous avons tous ces exemples spécifiés ici dans ce fichier.

Et en exercice bonus, vous pouvez aller de l'avant et même créer tous les points de rupture iOS, si vous aimez, comme ceux-ci sont spécifiés ici.

Et un conseil est si vous créez un cadre, et vous allez aux cadres, vous avez toutes sortes de formats pour vos formats iPhone ici.

Donc vous pouvez juste sélectionner un format iPhone, et ensuite implémenter une grille de mise en page.

Et juste en sélectionnant votre mise en page de colonne, spécifiant combien de colonnes sont nécessaires, la majorité d'entre eux utilisent quatre colonnes pour la pour cette version compacte ici ou juste pour les trois premiers ensembles d'iPhones ou les premiers pour les deux.

En portrait et paysage, vous remarquerez que les orientations sont différentes.

Donc vous devriez probablement vous aurez besoin de créer une grille pour un paysage horizontal aussi.

Donc prenez cela en considération.

Comme vous construisez ceux-ci, je vous recommande de vous mettre au défi, et de faire cela et de créer ces styles aussi.

Donc vous pourriez même aller de l'avant et créer ce style de grille.

Et vous pouvez spécifier que c'est une mise en page de grille iOS en fournissant cette convention de nommage, là en utilisant le slash pour les catégoriser comme styles de grille pour le point de rupture iOS.

Et ensuite vous pouvez juste spécifier iPhone portrait.

Et vous avez maintenant ce style de grille variante iOS.

Donc si je vais et crée un cadre, et je vais à mes styles de grille, vous remarquerez que je les ai catégorisés, j'ai des grilles extra small avoir des styles de grille small, choisir parmi medium et grands, et extra large et bien sûr, un iOS.

Donc vous pouvez aller de l'avant et construire ceux-ci aussi, ce qui est très utile.

bon exercice pour vous.

Et vous remarquerez aussi certains d'entre vous peuvent question, Pourquoi faire autant de styles de grille.

Si, disons, par exemple, tous ces formats small extra small, utilisent tous la même quantité de colonnes et marges de tripes et gouttières.

C'est une excellente question.

Et puisque c'est une mise en page responsive, techniquement, vous n'avez même pas besoin de faire tous ces quatre, je faisais uniquement tous les quatre pour reproduire la précision de ce système de point de rupture dans ce tableau spécifié par material design.

Donc si vous voulez aller de l'avant et en fait consolider ceux-ci au montant minimum de styles de grille nécessaires, vous pouvez aller de l'avant et faire cela.

Et en réalité, vous n'auriez en fait besoin que de trois styles de grille, vous auriez besoin de l'extra small et du small.

En fait, vous aurez besoin de trois styles de grille.

Donc vous auriez besoin du style de grille qui est pour ces points de rupture pour ces quatre premiers points de rupture ici, ces extra smalls avec les quatre colonnes, et marge et gouttière réglées à 16 dips.

Et ensuite vous en auriez un deuxième pour le point de rupture small pour la petite tablette où le c'est réglé à huit colonnes et 16 marge et gouttières.

Et ensuite vous en avez un troisième réglé au point de rupture pour grandes tablettes où les colonnes sont huit.

Mais les marges de gouttières sont réglées à 24.

Et ensuite pour chaque autre appareil, vous auriez 12 colonnes et 24 dip marge et gouttières.

Donc essentiellement, vous n'avez que 1234 styles de grille, vous pourriez consolider ceux-ci, et même aller dedans et si vous les consolidiez, vous pourriez écrire une description pour quels points de rupture ils s'appliquaient, ce qui est aussi un excellent exercice, je recommande que vous fassiez cela aussi.

Aujourd'hui, nous allons construire toutes les variantes pour la barre d'application, spécifiquement la portion inférieure de la barre d'application, qui est où vous pouvez penser comme une navigation inférieure.

Et nous avons un lien vers la description de ceci.

Et c'est une carte inférieure, barre d'application, qui affiche la navigation et les actions clés au bas des écrans mobiles.

Et puisque vous avez pris le coup de construire réellement ceci avec moi, et même par vous-même, j'espère donc vous avez déjà cela en bas maintenant.

Ce serait génial.

Sinon, nous allons passer à travers cela.

Vous remarquerez que nous avons quatre variations de cette barre d'application.

Cette barre d'application inférieure, nous avons étiqueté comme il y en a une sans bouton d'action flottant.

C'est juste un tas d'icônes pour accéder aux différentes actions et nous avons les boutons d'action flottants centrés et vous remarquerez qu'il y a un peu d'espacement ici un espacement complexe là qui aidera à accommoder pour les nouveaux designs.

Vous Et ensuite nous avons aussi les boutons d'action flottants centrés sur la barre d'application inférieure et ces actions.

Donc ce que nous ferons est dans Figma, avoir toutes les captures d'écran, ce que nous allons faire est de créer celle-ci.

Et je vais vous mettre au défi de créer ces deux car c'est très simple.

Nous allons créer celle-ci, obtenir tout l'espacement juste, et ensuite je veux que vous, je vais mettre la vidéo en pause, construire celles-ci par moi-même, et ensuite vous faire construire celles-ci, mettez-vous au défi de comprendre les, les spécifications ici pour construire celles-ci.

Et ensuite nous passerons en revue cela.

Et ensuite nous allons construire la variante coupe centrale ensemble car cela pourrait être difficile.

Mais rien n'est trop difficile pour nous car nous serons des fig maestros une fois ce cours complet.

Alors commençons par spécifier la hauteur de l'arrière-plan pour ce centre, cette barre d'application, donc je vais aller de l'avant et maintenant que nous avons la hauteur de ceci, la largeur de l'appareil Android spécifiée, je peux aller de l'avant et changer la hauteur à 56.

Maintenant que nous avons cet ensemble de 56, je vais changer la couleur d'arrière-plan.

Une chose que nous devons faire ne pas oublier est d'activer notre bibliothèque de système de design material.

Et avec cela spécifié, aller à mes couleurs d'arrière-plan et sélectionner sur primaire.

Et nous avons besoin de nos icônes maintenant.

Donc si nous allons à notre panneau des actifs, nous pouvons soit les chercher ou taper hamburger, pas de résultats pour hamburger, c'est décevant.

Aller à notre système de design material, vérifier nos icônes, et nous pouvons les chercher.

Donc il y a l'icône dont j'ai besoin là, c'est appelé réorganiser apparemment, je peux aller de l'avant et cliquer sur ce cadre, appuyer sur Command+V et cela le collera, ce que nous devons faire est d'enlever ce remplissage, détacher le style, sélectionner l'icône de style et appliquer la bonne couleur, qui est contenu sur primaire.

Et ensuite je vais maintenir option A sur ceci une fois que j'ai cette icône sélectionnée, Option A l'alignera à gauche du cadre.

Et ensuite je vais appliquer l'espacement approprié, c'est réglé à 24 là.

Donc je vais juste déplacer ceci quelques fois.

Maintenant cet espacement réglé 24 centré.

Et je peux même juste dupliquer cette icône pour montrer lentement l'utilisation des espaces réservés.

Comme vous pouvez le voir, si je vais de l'avant, réglé cet ensemble à 16.

Je l'ai pas dupliqué à nouveau.

Et je m'assurerai que l'espacement est réglé à 16, encore, entre ces deux icônes.

Donc nous avons ceux réglés à huit à droite, que nous voulons régler à 16.

Donc je pousse ça.

Et nous sommes prêts à partir.

Nous avons notre subvention d'icône, si vous voulez être particulier par nos icônes, vous pouvez les chercher, nous pouvons les chercher aussi, dans cette bibliothèque, je vais mettre en pause ceci et trouver ces icônes pour vous très vite.

Si vous ne pouvez pas trouver d'icônes, vous pouvez soit chercher et l'outil d'icônes de design material pour l'icône.

Donc j'ai téléchargé toutes celles-ci individuellement comme svgs juste en cliquant dessus et ensuite en sélectionnant télécharger, mais je les ai déjà téléchargées pour vous et elles sont dans ce fichier d'exercice.

Donc nous pouvons en fait dans votre dossier, donc si vous allez à la section appropriée ou composants, donc 2.1, vous aurez cela qui sera accessible.

Et ce que nous pouvons faire est d'ouvrir notre finder et de glisser les trois de ces composants sur le canevas.

Et nous pouvons aller de l'avant et ajouter les composants appropriés maintenant.

Mais avant que je fasse cela, je vais changer ces couleurs, enlever ce remplissage là, aller aux couleurs de sélection, cliquer sur l'icône de style et régler celles-ci à contenu sur primaire.

Et nous serons prêts à partir.

Donc je peux aller de l'avant et en fait remplacer ces deux.

Donc ce que je peux faire est de glisser individuellement celles-ci dans le canevas shift clic sur ceci.

Et vous remarquerez qu'avec la fameuse sélection intelligente, je peux maintenir Option W et cela alignera ce calque en haut et ensuite je peux les échanger, ce qui est très utile.

Donc je n'ai pas à faire tout ce redimensionnement encore le.

Le redimensionnement est maintenu.

Je peux aller de l'avant et glisser ces deux Sous le canevas, et échanger individuellement ceux-ci aussi, je vais appuyer sur option w pour que l'espacement ne soit pas là, et ils s'alignent tous les deux sur cet axe.

Et ensuite je vais les changer, ensuite supprimer.

Et juste, je vais centrer celui-ci Shift, cliquer dessus, et ensuite je vais échanger ceux-ci.

Maintenant j'ai toutes les icônes désirées qui sont reflétées ici.

Et nous pouvons aller de l'avant et même tirer dans notre cou notre, notre bouton d'action flottant.

Et nous voulons le régulier, qui est celui-ci et c'est plus grand et la vignette, comme vous pouvez le voir, nous pouvons en fait aller de l'avant et glisser ceci sur notre canevas.

Et avec cela fait, ce que nous allons vouloir faire est de s'assurer qu'il est aligné, et c'est horizontalement centré ici.

Donc si nous le groupons dans notre cadre et, et ensuite ce que nous allons vouloir faire est de cliquer sur clip, décocher rogner le contenu, cliquer ceci et ensuite maintenir Option H.

Et cela centrera ceci parce que ce n'était pas centré option h maintenant centré.

Nous avons ces icônes correctement implémentées.

Et nous voulons que ces icônes aient des contraintes qui s'alignent à droite et centrent verticalement, parce qu'elles sont sur le côté droit de cette barre d'application inférieure.

Et je vais régler ceci à au lieu de gauche et haut gauche et centrer verticalement sur l'axe.

Ainsi, quand je redimensionne ceci, le dos les éléments sont, sont verticalement restant proportionnels en taille, avec l'arrière-plan, donc c'est tout équilibré, les icônes sont horizontalement, proportionnelles, le dimensionnement est là, et ensuite verticalement, cela restera proportionnel alors que cela s'échelonne en hauteur.

Et ensuite nous avons ce bouton d'action.

Les spécifications sont toutes bonnes, parce que nous avons déjà construit ce composant.

Et puisque c'est une partie de notre bibliothèque, nous utilisons juste le panneau des actifs et le glissons dedans construire le composant, ce qui est super pratique.

Et nous savons que c'est une partie de ce composant, parce que je clique en fait sur le calque parent, maintenant Command+Shift+H et cachant tout.

Donc tout ce qui se cache est associé au calque parent sélectionné, ce qui me laisse savoir que c'est une icône que je veux.

Je veux dire le composant que je veux et c'est calqué en conséquence.

Et encore une fois, celles-ci devraient toutes être en fait des icônes.

Donc ce que je peux faire est de copier celles-ci aller à mon système de design material, je peux les coller dans mon système au besoin.

Je suis et ensuite je peux juste appliquer cette couleur par défaut générique comme le remplissage, donc je peux taper gris 1.

Si vous aviez besoin de faire court, ceci devrait juste être réglé à cela.

Et ce à quoi j'essaie essentiellement d'arriver est de m'assurer que ce sont tous des composants principaux, individuellement, publiant cela dans cette bibliothèque, peut voir que j'ai ajouté ces trois nouvelles icônes cliquer sur publier, je les organiserai plus tard.

Et nous allons en fait échanger celles-ci.

Avec ces, ces composants, je vais vous montrer un truc ici.

Donc si je vais de l'avant et tape recherche, il y a mon icône de recherche.

Et si je maintiens, haut, si je vais de l'avant et fais de tous ceux-ci des composants, créer plusieurs composants.

Et je vais à mon panneau des actifs encore, glisse ceci Maintiens OPTION command, cela devrait l'échanger en place, mais ce n'est pas le cas.

Donc nous allons aller de l'avant et faire cela manuellement mes excuses.

Donc juste saisir toutes ces icônes ici.

Et ensuite une fois que nous avons tout, nous allons aller de l'avant et glisser celles-ci dans le canevas et faire la même opération exacte.

Une fois que celles-ci ont toutes été échangées, nous serions prêts à partir.

Ok, donc maintenant que tout cela est fait, juste appliquer les bonnes couleurs encore, régler le contenu sur surface et nous sommes prêts à partir.

Donc maintenant nous avons juste besoin de nommer ce calque en conséquence.

Il tombe sous la catégorie barres d'application.

Donc il y a quelques catégories ici barres d'application, espace slash espace et ensuite il tombe sous la catégorie inférieure de la barre d'application.

Et c'est la barre d'application avec un bouton d'action flottant, la barre d'application inférieure avec un bouton d'action flottant qui est centré.

Donc une fois que c'est fait, nous sommes prêts à partir, nous pouvons même appliquer des contraintes ici à droite.

Donc que cela reste toujours centré.

Ou en fait, nous voulons que cela se centre horizontalement.

Donc cela restera toujours centré quand nous étirons la largeur.

Donc maintenant nous avons la largeur qui s'étire, ce que nous devons faire est d'appliquer les contraintes à nouveau à droite et centrer verticalement, et ensuite gauche et centrer verticalement.

Donc maintenant, quand cet élément sélectionné, et il s'étire, il s'étire en conséquence.

Et généralement, la hauteur ne s'étirera pas, puisque nous avons ces spécifications réglées parfaitement ou correctement.

Et ensuite quand nous ajustons la largeur, tout contraint en conséquence, comme si c'était une mise en page responsive d'application.

Donc nous pouvons aller de l'avant et faire de cela un composant principal.

C'est prêt à partir.

Maintenant, je vais mettre cette vidéo en pause, et je vous mets au défi de faire ces deux composants ici, c'est en fait vraiment facile.

Ne les faites pas à partir de zéro, dupliquez juste ce calque, et détachez l'instance et ensuite commencez à enlever et ajouter ce qui est nécessaire pour ces deux variantes.

Et je reviendrai tout de suite.

Ok, donc maintenant que j'ai créé celles-ci, une quelques choses à souligner est que vous avez déjà ceci dans le fichier d'exercice, donc vous pouvez vérifier celles-ci et vous mettre à jour ou et juste faire attention aux contraintes.

Si vous le construisez à partir de zéro.

Notez que les contraintes de ce bouton d'action flottant en haut et à droite, donc il se déplacera en conséquence.

Et ensuite celles-ci sont réglées à gauche et centre verticalement sur cela, toutes ces icônes sur la gauche ici ces actions pour qu'elles soient contraintes proportionnellement.

Et ensuite nous avons la barre d'application inférieure sans bouton d'action flottant.

Et nous voudrons nous assurer que les contraintes sont réglées correctement.

Donc par exemple, si je clique sur cet ensemble d'icônes ici, et règle celles-ci à droite et centre, celles-ci s'échelonneront en conséquence, horizontalement et verticalement.

Ainsi que ce, ce menu ou actions de menu hamburger.

Donc ce sont les deux que j'espère que vous avez apprécié construire par vous-même.

Et le dernier mais non le moindre, nous allons aller de l'avant et construire la barre d'application inférieure avec un bouton d'action flottant qui a la coupe centrale.

Donc il a cette coupe ronde au milieu de l'arrière-plan.

Et c'est en fait vraiment facile à reproduire, tout ce que nous avons à faire est de créer une ellipse qui est réglée à 72 par 72.

Une fois que c'est une fois que vous spécifiez ces paramètres, assurez-vous qu'il a la bonne couleur d'arrière-plan, donc surfaces sur arrière-plan mais pas pour le contour oups, donc ça pour l'arrière-plan lui-même du remplissage.

Et ensuite ce que j'ai fait était que je me suis juste assuré que j'ai créé un rectangle approprié pour la couleur d'arrière-plan, qui était réglé à primaire.

Et j'ai réglé les dimensions appropriées à la largeur d'un appareil Android et la hauteur appropriée de cette barre d'application inférieure.

Et ce que j'ai fait était que je les ai juste groupés.

Et puisqu'ils sont groupés, et ceci est superposé au-dessus, ce que nous pouvons faire est d'utiliser la sélection soustraire.

Donc quand je clique sur soustraire, cela créera l'espacement approprié ici.

Et la raison pour laquelle cette ellipse est réglée à 72 est parce qu'elle fournit ce remplissage de huit pixels tout autour de cet espace blanc juste ici, l'espace de balayage est de huit pixels tout autour.

Et donc quand nous allons de l'avant et construisons ceci, maintenant j'ai cet arrière-plan.

Et j'ai déjà, ce que j'ai fait c'est que j'ai dupliqué ce composant ici et juste attaché, il a presque toutes les mêmes icônes, sauf pour le cœur, que nous échangerons plus tard.

Eh bien, je peux aller de l'avant et faire est d'enlever la facture et en fait ajouter un rectangle parce que nous avons la couleur d'arrière-plan appliquée au cadre.

Mais dans ce scénario, nous pouvons en fait appliquer cette sélection soustraire au cadre.

Donc ce que nous allons aller de l'avant et faire est d'ajouter ceci dans le calque parent.

Donc maintenant c'est une partie de ce cadre, je peux juste aller de l'avant et appuyer sur option A et W pour aligner option s Oups, j'ai besoin d'annuler très vite, j'ai besoin de sélectionner mon arrière-plan.

Centre, je vais laisser tout cet arrière-plan coupe centrale.

Et je vais maintenir Command+crochet gauche et cela poussera tout en bas et appuyer sur option s et option W et cela l'alignera en conséquence.

Et j'ai maintenant atteint le look désiré au besoin.

Et nous pouvons aller de l'avant et vérifier que réglé les pixels, ce qu'il est la largeur est réglée à huit.

Donc c'est génial.

Nous avons l'espacement approprié réglé tout autour.

Et c'est comme ça que nous créons notre coupe centrale action flottante avec le bouton d'action flottant pour notre barre d'application inférieure.

Et assurez-vous juste que tout ceci est groupé correctement, assurez-vous que cet espacement est correct.

Et nos contraintes sont appliquées correctement.

Et vous remarquerez que cet arrière-plan a maintenant besoin d'avoir des contraintes réglées correctement.

Donc si je vais de l'avant et étire ceci maintenant, cela maintiendra cet espacement.

Mais avec cette coupe centrale, ce sera beaucoup plus facile pour vous de communiquer en développement, ce qui se passe réellement avec cet arrière-plan.

Donc, c'est quelque chose d'important à noter.

Ce que nous pouvons faire est, puisque c'est une sélection, nous pouvons nous assurer que centré horizontalement et lisser ce rectangle mélange que cela s'étire à gauche et à droite à tout moment.

Donc maintenant, quand nous allons de l'avant et déplaçons ceci autour, cela se déplacera en fait en alignement avec le bouton d'action flottant, ce qui est génial.

Et maintenant que c'est fait, nous avons juste, tout ce que nous avons à faire est de nommer ceci correctement.

Donc renommer cela fab center cut, et faire de cela un composant principal.

Et nous sommes prêts à partir les gars, tout s'échelonne correctement, nous avons juste besoin d'ajouter cette icône cœur, nous pouvons aller de l'avant et vérifier cela pour voir si nous avons réellement cela bibliothèque interne, je ne l'ai pas.

Mais encore une fois, nous pouvons juste utiliser l'outil de design material, icônes, outil, material icons tool.

Et c'est aussi simple que de juste taper heart, je peux aller de l'avant et cliquer ça vous avez déjà ceci dans votre finder accessible.

Donc avec cela, je vais aller ouvrir Figma, ouvrir mon Finder.

Et nous avons ce favori, je vais ajouter ceci à ma bibliothèque d'icônes pourrait avoir mes icônes par ici.

Et j'organiserai cela plus tard avec ce favori, ils vont faire de cela un composant principal, publier.

Et en fait, puisque je n'ai pas, si je tape favorite, j'ai en fait déjà ceci dans la bibliothèque, mes excuses.

Donc j'ai l'icône favorite.

Je vais la glisser là-dedans, détacher le style, ajouter le nouveau sur surface, style de contenu contenu sur primaire, glisser ceci dans mon composant ici, m'assurer que c'est verticalement centré shift clic et vous sélection intelligente pour les échanger rapidement.

Et j'ai maintenant reproduit cette capture d'écran exacte.

Donc nous pouvons aller de l'avant et maintenant organiser tout cela.

Donc avec cela dit, je vais juste organiser tous ces composants et mettre cette vidéo en pause.

organisé tout je suis prêt à partir.

J'espère que vous avez apprécié regarder cette vidéo et comprendre davantage les contraintes et encore une fois, plus tard dans la section auto layout de ce cours, nous implémenterons réellement l'auto layout sur les composants au besoin.

Et je vous montrerai comment définir et comprendre cela.

Nous allons parler de comment construire les variantes de composant de barre d'application supérieure.

Donc nous aurons deux de celles-ci pour être précis.

Et si nous allons de l'avant et cliquons sur le fichier d'exercice ici, nous avons l'accès à la documentation si vous ouvrez ce lien, et une fois que vous ouvrez ce lien, et vous remarquerez que je suis déjà là.

Et ce à quoi cela sert est de fournir des actions de contenu liées à l'écran actuel, et aussi un excellent moment pour utiliser votre image de marque, actions de navigation titres d'écran, qui peuvent alors se transformer en une barre d'action contextuelle, qui est juste un autre ensemble d'actions.

Basé sur ce sur quoi vous interagissez dans cet écran.

Pan, il y a deux types de barres AP que nous allons créer.

Et nous n'allons pas construire celles-ci à partir de zéro, nous allons en fait référencer ce que nous avons déjà créé, qui sont les boutons de barre d'application inférieure.

Et nous pouvons aller de l'avant et terminer ce fichier d'exercice.

Si vous le sauvegardez, vous pouvez aller de l'avant et je publie ceci déjà.

Et si vous saisissez ce fichier d'exercice, vous devrez activer la bibliothèque de système de design material une fois de plus.

Et une fois que vous avez cela activé, nous pouvons aller de l'avant et juste chercher les barres d'application.

Et nous avons toutes les barres d'application.

Donc nous pouvons aller de l'avant et être un peu plus spécifiques sur quel type de barre d'application nous avons besoin.

Nous avons clairement besoin de la barre d'application inférieure sans boutons d'action flottants.

Et maintenant que nous avons ceci, nous avons tous les styles de couleur appropriés car cela nous met en avant je vais juste détacher ce style.

J'ai détaché cette instance Mes excuses je l'ai attachée depuis le composant principal.

Et ce que nous avons est un excellent point de départ.

Et nous avons le titre de la page ici.

Et nous avons toutes les spécifications.

Donc ce menu est réglé à 24 pixels à gauche, la hauteur de ceci est réglée à 56.

Et vous remarquerez qu'il y a aussi cette petite portion supérieure ce que ceci référence est la barre UI système et Nous n'aurons pas besoin de concevoir pour cela c'est uniquement un espace réservé dans cette capture d'écran.

Donc quand quand les ingénieurs construisent réellement ceci, ces composants seront juste alignés en haut, juste en dessous de la barre UI système.

Donc ignorez cela, ce qui est pourquoi les spécifications sont spécifiées ici 256, et ne prenant pas en considération la hauteur de la barre UI système, juste pour un peu de contexte là.

Et nous avons trois icônes ici, obtenu cette icône plus verticale, l'icône de recherche, cette icône Partager, je crois que c'est le titre, ce le titre de la page, et ensuite nous avons l'icône Menu.

Donc je peux aller de l'avant et supprimer cette quatrième icône parce que nous n'allons pas en avoir besoin.

Et je vais renommer ceci.

Pour ne pas être confus, parce que c'est un autre ensemble de barres d'application.

Mais au lieu d'être en bas, c'est en haut, et nous créons le régulier, nous allons juste étiqueter ceci régulier, car nous savons déjà que c'est la barre d'application supérieure régulière.

Et avec cela étant dit, nous devons aller de l'avant et saisir la prop le style de page, comprendre quel textile cela utilise, et nous allons juste taper page obscure moi, titre de page, ajouter le bon style.

Donc si je vais de l'avant et sélectionne en-têtes, nous avons variation d'en-têtes et sous-titres, et nous allons probablement devoir référencer la documentation, je vais aller de l'avant et cliquer sur le remplissage, appliquer la couleur de contenu sur primaire, m'assurer que le redimensionnement est réglé sur largeur automatique là, et aligner verticalement cela au canevas, je n'ai pas la bonne couleur, style, ou style de police.

Donc je vais référencer la documentation pour trouver cette taille de police exacte de la typographie ici pour gagner un Joe, obtenir une idée générale de ce que c'est, vous remarquerez si vous faites très attention est que cette typographie est plus petite.

Et dans cette barre d'application supérieure étendue variante, c'est un peu plus grand.

Donc avec cela étant dit, nous devons faire un peu d'espionnage.

Et nous l'avons, nous avons notre catégorie, la taille de police est réglée à h6 dans ce scénario.

Nous avons la typographie référencée à nouveau, déclarant que c'est réglé à h6, h6 juste là, il y a un tas d'exemples.

C'est encore, nous donnant l'exemple du h6.

Donc c'est très important.

Maintenant que nous avons cela nous pouvons aller de l'avant et juste nous avons ceci comme un style de couleur.

Donc je peux aller de l'avant et juste sélectionner cela, aller à nos textiles et sélectionner h6.

Donc nous avons notre h6 ici.

Et nous allons aller de l'avant et centrer ceci.

Et c'est réglé à 30 pixels à gauche de cette icône de barre de menu.

Donc maintenant c'est réglé à 32.

Et nous l'avons réglé à 16.

À gauche, je crois que c'est réglé à 24 actuellement, donc je vais shift clic sur le texte et le Je vais cliquer sur ce shift clic sur l'icône menu, déplacer ceci d'un, j'ai mon montant de coup de pouce et mes préférences réglées à huit sur le petit coup de pouce et un sur le grand coup de pouce.

Donc je peux juste déplacer rapidement les choses par incréments de huit efficace efficacement, car ce sont les principes de mesure de ce système de design material.

Donc maintenant j'ai ce titre de page réglé juste ici.

Et je vais juste me concentrer sur l'alignement ici, m'assurer que le remplissage à droite réglé à 16.

Et l'espacement entre les icônes est 24, ce qu'il est.

Donc si je vais de l'avant et vérifie que réglé à 24.

Et je sélectionne celles-ci c'est réglé à 16.

À droite, le remplissage, les contraintes sont prêtes à partir, je peux aller de l'avant et appliquer les contraintes appropriées à cette typographie en réglant l'axe vertical au centre.

Et cette icône a déjà gauche et centre.

Donc nous sommes prêts à partir.

Donc si je devais échelonner ceci, cela maintiendrait tout sa position ou alors que la hauteur augmente, cela maintiendrait cette position sur l'axe y.

Donc nous avons cette variante construite.

La seule chose manquante sont les bonnes icônes, que vous pouvez aller de l'avant et ajouter vous-même.

Je vais mettre en pause ceci et les ajouter.

Donc j'ai identifié toutes les bonnes icônes.

Et il me manquait une icône c'était l'icône partager qui tombe sous la catégorie actions.

Donc je suis juste allé à l'outil icônes de design material, tapé share et je l'ai trouvée et j'ai cliqué dessus sauvegardé comme un SVG, je vous ai épargné cette étape en donnant juste cela à vous dans les fichiers d'exercice.

Donc vous pouvez glisser cela dans votre canevas et Figma le publier dans votre bibliothèque de système de design material, ce qui est exactement ce que j'ai fait.

Je l'ai juste publié, ajouté ici fait de cela un composant principal, publié et une fois que je l'ai publié j'étais puisque j'ai cette bibliothèque activée dans ce fichier d'exercice, j'étais capable de le tirer du panneau des actifs ici, et ensuite je les ai juste échangés en conséquence.

Donc maintenant que toutes ces spécifications sont prêtes à partir, vous pourriez vérifier l'espacement et ainsi de suite si vous en aviez besoin et vous assurer que les contraintes sont réglées correctement.

Et maintenant nous pouvons aller de l'avant et juste vérifier notre calque, et c'est étiqueté correctement.

Et je vais faire de cela un composant principal.

Donc maintenant que c'est un oups, je vais sélectionner le cadre parent supérieur, et faire de cela un composant principal, nous avons maintenant notre composant principal.

Une fois que c'est là, nous pouvons aller de l'avant et même dupliquer ceci.

Et avec cela dupliqué, je vais le détacher.

Et nous allons spécifier la hauteur de cet élément pour être réglée à 128.

Mais avant que je fasse cela, je vais intentionnellement régler quelques contraintes.

Donc les contraintes vont être appliquées à toutes les icônes.

Donc je vais Command+clic sur toutes ces icônes, ce qui vous permet de cliquer celles-ci individuellement et de maintenir la sélection de l'icône précédente.

Donc j'ai toutes celles-ci sélectionnées, et je vais régler ceci à top (haut), parce que je ne veux pas que celles-ci bougent quand je règle la hauteur.

Et ce que je vais faire est de régler ceci à bottom (bas), et je vais shift clic sur cette contrainte pour l'enlever et m'assurer que le texte est réglé à bottom.

Donc ce qui va se passer est que, quand je change la hauteur de cet élément, les icônes collent au haut, et le texte collera au bas.

Donc je vais changer la hauteur à 128.

Et ça a fait exactement cela.

Donc maintenant que cela a été créé, ce que je veux faire est de m'assurer que l'espacement de la ligne de base est réglé en conséquence.

Et vous pouvez voir qu'ils spécifient la ligne de base du texte, qui est différente de la boîte englobante du texte, c'est réglé à 28 pixels.

Et nous pouvons facilement faire cela en appuyant sur shift r ajoutant une ligne rouge à la ligne de base de la typographie.

Et en maintenant, nous pouvons maintenir Option ici, nous pouvons cliquer sur le texte, c'est réglé à 16 ici, mais si nous allons de l'avant et créons une zone de texte nous remarquerons que la hauteur de ceci est réglée à 21.

Donc ce que nous devons aussi nous assurer est que nous utilisons le bon style de texte pour cette barre d'application supérieure étendue.

Donc comment faisons-nous cela, allons-y et référençons notre documentation sur la barre d'application supérieure.

Et vous remarquerez que la typographie a juste référencé que c'était un H6.

Si nous défilons vers le bas un peu plus, ce titre est un H6.

Mais qu'en est-il de la barre d'application supérieure étendue, c'est différent, c'est une police différente.

Donc nous pouvons aller de l'avant et Google top app bar text size.

Donc nous pouvons aller de l'avant et continuer à comprendre quelle est la taille de la typographie en faisant juste une recherche Google, si vous êtes jamais confus mais si non je vais en fait ouvrir cette page à nouveau, une fois que c'est ouvert, nous pourrions vouloir être capables d'accéder aux directives développeur et un peu espionner là-bas.

Et cela nous donnera accès au code.

Mais ce que nous voulons est l'accès à ceci ici.

Et comprendre la topographie.

Donc l'apparence du texte, et nous lisons juste quelques propriétés ici.

Et ce que nous voulons vraiment faire est de comprendre le textile appliqué.

Donc je vais mettre en pause ceci et chercher cette valeur.

Donc je n'ai pas été capable d'identifier le titre réel en en espionnant à travers cette typographie, ou au moins le code d'impression ici, ne soyez pas confus.

Encore une fois, cette pratique que je viens de traverser ce petit exercice de recherche d'un attribut spécifique est une pratique courante, je recommanderais pour vous de commencer à comprendre parce que cela vous aidera vraiment à essayer de disséquer et comprendre comment identifier certains éléments d'un design en passant par différents ensembles de documentation, ce qui est une excellente compétence à avoir, et améliorera votre implémentation du design alors que vous pouvez mieux l'articuler aux développeurs, ainsi que vous continuez à plonger plus profondément dans ces types de recherches Google et essayant de comprendre comment c'est implémenté.

Donc j'ai un peu juste référencé la documentation développeur et accédé à cette page de composant où cela parle de barres d'application supérieures.

Et je regarde un peu à travers la structure de ce code.

Donc androids écrit dans ce format appelé XML.

C'est le langage dans lequel ils écrivent leur ils écrivent leur code, ou pour l'UI implémentant implémentant leur UI.

Et je regarde la barre d'application supérieure proéminente.

Et avec cette barre d'application supérieure proéminente, je vais et défile vers le bas et j'ai trouvé un ensemble de propriétés qui ont été communiquées.

Et cela parle des attributs de titre qu'ils utilisent.

Donc je suis allé de l'avant et cherchais la barre d'application supérieure, tout ce qui est lié à l'attribut de barre d'application supérieure pour voir si je peux alors identifier la taille.

Donc il y a un tas d'autres paramètres ici aussi, qui sont communiqués.

Mais spécifiquement, nous cherchons les attributs de type titre.

Donc cela utilise un titre.

Et le titre de la barre d'outils material est réglé à un âge six, ce que nous avons spécifié.

Et ensuite le sous-titre material est réglé à sous-titre un, et ils ont aussi une variante de titre réduit.

Et ensuite ils ont aussi un titre étendu, comme vous pouvez le voir ici, mais nous allons aller de l'avant et juste maintenir le titre que nous avons actuellement.

Encore une fois, si vous savez quel est ce style, allez-y et affinez cela.

Donc je vais aller de l'avant et juste je vais changer cela en sous-titre puisque c'est celui que j'essayais d'identifier.

Et si nous allons de l'avant et nous assurons que la ligne de base est réglée à 28, nous devrions être prêts à partir.

Donc je vais augmenter ce rectangle à 28 pixels, pousser ceci légèrement vers le haut, pour que la ligne de base soit alignée maintenant.

Donc quand je fais mes lignes rouges, la ligne de base de la topographie est maintenant à 28 pixels du bas, ce qui est ce qui est spécifié dans la barre d'application supérieure étendue, juste ici, 28 pixels, cette ligne horizontale verte.

Donc maintenant nous sommes prêts à partir.

Et tout l'espacement est correct déjà sur les icônes au-dessus.

Et nous avons juste réglé des contraintes pour que cela reste ainsi.

Donc avec ce titre de page réglé là, je vais m'assurer que la contrainte réglée à gauche aussi.

Donc quand nous tapons un nouveau titre, nous sommes prêts à partir.

Et avec cela dit, je vais juste m'assurer que mon espacement est réglé à gauche est réglé en conséquence.

Donc c'est réglé à 72.

Nous sommes prêts à partir.

Et nous allons aller de l'avant et nommer ceci extended, parce que c'est notre variante de barre d'application supérieure étendue.

Et maintenant que toutes les contraintes sont réglées, et nous sommes prêts à partir long, je vais aller de l'avant et faire de cela un composant principal.

Et vous pouvez aller de l'avant et organiser cela dans ce cadre.

Et c'est comme ça que nous construisons les composants app our supérieurs.

Aujourd'hui, nous allons faire quelques composants backdrop (toile de fond).

Donc nous allons construire les composants backdrop en les survolant d'abord en les construisant en appliquant les contraintes appropriées, et vraiment devoir comprendre et consommer ces composants d'abord.

Donc si nous allons de l'avant et cliquons sur la documentation backdrop là, cela ouvrira dans votre navigateur par défaut.

Et un backdrop apparaît derrière toutes les autres surfaces dans une application affichant du contenu contextuel et actionnable.

Et une chose non actuellement, à la date de cet enregistrement, 10 septembre 2020, jeudi, c'est actuellement en bêta.

Par conséquent, pour les développeurs référençant ceci.

Actuellement, il n'y a pas de statut autour de quand ceci sera développé pour les plateformes suivantes Android, iOS web et le cadre flutter.

Donc c'est important à noter.

Et aussi, le backdrop est composé de deux surfaces, n'est-ce pas, donc nous avons le calque arrière, qui est le le calque bleu là, n'est-ce pas ici, cet élément de barre supérieure, qui est ce à quoi cela ressemble essentiellement et ensuite le calque avant, qui est celui qui a ce fond blanc et utilise un peu d'élévation, que vous puissiez le voir ou non.

Et le calque arrière affiche des actions et un contexte et ceux-ci contrôlent et informent le contenu des calques avant.

Donc tout ce qui est sur l'arrière-plan dicte le contenu des calques avant.

Et c'est important à noter là.

Et cela utilise aussi un diviseur optionnel sous le sous-titre juste là alors que nous continuons à analyser ce composant backdrop.

Et voici la décomposition de l'anatomie de ce composant backdrop.

Il consiste en un calque arrière, le calque avant, et un sous-en-tête et diviseur optionnel là comme vous pouvez le voir, et soit le calque arrière ou le calque avant peut être actif à la fois.

Donc seulement une chose peut être active, soit le calque arrière ou le calque avant.

Et quand le calque arrière est actif, ce ce calque avant descend, utilisant le mouvement.

Donc ici vous pouvez voir que c'est une zone fixe, ou au moins, c'est une façon optionnelle d'utiliser le sous-en-tête comme une zone fixe avec du contenu à travers lequel défiler et ainsi de suite.

Et je recommande fortement de parcourir le reste de ceci et de lire et comprendre le comportement.

Juste ici.

Vous pouvez voir que le calque avant, comme le calque arrière repose juste sur la surface et le calque avant, utiliser l'élévation, c'est un dip sur l'index Z.

un pixel sur l'index Z est aussi une autre façon de le référencer sur le web.

Donc c'est important à noter pour notre calque avant là.

Et j'ai déjà saisi ces captures d'écran pour ce que, pour concevoir les spécifications ici, et vous remarquerez qu'il utilise quelques éléments de liste dans cet exemple, que nous allons aller de l'avant et un peu construire.

Donc ce que nous pouvons faire est d'aller dans Figma ici, ce que ces captures d'écran référencent, nous, nous allons aller de l'avant et créer cet exemple générique.

D'accord, donc nous avons est, nous pouvons chercher la barre d'application dans notre système, assurez-vous que votre bibliothèque est activée la bibliothèque de système de design material, et ensuite vous pouvez chercher la barre d'application, et nous avons toutes ces variantes, n'est-ce pas ? Donc la variante que nous allons vouloir utiliser est plus que probablement celle-ci avec titre de page, et vous voyez qu'elle a ces autres actions aussi.

Et ce que je voulais en fait faire est de placer ceci sur un cadre parent, et ce cadre parent va être utiliser les dimensions du téléphone Android.

Donc et je vais renommer ceci Android phone.

Donc je vais aller de l'avant et glisser ceci ici et aligner ceci au haut et à gauche du cadre parent.

Donc super, nous avons ce dont nous avons besoin pour commencer.

Et cela indique aussi que l'arrière-plan est réglé sur bleu encore, donc ce que nous pouvons faire est d'ajouter une couleur d'arrière-plan primaire pour représenter cela dans notre exemple.

Et Android, Android phone backdrop, je vais juste renommer cela très vite pour être précis.

Et ce que nous pouvons faire est que ce backdrop apparaît tout en haut de ce, ce cadre ici.

Donc je vais aller de l'avant et ajouter une règle ici dans Figma.

qui s'aligne avec cette sélection ici.

Obtenir cela parfait au pixel là.

Et maintenant avec cette règle spécifiée, je peux aller de l'avant et créer un autre cadre.

Et dans ce cadre, va régler la largeur à je vais régler ceci à surfaces surface, la couleur d'arrière-plan et la largeur pour s'étendre sur tout le corps de l'écran, qui est 360 dips, je vais aligner ceci au haut.

Et je vais aller de l'avant et sélectionner des coins indépendants et m'assurer que le haut et la gauche sont réglés à 16 pixels arrondis.

Donc nous atteignons ce même look ici, comme vous pouvez le voir, juste là, et il utilise un sous-titre qui a une ligne de base de 32 dips depuis depuis le haut du calque avant.

Donc je vais étiqueter ce calque, ce cadre front layer (calque avant), parce que c'est l'arrière-plan et il va y avoir du texte qui vit en son sein.

Et je vais m'assurer que j'ai le textile approprié spécifié et c'est sub title (sous-titre).

Et je vais m'assurer que le redimensionnement est réglé à largeur automatique.

Pour garder cela clair et concis, je peux aligner cela au haut et à gauche à 16 pixels 16 dips à gauche.

Et je peux pousser ceci vers le bas.

Et ce que je veux faire est de m'assurer que la ligne de base est réglée à 32 chiffres juste là.

Donc je peux aller de l'avant et faire est de saisir, oups, saisir un rectangle, saisir un rectangle, spécifier 32 bouts là.

Et ensuite je vais pousser ce contenu vers le haut pour qu'il s'aligne les lignes de base alignées.

Et je peux justifier cela double vérifier avec une règle.

Et nous sommes prêts à partir.

Cette ligne de base est là.

Et une chose que cela utilise optionnellement est un diviseur.

Donc nous allons aller de l'avant et ajouter cela dès le départ.

Je vais aller de l'avant et cherché diviseur dans mes actifs.

Et ensuite je peux aller de l'avant et tirer ce diviseur de mon système.

Et le diviseur est approximativement 12 pixels 12 dips vers le bas depuis le sous-titre.

Et ce que je vais vouloir faire est que je maintiens option command et rétrécis ceci pour que ce soit réglé à a un remplissage de 16 dips à gauche et à droite de cet autre sous-en-tête qui est reflété dans dans nos exemples ci-dessus, comme vous pouvez le voir ici.

il s'aligne juste là, ce diviseur.

Donc c'est génial que ce soit cohérent.

Donc maintenant nous avons cela et nos textiles attachés.

Et tout semble bon.

Nous sommes prêts à partir.

Nous pouvons faire maintenant est juste spécifier ceci comme notre mise en page d'os nus parce que les designers iront alors de l'avant et ajouteront dans le réel Les éléments nécessaires à ce composant.

Donc nous avons ce ce calque avant ici, si je vais de l'avant et rétrécis ce calque avant étendu, et nous avons maintenant un canevas pour le designer commencer à ajouter du contenu dessus.

Donc c'est super important à noter.

Donc ceci en soi pourrait être son tout propre composant, ce que je vais faire est de m'assurer que ce style de couleur spécifié à actif avec notre haute emphase, aussi connu comme haute emphase, et s'assurer qu'il a l'élévation appropriée réglée à un dip.

Donc nous pouvons voir légèrement cette élévation être utilisée maintenant.

Et avec ceci, je vais aller de l'avant et faire de cela un composant principal car c'est une variation que les designers pourraient utiliser cette mise en page d'os nus, la copier, et ensuite commencer à ajouter leurs propres éléments par-dessus, je peux aller de l'avant et spécifier les contraintes parce que maintenant quand je l'étire, cela ne colle pas nécessairement correctement, c'est toujours agréable de spécifier cela.

Donc j'ai pu régler les contraintes gauche et droite, donc maintenant quand j'étire ceci, cela s'étirera correctement, le diviseur c'est-à-dire, donc maintenant nous avons notre calque avant étendu, et vous pouvez un peu voir l'élévation être utilisée ici.

Une chose qui pourrait être un peu confuse au début, créer ce calque avant qui est étendu est que c'est un canevas vierge, n'est-ce pas, donc quand un designer va dedans et l'utilise, je vais aligner ceci ici.

Donc quand un designer va et utilise ceci, cela pourrait être un peu trompeur au début.

Donc parce que ce qu'un designer va avoir besoin de faire est de copier ceci.

Oups, je vais un peu d'un échange, j'ai mis l'instance ici.

Mais c'est bon.

Nous pouvons faire est d'aller de l'avant et déplacer ce maître maintenant vers ce cadre, front layer expanded (calque avant étendu).

Donc c'est, donc avec cela étendu, nous pouvons aller de l'avant et créer la variante dissimulée (concealed).

Et ce à quoi j'essayais d'arriver au début est que les designers copieront cela, copieront ce sous-titre, et iront de l'avant et ajouteront d'autres éléments dessus.

Donc par exemple, les éléments de liste que nous avons créés dans la dernière vidéo, je peux aller de l'avant, peut-être que je veux ajouter dans ce composant, n'est-ce pas, j'ai juste besoin de m'assurer que l'espacement approprié est spécifié.

Donc ce que je veux faire est, je vais devoir envelopper ceci dans un cadre, n'est-ce pas.

Donc ça va être mon front front layer, expanded with content (calque avant étendu avec contenu), donc vous allez devoir l'envelopper dans un cadre, s'assurer que tout s'aligne en conséquence.

Et je vais étirer ceci pour couvrir toute la largeur de ceci.

Et ensuite ce que vous pouvez faire est, alors juste continuer à dupliquer ces éléments au besoin.

Donc c'est génial, et s'assurer que clip content (rogner le contenu) est spécifié.

Et avec clip content spécifié, vous avez maintenant un exemple avec contenu, assurez-vous juste que le remplissage approprié est réglé au haut là.

Donc nous pouvons aller de l'avant et vérifier cela pour voir ce que ce remplissage spécifié à juste ici de cette liste au haut de ce diviseur.

Et ce que nous pouvons faire est de toujours référencer nos spécifications.

Donc avec nos spécifications référencées, on dirait qu'il y a un peu d'espacement ici.

Ce n'est pas nécessairement spécifié.

Mais nous pouvons aller de l'avant et l'estimer à l'œil semble être 24 pixels là.

Et avec cela, nous pouvons aller de l'avant et nous assurer que c'est réglé à 24, ce qui l'est presque entièrement, j'aurai juste besoin de déplacer ce contenu vers le bas d'un pixel de plus.

Et nous devrions être prêts à partir.

Là.

Et nous avons notre exemple.

Donc comme vous pouvez le voir, si nous regardons ce cadre, il enveloppe le calque avant, qui est l'arrière-plan avec tous ces éléments de liste ajoutés par-dessus.

Comme il peut y avoir plusieurs scénarios et comment vous voulez utiliser le le calque avant étendu, vous pourriez vouloir ajouter un autre type de contenu sur ce calque avant étendu sur ce backdrop.

Donc nous vous donnerons la mise en page d'os nus et vous donnerons la liberté d'ajouter des choses par-dessus.

Et vous pouvez juste faire cela en groupant et comme un cadre de ce contenu.

Et nous allons aller de l'avant et aller vérifier la la version dissimulée et la version dissimulée se réfère à ce, ce calque avant étant maintenant minimisé, ce qui est ce que je veux dire par dissimulé Material Design appelle cela concealed (dissimulé) et le tout Ceci est réglé à, voyons 48.

Donc la hauteur réglée à 48, nous pouvons aller de l'avant et spécifier cela ici et aligner cela au bas, nous avons maintenant cela réglé à 48.

Et j'utilise toujours la même version que je viens de dépouiller.

Donc je vais faire est de détacher ceci et étiqueter ceci front layer concealed (calque avant dissimulé).

Enlever cette contrainte supérieure, régler cela à bas gauche et droite.

Donc ça s'étire respectivement.

Et il n'y aura pas besoin de diviseur dans ce dans cette version, ce qu'il devra y avoir est une action, qui est ce chevron et j'en ai un ici, la flèche haut, flèche clavier haut, donc je vais sélectionner cela coller et sûr que c'est centré ici centré.

Et nous avons le remplissage réglé à 16 dips à droite, donc nous sommes prêts à partir, nous avons maintenant notre variante de calque avant dissimulé, je vais aller de l'avant et faire de cela un composant principal.

Et dupliquer ceci, saisir le composant principal et le glisser dans notre notre canevas là.

Et cela utilise toujours l'élévation d'un dip.

Donc c'est important à noter.

Et nous pouvons même le jeter dedans comme c'est, comme vous pouvez le voir, c'est maintenant un exemple ici.

Et ce que nous n'avons pas spécifié ici est le contenu pour ceci.

Donc je renomme juste cela.

Et essentiellement ce que vous pourriez faire est de créer ajouter tout contenu dont vous avez besoin ici.

Donc quand ceci est dissimulé, là le backdrop, les calques arrière étant utilisés.

Donc si nous allons de l'avant et faisons attention à la documentation Material Design encore.

Et nous regardons l'anatomie de ce backdrop, il a ce calque arrière, n'est-ce pas.

Et le backdrop a a les actions originales.

Et le calque avant a des actions respectives aux actions sur ce calque arrière.

Donc nous allons nous pouvons aller de l'avant et faire des exemples ici.

Donc nous pouvons aller de l'avant et créer ces éléments de liste je peux, je vais aller de l'avant et tirer.

Je vais aller de l'avant et changer.

Voyons cela à app name (nom de l'app).

Et je vais cacher ces icônes ici.

Et je peux même aller de l'avant et échanger cette icône en un X.

Donc je pourrais trouver cette icône de sortie.

Ou mieux encore, c'est probablement étiqueté close (fermer).

Ici nous avons cette icône close.

Et nous voulons double vérifier pour voir si nous avons réellement cela ici, ce que nous avons.

Donc c'est en fait appelé clear.

Donc je vais chercher clear ici, ma bibliothèque material design.

Et je vais glisser ceci ici et maintenir Option command et survoler cette icône et cela l'échangera.

Et je changerai cela à la la couleur active sur primaire, puisque c'est sur la surface primaire là.

Et nous sommes prêts à partir pour enlever ce remplissage caché ou éteint.

Donc nous avons cela spécifié.

Et ce que nous voulons aller de l'avant et faire maintenant est que nous pouvons apporter quelques quelques éléments de liste ici, nous pouvons apporter l'élément de liste que nous avons créé qui utilise une icône, cette variante d'une ligne, n'est-ce pas.

Et ce que nous pouvons même faire est d'enlever l'arrière-plan, nous pouvons changer la couleur du texte à un contenu sur surface primaire.

Et maintenant nous avons la capacité de de nous avons la capacité maintenant de faire pousser ce contenu vers le haut un couple.

Donc maintenant ceci s'aligne directement à la barre d'application supérieure.

Et nous avons la capacité d'échanger les icônes maintenant.

Donc au lieu d'utiliser cet espace réservé, nous pouvons utiliser par exemple male (mâle), je peux aller de l'avant et échanger cette icône ici.

Ajouter la bonne couleur à sur primaire.

Et comme vous pouvez le voir nous avons nos éléments maintenant.

Et je veux en fait m'assurer que cet état est réglé à inactif Mes excuses.

Donc ce serait le le cela devrait utiliser l'emphase moyenne qui n'est pas un style de couleur en ce moment que nous pouvons aller de l'avant et spécifier dans notre bibliothèque.

Donc si nous si nous détachons le style et frappons 68 là, nous avons maintenant notre style de couleur d'emphase moyenne.

Donc si je vais de l'avant et spécifie ce contenu sur primaire, emphase moyenne qui pourrait être notre nouveau style de couleur là, qui serait associé aux autres.

Et pour faire court, maintenant que nous avons ceci créé, nous devons changer la hauteur de cet élément de liste à 40.

Donc vous remarquez comment je commence à combiner des éléments dans notre système de design pour pour être utilisés sur le dessus d'autres composants tels que ces backdrops, qui sont comme, que vous pouvez penser comme ces calques de base, n'est-ce pas.

Donc je vais aller de l'avant et juste continuer à dupliquer ceci et nous avons maintenant reproduit notre, notre backdrop avec le calque avant dissimulé.

Donc ce calque avant est dissimulé là, nous pouvons même aller de l'avant et faire de cela un composant aussi.

Parce que le plus souvent, les designers peuvent utiliser ceci et si nous faisons de cela un composant, les designers peuvent aller de l'avant et juste échanger ces éléments au besoin et renommer le texte je ces éléments de liste et ainsi de suite, comme mess jugent nécessaire.

Donc, ou nous pouvons leur donner le nous pouvons aussi offrir nous pouvons offrir les deux variantes essentiellement n'est-ce pas donc nous avons le, le calque avant dissimulé qu'ils peuvent juste glisser et déposer sur sur un design au besoin ou nous pouvons leur donner tout cet exemple entier, que je vais aller de l'avant et créer.

Donc je vais je vais renommer ceci donc concealed, concealed.

Je vais étiqueter ceci comme concealed et ensuite ceci est juste le front layer concealed.

Donc maintenant que c'est prêt à partir, c'est un composant maître, et nous sommes prêts à partir et c'est comme ça que vous construisez les variantes de backdrop pour material design.   


Aujourd'hui nous allons construire des composants de bannière.

Et sans plus tarder, les aperçus vont être de discuter comment utiliser ces composants en vérifiant la documentation.

Et ensuite nous les créerons nous-mêmes, appliquant la bonne convention de nommage, et même ajoutant les bonnes contraintes et peut-être un peu d'auto layout, mais en fait sauvegarderons cet auto layout et vidéo approfondie sur auto layout, pour la prochaine section du cours recouvrant auto layout pour tous les composants que nous avons créés dans cette section du cours.

Mais avec les contraintes, la seule différence sera que les composants sont déjà faits et nous implémenterons auto layout sur eux dans la prochaine section du cours.

Donc sans plus tarder, vérifions cette ressource de documentation de bannière et une fois que cela ouvre dans votre navigateur, allez-y et cliquez sur cette case à cocher ne s'affiche plus pour ce site web, car vous le vérifierez fréquemment.

Et ici vous pouvez voir que nos j'ai eu ce petit trop zoomé.

Oups.

Et avec cela, les bannières affichent un message opposant et des actions optionnelles liées.

Donc ici nous avons ce message proéminent apparaissant en haut et ensuite nous avons des actions optionnelles liées à prendre basées sur ce qui est dit dans ce message proéminent.

Et vous pouvez aller de l'avant et comprendre l'utilisation ici.

Et cela discute aussi similaire composants similaires, et basé sur la priorité du message étant transmis transmis, vous pouvez utiliser un certain type de composants.

Donc pour les bannières, typiquement quand il y a un proéminent ou un niveau moyen de priorité basé sur le niveau de sévérité, si cette priorité est proéminente ou moyenne, il est typiquement utiliser une bannière, et elles les bannières restent jusqu'à ce qu'elles soient rejetées par l'utilisateur ou si l'état qui a causé la bannière est résolu.

Et il y a quelques différences décrites ici avec des snack bars, et ensuite le composant dialogue aussi.

Et la bannière affiche l'importance.

Importance message succinct et fournit des actions pour les utilisateurs pour adresser ou rejeter cette bannière nécessite une action utilisateur pour être rejetée.

Et elles devraient être affichées en haut de l'écran en dessous de la barre d'application supérieure.

Et elles sont persistantes et non modales, permettant à l'utilisateur de soit les ignorer ou interagir avec elles à tout moment, seulement une bannière devrait être montrée à la fois.

Voici quelques principes et l'anatomie d'une des bannières les plus complexes.

Comme vous pouvez le voir, la bannière la plus complexe a un conteneur avec une illustration de soutien, que vous pouvez aussi référencer comme l'icône de tête ou une icône informative.

Donc l'illustration de soutien.

Et ensuite ici nous avons ce conteneur en encapsulant tous ces éléments dans ce design, et ensuite nous avons le texte, bien sûr.

Et ensuite nous avons les boutons sont optionnels, je veux dire sont des actions de soutien.

Et voici quelques exemples de comment l'utiliser et comment ne pas l'utiliser, seulement une bannière devrait être montrée à la fois, toute bannière apparaît au-dessus du contenu et en dessous de cette barre.

Donc voici le contenu juste ici en dessous de ces images, la collection de ces images.

Et ensuite ici nous avons la barre d'application supérieure, et cela s'adapte juste entre.

Donc vous pouvez toujours vous pouvez penser à cela comme toujours en dessous de la barre d'application supérieure est où cela apparaîtrait.

Et voici quelques autres usages je vous recommande de parcourir pour vraiment comprendre le placement et le comportement est c'est très important.

Et ensuite j'ai ces captures d'écran sur les spécifications sur comment implémenter ceci.

Et nous allons aller de l'avant et référencer le textile dont nous avons besoin.

Et le textile dont nous avons besoin, comme vous pouvez le voir ici est le textile body to.

Et nous allons aller de l'avant et aller dans Figma maintenant et commencer à construire ceux-ci.

Et la première chose que nous allons vouloir faire est d'activer notre système de design material.

Donc pour commencer à tirer certains composants que nous avons déjà construits, donc nous avons construit ce bouton texte.

Et avec cela dit, allons-y et construisons cela.

Donc nous avons un cadre.

Et dans ce fichier d'exercice, j'ai déjà créé la convention de nommage sur comment nous voulons catégoriser ces bannières.

Comme vous pouvez le voir, il y a des bérets mobiles et de bureau.

Donc nous allons aller de l'avant et créer tout cela, je vais aller de l'avant et créer un, un ou deux dans chaque section.

Et ensuite je vais mettre la vidéo en pause et vous faire tester vos compétences et les construire par vous-même d'une manière systématisée.

Donc utilisant autant des actifs que nous avons créés déjà dans notre système de design material ici.

Donc sans plus tarder, commençons.

Donc nous avons cette variante mobile, n'est-ce pas, donc nous avons le texte et l'action en ligne, signifiant qu'ils sont tous les deux au même niveau.

Ils ne sont pas empilés l'un sur l'autre.

Ils sont horizontalement en ligne, n'est-ce pas, ils sont tous les deux sur le même axe, l'axe x était juste horizontal.

Et ce que cela dit, nous pouvons aller de l'avant et juste créer un cadre et je vais renommer ceci et puisque j'ai copié cette convention de nommage dans ce, dans ce fichier, mon calque sera maintenant étiqueté il vit sous la catégorie mobile comme une liste d'une ligne, qui a un texte et une action, et c'est en ligne, ce n'est pas empilé.

Ceci est empilé.

Mais ceci est un exemple de deux lignes.

Comme vous pouvez le voir avec la pile tech, le texte est au-dessus de ces actions.

Et ce dont nous aurons besoin d'abord est notre bouton texte.

Donc nous tapons juste texte, nous pouvons trouver ce bouton texte là.

Et notre panneau d'actifs, nous pouvons glisser cela ici, nous pouvons aller de l'avant et re nommer ceci à action.

Et vous remarquerez que nous avons déjà auto layout appliqué à ce bouton.

Donc nous ne devons pas le redimensionner manuellement, ce qui est très pratique.

Et nous laisserons cela de côté pour le moment.

Et justifions la largeur ici, réglons cela à 360, ce qui adhère aux principes mobiles pour Android car material design a été créé pour Android au début.

Donc avec cela spécifié, allons-y et spécifions la hauteur pour adapter quatre pixels.

Maintenant que nous avons la hauteur spécifiée, une chose dont nous aurons aussi besoin plus tard est le diviseur.

Donc si je vais dans mon panneau d'actifs et cherche le diviseur que nous avons déjà créé, je peux glisser cela ici, et nous avons déjà la largeur spécifiée, et il a le bon style de couleur dont nous avons besoin, je peux juste enlever, je vais aller au composant principal très vite et détacher ce textile éteint inutile, style de remplissage, couleur de remplissage.

Et je vais aller de l'avant et publier ceci.

Et nous serons prêts à partir.

Ajouter de vraies variantes.

Donc, donc maintenant que c'est publié, et c'est publié avec succès, je peux aller de l'avant et mettre à jour le composant ici, comme vous pouvez le voir, c'est maintenant mis à jour, ne contient pas ce, ce calque d'arrière-plan ce remplissage, parce que c'est inutile, nous utilisons un contour ici.

Et nous pouvons juste aller de l'avant et comme vous si vous faites très attention aux designs, vous pouvez ou non avoir besoin de cette bannière, pour avoir un diviseur, comme vous pouvez le voir, il y a un diviseur étant communiqué juste là entre le contenu et la barre supérieure juste là.

Donc gardez juste cela à l'esprit.

Et ce que nous pouvons faire est que nous pouvons offrir ceci, et ensuite les designers peuvent copier ce composant et ensuite l'éteindre si si besoin est.

Donc nous pouvons offrir cela.

Donc je vais, c'est la première chose que je vais ajouter à tous, j'ai juste aligné cela au bas de ce cadre, en maintenant Command S, option s incline moi, puisque c'est un élément enfant du cadre parent, je peux facilement aligner cela au besoin au haut ou au bas.

Donc maintenant que j'ai cet ensemble là, je vais régler les contraintes sont bas gauche et droite.

Donc de cette façon, si cela devait jamais être étiré, ce diviseur s'étirera avec.

Mais nous avons ceci défini ici, et nous n'aurons pas vraiment besoin de, nous n'aurons pas besoin de modifier cela car nous développons le système pour Android dans ce scénario.

Donc avec cela dit, je vais aller de l'avant et glisser dans ce bouton ici aligné à gauche, et c'est huit pixels de la droite et c'est centré verticalement sur l'axe y ici.

Donc c'est réglé en conséquence.

Et ensuite je vais ajouter la contrainte à droite du cadre parent à la contrainte collera à droite de son cadre parent et ensuite ce sera centré verticalement.

Donc chaque fois que c'est étiré, cela restera toujours centré par rapport à la hauteur soit diminuant ou augmentant.

Et ensuite nous allons aller de l'avant et spécifier le texte.

Donc le texte utilise encore, nous allons ajouter un style de couleur ici d'abord texte et iconographie et utiliser le style de couleur de texte haute emphase.

Et ensuite nous allons aller de l'avant et spécifier body to pour cette typographie.

Et ensuite si nous tapons juste one line, juste imiter ce qui est écrit là, et cette spécification chaîne d'une ligne avec une action websi ne peut pas taper ici avec une action, nous devrions être prêts à partir.

Donc avec cela spécifié, je vais aller de l'avant et centrer ceci ici, aligner ceci à gauche avec ma touche de raccourci option A et option B pour centrer verticalement.

Et je vais déplacer ceci à 16.

Donc le remplissage est réglé à 16 dips, juste là, et ce centre.

Et avec ce centré, notre contenu est prêt à partir.

Et vous pouvez voir que material design spécifie que la zone de texte est spécifiquement 30 a un espacement de 36 pixels juste ici.

Donc ce que nous pouvons faire est nous maintenant c'est réglé à 48.

Du bouton texte lui-même, cela donc nous pouvons aller de l'avant et maintenir Command et étirer cette zone de texte pour être réglée à donc l'espacement est réglé à 36.

Donc maintenant c'est réglé à 36.

Ici, l'espacement que nous allons devoir faire pour s'assurer que c'est fixe est que nous pouvons aller de l'avant avec des contraintes et régler cela à gauche et droite.

Donc ces contraintes sont maintenues si cela devait jamais être étiré, et nous n'avons pas nécessairement à nous soucier de cela maintenant.

Je vais régler la typographie aussi pour être centrée verticalement sur l'axe y pour que ce soit en alignement avec l'action qui est en ligne à sa droite.

Donc si les designers ont jamais un besoin d'étendre ceci, cela ne gâchera pas leurs designs.

Donc avec cela spécifié nous sommes prêts à partir.

Je ne vous montre pas l'autolab parce que je vous montrerai cela dans la prochaine section du cours, cela cela sera son propre focus, où vous maîtriserez cela je veux vraiment que vous compreniez les concepts de contraintes dans cette section du cours.

Et juste la la construction générale de ces composants, ainsi que l'ajout d'autolayout dans le mélange peut peut être très taxant déroutant, sur le dessus de toute cette connaissance dense que vous apprenez actuellement.

Donc avec ceci, tout avec la typographie toute spécifiée et attachée à leurs styles de couleur appropriés et tout utilisant des instances, nous devons maintenant aller dans l'arrière-plan de ce cadre et spécifier la couleur.

Donc la couleur utilise est l'arrière-plan de surface, nous pouvons spécifier cela comme surface surface ou surface arrière-plan là était que à surface surface, voilà, comme cela comme la surface qui est superposée au-dessus de l'arrière-plan, ce n'est pas l'arrière-plan initial pour toute la page, c'est juste la la surface pour cela pour ce composant de bannière.

Donc maintenant que nous avons créé ceci, nous allons aller de l'avant et le dupliquer.

Et ensuite nous allons faire de cela un composant.

Donc un composant principal, maintenant nous avons notre composant principal, nous avons notre premier parent créé.

Et allons-y et construisons cette variante de deux lignes avec actions.

Donc une chose à noter est que nous devons probablement modifier la hauteur de ligne de nos éléments de texte, parce qu'au début quand j'ai créé ces textiles dans notre système, ce que j'ai fait intentionnellement pour nous de modifier, et prêter attention à, à la hauteur de ligne de notre typographie, pour s'assurer que c'est fait correctement, parce que si ce n'est pas fait correctement, l'espacement de notre typographie sera off dans dans les composants qui sont des variantes de deux lignes et ainsi de suite.

Donc allons-y et créons quand je déplace cette capture d'écran, créez une nouvelle.

Donc je vais aller de l'avant et copier ceci, cette convention de nommage.

Et quand saisir, je vais créer ceci à partir de zéro un nouveau cadre, réglé à une largeur de 360 et une hauteur de 112.

Ensuite je vais coller dans la convention de nommage, nous avons la version mobile de la deux lignes avec texte et actions, variante de bannière, ce qui est génial.

Et maintenant cela utilise un textile body to, mais je vais aller de l'avant et copier ceci, ce bouton d'action, le coller et maintenir Option s, option D, et cela s'alignera au bas et à droite et ensuite déplacer cela jusqu'à ce que le remplissage soit réglé à huit sur le bas.

Et à droite.

Maintenant je vais dupliquer ceci et m'assurer que le remplissage est réglé à huit là à droite de cet élément.

Et nous avons les deux de ces éléments ici collant à la droite.

Et nous voulons qu'ils collent au bas aussi de ce composant.

Donc si cela devait jamais être étiré, cela collerait à ce bas et droite espacement respectivement respectif de son parent, qui est l'arrière-plan.

Et pendant que nous y sommes, allons-y et changeons le remplissage à surfaces surface cette couleur d'arrière-plan.

Et maintenant nous devons aller dedans et juste justifier l'espacement approprié pour comment notre typographie s'adaptera.

Donc je vais créer cette zone de texte ici, sélectionner le style de couleur body to.

Et ensuite je vais juste imiter ce qui est dans.

Dans ce composant, le texte dans ce composant.

Une à deux lignes est favorable sur mobile, et tablette.

D'accord, super.

Donc nous avons le texte dont nous avons besoin.

Maintenant nous avons besoin de un peu spécifier quelques choses.

Donc ce que nous avons besoin de spécifier est que la ligne de base de la première ligne de texte dans ce texte de deux lignes est réglée à 36 dips, et ce remplissage gauche est réglé à 16.

Ainsi que le remplissage à droite est réglé à nous pouvons dire 16 ici dans ce scénario.

Donc allons-y et alignons cela à la gauche là, poussons ce contenu vers le bas légèrement.

Donc nous avons cela réglé à 16.

Et je vais aller de l'avant et pousser cela et sûr que c'est réglé à 16.

À droite là, régler la contrainte à gauche et droite et le haut et bas.

Et ensuite nous allons avoir besoin de justifier l'espacement ici entre ces boutons et le texte là, qui est où nous commencerons à modifier la hauteur de ligne potentiellement.

Donc allons-y et sortons nos règles ici, shift R, et ensuite je vais créer un rectangle de 36 pixels de haut pour juste référencer où la ligne de base doit être pour ce texte.

Donc je vais pousser ce contenu vers le bas Et essentiellement, c'est en ce moment déclaré que la zone de texte a un remplissage sur le haut de 22 dips pour atteindre ce trois, six, dip ligne de base là depuis le haut.

Comme vous pouvez le voir, et avec cela, nous pouvons même ajuster cette zone de texte pour s'assurer qu'elle ne chevauche pas ou interfère avec les actions en dessous d'elle.

Et cela met en valeur qu'il y a un espacement de 12 pixels de la ligne de base au haut du bouton.

Donc allons-y et vérifions cela.

Et si ce n'est pas le cas, c'est une indication de potentiellement notre hauteur de ligne étant off sur le style de type.

Donc allez-y et créez ceci réglez cela à 12, nous sommes très proches, il y avait un pixel off les lignes de base un pixel off.

Donc essentiellement ce que nous pourrions faire est d'aller dans notre textile et modifier cela.

Donc c'est réglé à 20.

Donc je vais dedans et modifie, vais au style de définition, modifie le à 20.

Et ensuite publie cela dans ma bibliothèque, publier, publié avec succès et ensuite je peux mettre à jour ceci, une fois que je le mets à jour faire attention au texte ici tombant d'un pixel, et il est en fait tombé de plus d'un pixel.

Donc je vais aller de l'avant et annuler ce style.

Et référencer mon textile body to, m'assurer que c'est là, je vais republier ce changement, et juste m'assurer que cela se met à jour à nouveau, donc que cela reste là.

Et je vais vivre avec cela juste un pixel off là, bien que je pense vraiment que c'est correct.

Euh, et avec cela, atteint l'apparence et le sentiment et vous avez tout l'espacement réglé correctement.

Et ce style de couleur approprié sur le texte, avec le textile haute emphase appliqué, nous devrions être prêts à partir.

Donc tout comme je peux même cacher mes règles ou juste les enlever spécifiquement de ce calque, une chose qu'il nous manque est un diviseur.

Donc je vais copier ce diviseur ici, et ensuite le coller et ensuite frapper option s et cela s'alignera au bas de cet élément.

Et il a cela a les contraintes du composant précédent que nous avons construit.

Et ensuite une fois que j'ai construit cela, nous pouvons tester les contraintes là.

Et vous remarquerez que les contraintes sont maintenues et cet espacement quand j'étire cet élément, et le diviseur colle à où il doit être.

Et une fois que je suis satisfait de la réactivité de ce composant, je suis prêt à partir.

Si vous voulez vraiment être clair, concis, vous pouvez créer le réorganisé les les éléments dans votre composant, ce qui est une excellente chose à faire est que ce sera plus facile de consommer les composants.

Et je vais aller de l'avant et faire de cela un composant maître, je vais le dupliquer et mettre cette vidéo en pause et construire la la troisième variante pour la version mobile.

Donc ce que vous pouvez faire est de modifier ceci au besoin, vous pouvez glisser dans une icône d'espace réservé.

Donc nous pouvons taper placeholder.

Et nous avons cet espace réservé.

Et nous pouvons arrondir les bords.

Donc vous pourriez maintenant que nous avons cette icône ronde, et vous avez un, vous savez une longueur d'avance là, et un indice.

Donc je serai de retour.

Maintenant créé cette troisième variante, j'ai juste dû augmenter la hauteur à 120.

Ajouter dans cette icône de 40 par 40 dip, régler ce remplissage perspective en relation à ce qui est indiqué dans la spécification ici.

Et j'ai un peu juste c'était très simple et direct.

Rien, rien de difficile là, je me suis juste assuré que j'avais ces bonnes contraintes réglées.

Et je et vous devriez être prêt à partir.

Et avec cela dit, je vais aller de l'avant et faire de cela un composant principal.

Et nous allons aller de l'avant et créer la version de bureau.

Donc avec cette variante d'une ligne ici, nous pouvons aller de l'avant et spécifier la hauteur et j'ai juste dupliqué, cette première version que nous avons créée sur mobile parce que c'est essentiellement la même chose exacte.

Mais pour le bureau, la largeur est spécifiée à un beaucoup plus grand, c'est beaucoup plus grand la largeur là.

Et ce que nous pouvons faire est de régler cette largeur à 720.

Maintenant, et la chose agréable à ce sujet est que nos contraintes s'adapteront en conséquence.

Donc a toujours cet espacement là nécessaire.

Donc les textes peuvent remplir une bonne majorité de ce message ici, et nous avons le diviseur là pour les designers à utiliser si besoin est pour vraiment rendre ce message Tel distinct.

Et nos propriétés de typographie restent les mêmes ou action toujours là avec le même espacement sur ces éléments, c'est juste que la largeur est maintenant changée.

Et j'ai besoin de changer cela à la convention de nommage de ce composant aussi.

Donc c'est desktop.

C'est une ligne, texte et action en ligne pour la zone de bureau, donc je peux aller de l'avant et juste changer cela à desktop, il renomme cela, et nous sommes prêts à partir.

Donc avec cela, allez-y et faites de cela un composant principal.

Et nous créerons l'autre à partir de zéro, ici, donc nous avons, nous ne, la largeur pour cet élément de trois lignes semble qu'il peut être réglé à 80 pixels, il ne me donne pas en fait cette hauteur spécifiée, nous allons juste les jeter dehors.

Donc je vais référencer cette documentation à nouveau.

Ouais, c'est coupé, c'est difficile à lire, mais je vais, je suis assez sûr que c'est à comme c'est divisible par huit.

Donc pour cette liste de trois lignes, allons-y et créons un nouveau cadre.

Et cliquez, appliquez les bonnes surfaces couleur de surface trucs dans l'arrière-plan, je vais aller de l'avant et saisir cette convention de nommage là dans bien organisée et publier ces composants.

Donc j'ai cette convention de nommage réglée.

Et je vais aller de l'avant et spécifier la largeur à 720.

Et saisir un diviseur, comme cela saisira, mettra en place, obtiendra toutes les choses génériques hors du chemin, spécifier cette largeur à 720.

Régler les contraintes bas gauche et droite, cela utilise juste mes touches de raccourci pour l'aligner tout en bas, comme vous pouvez le voir ici.

Et c'est prêt à partir.

Et nous avons juste besoin de vérifier la hauteur ici, régler cela à 80.

Et ce diviseur colle toujours reste là comme besoin est.

Et nous pouvons aller de l'avant et ajouter ces deux actions, obtenir celles-ci hors du chemin.

Donc je vais copier ce bouton texte, le coller, l'aligner au bas et à droite et ensuite le déplacer vers le haut.

Donc le remplissage sur le bas à droite réglé à huit, dupliquer ceci et s'assurer que c'est huit pixels loin du bouton à droite, appliquer les contraintes appropriées ici.

Et nous devrions être prêts à partir les boutons d'action.

Maintenant nous avons juste besoin de trouver notre liste de trois lignes de notre chaîne de texte de trois lignes.

Donc je vais aller de l'avant et créer cela sélectionner le textile body to.

Et ce dont nous avons besoin, je vais aller de l'avant et mettre cette vidéo en pause, copier ce texte très vite.

J'ai écrit le mot exact pour mot, message de bannière ici.

Et j'utilise le bon textile.

Et j'ai besoin d'en fait maintenir Command et m'assurer que ce textile enveloppe l'intégralité de ce message et ensuite le centrer verticalement et ensuite vérifier l'espacement à gauche ici réglé à 24 dips.

Donc j'ai 25 en ce moment pousser cela d'un dip, et nous sommes prêts à partir.

Et l'espacement entre ici et ici.

Et la zone de texte est 90 dips.

Donc ce que je peux faire est d'étirer cela pour que ce soit réglé à 90.

Maintenant j'ai 90 pour pousser cela quelques fois.

Ce n'est pas ce que 94 donc maintenant j'ai déplacé cela, c'est réglé à 90.

Maintenant nous avons cet espacement de 90 entre la boîte englobante de texte et les actions ce qui est super important.

Donc maintenant que nous avons cela nous sommes prêts à partir, nous avons maintenant défini cela.

Et je vais aller de l'avant et créer ce composant.

Et je vais vous mettre au défi de construire ce dernier message de bannière de bureau par vous-même.

Donc suivez juste ces spécifications, la hauteur ici dit 72, juste parce que c'est coupé en cela pourrait être difficile.

Et ensuite la ligne de base de ce texte ici est 20 pixels du bas, mais juste c'est en fait juste huit.

Donc mêmes spécifications que nous avons faites ici pour ces boutons réels.

Quoi qu'il en soit, je vais mettre la vidéo en pause et faire ceci et j'espère que vous avez apprécié cet exercice.

Maintenant créé cette troisième variante de bureau pour le message de bannière et nous sommes prêts à partir.

Donc maintenant nous avons ce composant que les designers peuvent maintenant aller de l'avant et dupliquer et ensuite commencer à remplacer l'imagerie au besoin pour l'espace réservé d'icône modifiant la typographie avec la bonne boîte englobante de texte.

Appliquer spécifié là pour ce composant et ensuite aussi le placement approprié pour ces boutons aussi pour Ajouter et modifier le texte, ce qui est génial.

Aujourd'hui nous allons passer en revue la construction de la navigation inférieure et il n'y a que deux variantes sur la navigation inférieure et c'est la version portrait et le paysage.

version pour le, nous allons concevoir cela pour le format basé sur Android.

Et nous avons la ressource vers la documentation, donc vous pouvez ouvrir ce lien.

Et si nous allons de l'avant et cliquons dessus, clairement à la navigation inférieure permet le mouvement entre les destinations primaires et une application.

Ceci est crucial et très courant.

Et c'est utilisé dans chaque application, que vous utilisiez Facebook mobile sur votre téléphone, que ce soit iOS, ou Android, ou que vous utilisiez YouTube, ou que vous utilisiez une sorte d'application Google au sein de la suite Google.

Et je vous recommande fortement de juste lire à travers tous les contenus, tout comme chaque autre vidéo pour vraiment comprendre en profondeur ce que font ces composants tout ce qui est associé à ces éléments, et aussi la recherche derrière cela.

Et aussi comprendre les états et comment vous interagissez avec cela.

Donc dans Figma, j'ai pris des captures d'écran des spécifications.

Et une chose à noter qui est très importante est que la largeur minimale du conteneur pour chaque bouton est réglée à 80 dips, et la largeur maximale est réglée à 168 dips en largeur.

Donc vous remarquerez qu'ils utilisent tous les deux la largeur minimale spécifiée ici, 80, dips de large.

Et sur la version portrait, portrait étant si nous créons un cadre, et je vais de l'avant et sélectionne Android, j'ai maintenant ma version android.

Donc je vais juste taper, je vais étiqueter ceci correctement.

Donc je vais aller de l'avant et taper bottom navigation espace slash base, portrait.

Une fois que vous avez étiqueté cela correctement, je vais aussi dupliquer cela et régler ce type en paysage.

Et une fois que vous spécifiez paysage maintenant que paysages, ceci est paysage, donc nous allons concevoir pour le paysage ici.

Et nous allons aller de l'avant et commencer par lancer cette fête en spécifiant la hauteur de ceci à 56 pixels, et il a cette barre d'application inférieure l'élévation dans le diagramme, vous pouvez le regarder vous-même pour vérifier si vous ne me croyez pas, mais l'élévation par défaut réglée à huit dips.

Donc ce que vous remarquerez est que disons que j'avais un autre cadre ici, et je détache cela, et je suis juste allé et re spécifié que c'était le cadre de taille material design.

Et je suis allé de l'avant et juste Android juste étiqueté ce portrait Android.

Et vous remarquerez que ceci est la navigation inférieure réglée à portrait ici, et que le contenu est rogné.

Maintenant parce que le cadre parent a cela coché, vous ne verrez pas l'ombre portée sur les autres côtés.

Donc maintenant nous devons aller de l'avant et commencer à ajouter dans le contenu.

Donc qu'est-ce que nous avons nous avons ces trois icônes ici, mais celles-ci vivront à l'intérieur de conteneurs spécifiques.

Donc ces icônes sont réglées à 24 dips de large et en hauteur et sont centrées sur l'axe ici.

Donc si je vais de l'avant et sélectionne ces trois, je peux aller de l'avant et m'assurer que celles-ci sont horizontalement centrées, et ensuite les espacer en conséquence.

Et ce que vous pouvez faire pour vous assurer que c'est qu'il est centré au sein de 120 pixels cadre 120 dip large cadre.

Donc si vous êtes confus, est, puisque ceci est 363 60 divisé par trois est 120 dips.

Donc tout ce que nous avons à faire est d'envelopper un cadre autour de chacune de ces icônes, régler la largeur à 120 et la hauteur à 56.

Et ce que nous voulons faire est que je frappe option W et a pour l'aligner au haut et à gauche.

Et ensuite si je frappe Entrée, et frappe option V et H cela centrera cela parfaitement sur l'écran.

Et ensuite nous pouvons faire la même chose exacte pour celui-ci aussi.

Donc je peux en fait détacher cela maintenant que c'est centré, c'est positionné avec un remplissage de 48 à gauche et verticalement sur l'axe y.

Donc tout ce que nous avons à faire est d'envelopper cela dans un cadre, régler cela à 120 pixels de large, et la hauteur à 56.

Je vais frapper option w pour que les alignements au haut, et ensuite je vais agir aller centrer horizontalement ceci et ensuite frapper entrée et frapper option D et H pour centrer cela au sein de ce cadre.

Donc vous remarquerez que ceci est 120 pixels de large et donc est la section à sa gauche.

Et ce que nous pouvons faire est maintenant que c'est centré je peux dégrouper ce cadre.

Et je pourrais même appliquer juste l'espacement ici, juste pour vérifier.

Ou je pourrais envelopper cela dans un cadre.

Encore une fois, si vous n'êtes pas si confiant voulez être extrêmement précis, réglez la largeur à 120, la hauteur à 56, et ensuite frappez option D, donc les alignements à gauche, option W, donc cela s'aligne au haut du cadre parent que je vais entrer.

Maintenant j'ai mon icône sélectionnée, frappe option D, et ensuite H.

Maintenant que c'est centré au sein du cadre large de 120 dips, et c'est 48 pixels loin de la prochaine icône.

Et je peux dégrouper cela maintenant mon panneau Calques, et maintenant tout est centré en conséquence.

Donc maintenant j'ai mes icônes correctement centrées dans la navigation inférieure.

Donc une chose qui nous manque, bien sûr, est cette typographie.

Donc nous pouvons aller de l'avant et référencer la documentation une fois de plus.

Et cela vous montre que ce type, nous pouvons vérifier la typographie dans le thème.

Et cela utilise le style de légende.

Donc avec cette légende étant utilisée, la la ligne de base est 12 dips loin du bas du cadre d'icône, ce qui est une excellente chose pour nous à référencer.

Donc si nous allons de l'avant et maintenant créons un textile, je vais aller de l'avant et créer ce textile et étiqueter cela oups.

Je vais juste taper featured régler ce redimensionnement à largeur automatique, appliquer la légende textile.

Et m'assurer que le remplissage est réglé à sur primaire et m'assurer que c'est en majuscules.

Et je vais double vérifier oups, ce n'est pas tout en majuscules.

Et j'ai écrit la mauvaise chose, excusez-moi, c'est étiqueté favorites fait devrait faire attention ici.

Et essentiellement ce que je vais faire est avec cette hauteur de ligne réglée.

Avec cette ligne de base, je vais juste centrer ceci au centre de ceci en le déplaçant, vous verrez que cela s'aligne me donne cette indication de flèche rouge, je vais déplacer ceci vers le haut et voir j'ai cette ligne rouge ici que je vais appliquer au bas du cadre.

Et j'ai besoin que la ligne de base soit réglée à 12 pixels en ce moment.

C'est réglé à un 11 sur la ligne de base ou notre ligne de base réglée à 11.

Donc si nous avons besoin de pousser cela vers le bas d'un pixel, ce qui laisse un écart de pixel sur le haut de la boîte englobante extérieure des icônes.

Donc maintenant nous avons la ligne de base réglée à 12.

Donc c'est fantastique.

Et nous pouvons aussi référencer un donné notre, notre typographie ici, ce que nous allons avoir besoin de faire est en fait sélectionner cette icône.

Et nous pouvons aller de l'avant et grouper ceci et ensuite je peux maintenir option v.

et cela centrera en fait ce contenu.

Et ensuite je vais dégrouper cela à nouveau.

Et ce que je veux faire est de m'assurer que cet a lot, l'alignement du texte est au centre.

Donc chaque fois qu'un utilisateur le renomme, cela est juste automatiquement centré dans ce composant.

Donc ils n'ont pas à traiter avec le gâchis avec l'alignement et ainsi de suite, cela pourrait être très irritant.

Donc maintenant que c'est spécifié, nous sommes prêts à partir.

Et vous remarquerez que quand le texte est appliqué, cela pousse vers le haut l'icône.

Et les icônes qui ne sont pas actuellement actives restent verticales, verticalement centrées sur l'axe avec ce texte étant appliqué, prend cela en considération et le calcule, et ensuite centre cela verticalement avec icône plus texte.

Donc maintenant que nous avons cette variante créée, nous pouvons aller de l'avant et juste créer cela comme un composant principal.

Maintenant nous avons un notre paysage ou portrait composant principal.

Donc nous pouvons aller de l'avant et en fait dupliquer ceci, jeter ceci dans notre variante paysage, je vais renommer ceci à paysage et détacher cette instance avec la touche de raccourci option command B.

Et ce que nous pouvons faire est de s'assurer que nous avons des contraintes appropriées appliquées à ceci.

Donc avec cet exemple, cela utilise toute la largeur de la version paysage du téléphone Android ici dans le cadre six dans cet exemple.

Donc ce que nous pouvons faire est de s'assurer manuellement que c'est correctement appliqué.

Et en faisant cela, nous devons nous assurer que ces nous avons trois boîtes réglées à 168 dips de large ou si vous avez une autre meilleure façon de le calculer.

S'il vous plaît faites-le.

Car c'est la meilleure façon.

Je sais que tout est verticalement centré, comme vous pouvez le voir, mais ce que je vais faire est la même approche que nous faisons avec la version portrait.

Donc je vais régler la largeur à 168 dips pour la hauteur 256 et aligner cela au haut et à la droite, et sélectionner mon icône, maintenir Option v h, s'assurer que c'est centré.

Donc nous avons ceci implémenté correctement, je vais aller de l'avant et faire la même chose exacte pour pour ce prochain, et je vais séparer le haut et l'aligner horizontalement au centre.

Donc maintenant, j'ai juste besoin de faire cela avec l'icône aussi.

Maintenant que c'est appliqué, nous pouvons dire que nous voulons aligner ceci, nous voulons que les bords de chacun de ces cadres s'alignent les uns à côté des autres, parce que c'est centré au milieu de ce au milieu de cette variante paysage, faisant la même chose exacte.

Arbre appliquant ces valeurs, je vais m'assurer que ce texte et ses favoris et icône sont groupés aussi, et centrer cela au sein de ce cadre.

Et ensuite je vais aligner ceci au haut, et ensuite pousser ceci jusqu'à ce que cela s'aligne pour voir cette ligne rouge.

Maintenant j'ai les trois éléments alignés en conséquence.

Et je peux aller de l'avant et dégrouper ces propriétés au besoin.

Donc je vais dégrouper ces cadres.

Donc juste utiliser cela pour mesurer ceci parfaitement ou correctement.

Et avec cela dit, nous avons maintenant tout cela aligné correctement, et nous sommes prêts à partir.

Tout ce que nous avons à faire est de s'assurer que nous faisons de cela un composant principal.

Donc c'est notre composant principal.

Et maintenant tout ce que nous voulons faire est d'aller de l'avant nous pouvons même jeter ce cadre ici est un exemple de chaque format.

Ou vous pourriez juste en fait, nous voulons juste aller de l'avant et jeter ceci là-dedans tel quel.

Aujourd'hui, nous allons parler de comment construire des composants.

Et ça va être vraiment simple, nous allons commencer par dans ce fichier aller à notre bibliothèque d'équipe, vous pouvez maintenir Option 3.

Et activer cette bibliothèque, la bibliothèque à laquelle vous allez vouloir accéder est étiquetée comme material design system, ignorez celle qui est activée ci-dessus étiquetée material design, nous voulons le material design system.

Et je vais juste éteindre cela pour que vous ne soyez pas confus.

Donc maintenant que nous avons cette bibliothèque activée, il aura materializes some library incapable d'accéder dans notre panneau d'actifs.

Et la première chose que nous allons voir est que vous pouvez aller de l'avant et cliquer sur la documentation ici, c'est un lien dans Figma.

Donc vous pouvez aller de l'avant et ouvrir la page composant sur le site web de material designs pour comprendre ce que ce composant fait réellement.

Il y a beaucoup d'informations approfondies ici que je recommande totalement de consommer car cela ne vous bénéficiera qu'en tant que designer.

Et vous remarquerez que nous avons ce bouton d'action flottant interactif que nous allons en fait construire nous-mêmes.

Il y a une version par défaut, et il y a une version mini réglée à 40 dips, la défaut réglée à 56 dips, et c'est 56 dips en largeur et hauteur ainsi que les mini réglées à 40 dips en largeur et hauteur aussi.

Et ensuite nous avons une variante étendue de ce bouton d'action flottant qui vient soit avec ou sans une icône.

Et nous allons créer la majorité de ces composants aujourd'hui.

Et ce que j'ai fait est que j'ai saisi les captures d'écran des spécifications.

Et cela vous dit en fait comment construire ceux-ci dans Figma.

Et nous les transformerons en composants principaux pour ensuite publier dans notre bibliothèque.

Et cela parle du placement.

Et encore une fois, c'est vraiment important, parce que cela vous apprendra certainement comment différencier certains types de boutons alors que nous créons plusieurs types de boutons.

Et c'est seulement un ensemble de ces boutons.

Ce sont un bouton d'action flottant.

Et comme vous pouvez le voir, il y a des variantes de ceci, nous avons un deux, la variante de tête et texte.

Et ensuite nous avons deux variantes des boutons d'action flottants réguliers.

Donc nous avons un total de quatre variantes là.

Et maintenant, vous pouvez voir ceci comme vous souhaitez vous référer.

Et nous allons aller de l'avant et vérifier notre fichier Figma.

Et j'ai ce fichier d'exercice configuré avec les captures d'écran pour nous à référencer.

Et la première chose dont nous allons avoir besoin maintenant que nous avons pu bibliothèque est l'icône.

Donc c'est une icône plus.

Donc si je tape plus, peut-être que nous pouvons juste cliquer sur cela et continuer à chercher cette icône.

Et si cela n'apparaît pas dans votre panneau d'actifs, vous pourriez aussi juste étendre toutes les icônes ici et vous pouvez chercher par catégorie aussi.

Si c'est juste trop écrasant pour vous, vous remarquerez que je vous montre lentement ceci pour montrer Deviner la fonctionnalité.

Et encore une fois, nous pouvons continuer à chercher à travers ceci si nous voulons.

Mais encore une fois, c'est en fait très fastidieux et pas bon pour notre processus de design.

Donc la meilleure façon de s'y prendre est d'aller directement au fichier où toutes ces composants vivent.

Donc vous pouvez aller de l'avant et glisser n'importe lequel de ces composants dans votre canevas.

Et si vous glissez cela dedans, vous pourriez alors aller cliquer sur Aller au composant principal, et cela vous emmènera directement vers où ces composants maîtres vivent.

Et puisque tous nos composants vivent au même endroit, nous allons aller de l'avant et le chercher nous-mêmes.

Ceci, nous allons chercher cette icône plus, et elle devrait vivre sous notre catégorie action.

Je sais même ici, cela peut être difficile à analyser et trouver.

Donc je vais mettre en pause et chercher ceci très vite.

Puisque je ne peux pas trouver cette icône, ce n'est en fait pas dans notre bibliothèque.

Et encore une fois, c'est notre bibliothèque où je n'ai intentionnellement pas mis toutes les icônes ici, bien qu'avec le temps cela le fera.

Et j'ai fait cela parce que je veux en fait que nous utilisions l'outil icône.

Donc je vais taper en ligne sur l'internet Material Design icons tool.

Et essentiellement, cet outil est une ressource pour télécharger des icônes spécifiques dont nous avons besoin.

Et nous pouvons aussi chercher des catégories, comme je l'avais discuté dans la vidéo précédente.

Et nous pouvons soit la chercher en défilant à travers, bien que cela puisse être difficile, ou je peux la filtrer par le nom et je peux juste taper plus.

Et vous remarquerez que sous la catégorie actions, ce sont toutes les variantes plus de l'icône.

Donc j'ai gardé j'ai tapé plus.

Et ce que je cherchais en fait était l'icône Ajouter.

Donc si je peux vérifier en retournant à ma bibliothèque, et cherchant add, et mes icônes, et vous remarquerez que c'est là, c'était juste difficile pour moi de trouver car c'est tout très dense.

Oh, la voilà.

Laissez-moi voir, parfois vous pouvez être submergé par ce contenu.

Donc je peux aller de l'avant et copier ceci.

Et c'est appelé content add.

Et je vais aller de l'avant et chercher cela comme un exemple content.

Et si je tape slash add, cela compartimentera encore plus cela.

Et encore une fois, nous sommes prêts à partir, je peux glisser ceci sur le canevas, j'ai maintenant les dimensions appropriées pour cette icône, je vérifie juste que la largeur et la hauteur de cette icône est réglée à 24 par 24.

dips dans ce cas.

Donc vous voyez que c'est spécifié ici dans le panneau Propriétés.

Et toutes ces variantes du bouton d'action flottant, utilisent toutes une largeur de 24 par 24, largeur et hauteur de 24 dips.

Je suis ici pour l'icône.

Et nous allons aller de l'avant et créer la variante régulière d'abord.

Donc ce que nous allons faire est, maintenant que nous avons cette icône, je vais en fait maintenir Option Command G pour créer un cadre.

Et nous allons étiqueter ceci buttons, space slash space, floating action.

Oups, action button, regular.

C'est la variante régulière du bouton d'action flottant.

Et cela vit sous la catégorie des boutons et sous la catégorie bouton d'action flottant, et c'est la variante régulière.

Donc c'est important de noter que nous obtenons cette convention de nommage réglée dès le départ, cela rendra nos vies beaucoup plus faciles.

Et vous saurez ce que je veux dire quand nous commencerons à publier ces composants dans la bibliothèque.

Et Ok, donc maintenant ce que je veux faire est de maintenir Option, imaginer transformer ceci en un cadre à nouveau, eh bien c'est le cadre.

Et ce que je vais faire est de maintenir Shift Option alors que je glisse sur le cadre et m'assurer que c'est réglé à 56 par 56.

Et sinon, si vous ne voulez pas faire cela de cette façon, c'est beaucoup plus rapide, vous réglez juste ceux-ci à 56 par 56.

Vous remarquerez que l'icône est réglée en haut et à gauche.

Par défaut, alors que j'échelonne cela, ce que je vais faire est dans le panneau Calques, cliquer sur cette icône, maintenir Option V et ensuite H et cela centrera mon icône parfaitement comme nécessaire pour mon bouton d'action flottant afin de créer cela.

Donc maintenant que j'ai créé cela, vous remarquerez que l'espacement à gauche et à droite de l'icône devrait être réglé à 16.

Donc le remplissage devrait être réglé à 16 dips à gauche et à droite ce qu'il est sur ce cadre.

Et cela pourrait être difficile pour vous de voir parce que par défaut ce remplissage était désactivé éteint et je maintiens option pour obtenir ces mesures de ligne de pain.

Donc vous verrez que ces spécifications sont réglées correctement.

Et c'est déjà centré verticalement et horizontalement comme nécessaire.

La taille du cadre est correcte.

Et ce que je dois faire avant d'oublier est de m'assurer que la couleur de cette icône... je vais éteindre cette icône de remplissage et la couleur de sélection, qui est la couleur appliquée à l'icône ici, doit être réglée correctement.

Donc elle doit être réglée sur content on primary.

Et vous ne pouvez pas le voir pour le moment mais c'est bon.

Parce que nous allons spécifier la couleur d'arrière-plan de ce remplissage en cliquant sur style, en allant dans notre contenu.

Et ensuite nous allons sélectionner on background ou on surface.

C'est la même valeur de couleur.

Et encore une fois, s'il y a jamais la moindre confusion sur la couleur à appliquer, nous pouvons toujours référencer la documentation ici et dans Material Design, pour mieux comprendre le comportement et obtenir des indices ou des conseils sur la façon de mieux construire ces éléments.

Mais maintenant que je sais ce que c'est, je vais m'assurer que ce composant a des coins arrondis.

Donc je vais changer le rayon d'angle ici et arrondir cela.

Vous remarquerez que c'est maintenant arrondi quand je règle cela à 32 dips 32 sur le rayon d'angle, j'ai maintenant mon cercle arrondi.

Et nous avons les couleurs désirées appliquées.

Et avec cette icône implémentée aussi, je, la dernière chose que je dois faire est d'ajouter un style d'effet à ce bouton.

Et rappelez-vous, quand nous avons travaillé sur l'élévation, et j'ai créé un diagramme de l'élévation, une chose que nous pouvons faire est de référencer la documentation encore une fois, et aller à l'élévation sur le site web de Material Design.

Si nous allons à nos composants, ou si nous allons au design, et nous sélectionnons l'environnement et sélectionnons l'élévation, et nous allons à la hiérarchie d'élévation, ou oups, c'est quoi une délimitation par défaut de l'élévation, j'essaie de trouver le bon exemple d'élévation et où cela se situe sur un bouton d'action flottant.

Donc un bouton d'action flottant.

Trouvons l'exemple ici.

Ok, donc nous l'avons, c'est juste ici.

Donc vous voyez ce bouton d'action flottant juste ici, le bouton d'action flottant se situe sur quand il s'élève à 12 dips en élévation.

Et vous remarquerez qu'il vit entre quatre et huit dips sur cet axe ici.

Et il vit sur les six dips sur l'axe y.

Donc c'est là où le bouton d'action flottant est par défaut.

Donc si nous allons de l'avant et allons réellement à nos styles, allons aux effets et appliquons le 6 dip, qui est déjà étiqueté aussi dans un système de couleurs dans la description, ce qui est génial, nous avons maintenant créé notre bouton d'action flottant régulier.

Et une fois que vous avez créé le composant désiré au besoin, nous pouvons aller de l'avant et transformer cela en un composant principal (Main Component).

Et vous pouvez soit cliquer sur Créer un composant dans la barre d'outils juste là au centre.

Mais j', j'utilise toujours la touche de raccourci pour créer un composant principal et c'est Option+Command+K.

Si vous faites attention à votre panneau Calques, une fois que j'appuie sur cette touche de raccourci, j'aurai maintenant un composant principal.

Donc c'est génial.

Et ce dont nous avons besoin maintenant est un mini bouton d'action flottant, qui est le ce que FA B signifie, et tout ce que nous avons à faire en fait est que nous pouvons aller de l'avant et dupliquer ceci, parce que essentiellement ce que c'est, c'est une version plus petite du régulier, c'est juste rétréci.

Et ce que nous allons devoir faire est de détacher cet élément, je vais faire Option+Command+B, je ne suis pas attaché c'est un cadre régulier, ou vous pouvez faire un clic droit et cliquer sur détacher l'instance, ce qui le détache du composant principal.

Et ce que nous devrons faire est maintenant de spécifier l'espacement et le resserrer.

Donc vous remarquerez que le remplissage tout autour est réglé à 16 dips.

Et tout ce que vous avez à faire est de régler la hauteur et la largeur de ceci à 40 dips ici comme spécifié dans les spécifications, je peux aller de l'avant et appuyer sur ces proportions de contrainte, taper 40.

Et cela le fera et ce que je peux faire est de sélectionner l'icône appuyer sur Option V et ensuite Option H, je maintiens juste Option puis appuie sur D puis H et ensuite cela centrera automatiquement cela dans le cadre parent.

Donc tout est maintenant réglé à huit dips en haut, à gauche, en bas et à droite spécifié ici.

Et nous sommes prêts à partir.

La seule chose que nous devons faire est en fait d'aller de l'avant et renommer ceci et nous allons l'appeler le mini fab au lieu de régulier.

Donc nous n'avons pas à changer la convention de nommage à gauche de ce calque, juste la portion la plus à droite de celui-ci, qui est régulier.

Donc changez cela en mini fHb.

Vous pouvez une fois que vous avez fait cela, transformer cela en un composant maître, clic droit Créer un composant ou composant principal, je m'excuse.

Et maintenant nous avons ces deux variantes.

Super, nous sommes prêts à partir.

Et l'étape suivante est que nous allons avoir besoin de créer un autre bouton et c'est un bouton d'action flottant étendu.

Et c'est notre dernier élément que nous aurons besoin de créer ici.

Et avec ceci créé, nous allons aller de l'avant et référencer ce mini bind.

Je vais dupliquer ce bouton et je vais le détacher, détacher cette instance.

Et je vais aller de l'avant et régler la convention de nom.

Et c'est un long nom.

Donc je vais taper extended FA B.

Donc bouton d'action flottant étendu.

Maintenant que nous avons ce nom correctement, je vais aller de l'avant et m'assurer que nous spécifions le cadre parent, nous allons utiliser le cadre parent pour régler les paramètres du bouton.

Donc tout ce que j'ai fait était que j'ai saisi le bord droit, maintenu Command et étiré cet élément.

Et je dois m'assurer que j'ai mes contraintes réglées correctement, peut-être que je veux mes contraintes au centre sur l'axe y.

Donc si je ne centrais pas ceci, je réglais le haut et la gauche sur les contraintes, cela collerait juste là.

Et je ne veux pas ça parce que je dois régler cette hauteur à 48.

Et j'ai toujours besoin que cette icône soit alignée centrée verticalement, je pourrais juste appliquer cette propriété, aller de l'avant et changer la hauteur à 48.

Et cela reste centré, vous remarquerez que c'est quels pixels en haut et en bas proportionnellement.

Et vous pouvez voir à quel point l'utilisation des principes spécifiés par Material Design est puissante.

Les choses seront toujours divisibles par quatre ou huit.

Et maintenant que j'ai cette hauteur spécifiée, je dois régler l'espacement à 12 au lieu de huit à gauche.

Donc maintenant j'ai cela réglé à 12.

Donc cet espacement est maintenant proportionné.

Et j'ai besoin en fait de créer du texte.

Et nous avons déjà le style de couleur, parce que nous avons activé notre bibliothèque pour le style de couleur du bouton.

Et je vais spécifier, je vais créer du texte ici, appuyer sur T sur mon clavier, créer l'outil texte.

Et je vais taper Create.

Et je vais m'assurer que j'ai le contenu, le style de couleur réglé correctement.

Donc j'ai content on primary.

Donc sur primaire, vous remarquerez qu'il utilise le Roboto mano, donc ne ressemble pas encore à ce textile, mais nous devons appliquer un style.

Donc avec ce texte sélectionné, je peux cliquer sur l'icône des textiles.

Et ensuite aller de l'avant et sélectionner Button.

Et j'ai maintenant Create réglé.

Et avec cela créé, je peux aller de l'avant et donc une seconde, une fois que c'est spécifié, je peux aller de l'avant et et spécifier ce que je vais avoir besoin de faire avec ce style de couleur est de m'assurer que je maintiens command et saisis le bord de ce texte ici.

Et je peux aller de l'avant et centrer ceci.

Donc Option+V pour centrer verticalement ceci, mon espacement réglé à 12 ici et j'ai besoin que l'espacement à droite soit réglé à 20.

Parce que c'est ce qui est spécifié, le texte est centré comme il est pointé ici, à travers le contenu étant l'icône et le texte est centré dans ce bouton d'action flottant qui est étendu.

Et j'ai maintenant centré cela ici.

Et nous devons régler l'espacement à 20 ici, donc je peux aller de l'avant et cliquer sur ceci, je peux maintenir Option ici, ce qui me permettra de voir l'espacement et je maintiens Command et pousse ceci vers la gauche pour voir si j'obtiens le bon espacement, j'étais décalé d'un pixel.

Donc maintenant c'est réglé à 20 là.

Et j'ai maintenant créé le bouton d'action flottant étendu avec toutes les propriétés appropriées.

Donc nous pouvons aller de l'avant et double vérifier cela en tirant juste ceci à côté.

Et ce que nous pouvons voir est que nous avons l'icône réglée à 24 par 24 dips comme spécifié ici, l'espacement réglé à 12 sur la gauche et la droite de la gauche du bord du bouton et la droite du texte.

Et c'est centré verticalement.

Et la hauteur du bouton lui-même est réglée à 48 dips.

Et le texte a un remplissage à gauche réglé à 12 et un espacement de remplissage à droite réglé à 20 dips.

Et nous sommes prêts à partir.

C'est notre bouton d'action flottant.

Flottant bouton d'action flottant étendu désolé, beaucoup de mots qui se passent je me confonds moi-même.

Donc je vais créer cela comme un composant principal.

Et une chose que vous remarquerez est que si je tape dans ce composant, je n'ai pas essentiellement ce dont j'ai besoin, qui est Auto Layout, parce qu'il adaptera automatiquement ce que je tape et implémentera l'espacement approprié au besoin alors que je tape.

Donc ce que nous allons faire est de transformer cela en un composant Auto Layout.

Et la section suivante du cours passera en revue spécifiquement Auto Layout pour implémenter ces composants, ce qui doit être couvert séparément, je crois, parce que c'est beaucoup de contenu à consommer.

Et comprendre, fournir la nomenclature ici pour ce composant en le calquant en conséquence en le nommant dans le panneau Calques en conséquence.

Et ensuite aussi utiliser les trucs et astuces pour créer les composants eux-mêmes peut prendre un peu de temps.

Donc nous allons spécifiquement nous concentrer là-dessus et les contraintes au besoin.

Donc je vais en fait centrer ceci et m'assurer que cela colle à gauche et à droite mais encore une fois, rappelez-vous que quand nous finaliserons la publication de ces composants, nous allons utiliser Auto Layout.

Et nous n'utiliserons pas ces contraintes sont uniquement utiliser les contraintes pour la pratique de comprendre les contraintes, dont vous serez des maîtres une fois que nous aurons construit tous ces composants interactivement ensemble.

Donc c'est tout ce que j'ai.

La dernière chose est d'organiser et de publier ceci donc.

Donc maintenant que nous avons tout ceci organisé et publié, eh bien, maintenant nous devons l'organiser puisque nous avons ces composants principaux.

Donc ce que nous pouvons faire est, avec ce bouton d'action flottant régulier ici, nous pouvons aller de l'avant et spécifier cela s'assurer que c'est aligné en conséquence, nous pouvons changer, excusez-moi, l'espacement au besoin.

Oups, je vais aller de l'avant et glisser ceci ici.

J'ai cela réglé à 16.

espacement entre les types réglé à 72.

Et je vais aller de l'avant et glisser ce dernier bouton ici et changer ceci s'assurer que c'est réglé à 16.

Et nous avons maintenant nos trois variantes de bouton ici pour les boutons d'action flottants, comme dirigé ici par les spécifications spécifiées sur le site web Material Design.

Donc c'est ce que nous venons de créer.

Et vous pouvez aller de l'avant et lire le contenu de cette page web, qui est accessible dans notre fichier d'exercice juste ici en bas, vous cliquez juste sur ce lien, sélectionnez Ouvrir le lien.

Et cela ouvrira cette page pour vous.

Et vous serez prêt à partir.

Et encore une fois, je vais garder ceci ici court et doux.

Merci beaucoup d'avoir regardé.

Dans les autres vidéos, vous remarquerez que nous publierons en fait ceux-ci dans le, vers notre fichier de système de design material dans son ensemble.

Mais je vais garder cela pour la fin.

Donc nous pouvons faire cela tous ensemble en une seule fois.

Ainsi, vous n'êtes pas votre tête n'est pas en train de changer de contexte entre les types, les deux processus séparés, qui est la construction de ces composants, et ensuite l'organisation et la publication des composants.

Aujourd'hui, nous allons parler de la construction de juste quelques boutons génériques.

Et si vous cliquez sur le lien ici dans nos ressources, nous pouvons aller de l'avant et accéder à la documentation des boutons, je recommande totalement de parcourir tout cela en profondeur, mais nous allons principalement nous concentrer sur la construction de ces boutons.

Et ce que vous remarquerez est que nous avons aussi un autre champ interactif ici, un petit terrain de jeu agréable pour nous de voir ce que nous allons construire.

Et aussi nous allons parler de, nous avons les différentes variantes.

Ici, nous avons le bouton Contained (contenu), nous avons le bouton Outlined (contour), et nous avons le bouton Text (texte).

Et tous ces boutons ont aussi une icône de tête (leading icon).

Donc ils ont tous ce type aussi.

Donc nous avons trois, trois variantes régulières.

Donc nous allons créer bien là.

Et ensuite nous avons aussi chacune de ces variantes avec une icône de tête.

Donc nous allons créer six types de boutons aujourd'hui.

Et comme vous pouvez le voir, il y a aussi des états associés avec cela, que nous couvrirons plus tard dans la section différente du cours.

Et ce que nous pouvons faire est juste, nous avons toutes les spécifications ici.

Donc nous pouvons aller de l'avant et vérifier les spécifications pour voir les dimensions de comment construire réellement ces boutons.

Et un écran Ouais, j'ai toutes les captures d'écran ici, j'ai les cinq variantes.

Et notez que toutes ces variantes ont une avec une icône de tête, que nous prendrons en considération, ce qui est pourquoi nous vérifions la documentation.

Comme vous pouvez le voir ici, ils ont aussi des icônes de tête.

Donc je peux aller de l'avant et juste faire une capture d'écran de ceci aussi si je voulais.

Et je peux aller de l'avant et coller ceci sur mon canevas, et cliquer sur chaque type et juste faire une capture d'écran de tout cela et pour tous vous utilisateurs Mac là-bas.

Si vous maintenez Ctrl+Shift+Command+4, cela vous permettra de prendre une capture d'écran rapide de votre interface, et ensuite vous pouvez la coller dans le canevas et Figma.

Et maintenant j'ai toutes ces variantes.

Et nous allons aller de l'avant et commencer avec le bouton contenu.

Et puisque Auto Layout était super facile à implémenter avec ces boutons, nous allons aller de l'avant et couvrir ceci.

Mais Auto Layout sera sa propre section du cours aussi bien que créer ceux-ci, ceux-ci créer ces composants avec juste la seule compréhension de comment les construire et utiliser les styles de couleur et ainsi de suite est consommateur de temps en soi ce qui est pourquoi il y a une autre section dans le cours pour juste Auto Layout et l'ajout d'Auto Layout à ces composants que nous construisons actuellement.

Donc maintenant nous pouvons commencer avec un cadre générique.

Je vais aller de l'avant et frapper cela.

Donc le cadre a une hauteur de 36 dips.

Donc je changerai cela à 36.

Et maintenant que nous avons la hauteur réglée à 36 étapes, je vais aller de l'avant et m'assurer que la couleur d'arrière-plan on primary est spécifiée si nous allons aux effets et allons au remplissage, frapper l'icône de style.

Et une chose que nous devons faire que j'ai oubliée est que puisque ce sont des fichiers d'exercice individuels, nous devrons réactiver la bibliothèque et nous devons réactiver la bibliothèque de système de design material pour accéder à ces styles de couleur.

Donc maintenant que nous avons cela spécifié, je peux aller à mon Phil et j'ai cette bibliothèque ici visible material design system.

Et je vais aller de l'avant et cliquer Sur la couleur primaire, qui est la couleur de l'arrière-plan bouton, et encore une fois, nous allons devoir double vérifier le rayon d'angle de ce bouton, je peux aller, il y a quelques façons que vous pourriez réellement faire cela.

Et le rayon de bordure, je viens de vérifier le code, le rayon de bordure est réglé à quatre pixels là.

Donc je peux aller de l'avant et changer le rayon d'angle ici à quatre pixels.

Maintenant que c'est réglé, vous remarquerez que nous devons ajouter du texte à ceci, une fois que nous ajoutons le texte nous ajusterons la largeur de ce composant.

Donc si je tape, applique le bon style de couleur, va au contenu, et ensuite sélectionne contenu sur primaire, qui est le contenu de sur la surface primaire.

Donc si je tape button, ou applique le bon style de couleur, je veux dire textile, sélectionner le textile bouton, j'ai maintenant button.

Et une chose que j'ai remarquée avec ce style est que nous avions le clic sur le bouton Détails de type et pour s'assurer que la largeur automatique est sélectionnée pour le redimensionnement, ce qui est ce que nous voulons.

Et une chose que je peux faire est de maintenir Option V et H qui centrera ceci horizontalement et verticalement.

Mais cela n'aura pas vraiment d'importance une fois que nous ajouterons Auto Layout.

Donc c'est juste un truc que j'utilise fréquemment pour centrer les éléments au sein du cadre parent, horizontalement verticalement, qui est Option A v.

Donc maintenant que nous avons la côte sélectionnée pour à la fois l'arrière-plan et le texte, je peux aller de l'avant et ajouter Auto Layout.

Donc comment faites-vous cela ? Eh bien, je ne sais pas, cela doit être appliqué aux deux éléments.

Et quels sont ces deux ? Quels sont les deux éléments auxquels je me réfère ? Eh bien, les deux éléments sont le le calque texte ici et ce cadre, et je vais nommer ceci buttons.

Space slash space, et ensuite étiqueter ceci contained button parce que c'est notre bouton contenu.

Et maintenant que j'ai cela correctement étiqueté, je vais frapper Shift+A, ce que cela vient de faire est que cela vient d'ajouter Auto Layout.

Et ce que je vais vouloir faire est que par défaut, Auto Layout ajoute un remplissage horizontal et vertical par défaut, et nous ne voulons pas cela parce que nous voulons que ceci reste verticalement centré.

Donc je frappe juste Option B à nouveau pour centrer verticalement, et ensuite m'assurer que cet Auto Layout réglé sur horizontal.

Et ensuite je vais sélectionner le calque parent et ajouter Auto Layout à cela aussi.

Et je frappe juste Shift+A pour faire cela.

Ou vous remarquez que vous pouvez cliquer sur ce cadre, faire un clic droit et sélectionner Ajouter Auto Layout, ou vous pouvez le faire depuis le canevas aussi.

Je clique sur cela clic droit et sélectionne Ajouter Auto Layout.

Et vous remarquerez que nous avons cela réglé sur vertical.

Donc qu'est-ce que vertical fait si je tape c'est un peu juste le paramètre vertical vous permet de redimensionner ceci verticalement.

Tandis que si je règle ceci horizontalement, je serais en train de changer le je serais en train de redimensionner ceci horizontalement, je veux dire verticalement, désolé pour la confusion là.

Donc si je règle cet Auto Layout à vertical, vous remarquerez que je suis seulement capable de réellement redimensionner la largeur sur l'axe horizontal.

Et si je sélectionne horizontal, je suis en fait seulement capable de spécifier la modification des hauteurs.

Mais cela n'a pas d'importance.

Nous avons déjà notre hauteur spécifiée.

Et reconnaître cela et appliquer le remplissage vertical approprié pour que ce soit cohérent et avec le texte là, donc le centre du Texas.

Et maintenant tout ce que j'ai à faire est de m'assurer que le remplissage le remplissage horizontal n'est pas réglé à 162, ce qu'il est, comme vous pouvez le voir là.

Et c'est réglé à 16.

Donc je dois juste changer cela à 16.

Maintenant qu'est-ce qu'autolayout fait, j'ai ce bouton maintenant.

Et si j'utilise ce bouton, si je tape hello et juste continue de taper, cela ajuste automatiquement le remplissage.

Donc c'est ce dont nous avons besoin, cela vous fera gagner beaucoup de temps en tant que en tant que designer, c'est une fonctionnalité très utile.

Donc avec cela créé, la seule chose manquante si vous faites très attention, il y a des données d'élévation à ces boutons, et nous pouvons aller de l'avant et référencer la documentation Material Design une fois de plus.

Et ce que nous devons faire est d'aller de l'avant et d'accéder à l'environnement, bonne élévation, et cliquer sur dépeindre l'élévation pour défiler vers le bas un peu.

Et nous allons aller de l'avant et chercher ce diagramme.

Et ce que vous verrez est que nous devons trouver nos boutons et notre bouton contenu vit sur l'axe de deux dips pour l'élévation, et quand il est pressé, il monte aux huit dips, ou huit pixels et l'axe d'élévation.

Donc nous pouvons aller de l'avant et appliquer le style d'effet deux dips, qui est juste ici.

J'ai le deux dip réglé.

Là.

Donc maintenant nous avons l'élévation appropriée réglée pour ce bouton.

Et nous sommes prêts à partir avec ce bouton.

Et nous pouvons aller de l'avant et même créer cela comme un composant principal.

Maintenant nous avons ce composant principal réglé.

Maintenant nous pouvons créer l'autre composant principal, qui est un bouton contenu avec une icône de tête.

Et vous remarquerez que cette icône est réglée à 18 par 18 pixels.

Mais nous pouvons aussi double vérifier pour aller à nos boutons, cliquer sur l'icône de tête, nous pouvons inspecter le code reçu dans Command, Shift+C, pour voir ce bouton, je peux décomposer ceci et essayer de voir les spécifications de ce bouton.

Mais si c'est trop difficile pour vous, alors ne le faites pas.

Mais c'est une façon de regarder ces spécifications.

Mais nous avons déjà cela déjà.

Donc j'espère que je ne vous ai pas confus, fournissant juste quelques trucs et astuces techniques sur comment analyser les choses si vous êtes suspicieux qu'elles ne soient pas faites correctement.

Donc j'ai maintenant enlevé l'Auto Layout et le détaché l'instance.

Donc je peux aller de l'avant et redimensionner ce composant en conséquence.

Donc j'ai besoin de huit pixels entre mon icône et le texte.

Donc ce que je peux faire est en fait d'utiliser des contraintes ici, régler cela à droite, et centre sur l'axe vertical droite sur l'horizontal.

Et je peux étirer ceci, et cela maintiendra cet espacement approprié sur la droite à 16.

Et c'est toujours centré, et cela me donne un peu de place pour ajouter la nouvelle icône.

Et tout ce dont nous avons réellement besoin est une icône d'espace réservé.

Donc nous pouvons aller de l'avant et cliquer sur nos actifs.

Vous pourriez littéralement taper ce que vous voulez, j'ai juste tapé star.

Cela peut être n'importe quoi comme cela pourrait être le bouton Ajouter, comme nous l'avons fait dans le bouton Actions flottant.

Et ce que nous pouvons faire est un enlever ce calque de remplissage parce qu'il est inactif, il n'y a pas de but pour cela.

Donc c'est juste confus.

Et nous pouvons cliquer sur contenu et sélectionner on primary.

Et si ça va être sur notre style de couleur on primary surface, cet arrière-plan.

Et maintenant, ce que nous devions faire est d'échelonner cela à 18.

Par 18, tout ce que j'ai fait était que j'ai maintenu Option+Shift, ce qui échelonnera proportionnellement cela vers le bas alors que je glisse les poignées vers le bas, je peux plomber ceci dans mon calque et m'assurer que c'est verticalement aligné en maintenant Option V.

Puisque je sais que ce n'est pas c'est dans le cadre parent.

Et juste double vérifier l'espacement réglé à 12 dips là.

Donc maintenant je peux aller de l'avant et déplacer cela d'un pixel.

Et ce que je pourrais faire est de transformer cela en un Auto Layout aussi.

Et le cadre parent en un Auto Layout.

Et nous pouvons commencer à spécifier l'espacement entre les éléments.

Donc ce que nous pouvons faire ici est d'enlever ce remplissage initial réglé par Auto Layout ajoute toujours un pixel supplémentaire horizontal et verticalement, ce qui est ennuyeux.

Et nous voulons nous assurer que c'est réglé à 12 sur la gauche.

Cela pourrait être délicat avec Auto Layout, parce qu'il ne nous permet pas de spécifier chaque bord sur sur cette mise en page ici.

Donc cela peut être délicat.

Et encore une fois, nous pouvons couvrir cela dans la prochaine vidéo.

Si c'est trop difficile pour vous.

Ce que je vais faire en fait, puisque nous sommes seulement concentrés sur la construction de ce composant, et pas autolayout est de juste ignorer cela pour que nous obtenions les spécifications parfaites.

Et nous pouvons nous concentrer là-dessus dans la prochaine section du cours.

Donc nous avons cela réglé à 12.

Et je vais déplacer ceci, m'assurer que c'est réglé à huit.

Et m'assurer que le remplissage à droite de ce bouton est réglé à 16.

Donc maintenant que c'est réglé à 16, et dans le cadre parent est réglé à huit de la droite et gauche 12 sur la gauche.

Ce bouton a été construit correctement.

Donc une fois que c'est construit correctement, je vais juste impliquer que c'est un bouton contenu avec une icône.

Donc ce que nous pouvons faire est de spécifier cela juste là contain button with icon et faire de cela un composant principal.

Maintenant nous avons deux composants ici spécifiés.

Et nous allons aller de l'avant et créer la version contour (outlined) des deux de ceux-ci.

Donc je vais en fait nous faire gagner du temps dupliquer ces deux Une fois que ces deux sont dupliqués, nous savons que ceux-ci n'utilisent pas l'élévation, donc nous pouvons enlever cela.

Et ce que nous allons faire est de maintenir Option Command+B, ce qui détachera ces styles.

Et remarquez que l'un d'eux a Auto Layout, qui est celui-ci.

Donc je vais frapper Option+Shift+A pour détacher cela d'Auto Layout.

Donc c'est juste un cadre, ce qui est ce que nous voulons.

Nous savons que les hauteurs sont réglées correctement.

Et ce dont nous avons besoin est un contour d'une bordure autour de ce bouton.

Donc si je vais de l'avant et tape, outlined button, je vais aller de l'avant, faire la même chose pour celui-ci.

Et je spécifie juste l'espacement sur ceci, m'assure que c'est réglé à 16, je devrais être prêt à partir, tout ce que nous avions à faire réellement est de modifier la couleur et ajouter un contour (stroke).

Donc avec cela dit, Une chose à double vérifier est la hauteur sur ce bouton, la hauteur a été modifiée.

Donc je vais changer cela à 36.

Encore, pour m'assurer que ce contenu est toujours centré.

Donc c'est une chose que nous devrions toujours surveiller alors que nous construisons ces éléments est de s'assurer qu'ils sont centrés en conséquence.

Et alors que nous implémentons ces choses, donc je vais dégrouper cela là qui ne devrait pas être groupé, cela devrait certainement être centré sur notre canevas, toujours réglé à huit, tout, ce, ce bouton a un cadre parce que nous ajoutons un Auto Layout.

Donc quand je détache ces choses j'ai oublié d'ajouter d'enlever ce cadre.

Donc c'est pourquoi cela s'est produit.

Donc maintenant c'est s'assurer que les pixels sont parfaits là.

Donc nous sommes prêts à partir.

Et maintenant je peux aller de l'avant et enlever le style de remplissage (fill) des deux de ceux-ci.

Et ce que nous allons vouloir faire est d'ajouter un contour (stroke) et le laisser à un pixel.

Et pour la couleur de ceci, nous devons aller de l'avant et en fait voir ce bouton contour.

Et vous remarquerez que le bouton contour est réglé aux couleurs on primary.

Mais dans les spécifications, nous nous avons une couleur différente spécifiée, mais c'est bon, donc pour le seul but de construire ces éléments, nous laisserons ce contour à la couleur on primary, bien que cela puisse ne pas être le cas à tout moment.

Donc nous allons de l'avant et cliquons sur le contour, allons au style, sélectionnons on primary, et nous irons et double vérifierons ce bouton et le style de couleur est réglé à on primary aussi.

Donc je peux Command+clic sur ce texte et Command+Shift+clic sur le deuxième ensemble de texte, et ensuite aller de l'avant et sélectionner le style de couleur on primary.

Et je peux faire la même chose avec cette icône de tête ici, m'assurer que c'est réglé à on primer par opposition à on surface.

Donc maintenant nous avons ces deux variantes de bouton et s'assurer juste que l'espacement réglé à 16.

Et c'est verticalement centré, ce qu'il est en maintenant Option.

Et nous pouvons aller de l'avant et renommer ceci de contained button à outline button.

Et maintenant que nous avons cela nous sommes prêts à partir.

Et nous pouvons faire de cela un composant principal.

Vous remarquerez que cela se redimensionne toujours avec tous les paramètres appropriés, ce qui est génial.

Mais faire de cela un composant principal en maintenant Option Command+K.

Et nous sommes prêts à partir avec ce composant aussi.

Je vais aller de l'avant et maintenir Option Command+K.

Donc nous avons ces deux variantes.

Et nous avons seulement trois composants de bouton de plus à faire ensuite.

Donc nous avons nos variantes contenus et nos variantes contour.

Donc nous pourrions même supprimer cet écran.

Nous ne pouvons pas supprimer la capture d'écran.

Mais maintenant nous avons notre bouton texte.

Donc notre bouton est essentiellement juste du texte, mais pour ne pas vous confondre.

Pour ceux d'entre vous questionnant pourquoi nous ne devrions pas juste utiliser du texte pour ce bouton.

Eh bien, quand vous utilisez les états de ce bouton, comme quand vous survolez sur ce bouton, il a en fait quelques paramètres autour de lui.

Donc c'est pourquoi nous devons faire ceci c'est pourquoi ce n'est pas juste un bouton texte réel.

Il a en fait des paramètres transparents autour de lui.

Donc quand vous survolez dessus, ces couleurs apparaissent et vous pouvez voir que c'est en fait encapsulé dans un rectangle.

Donc si nous retournons à Figma nous pouvons créer cette variante et je vais juste dupliquer ce bouton ici.

Pas besoin de s'inquiéter créer à partir de zéro cela rendra vos vies plus difficiles, pas besoin de rendre votre vie plus difficile ou travailler plus intelligemment, pas plus dur.

Et ensuite nous détacherons le style parce qu'il n'utilise pas l'élévation, et nous allons en fait juste enlever le dos la couleur de remplissage, qui est l'arrière-plan et nous allons Command+clic sur le texte et régler ce texte au style de couleur on primary.

Et nous avons maintenant notre bouton texte, je vais étiqueter cela comme text button.

Et la seule différence est, nous devons changer le remplissage horizontal Auto Layout de 16 à huit, parce qu'il y a moins de remplissage, donc si nous cliquons sur ceci, c'est réglé à huit sur la gauche et la droite le remplissage horizontal, et le texte est centré verticalement, et la hauteur de ceci est réglée à 36.

Et la largeur minimale moyenne d'un bouton en termes de sa largeur peut être réglée à 64 pixels.

Donc ceci fonctionnerait un bouton étiqueté A donc, parce que la largeur minimale de celui-ci comme spécifié dans la documentation est doit avoir une largeur min de 64 bits, qui est juste 64 pixels.

Dans ce scénario, nous en avons un réglé à 100 tendances, donc nous sommes prêts à partir.

Et c'est la construction de notre notre bouton texte.

Et ce que je vais faire est que je dois en fait détacher ceci.

Et je vais le renommer text button.

Donc nous avons text button, je vais option command K pour faire de cela un composant principal.

Et nous sommes prêts à partir.

Seule chose manquante est un autre bouton texte avec une icône de tête.

Comme vous pouvez le voir ici est un bouton texte avec une icône de tête.

Donc ce que je peux faire est dupliquer ce bouton ici, ce bouton contour avec une icône de tête, tête signifiant qu'il est devant le texte ici en termes de gauche à droite.

Et je vais détacher cette instance car c'est une partie d'une famille différente.

Et attacher l'instance et m'assurer que le remplissage est réglé à huit sur la gauche et la droite.

Une fois que c'est fait, je dois être très prudent avec mes cadres ici et m'assurer que c'est agréable et propre.

Juste dégrouper ces cadres là.

Donc nous sommes prêts à partir.

Ce que je dois faire est que le remplissage ici réglé à 12.

Et c'est réglé à 16.

Donc je peux réduire cela.

Mais nous pouvons aussi référencer le code ici.

Donc ici, vous pouvez clairement voir que le remplissage est toujours réglé à 12.

Je veux dire huit sur la droite et la gauche la gauche de cette icône, réglé huit et droite avec boutons à huit.

Et ensuite cela maintient toujours cet espacement entre l'icône et le texte comme vous pouvez le voir.

Donc en essayant juste un peu d'inspecter ce code là, cela pourrait me donner une idée générale de l'espacement des éléments.

Donc le remplissage est resté là.

Et nous sommes prêts à partir, allons, je vais juste spécifier cela comme text button, je vais rétrécir en maintenant Command, rétrécir cela à quatrième réglé à huit.

Et ensuite ce bouton est réglé à ses paramètres appropriés.

Donc maintenant que c'est prêt à partir, nous avons juste besoin de le renommer.

Donc c'est un bouton texte avec icône et faire de cela un composant principal.

Et nous sommes prêts à partir.

Les derniers boutons que nous devons créer sont est cette variante toggle buttons (boutons à bascule).

Donc avec cela dit, Ok, donc maintenant avec ce bouton à bascule, ce que nous allons faire est que nous avons trois sections ici, ces il y a trois boutons et ce bouton à bascule.

Et ce sont tous des boîtes réglées à 48 par 48 dips.

Et ensuite il y a un contour entre, nous pourrions appeler cela le contour et ces deux contours ici réglés à un pixel.

Et ensuite il a aussi une bordure autour aussi, qui est un contour.

Donc nous prendrons cela en considération.

Comme nous construisons ceci.

Je vais aller de l'avant et créer un cadre donc nous pouvons juste faire le calcul.

Donc 48 fois trois est 144, nous pouvons spécifier cette largeur à 144 et s'assurer que la hauteur réglée à 48.

Donc nous avons cela et s'assurer que la couleur d'arrière-plan de ce remplissage est réglée à surfaces.

surface.

Et une fois que c'est réglé à surface, nous pouvons aller de l'avant et saisir les nous pouvons saisir des icônes d'espace réservé en ce moment nous ne savons pas si vous voulez entrer dans les détails et trouver celles-ci.

Maintenant nous vous pouvez en accédant à votre bibliothèque d'icônes.

Et en fait ouais, nous pouvons aller de l'avant et faire cela puisque c'est gratuit.

facile à trouver dans notre bibliothèque.

Et nous avons tous les formats nécessaires pour sélectionner pour cet exemple.

Donc je suis juste allé dans notre bibliothèque de système de design material, qui est aussi activée ici.

Et j'ai collé ces trois, et ce que je dois faire est d'ajouter le bon style de couleur.

Donc ajouter enlever le remplissage qui est éteint, qui est caché.

Et maintenant je peux aller à surfaces content, et ensuite on on surface, puisque l'arrière-plan est réglé à surface, et ils sont déjà réglés à 24 par 24.

Et ce que je dois faire est de régler le rayon d'angle aussi.

Donc généralement le noyau de rayon réglé.

Pour ce scénario, c'est réglé à deux.

Et avec cela réglé à deux, nous pouvons aller de l'avant et plomber ceux-ci en conséquence.

Donc cette icône, je vais centrer verticalement, puisque les hauteurs sont appropriées, s'il vous plaît réglé déjà, c'est juste le remplissage est réglé à 12 pixels de la gauche ici et 12 pixels de la droite de ce contour d'un pixel ici.

Et une chose que nous devons faire est d'ajouter une bordure.

Donc ce que nous pouvons faire est d'ajouter un contour et régler cela à triple E, frapper Entrée.

Et c'est déjà réglé à un pixel et nous voulons que ce soit réglé à l'intérieur.

Parce que si nous le réglons à l'intérieur, c'est le bon badigeonnage que nous voulons ou sinon cela le réglera dedans, cela le réglera à l'intérieur du cadre, si nous le réglons à l'extérieur le contour est maintenant en dehors de notre cadre.

Nous voulons que ce soit réglé à l'intérieur puisque c'est ce qui est spécifié ici.

Maintenant que réglé à l'intérieur, je vais créer une ligne qui est d'un pixel et les valeurs hexadécimales sont Triple E ou six E, la valeur x, ensuite juste régler cela à 48.

Et une chose que je vais faire est d'aplatir ceci en frappant command ou Command Shift O, et ensuite je vais frapper option W et cela l'alignera.

Et ensuite je vais juste m'assurer que le remplissage réglé à 12.

Donc maintenant ces icônes ont un remplissage à gauche et à droite à 12 et en haut et en bas.

Et nous pouvons glisser ceci ici, je peux centrer cela verticalement, je peux aller de l'avant et dupliquer ceci.

M'assurer que c'est réglé à 12 aussi.

Donc maintenant réglé à 12 à gauche et à droite.

Et ensuite tout ce que nous avons à faire est de glisser ceci ici et de s'assurer que c'est réglé à 12 aussi.

Donc maintenant c'est réglé à 12 à gauche.

Et droit une chose qui n'est pas correcte ici est cette dernière icône remplissage d'espacement de 10 à gauche, faire cela 12.

Et ensuite nous pouvons étirer ce bouton en maintenant Command sur la poignée droite, déplacer cela deux fois.

Et maintenant c'est réglé à 12 proportionnellement.

Donc maintenant ceux-ci sont tous prêts à partir.

Ce que nous pouvons faire est d'aller de l'avant et d'étiqueter ceci correctement.

Donc nous pouvons étiqueter ceci si nous renommons ce calque buttons, space slash space, étiqueter cela toggle buttons.

Entrée, nous sommes prêts à partir.

Nous pouvons même faire de cela un composant principal en frappant juste option command K, et nous sommes prêts à partir.

Et maintenant nous avons toutes nos variantes de bouton.

Maintenant nous pouvons juste aller de l'avant et les ajouter dans notre fichier au besoin.

Et c'est tout ce dont vous avez besoin d'avoir couvert dans ce cours.

Ou pour cette vidéo, excusez-moi.

Donc maintenant je glisse juste ceux-ci.

Donc je vais mettre en pause et organiser ceux-ci maintenant bareback.

Donc maintenant j'ai tous ceux-ci organisés dans mon calque buttons.

Et ils sont nommés en conséquence.

Aujourd'hui nous allons aller de l'avant construire des composants carte.

Et et nous allons obtenir un aperçu et une compréhension de l'utilisation pour l'utilisation et le besoin de cartes, quand les utiliser et comment construire ces cartes en utilisant les composants que nous avons déjà faits.

Donc nous pouvons aller de l'avant et commencer par ouvrir notre modal de bibliothèque d'équipe ici, et nous devons activer notre système de design material.

Et ensuite nous avons accès à la documentation des voitures ici dans ce fichier d'exercice.

Donc si nous allons de l'avant et ouvrons ce lien, ce que vous verrez est que les cartes contiennent des actions de contenu sur un seul sujet.

Et ici nous avons une excellente démo interactive, montrant les types de cartes.

Il y a plusieurs options pour la carte élevée, et ensuite il y a aussi une carte contour et dans notre fichier Figma.

Nous allons aller de l'avant et construire Quatre variantes, trois d'entre elles sont élevées.

Donc le type élevé ici vous pouvez voir, au sein de ceci il y a une ombre portée étant utilisée ici sur cette variante élevée.

Et ensuite sur la variante contour, c'est littéralement juste un contour par opposition à l'utilisation d'une ombre portée.

Donc ce sont les différences entre les deux types de cartes.

Et les deux de ces deux types de cartes, le type élevé et le type contour, ont des options avec média texte de soutien, et boutons, et vous pouvez mélanger et assortir ceux-ci allez-y et jouez avec ceux-ci familiarisez-vous avec ce qui est possible avec ces types de cartes.

Et il y a beaucoup d'excellent contexte autour de comment utiliser les cartes et les cartes sont techniquement des surfaces qui affichent du contenu et des actions sur un seul sujet.

Et elles devraient être faciles à scanner pour des informations pertinentes et actionnables, des éléments comme texte et images.

Comme vous pouvez le voir, dans la démo interactive, il y a le texte et l'exemple d'image.

Et nous avons quelques actions pour quelques boutons sont spécifiquement à propos de ce sujet unique dans la carte.

Et voici quelques principes où cette carte est contenue.

Elles sont identifiées comme une seule unité contenue, elle est indépendante et peut se tenir seule sans compter sur les éléments environnants pour le contexte.

Et c'est individuel, une carte ne peut pas fusionner avec une autre carte ou divisée en plusieurs cartes.

Et ici nous avons une décomposition de l'anatomie.

Et ici, comme vous pouvez le voir, le le conteneur de carte est le seul élément requis dans une carte.

Tous les autres éléments montrés sont optionnels.

Donc ce conteneur ici est le détient tous les éléments de panier.

Et c'est en fait le seul élément requis.

Donc ce que cela indique est que les mises en page de carte sont variées pour supporter les types de contenu qu'elles contiennent.

Et c'est vraiment spécifique sur vos besoins quand quand vous construisez des cartes.

Donc quand vous essayez d'implémenter ceci comme un système dans Figma, toutes ces variantes optionnelles devraient en fait être leurs propres éléments quand vous les publiez.

Donc vous pouvez alors commencer à construire votre dans votre propre carte individuellement.

Donc elle a toute la fonctionnalité définie.

Parce que si vous créez juste ces cartes spécifiques, peut-être qu'il y a certaines choses dont vous n'avez pas besoin de cela, que vous devrez enlever, par conséquent, nécessitant de créer la vôtre à partir de zéro, ce qui est pourquoi nous voulons la construire à partir de la base en utilisant des éléments par opposition à refactoriser une qui a déjà été construite.

C'est plus modulaire dans ce sens.

Voici quelques excellentes, vous savez, décomposition de l'utilisation du comportement et ainsi de suite.

Et j'ai saisi ces captures d'écran des spécifications.

Et ce que j'aime vraiment à propos des spécifications est que cela déclare pour les cartes, est que la section ne devrait pas être lue comme prescriptive, ou, ou exhaustive, ou aussi définie, ces cartes n'ont pas de mise en page singulière, type de graphique ou taille d'image.

Donc et Donc rien de tout cela n'est extrêmement spécifié.

Donc ce qu'ils essaient de déclarer est que c'est conçu pour répondre aux besoins du contenu qu'ils présentent.

Donc, donc le contenu que le designer essaie de présenter.

Donc c'est flexible dans ce sens que vous pouvez construire une carte selon vos besoins.

Et cela montre une variété de mises en page qui aident à montrer à quel point c'est flexible C'est vraiment.

Donc nous allons aller de l'avant avec cela dit, sauter dans Figma.

Et maintenant que nous sommes dans Figma, nous allons aller de l'avant et créer le premier type de carte.

Et une chose importante à ce sujet est que l'élévation pour l'état reposé d'une voiture est réglée à un dip.

Donc dans sous mon sous l'élévation ici dans les directives material design, il y a un tableau de valeurs par défaut, que j'ai déjà passé en revue quelques fois avant, et cela montre que la carte à l'état reposé est réglée à un dip sur la droite là.

Et quand elle est ramassée, quand cette carte est en train d'être interagi avec ou ramassée, elle utilise la valeur d'élévation par défaut de huit dip.

Donc juste juste une note latérale là, parce que nous aurons besoin de savoir cela pour implémenter la portion élevée des cartes que nous construisons.

Donc avec cela dit, allons-y et arrivons à craquer sur cette carte élevée vôtre.

Donc nous avons est un titre.

Mais nous allons aller de l'avant et définir le cadre ici.

Donc nous avons le style de couleur d'arrière-plan de surfaces surface ici, donc c'est juste blanc, et les coins arrondis sont réglés à quatre ou en fait cela réglé à huit.

Et nous allons aller de l'avant et copier le nom de ceci.

Donc j'ai déjà nommé ceux-ci.

Donc ces cartes vivent sous la catégorie élevée et cela a un titre, une certaine copie, copie de corps, une image et des actions, qui est tout déclaré là.

Donc je vais cliquer sur cela renommer ce calque, ou minaret cadre.

Et maintenant nous pouvons aller de l'avant et spécifier la largeur et la hauteur de ceci recherche réglée à 344 dips en termes de largeur 148 dips et hauteur.

Maintenant que nous avons cela spécifié le Le plus je regarde ces Quartier ce quartier car il devrait être réglé à quatre.

Maintenant que nous sommes prêts à partir, cela semblait juste différent quand nous ne l'avons pas redimensionné à ses dimensions appropriées, ce qui est bien.

Donc maintenant ce que nous savons est que cela utilise deux boutons.

Et nous pouvons tirer une image d'espace réservé de nos actifs.

Pour comprendre ce qu'avec notre bibliothèque de système de design material activée, nous pouvons aller de l'avant et chercher dans notre panneau d'actifs le type QA, et je peux juste taper placeholder et voilà.

Je peux aussi utiliser cet espace réservé d'icône comme un espace réservé d'image.

Donc si je glisse ceci ici, je peux régler la largeur et la hauteur là pour ajouter des dips.

Et ensuite je peux m'assurer que je positionne ceci correctement, par 16, dips en haut sur le haut et la droite, et je vais sûr régler les contraintes à haut et droite pour que cela colle, cela reste cela maintient cet espacement sur le haut et la droite quand redimensionné.

Maintenant nous pouvons aller de l'avant dans notre panneau d'actifs et chercher des boutons.

Et ici nous avons la variante de bouton texte, tout ce que nous pouvons faire est d'étiqueter ceci action un.

Et je peux sélectionner ceci à nouveau et juste régler l'espacement correctement.

Donc cet espacement est réglé à 16 depuis le début de ce texte.

Donc ce que cela signifie est que je sors mes règles et j'ai déplacé ceci de 16 pixels.

En ce moment c'est 16 pixels à la gauche ou dips à la gauche de du cadre.

Mais il veut que la typographie soit le début du texte à 16 dips loin.

Donc ce que je peux faire avec cet espace correctement, en ce qui concerne la boîte englobante du bouton, je peux ajouter cette règle ici.

Et avec cette règle, je peux aller de l'avant et pousser ce texte vers l'intérieur.

Donc maintenant ce texte est 16 dips à la gauche de du cadre parent là.

Et ensuite je peux aller de l'avant et juste dupliquer ceci et c'est réglé à huit dips à la droite, la deuxième action ici le deuxième bouton, ou nous étiquetons cela action deux.

Et nous devrions être bons.

Et maintenant nous avons juste besoin d'ajouter dans notre copie de corps et un titre.

Donc ce que je vais faire est de sortir mon texte ici, m'assurer que c'est réglé à texte et style de couleur text and iconography, qui a eu une haute emphase et je vais étiqueter ceci title oups, je vais sélectionner le bon textile.

Et cela devrait être réglé à un voyons ici, sous-titre un j'ai actuellement spécifié.

Donc le titre va ici.

Et avec cela spécifié, je vais m'assurer que le type dans les détails de type le redimensionnement est réglé à largeur automatique, donc cela s'aligne en conséquence, et adhère à la bonne hauteur de ligne spécifiée dans notre système de type.

Et je vais utiliser mes touches de raccourci option w n A pour aligner au haut et à gauche, et ensuite pousser ceci deux fois, et vers le bas deux fois.

Donc j'ai, donc j'ai remplissage haut et gauche réglé à 16 parce que j'ai modifié mon montant de coup de pouce à huit sur le petit coup de pouce par opposition à mon grand coup de pouce.

Donc j'ai inversé ceci, je vous recommande fortement de modifier votre jugement à cela pour que vous n'ayez pas à le déplacer incrémenté par un tout le temps.

Puisque ce système est divisible par huit, je peux juste le déplacer par incréments de huit chaque fois que j'utilise les touches fléchées, ce qui est très efficace.

Donc je vais dupliquer ce style ici.

Et ce que nous avons ce que nous voyons ici est notre zone de texte devrait, spécifions le corps à corps un là wo deux, corps deux, et texte à corps deux et ensuite aller de l'avant et appliquer emphase moyenne au style de couleur.

Et avec cette emphase média appliquée, je vais juste copier ce qui est écrit dans ce composant de spécification, secondary line text lorem ipsum.

De lor, sit omit.

Pas sûr si c'est réellement un mot.

C'est bon.

Et maintenant que j'ai cela spécifié, je vais pousser ceci vers le haut huit pixels.

Et ce que je veux m'assurer est que la zone de texte est 16 pixels à la droite de l'image en ce moment c'est réglé à 21.

Donc je peux aller de l'avant et augmenter cela de cinq.

Et maintenant c'est réglé à 16.

Ce que je peux faire est de régler les contraintes à haut gauche et droite et bas si besoin est.

Et ensuite, comme vous pouvez le voir ici, nos boutons sont huit dips du haut de cette boîte englobante de texte bond et tout est divisible a les bonnes mesures et ainsi de suite donc c'est fantastique.

Maintenant tout ce que nous avons à faire est juste de double vérifier nos paramètres ici, les choses sont réglées à 16.

Et nous sommes prêts à partir, nous avons maintenant créé notre première carte, en fait, la dernière chose que nous devons faire est d'aller de l'avant et aller à nos effets et appliquer cette élévation.

Donc ça à un dip.

Et maintenant nous sommes prêts à partir.

Donc nous avons créé notre première carte.

Et nous pouvons un peu double vérifier certaines choses et voir si cela utilise un Sous-titre différent en référençant la documentation de materials.

Donc si nous allons à nos spécifications et défilons juste vers le haut un peu, cela vous dira il, le titre utilise en fait un h6 et il utilise le corps un.

Donc si je dis si j'ai sélectionné corps un, oups.

Mais c'est pour un certain thème.

Donc prenez juste note de cela, que nous devrions adhérer aux styles étant utilisés et référencés si, même si les propriétés peuvent être différentes dans un autre thème, cela utilise toujours ces ces styles.

Donc maintenant je vais aller de l'avant et changer le sous-titre à un âge six.

Et c'est prêt à partir.

J'ai maintenant tout attaché en conséquence.

Et ouais, nous sommes bons.

Donc apparemment, ceci utilise juste Corps Corps un et mettait pour les métadonnées, cela utilise corps deux.

Donc allons-y et modifions ceci en conséquence.

Et maintenant que nous avons modifié cela notre carte devrait être prête à partir.

Mais ça ne ressemble pas en fait à ce qui est un textile approprié, cela devrait être plus petit la police, donc nous le laisserons tel quel.

Et nous allons aller toutes les contraintes et mesures sont correctement réglées.

Et nous pouvons aller de l'avant et dupliquer ceci et publier ceci comme un composant principal.

Donc nous avons maintenant notre premier composant créé.

Et nous pouvons même aller de l'avant et créer une autre version de ceci où c'est en fait une carte contour.

Donc pour la carte contour, ce que nous pouvons faire est ce que nous allons vouloir faire d'abord est d'enlever ce style d'élévation, ajouter un contour, et c'est réglé à un pixel comme un dip, comme vous pouvez le voir ici, un dip, et la couleur réglée à sous surfaces surface overlay.

Et c'est le contour de la la carte.

Comme vous pouvez le voir, là zoomé.

Et avec cela beaucoup de ces propriétés sont en fait les mêmes, mais la hauteur de notre carte est est est plus grande.

Et une chose que j'ai gâchée sur cette carte est que l'espacement en dessous de ces deux boutons devrait être réglé à huit dips au lieu de 16 dips.

Donc je vais aller de l'avant et cliquer sur ceci Maintenir COMMAND alors que je alors que je change ces dimensions ici.

Et maintenant je l'ai réglé à huit morts du bas.

Et cette carte devrait être prête à partir.

Maintenant aller de l'avant et toucher ceci ici.

Je pourrais juste redupliquer ceci.

Donc je ne veux pas modifier les dimensions ou l'espacement là et le détacher en maintenant option command B.

Et ensuite je vais re étiqueter ce calque et enlever cette élévation.

Et nous allons vouloir sélectionner outlined la convention de nommage que j'ai spécifiée ici déjà à l'avance.

Et cette convention de nommage déclare clairement quel type de carte C'est.

C'est une carte contour avec un surlignement, un titre, qui inclut le sang de copie de corps, et ensuite une image et quelques actions étant ces actions étant nos boutons.

Donc maintenant je vais aller de l'avant et réappliquer ce style de couleur de contour, qui est surfaces surface overlay.

Et c'est réglé à un dip ou pixel.

Et ce que nous allons faire est d'augmenter la hauteur de cette carte très vite.

Et nous allons avoir besoin de pousser ce contenu vers le bas parce que la ligne de base de ce titre ou cet en-tête est 40 dips loin de la ligne de base du texte de surlignement.

Donc ce que je peux faire est juste de pousser ce contenu vers le bas, dupliquer ce textile, ou ce texte et ensuite le changer à overline avec surcharge spécifiée.

Je vais juste écrire oh line.

Et ensuite je vais m'assurer que c'est 16 dips du haut, ce qu'il est.

Donc maintenant que nous avons notre surlignement spécifié, je vais aller de l'avant et m'assurer que la ligne de base est 40 dips loin de, de la typographie ici du du titre ici, et ce titre utilise un h5.

Donc c'est légèrement plus grand, comme comme vous pouvez le voir.

Maintenant je vais aller de l'avant et double vérifier, ajouter un peu, ajouter cette ligne rouge à la première ligne de base, ajouter une ligne rouge à la deuxième ligne de base au titre ici, qui est je vais l'appeler titre cinq.

Et ensuite je vais saisir un carré et juste calculer cela manuellement.

Donc c'est actuellement réglé à 41.

Donc nous voulons faire nous étions assez proches, pousser cela vers le haut un par défaut.

Et maintenant c'est réglé à 40.

Juste là, comme vous pouvez le voir, ce qui est exactement ce que nous voulions atteindre.

Donc c'est fantastique.

Je peux avoir mes règles en appuyant sur shift R.

Et nous sommes prêts à partir à cet égard.

Donc allons-y et fermons cet espacement du titre et ce texte.

Et cette ligne de base du titre est 24 dips au-dessus de la ligne de base de cette copie de corps.

Donc nous pouvons aller de l'avant et faire le même processus ici.

Et juste ajouter une autre ligne rouge ici à cette copie de corps, saisir un rectangle et s'assurer que cela est tout fait correctement et a actuellement une hauteur de 27.

Donc nous allons vouloir faire est de pousser cela vers le haut à travers quelques pixels et s'assurer que c'est réglé à 24.

Maintenant, la ligne de base n'est pas 24 pips loin de la ligne de base du titre, l'en-tête cinq, spécifiquement, h5 et nos textiles là.

Et nous allons aller de l'avant et double vérifier notre espacement entre la copie de corps et les boutons.

Et cela pour une raison quelconque n'est pas spécifié dans notre spécification, mais c'est spécifié ici dans ceci, donc il peut sembler que c'est réglé à 16 pixels en dessous de la typographie et ensuite en dessous des boutons eux-mêmes.

Je vais de l'avant et renomme ces boutons à buttons de comme être confus entre les types de boutons dans l'autre carte, je peux aller de l'avant et double vérifier ces éléments et les pousser.

Donc le remplissage à gauche est réglé à 16 maintenant donc c'est plus cohérent.

Et vous remarquerez que les les boutons réellement poussés dedans maintenant dans le type de boutons n'est pas aligné avec le type de la copie de corps juste là.

Donc c'est important de prendre note de cela, ce sera lent, cela apparaîtra visuellement légèrement indenté, ensuite je peux changer l'espacement entre les deux boutons à huit dips encore comme comme cela devrait être un dips là, et ensuite huit dips en dessous des boutons.

Donc maintenant je vais aller de l'avant et juste saisir cette voiture pour maintenir Command et tirer ceci vers le haut.

C'est actuellement réglé à neuf dip smoothie en dessous.

Donc si je pousse cela vers le haut un pixel de plus, nous sommes prêts à partir.

C'est maintenant huit dips en dessous et maintenant tout est à la spécification comme besoin est rivière surlignement le titre et la copie de corps et l'image que nous pouvons remplacer ici dans le style de remplissage.

Et juste sélectionner une image là.

Donc quand les designers dupliquent ceci, et ensuite nous avons nos actions qui sont des boutons.

Donc maintenant que c'est fait, c'est fantastique.

Nous allons aller de l'avant et créer notre prochaine carte.

Donc obtenu cela comme le composant principal maintenant.

Ensuite, nous allons aller de l'avant et aborder ce composant plus complexe et et ce que nous allons avoir besoin de faire est que nous avons réellement besoin de ce composant ici nous avons cet ensemble d'étoiles donc étoiles dans la spécification, je vais ignorer cela de ce composant parce que j'ai en fait quelques objectifs pour le ce composant en particulier que je veux utiliser plus tard.

Donc je vais construire sans les étoiles parce que je n'ai pas besoin de communiquer les ces évaluations.

Et ce que je peux faire est de créer cette variante année, spécifier la largeur à 344 dips et la hauteur 510 dips et le rayon d'angle à quatre.

Ceci est une voiture élevée.

Donc je vais aller à mes effets et appliquer l'élévation d'un dip, ensuite aller à mon Phil et sélectionner le style de couleur surfaces surface.

Et ce que cela est lié, je vais aller de l'avant et juste m'assurer que j'ai le bon nom pour ce composant dans mes composants et ensuite nous avons un espace réservé d'image comme vous pouvez le voir ici, je peux juste saisir l'espace réservé que nous avons dans notre système et spécifier la largeur à 344 dips, et ensuite la hauteur 294.

Et ensuite maintenir Option W et a pour aligner cela correctement dans notre composant au besoin.

Et ensuite nous réglerons les contraintes à haut gauche et droite, de cette façon quand cela s'étire à besoin d'être étiré, cela ne devient pas tout bizarre.

cela s'alignera à tous les bords correctement, donc cela semble propre.

Et avec cela dit, nous avons un titre qui est 44 dips, la ligne de base de ce titre est 44 dips depuis le haut de cette image.

Donc si je vais de l'avant et ajoute ce titre ici, ensuite appliquer le bon style de texte de sous-titre un.

Ou en fait, c'est le titre h5, je crois.

Voilà.

Et maintenant je vais régler sélectionner le redimensionnement et régler cela à largeur automatique, je vais pousser ceci vers le bas et pousser cela vers le bas un peu, pousser cela à 30.

et double vérifier la ligne de base.

Donc la ligne de base depuis l'image devrait être réglée à 44, ce qui est en fait juste ici.

Donc c'est en fait 24.

dips depuis le haut de l'image, avec la ligne de base étant 44 dips depuis le haut.

Et maintenant je veux ignorer ces étoiles ici.

Et même, je peux ajouter du texte secondaire.

Donc au texte secondaire, je vais utiliser les textiles de légende.

Si je duplique ceci, change le style de texte et vais à légende, je peux sélectionner cet ensemble, régler cela à texte secondaire.

M'assurer que c'est 16 Dibs depuis la gauche du conteneur de la carte.

Et je vais m'assurer que les deux ces styles de remplissage sont réglés à text and iconography.

Haute emphase.

Et une fois que cela est fait, je vais aller de l'avant et dupliquer ce textile secondaire, le pousser vers le bas et étirer la zone de texte pour qu'elle soit 24 morts de la droite du conteneur du conteneur de voiture.

Et avec cela, ça va pousser cela sur trois notes réglé à 24 de la droite aux contraintes, le haut gauche et droite.

Et ensuite je vais juste ajouter cette copie de corps qui est déjà dans cette carte.

Et je vais mettre en pause ça très vite.

Cette typographie spécifiée, vous remarquerez qu'elle utilise un diviseur aussi.

Donc nous pouvons même tirer dans notre composant diviseur que nous avons créé un diviseur là, tirer cela, et vous remarquerez que c'est 16 a un remplissage de 16 dips à gauche et 20 et 16 dips à droite donc nous pouvons apporter et nous pouvons faire le calcul nous voulons régler la largeur de ce composant est 344.

Et ensuite moins 32 est 312.

Donc nous pouvons changer la largeur de ceci au diviseur à 312.

Donc quand nous l'apportons dans notre composant, et c'est un peu difficile à saisir.

Donc je peux juste aller à mon panneau Calques et le glisser dedans si j'ai besoin.

Et ensuite maintenir Option H et cela l'alignera horizontalement et ensuite option v pour l'aligner verticalement, l'alignement correctement et je peux pousser ceci vers le bas et m'assurer que c'est 24 dips depuis la ligne de base de la deuxième ligne de base de texte dans ce corps copie de corps.

Donc si je pousse ceci vers le haut, j'ai besoin de m'assurer que c'est au 24 donc si je saisis une zone de texte, je peux mesurer 24 dips depuis le bas.

J'étais approximatif.

Presque là.

J'étais proche.

Donc Maintenant que cet ensemble à la ligne de base est 24 dips loin.

Donc je vais pousser ceci vers le bas sur plus.

Oups, je vais saisir ce diviseur, le pousser vers le bas d'un pixel de plus, et c'est depuis, depuis la zone de texte.

C'est sur cette copie de corps, c'est réglé à 20.

Donc c'est bon à noter.

Et nous devons changer la couleur de ce texte, la copie tachetée de haute emphase à emphase moyenne.

Et maintenant c'est précis.

Avec ce diviseur implémenté, nous pouvons aller de l'avant et ajouter une autre légende, nous sommes en fait c'est un sous-titre.

Donc je peux dupliquer ceci, et pousser ceci vers le bas un peu, l'étiqueter subtitle, ensuite juste changer le style de texte à subtitle.

Maintenant que nous avons le sous-titre doit aimer le sous-titre 2 utilise un sous-titre plus petit on dirait juste pour maintenir la hiérarchie là.

Comme ceux-ci comme sous-titre un, je crois, et ensuite juste s'assurer que l'espacement est approprié.

Donc c'est la ligne de base est 36 dips depuis le diviseur, donc nous pouvons aller de l'avant et mesurer cela.

Depuis ce diviseur.

Actuellement, nous l'avons 41 dips loin, donc je peux pousser cet élément vers le haut.

Et maintenant nous avons ce 36 étapes loin du diviseur, ce qui est génial.

Et je vais aller de l'avant et ajouter quelques composants puce (chip).

Donc nous avons quelques puces d'action étant utilisées ici.

Donc si je tape puce d'action, ou juste en fait puce dans notre panneau d'actifs, je peux glisser une puce dedans.

Et ce que je vais faire avec cette puce est que je peux la dupliquer quelques fois, n'est-ce pas, et elles sont espacées de huit dips l'une de l'autre.

Donc je vais jeter trois puces ici dedans.

Et elles sont, elles sont toutes étiquetées différemment article un.

Une chose que nous devons nous assurer est que ces puces utilisent auto layout, et on ne dirait pas qu'il utilise auto layout en ce moment.

Parce que j'avais besoin d'ajouter auto layout à mes puces parce qu'elles ne s'adaptaient pas à la taille du texte.

Donc maintenant si je vais dedans et tape article un, cela maintiendra l'espacement approprié à gauche et à droite.

Et ici vous pouvez voir que nous avons quatre puces.

Donc allons-y et sélectionnons celles-ci.

Ici nous avons article 123, et 4.

Donc je vais juste étiqueter celles-ci en conséquence.

Et maintenant, je peux aller de l'avant et juste restructurer l'espacement là, m'assurer que ce sont tous huit dips à part.

Et je vais aller et glisser et déposer ceci dans mon composant v ici.

Et cela spécifie la ligne de base 14 dips loin du haut de la puce.

Et je suppose que c'est en fait huit dips loin de de la boîte englobante et la typographie, je peux aller de l'avant et double vérifier cela.

Et techniquement c'est la ligne de base ici est 15 pips loin, mais nous allons aller et maintenir l'espacement depuis le haut du sous-titre et garder cela à huit.

Et maintenant que nous avons cela spécifié, tout ce qu'il nous manque est une action en dessous, qui est 20 étapes loin de la puce.

Donc si je vais de l'avant et vais à mes actifs et tape dans mon panneau d'actifs, tape bouton, cherche ce bouton.

Ça n'apparaît pas.

Donc si je vais de l'avant et re tape cela et cela cherche et je peux saisir ce bouton texte et juste glisser cela dans le canevas.

Je peux juste renommer ceci à action un.

Et une fois que cette action est renommée, je peux aller de l'avant et la glisser dans mon nouveau composant carte et m'assurer que l'espacement est réglé en conséquence.

M'assurer que c'est réglé à 20.

C'est indiqué dans la spécification ici 20 loin et c'est huit chiffres pixels loin le cadre extérieur du bouton est huit dips loin du conteneur parent parce que cela alignera la typographie avec une puce ici vous voyez cela c'est pourquoi ce bouton est huit dips loin parce qu'il aligne la typographie du bouton avec le reste du contenu dans la carte.

Et ensuite j'ai juste besoin de spécifier que c'est huit dips en dessous de l'espacement.

Donc je peux saisir le conteneur parent maintenir Command alors que je glisse vers le haut, m'assurer que c'est réglé à huit, en ce moment nous l'avons à cinq.

Donc juste pousser ceci vers le bas trois pixels, et nous sommes dorés.

Génial.

Donc nous avons maintenant créé une des cartes composants les plus complexes dans material design un des exemples encore, donc je vais aller de l'avant et vous mettre au défi de créer ce composant voiture par vous-même.

Et ensuite je vais mettre la vidéo en pause et vous montrer l'optimale, façon optimale de construire ces composants voiture.

D'accord, je vais mettre en pause.

Donc j'ai maintenant fini de créer tous les éléments, j'ai créé cette variante ici, la réplique exacte, et je l'ai fait un peu différemment cette fois.

Et la raison pour laquelle je voulais traverser cet exercice de la façon dont je viens de le faire avant que je ne vous montre tout est très intentionnelle, je veux vous montrer le processus manuel de construction de ce composant.

Et ensuite la puissance d'avoir ces éléments que je viens de créer pour, pour utiliser comme blocs de construction pour le système de design, non seulement pour vous-même, mais pour les designers auxquels vous vous adressez si vous travaillez jamais sur une équipe de systèmes de design.

Donc ici, nous ici vous pouvez voir que nous avons créé nous avons manuellement créé nos cartes, voici quelques exemples d'avoir des cartes plus composées.

Et ensuite je suis allé de l'avant pendant cette pause, et non seulement fait ces éléments ici, mais je les ai composés correctement.

Donc quand je dis je les ai composés correctement, ces ce sont tous spécifiquement des éléments pour les cartes, la largeur de ces cartes sont définies par 344, certaines variantes d'entre elles.

Et voici comme, nous les avons étiquetés comme éléments, textiles, et vous pouvez penser à eux comme des carreaux alors que vous, alors que vous ajoutez du carrelage sur un sol, vous pouvez les arranger et les ajouter et les empiler et ainsi de suite.

Donc c'est exactement ce que nous allons faire.

Donc avec ces éléments, je vais aller je peux décomposer ce dont ceux-ci sont composés.

Et ensuite c'est enveloppé dans un cadre avec la bonne couleur d'arrière-plan, qui est réglée à surface, la surface et ensuite l'élévation appropriée, les élévations au repos étant réglées à un dip.

Et ensuite bien sûr, le statut élevé réglé à huit dips là, comme vous pouvez voir les deux différences là.

Et dans ce cadre, si je clique sur ce cadre, vais de l'avant et je vais de l'avant et vérifie.

Oups, je vais de l'avant et vérifie les éléments dans ce cadre, j'ai trois pièces dans ce composant.

Donc je peux glisser celles-ci dehors.

Et notez qu'ils n'ont aucune couleur d'arrière-plan appliquée à eux sauf ceci est une icône, je veux dire espace réservé d'image.

Donc et voyez c'est ce qui est composé de ces trois éléments ici.

Donc c'est super important à noter et comprendre.

Donc utilise ces ces éléments pour commencer à construire et ajouter sur le dessus de l'autre dans la carte.

Et ce sont tous des éléments que vous pouvez avoir dans votre système de design.

Et c'est explicitement.

C'est pourquoi c'est là.

Donc nous pouvons aller de l'avant et construire un exemple.

Donc vous pourriez créer plusieurs exemples de ceci.

Donc nous pouvons commencer avec cet en-tête, je peux copier cet en-tête, et peut-être que l'en-tête a un texte de soutien, n'est-ce pas.

Et ensuite je peux aller de l'avant et ajouter dans comme une image, cette image de soutien au-dessus de l'en-tête.

Donc nous avons le média et ensuite l'en-tête là.

Et ensuite nous avons le texte de soutien en dessous.

Donc ce que je peux faire maintenant que ceux-ci sont tous connectés, je peux les sélectionner tous et ensuite les envelopper dans un cadre, je les sélectionne tous et ensuite je frappe option Command G pour créer un cadre.

Et maintenant je vais cliquer sur la couleur de remplissage, aller à surfaces et sélectionner surface.

M'assurer que j'ai le bon rayon d'angle arrondi que cela les quatre pixels ou dips là, et ensuite cliquer sur rogner le contenu.

Et nous allons aller aux effets et sélectionner un dip sur les styles d'élévation et regarder rapidement, nous avons été capables de construire un composant carte en utilisant des éléments par opposition à aller dedans et s'assurer que tout est parfait au pixel près glisser et déposer des trucs autour.

Donc si vous le faites, si vous construisez ces éléments une fois pixel avec précision pixel perfection, vous devriez être prêt à partir.

Aujourd'hui, nous sommes à une académie de design, et nous allons créer quelques composants puce.

Et donnons juste l'aperçu général de cette vidéo.

Nous allons Faire un aperçu Des composants puce d'abord, comment ils sont utilisés, ce qu'ils sont, et ensuite aussi construire ces composants puce.

Et nous allons aller de l'avant et ouvrir le lien ici dans notre fichier d'exercice pour la documentation des puces.

Et une fois que cela s'ouvre, allez-y et une fois que cela charge, vous pouvez voir que les puces sont des éléments compacts qui représentent une entrée attribut ou action.

Donc ceci est ici dans notre design.

Ceci est notre puce ici comme vous pouvez le voir, et c'est essentiellement dans ce texte Où c'est spécifier à qui envoyer un email.

Et c'est cette personne étiquetée Peyton Smith, nommée pin Smith, excusez-moi.

Et comme vous pouvez le voir, une fois que l'email a été tapé ou le nom d'utilisateur, et il a été sélectionné, il se transforme en une puce.

Et il y a une petite image aussi pour représenter qui est cet utilisateur cette image de profil.

Et avec ce contexte en tête, nous pouvons aller de l'avant et comprendre l'utilisation.

Cela permet aux utilisateurs d'entrer des informations, faire des sélections, filtrer le contenu, ou déclencher des actions.

Tandis que les boutons sont attendus pour apparaître de manière cohérente et avec des appels à l'action familiers.

les décalages devraient apparaître dynamiquement comme un groupe de multiples éléments interactifs.

Et ici vous pouvez voir les principes, ils sont intentionnellement compacts, pertinents, donc ils ont des informations de relais claires et utiles, information en relation avec le contenu ou la tâche qui est représentée dans l'UI.

Et les puces devraient rendre les tâches plus faciles à compléter ou le contenu plus facile à trier.

Et ici nous avons tous les types de puces ici, comme vous pouvez le voir.

Et nous avons une anatomie d'une des puces les plus complexes ici.

Donc nous avons le conteneur générique qui détient tous les éléments de puce et leur taille est déterminée par ces éléments.

Ici vous pouvez voir que nous avons une vignette optionnelle, qui est l'icône de tête ici, qui peut être utilisée pour identifier des entités telles que des profils, en affichant un avatar logo ou icône là.

Et ensuite nous avons aussi le le texte, bien sûr, pour afficher le nom de l'entité, description, étiquette action, ou, ou conversationnel.

Et ensuite le quatrième élément de cette décomposition anatomique est les puces d'entrée peuvent inclure une icône enlever, indiquant que vous pouvez enlever cette puce entière si besoin est.

Et nous où nous avons une décomposition de toutes les utilisations pour les différents types.

Mais nous n'allons pas entrer là-dedans je vous recommande de parcourir et consommer cette information au besoin.

Et ici, nous avons tous les types que nous allons créer.

Mais une chose que je veux que vous notiez est que trois de ces puces sont les mêmes, mais il y a explicitement déclaré comme différentes puces dans cette documentation.

Et je veux juste que nous prenions un peu note de cela et fassions attention.

Donc ici dans les spécifications, nous avons cette puce d'action, la puce contour puce de choix filtre.

Et nous avons les puces d'entrée et les puces, un exemple de puces en groupes où elles ont un espacement de huit dips là entre chaque puce.

Et vous remarquerez que la puce d'action choix et filtre sont toutes la même puce exacte, mais la fonctionnalité sous-jacente pourrait être différente, ce qui est un peu le point auquel je voulais arriver là.

Et avec cela déclaré, nous pouvons aller de l'avant et sauter dans notre fichier finger et commencer à construire ces puces.

Et je vais aller de l'avant, m'assurer que j'ai ma bibliothèque de système de design material activée dans ce fichier d'exercice.

Et avec cela dit, nous pouvons aller de l'avant et commencer à créer ces puces.

Donc avec cette puce créditée, je vais aller de l'avant et créer un cadre.

Et avant que je fasse, je vais vivre copier ce nom, étiqueter ce nom de cadre d'action, parce que cela va être notre puce d'action.

Et je vais aller de l'avant et ajouter la la couleur d'arrière-plan surface sous surfaces overlay.

Et ensuite je vais régler les coins arrondis à 16.

Donc c'est agréable et agréable et rond là.

Et je vais régler la hauteur à 32.

Et ensuite nous allons aller de l'avant et modifier la, la largeur au besoin.

Et la chose agréable est que nous serons capables d'ajouter rapidement sur permet pour ceci.

Donc cela s'adapte dynamiquement à la chaîne de texte en son sein.

Donc vous n'avez pas à le redimensionner manuellement, ce qui est très utile.

Donc je veux aller de l'avant et ajouter ce style de texte ici.

Et en ajoutant ce textile, je peux aller de l'avant et sélectionner le textile body to parce que c'est ce qui utilise les puces.

Et je peux aller de l'avant et étiqueter cette puce d'action.

Et je veux par défaut, mon ma ma typographie pour redimensionner automatiquement.

Et ensuite je vais aller de l'avant et centrer ceci.

Et ce que je vais faire est de maintenir shift a, cela crée auto layout, ensuite je vais frapper shift a à nouveau, ce qui crée auto layout sur le cadre parent.

Et maintenant vous remarquerez que je peux ajuster le remplissage dip à 12 dips la gauche et la droite par opposition à adapter le un ici, qui est ce qui est spécifié actuellement.

Donc si je tape 12, j'ai maintenant rétréci cela à 12.

Et cela dit actuellement 13 parce qu'autolayout par défaut ajoute un pixel supplémentaire horizontalement et verticalement à votre élément, ce qui est ennuyeux à mon avis.

Donc si nous réinitialisons cela vous maintenant cela montrera que c'est réglé à 12 sur la gauche et la droite et est verticalement centré, ce qui est génial sur l'axe y et nous avons maintenant créé notre première puce et nous pouvons aller de l'avant et frapper les deux autres puces ici.

La puce de choix dans le filtre Donc voici quelques choses complexes à comprendre à propos du système de design.

Et voici où les décisions sont prises sur une sur une base par équipe, comme j'aime l'appeler.

Donc nous avons cette puce d'action, n'est-ce pas.

Et il y a trois types de ceci, cette puce d'action où ils ont tous le même aspect visuellement.

Mais la la fonctionnalité sous le capot pourrait être très différente et utiliser dans différents scénarios.

Donc disons que ce composant, construit en code est représenté différemment, est-ce que cela signifie que vous voulez refléter cela dans vos designs aussi ? Ou voulez-vous juste utiliser le même design exact et juste appeler cela la puce d'action, au lieu d'avoir la puce réelle choix et filtre ? Eh bien, pour être cohérent, en termes des conventions de nommage que vous avez dans vos fichiers de design, et ce que les ingénieurs ont développé sur le front end, vous pourriez vouloir créer trois, trois variantes de ceci.

Donc afin de faire ainsi tout le style est le même.

Donc je vais juste dupliquer ceci, et je vais faire de cette action expédier un composant.

Et avec cela étant un composant, je vais étiqueter cette étiquette.

Et ensuite je vais aller de l'avant et renommer ceci la la puce de choix, et ensuite entrer et renommer le cadre comme étiquette.

Et ensuite je vais renommer cette puce de filtre, je vais étiqueter ce filtre.

Et je vais renommer ce cadre de texte autolayout à étiquette couche deux à étiquette, je peux aller de l'avant et sélectionner les deux, les deux de ces éléments et cliquer sur cela et sélectionner créer plusieurs composants.

Et maintenant j'ai toutes les trois variantes de composant, ce qui est très important, ce que je vais avoir besoin de faire est de les renommer.

Donc c'est la puce de choix.

C'est la puce de filtre.

Et maintenant nous sommes en train de déchirer, nous avons ces trois variantes frappées hors du parc.

Et ce que nous pouvons faire maintenant est de nous concentrer sur la puce contour et la puce d'entrée.

Donc avec cela dit, je vais aller de l'avant et saisir cette puce ici, pour obtenir une longueur d'avance.

Et ce que cette puce a actuellement est que je vais détacher ceci et étiqueter cette action outline.

Et une fois que c'est étiqueté correctement, je vais aller de l'avant et me débarrasser de l'autolayout en maintenant Command Option, en fait juste Option Shift A, ensuite je vais faire la même chose exacte à l'autre couche de cadre autolab, et ensuite frapper Option Shift a et ensuite frapper Command Shift G pour enlever ce cadre du Texas ce n'est pas nécessaire.

Donc avec cette typographie ici, ce dont nous allons avoir besoin en ce moment est un espace réservé d'icône parce que c'est une puce contour.

Donc ce que je peux aller de l'avant et faire est dans ce fichier, j'ai déjà un espace réservé d'icône, copier cela et je vais maintenir la commande sur cette boîte englobante sur la gauche pour étirer cela et coller ceci et je vais aligner ceci à la gauche.

Et m'assurer que c'est quatre pixels à la gauche là et est centré verticalement, et ensuite déplacer ce texte, ajouter cette contrainte pour régler les contraintes dans ce texte droit et centre sur l'axe y et ensuite pousser ceci jusqu'à ce que la typographie soit huit pixels loin de l'icône ici.

Donc il faut déplacer ceci environ essentiellement trois pixels.

Donc je dois déplacer cela d'un pixel de plus.

Oups, voilà.

Une fois que c'est spécifié là, nous avons ces spécifications réglées correctement.

Nous avons un et le remplissage est réglé à 12 pointes sur la droite et huit sur la gauche, nous sommes prêts à partir.

Et c'est notre action outlined puce d'action.

Je suis ce que nous allons vouloir faire maintenant est de spécifier un contour d'un pixel et régler cela à l'intérieur ce qu'il est déjà par défaut, et nous allons ajouter la couleur de superposition de surfaces au contour mais je vais enlever ce style de couleur juste là.

Et je vais aller à surfaces Overlay et j'ai maintenant cela spécifié et si ces espaces réservés d'icône trop difficiles à voir nous pouvons changer la couleur de cela.

Et maintenant nous avons notre puce d'action contour et nous pouvons aller de l'avant et même ajouter auto layout à ceci donc l'espacement est dynamique, donc vous n'avez pas à faire manuellement ceci tout le temps.

Donc je frappe shift a pour faire auto layout et ensuite je vais enlever le remplissage horizontal et vertical par défaut Et ensuite réaligner ceci, vous devez le réaligner quand vous faites cela, et ensuite je vais aller de l'avant et déplacer cela, m'assurer que c'est quatre dips à la gauche ici.

Et ensuite nous ajouterons cela à ceci aussi, et enlèverons le, le remplissage d'un pixel ajouté et réalignerons ces éléments, ce qui est ennuyeux.

Et ensuite ce que je vais faire est d'aller de l'avant et shift clic sur sur les deux de ceux-ci dans le panneau Calques et frapper shift a.

Et ce que j'ai essentiellement fait est de maintenir l'espacement entre ce ce ces deux éléments en créant ce parent.

Et maintenant ce que je peux faire est d'aller de l'avant et sélectionner mon cadre contour action le cadre parent et frapper shift a.

Et je peux aller de l'avant et spécifier l'espacement pour cet élément aussi.

Et ce sera dynamique, mais une chose à noter est que cela peut auto layout peut devenir délicat, parce que vous ne pouvez pas spécifier individuellement le l'espacement.

Donc si je veux que ce soit 12 sur ce côté, c'est actuellement pas possible de faire cela pensé tout dehors.

Donc ce que vous pouvez faire est juste d'aller de l'avant et d'annuler ces actions.

Et vous devrez peut-être réajuster manuellement ceci.

Et nous aborderons cela dans la dans la prochaine vidéo dans notre prochaine section du cours.

Donc maintenant que nous avons créé cette puce d'action contour, nous pouvons aller de l'avant et la dupliquer, et ensuite créer cela comme un composant principal.

Une fois que c'est spécifié, aller de l'avant et commencer à aborder cette puce d'entrée plus est légèrement différent, nous allons, je vais devoir finir par enlever l'auto layout dans les cadres, ici.

Et ensuite.

Donc j'utilisais la touche de raccourci Option Shift a pour enlever l'auto layout et ensuite Command Shift G pour enlever le cadre.

Comme c'est ce qui reste.

Une fois que vous créez enlevez auto layout, cela se transforme en un cadre et ensuite vous devez enlever le cadre.

Donc avec cela réglé, je vais étiqueter cette et mettre oups et mettre navire.

Tout le remplissage approprié a été spécifié en ce moment nous avons cet espace réservé d'icône.

Et maintenant nous devons ajouter une icône actionnable ici.

Et j'ai déjà cela ici dans notre bibliothèque de système de design qui est appelée l'icône cancel.

Donc je peux copier cela.

Sélectionner votre votre cadre parent, et ensuite le coller là-dedans.

Si besoin est, oups, je vais glisser ceci ici.

Et je vais réinitialiser la taille à 18 par 18.

Et aller de l'avant et glisser ceci dans ce composant et tshirts centrer verticalement et aligner cela à la droite et pousser cela environ Ouais, huit dips.

Et avec cela spécifié, nous avons maintenant notre puce d'entrée.

Mais ce que nous allons avoir besoin de faire est de régler les contraintes sur cette icône d'action à droite au centre verticalement.

Et ensuite je vais aller de l'avant et pousser ce contenu de sorte qu'il n'y ait que huit dips entre le texte et cette icône d'action.

Et nous allons régler cet espace réservé d'icône à gauche et centre verticalement.

Et ensuite laisser régler cela à gauche et centre verticalement.

Et ensuite déplacer ceci et m'assurer que j'ai cet espacement réglé de manière appropriée.

Donc j'ai huit dips sur la gauche et la droite de ce texte.

Et une chose qui me manque est un remplissage.

Et j'ai besoin d'enlever le contour et ajouter la couleur de superposition de surfaces à cette puce.

Et une fois que j'ai spécifié cela nous sommes maintenant prêts à partir et nous avons créé tous les types de puces pour notre système de design.

Tout ce que nous avons à faire est d'étiqueter cette entrée.

Et une fois que nous spécifions cela nous avons maintenant créé tous les composants principaux nécessaires pour nos puces.

Et c'est tout ce que j'ai à vous montrer aujourd'hui.

Merci beaucoup d'avoir regardé, et je vous retrouverai dans la prochaine.

Je pense que j'ai presque oublié, en plus de notre autolayout autolab tend à redimensionner la hauteur de vos composants.

Donc nous voulons nous assurer que nous allons dans nos composants ici car nous avons les bonnes contraintes réglées.

Nous voulons double vérifier que nous avons les bonnes contraintes réglées pour nos composants.

Et avec auto layout spécifié sur certains de ces composants, nous allons vouloir redimensionner certains de ces éléments et s'assurer qu'ils sont prêts à partir.

Juste s'assurer que c'est réglé à 32 est la hauteur pour toutes ces puces sont réglées à 32.

Et je vais aller de l'avant et faire la même chose pour le reste de ces composants.

Et puisque les contraintes sont réglées pour centrer verticalement, ils s'ajusteront dynamiquement correctement.

Et certains d'entre eux ont auto layout.

Donc je ne peux pas juste manuellement ajuster la hauteur avec auto layout implémenté.

Donc ce que je peux faire est, est d'enlever cet auto layout et réajuster cette hauteur.

Et faire la même chose ici avec ce composant.

Notez que quand j'enlève l'auto layout, vous ne pouvez pas le voir, j'utilise une touche de raccourci Option Shift a, cela préserve l'icône maître je veux dire composant principal.

Mais regardez, regardez cela ne peut pas regarder les limites changer, je serai capable de changer la hauteur après cela.

Donc je viens de frapper Option Shift a, c'est maintenant changé la boîte englobante, et je vais aller de l'avant et plier cela d'un pixel de chaque côté.

Tout l'espacement est maintenu et ainsi de suite, et nous sommes prêts à partir.

Nous allons construire des dialogues.

Et nous allons commencer par comprendre ce que sont les dialogues et comment ils sont utilisés et pourquoi.

Et nous allons construire des variantes de ce dialogue.

Et je vais aussi vous mettre au défi de construire quelques variantes aussi, j'ai toutes les captures d'écran ici spécifiées des barrières que nous allons faire.

Et ensuite nous allons aller de l'avant et juste creuser dans la documentation en ouvrant ce lien.

Une fois que vous avez cela ouvert ici vous pouvez voir que les dialogues informent les utilisateurs à propos d'une tâche et contiennent des informations critiques et nécessitent des décisions ou impliquent de multiples tâches au sein de ce dialogue.

Donc ici, nous pouvons voir que ce dialogue est déclenché basé sur un bouton n'est-ce pas.

Et vous remarquerez qu'il y a cette superposition d'arrière-plan, nous c'est appelé un scrim.

Et nous avons cela dans notre système de design comme un style de couleur non seulement comme un style de couleur, mais scrim que nous pouvons tirer de notre système.

Donc si nous allons à notre fichier Figma, activons juste cela ici.

Pour aller accéder à notre modal de bibliothèque d'équipe activer la bibliothèque de système de design material, je pourrais aller de l'avant et chercher scrim et nous l'avons déjà accessible, nous pouvons le glisser et déposer ici pour utiliser plus tard.

Donc c'est un scrim pour vous et utilisé dans ce contexte.

Et ensuite vous pouvez voir qu'il y a une certaine élévation autour des bords de ce dialogue étant utilisée.

Et il y a un diviseur, et dans ce dans cette variante de confirmation, vous verrez qu'il y a ce menu avec un certain contenu débordant.

Donc nous allons aller de l'avant et construire cette cette variante.

Et nous allons aller de l'avant et construire un ce qui est étiqueté un dialogue simple ici dans cette démo interactive, où nous avons des éléments de liste ici.

Et vous remarquerez que les états de ceux-ci n'envoient pas de spam toute la largeur du dialogue, ce qui est intéressant.

Donc si nous devions inspecter le code, vous verrez que ceci ceci est un élément de liste.

Et il y a un peu un peu de remplissage réglé à 16 sur la gauche et la droite de cet élément.

Donc c'est important à noter là.

Et par-dessus cela dans l'élément parent, il y a un remplissage de huit sur la gauche et la droite aussi.

Donc c'est un remplissage sur la gauche et la droite de ce dialogue qui ne s'applique pas aux éléments de liste.

Donc c'est pourquoi il y a là le l'état là ne prend pas toute la largeur de cet élément.

Je vais fermer cet élément d'inspection.

Et maintenant nous avons aussi une variante de dialogue d'alerte aussi, que nous allons construire.

Et non seulement il y a ces variantes pour cela, mais vous voyez qu'il y en a une avec juste une copie de corps, juste du texte et avec le titre.

Ou, vous savez, nous avons les boutons côte à côte ou nous avons l'option d'avoir deux boutons empilés.

Pour moi, je préfère la variante côte à côte qui semble être un modèle beaucoup plus courant utilisé.

Et vous verrez qu'il y a d'autres options aussi dans ce dialogue, pas pour simple, mais pour la confirmation.

Il y a la variante empilée de boutons aussi et côte à côte.

Et nous allons juste aller de l'avant et un peu comprendre l'utilisation.

Donc un dialogue est un type de fenêtre modale qui apparaît devant une application ou du contenu d'application n'est-ce pas pour fournir des informations critiques ou demander une décision dialogue, désactiver toute fonctionnalité d'application quand ils apparaissent et restent à l'écran jusqu'à confirmé rejeté ou une action requise a été prise.

Et ce sont délibérément interruptifs, ce qui est ce qui renvoie à comment ceci est affiché devant le contenu de l'application est délibérément interruptif.

Donc ils devraient être utilisés avec parcimonie.

Et il y a quelques principes autour de ce composant où c'est concentré.

Cela concentre l'attention de l'utilisateur pour s'assurer que leur contenu est adressé à ce moment précis rapidement.

Le dialogue devrait être direct et communication, en communiquant l'information et dédié à compléter une tâche, le dialogue devrait apparaître en réponse à une tâche utilisateur ou une action avec des informations pertinentes ou contextuelles.

Donc c'est très utile et direct.

Et ici, vous pouvez voir quand utiliser soit une barre de collation bannière ou dialogue et manière dialogue est utilisé quand ces ces, la la tâche à accomplir doit être très concentrée et ceci est considéré comme haute priorité.

Donc cela bloque le contenu de l'application en dessous jusqu'à ce que l'utilisateur prenne les actions sur le dialogue ou sorte du dialogue si les options disponibles.

Et ici vous pouvez voir quelques exemples là sur mobile et, et la décomposition de l'anatomie.

Nous avons le titre de conteneur ici, un peu de texte de soutien et les boutons et le scrim dans l'arrière-plan que nous avons déjà tiré leur fichier finger.

Et nous avons quelques spécifications ici, nous allons juste aller de l'avant et plonger droit dedans et commencer à construire certains de ces éléments.

Donc nous pouvons aller de l'avant et commencer avec les alertes mobiles de bureau.

Donc je vais saisir ceci ici, j'ai déjà eu ceux-ci étiquetés pour placer dans notre feuille d'autocollants.

Et ce que je vais faire est de sélectionner ces images, les déplacer.

Ici, j'ai référencé les typestyles aussi, donc nous savons quoi utiliser.

Et avec cela spécifié, je vais régler la largeur à 560 dips, et avec la largeur spécifiée correctement, je vais régler la hauteur à 182 dips et utilise un rayon d'angle de quatre dips.

Et ensuite cela utilise la couleur surfaces surface pour l'arrière-plan, le remplissage, et ensuite bien sûr utilise le style d'effet d'élévation de 24 dip là.

Et maintenant nous avons la ligne de base spécifiée, nous allons aller de l'avant et renommer ce composant à desktop, forward slash mobile alert car c'est la variante de dialogue étiquette material design.

Et nous allons aller de l'avant et créer un H six.

Avec un H six créé, je vais étiqueter cet en-tête de dialogue comme spécifié dans le fichier là dans la capture d'écran, régler les autos, le dimensionnement à largeur automatique, le redimensionnement, aller de l'avant et sélectionner mon h six.

Et avec cela spécifier, nous pouvons aller de l'avant et rock and roll ici, je vais aligner ceci au haut et, et à gauche, donc c'est 24 dips de la gauche et la ligne de base réglée à 40, que je crois est 24 minutes du haut aussi.

Et nous pouvons aller de l'avant et double vérifier cela ici en créant juste un rectangle et en poussant ce contenu vers le bas.

Donc la ligne de base supposément réglée à 40.

Donc j'ai besoin d'en fait aller de l'avant et pousser ceci vers le haut un peu.

Et à son tour faisant ce remplissage 21 dips du haut là avec la ligne de base réglée à 40.

Comme vous pouvez le voir.

Donc maintenant que cela est spécifié, nous allons de l'avant et spécifions notre style de couleur pour cet en-tête.

Et aller dans nos styles de couleur, texte et iconographie et sélectionner le style de couleur haute emphase, nous allons aller de l'avant et dupliquer ce texte et sélectionner le textile de couleur corps un.

Et maintenant nous avons le bon textile réglé, nous devons spécifier le style de couleur à emphase moyenne.

Et ce que nous pouvons faire essentiellement est de spécifier la boîte englobante de ceci.

Et en spécifiant la boîte englobante ici, je vais aller de l'avant et commencer à juste prêter attention aux spécifications.

Et la ligne de base est censée être réglée à 36 dips de la ligne de base de l'en-tête.

Donc nous pourrions essentiellement juste faire cela créer un oups, créer un pousser ce rectangle vers le bas à la ligne de base, régler cela à 36 ici.

Donc j'ai juste besoin de pousser ce contenu vers le haut un peu.

Donc maintenant la ligne de base réglée à 36 là.

Et la boîte englobante ici réglée à 24 bits sur la gauche et la droite de cette zone de texte.

Donc ce que je peux faire est d'adresser ceci pour être une zone de texte fixe.

Et c'est actuellement à 23.

Laissez-moi pousser cela trois pixels.

Et maintenant c'est à 24.

Et nous voulons régler les contraintes à gauche et droite donc je maintiens Shift et sélectionne cette contrainte droite.

Et ensuite ce que nous pouvons faire est si je continue de taper lorem ipsum à lorcet Matt, et juste continuer à taper et une nouvelle ligne apparaîtra.

Donc avec cette nouvelle ligne apparaissant, nous allons aller nous avons maintenant juste besoin de justifier que l'art nous devons avoir nous devons justifier nos boutons de texte ici.

Et nos boutons de texte seront potentiellement 28 dips de la ligne de base du bas ici.

Depuis Le conteneur.

Donc ici, ce que j'essaie d'expliquer est que la hauteur de cette portion inférieure du dialogue est soulignée.

Donc c'est essentiellement dans, vous pourriez penser à cela comme étant dans sa propre rangée, où le contenu étant les boutons au sein de cette rangée inférieure ici, presque comme le pied de page de ce dialogue utilise deux boutons, et la hauteur réglée à 52.

Et c'est centré au sein de cette, cette rangée inférieure là.

Et ce texte est essentiellement ce que le dire est que cette copie de corps est 28 dips de la de la ligne de base du texte ici, vous voyez cette distance d'ici à ce ce conteneur rangée.

Donc pour vraiment obtenir cela précis, ce que nous pouvons faire est je vais créer un cadre ici, vous pourriez appeler ce dialogue, vous pourriez vous nous référençons tous ceci comme pied de page, et je vais spécifier la hauteur là à 52 dips.

Et bien sûr, aligner cela à la gauche et au bas, ça va maintenir la commande et étirer cela et spécifier les contraintes là à bas gauche et droite.

Et nous il n'y a pas besoin d'un arrière-plan.

Et nous devons implémenter des boutons dans ceci.

Donc si nous saisissons ouvrons notre bibliothèque d'équipe, allons au bouton texte.

Si je tape bouton, j'ai obtenu mon bouton texte là, et c'est étiqueté dans la spécification d'action un.

Et je duplique cela, et c'est huit dips loin de ce bouton, et ensuite modifie ce texte pour dire action deux nous sommes en train de déchirer, aller de l'avant et apporter ceci et en fait juste glisser ceci dans cette rangée et spécifier voir comment c'est aligné au centre que Donc essentiellement, notre espacement est tout propre, prêt à partir, nous avons l'espacement approprié là, huit dips entre les deux boutons, et à la droite et au bas, et au haut.

Et à cause de la hauteur étant spécifiée à 52 pour ce pied de page inférieur, et nous sommes prêts à partir.

Et tout ce que nous avons à faire est vraiment juste de justifier la distance ici entre ici et donc 28.

Donc nous sommes essentiellement à deux pixels off, supposément, mais c'est assez précis.

Et c'est 23 degrés loin de de là la zone de texte, et nous pouvons aller de l'avant et modifier cela.

Donc c'est réglé à 24.

Pour maintenant c'est 2024 dips loin, et nous sommes prêts à partir.

Ceci est tout correctement espacé.

Et nous avons maintenant cette variante de dialogue d'alerte mobile, qui est conforme aux spécifications et nous pouvons faire de cela un composant maître.

Avant que je fasse, je vais dupliquer cela.

Et c'est un composant principal, je m'excuse.

Donc nous avons notre variante de composant principal.

Je vais glisser cela ici.

Et maintenant que nous avons notre variante de composant principal, je vais aller de l'avant et voir ce que nous aborderons ensuite, que devrions-nous aborder ensuite ? Eh bien, nous pouvons aller de l'avant et créer ce dialogue de confirmation avec actions.

Rien de trop spécial à propos de ceci.

La largeur n'est pas en fait spécifiée dans ceci et ce serait un peu juste fastidieux de construire celui-là.

Donc commençons avec celui-ci.

En fait, nous n'avons pas toutes les détails nécessaires ne tenez pas compte de ce que j'ai déclaré, nous allons construire le dialogue de confirmation mobile.

Donc je vais copier cela là.

Aller de l'avant et renommer ceci.

Maintenant que je l'ai renommé, j'ai besoin de spécifier la largeur.

Et nous avons les deux actions.

Et ce que nous pouvons faire est que cela se redimensionnera parce que nous avons les contraintes réglées correctement.

Et nous devons régler des contraintes aux deux de ces boutons.

Et ces boutons actuellement sont, sont alignés au haut et à gauche de son cadre parent, mais nous devons aligner au bas et à droite pour que quand il se redimensionne il se redimensionne correctement.

Donc ce que nous pouvons faire est que nous avons toute la propriété spécifiée correctement.

Donc nous sommes prêts à partir.

Tout ce que nous avons à faire est de régler la largeur de 560 dips à 280 dips, et regardez ça nous avons tout contraint proportionnellement.

La seule chose est que nous devons pousser ce contenu vers le bas.

Et avec ce contenu poussé vers le bas, nous devrions juste spécifier l'espacement entre ce texte et la rangée de pied de page.

Et comme vous pouvez le voir c'est 28 pips loin de la ligne de base.

Donc allons-y et assurons-nous que c'est implémenté correctement.

Ça va changer cela à 28.

Et ce que nous allons faire est de s'assurer que quand nous redimensionnons ceci, ce cadre parent est un ensemble une règle ici au sein de ce cadre juste ici.

Donc alors que je le redimensionne, je sais que cela alors que je redimensionne le cadre parent, je sais que je dois pousser ceci vers le haut d'un pixel de plus, j'espérais que cette ligne rouge m'aiderait à aligner le contenu, mais cela ne fait pas en fait cela ce n'est pas responsive, ces lignes rouges, elles restent en place.

Et ensuite je vais glisser cette zone de texte vers le bas et m'assurer que c'est réglé à 24.

Donc voilà, cet espacement approprié là sur la gauche et la droite et le bas.

Et nous avons maintenant notre variante de dialogue de confirmation là.

Et encore une fois, ceci adhère à une variante d'une ligne.

Il y a aussi ceci indique aussi un en-tête de dialogue de deux lignes là avec deux lignes.

Donc nous pourrions même aller de l'avant et faire cela si nous voulions.

Donc je peux aller de l'avant et faire cela très vite.

Donc nous aurons à pousser vers le bas ce contenu essentiellement.

Donc avec cela, je vais juste pousser cette copie vers le bas.

Et ensuite écrire à bash line dialog header, nous avons maintenant notre deux lignes, je vais pousser ceci vers le haut à 14, parce que cela me donne l'espacement approprié ici.

de 36 dips là, de d'une ligne de base à une autre.

Donc c'est réglé à 36, comme je l'ai déclaré, ce qui est génial.

Donc c'est correctement, proportionnellement implémenté.

Et maintenant j'ai juste besoin de justifier l'espacement de entre ce texte et les actions.

Donc c'est réglé à 28 profondeur, donc nous pouvons faire est, cela devrait être beaucoup plus facile est en fait d'aller de l'avant et de mettre pousser ce contenu, créer ce rectangle de 28 dip pour aligner les choses, et juste pousser ceci vers le haut pour quatre dips là, et le supprimer.

Et maintenant nos lignes de base sont alignées comme spécifié dans la spécification.

Et ce que je peux faire est de sélectionner Redimensionner pour adapter ou la touche de raccourci Shift Option command R.

Et cela devrait redimensionner le contenu au conteneur parent, ce qui est génial.

Ou vous pouvez juste maintenir Command jusqu'à ce qu'il jusqu'à ce qu'il s'aligne à votre conteneur.

Et vous avez maintenant votre deux en-tête de dialogue de deux lignes.

Et nous pouvons aller de l'avant et créer ce dialogue de confirmation avec de longues actions qui sont empilées.

Donc la différence entre celui-ci est que ces boutons sont côte à côte.

Et ceux-ci sont empilés.

Et tout ce que nous avons à faire est que nous n'avons pas à faire un peu plus de déplacement ici.

Donc là dans ce scénario, il y a le concept du pied de page n'a pas besoin d'être utilisé, il pourrait être où je vais l'enlever.

Et ce que je vais faire est de renommer ceci à turn on speed boost.

Et avec cela spécifié, je vais juste aligner ceux-ci correctement.

Et ensuite m'assurer qu'ils sont 12 dips en distance à part, et m'assurer qu'ils sont des dips de la droite de ce cadre.

Donc c'est un fossé dans la droite et devrait être profondeur du bas aussi.

Donc maintenant que nous avons cela spécifié, nous avons nos deux boutons.

Mais ce que nous avons besoin de savoir est la ligne de base.

Donc 828, donc 36 dips du cadre ici.

Donc quand vous spécifiez 36 dips du cadre, essentiellement ce que j'ai fait était que j'ai juste calculé la distance, la distance de cette ligne de base, et la distance de ce entre ce bouton et ici, et c'est 28 plus huit, qui est 36 cinq, si je fais mon calcul, juste, et je peux juste aller de l'avant et glisser ceci vers le haut jusqu'à ce que cela s'aligne là.

Et nous sommes alignés.

Donc je suis cet espacement approprié.

Et maintenant tout ce que j'ai à faire est de m'assurer que je glisse vers le haut le bas de cet élément.

Donc c'est huit profondeur du bas du bouton.

Et je pourrais appliquer mes contraintes 30 réglées correctement et nous sommes prêts à partir.

Je vais spécifier que c'est un dialogue de confirmation avec de longues actions.

Je vais faire de cela un composant principal et ensuite nous pouvons créer le dialogue d'alerte mobile j'ai juste attaché mon instance, étiqueter ce dialogue d'alerte.

Et le dialogue d'alerte est très simple.

Il n'a même pas d'en-tête, il utilise juste une copie de corps.

Donc ce que nous pouvons aller de l'avant et faire est d'ajouter 52 plus 28 plus 38.

Oups, vous ne pouvez pas faire de calcul 28 plus 38.

Je ne sais pas pourquoi ça ne fait pas le calcul pour moi là.

Donc 28 plus 3866 plus 52, c'est 118.

Donc la hauteur de cet élément va être 118.

Donc ce que nous pouvons faire est juste de régler ceci à 118.

Et maintenant nous pouvons mettre ce texte, pousser ce texte vers le haut, juste en faire une ligne.

Et maintenant que nous avons cette une ligne, je vais régler la typographie pour redimensionner la largeur, automatiquement, je vais alors m'assurer que la ligne de base est réglée de manière appropriée.

Donc c'est réglé à actuellement 38 dips depuis depuis le haut en ce moment c'est 40.

Voilà à 38.

Là, je peux pousser ce contenu vers le haut, excusez-moi.

Et maintenant je peux créer une zone de texte fixe.

Et je veux que ce soit 24 dips de la droite, ou 624.

Donc si je pousse ceci un peu plus à 22.

Et maintenant je l'ai réglé à 24.

Et avec cela spécifié, je veux aussi que la zone de texte soit huit dips du bas ici, j'ai ceci du bas du cadre extérieur des boutons.

Donc actuellement, c'est réglé à quatre.

Maintenant c'est réglé à huit là, et nous sommes prêts à partir.

Nous avons tout l'espacement approprié spécifié pour ce dialogue d'alerte.

Et nous sommes prêts à partir.

C'est ça.

Peut-être que nous pouvons juste renommer ceux-ci à annuler et rejeter.

Et ce que nous pouvons faire ici est juste s'assurer que l'espacement approprié est réglé à 12 actuellement réglé cela à huit, et ensuite pousser ceci.

Pour les dips.

Maintenant c'est correctement espacé, huit Entre les Boutons et le bas et la droite des boutons.

Donc c'est génial.

Et maintenant nous avons notre variante mobile de notre dialogue d'alerte.

Et maintenant que nous avons créé trois de ceux-ci, je peux, je veux vous mettre au défi de construire cet en-tête de dialogue ici.

Et nous pouvons voir que cela utilise est, eh bien si nous allons à nos éléments de liste, nous pouvons facilement voir que nous pourrions utiliser cette variante ici que je viens de tirer le avec l'icône et le texte et l'action, qui est une autre icône.

Et nous pouvons redimensionner ceci en conséquence.

Nous pouvons aller de l'avant et en fait construire ceci ensemble en modifiant certains composants d'éléments de liste existants que nous avons.

Donc avec cela dit, nous avons un nous allons juste perfectionner ceci, cet élément de liste ici.

Donc nous allons étiqueter cette icône et texte, j'ai obtenu cet élément de liste.

Et bien sûr, nous avons appliqué des contraintes déjà à ceci.

Donc cela vaudra la peine de choisir hors de la boîte parce que parce que nous avons déjà défini cela, et nous allons juste régler la hauteur de ceci 256 dips, le contenu reste centré au besoin.

Et comme prévu, et ensuite nous réglerons la hauteur de ceci 240 par 40.

Mais nous voulons que la hauteur de l'icône soit 40 par 40.

Donc je vais de l'avant et implémente ceci, avec l'icône actuellement est réglée à 33 point 33.

Donc ce que nous pouvons faire est que je peux détacher ceci le dégrouper et je veux juste m'assurer que j'échelonne le vecteur correctement.

Et le cadre réglé à 40 par 40.

Comme vous pouvez le voir, et nous pouvons juste utiliser temporairement nous avons un espace réservé.

Donc si vous saviez ceci en fait, vous savez, affiner cette icône plus tard, vous pouvez aller de l'avant et faire cela.

Mais je vais juste utiliser cet espace réservé donc ne pas gâcher avec la modification des les icônes qui sont systématiquement construites à partir de.

Pour le material design.

Je vais juste changer le taux de coin sur cet espace réservé d'icône pour qu'il soit 40 par 40.

Et c'est 24 dips depuis la la gauche de de cet élément de liste.

Donc maintenant que j'ai déplacé cette colonne C'est génial.

Et le texte est 20 dips à la gauche de, de l'icône aussi.

Et je vais m'assurer que les contraintes sont réglées à gauche et centrer verticalement.

Et les contraintes sont prêtes à partir sur ce texte ici.

Et tout ce que j'ai à faire est, je pourrais renommer ceci ici pour que le texte corresponde au, ce qui est spécifié dans la spécification.

Et ce que nous pouvons faire est juste de dupliquer ceci et aligner ceci au bas du prochain élément de liste.

Et juste étiqueter ceci utilisateur deux.

Et ensuite je peux dupliquer ceci à nouveau, et juste taper un compte publicitaire.

Et n'hésitez pas à modifier le remplissage de ceci et changer cela au type d'image et ajouter une image au besoin.

Comme cela utilise des icônes, il y a maintenant que l'espacement spécifié sur ces trois éléments de liste, allons-y et faisons le conteneur parent.

Donc notre conteneur parent, j'imaginerais est réglé à Eh bien, dans ce cas réglé à 320, ou deux à un spécifié ici.

Et cela semble comme la même largeur qu'un dialogue simple.

Donc je vais créer un cadre, aller à ma feuille d'autocollants et copier cette convention de nommage.

et renommer ceci au mobile / dialogue simple, que la largeur à 280 rayon d'angle à quatre style de couleur le filtre surfaces surface et ensuite les effets au avoir le style d'effet d'utiliser l'élévation de 24 dips.

Et avec cela, nous allons modifier la largeur ici à oups, la largeur est devrait être prête à partir.

Ce que nous allons faire est d'ajouter un H six ici, ce que je peux faire est juste de copier le H six ici.

Et ensuite, ou je peux saisir cette doublure h6 que j'ai déjà créée.

Et ils le positionneront au sein de cet élément.

Et nous devons vérifier et nous assurer que la ligne de base de ceci est réglée est 40 profondeurs depuis le haut de ce cadre.

Et avec cela, voyons, réglé cela à 40.

Juste pousser, essentiellement juste pousser cela vers le haut légèrement.

Et maintenant c'est prêt à partir.

Nous avons notre en-tête de dialogue et est enveloppé dans un cadre qui a une hauteur de 64.

Donc je vais régler la contrainte verticale pour centrer sur le texte.

Donc quand je redimensionne le cadre dans lequel je viens de l'envelopper il restera en position au besoin.

Donc c'est réglé à 60.

Maintenant c'est réglé à 60 pour la hauteur réglée à 64 dips, et ça n'a pas fait correctement ce que je voulais.

Donc je vais m'assurer que c'est centré au sein de ce cadre, ensuite pousser cela vers le haut, maintenir Command et redimensionner ce cadre d'en-tête en-tête, je vais étiqueter cet en-tête.

Maintenant j'ai cet ensemble correctement.

Et ensuite tous ces éléments de liste s'empileront sur le dessus de ce cadre.

Donc je peux maintenant qu'ils sont empilés, ceux-ci sont de taille appropriée, j'ai juste besoin d'ajuster la largeur.

Et nous sommes prêts à partir.

Tout ce que j'ai à faire est de justifier le redimensionnement de cette portion inférieure.

Et je pourrais avoir besoin d'ajouter 16 dips là, le bas est actuellement réglé à 870 et augmenter cela 17% vers le haut un et nous allons aller.

Donc nous avons maintenant atteint notre variante de dialogue simple.

Et nous avons quelques de plus à créer si nous voulons.

Je vais en fait vous mettre au défi de construire les deux derniers éléments.

Et ce que vous allez vous retrouver à faire en créant ces deux derniers est que nous avons créé ces quatre ensemble.

Mais dans ces dialogues, vous allez vous retrouver à construire quelques dialogues complexes ici, vous allez rencontrer ceci, ces éléments ou les éléments débordent et sont sont cachés à cause du débordement parce que nous avons ceci, ces actions apparaissant au-dessus et l'utilisateur peut défiler à travers ces éléments et en sélectionner un.

Donc je vais vous mettre au défi de construire cela et aussi vous mettre au défi de construire ce dialogue plein écran.

Ce que vous ne construisez pas sont ces champs de saisie de texte dans l'interface.

Vous pourriez Mais pour le dialogue plein écran, nous pourrions, c'est juste un bonus pour vous à créer, et vous mettre au défi.

Et, ouais, je vais juste mettre cette vidéo en pause et construire ce dialogue de confirmation défilant.

Et je reviendrai tout de suite.

Donc j'ai maintenant construit ma variante de dialogue de confirmation défilant pour mobile.

Et essentiellement ce que j'ai fait était que je l'ai juste recréé, laissez-moi aller de l'avant et le saisir.

Donc notre autre variante mobile, notre dialogue simple, ce que j'ai fait était que j'ai copié ceci, détaché.

Et je suis allé à mes actifs et j'ai saisi ma liste de contrôle radio Marriott.

Et ensuite j'ai enveloppé cela dans un cadre, j'ai réglé la hauteur, comme vous pouvez le voir ici, à 48.

Et j'ai juste spécifié l'espacement approprié entre tous les éléments au sein de cet élément de liste, ensuite je les ai juste dupliqués.

Et ils étaient parce qu'ils sont supposés s'empiler les uns sur les autres.

Et puisque nos boutons sont étiquetés correctement, j'étais capable de juste les échanger entre les deux états, ce qui était génial, réglé les contraintes à verticalement, être centré si cette hauteur est jamais modifiée.

Et ensuite j'ai saisi le pied de page ici, et déplacé cela au haut de l'ordre des calques.

Donc cela ressemblait à on dirait que vous êtes capable de défiler à travers ce contenu, comme indiqué ici.

Et ce pied de page était déjà créé, tout ce que j'avais à faire était d'ajouter un diviseur dans cet élément.

Et j'ai aligné ce diviseur au haut ici dans l'élément de pied de page dans le cadre de pied de page.

Et c'est tout ce que j'avais à faire.

Et c'est comme ça que j'ai créé ce dialogue là.

Et ouais, c'était comment j'ai construit cela.

Et c'est tout ce que j'ai à vous montrer aujourd'hui dans la construction de dialogues.

J'espère que vous avez appris beaucoup et apprécié cette vidéo.

Et je vous mets au défi en bonus de créer ce dialogue plein écran.

Nous allons passer en revue les sélecteurs de date et nous allons gagner un aperçu général de quels sélecteurs de date qui sont là-bas et quand et comment ils sont utilisés.

Et ensuite nous allons construire quelques sélecteurs de date nous-mêmes.

Et ici nous avons la documentation.

Et je vais aller de l'avant et ouvrir le lien.

Et une fois que votre lien ouvre, comme vous pouvez le voir, les sélecteurs de date laissent les utilisateurs sélectionner une date ou une plage de dates, comme vous pouvez le voir ici.

Ceci spécifie la date actuelle et ensuite la date sélectionnée ici.

Et nous avons un en-tête petite icône modifier pour éditer la date depuis ce champ ici, cet en-tête, menu déroulant là et quelques quelques flèches pour se déplacer entre les mois.

et servir.

Il y a un peu d'élévation étant utilisée.

Et voici une décomposition de l'anatomie d'un sélecteur de date calendrier mobile.

Et ici vous pouvez voir qu'il a un titre en haut et ensuite la date sélectionnée ici étant représentée.

Et ensuite il a le basculer vers l'icône d'entrée clavier, qui est ce que ceci est appelé.

Et ensuite il a le menu de sélection d'année.

Et nous avons aussi la pagination pour aller de mois en mois soit en avant ou en arrière.

Et ensuite nous avons la date actuelle ici.

Ceci est représenté avec ce contour.

Et ensuite nous avons la date sélectionnée ici avec une couleur primaire comme arrière-plan spécifié, et quelques actions là pour annuler ou frapper OK.

Et vous pouvez voir à quoi ressemble le sélecteur de plage de date mobile.

Donc ceci est un sélecteur de date calendrier mobile.

Et ensuite nous avons le sélecteur de plage de date.

Donc vous pouvez spécifier une date de début et une date de fin.

Et ensuite ceci est la plage sélectionnée ici avec la couleur primaire plus claire dans l'arrière-plan.

Ensuite nous avons une variante de sélecteur d'entrée mobile, tas de décompositions de l'anatomie là, et ainsi de suite.

Et cette vidéo va être très dense.

Il y a beaucoup de choses qui se passent dans ce composant sélecteur de date, et nous allons faire, nous allons le décomposer, nous allons vraiment le simplifier et commencer avec les petits éléments dont il est composé, et ensuite construire ces éléments en conséquence.

Et avec ce modèle mental en tête, nous serons capables d'aborder la construction de ces composants complexes.

Donc c'est génial.

Et nous allons construire non seulement des variantes mobiles, mais aussi des variantes de bureau.

Donc c'est c'est génial.

et ici si nous allons à nos spécifications, vous pouvez voir que nous avons des cibles tactiles spécifiées pour un sélecteur de date mobile, où la taille de cible tactile pour un sélecteur de date est réglée à 32 par 32 dips.

Et que le c'est l'approche recommandée ici Et le conteneur extérieur est réglé à 40 par 48 nips.

Et ici nous commençons à voir les spécifications de ce à quoi ressemble l'en-tête de calendrier ici.

Donc c'est très important.

Et un tas de spécifications spécifiées à juste là, pour que vous ne manquiez rien, puisqu'il y a beaucoup de choses qui se passent.

Et ici vous pouvez voir une vue calendrier pour le sélecteur de date mobile, et une vue de sélection d'année.

Ainsi de suite, nous allons couvrir ces lourdement dans Figma.

Donc sautons droit dedans.

Donc ici, j'ai une, notre bientôt feuille d'autocollants ici.

Et voici quelques éléments que nous allons construire.

Donc nous avons l'en-tête de calendrier mobile juste ici que nous allons construire, et notre outil de sélecteur de calendrier mobile, image de sélecteur de calendrier ici à référencer.

Donc je vais déplacer certaines de ces images hors du chemin.

Donc juste garder celles-ci ici, pousser cette image vers le haut.

Et avec cela, nous pouvons aller de l'avant et commencer.

Donc je vais aller de l'avant et copier ceci, ce texte, parce que ce sera le nom de notre composant principal une fois qu'il sera créé.

Et nous pouvons aller de l'avant et commencer à comprendre ce que la, la largeur de cette vue calendrier devrait être et cet ensemble à 328 dips.

Donc nous tapons 328.

Nous savons comment la largeur spécifiée, mais ce que nous devons identifier Ensuite est la hauteur de cet en-tête de calendrier.

Donc ici, vous pouvez voir que c'est réglé à 120.

Et ensuite nous avons 32 plus 24, donc 100 et ensuite plus 120.

Donc avec cela, nous obtenons 176.

Et la hauteur de ceci est réglée à 176.

Et maintenant que nous avons la hauteur, spécifiée correctement, nous allons vouloir aussi spécifier les coins arrondis sur ce cadre parent.

Donc régler les coins arrondis dans un coin indépendant.

Donc nous allons vouloir le régler au haut gauche et haut droit, et régler cela à quatre.

Maintenant nos coins sont arrondis sur le haut.

Et nous allons avoir besoin de faire est d'ajouter dans la propriété de texte de surlignement ici.

Comme vous pouvez le voir, la ligne de base est réglée à 32 dips.

Donc si nous allons de l'avant et oups, sortons notre outil texte, et juste spécifier select date, et ensuite changer le style de texte à over line, nous avons maintenant select date spécifié et tout notre contenu sera 16 dips à la gauche, et s'assurer ou en fait 24.

Mes excuses réglé à 24 dips à la gauche ici dans cet en-tête.

Et ensuite nous allons vérifier cette ligne de base.

Et sûr que c'est réglé à 32.

Donc 30, nous sommes presque précis.

Donc maintenant que nous avons cet ensemble là, la ligne de base réglée à 32 nous sommes prêts à partir.

Et une chose dont nous avons besoin est dans ce fichier d'exercice, voici quelques icônes, je vais copier cette icône edit.

Et j'ai besoin de la placer vers la droite de ceci.

Ce champ, donc une chose que j'ai besoin de spécifier est que ce que je pourrais faire est dans mon dans ce composant, si je nommais ceci correctement dans cet élément, qui est un en-tête de calendrier, je peux commencer à envelopper ces éléments en conséquence.

Donc peut-être que je veux transformer cela en un cadre et étiqueter ceci select date row.

Et avec cette Rowse, je pourrais, ce que je veux faire est de m'assurer que je maintiens command et aligne ceci à et glisse ceci aux bords haut et droit du cadre parent.

Donc de cette façon ce contenu est isolé du champ de texte ici parce que vous voyez cette boîte spécifiée ici cet écran entier vous pouvez penser à cela comme une rangée quand vous implémentez ceci en développement.

Et ensuite nous avons une autre rangée en dessous avec un grand en-tête.

Donc nous allons aller de l'avant et ajouter cela je crois que comme un h1, je vais spécifier cette date exacte, 17 novembre.

Le lundi, aller à mes styles de texte et sélectionner le h1 et ce n'est clairement pas un h1, nous allons vouloir changer cela à un h3.

Cela ressemble à ce que c'est en fait un h4.

Donc je vais aligner ceci au bas droit et ce que nous voulons faire est de s'assurer que notre texte ici Est 24 dips de la gauche.

Et non seulement cela, nous allons devoir aller de l'avant et aligner nos icônes ici.

Mais par-dessus cela notre typographie ici, vous remarquerez que dans ce composant ci-dessous, nous avons une autre portion de l'en-tête qui a un fond blanc.

Donc ce que nous allons faire est de spécifier la distance ici.

Donc nous avons 128 72.

Donc nous avons une distance, je crois que j'ai environ grossièrement 16.

Ici, ce n'est pas vraiment clair.

Donc si nous soustrayons 72 plus 3200 420, mm est 104, nous obtenons 16.

Donc oui, nous voulons nous assurer que nous avons spécifié la hauteur de la portion inférieure.

Donc ce que nous pouvons faire est si nous changeons cet arrière-plan, ou ces couleurs à texte, et je ne peux pas contenu sur primaire, et ensuite je peux changer ceci à contenu sur primaire aussi.

Et je vais de l'avant et sélectionne le remplissage d'arrière-plan de ceci, le conteneur, le composant, et je sélectionne cela le primaire, tout ce que j'ai à faire est que je peux même dupliquer cette rangée, supprimer le texte dans ce cadre, et, et spécifier cet arrière-plan pour être réglé à surfaces surface.

Et j'ai juste besoin de m'assurer que la hauteur est réglée de manière appropriée.

Donc c'est réglé à qu'est-ce que c'est 32 plus 24, ce qui nous donnera 56, la hauteur réglée à 56 sur cet sur cet élément.

Et je peux juste m'assurer que cela s'aligne au bas là.

Et avec cela justifié, j'ai juste besoin de m'assurer que cette typographie oups, cette typographie, et icône est nos nos 16 dips du bas, que nous avons maintenant justifié et 24 dips dans la gauche et la droite.

Et comme vous pouvez le voir ici, oups, la typographie est 64 dips à la gauche de cette icône, qui maintenant que tout est réglé proportionnellement, nous sommes prêts à partir.

Donc j'ai juste besoin de m'assurer que cette icône s'aligne à la ligne de base du type texte dans ce sélecteur de date.

Donc vous poussez cela vers le bas d'un pixel.

Et maintenant cela est en train d'être aligné.

Donc c'est génial.

Et nous sommes en train de déchirer.

Donc nous avons presque fini, nous devons aller de l'avant et construire notre typographie ici.

Donc ici vous pouvez voir qu'il y a du remplissage sur le haut et le bas de cette section ici, cette rangée de sélecteur de date.

Donc je peux spécifier cela.

Et une fois que c'est spécifié dans cette rangée de sélecteur de date, je vais avoir besoin de m'assurer que j'ai la bonne typographie spécifiée.

Et cela ressemble à ce que cela utilise un textile de légende.

Donc ce sera essentiellement centré.

Et avec ce texte texte légende style, notez taper novembre 2018.

Sélectionner mon style de texte légende.

et le centrer puisque c'est enveloppé dans une rangée qui a une hauteur de 56 et spécifie que les lignes de base 32 pixels du haut de ceci, je vais juste le centrer car c'est clairement centré dans cet élément.

S'assurer que réglé à 24 dips dans la gauche.

Et nous utilisons aussi une icône flèche vers le bas menu déroulant flèche menu déroulant.

Donc je peux copier ceci ici.

Aller de l'avant et sélectionner cette rangée de sélecteur de date, la coller dedans et commencer à déplacer ceci jusqu'à ce que ce soit quatre dips à la gauche de ce texte.

Donc maintenant que c'est à la spécification ici pour dips là de gauche à ce texte.

Et maintenant que cela est implémenté, nous pouvons aller de l'avant et ajouter les icônes pour se déplacer entre les mois.

Donc j'ai les deux ici.

Je vais copier celles-ci et spécifier l'espacement à 24 entre les icônes et il y a un espacement de 24 aussi juste ici.

Donc je peux en fait Juste aller glisser celles-ci ici.

Et une fois que celles-ci sont glissées, juste un peu déplacer ces éléments en conséquence.

Et maintenant nous sommes prêts à partir, nous avons créé notre en-tête.

Et nous pouvons aller de l'avant et double vérifier l'espacement au besoin là 16 dips s'asseoir en haut et en bas entre nos éléments là.

Et nous pouvons même envelopper ces deux ensemble si nécessaire.

Vous pouvez appliquer des contraintes et en relation à son élément parent.

Donc je règle tout ici à gauche et centrer verticalement, ensuite je réglerai ces deux icônes à droite et centrer verticalement.

Donc si elles restent sur leurs côtés, si elles bougent, la largeur obtient là tout changement de largeur là, je vais aussi sélectionner la rangée de sélecteur de date, et juste spécifier qu'elle reste toujours au bas et est réglée à gauche et droite pour qu'elle soit contrainte proportionnellement.

Et nous devrions être prêts à partir.

Donc maintenant avec cet en-tête de calendrier créé, nous pouvons aller de l'avant et commencer à utiliser cet élément à travers d'autres éléments mobiles aussi.

Donc si je vais de l'avant, et je peux juste dupliquer ceci au cas où, je veux créer une variante de celui-ci, mais établir ceci comme un composant principal et ensuite dupliquer cela, nous pouvons aller de l'avant et procéder à aborder notre premier sélecteur de date, qui est le sélecteur d'entrée mobile.

Donc ce que nous allons faire est que nous avons l'en-tête, donc nous pouvons copier l'en-tête.

Et nous avons besoin d'un champ de saisie de texte ici.

Donc si je vais à mes actifs et m'assure que nous avons toujours notre bibliothèque de système de design material activée, je vais aller de l'avant et chercher une entrée de texte.

Et oups champs de texte.

Désolé.

Et ensuite je peux aller de l'avant et juste accéder à un champ de saisie de texte.

Et nous pouvons aller de l'avant et sélectionner, disons, ce composant.

Et ce que ce composant spécifié, nous allons vouloir envelopper ceci dans un cadre aussi.

Et juste faire attention aux spécifications ici.

Donc les spécifications ont l'ensemble à 16 dips sur le dessus depuis le haut.

Et ce que nous devons faire est de créer un conteneur parent.

Donc nous allons établir ceci comme le sélecteur d'entrée mobile mobile.

Donc ce conteneur parent sera appelé le mobile / input picker, ensuite je vais spécifier la hauteur à 264.

Vous verrez qu'il y a un peu d'espace là.

Et ensuite je vais aller de l'avant et utiliser cette variation du le composant ici.

Et juste référencer cela.

Et placer ceci dans le conteneur a le bon remplissage sur la gauche et la droite déjà juste besoin de s'assurer que le remplissage sur le dessus réglé à 16 là, ce qu'il est.

Et maintenant nous avons juste besoin d'implémenter un arrière-plan, qui est réglé à Ville surfaces surface.

Et une chose à noter est que nous devons spécifier le rayon d'angle du conteneur parent à quatre tout autour.

Et aussi, puisque c'est un modal, ici, dans ce scénario, nous devons spécifier l'élévation 224 24 dip élévation sur le conteneur parent.

Et maintenant nous pouvons aller de l'avant et juste utiliser cet exemple de champ de texte.

Notez que ce n'est pas le bon type de champ de texte.

Mais ceci est juste un exemple de l'implémentation.

Et ici vous remarquerez que nous pourrions avoir besoin d'une autre variante d'en-tête.

Donc c'est un peu pourquoi j'ai dupliqué ceci ici.

Donc je veux en fait peut-être aller de l'avant et supprimer cette rangée de sélecteur de date.

Et avant que je supprime ce sélecteur de date, je vais aller de l'avant sélectionner le conteneur parent et déplacer ce contenu vers le haut et m'assurer qu'il s'aligne et ensuite supprimer ce jour choisir une rangée ci-dessous et faire de cela un composant principal et le dupliquer.

Et ensuite nous utiliserons celui-ci à la place.

Donc si je vais de l'avant et supprime cela, Puis-je coller ceci et l'aligner au haut, je peux déplacer cet élément vers le haut.

Donc c'est 16 choix dips depuis le haut.

Nous avons maintenant ce sélecteur de date et la largeur est toujours réglée à est réglée à 364.

Donc j'ai besoin de changer cela à 264 et nous allons aller de l'avant et implémenter quelques boutons texte seulement maintenant.

Donc je vais aller à mes actifs.

Juste tirer dans ce bouton texte et j'en ai besoin de deux.

J'en ai besoin d'un qui est dit ok, donc je vais aller de l'avant et glisser cela là-dedans.

Et ce que nous allons vouloir faire est d'aligner cela, en s'assurant que la typographie s'aligne avec la fin de ce champ de saisie de texte, ce qu'elle fait, signifiant que ce cadre parent du bouton est 16, dips à la droite du conteneur, là ajouté à 16 dips du bas aussi.

Donc c'est équivalent, taille égale.

Et je vais taper annuler sur ce champ de texte.

Et une fois que c'est spécifié, nous allons juste aligner cela ici avec cet autre bouton, et il doit être huit dips à la gauche du bouton OK.

Donc maintenant, nous avons créé notre sélecteur d'entrée mobile rapidement.

Et c'est l'un des sélecteurs de date les plus faciles à implémenter.

Donc avec cela, je vais faire de cela un composant principal, ce qui est génial.

Maintenant nous devons, nous avons notre premier sélecteur de date ici pour mobile.

Et ensuite, nous allons aborder l'un des composants les plus complexes.

Donc ici, vous commencerez à voir de quoi ceux-ci sont composés sur.

Peut-être que nous commencerons avec votre vue de sélection, c'est un peu plus simple à aborder au début, pas aussi écrasant.

Mais c'est comment nous allons décomposer ce composant.

Donc qu'est-ce que nous voyons ici ? Eh bien, nous voyons que nous avons besoin de créer des unités, nous pouvons appeler ces unités ou ces cellules, qui seront nos éléments, éléments Id pour les sélecteurs de date.

Et ces éléments contiennent le le texte, bien sûr, et cela nous donne les dimensions de cette, cette cellule que nous allons créer, et c'est 52 dips en hauteur, et c'est 88 dips de large.

Donc nous allons essentiellement, et cela a une variante d'état sélectionné.

Donc nous allons avoir besoin de faire cet état sélectionné aussi.

Et c'est Best Buy ici.

72, dips de large et 36 dips en hauteur, et cela utilise la couleur d'arrière-plan primaire.

Donc c'est génial.

Et nous avons déjà notre composant en-tête ici.

Donc nous pouvons aller de l'avant et apporter une copie de cela ici.

Et vous remarquerez que cela n'utilise pas dans la vue de sélection d'année pour le sélecteur d'entrée de données mobile, n'utilise pas ces icônes là.

Donc nous pouvons aller de l'avant et juste enlever celles-ci.

Donc quand nous supprimons ces instances, dans notre instance, cela les cachera juste, ce qui est bien, ne vous en faites pas.

Et nous pouvons aller de l'avant et commencer à créer ces cellules, n'est-ce pas.

Donc ce que nous allons aller de l'avant et faire est de créer un cadre, étiqueter ceci elements, space slash space, year selection, cell.

Et ensuite nous pouvons étiqueter cela la cellule par défaut, parce que nous allons avoir une cellule active ou une cellule sélectionnée pour en fait, nous pouvons étiqueter que celle-ci non sélectionnée.

Et ensuite nous allons en créer une autre plus tard appelée sélectionnée.

Donc maintenant nous avons les deux assurer que le projet de loi est réglé de surfaces surface, nous allons aller et ce que nous allons faire est juste de spécifier la hauteur pour les deux de ces 250 pour tuer deux oiseaux avec une pierre là.

Et la largeur pour les deux d'entre eux est réglée à 88 dips.

C'est fantastique.

Maintenant nous avons la typographie au milieu.

Donc sur la cellule, nous avons du texte, nous pouvons, voyons 2011, je peux sélectionner cela 2011.

Et je vais m'assurer que cette typographie réglée à haute emphase, et ensuite m'assurer que le redimensionnement réglé à largeur automatique.

Et maintenant j'ai besoin d'appliquer le bon style de texte.

Donc on dirait que ça utilise une légende.

Donc on dirait que ça utilise une légende, j'essaie de juste vérifier que leur semble précis.

Nous pouvons aussi référencer la documentation si nous sommes jamais confus sur ce que les textiles étant utilisés certains, mais je n'ai pas trouvé de spécifications là-dessus.

Donc ici nous avons cette typographie.

Pour le texte, peut-être que nous voulons appliquer.

Vérifions double et voyons si nous avons besoin d'utiliser le style de texte du corps.

Cela semble beaucoup mieux.

Donc nous appliquons ce style de texte du corps juste le centrer verticalement et horizontalement avec la commande, je veux dire les touches de raccourci, option V et H nous devrions être prêts à partir.

Donc nous avons la cellule.

Et maintenant que nous avons cela honnêtement, c'était la seule chose qui nous manquait.

Nous avons juste besoin de ces la variante de ceci.

Donc la variante de ceci, je vais copier ce texte, le coller et avec cette cellule, réglons juste les contraintes pour centrer verticalement et horizontalement.

Et ensuite faire la même chose exacte ici au sein de cette cellule conteneur.

Donc juste rester centré mais il n'y a pas va y avoir un scénario où nous avons besoin de les redimensionner.

Juste pour pour les meilleures pratiques.

Donc avec la variante sélectionnée, nous allons avoir besoin de sélectionner la couleur contenu sur primaire, je sais que nous ne pouvons pas la voir, mais nous allons finir par créer un rectangle avec une largeur de 72 dips et une hauteur de 36.

Et nous allons devoir arrondir les coins de ceci, nous pouvons changer le rayon d'angle à 24.

Là, je vais centrer ceci, placer ceci derrière la typographie, en utilisant command crochet gauche, donc cela change dans l'ordre de superposition.

Et étiqueter cela à superposition d'état.

Et maintenant, nous pouvons aller de l'avant et changer la couleur de remplissage à primaire.

Et nous avons maintenant atteint notre état sélectionné.

Et nous devrions aussi spécifier que la typographie, les deux les deux des alignements sont réglés à texte aligné centre.

Donc ça se redimensionne depuis le milieu, quand vos designers renomment ceci.

Et nous devrions être prêts à partir.

Donc maintenant que nous avons les deux variantes de cellule, allons-y et construisons juste cette vue de sélection d'année.

Donc ici, vous pouvez commencer à voir comment nous construisons ces éléments modulaires pour construire des interfaces entières.

Donc je vais créer ces multiples composants pour avoir celui-ci déjà.

Et nous allons vouloir aller de l'avant et juste déplacer ceux-ci vers le haut.

Et je vais dupliquer cette variante sélectionnée oups.

Quoi de dupliqué cela, ce que nous voulons spécifier est, disons que je vais envelopper ceci dans un cadre étiquette ceci.

Je vais saisir la convention de nommage pour ceci, le mobile Ceci est la vue de sélection d'année mobile, variante de sélecteur de date.

Donc ce cadre sera étiqueté exactement cela.

Et je vais appliquer une couleur d'arrière-plan une couleur de remplissage de surfaces surface.

Donc maintenant, je vais juste étirer cette hauteur, parce que nous n'avons pas défini cela exactement encore.

Mais nous le ferons.

Et vous remarquerez qu'il y a aussi un diviseur étant utilisé dans ce composant, et ensuite le contenu est coupé sous lui.

Donc nous avons trois, cinq.

Donc avec ce composant sélectionné, assurons-nous qu'il est au sein de notre, notre cadre ici.

Donc je vais glisser cela là-dedans, aligner cela à la gauche, m'assurer que c'est a un remplissage gauche de 24 et s'aligne au bas de l'en-tête de calendrier.

Et ce que nous pouvons faire est juste d'aller de l'avant et dupliquer ceci.

Et il vous savez, il y a un espacement de huit dips entre les éléments.

Et j'ai juste frappé Command D pour dupliquer cela.

Et maintenant nous pouvons juste shift sélectionner tous les trois de ceux-ci dans cette rangée.

Et je peux aller de l'avant et juste dupliquer ceux-ci vers le bas, maintenir Command D, et ils sont tous alignés, comme vous pouvez le voir ici, il n'y a pas d'espacement entre eux verticalement, seulement en termes de la largeur, il y a cette gouttière, donc quatre cinq, et ensuite j'ai six, mais je garderai six pour plus tard.

Et ce que nous pouvons faire s'il y a bien trop d'éléments ici, si c'est, c'est difficile pour vous à lire, eh bien, peut-être que nous pouvons juste nettoyer ceci en les sélectionnant dans un format de ligne.

Ou en fait, nous allons vouloir grouper ceux-ci dans un format de colonne, parce que sur mobile, les utilisateurs défileront à travers ceci, ces colonnes verticalement à imaginer par opposition à horizontalement.

Donc vous pourriez créer des prototypes de ce composant dans Figma avec cette mise en page de colonne, donc je vais envelopper ceci dans un cadre, étiqueter ceci colonne, colonne un, cellule colonne un, si vous voulez.

Juste peut-être, peut-être juste l'étiqueter colonne un, cela pourrait être plus facile.

Et ensuite je ferai la même chose exacte pour cet ensemble d'éléments.

Oups, maintenir Command Shift G pour le renommer et ensuite le renommer colonne deux.

Maintenant nous allons aller de l'avant et aborder le troisième.

Très direct.

Groupez-le, renommez-le colonne trois.

Et une chose à propos de ces colonnes est qu'il y a il y a cinq lignes ici, et dans chaque colonne qui sont coupées, il y a une sixième ligne qui est coupée, mais nous allons sauvegarder cela et aller de l'avant et implémenter nos boutons une fois de plus.

Et nous avions déjà créé les boutons annuler et ok ici.

Donc je vais Command+clic Sur ceux-ci, maintenir Shift retour pour sélectionner les calques parents et copier cela.

Et le remplissage réglé à 16 et 16.

Oh, chaque côté, je vais sélectionner le cadre parent ici et coller ceux-ci et les déplacer vers le bas et m'assurer qu'ils sont réglés à 24.

Et je crois, oups, 24 sur la droite, et ensuite 16 sur le bas, ou huit sur le bas, je crois.

Voyons.

Cela semble correct.

On dirait que ça l'est.

Et ensuite nous allons nous assurer que nous avons un diviseur huit dips au-dessus.

Et nous allons aller à notre panneau d'actifs et juste tirer ce diviseur.

et spécifier la largeur ici, nous voulons nous assurer que nous avons cette largeur spécifiée et nous assurer que notre conteneur parent est pour rayon d'angle dip.

Donc avec ce diviseur, besoin de changer la largeur à 328 pour couvrir toute la largeur du du sélecteur de date là.

Je vais glisser cela là-dedans.

pousser cela vers le haut.

Donc c'est huit dips des boutons.

Et maintenant tout ce que nous allons faire est de sélectionner nos colonnes, maintenir Command et glisser cela au pour s'aligner à notre diviseur.

Et sélectionner rogner le contenu.

Et ce que nous allons faire dans chaque rangée est que je vais maintenir colonne, Command D, et ensuite glisser ceci pour que cela s'aligne.

Donc vous pouvez voir que un, quand ce contenu est poussé vers le bas, il oups, le contenu est poussé vers le bas, il est ignoré.

Donc c'est important.

Mais vous ne pouvez pas réellement le voir dans la façon dont nous l'avons spécifié actuellement.

Une chose que nous avons besoin d'ajouter est un état sélectionné, par exemple.

Donc je pourrais aller de l'avant et supprimer ceci, copier cette instance, sélectionner cette colonne et oups, sélectionner la deuxième colonne ou toute colonne et la coller là-dedans.

Et juste s'assurer que c'est aligné correctement.

Et nous savons comment cette votre sélection vue implémentée.

Et nous avons maintenant nos nos vues de sélecteur de date ou votre sélection vue d'eux regardent, copiez juste ceux-ci une fois de plus.

Donc ici nous avons cette colonne.

Mais vous ne pouvez pas réellement la voir, et comment nous l'avons spécifiée actuellement.

Mais vous obtenez l'idée de ce composant, bien qu'il semble être caché.

Donc nous pouvons faire la même chose exacte ici est de dupliquer ceci.

S'assurer que s'alignent correctement.

Et maintenant j'ai ces vues de colonne construites et nous sommes prêts à partir nous avons notre vue de sélection d'année.

Donc si je voulais jamais en fait échanger ce composant avec un sélectionné, dû à nos conventions de nommage, nous pouvons aller de l'avant et faire cela très, très rapidement dans notre instance, menu déroulant.

Et c'est notre vue de sélection d'année.

Faire de cela un composant principal.

Aller de l'avant et glisser cela là-bas.

Et maintenant que celui-là spécifié nous avons créé.

Allons-y et abordons l'une des vues plus complexes.

Donc avec cette vue calendrier.

Allons-y et copions cette convention de nommage.

Ici sur mobile, nous avons la vue calendrier, nous pouvons clairement utiliser l'en-tête de calendrier mobile mobile.

Donc nous avons cela.

Donc notre calendrier mobile additionneur fait, nous allons l'envelopper dans un cadre, il va être appelé mobile / calendar view.

Et nous allons spécifier la hauteur pour être 512.

Oups.

Et une fois que c'est réglé à 512, nous allons régler la couleur de remplissage à surfaces surface.

Et encore une fois, cette vue de sélection d'année a en fait je m'excuse, un style d'effet 24 dips, et donc cette vue calendrier donc allons-y et spécifions cela et dans cet élément besoin d'aller de l'avant et changer ce style de couleur 000 à texting et iconography haute emphase.

Maintenant que tout est attaché les styles de couleur sont prêts à partir.

Et sur ce calendrier, vous spécifierez le rayon d'angle à quatre dips.

Donc maintenant que nous avons cela, nous devons commencer à créer ces cellules individuelles.

Donc dans ce format, nous allons aller de l'avant et spécifier la date ici.

Donc c'est utiliser une cellule de 40 par 40 dips.

Donc faire ce cadre 40 par 40, régler le remplissage à surfaces surface et copier ce textile pas donc, le coller ici, et le centrer et juste la seule différence étant la couleur.

Donc ceci utilise une emphase moyenne, style de couleur.

Donc nous devons spécifier cela régler cette emphase moyenne, je peux même dupliquer ceci, oups, peux le dupliquer, je suis sûr que c'est réglé à un nombre maintenant.

Et c'est centré.

Et les nombres ont un style de couleur haute emphase.

Nous allons avoir besoin de nommer ces cellules.

Donc nous avons nous avons le c'est un élément.

Et c'est la date, cell day SEL.

de sel.

Et ensuite nous allons aller de l'avant et copier cela spécifier ceci comme comme les éléments date.

Day, donc maintenant date, number.

Donc vous pouvez le nommer honnêtement, ce qui a le plus de sens pour vous ou votre équipe ou organisation.

Et ensuite, bien sûr, nous allons avoir besoin d'une variante Ace non sélectionnée, ce qui est ce que cela sera.

Et ensuite nous aurons une variante sélectionnée aussi.

Si je vais de l'avant et change cela à sélectionné.

Et avec la variante sélectionnée, nous allons avoir besoin de sélectionner la couleur contenu sur primaire, je sais que nous ne pouvons pas la voir, mais nous allons finir par créer un rectangle réglé 36 par 36 dips.

Avec les couleurs primaires quand vous changez ce style de couleur à contenu sur primaire, ensuite aller de l'avant et créer un rectangle au sein du cadre.

régler cela à 36 ou 36 dips et rond, l'arrondir et ensuite le centrer et utiliser Command crochet gauche pour le pousser vers l'arrière.

Et notre maintenant que nous avons cet état sélectionné, nous devons changer la couleur de remplissage à primaire.

Et nous avons maintenant notre style de texte réglé correctement.

Donc nous pourrions vouloir pousser cela d'un pixel car cela ne semble pas centré optiquement.

Mais maintenant ça l'est puisque nous le poussons.

Et avec cela nous pouvons aller de l'avant et faire de cela un composant principal.

Et tout devrait s'échelonner en conséquence.

Je réglerai les contraintes correctement à l'état sélectionné aussi.

Et cette typographie est prête à partir faire de cela un composant principal et faire du jour date un composant principal et le composant d'élément de nombres date.

Et nous devrions être prêts à partir.

Tout ce que nous avons à faire est de commencer à composer cela en conséquence.

Donc dans cette variante, vous pouvez voir que les dates sont affichées et elles s'alignent on dirait juste en dessous du juste en dessous de l'en-tête de calendrier.

Donc je vais faire cet alignement et le remplissage gauche est réglé à 24.

Et tout ce que je vais faire est de dupliquer ceci et m'assurer que c'est pour quatre dips à la à la droite.

Et ensuite je vais le dupliquer à nouveau et continuer à le dupliquer.

Et puisque j'ai cet espacement spécifié, je suis prêt à partir voir un doublon.

Maintenant que j'ai ces trois, six, j'ai besoin d'appliquer ces sept jours ici dans la semaine.

Et j'ai maintenant que je vais aller de l'avant et double vérifier mon espacement ici.

Donc l'espacement n'est pas supposé être réglé 24 sur la gauche, c'est supposé être réglé à 12 pour pour les cellules et cela sélectionnant réellement la date et je l'ai réglé à 24.

Donc mes excuses.

Pour maintenant maintenant le contenu est centré correctement et maintenant ce que nous allons faire est d'aller de l'avant Sélectionner notre cellule de nombre date et dupliquer cela et aligner cela ici.

Donc c'est jour un.

Et ensuite nous allons aller de l'avant et créer une rangée entière de ceci.

Et ça va être très simple, je vais aller de l'avant et créer une rangée avec vous.

Donc tout ce que nous avons à faire est de le dupliquer, s'assurer qu'il y a quatre pixels d'espacement entre tous les éléments ici.

Et je vais juste continuer à répéter cela tout le long à travers toute la rangée.

Et je vais juste faire la même chose, sélectionner tous ces éléments, et s'assurer qu'ils s'empilent tous.

Et juste dupliquer cela encore et le dupliquer encore, et j'ai mon, mon 556 rangées dans son intégralité.

Et nous avons juste besoin d'une de plus, nous avons besoin de celle du bas, qui est jour 32.

Aller de l'avant et vérifier cela.

Et ce que nous pouvons faire, puisque nous avons nos composants nommés correctement, je peux cliquer sur ceci et m'assurer que c'est l'état sélectionné.

Et je vais mettre en pause cette vidéo et aller de l'avant et ajouter dans ces boutons et aussi renommer tous ces jours.

Donc je reviendrai tout de suite.

Maintenant j'ai créé cette vue de calendrier mobile.

Et tout ce que j'ai fait était que j'ai copié les boutons de notre vue de sélection d'année, parce que les spécifications d'espacement sont les mêmes sur cette vue de calendrier.

Donc j'ai collé cela dedans par et je l'ai collé une fois que j'ai sélectionné le conteneur parent.

Et cela m'a fait une grande faveur et a juste appliqué cette même position exacte.

Et voilà, nous avons notre vue de calendrier, mûrir le nouveau composant principal maintenant.

Et nous avons nous avons un peu démystifié la complexité de ceci et la seule chose manquante est cette date actuelle.

Donc c'est la cellule de date actuelle.

Donc ce que nous allons faire est de dupliquer la cellule de nombre date qui est sélectionnée, et ensuite nous allons détacher cela, et je vais aller de l'avant et renommer ceci à date actuelle car c'est une cellule spécifique.

Et ensuite, avec la date actuelle spécifiée, je vais sélectionner mon rectangle et appliquer un contour d'un pixel.

C'est, devrait être réglé à voyons surfaces haute emphase, et nous allons supprimer ce remplissage.

Et nous allons aller de l'avant et sélectionner notre texte maintenant et s'assurer que le contenu est réglé à actif ou haute emphase.

Donc c'est notre variante de date actuelle de la cellule.

Donc ce que je peux faire est de faire de cela un composant maître ou composants principaux utiliser moi.

Et ensuite nous pouvons même aller de l'avant et sélectionner cette cellule dans notre vue calendrier maintenant.

Et maintenant nous avons une variante de date actuelle.

Donc maintenant nous avons cela.

Et avec notre variante de date actuelle, je vais en fait pousser ce pixel un pixel vers la droite, oups, un pixel vers la gauche, le rendre plus optiquement aligné.

Et nous sommes maintenant prêts à partir.

Et maintenant nous pouvons aller de l'avant et mettre cela de côté dans la vue calendrier.

Nous avons les cellules appropriées nécessaires pour nos nos calendriers pour mobile.

Et nous avons aussi un sélecteur de plage mobile, que je vais mettre de côté et vous laisser vous mettre au défi et construire cela.

Et essentiellement avec cette superposition, ce que vous allez vouloir faire est de juste créer un élément que vous pouvez superposer ou placer sous toutes ces rangées ici, ce sont les cellules pour voir cet effet en conséquence.

Donc ce que nous pouvons faire dans en fait notre, notre composant calendrier est d'aller de l'avant et commencer à sélectionner tous ceux-ci.

Et vous pourriez les mettre dans des colonnes ou des rangées au besoin.

Donc par exemple, ce que vous et votre équipe trouvez le plus efficace, je peux spécifier ceci comme rangée trois.

Ici, vous pouvez clairement voir que nous avons rangée rangée un.

Donc rangée un, et ensuite ceci se trouve être rangée deux.

Donc c'est important.

Et je viens de réaliser que j'ai gâché cette vue calendrier, nous avons besoin que cette vue calendrier s'empile correctement.

Donc si je vais de l'avant et clique sur cette vue calendrier, ce n'est en fait pas positionné correctement.

Donc j'ai besoin d'aller de l'avant et ce que je vais faire est de mettre en pause ceci et de faire de toutes celles-ci des rangées et je vais et m'assurer que je pousse cet élément vers le bas et je reviendrai sur mon élément aligner correctement et je les ai groupés en rangées.

Même s'il n'y a qu'un élément sur cette rangée, disons que vous deviez construire toute cette rangée à l'avenir, vous pourriez étirer ceci et l'aligner, vous pouvez vous assurer que la largeur s'est alignée correctement.

Et ensuite si vous aviez besoin de le modifier, vous pouvez aller de l'avant et dupliquer insérer des éléments s'alignant à la, à la fin et au milieu de vos éléments au besoin.

C'est juste une façon rapide de garder les choses organisées.

Et juste aussi juste garder ces calques propres, c'est fortement recommandé, comme vous pouvez le voir ici, et ceux enveloppés dans des cadres.

Sinon, c'est une tonne de cellules étant juste vues quand vous l'étendez dans le panneau Calques.

Donc c'est pourquoi nous avons notre vue compteur faite.

Et je vais vous mettre au défi de construire cette cette autre vue, le sélecteur de plage mobile aura un état sélectionné.

Et pour l'état sélectionné, vous aurez les deux mois aussi.

Donc vous pouvez détacher l'éditeur de calendrier et copier ceux la propriété fiscale et ainsi de suite.

En Ouais, vous avez juste besoin de créer comme un élément d'état sélectionné, transformé cela en composant, et ensuite juste mettre cela sous les rangées.

Et vous pouvez référencer la vue calendrier pour cela.

Donc maintenant nous allons aller de l'avant et aborder une variante du bureau.

Le bureau est légèrement différent.

Puisque c'est sur un plus grand appareil, vous remarquerez que c'est très dense.

sur le bureau, ici, nous avons une vue très dense, où les cellules pour la variante de bureau sont réglées à 32 par 32 dips ici.

Mêmes mêmes états pour chaque cellule, nous avons la date actuelle, nous avons la date sélectionnée, et ensuite nous avons celle par défaut ici.

Et ouais, je veux dire, nous sommes et ensuite nous avons aussi l'une des plus complexes, le sélecteur de plage de date, où c'est le où vous sélectionnez d'un mois à un autre mois.

Et nous allons aller de l'avant et construire ce sélecteur de plage de date.

Et ensuite je vais vous mettre au défi de construire le les sélecteurs de plage de date suivants par vous-même car c'est une vidéo très dense d'informations qui ne devrait pas être une bonne pratique pour vous.

Donc nous allons aller de l'avant et commencer par identifier les éléments de bas niveau.

Donc avec cela dit, nous, nous avons ici, des cellules réglées à 32 par 32.

Et ensuite nous avons ces icônes.

Donc je vais aller de l'avant et saisir ces cellules ici.

Puisque nous avons, puisque nous avons appliqué des contraintes à ces cellules, tout ce que nous avons à faire est de les détacher, les renommer correctement.

Et maintenant que je réalise cela, nous allons devoir catégoriser ces cellules.

Donc celles-ci vont être les versions mobiles.

Donc nous allons devoir catégoriser toutes celles-ci pour vivre sous sous mobile, parce que nous allons avoir des cellules pour bureau aussi.

Donc je vais juste dedans, et juste renommer certains éléments ici.

Juste appliquer mobile.

Donc juste aller dedans copier et coller très vite.

Et une fois que vous avez fait cela, vous devriez être prêt à partir.

Et maintenant la chose agréable à ce sujet est, puisque nous avons renommé toutes celles-ci à mobile, nous pouvons aller de l'avant et copier toutes ces variantes, nous pourrions ne pas avoir besoin de celles-ci au début, mais je vais détacher ces instances.

Et nous pouvons aller de l'avant et changer si nous renommons par lot en sélectionnant tout, et ensuite frapper command R, et ensuite je tape mobile, je peux alors descendre à ce remplacer par et taper desktop.

Donc maintenant j'ai mes variantes de bureau.

Si nous regardons dans les calques ici, nous avons nos cellules de bureau.

Et puisque nos contraintes sont réglées correctement pour centrer, nous pouvons juste modifier le conteneur parent et tout se redimensionnera correctement donc cela c'est très utile.

Une chose que nous allons vouloir faire est de créer cet état sélectionné ici, ce sélectionné cette cette plage ici de la entre la la date actuelle, la date sélectionnée, la date de début, et la date de fin.

Donc nous allons vouloir faire est de créer cela maintenant.

Donc nous devons nous assurer que nous savons à quelle hauteur de ce jour est réglée donc nous cela pourrait être référencé Dans une autre spécification, cette date sélectionnée là, voyons.

sur bureau la hauteur de cela, plus que probablement réglée à 28.

dips en hauteur, ralentir mon aller avec.

Ouais, ouais, réglé à 28.

Maintenant avec cela dit, allons-y et commençons juste à sortir cela, je vais saisir les icônes, j'ai besoin ici, mes, mes flèches ici, gauche et droite, je vais avoir besoin de ma copie de cette année.

Nous n'avons pas besoin de flèche déroulante.

Donc je vais supprimer cela.

J'ai besoin de ce textile de légende.

Sûr que c'est réglé à haute emphase aussi.

Aller changer cela ici, s'assurer que c'est réglé à haute emphase.

Savoir que c'est systématisé, nous pouvons aller de l'avant et avancer, nous avons un cadre ici.

Et allons-y et saisissons ce nom ici, sélecteur de plage de date de bureau.

Donc maintenant que j'ai copié cela, sélectionnez ce nom parent, cadre parent.

Et nous allons aller de l'avant et régler le rayon d'angle à quatre.

Et nous avons une hauteur de largeur de 512 dips et une hauteur de 280.

Et avec cela, nous pouvons rouler.

Donc une chose que nous pouvons faire est de nous concentrer sur le calque de base de des ces composants.

N'est-ce pas ? Donc qu'est-ce que le calque de base ? Eh bien, les choses qui ne vont pas bouger qui resteront en place est et qui seront aussi dynamiques dépendantes du mois puisque sont des jours spécifiques et chaque mois.

Donc cela changera toutes ces cellules.

Donc cela variera dans le combien de rangées ils seront, il y aura et combien de cellules dans chaque rangée.

Mais les jours resteront.

Et la flèche et le mois resteront dans ce diviseur.

Donc nous allons aller de l'avant et ajouter ce diviseur, ce diviseur prend toute la hauteur de ce, ce sélecteur de plage de date.

Donc si nous allons à notre panneau d'actifs, option pour tirer ce diviseur, je vais frapper Command Shift Option taper rotate left, et ensuite je vais maintenant je l'ai verticalement réglé.

Et c'est déjà dans mon cadre parent dans le conteneur parent, ce qui est génial, je vais régler la hauteur à 280.

Donc ensuite je vais juste maintenir Option v option h.

Donc maintenant c'est horizontalement aligné parfait.

Li entre les deux côtés ont ce sélecteur de plage de date, comme indiqué ici.

Et si nous ne l'avons pas déjà fait, allons-y et changeons ce remplissage à surfaces surface.

Appliquer lèvres, planifier le style d'effet de huit dips, car c'est utilisé dans les menus et sous-menus, comme un menu ou sous-menu.

Et maintenant nous allons aller de l'avant et ajouter dans nos, nos flèches.

Donc avec cela dit, nous allons ajouter cette flèche ici, ajouter la deuxième flèche là.

Et c'est 16 dips depuis le haut et la droite.

Donc si j'aligne cela, oups 16 dips depuis le haut et la droite, nous sommes prêts à partir là.

Et avec cela appliqué maintenant nous devons aller et copier ce textile.

Et septembre ici semble être un 32 dips de la ligne de base à travers deux chiffres depuis le haut du conteneur parent.

Et l'espacement semble être aligné.

Centre horizontalement entre ces éléments spécifiés ici.

Donc si nous faisons 256 moins 32, nous obtenons 224.

Donc si nous créons un cadre de, de 224 chiffres large.

Donc si j'enveloppe ceci dans un cadre, étiquette ceci comme rangée un ou en-tête rangée en-tête, j'étiquette juste cela en-tête.

Quand je spécifie ceci à 224, vous remarquerez que cette distance me donne 16 chiffres à la droite.

Et pourquoi j'enveloppe ceci dans un cadre est parce que quand je copie ce texte ici, et je le colle dans cet en-tête.

Donc je vais le coller là-dedans.

Et c'est dans ce cadre parent.

Donc je vais aligner verticalement et aligner horizontalement pour que ce soit vertical ici sur le côté calendrier.

Et une chose que je pourrais même faire est, si je voulais, je, si je ne veux pas répéter cela, je peux supprimer cette icône.

Et ce que je peux faire est de sélectionner l'icône ici, et Maintenir OPTION D et aligner cela à la droite et ensuite frapper Shift H et cela s'aligne correctement.

Et maintenant j'ai cet espacement réglé de manière appropriée.

Donc c'est génial.

Donc maintenant nous avons septembre et octobre.

Donc je peux renommer cela.

Et une chose que nous voulons nous assurer est que c'est réglé à texte aligné centre sur les deux éléments.

Et nous allons aller de l'avant et spécifier que la cette typographie centre horizontalement en termes de quand elle se redimensionne.

Donc c'est important.

Donc allez-y, changez cela à octobre 2019, ensuite nous changerons ceci à sep tember 2019.

Et nous devrions être prêts à partir.

Génial.

Donc avec cela spécifier, nous avons l'en-tête gauche.

Et ensuite nous avons l'en-tête, droite.

Et ceux-ci pourraient tous deux être catégorisés sur la gauche, comme mois, gauche et mois, droite.

Donc nous allons commencer avec ces jours ici pour la vue de bureau.

Et encore une fois, là, ils ont une hauteur de 32 par 32 dips, ce que nous avons déjà spécifié ici.

Et ce que nous voulons faire est que je vais sélectionner toutes ces cellules ici.

Et maintenant je veux en fait aller de l'avant et redimensionner celles-ci à 32.

Et notez que tout le contenu centré et ensuite il a été recadré, n'est-ce pas.

Mais la raison pour laquelle cela a été recadré est parce que nous devons spécifier cela pour avoir une hauteur et une largeur de 28.

Et ensuite je vais aller de l'avant et centrer cela une fois de plus.

Et je vais faire la même chose exacte pour le type de cellule date actuelle.

Donc maintenant et ensuite juste centrer cela maintenant nous sommes prêts à partir.

Nous avons poussé nous sur un pixel pour que ce soit centre et nos éléments ici.

Avec ce centre, nous sommes prêts à partir.

Donc maintenant je vais créer ces multiples composants principaux.

Et je peux copier cette cellule desktop Daiso est ce à quoi c'est actuellement étiqueté comme.

Et je vais spécifier la date sur les deux côtés gauche et droit.

Et comme vous pouvez le voir ici, l'espacement ici entre l'icône au-dessus et entre les dates n'est pas spécifié pourrait être spécifié ici, c'est réglé à 12.

Comme vous pouvez le voir, réglé à 12.

Donc nous pouvons aller de l'avant et implémenter cela ici, sélectionner ce sélecteur de plage de date, le coller, pas option, un aligner cela dans 60 réglé à 16 dips dans la gauche et les espacements 12 déjà par défaut.

Donc c'est génial, je peux aller de l'avant et juste copier ces dates.

Et maintenant j'ai tous les sept jours ici spécifiés.

Et ce que je peux faire est de sélectionner tous ceux-ci dès le départ mon panneau Calques, les grouper, les étiqueter.

Row days, je peux étiqueter ceci comme row days ou tout ce que vous trouvez le plus intuitif ou le plus efficace.

C'est ce que je recommande.

Et ensuite je vais m'assurer qu'il Whoa, que l'espacement ici est réglé de manière appropriée.

Et une fois que c'est réglé correctement, nous sommes prêts à partir.

Avoir ces jours ici.

Road days, gauche, pousser cela vers le haut.

Oups.

Et ensuite je vais organiser ceux-ci dans mon panneau Calques en conséquence, l'en-tête droite et ensuite les road days, droite.

Et ensuite, nous allons vouloir juste aller de l'avant et commencer à implémenter nos nos jours ici.

Et ce que je vais faire est juste de copier cette date nombre donc pour le bureau, le coller et avec cela, nous l'avons maintenant une ligne déjà.

Et ensuite nous allons juste créer ces rangées ici et il n'y a pas d'espacement entre ces cellules.

Donc je peux juste continuer à aller Frapper Command D pour répliquer cela.

Ensuite je peux grouper ceci, étiqueter ceci rangée trois, rangée trois gauche, ensuite je peux étiqueter ceci, oups, je peux grouper ceci aussi, route vers la gauche.

Et ensuite ce que je peux faire est juste de continuer à dupliquer ceci vers le bas, et juste m'assurer que ceux-ci incrémentent correctement.

Donc c'est rangée quatre.

Et ensuite nous avons rangée cinq ici en action, et ensuite nous avons, nous avons rangée six.

Donc nous allons aller de l'avant et vérifier combien de rangées sont nécessaires ici.

Pour ce jour, nous avons, nous avons cinq, six, au total, nous avons 1234, nous avons besoin de créer une rangée de plus semble comme elle ne semble pas juste, oups, je vérifie le mauvais 1234566 au total.

Donc nous avons 123456.

Et cette rangée, nous avons seulement obtenu, oh, nous avons seulement un ici spécifié un jour sur la dernière rangée, et il y a un remplissage de huit dip, huit pixels là sur le bas.

Donc j'ai besoin d'aller de l'avant et vérifier cela actuellement, c'est réglé à quatre, je ne sais pas pourquoi c'est.

Et ensuite le remplissage sur le dessus réglé à 16.

Et le bas est réglé à huit.

Et ensuite j'ai la hauteur réglée à 280.

Mais cela me demande toujours avec des dimensions de quatre sur le bas, ce que je ne comprends pas.

Donc ce que nous pouvons faire est d'aller de l'avant et sélectionner notre cadre parent et juste spécifier cela à huit.

actuellement réglé à sept.

Donc je vais juste pousser cela vers le bas d'un pixel de plus.

Et là nous l'avons, nous avons maintenant cette variante ici faite, je vais je vais aller de l'avant et mettre en pause ceci et faire cet autre côté et vous devriez faire de même.

Et je vais juste nommer tout en conséquence.

positif.

Donc maintenant j'ai créé ces rangées ici sur le côté droit.

Donc je vais juste vous permettre d'aller de l'avant et d'ajouter toutes les dates et jours ici pour que ce soit précis.

Et vous pouvez l'aligner avec ce qui est spécifié dans la spécification ici.

Et je vais vous mettre au défi de faire ce sélecteur de date de bureau par vous-même.

Et la vue de sélection d'année, nous avons déjà les éléments ici prêts et nommés correctement pour le système de design.

Et vous avez juste besoin de redimensionner ceux-ci une année cellules de sélection.

Et une chose que vous pouvez je vais passer en revue avec vous mais pas construire en pilote je vais juste vous guider est créer cette sélection de plage de date.

Donc ce que vous allez vouloir faire pour représenter cette sélection de plage, nous allons j'ai dupliqué ceci et juste enlevé le le remplissage et changé cette couleur ici sur la forme à primaire basse emphase.

Et j'ai changé les contraintes pour que les contraintes de ceci soient sur cet élément, j'ai besoin de le détacher Mon mauvais.

Maintenant j'ai besoin de sélectionner la forme et régler les contraintes à gauche et droite.

Donc de cette façon, quand je sélectionne le conteneur parent, je peux l'étirer correctement.

Donc je peux je peux obtenir cette plage dont j'ai besoin.

Et sous plage, je vais sélectionner des décès, ça va être nommé elements / desktop / range selection.

Donc c'est ça maintenant que nous avons cela vous pouvez aller de l'avant et vous savez, faire de cela un composant principal, et vous pouvez le copier.

Et ensuite comment vous l'utiliseriez est si vous le collez dans votre sélecteur de plage de date, vous allez vouloir le placer derrière tous vos calques ci-dessous et l'aligner avec la hauteur et la taille de la votre zone de texte.

Et ensuite vous pouvez aller de l'avant et commencer à étirer cela au besoin pour sélectionner vos dates.

Et notez que tout est prêt à partir à cet égard.

Et il y a un état où c'est juste une cellule à.

Donc c'est génial.

Et c'est tout ce que j'ai à vous montrer aujourd'hui.

Les gars, je vous mets au défi de faire ceci, ces autres variantes de bureau et cette variante mobile et avec toute cette connaissance vous devriez vous avez toutes les cellules et tout le nécessaire.

Dans pour construire la suite.

Et merci beaucoup d'avoir regardé.

Et c'était un long, espérons que vous avez appris beaucoup, et comment déconstruire ces images et en fait transformer ceci en un système.

Je sais, c'est difficile, mais très gratifiant pour vous.

Si vous pouvez obtenir ceci dans votre mémoire musculaire, en tant que designer, vous deviendrez un designer de système de design très précieux et designer.

Aujourd'hui, nous allons construire quelques diviseurs très directs.

Et nous allons couvrir comment ils sont utilisés, et ensuite juste les créer, ce sera super rapide et facile.

La partie la plus longue sera juste de décrire l'utilisation.

Donc un diviseur est une ligne mince qui groupe le contenu dans des listes et des mises en page.

Comme vous pouvez le voir, ici, nous avons un tas de composants de liste, et ils sont en train d'être divisés dans leurs propres sections légitimes avec ce diviseur, comme vous pouvez le voir, ici, nous avons obtenu cet élément diviseur.

Et cela parle des principes derrière cela.

Donc c'est juste utilisé pour séparer le contenu en groupes clairs.

Et ici vous pouvez voir que c'est lourdement utilisé dans la messagerie.

Et cette boîte de réception, ils utilisent des lignes pour compartimenter chaque message étant envoyé et reçu.

Et ici, vous pouvez utiliser diviseur ici vous voyez des diviseurs, divisant la description de cette image et sa tarification.

Et ensuite aussi, c'est diviser ce contenu où c'est très descriptif au-dessus et ensuite où il y a quelques actions en dessous et diviser ce contenu.

Et ici nous avons un diviseur étant utilisé pour diviser cette page de ce qui ressemble à des contacts.

Et il y a beaucoup d'excellent contexte approfondi ici, je recommande fortement que vous lisiez à travers, cela vous permettra de prendre des décisions plus intentionnelles sur vos designs à l'avenir.

Et améliorera juste votre jeu en tant que designer.

Et voici quelques exemples de diviseurs étant utilisés dans certains thèmes de design material tels que le thème étiqueté fortnightly et hibou thème material.

Et ici vous pouvez voir à quoi cela ressemblerait, un diviseur ressemblerait sur un sur cet arrière-plan primaire.

Et ensuite aussi les acclamations juste les spécifications, qui est maintenant dans Figma.

Nous allons aller de l'avant et créer cela.

Donc très direct.

C'est un pixel en hauteur.

Et nous allons juste régler cela à la largeur d'un appareil Android, qui est 30 à 60 dip.

Donc si je frappe l sur mon clavier, cela crée le le diviseur la ligne, donc je vais régler la largeur à 360 et la hauteur à un pixel.

Donc maintenant j'ai Whoa, oups, je vais inverser cela.

Donc la largeur est 360.

Et nous avons maintenant cette ligne.

Mais la chose, le problème avec cette ligne est que nous avons besoin d'aplatir ceci.

Donc quand je dis aplatir, nous avons en fait besoin de contourner le trait, parce que nous avons essentiellement un trait comme vous pouvez le voir ici.

Et quand nous volons cette rangée, vous remarquerez dans le panneau Propriétés, cela se mettra à jour, et nous irons à contourner le trait, et cela deviendra maintenant Phil.

Et pourquoi voulons-nous cela mur, j'aurai deux exemples pour nous, parce que cela nous aidera quand il s'agit de mesurer des éléments.

Parce que maintenant ce trait est centré.

Donc cette ligne bleue est le centre de où les choses seront mesurées.

Et vous remarquerez que cela ne nous donne pas en fait une mesure appropriée.

Donc si nous voulons séparer un groupe de texte ici, et nous avons cette zone de texte spécifiée, vous voyez comment c'est 60.

Eh bien, si j'ai ceci aligné, donc ce sont tous les deux des traits.

Si je vais de l'avant et maintenant change ceci de trait, vous remarquerez que la distance est 60 dips.

Mais regardez, quand je change ceci à un contour, trait, je contourne le trait, cela le changera en un remplissage.

Et ensuite vous remarquerez que maintenant la distance est réglée à 59 pixels.

Donc le point auquel j'arrive est pour être aussi précis que possible avec ces diviseurs, nous devons nous assurer que nous les aplatissons.

Et aplatir est juste un terme pour vous voyez comment il y a cette ligne ici.

Et ensuite quand je l'aplatis, c'est c'est en fait un ce n'est plus un trait, donc ce n'est pas au centre de cela avoir le trait.

Donc c'est maintenant essentiellement un peu comme un rectangle d'un pixel qui est très mince, vous pouvez penser à cela comme fini avec cela étant dit, les mesures seront plus précises.

Et c'est exactement ce que nous essayons d'atteindre.

Par opposition à ce ce mot de trait réglé à 60 en distance et ce ce trait aplati qui n'est plus un trait est réglé à 59 donc c'est en fait plus précis.

Donc c'est génial.

Nous avons cela là.

Et tout ce que nous avons à faire est d'appliquer le bon style de couleur et vous devez vous assurer que votre bibliothèque de système de design material est activée dans ce fichier, comme toujours, et nous allons aller de l'avant et sélectionner nos styles de couleur et aller au contenu et sélectionner la surface sur Lequel est utilisé pour les diviseurs ici.

Et encore une fois, vous pouvez voir que la couleur spécifiée sur ce diviseur est réglée à 00, qui est noir et utilise l'opacité de 12%.

Donc c'est très léger, et subtil.

Et certaines choses importantes à noter sont que d'autres systèmes de design spécifient plusieurs diviseurs, qui est essentiellement juste utiliser différents styles de couleur.

Et avec ces différents styles de couleur, c'est juste communiquer.

Vous pourriez communiquer différents niveaux d'opacités.

Par exemple, je détache ceci, disons que c'était le diviseur régulier réglé à 12%.

Mais nous avions un autre diviseur que nous voulions être plus proéminent en couleur, nous pouvons en fait augmenter cette opacité.

Peut-être que je augmente juste cela à 80% 87%.

Et si nous voulions une sorte de, par exemple, diviseur muet, oups, voyons ici, dupliquer cela nous voulions un diviseur muet, nous pourrions juste changer cette opacité, encore, pour représenter différents niveaux de proéminence dans le diviseur, et comment vous voulez que cela comment visible vous voulez que cela soit sur vos designs.

Donc c'est, c'est une façon de s'y prendre pour construire des choses.

Mais dans material design, nous avons juste ce diviseur unique, et je vais juste étiqueter cela comme régulier c'était juste un exemple pour vous tous, et juste réappliquer ce contenu surface overlay on surface style de couleur, nous avons maintenant notre diviseur et je vais aller de l'avant et l'étiqueter dividers espace slash espace et ensuite divider.

Donc c'est génial.

En fait, je peux aller de l'avant et juste étiqueter ceci comme divider et faire de cela un composant maître composant principal, excusez-moi, et nous sommes prêts à partir.

Et c'est tout ce que nous avons à faire pour créer un diviseur et merci beaucoup d'avoir regardé.