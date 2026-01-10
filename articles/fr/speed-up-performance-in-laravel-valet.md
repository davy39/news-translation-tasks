---
title: Laravel Valet Performance – Comment prévenir les erreurs 504 et accélérer Valet
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2023-01-02T23:12:30.000Z'
originalURL: https://freecodecamp.org/news/speed-up-performance-in-laravel-valet
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-jonathan-petersson-399636.jpg
tags:
- name: error
  slug: error
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Laravel Valet Performance – Comment prévenir les erreurs 504 et accélérer
  Valet
seo_desc: "Last week, I decided to install Laravel Valet on my Mac. But after the\
  \ installation, the performance of the microservice architecture application I had\
  \ it on was quite slow. \nI wondered if it was an M1 issue or because I had yet\
  \ to shut the machine d..."
---

La semaine dernière, j'ai décidé d'installer Laravel Valet sur mon Mac. Mais après l'installation, la performance de l'application d'architecture microservice que j'avais était assez lente. 

Je me demandais si c'était un problème avec le M1 ou parce que je n'avais pas encore éteint la machine. J'ai éteint, et le problème a persisté. Et je n'ai rien trouvé en ligne indiquant que c'était un problème avec le M1. Alors, comment pourrais-je le résoudre ?

**Dans ce tutoriel, vous apprendrez :**

* Pourquoi l'erreur 504 se produit-elle ?
* Qu'est-ce que Laravel Valet et comment fonctionne-t-il ?
* Les commandes Valet que vous devriez connaître
* Comment corriger l'erreur 504 et accélérer les performances dans Valet

## Pourquoi l'erreur 504 se produit-elle ?



![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-145.png)
_Erreur 504 Nginx_

L'erreur 504, également connue sous le nom de "Gateway timeout", est une erreur qui se produit lorsqu'un serveur met plus de temps que d'habitude à répondre à une requête HTTP. Cela l'empêche de compléter le cycle de la requête. 

Le Gateway timeout est une erreur côté serveur causée par plusieurs choses. Elle peut résulter de problèmes de connectivité réseau lorsque le serveur dépasse la limite par défaut de **256M** ou un temps d'exécution de **60 secondes**, un serveur surchargé, un pare-feu, etc. 

Cette erreur se produit également avec les serveurs locaux, tels que XAMPP, WAMP et Valet, pendant le cycle de développement local. 

Cet article vous aidera à résoudre ce problème sur Valet en ajoutant quelques configurations pour accélérer le cycle de vie des requêtes du serveur.

## Qu'est-ce que Laravel Valet et comment fonctionne-t-il ?

Laravel Valet est un environnement de développement pour macOS, Windows et autres systèmes d'exploitation. Une fois installé, Valet exécute des processus Nginx en arrière-plan lorsque votre ordinateur portable est allumé.

Contrairement à d'autres environnements de développement comme XAMPP et WAMP, vous devez démarrer manuellement votre serveur chaque fois que vous commencez à travailler. Valet utilise ensuite DnsMasq pour proxyfier toutes les applications garées vers un domaine `.test`. 

Ainsi, par exemple, vous accéderiez sur un serveur XAMPP à `http://localhost/application` mais sur Valet, vous feriez `http://application.test`, et cela pointera vers l'endroit où l'application est installée. 

Travailler avec Valet signifie que vous n'avez pas à mettre toutes les applications dans un répertoire htdocs ou www. Au lieu de cela, n'importe quel répertoire aléatoire que vous créez fonctionnera parfaitement dans Valet. 

## Commandes Valet utiles que vous devriez connaître :

* **`valet park` :** Enregistre toutes les applications/sites dans un répertoire et les expose avec le domaine .test.

```
cd ~/project_directory
valet park 
```

* **`valet parked` :** Donne un tableau récapitulatif de tous les sites enregistrés. Des informations comme le nom du site, SSL, URL et chemin sont disponibles.

```
cd ~/project_directory
valet parked
```

* **`valet secure` :** Sécurise votre application avec un certificat SSL et rend le site accessible via HTTPS.

```
cd ~/project_directory/site
valet secure
```

* **`valet unsecure` :** Utilisez cette commande pour désécuriser votre site et revenir à la diffusion via HTTP.

```
cd ~/project_directory/site
valet unsecure 
```

* **`valet isolate` :** Isole un site particulier et le fait fonctionner sur une version différente de PHP qui n'est pas la version installée globalement. Vous pouvez exécuter `php -v` dans le terminal pour voir la version. Mais si certaines de vos applications veulent rétrograder ou mettre à niveau, vous devriez utiliser la commande isolate et spécifier la version dont vous avez besoin. La commande isolate ci-dessous force le site à utiliser la version PHP 7.4 :

```
cd ~/project_directory/site
valet isolate @php7.4
```

* **`valet unisolate` :** Rétablit un site à la version PHP installée globalement.

```
cd ~/project_directory/site
valet unisolate
```

* **`valet restart` :** La commande restart assure que tous les services Valet sont redémarrés. Elle est utile lorsque les configurations sont modifiées, mises à jour et installées.

```
cd ~/project_directory/site
valet restart
```

* **`valet -v` :** Cette commande aide à vérifier la version actuelle de Valet. Non seulement cela, mais la commande affiche également une liste de toutes les commandes disponibles et des descriptions de ce qu'elles font dans Valet.

```
~/project_directory/site
valet -v
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-26-at-11.33.10.png)
_Commandes disponibles de Valet_

## Comment accélérer les performances dans Valet

Dans le terminal, nous devons créer un fichier `www.conf` dans un répertoire, puis ajouter les paramètres de configuration dont nous avons besoin.

Obtenez votre version globale de PHP et copiez-la comme ceci :

```
php -v
```

Accédez au répertoire et remplacez le 7.4 par la version PHP que vous avez copiée précédemment.

```
cd /opt/homebrew/etc/php/7.4/php-fpm.d
```

Créez un fichier `www.conf` comme ceci :

```
touch www.conf

```

Ouvrez le fichier afin de pouvoir ajouter les paramètres de configuration de Valet :

```
open -a TextEdit www.conf
```

La commande ouvre le fichier `www.conf` dans votre éditeur de texte et vous pouvez mettre à jour le fichier avec ces paramètres :

```
pm.max_children = 200
pm.start_servers = 20
pm.min_spare_servers = 10
pm.max_spare_servers = 20
pm.process_idle_timeout = 10s
pm.max_requests = 500
```

Enregistrez et fermez le fichier depuis l'éditeur de texte.

Passons en revue chaque ligne que nous avons ajoutée au fichier `www.conf` :

* **`pm`** est un acronyme pour process manager, et le paramètre aura un impact sur la manière dont le gestionnaire de processus contrôle chaque processus enfant. Les valeurs possibles disponibles pour nous incluent static, on-demand et dynamic.
* **pm.max_children** est une option statique, indiquant le nombre maximum de processus enfants, que nous avons fixé à 200.
* **`pm.start_servers, pm.max_spare_servers`** et `pm.min_spare_servers` : Ce sont des valeurs dynamiques, et les processus enfants sont définis dynamiquement en fonction des directives du serveur – c'est-à-dire start_servers = 20, min_spare_servers = 10 et max_spare_servers = 20.
* **pm.process_idle_timeout** : le temps total pris pour une requête inactive non traitée pour être tuée/terminée est fixé à une valeur par défaut de 10 secondes (s). D'autres unités peuvent être estimées en minutes (m), heures (h) ou jours (d).
* **pm.max_requests** : Cela fait référence au nombre maximum de requêtes qu'un processus enfant peut gérer à un moment donné avant d'être tué/terminé. Si la requête exécute le maximum, elle devient inactive, et le pm s'en débarrasse.

Enfin, redémarrez tous les services depuis le terminal en utilisant la commande sudo brew. Remarquez à nouveau le 7.4 – c'est à cause de ma version globale de PHP.

```
sudo brew services restart php@7.4
```

Vous pouvez maintenant dire adieu à l'erreur 504 et aux performances lentes de Valet dans votre environnement local.

## Conclusion

Dans cet article, vous avez appris à travailler avec Laravel Valet et comment configurer toutes les configurations Valet. Vous avez également appris comment assurer un environnement de développement rapide et vous débarrasser des erreurs persistantes de délai d'attente de la passerelle 504. 

Continuez à apprendre et bon codage !

Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/suleolanrewaju/) et [Twitter](https://twitter.com/bigdevlarry).