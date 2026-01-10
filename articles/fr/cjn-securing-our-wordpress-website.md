---
title: Sécuriser notre site WordPress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-20T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-securing-our-wordpress-website
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/SSL-Certificate-https-1.jpg
tags:
- name: '#ssl'
  slug: hash-ssl
- name: '#wordpress'
  slug: hash-wordpress
- name: '#hosting'
  slug: hash-hosting
seo_title: Sécuriser notre site WordPress
seo_desc: 'By Clark Jason Ngo

  First step looking for free SSL

  Search for “hostgator free ssl”:

  HostGator Free SSL " HostGator.com Support Portal_We have progressively and methodically
  gone through the HostGator cPanel servers to ensure the free SSL certificates...'
---

Par Clark Jason Ngo

# Première étape : rechercher un SSL gratuit

Recherchez « hostgator free ssl » :

[**HostGator Free SSL « Portail d'assistance HostGator.com**](https://support.hostgator.com/articles/ssl-certificates/hostgator-free-ssl)  
[_Nous avons progressivement et méthodiquement passé en revue les serveurs cPanel de HostGator pour garantir les certificats SSL gratuits..._support.hostgator.com](https://support.hostgator.com/articles/ssl-certificates/hostgator-free-ssl)

Ensuite, j'ai reçu une suggestion de plugin WordPress pour SSL :

[**Really Simple SSL**](https://wordpress.org/plugins/really-simple-ssl/)  
[_Aucune configuration requise ! Vous avez seulement besoin d'un certificat SSL, et ce plugin fera le reste._wordpress.org](https://wordpress.org/plugins/really-simple-ssl/)

Je me suis connecté en tant qu'administrateur sur notre site WordPress.

J'ai installé et activé le plugin Really Simple SSL.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l82QH0ls5ERIOqTBGWPgTQ.png)

En vérifiant l'icône de **cadenas** dans l'adresse web, il était indiqué « contenu non sécurisé ».

J'ai inspecté le site WordPress et j'ai eu un avertissement de **contenu mixte** provenant de l'image de fond que nous avons.

Cela ressemblait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_-JFxND1MBIL0ySeTnvmHw.png)

J'ai recherché sur Google « fixing Mixed Content » :

[**Prévenir le contenu mixte | Fondamentaux du Web | Développeurs Google**](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content)  
[_Trouver et corriger le contenu mixte est une tâche importante, mais elle peut être chronophage. Ce guide discute de certains outils..._developers.google.com](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content)

J'ai résolu le problème de **contenu mixte** en supprimant l'image de fond et en la réimportant.

Certaines images n'ont pas été corrigées en réimportant les images immédiatement.

Il était indiqué qu'une image avait été importée de manière non sécurisée (en http).

J'ai suivi l'option 1 de ce guide : [https://managewp.com/blog/wordpress-ssl-settings-and-how-to-resolve-mixed-content-warnings](https://managewp.com/blog/wordpress-ssl-settings-and-how-to-resolve-mixed-content-warnings)

### Option 1 : Forcer toutes les pages en HTTPS

![Image](https://cdn-media-1.freecodecamp.org/images/1*Me0yLoTfqvYz9lzXqAbdAA.png)

Après cela, j'ai réimporté les images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hIs4N8RQ2YKf1p1gOw0pdQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NKfT_aw-JG4U6xVRZJEPKw.png)

Merci d'avoir lu !

## Mise à jour. J'ai récemment mis à jour un certificat SSL pour un site WordPress hébergé chez GoDaddy.



1) J'ai recherché "buy godaddy ssl"

2) J'ai suivi ce lien [https://www.godaddy.com/web-security/ssl-certificate](https://www.godaddy.com/web-security/ssl-certificate)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-163.png)

3) J'ai été redirigé vers ma page de facturation et j'ai cliqué sur acheter

4) Allez sur la page Mes Produits et activez votre SSL

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-164.png)

5) Cliquez sur WordPress géré, choisissez le site Web où vous souhaitez installer le SSL et cliquez sur Gérer

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-165.png)

6) Cliquez sur Installer. Une fois l'installation réussie, il devrait afficher Activé.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-166.png)

7) Vérifiez votre site Web. Il devrait maintenant avoir une icône de cadenas, ce qui signifie qu'il est sécurisé. =)

%[https://www.youtube.com/watch?v=QJ8CkBMIvro&fbclid=IwAR2sBDELfC8ci-lfRU3VXcsjYgYn_qMy2ClxLGuZelJclqY6PfIXDZCbibY]

[**Clark Jason Ngo - Assistant d'enseignement diplômé - Institut de technologie - City University of Seattle |...**](https://www.linkedin.com/in/clarkngo/)  
[_Voir le profil de Clark Jason Ngo sur LinkedIn, la plus grande communauté professionnelle au monde. Clark Jason a 9 emplois répertoriés..._www.linkedin.com](https://www.linkedin.com/in/clarkngo/)