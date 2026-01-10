---
title: Traitement du langage naturel avec spaCy & Python - Cours complet
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-09-27T14:12:24.000Z'
originalURL: https://freecodecamp.org/news/natural-language-processing-with-spacy-python-full-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/nlp.jpeg
tags: []
seo_title: Traitement du langage naturel avec spaCy & Python - Cours complet
seo_desc: 'Natural language processing, or NLP, is a branch of linguistics that seeks
  to parse human language in a computer system. spaCy is a popular Python library
  used for NLP.

  We just published a NLP and spaCy course on the freeCodeCamp.org YouTube channel....'
---

Le traitement du langage naturel, ou NLP (Natural Language Processing), est une branche de la linguistique qui cherche à analyser le langage humain dans un système informatique. spaCy est une bibliothèque Python populaire utilisée pour le NLP.

Nous venons de publier un cours sur le NLP et spaCy sur la chaîne YouTube freeCodeCamp.org. Dans ce cours, vous apprendrez tout sur le traitement du langage naturel et comment l'appliquer à des problèmes concrets en utilisant la bibliothèque Python spaCy.

Le Dr W.J.B. Mattingly a créé ce cours. Le Dr Mattingly est un chercheur postdoctoral au Data Science Lab de la Smithsonian Institution. C'est aussi un excellent enseignant.

Le Dr Mattingly a créé une série de notebooks Jupyter pour accompagner le cours. Ils sont hébergés sur le site web du cours.

Étant donné que le NLP est un problème si complexe pour les ordinateurs, il nécessite une solution complexe. La réponse a été trouvée dans les réseaux de neurones artificiels, ou RNA, ou réseaux de neurones pour faire court. De nouvelles méthodes d'entraînement, telles que les modèles de transformateurs, font progresser le domaine. Vous apprendrez ces méthodes dans ce cours.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/spacy-frontier.gif)
_Un gif spaCy que j'ai créé. :)_

Voici les sections de ce cours :

* Introduction au cours
* Introduction au NLP
* Comment installer spaCy
* Conteneurs spaCy
* Annotations linguistiques
* Reconnaissance d'entités nommées
* Vecteurs de mots
* Pipelines
* EntityRuler
* Matcher
* Composants personnalisés
* RegEx (Bases)
* RegEx (Tokens multi-mots)
* NLP financier appliqué avec spaCy

Regardez le cours ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/dIUTsFT2MeQ) (3 heures de visionnage).

%[https://youtu.be/dIUTsFT2MeQ]

## Transcription

(générée automatiquement)

Dans ce cours, vous apprendrez tout sur le traitement du langage naturel et comment l'appliquer à des problèmes concrets en utilisant la bibliothèque spaCy.

Le Dr Mattingly est extrêmement compétent dans ce domaine et c'est un excellent enseignant.

Bonjour et bienvenue dans cette vidéo.

Je m'appelle Dr William Mattingly et je me spécialise dans le traitement du langage naturel multilingue. Je viens au NLP avec une perspective des sciences humaines, j'ai mon doctorat en histoire médiévale, mais j'utilise spaCy régulièrement pour répondre à tous mes besoins en NLP.

Ce que vous allez obtenir de cette vidéo au cours des prochaines heures est une compréhension de base de ce qu'est le traitement du langage naturel ou NLP, et aussi comment l'appliquer à des problèmes spécifiques à un domaine, ou des problèmes qui existent dans votre propre domaine d'expertise.

Je l'utilise tout le temps pour analyser des documents historiques ou des documents financiers pour mes propres investissements personnels.

Au cours des prochaines heures, vous allez en apprendre beaucoup sur le langage NLP dans son ensemble et, surtout, sur la bibliothèque spaCy.

J'aime la bibliothèque spaCy parce qu'elle est facile à utiliser et facile à mettre en œuvre pour des solutions vraiment générales à des problèmes généraux avec les modèles prêts à l'emploi qui sont déjà disponibles pour vous.

Je vais vous guider dans la première partie de cette série de vidéos sur la façon de tirer le meilleur parti de spaCy avec ces fonctionnalités prêts à l'emploi.

Dans la deuxième partie, nous allons commencer à aborder certaines des fonctionnalités qui n'existent pas dans les modèles prêts à l'emploi.

Et je vais vous montrer comment utiliser des pipelines ou des composants basés sur des règles dans spaCy pour résoudre des problèmes spécifiques à un domaine dans votre propre domaine, de l'EntityRuler au Matcher, en passant par l'injection de motifs d'expressions régulières complexes et robustes, et un composant spaCy personnalisé qui n'existe pas actuellement.

Je vais vous montrer tout cela dans la deuxième partie, afin que dans la troisième partie, nous puissions prendre les leçons que nous avons apprises dans les parties une et deux, et les appliquer pour résoudre un problème très courant qui existe en NLP et qui est l'extraction d'informations à partir de documents financiers.

Donc, trouver des choses qui sont pertinentes, telles que des actions, des marchés, des indices et des bourses.

Si vous me rejoignez au cours des prochaines heures, vous quitterez cette leçon avec une bonne compréhension de la position de spaCy et également une bonne compréhension des composants prêts à l'emploi qui sont là et une façon de prendre les composants prêts à l'emploi et de les appliquer à votre propre domaine.

Si vous me rejoignez également dans cette vidéo et que vous l'aimez, faites-le moi savoir dans les commentaires ci-dessous, car je suis intéressé à faire une deuxième partie à cette vidéo qui explorera non seulement les aspects basés sur les règles de spaCy, mais aussi les aspects basés sur l'apprentissage automatique de spaCy.

Donc, vous apprendrez à entraîner vos propres modèles pour faire vos propres choses, comme entraîner un analyseur de dépendances, entraîner un reconnaisseur d'entités nommées, des choses comme celles-ci, qui ne sont pas couvertes dans cette vidéo.

Néanmoins, si vous me rejoignez pour celle-ci et que vous l'aimez, vous trouverez la deuxième partie beaucoup plus facile à comprendre.

Donc, asseyez-vous, détendez-vous et plongeons dans ce qu'est le NLP, les types de choses que vous pouvez faire avec le NLP comme l'extraction d'informations, et ce qu'est la bibliothèque spaCy et comment ce cours sera organisé.

Si vous aimez cette vidéo, envisagez également de vous abonner à ma chaîne Python tutorials for digital humanities, qui est liée dans la description ci-dessous.

Même si vous n'êtes pas un humaniste numérique comme moi, vous trouverez ces tutoriels Python utiles car ils rendent Python accessible aux étudiants de tous niveaux.

Spécifiquement ceux qui sont débutants, je vous guide non seulement à travers les bases de Python, mais je vous guide également étape par étape à travers certaines des bibliothèques les plus courantes dont vous avez besoin.

Une grande partie de la chaîne traite des textes ou des problèmes basés sur le texte.

Mais d'autres contenus traitent de choses comme l'apprentissage automatique, la classification d'images et l'OCR, tout en Python.

Donc, avant de commencer avec spaCy, je pense que nous devrions passer un peu de temps à parler de ce qu'est réellement le NLP ou le traitement du langage naturel.

Le traitement du langage naturel est le processus par lequel nous essayons de faire comprendre, analyser et extraire le langage humain à un système informatique, souvent à partir de texte brut.

Il existe plusieurs domaines différents du traitement du langage naturel.

Il y a la reconnaissance d'entités nommées, l'étiquetage des parties du discours, l'analyse syntaxique, la catégorisation de texte, également connue sous le nom de classification de texte, la résolution de coréférence, la traduction automatique.

Adjacent au NLP se trouve un autre domaine de la linguistique computationnelle appelé compréhension du langage naturel (NLU). C'est là que nous entraînons les systèmes informatiques à faire des choses comme l'extraction de relations, l'analyse sémantique, les questions et réponses, c'est là que les bots entrent vraiment en jeu, la synthèse, l'analyse des sentiments et la paraphrase.

Le NLP et le NLU sont utilisés par un large éventail d'industries, de l'industrie financière à la loi et à l'académie, avec des chercheurs essayant d'extraire des informations à partir de textes.

Au sein du NLP, il existe plusieurs applications différentes.

La première et probablement la plus importante est l'extraction d'informations.

C'est le processus par lequel nous essayons de faire extraire par un système informatique des informations que nous trouvons pertinentes pour nos propres recherches ou besoins.

Par exemple, comme nous allons le voir dans la troisième partie de cette vidéo, lorsqu'il s'agit d'appliquer spaCy au secteur financier, une personne intéressée par la finance pourrait avoir besoin d'un NLP pour parcourir et extraire des choses comme les noms de sociétés, les actions, les indices, des choses qui sont référencées dans des articles de presse, de Reuters au New York Times en passant par le Wall Street Journal.

C'est un exemple d'utilisation du NLP pour extraire des informations.

Une bonne façon de penser au NLP est son application dans ce domaine : il prend des données non structurées, dans ce cas, du texte brut, et en extrait des données structurées ou des métadonnées.

Il trouve donc les choses que vous voulez qu'il trouve et les extrait pour vous.

Bien qu'il existe des moyens de faire cela avec des répertoires et la correspondance de listes, l'utilisation d'un framework NLP comme spaCy, dont je vais parler dans un instant, présente certains avantages, le principal étant que vous pouvez utiliser et exploiter des choses qui ont été analysées syntaxiquement ou sémantiquement.

Des choses comme la partie du discours d'un mot, ses dépendances, sa coréférence, ce sont des choses que le framework spaCy permet de faire prêt à l'emploi, et aussi d'entraîner dans des modèles d'apprentissage automatique, et de travailler dans des pipelines avec des règles.

C'est donc une sorte d'aspect du NLP.

Et une façon dont il est utilisé.

Une autre façon dont il est utilisé est de lire des données et de les classer.

Cela est connu sous le nom de catégorisation de texte.

Et nous voyons cela sur le côté gauche de cette image, la catégorisation de texte ou la classification de texte.

Et nous concluons dans cette analyse de sentiment pour la plupart, c'est une façon dont nous prenons des informations dans un système informatique, encore une fois des données non structurées ou du texte brut, et nous les classons de quelque manière.

Vous avez en fait vu cela à l'œuvre depuis de nombreuses décennies maintenant, avec la détection de spam, la détection de spam est presque parfaite, elle doit être continuellement mise à jour.

Mais pour la plupart, c'est un problème résolu.

La raison pour laquelle vous avez des e-mails qui vont automatiquement dans votre dossier de spam, c'est parce qu'il y a un modèle d'apprentissage automatique qui se trouve en arrière-plan de votre serveur de messagerie.

Et ce qu'il fait, c'est qu'il regarde en fait les e-mails, il voit s'il correspond au modèle de ce qu'il a vu comme spam auparavant, et il lui attribue une étiquette de spam.

Cela est connu sous le nom de classification.

Cela est également utilisé par les chercheurs, surtout dans l'industrie juridique, les avocats reçoivent souvent des centaines de milliers de documents, sinon des millions de documents, ils n'ont pas nécessairement le temps humain de tout parcourir et d'analyser chaque document mot à mot.

Il est important d'avoir une idée générale des documents sans avoir à les lire page par page.

Et donc, ce que les avocats font souvent, c'est utiliser le NLP pour faire de la classification et de l'extraction d'informations, ils trouveront des mots-clés pertinents pour leur affaire, ou ils trouveront des documents classés selon les domaines pertinents de leur affaire.

Et ainsi, ils peuvent prendre un million de documents et le réduire à peut-être seulement une poignée, peut-être 1000 qu'ils doivent lire mot à mot.

C'est une application réelle du NLP ou du traitement du langage naturel.

Et ces deux tâches peuvent être réalisées grâce au framework spaCy.

spaCy est un framework pour faire du NLP en ce moment.

En 2021, il n'est disponible, je crois, qu'en Python, je pense qu'il y a une communauté qui travaille sur une application avec R mais je ne le sais pas avec certitude.

Mais spaCy est l'un des nombreux frameworks NLP disponibles en Python.

Si vous êtes intéressé à les explorer tous, vous pouvez regarder des choses comme NLTK, le natural language toolkit, stanza, qui je crois provient du même programme à Stanford.

Il y en a beaucoup, mais je trouve que spaCy est le meilleur de tous pour plusieurs raisons.

La première raison est qu'ils fournissent des modèles prêts à l'emploi qui ont de très bonnes performances, c'est-à-dire qu'ils s'exécutent très rapidement.

Et ils ont également de très bonnes métriques de précision telles que la précision, le rappel et le score F.

Et je ne vais pas trop parler de la façon dont nous mesurons la précision de l'apprentissage automatique pour l'instant, mais sachez qu'ils sont très bons.

Deuxièmement, spaCy a la capacité de tirer parti des méthodes actuelles de traitement du langage naturel, spécifiquement les modèles de transformateurs, également connus, généralement collectivement sous le nom de modèles Bert, même si ce n'est pas entièrement exact, mais il permet d'utiliser un modèle de transformateur prêt à l'emploi.

Et troisièmement, il fournit le framework pour faire de l'entraînement personnalisé relativement facilement par rapport à ces autres frameworks NLP qui existent.

Enfin, la quatrième raison pour laquelle j'ai choisi spaCy plutôt que d'autres frameworks NLP est qu'il est bien scalable.

spaCy a été conçu par explosion AI, et le but entier de spaCy est de travailler à l'échelle de l'IA, par échelle, nous entendons travailler avec de grandes quantités de documents de manière efficace, efficace et précise.

spaCy est bien scalable car il peut traiter des centaines de milliers de documents avec une relative facilité en un temps relativement court, surtout si vous restez avec des pipelines plus basés sur des règles, dont nous allons parler dans la deuxième partie de cette vidéo.

Ce sont donc les deux choses que vous devez vraiment savoir sur le NLP et spaCy en général, nous allons parler de spaCy en profondeur alors que nous l'explorons à travers cette vidéo.

Et le manuel gratuit que je fournis pour accompagner cette vidéo, qui se trouve sur spaCy dot python humanities.com.

Et il devrait être lié dans la description ci-dessous cette vidéo et le manuel que j'ai prévu de travailler en tandem.

Certaines choses que je couvre dans la vidéo ne sont pas nécessairement dans le manuel car elles ne se prêtent pas bien à la représentation textuelle.

Et il en va de même pour l'inverse, certaines choses que je n'ai pas le temps de couvrir mot à mot dans cette vidéo, je les couvre un peu plus en profondeur dans la vidéo.

Et dans le livre, je pense que vous devriez essayer d'utiliser les deux, ce que je recommanderais est de faire une première lecture de cette vidéo entière, de la regarder dans son intégralité et d'avoir une idée générale de tout ce que spaCy peut faire.

Et tout ce que nous allons couvrir, je reviendrais et j'essaierais de reproduire chaque étape de ce processus dans une fenêtre séparée ou sur un écran séparé et j'essaierais de suivre et de coder, puis je reviendrais une troisième fois et j'essaierais de regarder la première partie pourquoi parler de ce que nous allons faire et essayer de le faire par moi-même sans regarder le manuel ou la vidéo.

Si vous pouvez faire cela à votre troisième passage, vous serez en très bonne forme pour commencer à utiliser spaCy pour résoudre vos propres problèmes spécifiques à un domaine.

Le NLP est un domaine complexe et l'application du NLP est vraiment complexe.

Mais heureusement, des frameworks comme spaCy rendent ce projet et ce processus beaucoup plus faciles.

Je vous encourage à passer quelques heures sur cette vidéo pour découvrir spaCy et je pense que vous allez trouver que vous pouvez faire des choses que vous ne pensiez pas possibles et relativement rapidement.

Donc, asseyez-vous, détendez-vous et profitez de cette série de vidéos sur spaCy.

Pour utiliser spaCy, vous allez d'abord devoir installer spaCy.

Il y a plusieurs façons de faire cela.

Selon votre environnement et votre système d'exploitation, je recommande d'aller sur spaCy.io/usage et de saisir le bon framework avec lequel vous travaillez.

Donc, si vous utilisez Mac OS, Windows ou Linux, vous pouvez parcourir cette interface utilisateur très pratique et sélectionner les différentes fonctionnalités qui vous intéressent le plus.

Je travaille avec Windows, je vais utiliser PIP dans ce cas, et je vais tout faire sur le CPU.

Et je vais travailler avec l'anglais.

J'ai donc établi tous ces différents paramètres.

Et cela passe en revue et vous dit exactement comment procéder à l'installation en utilisant PIP dans le terminal.

Je vous encourage donc à faire une pause dans la vidéo maintenant et à installer Windows comme vous le souhaitez.

Je vais vous montrer comment l'installer dans le Jupyter Notebook que nous allons utiliser dans un instant.

Je ne veux pas que vous travailliez avec le GPU du tout.

Travailler avec spaCy sur le GPU nécessite une compréhension beaucoup plus approfondie de ce à quoi sert le GPU, spécifiquement dans l'entraînement des modèles d'apprentissage automatique.

Cela nécessite que vous ayez CUDA installé correctement.

Cela nécessite quelques autres choses que je n'ai pas vraiment le temps d'aborder dans cette vidéo, mais nous les aborderons dans une vidéo de tutoriel spaCy plus avancée.

Donc, pour l'instant, je recommande de sélectionner votre système d'exploitation, de sélectionner soit PIP soit conda, puis de sélectionner CPU.

Et puisque vous allez travailler avec cette vidéo avec des textes en anglais, je vous encourage à sélectionner l'anglais maintenant et à installer ou télécharger le modèle N core web SM.

C'est le petit modèle.

J'en parlerai dans un instant.

La première chose que nous allons faire dans notre Jupyter Notebook est d'utiliser le point d'exclamation pour délimiter dans la cellule que ceci est une commande de terminal, nous allons dire pip install spaCy, votre sortie lorsque vous exécutez cette cellule va être un peu différente de la mienne.

J'ai déjà installé spaCy dans cet environnement.

Et donc le mien passe en revue et ressemble à ceci, le vôtre passera en revue et au lieu de dire exigence déjà satisfaite, il passera en revue les différentes choses qu'il installe pour installer spaCy et toutes ses dépendances.

La prochaine chose que vous allez faire est de suivre à nouveau les instructions, et vous allez faire Python dash m space spacey, space download, et ensuite le modèle que vous voulez télécharger.

Donc, allons-y et faisons cela maintenant.

Donc, allons-y et disons Python m spacing.

Download c'est une commande de terminal spaCy.

Et nous allons télécharger le N core web SM et encore une fois, j'ai déjà téléchargé ce modèle donc de mon côté, spaCy va avoir l'air un peu différent de ce qu'il va avoir de votre côté lorsqu'il s'imprime sur le Jupyter Notebook.

Et si nous lui donnons un instant, tout va se passer, et il dit qu'il l'a collecté, il le télécharge.

Et nous sommes tous très heureux maintenant.

Et maintenant que nous avons installé spaCy correctement, et que nous avons téléchargé le petit modèle correctement, nous pouvons commencer à utiliser spaCy et vérifier que tout est correct.

La première chose que nous allons faire est d'importer la bibliothèque spaCy comme vous le feriez avec toute autre bibliothèque Python.

Si vous n'êtes pas familier avec cela, une bibliothèque est simplement un ensemble de classes et de fonctions que vous pouvez importer dans un script Python afin de ne pas avoir à écrire un tas de code supplémentaire.

Les bibliothèques sont des collections massives de classes et de fonctions que vous pouvez appeler.

Donc, lorsque nous importons spaCy, nous importons toute la bibliothèque de spaCy et maintenant que nous avons vu quelque chose comme cela, nous savons que spaCy a été importé correctement, tant que vous n'obtenez pas de message d'erreur, tout a été importé correctement.

La prochaine chose que nous devons faire est de nous assurer que notre modèle English core web SM, notre petit modèle anglais, a été téléchargé correctement.

Donc, la prochaine chose que nous devons faire est de créer un objet NLP.

Je vais en parler beaucoup plus lorsque nous avancerons.

Pour l'instant, cela ne sert qu'à résoudre les problèmes pour nous assurer que nous avons installé spaCy correctement et que nous avons téléchargé notre modèle correctement.

Nous allons donc utiliser la commande spacey dot load.

Cela va prendre un argument, ce sera une chaîne qui correspondra au modèle que vous avez installé.

Et dans ce cas, n cor web s n.

Et si vous exécutez cette cellule et que vous n'avez pas d'erreurs, vous avez installé spaCy correctement et vous avez téléchargé le modèle English core web SM correctement.

Donc, prenez le temps et installez tout cela.

Mettez la vidéo en pause si nécessaire, puis revenez et nous allons commencer à travailler sur les bases de spaCy.

Je vais maintenant passer à une vue d'ensemble de ce qu'il y a dans spaCy, pourquoi c'est utile et quelques-unes des fonctionnalités de base dont vous devez être familier.

Et je vais travailler à partir du Jupyter Notebook dont j'ai parlé dans l'introduction de cette vidéo.

Si nous faisons défiler jusqu'au bas du chapitre un, les bases de spaCy, puis vous passez la section d'installation, vous arrivez à cette section sur les conteneurs.

Donc, qu'est-ce que les conteneurs ? Eh bien, les conteneurs dans spaCy sont des objets qui contiennent une grande quantité de données sur un texte.

Il existe plusieurs conteneurs différents avec lesquels vous pouvez travailler.

Dans spaCy, il y a le doc, le doc Ben exemple, la langue, le lexème, la portée, le groupe de portée et le jeton, nous allons traiter un peu du lexème dans cette série de vidéos.

Et nous allons traiter un peu du conteneur de langue dans cette série de vidéos.

Mais vraiment, les trois grandes choses dont nous allons parler encore et encore sont le dock, la portée et le jeton.

Et je pense que lorsque vous arrivez pour la première fois à spaCy, il y a une petite courbe d'apprentissage sur ce que sont ces choses, ce qu'elles font, comment elles sont structurées hiérarchiquement.

Et pour cette raison, j'ai créé cette image, à mon avis, assez facile à comprendre de ce que sont les différents conteneurs.

Donc, si vous pensez à ce qu'est spaCy comme une pyramide, un système hiérarchique, nous avons tous ces différents conteneurs structurés autour, vraiment l'objet dock, votre conteneur Docker, ou votre objet dock contient une grande quantité de métadonnées sur le texte que vous passez au pipeline spaCy, que nous allons voir en pratique dans quelques minutes.

L'objet doc contient un tas de choses différentes.

Il contient des attributs.

Et ces attributs peuvent être des choses comme des phrases.

Donc, si vous itérez sur doc dot cents, vous pouvez en fait accéder à toutes les différentes phrases trouvées dans cet objet doc.

Si vous itérez sur chaque élément individuel, ou index dans votre objet doc, vous pouvez obtenir des jetons individuels.

Les jetons vont être des choses comme des mots ou des marques de ponctuation, quelque chose dans votre phrase ou texte qui a une valeur importante autonome, soit syntaxiquement soit sémantiquement.

Donc, cela va être des choses comme des mots, une virgule, une période, un point-virgule, une marque de citation, des choses comme celles-ci, tout cela va être vos jetons.

Et nous allons voir comment les jetons sont un peu différents de la simple division des mots avec des méthodes de chaîne traditionnelles en Python.

La prochaine chose avec laquelle vous devriez être familier sont les spans.

Les spans sont importantes car elles existent en quelque sorte à l'intérieur et à l'extérieur de l'objet doc.

Contrairement au jeton, qui est un index de l'objet doc, une span peut être un jeton lui-même, mais elle peut aussi être une séquence de plusieurs jetons, nous allons voir cela en action.

Donc, imaginez si vous aviez une span dans sa catégorie, peut-être que le groupe un est nos lieux.

Donc, un seul jeton pourrait être une ville comme Berlin, mais le groupe de spans deux, cela pourrait être quelque chose comme des noms propres complets.

Par exemple, de personnes.

Donc, cela pourrait être, comme nous allons le voir, Martin Luther King, ce serait une séquence de jetons, une séquence de trois éléments différents dans la phrase qui composent une span, ou un élément autonome.

Donc, Martin Luther King serait une personne qui est une collection d'une séquence de jetons individuels.

Si cela n'a pas de sens pour l'instant, cette image sera renforcée au fur et à mesure que nous apprendrons davantage sur spaCy en pratique.

Pour l'instant, je veux que vous compreniez simplement que l'objet doc est la chose autour de laquelle tout spaCy repose, ce sera l'objet que vous créez.

Ce sera l'objet qui contient toutes les métadonnées dont vous avez besoin pour accéder.

Et ce sera l'objet que vous essayez essentiellement d'améliorer avec différents composants personnalisés, usines et pipelines.

Alors que vous avancez et faites des choses plus avancées avec spaCy, nous allons maintenant voir dans quelques secondes comment cet objet dock est en quelque sorte similaire au texte lui-même.

Mais comment il est très, très différent et beaucoup plus puissant.

Nous allons maintenant passer au chapitre deux de ce manuel, qui va traiter de l'habitude des fonctionnalités approfondies de spaCy.

Si vous voulez mettre la vidéo en pause ou garder ce notebook ou ce livre ouvert séparément de cette vidéo et suivre.

Alors que nous explorons et l'explorons en codage en direct, nous allons parler de quelques choses différentes alors que nous explorons le chapitre deux, cela sera beaucoup plus long que le chapitre un, nous allons non seulement importer spaCy, mais aussi passer en revue et charger un modèle, créer un objet dock autour de ce modèle.

Donc, nous allons travailler avec le conteneur et la pratique.

Et ensuite, nous allons voir comment ce conteneur stocke beaucoup de fonctionnalités différentes ou d'attributs de métadonnées sur le texte.

Et bien qu'ils semblent les mêmes en surface, ils sont en fait assez différents.

Donc, allons-y et travaillons dans notre même Jupyter Notebook où nous avons importé spaCy et nous avons déjà créé l'objet NLP.

La première chose que je veux faire est d'ouvrir un texte pour commencer à travailler dans ce dépôt, nous avons un dossier de données.

Dans ce sous-dossier de données, j'ai quelques ouvertures de Wikipedia différentes, j'en ai une sur MLK que nous allons utiliser un peu plus tard dans cette vidéo.

Et puis j'en ai une sur les États-Unis, c'est wiki underscore us.

C'est ce avec quoi nous allons travailler maintenant.

Donc, utilisons notre opérateur de largeur et ouvrons le dossier de données barre oblique wiki underscore us point txt.

Nous allons simplement le lire comme F.

Et ensuite nous allons créer cet objet texte qui sera égal à F point read.

Et maintenant que nous avons créé notre objet texte, allons-y et voyons à quoi cela ressemble.

Donc, imprimons le texte.

Et nous voyons que c'est un article Wikipedia standard qui suit ce même format d'introduction et il fait environ quatre ou cinq paragraphes de long avec beaucoup des fonctionnalités laissées telles que les crochets qui délimitent une sorte de note de bas de page.

Nous ne allons pas trop nous soucier de nettoyer cela maintenant, car nous sommes intéressés non pas par le nettoyage de nos données, mais plutôt par commencer à travailler avec l'objet doc dans spaCy.

Donc, la première chose que vous voulez faire est de créer un objet doc.