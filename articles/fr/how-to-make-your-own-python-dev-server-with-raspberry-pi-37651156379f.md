---
title: Comment créer votre propre serveur de développement Python avec Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T17:10:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-own-python-dev-server-with-raspberry-pi-37651156379f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ylvkldd2jkFaSSpn8MdVTQ.png
tags:
- name: Python
  slug: python
- name: Raspberry Pi
  slug: raspberry-pi
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer votre propre serveur de développement Python avec Raspberry
  Pi
seo_desc: 'By Karan Asher

  In simple terms, Raspberry Pi is a super cheap ($40) Linux based computer. That’s
  it. Seriously.

  It can do whatever you can imagine a normal Linux computer can do, such as browse
  the web, write code, edit documents, and connect to I/O ...'
---

Par Karan Asher

_En termes simples, Raspberry Pi est un ordinateur basé sur Linux super bon marché (40 $). C'est tout. Sérieusement._

Il peut faire tout ce que vous pouvez imaginer qu'un ordinateur Linux normal peut faire, comme naviguer sur le web, écrire du code, éditer des documents et se connecter à des périphériques d'E/S tels qu'une clé USB, une souris, un clavier, etc. Ce tutoriel se concentrera sur l'apprentissage de la création de votre propre serveur de développement Python avec Raspberry Pi.

### Étape 0. Définir l'objectif

Avant de commencer, il est important de comprendre ce que nous essayons de construire. À la fin de ce tutoriel, vous serez en mesure d'exécuter un site web de base (en utilisant [Flask](http://flask.pocoo.org/)) sur un Raspberry Pi sur votre réseau local domestique.

L'objectif de ce tutoriel est de démontrer comment un Pi peut être utilisé comme serveur de développement, plus spécifiquement, l'exemple sera d'héberger un site web simple (en utilisant [Flask](http://flask.pocoo.org/)).

### Étape 1. Énoncer les hypothèses

Voici quelques hypothèses que ce tutoriel fera :

1. Vous avez déjà un Raspberry Pi configuré avec le système d'exploitation Raspbian. [Voici](https://www.raspberrypi.org/documentation/setup/) un guide d'installation utile si vous en avez besoin.
2. Le Pi est connecté à votre WiFi domestique (et que vous connaissez l'adresse IP du Pi).
3. Vous n'aurez pas besoin d'un écran à l'avenir, en supposant que les points 1 et 2 sont complets.

Nous utiliserons [VS Code](https://code.visualstudio.com/) avec l'extension [Remote VSCode](https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode) pour créer et éditer des fichiers à distance sur le Pi. Je vous recommande définitivement d'utiliser ces deux outils pour suivre ce tutoriel. De plus, ils faciliteront grandement le travail avec des fichiers distants, ce qui est un avantage.

### Étape 2. Trouver l'adresse IP du Pi

Tout d'abord, connectez le Pi à une alimentation électrique et assurez-vous qu'il est correctement démarré et connecté au WiFi/Ethernet (en gros, il doit avoir une connexion Internet).

Nous utiliserons ssh pour nous connecter et communiquer avec le Pi. Pour cela à distance à l'aide d'un ordinateur portable, vous devez connaître son adresse IP. Cela peut être facilement obtenu en utilisant le portail d'administration de votre FAI (généralement disponible à [http://192.168.0.1](http://192.168.0.1). Veuillez noter que cela peut être différent pour différents FAI.)

Généralement, votre Pi devrait être connecté à une adresse qui pourrait ressembler à '192.168.0.12'. Encore une fois, cela sera différent pour différentes personnes. Utilisez donc l'adresse IP que vous avez trouvée pour votre Pi dans le portail d'administration. Pour la suite, ce tutoriel utilisera 192.168.0.12 comme adresse IP du Pi.

### Étape 3. Se connecter au Pi en utilisant ssh

Ouvrez VS Code et sa fenêtre de terminal intégrée sur votre ordinateur portable. Connectez-vous au Pi avec une adresse IP de 192.188.0.12 en utilisant la commande ssh suivante :

> _ssh -R 52698:localhost:52698 pi@192.168.0.12_

La commande ci-dessus établira un canal de communication bidirectionnel entre votre ordinateur portable et le Pi. Si c'est la première fois que vous vous connectez au Pi, utilisez 'raspberry' comme mot de passe. Il peut vous être demandé de changer votre mot de passe par défaut. Il est fortement recommandé de le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/k-iRsowxI6mnJfpiWmQPGkQOiaRQ8OE50gpg)
_Fenêtre de terminal après s'être connecté avec succès au pi_

### Étape 4. Créer un répertoire de projet

Vous devriez maintenant être dans le répertoire personnel du Pi. Créons un répertoire pour le site web que nous souhaitons construire. Utilisez la commande suivante pour créer le répertoire :

> _mkdir MyFlaskWebsite_

Utilisez la commande 'ls' pour vérifier que vous pouvez effectivement voir un nouveau dossier nommé MyFlaskWebsite.

![Image](https://cdn-media-1.freecodecamp.org/images/cUhjzjTdVOTdFCANjEYrStpwuNoy4YsKWTZj)
_Créer et vérifier le répertoire de projet_

### Étape 5. Installer Flask

Nous utiliserons [Flask](http://flask.pocoo.org/) pour créer un site web simple. [Flask](http://flask.pocoo.org/) est un micro-framework web basé sur Python. Il utilise [Jinja](http://jinja.pocoo.org/) (moteur de template basé sur Python) comme moteur de template, ce qui le rend très utilisable et puissant. Utilisez la commande suivante pour installer flask sur le Pi :

> _sudo apt-get install python3-flask_

![Image](https://cdn-media-1.freecodecamp.org/images/JBEt1A3RTqaIUErc0sevCZjxpZMppU1qTCjA)
_Installer flask_

### Étape 6. Écrire du code de base

Maintenant que Flask est installé, nous pouvons commencer à créer des fichiers et à écrire du code. Tout d'abord, naviguez vers votre nouveau répertoire de projet (de l'étape 4) en utilisant la commande suivante :

> _cd MyFlaskWebsite_

Tous les fichiers et dossiers du projet résideront dans ce répertoire 'MyFlaskWebsite'. Maintenant, créez votre premier fichier de code (app.py) en utilisant la commande suivante :

> _touch app.py_

En vérifiant le répertoire avec la commande 'ls', vous devriez pouvoir voir ce fichier nouvellement créé.

![Image](https://cdn-media-1.freecodecamp.org/images/Ad9fp3IFU8Q2TtuKgRC3f3-dInXyaEQ-6NZH)
_Naviguer vers le répertoire de projet et créer un nouveau fichier_

Maintenant, appuyez sur F1 et choisissez 'Remote Start Server.' Cela devrait vous permettre d'éditer des fichiers à distance sur le Pi en utilisant votre ordinateur portable.

![Image](https://cdn-media-1.freecodecamp.org/images/UB9XT8GkO3T49BOvUd6iAX6yn2iAbHiqKbqi)
_Démarrer le serveur distant_

Ensuite, utilisez la commande suivante pour commencer à éditer le fichier app.py nouvellement créé. Cela peut prendre quelques secondes, mais le fichier vide devrait alors être visible dans la fenêtre ci-dessus.

> _rmate app.py_

![Image](https://cdn-media-1.freecodecamp.org/images/O4Ybu5hVBCof4wGQ8q4z5c4MEA5zvNgBzkXv)
_Commencer à éditer le fichier à distance_

Tapez le code montré dans l'image ci-dessous. Ici, nous avons défini une route vers la page d'accueil du site web qui devrait afficher 'This is my flask website and it is so cool.' Notez que le fait de définir l'hôte sur 0.0.0.0 permet à ce site web d'être accessible par tous les appareils connectés au même réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/oyV0xCTNN59M32nPsaqLs5oCB8IwBNfgqiWC)
_Créer un site web de base_

Enregistrez le fichier et utilisez la commande suivante pour exécuter le site web sur le serveur Pi :

> _python3 app.py_

![Image](https://cdn-media-1.freecodecamp.org/images/V1gtV9AL1LrQnyZaQhq-5zk7eCuvaNMrmsWw)
_Exécuter le site web_

Après avoir reçu le message de succès ci-dessus, ouvrez une nouvelle fenêtre de navigateur sur n'importe quel appareil de votre réseau et tapez l'adresse IP du Pi (dans ce cas, il s'agit de 192.168.0.12) suivie du port sur lequel le serveur de développement est en cours d'exécution (5000). L'adresse complète sera donc [http://192.168.0.12:5000/](http://192.168.0.12:5000/)

Vous devriez voir le texte 'This is my flask website and it is so cool.' sur la page web.

![Image](https://cdn-media-1.freecodecamp.org/images/3OunjfD19vW0jkUprzpCRgxftK3PU1cWf2mT)
_Vérifier la page web dans un navigateur_

Cela confirme que votre serveur de développement est actif et exécute le site web que vous venez de créer.

### Étape 7. Ajouter plus de routes

Actuellement, le code ne contient qu'une seule route, qui est la page d'accueil du site web. Ajoutez une autre route en tapant le code suivant. Notez que vous pouvez apporter des modifications dynamiquement pendant que le serveur de développement est en cours d'exécution. Il capturera automatiquement le delta (changement de code) et exécutera une version révisée une fois que vous aurez actualisé votre fenêtre de navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/wFupha2dFoFLYbsxCjKwMHjnTXmD5YKLwuMu)
_Ajouter une route meow_

Pour vérifier si la nouvelle route fonctionne comme prévu, allez sur [http://192.168.0.12:5000/meow](http://192.168.0.12:5000/meow) et la page web devrait vous 'MEOW'.

![Image](https://cdn-media-1.freecodecamp.org/images/I-YacWJFs3S2wcDN2pVniaEwwkZj8B0XCZUN)
_Vérifier que la nouvelle route fonctionne comme prévu_

### Étape 8. Ajouter une structure à votre code

Maintenant, ajouter plus de routes est cool, mais avoir tout le code dans un seul fichier app.py n'est pas la façon dont un site web devrait être structuré. Habituellement, nous aurions un dossier avec des modèles HTML, un dossier avec des fichiers CSS statiques et un autre pour les fichiers JS. Ajoutons ces dossiers et déplaçons le code dans les dossiers appropriés pour mieux structurer notre code. Utilisez les commandes suivantes pour créer ces répertoires :

> _mkdir templates_

> _mkdir static_

Utilisez la commande 'ls' pour vérifier que ces dossiers ont été créés.

![Image](https://cdn-media-1.freecodecamp.org/images/MfI2Gvi6kC0WFxxxRkS9Jn4HYdu8KWF56teL)
_Ajouter une structure à votre code_

Maintenant, créons un fichier HTML pour la page d'accueil. Utilisez les commandes suivantes pour naviguer vers le répertoire des templates. Ensuite, créez un nouveau fichier nommé index.html et utilisez rmate pour l'éditer :

> _cd templates_

> _touch index.html_

> _rmate index.html_

![Image](https://cdn-media-1.freecodecamp.org/images/C7xLB4tDdW3twueajM9Elzh5LxD169l6DAuw)

Écrivez un peu de code HTML de base pour la page d'accueil à l'intérieur de index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/nLyBtnwKxFGqhx9d52DxFMj6mBE2u9gq-qXP)
_Code HTML pour la page d'accueil_

Apportons les modifications suivantes dans app.py pour utiliser le fichier index.html. Le code ci-dessous recherchera un fichier nommé index.html dans le répertoire des templates par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/lfuYCPtema6YCe4t1y7pCj8yxOZXPYGtzx8I)
_Utiliser le nouveau fichier index.html et le rendre avec app.py_

Revenez au répertoire du projet et exécutez à nouveau le site web.

![Image](https://cdn-media-1.freecodecamp.org/images/xnv7ptoeZLKzqOmUNfLBhZPgubKooaWj-D3-)

Retournez à la page d'accueil et vous devriez voir le contenu que vous avez mis à l'intérieur de index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/Lh1CRnj7mtlxmzyDPFjALEBRYAC0CvzcwyDn)

Maintenant, ajoutez un peu de style en créant 'main.css' à l'intérieur du répertoire static. Comme toujours, utilisez la commande 'cd' pour changer de répertoire, la commande 'touch' pour créer un nouveau fichier, et la commande 'rmate' pour éditer le même fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/SNa8U2sOoIrMN6tuAsBmtbHFUX43Vfgfc05J)
_Créer le fichier css_

Ajoutez un peu de style à la balise h4. Notez que nous avons actuellement 1 balise h4 dans index.html que le css est censé modifier.

![Image](https://cdn-media-1.freecodecamp.org/images/MUCDIINplzZwjSTrm-1fBkev15z0q7Juku3n)
_Un peu de code css_

Comme toujours, testez vos modifications en utilisant la commande suivante :

> _python3 app.py_

![Image](https://cdn-media-1.freecodecamp.org/images/zY2hMd8vwNjCYVsVs-DyfY7rkBOur3IC66DS)

Remarquez comment le texte à l'intérieur de la balise h4 est coloré selon le CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/VElytx48rZcyMNhmx3xUt6pf4PVjM3RZrmct)

### Étape 9. Tirer parti de Jinja

[Jinja](http://jinja.pocoo.org/) est un moteur de template basé sur Python qui ajoute de nombreuses fonctionnalités puissantes aux pages web. Bien que ce tutoriel ne soit pas axé sur l'apprentissage de Jinja, regardons simplement un exemple simple de l'utilité de Jinja.

Créons simplement une liste de fruits dans app.py et passons-la comme paramètre à index.html. Nous ferons ensuite en sorte que index.html affiche cette liste sur la page web. Apportons les modifications suivantes dans app.py et index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/Klh2Cgj-O8v8H4fYR8Jv00o-QiemELP-iH9t)
_Passer my_list comme paramètre à index.html_

![Image](https://cdn-media-1.freecodecamp.org/images/k3KZzf3MzBJCxvljXa0RoQKYzRPfc5kGl8JR)
_Afficher my_list sur la page web_

Actualisez votre page web et vous devriez voir la liste des fruits à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/o8hYHuUKS47d9bESOKFOhiUs1FR8JTKuL3MY)

Cela montre à quel point Jinja peut être puissant et utile. Pour plus d'informations sur Jinja, veuillez vous référer à [ceci](http://jinja.pocoo.org/).

### Étape 10. Prochaines étapes

Maintenant que vous avez un serveur de développement Python entièrement fonctionnel, les possibilités à venir sont pratiquement infinies. Voici quelques prochaines étapes utiles que vous pourriez envisager pour votre projet :

1. Actuellement, le Pi est accessible uniquement via les appareils de votre réseau personnel. Pour exposer le Pi au monde extérieur (y accéder via n'importe quel appareil en dehors de votre réseau personnel), vous avez besoin de ce qu'on appelle le transfert de port. Basiquement, vous avez besoin d'un nom de domaine et d'une adresse IP statique qui est définitivement assignée au Pi. Plus d'informations [ici](https://www.raspberrypi.org/documentation/remote-access/access-over-Internet/README.md) et [ici](https://maker.pro/raspberry-pi/projects/raspberry-pi-web-server).
2. La plupart des applications nécessiteront une base de données pour les opérations CRUD de base. Python supporte SQlite dès la sortie de la boîte. Apprenez à utiliser SQlite avec Flask [ici](http://flask.pocoo.org/docs/1.0/patterns/sqlite3/) et [ici](https://www.tutorialspoint.com/flask/flask_sqlite.htm).
3. [Voici un kit de démarrage Raspberry Pi cool sur Amazon](https://www.amazon.com/CanaKit-Raspberry-Starter-Premium-Black/dp/B07BCC8PK7/ref=sr_1_1_sspa?ie=UTF8&qid=1536006349&sr=8-1-spons&keywords=raspberry+pi+canakit&psc=1). Le truc sympa avec ce kit est qu'il contient tout ce dont vous avez besoin pour commencer et vous évite l'effort de rechercher des articles individuels vous-même.
4. Puisque vous n'utilisez pas d'écran, il est important que vous utilisiez la commande d'arrêt pour le Pi en utilisant le terminal. Cela garantit que le Pi et la carte SD ne sont pas endommagés :

> _sudo shutdown -h now_

#Jusqu'à la prochaine fois.