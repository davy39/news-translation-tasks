---
title: Comment déployer une application Node.js – De la configuration du serveur à
  la production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-01T21:39:43.000Z'
originalURL: https://freecodecamp.org/news/deploy-nodejs-app-server-to-production
coverImage: https://cdn-media-2.freecodecamp.org/w1280/603a54d9a675540a22924662.jpg
tags:
- name: deployment
  slug: deployment
- name: nginx
  slug: nginx
- name: node
  slug: node
- name: servers
  slug: servers
seo_title: Comment déployer une application Node.js – De la configuration du serveur
  à la production
seo_desc: 'By Yiğit Kemal Erinç

  In this tutorial, we are going to learn everything we need to know before deploying
  a Node app to a production server.

  We will start by renting a server on Digital Ocean. Then we''ll configure this server,
  connect to it, install N...'
---

Par Yiğit Kemal Erinç

Dans ce tutoriel, nous allons apprendre tout ce que nous devons savoir avant de déployer une application Node sur un serveur de production.

Nous commencerons par louer un serveur sur Digital Ocean. Ensuite, nous configurerons ce serveur, nous y connecterons, installerons Nginx et le configurerons, récupérerons ou créerons notre application Node, et l'exécuterons en tant que processus.

Comme vous pouvez le voir, il y a beaucoup à faire et ce sera un tutoriel riche en actions. Alors commençons sans perdre de temps.

Vous devez avoir quelques connaissances de base sur le fonctionnement du Terminal et sur la façon de travailler dans Vi/Vim avant de commencer. Si vous n'êtes pas familier avec les commandes de base, je vous conseille de vous renseigner un peu à leur sujet.

J'exécuterai les commandes dans MacOS. Si vous souhaitez suivre ce tutoriel sous Windows, vous pouvez utiliser Powershell ou un autre émulateur Unix de votre choix.

Bien que j'utiliserai Node.js comme plateforme de notre application exemple, la plupart des étapes sont les mêmes pour toute application web.

## Pourquoi Digital Ocean ?

J'ai choisi Digital Ocean parce que c'est bon marché et que l'interface est vraiment facile à utiliser, comparée à des services comme AWS. De plus, un crédit de 100 $ est inclus dans le pack étudiant GitHub, vous n'avez donc rien à payer pendant quelques mois. C'est idéal pour déployer un projet de cours ou un projet hobby.

Il a un concept appelé Droplets, qui est essentiellement votre part d'un serveur. Vous pouvez penser au serveur comme à un appartement dans lequel vous possédez ou louez un appartement.

Les Droplets fonctionnent à l'aide de machines virtuelles qui s'exécutent sur le serveur. Ainsi, un Droplet est votre machine virtuelle sur un serveur partagé. Comme il s'agit d'une VM, sa part de CPU et de mémoire peut être facilement augmentée, généralement en donnant plus d'argent à votre fournisseur.

## Comment créer un projet Digital Ocean

![Cette image a un attribut alt vide ; son nom de fichier est image-3.png](https://erinc.io/wp-content/uploads/2021/02/image-3.png)

Je suppose que vous vous êtes déjà inscrit et connecté à Digital Ocean avant de continuer. Nous devons d'abord créer un projet qui contiendra nos droplets. Cliquons sur le bouton nouveau projet dans le menu de gauche. Il vous demandera de nommer votre projet.

![Cette image a un attribut alt vide ; son nom de fichier est Screen-Shot-2021-02-22-at-13.35.06.png](https://erinc.io/wp-content/uploads/2021/02/Screen-Shot-2021-02-22-at-13.35.06.png)

Entrez le nom que vous souhaitez. Il vous demandera également si vous souhaitez déplacer des ressources, mais pour l'instant, cliquez simplement sur Skip – nous créerons le droplet plus tard.

## Comment créer un Droplet sur Digital Ocean

Créons notre droplet en cliquant sur le bouton Get Started.

![Cette image a un attribut alt vide ; son nom de fichier est image-4-1024x593.png](https://erinc.io/wp-content/uploads/2021/02/image-4-1024x593.png)

Après avoir cliqué sur le bouton, il nous demandera de choisir une image de VM.

![Cette image a un attribut alt vide ; son nom de fichier est Screen-Shot-2021-02-22-at-13.12.43-1024x567.png](https://erinc.io/wp-content/uploads/2021/02/Screen-Shot-2021-02-22-at-13.12.43-1024x567.png)
_Choix d'une image_

Sur cette page, je sélectionnerai Ubuntu 20.04 car c'est la dernière version LTS au moment où j'écris cet article. LTS signifie "Long Term Support". Il est préférable d'opter pour la version LTS pour les projets réels, car le fournisseur garantit qu'elle sera supportée et maintenue pendant longtemps. Cela signifie que vous n'aurez pas de problèmes à long terme.

J'ai choisi Ubuntu et je vous le recommande car c'est la distribution Linux la plus couramment utilisée. Cela signifie qu'il est également plus facile de trouver des réponses à vos futures questions.

Vous pouvez également choisir d'avoir un CPU dédié si vous en avez besoin. Si vous créez votre propre startup ou un projet commercial, je vous recommande de lire cet [article](https://www.digitalocean.com/docs/droplets/resources/choose-plan/) qui contient des instructions détaillées sur la façon de choisir la bonne option pour vous.

Je vais opter pour l'option la moins chère dans ce cas.

Ensuite, vous devrez sélectionner une région de centre de données. Vous devriez choisir celle qui est la plus proche de vous pour minimiser le délai de réseau.

![Cette image a un attribut alt vide ; son nom de fichier est image-2-1024x519.png](https://erinc.io/wp-content/uploads/2021/02/image-2-1024x519.png)
_Sélection d'un centre de données_

Ensuite, sélectionnons les clés SSH comme méthode d'authentification, car c'est beaucoup plus sécurisé que l'authentification par mot de passe de base.

![Cette image a un attribut alt vide ; son nom de fichier est image-5-1024x459.png](https://erinc.io/wp-content/uploads/2021/02/image-5-1024x459.png)
_Méthode d'authentification_

Pour se connecter au serveur, nous devons générer une nouvelle clé SSH sur notre propre appareil et l'ajouter à Digital Ocean.

## Comment générer une clé SSH

Je vais générer la clé sur mon appareil macOS. Si vous utilisez Windows, vous pouvez vous référer à [cet article](https://phoenixnap.com/kb/generate-ssh-key-windows-10). Ouvrez votre terminal et déplacez-vous dans le dossier ssh :

```
cd ~/.ssh
```

Ensuite, créez votre clé SSH :

```
ssh-keygen
```

Si votre ordinateur dit qu'il ne connaît pas cette commande, vous devez l'installer via brew.

![Cette image a un attribut alt vide ; son nom de fichier est image-7-1024x140.png](https://erinc.io/wp-content/uploads/2021/02/image-7-1024x140.png)

Il vous demandera de nommer le fichier et d'entrer une phrase de passe. Ne saisissez pas de nom, appuyez simplement sur entrée et acceptez les valeurs par défaut. Vous devriez avoir ces fichiers générés. J'ai nommé le mien digital-ocean-ssh dans cette capture d'écran, alors ne vous laissez pas tromper par cela.

```
➜ ls
id_dsa      id_rsa      known_hosts
```

Notre clé publique est `id_dsa` et `id_rsa` est notre clé privée. Si vous oubliez laquelle est privée, vous pouvez toujours imprimer l'une d'elles pour voir.

## Comment ajouter votre clé SSH à Digital Ocean

Maintenant, nous voulons copier notre clé publique et la télécharger sur Digital Ocean afin qu'ils sachent quelle clé utiliser pour l'authentification.

![Cette image a un attribut alt vide ; son nom de fichier est image-9-1024x149.png](https://erinc.io/wp-content/uploads/2021/02/image-9-1024x149.png)

Copiez cette clé entière y compris la partie ssh-rsa.

Cliquez sur "New SSH Key" :

![Cette image a un attribut alt vide ; son nom de fichier est image-10.png](https://erinc.io/wp-content/uploads/2021/02/image-10.png)

Collez la clé dans la zone de texte qui apparaît après avoir cliqué sur le bouton et vous devriez voir votre clé SSH.

![Cette image a un attribut alt vide ; son nom de fichier est image-11.png](https://erinc.io/wp-content/uploads/2021/02/image-11.png)

## Comment se connecter au serveur

Nous utiliserons le terminal pour nous connecter à notre serveur avec SSH. Vous pouvez également jeter un œil à Termius pour une interface agréable si vous le souhaitez.

Exécutez cette commande dans votre terminal après avoir remplacé IP_ADDRESS par l'adresse IP de votre serveur (vous pouvez la trouver dans le panneau de Digital Ocean).

```
ssh root@IP_ADDRESS
```

Si tout se passe bien, vous devriez maintenant être dans le terminal du serveur. Nous nous sommes connectés avec succès au serveur. Si une erreur se produit, vous pouvez la déboguer en exécutant la commande avec l'option "-v" ou "-vv" pour plus de verbosité.

## Comment configurer le serveur

Nous devons effectuer une configuration initiale avant de déployer l'application Node sur le serveur.

### Mettre à jour et améliorer les logiciels

Nous voulons mettre à jour les logiciels du serveur pour nous assurer que nous utilisons les dernières versions.

De nombreux serveurs sont vulnérables aux attaques car ils utilisent des versions plus anciennes de logiciels avec des vulnérabilités connues. Les attaquants peuvent rechercher les vulnérabilités dans ces logiciels et essayer de les exploiter afin d'obtenir un accès à votre serveur.

Vous pouvez mettre à jour les logiciels d'Ubuntu en utilisant la commande **"apt update"**.

```
apt update
Hit:1 https://repos.insights.digitalocean.com/apt/do-agent main InRelease
Get:2 http://mirrors.digitalocean.com/ubuntu focal InRelease [265 kB]
      Hit:3 http://mirrors.digitalocean.com/ubuntu focal-updates InRelease
                Get:4 http://security.ubuntu.com/ubuntu focal-security InRelease [109 kB]
Hit:5 http://mirrors.digitalocean.com/ubuntu focal-backports InRelease
Fetched 374 kB in 1s (662 kB/s)
                          Reading package lists... Done
Building dependency tree       Reading state information... Done
96 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

Si vous lisez le message, il indique que "96 packages can be upgraded". Nous avons installé les nouveaux paquets logiciels mais nous n'avons pas encore mis à niveau nos logiciels vers ces versions.

Pour cela, exécutons une autre commande :

```
apt upgrade
```

Tapez y lorsqu'il vous le demande et il mettra à niveau les logiciels.

### Créer un utilisateur

Nous nous sommes connectés au serveur en tant qu'utilisateur root (l'utilisateur avec les privilèges les plus élevés). Être root est dangereux et peut nous exposer à des vulnérabilités.

Par conséquent, nous devons créer un nouvel utilisateur et ne pas exécuter de commandes en tant que root. Remplacez `$username` par un nom d'utilisateur de votre choix.

```
whoami
root
```

```
adduser $username
```

Vous devez entrer un mot de passe pour l'utilisateur. Après cela, il vous posera une série de questions, alors tapez simplement y jusqu'à ce que l'invite soit terminée.

Le nouvel utilisateur a été créé, mais nous devons également ajouter cet nouvel utilisateur au groupe "sudo" afin que nous puissions effectuer toute action nécessaire.

```
usermod -aG sudo $USERNAME
```

Nous ajoutons le groupe avec l'option `-aG` (add group), et nous ajoutons le nom de groupe `sudo` à notre nom d'utilisateur.

Nous sommes toujours root, alors changeons notre utilisateur pour le nouvel utilisateur créé, en utilisant la commande `su` (switch user).

```
su $USERNAME
```

Après cette étape, si vous exécutez la commande **`whoami`**, vous devriez voir votre nom d'utilisateur. Vous pouvez confirmer l'existence du groupe sudo en exécutant cette commande :

```
sudo cat /var/log/auth.log
```

Seuls les superutilisateurs peuvent voir ce fichier et le système d'exploitation demandera votre mot de passe utilisateur après avoir exécuté cette commande.

### Copier la clé SSH

Nous avons créé l'utilisateur avec succès, mais nous n'avons pas encore activé la connexion SSH pour cet nouvel utilisateur.

Par conséquent, nous devons copier la clé publique que nous avons précédemment créée sur notre ordinateur local et la coller dans le dossier SSH de cet utilisateur afin que SSH sache quelle clé utiliser pour authentifier notre nouvel utilisateur.

```
mkdir -p ~/.ssh
```

L'argument `-p` crée le répertoire s'il n'existe pas.

```
vi ~/.ssh/authorized_keys
```

Nous allons utiliser vi ou vim pour créer un fichier et l'appeler **`authorized_keys`**.

Copiez votre clé publique (fichier `id_dsa`), puis appuyez sur "i" pour passer en mode insertion. Ensuite, collez-la simplement dans ce fichier avec CMD + V.

Appuyez sur esc pour quitter le mode insertion, tapez **:wq** pour sauvegarder et quitter.

Si vous avez des problèmes avec l'utilisation de Vim-Vi, vous pouvez consulter [l'un des nombreux tutoriels](https://www.freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae/) qui expliquent comment l'utiliser.

### Se connecter au serveur en tant que nouvel utilisateur

Maintenant, nous devrions pouvoir nous connecter au serveur sans aucun problème en utilisant ssh. Vous pouvez utiliser cette commande pour vous connecter, n'oubliez pas d'insérer votre nom d'utilisateur et `IP_ADDRESS`.

```
ssh $USERNAME@IP_ADDRESS
```

Si vous avez des problèmes à ce stade, vous devriez simplement supprimer le droplet et recommencer. Cela ne prend pas beaucoup de temps de recommencer, mais le débogage des problèmes de serveur peut être difficile.

### Comment désactiver la connexion Root

Il est bon de désactiver la connexion Root comme mesure de sécurité, alors faisons cela maintenant.

Il peut être utile de changer les permissions du fichier au cas où afin que nous ne rencontrions pas de problèmes de permissions à l'avenir.

```
chmod 644 ~/.ssh/authorized_keys
```

Ouvrons maintenant notre fichier `sshd_config` :

```
sudo vi /etc/ssh/sshd_config
```

Trouvez cette ligne et changez le yes en no de la même manière que nous l'avons fait précédemment avec vi.

```
PermitRootLogin no
```

Sauvegardez et quittez vi.

## Comment installer Node.js et Git

Nous pouvons maintenant installer Node.js et Git :

```
sudo apt install nodejs npm
```

```
sudo apt install git
```

Nous sommes maintenant prêts à créer une application Node et à l'exécuter. Vous pouvez soit récupérer votre projet Node depuis Github, soit créer une application Node ici juste pour tester si cela fonctionne.

Déplacez-vous dans un répertoire de votre choix et créez un fichier **"app.js"** :

```
sudo vi app.js
```

Vous pouvez coller le code suivant dans votre fichier **app.js** :

```
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
        res.send('Hello World');
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
```

Maintenant, nous pouvons l'exécuter avec la commande :

```
node app.js
```

Vous devriez voir "Example app listening on port 3000!" sur votre terminal.

Nous pouvons confirmer que cela fonctionne en envoyant une requête à notre serveur :

```
GET http://IP_ADDRESS:3000/
```

Envoyez cette requête soit à partir d'un client HTTP comme Postman, soit depuis votre navigateur, et vous devriez voir le message "Hello World".

À ce stade, vous devriez remarquer que quelque chose ne va pas : les utilisateurs réguliers ne savent pas comment envoyer des requêtes au port 3000.

Nous devons rediriger les requêtes qui arrivent à notre serveur web depuis notre IP vers le port 3000. Nous pouvons accomplir cela avec l'aide de Nginx.

![Cette image a un attribut alt vide ; son nom de fichier est image-16.png](https://erinc.io/wp-content/uploads/2021/02/image-16.png)

## Comment installer et configurer Nginx

Nous allons utiliser Nginx comme Reverse Proxy pour rediriger les requêtes vers notre application Node.

![Cette image a un attribut alt vide ; son nom de fichier est image-14-1024x531.png](https://erinc.io/wp-content/uploads/2021/02/image-14-1024x531.png)
_Nginx comme Reverse Proxy_

Installons Nginx :

```
sudo apt install nginx
```

Démarrez le service Nginx :

```
sudo service nginx start
```

Nous pouvons tester pour voir si cela fonctionne en envoyant une requête à l'adresse IP de notre serveur depuis le navigateur. Tapez l'adresse IP de votre serveur dans votre navigateur et vous devriez voir ceci :

![Cette image a un attribut alt vide ; son nom de fichier est image-15-1024x231.png](https://erinc.io/wp-content/uploads/2021/02/image-15-1024x231.png)

Il est important de savoir que Nginx sert depuis **"/var/www/html"** par défaut et vous pouvez trouver ce fichier HTML dans ce répertoire également.

Je vous conseille également de créer un dossier sous "/var/www", appelez-le app, et déplacez votre application Node dans ce dossier afin qu'elle soit facile à trouver.

### Comment configurer le Reverse Proxy Nginx

Nous allons modifier le fichier de configuration Nginx pour configurer un reverse proxy :

```
sudo vi /etc/nginx/sites-available/default
```

Dans ce fichier, vous devez trouver le bloc location / et le modifier comme suit :

```
location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                proxy_pass http://127.0.0.1:3000/;
        }
```

La directive `proxy_pass` redirige la requête vers un port spécifié. Nous donnons le port sur lequel notre application Node s'exécute.

Redémarrons Nginx pour que les modifications prennent effet :

```
sudo service nginx reload
```

Après cette étape, nous devrions pouvoir voir le message lorsque nous envoyons une requête à notre serveur. Félicitations, nous avons terminé le nombre minimum d'étapes pour déployer une application Node !

![Cette image a un attribut alt vide ; son nom de fichier est Screen-Shot-2021-02-24-at-01.10.33-1024x67.png](https://erinc.io/wp-content/uploads/2021/02/Screen-Shot-2021-02-24-at-01.10.33-1024x67.png)

Mais je vous conseille également de compléter l'étape bonus suivante, car je pense qu'elle est assez importante.

Si vous ne voyez pas le message hello world, vous pouvez vérifier si votre application et Nginx sont en cours d'exécution et les redémarrer.

## Comment exécuter votre application en tant que processus

Nous ne voulons pas démarrer notre application manuellement chaque fois que quelque chose ne va pas et que notre application plante. Nous voulons qu'elle redémarre toute seule. De plus, chaque fois que le serveur démarre, notre application doit également démarrer.

Pour que cela se produise, nous pouvons utiliser PM2. Installons PM2 et configurons-le.

```
sudo npm i -g pm2
```

Nous installons pm2 globalement en utilisant l'option "-g" afin qu'il soit accessible depuis chaque dossier.

```
pm2 start app.js
```

Cela garantit que l'application redémarrera si elle se termine en raison d'une erreur.

Sauvegardons la liste des processus actuels.

```
pm2 save
```

Nous devons également la convertir en un démon qui s'exécute chaque fois que le système démarre :

```
pm2 startup systemd
```

![Cette image a un attribut alt vide ; son nom de fichier est image-17.png](https://erinc.io/wp-content/uploads/2021/02/image-17.png)

Pour rappel, dans ce tutoriel, j'utilise les commandes pour Ubuntu. Si vous utilisez une autre distribution Linux, vous devez remplacer `systemd` dans cette commande.

Nous pouvons confirmer que le service est redémarré en redémarrant le serveur et en envoyant une requête sans exécuter app.js manuellement :

```
sudo reboot
```

Après avoir envoyé une requête comme nous l'avons fait précédemment, vous devriez pouvoir voir le message hello world.

## Conclusion

Dans ce tutoriel, nous avons commencé de zéro, loué un serveur pour nous-mêmes, nous y sommes connectés et l'avons configuré de manière à ce qu'il serve notre application Node.js depuis le port 80.

Si vous avez suivi et que vous avez pu compléter toutes les étapes, félicitations ! Vous pouvez être fier de vous, car ce n'était pas le sujet le plus facile :). J'espère que vous avez beaucoup appris. Merci pour votre temps.

Je prévois d'explorer ce sujet plus en profondeur en connectant le serveur à un nom de domaine, puis en le connectant à CircleCI pour l'intégration continue. Je passerai également en revue les étapes nécessaires pour rendre votre application Node.js/React prête pour la production. Cet article était déjà assez long, donc ces sujets sont réservés pour un autre article :)

Si vous avez aimé la lecture et que vous souhaitez être informé de mes futurs articles, vous pouvez vous abonner à mon [blog personnel](https://erinc.io/). Vous pouvez y voir mes articles précédents si vous êtes intéressé à lire davantage. J'écris généralement sur des sujets liés au développement web.