---
title: Extensions VS Code pour augmenter la productivité des développeurs
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-03-21T20:23:21.000Z'
originalURL: https://freecodecamp.org/news/vs-code-extensions-to-increase-developer-productivity
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/vscode.png
tags:
- name: Visual Studio Code
  slug: vscode
- name: youtube
  slug: youtube
seo_title: Extensions VS Code pour augmenter la productivité des développeurs
seo_desc: "Visual Studio Code is one of the most popular code editors used by software\
  \ developers. While it has many great features built-in, there are a lot of extensions\
  \ you can install to increase your productivity. \nWe just published a video on\
  \ the freeCode..."
---

Visual Studio Code est l'un des éditeurs de code les plus populaires utilisés par les développeurs de logiciels. Bien qu'il possède de nombreuses fonctionnalités intégrées, il existe de nombreuses extensions que vous pouvez installer pour augmenter votre productivité.

Nous venons de publier une vidéo sur la chaîne YouTube de freeCodeCamp.org qui vous présentera dix extensions Visual Studio Code.

Raman Hundal a développé cette vidéo. Raman est un développeur de logiciels qui a utilisé de nombreuses extensions différentes. Dans cette vidéo, il partage certaines de ses extensions VS Code préférées.

Dans ce cours, vous découvrirez les extensions suivantes :

* GitLens
* LiveShare
* Pieces
* Better Comments
* Turbo Console Log
* Code Runner
* Import Cost
* Prettier
* ESLint
* Docker

Et les spectateurs ont partagé encore plus d'excellentes extensions dans les commentaires de la vidéo.

Regardez la vidéo ci-dessous ou [sur la chaîne YouTube de freeCodeCamp.org](https://www.youtube.com/watch?v=g1vy03ZY5mM) (vidéo de 30 minutes).

%[https://www.youtube.com/watch?v=g1vy03ZY5mM]

### Transcription

(auto-générée)

Dans ce cours, vous découvrirez des extensions populaires de Visual Studio Code qui peuvent vous aider à améliorer votre productivité.

Bonjour à tous, je m'appelle Ramin et je suis un développeur full stack.

Aujourd'hui, je vais vous parler de 10 extensions VS Code qui vont vous faciliter la vie en tant que développeur et qui m'ont également rendu plus productif.

Sous cette vidéo se trouve une liste de ces 10 extensions ainsi que les endroits où vous pouvez aller pour les télécharger.

Alors, commençons.

La première extension dont nous allons parler est GitLens.

GitLens est une extension VS Code qui vous permet de visualiser le contexte Git autour des fichiers, mais aussi des lignes de code. Vous pouvez rechercher GitLens dans la marketplace des extensions de VS Code, et ce sera probablement le premier résultat de recherche qui apparaîtra.

Elle est publiée par GitKraken.

Si vous voyez cela, installez-la.

Une fois l'installation terminée, vous devrez recharger votre fenêtre pour que l'extension prenne effet immédiatement.

Sur Mac, vous pouvez appuyer sur Command Shift P, pour Windows Ctrl Shift P, ce qui ouvrira la palette de commandes ; tapez simplement "reload window" et rechargez-la.

Ce que vous remarquerez immédiatement, c'est que partout où se trouve votre curseur, il y aura cette annotation discrète.

En gros, elle indiquera l'auteur du Commit Git, la date du Commit et le message du Commit.

Et maintenant, si vous survolez cette ligne, vous obtiendrez une meilleure visualisation de toutes ces informations.

En bas à gauche, vous remarquerez un numéro de Commit Git. Si vous cliquez dessus, vous aurez plusieurs options : vous pourrez révéler le Commit dans une barre latérale, annuler le Commit, réinitialiser le Commit, et ainsi de suite.

Dans notre cas particulier, nous allons examiner ce Commit dans une barre latérale.

Vous verrez alors cette arborescence qui montre chaque Commit, et elle a déjà développé le Commit qui nous intéresse. Vous pouvez interagir avec cette arborescence ; je vais juste cliquer sur le fichier "calendar view" car il est indiqué qu'il a été ajouté.

Et je peux voir tous les ajouts qui ont été faits dans ce fichier.

Dans ce cas précis, tout le fichier a été ajouté.

Si vous souhaitez regarder d'autres Commits, vous pouvez réduire celui-ci et en développer d'autres à volonté.

Si vous remontez d'un niveau, vous pouvez voir tout ce que GitLens vous permet de faire.

Il vous permet d'utiliser le contrôle de source, d'utiliser cette vue des Commits, une vue de l'historique des fichiers, vous pouvez regarder toutes vos branches locales (je n'en ai qu'une, la branche main), vos branches distantes.

Encore une fois, je n'en ai qu'une qui est la branche main distante. Vous pouvez regarder les stashes Git, les tags.

Et il y a cette fonction de recherche et de comparaison où vous pouvez rechercher des Commits par message, auteur, fichier, etc.

Maintenant, si vous retournez dans ce menu au survol, vous remarquerez une icône de globe.

Cette icône de globe vous permet de regarder votre Commit sur GitHub.

Avant de faire cela, vous devrez vous synchroniser avec GitHub.

Dans mon cas, je l'ai déjà fait, il y aura une icône juste ici.

Et ce qu'elle fera, c'est récupérer la photo de l'auteur depuis GitHub et vous permettre de cliquer sur cette icône.

Je vais donc cliquer sur cette icône.

Et cela va me montrer tous les changements de ce Commit via GitHub.

Maintenant, nous allons revenir en arrière.

Et la dernière chose que je vais vous montrer est cette option d'équipe (Team).

Cela nous permet d'ouvrir une session Live Share avec l'auteur de ce Commit.

Dans ce cas particulier, nous n'avons pas encore installé Live Share.

Je vous montrerai comment démarrer des sessions et interagir avec Live Share plus tard dans cette vidéo.

Mais c'est une fonctionnalité pratique à connaître.

En bas, vous verrez cette option "bar blame".

En gros, cela nous montre le dernier auteur sur ce fichier, ainsi que la date du dernier Commit.

Et en haut, nous voyons tous les auteurs sur ce fichier.

Dans ce cas, c'est juste moi.

Il ne m'affiche donc que comme auteur unique.

Mais s'il y a plusieurs auteurs, il affichera le nom de tous les auteurs ainsi que leur nombre.

Je trouve cela souvent très utile quand je dois taguer des gens dans des PR.

Souvent, les meilleures personnes à taguer sur une PR sont celles qui ont soit créé le fichier, soit travaillé dessus auparavant.

C'est tout ce que je vais aborder sur GitLens dans cette vidéo.

Si vous souhaitez en savoir plus sur les différentes fonctionnalités, n'oubliez pas de consulter la documentation.

J'espère que vous trouverez cela utile lorsque vous chercherez les bonnes personnes à taguer sur les PR, ou si vous essayez simplement de mieux visualiser Git.

À une époque où le travail à distance est devenu si normalisé.

J'ai souvent trouvé très difficile de collaborer avec mes pairs dans VS Code.

Live Share est une extension qui a rendu la collaboration et le pair programming incroyablement plus faciles.

Live Share est un moyen pour moi d'héberger des sessions avec jusqu'à 30 personnes où je peux déboguer des fichiers avec d'autres, faire du pair programming et même enseigner.

Quand j'utilise Live Share, je peux aussi partager diverses ressources comme un serveur, mon terminal ou mes fichiers directement via ma session en utilisant des permissions de lecture et/ou d'écriture.

Actuellement, je vais appeler mon ami Liam, qui va m'aider à déboguer un problème avec mon application de calendrier en utilisant VS Code Live Share.

Pour commencer, je vais cliquer ici sur mon nom. Cela va ouvrir quelques options : "start a collaboration session" (démarrer une session de collaboration), "start read only collaboration session" (démarrer une session en lecture seule) ou "join a collaboration session" (rejoindre une session).

Dans mon cas, je veux en démarrer une.

Ensuite, je vais ouvrir cela à nouveau.

Et je vais copier mon lien.

Ainsi, je peux inviter mon ami Liam à m'aider avec ce bug sur lequel je galère.

Maintenant, mon ami Liam a rejoint l'appel, et je vais démarrer un appel audio avec lui.

Je vais donc cliquer sur cette barre en bas et démarrer ou rejoindre l'appel audio.

Cela va lancer un appel avec Liam, et il nous rejoindra sous peu.

Ce que vous remarquerez aussi entre-temps, c'est ce chat Live Share.

Le chat Live Share a également indiqué que Liam a rejoint. Vous pourriez choisir de discuter avec les autres via ce chat, mais dans mon cas, je trouve beaucoup plus facile de faire du pair programming via un appel.

Salut Ramin, tu m'entends ? Salut Liam.

Comment ça va ? Ça va bien, ça va bien. J'ai entendu dire que tu avais des problèmes de calendrier.

Ouais.

Il y a ce problème avec cette application de calendrier que j'ai faite.

En gros, je crée un événement.

Et après avoir créé l'événement, il s'affiche sur mon calendrier.

Mais quand je vais pour supprimer l'événement, il ne se supprime pas la première fois, mais il se supprime la deuxième fois que j'essaie.

Emmène-moi à ta fonction de suppression du calendrier.

Ouais, je pense qu'elle s'appelle `deleteEvent`.

Ok, ouais, c'est à la ligne 156.

Ok.

Je pense que tu vas vouloir ajouter un `async await` sur ce `calendarService.deleteEvents`.

Ok.

Essaie de sauvegarder ça et fais un test.

Très bien.

Je vais essayer de sauvegarder ça.

Je vais tester ça rapidement, juste pour m'assurer que ça fonctionne.

Oh, super.

Wow, ça a marché.

Hé, je suis ravi d'avoir pu t'aider.

Génial, merci.

De rien.

À plus tard.

À bientôt.

Et je vais arrêter cette session de collaboration, ce qui mettra également fin à l'appel avec Liam.

Et c'est là toute la puissance de VS Code Live Share : vous pouvez immédiatement partager votre session et votre écran avec quelqu'un d'autre.

Mais aussi configurer un appel audio et un chat directement dans votre éditeur VS Code.

Pieces est un gestionnaire de snippets de code assisté par IA qui classifie automatiquement les langages, aide à sauvegarder et réutiliser des extraits de code, et vous permet de convertir des captures d'écran de code en texte réel, entre autres choses, en utilisant leur extension VS Code et d'autres intégrations.

Pour commencer avec Pieces, vous pouvez aller directement sur code pieces.

En haut à droite, vous pouvez voir ce bouton "get pieces".

Quand vous le voyez, cliquez dessus.

Cela vous mènera à une page d'installation pour Pieces OS, qui est essentiellement le moteur qui alimente toutes les intégrations de Pieces, y compris l'extension VS Code.

Selon votre machine, vous devrez télécharger pour Mac ou Windows.

Dans mon cas, je veux l'installer pour Mac.

Après l'installation initiale, je veux obtenir à la fois Pieces OS et Pieces for Developers. Pieces for Developers ressemble à ceci.

Et c'est juste l'interface graphique pour mes snippets de code, sur laquelle je reviendrai un peu plus tard pour optimiser ma configuration.

Mais avant d'aborder Pieces for Developers, allons dans VS Code et installons l'extension Pieces for VS Code.

Quand vous allez dans VS Code et tapez "pieces", le premier résultat sera probablement Pieces for VS Code.

Si vous voyez cela, installez-le et vous verrez immédiatement cette nouvelle icône Pieces à gauche lors de l'installation.

Pour l'instant, je n'ai aucun snippet de code.

C'est donc vide. Ce que je vais vouloir faire, c'est ajouter un snippet de code.

En pratique, le genre de snippet de code que je veux ajouter est quelque chose que je pourrais réutiliser souvent, ou quelque chose que je pourrais référencer, ou peut-être juste quelque chose que j'ai trouvé particulièrement difficile à écrire ou à créer et que je veux garder en sécurité.

Disons que cette fonction `updateRange` répond à l'un de ces critères.

Je vais donc la sauvegarder dans Pieces avec un clic droit, puis "save to pieces".

Ce que nous allons voir immédiatement, c'est qu'il y a un nouveau répertoire de haut niveau appelé JavaScript provenant de l'auto-classification du snippet par Pieces.

Et si vous développez ce répertoire, vous pouvez cliquer sur le snippet JavaScript, et vous verrez la fonction `updateRange`. Vous pouvez également survoler le snippet, et cela vous montrera un aperçu de cette fonction.

Ce que je vais faire maintenant, c'est supprimer la fonction `updateRange` dans mon fichier `calendar.view`.

Et disons que je travaille sur un projet et que je veux récupérer cette fonction `updateRange`. Tout ce que j'ai à faire est d'aller sur mon snippet et d'appuyer sur "Insert snippet".

Et il a conservé la façon dont j'avais formaté cette fonction, et a également inséré ce morceau de code directement à l'endroit où je voulais que le snippet soit placé.

La dernière chose que je vais vouloir faire est de renommer le snippet en quelque chose de plus approprié. Je vais juste choisir le nom de la fonction, qui est `updateRange`.

Et maintenant, il est sauvegardé sous le nom `updateRange`.

Génial.

Pour récapituler, ce que Pieces me permet de faire est de stocker mon code facilement directement dans mon IDE, et me donne aussi la possibilité de ressortir ce code.

Là où Pieces commence à devenir vraiment puissant, c'est lorsque vous commencez à utiliser les autres intégrations avec VS Code.

Je vais maintenant aller sur Stack Overflow.

Et je regarde ce snippet SQL d'analyse de cohorte.

Je trouve ce snippet SQL d'analyse de cohorte vraiment utile.

Et c'est aussi assez difficile à écrire.

Je veux donc le sauvegarder dans Pieces.

Comme j'ai l'extension Google Chrome,

Je vais voir en haut à droite cette icône Pieces.

Cela me permet de cliquer sur l'icône et de sauvegarder directement ce snippet de code dans Pieces sans quitter Stack Overflow.

Je vais donc cliquer dessus.

Ensuite, au lieu de regarder dans VS Code, je vais ouvrir Pieces for Developers.

Ce que je vais voir dans Pieces for Developers, c'est une auto-classification du snippet SQL, qui est l'analyse de cohorte que je viens de vous montrer.

Et si je clique sur cette petite vue d'information, cela va me donner plus de métadonnées sur ce snippet particulier.

Il récupère le titre de Stack Overflow comme description, il récupère le lien de la question Stack Overflow, et il récupère l'origine, qui est l'extension Chrome de Pieces.

Et selon l'extension ou l'intégration que vous utilisez pour sauvegarder avec Pieces, l'origine sera différente.

Pour la recherche, je peux ajouter des tags, donc je vais ajouter "cohort" comme tag, je vais aussi ajouter "SQL" comme tag.

Et cela va généralement m'aider à mieux chercher en utilisant Pieces for Developers.

Maintenant, si nous retournons dans VS Code, nous pouvons ouvrir notre explorateur Pieces et rafraîchir l'arborescence.

Et si vous développez la section SQL, vous verrez le snippet SQL que nous venons de créer, qui est l'analyse de cohorte.

Cool.

Le deuxième cas d'utilisation pratique que j'ai trouvé pour l'intégration de Pieces, en particulier Pieces for Developers, est la conversion de captures d'écran de code en code réel que je peux utiliser.

Souvent, quand je regarde des vidéos de tutoriels, je ne veux pas mettre la vidéo en pause ou quitter la vidéo, parce que j'essaie vraiment de comprendre le sujet que j'apprends.

Mais je veux quand même prendre un morceau de code ou copier le morceau de code pour le garder, ou je veux juste l'exécuter localement pour le tester pendant que je regarde la vidéo.

Pieces peut être vraiment utile pour cela.

Cette vidéo particulière est une vidéo sur Free Code Camp qui vient de sortir pour construire un live stream en utilisant Flutter.

Je veux copier ces trois lignes de code, qui sont du Dart.

Et je vais convertir cela en code en utilisant Pieces for Developers.

Immédiatement, quand je fais glisser la capture d'écran vers Pieces for Developers, il l'identifie comme une image avec du Dart.

Il y a cette option "view as code" sur le côté droit.

Je vais cliquer dessus.

Ce que j'obtiens, c'est du code copiable depuis Pieces for Developers directement à partir de la capture d'écran.

Et juste pour vous montrer, je vais ouvrir mon IDE.

Je vais le coller et vous pouvez voir que j'ai copié ce code directement depuis Pieces for Developers.

Better Comments est une extension VS Code qui améliore vos commentaires en vous aidant à annoter et documenter le code plus efficacement en utilisant un système de balisage personnalisé.

Une fois l'installation de Better Comments terminée,

Vous allez vouloir ouvrir votre palette de commandes et taper "open Settings (JSON)".

Cliquez sur cette option.

Après avoir cliqué, nous allons taper "better-comments".

Et l'IntelliSense va s'activer et afficher ce `better-comments.tags`. Choisissez cela.

Cela affichera tous les paramètres par défaut pour Better Comments.

Il y a quelques tags qui sont fournis par défaut.

Il y a le tag d'alerte utilisant un point d'exclamation, il y a le point d'interrogation.

Il y a un tag de commentaire, un tag TODO, et un tag générique.

Et à l'intérieur d'un tag, il y a une propriété de couleur, un texte barré, un soulignement, une couleur d'arrière-plan, une propriété gras et italique.

Chacun d'eux peut être manipulé différemment, afin de créer un tag unique que n'importe qui peut identifier dans votre code ou qui peut être fait pour vous faciliter la lecture.

Avant de plonger dans le code, ajoutons un tag supplémentaire ici.

Nous allons créer un tag "bug".

Et ensuite, je vais changer la couleur.

Ainsi, nous pourrons l'identifier par une couleur aléatoire ici.

Sauvegardez ce fichier.

Et je vais aussi recharger ma fenêtre à nouveau, juste pour que cela s'applique.

Cool, donc ce tag "bug" devrait apparaître dans notre code.

Supposons que nous voulions simplement ajouter un commentaire à la ligne 15.

Je veux ajouter un commentaire disant que c'est un bug et qu'il y a une condition de concurrence (race condition).

Donc `// bug fix race condition here`.

Et maintenant, Better Comments récupère le tag du fichier `settings.json` et applique les propriétés que nous y avons définies.

Immédiatement.

Ce que je serai capable de dire avec l'utilisation de Better Comments, c'est que n'importe quel commentaire rose est probablement de la documentation pour un bug.

Et supposons que cette condition de concurrence soit, vous savez, un problème très grave.

Et nous voulons nous assurer que les gens le sachent, nous pouvons le passer en alerte.

Et il change pour cette couleur orangée qui a été définie par Better Comments.

Nous pouvons aussi regarder différents tags, comme un point d'interrogation, qui est bleu.

Et vous pourriez changer chacun d'eux comme vous le souhaitez dans notre fichier `settings.json`.

Disons, vous savez, que nous avions un commentaire de bug.

Et maintenant nous avons décidé que ce bug est corrigé.

Mais nous voulons laisser le commentaire dans la base de code.

Nous pouvons utiliser la fonction de texte barré de Better Comments, et cela le barrera simplement sans supprimer le commentaire.

Essentiellement, ce que Better Comments a fait, c'est qu'il a rendu plus facile la visualisation des commentaires dans votre base de code.

Et si vous utilisez des paramètres similaires, ou si tout le monde dans votre équipe l'utilise, ils vont maintenant pouvoir associer différentes couleurs de commentaires à différents types de problèmes.

Admettons-le.

Nous finissons tous par faire des tas de `console.log` quand nous essayons de trouver une erreur ou un bug.

Et j'adorerais dire que j'utilise le debugger à chaque fois.

Mais ce n'est tout simplement pas le cas.

Et c'est là que Turbo Console Log entre en jeu.

Turbo Console Log est fondamentalement une extension VS Code qui rend la journalisation (logging) beaucoup plus facile.

Vous pouvez facilement ajouter des détails aux messages `console.log`, supprimer ces messages d'un seul coup, et même les mettre tous en commentaire.

Je vais vous montrer ça rapidement.

En gros, supposons qu'il y ait un bug que j'essaie de trouver sur ce fichier `calendar.view`.

Et je veux faire un `console.log` de quelques éléments qui pourraient m'aider à traquer ce bug.

Je vais surligner quelques variables.

Et je vais utiliser Turbo Console Log pour m'aider à créer des messages de log pour elles.

Pour cette variable `event`, je vais appuyer sur Ctrl Option L.

Et cela créera un message de log pour moi sur Mac.

Pour les utilisateurs de Windows, vous ferez Ctrl Alt L.

Ensuite, je choisirai quelques autres variables, je ferai cet `event` ici.

CTRL Option L, je fais ce `type` ici CTRL Option L.

Et maintenant, nous avons quelques instructions de console.log.

Cool.

C'est à cela que finit par ressembler un fichier.

Et si nous regardons ces instructions `console.log`, ce que nous avons, c'est que chaque message contient le nom du fichier, le numéro de ligne associé au commentaire, la fonction et ensuite le nom exact de la variable.

Supposons maintenant que nous pensions avoir résolu le problème que nous essayions de traquer.

Et nous voulons mettre toutes ces lignes en commentaire pour s'assurer que le code fonctionne sans tout ce bruit supplémentaire.

Pour les utilisateurs de Mac, vous ferez Option Shift C et pour les utilisateurs de Windows, vous ferez Alt Shift C.

Nous allons donc faire Option Shift C puisque je suis sur Mac, et maintenant nous avons commenté toutes les lignes.

La seule chose à retenir ici, c'est que tous ces raccourcis clavier que je vous montre ne fonctionneront que pour les messages de log créés par Turbo Console Log. Si vous créez vos propres logs manuellement, ces raccourcis clavier ne fonctionneront pas pour ceux que vous avez créés vous-même.

Maintenant, après avoir commenté tous ces logs, nous nous rendons compte que nous n'avons pas encore trouvé l'erreur.

Nous voulons donc les remettre en action.

Pour les utilisateurs de Mac, vous ferez Option Shift U.

Et pour les utilisateurs de Windows, vous ferez Alt Shift U, et cela décommentera tous ces logs Turbo Console Log.

La dernière chose qui reste ici est, vous savez, vous avez fini de déboguer, vous voulez vous débarrasser de tous ces `console.log`.

Historiquement, la façon dont je faisais ça habituellement était de les chercher et de les supprimer via une recherche.

Mais avec Turbo Console Log, tout ce que vous avez à faire est d'appuyer sur Option Shift D pour Mac ou Alt Shift D pour Windows.

Et cela supprimera tous les logs d'un seul coup.

Code Runner est une extension VS Code qui vous permet d'exécuter facilement des snippets de code et des fichiers d'un simple surlignage et un clic droit.

Je vais ouvrir ce fichier `loop.py` et vous montrer comment fonctionne Code Runner.

Disons que j'ai cette fonction dans mon code.

Elle s'appelle `create_list`.

Et en gros, elle crée juste un tableau ou une liste de nombres de zéro à neuf.

Je veux vous montrer comment cela fonctionne.

Tout de suite.

Je vais juste imprimer cette liste et utiliser Code Runner : je surligne tout ce code, clic droit, "Run Code".

Cool.

Il m'a montré la liste `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`.

Et disons que dans un scénario pratique, je regarde ce code et je me dis : "Eh bien, je peux en fait refactoriser cela pour que ce soit bien mieux".

Mais d'abord, je veux m'assurer que c'est refactorisé correctement.

Ce que je vais faire, c'est ma refactorisation ; ma refactorisation est une compréhension de liste.

Disons `[i for i in range(10)]`.

Et assurons-nous simplement que cela renvoie la même chose que notre variable finale ici.

Je vais surligner cela à nouveau, clic droit rapide "Run Code", je vois le même résultat pour les deux.

Maintenant, tout ce que je vais faire est de prendre mon code refactorisé, de le mettre dans la valeur de retour et de me débarrasser de tout ce code superflu.

Et aussi simplement que cela, j'ai fait la refactorisation et maintenant je sais qu'elle fonctionne.

Et j'espère qu'après cela, je testerai par rapport à mes tests, et cela confirmera également que ça marche.

Mais j'ai souvent trouvé Code Runner vraiment utile quand j'essaie de faire ces refactorisations rapides.

Et d'obtenir une réponse immédiate sur si ce changement fonctionne ou non.

En tant que développeurs, nous connaissons l'importance des applications et des sites web rapides.

Et l'une des choses qui affecte la performance est la taille de vos bundles.

Une application ou un site web lent peut entraîner un moins bon classement SEO, plus d'utilisateurs quittant vos sites ou applications, et généralement une mauvaise expérience utilisateur.

C'est là qu'Import Cost entre en jeu.

Import Cost vous oblige à regarder la taille de vos paquets JavaScript tiers directement dans votre éditeur.

Et vous pouvez corriger tout import volumineux immédiatement.

Après avoir installé Import Cost, ouvrez un fichier `.js`.

Dans mon cas, j'ai ce fichier `main.js` avec quelques imports tiers.

Ce que je remarque immédiatement, c'est que lodash est mon plus gros paquet, mais je ne prends que cette fonction `forEach`.

Comment puis-je rendre cela plus petit ? Je peux le réduire peut-être en déstructurant ? Non, ça ne change pas vraiment grand-chose.

Import Cost montre que cela n'a pas vraiment fait de différence dans la taille du paquet que j'importe.

Eh bien, utilisons un sous-module pour juste récupérer cette fonction `forEach`.

Et voilà.

Maintenant, c'est descendu à 5,7 kilo-octets.

Et en temps réel, Import Cost me dit que j'ai réduit la taille de mon bundle.

Et cela instaure simplement de bonnes pratiques.

Ainsi, lorsque vous déployez une nouvelle application ou un nouveau site web, vous vous assurez que vos paquets tiers ne font pas gonfler votre bundle.

Prettier est un formateur de code d'opinion pour divers langages de développement web, tels que JavaScript, TypeScript, JSX, etc.

Ma configuration Prettier est réglée de manière à formater tous les fichiers JavaScript lors de leur sauvegarde, ce qui est extrêmement pratique car cela impose un style de code que j'ai personnalisé via mes propres paramètres.

Il y a deux bémols avec Prettier.

Le premier étant que si vous n'aimez pas que votre code soit réécrit (ce qui est essentiellement ce que fait Prettier avec son formatage automatique), vous pourriez ne pas l'apprécier beaucoup.

Il peut aussi être souvent difficile à configurer avec un linter.

Mais une fois configuré, il peut être génial en conjonction avec ESLint, qui est la prochaine extension dont nous allons parler.

Pour commencer, nous allons regarder les paramètres de Prettier, qui dicteront comment Prettier formatera ses propres fichiers.

Sur Mac, vous ferez Command virgule, sur Windows, Ctrl virgule.

Et vous pouvez taper "prettier".

Cela ouvrira tous les paramètres liés à Prettier.

Il y a un paramètre pour les fonctions fléchées, un pour l'espacement des crochets, et ainsi de suite.

Je vais garder les paramètres par défaut pour les besoins de cette vidéo.

Mais si vous avez envie d'utiliser un fichier de configuration personnalisé, vous pouvez le faire.

Ce que nous allons vouloir faire ensuite est de chercher "format on save" ici en haut.

Et vous voulez vous assurer que cette case est cochée.

Cela va essentiellement vous permettre de formater le fichier lors de la sauvegarde en utilisant vos paramètres Prettier.

La dernière chose que je veux aborder avant de vous montrer une démo de Prettier est que j'ai parfois eu du mal à configurer Prettier car une autre extension entrait en conflit avec elle.

Dans mon cas, c'était l'extension Vetur, et j'ai dû la configurer pour lui faire savoir que Prettier serait le formateur par défaut.

Je vais vous montrer comment j'ai fait.

Je vais ouvrir mon fichier `settings.json`.

Et essentiellement ce que j'ai fait, c'est qu'il y a des paramètres Vetur qui définissent un formateur par défaut.

Pour tous les fichiers que je veux que Prettier formate, j'ai spécifié que Prettier est le formateur par défaut pour ce fichier, pas Vetur.

Donc, si vous trouvez que votre Prettier ne fonctionne pas, vous devriez vérifier si l'une de vos autres extensions entre en conflit avec lui.

La dernière chose que je vais faire ici est d'ouvrir ce fichier `calendar.view`.

Et j'ai un tas de code mal formaté.

Je veux formater cela correctement selon les paramètres de ma configuration Prettier.

Je vais sauvegarder ce fichier, et Prettier applique automatiquement tout son style.

Comme vous pouvez le voir, c'est assez fluide et c'est souvent utilisé en conjonction avec le linter ESLint, qui est l'extension suivante.

Le paquet ESLint est un linter et formateur qui analyse statiquement le code JavaScript pour trouver des problèmes.

Ces problèmes peuvent être à la fois stylistiques et liés au code lui-même.

Certains problèmes de code sont des choses comme un nom de variable manquant, ou l'utilisation d'un `let` là où un `const` serait plus logique.

Dans cette vidéo, nous parlerons principalement de l'extension ESLint qui fonctionne avec le paquet ESLint pour vous aider à visualiser les erreurs de linting ainsi que des suggestions sur la façon de les corriger.

L'extension VS Code pour ESLint vous donne des corrections rapides directement dans l'éditeur, ce qui est super utile pour repérer des erreurs ou du code mal écrit en temps réel.

Pour commencer, nous devrons d'abord nous assurer que notre projet possède ESLint, et nous devons aussi nous assurer que le paquet ESLint est installé globalement.

Pour ce faire, vous pouvez exécuter cette commande ici : `npm install -g eslint` pour l'installer globalement.

Dans mon cas, je l'ai déjà installé globalement.

Je vais donc passer à l'étape suivante, qui est d'initialiser mon projet avec ESLint.

Une fois installé globalement, tapez `eslint --init` et on vous demandera comment configurer ESLint pour votre projet.

Dans mon cas, je veux toutes les capacités d'ESLint.

Je vais donc cocher la vérification de la syntaxe, la recherche de problèmes et l'application des styles de code.

Mes modules sont des modules JavaScript.

Le Framework que j'utilise pour l'application de calendrier est Vue.js, mon projet n'a pas de TypeScript.

Il s'exécute dans le navigateur.

Et je veux utiliser un guide de style populaire.

Si vous voulez répondre à des questions sur votre style, vous pouvez le faire. Cela vous permettra de personnaliser ESLint davantage, mais je vais choisir le guide de style Airbnb.

Et la dernière chose que je vais choisir ici est que je veux que mon fichier de configuration soit au format JSON.

Et je veux aussi m'assurer d'avoir toutes les dépendances paires (peer dependencies) installées.

Une fois que c'est fini, ce que nous allons voir sur notre gauche dans l'arborescence des fichiers, c'est un nouveau fichier appelé `.eslintrc.json`.

Et cela contient toutes les configurations dont nous venons de parler.

C'est exactement la configuration que j'ai eue via toutes ces questions.

Et maintenant, ce que je vais vouloir faire, par expérience, c'est ajouter un fichier `.eslintignore`.

Je vais donc faire un `touch .eslintignore` car ESLint va automatiquement linter certains fichiers que je ne veux pas, et le fichier `.eslintignore` va s'assurer qu'ESLint ignore ces fichiers particuliers que j'ai spécifiés.

Je vais donc ajouter le répertoire `node_modules`, je ne veux pas linter `src/assets`, ni le répertoire `public`. Sauvegardez cela.

Et la dernière chose que nous voulons faire est de nous assurer que l'extension ESLint est installée.

Dans mon cas, elle l'est déjà.

Après tout cela, vous pouvez recharger votre fenêtre.

Et vous allez voir ESLint prendre effet.

Ce que vous voyez immédiatement ici, c'est qu'il y a un tas d'erreurs qu'ESLint a détectées.

Je vais en corriger quelques-unes juste pour montrer comment ESLint fonctionne.

Je vais survoler cette première erreur sur la variable `snapshot`.

Cela montre une brève visualisation du problème, vous pouvez aussi cliquer sur "View Problem".

Et cela donnera un message détaillé.

Cela montre aussi la règle ESLint qui fait apparaître cela, vous pouvez cliquer sur cette règle.

Et cela ouvrira le navigateur pour vous montrer la spécification de ce qu'est exactement cette règle dans la documentation d'ESLint.

Nous voyons donc que `snapshot` n'est jamais réassigné, utilisez `const` à la place. D'accord, c'est logique.

Je veux corriger ça rapidement.

Comment faire ? Eh bien, vous survolez à nouveau, il y a cette option "Quick Fix", vous avez plusieurs choix ici : vous pourriez corriger tous les problèmes "prefer-const" d'un coup, ce qui réglerait beaucoup de problèmes dans ce fichier, vous pourriez corriger celui-ci en particulier, ou le désactiver.

Ainsi ESLint ignore simplement cette erreur pour cette fois, vous pourriez afficher la documentation pour le fichier.

Et enfin, vous pourriez corriger les problèmes auto-correctibles (auto-fixable), ce qui s'occuperait d'une grande partie de ce fichier.

Dans ce cas, je vais juste corriger ce problème de constante unique.

Et immédiatement, nous voyons qu'ESLint change ce `let` en `const`.

Et maintenant cette erreur a disparu.

Passons à la suivante, survolons, "Quick Fix", cela va juste corriger tous les problèmes auto-correctibles.

Et vous pouvez voir que la plupart des erreurs ont disparu.

Je sais que cela semble un peu désordonné là tout de suite.

C'est juste parce que j'ai initialisé tout le projet d'un coup.

Mais souvent, les linters sont configurés au début du projet.

Donc en pratique, vous feriez une grande partie de cela pendant la configuration du projet.

Et en temps réel, vous recevriez ces erreurs et vous les corrigeriez simplement.

En général, l'extension VS Code m'a permis de choisir où corriger mes problèmes, mais impose aussi les meilleures pratiques de codage, comme celles que je viens de vous montrer.

La dernière extension dont je veux parler est Docker.

Docker est une plateforme de conteneurisation que les développeurs utilisent pour livrer des applications de manière uniforme à travers plusieurs environnements.

Si vous ne connaissez pas bien Docker en dehors de ce tutoriel, je vous encourage vivement à en apprendre davantage avant de regarder l'extension car cela ne fera pas beaucoup de sens sinon.

Si vous avez déjà téléchargé Docker localement, vous pouvez également installer cette extension.

Elle est publiée par Microsoft et c'est comme ça que vous saurez que vous installez la bonne.

Si vous n'avez pas Docker installé localement, et que vous savez comment l'utiliser, assurez-vous de le télécharger sur docker.com.

Une fois l'extension installée,

L'une des premières choses que vous remarquerez est une nouvelle icône sur le côté gauche, celle de la baleine Docker.

Cela signifiera que vous avez l'installation de Docker et vous verrez ce nouveau panneau latéral qui vous montre diverses commandes que vous pouvez exécuter dans Docker.

Avant d'en venir à ce panneau gauche, nous allons jeter un œil à la palette de commandes.

C'est un endroit où vous pouvez exécuter de nombreuses commandes Docker que l'extension alimente.

Je vais donc charger la palette de commandes et taper "Docker" et vous allez voir de très nombreuses commandes Docker : une commande pour purger (prune) un conteneur, une commande pour ajouter des fichiers Docker à votre espace de travail, une commande pour purger le système et ainsi de suite.

Je veux générer un fichier Dockerfile pour ce dépôt sur lequel je travaille, car je veux conteneuriser mon application.

Tout ce que je vais faire est de taper "Docker" puis "files".

Et je vais avoir deux options : l'une pour ajouter des fichiers Docker à mon espace de travail, ou l'autre pour ajouter des fichiers Docker Compose.

Dans ce cas, je ne travaille pas avec plusieurs conteneurs, je veux juste conteneuriser ce dépôt unique et cette application unique, donc je veux juste un seul Dockerfile.

Je vais donc ajouter des fichiers Docker à mon espace de travail, la première option. Mon application va probablement fonctionner sur une plateforme Node.js.

C'est donc ce que je vais choisir comme image de base ici.

J'ai un fichier `package.json` dans mon dépôt.

Je vais donc choisir cela et accepter le port 3000.

Je ne veux pas inclure de fichier Docker Compose optionnel car je n'en ai pas besoin.

Et ce que nous allons voir sur le côté gauche, quand nous ouvrons notre arborescence, c'est qu'il y aura un Dockerfile nouvellement généré ici, ainsi qu'un `.dockerignore`.

Maintenant, nous pouvons cliquer sur le Dockerfile.

Et nous avons un tout nouveau Dockerfile ici qui devrait nous aider à conteneuriser cette application.

Nous remarquerons aussi que si nous interagissons avec ce Dockerfile, il y a de l'IntelliSense intégré, utilisant l'IntelliSense natif de VS Code.

En gros, si vous allez dans ce Dockerfile et que vous tapez quelque chose comme `RUN`, qui est une commande Docker, l'IntelliSense intégré de VS Code reconnaîtra que c'est une commande Docker.

Et il va vous montrer de la documentation pour cette commande spécifique, ce qui est vraiment cool et pratique tout le temps.

Maintenant, si nous retournons à la baleine Docker, nous allons regarder ce panneau sur le côté gauche.

Et la première chose que nous allons remarquer est qu'il y a un conteneur qui tourne pour moi.

C'est juste le conteneur "Getting Started" qui vient avec l'application Docker Desktop.

Je vais arrêter ce conteneur directement dans mon éditeur VS Code.

Et quand je le survole pour faire cela, j'obtiens une meilleure visualisation des informations concernant ce conteneur particulier, y compris son nom, l'image, les ports sur lesquels il tourne, etc.

Je vais l'arrêter en faisant un clic droit puis "Stop".

Et cela va arrêter le conteneur.

Maintenant, je peux aussi décider que je veux purger ce conteneur, je ne veux pas seulement l'arrêter, je veux m'assurer qu'il a complètement disparu pour nettoyer ma configuration.

Je vais donc purger ce conteneur dans la palette de commandes.

Il va demander "Êtes-vous sûr de vouloir supprimer tous les conteneurs arrêtés ?", je réponds oui.

Et j'ai supprimé ce conteneur "Getting Started".

Maintenant, si vous continuez à regarder le panneau gauche, vous verrez qu'il y a une option pour les images.

Dans mon cas particulier, je n'ai que l'image "Getting Started".

Et si vous développez les images, vous obtiendrez chaque tag d'image. Je n'ai que le tag "latest", c'est pourquoi il n'affiche qu'une seule image.

Vous pouvez aussi configurer votre extension pour qu'elle soit synchronisée avec un registre (registry).

Synchronisée avec un registre Azure.

Beaucoup de gens utilisent AWS et Docker Hub, vous pouvez faire de même.

Et essentiellement, cela vous permettra de pousser vos images Docker directement vers vos registres depuis VS Code.

Et il y a beaucoup d'autres fonctionnalités avancées que vous pouvez utiliser ici dans VS Code grâce à l'extension Docker, comme les volumes, les réseaux et ainsi de suite.

C'est donc vraiment incroyable toute la puissance que VS Code et l'extension en particulier vous donnent avec Docker : une fois l'extension Docker installée dans votre éditeur VS Code, vous bénéficiez de l'IntelliSense intégré.

Avec Docker, vous avez la possibilité d'arrêter et de démarrer des conteneurs directement dans l'éditeur.

Vous avez la possibilité de configurer plusieurs conteneurs en utilisant Docker Compose dans VS Code.

Et vous pouvez aussi interagir avec votre registre sans jamais quitter VS Code.

C'est tout pour cette vidéo.

Si vous avez aimé cette vidéo, n'hésitez pas à mettre un "like" et assurez-vous aussi de vous abonner à Free Code Camp.

Il y a toujours une grande variété de contenus qui sortent.

Et j'ai personnellement appris énormément grâce à eux.

Merci d'avoir regardé.