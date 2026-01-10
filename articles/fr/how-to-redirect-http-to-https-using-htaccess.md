---
title: Comment rediriger le trafic HTTP vers HTTPS avec .htaccess
date: '2019-06-13T12:10:15.000Z'
author: Bolaji Ayodeji
authorURL: https://www.freecodecamp.org/news/author/bolajiayodeji/
originalURL: https://freecodecamp.org/news/how-to-redirect-http-to-https-using-htaccess
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca210740569d1a4ca5257.jpg
tags:
- name: http
  slug: http
- name: https
  slug: https
- name: openssl
  slug: openssl
- name: servers
  slug: servers
- name: SSL
  slug: ssl
seo_desc: Chrome and Firefox have started showing insecure warnings on sites without
  SSL certificates. Without SSL, your website will show insecure to the visitors.
  Therefore, using an SSL-encrypted connection for safety, accessibility or PCI compliance
  reason...
---


Chrome et Firefox ont commencé à afficher des avertissements de sécurité sur les sites sans [certificats SSL][1]. Sans SSL, votre site web apparaîtra comme non sécurisé aux yeux des visiteurs. Par conséquent, l'utilisation d'une connexion chiffrée par SSL pour des raisons de sécurité, d'accessibilité ou de conformité PCI est nécessaire. Il devient donc très important de rediriger le trafic de HTTP vers HTTPS.

<!-- more -->

![0*wUTFJrRSM2vh1H7v](https://cdn-media-1.freecodecamp.org/images/0*wUTFJrRSM2vh1H7v.jpg)

### Qu'est-ce que le SSL ?

Le SSL (Secure Sockets Layer) est un protocole de sécurité standard permettant d'établir des liaisons chiffrées entre un serveur web et un navigateur dans le cadre d'une communication en ligne.

L'utilisation de la technologie SSL garantit que toutes les données transmises entre le serveur web et le navigateur restent chiffrées.

Un **certificat SSL** est nécessaire pour créer une connexion SSL. Vous devrez fournir tous les détails concernant l'identité de votre site web et de votre entreprise au moment où vous choisirez d'activer le SSL sur votre serveur web. À la suite de cela, deux clés cryptographiques sont créées : une clé privée (Private Key) et une clé publique (Public Key).

[_En savoir plus : Pourquoi le SSL est-il critique ?_][2]

Afin de forcer votre trafic web à utiliser le HTTPS, modifiez les codes dans le **fichier .htaccess.**

Avant de passer à la redirection de HTTP vers HTTPS, voici comment vous pouvez modifier le fichier .htaccess. Si vous savez déjà comment faire, passez directement aux étapes de redirection.

### Modifier le fichier .htaccess

Le fichier .htaccess contient des instructions/directives qui indiquent au serveur comment agir dans certains scénarios et affectent directement le fonctionnement de votre site web. Directives courantes dans le fichier .htaccess :

-   Redirections
-   Réécriture d'URLs (URL Rewriting)

**Façons de modifier un fichier .htaccess :**

1.  Modifiez le fichier sur votre ordinateur et téléchargez-le sur le serveur via FTP.
2.  Utilisez le mode « Édition » de votre programme FTP qui vous permet de modifier un fichier à distance.
3.  Utilisez un éditeur de texte et SSH pour modifier le fichier.
4.  Utilisez le Gestionnaire de fichiers dans **cPanel** pour modifier le fichier.

### Modifier le fichier .htaccess dans le Gestionnaire de fichiers cPanel

**Note :** Sauvegardez votre site web au cas où quelque chose tournerait mal.

1.  Connectez-vous à cPanel.
2.  Fichiers > Gestionnaire de fichiers > Racine du document (Document Root) pour :
3.  Sélectionnez maintenant le nom de domaine auquel vous souhaitez accéder.
4.  Cochez « Afficher les fichiers cachés (dotfiles) ».
5.  Cliquez sur « Go ».
6.  Après l'ouverture d'un nouvel onglet ou d'une nouvelle fenêtre, recherchez le fichier .htaccess.
7.  Faites un clic droit sur le fichier .htaccess et cliquez sur « Code Edit » dans le menu.
8.  Une boîte de dialogue peut apparaître pour vous interroger sur l'encodage. Cliquez sur le bouton « Edit » pour continuer.
9.  Modifiez le fichier.
10. « Save Changes » (Enregistrer les modifications) une fois terminé.
11. Testez votre site web pour vous assurer que l'opération a été effectuée correctement. En cas d'erreur, restaurez la version précédente et réessayez.
12. Une fois terminé, cliquez sur « Close » pour fermer la fenêtre.

### Redirection de HTTP vers HTTPS

#### 1\. Rediriger tout le trafic Web

Si vous avez déjà du code dans votre .htaccess, ajoutez ce qui suit :

```
RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]
```

#### 2\. Rediriger uniquement un domaine spécifique

Pour rediriger un domaine spécifique afin qu'il utilise le HTTPS, ajoutez ce qui suit :

```
RewriteEngine On
RewriteCond %{HTTP_HOST} ^yourdomain\.com [NC]
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]
```

#### 3\. Rediriger uniquement un dossier spécifique

Pour rediriger vers HTTPS sur un dossier spécifique, ajoutez ce qui suit :

```
RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteCond %{REQUEST_URI} folder
RewriteRule ^(.*)$ https://www.yourdomain.com/folder/$1 [R,L]
```

Note : Remplacez _`“yourdomain”`_ par votre nom de domaine réel partout où cela est nécessaire. De même, dans le cas du dossier, remplacez _`/folder`_ par le nom réel du dossier.

Vous pensez que cela a été utile ? Partagez cet article pour aider d'autres personnes à passer au HTTPS.

![0*P6EKtlMMzyIXNRMw](https://cdn-media-1.freecodecamp.org/images/0*P6EKtlMMzyIXNRMw.png)

[1]: https://www.instantssl.com/ssl.html
[2]: https://www.sslrenewals.com/blog/why-is-ssl-important-benefits-of-using-ssl-certificate