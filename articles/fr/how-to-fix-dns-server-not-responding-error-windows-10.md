---
title: Le serveur DNS ne répond pas – Comment corriger l'erreur sous Windows 10
subtitle: ''
author: Gavin Lon
co_authors: []
series: null
date: '2022-09-30T15:00:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-dns-server-not-responding-error-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/DNS-Issue-Main-Pic
seo_title: Le serveur DNS ne répond pas – Comment corriger l'erreur sous Windows 10
---

pexels-yan-krukov-4458420.jpg
tags:
- name: dns
  slug: dns
- name: erreur
  slug: erreur
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "Je pense qu'on peut dire sans se tromper que la grande majorité des professionnels dépendent d'Internet de nos jours. Se voir refuser l'accès à Internet alors que vous essayez d'extraire des pépites d'informations précieuses de vos sites Web habituels peut être une véritable épreuve. ..."
---

Je pense qu'on peut dire sans se tromper que la grande majorité des professionnels dépendent d'Internet de nos jours. 

Se voir refuser l'accès à Internet alors que vous essayez d'extraire des pépites d'informations précieuses de vos sites Web habituels peut être une véritable épreuve. Surtout lorsque vous êtes sous pression pour terminer un travail urgent. 

Une cause particulièrement importune de refus d'accès à Internet est l'erreur « Le serveur DNS ne répond pas ». C'est comme cette vieille fable où un troll se tient sous un pont et dit : « Vous ne passerez pas ! », ou quelque chose à propos de dévorer ceux qui souhaitent traverser le pont. 

Je suis ravi de vous dire que vous devriez être en mesure de vaincre le troll et de traverser le pont vers la joie de l'accès à Internet en suivant les étapes de dépannage simples présentées dans cet article.

## Qu'est-ce que l'erreur « Le serveur DNS ne répond pas » ?

L'erreur « Le serveur DNS ne répond pas » est un problème assez courant et est généralement facile à corriger. Il existe de nombreuses raisons pour lesquelles ce problème peut survenir. Mais fondamentalement, il est causé par le fait que le serveur DNS contacté lors du processus de chargement d'une page Web est incapable de trouver le site qui contient la page Web que vous avez demandée. 

Cet article explore ce qui a pu déclencher ce problème et comment vous pouvez essayer de le résoudre.

Tout d'abord, je pense qu'il est judicieux d'acquérir au moins une compréhension de base de l'erreur « Le serveur DNS ne répond pas ». Pour ce faire, comprenons d'abord ce qu'est le DNS. 

DNS signifie Domain Name System (système de noms de domaine). Une explication simple du DNS est qu'il s'agit d'un stockage décentralisé d'adresses Internet lisibles par l'homme, comme celles avec lesquelles vous êtes presque certainement familier (par exemple www.amazon.com ou www.netflix.com). 

Le DNS fait correspondre ces URL lisibles par l'homme à leurs adresses IP (Internet Protocol) appropriées. 

Les adresses IP sont beaucoup moins lisibles par l'homme, mais sont essentielles au fonctionnement interne d'Internet. Les adresses IP identifient de manière unique les ordinateurs sur Internet. L'adresse IP associée à l'URL www.netflix.com pourrait, par exemple, ressembler à ceci : 69.53.224.255. 

Il est clairement plus facile pour vous de vous souvenir de « [www.netflix.com](http://www.netflix.com) », plutôt que d'une chaîne de chiffres délimités par des points, lorsque vous souhaitez accéder à votre contenu préféré sur Netflix. Le DNS facilite donc cela pour vous, afin que vous n'ayez pas à mémoriser ou à rechercher manuellement des chaînes de données numériques peu conviviales chaque fois que vous souhaitez accéder à un site Web. 

L'analogie courante pour expliquer le DNS est celle d'un annuaire téléphonique. En gros, de la même manière que vous chercheriez un numéro de téléphone en utilisant le nom de la personne que vous souhaitez appeler dans un annuaire, une recherche similaire est effectuée lorsque vous tapez l'URL (comme www.amazon.com) du site Web que vous souhaitez consulter dans votre navigateur.

Heureusement, vous n'avez pas à rechercher manuellement l'adresse IP correspondante pour www.amazon.com, car cela est effectué automatiquement en coulisses. 

Ainsi, l'adresse IP appropriée est récupérée automatiquement chaque fois que vous tapez une URL dans votre navigateur. Cette adresse IP est ensuite utilisée pour contacter le serveur approprié qui héberge le site Web associé à l'URL que vous avez saisie.

Lorsque l'erreur « Le serveur DNS ne répond pas » se produit, cela signifie que les systèmes de nommage décentralisés responsables de la recherche automatique de l'adresse IP appropriée basée sur le nom d'hôte que vous avez saisi ne répondent pas. 

Il existe de nombreuses raisons pour lesquelles cette erreur se produit, mais heureusement, il existe également de nombreuses solutions pour résoudre le problème. 

Une solution simple peut consister à changer de navigateur Web ou, plus simple encore, à redémarrer votre ordinateur. Oui, le simple fait de l'éteindre puis de le rallumer pourrait résoudre le problème. 

Cependant, si vous n'avez pas cette chance et que le problème persiste, ne désespérez pas – il existe de nombreuses étapes que vous pouvez suivre pour trouver la cause du problème et le corriger par la suite. 

Dans cet article, vous découvrirez un certain nombre de solutions possibles à l'erreur « Le serveur DNS ne répond pas ».

## Comment corriger l'erreur « Le serveur DNS ne répond pas »

Ci-dessous, j'ai listé les moyens que vous pouvez essayer pour corriger l'erreur « Le serveur DNS ne répond pas ». Les sections suivantes de cet article fournissent des détails sur chacune de ces méthodes :

* Utiliser un autre navigateur Web
* Essayer d'accéder à un site Web avec un autre appareil
* Redémarrer votre routeur
* Rechercher d'éventuels problèmes de réseau
* Configurer manuellement votre serveur DNS
* Vider le cache DNS
* Désactiver le protocole Internet version 6
* Désactiver temporairement votre pare-feu et votre logiciel antivirus
* Réinitialiser vos paramètres DNS
* Mettre à jour le pilote de la carte réseau
* Désactiver toutes les connexions réseau sauf celle que vous utilisez pour accéder à Internet
* Redémarrer votre ordinateur en mode sans échec

### Utiliser un autre navigateur Web

Une solution potentielle très simple au problème « Le serveur DNS ne répond pas » consiste à essayer d'accéder au site Web concerné en utilisant un autre navigateur. 

Si, par exemple, vous utilisez Microsoft Edge ou Mozilla Firefox au moment où le problème survient, essayez d'utiliser un autre navigateur comme Google Chrome pour accéder au site.

Si l'utilisation d'un autre navigateur résout le problème, faites de ce navigateur votre navigateur par défaut. Mais si le problème persiste, nous savons au moins que le navigateur n'est pas la source du problème et notre enquête doit se poursuivre…

### Essayer d'accéder à un site Web avec un autre appareil

Essayez d'utiliser un autre appareil connecté à votre réseau domestique pour accéder au site Web que vous tentiez de consulter. 

Par exemple, utilisez le Wi-Fi de votre téléphone portable. Si le problème persiste, vous saurez que le souci ne vient pas uniquement de votre appareil principal et qu'il pourrait être lié à votre routeur.

### Redémarrer votre routeur

Le problème « Le serveur DNS ne répond pas » peut survenir simplement en raison du trafic de données. Il se peut qu'un simple redémarrage de votre routeur règle la situation. 

Vous pouvez redémarrer votre routeur en appuyant sur le bouton d'alimentation. Vous pouvez ensuite débrancher le câble d'alimentation du routeur. Attendez environ 30 secondes, puis rebranchez-le et appuyez sur le bouton d'alimentation pour le redémarrer.

### Rechercher d'éventuels problèmes de réseau

L'exécution de diagnostics réseau peut identifier des problèmes de réseau comme cause profonde. 

L'exécution d'un diagnostic réseau est très simple sur Windows 10. Vous pouvez le faire en suivant ces étapes :

* Ouvrez le Panneau de configuration. Une façon de le faire est d'appuyer sur la **Touche Windows + R** pour activer la boîte « Exécuter », puis de taper « control » et d'appuyer sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-443.png)

* Sélectionnez l'option **Réseau et Internet** dans la fenêtre du Panneau de configuration.
* Cliquez sur l'option **Centre Réseau et partage**.
* Cliquez sur l'option **Résoudre les problèmes** située sous la rubrique « Modifier vos paramètres réseau ».
* Cliquez sur **Utilitaires de résolution de problèmes supplémentaires** -> **Connexions Internet** -> **Exécuter l'utilitaire de résolution de problèmes**

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-457.png)

L'étape suivante consiste à attendre la fin de la tâche. Si des messages d'erreur s'affichent, suivez simplement les étapes indiquées pour corriger le problème réseau concerné.

### Configurer manuellement votre serveur DNS

La source de votre problème peut être que votre serveur DNS est en panne. Dans ce cas, vous serez heureux de savoir que vous pouvez changer manuellement votre serveur DNS. 

Vous pouvez passer, par exemple, au DNS public de Google ou à celui de CloudFlare. Pour changer votre serveur DNS, suivez ces étapes :

* Ouvrez votre Panneau de configuration.
* Cliquez sur l'option **Réseau et Internet**.
* Cliquez sur l'option **Centre Réseau et partage**.
* Dans la fenêtre **Centre Réseau et partage**, cliquez sur votre connexion active. Par exemple, cliquez sur « Ethernet » ou « Wi-Fi » selon votre connexion actuelle.
* Dans la boîte de dialogue qui s'affiche, cliquez sur le bouton « Propriétés ».
* Vous verrez une liste sous la rubrique « Cette connexion utilise les éléments suivants ».
* Dans cette liste, sélectionnez « Internet Protocol Version 4 (TCP/IPv4) » puis cliquez sur le bouton « Propriétés ».

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-445.png)

* Une autre boîte de dialogue s'ouvrira avec deux champs : « Serveur DNS préféré » et « Serveur DNS auxiliaire ».
* Cliquez d'abord sur le bouton radio **Utiliser l'adresse de serveur DNS suivante**.
* Pour utiliser le serveur DNS public de Google, entrez 8.8.8.8 dans le champ « Serveur DNS préféré » et 8.8.4.4 dans le champ « Serveur DNS auxiliaire ».

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-446.png)

* Vous pouvez également utiliser le serveur DNS de CloudFlare. L'adresse DNS de CloudFlare est simplement 1.1.1.1
* Une fois les paramètres saisis, assurez-vous que la case « Valider les paramètres en quittant » est cochée.
* Cliquez sur « OK » pour enregistrer vos nouveaux paramètres.
* Redémarrez votre ordinateur.

### Vider le cache DNS

Vous pouvez vider le cache DNS, ce qui peut résoudre le problème « Le serveur DNS ne répond pas ». Cette action effacera les adresses IP et autres données liées au DNS de votre cache.

Vous pouvez vider le cache DNS en exécutant une commande via l'invite de commandes.

Pour ouvrir l'invite de commandes, appuyez sur **Touche Windows + R**, tapez « cmd » et appuyez sur **Maj+Ctrl+Entrée** pour l'exécuter en tant qu'administrateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-458.png)

Dans l'invite de commandes, tapez la commande suivante : `ipconfig /flushdns` et appuyez sur Entrée. Si la commande s'est exécutée avec succès, vous verrez un message de confirmation.

### Désactiver le protocole Internet version 6

Au moment de la rédaction de cet article, l'Internet Protocol Version 6 est la dernière version du protocole Internet. Sa désactivation n'aura pas d'effets néfastes sur le fonctionnement de votre ordinateur, mais elle est connue pour corriger parfois l'erreur « Le serveur DNS ne répond pas ».

Pour désactiver l'IPv6 sous Windows 10, suivez ces étapes :

* Allez dans **Panneau de configuration** -> **Réseau et Internet** -> **Centre Réseau et partage**
* Cliquez sur la connexion concernée, par exemple « Wi-Fi »
* Cliquez sur le bouton « Propriétés ».
* Dans la liste, décochez l'élément intitulé « Internet Protocol Version 6 (TCP/IPv6) ».

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-448.png)

* Appuyez sur le bouton « OK ».

### Désactiver temporairement votre pare-feu et votre antivirus

Si votre pare-feu est Windows Defender, suivez ces étapes pour le configurer :

* Ouvrez le Panneau de configuration (**Touche Windows + R**, tapez « control »).
* Dans la zone de recherche en haut à droite, tapez « win ».

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-459.png)

* Cliquez sur « Pare-feu Windows Defender ».
* Cliquez sur « Autoriser une application ou une fonctionnalité via le Pare-feu Windows Defender ».

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-462.png)

* Cliquez sur le bouton « Modifier les paramètres ».

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-461.png)

* Dans la liste, trouvez le navigateur que vous utilisez (par exemple Google Chrome) et assurez-vous que les cases « Privé » et « Public » sont cochées.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-466.png)

* Essayez ensuite d'accéder au site Web pour voir si le problème est résolu.

Il est possible que votre pare-feu empêchait l'accès aux données externes. 

Notez qu'il n'est pas recommandé de laisser votre système sans protection antivirus indéfiniment. La désactivation de votre antivirus n'est recommandée que pour tester s'il est la cause de l'erreur.

Pour désactiver temporairement la protection antivirus de Microsoft Defender :

* Sélectionnez Démarrer et tapez « Sécurité Windows ».
* Sélectionnez l'application **Sécurité Windows**.
* Allez dans **Protection contre les virus et menaces**.
* Sous **Paramètres de protection contre les virus et menaces**, sélectionnez **Gérer les paramètres**.
* Désactivez la **Protection en temps réel**.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-467.png)

Tentez d'accéder au site Web pour tester si l'erreur persiste.

### Réinitialiser vos paramètres DNS

Pour réinitialiser vos paramètres DNS, suivez ces étapes :

* Exécutez l'invite de commandes en tant qu'administrateur (**Touche Windows + R**, tapez « cmd », **Maj + Ctrl + Entrée**).
* Tapez les commandes suivantes l'une après l'autre, en appuyant sur Entrée après chaque commande :

`ipconfig /registerdns`

`ipconfig /release`

`Ipconfig /renew`

`netsh winsock reset`

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-465.png)

Une fois ces commandes exécutées, fermez l'invite de commandes et redémarrez votre ordinateur.

### Mettre à jour le pilote de la carte réseau

Vous pouvez mettre à jour manuellement votre pilote, mais il est plus facile d'automatiser cette tâche. 

Vous pouvez utiliser un logiciel gratuit comme « Driver Easy » (https://www.drivereasy.com/download-free-version/). 

Avant d'exécuter ce type de logiciel, assurez-vous de créer un point de restauration du système. Cela vous offre une assurance au cas où un imprévu affecterait votre ordinateur.

Pour utiliser Driver Easy :

* Lancez le logiciel
* Cliquez sur le bouton « Analyser maintenant »
* Appuyez sur le bouton « Mettre à jour » à côté des pilotes obsolètes.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-455.png)

### Désactiver toutes les connexions réseau sauf celle que vous utilisez

Désactiver les connexions réseau supplémentaires (autres que celle que vous utilisez, comme le Wi-Fi) peut parfois corriger l'erreur.

* Appuyez sur **Touche Windows + R**.
* Tapez « ncpa.cpl » et appuyez sur Entrée.
* Faites un clic droit sur les connexions inutilisées et sélectionnez « Désactiver ». Répétez l'opération pour toutes les connexions sauf celle que vous utilisez.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-456.png)

### Redémarrez votre ordinateur en mode sans échec

Le mode sans échec charge Windows avec un ensemble limité de pilotes et de fichiers, ce qui aide à diagnostiquer la cause du problème par élimination. 

Pour démarrer en mode sans échec :

* Appuyez sur **Touche Windows + I** pour ouvrir les Paramètres.
* Sélectionnez **Mise à jour et sécurité** -> **Récupération**.
* Sous **Démarrage avancé**, sélectionnez **Redémarrer maintenant**.
* Une fois sur l'écran « Choisir une option », sélectionnez **Dépannage** -> **Options avancées** -> **Paramètres de démarrage** -> **Redémarrer**.
* Après le redémarrage, sélectionnez **5** ou appuyez sur **F5** pour le Mode sans échec avec prise en charge réseau.

Essayez d'accéder au site Web. Si le problème ne se produit pas en mode sans échec, cela signifie qu'un logiciel tiers est probablement la cause. Vous pouvez alors désinstaller vos logiciels récents un par un pour identifier le coupable.

## Conclusion

L'erreur « Le serveur DNS ne répond pas » est relativement courante et, heureusement, assez simple à corriger. 

Il peut être extrêmement frustrant d'être privé d'Internet, mais nous espérons que les solutions proposées dans cet article vous aideront à retrouver l'accès à vos sites Web préférés.