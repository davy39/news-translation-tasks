---
title: Apprendre à utiliser SPSS pour explorer et analyser des données
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-12T13:34:03.000Z'
originalURL: https://freecodecamp.org/news/spss-full-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/spss.png
tags:
- name: spss
  slug: spss
- name: youtube
  slug: youtube
seo_title: Apprendre à utiliser SPSS pour explorer et analyser des données
seo_desc: 'SPSS Statistics is a software package used for interactive, or batched,
  statistical analysis.

  We just released a full course on the freeCodeCamp.org YouTube channel that will
  teach you how to use the popular statistical application SPSS from IBM.

  Thi...'
---

SPSS Statistics est un logiciel utilisé pour l'analyse statistique interactive ou par lots.

Nous venons de publier un cours complet sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à utiliser l'application statistique populaire SPSS d'IBM.

Ce cours fournit un aperçu concis de la manière dont vous pouvez utiliser SPSS pour explorer et analyser vos données afin d'obtenir des informations exploitables.

Barton Poulson a développé ce cours. Barton est professeur d'université et scientifique des données.

Voici les sections de ce cours :

* Introduction
* Versions, éditions et modules
* Prendre un aperçu
* Données d'exemple
* Modèles de Graphboard
* Graphiques en barres
* Histogrammes
* Nuages de points
* Fréquences
* Statistiques descriptives
* Explorer
* Étiquettes et définitions
* Saisie des données
* Importation des données
* Regroupement hiérarchique
* Analyse factorielle
* Régression
* Prochaines étapes

Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/ZpwZS3XnEZA) (2 heures de visionnage).

%[https://youtu.be/ZpwZS3XnEZA]

## Transcription

(générée automatiquement)

Vous allez apprendre à connaître l'application statistique populaire SPSS d'IBM.

Ce cours du professeur d'université Burton Paulson vous montrera comment vous pouvez utiliser SPSS pour explorer vos données afin d'obtenir des informations exploitables.

Bienvenue dans SPSS, une introduction.

Je suis Martin Paulson.

Et dans ce cours, nous allons examiner ce programme statistique SPSS et certaines de ses fonctionnalités de base, et vous donner une idée de ce qu'il peut faire et de la manière dont il pourrait fonctionner dans votre propre travail de données.

Maintenant, SPSS, le nom mérite une petite explication.

Il fut un temps où cela signifiait un package statistique pour les sciences sociales.

Maintenant, c'est juste SPSS.

Mais c'est son origine.

Une chose importante à savoir est à quel point SPSS est populaire.

Voici un graphique qui provient du excellent site web are for stats.com.

Et ce qu'il montre, c'est le nombre d'articles universitaires publiés en 2015, utilisant divers packages et langages statistiques.

Et nous pouvons voir ici que SPSS Statistics est en tête.

SPSS est numéro un, et de loin en termes de recherche universitaire.

De plus, vous pouvez regarder les offres d'emploi.

Voici un autre graphique qui provient également de notre site for stats Comm.

Et ce que cela montre, ce sont les annonces d'emploi en analyse sur indeed.com.

En 2015, une source majeure d'emplois technologiques, SBS est sur la liste, mais cette fois, vous voyez, il est en fait beaucoup plus bas, il est numéro six.

Et donc il y a une différence ici, entre la publication académique et l'emploi dans l'analyse.

Ce que cela vous dit vraiment quelque chose sur la population ou le public pour SPSS, le public principal de SPSS est les chercheurs académiques, surtout dans les sciences sociales, mais dans d'autres domaines comme les affaires.

Maintenant, il y a quelques raisons pour lesquelles SPSS est populaire dans ces domaines.

Numéro un, il est convivial.

C'est une interface de type pointer-cliquer, qui vous permet d'assembler du code très rapidement.

Vous pouvez sauvegarder ce code dans ce qu'on appelle un fichier de syntaxe.

Et ensuite, vous pouvez le réutiliser, vous pouvez l'adapter et vous pouvez le partager avec d'autres.

De plus, SPSS est vraiment bien adapté pour les données provenant d'expériences, où vous comparez des moyennes via des tests t et l'analyse de variance, plusieurs options importantes comme les tailles d'effet et l'analyse de puissance intégrées.

Et donc ce sont quelques-unes des raisons de la popularité de SPSS, surtout dans la recherche académique.

En ce qui concerne ceux qui peuvent dire quelques choses.

Numéro un, SPSS, malgré avoir été développé il y a environ 40 ans, est toujours populaire.

Il a une interface facile à utiliser.

Et il est facile de sauvegarder et de réutiliser la syntaxe, vous donnant une base de code pour le travail que vous faites dans SPSS.

La première chose dont nous devons parler dans SPSS et l'introduction est la configuration et la préparation pour faire le travail.

Pour ce faire, cependant, nous devons prendre une minute et parler des versions, des additions et des modules, qui font tous référence à différents types de choses dans SPSS.

Le choix me fait vraiment penser à une pléthore de possibilités qui s'offrent à vous.

Et c'est bien de le décomposer un peu.

Donc les choses dont nous allons parler sont les versions, ce sont les mises à jour de publication, l'ancienne version une version deux additions, celles-ci varient selon ce qui est inclus dans un achat particulier.

Et les modules sont des fonctions supplémentaires que vous pouvez obtenir pour ajouter aux capacités de SPSS.

Nous commencerons par parler des versions.

La version un est sortie en 1968.

Et à ce moment-là, elle s'appelait statistical package for the social sciences SPSS version 24 est sortie en 2016.

Et maintenant elle s'appelle IBM SPSS Statistics, comme si SPSS ne signifiait rien.

Maintenant pour ce cours, j'utilise la version 22 sur un ordinateur Macintosh.

Heureusement, il n'y a pas eu de changements extraordinairement majeurs entre la version 22 et la version 24.

Et tout ce que je vais vous montrer dans ce cours fonctionnera très bien dans presque toutes les autres versions de SPSS.

Maintenant, il est possible que vous ayez entendu parler de quelque chose appelé p a s, w à un moment donné, et SPSS a brièvement été appelé logiciel d'analyse prédictive.

Lors d'un litige de marque après que SPSS ait été racheté par IBM, cela n'a duré qu'un an ou deux et cela a été résolu.

La chose importante à savoir est que, quelle que soit la version que vous utilisez, les fichiers sont généralement très compatibles entre les versions.

Et donc le code que vous avez créé dans la version 16 est probablement lisible dans la version 24.

Il y a quelques problèmes de compatibilité ascendante pour les fonctions avancées comme la modélisation automatique et ainsi de suite.

Mais la plupart sont cohérents tout au long.

Maintenant, nous devons également parler des éditions de SPSS.

Et il y a quelques choix majeurs ici.

Il y a l'édition de base, l'édition standard, l'édition professionnelle et l'édition premium.

Et elles diffèrent par le prix.

Et elles diffèrent par les fonctions qui sont incluses avec chaque édition.

Par exemple, dans la base, vous obtenez des statistiques de base, vous obtenez la régression linéaire, vous obtenez le regroupement et l'analyse factorielle.

D'autre part, le standard ajoute à cela la régression logistique, les modèles linéaires généralisés et l'analyse de survie.

Il ajoute également des tableaux interactifs par glisser-déposer.

L'édition professionnelle ajoute à cela la préparation des données, la prévision des arbres de décision et les méthodes d'imputation.

Et enfin, l'édition premium de SPSS ajoute le bootstrapping, l'échantillonnage complexe, les tests exacts et la modélisation d'équations structurelles.

Et ainsi, chacune ajoute un certain nombre d'autres fonctions.

Maintenant, voici les prix des produits en août 2016.

Et vous voyez, par exemple, que SPSS commence dans la base à 1 170 $ par an et par personne.

Donc c'est une licence annuelle.

Et cela va jusqu'à près de 8 000 $ par utilisateur et par an.

Et donc cela devient vraiment cher.

Cependant, je veux dire ceci, ne paniquez pas.

Il existe d'autres moyens, en dehors de devoir vendre votre maison pour obtenir SPSS.

Numéro un, il y a un essai gratuit.

Et vous pouvez télécharger SPSS et l'essayer pendant 14 jours.

Et pendant ce temps, la meilleure façon de faire est de voir si vous pouvez faire un cas d'affaires et faire en sorte que quelqu'un d'autre l'achète pour vous.

Il existe également des prix académiques, des prix étudiants pour SPSS à partir de 35 $ pour six mois.

Ce n'est pas la version super duper, mais elle est absolument suffisante pour faire la majorité de la recherche académique.

Maintenant, nous devons également parler des modules.

Et ce sont les composants qui ajoutent des fonctionnalités supplémentaires à SPSS.

Et ce sont les choses qui différencient principalement les différentes éditions.

Les modules de reformulation des modules disponibles incluent les statistiques avancées, le bootstrapping, les catégories et les échantillons complexes, peuvent être des tableaux personnalisés, la préparation des données, les arbres de décision, le marketing direct, les tests exacts, la prévision, les valeurs manquantes, les réseaux de neurones et la régression.

Donc, ce sont 14 modules supplémentaires.

Et cela semble beaucoup, mais si vous pouvez le comparer aux 9000 packages disponibles pour notre, il y a une différence.

L'autre différence majeure est que ces packages coûtent de l'argent, vous devez donc les intégrer dans votre budget.

D'autre part, il existe également des plugins gratuits qui permettent d'utiliser du code en R, Python, Java et le framework Microsoft dotnet dans SPSS.

Donc, il y a des capacités que vous pouvez ajouter en fonction de vos besoins.

D'une certaine manière, nous pouvons dire ceci.

SPSS a une longue histoire en tant que logiciel statistique, il existe plusieurs variations et reformulations supplémentaires.

Il existe plusieurs variations et additions que vous pouvez lui apporter en ajoutant des modules supplémentaires.

D'autre part, cela peut être très coûteux, donc c'est quelque chose à considérer lorsque vous faites l'analyse coût-bénéfice de SPSS.

La prochaine étape dans SPSS, une introduction et une configuration, consiste simplement à regarder SPSS et à voir à quoi ressemble le programme.

Et le moyen le plus simple de faire cela est de l'ouvrir simplement.

Lorsque vous ouvrez SPSS pour la première fois, vous obtenez cet écran de démarrage introductif.

Cela vous donne l'opportunité d'ouvrir certains fichiers, des fichiers récents et d'en apprendre davantage sur diverses choses que vous pouvez obtenir de SPSS.

Si vous le souhaitez, vous pouvez cliquer sur cette case, ne pas afficher cette boîte de dialogue à l'avenir, puis vous n'aurez plus à vous en occuper, vous pouvez également simplement appuyer sur Annuler.

Et cela vous amène à la fenêtre de données dans SPSS, qui a beaucoup en commun avec une feuille de calcul.

Elle a ces lignes et colonnes, où vous avez une ligne par cas et une colonne par variable.

Mais il y a une différence très importante entre SPSS et une feuille de calcul.

Pour démontrer cela, je veux ouvrir un ensemble de données que j'ai utilisé récemment.

Et lorsque cela s'ouvre, vous voyez qu'il ressemble à une feuille de calcul, nous avons les noms de variables en haut, nous avons les numéros de ligne en bas et nous avons des données au milieu.

Maintenant, une différence importante entre la fenêtre de données de SPSS et une feuille de calcul est celle-ci.

Vous avez une vue de données, mais vous avez également quelque chose appelé une vue de variable.

Et c'est le même ensemble de données, mais si nous cliquons dessus, nous le voyons différemment.

Chacune des variables a des métadonnées qui lui sont associées.

Par exemple, l'âge, il vous indique le type de temps de la variable.

Maintenant, ceux-ci sont principalement numériques, il y a une variable de chaîne.

Mais vous pouvez voir qu'il y a beaucoup de choix ici, numérique commun point, et ainsi de suite.

Vous pouvez également spécifier la largeur de la variable, le nombre de décimales.

Et puis une chose vraiment importante qui rend SPSS différent de la plupart des autres programmes est l'utilisation des étiquettes.

Cette colonne ici montre les étiquettes des variables.

Et l'idée est que nous avons un nom de variable court d'un mot ici à gauche.

Et si vous utilisez une très ancienne version de SPSS, ils étaient limités à huit caractères.

Et vous avez fini par avoir parfois des noms très cryptiques, vous n'avez plus tout à fait les mêmes restrictions.

Mais ce qui est courant, c'est de donner un nom court à la variable.

Et puis de lui donner une étiquette, qui est plus descriptive.

De plus, vous pouvez avoir des étiquettes de valeur.

Donc, venons ici à marital et cliquons sur ceci.

Et c'est une façon de dire à SPSS que dans cette colonne, zéro signifie non marié et un signifie et marié.

Évidemment, vous pouvez les faire quand vous voulez.

Et lorsque vous revenez ici, vous avez l'option de les voir.

Donc, je vais venir ici.

Et je vais cliquer sur celui-ci, qui affichera les étiquettes de valeur, et vous voyez comment elles sont apparues.

Maintenant, je peux les faire disparaître.

Il y avait les variables, si je survole simplement, alors je vois le nom plus long.

En revenant à la vue des variables, vous pouvez également spécifier des valeurs pour les valeurs manquantes, vous pouvez donner la largeur de la colonne, l'alignement, et ensuite vous pouvez spécifier l'échelle de la reformulation.

Et ensuite vous pouvez spécifier le niveau de mesure.

Maintenant, SPSS utilise trois valeurs d'échelle, qui est un niveau mesuré variable intervalle ou rapport ordinal, qui est des données classées, et nominal, qui est des catégories, vous avez également l'option de spécifier si quelque chose est une variable d'entrée, une variable cible, ou les deux.

Et il y a certaines fonctions qui utilisent celles-ci.

Mais la plupart du temps, ce n'est pas un gros problème.

Et vous voyez que dans cet ensemble de données de démonstration, celles-ci n'ont pas été changées du tout.

Donc la première fenêtre dans SPSS est cette fenêtre de données.

Mais il y a plus dans SPSS que cela.

Par exemple, faisons un graphique très rapide, je vais simplement faire un graphique simple ici.

Venez et faites un histogramme de l'âge.

et appuyez sur OK.

Et donc vous voyez, j'ai une interface utilisateur graphique avec des menus glisser-déposer qui me permet d'assembler mes commandes de cette manière, j'appuie sur OK.

Et ensuite, ce que nous obtenons est une autre fenêtre qui s'ouvre, elle est super minuscule ici.

Donc je vais la rendre beaucoup plus grande.

Et c'est la fenêtre de sortie.

Donc c'est une fenêtre séparée, les données sont dans une fenêtre.

Et lorsque vous faites une analyse, vous obtenez une fenêtre de sortie séparée, vous pouvez en fait avoir plusieurs fenêtres de sortie.

Et ce que celle-ci fait, c'est qu'elle contient les graphiques ou toute analyse statistique que nous faisons.

Elle contient également une table des matières ici que vous pouvez réduire ou développer.

Et une chose importante est que je l'ai configurée.

Donc elle montre le code que SPSS génère en arrière-plan pour créer cette analyse.

Et le bon côté de cela est que vous pouvez en fait utiliser ce code et le manipuler directement.

Ce code est appelé syntaxe dans SPSS.

Maintenant, par défaut, SPSS ouvre uniquement une fenêtre de données et une fenêtre de sortie.

Mais vous pouvez également obtenir une fenêtre de syntaxe.

En fait, laissez-moi faire cela, je vais venir ici à Fichier, Nouveau, et syntaxe.

Et c'est une fenêtre très vide.

Mais c'est une fenêtre dans laquelle vous pouvez taper.

Ou vous pouvez également utiliser les menus déroulants pour mettre une commande là.

Donc je vais revenir ici à la commande récente.

Et je l'ai fait histogramme.

Et je pourrais appuyer sur OK à nouveau, mais maintenant ce que je vais faire, c'est que je vais appuyer sur coller.

Et ce que cela va faire, c'est obtenir le code pour ce graphique.

Et il va le mettre ici.

En fait, c'est la partie que nous utilisons.

Et si je sélectionne cela, je peux appuyer sur Exécuter, je peux également faire Commande ou Ctrl R, cela exécute la sélection, et vous verrez que nous obtenons à nouveau la fenêtre de sortie.

Et cela a fait exactement la même chose une deuxième fois.

Mais cette fois, cela l'a fait à partir d'une fenêtre où je suis en mesure d'avoir le texte.

Maintenant, beaucoup de gens sont mal à l'aise avec la syntaxe, et ils aiment les menus glisser-déposer.

Mais une chose vraiment importante à ce sujet est qu'elle vous permet de sauvegarder votre analyse.

Donc vous pouvez la répéter à nouveau, sans avoir à passer par tous les menus.

Vous pouvez simplement coller la syntaxe des dialogues dans un fichier de syntaxe, et ensuite vous pouvez la répéter autant de fois que vous le souhaitez.

C'est aussi vraiment facile de modifier les choses lorsque vous le faites de cette manière.

Et les fichiers de syntaxe sont simplement des fichiers texte.

Ils sont sauvegardés avec une extension dot SPSS, mais ils se lisent comme des fichiers texte.

Maintenant, ce sont les éléments les plus importants de l'environnement SPSS, la fenêtre de données avec à la fois les données et la vue des variables, les fenêtres de sortie et les fenêtres de syntaxe qui vous permettent de sauvegarder la commande.

Et c'est ce qui donne à SPSS à la fois une partie de sa flexibilité et de sa puissance.

Et à mesure que vous devenez plus à l'aise, en passant d'avant en arrière entre ces différentes fenêtres, et en voyant ce que vous êtes capable de faire, à la fois avec les glisser-déposer et en tapant du texte, vous découvrirez qu'il y a une grande quantité de flexibilité et de puissance dans SPSS qui vous permet de faire les analyses dont vous avez besoin et d'obtenir les informations que vous souhaitez à partir de vos données.

Nous allons continuer notre introduction et notre discussion sur la configuration dans SPSS en examinant les données d'exemple qui font partie de l'application SPSS.

La chose vraiment agréable à ce sujet est qu'elle vous permet de commencer maintenant à travailler avec des choses et à voir comment SPSS fonctionne.

La partie difficile, cependant, est qu'elle est totalement cachée.

Et donc vous devez savoir où chercher afin d'utiliser les données d'exemple.

Maintenant, si vous êtes sur un Macintosh comme moi, alors ce sera dans votre dossier Applications sous IBM SPSS Statistics 22 ou quelle que soit la version que vous utilisez, puis échantillons et ensuite en anglais, puis vous les aurez.

Dans Windows, c'est un peu différent.

Ce sera C program files, IBM SPSS Statistics 22, ou quelle que soit la version que vous avez échantillons et ensuite anglais.

Donc vous devez naviguer manuellement jusqu'à cela afin de pouvoir trouver ceux-ci.

Mais lorsque vous le faites, vous verrez un tas de fichiers là.

Maintenant, il y en a quelques-uns en particulier qui sont importants.

Il y a les fichiers dot s, a V.

Ce sont des fichiers de données au format propriétaire SPSS, ils ne peuvent être ouverts que dans SPSS.

Habituellement, il y a aussi des fichiers dot SBS.

Et ce sont des fichiers de syntaxe SPSS.

Ce sont des fichiers texte avec les commandes qui peuvent exécuter un certain nombre d'analyses et de graphiques et d'autres fonctions dans SPSS.

Maintenant, nous pouvons l'essayer dans SPSS, en vous faisant ouvrir la fenêtre sur votre ordinateur, et en ouvrant un fichier appelé demo dot save.

Mais laissez-moi vous montrer comment cela fonctionne.

Lorsque vous naviguez vers le dossier avec les fichiers d'exemple SPSS, encore une fois, il est caché plusieurs couches plus bas.

Ce sont les fichiers que vous trouverez, ce sont les fichiers de données dot shp.

Et ce sont les fichiers de syntaxe dot SPSS.

Maintenant, il y a d'autres choses là-dedans, il y a quelque chose appelé un plan CSA.

C'est un plan d'analyse.

Il y a un fichier XML, et il y a quelques autres choses là-dedans.

Mais la majorité de ce avec quoi nous voulons traiter, en fait, reformuler.

Mais les seuls que nous allons traiter sont les fichiers dot shp, et éventuellement les fichiers dot SPSS.

Faisons défiler ici jusqu'à ce que nous trouvions demo dot Save.

Maintenant, veuillez noter, il y a beaucoup d'autres fichiers de démonstration autour de cela.

Donc vous voulez celui-ci en particulier demo dot shp parce que c'est le fichier SPSS.

Je vais double-cliquer dessus.

Et SPSS ouvre le fichier.

Maintenant, vous pouvez configurer SPSS pour qu'il n'ait qu'un seul fichier de données ouvert à la fois, ou vous pouvez en avoir plusieurs, je vais fermer ce fichier vide ici.

Mais voici notre fichier de démonstration.

Et cela nous permet de commencer à travailler avec un grand nombre d'analyses et de voir comment elles fonctionnent.

En fait, j'utiliserai ce fichier tout au long de ce cours entier, car il vous permet de faire un certain nombre d'analyses qui nécessitent des types de données spécifiques.

Et cela est tout configuré.

Donc je vais vous montrer un exemple très rapide, je vais venir ici à analyser, et à explorer.

Et je vais obtenir le niveau d'éducation et le mettre là.

Et donc j'ai une longue liste de variables avec lesquelles je peux travailler.

Ce sont toutes les mêmes variables, il suffit de cliquer sur OK.

Et cela ouvre à nouveau ma fenêtre de sortie, s'ouvre microscopiquement ici dans le coin supérieur.

Donc je vais l'agrandir.

Et maintenant je suis en mesure de commencer à travailler avec mes données d'exemple.

Et cela me permet d'avoir une certaine expérience pratique pour voir comment les fonctions fonctionnent dans SPSS et pour essayer certaines des options et voir comment elles affectent les choses.

Notre prochaine étape dans SPSS et l'introduction est de regarder les graphiques de base car ce sont toujours une bonne première étape dans l'analyse.

Et le moyen le plus simple de le faire dans SPSS est avec quelque chose appelé des modèles de graphiques.

Vraiment, vous pouvez simplement penser à ceux-ci comme des graphiques faciles à réaliser.

L'idée ici est que si vous définissez les niveaux de mesure dans SPSS, alors SPSS considère simplement les graphiques qui seraient appropriés pour ces variables.

Maintenant, en termes de niveau de mesure, rappelez-vous que SPSS utilise le nombre un est nominal pour différentes catégories.

Le nombre deux est ordinal pour les rangs, et le nombre trois est les échelles, c'est pour les mesures de niveau d'intervalle ou de rapport.

Et ensuite, lorsque vous êtes dans les modèles de graphiques, vous avez deux choix de base, vous avez des graphiques de base.

Et ce sont ceux où vous choisissez les variables.

D'abord, celles que vous voulez représenter graphiquement.

Et ensuite, SPSS vous montrera les graphiques suggérés, vous pouvez voir ce que vous voulez faire avec eux.

Il y a également une option pour détaillé et c'est là que vous choisissez d'abord le style de graphique, puis vous choisissez les variables qui y entrent.

Maintenant, ceux-ci ne sont pas exclusifs, vous pouvez passer d'un onglet à l'autre, et ce sera plus facile à voir comment cela fonctionne.

Si nous allons simplement à SPSS, si vous êtes connecté à data lab.cc, alors vous devriez être en mesure de télécharger les fichiers d'exercice à partir de la même page que cette vidéo, ouvrez ce fichier SPSS, oh un, underscore trois underscore un underscore graph board dot SPSS syntax file.

Et voyons à quoi cela ressemble.

Le fichier de syntaxe que vous avez ouvert semble un peu compliqué.

Mais c'est vraiment parce que je veux avoir un enregistrement écrit des mêmes choses que nous allons faire avec les menus glisser-déposer et le graphboard, nous devons ouvrir un ensemble de données.

Et comme je l'ai mentionné auparavant, selon que vous êtes sur un Macintosh ou sur un ordinateur Windows, le chemin vers l'ensemble de données est un peu différent.

Et aussi selon la version que vous utilisez, j'utilise la version 22.

Et donc si vous utilisez autre chose, changez ce nombre là, la plupart devrait être la même.

Et vous pouvez exécuter cette commande et ouvrir l'ensemble de données et l'activer.

Maintenant, je l'ai déjà fait, je vais vous montrer.

Voici mon ensemble de données, c'est le demo dot save.

Et nous pouvons venir ici à Variable View.

Et voir les niveaux de mesure que SPSS a assignés à ceux-ci.

La plupart d'entre eux sont à l'échelle, nous en avons quelques-uns qui sont ordinaux, nous n'avons qu'une seule variable dans cet ensemble de données qui est vraiment codée comme nominale.

Et c'est le genre, qui est en fait une variable de chaîne.

Dans ce cas.

Je vais revenir à cet index.

Maintenant, j'ai une syntaxe plutôt compliquée ici.

Mais ce que vous verrez, c'est que lorsque nous utilisons les menus, c'est en fait assez simple.

La première chose que nous allons faire est de faire un graphique de l'âge.

Mais je vais venir ici à graphs to the graph board template chooser.

Et lorsque je viens à cela, vous voyez que je suis dans cet onglet de graphs de base, et c'est là que je choisis une variable.

Je vais choisir l'âge ici.

Et il recommande trois types de graphiques différents, un graphique en points, l'histogramme et l'histogramme avec une distribution normale.

Nous prendrons le tout premier qui est disponible, le graphique en points, et nous cliquerons sur OK.

Il le place dans la fenêtre de sortie, que je dois maximiser.

Et le voilà, c'est un graphique en points qui ressemble beaucoup à un histogramme de l'âge de l'année.

Donc il descend à 18 ans, il semble monter jusqu'à environ 77 ou 78 ans.

Et c'est un moyen facile de se faire une idée de la distribution avec laquelle nous traitons.

Encore une fois, la commande en texte et en syntaxe est compliquée.

Mais l'interface graphique rend cela très facile à faire.

Revenons à la syntaxe un instant.

Si vous deviez coller la syntaxe de cette commande, c'est ce que vous verriez ici.

Et cette façon de la sauvegarder, vous pouvez la modifier manuellement si vous le souhaitez.

Maintenant, nous allons faire un histogramme de l'âge avec une distribution normale superposée.

Encore une fois, je vais venir à graphs, graph board template chooser.

Et cette fois, tout ce que j'ai à faire est de venir à droite, je clique sur histogramme avec distribution normale, et je clique sur OK.

Agrandissez la fenêtre de sortie.

Et c'est vraiment simple.

Les deux graphiques que je vous ai montrés étaient avec l'âge, qui est une variable de niveau de ratio ou d'échelle dans la terminologie SPSS, nous pouvons également le faire avec des variables catégorielles, j'utiliserai le genre et je ferai un graphique à barres, je reviendrai à graphs, je cliquerai sur GRAPH board template chooser.

Et lorsque je descends à genre, vous verrez que les graphiques recommandés changent car cette fois, il sait que c'est une variable catégorielle.

Maintenant, si j'avais des données GPS, je pourrais les mettre ici, je peux faire un tas de choses différentes, je vais simplement faire un graphique à barres car c'est le plus facile à gérer.

Je cliquerai sur OK.

Agrandissez la fenêtre de sortie.

Voici mon graphique à barres et vous voyez que dans cet ensemble de données particulier, nous avons un nombre presque exactement égal d'hommes et de femmes ou de données à leur sujet.

Maintenant, ce sont les graphiques de base où vous choisissez d'abord la variable et SPSS recommande des graphiques particuliers.

Vous pouvez également faire des graphiques détaillés.

Ce sont ceux où vous choisissez d'abord le style de graphique puis vous remplissez la variable.

Je vais le faire à nouveau pour un graphique en points de $1 du revenu puis vous montrer que c'est vraiment facile à modifier, je vais venir à graphs to graph board template chooser.

Cette fois, je vais aller à l'onglet détaillé, cliquer dessus.

Et je vais faire un graphique en points.

Donc je vais faire défiler cela, vous voyez que nous avons beaucoup de choix.

Choisissez le graphique en points.

Et cela va demander ce que je veux faire un graphique en points.

Je vais cliquer sur cela, et je vais faire défiler jusqu'à revenu.

Voici celui que je veux, le revenu du ménage en milliers.

Je peux cliquer sur OK.

Ensuite, agrandissez la fenêtre de sortie.

Et voici mon graphique.

C'est un graphique très basique, vous voyez que la plupart des gens sont à l'extrémité inférieure, surtout parce que cela représente des centaines de milliers de dollars.

Donc cela va être un million de dollars là.

Mais je veux vous montrer une chose intéressante à ce sujet.

Si nous double-cliquons sur le graphique, cela ouvre la fenêtre d'édition, et l'éditeur de graphboard a quelques options spéciales.

Pour une chose, je peux changer le nombre de décimales ici, je clique simplement sur les décimales, je vais à format et je change le niveau minimum, ou plutôt le nombre minimum de décimales à zéro.

C'est mieux.

Mais la plus intéressante est, si je clique sur les points eux-mêmes, ils sont faits comme des points et le modificateur est de les empiler, il y a quelques autres modificateurs qui peuvent être utiles.

L'un est de les esquiver.

Et ce que cela fait, c'est qu'il les place au milieu en s'étendant dans les deux sens, il peut être un peu plus difficile de faire des comparaisons d'un niveau à l'autre.

Mais c'est un type de graphique intéressant, je peux cliquer dessus à nouveau.

Et nous pouvons faire ce qu'on appelle le jitter avec une distribution normale, et cela prend des points avec la même valeur et les étale de manière aléatoire, de haut en bas.

Et encore une fois, vous pouvez voir que nous en avons beaucoup là en bas.

Un autre choix est le jitter uniforme, qui les maintient dans certaines limites.

Mais il est difficile de dire vraiment combien les choses sont étalées là en bas.

Donc je préfère en fait l'empilement ou je pense que l'esquive est intéressante dans ce cas.

Et c'est une façon d'utiliser le graphboard pour le configurer et ensuite le modifier manuellement en double-cliquant sur le graphique, vous pouvez fermer cela car j'ai terminé avec cela.

Et vous voyez que j'ai la version modifiée juste là.

Maintenant, nous pouvons obtenir beaucoup plus compliqué.

Par exemple, je peux faire un nuage de points de l'âge et du revenu avec des couleurs pour la densité des points.

Il y a beaucoup d'options, et vous pouvez les explorer.

Cette fois, je vais faire un peu différemment, je vais simplement sélectionner cette commande.

Et encore une fois, la façon dont je les ai obtenues était en les configurant dans les menus puis simplement en appuyant sur coller, et cela a mis cet index dans ce fichier d'index, donc je pourrais le sauvegarder et l'exécuter plus tard.

Donc je vais vous montrer comment cela fonctionne.

J'ai la commande ici que j'ai créée en utilisant le graph board template chooser.

Et je vais simplement venir ici et sélectionner Exécuter la sélection.

Et je maximise cette fenêtre.

Et là, vous pouvez voir que j'ai en fait ce qu'on appelle un nuage de points hexagonaux.

Et il montre quelques choses différentes.

Et c'est une manière vraiment sympa.

Donc vous avez beaucoup d'options sur la façon dont vous affichez les choses dans le graph board template chooser.

Et bien que le code soit compliqué, l'interaction avec les menus est vraiment simple.

Vous pouvez être créatif et vous pouvez obtenir différentes vues sur vos données et essayer d'obtenir plus d'informations lors de votre analyse.

La prochaine étape dans notre introduction à SPSS et aux graphiques de base est les graphiques en barres.

Et nous aimons les graphiques en barres pour une raison très simple.

Ils sont simples et simple est bien, ou plus spécifiquement, les graphiques en barres sont les graphiques les plus basiques pour les données les plus basiques, simplement les fréquences pour une catégorie simple.

C'est aussi une commande très basique dans SPSS.

Maintenant, nous avons en fait quelques options sur différents types de graphiques en barres.

Un, nous pouvons faire un graphique en barres simple, donc une seule variable montrant simplement les fréquences de catégorie dans cette variable, deux.

Nous pouvons faire un graphique en barres de groupe où nous le décomposons par une autre variable.

Et puis trois, nous pouvons faire plusieurs variables et montrer les barres simultanément.

Mais essayons cela dans SPSS, c'est vraiment facile à faire, il suffit d'ouvrir ce fichier de syntaxe SPSS, et nous allons l'essayer.

Une fois que vous avez le fichier ouvert, vous devrez ouvrir l'ensemble de données de démonstration et nous l'avons utilisé auparavant.

C'est la commande pour Mac si vous exécutez la version 22 et c'est la commande pour Windows si vous exécutez la version 22, changez simplement le numéro de version si nécessaire.

Une fois que vous avez le fichier ouvert, nous allons faire quelques graphiques en barres.

Maintenant, je vais le faire en venant ici à ce qu'on appelle les dialogues hérités.

Ce sont des dialogues spécialisés, un seul graphique, qui proviennent des versions antérieures de SPSS.

Et franchement, je les utilise habituellement parce que je les trouve si rapides et faciles à gérer, ce que nous allons faire, c'est que nous allons faire un graphique en barres pour les niveaux d'éducation dans notre échantillon.

Donc je vais cliquer sur bar, nous allons faire un graphique en barres simple.

Et nous allons faire des groupes de cas.

Et tout ce que je dois faire est de cliquer sur le niveau d'éducation, de le mettre dans l'axe de catégorie, et de cliquer sur OK.

Et je fais le sortie plus grande.

Le voilà, un morceau de gâteau absolu.

Et c'est aussi une syntaxe très, très simple.

Vous voyez cette syntaxe ici, c'est vraiment pourrait être une ligne.

Et juste à titre de comparaison, voici le même graphique produit avec le constructeur de graphiques.

Mais vous voyez, nous avons ce code vraiment compliqué, écrasant, le graphique hérité produit un moyen extrêmement simple.

Donc c'est un graphique en barres simple, un morceau de gâteau.

Maintenant, faisons un graphique en barres groupées pour des groupes de cas, nous allons regarder les niveaux d'éducation par genre.

Pour ce faire, nous revenons à graphs, legacy dialogues to bar.

Et maintenant, nous allons le regrouper en un niveau d'éducation groupé par genre, je clique sur définir, j'obtiens le niveau d'éducation, c'est notre variable de résultat, je le mets sous l'axe de catégorie, et puis je définis les groupes par genre, je le mets là.

Je vais cliquer sur OK.

Et le rendre plus grand.

Et cette fois, il utilise de plus belles couleurs.

Mais vous avez les cinq niveaux d'éducation décomposés où les femmes sont en bleu, et les hommes en vert.

Mais c'est vraiment facile de voir ici, la relation entre les deux variables.

Et dans cet ensemble de données particulier, il semble vraiment qu'il n'y a pas de différence substantielle entre les hommes et les femmes.

Maintenant, je vais dire que je crois que c'est un ensemble de données artificiel.

Donc nous ne nous attendrions pas à beaucoup de différences.

Mais c'est une belle façon de les comparer.

D'ailleurs, venez ici, et vous verrez que le code pour cela est vraiment simple.

Tout ce qu'il fait, c'est qu'il ajoute par genre.

Donc encore une fois, une commande très courte, je vais revenir à la syntaxe.

Et nous allons en faire une de plus ici.

Et celle-ci est pour plusieurs variables.

Donc c'est une situation dans laquelle cela peut être confus si vous avez beaucoup de catégories dans chaque variable.

Ce que je fais ici, c'est que je vais obtenir les moyennes des variables ou les nombres de uns.

Si vous avez une variable indicatrice où 04 Non, non, 4, oui, c'est une très belle façon de comparer les fréquences de chacune d'entre elles.

Je vais vous montrer comment cela fonctionne.

Nous allons à graphs, nous reviendrons à bar.

Et nous allons faire un simple.

Mais cette fois, nous faisons des variables séparées définir.

Ensuite, je vais venir ici et cet ensemble de données.

Encore une fois, que je crois être fictif, a demandé à beaucoup de gens diverses choses qu'ils pourraient faire.

Nous allons leur demander à propos du service sans fil.

Et nous allons descendre pour savoir s'ils possèdent une machine à fax, car ce sont des données anciennes.

Et cela demande à propos de l'ancienne technologie des bipeurs, je n'ai jamais eu de bipeur.

Mais je sélectionne simplement toutes ces variables, je les mets ici.

Et tant qu'elles sont toutes à la même échelle, cela va faire la moyenne de chacune.

Et sur le 01, la moyenne est la proportion de têtes, d'accord.

Et les voilà, c'est une façon de regarder la distribution de plusieurs variables simultanément.

C'est un affichage très dense en informations.

Et surtout lorsque vous êtes les analystes explorant vos données, cela peut être un moyen vraiment rapide et facile de vous faire une idée de vos données, ce qui peut ensuite diriger vos analyses ultérieures.

Alors que nous continuons à regarder les graphiques de base dans SPSS, un graphique très courant est l'histogramme.

Et c'est un graphique pour les données qui sont quantitatives ou mises à l'échelle ou mesurées, ou de niveau d'intervalle ou de rapport, toutes ces expressions font essentiellement référence à la même chose.

Et dans chacun d'eux, vous allez vouloir faire un histogramme pour voir à quoi ressemble la variable.

Maintenant, j'ai mentionné que SPSS préfère le terme échelle pour ces variables.

Et c'est ce qui apparaît dans les définitions des données.

Et j'aime penser à cela comme les balances de la justice.

Mais pourquoi faisons-nous un histogramme ? Le but est de voir ce que vous avez, de voir à quoi ressemblent les données.

Et il y a quelques choses en particulier que vous allez chercher.

Numéro un, vous allez chercher la forme de la distribution, est-elle unimodale, bimodale, asymétrique, à gauche, à droite ? Y a-t-il des lacunes dans les données ? Cela suggère que peut-être vous avez un mécanisme important en action ou qu'il y a des valeurs aberrantes que vous devez prendre en considération avant de faire votre analyse.

Vos données sont-elles symétriques ? Il y a beaucoup de choses différentes que vous pourriez chercher.

Et certaines d'entre elles auront une grande influence sur vos analyses.

Il est donc important de regarder les données et l'histogramme vous donnera une excellente impression d'une variable quantitative ou mise à l'échelle.

Nous allons l'essayer dans SPSS, il suffit d'ouvrir ce fichier de syntaxe, et nous verrons comment cela fonctionne.

Lorsque vous êtes dans SPSS, la plupart de cela est vraiment juste pour ouvrir l'ensemble de données, c'est le même que nous avons utilisé dans les autres, cet ensemble de données de démonstration.

Et voici le code pour Mac, ajustez le numéro de version si nécessaire, et voici le code pour Windows.

Mais une fois que vous avez l'ensemble de données ouvert, vous pouvez utiliser les commandes et c'est vraiment, vraiment simple.

Tout ce que vous avez à faire est de venir à graphs, nous allons aux dialogues hérités.

Et nous allons descendre ici au bas à histogramme.

Et nous allons faire un histogramme de base de l'âge.

Donc je clique sur cela, et je viens à l'âge, c'est notre première variable.

Et je clique simplement sur cela pour le déplacer et je clique sur OK.

Agrandissez la fenêtre de sortie.

Et voici notre histogramme.

Et à partir de cela, nous pouvons voir que notre distribution est unimodale, nous pouvons voir qu'elle est assez proche de la normale, elle est légèrement asymétrique à l'extrémité supérieure, mais pas beaucoup.

Et ce sera une très bonne variable pour la plupart de nos analyses, car cela signifie que la plupart des hypothèses des types de procédures que nous pourrions vouloir utiliser.

Maintenant, si je veux rendre les choses légèrement plus compliquées, car vous voyez que la commande pour cela est extrêmement simple, nous pouvons faire une petite modification que je vais vous montrer ici, nous pouvons superposer une distribution normale.

Et tout ce que j'ai à faire pour cela est de revenir à graphs, legacy dialogues into histogram.

Et je coche simplement cette case ici display normal curve.

Et ce que cela va faire, c'est créer la même distribution, nous allons simplement mettre par-dessus une ligne de courbe en cloche, une distribution normale qui a la même moyenne et le même écart-type.

Et ici, vous pouvez voir, nous sommes assez proches de la normale.

Et c'est une bonne façon de confirmer cela.

Et encore une fois, le code pour cela est vraiment simple.

Tout ce qu'il fait, c'est qu'il ajoute le mot normal dans cette phrase, et cela nous donne tout ce dont nous avons besoin.

L'une des raisons pour lesquelles j'aime vraiment les dialogues hérités dans SPSS, c'est parce que c'est si concis, si simple, et cela vous donne ce dont vous avez besoin.

Donc vous pouvez vous faire une idée de vos données et avancer.

Alors que nous continuons SPSS et l'introduction dans les graphiques de base, nous devrions examiner les nuages de points, une méthode très courante pour observer les associations, ou comme j'aime à penser, une façon d'évaluer la cohésion dans les données.

En d'autres termes, vous voulez voir ce qui va avec quoi ou plus spécifiquement, quelle variable va avec quelle autre variable.

Les nuages de points sont donc un excellent moyen de visualiser l'association entre deux variables quantitatives.

Lorsque vous créez un nuage de points, il y a certaines choses que vous devez rechercher.

Et au cas où vous vous demanderiez ce qu'elles sont.

Elles incluent, par exemple, si l'association entre les deux variables est linéaire, car beaucoup des procédures courantes supposent que vous pouvez tracer une ligne droite à travers les données, vous voulez vérifier l'étendue des données, surtout si l'étendue change lorsque vous allez de gauche à droite, sur un nuage de points.

Cela s'appelle l'hétérogénéité de la variance et cela peut causer des problèmes avec certaines procédures.

Vous voulez rechercher les valeurs aberrantes, soit univariées.

C'est un score qui est inhabituel sur une seule variable par elle-même.

Ou, dans ce cas, ce qui est encore plus significatif est par variante où vous avez une combinaison inhabituelle de scores.

Et enfin, vous voulez essayer d'avoir une idée de la corrélation ou de la force de l'association entre les deux variables.

Le nuage de points vous permettra de faire tout cela.

Maintenant, dans SPSS, il existe trois types généraux de nuages de points que vous pouvez faire.

Le numéro un est un nuage de points simple.

C'est un graphique x&y binaire, facile à faire.

Le numéro deux est un nuage de points matriciel, où vous avez en fait plusieurs variables, et elles sont simultanées.

Et c'est un bon moyen de regarder les associations complexes entre des collections de variables.

Et le numéro trois, SPSS est capable de faire un nuage de points 3D.

Mais j'aurai quelques mots à dire à ce sujet un peu plus tard.

Mais essayons cela et voyons comment les nuages de points fonctionnent dans SPSS, au moins très basiquement.

Donc, ouvrez simplement ce fichier de syntaxe, et nous pouvons voir comment cela fonctionne.

Lorsque vous ouvrez le fichier de syntaxe, nous avons la même situation où vous pouvez charger les données, nous utiliserons demo dot save.

Et vous pouvez utiliser cette commande si vous êtes sur un Mac utilisant la version 22.

Et cette commande sur Windows version 22.

Mais nous allons simplement faire quelques nuages de points et c'est une commande vraiment basique et facile.

La première chose que nous allons faire est de faire un nuage de points de l'âge et du revenu, venons à graphs, legacy dialogues, et descendons à scatter, voulons utiliser un scatter simple, c'est juste un graphique xy bivarié de base, je vais cliquer sur définir.

Et tout ce que je dois faire ici est de choisir mes variables pour l'axe des x en bas, et l'axe des y du côté, nous allons choisir l'âge pour l'axe des x et le mettre là.

Et le revenu du ménage pour l'axe des y.

Et l'idée est, peut-être qu'il y a une association entre le revenu du ménage et l'âge de la personne.

C'est tout ce que je dois faire, sauf cliquer sur OK.

Et lorsque j'obtiens cela, j'obtiens ce nuage de points de base.

Donc j'ai l'âge en années en bas, j'ai le revenu du ménage en milliers de ce côté.

Et vous pouvez voir, bien sûr, que la plupart des gens sont près du bas.

C'est parce que la plupart des gens gagnent moins de 200 000 $ par an, ce graphique monte jusqu'à 1,2 million.

Nous avons un marqueur qui est un grand cercle vide, il est en noir, et vous pouvez changer les marqueurs.

Et il y a des choses que vous pouvez faire pour nettoyer le graphique.

Mais il est également facile de dire que les gens qui, par exemple, gagnent beaucoup d'argent sont généralement plus âgés.

Donc nous pouvons voir dans ces données, il y a une sorte d'association entre l'âge et le revenu.

Mais essayons d'obtenir une vision plus nuancée en regardant plusieurs variables simultanément avec une matrice de nuage de points.

Revenez à graphs et legacy dialogues.

Et descendez à scatter.

Cette fois, cependant, je vais choisir scatter matrix, cliquez sur définir.

Et maintenant, tout ce que je dois faire est de choisir les variables que je veux inclure, je n'ai pas besoin de spécifier X ou Y, car elles vont toutes servir de X et de Y dans différentes parties de la matrice.

Je vais en choisir quelques-unes ici, je vais prendre le revenu du ménage, je vais le déplacer, je vais prendre l'âge et le déplacer.

D'accord, votre adresse à l'adresse actuelle et la déplacer, je vais prendre reside, qui est le nombre de personnes résidant dans la maison, déplacer cela.

Et enfin, je vais prendre le niveau d'éducation.

Il n'y a rien de particulièrement significatif à propos de ceux-ci, ce sont simplement ceux que je pensais être faciles à regarder.

Maintenant, en tant que recommandation générale, si vous avez une variable qui est une variable de résultat, vous pourriez vouloir la mettre en premier, cela la met dans la première colonne et la première ligne.

Et cela facilite sa recherche lorsque vous regardez vos analyses.

Mais j'ai mes cinq variables là, et je viens, j'appuie sur OK.

Cela prend un moment.

Et puis je viens ici.

Et c'est la matrice de nuage de points.

Et donc vous avez toutes les cinq variables listées sur le côté, vous avez toutes les cinq variables listées en bas.

Donc chacune fonctionne à la fois comme un X et un Y, vous avez des cases vides sur la diagonale, car ce serait chaque variable avec elle-même.

Et la corrélation est toujours de un.

Maintenant, il y a des choses que vous pouvez faire pour nettoyer cela, vous pouvez changer le marqueur d'un grand cercle noir à quelque chose de plus petit et plus facile à voir, vous pouvez mettre des lignes de régression à travers.

Mais il est facile de voir qu'il y a des motifs vraiment importants.

Par exemple, l'âge en années, et les années à l'adresse actuelle ici, évidemment, il y a une limite, vous ne pouvez pas vivre quelque part plus longtemps que vous avez vécu.

C'est pourquoi nous n'avons rien en haut à gauche à ce sujet.

Mais vous voyez certaines associations et certaines coupures qui traversent.

Maintenant, celui-ci est vraiment dense dans beaucoup de situations, il sera beaucoup plus facile de voir les motifs qui s'y trouvent, surtout si vous changez les marqueurs et mettez des lignes de régression.

Mais cela donne une bonne idée de ce que vous pouvez faire avec une matrice de nuage de points.

Maintenant, revenons une fois de plus aux dialogues hérités et à scatter, car vous avez vu qu'il y avait d'autres options là.

Il y a un graphique en points qui est comme un histogramme.

Et il y a un scatter superposé, avec lequel je ne veux pas traiter.

Et puis il y a un scatter 3D.

Et vous pourriez regarder cela et dire, oh, cool, c'est interactif, c'est en 3D, c'est une chose géniale.

Je ne vais même pas le faire.

Parce que chaque fois que j'ai fait un diagramme 3D, je l'ai trouvé, il est impossible de le lire clairement.

C'est très difficile à manipuler dans SPSS.

Et cela finit par être une mauvaise expérience.

Et il est beaucoup plus facile de regarder l'association entre les variables en utilisant une matrice de scatter.

C'est pourquoi je vous recommande d'éviter complètement le 3D, même s'il est disponible ici.

Mais évitez-le complètement.

Et utilisez le bivarié et les matrices de scatter comme moyen de regarder les associations entre les variables dans vos données.

Une fois que vous avez fait les graphiques de base pour vos données et que vous voyez avec quoi vous traitez, il est bon de passer aux statistiques de base.

Et dans SPSS, la version la plus basique de cela est les fréquences.

J'aime penser à cela comme mettre les choses dans des seaux, puis simplement compter ce qu'il y a dans les seaux.

Donc l'idée est que lorsque vous avez un nombre limité de catégories dans vos données, vous devriez simplement compter combien de fois chaque catégorie se produit.

C'est une première étape pour libérer des informations significatives.

Mais attendez, je veux juste mentionner que la commande de fréquences dans SPSS peut faire bien plus que cela.

Et je vais vous montrer comment cela fonctionne.

Par exemple, elle peut faire des graphiques.

Elle peut faire des graphiques à barres et des camemberts et des histogrammes et des distributions normales.

Et elles peuvent faire beaucoup de statistiques au-delà des fréquences, elle peut faire des quartiles, des percentiles, moyenne, médiane, mode, écart-type, variance, asymétrie, kurtosis, et ainsi de suite.

En fait, à cause de cela, j'aime penser aux fréquences comme à la version SPSS du personnage compétent dans la littérature et les films, qui peut tout faire bien.

Vous savez, quelqu'un comme Léonard de Vinci, ou Iron Man qui semble pouvoir tout faire, ou vous savez, Mary Curie ici, parce qu'elle a remporté deux prix Nobel, et l'un du reste d'entre nous.

Mais en tout cas, revenons aux statistiques.

Prenons un peu de temps pour regarder les fréquences et essayons cela dans SPSS.

Ouvrez simplement ce fichier de syntaxe, et nous verrons les choses qu'il est capable de faire pour vous.

Comme toujours, nous devons commencer par ouvrir un ensemble de données, nous utiliserons demo dot save.

Et vous pouvez utiliser cette commande sur Mac ou cette commande sur Windows pour le faire.

Une fois que vous avez l'ensemble de données ouvert, c'est une chose très simple d'obtenir les fréquences.

Maintenant, j'ai la syntaxe sauvegardée ici.

Mais vraiment, c'est plus comme un enregistrement de ce que j'ai fait, parce que j'utilise les menus déroulants pour créer ces commandes.

Donc je vais venir ici aux fréquences et je vais obtenir les fréquences pour le genre et la satisfaction au travail.

Pour ce faire, je viens à analyser deux statistiques descriptives.

Et puis la première option là est les fréquences.

Et ce que je vais obtenir, c'est le genre.

Juste ici, je vais simplement double-cliquer pour le déplacer.

Était-ce une bonne satisfaction au travail, je vais double-cliquer et le déplacer.

Maintenant, ce qui est important, ce sont deux types de variables différents.

Le genre est une variable catégorielle, nominale.

Et la satisfaction au travail ici est une variable mise à l'échelle.

Et donc normalement, vous ne faites pas les mêmes types de choses pour celles-ci.

Mais les fréquences sont très flexibles.

Donc je vais simplement cliquer sur OK, et nous verrons la sortie par défaut pour les fréquences.

La première chose qu'elle nous montre est combien d'observations valides il y a, donc combien de nos 6400 cas ont des données sur ces variables ? La réponse est tous.

Il n'y a pas de données manquantes ici.

Et puis elle descend.

Et elle nous donne des tableaux de fréquences où elle liste chaque valeur, ou un score possible sur la variable, puis dit combien de fois chacune se produit.

Donc pour le genre, nous avons 3179 répondants de sexe féminin, ce qui représente 49,7 %.

Et le pourcentage et le pourcentage valide seraient différents si nous avions des données manquantes.

Mais nous n'en avons pas, donc nous pouvons ignorer cela.

Et puis le cumulatif s'additionne simplement à 100.

Et puis la satisfaction au travail.

C'est une variable mise à l'échelle, qui a 12345 comme réponses.

Et ici, vous pouvez voir combien de personnes ont mis chacune des réponses, 17 % très insatisfaites, 21,8, neutres et 19,1 très satisfaites.

Et c'est un aperçu rapide des fréquences avec lesquelles nous traitons.

C'est aussi une bonne façon de vérifier si vos variables sont bien codées.

Mais ce que nous pouvons faire, c'est plus que cela, nous pouvons aussi désactiver les tableaux.

Et nous pouvons faire des graphiques à barres en utilisant la commande de fréquences.

Donc je vais garder ces deux mêmes variables, le genre et la satisfaction au travail.

Mais cette fois, je vais simplement faire des graphiques à barres.

Je vais revenir à mes commandes récentes et fréquences.

Et ce que je vais faire, c'est que je vais cliquer sur cela, cela va me donner un petit message d'erreur parce que je n'ai pas changé l'autre chose.

D'abord, je vais venir ici aux graphiques.

Je lui dis de faire des graphiques à barres, évidemment, vous pouvez faire des camemberts et des histogrammes aussi.

Je vais cliquer sur Continuer.

Et puis cliquer sur OK.

Et maintenant, la même commande générale, les fréquences ne produisent pas de tableaux, mais elles produisent des graphiques.

Et ici, vous pouvez voir que nous sommes très proches en termes de nombre de répondants masculins et féminins.

Et ici, vous pouvez voir que la satisfaction au travail atteint un pic à neutre et quelque peu satisfait.

Donc c'est une chose vraiment agréable.

Vous n'avez même pas besoin d'utiliser la commande de graphique à barres, vous pouvez le faire directement ici.

Vous pouvez également obtenir plus de types de statistiques.

Par exemple, celui-ci, je vais garder les tableaux désactivés lorsque je vais demander quelques choses supplémentaires.

En fait, laissez-moi revenir à celui-ci.

Nous allons analyser, descriptives et fréquences.

Et cette fois, je vais faire l'âge, résider et job set.

Donc je vais supprimer ma variable catégorielle ici.

Réinitialisez cela, je vais faire l'âge ou l'autre pour résider.

Et job set.

Et puis je pense que c'est celui-ci ici.

Ensuite, nous allons descendre à la satisfaction au travail.

Et nous allons le déplacer.

Donc j'ai trois variables, mais elles sont toutes des variables mises à l'échelle.

Ce que je vais faire ici, c'est d'abord je vais venir aux statistiques.

Et j'ai une gamme vraiment impressionnante de choses que je peux obtenir, je peux obtenir la moyenne, je peux obtenir la médiane, le mode, si vous voulez le mode, je pense que c'est le seul endroit pour l'obtenir dans SPSS, je peux obtenir des valeurs de quartile.

Maintenant, il ne fait pas le minimum et le maximum, vous devez les sélectionner séparément ici.

Mais vous pouvez également obtenir des points de coupure.

Maintenant, un point de coupure est intéressant.

Les quartiles sont des points de coupure, il divise les données en quatre groupes de taille égale avec le même nombre de personnes dans chacun.

Parfois, vous voulez autre chose que cela.

Par exemple, je sais que si vous faites des scores de propension, il n'est pas rare d'utiliser cinq groupes égaux, des quintiles.

Et aussi, il y a des situations où vous voulez non pas les scores les plus extrêmes, mais près des plus extrêmes.

Et donc je vais mettre, par exemple, le 2,5 percentile.

Et le 97,5 percentile, car ceux-ci encadrent les 95 % du milieu des données, je peux aussi obtenir l'écart-type et la variance, la phrase ou autre chose que je veux ici.

Je veux l'asymétrie et le kurtosis.

Je vais cliquer sur continuer, puis je vais revenir à celui-ci, je vais désactiver les tableaux de fréquences, car sinon, j'ai beaucoup de choses différentes possibles ici, j'aurais beaucoup de choses en cours.

Je vais cliquer sur les graphiques.

Et cette fois, je vais demander des histogrammes.

Et nous allons mettre une courbe normale au-dessus de chaque histogramme.

Cliquez sur Continuer.

Et cliquez sur OK.

Et voici ce que nous obtenons.

Il commence par la sortie statistique, voici les trois variables que j'ai sélectionnées, il nous donne la moyenne, l'écart-type, la variance, l'asymétrie et l'erreur standard de l'asymétrie, le kurtosis.

Nous avons les scores minimum et maximum.

Et puis les percentiles.

Maintenant, c'est une liste étrange ici, car j'ai trois choses mélangées, j'ai les quartiles, c'est quelque chose que j'ai demandé.

Donc nous avons le 25e percentile, le 50e percentile, et le 75e percentile.

Ce sont les valeurs des quartiles.

J'avais le minimum et le maximum ici.

Donc ce sont les 0 et 100 % des valeurs des quartiles, mais j'ai aussi demandé des quintiles.

Et donc cela le met à 20 40 60 et 80 %.

Et enfin, j'ai manuellement entré le 2,5 percentile, et puis le 97,5 percentile.

Et donc ils sont tous mis là ensemble, mais c'est vraiment facile de voir les changements dans la distribution.

En dessous, nous avons les histogrammes et nous avons chaque variable a son propre histogramme, ainsi qu'une distribution normale avec la même moyenne que l'écart-type posé sur le dessus, l'âge est assez proche de la normale.

Voici l'adresse actuelle, cependant, vous pouvez voir qu'elle est vraiment asymétrique car la plupart des gens n'ont pas vécu là-bas si longtemps.

Et enfin, la satisfaction au travail est un peu plus plate que ce que nous attendrions si elle était normalement distribuée.

Le but de cela est que je suis capable de faire un travail statistique et graphique énorme en utilisant une seule commande, la fonction de fréquences dans SPSS, l'une des commandes les plus polyvalentes que vous utiliserez jamais.

Dans notre vidéo précédente, nous avons examiné la puissance de la commande de fréquences, mais pour les statistiques de base, un autre choix très courant est les statistiques descriptives dans SPSS.

La bonne chose à propos des statistiques descriptives est qu'elles vous permettent d'atteindre une densité maximale.

C'est-à-dire comment obtenir beaucoup de chiffres sur beaucoup de variables en peu d'espace.

C'est ce que les statistiques descriptives font vraiment bien.

D'autre part, il y a une restriction, cela fonctionne uniquement avec des variables numériques.

Mais c'est beaucoup des données que vous pourriez avoir.

Et si vous avez cela, cela peut vous donner des choses comme la moyenne, la somme, l'écart-type, l'erreur standard, la variance, le minimum et le maximum, la plage, l'asymétrie et le kurtosis.

Maintenant, je dis cela, vous savez, au cas où vous ne vous souviendriez pas, les fréquences font plus, mais ce n'est pas grave.

Il y a certaines choses que la commande de statistiques descriptives fait bien, voici ce qu'elle fait bien, premièrement, elle vous donne une sortie tabulaire très concise et compacte.

Donc c'est vraiment facile de voir un tas d'informations dans un petit espace.

Deuxièmement, c'est un moyen vraiment rapide de trouver des erreurs évidentes dans le codage de vos données.

Enfin, vous pouvez obtenir des proportions pour les variables indicatrices en tant que variables 01 et je vais vous montrer comment cela fonctionne.

De plus, nous avons une fonctionnalité bonus ici dans les statistiques descriptives.

Les statistiques descriptives sont le foyer de la procédure de score Z en une étape secrète de SPSS.

J'ai vu des gens se donner du mal pour obtenir des scores Z en obtenant des écarts-types et des moyennes, vous n'avez pas à faire cela, vous cliquez sur un bouton et c'est fait.

Mais essayons cela dans SPSS et je vais vous montrer comment cela fonctionne.

Ouvrez simplement ce fichier de syntaxe, et nous verrons ce que vous pouvez faire avec les statistiques descriptives.

Nous commencerons comme toujours par ouvrir l'ensemble de données, nous utiliserons demo dot save, voici le chemin sur un Macintosh, en cours d'exécution de la version 22.

Et le chemin sur un Windows également en cours d'exécution de la version 22.

C'est ma première commande, et elle semble vraiment longue.

Mais c'est parce que j'ai beaucoup de variables dedans.

Tout ce que nous devons faire est de venir à analyser, à statistiques descriptives, et descriptives.

Nous cliquons dessus.

Maintenant, l'une des choses qu'il fait est qu'il ne vous montre que les variables qu'il peut analyser.

Donc le genre, qui était une variable de chaîne, ce qui signifie qu'elle n'avait que du texte, n'est pas là.

Mais ce que je peux faire, c'est que je peux simplement les sélectionner toutes et faire une commande ou un contrôle a, puis déplacer tout.

Et ensuite, je vais simplement faire l'analyse par défaut.

Je vais simplement cliquer sur OK.

Et voici notre sortie.

Nous avons un tas de variables, et il nous dit d'abord que le nombre d'observations est de 6400.

Presque tout en bas, cette question sur internet manque certaines données.

Mais cela semble être la seule que nous avons, la valeur minimale et la valeur maximale.

D'ailleurs, c'est là que je parle de la vérification rapide et facile des données.

Si vous avez une variable qui ne doit aller que de un à cinq ou de zéro à un, si vous avez un 17, vous savez que quelque chose ne va pas.

Et donc, en vérifiant simplement les limites extérieures, c'est un moyen rapide de voir s'il y a des erreurs vraiment évidentes, nous avons également la moyenne et l'écart-type, les deux choses dont vous avez généralement besoin, les deux premiers moments d'une distribution.

Et donc c'est beaucoup d'informations.

Et c'est dans un format très concis.

C'est une chose merveilleuse.

Si nous revenons à la syntaxe, je veux mentionner cette chose à propos des variables indicatrices que j'ai dite plus tôt, c'est ceci.

Si vous avez des variables indicatrices qui sont binaires ou dichotomiques, qui n'ont que deux valeurs possibles, et si cette variable est codée comme zéro et un, alors vous pouvez en fait obtenir la moyenne, et cela vous dit quelque chose, cela vous dit la proportion d'observations qui ont des uns.

Et cela fonctionne mieux si vous utilisez le format standard du programmeur, zéro est égal à faux ou non.

Et un est égal à vrai ou oui.

Et étrangement, dans cet ensemble de données particulier, c'est vrai pour la plupart des variables, mais pas pour les dernières ou les deux dans demo dot save.

Et je n'ai aucune idée de pourquoi ils ont changé cela.

Mais c'est quelque chose que vous voulez vérifier dans le codage avant de continuer et de le faire.

Donc si je reviens à la sortie, vous pouvez voir par exemple que la plupart de ces services sans fil jusqu'à possède une machine à fax, ce sont tous des zéros, non.

Et un est oui.

La moyenne ici nous dit que 99 % des personnes possèdent des téléviseurs, neuf six possèdent des magnétoscopes parce que c'était il y a longtemps que 25 % avaient des services de messagerie.

Et j'aime celui-ci, où est l'internet sur cette liste ? 27 % de l'internet parce que cela a été apparemment généré et comme, vous savez, 1990 qui sait quoi ? En tout cas, ce sont des points de données significatifs, la moyenne vous indique cette proportion de uns ou de oui.

Je vais revenir à la syntaxe ici.

Et puis, jetons un coup d'œil rapide aux scores Z.

Maintenant, toute personne raisonnable penserait que le score Z est une transformation des données et donc il devrait être sous le menu transformer.

Mais vous savez qu'il n'y est pas.

Au lieu de cela, il est caché en tant qu'option dans les descriptives.

Donc, revenons aux descriptives, à moins que vous n'ayez l'âge et le revenu, donc je vais réinitialiser cela.

Je vais choisir l'âge.

Et je vais choisir le revenu du ménage.

Et je vais obtenir les deux scores Z car beaucoup de procédures fonctionnent beaucoup mieux si vous avez des scores Z.

Tout ce que vous avez à faire est ceci.

Cliquez sur Enregistrer les valeurs standardisées en tant que variables.

Et si je clique sur OK.

Ce qu'il a fait ici, c'est qu'il me donne les descriptives car j'ai en fait encore exécuté la commande de descriptives pour ces deux variables.

Mais plus significativement, jetons un coup d'œil à l'ensemble de données.

Lorsque je viens à l'ensemble de données, si je fais défiler jusqu'à la fin ici, j'ai deux variables qui n'étaient pas là auparavant, l'âge z, le revenu pansy, et elles ont beaucoup de décimales car vous en avez besoin pour ces scores Z.

Maintenant, je suis rafraîchi.

Dans des circonstances normales, vous voudriez sauvegarder cela dans les données.

Je ne vais pas le faire car c'est l'un des ensembles de données par défaut intégrés de SPSS.

Mais je veux vous montrer que nous pouvons faire une autre chose ici.

Revenons et obtenons les descriptives pour ces scores Z.

Donc je vais venir à analyser, descriptives.

Je vais réinitialiser cela, descendre à voir nos deux nouvelles variables.

Je vais sélectionner, faire un petit clic de décalage pour obtenir les deux et les faire passer ici, puis je vais cliquer sur OK.

Et comme vous vous y attendriez, un score Z a une moyenne de zéro et un écart-type de un.

Et nous n'avons pas eu à le faire manuellement, nous n'avons pas eu à nous souvenir de valeurs, nous n'avons pas eu à arrondir les choses et cela l'a fait exactement pour nous.

Et c'est ce que fait la commande de descriptives, elle fait une sortie tabulaire très concise.

Et elle vous permet également d'enregistrer des scores standardisés ou Z pour une utilisation dans certaines procédures.

Pour un dernier regard dans SPSS sur les statistiques de base, nous allons examiner la commande Explorer.

J'aime penser à cela comme un moyen d'obtenir une vue plus rapprochée, d'obtenir une vue macro sur votre sujet, de vous rapprocher et de voir ce qui s'y trouve en détail.

Maintenant, la commande Explorer va vous donner un tas de statistiques, elle peut vous donner la moyenne et l'intervalle de confiance pour la moyenne.

Et la moyenne tronquée, ainsi que la variance, l'écart-type, l'intervalle interquartile, le minimum et le maximum, la plage, l'asymétrie.

Le kurtosis est une collection d'estimateurs M, qui sont des moyens robustes spéciaux pour mesurer le centre d'une distribution.

Les percentiles, que nous avons vus auparavant, et les listes de valeurs aberrantes peuvent également vous donner une collection de graphiques.

C'est le seul endroit dans SPSS où vous pouvez obtenir un diagramme en tige et en feuilles.

Maintenant, traditionnellement, ce sont des choses qui sont dessinées à la main.

Donc c'est un peu mignon de voir un ordinateur les faire.

Vous pouvez également obtenir des diagrammes en boîte, et vous pouvez obtenir des histogrammes.

Et vous pouvez obtenir un ensemble de graphiques de normalité, tels qu'un graphique QQ ou un graphique QQ détendu.

Et la chose sympa après cela est que vous pouvez décomposer toutes ces analyses par groupes.

Donc essayons cela dans SPSS et voyons comment cela fonctionne.

Ouvrez simplement ce fichier d'index.

Et nous allons parcourir les différentes procédures et explorer et voir comment cela peut s'ajouter à votre propre analyse.

Comme toujours, nous allons commencer par ouvrir l'ensemble de données demo dot save.

Voici la commande pour un Mac, voici la commande pour Windows.

Maintenant, encore une fois, je sauvegarde cela en tant que syntaxe, ce qui le rend répétable, et cela signifie que vous pouvez le télécharger et essayer de l'exécuter vous-même.

Mais j'ai créé tout cela en utilisant les commandes de menu.

Commençons par faire une analyse par défaut d'exploration pour quelques variables.

Je vais venir à analyser, à descriptives, et puis nous allons venir ici à explorer.

Et ce que nous allons faire, c'est l'âge et la catégorie de revenu.

Et encore une fois, c'est un peu intéressant, car ce sont des types de variables différents.

L'âge est une variable scalaire.

Et la catégorie de revenu dans ce cas est une variable ordinale.

Je vais simplement laisser toutes les valeurs par défaut telles qu'elles sont et cliquer sur OK.

Et voici ce que nous obtenons de cela.

Tout d'abord, nous découvrons s'il y avait des cas manquants, il n'y en avait pas dans cette situation.

Et puis nous obtenons une collection de statistiques descriptives pour celles-ci, nous avons d'abord pour l'âge, puis pour la catégorie de revenu, nous avons la moyenne avec l'erreur standard, les intervalles de confiance, la moyenne tronquée à 5 %, la médiane, la variance, l'écart-type, le minimum, le maximum, la plage, l'intervalle interquartile, l'asymétrie et le kurtosis, ainsi que leurs erreurs standards.

Donc il y a beaucoup d'informations là.

Et nous faisons défiler, nous trouvons les mêmes types d'informations pour la catégorie de revenu en milliers.

Maintenant, rappelez-vous, certaines de ces informations ne sont pas celles que vous voudriez normalement utiliser car la catégorie de revenu dans ce cas n'est pas une variable mise à l'échelle.

Et beaucoup de ces choses comme le minimum, le maximum et la moyenne tronquée fonctionnent mieux avec une variable mise à l'échelle.

Mais SPSS est capable de faire fonctionner tout cela.

Donc interprétez avec prudence.

Ensuite, nous descendons et regardons, nous avons un graphique en tige et en feuilles, où il s'agit de l'âge, qui dans notre échantillon est des nombres à deux chiffres.

Et donc cela signifie 118.

Et chacune de ces feuilles, chacun de ces nombres ici représente 10.

cas. Rappelez-vous, nous avons 6400 cas, nous avons environ 640 nombres ici.

Et vous pouvez voir par exemple, que les années 30 semblent vraiment courantes à la fin des années 30.

Et que nous allons jusqu'à quelqu'un dans la fin de la soixantaine.

Et donc c'est un moyen facile de voir ce qui se passe.

Simultanément, nous obtenons un diagramme en boîte.

Et le bon côté de cela est que vous pouvez dire vraiment rapidement s'il n'y a pas de valeurs aberrantes sur l'âge, pas dans cet ensemble de données particulier.

Nous faisons la même chose avec la catégorie de revenu.

Et le graphique en tige et en feuilles a l'air bizarre, mais c'est parce qu'il n'y a que quelques valeurs possibles, un ou deux ou trois ou quatre.

Et il le dessine de manière à ce qu'il ait l'air un peu bizarre.

Mais nous pouvons descendre et obtenir le diagramme en boîte également et voir qu'il n'y a pas de valeurs aberrantes, du moins sur ce type de variable.

Encore une fois, ce n'est pas normalement quelque chose que vous feriez avec une variable de rang.

Mais c'est possible ici.

Maintenant, la chose sympa est qu'il y a des statistiques supplémentaires.

Je vais faire la même chose avec les statistiques.

Mais je vais cocher beaucoup d'options que j'ai ici.

Donc, revenons à ce dialogue, je vais à explorer.

Ce que je vais faire, c'est que je vais dire, donnez-moi simplement les statistiques pour l'instant.

Et je vais venir ici, et je vais faire quelques sélections.

Une chose, bien que les intervalles de confiance à 95 % soient de loin les plus courants, j'ai vu des situations significatives où les gens utilisent un intervalle de confiance à 80 %, donc vous pouvez le changer si vous voulez.

Ensuite, je peux obtenir tous les estimateurs.

C'est une collection complète, je peux obtenir une liste de valeurs aberrantes et une liste de valeurs de percentile.

Je clique sur Continuer.

Et je clique sur OK.

Et maintenant, nous avons le même tableau que nous avions avant.

C'est leurs descriptives en haut, puis nous avons les estimateurs M.

Et cela concerne différentes mesures robustes du centre.

Encore une fois, elles essaient toutes de nous donner quelque chose d'équivalent à la moyenne.

Et vous voyez dans ce cas, l'estimateur de Huber, les estimateurs de poids de Turquie, et l'onde d'Andrews, les nombres sont tous assez similaires.

Je veux dire, cela va d'un minimum de 41, point 18 à un maximum de 41,5 à quatre, ils sont tous vraiment proches.

Et chacun de ces estimateurs a des paramètres spécifiques qui y entrent, vous ne pouvez pas les ajuster dans la boîte de dialogue.

Mais laissez-moi juste revenir à la syntaxe pendant une seconde.

Vous voyez ici, ce sont les paramètres pour chacun des estimateurs EM, vous pourriez les changer ici, si vous voulez le faire.

Je vais revenir à la sortie.

Ensuite, nous avons les percentiles 5 10 25, jusqu'à 95.

Et puis il nous donne les numéros de cas pour les cinq cas les plus élevés et les plus bas sur chaque variable.

Et donc c'est un moyen vraiment agréable de voir une image multidimensionnelle de nos données.

Maintenant, en termes d'images, et même de meilleures façons de faire cela avec plus de graphiques.

Donc laissez-moi revenir à la syntaxe pendant une seconde.

Et vous voyez que nous pouvons obtenir quelques graphiques supplémentaires, je vais utiliser à nouveau l'âge et la catégorie de revenu.

Mais je vais changer ce qu'il nous dit.

Donc, tout d'abord, je vais dire, donnez-moi juste les graphiques, nous n'allons pas obtenir de statistiques, je viens au menu des graphiques, je dis bien, nous avons une tige de feuille par défaut, obtenons un histogramme.

Obtenons également des graphiques de normalité.

C'est un moyen d'évaluer à quel point vos données correspondent à une distribution normale.

Je vais cliquer sur Continuer.

Et Okay.

Maintenant, j'ai un histogramme pour l'âge, le graphique en tige et en feuilles.

Mais celui-ci est normal.

Mais celui-ci est nouveau.

C'est un graphique qq normal ou quantile quantile de l'âge en années.

Et si c'était normalement distribué, tous ces cercles tomberaient exactement sur cette ligne.

Vous voyez, c'est vraiment proche, mais cela dévie à chaque extrémité.

Et puis un graphique qq détendu prend cette ligne, l'aplatit et il est beaucoup plus facile de voir où se trouvent les changements.

Maintenant, je sais que cela semble vraiment grand dans ce cas, mais cette variable est en fait assez proche de la distribution normale.

Ensuite, nous avons notre diagramme en boîte.

Et puis nous faisons la même chose pour le revenu, nous commençons par un histogramme, notre graphique en tige et en feuilles.

Et notre graphique qq normal, encore un peu bizarre, parce qu'il n'y a que quatre valeurs possibles dans cet ensemble de données.

Mais ils tombent tous assez bien sur la ligne.

Et voici notre graphique détendu.

Et puis enfin, le fichier bot que nous avons vu auparavant.

Maintenant, il y a une autre chose que nous pouvons faire avec la commande Explorer.

Et c'est que nous pouvons prendre certaines de ces analyses et les décomposer par groupes.

Donc si nous revenons à la syntaxe, nous verrons que je vais faire le revenu et le décomposer par genre.

Revenons au menu ici.

Mais explorons.

Et je vais réinitialiser cela.

Et nous allons prendre le revenu, et le mettre dans notre liste de variables dépendantes ou de résultats ou la chose que nous prétendez prédire.

Et puis nous allons prendre le genre, faire défiler un peu, il y a le genre et le mettre dans la liste des facteurs.

Ou parfois les gens l'appellent variable indépendante.

Donc c'est si c'est une variable manipulée expérimentalement pour la variable prédictive.

Je vais venir ici et je vais en fait sauter les statistiques et obtenir uniquement les graphiques.

Je ne veux pas une tige et une feuille, mais je vais obtenir un histogramme et obtenir le graphique de normalité.

Et maintenant, parce que je le décompose par groupes, je peux vérifier l'étendue par rapport au niveau avec le test de Levene.

L'idée ici est que les données devraient être étalées approximativement de la même quantité pour chacun des groupes afin que nous puissions les comparer en utilisant certaines statistiques uniformes.

Je vais faire ce qu'on appelle une estimation de puissance ici, cliquez sur Continuer.

Et puis okay.

Et maintenant, ce que nous obtenons, c'est encore une fois une liste du nombre de cas qui ont des données complètes et ensuite, ils le font tous sans données manquantes, nous avons un test de normalité.

Et ce que nous voyons ici, c'est que, sur la base des deux, les données pour aucun des groupes ne sont normales.

Ce n'est pas grave, car nous savions que le revenu était fortement asymétrique positivement.

En ce qui concerne l'homogénéité de la variance, si les deux groupes ont à peu près la même variance ou étendue, vous savez, il y a une certaine différence, mais elles ne sont pas statistiquement significatives.

Et donc il semble être le même pour les hommes et les femmes, ce qui est bien dans cet ensemble de données particulier.

Et puis nous pouvons descendre et voir les histogrammes d'abord pour les femmes.

Et vous voyez, il y a une forte asymétrie.

Et la même chose, encore une fois, pour les hommes, fortement asymétrique, puis nous obtenons les graphiques qq normaux ou quantile quantile.

Et encore une fois, si c'était normalement distribué, tous ces points tomberaient exactement sur cette ligne, elle est fortement asymétrique.

Et donc nous avons cette grande courbe dans les données.

Il en va de même pour les hommes.

Et voici les lignes détendues, où elles devraient toutes être plates sur ces lignes aussi, vous obtenez cette marque de swoosh à la place.

Donc cela confirme simplement que nous ne traitons pas avec des données normalement distribuées, ce que vous voulez avoir, c'est cette grande collection de valeurs aberrantes dans les diagrammes en boîte, je vais faire une chose, je vais double-cliquer sur cela.

Et puis je vais venir ici.

Et cela désactivera les étiquettes de données afin que nous puissions nous débarrasser des numéros d'identification.

Et vous pouvez voir que nous avons beaucoup de valeurs aberrantes dans les deux groupes, les hommes et les femmes, et il n'y a pas de différences vraiment évidentes entre les deux groupes.

Et le graphique de l'étendue par rapport au niveau est quelque chose que vous pouvez utiliser si vous avez plusieurs niveaux, cela peut vous aider à sélectionner un type de transformation de puissance, une racine carrée ou une réciproque, un carré, quelque chose comme cela.

Mais c'est un sujet plus compliqué et quelque chose pour un autre jour.

Et en plus, il semble que nous avons une variance relativement homogène dans les deux groupes.

Donc nous serions bons pour aller de l'avant et faire nos autres analyses.

Donc ce sont quelques-unes des options et explorer.

Et c'est là que nous allons terminer notre discussion sur les statistiques de base, nous pouvons voir comment elles peuvent être utilisées pour voir à quel point vos données répondent aux hypothèses des procédures que vous utilisez, et puis vraiment, à quel point vous pouvez faire des inférences à partir de votre échantillon vers d'autres groupes.

Lorsque vous travaillez dans SPSS et que vous accédez aux données, l'une des choses les plus importantes que vous pouvez faire est de créer des étiquettes et des définitions pour vos données.

J'aime penser à cela comme la version statistique d'Alice au pays des merveilles et la chenille lui demandant de s'expliquer, vous devez vous expliquer ou plus spécifiquement, en ce qui concerne vos données, vous devez dire à SPSS, que signifient vos données.

Maintenant, c'est la description des données, et je vois deux types d'informations que vous dites à SPSS à propos de vos données.

Le premier que je vais appeler la sémiotique, qui vient de l'étude de la signification.

C'est là que vous dites à SPSS, quels sont les noms des variables, les types de données, les étiquettes des variables, les étiquettes des valeurs, les valeurs manquantes, le niveau de mesure, et le rôle que joue chaque variable.

Contrasté avec cela, il y a d'autres éléments que même appeler l'esthétique.

Et cela aborde la largeur des variables, les décimales, la largeur des colonnes, et l'alignement.

Et ce sont tous des paramètres dans la fenêtre de données de SPSS.

L'un des plus importants, du moins pour la consommation humaine, va être les étiquettes des variables et des valeurs.

Et donc je vais prendre un peu de temps et parler de celles-ci avec les noms des variables.

C'est ce que sont les noms courts, ceux que vous avez là en haut de la colonne, il y a des règles importantes.

Donc les règles pour les noms des variables.

Numéro un, les noms doivent être uniques.

Aucune variable ne peut avoir le même nom, cela ne devrait pas être trop surprenant.

C'est un identifiant.

Règle numéro deux, les noms doivent commencer par une lettre.

J'ai mis un astérisque là parce que vous pouvez commencer par un signe ad, un signe livre ou un signe dollar, mais vous ne voulez pas parce que ceux-ci sont généralement réservés pour des fonctions spéciales dans SPSS.

Règle numéro trois, les noms peuvent utiliser des lettres, majuscules ou minuscules, ils peuvent utiliser des chiffres, et ils peuvent utiliser la période, le soulignement, le signe livre, le signe dollar, d'autre part, ne terminez pas par une période, cela peut causer de la confusion avec le terminateur de commande.

Et ne terminez pas par un soulignement parce que cela est utilisé pour les noms de variables automatiques lorsque SPSS fait des calculs.

Règle numéro quatre, les noms ne peuvent pas inclure d'espaces.

Et règle numéro cinq, les noms doivent être inférieurs à 64 octets.

Et la plupart des systèmes de codage de texte, cela représente 64 caractères, mais si vous utilisez un système Unicode, cela pourrait être seulement 32 caractères.

Et la dernière règle, la règle numéro six, les noms ne peuvent pas être l'un de ces mots, tous et par eq GGTL, e, lt et E not or two or with, parce que ce sont tous des noms de fonctions réservés dans SPSS, donc ne créez pas cette confusion.

Donc ce sont les noms courts qui vont en haut d'une variable.

D'autre part, l'étiquette que vous associez à cela, vous pouvez lui donner un nom plus descriptif.

Ce sont les étiquettes des variables.

Et donc il y a quelques règles pour celles-ci.

Règle numéro un, elles doivent être inférieures à 256 octets.

Cela signifie en fait qu'elles pourraient être vraiment longues, bien que vous ne vouliez généralement pas faire cela, car certaines procédures n'afficheront que 40 octets, 40 caractères, et vous voulez vraiment pouvoir lire ce que c'est.

Donc vous voulez le garder court.

Mais vous pouvez aller plus long si vous en avez besoin.

Règle numéro deux, les étiquettes doivent être entourées de guillemets, bien que je vous dise qu'elles doivent être des guillemets droits, les guillemets verticaux, et non les guillemets bouclés, car SPSS s'étouffe avec ceux-ci.

Règle numéro trois, les étiquettes peuvent inclure n'importe quel caractère, y compris les espaces, ce qui est quelque chose que vous ne pouvez pas avoir dans le nom de la variable, mais vous pouvez le mettre ici.

Cela vous permet de mettre des étiquettes qui flottent au-dessus des noms des variables.

Et celles-ci peuvent apparaître dans les listes de variables, elles peuvent apparaître dans les graphiques de la sortie que vous créez.

Une autre chose vraiment importante est les étiquettes de valeur.

Donc vous pouvez avoir une variable appelée genre et vous pouvez mettre des zéros et des uns.

Mais vous vous souvenez de ce que sont ces zéros et ces uns.

Et donc je vais vous montrer quelques façons de gérer cela.

La chose la plus importante est de mettre des étiquettes de valeur dessus.

Donc voici les règles pour les étiquettes de valeur.

Règle numéro un, elles doivent être inférieures à 121 octets.

Donc cela est vraiment long, vous voulez généralement garder vos étiquettes assez courtes.

Règle numéro deux, comme les étiquettes de variable, les étiquettes de valeur doivent être entourées de guillemets, et elles doivent être des guillemets droits et non des guillemets bouclés.

Règle numéro trois, les étiquettes peuvent inclure n'importe quel caractère, y compris les espaces, c'est bien.

C'est intéressant.

Et règle numéro quatre, les étiquettes de valeur n'ont pas besoin d'être uniques, c'est-à-dire que plus d'une valeur peut avoir la même étiquette.

Donc vous pouvez avoir les chiffres de un à neuf.

Et il se peut que 789 disent tous la même chose.

Mais en dessous, ils ont des intérêts de code différents dans des situations où vous pourriez vouloir faire cela.

Mais surtout, je veux vous montrer comment cela fonctionne dans SPSS.

Donc ouvrez simplement ce fichier de syntaxe.

Et celui-ci va être un peu différent, car nous n'allons pas utiliser de fichier de données, je vais me référer à un mais je veux surtout vous montrer la syntaxe.

Ce fichier d'index montre comment écrire des étiquettes de variable et des étiquettes de valeur.

Maintenant, vous n'avez pas nécessairement à les mettre tous décomposés en lignes, je le fais parce que cela les rend beaucoup plus lisibles, c'est beaucoup plus facile de voir ce qui se passe.

La première chose est la commande variable labels.

Parce que c'est une commande SPSS, elle est écrite en majuscules.

Et ensuite, ce que vous faites, c'est que vous écrivez le nom court de la variable.

Et puis vous avez au moins un espace et puis vous avez des guillemets droits, et puis l'étiquette longue.

Donc ici, par exemple, j'ai vair 01, ce serait la première variable.

Et puis voici son étiquette écrite.

Et vous n'avez pas besoin d'avoir quoi que ce soit après, vous n'avez pas besoin de virgules ou de points d'interrogation ou de points-virgules ou autre chose.

Vous passez simplement à la suivante.

Maintenant, je l'ai mis dans une autre ligne, parce que cela le rend facile à suivre.

Et je les fais tous passer par ici, je vais faire une recommandation importante.

Si vous avez une variable dichotomique ou binaire qui n'a que deux valeurs possibles, et le genre pourrait entrer dans cette catégorie.

Permettez-moi de recommander ceci, que vous la codiez comme des zéros et des uns.

Beaucoup de gens utilisent des uns et des deux, mais cela devient confus si vous la codez comme des zéros et des uns, et que vous nommez la variable d'après ce que le un est.

Maintenant, en ce qui concerne les hommes et les femmes, je donne généralement un à celui des deux groupes que je pense avoir le score le plus élevé sur ma variable de résultat principale, donc cela changera.

Mais si pour une raison quelconque, je pense que les hommes vont avoir un score plus élevé sur une variable de résultat, alors je l'appellerai homme et ensuite l'étiquette sera are pour le répondant est un homme.

D'autre part, si je pense que les femmes vont avoir un score plus élevé, alors je vais appeler la variable femme et l'étiquette sera RS femme, je n'utiliserais évidemment qu'une de ces deux.

Maintenant, voici quelques autres exemples.

J'ai tendance à donner des noms génériques tels que variable ou vraiment juste q pour question q un q deux, et j'utilise les zéros de tête pour qu'ils soient stockés correctement dans les boîtes de dialogue.

Et lorsque vous avez terminé la liste de tous vos noms de variables et les étiquettes de variables et les guillemets, terminez simplement par un point, il n'a pas besoin d'avoir d'espace avant, c'est un reste des versions antérieures de SPSS.

C'est une habitude que j'ai.

Donc vous pouvez exécuter cela à tout moment et cela assignera ces étiquettes aux variables et ensuite elles apparaîtront dans le fichier de données, ce qui est bien.

Ensuite, il y a les étiquettes de valeur.

Et ce que vous avez ici, c'est la première commande qui est écrite en majuscules.

Et puis vous donnez une liste de variables auxquelles les valeurs s'appliquent.

Et vous pouvez les lister séparément, très un très deux.

Ici, j'ai un VAR trois sans zéro de tête.

Et puis si elles sont toutes à côté les unes des autres, si elles sont adjacentes, elles peuvent en fait spécifier des plages vair, trois, deux, et majuscules, très tan, donc cela fera 345678 910.

Et puis vous passez simplement à la ligne suivante, et vous donnez la première valeur qui est zéro, et puis je donne zéro égale Non, et un égale Oui, lorsque vous avez terminé de donner les valeurs, vous devez mettre une barre oblique, afin qu'il sache que vous avez terminé avec les valeurs pour cette variable, puis vous pouvez passer à la variable suivante.

J'ai dit, par exemple, si j'ai donné un sur une variable de genre aux hommes, je l'appellerais homme.

Et donc zéro, qui signifierait Non, ils ne sont pas mâles, serait femelle en un, oui, ils le sont ou vrai, ce serait mâle, et faire une barre oblique.

D'autre part, si vous l'avez codé de l'autre manière, et puis vous l'appelez simplement femelle et zéro, ce qui signifie non ou faux signifie qu'ils ne sont pas femelles, ils sont mâles, un signifie qu'ils sont bien.

Évidemment, utilisez juste l'un de ceux-ci, je fais la barre oblique.

Et puis je pourrais avoir une variable de notation, disons, par exemple, beaucoup de gens l'appellent des échelles de Likert, juste une échelle de notation.

Et je pourrais faire rate 01, à rate 10.

Et je peux spécifier chaque valeur.

Donc c'est une échelle de cinq points allant de fortement en désaccord à fortement d'accord, terminé par une barre oblique, ou peut-être avez-vous un type d'échelle différent.

Ici à la fin, j'ai scale 01 à scale 02.

C'est une échelle de 11 points, mais je ne marque que les deux extrémités, le zéro et le 10.

Donc zéro est jamais ou pas du tout 10 est toujours complètement.

Et puis pour faire savoir à SPSS que j'ai terminé de spécifier les étiquettes de valeur, et avec un point.

Donc c'est en fait une seule phrase.

Et c'est une façon de lui dire comment vous voulez que les nombres apparaissent, à la fois dans la fenêtre de données et dans toute sortie que vous obtenez.

Enfin, je vais mentionner quelque chose à propos des valeurs manquantes, car il peut également être plus facile de les spécifier dans la syntaxe, la commande est missing values.

Et vous donnez simplement les noms des variables et vous pouvez utiliser deux de la même manière.

Et puis entre parenthèses, vous mettez le nombre qui est assigné aux valeurs manquantes.

99 est courant.

Donc je l'ai là.

Et puis vous pouvez faire une barre oblique si vous allez utiliser des codes différents après cela, je pourrais faire male à female.

Et ici, je dis deux à high.

Et vraiment, ce que cela signifie, c'est autre chose qu'un zéro ou un est manquant.

Donc si je tape accidentellement un sept, vous savez qu'il est manquant.

Et puis ici, je spécifie plusieurs valeurs différentes, je peux mettre sept, virgule huit, virgule neuf.

Donc si l'un de ceux-ci apparaît, ils seraient considérés comme des valeurs manquantes, faites ce que vous voulez.

La bonne chose est qu'il les exclura automatiquement des analyses.

Mais il les inclura dans les fréquences lorsque vous obtenez cette sortie, terminé par un point.

Et puis vous exécutez simplement celles-ci comme vous le faites pour toute autre commande.

Et cela va faire beaucoup pour clarifier vos données et faciliter le suivi de vos analyses et reconstituer votre travail à l'avenir.

Lorsque vous travaillez dans SPSS et que vous essayez d'accéder aux données, vous pourriez avoir l'idée de saisir des données.

Eh bien, laissez-moi vous dire ce que je pense.

Vous voulez saisir des données dans SPSS, je ne vois cela que comme un exercice de frustration.

C'est une douleur de le faire manuellement.

Et je dirais peut-être que vous saisissez 10 ou 12 nombres, vous savez, essentiellement rien, c'est quelque chose qui est souvent appelé un ensemble de données jouet.

Peut-être pourriez-vous faire cela.

Maintenant, il est également possible de copier et coller des données, mais je vais dire que c'est un peu compliqué car cela ne fonctionne pas vraiment bien, je vais vous montrer cela.

Il est beaucoup, beaucoup plus facile de simplement importer les données à partir d'un fichier CSV ou txt.

Et je vais vous montrer comment faire cela dans la prochaine section.

Mais en termes de saisie de données, laissez-moi vous montrer comment cela fonctionne dans SPSS, nous allons simplement ouvrir un document vide.

Et nous allons l'essayer.

Voici une fenêtre de données vide dans SPSS, je peux venir ici et je peux entrer un nombre.

Et, vous savez, malheureusement si j'appuie sur tabulation, cela descend en fait, ce qui est un comportement inhabituel.

Et vous voyez qu'il lui donne un nom de variable automatique très 00001.

Eh bien, si je veux me déplacer latéralement, j'ai en fait besoin de déplacer la touche flèche droite.

Donc je vais aller de cette façon à trois, et ainsi de suite.

Et puis je peux appuyer sur retour, et cela descend.

Je vais revenir ici et je vais faire 456, je vais appuyer sur tabulation et cela revient au début.

Donc ce n'est pas le comportement le plus intuitif, de plus vous voyez qu'il lui donne ces noms génériques.

C'est parce que vous ne pouvez pas entrer le nom de la variable directement dans cette fenêtre.

Au lieu de cela, ce que vous devez faire est d'aller à la vue des variables, comment y arriver en double-cliquant simplement sur le nom de la variable.

Nous y voilà.

Et vous pouvez entrer le nom de la variable et vous pouvez changer d'autres choses que vous voulez faire.

Cela fonctionne, mais c'est une douleur.

Je vais revenir ici à la vue des données.

Maintenant, j'ai mentionné que vous pouvez importer des données de manière quelque peu.

Donc laissez-moi vous montrer comment cela fonctionne.

Je vais en fait aller à une feuille Google qui n'a rien dedans pour le moment.

Et ici, je vais entrer quelques valeurs, j'ai quelques types différents, je vais faire 5643.

Et je vais entrer un nombre j, retour.

D'accord, donc il y a des données, j'ai des nombres à deux chiffres, et j'ai des lettres, qui seront des variables de chaîne dans SPSS, je vais copier celles-ci.

Et nous allons voir à quel point elles se collent bien dans SPSS.

Donc je vais y retourner.

Je vais venir ici sur le côté.

Et je vais coller celles-ci.

Et vous voyez que les valeurs sont entrées et apparaissent avec des décimales, et je peux m'en débarrasser.

Mais c'est vraiment bizarre avec la variable de chaîne avec les lettres et donc vous pouvez la copier.

Remarquez également, je ne peux pas copier les noms de variables, je dois encore les entrer manuellement, vous pouvez traiter celles-ci lorsque vous importez.

Mais vraiment, c'est une démonstration que mettre des choses manuellement dans SPSS, ce n'est pas un bon environnement pour cela.

Utilisez une feuille de calcul, utilisez Google Sheet, utilisez Numbers, utilisez Excel, n'importe quoi, entrez-le là et puis importez-le.

Je vais vous montrer cela dans la prochaine section.

Et vous verrez que c'est un processus beaucoup, beaucoup plus facile.

La dernière chose que je veux dire dans SPSS à propos de l'accès aux données concerne l'importation de données.

Et vous savez, par rapport à l'entrer manuellement, cela me fait simplement me sentir comme cela et j'ai eu recours à des cliparts ringards pour montrer à quel point je suis heureux.

Parce qu'il n'y a aucun doute à ce sujet.

L'importation est absolument la meilleure façon de procéder si vous voulez obtenir des données dans SPSS.

Maintenant, la bonne chose est que SPSS peut ouvrir des fichiers texte, il peut ouvrir des fichiers CSV ou des fichiers de valeurs séparées par des virgules, et même des fichiers XLS.

x, c'est des fichiers Excel, tant qu'ils sont formatés correctement.

Maintenant, que veux-je dire par formatés correctement ? Il y a un terme de Hadley Wickham dans la communauté des développeurs R, des données bien organisées, et cela fait référence à quelque chose de très spécifique.

Il dit que votre fichier doit avoir une seule feuille.

Donc c'est une feuille de calcul, même si Excel peut en prendre plus, que chaque colonne doit être exactement égale à une variable.

Et que chaque ligne doit être égale à un cas.

Et une chose importante est qu'il n'y a pas de choses bizarres dans votre feuille Excel.

Parce qu'Excel est très flexible.

Et lorsque je fais référence à des choses bizarres, je parle de choses comme des macros, des formules, des graphiques, de la mise en forme, des commentaires ou des cellules fusionnées, ou des en-têtes occupant leurs propres lignes ou dupliquant les numéros de ligne.

Vous ne voulez rien de tout cela, essentiellement, vous voulez le traiter comme un fichier CSV.

Et si vous faites cela, alors vous trouverez que vous pouvez l'importer très facilement dans SPSS.

Et en fait, laissez-moi vous montrer comment cela fonctionne.

Nous allons essayer cela dans SPSS, mais je veux que vous fassiez deux choses.

Tout d'abord, je veux que vous téléchargiez les fichiers du cours.

Et cela inclura un dossier zippé de ce nom qui se termine par des ensembles de données, qui contiendra trois fichiers à l'intérieur.

Je vais vous montrer ceux-ci dans une seconde.

Et puis vous pouvez également ouvrir ce fichier de syntaxe qui fonctionnera avec eux.

Mais allons voir ce qu'il y a dans le dossier et expliquons un peu ce qui va se passer ici.

Le dossier que je vous ai demandé de télécharger contient trois fichiers différents.

Maintenant, j'ai à la fois le dossier ici, et j'ai les trois fichiers sauvegardés séparément à côté, mais normalement ils seraient à l'intérieur.

Mais pour que la syntaxe fonctionne correctement, vous voulez qu'ils soient assis séparément sur le bureau.

Les trois contiennent les mêmes données.

Il dit MBB, qui signifie Mozart, Beethoven et Bach, car ce sont des données Google Trends sur la popularité de la recherche pour chacun de ces trois noms de compositeurs depuis 2004.

Le premier est au format CSV ou valeurs séparées par des virgules.

Le deuxième est un fichier texte brut, et il est séparé par des tabulations.

Et le troisième est un fichier XLS.

x. Donc c'est une feuille Excel.

Et vous pouvez voir que c'est le même nombre mais il apparaît un peu différemment lorsque je fais l'aperçu rapide ici sur mon Macintosh.

Ce que nous allons faire ensuite est d'ouvrir le fichier de syntaxe.

Et nous allons voir ce que nous devons faire pour importer chacun de ceux-ci.

Maintenant.

J'ai sauvegardé cette syntaxe, mais le fait est qu'il est plus facile de faire cela à travers les menus.

Maintenant, je donne quelques informations ici sur l'utilisation du chemin de fichier.

Dans chacune de ces commandes de syntaxe, je dois spécifier l'emplacement du fichier.

Maintenant, c'est le format.

Si vous êtes sur un Macintosh comme moi, bien sûr, vous voudrez changer Bart pour être le nom de votre répertoire personnel.

Si vous êtes sur un ordinateur Windows, vous allez devoir le changer en quelque chose de plus comme ceci, ou éventuellement, selon la version de votre système d'exploitation, en utilisant des barres obliques inverses.

Bref, je vais vous montrer comment importer chacun de ceux-ci.

Et j'ai les informations en double ici dans le script, au cas où vous voudriez l'exécuter de cette manière.

Mais c'est en fait très facile à faire à partir des menus.

Donc voici ce que je vais faire, je vais venir à ma fenêtre de données, je vais simplement cliquer dessus.

Et ma fenêtre de données est vide pour le moment.

Je vais aller à Fichier, Ouvrir, et données, vous faites cela si vous ouvrez un fichier SPSS existant, ou si vous importez quelque chose dans un format différent.

Maintenant, je suis sur le bureau, vous pouvez voir mon dossier là.

Mais vous ne pouvez pas voir les trois fichiers de données que j'ai à côté, car pour le moment, il n'affichera que les fichiers qui sont dans le dot save.

C'est le format propriétaire de données SPSS.

Je vais cliquer dessus, et venir ici.

Et nous allons commencer par le fichier texte, la version txt.

Je vais cliquer dessus et maintenant vous pouvez voir qu'il est là.

Je vais sélectionner ce fichier, et je vais cliquer sur Ouvrir.

Donc maintenant j'ai l'assistant d'importation de texte SPSS.

Et nous pouvons faire défiler la plupart de cela assez rapidement.

Il demande si cela correspond à un format prédéfini, quelque chose qui aurait été sauvegardé ailleurs, ce n'est pas le cas.

Il a demandé s'ils étaient délimités, oui, ou délimités par des tabulations dans ce cas, les variables sont-elles incluses en haut du fichier, vous voyez comment elles apparaissent ici comme la première ligne.

Je clique sur Oui.

Et maintenant, il les exclut car il sait que celles-ci doivent être dans l'en-tête du fichier de données.

Cliquez sur Continuer.

Chaque ligne représente un cas, je veux tous les cas, vous pourriez échantillonner si vous aviez un très grand ensemble de données, ils vous permettraient de faire des analyses exploratoires plus rapidement que vous ne pourriez autrement.

Et c'est ce que les délimiteurs apparaissent.

Maintenant, par défaut, un fichier texte, celui que j'ai utilise des tabulations et il le sait, il demande des qualificateurs de texte, je n'ai pas de qualificateurs de texte ici.

Donc je clique simplement sur continuer, je n'ai pas besoin de changer quoi que ce soit.

Maintenant, j'ai des dates ici au début, et elles sont année-tiret-mois.

Maintenant, SPSS peut gérer les dates, cependant, il n'aime pas le fait que j'utilise l'année et le mois sans le jour qui y est associé.

Par conséquent, je vais le laisser comme une variable de chaîne comme une variable de texte.

Et cela fonctionne toujours correctement dans toutes les analyses que je veux faire.

Donc c'est bien.

Je vais simplement cliquer sur continuer, je ne change rien ici.

Il a demandé si j'aimerais enregistrer le format de fichier pour une utilisation future.

C'est la chose à laquelle je faisais référence dans la première boîte de dialogue ici.

Et c'est si je veux coller la syntaxe, je pourrais le faire.

Mais je l'ai déjà collée, je vais simplement cliquer sur Terminé.

Et le voilà, il l'a ouvert, et il est formaté correctement.

Si nous allons à Variable View, vous pouvez voir qu'il a une variable de chaîne, il a trois variables numériques, il a le bon nombre de chiffres, il a le bon nombre de décimales, et il les reconnaît comme nominales, ce qui n'est en fait pas le cas.

Donc je dois en fait venir ici et changer cela en une variable d'échelle.

Parce que les données que vous obtenez de Google Trends sont en quelque sorte des pourcentages de zéro à un en termes de popularité relative des termes de recherche, changez cela en échelle.

Et sinon, je suis prêt à partir.

Maintenant, faisons la même chose, mais avec un fichier CSV.

Pour ce faire, je vais simplement me débarrasser de ce fichier de données, je vais simplement en ouvrir un nouveau.

Nous y voilà.

Je vais revenir ici au fichier et ouvrir les données.

Cette fois, je dois dire que je cherche un CSV, mais si je m'en souviens, c'est en fait sous texte.

Donc je clique ici.

Et sauf que cette fois, au lieu de sélectionner le fichier dot txt, je vais sélectionner le fichier dot CSV.

Et ce que vous trouvez, c'est que la procédure est presque identique.

Il n'y a qu'un super petit changement ici.

Je clique sur Continuer.

Je dis que les noms des variables sont en haut.

C'est délimité.

et il est bon de savoir que chaque ligne est un cas, je clique simplement sur continuer et tout cela.

Voici la seule différence.

Lorsque j'ai fait le fichier texte, l'onglet était automatiquement sélectionné.

Maintenant que je fais un CSV, ce qui signifie des valeurs séparées par des virgules, la virgule est automatiquement sélectionnée.

Je clique sur Continuer.

Il fait la même chose avec le mois, nous allons le laisser comme une chaîne, je clique sur continuer et je peux cliquer sur Terminé.

Et vous voyez, cela ressemble exactement à la même chose.

J'ai cependant le même problème, ces trois chiffres qui vont de zéro à 100, sont codés comme nominaux, je dois les changer manuellement en échelle.

D'accord.

Maintenant, nous allons faire le troisième, un fichier Excel.

Maintenant, dans beaucoup de programmes, vous obtenez des avertissements très sévères sur l'importation de fichiers Excel.

Et il y a de bonnes raisons à cela.

Parce que les fichiers Excel sont très flexibles, et les gens peuvent y mettre beaucoup de choses, encore des commentaires et des colonnes de largeur variable et des cellules fusionnées qui facilitent l'utilisation d'Excel juste pour afficher des informations.

Mais si vous l'importez, vous ne voulez pas faire cela.

Heureusement, je l'ai configuré comme des données bien organisées déjà.

Les colonnes sont les mêmes que les variables, les lignes sont les mêmes que les cas, il n'y a rien d'autre là-dedans.

Et donc ce que je peux faire dans ce cas est de venir à Fichier, Ouvrir, nous allons à nouveau aux données.

Et cette fois, je descends ici, il a en fait un format de fichier Excel.

Le voilà, je clique sur ouvrir.

Et vous voyez que la boîte de dialogue est différente.

Dans ce cas.

Il dit ouvrir la source de données Excel au lieu de l'assistant d'importation de texte.

Il dit lire les noms des variables à partir de la première ligne, c'est coché par défaut, il sait combien de lignes de données j'ai.

Et il a cette chose sur la largeur maximale, je n'ai pas besoin de m'en soucier, je clique simplement sur OK.

Et c'était tout.

Voici les données d'Excel, ce sont les mêmes données, je dois encore changer manuellement ces trois mesures, vous pourriez sauvegarder ces informations en syntaxe si vous allez les faire plusieurs fois.

Mais cela est suffisant pour le besoin.

Et il s'avère que l'importation d'informations dans SPSS est vraiment facile.

Et c'est massivement plus efficace et plus facile à faire que de l'entrer directement.

Vous le faites dans une feuille de calcul.

Et surtout si vous le faites sur Google Sheets, si vous entrez des choses manuellement, vous pouvez collaborer dessus.

Et puis vous l'enregistrez comme un fichier CSV, et vous le mettez là.

Et puis vous pouvez passer directement à votre analyse.

Et c'est le but de tout ce travail de toute façon.

Et maintenant dans SPSS et introduction, nous arrivons à la partie que vous attendiez peut-être, et c'est l'analyse des données.

J'ai mentionné.

Cependant, je ne vais donner qu'un très petit aperçu de l'analyse des données, car nous avons un cours entier séparé ici pour l'analyse des données, ainsi que la visualisation des données dans SPSS.

Et je vous recommande de les consulter.

Mais pour vous donner un avant-goût de ce qui est disponible, nous allons parler d'une procédure qui intéresse beaucoup de gens dans les milieux appliqués.

Et c'est le regroupement hiérarchique.

Maintenant, l'idée ici est que vous essayez de trouver des regroupements, vous essayez de trouver les regroupements dans vos données.

Plus spécifiquement, ce que vous essayez de voir, c'est si des cas similaires se regroupent d'une manière que vous pouvez utiliser pour faire des inférences à leur sujet.

Le truc, cependant, est que la similarité dépend de vos critères.

Et il y a quelques décisions que vous devez prendre lorsque vous faites une analyse de regroupement de quelque sorte que ce soit.

Par exemple, vous devez décider si vous allez faire une analyse de regroupement hiérarchique, qui va d'un groupe à autant de groupes que vous avez de cas, ou si vous allez utiliser un ensemble K ou un nombre défini de regroupements.

Vous devez également décider des mesures de distance que vous allez utiliser, la distance euclidienne, qui est un peu comme mesurer la distance à vol d'oiseau entre les cas, est très courante, tout comme la distance euclidienne au carré, que SPSS utilise.

Il y a aussi la question de savoir si vous voulez commencer avec tout ensemble et le diviser en une procédure divisive, ou commencer avec tout séparé et le mettre ensemble dans une procédure agglomérative.

Par défaut, certains programmes comme R divisent, mais par défaut, SPSS fait de l'agglomératif, vous finissez par avoir les mêmes résultats généraux de toute façon, donc ce n'est vraiment pas une énorme différence.

Donc nous allons faire une analyse de regroupement, mais nous allons essayer de garder cela simple.

Nous allons utiliser certaines des méthodes les plus basiques pour faire cela, nous allons utiliser la distance euclidienne ou la distance euclidienne au carré.

Dans ce cas, nous allons utiliser le regroupement hiérarchique où nous n'avons pas à choisir le nombre de groupes à l'avance.

Et nous allons utiliser une procédure agglomérative où elle commence avec chaque cas séparé puis les met progressivement ensemble.

Nous allons essayer cela dans SPSS, mais j'ai besoin que vous fassiez quelque chose d'abord.

Il y a un dossier que vous pouvez télécharger à partir des fichiers de cas qui se termine par des données ici et dedans il y a un fichier, c'est cars dot save word SAE est un format de données propriétaire SPSS.

Et en plus de cela, il y a le fichier de syntaxe SPSS et vous voudrez les deux pour cette démonstration.

Si vous enregistrez le fichier de données sur votre bureau, il ressemble à ceci.

Vous pouvez simplement double-cliquer dessus et il s'ouvrira dans SPSS, vous avez également la possibilité d'utiliser la syntaxe pour le faire.

Cela dépend de votre système d'exploitation.

C'est pour un Macintosh ici.

Et c'est pour un ordinateur Windows, bien que vous deviez peut-être utiliser des barres obliques inverses.

Au lieu de cela, selon votre version de Windows.

Je vais simplement revenir en arrière et double-cliquer sur cela, pour l'ouvrir dans SPSS.

Et voici mon ensemble de données.

Ce que cet ensemble de données est, c'est une légère variation d'un ensemble de données appelé m t cars.

C'est dans le package de jeux de données par défaut dans R.

Il contient des données de test routier sur un certain nombre de voitures de 1974, du magazine Motor Trend.

Et ce que nous allons faire, c'est que nous allons examiner ces informations, nous allons voir si les voitures se regroupent d'une manière importante.

Je vais à la vue des données ici.

Et vous pouvez voir que nous avons Mazda RX quatre Hornet sport à propos de Mercedes, 450, se, Lincoln, continental et ainsi de suite, des voitures qui étaient toutes disponibles au début des années 70.

Et nous avons des informations sur les miles par gallon.

Nous avons les cylindres, nous avons le déplacement en pouces cubes, la puissance, le poids en tonnes, le temps en secondes dans le quart de mile debout.

Si c'est une transmission automatique ou manuelle, le nombre de vitesses dans la transmission.

Et le nombre de carburateurs, probablement des barils de carburateur ici, je vais activer les étiquettes.

Une seule variable change ici.

D'ailleurs, l'une des choses que j'ai faites est de formater cela pour SPSS en ajoutant des étiquettes et en changeant certaines des décimales, ce qui le rend un peu plus facile à travailler dans le programme.

Mais allons au fichier de syntaxe maintenant.

Une fois que nous avons les données ouvertes, nous voulons faire un regroupement hiérarchique par défaut.

Maintenant, voici le code pour le produire.

Mais je vais le faire avec les menus déroulants pour vous montrer que ce n'est pas difficile à faire.

Tout ce que nous devons faire est de venir à analyser.

Et puis nous descendons à classer.

Maintenant, je dois admettre, de mémoire, je ne peux pas me souvenir si chaque version de SPSS a ce menu particulier, la plupart le feront, j'espère que la vôtre le fait.

Donc vous pouvez suivre avec ce regroupement hiérarchique.

Je vais cliquer dessus.

Et ce que je vais faire ici, c'est que je vais prendre Carnegie, qui me dit simplement ce que sont les voitures.

Et je vais utiliser cela pour étiqueter les cas car cela aura du sens pour moi.

Et je vais prendre toutes mes autres variables sur le tabouret, je vais faire un clic décalé ici et les mettre ici.

Et à ce moment-là, je ne vais rien changer d'autre, vous verrez qu'il va regrouper les cas, c'est ce que nous voulons, il va nous donner à la fois des statistiques et des graphiques, c'est bien.

Je vais cliquer sur OK.

Et nous allons obtenir un résultat identique à ma première commande de syntaxe.

Je vois le son, je vais agrandir la fenêtre de sortie ici.

Et voici ce que nous avons.

Tout d'abord, il nous dit combien de cas il y avait et il y en avait 32.

Et ils avaient tous des données complètes, ce qui est bien.

Ensuite, SPSS nous donne quelque chose de plutôt inhabituel, appelé un calendrier d'agglomération.

Et il spécifie vraiment à quel moment de la procédure deux cas ont été mis dans le même cluster.

Personnellement, je n'ai pas beaucoup d'utilité pour cela, sauf que je sais que lorsqu'il y a un grand saut dans les coefficients comme ici de trois à 26, vous savez qu'il y a un changement de catégorie très distinct en ce qui concerne de 662 1125, et ainsi de suite.

La plupart du temps, cependant, je vais complètement ignorer celui-ci.

Et ceci, c'est ce qu'on appelle un graphique en icicle.

Et c'est juste une sorte des mêmes informations sur le moment où divers cas ont été abandonnés avec tout le reste.

C'est assez joli à regarder, je le trouve assez insignifiant.

Et donc, franchement, la sortie par défaut de SPSS pour le regroupement hiérarchique ne m'est pas très utile.

En fait, c'est si peu utile que je vais tout supprimer.

Et je vais recommencer, revenir ici à mes éléments de menu récents, je vais aller à cette analyse à nouveau, je vais faire quelques changements.

Je ne veux pas le calendrier d'agglomération, cela ne m'aide pas vraiment.

Et pour les graphiques, je vais me débarrasser du graphique en icicle.

Et puis lorsque vous obtenez un dendrogramme au lieu de dendogramme.

Cela signifie des branches en grec.

Donc c'est un graphique des branches.

Et c'est généralement la chose la plus importante que vous pouvez obtenir d'une analyse de regroupement hiérarchique.

Je vais cliquer sur OK.

Et maintenant, ce que nous avons, c'est un graphique ici qui liste tous les cas, les voitures sur le côté, et il montre comment ils se sont regroupés.

Donc nous voyons, par exemple, ces quatre premières voitures, la Mazda RX quatre, et le wagon et la Mercedes 280 et deux, etc, sont très similaires les unes aux autres, elles vont toutes ensemble ici, nous voyons cette mère, nous descendons ici.

Par exemple, le Cadillac Fleetwood, le Lincoln Continental, le Chrysler Imperial, qui sont toutes des voitures américaines gargantuesques avec un gros VAT, elles vont toutes ensemble là.

Et puis nous voyons ici en bas, que celle-ci, la mazarine board est toute seule pendant très longtemps.

C'est là que les cas sont individuels ici à gauche, et ils se mettent progressivement ensemble.

Et vous voyez comment ils se rejoignent dans chacune de ces branches.

C'est pourquoi on l'appelle un dendrogramme.

Et c'est une très belle façon de voir à quel point vos cas sont similaires.

Et si vous avez plus de pixels affichés, vous pouvez voir le graphique entier à la fois, j'ai une faible résolution ici.

Et vous pouvez voir, peut-être qu'il est logique de le diviser en, disons, quatre groupes, il semble que nous avons un groupe distinct ici, là, là, et là.

Et donc je peux faire autre chose avec cela.

Je vais revenir au menu ici.

Et ce que je vais faire, c'est sauvegarder l'appartenance au groupe.

Maintenant, j'ai fait une analyse hiérarchique.

Donc je n'ai pas eu à spécifier le nombre de groupes.

Mais maintenant que j'ai regardé le graphique, quatre semble être un bon nombre.

Donc je vais venir ici et dire, donnez-moi l'appartenance au groupe pour chaque cas, en le décomposant en quatre clusters.

Je vais cliquer sur Continuer.

Et puis je vais demander à ne pas avoir de graphiques.

Je clique sur OK.

Et cette fois, nous n'allons pas avoir de sortie sauf pour dire qu'il a fait le travail.

Prenons simplement cela.

Ici, il dit qu'il les a traités.

L'endroit où nous allons voir les différences dans les fichiers de données, je vais me déplacer vers le fichier de données.

Ce bouton, d'ailleurs, me permettra de passer aux données.

Et maintenant, vous pouvez voir que j'ai une nouvelle variable qui a été ajoutée ici, quatre clusters pour et vous pouvez voir que chacune des voitures est listée dans l'un de ces quatre clusters.

Et ce que vous pouvez faire ensuite, c'est que vous pouvez prendre ces appartenances aux clusters, et vous pouvez les comparer sur les autres variables.

Rappelez-vous encore une fois, le regroupement ici n'est valable que pour les données que nous lui donnons.

Donc il ne compare ces voitures que sur un petit nombre de variables.

Et il utilise cela pour décider ce qui va avec quoi, c'est ici, par exemple, que vous voyez qu'elles étaient Roddy Bora dans une catégorie toute seule.

Et c'est une manière sympa de regarder la similarité entre les éléments.

Vous pouvez le faire avec des personnes si vous faites des recherches marketing, vous pouvez le faire avec des entreprises si vous faites une sorte de segmentation.

Et cela vous permet de voir quels groupes ont des similarités importantes pour ce que sont vos objectifs, et quels groupes vous devez traiter différemment les uns des autres.

C'est l'objectif de l'analyse de regroupement hiérarchique.

Et vous trouvez que c'est une chose très facile à faire dans SPSS.

Une autre procédure importante dans SPSS lorsque vous analysez des données est quelque chose appelé analyse factorielle.

Maintenant, j'aime penser à cela comme regarder vos données et essayer de trouver des ombres.

Dans cette image, ce que vous avez, ce sont des ombres, ce sont les figures noires que vous voyez, il faut un moment pour comprendre que vous regardez vers le bas et qu'il y a en fait des personnes, mais qui sortent un peu.

Et donc dans cette photo, nous passons d'une sorte d'origine tridimensionnelle, c'est la personne elle-même, à une variation bidimensionnelle avec l'ombre.

Ce qui est intéressant, c'est que vous conservez la plupart des données utiles, vous pouvez dire qu'il y a des personnes, qu'elles marchent, vous pouvez probablement même dire certaines choses sur leur taille, ce qu'elles portent, et ainsi de suite.

Ce que vous avez fait, c'est que vous avez rendu les choses plus efficaces.

Dans le monde des données, cela s'appelle la réduction de la dimensionnalité, où chaque variable est une dimension.

Et trop de variables peuvent en fait être vraiment problématiques.

Vous essayez de réduire un peu les choses.

Et vous pouvez penser à l'expression moins c'est plus ou moins est égal à plus.

Plus spécifiquement, cela signifie moins de bruit et moins de variables inutiles dans votre ensemble de données.

Égal à plus de signification, car c'est ce que vous essayez de faire, vous essayez d'extraire de la signification.

Maintenant, en ce qui concerne l'analyse factorielle et les techniques connexes, j'ai un conseil très important et c'est d'être pratique.

À tous les points, vous devez vous rappeler quel est votre objectif ? Donc quel est l'objectif ? Eh bien, l'objectif de l'analyse factorielle, je vais vous dire ce que ce n'est pas.

Ce n'est pas un exercice de pureté analytique.

Vous n'êtes pas là pour montrer que vous savez comment passer par toutes les étapes au format approuvé.

Vraiment, vous travaillez avec vos données parce que vous essayez d'obtenir une certaine compréhension.

Donc l'objectif d'une procédure comme l'analyse factorielle est une compréhension utile, en essayant de suivre les règles, faites ce que vous pouvez pour vous assurer de ne pas faire d'erreurs évidentes.

Mais rappelez-vous, vous n'êtes pas lié par les mathématiques, vous êtes lié par ce que les données vous disent sur les gens.

Une autre façon de voir cela est d'utiliser l'analyse factorielle, ou vraiment toute autre procédure pour sa valeur heuristique.

C'est-à-dire qu'elle suggère des possibilités lorsque vous analysez les données lorsque vous essayez d'obtenir des informations sur les personnes.

Maintenant, c'est une sorte de discours philosophique, laissez-moi vous montrer comment cela fonctionne réellement dans SPSS, vous allez devoir télécharger à partir des fichiers du cours un dossier qui dit data ici à la fin.

Et de celui-ci, l'ensemble de données cars dot save, celui que nous avons utilisé dans le regroupement hiérarchique également.

Et puis vous voulez ouvrir le fichier de syntaxe SPSS qui accompagne cette section particulière.

Maintenant, le moyen le plus facile d'ouvrir l'ensemble de données est simplement de double-cliquer dessus et vous êtes prêt à partir.

J'ai une syntaxe que vous pouvez utiliser si vous l'avez sauvegardé sur votre bureau.

Je l'ai déjà ouvert.

Donc jetons un coup d'œil rapide à l'ensemble de données.

Nous avons une collection de voitures listées sur le côté et des attributs comme mpg et ainsi de suite et les vitesses dans la transmission et les carburateurs.

C'est super.

Maintenant, je dois faire une confession très importante ici.

C'est un ensemble de données très, très petit pour l'analyse factorielle.

Il n'a que neuf variables autres que l'identifiant, et il n'a que 32 cas, vraiment, vous voudriez avoir au moins plusieurs centaines de cas.

Et disons plusieurs dizaines de variables avant de pouvoir faire cela de manière vraiment fiable.

Mais cet exemple fonctionne.

Et il est en fait très facile de voir comment cela se passe, et comment interpréter les résultats.

La première chose que nous allons faire, si vous regardez la syntaxe, c'est que nous allons faire une analyse factorielle par défaut.

Et c'est en fait un abus de langage, car ce n'est pas une analyse factorielle.

C'est une analyse en composantes principales, mais c'est dans la commande d'analyse factorielle dans SPSS.

Donc, venons ici à analyser.

Et descendons à la réduction de dimension.

Je me souviens que c'est ce que cela s'appelle, choisissez facteur, c'est notre seul choix là.

Et ce que nous devons faire, c'est choisir les variables que nous allons utiliser pour voir ce que nous pouvons compresser, ce qui va avec quoi, donc nous n'avons pas besoin du nom de la voiture, c'est juste un identifiant.

Nous pouvons prendre le reste de ceux-ci, cependant, et nous pouvons les mettre sous variables.

Maintenant, nous avons beaucoup d'options ici, je ne vais pas en faire, je vais juste cliquer sur OK pour l'instant.

Et agrandir la fenêtre de sortie.

Et voici ce que nous obtenons de l'analyse par défaut, nous obtenons une sortie texte des commandes qui ont été générées par les menus déroulants, nous obtenons quelque chose appelé la communalités.

Chaque variable apporte avec elle une unité de variance standardisée.

Cela est basé sur la dispersion des scores.

Et si vous les standardisez, alors vous avez une variance et un écart-type de un pour chacun.

Et l'extraction nous dit combien de cette variance est vraiment capable d'être constituée à travers le processus que nous faisons.

Un point important ici est la variance totale expliquée, car ce que cela a fait, c'est qu'il a créé des composants, j'ai dit que c'est en fait une analyse en composantes principales ici, qui a des fondements philosophiques profondément différents de l'analyse factorielle, la différence a à voir avec ce qui est venu en premier, les facteurs ou les variables observées.

Et franchement, la plupart des gens les traitent comme relativement interchangeables.

Et si vous les utilisez pour leur valeur heuristique, ce ne sera pas une grande différence.

Mais ce que nous avons ici, ce sont deux composants, nous en avons un avec 5,472 unités de variance, soit 61 % de la variance originale des neuf variables, et puis un autre avec 2,341.

Je prends ces chiffres ici.

Et vous pouvez voir qu'il a retenu ces deux, qui collectivement s'additionnent à environ 87 % de la variance.

La matrice des composants montre la relation entre les variables originales et les deux composants.

Ce sont comme des coefficients de corrélation, vous pouvez voir que mpg est fortement associé négativement au premier composant et vraiment pas associé au second.

Mais le nombre de carburateurs a une association assez forte avec chacun.

Et donc c'est une façon de commencer à le regarder.

Mais ce sera beaucoup plus facile si nous faisons certaines modifications à cela.

En fait, je vais simplement supprimer cette sortie ici.

Et nous allons recommencer, je vais faire quelques changements, passons en revue chacune de ces options.

D'abord, nous allons aux descriptives.

Et je ne pense pas vraiment avoir besoin de la solution initiale.

Donc je vais désélectionner cela, je vais cliquer sur Continuer.

Extraction.

C'est l'algorithme réel que SPSS utilise pour travailler à travers les relations dans l'espace multidimensionnel.

Vous voyez ici, c'est les composantes principales.

C'est pourquoi j'ai dit que c'est vraiment une analyse en composantes principales, vous avez beaucoup d'options ici.

Maintenant, dans de nombreuses situations, le maximum de vraisemblance serait une très bonne réponse, je vais choisir l'axe principal de factorisation simplement parce que c'est la version classique de l'analyse factorielle.

Je n'ai pas besoin de voir la solution factorielle non tournée, mais je veux voir quelque chose appelé un graphique en coude.

Et c'est un graphique qui me montre peut-être combien de facteurs je devrais garder, je vais descendre ici et changer le nombre maximum d'itérations pour la convergence, cela a à voir avec les mathématiques, c'est fait, je vais le changer à 50.

Ensuite, je vais à la rotation, ce que vous obtenez ici, c'est un espace multidimensionnel.

Et parfois, c'est un peu plus facile.

Si vous faites tourner les axes, vous pouvez augmenter l'interprétabilité.

Maintenant, il y a beaucoup de méthodes différentes.

Varimax est une méthode qui maintient les relations orthogonales, cela rend toutes vos axes perpendiculaires les uns aux autres.

Il y a des situations où c'est vraiment bien.

Mais franchement, à des fins exploratoires, ce que nous faisons, j'aime utiliser ce qu'on appelle une rotation oblique, cela permet à vos facteurs d'être corrélés les uns avec les autres, ils n'ont pas besoin d'être totalement perpendiculaires.

Je vais utiliser direct oblem.

Et promax est un autre choix vraiment bon.

Mais il est généralement pour des ensembles de données plus grands, et j'en ai un tout petit ici.

Maintenant, ici, je peux obtenir une solution tournée, je ne pense pas vraiment en avoir besoin.

Mais je veux voir le graphique de chargement.

Et je vais augmenter le nombre maximum d'itérations à 50.

Je vais cliquer sur Continuer.

Nous allons descendre à scores.

Et vous pouvez sauvegarder les chargements de facteurs comme scores.

Et il peut y avoir des situations où vous voulez faire cela.

Mais parce que j'utilise l'analyse factorielle pour sa valeur heuristique, comme un moyen, suggérant quelles variables vont avec d'autres, je ne vais en fait pas le faire.

Donc je vais cliquer sur annuler.

Ensuite, options.

C'est là que vous parlez d'exclure les cas, j'ai un ensemble de données complet, donc je n'ai pas besoin de m'en soucier.

Mais le format d'affichage des coefficients, maintenant, je vais les trier et ensuite je vais en fait effacer complètement les petits coefficients.

Maintenant, je l'ai déjà fait une fois.

Donc il se trouve que je sais qu'une valeur de point six, dans des circonstances normales, est vraiment élevée.

Mais étant donné mon très petit ensemble de données, cela semble être un choix raisonnable.

Et cela rend la solution très, très claire lorsque nous la regardons.

Donc je vais cliquer sur Continuer.

Et puis là, je vais cliquer sur OK.

J'ai ma sortie ici.

Et la première partie est assez similaire, sauf qu'elle ne commence pas avec une variance unitaire pour chacune de celles-ci.

C'est parce que je ne fais plus de composantes principales.

Je fais l'axe principal de factorisation.

Et donc les mathématiques derrière sont un peu différentes.

Mais nous n'avons pas besoin de nous attarder sur cela.

Variance totale expliquée, vous voyez que nous avons toujours deux facteurs.

Et le premier en rend compte pour beaucoup de la variance, le second en rend compte pour une quantité assez importante aussi, et ceux-ci sont très proches de ce que nous avions avec les composantes principales.

Le graphique en coude est un graphique en ligne très simple.

Cela suggère combien de facteurs nous pourrions vouloir garder.

Maintenant, il y a plusieurs règles différentes que vous pouvez utiliser pour interpréter cela.

L'une est tout ce qui est au-dessus d'une valeur de un, car un est ce que ce serait si une variable expliquait simplement une unité de variance, mais c'est ce qu'elle a apporté, vous voulez des facteurs qui ont expliqué plus que cela.

Et vous voyez que nous en avons deux qui font beaucoup plus que un et ceux-ci sont un peu en retard.

L'autre règle est de chercher une courbure dans la ligne et vous voyez une courbure forte ici.

Donc trois est là où se trouve la courbure, nous sommes justifiés de dire avec deux, il y a d'autres méthodes pour s'impliquer davantage dans la vérification de la pente de cette ligne et trouver des choses qui sont au-dessus de cette pente.

Vous pouvez les faire à un autre moment.

C'est une démonstration rapide.

Maintenant, ce que nous obtenons ensuite, ce sont trois matrices, nous obtenons une matrice de facteurs, une matrice de motifs et une matrice de structure.

Elles sont toutes associées les unes aux autres.

Et j'ai une petite note ici dans la syntaxe qui les explique.

Je vais descendre ici.

La matrice des facteurs est l'association de chaque variable avec chaque facteur et elle est de nature similaire, elle est analogue au coefficient de corrélation.

C'est celle sur laquelle nous allons nous concentrer.

La matrice de structure nous dit combien chaque variable est prédite par les facteurs, car l'idée ici est que les facteurs viennent en premier et les variables en second, en utilisant ce que l'on appelle les contributions uniques et communes.

Donc un facteur peut contribuer quelque chose de lui-même par rapport aux autres facteurs ou il contribue ensemble.

Et puis la matrice de motifs est une indication de la contribution unique de chaque facteur à la variance des variables.

Celles-ci peuvent toutes être importantes dans différentes situations, et elles peuvent vous aider à interpréter les choses.

Mais pour l'instant, je vais me concentrer sur cette première.

Nous y voilà, la matrice des facteurs.

Donc laissez-moi revenir à l'endroit où j'en étais.

Et lorsque nous arrivons à la matrice des facteurs, ce que vous voyez ici, c'est que parce que j'ai supprimé les valeurs avec une valeur absolue inférieure à 0,6, nous avons cette séparation totalement claire.

Le facteur un est fortement associé au nombre de cylindres dans la voiture.

Donc plus de cylindres, plus élevé sur le facteur un, et puis le déplacement, très élevé, le mpg est négatif, mais très fort.

Et puis nous avons le poids en tonnes très fort et la puissance.

C'est vraiment le gros facteur, les voitures qui sont vraiment grandes vont marquer fortement sur le facteur un.

Le facteur deux est composé du nombre de vitesses et plus de vitesses, le temps au quart de mile, donc moins de temps il faut pour traverser le quart de mont, c'est-à-dire plus rapide.

C'est parce que c'est négatif ici, plus il est automatique ou manuel, vous devez savoir que zéro est automatique, et un est manuel.

Donc ce sont des voitures à transmission manuelle, et celles avec plus de carburateurs.

C'est vraiment le facteur rapide.

Et c'est là que se trouvent les voitures de sport, celle-ci, celle-ci a les Cadillacs et les Lincoln et celle-ci a les Ferraris et les Lotus et ainsi de suite.

Et cela a parfaitement du sens, c'est vraiment facile de voir pourquoi cela serait ainsi.

Et puis si vous descendez ici, ce graphique est également vraiment utile, il a les deux facteurs, nous avons le facteur un en bas, c'est notre gros facteur.

Et vous pouvez voir que le poids va sur celui-ci, le déplacement va sur celui-ci, le cylindre, et puis nous avons le nombre d'années et les miles par gallon, évidemment, vous êtes à l'extrémité basse.

Le facteur deux est le facteur rapide.

Plus de carburateurs, plus de puissance, plus de cylindres, et des temps de quart de mile plus bas.

Et cela a beaucoup de sens.

Et cela nous permet de savoir que nous pourrions réduire nos données à vraiment juste ces deux facteurs, un peu comme la taille de la voiture et sa rapidité.

Et cela peut nous donner une image beaucoup plus concise de nos données, et nous permet d'extraire plus de sens et c'est le but global d'une procédure comme l'analyse factorielle ou les composantes principales dans SPSS.

Pour un dernier regard sur SPSS et l'analyse des données, du moins dans ce cours d'introduction, examinons l'une des procédures les plus utiles : la régression.

Maintenant, vous pourriez penser à la régression comme une sorte de version statistique des Trois Mousquetaires où c'est tous pour un.

Je dis cela parce que tous pour un est en fait toutes les variables pour prédire un résultat.

En d'autres termes, la régression utilise de nombreuses variables différentes, de nombreuses variables prédictives pour prédire les scores sur une variable de résultat.

Cela la rend vraiment utile dans une énorme gamme de circonstances, surtout parce qu'il y a quelque chose pour tout le monde avec la régression.

Il existe de nombreuses versions différentes et de nombreuses adaptations de la régression qui la rendent vraiment flexible et puissante.

Lorsque vous analysez des données et en faites un outil de prédilection pour presque tous les objectifs analytiques que vous pourriez avoir.

Nous allons essayer une version simple de cela dans SPSS.

Tout d'abord, assurez-vous d'avoir téléchargé ce dossier de données à partir des fichiers du cours.

Il utilisera l'ensemble de données cars dot save que nous avons utilisé dans nos deux exemples précédents, ainsi que ce fichier de syntaxe.

Et lorsque vous arriverez à ce fichier d'index, il commence comme d'habitude.

Avec le code pour charger l'ensemble de données à partir du bureau, franchement, il est plus facile de simplement double-cliquer sur le fichier cars dot save et de l'avoir ouvert directement dans SPSS.

C'est ce que j'ai fait ici.

Et vous pouvez voir que c'est le même ensemble de données avec environ 32 lignes de données, un tas de voitures de 1974.

Et plusieurs variables, nous allons essayer de prédire dans celle-ci, les miles par gallon, sur la base de choses comme le nombre de cylindres, le déplacement, la puissance, le poids, le temps en secondes, la transmission et le type et les vitesses et les carburateurs.

D'accord, donc cela devrait être assez facile.

Ce que nous allons faire, c'est aller à analyser, et descendre à régression.

Et nous allons utiliser cette deuxième option ici, linéaire.

C'est juste la régression linéaire de base.

Maintenant, nous devons mettre sous dépendant la variable de résultat, la chose que nous essayons de prédire, cela me dérange un peu ici, parce que indépendant et dépendant devraient vraiment être réservés aux expériences manipulées.

Mais nous savons toujours ce qu'ils signifient, notre variable de résultat, la chose que nous essayons de prédire va ici, indépendant.

Donc c'est mpg.

Maintenant, nous pouvons prendre tout le reste sauf le nom de la voiture, c'est juste une étiquette, nous allons prendre tout le reste de ceux-ci et nous allons les mettre sous notre indépendant ou les variables que nous utilisons pour prédire le résultat.

Maintenant, je veux faire la version par défaut, sans étapes supplémentaires.

Donc j'ai mis les variables à leur place respective.

Et je vais simplement cliquer sur OK.

Et maintenant, nous obtenons notre sortie.

Et elle nous dit d'abord le code qui a été utilisé pour produire cette analyse, qu'elle a utilisé toutes ces variables simultanément pour prédire un seul résultat, qui est listé ici.

Et elles ont été entrées en une fois.

Le résumé du modèle nous indique que nous avons une corrélation multiple de ces variables prédictives avec notre variable de résultat de 0,931, ce qui est vraiment élevé.

Si vous élevez cela au carré pour obtenir la proportion de variance expliquée, c'est 86,7 %.

Même le R carré ajusté, parce que nous avons un petit échantillon, est encore de 82 %.

C'est énorme.

Nous obtenons un test de signification ici, nous ne sommes pas surpris de voir que la signification est de 0,000.

Ce n'est pas zéro jusqu'au bout, mais c'est très significatif.

Et puis nous obtenons des coefficients pour les coefficients de régression individuels.

Donc ce que nous cherchons ici, ce sont des niveaux de signification inférieurs à 0,05, et intéressamment, un seul d'entre eux dans cette collection est inférieur à 0,05 et c'est le poids en tonnes.

Aucun des autres n'y est proche.

Cela ne signifie pas que les autres n'ont pas d'importance.

Cela signifie simplement que lorsque vous prenez toutes les variables ensemble en même temps, lorsqu'elles sont prises dans leur ensemble, une seule d'entre elles s'écarte de manière significative de zéro pour devenir un prédicteur.

C'est une attente.

Maintenant, il y a beaucoup d'autres façons de faire de la régression.

Et SPSS vous donne beaucoup de choix.

Je vais venir ici, revenir à analyser, descendre à régression.

Maintenant, je vais mentionner, il y a une option vraiment intéressante ici appelée modélisation linéaire automatique.

C'est une fonction SPSS, elle est apparue il y a quelques versions, elle fait beaucoup de préparation automatique des données, elle fait beaucoup de combinaison et de division des variables.

D'autre part, c'est vraiment assez difficile à expliquer comment tout cela fonctionne.

Et puis à l'interpréter correctement.

Je vais le garder pour un autre cours où je parle spécifiquement de l'analyse des données.

Pour l'instant, je vais revenir à linéaire.

Et nous allons faire quelques choix, nous allons faire quelques options, reformuler.

Et nous allons faire quelques choix, nous allons prendre certaines des options que SPSS rend disponibles.

Maintenant, la première que je vais faire, au risque de faire quelque chose de très controversé, c'est que je vais en fait passer de l'entrée simultanée à la régression pas à pas.

C'est controversé parce que certaines personnes dans la littérature l'ont appelé positivement diabolique.

Et son risque d'erreur de type un ou de faux positif.

Et il y a de bonnes preuves à ce sujet.

D'autre part, dans l'apprentissage automatique moderne, les procédures pas à pas ont été très fructueuses.

Et donc ce n'est pas totalement inacceptable d'essayer, surtout lorsque nous faisons un projet exploratoire comme celui-ci en ce moment, vous ne voudriez certainement pas l'utiliser pour la construction de modèles rigoureux, mais c'est un bon moyen d'obtenir un aperçu des données assez rapidement.

Je vais venir juste aux statistiques, et je vais ajouter quelques choses, je vais obtenir des intervalles de confiance pour les coefficients, c'est bien de les avoir, nous avons l'ajustement global du modèle.

Et je vais obtenir le changement de R carré, car un modèle pas à pas passe par plusieurs étapes différentes, en ajoutant des variables.

Et nous voulons voir si chaque variable ajoute quelque chose qui est statistiquement significatif au modèle global.

Nous pourrions obtenir beaucoup plus d'informations ici, mais je vais m'arrêter là pour l'instant.

Sous les graphiques, nous pouvons obtenir une tonne de graphiques différents, mais je vais en fait simplement descendre ici et choisir les graphiques de résidus standardisés, un histogramme et un graphique de probabilité normale.

Maintenant, il y a d'autres options également.

Je pourrais sauvegarder environ 15 types de scores différents dans l'ensemble de données.

Je peux dire des valeurs prédites non standardisées, je peux sauvegarder des résidus studentisés supprimés, et ainsi de suite.

Des choses que je pourrais faire ici et il y a des situations où je pourrais vouloir faire cela.

Mais pour l'instant, je vais les sauter car je construis simplement un modèle sans nécessairement sauvegarder toutes les étapes intermédiaires. Les options parlent vraiment des critères utilisés dans la procédure pas à pas, je vais les laisser par défaut pour l'instant, mais vous pourriez les changer si vous le souhaitiez.

Et puis le style est une nouvelle chose qui a à voir avec la mise en forme du tableau.

Je vais laisser celui-là tranquille pour l'instant, car nous allons avoir exactement ce dont nous avons besoin.

Maintenant, j'ai déjà créé cela, et je l'ai sauvegardé dans la syntaxe, je vais simplement cliquer sur OK.

Et vous verrez que nous obtenons un type de sortie différent maintenant.

Je vais zoomer sur cela.

Maintenant, ce que nous avons, c'est un code un peu plus long, cela doit passer par les variables une à la fois.

Et trouver la variable prédictive qui est le plus fortement associée au résultat, la mettre dans le modèle, obtenir des corrélations partielles et passer étape après étape.

Ce que nous trouvons ici, c'est que bien que nous avions neuf prédicteurs à l'origine, seuls deux d'entre eux étaient statistiquement significatifs lorsqu'ils étaient mis dans le modèle.

Ils étaient le poids et le nombre de cylindres.

Encore une fois, ce que nous essayons de prédire, c'est la consommation d'essence, mpg.

Si vous descendez ici, vous pouvez voir qu'ils étaient tous les deux statistiquement significatifs, ou le R carré ajusté pour le poids seul est de 74,5.

Et lorsque vous ajoutez le nombre de cylindres, il augmente.

Pas une énorme quantité, mais il augmente de près de 8 %.

Le tableau d'analyse de variance nous permet de savoir que les deux modèles avec une seule variable et avec deux variables prédictives sont tous deux statistiquement significatifs.

Voici les coefficients individuels ainsi que leurs intervalles de confiance ici à droite.

Maintenant, parce que nous avons passé par une procédure pas à pas, il n'est pas surprenant que tous ceux-ci soient statistiquement significatifs, car c'était le critère utilisé pour les inclure.

Ici, nous avons une liste de variables exclues ainsi que leurs statistiques de colinéarité.

Et cela concerne la corrélation de chacune de ces variables avec les autres.

Par exemple, le nombre de carburateurs est fortement colinéaire, ou facilement prédit par les autres variables que nous aurions pu inclure dans le modèle.

Maintenant, nous descendons aux résidus, je vais regarder spécifiquement le graphique.

Dans un monde idéal, vos résidus sont normalement distribués, ce qui signifie qu'ils sont aussi susceptibles d'être élevés que bas, et qu'ils sont symétriques.

Et nous voyons ici qu'ils ne sont pas horriblement, pathologiquement éloignés de la normale.

Donc c'est probablement un bon modèle sur l'ensemble.

Et voici un graphique de probabilité normale de ces mêmes données.

Et si c'était parfaitement normal, tous les points seraient sur la ligne, la ligne diagonale, ils sont proches.

Ce sont les 32 observations individuelles et à quel point elles sont éloignées, elles sont assez proches.

Et donc cela nous permet de savoir que notre modèle prédit vraiment bien et qu'il semble ne pas être biaisé dans une direction ou une autre.

Donc c'est une méthode de développement de modèle.

Encore une fois, cette procédure pas à pas est meilleure pour les analyses exploratoires, ce n'est pas quelque chose que vous utiliseriez pour confirmer une découverte.

Mais comme un moyen rapide de trier une grande collection de variables potentielles, c'est une bonne façon de le faire.

Cela nous permet de savoir, par exemple, que dans cet ensemble de données particulier, mpg est prédit principalement par un poids, ce qui a complètement du sens pour la voiture, et le nombre de cylindres, qui est associé à un moteur grand et assoiffé.

Donc l'idée générale de la régression multiple, encore une fois, est d'utiliser de nombreuses variables pour prédire un seul résultat, SPSS donne beaucoup d'options pour celles-ci, nous avons regardé le défaut, nous avons regardé une variation là-dessus, mais il y en a beaucoup plus que vous pouvez explorer et que nous allons couvrir dans un autre cours sur l'analyse statistique dans SPSS.

Mais pour l'instant, je vous encourage à prendre un peu de temps et à regarder certaines de ces options et à voir le type d'informations qu'elles peuvent vous donner sur vos propres données, et à voir quelles options vous pouvez utiliser pour obtenir des informations utiles sur vos propres analyses.

Je veux vous remercier de vous être joint à moi dans SPSS et introduction.

Et nous allons conclure en vous donnant quelques prochaines étapes, des choses que vous pouvez faire ensuite, car vous savez, une fois que vous avez terminé cela, cela peut être un peu déroutant, avoir l'impression que les choses vont partout.

Et il peut ne pas être totalement clair où vous devriez aller.

Eh bien, ici à data lab.cc, nous avons quelques opportunités pour vous.

Tout d'abord, bien sûr, il y a plus de SPSS, nous avons des cours supplémentaires sur la préparation des données, sur la visualisation des données, sur l'analyse statistique, et d'autres sujets que vous pouvez utiliser pour élargir ce que vous avez appris dans ce cours d'introduction, et travailler sur vos propres données.

Maintenant, si vous avez aimé ce que vous avez appris avec SPSS, vous pourriez vouloir essayer de vous diversifier dans certains autres langages.

Ce langage de programmation statistique R et le langage de programmation généraliste Python, sont très courants et des outils puissants dans la communauté de la science des données et de l'analyse en général.

Ils sont un excellent moyen d'élargir à la fois les choses que vous pouvez faire avec vos analyses et vos opportunités d'emploi, et donc, je vous encourage fortement à jeter un coup d'œil aux cours sur R et Python dans data lab.

Ensuite, nous avons des cours spécifiques sur la visualisation des données, l'une des choses les plus importantes que vous pouvez faire pour comprendre vos données.

SPSS peut bien fonctionner dans ceux-ci ainsi que dans d'autres programmes.

Et puis je vais mentionner une dernière chose ici.

SPSS est un programme merveilleux, mais il a encore un nombre assez important de bugs et il peut aussi être très cher.

Heureusement, un travail vraiment intéressant récemment dans la communauté open source a développé un programme appelé j SB.

Il se prononce en fait Jasper, qui est une sorte de version open source de SPSS, il fonctionne très différemment, je le trouve très facile à utiliser, et il le rend reproductible.

Il facilite le partage.

Il a des avantages considérables et nous avons des cours sur Jasper ici dans data lab, je vous suggère de les consulter et de voir à quel point ce programme est capable de répondre à certains de vos besoins informatiques.

Cela dit, il manque certaines choses.

Qu'est-ce qui manque exactement ? Eh bien, SPSS n'a pas une communauté d'utilisateurs et de développeurs forte et active de la même manière que des langages comme R et Python.

Mais si vous êtes créatif, vous pouvez contourner cela, les conférences académiques, je veux dire spécifiquement les conférences académiques thématiques comme la biologie ou la gestion ou les sciences sociales.

Elles ont souvent des utilisateurs et des enseignants de SPSS très dévoués, et peuvent sponsoriser des ateliers pratiques spécifiques pour en apprendre davantage sur SPSS et comment je peux l'utiliser dans votre domaine particulier.

Mais peu importe ce que vous faites, je vais vous encourager à simplement commencer, à explorer et à voir ce que vous pouvez faire avec SPSS dans votre propre travail de données.

Merci beaucoup de vous être joint à moi et bon calcul.