---
title: 'SimpleHTTPServer Expliqué : Comment Envoyer des Fichiers en Utilisant Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T23:14:00.000Z'
originalURL: https://freecodecamp.org/news/simplehttpserver-explained-how-to-send-files-using-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e01740569d1a4ca3ad4.jpg
tags:
- name: Python
  slug: python
seo_title: 'SimpleHTTPServer Expliqué : Comment Envoyer des Fichiers en Utilisant
  Python'
seo_desc: "As a web developer, there will be a point when you need to create your\
  \ own local web server. \nMaybe it's because you'll be on a flight and want to work\
  \ on your project, far from internet service. Or perhaps you just want a quick way\
  \ to access files f..."
---

En tant que développeur web, il arrivera un moment où vous devrez créer votre propre serveur web local. 

Peut-être parce que vous serez en vol et voudrez travailler sur votre projet, loin du service internet. Ou peut-être voulez-vous simplement un moyen rapide d'accéder à des fichiers depuis un autre ordinateur sur votre réseau domestique. 

Quoi qu'il en soit et quelle que soit la manière dont le besoin se présente, la configuration d'un serveur HTTP local est une compétence utile à avoir.

### Qu'est-ce qu'un serveur HTTP ?

Simplement dit, un serveur HTTP ou serveur web est un processus en cours d'exécution sur une machine qui écoute les requêtes entrantes et sert des pages web. 

Par exemple, lorsque vous tapez `https://www.freecodecamp.org/news/` dans votre navigateur, il y a un serveur quelque part qui écoute cette requête. En réponse, il envoie des données pour que votre navigateur puisse rendre la page freeCodeCamp Developer News.

Bien sûr, il se passe beaucoup plus de choses en coulisses, mais pour les besoins de ce tutoriel, c'est tout ce que vous devez vraiment savoir.

### Comment configurer un serveur HTTP local

1. [Installer Python](https://www.freecodecamp.org/news/best-python-tutorial/#installation)
2. Ouvrez votre invite de commande ou terminal et exécutez `python -V`
3. Allez dans le répertoire de votre projet avec `cd` sur les systèmes *nix ou MacOS ou `CD` pour Windows
4. Exécutez les commandes suivantes pour démarrer un serveur HTTP local :

```
# Si python -V retourne 2.X.X
python -m SimpleHTTPServer

# Si python -V retourne 3.X.X
python3 -m http.server

# Notez que sur Windows, vous devrez peut-être exécuter python -m http.server au lieu de python3 -m http.server
```

Vous remarquerez que les deux commandes semblent très différentes – l'une appelle `SimpleHTTPServer` et l'autre `http.server`. Cela est simplement dû au fait que le module `SimpleHTTPServer` a été intégré dans `http.server` de Python dans Python 3. Ils fonctionnent tous les deux de la même manière.

Maintenant, lorsque vous allez sur [`http://localhost:8000/`](http://localhost:8000/), vous devriez voir une liste de tous les fichiers dans votre répertoire. Ensuite, vous pouvez simplement cliquer sur le fichier HTML que vous souhaitez voir.

Gardez simplement à l'esprit que `SimpleHTTPServer` et `http.server` ne sont que pour tester des choses localement. Ils ne font que des vérifications de sécurité très basiques et ne devraient pas être utilisés en production.

### Comment envoyer des fichiers localement

Pour configurer un système NAS (Network Attached Storage) rapide et simple :

1. Assurez-vous que les deux ordinateurs sont connectés au même réseau via LAN ou WiFi
2. Ouvrez votre invite de commande ou terminal et exécutez `python -V` pour vous assurer que Python est installé
3. Allez dans le répertoire dont vous voulez partager le fichier en utilisant la commande cd (changer de répertoire).
4. Allez dans le répertoire avec le fichier que vous voulez partager en utilisant `cd` sur les systèmes *nix ou MacOS ou `CD` pour Windows
5. Démarrez votre serveur HTTP avec soit `python -m SimpleHTTPServer` soit `python3 -m http.server`
6. Ouvrez un nouveau terminal et tapez `ifconfig` sur *nix ou MacOS ou `ipconfig` sur Windows pour trouver votre adresse IP

Maintenant, sur le second ordinateur ou appareil :

1. Ouvrez le navigateur et tapez l'adresse IP de la première machine, avec le port 8000 : `http://[adresse IP]:8000`

Une page s'ouvrira montrant tous les fichiers dans le répertoire partagé depuis le premier ordinateur. Si la page met trop de temps à charger, vous devrez peut-être ajuster les paramètres du pare-feu sur le premier ordinateur.