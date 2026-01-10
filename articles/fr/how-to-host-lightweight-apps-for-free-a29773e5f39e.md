---
title: Comment héberger des applications légères gratuitement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-26T15:46:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-lightweight-apps-for-free-a29773e5f39e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m8zEyzBZkPlhZlNZ-w1gaw.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: coding
  slug: coding
- name: Heroku
  slug: heroku
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment héberger des applications légères gratuitement
seo_desc: 'By Pubs Abayasiri

  When you look for web hosting services, there are many free options available. But
  there aren’t that many places where you can host full stack web apps that involve
  APIs, CGI, or AJAX backend queries — especially if you want to use ...'
---

Par Pubs Abayasiri

Lorsque vous cherchez des services d'hébergement web, il existe de nombreuses options gratuites. Mais il n'y a pas autant d'endroits où vous pouvez héberger des applications web full stack impliquant des APIs, CGI ou des requêtes backend AJAX — surtout si vous souhaitez utiliser autre chose que PHP.

Cet article est un guide simple mais significatif de type « marcher avant de courir » sur la façon de commencer à héberger vos scripts sur des serveurs cloud.

### **Quand utiliser une plateforme d'application cloud**

Les plateformes d'applications cloud fonctionnent bien dans les scénarios où vous avez besoin d'un peu de code pour s'exécuter sur un serveur. De nombreuses plateformes offrent une série de conteneurs d'applications basés sur Linux (qui apparaissent comme des machines virtuelles) où vous déployez le code développé sur votre ordinateur local avec un ensemble de mots-clés de ligne de commande.

Heroku est un tel service que vous pourriez utiliser pour héberger votre code (dans divers langages) relativement facilement. Il offre un modèle freemium où ils vous permettent d'utiliser environ 500 heures de calcul gratuitement (leurs tarifs complets sont [ici](https://www.heroku.com/pricing)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*5r9A_yT2n4zTeBVXAJRD_w.png)
*En mai 2017, les langages de programmation que vous pouvez héberger sous Heroku*

Une fois que vous avez écrit votre code sur votre bureau local, vous pouvez exécuter des commandes qui déplient le code sur un espace de travail dans Heroku. Le code s'exécute ensuite en fonction d'un déclencheur. Les déclencheurs peuvent être un travail planifié, un serveur web déclenché par une requête de page web, ou quelque chose qui s'exécute constamment et traite des données — ce qui pourrait devenir assez coûteux.

Ce qui est vraiment bien, c'est que vous n'avez pas à vous soucier du système d'exploitation (mémoire, stockage, CPU, correctifs de sécurité) car tout cela est géré pour vous — mais en même temps, cela signifie que vous avez une flexibilité limitée puisque vous ne pouvez pas allouer de ressources directement.

Quelques exemples spécifiques où Heroku peut bien fonctionner pour vous :

* Héberger votre propre site web où vous souhaitez écrire votre propre serveur web
* Récupérer périodiquement des données d'un site web puis les stocker dans une base de données pour analyse
* Offrir un serveur API pour une tâche spécifique. Des choses comme offrir des données météo, stocker des données de capteurs Internet des Objets, ou un appel de service web pour un modèle d'apprentissage automatique
* Un service de base de données (bien qu'un service comme Firebase soit peut-être mieux adapté)

### **Architecture Heroku**

Heroku fournit une machine virtuelle (VM) légère pour déployer votre code. Notez que sous l'option gratuite, vous pouvez déployer jusqu'à 5 applications considérées comme 5 VM légères. Pour votre application réelle, vous recevez un sous-domaine URL séparé sous Heroku. Ainsi, les noms de vos projets doivent être uniques.

Ces espaces de travail ont leur propre espace pour des composants tels que : fichiers de code et de ressources (non des fichiers de données dynamiques), base de données (Postgres), et fichiers de journalisation.

Sur votre bureau local, Heroku utilise le nom de votre répertoire pour définir votre projet, et aussi pour que Heroku comprenne votre contexte. Ainsi, vous pouvez avoir plusieurs projets dans différents répertoires et lorsque vous exécutez les commandes Heroku — assurez-vous simplement de le faire dans le bon dossier.

La chose clé à laquelle vous devez être attentif (que j'ai découverte à la dure après des heures de débogage — j'aurais souhaité prêter plus attention à la documentation) est que tout est exécuté à partir de la mémoire. Il n'y a pas de stockage persistant. Je le répète — vous ne pouvez pas stocker de fichiers sur le serveur de fichiers ! Pour la persistance, Heroku offre une base de données SQL postgress où vous pouvez ajouter des enregistrements selon vos besoins.

### **Un exemple simple — détection de changement de site web**

Voici un guide étape par étape pour obtenir un exemple fonctionnel d'un service simple qui vous enverra un email si un site web a changé — essentiellement un clone de [www.changedetection.com](http://www.changedetection.com). Il y aura plusieurs composants clés :

1. Une base de données qui stockera : (a) l'adresse email à notifier d'un site web changé ; (b) le site web à suivre ; (c) la dernière « copie » du site web
2. Un morceau de code qui vérifiera un site web donné à partir de la base de données dans #1 (script Python)
3. Un planificateur de tâches qui exécutera le programme dans #2 (équivalent d'une tâche cron)
4. Une interface utilisateur web où vous pouvez ajouter/supprimer des sites web à surveiller dans la base de données mentionnée dans #1
5. Un mécanisme pour envoyer des emails

Comprendre ces composants vous dotera des compétences pour faire beaucoup de choses déjà. J'ai appris toutes ces choses à travers de multiples sources, donc cela sert de post consolidé.

### **Hypothèses**

Le guide suivant fait les hypothèses suivantes :

* Vous avez un compte GitHub — si ce n'est pas le cas, veuillez en créer un [ici](https://github.com/). Vous devriez également lire ce guide simple [ici](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1/).
* Vous avez déjà un compte Heroku — si ce n'est pas le cas, veuillez en créer un [ici](http://www.heroku.com).
* Vous utilisez une machine Windows — si ce n'est pas le cas, ce n'est pas grave, les instructions sont assez similaires dans d'autres environnements
* Vous avez déjà installé Python — si ce n'est pas le cas, veuillez aller [ici](https://www.continuum.io/downloads) pour l'installer
* Vous pouvez déjà programmer en Python — si ce n'est pas le cas, je vous suggère d'apprendre d'abord quelques bases. Certains guides sont [ici](https://medium.mybridge.co/19-free-ebooks-to-learn-programming-with-python-8f6f0ad4a7f8).
* Vous connaissez SQL — si ce n'est pas le cas, veuillez aller [ici](https://www.w3schools.com/sql/DEfaULT.asP).

### **Aperçu des étapes**

Je trouve qu'une approche « marcher avant de courir » aide au processus d'apprentissage. Cela sert également de documentation pour vous-même sur la façon de résoudre chaque partie du processus plus large. Ainsi, si quelque chose ne fonctionne pas dans votre future entreprise, vous avez une meilleure chance de comprendre où cela a mal tourné.

**Étape 1** : Développer l'interface utilisateur web — construire d'abord Hello World

**Étape 2** : Persistance — créer une base de données

**Étape 3** : Vérifier les sites web pour les changements

**Étape 4** : Envoyer une notification par email en cas de changements

**Étape 5** : Lister la sortie sur la page web

**Étape 6** : Déployer

### **Étape 1 : Développer l'interface utilisateur web — construire d'abord Hello World**

Tout d'abord, déployons un programme simple sur Heroku pour commencer. Ce programme sera un précurseur de l'interface utilisateur web (élément #4) dans la liste des composants ci-dessus. Pour servir une page, nous pourrions simplement avoir une page HTML, mais nous aurions alors besoin d'un serveur web pour servir ce fichier. En d'autres termes, lorsque vous tapez l'URL du site web, un programme devrait interpréter la requête, puis fournir le contenu du fichier HTML. Vous pouvez créer votre propre mini serveur web avec la bibliothèque Python Flask, ce que nous allons faire.

* Créez un dossier appelé webchecker et allez dans ce répertoire (ce nom de répertoire n'a pas besoin d'être le même que le nom de l'application Heroku)
* Installez la bibliothèque Flask. Entrez la commande : npm Flask
* Créez le programme Python suivant et nommez-le showchecks.py :

Avant de déployer sur Heroku, testez qu'il fonctionne sur votre PC local. Vous pouvez le tester avec les étapes suivantes :

* Exécutez le programme : python webchecker.com
* Ouvrez votre navigateur sur votre PC local et ouvrez la page : [http://localhost:5000/hello](http://localhost:5000/hello)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GXR1TOFAk6wIUCm_mVTWLQ.png)
*L'exécution du script retournera une page statique avec la sortie 'hello world'*

Ensuite, déployons cela sur Heroku. Avant de pouvoir déployer, il doit y avoir quelques fichiers supplémentaires à inclure pour aider Heroku à en savoir plus sur votre application.

Tout d'abord, le fichier requirements.txt

Deuxièmement, le fichier pour dire à Heroku quoi exécuter lorsqu'une requête web est faite :

Enfin, la version d'exécution de Python à utiliser (par défaut 2.7, mais nous voulons spécifier la dernière version de Python) :

Ainsi, vous devriez avoir quatre fichiers :

1. showchecker.py qui est le code
2. requirements.txt pour la liste des dépendances de bibliothèque non standard. Chaque fois que vous avez de nouvelles bibliothèques qui ne font pas partie de la bibliothèque standard Python — c'est-à-dire que vous devez les installer à l'aide d'un outil tel que « pip » — ajoutez-les ici. Vous pouvez trouver la version d'une bibliothèque installée telle que Flask en exécutant la commande : `pip show Flask` dans la ligne de commande
3. Procfile qui est le script Python réel à exécuter lorsque le site web est appelé — assurez-vous de le mettre à jour si vous changez le fichier Python
4. runtime.txt qui est la version réelle de python à utiliser

Vous pouvez déployer avec les étapes suivantes à partir de la ligne de commande :

1. heroku create webchecker01 — buildpack heroku/python
2. git add *.* *
3. git status
4. git commit -m "all files"
5. git push heroku master

![Image](https://cdn-media-1.freecodecamp.org/images/1*nLcnlwU1UocIvqbiHhviXQ.png)
*Une fois que vous exécutez « git push heroku master », les journaux de déploiement seront affichés, y compris l'URL où il est déployé*

Pour la commande #1 (`heroku create…`), la partie « webechecker01 » est le nom unique que vous devrez fournir pour le nom de l'application.

Pour la commande #3 (`git status`), cela vous indiquera quels fichiers sont prêts à être déployés. Assurez-vous que tous les fichiers sont là, sinon ajoutez-les en utilisant `git add <nomdefichier>`.

Maintenant, vous pouvez vérifier votre site web : <nomdelapplication>.herokuapp.com/hello

![Image](https://cdn-media-1.freecodecamp.org/images/1*tSMmTHoxgA2-xXQ0RaTrHg.png)
*Le programme hello world s'exécutant sur le web*

Assurons-nous également de pouvoir voir les journaux, car c'est un excellent moyen de voir ce qui se passe avec votre serveur d'applications. Sur votre PC et dans le répertoire webchecker, exécutez la commande : `heroku logs`

![Image](https://cdn-media-1.freecodecamp.org/images/1*GQkthW50XPatw-J7fnrDlA.png)
*« heroku logs » est une commande cruciale à exécuter pour voir ce qui se passe dans votre serveur d'applications*

Vous verrez les dernières étapes d'exécution. Si les choses ne fonctionnent pas comme prévu, c'est votre premier arrêt pour obtenir plus de détails.

Vous pouvez également aller au tableau de bord Heroku pour voir votre consommation :

[https://dashboard.heroku.com](https://dashboard.heroku.com)

### **Étape 2 : Persistance — créer une base de données**

Pour créer des programmes plus utiles, vous aurez besoin d'un type de stockage de données. C'est là qu'intervient le service de base de données Postgres. Vous devez d'abord déployer le service de base de données Heroku, puis créer vos tables, et enfin pouvoir vous connecter à la base de données à partir de votre code local (pour les tests).

Pour déployer un service de base de données, créez-le d'abord en utilisant la commande suivante :

`heroku addons:create heroku-postgresql:hobby-dev`

Ensuite, accédez à la base de données à partir de la ligne de commande et créez vos tables. La base de données est créée sur le service cloud Heroku et non localement. Cependant, vous pouvez y accéder via la ligne de commande. Pour vous connecter à la base de données via la console, exécutez la commande `heroku pg:psql`. N'oubliez pas que vous devez le faire dans votre dossier webchecker afin que Heroku sache qu'il s'agit de la base de données pour le site webchecker.

Pour voir la liste des tables, tapez la commande `\d`

![Image](https://cdn-media-1.freecodecamp.org/images/1*sctwYakzP69ePN-W50Rezw.png)

Pour créer une table, vous devez utiliser des instructions SQL normales. Pour notre programme webchecker, créons une table avec les colonnes suivantes :

* ID — identifiant généré automatiquement pour chaque entrée (ce sera la clé primaire). Cela se fait en utilisant le type « serial »
* website — le site web à surveiller
* emailaddress — l'adresse email à laquelle envoyer la notification qu'un changement s'est produit
* lasthashcode — nous ne stockerons pas une copie de toute la page web, mais nous générerons un hachage basé sur le HTML de la page, puis nous le comparerons à chaque fois. Cela est plus efficace en termes de stockage, mais ne nous dira pas ce qui a réellement changé
* lastchangedate — la date à laquelle le web a changé la dernière fois. Ainsi, nous ferons en sorte que la base de données définisse par défaut cette date avec la date actuelle

Pour créer cette table, entrez la commande suivante dans la console de la base de données Heroku Postgres :

```
CREATE TABLE webcheckerdb (id serial, website varchar(250), emailaddress varchar(250), lasthashcode varchar(32), lastchangedate timestamp DEFAULT current_date );
```

(Assurez-vous d'inclure le point-virgule à la fin !)

![Image](https://cdn-media-1.freecodecamp.org/images/1*DJFH7kef_tDJhIse7sazWA.png)
*Création de la base de données, puis utilisation de l'option \d pour voir la liste des tables et ensuite « \d webecheckerdb » pour voir les colonnes*

Ensuite, insérons un seul enregistrement dans la base de données pour nous assurer d'avoir quelque chose avec quoi travailler avant de mettre en place notre interface web (vous pouvez utiliser votre propre adresse email pour que cela fonctionne à l'avenir) :

```
INSERT into webcheckerdb values(DEFAULT, 'news.google.com', 'email@me.com', '', DEFAULT);
```

(Assurez-vous d'inclure le point-virgule à la fin !)

![Image](https://cdn-media-1.freecodecamp.org/images/1*lzafM9Y_USmlAaY-FPIjGw.png)
*Vous pouvez ensuite faire une instruction select (inclure le point-virgule à la fin !) pour voir les données*

Vous pouvez quitter avec `\q`.

### **Étape 3 : Vérifier les sites web pour les changements**

Tout d'abord, obtenons un morceau de code pour vérifier au moins si un site codé en dur peut être récupéré (en suivant le concept de marcher avant de courir).

Ainsi, la première étape est de voir si nous pouvons récupérer une page web, la hacher, puis la comparer à un hachage codé en dur. Créez un nouveau fichier Python appelé checkwebsite.py. Code ici :

L'exécution de ceci produira la sortie suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mnR-Yfax_dWTE3GeoffaaQ.png)

Si vous avez des erreurs avec des bibliothèques manquantes, vous pouvez les ajouter via : `pip install <bibliothèque>` depuis la ligne de commande.

Ensuite, connectons-nous à la base de données avec le code suivant :

Lorsque vous essayez d'exécuter ce code, vous risquez d'obtenir une erreur de la forme `KeyError: 'DATABASE_URL'`. Cela est dû au fait que votre code Python essaie de localiser l'adresse web de la base de données Postgres hébergée sur Heroku. Cela est automatiquement mis à jour dans la variable d'environnement DATABASE_URL sur le serveur Heroku. Cependant, sur votre PC local, vous devrez le faire manuellement :

1. heroku config
2. set DATABASE_URL=<la chaîne de la base de données listée à partir de « heroku config »>

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q4i73mFPaKPuDobdX9G_ZA.png)
*Si vous obtenez l'erreur DATABASE_URL, définissez la variable d'environnement*

### Étape 4 : Envoyer une notification par email en cas de changements

La dernière étape consiste à envoyer un email. Pour cela, vous devrez installer un Addon capable d'envoyer des emails — vous pouvez les trouver via le marché Heroku : [https://elements.heroku.com/addons](https://elements.heroku.com/addons)

Ici, il y a un Addon appelé SendGrid : [https://elements.heroku.com/addons/sendgrid](https://elements.heroku.com/addons/sendgrid)

Vous pouvez ajouter SendGrid à votre application dans la ligne de commande en tapant :

`heroku addons:create sendgrid:starter`

Lorsque vous allez à votre tableau de bord, vous pouvez voir le nouvel Addon dans la section Ressources :

![Image](https://cdn-media-1.freecodecamp.org/images/1*c15ERSHkLS2tpByYFEJM1g.png)
*L'addon SendGrid qui peut activer l'envoi d'emails sera en bas*

Avant de l'utiliser, vous devrez créer une clé API. Double-cliquez sur le composant SendGrid ci-dessus et allez dans Paramètres->Clé API->Créer une clé (bouton bleu en haut à droite).

![Image](https://cdn-media-1.freecodecamp.org/images/1*DENX5_vY3u5ibFsMNW0Dug.png)
*Cliquez sur le bouton Créer une clé en haut à droite*

Une fois que vous avez créé la clé, copiez-la et retournez à l'invite de commande et entrez :

`heroku config:set SENDGRID_API_KEY=<clé API de ci-dessus>`

Cela ne l'enregistrera que sur le serveur, vous devez l'ajouter localement à votre bureau avec :

`set SENDGRID_API_KEY=<clé API de ci-dessus à nouveau>`

Une fois terminé, vous pouvez tester votre code dans un nouveau script Python appelé sendmail.py. Installez la bibliothèque via `pip install sendgrid` :

Pour confirmer que l'email a été envoyé et livré, vous pouvez retourner au tableau de bord SendGrid et vérifier l'écran Aperçu des statistiques :

![Image](https://cdn-media-1.freecodecamp.org/images/1*i3v-OiFWlQhSEY_1y2VNoQ.png)

Lorsque vous vérifiez votre email, n'oubliez pas de vérifier votre spam.

Une fois que cela fonctionne, il n'y a que deux lignes de code que vous devez ajouter à votre script principal checkwebsite.py. C'est :

```
import sendmail #import la sous-routine d'envoi d'email que vous avez écrite ci-dessus
```

```
...
```

```
#appeler la sous-routine après avoir trouvé que le hashcode a changé
sendmail.sendemail(webrecord['emailaddress'], 'Site web changé', webrecord['website'] + ' changé')
```

Le code complet est ici :

### **Étape 5 : Lister la sortie sur la page web et planifier le travail**

L'étape suivante consiste à lister la sortie sur la page web.

Cela implique d'interroger la base de données, puis de parcourir et d'afficher les données sur votre écran. Ainsi, cela reprend le code « Hello World » ci-dessus et apporte la modification. J'ai également créé un chemin différent pour cela, donc pour tester cela, vous devrez aller à l'URL : http://localhost:5000/list

Et voici la sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cr3hYo0DKRwBiXhfgVLE0g.png)

### Étape 6 : Déployer

La dernière étape consiste à déployer tout sur Heroku puis à planifier le travail afin qu'il vérifie les emails.

Vous devriez avoir les fichiers suivants :

1. Procfile — le fichier qui pointe vers showchecker.py
2. requirements.txt — le fichier qui contient les dépendances de bibliothèque
3. runtime.txt — la version de python
4. showchecker.py — le code python qui affiche la sortie de la base de données sur le web via <nomdevotreapp>.herokuapp.com/list
5. checkwebsite.py — le code python qui vérifie les changements sur les sites web

Pour le fichier requirements.txt, vous devrez apporter des modifications pour ajouter les dernières bibliothèques :

Déployez le tout sur Heroku :

1. git add *.* *
2. git commit -m "déploiement"
3. git push heroku master

Testez chaque composant :

1. Allez sur <nomdevotreapp>.herokuapp.com/hello
2. Allez sur <nomdevotreapp>.herokuapp.com/list

Si des erreurs surviennent, exécutez `heroku logs` dans la ligne de commande pour voir ce qui se passe.

Ensuite, exécutez checkwebsite.py directement sur Heroku pour vous assurer qu'il n'y a pas de problèmes. Pour cela, vous pouvez taper :

`heroku run python checkwebsite.py`

![Image](https://cdn-media-1.freecodecamp.org/images/1*eTeK6EvsZjWvMw-IYnDGuA.png)
*C'est un excellent moyen de s'assurer que votre code s'exécute aussi bien sur le cloud heroku qu'en local*

Enfin, vous pouvez maintenant planifier votre travail. Encore une fois, vous devez inclure un Addon pour cela.

`heroku addons:create scheduler:standard`

![Image](https://cdn-media-1.freecodecamp.org/images/1*6O4ealFi6wtJ2OuE-wXa8w.png)

Et vous devriez pouvoir voir le planificateur dans votre page de ressources :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RG3zOR_MfVjM2fjHStyZmg.png)
*L'addon planificateur a également été inclus, que vous pouvez double-cliquer*

Vous pouvez simplement utiliser la ligne de commande pour exécuter le programme, dans notre cas, c'est : `python checkwebsite.py` (c'est la même chose que ce que nous avons testé ci-dessus avec la commande `heroku run`).

![Image](https://cdn-media-1.freecodecamp.org/images/1*zfwYHHgSwOl4WHIcY1DJTw.png)
*Vous pouvez planifier cela avec quelques options.*

### Résumé

Et c'est tout... la première fois, c'est un peu complexe, mais espérons que les étapes incrémentales ci-dessus vous aideront à comprendre ce qui se passe sous le capot. Il existe de nombreuses autres ressources sur [Heroku](http://www.heroku.com) ainsi qu'une mine d'informations sur [Stack Overflow](http://stackoverflow.com/). Ces ressources devraient avoir beaucoup plus de sens après avoir parcouru ce qui précède.

Bonne chance !

*Merci d'avoir lu ! Si vous aimez ce que vous lisez, cliquez sur le bouton ❤️ ci-dessous pour que d'autres puissent trouver cela (vous pouvez aussi me trouver sur [Twitter](http://www.twitter.com/pubs12))*