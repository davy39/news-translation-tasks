---
title: Apprendre à utiliser la base de données MySQL
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-20T13:18:33.000Z'
originalURL: https://freecodecamp.org/news/learn-to-use-the-mysql-database
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/mysql.png
tags:
- name: MySQL
  slug: mysql
- name: youtube
  slug: youtube
seo_title: Apprendre à utiliser la base de données MySQL
seo_desc: 'MySql is one of the most popular databases.

  We just published a MySQL Database course on the freeCodeCamp.org YouTube channel.

  Bharath Ram Manoharan from Execute on Command created this course. He is a senior
  database engineer and great teacher.

  This...'
---

MySQL est l'une des bases de données les plus populaires.

Nous venons de publier un cours sur la base de données MySQL sur la chaîne YouTube freeCodeCamp.org.

Bharath Ram Manoharan de Execute on Command a créé ce cours. Il est ingénieur principal en bases de données et un excellent enseignant.

Ce cours commence par les bases de SQL. Ensuite, il aborde également des concepts clés de bases de données tels que la modélisation des données, les verrous, les index, SQL Explain, et plus encore.

Voici les sujets abordés dans ce cours :

* Comment créer une instance AWS EC2
* Comment installer la base de données MySQL
* Modélisation des données
* Bases de SQL - Création d'une table
* Bases de SQL - Insertion de données
* Bases de SQL - Mise à jour et suppression de données
* Bases de SQL - Lecture de données (instructions Select)
* Jointures SQL
* Niveaux d'isolation des transactions
* Verrous au niveau de la table
* Verrous au niveau des lignes
* Interblocages de la base de données
* Index clusterisés
* SQL Explain

Regardez le cours complet ci-dessous ou sur la chaîne YouTube freeCodeCamp.org (2 heures de visionnage).

%[https://www.youtube.com/watch?v=ER8oKX5myE0]

## Transcription

(autogénérée)

MySQL est l'une des bases de données les plus populaires, apprenez à l'utiliser dans ce cours dispensé par un ingénieur principal en bases de données.

Bienvenue dans ce cours de base sur MySQL. Je veux commencer par vous remercier d'essayer d'apprendre une nouvelle compétence.

Permettez-moi de me présenter.

Je m'appelle Barbara et je travaille pour Salesforce en tant qu'ingénieur principal en bases de données. J'ai plus de 12 ans d'expérience avec diverses bases de données, Oracle étant la principale. J'ai travaillé avec des entreprises comme Chase, PayPal, Wells, Fargo, StubHub, etc.

Permettez-moi de répondre à quelques questions de base pour vous d'abord, à savoir qui, quoi et pourquoi.

Alors, qui devrait suivre ce cours ? Ce cours est destiné aux professionnels des bases de données qui souhaitent élargir leurs compétences.

Si vous êtes ingénieur logiciel ou développeur full stack et que vous souhaitez acquérir une compréhension approfondie de la base de données MySQL, ce cours est fait pour vous.

Et si vous êtes étudiant en informatique, ou un jeune diplômé, ce cours vous donnera quelques connaissances sur les bases de données internes.

Alors, pourquoi devriez-vous apprendre MySQL ? MySQL est la base de données open source la plus populaire et, bien sûr, Postgres.

SQL est définitivement en haut de la liste.

Alors que les entreprises déplacent leurs données de l'interne vers le cloud, elles préfèrent généralement migrer vers une base de données native cloud ou une base de données open source comme MySQL ou Postgres sequel, afin d'économiser des coûts.

Donc, disons que vous êtes un expert de la base de données Oracle.

Si vous acquérez des connaissances sur une base de données comme MySQL, alors vous pourriez aider les entreprises à migrer leurs données d'Oracle vers MySQL, et cela peut être vraiment précieux.

Maintenant, voyons ce qui est couvert dans ce cours.

Tout d'abord, par MySQL, j'entends le moteur de stockage MySQL InnoDB tout au long de ce cours, qui est utilisé derrière tout site web de commerce, ou une banque ou une institution financière, et ainsi de suite.

Et MySQL offre une variété de moteurs de stockage, mon I Sam, moteur de stockage en mémoire, ou certains moteurs de stockage populaires, qui sont disponibles, nous allons apprendre sur MySQL InnoDB, je ne couvre aucun autre type de moteurs de stockage.

Maintenant, ce sont les sujets que je vais couvrir dans ce cours.

Et veuillez noter que ceci est un cours d'administration de base de données.

Donc, c'est 80% d'administration de base de données.

Et pour les personnes qui sont complètement nouvelles dans les bases de données, j'ai inclus les bases de SQL.

Donc, vous apprendrez sur l'installation de la base de données, MySQL Workbench, les index de base de données, les journaux de base de données, vous apprendrez également un peu d'optimisation des performances, c'est-à-dire SQL explain.

Donc, ce sont quelques sujets intéressants que je vais couvrir.

Donc, qu'avez-vous exactement besoin pour commencer avec ce cours, vous avez besoin d'un PC ou d'un Mac.

Donc, si vous utilisez un PC, alors je vous recommande de regarder les feuilles de travail ou le matériel supplémentaire qui est joint dans la description.

Si vous avez un ordinateur portable Mac, alors vous êtes dans la meilleure position pour apprendre ce cours.

Parce que vous pouvez voir ce que je tape.

Et vous pouvez taper les mêmes commandes et suivre de bout en bout.

Et surtout, c'est l'exigence principale, je veux que vous créiez un compte AWS, c'est correct et amaze sur les services Web.

Donc, si vous ne savez pas de quoi je parle, veuillez consulter ma feuille de travail qui peut être trouvée dans la description, j'ai joint quelques ressources, qui vous montreront comment créer un compte AWS, je vais utiliser une instance AWS EC deux tout au long du cours.

Et je vous montrerai comment en créer une.

Mais une chose principale que je veux que vous reteniez est qu'après chaque session d'étude, vous pouvez éteindre votre instance EC deux.

De cette façon, vous n'avez pas à payer de coûts inutiles.

Et veuillez vous souvenir que vous n'avez pas à garder votre instance EC deux en marche 24 heures sur 24.

Donc, une fois que vous avez créé un compte AWS et que vous vous êtes connecté, vous atterrirez sur ce tableau de bord ou cette page.

Et vous pouvez aller dans le menu des services ici.

Et sous calcul, vous pouvez choisir facile à faire ici sur le côté gauche, vous pouvez choisir des instances.

Et ici, nous allons créer une instance qui sera notre environnement de laboratoire.

Donc, cliquez sur lancer l'instance.

Et choisissons une image pour notre instance.

Donc, je vais choisir Red Hat Enterprise Linux version 864 bits et mon type d'instance sera T deux micro qui est éligible pour la couche gratuite.

Et vous devez choisir un sous-réseau approprié.

Si vous venez de créer un compte AWS, vous pouvez simplement laisser.

Laissez-le tel quel, le sous-réseau par défaut qui s'affiche pour vous.

Pour moi, je vais choisir un sous-réseau spécifique.

Et assurez-vous d'activer cette option d'attribution automatique d'IP publique.

Parce que cela attribuera une IP publique à votre instance que vous pourrez utiliser pour vous connecter en SSH à votre instance depuis votre ordinateur portable, et laissez tous les autres paramètres tels quels.

Et allons allouer environ 25 gigas pour la base de données ou pour toute l'instance.

Et vous pouvez simplement laisser le reste ISIS, allez à la page suivante, lisez, vous pouvez créer une étiquette pour votre instance.

Donc, je vais l'appeler mon instance SQL.

Un, allez à la page du groupe de sécurité.

Et ici, ce qui est important, c'est que vous devez pouvoir vous connecter en SSH à l'instance.

Et vous devez créer des règles de pare-feu appropriées pour cela, n'importe qui, en fait, n'importe qui dans le monde peut se connecter à cette instance via le port 22.

Et ce n'est pas sécurisé du tout.

Et je vais m'occuper de cette instance.

Parce qu'une fois que j'ai fini l'enregistrement, je la supprime généralement.

Donc, je sais comment gérer cela.

Mais lorsque vous créez des règles, assurez-vous de mettre l'IP de votre ordinateur portable, juste pour qu'il soit plus sécurisé, vous pouvez maintenant passer en revue votre configuration et cliquer sur lancer.

Mais si vous le souhaitez, vous pouvez créer une nouvelle paire de clés et lui donner un nom.

Et la télécharger avant de créer l'instance.

Pour moi, je vais simplement choisir une paire de clés existante.

Peut-être celle-ci, et je dis connaissance, peut-être une différente.

D'accord, celle-ci.

Et lancer l'instance.

Maintenant, votre instance est en cours de création, cela prendra probablement quelques minutes pour créer cette instance.

D'accord, c'est ainsi que vous créez une instance EC deux.

Et maintenant que mon instance est opérationnelle, et je peux voir l'IP publique.

Plus tard, j'installerai MySQL sur cette instance.

Donc, c'est ce que je voulais vous montrer dans cette leçon.

Donc, ce que vous voyez est essentiellement ma documentation MySQL montrant tous ces différents guides d'installation, comme Windows et Mac, et ainsi de suite.

Donc, nous sommes intéressés par l'installation Linux ou essentiellement l'installation MySQL sur Linux.

Et il y a en fait quelques guides.

Donc, celui-ci est essentiellement l'installation du binaire jannettek, nous allons sauter cela et aller ici.

Et même dans l'installation de MySQL, sur Linux, il y a un tas de guides.

Donc, la méthode recommandée d'installation est l'utilisation des packages RPM d'Oracle.

Mais nous allons utiliser cette installation basée sur le dépôt MySQL yum.

Et c'est en fait assez simple.

Donc, pour cette installation, nous devons aller sur MySQL comm et téléchargements.

Et nous téléchargeons l'édition Community et allons au dépôt yum.

Comme vous le savez, l'instance que nous avons créée a Archie l huit, Red Hat, Enterprise Linux huit qui fonctionne dessus.

Et donc nous devons télécharger ce rpm.

Mais ensuite, nous devons télécharger le RPM sur l'instance elle-même, celle que nous avons créée.

Donc, connectons-nous réellement à l'instance.

Donc, je vais utiliser SSH, et nous allons utiliser ma clé privée.

Et la connexion est facile, choisissez l'utilisateur par défaut et obtenez essentiellement l'IP publique de mon instance de connexion et nous passons à root d'accord.

Donc, une chose dont nous avons besoin pour télécharger ce RPM sur cette instance Linux est le paquet W get.

Donc, allons-y et installons cela d'abord.

D'accord, maintenant que w gate est installé, nous devons télécharger le RPM que nous venons de voir.

Donc, pour obtenir le lien de ce RPM, nous devons aller dans ce téléchargement.

Et nous devons cliquer avec le bouton droit ici et copier le lien.

Et si vous installez sur un OSS différent, vous devez cliquer sur le bouton approprié.

D'accord, donc nous avons le lien, et allons simplement coller ce lien ici, comme w get et le lien.

Et cette commande télécharge ce package, maintenant nous allons utiliser une commande RPM pour installer ce package.

Donc, ce package, comme je l'ai mentionné auparavant, va ajouter ce dépôt MySQL yum à votre liste de dépôts locaux.

Avec l'installation de Red Hat Enterprise Linux, vous obtenez comme un module MySQL par défaut.

Donc, désactivons celui-ci.

Si vous ne le désactivez pas, alors cela interférera avec notre installation MySQL.

Donc, allons-y et désactivons-le en utilisant cette commande.

Et ne vous inquiétez pas pour écrire ces commandes, je mettrai un lien vers mon dépôt Git avec tous ces commentaires dans la description.

Donc, tous ceux-ci ont été désactivés.

Maintenant, allons-y et installons l'édition serveur communautaire MySQL en utilisant yum install MySQL community server.

Et mettons moins y pour accepter toutes les invites.

Et cela installe tous ces packages.

D'accord, donc MySQL a été installé.

Allons-y et démarrons la base de données MySQL en utilisant system CTL.

Commande.

Et vérifions le statut.

Donc maintenant, la base de données MySQL est opérationnelle.

D'accord, donc le fichier journal de ce logiciel de base de données MySQL est sous var log.

Et si vous grippez temp à partir de ce fichier journal, vous obtiendrez le mot de passe temporaire pour l'utilisateur root.

Et vous pouvez utiliser cela pour vous connecter à la base de données MySQL.

Et comment vous connectez-vous, vous utilisez cette commande my sequel moins u, qui sera root et moins P est pour la connexion basée sur le mot de passe.

Et ensuite nous nous connectons à la base de données MySQL.

Donc, utilisons ce mot de passe et voyons si cela se connecte.

Et nous sommes connectés.

Et si vous exécutez une commande à ce stade, my sequel va vous demander de réinitialiser le mot de passe en utilisant l'instruction alter user.

Nous pouvons faire cela d'une autre manière.

Donc, il y a un exécutable appelé MySQL admin.

Et voici la commande pour cela.

MySQL admin, moins vous le nom d'utilisateur et moins p mot de passe.

Nous allons réinitialiser le mot de passe de l'utilisateur root.

Et fournissons le mot de passe actuel qui est ce mot de passe temporaire d'abord.

Et fournissons le nouveau mot de passe No.

D'accord, le mot de passe a été accepté.

Maintenant, essayons de nous connecter avec ce nouveau mot de passe en utilisant la commande précédente my SQL moins u prouvé et moins p MySQL.

Je vais mettre le mot de passe que j'ai dit il y a un instant, nous sommes connectés.

Donc, allons-y et exécutons une simple commande show databases qui montre toutes les bases de données par défaut qui font partie de l'installation.

Donc, une chose de plus que nous devons faire pour compléter l'installation est de charger un fichier de fuseau horaire ou une table de fuseau horaire comme montré ici.

Donc, si je fais un select star, qui est essentiellement une requête SQL pour lire à partir de cette table, vous pouvez voir que la table est vide pour l'instant.

Donc, sortons et exécutons une autre commande.

Pour charger les données liées au fuseau horaire.

Donc, voici la commande.

Et allons-y et exécutons-la.

Et je vais mettre mon mot de passe, et cela charge un tas de données, vous pouvez ignorer tous ces avertissements.

Retour à notre base de données MySQL.

Donc, si vous faites un select star, à partir de MySQL dot timezone, encore une fois, il montre un tas de données.

Donc maintenant, vous êtes bon.

Et cela complète l'installation de la base de données MySQL.

D'accord, les amis, dans cette section, nous allons parler de la modélisation des données.

D'accord, donc la conception de la base de données, la modélisation des données, la conception du schéma, ce sont tous des termes interchangeables pour la conception de la base de données est un processus continu.

Donc, vous arrivez avec une conception de base, lorsque vous créez votre application.

Et ensuite, à mesure que l'application, vous savez, ajoute de nouvelles fonctionnalités, améliorations, améliorations, vous itérez essentiellement sur cette conception, n'est-ce pas, vous continuez à ajouter de nouvelles choses à votre conception, et ainsi de suite.

Donc, la première chose que vous faites lorsque vous faites de la conception de base de données ou de la modélisation des données est de comprendre les données commerciales.

Et ensuite, une fois que vous comprenez les données commerciales, vous devez arriver avec une conception logique de votre base de données.

Que veux-je dire par là ? Eh bien, essentiellement, vous devez concevoir vos tables, les colonnes qui vont dans ces tables, les index, les contraintes, comme la contrainte de clé primaire, la contrainte de clé unique, les contraintes non nulles, les valeurs par défaut, les clés étrangères, ce sont toutes les différentes choses que vous devez créer.

Lorsque vous arrivez avec une conception logique de votre schéma, une fois que vous avez cette conception de table de base ou de schéma de base, alors vous pouvez chercher la redondance des données, c'est-à-dire que vous voyez où vos données sont répétitives.

Et ensuite, vous commencez à l'éliminer en normalisant vos tables.

Et c'est parce que la redondance des données cause des anomalies de données.

Ce que je veux dire par là, c'est que lorsque vous avez plusieurs occurrences des mêmes données, lorsque vous mettez à jour certaines données, vous devez les mettre à jour à plusieurs endroits.

Et si vous oubliez de mettre à jour même un seul endroit, maintenant vous avez deux versions des mêmes données dans votre base de données.

Et cela crée des anomalies de données, l'incohérence des données est similaire.

Et tout cela arrive à cause de la redondance des données.

Donc, ce que nous regardons est essentiellement une feuille de calcul et la feuille de calcul est essentiellement une grande table, une grande table, n'est-ce pas ? Et ce que nous allons faire est essentiellement concevoir une table pour un site web de commerce électronique, un site web de commerce électronique est essentiellement comme une zone amazone, ou E Bay, ou autre, comme une entreprise en ligne, comme un site web de commerce électronique en ligne, comme Alibaba, ou autre, n'est-ce pas ? Disons que vous n'avez qu'une seule table dans cette base de données, n'est-ce pas ? Et vous commencez, à mesure que les commandes arrivent, à travers ce site web, vous commencez à mettre des données dans cette table, n'est-ce pas ? Vous avez, vous savez, regardons quelques-unes des choses que vous enregistrerez dans cette table, n'est-ce pas, vous avez évidemment besoin d'un compte de vos commandes.

Donc, vous pourriez aimer numéroter vos commandes, et ensuite comment cela arrive, comme, vous savez, est-ce un bureau ou un mobile ? Ou quel produit est-ce ? Comme, vous savez, ici j'ai quelques livres, les titres des livres, et ensuite le prix des produits.

Et ensuite qui est le client, les détails des clients, les détails de paiement, les détails de livraison, et ainsi de suite.

Donc, tout cela fait partie du commerce électronique, essentiellement.

N'est-ce pas ? Et vous avez une table géante.

Et si vous regardez les données ici, n'est-ce pas ? Donc, vous savez, ici, j'ai quelques clients qui achètent, vous savez, deux produits différents, n'est-ce pas.

Donc, et vous pouvez voir que les données ont été répétitives.

Ce que je veux dire par là, c'est que chaque fois que j'achète le même produit, je dois répéter ces données, comme la première commande qui est arrivée était via le site web de bureau qui a été acheté par birth et ensuite vous pouvez voir tous les détails de ce client et tous ces détails sur le produit et le paiement, les détails de paiement également.

Ensuite, la deuxième commande qui est arrivée était d'une personne différente, mais c'était, vous savez, la commande était pour le même produit et vous avez dû répéter les informations sur le produit.

D'accord.

La troisième était du client précédent.

Mais cette fois, il a acheté un produit différent, ses informations, les informations du client ont été répétées.

Donc, il y a beaucoup de redondance de données, les données ont été répétitives.

Donc, c'est essentiellement une base de données non normalisée, où vous n'avez qu'une seule table ou une poignée de tables, nous avons toutes les informations de votre site web, ou de votre entreprise dans ces quelques tables.

En fait, c'est une version non normalisée de votre base de données, allons voir ce que vous pourriez faire d'autre.

Donc, ce que vous pouvez faire, c'est essentiellement, vous pouvez commencer avec cette table de base non normalisée, et ensuite vous pouvez commencer à enlever toutes les informations redondantes de votre base de données ou de votre table, la première chose que j'ai faite, c'est que j'ai enlevé les informations sur les clients, je les ai mises dans une table séparée, n'est-ce pas.

Et j'ai seulement les détails des clients ici.

Et j'ai commencé à mettre un numéro d'identification pour chaque identifiant client ou numéro de client, peu importe comment vous l'appelez.

Une fois que j'ai enlevé les informations sur les clients, j'ai la table des commandes, la table initiale, je l'appelle la table des commandes qui ressemble à ceci maintenant, n'est-ce pas ? Et vous pouvez voir que j'ai une colonne d'identifiant client ici.

Et qu'est-ce que cette colonne d'identifiant client ? Vos suppositions ? Exact. Donc, cette colonne d'identifiant client est la même que ce que vous voyez ici.

Exact ? Donc, pourquoi l'ai-je ? Parce que j'ai besoin d'un moyen de relier ces lignes.

Comme vous pouvez le dire, vous savez, ce sont des colonnes, ce sont des lignes, ces lignes, j'ai besoin de pouvoir les relier à un client, n'est-ce pas ? Si j'enlève les informations sur les clients, alors comment puis-je les relier ? Vous savez, cette table et cette table ? C'est par une colonne commune, ou un ensemble de colonnes.

En fait, dans ce cas, c'est juste une colonne.

Donc, l'identifiant client, n'est-ce pas ? Je mets simplement le numéro d'identification ici.

Et qu'est-ce que nous pouvons encore enlever de cette table.

Donc, c'est un niveau de normalisation.

N'est-ce pas ? Donc, continuons à normaliser, ce qui signifie enlever les détails des produits.

N'est-ce pas ? Donc, les détails des produits se répètent également.

Ici, vous ne ressentez pas autant de douleur, car il n'y a que trois enregistrements dans cette table.

Et si la table a un million d'enregistrements, n'est-ce pas ? C'est pourquoi nous devons normaliser la table.

Maintenant, vous prenez réellement les informations sur les produits et les déplacez vers une table différente.

Et ensuite, j'ai une colonne d'identifiant de produit juste pour numéroter, comme identifier les produits, et votre table des commandes ressemblera à ceci, puis vous prenez les informations de paiement vers une table différente.

Et votre table des commandes ressemblera alors à ceci.

C'est essentiellement le processus de passage d'un schéma ou d'une base de données non normalisée à une base de données normalisée.

Lorsque vous avez vos données dans une seule table, vous n'avez pas besoin de faire de jointures.

Donc, vous pourriez demander, en fait, qu'est-ce que les jointures, en fait, lorsque vous exécutez des requêtes, comme en utilisant SQL, SQL est un langage, n'est-ce pas ? Un langage de requête structuré, lorsque vous exécutez des commandes dans votre base de données, vous pouvez obtenir toutes vos données de cette seule table si votre base de données de table est totalement non normalisée.

Alors que si vous avez plusieurs tables, vous devez combiner ou joindre les tables et ensuite vous devez obtenir les données.

Donc, cela s'appelle joindre les tables.

Donc, lorsque vous avez une base de données non normalisée, vous n'avez pas à faire beaucoup de jointures.

Et c'est plutôt bien d'une certaine manière parce que votre base de données n'a pas à réfléchir autant pour obtenir les données.

Vous dites que je veux ces données et ces données sont disponibles dans cette table.

Donc, c'est très simple.

Alors que dans une base de données normalisée, lorsque vous joignez plusieurs tables, alors votre moteur de base de données, qu'ils appellent optimiseur dans Oracle ou dans la plupart des bases de données.

Donc, ce moteur de base de données doit réfléchir davantage, comme, d'accord, quelle table dois-je scanner en premier ? Et comment dois-je filtrer les données dans cette table.

Et ensuite, d'accord, je prends l'ensemble de résultats de cette table et je dois le joindre avec ces autres tables.

Donc, il y a tellement plus de réflexion, il y a tellement plus de traitement qui doit se produire sur le serveur où cette base de données est en cours d'exécution.

D'accord.

Et à cause de cela, la performance sera plutôt flexible.

Plus faible, et elle consommera beaucoup de ressources et vous avez tout cela qui se produit à grande échelle, comme de nombreuses opérations se produisent en même temps, alors vous avez essentiellement une performance lente, ou au moins inférieure à ce qu'elle aurait été dans une base de données non normalisée, mais en même temps, nous supprimons tellement de répétition de données ou la redondance des données est très faible, à cause de cela, le stockage nécessaire dans une base de données normalisée est beaucoup plus faible.

Donc, vous ne pouvez pas vraiment généraliser et dire qu'une base de données normalisée sera toujours lente ou qu'une base de données non normalisée sera rapide, tout dépend en fait, vous devez examiner les données et voir combien de répétitions se produisent, etc., etc.

Donc, mais généralement, c'est ainsi que cela se passe, à mesure que vous passez par ce processus de conception, vous savez, voyez ce que nous avons fait en fait, n'est-ce pas.

Donc, nous avons décidé des tables dont nous avons besoin, comme vous le savez, nous avons des commandes, une table de produits, des clients et des paiements, et nous décidons des noms de colonnes.

Et pas seulement cela, pour chaque table, vous devez décider en fait ce qui sera la clé primaire.

Ce que je veux dire par là, c'est qu'une clé primaire est une clé unique et qui ne peut pas être nulle, en fait, ce qui est très important.

Donc, en utilisant cette clé primaire, vous devriez être capable d'identifier n'importe quel enregistrement dans cette table, n'importe quelle ligne dans cette table.

Par exemple, si je dis ici, la clé primaire est le numéro de commande, alors je peux, à tout moment si j'ai un numéro de commande, alors je peux rechercher cette table, disons numéro de commande égal à deux, je peux simplement obtenir cet enregistrement de ma base de données.

Et ensuite, vous devez également avoir des clés uniques, n'est-ce pas.

Donc, les clés uniques sont presque comme les clés primaires.

Et une clé unique peut être maintenant une clé primaire ne peut pas être nulle, comme je l'ai mentionné.

Et ensuite, vous pouvez également avoir des index sur votre table.

Donc, les index sont des moyens de sélectionner vos données plus rapidement.

Disons que je recherche souvent cette table en fonction de l'email d'un client, alors j'ai besoin d'un index sur la colonne email du client, n'est-ce pas, vous devez décider cela.

Et vous devez décider quelles colonnes peuvent être nulles.

N'est-ce pas ? Ici, aucune des colonnes ne peut être nulle.

Disons que vous avez une autre colonne appelée préférence, la préférence du client en termes de type d'expédition ou de type de numéro de téléphone préféré, ou quelque chose comme ça.

Donc, cela peut être une colonne nulle, n'est-ce pas ? Donc, vous pouvez avoir des colonnes nulles.

Sinon, vous définissez vos colonnes comme non nulles.

Disons que dans votre table des commandes, vous avez cette colonne livrée, lorsqu'une commande est essentiellement créée lorsqu'un client achète un produit sur votre site web.

Bien sûr, il n'est pas livré immédiatement, au moment de la création de la commande, la colonne livrée aura toujours non ou n, une valeur n, n'est-ce pas ? Toutes ces choses, toutes ces décisions que nous prenons dont nous parlons font partie de la conception du schéma.

Et une fois que vous avez tout cela, vous pouvez mettre les informations dans votre outil de conception Entity Relationship.

Et dans la section suivante, je vous montrerai comment je fais cela sur sequel workbench, mon sequel world workbench, en fait, vous pouvez avoir une représentation picturale de votre conception logique de votre base de données, n'est-ce pas.

Et c'est essentiellement ce que vous appelez un diagramme ER.

Et bien sûr, vous pouvez parler de la relation entre les deux tables, disons que vous pouvez dire oh, cette table dans cette table, elles ont une relation un à plusieurs, par exemple, chaque client peut passer plusieurs commandes.

Donc, c'est en fait une relation un à plusieurs, n'est-ce pas.

Mais une commande peut être effectuée par un seul client.

N'est-ce pas ? Donc, ce genre de chose.

Donc, vous avez une relation un à un, une relation un à plusieurs, ou une relation plusieurs à plusieurs entre les tables.

En fait, tout cela fait partie de la modélisation des données.

Mais vous n'avez pas besoin de vous en soucier autant, tant que vous avez une idée claire des données qui entrent dans votre base de données.

Et en cours de route, vous devez définir le type de données de vos colonnes.

En fait, c'est très important.

Vos noms vont être un char générique.

Vous savez, les numéros de téléphone peuvent être des nombres, et l'email est à nouveau comme un char générique.

Et votre colonne d'identifiant ou les colonnes de numéro vont être int ou numéro.

Ce sont toutes des décisions que vous prendriez dans une tâche de modélisation de données, en fait, c'est à peu près ce que je veux dire sur la modélisation de données, puis il y a beaucoup plus dont nous pouvons parler.

Et comme l'atomicité, vous avez toutes les adresses, sorte d'attributs regroupés dans une colonne, nous devons les diviser également.

Donc, cela s'appelle l'atomicité.

Vous pouvez avoir l'adresse séparément, la ville séparément, l'état séparément, et le code postal séparément, n'est-ce pas.

Donc, ce genre de choses, il y a des nuances qui rendent votre base de données de plus en plus efficace.

Et, bien sûr, nous n'allons pas entrer dans beaucoup de détails là-dessus.

Mais c'est la modélisation de données de base que vous devez comprendre.

Et comme je l'ai dit avant, dans la section suivante, je vous montrerai comment prendre cela et ensuite l'entrer dans mon séquentiel workbench.

Récapitulatif rapide de ce que j'ai fait dans la dernière section, j'ai essentiellement créé une conception logique d'un site web de commerce électronique.

Donc, ce que vous regardez est une table que j'ai commencée.

C'est une table non normalisée, et nous avons essentiellement pris cette table non normalisée et nous l'avons normalisée.

Comme vous pouvez le voir, il y a quatre versions de cette table, j'appelle cette table la table des commandes.

Donc, il y a quatre versions différentes.

Et avec chaque itération, j'ai enlevé les données répétitives.

Donc, finalement, nous avons abouti à quatre tables, en plus de la table des commandes d'origine.

Donc, maintenant, nous avons aussi les clients, les produits et le paiement.

Dans cette vidéo, je vais prendre toutes les tables stables et ensuite je vais prendre la structure, et je vais créer une conception logique.

D'accord, allons directement dans MySQL Workbench et je suis déjà connecté à une base de données, ce que je vais faire, c'est aller dans Fichier et aller dans nouveaux modèles.

Donc, ici, nous pouvons ajouter un nouveau diagramme ER, un diagramme de relation d'entité.

Et appelons cette base de données eecom.

Magasin, quelque chose comme ça.

Donc, allons-y et commençons à créer nos tables.

Maintenant, je ne vais pas créer les quatre tables, cela prendrait probablement plus de temps ou longtemps, et je vais créer quelques tables.

Et cela devrait être suffisant pour que vous compreniez comment nous faisons cela.

Donc, commençons simplement par la table Clients.

Donc, la table client a cinq colonnes, voici l'icône pour créer une nouvelle table, vous pouvez glisser-déposer, ou vous pouvez essayer de dessiner maintenant double-cliquez et créez une table appelée client et ici nous pouvons commencer à mettre les noms de colonnes de la table, l'identifiant client, et ensuite cela va être peuplé par votre séquence.

Donc, la séquence est un objet de base de données.

Et ce sera un entier.

Donc, nous pouvons le laisser tel quel.

Et nous pouvons l'avoir comme clé primaire, c'est bien et une clé primaire doit être peuplée, elle ne peut pas être nulle.

Donc, cela est automatiquement sélectionné.

Le suivant est le nom du client, nous pourrions le diviser en prénom, et ensuite nous pouvons choisir un char et peut-être donner un peu plus de place comme la longueur du nom et ensuite le nom de famille, je peux choisir 100 et ensuite tous ceux-ci ne peuvent pas être nuls donc nous pouvons choisir la contrainte not null.

Donc, ce sont différentes contraintes qui sont disponibles.

Passons au suivant, l'adresse à nouveau.

Et si vous vous souvenez, j'ai parlé de l'atomicité.

Donc, vous voulez que vos colonnes soient atomiques, dans le sens où ici, essentiellement toute l'adresse est regroupée dans une colonne.

Bonne pratique de diviser cela en colonnes atomiques comme une adresse séparée, une ville séparée, un état séparé et ensuite un code postal séparé.

Donc, nous avons tout cela, bien sûr, aucun de ceux-ci ne peut être nul et qu'est-ce qu'il y a d'autre ? Donc, le numéro de téléphone du client, le numéro de téléphone sera tous des chiffres.

Mais alors, je veux en faire 10 chiffres, bien sûr pas nul et l'email du client.

Donc, je peux simplement dire email id 100 Ok, pas nul.

Donc, puisque l'Id est la clé primaire ici ou l'identifiant client, je veux m'assurer que nous avons une contrainte pour éviter la répétition des informations clients.

Par exemple, si vous avez les données d'un client pour l'Id un, je ne veux pas que les mêmes données du client se répètent pour un Id différent, par exemple, Id deux.

Donc, je vais en fait rendre l'email id unique pour chaque enregistrement ici.

Et peut-être aussi le numéro de téléphone.

Donc, ce sont toutes des contraintes de clé unique, ou des contraintes uniques.

C'est tout.

Donc, nous avons la table Clients créée.

Donc, revenons en arrière et voyons ce qu'il y a d'autre.

Donc, maintenant, je vais créer, disons, le produit.

Et ensuite, vous faites essentiellement la même chose, sélectionnez cela pour créer une nouvelle table.

Et ensuite, maintenant ici, vous pouvez simplement dessiner dans celle-ci, je vais l'appeler produit.

Et nous voulons passer par le même processus et ensuite mettre les noms de colonnes de produit là.

Si vous vous demandez, c'est la même colonne d'identifiant client que nous avons ajoutée ici.

Et nous allons en faire une clé étrangère dans une minute.

Donc, allons-y et divisons cela en plusieurs colonnes.

Parce que, encore une fois, tout est regroupé dans une colonne, ce qui n'est pas une bonne pratique.

Donc, disons, appelons cela le numéro de carte de crédit.

Si le client utilise PayPal, alors nous avons besoin de cet email.

Donc, nous pouvons utiliser l'identifiant email ici.

Donc, cela peut être nul ou non nul en fonction du type de paiement utilisé.

Donc, c'est bon, donc la date d'expiration sera une colonne de date.

Donc, changeons cela.

Donc, si vous n'êtes pas sûr, vous pouvez cliquer sur la liste déroulante et choisir le type de données approprié pour chacun.

L'autre chose que j'ai mentionnée, qui concerne essentiellement la clé étrangère, cet identifiant client est le même que celui que nous avons ajouté ici.

Donc, faisons de cet identifiant client une clé étrangère.

Donc, nous pouvons simplement l'appeler identifiant client clé étrangère un.

Et ensuite, la table qui sera référencée est les clients.

Et la colonne sera l'identifiant client.

Et c'est tout.

Donc, vous pouvez voir que maintenant nous avons une connexion ou une relation entre ces deux tables, je vais en fait ajouter la table des commandes également.

J'ai créé la table des commandes également, qui est la table principale et je vais maintenant créer quelques clés étrangères pour les commandes.

Tout est fait.

Si vous voulez créer des index à ce stade, vous pouvez le faire.

Donc, je pense que nous avons terminé.

Donc, nous avons essentiellement ajouté quatre tables à notre conception logique, ces quatre tables et ensuite nous avons créé des colonnes et défini leurs types de données.

Et nous avons également créé les clés étrangères et bien sûr la clé primaire et la clé unique pour chacune des tables.

Et vous pouvez voir la relation de clé étrangère clairement ici et cela, vous savez, c'est ce que vous feriez pour créer un modèle de données.

D'accord, donc maintenant, allons-y et créons un script SQL pour ce modèle de données.

Donc, vous allez dans la base de données, puis faites l'ingénierie directe.

Et ensuite, vous fournissez les détails de la base de données où vous voulez créer ces tables ou le schéma.

Donc, voici mes détails, continuez, allez au suivant, fournissez le mot de passe.

Maintenant, nous sommes connectés, j'ai dû essayer le mot de passe deux, trois fois.

Et cela a essentiellement créé un script SQL pour nous pour créer le schéma et les tables avec toutes les contraintes de clé primaire, clé unique et clé étrangère.

Donc, ce que nous pouvons faire, c'est simplement continuer et maintenant la base de données ou le schéma est créé alors qu'il parcourt et exécute ce script.

Et fermez.

Et maintenant, vous pouvez voir que les tables sont réellement créées.

Donc, vous pouvez même aller dans votre éditeur SQL, et ensuite vous pouvez commencer à lire, vous pouvez commencer à interroger vos tables.

Les voilà.

Donc, vous êtes revenu, bien sûr, il n'y a pas de données dedans.

Et vous pouvez maintenant commencer à utiliser votre base de données.

Donc, nous avons en fait créé avec succès le schéma de base, ou conçu le modèle de données pour ce site web de commerce électronique.

La création de table ou une commande CREATE TABLE commence par le mot-clé CREATE TABLE suivi du nom de la table et suivi de parenthèses.

Donc, à l'intérieur des parenthèses, cette paire de parenthèses, vous avez tous ces noms de colonnes, suivis des types de données des colonnes, et suivis des contraintes.

Et vous pouvez également utiliser ce mot-clé auto increment si vous voulez que la valeur de votre colonne soit incrémentée.

Automatiquement, à mesure que vous chargez des valeurs dans la table, et après la définition de la colonne, vous avez l'option de spécifier les clés comme les clés primaires, les clés uniques, les clés étrangères, et ainsi de suite, vous pouvez également spécifier le type de moteur de stockage dans le cadre de la création de votre table.

Et c'est une table très simple.

Vous pouvez également avoir des tables partitionnées ou des tables partitionnées qui ont des tables compressées, des tables chiffrées, et toutes ces choses nécessitent des mots-clés spéciaux à utiliser dans votre définition de table.

Et veuillez consulter la documentation MySQL.

Si vous voulez plus de détails sur la syntaxe.

Comme mentionné, j'utilise simplement des types de données entiers et des caractères, la documentation MySQL montre tous ces différents types de données comme numériques, date et heure, types de données de chaîne, comme ceux que j'utilise, et JSON spatial.

Donc, tous ceux-ci sont disponibles dans MySQL pour que vous les utilisiez.

Donc, allons-y et créons cette table.

Et avant de créer la table, je veux exécuter cette commande drop juste pour m'assurer que la table n'existe pas.

Et je vais créer cette table et voir si la table a été créée.

Oui, la table a été créée avec succès, je vais exécuter une commande select star à partir du nom de la table pour voir si je peux interroger avec succès cette table également.

Et ensuite, elle retourne.

Essentiellement, elle ne retourne rien, ce qui signifie qu'aucune donnée n'existe dans la table.

Et c'est ainsi que vous créez une table en utilisant la syntaxe CREATE TABLE.

Enfin, il y a en fait un mot-clé par défaut qui vous aide à spécifier des valeurs par défaut pour une certaine ou pour vos colonnes.

Donc, si vous ne spécifiez pas de valeur pour cette colonne de quantité dans vos instructions d'insertion, ou lorsque vous chargez des données via des procédures, le chargement de données via des procédures, il prendra automatiquement cette valeur par défaut.

C'est à peu près tout.

Et je vous verrai dans ma prochaine session MySQL SQL.

Donc, je viens de faire une description de la table que j'ai créée et elle a un identifiant de produit, un nom de produit, un type de produit, un prix et une quantité.

Et vous pouvez voir que l'identifiant de produit est également une colonne d'incrémentation automatique, pour l'instant, il n'y a pas de données dedans, une instruction d'insertion typique ressemble à ceci, allons à l'insertion dans le mot-clé et le nom de la table, un ensemble de colonnes entre parenthèses, celles que vous voulez remplir, suivi du mot-clé valeurs.

Et suivi des valeurs réelles des colonnes.

Si vous pouvez réaliser que je n'ai pas réellement spécifié la valeur de l'identifiant de produit parce que c'est une colonne d'incrémentation automatique.

Donc, allons-y et exécutons cette instruction d'insertion.

Donc, je vais également exécuter l'instruction select.

Comme vous pouvez le voir, la table des identifiants de produit a pris la valeur un, et cela s'est produit automatiquement, identifiez la valeur un, donc je vais continuer et valider la modification.

Et ensuite, passons à la deuxième variation.

Donc, cette fois, je vais spécifier une valeur pour l'identifiant de produit, rien d'autre n'est différent.

Donc, je veux juste vous montrer que c'est possible.

Donc, cela fonctionne et ensuite une validation.

Et ensuite, faisons un select pour nous assurer que la valeur a été insérée.

Donc, passons à cette troisième variation de cette instruction d'insertion.

Donc, ce sera à peu près la même chose, sauf que je vais sauter quelques valeurs et ensuite insérer la valeur 10.

Pour cette colonne d'identifiant de produit, je vais continuer et faire cela.

Cela fonctionne, un commentaire et une sélection à nouveau, puis vous pouvez voir que cela fonctionne également.

Donc, oui, cela a fonctionné.

Donc, vous pouvez en fait sauter quelques valeurs.

Regardons la prochaine variation.

Encore une fois, je vais insérer un enregistrement dans la table, sans spécifier explicitement l'identifiant du produit.

Ou explicitement, la colonne d'identifiant du produit est manquante ici, et je vais exécuter l'instruction d'insertion et valider.

Et ensuite, je vais exécuter l'instruction de sélection.

Je voulais juste vous montrer que là où se trouve la dernière valeur pour cette colonne d'incrémentation automatique, j'ai inséré la valeur 10 pour l'identifiant du produit la dernière fois, et ensuite la prochaine fois que je fais une insertion, l'incrémentation automatique se déclenche et augmente la valeur de 10 à 11, n'est-ce pas, reprend à partir de la valeur qui a été insérée la dernière fois.

Et je vais simplement prendre une autre instruction d'insertion, et cette fois, c'est en fait une insertion dans le nom de la table.

Et au lieu du mot-clé valeurs, en spécifiant les noms de colonnes, les valeurs, etc., nous sélectionnons en fait à partir d'une table différente.

Essentiellement, si la table produits trois correspond exactement à la structure de la table produits un, alors nous pouvons même faire une sélection étoile si les colonnes ne correspondent pas exactement, comme si les produits un ont un ensemble différent de colonnes, et les produits trois ont un ensemble différent de colonnes, alors nous devons nous assurer que nous sélectionnons réellement les colonnes.

Et par exemple, cet identifiant de produit à partir de produits trois correspond à cet identifiant de produit et produits un, et le nom de produit à partir de produits trois correspond à produit un, je suis désolé, le nom de produit et produit un, et ainsi de suite.

Allons-y et exécutons cela et voyons ce qui se passe.

Et cela fonctionne.

Et si je sélectionne maintenant la table produits un, vous pouvez voir que toutes ces lignes sont insérées correctement.

Et essentiellement, la table produits un est peuplée.

Et nous avons obtenu toutes les données de la table produits trois.

Cette fois, je veux vous montrer l'instruction d'insertion.

Encore une fois, c'est une sorte d'insertion en masse ou d'insertion multiple combinée en une seule instruction, vous pouvez voir que la clause insert into est spécifiée une seule fois, mais dans la clause values spark, nous avons en fait deux lignes spécifiées en même temps.

Donc, nous pouvons même utiliser une telle syntaxe et une validation, puis faire une sélection, tout est bon.

Donc, ce sont quelques variations de l'instruction insert.

J'espère que vous avez compris comment cela fonctionne.

Je vous verrai dans la prochaine session.

Hey, les apprenants de MySQL.

Donc, dans cette session, en fait, je vais parler des instructions de mise à jour et de suppression.

Donc, comme d'habitude, je vais utiliser mon schéma eecom store.

Et je vais utiliser ma table de produits pour faire cette démonstration.

Donc, rapidement, si nous sélectionnons la table des produits, il y a deux lignes pour l'instant.

Donc, la première mise à jour est juste pour vous montrer la syntaxe de la mise à jour.

Donc, vous avez le mot-clé de mise à jour suivi du nom de la table suivi du mot-clé set.

Et ensuite, vous pouvez avoir autant de colonnes que votre table contient, mais dans ce cas, j'ai seulement une colonne et je peux simplement exécuter cette mise à jour.

Donc, allons-y et ajoutons une clause de plus, qui est la clause where et cela est juste pour mettre à jour les lignes que vous voulez vraiment mettre à jour, donc nous allons mettre à jour uniquement les lignes avec l'identifiant de produit égal à un.

Donc, allons-y et faisons cela.

Et ensuite, je vais simplement faire un commit et faire un SELECT FROM products, la quantité est passée à 50, elle est passée de 299 à 349.

Maintenant, une autre chose à réaliser est que vous pouvez, vous savez, spécifier des valeurs littérales, lorsque vous mettez à jour, vous savez, cela arrive tout le temps.

Ou vous pouvez également spécifier une formule, ou vous pouvez avoir des fonctions SQL comme remplacer, sous-chaîne, longueur, et ainsi de suite, vous savez, vous pouvez consulter la documentation MySQL pour voir quels types de fonctions sont disponibles dans cette mise à jour, comme, je voulais juste vous montrer la syntaxe, essentiellement, pour vous faire savoir que vous pouvez avoir plusieurs, vous pouvez mettre à jour plusieurs lignes à la fois.

Dans ce cas, j'ai mis des valeurs un, deux, et trois, vous savez, vous n'avez pas à faire une ligne à la fois ou autre chose.

Donc, lorsque vous utilisez le mot-clé end, et vous pouvez dire l'identifiant du produit ou n'importe quel appel, et ensuite une série de valeurs à sélectionner les lignes que vous voulez.

Et il y a d'autres façons de le faire.

Mais le point étant, vous pouvez mettre à jour plusieurs enregistrements à la fois.

Et une autre utilisation intéressante est l'utilisation de l'instruction case, vous savez, vous pouvez dire que vous avez une série d'instructions de mise à jour, une pour l'identifiant du produit égal à un, une autre pour l'identifiant du produit égal à deux et une autre pour les autres valeurs d'identifiant du produit.

Et vous pouvez combiner tout cela en une seule instruction UPDATE en utilisant une clause ou un mot-clé case when then, dans ce cas, en fait, pour l'identifiant du produit égal à un, je veux incrémenter la quantité de 50.

Et l'identifiant du produit égal à deux, je veux incrémenter la quantité de 100, et ainsi de suite.

Donc, j'ai cette clause WHERE similaire ou similaire à celle que je vous ai montrée avant, je vais l'exécuter, vous pouvez voir que les colonnes sont incrémentées, je ne vais pas revenir en arrière et vérifier, je suis assez sûr que cela a fait la bonne chose.

Donc, le suivant est essentiellement lorsque vous voulez supprimer des enregistrements d'une table ou purger des données d'une table, alors vous pouvez simplement utiliser une simple instruction delete.

Et si vous voulez supprimer une ligne particulière, encore une fois, similaire à la mise à jour, vous pouvez utiliser une clause where pour en fait réduire les données que vous voulez supprimer, cette instruction particulière, qui est delete from un nom de table, et ensuite where le nom de la colonne est égal ou la valeur de la colonne.

Et vous pouvez avoir plusieurs filtres ici.

Donc, ici, je n'ai pas la ligne numéro trois, je pense que je l'ai déjà supprimée.

D'accord, donc continuons, la table produits trois, je voulais juste vous montrer qu'elle contient beaucoup plus de données que ma autre table.

Vous pouvez voir qu'elle contient des données sur 5849 lignes, je voulais aussi vous montrer ce paramètre particulier, le paramètre de configuration MySQL pour activer et désactiver les mises à jour sécurisées.

Donc, disons que votre instruction delete ou UPDATE n'utilise pas une colonne de clé primaire dans la clause where, vous savez, alors essentiellement si vous activez ce paramètre particulier, disons en définissant celui-ci, et ensuite si vous exécutez votre delete, vous obtiendrez comme un code d'erreur 1175, il signifie, et ensuite il dit que vous utilisez le mode de mise à jour sécurisée, etc., etc.

Il ne vous laisse pas exécuter ce genre d'ajouter des instructions de suppression, car cela pourrait causer de mauvaises performances.

Donc, si je désactive la même chose, et ensuite si j'exécute l'instruction Delete, et ensuite je lance un select à nouveau, alors cela devrait fonctionner car maintenant le paramètre est désactivé.

Et deux choses de plus.

L'une est en fait, si vous avez une table énorme et que vous voulez supprimer seulement quelques lignes à la fois, alors vous pouvez utiliser le mot-clé limit pour limiter le nombre d'enregistrements qui sont supprimés par l'instruction, vous savez, dans ce cas, parce que je voulais supprimer seulement 10 lignes, allons-y et faisons cela.

Et cela devrait fonctionner sans problème.

Et ensuite, si je fais un select, vous verrez la différence dans le compte de lignes, en fait, maintenant c'est comme 5839, avant c'était 5849.

Donc, c'est comment la clause LIMIT vous aide également dans les planchers de limite, vous pouvez également spécifier la clause ORDER BY.

Elle trie essentiellement les données par ces colonnes, d'abord par quantité, puis par identifiant de produit, puis elle supprime les 100 premières ou la valeur que vous mettez ici, en fait.

Donc, allons-y et faisons-le et ensuite sélectionnons à nouveau.

Oui, Kearney, sept D est parti.

Donc, les 10 premières lignes sont parties.

Et oui, c'est à peu près tout.

En fait, ce sont toutes les quelques variations des instructions de mise à jour et de suppression.

Et bien sûr, il y a beaucoup de tangentes dans lesquelles nous pouvons nous engager, mais je vais vous laisser cette tâche.

Et j'espère que cela a été utile.

Et si vous avez des questions, faites-le moi savoir dans les commentaires.

Je vous verrai dans la prochaine session.

Apprenants de MySQL.

Dans cette session, nous allons examiner les instructions SELECT, non seulement la syntaxe, mais aussi quelques moyens d'améliorer les performances de vos requêtes. Je vais utiliser le schéma appelé income store pour expliquer cette instruction SELECT dans sa forme la plus simple, qui ressemblera à ceci.

Donc, vous avez les mots-clés Select et from, et ensuite après Select, vous spécifiez la liste de sélection, qui est les colonnes que vous voulez sélectionner.

Si vous spécifiez une étoile ou un astérisque, cela sélectionne en fait toutes les colonnes de cette table, et ensuite après le mot-clé from, vous spécifiez les noms des tables à partir desquelles vous voulez sélectionner les données.

Donc, si je fais un select star from products underscore three, cela va retourner toutes les données de la table products underscore three.

Mais rappelez-vous que chaque fois que vous utilisez une étoile après le Select, ou dans la liste de sélection, vous interrogez essentiellement toutes les colonnes de cette table, vous n'avez pas besoin d'interroger toutes les colonnes de la table dans la plupart des cas, donc vous spécifiez uniquement les colonnes que vous devez interroger.

Donc, dans cette prochaine requête, allons ligne par ligne et voyons quels changements ont été apportés à cette requête pour la rendre meilleure.

Donc, disons que je veux sélectionner uniquement ces colonnes.

C'est pourquoi j'ai spécifié uniquement ces colonnes dans la liste de sélection.

Dans la clause from, j'ai spécifié la table products underscore three, très souvent vous allez sélectionner à partir de plusieurs tables, vous devez joindre les tables et ensuite récupérer des données utiles.

Et dans la clause where, vous spécifiez tous les filtres, ou les conditions en fonction desquelles vos données seront filtrées.

Donc, ici, j'inclus uniquement les données qui ont une quantité inférieure à 25.

Ainsi, je peux filtrer la plupart des données de cette table, ce qui est très utile pour minimiser la quantité de données que vous récupérez de la base de données.

Et vos requêtes seront rapides, ordered by va essentiellement trier les données qui sont récupérées en fonction des colonnes que nous spécifions ici.

Donc, ici, je trie simplement par nom de produit.

Et bien sûr, lorsque vous triez des données, surtout lorsque vous triez beaucoup de données, l'opération peut être coûteuse, à moins que votre taille de tampon de tri, qui est en fait la zone mémoire où les tris se produisent, ne soit correctement dimensionnée, l'opération peut être vraiment lente.

Donc, vous devez prêter attention à cette configuration également.

Et j'ai cette autre requête, qui montre simplement que c'est une instruction SELECT très simple.

Encore une fois, dans ce select, j'ai en fait seulement le mot-clé Select et une fonction, j'utilise la fonction now.

Mais il y a plusieurs autres fonctions SQL que vous pouvez utiliser dans le script, par exemple, je peux utiliser la fonction database pour retourner la base de données à laquelle je suis réellement connecté.

Et comme vous pouvez le voir, je suis en fait capable d'invoquer plusieurs fonctions dans la même requête.

Donc, c'est à peu près tout.

Je vous verrai dans la prochaine session.

Dans cette session, je vais enseigner les jointures SQL, plongeons directement dans la démonstration, je vais utiliser un schéma appelé eecom store.

Et je crée d'abord une table appelée T one avec une colonne, le nom de la colonne est C one, et j'insère ces deux valeurs dans cette table.

Un et deux, je crée une autre table appelée T deux avec une colonne appelée C one et j'insère ces deux valeurs à nouveau, dans la table D deux, un et trois.

Donc, c'est un et deux ici et un et trois, ici, nous allons exécuter un commit pour rendre mes modifications permanentes.

Donc, je vais simplement créer ces deux tables juste pour vous montrer les enregistrements, D one a un et deux, D deux a un et trois.

Bien sûr, une jointure est une opération qui joint deux tables.

Et nous avons tous ces différents types de jointures, nous allons les passer en revue une par une et comprendre ce qu'elles sont.

Donc, voici la syntaxe, donc sélectionnez une liste de colonnes que vous sélectionnez.

Donc, nous joignons T one et T two.

Et ensuite, nous spécifions le type de jointure que nous faisons.

Et ensuite, nous avons également ce mot-clé on.

Et ensuite vient la condition sur laquelle la table est jointe.

Donc, je vais exécuter cette requête et voir ce qui se passe.

Comme vous pouvez le voir, cette requête, cette jointure interne a retourné la valeur un, donc cela signifie en fait, donc elle retourne les valeurs qui existent dans les deux tables qui correspondent.

Donc, c'est ce que fait INNER JOIN.

Donc, changeons simplement pour une jointure gauche, allez-y et exécutez-la.

Maintenant, la jointure gauche va retourner toutes les valeurs de votre table gauche qui est T one.

Donc, T one a les valeurs un et deux sont les lignes un et deux, et ensuite T two, elle va retourner seulement les valeurs correspondantes.

Et ensuite, pour cette valeur, qui n'existe que dans la table T one, elle va retourner et maintenant et je vais la changer en jointure droite et comme vous l'avez peut-être deviné, elle va retourner toutes les valeurs de la table t à dans les endroits où il n'y a pas de valeur correspondante, elle va retourner un null.

Donc, voyons si cela se produit.

C'est ce que nous attendions.

Donc, nous avons obtenu toutes les lignes de T deux, et ensuite pour trois, il n'y a pas de valeur correspondante et T one, vous savez, cette position n'a pas de valeur.

Maintenant, nous allons sauter rapidement à une union.

Et ensuite, nous reviendrons à une jointure complète, une union est essentiellement comme ceci.

Donc, deux requêtes, et ensuite entre les deux, nous avons le mot-clé union, voyons ce qu'il retourne, vous pouvez voir qu'il a écrit un, deux, et trois.

Donc, ce sont en fait les lignes des deux tables, mais c'est un peu comme si les données étaient combinées et ensuite écrasées ensemble.

Et ensuite, vous avez un, deux, et trois, et ensuite, exécutons la même requête avec une légère différence.

Nous allons mettre union all et ensuite nous verrons ce qui se passe.

Cela a écrit un, deux, et un, trois.

Donc, cela a retourné toutes les données des deux tables, sauf cette fois, nous avons des valeurs en double, Union se débarrasse de toutes les valeurs en double, c'est presque comme un ensemble où vous avez un ensemble unique de données, union all retourne toutes les valeurs, y compris les données en double.

Revenons à la jointure complète, nous n'avons pas de mot-clé de jointure complète.

Donc, plutôt, nous faisons la jointure complète de cette manière dans ma séquence.

Donc, essentiellement, vous avez la requête similaire où vous joignez T one et T two, une jointure gauche d'abord sur cette colonne que nous avons, et ensuite vous avez une autre requête, à nouveau, en joignant T one et T two sur cette colonne, mais ensuite nous faisons une union de ces deux, et cela va retourner les données des deux tables, nous avons un, deux, ces deux correspondent, puis pour deux, il n'y a pas de valeur correspondante.

Donc, il retourne et maintenant pour trois, il n'y a pas de valeur correspondante dans T one, il retourne un null ici.

Donc, c'est une jointure complète, ce sont essentiellement toutes les jointures, tous les différents types de jointures que vous pouvez faire dans MySQL, j'espère que cet exemple était clair.

Et je vous verrai dans ma prochaine session.

D'accord, les apprenants de MySQL.

Dans cette section, nous allons apprendre les verrous.

Plus spécifiquement, je veux parler de la section des niveaux d'isolation.

Donc, la première chose est de voir ce que j'ai ici, j'ai deux sessions de terminal.

L'une est en noir.

L'autre est en couleur marron clair.

Donc, je vais en fait me connecter à la base de données en tant qu'utilisateur root.

Et je vais faire la même chose ici.

Les voilà.

Je suis connecté à ma base de données MySQL.

Donc, j'ai un petit script ici pour créer une table factice appelée T one.

D'accord, donc laissez-moi vous montrer le script SQL.

À ce stade, en fait, vous ne comprenez peut-être pas la syntaxe SQL et ainsi de suite.

Mais laissez-moi expliquer.

La première chose que je fais est de définir l'auto-commit à zéro ou commit est essentiellement une commande que vous utilisez pour sauvegarder votre travail.

Essentiellement, les modifications de données que vous effectuez sont stockées de manière permanente dans la base de données.

Lorsque vous émettez une commande commit dans ma séquence, vous avez cette variable appelée auto-commit, qui est activée par défaut, ce qui signifie que toutes vos commandes seront automatiquement validées.

Si vous ne désactivez pas cela, je veux avoir plus de contrôle sur ce que je fais ici.

Donc, essentiellement, je fais une désactivation de l'auto-commit d'abord, et ensuite je commence une transaction.

Et juste pour être sûr, je supprime cette table si je l'ai déjà créée.

Donc, cette table n'existe pas.

Donc, il dit table inconnue.

Et la chose suivante est que je crée une table appelée T one dans le schéma eecom store.

Et ensuite, le nom de la colonne est C one.

Et le type de données est int et c'est la clé primaire.

Donc, et ensuite, j'insère en fait une valeur, juste une ligne dans cette table appelée p one, n'est-ce pas, celle que nous venons de créer.

Et j'émets une commande commit, alter ou l'alternative à commit est la commande rollback.

Donc, qui annule essentiellement les modifications que vous venez de faire dans cette session.

Donc, si je fais simplement un select star à partir de la table, alors je vais voir cette valeur, donc qui est bien jusqu'à présent.

Donc, c'est assez simple.

Jusqu'à présent, nous n'avons pas parlé des niveaux d'isolation.

Donc, ce que j'entends par niveau d'isolation, c'est lorsque plusieurs sessions essaient de modifier ou d'accéder aux mêmes données, vous avez besoin d'un mécanisme de verrouillage pour vous assurer que les données ne sont pas corrompues, ou que la base de données se comporte de la manière que vous attendez de voir comment vous définissez réellement les niveaux d'isolation.

Et voici la commande.

Donc, voici l'autre session que j'avais ouverte, show session variables like isolation.

Donc, cela montre que le niveau d'isolation des transactions est défini sur read committed.

Exact.

Donc, c'est l'une des options possibles.

Donc, c'est read committed, et vous avez read uncommitted, et vous avez repetative read, ou repeatable read.

Et ensuite, vous avez une valeur serializable, en fait, donc allons-y une par une, d'accord.

Dans cette session, j'ai déjà commencé une transaction.

Donc, je vais en fait essayer de mettre à jour cette valeur en utilisant une commande de mise à jour.

Donc, essentiellement, je mets à jour la même table, et je mets à jour cette colonne à deux où la valeur de la colonne est actuellement un, n'est-ce pas.

Donc, je vais faire cela, l'auto-commit est désactivé.

Donc, ce n'est pas encore validé pour le début d'une transaction ici.

Et laissez-moi exécuter une requête contre la même table et simplement copier et coller le nom de la table, voulez-vous le taper, d'accord, donc nous voyons la valeur un, qui est la valeur précédente.

Et si j'ai exécuté la même requête ici, dans cette session, je vois la valeur deux, parce que c'est la session où nous modifions les données, n'est-ce pas ? Donc, je peux voir les modifications avant de les valider dans la même session ici.

En fait, puisque la valeur de cette transaction isolation, ou le niveau d'isolation est défini sur read committed, il est possible de ne lire que les données validées.

En d'autres termes, lorsque plusieurs sessions accèdent aux mêmes données, dans ce cas, cette colonne ici de cette table, à part la session qui modifie réellement les données, les autres sessions ne peuvent voir que les données validées, toutes les données qui ont été validées juste avant que ce select soit exécuté.

Donc, je vais aller ici et exécuter un commit, et revenir ici et exécuter un select.

Donc, maintenant vous voyez les dernières données parce que ce commit s'est produit avant que j'ai exécuté cette requête.

Maintenant, parlons de l'isolation read uncommitted, en fait, reconnectons-nous, car ces choses peuvent devenir compliquées.

Donc, chaque fois que je veux simplement recréer les tables pour éliminer toute confusion.

Donc, reconnectons-nous, d'accord, ici, et je vais en fait exécuter le même script que je vous ai montré auparavant.

Donc, désactivation de l'auto-commande, début d'une transaction, suppression de la table et recréation, insertion de cette valeur, puis exécution de la commande.

Donc, maintenant, ici, ce que nous pourrions faire, c'est aller de l'avant et mettre à jour cette valeur à deux.

Mais rappelez-vous, je n'ai pas encore validé ces données.

Allons à cette session.

Et ici, allez-y et changez le paramètre d'isolation en read uncommitted, car par défaut, il est toujours défini sur read committed.

Exact.

Donc, vous pouvez voir cela ici.

Donc, c'est un paramètre au niveau de la session.

Et vous pouvez également le changer au niveau global.

Mais pour les besoins de cette démonstration, nous devons simplement le changer au niveau de la session.

Donc, le niveau d'isolation de la session est initialement read committed, puis j'ai exécuté set session transaction, isolation level, read uncommitted, et ensuite vérifié la valeur à nouveau.

Maintenant, il est changé en read uncommitted, si j'ai exécuté un select star à partir de cette table, alors j'obtiens la valeur deux, et si vous vous souvenez que j'ai mis à jour la valeur de un à deux.

Et vous pouvez déjà voir cette valeur même si elle n'est pas validée ici.

Donc, c'est ainsi que fonctionne read uncommitted.

Il n'y a pas beaucoup de verrouillage ici.

Parce que la base de données permet maintenant aux sessions de faire des lectures sales, car une session est capable de lire les changements des autres sessions même avant que les validations ne se produisent, n'est-ce pas.

Donc, ce sont des lectures sales.

Oui, en fait.

Donc, passons au suivant.

Donc, nous avons vu read, committed et read Committed jusqu'à présent.

Donc, maintenant, passons à repeatable reads.

Exact ? Donc, exit.

Donc, ici, je vais simplement valider.

Et je vais relancer mon script initial juste pour effacer la table.

Donc, drop table et ensuite recréer, insérer, valeur un à nouveau, et ensuite valider.

Donc, maintenant, la table est revenue à ce à quoi elle ressemblait avant.

Donc, ici, laissez-moi me reconnecter.

Donc, c'est le paramètre repeatable read, n'est-ce pas ? Donc, rappelez-vous que la valeur par défaut pour ce paramètre d'isolation est toujours read committed.

Donc, si je le change en repeatable read, write, et ensuite vérifie la valeur à nouveau, alors vous pouvez voir cela.

Donc, et encore une fois, rappelez-vous, ou show variables est la commande pour vérifier la valeur actuelle.

Et ensuite, set est la commande pour définir la configuration, n'est-ce pas, donc je vais mettre toutes ces commandes dans un fichier de dépôt GitHub, puis vous pouvez en fait prendre les commandes de là, et ensuite vous pouvez les essayer vous-même.

Essentiellement, je change le paramètre de read committed à repeatable read, n'est-ce pas, donc je vais simplement commencer une nouvelle transaction ici, je vais mettre à jour cette valeur à deux.

Et ici, je vais exécuter la requête Select que nous avons vue avant, en sélectionnant simplement tout de cette table.

Et vous voyez que la valeur est actuellement un.

Et cela a du sens.

Donc, laissez-moi aller de l'avant et exécuter un commit.

Et si j'ai exécuté la même requête, à nouveau, je vois la valeur un.

Et cela est le même que la valeur qui a été lue avant, même si les données ont été modifiées par cette autre session.

Et ensuite validées dans cette transaction, les données que nous voyons sont les mêmes, en d'autres termes, essentiellement, nous lisons les mêmes données, ou les lectures sont répétées.

Exact.

Donc, c'est le troisième paramètre.

Et le dernier est la configuration de verrouillage la plus stricte.

Donc, qui est appelée serializable.

Donc, je vais, comme d'habitude, je vais supprimer la table et ensuite simplement les recréer, recréer, insérer la valeur un à nouveau, ils peuvent venir.

Donc, ici, nous allons nous reconnecter.

Et comme d'habitude, le paramètre par défaut est read committed, n'est-ce pas ? Donc, vérifions cela d'abord, juste pour vous montrer, et ensuite je vais le changer en serial serializable.

Donc, ce que cela signifie, c'est que, essentiellement, je vais commencer une transaction.

Donc, sur la première session, je vais exécuter une mise à jour, en changeant essentiellement la valeur de un à deux.

Et ici, je vais commencer une transaction, et je vais exécuter une requête sur cette table.

Exact.

Et maintenant, cette requête, même si ce n'est qu'un select, select est juste une lecture, ce n'est pas une mise à jour, ce n'est pas une suppression ou autre chose, c'est juste une lecture, elle attend, parce que la mise à jour met essentiellement à jour ces données.

Et ensuite, la base de données MySQL ne laisse même pas cette lecture ou la requête Select de l'autre session voir les données.

Donc, c'est le paramètre le plus strict.

Donc, si je fais un commit ici, alors sur cette autre session, vous verrez que le Gradius retourne et il voit la dernière valeur, n'est-ce pas.

Donc, si je vais de l'avant et exécute un autre select, bien sûr, il retourne la même chose.

Mais si j'essaie de mettre à jour cette valeur de deux à trois, une autre mise à jour, qui est essentiellement en attente sur le Select, essentiellement cette transaction qui est en cours d'exécution maintenant parce que le Select à nouveau, select est juste une lecture, il lit simplement les données.

Mais il verrouille toujours cette ligne dans la base de données, et il n'autorise aucune mise à jour ou modification de ces données.

Et ensuite, vous pouvez voir que la mise à jour a même échoué parce qu'elle a attendu un certain temps et ensuite la valeur de délai d'attente a été dépassée, donc nous n'avons pas besoin d'entrer dans ces détails.

Mais je vais essayer de mettre à jour maintenant.

Et ici.

Je vais simplement sortir de cette session, ce qui libérera tous les verrous.

Et cela aidera la mise à jour à passer.

Et ensuite, je peux valider et sortir également, et savoir si cela était clair pour vous.

Et si vous avez des questions, mettez-les dans les commentaires et contactez-moi d'une manière ou d'une autre, je sais que vous pouvez le comprendre, vous êtes la prochaine section.

Hey, les apprenants de MySQL.

Donc, bienvenue dans cette nouvelle section de mon tutoriel MySQL.

Donc, dans cette vidéo, ou dans cette section, nous allons parler des verrous.

Donc, qu'est-ce que ces verrous ? D'accord ? Donc, abordons cela de manière logique.

Donc, si vous avez une base de données, et si vous êtes la seule personne à travailler dans cette base de données, alors vous n'avez essentiellement pas à vous soucier de quoi que ce soit, n'est-ce pas ? Vous savez ce que vous faites.

Donc, vous insérez des données, supprimez ou mettez à jour des données comme vous le souhaitez.

Et il n'y a personne d'autre qui essaie d'intervenir ou d'interrompre votre travail.

Mais malheureusement, ce n'est pas le cas.

Dans le monde d'aujourd'hui.

Si vous pensez à une base de données de commerce électronique très fréquentée comme Amazon, alors il y a beaucoup de choses qui se passent sur ces sites web.

Il y a beaucoup de gens qui naviguent, il y a beaucoup de gens qui achètent des choses.

Il y a des gens qui vendent des choses sur ces sites web, ils mettent à jour les données relatives à leurs produits.

Donc, c'est essentiellement de la concurrence, n'est-ce pas ? Donc, vous avez de nombreux utilisateurs qui essaient de faire quelque chose sur ce site web en même temps, comment gérez-vous cette concurrence, c'est pourquoi nous avons besoin de verrous.

Donc, si je laisse tout le monde travailler sur les mêmes données en même temps, alors il y aura beaucoup de confusion.

Et nous pourrions finir par perdre certaines données.

Donc, laissez-moi en fait vous montrer un exemple simple de la façon dont cela se produit.

Donc, j'ai une table, une table de produits.

Donc, si vous avez suivi mon tutoriel jusqu'à présent, nous avons parlé de cette table appelée produits.

Donc, où nous stockons toutes les informations sur les produits, n'est-ce pas.

Donc, maintenant, il y a quelques enregistrements ici.

Et disons que nous avons un vendeur et un acheteur qui travaillent sur ces enregistrements, surtout comme cet enregistrement particulier, le premier, qui est un livre, et le prix du livre, et la quantité, la chose que nous n'avions pas de quantité lorsque nous en avons parlé dans mes sections précédentes.

Mais ensuite, j'ai ajouté la quantité ici.

Donc, il y a cette colonne de quantité.

Et il y a un vendeur et un acheteur intéressés par cet enregistrement, regardons cela, n'est-ce pas, donc nous avons une sorte de séquence temporelle ici.

Ce que le vendeur de ce produit particulier essaie de faire, c'est qu'il essaie de mettre à jour la quantité de ce produit à neuf heures, il ajoute 60 quantités supplémentaires à ce produit, ce qui est, vous savez, 40 plus 60, ce qui fait 100.

Et c'est ce que nous avons ici.

Ensuite, un acheteur arrive et il regarde la quantité.

Et ensuite, il veut essentiellement commander deux ou ces livres, c'est 100 moins 90, 100 moins deux, c'est 98 et ensuite vous avez la quantité 98 ici.

Donc, cela s'est produit dans une séquence.

Donc, mais nous nous inquiétons de la concurrence, n'est-ce pas ? La concurrence, c'est quand les choses se produisent en même temps.

Mais que se passe-t-il si, d'abord, le vendeur arrive et lit la quantité de cet article.

Initialement, elle était de 40, puis l'acheteur arrive et voit également que la quantité est de 40.

N'est-ce pas ? Et à 9h01.

Donc, les deux premières opérations se produisent en même temps à neuf heures ou une heure, le vendeur arrive, il dit que je veux mettre à jour, je veux ajouter 60 quantités supplémentaires, comme si je voulais dire que j'ai 60 livres de plus de ce titre, mais ensuite l'acheteur arrive et dit d'accord, j'achète deux articles ou deux de ces livres.

Mais pendant que vous faisiez cela, il a vu avant que c'était 40.

Donc, 40 moins deux est 38.

Donc, il met à jour la quantité à 38.

Donc, le vendeur met à jour à 200.

Mais ensuite, à cause de cette recherche précédente, la quantité est mise à jour à 38.

En raison de quoi, cette opération entière, cette opération entière est perdue.

Et nous nous retrouvons avec des données corrompues pour cette colonne de quantité.

Donc, c'est un exemple simple de la façon dont la concurrence, lorsqu'elle n'est pas bien gérée, peut causer des problèmes de données comme celui-ci.

Apprenants de MySQL.

Donc, dans cette vidéo, nous allons examiner comment fonctionnent les verrous de table.

Dans le contexte d'une base de données de commerce électronique, nous avons créé une base de données simple ou un schéma appelé le magasin de colonnes.

Et nous avons créé un tas de tables ou utilisé une autre table factice pour expliquer nos niveaux d'isolation des transactions.

Donc, si vous n'avez pas vu mon matériel précédent, retournez et vérifiez-le.

Et revenez ici.

Mais alors oui, vous avez quatre tables principales.

Et la table principale qui nous intéresse est la table des produits ici.

Et dans la table des produits, j'ai inséré quelques enregistrements.

Ce sont des enregistrements factices.

Donc, je n'ai pas de front-end ou d'application en cours d'exécution ici.

Donc, nous regardons simplement la base de données, n'est-ce pas.

Donc, ce qui va se passer dans ce tutoriel, c'est que nous allons essentiellement simuler une situation où un vendeur essaie de mettre à jour la quantité du livre qu'il vend sur ce site web, qui est en fait ce premier livre, le chemin commun vers le succès peu commun.

Et ensuite, la quantité de ce livre disponible.

Vous savez, pour ce livre est de 40, n'est-ce pas ? Donc, il veut mettre à jour cette quantité à 200.

Et aussi, nous aurons quelques autres utilisateurs, ou acheteurs, en fait, un acheteur essaie d'acheter le même livre, nous aurons un autre acheteur Hill, qui a essayé d'acheter un livre différent, qui est ce livre, de petites habitudes, et ensuite le même acheteur essaiera également de parcourir le site web, comme bien sûr, nous allons devoir imaginer un peu parce que je n'ai pas de front-end pour vous montrer tout.

Donc, voyons comment cela se passe.

Tout d'abord, les bases d'abord, en fait, désactivons l'auto-commit.

Juste pour avoir plus de contrôle sur ce qui se passe.

Et laissez-moi faire cela dans les trois sessions que j'ai ouvertes et la première session est la session du vendeur.

La deuxième session est la session de l'acheteur un.

Et la troisième session est la session de l'acheteur deux, en fait.

Donc, je vais désactiver l'auto-commit, qui est essentiellement un mécanisme qui valide automatiquement si elle est activée.

Et je ne veux pas de cela.

Donc, je la désactive.

Ensuite, je veux vous montrer le niveau d'isolation des transactions.

Et nous en avons parlé dans ma session précédente.

Donc, pour l'instant, c'est une lecture répétable.

Et c'est la même chose pour tous.

Donc, nous allons le changer en lecture validée, car la lecture validée est l'isolation appropriée pour les bases de données OLTP.

Maintenant, commençons par la première session du vendeur.

Donc, trois sessions.

Donc, la première session du vendeur va mettre à jour la quantité de ce livre qui l'intéresse ou qu'il vend.

Mais nous allons adopter cette approche agressive et verrouiller toute la table.

Exact.

Donc, disons que l'application est conçue de manière à verrouiller toute la table des produits.

Et ensuite, la session de l'acheteur un, disons que l'acheteur un vient et essaie d'acheter deux livres et comment nous allons faire cela, c'est en exécutant une mise à jour.

Donc, nous mettons essentiellement à jour la table des produits et nous soustrayons la quantité de deux, ce qui signifie en fait que nous achetons deux livres.

Et quel livre est-ce dans le livre ? Où est l'enregistrement où l'identifiant du produit est égal à un, n'est-ce pas ? Donc, si vous vous souvenez des données, l'identifiant du produit un est ce livre, allons-y et exécutons cette mise à jour dans la deuxième session.

Et elle va évidemment attendre, parce que la table elle-même a été verrouillée pour l'écriture par la session du vendeur, la session de l'acheteur un est en attente.

Et allons à la session de l'acheteur deux, l'acheteur deux essaie d'acheter un livre différent, quel livre est-ce ce autre livre, qui est le livre des petites habitudes, où l'identifiant du produit est égal à deux.

Et nous allons faire cela.

Bien sûr, même cela est en suspens ou en attente.

Et c'est en fait un peu fou, n'est-ce pas.

Donc, les vendeurs essaient de mettre à jour la quantité de cet enregistrement avec juste un livre.

Et tout est en train de s'effondrer.

Et l'acheteur deux essayait d'acheter un livre différent, il abandonne un peu.

Donc, il passe à une session différente.

Et au lieu d'acheter ou d'essayer d'acheter un livre, il essaie simplement de parcourir le site web, ce qui est une requête de sélection ou une requête de lecture, une requête de sélection, qui est également en suspens.

Donc, l'acheteur deux est frustré en ce moment.

Donc, vous pouvez voir à quel point cette séquence est restrictive.

Donc, si quelqu'un utilise des verrous de table, cela va essentiellement réduire la concurrence des opérations qui peuvent se produire dans cette base de données.

Donc, c'est le point principal ici dans cette démonstration.

Hey, les apprenants de MySQL.

Donc, dans cette session, nous allons jeter un bref coup d'œil aux verrous au niveau des lignes.

Dans MySQL, j'ai trois sessions, je suis déjà connecté à ma base de données de commerce électronique, MySQL, et voici à quoi ressemblent les données maintenant.

Donc, nous avons une table de produits qui contient, vous savez, ces données, seulement deux livres maintenant, juste des données factices que j'ai créées, voici le prix et vous avez la colonne de quantité qui vous montre combien de quantité il reste pour chacun de ces livres.

Donc, la première session est la session du vendeur.

La deuxième session est la session de l'acheteur, nous pouvons appeler cela la session de l'acheteur un.

Et la troisième session est la session de l'acheteur deux.

Donc, voici les données.

Et juste pour plus de clarté, en fait, je voulais vous montrer le paramètre de niveau d'isolation des transactions, qui est read committed.

Et l'auto-commit est désactivé, essentiellement, il est désactivé.

Donc, à moins que je ne valide explicitement, mes transactions ne seront pas permanentes.

Donc, commençons par le vendeur.

Il va sur le site web ou un portail qu'il a à sa disposition pour mettre à jour l'inventaire, disons du livre un, ou du produit un, qui est ce livre.

Et donc, il va cliquer sur quelques boutons, ce qui se traduira par l'exécution d'une instruction de mise à jour dans cette base de données, n'est-ce pas ? Disons qu'il veut augmenter le nombre de livres disponibles dans l'inventaire.

Donc, cela signifiera que la quantité va être augmentée, incrémentée de 50.

Donc, c'est l'instruction de mise à jour.

Et il va exécuter cette mise à jour.

Et nous pouvons regarder la session de l'acheteur un, disons que l'acheteur un essaie d'acheter le même livre.

Et ensuite, donc il va sur le site web et ensuite clique sur acheter maintenant ou autre chose et ensuite cela se traduira par cette instruction de mise à jour dans la base de données, choisissez la quantité égale à la quantité moins un.

Donc, réduire la quantité de un, ce qui signifie qu'il achète un livre.

Et bien sûr, il y aura, vous savez, d'autres instructions mettant à jour d'autres tables.

Mais pour garder cela simple, je vous montre simplement la section des changements de la table des produits.

Donc, comme vous pouvez le voir, cela va attendre parce que le vendeur met à jour cette ligne particulière.

Et cela peut être vu en utilisant acquittee.

Sur les verrous de données, donc si vous êtes sous ce greddy, bien sûr, vous pouvez modifier cette requête selon vos besoins.

Mais ensuite, si vous interrogez cela, vous verrez qu'il y a un tas de sessions et est, est la colonne de mode de verrouillage.

Et ensuite la table sur laquelle la base de données sur laquelle les verrous se produisent, la table, donc cela vous donne beaucoup de détails.

Donc, si vous voulez comprendre ce qui se passe ici.

Donc, nous avons la table des produits, et ensuite nous avons le verrou ix, qui est l'intention, le verrou exclusif sur la table elle-même, ce qui signifie qu'une transaction est sur le point d'obtenir un verrou exclusif.

Et cela est au niveau de la table, mais ne vous laissez pas tromper par cela.

Il y a aussi un autre enregistrement indiquant qu'il y a un verrou au niveau de l'enregistrement ou de la ligne.

Et, et cela verrouille uniquement les données égales à un.

Donc, si vous vous souvenez de cette instruction de mise à jour, nous utilisons l'identifiant du produit.

Donc, et les données pour lesquelles est un, en fait, donc l'identifiant du produit est égal à un.

Donc, c'est ce que nous voyons ici.

Et si vous voyez ici, cette session d'acheteur a en fait dépassé le délai d'attente, donc il va tenter d'acheter à nouveau.

Donc, c'est ainsi que vous pouvez regarder les détails de verrouillage dans cette table.

Essayons, disons que l'acheteur deux arrive à ce moment-là.

Et ensuite, il essaie simplement de parcourir l'inventaire sur ce site web de commerce électronique.

Donc, cela signifierait une requête de sélection ou une requête de lecture.

Et il est capable de le faire, une réaction heureuse.

Exact.

Donc, il n'y a pas de problème.

Donc, pendant que les verrous de ligne se produisent, d'autres sessions peuvent lire cette table, elles peuvent même regarder les données pour le même produit.

Mais elles ne peuvent pas acheter ce livre, car cela est bloqué par le vendeur.

Donc, encore une fois, le délai d'attente a été dépassé.

Donc, à ce stade, l'acheteur deux veut acheter un livre différent, vous savez, je ne peux pas acheter ce livre, laissez-moi essayer d'acheter un livre différent, cela se traduira par, vous savez, l'identifiant du produit est égal à deux, qui n'est pas verrouillé par le vendeur.

Et ensuite, cette mise à jour passe.

Et à ce stade, disons que le vendeur a terminé la mise à jour de l'inventaire.

Et, bien sûr, si vous regardez les données, maintenant, elles vont avoir l'air différentes, car cela a été mis à jour à 150.

Et bien sûr, cela n'a pas diminué parce que l'acheteur, l'acheteur un est toujours en train d'acheter le livre, parce que la validation n'a pas encore eu lieu dans l'application.

Et ensuite, si nous regardons les données à nouveau, les données ont diminué, ou la quantité a diminué, puis via deux, disons que l'acheteur veut acheter le premier livre que l'acheteur un voulait acheter.

À ce stade, il n'y a pas de verrous dans cette table.

Parce que tout le monde a validé, et disons que l'acheteur, qui essaie d'acheter ce livre, et ensuite il passe à cette date, et ensuite il valide et regarde les données.

Et ensuite, les données changent en fait.

Donc, c'est ainsi que le verrouillage au niveau des lignes permet essentiellement une haute concurrence.

Donc, seules les lignes qui sont verrouillées par vos transactions ne sont pas disponibles pour ces autres sessions à modifier.

Exact. Donc, les autres enregistrements qui ne sont pas touchés par vos transactions sont disponibles pour la mise à jour, la suppression, etc.

et bien sûr, vous pouvez ajouter de nouveaux livres, cela signifie insérer de nouveaux enregistrements dans cette table.

Je voulais simplement vous montrer la différence entre les verrous au niveau de la table et les verrous au niveau des lignes.

Donc, cette session et ma session précédente seront utiles pour comprendre cette différence.

Merci, je vous verrai dans ma prochaine session.

Dans cette session, nous allons parler des interblocages.

Et je veux juste vous montrer comment les interblocages se produisent, ils se produisent souvent dans une base de données de commerce électronique ou B.

Donc, c'est une session courte et douce.

Donc, ici, nous avons quelques sessions à nouveau, donc connecté à la même base de données a deux sessions, deux sessions différentes.

Donc, disons que nous travaillons avec la table des produits, n'est-ce pas.

Donc, nous avons vu la table avant dans mes sessions précédentes.

Essentiellement, cette table contient des informations sur les produits qui sont vendus sur, vous savez, un site web de commerce électronique.

Donc, nous avons quelques enregistrements ici, vous savez, nous allons d'abord dire, vous savez, je viens, un vendeur vient pour mettre à jour la quantité de ce produit, essentiellement, disons s'il veut augmenter la quantité de 25.

Pour ce premier livre, c'est la commande qu'il, vous savez, qui va être exécutée, vous savez, quels que soient les boutons sur lesquels il clique, seront traduits en une commande de mise à jour comme celle-ci.

Exact.

Et disons qu'une personne différente de la même entreprise veut mettre à jour le prix de ce livre, pas ce livre, disons que nous l'avons, l'autre livre, je suis juste en fait en train d'utiliser l'identifiant du produit pour mettre à jour le bon produit, n'est-ce pas.

Donc, nous avons une session où le vendeur un met à jour la quantité de cet article, nous avons une autre session où nous mettons à jour le prix de cet article.

Et ensuite, si vous voyez le prix est incrémenté de deux, disons 2 $.

Et c'est bien, n'est-ce pas ? Donc, maintenant nous avons des verrous au niveau des lignes.

Donc, ce gars détient un verrou au niveau des lignes sur cette ligne.

Et ce gars détient un verrou au niveau des lignes sur cette ligne.

Donc, c'est bien, n'est-ce pas ? Donc, nous opérons sur deux enregistrements différents, deux verrous sont indépendants l'un de l'autre.

Tout va bien.

Donc, maintenant, disons que le même vendeur, la deuxième personne qui met à jour le prix, veut mettre à jour le prix de cet autre livre pour en fait augmenter le prix.

Encore une fois, de 2 $ de ce livre, l'identifiant du produit est égal à un, quel livre, celui-ci juste ici, allons-y et essayons d'incrémenter le prix.

En exécutant cette commande, vous savez, il attend le verrou ECI exclusif.

Et ce n'est pas disponible, parce que ce vendeur n'a pas encore validé, en fait, ce n'est pas validé.

Donc, allons-y et revenons ici, et ce vendeur en même temps, le prix de mettre à jour le prix ou la quantité de ce livre.

Donc, deux sessions se battent pour à peu près la même ressource, vous savez, nous avons abouti à une situation d'interblocage.

Donc, MySQL était assez intelligent pour simplement tuer la session.

Sinon, nous aurions deux sessions attendant l'une pour l'autre indéfiniment.

N'est-ce pas ? Donc, ici vous pouvez voir le code d'erreur qui est lancé, il dit deadlock trouvé en essayant d'obtenir des verrous et essayer de redémarrer cette transaction.

Donc, allons-y et interrogeons la table des produits et voyons à quoi elle ressemble.

Vous pouvez voir que cette transaction entière a été annulée.

Correct.

Les deux transactions ont été annulées.

Il y a même celle-ci qui a été annulée.

Donc, je pense que ce verrou a également été tué.

Donc, c'est pourquoi celle-ci a fonctionné.

Si vous pouvez voir les prix ont augmenté de 2 $.

Exact, car initialement, ils étaient de 1699 et 2039, et ici 8099 et 20 à 39.

D'accord, donc c'est ainsi que cela fonctionne.

C'est une situation typique d'interblocage, j'espère que cette explication était claire.

Et je vous verrai dans ma prochaine session.

D'accord, les apprenants de MySQL.

Donc, dans cette session, nous allons parler des index clusterisés.

Donc, l'index clusterisé n'est pas un type d'index différent, comme, vous savez, vous pouvez créer directement un index clusterisé vous-même.

Donc, c'est un type d'index que MySQL maintient en arrière-plan.

Donc, dans vos données de table, les données que vous insérez dans vos tables ou chargez dans vos tables sont maintenues dans ces index.

Les index seulement, ce que je veux dire par là, c'est que, disons que c'est un index B-tree, n'est-ce pas, donc c'est un index B-tree.

Donc, vous avez MySQL qui crée cet index B-tree lorsque vous chargez les données dans ces tables.

Et ensuite, vous savez, dans les nœuds feuilles, ce que vous avez, c'est en fait les données, les données que vous chargez dans ces tables, n'est-ce pas ? Dans le clustering, le tri est basé sur la clé primaire que vous définissez, ou, vous savez, dans cette table, en fait, donc si vous ne définissez pas de clé primaire, MySQL choisira automatiquement une clé d'index non nullable, ce que cela signifie, c'est que, disons que, en fait, sautons directement dans l'exemple que j'ai préparé pour vous.

Donc, voici mon MySQL Workbench.

Et, vous savez, je vais vous montrer cette définition de table.

Donc, cela s'appelle products underscore one.

Et c'est essentiellement une table de produits qui est typiquement utilisée dans un magasin de commerce électronique.

Et si vous avez suivi mes leçons, c'est ce que j'ai utilisé, j'ai simplement changé le nom de la table pour, vous savez, démontrer ce concept, ce concept de clustering, d'index clusterisé.

Donc, vous avez toutes ces colonnes, et je définis une clé primaire.

D'accord, donc commençons par, vous savez, je vais simplement passer à une base de données appelée eecom, store notre schéma appelé le magasin eecom, je vais supprimer, vous savez, ces tables si elles existent déjà, par hasard.

Donc, la table n'existe pas, ce qui est bien, donc je vais créer cette table dont je viens de parler, appelée produits.

Et ensuite, cette table a une clé primaire dans une clé primaire est l'identifiant du produit.

Donc, l'identifiant du produit est une sorte de colonne entière.

Donc, c'est un auto-incrément, n'est-ce pas ? Donc, vous n'avez même pas besoin de fournir de valeur pour cette colonne, en fait, lorsque vous chargez les données, donc vous pouvez simplement mettre toutes ces informations et les charger et ensuite nous sommes bons, MySQL incrémentera automatiquement la valeur de cette colonne.

Donc, et ensuite, bien sûr, comme je l'ai dit, comme il y a une colonne isbm, qui est ici, une sorte de livre isbm.

Et information si vous êtes, vous savez, si vous vous souvenez de vos jours d'école comme ça, c'est un numéro attaché à un livre, donc quelque chose comme ça.

Donc, un genre de numéro alphanumérique ISDN.

Donc, je vais appeler cela une clé unique ou une contrainte unique.

Et allons-y et créons la table et cette contrainte.

Donc, cela a été créé avec succès.

Et je vais créer une procédure, que je peux utiliser pour remplir la table, n'est-ce pas, ne vous inquiétez pas des détails de cette procédure.

C'est quelque chose que j'ai écrit pour remplir cette table.

Et ensuite, cela a été créé avec succès et changer le délimiteur en un point-virgule.

Et ensuite, je vais appeler cette procédure et qui va lancer quelques avertissements, ce qui est bien pour moi.

Tant que les données sont peuplées, je suis content.

Donc, cela va probablement générer quelques, vous savez, charger plus de 6000 lignes dans cette table.

Donc, nous verrons combien nous obtenons, c'est génial.

Donc, cela charge en fait beaucoup de données.

Cela semble être terminé.

Donc, allons-y et validons les données et maintenant, en fait, je vais sélectionner les données dans cette table, n'est-ce pas ? Juste sélectionner toutes les données, et vous verrez que les données par défaut, ou les données sont en fait triées en fonction de la clé primaire, qui est l'identifiant du produit.

Et vous pouvez voir, nous savons, je n'ai pas spécifié de tri.

Donc, c'est, vous savez, c'est le tri par défaut des données, n'est-ce pas.

Et donc, essentiellement, vos données de table sont triées en fonction de votre index clusterisé, qui est la clé primaire ici, parce que vous avez la clé primaire dans la section de la table.

Exact.

Donc, maintenant, la chose suivante est en fait, je vais créer une table similaire, qui est, vous savez, donc je vais l'appeler produits deux.

Mais dans ce cas, je vais essentiellement ne pas définir de clé primaire, je vais toujours avoir une clé unique appelée, encore une fois, la même chose, vous savez, c'est isbm, c'est une clé unique.

Et donnons-lui simplement un nom différent, juste pour que nous ayons une sorte de, nous avons des noms différents pour différentes contraintes.

Donc, allons-y et créons cette table.

Et donc cette table est créée, je vais copier les données de la première table où vous savez, j'ai chargé beaucoup de données.

Donc, je vais copier les données de cette table dans cette table, n'est-ce pas.

Donc, très simple.

Et ensuite, je vais valider, n'est-ce pas, donc c'est un conseil 6455 6455 nombre de lignes insérées dans cette table.

Et je vais sélectionner toutes les lignes de cette table.

Et vous pouvez voir que maintenant, les données ne sont pas triées par l'identifiant du produit, mais plutôt par cet isbm.

Et il trie en fonction du premier caractère d'abord, puis initialement, les premier et deuxième caractères sont les mêmes, puis 010 vrai.

Et cela continue 05 et ensuite 090, un BCD de GE haie et ensuite avoir après les zéros, vous savez, voir un, donc il trie essentiellement les données en fonction de l'isbm.

Et pourquoi est-ce que cela se produit ? Parce qu'en l'absence de clé primaire, il va choisir cette colonne isbm, comme la clé d'index unique non nullable, qui est basée sur la colonne isbm, n'est-ce pas.

Donc, il trie en fonction de cela, mais c'est en fait une idée terrible, terrible.

Parce que si vous générez des chaînes alphanumériques aléatoires pour isbm.

Et, vous savez, alors vous n'allez pas générer la chaîne dans un ordre ascendant ou dans un type d'ordre, en fait.

Donc, dans ce cas, en fait, vous savez, lorsque vous insérez des données dans la table, cet arbre B va être créé en arrière-plan.

Et ensuite, MySQL, comme tout programme qui crée ou maintient cette structure de données en arrière-plan, doit travailler très, très dur pour gérer cet index B-tree, en fait, n'est-ce pas.

C'est pourquoi c'est une mauvaise idée d'avoir un UID ou une sorte de chaîne alphanumérique comme clé primaire, en fait, ou en l'absence de clé primaire.

Eh bien, MySQL va utiliser cette clé pour le clustering.

Et encore une fois, c'est très mauvais.

Donc, gardez cela à l'esprit lorsque vous créez des tables, en fait.

Exact.

Donc, enfin, ce que je vais faire, c'est créer une autre table appelée produit trois.

Et avant cela, je vais vous montrer le résultat de cette requête, qui est essentiellement vide ou non, non, non, aucune ligne retournée.

Tout ce que je fais, c'est vérifier si cet index, l'index nommé Jen flushed index est là dans cette base de données, en fait.

Et ensuite, je vérifie les tables InnoDB et information schema, je joins les tables odb et les index odb.

Et je vérifie si cet index existe, n'est-ce pas ? En disant qu'il n'existe pas, c'est pourquoi ce crédit retourne aucune ligne, et je vais créer cette table et cette fois, je ne vais même pas créer la clé unique.

Et je vais rendre toutes ces colonnes comme des colonnes nulles, vous savez.

Donc, je veux juste vous montrer ce qui se passe lorsque vous avez un scénario où vous créez une table avec toutes les colonnes nulles et aucune clé primaire, aucun index unique, pas de clé unique, et vous savez, ensuite, je vais insérer des données dans cette table.

Encore une fois, six, les 400 plus lignes insérées, valider.

Et ensuite, je vais sélectionner à partir de cette table de produits trois maintenant.

Et lorsque les données apparaissent, vous pouvez voir qu'il y a encore un certain tri qui se produit.

Et, vous savez, nous n'avons aucune de ces options de clé primaire ou de clé unique non nulle disponibles, alors comment MySQL peut-il trier les données ? Qu'est-ce qu'il utilise, donc il utilise en fait une clé cachée, une clé primaire cachée.

Donc, si vous exécutez la même requête, encore une fois, est prêt, vous pouvez voir que cet index a été créé sur la table des produits trois, qui est maintenu en interne par MySQL, juste dans le but de clusteriser cette table, en fait.

D'accord, donc c'est beaucoup d'informations.

J'espère que vous avez trouvé cela utile.

Et je vous verrai dans ma prochaine vidéo.

Bonjour, les apprenants de MySQL.

Donc, dans cette session, je veux vous enseigner les bases de l'utilisation de explain ou du plan expliqué dans MySQL.

D'accord, donc maintenant, laissez-moi simplement vous montrer la table avec laquelle je vais travailler, je vais travailler avec cette table appelée products underscore one.

Et elle contient un nom de produit, un type de produit, un prix.

Et si le produit est un livre, il aura un numéro ISPN qui lui est attaché.

Et ensuite, il y a une colonne de quantité.

Donc, ce sont quelques colonnes de base que vous verriez dans un magasin en ligne de commerce électronique.

Donc, commençons par simplement regarder les index de cette table.

Donc, celle-ci a essentiellement deux index.

L'un est un index de clé primaire, qui est sur l'identifiant du produit.

Et l'autre est un index sur la colonne isbn.

Et celui-ci est en fait un index unique.

Donc, commençons par choisir une requête simple que nous allons optimiser en utilisant explain.

Donc, la requête que je vais utiliser est celle-ci.

Donc, je vais sélectionner isbn.

Et à partir de cette table products underscore one où le nom du produit contient cat.

Donc, le nom du produit est cat.

D'accord, donc et avant d'exécuter cette requête, je vais regarder le plan expliqué.

Et je vais mettre un slash g à la fin.

Donc, j'obtiens ce qui sera mis là dans un format lisible.

Tout d'abord, il donne cette sortie, n'est-ce pas, et selectors, juste un straights, simple select.

C'est ce que cela montre.

Mais la chose principale est que nous travaillons avec notre cette ligne particulière fait référence à cette table.

Et en dehors de cela, en fait, vous avez toutes ces colonnes, et ensuite elles sont toutes nulles pour l'instant, comme elles ne font pas beaucoup de sens en dehors de cela.

Donc, c'est une colonne serrée et all signifie qu'elle effectue un scan complet de la table.

Essentiellement, MySQL effectue un scan complet de la table, il scanne toute la table.

Et combien de lignes est-ce ? C'est autant de lignes.

Et nous utilisons un filtre ici, il obtient toutes ces lignes et ensuite il filtre la sortie.

Et essentiellement, vous savez, il y a environ 600 lignes avec le nom du produit égal à cat, n'est-ce pas, donc le pourcentage filtré est comme 10%, essentiellement, et ensuite il y a quelques informations supplémentaires.

Allons-y et créons un index sur cette table.

Créons un index appelé, vous savez, nous pouvons donner un nom arbitraire.

Et, et je vais créer un index sur la table products one et la colonne est le nom du produit, bien sûr.

C'est la colonne sur laquelle je crée l'index.

En fait, allons-y et exécutons explain à nouveau.

Donc, c'est le plan expliqué.

Et voici à quoi il ressemble.

Donc, essentiellement, vous pouvez voir que le encore une fois, c'est à peu près le même type de sortie, mais cette fois, il montre également quelques données pour toutes ces colonnes.

Donc, tout d'abord, la colonne des clés possibles montre comme tous les index que cette requête peut utiliser.

Et, et parmi lesquels, comme celui-ci est la clé ou l'index qu'il est, vous savez, il va utiliser cette exécution particulière va utiliser, et c'est la longueur de la clé en octets, en fait, le nombre de lignes qui sont scannées dans cette clé, qui est 589.

Et, vous savez, puisque cela est basé sur l'index, nous ne filtrons pas vraiment les données, plutôt, nous allons simplement à l'index et obtenons les données.

Donc, il n'y a pas de filtrage là-bas.

Créons en fait un autre index, qui inclut également isbn.

Et, et voyons, comme, ce qui se passe, en fait, nous allons créer l'autre index et lui donner un nom différent.

Donc, allons-y et exécutons le plan expliqué à nouveau.

Donc, maintenant, encore une fois, les clés possibles sont ces deux index, mais il choisit toujours d'aller avec cet index particulier, et la longueur de la clé d'index est la même, et ensuite les lignes, etc., etc.

Donc, il n'y a pas eu de filtrage, n'est-ce pas ? Parce que nous choisissons un index.

Donc, vous vous demandez peut-être, comme, vous savez, pourquoi il n'utilise pas l'index couvrant, n'est-ce pas.

Donc, cela est censé être l'index couvrant et les index couvrant sont censés être meilleurs que l'index non clusterisé normal ou un index secondaire.

Donc, vous pouvez en fait utiliser un format comme le format JSON pour obtenir plus d'informations.

Donc, comment vous pouvez faire cela, c'est simplement en spécifiant comme format égal JSON, et utilisez cela.

Et donc, cela va vous donner la sortie au format JSON.

Et vous pouvez voir que, vous savez, il vous donne un peu plus d'informations, comme le coût de la requête, vous savez, c'est combien cela va coûter à MySQL pour exécuter cette requête.

Et c'est une représentation de la quantité de travail que MySQL doit faire pour exécuter cette requête.

Donc, le coût pour celle-ci est de 7690, n'est-ce pas.

Et ensuite, il dit que ce sont les clés possibles.

Et la clé utilisée est utilisée, les parties de la clé sont le nom du produit, qui n'a pas été donné ici.

Et ensuite, il y a un coût et pour lequel est une division de là où le coût va.

Donc, vous pouvez lire la documentation MySQL sur tous ces champs.

Vous savez, vous vous demandez peut-être pourquoi l'index couvrant n'est pas utilisé.

Et nous pouvons en fait forcer cet index en utilisant cette syntaxe ou ce mot-clé use index.

Et ensuite, je vais mettre le nom de l'index que je veux forcer, qui est celui-ci.

Et lorsque je l'ai exécuté, ce plan expliqué montre que le coût de celui-ci va être de 109,27, vous savez, en comparaison avec le plan expliqué précédent, où le coût n'est que de 76.

Et c'est pourquoi MySQL utilise ce plan particulier au lieu de celui-ci.

D'accord, j'espère que cette session a été utile.