---
title: Comment utiliser PySpark pour le traitement des données et le machine learning
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-28T14:18:37.000Z'
originalURL: https://freecodecamp.org/news/use-pyspark-for-data-processing-and-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pyspark.png
tags:
- name: '#apache-spark'
  slug: apache-spark
- name: youtube
  slug: youtube
seo_title: Comment utiliser PySpark pour le traitement des données et le machine learning
seo_desc: 'PySpark is an interface for Apache Spark in Python. PySpark is often used
  for large-scale data processing and machine learning.

  We just released a PySpark crash course on the freeCodeCamp.org YouTube channel.

  Krish Naik developed this course. Krish i...'
---

PySpark est une interface pour Apache Spark en Python. PySpark est souvent utilisé pour le traitement de données à grande échelle et le machine learning.

Nous venons de publier un cours intensif sur PySpark sur la chaîne YouTube freeCodeCamp.org.

Krish Naik a développé ce cours. Krish est un data scientist principal et il gère une chaîne YouTube populaire.

Apache Spark est écrit dans le langage de programmation Scala. Pour supporter Python avec Spark, la communauté Apache Spark a publié un outil appelé PySpark. PySpark permet aux gens de travailler avec des ensembles de données distribués résilients (RDD) en Python à travers une bibliothèque appelée Py4j.

Voici les sujets abordés dans ce cours :

* Introduction à PySpark
* PySpark DataFrame Partie 1
* PySpark Gestion des valeurs manquantes
* PySpark DataFrame Partie 2
* PySpark Groupby et fonctions d'agrégation
* PySpark Mlib et installation et implémentation
* Introduction à Databricks
* Implémentation de la régression linéaire en utilisant Databricks dans des clusters uniques

Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/_C8kWso4ne4) (2 heures de visionnage).

%[https://youtu.be/_C8kWso4ne4]

## Transcription

(auto-traduction)

PiSpark est une interface pour Apache Spark en Python, souvent utilisée pour le traitement de données à grande échelle et le machine learning.

Krish knack enseigne ce cours.

Nous allons donc commencer la série Apache Spark.

Et spécifiquement, si je parle de Spark, nous allons nous concentrer sur la manière dont nous pouvons utiliser spark avec Python.

Nous allons donc discuter de la bibliothèque appelée pi Spark, nous allons essayer de comprendre pourquoi spark est réellement nécessaire.

Et probablement, nous allons également essayer de couvrir beaucoup de choses, il y a quelque chose appelé emblème, spark emblème, qui dira essentiellement comment vous pouvez appliquer le machine learning, vous savez, dans Apache Spark lui-même avec l'aide de cette API spark appelée bibliothèques pi spark.

Et en plus de cela, nous allons également essayer de voir à l'avenir, une fois que nous comprendrons les bases de la bibliothèque PI spark, comment nous pouvons réellement pré-traiter notre ensemble de données, comment nous pouvons utiliser les data frames PI spark, nous allons également essayer de voir comment nous pouvons implémenter ou comment nous pouvons utiliser PI spark et les plateformes cloud comme data, bricks, Amazon, AWS, vous savez, tous ces types de clouds, nous allons essayer de couvrir.

Et rappelez-vous, Apache Spark est assez pratique.

Laissez-moi vous dire, laissez-moi juste vous donner quelques-unes des raisons pour lesquelles Apache Spark est assez bon.

Parce que comprenez, supposons que vous avez une énorme quantité de données, d'accord, supposons que je dise que j'ai 64 Go de données, 128 Go de données, vous savez, nous pouvons avoir certains types de systèmes ou de systèmes autonomes, vous savez, où nous pouvons avoir 32 Go de RAM, probablement 64 Go de RAM maintenant dans la station de travail où je travaille.

Elle a 64 Go de RAM.

Donc, au maximum, elle peut directement télécharger un ensemble de données de 32 Go, 48 Go, d'accord.

Mais que se passe-t-il si nous avons un ensemble de données de 1,8 Go, vous savez, c'est le moment, les gars, nous ne dépendons pas seulement d'un système local, nous allons essayer de pré-traiter ces données particulières ou d'effectuer une opération quelconque dans des systèmes distribués, des systèmes distribués qui signifient essentiellement qu'il y aura plusieurs systèmes, vous savez, où nous pouvons réellement exécuter ce pipeline de travaux ou de processus ou essayer de faire des activités que nous voulons vraiment.

Et définitivement, Apache Spark va réellement nous aider à faire cela.

Et cela a été assez incroyable.

Et oui, les gens voulaient ce genre de vidéos beaucoup.

Donc, comment allons-nous parcourir cette playlist spécifique, c'est que nous allons essayer, tout d'abord, de commencer par l'installation, nous allons essayer d'utiliser PI Spark, parce que c'est aussi Apache Spark, c'est une API spark avec Python, lorsque vous travaillez réellement avec Python, nous utilisons essentiellement la bibliothèque PI spark.

Et oui, nous pouvons également utiliser spark avec d'autres langages de programmation comme Java, Scala R.

Et d'accord, et nous allons essayer de comprendre depuis les bases, vous savez, depuis les bases, comment lisons-nous un ensemble de données ? Comment nous connectons-nous à une source de données ? Probablement, comment jouons-nous avec les data frames, vous savez, dans cet Apache Spark, qui est votre PI Spark, aussi, ils vous fournissent des structures de données, comme des data frames, qui est très similaire au data frame de panda.

Mais oui, différents types d'opérations sont supportés là-bas, que nous allons voir un par un au fur et à mesure que nous avançons.

Et ensuite, nous allons essayer d'entrer dans emlid, le spa, Apache Spark et lib.

Donc, essentiellement, il est appelé un spark em lib, qui va réellement nous aider à effectuer du machine learning, qui sera où nous serons capables d'effectuer une tâche d'algorithme de machine learning où nous serons capables de faire de la régression, de la classification, du clustering.

Et enfin, nous allons essayer de voir comment nous pouvons réellement faire la même opération dans le cloud, où je vais essayer de vous montrer quelques exemples où nous aurons un énorme ensemble de données, nous allons essayer de faire l'opération dans les clusters de système, vous savez, dans un système distribué, et nous allons essayer de voir comment nous pouvons utiliser spark dans cela, d'accord.

Donc, toutes ces choses seront essentiellement couvertes.

Maintenant, certains des avantages d'Apache Spark et pourquoi il est très célèbre, parce qu'il exécute des charges de travail 100 multipliées par 100 fois plus vite, vous savez, cela signifie essentiellement que si vous connaissez le big data, les gars, lorsque nous parlons de big data, nous parlons essentiellement d'énormes ensembles de données, n'est-ce pas.

Et puis si vous avez entendu parler de cette terminologie appelée MapReduce, n'est-ce pas, Trashman Apache Spark est beaucoup plus rapide, 100 fois plus rapide que MapReduce aussi.

D'accord, et c'est certains des avantages supplémentaires qu'il est facile à utiliser.

Vous pouvez écrire une application rapidement en Java, Scala, Python, ou R.

Comme je l'ai dit, nous allons nous concentrer sur Python, où nous allons utiliser une bibliothèque appelée pi Spark.

Ensuite, vous pouvez également combiner le streaming SQL et l'analyse complexe.

Lorsque je parle d'analyse complexe.

Je parle essentiellement de cet emblème, des bibliothèques de machine learning.

Cela fonctionnera définitivement bien avec Apache Spark.

Et Apache sparks peut fonctionner sur Hadoop, Apache missiles Cuba net autonome dans nos clouds, cloud, différents types de clouds, les gars, lorsque je parle d'AWS data, bricks, toutes ces choses, nous pouvons définitivement travailler, d'accord.

Et il fonctionne réellement en mode cluster, le mode cluster signifie essentiellement en mode distribué, n'est-ce pas.

Donc, ce sont quelques exemples.

Maintenant, si je vais avec le respect de quelle version de pi spark, spark nous allons utiliser pi spark 3.1 point un, nous allons utiliser, nous allons essayer de travailler.

Et si vous allez simplement et recherchez ici, vous pouvez voir SQL et data frames et tout ici, vous pouvez voir Spark streaming machine emilich, qui est appelé machine learning.

Et d'accord, et en plus de cela, si je vais et vois l'aperçu, ici, vous pouvez voir qu'Apache Spark est un système de calcul de cluster rapide et généraliste et fournit des API de haut niveau en scalaire, Java et Python, qui rend les travaux parallèles faciles à écrire et un moteur optimisé qui supporte des graphes de compétition authentiques, il est essentiellement pour travailler avec une énorme quantité de données en peu de temps, vous savez, et c'est assez pratique, nous allons essayer de travailler.

Maintenant, si je vais et recherche spark en Python, vous savez, cette page va s'ouvrir.

Et ces choses, nous allons essayer de discuter de la façon de l'installer.

Et dans cette vidéo, nous allons essayer d'installer la bibliothèque PI spark.

Et si je parle de la bibliothèque pi spark, vous serez en mesure de voir que la bibliothèque pi spark est assez incroyable.

Cette bibliothèque est si vous voulez vraiment travailler avec spot, si vous voulez travailler avec cette fonctionnalité spark avec Python, vous utilisez essentiellement cette bibliothèque spécifique.

Et procédons, et essayons de voir comment nous pouvons rapidement installer les bibliothèques spécifiques et vérifier les choses que nous pouvons réellement faire ? D'accord, donc toutes ces choses, nous allons essayer de voir.

Alors commençons, veuillez vous assurer que vous créez un nouvel environnement lorsque vous travaillez avec PI Spark.

J'ai donc créé un nouvel environnement appelé my envy ici, tout d'abord, je vais essayer d'installer la bibliothèque PI spark.

Je vais donc écrire pip install pi Spark.

D'accord, et voyons, dans ce cas, nous nous concentrerons sur l'installation, nous nous concentrerons sur la lecture de certains ensembles de données et nous essaierons de voir quelles sont les choses que nous pouvons réellement faire, d'accord, et après avoir fait cela, ce que nous pouvons réellement faire, c'est que vous pouvez voir que notre PI spark a été installé, afin de vérifier si l'installation est parfaite ou non, je vais simplement écrire input by Spark.

Donc, cela semble parfaitement bien, cela fonctionne, vous savez, nous sommes en mesure de voir que le PI spark est installé correctement.

Maintenant, vous pouvez rencontrer certains types de problèmes avec PI Spark.

C'est la raison pour laquelle je vous dis de créer un nouvel environnement.

Si vous rencontrez un problème, faites-moi savoir quelle est l'erreur que vous obtenez ? Probablement en écrivant dans la section des commentaires.

D'accord, maintenant, faisons une chose, je vais simplement ouvrir une feuille Excel.

D'accord.

Et probablement, je vais simplement essayer de créer quelques ensembles de données, je vais dire nom, probablement je vais simplement dire nom, et âge, d'accord.

Et supposons que mon nom ici que je vais écrire comme crash, et aussi 31.

Je vais dire Sudan shoe.

right shoe down shoe, je vais simplement dire d'accord, 30, probablement, je vais simplement écrire quelques noms comme Sonny, probablement, je vais aussi donner les données comme 29.

Donc, ces trois données, nous allons simplement essayer de voir comment nous pouvons lire ce fichier spécifique.

D'accord, je vais simplement l'enregistrer.

Voyons, je vais l'enregistrer au même endroit où mes Jupyter notebooks, les gars, il a créé un dossier, je suppose, vous pouvez l'enregistrer à n'importe quel endroit où votre fichier notebook est ouvert, n'est-ce pas ? Donc ce n'est pas nécessaire.

Et juste pour s'assurer que vous ne voyez aucun de mes fichiers.

D'accord, et je l'enregistre simplement.

D'accord, je l'enregistre comme test un ici, vous pouvez voir que je l'enregistre comme test un point CSV.

Donc je vais l'enregistrer.

Gardons ce fichier particulier enregistré.

D'accord.

Maintenant, si je veux probablement, vous savez, lire avec les pandas, ce que nous écrivons, nous écrivons PD dot read underscore CSV, n'est-ce pas.

Et j'utilise essentiellement cet ensemble de données particulier appelé test un point CSV, n'est-ce pas.

Donc lorsque je l'exécute ici, vous serez en mesure de voir les informations spécifiques.

Maintenant, lorsque je veux vraiment travailler avec PI Spark, toujours, tout d'abord, rappelez-vous, nous devons démarrer une session spark.

Et afin de démarrer une session spark, tout d'abord, laissez-moi créer quelques champs supplémentaires.

Voir cela, suivez simplement ces étapes particulières, ou concernant la création d'une session de passe.

Donc, je vais écrire from pi Spark, dot SQL, input spark session.

Ok.

Et puis je vais exécuter cela, vous pouvez voir que cela s'exhibe bien, alors d'accord, désolé, je ne sais pas ce qui s'est ouvert.

Donc, je vais écrire, je vais créer une variable appelée a spark.

Et probablement, je vais utiliser le spark session dot builder.

Et je vais dire app name.

Et ici, je vais juste donner mon nom de session.

D'accord.

Donc, ce sera comme pratique.

Supposons que je pratique ces choses.

Et puis je peux dire get or create.

Donc, lorsque je l'exécute réellement, vous serez en mesure de nous voir, la session barks sera créée.

Et si vous l'exécutez pour la première fois, cela prendra probablement un certain temps.

Autrement, si je l'ai exécuté plusieurs fois, alors vous serez en mesure de travailler.

Maintenant, ici, vous pouvez définitivement voir que, dans cela, lorsque vous exécutez en local, il y aura toujours un seul cluster, mais lorsque vous travaillez réellement dans le cloud, vous pouvez créer plusieurs clusters et instances, d'accord.

Donc, la version spark que vous allez utiliser est V 3.1.

point un.

Ici, vous pouvez voir que cela est essentiellement présent dans le master, lorsque probablement vous allez travailler dans plusieurs instances, vous allez voir masters et cluster un, cluster deux, toutes ces sortes d'informations.

D'accord, donc cela concerne spark.

Maintenant, écrivons simplement le F de pi Spark, où je vais essayer de lire un ensemble de données concernant spark, d'accord.

Maintenant, afin de lire un ensemble de données, ce que je peux écrire, je peux écrire comme ceci spark dot read dot, il y a beaucoup d'options comme CSV format, JDBC, Parque qL, schema, table text, beaucoup d'options là.

Donc ici, nous allons prendre CSV, et ici, je vais simplement écrire tips, one, tips, one dot CSV, n'est-ce pas ? Et si je essaie simplement de l'exécuter ici, j'obtiens une erreur disant que ce fichier particulier n'existe pas.

Laissez-moi voir.

Je pense que ce fichier est présent.

Laissez-moi voir, les gars, pourquoi cela ne s'exécute pas tips, one, b, f file open.

Ici, je peux voir test one dot CSV, d'accord, désolé, je n'ai pas écrit le fichier CSV, je suppose, test one dot CSV.

D'accord, cela a maintenant fonctionné.

Maintenant, si je vais et vois les points blancs, pi Spark, il montre ces deux chaînes, n'est-ce pas, cette colonne C zéro et C un.

Maintenant, vous pouvez voir que j'ai créé ce fichier CSV particulier, n'est-ce pas.

Et il prend simplement ce A B comme colonne par défaut probablement.

Donc, il dit c zéro et C un.

Donc, ce que nous pouvons réellement faire, c'est que probablement si vous voulez vraiment voir tout votre ensemble de données, vous pouvez essentiellement voir comme ceci df underscore pi spark dots show you ici, vous serez en mesure de voir le nom et l'âge, il y a cette information que je veux vraiment faire de ma colonne nom ou âge comme ma colonne principale, n'est-ce pas.

Mais lorsque je lis directement le fichier CSV correctement, nous obtenons underscore Cesar underscore c un.

Donc, afin de résoudre cela, ce que je vais faire, c'est que nous avons une technique de fichier différente, n'est-ce pas, spark dot read dot option, il y a quelque chose appelé option.

Et à l'intérieur de cette option, ce que vous pouvez essentiellement donner, c'est qu'il y aura une option concernant l'en-tête, je suppose, voyez, il y aura quelque chose comme une valeur clé que vous allez fournir une option.

Donc, ce que vous pouvez faire, vous pouvez simplement écrire header, virgule true.

Donc, quelle que soit la valeur de la première colonne, la valeur de la première ligne sera là, cela sera considéré comme votre en-tête.

Et si j'écris CSV concernant test one, maintenant je vais simplement lire cet ensemble de données test one test one dot CSV.

Maintenant, une fois que j'exécute cela ici, vous serez en mesure de voir que j'obtiens maintenant le nom de la chaîne h string, d'accord, mais voyons notre ensemble de données complet.

Donc, ici, si j'exécute cela maintenant, je serai en mesure de voir l'ensemble de l'ensemble de données avec ces colonnes particulières.

D'accord, donc laissez-moi simplement enregistrer cela rapidement dans mon df underscore pi Spark.

D'accord, et maintenant, allons voir le type de df underscore pi spark, d'accord.

Maintenant, lorsque j'exécute cela ici, vous serez en mesure de voir, les gars, lorsque je lis ce df, lorsque j'étais, si je vais et vois le type de cela avec l'aide de pandas, ici, vous serez en mesure de voir qu'il y a des partenaires ou core dot frame dot data frame, mais ici vous verrez que lorsque vous lisez cet ensemble de données particulier, il est de type pi spark dot SQL dot data frame dot data frame.

Oui, donc c'est un DataFrame pandas, ce SQL dot data frame Rhonda, oui, la plupart des API sont presque les mêmes, les fonctionnalités sont vues, beaucoup de choses que nous allons apprendre au fur et à mesure que nous avançons.

Mais si je veux rapidement voir mon probablement, je ne sais pas si head va fonctionner, voyons, oui, head fonctionne aussi.

Donc, si j'utilise dot head, probablement vous serez en mesure de voir les informations des lignes qui sont essentiellement montrées ici.

Maintenant, si je veux vraiment fournir plus d'informations concernant mes colonnes, je serai en mesure d'utiliser quelque chose appelé print schema.

D'accord.

Maintenant, dans ce print schema, c'est comme un df dot info qui vous dira réellement vos colonnes comme le nom est une chaîne et l'âge est une chaîne.

D'accord, donc toutes ces opérations de base que vous avez réellement faites après l'installation.

Encore une fois, la chose principale sur laquelle je me concentre est que vous essayez simplement d'installer ce PI spark et de le garder prêt pour ma prochaine session, je vais essayer de vous montrer comment nous pouvons changer le type de données, comment nous pouvons travailler avec des data frames, comment nous pouvons réellement faire le pré-traitement des données, comment nous pouvons gérer les valeurs nulles, les valeurs manquantes, comment nous pouvons supprimer les colonnes, comment nous pouvons faire diverses choses, toutes ces choses seront essentiellement discutées là-bas, comment supprimer les colonnes.

Et donc, les gars, nous allons continuer la série PI spark.

Et dans ce tutoriel, nous allons en fait voir ce que sont nos PI spark data frames, nous allons essayer de lire l'ensemble de données, vérifier les types de données des colonnes, nous avons essentiellement vu le schéma de couleur pi spark, puis nous verrons comment nous pouvons sélectionner les colonnes et faire l'indexation.

Nous verrons la fonctionnalité describe qui est similaire à pandas, puis nous allons essayer de voir comment nous pouvons ajouter de nouvelles colonnes et probablement supprimer des colonnes.

Maintenant, ceci n'est que la partie un.

Donc, laissez-moi simplement l'écrire comme partie un, car après cela, il y aura aussi une autre partie, pourquoi cette vidéo sera importante car dans PI Spark, aussi, si vous prévoyez d'appliquer l'emblème, vous savez, les bibliothèques de machine learning, vous devez vraiment faire le pré-traitement des données initialement, vous savez, probablement dans la partie deux, nous allons essayer de voir comment gérer les valeurs manquantes.

Et tout, nous allons essayer de voir comment filtrer les lignes, comment nous pouvons probablement mettre une condition de filtre et tout va bien, alors procédons.

Avant d'aller de l'avant, ce que je vais faire, c'est que nous allons d'abord créer un ensemble de données appelé test un.

Donc, j'ai pris trois colonnes.

L'une est le nom, l'âge et l'expérience.

Et puis j'ai un ensemble de données comme Krish Taki 110, comme ceci Sudan shoe Sunday, n'est-ce pas.

Donc, c'est un ensemble de données que vous avez enregistré au même endroit.

Maintenant, ce que je vais faire, tout d'abord, comme d'habitude, la première étape concernant pi spark est de construire la session PI spark.

Maintenant, afin de construire la session PI spark, je vais écrire le code ligne par ligne.

Veuillez donc vous assurer que vous le faites également avec moi, cela sera définitivement utile.

Donc, je vais écrire from pi Spark, dot SQL, input, sparks session, et puis je vais créer une variable, oops, désolé, puis je vais commencer à créer une variable concernant ma session.

Donc, je vais écrire spark est égal à sparks session.we, essentiellement, comme builder dot app name.

Et ici, je vais juste donner mon nom d'application comme pratique, je peux simplement dire, ou liquide data frame pratique ou data frame, n'est-ce pas, quelque chose comme ceci, puisque nous pratiquons data frame dot get or create function.

Et c'est ainsi que vous commencez réellement une session.

Donc, encore une fois, si vous exécutez pour la première fois, cela prendra un certain temps, sinon, c'est parfait pour y aller.

Donc, voici tout mon Spark, il fonctionne en mémoire, la version qu'il exécute ici.

Et évidemment, lorsque vous exécutez en local, vous avez essentiellement un nœud maître, d'accord, et le nom de l'application est data frame.

Pour commencer, nous allons essayer de lire à nouveau l'ensemble de données.

Donc, lisons l'ensemble de données.

Maintenant, la lecture de l'ensemble de données, je vous ai déjà montré plusieurs façons.

L'une consiste à lire l'option, l'autre est de et puisque c'est un fichier CSV, nous allons essayer de le lire d'abord, la première option, nous allons essayer de voir comment nous pouvons réellement le lire.

Et puis je vous montrerai plusieurs façons de le lire.

D'accord, donc je vais écrire spark dot read dot options.

Et ici, dans cette option, nous disons essentiellement clé valeur, n'est-ce pas, donc ici, je vais simplement le définir comme header est égal à true afin que, vous savez, il devrait considérer ma première ligne comme l'en-tête.

Et ici, je vais l'écrire comme header, c'est vrai, dot CSV, à l'intérieur du CSV.

Je vais donner le nom de mon ensemble de données qui est appelé test un.

point c est correct.

Maintenant, lorsque je l'exécute, probablement, je pense que vous serez en mesure de voir l'ensemble de données.

Donc, ici, vous êtes en mesure de voir que d'accord, c'est un data frame, et il aura des caractéristiques comme nom, âge, expérience, n'est-ce pas ? Donc, si je veux voir l'ensemble de données complet, je vais simplement écrire dot show.

Donc, voici tout mon ensemble de données ici très clairement, je peux le voir.

Maintenant.

Laissez-moi simplement sauvegarder cela dans une variable appelée df underscore pi Spark.

D'accord, donc voici tout mon ensemble de données.

Maintenant, première chose, comment vérifions-nous le schéma, vérifions le schéma.

D'accord, le schéma signifie essentiellement les types de données comme nous écrivons dans pandas df dot info, de manière similaire, nous pouvons écrire ici.

Donc, ici, vous serez en mesure de voir que j'ai écrit df underscore pi spark dot print, je pense que cela devrait fonctionner, print schema ou none type a spring theme, oh désolé.

Donc, j'avais écrit dot show et sauvegardé dans une variable, je vais supprimer ce dot show, laissez-moi l'exécuter une fois de plus.

Et maintenant, si j'écris print schema, ici, vous serez en mesure de voir le nom, l'âge et l'expérience, mais par défaut, il prend une chaîne même si dans ma feuille Excel, ce que nous avons fait, c'est que nous avons écrit des valeurs, probablement cela devrait être une chaîne, cela devrait être des entiers, puis ils devraient être des entiers, mais pourquoi cela prend une chaîne.

La raison pour laquelle cela prend probablement une chaîne, les gars, c'est que par défaut, à moins que nous ne donnions une autre option dans CSV, ce CSV a une option appelée infer schema, d'accord ? Si je ne fais pas de cela une vraie valeur, n'est-ce pas ? Il considérera par défaut toutes les caractéristiques comme vous le savez dans la valeur de la chaîne, les valeurs de la chaîne.

Donc, je vais l'exécuter maintenant.

Et maintenant, si je vais et vois le F underscore pi spark dot print, Sima, vous serez en mesure de voir que j'obtiens le nom et la chaîne, l'âge comme entier, l'expérience comme entier et un niveau égal à deux, ce qui signifie essentiellement qu'il peut avoir des valeurs nulles.

D'accord, donc c'est une façon de le lire.

Une autre façon, je vais essayer de vous montrer, qui est assez simple, donc je peux inclure à la fois l'en-tête et infer schema en une seule chose.

Donc, je vais écrire d f underscore pi spark est un appel à spark dot read dot CSV et à l'intérieur du fichier CSV, tout d'abord, je vais fournir mon fichier de test CSV, d'accord, et puis ici, je vais continuer et écrire l'en-tête probablement est égal à vrai et je peux écrire infer schema est égal à, donc lorsque j'écris comme ceci et si j'écris df underscore pi spark dot show you ici, vous serez en mesure de voir toutes mes données, d'accord, donc voici toutes mes données.

Maintenant, si je vais et vois et exécute ce schéma à nouveau, il me donnera probablement la même chose que nous avions ici, d'accord.

Donc, ici, vous pouvez voir que le nom est égal à la chaîne, l'âge est égal à l'entier, l'expérience est égale à l'entier, parfait.

Donc, quelles sont les choses que nous avons faites, nous avons compris à propos de ceci et de cela, si je vais et vois le type de ceci, si je vais et vois le type de ceci, c'est essentiellement un data frame.

pandas a aussi un data frame.

Donc, si quelqu'un vous demande en entretien, qu'est-ce qu'un data frame, vous pouvez essentiellement dire qu'un data frame est une structure de données, vous savez, parce qu'à l'intérieur de cela, vous pouvez effectuer divers types d'opérations.

Donc, c'est aussi un type de structure de données.

D'accord, donc quelles sont les choses que nous avons réellement faites, je vous ai donné une introduction au data frame, à la lecture de l'ensemble de données, à la vérification des types de données de la colonne.

Afin de vérifier les types de données de la colonne, nous avons déjà écrit print schema.

D'accord, maintenant, une autre chose que je peux faire après cela, voyons, sélectionner des colonnes et indexer.

Tout d'abord, comprenons quelles colonnes sont essentiellement présentes, comment vous pouvez obtenir tous les noms de colonnes.

Donc, afin d'obtenir les noms de colonnes, vous pouvez simplement écrire dot colonnes, d'accord.

Et lorsque vous exécutez ici, vous serez en mesure d'obtenir le nom de la colonne comme nom, âge, expérience, parfait, c'est parfaitement bien.

Maintenant, c'est mon D F.

Maintenant, supposons que je veux prendre quelques éléments de tête, aussi, je serai en mesure de les prendre car dans pandas aussi, vous n'aviez pas de tête, supposons que je vois, je veux obtenir les trois premiers enregistrements.

Je les obtiendrai dans ce format particulier, dans le format de liste.

Habituellement, dans pandas, lorsque nous utilisons, nous obtenons généralement dans un format de data frame.

Donc, ici, vous verrez la combinaison de nom, âge et expérience.

D'accord, comme ceci.

C'est ma première ligne, c'est ma deuxième ligne, c'est ma troisième.

D'accord, maintenant, passant à la chose suivante que nous allons discuter maintenant, comment sélectionner une colonne ? Vous savez, je veux probablement prendre une colonne et voir tous les éléments, n'est-ce pas, comme nous le faisons dans pandas.

Donc, tout d'abord, laissez-moi simplement l'écrire comme ceci PI spark dot show ici, nous serons en mesure de voir toutes les colonnes sont si je veux vraiment prendre la colonne nom.

D'accord, donc comment faire ? D'accord, essayons de voir.

Maintenant, afin de prendre la colonne nom, il y a une fonctionnalité très simple que nous allons écrire qui est appelée pi spark dot select.

Et ici, je vais simplement donner ma colonne nom.

Maintenant, une fois que j'exécute cela, vous serez en mesure de voir que le type de retour est data frame.

D'accord, le type de retour est data frame, et le nom est essentiellement une chaîne.

Maintenant, si j'écris dot show, je serai en mesure de voir la colonne entière.

D'accord, donc lorsque je fais cela, je serai en mesure de voir cela et si j'essaie de trouver le type de cela, désolé, si je supprime ce dot show et vois le type de cela, c'est essentiellement un data frame par spark dot SQL dot data frame dot data for not pandas dot data frame.

D'accord, assez simple.

Maintenant, supposons que je veux prendre plusieurs lignes, comme désolé, plusieurs colonnes, comme je veux prendre le nom et l'expérience, probablement deux colonnes que je veux prendre, donc ce que je vais faire, je vais simplement faire un changement.

Ici.

Initialement, je fournissais le nom de ma colonne comme ceci.

Après cela, ce que je vais faire, je vais fournir une autre colonne qui est comme expérience, et je vais exécuter cela maintenant, une fois que je l'exécute ici, vous pouvez voir que les gars, j'obtiens un data frame avec deux caractéristiques, l'une est le nom et l'expérience.

Maintenant, si je vais et écris dot show, ici vous serez en mesure de voir tous mes éléments sont essentiellement présents à l'intérieur de ce data frame particulier.

Assez simple, comment sélectionnez-vous plusieurs lignes ? Et oui, ici, le slicing ne fonctionnera définitivement pas car j'ai essayé de faire du slicing, cela ne fonctionnait pas, d'accord ? Et, d'accord, chaque fois que vous avez des préoccupations, essayez toujours de voir la documentation, la documentation PI spark, assez simple.

D'accord, c'est une façon de savoir comment nous pouvons réellement sélectionner les colonnes et probablement voir les lignes.

D'accord.

Maintenant, laissez-moi vous montrer si je veux simplement prendre, il y a aussi une façon comme le voir si j'écris le F de pi spark off named.

Si je l'exécute ici, vous serez en mesure de voir le nom de la colonne là.

Le type de retour sera la colonne ici, si je la prends directement parce que dans pandas, nous la prenons directement comme ceci, n'est-ce pas.

Et lorsque nous avons ce genre de colonnes, nous ne pouvons définitivement pas, nous sommes simplement capables de comprendre ce qu'est cette caractéristique particulière, c'est essentiellement une colonne, elle dit, d'accord, rien de plus, nous ne serons pas en mesure d'obtenir l'ensemble de données, il y aura une erreur, elle dira qu'elle est essentiellement une erreur.

Donc, habituellement, ce que nous faisons, chaque fois que nous voulons obtenir une colonne et essayer de la voir, nous devons essentiellement sélectionner en utilisant cette opération de sélection particulière, qui est ma fonction.

D'accord, donc ces choses ont été faites, les gars, ce que nous essayons de comprendre maintenant, voyons comment nous pouvons vérifier les types de données.

Donc, il y a une fonctionnalité qui est appelée D types.

Donc, ici, vous serez en mesure de voir que le nom est appelé une chaîne, l'âge est égal à la fin, l'expérience est égale à l'entier.

Et encore, D types est très similaire car nous utilisons aussi cela dans pandas.

D'accord, la plupart des fonctionnalités sont similaires à pandas, les gars.

Donc, quelles sont les choses que nous avons réellement faites ? Voyons, pi spark DataFrame, lecture de l'ensemble de données, vérification du type de données, sélection des colonnes et indexation, vérification des options de description similaires à pandas.

Donc, nous pouvons également vérifier les options de description.

Donc, voyons pi spark dot describe et si je l'exécute, vous serez en mesure de voir qu'il vous donnera un résumé du data frame est égal à la chaîne, cette information est là.

Maintenant, lorsque j'écris dot show, d'accord, vous serez en mesure de voir tout cela, cela est essentiellement sous la forme de data frame, vous pouvez penser pourquoi ces valeurs nulles viennent de la moyenne et de la division standard, car même dans cela, il prendra la colonne de chaîne, essentiellement les valeurs qui ont le type de données de chaîne, nous avons évidemment rien, donc min et max sont essentiellement pris sur l'index, car dans les zéros dans le deuxième index, vous serez en mesure de voir dans les écrasements, puis après cela, Sonny est là, d'accord, cherchez le suivant et toutes ces informations sont réellement présentes.

Donc, c'est essentiellement la même chose que les options de description que nous avons réellement vues, vous savez, probablement dans nos pandas, n'est-ce pas, donc de manière similaire, nous avons réellement fait cela.

D'accord, donc l'option de description est également faite.

Donc, allons-y et voyons l'ajout de colonnes, la suppression de colonnes.

Donc, l'ajout de colonnes et la suppression de colonnes est très, très simple, les gars, si nous devons ajouter les colonnes, donc je vais simplement écrire le commentaire ici, ajouter des colonnes dans un data frame, et ce data frame est par pi spark data frame, d'accord, maintenant afin d'ajouter la colonne, donc nous avons une fonction d'ajout incroyable, qui est appelée comme le PI spark dot, il y a quelque chose appelé comme width column.

D'accord ? Maintenant, ce width column, si je vois la fonctionnalité, il retourne un nouveau data frame en ajoutant une classe ou en remplaçant la colonne existante qui a le même nom.

D'accord, donc ici, le premier paramètre que je vais donner est le nom de ma colonne.

Supposons que je veux prendre, voyons, je vais prendre l'expérience.

Donc, je vais dire expérience, d'accord.

Et probablement, ce sera ma nouvelle colonne.

Après deux ans, que va-t-il se passer si l'expérience après deux ans, vous savez, initialement, le candidat a 10 ans d'expérience, après deux ans, cela deviendra 12.

D'accord, donc nous allons essayer de mettre maintenant la valeur, c'est le nom de ma nouvelle colonne, et quelle valeur elle devrait avoir.

Donc, pour cela, je vais écrire df pi Spark.

Et ici, je vais dire, probablement, je vais prendre cette même expérience, je vais la multiplier par, je vais ajouter comme deux parce qu'après deux ans, l'expérience sera ajoutée par deux, je prends juste une façon de résoudre cela, je peux mettre n'importe quelles valeurs que je veux, les gars, c'est à vous.

D'accord, et vous pouvez réellement vérifier cela.

D'accord, maintenant après cela, ce sont seulement les deux choses qui sont requises.

Et maintenant, si je l'exécute, vous serez en mesure de voir que la même opération se produira.

Et maintenant, dans ce data frame, vous avez 123 et quatre caractéristiques, si je veux voir l'ensemble de données complet, je peux ajouter dot show, une fois que je l'exécute maintenant, ici, nous verrons que l'expérience après deux ans n'est rien d'autre que 266 parce que 10 plus 212, vous avez très simple, le reste et c'est ce que width column nous a essentiellement dit et vous pouvez aussi faire différentes choses à ce sujet.

C'est ainsi que vous ajoutez une colonne dans un data frame.

Et encore une fois, les gars, ce n'est pas une opération en place, vous devez essentiellement l'assigner à une variable afin qu'elle soit reflétée.

Supposons que je veux qu'elle soit reflétée, j'ai vraiment besoin de l'assigner comme ceci.

Et ici, maintenant, si je vais et vois mon désolé, tout d'abord, laissez-moi supprimer le show.

Le show ne nous donnera pas de résultat correct.

D'accord, oh n'a pas d'attribut avec colonne.

D'accord, désolé.

Donc, il y avait un problème à ce sujet, je vais relire cet ensemble de données, car je l'ai complètement remplacé, n'est-ce pas.

Maintenant, je vais l'exécuter.

Et encore une fois, maintenant, c'est bien.

Maintenant, si je vais et écris dot show, ici, vous serez en mesure de voir tous les éléments correctement donnés.

Maintenant, cela concernait l'ajout des colonnes avec le data frame.

Maintenant, je dois probablement aussi supprimer les colonnes.

Donc, supprimer les colonnes.

Voyons comment nous pouvons réellement supprimer les colonnes.

Supprimer les colonnes est assez simple, comme nous le faisons habituellement avec cette fonctionnalité de suppression.

Par défaut, les noms des colonnes, vous pouvez donner une liste de colonnes.

Vous pouvez donner un seul nom de colonne.

Donc, supposons que je dise expérience après deux ans, je veux supprimer cela, parce que qui sait, après deux ans, ce qui va se passer.

Donc, supprimons cela, afin de supprimer cela, exécutez simplement comme ceci et allez voir dot show.

Ici, vous serez en mesure de trouver sans cette colonne spécifique.

Encore une fois, ce n'est pas une opération en place, vous devez l'assigner à une variable, très simple.

Donc, laissez-moi simplement l'assigner à une variable est égal à et assurez-vous de supprimer ce dot show, dot show est la fonctionnalité, n'est-ce pas ? Maintenant, si j'écris ce dot show, ici, vous serez en mesure de voir tous les éléments.

Mais maintenant, allons de l'avant et voyons comment renommer la colonne.

Donc, nous faisons simplement cela, les gars, parce que vous devez vraiment être très bon en pré-traitement des données, d'accord, donc je vais écrire le hot et il y a une autre fonction, qui est appelée comme with column rename.

D'accord ? Neuf, cela vous donne simplement votre colonne existante et le nouveau nom de colonne.

Supposons que j'ai le nom de ma colonne existante ici, je vais dire, nom.

Et je vais dire new name.

D'accord, et juste exécuté.

Et maintenant, si je vais et juste comme dot show, et essaie de voir les éléments ici, vous serez en mesure de voir au lieu de nom, il y aura quelque chose appelé comme new name.

D'accord.

Maintenant, c'est ce que j'avais à discuter.

Je vais écrire un autre point ici.

Nous avons également discuté du renommage des colonnes, n'est-ce pas ? Oui, ce n'est que la partie un des data frames, la partie deux, nous allons essayer de faire quelque chose appelé opération de filtre.

Et dans l'opération de filtre, nous allons essayer de voir diverses opérations car cela sera assez incroyable, vous serez en mesure d'apprendre beaucoup probablement, c'est le tutoriel trois, qui est la partie trois concernant les opérations de data frame.

Dans cette vidéo particulière, nous allons voir comment nous pouvons gérer les valeurs manquantes, les valeurs nulles, vous savez.

Donc, en bref, toutes ces choses que nous allons essayer de faire, nous allons voir comment supprimer les colonnes, nous allons voir comment supprimer les lignes, puis nous allons voir quand nous supprimons les lignes, probablement en fonction des valeurs nulles, nous allons essayer de supprimer les roses.

Et puis nous allons essayer de voir quels sont les différents paramètres dans les fonctionnalités de suppression et de gestion des valeurs manquantes par la moyenne, la médiane ou le mode.

D'accord, donc ici, je vais simplement l'écrire comme moyenne, médiane, et plus probablement, n'est-ce pas.

Donc, toutes ces choses que nous allons essayer de voir, encore une fois, la chose principale est que je veux vraiment vous montrer comment nous pouvons gérer les valeurs manquantes.

C'est assez important car dans pandas, et aussi nous essayons de le faire dans une échelle, nous avons une sorte de fonction intégrée.

Donc, procédons.

Chaque fois que nous commençons généralement pi Spark, chaque fois que nous travaillons avec PI Spark, nous devons vraiment démarrer une session PI spark.

Donc, j'espère que jusqu'à maintenant, vous êtes tous familiers.

Donc, je vais écrire pour pi spark dot SQL, je vais importer sparks session, encore une fois.

Et puis je vais créer une variable avec Spark.

Et puis ici, je vais écrire spark session dot builder.

Ce n'est pas en train de se passer.

D'accord, pas de nom d'application.

Encore une fois, laissez-moi juste garder ce nom d'application comme pratique, d'accord, parce que je pratique juste des choses, puis j'aime get or create et juste l'exécuter.

Donc, dans l'ensemble, cela prendra un certain temps pour être exécuté.

Oui, cela a été exécuté correctement.

Maintenant, pour cela, j'ai juste créé un ensemble de données très simple, qui ressemble à ceci.

J'ai une colonne comme nom, âge, expérience, salaire.

Donc, ce sont toutes mes caractéristiques, tous les noms des candidats, et probablement il y a certaines valeurs qui sont laissées en blanc.

Ici, vous pouvez voir certaines valeurs que j'ai laissées en blanc.

Donc, nous allons essayer de voir comment probablement supprimer les valeurs nulles ou comment gérer ces valeurs manquantes ou non.

D'accord, donc procédons.

Donc, tout d'abord, afin de lire l'ensemble de données, je vais simplement écrire spark dot read dot CSV.

Et ici, je vais simplement utiliser le nom du fichier CSV qui est deux points CSV.

Et il est enregistré au même endroit où se trouve ce fichier particulier, de toute façon, je vais vous le fournir dans ces données.

Et je vais utiliser header est égal à true et probablement il y a aussi info schema est égal à true, donc que je serai en mesure d'obtenir l'ensemble de données correctement.

Donc, probablement lorsque je lis cela, vous serez en mesure de voir que c'est mon data frame que je suis en train d'obtenir, si vous voulez voir l'ensemble de données complet, cela sera comme show us dot show.

Et c'est votre ensemble de données complet ici, vous avez des valeurs nulles sous parfait.

Donc, laissez-moi faire une chose, laissez-moi simplement l'enregistrer dans une variable.

Donc, je vais écrire df underscore pi Spark.

Donc, si je vais et vérifie maintenant, dots show et c'est tout mon ensemble de données.

D'accord, parfait.

Nous sommes assez bons, 10, ici, nous travaillons bien.

Par rapport à cela.

Nous savons que nous avons réellement lu un ensemble de données.

Maintenant, probablement, commençons.

Comment supprimer les colonnes ? Supprimer les colonnes est très, très simple, les gars.

Supposons que je veux supprimer la colonne Nom, alors je me contente d'utiliser df dot drop et de fournir le nom de ma colonne comme ceci, n'est-ce pas ? Donc, colonne, n'est-ce pas, le nom de la colonne, supposons que j'écrive df.pi spark et ici, le nom de la colonne sera nommé.

Donc, laissez-moi l'écrire comme nom.

Et je peux essentiellement aller et vérifier mon dot show.

Et puis vous serez en mesure de voir toutes les caractéristiques qui sont réellement présentes.

C'est assez simple, que je vous ai probablement montré aussi dans la session précédente, d'accord.

Et c'est ainsi que cela est essentiellement fait, en supprimant essentiellement votre caractéristique ou une colonne, mais notre principal objectif est de supprimer la valeur non.

Donc, maintenant, laissez-moi simplement écrire df.pi spark dot show.

Donc, c'est mon ensemble de données, n'est-ce pas ? Maintenant, voyons comment supprimer ces lignes spécifiques basées sur les valeurs nulles.

Donc, ici, je vais simplement utiliser df.by spark.na.

D'accord, il y a quelque chose appelé na et puis vous avez drop, fill et replace.

Donc, tout d'abord, je vais commencer par drop.

Maintenant, à l'intérieur de ce drop particulier, rappelez-vous toujours que si je ne donne rien, d'accord, et que je l'exhibe simplement, vous serez en mesure de voir que partout où il y a des valeurs nulles, toutes ces lignes seront supprimées.

Donc, ici, nous verrons que ces trois dernières lignes ne sont pas présentes, n'est-ce pas ? Donc, ici, vous pouvez voir que la valeur particulière de Shibam est présente, ce qui signifie que toutes les lignes ont été supprimées, parfait, n'est-ce pas.

Donc, pas de problème du tout.

Donc, vous aviez en bref ce que vous faites, c'est que lorsque vous utilisez .na dot drop, il va simplement supprimer partout où il va supprimer ces lignes où les valeurs nulles sont réellement présentes, d'accord, parfait, ce match est bien.

Si je vais et cherche dans le drop, il y a deux caractéristiques principales, l'une est how et l'autre est threshold et puis une est subset.

Donc, essayons de comprendre ces caractéristiques particulières.

Maintenant, d'abord, je vais commencer par how any est égal à how, je viens d'essayer comme ceci, d'accord.

Donc, supposons que j'écrive df.pi spark.na dot drop et si ma valeur how peut avoir deux valeurs, l'une est any, l'autre est all, d'accord, l'une est any, l'autre est on any si la valeur sélectionnée est any drop une ligne si elle contient des notes comme même s'il y en a juste une, d'accord, l'un des riches tuners ou il y a un emblème entier, vous savez, none par défaut, il va être supprimé, d'accord.

Mais comment est l'appel à all, quand utilisons-nous all, cela signifie essentiellement que supposons que dans votre futur, vous avez, supposons que dans une règle, vous avez toutes les valeurs comme null, dans ce cas, vous avez 36, une valeur, cela ne sera pas supprimé, mais si vous avez dans un enregistrement, vous avez toutes les valeurs et ml, alors seulement il sera supprimé, d'accord.

Donc, voyons si cela va fonctionner ou non, cela ne va définitivement pas fonctionner car je sais qu'au moins une valeur ou au moins une valeur, une valeur non nulle est toujours là, n'est-ce pas ? Si j'utilise How est égal à all, il va supprimer ces enregistrements qui ont complètement non par défaut, cette valeur how devrait avoir any, n'est-ce pas, par défaut, c'est any, any dit essentiellement que qu'il y ait une ou deux maintenant, nous allons simplement le supprimer, supprimer ces enregistrements spécifiques, n'est-ce pas.

Assez simple, c'était ce que how était et allons-y et essayons de comprendre par rapport au seuil, qu'est-ce que ce seuil, je vais vous dire ce qu'est ce seuil, maintenant, laissez-moi simplement utiliser ceci, d'accord, je sais que how est any, mais il y a une autre option appelée thrush nine, Thresh, ce que nous faisons, c'est que supposons que je dise, gardons le seuil à deux, cela signifie essentiellement que supposons que dans ce cas particulier, si la valeur de seuil est deux, d'accord, laissez-moi d'abord l'exécuter, vous serez en mesure de voir que la dernière colonne a été supprimée ici, d'accord, c'est la dernière ligne qui a été supprimée, pourquoi elle a été supprimée parce que nous avons gardé la valeur de seuil à deux, cela dit qu'au moins deux valeurs non nulles doivent être présentes, d'accord, au moins deux valeurs non nulles, maintenant ici, vous avez deux valeurs non nulles comme plus de 40 000, d'accord, ici, vous avez juste une valeur non nulle.

Donc, à cause de cela, il a été supprimé, supposons que vous aviez deux valeurs non nulles ici, voyez 34 et 10, cela n'a pas été supprimé, c'est la même chose ici, 3410, n'est-ce pas, 3410, vous avez si je vais et vous montre 3410 ici et 38 000, il y a au moins ici, vous ajoutez trois valeurs normales, ici, vous ajoutez deux valeurs normales.

Donc, ici, chaque fois que nous donnons une valeur de seuil, cela va essentiellement vérifier si dans cette ligne spécifique, au moins deux valeurs non nulles sont là, si elles sont là, cela va simplement garder cette ligne, sinon, cela va simplement la supprimer, c'est ce que vous ne pouvez pas faire, vous pouvez aussi vérifier avec le un, donc si je vais et vois un, alors vous pouvez voir que toutes ces lignes particulières sont là parce que cela va simplement vérifier, d'accord, ici, une valeur non nulle est là, ici, elle est là.

Si je la mets à trois, d'accord, voyons ce qu'il va venir.

Maintenant, ici, vous pouvez voir au moins cela, il reste, tout le reste a été supprimé, n'est-ce pas, voyez ici, vous n'aviez que deux valeurs non nulles, ici aussi, vous avez ajouté trois, donc c'est le 3410 38 009, donc ici, vous pouvez voir la valeur qui comprend par rapport au seuil.

Maintenant, passons à l'autre, nous allons simplement appeler un sous-ensemble.

Donc, ici, je vais simplement l'écrire comme un sous-ensemble, car c'est le troisième paramètre à l'intérieur de ma fonction de suppression.

Et rappelez-vous, ces caractéristiques sont assez simples par rapport à si vous avez travaillé avec pandas, la même chose que nous faisons, sous-ensemble dans le sous-ensemble, nous pouvons réellement fournir.

Supposons que je dise dans le sujet, enlevez le seuil, je ne veux pas garder de seuil, disons que je veux simplement supprimer les valeurs nulles uniquement pour ma colonne spécifique, probablement uniquement à partir de la colonne expérience, alors je peux essentiellement le donner comme un sous-ensemble.

Donc, à partir de la colonne expérience, vous pouvez voir que partout où il y avait des valeurs nulles dans les enregistrements, tous ces enregistrements ont été supprimés, n'est-ce pas.

Donc, comme ceci, vous pouvez appliquer par rapport à, supposons que vous voulez l'appliquer dans l'âge, vous pouvez aussi appliquer cela, n'est-ce pas, partout où il y avait des valeurs nulles, cet ancien enregistrement a été supprimé dans la colonne âge.

Donc, c'est par rapport au sous-ensemble, donc j'espère que vous avez une idée, les gars, c'est assez bien parce que la même chose que nous essayons de faire, n'est-ce pas, nous appliquons réellement tout ce que nous avons fait dans pandas et c'est très, très pratique lorsque vous travaillez avec des données manquantes.

D'accord.

Passons à la chose suivante.

Maintenant, allons-y et remplissons la valeur manquante, remplissons la valeur manquante, l'ordre de remplir la valeur manquante, je vais encore utiliser Vf eyespot dot fill dot, désolé na dot fill, d'accord.

Et à l'intérieur de cela, ce champ prendra deux paramètres, l'un est la valeur et l'autre est le sous-ensemble, d'accord.

Maintenant, supposons que je vais et donne une valeur comme ceci, supposons que je dise valeur manquante et si je vais et écris dot show, alors ce qu'il va faire, lorsque qu'il y a une valeur non valide, il va la remplacer par des valeurs manquantes.

Donc, ici, vous pouvez voir que la valeur nulle est là.

Donc, valeur manquante, valeur manquante, valeur manquante.

Supposons que vous voulez vraiment effectuer cette gestion des valeurs manquantes dans une colonne spécifique, alors vous pouvez essentiellement écrire le nom de votre colonne aussi comme ceci.

Donc, ce sera mon sous-ensemble Excel, d'accord.

Je peux aussi donner plusieurs enregistrements comme ceci.

Voyez, je peux aussi donner plusieurs dieux comme expérience karma probablement âge, karma âge en appelant la liste, n'est-ce pas, lorsque je donne comme ceci, alors ce genre de fonctionnalités se produira dans deux colonnes, n'est-ce pas ? Assez simple.

Donc, maintenant, la prochaine étape, ce que nous allons faire, c'est que nous allons prendre une colonne spécifique, et probablement nous allons gérer les valeurs manquantes avec l'aide de la moyenne de cette colonne spécifique ou de la médiane de cette colonne spécifique.

Donc, maintenant, si je vais et vérifie mon bf got pi spark ici, si je vais et vois mon dot show value, c'est tout mon ensemble de données ici.

Maintenant, ce que je vais faire, c'est que je vais prendre cette colonne d'expérience particulière et probablement remplacer les valeurs nulles par la moyenne de l'expérience elle-même.

Donc, afin de faire cela, je vais utiliser une fonction intégrée.

Et les gars, si vous connaissez la fonction d'imputation, nous l'utilisons essentiellement avec l'aide de SK learn aussi dans PI Spark, nous avons aussi une fonction d'imputation.

Donc, je vais simplement copier et coller le code ici pour le rendre très, très simple.

De pi spark.ml dot feature import in pewter, ici, je vais simplement donner mes colonnes d'entrée qui sont l'âge, l'expérience, le salaire, probablement je veux appliquer pour chaque colonne ici.

Et puis je dis simplement que pour l'âge, l'expérience, le salaire, je vais essayer de trouver ce point de format dot c output columns.

Et puis je vais garder la stratégie comme moyenne, vous pouvez aussi changer la stratégie a immédiatement plus que tout.

Donc, je vais l'exécuter, cela a été exécuté correctement, et puis nous allons simplement écrire fit et transform.

Donc, imputed reflect df of pi spark dot transform.

Donc, une fois que j'exécute cela, les gars, ici, vous serez en mesure de voir que nous allons créer plusieurs colonnes avec underscore imputed comme nom.

Donc, ici, vous pouvez voir h underscore imputed.

En bref, ce que nous avons fait, nous avons essayé une sorte de fonctionnalité moyenne ici, ce qui signifie essentiellement que la valeur nulle a été remplacée par la moyenne.

Donc, ici, vous pouvez voir que cette valeur nulle est remplacée par 28.

De même, cette valeur nulle est remplacée par 10 et cinq, désolé, cinq.

C'est ce qu'est la colonne d'expérience imputée.

Ici, vous verrez que partout où il y a une valeur nulle, elle est remplacée par la moyenne de la colonne d'expérience, la moyenne de la colonne d'âge et la moyenne ou la colonne de salaire.

Et de cette manière, vous serez en mesure de le faire si vous voulez vraiment continuer avec la médiane.

Il suffit d'aller et de changer cette moyenne en médiane et d'essayer de l'exécuter.

Ici.

Maintenant, vous serez en mesure de voir la valeur médiane et ici sont vos colonnes initiales nulles, qui avaient désolé, ici sont les colonnes qui ont des valeurs nulles.

Et ici sont toutes les colonnes qui ont essentiellement les valeurs imputées, n'est-ce pas, par rapport à la moyenne médiane.

Donc, les gars, aujourd'hui nous sommes dans le tutoriel quatre des data frames de pi spark.

Et ici, dans cette vidéo particulière, nous allons discuter de l'opération de filtre.

Une opération de filtre est assez importante pour la technique de pré-traitement des données.

Si vous voulez récupérer certains des enregistrements basés sur certaines conditions, ou certains types de conditions booléennes, nous pouvons définitivement le faire avec l'aide de l'opération de filtre.

Maintenant, les gars, veuillez vous assurer que vous suivez cette playlist particulière concernant pi Spark, je vais télécharger de plus en plus de vidéos au fur et à mesure que nous avançons.

Et rappelez-vous une chose de plus, il y avait beaucoup de plaintes de la part des gens qui disent de télécharger SQL avec Python.

Ne vous inquiétez pas, parallèlement, je vais commencer à télécharger SQL avec Python.

Je suis extrêmement désolé, à cause de quelque retard, parce que j'étais occupé avec quelque chose.

Mais je vais m'assurer que je vais essayer de télécharger toutes les vidéos.

Donc, parallèlement, SQL avec Python sera également téléchargé.

Donc, procédons.

Maintenant, tout d'abord, laissez-moi aller et faire quelques cellules.

Aujourd'hui, pour cette application, j'ai pris notre ensemble de données, un petit ensemble de données, qui est appelé test un dot CSV.

Ici, j'ai un ensemble de données comme nom, âge, expérience et salaire.

Et je vais simplement utiliser cela et essayer de vous montrer quelques exemples concernant l'opération de filtre.

Initialement, chaque fois que vous voulez travailler avec PI Spark, vous devez vous assurer que vous installez toutes les bibliothèques.

Donc, je vais utiliser plus pi spark dot SQL import spark session.

Et cela va réellement nous aider à créer une session spark, n'est-ce pas.

Et c'est la première étape chaque fois que nous voulons travailler avec PI Spark, n'est-ce pas.

Donc, nous allons utiliser sparks session dot builder dot app name, puis je vais simplement créer mon app name comme data frame.

Et essentiellement écrire get our create function, qui va réellement m'aider à créer rapidement une session spark, je pense que cela est assez familier pour chacun d'entre vous.

Et procédons, essayons de lire un ensemble de données spécifique.

Donc, ici, ce que je vais faire, je vais simplement créer une variable, df underscore pi Spark, et je vais utiliser la variable spark dot read dot CSV.

Et ici, je vais simplement considérer mon ensemble de données test un dot CSV.

Et ici, je vais simplement m'assurer que nous avons cette option particulière sélectionnée, header est égal à true et infer schema est égal à true, je pense que tout cela, je vous l'ai déjà expliqué, puis si j'écris df.pi spark dot show up, ici, vous serez en mesure de voir votre ensemble de données.

D'accord, donc il est en train de lire, voyons comment nous allons obtenir le résultat.

Donc, voici tout mon résultat.

Maintenant, les gars, comme je vous l'ai montré, nous allons travailler sur une opération de filtre, je vais essayer de récupérer certains des enregistrements en fonction de certaines conditions.

Rappelez-vous, les filtres sont également disponibles dans pandas.

Mais là, vous essayez d'écrire d'une manière différente.

Laissez-moi simplement vous montrer comment nous pouvons effectuer une opération de filtre en utilisant pi Spark.

D'accord, donc les opérations de filtre, laissez-moi en faire un markdown.

Donc, cela semble grand.

Cela semble incroyable.

Laissez-moi faire quelques cellules supplémentaires, parfait.

Maintenant, première étape, comment faire une opération de filtre, supposons que je veux trouver le salaire des personnes qui sont inférieures à probablement 20 000.

D'accord, inférieur ou égal à 20 000.

Encore une fois, j'aimerais que ce soit inférieur ou égal à 20 000.

Maintenant, pour cela, il y a deux façons de l'écrire, la première façon, je vais simplement essayer d'utiliser l'opération de filtre.

Donc, vous avez comme dot filter.

Et ici, vous devez simplement spécifier la condition que vous voulez.

Supposons que j'écrive salaire est inférieur ou égal à 20 000.

Rappelez-vous, ce salaire doit être le même nom de la colonne ici, n'est-ce pas ? Et lorsque j'écris dot show, vous serez en mesure de voir cet enregistrement spécifique.

Et vous serez en mesure de voir, d'accord, inférieur ou égal à 20 000 est ce salaire étranger pour les gens, Sonny Paul a montré sobre ici, vous serez en mesure de voir toutes ces choses avec l'expérience, n'est-ce pas ? Maintenant, c'est une façon, probablement, je viens de prendre.

Après avoir mis cette condition particulière, je veux prendre deux colonnes.

Donc, ce que je peux faire, je peux utiliser cela.

Et puis je peux essentiellement écrire dot select.

Et ici, je vais spécifier mon nom, probablement je veux le nom et l'âge, nom, virgule, âge.

Donc, dot show, je vais le faire.

Maintenant, c'est ainsi que vous pouvez réellement le faire.

Ici, vous pouvez voir que name underscore age est réellement là.

Et vous êtes en mesure d'obtenir cette information spécifique après cela.

Probablement, je veux faire certaines des opérations que vous pouvez réellement faire, moins que plus grand que toutes les choses que vous voulez.

Probablement, je vais mettre deux conditions différentes, alors comment devrais-je le faire ? Voyons.

Voyons aussi pour cela.

Donc, je vais écrire diviser df pi spark dot theta.

Et ici, je vais spécifier ma première condition.

Supposons que c'est une façon.

C'est une façon d'utiliser l'opération de filtre.

Aussi, les gars, alors ces conditions que j'écris, je peux aussi écrire quelque chose comme ceci, voyez ceci, supposons que j'écrive df pi spark of salary, supposons que le salaire est inférieur ou égal à 20 000, je peux aussi écrire comme ceci, je serai aussi en mesure d'obtenir le même résultat.

Donc, ici, vous serez en mesure de voir le même résultat ici.

Maintenant, supposons que je veux écrire plusieurs conditions, comment faire, c'est très simple, je vais prendre cela, cela est, tout d'abord, c'est une de mes conditions.

Donc, je vais simplement utiliser cette condition.

Et je peux aussi utiliser une opération AND, vous savez, donc je vais dire and, or, ou n'importe quel type d'opération que vous voulez, probablement, je veux dire que df underscore pi salary est grand, inférieur ou égal à 2000 20 000.

Et probablement, je veux un df pi spark of salary, salaire supérieur ou égal à 15 000.

Donc, je serai en mesure d'obtenir tous ces enregistrements spécifiques, d'accord.

Et encore une fois, je vais essayer de mettre cela dans d'autres crochets, assurez-vous de le faire, sinon, vous allez obtenir une erreur.

D'accord ? Très, très simple, les gars.

Donc, voyez comment je l'ai réellement écrit, c'est quelque chose comme ceci d f underscore pi spark dot filter df or pi spark of salary est inférieur ou égal à 20 000, supérieur à égal à 15.

Si je l'exécute, vous serez en mesure de voir entre 15 000 et 20 000, vous serez en mesure de trouver, vous pouvez aussi écrire ou alors vous serez en mesure d'obtenir toutes les différentes valeurs.

Maintenant, c'est notre genre d'opération de filtre que vous pouvez essentiellement spécifier, rappelez-vous, cela sera très pratique lorsque vous récupérez certains des enregistrements par rapport à n'importe quel type d'ensembles de données, et vous pouvez essayer différentes choses.

Donc, c'est une façon où vous fournissez directement le nom de votre colonne et mettez une condition, PI spark comprend cela et vous serez en mesure d'obtenir le résultat, n'est-ce pas.

Donc, oui, c'était tout à propos de cette vidéo particulière, j'espère que vous l'avez aimée, j'espère que vous avez aimé cette opération de filtre particulière, essayez simplement de le faire de votre côté.

D'accord, une autre opération est essentiellement en attente, je peux aussi écrire comme ceci, sérieux tout le monde, je peux essentiellement dire, d'accord.

Probablement, je peux utiliser cette opération, qui est appelée une opération de nœud.

Voyons comment cette opération de nœud va venir.

D'accord.

Essentiellement, l'opération de condition inverse, nous disons essentiellement, donc je vais utiliser cela, d'accord.

Et cela, et à l'intérieur de cela, je peux mettre une condition de nœud comme ceci, donc je vais dire que c'est un nœud de df of pi spark salary est inférieur ou égal à 20 000.

Donc, tout ce qui est supérieur à 20 000 sera donné ici.

D'accord, donc l'opération inverse, vous pouvez voir dans les mots de l'opération de filtre, les gars, nous allons continuer la série PI spark.

Et dans cette vidéo particulière, nous allons voir le group by et la fonction d'agrégation.

J'ai déjà créé quelque part autour de quatre tutoriels sur pi Spark, c'est essentiellement le cinquième tutoriel.

Et encore une fois, cela fait partie d'un data frame, pourquoi nous devrions réellement utiliser le group by et les fonctions d'agrégation pour faire un certain type de pré-traitement des données.

Donc, commençons pour cet ensemble de données particulier.

Pour ce problème particulier, j'ai créé un ensemble de données qui a trois caractéristiques, comme le nom, les départements et le salaire, et vous avez certains des données comme crash data science, salaire, n'est-ce pas, quelque chose comme ceci.

Donc, ici, en bref, si je veux comprendre cet ensemble de données particulier, il y a certains départements probablement où crash et d'autres personnes enseignent.

Et en fonction de différents départements, ils obtiennent un salaire différent.

Donc, voyons comment nous pouvons effectuer différentes fonctions de group by et d'agrégation et voir comment nous pouvons pré-traiter ou comment nous pouvons obtenir ou récupérer un certain type de résultats à partir de ces données particulières.

Donc, pour commencer, ce que nous allons faire, nous allons d'abord importer pi Spark SQL import spark session.

Comme d'habitude, nous devons créer une session spark.

Donc, après cela, ce que nous devons faire, je vais créer une variable spark.

Donc, je vais utiliser spark session dot builder dot happening.

Je pense que tout le monde doit être familier avec cela.

Mais encore une fois, j'essaie de vous montrer cela, donc laissez-moi l'écrire comme aggregate dot get auto create.

Donc, maintenant, j'ai effectivement créé une session spark.

D'accord, probablement cela prendra un certain temps.

Maintenant, si je vais et vérifie ma variable spark, voici toutes vos informations, d'accord, concernant cette vidéo spark particulière, maintenant, allons-y et essayons de lire l'ensemble de données.

Maintenant, je vais simplement écrire df underscore pi Spark.

Et puis ici, je vais écrire spark dot read dot CSV.

Le nom du fichier CSV est essentiellement test trois dot CSV, et rappelez-vous, je vais donner ce fichier CSV particulier dans le GitHub aussi.

Et puis je vais utiliser header est égal à true, virgule, infer schema est égal à deux.

Maintenant, c'est mon df underscore pi Spark.

Maintenant, ce que je vais faire dans l'instruction suivante, je vais écrire df underscore pi Spark.

point show, n'est-ce pas.

Maintenant, ici, vous serez en mesure de voir que je suis effectivement en mesure de voir tous les ensembles de données.

Ici, j'ai nommé les départements et le salaire, toutes ces informations particulières.

Si je veux vraiment voir le schéma ou les colonnes, comme toutes les colonnes où il appartient à ceci, comme un type de données, donc je peux définitivement utiliser le F underscore pi spark dot print schema, n'est-ce pas.

Et maintenant, ici, vous pouvez voir que le nom est une chaîne, le département est une chaîne, et le salaire est essentiellement un entier.

D'accord, maintenant, effectuons quelques opérations de group by, d'abord, nous allons commencer par l'opération de group by, probablement, je veux regrouper par nom, et probablement essayer de voir quelle sera la moyenne du salaire.

Vous savez, bien, qu'est-ce que supposons, prenons un exemple spécifique ici.

Donc, je vais écrire TF dot underscore pi spark dot group by, supposons que je veux aller et vérifier qui a le salaire maximum parmi toutes ces personnes qui sont présentes dans cet ensemble de données particulier.

Donc, je vais d'abord regrouper par nom, si je l'exécute, vous pouvez voir que nous allons obtenir un type de retour de données de groupe à un emplacement de mémoire spécifique.

Et vous devez toujours savoir que, les gars, les fonctions de group by et d'agrégation fonctionnent ensemble.

Cela signifie essentiellement que, tout d'abord, nous devons appliquer une fonctionnalité de group by et ensuite nous devons appliquer une fonction d'agrégation.

Donc, la fonction d'agrégation, voulez-vous vraiment vérifier, appuyez simplement sur le point et appuyez sur tab.

Donc, ici, vous serez en mesure de voir beaucoup de fonctions différentes, des exemples comme l'agrégation, la moyenne, le compte, le max, la moyenne, par mieux, beaucoup plus, n'est-ce pas ? Maintenant, ce que je vais faire, je vais simplement utiliser ce dot sum parce que j'ai vraiment besoin de trouver quel est le salaire maximum parmi toutes ces personnes particulières, qui a le salaire maximum.

Donc, ici, je vais dire Datsun et si je l'exécute, vous serez en mesure de voir que nous obtenons sequel dot data frame, qui a le nom et la somme du salaire, c'est très important, voyons la somme du salaire parce que j'ai vraiment besoin d'avoir la somme du salaire, rappelez-vous, nous ne pouvons pas appliquer la somme sur la chaîne.

Donc, c'est la raison pour laquelle cela n'a pas été fait ici, il vous donne simplement le nom parce que nous avons regroupé par nom et ce dot some sera simplement appliqué sur ce salaire particulier.

Maintenant, si je vais et écris dot show ici, vous serez en mesure de voir que la réponse sera ici, il a le salaire le plus élevé de 35 000, Sonny a 12 000, Krish a 19 000, Mahesh a 7 000, donc, si vous allez et voyez ici, donc, l'uncial est essentiellement présent ici et dans le big data.

Donc, dans l'ensemble, son salaire devrait être de 35 000 si vous le calculez, de même, vous pouvez aller et calculer mon salaire ici, ici en calculant simplement cela et puis vous pouvez aussi calculer le salaire de sunny.

Et vous pouvez aussi voir mon hash et ainsi de suite, c'est juste un exemple.

Donc, ici, je vais simplement écrire que nous avons regroupé pour trouver le salaire maximum.

Et définitivement ici, à partir de cette observation entière, nous pouvons récupérer que sudhanshu a le salaire le plus élevé.

D'accord, maintenant, passons à une étape suivante.

Une étape de plus.

Maintenant, nous allons essayer de regrouper par départements pour trouver quel département donne le salaire maximum, d'accord, nous allons faire un group by départements qui donne le maximum standard, supposons que c'est mon, c'est mon exigence, d'accord, et différents types d'exigences peuvent venir, je montre simplement quelques exemples.

Je vais simplement copier cela.

Je vais utiliser ce département, d'accord.

Et puis je vais essentiellement dire dot some dots show, si je l'exécute, laissez-moi voir, le département est un nom de colonne incorrect.

Donc, je vais écrire departments, c'est department.

Donc, laissez-moi écrire cela.

Maintenant, si je vais et vois IoT ici, cela donne un salaire d'environ 115 1000 aux employés les plus simples, n'est-ce pas, combiné parce que nous faisons le some big data donne quelque part autour de 15 000, la science des données donne autour de 43 000, je suppose, si je vais et vois big data ici, 4000 4000 8000 8013 1000 13 000 15 000, donc j'espère que je comprends, oui, Big Data nous donne effectivement 15 000, donc vous pouvez aller et le calculer.

Supposons que vous voulez trouver la moyenne, vous pouvez aussi trouver la moyenne, d'accord, donc laissez-moi simplement l'écrire ici.

Copiez simplement toute cette chose, collez-la ici et lisez-moi, au lieu de, au lieu de some, je vais essayer d'écrire mean, donc par défaut, le salaire moyen ici, vous pouvez voir que pour un employé particulier, quelque part pour IoT, il est de 7500 parce que cette moyenne sera basée sur le nombre de personnes travaillant dans le département, n'est-ce pas.

Donc, comme ceci, vous pouvez réellement trouver, je peux aussi vérifier une autre chose, je peux copier cela, je peux essayer de trouver combien de personnes sont réellement en train de travailler en fonction du département, donc je peux utiliser dot Count et puis si je vais et l'exécute correctement, c'est une méthode, d'accord.

Maintenant, ici, vous verrez que IoT, il y a deux personnes dans big data, il y a quatre personnes dans data science, ils sont quatre personnes.

Donc, quatre plus quatre plus huit, le nombre total d'employés présents ici est essentiellement maintenant, une autre façon que je peux appliquer directement une fonction d'agrégation.

Maintenant, voyez, ce sont tous quelques exemples et encore une fois, vous pouvez faire différentes fonctions de groupbuy, laissez-moi utiliser df pi spark, supposons que je dise dot aggregate, d'accord, et à l'intérieur de cela, je vais simplement donner mes paires clé-valeur comme ceci, supposons que je dise, laissez-moi dire que le salaire, je veux trouver la somme des salaires, la dépense totale à l'intérieur.

Donc, la dépense totale que vous serez en mesure de voir quelque part sur 73 000, d'accord.

Donc, nous pouvons aussi appliquer une fonction d'agrégation directe, sinon, toutes ces fonctions sont aussi des fonctions d'agrégation que nous appliquons après avoir appliqué une fonction de group by.

Maintenant, supposons que ce sont probablement les salaires que je veux trouver, supposons que je prends cet exemple, je veux trouver le salaire maximum que la personne obtient essentiellement, qui obtient le salaire maximum, désolé.

Donc, ici, au lieu d'écrire dot sum, maintenant je vais écrire max dot show.

Maintenant, ici, vous pouvez voir que Sudan shows obtient essentiellement 20 000 ici, 10 000 crashes obtient 10 000, matches obtient quatre pour 4000, n'est-ce pas.

Donc, toutes ces données particulières sont là, voyez, Krishna obtient essentiellement par rapport à la science des données ici, 10 000, donc il a essentiellement pris, il ne prend pas les deux enregistrements, mais au moins lorsqu'il regroupe par nom, et puis il montre ces données particulières, ce temps-là, vous serez en mesure de le voir, voyons si je serai aussi en mesure de voir cela ou non.

Donc, group by si je marque et écris min.

Donc, ici, vous serez en mesure de voir la valeur minimale par rapport à différents enregistrements lorsque je regroupe par ici, vous serez en mesure de voir que Sudan shoe, désolé.

Donc, la réponse obtient un salaire minimum de 5000, 2000, les crashs obtiennent un salaire minimum de 4000.

D'accord, nous pouvons aussi obtenir cette information particulière.

Maintenant, voyons quelles sont les différentes opérations, la moyenne est aussi là.

Donc, si j'écris AVG, c'est comme la moyenne seulement, les gars.

Donc, c'est essentiellement le salaire moyen que probablement, encore une fois, vous pouvez vérifier différentes fonctionnalités, pourquoi toutes ces choses sont essentiellement requises.

Comprenez une chose, c'est que vous devez vraiment faire beaucoup de pré-traitement des données, beaucoup de compétences de récupération que vous faites essentiellement, vous pouvez le vérifier, celui-ci et vous pouvez faire différentes fonctionnalités comme vous l'aimez, spark émuler a aussi une documentation incroyable concernant divers exemples.

Donc, ici, vous pouvez aller et cliquer sur exemples.

Et vérifier essentiellement cette documentation particulière, vous pouvez réellement voir différents types d'exemples comment cela est essentiellement fait.

Mais concernant spark ml, il y a deux techniques différentes.

L'une est les techniques RDD, et l'autre est les API de data frame.

Maintenant, ce que nous allons faire, les gars, l'API de data frame est la plus récente, vous savez, et elle est assez célèbre partout.

Donc, nous allons nous concentrer sur l'API de data frame.

C'est la raison pour laquelle nous apprenons très bien le DataFrame dans PI spark.

Donc, nous allons essayer d'apprendre à travers les API de data frame.

Et nous allons essayer de voir la technique comment nous pouvons résoudre un cas d'utilisation de machine learning.

Maintenant, allons-y et voyons un exemple très simple, les gars.

Et rappelez-vous toujours, la documentation est assez incroyablement donnée, vous pouvez réellement vérifier ici et essayer de lire toutes ces choses.

D'accord.

Donc, procédons.

Et essayons de voir quelles sont les choses que nous pouvons réellement faire.

Dans cet exemple particulier, je vais simplement prendre un problème simple de machine learning.

Donc, laissez-moi simplement ouvrir un ensemble de données spécifique pour vous tous, et puis probablement, nous allons essayer de le faire.

D'accord.

Donc, c'est mon ensemble de données.

Les gars.

Je sais qu'il n'y a pas beaucoup d'enregistrements ici.

D'accord, donc j'ai un ensemble de données, qui a comme nom, âge, expérience et salaire.

Et c'est juste un problème simple pour vous montrer à quel point SPARC est puissant, par rapport aux bibliothèques M lab, juste pour vous montrer une démo.

À partir de la vidéo suivante, je vais vous montrer une explication détaillée des algorithmes de régression, comment nous pouvons faire l'implémentation, tout théorique et tout, les gars ont déjà téléchargé, vous pouvez voir ici, je vais le faire, voir après ce tutoriel cinq, c'est essentiellement le tutoriel six, je vais essayer de l'ajouter après cela et quand je vais télécharger l'algorithme de régression linéaire avant cela, assurez-vous que vous regardez cette infusion de match.

D'accord, j'ai téléchargé cette vidéo spécifique aussi dans la même playlist.

Donc, après ce tutoriel 26 St.

yt disant tutoriel 26 parce que je l'ai aussi ajouté dans ma playlist de machine learning.

Donc, après cela, vous serez aussi en mesure de trouver quand nous allons discuter de la régression linéaire, comment nous pouvons implémenter en profondeur, cette vidéo sera aussi téléchargée.

Donc, procédons.

Et voici tout mon ensemble de données.

Les gars, c'est mon ensemble de données.

Maintenant, ce que je dois faire, c'est que sur la base de l'âge et de l'expérience, j'ai besoin de prédire le salaire, un cas d'utilisation très simple, pas beaucoup de pré-traitement des données, pas beaucoup de transformation, pas beaucoup de normalisation et tout ça, d'accord, je vais simplement prendre ces deux caractéristiques indépendantes.

Et je vais prédire le salaire de cette personne particulière sur la base de l'âge et de l'expérience.

D'accord, donc c'est ce que je vais faire.

Donc, voici un exemple parfait, encore une fois, en détail, je vais essayer de vous montrer comment implémenter ligne par ligne probablement à partir des vidéos à venir où je vais discuter de la régression linéaire, et si je vais voir ce problème particulier, c'est aussi un exemple de régression linéaire.

D'accord, donc allons-y.

Tout d'abord, comme d'habitude, je vais créer une session spark.

Donc, je vais utiliser from pi spark dot SQL import spark session.

Et puis je vais utiliser spark session dot builder dot app name.

Ici, je crée effectivement une session spark sur missing, laissez-moi l'exécuter, je pense que cela est assez familier, vous êtes familier avec cela, puis ce que je vais faire ici, c'est que nous allons simplement lire cet ensemble de données particulier avec test un dot CSV header est égal à true et infer schema est égal à true.

Donc, lorsque je vais et vois mon training dot show, ce sont toutes mes caractéristiques ici, parfait, je vais vous donner cet ensemble de données.

Ne vous inquiétez pas.

Maintenant, à partir de cet ensemble de données particulier, si je vais et vérifie mon print schema, donc ici, vous serez en mesure de voir que j'obtiens cette information particulière.

C'est tout mon print schema.

Ici, j'ai des caractéristiques comme nom, âge, expérience et salaire.

Maintenant, si je vais et vois train dot columns, c'est mon training dot columns.

Maintenant, rappelez-vous toujours, les gars, dans PI Spark, nous utilisons un fonds différent ou un mécanisme ou un type de pré-traitement des données avant de voir, habituellement ce que nous faisons, c'est que en utilisant des algorithmes de machine learning qui sont disponibles sur le net scalaire, nous faisons essentiellement un train test split, n'est-ce pas.

Et puis nous divisons d'abord cela en caractéristiques indépendantes, caractéristiques dépendantes, n'est-ce pas, que nous utilisons une variable X et Y, et puis nous faisons un train test split.

En faisant cela, dans PI Spark, nous faisons simplement quelques techniques différentes, ce que nous faisons, c'est que oui, nous devons essentiellement créer un moyen où je peux regrouper toutes mes caractéristiques indépendantes.

Donc, probablement, je vais essayer de créer vector assembler, nous l'appelons essentiellement vector assembler, voir où la classe que j'ai réellement utilisée, le vector assembler s'assurera que j'ai toutes mes caractéristiques ensemble regroupées comme ceci, regroupées comme ceci, sous la forme de l'âge et de l'expérience, supposons ici, mes deux caractéristiques principales sont l'âge et l'expérience, qui sont mes caractéristiques indépendantes, n'est-ce pas.

Donc, il sera regroupé comme ceci, pour chaque enregistrement, il sera regroupé comme ceci, d'accord, pour chaque rapport, il sera regroupé comme ceci, et puis ce que je vais faire, c'est que je vais traiter ce groupe comme une caractéristique différente.

Donc, ce sera essentiellement ma nouvelle caractéristique, n'est-ce pas.

Et rappelez-vous, cette nouvelle caractéristique est ma caractéristique indépendante.

Donc, ma caractéristique indépendante ressemblera à ceci dans un groupe de H, expérience, qui sera traitée comme une nouvelle caractéristique.

Et c'est exactement ma caractéristique indépendante.

Donc, je dois regrouper cette manière particulière.

Donc, afin de regrouper cela, ce que nous faisons, c'est que dans PI Spark, nous utilisons quelque chose appelé vector assembler.

Donc, dans ce vector assembler est essentiellement présent dans pi spark.ml dot feature, nous utilisons ce vector assembler, nous utilisons deux choses.

L'une est input column, quelles colonnes nous prenons essentiellement pour les regrouper.

Donc, deux colonnes, l'une est l'âge et l'expérience, n'est-ce pas, nous n'avons pas à prendre le nom parce que le nom est fixe, c'est une chaîne.

Oui, si des caractéristiques de catégorie sont là, ce que nous faisons, ce que nous devons faire, nous allons convertir cela en une certaine représentation numérique que je vais vous montrer lorsque je fais une implémentation en profondeur, les vidéos à venir de régression linéaire, régression logistique et tout.

Mais ici, vous serez en mesure de voir que je vais prendre les colonnes d'entrée, l'âge vient de l'expérience sous la forme d'une liste.

Et puis je vais essayer de regrouper cela et créer une nouvelle colonne, qui est appelée comme caractéristique indépendante ici, n'est-ce pas, c'est ce que je fais réellement.

Donc, si je vais et exécute ce vector assembler, donc ici, j'ai obtenu mon feature assembler, et puis je fais dot transform, je fais dot transform sur mes données d'entraînement.

Donc, c'est essentiellement mes données d'entraînement lorsque je fais cela, et lorsque je fais output dot show ici, vous serez en mesure de voir que j'avais toutes ces caractéristiques, et une nouvelle caractéristique a été créée, qui est appelée comme caractéristiques indépendantes.

D'accord, donc nous avons effectivement créé une caractéristique indépendante.

Et vous pouvez voir ici, âge, et expérience, âge et expérience, âge et expérience, donc c'est mes lignes groupées que j'ai effectivement obtenues, en bref, ce que j'ai fait, j'ai combiné ces deux colonnes et je les ai faites comme une seule caractéristique indépendante, d'accord ? Maintenant, ce sera ma caractéristique d'entrée.

D'accord.

Et ce sera ma caractéristique de sortie, et nous allons essayer d'entraîner le modèle.

D'accord, donc ici, maintenant, si je vais et vois output dot columns, j'ai le nom, l'âge, l'expérience, le salaire, les caractéristiques indépendantes.

Maintenant, ce que je vais faire, c'est que parmi tout cela, voyons quelles données je suis réellement intéressé.

Donc, parmi tout cela, je vais simplement être intéressé par ces deux données.

Séparer les caractéristiques indépendantes et le salaire, le salaire sera ma caractéristique de sortie, la variable y, n'est-ce pas, et ce sera ma caractéristique d'entrée.

Donc, ce que je vais faire, je vais simplement sélectionner output, ou je vais dire que c'est essentiellement mes données finalisées.

Et je vais simplement prendre deux colonnes, c'est output dot select.

Et à l'intérieur de cela, je vais simplement donner mes deux caractéristiques, que je vais dire, l'une est les caractéristiques indépendantes.

D'accord, indie band features, j'espère que le nom est correct.

Sinon, je vais simplement le confirmer une fois de plus.

Donc, laissez-moi cliquer dessus ici.

Caractéristiques indépendantes, et l'une est total underscore bill.

Parfait, virgule, total underscore bill.

D'accord.

Maintenant, si je vais simplement et exécute cela, maintenant je prends simplement deux caractéristiques, n'est-ce pas.

Maintenant, si je vais et trouve finalized data dot show, maintenant je serai en mesure de voir deux caractéristiques importantes, c'est les caractéristiques indépendantes et le total bill.

Rappelez-vous, ce sont toutes mes caractéristiques indépendantes.

Et c'est ma caractéristique dépendante.

C'est très simple jusqu'ici.

Si c'est fait, les gars, l'étape suivante est essentiellement que je vais simplement copier et coller un peu de code, je vais simplement appliquer la régression linéaire.

Donc, tout d'abord, de pi spark.ml dot regression, je vais importer la régression linéaire.

Et puis je vais prendre toutes ces données finalisées et faire un split aléatoire de 75 et 25%.

D'accord, et puis dans ma régression linéaire, je vais simplement fournir mes caractéristiques indépendantes comme ma colonne de caractéristiques.

Ce sont deux paramètres qui doivent être donnés dans la régression linéaire, l'un est la colonne de caractéristiques, ici je vais fournir les caractéristiques indépendantes.

Le second est essentiellement le total bill qui est ma caractéristique dépendante.

Et maintenant, je vais simplement faire un fit sur les données d'entraînement.

Donc, une fois que je le fais, mon modèle de régression va être créé.

Et probablement, cela prendra du temps.

Maintenant, ici, vous pouvez voir toutes les informations, des informations incroyables que vous obtenez concernant l'entraînement et le test.

D'accord, et rappelez-vous, les gars, quel que soit le groupe que vous avez fait, cette caractéristique indépendante, cela est au format UDT.

D'accord, vous pouvez voir la forme complète de UDP, ce n'est pas un gros problème, je pensais, d'accord, maintenant j'ai mon régressor.

Donc, ce que je vais faire, je vais simplement dire regressor dot coefficient, puisque c'est une régression linéaire multiple, donc je vais simplement utiliser regular, donc dot coefficient et ce sont tous mes paramètres, différents coefficients parce que j'ai environ six paramètres.

Rappelez-vous toujours, dans une régression linéaire, vous aurez un coefficient basé sur le nombre de caractéristiques.

Et vous aurez aussi une interception.

Donc, ici, je vais simplement intercepter.

D'accord, donc c'est essentiellement mon interception, qui est de 0,923.

D'accord, donc ici, vous avez les deux informations, maintenant c'est le moment où nous allons essayer d'évaluer, évaluer les données de test.

Donc, ici, je vais simplement dire test.

Et c'est essentiellement mes prédictions, n'est-ce pas ? Donc, ici, laissez-moi l'écrire comme quelque chose comme ceci.

Donc, prédictions, d'accord.

prediction.

Et ce que je vais faire, je vais simplement écrire pred underscore results.

Results est égal à celui-ci.

Et ce sera essentiellement mes résultats, d'accord ? Ou test n'est pas défini, pourquoi test n'est pas défini, parce qu'il devrait y avoir des données de test.

Je suis vraiment désolé, d'accord.

Mais ce n'est pas grave, vous serez en mesure d'obtenir de si petites erreurs, d'accord.

Maintenant, si je veux vraiment voir mes résultats de prédiction, il suffit d'aller et de voir red dot predictions, il y aura quelque chose comme predictions dot show, d'accord.

Si vous écrivez comme ceci, ici, vous serez en mesure d'obtenir toute la prédiction.

D'accord.

Donc, rappelez-vous, dans cette prédiction, c'est votre caractéristique indépendante, c'est votre total bill, c'est votre valeur réelle.

Et c'est une valeur de prédiction, valeur réelle, valeur de prédiction, valeur réelle et valeur de prédiction ici, vous pouvez réellement comparer à quel point c'est bon, vous savez, en regardant simplement votre total bill et la valeur de prédiction, assez bon, assez incroyable, vous êtes en mesure de voir les données, je vais simplement écrire ma comparaison finale.

D'accord, comparaison finale.

Parfait.

Je suis très bon à cela, vous pouvez le voir.

Maintenant, voyons quelques autres informations comme quelles informations nous pouvons vérifier.

À partir de cela, nous pouvons vérifier beaucoup de choses, probablement vous voulez vérifier le R carré.

Donc, ce que vous pouvez écrire, vous pouvez vérifier le coefficient d'interception, puis vous avez perdu, puis il y a aussi quelque chose appelé R carré.

Si je vais et exécute cela, c'est essentiellement mon R carré.

Ou laissez-moi simplement l'écrire.

Je pense, predictions.

Je ne pense pas que le R carré soit où, laissez-moi voir si nous serons en mesure de voir la valeur R carré ou non.

Dans une seconde, je vérifie simplement la page de documentation.

D'accord, oh, désolé, je n'ai pas à utiliser regressor ici.

Donc, ici, je vais utiliser prediction dot results.

Et laissez-moi calculer le R carré.

Donc, c'est mon R carré.

De même, vous pouvez aussi vérifier prediction results dot mean absolute error.

Donc, vous avez mean absolute error.

Vous avez aussi prediction underscore result dot mean, squared.

Donc, toutes ces trois valeurs, vous pouvez définitivement les vérifier.

Donc, voici votre mean absolute error, voici votre mean squared error.

Donc, ce sont mes métriques de performance que je peux définitivement avoir.

Et chaque fois que vous, les gars, chaque fois que vous rencontrez un problème, assurez-vous de vérifier la documentation dans la documentation Apache Spark em lib.

Maintenant, de cette manière, vous pouvez définitivement faire cette déclaration de problème entière.

Maintenant, je vais vous donner une mission, essayez simplement de la rechercher sur Google et essayez de voir comment vous pouvez enregistrer ce fichier particulier probablement dans un format pickle ou probablement dans un fichier modèle pickle temporaire.

Vous savez, c'est très, très simple, vous devez simplement utiliser la sauvegarde du régressor, mais essayez de jeter un coup d'œil et essayez de voir comment vous pouvez enregistrer ce fichier pickle particulier.

Maintenant, c'était tout à propos de cette vidéo particulière.

J'espère que vous aimez cela maintenant, essayez simplement de résoudre un autre problème.

Essayez de faire cela.

Dans les vidéos à venir.

Je vais aussi essayer de montrer comment vous pouvez faire un encodage one hot et probablement serez en mesure d'apprendre cela aussi.

Donc, j'espère que vous avez aimé cette vidéo particulière.

Veuillez vous abonner à la chaîne si vous n'êtes pas abonné, assurez-vous de passer une excellente journée.

Merci. Au revoir.