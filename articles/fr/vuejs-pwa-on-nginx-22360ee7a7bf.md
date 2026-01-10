---
title: Comment créer une PWA VueJS sur une infrastructure NGINX haute performance
  et sécurisée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T11:20:23.000Z'
originalURL: https://freecodecamp.org/news/vuejs-pwa-on-nginx-22360ee7a7bf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mbz297hBc_ymcQZWcFP45A.png
tags:
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Comment créer une PWA VueJS sur une infrastructure NGINX haute performance
  et sécurisée
seo_desc: 'By Thomas Reinecke

  I’ve been pretty curious ever since one of my developers presented the concept of
  Progressive Web Apps (PWAs) sometime a few months back to me. And finally I found
  the time to get my hands a little dirty on it :-)

  This article desc...'
---

Par Thomas Reinecke

Je suis assez curieux depuis qu'un de mes développeurs m'a présenté le concept des **Progressive Web Apps** (PWA) il y a quelques mois. Et finalement, j'ai trouvé le temps de m'y essayer :-)

Cet article décrit mes premiers pas et une introduction de haut niveau aux PWA basées sur le framework élégant [VueJS](https://vuejs.org/), et se concentre principalement sur son déploiement sur un serveur [nginx](https://www.nginx.com/) bien sécurisé.

Voici quelques lectures que j'ai utilisées pour plonger dans ce sujet :

[**Progressive Web Apps | Web | Google Developers**](https://developers.google.com/web/progressive-web-apps/)  
[_Lighthouse, un outil open-source et automatisé pour améliorer la qualité de vos Progressive Web Apps, élimine une grande partie...developers.google.com](https://developers.google.com/web/progressive-web-apps/)[**Getting started with PWA using Vue - Pusher Blog**](https://blog.pusher.com/getting-started-pwa-vue/)  
[_Dans ce tutoriel, découvrez comment créer une application de liste de livres avec des applications web progressives en utilisant Vue...blog.pusher.com](https://blog.pusher.com/getting-started-pwa-vue/)

Voici une architecture approximative du scénario que nous allons configurer. Comme vous pouvez le voir, il s'agit davantage d'une configuration traditionnelle sur site où je suppose que vous possédez un domaine configuré et pointant vers votre serveur racine. Dans cet article, je ne couvre pas les déploiements basés sur le cloud :

![Image](https://cdn-media-1.freecodecamp.org/images/T-Dt47h5nkWccQI90G4YG5diB99cLw177VQm)
_architecture de base_

### Préparation et installation de nginx

Commençons par quelques travaux préparatoires pour configurer l'infrastructure que nous utiliserons pour le déploiement plus tard :

* Si vous ne l'avez pas encore, procurez-vous un domaine et un serveur racine et configurez les enregistrements DNS de votre domaine (pour IPv4 et IPv6) pour qu'ils pointent vers votre serveur. J'utiliserai mon site personnel [www.thomas-reinecke.de](http://www.thomas-reinecke.de) comme exemple ici.
* Sur votre serveur, et je suppose que vous avez un accès root/sudo, [installez nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04) (exemple pour les distributions linux basées sur apt comme debian ou ubuntu).

```
sudo apt-get install nginx
```

* créez votre définition de serveur sur _/etc/nginx/sites-available/default_ qui peut être assez basique pour l'instant

```
server {    server_name www.thomas-reinecke.de thomas-reinecke.de;    root /server/thomasreinecke/nginx;}
```

* testez votre configuration nginx pour vous assurer que sa syntaxe est correcte avant de continuer

```
> nginx -t
```

```
nginx: the configuration file /etc/nginx/nginx.conf syntax is oknginx: configuration file /etc/nginx/nginx.conf test is successful
```

### Configurer et sécuriser nginx

Puisque notre plan est d'utiliser les service workers PWA, votre application web doit fonctionner uniquement en HTTPS (et idéalement aussi en HTTP/2). De plus, nous devrions certainement soutenir [les efforts de Google pour imposer un web plus sécurisé](https://security.googleblog.com/2018/02/a-secure-web-is-here-to-stay.html).

> À partir de juillet 2018 avec la sortie de Chrome 68, Chrome marquera tous les sites HTTP comme "non sécurisés".

Heureusement, [Let's Encrypt](https://letsencrypt.org/) fournit des certificats SSL gratuits pour votre serveur web, y compris le renouvellement automatique, et tout ce que vous avez à faire est de le sécuriser correctement.

* installez **certbot** de Let's Encrypt

```
sudo apt-get install certbot python3-certbot python-certbot-nginx python3-certbot-nginx
```

* Sur la base de la configuration initiale de votre serveur nginx que nous avons faite précédemment, **certbot** fournit un moyen assez confortable de créer un certificat pour votre site, y compris une reconfiguration de bout en bout de votre service nginx pour supporter SSL et rediriger le trafic HTTP vers HTTPS.

```
sudo certbot --nginx -d thomas-reinecke.de -d www.thomas-reinecke.de
```

* Il vous demandera si vous souhaitez que certbot reconfigure votre instance nginx.

```
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.--------------------------------------------------------------------1: No redirect - Make no further changes to the webserver configuration.2: Redirect - Make all requests redirect to secure HTTPS access. Choose this fornew sites, or if you're confident your site works on HTTPS. You can undo thischange by editing your web server's configuration.--------------------------------------------------------------------Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
```

* Choisissez la 2ème option et laissez-le faire. Attendez-vous à ce que votre configuration de site dans _/etc/nginx/sites-available/default_ ressemble à ceci par la suite :

```
# Configuration HTTPS de mon siteserver {  server_name thomas-reinecke.de www.thomas-reinecke.de;  root /server/thomasreinecke/nginx;
```

```
  location / {    index index.html index.htm;  }
```

```
  listen <votre_IP>:443 ssl http2;   ssl_certificate <chemin_vers_fullchain.pem>;   ssl_certificate_key <chemin_vers_privkey.pem>;   include /etc/letsencrypt/options-ssl-nginx.conf;   ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; }
```

```
# Configuration HTTP de mon site, dans tous les cas redirigeant vers HTTPSserver {  if ($host = www.thomas-reinecke.de) {    return 301 https://$host$request_uri;  } 
```

```
  if ($host = thomas-reinecke.de) {    return 301 https://$host$request_uri;  } 
```

```
  listen <votre_IP>:80 default;  server_name thomas-reinecke.de www.thomas-reinecke.de;  return 404; }
```

* J'ai ajouté l'option **http2** dans la zone de configuration HTTPS de votre site, cela ne vient pas de certbot.

Plus de détails sur cette procédure (y compris ce que vous devriez faire pour renouveler votre certificat) peuvent être trouvés [ici](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04).

Il est maintenant temps de démarrer votre serveur nginx, alors créons un simple index.html et redémarrons nginx pour le prendre en compte.

```
echo "Hello World!" > /server/thomasreinecke/nginx/index.htmlsudo systemctl reload nginx
```

Félicitations, vous devriez maintenant avoir votre page web sécurisée en ligne. Tout accès à HTTP sera automatiquement redirigé vers HTTPS. Vous pouvez maintenant le tester sur [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/) et vous obtiendrez une note **A** :) N'est-ce pas génial ?

![Image](https://cdn-media-1.freecodecamp.org/images/2ESrJyGkNj1Y-WYQq3Xp8LTuldlwnrTjuUUn)

### Créer votre PWA VueJS et la déployer sur nginx

Maintenant que nous avons l'infrastructure de déploiement cible prête, il est temps de créer votre première PWA basée sur le CLI de VueJS.

```
# installer vue cli, passez si vous l'avez déjànpm install -g vue-cli
```

```
# créer une application vue basée sur le modèle pwavue init pwa <nom_de_votre_application>
```

Pour les quelques questions que ce script vous pose, fournissez le nom de votre projet et pour le reste, prenez simplement les valeurs par défaut. Je ne vais pas plonger dans les changements réels de l'application qui vient d'être créée sur la base du modèle. Au lieu de cela, concentrons-nous sur l'aspect de déploiement et d'exploitation pour exécuter cela sur votre infrastructure nginx sécurisée. Comme prochaines étapes, construisez votre application, puis déplacez son dossier dist dans votre racine web nginx :

```
# construire votre application pwa vuejscd <dossier de votre application>npm run build
```

```
# copier votre dossier dist sur votre serveur exécutant nginxscp -r dist/* <votre_serveur>:/server/thomasreinecke/nginx/
```

```
# sur votre serveur, redémarrez nginx pour rafraîchirsudo systemctl reload nginx
```

Vous devriez maintenant avoir votre PWA VueJS en cours d'exécution sur votre serveur nginx :

![Image](https://cdn-media-1.freecodecamp.org/images/xCyJM0HpJUk4RVI6UTAqTt6CSzHCBLhdShOf)

Lorsque vous accédez à cette page avec une URL HTTP habituelle, vous remarquerez une redirection vers HTTPS, ce qui est exactement ce que nous voulions. Il est maintenant temps d'exécuter **Google Lighthouse** contre notre site et de voir comment cela se passe. Pour plus de détails :

[**Lighthouse | Tools for Web Developers | Google Developers**](https://developers.google.com/web/tools/lighthouse/)  
[_Apprenez comment configurer Lighthouse pour auditer vos applications web._developers.google.com](https://developers.google.com/web/tools/lighthouse/)

Ouvrez Chrome > utilisez ses outils de développement > Audits > Exécuter les audits. Voici ce que nous obtenons de cette configuration — n'est-ce pas fantastique !?

![Image](https://cdn-media-1.freecodecamp.org/images/SD-lwY9PNX3VtjWBxAw3BglL98MrZpaG7CoA)

### Conclusion

Dans cet article, j'ai montré comment configurer un environnement sécurisé pour exécuter une Progressive Web App basée sur VueJS sur un serveur nginx. Je dois admettre que je pensais que cela serait quelque peu plus difficile, mais la réalité était : cela ne m'a pas pris plus de ~3 heures au total pour y parvenir à partir de zéro, ce qui était assez surprenant.

Configurer une infrastructure sécurisée et haute performance n'est vraiment pas une grosse affaire et j'encourage tout le monde qui traite avec des déploiements sur site à se plonger dans cela.