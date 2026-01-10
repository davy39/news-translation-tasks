---
title: Tutoriel HTML / CSS - Construire un Site Web de Recettes
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-09-28T18:56:03.000Z'
originalURL: https://freecodecamp.org/news/html-css-tutorial-build-a-recipe-website
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/maxresdefault-2.jpeg
tags:
- name: HTML
  slug: html
- name: youtube
  slug: youtube
seo_title: Tutoriel HTML / CSS - Construire un Site Web de Recettes
seo_desc: 'Building projects is a great way to build your skills, especially when
  it comes to web development.

  We just published an HTML & CSS course on the freeCodeCamp.org YouTube channel that
  will teach you how to build a recipe website.

  John Smilga develope...'
---

Construire des projets est une excellente façon de développer vos compétences, surtout en matière de développement web.

Nous venons de publier un cours HTML & CSS sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à construire un site web de recettes.

John Smilga a développé ce cours. Il est l'un des contributeurs les plus prolifiques de la chaîne YouTube freeCodeCamp et a créé une série de cours populaires.

Le projet que vous allez construire est un site web multi-pages créé uniquement avec HTML et CSS, sans frameworks. Les pages incluent une page d'accueil, une page à propos, une page de recettes, une page de contact, et plus encore.

Il n'y a pas de prérequis pour ce cours, mais il serait utile d'avoir des connaissances de base en HTML et CSS. Le cours inclut des fichiers de démarrage et des ressources pour vous lancer rapidement.

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=-8LTPIJBGwQ) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=-8LTPIJBGwQ]

## Transcription

(générée automatiquement)

Ce cours vous aidera à améliorer vos compétences en HTML et CSS.

L'instructeur populaire John Smith vous apprendra à créer un site web de recettes multi-pages en utilisant uniquement HTML et CSS.

Hey, quoi de neuf, c'est John de Coding Addict, et bienvenue dans un autre projet HTML et CSS.

Dans cette vidéo, nous allons construire un site de recettes de nourriture multi-pages.

Si vous voulez voir l'ensemble du projet en action, il suffit de naviguer vers l'URL HTML, CSS simplement recettes dotnet pour cette application, encore une fois, l'URL est HTML, CSS simplement recettes dotnet vous le trouverez.

Et effectivement, nous avons un site de recettes avec un tas de pages.

Nous avons donc une page d'accueil, une page à propos, la page des tags.

Et ensuite, une fois que nous cliquons sur un tag, nous naviguerons vers une page de modèle de tag.

Nous avons également une page de recettes, ainsi que la page de contact.

Et aussi si nous cliquons sur une recette similaire, nous aurons une page de recette unique.

Avant de commencer à configurer le projet, ou l'image que je viens de mentionner, puisque c'est un projet HTML CSS, il y aura très peu de fonctionnalités.

Je copie et colle donc dans la démonstration plenish, il n'y a pas de modèles ou de composants.

Par exemple, si vous voulez afficher la barre de navigation et toutes les pages, oui, vous devrez copier et coller, puisque il n'y a pas moyen de faire autrement.

Pour suivre le projet, vous aurez besoin d'une étoile et probablement le moyen le plus rapide de l'obtenir est de naviguer vers john smith sans calme encore une fois, l'URL est john smith, calme, puis cherchez la page du projet et filtrez par YouTube.

Donc vérifiez pour vous le projet.

Et ici, si vous cliquez sur ce bouton, bien sûr, vous naviguerez vers le projet, celui que je viens de vous montrer, mais vous cherchez les étoiles.

Donc cliquez simplement sur l'étoile ou le code source, les deux mènent au même dépôt.

Et une fois que nous y sommes, cherchez simplement l'option de téléchargement zip.

Et une fois que vous avez téléchargé le zip, bien sûr, vous voulez l'ouvrir ici.

Et ensuite, je vais simplement glisser-déposer et le placer sur le bureau, j'utiliserai mon éditeur de texte préféré, Visual Studio code.

Et je préfère toujours travailler côte à côte avec une fenêtre de navigateur.

Donc ouvrez le navigateur.

Je vais les mettre côte à côte.

Et ensuite, nous passerons en revue ce que vous pouvez trouver dans le projet.

Et essentiellement, nous avons deux dossiers, nous avons un final, une étoile.

Et bien sûr, dans le final, c'est là que vous trouverez l'ensemble du code source, au cas où vous auriez besoin d'une référence.

Et l'étoile est le monde où nous faisons tout notre travail dans le magasin, vous trouverez la structure générale pour le projet.

J'ai déjà préparé quelques choses pour vous.

Comme nous avons des actifs.

C'est là que vous trouverez toutes les images, certains fichiers CSS dont je vais parler un peu plus tard, quelques pages HTML vides.

Ce sont toutes les pages que nous allons éventuellement créer, ainsi qu'un fichier JavaScript solitaire.

Et si vous regardez l'index HTML, vous trouverez ici la configuration générale, où nous avons essentiellement quelques balises de lien.

Donc l'une va être pour la favicon.

Ensuite, la suivante sera pour le CSS normalisé.

Nous avons également une pour les icônes Font Awesome, et une pour le CSS principal.

Et si vous regardez le CSS principal, vous trouverez quelques styles globaux qui sont utilisés dans tous mes projets.

Si vous êtes confus à propos de certaines de ces choses, par exemple, pourquoi utilisons-nous normalize ? Et quel est l'avantage des styles globaux, veuillez regarder ma vidéo default star où je couvre tout cela en détail.

Et vous pouvez trouver le lien de la vidéo dans la description.

Enfin, nous travaillons sur un projet HTML CSS, je préfère l'extension appelée preview on a web, qui lance un serveur web local.

Et par conséquent, une fois que j'ai sauvegardé le fichier, je peux voir les changements instantanément.

Donc laissez-moi vous montrer.

Ce sont mes extensions.

Celle que je préfère utiliser est celle-ci, nous la passons en revue sur un serveur web.

Et bien sûr, vous devez simplement l'installer.

Et si vous voulez voir dans un navigateur, vous pouvez soit cliquer dessus avec le bouton droit de la souris, et je vous montrerai cela dans une seconde.

Ou vous pouvez utiliser ce raccourci.

Une fois que vous avez installé l'extension, il suffit de naviguer vers index HTML dans l'étoile.

Donc bien sûr, c'est tout le travail.

Maintenant, si vous voulez vérifier le final, bien sûr, naviguez là-bas.

Et comme je l'ai dit, nous pouvons cliquer avec le bouton droit de la souris ici, puis choisir cette option.

Ou vous pouvez simplement opter pour le raccourci, et je crois qu'il s'agissait de Ctrl Shift L et une fois que vous l'avez divisé, vous devriez voir un pont dans le navigateur.

Et comme je l'ai dit, la raison pour laquelle je préfère utiliser cette extension est que chaque fois que vous faites quelque sorte de changements, vous verrez immédiatement cela dans le navigateur.

Donc si je vais ici avec Hello people.

Et une fois que j'ai sauvegardé le fichier, vérifiez-le.

Maintenant, bien sûr, j'ai l'élément affiché dans le navigateur.

Et ensuite, de temps en temps, je veux présenter plus, nous avons aussi sur un grand écran.

Donc par conséquent, je vais naviguer ici.

Et je vais simplement copier et coller cette URL.

Donc essentiellement, j'ai deux navigateurs, l'un va être le plus intelligent, où il verra le résultat immédiatement.

Et de temps en temps, je reviendrai au grand navigateur, juste pour montrer comment quelque chose apparaît sur un grand écran également.

D'accord, et nous allons commencer avec une navbar, qui a deux mises en page, nous avons une mise en page pour petit écran et une mise en page pour grand écran.

Et sur le petit écran, nous pouvons également basculer la longueur.

Donc laissez-moi rendre cela plus petit, l'infirmière va être une mise en page pour petit écran où, bien sûr, nous pouvons basculer.

Maintenant, j'ai probablement oublié de vous dire que lorsque j'enregistre, je zoome en fait.

C'est pourquoi tout semble si grand.

Techniquement, si je reviens à 100 %.

Maintenant, bien sûr, vous verrez que tout est plus petit.

Donc ne soyez pas surpris si à un moment donné, votre application semble un peu différente de la mienne.

Laissez-moi agrandir cela.

Je vais revenir à l'index HTML.

Encore une fois, j'utilise mon serveur web situé dans l'étoile dans l'index HTML.

Et bien sûr, comme toujours, nous devons simplement commencer par ajouter le HTML, nous allons le faire de la manière suivante, nous allons supprimer tout le code, tout le code factice.

Et je vais fermer la barre latérale juste pour que nous ayons plus d'espace.

Donc maintenant j'ai une application.

Et maintenant, c'est juste ma préférence.

Et commençons par l'élément nav également tout de suite, ajoutons une classe de navbar.

Et à l'intérieur de la barre de navigation, je veux grandir avec des couteaux sur le troisième live.

Et puis trier ce jour, nous allons avoir deux de plus.

L'un va être pour les liens de novel, et l'autre pour ni l'un ni l'autre.

Donc d'abord, configurons l'en-tête.

Et encore une fois, je vais utiliser quelques commentaires ici.

Donc disons en-tête.

Donc une année, nous placerons un logo avec un bouton de bascule, puis aussi un pour maintenant, bien sûr, c'est là que tous les liens vont être.

Maintenant, en ce qui concerne le centre de navigation, pourquoi je préfère coller dans un nombre, parce que maintenant nous sommes sur un grand écran, je peux toujours m'assurer que le contenu de la navigation ne s'étend que sur une certaine largeur et bien sûr, je vous montrerai une fois que nous commencerons à styliser le grand écran, car remarquez que la barre de navigation va en fait s'étendre sur toute la largeur, puis en ce qui concerne le contenu, le centre de la barre de navigation, celui que je vais toujours être certain de la largeur.

C'est pourquoi j'ai ce centre de navigation à l'intérieur de Napa.

Maintenant, en ce qui concerne l'en-tête, nous voulons placer deux choses ici, nous avons un lien retour vers la page d'accueil.

Donc, en gros, j'encadre mon image dans le lien.

Donc nous pouvons toujours naviguer vers la maison.

Juste pour montrer Grace, comment cela ne va pas fonctionner.

Comme si je vais à la page à propos.

C'est le look.

Mais si je veux naviguer en arrière, soit cliquer sur la maison, soit je peux simplement cliquer sur un logo, et je serai de retour à la maison.

Et puis la deuxième chose est le bouton de bascule, qui bien sûr aura cette icône Font Awesome.

Donc commençons par un lien pour le href.

Nous allons opter pour index HTML.

Et bien sûr, cela aura du sens une fois que nous aurons ajouté cette barre de navigation à différentes pages.

Parce que bien sûr, nous sommes déjà situés dans l'index HTML, lorsque nous ajouterons une classe de nav logo.

Et puis à l'intérieur de ce lien, allons-y avec IMG.

Et puis toutes les images vont être dans les actifs.

Et puis plus spécifiquement, nous avons des recettes une montre celles-ci que nous utiliserons un peu plus tard que 40.

À propos de la principale, ainsi que le logo, eh bien, ils vont simplement être situés directement dans le dossier des actifs.

Donc configurons le chemin.

Nous allons opter pour une barre oblique avant le rapport des actifs.

Et en ce qui concerne le logo un, nous cherchons simplement le logo, SVG.

Et puis ajoutons un texte alternatif sur notre site ici, simplement des recettes, serveur un, nous devrions voir le logo à l'écran.

Et bien sûr, nous le faisons.

Et après cela, configurons ce bouton.

Et ce bouton va avoir deux classes, il va avoir une classe de btn.

Donc cela provient des styles globaux ainsi que du NAB btn car nous ferons un peu plus de style.

Et aussi, vous savez, ajoutons un type.

Disons que cela va être égal au bouton couru à l'intérieur du bouton.

Comme je l'ai dit, nous allons opter pour l'icône Font Awesome.

Donc nous cherchons l'élément I.

Et bien sûr, je peux accéder à ces classes, car j'ai le lien vers la police.

Génial.

Remarquez ici, donc c'est le lien CDN pour Font Awesome.

Et puis en ce qui concerne les classes, nous cherchons FA s et puis FA et aligner, justifier.

Donc une fois que j'ai mon élément, bien sûr, je devrais voir mon icône.

Puisque je le fais bien, passons à la chose suivante.

Donc une fois que nous avons configuré l'en-tête, nous sommes ici, lorsque nous voulons ajouter un commentaire de déjeuner.

Et comme le nom le suggère déjà, dans les liens de navigation, nous aurons un tas d'éléments de lien.

Mais l'un d'eux, le dernier, le contrat un va être enveloppé dans une div, car il aura un style un peu différent, non seulement sur un grand écran, un style différent, et bien sûr, aussi sur un petit écran.

À cause de cela, bien sûr, nous l'envelopperons dans une div.

Donc créons quatre liens, nous devons nous assurer que les valeurs pour le href correspondent réellement à nos pages.

Sinon, cela n'aura pas de sens.

Et je commencerai par index HTML.

Et en ce qui concerne le texte, je vais opter pour la maison.

Mais nous voulons aussi ajouter une classe de lien de navigation, je vais en avoir une pour à propos, une pour les tags, et une pour les recettes.

Et puis assurez-vous que la valeur de l'éditeur correspond réellement aux pages que nous avons ici.

Donc laissez-moi basculer la barre latérale.

Homme, je vais copier et coller quatre fois, et apprendre en ce qui concerne les valeurs et nous allons opter pour about HTML, lorsque je cherche tags, HTML.

Et le dernier sera recipes, HTML, recipes, HTML, tous ont une classe de modélisation, donc cela reste le même.

Et maintenant, bien sûr, nous voulons simplement changer ces routeurs autour en ce qui concerne les textes.

Donc laissez-moi les sélectionner.

Lorsque je cherche home, je vais tous les supprimer.

Et nous allons opter pour about lorsque nous cherchons tags.

Et bien sûr, le dernier peu de bière recipes.

Comme déjà mentionné précédemment, en ce qui concerne contactez-nous, ce sera un lien Oui, il naviguera vers la page de contact.

Mais nous l'envelopperons dans une div avec deux classes avec nav une classe ainsi que la classe de contact.

Donc disons votre lien de navigation, un autre lien de contact.

Donc contact hyphen link.

à l'intérieur de cette div, allons-y avec un autre élément href.

Et je dirai contact HTML.

Et puis nous allons simplement ajouter une classe de bouton.

Et bien sûr, en ce qui concerne le texte, nous allons opter pour contact, et cela devrait suffire pour le HTML.

En ce qui concerne le logo que j'ai créé dans figma, qui est sans doute le logiciel de design web le plus populaire.

C'est très, très facile de commencer.

Et vous pouvez facilement trouver une série de grands tutoriels sur la façon de se lancer avec pigma sur YouTube, ainsi que sur Udemy.

Et une fois les bases en place, bien sûr, nous pouvons commencer à styliser le maillage numérique.

Et une fois que nous avons le HTML en place.

Maintenant, bien sûr, commençons à styliser.

D'abord, nous nous inquiéterons de la mise en page pour petit écran.

Donc d'abord, je veux configurer celui-ci.

Ne vous inquiétez pas de l'effet de bascule.

Et seulement alors je vais configurer le grand écran où nous allons le faire en naviguant vers main CSS, encore une fois, il est situé dans le dossier CSS, et plus spécifiquement, main CSS.

Et puis nous avons le commentaire navbar.

Donc ce sont tous les styles globaux et puis juste après le commentaire navbar, nous allons commencer à styliser.

Et commençons simplement par nav center.

Et éventuellement, il y aura aussi quelques styles pour le nombre.

Mais pour le moment, cela ne va probablement pas avoir de sens.

Donc je vais simplement ajouter un sélecteur pour l'ensemble de la navbar.

D'abord, nous allons commencer par notre centre, et puis vous verrez quels styles nous voulons ajouter à la barre de navigation également.

Donc commençons par ici et je veux simplement opter pour une sorte de largeur.

Puisque je veux configurer cette largeur fluide, ce qui signifie que je veux la définir en fonction de la taille de l'écran, je vais opter pour la largeur, et 90 vue largeur.

Donc ce sont des unités.

Et essentiellement, cela signifie simplement 90% de la largeur de l'écran, quelle que soit sa taille, très petite ou très grande.

Et puis en ce qui concerne la largeur maximale, nous allons passer par ici.

Et puis rappelez-vous, j'ai mentionné que j'allais utiliser une variable CSS pour cela.

Et dans mes styles globaux, j'ai la largeur maximale définie à 11 120 pixels.

Donc c'est la largeur que je vais utiliser.

Laissez-moi revenir ici, je vais simplement dire demi-heure ami, et puis largeur maximale.

Et ce que cela signifie, c'est que notre contenu numérique ne sera jamais plus grand que 1112.

C'est pourquoi nous avons une App Center.

C'est pourquoi nous avons ajouté Bien sûr, la largeur maximale.

Maintenant, vous remarquerez que pour l'instant, bien sûr, le centre nerveux est tout à fait du côté gauche.

Pourquoi ? Eh bien, parce que nous avons la barre de largeur, nous n'avons pas configuré la marge, ou nous n'avons pas stylisé le conteneur parent.

Donc nous avons deux choix, soit vous allez ici avec une marge zéro et auto.

Donc cela va aussi toujours le placer au centre.

Ou nous allons travailler avec un conteneur parent.

Et dans ce cas, nous allons simplement dire display flex, et puis justify content.

Nous allons le mettre au centre.

Et enfin, nous allons opter pour des éléments de ligne et je vais le définir égal au centre, mais je peux vous dire tout de suite que nous ne pourrons pas voir cela.

Pourquoi ? Eh bien, parce que maintenant la barre n'a aucune hauteur.

Donc une fois que nous aurons ajouté la hauteur et cela va être sur un grand écran, alors nous verrons effectivement cette propriété en action.

Si vous avez un doute, je vous suggère fortement d'ajouter simplement l'arrière-plan.

Donc dans ce cas, disons que vous êtes confus, ce qui se passe avec le centre de la carte, allez simplement avec l'arrière-plan et puis définissez-le égal à la course.

Encore une fois, cela ne va être que temporaire.

Et puis vous pouvez faire la même chose avec une barre de navigation et trudge autour et définissez-le égal à bleu.

Et ce que vous remarquerez, une fois que vous irez à l'écran grand, donc cela va être ce centre de navigation, il ne sera jamais plus grand que ce 1100 20 sauf si vous utilisez le reste de la barre de navigation.

Encore une fois, si vous avez un doute, deux options, soit vous pouvez configurer le bord.

Et c'est aussi quelque chose que les gens utilisent.

Ou vous pouvez simplement ajouter les couleurs d'arrière-plan.

Et de cette façon, vous pouvez clairement voir, d'accord, donc c'est mon centre nerveux.

Et c'est le reste de la carte.

Maintenant, bien sûr, puisque j'ai justifié con au centre, vous pouvez clairement voir que les Madison sont assis au centre de la barre de navigation.

Donc maintenant, laissez-moi venir et ces uns sortent, parce qu'ils sont utiles.

Mais ils sont aussi un peu ennuyeux, parce que bien sûr, je ne veux pas regarder la couleur rouge tout le temps.

Et ensuite, je veux opter pour l'en-tête.

Maintenant, bien sûr, nous stylisons, où nous avons le logo, ainsi que le bouton.

C'est là que je vais configurer la hauteur.

Et je vais opter pour six REM.

Et ce qui est vraiment intéressant, c'est que une fois que nous arrivons au grand écran, nous allons changer cette hauteur, et effectivement nous allons ajouter la hauteur à l'ensemble du nombre.

Mais pour l'instant, puisque nous stylisons simplement le petit écran, nous allons opter pour une hauteur de six bras pour l'en-tête.

Et puis encore une fois, nous voulons opter pour un affichage flexible.

Et nous allons opter pour justifier le contenu, l'espace entre.

Et essentiellement ici, nous poussons simplement ces éléments aussi loin que possible, loin l'un de l'autre.

Donc remarquez maintenant que les boutons sont tout à fait à droite à l'intérieur du logo est tout à fait du côté gauche.

Et puis je veux aussi les configurer au centre verticalement.

Et bien sûr, pour ce faire, nous allons simplement opter pour aligner les éléments au centre.

Bien sûr, vous pouvez utiliser la grille pour cela.

Mais c'est juste toujours ma préférence de rester avec flex.

Si vous avez ces lignes droites horizontales et verticales.

Bien sûr, une fois que cela commence à devenir plus complexe, alors la grille est toujours un meilleur choix.

Et après cela, ils veulent rendre mon logo un peu plus petit.

Donc allez avec un en-tête de navigation.

Et puis je vais cibler l'image.

Et essentiellement, je veux simplement aller au-dessus de 200 pixels.

Maintenant, vous verrez que bien sûr, notre logo est un peu plus petit que nous voulons aller avec maintenant le bouton.

Comme vous pouvez le voir, nous avons déjà une série de styles appliqués parce que nous utilisons cette classe de bouton global.

Mais je veux simplement ajouter un peu de rembourrage différent.

Donc ici, allons-y avec NAB btn.

Et puis je cherche un rembourrage, zéro point 15.

Et bien sûr, je vais opter pour REM.

Et puis la même chose va être ici, où nous allons opter pour zéro point 75.

REM essentiellement ici, faites simplement ce rembourrage un peu plus petit, celui-ci un peu plus grand.

Bien sûr, c'est un choix.

Si vous ne voulez pas cela, vous n'avez pas à appliquer les styles.

Et puis allons-y pour Font Awesome.

Maintenant, l'un est, bien sûr, l'IOM et donc je vais opter pour la navigation.

Et puis je vais définir la taille de la police égale à un point 25.

Un point 25 RPMs.

Et une fois que nous avons le bouton de la carte en place, quand je veux simplement aller à tous les liens.

Donc bien sûr maintenant je parle de toute la liste.

Et en ce qui concerne les liens de navigation, je vais le définir égal à un affichage flexible encore une fois.

Donc affichage flexible heure, nous allons opter pour la direction flexible, égale à une colonne.

Donc maintenant bien sûr, au lieu d'être en une ligne, nous sommes empilés les uns sur les autres.

Et puis il y aura plus de styles.

Donc ici à faire, mais nous nous en occuperons une fois que nous commencerons à basculer les liens, et puis nous irons directement à ce lien individuel.

Mon lien a une classe de lien ici.

Allons-y avec display block.

Donc nous allons changer de l'être ligne un à display block un, et nous voulons opter pour text align.

Et je vais le définir égal à center.

Et bien sûr, Texas au centre, puis ajoutons aussi text transform.

Et nous allons simplement opter pour capitaliser.

Et après cela, ajoutons une couleur différente.

Et dans ce cas, je vais opter pour gray one, mais je vais opter pour 900.

Donc maintenant bien sûr, tous les liens ont la même couleur que notre texte.

Et puis allons-y pour l'espacement des lettres, MT sera égal à notre variable CSS lorsque nous voulons ajouter un rembourrage pour seulement ajouter le rembourrage haut bas, rembourrage, un REM et puis gauche et droite zéro.

Et aussi je veux ajouter une bordure en haut.

Donc allons-y bordure haut un pixel solide, et puis nous cherchons notre variable CSS.

Donc encore une fois, je vais opter pour gray et 500.

Donc ce sera ma bordure.

Ensuite, je veux aussi ajouter une transition parce que lorsque nous allons survoler, je vais changer la couleur de mon lien.

Donc je vais aller ici, nous transitionnons cela est égal à ma variable CSS, bien sûr, dans les styles globaux.

Et puis allons-y simplement avec nav link, et puis survoler.

Donc lorsque nous survolons, nous voulons changer la couleur, et nous allons la définir égale à la primaire.

Et puis enfin, en ce qui concerne ce lien de contact, je veux simplement changer le rembourrage à nouveau, tout comme nous l'avons fait ici avec un bouton d'application.

Pour ne pas faire cela, nous allons simplement ici avec contact, et puis lien, et je cible l'élément de lien réel ici.

Donc j'ai la classe et puis je cible le lien.

Et ici, allons-y avec le rembourrage.

Et encore une fois, je vais opter pour zéro point 15.

REM, et puis un REM à gauche et à droite.

Et une fois que nous avons terminé de styliser le lien de contact, nous avons presque presque terminé.

Mais avant de vous laisser partir, il y a quelque chose que je veux souligner.

Et c'est simplement le fait que si vous regardez le logo, le bouton, vous avez probablement remarqué que même si j'ai configuré pour le parent, pour l'en-tête d'être aligné sur les éléments au centre, le logo et le bouton ne sont pas verticalement en train de s'assembler.

Maintenant, tout d'abord, jetons un coup d'œil à pourquoi cela se produit.

Plus me souvenir, dans l'index HTML, nous avons bien sûr un lien, et ce lien enveloppe l'image.

Donc si nous allons revenir, et encore une fois, je vais le faire juste après l'en-tête, mais cela n'a pas vraiment d'importance où vous le faites, je vais opter pour nav logo.

Et faisons ce truc.

Nous allons avec l'arrière-plan.

Et puis ajoutons le rouge.

Et vous remarquerez que oui, ceux-ci, donc le lien, pas le logo, mais le lien est en une ligne avec le bouton, mais pas le logo qui est assis à l'intérieur de l'aller.

Pour corriger cela, nous devons simplement définir notre logo pour qu'il soit en affichage flexible.

Et puis pour placer l'image au centre, nous devons simplement aller avec aligner les éléments, et puis le centre.

Encore une fois, veuillez garder à l'esprit, nous parlons du logo.

Donc nous parlons du lien, un homme nous l'avons configuré comme affichage flexible et aligner les éléments au centre.

Donc maintenant l'image réelle est au centre.

Maintenant, bien sûr, vous pouvez clairement voir que nous sommes réellement en une ligne.

Donc maintenant nous voulons supprimer l'arrière-plan, nous ne savons même plus.

Et une fois que nous avons corrigé ce petit bug, nous avons terminé de styliser la barre de navigation pour la mise en page de l'écran petit.

D'accord, il semble que nous avons terminé avec le CSS initial de la barre de navigation.

Mais avant de nous inquiéter du style, la mise en page du grand écran, faisons rapidement le bouton de bascule.

Et en aparté, si vous n'êtes pas à l'aise avec JavaScript, vous pouvez simplement copier et coller le code du répertoire final.

Et l'idée est la suivante sur un petit écran, nous voulons masquer toutes les chaînes par défaut.

Et nous allons le faire en configurant la hauteur zéro dans le déjeuner et ne pas les montrer, nous allons créer une nouvelle classe avec la hauteur actuelle ou la connaissance.

Et enfin, en JavaScript, nous allons basculer les liens de navigation en ajoutant et en supprimant la classe show links.

Donc le résultat final devrait ressembler à ceci.

Et si je rendais mon écran plus petit ? Remarquez le bouton.

Et une fois que nous cliquons, nous montrons les liens.

Et une fois que nous cliquons une fois de plus, c'était LAN, nous masquons les liens.

Comme je l'ai déjà mentionné, le plan est le suivant, où nous allons trouver les liens de navigation, les meurtres, nous avons notre à faire avant de faire quoi que ce soit avant de définir la hauteur zéro, je veux en fait vérifier la hauteur des liens de navigation.

Donc ouvrons les outils de développement.

Nous cherchons les éléments.

Et plus spécifiquement, nous cherchons à avancer dans les liens de navigation et je peux voir que la hauteur pour les liens de navigation est de 309,79 pixels.

Et une fois que je connais cette info, je vais créer une classe, je vais dire show lunch.

Et puis nous allons configurer la hauteur pour qu'elle soit exactement celle-ci, ce que nous avons maintenant pour not once, et dans mon cas, je vais opter pour 310 pixels.

Et une fois que j'ai cette hauteur.

Maintenant, bien sûr, je veux aller maintenant, ce que j'aime, comme je l'ai dit, par défaut, je vais les embaucher.

Donc disons ici, la hauteur est égale à zéro, alors nous devons aussi configurer le débordement caché.

Sinon, vous pouvez clairement voir que nous pouvons encore voir les liens.

Donc allons-y ou le flux caché.

Nous voulons aussi la transition parce que lorsque nous allons basculer, en fait, cet effet de bascule se produira au fil du temps, pas instantanément.

Donc, par conséquent, nous allons ici avec la transition.

Nous allons simplement chercher la variable CSS, la transition.

Et une fois que nous avons tout cela en place, nous pouvons en fait le tester en ajoutant et en supprimant la classe show links, E et F ceux-ci et puis bien sûr, nous allons naviguer vers le fichier JavaScript de la fonctionnalité également.

Donc allons à l'écran grand.

Je trouve toujours plus facile de travailler là-bas.

Donc inspectons, bien sûr, je cherche l'élément nav links ou ici, puis cliquez sur la classe.

Et juste à côté des liens de navigation, allez avec show links.

Et ce que vous remarquerez, le moment où vous appuyez sur entrer, maintenant vous pouvez voir les liens.

Si je supprime la classe, alors vous pouvez probablement déjà deviner, nous ne pourrons pas voir les liens.

Effectivement, la seule chose que nous devons faire maintenant est de naviguer vers le fichier JavaScript.

Donc allons dans le répertoire, le JavaScript, nous cherchons app j, s.

Et ici, nous allons commencer avec un simple Hello World.

Et puis dans l'index HTML, nous voulons configurer les balises de script.

Donc disons votre script.

Et en ce qui concerne la source, encore une fois, nous pointons vers le dossier JavaScript, et l'app js.

Si vous pouvez voir le hello world dans une console, alors bien sûr, nous allons dans la bonne direction.

En ce qui concerne l'adresse, vous pouvez sélectionner les liens de navigation et le bouton de navigation directement.

Mais j'aime toujours configurer une fonction qui me permet d'obtenir l'élément nav et si l'élément n'existe pas.

Donc essentiellement, si je reviens à No, alors je lance simplement une erreur qui peut sembler un peu excessive sur un petit projet, mais j'ai quand même décidé de partager la fonctionnalité.

Donc ici, nous voulons aller avec const get element.

Et nous allons passer dans le sélecteur.

Donc cela va être soit les liens de navigation ou le bouton de navigation, ou n'importe quel élément que vous voulez sélectionner.

On.

D'abord, allons-y avec const element.

Donc maintenant sélectionné, et je vais dire document, puis query selector.

Et maintenant nous passons dans le sélecteur.

Et vous savez probablement déjà que dans vanilla j s, s'il n'y a pas d'élément.

Bien sûr, si je passe dans une sorte de sélecteur, qui ne pointe pas vers un élément, ce que je vais obtenir en retour, c'est non.

Donc je vais dire ici, si l'élément existe, seulement s'il existe, alors je vais retourner l'élément.

Sinon, je vais lancer l'air.

Et je vais simplement dire lancer une erreur.

Et bien sûr, je vais passer une sorte de message.

Dans ce cas, je vais opter pour une chaîne de modèle, je vais dire s'il vous plaît, double vérifiez vos noms de classe.

Et nous allons là, il n'y a pas de.

Et bien sûr, maintenant je cherche ce sélecteur.

Et ajoutons une classe ici.

Et une fois que j'ai la fonction, bien sûr, nous allons la tester, où je vais opter pour cons lunch, snom, sélectionner les liens de navigation, et tous passer dans la classe des liens de navigation.

Si je ne vois rien dans la console, alors bien sûr, nous sommes en bonne forme.

Maintenant, si j'ajoute un nom de classe, qui ne pointe pas vers un élément, cela va bien sûr avoir s'il vous plaît double vérifiez vos noms de classe.

Il n'y a pas de bla bla bla classe.

Espérons que cela soit clair.

Donc maintenant bien sûr, nous pouvons définir la classe correcte ici, copier et coller, nous allons chercher nav be 10.

Dans ce cas, bien sûr, nous devons aussi changer le nom ici.

Donc nav, btn, et puis DOM.

Et puis ajoutons simplement un écouteur d'événement sur le bouton, le clic autour et puis chaque fois que je clique sur le bouton, nous allons basculer la classe showings.

Donc nous allons ajouter et supprimer la classe sur l'élément liens.

Donc disons hello ici maintenant btn, van, ajoutez un écouteur d'événement.

Et puis nous allons écouter les événements de clic.

Et bien sûr, nous devons passer dans une fonction de rappel.

En ce qui concerne la logique plus simple, allez avec les liens, class list.

Et basculez.

Donc les listes de classes est la propriété sur laquelle nous avons la méthode de bascule.

Et ici, nous devons simplement dire quelle classe nous voulons basculer.

Gardez à l'esprit ou ici, vous devez passer dans le. nous savons déjà que nous parlons de la classe ou vous devez simplement fournir la valeur de la classe.

Et le moment où je sauvegarde, je peux voir que je n'ai pas de bugs dans la console, ce qui est toujours un bon moment.

Et puis bien sûr, remarquez, lorsque nous cliquons, nous basculons les liens.

Donc si vous voulez le tester sur un grand écran, bien sûr, vous pouvez le faire.

Et vous verrez clairement que le moment où je clique, je montre les liens ici, remarquez comment nous ajoutons à nouveau cette classe.

Bien sûr, dans ce cas, nous ne le faisons pas manuellement.

Et puis une fois que nous cliquons une fois de plus, alors nous masquons les liens.

Et avant de vous laisser partir, laissez-moi simplement dire que je suis pleinement conscient que nous trichons un peu, simplement parce que si nous changeons la quantité de liens, ou la fonctionnalité ne va pas fonctionner comme prévu, parce que gardez à l'esprit que dans le CSS principal, nous codons en dur cette valeur de hauteur.

Donc bien sûr, lorsque nous allons ajouter plus de liens, ou supprimer les liens, notre fonctionnalité ne va pas fonctionner comme prévu.

Si vous avez suivi mon cours JavaScript, vous avez probablement travaillé sur un projet où nous couvrons la fonctionnalité de bascule appropriée, mais puisque ce n'est pas le principal objectif du projet, j'ai décidé de prendre cette route à la place.

D'accord, et une fois que nous avons la fonction de bascule, nous allons placer le doigt et fermer l'app js.

Et maintenant bien sûr, nous allons nous concentrer sur un écran sauvage.

Donc essentiellement, c'est le look que je vise.

Une fois que nous arrivons au grand écran, je veux tous en une ligne, les liens vont être du côté gauche, et puis le contact va être tout à fait du côté droit, et non utilisateur, nous devons simplement trouver une sorte de valeur pour la requête média.

En ce qui me concerne, je vais opter pour 992.

Gardez simplement à l'esprit que bien sûr, je suis zoommé.

Donc techniquement, cela ne va pas se produire exactement à 992.

Donc allons-y avec l'écran des médias.

Et nous allons chercher la largeur minimale, la largeur minimale.

En ce qui concerne la valeur, comme je l'ai dit, je vais opter pour 992.

La première chose que je veux faire est de masquer le bouton de la barre de navigation.

Donc commençons simplement par la classe du bouton de la barre de navigation.

Et nous allons opter pour l'affichage.

Une fois que nous arrivons au grand écran, je ne veux pas montrer le bouton.

Bien sûr, une fois que nous dépassons les neuf pour remarquer que nous n'avons pas le bouton, c'est la première chose que nous voulons accomplir.

Après cela, nous voulons aller avec la barre de navigation, et nous voulons définir la hauteur à six milligrammes.

Si vous vous souvenez, sur un petit écran, nous avons maintenant eu ou ce que six résultats corrects.

Maintenant, dans ce cas, ce n'est pas ce que je veux.

Par conséquent, j'irai avec le nombre.

Et puis nous allons définir la hauteur à six RPMs.

Et encore une fois, si vous voulez vérifier, bien sûr, l'arrière-plan juste là, et vous verrez comment cela va ressembler, puis nous voulons aller avec un couteau au centre.

Et je veux configurer l'affichage flexible, pourquoi ? Parce que je veux tous en une ligne, gardez à l'esprit que bien sûr pour les liens, nous devons encore les configurer comme affichage flexible également.

Sinon, cela ne fonctionnera pas, il y aura encore une direction flexible de colonne.

Mais en ce qui concerne le centre nerveux, oui, je veux l'en-tête, je veux la longueur en une ligne.

Par conséquent, nous allons ici avec maintenant le centre.

Et nous cherchons l'affichage.

Et bien sûr, nous allons le définir égal à flexible, puis nous voulons les aligner verticalement au centre.

Donc allez avec les éléments d'alignement au centre.

Après cela, nous avons le maintenant en-tête.

Et c'est le cas où bien sûr nous allons cibler cela, nous allons dire nav en-tête, je ne veux pas que la hauteur soit de six éléments.

Donc nous allons simplement dire ici, auto.

Donc essentiellement, cela va être la hauteur du contenu réel.

Et puis allons-y avec la marge.

Droite.

Donc cela va simplement créer un peu de distance entre les liens.

Maintenant, si je navigue vers le grand écran, c'est ce que vous devriez voir.

Maintenant, bien sûr, nous pouvons voir les liens.

Et c'est exactement ce sur quoi nous allons travailler maintenant.

Où, essentiellement, nous devons comprendre que si je regarde les liens, je les ai définis pour être égaux à zéro.

Donc que se passe-t-il si je masque les liens sur un petit écran, bien sûr, c'est exactement ce que j'ai maintenant, je ne vais pas pouvoir les voir sur un grand écran.

Donc remarquez, si je montre les liens sur un petit écran, je vais aussi les voir sur un grand écran.

Maintenant, bien sûr, la mise en page est encore domestique, ne vous inquiétez pas de cela.

Ce n'est pas sur ce que nous nous sommes concentrés.

Ce que je veux montrer, c'est que si nous les masquons sur un petit écran, nous ne pourrons pas les voir sur un grand écran.

Pourquoi ? Eh bien, parce que cette hauteur est définie à zéro.

Et pour corriger cela, nous devons simplement cibler la classe en premier, certains liens de navigation, nous voulons aller avec la hauteur, auto.

Et maintenant vous remarquerez que même si les liens sont masqués sur un petit écran, une fois que nous arrivons au grand écran, nous définissons la hauteur, nous pouvons voir les liens.

Maintenant, bien sûr, ce qui est plus courant est la mise en page et parce que c'est un désordre, je veux simplement changer ma direction flexible.

Et je veux la définir égale à la rangée.

Et bien sûr, ils seront en une ligne, puis je veux les aligner au centre verticalement parce que j'ai le bouton et j'ai les uns au cas où il y aurait des différences.

Et remarquez aussi ici, le centre de navigation prend tout l'espace.

Et en ce qui concerne l'en-tête, il a simplement sa propre largeur correcte.

Et il en va de même pour la connaissance.

Mais je veux changer cela centralement.

Puisque maintenant le centre prend tout cet espace, je veux que mes liens prennent le reste de l'espace.

La façon dont nous définissons cela, nous allons simplement avec la largeur, et nous la définissons égale à 100%.

Et oui, le moment où rien n'a changé ici, ne vous inquiétez pas.

Nous allons travailler un peu plus tard.

Mais maintenant, si nous regardons les liens, remarquez qu'ils s'étendent tous, donc j'ai mon centre de navigation, ils sont toujours en affichage flexible et maintenant les liens de navigation s'étendent tous, encore une fois.

Vous voulez que nous routions simplement avec l'arrière-plan et le rouge et vous verrez que maintenant.

Les liens prennent l'espace restant.

Et si je retire cette largeur de 100.

Et bien sûr, ce n'est pas le cas.

Maintenant, bien sûr, ce que je veux, c'est styliser ces liens de navigation spécifiquement, car si vous vous souvenez, il y a assez de styles provenant du petit écran, je veux en fait les remplacer.

Donc allez avec un avalanche de nontargeting à un lien spécifique, et je vais opter pour un rembourrage zéro, puisque nous avons ajouté un peu de rembourrage sur un petit écran, puis nous voulons opter pour une bordure supérieure, un peu égale à aucune, lorsque la marge est concernée, je veux une certaine distance entre les deux, nous allons opter pour une marge, à droite, et nous la définirons égale à un REM.

Et en ce qui concerne la taille de la police, je vais opter pour un REM non.

Et puis enfin, en ce qui concerne ce lien de contact, je veux le placer tout à fait du côté droit et simplement opter pour une marge à gauche, et nous la définirons égale à zéro.

Et ce que vous remarquerez, c'est que nous avons l'en-tête, nous avons le déjeuner.

Et bien sûr, le lien de contact est tout à fait du côté droit.

Et probablement le plus gros piège est la hauteur zéro, nous sommes essentiellement, encore une fois, sur un petit écran, nous la définissons égale à la hauteur zéro, bien sûr, une fois que nous arrivons au grand écran, si nous masquons ces liens sur un petit écran, nous devons les montrer et donc nous la définissons égale à l'aura.

Et avec cela en place, nous avons terminé l'installation de la barre de navigation.

Maintenant, bien sûr, nous pouvons passer à notre prochaine tâche.

D'accord.

Et une fois que nous avons terminé avec la barre de navigation, configurons une structure pour toutes nos pages.

Maintenant, avant de faire cela, l'administrateur a simplement mentionné rapidement que si vous êtes dérangé par la petite marge sur un contact, vous pouvez simplement revenir et ajouter ici une marge.

Et bien sûr, nous cherchons une marge à droite dans ce cas.

Et nous allons considérer égale à zéro parce que bien sûr, tous les liens obtiennent cette marge, à droite.

Donc si nous la supprimons, bien sûr, nous n'aurons pas cet espace tout à fait du côté droit.

En ce qui concerne la structure, nous voulons configurer la classe de page.

Et puis nous voulons aussi configurer le pied de page.

Donc ce sera la structure pour toutes les pages.

Et puis dans différentes pages, bien sûr, nous ajouterons un contenu différent, mais toutes auront la barre de navigation, le pied de page, ainsi que le pont.

Et vous verrez une fois que nous y serons.

Donc d'abord, retournons à index HTML.

Et puis juste après nav, nous avons un de nav, et disons simplement ici, main ou page ou autre chose.

Donc une sorte de commentaire, copier et coller, et nous allons dire fin de main.

Et maintenant, configurons un élément principal.

Et ajoutons une classe de page.

Et puis après le principal, c'est là que nous voulons configurer un pour un court Mingo ici avec Porter.

Et je vais opter pour l'élément pauvre.

En ce qui concerne la classe, puisque il pourrait y avoir un pied de page, aussi, dans une sorte de carte ou quelque chose comme ça.

Je préfère toujours le configurer explicitement comme pied de page de la page.

Mais bien sûr, c'est la préférence.

Techniquement, vous pouvez simplement sélectionner le pied de page dans le CSS, et vous serez toujours en bonne forme.

Et en ce qui concerne le pauvre.

Je veux opter pour un paragraphe ici, puis nous allons avec un caractère HTML spécial.

Donc je vais opter ici avec un esperluette et puis nous allons dire copie.

Donc bien sûr, maintenant nous allons obtenir ce signe de copyright.

Et puis je veux simplement configurer la date.

Pour l'instant, nous allons la coder en dur.

Et puis plus tard dans la vidéo, nous allons en fait configurer le code JavaScript également.

Donc allons-y avec ID et date.

Donc c'est ce que nous allons utiliser en JavaScript.

Comme je l'ai dit, pour l'instant, nous allons simplement coder en dur, nous allons dire 2021.

Et puis juste à côté dans le span, nous allons configurer un autre.

Donc toujours dans le même paragraphe, nous allons avec le second span.

Et ici, allons-y avec la classe et nous allons dire pour le logo pour le logo.

Et écrivons simplement ce qu'est le logo du site.

Dans mon cas, c'est simplement des recettes.

Mais bien sûr, vous pouvez ajouter différents logos également.

Et puis juste à l'extérieur du span, mais toujours dans le paragraphe, nous allons avec construit par, je vais simplement utiliser un plug sans vergogne.

Et je vais configurer un lien retour à John's milk about calm.

Donc allons-y avec href quand je veux aller à l'écran grand, et je vais chercher John's melton.com, je vais prendre le href copier et coller.

Et bien sûr, maintenant j'ai un lien, allons-y simplement ici codage.

Donc cela devrait suffire pour la partie HTML pour la structure de toutes les pages.

Maintenant, bien sûr, nous voulons simplement revenir au main CSS.

Et je vais prendre ce commentaire, copier et coller et nous allons configurer un pour le pied de page également.

Laissez-moi copier celui-ci, copier et coller et puis configurons un pour photo et vous n'êtes pas mature.

Nous allons copier coller une fois de plus, parce que de cette façon je peux configurer le prochain commentaire également.

Et pour la simplicité, je vais simplement le laisser vide.

Maintenant, nous allons en fait commencer par un pied de page.

Et seulement alors nous nous inquiéterons de la page.

Et vous verrez dans une seconde pourquoi, pour le moment, ce que nous pouvons faire sur une page est simplement configurer notre célèbre arrière-plan rouge, afin que nous puissions clairement voir ce que nous stylisons.

Et commençons simplement par cibler le pied de page de la page.

Donc disons ici, pied de page de la page, et je veux opter pour une hauteur égale à des forums.

Donc ajoutez une sorte de hauteur, puis nous allons aussi opter pour un alignement de texte au centre.

Donc maintenant tout le texte va être au centre, puis nous voulons ajouter un arrière-plan.

Et allons-y avec la variable CSS.

Dans ce cas, je cherche la valeur du noir.

Et puis bien sûr, nous voulons aussi ajouter une sorte de couleur.

Dans ce cas, nous allons opter pour la couleur.

Et nous cherchons le blanc.

Donc maintenant bien sûr, tout le texte est blanc, à part le lien, mais je remarque ici que bien sûr, j'ai la hauteur.

Mais je ne place pas le contenu au centre.

Donc en fait, une meilleure approche est de supprimer cet alignement de texte au centre, et nous allons opter pour l'affichage.

Et je vais le définir égal à flexible.

Et puis alignons-les au centre verticalement, et aussi justifions le contenu, qui bien sûr, va le faire horizontalement.

Donc à la fois justifions le contenu, ainsi que les éléments d'alignement sont définis au centre.

Maintenant, nous avons encore quelques marges par défaut.

Et donc nous allons cibler le pied de page, et plus spécifiquement le paragraphe, et aussi la marge inférieure est égale à zéro.

Et une fois que nous avons cela, je veux simplement ajouter des couleurs au lien, ainsi qu'au logo.

Et pour y parvenir, nous ciblons simplement le logo du pied de page, puis la virgule, et puis nous allons avec le pied de page de la page.

Et puis, bien sûr, je veux opter pour la couleur.

Et nous allons chercher la primaire.

Donc une fois que nous avons configuré la première, maintenant le logo, ainsi que le lien ont cette couleur primaire.

Si je regarde le projet complet, c'est ce que je vise.

Maintenant, la prochaine chose que je veux faire est configurer la hauteur de la page.

Parce que si vous remarquez un moment, bien sûr, oui, nous avons la barre de navigation, nous avons le pied de page, mais je veux en fait que la page prenne l'espace restant.

Et comment nous pouvons faire cela, eh bien, nous pouvons utiliser la hauteur minimale.

Et nous allons utiliser la fonction calc, parce que la barre de navigation ainsi que le pied de page ont une sorte de hauteur.

Et d'abord, commençons par une sorte de largeur.

Donc ici, disons l'arrière-plan rouge, et nous allons avec la largeur.

Et la largeur sera toujours de 90% de la taille de l'écran.

C'est pourquoi nous avons des unités de vue.

Et bien sûr, je veux aussi configurer une sorte de largeur maximale.

Et cela sera égal à ma variable CSS.

Donc allons-y avec la largeur maximale.

Et éventuellement, ce que vous remarquerez, c'est que le contenu de la page va être aligné exactement comme la barre de navigation.

Donc si vous vous souvenez, nous utilisons aussi la largeur maximale dans le centre de la carte.

Et c'est pourquoi les deux seront en une ligne.

Maintenant, bien sûr, nous n'avons pas de contenu.

Donc vous ne pouvez pas encore voir cela.

Mais faites-moi confiance, éventuellement, cela va être là, chaque fois que nous voulons opter pour une marge, zéro et auto.

Donc maintenant, je le place toujours au centre.

Et puis je veux aussi ajouter un peu de rembourrage en haut.

Donc disons ici, rembourrage en haut, et allons-y simplement avec deux REM maintenant, bien sûr, vous pouvez clairement voir notre boîte rouge, qui est essentiellement notre page.

Et enfin, ce que nous voulons est configurer cette hauteur minimale.

Donc pour toutes les pages, il y aura toujours cette hauteur minimale.

Je veux que cela soit 100%.

Mais je veux soustraire la hauteur de la barre de navigation ainsi que la hauteur du pied de page.

Donc nous pouvons faire cela en configurant la hauteur minimale.

Lorsque nous allons avec la fonction calc.

Allons-y simplement avec la hauteur de vue honorée.

Donc cela va être 100% sur l'écran moins.

Et puis bien sûr, nous voulons ajouter six heures plus les quatre bras, je ne veux pas que vous remarquiez que quelle que soit la taille de l'écran, cela va prendre au moins 100% de la hauteur.

Maintenant, bien sûr, si nous allons ajouter plus de contenu, cela va être plus grand.

Et vous verrez cela dans les pages ultérieures, mais au moins le minimum va être 100% moins la barre de navigation ainsi que le pied de page.

Et puis avant de l'avoir sur toutes les pages, je veux en fait aller à l'app js, je veux cibler l'élément de date.

Et je veux simplement montrer comment nous pouvons ajouter cela dynamiquement.

Donc pour le moment, supprimons simplement ce code, essentiellement, supprimons l'année en cours parce que nous ne allons pas la coder en dur.

Et je veux revenir à App j s.

Et ici, juste après le bouton.

Nous allons avec const date.

Donc maintenant nous sélectionnons get element et bien sûr je cherche cet Id manqué une date.

Et ici, nous allons simplement avec la constante current year.

Et si vous voulez current year en JavaScript, nous allons simplement avec new date, nous l'invoquons.

Et nous avons une fonction appelée get full year.

Donc maintenant bien sûr, nous devons simplement aller avec date.

Donc c'est l'élément lorsque le contenu textuel est égal à l'année en cours.

De cette façon, nous aurons toujours l'année en cours, nous n'aurons pas à coder cela en dur.

Et puis enfin, une fois que nous avons cette structure, je veux en fait la prendre, copier et coller et la configurer dans toutes les pages.

Et avant que vous ne soyez en colère à ce sujet, avant que vous ne soyez en colère à propos du fait que nous devons encore copier et coller dans toutes les pages, laissez-moi simplement dire une fois de plus, puisque nous utilisons simplement HTML et CSS, nous n'avons pas, nous n'avons pas de concept de modèles ou de composants que nous avons en Corée.

Donc oui, si nous avons plusieurs pages, il n'y a vraiment pas d'autre moyen.

Et bien sûr, une fois que nous avons configuré une structure pour toutes les pages, alors nous nous inquiéterons de l'index HTML.

Et puis une par une, nous ajouterons du code, ce qui signifie le HTML et le CSS au reste des pages.

Donc une fois que vous avez la structure, puisque nous l'utiliserons et toutes les pages, et puisque nous avons tous les liens corrects, que ce soit pour le CSS ou pour le JavaScript, je veux prendre tous ceux-ci, et puis un par un, je veux les ajouter à toutes les pages.

Parce qu'ici, oui, nous avons un peu de code de base.

Mais essentiellement, ce que nous voulons, c'est simplement sélectionner tout, et puis écraser avec notre code actuel qui provient de l'index HTML.

Et bien sûr, la seule chose que vous devez faire ici, c'est simplement changer le titre.

Et puisque c'est une page 404, puisque c'est une page d'erreur, nous allons opter pour une erreur.

Et si vous voulez ajouter plus de texte, bien sûr, vous pouvez le faire.

Mais dans mon cas, je veux et puis juste pour que je puisse comprendre ce qui se passe, où j'ai la page, ajoutez aussi un nouveau.

Et je vais dire notre page, encore une fois, nous devons faire cela pour toutes les pages, nous voulons faire cela pour à propos, contact, recettes, recette unique, modèle de retour, et tags.

Et bien sûr, je vais arrêter la vidéo parce que je ne pense pas que ce soit très utile pour vous de regarder comment je fais 200 pages.

Mais je vous suggère fortement de faire de même parce que de cette façon, ce sera plus facile plus tard lorsque nous configurerons les pages.

Et une fois que vous copiez et collez notre structure de page, votre site web devrait ressembler à ceci, où toutes les pages utilisent la barre de navigation, vous aurez le pied de page, vous aurez aussi la page avec un en-tête avec le nom de la page.

Et bien sûr, un titre qui correspond à ce que est le nom de fichier ou ici.

Et essentiellement à partir de la barre de navigation, vous devriez être capable de naviguer vers toutes les pages ainsi que le 404.

Donc le 404, bien sûr, est celui où nous devons aller à l'URL.

Et disons simplement pour le HTML.

Et effectivement, c'est une page d'erreur, si l'utilisateur cherche une sorte de ressource sur un serveur qui n'existe pas.

Et juste pour montrer comment cela va ressembler dans l'application dynamique réelle.

Laissez-moi simplement trouver ici, Gatsby version trois.

Donc c'est le projet original.

Remarquez, si je cherche une sorte de page qui n'existe pas, disons la page des utilisateurs, aussi dans ce portail pour, donc c'est celui que nous allons configurer ici dans la page d'erreur.

Et avec tout cela en place.

Maintenant, bien sûr, nous pouvons continuer à travailler sur un projet.

Ensuite, je veux en fait travailler sur la page d'accueil, où nous avons cette bannière.

D'accord, et une fois que nous avons toute la structure en place.

Maintenant, bien sûr, inquiétons-nous de notre héros.

Et essentiellement ce que je veux, c'est une sorte de div avec un arrière-plan.

Et pour cet arrière-plan, nous utiliserons l'image.

Et puis nous placerons aussi un texte au centre.

Et en ce qui concerne le HTML, nous voulons aller à index HTML.

Donc bien sûr, ce sera notre page d'accueil.

Et à l'intérieur du main, ajoutons ici un commentaire.

Disons que nous allons chercher l'élément header ici.

Et allons-y avec l'élément header réel avec une classe de hero.

Et à l'intérieur, nous allons avoir hero container et hero tags.

Et vous verrez dans le CSS, pourquoi nous avons cette structure imbriquée.

Donc allons-y avec hero container.

Et puis à l'intérieur de ce hero container, nous allons avoir hero text.

Et là, nous placerons l'en-tête un avec un texte, encore une fois, dans mon cas, ce sera simplement des recettes.

Et puis juste en dessous, nous allons avec un sous-titre.

Maintenant, un sera sans fioritures, sans fioritures, juste les recettes.

Et une fois que nous avons le HTML en place, maintenant, bien sûr, nous voulons naviguer vers main CSS, ouvrir le main CSS ici, nous avons déjà un commentaire.

Donc nous allons simplement dire votre héros, je suppose, avant de faire quoi que ce soit, peut-être que nous allons simplement copier et coller.

Donc nous ne nous inquiétons pas du suivant.

Donc copier et coller.

Et puis disons ici, ici, oh, et ici, je veux simplement configurer une sorte de hauteur pour mon héros.

Et je suppose que je vais opter pour une hauteur de 40 hauteurs de vue, essentiellement 40% de l'écran.

Donc allons-y avec la hauteur.

Et une fois que nous avons cela, ajoutons cet arrière-plan.

Donc allons-y avec l'URL de l'arrière-plan.

Et nous allons chercher l'image.

Et dans ce cas, je cherche dans les actifs.

Et nous allons avec main jpg.

Mais bien sûr, nous voulons le placer au centre, nous voulons nous assurer qu'il couvre tout.

Et aussi il n'y a pas de répétition, bien sûr, nous pouvons le faire de manière longue.

Ou il y a aussi un raccourci, où nous allons et centre, couvrir, et puis nous le définissons égal à ne pas répéter.

Donc une fois que nous faisons cela, bien sûr, nous devrions voir l'image.

Maintenant, ce que je veux, c'est ajouter un rayon de bordure.

Donc je veux autour des bords.

Et je veux aussi ajouter un peu de marge en bas.

Donc allons-y avec la marge inférieure sur l'assertion égale à deux RMS.

Et aussi je veux ajouter ce rayon de bordure.

Donc allons-y simplement avec le rayon de bordure, et définissons-le égal à notre propriété de rayon de bordure globale.

Maintenant, afin de configurer le regard, où j'ai un texte juste au centre, et comme vous le remarquez, ici, l'arrière-plan est en fait un peu plus sombre.

Donc il y a une sorte de superposition sur l'image, nous allons en fait définir celle-ci comme position relative, position relative, et puis le centre du héros.

Donc cette div de fermeture, c'est là que nous allons configurer la position absolue.

Et puis nous allons utiliser ce joueur flexible pour placer un texte au centre.

Donc continuons à faire défiler.

Et nous allons opter pour le conteneur de héros.

Et comme je l'ai dit, nous allons opter pour la position absolue.

Et puisque le parent est positionné, maintenant, bien sûr, nous configurons tout en fonction du parent.

Et puis ici, je veux simplement avoir une largeur de 100%, une hauteur de 100%.

Et puis définissons simplement le haut et la gauche pour qu'ils soient égaux à zéro.

Donc le haut et la gauche, tous deux égaux à zéro.

Et une fois que nous avons tout cela en place, maintenant, bien sûr, ajoutons cette superposition.

Et nous le faisons en allant avec l'arrière-plan.

Et puis nous cherchons RGBA.

Et je vais simplement opter pour 000 0.4.

Donc RGBA.

Maintenant, cela me donne 0.04.

Ce n'est pas ce que je veux.

Donc essentiellement, remarquez comment l'arrière-plan est maintenant plus sombre.

Donc nous avons ajouté la superposition sur le dessus de l'image.

Et bien sûr, si nous allons vraiment sombre, alors bien sûr, il va être difficile de voir l'image.

Donc, par conséquent, je vais ici avec RGB.

Et par conséquent, je peux bien contrôler cette couleur.

Donc plus vous irez sombre ici, bien sûr, plus la superposition sera sombre.

Et la raison pour laquelle nous voulons la configurer, c'est parce que si nous ne le faisons pas, alors bien sûr avec le texte blanc, il va être difficile de voir le texte.

C'est pourquoi nous voulons configurer l'image, nous voulons ajouter la superposition, et nous voulons ajouter une couleur sombre.

Et puis nous allons rendre le texte blanc.

Donc juste après l'arrière-plan, nous pouvons probablement opter pour un rayon de bordure puisque à l'instant, notre image a le rayon de bordure, mais pas le conteneur.

Donc allons-y avec le rayon de bordure, et définissons-le égal à la propriété de rayon de bordure.

Et puis si je veux placer le texte au centre, nous voulons opter pour un affichage flexible, aligner les éléments au centre.

Donc maintenant, ce sera pour le vertical, juste pour le contenu, ce sera pour l'horizontale.

Et puis nous voulons cibler le Hero Packs.

Donc ce sera une div à l'intérieur de ce conteneur.

Donc voici les tags.

Et définissons simplement l'alignement du texte au centre, car vous remarquez, même si le texte du héros est au centre, le texte réel à l'intérieur n'est pas avant d'aller à l'alignement du texte, et nous le définissons égal au centre.

Maintenant, bien sûr, tout est au centre.

Et ajoutons aussi cette couleur blanche.

Donc allons-y avec notre variable CSS.

Et bien sûr, le nom est blanc.

Et puis la toute dernière chose que je veux ajouter est la requête média pour 768 pixels.

Et une fois que nous arrivons à cette taille d'écran, je veux que la taille de la police pour l'en-tête un soit de 4 RPMs et que la marge inférieure soit égale à zéro.

D'ici, allons-y avec l'écran des médias.

Et bien sûr, nous cherchons une sorte de valeur.

Dans ce cas, je vais opter pour des pixels de 768.

Et une fois que nous arrivons à la taille de l'écran, comme je l'ai dit, nous allons opter pour le texte du héros et comment tout le monde, allons-y simplement avec la taille de la police de 4 RPMs.

Et puis définissons la marge inférieure égale à zéro.

Et une fois que nous avons tout en place, naviguons ici, ce sera le look sur un grand écran.

Et si nous rendons cela plus petit, bien sûr, ce sera le look sur mon écran.

Maintenant, comme toujours, je suis massivement zoommé.

Donc techniquement, si vous regardez l'écran petit, il va ressembler à quelque chose comme ceci.

Et une fois que nous avons notre héros en place, maintenant bien sûr, nous pouvons nous concentrer sur nos recettes, où nous aurons une mise en page à deux colonnes.

D'un côté, nous aurons des tags.

Et puis de l'autre côté, nous aurons les cartes magnifiques.

Avec notre héros hors du chemin.

Maintenant, attaquons la grande bête, la mise en page des recettes, où nous avons une mise en page à deux colonnes avec des tags dans une colonne et des cartes dans l'autre.

Maintenant, puisque nous allons réutiliser cette mise en page dans plusieurs pages, prenez votre temps.

Et ne vous précipitez pas avec celle-ci.

Mieux vaut prendre plus de temps maintenant que de courir après quelques erreurs de frappe plus tard de ma part, je vais probablement être encore plus ennuyeux que d'habitude, en répétant les mêmes choses encore et encore.

Puisque ici nous avons la mise en page imbriquée.

Donc cela peut devenir compliqué.

Et donc je pense qu'il est important que je répète essentiellement les mêmes choses.

Et nous allons aussi diviser celle-ci en plusieurs vidéos, juste pour que nous puissions construire tout étape par étape.

La bonne nouvelle est, une fois que nous avons terminé avec les recettes, c'est assez fluide à partir de là.

Et effectivement, nous voulons revenir à l'index HTML, bien sûr, nous cherchons le main et vous voulez placer celui-ci dans le main et donc autoriser un tas de commentaires ici aussi.

Encore une fois, nous allons réutiliser celui-ci.

Donc c'est beaucoup plus facile si vous avez des commentaires clairs où la section suivante commence, ou l'élément.

Et espérons que vous comprenez.

Donc nous allons ici avec la fin de l'erreur.

Et nous aurons un autre ensemble de commentaires.

Et disons simplement le conteneur de recettes.

Je vais le faire ici aussi.

Et disons simplement la fin de l'amour du conteneur de recettes.

Et nous allons avec la section avec une classe de conteneur de recettes, section, conteneur de recettes, à l'intérieur du conteneur, nous aurons deux choses majeures.

Nous aurons un conteneur de tags.

Donc je parle de la colonne de versets ici.

Donc ce sera nos tags.

Et puis nous aurons des cartes de recettes.

Et bien sûr, il y aura plus de contenu.

Mais pour l'instant, configurons simplement ces éléments principaux.

Et encore une fois, nous placerons un tas de commentaires, disons le conteneur de tags.

Et nous allons copier et coller le cours, ici, nous allons dire le conteneur de tags.

Et en ce qui concerne les tags, nous allons simplement avec div avec une classe de conteneur de tags.

Donc si vous voulez, peut-être ajoutons un s ici aussi, juste pour que cela ait un peu plus de sens.

Et puis nous avons une liste de recettes.

Donc ce seront ces cartes.

Et dans ce cas, je pense que je peux simplement copier et coller, nous allons simplement changer les choses autour où je veux sélectionner tous les tags ici.

Et disons recettes.

Et au lieu de conteneur, ce sera une liste.

Donc disons ici.

Donc ce sera la structure pour ce conteneur, le conteneur de recettes, le conteneur de tags, où nous aurons les tags.

Ici, bien sûr, nous aurons les cartes, les cartes de recettes.

Et maintenant, un par un, ajoutons plus de contenu.

En ce qui concerne le conteneur de recettes, nous allons avoir 104 avec un texte de recettes.

Et puis aussi avoir une div avec une classe de liste de tags.

Et essentiellement ici, je vais simplement avoir un déjeuner.

Maintenant, puisque encore une fois, c'est un projet HTML et CSS, nous allons simplement naviguer à travers la page vers la page de modèle de tag, nous allons afficher ces recettes lorsque vous parlez du projet dynamique, mais nous allons le configurer dans Gatsby.

Bien sûr, ici, nous naviguons vers le tag, bien sûr, nous affichons cette recette spécifique ou plusieurs recettes qui sont associées à ce tag.

Gardez à l'esprit que dans ce cas, bien sûr, ce ne sera pas dynamique, nous aurons une seule page et nous naviguons là-bas, le contenu sera toujours le même.

Mais en ce qui concerne le projet dynamique, bien sûr, vous cliquez sur un tag et puis vous affichez uniquement les recettes qui sont associées à ce tag.

Et espérons que vous pouvez déjà voir lorsque cela concerne la mise en page, elle ressemble beaucoup à ce que nous avons ici dans la liste des recettes.

Donc c'est ce dont je parle où nous allons réutiliser cette mise en page.

Certaines parties de cette mise en page assez lourdement autour du projet.

Donc assurons-nous que nous configurons tout correctement.

Donc dans le HTML de l'index, le conteneur de tags contient un tableau de l'en-tête quatre.

Et ici, je veux opter pour la liste des tags.

Et essentiellement, ceux-ci ne seront que des liens vers la page de modèle de tag, ils ne seront pas dynamiques, tous pointeront vers la même page.

Et essentiellement là, nous aurons simplement un contenu statique.

Et en ce qui concerne le href, nous voulons opter pour le modèle de tag HTML.

Et ici, ajoutons simplement quelques valeurs différentes.

Donc je vais opter pour le bœuf.

Et je vais dire un.

Donc ce que j'essaie de dire ici, c'est qu'il y a une recette qui a le tag de bœuf.

Et bien sûr, nous allons simplement copier et coller et changer ces routeurs.

Donc pour le petit-déjeuner, nous allons avec deux que quatre carrots, nous allons avec trois carrots, nous allons avec trois.

Et ici, bien sûr, nous aurons le générique, le food, qui est pour, et encore une fois, pour ne pas être redondant, mais dans un projet normal, bien sûr, cela vient de la base de données.

Donc cette info provient de la base de données.

Et cela change, c'est dynamique, plus d'éléments que vous ajoutez, bien sûr, vous allez afficher différentes infos ici, juste un projet HTML et CSS.

Donc bien sûr, nous codons en dur.

En ce qui concerne la liste des recettes, nous voulons configurer ces gardes.

Donc nous avons terminé avec le conteneur de tags, cela devrait ressembler à ceci.

Je suis de retour dans la liste des recettes, nous voulons configurer un autre commentaire, nous allons avec une recette unique.

Donc ce sera cette carte.

Et nous allons copier et coller.

Donc disons et avons une recette unique.

Et ici, je veux opter pour un lien.

Maintenant, ce lien va aller à la page de recette unique.

Essentiellement, cette page sera probablement la dernière que nous configurerons car il y a aussi beaucoup de travail là-bas.

Mais l'idée est que cela va à la page de tag.

Mais ensuite, celui-ci va à cette recette unique, quelle qu'elle soit, encore une fois, dans notre cas, cela sera codé en dur.

Donc si vous regardez tout le temps afficher les mêmes infos ici.

Mais en général, lorsque vous avez un produit dynamique, bien sûr, vous affichez une recette différente.

Espérons que cela soit clair.

En ce qui concerne le href, nous allons avec single recipe HTML, tout de suite, ajoutons une classe ici, avons une recette.

Et à l'intérieur, nous voulons opter pour une image, en ce qui concerne la source, elle sera dans les actifs.

Et nous allons commencer avec recipe one, puis deux, je crois que nous en aurons quatre.

Donc vous pouvez déjà deviner que bien sûr, dans les actifs, nous avons un dossier de recettes.

Et là, j'ai recipe one, recipe two, trois, et quatre.

Donc commençons par le premier.

Donc nous allons avoir ici une balise image.

Maintenant, laissez-moi fermer la barre latérale.

Et nous allons chercher dans les actifs, et puis plus spécifiquement les recettes.

Et puis là, nous avons recipe one, jpg.

Maintenant, en ce qui concerne l'alternative, disons simplement food.

Et je veux aussi ajouter des classes tout de suite.

Donc la classe IMG générique, rappelez-vous, a été définie dans les styles globaux, ainsi que recipe.

ru IMG master class, je veux apprendre juste après mon image.

Laissez-moi fermer celui-ci.

Et juste après mon image, laissez-moi opter pour l'en-tête cinq.

Et je vais opter pour un texte.

Laissez-moi simplement voir.

Donc je vais opter pour celui-ci.

Et je vais aussi opter pour le temps de préparation et le temps de cuisson.

Donc je vais configurer un paragraphe avec le texte de prep.

Et encore une fois, dans ce cas, nous codons en dur, bien sûr, nous allons opter pour 15 minutes d'une barre verticale.

Et bien sûr, nous allons opter pour cuisiner.

Cela va être égal à cinq minutes.

Laissez-moi sauvegarder, laissez-moi regarder.

Cela devrait être le look sur une grande page.

D'accord, cela semble correct.

Et maintenant, nous voulons simplement copier et coller celui-ci et simplement changer l'en-tête cinq.

Donc je vais laisser le paragraphe exactement le même.

Mais puisque je vais changer les images, je vais aussi changer le texte ici.

Et si vous voulez voir le texte final, naviguez simplement vers le projet complet et bien sûr, c'est ce que nous visons.

Donc ce sont les titres de nos recettes.

Donc laissez-moi simplement prendre ici où j'ai le commentaire de départ et sélectionner tout, y compris le commentaire d'admin et maintenant bien sûr, nous voulons copier et coller trois fois donc 123 et maintenant la seule chose qui reste à faire est de faire défiler vers le haut.

D'accord, c'est notre première recette.

Et nous allons chercher la suivante, nous allons simplement changer l'image.

Maintenant, bien sûr, cela va être le numéro de recette deux.

Et en ce qui concerne le texte, ce seront des côtes grecques, des côtes et laissez-moi simplement sauvegarder pour que je puisse voir Oui, cela semble correct, puis nous avons la soupe aux légumes.

Et cela va être le numéro de recette trois.

Et bien sûr, je vais changer le texte ici aussi.

Et la dernière sera des crêpes à la banane.

Et bien sûr, nous voulons changer l'image aussi.

Donc dans ce cas, nous cherchons le numéro de recette quatre.

Donc si je regarde le grand écran, cela devrait ressembler à ceci.

Bien sûr, nous avons les recettes.

Donc ce seront nos tags.

Et puis nous avons ces quatre cartes de recettes.

Magnifique.

Nous avons en fait terminé avec HTML.

Donc maintenant, naviguons vers main CSS.

Et bien sûr, configurons les styles.

Comme toujours, nous allons commencer par le petit écran, bien sûr, et puis nous nous inquiéterons de la mise en page du grand écran, j'ai mon commentaire ici.

Laissez-moi copier et coller.

Et ici, je vais simplement écrire recettes.

Et afin de nous aider, je vais ajouter quelques bordures, encore une fois, juste pour que nous ayons une compréhension de ce qui se passe.

Donc ici, allons-y avec un conteneur de recettes.

Donc ce sera ce conteneur principal.

Et ici, nous allons opter pour l'affichage de la grille.

Et si vous vous souvenez, par défaut, cela va être une mise en page à une colonne.

Donc c'est exactement ce que je veux sur un petit écran.

Mais éventuellement, gardez à l'esprit que cela va être une mise en page à deux colonnes.

Correct.

Donc nous pouvons aussi bien configurer l'écart maintenant pour les deux pour les rangées, ainsi que les colonnes.

Encore une fois, je parle du conteneur parent, où j'ai les recettes et les cartes.

Et donc, je vais opter pour l'écart ici.

Et je vais dire, deux REM, et nous allons le configurer comme un REM encore, pour l'instant, nous allons seulement utiliser un, parce que nous avons une mise en page à une colonne.

Mais alors éventuellement, une fois que nous avons deux colonnes, essentiellement, une fois que nous avons configuré le mètre queer, bien sûr, alors nous allons utiliser les deux valeurs sont des travailleurs, afin de nous aider plus simplement opter pour deux pixels, solide, et rouge, juste pour que nous puissions voir ce qui se passe.

Donc ce sera mon conteneur principal.

Quand nous voulons opter pour le conteneur de tags, qui est pour les tags, le conteneur de tags.

Et essentiellement, nous voulons configurer tout de suite la bordure juste pour que nous puissions voir ce qui se passe.

Donc ce que nous stylisons.

Et dans ce cas, je vais opter pour le bleu.

Une fois que je sauvegarde, je devrais voir ici que c'est mon conteneur de tags.

Et en ce qui concerne les styles, je veux en fait le placer tout en bas.

Donc je veux changer l'ordre.

Remarquez ici dans l'index HTML, qu'est-ce que j'ai en premier, bien sûr, j'ai les tags.

Correct, j'ai mon conteneur sombre.

Et seulement alors j'ai la liste des recettes.

Et comme je l'ai noté, je vais simplement changer celui-ci aussi.

Donc ce ne sera pas le conteneur de recettes, nous allons avec les listes de recettes, donc et les recettes.

Juste pour avoir un peu plus de clarté sur ce que j'essaie de faire sur un petit écran, c'est en fait de changer l'ordre.

Donc remarquez ici, j'ai le héros en premier.

Et puis j'ai les cartes.

Et tout en bas, j'ai les recettes.

Je veux dire, ce n'est pas grave, vous pouvez techniquement le garder en haut, mais c'est en fait ma préférence de changer l'ordre.

Et si vous vous souvenez, par défaut, tous ont un ordre de zéro.

Donc si vous ajoutez un ordre de un, vous remarquerez que les recettes vont être tout en bas.

Donc essentiellement, nous avons la liste des recettes toujours avec un ordre zéro, et nous changeons simplement l'ordre ici.

Maintenant, bien sûr, une fois que nous arrivons au grand écran, nous allons le changer à nouveau.

Mais c'est un scénario différent, alors nous voulons opter pour un affichage flexible, et une direction de colonne flexible.

Maintenant, encore une fois, gardez à l'esprit que je parle du conteneur parent pour l'en-tête quatre ainsi que le déjeuner.

Donc pour les deux.

Maintenant, en ce qui concerne les liens, il y aura une autre mise en page imbriquée.

Mais nous nous en occuperons un peu plus tard.

Donc disons simplement ici, affichage flexible, puis nous voulons opter pour la direction flexible, nous allons chercher la colonne.

Éventuellement, nous voulons configurer le bouton en bas aussi.

Et nous allons le définir égal à trois REM, donc cela devrait ressembler à ceci, puis nous voulons opter pour une liste de recettes.

Et puis nous allons revenir aux tags.

Donc allons-y avec une liste de recettes.

Et encore une fois, par défaut, cela va être une mise en page à une colonne.

Et nous allons le faire simplement en configurant l'affichage de la grille.

Et puis nous allons tout de suite configurer l'écart de qR yams et un REM et encore une fois, cela va être le même qu'avec le conteneur principal où puisque nous avons une mise en page à une colonne, bien sûr, nous n'utilisons pas pour l'instant les deux valeurs.

Mais comment la liste des recettes va finalement ressembler.

Eh bien, ce sera une mise en page à trois colonnes.

Correct.

Donc, je vais tout de suite ajouter la propriété de l'écart avec les deux valeurs.

Et aussi, je veux faire la même chose où je vais ajouter le rembourrage inférieur égal à trois REM quand nous voulons revenir aux tags.

Donc j'ai configuré presque tous les styles majeurs pour la liste des recettes.

Maintenant, je veux m'inquiéter des tags.

D'abord, faites-moi défiler vers le bas juste pour que vous puissiez voir ce qui se passe.

Nous allons opter pour le conteneur de tags, quand nous cherchons l'en-tête quatre, bien sûr, et nous allons ajouter un peu de marge en bas.

Donc disons ici 0.5 RPMs.

Et en ce qui concerne le mot de la police a été changé, et allons-y avec 500.

Après cela, je veux opter pour la liste entière, bien sûr, je parle de la liste des tags réels, et je vais rendre la taille de l'écran plus grande juste parce que j'ai zoomé.

Sinon, cela va avoir l'air bizarre.

Et nous allons opter pour la liste des tags.

Et ici, nous voulons opter pour l'affichage de la grille, et tout de suite, la configurer comme une mise en page à trois colonnes.

Donc disons la grille, le modèle de colonnes.

Et nous cherchons une fraction, une fraction, et une fraction.

Encore une fois, gardez à l'esprit que cela va être une mise en page pour petit écran.

Une fois que nous arrivons au grand écran, bien sûr, nous allons la remettre à une mise en page à une colonne, alors que nous allons styliser le lien réel.

Donc disons ici, la liste des tags.

Et bien sûr, l'élément de lien en avant.

En ce qui concerne la transformation du texte, nous allons le capitaliser quand nous voulons les configurer comme un affichage de bloc.

Et après cela, nous voulons configurer la couleur.

Et je vais opter pour mon gris 500 ici.

Et aussi j'ajouterai une transition parce qu'il y aura un effet de survol.

Donc la transition.

En ce qui concerne le survol, laissez-moi simplement accélérer cela en copiant.

Ensuite, je vais dire survoler.

Et en survolant, je vais simplement le changer en primaire.

Donc encore une fois, en couvrant à la fois la couleur, et au lieu de gris.

Allons-y avec le primaire.

Une fois que nous sauvegardons, nous devrions voir que lorsque nous survolons, remarquez, bien sûr, nous changeons la couleur du lien, courons, nous voulons aller et styliser la recette.

Maintenant, qu'est-ce que la recette ? Eh bien, ce sera notre carte.

Donc nous avons presque terminé avec les tags, bien sûr, à part le grand écran, et donc je vais encore laisser ces bordures, je les supprimerai à la toute fin.

Et vous n'êtes pas en fait avec moi à la recherche de la liste des recettes.

Et laissez-moi ajouter la bordure ici aussi.

Parce que je pense que cela va être très utile plus tard.

Donc disons ici, vert, disons celui-ci sur votre cours, nous allons voir où nous avons nos colonnes.

Et comme je l'ai dit, nous allons cibler la recette.

Donc ce sera la carte entière de la recette ici.

Et rappelez-vous, c'était un lien.

Donc commencez par l'affichage du bloc.

Et puis une fois que cela est configuré, maintenant, bien sûr, je veux cibler l'image.

Donc chaque carte a l'image.

Donc ciblons-la, disons recette.

Et je crois que la classe 40 image était recette IMG.

Et je vais configurer la hauteur, et je vais opter pour 15 REM work.

Donc Vern, tout de suite un rayon de bordure.

Cherchez notre variable CSS pour cela, bien sûr, le rayon de bordure.

Et en ce qui concerne la marge, eh bien, nous allons simplement configurer la marge inférieure un, REM, nous sauvegardons cela.

Et puis nous voulons opter pour une recette et un en-tête cinq.

Donc bien sûr, ce sera le titre, et aussi vouloir styliser le paragraphe.

Et puis nous avons presque terminé avec un petit écran.

Donc allons-y ici, disons recette.

Et en-tête cinq, comme je l'ai dit, nous cherchons la marge inférieure zéro, puis je veux rendre la hauteur de la ligne plus petite.

Donc allez avec un, si vous vous souvenez dans les styles globaux, bien sûr, par défaut, c'était plus grand.

Et puis en ce qui concerne la couleur, allons-y avec la couleur.

Et nous allons opter pour le gris 700.

Donc ce ne sera pas aussi sombre que le reste de notre texte, ce sera un peu plus clair.

Et puis aussi nous avons un pour le paragraphe.

Donc disons votre recette paragraphe.

Et essentiellement ce que nous cherchons, c'est que la marge inférieure soit égale à zéro parce qu'il y a une marge par défaut.

Et la même chose, la hauteur de la ligne sera égale à un.

Et c'est généralement le cas lorsque je traite avec une sorte de cartes parce que vous ne voulez pas ces hauteurs de ligne massives autour de ce qui est aussi ajouté tout de suite la marge supérieure à être 0.5 RPMs.

Juste pour que nous obtenions un peu d'espace.

En ce qui concerne la couleur, je vais opter pour le gris, mais je cherche 500.

Donc je vais simplement copier celui-ci, juste pour que nous puissions économiser un peu de temps.

Et puis je veux aussi configurer l'espacement des lettres.

Donc l'espacement des lettres, et nous cherchons la variable CSS.

La voilà.

Avec cela en place, nous avons en fait terminé de styliser la mise en page du petit écran.

Maintenant, bien sûr, nous devons simplement nous concentrer sur plusieurs requêtes médias.

Magnifique.

Notre petit écran a l'air assez bien, à part ces bordures, que bien sûr nous allons supprimer un peu plus tard.

Donc maintenant, concentrons-nous sur les différentes tailles d'écran.

Et bien sûr, nous allons le faire en configurant les requêtes médias.

Donc laissez-moi aller ici avec l'écran des médias Et je crois que nous en aurons trois.

Donc tout de suite, configurez-les.

Et puis nous allons simplement nous inquiéter du code à l'intérieur.

Donc allons-y simplement avec 576 pixels.

Et puis nous voulons copier et coller cela deux fois.

Et puis en ce qui concerne les valeurs, l'une sera pour 992.

En ligne, la dernière sera pour 1200 pixels.

Donc nous avons configuré cela.

Et à l'intérieur du premier, nous voulons opter pour la liste des recettes.

Donc c'est la liste réelle où nous avons les cartes.

Gardez cela à l'esprit, je ne parle pas du conteneur, je parle de la liste des recettes où nous avons les cartes, et je veux la configurer comme une mise en page à deux colonnes.

Donc allons-y avec la liste des recettes.

Et nous voulons opter pour le modèle de colonnes de grille.

Et nous allons le configurer comme une fraction, une fraction.

Maintenant, gardez à l'esprit que si nous faisons défiler vers le haut, si nous regardons la liste des recettes, c'est déjà un affichage de grille.

Correct.

Donc, par conséquent, je peux tout de suite configurer cette colonne.

Eh bien, je veux aussi configurer mes images un peu plus, une fois qu'elles sont côte à côte.

Donc sur un petit écran, je veux dire, 15 remc, c'est assez bien.

Mais une fois que la taille de l'écran devient un peu plus grande, ce qui signifie à partir de 576.

Une fois que j'ai deux colonnes, eh bien, en fait, il est un peu plus logique d'opter pour une recette.

Et puis IMG, au moins à mon avis, bien sûr, vous n'avez pas à le faire, mais à mon avis, je vais toujours avec 10 RPMs.

Essentiellement, je les ai rendues plus petites, parfois plus grandes que REM.

Donc espérons que vous comprenez.

Donc maintenant, laissez-moi naviguer ici vers le grand écran juste pour montrer ce qui se passe.

Donc je vais faire celui-ci sur ici.

Donc ce sera notre mise en page à une colonne.

Et puis une fois que nous arrivons à 576, bien sûr, ce sera le look.

Donc maintenant nous avons cette mise en page à deux colonnes.

Espérons que cela soit clair.

Maintenant, nous pouvons nous concentrer sur 992.

Maintenant, à 992, nous allons en fait changer la mise en page pour l'ensemble du conteneur, où nous avons les tags, ainsi que cette liste de recettes.

Et nous allons le faire, bien sûr, nous allons chercher notre requête média.

c'est l'étape numéro un.

Et nous cherchons le conteneur de recettes.

Maintenant, encore une fois, c'est déjà en affichage de grille.

Correct, en commençant par un petit écran.

Donc la seule chose que nous devons vraiment faire est de trouver des valeurs pour les colonnes.

Et dans mon cas, je suis allé avec 200 pixels.

Donc c'est pour les tags.

C'est la largeur de ma première colonne, et puis une fraction, essentiellement pour prendre l'espace restant pour la liste de recettes.

Et en ce qui concerne la liste des recettes, eh bien, j'ai déjà une colonne de modèle de grille définie à une fraction, une fraction, donc je n'ai pas besoin de m'en soucier.

La seule chose que je veux configurer ici, et peut-être que je vais styliser le paragraphe un peu différemment aussi.

Mais en ce qui concerne le conteneur de tags, je veux opter pour ou zéro.

Rappelez-vous, sur un petit écran, quel était l'ordre ? C'était un.

Et quel était le résultat ? Eh bien, le résultat était que les tags sont tous en bas, correct.

Donc ils sont après la liste des recettes.

Maintenant, bien sûr, une fois que nous arrivons à 992, je veux ce look, je veux en fait les deux côte à côte, comme ceci.

Donc je dois le replacer où il appartient.

Et bien sûr, je peux le faire avec un ordre de zéro.

Donc allons-y avec les tags.

Et puis la liste, allons-y avec ou, je suis désolé, pas tagué avec mon mauvais.

Donc le conteneur de tags d'abord, et nous allons avec ou, et bien sûr, il va être zéro.

Et en ce qui concerne la liste des tags, bien sûr, nous avons une mise en page à trois colonnes sur un petit écran.

Mais c'est quelque chose que nous voulons ici, où il n'y a pas de mise en page à une colonne, parce que maintenant bien sûr, ils seront côte à côte.

Maintenant, comment nous pouvons y parvenir, nous pouvons simplement aller à la liste des tags et nous rappeler qu'elle est déjà en affichage de grille, elle a déjà les mises en page des colonnes, nous devons simplement les changer, nous devons opter pour le modèle de colonnes de grille et le configurer comme une fraction.

Et enfin, en ce qui concerne la recette, je veux en fait opter pour la taille de la police du paragraphe à être zéro point 85.

REM, donc vous pouvez le placer à la toute fin ou après la recette, cela n'a pas vraiment d'importance.

Nous allons opter pour le paragraphe de la recette.

Et allons-y simplement avec la taille de la police.

Et comme je l'ai dit, nous allons chercher 0.5 REM.

Enregistrons-le.

Et regardons-le.

Et nous pouvons clairement voir que c'est notre conteneur principal avec une bordure rouge.

Et puis bien sûr, nous avons la bordure bleue pour les tags, je suis désolé, et la bordure verte pour les recettes.

Et comme vous pouvez le voir, une fois que nous avons un écran plus petit, alors bien sûr, nous avons cette mise en page.

Et une fois que nous sommes bons ici, c'est magnifique, maintenant nous avons une mise en page à deux colonnes.

Et enfin, une fois que nous arrivons à 1200 pixels, la seule chose que je veux vraiment faire ici est de rendre la liste des recettes une mise en page à trois colonnes.

Donc laissez-moi revenir.

Et nous allons continuer à faire défiler.

Et bien sûr, à 1200 pixels, nous allons configurer notre liste de recettes pour être un modèle de colonnes de grille.

Et bien sûr, je cherche une mise en page à trois colonnes.

Donc je vais opter pour une fraction, une fraction et une fraction.

Et oui, je suis pleinement conscient.

Et bien sûr, nous pouvons écrire le repeat et tout cela.

Mais dans ce cas, j'ai simplement pensé que ce serait plus rapide si j'optais pour une fraction.

Et puis en ce qui concerne la taille de la police pour l'en-tête cinq, je veux la configurer pour qu'elle soit de un point 15.

REM.

Donc je cherche une recette.

Et puisque j'ai déjà pour le paragraphe, je pourrais aussi bien copier et coller.

Et essentiellement, nous voulons opter pour l'en-tête cinq ici, je crois que c'était l'en-tête cinq, et puis nous allons avec 1.1 point 15 RMS, enregistrons cela.

Et j'ai besoin de revenir à la page d'accueil ici.

Maintenant, regardons notre mise en page pour grand écran.

Donc essentiellement, une fois que notre écran devient de plus en plus grand, bien sûr, nous arrivons aux trois colonnes.

Encore une fois, c'est le look sur un petit écran, où nous avons la liste des recettes en premier.

Tout d'abord, et nous avons les tags, une fois que nous arrivons à 576, nous avons une mise en page à deux colonnes pour la liste des recettes.

Puis une fois que nous arrivons à 992, nous avons une mise en page à deux colonnes pour l'ensemble du conteneur.

Et nous avons toujours ces deux colonnes ici pour la liste des recettes.

Et puis une fois que nous arrivons au grand écran, Wallah, bien sûr.

Maintenant, nous avons une mise en page à deux colonnes.

Ici, nous avons une mise en page à trois colonnes.

Donc maintenant, bien sûr, la seule chose qui reste vraiment est de supprimer ces bordures.

Donc nous avons la liste des recettes, nous avons le conteneur de tags, bien sûr, nous avons le conteneur de recettes.

Et avec cela en place, nous avons abordé la grande bête, félicitations.

Et bien sûr, nous pouvons passer à notre prochaine étape.

Pas mal, pas mal.

Essentiellement, nous avons terminé avec notre propre page.

Donc maintenant, faisons les autres pages aussi.

Nous allons commencer par les plus faciles d'abord, comme l'erreur et les recettes, et éventuellement travailler sur les plus complexes aussi.

Et cette vidéo, je veux compléter trois pages, ou une page ou une page de recettes.

page de modèle.

Commençons par une erreur.

Je sais que je l'ai déjà dit avant.

Mais essentiellement, la page d'erreur 404 est si le serveur ne peut pas trouver la ressource dans le projet Gatsby, cela va ressembler à ceci.

Ou encore, nous allons avec un domaine et puis nous disons erreur.

Et bien sûr, c'est ce qui va renvoyer la page d'erreur.

Et en fait, si vous déployez ce projet, vraiment des recettes simples, un, cela va fonctionner de la même manière.

Donc même le HTML et le CSS sur natla phi, si vous cherchez une sorte de pression, il existe une existence, nous avons le 404, bien sûr, nous allons obtenir ce résultat.

Maintenant, dans notre développement local, cela ne va pas se produire parce que l'extension n'est pas si intelligente.

Donc pour voir la page, bien sûr, nous devons le faire manuellement.

La façon dont nous allons faire cela dans le projet est la suivante, nous étions d'abord sur un grand écran, écrivons simplement 404.

html, D'accord, cela semble correct.

Et puis nous voulons faire la même chose.

Donc laissez-moi prendre l'URL, et simplement copier et coller et la configurer sur un petit écran aussi.

Donc laissez-moi sélectionner tout.

Et puis je cherche 404.

Donc c'est à quoi cela va ressembler.

Maintenant, en ce qui concerne le code réel, bien sûr, nous voulons naviguer vers 404.

html, bien sûr, ce sera notre structure de base pour toutes les pages.

Et pour la page d'erreur, nous voulons simplement ajouter une classe ici, puisque nous allons ajouter un peu plus de styles.

Et disons ici, nous avons un trait d'union.

Et puis en ce qui concerne le contenu, nous allons ici avec une section et puis servir de section.

Allons-y avec l'en-tête un, disons erreur.

Et puis enfin, allons-y avec l'en-tête trois, et aussi une page non sur la police.

Donc resauvez-le ici.

Et maintenant, bien sûr, nous voulons simplement revenir au main CSS.

Encore une fois, nous cherchons notre commentaire, nous voulons nous assurer que nous avons pour le suivant.

ici, je vais simplement dire erreur en ce qui concerne le code.

Essentiellement, ce que nous cherchons, c'est cette classe de page d'erreur.

Et nous allons avec l'alignement du texte, l'alignement du texte, le centre, comme ci.

Et bien sûr, nous voulons aussi ajouter un peu de rembourrage en haut, ce qui sera égal à cinq bras.

Et en ce qui concerne l'en-tête un, allons-y simplement avec la page d'erreur sur l'en-tête un et allons-y avec la taille de la police et RPMs.

Et vous savez, j'ai un peu merdé dans le 404, nous voulons en fait opter pour 404, les nombres marqués le texte de son erreur.

Et bien sûr, nous avons notre page.

Et une fois que cela est fait avec moi, revenons simplement.

Et dans ce cas, nous cherchons la page des recettes, encore une fois, dans la barre de navigation.

page des recettes.

Et ce sera la même chose sur un grand écran où nous voulons aller à la page des recettes.

Et ce qui est vraiment cool, nous avons déjà tout le code pour cela.

Et vous savez, obtenez le code ici, regardez le projet.

Donc c'est notre page d'accueil, correct.

Nous avons le héros ainsi que la mise en page des recettes.

Maintenant, à votre avis, qu'est-ce qu'il y aura dans les recettes ? Eh bien, ce sera à peu près la même page sans le héros.

Et encore une fois, c'est le cas où bien sûr, normalement, c'est une sorte de modèle, ou c'est un composant où vous passez simplement les données.

Donc vous n'avez pas à vous répéter.

Mais comme je l'ai déjà dit un million de fois, puisque nous travaillons avec juste HTML et CSS.

Oui, nous allons devoir copier et coller.

Maintenant, bien sûr, laissez-moi revenir à mon projet.

Et je cherche l'index HTML.

C'est la raison pour laquelle j'ai ajouté tant de commentaires ici, parce que nous ne voulons définitivement pas tout gâcher.

Donc nous avons le main ici, correct avec une classe de page, puis nous avons le héros donc nous pouvons en fait réduire celui-ci.

Et ce que nous cherchons, c'est ce conteneur entier.

Maintenant, il y aura quelques autres instances où nous allons simplement chercher la liste des recettes.

Ce n'est pas le cas, dans la page des recettes, vous voulez prendre le tout.

Donc j'ai ces commentaires où le conteneur de recettes, donc copiez tout avec le commentaire du conteneur de recettes, et puis et du conteneur de recettes.

C'est ce que vous cherchez, pas le main.

Maintenant, cela reste ici.

Mais le conteneur de recettes.

Oui, prenez le tout, copiez.

Et maintenant bien sûr, je veux naviguer vers recipes, HTML, c'est ma page, nous continuons à faire défiler.

Et où nous avons la page, le main, nous voulons simplement déposer notre mise en page de recettes.

Donc nous collons simplement notre code ici.

Laissez-moi sauvegarder recipes, HTML, ainsi que l'index.

Et maintenant dans notre projet, si nous regardons, Wallah, nous avons une page de recettes.

Donc ce sera notre page d'accueil.

Et ce sera notre page de recettes.

Et enfin, dans cette vidéo, je veux travailler sur le modèle de tag, qui va aussi ressembler à quelque chose de très, très familier.

Parce que si nous regardons le projet complet, soit le Gatsby, soit simplement le HTML et le CSS, que vous remarquerez, mais si nous naviguons vers un pont de tag, qu'avons-nous ici, nous avons une sorte de valeur codée en dur, qui bien sûr, encore une fois, ne sera pas le cas dans le projet dynamique.

Donc cette valeur va changer en fonction du tag.

Maintenant, dans ce cas, bien sûr, ce n'est pas le cas, nous aurons toujours ce bœuf.

Et puis que voyez-vous ici ? Cela ressemble à une liste.

Correct ? Maintenant, d'où pensez-vous que cette liste provient ici.

Donc c'est pourquoi nous avons configuré le CSS de telle manière que cela n'a pas vraiment d'importance où nous plaçons cette liste, elle aura une colonne où je vais la mettre sur un petit écran, et une mise en page à deux colonnes sur un écran plus grand.

Et puis une fois que nous arrivons au grand écran, ce sera un monde à trois colonnes.

Et pour le configurer, nous allons simplement chercher le modèle de tag, parce que rappelez-vous, index HTML, ou dans les recettes maintenant aussi, lorsque nous parlons de ces liens de tags, où naviguent-ils ? Correctement.

Donc, par conséquent, nous allons chercher le modèle de tag.

Et puis encore une fois, nous avons le main, une classe de page.

Maintenant, bien sûr, nous voulons simplement le changer un peu, où nous allons commencer par configurer une div de fermeture.

Et nous faisons simplement cela parce que je veux placer l'en-tête quatre au-dessus du reste du contenu.

Et nous allons opter pour le bœuf.

Donc encore une fois, nous codons en dur une sorte de valeur, dans ce cas, le bœuf.

Et maintenant, ce que vous voulez, c'est prendre la liste des recettes de l'index HTML.

Et je ne vais pas répéter tout ce discours sur pourquoi nous copions et collons, parce que je pense que je l'ai déjà mentionné bien trop de fois pendant le projet.

Donc nous cherchons la liste des recettes, pas le conteneur.

Nous cherchons la liste des recettes.

Regardez le commentaire et cherchez la fin aussi.

Donc nous cherchons et avons ici probablement dû nous lever, ou non, désolé, je dois me lever maintenant parce que je cherchais un commentaire différent.

Encore une fois, nous cherchons les recettes, j'ai fait une erreur.

Je l'ai mélangé avec le conteneur de recettes et la liste des recettes.

C'est le point final.

Nous copions celui-ci et en ce qui concerne le modèle de tag, nous copions et collons, et félicitations, nous avons trois pages de moins.

Donc maintenant bien sûr, nous avons la page d'accueil, nous avons les recettes, nous avons 404.

Si nous cliquons sur l'un des tags, que ce soit dans la page des recettes ou dans la page d'accueil, où allons-nous naviguer, nous allons naviguer vers un modèle de tag, où il affichera le sac et la liste des recettes, qui encore une fois normalement pointerait vers les recettes qui sont associées à ce tag.

Et bien sûr, vous allez configurer cela dynamiquement normalement.

Mais si nous nous inquiétons simplement du HTML et du CSS, nous avons trois pages de moins.

Et bien sûr, nous pouvons nous concentrer sur les prochaines pages.

Bien.

Et ensuite, je veux travailler sur la page à propos, où effectivement nous aurons une mise en page à deux colonnes pour les infos, ainsi que la photo.

Et puis ici en bas.

Encore une fois, nous allons utiliser une liste.

Donc techniquement, ce seraient quelques recettes en vedette que vous voulez afficher.

Encore une fois, normalement, cela va être dynamique, vous allez simplement passer les recettes que vous voulez présenter point et Rockers, nous allons simplement utiliser notre liste de recettes, la même que nous avons utilisée dans le modèle de tag, celle-ci ici.

Maintenant, dans ce cas, ou nous allons simplement passer trois.

Donc nous sommes dans le modèle de tag, nous avons configuré quatre paramètres, nous allons simplement opter pour trois.

Et effectivement, nous allons réutiliser cette liste quelques fois de plus tout au long du projet.

La configuration va être exactement la même où encore une fois, en regardant about HTML, j'ai ma page.

Donc j'ai la structure.

Et ici, configurons d'abord ces recettes, et naviguons ici vers la page à propos aussi.

Donc nous pouvons voir tout de suite.

Et une fois que nous avons configuré ces recettes en vedette, donc la liste des recettes, alors nous nous inquiéterons du reste du contenu.

À l'intérieur de la page, nous voulons opter pour une section.

Et puis ajoutons une page à propos.

Donc c'est là que les infos ainsi que la photo vont être situées.

Et puis nous voulons opter pour une autre section.

Et puis appelons simplement cela des recettes en vedette, des recettes.

Et en fait, je ne pense pas qu'il y ait des styles avec, mais plus simplement sur la section avec cette classe.

Et puis à l'intérieur, nous voulons opter pour un en-tête cinq.

Et nous cherchons un titre en vedette.

Et je suis désolé, c'est une classe.

Donc c'est un titre en vedette.

La seule raison pour laquelle j'ajoute ici cette classe est parce que je veux placer le texte au centre.

Et encore une fois, techniquement, nous pouvons utiliser cette fonctionnalité des recettes.

Mais si je me souviens bien, l'en-tête cinq était déjà dans la voiture.

Donc c'est pourquoi je suis simplement allé ici avec cette classe.

Encore une fois, en bref, essentiellement, nous allons définir celui-ci au centre.

Et en ce qui concerne le texte logistique, regardez cette source géniale.

Et juste en dessous.

C'est là que nous voulons placer ces recettes.

Donc retournons à index HTML.

Encore une fois, nous cherchons la liste des recettes.

Même chose, mec.

Cela va bien sûr, éventuellement nous allons supprimer l'une des cartes placées dans ma configuration.

Mais si vous voulez, bien sûr, vous pouvez garder les quatre.

Donc nous copions et collons la liste.

Nous cherchons ce que nous cherchions about HTML correct.

Nous avons un peu perdu l'ordre.

Et puis juste après l'en-tête cinq.

Donc dans les recettes en vedette, nous voulons copier et coller et comme je l'ai dit, Margot's, je vais supprimer l'une d'entre elles.

Donc je vais supprimer la dernière recette.

Et une fois que nous sauvegardons, bien sûr, nous avons notre belle mise en page, comme je l'ai mentionné précédemment, effectivement pour celle-ci pour 205, je veux simplement la placer au centre.

Donc configurons rapidement le CSS.

Et nous cherchons le titre en vedette, je crois, en vedette.

Et nous cherchons le titre.

Et nous voulons simplement opter pour l'alignement du texte au centre.

Maintenant, bien sûr, cela va être au centre sans la partie des recettes.

Maintenant, bien sûr, nous voulons simplement ajouter ces infos, qui vont être ici dans la page À propos.

Nous voulons aussi ajouter une photo.

Donc configurons cela.

Et ici, nous voulons opter pour un article.

Donc c'est là que les infos vont être situées.

Et puis juste en dessous, nous allons opter pour une image.

Et dans ce cas, nous cherchons dans les actifs.

Plus spécifiquement, nous cherchons l'image à propos de l'un et neuf en ce qui concerne l'alternative.

Je vais simplement dire en versant du sel.

Et nous allons aussi ajouter quelques classes à l'image.

Ceux-ci sont suivants, nous allons opter pour notre IMG, donc le global, ainsi que l'image à propos.

Maintenant, en ce qui concerne les infos, nous cherchons l'en-tête deux.

Nous allons simplement taper un texte et vous n'êtes pas dans ce cas, juste pour que nous puissions accélérer celui-ci.

Regardez ce projet déjà.

L'autre, en gros, copiez et collez simplement le texte, il n'y a vraiment aucun intérêt à le retourner de zéro.

Et essentiellement, j'ai obtenu ce texte, je crois de l'ipsum hipster, qui est mon endroit préféré pour obtenir le texte lorem ipsum, effectivement le texte factice.

Et nous allons opter ici pour le premier paragraphe.

Donc il y aura deux paragraphes.

Et je prends simplement le texte ici, si vous voulez, vous pouvez simplement taper Lorem, et puis le nombre de caractères que vous voulez, donc vous pouvez opter ici pour Lorem.

Et puis disons 20, ou 10, ou ce que vous voulez.

Maintenant, dans mon cas, puisque j'ai aimé ce texte mieux, nous allons simplement copier et coller.

C'est mon premier paragraphe.

Et puis bien sûr, nous cherchons un deuxième.

Et tout en bas, aussi avoir le bouton.

Donc c'est ici le bouton, la classe sera btn.

Et nous voulons ou vous n'êtes pas sûr, cela va être un lien, mon bouton me montre supprimer mes excuses, nous allons opter pour un lien, cela va être vers contact HTML, quand nous voulons ajouter une classe de btn.

Et ajoutons un contact.

Et puisque nous avons déjà une classe globale pour le battre, c'est pourquoi nous avons à regarder.

Et maintenant bien sûr, nous voulons revenir au main CSS, et nous voulons simplement appliquer quelques styles à la page à propos, je vais simplement garder celui-ci en bas.

Parce que j'aime garder les choses organisées de cette façon, mais bien sûr, vous allez le laisser en haut aussi.

Nous allons opter pour la page à propos, nous cherchons l'en-tête deux.

Donc c'est cet en-tête principal avec le texte factice.

Donc la page à propos de l'en-tête Q et le héros, disons la transformation du texte, définissons-la égale à aucune.

Et il n'y a pas de transformation parce que pour tous les en-têtes, nous avons cette transformation de base, puis en ce qui concerne la taille de la police, je vais opter pour le gras, donc je vais le rendre un peu plus gras.

Et puis ici, définissons aussi la page à propos.

Maintenant, bien sûr, je parle de cette section.

Et d'abord, je veux opter pour l'affichage de la grille, l'affichage de la grille.

Et encore une fois, par défaut, ce sera cette mise en page à une colonne.

Mais cela ne m'empêche pas de configurer l'écart.

Correct.

Donc encore une fois, j'ai deux bras, et quatre bras.

Donc celui-ci, bien sûr, sera pour ma rangée.

Et puis celui-ci sera pour mes colonnes.

Et encore une fois, le matin nous avons une colonne, donc cela n'a pas vraiment d'importance.

Et puis nous voulons aussi configurer tout de suite un peu de rembourrage ici.

Allons-y avec le rembourrage inférieur, trois REM, donc cela va être ajouté à tout cela.

Donc maintenant bien sûr, nous avons une distance entre la section, la page à propos, nos recettes en vedette.

Et puis je veux aussi cibler tout de suite l'image.

En ce qui concerne l'image à propos, nous avons la classe correcte.

Donc allons-y avec l'image à propos de la moitié.

Et nous cherchons le rayon de la bordure.

Et nous utilisons notre variable CSS pour cela.

En ce qui concerne la hauteur, eh bien, définissons-la à 300 pixels.

Maintenant, bien sûr, la hauteur est un peu plus petite.

Et nous voulons aussi bien sûr, opter pour une sorte de requête média parce que sur un écran plus grand, nous aurons un monde à deux colonnes.

Donc définissons une requête de météorite.

En ce qui concerne la taille, allons-y avec les macros.

Encore une fois, je suis allé avec 992.

C'était juste ma préférence.

Et nous allons cibler la page à propos, configurer le modèle de colonnes de grille, le modèle de colonnes de grille comme une fraction et une fraction.

Donc nous avons une mise en page à deux colonnes.

Et puis en ce qui concerne les rangées, je vais opter pour 400 pixels.

Maintenant, gardez quelque chose à l'esprit où nous n'aurons qu'une seule rangée.

Et essentiellement ce que je fais, je configure la hauteur pour ma rangée, et puis j'utiliserai la hauteur pour l'image et je la définirai égale à 100%.

Donc effectivement, par conséquent, mon image va être la hauteur de ma flèche.

Donc essayons cela ici.

Nous allons dire le modèle de rangées de grille, et nous cherchons 400 pixels.

Et puis bien sûr ici, nous allons avec les éléments de ligne, et nous allons le placer au centre.

Et je vais commenter celui-ci dans une seconde juste pour que nous puissions voir pourquoi nous ajoutons celui-là.

Et allons-y avec notre image à propos et puis ici, nous allons avec la hauteur.

Et comme je l'ai dit, nous allons opter pour 100%.

Donc maintenant, que se passe-t-il sur un petit écran ? Eh bien, ce look, donc une fois que je rendrai la taille de mon écran plus petite, cela ressemblera à quelque chose comme ceci.

Et une fois que nous arrivons à 992, nous avons cette mise en page à deux colonnes, et puis l'image est la hauteur de ma rangée.

Et puisque le texte est plus petit, maintenant bien sûr, nous le plaçons au centre.

Maintenant, si je vais commenter celui-ci, vous remarquerez que le texte est tout en haut.

Donc laissez-moi le remettre là.

Et bien sûr, nous avons la page à propos complétée également.

D'accord, en ce qui concerne l'étape suivante, nous voulons aller à la page de contact.

Et bien sûr, carrelons ce truc.

Pratiquement ici, où je dis les recettes en vedette, nous savons déjà où les obtenir.

Le moment où nous les avons déjà dans le about a man quand il s'agit de form.

Je veux dire, la plupart est déjà dans un CSS global.

Donc nous devrions avoir terminé cela en un rien de temps.

Maintenant, pour l'instant, bien sûr, dans le contact, c'est tout ce que j'ai un texte avec la page de contact.

Et bien sûr, nous allons commencer dans le contact HTML.

C'est ce que nous cherchons.

Et comme je l'ai dit, puisque je veux simplifier cela, d'abord, nous allons à about HTML.

Et nous cherchons ces recettes en vedette.

Donc prenez cette section, la vedette, et collez-la simplement et placez-la dans la page de contact.

Donc prenez tout ce code, revenez à contact HTML.

Et ici, nous aurons deux sections.

L'une sera pour le point info, ainsi que le formulaire.

Maintenant, laissez-moi fermer la barre latérale.

Donc commençons par ce conteneur.

Configurons une section avec une classe de contact, et puis un trait d'union, un conteneur.

Et juste après, nous allons copier et coller nos vedettes.

Donc c'est ce que vous devriez voir sur un écran, les recettes en vedette.

Et bien sûr, nous devons simplement naviguer vers le haut où nous avons le conteneur réel, le contrat.

En ce qui concerne le HTML, je veux dire, il n'y a pas beaucoup, il y a quelques en-têtes, quelques paragraphes, comme je continue à le dire, le formulaire aussi.

Et nous allons commencer avec un article.

Donc l'article va avoir une sorte de classe.

Et nous allons opter pour contact info.

Et cela continue, en ce qui concerne le texte.

Encore une fois, je vais simplement accélérer cela.

Et je vais simplement copier et coller à partir du final.

Donc nous cherchons l'en-tête trois, copier et coller.

Et il en va de même pour ces trois paragraphes.

C'est tout, c'est tout ce que nous avons à faire, venir avec un paragraphe et puis copier et coller.

Il en va de même pour le reste des deux.

Donc un autre paragraphe ici, un autre ensemble de texte.

Si vous n'aimez pas mon texte, bien sûr, vous pouvez toujours opter pour Lorem.

troisième paragraphe, et apprendre encore, nous copions et collons le texte.

Et puis juste à côté de cet article, nous allons placer un autre.

Et c'est là que nous allons placer notre formulaire.

Et effectivement, nous cherchons une forme de classe, ainsi que le formulaire de contact.

Donc c'est là que nous allons ajouter un peu plus de style.

Et c'est ce que vous devriez voir sur l'écran.

Maintenant, je vais supprimer l'action parce que bien sûr, ce ne sera pas dynamique, ce ne sera pas un formulaire fonctionnel.

Et puis, nous allons opter pour une rangée de formulaire.

Et puis je veux ajouter l'étiquette, ainsi que l'entrée.

Donc nous allons ici avec l'étiquette, en ce qui concerne l'attribut pauvre, nous allons ici avec le nom, je veux ajouter une classe de formulaire, un trait d'union, une étiquette, encore une fois, cela provient du CSS global, et puis nous allons simplement ajouter votre nom, Ron, nous allons le sauvegarder.

Et après cela, je vais opter pour une entrée, un type sera du texte, nous allons simplement configurer un nom égal au nom.

Et puis nous allons opter pour un ID ainsi que la classe de l'entrée du formulaire.

Donc définissons cela ici, ne dites pas ID, et je vais le définir égal à neuf.

Donc juste pour m'assurer que les deux attributs, l'ID et les quatre ont la même valeur.

Et nous allons aussi chercher la classe.

Et cela sera l'entrée du formulaire.

Et une fois que j'ai ma première rangée, essentiellement, ce que nous voulons faire est simplement ajouter un commentaire.

Et nous allons dire, une seule rangée de formulaire, aussi ajouté ici, la fin de ma div, et aussi la fin d'une seule rangée.

Et maintenant bien sûr, nous voulons simplement copier et coller, je crois deux fois de plus.

Je veux dire, cela va être une zone de texte, donc peut-être que vous voulez seulement.

Donc prenons celui-ci, copions et collons.

Et en ce qui concerne les valeurs, essentiellement partout où nous avons le nom, nous voulons le changer pour email, montrez-moi sélectionner tous les noms ici.

Je vais opter pour email, et le seul que je dois changer en arrière, bien sûr, c'est celui-ci.

Donc disons que le nom est aussi égal à un email.

Donc si je regarde, oui, le voilà.

Maintenant, bien sûr, nous devons encore ajouter un peu de CSS, mais au moins la configuration de base fonctionne.

Et comme je l'ai dit, nous allons aussi ajouter une zone de texte.

Donc laissez-moi continuer à faire défiler ici.

Et après cette rangée, nous allons en configurer une autre.

La classe est exactement la même.

Donc allez ici avec la rangée de formulaire.

Et puis à l'intérieur.

Encore une autre étiquette.

Dans ce cas, nous cherchons un message, la classe sera toujours une étiquette de formulaire.

En ce qui concerne le texte, écrivons simplement message et c'est là que nous voulons opter pour cette zone de texte, donc juste après cette étiquette, nous allons avec la zone de texte.

Et en ce qui concerne les valeurs des attributs, définissons à la fois le nom et l'ID égaux à un message.

Et puis je vais supprimer les colonnes et les rangées, parce que bien sûr, nous avons déjà tout le style dans un CSS global, donc allez avec la forme, nous cherchons une classe de zone de texte.

Et une fois que nous sauvegardons, nous avons seulement besoin d'ajouter un bouton.

Donc juste après ce Dev, nous allons avec le bouton.

Maintenant, dans ce cas, ce sera le type Soumettre.

Et maintenant, en ce qui concerne le style, nous allons avec btn, btn iphon block.

Maintenant, bien sûr, le bouton va s'étendre sur toute la largeur de notre formulaire.

Et la ligne, en ce qui concerne le texte des messages, allez avec sub.

Et une fois que nous avons tout cela en place, essentiellement, nous devons simplement naviguer vers main CSS.

Bien sûr, laissez-moi ouvrir le fichier pour CSS et travailler pour main CSS, j'ai le about pense que j'ai besoin de copier le commentaire aussi, copier et coller.

Et bien sûr, maintenant je cherche la page de contact.

D'abord la valeur de la page de contact.

Et je vais fermer la barre latérale ici.

Et ce que je veux faire, c'est configurer ce formulaire pour qu'il soit à 100%.

Rappelez-vous, par défaut, nous avons déjà une valeur sur la classe du forum.

Et c'est pourquoi nous avons ajouté cette classe de formulaire de contact.

Et ici, allons-y simplement avec la largeur à être notre pourcentage.

Et en ce qui concerne la marge, je vais opter pour zéro.

Maintenant, le mot bien sûr, utilisera le conteneur, le conteneur de contrat pour les configurer côte à côte.

Et en fait, nous allons le faire maintenant.

où nous voulons revenir au main CSS, nous voulons chercher le contact et apprendre le trait d'union, le conteneur.

Et ici, nous allons opter pour l'affichage de la grille.

Maintenant, encore une fois, sur le petit écran, par défaut, ce sera une mise en page à une colonne.

Mais cela ne nous empêche pas de configurer les propriétés pour l'écart.

Donc deux REM réoriente.

Ici pour la colonne, un homme, je vais aussi ajouter un rembourrage en bas des marqueurs.

Et nous allons opter pour trois RPMs.

Donc ce sera la distance entre ces gars.

Et une fois que nous avons tout cela en place, maintenant, bien sûr, nous voulons simplement nous inquiéter du média.

Et nous allons opter pour l'écran des médias.

En ce qui concerne la largeur minimale, un, nous allons simplement la configurer à 992 pixels de largeur minimale.

Bien sûr, je suis ici, allons-y simplement avec le conteneur de contact.

Et je vais chercher le modèle de colonnes de grille.

Et dans ce cas, je vais opter pour une fraction.

Donc c'est pour le texte, c'est pour la première colonne ici.

Et en ce qui concerne le formulaire, je vais en fait coder en dur, je vais dire 450 pixels.

Et puis puisque je veux du texte au centre, encore une fois, je vais opter pour ces éléments d'alignement au centre.

Donc allons-y ici en ligne.

Et nous allons le définir égal au centre.

Et bien sûr, une fois que nous avons ajouté le CSS, nous avons terminé avec le formulaire de contact, maintenant nous pouvons nous concentrer sur notre prochaine tâche.

Et une fois que nous avons le formulaire de contact en place, maintenant, bien sûr, configurons la page des tags, le moment n'a qu'un en-tête.

Et ce que nous visons, c'est ce look où nous avons les tags.

Bien sûr, ceux-ci seront dynamiques dans le projet normal.

Mais dans notre cas, nous allons simplement coder en dur.

Et une fois que vous cliquez sur un tag, lorsque vous naviguez sur la page de modèle de tag, et bien sûr, cette page nous l'avons déjà, c'est pourquoi nous avons les recettes en place.

Et dans le cadre de la configuration, eh bien, ici, laissez-moi revenir aux tags.

Et je vais faire la même chose ici.

Et bien sûr, je suis déjà dans la page, donc je suis bon.

Nous cherchons tags, HTML, fermez la barre latérale pour l'instant, nous voulons supprimer cet en-tête, nous allons toujours garder la page.

Ce que nous cherchons, c'est la section.

Et je vais opter pour tags wrapper.

Donc c'est la classe ici.

Ajoutons un commentaire.

Donc un seul Montag, et je suis simplement parce que ce sera sous un seul tag et un tag optionnel.

Et puis en ce qui concerne la configuration, ce sera un lien, la classe sera un tag.

Et encore une fois, nous allons coder en dur ces valeurs.

Et je ne vais pas expliquer pourquoi nous codons en dur les valeurs, parce que je crois que je l'ai déjà dit plus qu'assez de fois pendant ce projet où vous voulez que ce lien navigue bien, vers le modèle de tag.

Rappelez-vous, cela représente un tag spécifique et des recettes qui ont ce tag.

Et en ce qui concerne le chemin correct.

Eh bien, c'est le modèle de tag HTML.

Correct.

Comme je l'ai dit, nous allons ajouter une classe ici, et je vais dire tag, et en ce qui concerne les valeurs, nous allons simplement opter pour l'en-tête cinq, nous allons le définir égal à beef.

Et en ce qui concerne le mana recettes, eh bien, ce sera un paragraphe avec une recette.

Et maintenant, ce que nous voulons faire, c'est simplement prendre ce tag, copier et coller, laissez-moi regarder combien sont créés, je pense que je suis allé avec cinq, soudainement voir, le moment où j'ai 1234, montrez-moi copier cela une fois de plus.

Et maintenant, nous voulons simplement changer ces routeurs, nous allons, celui-ci va avoir deux recettes.

Et nous avons le dîner, la nourriture, et tout cela.

Donc laissez-moi faire défiler vers le haut, laissez-moi m'assurer que je ne fais rien avec le premier.

D'accord, celui-là reste le même.

Pour le deuxième, nous cherchons le petit-déjeuner, il va avoir deux recettes.

Ensuite, nous avons un pour les carottes.

Et cela va avoir, je crois, trois recettes.

Ensuite, nous avons le dîner et la nourriture.

Nous avons une recette pour le dîner avec les forestiers, en ligne, la nourriture avec un veut, le HTML est en place.

Maintenant, bien sûr, naviguons simplement vers main CSS.

Et nous voulons configurer un autre nouveau commentaire ici.

Donc allez ici avec les tags, bien sûr, celui-ci un peu plus sérieux que la page de contact, parce que, bien sûr, nous sommes la page de contact, le plus grand était le formulaire.

Mais nous avions déjà une série de styles dans un CSS global.

Donc allons-y avec la page des tags.

Et puis je vais m'inquiéter de mon wrapper, encore une fois, ce sera une mise en page à une colonne, en commençant par le petit écran.

Et à mesure que la taille de l'écran augmente, nous allons aussi changer le nombre de colonnes.

Mais cela ne nous empêche pas de tags wrapper.

Donc c'est l'ensemble du wrapper.

Quand nous allons avec l'affichage de la grille, je vais opter pour qR M.

Donc ce sera pour les colonnes et les rangées, et la même chose.

Nous allons avec le rembourrage inférieur trois yums.

Et une fois que nous avons toutes nos listes en place, maintenant bien sûr, nous voulons simplement nous inquiéter de ce tag unique.

Et nous allons configurer le CSS, ce sera le suivant où nous allons cibler le tag, nous cherchons l'arrière-plan.

Et dans ce cas, je vais opter pour le gris, et 500.

Cela va être la valeur par défaut, puis je veux aussi ajouter tout de suite un rayon de bordure.

Et bien sûr, nous allons utiliser notre variable CSS pour cela.

Après cela, nous voulons opter pour l'alignement du texte au centre.

Donc assurez-vous que le texte est au centre, la couleur, la chose blanche devrait avoir l'air bien.

Et en ce qui concerne la transition, eh bien, nous allons simplement utiliser notre variable CSS, parce que lorsque nous allons survoler, je vais changer cette couleur.

Et puis nous avons presque terminé, je veux simplement configurer le rembourrage haut bas, zéro point 75, REM, et gauche et droite zéro.

Comme je survole le tag, comme je l'ai dit, je veux le changer en couleur primaire, religieux, prenez l'arrière-plan une personne ici, et au lieu de gris 500, nous allons avec le primaire 571.

Remarquez en survolant maintenant, bien sûr, nous changeons la couleur, et nous voulons simplement ajouter des marges, zéro au bas de l'en-tête cinq, paragraphe parce que si vous vous souvenez, par défaut, nous les avons là.

Donc maintenant, bien sûr, nous allons supprimer ces marges.

Et je veux aussi augmenter le poids de la police pour l'en-tête.

Donc configurons l'audition ici.

Nous allons opter pour le poids de la police.

Et définissons-le à 600.

Enregistrons comme vous pouvez le voir, maintenant bien sûr, le poids de la police est un peu plus gras.

Et enfin, nous allons avoir la Commonwealth en commençant par 576.

Et une mise en page à trois colonnes.

Une fois que nous arrivons à neuf ou 92.

Puisque je veux économiser un peu de temps sur le code de base, nous allons simplement copier et coller, le configurer ici 576 nous ciblons un wrapper de tags, bien sûr.

Donc les classes, les tags et le wrapper.

Puisque nous avons déjà l'affichage de la grille, nous allons simplement opter pour le modèle de colonnes de grille.

une fraction, une fraction.

Bien sûr, la seule chose qui reste à faire est de prendre ceci, copier et coller 992 et puis nous aurons trois Commonwealth montre parce que certaines personnes sont probablement énervées et nous allons opter pour répéter.

Nous allons simplement dire trois, une production.

Donc bien sûr, c'est la syntaxe alternative que nous pouvons utiliser.

Maintenant, laissez-moi naviguer vers le grand écran pour les tags.

route sera ma mise en page Une fois que je clique sur un tag, naviguez vers une page de modèle de tag, et avec cela en place, nous avons vraiment besoin de nous inquiéter de cette page de recette unique, celle-ci ici.

Et ne paniquez pas à propos de cette page d'erreur.

Essentiellement, lorsque je configurais la structure pour toutes les pages, j'ai simplement oublié de la changer en une recette unique.

Si vous regardez le titre, bien sûr, il dit recette unique.

Et en ce qui concerne la page de recette unique, elle va ressembler à quelque chose comme ceci, nous sommes de retour à la maison.

Et nous venons de cliquer sur l'une des recettes.

Encore une fois, nous codons en dur ces valeurs, il y en aura quatre pour les crêpes à la banane.

Arrêtez, nous avons une sorte d'info.

Et puis nous avons des instructions, des ingrédients, et des outils.

Et pour faciliter les choses, encore une fois, nous allons séparer ces deux, nous étions dans la première vidéo, ou nous nous inquiétons de toutes les sections d'info.

Et puis nous allons traiter les instructions, les ingrédients.

Et nous allons commencer par naviguer vers la recette unique, bien sûr, ici, d'abord, je veux supprimer celle-ci, nous n'allons plus l'utiliser, la mise en page sera la suivante ou encore une fois, nous avons la page.

Donc c'est là que nous allons placer tout notre contenu.

Et au lieu de la page de recette, nous allons avoir deux sections.

L'une sera la section héroïque de la recette avec une classe de recette et un trait d'union, un héros.

Et puis la seconde sera le contenu de la recette.

Donc c'est là que les instructions, les outils et tout cela vont aller.

Donc nous allons ici avec le contenu de la recette.

Et c'est celui sur lequel nous allons travailler dans la prochaine vidéo.

Et cette vidéo se concentrera sur celui-ci, je vais commencer par placer une sorte d'image, comme je l'ai dit, nous codons en dur cela.

Donc nous cherchons simplement les actifs.

Et puis plus spécifiquement, l'image que nous voulons et Marcos, puisque je vais avec les crêpes à la banane, je vais opter pour le numéro de recette cinq, je veux ajouter quelques classes ici.

Donc nous allons commencer avec notre classe d'image.

Et il y aura aussi un trait d'union de recette, un trait d'union, et un trait d'union d'image.

En ce qui concerne l'alternative, disons simplement banque x, une fois que nous sauvegardons, nous devrions voir l'image, ce qui est toujours un bon signe juste à côté de l'image, nous aurons cette deuxième mise en page.

Et ce sera l'article, sorte d'articles commencez avec l'en-tête deux.

Et nous écrivons simplement les noms des crêpes à la banane.

Et après cela, nous voulons configurer un texte factice.

Et dans ce cas, je vais opter pour un paragraphe et bien sûr, comme je l'ai fait avant, je vais simplement prendre mon texte hipster, copier et coller mon texte.

Génial.

Et nous aurons des icônes de recette.

Donc bien sûr, nous parlons de cette colonne ici.

Et il en va de même pour les tags.

Et je suppose plus correctement, c'est une rangée avec une mise en page à trois colonnes.

Eh bien, bien sûr, nous avons les icônes.

Et puis ici, nous avons une autre rangée où nous affichons les tags.

Donc continuons à faire défiler.

En ce qui concerne les icônes de recette, eh bien, nous voulons opter pour elles, sortez, configurez quelques articles.

Encore une fois, nous ne plaçons pas dans le contenu de la recette.

Donc ajoutons simplement ici un commentaire sur le contenu de la recette.

Donc nous sommes clairs sur l'endroit où nous configurons cela.

Donc nous voulons chercher le héros de la recette.

Et puis juste après le paragraphe, nous allons avec Dev, et nous allons simplement dire les icônes de la recette, nous allons copier et coller.

Et bien sûr, le moment où je configure simplement le commentaire, mais éventuellement le dev sera là.

Et le second sera les tags de la recette.

Et c'est très utile.

Une fois que vous commencez à dépanner.

Faites-moi confiance, ajouter ces commentaires semble être une idée stupide.

Mais de temps en temps, cela vous aide vraiment.

Et puis nous allons chercher eux.

Et comme je l'ai dit, nous allons chercher une icône de recette unique.

En ce qui concerne la configuration, eh bien, nous devons simplement chercher l'icône, et donc je vais opter pour l'élément.

Les classes sont les suivantes FA s et FA Clark, un homme ajouterait une sorte de texte factice qui sera placé dans l'en-tête cinq ou disons le temps de préparation.

Et aussi nous aurons un paragraphe avec une sorte de valeur codée en dur.

Dans ce cas, ce sera 30 minutes.

Et maintenant bien sûr, je veux simplement prendre cet article, copier et coller et changer quelques valeurs autour où le second sera f A ne sont pas FA s FA ne seront pas un temps de préparation.

Gonna être un temps de cuisson.

Ici, je vais simplement opter pour 15 minutes.

Et puis enfin, nous avons les amis des utilisateurs.

Donc c'est le nom de l'icône.

Nous cherchons FA s fa.

Et enlevons ce morceau et disons les amis des utilisateurs, ce ne sera que la quantité de portions, portions.

Et nous cherchons une sorte de valeur encore une fois.

Donc dans ce cas, je vais opter pour six portions.

Et enfin, nous voulons configurer ces tags.

Donc encore une fois, assurez-vous de ne pas placer cela dans les icônes de recette, assurez-vous de le placer ici dans les tags de recette.

Donc il y aura la classe des tags de recette.

Et en ce qui concerne le contenu ici, nous allons avec les tags.

Donc c'est le texte.

Et ce sera un lien.

Maintenant encore une fois, nous naviguons vers une page de modèle de tag, donc dans mon href, doctype, tag, template, et HTML, et nous voulons simplement configurer quelques valeurs factices.

Donc bœuf, sauvegardez-le, maintenant vous voulez prendre le lien.

Donc ne pensez pas aux tags, tag, ne pensez pas au lien, je pense que je vais copier et coller cela, je ne sais pas deux fois de plus.

Donc trois au total.

Laissez-moi fermer la barre latérale, nous voulons simplement changer ces pouvoirs.

Le second sera le petit-déjeuner.

Le troisième sera les crêpes.

Et le quatrième sera la nourriture.

Une fois que nous avons le HTML pour entendre la voix, maintenant bien sûr, naviguons simplement vers main CSS.

Et continuons ici.

D'abord, nous nous inquiéterons du héros de la recette.

Maintenant, bien sûr, je parle du conteneur où le texte ainsi que l'image sont assis, parce que nous devons configurer la mise en page à deux colonnes.

Donc allons-y avec la recette, le trait d'union de la recette.

Et nous cherchons un rembourrage, haut bas, trois, REM et puis gauche et droite zéro chaque fois que nous voulons opter pour l'affichage de la grille.

Donc c'est, bien sûr, notre mise en page pour petit écran.

Et nous allons le configurer comme un écart de deux jeux pour les rangées et les feux d'artifice pour les colonnes.

Mais bien sûr, nous n'avons que les rangées sur un petit écran.

Et puis allons-y avec une requête média.

Et si vous voulez, vous pouvez l'ajouter ici aussi, assurez-vous simplement de déplacer cette requête média en dessous de la recette comptée.

Sinon, il y aura un désordre, vous savez, dans mon cas, restez cohérent.

Je vais simplement le copier et le coller.

Et nous cherchons le contenu de la recette, je veux opter pour le modèle de colonnes de grille.

Et en ce qui concerne les valeurs, nous allons avec deux fractions, donc c'est pour la première colonne.

C'est pour les instructions, et puis une fraction pour l'autre valeur.

Maintenant, si nous allons à l'écran grand, vérifiez-le, nous avons les instructions, ainsi que les ingrédients et les outils dans une deuxième colonne.

Et puis lentement mais sûrement, commençons à travailler sur ces instructions.

Donc nous cherchons une instruction unique.

Et d'abord, je veux opter pour l'en-tête.

Et ce sera un affichage de grille.

Donc maintenant bien sûr, je traite de cette étape, la ligne horizontale que nous ne pouvons pas voir, en ce qui concerne la configuration, ce sera le modèle de colonnes de grille.

Nous cherchons auto, une fraction, montre l'étape qui aura sa hauteur, ou je suis désolé, sa largeur, et la ligne horizontale va prendre le reste.

Je veux aussi ajouter un peu d'écart ici.

Je vais opter pour 1.5 RPMs.

Et qu'est-ce que cette ligne horizontale au centre ? Nous allons opter pour les éléments de ligne, et puis le centre.

Sir, la raison pour laquelle nous ne voyons rien, c'est parce que nous n'avons pas stylisé cette ligne horizontale.

Donc pourquoi ne pas le faire ? D'abord, allons-y avec une instruction unique, quand nous cherchons l'en-tête, et puis plus spécifiquement une div.

Et ici, allons-y avec une hauteur de deux pixels.

Et l'arrière-plan sera un gris.

Et je pense que je vais opter pour ce 300, nous avons notre recette unique.

C'est bien.

Et nous avons aussi cette ligne horizontale.

Maintenant, il y a encore quelques choses que nous devons ajouter.

Ne vous inquiétez pas.

Tant que vous pouvez voir cette ligne horizontale.

Cela signifie que nous allons dans la bonne direction.

Et je vais revenir à l'en-tête et plus spécifiquement, le paragraphe.

Donc nous vivons A single instruction van will import a header.

Et au lieu du jour, nous cherchons le paragraphe.

Et dans ce cas, je veux opter pour la transformation du texte, et la configurer comme majuscule.

Maintenant, bien sûr, nous traitons de cette étape un, deux, et trois, puis allons-y avec le poids de la police.

Et nous allons le configurer à 600.

Gris.

Et ajoutons tout de suite une marge inférieure à être zéro, marge inférieure, zéro, et je veux aussi changer la couleur.

Et je vais la configurer comme primaire.

Et une fois que nous sauvegardons tout, cela fonctionne, enfin, en ce qui concerne l'instruction, donc celle-ci ici, je veux configurer une couleur différente, la cible de cette recette puisque je ne veux pas sélectionner ce paragraphe ici, je vais simplement dire, single, single instruction, one error, et je cible simplement le paragraphe.

Et vous n'avez pas vraiment besoin de supprimer cette erreur, mon mauvais.

Donc essentiellement, je cherche l'ensemble du paragraphe, donc algos single instruction.

Et seulement l'enfant direct de cette instruction, qui est le paragraphe, aura cette couleur et gris.

Donc allez ici avec la couleur.

Et pour le gris.

Je pense que je vais opter pour le séminaire.

Maintenant, bien sûr, celui-ci est un peu plus léger.

Si vous ne me croyez pas, vous pouvez en fait le configurer comme 300.

Et vous verrez clairement que je cible le bon paragraphe lorsque nous voulons styliser la deuxième colonne.

Donc continuons, nous allons dire la deuxième colonne.

Et dans ce cas, il n'y a pas grand-chose à faire, nous allons dire l'affichage de la grille, nous cherchons la grille dans ce cas.

Maintenant, je veux ajouter un programme, qui sera égal à deux RPMs.

Donc c'est la distance entre les deux.

et la connaissance a simplement commencé l'ingrédient unique, ainsi que l'outil unique.

Maintenant, en ce qui concerne l'ingrédient unique, je vais encore m'assurer que je l'épelle correctement.

Je cherche une bordure inférieure, une bordure inférieure.

Maintenant, ce sera deux pixels solides.

Et nous cherchons deux gris.

Donc définissons ici var et puis nous cherchons le gris, et puis 300.

Cela va être la bordure.

Je veux aussi ajouter un peu de rembourrage en bas, rembourrage en bas zéro point 75 RPMs et neuf en ce qui concerne la couleur, je vais opter pour ce gris 700.

Et, il en va de même pour l'outil unique, l'outil unique ici.

Nous allons avec la même bordure, montre copier et coller.

Il en va de même pour le rembourrage.

Donc à peu près les mêmes choses.

Juste les couleurs vont être différentes, où je vais opter pour le primaire 500 et puis en ce qui concerne le texte, je veux simplement capitaliser, donc la transformation du texte, définissons-la comme capitalisée.

Et une fois que tout cela est en place, nous avons terminé avec le projet.

Félicitations.

Et j'espère vous voir dans le prochain.