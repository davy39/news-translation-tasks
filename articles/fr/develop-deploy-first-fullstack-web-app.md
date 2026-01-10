---
title: Comment développer et déployer votre première application Web Full-Stack en
  utilisant un site statique et Node.js
subtitle: ''
author: Louise Findlay
co_authors: []
series: null
date: '2020-07-29T18:03:27.000Z'
originalURL: https://freecodecamp.org/news/develop-deploy-first-fullstack-web-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Develop-and-Deploy-Node.js-App-FreeCodeCamp-Cover-1.jpg
tags:
- name: coding
  slug: coding
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: Web Applications
  slug: web-applications
- name: Web Development
  slug: web-development
seo_title: Comment développer et déployer votre première application Web Full-Stack
  en utilisant un site statique et Node.js
seo_desc: "This tutorial will show you how to convert a static website that uses HTML,\
  \ CSS and JavaScript (JS) to a dynamic one using MongoDB, Express, Static HTML,\
  \ CSS, JS, and Node.js. \nOur tech stack will be similar to the popular MEAN/MERN\
  \ stack (MongoDB, E..."
---

Ce tutoriel vous montrera comment convertir un site Web statique qui utilise HTML, CSS et JavaScript (JS) en un site dynamique en utilisant MongoDB, Express, HTML statique, CSS, JS et Node.js. 

Notre stack technique sera similaire à la stack MEAN/MERN populaire (MongoDB, Express, Angular ou React, et NodeJS). Mais au lieu d'utiliser Angular ou React, nous utiliserons un moteur de templating appelé [EJS](https://ejs.co) (Embedded JavaScript.) 

D'autres moteurs de templating populaires incluent Handlebars, Pug et Nunjucks. 

Ensuite, nous déployerons notre application Web Node.js sur DigitalOcean et aborderons les noms de domaine, SSL, les proxys inverses et les gestionnaires de processus.

Apprendre un langage de templating peut être plus facile qu'un framework JS. Vous pouvez simplement écrire du HTML, et il vous permet d'insérer le même morceau de code à plusieurs endroits (appelés partials) ou de passer des variables côté serveur à afficher sur le front-end (comme un nom d'utilisateur).

## Table des matières

* [Développer votre première application Web Node.js](#heading-developing-your-first-nodejs-web-app)
    * [Installation de Node.js](#heading-installing-nodejs)
    * [Tester l'installation](#heading-testing-the-install)
    * [Créer votre premier serveur](#heading-creating-your-first-server)
    * [Prochaines étapes](#heading-next-steps)
    * [Bases du templating](#heading-templating-basics)
    * [Passer des données côté serveur au front-end](#heading-passing-server-side-data-to-the-frontend)
* [Déployer votre première application Web Node.js](#heading-deploying-your-first-nodejs-web-app)
    * [Configuration de DigitalOcean](#heading-setting-up-digitalocean)
    * [Connexion à votre Droplet](#heading-connecting-to-your-droplet)
    * [Déployer votre application Web Node.js](#heading-deploying-your-nodejs-web-app)
    * [Configurer votre nom de domaine](#heading-configuring-your-domain-name)
    * [Supprimer le numéro de port de votre URL](#heading-removing-the-port-number-from-your-url)
    * [Exécuter l'application au démarrage (Configuration d'un gestionnaire de processus)](#heading-running-the-app-on-boot-setting-up-a-process-manager)

## Développer votre première application Web Node.js

### Installation de Node.js

Tout d'abord, assurez-vous d'avoir installé Node.js sur votre machine locale ou sur votre fournisseur d'hébergement VPS. Si vous ne l'avez pas installé, rendez-vous sur le [site Web de Node.js](https://nodejs.org/en/) pour le faire. 

Avec Node.js, vous pouvez écrire du code côté serveur en utilisant une forme spéciale de JavaScript afin de pouvoir utiliser un langage déjà familier.

L'installateur de Node.js est livré avec le gestionnaire de paquets NPM. NPM est un dépôt pour les modules Node, des morceaux de code réutilisables qui peuvent étendre la fonctionnalité de votre serveur. C'est similaire à un dépôt de plugins, et les modules Node peuvent être considérés comme des extraits de code ou des bibliothèques (selon leur taille).

*Utilisateurs de Windows :* Doivent ajouter Node et NPM à leur PATH pour pouvoir les appeler facilement sur la ligne de commande. Pour des instructions plus détaillées, voir mon [guide](https://louisefindlay.com/blog/getting-to-grips-with-databases-part1) ici.

### Tester l'installation

Pour tester que l'installation a fonctionné correctement, ouvrez une fenêtre de terminal et tapez `node -v` et `npm -v`. Si le message résultant commence par un v et est suivi de quelques chiffres (indiquant une version), alors l'installation a été réussie. Vous êtes maintenant prêt à créer votre premier serveur.

### Créer votre premier serveur

Une fois que vous avez créé un site Web statique, la première étape pour créer une application Node.js est de créer un serveur Web Express.

Tout d'abord, déplacez tous les fichiers statiques de votre site Web (HTML, CSS, JS, images, etc.) dans un dossier appelé public et créez un fichier appelé server.js dans le répertoire racine de votre dossier de site Web. Dans le fichier server.js, tapez :

```js
// Charger les modules Node
var express = require('express');
// Initialiser Express
var app = express();
// Rendre les fichiers statiques
app.use(express.static('public'));
// Port sur lequel le site Web s'exécutera
app.listen(8080);
```

Ensuite, dans le terminal, tapez : `npm init`. Appuyez sur Entrée pour accepter les paramètres par défaut pour toutes les options suivantes, mais assurez-vous que le point d'entrée est server.js.

Enfin, tapez : `npm start` puis allez à l'adresse IP de votre hôte VPS, ou localhost:8080/index.html (ou le nom de l'une de vos pages Web) dans le navigateur. Le serveur Express que vous venez de créer devrait maintenant servir les fichiers statiques de votre site Web.

### Prochaines étapes

Par la suite, nous discuterons de la manière de convertir vos fichiers statiques en fichiers dynamiques en utilisant le moteur de templating EJS. Ensuite, nous verrons comment copier du code répété en utilisant des partials et injecter des variables côté serveur vers le front-end.

### Bases du templating

#### Installation d'EJS

La première étape pour utiliser EJS est de l'installer. Un simple `npm install ejs --save` fera l'affaire. Le paramètre `--save` sauvegarde le module dans le fichier `package.json`. 

Cela permet à quiconque de cloner le dépôt git (ou de télécharger les fichiers du site) d'installer tous les modules Node requis pour le projet (appelés dépendances) en utilisant la commande `npm install`. Ensuite, ils n'ont pas à taper `npm install (nom du module)` pour chaque module dont ils ont besoin.

#### Conversion des pages statiques en fichiers EJS

Ensuite, vous devez convertir vos fichiers HTML statiques en fichiers EJS dynamiques et configurer votre structure de dossiers de la manière dont EJS l'attend. 

Dans le répertoire racine de votre site Web, créez un dossier appelé views. À l'intérieur de ce dossier, créez deux sous-dossiers appelés pages et partials. Déplacez tous vos fichiers HTML dans le sous-dossier pages et renommez les extensions de fichier .html en .ejs. 

Votre structure de dossiers devrait ressembler à l'image ci-dessous.

![nodejs-file-structure](https://www.freecodecamp.org/news/content/images/2020/07/nodejs-file-structure.png)

#### Réutilisation de code - Création de votre premier EJS Partial

Lors de la création de sites statiques, il y a souvent du code que vous répétez sur chaque page, comme l'en-tête (où se trouvent les balises meta), les sections d'en-tête et de pied de page. 

Il est peu pratique de les changer sur chaque page (surtout sur les sites plus grands) si des modifications sont nécessaires. Mais si vous utilisez des partials EJS, vous n'aurez pas à le faire. Modifier un fichier de template (partial) mettra à jour le code sur chaque page où le fichier est inclus.

Nous prendrons une partie typique d'un site Web à templater, l'en-tête, comme exemple. Créez un nouveau fichier appelé header.ejs dans le dossier partials. Copiez et collez tout le code entre les balises `<header></header>` sur l'une de vos pages EJS dans celui-ci.

Enfin, sur toutes les pages avec un en-tête, supprimez le code entre les balises `<header></header>` (le même code que vous avez copié dans le fichier partial header.ejs) et remplacez-le par `<% include('../partials/header') %>`. Maintenant, vous avez créé votre premier partial EJS. Répétez le processus pour tout autre morceau de code répétitif, comme les sections head et footer.

*Astuce :* Si vous avez du mal à différencier vos pages et vos partials puisqu'ils ont la même extension de fichier .ejs, il peut être utile de mettre un underscore _ devant les noms des partials (donc _header.ejs). C'est une convention de nommage que certains développeurs utilisent et qui peut être utile.

#### Rendu des pages EJS

Maintenant, nous arrivons à la partie excitante : faire en sorte que le serveur rende les pages et partials EJS pour que vous puissiez les voir sur le front-end.

**Exemple de server.js**
```js
// Charger les modules Node
var express = require('express');
const ejs = require('ejs');
// Initialiser Express
var app = express();
// Rendre les fichiers statiques
app.use(express.static('public'));
// Définir le moteur de vue sur ejs
app.set('view engine', 'ejs');
// Port sur lequel le site Web s'exécutera
app.listen(8080);

// *** Routes GET - afficher les pages ***
// Route racine
app.get('/', function (req, res) {
    res.render('pages/index');
});
```

Tout d'abord, nous devons ajouter le module Node EJS à notre serveur. Donc, dans le fichier `server.js` (voir exemple ci-dessus), ajoutez `const ejs = require('ejs');`.

Deuxièmement, nous devons dire à notre serveur Express d'utiliser EJS, donc ajoutez `app.set('view engine', 'ejs');`.

Maintenant, nous devons configurer les routes. Les routes disent au serveur quoi faire lorsqu'un utilisateur va à une certaine URL dans votre site Web, comme `http://testapp.com/login`. 

Il existe deux types de routes, GET et POST. Les routes GET affichent les pages et les routes POST téléchargent des données du front-end vers le serveur (généralement via un formulaire), généralement avant qu'une page ne soit rendue et que les données téléchargées soient utilisées d'une certaine manière.

Puisque nous voulons seulement afficher nos pages EJS, nous utiliserons uniquement les routes GET. Ajoutez-les après la ligne `app.listen(8080)` dans `server.js`. Pour la page d'accueil, la route sera :

```js
// *** Routes GET - afficher les pages ***
// Route racine
app.get('/', function (req, res) {
    res.render('pages/index');
});
```

Le '/' spécifie l'URL du site Web sur laquelle le code sera activé, `req` signifie requête et `res` signifie réponse. Donc, la réponse retournée lorsque vous allez sur `http://testapp.com` est le rendu (affichage dans le navigateur) de la page pages/index.ejs. Ajoutez des routes similaires pour vos autres pages EJS.

### Passer des données côté serveur au front-end

L'attrait principal du templating, en plus de la réutilisation de code, est que vous pouvez passer des variables côté serveur au front-end. Soit une seule variable comme le nom d'utilisateur de l'utilisateur actuel, soit un tableau, comme les détails de chaque utilisateur enregistré. 

Cependant, la véritable puissance du passage de variables côté serveur devient apparente lors de l'utilisation d'API ou de bases de données.

Pour un exemple de base, le code ci-dessous affichera "Louise" dans la balise h2 de la page d'accueil :

**server.js**
```js
// Route racine
app.get('/', function (req, res) {
    var name = "Louise";
    // Rendre la page d'accueil
    res.render('pages/index', {
        // Variable EJS et variable côté serveur
        name: name
    });
});
```

Le premier `name` est le nom de la variable EJS (le nom pour l'afficher sur le front-end), et le second est la variable qui contient les données que vous voulez envoyer. (Ils n'ont pas besoin d'être identiques.)

**index.ejs**
``` html
<h2>Mon nom est <%= name %></h2>
```

Pour un simple tableau, vous pouvez utiliser cet exemple à la place, qui créera une balise p pour chaque nom dans la variable listnames :

**server.js**

``` js
// Route racine
app.get('/', function (req, res) {
    var listnames = ["Louise", "Sadie", "Erik", "Raph", "Gina"];
    // Rendre la page d'accueil
    res.render('pages/index', {
        // Variable EJS et variable côté serveur
        listnames: listnames
    });
});
```

**index.ejs**
``` html
<% listnames.forEach(function(name) { %>
        <p><%= name %></p>
        <% }); %>
```

Félicitations. Vous avez terminé le développement de votre première application Web Node.js. Dans la prochaine partie, nous verrons comment la rendre accessible (la déployer) sur le Web pour que vous puissiez la montrer.


## Déployer votre première application Web Node.js

Il existe de nombreuses plateformes d'hébergement que vous pouvez utiliser pour déployer vos applications Web Node.js, telles que [Section](https://www.freecodecamp.org/news/modules/node-js), [Heroku](https://www.heroku.com), [Vultr](https://www.vultr.com), [Linode](https://www.linode.com), [Google Cloud Platform](https://console.cloud.google.com) et [Amazon Web Services](https://aws.amazon.com). 

Dans ce guide, nous utiliserons [DigitalOcean](https://www.digitalocean.com) pour déployer notre application Node.js.

### Configuration de DigitalOcean

Tout d'abord, créez un compte sur la plateforme DigitalOcean. Il existe des codes de réduction disponibles pour ajouter du crédit gratuit à votre compte, comme le code disponible dans le GitHub Student Developer Pack. Sachez que vous ne pouvez racheter qu'un seul code par compte.

Deuxièmement, vous devez créer un droplet. Un droplet est un VPS (Virtual Private Server). C'est similaire à une VM Linux qui est hébergée sur une ferme de serveurs quelque part. 

Une fois que vous avez connecté votre compte, allez à droplets sous l'en-tête Manage et cliquez sur create puis sur droplets.

Vous pouvez laisser la plupart des paramètres par défaut, mais changez le plan pour le plan de base à 5 $ par mois, qui contient suffisamment de ressources pour votre application. Vous pouvez augmenter cela plus tard si nécessaire.

De plus, choisissez le centre de données le plus proche de l'audience cible de votre application et changez l'authentification en mot de passe. Bien que l'authentification par mot de passe soit moins sécurisée (les clés SSH sont recommandées), elle est beaucoup plus facile à configurer. Donc, à des fins de démonstration, nous utiliserons cette méthode.

Il ne reste plus qu'à choisir un nom (nom d'hôte) et à cliquer sur Create Droplet.

### Connexion à votre Droplet

Peu de temps après, vous recevrez un e-mail contenant le nom d'utilisateur et le mot de passe de votre droplet que vous utiliserez pour vous connecter.

De retour sur le site Web de DigitalOcean, sous droplets, cliquez sur le nom de votre nouveau droplet, puis cliquez sur Console. Cela ouvrira un nouvel onglet qui vous permettra de contrôler votre droplet. 

Alternativement, vous pouvez utiliser n'importe quel client SSH avec l'adresse IP et les identifiants de l'utilisateur contenus dans l'e-mail.

Lors de votre première connexion, puisque vous avez utilisé l'authentification par mot de passe, il vous sera demandé de définir un nouveau mot de passe. Une excellente façon de générer des mots de passe sécurisés et de les stocker est d'utiliser un gestionnaire de mots de passe comme [LastPass](https://www.lastpass.com).

### Déployer votre application Web Node.js

Tout d'abord, vous devrez copier le code de votre application Web sur votre droplet. Si vous utilisez un contrôle de source comme [Git](https://www.freecodecamp.org/news/engineering-education/beginner-guide-to-git/), alors c'est aussi simple que d'installer git en utilisant `apt-get install git -y` puis en utilisant la commande git clone `git clone (lien vers votre dépôt)`, en ajoutant le lien vers votre dépôt à la fin.

Deuxièmement, vous devrez installer Node. Tapez :

```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Troisièmement, vous devrez naviguer jusqu'au dossier contenant votre application Web. Tapez ls puis entrée pour voir tous les dossiers dans votre répertoire de travail actuel (emplacement). Cela devrait ressembler à l'image ci-dessous :

![website-folders](https://www.freecodecamp.org/news/content/images/2020/07/website-folders.png)

Tapez cd puis le nom du dossier qui apparaît. Tapez ls à nouveau et vous devriez voir les fichiers dans le répertoire racine de votre application Web.

Ensuite, vous devrez installer les modules Node (dépendances) pour votre application Web. Si vous avez installé tous vos modules avec `-save` à la fin, ce qui les sauvegarde dans le fichier package.json, alors tapez simplement `npm install` et appuyez sur entrée.

Sinon, lorsque vous exécutez `npm start`, une erreur apparaîtra avec module not found. Tapez `npm install (nom du module)` et appuyez sur entrée, puis essayez d'exécuter `npm start` à nouveau. Répétez le processus jusqu'à ce que l'erreur disparaisse.

Si vous devez installer MongoDB (si vous avez créé une base de données MongoDB), alors suivez ces [instructions](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition).

Enfin, tapez `npm start` pour démarrer votre application Web. Maintenant que votre application Web est en cours d'exécution, dans un nouvel onglet du navigateur, tapez l'adresse IP de votre droplet (trouvée dans l'e-mail que DigitalOcean a envoyé lorsque vous avez créé le droplet) suivie de deux points et du port sur lequel votre application s'exécute. Par exemple, `167.172.54.51:8080`.

Si vous utilisez un serveur Web Express (ce que vous avez fait si vous avez suivi mon guide de démarrage avec [Node.js](https://www.section.io/engineering-education/static-site-dynamic-nodejs-web-app/)), vous trouverez le numéro de port situé dans la ligne `app.listen()` à l'intérieur du fichier server.js. Par exemple, `app.listen(8080)` qui est un port commun utilisé.

Félicitations, votre première application Web Node.js devrait être affichée dans votre navigateur Web qui s'exécute sur votre droplet DigitalOcean.

### Configurer votre nom de domaine

Vous avez tapé une adresse IP et un numéro de port pour voir votre application Web, mais ne préféreriez-vous pas un nom de domaine personnalisé comme yourapp.com ?

En supposant que vous avez déjà acheté un domaine, la première étape est d'ajouter un enregistrement DNS afin que votre nom de domaine soit résolu en l'adresse IP de votre droplet DigitalOcean. Un enregistrement DNS indique à votre navigateur quoi faire lorsqu'ils chargent votre domaine. Dans ce cas, il doit aller à l'adresse IP de votre droplet. 

Si vous n'avez pas acheté de domaine, des registraires de domaines comme [Namecheap](https://www.namecheap.com) vendent des noms de domaine et souvent d'autres services tels que l'e-mail et l'hébergement statique/CMS, bien qu'il y ait des avantages à opter pour un fournisseur d'hébergement et d'e-mail dédié. 

[Netlify](https://www.netlify.com) offre l'hébergement pour les sites statiques et [SiteGround](https://www.siteground.co.uk) pour les sites Web CMS. Office365 et GSuite sont les rois des fournisseurs d'e-mails personnalisés. Voir mon guide pour [Configurer un e-mail professionnel](https://www.section.io/engineering-education/creating-professional-email/) pour lire une comparaison de Office365 et GSuite.

![advanced-dns](https://www.freecodecamp.org/news/content/images/2020/07/advanced-dns.png)

Connectez-vous à votre registraire de domaine et allez aux paramètres DNS avancés de votre domaine. Par exemple, sur Namecheap, c'est l'onglet Advanced DNS sur l'écran Manage Domain.

![dns-records](https://www.freecodecamp.org/news/content/images/2020/07/dns-records.png)

Vous voulez ajouter un nouvel enregistrement comme suit : le type doit être défini sur A, l'hôte doit être soit @ soit vide (selon votre fournisseur), et la valeur doit être l'adresse IP de votre droplet. Répétez le processus pour l'hôte www qui fera de même pour la version www de votre domaine.

![dns-check](https://www.freecodecamp.org/news/content/images/2020/07/dns-check.png)

Il peut falloir jusqu'à 24-48 heures pour que les changements soient traités, mais c'est généralement entre 15 minutes et une heure. Un moyen rapide de vérifier quand c'est fait est d'aller sur [DNSChecker](dnschecker.org). Tapez votre nom de domaine et assurez-vous que le type est défini sur A. Lorsque le résultat revient comme l'adresse IP de votre droplet, alors vous avez connecté votre domaine avec succès.

Le test final est de taper votre nom de domaine suivi de deux points et puis le numéro de port (par exemple, `yourdomain.com:8080`). Vous devriez maintenant voir votre application Web se charger.

### Supprimer le numéro de port de votre URL

Maintenant que vous avez un nom de domaine cool connecté à votre application Web, vous voudrez probablement supprimer ce numéro de port gênant. 

Nous pouvons faire cela en configurant ce qu'on appelle un proxy inverse. Un proxy inverse indiquera à votre droplet que lorsque quelqu'un va sur yourdomain.com, il doit servir le site à yourdomain.com:8080. Nous utiliserons le proxy inverse populaire [Nginx](https://www.nginx.com) pour cela.

La première étape est d'installer Nginx. Tapez ce qui suit pour mettre à jour votre liste de paquets (afin de pouvoir obtenir la dernière version) et installer Nginx :

```bash
sudo apt-get update
sudo apt-get install nginx
```

Puisque les droplets DigitalOcean sont créés avec un pare-feu activé, vous devrez autoriser Nginx à travers celui-ci pour qu'il puisse fonctionner correctement. `sudo ufw allow 'Nginx Full'` fera cela.

Pour vérifier que l'installation s'est déroulée sans problème, allez à la version http de votre nom de domaine, par exemple `http://yourdomain.com`. Si vous voyez une page de bienvenue à Nginx, alors cela a été un succès.

La deuxième étape est de sécuriser votre proxy inverse. Actuellement, aller sur `https://yourdomain.com` ne fonctionnera pas. C'est parce que nous n'avons pas encore configuré SSL, et nous devons installer un package appelé Certbot pour le faire.

Pour installer Certbot, tapez ce qui suit pour vous assurer d'obtenir la dernière version :

```bash
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get install python-certbot-nginx
```

Ensuite, vous devez ajouter votre domaine à Nginx afin que Certbot puisse générer un certificat pour le bon domaine. Ouvrez le fichier de configuration en utilisant `sudo nano /etc/nginx/sites-available/default` et remplacez les underscores dans la ligne server_name par votre domaine. Par exemple, `server_name yourdomain.com www.yourdomain.com;`. Enregistrez le fichier et quittez en tapant CTRL+x, y et puis entrée.

Pour tester qu'il n'y a pas d'erreurs dans le fichier, tapez `sudo nginx -t` et s'il n'y en a pas, tapez `sudo systemctl reload nginx` pour recharger Nginx afin qu'il utilise la configuration mise à jour.

Maintenant, nous devons simplement générer le certificat SSL. `sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com` lancera le processus. Vous devriez choisir l'option 2 pour le processus de redirection car elle redirigera toute personne essayant d'accéder à la version non sécurisée de votre site (http) vers la version sécurisée (https) à la place.

Pour tester cela, allez sur `https://yourdomain.com` et vous devriez voir à nouveau l'écran de bienvenue de Nginx.

Enfin, nous passons à la dernière étape, l'ajout de la configuration Nginx pour votre application Web. À des fins de démonstration, nous modifierons simplement celle par défaut au lieu d'en créer une nouvelle spécifiquement pour votre application Web. Si vous devez héberger plusieurs applications Web sur un seul droplet, vous devrez ajouter une nouvelle configuration pour chaque site.

Tapez : `sudo nano /etc/nginx/sites-available/default` pour éditer le fichier de configuration par défaut.

Vous devez changer le paramètre `server_name` par le nom de votre domaine. Par exemple : yourdomain.com. Sous location /, `proxy_pass` doit être changé en `http://localhost:(nom du port)`. Le `ssl_certificate_key` doit être modifié : `/etc/letsencrypt/live/(nom de domaine)/privkey.pem`. Enfin, ajoutez le bloc de code ci-dessous à la fin du fichier, puis tapez CTRL+X, puis y pour quitter.

```bash
server {
    if ($host = auroraspotter.space) {
        return 301 https://$host$request_uri;
    } # géré par Certbot
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name auroraspotter.space;
    return 404; # géré par Certbot
```

Voici un exemple complet de ce à quoi cela devrait ressembler. **Note :** le `server_name` doit être le nom de votre domaine.

```bash
server {
        root /var/www/html;      
        index index.html index.htm index.nginx-debian.html;
        server_name auroraspotter.space;
         
location / {
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-NginX-Proxy true;
       proxy_pass http://localhost:8080;
       proxy_set_header Host $http_host;
       proxy_cache_bypass $http_upgrade;
       proxy_redirect off;
 }
    listen [::]:443 ssl ipv6only=on; # géré par Certbot
    listen 443 ssl; # géré par Certbot
    ssl_certificate /etc/letsencrypt/live/auroraspotter.space/fullchain.pem; # géré par Certbot
    ssl_certificate_key /etc/letsencrypt/live/auroraspotter.space/privkey.pem; # géré par Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # géré par Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # géré par Certbot
}
server {
    if ($host = auroraspotter.space) {
        return 301 https://$host$request_uri;
    } # géré par Certbot
    
        listen 80 default_server;
        listen [::]:80 default_server;
        
        server_name auroraspotter.space;
    return 404; # géré par Certbot
```

Pour tester qu'il n'y a pas d'erreurs dans le fichier, tapez `sudo nginx -t`. S'il n'y en a pas, tapez `sudo systemctl reload nginx` pour recharger Nginx afin qu'il utilise la configuration mise à jour.

Enfin, vous devriez pouvoir aller sur yourdomain.com et votre application Web sera en cours d'exécution.

### Exécuter l'application au démarrage (Configuration d'un gestionnaire de processus)

Vous avez connecté votre nom de domaine à votre droplet et configuré Nginx pour servir votre application Web, mais comment la garder en cours d'exécution tout le temps, surtout après avoir redémarré votre droplet ? 

C'est là qu'intervient un gestionnaire de processus. Il gérera votre application Web Node.js, journalisera les erreurs et la démarrera/arrêtera selon les besoins. Nous utiliserons le gestionnaire de processus appelé PM2.

La première étape est d'installer PM2 en utilisant `sudo npm install pm2@latest -g`. Ensuite, pour l'exécuter au démarrage, exécutez `pm2 startup systemd`. Il devrait dire de configurer le script de démarrage, copiez et collez la commande suivante qui sera `sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u (nom d'utilisateur) --hp /home/(nom d'utilisateur)`. 

Si vous utilisez la connexion par défaut que DigitalOcean a fournie, ce sera root. Tapez cela dans le terminal et appuyez sur entrée. Si cela dit que la commande a été exécutée avec succès (comme ci-dessous), alors cela a fonctionné.

```bash
[ 'systemctl enable pm2-root' ]
[PM2] Écriture de la configuration d'initialisation dans /etc/systemd/system/pm2-root.service
[PM2] Création du script de démarrage...
[PM2] [-] Exécution : systemctl enable pm2-root...
[PM2] [v] Commande exécutée avec succès.
```

En utilisant la commande cd, naviguez jusqu'au dossier de votre application Web. Ensuite, tapez `pm2 start server.js`. Cela démarrera l'application Web en utilisant pm2. Ensuite, tapez `pm2 save` qui la sauvegardera pour être démarrée au démarrage. Si cela dit sauvegardé avec succès, alors cela a été sauvegardé correctement.

```bash
[PM2] Sauvegarde de la liste des processus en cours...
[PM2] Sauvegardé avec succès dans /root/.pm2/dump.pm2
```

Enfin, tapez `sudo systemctl start pm2-(nom d'utilisateur)`.

Essayez de redémarrer votre droplet en tapant reboot et après quelques minutes, allez sur `yourdomain.com`. Votre application Web devrait être en cours d'exécution comme d'habitude.

Si vous cherchez à développer les compétences que vous avez apprises dans ce tutoriel, je suggère d'utiliser le templating EJS pour travailler avec des API et des [bases de données](https://louisefindlay.com/blog/getting-to-grips-with-databases-part1).