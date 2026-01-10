---
title: Développement Web Backend avec Python - Cours Complet
date: '2021-07-01T16:51:30.000Z'
author: Beau Carnes
authorURL: https://www.freecodecamp.org/news/author/beaucarnes/
originalURL: https://freecodecamp.org/news/backend-web-development-with-python-full-course
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/backendpython.png
tags: []
seo_desc: 'The backend of a website can be written in many different programming languages.
  It is becoming increasingly common for to use Python for the backend of a website.

  We just published a full backend web development with Python course on the freeCodeCam...'
---


Le backend d'un site web peut être écrit dans de nombreux langages de programmation différents. Il est de plus en plus courant d'utiliser Python pour le backend d'un site web.

<!-- more -->

Nous venons de publier un cours complet sur le développement web backend avec Python sur la chaîne YouTube de freeCodeCamp.org.

Ce cours complet s'adresse aux débutants absolus et vous enseignera le développement web backend avec Python. Vous apprendrez les bases de Python et de Django, et créerez plusieurs projets au cours de votre apprentissage.

Tomi Tokko a créé ce cours. Tomi a réalisé de nombreux cours populaires tant sur sa propre chaîne que sur celle de freeCodeCamp.

Voici la liste complète des sujets abordés dans ce cours :

-   Introduction à Python
-   Installation de Python
-   Hello World en Python
-   Variables en Python
-   Chaînes de caractères (Strings) en Python
-   Nombres en Python
-   Récupérer l'entrée d'un utilisateur
-   Exercice de remplacement de mots
-   Listes en Python
-   Méthodes de liste
-   Tuples en Python
-   Fonctions en Python
-   Le mot-clé Return
-   Instructions IF en Python
-   Création d'un programme de vérification de nombres pairs
-   Dictionnaires en Python
-   Boucles While en Python
-   Boucles For en Python
-   Listes 2D
-   Commentaires en Python
-   Création d'une calculatrice basique
-   Try Except en Python
-   Lecture de fichiers
-   Écriture de fichiers
-   Classes et objets en Python
-   Héritage en Python
-   Le Shell Python
-   Création d'un système simple de connexion et d'inscription
-   Modules et PIP en Python
-   Introduction à Django
-   Installation de Django
-   Routage URL et applications Django
-   Langage de template Django
-   Envoi de données au fichier de template
-   Création d'un compteur de mots en Django
-   Get vs Post en Django
-   Fichiers statiques en Django
-   Introduction aux modèles Django
-   Panneau d'administration Django et manipulation de base de données
-   Inscription utilisateur en Django
-   Connexion et déconnexion utilisateur en Django
-   Routage URL dynamique en Django
-   Configuration de PostgreSQL
-   Création d'un blog avec Django - Partie 1
-   Création d'un blog avec Django - Partie 2
-   Création d'une application météo avec Django - Partie 1
-   Création d'une application météo avec Django - Partie 2
-   Création d'une application de chat en temps réel avec Django - Partie 1
-   Création d'une application de chat en temps réel avec Django - Partie 2
-   Cours accéléré sur Django Rest Framework

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube de freeCodeCamp.org][1] (durée de 10 heures).

<iframe width="560" height="315" src="https://www.youtube.com/embed/jBzwzrDvZ18" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

## Transcription

(générée automatiquement)

Ce cours complet s'adresse aux débutants absolus et vous enseignera le développement web backend avec Python.

Vous apprendrez les bases de Python et de Django et créerez quelques projets en cours de route.

Tomi a créé de nombreux cours populaires, tant sur sa propre chaîne que sur la chaîne Free Code Camp.

Hé les gars, bienvenue dans ce cours de développement web backend avec Python.

Dans ce cours, nous allons apprendre tout ce que vous devez savoir pour commencer votre voyage dans le développement web avec Python.

Jetons un coup d'œil rapide au programme de cette vidéo.

Tout d'abord, nous commencerons par apprendre Python, qui est le langage de programmation que nous allons utiliser dans cette vidéo.

Dans le tutoriel Python, il y aura beaucoup d'exercices que nous ferons ensemble juste pour nous familiariser avec le langage de programmation Python.

Une fois que nous serons familiers avec Python, nous passerons directement à Django.

Django est un framework Python utilisé pour créer des applications web côté serveur.

Dans le tutoriel Django, nous apprendrons tous les concepts que vous devez connaître pour bien débuter avec Django.

Après cela, nous allons construire trois projets différents en utilisant Django.

Les projets que nous allons réaliser sont une application de blog, un programme de détection météo et une application de chat en temps réel avec Django.

Nous allons construire ces projets pour que vous vous habituiez à construire vos propres projets avec Django.

Après cela, vous serez initiés aux APIs avec Django, vous apprendrez comment vous pouvez exposer des APIs REST dans Django en utilisant le Django Rest Framework.

Et j'espère qu'après cette vidéo, vous serez à l'aise pour construire vos propres applications web côté serveur en utilisant Django.

Maintenant, j'ai quelques ressources gratuites comme une roadmap Django, un aide-mémoire sur les structures de données Python, un aide-mémoire Django et bien d'autres ressources gratuites compilées dans un PDF.

Et vous pouvez télécharger ce PDF gratuitement en utilisant le lien dans la description ci-dessous.

Et si vous voulez plus de tutoriels comme celui-ci, vous pouvez également consulter ma propre chaîne "Code with Tomi" où j'enseigne davantage Python et le développement web en général.

Maintenant que vous savez cela, plongeons directement dans cette vidéo.

Ce tutoriel est très complet car nous allons apprendre la programmation Python à partir de zéro.

Voici donc une liste de tout ce dont nous allons parler dans cette vidéo.

Permettez-moi de faire une brève introduction à Python.

Python est l'un des langages de programmation dont la croissance est la plus rapide au monde.

Avec Python, vous pouvez vous lancer dans divers domaines comme le machine learning et l'IA, le développement web, et bien d'autres encore.

Apprendre Python est donc une très bonne décision pour votre parcours de programmation.

Sans perdre de temps, passons directement au tutoriel.

Ici même, je suis sur mon navigateur.

Nous allons télécharger Python sur notre ordinateur.

Pour ce faire, je vais simplement chercher "download Python for Windows" puisque je suis sur Windows, et je vais cliquer sur le premier lien.

Et puis ici, je vois "download Python 3.9.1", qui est la dernière version.

Nous allons donc cliquer dessus.

Et vous pouvez voir qu'il l'a téléchargé automatiquement.

J'ai déjà téléchargé Python.

Maintenant, ce que je dois faire, c'est l'installer, je vais aller là où je l'ai sauvegardé.

Et puis je vais l'exécuter.

Assurez-vous que lorsque vous installez Python, vous cochez bien "Add Python to PATH".

Sinon, cela va rendre les choses plus complexes.

C'est censé être simple pour vous.

Cliquons sur "Install Now".

Oui.

Et donc cela va installer Python sur notre machine.

Cela devrait prendre quelques minutes pour s'installer.

Et je reviendrai quand l'installation sera terminée.

Maintenant, l'installation a réussi.

Comme vous pouvez le voir, l'installation est terminée.

Je peux donc cliquer sur "Close".

Maintenant, pour confirmer que Python est bien installé, je vais ouvrir mon invite de commande.

Ici, dans mon invite de commande, je vais simplement taper `python`.

Une fois que je l'ai tapé, cela devrait ouvrir ce shell.

Vous ne comprenez peut-être pas tout cela maintenant.

Mais c'est juste pour vérifier si Python a été vraiment installé.

Maintenant que nous savons que Python est installé, installons notre éditeur de code.

Python est le langage de programmation.

Mais nous allons coder, nous allons tout programmer dans un éditeur de code.

Et il existe divers éditeurs de code.

Nous avons Visual Studio Code, PyCharm, Sublime Text, Atom.

Il y en a énormément, mais pour ce tutoriel, nous allons utiliser Visual Studio Code.

Allons-y et téléchargeons-le.

Je peux fermer mon invite de commande maintenant.

Laissez-moi juste dire que si vous ne savez pas comment accéder à votre invite de commande, vous pouvez simplement la chercher dans votre barre de recherche Windows.

Ici, nous pouvons retourner sur Google.

Et puis nous pouvons chercher, disons "download Visual Studio Code".

Et je vais cliquer sur le premier lien.

Puisque je suis sur Windows, je vais télécharger celui pour Windows.

Si vous êtes sur Ubuntu, Linux ou Mac, téléchargez celui correspondant à votre OS.

Maintenant, vous pouvez voir qu'il est en train de se télécharger.

Je l'ai déjà téléchargé sur mon PC, je vais donc annuler puisque je l'ai déjà.

Laissez-moi juste vous montrer le processus d'installation.

Ici, je l'ai déjà téléchargé, nous cliquons simplement sur Entrée pour l'exécuter.

Ce qu'il me dit ici, c'est que l'installation a détecté que Visual Studio Code est en cours d'exécution.

Cela signifie simplement que j'ai déjà Visual Studio Code installé sur mon ordinateur.

Je vais donc appuyer sur "Annuler".

Mais pour vous, en tant que débutant, vous voudrez l'installer comme un nouveau logiciel.

Une fois que nous l'avons installé, nous allons simplement ouvrir notre Visual Studio Code, et voici à quoi cela devrait ressembler une fois que vous l'ouvrez pour la première fois.

Maintenant, nous avons tout configuré.

Nous avons téléchargé Python et l'avons installé.

Et puis nous avons téléchargé Visual Studio Code et l'avons installé.

Maintenant, nous pouvons passer directement au codage.

Maintenant que nous avons tout installé, ce que nous voulons faire, c'est créer un nouveau fichier, et c'est dans ce fichier que nous allons coder tout notre Python.

Dans Visual Studio Code, nous allons aller dans la barre d'outils et cliquer sur "New File".

Une fois que nous cliquons sur "New File", vous pouvez voir qu'il a automatiquement ce nom "Untitled", mais je veux le sauvegarder en appuyant sur Ctrl+S.

Et je vais le sauvegarder.

Tout d'abord, laissez-moi dire "All files" là, maintenant pour le sauvegarder sous `app.py`.

Le nom du fichier est `app`.

Mais à la fin de l'extension du fichier, j'ai utilisé `.py`.

Chaque fois que nous travaillons avec Python, chaque fois que vous créez un nouveau fichier Python, il doit toujours avoir l'extension `.py`, cela permettra à tout ce que nous exécutons de savoir que nous utilisons un fichier Python.

Maintenant, une fois que je l'ai sauvegardé, il est mis à jour ici.

Et comme vous pouvez le voir, Visual Studio Code détecte automatiquement le logo de Python. Voilà comment sauvegarder et créer un nouveau fichier Python.

C'est fondamentalement à quoi tout ressemble dans Visual Studio Code.

Sur la barre de gauche, nous avons la barre d'exploration, si nous ouvrons un dossier, c'est là que nous verrons tous les fichiers et dossiers qu'il contient.

Nous avons la recherche, GitHub.

Nous n'avons pas besoin de nous en soucier pour l'instant.

Mais voici à quoi ressemble Visual Studio Code.

Puisque nous avons tout, nous savons comment créer un nouveau fichier, ce dont nous voulons parler maintenant est la fonction `print`.

En Python, nous avons des fonctions intégrées, ce qui signifie que certaines choses sont déjà faites automatiquement, nous n'avons pas besoin d'écrire trop de code.

Maintenant, disons que nous voulons simplement afficher du texte à l'écran.

Comme nous voulons simplement montrer à un utilisateur un "Hello World" ou un message de bienvenue, nous allons utiliser la fonction `print`, elle va afficher du texte de base à l'écran.

Pour ce faire, nous allons écrire `print`, puis nous allons ouvrir des parenthèses.

Et ensuite, nous pouvons utiliser des guillemets simples.

Ou nous pouvons aussi utiliser des guillemets doubles.

Il n'y a pas de problème ici en Python.

Mais nous pouvons simplement utiliser des guillemets simples.

Dans ces guillemets, je vais écrire mon texte comme `Hello World`.

Maintenant, comme vous pouvez le voir, j'ai écrit `print('Hello World')`.

Et je dois m'assurer de sauvegarder ce fichier.

Et puis pour que j'exécute ce fichier Python, pour que je voie le résultat de mon code, je vais devoir aller dans le coin supérieur droit ici et cliquer sur "Run".

Une fois que je clique sur "Run", vous voyez qu'il ouvre automatiquement un nouveau terminal.

Et notre code va être exécuté dans ce terminal.

Si nous attendons une seconde, nous allons voir le résultat de ce code.

Vous pouvez voir ici même que nous avons `Hello World` qui s'affiche automatiquement.

Si je dis `Hello World Welcome` et que je l'exécute, vous voyez que cela change et affiche `Hello World Welcome`.

Voilà comment exécuter un fichier Python.

Parlons maintenant de quelques fonctionnalités supplémentaires de cette fonction `print`.

Maintenant, disons que nous voulons afficher sur une nouvelle ligne.

`Hello World`, et je voulais que `Welcome` soit sur une autre ligne, nous pouvons facilement le faire, nous pouvons simplement enlever ceci.

Et puis sur une nouvelle ligne, nous allons simplement faire un `print` de `Welcome` exactement de la même manière.

Une fois que je l'exécute, vous pouvez voir qu'il affiche `Hello World` en haut, et `Welcome` en bas, voilà comment afficher sur une nouvelle ligne, nous pouvons aussi faire beaucoup de choses, disons que nous voulons ajouter une autre valeur à ce `Hello World`.

Comme, affichons une phrase, disons `My name is Tomi`.

Et puis je veux dire `My age is`, alors je peux ajouter une virgule ici et dire `100`.

Cela dira automatiquement à Python que c'est un nombre, et ce n'est plus une chaîne de caractères (string), juste un caractère normal.

Maintenant, une fois que je l'exécute, vous allez voir qu'il affiche `My name is Tomi my age is 100`, sans erreurs.

Et automatiquement, vous voyez qu'il laisse un espace ici, ici même, nous n'avons pas laissé d'espace, mais automatiquement une fois que nous mettons ce nombre ici, il laisse un espace pour clarifier. Si je ne laisse pas d'espace et que je l'exécute, vous voyez que l'espace est toujours là.

C'est juste une fonctionnalité intelligente de Python.

Je pense que ce sera tout pour la fonction `print`.

Parlons maintenant des variables en Python.

Comme vous pouvez le voir, j'ai trois fonctions `print`.

La première dit `Tim is a boy`.

La deuxième dit `Tim is 18`.

Et la troisième dit `Tim is from Turkey`.

Comme vous pouvez le voir, dans les trois fonctions `print`, je répète `Tim` trois fois.

Maintenant, nous pouvons utiliser des variables au lieu de répéter un texte particulier.

Les variables consistent essentiellement à sauvegarder une donnée dans la mémoire de Python.

Et ensuite, nous pouvons récupérer cette donnée en référençant son nom.

Voyons cela en action.

Disons qu'au-dessus du code, j'ai une variable nommée `name`.

Ce `name` est le nom de la variable.

Et je dis `equals to`, je mets des guillemets simples, et le nom est `Tim`.

Donc `name` est le nom de la variable.

Et `Tim` est la valeur assignée à ce nom.

Ainsi, nous avons sauvegardé cette variable ici.

Nous pouvons l'afficher, nous disons aussi `print`.

Chaque fois que nous affichons une variable, nous ne mettons pas de guillemets comme nous le faisons lorsque nous affichons une chaîne de caractères normale.

Nous pouvons donc enlever les guillemets et simplement taper le nom de la variable qui est `name`.

Maintenant, quand j'exécute ceci, vous allez voir qu'il affiche tout cela.

Et sur la quatrième ligne, il affiche `Tim`.

Il n'a pas affiché `name`.

C'est ce qu'est une variable, c'est essentiellement sauvegarder une donnée particulière et ensuite la référencer via le nom de la variable.

Maintenant, au lieu de dire `Tim` trois fois, nous pouvons simplement remplacer ce `Tim` par `name`.

Et pour que nous fassions cela ici, vous voyez que nous avons affiché seulement la variable.

Et nous n'avions pas de guillemets.

Mais ici, nous affichons une chaîne de caractères avec des guillemets.

Et nous voulons aussi afficher la variable avec elle.

C'est ce qu'on appelle la concaténation.

Nous allons joindre la variable et la chaîne de caractères normale ensemble.

Pour faire cela.

Enlevons `Tim`.

Et nous allons dire `name`, qui est le nom de la variable, plus le texte restant.

Maintenant, ce que fait `name + ' is a boy'`, c'est qu'il va nous afficher `Tim is a boy`.

Nous pouvons aussi faire la même chose ici.

Nous enlevons simplement `Tim`, nous disons `name + ' is 18'`.

Nous faisons la même chose pour la troisième ligne, nous disons `name + ' is from Turkey'`.

Maintenant, une fois que nous affichons cela, vous pouvez voir qu'il dit `Tim is a boy`, `Tim is 18`, `Tim is from Turkey`.

Alors qu'ici nous avons écrit `name`.

C'est à cela que servent les variables.

Tapons simplement `CLS` pour nettoyer tout ça.

Mais les variables sont plus vastes que cela.

Il y a quelque chose que nous appelons les types de données (data types).

Comme vous pouvez le voir, ceci est juste `Tim`, `Tim` est composé de lettres, c'est une chaîne de caractères (string).

Les chaînes de caractères sont essentiellement des caractères.

Une chaîne de caractères est un type de données.

Nous avons, si c'est un nombre comme `23`, ce n'est plus une chaîne de caractères, c'est maintenant un entier (integer).

Nous avons les booléens (Boolean) qui sont pour les valeurs vraies ou fausses (true/false) et tout cela.

Laissez-moi juste annuler cela.

Laissez-moi spécifier une nouvelle variable et la nommer `age`.

Cette variable, je veux que ce soit l'âge.

Donnons-lui `18`.

Chaque fois que nous utilisons un entier ou un nombre, nous n'ajoutons pas de guillemets lorsque nous assignons la variable.

Vous voyez ici, nous avons ajouté des guillemets, et à l'intérieur de ces guillemets nous avons mis `Tim`, mais pour que ce soit un entier, vous verrez que nous n'ajoutons pas de guillemets.

Si je survole ceci, vous voyez qu'il dit que `18` est un `int`, qui signifie entier, et puis `Tim` ici est une chaîne de caractères (string).

Maintenant, nous pouvons simplement joindre cela en disant `+ age`.

Une fois que nous affichons cela, cela va toujours nous donner... D'accord, vous pouvez voir maintenant que cela ne peut concaténer que des chaînes de caractères, pas des entiers.

Il y a donc un problème avec Python.

Chaque fois que je veux concaténer une chaîne de caractères avec une variable, cela ne fonctionne pas, je veux dire, un entier avec une chaîne de caractères, cela ne fonctionne pas.

Nous pouvons donc résoudre cela au lieu d'utiliser ceci, nous pouvons dire `, age`.

Une fois que nous appuyons sur ceci, vous pouvez voir qu'il dit `Tim is from Turkey`.

Laissez-moi fermer ceci.

Ici, nous pouvons voir que chaque fois que nous concaténons seulement des chaînes de caractères, c'est possible.

Mais quand nous traitons avec un entier, nous ne pouvons pas utiliser ce `+`, nous devons utiliser une virgule.

Et nous pouvons aussi utiliser une virgule lorsque nous concaténons avec une chaîne de caractères également.

Ce sont les deux choses, nous pouvons utiliser le signe d'addition avec seulement des chaînes de caractères.

Et ensuite, nous pouvons utiliser la virgule avec des chaînes de caractères et des entiers.

Si je l'exécute, cela va fonctionner, `Tim is 18`, c'est fondamentalement comment concaténer et joindre des chaînes de caractères avec des variables.

Maintenant, nous allons parler davantage des chaînes de caractères (strings).

Les chaînes de caractères sont juste du texte brut.

Si j'affiche quelque chose comme `print('Alright this is a string')`. Les chaînes de caractères sont juste du texte brut.

Maintenant, nous allons parler davantage des fonctionnalités des chaînes de caractères, des différentes choses que vous pouvez faire avec elles.

Disons que je dis, je mets un point.

Oh, vous savez, une fois que je l'exécute, vous voyez qu'il l'exécute sur la même ligne, qui est `I will you wave`, si je veux que ce soit sur une autre ligne sans être mis dans une autre fonction `print`, je peux simplement utiliser un `\n`.

C'est un `\n`.

Cela va automatiquement amener ceci sur une nouvelle ligne, c'est juste comme un saut de ligne, cela va ajouter un saut de ligne entre ceci et cela.

Maintenant, une fois que je l'exécute, vous allez voir qu'il dit `I`, `our you will have this space here` à cause de cela, si je peux enlever cela et que je l'exécute à nouveau, vous allez voir que nous avons `I owe you`.

Nous pouvons aussi afficher une chaîne de caractères en tant que variable.

Disons que nous avons quelque chose nommé `name`, et le nom est `Tim`.

C'est une chaîne de caractères, c'est une variable, mais un type de variable chaîne de caractères.

Et ensuite, dans la fonction `print`, nous affichons aussi cette variable chaîne de caractères en disant simplement `print(name)`, sans guillemets.

Une fois que vous l'affichez, vous allez voir ici même que nous avons `Tim` affiché. Fermons tout ça.

Si nous venons ici, nous pouvons aussi afficher, disons que nous voulons ajouter des guillemets doubles ou des guillemets simples.

Vous savez que nous ne pouvons pas ajouter de guillemets simples au milieu de notre texte parce que Python va voir cela comme si nous voulions fermer ce texte à afficher.

Pour ajouter les guillemets doubles, nous pouvons simplement ajouter le backslash `\` puis les guillemets.

Maintenant, une fois que vous avez un backslash, et ces guillemets, ces guillemets vont être affichés. Si je l'exécute, vous voyez maintenant que nous avons `I` avec ces guillemets `hour you`.

Donc si vous voulez créer des caractères spéciaux, nous utilisons le backslash, ou vous pouvez simplement afficher le backslash seul, cela va fonctionner.

Vous pouvez voir que le backslash est là.

Nous pouvons donc afficher.

Utilisez-les.

Backslash pour casser, pour le mettre sur une nouvelle ligne, parce qu'il y a un backslash pour ajouter des guillemets.

Et ensuite, nous pouvons afficher le backslash juste comme ça.

Laissez-moi vous parler des fonctions spéciales sur les chaînes de caractères.

Les fonctions en Python sont juste un bloc de code qui effectue une tâche particulière.

Donc, dans ces chaînes de caractères, il y a beaucoup de fonctions qui font différentes choses.

Disons que nous voulons convertir tous les caractères de ceci en majuscules, nous pouvons utiliser une fonction de chaîne de caractères, nous voulons vérifier si c'est en minuscules, ou nous voulons accéder à la première lettre, ou à la seconde, ce sont des fonctions en Python.

Maintenant, nous pouvons simplement dire que nous voulons obtenir seulement la première lettre.

Une fois que nous obtenons la première lettre, nous pouvons simplement faire quelque chose comme `print(name[0])`.

Maintenant, `0` représente la première lettre, si je dis `1`, cela représente la deuxième lettre, si je dis `2`, cela représente la troisième lettre.

En Python, ou en programmation en général, les nombres commencent à compter à partir de zéro.

Donc, une fois que je mets `0` et que je l'exécute, en bas ici, vous voyez qu'il affiche seulement `T`.

Maintenant, laissez-moi mettre `2` qui est la troisième, vous voyez qu'il affiche seulement `m`.

Et si je mets ce qui n'est pas là, comme `3`, cela va nous donner une erreur, `index error`.

Vous pouvez voir `string index out of range`, ce qui signifie que ce n'est pas présent.

On peut aussi faire plusieurs choses.

Disons que nous voulons convertir tout cela en majuscules, nous pouvons simplement faire `name.upper()`.

Maintenant, une fois que nous exécutons ceci, s'il dit qu'il n'a pas d'attribut `upper case`, c'est parfois parce que nous rencontrons une erreur, nous changeons simplement.

Je pense que c'est parce qu'il ne doit pas y avoir `case`.

Donc `name.upper()` est la fonction qui le change en majuscules.

Une fois que je l'exécute, vous voyez maintenant que nous avons `TIM` en majuscules.

Nous pouvons aussi faire la même chose avec `lower`, nous disons simplement `name.lower()`, et ensuite nous l'exécutons, maintenant vous pouvez voir que tout a été changé en minuscules.

Maintenant, une fois que nous revenons ici, nous pouvons aussi vérifier si tout ce qui est présent ici est en majuscules, ou si tous les caractères sont en minuscules.

Pour que nous fassions cela, nous allons simplement dire `name.islower()`.

Maintenant que je l'exécute, vous voyez qu'il dit `False`, donc cela va me donner une réponse vraie ou fausse (True/False).

Si tout est en majuscules, cela va me donner `False`, mais si c'est en minuscules, cela va me donner `True`.

Vous pouvez voir, puisqu'il y a un `T` majuscule, j'ai demandé si c'est en minuscules, et il dit `False`.

Mais si je demande si c'est en majuscules (`isupper()`), je l'exécute.

Si c'est `False`, c'est simplement parce qu'il y a des majuscules et des minuscules, tout n'est pas en majuscules ou en minuscules.

Mais si je le change en minuscules, laissez-moi tout changer en majuscules `TIM`, et ensuite je l'exécute, vous voyez maintenant c'est `True`, parce que tout est en majuscules, et nous pouvons aussi joindre différentes fonctions ensemble.

Maintenant, vous pouvez voir si je dis quelque chose comme `islower()` et que je l'exécute, il dit `False`.

Mais je peux d'abord le convertir en minuscules, puis demander si c'est en minuscules, donc je peux faire `.lower().islower()`.

Et ensuite exécuter.

Vous voyez maintenant qu'il dit `True`.

Alors que c'est en majuscules.

Donc, tout d'abord, il dit `name.lower()`, ce qui signifie le convertir en minuscules, puis il vérifie si c'est en minuscules, ce qui nous donne `True`.

C'est fondamentalement comment joindre différentes ou ajouter différentes fonctions ensemble.

Nous pouvons aussi faire autre chose en disant, disons que nous voulons obtenir le nombre de caractères que nous avons dans cette variable.

Pour faire cela, nous pouvons dire `len()`, puis nous ouvrons une parenthèse et la fermons.

Quand nous exécutons ceci, vous pouvez voir qu'il nous donne `3` parce que nous avons `1 2 3`. Si j'en ai beaucoup, et qu'ensuite je l'exécute, cela va me donner `18`, le nombre que nous avons là-dedans.

C'est ainsi qu'on obtient la longueur d'une chaîne de caractères.

Mais laissez-moi juste annuler cela.

Mais disons que nous voulons trouver où se trouve un texte particulier.

Voici `i`, disons que nous voulons obtenir le numéro d'index de `i`, comme nous le savons, c'est `0` et `1`.

Donc cet `i`, son numéro d'index est `1`, si nous voulons l'obtenir, nous allons simplement dire... nous allons enlever `len`.

Je vais donc dire `name.index('i')`.

Maintenant, il va m'afficher `1`, parce que c'est le numéro d'index de `i`. Une fois que je l'exécute, vous voyez qu'il m'affiche `1`, qui est le numéro d'index.

Maintenant, disons que nous voulons remplacer un texte, disons que nous avons `m` et que nous voulons le remplacer par `c`.

Nous pouvons facilement le faire.

Nous allons simplement dire `name.replace('m', 'c')`.

Maintenant, une fois que j'exécute ceci, vous pouvez voir qu'il a affiché `Tic`.

C'est donc remplacer ce `m` par `c`, c'est fondamentalement comment remplacer.

Il y a aussi beaucoup de fonctions, beaucoup de fonctions de chaînes de caractères.

Mais ce ne sont que quelques-unes, je vous ai montré comment les utiliser.

Ce sera tout pour les chaînes de caractères.

Dans cette partie, nous allons parler des nombres en Python.

Afficher un nombre en Python est assez facile.

Nous tapons simplement `print`, puis nous tapons le nombre `78`.

Une fois que nous l'exécutons, vous verrez qu'il affiche `78`.

Nous n'avons donc pas besoin d'ajouter de syntaxe ou quoi que ce soit, nous affichons simplement `78` et cela nous donne `78`.

Nous pouvons aussi spécifier un nombre dans une variable, nous pouvons dire `number = 79`. Nous écrivons simplement le nombre, nous n'avons pas besoin d'ajouter de guillemets.

Et ensuite, nous pouvons afficher `number`.

Une fois que vous l'exécutez, cela nous donne `78` et `79`.

Nous pouvons aussi additionner des nombres.

Laissez-moi simplement enlever ceci.

Au lieu d'afficher seulement `78`, nous pouvons afficher `78 + 22`.

Maintenant, nous pouvons additionner un nombre, nous pouvons effectuer des opérations arithmétiques.

Une fois que je l'exécute, vous voyez qu'il me donne `100`, il additionne automatiquement ces deux nombres ou entiers ensemble, et ensuite il l'exécute.

Je peux aussi essayer cela avec un nombre décimal `2.7`.

Ensuite, une fois que je l'exécute, vous verrez qu'il me donne `100.934`.

C'est ainsi que fonctionnent les nombres.

Et nous pouvons aussi tester avec la soustraction.

Cela nous donne `55.066`.

Et ensuite, nous pouvons tester avec la division, cela nous donne la réponse.

Et ensuite, nous pouvons aussi tester avec la multiplication.

Quand nous l'exécutons, cela nous donne la réponse.

C'est fondamentalement l'opération arithmétique de base avec Python, nous pouvons aller plus loin juste comme ce que nous avons fait avec les chaînes de caractères, nous pouvons aller plus loin et utiliser les fonctions de nombres intégrées.

Disons que je veux montrer le reste d'une division.

Disons quelque chose comme `20` divisé par `6`.

Vous savez que cela nous donnera `3` reste `2`.

Cela va nous donner `3` reste de ceci.

Mais si nous voulons seulement obtenir le reste, nous ne voulons pas obtenir la réponse principale, nous pouvons simplement faire `20 % 6`. Une fois que je l'exécute, vous voyez qu'il me donne `2`, qui est le reste.

C'est ainsi qu'on obtient le reste d'une division. Nous pouvons aussi convertir un nombre en chaîne de caractères.

Laissez-moi vous montrer.

Disons que nous avons cette variable.

Nous avons une variable nommée `number = 55`. Vous pouvez voir que c'est un nombre, un entier ici même.

Ensuite, je peux spécifier une nouvelle variable, je peux la nommer `number2`, et je veux que ce nombre soit une chaîne de caractères.

Je vais donc dire que c'est le `str(number)`.

Maintenant, si je survole ce `number2`, vous allez voir que c'est une chaîne de caractères, quand j'affiche `number2`, cela va être `55`. Mais maintenant c'est une chaîne de caractères `55` aussi.

Comment savoir si c'est vraiment une chaîne de caractères ? Rappelez-vous que lors de la concaténation, vous ne pouvez pas concaténer des nombres, mais vous pouvez concaténer des chaînes de caractères.

Essayons de concaténer.

Ici même, disons.

`Number is`, essayons de concaténer avec le nombre principal.

Disons `+ number`.

Exécutons-le, vous voyez qu'il nous donne une erreur, ne peut concaténer que des chaînes de caractères, pas des entiers.

Mais maintenant que nous l'avons converti, essayons de concaténer avec `num2`. Une fois que nous l'exécutons, vous voyez qu'il nous donne `Number is 55`.

C'est pour montrer qu'il a converti cet entier ou ce nombre en une chaîne de caractères.

Maintenant, Python voit cela comme une chaîne de caractères, c'est aussi très utile dans beaucoup de cas.

C'est tout pour cela.

Et ensuite, nous pouvons aussi obtenir la valeur absolue d'un nombre.

Annulons cela, affichons `-5`.

Évidemment, quand nous l'affichons, cela devrait nous donner `-5`, comme vous pouvez le voir en bas ici, fermons tout ça.

Et si je voulais qu'il affiche seulement `5` quel que soit le signe, s'il est positif ou négatif, je vais ajouter `abs()`.

C'est une fonction, c'est une fonction de nombre, comme je l'ai expliqué plus tôt, une fonction est juste un bloc de code qui effectue une tâche particulière.

Nous pouvons écrire une fonction manuellement par nous-mêmes.

Mais Python a des fonctions intégrées que vous pouvez utiliser automatiquement.

C'est pourquoi quand nous utilisons `abs`, il le voit automatiquement comme une fonction Python.

Cet `abs` signifie absolue, c'est la signification complète de `abs`, nous allons donc obtenir la valeur absolue de ce nombre.

Maintenant, quand je l'exécute, vous voyez qu'il affiche seulement `5`, quel que soit ce signe négatif à côté.

Nous avons `4` et `2`.

Maintenant, vous savez que `4` est évidemment plus grand que `2`.

Une fois que j'affiche cela, cela va me donner `4`, c'est montrer le nombre le plus élevé de ceci.

Cela signifie que nous avons ces deux nombres, `max()` va obtenir le nombre le plus élevé.

Disons que nous avons un autre nombre nommé `3`, une fois que je l'exécute, il va toujours afficher `4`, parce que `4` est plus grand que tout cela. Maintenant, si j'ai `16`, une fois que je l'exécute, il me donne `16`. Parce que `16` est le nombre le plus élevé dans cette plage de nombres, je peux aussi faire la même chose pour obtenir le montant minimum de nombres, je peux dire `min()`. Cela va donc afficher automatiquement `2` parce que c'est le minimum. Une fois que je l'exécute, vous voyez qu'il affiche `2`. C'est la manière de base d'obtenir le maximum et le minimum. Et ensuite, il y a l'arrondi d'un nombre aussi.

Nous pouvons estimer un nombre.

En mathématiques normales, si nous avons quelque chose comme `3.2`, c'est estimé à `3`, mais si nous avons quelque chose comme `3.5`, c'est estimé à `4`. Nous pouvons aussi faire cela ici en Python.

Pour faire cela, nous disons simplement `round()`. `round(3.2)` va nous donner `3`, mais si nous arrondissons `3.5`, cela va nous donner `4`, juste une estimation normale, arrondir un nombre.

Et ensuite, nous en avons un autre, qui est `bin()`.

Ce que fait ce `bin`, c'est qu'il convertit un nombre particulier en une chaîne binaire.

Si vous connaissez les nombres binaires, c'est ce type de texte bizarre.

Chaque nombre a sa chaîne binaire, nous obtenons la chaîne binaire d'un nombre, nous l'exécutons simplement, et il affiche ceci.

Exécutons quelque chose comme `334`.

Il affiche la chaîne binaire pour `334`.

Ce sont quelques fonctions de base.

Mais il y a d'innombrables fonctions pour d'innombrables nombres.

Toutes celles-ci, nous pouvons y accéder parce qu'elles sont déjà intégrées dans Python.

Mais il y en a encore plus auxquelles nous ne pouvons pas accéder.

Sauf si nous les importons.

Il y a quelque chose en Python appelé imports.

Nous avons plus de fonctions de nombres, celle qui peut trouver la racine carrée, celle qui peut obtenir la puissance, diverses fonctions innombrables.

La raison pour laquelle nous ne pouvons pas accéder à celles-là, c'est parce que nous ne les avons pas importées. Celles que je viens de vous montrer, nous pouvons les utiliser sans importer.

Mais celles que je veux vous montrer maintenant, nous devons les importer de la fonction `math` de Python avant de pouvoir les utiliser.

Pour importer, nous allons dire `from math import *`.

Ce que cela fait, c'est dire que de la classe `math` ou de la fonction `math`, importe tout ce qui s'y trouve.

Maintenant, dans cette classe ou fonction `math`, il peut y avoir celle qui peut trouver la racine carrée, celle qui peut trouver la puissance, tout.

Nous ne savons pas encore celle que nous voulons.

Nous importons donc tout avec cet astérisque.

Puisque nous avons importé cela, nous pouvons trouver la racine carrée.

Nous pouvons simplement dire racine carrée (`sqrt`) de... faisons quelque chose comme `100`.

Une fois que nous exécutons cela, cela nous donnera `10`.

Comme vous pouvez le voir, cela nous donne `10`. Aujourd'hui, ce point `00` est correct, mais maintenant cela nous donne `10`.

Ce sera tout sur le travail avec les nombres.

Dans cette partie, nous allons récupérer l'entrée des utilisateurs.

Ce que nous allons faire, c'est dire à un utilisateur de saisir un texte, puis nous allons sauvegarder ce texte dans une variable.

Et ensuite, nous allons dire à l'utilisateur ce qu'il a saisi.

Allons-y et mettons cela en pratique.

Utiliser les entrées utilisateur en Python est assez facile.

Nous allons simplement dire `input()`, puis ouvrir et fermer les parenthèses.

Dans ces parenthèses ouvertes ou fermées, nous allons demander à l'utilisateur ce que nous voulons qu'il saisisse.

Nous allons mettre des guillemets doubles.

Et dans ces guillemets, nous allons dire quelque chose comme `Input your name`.

Cela va dire à l'utilisateur de saisir son nom.

Et ensuite, une fois que l'utilisateur tape quelque chose comme `Tim`, ou `Tomi` ou `John`, tout ce que l'utilisateur tape, nous voulons le sauvegarder dans cette variable appelée `name`.

Cette variable appelée `name` va être l'entrée.

Essayons cela, nous l'exécutons.

Vous voyez maintenant, la première chose qu'il dit est `Input your name`. Laissez-moi dire `Tomi`. Quand je clique sur Entrée, rien ne s'est passé. Voilà comment utiliser l'entrée utilisateur. Fermons tout ça, nous pouvons revenir ici et simplement afficher à l'utilisateur `name`.

Exécutons-le. Quelle est l'entrée du nom ? Disons `Tim`, vous voyez qu'il affiche simplement `Tim`.

Nous pouvons rendre cela plus interactif en demandant le nom de l'utilisateur.

Et peut-être en demandant l'âge de l'utilisateur et en lui disant `Your name is this and your age is this`.

Nous avons besoin d'avoir deux variables. La deuxième est `age`.

`name = input('Input your name')` et ensuite `age = input('Input your age')`.

Ce que nous voulons afficher est `Your name is` et nous voulons juste ajouter le nom, puis nous fermerons cela.

Et nous dirons `and you are age years old`.

Quand nous exécutons ceci, il dit `Input your name`. Laissez-moi dire `John`, et il a `105` ans.

Il dit `Your name is John and you are 105 years old`.

C'est fondamentalement comment collecter des données simples de l'utilisateur.

Et ensuite les utiliser comme vous le souhaitez, dire à l'utilisateur `your name is this your age is this`.

C'est le concept de base.

Vous pouvez aussi le lier à la façon dont ils font les sites web, comme lorsque vous créez une inscription sur un site web.

Et ensuite, ils sauvegardent votre nom, votre email et tout le reste dans la base de données.

Et plus tard, ils vous disent `Welcome John` ou bienvenue quel que soit votre nom.

Juste pour lier ce concept, c'est fondamentalement juste obtenir les entrées de l'utilisateur, et ensuite les stocker comme une variable, dans ce cas comme une donnée, et ensuite nous pouvons les réafficher à l'utilisateur.

C'est tout ce que vous devez savoir sur la récupération des entrées de l'utilisateur, nous pouvons aussi rendre cela plus amusant.

Maintenant, quand nous récupérons l'entrée de l'utilisateur, vous pouvez voir que l'âge est vu comme une chaîne de caractères, n'est-ce pas ? Ici, l'âge est une chaîne de caractères, mais nous voulons que l'âge soit un entier.

Nous pouvons convertir cette chaîne de caractères en un entier.

Pour faire cela, nous allons dire `int()`, nous ouvrons la parenthèse, puis nous fermons la parenthèse.

Tout est à l'intérieur de cette fonction entière.

Si je reviens ici, vous voyez maintenant que cela a été changé en entier, plus des chaînes de caractères normales.

Mais maintenant, si nous essayons d'exécuter ces entrées, mon nom, je saisis un âge au hasard, vous pouvez maintenant voir qu'il nous donne cette erreur, ne peut concaténer que des chaînes de caractères, pas des entiers.

Pour que nous puissions ajouter l'âge, vous savez ce que nous devons faire, nous devons soit le convertir en une chaîne de caractères, ce que nous savons faire.

Ou nous pouvons simplement utiliser une virgule.

Enlevons simplement ceci.

Et ensuite exécutons-le.

Saisissons un âge au hasard ici même. Nom au hasard, et âge.

Maintenant, vous voyez que cela fonctionne. Il dit `Your name is John and you are 13`. Voilà comment obtenir l'entrée de l'utilisateur, l'utiliser comme vous le souhaitez, puis renvoyer cette information à l'utilisateur.

Dans cette partie, nous allons faire un exercice Python simple.

Ce que nous allons faire est un programme simple de remplacement de mots.

Ce qui va se passer, c'est qu'un utilisateur va saisir une phrase.

Et ensuite, disons que vous voulez changer un mot dans cette phrase ou changer quelque chose dans cette phrase, alors nous allons permettre à l'utilisateur de pouvoir faire cela.

Si un utilisateur saisit une phrase comme `I am a boy`, et qu'il veut plus tard changer `boy` en, disons, `guy` ou autre chose.

C'est ce que nous voulons simplement faire.

Je vais demander à l'utilisateur trois entrées, la première entrée sera la phrase, la deuxième entrée sera `what do you want to change`, et ensuite la troisième entrée est `what do you want to replace it with`.

Mettons cela en pratique.

La première chose que nous allons faire est juste d'avoir ces variables.

Ayons une variable nommée `sentence`.

Et je veux que cette variable soit une entrée.

Et ensuite je dirai `Enter your sentence`.

Maintenant, laissez-moi simplement afficher la phrase à l'utilisateur.

Exécutons-le. Disons que la phrase est `I am a boy`.

Et il affiche simplement cette phrase.

Nous allons revenir ici, disons simplement `your sentence is I am a boy`, ce qui sera tout ce que l'utilisateur écrit.

Ensuite, ce que nous voulons maintenant faire, c'est d'avoir une autre variable, disons `word1` qui sera une entrée.

Cette variable est le mot que l'utilisateur veut supprimer ou remplacer.

Et ensuite nous pouvons dire `Enter word to replace`.

Disons le mot à remplacer.

Et ensuite, une fois que nous avons cela, il va être stocké dans cette variable nommée `word1`.

Nous allons aussi avoir un autre mot, appelons-le `word2`.

Ce sera `what do you want to replace it with`.

Saisissons le mot par lequel le remplacer.

Une fois que nous avons tout cela, nous allons simplement afficher `sentence.replace()`.

Cela signifie que nous voulons remplacer ceci par cela, ouvrir la parenthèse pour prendre deux entrées, qui sont `word1`, le mot qu'on veut remplacer, et ensuite `word2`, par quoi nous voulons le remplacer.

Ce que cela fait, c'est que, disons que nous avons une phrase nommée `I am a boy`, alors ce `word1` est le `boy` qu'on veut changer, et ensuite `word2` est ce par quoi on veut le remplacer.

Allons-y et testons-le.

Ici même, il s'exécute. D'accord, il nous donne une erreur de syntaxe. C'est parce que nous avons oublié d'ajouter un plus ici même.

Recommençons.

Ici même, vous pouvez voir qu'il dit `Enter your sentence`. Laissez-moi dire `I am a boy`, maintenant il nous affiche `your sentence is I am a boy`.

Et il dit `Enter the word to replace`, donc je veux remplacer ce `boy` et saisir le mot par lequel le remplacer, `dude`.

Maintenant, vous voyez qu'il affiche `I am a dude`. Voilà comment faire un exercice simple de remplacement de mots.

Il prend une entrée, qui est une phrase, puis il prend une autre entrée, qui est le mot qu'on veut remplacer.

Et ensuite la troisième est ce par quoi on veut le remplacer.

Et ensuite, il est simplement affiché à l'écran.

J'espère que vous avez compris ce que nous avons fait dans cette partie.

Si ce n'est pas le cas, vous pouvez simplement revenir en arrière et regarder à nouveau cette partie, et assurez-vous de bien comprendre avant de passer à la suivante.

Dans cette partie, nous allons parler du travail avec les listes en Python.

Lorsque vous travaillez en Python, vous allez traiter beaucoup de données, ou vous voulez pouvoir savoir comment intégrer vos données dans une liste.

La liste en Python est fondamentalement juste une liste de différents attributs de différentes valeurs fixées dans une valeur.

Plongeons directement dans la pratique.

Pour définir une liste, c'est similaire à la définition d'une variable.

Nous pouvons simplement lui donner un nom de liste, disons une liste de pays, et je peux nommer la liste `countries`.

Et je vais juste utiliser le signe égal et les crochets.

Lorsque nous définissons des listes, nous devons utiliser des crochets. Je peux vous donner quelques entrées comme `United Kingdom`.

Je peux aussi lui donner une autre liste comme, disons, `Ghana`, laissez-moi dire `Nigeria`, laissez-moi lui donner une valeur de plus.

Et je peux dire `Australia`.

Cette liste est une variable de liste, elle a quatre valeurs.

Maintenant, une fois que j'affiche la liste comme ceci, je dirai simplement `print(countries)`, qui est la liste, vous voyez qu'il m'affiche simplement toute la liste telle qu'elle est ici même.

C'est fondamentalement la chose principale que vous devez savoir pour définir la liste.

Mais la liste est plus vaste que cela, il y a beaucoup de choses que nous pouvons faire avec les listes, comme, je veux juste obtenir les premiers attributs.

Chaque liste a un numéro d'index, comme ceci : `0 1 2 3`. Et ainsi de suite, juste comme je l'ai dit plus tôt dans ce tutoriel, en Python ou en programmation en général, les nombres comptent à partir de zéro.

Le numéro d'index de cette valeur est `0 1 2 3`. C'est juste similaire à quand nous avons une variable, disons que nous avons une variable nommée `name`.

Et nous avons `Tomi`. Cela a un index de `0 1 2 3`. C'est très similaire à une liste, chaque valeur a un index de `0 1 2 3`.

Nous pouvons simplement supprimer cela.

Maintenant, disons que nous voulons seulement afficher ceci, nous ne voulons pas afficher toute la liste.

Je peux le faire comme ceci : `countries` avec des crochets et je fixe le numéro d'index entre ces crochets.

Quand j'exécute ceci, vous voyez maintenant qu'il m'affiche seulement `United Kingdom`.

Je peux aussi faire la même chose. Disons que je veux afficher `Nigeria`.

Je lui donne `2`, je l'exécute, maintenant vous voyez que vous avez `Nigeria`. Il y a beaucoup de choses que nous pouvons faire.

Disons qu'une fois que nous avons cela, nous voulons juste afficher seulement `N` de celui-ci, nous pouvons aussi faire cela.

Donc, à l'index numéro `2` de `countries`, nous pouvons spécifier le numéro d'index `0`.

Une fois que je l'exécute, vous voyez qu'il m'affiche `N`. Maintenant, qu'est-ce que cela signifie ? Il dit `countries`, récupère la valeur avec le numéro d'index `2` (`0 1 2`). Il a donc `Nigeria`.

Et ensuite je dis à partir de ce `Nigeria`, récupère-moi celui avec le numéro d'index `0`.

Et nous voyons que dans `Nigeria`, `N` a le numéro d'index `0`.

C'est fondamentalement comment ajouter quelques choses simples dans les listes Python.

Maintenant, disons que nous voulons juste obtenir seulement toutes les listes de `Ghana` jusqu'à la fin, nous ne voulons pas ajouter `United Kingdom`, ou nous voulons juste obtenir la liste de `Nigeria` jusqu'à la fin, nous pouvons aussi faire cela.

Nous disons donc `countries`, nous voulons obtenir de `Ghana` jusqu'à la fin, nous pouvons simplement dire, nos crochets, `1` et deux points.

Cela va récupérer tout à partir du numéro d'index `1` jusqu'à la fin.

Laissez-moi vous montrer, nous fermons ceci.

Quand je l'exécute.

Vous voyez maintenant qu'il me donne la liste sans `United Kingdom`. C'est comment l'obtenir à partir d'un numéro d'index particulier jusqu'à la fin, nous pouvons aussi faire la même chose, nous pouvons dire à partir de `2`, l'utiliser à nouveau, de `Nigeria` à `Australia`, ici même, `Nigeria` et `Australia`.

Je peux aussi spécifier une plage.

Disons que je veux seulement obtenir la liste de `1` à `2`. D'accord, laissez-moi ajouter une valeur de plus ici, laissez-moi dire `New Zealand`.

Oui, donc ici même, je dis `New Zealand`.

Et c'est `0 1 2 3 4`. Disons que je veux seulement obtenir de `1` à `3`, je ne veux pas la dernière.

Et je ne veux pas celle-ci, je peux facilement le faire, disons de `1`, qui est à partir de `Ghana`, numéro d'index `1`. Après les deux points, je dirai `3`. Donc `1 2 3`.

Quand j'exécute cela, d'accord, il me donne `Ghana` et `Nigeria`.

C'est donc `0 1 2 3`. D'accord, disons jusqu'à `4`.

Quand j'exécute cela, il me donne `Ghana`, `Nigeria` et `Australia`.

Il me donne donc d'ici jusqu'à `3`. C'est fondamentalement comment faire cela en Python.

Et ensuite, nous pouvons aussi obtenir le type de la liste.

Si j'affiche quelque chose comme `type(countries)`.

Maintenant, il va m'afficher que c'est une liste en bas.

Laissez-moi simplement taper `CLS` pour tout effacer.

Maintenant, laissez-moi l'afficher, vous voyez qu'il dit `class list`.

Cela me montre que ce type de variable est une liste.

Si c'est juste une variable normale comme une variable chaîne de caractères, cela va aussi me montrer que c'est une chaîne de caractères.

Essayons cela. Détournons-nous des listes pendant une seconde. Disons que nous avons `name`.

`Tomi`, et j'ai dit le type de `name`.

Quand je l'exécute, vous voyez en bas ici qu'il dit que c'est une chaîne de caractères (`str`).

Si je change cela en `12`, vous verrez en bas ici qu'il dit entier (`int`). Voilà comment obtenir le type d'une valeur particulière.

Ceux-là, nous savons maintenant que c'est une variable de liste.

Je peux simplement supprimer cela.

Et ensuite, disons que je veux changer la valeur d'une valeur dans cette liste.

Disons que je veux changer ceci de `United Kingdom` en `United States`.

Ce que je vais faire, c'est simplement dire `countries[0]` parce que le numéro d'index de `United Kingdom` est `0`, devrait maintenant être égal à `United States`.

Et ensuite laissez-moi juste ajouter un `print(countries)`. Maintenant quand j'affiche `countries`... D'accord, vous voyez que `name` n'est pas défini, c'est parce que nous avons enlevé cette variable qui était là.

Enlevons simplement cette ligne.

Je l'exécute à nouveau.

Vous voyez maintenant que la première valeur est maintenant `United States`. Alors que c'est `United Kingdom` ici même, mais c'est simplement parce que nous l'avons changé.

`United States` ici, nous pouvons le refaire, disons que nous voulons changer `Australia`, qui est la troisième, nous dirons `3`, et disons que nous voulons changer `Australia` en un pays comme le `Canada`.

Quand je l'exécute, vous voyez, nous avons `United States`, `Ghana`, `Nigeria`, nous n'avons plus `Australia`, c'est maintenant `Canada`, puis nous avons `New Zealand`. Voilà comment changer une valeur particulière dans notre liste.

Maintenant, disons que nous voulons obtenir seulement la fin de cette liste.

Vous savez, nous pouvons aussi l'obtenir en... laissez-moi simplement supprimer tout cela rapidement, nous pouvons obtenir `New Zealand` en tapant simplement `countries`, qui est le numéro d'index, qui est `0 1 2 3 4`. `New Zealand`, le numéro d'index est `4`. Si je tape `4` et que je l'exécute, il me donne `New Zealand`.

Mais je peux aussi le faire d'une autre manière.

Maintenant, si j'ajoute un signe négatif ici, laissez-moi supprimer ceci.

Et je dis `-1`.

Cela va récupérer la liste à partir de la dernière valeur de cette liste.

Si j'exécute ceci, vous voyez qu'il me donne `New Zealand`. Si je dis `-2`, `-2` est évidemment `Australia`.

Si j'exécute cela maintenant, vous voyez que nous avons `Australia`.

Notez que lorsque vous utilisez un signe négatif, il vous donne cette liste à partir de la fin, à partir du bas, essentiellement.

Mais vous remarquez que depuis le début, nous utilisons `0` pour la première, et ensuite pour la dernière, nous utilisons `-1`.

Oui, c'est parce que, comme nous le savons, en mathématiques normales, zéro n'est ni négatif ni positif.

Donc, quand nous commençons par l'arrière, nous utilisons `-1`, pas `-0`.

Nous commençons par l'avant, c'est `0`, nous commençons par l'arrière, c'est `-1`. Voilà comment utiliser cela.

Il y a aussi beaucoup d'autres choses que nous pouvons faire avec les listes, comme nous pouvons obtenir la longueur de cette liste, disons que nous voulons savoir combien de valeurs nous avons dans cette liste, parce que la plupart du temps vous avez de grandes quantités de données, vous ne pouvez pas commencer à les compter une par une comme ceci.

Mais vous pouvez simplement dire `len(countries)`, qui est le nom de la liste.

Une fois que je l'exécute, vous voyez qu'il me donne `5`, parce que j'ai cinq valeurs ici.

Mais notez que lorsqu'il me donne la réponse, il ne l'utilise pas en fonction de la valeur d'index.

La valeur d'index est juste comme l'ID assigné à chacune de ces valeurs ici même.

Mais quand je calcule la longueur, il me donne le montant réel que nous avons ici, qui est de cinq variables, alors que l'index irait jusqu'à quatre. J'espère que vous comprenez cela.

Nous pouvons aussi faire d'autres choses comme dans la liste.

Comme vous pouvez le voir, toutes celles-ci sont des chaînes de caractères.

Maintenant, au lieu d'afficher seulement des chaînes de caractères, laissez-moi simplement supprimer ce `New Zealand`.

Au lieu d'afficher seulement des chaînes de caractères, je peux changer, disons ce `Ghana`, je peux le changer en un nombre comme `2`.

Nous avons donc la chaîne de caractères, nous avons un entier, si j'affiche ceci... d'accord, cela me donne `4`.

Enlevons `len`.

Une fois que j'affiche ceci, vous voyez, il me donne ce que je veux voir, si j'affiche le numéro d'index de celui-ci, qui est `1`.

Et j'appuie sur exécuter, il me donne `2`.

Nous pouvons donc mélanger différents types de données dans une liste.

Je peux aussi changer ce `Nigeria` en `True`, qui est une valeur booléenne.

Une fois que je l'exécute, enlevons ceci.

Je l'exécute, il me donne cela. Il n'y aura donc pas d'erreur, rien ne va entrer en conflit, nous pouvons simplement faire cela.

Et vous vous rappelez que nous avons vérifié le type d'une liste.

Ici même, une fois que j'exécute ceci, vous verrez qu'il me donne `class list`, ce qui signifie que cette variable est une liste.

Mais disons que je veux vérifier le type des valeurs dans une liste, comme je veux vérifier le type de cette valeur ou le type de cette valeur.

Comme vous le savez, cette valeur est une chaîne de caractères, celle-ci est un entier, celle-ci est une valeur booléenne.

Celles-ci sont aussi des chaînes de caractères.

Laissez-moi survoler.

Vous voyez qu'il me donne `int` qui est un entier, et une fois que je survole celle-ci... d'accord, il ne me donne rien là, mais c'est une valeur booléenne.

C'est une chaîne de caractères.

Disons que je veux obtenir cela, je vais simplement dire `type(countries[0])`.

Maintenant, quand j'exécute ceci, vous voyez qu'il dit `class str`.

Disons que je veux donner pour la deuxième, qui a une valeur d'index de `1`.

Une fois que je l'exécute, il me donne entier (`int`).

Essayons pour la troisième.

Il me donne un booléen (`bool`), voilà comment obtenir le type d'une chaîne de caractères.

Et nous pouvons aussi faire d'autres choses comme... la dernière chose que je veux vous montrer pour cette partie est une autre façon de définir une liste.

Au lieu d'utiliser les crochets, nous pouvons aussi utiliser quelque chose que nous appelons `list()`.

Mais maintenant, lorsque nous utilisons ce constructeur de liste, il est utilisé pour construire une liste, nous n'allons pas utiliser de crochets à nouveau, nous allons utiliser des parenthèses normales comme ceci.

Laissez-moi simplement supprimer cette ligne.

Utilisons maintenant le constructeur de liste pour spécifier comment construire une nouvelle liste.

Je vais donc dire `list()`.

Et je vais utiliser des parenthèses normales, et cela doit être double.

Lorsque j'utilise le constructeur de liste, cela doit être double comme ceci.

Maintenant, vous pouvez avoir toutes mes valeurs comme `Nigeria`, je peux avoir `44`, je peux avoir `False`. Une fois que j'affiche tout cela, nous ne voulons pas afficher le type, nous voulons juste tout afficher.

`countries`, cela me donne tout ce que je veux voir.

Voilà comment utiliser le constructeur de liste pour spécifier une liste.

Nous pouvons donc afficher une liste de deux manières, la normale et le second constructeur de liste.

Et ensuite, nous pouvons aussi les afficher de la manière normale sans `list` comme les crochets, comme `countries2`.

Maintenant, si je dis `type(countries)`, vous voyez qu'il va me donner `list`.

Et ensuite laissez-moi aussi afficher le type de `countries2` juste pour montrer que les deux sont toujours des listes. Donc `list` et `list`. Ce sera tout sur les bases des listes.

Dans la prochaine vidéo, nous allons parler davantage des listes, des attributs, il y a encore beaucoup de choses que nous pouvons faire avec les listes. Dans cette partie, nous allons parler davantage des listes, plus précisément, nous allons parler des fonctions de liste ou des méthodes de liste en Python.

Dans la dernière partie, je vous ai parlé des listes et de plein de choses que vous pouvez faire avec les attributs de liste.

Dans cette vidéo, nous allons aller plus loin.

Disons que nous avons deux listes.

La première est `list1`.

Et cette `list1` est juste un groupe de nombres `1 2 3 4 5`.

Et ensuite nous avons `list2`.

Et ensuite nous voulons que cette `list2` soit juste, disons, un groupe de fruits, donc nous avons une banane, et ensuite nous avons des pommes, des mangues et des oranges.

Nous avons donc ces deux listes.

Maintenant, disons que nous voulons joindre ces deux listes ensemble, comme si nous voulions les afficher ensemble.

Nous allons faire quelque chose comme `list1.extend(list2)`.

Maintenant, qu'est-ce que cela va me donner ? C'est ceci joint à cela.

Affichons-le.

Ici, vous voulez `1 2 3 4 5` puis `banana`, `apple`, `mango`, `oranges`.

Cela m'a juste donné ceci joint à cela, la première liste jointe à la seconde liste.

C'est ce que fait `extend`, il combine les deux listes ensemble.

Mais disons que nous voulons ajouter une valeur à la fin de cette liste comme `oranges`.

Nous voulons ajouter quoi ? Je pense que nous avons des cerises, mais nous voulons juste ajouter autre chose à cela.

Nous pouvons faire quelque chose comme `list2.append('cherry')`.

Maintenant nous dirons `print(list2)`, vous allez m'afficher tout cela avec `cherry`.

Maintenant `cherry` fait partie de cette liste, vous voyez non seulement des bananes, des pommes, des mangues, des oranges, et il m'affiche `cherry`.

Si je dis que je veux obtenir la longueur de `list2`.

Nous en avons quatre ici, mais puisque nous en avons ajouté une, cela devrait nous en donner cinq.

Maintenant vous voyez que nous en avons cinq.

C'est donc une façon simple d'ajouter une valeur à une liste.

Et c'est aussi très, très utile.

Mais disons que nous voulons mettre une valeur entre l'une de celles-ci, comme nous avons plusieurs fois une valeur entre banane et pomme.

Cette cerise, nous voulons qu'elle soit ici même, quelque chose comme ça.

Si nous voulons faire cela, nous allons simplement dire `list2.insert()`.

Et ensuite cela va prendre deux entrées, maintenant cela va prendre le numéro d'index, la place d'index où nous voulons la mettre, nous voulons la mettre à `1`, et ensuite nous voulons mettre `cherry`.

Laissez-moi expliquer cela davantage.

Il dit `list2.insert()`, nous voulons dire dans le numéro d'index `1`, c'est-à-dire ici même, alors `cherry` devrait être ici même.

Donc `0 1` nous voulons insérer `cherry`.

Maintenant quand j'affiche `cherry`, laissez-moi juste exécuter ceci, vous voyez maintenant que nous avons une banane puis nous avons une cerise entre les deux.

Donc entre les bananes et les pommes, nous avons une cerise.

Voilà comment insérer une valeur entre une liste.

Mais maintenant, disons que nous voulons supprimer une valeur particulière de la liste, nous pouvons dire `list2.remove()`, et supprimons les bananes.

Maintenant, quand j'affiche `list2`, cela va m'afficher une liste sans bananes.

Et c'est très facile, c'est juste en disant `remove`, puis tout ce que vous voulez supprimer.

Mais maintenant, disons que nous voulons faire quelque chose, je veux tout supprimer dans cette liste, je veux la vider, vous pouvez simplement dire `list2.clear()`.

Et rien ne sera ici.

Comme j'ai dit `list2.clear()`, cela va être vide, cela va juste être une liste vide.

Cela vide tout, supprime toutes les valeurs qui s'y trouvent. Une fois que je l'exécute, vous voyez qu'il m'affiche une liste vide.

Voilà comment supprimer une liste. Très facile.

Mais maintenant, disons que nous avons ces valeurs.

Et la mangue, nous voulons obtenir le numéro d'index de la mangue, comme nous le savons, c'est `0 1 2`. Donc le numéro d'index de la mangue est `2`.

Mais nous voulons l'obtenir, disons que nous avons des milliers de listes de valeurs dans cette liste.

Nous voulons savoir où se trouve la mangue dans cette liste, nous allons simplement dire `print(list2.index('mango'))`.

Cela va donc simplement afficher le numéro d'index de la mangue.

Exécutons-le ici même, vous voyez que c'est `2` (`0 1 2`). Cela me dit donc où se trouve la mangue dans cette liste, ce qui est très, très utile.

Maintenant, disons que nous avons une valeur qui apparaît plus d'une fois.

Nous voulons juste savoir combien de fois une valeur apparaît dans cette liste.

C'est très facile, nous allons simplement dire `list.count('mango')`.

Donc cela devrait nous dire `1` parce que la mangue ne vient dans cette liste qu'une seule fois.

Une fois que je l'exécute, vous voyez ici que nous avons `1`.

Laissez-moi venir ici et saisir à nouveau `mango`.

Maintenant, quand je l'exécute cette fois, vous voyez que nous en avons `2` parce que la mangue est dans notre liste deux fois.

Voilà comment faire cela simplement.

Mais maintenant, disons que nous avons une liste de nombres et disons qu'ils sont éparpillés, comme disons que nous avons `1` ici et laissez-moi juste supprimer tout cela, nous avons `4 5`, donc nous avons `3` ici.

Donc `4 3 5 1` et disons que j'ai `2` à la fin.

Disons que nous voulons afficher cette liste dans l'ordre croissant.

Vous savez, comme je l'ai dit, en Python, vous pourriez travailler avec beaucoup de données, et nous avons des milliers de nombres qui sont éparpillés, je veux les afficher correctement.

Disons de `100` à `250` à `350`, correctement, pas éparpillés, nous pouvons facilement le faire, nous allons dire `list1.sort()`.

Ici même, je vais juste afficher `list1`.

Maintenant, quand je l'affiche, il ne va pas afficher `4 3 5 1 2`, il va afficher `1 2 3 4 5` dans l'ordre croissant.

Maintenant vous voyez que nous avons `1 2 3 4 5`. C'est aussi très utile lorsque vous travaillez en Python.

Mais maintenant, laissez-moi juste enlever cette mangue, nous ne voulons pas l'avoir deux fois.

C'était juste pour tester.

Mais maintenant, disons que nous voulons afficher une liste à partir de la fin, nous voulons inverser la liste.

Nous voulons l'afficher à partir du bas, ce que nous allons faire, nous dirons `list2.reverse()`.

C'est très facile, nous faisons juste `list2.reverse()`. Une fois que nous affichons `list2`, vous verrez qu'il est affiché à partir des oranges, puis des mangues, des pommes et des bananes.

Exécutons-le. Maintenant je vois `oranges`, `mango`, `apple`, `banana`. Voilà comment afficher facilement une liste à partir du bas, à partir de la dernière valeur de cette liste.

Maintenant, disons que nous voulons dupliquer une liste, comme si nous voulions juste prendre cette liste et la copier à nouveau ou quelque chose comme ça.

Testons cela pour `list2`, laissez-moi supprimer ces deux-là, ayons une autre liste nommée `list3`. Disons que nous voulons que `list3` soit exactement la même chose que ce duplicata de `list2`.

Nous allons donc simplement dire que `list3` peut être égal à `list2.copy()`.

Cela va donc copier toutes les valeurs de `list2`, puis les coller dans `list3`. Quand nous affichons `list3`, je l'exécute, nous avons exactement la même chose que ce que nous obtenons quand nous affichons `list2`. C'est exactement la même chose.

Et ensuite nous pouvons aussi faire quelque chose de plus amusant.

Comme, disons que nous voulons juste supprimer la dernière valeur de ceux-ci et afficher tout le reste.

Nous pouvons faire cela en utilisant la méthode `pop`, donc nous pouvons simplement dire `list2.pop()`.

Donc, quand nous disons `list2.pop()`, cela va simplement supprimer la dernière valeur que nous avons dans cette liste, cela va supprimer la dernière valeur que nous avons dans cette liste, et ensuite laisser le reste.

Donc, quand j'affiche `list2` maintenant, il n'y a plus que trois valeurs.

Maintenant vous voyez que nous avons des bananes, des pommes et des mangues, plus d'orange.

Mais disons que nous voulons être spécifiques sur ce que nous voulons supprimer, vous vous rappelez que nous pouvons supprimer une valeur en disant `list2.remove()` et nous pouvons spécifier, disons, `banana`.

Et ensuite, quand nous affichons cela, il va supprimer `banana`.

Mais nous pouvons aussi simplement supprimer une valeur en utilisant le numéro d'index.

Donc, dans `pop`, nous allons dire `list.pop()` juste comme faire sauter quelque chose.

Supprimons celle avec le numéro d'index `1`. Nous disons `1` et cela nous donne `banana`, `mango`, `oranges`.

Cela nous donne cette même liste mais sans la valeur de ce numéro d'index.

Mais nous pouvons aussi utiliser cela. Au lieu d'utiliser `pop`, nous pouvons faire exactement la même chose.

Mais maintenant, nous pouvons utiliser `del` (delete).

Nous allons donc dire `del list2[0]`.

Maintenant, cela va supprimer la valeur avec le numéro d'index `0` dans cette liste `list2`.

Quand nous affichons `list2`, ils vont nous donner tout sans banane.

Exécutons-le maintenant, vous voyez que nous avons des pommes, des mangues et des oranges.

Rappelez-vous que nous vous avons aussi montré comment vider les listes, je vais juste tout supprimer dans notre liste.

Nous pouvons aussi faire cela en utilisant cette fonction `del`.

Donc, au lieu de spécifier quelque chose ici, nous disons simplement `del list2`.

Maintenant, cette chose va vider cette liste.

Une fois que je l'exécute, vous voyez qu'il dit que `list2` n'est pas défini.

D'accord ? Mais nous avons bien `list2` ici même.

Faisons donc quelque chose comme `del list1`.

Et ensuite affichons simplement.

D'accord, donc la raison pour laquelle il dit `list2` non défini, vous pouvez voir que nous avons `list1`, ici nous avons `list2`, qui a banane, pomme, mangue et oranges.

Nous avons juste supprimé `list2`.

Une fois que nous supprimons cette `list2`, c'est assez différent de ce que nous avons fait plus tôt, qui était `list.clear()`.

Rappelez-vous que si nous faisons `list2.clear()`, cela va simplement tout enlever ici.

Mais cette liste va être disponible dans notre code.

Mais quand nous utilisons ce `del`, cela va simplement supprimer cette valeur.

Donc elle ne sera plus dans notre code, c'est pourquoi quand j'ai essayé d'afficher `list2`, Python ne la voit plus, il dit que `list2` n'est pas défini, donc il la supprime complètement.

Ce sera tout pour les listes pour le moment.

Dans ce tutoriel, nous allons parler des tuples en Python.

Les tuples sont utilisés pour stocker plusieurs éléments dans une seule variable.

Vous connaissez les listes dont nous avons parlé dans la dernière partie, les tuples sont très similaires aux listes.

Mais il y a une différence fondamentale, les tuples sont immuables.

Immuable signifie que vous ne pouvez changer aucune valeur dans un tuple.

Laissez-moi vous montrer comment écrire un tuple en Python.

Disons que nous avons un tuple de trois nombres.

Je dirai `three_numbers`.

Et je donne ces nombres, j'écris dans le tuple, ce qui signifie une parenthèse normale, pas de crochets, donc `(1, 2, 3)`.

Disons que nous avons ceci maintenant, quand nous affichons `three_numbers`, nous exécutons cela, cela nous donne simplement ce tuple, nous pouvons aussi faire certaines choses comme obtenir la première valeur dans ce tuple en utilisant le numéro d'index, je peux dire `0`, ce qui affichera `1`.

Nous pouvons donc aussi faire toutes ces sortes de choses.

Mais disons que nous essayons maintenant de changer la valeur de `2` en quelque chose comme `25`.

Ce n'est pas possible parce que, comme je l'ai dit plus tôt, c'est immuable, ce qui signifie que nous ne pouvons pas le changer.

Une fois que nous avons le tuple, c'est ce qu'il va être pour notre code, nous ne pouvons pas le redéfinir ou ajouter quoi que ce soit au tuple plus tard dans le code.

Disons que nous voulons faire quelque chose comme `three_numbers[1] = 23`.

Et ensuite je veux afficher `three_numbers`.

Cela va nous donner une erreur.

Oui, il dit `TypeError: 'tuple' object does not support item assignment`.

Il dit donc que ce que nous voulons faire, le tuple ne le supporte pas.

C'est la différence fondamentale entre un tuple et une liste.

Et ensuite, nous pouvons aussi faire d'autres choses comme les tuples permettent la répétition de nombres ou la répétition de valeurs, comme j'ai `(1, 2, 3)`, je peux saisir à nouveau `1`.

Quand je l'affiche, laissez-moi supprimer cette ligne, j'ai `1` deux fois, une fois que je l'affiche, cela va fonctionner correctement, cela permet la répétition de la même valeur.

Et je peux aussi faire des choses comme je peux obtenir la longueur d'un tuple, je peux simplement dire `print(len())`, et ensuite cela va simplement me donner le nombre de valeurs que nous avons dans ce tuple.

Comme vous pouvez le voir, il affiche `4` parce que nous avons `1 2 3 4` valeurs.

Et ensuite, je peux aussi obtenir le type juste pour m'assurer que c'est un tuple, je peux faire `type()` pour savoir si c'est un tuple ou non.

Une fois que je l'exécute, vous voyez `class tuple`.

Cela me montre que c'est un tuple et le tuple permet aussi divers types de données.

Comme je peux avoir un autre tuple et dire `strings`.

Et ensuite je peux dire `orange`.

Laissez-moi en donner un de plus.

Maintenant, quand j'essaie d'afficher `strings`, vous voyez que tout fonctionne bien.

Il permet donc divers types de types de données, nous pouvons aussi le refaire pour, disons, le type booléen, disons `BO` et disons `True`, `False`, et ensuite `True` à nouveau.

Maintenant, quand nous essayons d'afficher `BO`, vous voyez que cela fonctionne bien.

Il permet donc divers types de données, et il ne les permet pas seulement sur des variables séparées, nous pouvons les mélanger ensemble, comme nous avons `1`, je peux en avoir un autre, qui sera une chaîne de caractères, qui sera `own`.

Et ensuite je peux en avoir un autre, qui va être un booléen.

Une fois que j'affiche le premier, qui est `three_numbers`.

Maintenant vous verrez que tout fonctionne toujours bien.

Les tuples permettent donc toutes ces sortes de choses.

Et ensuite, dans les tuples, nous pouvons aussi vérifier le type de données de la valeur de ce tuple.

Maintenant nous voulons vérifier le type de données de cette première valeur, nous pouvons dire `type(three_numbers[0])`, qui est la première, cela devrait nous afficher `int`, qui est un entier.

Comme vous voyez, il dit `class int`.

Le tuple peut aussi faire cela.

Maintenant, au lieu d'écrire simplement ces parenthèses ici même ou ces parenthèses normales ou circulaires, peu importe comment vous voulez les appeler, c'est tout à fait correct.

Nous pouvons aussi utiliser le constructeur de tuple, tout comme je vous ai parlé du constructeur de liste, il y a aussi un constructeur de tuple.

La seule différence est que nous allons ajouter `tuple()` ici même.

Et il aura deux parenthèses comme ceci, j'essaie de tout afficher, cela va toujours être correct, laissez-moi simplement afficher la variable de tuple normalement.

Maintenant, comme je l'ai affiché, vous voyez qu'il y a toujours un tuple, rien ne va mal.

Et ce sera fondamentalement tout sur les tuples, les bases des tuples en Python. Nous pourrions utiliser ces tuples moins souvent en Python, nous utiliserons principalement des listes.

Mais dans certains cas, nous voulons vraiment utiliser des tuples en Python, quelque chose comme, disons que vous travaillez avec des coordonnées, ou juste quelques nombres que vous ne voulez pas changer, ou quelques valeurs que vous ne voulez pas changer, les tuples pourraient être la meilleure option.

Dans ce tutoriel, je vais vous parler des fonctions en Python.

Les fonctions sont juste un groupe de code qui effectue une tâche particulière.

Les fonctions vous permettent de bien empaqueter votre code, permettez-moi de dire de bien restructurer, c'est juste comme un bloc de code qui effectue une tâche particulière de la manière dont vous voulez utiliser la fonction, vous l'appelez simplement.

Laissez-moi vous montrer comment faire une fonction en Python.

Pour définir une fonction, nous allons utiliser un mot-clé appelé `def`.

Une fois que nous tapons ce `def`, Python sait que nous voulons maintenant définir une fonction.

Nous pouvons dire `def`, faisons juste une fonction simple, qui va saluer l'utilisateur.

Peut-être qu'elle dira bienvenue ou quelque chose comme ça.

Nous pouvons donc dire `greetings`.

Le mot-clé est `def`, et ensuite il est suivi par `greetings_function`.

C'est le nom de notre fonction, et ensuite elle va être suivie par des parenthèses ouvertes et fermées, et ensuite après cela, nous allons avoir deux points.

Après ce bloc de code, Python sait que tout ce qui va venir en dessous va être la tâche que nous voulons que cette fonction effectue.

Une fois que je clique sur Entrée, je remarque qu'il ne commence pas par le début, il commence juste à partir de cet endroit, il indente automatiquement.

En Python, l'indentation est très importante.

Cette indentation nous montre que tout code que nous allons écrire, comme afficher quelque chose, va être sous cette fonction.

Mais si je supprime simplement l'indentation, et que je commence d'ici, alors la fonction est annulée.

C'est une syntaxe invalide, car normalement il est censé y avoir une indentation et une indentation, une indentation équivaut à quatre espaces.

Si je vais ici, vous pouvez voir que c'est `1 2 3 4`. Une fois qu'il indente automatiquement. Cela signifie qu'il a créé quatre espaces.

Maintenant, disons que vous utilisez un éditeur de code qui ne fait pas l'indentation automatiquement. Comme si vous utilisiez le Bloc-notes, et qu'ensuite une fois que vous cliquez sur Entrée, il n'ajoute pas l'indentation, vous pouvez simplement demander quatre espaces comme ceci `1 2 3 4`. Cela a automatiquement indenté.

Maintenant, nous voulons que cette fonction dise simplement à l'utilisateur `Welcome user` ou `Greetings from me` ou quelque chose comme ça.

On peut dire `Welcome user`.

Comme ceci, cette fonction nommée `greetings_function` affiche à l'utilisateur `Welcome user`.

Mais si j'exécute ceci, rien n'est fait.

Je ferme tout ça.

Et pourquoi cela ? Quand nous avons une fonction pour que cette fonction soit exécutée, ou pour que cette tâche soit exécutée, nous devons appeler la fonction.

Et j'appellerai cette fonction, nous pouvons simplement dire...

Une fois que j'appuie sur Entrée, vous voyez qu'il est toujours indenté.

Mais je veux sortir de cette fonction, j'ai fini ce que je faisais dans cette fonction.

Donc, si j'appuie simplement sur une touche Retour arrière (Backspace), maintenant, c'est hors de cette fonction.

Maintenant, si je dis simplement `greetings_function()` avec des parenthèses ouvertes et fermées, maintenant j'appelle cette fonction.

C'est la même chose que tout ce que nous avons dans cette fonction.

Maintenant, il devrait afficher `Welcome user`.

Exécutons-le, vous voyez maintenant qu'il dit `Welcome user`.

Voilà comment utiliser les fonctions en Python.

Mais les fonctions sont plus vastes, il y a beaucoup de choses que nous pouvons faire avec les fonctions.

Comme vous pouvez le voir, cela dit `Welcome user`.

Mais quel utilisateur ? Rendons cela plus amusant, quelque chose comme ça, nous pouvons passer quelque chose appelé des arguments ou des paramètres.

Ici, dans ces parenthèses ouvertes ou fermées, au lieu de les laisser vides, nous pouvons passer quelque chose comme, disons, nous avons `name`.

Pas ceci.

Donc `name`, qui est le nom de l'utilisateur.

Maintenant, au lieu de dire `Welcome user`, nous voulons dire `Welcome name`.

Ici, nous allons simplement dire `name`.

Et cela va simplement afficher `Welcome name`.

Mais au lieu de `name`, il s'attend à ce que nous passions quelque chose lors de l'appel de cette fonction.

Si j'exécute simplement ceci, vous voyez, cela me donne une erreur.

Il dit `greetings_function() missing 1 required positional argument: 'name'`.

Cela nous montre que lorsque nous appelons cette fonction, maintenant, nous devons passer quel que soit l'utilisateur.

Disons que le nom de l'utilisateur est `John`.

Maintenant, quand j'exécute ceci, ici même, vous voyez qu'il dit `Welcome John`.

Laissez-moi revenir en arrière et m'assurer de bien expliquer.

Ici même, nous avons cette fonction, elle a un argument ou paramètre, qui est `name`.

Ce `name` va pouvoir dire à la fonction quel utilisateur elle veut saluer.

Et ensuite, elle va simplement saluer l'utilisateur avec la fonction `print`.

Pour que nous lui donnions ce `name`, ce `name` est juste comme une variable.

Donc, quand nous appelons la fonction, au lieu de laisser cela vide comme ceci, nous allons simplement passer la chaîne de caractères comme `John`.

Mais vous savez, nous pouvons aussi passer d'autres types de données.

Vous pouvez voir que ce `John` est une chaîne de caractères.

Mais disons que nous voulons simplement passer un entier ou un nombre.

Chaque fois que nous traitons des nombres en Python, nous n'avons pas besoin de guillemets, nous pouvons simplement dire `34`.

Une fois que j'exécute ceci, vous voyez qu'il dit `can only concatenate str (not "int") to str`.

Si vous avez suivi ce tutoriel depuis le début, je vous ai montré comment convertir un entier en une chaîne de caractères.

Ici même, il dit qu'il ne peut pas concaténer une chaîne de caractères et un entier.

Pour que nous puissions utiliser ceci, nous devons nous assurer que nous convertissons cet entier en une chaîne de caractères.

Je vais donc dire `str()` comme ceci.

Maintenant ce `name` est une chaîne de caractères.

Une fois que je l'exécute, il dit `Welcome 34`.

C'est fondamentalement comment faire cela.

Revenons en arrière.

Assurons-nous que nous passons `John`.

Voilà comment passer des paramètres ou des arguments.

Vous pouvez l'appeler paramètres.

Vous pouvez l'appeler arguments, peu importe ce que vous voulez, c'est correct.

Et ensuite, nous pouvons aussi passer plus d'un paramètre ou argument.

Nous pouvons donc passer `name`, nous pouvons aussi passer `age`.

Et ensuite nous pouvons dire `Welcome` puis le nom.

Et ensuite nous pouvons dire quelque chose comme... faisons ceci, vous avez tapé le nom, disons `age` ans.

Ici même, quand nous passons ceci, `John`, nous passons aussi l'âge comme un entier, disons `27`.

Mais rappelez-vous, maintenant c'est un entier.

Si nous exécutons ceci, évidemment, nous allons avoir une erreur, qui est `cannot concatenate str and int`.

Vous savez que nous devons maintenant convertir cela en une chaîne de caractères ici même.

Et ensuite l'exécuter.

Vous voyez, il dit `Welcome John you are 27 years old`.

C'est fondamentalement comment faire cela, vous pouvez passer deux arguments ou paramètres.

Maintenant, disons que vous ne connaissez pas le nombre d'arguments qui vont être passés ici.

Laissez-moi mettre cela en pratique avant d'expliquer.

Disons que nous avons `names`.

Enlevons tout cela.

`Welcome name`.

Disons que nous avons ceci.

Mais nous ne savons pas combien vont être passés ici.

Nous allons donc devoir mettre quelque chose comme un astérisque `*`.

Cet astérisque montre que nous passons diverses quantités comme un tuple, un tuple qui est comme une liste de valeurs que nous passons ici.

Et ensuite nous ne connaissons pas les quantités qui sont passées.

Disons qu'ici même, nous avons ce tuple, `John`.

Disons que nous en avons aussi un autre nommé `Tim`.

Donnons-en un de plus.

D'accord, ici même.

Un de plus nommé `Tom`.

Ici même, nous passons ces trois valeurs ici comme `names`.

Ces `names` sont comme un tuple maintenant, c'est pourquoi il y a un astérisque.

Parce que nous ne savons pas.

Pour que nous montrions maintenant le nom que nous voulons.

Disons que nous voulons seulement saluer le deuxième utilisateur, alors nous pouvons saluer l'utilisateur en utilisant son numéro d'index.

On peut donc dire `names`, le numéro d'index est `1`.

Maintenant, quand j'exécute ceci, vous voyez qu'il dit `Welcome Tim`.

Voilà comment passer diverses valeurs, plus d'une valeur si nous ne savons pas ce que nous passons.

Revenons en arrière.

Laissez-moi appuyer sur Ctrl+Z, pour revenir à `name` et `age`.

Rapidement, d'accord, comme ça.

Oui.

Affichons cela et assurons-nous que notre code fonctionne.

`Welcome John you are 27 years old`.

Bien.

Maintenant, nous pouvons aussi passer cela au lieu de passer simplement les valeurs, nous pouvons passer par les noms de variables.

Cela peut être comme `name = 'John'`.

Et ensuite `age = 27`. C'est toujours exactement la même chose.

Donc, quand nous l'exécutons, cela va toujours nous afficher `Welcome John you are 27 years old`, c'est fondamentalement la même chose.

Rendons cela plus amusant.

Au lieu de simplement passer ces valeurs de manière statique, ou en codant en dur les valeurs, nous pouvons d'abord demander à l'utilisateur de nous donner une entrée de son nom et de son âge, puis nous allons simplement afficher cela.

Faisons cela rapidement.

Ici même.

Non, ici même.

Ici même, nous pouvons dire `name = input('Enter your name')`.

Et ensuite nous pouvons dire `age = input('Enter your age')`.

Maintenant, nous demandons à l'utilisateur la valeur, je vais juste taper ceci.

Et ensuite une fois que l'utilisateur nous donne cela, je vais juste le remplacer ici.

En le remplaçant par `name`, et en remplaçant ceci par `age`.

Exécutons cela.

Si je descends ici, il demande mon nom. Je dis `Tim`, il demande l'âge, je dis `101`.

Maintenant il dit `Welcome Tim you are 101 years old`.

J'espère que vous comprenez le concept des fonctions en Python.

Ce sont les choses de base que vous allez traiter en Python.

Dans cette partie, nous allons parler de l'instruction `return` dans une fonction Python.

Les instructions `return` sont simplement utilisées pour obtenir une réponse de la tâche exécutée dans une fonction.

Comme vous le savez, dans la dernière vidéo, lorsque nous avons défini notre fonction, nous avons simplement affiché tout ce que nous voulions renvoyer.

Mais normalement, en Python, nous utilisons ce que nous appelons une instruction `return`.

Cette instruction `return` va nous donner un résultat ou nous donner un retour sur ce qui a été exécuté.

Personnifions cela, disons que vous êtes envoyé en mission pour aller chercher des informations.

Et ensuite, quand vous revenez, vous voulez donner une réponse ou vous voulez retourner un retour, vous voulez dire ce que vous avez obtenu, ou la tâche que vous avez exécutée.

C'est la même chose ici dans la fonction Python, le bloc de code part en mission, et dans l'instruction `return`, nous donne une réponse.

Laissez-moi vous montrer comment faire cela.

Nous allons définir une fonction normale, disons simplement `my_function`.

Et elle ne va prendre aucun argument pour le moment.

Ici, nous voulons juste retourner, disons, `5 + 4`.

Cette fonction de base va maintenant simplement retourner `9`, parce que c'est `5 + 4`.

Mais maintenant, si nous pouvons simplement afficher `my_function`.

Une fois que nous affichons `my_function`, vous voyez, il dit `function my_function`, c'est juste pour savoir que c'est une fonction, mais nous devons aussi ajouter nos parenthèses ouvertes et fermées, quand je l'exécute à nouveau, nous voyons `9`.

Nous allons rendre cela plus interactif, nous pouvons simplement avoir une fonction qui additionne deux nombres ou soustrait des nombres ou quelque chose comme ça.

Nous pouvons donc dire `add_numbers`.

Et ensuite nous voulons ajouter deux arguments, `num1` et `num2`.

Ce que nous voulons juste retourner est `num1 + num2`.

Ici même, nous pouvons simplement passer `num1` et `num2` comme `2` et `3`.

Cela va nous donner... vous voyez, il dit que `my_function` n'est pas défini, c'est parce que nous avons changé le nom en `add_numbers`, nous allons simplement l'exécuter à nouveau.

Vous voyez, maintenant il nous donne `5`.

Mais rendons cela plus interactif ici.

Disons que `num1 = input('Enter first number')`.

Et ayons `num2 = input('Enter second number')`.

Il va nous donner `num1` ici, nous allons donner `num2`.

Maintenant, quand nous exécutons ceci, il va nous demander le premier nombre, disons `80`.

Ou disons `20` comme deuxième nombre, cela va s'additionner et nous donner `100`.

Maintenant, vous voyez qu'il dit `8020`.

Et la raison pour laquelle il dit cela est parce qu'il voit cela comme une chaîne de caractères.

Et donc, quand nous utilisons l'addition, il le voit comme une concaténation.

Il a donc juste dit `8020`, mais je voulais qu'il l'additionne. Vous voyez qu'il dit `str`. Mais nous savons que nous collectons un entier. Ce que Python fait, vous savez cela. Nous devons dire à Python que ce que nous voulons collecter est un nombre.

Je veux donc que vous l'additionniez. Pour faire cela, convertissez-le en un entier en disant `int()`.

Nous le fermons ici même, puis nous faisons la même chose `int()` et ensuite nous le fermons ici même.

Maintenant, quand nous exécutons ceci, il va l'additionner pour nous, `80` plus `20`.

Maintenant il nous donne `100`.

C'est le concept de base de l'instruction `return`.

Et je veux aussi souligner quelque chose : chaque fois que nous utilisons l'instruction `return` dans une fonction Python, nous n'écrivons rien après ce bloc de code.

Cette instruction `return` montre la fin de la fonction. Si je viens ici et que je dis `print('Hello')`.

Une fois que je l'exécute, il me demande les nombres, vous voyez qu'il a juste retourné ceci, il n'affiche pas `Hello`, parce que c'est en dehors de notre fonction et ce n'est pas une indentation normale.

Ce code n'est donc pas vu dans notre bloc de code.

Mais si je viens ici, si je le supprime et qu'à l'intérieur de la fonction, je le colle, il va l'afficher pour nous.

Disons `4` et `4`. Maintenant vous voyez que nous avons `Hello`, et ensuite nous avons la réponse de l'addition.

C'est ainsi qu'on utilise les instructions `return` dans une fonction Python.

Dans cette partie du tutoriel, nous allons parler des instructions `if` en Python.

L'instruction `if` consiste essentiellement à donner une condition à Python.

Ce concept est très facile à saisir, non seulement en Python, mais en programmation en général, il y a toujours des instructions `if`, mais peut-être avec une syntaxe différente.

L'instruction `if` permet donc à Python d'exécuter du code automatiquement par lui-même.

En supposant que si une condition particulière est vraie, alors Python doit faire ceci.

Mais si ce n'est pas vrai, alors Python doit faire cela.

Nous donnons donc à Python une condition avant qu'il n'exécute le code.

Laissez-moi d'abord taper quelques petites notes pour que vous puissiez comprendre le concept.

Je peux dire quelque chose comme : si j'écris un nombre.

Et ensuite, si le nombre est divisible par deux, alors nous savons que le nombre est un nombre pair.

Et s'il n'est pas divisible par deux, alors ce nombre est impair.

Quelque chose comme ça, ce n'est pas comment écrire du code.

C'est juste du texte brut.

Mais je montre ici : l'utilisateur a écrit un nombre, puis si le nombre est divisible par deux, alors nous pouvons dire à Python de dire à l'utilisateur que ce nombre est pair.

Mais s'il n'est pas divisible par deux, alors ce nombre est impair.

Mettons cela en pratique, écrivons du vrai code Python.

Nous avons une variable nommée `a = 4`.

Et ensuite nous avons une autre variable nommée `b = 3`.

Nous allons avoir une instruction `if` simple vérifiant si `2` est plus grand que `3` ou si `3` est plus grand que `2`, ou si la variable `a` est plus grande que la variable `b`.

Disons, `if a > b:`.

Alors nous pouvons simplement afficher à l'utilisateur `a`... concaténons `is greater than b`.

D'accord, mais nous savons que `b` est plus grand que `a`.

Rendons cela plus grand.

Exécutons.

Maintenant, exécutons ceci.

Maintenant vous voyez qu'il ne peut pas concaténer une chaîne de caractères, et toutes ces sortes de choses.

Convertissons-le simplement en une chaîne de caractères.

Exécutons cela à nouveau.

Vous voyez maintenant qu'il dit `4 is greater than 3`.

Nous avons vérifié si `a` est plus grand que `b`.

Nous pouvons aussi vérifier, évidemment, si `a` est plus petit que `b`.

Maintenant vous voyez que rien ne se passe.

Parce que nous avons dit qu'il devrait exécuter ce code seulement si `a` est plus petit que `b`. Puisqu'il n'est pas plus petit que `b`, le code n'est pas exécuté.

Nous pouvons aussi vérifier si `a` est la même chose que `b`.

Si `a == b`. Rendons `a` égal à `b`.

Et nous l'exécutons.

Vous voyez qu'il dit `4 is greater than 4` parce que c'était ce qu'il était censé dire, mais nous pouvons simplement dire `a equals b`.

Quand nous l'exécutons, vous voyez que c'est `a equals b`, alors que nous changeons cela maintenant en `3`.

Maintenant `4` n'est plus égal à `3`.

Il ne s'exécute pas.

C'est le concept de base des instructions `if`.

Nous pouvons aussi le faire pour différents types de données.

Disons que nous avons une chaîne de caractères, qui est `Tim`. `b` est aussi `Tim`.

Nous savons donc que `a` est égal à `Tim`, `b` est égal à `Tim`.

Évidemment `a` est la même chose que `Tim`.

Et ensuite vous dites `a equals b`.

Quand nous l'exécutons, vous voyez qu'il dit `a equals b`, puis nous pouvons aussi utiliser le booléen.

Disons `True`.

On peut dire `if a == True:`. Cela signifie que si `a` est vrai, alors nous pouvons simplement dire `a is true`.

Et ensuite nous pouvons simplement exécuter ceci.

Donc `a is true`.

C'est le concept de base d'une instruction `if`.

Mais nous pouvons aussi dire si `a` n'est pas vrai, ce qui signifie qu'il est quelque chose comme `False`.

Nous dirons `a is not true`.

Vous savez maintenant que c'est `False`.

Quand nous l'exécutons, il dit `a is not true`.

C'est ainsi qu'on utilise une simple instruction `if`.

Nous pouvons aussi ajouter deux types différents, comme si `a` est plus grand ou égal à `b`. Vous savez que `a` est plus grand que `b`.

Ou si `a` est plus grand ou égal à `b`, alors nous dirons... disons `True` ou quelque chose comme ça.

Exécutons-le, vous verrez qu'il dit `True` parce que `a` est plus grand que `b`.

Et si `a` est aussi égal à `b`, il dira toujours `True` parce que `a` est égal à `b`.

Mais maintenant, disons que `a` est plus petit que `b`.

Quand nous l'exécutons, rien n'a été exécuté.

Maintenant, nous voulons ajouter plus de fonctions à cette instruction `if`.

Il dit si `a` est plus grand ou égal à `b`. Vérifions si `a` est égal à `b`. Non, disons `a equals b`.

Mais que se passe-t-il si `a` n'est pas égal à `b` ? Que doit faire Python ? Que doit faire le code ? Doit-il simplement ne rien exécuter ? Nous pouvons maintenant ajouter `else`. Ce `else` signifie si `a`... corrigeons cela, si `a` n'est pas égal à cela.

Donc si `a` est égal à `b`, il doit afficher `a equals b`, puis `else` signifie tout sauf cela, alors il doit simplement afficher `a not equals b`.

Donc si `a` est égal à `b`, affiche ceci, sinon si c'est le contraire de cela, alors il doit simplement afficher `a is not equal to b`.

Maintenant, quand j'exécute ceci, il affiche `a is not equal to b`.

Voilà comment utiliser une simple instruction `if else`.

Nous pouvons aussi faire cela avec un booléen, rendons cela `True`.

Disons que si `a` est vrai, disons `a is true`.

Sinon, disons `not true`.

Quand nous l'exécutons, vous voyez qu'il dit `a is true`, si nous changeons cela en `False`.

Évidemment `a` n'est pas vrai.

Il dit donc `a not true`.

Voilà comment utiliser fondamentalement une simple instruction `if else`.

Nous pouvons aussi aller plus loin.

Disons que nous voulons ajouter plus d'une condition, comme si `a` est égal à `True`. `elif a == False:`.

Affichez `a is false`.

`else` n'est aucun des deux.

Donc si `a` est égal à `True`, il doit afficher `a is true`.

`elif` signifie que nous ajoutons une autre instruction, c'est la même chose que `if` mais `else if`. Cela signifie que vous avez `if`.

Donc si `a` n'est pas vrai, alors vous pouvez vérifier si `a` est faux.

Si `a` est faux, affichez ceci, mais si ce n'est aucun des deux, alors affichez simplement `a is none of the two`.

Maintenant, il devrait afficher `a is false` quand nous l'exécutons.

Vous verrez `a is false`.

Maintenant vous savez comment ajouter une instruction `elif` simple.

Nous pouvons ajouter n'importe quel nombre d'instructions `elif` que nous voulons ajouter, nous pouvons dire... un autre `elif a != 'a':`. Alors nous pouvons afficher... nous pouvons simplement afficher tout ce que nous voulons faire.

C'est la syntaxe de base pour utiliser une instruction `if else`.

Mais nous pouvons rendre cela plus... nous pouvons monter d'un cran.

Au lieu de dire si `a` est égal à `True`.

Nous pouvons spécifier une variable, disons `boy = True`.

Disons `short = True`.

Je peux dire `if boy == True:`. Alors affichez `is a boy`.

Puisque `boy` est vrai, ici même il n'y a rien de tel.

Changeons simplement ceci en `boy`, puisque `boy` est vrai, alors nous pouvons dire `is a boy`. Nous pouvons aussi faire quelque chose comme `if boy == True or short == True:`.

Cela signifie que si l'une de ces deux conditions est vraie, vous afficherez `is a boy or he is short`.

Quand j'exécute ceci, vous voyez `is a boy or he is short`.

Puisque les deux sont vrais, il affiche ceci. Si ceci est faux, c'est toujours comme s'il disait : si `boy` est vrai ou `short` est faux, il va toujours afficher ceci.

La raison pour laquelle il affiche toujours ceci est parce que nous utilisons `or`. Il va vérifier seulement une condition.

Si l'une de ces conditions est correcte, il exécute simplement ceci.

Quand j'exécute ceci, vous voyez `is a boy or he is short`.

Mais si je change cela maintenant en `and`.

Vous voyez qu'il n'affiche pas ceci, il affichera `a is none of the two`.

Enlevons simplement cet `elif` pendant un moment.

Maintenant vous voyez qu'il affiche l'instruction `else` `a is none of the two`.

Et c'est parce que nous utilisons `and` et il doit vérifier que ces conditions sont toutes les deux correctes.

Si l'une d'elles n'est pas correcte, il va simplement passer à l'instruction suivante et sauter cette instruction.

C'est la différence entre `or` et `and`.

Maintenant que nous connaissons les concepts, le concept de base des instructions `if`, `else` et `elif`, allons-y et faisons quelques exercices simples.

Disons que nous voulons utiliser l'instruction `if else` pour vérifier le type de données.

Et dire à l'utilisateur `Alright this data type is, let's say, a string, or it's a list`, quelque chose comme ça.

Tout d'abord, demandons à l'utilisateur de saisir quelque chose.

Disons que `value` devrait être une entrée.

Et nous dirons à l'utilisateur de saisir une valeur.

Une fois que l'utilisateur saisit une valeur, nous allons vérifier la valeur et dire à l'utilisateur `oh, this is your value`.

Nous pouvons utiliser une instruction `if` pour cela.

Nous voulons vérifier si l'instruction est une chaîne de caractères.

On peut dire `if type(value) == str:`. Alors nous afficherons...

Affichons simplement `value is a string`.

Ajoutons un `elif`.

Disons que nous voulons vérifier si le type est un entier.

`type(value) == int`. C'est un entier, nous afficherons `value is an integer`.

Et nous voulons aussi vérifier si c'est une liste. `elif type(value) == list:`.

Affichez `value is a list`.

Mais si ce n'est aucun de ceux-là, nous dirons simplement `we don't know`.

Ici même, je voulais ajouter ceci, mais évidemment il dit que Python dit que je l'ai fermé.

Pour que j'ajoute ces guillemets là, je dois utiliser le backslash.

Maintenant, une fois que j'utilise le backslash, cela va être affiché avec.

Maintenant nous pouvons dire que nous ne connaissons pas le type de données ou quoi que ce soit que l'utilisateur a écrit comme valeur.

Fermons cela rapidement.

Et testons cela.

Nous saisissons la valeur, laissez-moi saisir `6`. Il dit que `6` est une chaîne de caractères. Ce n'est pas correct ici.

La raison pour laquelle c'est une chaîne de caractères est parce que tout ce que nous saisissons, Python le voit automatiquement comme une chaîne de caractères.

Si nous voulons obtenir cela comme un entier, nous devons taper `int()`, nous devons le convertir en entier.

Ce type d'exercice ne fonctionne donc que pour les chaînes de caractères.

Nous changeons donc le nom de cet exercice en "vérification s'il s'agit d'une chaîne de caractères seulement".

Ce que nous voulons simplement faire, c'est annuler cela, nous ne vérifions pas l'âge ou la liste ou tout autre type de données, nous vérifions simplement si c'est une chaîne de caractères.

C'est parce que Python le voit automatiquement comme une chaîne de caractères.

Et nous devons le convertir en un entier si nous voulons savoir si c'est un entier.

Nous pouvons aussi aller plus loin pour vérifier s'il s'agit d'un entier en utilisant des instructions `if` complexes, ou des expressions régulières (regex) dont nous n'avons pas besoin de nous soucier pour le moment.

Mais pour l'instant, tenons-nous-en à cet exercice de base.

Nous vérifions donc si c'est une chaîne de caractères.

Si c'est une chaîne de caractères, nous disons `the string is`, sinon nous disons `is not a string`.

Nous amenons tout cela en haut.

Ici même, c'est là que cela devrait être, s'il y a un espace, et ensuite exécutons-le à nouveau.

Maintenant, quand j'affiche la valeur, et que je dis `I know`, vous pouvez voir qu'il devine que c'est une chaîne de caractères.

C'est fondamentalement comment le faire.

Mais si nous voulons changer ou dire entier.

Tout ce que nous saisissons est automatiquement vu comme un entier.

Il dira donc automatiquement que la valeur n'est pas une chaîne de caractères.

Même si je mets `6`.

Maintenant il dit `cannot concatenate str`.

C'est simplement parce que nous devons convertir cela en chaîne de caractères avant de concaténer.

Ou, laissez-moi vous montrer une meilleure façon de le faire.

Puisque nous n'en traitons qu'un seul.

Au lieu d'utiliser `+` ici, je peux simplement utiliser une virgule.

Quand j'exécute ceci, à nouveau, je saisis un entier, il dit `7 is not a string`.

Le deuxième exercice que nous allons faire est de vérifier si un nombre est divisible par cinq.

Nous savons que nous avons des nombres, des multiples de cinq, ou quelque chose comme ça. Cela signifie les nombres par lesquels cinq peut être divisé.

Nous avons `5` lui-même, nous avons `10 15 20`. Si nous vous donnons quelque chose comme `17`, nous voulons qu'il nous dise que `17` ne peut pas être divisé par cinq.

Nous allons donc automatiquement obtenir une entrée tout d'abord, et nous assurer que c'est un entier.

Disons `input a number`.

Et ensuite nous dirons si la valeur... ce que cela fait est que `value` est essentiellement le nombre que l'utilisateur a saisi.

Et puis ce signe de pourcentage signifie le reste.

Nous dirons si la `value % 5 == 0`.

Tout d'abord, laissez-moi couper cela.

Et laissez-moi vous montrer ce que cela fait.

Si je dis `print(20 % 5)`.

Maintenant vous allez voir qu'il va afficher `0`, il va afficher le reste de cette division.

Quand je dis `print(22)`, il devrait m'afficher `2`, parce que `22` divisé par `5` est `4`, alors le reste devrait être `2`. Vous voyez ici que nous avons `2`. Ramenons cela rapidement.

Maintenant nous disons que si la `value % 5 == 0`. Cela signifie que si le reste est égal à zéro, alors évidemment, cette valeur peut être divisée par cinq, sinon la valeur ne peut pas être divisée par cinq.

Puisque nous utilisons un entier, ajoutons une virgule ici, comme ceci.

Cela devrait fonctionner.

Il nous donne un nombre, disons `100`. Maintenant il dit `100 can be divided by 5`.

Exécutons cela à nouveau et donnons-lui un nombre qui ne peut pas être divisé par cinq comme `106`.

Il dit `106 cannot be divided by 5`.

Voilà comment construire un programme de base avec des vérifications pour savoir si un nombre peut être divisé par cinq.

Le dernier exercice que nous allons faire sur l'instruction `if else` va être l'exercice pour vérifier si la longueur d'une phrase est inférieure à `10`.

Encore une fois, nous allons collecter une valeur, mais cette fois-ci, ce ne devrait pas être un entier.

Puisque cela va être une phrase.

Maintenant, je veux vérifier si la longueur de cette phrase est inférieure à `10`.

Si la longueur de la phrase est inférieure à `10`, alors nous dirons `value is less than 10`.

Sinon, nous dirons `value is more than 10`.

Saisissons des choses au hasard comme `my name is my name`.

C'est évidemment plus de `10`.

J'appuie sur Entrée, il dit `not supported between instances`.

Parce que ceci n'est pas vu comme un entier, nous ne pouvons pas faire cela.

Chaque fois que nous utilisons ce "inférieur à" ou "égal à", cela doit être un entier, nous ne pouvons pas faire "inférieur à" ou "égal à" pour une chaîne de caractères.

Il y a d'autres façons de faire cela, nous allons en parler.

Nous aurions pu résoudre cela maintenant.

Mais je laisse cela pour le tutoriel, parce que je ne veux pas sauter d'étapes.

Pour le tutoriel, nous allons revenir à cet exercice et je vais vous montrer comment faire cela avec des chaînes de caractères.

Mais pour l'instant, j'espère que vous avez compris le concept de l'utilisation de l'instruction `if else`.

Avant de continuer avec plus de concepts en Python, nous voulons juste faire un programme Python simple qui vérifie si un nombre est un nombre pair ou un nombre impair.

Comme nous le savons, un nombre pair est un nombre qui peut être divisé par deux, un nombre impair est celui qui ne peut pas l'être.

Cela ne devrait pas nous prendre plus de deux minutes à faire.

Je vais donc simplement appeler une entrée de l'utilisateur et la nommer `number`. Nous dirons `input` et nous dirons `Enter a number`.

Et ensuite nous voulons nous assurer que c'est un entier.

Et ensuite nous allons dire `if number % 2 == 0:`. Alors évidemment, c'est un nombre pair.

Ce que cela fait, c'est que si le reste du nombre divisé par deux est égal à zéro, alors c'est un nombre pair.

Sinon.

Nous disons simplement `odd number`.

Quand nous exécutons ceci, nous mettons la valeur de, disons, `26`.

Puisque c'est un nombre pair, nous l'exécutons à nouveau et mettons `767`. `767` est un nombre impair.

Voilà comment faire un exercice simple comme celui-là en utilisant des instructions `if` en Python.

Dans ce tutoriel, nous allons parler des dictionnaires en Python.

Les dictionnaires sont utilisés pour stocker des valeurs de données dans des paires clé-valeur (key-value pairs).

Les dictionnaires sont aussi un type de données, tout comme les listes, tout comme les chaînes de caractères.

Le dictionnaire est aussi un type de données.

Mais ce dictionnaire stocke les valeurs dans une paire de clés et de valeurs.

Tout comme un dictionnaire principal, comme un dictionnaire anglais, où nous avons le mot comme clé, et la valeur comme la signification de ce mot, c'est fondamentalement ainsi que fonctionne un dictionnaire.

Les dictionnaires sont modifiables, ce qui signifie que vous pouvez les modifier même après les avoir configurés ou assignés.

Mais ils ne permettent pas les doublons, contrairement aux listes ou aux tuples, où vous pouvez saisir une valeur plus d'une fois. Dans un dictionnaire, vous ne pouvez pas faire cela.

Laissez-moi vous montrer comment écrire un dictionnaire en Python.

Laissez-moi nommer ce dictionnaire `my_dict`. Pour écrire un dictionnaire, nous allons utiliser ces accolades, et ensuite nous allons lui donner la clé.

La clé peut être quelque chose comme `name`, et ensuite je vais utiliser ces deux points.

Et la valeur peut être `Tim`.

Et ensuite je vais mettre une virgule.

Je peux avoir une autre clé et valeur, disons `age`.

Non, laissez-moi dire quelque chose comme `nationality`.

Je peux dire quelque chose comme `African` ou quelque chose comme ça.

Et ensuite ayons ces deux-là.

Laissez-moi en donner un de plus.

Je dirai `qualification`.

Disons `college degree` ou quelque chose comme ça.

C'est un dictionnaire de base en Python.

Commençons par la chose de base en affichant simplement ce dictionnaire sur notre écran.

Affichons simplement `my_dict`.

Une fois que nous affichons cela, vous voyez qu'il nous donne juste le dictionnaire : `name Tim nationality African qualification college`.

Mais maintenant, disons que nous voulons seulement afficher cette valeur de `name`, nous voulons afficher la valeur de ce `name`.

C'est la valeur et c'est la clé assignée à cette valeur.

Cela signifie que si nous voulons obtenir cette valeur, nous devons chercher cette clé.

Tout comme lorsque vous allez en ligne et cherchez la signification de quelque chose, la signification de n'importe quoi.

Par exemple, la signification de `order`. Donc `order` est la clé, puis la valeur que vous cherchez est la définition.

C'est ainsi que fonctionne le dictionnaire. C'est très similaire au dictionnaire de mots normal.

Maintenant, une fois que vous obtenez la valeur de ce `name`, nous pouvons simplement utiliser les crochets après cela et dire `name`.

Ce que cela va afficher pour nous est `Tim` ici même, vous pouvez voir `Tim`, qui est la valeur de ce `name`.

Il y a d'autres choses que nous pouvons faire, comme je l'ai dit, les doublons ne sont pas autorisés dans le dictionnaire.

Disons que j'ai deux noms.

Et l'autre est `John`.

Quand j'essaie d'afficher ceci, vous voyez qu'il affiche seulement le deuxième, c'est-à-dire le plus récent, il supprime automatiquement celui-ci. C'est ce que je veux dire par doublon non autorisé dans les dictionnaires, vous ne pouvez pas avoir deux clés avec le même nom, nous pouvons avoir deux valeurs.

Disons que ceci est nommé `name2`.

`name2` peut toujours être le même.

Si j'affiche ceci, vous verrez que `name` est `Tim`, `name2` est aussi `Tim`.

Nous pouvons donc avoir les valeurs identiques, nous pouvons répéter cela.

Mais la clé assignée ne peut pas être répétée.

Elle ne peut pas être un doublon.

Maintenant, disons que nous voulons obtenir la longueur de ceci.

C'est très facile à obtenir en disant `len()`.

Comme ceci, une fois que nous l'affichons, vous voyez qu'il nous dit `4` parce que nous avons quatre clés et valeurs ici.

Et ensuite, nous pouvons aussi mélanger les types de données.

Vous savez que... laissez-moi simplement supprimer ceci, vous savez que ce `name`, la valeur qui lui est assignée est une chaîne de caractères. La valeur à côté de `nationality` est aussi une chaîne de caractères, et la valeur assignée à `qualification` est aussi une chaîne de caractères.

Mais nous pouvons le changer, disons que nous voulons ajouter, par exemple, `age`, et nous savons que l'âge sera évidemment un entier, nous pouvons simplement l'ajouter ici, disons `27`.

Normalement, nous écririons un entier sans les guillemets, alors nous allons l'écrire là-dedans.

Et ensuite, une fois que nous l'affichons, nous pouvons toujours continuer et afficher.

Cela va afficher `27` sans problème.

Vous pouvez le voir ici même `27`, nous pouvons aussi ajouter un booléen, nous pouvons dire `is_tall`.

Donc `is_tall` peut être `True`.

Et ensuite, une fois que nous affichons l'âge, je veux dire une fois que nous affichons `my_dict`.

Vous voyez qu'il affiche `True`.

Cela nous dit que d'accord, cette personne est grande.

Nous pouvons donc ajouter différents types de données.

Et ce qui est très cool, c'est que nous pouvons aussi ajouter une liste, donc nous pouvons avoir une liste de ses amis.

On peut mettre le type de données comme une liste comme ceci. On peut dire que l'un de ses amis est `Peter`.

On peut dire `Paul`, on peut dire `Precious`. Et maintenant, une fois que nous affichons `friends`.

Cela va simplement nous afficher une liste.

D'accord, ici même, il dit erreur de syntaxe invalide.

Et ce serait parce que nous avons oublié d'ajouter une virgule ici même.

Nous devons donc nous assurer d'ajouter une virgule avant d'ajouter une autre valeur.

Une fois que nous cliquons sur Entrée, vous voyez qu'il nous donne `Peter`, `Paul` et `Precious`.

Maintenant, affichons simplement tout le dictionnaire sans rien d'attaché.

Nous descendons ici, nous voyons qu'il affiche tout ce qui concerne ce dictionnaire nommé `Tim` et tout ce que nous devons savoir.

Et ensuite, pour vérifier s'il s'agit d'un dictionnaire, nous pouvons aussi utiliser le `type()`.

Mettez simplement `type()` ici, cela va afficher `dict` pour nous.

Vous pouvez voir ici même `class dict`, ce qui signifie que ceci est un dictionnaire.

Nous pouvons aussi rendre cela plus amusant.

En spécifiant une variable, disons que nous avons une variable nommée `x`.

Et nous voulons que cette variable soit égale à l'une des valeurs de ceci.

Nous pouvons donc simplement dire que `x` peut être égal à `my_dict['name']`.

Donc `x` est maintenant le nom.

Une fois que vous affichez `x`, évidemment il affiche le nom.

Ce sont des fonctions de dictionnaire de base et des méthodes de dictionnaire.

J'espère que vous avez compris le concept de dictionnaire en Python.

Dans ce tutoriel, nous allons parler de la boucle `while` en Python.

La boucle `while` est une fonctionnalité de Python qui vous permet de boucler à travers un bloc de code tant qu'une certaine condition est vraie.

Disons que vous avez une condition comme : si un nombre est plus grand que `10`, alors il doit simplement boucler à travers un groupe de code en dessous.

C'est juste comme une fonction avec une instruction `if` ou quelque chose comme ça.

Nous lui donnons une condition et en dessous nous avons un groupe de code que nous voulons boucler.

Laissez-moi vous montrer comment utiliser la boucle `while` en Python.

Tout d'abord, nous pouvons spécifier une variable nommée `i`, disons qu'elle est égale à `1`.

Et pour utiliser une boucle `while`, nous pouvons dire `while i < 6:`.

C'est une condition, nous disons tant que `i` est inférieur à `6`.

Alors nous voulons simplement afficher `i`.

Et ensuite nous voulons simplement incrémenter `i` par `1`.

On peut donc dire `i = i + 1`.

Cela va simplement exécuter cette boucle `while`, tant que `i` est inférieur à `6`, cela va simplement l'afficher à l'écran, et ensuite cela va l'augmenter de `1`, puis l'exécuter à nouveau, l'exécuter à nouveau, jusqu'à ce qu'il s'assure qu'il ne dépasse pas `6`, qu'il n'atteigne pas `6`.

On peut aussi incrémenter cela en tapant `i += 1`, c'est la même chose, n'importe lequel fonctionnera.

Quand nous exécutons ceci, vous voyez maintenant `1 2 3 4 5`.

Ce qui s'est passé, c'est qu'il a bouclé à travers ce bloc de code.

Nous avons dit tant que `i` est inférieur à `6`. Donc cela a dû boucler à travers ce bloc de code, il a affiché `i`, puis après cela nous l'avons incrémenté, donc maintenant `i` est égal à `2`, c'est toujours inférieur à `6`. C'est pourquoi nous avons `2`, puis il a fait la même chose, il l'a incrémenté, nous avons `3 4 5`.

Mais après `5`, il a fait la même chose, il l'a incrémenté de `1`, mais maintenant `i` est égal à `6`. Donc parce que cette condition est vraiment fausse, elle n'est plus inférieure à `6`, alors la boucle `while` s'arrête, elle s'interrompt en quelque sorte.

C'est fondamentalement ce qu'est la boucle `while`, c'est très important en Python, il y a beaucoup de programmes Python que vous voudrez construire où nous aurons besoin d'utiliser une boucle `while` pour boucler à travers différentes choses avec une condition.

Et ensuite vous pouvez aussi faire plus de choses comme `while i < 6 or i == 6`, quelque chose comme ça.

Maintenant vous savez que quand nous exécutons ceci, cela devrait nous afficher `1` à `6`. Parce que ce n'est plus seulement quand `i` est inférieur à `6`, c'est aussi quand il est égal à `6`.

Maintenant cela nous donne une erreur, parce que lorsqu'on écrit "égal à" en Python, cela doit être double.

Exécutons-le à nouveau.

Maintenant vous voyez `1 2 3 4 5 6`.

Donc la boucle `while` en Python boucle à travers un bloc de code tant qu'une certaine condition est vraie.

Puisque c'est vrai, l'une de celles-ci est vraie. Elle affiche simplement `i`, l'augmente de `1`, revient, exécute ce code à nouveau, l'augmente de `1`, revient, et ensuite elle s'assure qu'elle va jusqu'à `6`.

On peut aussi dire `i = 10`. Une fois que j'exécute ceci, cela nous donne `1 2 3 4 5`.

Si nous disons `and`. Et maintenant nous l'exécutons, cela ne nous donne rien.

Parfois, les conditions d'une boucle `while` ne sont pas similaires à l'instruction `if`, vous savez, où nous pouvons faire soit c'est inférieur à `6` et c'est ceci, alors vous devriez faire une certaine chose.

Maintenant vous pouvez voir que si `i` est inférieur à `6` et `i` est égal à `10`.

La raison pour laquelle cela ne s'est pas exécuté est parce qu'au début `i` est inférieur à `6`. Donc cela devrait s'exécuter, mais nous avons dit `and` et il doit aussi être égal à `10`. Mais nous savons que `i` ici n'est pas égal à `10`.

Si je change cela en `10`. Cela ne s'exécutera toujours pas.

Et la raison pour laquelle cela ne s'exécutera pas est parce que l'une de celles-ci n'est pas correcte.

`i` n'est pas inférieur à `6` parce que `10` n'est pas inférieur à `6`.

Mais si nous disons `i < 16`. Maintenant, cela va afficher quelque chose.

Ne nous soucions pas du `and` pour le moment. Changeons cela en `1`. Changeons cela en `10`.

Maintenant, quand nous exécutons ceci, nous devrions obtenir `1` à `9`. Laissez-moi simplement agrandir ceci, nous voyons que nous avons `1 2 3 4 5 6 7 8 9`.

C'est fondamentalement le concept de base de la boucle `while` en Python.

Dans ce tutoriel, nous allons parler des boucles `for` en Python.

La boucle `for` est utilisée pour itérer sur une séquence.

Cela signifie qu'elle est utilisée pour boucler sur une séquence.

Et cette séquence peut être soit une liste, un tuple, un dictionnaire, même une chaîne de caractères, une plage de nombres, cela peut être tout ce qui est une liste.

Nous utilisons la boucle `for` pour boucler à travers eux.

La boucle `for` est très utilisée en Python, elle est beaucoup utilisée en Python, en fait, parce que la plupart du temps nous avons des listes de données, nous avons de grandes quantités de données. Maintenant, la boucle `for` est utilisée, encore une fois, pour boucler à travers chaque quantité de données, chaque valeur dans ces données.

Laissez-moi vous montrer comment nous faisons une boucle `for`, ou comment nous appelons la boucle `for` en Python, c'est très facile.

Pour taper une boucle `for`, la première chose que vous devez faire est de taper ce mot-clé `for`.

Ce mot-clé montre que nous voulons boucler à travers quelque chose.

On peut dire `for letter in 'Hello':`.

C'est un "pour chaque lettre dans Hello", qui est `H E L L O`, nous voulons simplement afficher `letter`.

Quand j'exécute ceci, vous verrez qu'il l'affiche différemment, il affiche tout séparément.

Il boucle donc à travers chaque lettre dans cette chaîne de caractères `Hello`, itérant à travers la séquence.

Nous pouvons aussi faire cela en ayant une liste.

Disons `my_list`. Je vais donner à cette liste n'importe quoi, disons `gi j Yu Gi Oh`.

Maintenant nous pouvons boucler à travers cela et dire `for letter in...`.

Notez que cela peut être n'importe quoi, laissez-moi juste ceci dans lequel j'ai mis `letter`, cela peut être dénoté par n'importe quoi.

Cela peut être représenté par n'importe quoi.

Quand j'ai commencé avec Python, j'étais un peu confus dans ces boucles `for`, simplement à cause de ce `letter`.

J'ai donc pensé que, puisque nous utilisons `Hello`, et que chacun est un caractère, chacun est une lettre, nous devons utiliser `letter` pour chacun.

Mais maintenant je veux juste clarifier cela pour que personne n'ait à subir cette confusion.

Cela peut donc être dénoté par n'importe quoi.

Si je dis `for x in 'Hello':` et que je dis simplement `print(x)`, cela va faire exactement la même chose.

Si je dis `for gi` ou pour n'importe quoi que je fais, cela peut être dénoté par n'importe quelle chose.

Laissez-moi donc simplement... je veux juste dire `for items` ou `for values` serait mieux.

`for values in my_list:`.

Je vais donc enlever cette chaîne de caractères et mettre `my_list`.

Maintenant je veux juste afficher `values`.

Une fois que j'appuie sur exécuter, vous voyez qu'il affiche tout `gi ju j yu gi oh`.

C'est fondamentalement comment boucler à travers une liste.

Maintenant vous pouvez boucler à travers n'importe quoi, en fait, vous pouvez boucler à travers un dictionnaire. Disons que nous avons un dictionnaire simple.

Et ensuite, disons que nous avons des accolades, et ensuite nous avons `name John`, nous avons `age 13`. Laissez-moi juste laisser ces deux-là.

Maintenant vous pouvez voir `for values in my_dict: print(values)`.

Comme j'affiche ceci, vous voyez qu'il dit `name`, `age`.

Il affiche donc fondamentalement ces deux que nous avons, `name` et `age`.

C'est donc itérer sur une liste de valeurs.

Et ensuite, dans la boucle `for`, il y a aussi quelque chose que nous appelons le `break`.

Revenons à notre liste.

Oui, donc ici même, nous avons toujours cette `my_list`. Je dirai `for values in my_list: print(values)`. Mais je peux dire si `values == 'Jeju'`, alors je veux que tu t'arrêtes (`break`).

Ce que cela va faire, c'est qu'il va boucler un par un, il va de `gi` à `Jeju`.

J'ai donc dit qu'une fois qu'il arrive à ce `Jeju`, il doit s'arrêter, il doit arrêter cette boucle.

Une fois que j'exécute ceci, vous allez voir juste `gi` et `Jeju`.

Maintenant, pourquoi cela ? J'ai dit qu'il devrait continuer à boucler, afficher toutes les valeurs, mais une fois qu'il arrive à cette valeur égale à `Jeju`, il doit s'arrêter. Une fois qu'il boucle sur ce `Jeju`, alors il s'arrête.

C'est pourquoi nous n'avons pas `gi oh` ici même.

Maintenant, nous pouvons aussi, au lieu d'avoir le `break` ici, je peux faire quelque chose comme ça.

Même avant d'afficher `values`, je peux avoir mon instruction `if`.

Et je peux dire `for value in values, if value == 'Jeju' break`.

Et après ce `break`, je peux afficher `values`.

Si vous n'avez pas compris maintenant, la différence est que si `value` est `value`... donc il boucle à travers ces valeurs.

Mais si la valeur est `Jeju`, il doit s'arrêter.

Vous savez, la dernière fois, il a d'abord affiché la valeur, il a d'abord affiché `Jeju` avant de s'arrêter.

Mais maintenant, si la valeur est `Jeju`, il doit s'arrêter avant même d'afficher.

Il va donc deviner que nous avons `Jeju` et qu'on veut s'arrêter, puis nous allons afficher. Python exécute le code ligne par ligne, il exécute d'abord ce code, puis celui-ci, puis celui-là.

La première chose qu'il voit est que nous vérifions si ce que nous voulons boucler ensuite est `Jeju`.

Et nous voyons que oui, c'est vrai, c'est `Jeju`. Maintenant nous nous arrêtons simplement, puis après nous être arrêtés, nous affichons `values`, donc la seule valeur que je veux afficher est `gi` parce que nous nous sommes arrêtés quand nous sommes arrivés à `yu`.

Quand j'exécute ceci, vous voyez que je n'ai que `gi`, nous n'affichons plus `Jeju`.

C'est fondamentalement comment utiliser le `break` dans une boucle `for`.

Mais nous pouvons aussi boucler à travers une plage de nombres.

Disons que nous avons `for x in range(4):`.

Maintenant, ce que je peux faire, c'est afficher `x`.

Une fois que j'affiche `x`, cela va me donner une liste de nombres de zéro à trois.

Cela va donc me donner une plage de nombres commençant de zéro jusqu'au dernier nombre avant quatre.

Je peux aussi changer cela en `10`, cela va me donner de zéro à neuf.

Comme vous pouvez le voir, cela me donne de zéro à neuf.

Et ensuite, nous pouvons aussi spécifier pour chacun de boucler à travers une plage particulière de nombres.

Nous avons donné `0` à `10`. Mais nous pouvons dire à chaque boucle de boucler de trois à sept, ou de dix à soixante-dix, ou n'importe quel montant.

Si nous voulons qu'il boucle de trois à sept, voici comment nous allons le faire, nous disons simplement `for x in range(3, 7):`. Boucle à travers ce nombre.

Quand j'exécute cela, vous voyez qu'il me donne `3 4 5 6`, il ne commence pas à partir de zéro.

Il boucle donc de trois jusqu'à ce sept.

C'est ainsi qu'on boucle à travers une plage particulière de nombres.

Et la dernière chose que je vais vous montrer dans la boucle `for` est que nous pouvons aussi utiliser l'instruction `else`.

Bouclons pour une plage de sept.

Après avoir bouclé, nous pouvons dire `else:`. Ce que fait ce `else`, c'est qu'une fois que cette boucle est finie, une fois qu'elle est terminée, nous pouvons simplement afficher `finished looping`.

Maintenant, une fois que j'exécute ceci, il affiche de zéro à six, et il dit `finished looping`.

C'est ce que fait l'instruction `else`, c'est qu'elle finit d'abord la boucle, elle finit d'abord d'itérer sur la séquence, puis elle nous dit simplement ce qui se trouve dans l'instruction `else`.

C'est une introduction aux boucles `for` en Python.

Dans cette partie, nous allons parler des listes 2D en Python.

Les listes 2D signifient également listes à deux dimensions.

C'est comme lorsque nous avons plusieurs listes à l'intérieur d'une variable de liste.

Maintenant, nous pouvons avoir une liste normale comme `my_list` qui peut être juste des nombres comme `1 2 3 4`. Une fois que nous affichons `my_list`, sachez que nous allons obtenir `1 2 3 4`, ce qui est une liste normale.

Mais maintenant nous voulons avoir une liste 2D, tout d'abord il est recommandé d'appuyer sur Entrée juste pour organiser l'indentation, puis nous allons avoir une liste.

Celle-ci peut être `1 2 3`.

Et ensuite nous pouvons avoir une autre ligne, qui peut être `4 5 6`, puis nous ajoutons une virgule sur une autre ligne peut être `7 8 9`.

C'est une liste 2D, car elle a des lignes et des colonnes.

C'est évidemment une liste dans une liste.

C'est comme la liste de haut niveau et ses sous-sections ou quelque chose comme ça.

Maintenant, une fois que nous affichons simplement `my_list`, vous verrez qu'il nous donne juste cette liste normale.

Mais disons que nous voulons obtenir cette valeur de un ou deux.

Nous allons l'obtenir en utilisant le numéro d'index.

Nous savons donc que le numéro d'index de ceci est `0`, qui est le premier, puis nous voulons aussi obtenir la première valeur, qui serait `0`.

Une fois que nous affichons cela, vous verrez que nous avons `1`.

Mais disons que nous voulons obtenir la valeur de cinq.

Nous savons donc que le numéro d'index de ceci est `1`, alors quel est le numéro d'index de cinq ? C'est aussi `1`.

Maintenant que j'exécute ceci, vous voyez maintenant que j'ai `5`.

C'est fondamentalement comment naviguer pour afficher ou obtenir certaines valeurs de vos listes 2D.

Et ensuite, nous pouvons aussi boucler à travers cela.

Je vais vous présenter les boucles imbriquées.

Les boucles imbriquées sont celles où vous avez une boucle dans une boucle, une boucle `for` pour être spécifique, quand vous avez une boucle `for` dans une boucle `for`.

Maintenant, au lieu de simplement afficher, disons simplement `for list in my_list:`. Puis affichons simplement `my_list`.

Quand j'exécute ceci, vous voyez qu'il affiche juste ma liste, j'ai une liste dans ma liste, il boucle simplement à travers cela.

Mais au lieu de simplement boucler à travers cela ou de simplement afficher cela, je peux ajouter une autre boucle `for` dedans. Donc `for list in my_list`, et je peux dire `for row in list:`.

Alors maintenant nous voulons afficher `row`.

Quand j'exécute ceci, cela nous donne une erreur parce qu'en Python, il doit y avoir une indentation pour montrer que ceci est sous cela.

Exécutons-le à nouveau.

Maintenant vous voyez qu'il dit `type object is not iterable`.

Pour `for row in list`, je dois m'assurer que tout est intact.

J'ai mis la liste, mais le nom de ceci est `list`.

Après cela, c'est maintenant quand j'exécute ceci à nouveau, vous voyez qu'il me donne... laissez-moi simplement ouvrir ceci.

Vous voyez qu'il me donne de un à neuf, c'est-à-dire chaque chose que nous avons ici `1 2 3 4` jusqu'à neuf.

C'est ainsi qu'une boucle imbriquée fonctionne.

C'est comme boucler à travers une boucle déjà existante.

Une boucle dans une boucle.

Je ne l'ai pas essayé auparavant, mais je pense que nous pouvons aussi avoir une autre boucle encore en bouclant à travers quelque chose comme ça.

Il y a diverses choses que vous pouvez essayer avec Python, c'est génial.

J'espère que vous comprenez les concepts de base des listes 2D et des boucles imbriquées.

Dans cette partie du tutoriel, nous allons parler des commentaires en Python.

Les commentaires sont utilisés pour empêcher un code particulier ou un bloc de code de s'exécuter avec votre programme réel.

Disons que nous avons `print('Hello')`.

Et ensuite nous avons aussi `print(1)`.

Quand j'exécute ceci, vous allez voir qu'il affiche `Hello 1`.

Si je viens ici et que je mets un hashtag `#` juste à côté de `print`.

Comme ceci, vous voyez que ceci est grisé, cela ne fait plus partie de notre code, c'est toujours là.

Mais quand je l'exécute, il ne va pas être exécuté avec notre code, seul le `1` s'affiche.

C'est à cela que servent les commentaires, principalement en Python. Les commentaires sont principalement utilisés en programmation en général pour expliquer notre code ou pour prendre des notes dans notre code, pour rendre notre code plus lisible.

En Python, vous pouvez aussi simplement ajouter un commentaire, disons que vous voulez tester rapidement votre code sans un bloc de code particulier, vous pouvez aussi utiliser les commentaires.

Vous pouvez aussi ajouter un commentaire, disons à la fin.

Comme vous pouvez voir `# this line prints Hello`.

Vous pouvez donc l'utiliser pour expliquer votre code.

Ou vous pouvez simplement l'utiliser pour empêcher le code de s'exécuter.

Et comme vous l'avez vu, si vous voulez commenter plus d'une ligne, vous pouvez mettre un hashtag sur cette ligne, sur la deuxième ligne, alors tout sera commenté.

Mais il y a aussi une meilleure façon de faire cela en Python, vous pouvez simplement ajouter... disons que vous avez un bloc de code, ou que vous avez une fonction comme `my_func`.

Et ensuite cette fonction affiche simplement `Hi`.

Maintenant, disons que vous voulez simplement commenter cette fonction particulière.

Ce que vous allez faire, c'est qu'au-dessus de la fonction, vous allez ajouter trois guillemets comme ceci.

Et comme vous pouvez le voir, cela commente automatiquement tout votre code.

Si nous exécutons ceci maintenant, rien ne va s'exécuter du tout.

Il dit que nous avons une erreur de syntaxe et des choses comme ça.

Nous devons donc fermer ces commentaires en remettant ces trois guillemets là où nous voulons les fermer, donc nous voulons fermer du début de cette fonction jusqu'à la fin.

Quand nous exécutons ceci, nous verrons que `print('Hello')` et `print(1)` s'exécutent.

Maintenant nous essayons d'exécuter ceci en disant `my_func()`.

Vous voyez, cela va nous donner une erreur.

Il dit `NameError: name is not defined`, cela signifie qu'il ne voit même pas cette partie du code où nous avons défini la fonction quand nous essayons de l'exécuter, cela ne fonctionne pas.

C'est à cela que servent les commentaires en Python, principalement deux choses : supprimer votre code, ou prendre des notes ou rendre votre code plus lisible.

Dans ce tutoriel, nous allons construire une calculatrice de base en utilisant Python.

Nous allons utiliser toutes les compétences et tout ce que nous avons appris dans les sessions précédentes, nous allons les additionner ensemble et ensuite construire une calculatrice simple.

Ce que nous voulons faire, c'est d'avoir trois entrées, collecter trois entrées d'un utilisateur, qui sont le premier nombre, le deuxième nombre et l'opérateur.

La calculatrice que nous voulons faire est très basique, c'est juste celle qui va additionner, soustraire, diviser, multiplier deux nombres ensemble.

Nous voulons donc collecter un nombre, qui serait `num1`, et le deuxième nombre, qui serait `num2`, et l'opérateur. L'opérateur est si vous voulez additionner ou soustraire, ou tout ce que vous voulez faire.

Définissons cela, disons que `num1` devrait être égal à une entrée.

On peut dire `Enter first number`.

Et ensuite nous allons faire la même chose.

Disons `num2 = input('Enter second number')`.

Et ensuite disons `op = input('Enter operator')`.

Maintenant que nous avons les trois entrées, nous allons utiliser une instruction `if`.

Ce qui va se passer, c'est que si l'opérateur (`op`) est égal à l'addition.

Maintenant nous voulons simplement additionner le premier nombre et le deuxième nombre, puis nous allons utiliser un `elif` pour obtenir la soustraction, peu importe, alors nous allons faire selon l'opérateur que l'utilisateur a saisi.

Disons que si `op == '+'`.

Alors s'il est égal à plus, nous allons simplement afficher `num1 + num2`.

Testons cela.

Ici même, disons `2` et `3`.

Et je veux additionner. Vous voyez qu'il dit `23`, ce qui est très faux, deux plus trois est censé être cinq.

La raison pour laquelle il dit `23` est parce qu'il voit toujours cela comme une chaîne de caractères.

Si je survole, vous voyez qu'il dit `str`. Mais il est censé le voir comme un entier.

Puisque c'est une chaîne de caractères, il est juste en train de les concaténer ensemble, mais nous voulons que ce soit un entier, pour qu'il puisse effectuer l'opération normale.

Nous devons donc dire `int(num1)`. Nous allons coller cela, nous allons faire la même chose pour le deuxième `int(num2)`.

Maintenant, quand nous exécutons ceci, cela devrait fonctionner.

Saisissons le premier nombre, disons `75`.

Notre deuxième devrait être `25`.

Je veux additionner. Maintenant, il me donne `100`. Il les additionne ensemble, c'est ce que nous voulons qu'il se passe.

Faisons juste quelques ajustements.

Disons que l'addition est `num1 + num2`.

Mais maintenant nous voulons vérifier : et si un utilisateur saisit une soustraction ? Donc si un utilisateur dit soustraire, alors nous voulons simplement afficher que la soustraction est `num1 - num2`.

Nous devons nous assurer de fermer ce signe ici même. Nous savons que nous pouvons faire cela, nous pouvons dire que la soustraction est `num1 - num2` parce que c'est une chaîne de caractères, c'est un nombre.

Et ensuite c'est une chaîne de caractères.

Ce que nous pouvons faire maintenant est de mettre une virgule ici même.

Testons-le.

Si je dis `70` et `20`, je vais soustraire, cela me donne que la soustraction est `50`, ce qui est bien.

Et faisons la même chose pour la multiplication.

Nous dirons simplement que la multiplication est `num1 * num2`.

C'est l'arithmétique de base pour la multiplication.

Et ensuite nous allons faire exactement la même chose pour la division.

Donc s'il est égal à diviser, alors nous affichons simplement que la division est `num1 / num2`.

Maintenant cela devrait fonctionner.

Quand je l'exécute, et que je dis `60` et `20`, et que je veux diviser, vous voyez, cela me donne que la division est `3.0`.

Et si je fais quelque chose comme la valeur absolue de ceci ? Non.

Valeur absolue de ceci, laissez-moi l'exécuter à nouveau.

Maintenant si je dis `60` et `20`.

Je mets diviser. D'accord, donc il m'a donné `3.0`. Je m'attendais à ce qu'il me donne `3`.

Mais nous allons contourner cela.

Voilà comment construire une calculatrice de base en utilisant Python en obtenant les entrées de l'utilisateur et en utilisant des instructions `if`. Instruction `if`, instruction `elif`.

Ajoutons une chose de plus.

Si l'utilisateur ne saisit pas `+`, `-`, `*`, ou `/`, ce que nous voulons simplement dire à l'utilisateur est... nous pouvons simplement afficher `invalid operator`.

Testons cela en l'exécutant.

L'utilisateur dit `60` ou `90` et `7`, et il va faire quelque chose comme un signe dollar `$`.

Il dit `invalid operator`.

Maintenant exécutons-le à nouveau et testons depuis le début.

Testons pour l'addition `90` et `20`. Cela devrait me donner `110`.

Maintenant testons pour la soustraction `50` et `70`. Pratiquement, cela me donne `-20`, ce qui est la bonne réponse. Testons pour la multiplication `40` et `4`.

Et ensuite nous avons la multiplication.

Maintenant il dit `160`, ce qui est correct.

Et pour la division aussi, nous avons `80`, nous avons `5`, nous avons la division, `16.0`. Maintenant tout fonctionne bien.

J'espère que vous avez compris ce que nous avons fait en construisant cette calculatrice de base.

Dans ce tutoriel, nous allons parler de `try except` en Python.

Ce que cela fait, c'est que cela empêche une erreur.

La plupart du temps, lorsque vous travaillez en Python, vous allez obtenir beaucoup d'erreurs, vous pourriez faire certaines choses et le programme va lancer une erreur ou une exception.

La plupart du temps, cette erreur arrête simplement notre programme. Si notre programme est en train d'exécuter une tâche spécifique, une fois qu'une erreur survient, le programme s'arrête.

Pour éviter cela, nous utilisons la méthode `try except`.

Cela va automatiquement détecter une erreur, puis afficher tout ce que nous voulons dire à l'utilisateur.

Par exemple, vous savez, quand nous voulons faire une addition, nous voulons que l'utilisateur saisisse un entier.

Mais disons que l'utilisateur saisit une valeur booléenne ou une chaîne de caractères ou autre chose.

Au lieu que Python lance une exception ou une erreur, nous pouvons automatiquement dire à l'utilisateur que l'entrée est invalide, que ce n'est pas une chaîne de caractères ou quelque chose comme ça.

Laissez-moi vous montrer comment faire cela en Python.

Maintenant, disons que j'ai `x = int(input('Input an integer'))`.

Et ensuite nous affichons `x`.

Quand j'exécute ceci, il demande un entier, il affiche `x`, il affiche `7`, l'entier.

Maintenant, laissez-moi l'exécuter à nouveau, et saisir une chaîne de caractères.

Maintenant vous voyez qu'il me donne une erreur nommée `ValueError: invalid literal for int()`.

Il dit donc que `hjk` n'est pas un entier.

Nous pouvons simplement détecter automatiquement cette erreur par nous-mêmes, et ensuite dire à l'utilisateur au lieu que Python lance cette exception, ce qui peut arrêter notre programme.

Pour faire cela, nous allons dire `try:`. Tout cela va être dans `try`, puis après cela, nous allons dire `except:`. Nous allons simplement afficher `value not an integer`.

Ou nous pouvons simplement afficher que quelque chose s'est mal passé parce que nous ne savons pas ce qui a pu causer l'exception, ce n'est peut-être pas parce que l'utilisateur a saisi une chaîne de caractères, cela pourrait être autre chose.

Disons simplement `Something went wrong please try again`.

Maintenant, quand j'exécute ceci, et que je saisis `Tim`. Maintenant vous voyez qu'il dit `Something went wrong please try again`, il n'a pas lancé cette erreur comme la dernière fois. Voilà comment utiliser fondamentalement `try except` en Python, mais c'est plus profond que cela, nous pouvons utiliser la méthode `except` pour certains types spécifiques d'exceptions.

Si je remonte ici, vous allez voir que cette exception qu'il nous a donnée est appelée `ValueError`.

Nous pouvons dire `except ValueError:`. Alors dites ceci.

Ce que je fais ici, c'est juste deviner s'il y a une erreur du tout. Mais soyons spécifiques. Disons s'il y a une `ValueError`.

Maintenant, s'il y a une `ValueError`, une `ValueError` signifie que l'utilisateur a saisi ce que nous ne voulions pas, nous avons demandé une chaîne de caractères et il a saisi autre chose.

Nous pouvons dire `value not an integer`.

Maintenant, quand j'exécute ceci, je saisis autre chose.

Maintenant il dit `value not an integer`. Mais il ne détecte que ce type d'erreur.

Laissez-moi essayer d'ajouter une autre erreur intentionnellement.

Disons que j'essaie de concaténer avec un nom.

Ici même, j'essaie de concaténer avec une variable nommée `name`.

Mais nous n'avions aucune variable comme celle-là auparavant.

Cela va donc me donner une `NameError`.

Quand j'exécute ceci, et que je saisis...

Maintenant vous voyez, si vous remontez, cela me montre `NameError: name is not defined`.

Et si je mets seulement `except` et que je l'exécute, cela me montre que `name` n'est pas défini.

C'est parce que nous essayons de définir quelque chose qui n'est pas... je veux dire une variable qui n'est pas là. Cette erreur vient donc de nous, nous pouvons passer quelque chose comme ça.

Mais maintenant nous essayons de passer une erreur de l'utilisateur, nous essayons de nous assurer que l'utilisateur ne saisit rien de mal.

Nous disons donc `except ValueError: value not an integer`.

J'espère que vous comprenez le concept de base de la méthode `try except` en Python.

Nous pouvons aussi faire quelque chose comme ceci : changer cela en `something went wrong`.

On peut dire `Something went wrong`.

Après avoir écrit cela, nous pouvons dire `else: print('Nothing went wrong')`.

Ce que fait ce `else`, c'est qu'après avoir exécuté ce code, s'il y a quelque chose qui s'est mal passé, il doit faire ceci.

Mais si tout s'est bien passé, alors il doit dire que rien ne s'est mal passé.

Maintenant, quand j'exécute ceci, il me demande un entier, je veux un entier.

Maintenant il affiche l'entier et il dit que rien ne s'est mal passé.

Mais si je l'exécute à nouveau, je saisis une chaîne de caractères. Maintenant il dit que quelque chose s'est mal passé, mais il n'a pas dit ceci.

Ce `else` est donc si tout est réussi, s'il n'y a pas d'erreur, alors il va dire quelque chose, rien ne s'est mal passé.

Ensuite, le dernier que je vais vous montrer est appelé `finally`. C'est aussi un mot-clé.

Cela va s'exécuter qu'il y ait une erreur ou non.

Je peux donc dire `try except finished`.

Qu'il y ait une erreur ou non, cela va afficher... s'il n'y a pas d'erreur, il affiche `7` et dit que le `try` est fini.

Si je l'exécute à nouveau, et que j'affiche une chaîne de caractères. Il dit que quelque chose s'est mal passé, ce qui est ceci, et il dit `try except finished`.

C'est juste pour dire qu'après tout, qu'il y ait un problème ou non, affichez simplement que le `try except` est fini.

Maintenant je veux parler de la lecture de fichiers en Python.

Parfois, lorsque vous codez avec Python, vous pourriez vouloir travailler avec certains fichiers externes, disons comme un document texte, ou comme une feuille de calcul, comme un tableur Excel, ou comme un fichier HTML ou tout autre fichier externe.

Vous voulez donc savoir comment lire et écrire dans ce fichier.

Mettons cela en pratique.

Tout d'abord, créons un nouveau fichier ici même.

Et nommons-le quelque chose comme... sauvegardons ceci, et ensuite je vais le sauvegarder au même endroit où j'ai sauvegardé ceux-là.

Laissez-moi dire "All files" là, je suis sûr qu'il est situé ici.

Tout d'abord, annulons cela et assurons-nous que nous savons où cela est sauvegardé.

Oui, si je viens ici, oui. Je vois où il est sauvegardé.

D'accord, ici même.

Maintenant je peux créer un nouveau fichier et ensuite le sauvegarder.

Ici même, je peux le sauvegarder sous le nom `countries.txt`.

Vous voyez, c'est déjà sur le `.txt`, je peux simplement le changer en "All files".

Dans ces pays, je veux avoir juste une liste de pays au hasard.

Je peux dire `Ghana`.

Je peux dire `Mexico`.

Je peux dire `Morocco`.

Laissez-moi dire `Spain`.

Je n'ai pas de fautes d'orthographe là. `Ghana`, `Mexico`, `Spain`.

Oui, je pense que c'est bon. Donnez-m'en un de plus, disons `France`.

Je pense que c'est bon.

Pour que nous lisions ce fichier, nous devons l'importer dans notre fichier Python.

C'est très facile à faire, ce que nous devons faire est de dire `open('countries.txt')`.

Nous devons nous assurer que ce `countries.txt` est dans le même dossier que cet `app.py` afin que nous puissions facilement y naviguer.

Et ensuite, après avoir dit cela, le deuxième paramètre que cela va prendre est `r`.

Ce que ce `r` signifie, c'est que nous voulons lire ce fichier.

Nous voulons seulement lire ce fichier, nous ne voulons rien y modifier.

Il y a aussi quelque chose comme `w`. Ce `w` signifie que nous voulons écrire dans ce fichier, nous voulons modifier ce fichier.

Et nous avons aussi `a`. Ce `a` signifie que nous voulons ajouter au fichier, nous pouvons donc ajouter au milieu du fichier ou modifier le fichier ou faire des changements, nous voulons simplement ajouter à la fin du fichier.

Et nous en avons un de plus appelé `r+`. Cela signifie que nous voulons faire à la fois la lecture et l'écriture.

Cela nous donne une capacité complète.

C'est à cela que sert le `r+`.

Mais pour cette partie, nous allons travailler uniquement avec `r`. Nous ouvrons donc ce fichier.

Et la plupart du temps, nous voulons toujours le sauvegarder dans une variable.

Nommons simplement une variable `country_file`.

Et elle devrait être égale à ceci.

Si nous affichons... et chaque fois que nous ouvrons un fichier, nous devons toujours nous assurer de fermer le fichier.

Ici même, nous pouvons aussi dire `country_file.close()`.

C'est pour s'assurer que nous fermons le fichier.

Et entre ceux-là, nous pouvons faire tout ce que nous voulons avec le fichier.

Maintenant, je peux simplement afficher `country_file`.

Tout d'abord, je veux vérifier si ce fichier est lisible, si j'ai accès pour le lire.

Je vais donc simplement dire `country_file.readable()`.

Cela va simplement retourner une valeur booléenne vraie ou fausse.

Exécutons cela.

Il dit `no such file in directory: countries.txt`.

Assurons-nous.

Ce que nous allons faire, c'est naviguer dans ce dossier, et nous assurer de créer cela.

Allons-y.

Je pense que je l'ai ici même.

C'est donc dans... d'accord.

Et ensuite Django.

Donc je pense que je serai ici même.

Et puis il y a `countries.txt`, `C O U N T R I E S`.

Il dit que nous ne pouvons pas ouvrir. Il dit `no such file or directory`.

Ce que nous devons faire, c'est faire quelque chose comme ça.

Ceci, bien que ce ne soit pas la raison pour laquelle nous avons cette erreur.

Quand nous l'exécutons, cela nous donne cette erreur.

La meilleure chose à faire est de prendre le répertoire principal de cela et de le coller ici avec ce slash comme ceci.

Maintenant essayons de l'exécuter à nouveau.

Maintenant vous voyez qu'il nous donne cette erreur.

La raison de cette erreur est ce slash ici même, nous allons donc simplement le changer en slash, le slash vers l'avant ici aussi.

Et ensuite quand nous l'exécutons à nouveau, maintenant vous voyez qu'il dit `True`.

La raison pour laquelle nous avons eu l'erreur est parce qu'ici nous utilisions un backslash, mais quand nous l'utilisons en Python, il doit être dans un slash vers l'avant.

Maintenant nous naviguons avec succès vers ce `countries.txt`.

Quand nous disons `print(country_file.readable())`. Nous demandons : avons-nous accès pour lire ce fichier ? Il dit `True`.

Puisque nous avons accès, nous pouvons le lire, cela va nous dire `True`. Maintenant que c'est `True`, je pense que nous sommes prêts à partir.

Maintenant que nous pouvons lire ce fichier, ce que nous voulons faire est d'afficher quelque chose comme... nous pouvons dire `country_file.readline()`.

Maintenant, quand je dis ce `readline`, cela va afficher la première ligne de ce fichier, qui est `Ghana`.

Une fois que j'affiche cela, vous voyez maintenant qu'il affiche `Ghana`, et c'est comme une séquence.

Si j'affiche ce fichier à nouveau, si je dis `print` et que je dis `country_file.readline()` à nouveau. Maintenant qu'est-ce qu'il va apporter ? La deuxième ligne.

Et notez que je n'ai fait aucun changement au même code, mais quand je l'exécute, il affiche `Ghana`, et la deuxième fois il affiche `Mexico`. Nous pouvons aussi simplement afficher tout ce que j'ai dans le fichier, mais la manière la plus recommandée est de dire simplement `country_file.readlines()`. Maintenant `readlines` va tout afficher pour vous dans une liste, il va afficher toutes les lignes de votre fichier, puis les stocker dans une liste.

Maintenant nous pouvons simplement obtenir, disons, la première. Disons que nous voulons obtenir la première.

Nous avons `Ghana`.

La dernière.

Maintenant vous voyez que nous avons `France`. Voilà comment utiliser la fonction `readlines`.

Et ensuite nous pouvons aussi le rendre plus cool en bouclant à travers cela.

Nous pouvons donc dire `for`, changeons cela en une boucle `for`, `for lines in country_file.readlines():`. Alors nous voulons afficher `lines`.

Maintenant, quand je l'exécute, vous voyez qu'il affiche simplement toutes les lignes que j'ai.

La meilleure façon d'appeler cela est `lines`, pas `fells`.

Donc `lines`.

Quand je l'exécute à nouveau, même chose, il affiche simplement toutes les lignes que j'ai. Si je venais ici et faisais un changement, comme dire `Ghana is a country in Africa`.

Quand je l'exécute, ce changement est automatiquement fait.

Vous voyez ici même, la première ligne dit `Ghana is a country in Africa`.

J'espère que vous comprenez le concept de lecture de fichiers en Python. Voilà comment vous pouvez lire des fichiers ligne par ligne, par texte et des choses comme ça.

Passons maintenant directement à la partie suivante de ce tutoriel.

Dans cette partie, nous allons parler de l'écriture de fichiers en Python.

Dans la dernière partie, nous avons parlé de l'ouverture ou de la lecture de fichiers externes en Python, mais dans cette partie, nous allons parler de l'ajout de texte au fichier, ou de l'écriture de tout le fichier à nouveau.

Tout d'abord, pour écrire un fichier, ici même, nous devons changer ce `r` en `w`.

Maintenant, quand nous changeons ce `r` en `w`, enlevons simplement tout cela, puis nous pouvons simplement dire `country_file.write()`.

Et ensuite ce que vous voulez faire est de simplement écrire le fichier.

Vous pouvez voir que c'est le fichier, mais si je saisis quelque chose, vous savez, comme `this is the new text`.

Maintenant, quand j'exécute ceci, vous verrez que rien ne se passe dans le terminal, mais quand je viens ici, vous voyez que cela a été changé.

Tout ce qui était là est parti. Nous avons donc réécrit tout le fichier.

Cela peut être utile. Disons que vous voulez écrire un nouveau fichier.

C'est très utile.

La raison pour laquelle il a tout réécrit était parce que c'était un fichier existant. Il a donc écrasé ce qui s'y trouvait.

Mais c'est principalement utilisé pour créer un nouveau fichier.

Disons que nous voulons avoir `country`.

Maintenant laissez-moi dire `this is the new country`.

Une fois que je le sauvegarde et que je l'exécute, si je viens dans ce répertoire ici même dans ma commande.

Je vais faire `cd` entrer dans le répertoire.

Cela ne va pas dans ce répertoire.

Mais ce que cela fait, c'est qu'il a créé ce nouveau fichier appelé `country.txt` dans ce répertoire, alors allons-y normalement.

Ici même, vous voyez que nous avons un nouveau fichier appelé `country`, changeons-le et disons simplement `new_file`.

Quand je l'exécute, vous voyez que rien ne se passe, mais ici même, `new_file` est créé.

C'était tout pour créer un nouveau fichier et y écrire automatiquement quelque chose.

Revenons donc en arrière avec Ctrl+Z aux pays que nous utilisions.

Maintenant, j'ai ce fichier de pays, disons que je veux ajouter quelque chose en bas comme un nouveau texte, ce que je peux faire est quelque chose comme... pour ajouter, je dois m'assurer de changer ce `w` en `a`.

Et ensuite ici même, ce que je vais faire est de dire simplement `file.write()`, puis `this is a new line`.

Quand j'exécute ceci, rien ne se passe dans le terminal, mais quand je viens ici, il a ajouté `this is a new line` à celui-ci.

Mais vous pouvez voir qu'il les joint ensemble.

Voyons comment former une nouvelle ligne, je veux que ce soit la ligne deux, je peux juste venir ici.

Et je peux dire `\n`.

Cela va automatiquement vous amener sur une nouvelle ligne, quand je l'exécute à nouveau, et que je viens ici, vous devriez maintenant savoir que c'est sur une nouvelle ligne.

C'est fondamentalement comment ajouter en Python.

Vous pouvez le faire pour divers types d'extensions de fichiers.

Comme vous le savez, nous l'avons fait pour le document texte, qui est `.txt`, vous pouvez même utiliser un fichier Python pour ouvrir un nouveau fichier Python.

Mettons cela en action.

Disons que nous voulons ouvrir un nouveau fichier et le nommer `new.py`.

Et ensuite dans ce `new.py`, je veux écrire et nous allons lui permettre d'y écrire.

Ici même, laissez-moi simplement écrire un code Python simple, je peux dire `print('This is a new file')`.

Ici même, j'ai juste écrit un code Python simple.

Et ensuite, évidemment, nous devons utiliser le backslash avant de pouvoir écrire un code.

J'ai donc utilisé ce `print('This is a new file')`, et cela va être dans ce `new.py`.

Maintenant, quand j'exécute ceci, vous verrez maintenant que nous avons un fichier `new.py`.

Et ensuite je peux juste... quand je viens ici, je peux exécuter `new.py`, vous voyez maintenant qu'il affiche simplement `This is a new file`, qui était la commande ou la ligne que nous y avons mise.

C'est aussi très important et très utile d'écrire de nouveaux fichiers en Python.

Maintenant, nous allons parler des classes et des objets en Python.

Je dois dire que Python est un langage de programmation orienté objet.

Cela signifie que tout ce qui traite des classes, des objets et des choses comme ça, est classé comme orienté objet.

Les classes sont juste comme une fonctionnalité en Python, disons quelque chose comme une fonction.

Une fonction est une fonctionnalité que Python possède, les classes sont aussi une fonctionnalité de Python, mais les classes sont maintenant comme un constructeur d'objets.

Vous ne comprenez peut-être pas ce que je dis maintenant, mais quand je vous montrerai le code, je suis sûr que vous comprendrez plus facilement.

Une classe est comme un constructeur de différents objets sous la classe, nous avons divers objets.

Allons-y et montrons comment faire une classe.

Pour faire une classe, nous allons simplement dire `class` en utilisant le mot-clé `class`, puis nous pouvons dire `MyClass`.

Et ensuite ici, nous pouvons dire `x = 5`.

Maintenant nous avons cette classe.

C'est la classe, le nom de la classe est `MyClass`.

Et ensuite nous avons un `x`, qui est un objet sous cette `MyClass` et `x = 5`.

Maintenant, disons que nous voulons créer un objet en utilisant cette classe, ce que nous allons faire est de faire quelque chose comme `p1`.

Égal à `MyClass`.

Ensuite nous l'initialisons, puis nous affichons `p1.x`.

Cela va afficher `5`, parce que nous disons que `p1` est égal à `MyClass`, qui est cette classe, puis nous disons simplement `print(p1.x)`. Une fois que j'exécute ceci, il affiche `5`.

Voilà comment afficher fondamentalement cela.

Parlons maintenant de la fonction `__init__`.

Tout ce que je viens de dire maintenant, ce sont les concepts de base de la classe où nous pouvons fondamentalement les utiliser dans la vie réelle, disons dans des choses du monde réel et des projets du monde réel.

Mais la fonction `__init__` nous permet d'initialiser différentes valeurs dans notre classe.

Par exemple, nous avons cette classe, disons que cette classe est nommée `Person`.

Et ensuite sous cette classe, nous allons avoir une fonction.

Elle va prendre deux underscores `init` comme ça, puis elle va avoir des paramètres `self`.

Ce `self` va être là, il est juste là. C'est comme ça que c'est.

Et ensuite, disons qu'elle a `name`, que nous allons mettre, disons, son `age`.

Et ensuite.

Nous mettons nos deux points juste comme une fonction normale.

Enlevons ceux-là.

Et ensuite pour déterminer le nom de ce `self.name`, cela peut être égal à `name`.

Et ensuite nous allons faire la même chose pour l'âge. Donc `self.age = age`, juste comme ça.

Et ensuite initialisons-le comme nous l'avons fait ici.

Donc `p1 = Person()`.

Mais maintenant nous devons lui donner ce nom et cet âge.

Nous dirons donc que le nom est `John`.

Et ensuite l'âge est `87`.

Maintenant, une fois que nous affichons `p1.name`.

Vous verrez que cela nous donne `John`.

D'accord, donc il dit erreur d'indentation. Tout cela sous cette fonction est censé être indenté.

Exécutons cela à nouveau.

Maintenant vous voyez qu'il a affiché `John`, nous pouvons aussi afficher `p1.age`.

Et nous voulons voir qu'il affiche `87`.

Rendons cela possible pour l'utilisateur de saisir.

On peut dire `name = input('Enter your name')`.

Et on peut dire `age = input('Enter your age')`.

Et ensuite une fois que nous avons le nom et l'âge de l'utilisateur sauvegardés, nous pouvons simplement les remplacer par ceux-là comme `name` et `age`.

Maintenant, quand nous exécutons ceci, tout d'abord, il nous demande un nom, j'ai dit `Tim`, il demande l'âge, et il affiche simplement `Tim` et `9`.

Nous pouvons aussi utiliser une classe pour faire quelque chose comme ça.

Les classes sont très vastes en Python, et elles sont très, très utilisées en Python.

Mais il y a encore d'autres propriétés d'objets que nous pouvons faire, disons que nous voulons supprimer une propriété de ceux-là, je peux supprimer cet âge.

Enlevons simplement ceux-là, et donnons-lui le nom `John`.

Maintenant, disons que nous voulons supprimer son âge, ce que nous pouvons faire est de dire simplement `del p1.age`.

Maintenant, une fois que nous supprimons `p1.age`, cela ne va plus avoir cet âge dedans.

Et ensuite nous pouvons même supprimer ces objets au total en disant simplement `del p1`. Une fois que nous exécutons ceci, cela va être supprimé. Si nous essayons d'afficher `p1` après cela, cela ne fonctionnera pas.

Il dit que le nom n'est pas défini, c'est parce que nous avons déjà supprimé `p1`, il n'y a rien de tel.

Et ensuite nous avons aussi une fonctionnalité que nous pouvons utiliser dans la classe.

Ici même, disons que nous avons une classe qui est nommée `Person`.

Et pour l'instant, nous ne savons pas quoi y mettre. Nous ne connaissons pas les valeurs, et nous voulons juste continuer à coder.

Nous pouvons donc coder `pass`. Ce `pass` nous permet de contourner toute erreur.

Si nous avons cette classe qui est vide, nous pouvons simplement mettre `pass` pour l'instant, puis revenir plus tard ajouter des attributs.

Une fois que je mets `pass`, et que j'exécute, cela ne va pas poser de problème.

Mais si je mets seulement `class Person` et que j'exécute, vous voyez que cela va me donner une erreur.

Ce `pass` sert donc juste à contourner l'erreur, afin que nous puissions continuer avec notre code pour le moment.

J'espère que vous comprenez le concept de classe et d'objets en Python.

Maintenant, nous allons parler de l'héritage en Python.

L'héritage signifie simplement prendre d'une classe existante, puis récupérer toutes les méthodes et tout ce qui s'y trouve et les mettre dans une nouvelle classe.

Vous allez comprendre ce que je veux dire dans un instant.

Disons que nous avons une classe existante dans ce fichier nommé `new.py`, j'ai juste créé ce fichier que nous avons en fait créé plus tôt dans cette vidéo, ayons une classe nommée `Student`.

Et ensuite, disons que `name = 'Tim'`, `age = 34`.

Et disons que `gender = 'male'`.

Maintenant nous avons cette classe ici, nous pouvons facilement l'importer en disant... nous pouvons dire `from new import Student`, qui est ceci ici même.

Nous importons donc `Student`.

Au lieu de dire `from new.py`, nous pouvons simplement dire `from new` sans ajouter `.py`, l'extension, il comprend automatiquement que nous importons de ce fichier.

Mais avant de pouvoir importer, nous devons nous assurer que ce `new` et `app.py` sont dans le même répertoire.

Laissez-moi simplement annuler cela, nous devons nous assurer qu'ils sont dans le même répertoire.

Maintenant j'ai cette nouvelle classe nommée `Person`, ce que je veux faire est juste de voir cet `Student`.

Je récupère donc tout de cette classe `Student` dont nous avons hérité, je le mets simplement dans cette classe `Person`.

J'ai juste mis `pass` pour éviter toute erreur.

Maintenant je peux dire `p1 = Person()`.

Et je peux maintenant dire `p1.name`, je peux simplement dire `print(p1.name)`.

Maintenant, quand j'exécute ceci, vous voyez qu'il affiche `Tim`, tout le chemin depuis `new.py`.

Alors qu'il exécute `app.py`.

C'est le concept de base de l'héritage en Python. Il hérite de chaque chose que nous avons dans cette classe. Et il l'apporte juste dans cette classe.

C'est donc comme un duplicata de cette classe, mais ce n'est pas un duplicata parce que ce sont des noms différents dans des fichiers différents.

Cela s'appelle donc l'héritage en Python.

Dans ce tutoriel, je vais vous parler de l'interpréteur Python ou du shell Python.

Le shell Python est une application qui est automatiquement installée chaque fois que vous installez Python sur votre ordinateur.

Laissez-moi ouvrir rapidement mon shell Python.

Voici mon shell Python ici même.

Comme vous pouvez le voir, IDLE.

Laissez-moi vous montrer comment j'ai ouvert cela, vous pouvez simplement venir ici et chercher `IDLE`. Si vous avez Python installé, cela devrait le faire sortir automatiquement et appuyez simplement sur ouvrir.

Mais puisque j'ai déjà cela ouvert, le shell Python est juste comme un environnement plus petit où je peux exécuter et tester rapidement du code Python.

Comme tout ce que nous avons appris dans ce tutoriel, je peux facilement les coder ici, comme, laissez-moi dire `print('You enjoying this tutorial')`.

Une fois que j'appuie sur Entrée, vous voyez qu'il affiche cela immédiatement, il exécute automatiquement ce code.

Dès que j'appuie sur Entrée.

Et nous pouvons aussi dire comme une variable, disons `name = 'Tim'`.

Et ensuite nous pouvons maintenant afficher `name`.

Ici même, dans l'interpréteur Python, nous pouvons aussi afficher le nom sans même écrire `print`.

Si vous dites simplement `name`, il l'affiche automatiquement.

C'est seulement quand vous testez votre code ici dans votre shell Python que vous pouvez faire cela. Vous ne pouvez pas faire cela dans votre éditeur principal.

Maintenant nous pouvons faire beaucoup de choses comme je suis sûr que nous pouvons utiliser une boucle `for`.

Disons `for letter in 'Tim':`.

Alors je peux simplement dire `print(letter)`.

Maintenant vous voyez qu'il affiche automatiquement `Tim`, je peux faire n'importe quoi ici, je peux même écrire une classe.

Et je peux dire la classe `Person`.

Et ensuite je peux dire `name = 'John'`.

Et ensuite ici je peux dire `p1 = Person()`.

Et ensuite je peux dire `p1.name`.

Cela va simplement m'afficher `John`.

Je peux fondamentalement faire tout ce que je fais dans l'éditeur de code ici même.

Je peux avoir une instruction `if`.

Disons si `p1.name == 'John'`, alors affichez `Yes it is`.

Maintenant il va afficher `Yes it is` parce que `p1.name` est évidemment égal à `John`.

Et ensuite nous effectuons aussi notre arithmétique de base, comme `2 + 3` nous donne `5`, `9 - 0` nous donne `9`.

Et tout ce que nous pouvons faire à l'endroit normal.

Parce que nous allons définir une fonction, disons que nous avons une fonction pour dire `Hi`, et ensuite laissons-la passer un nom.

Et laissons le nom être `name`.

Et disons `print('Hi ' + name)`.

Maintenant disons `Hi('John')`.

Maintenant vous voyez qu'il dit `Hi John`.

Presque tout ce que nous pouvons faire ici, nous pouvons aussi le faire dans notre éditeur principal, c'est comme la même chose mais il n'est pas conseillé d'utiliser cela lors de la construction de projets normaux ou de choses comme ça.

C'est juste fondamentalement pour tester ou n'importe quoi de ce genre.

Essayons aussi d'autres choses comme `try except`.

Donc `try`, disons que `age` devrait être égal à l'une des entrées de `enter age` sous ce...

Ici, nous devons nous assurer d'avoir la bonne indentation.

Donc `except`, cela nous donne une erreur à cause de l'interprétation.

Mais nous pouvons fondamentalement faire tout cela ici même dans notre Python IDLE, c'est ce que je veux vous montrer.

Parfois, vous pourriez rencontrer cette erreur de syntaxe d'indentation.

Parce que l'indentation n'est pas vraiment claire.

Tout comme la façon dont elle est ici même dans Visual Studio Code.

C'est pourquoi il est recommandé d'utiliser votre éditeur normal et non fondamentalement un IDLE pour l'édition, mais j'espère que vous avez compris le concept d'un shell Python. Voilà pour l'interpréteur Python.

Maintenant, nous allons créer un système simple d'inscription et de connexion en Python.

Nous allons mettre en œuvre tout ce que nous avons appris dans ce tutoriel, puis construire ce programme simple.

Comme vous pouvez le voir ici, il est écrit `Create your account`.

Maintenant, il demande de saisir le nom d'utilisateur, je vais simplement saisir `admin`, et il dit que nous devrions saisir le mot de passe.

Je vais saisir `admin`.

Comme mot de passe, maintenant il dit `User admin created successfully login now`.

Ce que fait ce programme, c'est qu'il crée cet utilisateur, évidemment nous n'utilisons pas de base de données réelle, nous stockons simplement cela dans une variable.

Une fois que nous exécutons ce programme à nouveau, nous devons le créer à nouveau.

C'est juste pour la pratique.

Une fois que nous créons un compte, et qu'il dit que l'utilisateur a été créé avec succès, il dit `login now`.

Maintenant, quand nous essayons de nous connecter, si ce que nous tapons est le même que cela, alors automatiquement nous serons connectés. Si c'est différent, si notre nom d'utilisateur est faux ou le mot de passe est faux, alors il dira simplement `invalid credentials`.

Laissez-moi essayer de me connecter normalement.

Et je dis `admin`. Maintenant il dit `user logged in successfully`.

Exécutons cela à nouveau. Laissez-moi maintenant en créer un autre `admin`, encore `admin`.

Maintenant il dit `admin created` et veut que je me connecte.

Si je dis maintenant `admin`, par le mot de passe, et que j'ajoute un `n`, je clique sur Entrée.

Vous voyez maintenant qu'il dit `invalid credentials`.

Ce programme Python que nous allons construire va détecter si le mot de passe est correct, ou si le nom d'utilisateur est correct ou non.

Passons directement à cela.

Quittons simplement ceci. Revenons ici.

Nous pouvons aussi quitter ceci.

Ce que nous voulons faire, c'est prendre quatre paramètres.

Le premier va être le nom d'utilisateur et le mot de passe pour la création du compte.

Et le deuxième et le troisième, et le quatrième vont être le nom d'utilisateur et le mot de passe pour la connexion.

Faisons cela. Disons que `username` sera égal à... c'est donc le premier nom d'utilisateur pour la création du compte.

Égal à notre entrée, et nous dirons `Enter username`.

Et pour le mot de passe, disons la même chose `input('Enter password')`.

Et une fois que les utilisateurs ont saisi le nom d'utilisateur et le mot de passe, nous pouvons simplement afficher à l'utilisateur et dire simplement que votre compte a été créé avec succès.

Et maintenant nous savons comment dire à l'utilisateur de se connecter.

Affichons à nouveau `login now`.

Maintenant, une fois que nous avons une autre variable, qui est `username2`, elle devrait être égale à l'entrée `Enter username`.

Et le mot de passe pour la connexion. `password2 = input('Enter password')`.

Maintenant nous savons que nous vérifions si ceci est égal à cela.

Disons simplement `if username == username2 and password == password2:`.

C'est notre instruction `if` disant que ceci et cela doivent être équivalents.

C'est pourquoi nous utilisons `and`. Si nous utilisons `or`, cela va être faux, parce que si le nom d'utilisateur est correct, et que le mot de passe est faux, il va toujours nous laisser entrer. Nous voulons donc nous assurer que les deux sont corrects.

Deux réponses correctes avant de nous connecter.

Une fois que c'est correct, nous pouvons simplement dire `print('logged in successfully')`.

Mais si c'est faux, `else`.

Nous voulons simplement afficher `invalid credentials` comme ceci.

Venons juste en haut ici et affichons quelque chose comme `Create account now`.

Maintenant cela devrait fonctionner, exécutons-le.

Nous créons un nom d'utilisateur, disons simplement `Tomi`, le mot de passe disons `Tomi`.

Maintenant votre compte a été créé avec succès, connectez-vous maintenant. `Tomi` et le mot de passe `Tomi`.

Maintenant il dit `login successfully`.

Exécutons-le à nouveau et essayons un faux. `hai hai hai, hai hai hai`.

Maintenant, quand je dis que le nom d'utilisateur est `ah ah ah ah ah y`.

Mais le mot de passe est `Ui Ui Ui`.

Maintenant, vous voyez, il dit `invalid credentials`. Voilà comment construire ce programme Python de base en utilisant la récupération des entrées utilisateur et les instructions `if`.

J'espère que vous avez compris ce que nous avons fait ici. Si ce n'est pas le cas, vous pouvez revenir en arrière d'environ cinq minutes, et regarder à partir de là, je suis sûr que vous allez comprendre.

Dans ce tutoriel, nous allons parler des modules en Python.

Les modules vous permettent essentiellement d'obtenir la fonction, la classe ou tout ce qui est présent dans un autre fichier, cela vous permet de mettre en œuvre et d'utiliser ces mêmes fonctions dans votre propre fichier ou projet.

Les modules sont donc très, très polyvalents, ils sont très largement utilisés en Python. Tout le monde utilise des modules.

Disons que j'ai ce fichier nommé `new.py`.

J'ai une fonction nommée `say_hi`.

Et cette fonction `say_hi`, je veux juste qu'elle affiche `Hi now`.

Mais cette fonction ici, je peux l'importer, je vais simplement dire `import new`.

Ce `new` sert de module pour ce mon fichier.

Maintenant, ici, je peux simplement dire `new.say_hi()`.

Une fois que je vois cela, j'exécute ce fichier, vous voyez qu'il dit automatiquement `Hi`. Voilà comment utiliser les modules en Python.

Il y a beaucoup de choses que nous pouvons faire avec les modules.

Et les modules sont très polyvalents.

Si vous voulez, disons que vous vouliez utiliser une fonction qui dit... au lieu de coder à partir de zéro, il est possible que quelqu'un d'autre ait déjà écrit cette même fonction, ou quelque chose de similaire à ce que vous voulez faire.

Et vous pouvez l'obtenir sous forme de module ou de bibliothèque, que vous pouvez obtenir et mettre en œuvre.

Les modules ne sont pas seulement sur votre ordinateur portable local ou votre PC local comme celui-ci, les modules sont hébergés en ligne.

Python possède quelque chose que nous appelons PIP, dont je vais parler davantage dans la prochaine vidéo, la prochaine partie.

Tous les modules sont hébergés en ligne.

Disons que vous cherchez un module qui vous permette de faire une tâche spécifique.

Et vous savez que oui, bien sûr, quelqu'un d'autre l'aurait fait, alors vous pouvez aller chercher ce module, ou faire des recherches là-bas, vous allez voir ce module en ligne.

Dans la partie suivante, je vais vous montrer comment mettre en œuvre PIP et ensuite installer toutes ces sortes de modules sur votre ordinateur.

Dans cette partie, je vais vous présenter quelque chose appelé PIP.

PIP est utilisé pour installer des modules externes du web sur votre PC local.

Comme je l'ai expliqué dans la dernière vidéo sur les modules, ils vous permettent essentiellement d'obtenir des fonctions d'un autre fichier ou d'une autre bibliothèque.

PIP vous permet donc d'installer un module d'Internet sur votre ordinateur.

Si nous allons en ligne, et que nous cherchons simplement quelque chose comme "Python modules", alors nous pouvons simplement aller voir...

Allons sur PyPI.

C'est un site appelé PyPI.

C'est là que presque tous les modules Python sont hébergés.

Comme vous pouvez le voir, 200 000 projets.

Il dit donc fondamentalement 200 000 bibliothèques ou modules qui sont hébergés sur ce site.

Maintenant vous pouvez voir que chacun a des tâches différentes qu'il accomplit.

Voyez ce module est pour la recommandation Spotify.

Disons... cherchons un module comme...

Allons à la page d'accueil.

Et voyons ce que nous voulons.

Vous pouvez aussi voir les produits tendance.

Des modules tendance, beaucoup de choses différentes.

Et disons, allons dans "Browse development framework".

Cliquons simplement sur ceci.

C'est le nom d'un module.

Laissez-moi en chercher un qui a une description.

"Django deep serializer".

Django est en fait un framework web qui vous permet de construire des sites web en utilisant Python.

Celui-ci dit donc un "Django deep serializer".

C'est ce que fait ce module particulier.

Pendant que nous l'étudions sur notre ordinateur, nous tapons simplement `pip install django-deep-serializer`.

De la façon dont c'est dit ici, alors comment... où exécutons-nous cette commande ? Si vous êtes sur un Mac, ouvrez votre terminal, si vous êtes sur Windows, ouvrez votre invite de commande, et tapez simplement `pip install django-deep-serializer`.

Si c'est la bibliothèque ou le module que vous voulez utiliser, vous pouvez simplement exécuter cette ligne de commande, et c'est parti, j'ai installé ce module ou cette bibliothèque sur votre ordinateur local.

Maintenant vous pouvez voir qu'il dit "collecting django-deep-serializer", puis "downloading django-deep-serializer 0.1.3" et tout cela.

Il configure tout cela.

Oui, vous voyez qu'il dit "successfully installed django-deep-serializer".

Maintenant j'ai ceci sur mon ordinateur.

Maintenant, je suis sûr que si je veux importer cela, je vais juste chercher comment l'importer.

D'accord, ils n'ont pas mentionné cela ici parce que nous n'exécutons pas de projet Django.

Vous n'avez donc pas besoin de comprendre ce que je dis pour l'instant sur Django.

Mais c'est ainsi qu'on installe fondamentalement un module ou une bibliothèque en utilisant PIP sur votre ordinateur local, c'est ce qu'est fondamentalement PIP.

Ce PIP, vous n'avez pas besoin de le télécharger de l'extérieur, une fois que vous installez Python, il s'installe automatiquement avec lui.

C'est pourquoi une fois que vous installez votre Python, c'est bien s'ils demandent si vous voulez installer des composants, il est bon de tout cocher.

Et d'ajouter Python au PATH, cochez tout.

Ainsi, tous ces composants seront installés quand vous voudrez les utiliser plus tard.

PIP est donc automatiquement installé avec Python.

Si je viens ici, nous cherchons PIP.

Vous voyez, il dit... laissez-moi dire Python, laissez-moi être spécifique.

PIP Python est un système de gestion de paquets écrit en Python utilisé pour installer et gérer des paquets logiciels.

Comme je l'ai dit, PIP est utilisé pour télécharger, ou dans ce cas, installer des paquets.

Les modules sont aussi ce que nous appelons des paquets.

PIP est donc le gestionnaire, c'est ce qui le télécharge et le stocke sur votre ordinateur.

C'est le concept de base que vous devez comprendre à propos de PIP.

Les gars, ce sera tout pour ce tutoriel. J'espère que vous avez appris quelque chose et que vous avez apprécié la vidéo.

Bienvenue au cours accéléré de Django.

Le but principal de cette vidéo est de vous présenter Django et de vous montrer tous les concepts dont vous avez besoin pour commencer à construire votre propre projet en utilisant Django.

Dans ce tutoriel, nous n'allons pas construire de projet complet, mais nous allons prendre chaque concept de Django étape par étape, en l'utilisant dans un cas pratique.

Et à la fin de cette vidéo, vous saurez comment construire vos propres projets en utilisant Django.

Ce tutoriel est principalement axé sur les débutants, car nous allons commencer par les bases jusqu'aux choses les plus complexes de Django.

Une introduction rapide à Django.

Django est un framework web Python. Cela signifie qu'en utilisant Python, nous pouvons construire des applications web avec Django.

Sans perdre de temps, passons directement à cette vidéo, voici une liste de ce que nous allons couvrir dans cette vidéo.

Passons directement à l'introduction et à l'installation de Django.

La première chose que nous devons faire est d'installer et de configurer Django sur notre ordinateur.

Je suis sur Windows. Si vous êtes sur un Mac ou sur un Linux, le processus d'installation est assez similaire, avec seulement quelques différences dans la ligne de commande.

Mais je vais aussi dire ce que vous devez faire si vous êtes sur un OS différent du mien.

C'est juste le site officiel de Django.

Mais avant de devoir installer Django, vous devez avoir Python installé sur votre ordinateur, car nous allons utiliser un gestionnaire de paquets Python appelé PIP.

Et cela ne vient que lorsque vous avez Python installé.

Et Django est un framework Python, alors pourquoi pas.

Si vous n'avez pas Python installé, allez sur Google.

Et ensuite c'est très facile, vous pouvez simplement chercher "Python download", puis cliquer sur le premier site web.

Oui, vous allez voir la dernière version ici, et vous pouvez facilement cliquer dessus pour la télécharger.

Quand vous la téléchargez, vous allez l'installer comme une application normale.

Je ne vais pas faire cela, car je l'ai déjà installée sur mon propre ordinateur portable.

Si vous n'avez pas cela installé, venez ici, téléchargez-le, et tout ira bien.

Maintenant, nous pouvons quitter cet onglet.

Maintenant que nous avons Python installé sur notre ordinateur. Ce que nous devons faire ensuite est d'ouvrir notre invite de commande.

C'est notre invite de commande, c'est là que nous allons faire la plupart des exécutions de serveur, des installations et tout ce que nous devons faire dans notre projet Django.

La première chose que nous voulons faire est d'installer Django, c'est très facile, ce que nous devons taper est `pip install django`.

Cette ligne de commande va installer Django sur notre ordinateur, elle va installer Django sur le système, afin que nous puissions y accéder de n'importe où.

Mais j'ai déjà Django installé. Ce qu'il va me dire, c'est "requirement already satisfied".

Si vous travaillez beaucoup avec Python, vous savez qu'une fois que vous avez un module Python, ou une bibliothèque ou un paquet installé, il va vous dire "requirement already satisfied".

Comme vous pouvez le voir, il dit "requirement already satisfied".

Je vais donc fermer cela, et le laisser comme ça.

Maintenant, vous pouvez voir que nous avons Django installé sur notre ordinateur.

Et la version qu'il va installer est la dernière version.

Je ne suis pas vraiment sûr si c'est la 3.2 ou la 3.1. Je sais que nous sommes sur Django 3 en ce moment.

Et c'est ce qu'il va installer, la dernière version.

Mais disons que pour un projet différent, pour chaque projet Django, vous voulez avoir des paquets particuliers juste pour ce projet, pas pour tout votre ordinateur.

Je veux aussi avoir une version différente de Django juste pour une raison spécifique sur chaque projet.

Maintenant, ce que nous devons faire est de créer un environnement virtuel (virtual environment). L'environnement virtuel est comme une petite boîte où tout ce qui concerne votre projet est stocké.

C'est donc juste comme un mini environnement où vous pouvez accéder à tout ce qui concerne votre projet.

La version de Django de ce projet particulier est différente, quelle que soit la version que vous utilisez pour tout autre paquet installé peut être différente.

C'est donc juste pour ce projet particulier, cela ne va pas être disponible dans tout l'ordinateur.

Pour faire cela, vous devez tout d'abord installer un environnement virtuel sur votre ordinateur.

Il y a plusieurs environnements virtuels que vous pouvez avoir. Celui que j'utilise et que je recommande s'appelle Anaconda.

Mais cela a aussi son processus d'installation.

Et cela est principalement utilisé dans le machine learning à cause des paquets qui viennent avec.

Mais pour ce projet, nous allons nous en tenir à un environnement virtuel très simple.

Et cet environnement virtuel est très facile. Nous allons simplement l'installer sur notre ligne de commande ici même.

Mais si c'était Anaconda, vous devriez télécharger l'application, tout comme nous l'avons fait pour Python, puis l'installer.

Si vous voulez vérifier cela, il y a d'innombrables séries de tutoriels sur YouTube à ce sujet, vous pouvez les consulter.

Mais installons simplement un environnement virtuel ici même sur notre interface de ligne de commande.

Et cet environnement virtuel s'appelle `virtualenvwrapper-win`.

Pour l'installer, nous dirons `pip install virtualenvwrapper-win`. Et après avoir fait cela, nous mettrons un trait d'union, puis nous dirons `win`. Cette ligne de commande va l'installer sur notre ordinateur.

Encore une fois, j'ai cela installé, donc il va me dire "requirement already satisfied", mais pour vous, il devrait dire d'aller de l'avant et de l'installer.

Il devrait donc montrer la barre de chargement, le téléchargement ou quelque chose comme ça.

Notez que si vous êtes sur un Mac, lorsque vous installez tous ces paquets, vous devez taper `pip3`.

Vous pouvez voir qu'ici sur Windows nous tapons `pip install`, puis nous tapons le nom du paquet, mais si vous êtes sur un Mac, vous taperez `pip3 install` puis le nom du paquet.

C'est juste la différence principale entre l'installation sur Windows et sur Mac.

Maintenant que nous avons ce `virtualenvwrapper` installé, allons-y et créons un environnement virtuel dans notre projet Django.

Pour faire cela, nous allons dire `mkvirtualenv`.

Maintenant, quand nous disons `mkvirtualenv`, nous allons laisser un espace, puis nous allons mettre le nom de l'environnement virtuel.

Vous pouvez lui donner n'importe quel nom, disons que vous travaillez sur un projet nommé "online dictionary", c'est votre projet Django, vous pouvez aussi donner le nom de l'environnement virtuel "online dictionary".

C'est juste pour que vous puissiez facilement y accéder quand vous le souhaitez.

Vous pouvez lui donner n'importe quel nom que vous aimez.

Mais personnellement, j'adore donner le nom de mon projet.

Mais pour l'instant, donnons-lui le nom `my_app`.

Donc `mkvirtualenv my_app` puis Entrée.

Maintenant, cela va créer un environnement virtuel nommé `my_app`.

Et ensuite, une fois qu'il a fini de créer cet environnement virtuel particulier, ce qu'il va faire est d'activer automatiquement cet environnement.

Cela prendra quelques secondes.

Comme vous pouvez le voir, nous avons déjà cela installé.

Et ensuite, avant de l'installer, à côté du répertoire où nous sommes, nous ne voyions rien encore.

Mais après maintenant, vous pouvez voir que nous avons `(my_app)`.

Cela vous montre qu'il a créé l'environnement virtuel appelé `my_app`, et il l'a activé.

Comme je l'ai dit, nous utilisions un environnement virtuel, c'est comme une boîte différente de tout l'ordinateur.

Mais avant de pouvoir accéder à cette boîte, à notre petit environnement, nous devons l'activer.

Maintenant que nous avons activé cet environnement virtuel, tout ce que nous faisons dans cette ligne de commande particulière va être dans cet environnement.

Maintenant, je vais installer Django, et quand j'installe Django en disant `pip install django`, sachez que si vous êtes sur un Mac, ce devrait être `pip3 install django`.

Maintenant, quand j'installe Django et que j'appuie sur Entrée, il ne va pas me dire "requirement already satisfied" à nouveau.

Et maintenant vous devriez savoir pourquoi, c'est parce que nous avons Django installé sur notre ordinateur.

Mais nous ne l'avons pas installé dans cet environnement virtuel, qui est séparé de ce que nous avons sur notre ordinateur.

Comme vous pouvez le voir, il installe à nouveau Django, qui est la version 3.2.2, la dernière version.

C'est donc la différence entre votre environnement virtuel et votre environnement d'ordinateur normal ou peu importe comment vous voulez l'appeler.

Mais comme vous pouvez le voir ici même, nous avons cet environnement, au fur et à mesure que nous avons créé l'environnement virtuel, il s'est automatiquement activé.

Pour que vous sachiez si vous êtes dans un environnement virtuel, ou si l'environnement est activé, vous allez voir ces parenthèses et ensuite le nom de l'environnement à l'intérieur avant le répertoire.

Vous savez, quand vous ouvrez pour la première fois votre terminal ou invite de commande, la première chose que vous allez voir est le répertoire où vous êtes. Dans un environnement virtuel, vous verrez d'abord le nom de l'environnement virtuel entre parenthèses, puis le répertoire. Cela devrait vous montrer que vous êtes dans l'environnement virtuel.

Et si nous fermons cette ligne de commande ou invite de commande et que nous revenons, vous savez, nous n'allons plus voir ce `my_app`.

Alors comment pouvons-nous accéder à cet environnement ou activer ou entrer dans l'environnement ? Je vais aussi en parler dans quelques minutes.

Pour l'instant, vous pouvez voir que nous avons Django installé dans cet environnement.

C'est très bien.

Maintenant, nous sommes dans un environnement virtuel pendant un moment, passons directement à Django.

Nous avons Django installé.

La chose suivante que nous voulons faire est de créer un projet Django parce que nous voulons travailler avec Django.

Django a cette ligne de commande qui vous permet de créer un projet, un nouveau projet.

Tout d'abord, vous devez vous assurer que vous êtes dans le répertoire que vous voulez.

Laissez-moi ouvrir mon dossier rapidement.

C'est mon dossier. Ce répertoire est ce qui se trouve dans cette ligne de commande.

Vous pouvez donc voir ici même, `project/django-tutorial`.

Ici, vous voyez `project/django-tutorial`.

Cette ligne de commande est ouverte dans ce répertoire. Tout ce que je crée, si je crée un nouveau projet Django, il va être créé dans ce répertoire.

Maintenant, je vais juste dire `django-admin startproject my_project`.

Donnons-lui le nom `my_project`.

Vous pouvez donc voir maintenant que nous avons l'environnement virtuel dans `my_app`.

Et c'est la ligne de commande que nous allons utiliser pour créer un nouveau projet Django.

Une fois que j'appuie sur Entrée, je vais juste lui donner quelques secondes.

Cela n'a rien montré ici.

Mais si je reviens dans cette page, vous voyez maintenant que j'ai un nouveau projet nommé `my_project`.

Revenons rapidement. Ce que nous avons fait était `django-admin startproject my_project`.

Cela va nous permettre de créer un nouveau projet `django-admin startproject`, puis le nom du projet après.

Si vous travaillez sur, disons, un moteur de recherche en ligne, ou si vous voulez le nommer... peu importe comment vous voulez le nommer.

Vous pouvez donc dire `django-admin startproject online_search_engine`, ou peu importe comment vous voulez nommer le vôtre.

Voilà comment créer un projet Django simple.

Maintenant, si j'appuie sur `dir`, je vois que j'ai un nouveau fichier, un nouveau dossier ici, entrons dans ce dossier, `cd my_project`.

Maintenant je suis dans mon dossier de projet.

Si j'appuie à nouveau sur `dir`, vous pouvez voir que j'ai `manage.py` et `my_project`, je vais expliquer tout cela. Cela peut sembler déroutant au début, je vais tout expliquer, je le promets.

Je vais donc expliquer rapidement comment vous pouvez aussi faire toutes ces choses sur Mac.

Créer un nouveau projet est exactement la même chose, juste comme `django-admin startproject my_project`, exactement la même chose.

Et ensuite ici même, quand j'ai appuyé sur `dir`, ce que j'ai fait était de voir tous les fichiers et dossiers dans ce répertoire particulier.

Si vous êtes sur un Mac, ce que vous devez taper est `ls`. Une fois que vous tapez `ls`, laissez-moi juste le taper rapidement ici.

Si je clique sur Entrée, ce n'est pas reconnu parce que je suis sur Windows, mais sur Mac, cela va vous montrer une liste juste comme ceci de tous les fichiers et dossiers que vous avez dans ce répertoire.

Et ce que j'ai fait était d'aller dans ce dossier `my_project`, exactement la même chose avec Mac, tapez simplement `cd my_project`, vous allez entrer.

Maintenant que nous avons cela, revenons.

Laissez-moi entrer dans ce projet.

Que voyons-nous ici ? Nous voyons un fichier `manage.py`.

Et ensuite nous voyons un dossier, qui porte le nom de notre projet, qui est `my_project`.

Laissez-moi l'ouvrir.

Et nous voyons comme un groupe de fichiers ici.

Et je vais expliquer tout cela.

Mais avant de faire cela, amenons ce projet dans Visual Studio Code.

Nous avons donc parlé de tout faire dans l'interface de ligne de commande, de créer le projet.

Mais que voulons-nous réellement coder ? Nous avons besoin d'un IDE, d'un éditeur de code, peu importe comment vous voulez l'appeler.

Et celui que j'adore utiliser est Visual Studio Code.

J'ai donc Visual Studio Code ici.

Je vais simplement dire, venir ici, cliquer sur "File".

Et ensuite je vais ouvrir un nouveau dossier.

Je ne suis pas... oh oui, j'ouvre un nouveau dossier.

Ce devrait être dans `project/django-tutorial/my_project`.

Je veux donc ouvrir ce dossier, sélectionner le dossier.

Cela devrait prendre quelques secondes.

C'est pourquoi j'aime Visual Studio Code, parce qu'il est vraiment rapide et léger, comparé à d'autres IDE.

Cela devrait s'ouvrir maintenant.

Pendant que cela s'ouvre, laissez-moi dire quelque chose rapidement.

Cela s'est ouvert là. Mais laissez-moi juste fermer cela.

Rappelez-vous que j'ai dit : et si l'un de nous accède à cet environnement virtuel particulier, disons que nous fermons cette interface de ligne de commande et que nous voulons accéder à cet environnement virtuel ? Je vais vous montrer comment faire cela dans notre Visual Studio Code.

Ici même.

Tout d'abord, ce sont les fichiers que nous obtenons lorsque nous créons un nouveau projet Django.

Ce fichier `manage.py`, vous ne voulez pas y toucher tout au long de votre codage, tout au long de la construction de quoi que ce soit.

C'est personnellement... il peut y avoir des développeurs qui manipulent ce fichier. Normalement, en tant que débutant, même en tant que développeur Django intermédiaire, vous ne voulez pas toucher à ce fichier, il n'y a rien que vous vouliez faire ici.

Ce fichier sert juste à nous permettre de faire plusieurs choses dans notre projet, comme exécuter notre projet sur l'hôte local (localhost).

Nous pouvons donc voir ce que nous construisons, migrer les bases de données, et je ne veux pas entrer dans les détails, parce que vous ne comprenez peut-être pas maintenant, mais vous comprendrez plus tard.

Mais pour l'instant, vous ne voulez pas toucher à ce fichier.

Fermons donc cela.

Et ensuite quand nous entrons dans `my_project`, nous avons un fichier `__init__.py`. Oui, ce fichier est vide pour l'instant. Il n'y a pas grand-chose à expliquer dans ce fichier, laissons-le comme ça.

Nous allons utiliser tous ces fichiers plus tard dans ce tutoriel, donc je vous montre juste comme un boilerplate que Django fait apparaître quand nous créons un nouveau fichier, donc nous allons utiliser ce `asgi.py`, c'est un fichier important. Nous n'avons pas besoin de beaucoup de manipulation dans celui-ci, c'est juste une ligne de code ou quelque chose pour accéder à certains sockets et autres. Donc laissez cela pour l'instant.

Et ensuite ce fichier `settings.py` est comme le socle de tout votre projet.

Si vous faites quelque chose de mal dans ce fichier `settings`, cela va affecter votre projet.

Nous avons donc besoin de ce fichier, nous avons beaucoup besoin de ce fichier. Nous allons l'utiliser pour, par exemple, ces `INSTALLED_APPS`, nous allons faire certaines choses là-dedans. Nous descendons pour voir où nous avons les templates. C'est vide pour l'instant. Nous allons faire certaines choses.

Et ensuite nous continuons, oui, nous allons faire beaucoup de choses dans ce fichier `settings`, c'est juste le fichier qui a tout ce dont nous avons besoin dans notre projet.

Toutes les configurations, et les applications lors de l'installation de n'importe quoi dans toutes nos bases de données sont à l'intérieur de ce fichier, nous allons le configurer.

Maintenant nous avons ce fichier `urls.py`. Laissez-moi expliquer ce que fait ce fichier `urls.py`. Ce que fait ce fichier `urls.py`, c'est que nous allons venir ici.

Et ensuite nous allons spécifier toutes les URLs que nous voulons dans notre projet.

Par exemple, disons que nous avons un site web nommé `www.codewithtomi.ml`.

Nous avons ce site web, quand un utilisateur vient juste sur `codewithtomi.ml`, quelle page voulons-nous ouvrir ? Vous allez le spécifier, mais quel que soit l'utilisateur qui va sur `codewithtomi.ml/newsletter`, ou `/blogpost` ou autre chose.

Chaque slash est une autre page web. Une autre URL est ici. Nous allons le spécifier ici, nous allons configurer chaque URL que nous avons dans notre projet. Nous allons en parler plus tard dans ce cours.

Et ce `wsgi.py`, oui, c'est un peu similaire à l'ASGI. Mais pour l'instant nous allons laisser cela.

Ici, nous avons tout cela.

Maintenant, ce que je veux faire... j'adore travailler dans cette invite de commande.

Mais ce que je veux faire maintenant, tout d'abord, je veux désactiver cet environnement virtuel.

C'est très facile. Tout ce que j'ai à faire est de taper `deactivate`.

Maintenant vous pouvez voir que nous ne sommes plus dans l'environnement virtuel.

Mais maintenant je suis loin de l'environnement virtuel, comment puis-je y accéder à nouveau ? Allons dans VS Code.

Dans VS Code, nous pouvons avoir notre terminal, notre petit terminal ici même.

Nous n'avons donc pas besoin de retourner à l'invite de commande chaque fois que nous devons faire quelque chose.

Ici même, vous allez voir que nous avons ce terminal, nous allons lui donner quelques secondes pour se charger.

Cela ne devrait pas prendre trop de temps.

Ici même dans ce terminal, nous allons accéder à notre projet, il est déjà dans ce répertoire de projet.

Maintenant, disons que nous voulons aller dans l'environnement virtuel très, très facilement. Nous avons juste besoin de dire `workon`. C'est une abréviation de cela.

Et ensuite nous dirons le nom de l'environnement virtuel. Mon environnement virtuel était `my_app`.

Normalement, nous devrions avoir quelque chose comme ça ici même, mais ce n'est pas le cas. Venons dans notre invite de commande et disons `workon my_app`.

Ici même, vous pouvez voir qu'il ramène l'environnement virtuel, cela montre que nous sommes dans cet environnement virtuel.

Dans VS Code, il est censé faire la même chose, mais je suis sûr que c'est parce qu'il utilise peut-être un autre type d'interface de ligne de commande ou autre chose.

Mais oui, cela va être un problème mineur. Nous pouvons simplement passer outre.

Mais voici comment nous pouvons désactiver un environnement virtuel et retourner dans l'environnement virtuel, c'est très facile.

Laissez-moi simplement quitter ceci.

Maintenant, ce que nous avons fait, c'est que nous avons créé un nouveau projet Django, nous avons installé Django, nous avons parlé de l'environnement virtuel, j'ai expliqué tous les fichiers, ces fichiers qui ont été créés quand nous avons créé un projet Django, j'ai expliqué l'interface de ligne de commande, nous avons fait beaucoup de choses pour introduire Django.

Maintenant, je suis sûr que vous devriez au moins avoir une idée de ce qu'est Django.

Et maintenant nous pouvons commencer à travailler avec.

Maintenant que nous avons notre projet Django créé, ce dont je veux parler est l'application Django (Django app).

Maintenant, cela peut sembler drôle, mais il y a une différence entre votre projet Django et votre application Django.

Je vais l'expliquer en utilisant un site populaire.

Les applications Django sont comme des sous-ensembles du projet principal. Nous avons ce projet créé ici même.

À l'intérieur de ce projet, nous pouvons avoir plusieurs applications Django. Elles sont donc comme des sous-ensembles d'un projet particulier.

Mais pourquoi utiliserions-nous une application Django alors que nous avons déjà un projet ici ? Laissez-moi utiliser, par exemple, Instagram pour expliquer.

Nous avons Instagram.

Dans Instagram, vous savez que nous avons différentes sections, nous avons le flux (feed), le flux de photos, nous avons la place de marché (marketplace), nous avons les messages directs, nous avons les stories et plein d'autres choses.

Instagram pourrait être le projet principal, si nous utilisons Django pour cet exemple, disons qu'Instagram est le projet principal, puis nous avons les messages directs, cela peut être une application particulière, une autre application juste pour ce message direct, nous pouvons avoir une autre application pour la place de marché, nous pouvons avoir une autre application pour les réels, nous pouvons avoir une autre application pour vos stories, nous pouvons avoir une autre application juste pour le flux de photos.

Chaque application peut donc avoir une fonction particulière qu'elle remplit.

Maintenant, dans la plupart des projets, vous n'avez pas trop d'applications, vous pourriez juste avoir un projet et une application avec le projet, j'ai fait cela aussi.

Mais si vous avez un très gros projet que vous voulez faire et qui nécessite plusieurs applications, il n'y a aucun problème à faire cela.

C'est ce que sont les applications dans Django, elles sont le projet principal, et elles sont les sous-ensembles de ce projet, qui sont des applications pour différentes fonctionnalités.

Vous pouvez aussi avoir un projet ou une application et vous pouvez juste avoir plusieurs fonctionnalités. C'est aussi tout à fait correct. Cela dépend de la façon dont vous voulez organiser votre projet.

Mais un projet... au moins je vais créer une application Django très facilement, tout comme nous avons créé le projet Django.

Tout d'abord, nous devons nous assurer que nous sommes dans l'environnement.

Et ensuite nous sommes dans le répertoire de notre projet, le répertoire racine (root directory).

Quand je dis répertoire racine, ce que je veux dire est le répertoire qui contient le fichier `manage.py`. C'est le répertoire racine de ce projet Django.

Nous pouvons confirmer que nous sommes dans le répertoire racine en disant `dir`.

Nous voyons `manage.py`. Cela nous dit que oui, vous êtes dans le répertoire racine.

Maintenant, pour créer une application, c'est là que nous utilisons ce `manage.py`. Plus tôt j'ai expliqué que ce `manage.py`, nous ne voulons pas vraiment coder quoi que ce soit à l'intérieur, mais nous utilisons beaucoup le fichier pour différentes choses.

Créer une application est l'un des moments où nous utilisons ce fichier `manage.py`, nous dirons simplement `python manage.py startapp my_app`. Puisque j'ai déjà mon projet nommé `my_project`.

Et ensuite quand nous appuyons sur Entrée, il ne va pas nous donner de réponse ici même sur l'interface de ligne de commande.

Mais si nous allons dans notre Visual Studio Code, si je viens ici, vous voyez maintenant que j'ai un nouveau dossier nommé `my_app`.

Et en dessous j'ai un autre dossier et un groupe de fichiers.

Laissez-moi donc rapidement faire le tour et expliquer. Ce `__init__`, nous ne faisons pas vraiment grand-chose à l'intérieur. C'est juste pour les migrations pour les modèles, vous comprendrez cela plus tard.

Cet `admin.py`, Django a cette belle interface d'administration, qui vous permet de contrôler votre site ou de maintenir votre site, vous voyez toutes les bases de données, tout ce que vous devez savoir sur votre site.

Et ce fichier `admin.py` est l'endroit où nous enregistrons certaines bases de données que nous voulons y mettre, et d'autres choses que nous voulons faire.

Et ce fichier `apps.py`, nous l'utilisons aussi, mais pas trop. Mais laissons cela.

Et ce fichier `models.py` est le fichier où nous créons toutes nos bases de données.

Traiter les bases de données dans Django est assez différent. Parce que nous n'avons pas besoin d'écrire une seule ligne de code SQL. Je vais aussi expliquer cela plus tard dans ce cours.

Et ce fichier `tests.py`, nous l'utilisons dans certains cas, mais pas souvent, donc il n'est pas fréquemment utilisé.

Et ce `views.py` est l'endroit où tout le principal se passe.

Ce que nous allons regarder dans cette vidéo, si vous voulez dans cette vidéo, c'est par là que nous allons commencer.

Maintenant, laissez-moi quitter tout ça.

Maintenant, nous avons tout cela.

Maintenant, disons que nous voulons commencer par les configurations des URLs.

Les configurations des URLs, quand je dis cela, ce que je veux dire, comme je l'ai expliqué plus tôt, j'ai dit c'est... disons que vous avez un projet, et ensuite chaque lien particulier, disons que vous avez un site web comme `youtube.com`, alors chaque lien particulier est une URL différente.

C'est ce qu'est la configuration des URLs, vous allez comprendre cela dans un instant.

Ce que nous voulons faire maintenant est de configurer les URLs. Laissez-moi rendre cela plus compréhensible.

Nous avons ce site web `djangoproject.com`. Si je clique sur "Overview", ou si je clique sur "Downloads", laissez-moi venir ici cliquer sur "Download".

Maintenant vous voyez que j'ai `djangoproject.com/download`. Ce `/download` est une autre URL.

Ce `djangoproject.com`, le principal, est l'URL racine, c'est l'URL que l'utilisateur doit voir quand il entre sur notre site.

Et nous avons `/download` parce que je connais cette URL. Nous devons configurer tout cela à l'intérieur de notre projet Django, c'est ce qu'on appelle le routage URL (URL routing), ou le mapping URL, ou la configuration URL. On peut l'appeler n'importe comment.

Pour commencer, nous n'allons pas venir dans `my_app`, et ensuite dans `my_app`. Mais où sont les fichiers URLs ?

Nous allons donc créer un nouveau fichier et le nommer `urls.py`.

Et nous devons importer quelque chose de Django appelé `path`.

On dit donc `from django.urls import path`.

Ce `path` va nous permettre d'utiliser plusieurs URLs dans notre liste.

Nous allons donc avoir une nouvelle liste appelée `urlpatterns`.

Et cette liste va prendre toutes les URLs que nous avons dans notre projet.

On peut donc dire `path`. Voilà comment nous spécifions une nouvelle URL.

Et ensuite j'ai juste ce qu'on appelle des guillemets.

Et ensuite maintenant je dis `views.index`. Je vais expliquer tout cela, et ensuite `name='index'`.

Nous avons donc importé `path` de `django.urls`. C'est ce qui nous permet de configurer chaque URL, vous pouvez voir que nous utilisons les chemins.

Et ensuite nous avons juste une nouvelle liste nommée `urlpatterns`.

Et ensuite nous avons plusieurs... comme si vous voulez une autre URL, vous pouvez simplement ajouter une nouvelle URL, une nouvelle URL comme ça. Cela montre que c'est une liste.

Maintenant utilisons `path` sur l'ouverture d'une parenthèse.

Et ensuite nous avons ces guillemets vides.

Quand c'est vide, cela signifie que c'est l'URL racine.

Disons que nous avons quelque chose comme `/download`. `/download` signifie maintenant que lorsqu'un utilisateur va sur notre site web `/download`, alors voici ce qui se passe.

Mais pour l'instant, quand c'est vide, cela signifie le retour, juste le site principal, le projet principal. Quand nous disons `/download`, c'est notre site `/download`.

Pour l'instant, c'est le site principal, et ensuite `views.index`.

La façon dont l'URL fonctionne dans Django est que dans votre fichier `urls.py`, nous configurons les URLs, mais quand un utilisateur vient sur cette URL particulière, que se passera-t-il ? Maintenant, cela va être fait dans le `views.index`. Nous pouvons rendre un fichier HTML, nous pouvons simplement envoyer une réponse HTTP RESTful, une réponse JSON, nous pouvons tout faire.

Cela va donc se passer dans les vues. Mais avant de pouvoir utiliser ces vues, nous devons les importer.

On peut donc dire `from . import views`.

Maintenant que nous avons importé les vues, nous pouvons dire `views.index`. Qu'est-ce que cet index signifie ? Cela signifie une fonction.

Ces vues que nous avons importées sont fondamentalement juste ce fichier `views.py` ici. Quand je viens ici, j'ai une nouvelle fonction nommée `index`. Elle prend une requête (`request`). Je vais aussi expliquer tout cela, et ensuite je peux passer (`pass`) pour l'instant.

Ici même, j'ai une fonction nommée `index`. Tout ce que nous faisons dans cette fonction est ce qui va être assigné à cette URL particulière.

C'est ainsi que cela fonctionne : l'utilisateur vient sur cette URL, et ensuite il voit qu'il doit aller dans les vues et chercher une fonction ou une classe ou peu importe appelée `index`.

Et ensuite tout ce qui est fait dans cet index est ce qui va être rendu à l'utilisateur.

Et ensuite nous allons simplement utiliser `name`. Vous pouvez donner à ce nom n'importe quoi, vous pouvez le nommer `index` ou `home`, mais il est conseillé de le nommer de la même manière que votre URL particulière, afin de ne pas être confus ou bloqué, ou d'avoir des sortes d'erreurs.

Ce nom sert aussi à donner à cela une sorte d'ID, c'est le nom.

Plus tard, vous allez voir pourquoi nous donnons un nom, pour l'instant nous le laissons comme ça.

Sauvegardons ce fichier.

Comme je l'ai dit, la plupart des utilisateurs qui viennent sur l'URL vont aller dans `views.index`.

Et ensuite tout ce que nous faisons dans cet index est ce qui va être rendu.

Ce que nous voulons juste faire maintenant, c'est... ce que je fais ici est ce qui va être rendu, faisons quelque chose, retournons quelque chose.

Et nous pouvons simplement retourner une réponse HTTP.

Pour que nous fassions cela, nous devons l'importer de Django URLs de `django.http import HttpResponse`.

Et maintenant disons `return HttpResponse`.

Et ensuite cette réponse HTTP peut être comme une balise HTML, comme un `h1`.

Et ensuite elle dit `Welcome`.

Et ensuite nous pouvons fermer ce `h1`.

Nous avons donc juste un code HTML simple à l'intérieur de ceci.

Maintenant, si j'exécute mon projet, je vais aussi vous montrer comment exécuter votre projet Django.

Si j'exécute mon projet, vous allez voir que nous n'avons rien.

Tout d'abord, exécutons notre projet. Avant de continuer.

Revenons dans notre ligne de commande et disons `python manage.py runserver`.

Rappelez-vous que j'ai dit que nous allons beaucoup utiliser `manage.py` dans notre ligne de commande.

Pour que nous exécutions notre projet sur notre hôte local, afin que nous puissions voir ce que nous construisons, nous devons appuyer sur `python manage.py runserver`. Je vais appuyer sur Entrée, et ensuite vous allez voir ce qui va se passer, cela va exécuter notre projet sur l'hôte local avec un port de 8000.

Nous n'avons pas besoin de copier cela. Venons dans notre navigateur, et ensuite collons-le simplement.

Pendant que nous attendons que cela se charge, vous pouvez voir ce qu'il nous montre. Ce qu'il nous montre ici même est un template Django par défaut d'un nouveau projet. Si vous créez un nouveau projet et que vous l'exécutez, c'est ce que vous allez voir.

Mais évidemment, nous ne voulons pas voir cela. Ce que nous voulons voir, c'est notre propre site web, nos propres templates, notre fichier HTML, notre réponse, tout ce que nous voulons faire.

Revenons maintenant à Visual Studio Code.

Nous avons tout fait ici.

Nous avons dit que lorsqu'un utilisateur vient sur la page d'accueil, il doit aller dans `views.index`. Et dans `views.index`, nous envoyons simplement une réponse HTTP, qui est un `Welcome`. Tout cela est censé montrer un `Welcome` maintenant.

C'est parce que tout ce que nous avons fait est à l'intérieur de cette application, cette `my_app`.

Mais rappelez-vous que j'ai dit que `my_app` est juste un sous-ensemble du projet principal. Nous devons aussi dire au projet principal où chercher sa propre URL.

C'est ainsi qu'il va le voir.

Ce que nous allons faire, c'est venir dans `my_project`, dans `urls.py`. Nous allons, tout d'abord, importer quelque chose nommé `include`.

De `django.urls import path`, de `django.urls` nous pouvons aussi importer `include`.

Cela va nous permettre d'inclure une URL similaire à partir d'un chemin d'application, tout comme nous créons une autre URL, la même chose.

Ici même maintenant, nous ne disons pas `views` ou quoi que ce soit, puisque nous avons déjà configuré cela dans l'application. Mais nous allons simplement dire `include('my_app.urls')`.

Si vous connaissez bien Python, vous devriez comprendre ce que cela fait ici. Ce qu'il fait, c'est qu'il inclut `my_app.urls`. Il va donc aller dans `my_app` ici même, dans `urls.py`, qui est ce fichier d'URL, et il va chercher une URL similaire à celle-ci.

Donc, n'importe où avec cette page d'accueil, ce qui est fait là est ce qui va être rendu.

Nous pouvons quitter tout ça.

Maintenant nous revenons ici et nous rafraîchissons, vous allez voir maintenant que nous avons un `Welcome`. Nous n'avons plus ce template Django par défaut. Ce que nous avons maintenant, c'est cette balise `h2` particulière, cette réponse HTTP particulière.

C'est fondamentalement comment faire un routage URL simple.

Il y a beaucoup plus de ce routage URL dont nous allons parler plus tard dans ce cours, c'est ainsi qu'on fait fondamentalement une configuration d'URL simple dans Django.

À ce stade, nous avons vu comment nous débarrasser des templates par défaut de Django. Quand nous créons un nouveau projet Django, ce template allait vous montrer comment vous en débarrasser et mettre notre propre réponse.

Comme vous pouvez le voir, ici même, il est écrit `Hey Welcome`. C'était ce que nous avons fait, n'est-ce pas ? Dans Visual Studio Code, nous avons juste retourné une réponse HTTP simple avec une balise HTML `h1` disant `Hey Welcome`.

Maintenant, nous voulons plus que cela. Nous pouvons coder tout notre HTML ici même, nous pouvons mettre toutes nos balises `p`, tous nos formulaires, si vous connaissez bien le HTML, vous savez de quoi je parle. Mais nous voulons avoir notre propre fichier HTML externe, que nous voulons rendre quand un utilisateur veut accéder à cette page d'index.

C'est facile. Django est assez facile. Ce que nous devons faire, c'est configurer Django pour qu'il puisse voir nos fichiers HTML, pour qu'il puisse voir nos fichiers de templates, ou pour qu'il puisse localiser ces fichiers. C'est le bon mot.

Donc, quand nous demandons, disons `index.html`, Django sait où localiser ce fichier, et ensuite il le rend.

Faisons cela rapidement. Fermons tout ça. Fermons tout ça aussi.

Ici même dans notre répertoire racine, rappelez-vous que j'ai dit que le répertoire racine d'un projet Django est le répertoire qui contient le fichier `manage.py`. Ici même, nous allons créer un nouveau dossier. Ce dossier va s'appeler `templates`.

Et dans ce dossier, nous allons stocker tous nos fichiers de templates. C'est-à-dire tous les fichiers HTML que nous allons utiliser dans ce projet.

Mais si je stocke simplement mon fichier de template ici même, et que je viens ici et que je dis "D'accord, Django, montre index.html". Nous venons de créer un fichier de template. Mais nous n'avons pas dit à Django que c'est là qu'il doit chercher `index.html`, ou n'importe quel fichier de template que nous utilisons.

Nous devons donc dire à Django cela. Nous allons le faire en utilisant ce fichier `settings.py` dans notre dossier de projet.

Nous allons donc devoir ouvrir `settings.py` et ensuite nous allons remonter.

Et ensuite nous allons venir, rendons cela plein écran ici même où nous voyons `TEMPLATES`. C'est la configuration pour le template que nous allons chercher là-dedans.

C'est une forme abrégée de répertoire (`DIRS`).

Il s'agit donc de dire dans quel répertoire Django doit aller pour chercher le fichier de template.

C'est très facile puisque nous avons déjà le dossier templates ici. Nous allons simplement dire `BASE_DIR / 'templates'`.

Ce `templates` doit être le nom de ce dossier.

Ce que nous disons, c'est qu'il doit aller dans le répertoire de base, qui est aussi le répertoire racine, et chercher un dossier nommé `templates`.

Disons que nous avons nommé ce template sans un `s`, nous devons aussi venir ici et enlever ce `s` et mettre `template`.

Donc tout ce que vous mettez ici doit correspondre au nom du dossier.

Maintenant, nous pouvons sauvegarder cela.

Maintenant Django sait où chercher nos fichiers de templates, fermons tout ça.

Ce que nous voulons faire maintenant est d'aller dans ce dossier templates, et de créer un nouveau fichier nommé `index.html`.

Dans cet `index.html`, nous pouvons avoir un `h1` maintenant avec un fichier HTML normal, un fichier HTML normal, et ensuite nous pouvons simplement dire, disons, `How are you doing today`.

Dans nos vues maintenant, nous ne voulons pas retourner cette réponse HTTP, ce que nous voulons faire est de rendre ce template HTML. Django sait où chercher les templates. Tout est simplifié.

Maintenant, nous pouvons enlever cette réponse HTTP, et dire `return render(request, 'index.html')`.

C'est demander `index.html`, qui est le nom du fichier que nous essayons de rendre, qui est ici même.

Nous avons donc notre fonction `index`, qui a une requête, maintenant ce qu'elle retourne, c'est qu'elle rend `index.html`.

Sauvegardons ce fichier.

Et ensuite nous venons ici.

Et ensuite nous rafraîchissons.

Vous allez voir maintenant que nous n'avons rien. Voyons pourquoi. C'est parti. Oui. Et je me suis assuré. Sortons du serveur. Et puis exécutons-le à nouveau. Donnons-lui une minute pour s'exécuter. Et ensuite venons ici, et rafraîchissons.

Vous pouvez voir maintenant qu'il est écrit `How are you doing today?`. Cela montre que cela vient de notre fichier `index.html`, pas d'une réponse HTTP.

Maintenant, la raison pour laquelle cela n'a pas chargé avant, je suis sûr que c'est parce qu'il a été mis en cache ou quelque chose comme ça. Quand nous sommes sortis de ce serveur Django, nous avons fermé le serveur et nous l'avons redémarré, il s'est rechargé. Parfois, vous pourriez avoir besoin de faire cela.

Vous voyez maintenant qu'il est écrit `How are you doing today?`. Nous pouvons juste avoir une image. Ici même, sauvegardez-le. Nous avons cela sauvegardé. D'accord, rafraîchissez. Et ensuite vous pouvez voir cette image. C'est du HTML typique, nous pouvons donc fermer tout ça maintenant.

Maintenant vous avez vu comment rendre un template HTML, ou un fichier de template dans une URL Django.

À ce stade, vous devriez commencer à comprendre comment travailler avec Django, comment créer un nouveau projet, vous devriez connaître la différence entre un projet Django et une application Django. Vous devriez savoir comment procéder aux configurations des URLs, vous devriez savoir comment configurer vos fonctions de vues, puis vous devriez comprendre le rendu des templates Django.

Maintenant, nous voulons parler de l'envoi de données dynamiques à votre fichier de template. Je vais expliquer ce que je veux dire par là. Venons dans mon Visual Studio Code.

Ici même, j'ai juste le texte brut nommé `How are you doing`. Laissez-moi expliquer la différence entre statique et dynamique. Quand quelque chose est statique, cela signifie qu'il est le même. Quand quelque chose est dynamique, cela signifie qu'il change selon une lettre particulière ou une fonction particulière ou tout ce qui est donné. Je vais expliquer cela davantage quand nous ferons les choses pratiques.

Ce `How are you doing?` est statique, parce qu'il est là, il ne change pas. Nous disons cela parce que si je recharge cette page, il est là, il ne change pas. Il est juste là parce que c'est ce que je lui ai donné.

Quand quelque chose est dynamique, cela peut être comme une variable qui est différente pour chaque utilisateur. Tout comme lorsque vous venez sur `facebook.com`, vous voyez votre nom là-bas, ils peuvent dire `Welcome Tom` si c'est votre nom. Et ensuite si quelqu'un nommé John se connecte, il verra `Welcome John`. Mais quand vous allez sur Facebook et que vous voyez votre fil d'actualité, vous verrez le fil d'actualité de vos propres amis, pas celui d'une autre personne. Il y a d'innombrables façons d'y penser.

C'est ce que sont les choses dynamiques. Maintenant, cela arrive parce que c'est en fait la même page, comme le même fichier HTML, ou le même code, mais c'est différent pour chaque utilisateur. Et c'est ce que nous voulons dire par dynamique quand quelque chose n'est pas le même pour tout le monde.

Nous allons donc parler de l'envoi de données dynamiques à notre fichier de template. Ce que je veux dire, c'est que dans Django, parce que Django est un framework backend, nous avons implémenté certaines fonctionnalités de programmation dans le HTML, certaines choses comme les variables, certaines choses comme les instructions `if`, certaines choses comme les boucles `for`. Nous avons pu coder cela dans le HTML, en utilisant un langage particulier, c'est un langage de template appelé Jinja. Nous allons en parler plus tard.

Pour l'instant, comment envoyer ces données dynamiques à mon fichier ? Ce que je dois faire, disons que j'ai une variable appelée `name`. Je dis simplement que ce nom est `John`. Ici même, je peux dire `Welcome John`. Laissez-moi juste dire `John`. Rafraîchissez. `Welcome John`.

C'est statique, parce que c'est John. Si une autre personne nommée Tim se connecte, il va dire John. Si quelqu'un d'autre nommé Rose se connecte, il va dire John. Mais nous venons ici et maintenant changeons ce nom en, disons, `Patrick`.

Je peux envoyer cette variable dans mon fichier `index.html`, et je peux y accéder d'ici. Je peux faire cela en venant simplement après l'index HTML, vous ajoutez simplement les accolades, et ensuite le nom de la variable `name`. Et ensuite nous lui donnons cette variable `name`, que nous avons ici.

C'est donc comme la clé et la valeur. C'est comme un dictionnaire, c'est la clé, c'est la valeur. Maintenant, je vais pouvoir accéder à cette variable, grâce à cette clé dans mon `index.html`. Si je viens ici maintenant, au lieu de dire John, pour accéder à cela, je vais utiliser les accolades deux fois. Et je vais dire `name`. Si je sauvegarde ici maintenant...

Comme vous pouvez le voir maintenant, il est écrit `Welcome Patrick`. Maintenant, ce Patrick vient de notre backend, il ne vient pas juste comme un texte brut. Ici même nous disons `name`, mais ce qui est affiché là est Patrick. C'est parce que c'est ce que nous lui avons assigné ici même.

Maintenant, cela peut être différent pour tout le monde. Quand nous irons plus loin, vous allez voir comment nous allons utiliser l'authentification pour permettre à chaque utilisateur d'avoir ses propres données. Disons que ces données viennent d'une base de données. Disons que nous connectons un utilisateur, et ensuite nous obtenons ce nom. Et disons que ce serait quelque chose comme `user.name`, je montre cela et quelque chose comme le nom d'utilisateur.

Donc ce nom reçoit une valeur de `user.name`, qui vient maintenant de la base de données. Donc intuitivement, ce sera différent pour chaque personne. C'est ainsi que nous envoyons des données dynamiques en utilisant Django dans Django.

Maintenant, nous pouvons aussi rendre cela plus formaté. Comme, disons que nous en avons plusieurs. Ce n'est pas une bonne pratique de venir et de faire une virgule et de dire `age`, et ensuite de donner... sachez que vous pouvez aussi faire cela. Mais ce n'est pas une bonne pratique.

Nous pouvons donc avoir quelque chose que nous appelons `context`. C'est populairement utilisé dans Django, et ce contexte va être un dictionnaire. Dans ce dictionnaire, nous allons simplement avoir tous les champs que nous voulons, disons `name`, et ensuite nous lui donnons `Patrick`.

Et ensuite je dis `age`, nous pouvons lui donner `23`. `nationality`, nous pouvons dire `British`, et ensuite nous pouvons simplement continuer comme ça, c'est fondamentalement un dictionnaire.

Et ensuite si nous voulons passer cela dans le HTML, nous n'avons plus besoin de ces accolades, nous pouvons simplement dire `context`. Maintenant ce contexte est envoyé à cet `index.html`. Si je viens ici maintenant et que je dis `name`, cela va afficher le nom qui est ici, qui est toujours Patrick.

Cela n'a donc pas changé. Il dit `Welcome Patrick`. Et laissons-lui juste un saut de ligne. Et ensuite nous pouvons dire `you are age years old`.

Maintenant rafraîchissons, vous voyez qu'il dit `you are 23 years old`, qui est la variable `age` venant des vues. Mais nous pouvons aussi utiliser la nationalité et dire `you are British`. Rafraîchissons et il dit `you are British`.

C'est juste comment manipuler les données. Comme vous pouvez le voir, différentes données venant du backend, venant des vues. Et plus tard, je vais vous montrer comment obtenir tout cela de la base de données, pas seulement vous en tapant des données factices ou des données statiques.

Maintenant, j'espère que vous comprenez le concept de l'envoi de valeurs dynamiques de vos vues à votre fichier de template dans Django.

Maintenant, nous allons prendre certaines des fonctionnalités que nous avons apprises dans les parties précédentes, puis avec quelques nouvelles fonctionnalités, et ensuite nous allons les utiliser pour construire un compteur de mots très simple dans Django.

C'est juste un tout petit projet, dans lequel un utilisateur va pouvoir mettre un groupe de mots là-bas, comme une phrase ou un article, et ensuite une fois que l'utilisateur le soumet, cela va montrer à l'utilisateur la quantité de mots qui sont présents dans ce groupe de texte.

Faisons cela. La première chose que nous devons faire, venons rapidement à notre serveur, qui s'exécute ici même. Nous voulons avoir comme un formulaire ici même, dans lequel un utilisateur pourra mettre tout le texte, et ensuite nous devrions avoir un bouton de soumission en dessous.

Faisons cela. Tout d'abord, dans VS Code, nous pouvons nous débarrasser de tout cela maintenant. Et ensuite nous avons juste un formulaire. Nous pouvons le laisser vide pour l'instant.

Dans ce formulaire, ayons une zone de texte (`textarea`). Donnons-lui un nom de `text`. Ce devrait être bien. Et ensuite ayons notre bouton de soumission. Cela ne devrait pas être `Submit`. Mais oui, nous pouvons avoir un saut de ligne.

Sauvegardons cela et rafraîchissons ici même. C'est juste ce que nous avons. Maintenant, disons que nous pouvons ajouter quelque chose comme des lignes (`rows`). Et ensuite disons juste pour lui donner plus de longueur. Je pense que quelque chose vient après. Donnons-lui `10`. Rafraîchissons.

D'accord, alors rendons cela comme `25`. Rafraîchissons. D'accord, je pense que c'est bien. Et ensuite rendons cela un peu plus grand, un double de `50`. Voyons. D'accord, je pense que c'est bien.

Et ensuite ici même, nous ne sommes pas vraiment pointilleux sur le design, nous voulons juste savoir comment ajouter la fonctionnalité backend. Venons ici au-dessus du formulaire, ici même, ayons un `h1`, qui dit simplement `Input your texts below`.

C'est donc notre formulaire. Rafraîchissons et voyons. C'est notre formulaire ici même. Et ensuite ce formulaire, donnons-lui une méthode. Si vous connaissez le HTML, vous savez qu'il y a deux méthodes quand vous soumettez un formulaire, qui sont `GET` et `POST`.

Nous allons laisser cela vide pour l'instant. Et nous allons parler davantage des méthodes `GET` et `POST` lorsque vous traitez avec Django. Nous allons en parler plus tard. Mais pour l'instant, nous allons laisser cela vide.

Ce que nous voulons faire maintenant, c'est récupérer tout le texte ici, et le soumettre. Maintenant l'URL, nous sommes toujours dans cette URL, cette page, et ensuite elle passe simplement quelques données, tout ce qui a été écrit dans cette zone de texte quand elle est soumise, ce qui est maintenant passé dans l'URL, et c'est sauvegardé dans cette variable, cette clé nommée `text`.

Et la raison pour laquelle c'est sauvegardé dans `text` est parce que nous lui avons donné un nom de `text`. Si nous lui donnons un nom de `words`. Je viens ici et je rafraîchis, je dis `How are you doing`, et ensuite je viens ici et je clique sur soumettre. Vous voyez maintenant qu'il est sauvegardé dans une variable clé de `words` avec toutes ces valeurs.

Maintenant que tout cela est passé à l'URL, il est très facile pour nous de récupérer toutes ces valeurs dans le backend. Laissez-moi expliquer ce que nous allons faire. Une fois que l'utilisateur clique sur soumettre, nous voulons l'envoyer à une autre URL. Ici même, vous pouvez voir qu'il renvoie simplement à cette page d'accueil. Nous allons créer une autre URL, peut-être comme un compteur, peut-être comme `/counter`. Cette URL va compter la quantité de mots, et ensuite elle va les renvoyer au fichier de template, puis nous montrer la quantité de mots.

Cela va prendre tout son sens dans un instant. Faisons cela. Tout d'abord, nous sommes censés avoir une action (`action`). L'action est l'endroit où nous voulons que toutes ces données soient envoyées. Maintenant nous n'avons pas vraiment d'autre URL, allons en créer une.

Ici même dans `urls.py`, ayons une autre URL. Et ensuite nous pouvons simplement nommer celle-ci `counter`. Et ensuite disons `views.counter`. Et ensuite donnons-lui un nom de `counter`.

Maintenant, vous savez que nous avons dit `views.counter`. Quand nous venons dans nos vues, nous n'avons aucune fonction nommée `counter`, alors allons en créer une. Ici même, nous voulons juste avoir une nouvelle fonction nommée `counter`. Et ensuite nous voulons qu'elle prenne une requête.

Maintenant, nous pouvons aussi retourner le rendu de la requête. Et ensuite nous voulons avoir juste comme nous avons `index.html` pour cette page, nous voulons avoir un autre fichier HTML pour ce compteur. Venons ici et créons simplement un nouveau fichier nommé `counter.html`. Pour l'instant c'est vide, laissons-le vide.

Maintenant nous pouvons rendre ce `counter.html`. Et ensuite nous pouvons laisser cela pour l'instant. Nous n'avons plus besoin de tout cela, débarrassons-nous de cela.

Maintenant ce que nous voulons faire, c'est que nous voulons que cette action aille vers `counter`. C'est très facile, nous allons juste mettre dans l'action le nom de l'URL, qui est `counter`. Maintenant une fois que nous cliquons sur soumettre, cela envoie toutes ces données à cette vue `counter`.

Allons voir comment cela se passe. Venons ici et rafraîchissons. D'accord, pas comme ça, et ensuite `what's up`, puis nous cliquons sur soumettre. Maintenant vous voyez qu'il va vers `/counter`. Avec ces mots. Maintenant que ce compteur a ces données particulières, nous pouvons récupérer ces données.

La première chose pour récupérer ces données, nous allons venir dans les vues, nous allons avoir une nouvelle variable, ou nommons simplement cette nouvelle variable comme `text`. Et ensuite pour la récupérer, nous allons dire `request.GET['text']`. Je vais expliquer tout cela.

Ce que nous faisons maintenant, c'est définir une nouvelle variable, et ensuite nous disons `request.GET`. Je veux donc envoyer une requête à tout ce qui est passé à cette vue particulière. Et ensuite nous voulons récupérer ceci, et ensuite ce que nous voulons récupérer, ce sont ces mots. Maintenant nous venons à l'index HTML, vous allez voir que nous envoyons ces données particulières dans ce compteur.

Et dans ce compteur, nous récupérons ces données. Donc `request.GET['words']`. Pourquoi nous avons ce mot, c'est parce que c'est le nom que nous avons donné au collecteur de texte particulier, comme la zone de texte, qui a collecté ces données, c'est le nom qui lui est assigné.

Maintenant nous changeons cela en `text`. Ce que nous voulons être maintenant devrait être `text`. Changeons-le simplement en `text` parce que cela a plus de sens. Maintenant vous voyez que, une fois que nous collectons ici, cela devrait être le même que ce qui est ici aussi.

Si nous changeons cela en, disons, `tx`. Maintenant cela ne peut pas... quand nous essayons de collecter des données à partir de lui. Il ne voit aucun formulaire avec le nom de `text`. Il ne va donc collecter aucune donnée. Donnez-lui `text`, il va collecter nos données. Ce que nous pouvons faire maintenant puisque nous avons déjà ces données, nous avons collecté nos données et les avons stockées dans cette variable nommée `text`.

En Python, il y a une façon de compter la quantité de mots présents dans un texte. Laissez-moi ouvrir rapidement mon invite de commande ici et vous montrer de quoi je parle, puis nous reviendrons ici. Laissez-moi ouvrir mon shell Python rapidement.

Et ensuite, disons que j'ai une variable nommée `text` et qu'elle a une phrase nommée `Hey, how are you doing`. Vous pouvez voir maintenant que c'est `1 2 3 4 5`, cinq mots là-dedans. Maintenant nous pouvons compter cela par, disons, nous pouvons simplement l'afficher directement, et dire `len(text.split())`.

Ce que cela fait, c'est que nous affichons simplement la longueur de `text.split()`. `split()` signifie que vous récupérez chaque mot présent dans ce texte. Une fois qu'il a tout séparé en une valeur différente, alors vous allez compter la quantité qui s'y trouve.

Faisons cela à nouveau. D'accord, c'est parce que je n'ai pas fermé la fonction `print`. Sortons de là. Et un de plus. Maintenant vous pouvez voir que nous en avons cinq. C'est parce que nous avons cinq mots ici.

C'est exactement la même chose que nous allons faire ici même dans notre projet. C'est déjà ce que l'utilisateur a écrit, stocké dans cette variable nommée `text`. Nous allons juste ajouter une nouvelle variable, je vais la nommer `amount_of_words`.

Et ensuite la quantité de mots sera la longueur de `text.split()`. Comme ceci. Maintenant nous avons la quantité de mots présents dans ce que l'utilisateur a écrit. Et nous l'avons stockée dans cette variable nommée `amount_of_words`. Ce que nous pouvons faire maintenant est d'envoyer cette quantité de mots directement dans ce `counter.html`.

Très facile. Ayons juste une clé et une valeur, disons `amount` et ensuite nous voulons lui donner `amount_of_words`. Très facile, nous sauvegardons cela. Et maintenant nous pouvons dire `the amount of words is` et ensuite quelle est la clé ? La clé est `amount`.

C'est la clé, c'est la valeur. Et nous utilisons la clé ensemble. La quantité de mots est donc ceci. Revenons maintenant en arrière. Et maintenant écrivons un texte complet qui a du sens. Disons `Hey, good, you are doing well`. Comptons ceux-là : `1 2 3 4 5 6 7 8 9 10`. Maintenant nous cliquons sur soumettre.

Et il dit `the amount of words is 10`. Vous pouvez voir maintenant qu'il dit que la quantité de mots est `10`, c'est exactement ce que nous voulons. Venons ici et donnons-lui juste un `h1`. Copiez, sauvegardez, visitez, rafraîchissez, et maintenant vous voyez, il dit que la quantité de mots est `10`.

Revenons simplement en arrière et ajoutons quelque chose pour enlever ceux-là et maintenant nous devrions avoir `1 2 3 4`, quatre. Nous cliquons sur soumettre, il dit que la quantité de mots est `4`. Maintenant vous pouvez voir que nous commençons à transformer ces fonctionnalités Django que nous apprenons en projet.

Vous pouvez voir maintenant que nous venons de faire un simple compteur de texte, il compte tous les textes. Cela peut aussi être très utile. Parfois, vous pourriez en avoir besoin pour un usage personnel. Si vous avez, par exemple, un article de blog. Laissez-moi simplement ouvrir un article de blog.

Et ensuite vous pouvez copier tout le texte et ensuite simplement le coller. Prenons quelque chose d'ici. Et ensuite nous pouvons simplement copier tout cela. D'accord, c'est un groupe de code. Vous comprenez de quoi je parle. Puis nous venons ici, nous le collons.

Et ensuite nous cliquons sur soumettre, et il a compté `4328` mots. Vous pouvez voir que c'est aussi très utile. Parfois, nous en avons juste besoin. Nous avons donc fait cela. Mais il y a quelque chose dont je veux parler davantage. Quand vous cliquez sur soumettre, vous allez voir que tout ce que nous avons écrit dans cette zone de texte, dans ce texte, a été envoyé dans l'URL, et c'est assez long.

C'est beaucoup. Et c'est la raison pour laquelle nous avons pu y accéder. Mais pourquoi ne voulons-nous pas que tout cela soit dans l'URL ? Ce que nous voulons, c'est que ce soit juste `/counter`. Et qu'il soit toujours capable de compter ce texte sans avoir tout cela dans l'URL comme ceci. Sans avoir cela, nous voulons juste ceci, et nous voulons être capables de compter. Nous allons aussi en parler davantage dans la partie suivante.

Parlons maintenant des requêtes GET et POST. Dans la dernière partie, nous avons construit le simple compteur de mots où nous avons pu mettre un groupe de texte. Et ensuite une fois que nous cliquons sur soumettre, il compte ce texte pour nous. Nous allons remarquer que tout le texte qui a été soumis est passé dans cette URL.

Laissez-moi expliquer pourquoi tout cela arrive. Si nous revenons à notre code, ici même dans notre formulaire, vous allez voir que lorsque nous avons spécifié la méthode, nous l'avons laissée vide. Cette méthode sert à vous faire connaître le type de requête que vous utilisez, le type de méthode que vous utilisez dans ce formulaire.

Il y a donc deux types qui sont utilisés, qui sont la méthode `GET` ou `POST`. Ce sont les deux types qui sont utilisés. Et une méthode `GET` est principalement utilisée chaque fois que nous ne passons aucune information personnelle ou aucune information très sûre. Parce que, comme je l'ai dit, elle est affichée dans l'URL.

Mais en utilisant une méthode `POST`, les informations qui sont envoyées ne vont pas être affichées dans l'URL. Laissez-moi vous expliquer pourquoi nous utilisons principalement la méthode `POST`. Disons qu'un utilisateur veut s'inscrire sur un site web, nous ne voulons pas passer le nom d'utilisateur et le mot de passe de l'utilisateur ici même dans l'URL, cela n'aurait pas de sens.

Ou un utilisateur veut payer en ligne avec sa carte de crédit, nous ne voulons pas mettre les détails de la carte de crédit dans son URL. C'est pourquoi nous utilisons la méthode `POST` parce qu'elle est plus sûre. Et elle empêche certaines attaques sur notre site web. Ici même, comme vous pouvez le voir, c'était bloqué, je n'ai spécifié aucune méthode.

Donc, quand on le laisse vide comme ceci, par défaut, il utilise automatiquement une méthode `GET`. Donc, si je ne mets aucune méthode ici même, mais que je mets juste une méthode et que je ne la spécifie pas, il utilise automatiquement une méthode `GET`. Je peux aussi venir ici et essayer `GET`. C'est toujours une méthode `GET`, ou je le laisse vide, c'est toujours une méthode `GET`.

Mais si je veux utiliser une méthode `POST`, je dois le mettre ici, c'est `POST` que je veux utiliser. Nous allons donc reconstruire ce compteur de mots à nouveau, mais maintenant en utilisant cette méthode `POST`, afin que vous compreniez le concept de `POST`. Changeons cela en méthode `POST`. Sauvegardons cela.

Et ensuite revenons ici et rafraîchissons. Maintenant nous allons mettre un groupe de texte. Et cliquons sur soumettre. Oui, donc ici même nous avons cette erreur. Maintenant il est écrit `Forbidden CSRF token verification failed. Request aborted`. Cela arrive parce que, comme je l'ai dit, une méthode `POST` est utilisée pour des informations plus personnelles.

Et chaque fois que nous utilisons une méthode `POST`, Django s'attend à ce que nous utilisions quelque chose que nous appelons un token CSRF (`CSRF token`). CSRF signifie Cross-Site Request Forgery. C'est comme une attaque. Quand vous passez des données à travers les URLs, un attaquant ou quelqu'un qui a de mauvaises intentions sur votre site peut puiser dans celles-ci et obtenir ces informations en utilisant ce token CSRF.

Django fournit un token CSRF par défaut qui nous permet d'empêcher cette attaque. Cherchons-le rapidement, `CSRF token`. Cela va apparaître, comme vous pouvez le voir, le token CSRF est une valeur secrète unique et imprévisible qui est générée par l'application côté serveur et transmise.

C'est juste une définition ennuyeuse. Mais c'est ce que fait le token CSRF. Il empêche cela. Ouvrons l'attaque CSRF. Oui, attaque CSRF. Dans une attaque CSRF, un utilisateur innocent est trompé par un attaquant pour soumettre une requête web qu'il n'avait pas l'intention de faire. C'est donc comme voler des informations.

Mais quand nous utilisons le token CSRF, cela empêche cela. J'espère que vous comprenez à quoi cela sert. Si nous n'utilisons pas le token CSRF dans Django, il ne permettra pas à notre formulaire de fonctionner. Nous devons donc ajouter cela. C'est très facile, juste une ligne de code, tout ce que nous devons faire est de mettre deux accolades, deux signes de pourcentage, et taper `csrf_token`.

Maintenant que c'est fait, tout va bien. Si nous revenons en arrière, rafraîchissons, mettons cela et cliquons sur soumettre. Je suis sûr qu'une erreur va encore apparaître. Oui, il est écrit `MultiValueDictKeyError /counter`. Nous avons donc une erreur. Mais maintenant ce n'est pas à cause de notre requête `POST`.

Nous avons tout couvert pour cela. Voilà comment faire votre méthode `POST`. Mais pourquoi nous avons cette erreur, c'est parce qu'ici même dans nos vues, vous allez voir que nous avons dit que nous voulions récupérer ce que l'utilisateur a envoyé, nous disons `request.GET`. Mais maintenant nous utilisons `POST`.

Nous devons donc aussi faire cela et dire simplement `request.POST`. C'est aussi simple que cela. Revenons en arrière, rafraîchissons. Saisissons trois mots. Maintenant cliquons sur soumettre. Vous voyez maintenant qu'il dit que la quantité de mots est trois, et ensuite notre URL est complètement propre. Nous n'avons aucune information passée dans notre URL.

La méthode `POST` est donc très, très utile chaque fois que vous traitez des informations plus sûres et sécurisées. J'espère que vous avez compris la différence entre les méthodes `GET` et `POST`.

Parlons des fichiers statiques dans Django. Qu'est-ce que ces fichiers statiques dans Django dont nous parlons ? C'est n'importe quel fichier externe que vous utilisez dans votre fichier de template. Les fichiers de templates sont les fichiers HTML que nous utilisons dans Django. Cet `index.html` est un fichier de template.

N'importe quel fichier externe que nous utilisons est un fichier statique. Comme si nous avons un fichier CSS externe qui est lié à ce fichier HTML, c'est un fichier statique. Si nous avons une image, nous avons une vidéo externe, tout cela sont des fichiers statiques. Tout comme nous avons configuré pour le fichier de template.

Rappelez-vous, plus tôt dans ce tutoriel, nous sommes allés dans les paramètres de ce projet, et nous avons dû dire à Django où tous ces fichiers de templates sont situés. Maintenant nous devons faire la même chose pour le fichier statique. Fermons cela. Fermons tout cela.

Disons que nous voulons ajouter un CSS externe à cette page. Enlevons ce formulaire, nous n'en avons plus besoin. Disons `Welcome to my project`. Disons que nous voulons ajouter un CSS externe à cette page particulière. Et ensuite nous voulons que ce CSS y soit lié.

Dans un HTML normal, nous n'avons pas besoin d'utiliser notre balise `link`. Et ensuite nous spécifions simplement où le fichier CSS est situé. Django est un peu différent. Tout comme nous stockons tous les fichiers de templates dans un dossier nommé `templates`, nous devons stocker tous les fichiers statiques dans un dossier nommé `static`.

Faisons cela. Créons un nouveau dossier. Disons `static`. Ce fichier statique, comme je l'ai dit, va contenir tous les fichiers externes dont nous avons besoin. Mais maintenant nous devons dire à Django où localiser tous les fichiers statiques. Et nous allons aussi le faire dans le fichier `settings.py`.

C'est pourquoi j'ai dit plus tôt dans cette vidéo que le fichier `settings.py` est comme le socle de tout le projet. Il est très utile. Ce que nous allons faire maintenant est de venir directement dans `my_project`, puis d'aller dans `settings.py`. C'était là que nous avions configuré les templates.

Pour les fichiers statiques, nous allons les configurer ici même. Mais avant de descendre, nous devons d'abord monter, et ici même nous devons importer quelque chose nommé `os`. Tapons `import os`. Ce que fait cet `os`, c'est qu'il récupère le système d'exploitation spécifique sur lequel nous codons. `os` signifie Operating System.

Cela permet de savoir si vous êtes sur un Windows ou un Mac ou peu importe. Maintenant que nous avons importé `os`, ce que nous voulons faire est d'aller tout en bas. Juste en dessous de `STATIC_URL`, nous pouvons avoir quelque chose qui s'appelle `STATICFILES_DIRS` avec un `s`. Nous allons dire `equals to` ouvrir un crochet, nous dirons `os.path.join(BASE_DIR, 'static')`.

Ici même nous laissons aussi une virgule. Ce qu'il fait, c'est qu'à partir de notre `os`, il va aller au répertoire de base, qui est aussi le répertoire racine de ce projet. Donc, quand je dis le `BASE_DIR`, je veux dire le répertoire racine. Ici même se trouve le répertoire de base, le dossier qui contient le fichier `manage.py` est le répertoire de base.

Et ensuite il va au dossier où nous avons `static`. Ici même se trouve ce dossier. Maintenant que nous avons configuré cela, dans ce dossier, nous pouvons créer un nouveau fichier et le nommer `style.css`. Maintenant nous avons ce `style.css`, stylisons ce `h1` et donnons-lui, par exemple, une couleur rouge.

On peut dire `h1 { color: red; }`. Nous avons cela. Et maintenant nous devons lier ce `static` ici même dans ce HTML. Nous faisons cela en haut du fichier. Et ensuite, vous savez, dans le HTML normal, ce que nous devons faire est de dire `link`, et ensuite nous disons `rel="stylesheet"`. Et ensuite nous disons `href` et ensuite nous lui donnons juste, par exemple, `style.css`, le nom du fichier, et ensuite nous fermons le fichier.

Maintenant, si je sauvegarde cela, et que je viens ici, et que je rafraîchis, vous verrez que nous avons juste ce texte, qui est en noir, et ensuite le CSS ne se reflète pas dessus. Et c'est parce que ce lien n'est pas vu par Django. C'est trop détaillé, nous allons utiliser les deux dans ce `href`.

Au lieu de simplement écrire `style.css`, nous devons ajouter quelque chose que nous appelons `static`. Pour utiliser notre `static`. Avant le nom du fichier, nous mettrons des accolades, un signe de pourcentage, nous écrirons `static`, laisserons un espace, ajouterons l'un des guillemets, nous le fermerons ici même comme ceci.

C'est ainsi qu'on utilise `static`. De cette façon, Django devrait savoir où localiser ce `style.css`. Maintenant, si nous sauvegardons et rafraîchissons, nous allons avoir une erreur, une erreur de template. Maintenant vous voyez qu'il est écrit `TemplateSyntaxError`. Il dit `Invalid block tag on line 1 'static', did you forget to register or load this tag?`.

Il dit donc que nous avons oublié de charger ce tag appelé `static`. Ici même, ce `static` est comme un tag que Django voit. Avant de pouvoir l'utiliser, nous devons le charger. C'est très facile, nous allons juste en haut du fichier. Chaque fois que nous voulons charger quelque chose dans Django, cela doit être en haut du fichier.

Et nous dirons accolades ouvertes et fermées, signe de pourcentage et `load static`. Maintenant quand nous sauvegardons cela, nous revenons et rafraîchissons. Boom, vous voyez maintenant qu'il l'affiche en couleur rouge. Cela montre que le CSS fonctionne sur ce fichier HTML. Il y est lié. Venons ici et changeons cela en bleu.

Sauvegardons, rafraîchissons, vous voyez maintenant que c'est bleu. Voilà comment lier un fichier statique à votre fichier de template. Mais maintenant allons plus loin. Et ensuite travaillons sur des projets plus réels. Ce que je veux faire maintenant est juste d'aller sur Google et ensuite de télécharger un template HTML gratuit.

Et ensuite je vais vous montrer comment lier différents types de fichiers statiques, pas seulement le CSS maintenant, peut-être des images, peut-être du JavaScript, n'importe lequel que nous téléchargeons. Je ne me suis pas préparé pour cela. Je vais juste chercher "free HTML templates" et n'importe lequel que nous verrons, nous allons l'utiliser. Voyons.

Je pense que celui-ci devrait être bon. Et descendons. D'accord. Regardons-les. Oui. Celui-ci devrait avoir beaucoup de CSS dedans. Et ensuite nous allons juste le télécharger. Le gratuit. Descendons. D'accord. C'est gratuit, descendons tout en haut et disons "free HTML template download" ou quelque chose comme ça, et récupérons-en un à télécharger.

Voyons. Je connais un site. BootstrapMade. Oui. Mais ce site web, je sais qu'ils sont gratuits, et ensuite venons ici et récupérons-en un à télécharger. Voyons. Travaillons avec celui-ci, "OnePage", téléchargeons. Téléchargement gratuit. Bootstrap 5, téléchargeons tout en s'inscrivant à la newsletter. Voyons.

Il se téléchargeait ici même, comme vous pouvez le voir. Donnez-lui une seconde. Et cela devrait être fini. D'accord, allons dans le dossier des téléchargements et cherchons cet extrait, puis déposons-le dans Visual Studio Code. Nous saurons comment l'utiliser. Cela devrait être fini de télécharger. Venons ici. Allons dans les téléchargements.

Ici même, nous pouvons simplement faire glisser cela ou nous pouvons simplement copier. Et ensuite revenons deux fois, ou trois fois. Et ensuite ici même se trouve notre projet Django, nous le collons là-dedans. Cela devrait prendre quelques secondes pour coller. Maintenant nous pouvons fermer tout cela, nous n'avons plus besoin de tout cela.

Maintenant nous pouvons juste commencer avec ce que j'ai dit que nous allions faire, changer différents ou connecter différents fichiers statiques dans notre projet. C'est fait. Et ensuite cela va l'ouvrir. Nous avons tout cela ici même. Bien. Maintenant nous venons ici, nous devrions avoir ce OnePage ici.

Et ensuite nous pouvons supprimer cet `index.html`. Supprimons simplement cela. Et ensuite d'ici, OnePage où nous avons `index.html`, faisons-le glisser dans le dossier templates. Oui, nous l'avons déplacé. Maintenant que nous avons déplacé cela, ce que nous voulons faire maintenant est de simplement déplacer ces `assets` dans le fichier `static`, parce que c'est là que les fichiers statiques sont situés.

Comme je l'ai dit, nous voyons le CSS, l'image, le JavaScript ici. Fermons ce OnePage pour l'instant. Et ensuite ici même dans `index`, c'est ce qui va être rendu quand la page Index est appelée `index.html`. Fermons cela. Et maintenant retournons à notre projet, et ensuite rafraîchissons.

Vous pouvez voir que le titre a changé. Et ensuite nous avons tout cela. Vous pouvez voir qu'il est lié aux fichiers statiques, mais pas de la façon dont Django le reconnaît. Tout cela est lié, mais pas de la façon dont Django les reconnaît. Maintenant, faisons juste changer tout ce dont nous avons besoin pour ce fichier.

Nous allons venir ici et faire `load static`. Et ensuite commençons d'ici, et ensuite nous pouvons en fait le rendre plus rapide en utilisant les deux comme ceci. Partout où nous voyons cela, nous le mettons simplement là-dedans. C'est une bonne astuce que j'utilise et ensuite nous faisons le signe de pourcentage, espace `static`.

Et ensuite nous mettons ceci juste ici. Et maintenant nous venons ici nous faisons la même chose. Nous le faisons juste ici à la fin de tous ces fichiers, et ensuite nous fermons juste un pourcentage et fermons. Maintenant si je sauvegarde cela, et que je viens ici et que je rafraîchis, je devrais voir un changement massif dans le site web.

Vous voyez maintenant que nous avons le chargement préalable, la balise ou le div, le style ou peu importe ce qui charge. Et ensuite notre page devrait charger comme prévu. Cela charge depuis trop longtemps, et je suis très sûr que c'est parce que nous n'avons pas lié tous les fichiers que nous étions censés lier. Copions simplement ce `static` et continuons à lier.

Continuons à lier. Voyons, descendons. Maintenant quand nous venons ici et rafraîchissons, cela devrait fonctionner, et cela ne devrait pas charger éternellement, bien. Maintenant vous pouvez voir que c'est ce que nous voulons. Ici même. Vous pouvez voir que le site web charge avec succès.

Voilà comment prendre fondamentalement un fichier de template, puis avec le statique, les fichiers statiques peuvent être liés différemment, ou comment les utiliser ou les lier dans Django. Maintenant, j'espère que vous avez compris tout ce dont nous avons parlé dans les fichiers statiques.

Parlons maintenant des modèles (models) dans Django. Dans Django, nous avons quelque chose appelé les modèles. Et ces modèles sont principalement utilisés pour configurer notre base de données. La plupart du temps dans Django, vous n'avez pas besoin d'écrire une seule ligne de code SQL pour mettre votre base de données en service.

C'est pourquoi nous avons quelque chose que nous appelons Modèle-Vue-Template (MVT). Le modèle est ce que nous utilisons pour notre base de données, la vue est ce que l'utilisateur voit, et le template est l'endroit où se trouve tout ce HTML. À partir du modèle, nous passons simplement toutes nos données dans notre template, vous comprendrez tout cela dans une minute.

Les modèles sont très faciles à configurer, au lieu d'utiliser un code SQL de table de base de données, nous allons simplement utiliser les classes en Python pour construire notre base de données. Pour l'instant, nous allons juste parler des classes et de l'héritage dans la vue, puis plus tard nous allons passer à la façon dont nous allons l'intégrer dans notre base de données.

Allons dans un fichier appelé `models.py`. Et ces fichiers sont toujours situés dans notre application. Ici même dans ce fichier, nous pouvons créer un nouveau modèle. En créant simplement une classe, et ensuite nous pouvons simplement la nommer comme nous voulons la nommer, disons comme... venons ici.

`Features` (fonctionnalités), et ensuite nous pouvons utiliser cela comme ceci. Et ensuite nous pouvons donner à cela un ID qui devrait être un entier. Et nous pouvons avoir le nom de la fonctionnalité, que nous voulons être une chaîne de caractères. Et nous pouvons aussi avoir quelque chose comme les détails, appelons cela `details`.

Ce qui devrait aussi être une chaîne de caractères. Ici même, ce que nous savons est le nom, nous avons un ID et ensuite les détails de la fonctionnalité. Nous avons cela ici même maintenant. Comment pouvons-nous utiliser cela dans nos vues ? C'est aussi très facile, tout ce que nous devons faire est de venir dans nos `views.py`.

Et ensuite ici même dans l'index, ce que nous pouvons faire est de d'abord importer ce modèle de là. On peut dire `from .models import Feature`. Maintenant que nous avons cela importé, ce que nous pouvons faire est de dire, disons, `feature1`. Devrait hériter du modèle `Feature`.

Maintenant que ce `feature1` hérite du modèle `Feature`, nous pouvons maintenant facilement spécifier le détail des attributs de cette fonctionnalité. On peut dire `feature1.id = 0`, et `feature1.name = 'Fast'`. C'est donc une fonctionnalité. Et rappelez-vous que c'est une chaîne de caractères.

Et ensuite nous en avons ajouté un de plus, qui était je pense `details`. Donc `feature1.details = 'Our service is very quick'`. Maintenant nous avons cela ici, ce que nous voulons juste faire est de passer cela dans l'`index.html`. On peut donc dire `feature` devrait être égal à `feature1`.

Si nous venons dans `index.html`, et ensuite nous cherchons cela. Cela devrait être sous le "Get Started" de ceci, descendons tout en haut. "Get Started". Il y a environ une minute. Descendons un peu. Nous devrions voir "Get Started". Et ensuite oui, ici même nous avons ceci.

Au lieu de Lorem ou peu importe ce que c'est maintenant, nous pouvons juste avoir `feature`. C'est la fonctionnalité. Je viens ici et je fais glisser juste à côté de cela parce que j'en ai besoin d'un de plus. C'est la fonctionnalité, on peut dire `feature.name`. Une fois que nous sauvegardons, venons ici et rafraîchissons, ce que nous devrions avoir maintenant est le nom, qui est "Fast".

Attendons que cette page se rafraîchisse. Maintenant vous pouvez voir que ce que nous avons est "Fast", nous n'avons plus ce qui était là. Et ensuite nous pouvons aussi changer les détails de cela. Supprimons tout cela. Et nous pouvons dire `feature.details`. Et ensuite si nous venons ici, et rafraîchissons.

Vous voyez qu'il est écrit "Our service is very quick" comme détail. Maintenant nous pouvons aussi faire la même chose pour tout cela. Ce que nous pouvons faire est de venir dans nos vues. Nous avons donc `feature1`, nous pouvons simplement copier tout cela, coller, coller, coller. Prenons-en deux de plus.

Maintenant changeons tout cela en `feature2`. Et ensuite changeons tout cela en `feature3`. Et ensuite jusqu'à `feature4`. Nous avons donc `feature1, 2, 3, 4`. Et ensuite l'ID devrait être `1, 2, 3`. C'est "Fast". Disons que celui-ci est "Reliable" (fiable). "Easy to use" (facile à utiliser), et "Affordable" (abordable).

Maintenant nos services sont fiables, c'est facile à utiliser, et nos services sont très... nous avons donc `1, 2, 3, 4`. Comment pouvons-nous les passer dans le frontend ? Nous pouvons faire la même chose en faisant quelque chose comme ceci. Nous pouvons changer de `feature` à `feature1`. Et ici nous pouvons simplement dire que `feature2` devrait être `feature2`.

Et ensuite `feature3` devrait être `feature3` et ensuite `feature4` devrait être `feature4`. Et ensuite nous venons ici et y accéd