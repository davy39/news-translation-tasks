---
title: Comment afficher les fichiers de journalisation de CodeIgniter dans le navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T23:09:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-view-codeigniter-log-files-in-the-browser-e4ec7a9e8b23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gmHGclQeDOJ1jUM3zhfXKg.jpeg
tags:
- name: codeigniter
  slug: codeigniter
- name: logging
  slug: logging
- name: open source
  slug: open-source
- name: PHP
  slug: php
- name: General Programming
  slug: programming
seo_title: Comment afficher les fichiers de journalisation de CodeIgniter dans le
  navigateur
seo_desc: 'By Seun Matt

  Just like any other page, it is now possible to read CodeIgniter log files in the
  browser. My Sweet Goodness!


  Example view of code igniter log files

  I began using CodeIgniter in my day to day coding after joining an awesome company.
  The...'
---

Par Seun Matt

Tout comme n'importe quelle autre page, il est désormais possible de lire les fichiers de journalisation de CodeIgniter dans le navigateur. Mon Dieu, c'est génial !

![Image](https://cdn-media-1.freecodecamp.org/images/d-k2Dfg0rgazIaeVdTY2NdzxgYN-2nUJxiQJ)
_Exemple d'affichage des fichiers de journalisation de CodeIgniter_

J'ai commencé à utiliser CodeIgniter dans mon travail quotidien après avoir rejoint une entreprise formidable. La pile technologique de l'entreprise inclut le Framework PHP — parmi d'autres. Jusqu'à présent, j'ai utilisé (et j'utilise toujours) Laravel pour construire des applications formidables.

Laravel dispose d'un système de journalisation simple et élégant. De plus, il existe une [bibliothèque](https://github.com/rap2hpoutre/laravel-log-viewer) pour afficher les journaux dans le navigateur. Pouvoir lire les journaux dans le navigateur est utile pour le débogage et l'analyse des applications. Surtout dans un environnement de production.

Me voilà donc dans le monde de CodeIgniter, sans trouver de bibliothèque équivalente pour lire mes journaux afin de déboguer et analyser.

J'ai donc relevé le défi et créé mon premier projet Open Source de l'année — [codeigniter-log-viewer](https://github.com/SeunMatt/codeigniter-log-viewer).

### Utilisation

Tout d'abord, ajoutons-le comme dépendance. Nous pouvons le faire en exécutant :

```
composer require seunmatt/codeigniter-log-viewer
```

Ensuite, nous pouvons créer un contrôleur d'application CodeIgniter, _LogViewerController.php_ :

```
private $logViewer;
```

```
public function __construct() {    $this->logViewer = new \CILogViewer\CILogViewer();    //...}
```

```
public function index() {    echo $this->logViewer->showLogs();    return;}
```

Ce que nous avons fait, c'est instancier _$logViewer_ dans le constructeur, puis afficher le résultat de _showLogs()_ dans la fonction _index()_.

La méthode _showLogs()_ de [codeigniter-log-viewer](https://github.com/SeunMatt/codeigniter-log-viewer) analysera le contenu des fichiers de journalisation dans _application/logs_. Elle le retournera pour affichage dans le navigateur.

Enfin, nous pouvons mapper n'importe quelle route de notre choix vers l'_index()_ que nous avons créé ci-dessus. Cela peut être fait en ajoutant une entrée au tableau _$route_ dans _application/config/routes.php_ :

```
$route['logs'] = "logViewerController/index";
```

Maintenant, nous pouvons visiter _/logs_ dans le navigateur et voir tous les fichiers de journalisation. Il est également possible de supprimer et de télécharger les fichiers de journalisation.

**Note** : Il est conseillé d'utiliser une route protégée en environnement de production pour éviter l'accès du grand public.

### Fonctionnement

En interne, la bibliothèque lit le nom de tous les fichiers de journalisation disponibles dans le répertoire de journaux par défaut dans un tableau et l'inverse. Si aucun fichier n'est spécifié dans les paramètres de requête de l'URL, le dernier fichier de journalisation est traité pour affichage par défaut.

Le traitement d'un fichier de journalisation pour affichage implique la lecture de son contenu, l'utilisation de regex pour déterminer le niveau de journalisation, la classe CSS et l'icône de chaque entrée.

Chaque entrée est également vérifiée pour savoir si elle est une nouvelle ligne de journalisation ou une continuation de la ligne précédente (_due à un caractère de nouvelle ligne_).

Enfin, les entrées de journalisation sont traitées en contenu HTML qui est ensuite envoyé au navigateur pour affichage.

Le code source complet est disponible sur Github si vous souhaitez jouer avec ou l'adapter pour une utilisation dans d'autres frameworks.

### **Conclusion**

Il est désormais plus facile et plus rapide de déboguer une application CodeIgniter — même en production. Faites passer le mot à vos amis et collègues au travail.

Je veux entendre parler de votre expérience (et de vos opinions) sur l'utilisation de la bibliothèque dans la section des commentaires. Merci !

Visitez le [lien Github](https://github.com/SeunMatt/codeigniter-log-viewer)