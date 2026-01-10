---
title: Créer des Applications Web Interactives et Basées sur les Données avec R Shiny
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-09-22T13:17:46.000Z'
originalURL: https://freecodecamp.org/news/build-interactive-data-driven-web-apps-with-r-shiny
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/maxresdefault-1.jpeg
tags:
- name: R Language
  slug: r
- name: youtube
  slug: youtube
seo_title: Créer des Applications Web Interactives et Basées sur les Données avec
  R Shiny
seo_desc: 'Shiny is an R package that makes it easy to build interactive and data-driven
  web apps straight from R.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to use R Shiny.

  Dr. Chanin Nantasenamat, also known as ...'
---

Shiny est un package R qui facilite la création d'applications web interactives et basées sur les données directement depuis R.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à utiliser R Shiny.

Dr. Chanin Nantasenamat, également connu sous le nom de Data Professor, enseigne ce cours. Il est professeur associé en bioinformatique dans une université de recherche et possède plus de 15 ans d'expérience en science des données.

Les applications créées avec Shiny peuvent être hébergées sur une page web autonome ou intégrées dans des documents R Markdown. Shiny permet de construire ces applications web à partir de R et également de les créer en utilisant uniquement du code R.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/giphy--2-.gif)
_Ce R est un peu brillant. :)_

Dans ce cours, vous apprendrez d'abord les bases de Shiny. Ensuite, vous apprendrez à utiliser Shiny pour construire les applications suivantes :

* Imprimer l'entrée de l'utilisateur
* Afficher un histogramme
* Apprentissage automatique (Jeu de données météo)
* Apprentissage automatique (Jeu de données Iris)
* Calculatrice d'IMC

Après avoir construit ces applications, vous apprendrez à les déployer en utilisant Heroku.

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/9uFQECk30kA) (90 minutes de visionnage).

%[https://youtu.be/9uFQECk30kA]

## Transcription

(générée automatiquement)

Apprenez à utiliser R pour construire une application interactive basée sur les données avec le package R shiny.

Dr. Chanin Nantasenamat, également connu sous le nom de Data Professor, enseigne ce cours.

En plus d'enseigner sur sa chaîne YouTube, il est également professeur d'université.

Vous savez probablement que notre langage de programmation peut vous aider à effectuer des analyses statistiques.

Mais saviez-vous que vous pourriez utiliser R pour construire une application web interactive basée sur les données.

Dans ce cours sur Free Code Camp, vous apprendrez comment vous pourriez utiliser le package R shiny pour construire une application web interactive et basée sur les données qui ira d'une application simple permettant d'imprimer les entrées utilisateur, des applications web permettant d'afficher la visualisation de données, ainsi que des applications web permettant de faire des prédictions à partir de modèles d'apprentissage automatique.

Enfin, vous apprendrez à déployer les applications web que vous avez créées dans le cloud au moyen de la plateforme Heroku.

Tous les codes utilisés dans ce tutoriel seront fournis dans la description de la vidéo.

Et sans plus attendre, plongeons-nous dans le sujet.

Avant de commencer, couvrons les bases de ce qu'est un package shiny.

Donc, shiny est un package R qui vous permet de construire une application web interactive, il existe plusieurs packages d'extension qui vous permettront d'étendre la fonction de shiny, y compris les thèmes shiny, le tableau de bord shiny, shiny j, s et plusieurs autres.

Et une fois que vous avez développé votre application web dans shiny, vous voulez la déployer.

Vous avez donc deux options, vous voulez la déployer sur votre propre serveur, par exemple, en utilisant un service comme Digital Ocean ou sur shiny apps.io.

Il existe de nombreux exemples de codes qui peuvent vous aider à démarrer.

Et cela est disponible dans la galerie shiny.

Donc les liens sont dans les diapositives.

D'accord, donc ce que nous allons apprendre aujourd'hui, tout d'abord, nous allons apprendre la structure d'une application web shiny.

Et ensuite, nous allons jeter un coup d'œil à certains des exemples de l'application web shiny.

Et enfin, nous allons vous montrer étape par étape comment vous pouvez construire votre application web interactive.

Donc, jetons un coup d'œil à la structure d'une application web shiny.

Donc, essentiellement, une application web shiny se compose de trois composants.

Donc, le premier composant est l'interface utilisateur, qui est hébergée dans un fichier appelé UI dot r.

Et le second est la fonction serveur, qui effectuera le traitement des données, qui est hébergée dans le fichier appelé server dot r.

Et ensuite, la fonction shiny app fusionnera les composants UI et serveur ensemble.

Donc, l'UI est le front-end qui accepte les valeurs d'entrée de l'utilisateur, le serveur est le back-end qui traite ces valeurs d'entrée pour finalement produire des résultats de sortie qui sont affichés sur le site web.

D'accord, donc vous voyez que les données d'entrée circuleront dans l'interface utilisateur, qui est le site web que vous voyez.

Et ensuite, vous entrerez les données dans la zone de texte, puis les données seront soumises au serveur, le serveur traite les informations, puis il produira le résultat.

Et le résultat est affiché sur les sites web.

D'accord, et ensuite l'utilisateur verra les résultats.

D'accord, donc jetons un coup d'œil à certaines des applications web shiny.

Donc, allons à ce lien.

D'accord, donc c'est la galerie disponible de SHINee.

Et vous pouvez voir qu'il y a beaucoup d'exemples.

Donc, il y a l'intégration de cartes, des insights, une application shiny, et aussi des graphiques de dispersion interactifs.

Vous pouvez également intégrer des graphiques Google, vous pouvez effectuer un clustering k-means, vous pouvez créer des graphiques à barres en utilisant des ensembles de données disponibles à partir du package de données.

Et puis vous pouvez également créer un nuage de mots, d'accord, et il y en a plusieurs autres.

Et puis il y a des widgets comme des boutons, des tables, des curseurs, des entrées, des curseurs, K, téléchargement de fichiers, upload de fichiers, sous-ensembles, ensemble de données et tout cela.

D'accord, donc il y a plusieurs exemples sur la façon dont vous pouvez développer des applications web shiny personnalisées.

Donc, pourquoi ne pas cliquer sur l'un d'eux, le premier, d'accord, donc cette carte est interactive.

Si nous cliquons dessus, nous pouvons zoomer.

Oui, donc vous cliquez sur la couleur, et ensuite elle mettra à jour la carte en fonction de votre entrée, il y a aussi Data Explorer.

Donc, c'est un tableau interactif.

Vous pouvez également trier les données, d'accord.

Ou comment un générateur de nuage de mots.

Vous pouvez jouer avec les paramètres d'entrée, la fréquence minimale de chaque mot.

Par exemple, si c'est 25, cela signifie que le mot courant comme "love" doit être présent au moins 25 fois.

Donc 26 fois afin qu'il soit compté ici, combien de mots limitons-nous à afficher ici ? D'accord, et ceux-ci acceptent l'entrée des livres de notre choix : Le Songe d'une nuit d'été, Le Marchand de Venise ou Roméo et Juliette, nous devons cliquer sur le bouton Changer.

k.

k signifie clustering, en utilisant le jeu de données iris, oui.

D'accord.

D'accord, et ensuite, nous allons jeter un coup d'œil à certaines des applications web issues de mon propre laboratoire de recherche.

Donc, allons-y.

Allons à code stop bio slash osfp.

Donc, en tant que chercheur en bioinformatique et scientifique des données, ce que nous faisons dans notre laboratoire, c'est que nous essayons d'appliquer l'apprentissage automatique afin de donner un sens aux données biologiques et chimiques.

Et donc l'objectif de ce serveur web est de prendre en entrée la séquence protéique, et ensuite nous prédirons si la séquence protéique est un oligomère ou un monomère.

D'accord, donc cliquons sur le bouton Insérer des données d'exemple, et ensuite l'entrée sera un format rapide de la séquence protéique.

Donc la première ligne qui contient le symbole supérieur, suivi du nom de la protéine est donnée ici.

Donc nous voyons que la première protéine est un monomère.

Et la deuxième protéine est un tétramère.

Et cliquons sur le bouton soumettre pour faire la prédiction.

D'accord, et donc nous voyons que la prédiction est correcte à chaque fois, car la première est un monomère.

Et il prédit qu'elle est un monomère.

Et la seconde est un tétramère.

Et il prédit qu'elle est un oligomère.

D'accord, donc c'est l'interface du serveur web de prédiction.

Et si nous cliquons sur les autres boutons, cela ressemblera à n'importe quel autre site web ordinaire.

D'accord, donc ce sont des descriptions sur la façon d'utiliser le serveur web.

Et elles sont écrites en markdown.

Donc cette application shiny peut également intégrer du markdown à l'intérieur.

D'accord, nous fournissons également l'ensemble de données pour le téléchargement.

Et nous l'hébergeons sur GitHub.

Et si vous êtes intéressé à lire cet article, vous pouvez cliquer sur le lien.

D'accord, donc c'est l'article que nous avons publié en 2016, dans le Journal of Chem informatics.

D'accord, donc retournons à la diapositive.

Et commençons.

Nous créons notre propre application web en utilisant SHINee.

Donc, ce que vous voulez faire maintenant, c'est lancer votre studio R ou votre studio cloud R.

Et donc le code qui sera utilisé aujourd'hui est disponible sur le GitHub de Data Professor.

Donc, si vous allez sur github.com, slash data professor, d'accord, et puis vous cliquez sur code, et puis trouvez SHINee slash 001 first app.

Et puis vous voulez cliquer sur App dot r.

Et puis vous voulez faire un clic droit sur le bouton raw ici.

Et puis vous voulez cliquer sur les liens sécurisés, et puis sélectionner une position appropriée où vous voulez sauvegarder le fichier.

Et parce que je l'ai déjà, je vais juste cliquer sur Annuler, mais si vous ne l'avez pas encore, cliquez sur le bouton Sauvegarder.

D'accord, donc ouvrons le fichier app dot r directement dans notre studio.

D'accord, donc avant de commencer, un crédit à Winston Chang pour avoir développé ce modèle que nous avons grandement modifié et simplifié pour créer ce fichier app dot r.

Donc, si vous voulez vérifier la version complète, allez-y ici, les liens sont fournis ici.

D'accord, donc dans cette simplification, nous allons commencer par les étapes de base.

Donc, cette application web est une application web interactive où elle acceptera des valeurs d'entrée sous forme de texte, principalement le prénom et le nom.

Donc, jetons un coup d'œil.

D'accord, donc l'application acceptera une entrée qui a le prénom et le nom. D'accord, donc allons-y et tapons le prénom john et le nom est toujours d'accord, et donc le nom john doe apparaîtra dans la sortie ici et le nom de l'application est ma première application, vous pouvez également le modifier à votre guise, d'accord, et dans cet exemple, nous avons trois barres de navigation donc nous les avons intentionnellement laissées vides ici, selon le modèle original de Winston Chang.

D'accord, donc le code que nous avons est situé sur le nav bar dot one donc un point à noter que vous pouvez également créer plusieurs applications web à l'intérieur de différentes barres de navigation.

Disons que vous voulez modifier le nom comme par exemple le prénom est Jennifer.

Alors vous verrez que le nom est automatiquement mis à jour.

Donc, notez qu'il n'y a pas de bouton Soumettre et chaque fois que vous tapez un nom mis à jour, il mettra automatiquement à jour les résultats.

Donc, dans notre cas, ils implémentent réactif, jetons un coup d'œil à shiny, réactif, expressions réactives, réactivité et aperçu, d'accord, donc c'est basé sur les principes de la programmation réactive, qui est utilisée par le package shiny.

Donc, nous n'allons pas entrer dans les détails.

Mais si vous êtes intéressé, je peux également fournir les liens dans le fichier.

concepts sur la programmation réactive utilisée par SHINee.

D'accord, donc je vais vous fournir le lien ici.

D'accord, donc il y a un moment, nous avons jeté un coup d'œil à l'apparence de l'application web, qui est le résultat final de ce code.

Donc, regardons sous le capot, à quoi ressemble le code ? D'accord, donc dans les diapositives, je vous ai montré qu'il se compose de trois composants.

Donc, jetons un coup d'œil.

Donc, le premier composant est l'UI, qui est juste ici.

Donc, c'est à la ligne 19, jusqu'aux lignes 43k, lignes 19 jusqu'aux lignes 43.

Ceci est l'UI ou l'interface utilisateur, et ensuite les lignes 47 jusqu'à 52 est le composant serveur.

Donc, vous allez remarquer que nous ne faisons pas grand-chose ici.

Nous affichons simplement les résultats.

Et donc le code est très concis.

Et le troisième composant est la fonction shiny app.

Donc, cette chose va assembler l'UI et le serveur.

Donc, c'est essentiellement dire que, d'accord, cette partie ici est l'UI.

Cette partie ici est le serveur et fusionne les deux pour créer un objet shiny app.

D'accord, donc c'est tout ce qu'il y a à comprendre au niveau conceptuel.

Donc, jetons un coup d'œil aux composants à l'intérieur de l'objet UI.

D'accord, donc ici, en utilisant à l'intérieur de la balise fluid page, il utilise l'argument theme, et il indique que nous voulons utiliser le thème C raelian.

thème.

D'accord.

Et le thème C rolling est le thème bleu que vous avez vu il y a un moment.

Disons que je veux le changer en United.

Et je peux cliquer sur recharger, ou je dois d'abord l'enregistrer.

Et puis je cliquerai sur recharger, et il change en United. Puis-je le changer en Yeti, l'enregistrer, et il devient le thème Yeti.

Donc, peut-être que vous vous demandez, quelles sont les options disponibles pour vous.

Donc, si vous recherchez shiny themes dans Google key, les premiers résultats et cliquez simplement dessus.

Donc, voici à quoi ressemble un civilisé, si vous aimez cela, vous pourriez taper zulian, il y a Cosmo Cyborg darkly, paper, lumen journal, flatly readable ? sandstone, simplex, slate, Space Lab, superhero, united et Yeti.

Essayons superhero.

D'accord, donc c'est john doe.

D'accord.

Le voilà.

Par défaut, revenez à civilisé.

Donc, envisageons le code comme des composants modulaires.

Donc, vous allez voir qu'à l'intérieur de l'UI, vous allez avoir une page fluide, vous pouvez dans cette page fluide, vous allez définir le thème.

Et à l'intérieur de la page fluide, en plus du thème, vous allez avoir une page de barre de navigation, n'est-ce pas ? Donc la page de barre de navigation est juste ici.

C'est cette barre.

Et donc le nom de l'application est ma première application.

Donc, c'est le nom de la page de barre de navigation.

À l'intérieur de la page nav bar, il y a le panneau d'onglets.

D'accord, donc le panneau d'onglets comprend nav bar, un nav, bar, deux nav, bar, trois peut à l'intérieur et à l'extérieur.

Un, vous avez le panneau de la barre latérale ici à gauche, à droite, vous avez ici le panneau de la barre latérale, et votre panneau de la barre latérale contient la balise h3, h3 est l'en-tête de troisième niveau, l'entrée.

Et puis l'entrée de texte est le prénom.

Et l'entrée de texte est le type d'entrée.

Donc, si vous changez cela en autre chose, cela aura une apparence différente ici.

Et il y a beaucoup de widgets, d'accord, donc vous pouvez trouver ce que vous voulez.

Vous pouvez choisir le widget que vous aimez, puis le remplacer ici dans le code.

D'accord, donc le prénom est ici, affiché ici.

Et puis cette chose ici est la valeur par défaut.

Donc, disons que je pourrais taper john doe, et l'enregistrer et recharger l'application.

Donc vous voyez que john doe apparaîtra automatiquement par défaut dans la zone de texte, d'accord, mais je peux aussi le laisser vide.

Oui.

Donc, c'est le contenu du panneau de la barre latérale.

Donc, le panneau de la barre latérale acceptera l'entrée à droite et ensuite le panneau principal est ici où nous voyons l'en-tête un, la sortie un john doe, qui est le résultat.

Donc, dans le panneau principal un, à droite, Heather un est à l'intérieur du h1.

Donc, h1 est la balise, qui est la plus grande balise disponible.

Et h4 est une balise plus petite, n'est-ce pas ? Donc nous avons dans l'ordre du plus grand au plus petit, nous avons h1 et h2 h3, h4, n'est-ce pas.

Donc, pour l'entrée ici, nous utilisons h3, si nous la changeons en h1, elle sera plus grande.

Elle aura la même taille que l'en-tête un ici, mais c'est trop grand.

Donc, je vais la changer en h3, nous ne pourrions même pas rendre cela un flux.

Oui, donc vous avez un peu plus grand pour la sortie un ici.

Oui, donc vous pouvez jouer avec le changement des options ici.

D'accord, et donc la sortie de texte verbatim est simplement une zone de texte qui retournera la valeur de sortie.

Donc, c'est juste une simple zone de texte, et puis le nav bar deux nav bar trois, comme nous l'avons mentionné précédemment, il est intentionnellement laissé vide.

D'accord, donc c'est tout ce qu'il y a à l'UI.

Mais la partie confuse est comment l'UI et le serveur interagissent ? Comment envoient-ils des informations dans les deux sens ? Oui, comment l'UI envoie-t-elle la valeur d'entrée au serveur ? Et comment le serveur accepte-t-il la valeur d'entrée ? D'accord, jetons un coup d'œil ici.

Donc, notez que la zone de texte a cette chose appelée text one.

txt one à droite dans le prénom, d'accord.

Et un nom de famille est txt deux, d'accord.

Maintenant, cette stat fait une note de cela, comment si je le mets dans les commentaires t x T one et T x T deux, d'accord, et fait une note de cela à t x t out.

txt ou UT d'accord.

Donc, ces deux seront envoyés à, au serveur TFT deux sera également envoyé au serveur t x t out est généré à partir du serveur.

D'accord, donc retournons aux diapositives.

D'accord, pourquoi ne pas créer une nouvelle diapositive.

Donc, dupliquons cette diapositive.

Donc, appelons cela la première application web.

Et nous allons modifier cela pour refléter le contenu de cette application web.

Donc, les données d'entrée sont txt one.

Et txt to write et la sortie est txt out, oui.

Donc, il enverra txt one et 62 au serveur.

Et donc en fait, le serveur envoie write txt out et le TTL sera affiché.

affichages.

txt out.

Donc, ici txt one et txt deux seront envoyés au serveur txt one et txt deux ici est input dollar sign txt one et input dollar sign txt to D'accord, et donc la question est, comment l'envoie-t-il en tant que txt out, c'est ici output dollar sign txt out, et il va utiliser cette fonction appelée render text.

D'accord, donc il y a plusieurs fonctions de rendu comme render table render text, right que vous pouvez modifier.

Donc, vous pouvez également trouver à partir de la documentation SHINee, d'accord, donc cette sortie txt out, ce qu'elle fait essentiellement, c'est qu'elle utilisera la fonction paste pour combiner TF T one et T deux et séparés par un espace MP.

Et puis elle produira le résultat comme le texte concaténé de TF T one et T deux à l'intérieur de la variable txt out.

Et puis cette variable sera appelée à partir de la sortie de texte verbatim, et puis elle affichera le texte à l'intérieur de la zone de texte.

C'est tout ce qu'il y a à cette application web shiny, cela peut sembler un peu confus, mais si vous comprenez bien les concepts, ce sera très simple.

Et vous pourriez créer n'importe quelle application web selon votre imagination, vous pouvez rendre cette application web basée sur les données, vous pourriez demander une entrée, vous pourriez télécharger un fichier des données d'entrée et puis les données d'entrée seront envoyées au serveur, et puis dans le serveur, vous pourriez créer un modèle d'apprentissage automatique et puis une fois que le modèle d'apprentissage automatique est construit, il renverrait alors les résultats dans l'UI et puis l'UI affichera les résultats prédits.

D'accord, donc cela sera très puissant comme approche de déploiement de modèle pour votre modèle d'apprentissage automatique, il y a plusieurs astuces et conseils que nous utilisons dans notre laboratoire de recherche, et nous pouvons partager cela dans une vidéo future.

Et donc si vous trouvez de la valeur dans cette vidéo, veuillez appuyer sur le bouton like.

D'accord, donc laissez-moi résumer ce processus.

En résumé, ce fichier app Our contiendra trois composants : le composant UI, qui est l'interface utilisateur, il acceptera l'entrée, qui est txt one et txt deux, qui correspondent au prénom et au nom.

Et lorsque vous entrez le prénom et le nom, il sera envoyé au serveur.

Et ensuite, la fonction paste combinera tasty one et txt deux et le mettra dans une variable txt out.

Et ensuite, cette variable TFT out est intégrée dans la sortie de texte verbatim, qui est une zone de texte sur l'UI.

Et en conséquence, vous verrez les valeurs d'entrée que vous avez tapées affichées dans la zone de texte.

D'accord, donc cette première application web, qui est essentiellement en partant des bases, donc rien de fantaisiste ici, juste une application web simple où vous pouvez taper le nom, le prénom, le nom de famille, et ensuite elle affichera le résultat.

D'accord, donc dans les vidéos futures de cette série, appelée l'application web dans notre nous allons avoir plusieurs autres vidéos.

Et si vous avez des idées sur l'application que vous aimeriez que nous développons, faites-le nous savoir.

Donc, veuillez commenter ci-dessous, et je vous verrai dans la prochaine vidéo.

D'accord, donc cette vidéo représente le deuxième épisode de la série des applications web dans notre.

Dans la première vidéo, nous avons couvert comment vous pouvez développer votre toute première application web shiny, et l'application web vous permet d'entrer le prénom et le nom, et l'application web affichera la sortie pour un échantillon.

Si vous entrez le prénom comme john et le nom comme Doe, alors le panneau de sortie affichera john doe.

Donc, dans cette vidéo, nous allons vous montrer comment vous pouvez développer votre deuxième application web en R.

Et donc, l'application web d'aujourd'hui est vraiment assez simple.

L'application web affichera un histogramme du jeu de données sur la qualité de l'air, en particulier les niveaux d'ozone, et l'utilisateur pourra ajuster la taille des bacs, et ensuite l'histogramme s'ajustera en conséquence.

D'accord, donc commençons.

Donc, ce que vous voulez faire maintenant, c'est aller sur le GitHub de Data Professor, donc cliquez sur le dossier code, puis cliquez sur le dossier shiny, puis cliquez sur le dossier 002 histogramme.

Et ensuite, ce que vous voulez faire maintenant, c'est cliquer sur app dot r, puis faire un clic droit sur le lien raw, et ensuite enregistrer le lien sous et ensuite l'enregistrer à une destination souhaitée.

Donc, puisque j'ai déjà téléchargé le fichier, ouvrons le fichier app dot r.

Donc, pourquoi ne pas lancer l'application.

Donc, comme vous pouvez le voir, l'application web a pour titre le niveau d'ozone et le panneau latéral affiché à gauche comme le nombre de bacs en tant que valeur d'entrée de curseur.

Donc, vous pouvez ajuster cela en glissant vers la gauche ou la droite et ensuite l'histogramme résultant sera mis à jour automatiquement en temps réel.

Donc, disons que nous l'avons ajusté à sept bacs, et vous verrez que dans l'histogramme, il y aura un total de sept barres.

Si vous l'ajustez à 12, alors le nombre de bacs ou le nombre de barres sera ajusté à 12.

Donc, qu'est-ce que le bac et ensuite dans un histogramme est essentiellement le nombre de barres et chaque barre représente une plage dans la valeur pour un échantillon de la plage de zéro à cinq ou zéro à 10.

Et donc si vous l'ajustez à une barre, alors vous ne verrez qu'une seule barre ici.

Et si vous l'ajustez à deux bacs, vous verrez deux barres, oui, etc.

Et pour un maximum de 50 barres.

D'accord, donc retournons au code.

Donc, dans ce fichier app dot r, vous verrez qu'à la ligne numéro neuf, il charge essentiellement la bibliothèque shiny et la ligne numéro 10 chargera le jeu de données sur la qualité de l'air dans la mémoire.

Et j'ai déjà épinglé l'UI en rouge ici.

Et le serveur en rouge, et la fonction shiny app en rouge.

Donc, comme dans la vidéo précédente, j'ai déjà mentionné que l'application shiny a essentiellement trois composants principaux constitués du composant UI, qui est l'interface utilisateur et du composant serveur qui acceptera la valeur d'entrée de l'UI, et il effectuera un certain traitement comme montré ici.

Et enfin, il générera la sortie et la sortie sera ensuite renvoyée à l'UI pour être affichée dans le panneau principal.

D'accord, donc récapitulons cela à nouveau.

Donc, cette UI est l'interface utilisateur et elle vous permettra de spécifier le nom du panneau de titre ici qui est spécifié comme aussi niveau.

Donc, jetons un coup d'œil.

Donc, le niveau d'ozone est spécifié par le panneau de titre.

Donc, vous pouvez modifier ce nom si vous le souhaitez.

D'accord, donc disons que vous voulez l'appeler simplement ozone, puis vous devez l'enregistrer et ensuite recharger l'application et l'application sera alors appelée ozone.

D'accord.

D'accord, donc c'est le panneau de titre ici.

Et le bloc de code suivant ici sera la disposition de la barre latérale.

Et la disposition de la barre latérale vous permettra de spécifier le panneau de la barre latérale et à l'intérieur du panneau de la barre latérale se trouvera une entrée de curseur.

Et l'entrée de curseur est essentiellement le nombre de bacs, le nombre de bacs dans l'UI, et elle aura un ID d'entrée de bacs, que le composant serveur reconnaîtra.

D'accord, je vais vous montrer dans un instant.

Et donc la valeur minimale ici est un et la valeur maximale de la bande est 50.

Et la valeur par défaut est 30.

Donc, vous voyez ici que le minimum est un, le maximum est 50.

Et la valeur par défaut est 30.

Donc, vous pouvez ajuster le maximum à, disons, 40.

Et la chute, vous pouvez le tester avec 20.

Et nous allons l'enregistrer et recharger l'application et vous allez voir que l'application web se met à jour automatiquement à 140.

Et avec un défaut de 20.

D'accord, et vous, lorsque vous faites glisser, il se met à jour comme avant.

Donc, ici vous pouvez voir que la taille de l'étape est un parce que lorsque vous faites glisser le bouton, il augmentera de manière incrémentielle de un.

Disons que vous voulez modifier la taille de l'étape à un autre nombre.

Pouvez-vous faire cela ? Oui, vous pouvez.

Donc, vous voulez spécifier l'étape pour qu'elle soit égale à, disons, deux.

Et le minimum que vous voulez, ajustez-le à zéro, enregistrez-le et rechargez l'application.

Et maintenant, la taille de l'étape devient 2k.

Donc, 18 et ensuite vous le déplacez, il devient 20, vous le déplacez, il devient 22k.

Donc, vous remarquez que j'ai également modifié le minimum pour qu'il soit zéro parce que si c'est un, alors la taille de l'étape sera 13579.

Mais si vous en faites un nombre pair, alors la taille de l'étape sera également un nombre pair. D'accord, donc jetons un coup d'œil si la taille de l'étape est un, ce sera 135, oui, ce sera 135.

Donc, je ne peux pas sélectionner 20.

D'accord, donc il doit être uniquement des nombres impairs.

Donc, si vous voulez que ce soit un nombre pair, vous voulez mettre le minimum à devenir zéro.

D'accord.

Donc, ici maintenant, vous pouvez même faire en sorte que la taille de l'étape soit cinq.

Oui ? 05 1015 2025 30, oui.

D'accord, donc notez que l'entrée du curseur a un ID d'entrée de bacs, et allons dans le composant serveur.

Et trouvons bacs où spins, spins, c'est ici et bacs est ici.

D'accord, donc le composant serveur aura deux bacs, l'entrée bacs, et ce sera la valeur de l'argument et breaks, d'accord, donc il vous permettra de spécifier le nombre de bacs dans l'histogramme et x sera le jeu de données sur la qualité de l'air.

Et puis nous utilisons le signe dollar pour spécifier la colonne appelée ozone.

Parce que dans le jeu de données sur la qualité de l'air, laissez-moi arrêter l'application shiny.

D'abord, jetons un coup d'œil à air quality dollar sign.

Et puis notez que vous avez ozone, vous avez solar, vous avez quand vous avez la température du mois.

Ils d'accord, donc nous spécifions ozone.

Et nous allons également noter que aussi on a des données manquantes.

Oui, il a des données manquantes ici nous montrant et un ce que nous allons faire avec les données manquantes est de les omettre de l'ensemble de données en utilisant la fonction NA dot omit et puis les sauvegarder dans la variable x.

D'accord, et puis la variable bins déterminera quelle est la valeur minimale du bac et quelle est la valeur maximale du bac.

D'accord, donc la fonction suivante est la fonction histogramme où x est la donnée d'entrée, qui est la colonne air quality ou sown et les breaks seront égaux au nombre de bacs que nous spécifions ici, la couleur sera discolor, qui est une couleur bleutée, et la bordure sera noire.

Donc, c'est la couleur bleue mentionnée ici et la bordure est noire.

Donc, nous voyons une ligne noire et l'étiquette x est aussi au niveau de l'ozone.

Donc, l'étiquette x est ici.

Et puis le main est l'histogramme du niveau d'ozone.

Donc, main est ici, n'est-ce pas ? Donc, vous pouvez simplement étiqueter ou aussi le texte principal.

Donc, dans cette sortie dollar sign dist plot, nous allons utiliser le render plot et puis cela générera une sortie appelée output dist plot.

Et puis nous allons connaître cela.

Si nous nous trompons dans le panneau principal du composant UI, la fonction plot output aura un output ID égal à ce plot.

D'accord, donc le nom, ce plot ici et ce point ici sont le même objet.

Donc, le serveur générera cet objet de sortie appelé ce plot et l'enverra au composant UI pour l'affichage dans le panneau principal.

Donc, le panneau principal est situé ici.

D'accord, donc finalement, la fonction shiny app fusionnera le composant UI et le composant serveur.

Donc, vous allez voir que le code communique entre l'UI et le serveur, n'est-ce pas, donc l'UI acceptera l'entrée, qui est le nombre de broches et il enverra un nombre de broches au composant serveur, et le composant serveur générera le tracé de l'histogramme.

Et le tracé de l'histogramme sera contenu dans cette sortie ce plot et il sera envoyé à la fonction plot output dans le panneau principal de l'UI.

Et donc vous verrez l'histogramme résultant être généré.

Et si vous ajustez la valeur du nombre de bacs d'entrée, alors le tracé se mettra également à jour automatiquement en utilisant la fonction réactive de SHINee.

D'accord, donc vous pouvez personnaliser la couleur si vous le souhaitez, faisons-la 003366.

D'accord, donc c'est bleu foncé ? Ou si nous l'appelons simplement bleu ? Ou comment faire pour utiliser le rouge.

D'accord, donc le tracé deviendra rouge, si nous utilisons le vert.

Donc l'histogramme sera également vert.

Donc, ici, vous pouvez personnaliser la couleur à votre guise et expérimenter.

Et n'oubliez pas de télécharger cela sur votre GitHub afin de commencer à construire votre portfolio pour les projets de science des données, et ensuite vous allez avoir plusieurs dépôts dans votre GitHub en un rien de temps.

Félicitations, vous avez construit votre deuxième application web shiny en R. D'accord, donc cette vidéo représente le quatrième épisode de la série des applications web dans notre.

Et aujourd'hui, nous allons couvrir comment nous pouvons développer un prédicteur Iris, qui est un modèle d'apprentissage automatique en arrière-plan.

Et l'application web permet à l'utilisateur de sélectionner les valeurs d'entrée pour les quatre paramètres d'entrée et d'appuyer sur le bouton soumettre et de faire une prédiction.

Donc, sans plus attendre, commençons.

D'accord, donc la première chose que vous voulez faire est d'aller sur le GitHub de Data Professor.

D'accord, une fois que vous êtes arrivé ici, vous cliquez sur le lien code, puis trouvez SHINee, puis cliquez sur le zéro série pour Iris predictor.

Donc, ce que vous voulez faire maintenant, c'est de télécharger les trois premiers fichiers comprenant app numeric dot, notre app, slider dot r et le model dot r, car les trois autres fichiers trouvés ci-dessous seront générés automatiquement lorsque nous exécuterons le code.

D'accord, donc pourquoi ne pas cliquer sur chacun d'eux manuellement.

Et puis pour chacun, faites un clic droit sur le bouton raw et cliquez sur le bouton Save Link As et ensuite vous sélectionnez l'emplacement dans votre ordinateur où vous voulez sauvegarder les fichiers.

Donc, vous faites cela pour les trois fichiers, app numeric that our apps are et le model dot r.

D'accord, donc je l'ai déjà fait.

Et je vais retourner à l'application our studio.

D'accord, avant de commencer, jetons un coup d'œil à ce que l'application web de prédiction iris que nous allons développer aujourd'hui ressemble à ce que vous voulez frapper sur l'application run, vous devez vous assurer que votre répertoire de travail est dans le dossier qui contient tous les fichiers nécessaires à l'exécution de celui que vous venez de télécharger.

D'accord, et une fois que vous vous êtes assuré, vous voulez cliquer sur le bouton run app.

D'accord, donc voici à quoi ressemble l'application.

Et elle vous permet de mettre les quatre paramètres d'entrée.

Et donc ce sont les valeurs par défaut que vous pouvez ajuster en conséquence.

Et puis lorsque vous cliquez sur le bouton soumettre, la prédiction sera faite.

Et ici, la prédiction est faite pour que le paramètre d'entrée soit prédit comme une fleur Iris setosa et la probabilité qu'il s'agisse d'une Iris atossa est de 100% de sens, d'accord, et donc si vous changez les paramètres d'entrée et donc la prédiction changera également car le paramètre d'entrée sera alimenté dans le modèle prédictif, qui est une forêt aléatoire.

Et puis la forêt aléatoire effectuera la classification.

Et elle a classé ce paramètre d'entrée comme une Iris virginica avec une probabilité de 100%.

Donc, jetons un coup d'œil sous le capot, à quoi ressemble réellement le code ? D'accord, donc le premier code que vous voulez ouvrir maintenant est le model dot r.

Donc, dans ce tutoriel, nous allons pré-construire le modèle de forêt aléatoire, et ensuite nous allons le charger, n'est-ce pas.

Donc, comme vous vous en souvenez, dans les vidéos précédentes de cette chaîne, nous vous avons montré comment vous pouvez déployer votre modèle prédictif dans un fichier RDS.

Et donc ce que vous voulez faire, c'est développer le modèle dans ce fichier model, dot our, et vous l'enregistrez en tant que RDS, n'est-ce pas ? Donc vous déployez cela.

Et puis vous allez le lire ici à la ligne numéro 15, vous allez lire le model dot RDS n, et vous allez lui donner un nom, le nom est model, et ensuite nous allons utiliser ce modèle pour faire la prédiction.

Donc, l'avantage de cela est que le modèle est déjà construit.

Et donc il n'y a pas de charge de travail supplémentaire sur l'application shiny.

Donc, elle peut simplement lire le modèle et effectuer la classification.

Donc, cela sera bénéfique dans le cas où le modèle prédictif prendra beaucoup de temps à construire le modèle.

D'accord, donc jetons un coup d'œil au fichier model dot r où nous allons construire le modèle.

Donc, les premières étapes que nous voulons faire maintenant est de charger les bibliothèques, qui incluront le our curl et le random forest.

Donc, la bibliothèque our curl nous permettra de lire le GitHub de data Professor pour télécharger le jeu de données iris, et ensuite le random forest sera utilisé pour créer le modèle de prédiction.

Et nous avons également besoin du package carrot afin de faire la division des données.

D'accord, donc Iris ici signifiera que nous allons créer un objet de données appelé Iris parce que nous allons lire le CSV, qui récupérera le fichier CSV à partir du GitHub de data Professor, et le fichier s'appelle Iris dot CSV, d'accord, et il utilisera le package carrot pour effectuer la division des données, en utilisant un ratio de 8020 à 0.8.

Ici, c'est 80% de division, qui ira dans l'index de formation, et ensuite nous utiliserons l'index de formation pour créer un ensemble de formation dans lequel il effectuera le tranchage du cadre de données Iris original, et ensuite le reste 20% ira à l'ensemble de test.

Donc, ce que nous allons faire ensuite, c'est que nous allons écrire l'ensemble de formation et l'ensemble de test dans les fichiers CSV, n'est-ce pas, car cela aiderait à remédier au mélange possible des données qui iront dans l'ensemble de formation et l'ensemble de test, donc cela permettra la reproductibilité dans le futur.

Donc, dans le futur, nous pouvons simplement lire le fichier training dot CSV, au lieu de effectuer à nouveau la division des données, n'est-ce pas.

Donc, ici, nous allons lire le fichier training dot CSV et lui donner le même nom, qui est le train set Canada, nous allons supprimer la première colonne, qui est le numéro d'index.

Et ensuite nous allons construire un modèle et assigner le modèle construit à l'objet de données modèle.

Et une fois qu'un modèle a été construit, nous allons l'enregistrer en tant que fichier RDS.

Donc, nous allons déployer le modèle dans le format RDS.

Donc, dans ce code de fonction de forêt aléatoire, nous spécifions que nous voulons prédire l'espèce de la fleur d'iris.

Et nous allons utiliser les quatre paramètres d'entrée et l'ensemble de données, nous utiliserons l'ensemble de formation pour faire le modèle et ensuite nous allons assigner une valeur d'entrée, qui est le paramètre de la forêt aléatoire à cinq Heinz red, et nous allons assigner le paramètre M try à être quatre, oui, et ensuite nous allons assigner une valeur vraie pour l'argument d'importance, d'accord, et donc ce que vous voulez faire, c'est exécuter tous ces blocs de code, donc vous pourriez simplement Ctrl A, sélectionner tout et ensuite Ctrl, entrer.

D'accord, et ensuite les données seront lues, et ensuite un modèle sera construit, et il sera enregistré en tant que model dot RDS.

D'accord, cela conclut le fichier model dot r, et ensuite nous allons le fermer.

Et ensuite nous allons ouvrir le deuxième fichier, qui est le app gnumeric dot r k.

Donc, jetons un coup d'œil.

Les premières lignes seront l'importation des bibliothèques nécessaires, qui seront la bibliothèque shiny, la data dot table, le package random forest, et ensuite nous allons lire le modèle que nous avons construit à l'étape précédente.

Et nous allons l'assigner à un objet modèle, oui.

Et comme dans la vidéo précédente, l'application web shiny contiendra trois composants.

Donc, le premier composant étant l'UI, et le deuxième composant étant le serveur.

Et le troisième composant étant la fonction shiny app, qui assemblera essentiellement l'UI et le serveur.

D'accord, donc jetons un coup d'œil à l'UI.

Et nous allons ouvrir l'application web et regarder en même temps.

Et pour la lisibilité du code, je vais simplement ajouter des entrées supplémentaires et une nouvelle ligne.

Donc, lorsque j'ouvre le navigateur web, simultanément, les valeurs ici ne seront pas cachées.

D'accord ? Enregistrez-le et retournez à l'application web.

D'accord, donc ici, le nom de cette application web s'appelle Iris predictor.

Et donc il est dans le panneau d'en-tête ici.

Donc, nous mettons le prédicteur iris, si vous voulez changer le nom, n'hésitez pas à le faire ici.

Et ensuite nous allons avoir le panneau de la barre latérale, qui est à gauche, et ensuite nous allons avoir le panneau de la barre principale, qui est à droite, donc comme toujours, la gauche ou le panneau de la barre latérale prendra les paramètres d'entrée, et ensuite en cliquant sur le bouton soumettre, qui est ici, il enverra les paramètres d'entrée à la fonction serveur, et le serveur utilisera ces paramètres d'entrée pour les alimenter dans le modèle prédictif, qui est le modèle de forêt aléatoire et faire une prédiction.

Et une fois que votre prédiction a été faite, la valeur de sortie résultante générée sera ensuite renvoyée dans le panneau principal ici.

Et ensuite les résultats seront affichés dans les données de tableau, qui vont se produire juste en dessous de ce message texte.

Donc, les données de tableau seront affichées ici, qui est la prédiction faite.

D'accord, donc dans les paramètres d'entrée, nous allons utiliser la balise HTML et à l'intérieur nous allons assigner une taille de l'en-tête à être h3, oui, et un nom sera les paramètres d'entrée ici.

Donc, montrant davantage la polyvalence du cadre d'application shiny.

Donc, notez que les s et l sont des lettres majuscules, et c'est l'ID de ce paramètre d'entrée sepal length, et il est sensible à la casse.

Donc, nous devons le taper exactement S est lorsque nous allons l'utiliser à l'étape suivante.

Donc, ce sera comme input dollar sign, et puis CBOE dot length.

Et puis ce sera le paramètre d'entrée, que la fonction serveur utilisera comme les données à alimenter dans le modèle de forêt aléatoire.

D'accord, et donc l'étiquette ici sera sepal length.

Et l'étiquette signifie ici, l'étiquette et la valeur est la valeur par défaut, qui est cinq et ici est cinq.

Donc, si vous changez la valeur par défaut à 5.1, et vous l'enregistrez, exécutez l'application à nouveau.

Donc, vous voyez que 5.1 sera mis à jour ici à la place de 5.0.

D'accord, donc la même chose sera pour la largeur du sépale, la longueur du pétale et la largeur du pétale, oui avec l'étiquette et avec la valeur, qui est la valeur par défaut ici.

Et puis le bloc de code suivant ici est la fonction action button.

Et ce sera le bouton soumettre.

Donc, il remplacera la fonction réactive dans laquelle, lorsqu'il n'y a pas de bouton Soumettre, chaque fois que nous modifions les nombres ici, une prédiction sera faite.

Donc, cela mettrait une charge lourde sur le serveur, car chaque fois que vous mettez à jour la valeur ici, une prédiction sera faite.

Donc, imaginez que vous mettez à jour les valeurs 10 fois, 20 fois et 20 modèles prédictifs seront créés.

Alors que dans une situation où vous avez le bouton soumettre, vous pouvez passer tout le temps ou autant de fois que vous en avez besoin pour mettre à jour les valeurs, n'est-ce pas ? Voyons si je suis allé à et puis j'ai changé d'avis, je veux qu'il soit 4.9.

Donc, faites cela 10 fois de plus.

Et donc le modèle de prédiction ne sera pas construit, n'est-ce pas.

Donc, il va attendre que vous cliquiez sur le bouton soumettre et ensuite la prédiction sera faite.

D'accord, donc cela sera plus économique du côté serveur.

Et aussi pour la familiarité, où nous cliquerions normalement sur un bouton afin d'initier le processus de prédiction.

D'accord, et puis le bloc de code suivant main panel sera ici.

Donc, dans l'étiquette de taxe h3 status output, ce sera cette partie.

Donc, notez que ce bloc de code est exactement le même que le bloc de code HTML.

Donc, je vous montre simplement la polyvalence de l'application web shiny.

Et vous pourriez utiliser l'une ou l'autre, d'accord, mais c'est la manière shiny de faire les choses, n'est-ce pas.

Donc, laissez-moi vous montrer en le mettant ici.

Et puis je vais commenter cela et mettre les paramètres APR ici et puis remplacer la valeur à l'intérieur.

D'accord, rechargez l'application, oui, et puis cela a l'air exactement pareil, n'est-ce pas.

Donc, vous pouvez le faire des deux manières, oui, et puis la boîte de texte suivante montrée ici vous dira que le serveur est prêt pour le calcul.

Donc, cela sera affiché lors du chargement de l'application web.

Et lors du clic sur le bouton soumettre, la valeur sera changée pour être le calcul complet.

D'accord, donc cela sera du côté serveur.

Donc, je vais vous montrer dans un instant.

D'accord, donc nous avons terminé avec le composant UI.

Et maintenant, passons au composant serveur.

Et donc ici, nous allons charger la fonction, d'accord, donc ce bloc de code ici sera les paramètres d'entrée, qui seront obtenus à partir du composant UI où l'utilisateur entrera les paramètres d'entrée et cliquera sur le bouton Soumettre.

Et en faisant cela, tous les paramètres d'entrée viendront comme montré dans ce bloc de code ici.

Et ce bloc de code générera essentiellement le fichier CSV d'entrée, qui sera lu dans l'objet de test et ensuite appliquera le modèle pour faire une prédiction sur cet objet de test.

Et une fois la prédiction faite, ce bloc de code data set input contiendra la prédiction et la valeur de prédiction sera insérée ici, à droite, et elle sera encapsulée par une variable de nom output table data et puis cette chose et puis le input dollar sign, et puis le output dollar sign table data sera envoyé au panneau principal dans l'UI pour être affiché.

Donc, c'est ici, à droite.

Donc, celui-ci viendra des données de tableau ici, données de tableau, à droite, ce qui est mis en évidence en bleu, et il viendra du tableau des résultats de prédiction, à droite, que nous utilisons la fonction render table ici, et les données de tableau input ici contiendront la prédiction qui provient de l'objet de données de sortie.

D'accord, donc laissez-moi aller spécifiquement ligne par ligne ici.

Donc, un cadre de données sera créé, et puis le nom sera le nom de la variable Heather name sur la première ligne, et puis les valeurs prendront et la valeur du paramètre d'entrée de l'UI.

Donc, input dollar sign, sepal length, sepal width, petal length, petal width viendront de la zone de texte d'entrée ici 5.1 3.6 1.4 2.2.

Donc, ces zones de texte seront input dollar sign, sepal length, sepal width, petal length, petal width, d'accord, et puis nous allons créer un cadre de données.

Et une fois que nous avons fait cela, nous allons l'écrire en tant que fichier input dot CSV.

Maintenant, nous allons le relire, et puis nous allons le mettre dans l'objet test, et puis nous allons créer un objet output et un cadre de données sera créé.

Et nous appliquons la fonction de prédiction afin de faire une prédiction en utilisant le modèle de forêt aléatoire sur les données de test d'entrée.

Et une fois la prédiction faite, nous allons également indiquer la probabilité en trois chiffres, d'accord, et une fois la prédiction faite, elle sera ensuite envoyée à cet objet de données de sortie et elle l'imprimera et elle représentera les entrées de l'ensemble de données, et cet ensemble de données d'entrée sera inséré dans la fonction render table, et un tableau sera généré pour vous montrer les résultats de prédiction de sortie affichés ici.

Oui.

D'accord.

Donc, c'est essentiellement tout pour ce prédicteur Iris sous forme numérique.

Donc, fermons cela et passons au suivant.

D'accord, donc maintenant nous allons procéder avec la version app slider.

Et avant de le faire, vous voulez nettoyer l'environnement de l'espace de travail.

Donc, cliquez sur le bouton balai.

Et puis après avoir fait cela, vous voulez cliquer sur app, slider dot r et puis Ctrl, a, et puis Ctrl, enter.

Oui, et puis l'application web sera chargée.

Donc, vous voyez que maintenant, au lieu de tap spots où nous mettons la valeur numérique, vous allez avoir un curseur, oui, et puis vous cliquez sur le paramètre d'entrée en glissant ici, et puis après être satisfait des valeurs d'entrée, vous cliquerez sur le bouton soumettre, et puis la prédiction sera faite.

Et comme toujours, cela a l'air exactement pareil, mais la seule différence est que les paramètres d'entrée auront la barre de curseur au lieu de la zone de texte.

D'accord, donc jetons un coup d'œil sous le capot.

Donc, quel nouveau code avons-nous ajouté à ce fichier, nous avons ajouté les lignes 17, 18 et 19.

Et puis nous avons également ajouté deux nouveaux arguments, qui sont le minimum et le maximum, à chacune des entrées.

Et nous avons également changé le nom de numeric input en slider input.

Et c'est essentiellement tout, nous avons juste changé quelques lignes de code et l'application web ressemblera à ceci.

Au lieu d'une zone de texte numérique, nous allons avoir une barre de curseur.

Donc, la valeur du minimum ici sera prise comme la fonction minimum et puis le train set dollar sign simple link, oui.

Donc, je n'ai pas à mettre manuellement la valeur minimale ou maximale, mais je vais le faire de manière programmatique.

Donc, je vais utiliser la fonction minimum et à l'intérieur de la fonction minimum en tant qu'argument, je vais dire, d'accord, je veux avoir l'objet train set.

Et je veux avoir la colonne simple link.

Et je veux savoir quelle est la valeur minimale, oui, ce sera comme ceci.

Donc, laissez-moi fermer cela, et je vais lire le fichier.

Donc, laissez-moi vous montrer à quoi cela ressemble.

Et si je lance le train set, cela ressemblera à ceci.

Et puis je vais lancer cette ligne et puis notez que la première colonne aura disparu, oui, je ne veux pas que l'index soit affiché.

Donc, je l'ai simplement supprimé.

Et puis quand je dis train set dollar sign sepal length, où ils obtiendront cela, donc ce seront les valeurs de la première colonne seulement.

Et en ajoutant la fonction minimum devant, je vais obtenir la valeur minimale.

Et si j'utilise la fonction maximum, je vais obtenir la valeur maximale de cette colonne.

Donc, le minimum est 4.3.

Et le maximum est 7.9.

Donc, au lieu de mettre les valeurs manuellement, 4.3 7.9, je vais le faire de manière programmatique, et ce sera tellement plus facile, n'est-ce pas ? Et puis je le mets ici.

Et c'est tout pour la modification du code et tout le reste fonctionne exactement de la même manière.

Et vous obtenez une nouvelle sensation pour l'application web et ce n'est pas si difficile.

D'accord, donc amusez-vous et faites-moi savoir quel type d'application web vous voulez que je crée ou les données d'entrée que vous voulez que j'utilise pour créer l'application web.

D'accord, donc aujourd'hui représente le cinquième épisode de la série des applications web dans notre.

Et aujourd'hui, nous allons couvrir comment vous pouvez développer une calculatrice d'IMC.

Donc, si vous vous demandez ce qu'est un IMC, eh bien, l'IMC signifie indice de masse corporelle, et il est calculé en divisant le poids en kilogrammes par la taille en mètres carrés.

Par exemple, si vous pesiez 70 kilogrammes et que vous mesuriez 170 centimètres, vous devriez d'abord convertir la taille en mètres.

Donc, 170 centimètres deviendraient 1,7 mètres.

Et selon l'équation, vous prendriez votre poids, qui est de 70 kilogrammes divisé par 1,7 mètre carré, d'accord, donc laissez-moi calculer cela.

Donc, 1,7 fois 1,7, serait 2,89.

Et si je pesais 70 kilogrammes, divisé par les tailles au carré, alors mon IMC serait de 24,2.

D'accord, donc jetons un coup d'œil à l'échelle de l'IMC chez les adultes.

Donc, si vous avez un IMC inférieur à 18,5, cela signifierait que vous êtes en sous-poids.

Si vous avez un IMC dans la plage de 18,5 et 24,9, cela signifie que vous avez un poids santé.

Et si votre IMC est entre 25 et 29,9, cela signifie que vous êtes en surpoids.

Et si vous avez un IMC supérieur à 30, alors vous êtes obèse.

D'accord, donc dans l'exemple précédent, un IMC de 24,2 signifierait que le poids est un poids santé.

Donc, sans plus attendre, commençons à développer notre application web IMC.

Donc, vous voulez d'abord aller sur le GitHub de Data Professor.

Et donc, cliquez sur le dossier code, trouvez shiny et cliquez sur le dossier shiny.

Et puis trouvez le 005 que BMI cliquez dessus.

Et puis vous voulez télécharger à la fois le about.md et le app dot r sur votre ordinateur.

Donc, pourquoi ne pas le faire, faites un clic droit sur le raw pour enregistrer le lien sous, car nous allons le télécharger dans un dossier BMI.

Nous l'enregistrons là.

Et puis téléchargez le deuxième fichier, faites un clic droit sur le lien raw, ajoutez-le en toute sécurité en tant que sauvegarde dans le dossier BMI.

D'accord, et maintenant nous devons télécharger le dossier.

D'accord, le voilà, vous avez deux fichiers à ce R et about.md.

Donc, jetons un rapide coup d'œil à ce que ce fichier ressemble.

Donc, comme vous le montrez, app dot r est le code R comprenant les trois composants majeurs, l'UI, l'interface utilisateur, le numéro deux est le serveur.

Et le numéro trois est la fonction de sortie qui fusionne à la fois l'UI et la fonction serveur.

Et dans le deuxième fichier, vous avez le about.md.

Donc, ceci est écrit en langage markdown.

Et il sera utilisé par le fichier app dot r.

Donc, nous allons voir cela dans un instant.

Donc, avant de plonger profondément dans le code R, jetons un coup d'œil à ce que l'application web ressemble.

Cliquez sur run app.

D'accord, donc voici une application web simple où vous pouvez mettre votre taille et votre poids, donc la taille sera en centimètres et le poids sera en kilogrammes.

Donc, la valeur minimale ici est 40 pour la taille, et 250 pour la valeur maximale, et pour le poids, la valeur minimale est 20.

Et la valeur maximale est 100.

Donc, veuillez noter que cette calculatrice d'IMC est développée pour les adultes et qu'elle n'est pas adaptée aux enfants.

Si vous voulez développer un IMC pour les enfants, alors nous devrons nous référer à ce deuxième lien ici.

D'accord, donc comme vous le remarquez, lorsque vous cliquez sur le lien à propos de la barre de navigation, il montre les informations dans la page À propos.

Donc, à l'origine, le code était écrit ici en langage markdown et ici dans le site web.

Il l'affiche comme une page web normale.

Donc, ici vous pouvez ajouter de la gras au texte, vous pouvez ajouter un exposant pour le faire ressortir comme une équation, vous pourriez ajouter une police italique, oui.

Donc, tout cela est dans le langage markdown, oui. Par exemple, si vous utilisez deux astérisques, cela signifie que les tests seront en gras.

Donc, cela signifie que vous devez utiliser deux astérisques avant et après le test, vous voulez que les deux soient en gras.

Et si vous utilisez le tag hash, cela signifie que vous allez utiliser le tag de niveau Heather, qui est le tag h4 en HTML.

Et si vous utilisez le symbole supérieur à ici, cela signifie qu'il va afficher cette barre gris clair à gauche.

Donc, vous savez que c'est une équation.

Et si vous utilisez un astérisque, alors cela signifie que le texte sera en forme Tillich, oui.

Et ici nous l'utilisons pour le hashtagging et donc il devient un en-tête.

Et puis nous faisons le calculateur d'IMC en forme d'Italie en utilisant l'astérisque avant et après, et même ajouter les liens vers le site web, oui.

Donc, les robinets que vous voulez transformer en lien, vous devez les mettre entre crochets et immédiatement après cela, vous devez mettre entre parenthèses l'URL de la page web.

Et donc ce format est comme une page web normale.

Et donc l'application web, et donc l'application web, est adaptée aux mobiles, et vous pouvez l'utiliser sur votre téléphone portable, d'accord, cela ressemblerait à ceci sur le téléphone.

Et si vous cliquez dessus, et vous obtenez l'IMC, oui, dans mon exemple précédent, une taille de 170 et un poids de 70, vous obtiendrez un IMC de 24.2 à 145.

Et parce que nous l'arrondissons, et donc nous obtenons 24.22.

D'accord, donc cette application web semble assez simple, d'accord.

Et donc, plongeons profondément dans le code.

D'accord, donc jetons un coup d'œil au code du fichier app dot r.

Donc, les deux premières lignes ici seront le chargement du package de la bibliothèque shiny et shiny themes.

Et ensuite, nous avons l'interface utilisateur.

Donc, à l'intérieur de l'optique UI, il y aura la fonction fluid page.

Et ici, nous allons définir que nous allons utiliser le thème shiny de united et d'abord exécuter l'application et regarder.

Donc, ici, la fonction nav bar page montre que nous allons utiliser le nom de cette barre de navigation pour être BMI calculator.

Et puis le panneau d'onglets aura le premier onglet de navigation ici pour être home.

D'accord, et à l'intérieur du panneau supérieur ici, nous allons utiliser le panneau de la barre latérale et le panneau principal.

Donc, comme d'habitude, le panneau de la barre latérale est ici à gauche, et à droite, dans la sortie de statut, nous allons avoir le panneau principal, oui, donc le panneau de la barre latérale contiendra les paramètres d'entrée, qui comprennent deux paramètres d'entrée, la taille et le poids, et nous utilisons une entrée de curseur, donc vous pouvez faire glisser la barre ici, et puis vous obtenez la valeur souhaitée, cliquez sur le bouton soumettre, et puis vous obtenez la valeur de l'IMC calculée.

D'accord, donc l'entrée du curseur ici est responsable de ce bouton curseur.

Et donc le nom de cette entrée de curseur s'appelle height ici dans l'étiquette height.

Et le premier sera l'ID de ces entrées de curseur spécifiques.

Et donc cette entrée de curseur a un ID de heights, notez le petit h et puis la deuxième entrée de curseur a une valeur de weights et notez le petit W et donc ces deux entrées de curseur seront ensuite utilisées à l'étape suivante, elles seront utilisées par la fonction serveur comme input dollar sign weights et input dollar sign heights afin de calculer l'IMC, d'accord, et puis la fonction action button sera le bouton rouge sur lequel vous cliquez pour initier le processus de calcul.

Et donc le panneau principal aura une balise h3 ici montrant les sorties de statut, d'accord, et puis la sortie de texte verbatim contiendra l'ID contents, qui provient de la sortie dans la fonction serveur.

Et dans la sortie de tableau est également de la sortie de la fonction serveur, elle est appelée table data.

Et ce sont les données de tableau contenant la valeur de l'IMC calculée.

Donc, laissez-moi résumer cela à nouveau.

Donc, ici, l'entrée du curseur, nous avons deux poids de hauteur et donc il sera appelé input dollar sign heights input dollar sign weights.

Et lorsque l'utilisateur fait glisser cette valeur, elle ajustera la valeur au paramètre de hauteur ou au paramètre de poids et la valeur input dollar sign height et la valeur input dollar sign weight iront ensuite à la fonction serveur.

Je vais vous le montrer maintenant, ici.

Donc, nous allons à la fonction serveur dans l'équation que nous allons créer puti BMI.

Donc, ici, nous prenons le input dollar sign weight, en le divisant par le input dollar sign height divisé par 100, oui, car nous voulons convertir les centimètres en mètres, donc nous devons diviser la valeur en centimètres par nos amis lus, et cela en fera une forme majeure.

Et puis nous allons multiplier la hauteur par elle-même afin d'obtenir la valeur de hauteur au carré.

Et puis nous allons diviser le poids par la hauteur afin d'obtenir l'IMC.

Et nous allons encapsuler la valeur de l'IMC dans un cadre de données afin de pouvoir l'afficher dans la sortie finale ici en dessous dans la sortie contents, il montrera que le serveur est prêt pour le calcul ou que le serveur a déjà terminé le calcul.

Donc, cela sera modifié par le bouton soumettre, le bouton rouge sur lequel nous avons cliqué ici.

Donc, lorsque nous ne cliquons pas sur le bouton, il dira que le serveur est prêt pour le calcul.

Mais en cliquant sur le bouton rouge, l'IMC sera calculé.

Et puis dans cette boîte de texte, le texte changera pour indiquer que le calcul est terminé et que les résultats de sortie suivants ici sont appelés output dollar sign table data.

Et à l'intérieur, nous allons utiliser la fonction render table.

Donc, les résultats de l'ensemble de données input seront la valeur de l'IMC calculée ici dans le print BMI.

Donc, laissez-moi résumer à nouveau, jetons un coup d'œil à l'application web à nouveau.

Donc, cette application web prendra deux paramètres d'entrée, la taille et le poids, et ils sont en unité centimètre et la taille et le poids seront appelés input dollar sign heights et input dollar sign weights.

Et en cliquant sur le bouton rouge, ils seront envoyés à la fonction serveur dans cette fonction de calculatrice d'IMC.

Donc, elle prendra ensuite les poids d'entrée et la hauteur d'entrée et effectuera le calcul et retournera la valeur de l'IMC.

Et puis nous mettons la valeur de l'IMC dans un cadre de données.

Et puis nous l'imprimons et les résultats de l'IMC imprimés font partie de la variable data set input.

Et cela est appelé dans la fonction render table de output dollar sign table data et output dollar sign table data ira au panneau principal ici dans le panneau principal pour être affiché dans la sortie de tableau.

Et cela ressemble à ceci ici.

Donc, vous voyez que c'est appelé BMI et puis nous avons la valeur de l'IMC juste en dessous, oui.

Et c'est tout ce qu'il y a à construire cette application web de calculatrice d'IMC.

Donc, vous pouvez jouer avec ce code.

Et vous pouvez changer la valeur par défaut, par exemple, la taille, vous pouvez la mettre à 180 et la valeur du poids, vous pourriez la mettre à 75, oui, et puis exécuter le code à nouveau.

Donc, la valeur par défaut devient alors mise à jour pour être 180 et 75.

Donc, disons que vous voulez mettre à jour la valeur maximale à 300, la valeur minimale à 50.

Et le poids, vous voulez le mettre à 30.

Et le maximum serait 120.

Et puis nous chargeons l'application et ici vous voyez les valeurs minimales et maximales mises à jour en conséquence.

Donc, vous voyez ici, si le poids est maintenu le même et que la taille augmente, alors l'IMC devient moins.

Mais si la taille diminue, alors l'IMC est élevé, oui, à cause de l'équation de l'IMC, où le poids est divisé par la taille au carré, d'accord, et donc vous pouvez jouer avec les valeurs existantes, en jouant avec le modèle.

Donc, disons que vous voulez changer le thème United pour qu'il devienne un Booléen.

Enregistrez-le, rechargez l'application, et voici, vous obtenez une application web de couleur différente.

Oui.

Donc, les types de thème peuvent être obtenus en regardant les sites web.

Vous pouvez Googler cela, Googler pour shiny themes, cliquer sur le cliquer sur le art studio.github.io slash shiny themes.

Donc, je vais fournir le lien dans la description ci-dessous.

Donc, vérifiez cela.

Dans cette vidéo, je vais vous montrer comment vous pouvez déployer une application web shiny.

Et sans plus attendre, nous commençons maintenant.

D'accord, donc la première chose que vous voulez faire est de vous rendre sur le GitHub de Data Professor.

Et vous voulez cliquer sur les dépôts, puis trouver et cliquer sur iris, notre Heroku.

Et donc tous les fichiers nécessaires pour déployer votre application se trouvent ici.

Donc, n'hésitez pas à cloner cela sur votre propre GitHub ou également vous pourriez télécharger l'intégralité du contenu du dossier ici en cliquant sur le code et ensuite télécharger le fichier zip.

Donc, jetons un coup d'œil ici.

Donc, vous allez voir que nous avons le UI dot r, qui est l'interface utilisateur.

Et nous avons aussi server dot r, qui est le composant côté serveur de l'application web.

Donc, essentiellement, notre application web shiny sera composée de deux composants, l'interface utilisateur et le composant serveur.

Et puis nous allons avoir l'ensemble de données d'entraînement et l'ensemble de données de test en tant que fichier CSV.

Et le modèle réel sera contenu dans le model dot RDS.

Et donc le modèle d'apprentissage automatique est enregistré en tant que model dot RDS.

Et il sera chargé dans l'application web lorsque nous l'exécuterons.

Et puis il y a deux fichiers r supplémentaires.

Jetons un coup d'œil.

Donc, le premier est in that dot r.

Et donc, jetons un coup d'œil ici.

Donc, il nous permettra d'installer les bibliothèques nécessaires.

Donc, nous allons installer le random forest et le data dot table.

Et le run dot r nous permettra d'exécuter le R shiny et d'assigner les ports appropriés.

D'accord.

Et donc, c'est tout ce qu'il y a à avoir les composants nécessaires pour déployer votre application web shiny.

Donc, dirigeons-nous vers Hiroko.

Et donc, vous voulez cliquer sur new create new app.

Et puis vous voulez donner un nom à l'application.

Donc, laissez-moi l'appeler VP, Iris, r create app.

Et puis je veux me connecter à GitHub.

Et je vais trouver Iris ou he Roku.

Donc, dans votre cas, vous voulez trouver votre propre GitHub et vous voulez trouver votre propre RSR he Roku et ensuite vous connecter.

Et puis c'est très important, car vous voulez cliquer sur les paramètres.

Et afin d'avoir le support pour notre, vous allez avoir besoin d'ajouter le custom build pack.

Et donc, vous voulez cliquer sur Add build pack.

Et vous allez remarquer qu'il y a certains build packs officiellement supportés.

Donc, par défaut, vous allez avoir Python, n'est-ce pas, et vous allez avoir d'autres comme PHP, Ruby, Java, node j s.

Et donc pour notre R, nous allons utiliser un tiers.

Et le lien tiers vers le build pack pour R est donné ici.

Donc, je vais vous fournir ce lien dans la description de cette vidéo.

Donc, vous voulez copier cela et puis le mettre ici aussi.

Et puis cliquez sur save changes.

Et puis vous allez voir qu'il a été ajouté avec succès ici.

Maintenant, vous voulez retourner à deploy, faites défiler vers le bas et vous voulez cliquer sur deploy branch dans le déploiement manuel.

Donc, à ce stade, vous voulez faire une pause, prendre une tasse de café et attendre que l'application web se déploie.

Donc, nous allons voir le journal de ce qui se passe ici.

Donc, initialement, il installe la version 3.6, point trois ici.

Et il télécharge le bill pack directement depuis Amazon Web Service, et aussi avoir shiny.

Oui, donc il installe la bibliothèque data dot table.

Et maintenant, il construit l'environnement.

Donc, cette application web a déjà été construite dans une vidéo précédente.

Donc, le lien vers cette vidéo sera fourni dans la description ci-dessous.

Et en attendant, peut-être que je pourrais vous montrer que shiny et c'est le numéro quatre Iris predictor.

Et donc vous allez remarquer que nous avons utilisé le testing et le training et pour l'application, nous avons divisé les composants de l'UI et du serveur dans ces fichiers séparés.

D'accord, et donc il compresse l'environnement de 499 mégaoctets à 121 mégaoctets.

Bien que les packages R occupent 121 mégaoctets, d'accord, donc il l'a compressé à 152.

Et il déploie l'application web sur dp c'est Iris dash r dot e Roku app.com.

Et donc dans un instant, vous allez voir un lien pour visualiser les sites web déployés.

D'accord, terminé.

Et donc il dit que votre application a été déployée avec succès.

Cliquons dessus.

D'accord, donc il dit ici que le serveur est prêt pour un calcul.

Soumettons. D'accord, donc les prédictions semblent fonctionner et il est prédit d'être setosa avec une probabilité de 100%.

k, ce prédicteur est pseudoscience.

Eh bien, même chose qu'elle nous a dit et maintenant il a été prédit d'être virginica.

100% virginica.

Merci d'avoir regardé jusqu'à la fin de cette vidéo, et j'espère que cette vidéo vous a été utile.

Et pour plus de tutoriels en science des données, bioinformatique, ainsi que Python et nos tutoriels de codage, veuillez consulter ma chaîne YouTube à l'adresse data professor et aussi ma nouvelle et deuxième chaîne YouTube decoding professor.

Et vous pouvez également me trouver sur la plateforme medium où je blogue sur la science des données ainsi que sur les tutoriels Python.

Et enfin, mais non des moindres, je voudrais remercier Free Code Camp pour cette collaboration géniale.

Et s'il vous plaît, n'oubliez pas d'appuyer sur le bouton like, de vous abonner si vous ne l'avez pas déjà fait.

Et jusqu'à la prochaine fois, la meilleure façon d'apprendre la science des données est de faire de la science des données, et s'il vous plaît, profitez du voyage.