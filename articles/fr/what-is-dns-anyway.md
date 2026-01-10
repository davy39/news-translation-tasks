---
title: Ce que vous devez savoir sur le DNS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-12T21:07:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-dns-anyway
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/nasa-53884-unsplash.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: internet
  slug: internet
- name: technology
  slug: technology
seo_title: Ce que vous devez savoir sur le DNS
seo_desc: 'By Megan Kaczanowski

  What is DNS lookup?

  Domain Name System Lookup, or DNS for short, is what happens in the time between
  someone typing a URL into the search bar and the page loading. Technically speaking,
  it is a process that translates URLs (like ...'
---

Par Megan Kaczanowski

### Qu'est-ce que la recherche DNS ?

Le système de noms de domaine (DNS) est le processus qui se produit entre le moment où quelqu'un tape une URL dans la barre de recherche et le chargement de la page. Techniquement parlant, il s'agit d'un processus qui traduit les URL (comme [www.google.com](http://www.google.com%29) en adresses IP. 

Une adresse IP est similaire à votre adresse postale. Tout comme vous utilisez des adresses pour envoyer du courrier, les ordinateurs utilisent des adresses IP pour envoyer des données à un endroit spécifique. Comme les adresses IP sont difficiles à retenir (ce sont de longues chaînes de chiffres), les ordinateurs utilisent le DNS pour traduire entre les adresses IP et les URL (qui sont beaucoup plus faciles à retenir). Tous les appareils connectés à Internet ont une adresse IP.

### Comment fonctionne le DNS ?

Étant donné la taille d'Internet, les ordinateurs ne peuvent pas stocker toutes les adresses IP dans leur mémoire. Au lieu de cela, taper [www.google.com](http://www.google.com) dans un navigateur indique à l'ordinateur de rechercher l'adresse IP du site web.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-5.00.46-PM.png)

Tout d'abord, l'ordinateur vérifie sa mémoire locale, appelée cache. C'est là que l'ordinateur stocke les adresses IP des sites les plus récemment visités, afin de les charger plus rapidement sans avoir à les rechercher. Cependant, comme seuls quelques sites récemment visités s'y trouvent, il est probable que l'ordinateur ne trouve pas l'adresse IP.

**Étape 1 (les étapes correspondent aux numéros du diagramme ci-dessus) :** Ensuite, l'ordinateur demandera au serveur de noms récursif local du FAI. Un FAI est un fournisseur de services Internet, comme Time Warner Cable, Spectrum, Verizon, etc. Un serveur de noms semble compliqué, mais il s'agit simplement d'un logiciel serveur conçu pour répondre aux requêtes DNS (comme « quelle est l'adresse IP pour www.google.com ? »).

Tout serveur de noms peut répondre à cette question, soit en répondant avec l'adresse IP (s'il la connaît), soit en répondant qu'il ne la connaît pas et en indiquant au serveur demandeur de poser la question à un autre serveur. Un serveur de noms récursif est différent car, s'il ne connaît pas la réponse à la question, il effectuera le travail de trouver la réponse, au lieu de simplement rediriger la requête. Tous les serveurs de noms ne sont pas récursifs.

**Étape 2 :** Le serveur de noms récursif vérifiera d'abord son cache. Si l'adresse IP n'y est pas, il demandera à un serveur de noms racine (les serveurs de noms racine ne connaissent pas les adresses IP, mais ils peuvent lire les requêtes et indiquer au serveur de noms récursif où aller ensuite). Tous les serveurs de noms récursifs sont préconfigurés avec les adresses IP de 13 serveurs de noms racine. Le serveur de noms récursif en choisit un et lui pose la même question (« quelle est l'adresse IP pour www.google.com ? »).

**Étape 3 :** Le serveur de noms racine lit le domaine de premier niveau (la fin de la requête), dans ce cas .com (www.google.com), et indiquera au serveur de noms récursif de demander aux serveurs de domaine de premier niveau mondial (GTLD). Les GTLD sont essentiellement des listes de référence pour chaque type de domaine — .com, .net, .edu, etc. Bien qu'ils ne connaissent pas les adresses IP des sites web, ils savent quels serveurs de noms auront cette information.

**Étape 4 :** Le serveur de noms récursif demande au serveur de noms GTLD l'adresse IP de www.google.com.

**Étape 5 :** Le serveur de noms GTLD lira la partie suivante de votre requête, de droite à gauche (dans ce cas, le « google » de [www.google.com](http://www.google.com%29), et enverra un message avec le serveur de noms faisant autorité à contacter. Un serveur de noms faisant autorité est un serveur de noms responsable du domaine (et est la source principale d'informations).

**Étape 6 :** Le serveur de noms récursif posera la même question au serveur de noms faisant autorité (« quelle est l'adresse IP pour www.google.com ? »). Techniquement, le serveur demande l'enregistrement d'adresse (A), qui est la manière dont les serveurs se réfèrent à l'adresse IP.

**Étape 7 :** Ce serveur a la réponse ! Il transmettra l'adresse IP au serveur de noms récursif, marquée pour indiquer au serveur de noms récursif que la réponse est faisant autorité. Le serveur de noms récursif enregistre l'adresse IP dans son cache au cas où quelqu'un essaierait d'accéder au même site web bientôt. Chaque élément du cache est marqué avec un « temps de vie » qui indique au serveur combien de temps conserver l'information avant de la supprimer.

**Étape 8 :** Le serveur de noms récursif indique à votre ordinateur quelle est l'adresse IP (elle n'est pas marquée comme faisant autorité cette fois, car elle n'est pas la source principale d'informations. Elle transmet simplement l'information).

**Étape 9 :** Votre ordinateur envoie une requête pour [www.google.com](http://www.google.com) à l'adresse IP qu'il vient de recevoir.

**Étape 10 :** Le serveur web à cette adresse renvoie la page d'accueil de Google et la page se charge.

L'ensemble de ce processus ne prend que quelques millisecondes et se produit des milliards de fois chaque jour.

### Comment le DNS impacte-t-il les utilisateurs finaux ?

Le DNS étant essentiel au fonctionnement d'Internet, il est une cible de choix pour les pirates. Le problème fondamental avec le DNS est le même que la plupart des problèmes de sécurité que nous rencontrons avec la technologie d'aujourd'hui. Internet, et une grande partie de la technologie que nous utilisons aujourd'hui, a été conçu pour un petit groupe de chercheurs et s'est développé au fil du temps en un système utilisé par le monde entier. Le DNS (et le HTTP, et la plupart des protocoles que nous utilisons) n'a pas été conçu en tenant compte de la sécurité. Maintenant, nous avons dû ajouter des correctifs pour divers problèmes de sécurité. Malheureusement, la sécurité ajoutée à la fin n'est pas aussi efficace que la sécurité intégrée dès le développement.

Un problème que cela pose pour le DNS est qu'il n'y a aucune vérification de l'authenticité du serveur de noms lorsqu'une réponse est reçue. Ainsi, un pirate peut envoyer des réponses malveillantes à une requête DNS d'un ordinateur et tromper l'ordinateur en lui faisant croire qu'il s'agit de la véritable réponse du serveur de noms DNS. En d'autres termes, lorsque l'ordinateur demande : « quelle est l'adresse IP pour www.chase.com ? », le pirate répondra (avant que le serveur DNS ne puisse le faire) avec l'adresse IP du site malveillant du pirate. Ensuite, lorsque le site se charge, il ressemble exactement au site chase.com, mais est en réalité contrôlé par le pirate.

Cela ressemble beaucoup au phishing, sauf que les utilisateurs ne sont pas trompés en cliquant sur de mauvais liens, mais plutôt les sites web qu'ils essaient de visiter sont redirigés vers de mauvais sites via la recherche DNS (beaucoup plus dangereux, car il est beaucoup plus difficile de prévenir ces types d'attaques). Cela nécessite alors que l'utilisateur soit prudent, pour remarquer que le site est une contrefaçon du site réel (peut-être que le lien ne semble pas tout à fait correct, ou il y a des fautes d'orthographe ou des copies de logo de mauvaise qualité). Cependant, cela peut être très difficile et repose sur le fait que les utilisateurs soient relativement techniquement avertis.

En 2016, une attaque DNS a mis hors service des parties importantes d'Internet pour la majeure partie de la côte est des États-Unis pendant presque une journée entière. Dans ce cas, la panne a été causée par une attaque DDoS. Une attaque DDoS est une attaque par déni de service distribué, dans laquelle des milliers de machines à travers Internet attaquent un système en même temps. Généralement, ce sont des machines qui ont été infectées par des logiciels malveillants sans que leur propriétaire le sache, et un pirate, ou un groupe de pirates, contrôle toutes les machines. Ces machines sont appelées un « botnet » lorsqu'elles sont utilisées ensemble.

Le botnet envoie des requêtes DNS au serveur victime et la quantité de requêtes envoyées submerge le système, rendant le serveur incapable de gérer le trafic légitime qu'il reçoit. Ainsi, tandis que les pirates attaquent les serveurs DNS et qu'un ordinateur essaie de demander des adresses IP, le serveur est incapable de répondre. L'ordinateur ne peut donc pas accéder aux sites que le serveur contrôle (ou pour lesquels il est faisant autorité) jusqu'à ce que l'attaque soit arrêtée.

Cette attaque peut être atténuée en surdimensionnant les serveurs afin de gérer la demande excédentaire ou en ayant un pare-feu DNS.

Une approche plus large pour résoudre de nombreux problèmes posés par le DNS est DNSSEC. DNSSEC renforce l'authentification avec des signatures numériques basées sur la cryptographie à clé publique. Essentiellement, le propriétaire des données demandées les signe numériquement, afin de s'assurer que la situation ci-dessus ne peut pas se produire. Cela fournit une authentification de l'origine des données (les données proviennent réellement de l'endroit où le résolveur pense qu'elles proviennent) et une protection de l'intégrité des données (les données n'ont pas été modifiées pendant le transit).

Malheureusement, pour corriger le DNS, DNSSEC nécessite un déploiement à grande échelle. Il doit être spécifiquement activé par les opérateurs de réseau sur leurs résolveurs récursifs, et par les propriétaires de noms de domaine sur les serveurs faisant autorité. Cela n'a pas encore eu lieu, mais espérons que cela se fera à mesure que davantage de personnes prendront conscience des problèmes que pose le DNS et militeront pour des changements.