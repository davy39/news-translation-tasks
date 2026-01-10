---
title: Erreur dns_probe_finished_nxdomain [Résolu]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-20T15:39:02.000Z'
originalURL: https://freecodecamp.org/news/dns-probe-finished-nxdomain-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/earth-931552_1920.jpg
tags:
- name: Google Chrome
  slug: chrome
- name: error
  slug: error
seo_title: Erreur dns_probe_finished_nxdomain [Résolu]
seo_desc: 'If you are a regular Google Chrome user, then you might have encountered
  the error “dns_probe_finished_nxdomain” before. It is usually accompanied by “This
  site can’t be reached”.


  This error is associated with the Domain Name System (DNS) server and...'
---

Si vous êtes un utilisateur régulier de Google Chrome, vous avez peut-être déjà rencontré l'erreur « dns_probe_finished_nxdomain ». Elle est généralement accompagnée de « Ce site est inaccessible ».
![ss1-5](https://www.freecodecamp.org/news/content/images/2022/04/ss1-5.png)

Cette erreur est associée au serveur du système de noms de domaine (DNS) et peut survenir en raison d'une mauvaise configuration du serveur DNS, d'un serveur non réactif ou d'un DNS de site web non encore propagé. 

Le terme « nxdomain » dans l'erreur signifie que vous essayez d'accéder à un « domaine inexistant ».

Dans d'autres navigateurs, l'erreur « dns_probe_finished_nxdomain » peut se présenter différemment. Sur Microsoft Edge, elle peut apparaître comme « Hmm… impossible d'atteindre cette page », et sur Firefox, elle apparaît généralement comme « Hmm. Nous avons du mal à trouver ce site ».

Corriger cette erreur afin de restaurer votre connectivité Internet n'est pas une tâche ardue. Ainsi, dans cet article, je vais vous montrer 4 façons de la résoudre.

## Ce que nous allons couvrir ici
- [Désactiver votre Antivirus et VPN](#heading-fix-1-desactivez-votre-antivirus-et-vpn)
- [Vider, libérer et renouveler votre cache DNS](#heading-fix-2-vider-liberer-et-renouveler-votre-cache-dns)
  - [Vider le cache DNS de votre navigateur Google Chrome](#youshouldalsoconsiderflushingchromesdns) 
- [Redémarrer votre routeur ou modem](#heading-fix-3-redemarrer-votre-routeur-ou-modem)
- [Changer manuellement votre serveur DNS](#heading-fix-4-changer-manuellement-votre-serveur-dns)
  - [Changer le serveur DNS de votre navigateur Google Chrome](#heading-vous-pouvez-aussi-changer-le-serveur-dns-du-navigateur-google-chrome-en-particulier) 
- [Conclusion](#heading-conclusion)

## Fix 1 – Désactivez votre Antivirus et VPN
Les programmes antivirus sont notoires pour interférer avec les applications et les empêcher de fonctionner correctement.

Les VPN, en revanche, peuvent bloquer certains sites web, tandis que d'autres sites ne fonctionnent pas bien avec eux.

Si vous obtenez l'erreur « dns_probe_finished_nxdomain », envisagez de désactiver votre Antivirus et de désactiver votre VPN, puis vérifiez que vous pouvez à nouveau accéder à Internet. 

Si vous êtes en mesure d'accéder à Internet après avoir désactivé votre programme antivirus et désactivé votre VPN, alors c'est la raison pour laquelle vous obtenez l'erreur. 

Si vous êtes sous Windows 10, vous pouvez désactiver la sécurité Windows en suivant les étapes ci-dessous :
**Étape 1** : Ouvrez le Gestionnaire des tâches en appuyant sur `ALT` + `SHIFT` + `ESC` sur votre clavier.

**Étape 2** : Cliquez sur l'onglet Démarrage.

**Étape 3** : Localisez votre programme Antivirus dans la liste, faites un clic droit dessus et sélectionnez « Désactiver ».
![ss3-4](https://www.freecodecamp.org/news/content/images/2022/04/ss3-4.png)

Essayez à nouveau d'accéder à Internet pour voir si l'erreur n'apparaît plus. Si cela ne corrige pas l'erreur, continuez à lire et essayez d'autres solutions dans cet article.

## Fix 2 – Vider, libérer et renouveler votre cache DNS
Le cache DNS enregistre les adresses IP des sites web que vous avez visités afin d'accélérer le temps de chargement lorsque vous essayez de visiter les mêmes sites.

Vider, libérer et renouveler le cache DNS peut corriger l'erreur « dns_probe_finished_nxdomain » car les processus suppriment les configurations IP invalides et les informations obsolètes dans le cache DNS.

Pour vider, libérer et renouveler le DNS de votre ordinateur sous Windows, suivez les étapes mises en évidence ci-dessous :
**Étape 1** : Appuyez sur le bouton `WIN` de votre clavier et recherchez « cmd ». Puis sélectionnez « Exécuter en tant qu'administrateur » à droite.

**Étape 2** : Entrez et exécutez les commandes suivantes une après l'autre :
- `ipconfig /flushdns`
- `ipconfig /release`
- `ipconfig /renew`
![ss4-3](https://www.freecodecamp.org/news/content/images/2022/04/ss4-3.png)

### Vous devriez également envisager de vider le DNS de Chrome.

Pour vider le DNS de Chrome, il vous suffit de taper `chrome://net-internals/#dns` dans la barre d'adresse et d'appuyer sur `ENTRÉE`. Puis cliquez sur « Clear host cache » :
![flushChromeDNS-1](https://www.freecodecamp.org/news/content/images/2022/04/flushChromeDNS-1.png)
 
Après avoir vidé le cache DNS de votre ordinateur ainsi que celui de Chrome, redémarrez votre ordinateur et vérifiez que vous n'obtenez plus l'erreur.

## Fix 3 – Redémarrer votre routeur ou modem
Si vous accédez à Internet via un routeur ou un modem, le redémarrer pourrait vous aider à vous débarrasser de l'erreur « dns_probe_finished_nxdomain ». 

Cela est dû au fait que l'extinction puis la remise sous tension d'un routeur ou d'un modem efface le cache des adresses IP, ce qui pourrait corriger l'erreur à long terme.

Pour redémarrer votre routeur ou modem, localisez le bouton d'alimentation et appuyez longtemps pour l'éteindre, puis appuyez à nouveau longtemps pour le rallumer.

## Fix 4 – Changer manuellement votre serveur DNS 
Si aucune des solutions ci-dessus ne fonctionne pour vous, vous devriez envisager de changer l'adresse de votre serveur DNS car c'est l'une des méthodes les plus fiables pour corriger l'erreur « dns_probe_finished_nxdomain ».

Par défaut, une adresse de serveur DNS est fournie par votre fournisseur d'accès Internet, mais l'utilisation de ce DNS par défaut n'est pas toujours sécurisée. Et cela pourrait être la raison pour laquelle vous obtenez l'erreur « dns_probe_finished_nxdomain ».

Vous pouvez changer votre serveur DNS pour l'un des serveurs gratuits fournis par des entreprises comme Google et Cloudflare.

Les étapes ci-dessous vous montrent comment changer votre serveur DNS pour celui de Google : 
**Étape 1** : Faites un clic droit sur Démarrer et sélectionnez « Connexions réseau » :
![ss5-3](https://www.freecodecamp.org/news/content/images/2022/04/ss5-3.png)

**Étape 2** : Faites défiler vers le bas et sélectionnez « Modifier les options de l'adaptateur » :
![ss6-3](https://www.freecodecamp.org/news/content/images/2022/04/ss6-3.png)

**Étape 3** : Dans la fenêtre contextuelle qui apparaît, faites un clic droit sur le réseau auquel vous êtes connecté et sélectionnez « Propriétés » :
![ss7-2](https://www.freecodecamp.org/news/content/images/2022/04/ss7-2.png)

**Étape 4** : Dans une autre fenêtre contextuelle qui apparaît, double-cliquez sur « Protocole Internet version 4 (TCP/IPv4) » :
![ss8-2](https://www.freecodecamp.org/news/content/images/2022/04/ss8-2.png)

**Étape 5** : Une autre fenêtre contextuelle apparaîtra. Cette fois-ci, sélectionnez le bouton radio qui dit « Utiliser l'adresse de serveur DNS suivante » :
![ss9-2](https://www.freecodecamp.org/news/content/images/2022/04/ss9-2.png)

**Étape 6** : Entrez 8.8.8.8 pour « Serveur DNS préféré » et 8.8.4.4 pour « Serveur DNS alternatif ». Ce sont les serveurs DNS gratuits fournis par Google.
![ss10-2](https://www.freecodecamp.org/news/content/images/2022/04/ss10-2.png)

**Étape 7** : Cliquez sur « Ok », puis à nouveau sur « Ok ». 

**N.B.** : Si votre ordinateur est configuré pour utiliser IPv6 au lieu d'IPv4, alors à l'étape 4, vous devriez choisir « Protocole Internet version 6 (TCP/IPv6) » au lieu de « Protocole Internet version 4 (TCP/IPv4) ». Ensuite, entrez `2001:4860:4860::8888` pour le serveur DNS préféré et `2001:4860:4860::8844` pour le serveur DNS alternatif.

### Vous pouvez également changer le serveur DNS du navigateur Google Chrome en particulier.

Pour ce faire, rendez-vous sur votre navigateur Chrome, tapez `chrome://settings/security` dans la barre d'adresse et appuyez sur `ENTRÉE`.
![ss2-6](https://www.freecodecamp.org/news/content/images/2022/04/ss2-6.png)

Sur la page qui apparaît, faites défiler vers le bas, cliquez sur « Personnalisé », et sélectionnez « Google (DNS public) » :
![ss3-5](https://www.freecodecamp.org/news/content/images/2022/04/ss3-5.png)

Après avoir fait tout cela, vérifiez si votre connexion Internet est rétablie.

## Conclusion
Comme vous pouvez le voir dans cet article, résoudre l'erreur « dns_probe_finished_nxdomain » n'est pas difficile car il existe plusieurs façons de la corriger. Cet article a discuté de 4 de ces méthodes.

Si l'une des solutions ne parvient pas à résoudre l'erreur pour vous, alors vous devriez essayer une autre solution. En ce qui me concerne, j'ai rencontré cette erreur il n'y a pas longtemps et ce qui l'a corrigée pour moi a été de changer mon serveur DNS – [Fix 4](#heading-fix-4-changer-manuellement-votre-serveur-dns).

Merci d'avoir lu.