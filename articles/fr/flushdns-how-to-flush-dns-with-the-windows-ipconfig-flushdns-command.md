---
title: flushdns – Comment vider le cache DNS avec la commande Windows ipconfig /flushdns
date: '2022-04-07T03:41:13.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/flushdns-how-to-flush-dns-with-the-windows-ipconfig-flushdns-command
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/domain-names-1772240_1920.png
tags:
- name: dns
  slug: dns
- name: networking
  slug: networking
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_desc: 'You''ve probably noticed that, after visiting a website for the first time,
  the website loads much quicker the next time you visit.

  This is because your operating system, or browser in the case of Google Chrome,
  cache IP addresses and DNS (Domain Name...'
---


Vous avez probablement remarqué que, après avoir visité un site web pour la première fois, le site se charge beaucoup plus rapidement la fois suivante.

<!-- more -->

C'est parce que votre système d'exploitation, ou votre navigateur dans le cas de Google Chrome, met en cache les adresses IP et les informations DNS (Domain Name System) de tous les sites web que vous visitez. Le cache DNS contient :

-   l'adresse du site web ou le nom d'hôte, techniquement appelé données de ressource (rdata)
-   le nom de domaine du site web
-   le type d'enregistrement (IPv4 ou IPv6)
-   la validité du cache ou TTL (time to live)

Lorsque le TTL expire, le cache est effacé et le DNS est vidé automatiquement. Mais il arrive que vous ne souhaitiez pas attendre des heures ou des jours que le TTL expire, et que vous vouliez vider votre DNS manuellement.

Dans cet article, je vais expliquer pourquoi vous devriez vider votre cache DNS et comment le faire sous Windows 10 et Chrome.

## Alors, pourquoi devriez-vous vider (ou effacer) votre cache DNS ?

Vider votre DNS présente plusieurs avantages, tels que :

-   masquer votre comportement de recherche aux collecteurs de données qui pourraient vous afficher des publicités basées sur votre historique de recherche
-   demander le chargement d'une version mise à jour d'un site web ou d'une application web. Cela peut aider à résoudre les problèmes d'erreur 404 si un site ou une application web a été migré vers un nouveau domaine
-   prévenir l'empoisonnement du cache DNS – une situation de sécurité dans laquelle des hackers black hat accèdent de manière malveillante à votre cache DNS et le modifient afin que vous soyez redirigé vers un site web où des informations sensibles pourraient vous être dérobées

## Comment vider votre cache DNS sur Windows

Pour vider vos enregistrements DNS sur Windows 10, suivez les étapes ci-dessous :

**Étape 1** : Cliquez sur Démarrer ou appuyez sur la touche Windows `[logo]` de votre clavier

**Étape 2** : Tapez "cmd", puis sélectionnez "Exécuter en tant qu'administrateur" sur la droite

![cmd-admin](https://www.freecodecamp.org/news/content/images/2022/04/cmd-admin.jpg)

**Étape 3** : Tapez `ipconfig /flushdns` et appuyez sur `ENTER`

Vous devriez recevoir une réponse indiquant que le cache DNS a été vidé, comme celle ci-dessous :

![flushDNS](https://www.freecodecamp.org/news/content/images/2022/04/flushDNS.png)

Cela signifie que votre cache a été complètement effacé et que des versions fraîches de tous les sites web que vous visiterez seront chargées.

## Comment effacer le cache DNS sur Google Chrome

Bien qu'il ne soit pas un système d'exploitation, Chrome conserve son propre cache DNS pour aider à personnaliser votre expérience de navigation.

Pour vider le DNS de Chrome, il vous suffit de taper `chrome://net-internals/#dns` dans la barre d'adresse et d'appuyer sur `ENTER`.

Ensuite, cliquez sur « Clear host cache » :

![flushChromeDNS](https://www.freecodecamp.org/news/content/images/2022/04/flushChromeDNS.png)

## Conclusion

Comme vous l'avez appris dans cet article, vider votre cache DNS vous offre de nombreux avantages qui peuvent rendre votre expérience sur Internet plus sûre.

Même si le cache est effacé après l'expiration du TTL, vous devriez vider votre DNS aussi souvent que possible pour profiter de ces avantages.

Merci de votre lecture !