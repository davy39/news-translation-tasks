---
title: Comment utiliser lite-server pour un serveur Web de développement simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-26T15:50:01.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-use-lite-server-for-a-simple-development-web-server-33ea527013c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m6fftYKAvqCzHI0Zx_4FGQ.jpeg
tags:
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment utiliser lite-server pour un serveur Web de développement simple
seo_desc: 'By Todd Palmer

  If you need an easy and light-weight Web Server just to do some development, lite-server
  is an excellent choice.

  In this article I will:


  Briefly explain the what and why of lite-server.

  Show you how to create a simple web application ...'
---

Par Todd Palmer

Si vous avez besoin d'un **serveur Web facile et léger** juste pour faire du développement, [lite-server](https://github.com/johnpapa/lite-server) est un excellent choix.

Dans cet article, je vais :

1. Expliquer brièvement le **quoi et pourquoi** de **lite-server**.
2. Vous montrer comment **créer une application web simple** et la servir avec **lite-server**.
3. Expliquer quelques configurations simples de **lite-server**.
4. Enfin, si vous souhaitez **installer lite-server une fois et l'utiliser partout**, consultez mon projet [www-lite-server sur GitHub](https://github.com/t-palmer/www-lite-server).

Bien que cet article soit écrit pour un niveau introductif, je m'attends à ce que :

* Vous connaissiez un peu l'invite de commande, comme la création et le changement de répertoires.
* Vous ayez [npm](https://www.npmjs.com/) installé et compreniez comment l'utiliser pour installer des packages.
* Vous sachiez comment créer des pages web simples en utilisant HTML.

### Qu'est-ce que lite-server ?

[lite-server](https://github.com/johnpapa/lite-server) est un **serveur web de développement léger avec support pour les Applications Monopage (SPAs)**. En réalité, c'est un peu plus technique que cela. Mais pour nos besoins, c'est suffisant.

**lite-server** a été créé par [John Papa](https://www.freecodecamp.org/news/how-you-can-use-lite-server-for-a-simple-development-web-server-33ea527013c9/undefined). Vous devriez le suivre et lire tout ce qu'il écrit, car il est un **vrai héros de la communauté open source** !

![Image](https://cdn-media-1.freecodecamp.org/images/1*nV5CbqhIJg22vVQnOA9dKw.png)
_[John Papa](undefined" rel="noopener" target="_blank" title=")_

John a créé **lite-server** parce qu'il voulait un serveur web simple qu'il pouvait utiliser pour tester le déploiement d'**Applications Monopage** qui utilisent des routes URL. Peut-être que vous n'utilisez pas encore de Frameworks GUI JavaScript comme [Angular](https://angular.io/), [React](https://reactjs.org/), et Vue.js. Mais sachez que lorsque vous le ferez, **lite-server** sera toujours là pour vous.

Alors, profitons du travail de John en...

### Utilisation de lite-server dans un projet Web

Tout d'abord, nous allons créer un petit projet web avec un simple **index.html**. Nous installerons **lite-server**. Ensuite, nous utiliserons **lite-server** pour servir notre page web.

#### Créer un projet

À votre invite de commande, exécutez :

```
mkdir lite
cd lite
```

Cela crée un nouveau répertoire appelé **lite** et en fait notre répertoire de travail.

Dans notre répertoire **lite**, ajoutez un fichier **index.html** qui ressemble à ceci :

#### Installer lite-server

À l'invite de commande dans votre répertoire **lite**, exécutez :

```
npm init -y
```

Nous utilisons [npm](https://www.npmjs.com/) pour initialiser un projet vide. Le `-y` lui indique d'utiliser simplement les valeurs par défaut pour tous les paramètres.

Pour ajouter **lite-server** à notre projet, nous pouvons exécuter :

```
npm install --save-dev lite-server
```

Cela installe le package **lite-server** et l'ajoute aux **devDependencies** dans le fichier **package.json** de notre projet.

```
"devDependencies": {    "lite-server": "^2.3.0"  }
```

De plus, vous pouvez consulter le dossier **node_modules** et voir que **lite-server** et ses dépendances sont tous installés là.

#### Exécuter lite-server

Dans votre fichier **package.json**, modifiez l'objet **scripts**. Remplacez le contenu par une entrée appelée `start` qui exécute **lite-server**, comme ceci :

```
"scripts": { "start": "lite-server"},
```

Ainsi, votre fichier **package.json** devrait maintenant ressembler à ceci :

Pour exécuter **lite-server** et servir votre page web **index.html**, exécutez :

```
npm start
```

Remarquez que **lite-server** lance votre navigateur par défaut et affiche votre **index.html** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qAp97i9vMP7N5nC6z95Bjw.png)

De plus, **lite-server** est construit sur [Browsersync](https://www.browsersync.io/). Ainsi, lorsque nous mettons à jour notre **index.html**, lite-server se rafraîchira automatiquement. Essayons !

Dans votre **index.html**, juste avant la balise `<a>`, ajoutez une balise d'en-tête à la page :

```
<h1>lite-server</h1>
```

Enregistrez votre fichier et regardez votre navigateur se mettre à jour **auto-magiquement** !

![Image](https://cdn-media-1.freecodecamp.org/images/1*7OY0E-v8l2vZZxNjHKK14Q.png)

### Quelques configurations simples

**lite-server** supporte beaucoup de flexibilité quant à sa configuration. Mais pour cet article, nous allons garder cela simple.

Nous allons créer un fichier de configuration **lite-server** et l'éditer pour changer :

* le port HTTP
* le répertoire racine web
* quel navigateur est lancé

#### Le fichier de configuration de lite-server

Le **fichier de configuration** pour **lite-server** est : **bs-config.json**

Pourquoi **bs-config** ? Eh bien, **lite-server** est construit sur [Browsersync](https://www.browsersync.io/) qui supporte l'utilisation d'un fichier de configuration JSON ou JavaScript nommé **bs-config**.

Ajoutez un fichier **bs-config.json** à la racine de votre projet. Il devrait ressembler à ceci :

Cet exemple de fichier de configuration reproduit simplement les valeurs par défaut. Mais nous allons l'utiliser comme base pour expliquer comment changer certains des paramètres de configuration les plus utiles.

#### Spécifier le port HTTP

Par défaut, **lite-server** utilise le **port 3000**. Mais si vous souhaitez utiliser un autre port, vous pouvez facilement le changer.

Par exemple, changeons-le pour utiliser le port 3001. Dans votre fichier **bs-config.json**, changez le **port** pour qu'il ressemble à ceci :

```
"port": 3001,
```

Redémarrez **lite-server** en utilisant `npm start`.

**lite-server** lance à nouveau notre navigateur par défaut. Mais cette fois, l'URL ressemble à ceci :  
`[http://localhost:3001/](http://localhost:3001/)`

#### Spécifier le répertoire racine Web

Par défaut, **lite-server** sert les pages à partir du répertoire courant où il est installé. En utilisant l'élément **server** dans **bs-config.json**, nous pouvons spécifier un autre répertoire racine web ou **"répertoire de base"** comme l'appelle **lite-server**.

Essayons :

1. Dans votre projet **lite**, créez un répertoire appelé : **test**
2. Copiez votre **index.html** dans le répertoire **test**
3. Dans **bs-config.json**, modifiez l'élément server pour qu'il ressemble à ceci :

```
"server": {  "baseDir": "./test"}
```

Redémarrez lite-server. Vous pouvez voir dans la sortie qu'il est :  
**Serving files from: ./test**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gc6nHvtkISSEKhehhLggJg.png)

#### Lancer le navigateur

Lorsqu'il démarre, **lite-server** lance notre navigateur par défaut pour afficher la page web. Mais peut-être souhaitez-vous que votre projet supporte à la fois **IE** et **Chrome**. Eh bien, nous pouvons dire à **lite-server** de lancer les deux.

Remarquez que l'entrée du navigateur dans le fichier de configuration est en réalité un tableau. Nous pouvons donc lui donner une liste de chaînes.

Amusons-nous un peu avec cela et faisons en sorte que lite-server lance plusieurs navigateurs. Sur ma machine, j'ai trois navigateurs installés : Chrome, IE et Firefox. Pour faire en sorte que **lite-server** lance les trois, je change simplement l'entrée du navigateur en :

```
"browser": ["chrome", "iexplore", "firefox"]
```

Et maintenant, lorsque j'exécute `npm start`, je vois ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OXA9XEMm6zFc2VvrWiMaMg.png)

Parce que hey ! On ne peut jamais avoir **trop** de navigateurs ouverts.

### www-lite-server : Installer une fois et l'utiliser partout

Puisque nous pouvons configurer le **répertoire de base** du serveur dans notre **bs-config.json**, nous pouvons en fait installer **lite-server** à un endroit et le pointer vers n'importe quel autre projet.

J'ai créé un projet simple appelé [www-lite-server](https://github.com/t-palmer/www-lite-server) pour vous qui fait exactement cela. Vous pouvez l'utiliser comme ceci :

```
git clone https://github.com/t-palmer/www-lite-server.git
cd www-lite-server
npm install
npm start
```

Cela servira le **index.html** local, qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1XEsYGi6EatSvZ4KmxL-VQ.png)

En modifiant l'entrée **baseDir** dans le **bs-config.json**, vous pouvez faire en sorte que **www-lite-server** serve des pages web pour n'importe lequel de vos projets. Par exemple, si vous avez un projet dans :  
**C:\dev\my-project**   
changez simplement votre **bs-config.json** pour qu'il ressemble à ceci :

```
{  "port": 3000,  "server": {    "baseDir": "C:\dev\my-project"  }}
```

Puis utilisez `npm start` pour commencer à servir des pages web.

### Quelques notes techniques

**lite-server** n'est qu'un wrapper autour de [Browsersync](https://www.browsersync.io/). En réalité, c'est Browsersync qui fait la plupart du "travail lourd". Cependant, les **Applications Monopage** utilisent généralement des routes que Browsersync ne gère pas. Pour plus d'informations, consultez la [section Why sur le README GitHub de lite-server](https://github.com/johnpapa/lite-server#why).

### Ressources

Suivez [John Papa](https://www.freecodecamp.org/news/how-you-can-use-lite-server-for-a-simple-development-web-server-33ea527013c9/undefined) sur Medium : [https://medium.com/@John_Papa](https://medium.com/@John_Papa)

Veuillez mettre une étoile à lite-server sur GitHub : [https://github.com/johnpapa/lite-server](https://github.com/johnpapa/lite-server)

www-lite-server : [https://github.com/t-palmer/www-lite-server](https://github.com/t-palmer/www-lite-server)

Browsersync : [https://www.browsersync.io/](https://www.browsersync.io/)