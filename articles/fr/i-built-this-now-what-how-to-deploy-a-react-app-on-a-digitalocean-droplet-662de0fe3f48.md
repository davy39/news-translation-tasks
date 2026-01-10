---
title: Je l'ai construit - Et maintenant ? Comment déployer une application React
  sur un Droplet DigitalOcean.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-01T09:28:12.000Z'
originalURL: https://freecodecamp.org/news/i-built-this-now-what-how-to-deploy-a-react-app-on-a-digitalocean-droplet-662de0fe3f48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6K5vmzalJUxn44v3cm6wBw.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Je l'ai construit - Et maintenant ? Comment déployer une application React
  sur un Droplet DigitalOcean.
seo_desc: 'By Andrea Stringham

  Most aspiring developers have uploaded static HTML sites before. The process isn’t
  too daunting, as you’re essentially just moving files from one computer to another,
  and then BAM! Website.

  But those who have tackled learning Reac...'
---

Par Andrea Stringham

La plupart des développeurs en herbe ont téléchargé des sites HTML statiques auparavant. Le processus n'est pas trop intimidant, car vous déplacez essentiellement des fichiers d'un ordinateur à un autre, et puis BAM ! Site web.

Mais ceux qui ont relevé le défi d'apprendre React y consacrent souvent des centaines, voire des milliers d'heures pour comprendre les composants, les props et l'état, pour se retrouver avec la question « Comment puis-je héberger cela ? » Ne craignez rien, cher développeur. Déployer votre dernier chef-d'œuvre est un peu plus approfondi, mais pas excessivement difficile. Voici comment faire :

### Préparation pour la production

Il y a quelques choses que vous voudrez faire pour préparer votre application au déploiement.

#### Désactiver les service workers

Si vous avez utilisé quelque chose comme create-react-app pour démarrer votre projet, vous voudrez désactiver le service worker intégré si vous ne l'avez pas spécifiquement intégré pour qu'il fonctionne avec votre application. Bien qu'il soit généralement inoffensif, il peut causer quelques problèmes, il est donc préférable de s'en débarrasser dès le départ. Trouvez ces lignes dans votre fichier `src/index.js` et supprimez-les : `registerServiceWorker();` `import registerServiceWorker from 'register-service-worker'`

#### Préparez votre serveur

Pour obtenir le meilleur rapport qualité-prix, une version de production minimisera le code et supprimera les espaces blancs et les commentaires supplémentaires afin qu'il soit aussi rapide à télécharger que possible. Elle crée un nouveau répertoire appelé `/build`, et nous devons nous assurer que nous disons à Express de l'utiliser. Sur votre page serveur, ajoutez cette ligne : `app.use( express.static( `${__dirname}/../build` ) );`

Ensuite, vous devrez vous assurer que vos routes savent comment accéder à votre fichier index.html. Pour ce faire, nous devons créer un point de terminaison et le placer en dessous de tous les autres points de terminaison dans votre fichier serveur. Cela devrait ressembler à ceci :

```
const path = require('path')app.get('*', (req, res)=>{  res.sendFile(path.join(__dirname, '../build/index.html'));})
```

#### Créer la version de production

Maintenant qu'Express sait utiliser le répertoire `/build`, il est temps de le créer. Ouvrez votre terminal, assurez-vous d'être dans votre répertoire de projet, et utilisez la commande `npm run build`

#### Gardez vos secrets en sécurité

Si vous utilisez des clés API ou une chaîne de connexion de base de données, espérons que vous les avez déjà cachées dans un fichier `.env`. Toutes les configurations qui diffèrent entre le déploiement et le local doivent également aller dans ce fichier. Les balises ne peuvent pas être proxifiées, nous devons donc coder en dur l'adresse backend lors de l'utilisation du serveur de développement React, mais nous voulons utiliser des chemins relatifs en production. Votre fichier `.env` résultant pourrait ressembler à ceci :

```
REACT_APP_LOGIN="http://localhost:3030/api/auth/login"REACT_APP_LOGOUT="http://localhost:3030/api/auth/logout"DOMAIN="user4234.auth0.com"ID="46NxlCzM0XDE7T2upOn2jlgvoS"SECRET="0xbTbFK2y3DIMp2TdOgK1MKQ2vH2WRg2rv6jVrMhSX0T39e5_Kd4lmsFz"SUCCESS_REDIRECT="http://localhost:3030/"FAILURE_REDIRECT="http://localhost:3030/api/auth/login"
```

```
AWS_ACCESS_KEY_ID=AKSFDI4KL343K55L3AWS_SECRET_ACCESS_KEY=EkjfDzVrG1cw6QFDK4kjKFUa2yEDmPOVzN553kAANcy
```

```
CONNECTION_STRING="postgres://vuigx:k8Io13cePdUorndJAB2ijk_u0r4@stampy.db.elephantsql.com:5432/vuigx"NODE_ENV=development
```

#### Poussez votre code

Testez votre application localement en allant sur `[http://localhost:3030](http://localhost:3030)` et en remplaçant 3030 par le port de votre serveur pour vous assurer que tout fonctionne toujours correctement. N'oubliez pas de démarrer votre serveur local avec node ou nodemon pour qu'il soit opérationnel lorsque vous le vérifiez. Une fois que tout semble bon, nous pouvons le pousser vers Github (ou Bit Bucket, etc).

**IMPORTANT !** Avant de le faire, vérifiez que votre fichier `.gitignore` contient `.env` et `/build` pour ne pas publier d'informations sensibles ou de fichiers inutiles.

### Configuration de DigitalOcean

[DigitalOcean](https://www.digitalocean.com/) est une plateforme d'hébergement de premier plan, et rend le déploiement de sites React relativement facile et économique. Ils utilisent des Droplets, qui est le terme qu'ils utilisent pour leurs serveurs. Avant de créer notre Droplet, nous avons encore un peu de travail à faire.

#### Création de clés SSH

Les serveurs sont des ordinateurs qui ont des adresses IP publiques. Pour cette raison, nous avons besoin d'un moyen de dire au serveur qui nous sommes, afin que nous puissions faire des choses que nous ne voudrions pas que quelqu'un d'autre fasse, comme apporter des modifications à nos fichiers. Votre mot de passe quotidien ne sera pas assez sécurisé, et un mot de passe assez long et complexe pour protéger votre Droplet serait presque impossible à retenir. Au lieu de cela, nous utiliserons une clé SSH.

![Image](https://cdn-media-1.freecodecamp.org/images/j4ZwaQlN-vlDVs20wxu3Xxq9QccGKA-gLdLp)
_Photo par [Brenda Clarke](https://www.flickr.com/photos/37753256@N08/" rel="noopener" target="_blank" title=")_

Pour créer votre clé SSH, entrez cette commande dans votre terminal : `ssh-keygen -t rsa`

Cela commence le processus de génération de la clé SSH. Tout d'abord, on vous demandera de spécifier où sauvegarder la nouvelle clé. Sauf si vous avez déjà une clé que vous devez conserver, vous pouvez garder l'emplacement par défaut et simplement appuyer sur Entrée pour continuer.

En tant que couche de sécurité supplémentaire au cas où quelqu'un mettrait la main sur votre ordinateur, vous devrez entrer un mot de passe pour sécuriser votre clé. Votre terminal n'affichera pas vos frappes lorsque vous tapez ce mot de passe, mais il en tient compte. Une fois que vous avez appuyé sur Entrée, vous devrez le taper une fois de plus pour confirmer. Si tout se passe bien, vous devriez maintenant voir quelque chose comme ceci :

```
Generating public/private rsa key pair.Enter file in which to save the key (/Users/username/.ssh/id_rsa):Enter passphrase (empty for no passphrase):Enter same passphrase again:Your identification has been saved in demo_rsa.Your public key has been saved in demo_rsa.pub.The key fingerprint is:cc:28:30:44:01:41:98:cf:ae:b6:65:2a:f2:32:57:b5 user@user.localThe key's randomart image is:+--[ RSA 2048]----+|=*+.             ||o.               || oo              ||  oo  .+         || .  ....S        ||  . ..E          || . +             ||*.=              ||+Bo              |+-----------------+
```

#### Que s'est-il passé ?

Deux fichiers ont été créés sur votre ordinateur — `id_rsa` et `id_rsa.pub`. Le fichier `id_rsa` est votre clé privée et est utilisé pour vérifier votre signature lorsque vous utilisez le fichier `id_rsa.pub`, ou clé publique. Nous devons donner notre clé publique à DigitalOcean. Pour l'obtenir, entrez `cat ~/.ssh/id_rsa.pub`. Vous devriez maintenant voir une longue chaîne de caractères, qui est le contenu de votre fichier `id_rsa.pub`. Cela ressemble à ceci :

```
ssh-rsaAABC3NzaC1yc2EAAAADAQABAAABAQDR5ehyadT9unUcxftJOitl5yOXgSi2Wj/s6ZBudUS5Cex56LrndfP5Uxb8+Qpx1D7gYNFacTIcrNDFjdmsjdDEIcz0WTV+mvMRU1G9kKQC01YeMDlwYCopuENaas5+cZ7DP/qiqqTt5QDuxFgJRTNEDGEebjyr9wYk+mveV/acBjgaUCI4sahij98BAGQPvNS1xvZcLlhYssJSZrSoRyWOHZ/hXkLtq9CvTaqkpaIeqvvmNxQNtzKu7ZwaYWLydEKCKTAe4ndObEfXexQHOOKwwDSyesjaNc6modkZZC+anGLlfwml4IUwGv10nogVg9DTNQQLSPVmnEN3Z User@Computer.local
```

Maintenant, voilà un mot de passe ! Copiez la chaîne manuellement, ou utilisez la commande `pbcopy < ~/.ssh/id_rsa.pub` pour que le terminal la copie pour vous.

#### Ajout de votre clé SSH à DigitalOcean

Connectez-vous à votre compte DigitalOcean ou inscrivez-vous si vous ne l'avez pas encore fait. Allez dans vos [Paramètres de sécurité](https://cloud.digitalocean.com/settings/security) et cliquez sur Ajouter SSH. Collez la clé que vous avez copiée et donnez-lui un nom. Vous pouvez la nommer comme vous le souhaitez, mais il est bon de faire référence à l'ordinateur sur lequel la clé est enregistrée, surtout si vous utilisez plusieurs ordinateurs régulièrement.

#### Création d'un Droplet

![Image](https://cdn-media-1.freecodecamp.org/images/XhAxSEJtF-5YqybAqqiqlvHcgjl1nhU11ybt)
_Photo par [M. Maddo](https://www.flickr.com/photos/14141796@N05/" rel="noopener" target="_blank" title=")_

Avec la clé en place, nous pouvons enfin créer notre Droplet. Pour commencer, cliquez sur Créer un Droplet. On vous demandera de choisir un système d'exploitation, mais pour nos besoins, l'Ubuntu par défaut fonctionnera très bien.

Vous devrez sélectionner la taille du Droplet que vous souhaitez utiliser. Dans de nombreux cas, le plus petit Droplet suffira. Cependant, passez en revue les options disponibles et choisissez celle qui conviendra le mieux à votre projet.

Ensuite, sélectionnez un centre de données pour votre Droplet. Choisissez un emplacement central par rapport à votre base de visiteurs attendue. Les nouvelles fonctionnalités sont déployées par DigitalOcean dans différents centres de données à différents moments, mais sauf si vous savez que vous souhaitez utiliser une fonctionnalité spéciale qui n'est disponible que dans des emplacements spécifiques, cela n'aura pas d'importance.

Si vous souhaitez ajouter des services supplémentaires à votre Droplet, tels que des sauvegardes ou un réseau privé, vous avez cette option ici. Soyez conscient qu'il y a un coût associé à ces services.

Enfin, assurez-vous que votre clé SSH est sélectionnée et donnez un nom à votre Droplet. Il est possible d'héberger plusieurs projets sur un seul Droplet, vous ne voudrez donc peut-être pas lui donner un nom spécifique au projet. Soumettez vos paramètres en cliquant sur le bouton Créer en bas de la page.

#### Connexion à votre Droplet

Avec notre Droplet créé, nous pouvons maintenant nous y connecter via SSH. Copiez l'adresse IP de votre Droplet et retournez à votre terminal. Entrez ssh suivi de root@votre-adresse-ip, où votre-adresse-ip est l'adresse IP de votre Droplet. Cela devrait ressembler à ceci : `ssh root@123.45.67.8`. Cela indique à votre ordinateur que vous souhaitez vous connecter à votre adresse IP en tant qu'utilisateur root. Alternativement, vous pouvez [configurer des comptes utilisateur](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04) si vous ne souhaitez pas vous connecter en tant que root, mais ce n'est pas nécessaire.

#### Installation de Node

![Image](https://cdn-media-1.freecodecamp.org/images/yuVxVs5VxSTn0vkLxPKclZXDgs60-xuMWuE1)

Pour exécuter React, nous aurons besoin d'une version mise à jour de Node. Tout d'abord, nous voulons exécuter `apt-get update && apt-get dist-upgrade` pour mettre à jour la liste des logiciels Linux. Ensuite, entrez `apt-get install nodejs -y`, `apt-get install npm -y`, et `npm i -g n` pour installer Nodejs et npm.

Les dépendances de votre application React peuvent nécessiter une version spécifique de Node, alors vérifiez la version que votre projet utilise en exécutant `node -v` dans le répertoire de votre projet. Vous voudrez probablement faire cela dans un autre onglet de terminal pour ne pas avoir à vous reconnecter via SSH.

Une fois que vous savez quelle version vous avez besoin, retournez à votre connexion SSH et exécutez `n 6.11.2`, en remplaçant 6.11.2 par votre numéro de version spécifique. Cela garantit que la version de Node de votre Droplet correspond à votre projet et minimise les problèmes potentiels.

### Installez votre application sur le Droplet

Tout le travail préparatoire a été fait, et il est enfin temps d'installer notre application React ! Tout en étant toujours connecté via SSH, assurez-vous d'être dans votre répertoire personnel. Vous pouvez entrer `cd ~` pour vous y rendre si vous n'êtes pas sûr.

Pour obtenir les fichiers sur votre Droplet, vous allez les cloner depuis votre dépôt Github. Récupérez le lien de clonage HTTP depuis Github et dans votre terminal entrez `git clone [https://github.com/username/my-react-project.git](https://github.com/username/my-react-project.git)`. Tout comme avec votre projet local, entrez dans votre dossier de projet en utilisant `cd my-react-project` puis exécutez `npm install`.

#### Ne négligez pas vos fichiers ignorés

Rappelez-vous que nous avons dit à Git d'ignorer le fichier `.env`, donc il ne sera pas inclus dans le code que nous venons de télécharger. Nous devons l'ajouter manuellement maintenant. `touch .env` créera un fichier `.env` vide que nous pourrons ensuite ouvrir dans l'éditeur nano en utilisant `nano .env`. Copiez le contenu de votre fichier `.env` local et collez-le dans l'éditeur nano.

Nous avons également dit à Git d'ignorer le répertoire build. C'est parce que nous testions simplement la version de production, mais maintenant nous allons la reconstruire sur notre Droplet. Utilisez `npm run build` pour exécuter ce processus à nouveau. Si vous obtenez une erreur, vérifiez que vous avez toutes vos dépendances listées dans votre fichier `package.json`. Si certaines sont manquantes, installez ces packages avec npm.

#### Démarrez-le !

Exécutez votre serveur avec `node server/index.js` (ou quel que soit le nom de votre fichier serveur) pour vous assurer que tout fonctionne. Si une erreur est lancée, vérifiez à nouveau les dépendances manquantes qui n'auraient pas été détectées lors du processus de construction. Si tout démarre correctement, vous devriez maintenant pouvoir accéder à adresseip:portduserveur pour voir votre site : `123.45.67.8:3232`. Si votre serveur s'exécute sur le port 80, il s'agit d'un port par défaut et vous pouvez simplement utiliser l'adresse IP sans spécifier de numéro de port : `123.45.67.8`

![Image](https://cdn-media-1.freecodecamp.org/images/Lmb7jLrh1rmpnZFyV0lHZhRpwxCj-4b58LJk)
_Photo par [Unsplash](https://unsplash.com/photos/3To9V42K0Ag?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">John Baker</a> sur <a href="https://unsplash.com/search/photos/key?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Vous avez maintenant un espace sur Internet à vous ! Si vous avez acheté un nom de domaine que vous souhaitez utiliser à la place de l'adresse IP, vous pouvez suivre [les instructions de DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars) pour configurer cela.

#### Gardez-le en fonctionnement

Votre site est en ligne, mais une fois que vous fermez le terminal, votre serveur s'arrêtera. C'est un problème, donc nous voudrons installer un logiciel supplémentaire qui dira au serveur de ne pas s'arrêter une fois la connexion terminée. Il existe quelques options pour cela, mais utilisons Program Manager 2 pour les besoins de cet article.

Arrêtez votre serveur si vous ne l'avez pas déjà fait et exécutez `npm install -g pm2`. Une fois installé, nous pouvons lui dire d'exécuter notre serveur en utilisant `pm2 start server/index.js`

### Mise à jour de votre code

À un moment donné, vous voudrez probablement mettre à jour votre projet, mais heureusement, le téléchargement des modifications est rapide et facile. Une fois que vous avez poussé votre code vers Github, connectez-vous en SSH à votre Droplet et entrez dans le répertoire de votre projet. Comme nous avons cloné depuis Github initialement, nous n'avons pas besoin de fournir de liens cette fois. Vous pouvez télécharger le nouveau code simplement en exécutant `git pull`.

Pour incorporer les modifications du frontend, vous devrez exécuter à nouveau le processus de construction avec `npm run build`. Si vous avez apporté des modifications au fichier serveur, redémarrez PM2 en exécutant `pm2 restart all`. C'est tout ! Vos mises à jour devraient être en ligne maintenant.