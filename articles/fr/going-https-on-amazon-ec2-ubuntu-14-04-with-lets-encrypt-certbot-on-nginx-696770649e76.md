---
title: Utilisation de Certbot de Let's Encrypt pour obtenir HTTPS sur votre instance
  Amazon EC2 NGINX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-01T06:29:11.000Z'
originalURL: https://freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Cd2NBjQD8Luwbu1Z23n5QQ.png
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Utilisation de Certbot de Let's Encrypt pour obtenir HTTPS sur votre instance
  Amazon EC2 NGINX
seo_desc: 'By Karan Thakkar

  Let’s Encrypt is a new Certificate Authority which provides free SSL certificates
  (up to a certain limit per week). It came out of beta around a month back and is
  supported by a wide array of browsers.

  Certbot is the official Let’s E...'
---

Par Karan Thakkar

Let's Encrypt est une nouvelle autorité de certification qui fournit des certificats SSL gratuits (jusqu'à une certaine limite par semaine). Elle est sortie de la version bêta il y a environ un mois et est soutenue par une [large gamme de navigateurs](https://community.letsencrypt.org/t/which-browsers-and-operating-systems-support-lets-encrypt/4394).

**Certbot** est le client officiel de Let's Encrypt, développé par la [Electronic Frontier Foundation](https://www.eff.org/). Il simplifie le processus d'obtention et de déploiement automatique des certificats SSL/TLS pour votre serveur web.

Commençons.

### **Étape #1**

Assurez-vous d'avoir ouvert les ports 80 (HTTP) et 443 (HTTPS) dans le **Groupe de sécurité** de votre instance pour le public. Certbot utilisera ces ports pour établir des connexions lors de la génération de vos certificats.

Notez que j'ai passé beaucoup trop de temps à essayer de comprendre pourquoi je ne pouvais pas générer un certificat, alors que le seul problème était que je n'avais pas ouvert le port 443 dans le Groupe de sécurité de mon instance EC2.

![Image](https://cdn-media-1.freecodecamp.org/images/K0p2kFeBVDFczsI2Xh4PwHf7YJCLRaThGpDn)
_Paramètres **Inbound** dans le Groupe de sécurité EC2_

### Étape #2

Configurez l'**enregistrement CNAME** de votre domaine pour qu'il pointe vers le **DNS public** de votre instance EC2.

![Image](https://cdn-media-1.freecodecamp.org/images/IMIqPlaLo5Voda4d8iwhE1ox27vrr19CPemW)
_Valeur **Public DNS** dans la description de votre instance EC2_

![Image](https://cdn-media-1.freecodecamp.org/images/dRD-X8-N9a7wnq9Z81WtxO1sIV4B8V4cfMm0)
_Ce paramètre pointerait **api.mondomaine.com** vers mon instance EC2_

### Étape #3

Installez Certbot sur votre instance. Selon votre système d'exploitation et votre serveur, vous pouvez trouver comment l'installer sur la [page d'accueil de Certbot](https://certbot.eff.org). Pour NGINX sur **Ubuntu 14.04**, utilisez [ce guide](https://certbot.eff.org/#ubuntutrusty-nginx).

```
wget https://dl.eff.org/certbot-auto
chmod a+x certbot-auto
```

Exécutez cette commande dans votre répertoire personnel :

```
/home/ubtuntu
```

### Étape #4

Arrêtez tous les serveurs existants qui s'exécutent sur les ports 80 et 443, car ceux-ci sont utilisés par Certbot pour vérifier votre domaine et générer des certificats.

Vous pouvez redémarrer ces serveurs une fois que vous avez terminé la génération des certificats.

### **Étape #5**

Exécutez la commande suivante pour générer des certificats pour votre domaine :

```
./certbot-auto certonly --standalone -d xyz.votredomaine.com
```

Vous pouvez générer des certificats pour plusieurs domaines en utilisant cette approche.

### **Étape #6**

Modifiez votre configuration NGINX dans **/etc/nginx/nginx.conf** pour [activer SSL](http://nginx.org/en/docs/http/configuring_https_servers.html) :

```
http {
  ##
  # Paramètres de journalisation
  ##
  
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;
  
  server {
    listen 80;
    server_name xyz.votredomaine.com;
    location / {
      # Redirige toutes les requêtes http vers https
      return 301 https://$server_name$request_uri;
    }
  }
  
  server {
    listen 443 ssl;
    server_name xyz.votredomaine.com;
    ssl_certificate /etc/letsencrypt/live/xyz.votredomaine.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/xyz.votredomaine.com/privkey.pem;
    add_header Strict-Transport-Security "max-age=31536000";
    location / {
      proxy_pass http://127.0.0.1:3000;
    }
  }
  
}
```

L'en-tête [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/Security/HTTP_strict_transport_security) (HSTS) garantit que tous les liens internes qui ne sont pas en HTTPS seront [automatiquement redirigés](https://loune.net/2016/01/https-with-lets-encrypt-ssl-and-nginx) vers la version HTTPS pendant une session HTTPS.

### **Étape #7**

Enfin, rechargez votre configuration NGINX :

```
sudo service nginx reload
```

Félicitations ! Votre site **xyz.example.com** fonctionne désormais avec succès en HTTPS.

**NOTE** : Les certificats Let's Encrypt ne sont valables que pendant 3 mois après leur émission. Il est donc nécessaire de les renouveler tous les 3 mois. Voici comment vous pouvez automatiser cela [en utilisant une tâche cron](https://loune.net/2016/01/https-with-lets-encrypt-ssl-and-nginx/).

Si cet article vous a aidé, cliquez sur le bouton cœur ci-dessous. ? Et s'il ne vous a pas aidé, laissez un commentaire pour me dire comment je peux l'améliorer.

PS : Merci à [Narendra N Shetty](https://www.freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76/undefined) pour la relecture et les suggestions.

![Image](https://cdn-media-1.freecodecamp.org/images/lcR6uQdCciRYcGIs1Pl2XihJOQeYci-1axVE)

[Karan Thakkar](https://twitter.com/geekykaran) est le responsable Frontend chez [Crowdfire](https://www.freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76/undefined) — _Votre assistant marketing super-intelligent_. Son [article](https://bit.ly/hackingtwitter) a été précédemment [mis en avant](https://bit.ly/geekyonhuffpo) sur [The Huffington Post](https://www.freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76/undefined). Il aime essayer de nouvelles technologies pendant son temps libre et a développé [Tweetify](https://karanjthakkar.com/projects/tweetify) (en utilisant React Native) et [Show My PR's](https://showmyprs.com) (en utilisant Golang).

Autres articles écrits par lui :

[**Comment je suis passé de 300 à 5k abonnés en seulement 3 semaines**](https://blog.markgrowth.com/how-i-grew-from-300-to-5k-followers-in-just-3-weeks-2436528da845)  
[_#GrowthHacking mon compte Twitter pour @Crowdfire Twitter Premier League_blog.markgrowth.com](https://blog.markgrowth.com/how-i-grew-from-300-to-5k-followers-in-just-3-weeks-2436528da845)[**Un guide illustré pour configurer votre site web en utilisant Github & Cloudflare**](https://medium.freecodecamp.org/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465)  
[_Facile à configurer, déploiement instantané, HTTPS gratuit, support HTTP2/SPDY, redirection personnalisée, expiration du cache du navigateur, HTTP sécurisé..._medium.freecodecamp.org](https://medium.freecodecamp.org/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465)