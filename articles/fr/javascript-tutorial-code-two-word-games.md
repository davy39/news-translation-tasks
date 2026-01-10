---
title: Tutoriel JavaScript – Coder Deux Jeux de Mots
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-07-06T14:59:15.000Z'
originalURL: https://freecodecamp.org/news/javascript-tutorial-code-two-word-games
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/maxresdefault.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: youtube
  slug: youtube
seo_title: Tutoriel JavaScript – Coder Deux Jeux de Mots
seo_desc: 'Coding games is a fun way to improve your JavaScript skills.

  We just published a full course on the freeCodeCamp.org YouTube channel that will
  teach you how to code two word games in JavaScript.

  Ania Kubów developed this course. Ania works for freeCo...'
---

Coder des jeux est une manière amusante d'améliorer vos compétences en JavaScript.

Nous venons de publier un cours complet sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à coder deux jeux de mots en JavaScript.

Ania Kubów a développé ce cours. Ania travaille pour freeCodeCamp et possède une chaîne YouTube de tutoriels populaire.

Dans ce tutoriel JavaScript, vous apprendrez à créer un jeu de type Jeopardy et un jeu d'associations de mots. Ce tutoriel est destiné à ceux qui ont déjà appris les bases de JavaScript.

Le jeu Jeopardy a été adapté pour bien fonctionner pour un seul joueur. Vous marquez des points en répondant correctement aux questions.

Dans le jeu d'association de mots, on vous donne trois mots et vous devez ensuite choisir l'une des deux options qui sont associées aux trois mots donnés. Le nombre total de points est basé sur le nombre de réponses correctes et incorrectes que vous choisissez.

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=vYEkEMfoi1c) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=vYEkEMfoi1c]

### Transcription

(générée automatiquement)

Bonjour à tous sur freeCodeCamp.

Je m'appelle Ania Kubow et je suis développeuse logicielle, ainsi que votre guide pour ce tutoriel JavaScript amusant. Dans ce tutoriel JavaScript, nous allons créer deux jeux de mots, c'est-à-dire un jeu de type Jeopardy que j'ai adapté pour bien fonctionner pour un seul joueur et un jeu d'association de mots.

Ce tutoriel sera pour ceux qui ont appris les bases de JavaScript et veulent pratiquer quelques jeux amusants.

D'accord ? Donc il y aura beaucoup de travail avec des objets, des tableaux, des boucles et tout ça.

En fait, voici une liste complète de toutes les propriétés et méthodes JavaScript que nous allons utiliser dans ce tutoriel.

Alors, analysons le premier jeu.

Le premier jeu sera mon jeu adapté de Jeopardy.

Comme vous pouvez le voir ici, la signalisation est très basique.

C'est un tutoriel JavaScript.

D'accord.

Je ne vais pas me concentrer autant sur le style, car cette partie vous appartient dans ce jeu.

Lorsque vous retournez une carte, vous ne pourrez pas retourner aucune des autres cartes jusqu'à ce que vous répondiez à la question.

Et si vous répondez correctement, vous obtenez des points.

Et bien sûr, si vous ne répondez pas bien, pas de points pour vous.

Et dans le prochain jeu d'association de mots, vous aurez des cartes qui seront peuplées à partir d'un tableau et vous devrez essentiellement obtenir le mot associé aux trois indices ci-dessus.

Si vous obtenez la bonne réponse, vous obtenez un point et si ce n'est pas le cas, c'est un moins un point pour vous.

Le nombre total de points sera reflété en fonction du nombre de réponses correctes et incorrectes que vous choisissez.

D'accord.

Alors, qu'attendons-nous ? Commençons à pratiquer un peu de JavaScript.

D'accord.

Alors, commençons.

Je vais commencer par créer mon projet.

J'utilise WebStorm comme mon éditeur de code ou mon IDE technique de choix, mais n'hésitez pas à utiliser l'éditeur de code que vous souhaitez, comme FIS code ou autre.

D'accord.

Donc, ce que je vais faire, c'est simplement aller de l'avant et créer un nouveau projet et je vais appeler cela association de mots

Jeu.

D'accord.

Donc, c'est tout ce que je vais l'appeler et il sera stocké dans mon répertoire de projets WebStorm.

Et je vais simplement cliquer sur créer.

Donc, nous y voilà.

Vous verrez un répertoire appelé jeu d'association de mots qui a été créé.

La prochaine chose que je veux faire est d'ajouter les fichiers nécessaires.

Donc, ce sera un fichier HTML.

Je vais simplement l'appeler index HTML.

Vous pouvez mettre l'extension, mais comme j'ai choisi le fichier HTML, il sera simplement ajouté pour moi.

Donc, nous y voilà.

Nous disons à notre éditeur de code de choix de traiter cela comme un fichier HTML.

Super.

Et nous allons simplement l'appeler mot a so ation.

D'accord.

Peut-être faisons-le un peu plus grand.

Donc, le voici.

Le prochain fichier que nous allons créer est pour notre feuille de style.

Donc, je vais cliquer sur feuille de style et appelons les styles et je vais simplement sélectionner le fichier CSS pour ceux d'entre vous qui n'utilisent pas webstore, tapez simplement CSS et cela devrait être créé pour vous.

Donc, maintenant notre éditeur de code sait qui traiter cela comme un fichier CSS.

Un de plus et c'est un fichier JavaScript.

Donc, celui-ci, je vais simplement l'appeler app et appuyer sur entrer une fois de plus, si vous n'utilisez pas webstore, assurez-vous de mettre l'extension .JS afin que votre éditeur de code sache qui traiter cela comme un fichier JavaScript.

Super.

Donc, maintenant que nous avons les trois fichiers, ce que je dois faire est de connecter ces deux fichiers à mon fichier index HTML.

Donc, nous allons le faire maintenant avec une balise de lien et une balise de script.

Donc, les feuilles de style, nous le faisons en fait entre les deux balises ahead.

Je vais obtenir la balise de lien comme ceci, donc c'est en fait une balise auto-fermante et je vais simplement mettre le rail comme feuille de style et le ref sera simplement la partie où vit notre feuille de style.

Eh bien, elle est à la racine de notre projet, donc je vais simplement taper styles, CSS.

D'accord.

Nous n'avons pas besoin d'aller dans des répertoires ou autre chose comme ça.

C'est juste un projet très simple.

Tout est juste ici et maintenant pour la balise de script.

Donc, la balise de script, nous devons nous assurer de la mettre en bas de notre body.

Donc, une fois que n'importe quel type, uh, je suppose des éléments que nous voulons mettre.

Donc, si nous mettons des éléments ici, nous devons mettre la balise de script après.

D'accord.

Donc, assurez-vous qu'elle est en bas de vos deux balises body.

Et je vais simplement mettre la source à nouveau comme le chemin vers le fichier app JS.

Donc, super.

Maintenant, vous verrez du code qui m'est suggéré.

Donc, comme vous pouvez le voir, cela m'est suggéré, si vous ne voyez pas cela, c'est parce que j'utilise l'extension tab nine, uh, qui me donnera des suggestions de snippets de code de nouvelle génération.

Donc, si vous ne voyez pas cela, ne vous inquiétez pas.

Il n'y a rien de mal avec votre éditeur de code.

C'est juste une, uh, extension que j'ai installée.

D'accord.

Donc, super.

Donc, nous avons lié notre feuille de style.

Nous avons lié notre fichier app JS.

La prochaine chose à faire est de commencer à ajouter des éléments dans mon fichier HTML afin de commencer à construire, vous savez, le squelette de notre jeu associé de mots, c'est un tutoriel JavaScript.

Donc, la majorité de notre travail sera en fait faite dans le fichier app JS, mais une petite partie de, um, HTML est encore un peu nécessaire.

Donc, je vais mettre un div, donnons à cela la classe de app afin que nous puissions le sélectionner plus tard dans notre CSS et le styliser.

Donc, voici notre app et que veux-je mettre dans l'app ? Eh bien, je vais avoir une zone de question.

Donc, je vais mettre diviv et donner à cela la classe de zone de question comme ceci, afin que nous puissions une fois de plus, la sélectionner dans notre fichier CSS pour la styliser.

Maintenant, ma zone de question, eh bien, une chose que je ne veux définitivement pas changer est juste, vous savez, la tête de l'app.

Cela va dire bienvenue à l'association web.

D'accord.

Et ensuite, ayons aussi une balise H trois, qui va nous montrer notre score et cela va changer.

Donc, je vais simplement mettre votre score est, et ensuite je vais utiliser un élément span.

D'accord.

L'élément span nous permettra d'interrompre cette balise H trois en ligne.

Donc, cela ne fera rien de bizarre.

Cela ressemblera toujours à faire partie, vous savez, je suppose d'une phrase, uh, et ce score où nous allons devoir l'injecter avec notre JavaScript, ce qui est pourquoi je veux sélectionner cet élément span et je vais le faire en lui donnant un ID.

Donc, l'ID que je vais lui donner est l'affichage du score, juste comme du sel.

Donc, maintenant je peux le sélectionner avec mon script de travail.

D'accord.

Donc, nous avons la zone de question.

Elle a une balise H un, elle a une balise H trois.

La prochaine chose que je veux faire est d'ajouter un diviv et je vais lui donner la classe afin que nous puissions le styliser des questions.

D'accord.

Mais je vais aussi lui donner cet ID afin que nous puissions aussi le sélectionner dans notre JavaScript.

Nous pouvons le sélectionner par classe, mais c'est juste plus propre, je pense, de le faire par IDs.

Mais encore une fois, à chacun son propre, il y a tant de façons de coder ce jeu.

C'est absolument fou.

Donc, nous lui avons donné une classe afin que nous puissions le silo.

Nous avons aussi donné cet ID afin que nous puissions le sélectionner dans notre JavaScript.

Et essentiellement ce que nous allons faire, c'est injecter.

Nous allons injecter des éléments ici en utilisant JavaScript.

Donc, j'espère que vous êtes excité pour cela.

C'est pourquoi nous le sélectionnons.

Nous allons littéralement ajouter des éléments ici, tous ici.

Super.

Donc, nous avons presque terminé avec cette page.

Maintenant, passons au fichier app JS.

Donc, la première chose que j'ai dite que nous allons faire est simplement sélectionner cet élément, n'est-ce pas ?

Eh bien, nous allons sélectionner ces deux éléments.

Peut-être commençons-nous par ce score.

Que devrions-nous enregistrer cela ? Comme je vais dire, c'est l'affichage du score.

Cela va le rendre un peu plus grand pour vous.

Nous pouvons en fait le minimiser.

Donc, affichage du score.

Je vais utiliser document.

Parce que je cherche dans le document HSL entier.

Tout cela, je vais utiliser, obtenir l'élément par ID et je vais l'obtenir par affichage du score, en m'assurant qu'il est orthographié exactement de la même manière que nous l'avons orthographié ici.

Donc, maintenant nous avons sélectionné tout cela.

D'accord.

Parce que nous allons vouloir injecter le score ici.

De même pour l'affichage de la question, parce que nous allons injecter des éléments ici.

Donc, que devrions-nous appeler cela ? Eh bien, pour la cohérence, je vais simplement l'appeler affichage de la question.

Et si j'appuie sur entrer, cela a en fait été complété automatiquement pour moi par tab nine.

Donc, nous y voilà.

Nous sélectionnons des choses.

Nous les enregistrons comme des cons afin que nous puissions les utiliser plus tard dans notre code.

Donc, super.

Donc, maintenant que nous avons cela, continuons.

La première chose que je veux vraiment faire est en fait simplement écrire quelques questions que nous allons, vous savez, afficher dans notre jeu d'association de mots.

Donc, je vais montrer comment faire cela.

Cela va être un tableau.

Donc, je vais appeler cette constante questions et faire un tableau et cela va être un tableau d'objets.

D'accord.

Donc, chaque objet va contenir, vous savez, les mots réels.

Donc, vous allez avoir trois mots et ensuite nous allons devoir choisir une réponse basée sur deux mots que le, um, mot est le plus associé avec.

Je n'ai pas très bien expliqué cela, mais j'espère que je vais vous montrer maintenant comment faire.

Et ensuite, nous allons aussi nous dire, quelle est la bonne réponse.

Par exemple, si j'ai trois mots et que ces mots vont être valeur, et ensuite le mot suivant va être estimer, et ensuite le troisième mot va être une valeur.

Attendez, donc nous avons trois mots comme les mots du quiz, et ensuite nos options à sélectionner, comme quel mot est le plus probablement, uh, associé à ces trois mots.

Eh bien, le premier que je vais mettre est jury, ce qui n'a pas vraiment de sens, n'est-ce pas ? Jury n'est pas associé à ces trois mots, cependant, évaluer est correct.

Donc, le spectateur va voir ces trois mots et ensuite avoir l'option de ces deux pour choisir celui qui est le plus associé à ces trois.

Et ensuite, je vais aussi mettre la bonne réponse est l'option deux parmi celles-ci, nous pourrions aller par l'index zéro ou un.

C'est à vous.

Je ne vais pas le faire purement parce que, uh, je fais cette vidéo, sur ma chaîne personnelle en utilisant une API.

Et cette API utilise en fait ce format.

Donc, n'utilisant pas les index, mais simplement en disant que l'option un n'est pas correcte, mais que l'option deux est correcte.

Donc, c'est pourquoi je l'ai fait de cette manière.

Encore une fois, c'est à vous de choisir comment vous souhaitez le faire.

Donc, voici notre première question.

Allons-y et créons-en d'autres.

Donc, pour l'instant, je vais simplement en faire quelques-unes, bien sûr, vous pouvez en avoir autant que vous le souhaitez, comme je l'ai dit, je fais ce tutoriel sur ma propre chaîne en utilisant une API qui obtient en fait des charges et des charges de questions.

Il y en a une énorme quantité.

Donc, si vous voulez vérifier cela, veuillez utiliser le lien dans ma description ci-dessous afin de, uh, essentiellement obtenir le lien pour ce tutoriel.

D'accord.

Donc, ceux-ci sont simplement codés en dur pour nous comme je l'ai mentionné.

D'accord.

Donc, je vais simplement coller trois autres que j'ai préparés plus tôt.

Donc, nous y voilà.

D'accord.

Ceux-là, je viens de les coller, veuillez faire une pause ici si nécessaire, ou le code sera également disponible dans la description ci-dessous.

Donc, ce sont mes cinq questions avec les bonnes réponses.

D'accord.

Donc, où maintenant vous allez utiliser ce tableau afin de créer de nouveaux éléments en utilisant des boucles.

D'accord.

Cela signifie que si vous voulez ajouter plus de questions, alors vous savez, chaque élément sera facilement créé pour nous et ainsi de suite.

Donc, la première chose que je vais faire est, eh bien, en fait, commençons par le score.

Donc, le score va changer, c'est pourquoi j'ai utilisé let, et maintenant ce n'est pas assez bien de dire que le score est zéro.

Nous allons devoir l'ajouter dans notre HTML et nous allons le faire.

Parce que nous avons déjà sélectionné cet affichage de score.

Donc, je peux utiliser ce contexte et je vais utiliser le contenu texte et je vais simplement utiliser cette variable de score.

D'accord.

Donc, c'est tout ce que j'ai fait et maintenant en m'assurant que c'est juste un égal.

Et maintenant si je regarde cela, je vais simplement l'ouvrir dans WebStorm.

Je peux en fait simplement utiliser ce bouton ici et je vais l'ouvrir dans mon navigateur.

D'accord.

Donc, vous verrez que le score a été ajouté TA merveilleux.

Uh, pour ceux d'entre vous qui n'utilisent pas WebStorm, vous pouvez simplement copier le chemin.

Donc, vous copiez le chemin ici et ensuite vous le collez dans votre navigateur.

Donc, je vais simplement le faire, uh, pour vous.

Je vais obtenir le chemin absolu et ensuite le coller ici.

Comme, donc c'est la même chose.

Super.

J'allais le minimiser à nouveau.

Donc, merveilleux.

Donc, nous affichons le score.

La prochaine chose que nous allons faire est d'écrire une fonction pour remplir la question.

Donc, tout comme nous avons obtenu l'affichage du score ici, nous allons maintenant obtenir l'affichage de la question et le remplir avec des questions.

Donc, je vais faire tout cela dans une fonction autonome.

Cependant, donc la fonction va s'appeler Pope questions.

D'accord.

C'est juste ce que j'ai choisi de l'appeler.

Maintenant, nous allons en fait utiliser quatre chacun.

Donc, essentiellement une boucle afin de créer un tas de DS qui vont être notre question.

Les boîtes vont contenir toutes les questions ensemble.

Donc, en fonction du nombre d'éléments que j'ai dans ce tableau, donc je vais obtenir ce tableau.

Donc, je vais obtenir le tableau.

Je vais utiliser quatre chacun et pour chaque élément de mon tableau.

Maintenant, nous savons qu'il y a cinq éléments, je vais choisir de les appeler.

Chacun d'eux une question.

Donc, pour chaque élément, que je me suis choisi de core question, ce que je veux faire est essentiellement créer un élément.

Je veux créer un diff, d'accord.

Et sauvegardons cela comme question box afin que nous puissions l'utiliser dans un JavaScript const question box.

Maintenant, je vais en fait ajouter une liste de classes afin que nous puissions le faire avec class list add, et je vais ajouter la classe de question box au div que nous venons de créer.

D'accord.

Donc, c'est ainsi que vous le feriez.

Vous utiliseriez cette méthode afin d'ajouter la classe question box.

Donc, le div que nous venons de créer, bien sûr, nous ne pourrons pas voir quoi que ce soit pour l'instant.

Nous n'avons stylisé aucun divs et nous n'avons pas encore mis ce div dans le HTML.

Donc, je vais vous montrer comment faire cela ensuite.

Donc, pour l'instant, que pouvons-nous faire ? Peut-être commençons-nous par la question box juste pour que nous puissions voir les choses visuellement d'abord.

Donc, je vais simplement peut-être agrandir cela et prendre la question box, comme ceci, et faire un peu de style.

Donc, mes question boxes pour le moment, je vais simplement leur donner une couleur de fond.

Uh, je vais simplement utiliser une couleur RGB pour cela, comme ceci, et donner à chacune une marge de 15 pixels.

D'accord.

Donc, c'est tout ce que je vais faire juste pour que nous puissions commencer à voir certaines choses.

Donc, nous avons créé un div, nous avons ajouté la classe de question box à celui-ci, ce qui est essentiellement juste le rendre noir ou la marge.

La prochaine chose que nous allons faire est de mettre la question box dans notre question display afin que nous puissions le faire, prenons la question, display display, et je vais utiliser une pen pour mettre la question box.

D'accord.

Et ensuite je vais simplement appeler la fonction.

Donc, je vais simplement l'appeler pour que cela fonctionne.

Et maintenant si je rafraîchis cela, vous verrez, il y a cinq question boxes ici.

Nous devons mettre quelque chose dedans afin de voir qu'ils sont noirs.

Donc, tout ce que je vais faire est de revenir ici et pour l'instant, juste pour que vous puissiez voir que cela fonctionne, je vais simplement mettre box.

D'accord.

Donc, juste mettre la chaîne de box.

Donc, nous y voilà.

Box, box, box, peut-être, peut-être faisons, vous savez, donner à ce texte, faisons-le blanc, juste pour que nous puissions voir ce qui se passe fat.

Je vais simplement le rendre légèrement blanc cassé.

Donc, RGB 2 30, 2 30, 2 30.

Super.

Donc, incroyable.

Nous bouclons afin de créer des question boxes pour chacune de nos questions, continuons.

Donc, j'espère que cela a du sens, car nous allons utiliser cette logique beaucoup dans ce tutoriel.

Nous allons simplement répéter cela afin de créer plus d'éléments.

D'accord, super.

Pendant que nous sommes ici, je vais en fait simplement prendre l'app elle-même.

Donc, le diviv de la classe de app, juste pour m'assurer que tout est centré et je vais en fait appliquer la famille de polices de Trabu sounds à celle-ci également.

Donc, donc tra butcher, Ms.

Désolé.

Uh, et puis quelques sauvegardes, deux.

Donc, peut-être que nous avons Lucinda Grande pour Donna.

Sûr.

Ceux-là.

Donc, pour centrer, tout je vais utiliser display flex.

Donc, c'est flex box.

D'accord.

Vous devez utiliser display flex afin de faire ces prochaines lignes.

Sinon, elles ne seront pas appliquées.

Donc, justify content vient avec flex box et ensuite text align ne vient pas en fait avec flex box.

Donc, text align center, c'est juste le centre ou le texte, et je vais lui donner un padding de cent pixels.

Donc, l'app va avoir un PA de cent pixels fixes.

Super.

Et maintenant les question boxes vivent dans le diviv questions.

D'accord.

Donc, nous les insérons ici.

Donc, je vais simplement styliser un peu ce diviv aussi.

Je veux juste m'assurer que je vais utiliser flex box à nouveau, d'ailleurs, j'utilise display flex.

Et je veux juste m'assurer qu'ils s'enroulent.

D'accord.

Donc, si vous changez la taille de votre écran, ils s'enroulent les uns sur les autres et vous le faites avec flex wrap wrap, et je vais aussi les centrer.

Donc, justify content center.

Merveilleux.

Et je vais juste commencer la question box un peu plus.

Um, faisons, donnons-leur un border radius.

Je suis un grand fan du border radius.

Pour ne pas rendre les choses trop dures.

Je pense que c'est toujours comme une chose assez agréable à faire.

Je pense que trois est bien.

Peut-être allons-nous pour 10 pixels.

Je vais aussi donner un padding, mais le padding ne sera pas égal.

Je vais lui donner un padding zéro depuis le haut 40 pixels, uh, à droite 10 pixels en bas et 40 pixels à gauche.

D'accord.

Donc, c'est ce que j'ai fait.

Super.

Donc, c'est notre question box qui a l'air bien.

Et si nous regardons ici, cela ressemble juste plus à cela maintenant.

D'accord.

Donc, chaque question box est prête à avoir nos questions qui y sont réellement mises ainsi que, vous savez, quelques boutons, uh, et ainsi de suite.

Donc, continuons.

Donc, au lieu d'avoir ceci qui dit simplement box, nous allons en fait utiliser quatre chacun pour montrer chacun des trois mots de quiz depuis le tableau.

D'accord.

Donc, nous allons faire cela ensuite.

Donc, encore une fois, cela va être un quatre chacun, nous allons entrer dans le tableau des questions, nous allons ensuite entrer dans le tableau et trouver la clé quiz.

Et ensuite nous allons utiliser quatre chacun et pour chacun de ceux-ci, que devrions-nous appeler cela ? Je suppose que c'est un indice, n'est-ce pas ? Nous pouvons l'appeler un indice pour chaque indice.

Donc, indice, nous allons essentiellement créer une balise PTAG, donc document create element et l'élément que nous voulons créer est un PAG.

D'accord.

Donc, c'est tout ce que je vais faire.

Et sauvegardons cela comme constante tip text.

D'accord.

Encore une fois, vous pouvez l'appeler comme vous le souhaitez.

Donc, nous avons créé une balise P.

La prochaine chose que nous allons faire est d'ajouter une, uh, nous n'allons pas ajouter une classe de lèvres.

Nous allons obtenir le tip text, et nous allons utiliser text content.

Vous pouvez utiliser inner HTML, c'est ce que vous voulez faire.

Et ensuite nous allons simplement assigner le tip lui-même.

D'accord.

Donc, nous allons simplement assigner fast et ensuite quick et ensuite prompt.

D'accord.

Et enfin, bien sûr, nous devons le mettre dans quelque chose, mais nous voulons le mettre dans la question box cette fois-ci.

D'accord.

La question box que nous avons mise dans le question display, mais dans le, d'accord.

Donc, revenons ici.

La question box.

Cette chose regarde ici.

Donc, je vais dans, voici notre HTML.

Et ensuite nous prenons cela, c'est le question display.

Et nous injectons ces question boxes.

Maintenant, dans chaque question box, nous voulons aussi injecter les tips.

D'accord.

Donc, nous allons faire cela.

Donc, cette fois-ci, je vais prendre la question box que nous avons créée ici et je vais utiliser une pen tip text.

D'accord.

Donc, maintenant si nous regardons ici, donc encore une fois, voyons, nous ajoutons des éléments, nous les ajoutons en utilisant JavaScript.

Donc, maintenant chaque question box a des balises P avec des tips.

Super.

D'accord.

Donc, j'espère que cela se solidifie un peu plus, plus nous le faisons, continuons.

Je veux aussi mettre un logo.

Donc, faisons cela au-dessus d'ici.

Donc, avant que ceux-ci ne soient injectés dans la question box, car ces Juifs s'empilent lorsque vous injectez des choses.

Donc, vous devez vous assurer que l'ordre dans lequel, uh, vous voulez mettre les choses doit aller de haut en bas.

Donc, appelons cela logo.

Um, oui, appelons cela all logo display.

Sûr.

Et je vais créer un élément, en fait, faisons une balise H one parce que notre logo sera en fait un symbole.

D'accord.

De l'internet.

<rires> bien sûr, vous n'avez pas à le faire, vous pouvez faire une image ou autre chose, mais ce que je vais faire, allez logo display.

Donc, je vais prendre ce logo display, et je vais utiliser text content, et je vais utiliser ce, uh, parce que c'est un jeu d'association de mots.

Je vais utiliser ce symbole de stylo ici.

D'accord.

Donc, c'est tout ce que j'ai fait.

C'est juste un symbole de texte.

Donc, nous l'avons ajouté.

Et bien sûr, encore une fois, nous devons le mettre dans la question box.

Nous allons prendre notre question box et nous allons ajouter.

Vous pouvez ajouter un enfant, ajouter permet en fait d'ajouter plusieurs choses, uh, où l'enfant permet simplement d'ajouter un, je crois.

Et la chose que nous allons ajouter est le logo display après lui avoir ajouté du texte.

Donc, super.

Donc, encore une fois, si je rafraîchis cela, voici notre logo.

Cool.

Bien sûr, nous pouvons aussi le styliser si nous le souhaitons, une manière simple de le faire sans donner à ceci un nom de classe, en fait, afin que nous, vous savez, nous ne voulons pas trop, trop de surcharge, c'est que je peux en fait aller dans la question box et toute balise H one qui y vit aura ce style.

Donc, je vais simplement le faire aller à gauche en allant une ligne de texte à gauche, et peut-être changer sa couleur en deux.

Donc, je vais aller RGB 1 77, 1 3 6 2 1 1.

D'accord.

Mais bien sûr, si vous mettez des balises H one dans la question box, cela aura le même style.

Donc, gardez cela à l'esprit.

Mais sinon, cela ressemble à ceci.

Super.

Donc, nous avons nos tips.

La prochaine chose que nous allons faire est nos deux boutons qui nous montreront les deux, uh, réponses potentielles que nous pourrions avoir.

Donc, faisons cela ensuite.

Donc, nous venons d'ajouter les tips ici et nous mettons la question box dans les question displays, mais avant de le faire, nous devons faire plus de choses.

Donc, la prochaine chose que je veux faire est en fait créer un diviv qui stockera nos deux boutons afin que nous puissions les garder ensemble.

Donc, je vais utiliser document, create element, et nous allons créer un div D comme ceci, et stockons cela comme question buttons.

Est-ce que cela va contenir nos question buttons ? Uh, et cette fois, je vais en fait ajouter une liste de classes à cela.

Donc, question buttons, class list, add question buttons.

Merci.

Tab nine.

Et bien sûr, nous devons aussi l'ajouter.

Donc, cette fois, je vais simplement prendre la question box à nouveau et ajouter question buttons.

D'accord.

Donc, nous avons mis le div qui a la classe de question buttons dans la question box.

La prochaine chose que nous devons faire est d'ajouter quelques boutons réels dans les questions, buttons cette fois-ci.

Donc, je veux faire cela.

Nous sommes toujours dans la boucle.

Donc, si vous pouvez voir ici pour chaque question avec make sure vous êtes toujours entre ces accolades, car nous bouclons sur chacun de ceux-ci.

D'accord.

1, 2, 3, 4, 5, et dans la boucle, je veux obtenir les options.

D'accord.

Donc, nous avons appelé chaque élément dans la boucle question, ce qui signifie que je vais obtenir la question quiz et pour chaque élément quiz, que voulons-nous appeler cela pour chaque fast pour chaque option ? Appelons-le.

Eh bien, que veux-je faire ? Je veux créer un bouton.

Donc, utilisons document, create element button.

Je vais sauvegarder cela comme la constante question button.

D'accord.

Donc, singulier cette fois.

Donc, nous créons essentiellement deux boutons comme nous avons deux éléments dans le tableau quiz.

Et maintenant, je vais simplement lui donner une liste de classes.

Donc, question button, class list.

Add question button singulier.

D'accord.

Eh bien, bien sûr, nous n'avons pas encore écrit cette classe et je vais aussi lui donner un contenu texte, afin que nous puissions voir ce qui se passe.

Question button, text, content, et cela va être l'option.

D'accord.

Et bien sûr, n'oublions pas que nous devons en fait l'ajouter dans les question buttons.

Donc, je vais le mettre ici.

Question buttons, append the question button singulier.

D'accord.

Donc, cela va boucler une fois.

Cela va mettre le premier, cela va boucler une deuxième fois.

Cela va mettre le deuxième après que nous ayons, bien sûr, assigné la liste de classes et assigné l'option réelle elle-même.

Donc, jetons un coup d'œil ici et oh, nous avons choisi la mauvaise chose.

Je veux dire, c'est bien.

N'est-ce pas ? Nous sommes en train de comprendre cela.

Ce n'est pas questions, quiz.

C'est question.

C'est options.

Donc, chacune des questions, options, donc TA nous le faisons.

Nous avons nos deux options.

Cela a l'air bien.

Faisons une pause avec un peu de JavaScript et détendons nos cerveaux avec un peu de style.

Donc, choisissons en fait les question buttons et question button pour les styliser.

Donc, je vais simplement utiliser la classe des question buttons et je veux m'assurer que tout ici.

Donc, les deux boutons que nous avons créés vont être côte à côte.

Donc, je vais utiliser display flex.

Et pour être sûr, je vais lui donner une direction de flex non pas colonne mais ligne.

Et maintenant pour chaque question button individuel, je vais donner à chacun une marge de cinq pixels,

Un peu de padding, 10 pixels depuis le haut et le bas et 20 depuis la gauche et la droite, je vais lui donner un border radius, qui sera de 20 pixels.

Assurez-vous de l'orthographier correctement.

Je vais dire border nuns.

Nous nous débarrassons du style générique, uh, du bouton et ensuite la couleur de fond.

Je vais simplement opter pour RGB 75 1 3 4 1 1 1.

D'accord.

Et le texte sera simplement blanc, mais je voudrais le rendre RGB.

Donc, peut-être juste un peu de blanc cassé RGB, 2 5, 5, 2 5, 5, 2, 5, 5.

Super.

Cependant, si nous obtenons aussi le, uh, question button et si nous ajoutons disabled à celui-ci, c'est pour plus tard.

Je veux en fait que la couleur de fond soit comme un gris foncé RGB, 8, 9 1 8 9 1 8 9.

Quelque chose comme ça.

Peut-être même un peu plus foncé.

D'accord.

Bien sûr, cela ne s'est pas encore produit.

Mais lorsque nous désactivons les boutons, uh, parce que nous allons le faire, c'est juste ce que je veux faire.

Et aussi le texte, je veux qu'il ait l'air un peu comme ce gris aussi.

Donc, il semble que nous ne pouvons pas cliquer dessus.

Super.

Donc, maintenant que nous avons cela, ajoutons en fait un écouteur d'événements à nos boutons afin qu'il gère la vérification des résultats.

Donc, nous allons faire cela ici.

Donc, encore une fois, nous allons prendre le question button.

Donc, le question button que nous venons de créer et utiliser ad event listener pour écouter les clics.

Et si un clic est fait, nous voulons vérifier la réponse.

Donc, c'est une fonction de rappel que nous n'avons pas encore écrite.

D'accord.

En fait, juste pour l'instant, je vais simplement faire cela ici.

Je vais écrire function, check, answer, et je vais simplement console log checked juste pour que nous puissions voir que cela fonctionne.

D'accord.

Mais encore une fois, attendez cette page, obtenez le console log et si je clique sur n'importe quel bouton, il dira checked, voir, checked, checked, checked, check, check, check, checked.

Donc, nous savons que cela a été accroché.

L'écouteur d'événements fonctionne.

Continuons.

Maintenant.

Nous ne voulons pas que le console log dise simplement quelque chose, n'est-ce pas ? Que voulons-nous qu'il se passe ? Eh bien, réfléchissons-y.

Je veux en fait vérifier si la réponse est correcte.

Et nous avons déjà ces données stockées dans un tableau.

Et si c'est correct, je voulais dire correct en dessous.

Ou si c'est faux, je voulais dire faux.

Et je veux aussi désactiver le bouton car nous avons cliqué dessus.

Nous ne pouvons pas cliquer dessus à nouveau.

Et si c'est correct, je veux ajouter un score et si c'est faux, je veux moins de score.

D'accord.

Donc, à la fin, vous avez un score final.

C'est basé sur le nombre de réponses fausses et correctes que vous avez.

Cool.

Donc, faisons-le.

Donc, pour faire cela, je vais en fait devoir passer certaines choses à travers, dans ma fonction check answer.

Donc, je vais passer certaines choses à travers.

Donc, je l'ai ouvert, non par parenthèse, mais uhoh cela signifie que j'appelle la fonction.

Ce n'est plus une fonction de rappel.

Donc, nous devons faire cela pour en faire une fonction de rappel à nouveau, et les choses que nous allons devoir passer à travers sont, eh bien, réfléchissons à cela.

Je veux en fait passer à travers, eh bien, je veux passer à travers le, je veux définitivement passer à travers l'option.

Donc, par ce moyen, je veux passer à travers ceci.

Je vais passer à travers ceci et ensuite je vais aussi passer à travers lequel index.

C'est parce que nous savons que par exemple, ceci est la bonne réponse, n'est-ce pas ? Cela dit deux.

Donc, nous allons passer à travers les questions, la bonne réponse.

Aussi, je vais passer à travers l'option sur laquelle nous avons cliqué et ensuite sa valeur d'index.

D'accord.

Où elle se trouve dans ce tableau.

Donc, faisons cela maintenant.

Donc, nous allons devoir donner à cela un index.

Donc, je vais choisir de l'appeler option index.

Donc, par exemple, je vais simplement vous montrer ce que je veux dire par cela.

Je vais passer à travers l'option et ensuite je vais aussi console log l'option index.

D'accord.

Et si je vais ici, cliquez sur l'option un, deux cliquez.

Donc, l'option sur laquelle nous avons cliqué est évaluer l'option est en train de passer à travers l'option.

L'index est de ne pas trouver pourquoi est-ce ? Revenons ici en passant à travers l'option index.

Ah, mais nous ne le passons pas à travers dans la fonction check answers.

Donc, maintenant cliquez sur celui-ci.

Super.

L'option est évaluée et l'option index est un parce que cela dit option index zéro.

D'accord.

Donc, chacun d'eux, cela serait 0 1 0 1.

Vous pouvez vérifier.

C'est ce que cela devrait être.

Donc, nous voulons un moyen de dire que, vous savez, le correct an nous passons aussi à travers la bonne réponse.

Donc, allons-y et faisons cela.

Nous avons besoin des questions, de la bonne réponse.

Donc, nous savons que cela va être un ou un deux, n'est-ce pas ? Donc, changeons l'option index.

Ajoutons plus un à celui-ci.

Donc, au lieu de traiter avec les index, nous allons littéralement, c'est soit l'option un ou deux.

Donc, cela correspond à la manière dont nous comptons la bonne réponse ici.

Donc, c'est un ou deux.

Donc, nous devons simplement savoir que si cela est égal à cela, alors c'est correct.

D'accord.

Donc, je vais passer cela à travers.

Je vais le nommer.

Quelque chose d'autre ici.

Parce que tant que c'est dans le bon ordre, c'est uh, nous n'avons pas à l'appeler de la même manière.

En fait, il sera probablement moins confus si nous l'appelons simplement la bonne réponse.

D'accord ? D'accord.

Donc, cela signifie que si je vais simplement le déplacer vers le haut, si l'option index est égale à la bonne réponse, cela n'a pas vraiment besoin d'être strict.

Alors nous savons que c'est bien correct.

Remettons cela ici car cela me crie dessus.

Donc, nous allons simplement ajouter un au score, n'est-ce pas ? Et bien sûr, nous devons afficher le score.

Donc, score, display, text content score, parce que sinon nous ajoutons au score, mais nous ne mettons pas à jour notre navigateur pour montrer le nouveau score.

Donc, cette ligne est importante.

D'accord.

Donc, c'est tout ce que je fais, sinon.

Si ce n'est pas le cas, nous allons soustraire un du score.

Et encore une fois, nous devons montrer ce nouveau score, n'est-ce pas ? Parce que ce n'est pas assez bien de simplement mettre à jour le score et ici nous devons en fait montrer cela dans le navigateur deux.

Super.

Donc, vérifions cela.

Donc, si je clique sur évaluer cool, j'obtiens un au score parce que c'est correct.

Et si je clique sur bijoux, eh bien, moins a été ajouté parce que nous savons que c'est faux.

Donc, cela fonctionne, cela a l'air bien.

Cependant, regardez, nous pouvons tricher, n'est-ce pas ? Et aussi, ce serait bien de désactiver le bouton si nous avons déjà cliqué dessus.

Donc, travaillons sur la désactivation des boutons maintenant pour faire cela, nous allons en fait devoir collecter les éléments que nous avons déjà cliqués.

Donc, je vais faire un tableau.

Allons-y et peut-être faisons cela ici.

Donc, laissez cliqué.

Donc, nous voulons peut-être, vous savez, changer cela pourrait être con laissez simplement cela comme let pour l'instant juste parce que je ne suis pas exactement sûr de ce que je veux faire avec cela encore.

Donc, voici notre tableau et si nous cliquons sur quelque chose, eh bien, peu importe si c'est correct ou faux, je vais simplement le mettre dans le tableau.

Donc, voici mon tableau.

Je vais pousser l'option dedans.

Donc, cela signifie en fait que je vais simplement console log out le tableau cliqué pour nous ici.

Donc, peu importe si c'est correct ou faux, nous collectons simplement des choses dans notre tableau cliqué, n'est-ce pas.

Nous les collectons afin que nous sachions que cela est cliqué et nous allons désactiver les boutons.

Grâce à cela.

Donc, super.

Se débarrasser de cela.

Donc, cela signifie que, en fait, peut-être laissons passer le question button ici aussi dans la fonction check answer.

Donc, le bouton lui-même, parce que nous pouvons le faire.

Vous pouvez faire presque n'importe quoi.

Et maintenant nous allons obtenir le question button et disabled, uh, n'est pas vrai.

Nous allons en fait regarder dans le tableau cliqué.

Et si le tableau cliqué inclut l'option, alors nous savons.

Donc, l'option sur laquelle nous avons cliqué, alors nous savons que le bouton doit être désactivé.

Donc, essayons cela.

Cliquez.

Oh, il est désactivé.

Cliquez désactivé.

Oui.

Cela a l'air génial.

À quel point c'est cool, c'est incroyable.

Donc, super.

Maintenant, une dernière chose, ce serait bien d'avoir, vous savez, comme un affichage correct ou incorrect sous ici.

D'accord.

Donc, que nous sachions immédiatement si nous avons raison ou tort.

Donc, je vais vous montrer comment faire cela maintenant, en fait, d'accord.

Nous allons créer, <affirmatif> créer.

Donc, en bas, une fois que nous avons mis tout, je vais en fait créer, mettre un autre diviv qui va montrer notre réponse.

Donc, je vais le faire ici.

Donc, je vais utiliser document, create element.

Je vais créer un div cette fois et je vais l'appeler, answer display,

Et nous allons obtenir l'answer display.

Et je vais lui donner la liste de classes, class list, add de answer display, que nous allons démarrer plus tard.

Et bien sûr, nous devons mettre cela dans notre question box.

Donc, question box, append, answer display.

Et maintenant, stylisons-le un peu.

Peut-être devrions-nous simplement, nous pouvons le faire.

Donc, je vais obtenir dans mon fichier CSS.

Prenons notre answer display.

Et je vais en fait coder en dur une hauteur pour cela.

Donc, peu importe si elle est vide ou non, elle aura simplement la même hauteur et je vais simplement centrer tout ici.

Donc, encore une fois, je vais utiliser flex box display, flex align items, center justify content center.

Donc, nous y voilà.

D'accord.

Donc, nous avons notre answer display et maintenant je vais simplement le rendre plus petit à nouveau.

Je vais en fait écrire une autre fonction.

Donc, voici notre fonction check answers.

Nous allons obtenir function, get results, ou peut-être add results car c'est ce que nous faisons techniquement.

Ajout de la réponse dans l'answer display.

Donc, fonction add result.

Eh bien, que voulons-nous faire ? Eh bien, cette fois, je vais en fait,

En fonction de la question box dans laquelle nous nous trouvons.

Donc, quand voulons-nous appeler cette fonction ? Je suppose que nous voulons l'appeler après ici.

D'accord ? Nous voulons le faire ici ou si nous le faisons en fonction de.

Donc, si nous sommes, si c'est la bonne réponse, nous allons ajouter le score et nous pouvons passer à travers la question box réelle.

D'accord ? Parce que nous voulons l'ajouter à la question <affirmatif> box.

Oui.

Donc, prenons le, tout ce que nous pourrions faire.

Answer display.

Oui.

Laissez passer à travers l'answer display aussi dans check answer.

Et nous allons dire que nous allons ajouter les résultats à l'answer display et que le résultat va être correct.

D'accord.

Ce qui signifie que, encore une fois, nous pouvons simplement utiliser la même fonction pour passer à travers différentes variables pour changer le résultat.

Donc, faisons dire que c'est faux.

<affirmatif>

D'accord.

Donc, cela signifie que nous savons que nous passons à travers l'answer display et nous allons aussi passer à travers la réponse réelle.

D'accord.

Donc, cela signifie que nous pouvons prendre l'answer display, uh, et ensuite nous pouvons utiliser text content.

En fait, nous voulons probablement effacer tout ce qui s'y trouve, n'est-ce pas ? Parce que sinon nous allons simplement en ajouter plus.

Nous allons ajouter correct, faux, correct, faux.

Selon celui sur lequel nous cliquons.

Parce que cela continuera à s'ajouter.

Donc, nous voulons effacer tout ce qui s'y trouve.

Et ensuite nous voulons obtenir l'answer display, text, content, et choisir de mettre la réponse que nous passons à travers.

D'accord.

Comme le deuxième paramètre.

D'accord.

Donc, nous allons, nous allons soit passer votre correct ou faux selon que nous sommes ici ou si nous sommes ici.

D'accord.

Donc, c'est tout ce que je vais faire.

Et je sens que cela devrait être cela parce que nous mettons déjà le want to display dans la question box ici, mais vérifions cela.

Donc, jury voyons answer display.

Non, il semble que nous ne mettons pas cela ici.

Answer display, answer display, juste pour voir ce que nous cliquons.

Donc, si nous cliquons sur ici, answer display adjacent,

Ah, parce que nous ajoutons l'answer display ici parce qu'il doit être après les options.

Nous ne pouvons pas évidemment l'ajouter ici.

C'est de ma faute.

Donc, ce que je vais faire à la place est de passer à travers la question box.

Nous venons de créer inter check answer, parce que nous pouvons passer cela à travers.

Et ensuite cela signifie que nous passons cela à travers inter check.

Donc, prenons cela et passons à travers la question box, ce qui signifie que sur l'ad results, nous allons passer à travers la question box, passer à travers la question box.

C'est une question box et cela signifie que nous allons obtenir la question box et obtenir le, uh, Bo ou nous pouvons utiliser query selector, en fait query selector pour trouver le div avec le nom de classe answer display.

Donc, avant, si vous remarquez, uh, disant en regardant dans le document entier, vous pouvez en fait juste regarder dans un, uh, élément.

Donc, c'est ce que j'ai fait ici.

Et sauvegardons cela comme answer display.

Donc, nous ne voulons pas de document à nouveau.

Nous voulons regarder dans la question box.

D'accord, cool.

En fait, nous n'avons peut-être pas besoin de cela car cela le remplace.

Donc, débarrassons-nous de cela

Et <affirmatif> et super.

Donc, cela a l'air bien.

Une dernière chose que je veux faire dans cela est simplement changer la couleur de cela en fonction de si c'est correct ou faux.

Mais c'est super, super simple.

Tout ce que je vais faire est bien sûr obtenir l'answer display.

Uh, je vais simplement supprimer toute liste de classes qui pourrait exister.

Donc, si wrong existe, je veux le supprimer car sinon il ajoutera simplement, vous savez, cela pourrait causer quelques problèmes bizarres.

Donc, supprimez s'il y a une classe wrong ou une classe correct, supprimez les deux et je vais obtenir l'answer display et utiliser class list add, et je vais simplement ajouter, eh bien, en fait, nous pouvons simplement le passer à travers ici pour nous faciliter la vie.

Donc, le nom de classe que je veux ajouter est correct.

Et si c'est faux, le nom de classe que je veux ajouter est wrong.

Donc, je vais passer à travers class name et simplement utiliser cela pour ajouter un nom de classe.

Et il y a aussi des moyens de course nous devons le faire ici afin que nous puissions nous assurer qu'il est juste sur l'answer display si je fais.

Correct.

Donc, nous y voilà.

Cela signifie qu'il est sur le même div.

La classe est sur n'importe quoi avec la classe answer display

Et la couleur du texte va être RGB 2 0 1 2 0 1 1 1 7.

Et ensuite je vais aussi faire answer display wrong et wrong va être 2 1 1 1 3 4 1 1 7.

D'accord, donc super.

Nous avons maintenant terminé notre jeu.

D'accord.

C'est assez infaillible car nous désactivons les boutons.

Donc, vous ne pouvez pas tricher.

Je ne pense pas, uh, mais faites-moi savoir ce que vous pensez de ce jeu.

D'accord.

Donc, merveilleux.

Nous venons de terminer notre jeu en pur JavaScript vanilla.

Si vous êtes intéressé à aller plus loin et que vous aimez apprendre à utiliser les APIs afin d'obtenir des questions aléatoires et s'il vous plaît, vérifiez la vidéo.

Comme je l'ai dit dans la description ci-dessous pour cela sur ma propre chaîne.

D'accord.

Donc, je vais commencer sur WebStorm, qui est mon IDE de choix est l'éditeur de code que je vais utiliser aujourd'hui.

Et je vais simplement cliquer sur nouveau projet ici et appelons cela jeopardy.

Donc, jeopardy,

Vanilla JS, comme ceci, et je vais simplement cliquer sur créer.

Donc, vous verrez qu'un répertoire a été créé pour moi.

Bien sûr, il n'y a rien dans ce répertoire pour l'instant, nous allons devoir ajouter quelques fichiers.

Donc, je vais simplement aller de l'avant et ajouter un nouveau fichier.

Il y aura un fichier HTML.

Je vais simplement l'appeler index et sélectionner qu'il s'agit d'un fichier HTML.

Maintenant, si vous n'utilisez pas WebStorm, vous devrez mettre l'extension afin que votre éditeur de code sache traiter cela comme un fichier HTML, mais nous utilisons WebStorm.

Donc, je vais simplement faire comme cela.

Super.

Et maintenant, appelons notre projet quelque chose.

C'est ce qui sera affiché dans le navigateur.

Donc, je vais simplement aller de l'avant et appeler cela jeopardy.

Et maintenant, créons quelques fichiers supplémentaires car nous allons devoir trier notre style quelque part.

Donc, je vais simplement entrer ici, créer un nouveau fichier, cette fois-ci, ce sera une feuille de style.

C'est un fichier CSS.

Je vais appeler cela styles et sélectionner qu'il s'agit d'un fichier CSS.

Donc, nous y voilà.

Et vous pouvez voir que l'extension a été ajoutée.

Merveilleux.

Et un fichier de plus.

Celui-ci contiendra notre JavaScript et je vais simplement l'appeler app.

Et comme vous le verrez, l'extension JS a été ajoutée à notre éditeur de code qui sait qui traiter cela comme un fichier JavaScript.

Super.

D'accord.

Maintenant, je vais simplement agrandir cela.

Nous devons lier les deux fichiers que nous avons créés au fichier CMR.

Donc, nous allons le faire grâce à la balise de lien, comme ceci, et la référence à cela est simplement le chemin vers mon fichier de style CSS, qui est à la racine de mon projet.

Donc, je n'ai pas besoin de m'inquiéter d'aller dans des répertoires ou autre chose et cela ressemble simplement à cela.

Et ensuite, nous devons aussi lier notre Java script et nous allons le faire avec une balise de script et la source de cela.

Nous allons aussi donner le chemin vers notre fichier app JS.

Donc, comme ceci.

D'accord.

En s'assurant qu'il est au-dessus de tout HTML que nous écrivons, car cela doit être chargé en premier.

Maintenant, ici, je vais simplement mettre le strict minimum de ce dont nous avons besoin et cela va être une balise H one.

Qui va dire jouons à Jeffrey.

D'accord.

Donc, comme ceci.

Et je vais maintenant faire un diff qui va contenir tout le jeu.

D'accord.

Nous allons injecter des trucs avec JavaScript ici.

Donc, nous devons bien sûr sélectionner cela et c'est pourquoi je vais donner à cela l'ID de game.

D'accord.

Et nous allons injecter des trucs avec notre JavaScript.

Nous allons injecter exactement ici entre ces deux dips, mais je vous montrerai cela plus tard.

Donc, nous avons le diviv avec l'idée de game.

La prochaine chose que je vais faire est simplement mettre une balise H deux.

Qui va montrer notre score et je vais utiliser une balise span afin que nous puissions ajouter le score dynamiquement plus tard.

D'accord.

Donc, pour le faire, je vais devoir sélectionner cela.

Je vais devoir sélectionner cela, um, dans mon JavaScript, c'est pourquoi je lui ai donné l'ID.

Et je vais simplement donner à cela l'idée de score.

D'accord.

Donc, en utilisant le span, cela va simplement interrompre cette balise H deux et cela apparaîtra simplement comme une phrase.

Super.

Donc, maintenant que nous avons fait cela dans WebStorm, je peux simplement cliquer sur ce bouton et cela ouvrira le jeu et le navigateur pour moi, ou si vous n'utilisez pas WebStorm, vous pouvez simplement l'ouvrir par vous-même.

Vous devez simplement cliquer avec le bouton droit ici, copier le chemin, vous assurer qu'il s'agit du chemin absolu et ensuite simplement le coller dans votre navigateur.

Comme ceci, donc vous allez littéralement là où se trouve votre fichier index HTML sur votre ordinateur.

D'accord.

Et l'ouvrir.

Super.

Et si j'inspecte la page, cela me permettra de faire apparaître ma console log pour continuer à coder.

Donc, continuons à coder.

Commençons à ajouter nos éléments avec JavaScript ici.

Donc, pour faire cela, je vais bien sûr sélectionner ce diviv, je vais le sélectionner en fonction de son ID.

Et je vais faire de même pour celui-ci.

Donc, l'élément span aussi.

Donc, ici, nous allons utiliser document, get element I can do by ID.

Pourquoi pas par ID game ? Et je vais sauvegarder cela comme quelque chose, que devrions-nous choisir de sauvegarder comme let's just save it as game et let's do the same for the score.

Donc, je vais l'appeler score, display document, get element by ID et l'ID était score.

Donc, maintenant nous avons essentiellement sauvegardé ces deux éléments.

Donc, le span et ce so que nous pouvons travailler avec dans notre JavaScript basé sur ces const.

D'accord, super.

Donc, avant de continuer, obtenons en fait quelques données.

Donc, bien sûr, nous créons simplement un jeu en utilisant du JavaScript vanilla.

Si vous voulez apprendre à utiliser les APIs, construire un backend et ainsi de suite.

Uh, j'ai un lien pour faire exactement ce même jeu avec une API ouverte.

Donc, nous n'aurons pas à faire de travail backend pour celui-ci en particulier, mais je vais vous montrer comment utiliser fetch et simplement faire une requête API afin d'obtenir beaucoup plus de données que nous allons coder en dur ici.

D'accord.

Donc, nous allons simplement coder en dur un tableau de genres, cinq genres qui ont trois questions chacun, chacun, donc catégorie de Jeopardy, je vais sauvegarder cela comme catégories et ce tableau va contenir essentiellement nos, uh, catégories.

Donc, le genre, le premier genre va être qui, et chaque genre aura aussi ses propres questions, qui seront un tableau d'objets.

Donc, cela va être amusant.

Il y aura beaucoup de choses intéressantes que nous allons travailler aujourd'hui, surtout pour YouTube en travaillant avec des tableaux et des objets et des données.

Donc, le prochain genre que je vais avoir est où, et je vais simplement avoir un tableau vide pour les questions aussi.

D'accord.

Et nous allons en avoir cinq.

Uh, en fait, je vais simplement vous montrer à quoi ressemble le premier objet, car les cinq auront la même forme.

Donc, les questions dans mon tableau de questions, comme je l'ai dit, il y aura trois questions.

Chaque, chacune sera symbolisée par un objet et l'objet aura cette apparence.

Il aura la question elle-même.

Donc, par exemple, nous pouvons avoir qui a écrit Harry Potter ? C'est ma question.

Et ensuite, bien sûr, nous aurons deux réponses parmi lesquelles choisir.

Donc, je sais que dans Jeopardy, vous étiez censé ombrager la réponse, mais bien sûr, c'est un jeu en ligne.

Donc, j'ai simplement choisi d'avoir deux réponses disponibles pour l'utilisateur qui joue et ensuite nous montrerons la bonne réponse.

Donc, JK rolling est une réponse, et ensuite nous allons avoir J R R Tokin comme deuxième réponse.

Et ensuite nous aurons aussi la bonne réponse, qui dans ce cas sera JK rowing, en faisant attention à l'orthographe exactement de la même manière.

Sinon, cela causera des problèmes même avec les lettres majuscules et ainsi de suite.

Cela doit être exact.

Et ensuite le niveau que nous aurons facile.

D'accord.

Donc, c'est ce que nous allons avoir.

C'est à quoi notre question va ressembler.

Nous allons en avoir trois dans chaque objet de genre.

Donc, je l'ai en fait préparé pour vous car vous ne voulez pas vraiment rester ici à me regarder taper toutes les données, je suppose.

Donc, je vais simplement le coller ici, comme ceci, donc nous y voilà.

Comme toujours, cela sera disponible dans la description ci-dessous, le code final sera disponible.

Donc, s'il vous plaît, ne vous inquiétez pas.

Donc, je vais vous parler de cela sous le genre qui nous avons un tableau de questions.

Donc, voici l'accolade d'ouverture, uh, du tableau et il y a trois questions.

Une serait de niveau facile, une de niveau moyen et une de niveau difficile.

Et ensuite nous avons le prochain objet, qui est exactement le même cette fois.

Le genre est où, mais les questions sont plus autour de où, mais encore une fois, elles ont les réponses disponibles, la bonne réponse, qui est exactement la même jusqu'aux, uh, majuscules et non majuscules.

Et ensuite le niveau.

Et ensuite nous avons quand, et ensuite nous avons quoi, et ensuite nous avons combien, d'accord, donc n'hésitez pas à faire une pause ici et à regarder ces données, encore une fois, obtenez-les dans la description.

Assurez-vous simplement d'être à l'aise avec elles avant de continuer à travailler avec ces données afin de construire notre jeu de Jeopardy.

Donc, la première chose que je veux faire est d'ajouter une catégorie, n'est-ce pas ? Donc, nous avons nos cinq catégories de Jeopardy et je vais utiliser chacune des catégories afin de créer une colonne.

La colonne va avoir le nom de la catégorie et ensuite chacune des trois questions.

D'accord.

Donc, c'est ce que je vais faire.

Il y aura beaucoup de quatre chacun et de boucles dans des boucles.

D'accord.

Cuz nous allons boucler cinq colonnes que nous allons boucler dans chaque colonne, les questions et ainsi de suite.

Donc, je vais vous montrer comment faire cela.

Maintenant, allons-y et écrivez notre première fonction.

Donc, je vais écrire fonction, add category et que voulons-nous faire ? Eh bien, en fait, prenons ce tableau.

Je vais prendre les catégories de Jeopardy, les catégories de Jeopardy.

Et pour chaque, appelons cela une catégorie.

Je vais simplement le passer à travers, dans la fonction add category.

D'accord.

Donc, essentiellement tout cela, voici notre première catégorie, n'est-ce pas ? De ici à ici, tout cela est en train d'être passé maintenant dans cette fonction add category, mais nous ne faisons rien avec pour l'instant.

Allons-y et passons-le à travers.

Maintenant, nous devons obtenir le genre de la catégorie en premier.

D'accord.

Donc, c'est ce que nous allons faire et nous allons faire un élément de titre avec.

Donc, faisons-le.

Donc, la première chose que je vais faire est en fait utiliser document, create element afin de créer un diviv et sauvegardons cela comme quelque chose, je vais appeler cela comme une colonne.

D'accord.

Nous allons créer une colonne.

Et en fait, nous allons prendre cette colonne et utiliser classless, add une classe de colonne afin que nous puissions la styliser plus tard dans notre feuille de style.

Donc, cela ressemble en fait plus à une colonne et pas seulement à un div, en fait, peut-être soyons plus précis et appelons cela genre colonne comme ceci, donc nous avons fait un div.

La première chose que j'ai dite que nous voulons mettre dans la colonne est un, comme un div pour un titre.

Donc, je vais simplement utiliser document, create element diviv à nouveau, merci.

Tab nine.

Et appelons cela genre title et cette fois genre title, donnons-lui class list, add genre title.

Donc, nous pouvons à nouveau, le styliser.

Et je vais simplement utiliser inner text pour lui donner le nom du genre.

Donc, comme je l'ai dit, nous entrons ici et obtenons le genre.

D'accord.

Donc, nous obtenons la chaîne de qui et ensuite quoi et pourquoi et ainsi de suite.

Donc, les cinq catégories.

Donc, c'est tout ce que je fais, même si pour l'instant, vous ne verrez rien dans le navigateur, n'est-ce pas ? Parce que nous, nous avons créé des éléments.

Nous leur avons donné des noms de classe, nous avons mis du texte à l'intérieur.

D'accord, nous avons tout fait cela, mais nous n'avons pas encore remis cela dans notre HDML.

Nous ne l'avons pas fait, n'est-ce pas, nous devons le faire maintenant.

Donc, c'est pourquoi j'ai sélectionné le jeu.

Donc, c'est pourquoi j'ai sélectionné cela.

Car je veux mettre mes cinq premières colonnes que je crée ici.

Donc, je vais le faire comme, donc je vais boucler sur.

Donc, dès que je fais une colonne, je vais prendre le jeu.

Je vais utiliser une pen pour mettre la colonne que nous venons de faire.

Donc, cela va boucler chaque fois que nous avons cela.

Donc, nous allons cinq fois, nous allons ajouter une colonne et cela ajoutera une autre colonne.

Cinq fois, cela le fera.

Mais notre colonne doit aussi avoir tout cela dedans.

N'est-ce pas ? Donc, je vais prendre la colonne avant de la remettre dans le jeu de colonnes et je vais ajouter le genre de titre dedans.

Donc, maintenant si nous regardons dans le navigateur, da, da et je vais simplement vous montrer à quoi cela ressemble en HTML maintenant.

Donc, c'est ce que nous avons fait avant.

Souvenez-vous que c'est là que nous avons écrit dans notre HTML, mais grâce à JavaScript, j'ai mis cinq DS qui ont la classe de genre colonne et chacun a un autre diviv avec une classe genre titre et le genre lui-même.

Donc, nous l'avons fait.

D'accord.

Nous avons fait notre premier pour chaque afin de créer des éléments en utilisant JavaScript, faisons une pause ici, laissons cela s'imprégner car nous allons faire cela à nouveau.

Comme je l'ai dit pour ajouter chacune des trois questions dans chaque colonne, uh, et d'abord, prenons en fait une pause mentale avec un peu de style, car le style est vraiment agréable.

C'est vraiment facile.

Et je vais permettre à nos cerveaux de peut-être, vous savez, ralentir un peu avant de faire un autre quatre chacun.

Donc

Tout d'abord, je vais simplement commencer le corps en me débarrassant de toute marge et de tout padding, juste pour m'assurer qu'il est, vous savez, étalé, uh, partout et je vais lui donner une couleur de fond, RGB, cela le rend RGB.

C'est un peu, eh bien, je vais vous montrer.

Eh bien, six, c'est un peu comme un gris foncé que je vais utiliser.

Et la police que je veux utiliser ici est aussi toute la police ou le texte, désolé, va être blanc, juste pour qu'il se démarque.

La prochaine chose que je veux faire est en fait utiliser flex box afin de m'assurer que tout est affiché au centre.

Donc, en initialisant flex box, je peux maintenant utiliser cette commande, qui est justify content pour centrer.

Je ne pourrai pas l'utiliser sans display flex.

Donc, assurez-vous que display flex est là et align items center aussi.

C'est quelque chose que je vais utiliser ainsi que flex direction, flex direction column pour m'assurer qu'il est empilé les uns sur les autres.

D'accord.

Et super.

Je vais aussi en fait importer une famille de polices qui est en dehors de ce que nous avons.

Donc, si vous allez sur font ou SIM, donc si vous allez sur Google fonts,

La police que je veux choisir s'appelle Anton.

Donc, je vais simplement la rechercher.

Uh, je l'ai déjà utilisée ici.

Je ne veux en fait aucune de celles-ci, donc allons-y et supprimons Oswald, supprimons tout

Anton.

Donc, c'est celle que je veux.

Donc, s'il vous plaît, allez-y et cliquez dessus et sélectionnez simplement ce type.

Il n'y a qu'un seul style et vous pouvez choisir de le faire dans votre H share mile ou CSS.

Je vais choisir de le mettre dans mon fichier CSS.

Je vais simplement copier cela.

Et en haut de ce fichier, je vais l'importer comme ceci en tant qu'URL.

Et cela signifie simplement que je peux maintenant l'utiliser à côté de cela.

Donc, super.

Donc, je peux maintenant utiliser la famille de polices, Anton avec Sans comme sauvegarde.

Merveilleux.

Donc, c'est mon corps.

Cela signifie simplement que j'ai un peu stylisé tout pour que cela ressemble un peu plus à ceci.

La prochaine chose que je veux en fait styliser est le, uh, jeu.

Donc, sélectionnons ce div par l'ID de jeu.

Donc, cela signifie que je dois aller chercher l'ID de jeu, comme ceci, et je vais simplement dire que tout ici aura la couleur de fond de RGB, comme cette sorte de, uh, couleur grisâtre plus foncée.

D'accord.

Donc, c'est tout ce que je vais faire pour l'instant.

Il y avait une autre chose que je voulais faire, c'est juste m'assurer que toutes ces colonnes sont en fait empilées les unes à côté des autres.

Donc, je vais aussi utiliser display flex pour faire cela.

Et c'est à quoi cela devrait ressembler pour l'instant.

Bien sûr, nous allons changer tout cela un peu plus tard, donc quelle est la prochaine chose que nous allons faire ? Eh bien, allons-y et incitons les cartes.

En fait, pendant que nous sommes ici, ajoutons simplement ce style pour une carte afin que nous puissions voir les choses un peu plus joliment lorsqu'elles se produisent, la largeur d'une carte que je vais coder en dur est de 160 pixels.

La hauteur que je vais coder en dur est de 120 pixels.

Uh, la couleur de fond.

Je vais simplement la faire être ce bleu de Jeopardy, qui est RGB 26, 26, 2 55.

Maintenant, je vais la faire paraître biseautée.

Donc, border left, je vais dire solid RGB.

Uh, et ensuite ce sera comme cette sorte de couleur bleue plus claire que j'ai choisie plus tôt, et elle aura une épaisseur de 10 pixels.

Et je ne sais pas s'il y a un moyen abrégé de faire cela, mais je suis paresseux.

Donc, je vais simplement le faire à gauche.

À droite ? Et ensuite nous avons le haut et le bas, et ensuite je vais simplement changer un peu les couleurs.

Donc, je vais faire cela comme un bleu foncé.

Je vais faire cela comme une autre teinte de bleu juste pour la faire paraître biseautée.

Et ensuite encore, même chose ici.

Donc, la réponse est super.

Uh, je vais simplement m'assurer que tout le texte est centré aussi, et la taille de la police que je vais utiliser pour les cartes.

Cela va être une taille de cent pixels.

D'accord.

Cela va être vraiment grand.

Donnons-lui une marge de cinq pixels.

Donc, chaque carte va avoir une marge de cinq pixels et un peu de padding.

Et je vais aussi donner à la ligne.

Je vais changer la hauteur de ligne, uh, de la police.

D'accord.

Donc, c'est tout ce que j'ai fait.

Donc, nous avons créé une classe de carte.

Maintenant, allons-y et créons quelques cartes.

Donc, nous avons ajouté la colonne à l'intérieur du jeu.

La prochaine chose que nous devons faire est en fait travailler avec les questions.

Donc, pour l'instant, nous sommes toujours dans cet objet, n'est-ce pas ? Nous avons sélectionné le genre.

La prochaine chose que je veux faire est de sélectionner ce tableau de questions et nous allons utiliser quatre chacun à nouveau pour boucler sur chaque élément de ce tableau.

Donc, j'espère que cela a du sens en fonction de ce que nous avons fait précédemment.

Donc, comme nous sommes actuellement pour chaque, donc nous sommes dans la boucle pour chaque, grâce à cela.

Prenons une catégorie et tout ce que je vais faire est de prendre les questions de cette catégorie cette fois-ci.

Donc, le tableau et pour chaque élément ou chaque question, désolé, appelons cela une question.

Que voulons-nous qu'il se passe ? Eh bien, comme je l'ai dit, je veux faire une carte.

Donc, document create element div, et je vais simplement appeler cela littéralement carte, comme, donc, et cette fois, je vais utiliser classless, add, uh, cartes, car c'est la, la classe que nous venons de créer ici.

Donc, c'est ce que je veux appliquer à ce div.

Et bien sûr, nous devons le mettre dans la colonne.

Donc, prenons la colonne et utilisons append et je vais mettre la carte.

D'accord, super.

Vous pouvez utiliser un append child.

Append permet d'ajouter plusieurs choses, mais vous pouvez utiliser append child si vous voulez, si vous voulez simplement ajouter une chose, ce que je suppose techniquement nous faisons ici, donc super.

C'est ce que nous faisons en ce moment.

Nous ne verrons pas grand-chose car ce n'est qu'un div vide.

Cependant, nous pouvons mettre du texte ici.

Uh, en fait, peut-être faisons-le par le niveau.

Donc, nous bouclons sur chaque élément du tableau des questions, n'est-ce pas ? Donc, je veux obtenir le niveau de chaque question et si c'est facile.

Donc, ici après avoir mis la carte, si le niveau de la question est égal à facile, eh bien, je veux obtenir la carte et dans un HTML ou dans un texte, vous pouvez faire ce que vous voulez vraiment dans un H dans un texte, c'est la même chose.

Peut-être gardons tout cohérent.

Donc, je sais que nous l'avons fait quelque part ici dans un HTML.

Nous allons simplement coder en dur 100 car c'est le nombre de points que vous obtenez pour répondre à une question facile et faisons de même pour les autres.

Donc, si c'est moyen, je veux mettre dans le inner HTML 200 et si c'est difficile, je vais nous donner 300 points.

D'accord ? Donc, c'est littéralement tout ce que je fais.

Donc, maintenant si je regarde ici, da da, c'est ce que nous avons fait.

C'est notre carte.

Et c'est le inner HTML que nous avons donné à notre carte.

Cela a l'air super.

Maintenant, si vous avez regardé mon tutoriel sur la création d'un jeu d'association de mots, dans ce jeu, nous avons en fait, vous savez, des fonctions et nous avons passé beaucoup de choses à travers elles afin de travailler avec des écouteurs d'événements.

Donc, nous passons beaucoup de, um, informations dans des fonctions.

Cette fois, je vais vous montrer une autre façon de faire cela.

Vous pouvez en fait définir des attributs aux éléments afin que vous puissiez ajouter plus de données à ceux-ci que vous pouvez sélectionner plus tard et vous pouvez le faire en utilisant la méthode set attribute.

Donc, c'est ce que je vais vous montrer aujourd'hui.

D'accord, je vais mettre cela en place car nous allons avoir besoin de voir exactement ce que j'ajoute à chaque div pour l'instant.

Chacun de ces divs a simplement la classe carte et le inner HTML de 100, 200 ou 300, je vais ajouter beaucoup plus d'informations à ceux-ci avec l'aide de set attribute.

Bien sûr, cela signifie que quelqu'un pourrait, vous savez, inspecter la page et tricher à Jeopardy, mais vous savez, c'est juste pour le plaisir.

Donc, mais oui, soyez simplement conscient de cela.

Donc, je veux essentiellement ajouter toutes les informations sur ma question à ce div afin que lorsque je le retourne.

Nous avons toujours accès à ces informations.

Donc, comme je l'ai dit, nous allons utiliser set attribute pour faire cela.

Donc, je vais prendre la carte.

Donc, littéralement la carte que nous avons créée, à laquelle nous avons ajouté les classes, et ensuite nous l'avons mise dans la colonne et ensuite nous avons ajouté un HTML à côté.

Nous allons utiliser set attribute afin d'ajouter une data question, qui va être simplement la question de la question, n'est-ce pas ? Parce que nous bouclons sur

Ce tableau de questions, que nous avons appelé question, c'est une question, c'est pourquoi j'ai dit question, question.

Je veux dire, malheureusement, vous savez, cela s'est simplement passé ainsi que nous devons utiliser question, question ensuite.

Nous allons avoir question.

Correct.

Et nous allons entrer dans l'objet question et obtenir le niveau ainsi que la première réponse et la deuxième réponse.

Donc, c'est ce que nous avons fait ici.

Et en fait, si je vous montre à quoi cela ressemble, si je le rafraîchis, vous verrez maintenant que chaque div non seulement a la classe de carte, non seulement a le contenu NEX de cent, il a aussi maintenant data question et la question réelle, combien de joueurs dans une équipe de football, combien de secondes dans une heure et combien de personnes en Chine.

Donc, ces informations sont toutes attachées à ce div que nous ne pouvons pas voir visuellement, mais elles existent.

Donc, je vais faire de même.

Donc, card set, attribute pour les autres choses que j'ai dites.

Donc, nous avons la data question, obtenons la data, correct.

Qui va être question correct.

Et ensuite aussi les réponses, n'est-ce pas ? Donc, set, attribute data.

Uh, faisons answer one et allons question answers et ensuite entrons dans le premier, obtenons le premier élément de ce tableau.

Donc, celui-ci, et ensuite obtenons le deuxième aussi.

Tim va copier <affirmatif> je vais simplement copier cette ligne.

Obtenez le deuxième élément en utilisant la valeur d'index de un pour entrer dans cela, obtenez le deuxième élément du tableau.

Parce que comme nous le savons, les tableaux utilisent des index.

Maintenant, je vais faire une dernière chose et vous pourriez penser comme, oh, quoi, mais nous avons utilisé toutes les informations que nous pouvons ici.

Quoi, quoi d'autre voulez-vous faire ? D'accord.

Eh bien, je veux en fait obtenir cette valeur et aussi la définir sur le di afin que lorsque nous retournons la carte, nous sachions toujours la valeur de la carte et je peux le faire avec une fonction afin que je puisse obtenir la carte et utiliser, get inner HTML et l'appeler.

Donc, appeler la méthode afin d'obtenir le inner HTML de ce diviv, qui dans ce cas est cent, le cas est deux cents et ce cas est

trois cents.

Donc, c'est assez génial si je puis me permettre.

Donc, maintenant si je rafraîchis cela et que nous regardons n'importe lequel de ceux-ci, vous verrez la data question, data, answer one data, answer corrects et la data value.

Pourquoi la data answer two n'est-elle pas ajoutée, ah, c'est parce que data est écrasée.

Donc, TA nous avons toutes ces informations ainsi que la data value maintenant à notre disposition.

Super.

Donc, maintenant, commençons à retourner ces cartes.

Donc, je vais le faire en ajoutant un écouteur d'événements à notre carte.

Donc, card add event listener et au clic de la carte.

Je veux simplement retourner la carte.

Donc, c'est une fonction de rappel.

Nous devons écrire cette fonction et si nous cliquons sur n'importe quelle carte, cela sera capturé.

D'accord.

Mais seulement si nous cliquons sur la carte, donc allons-y et faisons cela maintenant.

Donc, nous avons terminé avec cette fonction.

C'est une longue.

Donc, la fonction ad category est maintenant terminée.

La prochaine fonction que nous allons écrire est la fonction.

Donc, fonction flip cut card.

Donc, que voulons-nous qu'il se passe lorsque nous retournons la carte ? Eh bien, nous voulons simplement qu'elle ait l'air de retourner la carte, n'est-ce pas ? Donc, en fait, je veux simplement me débarrasser du style du div.

Donc, je veux me débarrasser du style et simplement faire en sorte qu'elle ait l'air de retourner la carte en ajoutant peut-être quelques animations et ensuite, vous savez, avoir, uh, la question, apparaître avec les deux options des réponses.

Donc, faisons-le.

Donc, je vais prendre cette carte.

Donc, cet élément sur lequel j'ai cliqué, je vais prendre son HTML et je vais littéralement mettre une chaîne vide.

D'accord.

Donc, c'est un peu comme une manière de tricher pour le vider.

Maintenant, la prochaine chose que je veux faire est de créer un, uh, diviv que j'ai appelé text display afin que nous puissions afficher le texte de la question et ensuite le styliser un peu.

Donc, je vais utiliser, create element et je vais créer un div pour faire cela.

D'accord.

Donc, maintenant que nous avons créé le diviv, encore une fois, je vais prendre text display et je vais utiliser class list, add pour ajouter une liste de classes que nous n'avons pas encore écrite.

Nous pouvons utiliser text display, ou peut-être choisissons card text, comme

Donc, donc nous mettons le text display.

C'est bien.

La prochaine chose que je veux faire est d'ajouter deux boutons.

Donc, encore une fois, je vais utiliser document create element, et cette fois je vais créer un élément button.

Et une fois que nous avons créé ce bouton, je vais simplement l'appeler fast button, car je ne suis pas très imaginatif, mais nous avons en fait besoin de deux boutons.

Donc, premier bouton et deuxième bouton, encore une fois, en utilisant la méthode create element pour créer un élément button.

Donc, une fois que nous avons ceux-ci, eh bien, bien sûr, nous allons devoir ajouter, uh, des classes à eux.

Donc, merci beaucoup, mais ce premier bouton va avoir la classe first button et ensuite le deuxième va avoir la classe.

Vous l'avez deviné, second button.

Donc, comme ceci, donc nous avons ajouté les classes et maintenant nous devons simplement ajouter du texte à ceux-ci, n'est-ce pas ? Donc, je vais aller first button in a HTML et nous allons obtenir cela, ce que nous avons cliqué, cet attribut, allons voir à nouveau.

Qu'est-ce qui est à notre disposition, obtenir l'attribut, la vue data, answer one, answer one.

Et bien sûr, pour le deuxième, nous obtiendrons data, answer two pour le deuxième bouton.

Donc, nous avons créé les boutons.

Nous avons ajouté des classes aux boutons.

Nous avons également défini le inner HTML des boutons pour avoir soit une réponse soit une autre.

Et bien sûr, nous devons mettre ces boutons dans ce que nous cliquons.

Donc, nous allons utiliser ce mot-clé, je vais faire un pen et je vais en fait mettre le text display

Et ensuite le first button et ensuite le second button.

D'accord, super.

Donc, cela a l'air bien.

Nous devons bien sûr aussi obtenir le, uh, nous devons ajouter un HTML.

Nous devons en fait ajouter le, uh, la question elle-même.

Donc, nous allons utiliser get attribute pour obtenir la data question, en faisant attention à l'orthographe exactement de la même manière que nous l'avons sauvegardée.

Donc, data question comme ceci super.

Donc, cela devrait maintenant avoir l'air bien.

Testons cela.

Donc, ou quelque chose ne va pas, l'événement.

Listener n'est pas une fonction.

D'accord.

Card.

Notre add event listener devrait être une majuscule L ici.

D'accord.

Donc, si vous cliquez sur un maintenant, donc cela disparaît et nous obtenons la question et nous obtenons deux boutons.

Bien sûr, nous devons faire un peu de style car cela n'a pas l'air bien.

Donc, une chose que je peux en fait faire est de changer.

Nous allons probablement devoir changer la taille de la police ici afin que nous puissions le faire en utilisant le style de la police.

Uh, ce style de police et changeons-le pour qu'il soit de 15 pixels.

Donc, encore une fois, nous utilisons simplement JavaScript pour faire cela et nous allons aussi changer la hauteur de la ligne d'ici.

La hauteur de la ligne va être de 30 pixels.

Donc, maintenant si nous cliquons sur l'un de ceux-ci, incroyable, <affirmatif> incroyable.

Donc, cela a l'air beaucoup mieux.

Il y a bien sûr encore quelques choses que nous devons faire.

Une chose que nous devons faire est en fait, um, ajouter un on click à ces boutons pour le gérer comme la bonne réponse ou non.

Et aussi, je veux désactiver le clic sur l'un de ceux-ci.

Si nous répondons actuellement à une question, n'est-ce pas, nous ne voulons pas tricher, pas de tricherie autorisée.

Et aussi, je veux ajouter un au score.

Si la bonne réponse est cliquée.

Donc, je vais vous montrer comment faire tout cela d'abord, cependant, passons à styliser quelques choses.

La première chose que je vais styliser est les boutons.

Donc, faisons cela maintenant.

Je vais simplement faire de la place et super.

Donc, le premier bouton,

Je vais simplement lui donner une couleur de fond RGB, 2, 4, 1 7 1 2, 4.

Nous allons le faire ressembler à du rétro.

Et ensuite, bien sûr, le deuxième bouton a aussi besoin d'avoir un style.

Donc, un, choisissons 1 90, 57 37.

Donc, nous venons d'ajouter deux couleurs aux boutons.

Nous pouvons, gardons ce style rétro.

Car je suis un peu étrangement dedans.

Vous n'avez pas à le faire, bien sûr, vous pouvez choisir de vous en débarrasser si vous le souhaitez.

D'accord.

Pendant que nous sommes ici, stylisons aussi le genre de titre.

Donc, la classe de ceci était genre de titre.

Si je m'en souviens bien, je vais lui donner une couleur de fond du même bleu que nous avions.

Donc, RGB 2 6, 2 6, 2, 5, 5, comme ceci, uh, alignons le texte au centre.

Oups, texte

Ligne centre.

Faisons la taille de la police.

Je vais la mettre à 28 pixels et donnons-lui un padding de cinq pixels.

D'accord.

Et aussi une marge de cinq pixels.

Donc, cela ressemble un peu plus à ceci, juste comme le jeu.

Super.

D'accord.

Donc, nous avons fait cela.

La prochaine chose que je veux faire est de gérer le clic.

Donc, faisons cela.

Donc, maintenant, que voulez-vous faire, savez-vous, en fait, avant de passer à l'ajout des écouteurs d'événements pour les deux boutons, je vais en fait dire que si nous retournons la carte, je veux encore une fois, chaque carte, chaque carte et supprimer l'écouteur d'événements.

Donc, je vais utiliser en utilisant document query, select all et regarder tout ce qui a la classe de carte.

Donc, ce seront toutes, toutes ces cartes, d'accord.

Toutes celles-ci.

Et je vais supprimer l'écouteur d'événements pour elles, mais seulement sur ce flip.

Donc, toutes les cartes, je vais sauvegarder cela comme, et je pense que nous devons en faire un tableau.

Je vais faire un tableau à partir de ces excuses.

Si ce n'est pas le cas, assurez-vous que cette requête est sélectionnée.

Uh, et ensuite nous allons obtenir toutes les cartes et pour chaque

Carte, je vais simplement obtenir chaque carte et supprimer l'écouteur d'événements.

Et je vais supprimer le clic et je vais supprimer le flip card afin que maintenant si une carte est retournée, nous ne pouvons pas cliquer sur aucune d'entre elles.

Le flip est désactivé.

C'est cool.

D'accord.

Et je ne veux l'activer à nouveau que si nous choisissons une réponse.

Donc, maintenant, gérons les clics des boutons.

Donc, je vais écrire une autre fonction.

Cette fonction va s'appeler, uh, appelons-la, get result.

D'accord.

Donc, comme, donc nous déplaçons tout cela.

Oups.

Déplaçons simplement tout cela un peu.

Donc, que veux-je qu'il se passe ? Eh bien, je veux, si je clique sur le bouton, n'est-ce pas ? Donc, ajoutons un écouteur d'événements au premier bouton.

First button, add event listener.

Si je clique dessus, alors je veux obtenir des résultats juste comme ils appellent la fonction de rappel.

D'accord.

Et ensuite, faisons de même pour le deuxième bouton aussi.

Donc, ils vont tous les deux essentiellement appeler cette fonction si nous cliquons dessus et si nous cliquons dessus, je veux obtenir cela ou ce que.

J'ai cliqué, n'importe quel bouton sur lequel j'ai cliqué.

Je veux obtenir comme parent et comme parent comme la carte.

Donc, si nous avons un coup d'œil ici, le bouton vit dans le div avec une classe de cartes, je veux obtenir le parent de celui-ci.

D'accord.

Je veux obtenir le parent.

Donc, cet élément parent.

Donc, je vais simplement vous montrer la console log.

Uh, disons que c'est quelque chose de constant de la carte du bouton pour être vraiment précis.

Cuz c'est ce que nous obtenons.

Nous obtenons la carte à laquelle le bouton appartient.

Et ensuite avons-nous d'autres console logs ici ? Je sens que nous en avons.

Vous n'en avez pas.

D'accord.

Donc, voici notre console log.

Donc, si je clique sur cela, cliquez sur un bouton, il me montrera son parent, qui est cette carte qui appartient à, et vous verrez toutes ces données dont nous avons besoin pour travailler.

D'accord.

Donc, c'est assez cool.

C'est continuer.

Donc, pour obtenir le résultat, eh bien, ce que je vais faire, c'est dire si la carte du bouton et ensuite je vais utiliser get attribute pour obtenir l'attribut de, eh bien, je suppose que nous voulons obtenir la data correct answer.

D'accord ? Nous voulons obtenir la data.

Correct.

Qui est 11.

Donc, nous savons que c'est la bonne réponse et nous voulons nous assurer qu'elle est la même que le inner HTML du bouton.

Donc, si cela est égal à ce inner HTML, alors nous savons que c'est une bonne réponse.

D'accord.

Donc, nous allons obtenir ce score et nous allons essentiellement ajouter le score en obtenant à nouveau, um, la data value du bouton, c'est pourquoi nous sauvegardons la data value.

Donc, nous y voilà.

Donc, je vais, encore une fois, aller à la carte du bouton, obtenir l'attribut, data value.

Cependant, c'est une agitation de droits.

Nous devons passer cela à travers passer inch pour nous assurer que c'est un type de nombre et ensuite nous allons l'ajouter au score.

Donc, score plus la valeur et nous allons l'assigner à la variable score.

D'accord.

Donc, sommes-nous en train de sauvegarder le score quelque part ici ? Je ne crois pas que nous le soyons.

Donc, je vais mettre let score égal à zéro pour commencer.

D'accord.

Donc, c'est ce que nous faisons.

Si c'est, si la réponse est correcte, nous allons ajouter quelque chose au score.

Nous allons ensuite montrer le score dans le navigateur.

Car nous ne le faisons pas encore.

Donc, prenez simplement la variable de score après avoir ajouté la data value à celle-ci et ensuite montrez-la ici.

La prochaine chose que je vais faire est en fait, uh, prendre la carte du bouton et je vais aussi class list.

Add je vais ajouter une classe correct answer afin que nous puissions changer cela symboliser.

C'est correct.

Allons-y comme un orange ou quelque chose et ensuite, uh, en fait, enlevons tout dans la carte elle-même.

Nous allons enlever la question.

Nous allons enlever ces deux boutons et nous allons simplement montrer la valeur que nous voulons si c'est correct.

Donc, pour faire cela, je vais laisser un peu de temps, afin que ce ne soit pas si abrupt.

D'accord.

Donc, je vais utiliser un set time out pour faire cela et ensuite nous allons utiliser une boucle while pour essentiellement enlever les enfants.

Nous allons enlever le dernier enfant et ensuite le dernier enfant, jusqu'à ce qu'il n'y ait plus d'enfants dans le div parent.

Donc, tant que le premier enfant de la carte du bouton existe, cela va continuer à le faire jusqu'à ce qu'il n'y ait plus de premier enfant.

D'accord ? Donc, tant que cela est vrai, nous allons obtenir l'enfant de la carte du bouton, enlever l'enfant de la carte du bouton, le dernier enfant.

Donc, nous allons essentiellement, si cela a du sens, nous allons continuer à boucler et nous débarrasser du dernier enfant, nous débarrasser du dernier enfant, nous débarrasser du dernier enfant jusqu'à ce que le dernier enfant soit le premier enfant, nous débarrasser de cela.

Et ensuite il n'y aura plus de dernier enfant et cela va, um, finir de fonctionner.

D'accord.

Donc, nous allons faire cela.

Nous allons déplacer tout ce qui s'y trouve.

Uh, et nous allons faire cela après cent millisecondes et ensuite nous allons simplement prendre la carte du bouton.

Et ensuite le ntml comme nous l'avons dit, nous allons simplement en faire la valeur.

Donc, obtenir l'attribut data value.

Nous allons simplement montrer combien de points nous voulons.

Donc, cela se passe.

Tout cela est ce qui se passe si vous savez que la réponse est correcte, sinon.

Nous allons dire mauvaise réponse.

Donc, je vais essentiellement simplement prendre cette ligne, mais cette fois mauvaise réponse.

Donc, ce sera comme une couleur rougeâtre.

Peut-être que je n'ai pas encore décidé.

Et cette fois, nous allons faire set time out.

Uh, et ensuite nous allons en fait toujours tout enlever.

Mais cette fois, nous allons simplement ajouter un zéro, car nous voulons zéro point.

Nous pouvons le faire comme un nombre si vous voulez.

C'est entièrement à vous et nous allons faire cela à nouveau après des millisecondes.

D'accord, super.

Et ensuite, nous allons ajouter en arrière.

Eh bien, en fait, nous devons ajouter en arrière tous les écouteurs d'événements aux cartes, mais aussi nous allons supprimer l'écouteur d'événements pour cette carte spécifique car nous avons terminé avec elle.

Supprimer l'écouteur d'événements, cliquer sur flip card.

Nous avons terminé avec cette carte.

Nous avons nos points, plus de tricherie.

Et cela signifie que, en fait, um, peut-être faisons-le ici.

Donc, encore une fois, document queries, obtenez toutes les cartes à nouveau.

Donc, tout ce qui a le nom de classe de carte et je vais sauvegarder cela comme toutes les cartes, faire un tableau à partir de cela à nouveau, je ne suis pas vraiment sûr si je dois faire cela, mais je le fais maintenant.

Je me suis engagé.

Uh, et ensuite toutes les cartes pour chaque carte.

Je vais, eh bien, simplement ajouter en arrière le, supprimer l'écouteur d'événements.

D'accord, super.

Et ensuite, juste un style final pour ajouter la bonne réponse et la mauvaise réponse.

Donc, bonne réponse.

C'est une bonne réponse.

Je veux que la couleur de fond change pour RGB 1 8 6 1 8 6 24.

Et si c'est une mauvaise réponse, alors je veux que la couleur de fond soit RGB 2, 2, 1 6 4, 5, 6.

Super.

Donc, maintenant, partageons l'art.

Donc, celui-ci, quand est Noël ? Je sais que c'est ici.

Yay.

C'est correct.

Donc, nous voyons la valeur.

Nous obtenons cent du score et le fond est devenu jaune.

Maintenant, celui-ci, quelle est la capitale de l'Arabie Saoudite ? Je vais dire Jed.

C'est la mauvaise réponse d'ailleurs, mais je devrais obtenir un zéro rouge et zéro est ajouté.

Donc, cela a l'air merveilleux.

Et bien sûr, je ne peux pas cliquer sur autre chose jusqu'à ce que je réponde à cette question et ensuite je peux cliquer sur une autre question.

Donc, même lorsque cela est ici, je ne peux pas cliquer sur autre chose Superman.

Merveilleux.

Donc, cela a l'air fantastique.

Nous avons maintenant terminé notre jeu de Jeopardy, donc j'espère que vous avez apprécié ce tutoriel.

J'ai vraiment apprécié le faire pour vous.

Je veux dire, je pense que nous avons fait un très bon travail.

C'est un peu infaillible.

Bien sûr, si vous, uh, rencontrez des bugs, alors faites-le moi savoir, mais je suis assez content de cela.

Et bien sûr, n'hésitez pas à le styliser.

Cependant, vous le souhaitez, cette partie vous appartient entièrement.

Merci encore pour avoir regardé et j'espère vous revoir bientôt.