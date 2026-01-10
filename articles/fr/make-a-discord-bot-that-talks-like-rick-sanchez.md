---
title: Créer un bot Discord qui parle comme Rick Sanchez
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-26T13:59:54.000Z'
originalURL: https://freecodecamp.org/news/make-a-discord-bot-that-talks-like-rick-sanchez
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/rick.png
tags:
- name: discord
  slug: discord
- name: youtube
  slug: youtube
seo_title: Créer un bot Discord qui parle comme Rick Sanchez
seo_desc: 'You can use artificial intelligence to make a Discord chat bot talk like
  your favorite character. It could be a Rick and Morty character, Harry Potter, Peppa
  Pig, or someone else.

  We just released a tutorial on the freeCodeCamp.org YouTube channel th...'
---

Vous pouvez utiliser l'intelligence artificielle pour faire parler un bot Discord comme votre personnage préféré. Il pourrait s'agir d'un personnage de Rick et Morty, Harry Potter, Peppa Pig, ou quelqu'un d'autre.

Nous venons de publier un tutoriel sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer un bot Discord qui parle comme un personnage de votre choix. Vous apprendrez à créer le bot en Python et en JavaScript.

Lynn Zheng a créé ce cours. Lynn est ingénieure logicielle chez Salesforce et développeuse de jeux à ses heures perdues. Elle est aussi une excellente enseignante !

Voici les sections de ce cours :

* Collecter des données
* Entraîner le modèle
* Déployer le modèle
* Construire le bot Discord en Python
* Construire le bot Discord en JavaScript
* Garder les bots en ligne

Créer ce bot génial vous fera sentir comme un magicien de la programmation.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/giphy-1.gif)

Regardez le cours ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=UjDpW_SOrlw) (1 heure de visionnage).

%[https://www.youtube.com/watch?v=UjDpW_SOrlw]

## Transcription

(générée automatiquement)

Vous voulez créer un bot Discord qui parle comme des personnages de Rick et Morty ou Harry Potter ? Peut-être voulez-vous faire parler un autre personnage préféré.

Dans ce cours, Lynn vous montrera comment créer un bot Discord qui utilise l'intelligence artificielle pour parler comme un personnage de votre choix.

Bonjour. Je m'appelle Lynn. Je suis ingénieure logicielle, développeuse de jeux à mes heures perdues et récente diplômée de l'Université de Chicago.

Dans ce tutoriel, nous allons construire un bot Discord d'IA qui peut parler comme votre personnage préféré.

Avant de commencer, si vous n'avez pas vu cette vidéo, sachez que cette vidéo est quelque chose de différent et plus complet.

Alors continuez à regarder jusqu'à la fin, le tutoriel original et mon premier bot Discord ont commencé comme une blague entre mes amis et moi lorsque nous jouions à des jeux vidéo, et cela m'a vraiment surpris de voir à quel point il est devenu populaire et combien de personnes voulaient construire leur propre bot basé sur ce tutoriel.

Par conséquent, j'ai décidé de mettre à jour ce tutoriel pour inclure plus de personnages, ainsi que pour vous montrer comment trouver des données pour votre personnage préféré.

D'autres sujets que nous aborderons ici incluent, mais ne sont pas limités à, comment entraîner le modèle, comment déployer le modèle, les erreurs que vous pourriez voir pendant ce modèle, l'entraînement et le pipeline de déploiement et comment les résoudre.

De plus, nous aborderons comment construire le bot en Python et comment le construire en JavaScript.

Enfin, nous aborderons comment déployer correctement le bot sur un serveur Discord et le limiter à certains canaux, et comment garder le bot en fonctionnement indéfiniment.

J'espère que vous êtes excité.

Et plongeons dans le tutoriel.

Tout d'abord, nous allons trouver des données pour notre personnage.

Mes sources préférées sont kaggle, les transcriptions wiki, et simplement des sites de fans aléatoires qui apparaissent dans une recherche Google.

Et mon processus de recherche se déroule comme suit : je commence par rechercher sur kaggle pour voir s'il y a des ensembles de données de dialogue pré-faits.

Par exemple, si nous recherchons Rick et Morty, nous obtenons cet ensemble de données bien formaté qui inclut le nom du personnage et les lignes qu'il parle.

Si nous recherchons Harry Potter, voici un autre ensemble de données qui inclut le personnage et la phrase qu'il prononce.

Puisque nous construisons un chatbot, nous avons besoin uniquement de ces deux colonnes dans notre ensemble de données : le nom du personnage et la ligne qu'il parle.

Ainsi, ces ensembles de données de dialogue sur kaggle sont parfaits pour notre exigence.

D'accord, si nous avons réussi à trouver des données sur kaggle, nous pouvons passer à l'étape d'entraînement du modèle.

Mais que faire si nous ne trouvons pas d'ensemble de données pour notre personnage sur kaggle.

Par exemple, si je veux trouver un ensemble de données pour Peppa Pig, il semble qu'il n'y ait pas d'ensemble de données pour le personnage.

Dans ce cas, nous devons peut-être trouver une transcription brute du média, qu'il s'agisse d'un jeu vidéo, d'un dessin animé ou d'une émission.

Et j'ai trouvé que transcript wiki a quelques bonnes ressources.

Ainsi, nous avons ici une liste de films, d'émissions, de jeux vidéo, de comédies musicales et de publicités.

Par exemple, j'ai pu trouver la transcription de Peppa Pig.

Et aussi des films comme Batman sur transcript wiki.

La transcription ressemble à ceci.

Ainsi, nous avons le nom du personnage et leurs actions ou les lignes qu'ils parlent.

Nous verrons bientôt comment transformer une transcription brute comme celle-ci en un ensemble de données comme ceux que nous avons vus sur kaggle.

Outre transcript wiki, vous pouvez également simplement rechercher sur Google le nom de votre média avec le mot-clé transcription.

Par exemple, ma première pensée était basée sur le jeu, le mot se termine avec vous.

Et il n'a pas de résultats non plus sur kaggle ou transcript wiki.

Ainsi, ce que j'ai fait, c'est simplement de rechercher sur Google le nom du jeu et la transcription du jeu.

Et il se trouve que ce site de fans a la transcription complète du jeu.

Ainsi, assurez-vous d'utiliser vos compétences de recherche Google pour trouver des données pour votre personnage.

Si, plutôt qu'un personnage fictif, vous êtes plus intéressé par un personnage de la vie réelle, vous pouvez rechercher des scripts d'interviews comme source de données.

Si vous voulez créer un chatbot qui parle comme vous-même ou vos amis, vous pouvez traiter les messages texte entre vous et vos amis comme des dialogues, et créer votre ensemble de données.

Il y a des tonnes de façons d'obtenir des données pour votre personnage.

Ainsi, soyez créatif.

Et maintenant, nous allons voir comment transformer des transcriptions brutes en ensemble de données.

Maintenant, supposons que nous avons trouvé notre transcription brute, voyons comment nous pouvons la transformer en un ensemble de données à deux colonnes : personnage et ligne.

Supposons que nous prenons cette transcription de Peppa Pig et que nous la copions dans un fichier texte.

Maintenant, nous allons sur Google Colab et téléchargeons notre fichier de données.

Maintenant, nous créons un notebook Google Colab.

Et nous utilisons cela pour analyser notre script.

Ainsi, je vais nommer ce script d'analyse ipnb.

Et nous allons importer drive depuis Google Colab et appeler drive.about.mount.content.drive.

Cela nous permettra de lire les données depuis notre Google Drive.

D'accord, maintenant que notre drive a été monté, importons OS et changeons le répertoire dans content, drive par drive.

Et ensuite, nous voyons s'il y a quelque chose dedans.

Oui, nous avons notre Peppa Pig dot txt.

Ainsi, ici, nous allons importer des expressions régulières pour analyser notre transcription, mettre le résultat analysé dans un dataframe panda, et l'exporter en tant que fichier CSV comme ceux que nous avons vus sur kaggle.

Ceci va être notre motif d'expression régulière.

Vous n'avez pas besoin d'être un pro des expressions régulières pour comprendre cette partie.

Si nous prenons le motif sur ce site, et que notre test est Peppa Pig, vous verrez que nous avons deux groupes de capture de correspondance, le premier étant le nom du personnage, le second étant la ligne parlée.

Et aussi pour la deuxième ligne, mama pig, nous avons le nom du personnage et la ligne étant parlée.

Bien, ainsi c'est tout pour l'expression régulière.

Maintenant, définissons un dictionnaire qui stockera nos données.

Ainsi, nous savons que nous avons besoin du nom de la colonne et de la colonne de ligne dans notre dataframe de résultat, puis nous ouvrons et lisons le fichier. Pour chaque ligne, nous la faisons correspondre avec notre motif d'expression régulière.

S'il y a une correspondance, nous extrayons le nom et la lumière de cette correspondance d'expression régulière, puis nous l'ajoutons à notre dictionnaire ici.

Et ensuite, nous convertissons ce dictionnaire en un dataframe.

Maintenant, nous pouvons inspecter le dataframe, citation.

Ainsi, nous avons le nom est Peppa Pig disant que je suis Peppa Pig.

Et George fait le son que mama pig fait le son super.

Nous pouvons également compter le nombre de lignes qui appartiennent à notre personnage.

Ainsi, nous faisons une somme où le nom est égal à Peppa Pig.

Et nous avons vu que Peppa Pig a 38 lignes dans notre dataframe entier.

Ainsi, la longueur de notre dataframe est de plus de 100 et Peppa Pig a 1/3 des lignes.

La dernière étape sera d'exporter le dataframe.

Ainsi, df.to, CSV, le nom sera Peppa Pig.

csv et nous allons supprimer l'index.

Cool.

Maintenant, nous devrions avoir un Peppa Pig dot CSV dans overdrive.

Et entendre ce nom et cette ligne.

C'est ainsi que nous analysons ces transcriptions brutes dans un fichier qui peut être utilisé dans notre entraînement de modèle.

Ainsi, ensuite, procédons à l'étape passionnante de l'entraînement du modèle.

Maintenant, nous allons entraîner le modèle.

Allez dans mon dépôt GitHub lié dans la description ci-dessous et téléchargez le contenu.

Nous allons utiliser ce workflow d'entraînement et de téléchargement de modèle, l'IP un MB qui ressemble à ceci.

D'accord, maintenant notre fichier a été téléchargé, nous décompressons le contenu.

Et ici, nous avons un fichier notebook d'entraînement et de téléchargement de modèle dot ipnb.

Nous téléchargeons ce fichier notebook sur Google Drive et l'ouvrons dans Google Colab.

Nous allons entraîner un modèle GPT qui signifie transformateur génératif pré-entraîné.

Dans le runtime, changez le type de runtime.

Assurez-vous de sélectionner GPU car cela accélérera notre entraînement de modèle.

Ainsi, maintenant ici, nous montons le drive.

Nous installons le module Transformers que nous allons utiliser.

Et nous changeons de répertoire dans mon drive.

Voici tous les modules que nous importons.

Si nous utilisons l'ensemble de données de kaggle, nous devons obtenir notre clé API de kaggle.

Ainsi, allez dans notre profil kaggle, allez dans compte.

Faites défiler jusqu'à la section clé API.

Créez un nouveau jeton API et téléchargez ce fichier en tant que kaggle dot JSON.

Nous retournerons à Google Drive et téléchargerons kaggle dot JSON.

Maintenant, nous pouvons télécharger notre ensemble de données de kaggle, nous allons utiliser l'ensemble de données Harry Potter comme exemple.

Ainsi, prenez ce nom d'utilisateur et le nom de l'ensemble de données.

Et notre fichier est ici partie un dot CSV.

Non, non, car il y a des espaces blancs, dans notre nom de fichier, nous avons des caractères spéciaux dans le nom de fichier.

Ainsi, inspectons le contenu de notre fichier de données.

Eh bien, les fichiers CSV sont généralement séparés par des virgules, d'où le nom CSV.

Cependant, celui-ci semble être séparé par des points-virgules.

Ainsi, nous devons prendre en charge les points-virgules lorsque nous lisons les données dans un dataframe panda.

Ainsi, la séparation est un point-virgule au lieu d'une virgule.

Cool.

Ainsi, échantillonnons les données pour voir ce qu'il y a à l'intérieur.

D'accord, ainsi nous avons le personnage et la phrase.

Remarquez que ces deux noms de colonnes ne sont pas exactement ce dont nous avons besoin.

Nous voulons que les deux colonnes de notre dataframe soient nommées nom et ligne comme utilisé ici dans cette cellule, donc nous devons changer le nom de nos colonnes.

D'accord, rééchantillonnons nos données.

Il semble que nous avons réussi à changer le nom de nos colonnes.

Maintenant, voyons à quel point nos données sont grandes.

Ainsi, il n'a que 1000 lignes environ.

Et voyons combien de lignes notre personnage a.

Notre personnage a 155 lignes.

Ainsi, ici, nous changeons le nom de notre personnage en Harry.

Et maintenant, nous exécutons cette cellule pour créer un dataframe de contexte qui inclut la ligne actuelle que notre personnage parle, et plusieurs lignes directement précédant la ligne.

Le dataframe de contexte est utile ici car nous créons un chatbot conversationnel.

Et nous voulons générer une réponse basée sur le contexte de la conversation.

Ainsi, échantillonnons notre dataframe de contexte.

Ainsi, dans le contexte de la clarté, quelque chose quelque chose notre personnage répond avec semble dommage de ne pas demander.

Super, maintenant nous avons notre ensemble de données, qui divise l'ensemble de données en un ensemble d'entraînement et un ensemble de test.

C'est parce que nous ne voulons pas surajuster le modèle.

Dans le cas du surajustement, le modèle mémorisera simplement les lignes de l'ensemble de données et nous répondra en utilisant les lignes exactes, nous ne voulons pas cela, nous voulons que la conversation soit plus organique.

Ainsi, nous n'entraîons le modèle que sur un ensemble d'entraînement et évaluons le modèle sur l'ensemble de test.

Ainsi, nous continuons à exécuter ces cellules pour construire des ensembles de données, des points de contrôle de cache, et ici nous construisons le modèle.

Nous construirons notre modèle en affinant le GPT small pré-entraîné de Microsoft.

Small ici fait référence au nombre de paramètres dans le modèle.

Il existe également un modèle medium et un modèle large.

Généralement, plus le modèle est grand, plus il prend de temps à entraîner, mais plus le modèle peut devenir intelligent.

Je recommanderais d'entraîner un modèle medium, car il est assez intelligent et pas trop difficile à changer.

Mon chatbot de production qui fonctionne actuellement sur un serveur avec plus de 1000 utilisateurs est également un modèle medium.

Pour ce tutoriel, pour des raisons de temps, j'entraîne simplement un petit modèle.

Vous pouvez voir ici qu'il télécharge le modèle.

Et cela peut prendre un certain temps car il fait essentiellement 300 mégaoctets.

Voici quelques hyperparamètres que vous pourriez trouver utiles.

Par exemple, num train epochs est le nombre d'époques d'entraînement.

Cela est défini à quatre ici, et c'est le nombre de fois que le modèle cyclera à travers l'ensemble d'entraînement.

Tant que le modèle n'est pas surajusté, augmenter le nombre d'époques d'entraînement donne généralement des modèles plus intelligents.

Parce que le modèle a plus de temps pour cycler à travers l'ensemble de données et saisir les détails minutieux.

Il y a un autre hyperparamètre appelé la taille du lot.

C'est le nombre d'exemples d'entraînement que le modèle verra dans le lot avant de mettre à jour son gradient.

Je ne recommanderais pas de changer cela à moins que vous sachiez ce que vous faites, puisque d'autres hyperparamètres comme le taux d'apprentissage et la température pourraient être sensibles à ce changement de taille de lot.

Cependant, si vous entraînez un modèle plus grand sur un ensemble de données plus grand et que vous rencontrez des erreurs de mémoire, pour faire disparaître l'erreur, il pourrait aider de diminuer la taille du lot.

Les cellules restantes ont été configurées pour prendre ce dataframe de contexte que nous avons créé, entraîner le modèle et le sauvegarder dans un dossier appelé output small.

Maintenant, exécutons cette fonction principale.

L'entraînement prendra un certain temps, j'ai entraîné mon modèle medium pendant 12 époques, et cela a pris environ deux heures.

Ainsi, asseyez-vous et prenez une collation pendant que le modèle s'entraîne.

Vous pouvez voir la progression dans les barres de progression. D'accord, ici nous obtenons un perplexing cancer.

Cela fait généralement référence à la confusion du modèle.

Si un modèle a une grande complexité, cela signifie que le modèle est assez confus quant aux mots à choisir pour répondre à une situation donnée.

Et le modèle pourrait ne pas être très intelligent.

Dans notre cas, notre ensemble de données est assez petit.

Il n'a que 150 lignes environ.

Ainsi, il est logique que la perplexité soit élevée pour diminuer la perplexité, nous devons peut-être entraîner pendant plus d'époques.

Cool.

Mais maintenant que l'entraînement est terminé, nous pouvons charger et discuter avec le modèle ici.

Cela a changé le nom du Hello, fellow read writer.

Ainsi, posons une pause.

Quidditch.

Il n'y a pas de tel chose qu'un mauvais read writer.

Super, il semble que notre chatbot soit capable de tenir une conversation.

Maintenant, nous pouvons pousser le modèle vers Huggy face et commencer à construire notre bot de chat Discord.

D'accord, maintenant changeons de répertoire juste dans le dossier de contenu.

Parce que nous allons faire notre push là.

Et nous faisons pip install hugging face command line client.

Et ensuite, nous nous connectons en utilisant nos identifiants.

Juste après la connexion, nous avons assigné ce jeton, nous devons prendre ce jeton pour la chanson que nous devons faire ensuite.

Ainsi, nous pouvons créer un dépôt pour stocker tous les modèles depuis la ligne de commande, le mien va s'appeler dialogue up at small Harry Potter.

Et notre dépôt de modèle vide est juste ici.

Il n'y a rien sauf le fichier get attributes, mais nous allons ajouter le fichier de modèle bientôt.

Maintenant, nous avons toujours get Fs, qui signifie get large file storage, ce mur nous permet de pousser et de tirer tous les modèles.

Et nous avons remplacé ce jeton par le takeaway que nous venons de copier ci-dessus.

Ainsi, voici mon nom d'utilisateur et mon jeton.

Et nous l'appelons, notre résultat d'entraînement est stocké dans ce répertoire output small.

Et ensuite, nous changeons de répertoire dans notre répertoire de dialogue up the small car nous devons faire git add et permit depuis là, nous avons vu les get Fs et inspecté le contenu de notre répertoire actuel, qui devrait être dialogue GPT, small her father et aussi juste imprimé le répertoire de travail où pour s'assurer que nous sommes à l'intérieur du contenu.

Cool.

Maintenant, nous vérifions le statut du fichier sur Git.

Ainsi, ces fichiers ne sont pas ceux que nous devons ajouter à get.

Ainsi, nous faisons un git add, cela prendra un certain temps car le pytorch model dot étant est assez grand.

Et nous avons configuré un nom d'utilisateur global et un email d'utilisateur.

Ce sont juste mes identifiants hug et basés.

Cela viendrait avec le message de commentaire initial.

Et enfin, nous allons pousser le modèle.

Il fait environ 400 mégaoctets car le modèle pytorch lui-même fait environ 400 mégaoctets.

D'accord, il semble que le push soit terminé.

Maintenant, nous voyons notre modèle pytorch ici.

Cependant, il y a une chose de plus que nous devons faire avant de pouvoir converser avec le modèle sur Huggy face.

C'est-à-dire, vous voyez ici, il est marqué comme génération de texte.

Cependant, nous savons que nous entraînons un modèle de chatbot, et nous voulons que notre modèle soit conversationnel.

À cette fin, nous devons éditer la carte du modèle.

Ainsi, nous créons une carte de modèle ici et nous mettons notre taxe de modèle souhaitée, donc notre taxe est conversationnelle.

Nous venons dans notre carte de modèle.

Et maintenant, notre modèle est correctement marqué comme conversationnel.

Si nous allons à la page principale du modèle, nous pouvons commencer à discuter avec le modèle ici.

D'accord, maintenant que nous avons poussé notre modèle vers hugging face, nous sommes prêts à l'utiliser dans nos bots de chat Discord.

Maintenant, nous avons notre modèle, construisons le bot Discord ici sur Discord.

J'ai mon serveur lease dev lab.

J'ai deux canaux, un pour le bot Python et un pour le bot job. La raison pour laquelle nous avons un canal séparé pour les bots est que nous ne voulons pas que les bots se parlent entre eux.

Ainsi, après avoir construit le bot, nous apprendrons comment définir leurs permissions correctement afin qu'ils ne sortent pas de leur canal dédié.

Ainsi, nous allons sur la page des développeurs de Discord, créons une application, nous avons besoin d'une application par bot.

Ainsi, notre nom sera chatted about Python.

Ainsi, ici, nous créons un bot.

Et je vais nommer celui-ci Harry Potter, bot, Python et télécharger une icône.

Nous allons utiliser ce jeton API ici.

Lorsque nous créons notre bot en Python, nous allons héberger notre bot notre rapida, donc inscrivez-vous à repple.id et créez un nouveau Python repple ici, allez le nommer chatty, mais je pensais et ici, nous devrons stocker nos jetons API pour Huggy face underscore us environmental variables.

Ainsi, voici le haut pour les secrets des variables d'environnement.

Ainsi, le premier sera le jeton hugging face.

Et pour la valeur, nous irons à notre profil hugging face ou le profil API tokus, copier le jeton API, revenir ici et remplir cette valeur.

Ensuite, nous avons créé ce jeton core.

Et pour cette valeur, nous irions à ce portail des développeurs de discord et copierions le jeton.

Trois, ajoutez le jeton ici.

Et nos variables d'environnement sont toutes définies.

Ensuite, j'ai le fichier Python dans mon dépôt GitHub appelé ce court bot dot p y.

Ainsi, nous avons apporté le code d'ici, et je vais expliquer le code ligne par ligne.

En commençant par la ligne un, nous importons d'abord le module OS qui nous aidera à lire nos variables d'environnement.

Ensuite, nous importons des modules qui sont utiles pour interroger le modèle Huggy face.

Enfin, nous importerons le module discount.

Et ici, j'ai mon URL API pointant vers mon nom d'utilisateur.

Et avec le Find a bot comme suit.

Dans la fonction init, elle prend un nom de modèle, qui pour moi sera dialogue GPT small Harry Potter.

Ensuite, nous stockons ce point de terminaison API en concaténant cette URL API, qui est mon lien de profil avec le nom du modèle.

Maintenant, nous récupérons le jeton API secret de l'environnement système en regardant Oh s dot environment hugging face token.

Ensuite, nous formatons l'en-tête, vous savez, la requête à Huggy face.

Pour la partie autorisation.

Nous mettons bearer et le jeton hugging face.

Ensuite, nous définirons la méthode quorum qui prend le payload.

nous vidons le payload en tant que chaîne JSON.

Et utilisons le module de requête pour faire une requête HTTP POST au point de terminaison API en utilisant nos en-têtes de requête définis, qui contient notre clé API Hugging face et en passant les données.

Une fois la requête terminée, elle devrait nous donner un objet de réponse et nous le décodons depuis UTF huit et chargeons le résultat en tant que taux et retournons à la chaîne.

Ensuite, vous trouverez une fonction asynchrone nommée déjà.

Les deux définitions de fonction suivantes sont basées sur l'API discord.

Les deux sont des fonctions asynchrones.

La première est déjà, cette fonction sera appelée lorsque le bot se connecte.

Ainsi, lorsque le bot se connecte, nous imprimerons logged as print out le nom du bot et un ID de bot afin que nous sachions que le bot fonctionne.

Ensuite, parce que notre bot est un chatbot, il doit répondre aux messages.

Ainsi, notre méthode de message sera appelée chaque fois que le bot voit un message dans le canal.

Ainsi, étant donné le message, si le message provient du bot lui-même, le bot ignore le message et n'y répond pas.

Sinon, il formera un payload de Corée avec le contenu du message.

Et pour rendre le bot plus convivial.

Pendant que le bot attend la réponse HTTP du modèle, nous définissons son statut comme en train d'écrire afin que l'utilisateur sache que le bot génère sa réponse.

Ainsi, c'est un appel synchrone avec un message.channel.tv.

Nous l'appelons soft query en utilisant le payload et obtenons la réponse.

S'il y a une réponse générée valide, il y aura un champ de taxe généré dans cette réponse.

Et nous pourrons l'extraire en tant que réponse du bot.

Sinon, il pourrait y avoir une erreur dans la réponse, nous enregistrons simplement le message d'erreur afin de pouvoir le déboguer plus tard.

Enfin, nous utilisons une autre méthode asynchrone pour envoyer la réponse du bot au canal en utilisant message dot channel dot send.

Et c'est tout pour notre définition de bot.

Dans la fonction principale, nous avons simplement créé un bot en passant le nom du modèle.

Ainsi, pour moi, c'est style gptc small Harry Potter et us client that run looking up the score token from the environment variables.

Super, maintenant que notre bot devrait être entièrement configuré, il semblait que le bot était dans notre canal.

Dans l'onglet OAuth deux, nous allons sélectionner le bot.

Et pour les permissions du bot.

La seule chose dont vous avez besoin est d'envoyer des messages.

Ainsi, nous copions cette URL, la collons dans une nouvelle fenêtre de navigateur et l'invitons à mon serveur.

D'accord, maintenant que nous voyons que notre bot est apparu, cependant, il apparaît comme hors ligne.

Ainsi, nous devons exécuter le repple.

Ainsi, nous cliquons sur exécuter ici.

Et le rapport installe toutes nos dépendances et imports.

Super, maintenant que notre bot s'est connecté en tant que Harry Potter about Python, et voici son ID unique.

Allons sur le serveur.

Et maintenant que le bot est en ligne, nous ne voulons pas que le bot apparaisse dans le canal général.

Ainsi, nous allons dans les paramètres du canal, permissions.

Permissions avancées, ajouter un bot et nous supprimons sa permission d'envoyer des messages et sauvegardons les changements.

Maintenant, voyons ce qui se passe si je tape quelque chose dans le canal général, rien ne devrait se passer car le bot ne devrait pas être capable d'envoyer un message.

Rien ne se passe, bien que le bot soit en ligne.

Et maintenant, ce bot devrait fonctionner dans ce canal de bots Python.

Ainsi, faisons Hello.

Et nous avons brièvement vu qu'il n'y a pas de prompt de frappe.

Cool.

Ainsi, oui, c'est ainsi que nous avons construit un bot en Python.

Une chose à savoir, vous savez, raphoe, bien qu'il ne soit pas, car nous avons enlevé la permission du bot d'envoyer les messages dans le canal général, il affiche une exception, et c'est totalement acceptable.

Si vous n'aimez pas voir cette exception, vous pouvez utiliser le bloc try, accept et enregistrer cette exception.

Super.

Ainsi, maintenant nous allons répéter le processus pour le bot JavaScript.

Ainsi, nous retournons au portail des développeurs de discord, et créons une nouvelle application.

Cette fois, je vais l'appeler chatty bots, JavaScript.

Et je vais créer un bot.

Retour à wrap it, nous créons une application node.js.

allons l'appeler chadic, thought js.

Nous créons à nouveau deux variables environnementales.

La première est le jeton hugging face, en copiant mon jeton API de mon profil Edit Profile, en le mettant ici et en copiant mon jeton de bot discord.

Appelons celui-ci ce jeton de cour et ajoutons la valeur.

Super.

Maintenant, nous avons notre variable environnementale configurée.

Allons dans mon dépôt GitHub, il y a un fichier discord bots.js qui contient le code que nous allons utiliser pour ce chatbot JavaScript.

Copions-collons.

Et je vais passer en revue le code ligne par ligne.

Ainsi, d'abord, nous importons le CPI discord pour le module JavaScript.

Et nous importons fetch pour faire des requêtes HTTP, tout comme avec it en Python.

Et nous initialisons un nouveau client discord et définissons l'URL du modèle comme mon nom d'utilisateur et le nom du modèle.

Ainsi, ce gars est le LGBT small Harry Potter.

Et c'est le même callback qui est appelé lorsque le bot est prêt, tout comme la fonction déjà que nous avons vue en Python.

Ainsi, lorsque le bot est prêt et connecté, nous imprimons logged in as client user dot Tak.

Et voici un autre callback.

Cette fois, all message, nous utilisons un callback asynchrone, car nous faisons des requêtes HTTP.

Comme dans le script Python, nous ignorons le message si le message provient du bot lui-même.

En vérifiant si message dot author est le bot.

Maintenant, nous formons le payload.

Ainsi, le payload est un dictionnaire contenant des inputs avec le contenu du message texte, qui est le message que le bot a reçu.

Et nous formons les en-têtes de requête en utilisant à nouveau la clé API Huggy face.

Ainsi, nous lisons le jeton Huggy face de l'environnement, process dot m dot hugging face token et formons les en-têtes.

Juste avant de commencer à faire la requête HTTP, nous définissons le statut du bot comme en train d'écrire.

Maintenant, enregistrons un serveur.

Ainsi, la réponse est le résultat de cet appel à fetch en utilisant HTTP POST, étant donné le payload comme corps et les en-têtes en utilisant le jeton Huggy face.

Et nous convertissons la réponse en format JSON, et extrayons le champ de texte généré.

S'il n'y a pas de champ de texte généré dans la réponse, mais que la réponse contient un champ plus étroit.

Cela signifie que le board a rencontré des erreurs, et nous pouvons vouloir imprimer l'erreur pour un débogage ultérieur.

Maintenant que nous avons la réponse du bot, nous pouvons effacer son statut de frappe et envoyer le message au canal en tant que réponse.

Cela met fin à la définition de notre client dot our message call.

Ici, nous nous connectons en utilisant le jeton discord.

Maintenant, invitons le boss à notre serveur.

Ainsi, nous allons à o auth.

Vérifions le bot, sa seule permission est d'envoyer des messages.

Nous copions cela, le collons dans une nouvelle fenêtre de navigateur et l'invitons à notre serveur.

Super, il semble que nous ayons un autre bot.

N'oubliez pas de cliquer sur sauvegarder les changements.

Sinon, l'icône du bot ne s'affichera pas.

Maintenant que nous avons notre bot, cependant, il n'est pas connecté.

Ainsi, nous devons retourner à la repple pour exécuter notre script.

Mais avant d'exécuter notre repple, assurons-nous que le bot n'a pas accès au canal général.

Ni n'a-t-il accès au canal Python car il ne devrait pas y aller.

Ainsi, dans les permissions, nous trouvons ce chat about JavaScript.

Supprimons sa permission d'envoyer des messages.

Et n'oubliez pas de sauvegarder les changements.

Nous faisons la même chose pour lui sur le canal Python et allons au canal jazz.

Cette fois, celui que nous devons supprimer est le bot Python.

Ainsi, ce bot Python ne devrait pas être capable d'envoyer des messages à ce canal JavaScript.

Maintenant, nous retournons pour exécuter notre raphoe dotnet.

Si vous voyez cette erreur, cela signifie que la version de discord que NPM essaie d'installer est incorrecte.

Vous pouvez voir qu'il y a ces avertissements que le module discord le plus récent n'est pas compatible avec la version de node ou NPM de rapida.

Ainsi, nous devons changer manuellement quelque chose dans package dot JSON.

Ainsi, ici, nous utilisons simplement l'ancienne version et le réexécutons.

Maintenant que nous sommes connectés en tant que chatty about JavaScript 1048, retournons à notre canal discord.

Appelons le chat about est également en ligne.

Voyons s'il répond à nos messages.

D'accord, bien.

Ainsi, voici maintenant un message d'erreur nous indiquant que le modèle est encore en train de charger.

Le modèle prendra généralement une ou deux minutes pour charger.

Ainsi, donnons-lui un peu de temps.

Super, il semble que notre bot réponde.

Et parce que nous avons défini les permissions du bot correctement, le bot Python ne répond à aucun message ici.

Et les bots JavaScript ne devraient pas être capables de parler ici.

Et dans notre canal général, personne n'est jamais autorisé à parler ici.

Cool.

Ainsi, maintenant nous avons réussi à construire le bot à la fois en Python et en JavaScript.

Une chose à noter est que si je ferme l'onglet du navigateur pour le bot Python, le bot ne répond plus, bien qu'il montre toujours que le bot est en ligne.

Ainsi, dans la prochaine partie, nous allons voir comment garder les bots en fonctionnement indéfiniment dans le navigateur, même lorsque nous fermons l'onglet du navigateur.

Afin de faire fonctionner notre bot indéfiniment, nous devons créer un serveur web dans raphoe dotnet, et configurer un service appelé uptime robot pour pinguer continuellement le serveur web.

Ainsi, c'est pour le bot Python.

Et nous créons un nouveau fichier appelé people live dot p y.

Et nous ajoutons le code pour un serveur web comme ceci.

Et dans notre main.py, nous importons cette partie.

Et ici, dans la fonction principale, juste avant que le bot ne s'exécute.

Nous lui demandons de rester en vie.

Nous l'exécutons.

Lorsque le code s'exécute, nous voyons une URL affichée dans cet onglet.

Et nous copions cette URL et l'apportons à notre service uptime robot.

Ainsi, voici le site web d'uptime robots.

Et j'ai déjà un compte.

Ainsi, je vais simplement aller à mon tableau de bord et ajouter un nouveau moniteur.

Le type de moniteur montra va être HTTPS, le nom convivial, ce court, Python mais l'URL est celle que nous avons copiée d'ici.

Et le niveau monétaire sera un ping toutes les cinq minutes, ce qui devrait être suffisant.

Et enfin, nous créons, surveillons et le fermons.

Maintenant, voyons si notre bot Python est capable de fonctionner indéfiniment.

D'accord, je vais fermer ce haut contenant mon script Python.

Et il semble que notre modèle soit toujours en ligne.

C'est juste qu'après un certain temps, le modèle ou le backend Huggy face se rechargera car le bot lui-même répond.

Nous savons que notre approche de serveur web a fonctionné. Maintenant, répétons ce processus pour le bot JavaScript.

Nous créons un nouveau fichier appelé server.js et collons le code de base en attendant d'importer cette partie du fichier que nous venons de créer.

Enfin, juste avant que le bot ne s'exécute, nous allons appeler keep alive.

Arrêtez ce service.

Et écrivez.

D'accord, le serveur est maintenant prêt.

Nous copions cette URL, allons à uptime robot et ajoutons un nouveau moniteur.

C'est à nouveau un moniteur HTTP, ce cord.

js bot, et l'URL est comme ceci.

Nous créons un moniteur.

Maintenant, nous pouvons fermer en toute sécurité cette fenêtre de navigateur et revenir à notre chat discord, il est toujours en cours d'exécution.

Super.

Maintenant, nous avons terminé.

Nous avons un bot de chat Python cool et un bot de chat JavaScript cool qui peut fonctionner indéfiniment.

J'espère que vous avez apprécié cette vidéo.

Veuillez vous abonner pour plus de contenu comme celui-ci et je vous verrai dans le prochain.