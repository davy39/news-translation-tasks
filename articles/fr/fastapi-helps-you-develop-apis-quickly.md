---
title: Cours FastAPI – Développez des API rapidement
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-12T13:07:37.000Z'
originalURL: https://freecodecamp.org/news/fastapi-helps-you-develop-apis-quickly
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/fastapi.png
tags:
- name: api
  slug: api
- name: youtube
  slug: youtube
seo_title: Cours FastAPI – Développez des API rapidement
seo_desc: "FastAPI makes it quicker and easier to develop APIs with Python.\nWe just\
  \ published a crash course on the freeCodeCamp.org YouTube channel that will teach\
  \ you how to use FastAPI. \nTomi Tokko developed this course. Tomi has made many\
  \ popular courses bo..."
---

FastAPI permet de développer des API avec Python plus rapidement et plus facilement.

Nous venons de publier un cours accéléré sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à utiliser FastAPI.

Tomi Tokko a développé ce cours. Tomi a créé de nombreux cours populaires à la fois sur sa propre chaîne et sur la chaîne freeCodeCamp.

Voici les sections couvertes dans ce cours :

* Installation et création de votre première API
* Paramètres de chemin
* Paramètres de requête
* Combinaison des paramètres de chemin et de requête
* Corps de la requête et la méthode Post
* Méthode Put
* Méthode Delete

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/tLKKmouUams) (1 heure de visionnage).

%[https://youtu.be/tLKKmouUams]

## Transcription

(générée automatiquement)

FastAPI rend le développement d'API avec Python plus rapide et plus facile.

Tomi vous aidera à comprendre comment l'utiliser dans ce cours.

Salut les gars.

Bienvenue dans ce cours accéléré sur FastAPI.

FastAPI est un framework web moderne, rapide et performant pour construire des API avec Python.

Dans cette vidéo, je vais vous montrer comment vous devez commencer à travailler avec FastAPI.

FastAPI dispose également d'une documentation très bonne et facile à suivre, que je peux également recommander.

Et c'est aussi un excellent framework pour construire des applications web avec Python.

Au cours de ce tutoriel, il y a quelques conseils sur les points clés que vous pourriez vouloir noter.

Mais je l'ai déjà fait pour vous.

J'ai donc créé une feuille de triche FastAPI que vous pouvez télécharger gratuitement en utilisant le lien dans la description ci-dessous.

Et si vous souhaitez plus de tutoriels, d'idées, n'oubliez pas de consulter ma chaîne comme Cody me l'a dit, où j'enseigne davantage sur Python et le développement web en général.

La seule exigence pour ce tutoriel est que vous ayez les connaissances de base de Python et que vous ayez Python installé sur votre ordinateur avec une version minimale de 3.6 ou supérieure.

Avez-vous remarqué, commençons directement cette vidéo.

La première chose dont nous allons parler est donc de savoir comment nous allons installer FastAPI.

Maintenant, pour installer FastAPI sur votre ordinateur, votre ordinateur portable est très facile.

Parce que FastAPI est un framework Python, nous allons utiliser le gestionnaire de paquets Python, qui est Pip.

Vous pouvez donc simplement ouvrir votre invite de commande si vous êtes sur Windows, que vous soyez sur un Mac, ouvrir votre terminal, et nous pouvons simplement taper Python, je pense m pip install fastapi.

Maintenant, il est très facile de simplement faire une ligne de commande, vous devez installer FastAPI.

Vous pouvez également faire Dinamo, nous aimons pip, donc fastapi.

Ou si vous êtes sur un Mac, vous pouvez faire PIP trois install fastapi, juste les commandes d'installation normales.

J'aime donc utiliser Python, par gratuit, juste personnellement, mais vous pouvez l'installer de toute façon.

Donc, cela fonctionne.

Et comme vous pouvez le voir, il dit que la exigence est déjà satisfaite.

Maintenant, si vous travaillez avec Python, vous savez que cela signifie que j'ai déjà cette bibliothèque particulière installée sur mon ordinateur.

Donc, parce que je l'ai installée, elle ne va pas continuer et l'installer à nouveau.

Je vais simplement taper CLS pour effacer cela.

Donc, ce que cela a fait, c'est qu'il a installé FastAPI.

Donc, si vous faites un FastAPI, vous l'avez stocké, vous allez de l'avant et téléchargez certains fichiers ou non, pas seulement FastAPI, d'autres choses que vous allez utiliser plus tard, comme la frappe ou d'autres bibliothèques, cela va l'installer seul.

Et il y a une chose de plus que nous devons installer pour dire, Pip, installez vous vous souviendrez.

Maintenant, la raison pour laquelle nous disons p p.

Donc, vous vous souvenez de ce rappel est ce que nous allons utiliser pour exécuter notre serveur web.

Maintenant, si vous travaillez avec d'autres bibliothèques, comme par exemple, Django, vous savez que Django, vous n'avez pas besoin d'installer une équipe externe pour l'exécuter ou votre serveur web.

Une fois que vous tapez simplement une ligne de commande, si vous avez Django installé, cela va s'exécuter dans un serveur web.

Mais FastAPI est totalement différent.

Parce que travailler avec FastAPI est une bibliothèque très légère.

Donc, vous avez besoin d'une bibliothèque externe pour exécuter ce fichier sur le serveur web.

Donc, cet UV con va nous permettre d'exécuter notre premier projet ou fichier API sur le serveur web.

Une fois que j'appuie sur entrer, maintenant, je devrais également m'attendre à une exigence déjà satisfaite, parce que j'ai cette bibliothèque particulière installée.

Comme vous pouvez le voir, il me dit que l'exigence est déjà satisfaite, les registres ont fermé notre proposition.

La prochaine chose que je veux faire maintenant, la première chose avant de commencer cela, j'ai déjà donné mon dossier par ce répertoire, et puis j'ai créé un fichier Python nommé my api.py.

Et dans mon Visual Studio code, j'ai déjà ouvert le fichier.

Oui, my api.py.

Donc, c'est le fichier que nous allons créer dans nos API qui s'exécutent, tout ce que nous allons faire.

Ce que je veux juste faire, c'est copier ce répertoire particulier pour moi dans mon invite de commande et CD dans celui-ci.

Si j'appuie sur dir, maintenant, vous pouvez voir que j'ai le fichier, juste pour être sûr que nous sommes dans ce répertoire particulier.

Et maintenant que je sais que je suis dans ce répertoire, allons-y et créons notre première API.

Maintenant, la raison pour laquelle je viens d'opter pour ce répertoire est simplement parce que lorsque je veux exécuter ceux-ci sur nos locaux sur notre serveur web plus tard, je dois m'assurer que je suis dans ce répertoire particulier.

Donc, je peux exécuter le fichier dans ce répertoire.

Donc, oh, cela va avoir du sens plus tard.

Mais allons simplement dans Visual Studio.

Maintenant, tout d'abord, importons simplement FastAPI.

Donc, nous pouvons simplement faire import fastapi.

Et si nous sauvegardons cela et venons dans notre ligne de commande et exécutons ce Python, my API spy, donc si cela s'exécute sans aucune erreur, ou quoi que ce soit de ce genre, comme vous pouvez le voir, cela ne nous donne aucune réponse précoce, c'est simplement parce qu'il y a le caissier, la première étape a été installée avec succès.

Donc, fermons simplement cela.

Maintenant, allons-y et créons notre première API.

Maintenant, ce que nous devons faire pour créer notre première API, nous dirons de fastapi, import fastapi.

Exactement.

Donc, cela importe simplement fastapi, comme un objet à utiliser lorsque vous utilisez cet objet, ou une instance de cet objet pour créer nos API plus tard.

Donc, maintenant que nous avons cela importé, nous allons configurer est égal à fastapi.

Nous le prenons de ce fastapi, que nous avons importé pour créer comme une instance de l'objet fastapi, donc nous pouvons évaluer cela plus tard.

Maintenant, cet objet a de nombreux attributs comme le get, laissez-moi faire, laissez-moi entrer dans cela maintenant par quelques autres choses que nous allons utiliser pour créer notre API plus tard.

Donc, maintenant que nous avons cela créé, ce que nous voulons faire est de créer un endpoint.

Maintenant, laissez-moi expliquer ce qu'est un endpoint, un endpoint est une extrémité d'un canal de communication.

Donc, c'est pourquoi c'est si compliqué.

Mais ce que cela signifie simplement pour une API, un endpoint dans une URL, donc disons que nous avons une URL comme sur nos hôtes locaux, slash, supprimer l'utilisateur.

liste si un utilisateur donc pour cette URL particulière, l'endpoint est cette suppression de l'utilisateur.

Donc, c'est comme le chemin dans une URL normale, nous l'appelons le chemin.

Disons que nous avons quelque chose comme amazon.com.

Et puis nous avons quelque chose comme oui, juste supprimer l'utilisateur ou quelque chose comme créer l'utilisateur.

Donc, c'est ce que nous pouvons dire que c'est notre endpoint dans une URL normale.

C'est le chemin, nous traitons avec l'API.

C'est comme notre endpoint pour avoir cela à l'esprit sur chaque endpoint, où vous spécifiez vos URL, faites comme moi, effectuez différentes opérations.

Donc, je vais simplement obtenir une information particulière, une donnée particulière, le magasin pourrait être trop tard, par exemple, cet utilisateur génial, l'endpoint est explicite, il crée un nouvel utilisateur.

Donc, cela signifie qu'il devra publier certaines données à cet endpoint, donc nous pouvons créer un nouvel utilisateur.

Donc, encore une fois, vous allez comprendre cela lorsque nous entrerons directement dans le vif du sujet.

Et il existe différents types de méthodes d'endpoint, de corps de requête, il y en a beaucoup, il n'y en a pas trop, mais il y en a beaucoup, mais les principales sont get, post, put.

Et puis nous avons delete, laissez-moi simplement expliquer cela rapidement.

Donc, le get est utilisé pour simplement obtenir une information ou retourner une information, simplement pour obtenir ou retourner une donnée ou quelque chose de ce genre.

Et puis, bien sûr, cela est simplement pour créer quelque chose de nouveau, et le mettre comme cela avec quelque chose de nouveau, ou créer comme un nouvel objet dans la base de données.

Et donc, ce port est utilisé pour mettre à jour une donnée ou pour mettre à jour quelque chose dans un objet particulier.

Donc, tout cela, encore une fois, vous allez comprendre lorsque nous mettons tout cela en pratique, pour la mise à jour sur Delete est explicite, il est simplement utilisé pour supprimer quelque chose.

Donc, comme je l'ai dit, ces gets sont utilisés simplement pour obtenir ou retourner des données ou des informations, post est pour créer quelque chose de nouveau ou simplement pour ajouter quelque chose de nouveau, input est utilisé pour mettre à jour quelque chose qui existe déjà dans cette base de données particulière, et delete est simplement pour supprimer comme une donnée d'une base de données ou quelque chose de ce genre.

Donc, maintenant que nous avons tout cela connu, j'ai déjà compris tout cela, allons directement à la création de la route HIV, la vraie API.

Maintenant, pour moi de créer une nouvelle API, je vais faire le signe Add up dot get.

Et comme vous pouvez le voir, pour cette API, j'utilise Git, et selon l'explication que j'ai faite il y a quelques minutes, cela montre que je veux retourner une information ou nous voulons simplement montrer une information.

Donc, si je veux, comme faire autre chose, comme posts, put delete, nous allons aussi faire tout cela plus tard dans cette vidéo.

Mais commençons par get laughter, vous dites app dot get une note que cette app provient de l'instance fastapi, que nous avons importée, dites app dot get.

Et puis nous ouvrons une parenthèse à la sortie actuelle slash.

Donc, c'est notre endpoint, notre API à la maison ou à droite slash, cela signifie notre propre et notre propre peut être comme, ce que nous montrons lorsque nous venons simplement à notre propre page, comme google.com fait la page d'accueil.

Donc, quel que soit notre domaine, c'est juste notre propre page, c'est quelque chose comme slash, Bessie comme delete.

Donc, c'est une autre URL, cela peut être google.com slash delete.

Mais maintenant, c'est juste la page d'accueil, juste pour être sûr que vous comprenez cela correctement.

Mais maintenant que nous avons cela, nous allons avoir une nouvelle fonction, nommons cette index, notre propre ou n'importe quoi que nous voulons nommer.

Et le registre Ledger retourne des données particulières, des séries de noms, des chiffres de données.

Donc, ce que cela fait maintenant, comme nous disons que nous prenons de l'application, qui est également prise de l'objet fastapi, pendant des heures dans une méthode get.

Et l'endpoint que vous avez spécifié est la page d'accueil ou l'URL de la page d'accueil.

Et puis sous cela, nous allons simplement avoir une nouvelle fonction, nous pouvons nommer cela n'importe quoi que nous voulons, ce que nous faisons simplement est de retourner ces données particulières.

Maintenant, ce sont simplement des données factices que nous avons saisies.

Mais plus tard, je vais vous montrer comment vous allez l'utiliser comme un dictionnaire Python.

Et oui, normalement lorsque nous retournons des données à écrire en Python, votre réponse.

Cette API fastapi utilise JSON, mais plus tard, donc je vais vous montrer comment utiliser un dictionnaire Python et le convertir automatiquement en données JSON.

Mais pour l'instant, ce sont simplement des données JSON normales qui sont retournées.

Enregistrons ce fichier particulier.

Et exécutons d'abord cela et voyons vraiment ce que nous faisons sur notre serveur web.

C'est là que UV call intervient.

Mais revenons à notre invite de commande.

Tout d'abord, pour pouvoir exécuter ceux-ci, assurons-nous simplement que nous sommes dans le répertoire de ce fichier particulier.

Et pour être sûr, nous appuyons simplement sur dir, puis nous voyons notre fichier, c'est bien.

Maintenant, pour nous exécuter, nous devons appuyer après, c'est le premier dont nous avons besoin pour ajouter le nom du fichier, qui est my api.py.

Le second est le nom de la variable que vous utilisez, la plupart du temps, c'est toujours up.

Et puis il y a essentiellement deux choses, mais le registre dit que nous savons que Ledger's roll cela sur le serveur web, ce que je vais faire maintenant, je vais dire yuvika va laisser un espace.

Et je vais dire my API, qui est le nom du fichier, mais maintenant nous n'écrivons pas sur api.py, nous écrivons seulement le nom du fichier, pas avec l'extension du fichier.

Et puis nous mettrons un deux-points, je dirai up.

Et cela vient de juste ici, qui est la variable que nous donnons à l'instance d'objet de fastapi.

Et puis nous mettons simplement des iPhones, sauvegardons le rechargement.

C'est la ligne de commande de base pour exécuter notre projet fastapi pour notre serveur.

Une fois que nous mangeons, entrez, vous pouvez voir qu'il dit que vous avez exécuté une application PC, le démarrage est complet.

Et il nous donne cette URL particulière.

C'est l'URL qui dit où nous devons aller pour voir notre projet.

Je vais simplement venir dans mon navigateur ici, coller notre URL, appuyer sur Entrée.

Et boom, vous pouvez voir que j'ai nommé les premières données, qui est exactement ce que nous avons retourné ici comme réponse aux nouvelles premières données.

Donc, c'est comment vous pouvez simplement avoir une API très simple.

Maintenant, passez l'API comme une chose très cool que j'aime le plus de tout le monde qui travaille avec fastpay.

Comme, nous avons simplement obtenu la documentation pour générer automatiquement cette belle documentation UI pour votre API.

Si nous allons à slash Docs.

Et nous appuyons sur entrer, CCS fastapi swagger UI.

C'est juste comme une documentation de base pour toutes les API que vous avez sur ces sites comme votre site web, ou comme votre application API, peu importe comment vous voulez l'appeler.

Mais comme vous pouvez le voir, il dit par défaut, nous avons de l'endpoint de l'UI, juste slash.

Et la fonction est index, qui est juste ici, fonction, donnez-le à l'index.

Et comme vous pouvez le voir, en utilisant une méthode get, c'est ce qu'il vous montre, c'est une méthode get, ils génèrent simplement ces, comme une API pour, comme cette documentation pour notre API.

Et nous pouvons tester notre API directement depuis cet endroit.

Mais nous n'avons pas besoin d'utiliser postman ou un service externe pour tester l'API, vous pouvez simplement venir ici, cliquer sur essayer.

Je vais dire qu'il exécute.

Et je viens ici, il me donne simplement la réponse, qui est nommée les premières données de ce qui est fait ici.

Maintenant, nous allons également aller plus loin dans la vidéo et vous montrer comment manipuler toutes ces données très bien.

Mais pour l'instant, c'est simplement la réponse qui est donnée à cette page.

Et bien sûr, si nous allons à l'oh, les étudiants ont la même réponse, donc à ce stade, nous avons parlé de, tout d'abord, nous avons créé notre première API, nous nous sommes assurés d'avoir installé tous nos fastapi, vous vous souvenez de tout ce dont nous avions besoin.

J'ai expliqué, endpoint, ce que sont les endpoints et get post, put, delete, implémenté.

Et encore une fois, nous avons créé notre première API, et nous vous avons également montré comment utiliser la documentation de fastapi.

Donc, c'est essentiellement tout ce qui concerne l'atteinte de notre première API.

Maintenant, parlons de notre paramètre d'endpoint.

Le paramètre de nom est essentiellement utilisé pour retourner une donnée relative à une entrée dans la partie ou dans l'endpoint, essentiellement.

Nous pouvons donc faire cela en utilisant soit une partie soit une requête.

Nous avons donc deux paramètres d'entrée, qui sont le paramètre de chemin et un paramètre de requête.

Je vais vous montrer, illustrer cela maintenant.

Mais tout d'abord, ayons une année comme un nouveau dictionnaire, notre nom est étudiants.

Il est simplement rempli correctement, le jour dense.

Et il y a une clé avec un ID de un, à moins que vous n'ayez cela comme un autre dictionnaire, leçon de nom.

Donnez-vous comme john.

Ce sont les âges de ce C 17.

Il y a une classe encore.

Donc, c'est juste une base, faites que les petites capitales.

C'est juste un dictionnaire Python de base, nous n'avons qu'un champ en Inde, c'est une clé, et c'est la valeur.

Donc, ce que nous voulons faire maintenant, c'est retourner les données de cet étudiant particulier en utilisant l'ID de l'étudiant.

Donc, dans le champ, par clé, disons slash, nous pouvons avoir un paramètre comme slash, c'est alors slash un.

Donc, pendant que vous avez un, cela signifie que vous retournez les données avec l'étudiant, l'ID idéal pour.

Avant d'entrer dans cela, laissez-moi expliquer ce que je veux dire par un paramètre de chemin.

Plus.

Donc, laissez-moi simplement descendre ici.

Disons que j'ai un site web comme google.com, slash, et ils ont un étudiant, alors c'est juste l'URL de base pour obtenir un étudiant.

Et il peut simplement me montrer toutes les données que nous avons dans ce dictionnaire.

Mais voyons comment obtenir seulement un étudiant spécifique comme cette date, qui a l'ID de un, et je peux ajouter un autre endpoint.

Mais maintenant, cet endpoint sera dynamique, ce sera comme un paramètre que l'utilisateur saisit, ce sera quelque chose comme slash, puis peut être un, puis lorsque nous allons à cette URL, c'est l'utilisateur qui a l'idée de Wanda qui sera retourné à son utilisateur comme l'idée de deux.

Donc, annulons cela et allons directement dans le vif du sujet.

Donc, nous avons cet objet ici.

Et puis ce que nous voulons faire ici dans app dot get place tout d'abord, avoir un nouvel endpoint, app dot get aussi pourquoi n'utilise-t-il pas I get, et cette fois-ci, disons get student.

Maintenant, nous avons ce nom d'endpoint get to them.

Et nous mettrons slash à nouveau, je veux maintenant prendre un paramètre dummies, je veux prendre un ID de ce qu'un utilisateur devrait saisir.

Le premier à faire cela, nous utiliserons les accolades, et ils diront student underscore ID.

Cela nous dit simplement que l'ID précédent est énorme, il sera essentiellement collecté.

Et maintenant, ils Jeff, cela crée dans la fonction normale de Cassie gay student.

Maintenant, rappelez-vous ici, c'était juste vide en euros, pas en Inde, mais maintenant nous collectons students ID underscore ID.

Et cela devrait être équivalent à ce que vous mettez ici.

Cela fait ce qu'il vient d'être collecté.

Et nous devons spécifier le type de données de cela, qui est notre entier, donc l'ID devrait être notre entier maintenant, ou nous pouvons simplement faire est de retourner les étudiants.

Nous retournons les étudiants, qui est de l'année est dans l'ID de l'étudiant.

Donc, laissez-moi expliquer cela.

Une fois de plus, ce que cela fait maintenant, c'est que nous avons ces adultes invités slash guest today, slash why now why n'est-il pas dans les accolades, c'est bien comme une variable mpg comme une variable dynamique.

Donc, ce que vous entrez ici est ce qui sera utilisé pour obtenir l'étudiant.

Donc, d f, get student there now, initialisant la chose student ID que nous donnons est comme un type de données de int, cela signifie qu'il ne doit pas être une chaîne ou une valeur booléenne, il doit être un entier.

Et puis nous disons simplement retourner les étudiants qui retournent l'étudiant avec l'ID de l'étudiant.

Mais ce que je veux dire par cela, vous savez, dans un dictionnaire Python normal, si nous voulons simplement retourner ces étudiants, parce qu'il a une clé de un parce que les étudiants veulent.

Et cela va simplement retourner la valeur de celle-ci.

Mais puisque un doit être dynamique, je veux que vous fassiez ce que l'utilisateur entre, nous changeons ce un en l'ID de l'étudiant, peu importe ce que l'utilisateur entre, la clé de cela est ce qui devrait être, et non, disons que l'utilisateur entre comme cinq, et nous savons que cela ici, va simplement vous donner comme le canal trouvé ou quelque chose de ce genre.

Donc, sauvegardons cela.

Tout d'abord, allons simplement tester cela.

Si nous revenons ici, et rafraîchissons cette page.

Maintenant, vous pouvez voir que nous avons un grand invité étudiant.

Et au lieu de connaître les noms sont Roscoe ID qui m'appelle utilise les étudiants ID est requis.

Cela signifie que nous pouvons simplement tester cela, je dis exécuter le nous essayer et exécuter T, il dit que nous devons entrer quelque chose ici.

Maintenant, nous mettons un, je dis exécuter.

Nous voyons maintenant que cela nous donne une réponse de nommé john 17.

Sur l'année deux, c'est essentiellement celui-ci ici.

Donc, si nous venons ici maintenant, et que nous essayons de mettre quelque chose qui n'est pas comme trois, je dirai exécuter.

Vous voyez l'ISIS interne enquête Rodas parce qu'il n'y a pas de détail comme le, bien sûr, allons directement au répertoire URL, nous disons get student finish student puis slash one.

Vous voyez maintenant que nous avons john age, nous avons simplement les données de base qui procèdent à une erreur interne du serveur.

Retournez aux docs, les docs, de quoi s'agit-il essentiellement le paramètre de chemin, nous pouvons l'enrichir, nous pouvons ajouter plus de détails.

Ou nous pouvons dire, par exemple, nous pouvons le rendre obligatoire.

Donc, laissez-moi revenir ici.

Disons que nous voulons ajouter plus de détails à cet identifiant d'étudiant, comme, vous savez, lorsque nous servons cette API à un utilisateur, l'utilisateur manuel est vraiment bon comme vous nommez vraiment cet identifiant d'étudiant, nous disons simplement student ism, je comprends ce que c'est, devons-nous passer le nom de l'étudiant, ou l'âge de l'étudiant ou la classe ou l'ID.

Donc, si nous n'avons pas de surface financière, nous pouvons utiliser quelque chose dont nous avons besoin pour importer.

Et cela va nous permettre d'avoir une description de cela que l'utilisateur peut savoir quoi entrer.

Mais tout d'abord, venons ici et entrons path.

Pour dire que nous n'avons pas besoin d'avoir un dialogue, nous pouvons simplement appuyer sur la virgule, entrer path, parce que c'est de fastapi, entrez dedans.

Donc, maintenant que nous avons des parties importées, nous pouvons simplement dire student ID, ci-dessous int égal à deux, puis nous pouvons dire path.

Tout d'abord, nous dirons none.

Maintenant, ce non est donc, si l'étudiant, si la personne n'entre rien, il va simplement le laisser vide ou ne va pas une fois que l'Iran est simplement va comme apporter des données vides.

Juste pour attraper l'erreur.

Rappelez-vous, lorsque nous l'avons fait l'année dernière, lorsque nous avons essayé d'obtenir sans entrer quelque chose, il nous a simplement dit que nous devons entrer quelque chose.

C'est simplement ce que cela fait.

Et maintenant, nous pouvons ajouter une description.

Maintenant, dans cette description, nous pouvons faire quelque chose comme nous voulons l'ID de l'étudiant.

Vous voulez voir cela.

Donc, c'est simplement la description que nous lui donnons.

Et une fois que nous avons cela, si nous l'enregistrons et rappelons notre code ici.

Et essayons simplement de rafraîchir la page pour rafraîchir les chiens.

Et puis nous disons get student.

Non, parce qu'il écrit en distribution.

Il dit l'idée de cet étudiant que vous voulez dire, juste plus, nous donnant plus de description ou plus de détails de ce que nous voulons vraiment collecter.

Ce que vous avez également plus d'attributs n'est pas seulement cela revient à notre code, nous avons plus d'attributs dans ce chemin, nous avons des attributs comme moins de deux, laissez-moi simplement descendre ici et l'expérimenter.

Mais nous avons moins que gt GT, cela signifie simplement supérieur à, c'est explicite, nous avons moins que, nous avons D, qui est supérieur ou égal à, nous avons également LD, qui est inférieur ou égal à.

Donc, cela nous dit simplement que puisque nous collectons un entier, nous pouvons spécifier si l'entier que nous voulons collecter ne doit pas être supérieur à 50, ou ne doit pas être inférieur à un ou zéro ou quelque chose de ce genre.

Disons que nous ne voulons pas que notre entier soit supérieur à zéro.

Mais nous voulons qu'il soit supérieur à zéro, donc il doit être supérieur à zéro.

Enregistrons maintenant, nous revenons ici, nous rafraîchissons.

Maintenant, essayons cela ici.

Disons que nous essayons d'utiliser zéro et disons exécuter le nous donne cette erreur disons, assurez-vous que la valeur est supérieure à zéro.

Mais c'est parce que nous avons spécifié en jaune, nous ne voulons pas qu'il soit inférieur à zéro, il doit être supérieur à zéro.

Et nous pouvons également ajouter à, disons que nous voulons que vous soyez supérieur à zéro, mais inférieur à, inférieur à, comme trois.

Cela signifie que le nombre doit être de un à deux.

Donc, si nous allons contre l'une de ces règles, pour moi encore, dans le bouton de rafraîchissement, et ici, nous avons essayé le disons que nous faisons trois appuie sur un traumatisme aigu, nous donne une erreur, nous disons assurez-vous que la valeur est inférieure à trois, quand je fais deux, cela va nous donner une erreur interne du serveur, car cette donnée n'est pas trouvée, il n'y a pas de donnée avec la clé de deux avec un, vous savez, nous avons cette donnée ici.

Ici, nous venons simplement ici, la clé de un à venir ici.

Maintenant, vous voyez que cela nous donne une donnée qui est notre nous pouvons simplement ajouter plus de valeurs.

Ou nous pouvons oui, nous pouvons ajouter plus de valeurs et de détails à cette API particulière.

Maintenant, parlons des paramètres de requête.

La requête est utilisée pour passer une valeur dans une URL qui est assez similaire au paramètre de chemin.

Laissez-moi expliquer cela à nouveau rapidement.

Maintenant, dans une URL, comme je dis, google.com, slash, et nous avons des résultats.

Maintenant, lorsque nous avons ce point d'interrogation, puis nous avons un nom de variable égal à quelque chose comme Python.

Maintenant, dans cette URL, le paramètre de requête est cette recherche égale à Python.

Donc, cela nous donne simplement une clé et une valeur.

Donc, c'est le nom de la variable que nous passons indéfinie est très, très, très similaire au paramètre de chemin, ici.

Et le paramètre de chemin, vous savez, nous avons un nom d'ID d'étudiant, ou nous avons une valeur de ce que l'utilisateur entre, c'est simplement notre qui est zéro.

Donc, nous pouvons avoir une URL, puis au lieu d'avoir slash ou quelque chose pour, vous savez, être sur cet endpoint, pour l'instant, c'est simplement avoir une requête attachée à cet endpoint.

pour avoir cela dit, allons directement à l'utilisation de ceux-ci en pratique, ce que je veux faire maintenant, c'est que je veux créer une nouvelle personne, un nouvel endpoint, je dirai app dot get aussi.

Et puis, disons slash get, je pense par le vouloir obtenir les données de l'étudiant par le nom, ici, nous obtenons par l'ID de l'étudiant pour la différence entre le paramètre de requête et le paramètre de chemin est que dans le paramètre de chemin, nous devons ajouter ce que le paramètre veut collecter dans l'URL dans l'endpoint ici.

Lorsque le paramètre de requête, nous n'avons pas besoin de faire cela.

Ou nous devons simplement faire venir à notre fonction.

Ce feu de fonction, je dis get student.

Et puis nous dirons simplement, le nom est une chaîne.

Donc, ici, c'est très similaire.

Vous le voyez dans le chemin avec l'ID de l'étudiant est égal à un entier.

Mais nous avons déjà défini notre ID d'étudiant dans l'URL.

Mais ici, nous n'avons défini aucune équipe, mais nous venons maintenant dans la fonction et la définissons.

Donc, une fois que vous voyez quelque chose comme est-il prêt, le prend comme un paramètre de requête.

Et puis une fois que nous avons cela, je vais simplement à ces données particulières.

Et maintenant, une fois qu'un utilisateur vient à cette URL et fait quelque chose comme cela, je dirai nom égal à john, nous voulons obtenir les données là-bas comme le nom de john, à ces tâches maintenant, et j'utilise une boucle for et je dis pour un étudiant, ID, étudiant.

Si les étudiants étaient des crochets, ID de l'étudiant, nom.

les postes sont le nom qui a été passé.

Et ce que nous voulons simplement faire, c'est retourner à la danse.

Cet étudiant particulier ID, aucun de cela n'est simplement retourner.

Données.

Pensée.

Ce que cela fait, c'est, tout d'abord, parcourir les valeurs que nous avons dans cette année des étudiants dans la clé des étudiants ID.

Dans cet étudiant, nous disons si les étudiants ont cet ID d'étudiant, le nom de celui-ci est parce que avec le nom qui a été passé, laissez-moi expliquer son volonté de nous parcourons cet ID d'étudiant en utilisant tandis que parcourons ce dictionnaire d'étudiants en utilisant l'ID des étudiants.

Et cet ID de Jeanette est celui-ci.

Donc, nous pouvons nommer cela n'importe quoi ici, nous pouvons simplement dire ID n'importe quoi que nous ne voulons pas nommer.

Mais si je dis ID pattern, il voit automatiquement cela comme un mot-clé.

Donc, je vais simplement mettre un ID d'étudiant pour qu'il soit original.

Donc, maintenant, nous le parcourons en utilisant ceux-ci, je vais dire si l'étudiant avec cet ID d'étudiant, le nom de celui-ci est égal au nom qui est en cours de passage, ils veulent retourner cet étudiant particulier.

Si ce n'est pas le cas, vous dites simplement que les données sont introuvables.

Maintenant, pour faire un paramètre de requête, allons simplement le tester.

Revenons ici.

Maintenant, c'est bien.

Donc, maintenant, nous avons des invités par nom, ou nous voyons encore nous sommes nom requis.

Nous pouvons simplement, vous savez, nous disons john, une fois que nous exécutons cela, cela devrait fonctionner.

Donc, comme vous pouvez le voir maintenant, il s'appelle john, parce qu'il obtient cette valeur par les données avec le nouveau module où nous essayons quelque chose comme disons, une équipe.

Nous exécutons, allons dire que les données sont perdues, parce que nous n'avons aucune donnée à droite dans l'année avec le nom de l'équipe.

Donc, c'est essentiellement comment créer un paramètre de requête très simple et rapide dans FastAPI.

Maintenant, pour rendre ces paramètres de requête optionnels, nous pouvons le faire, c'est très simple.

Disons que nous voulons simplement le rendre optionnel.

Comme nous ne voulons pas l'exiger, vous voyez que cela dit qu'il est requis ici.

Rendons cela optionnel maintenant.

Nous pouvons simplement dire nom, ici dans cette chaîne Kathy égale à non égale à non est plus requis, nous pouvons aller année.

Donc, les chiens disent toujours get by name, Katsina, il ne dit plus da requis.

Cela signifie que nous pouvons essayer cela va nous donner une erreur ou quelque chose.

Ils disent simplement que les données sont introuvables.

Mais maintenant, ce n'est plus requis.

Maintenant, c'est une façon de le faire.

Mais la meilleure pratique est d'utiliser l'option par défaut maintenant, la méthode que fastapi est pour nous.

Pour nous utiliser ceux-ci, ce que nous devons simplement faire.

Tout d'abord, nous viendrons ici, c'est très facile, nous disons simplement optionnel.

Et puis égal à connu.

Cela va simplement le rendre optionnel pour nous.

Mais avant de pouvoir utiliser cela, nous devons nous assurer de mettre cette option maintenant, ils de la frappe importent l'option.

Cela est simplement pour en faire la meilleure pratique.

Parce que ces faits épidémies recommandent que si nous avons besoin de documentation, faites-le également de la manière normale ou simplement de l'autre manière, pas de la manière normale.

C'est la manière normale.

Nous pouvons donc également le faire de cette manière pour garder les choses simples.

Nous voulons simplement que vous ayez un code propre et un code plus lisible comme les points principaux pour le rendre plus lisible.

Nous pouvons également utiliser cela, donc non, cela va être comme, non requis, cela va être optionnel.

Donc, maintenant, disons que nous voulons ajouter un autre paramètre de requête dans l'éloquent pour avoir deux paramètres de requête.

Comment faisons-nous cela ? Je vais vous montrer quelque chose.

Oui, mettons simplement une virgule, je dirai testons-le.

Donc, nous avons simplement un paramètre de requête de JSON est un entier.

Donc, si j'essaie d'exécuter cela, nous devrions obtenir une erreur.

Et je vais vous montrer pourquoi nous avons cette erreur, maintenant.

Laissez-moi m'appeler pas ici, un navigateur.

Donc, d'accord, vous pouvez voir que ce n'est même pas en train d'aller si je viens ici.

Maintenant, vous voyez des dés de syntaxe d'erreur, un argument non par défaut, suit un argument par défaut.

Donc, ce que cela dit simplement, c'est que nous avons, comme vous pouvez le voir, ici, nous avons nommé optionnel.

Et puis nous avons test, qui est optionnel.

Donc, Python ne nous permet pas d'avoir comme, un argument optionnel avant, un argument requis.

Donc, le dos de couverture est rapide, c'est à propos de Python qui ne nous permet pas simplement parce que Python est une langue écrite.

Donc, nous devons également nous en tenir à Python.

Si nous descendons ici, une chose que nous pouvons faire est de simplement changer de place comme des changements, ou de l'amener ici ou quelque chose, nous pouvons aussi faire cela.

Mais la meilleure façon de le faire, donc nous pouvons avoir un nombre limité de paramètres de requête et les avoir où nous voulons.

C'est très facile, ce que nous pouvons utiliser pour dire asterik sa, coma.

Donc, une fois que nous avons ceux-ci, nous pouvons maintenant l'écrire si nous avons un paramètre par défaut ou optionnel, ou quoi que ce soit requis va fonctionner puisque nous avons cela maintenant.

Va pouvoir prendre soin de tout ce qui vient après.

Ne m'appelle jamais dessus, rafraîchis.

Cela devrait fonctionner.

Eh bien.

Regardons, avons-nous un rechargement ? Oui, nous venons, vous savez, elle est prête à recharger.

Et cela devrait fonctionner.

Maintenant.

Donnons-lui un autre essai.

D'accord, cela prend un certain temps pour recharger, nous ne devrions pas.

Mais c'est simplement comment résoudre cette erreur particulière, ou lorsque vous avez un paramètre optionnel avant un paramètre de requête requis.

Donc, j'espère que vous comprenez ce concept.

Maintenant, parlons de la combinaison des paramètres de chemin et de requête ensemble.

Maintenant, parfois vous pourriez vouloir faire cela, eh bien, la plupart du temps, vous pourriez ne pas.

Disons que vous voulez obtenir deux valeurs différentes d'un utilisateur, comme disons son ID et son nom, ou la classe ou autre chose, vous pourriez vouloir combiner un paramètre de requête avec un paramètre de chemin.

Tout d'abord, pour faire cela, vous savez, ici, nous avons déjà un paramètre de requête de nom et de test, la longueur du paramètre de chemin, appelons-le également l'ID de l'étudiant, le slash K, students underscore ID.

Et puis puisque nous définissons les initialiseurs, à net ID dans le chemin, et nous venons également ici, et puis disons, dent underscore ID, et puis nous lui donnons int, j virgule.

Donc, puisque nous avons eta ici, c'est un paramètre de chemin, qui n'est que dans la fonction, c'est un paramètre de requête.

Donc, c'est simplement la différence de base dont vous devez prendre note.

Donc, nous sommes entre ces deux endroits, cela.

Donc, maintenant, nous pouvons simplement tester cela facilement ? En fait, même lorsque nous collectons les étudiants, Id un organisateur pour autre chose ? Oui, parce que tout ce que nous faisons est essentiellement de l'obtenir par le nom.

Mais c'est simplement comment vous pouvez combiner un paramètre de requête avec nous, revenons ici.

Maintenant.

Nous appuyons sur Entrée.

Donc, si nous disons get, non, ce n'est pas ce dont nous avons besoin.

Nous voulons obtenir par nom.

Nous disons get non, vous voyez que nous sommes nom test.

Nous devrions également avoir des étudiants ID pour rayer comme la clé.

Si nous revenons ici.

Did I okay, nous n'avons pas sauvegardé notre fichier.

Assurons-nous de sauvegarder notre fichier, canards, maintenant nous avons student ID qui est également requis.

C'est simplement le concept de base de la combinaison d'un paramètre sur un paramètre de requête ensemble.

Cette partie, nous allons parler du corps de la requête et de la méthode POST.

Donc, ce que c'est, c'est comme l'information ou les données passées lors de la création d'un nouvel objet en utilisant la méthode POST.

Maintenant, pour faire cela, tout d'abord, importons quelque chose ici pour la base.

Donc, disons de la base de downtick import base model, juste pour être plus élaboré.

Le corps de la requête est comme les données passées lorsque vous voulez créer un nouvel objet ou une nouvelle donnée de t.

Donc, je vais expliquer cela plus tard, comme, vous allez voir de quoi nous parlons, vous n'avez pas besoin de connaître la définition ou autre chose, juste de savoir comment l'utiliser dans un cas pratique.

Donc, maintenant que nous avons cette base, Moodle importer, nous allons créer une nouvelle classe.

Et cette classe, nous voulons simplement qu'elle soit similaire au dictionnaire des étudiants, et nommons la classe étudiant, allons prendre de la base Moodle, ayons un nom qui devrait être une chaîne, un âge et utilisons cela comme un entier.

Et puis ils ont une classe.

Maintenant, j'aurais aimé avoir une classe boy, Cassie l'a vue comme un mot-clé.

Donc, changeons cela en quelque chose comme l'année, l'année de l'étudiant et cela devrait être une chaîne aussi, ils m'appellent simplement Mr.

of class ici.

Donc, nous pouvons l'utiliser, vous savez que nous avons cela, ce que nous pouvons simplement faire, nous voulons créer un nouveau chemin maintenant.

Mais cette fois-ci, nous allons utiliser une méthode POST.

Tout d'abord, pour faire cela, simplement similaire à dire arts app dot post proposé.

Et maintenant, nous allons dire créer des étudiants maintenant, nous voulons créer un nouvel objet d'étudiants, nous allons prendre un paramètre de chemin, ou étudiants ID, je sais ce que nous faisons, lorsque nous prenons un paramètre de chemin, nous devons définir cela dans la fonction.

Donc, créer, souligner, le bureau.

routeur, définir notre étudiant souligner ID comme un entier.

Et ce que vous voulez spécifier ensuite, c'est l'étudiant.

L'étudiant sait ce que c'est, c'est essentiellement les détails que l'utilisateur soumet.

Donc, afin de créer un nouvel objet d'étudiants, en utilisant cette classe particulière, pour connaître les détails, disons les détails, le nom que l'utilisateur m'a vu, l'âge et l'année est ce qui sera sauvegardé dans cet étudiant.

Donc, nous voulons que cela soit parce que ce modèle d'étudiant, vous pouvez voir que celui-ci avec une lettre minuscule et une lettre majuscule.

Donc, c'est ce qui est vraiment différent.

Donc, comme une valeur clé, mais maintenant que nous avons cela, allons directement dire, si l'ID de l'étudiant qui a été passé.

Dans les étudiants, ce que nous voulons simplement faire, c'est dire, retourner comme une erreur, dire que l'étudiant existe.

Donc, cela signifie que si l'ID de l'étudiant est déjà dans les étudiants, et l'ID de l'étudiant ici, alors ce que nous faisons simplement, c'est de dire retourner une erreur, cela signifie que l'historique existe déjà, endommageant le béton, le même étudiant avec un étudiant avec le même ID deux fois.

Ce qu'il ne fait pas le cas, Justice students.

Dans l'ID de l'étudiant est égal à l'étudiant, je vous dis que l'étudiant est ce que l'utilisateur a diffusé ou soumis en utilisant ce métal de poste, mais maintenant que nous avons cela, nous avons créé un nouvel objet d'un étudiant.

Et puis nous pouvons simplement retourner les étudiants de cet ID d'étudiant.

C'est simplement le code dont nous avons besoin pour cela.

Avant de tester ce code, ou laissez-moi expliquer ce que nous avons fait dans ce code, encore une fois, ce que nous faisons dans le registre ci-dessus, nous prenons un paramètre de chemin d'un ID.

Donc, c'est un paramètre de chemin avec tous les détails de l'étudiant, et ils utilisaient cela pour créer un nouvel objet d'étudiant.

Donc, allez simplement de l'avant et testez ce code pour sauvegarder le Permian.

ducks.

Maintenant, vous pouvez voir que nous avons des posts, pas de get plus de grands étudiants, notre ID d'étudiant est requis.

Et ils peuvent voir qu'il dit que le corps de la requête est également requis.

C'est ce dont j'ai parlé.

J'ai parlé du corps de la requête, c'est essentiellement les détails comme le nom, le doctorat, l'année, il a besoin d'ordres, essayons-le.

Un de nos étudiants doit avoir deux, bien que nous disions, disons simplement, Tim, donnez à Tim l'âge de 12.

Voir neuf.

Maintenant, si je l'exécute, je vois maintenant qu'il vient de me donner la réponse de ce que je viens de créer.

Mais maintenant, nous avons un ID d'étudiant de deux, si je l'appelle pour obtenir par l'ID de l'étudiant, alors allons simplement obtenir les étudiants en utilisant l'ID, nous devrions aimer cela maintenant sûr.

Donc, disons pour dire exécuter.

Maintenant, nous pouvons voir que nous avons cette équipe, avec des données factices, elle a été sauvegardée ici.

Mais une chose à propos de cela, c'est qu'elle est sauvegardée dans une mémoire.

Donc, si nous rafraîchissons cette page, cela a disparu.

Mais vous savez, nous travaillons avec des applications du monde réel, vous voulez sauvegarder comme votre base de données ou quelque chose de ce genre.

Donc, vous pouvez voir que nous avons créé un nouvel objet de cela maintenant.

Et puis nous utilisons simplement le get pour obtenir cette URL, si nous voulons lire ce qui existe déjà comme vrai, et vouloir le créer à nouveau, laissons exécuter, nous disons dit erreur étudiants existe déjà, nous ne pouvons pas créer avec le même ID deux fois, ce qui est bien à ce sujet ? Revenons à notre code.

Donc, c'est essentiellement comment nous pouvons simplement utiliser la méthode POST et le corps de la requête pour créer un nouvel objet dans votre nouvel objet dans nos données dans notre base de données, essentiellement.

Parlons de la méthode des ports.

Comme je l'ai expliqué plus tôt, dans ce tutoriel, la méthode put est utilisée pour mettre à jour quelque chose qui existe déjà.

Donc, pour faire cela, tout d'abord, ayons un nouvel endpoint policy up these goods.

Cette fois-ci, nous allons dire patch update.

affaires aujourd'hui étudiant et ils veulent collecter l'ID de l'étudiant.

Donc, nous connaissons l'étudiant que nous mettons à jour.

Maintenant, ayons une fonction disant date.

Student nous devons également nous défendre aujourd'hui et ID comme un entier.

Maintenant, les étudiants sont très similaires à ce que nous avons fait ici, nous savons que nous collectons.

L'avantage va à cet étudiant.

Maintenant, je veux expliquer quelque chose.

Donc, ici, vous pouvez voir qu'il dit à cela à cause de studio.

Mais lorsque nous publions ces données de publication à cette URL, je vais dire que cet étudiant est égal à l'étudiant, tout doit être essentiellement tous les champs dans le compositeur.

Donc, vous venez ici maintenant.

Et nous donnons un champ de nom et nous ne donnons pas de champ d'âge, cela ne va pas fonctionner si nous utilisons le module des étudiants pour la mise à jour.

Donc, nous devons créer un nouveau modèle, mais cette fois-ci, pour rendre tout cela optionnel.

Donc, la raison de cela est que lorsque l'utilisateur veut mettre à jour une valeur, il ne veut mettre à jour que le nom et non l'âge, il ne veut mettre à jour que l'année et non le nom d'un nouveau corps que nous utilisons cette classe d'étudiant pour la méthode de mise à jour.

Aussi.

Le scénario est que l'utilisateur doit entrer toutes les données complètes, ce qui signifie qu'il doit changer les données audio chaque fois qu'il veut mettre à jour quelque chose, ce qui n'est pas une bonne pratique.

Laissez simplement tranquille et créez.

Plus notre nom est update.

Student et cela prend également de la base model.

Même chose nom.

Maintenant, nous allons dire optionnel.

Formé personne juste pour le rendre optionnel.

Faire la même chose pour l'âge.

Optionnel, formé entier personne et puis exactement simplement pour la classe ici, nous utilisons l'année optionnelle et c'est une chaîne égale à non maintenant, nous pouvons utiliser cela de ce modèle d'étudiants comme référence ici.

Donc, ces notes ce soir encore ces objets aujourd'hui maintenant avec chacun d'eux est optionnel, voyez que nous utilisons I donne seulement une valeur, les autres valeurs peuvent encore rester les mêmes, c'est très bien.

Et maintenant, ce que nous voulons simplement faire, c'est dire si l'ID de l'étudiant n'est pas dans l'étudiant, nous allons dire retourner une erreur comme cet étudiant particulier n'existe pas ou quelque chose du monde, cela va, laissez-moi écrire cela rapidement, bien que cela sous les étudiants n'existe pas, ce que cela fait, c'est tout d'abord vérifier si l'ID de l'étudiant n'est pas un étudiant, le dommage si l'ID qui a été passé à ce que nous faisons, c'est si nous voulons mettre à jour cet étudiant aujourd'hui, nous allons passer l'ID de l'étudiant puis ce que nous voulons mettre à jour.

Donc, il va d'abord vérifier si l'ID est présent dans les étudiants, ne sera pas présent, il vous donnera l'étudiant n'existe pas aujourd'hui.

Vous mettez également à jour n'existe pas, au moins vous devez avoir un étudiant avant de pouvoir mettre à jour ces données.

Nous devons vérifier cela d'abord.

Mais si cela existe, nous pouvons simplement faire quelque chose comme les étudiants n'ont pas ID égal à l'étudiant et puis maintenant nous pouvons simplement retourner l'étudiant, c'est exactement la même chose que nous avons fait ici, danse ID exactement ce que je vais vous montrer où la flèche est dans ce particulier n'est pas une flèche mais où le toucher est si nous venons près de maintenant sur les jours de test, vous voyez le bouton de rafraîchissement maintenant, vous pouvez voir que c'est le put, nous avons la méthode put et non, essayons d'abord de créer un nouvel étudiant, donc directement cela, nous créons avec deux, disons Team 12 nine maintenant, nous exécutons cela, nous avons de nouveaux objets ou de nouvelles données ou le contrepartie veut mettre à jour cet étudiant.

Donc, essayons-le.

Et quoi de neuf, JD étudiants avec l'ID de deux, qui est l'équipe, quand je veux changer le nom en Tom, pas l'équipe, nous n'avons pas besoin de l'âge ou des données factices, cette option aussi, nous ne voulons pas qu'il ne sache pas quoi faire.

Si nous exécutons cela maintenant, vous verrez ce qui va se passer.

Donc, maintenant, il dit nommé Tom, âge non, oui, non, parce que nous n'avons pas spécifié cela, il dit non.

Ils sont allés jusqu'à obtenir votre étudiant par ID et je veux simplement obtenir cet étudiant dans un exécuter, ce qui va se passer maintenant, vous pouvez voir qu'il ne montre même pas l'âge à nouveau.

Il ne montre pas qu'il a 12 ans.

Le est en année neuf.

Donc, il a été écrasé, donc parce que nous n'avons pas fourni cet âge sur l'année lorsque nous le mettons à jour, il l'a également écrasé comme non, dommage n'a pas de valeur.

Et cette flèche vient parce que nous avons simplement fait des étudiants avec nous aujourd'hui, Id est égal à l'étudiant, il doit savoir ce que l'utilisateur passe.

Donc, puisque nous n'avons rien passé, il a simplement mis à jour notre étudiant qui a déjà une valeur de cela, il n'a rien, ce qui est, mais le premier soin de cela, nous allons devoir le faire de manière manuelle pour venir ici pour dire si un étudiant, le nom n'est pas posté, non, les nombres si il y a quelque chose dans ce que l'utilisateur a passé, alors il ne veut pas le mettre à jour, disons à la danse.

Dance ID fait le nom sera mis à jour à l'étudiant.

Celui-ci fait le nom est exactement le genre de code que nous voulons utiliser, je vais aussi faire la même chose pour l'âge et la classe ou l'année, l'ève étudiant que l'âge n'est pas égal à aucun.

Voir, la danse avec un ID d'étudiant, l'étudiant particulier fait l'âge égal à la dent.

Mais ah, maintenant, la dernière fois, nous allons devoir le faire pour l'année, c'est ici, maintenant égal à aucun, je veux dire, vous nous donnez une valeur vide, alors c'est la seule fois où nous voulons maintenant mettre à jour ce type de données, cette valeur particulière, mais une clé particulière, donc vous ne nous donnez pas quelque chose, nous ne allons pas le mettre à jour.

Quand vous nous donnez quelque chose, nous allons le mettre à jour, puis à une année.

C'est simplement le code pour prendre soin de cette erreur.

Donc, maintenant, nous sauvegardons cela.

Maintenant, c'est très bien, parce que nous avons pris soin de cette erreur particulière.

Et maintenant, allons simplement de l'avant et revenons dans votre et puis nous mangeons frais, cela.

Génial, mais ce que nous voulons faire tout d'abord, c'est créer un nouveau dent à lui.

Les deux oui ou non.

Laissons exécuter.

Et maintenant nous avons cela, venons à nos sorties et mettons à jour cette équipe.

Pour l'instant, nous voulons qu'il ait 15 ans, laissez ce nom vide.

Eh bien, maintenant l'âge voulait être 15.

Donc, vous pouvez voir que maintenant nous n'avons pas passé le nom ou l'année.

Mais si cela s'exécute, seulement, alors voyons où vient l'erreur, cela attend un nom de code d'intervalle correct.

D'accord, donc il veut que cela soit en double cordial parce que c'est des données JSON.

Faisons cela ou exécutons.

D'accord, surtout un nom d'intervalle de code incorrect.

D'accord, cela nous donne une erreur enclose dans des guillemets.

Regardons.

Maintenant, laissez-moi vous dire d'où vient la flèche, si vous n'avez rien après, comme vous avez une autre valeur ici, quelque chose, retirez simplement cette virgule, nous n'en avons pas besoin en fait, nous ne devrions pas en avoir besoin parce qu'un entier pour vous assurer que vous n'avez pas de virgule à la fin s'il n'y a pas assez à lire.

Donc, maintenant, appuyons sur exécuter.

Et si nous venons ici maintenant, vous voyez qu'il n'y a que 15 qui a été mis à jour et allumé à 15.

Mais seulement 15 a été mis à jour.

Maintenant, nous avons une équipe, une belle intacte.

C'est ce que nous voulons, nous pouvons aussi le faire à nouveau.

Et maintenant, nous pouvons simplement mettre à jour notre nom.

Et nous voulions notre nom.

Maintenant, être Tom.

La procédure d'exécution, nous avons maintenant Tom, âge de 15.

année sur année neuf, c'est exactement ce que nous voulons.

Si nous revenons, vous savez et essayez d'obtenir à ne pas essayer.

Essayons de le faire, vous pouvez voir que nous avons le nom de la chanson qui fonctionne parfaitement, l'âge et l'année.

C'est exactement ce que nous voulons obtenir.

C'est notre objectif principal.

Je viendrai aussi ici pour obtenir par nom.

Testons cela.

Donc, essayons-le.

Nous devons avoir le nom de Tom.

Et comme je l'ai dit, cela peut être n'importe quoi parce que nous ne l'utilisons pas.

Si nous exécutons cela maintenant, cela nous donne une erreur interne du serveur, car bien sûr, cela ne le fait pas.

Cela ne le fait pas.

Maintenant, il y a donc, voyons slash au nom de la chanson et test 32.

Donc, la raison pour laquelle c'est parce que nous avons définitivement changé certaines valeurs ici, un certain code ici, où nous avons commencé à obtenir pour prendre soin du litre.

Mais maintenant, c'est essentiellement comment nous pouvons simplement mettre à jour certaines données dans notre base de données si nous utilisons des données réelles.

Ce n'est pas comme une mémoire ou comme je dirais un cookie parce que les cookies dans le navigateur ou est-ce comme une mémoire une fois que nous rafraîchissons ou comme une session une fois que nous rafraîchissons, cela a disparu.

Mais maintenant, c'est comment nous pouvons simplement faire cela sur j'espère que vous avez compris pourquoi nous avons fait cela.

Donc, si vous lisez ce code, vous voyez notre dire si cela, quelle que soit la valeur, n'est pas connu, cela signifie qu'il n'est pas vide, alors cela signifie qu'il y a quelque chose là que nous ne voulons pas mettre à jour.

Donc, j'espère que vous avez compris ce que nous avons exactement fait dans ce bar.

Et cette partie suivante, nous allons examiner la méthode Delete.

La méthode delete est explicite, supprimez simplement un objet de données de notre base de données.

Ce que nous pouvons simplement faire savoir, c'est d'ajouter un nouvel endpoint, nous pouvons dire add up dot delete, puis slash delete ne devrait pas rougir, prenons l'idée de l'étudiant que nous voulons supprimer comme un paramètre de chemin, puis définissons notre fonction.

Élite étudiant nouvel étudiant ce gars ID veut que vous soyez un entier aussi nous collectons et maintenant nous vérifierons si l'ID de l'étudiant n'est pas dans l'étudiant.

Donc, s'il n'est pas un étudiant, cela signifie qu'il n'existe pas et nous retournons simplement une erreur que ce que vous essayez de supprimer n'est même pas dans notre base de données, il doit être dans la base de données pour que vous puissiez le supprimer pour juger cela n'existe pas, puis vous devez nous créer pour savoir d'abord avant de pouvoir essayer de supprimer, mais cela ne se désintègre pas, continuez avec notre code et supprimez cela, c'est deux questionnaires différents, ID des étudiants et ils retournent simplement un message que l'étudiant n'a pas été supprimé avec succès, c'est une manière basique de simplement pouvoir supprimer des données ou une valeur d'une base de données, d'abord, venez ici et testez cela.

Maintenant, si nous jouons avec les poses, tout d'abord, nous devons créer un nouvel objet avant de pouvoir faire cela.

Donc, voyons faire cela, un pour Jerry 20 ans, voyons l'année 13, maintenant, exécutons cela, cas d'étude, exit, donc comme vous pouvez le voir, j'appuie dessus deux fois, c'est pourquoi je dis que les étudiants existent, mais je viens ici pour obtenir sans vraiment l'avoir créé quand je l'ai pressé la première fois, quand je l'ai pressé par erreur à nouveau, donc disons exécuter, nous pouvons voir que nous avons Jerry 20 ans, retour.

Si je viens maintenant pour supprimer, vous pouvez voir que nous avons cette fonction de suppression.

Maintenant que nous avons cette fonction de suppression, c'est écrit maintenant en tapant simplement pour manger, exécuter j student supprimé avec succès.

Maintenant, nous ne savons peut-être pas s'ils l'ont supprimé, allons simplement de l'avant et appuyons sur vérifier pour voir si nous exécutons maintenant.

Il dit erreur interne du serveur, car l'étudiant n'existe plus.

Donc, vous venez aussi maintenant et essayez d'exécuter à nouveau.

Il dit que l'étudiant ne fait pas non, je suis un étudiant, j'essaie de supprimer n'existe pas.

Donc, c'est comment nous pouvons utiliser la méthode Delete.

Les geysers FastAPI vont être tous pour cette vidéo.

Merci beaucoup d'avoir regardé jusqu'à ce point.

Dans cette vidéo, nous avons parlé de fast API et de toutes les bases et les fondamentaux dont vous avez besoin pour commencer à travailler avec fast API.

Merci encore une fois d'avoir regardé cette vidéo et je vous verrai dans la prochaine.