---
title: Comment héberger plusieurs noms de domaine et projets sur un seul serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-29T16:50:07.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FT9uL7NRg2iep6-e
tags:
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: servers
  slug: servers
- name: 'tech '
  slug: tech
- name: Web Hosting
  slug: web-hosting
seo_title: Comment héberger plusieurs noms de domaine et projets sur un seul serveur
seo_desc: 'By BinHong Lee

  NGINX is one magical tool


  _Photo by [Unsplash](https://unsplash.com/@imgix?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">imgix on <a href="https://unsplash.com?utm_source=medium&utm_medium=referral"
  re...'
---

Par BinHong Lee

#### NGINX est un outil magique

![Image](https://cdn-media-1.freecodecamp.org/images/0*FT9uL7NRg2iep6-e)
_Photo par [Unsplash](https://unsplash.com/@imgix?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">imgix</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Je possède plusieurs noms de domaine, et chacun héberge un projet différent. Pendant longtemps, tout ce qui nécessitait de l'hébergement était hébergé sur Heroku. Mais leur niveau gratuit peut être assez limité, et cela peut aussi devenir coûteux rapidement si vous payez pour chaque projet séparé. J'ai donc décidé d'explorer la possibilité de les regrouper tous ensemble en utilisant NGINX (recommandé par [Jane Manchun Wong](https://www.freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1/undefined)).

### Ressources requises

#### Serveur Privé Virtuel (VPS)

Vous aurez besoin d'un serveur virtuel tel que [DigitalOcean](https://www.freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1/undefined) ou EC2 par [AWS](https://www.freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1/undefined). Personnellement, j'utilise [Vultr](https://www.vultr.com/?ref=7358373) (voici le [lien sans parrainage](http://vultr.com/)) qui me coûte environ 2,50 $/mois.

#### Noms de domaine

Vous devrez enregistrer quelques noms de domaine. En supposant que vous les avez déjà, assurez-vous que vos noms de domaine pointent vers les serveurs de noms de votre VPS. Il devrait y avoir une section DNS dans le tableau de bord de votre service de noms de domaine où vous pouvez sélectionner "DNS personnalisé" ou quelque chose de similaire. Si vous n'êtes pas sûr des serveurs de noms de votre VPS, vous devriez pouvoir trouver cette information facilement grâce à une simple recherche de "serveur de noms" + nom du service VPS.

### Configuration de NGINX

#### Installation et configuration de base

_Référence de [How To Install Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04)_

Exécutez les commandes suivantes via SSH sur le VPS. Cela installera NGINX, définira les règles de pare-feu pour l'autoriser et configura NGINX pour qu'il démarre automatiquement au démarrage.

#### Configuration

_Référence de [Host Multiple Domains on One Server/IP with Apache or nginx](https://geekflare.com/multiple-domains-on-one-server-with-apache-nginx/)_

L'emplacement par défaut de virtual.conf devrait être /etc/nginx/conf.d/virtual.conf. Je recommande de sauvegarder le fichier par défaut avant de faire des modifications. (S'il n'existe pas, vous pouvez simplement le créer.) Modifiez le fichier pour qu'il ressemble à quelque chose comme ceci :

Voici quelques éléments à examiner :

* Bloc _server_ — Chacun de ceux-ci devrait représenter chaque domaine ou sous-domaine différent en utilisation.
* _root_ — C'est l'emplacement où les fichiers (HTML) sont chargés.
* _server_name_ — (sous)nom(s) de domaine qui devrait charger ces fichiers spécifiques.
* _proxy_redirect_ — dans les cas où vous redirigez un sous-domaine spécifique vers un serveur actif, vous voudrez ajouter ceci et mettre l'emplacement IP après. (Pour les serveurs locaux, soit [_http://127.0.0.1:port_](http://127.0.0.1:port) ou [_http://localhost:port_](http://localhost:port) devrait fonctionner comme prévu.)

```
sudo systemctl restart nginx
```

Une fois terminé, redémarrez le serveur pour que les nouvelles configurations soient chargées et appliquées.

### Clonage et liaison

Maintenant, rappelez-vous, puisque vous avez votre répertoire pointant vers /opt/htdocs/_nomDuSite_, votre première pensée pourrait être de cloner vos projets dans ces dossiers. Cela peut fonctionner, mais ce n'est pas idéal puisque de nombreuses opérations dans ces dossiers nécessitent un accès root pour vraiment faire quoi que ce soit.

Au lieu de cela, vous pouvez les cloner dans votre dossier utilisateur ou ailleurs comme vous le feriez normalement, puis créer un lien symbolique pour connecter le chemin à votre dossier de dépôt. Quelque chose comme ceci :

```
git clone git@github.com:binhonglee/binhonglee.github.io ~/website
sudo ln -s ~/website /opt/htdocs/binhong
```

Bien sûr, lorsque vous clonez un dossier de site statique Node.js (ReactJS, Angular ou Vue.js), vous voudrez les installer (`npm install`) et les construire (`npm run-script build`). Ensuite, liez le dossier _./build_ au lieu du niveau de base du dépôt cloné. (De même pour les sites Jekyll, mais utilisez le dossier _./_output_ à la place.) Quant aux serveurs actifs, assurez-vous simplement que votre serveur fonctionne sur le même port que celui indiqué dans le fichier de configuration.

### Configuration de HTTPS avec certbot

Grâce à Let's Encrypt, vous pouvez maintenant obtenir des certificats HTTPS gratuits et faciles. Avec l'introduction de certbot, tout est devenu encore plus facile !

_Référence de [How To Secure Nginx with Let's Encrypt on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)_

Exécutez simplement ce qui précède pour tous vos noms de domaine et sous-domaines et certbot s'occupera de tout. Si vous deviez renouveler les certificats, vous pouvez exécuter ce qui suit pour que certbot vous aide à renouveler votre certificat SSL.

```
sudo certbot renew --dry-run
```

### Mise à jour de tout

Maintenant que tout est en place et fonctionne, vous pourriez penser qu'il semble y avoir beaucoup de choses à retenir si/quand je dois mettre quelque chose à jour. Malheureusement, c'est un peu vrai, mais nous pouvons toujours faciliter les choses en ajoutant un script qui le fait pour nous.

Voici à quoi cela pourrait ressembler :

Merci d'avoir lu ! Faites-moi savoir si vous avez des questions dans les commentaires ci-dessous.

### À propos de moi

Au moment de l'écriture, je travaille chez Apple Inc. en tant qu'ingénieur linguistique Siri en tant que contractuel indépendant via AdvantisGlobal. Je passe beaucoup de mon temps libre à expérimenter et à construire de nouvelles choses avec des technologies que je trouve amusantes et intéressantes. Suivez mon voyage d'exploration [ici](https://binhong.me/blog) ou sur [GitHub](https://github.com/binhonglee).

### Autres références

* [nginx proxy pass redirects ignore port](https://serverfault.com/questions/363159/nginx-proxy-pass-redirects-ignore-port) sur [serverfault](https://serverfault.com)
* [Continue SSH background task/jobs when closing SSH](https://superuser.com/questions/632205/continue-ssh-background-task-jobs-when-closing-ssh) sur [superuser](https://superuser.com/)