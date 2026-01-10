---
title: Serveur DNS ne répond pas – Échec DNS Service Indisponible [Résolu]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-11T15:59:55.000Z'
originalURL: https://freecodecamp.org/news/dns-server-not-responding-service-unavailable-dns-failure-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/binary-g3068c576e_1920.jpg
tags:
- name: dns
  slug: dns
- name: error
  slug: error
- name: internet
  slug: internet
- name: servers
  slug: servers
seo_title: Serveur DNS ne répond pas – Échec DNS Service Indisponible [Résolu]
seo_desc: "Sometimes, you might suddenly discover that you can’t access the internet\
  \ on your computer because of the error “DNS server not responding”. \nIf you run\
  \ a troubleshooter for the issue, you'll get a message like the below:\n\nIn your\
  \ Chrome browser, you..."
---

Parfois, vous pourriez soudainement découvrir que vous ne pouvez pas accéder à Internet sur votre ordinateur en raison de l'erreur « Serveur DNS ne répond pas ».

Si vous exécutez un utilitaire de résolution des problèmes pour ce problème, vous obtiendrez un message comme celui ci-dessous :
![ss1-1](https://www.freecodecamp.org/news/content/images/2022/04/ss1-1.png)

Dans votre navigateur Chrome, vous pourriez également obtenir une erreur comme celle ci-dessous :
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/04/ss2-2.png)

C'est parce que le serveur du système de noms de domaine (DNS) est crucial pour obtenir une connexion Internet sur votre ordinateur.

En ce qui concerne les sites web, l'erreur « Serveur DNS ne répond pas » pourrait être causée par des lacunes DNS et une attaque DDoS (Distributed Denial of Service). Si c'est le problème, vous devrez peut-être attendre 72 heures pour que les lacunes de domaine soient corrigées ou que les administrateurs du site web résolvent les problèmes de sécurité du site.

Du côté de l'utilisateur, l'erreur « Serveur DNS ne répond pas » pourrait être causée par de nombreuses raisons telles que des paramètres DNS mal configurés et des navigateurs obsolètes.

Si c'est la cause, je vais vous montrer 7 façons de corriger l'erreur afin que vous puissiez restaurer votre connexion Internet.

## Table des matières
- [Comment fonctionne le système DNS ?](#heading-comment-fonctionne-le-systeme-dns)
- [7 Façons de corriger l'erreur « Serveur DNS ne répond pas »](#heading-7-facons-de-corriger-l-erreur-serveur-dns-ne-repond-pas)
  - [Solution 1 : Changer de navigateur](#heading-solution-1-changer-de-navigateur)
  - [Solution 2 : Désactiver temporairement votre antivirus](#heading-solution-2-desactiver-temporairement-votre-antivirus)
  - [Solution 3 : Redémarrer votre routeur ou modem](#heading-solution-3-redemarrer-votre-routeur-ou-modem)
  - [Solution 4 : Vider le cache DNS](#heading-solution-4-vider-le-cache-dns)
  - [Solution 5 : Changer manuellement votre serveur DNS](#heading-solution-5-changer-manuellement-votre-serveur-dns)
  - [Solution 6 : Mettre à jour le pilote de votre adaptateur réseau](#heading-solution-6-mettre-a-jour-le-pilote-de-votre-adaptateur-reseau)
  - [Solution 7 : Désactiver IPv6](#heading-solution-7-desactiver-ipv6)
- [Réflexions finales](#heading-reflexions-finales)

## Comment fonctionne le système DNS ?

Chaque fois que vous essayez d'accéder à un site web, comme freeCodeCamp.org, vous tapez l'URL comme « freecodecamp.org » dans la barre d'adresse et appuyez sur `ENTRÉE`.

En coulisses, le serveur DNS recherche l'adresse numérique de freeCodeCamp.org. Cette adresse numérique est appelée adresse de protocole Internet (IP).

Une fois que le navigateur obtient cette adresse IP, le site web (freeCodeCamp.org ou un autre) sera affiché. Si le navigateur ne parvient pas à trouver cette adresse, vous pourriez obtenir l'erreur « Serveur DNS ne répond pas ».

## 7 Façons de corriger l'erreur « Serveur DNS ne répond pas »

Passons maintenant en revue sept façons de vous débarrasser de l'erreur « Serveur DNS ne répond pas » afin que votre connexion Internet puisse être rétablie.

### Solution 1 : Changer de navigateur

L'erreur « Serveur DNS ne répond pas » pourrait s'afficher en raison du navigateur que vous utilisez actuellement. Certains navigateurs ont leur propre cache DNS et s'il y a un problème avec le cache, votre expérience Internet sur ce navigateur pourrait être négativement affectée.

Ainsi, une solution simple consiste à changer de navigateur et à voir si l'erreur persiste.

Par exemple, si vous utilisez Chrome, passez à Edge si vous êtes sous Windows ou à Safari si vous utilisez Mac.

Si le site web se charge dans un autre navigateur, vous devrez peut-être mettre à jour votre autre navigateur ou le réinstaller.

### Solution 2 : Désactiver temporairement votre antivirus

Les programmes antivirus sont notoires pour interférer avec les applications et les empêcher de fonctionner correctement.

Si vous obtenez l'erreur « Serveur DNS ne répond pas », envisagez de désactiver votre programme antivirus pour voir si votre connexion Internet fonctionne correctement.

Si vous pouvez accéder à Internet après avoir désactivé l'antivirus, alors c'est la raison pour laquelle vous obtenez l'erreur.

Dans ce cas, vous pourriez envisager d'obtenir un autre programme antivirus.

Si vous êtes sous Windows 10, vous pouvez désactiver Windows Security (alias Windows Defender) en suivant les étapes ci-dessous :
**Étape 1** : Appuyez sur `ALT` + `SHIFT` + `ESC` sur votre clavier pour ouvrir le Gestionnaire des tâches

**Étape 2** : Passez à l'onglet Démarrage

**Étape 3** : Localisez votre programme antivirus dans la liste, faites un clic droit dessus et sélectionnez "Désactiver".
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/04/ss3-1.png)

### Solution 3 : Redémarrer votre routeur ou modem

Si votre connexion Internet dépend d'un routeur ou d'un modem, le redémarrer pourrait vous aider à vous débarrasser de l'erreur « Serveur DNS ne répond pas ».

C'est parce qu'éteindre puis rallumer un routeur ou un modem efface le cache des adresses IP. Cela pourrait corriger l'erreur à long terme.

Pour redémarrer votre routeur ou modem, localisez le bouton d'alimentation et appuyez longtemps pour l'éteindre, puis rallumez-le.

### Solution 4 : Vider le cache DNS

Si l'erreur « Serveur DNS ne répond pas » est due à une mauvaise configuration sur votre appareil, vider votre DNS est l'une des méthodes les plus fiables pour la corriger. En effet, ce processus supprimera les configurations IP invalides et les informations obsolètes dans le cache DNS.

Pour vider le cache DNS de votre ordinateur sous Windows, suivez les étapes mises en évidence ci-dessous :

**Étape 1** : Appuyez sur le bouton `WIN` de votre clavier et recherchez "cmd". Puis sélectionnez "Exécuter en tant qu'administrateur" à droite.

**Étape 2** : Entrez et exécutez les commandes suivantes une après l'autre :
- `ipconfig /flushdns`
- `ipconfig /release`
- `ipconfig /renew`
![ss4](https://www.freecodecamp.org/news/content/images/2022/04/ss4.png)

**Étape 3** : Redémarrez votre ordinateur

### Solution 5 : Changer manuellement votre serveur DNS

L'utilisation du serveur DNS par défaut de votre fournisseur d'accès Internet pourrait être la raison pour laquelle vous obtenez l'erreur « Serveur DNS ne répond pas ».

Vous pouvez changer votre serveur DNS pour l'un des serveurs gratuits fournis par des entreprises comme Google et Cloudflare.

Les étapes ci-dessous vous montrent comment changer votre serveur DNS pour celui de Google :

**Étape 1** : Faites un clic droit sur Démarrer et sélectionnez "Connexions réseau" :
![ss5](https://www.freecodecamp.org/news/content/images/2022/04/ss5.png)

**Étape 2** : Faites défiler vers le bas et sélectionnez "Modifier les options de l'adaptateur" :
![ss6](https://www.freecodecamp.org/news/content/images/2022/04/ss6.png)

**Étape 3** : Dans la fenêtre contextuelle qui apparaît, faites un clic droit sur le réseau auquel vous êtes connecté et sélectionnez "Propriétés" :
![ss7](https://www.freecodecamp.org/news/content/images/2022/04/ss7.png)

**Étape 4** : Dans la fenêtre contextuelle suivante qui apparaît, double-cliquez sur "Protocole Internet version 4 (TCP/IPv4)" :
![ss8](https://www.freecodecamp.org/news/content/images/2022/04/ss8.png)

**Étape 5** : Dans la fenêtre contextuelle suivante qui apparaît, cliquez sur le bouton radio qui dit "Utiliser les adresses de serveur DNS suivantes" :
![ss9](https://www.freecodecamp.org/news/content/images/2022/04/ss9.png)

**Étape 6** : Entrez 8.8.8.8 pour "Serveur DNS préféré" et 8.8.4.4 pour "Serveur DNS alternatif" :
![ss10](https://www.freecodecamp.org/news/content/images/2022/04/ss10.png)

C'est le serveur DNS gratuit fourni par Google.

**Étape 7** : Cliquez sur "Ok", puis sur "Ok" à nouveau.

N.B. : Si votre ordinateur est configuré pour utiliser IPv6 au lieu de IPv4, alors à l'étape 4, vous devez choisir "Protocole Internet version 6 (TCP/IPv6)" au lieu de "Protocole Internet version 4 (TCP/IPv4)".

### Solution 6 : Mettre à jour le pilote de votre adaptateur réseau

Mettre à jour le pilote de votre adaptateur réseau peut corriger de nombreux problèmes techniques – y compris l'erreur « Serveur DNS ne répond pas », car le nouveau pilote pourrait inclure des corrections de bugs.

Pour mettre à jour le pilote de votre adaptateur réseau, vous pouvez le faire avec les étapes ci-dessous :

**Étape 1** : Cliquez sur Démarrer et sélectionnez Gestionnaire de périphériques.

**Étape 2** : Développez Adaptateurs réseau.

**Étape 3** : Faites un clic droit sur le pilote concerné et sélectionnez Mettre à jour le pilote :
![ss11](https://www.freecodecamp.org/news/content/images/2022/04/ss11.png)

**Étape 4** : Choisissez Rechercher automatiquement un logiciel de pilote mis à jour :
![ss12](https://www.freecodecamp.org/news/content/images/2022/04/ss12.png)

**Étape 5** : Laissez votre ordinateur rechercher un pilote en ligne et l'installer pour vous. Une fois l'installation terminée, redémarrez votre ordinateur.

### Solution 7 : Désactiver IPv6

Si votre réseau actuel est configuré pour utiliser IPv4 et que IPv6 est activé sur votre ordinateur, cela pourrait entraîner des interférences négatives qui pourraient vous faire obtenir l'erreur « Serveur DNS ne répond pas ».

Pour désactiver IPv6, les étapes suivantes peuvent vous aider :

**Étape 1** : Faites un clic droit sur Démarrer et sélectionnez "Connexions réseau" :
![ss5](https://www.freecodecamp.org/news/content/images/2022/04/ss5.png)

**Étape 2** : Faites défiler vers le bas et sélectionnez "Modifier les options de l'adaptateur" :
![ss6](https://www.freecodecamp.org/news/content/images/2022/04/ss6.png)

**Étape 3** : Dans la fenêtre contextuelle qui apparaît, faites un clic droit sur le réseau auquel vous êtes connecté et sélectionnez "Propriétés" :
![ss7](https://www.freecodecamp.org/news/content/images/2022/04/ss7.png)

**Étape 4** : Dans la fenêtre contextuelle suivante qui apparaît, décochez "Protocole Internet version 6 (TCP/IPv6)" :
![ss13](https://www.freecodecamp.org/news/content/images/2022/04/ss13.png)

**Étape 6** : Cliquez sur "Ok", puis sur "Ok" à nouveau.

## Réflexions finales

L'erreur « Serveur DNS ne répond pas » peut être frustrante et perturber votre expérience Internet. Mais dans cet article, vous avez appris comment la corriger si l'erreur est causée par une mauvaise configuration du DNS du côté de l'utilisateur.

J'espère que l'une des solutions à l'erreur expliquées dans cet article vous aidera à corriger l'erreur.