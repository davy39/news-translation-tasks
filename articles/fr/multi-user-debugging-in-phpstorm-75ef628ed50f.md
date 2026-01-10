---
title: Débogage multi-utilisateur dans PhpStorm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-27T18:53:09.000Z'
originalURL: https://freecodecamp.org/news/multi-user-debugging-in-phpstorm-75ef628ed50f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yKZWGE1b63HIBG7t.png
tags:
- name: debugging
  slug: debugging
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Débogage multi-utilisateur dans PhpStorm
seo_desc: 'By Ray Naldo

  Using Xdebug and DBGp Proxy


  _Photo by [Unsplash](https://unsplash.com/photos/iIJrUoeRoCQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Philipp Katzenberger on <a href="https:...'
---

Par Ray Naldo

#### Utilisation de Xdebug et du proxy DBGp

![Image](https://cdn-media-1.freecodecamp.org/images/zy6mxhP-e7wKyxEDa6MiScE97bsEsCHC6lOT)
_Photo par [Unsplash](https://unsplash.com/photos/iIJrUoeRoCQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Philipp Katzenberger</a> sur <a href="https://unsplash.com/search/photos/computer?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

« Er, attendez une minute… N'utilisez-vous pas simplement `xdebug.remote_connect_back` qui a été introduit depuis Xdebug 2.1 ? »

Bien sûr, si le serveur web n'est accessible que par les développeurs (par exemple, serveur de développement privé), et s'il ne fonctionne pas derrière un pare-feu NAT, et si vous voulez que ce guide se termine ici. Voyez-vous ces SI ? Personnellement, je n'aime pas les SI en programmation ou dans la vie. Donc ce guide empruntera le chemin le plus long qui ne nécessite pas un SI pour commencer (ou au moins moins de SI), c'est-à-dire en utilisant le proxy DBGp de Xdebug.

> _Lorsqu'un proxy est utilisé, l'extension PHP Xdebug ne se connecte plus directement à PhpStorm, mais se connecte plutôt au serveur proxy DBGp. Tous les développeurs de l'équipe se connectent ensuite à ce proxy. Chaque développeur dispose d'une session de débogage distincte fonctionnant via ce proxy, ce qui permet de faire du débogage multi-utilisateur du même code sur le même serveur._

![Image](https://cdn-media-1.freecodecamp.org/images/eqhOVjy5SAixdKUAx6nGOpQuLuVZqKZWIkAz)
_[https://www.jetbrains.com/help/phpstorm/multiuser-debugging-via-xdebug-proxies.html](https://www.jetbrains.com/help/phpstorm/multiuser-debugging-via-xdebug-proxies.html" rel="noopener" target="_blank" title=")_

Ainsi, avec le proxy DBGp, vous pouvez limiter qui peut se connecter au proxy, et vous pouvez avoir plusieurs développeurs déboguant le même serveur web fonctionnant derrière un pare-feu NAT.

> _Exécuter un proxy DBGp vous permet également d'éviter les problèmes de NAT où (comme vu depuis PHP+Xdebug sur le serveur) toutes les connexions semblent provenir de la même IP (parce que votre réseau interne est NAT). Dans ce cas, vous pouvez simplement exécuter le proxy dbgp sur votre machine NAT, configurer le paramètre `xdebug.remote_host` avec l'adresse IP de votre machine NAT, et configurer les IDE pour qu'ils se connectent au proxy fonctionnant sur `<NAT-machine>`:9001._

> _— [https://derickrethans.nl/debugging-with-multiple-users.html](https://derickrethans.nl/debugging-with-multiple-users.html)_

### Installation

Les mappages entre les dossiers du projet et les dossiers sur le serveur doivent être correctement effectués dans PhpStorm pour que le débogage fonctionne.

### Configuration du serveur web

Bien que ce guide suppose que le serveur web fonctionne sous Linux, le guide peut également être utilisé sur des serveurs web non-Linux avec des modifications mineures.

1. Installez Xdebug.

```
# PHP 7+
pecl install xdebug
# PHP 5.6.x
pecl install xdebug-2.5.5
```

2. Activez l'extension Xdebug, puis ajoutez la configuration suivante de [Xdebug](https://xdebug.org/docs/all_settings) à php.ini :

```
[xdebug]
zend_extension="<full_path_to_xdebug.so>"
```

```
; paramètres du débogueur
xdebug.remote_enable=1
xdebug.remote_host=127.0.0.1
xdebug.remote_port=9000
```

Pour ce guide, le proxy DBGp fonctionnera sur la même machine que le serveur web et utilisera le port par défaut de Xdebug, d'où `127.0.0.1:9000`.

3. Téléchargez et installez le proxy DBGp pour le débogage à distance depuis [Komodo Remote Debugging Package](http://code.activestate.com/komodo/remotedebugging/), spécifiquement pour le système d'exploitation de votre serveur web. Ce guide utilisera Linux 64 bits et le client PHP Remote Debugging v11.1.0. Extrayez l'archive ; pour simplifier, j'extrais tout le contenu dans mon répertoire personnel, c'est-à-dire `/home/ray/`.

4. Exécutez le proxy DBGp en exécutant le fichier `pydbgpproxy` avec les paramètres :

* `-d <ip_address:po`rt> pour définir l'adresse IP et le port de la machine qui recevra la connexion du débogueur depuis le serveur web
* `-i <ip_address:po`rt> pour définir l'adresse IP et le port de la machine qui recevra la connexion de débogage depuis l'ordinateur du développeur

Dans ce guide, le serveur web et le proxy DBGp fonctionneront sur la même machine. Si l'adresse IP est `10.211.1.32` et que nous voulons exécuter le proxy sur le port `9001`, la commande sera :

```
pydbgpproxy -d 127.0.0.1:9000 -i 10.211.1.32:9001
```

Pour plus de commodité, nous pouvons utiliser ce script, enregistré sous `start-dbgp-proxy.sh`. Je l'ai placé dans le même répertoire que `pydbgpproxy`, c'est-à-dire `/home/ray/start-dbgp-proxy.sh`) :

```
ip=$(hostname -I | awk '{$1=$1};1')
pydbgpproxy -d 127.0.0.1:9000 -i $ip:9001
```

5. Assurez-vous d'autoriser la connexion depuis localhost sur le port `9000`, et depuis les machines des développeurs sur le port `9001`.

6. Exécutez `start-dbgp-proxy.sh`. Ajoutez la permission d'exécution du fichier si vous ne pouvez pas l'exécuter.

```
start-dbgp-proxy.sh
```

Assurez-vous qu'il peut être exécuté sans problème.

```
INFO: dbgp.proxy: starting proxy listeners.  appid: 30430
INFO: dbgp.proxy:     dbgp listener on 127.0.0.1:9000
INFO: dbgp.proxy:     IDE listener on  10.211.1.32:9001
```

7. (Facultatif) Démarrez automatiquement `start-dbgp-proxy.sh` à chaque démarrage de la machine en utilisant crontab.

Éditez crontab :

```
crontab -e
```

Ajoutez une tâche cron pour démarrer automatiquement `start-dbgp-proxy.sh` à chaque démarrage :

```
@reboot /home/ray/start-dbgp-proxy.sh
```

### Configuration du client

1. Accédez au menu `Outils > DBGp Proxy > Enregistrer l'IDE` dans PhpStorm.

![Image](https://cdn-media-1.freecodecamp.org/images/6jGBI3DEhZtfJD5M9y2OTjN-omaT4beNyZne)

2. Remplissez `Clé IDE` avec une chaîne unique entre les développeurs. Remplissez `Hôte` et `Port` avec l'adresse IP et le port du proxy DBGp (paramètre `-i` dans [Configuration du serveur #4](https://medium.com/@naldoray/multi-user-debugging-in-phpstorm-75ef628ed50f#6728)).

![Image](https://cdn-media-1.freecodecamp.org/images/DxgCWv1iY1bg6qD0RY5nMnL1KjJZ1c60LSKQ)

3. Cliquez sur OK. Vous devriez voir une notification de succès apparaître. Si vous ne la voyez pas, réenregistrez l'IDE via `Outils > DBGp Proxy > Enregistrer l'IDE`. Si cela échoue ou si vous souhaitez modifier la configuration, faites-le via `Outils > DBGp Proxy > Configuration...`

4. (Facultatif) Si vous souhaitez initier une connexion de débogage depuis le navigateur web, il est recommandé d'installer une extension de débogage sur votre navigateur : [Xdebug Helper Firefox](https://addons.mozilla.org/en-US/firefox/addon/xdebug-helper-for-firefox/) ou [Xdebug Helper Chrome](https://chrome.google.com/webstore/detail/xdebug-helper/eadndfjplgieldjbigjakmdgkmoaaaoc). Configurez ensuite votre Xdebug Helper.

![Image](https://cdn-media-1.freecodecamp.org/images/Hr29yIOm6QT9tq3EKQTbvrDMb5F4r1Z17phu)

Sur Firefox, cliquez avec le bouton droit sur l'icône Xdebug Helper > Gérer l'extension… > Options
Sur Chrome, cliquez avec le bouton droit sur l'icône Xdebug Helper > Options

![Image](https://cdn-media-1.freecodecamp.org/images/11KlHe-x9KNf9mJhpIGd6ZNrsjYF9yNYbE2S)

Remplissez et enregistrez `Clé IDE` avec la même chaîne unique que lors de l'enregistrement de l'IDE ([Étape #2](https://medium.com/@naldoray/multi-user-debugging-in-phpstorm-75ef628ed50f#bea9)).

### Démarrer le débogage

1. Définissez des points d'arrêt dans PhpStorm.

2. Commencez à écouter la connexion de débogage dans PhpStorm en cliquant sur le bouton « téléphone » dans la barre d'outils en haut à droite ou depuis le menu `Exécuter > Commencer à écouter les connexions de débogage PHP`. Cela permettra à PhpStorm de réagir et d'ouvrir automatiquement la fenêtre de débogage lorsqu'une session de débogage est démarrée.

![Image](https://cdn-media-1.freecodecamp.org/images/8vY-Obed-f51RvowC6kRMJM3s6bDKfDX8l-G)

3. Activez le débogueur Xdebug lors de l'envoi d'une requête. Selon la [documentation Xdebug](https://xdebug.org/docs/remote#starting), il existe 3 façons de procéder. Mais à mon avis, la meilleure méthode qui fonctionne pour tous les types de méthodes HTTP consiste à définir un cookie nommé `XDEBUG_SESSION` avec la valeur `<IDE_k`ey> qui est la même chaîne unique que lorsque nous avons enregistré notre IDE auprès du proxy DBGp ([Configuration du client](https://medium.com/@naldoray/multi-user-debugging-in-phpstorm-75ef628ed50f#bea9) #2).

* Dans le navigateur web, le cookie sera défini automatiquement par l'extension Xdebug Helper

![Image](https://cdn-media-1.freecodecamp.org/images/iaIbl9VnNuiuhc2t7wy8lnAmrI-sTu7Iy4VF)

* Dans Postman, le cookie peut être défini dans les en-têtes de requête

![Image](https://cdn-media-1.freecodecamp.org/images/yz6sMh-jHy6KD3ninIJj3ftMZtkaMGJQTro1)

4. Exécutez le script avec le cookie déjà défini.

5. En cas de succès, PhpStorm affichera automatiquement la fenêtre de débogage.

![Image](https://cdn-media-1.freecodecamp.org/images/3LS3M-zKZuX8o5rtYKGYXYX1XKPDL0aSdDJK)

6. Assurez-vous de désactiver/ne pas envoyer le cookie pour désactiver le débogage et arrêter d'écouter la connexion de débogage dans PhpStorm si vous ne faites pas de débogage. Si vous ne le faites pas, cela fera planter le proxy DBGp lorsqu'il y a trop de connexions en attente.

J'espère que ce guide fonctionne pour vous.

Merci d'avoir lu !

### Références

* [https://www.jetbrains.com/help/phpstorm/multiuser-debugging-via-xdebug-proxies.html](https://www.jetbrains.com/help/phpstorm/multiuser-debugging-via-xdebug-proxies.html)
* [https://www.jetbrains.com/help/phpstorm/browser-debugging-extensions.html](https://www.jetbrains.com/help/phpstorm/browser-debugging-extensions.html)
* [https://xdebug.org/docs/remote#starting](https://xdebug.org/docs/remote#starting)