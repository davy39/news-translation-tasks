---
title: Comment installer PHP, CaddyServer et Kirby sur MacOS — et pourquoi vous devriez
  le faire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-03T07:32:22.000Z'
originalURL: https://freecodecamp.org/news/php-caddyserver-und-kirby-on-macos-96811af35394
coverImage: https://cdn-media-1.freecodecamp.org/images/0*A-xWmyVxuvS0GqWQ
tags:
- name: Apple
  slug: apple
- name: development
  slug: development
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment installer PHP, CaddyServer et Kirby sur MacOS — et pourquoi vous
  devriez le faire
seo_desc: 'By Philipp Haidenbauer

  Recently Kirby Version 3.0 was released. As I have worked with Version 2 for quite
  some time in the past, I figured why not give it a try?

  Just before Christmas, I bought a brand new MacBook Air, so it was obvious that
  I would ...'
---

Par Philipp Haidenbauer

Récemment, [Kirby Version](https://getkirby.com/) 3.0 a été publiée. Comme j'ai travaillé avec la version 2 pendant un certain temps dans le passé, je me suis dit pourquoi ne pas essayer ?

Juste avant Noël, j'ai acheté un tout nouveau MacBook Air, il était donc évident que je voulais essayer Kirby immédiatement dessus. Je suis tombé sur un excellent [article](https://simonecarletti.com/blog/2016/05/caddy-server-php-macosx/) sur la façon d'installer [CaddyServer](https://caddyserver.com/) et PHP sur MacOS. Mais j'ai changé certaines choses.

### CaddyServer, PHP et Kirby

Commençons par un bref aperçu des logiciels dont je parle.

#### [PHP](http://www.php.net/)

Je ne pense pas avoir grand-chose à dire sur PHP. C'est probablement l'un des plus anciens langages de script dans le monde du Web. PHP était "le" langage pour rendre votre site web "dynamique". Et c'était aussi le premier langage que j'ai découvert et appris à utiliser.

#### [CaddyServer](https://caddyserver.com/)

C'est un petit mais très puissant serveur Web que j'ai découvert il y a quelques mois. Il possède des fonctionnalités vraiment intéressantes comme le SSL/HTTPs automatique et un fichier de configuration très facile à utiliser (que vous verrez plus tard). Et il est extrêmement rapide. :)

#### [Kirby](https://getkirby.com/)

Un autre excellent outil que j'ai découvert il y a quelques années. Basiquement, c'est un CMS (Content Management System) basé sur une simple structure de fichiers. Même si vous ne connaissez pas beaucoup PHP, il est relativement simple de créer des templates pour les pages et d'étendre toute la fonctionnalité.

#### Pourquoi ?

Maintenant que vous connaissez ces trois projets, vous vous demandez peut-être pourquoi vous devriez les utiliser ensemble. Eh bien, il y a plusieurs raisons à cela :

* MacOS est livré avec une installation par défaut d'[apache2](https://httpd.apache.org/), mais comme vous le savez peut-être, Apache est l'un des plus grands serveurs HTTP. Il est largement adopté, mais il a un inconvénient. Il consomme de la mémoire et du CPU comme aucun autre serveur web. Donc, si vous êtes en déplacement, il consomme également la batterie comme un fou et je n'aime pas ça.
* Caddy est très léger et n'utilise pas beaucoup de mémoire/CPU/batterie.
* Kirby, comme je l'ai dit, est facile à personnaliser et à étendre. Comme c'est un CMS, vous n'avez pas à vous soucier d'une base de données ou de la logique spécifique à l'application dès le début. Ainsi, vous pouvez prototyper assez rapidement, ce qui conduit à des résultats plus rapides et plus de satisfaction lorsque vous obtenez des choses faites. :)

Sans plus tarder, passons à l'installation :

### Tout d'abord

Il est essentiel d'avoir [homebrew](https://brew.sh/index_de) installé, car la gestion des paquets devient beaucoup plus facile avec lui.

Vous pouvez l'installer avec une simple commande :

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### PHP

Maintenant que nous avons un gestionnaire de paquets, il est temps d'installer la bonne version de PHP. Kirby nécessite au moins PHP 7.1, donc j'ai installé 7.2 :)

```
brew install php@7.2
```

Il y a aussi quelques extensions nécessaires :

```
brew install freetype jpeg libpng gd
```

### CaddyServer

Maintenant que nous avons PHP et certaines dépendances installées, nous pouvons installer CaddyServer.

Téléchargez simplement la version appropriée depuis [https://caddyserver.com/download](https://caddyserver.com/download).

Vous recevrez un fichier zip. Extrayez-le et copiez l'exécutable dans un chemin dans votre $PATH (dans mon cas `/Users/phaidenbauer/bin/`):

```
unzip caddy_v0.11.2_darwin_amd64_personal.zip
cp caddy /Users/phaidenbauer/bin/caddy
```

### Kirby

Le suivant est Kirby. Téléchargez à nouveau le zip depuis [https://getkirby.com/try](https://getkirby.com/try).

Extrayez-le quelque part où vous avez vos projets. Dans mon cas, c'est `/Users/phaidenbauer/development/`.

La prochaine chose essentielle pour faire fonctionner tout cela est le Caddyfile qui indique à Caddy quoi faire :)

```
localhost:8080
tls off
root ./
gzip
```

```
rewrite {    r .*    to {path} {path}/ /index.php?{path}&{query}}
```

```
fastcgi / 127.0.0.1:9000 php
on startup launchctl load -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.plist
on shutdown launchctl unload -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.plist
```

Passons en revue cela :

`localhost:8080` indique sur quel port il doit écouter. Si vous ne voulez pas l'exécuter en tant que root (ou via `set_cap`), vous devriez utiliser quelque chose au-dessus de 1024.

`tls off` désactive la fonctionnalité SSL/HTTPS intégrée, car nous travaillons uniquement localement.

`root ./` définit le chemin racine du répertoire de service.

`gzip` active la compression gzip pour les réponses.

`rewrite { r .* to {path} {path}/ /index.php?{path}&{query} }` réécrit toutes les URL entrantes pour répondre aux besoins de Kirby. (Ce n'est probablement pas la meilleure solution, mais cela fonctionne bien pour mon environnement de développement.)

`fastcgi / 127.0.0.1:9000 php` indique à Caddy de transférer les requêtes à un serveur FastCGI. Qui, dans notre cas, est PHP.

Maintenant, nous avons deux fonctions spéciales.

```
on startup launchctl load -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.plist
on shutdown launchctl unload -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.plist
```

Comme je l'ai mentionné plus tôt, ce n'est qu'un MacBook Air, donc je ne veux pas que PHP tourne tout le temps. Surtout quand je n'en ai pas besoin. La bonne chose est que Caddy peut exécuter des commandes sur des événements. Dans ce cas, nous utilisons les événements de démarrage et d'arrêt pour démarrer et arrêter PHP. Super ! Plus de gaspillage de RAM et de CPU en vérifiant les emails.

### Démarrer le tout :)

Maintenant, nous sommes presque prêts. La dernière chose à faire est de tout démarrer ensemble et de commencer à travailler :

```
cd /Users/phaidenbauer/development/fly.phaidenbauer.com
caddy
```

Vous devriez voir quelque chose comme ceci :

```
Activating privacy features... done.
http://localhost:8080
WARNING: File descriptor limit 4864 is too low for production servers. At least 8192 is recommended. Fix with `ulimit -n 8192`.
```

Et c'est tout. Prenez votre navigateur préféré et surfez vers [http://localhost:8080](http://localhost:8080). Selon que vous avez téléchargé le Kirby-Plainkit ou le Kirby-Starter kit, vous devriez voir un simple "Hello" ou une simple galerie.

Et c'est tout. Bon codage :)