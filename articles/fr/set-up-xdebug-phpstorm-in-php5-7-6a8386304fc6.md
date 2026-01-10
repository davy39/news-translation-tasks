---
title: Comment configurer un environnement de débogage local en PHP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T19:18:43.000Z'
originalURL: https://freecodecamp.org/news/set-up-xdebug-phpstorm-in-php5-7-6a8386304fc6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6PPymPtLj4ITAaE_ei9ulw.jpeg
tags:
- name: debugging
  slug: debugging
- name: PHP
  slug: php
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment configurer un environnement de débogage local en PHP
seo_desc: 'By Goran Aviani

  Recently I started focusing more on PHP, and I needed to set up a local debugging
  environment. Since there aren’t many tutorials on how to do it, I’ve encountered
  some problems on how to get the setup up and running.

  By combining a fe...'
---

Par Goran Aviani

Récemment, j'ai commencé à me concentrer davantage sur PHP et j'ai eu besoin de configurer un environnement de débogage local. Comme il n'y a pas beaucoup de tutoriels sur la façon de le faire, j'ai rencontré quelques problèmes pour faire fonctionner la configuration.

En combinant quelques tutoriels et en passant quelques heures sur plusieurs forums, j'ai rédigé ce texte. L'application sur laquelle je travaille s'exécute dans une boîte Vagrant qui est quelque peu instable. Elle s'effondre de temps en temps, donc je dois refaire cette configuration, et c'est pourquoi je sais que cette configuration fonctionne :).

> _L'objectif de ce tutoriel est de faire fonctionner Xdebug sur votre serveur, puis de pointer PhpStorm vers Xdebug._

Commençons.

#### Prérequis

Si vous n'avez pas Xdebug installé sur votre serveur mais que vous utilisez PHP7, vous pouvez le faire en utilisant les instructions d'installation personnalisées du site officiel de Xdebug [ici](https://xdebug.org/wizard.php).

Cependant, comme mon projet utilise PHP5, j'ai dû le faire à l'ancienne : _en cherchant sur les forums_.

Dans ce tutoriel, je supposerai que vous avez Xdebug installé.

### Mise en route

Tout d'abord, vous devez trouver l'emplacement du fichier xdebug.so sur votre serveur. Copiez l'emplacement quelque part car vous en aurez besoin plus tard.

```
locate xdebug.so
```

Maintenant, vous devez naviguer dans votre serveur vers l'emplacement : /etc/php5/apache2/conf.d/ et vérifier si le fichier 20-xdebug.ini existe. S'il n'existe pas, créez-en un. Vous pouvez en créer un en utilisant des commandes telles que touch, vim, vi, nano, etc.

Vous pouvez voir que mon projet est fait en PHP5, alors changez le nom/emplacement de votre dossier selon votre version de PHP.

Maintenant, ouvrez le fichier 20-xdebug.ini et collez ceci :

```
zend_extension="emplacement de votre fichier xdebug.so"
xdebug.remote_enable=1
xdebug.remote_port=9000
xdebug.remote_host="votre adresse localhost"
xdebug.remote_autostart=1
xdebug.remote_connect_back=0
xdebug.remote_handler="dbgp"
xdebug.remote_mode=req
xdebug.remote_cookie_expire_time=-9999
xdebug.remote_log="/tmp/xdebug.log"
xdebug.var_display_max_depth=15
xdebug.profiler_enable=0
xdebug.idekey="phpstorm"
```

D'après l'explication du fichier 20-xdebug.ini écrite ci-dessous, vous verrez que certains de ces paramètres ne sont pas nécessaires, ou qu'ils sont définis à une valeur par défaut. Je garde ces valeurs dans le fichier 20-xdebug.ini car elles sont bonnes à savoir.

#### **Explication du fichier 20-xdebug.ini :**

* xdebug.remote_enable — contrôle si Xdebug doit essayer de contacter un client de débogage qui écoute sur l'hôte et le port définis avec les paramètres
* xdebug.remote_port — Le port auquel Xdebug essaie de se connecter sur l'hôte distant. Par défaut, c'est 9000.
* xdebug.remote_host — Sélectionne l'hôte où le client de débogage s'exécute. Par défaut, c'est localhost.
* xdebug.remote_autostart — lorsque ce paramètre est défini sur 1, Xdebug tentera de démarrer une session de débogage à distance et essayera de se connecter à un client.
* xdebug.remote_connect_back — Si activé, le paramètre [xdebug.remote_host](https://xdebug.org/docs/all_settings#remote_host) est ignoré et Xdebug essaiera de se connecter au client qui a fait la requête HTTP. Par défaut, c'est 0.
* xdebug.remote_handler — Peut être soit 'php3' qui sélectionne l'ancienne sortie de débogage [style PHP 3](http://www.php.net/manual/en/debugger.php), soit 'gdb' qui active l'interface de débogage de type GDB, soit 'dbgp' — le [protocole de débogage](http://xdebug.org/docs-dbgp.php). Le protocole DBGp est le seul protocole supporté. Par défaut, c'est dbgp.
* xdebug.remote_mode — Sélectionne quand une connexion de débogage est initiée. Ce paramètre peut avoir deux valeurs différentes : req — Xdebug essaiera de se connecter au client de débogage dès que le script démarre. jit — Xdebug n'essaiera de se connecter au client de débogage que lorsqu'une condition d'erreur se produit.
* xdebug.remote_cookie_expire_time — Ce paramètre peut être utilisé pour augmenter (ou diminuer) le temps pendant lequel la session de débogage à distance reste active via le cookie de session. Par défaut, c'est 3600.
* xdebug.remote_log — Si une valeur est définie, elle est utilisée comme nom de fichier pour un fichier dans lequel toutes les communications du débogueur à distance sont enregistrées.
* xdebug.var_display_max_depth — Contrôle le nombre de niveaux imbriqués d'éléments de tableau et de propriétés d'objet affichés lorsque les variables sont affichées avec soit [xdebug_var_dump()](https://xdebug.org/docs/all_functions#xdebug_var_dump), soit [xdebug.show_local_vars](https://xdebug.org/docs/all_settings#show_local_vars), soit via [Function Traces](https://xdebug.org/docs/execution_trace). Par défaut, c'est 3.
* xdebug.profiler_enable — Active le profileur de Xdebug qui crée des fichiers dans le [répertoire de sortie du profileur](https://xdebug.org/docs/all_settings#profiler_output_dir). Par défaut, c'est 0.
* xdebug.idekey — Contrôle quelle clé IDE Xdebug doit transmettre au gestionnaire de débogage DBGp. La valeur par défaut est basée sur les paramètres d'environnement.

Enregistrez le fichier et redémarrez le serveur Apache :

```
sudo service apache2 restart
```

### Xdebug et PhpStorm

Tout d'abord, vous devez ouvrir PhpStorm et sélectionner Exécuter > Modifier la configuration. Là, vous devez sélectionner + (Ajouter une nouvelle configuration) et choisir « PHP Remote Debug ».

Changez le nom de la configuration de « Unnamed » à autre chose. J'ai choisi le nom « Tutorial » pour des raisons évidentes ;) Ensuite, cochez « Filter debug connection by IDE key ».

![Image](https://cdn-media-1.freecodecamp.org/images/NjnubSo0dlzY8tQYtosUr2zbV-3PwZtPvdd9)

Sélectionnez le bouton Servers (...) puis sélectionnez + (Ajouter un nouveau serveur).

* Renommez votre serveur en quelque chose de plus apaisant. J'ai choisi « localbackend1 » dans cet exemple.
* Dans le champ Hôte, tapez votre localhost. Définissez le débogueur sur Xdebug.
* Sélectionnez « Use path mapping » et pointez vers le dossier de votre application.

Cliquez sur Appliquer. Vous serez renvoyé à la fenêtre précédente où vous verrez que la clé IDE est modifiable, et maintenant vous devez entrer une clé. Je mets toujours « phpstorm » ou quelque chose de similaire.

![Image](https://cdn-media-1.freecodecamp.org/images/KaooonBEOf6t7dTzZn8fGN-unZ7tyOEK9BHJ)

Vous remarquerez que la clé IDE « phpstorm » est déjà dans votre fichier 20-xdebug.ini :

```
xdebug.idekey="phpstorm"
```

Vous devriez également sélectionner « Single instance only » car cela vous empêchera de lancer plus d'une instance du même projet.

Cliquez sur Appliquer et voilà !

Vous avez terminé la configuration !

### **Test et conclusion**

Maintenant, vous avez terminé. Vous devriez voir la configuration Tutorial que nous avons créée dans le coin supérieur droit de PhpStorm.

![Image](https://cdn-media-1.freecodecamp.org/images/aJXGrZ-94n-cjERXOV4rjkTLm8kNe3GsboJ9)

Vous pouvez la tester en définissant un point d'arrêt dans votre projet. Cliquez sur le bouton « bug » dans la fenêtre de configuration de Tutorial, puis exécutez votre application.

Cela devrait être tout, si tout est correct, vous devriez atteindre le point d'arrêt.

Et n'oubliez pas, rien ne vaut le sentiment de voir les valeurs d'exécution lors du débogage.

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci et d'autres choses amusantes que je crée sur mon profil Github : [https://github.com/GoranAviani](https://github.com/GoranAviani)