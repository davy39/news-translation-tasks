---
title: Comment vider le cache DNS sur Mac – Effacer le cache DNS de macOS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-04-21T00:15:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-flush-dns-on-mac-macos-clear-dns-cache
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/kaitlyn-baker-vZJdYl5JVXY-unsplash.jpg
tags:
- name: dns
  slug: dns
- name: macOS
  slug: macos
seo_title: Comment vider le cache DNS sur Mac – Effacer le cache DNS de macOS
seo_desc: 'In this tutorial, you will learn why flushing your DNS cache is important,
  and how you can clear the cache on your local system.

  Here is what we''ll discuss in this guide:


  What is DNS cache?

  Why flushing DNS cache is important



  How to flush DNS cach...'
---

Dans ce tutoriel, vous apprendrez pourquoi il est important de vider votre cache DNS et comment vous pouvez effacer le cache sur votre système local.

Voici ce que nous allons discuter dans ce guide :

1. [Qu'est-ce que le cache DNS ?](#questceque)
    1. [Pourquoi vider le cache DNS est important](#pourquoi)
2. [Comment vider le cache DNS sur macOS](#commentvider)
    1. [Comment accéder à l'application Terminal sur macOS](#terminal)
    2. [Comment effacer le cache DNS pour votre version de macOS](#version)

## Qu'est-ce que le cache DNS ? <a name="questceque"></a>

Le DNS fonctionne comme un annuaire téléphonique internet. Imaginez ce qu'un annuaire fait – il associe le nom d'une personne à son numéro de téléphone.

Le DNS (Domain Name System) associe les noms de domaine à leurs adresses IP correspondantes.

Un nom de domaine, comme `freecodecamp.org`, est facilement lisible, compris et mémorisé par les humains.

Les adresses IP (IP pour Internet Protocol) sont des adresses lisibles par machine et composées d'une série unique de chiffres. Ces chiffres identifient un appareil connecté à Internet.

Leur format n'est pas très convivial pour les humains, car il est difficile de mémoriser une séquence exacte de chiffres chaque fois que vous souhaitez visiter un site web.

Le DNS associe alors `freecodecamp.org` à son adresse IP correspondante - `104.26.3.33`.

Imaginez le cache DNS comme une zone de stockage locale sur votre Mac.

Il stocke temporairement et suit les enregistrements d'activité de votre ordinateur, comme les visites récentes de sites web.

Chaque fois que vous visitez un site web en tapant son URL (Uniform Resource Locator), le cache DNS enregistrera l'adresse IP associée à ce site web.

Lorsque vous visitez ce même site web une deuxième fois, le processus de recherche est plus efficace et le temps de recherche est beaucoup plus court.

Cela permet d'économiser un temps considérable.

### Pourquoi vider le cache DNS est important <a name="pourquoi"></a>

Vous devriez vider le cache DNS pour plusieurs raisons.

Les deux plus importantes sont :

1) **Vider le cache DNS est une étape utile pour résoudre les problèmes de connectivité Internet**.

Vous pouvez rencontrer des erreurs DNS dans votre navigateur, comme le message "Le serveur DNS ne répond pas" lorsque vous essayez d'accéder à un site et d'établir une connexion.

Gardez à l'esprit que les informations de votre cache local peuvent devenir obsolètes avec le temps.

Lorsque des mises à jour DNS se produisent sur un site web, votre Mac utilise toujours les anciennes informations inexactes pour charger la page demandée.

Vider le cache DNS garantit que les informations du cache sont à jour.

2) **Vider le cache DNS empêche les menaces de sécurité réseau, les attaques malveillantes et l'empoisonnement du cache DNS**.

Les pirates peuvent accéder et corrompre vos enregistrements de cache DNS enregistrés.

Par exemple, ils pourraient manipuler et changer l'adresse IP associée à un nom de domaine d'un site web que vous avez déjà visité et l'associer à une adresse malveillante.

La prochaine fois que vous demanderez à accéder à ce même site web, il y aura une redirection vers une URL falsifiée et corrompue.

Les pirates peuvent demander des informations personnelles et sensibles, comme des numéros de carte de crédit, et les voler.

Le vidage fréquent du cache DNS aidera à prévenir cela.

## Comment vider le cache DNS sur macOS <a name="commentvider"></a>

Effacer le cache DNS sur votre Mac est un processus relativement simple, même si vous n'avez pas beaucoup de connaissances techniques.

Voici ce dont vous aurez besoin :

- Accès à la ligne de commande,
- Le mot de passe de votre ordinateur,
- Entrer une commande texte (la commande dépendra de la version de macOS que vous utilisez).

### Comment accéder à l'application Terminal sur macOS <a name="terminal"></a>

macOS dispose d'une interface en ligne de commande (CLI) intégrée nommée `Terminal.app`, qui vous permet d'entrer des commandes basées sur du texte que le système d'exploitation exécutera.

Il existe plusieurs façons d'ouvrir le terminal.

La manière la plus simple est via la recherche Spotlight.

Pour cela, vous pouvez :

- Soit naviguer jusqu'au coin supérieur droit de l'écran et cliquer sur l'icône qui ressemble à une loupe.
- Ou utiliser le raccourci `Commande Espace`.

Les deux méthodes ouvriront la fenêtre suivante :

![Screenshot-2022-04-20-at-10.07.52-AM](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-20-at-10.07.52-AM.png)

À partir de là, commencez à taper `terminal` et cliquez sur l'option `Terminal.app` qui apparaît.

Vous devriez voir une fenêtre s'ouvrir qui ressemble à ceci :

![Screenshot-2022-04-20-at-10.12.29-AM](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-20-at-10.12.29-AM.png)

### Comment effacer le cache DNS pour votre version de macOS <a name="version"></a>

Dans la fenêtre du terminal, vous devrez ensuite entrer une commande.

La commande est différente selon la version de macOS que vous utilisez.

Chaque version de macOS a un numéro de version et un nom de version.

Pour connaître la version de macOS sur votre ordinateur, cliquez sur l'icône Apple en haut à gauche de votre écran. Dans le menu déroulant qui apparaît, sélectionnez `À propos de ce Mac`.

Dans l'onglet `Aperçu`, vous verrez d'abord le nom de la version. Ensuite, en dessous, vous verrez le numéro de version.

![Screenshot-2022-04-20-at-11.07.26-AM](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-20-at-11.07.26-AM.png)

Dans le tableau ci-dessous, vous verrez les versions de macOS dans l'ordre chronologique inverse – de la plus récente à la plus ancienne.

Naviguez jusqu'à votre version de Mac et copiez la commande correspondante.

| Version de macOS      | Commande |
| ----------- | ----------- |
| macOS 12 (Monterey)     | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`       |
| macOS 11 (Big Sur)   | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`       |
| macOS 10.15 (Catalina)   | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`       |
| macOS 10.14 (Mojave)   | `sudo killall -HUP mDNSResponder`     |
| macOS 10.13 (High Sierra)   | `sudo killall -HUP mDNSResponder`     |
|macOS 10.12 (Sierra)   | `sudo killall -HUP mDNSResponder`     |
|OS X 10.11 (El Capitan)   | `sudo killall -HUP mDNSResponder`    |
|OS X 10.10 (Yosemite)   |`sudo discoveryutil udnsflushcaches`   |
|OS X 10.9 (Mavericks)   | `sudo killall -HUP mDNSResponder`  |
|OS X 10.8 (Mountain Lion)   | `sudo killall -HUP mDNSResponder` |
|Mac OS X 10.7 (Lion)   | `sudo killall -HUP mDNSResponder`|
|Mac OS X 10.6 (Snow Leopard)   | `sudo dscacheutil -flushcache`|
|Mac OS X 10.5 (Leopard)   | `sudo lookupd -flushcache`|
|Mac OS X 10.4 (Tiger)   | `lookupd -flushcache`|

Après avoir tapé la commande et appuyé sur Entrée, une invite vous demandera d'entrer le mot de passe de votre ordinateur.

Gardez à l'esprit que lorsque vous tapez votre mot de passe, vous ne pourrez pas voir ce que vous tapez – pas même d'astérisques.

Il semble que rien ne se passe, mais soyez assuré que quelque chose se passe.

Une fois que vous avez entré votre mot de passe et appuyé sur Entrée, vous ne verrez pas de message indiquant que le processus est terminé.

Au lieu de cela, vous verrez une nouvelle invite de terminal.

## Conclusion

Et voilà – votre cache DNS local est maintenant effacé.

Espérons que cela a aidé à résoudre les problèmes de connectivité que vous pourriez rencontrer.

Effacer fréquemment le cache DNS est toujours une bonne idée pour aider à corriger les connexions Internet problématiques et garantir que votre système est sécurisé contre les menaces potentielles.

Merci d'avoir lu !