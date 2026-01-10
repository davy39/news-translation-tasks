---
title: Comment créer une extension Chrome
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-05-27T14:35:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chrome-extension
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/ext.png
tags:
- name: chrome extension
  slug: chrome-extension
- name: youtube
  slug: youtube
seo_title: Comment créer une extension Chrome
seo_desc: 'A chrome extension is a software program that is designed to run within
  the Google Chrome web browser.

  Extensions can add a variety of functionality to the browser, including providing
  tools for web development, adding features to the browser interfa...'
---

Une extension Chrome est un programme logiciel conçu pour fonctionner dans le navigateur web Google Chrome.

Les extensions peuvent ajouter diverses fonctionnalités au navigateur, y compris des outils pour le développement web, l'ajout de fonctionnalités à l'interface du navigateur et la modification du comportement des pages web.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer votre propre extension Chrome avec JavaScript.

À la fin de ce cours, vous comprendrez comment créer une extension Chrome moderne. Vous apprendrez à créer l'extension en utilisant la nouvelle itération de la plateforme d'extensions web, appelée Manifest V3.

Pour suivre ce cours, il est préférable d'avoir une compréhension de base de JavaScript et de la manipulation du DOM.

Raman Hundal a créé ce cours. Raman est un excellent instructeur et il travaille pour Pieces.app. Pieces.app a fourni une subvention qui a rendu ce cours possible, mais vous n'avez pas besoin d'utiliser leur extension pour suivre le cours.

L'extension que vous allez créer dans ce cours est un marque-page YouTube. Elle permettra d'afficher une icône sur le lecteur vidéo chaque fois que vous naviguez vers une page vidéo YouTube, vous permettant de marquer un timestamp particulier sur la vidéo.

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=0n809nd4Zu4) (1 heure de visionnage).

%[https://www.youtube.com/watch?v=0n809nd4Zu4]

### Transcription

(générée automatiquement)

Si vous voulez créer votre propre extension Chrome, vous êtes au bon endroit.

Dans ce cours, Rahman vous apprendra à créer une extension Chrome en utilisant la nouvelle itération de la plateforme d'extensions web, qui s'appelle Manifest v3.

Rahman est un excellent instructeur.

Et il travaille pour Pieces.app, qui a fourni une subvention qui a rendu ce cours possible, mais vous n'avez pas besoin d'utiliser leur extension pour suivre le cours. Partagez dans les commentaires quel type d'extension Chrome vous voulez créer.

Maintenant, la raison pour laquelle je veux enseigner ce sujet particulier est que j'ai créé deux extensions web dans ma carrière.

La première était pour une entreprise précédente, où mon extension a généré une quantité significative de revenus pour l'entreprise.

Et la seconde pour mon entreprise actuelle, Pieces, où nos extensions web jouent un rôle critique dans notre pile de produits et aident les développeurs du monde entier à augmenter leur productivité.

Je vais utiliser les extensions web et les intégrations de Pieces assez souvent dans cette vidéo.

Donc, si vous êtes intéressé à télécharger un assistant de codage IA qui vous aide à sauvegarder et réutiliser des extraits de code, convertir des captures d'écran en code, et plus encore, allez-y et téléchargez Pieces dans la description.

Et vous pouvez tout à fait suivre le cours.

Donc, pendant mon parcours en tant que développeur d'extensions Chrome, j'ai souvent remarqué que les tutoriels et les réponses StackOverflow utilisaient des versions obsolètes de la plateforme d'extensions web.

Mon espoir pour vous après avoir regardé cette vidéo est que vous ayez une ressource pour créer une extension Chrome moderne, et que vous compreniez la différence entre la nouvelle version de la plateforme d'extensions web Manifest v3 et les versions plus anciennes.

Maintenant, avant de commencer, il y aura trois prérequis pour ce cours, le premier est obligatoire, et c'est que vous ayez une compréhension de base de JavaScript et de la manipulation du DOM.

Le second est optionnel.

Si vous voulez suivre cette vidéo et coder avec moi, vous pouvez aller à la description ci-dessous, je vais avoir un lien vers mon dépôt GitHub, allez-y et clonez-le et vous pourrez suivre le cours.

Le troisième est également optionnel.

Si vous voulez vraiment suivre le cours, vous pouvez aller sur Pieces.app et installer une intégration IDE Pieces ainsi que l'extension web Pieces, et vous pourrez utiliser Pieces exactement comme je le fais dans cette vidéo.

Avec cela, commençons.

Donc, comme je l'ai mentionné auparavant, l'extension que nous allons créer est un marque-page YouTube.

En gros, chaque fois que vous naviguez vers une page vidéo YouTube, une icône apparaîtra sur votre lecteur vidéo YouTube pour vous permettre de marquer un timestamp particulier sur n'importe quelle vidéo.

Donc, laissez-moi vous montrer comment cela va fonctionner.

Si vous êtes sur une page vidéo YouTube, vous allez voir cet élément en bas à droite, vous pouvez cliquer dessus.

Et si vous naviguez vers l'icône de votre extension Chrome en haut à droite, j'ai épinglé, donc elle s'affiche dans la barre d'outils, vous allez voir un nouveau timestamp déjà ajouté un timestamp pour 15 minutes, j'en ai ajouté un avec une heure 18.

Je peux supprimer celui-ci parce que je viens de décider que je ne le veux pas.

Et notre extension va nous donner cette capacité à le faire.

Maintenant, si je veux revenir à mon timestamp de 15 minutes, vous pouvez cliquer sur le bouton de lecture.

Et il revient directement à ce timestamp particulier.

Je peux aussi supprimer celui-ci.

Et lorsqu'il n'y a pas de marque-pages à afficher, il va dire qu'il n'y a pas de marque-pages à afficher.

Maintenant, nous allons en ajouter un, juste pour en avoir un sur cette vidéo, et je peux vous montrer comment fonctionne le stockage.

Je vais naviguer vers une nouvelle vidéo.

Et dans cette vidéo, nous n'avons pas de marque-pages.

Donc, il dit qu'il n'y a pas de marque-pages à afficher.

Mais si nous retournons à notre vidéo précédente où nous avons sauvegardé un marque-page, il va charger ce marque-page précédent.

Maintenant, la dernière chose est que si vous naviguez vers une page qui n'est pas une vidéo YouTube, il va dire que ce n'est pas une page vidéo YouTube dans l'interface utilisateur de l'extension.

Et c'est essentiellement toutes les capacités de cette extension Chrome que nous allons développer ici, il y aura beaucoup plus que vous pourrez faire par vous-même ensuite.

Maintenant, je veux aussi mentionner la raison pour laquelle nous travaillons sur la création de cette extension en particulier, c'est parce qu'elle va vous montrer toutes les parties majeures de la création d'une extension Chrome, elle va vous montrer comment travailler avec un script de contenu pour manipuler le DOM.

Elle va vous montrer comment créer une interface utilisateur pour votre extension.

Et elle va vous montrer comment utiliser les service workers comme scripts de fond, ce qui est une partie majeure du passage de manifest v2 à manifest v3.

Et pour commencer à travailler sur l'extension.

Une fois que vous avez cloné mon dépôt, vous pouvez cliquer sur l'icône de puzzle dans votre navigateur Chrome en haut à droite, cliquer sur Gérer les extensions.

Je vais supprimer mon extension pour vous montrer comment elle fonctionne.

Et vous allez voir cette option de mode développeur en haut à droite, activez-la pour qu'elle soit activée, cliquez sur Charger l'extension décompressée, puis allez dans le dépôt que vous avez cloné avec le code de base.

Chargez-le.

Et nous allons voir notre extension ici.

Si nous cliquons sur cette icône de puzzle et l'épinglons.

Ce que nous allons voir est cette interface utilisateur de base, elle va simplement dire vos marque-pages pour cette vidéo sans marque-pages, et elle va simplement s'afficher partout.

C'est le message par défaut dans le code de base que j'ai fourni et le code de base contiendra également tous les fichiers dont vous avez besoin pour suivre le cours.

Le meilleur endroit pour commencer à créer notre extension est le fichier manifest.json.

Ce fichier est un fichier JSON où nous pouvons spécifier quelle version de la plateforme d'extensions nous allons utiliser, parmi d'autres informations qui serviront de valeurs par défaut pour le chargement de nos extensions.

De plus, chaque extension que vous souhaitez créer, qu'il s'agisse de Safari, Mozilla ou toute extension basée sur Chromium, aura besoin d'un fichier manifest.json.

Et c'est probablement le fichier le plus important de votre extension, car elle ne fonctionnera tout simplement pas sans lui.

Dans notre code de base, nous avons déjà ajouté le fichier manifest.json, donc nous n'avons pas besoin de passer trop de temps à l'écrire, je pense qu'il serait particulièrement utile si je soulignais simplement certaines des choses que vous devez noter, au cas où vous créez votre propre extension.

Donc, examinons cela, comme vous vous en doutez, il y a un nom, un numéro de version et une description.

Et, en gros, le numéro de version va s'afficher lorsque vous chargez l'extension, le nom que vous voyez sera également le nom de l'extension lorsque vous la chargez.

Et la description est assez explicite.

C'est simplement une description de ce que fait l'extension.

Maintenant, les choses deviennent plus intéressantes avec les permissions.

Les permissions seront différentes selon l'extension Chrome que vous construisez.

Pour cette extension particulière, nous allons demander deux permissions, qui seront la permission d'utiliser l'API Chrome.storage et l'API Chrome.tabs.

L'API Chrome.storage est utilisée pour stocker des choses dans le navigateur de l'utilisateur pour l'extension.

Et la deuxième permission, qui est l'API Chrome.tabs, est ce qui nous aide à accéder au système d'onglets de notre navigateur.

Ainsi, nous pouvons lire l'onglet pour l'extension.

Cela va essentiellement nous aider à identifier quel onglet du navigateur l'utilisateur utilise actuellement, et récupérer l'URL pour voir s'il est sur une page vidéo YouTube pour notre extension.

Maintenant, les permissions d'hôte vous donnent simplement la capacité d'envoyer des requêtes à certains noms d'hôte.

Notre extension ne traite qu'avec les pages YouTube.

Donc, j'ai écrit un motif de correspondance ici juste pour YouTube.

Le service worker, comme je l'ai mentionné auparavant, il y a un grand changement entre les extensions v2 et v3.

Et l'un des grands changements est l'utilisation d'un service worker.

Comme vous pouvez le voir ici, l'autre est la capacité à utiliser des promesses.

Mais concentrons-nous simplement sur les service workers.

Pour l'instant.

Les service workers sont simplement un fichier JavaScript qui s'exécute séparément du thread principal du navigateur.

Cela signifie que votre service worker n'aurait pas accès au contenu d'une page web, puisqu'il est séparé des processus principaux.

Cependant, votre service worker a la capacité de communiquer avec votre extension en utilisant le système de messagerie des extensions, que nous allons voir et utiliser dans notre extension de marque-pages.

La prochaine chose que je veux souligner est les scripts de contenu.

Les scripts de contenu sont simplement des fichiers qui s'exécutent dans le contexte des pages web sur lesquelles nous nous trouvons.

Nous allons utiliser cela pour manipuler le DOM de notre page web que notre extension regarde.

Et ici, nous spécifions simplement que notre script de contenu est représenté par notre fichier content script JS.

Comme vous pouvez le voir, avec le JS : content script.js, la dernière chose que je veux souligner est le fichier pop-up.html ici, sous pop-up par défaut, cela spécifie simplement quel fichier est servi comme notre interface utilisateur.

Dans notre cas, nous avons spécifié le fichier pop-up.html, et dans ce fichier, nous spécifions que le fichier correspondant qui l'aide avec son interactivité est un fichier pop-up.js.

Avec tout cela, commençons à coder l'extension réelle.

Nous allons enfin commencer à écrire du code pour faire fonctionner notre extension.

Pour même tester l'extension, nous devons ajouter le bouton du lecteur YouTube qui nous permettra de sauvegarder des marque-pages avec des timestamps.

Donc, pour ajouter un bouton sur le lecteur vidéo YouTube, nous devons manipuler le DOM de la page web sur laquelle nous nous trouvons.

Cela signifie que nous devons écrire notre logique dans notre fichier de script de contenu, qui fonctionne dans le contexte de la page web, comme je l'ai mentionné auparavant, alors allons-y et ajoutons du code à notre fichier de script de contenu.

Nous allons ajouter les variables suivantes : YouTube, left, controls, et YouTube player one sera pour accéder au lecteur YouTube, one sera pour accéder aux contrôles.

Et cela nous permettra de manipuler chacun de ceux-ci.

Mais avant de continuer à écrire la logique pour faire la manipulation du DOM dans le contexte de la bande, nous devons aussi penser à la façon dont notre extension va savoir quand nous avons navigué vers une nouvelle page web.

Et nous devons savoir cela pour que le script de contenu sache exécuter la logique pour ajouter l'icône plus pour ajouter des marque-pages pour notre extension.

Allons-y et ouvrons notre fichier background.js maintenant.

Et ce que nous voulons faire ici, c'est écouter les mises à jour dans notre système d'onglets et trouver l'onglet le plus récent ou l'onglet sur lequel nous nous trouvons actuellement et voir s'il s'agit d'une page YouTube.

Donc, nous allons avoir un écouteur, qui va écouter les onglets.

Et si vous vous souvenez, nous avons obtenu les permissions d'accéder à l'API Chrome tabs.

Et nous allons écouter une mise à jour des onglets.

Les paramètres qui nous sont donnés sont un ID d'onglet et un onglet.

Ce que nous allons faire à partir de là, c'est voir s'il y a une URL d'onglet, et s'il y a un onglet Euro.

Voyons si cet Euro inclut youtube.com/watch.

La façon dont j'ai pensé à cela est que si vous regardez notre vidéo YouTube, chaque vidéo individuelle a YouTube slash watch.

Et nous voulons simplement nous assurer que nous sommes sur une page qui a cela spécifiquement comme URL, puis ce que nous voulons faire est de définir nos paramètres de requête.

Et nous allons utiliser les paramètres de requête comme identifiant unique pour chaque vidéo.

Ainsi, nous pouvons le récupérer depuis le stockage, vous verrez ce que je veux dire dans une seconde, et je vous montrerai.

Donc, nous allons faire cela en utilisant la méthode JavaScript split.

Ce que cela signifie, c'est qu'après ce point d'interrogation du paramètre de requête, nous allons récupérer cette valeur.

Et cela va être notre valeur vidéo unique ici, juste après le signe égal.

Et chaque vidéo sur YouTube a une valeur différente ici.

Donc, c'est une clé assez unique qui nous aidera à stocker les vidéos de manière unique également dans notre stockage, et c'est cohérent.

Donc, nous allons ajouter vos paramètres d'URL.

Et ce n'est qu'une interface pour travailler avec les URL, les paramètres de recherche d'URL.

Et la dernière chose que nous voulons faire est qu'il y a un système de messagerie qui se produit entre l'extension, nous allons envoyer un message à notre script de contenu qui dit essentiellement qu'une nouvelle vidéo est chargée.

Et c'est l'ID de la vidéo, et l'ID de la vidéo étant cette valeur vidéo unique que nous avons vue dans l'URL sur YouTube.

Et cette utilisation de l'envoi de message avec l'ID de l'onglet que je fais ici est directement tirée de la documentation.

L'envoi de message prend un ID d'onglet, il prend un objet unique.

Donc, maintenant, je vais taper le type.

Et c'est un type d'événement, c'est un nouvel événement vidéo.

Et puis une valeur d'ID de vidéo, qui va être l'URL, les paramètres, le point get v.

Donc, si nous faisons URL point get D, il va récupérer cela ici.

Et c'est essentiellement le code pour que l'envoi de message prenne un ID d'onglet, il prend un objet et puis il peut aussi prendre une fonction de rappel.

Cet objet ici n'a pas besoin d'être de type ou d'ID vidéo, il pourrait aussi être quelque chose d'aléatoire, comme je pourrais littéralement passer cela et le script de contenu aura accès à aléatoire, et puis à la chaîne aléatoire.

Dans notre cas, la seule chose qui est applicable est le type de l'événement et puis l'ID de la vidéo, dont le script de contenu a besoin.

Maintenant, dans notre script de contenu, nous allons ajouter un écouteur qui va écouter tous ces messages entrants, nous devons être capables d'écouter ce message background.js.

Donc, pour faire cela, nous allons finir par écrire le code suivant pour ajouter cet écouteur, donc nous allons dire on message add listener.

Et cela va accepter trois paramètres.

Donc, un objet, un expéditeur et une réponse.

Et la réponse est, lorsqu'un message est envoyé au script de contenu, nous pouvons aussi envoyer une réponse en retour d'où vient le message.

Donc, je vais déstructurer ces valeurs que nous recevons et si vous vous souvenez, la façon dont je déstructure le type de valeur vidéo ID est essentiellement que nous recevons un vidéo ID ici.

Plus tard, nous allons récupérer une valeur aussi, et je déstructure simplement.

Donc, chacun de ceux-ci est sa propre variable.

Donc, c'est un si le type est égal à nouveau, donc si le type d'événement est nouvelle vidéo chargée, que nous recevons du fichier background.js, nous voulons être capables de définir la vidéo actuelle, qui sera une variable globale dans le script de contenu comme l'ID de la vidéo, et puis nous voulons appeler une fonction pour gérer toutes les actions avec une nouvelle vidéo.

Donc, nous allons appeler une fonction de nouvelle vidéo chargée.

Et allons-y et définissons la vidéo actuelle comme une variable de niveau supérieur.

Et ce sera juste une chaîne vide.

Mais elle sera définie comme la chaîne définie à partir du fichier background.js, une fois le message reçu à cette extrémité, allons-y et voyons si cela fonctionne du tout.

Je vais simplement faire un console.log de vos paramètres.

Je vais lui donner un rechargement.

Ouvrez cela, inspectons-le.

Et nous avons des paramètres de recherche d'URL.

Donc, nous savons que nous obtenons nos paramètres de recherche d'URL maintenant.

Super.

Donc, jusqu'à présent, les choses ont l'air bonnes.

Maintenant, ce que nous voulons faire à partir de là est de créer cette fonction de nouvelle vidéo chargée.

Et après avoir créé cette fonction et toutes les fonctionnalités qui l'entourent, nous devrions voir le bouton du lecteur YouTube sur la vidéo YouTube.

Donc, allons-y et faisons cela.

Donc, ce que nous allons faire est de créer cette fonction que nous avons ici appelée New Video loaded.

Et ce que nous voulons probablement faire est de vérifier si un bouton de marque-page existe déjà, je connais le nom de la classe que cet élément a, il s'appelle Bookmark button parce que j'ai écrit le code CSS qui va styliser cette extension entière.

Donc, vous pourriez simplement copier cette partie ici.

Mais ce n'est que du DOM natif, des méthodes JavaScript que nous pouvons utiliser.

C'est en fait MB par nom de classe.

Et il va retourner une collection HTML.

Donc, ce que nous allons faire est de récupérer le premier élément qui correspond à ce nom de classe, bookmark button.

Et il va simplement exister sur chaque page vidéo YouTube.

Donc, si nous voulons tester cela, nous pourrions simplement dire console dot log bookmark exists.

Et rechargeons cette page et inspectons-la.

En fait, rechargeons aussi notre extension.

Rechargeons cette page, inspectons, nous allons probablement obtenir undefined, c'est exactement ce à quoi je m'attendais.

Parce que nous n'avons pas encore de logique entourant le bouton Bookmark.

Et aussi, nous ne définissons même pas de bouton Bookmark pour l'instant.

Donc, si le bouton Bookmark existait, nous obtiendrions true, il existe, mais nous obtenons undefined pour l'instant.

Donc, ce que nous voulons faire si nous obtenons cette valeur undefined ou false qu'un bouton Bookmark n'existe pas, c'est ajouter une logique pour dire, hé, ajoutons ce bouton Bookmark à n'importe quel lecteur YouTube.

Donc, nous allons créer un élément image.

C'est l'image que nous cliquons pour les boutons Bookmark.

En tant que partie, nous allons ajouter quelques attributs.

La première chose que nous allons vouloir faire est de tirer l'image que nous utilisons, qui est notre assets slash bookmark.

PNG, vous avez déjà cela si vous suivez avec le code de base.

La deuxième chose que nous voulons faire est d'ajouter une classe.

Et la façon dont nous allons ajouter cette classe est de la rendre assez dynamique ici.

Donc, nous allons ajouter une classe YouTube button avec un espace et puis nous allons ajouter une classe bookmark button entre guillemets.

Et c'est encore une fois, juste un peu de style que j'ai et dont vous n'avez pas besoin de vous soucier pour l'instant.

Et la dernière chose que nous voulons faire est de faire en sorte que, au survol, un titre s'affiche.

Donc, nous allons simplement dire que le titre est cliquez pour marquer le timestamp actuel.

Et c'est juste une question d'interface utilisateur.

Vous verrez cela dans un instant.

Ensuite, ce que nous voulons montrer, c'est une façon de récupérer les contrôles YouTube.

Donc, ce sont les contrôles YouTube ici, nous voulons être capables de récupérer ces contrôles de gauche, afin que nous puissions ajouter un bouton de marque-page ici.

Donc, allons-y et découvrons comment faire cela.

Je sais déjà comment faire cela.

Donc, je vais vous montrer comment cela fonctionne.

Vous pouvez inspecter les éléments ici et trouver quels éléments ils sont exactement.

Mais, en gros, nous allons utiliser des méthodes JavaScript natives comme nous l'avons fait précédemment pour récupérer ces contrôles et insérer notre bouton.

Si je fais document dot get elements by class name.

Et que je récupère YouTube left controls, nous devrions obtenir un élément en retour, qui va être cette div class ici.

Et vous pouvez voir qu'elle nous donne tous les contrôles de gauche ici, où nous allons ajouter notre bouton.

Et la deuxième chose que nous allons vouloir faire est de récupérer le lecteur YouTube également.

Et c'est l'une des variables globales que nous avons définies dans notre script de contenu.

Et nous pouvons aussi le faire en écrivant document dot get elements by class name.

Et puis il y a cette classe video stream.

Et nous allons récupérer celle à l'index zéro.

Et elle récupère tout le composant YouTube là.

Donc, maintenant nous connaissons les deux éléments dans le DOM que nous devons manipuler.

Mais définissons ces éléments.

Tout d'abord, nous allons faire exactement ce que nous avons vu dans notre contenu là-bas.

Document get, en fait, je vais simplement revenir en arrière et copier ces éléments, c'est beaucoup plus facile, donc ne faites pas d'erreur.

Et puis le second sera YouTube player.

Revenez en arrière et copiez cela.

D'accord, donc après cela, ce que nous allons vouloir faire est d'ajouter ce bouton de marque-page et nous avons récupéré les contrôles, vous avez vu cette rangée dans le lecteur, nous voulons l'ajouter à cette rangée.

Donc, nous allons taper YouTube left controls pour obtenir ces contrôles de gauche que nous avons stockés dans une variable.

Et pour utiliser cette méthode JavaScript native que nous pouvons utiliser appelée append child, qui va ajouter cet élément de marque-page à l'intérieur de cette rangée.

Et puis la deuxième chose que nous allons vouloir faire est probablement ajouter un écouteur pour écouter les clics sur notre icône.

Donc, il y a une correction que je veux apporter à cette partie de la vidéo, avant de continuer, elle sera très importante pour que votre extension fonctionne correctement.

Et ce n'est qu'une ligne de code, mais elle va faire une grande différence.

Je vais aussi expliquer un concept important des extensions Chrome que j'ai négligé en écrivant cela, qui est que dans notre fichier manifest.json, nous avons un motif de correspondance pour notre script de contenu.

Et, en gros, le motif de correspondance que nous avons actuellement vérifie si une vidéo youtube.com est chargée.

Et si c'est le cas, nous injectons notre script de contenu dans le contexte de cette page web.

Donc, en gros, ce que cela signifie, c'est que chaque fois qu'une page youtube.com apparaît, nous exécutons une série de logiques en utilisant notre script de contenu.

Mais le problème en ce moment est que notre fichier background.js nous dit quand une nouvelle vidéo est chargée.

Et l'écouteur d'événements que nous utilisons est on updated, qui vérifie simplement si cette URL est mise à jour.

Si vous actualisez cette page, l'URL n'est pas mise à jour.

Donc, ce bouton ne va pas apparaître.

Et si vous continuez à coder sans cette correction ici, vous allez voir certains cas limites que vous n'aimerez peut-être pas.

Donc, allons-y et corrigeons cela, nous allons faire une correction super simple.

Ce n'est pas la meilleure correction au monde, mais elle va résoudre le problème ici.

Nous allons simplement appeler une nouvelle vidéo chargée chaque fois que notre script de contenu correspond à youtube.com.

Et ce que cela va faire, c'est appeler cette fonction de nouvelle vidéo chargée chaque fois que nous atteignons ce motif de correspondance.

L'inconvénient de cela est que maintenant, si le script de fond le voit comme une nouvelle vidéo en utilisant l'écouteur d'événements on updated, et qu'il y a une condition que le script de contenu est injecté, nous allons frapper ou appeler cette fonction de nouvelle vidéo chargée deux fois, vous pouvez corriger cela assez facilement en ajoutant simplement une conditionnelle pour vous assurer que cela n'arrive pas.

Mais pour m'assurer que tout le monde peut suivre cette correction, je ne vais pas le faire ici.

Et nous allons simplement insérer cette seule ligne de code appelant la fonction de nouvelle vidéo chargée.

Heureusement, la seule chose que notre fonction de nouvelle vidéo chargée fait est d'ajouter le bouton de marque-page au lecteur YouTube.

Donc, il n'y aura pas d'implications négatives à l'appeler deux fois.

Puisque nous avons une condition qui vérifie si le bouton est déjà sur le lecteur.

Ce n'est simplement pas l'implémentation la plus efficace, ce qui est bien pour le bien de ce tutoriel.

Avec cela, continuons avec le reste de la vidéo.

Nous y voilà, nous avons le bouton juste là.

Mais pour l'instant, si nous cliquons sur le bouton, il ne fait rien.

Et il y a une raison à cela.

La raison est que nous n'avons aucun écouteur d'événements qui écoute le clic sur ce bouton particulier.

Allons-y et ajoutons le code pour cela.

Donc, ce que nous allons faire est d'ajouter un écouteur d'événements pour écouter un clic sur le bouton.

Et nous allons littéralement utiliser la méthode add event listener, écouter un clic, et puis appeler une fonction appelée add new bookmark event handler.

Et c'est une fonction que nous n'avons pas encore codée.

Donc, pour faire fonctionner cette fonction, nous allons devoir faire ce qui suit.

Nous allons probablement devoir déterminer le timestamp de la vidéo au moment où quelqu'un appuie sur le bouton.

Cela va essentiellement nous aider à déterminer ce que notre marque-page doit être enregistré comme dans le stockage selon son timestamp.

Donc, comment allons-nous faire cela ? Comment allons-nous déterminer le timestamp de la vidéo YouTube.

Encore une fois, YouTube rend cela assez accessible, il peut être trouvé comme un attribut.

Donc, ce que nous allons vouloir faire est de récupérer le lecteur YouTube.

Et nous avons déjà une variable globale qui l'a.

Mais je vais simplement le récupérer à nouveau.

Donc, nous pouvons voir comment faire cela dans la console, je vais créer une variable YouTube player dans notre console.

D'accord, maintenant nous l'avons sauvegardé.

Et puis sur YouTube player, il y aura une propriété appelée current time.

Et elle va nous donner le temps actuel en secondes.

Et afin de sauvegarder notre marque-page, selon les heures, minutes, secondes, nous allons probablement aussi devoir créer une fonction qui convertit les secondes en un temps standard tel qu'il est affiché sur YouTube.

Donc, allons-y et commençons par toutes ces choses.

Nous allons ajouter la fonction, add new bookmark event handler.

Et nous allons utiliser la propriété exacte que nous avons vue dans notre console, YouTube player dot current time, qui va nous donner le temps actuel.

Et nous allons dire d'accord, maintenant, cela n'est appelé que lorsqu'un nouveau marque-page est créé.

Donc, créons une nouvelle variable de marque-page.

Et cela va être un objet qui a le temps du marque-page et une description.

Et la description va simplement finir par être le titre qui va être affiché dans l'extension Chrome.

Donc, ce sera une description dynamique et skins un marque-page à l'heure actuelle.

Cependant, le problème est que cela est en secondes, comme nous l'avons dit auparavant, donc nous allons devoir convertir cela.

Donc, nous allons utiliser une fonction appelée get time.

Je vais simplement l'insérer en utilisant des morceaux.

Donc, ce que je vais faire, c'est aller à cette fonction de temps ici.

Insérer un extrait.

Et la voilà.

Donc, maintenant je suis capable de convertir mes secondes en temps.

Et puis la dernière chose que je veux faire ici est de le synchroniser avec Chrome Storage.

Et ce que cela va faire est de définir Chrome storage avec chaque marque-page.

Donc, en gros, chaque vidéo, selon son numéro d'identification vidéo que nous récupérons de l'URL, correspondra également à un ensemble de marque-pages dans Chrome Storage.

Donc, pour faire cela, nous allons faire Chrome storage sync.

Et encore une fois, si vous êtes intéressé par cela, vous pouvez regarder dans la documentation pour trouver ce que cette fonction prend.

Current video, il est important de se souvenir que les choses doivent être stockées en JSON dans Chrome Storage.

Donc, je vais faire JSON stringify.

Tous mes marque-pages de vidéo actuelle, donc je vais en fait ajouter une variable ici qui va stocker tous les marque-pages de vidéo actuelle dans un tableau.

Et je vais l'étendre.

Donc, nous pouvons ajouter un nouveau marque-page à cet ensemble de marque-pages de vidéo actuelle.

Et puis la dernière chose que je veux faire ici est de trier les marque-pages par leur timestamp de sauvegarde dans notre Chrome Storage.

Donc, nous allons trier par temps, et cela vient simplement de ceci ici, chaque marque-page va avoir un temps et une description.

Donc, nous allons regarder cela et trier en conséquence.

Super.

Maintenant, si nous rechargeons notre extension, nous allons voir si elle fonctionne comme prévu.

Et la façon de voir cela est essentiellement console dot log, ce nouveau marque-page, faisons-le.

Super.

Cette fois, cela a fonctionné, nous avons juste dû lui donner une autre recharge.

Et nous avons obtenu un temps en secondes et une description.

Maintenant, la dernière chose que je veux faire est de compléter ce fichier avant de passer à l'interface utilisateur.

Et nous voulons rendre cela entièrement fonctionnel pour récupérer tous les marque-pages lorsqu'une nouvelle vidéo est chargée.

Pour ce faire, nous allons récupérer de manière asynchrone tous les marque-pages de Chrome storage, ce qui signifie que je vais écrire une promesse qui se résout une fois que nous avons récupéré tous les marque-pages.

Donc, ce code va ressembler à ceci.

Je vais le créer ici.

Et je vais dire const fetch bookmarks.

Et je veux retourner une promesse.

Donc, nous pouvons résoudre cela de manière asynchrone.

Et dans cette promesse, je vais récupérer depuis Chrome Storage.

Donc, je vais faire un Chrome storage sync et nous avons fait un set avant pour définir Chrome Storage, nous allons obtenir cette fois notre vidéo actuelle, il prend un objet.

Et nous allons résoudre pour trouver des marque-pages lors de l'indexation en utilisant notre vidéo actuelle.

Donc, en gros, regardez dans le stockage pour voir si notre vidéo actuelle a des marque-pages, ou si elle existe dans le stockage.

C'est ce qui se passe ici.

Si elle existe, nous allons faire un JSON dot parse car nous avons fait un JSON dot Stringify avant, si elle n'existe pas, ce que nous voulons faire est de retourner un tableau vide.

Et cela devrait fonctionner.

Et nous allons vraiment seulement les ajouter dans deux endroits, qui seront dans notre fonction de nouvelle vidéo chargée.

Donc, nous allons rendre cela async.

Et nous allons ajouter un fetch bookmarks.

Donc, en fait, nous allons simplement ajouter cela à notre variable de marque-pages de vidéo actuelle.

Et appeler un poids fetch bookmarks.

Async await va résoudre cette promesse.

Et puis le deuxième endroit où nous voulons ajouter cela est à notre gestionnaire d'événements de nouveaux marque-pages.

Pour gérer ce cas, et nous assurer que nous utilisons toujours l'ensemble le plus à jour de marque-pages lors de la déstructuration.

Donc, nous allons faire current video bookmarks equals the weight, veg bookmarks.

Et aussi rendre cela async.

Génial.

Donc, pour l'instant, nous avons terminé tout ce dont nous avons besoin pour notre fichier de script de contenu, évidemment, les choses ne vont pas s'afficher dans l'interface utilisateur.

Et nous pourrions vérifier cela ici.

Et comme vous pouvez le voir, il n'y a rien dans l'interface utilisateur parce que tout ce que nous avons fait jusqu'à présent a été de manipuler le DOM ici pour ajouter l'icône.

Ajoutez une logique pour nous préparer à créer une interface utilisateur pour notre extension.

Commençons à faire apparaître certains composants de l'interface utilisateur en commençant par quelques marque-pages en cliquant sur ce bouton d'addition dans le lecteur YouTube que nous avons ajouté.

Maintenant, la première chose que nous devons déterminer sur n'importe quelle page donnée est de savoir si c'est une page vidéo YouTube ou non, si c'est le cas, nous allons récupérer les marque-pages que nous avons éventuellement depuis Chrome Storage.

Et si ce n'est pas le cas, nous allons simplement vouloir afficher un message disant qu'il ne s'agit pas d'une page YouTube.

Si vous ouvrez l'extension Chrome sur une page qui n'est pas YouTube.

Pour ce faire, nous allons ajouter une fonction utilitaire qui va nous permettre de déchiffrer cette logique.

Donc, nous allons en fait récupérer notre fonction utilitaire pour trouver l'onglet actif sur lequel se trouve l'utilisateur via la documentation Google Chrome.

Je vais utiliser cet exemple ici, qui nous aide à récupérer l'onglet actuellement focalisé depuis la documentation Chrome.

Et puisque j'ai l'extension Google Chrome Pieces sur chaque bloc de code, qu'il s'agisse de documentation ou de Stack Overflow, je suis en mesure de sauvegarder directement sur Pieces avec cette icône qui apparaît en haut à droite de tout bloc de code, je vais sauvegarder cela.

Et puis je vais revenir à mon VS code et rafraîchir mon arbre de pièces, je peux insérer cet extrait, qui est le plus récent, et je vais simplement renommer cet extrait en active tab Chrome.

Incroyable et Pieces a automatiquement classé cela comme JavaScript, car il a été en mesure de déchiffrer cela à partir d'un peu d'apprentissage automatique.

Je vais supprimer ce commentaire background.js.

Et génial, nous avons maintenant une fonction qui récupère l'onglet actuel.

Mais aussi, je veux m'assurer que j'exporte cette fonction.

Donc, je vais ajouter export.

Et puis ce que je veux faire est d'ouvrir le fichier pop-up.js.

Et ici, nous allons vouloir importer cette fonction tout en haut.

Donc, nous pouvons l'utiliser ici.

Donc, je vais importer Get active tab URL depuis utils dot j, s, et en fait, je ne pense pas que la documentation l'ait appelé ainsi.

Donc, je vais changer le nom de la fonction pour qu'il corresponde.

Donc, allez dans utils.js.

Changez cela, génial.

Maintenant, l'événement que nous voulons écouter lors de l'ouverture du fichier pop-up.js est l'événement DOM content loaded, qui est ici.

Cet événement est un événement natif de la fenêtre qui se déclenche lorsqu'un document HTML a été initialement chargé.

C'est essentiellement lorsque nous voulons charger tous nos marque-pages et les afficher.

Donc, nous allons taper ce qui suit pour ce faire, ce que nous allons faire est de récupérer notre fonction active tab en premier.

Et nous allons regarder l'onglet actuel de l'utilisateur, que nous avons déjà la fonction pour depuis les utiles.

C'est une fonction asynchrone.

Donc, nous allons async await cela.

Et puis après cela, nous allons récupérer les paramètres de requête pour nous aider à identifier la vidéo.

Si vous vous souvenez, chaque vidéo YouTube a un identifiant unique.

Après le point d'interrogation, où le paramètre de requête, nous allons récupérer cela, nous allons utiliser un URL search params pour pouvoir obtenir l'identifiant unique pour chaque vidéo.

Et pour obtenir l'identifiant unique, nous allons créer une variable current video et faire URL parameters dot get V.

Et cela est simplement basé sur l'apparence des URL des vidéos YouTube.

Maintenant, notre active tab URL devrait avoir youtube.com/watch car toute vidéo YouTube spécifique a toujours cela dans son URL.

Et nous voulons nous assurer que nous regardons une vidéo YouTube lorsque notre extension Chrome a une logique avec des marque-pages.

Et nous voulons nous assurer que cette variable current video est vraie, ce qui signifie qu'elle a effectivement retourné quelque chose d'autre que undefined ou une valeur fausse.

Et puis ce que nous voulons faire, c'est que nous voulons obtenir tous les marque-pages de la vidéo actuelle depuis le stockage Chrome.

Si vous vous souvenez, nous définissons le stockage Chrome avec la vidéo actuelle comme clé et puis tous les marque-pages comme valeur qui est JSONifiée.

Et afin de récupérer ces marque-pages, nous devons utiliser une API Chrome Storage pour les obtenir.

Donc, pour ce faire, nous allons récupérer les marque-pages vidéo en utilisant Chrome storage sync get.

Et nous allons l'obtenir avec l'identifiant unique de la vidéo actuelle, qui est l'identifiant unique des vidéos YouTube dans l'URL.

Et puis, nous allons définir une variable current video bookmarks qui va contenir tous ces marque-pages vidéo actuels JSONifiés.

Et afin de passer cela à n'importe quelle fonction ou d'écrire une logique personnalisée pour afficher les marque-pages, nous allons devoir JSON dot parse tous les marque-pages qui sont sauvegardés dans Chrome Storage puisque c'est en JSON, et nous ne pouvons pas vraiment travailler avec cela.

Mais s'il n'y a pas de marque-pages ou si chrome searches et ne retourne rien, nous allons simplement vouloir retourner un tableau vide.

Maintenant, nous allons devoir passer cela à la fonction view bookmarks, qui va essentiellement nous aider à voir tous les marque-pages dans notre extension, que Chrome Storage dot get retourne.

Mais avant cela, je vais simplement mettre un commentaire ici.

Donc, nous nous souvenons, nous voulons gérer cette condition else, qui est essentiellement pour le scénario où nous ne sommes pas sur une page vidéo youtube.com, ou current video retourne une valeur fausse.

Donc, ce que nous allons vouloir faire est d'ajouter un message qui dit que ce n'est pas une page vidéo YouTube.

Et revenons simplement à chrome pour voir à quoi cela pourrait ressembler.

Donc, voici notre interface utilisateur actuellement, nous avons cette classe de conteneur ici qui encapsule et encapsulera éventuellement tous les marque-pages que nous avons, elle a ce nom de classe de conteneur, ce que nous allons vouloir faire est d'obtenir ce nom de classe.

Donc, nous allons simplement faire cela dans la console avant de le faire en code juste pour être sûr que cela fonctionne.

La classe s'appelait container.

Et cela vient simplement du CSS dans le code de base, donc vous n'avez pas à vous en soucier, ou du HTML ou autre.

Donc, lorsque nous avons écrit ce document qui obtient les éléments par le nom de classe container, puis nous avons pris le premier élément dans la collection HTML, nous avons obtenu cet élément ici, qui contient tous ces autres éléments.

Et ce que nous voulons faire ici est de spécifier dans le HTML sur les pages qui ne sont pas youtube.com.

Donc, c'est en fait une page vidéo YouTube.

Nous ne voulons pas afficher ce message.

Mais je veux juste montrer comment cela va ressembler, nous allons vouloir mettre une nouvelle div class qui dit, ce n'est pas une page vidéo YouTube.

Et voyons simplement si cela fonctionne.

Cela va-t-il changer l'extension de la manière dont nous le voulons ? Container n'est pas.

Donc, ce que nous devons faire ici est en fait d'encapsuler cela dans une variable.

Nous allons définir cela égal à container.

Et maintenant, essayons cela.

Et changeons l'extension pour montrer que ce n'est pas une page vidéo YouTube.

Donc, la façon dont nous allons faire cela dynamiquement dans notre code est de mettre tout le code que nous venons de mettre dans notre console pour tester cela dans nos conditions else.

Donc, chaque fois que nous ne sommes pas sur une page vidéo YouTube, ou que cela retourne une valeur fausse, nous voulons montrer que ce n'est pas une page vidéo YouTube lorsque nous essayons d'ouvrir l'extension Chrome dans ces scénarios.

Donc, nous allons dire const container égal document dot get elements by class name, juste là.

Prenez cette classe de conteneur, premier élément.

Et puis définissez le inner HTML, définissez cela égal à div class égal title, title, ajoutez simplement un peu de style, cela va le rendre légèrement plus joli.

Il n'y a rien de super spécial dans le style que j'ai.

Et puisque nous l'avons testé, il ne devrait pas vraiment y avoir de surprises ici, cela devrait fonctionner comme prévu.

Donc, allons-y et donnons à cette extension une recharge.

Elle ne devrait pas montrer le message pour cette page.

Elle ne le fait pas.

Mais si nous allons sur une page non YouTube, elle va dire que ce n'est pas une page vidéo YouTube.

Incroyable.

Donc, retournons à notre code.

Et nous allons vouloir écrire cette fonction view bookmarks.

Donc, si elle remplit les conditions d'être sur une page youtube.com/watch, et comme vous pouvez le voir, c'est à partir de n'importe quelle page qui a une page vidéo, elle a youtube.com/watch dessus.

Et vos URL params dot get le retour quelque chose donc c'est une valeur vraie, nous allons vouloir voir les marque-pages associés à cette vidéo.

Donc, allons-y et appelons la fonction view bookmarks et passons-lui tous les marque-pages de la vidéo actuelle.

Et nous allons écrire la logique qui va nous aider à remplir l'interface utilisateur avec tous les marque-pages que nous avons récupérés de Chrome Storage.

Donc, pour ce faire, nous allons lui passer les marque-pages actuels.

Et nous allons définir un argument par défaut comme un tableau vide au cas où rien ne lui serait passé.

Il va simplement retourner ou montrer aucun marque-page, et nous allons récupérer un élément de marque-page.

Encore une fois, cela vient simplement du HTML que je vous ai donné.

Donc, ce n'est rien dont vous devez vous soucier.

Si vous voulez essayer cela par vous-même, vous pourriez l'essayer dans la console.

Juste pour gagner du temps ici, je vais simplement écrire le code ici.

Et vous pouvez aller de l'avant et le copier.

Mais encore une fois, il s'agit simplement de savoir comment travailler avec le DOM et d'inspecter les éléments pour comprendre comment faire cela.

Ce que je fais ici, c'est essentiellement dire, d'accord, s'il y a des marque-pages, définissons-le simplement à rien.

Donc, nous n'affichons rien, nous allons réinitialiser tout cela, puisque nous appelons cette fonction pour voir les marque-pages.

Et nous allons avoir de nouveaux marque-pages qui sont passés, qui sont les marque-pages actuels.

Et nous allons dire si la longueur des marque-pages actuels est supérieure à zéro, ce qui signifie s'il y a des marque-pages actuels, et ce n'est pas simplement un tableau vide.

Allons-y et itérons sur tous ces marque-pages, et affichons-les dans notre interface utilisateur.

Donc, pour ce faire, nous allons itérer sur chaque marque-page dans une boucle.

Et puis, nous allons récupérer le marque-page par indexation, donc les marque-pages actuels.

Avec n'importe quelle itération dans laquelle nous nous trouvons dans la boucle.

Et puis, ce que nous allons devoir faire à partir de là est d'appeler une autre fonction, add new bookmark, qui va ajouter une nouvelle ligne de marque-page à notre pop-up, je vais supprimer ce commentaire.

Et nous allons ajouter un nouveau marque-page, nous allons lui passer l'élément de marque-page ici, qui va remplir tous nos marque-pages, eh bien, ce sera là où nous ajouterons chacune de nos lignes.

Et je vais lui passer chaque marque-page spécifique.

Donc, nous allons ajouter un marque-page à la fois et appeler cette fonction chaque fois que nous ajoutons un marque-page.

Mais avant cela, ce que nous voulons faire est, s'il n'y a pas de marque-pages à montrer, ce qui signifie que les marque-pages actuels sont simplement un tableau vide.

Nous allons vouloir un message qui dit qu'il n'y a pas de marque-pages ici.

Donc, nous allons définir un message en utilisant l'italique.

En disant aucun marque-page.

Pour montrer avant de passer à autre chose et d'ajouter des marque-pages individuels à notre pop-up, allons-y et vérifions si cette condition fonctionne.

Où il n'y a pas de marque-pages à montrer et puisque nous n'avons ajouté aucun marque-page à cette vidéo YouTube que je regarde en ce moment, cela devrait fonctionner, je veux aller de l'avant et recharger mon extension.

Oui, il est là, aucun marque-page à montrer.

Incroyable.

Donc, maintenant nous allons vouloir enfin gérer le cas où nous avons des marque-pages à montrer et cela va nous permettre de commencer à voir des marque-pages dans notre interface utilisateur.

Donc, la première chose que nous allons faire est d'aller à notre fonction add new bookmark.

Et elle va accepter bookmark bookmarks element, et elle va accepter un bookmark.

Et puis ce que nous allons faire à partir de là est de créer deux éléments.

Donc, un élément est pour le titre, qui va s'afficher dans l'interface utilisateur de chaque bookmark.

Et puis un élément est l'élément bookmark entier qui contiendra le titre, contiendra le bouton de suppression et contiendra le bouton de lecture.

Donc, allons-y et créons l'élément bookmark title.

Et puis après celui-ci, nous allons aussi créer le nouvel élément bookmark, qui encapsulera tous ces autres éléments qui font partie d'une ligne de bookmark.

À partir de là, pour l'élément bookmark title, nous allons vouloir afficher ce qu'est le bookmark et lui donner un titre.

Donc, nous avons en fait déjà créé le titre.

Le titre est la description du bookmark.

Si vous vous souvenez de notre objet bookmark, il y a un timestamp et une description.

Donc, nous allons définir notre contenu texte à la description, qui est bookmark dot description.

Et puis notre nom de classe va être bookmark title element dot class name, et cela sera défini égal à bookmark title et cela va simplement ajouter un peu de CSS, qui est déjà dans notre code de base.

Maintenant, pour le composant général qui va encapsuler tous les boutons de lecture, le titre, un bouton de suppression, tout ce que vous pourriez vouloir ajouter, nous allons faire quelques choses, la première chose que nous allons faire est de lui donner un ID de bookmark element, ou bookmark avec le temps du bookmark, et cela va garantir un ID unique pour chaque élément qui est une ligne.

Donc, si vous sauvegardez un bookmark, ce qui va se passer, c'est qu'il y aura une ligne associée à chaque bookmark, qui est notre nouvel élément bookmark.

Et il y aura un ID défini pour cette ligne, qui sera le bookmark avec le temps et ils nous aideront à identifier de manière unique toute ligne spécifique dans l'interface utilisateur.

Et plus tard, nous allons l'utiliser pour supprimer des éléments lorsque nous supprimons un bookmark spécifique.

Et puis nous allons définir un nom de classe, qui va aider avec un peu de style, qui va être défini à une classe bookmark.

Et puis nous allons définir un attribut qui va nous aider avec la lecture d'une vidéo.

Parce que, en gros, nous allons vouloir connaître le timestamp de tout bookmark spécifique.

Donc, lorsque nous lisons la vidéo, nous savons où définir le lecteur vidéo à l'heure que nous voulons l'envoyer et l'attribut de l'élément bookmark va nous aider à trouver cela.

Et les dernières choses que nous voulons faire ici sont, puisque nous savons que le nouvel élément bookmark encapsule toutes ces autres choses, nous voulons append child bookmark title element, donc il s'affiche dans le nouvel élément bookmark.

Et puis nous avons cet élément bookmarks qui est passé.

Et nous allons append notre nouvel élément bookmark, qui est cet élément qui encapsule toutes les autres choses.

À l'intérieur de cela puisque c'est un conteneur.

Donc, maintenant si nous retournons à notre interface utilisateur, et que nous lui donnons une recharge, juste au cas où, allons simplement à une nouvelle vidéo.

Et si j'appuie sur plus, dans cette vidéo, nous voyons une nouvelle ligne, elle dit bookmark out une heure, 54 minutes.

Et nous pourrions ajouter une autre ligne si nous le voulons.

Et elle nous donne cette même ligne, nous allons gérer le cas de la suppression, il y a un ADD, il va simplement se définir à zéro secondes.

Bookmark it 000.

Génial.

Donc, cela fonctionne.

Donc, maintenant, travaillons sur quelques fonctionnalités supplémentaires.

Pour l'instant, nous n'avons aucune fonctionnalité associée à chaque bookmark, donc nous ne pouvons pas lire de bookmark avec un timestamp particulier, nous ne pouvons pas supprimer un bookmark.

Et la prochaine chose que nous voulons ajouter est le bouton de lecture.

Donc, pour ce faire, nous allons ajouter un bouton de lecture à chaque bookmark qui ira directement à ce timestamp que nous avons sauvegardé pour chaque vidéo.

Pour commencer, nous allons devoir ajouter une fonction qui va ajouter une icône pour un bouton de lecture, écouter un clic et appeler une fonction ou un écouteur d'événements qui effectuera la logique pour définir une vidéo à un timestamp particulier.

La fonction finira par ressembler à quelque chose comme ce que nous allons coder ici dans une seconde.

Et nous allons la garder super générique car elle sera utilisée à la fois pour notre fonctionnalité de suppression et de lecture.

Donc, les fonctions vont prendre un attribut source, un écouteur d'événements.

Et un élément parent de contrôle.

Et lorsque nous disons des éléments de contrôle dans notre code, cela signifie le bouton de lecture, le bouton de suppression, nous appelons simplement ceux-ci des éléments de contrôle.

Donc, nous allons créer un élément de contrôle.

Et ce n'est qu'une fonctionnalité particulière, nous allons appeler un élément de contrôle singulier.

Donc, dans ce cas spécifique, nous allons avoir un bouton de lecture.

Mais encore une fois, c'est une fonction générique.

Donc, pensez à cela comme un bouton de lecture, un bouton de suppression, nous voulons que cet élément de contrôle singulier soit l'un de ceux-ci.

Et puis ces éléments de contrôle seront liés à une image dans notre dossier d'actifs.

Donc, si nous voulons un bouton de lecture, ce que nous allons lier est assets slash play dot PNG, et notre schéma est super prévisible pour cela.

Donc, tout ce que nous allons faire est assets plus SRC plus dot png.

Et il y a définitivement une meilleure façon de faire cela, vous pouvez revenir et travailler sur le code après cette vidéo.

Mais nous allons simplement le garder super simple pour l'instant.

Nous allons lui donner un titre qui est le même que notre attribut source, ou ce que nous passons dans cette source.

Donc, ce qui va être passé ici est play, edit, delete, peu importe.

Et le titre sera défini à cela.

Donc, dans ce cas particulier, pour play, il sera défini comme play, nous allons ajouter un écouteur d'événements.

Et cet écouteur d'événements écoutera un clic.

Et nous allons lui passer une fonction qui sera exécutée lors de ce clic.

Et la dernière chose que nous voulons faire est qu'il y aura un conteneur pour tous les éléments de contrôle.

Et nous passons cela dans cette fonction.

Et nous l'appelons control parent element.

Donc, nous allons append cet élément de contrôle singulier à l'élément parent.

Et la prochaine chose que nous allons vouloir faire est d'ajouter l'appel de fonction qui ajoutera un bouton de lecture, un titre et notre écouteur d'événements à chaque bookmark individuel.

Donc, dans la fonction add new bookmark que nous avons codée plus tôt, nous allons ajouter quelques lignes de code ici.

Et ces quelques lignes de code vont ajouter ces éléments de contrôle.

Donc, nous allons créer l'élément qui va contenir tous nos boutons, nous allons l'appeler l'élément controls.

Et ce sera une div comme ces autres, nous allons le garder super simple.

Et puis ce que nous voulons faire est de lui donner un peu de style.

Nous allons ajouter le nom de la classe, mais controls, et vous allez simplement devoir me faire confiance sur cela, il existe.

Ensuite, ce que nous voulons faire est de définir nos attributs en utilisant une fonction set bookmark attributes que nous avons créée, nous allons passer en lecture, l'écouteur d'événements sera appelé sur Play.

Et nous allons le coder plus tard.

Et puis nous allons passer l'élément controls, qui sera l'élément parent.

Et la dernière chose que nous voulons faire est de l'ajouter à notre nouvel élément bookmark.

Et ce que nous devrions voir maintenant, c'est que ce bouton de lecture va apparaître dans notre extension.

Donc, vérifions cela.

Donnons-lui une actualisation ici.

Le voilà.

Nous avons le bouton de lecture dans notre extension.

Mais ce que nous allons remarquer, c'est qu'il ne va pas fonctionner.

Allons-y et lisons cette vidéo.

Et nous allons essayer de la ramener à 26 minutes, 51 secondes, cela ne fonctionne pas.

Et la raison pour laquelle cela ne fonctionne pas est que nous devons encore coder l'écouteur d'événements On Play.

Donc, allons-y et faisons cela.

Ce que nous allons faire est de cibler l'attribut timestamp que nous avons défini précédemment.

Donc, encore une fois, vous pourriez vérifier cela dans votre console ou inspecter, si vous voulez une visualisation de la façon dont cela va fonctionner.

Mais je vais taper cela pour gagner du temps.

Et nous allons récupérer ce timestamp que nous avons défini précédemment.

Et puis la deuxième chose que nous allons vouloir faire est de récupérer l'onglet actif, et cela en utilisant simplement la fonction active tab.

C'est une fonction async await.

Donc, nous allons devoir l'async await.

Et je vais ajouter async pour rendre cette fonction asynchrone.

Donc, nous avons en fait un problème maintenant, nous devons envoyer le script de contenu et un message pour manipuler le lecteur YouTube pour le définir au timestamp où le marque-page est placé.

Donc, dans ce fichier, nous allons devoir ajouter ce message.

Allons-y et envoyons un message au script de contenu.

Et cela va suivre le même schéma que nous l'avons fait avec notre script de fond.

Il manque une virgule là.

Nous allons avoir un type de lecture.

C'est le type d'événement.

Et puis la valeur va être le temps du marque-page.

Et puis dans notre script de contenu, nous allons devoir être capables de lire ce message.

Donc, ce que nous allons faire est d'ajouter une condition à notre écouteur de messages ici, et nous allons dire si le type est lecture.

Définissons le temps du lecteur YouTube égal à la valeur qui est passée.

Donc, en gros, jetons un coup d'œil à cela pendant une seconde.

Si un message de type lecture est envoyé, et que la valeur est le temps du marque-page, alors ce que nous voulons faire est de prendre cette valeur et de la définir comme le temps actuel du lecteur YouTube, ce qui en fera le temps du marque-page.

Et allons-y et voyons si cela fonctionne.

Je vais recharger mon extension.

Et allons-y et allons à l'extension, nous avons un marque-page à 26 minutes, 51 secondes, il est actuellement à 48 minutes, 30 secondes.

Appuyons sur ce bouton de lecture.

Il revient à 26 minutes, 51 secondes.

Et maintenant si nous appuyons également sur ce bouton d'addition n'importe où dans la vidéo, nous devrions obtenir un nouveau marque-page, nous avons deux heures, 21 minutes, 22 secondes.

Maintenant, allons de l'avant.

Appuyons sur lecture ici.

Et il revient à ce moment-là.

Génial.

Donc, maintenant notre bouton de lecture fonctionne.

La dernière fonctionnalité que nous voulons construire est la capacité de supprimer un marque-page, ce qui sera très similaire à ce que nous avons fait pour le bouton de lecture.

La première chose que nous allons vouloir faire est d'aller dans notre fichier POP up.js.

Et nous allons ajouter le bouton de suppression à notre élément controls avec le code dans notre fonction add new bookmark pour définir les attributs du marque-page.

Donc, allons-y et faisons cela, nous allons passer en suppression notre écouteur d'événements on delete, et puis l'élément parent controls.

Et puisque nous avons défini la fonction ondelete comme l'écouteur d'événements, nous devons coder quelques opérations qui vont prendre soin de notre suppression.

Donc, nous savons déjà que nous allons utiliser cet onglet actif que nous avons utilisé ici.

Donc, allons-y et créons cette fonction asynchrone à l'avance.

Prenons l'onglet actif de l'utilisateur.

Et puis ce que nous allons vouloir faire est de récupérer l'attribut timestamp que nous avons défini précédemment.

Et ce sera le même code que celui d'ici.

Donc, je vais simplement copier et coller, voilà.

Ensuite, ce que nous allons aussi vouloir faire est de récupérer l'élément que nous voulons supprimer.

Donc, si vous vous souvenez, j'ai créé un ID spécifique lié aux timestamps, ce que nous allons vouloir faire est de récupérer les éléments par l'ID afin que nous puissions les supprimer.

Donc, bookmark.

Plus le bookmark time nous donnera l'élément que nous voulons supprimer.

Et puis ce que nous allons faire est de supprimer cet élément en allant au nœud parent, et puis en supprimant l'enfant qui sera l'élément que nous voulons supprimer.

Et puis la dernière chose que nous allons vouloir faire ici est d'envoyer un message à notre script de contenu.

En disant que nous voulons effectuer une suppression de type delete, et puis la valeur sera le bookmark time.

Et il y a une dernière chose que nous voulons faire ici, cette fonction Send Message de l'API Chrome's tabs prend en fait une fonction de rappel en option.

Et nous allons en passer une qui sera notre fonction view bookmarks.

Et cela va simplement rafraîchir nos marque-pages, donc toute suppression apparaît immédiatement, puis dans notre script de contenu, nous allons ajouter une autre condition, qui est essentiellement que vous allez ingérer ce message de suppression.

Donc, nous allons dire else if type equals Delete.

Les marque-pages de la vidéo actuelle seront égaux aux marque-pages de la vidéo actuelle.

Filtre, et nous allons filtrer par temps.

Donc, le temps n'est pas égal à la valeur passée car c'est une valeur que nous supprimons.

Et puis la dernière chose que nous voulons faire est de synchroniser Chrome Storage.

Donc, si cette page se recharge, ce marque-page supprimé ne s'affiche pas.

Nous allons JSON fi, error bookmarks et si cela devrait fonctionner, la dernière chose que nous voulons faire est d'ajouter un moyen d'envoyer les marque-pages mis à jour à notre fichier POP up.js afin d'afficher les marque-pages les plus récents, et nous ferons ce qui suit.

Pour ce faire, nous allons envoyer une réponse des marque-pages de la vidéo actuelle.

Donc, maintenant nous pouvons essayer de supprimer un marque-page avec un rechargement de notre extension, et cela devrait commencer à fonctionner.

Donc, je vais revenir à notre navigateur Chrome, recharger notre extension.

Et si nous supprimons un marque-page, nous allons voir qu'ils sont supprimés.

Si nous ajoutons un marque-page, nous allons voir qu'il y a un nouveau marque-page.

Il est à un timestamp différent, le lecteur YouTube est à un temps différent.

Donc, si nous lisons, il revient au timestamp du marque-page.

Nous voulons supprimer à nouveau, il va supprimer.

La dernière chose que nous allons vouloir faire est de distribuer notre extension.

Cependant, je ne vais pas tout à fait passer en revue cela dans cette vidéo, car Google fournit une excellente documentation qui sert de guide étape par étape sur la façon de publier votre extension chrome sur le Google web store pour que tout le monde puisse la télécharger.

Et avec cela, la vidéo est terminée, vous savez tout ce que vous devez faire pour créer une extension web moderne en utilisant manifest v3, et je vous verrai la prochaine fois.