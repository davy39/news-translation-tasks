---
title: snapd simplifie l'administration de Nextcloud
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-14T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/snapd-nextcloud
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/cisco-1.png
tags:
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
seo_title: snapd simplifie l'administration de Nextcloud
seo_desc: As I’ve described in both my Linux in Action book and Linux in Motion course,
  Nextcloud is a powerful way to build a file sharing and collaboration service using
  only open source software running on your own secure infrastructure. It’s DropBox,
  Skype...
---

Comme je l'ai décrit dans mon [livre Linux in Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9) et mon [cours Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1), Nextcloud est un moyen puissant de créer un service de partage de fichiers et de collaboration en utilisant uniquement des logiciels open source exécutés sur votre propre infrastructure sécurisée. C'est DropBox, Skype et Google Docs réunis en un seul, mais sans le verrouillage des fournisseurs, les craintes de sécurité et de confidentialité.

Bien que la plateforme soit certainement bien conçue et polie, l'installation initiale peut être délicate. Vous cherchez une preuve ? Essayez d'installer manuellement Nextcloud sur un serveur Ubuntu 18.04 en utilisant l'une des instructions détaillées disponibles sur Internet. Parfois, tout se passe bien, mais pas toujours. Vous pourriez rencontrer des paquets qui ne sont plus pris en charge par les dépôts officiels en amont ou des dépendances modifiées. Ne blâmez pas les personnes qui ont écrit ces guides : blâmez le rythme du changement dans les dépôts officiels de logiciels Linux.

## Utiliser snapd pour installer Nextcloud

Il existe une meilleure façon, mais elle a son propre côté obscur.

Comme je [l'ai écrit dans cet article](https://www.freecodecamp.org/news/aws-s3-based-enterprise-network-file-sharing-using-nextcloud/), le système de gestion de paquets snapd de Canonical a été conçu pour simplifier la distribution sûre et prévisible de logiciels sur plusieurs distributions et versions Linux. Et cela fonctionne. Prenez le snap Nextcloud. Plutôt que d'investir 15 minutes, beaucoup de frappe dans le terminal — et un sérieux dépannage lorsque les choses ne se passent pas comme vous l'aviez espéré — la préparation de la pile logicielle sous-jacente sur votre serveur pour Nextcloud fonctionne avec une seule commande :

```
snap install nextcloud
```

C'est tout. Non, vraiment. Le système snap va mettre en place un serveur Nextcloud fonctionnel pour vous, complet avec des couches backend exécutant des instances autonomes de MySQL, Apache, Redis et PHP. Essayez-le vous-même sur votre machine Linux [avec snap activé](https://docs.snapcraft.io/installing-snapd/6735).

Jusqu'à présent, tout va bien. Vous pouvez maintenant configurer manuellement un compte administrateur et attribuer un mot de passe (espérons-le meilleur que celui de cet exemple) :

```
nextcloud.manual-install admin password
```

Une étape de plus. Par défaut, Nextcloud acceptera les requêtes HTTP adressées à _localhost_ depuis le serveur lui-même. Mais, comme ce sera généralement le cas, vous allez probablement configurer les choses sur un serveur distant ou virtuel (comme une instance AWS EC2, par exemple). Vous devrez donc indiquer à Nextcloud d'accepter les requêtes de navigateur distantes faites à votre adresse IP ou nom de domaine. Voici à quoi cela pourrait ressembler. Notez comment vous attribuez un numéro d'ID séparé (1 et 2 dans cet exemple) pour chaque domaine.

```
nextcloud.occ config:system:set trusted_domains 1 \
    --value=nextcloud.bootstrap-it.com$ nextcloud.occ \ 
    config:system:set trusted_domains 2 \
    --value=192.168.2.45
```

Ces valeurs seront enregistrées dans le fichier config.php, que vous pouvez lire vous-même.

```
cat /var/snap/nextcloud/current/nextcloud/config/config.php
```

Avec cela fait, vous devriez maintenant pouvoir naviguer vers l'adresse IP du serveur Nextcloud (ou le nom de domaine) et vous connecter à la console d'administration en utilisant les identifiants d'administrateur que vous avez configurés juste avant. Je vous laisse explorer l'interface par vous-même.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-133.png)
_L'interface utilisateur de Nextcloud_

## Dépannage et administration de Nextcloud

Mais j'ai bien dit que le snap Nextcloud avait son côté obscur, n'est-ce pas ? Eh bien, supposons que quelque chose tourne mal. Supposons que, un beau jour, vos utilisateurs soient empêchés de se connecter normalement à l'interface utilisateur de Nextcloud. Même les tentatives de connexion des utilisateurs administrateurs échouent. Votre première et seule option à ce stade est de vous connecter en SSH au serveur.

Je suis sûr que ce ne sera pas votre première expérience d'administration sur un serveur Linux. Vous portez une ceinture à outils bien garnie et — pour être honnête — vous attendez avec impatience le défi.

Mais attendez ! Qu'est-ce que c'est ? Le répertoire _/etc/_ ne contient aucun fichier ayant une connexion évidente avec les services Apache, Redis et MySQL que vous savez être en cours d'exécution, et les logs dans _/var/log/_ sont tous mystérieusement silencieux. Même _systemctl status_ n'offre aucun espoir. Tant pis pour votre ceinture à outils Linux bien garnie.

Puis, comme le proverbial coup de tonnerre, cela vous frappe : vous avez installé Nextcloud en utilisant snapd. Toutes les anciennes règles ne s'appliquent pas. Où allez-vous chercher de l'aide pour cela ? Eh bien, si je peux humblement suggérer, vous pourriez commencer par [lire mon article sur la gestion des snaps Ubuntu](https://www.freecodecamp.org/news/aws-s3-based-enterprise-network-file-sharing-using-nextcloud/). Cela expliquera où snapd cache les fichiers de configuration importants basés sur snap sur votre système de fichiers. Cela vous présentera également quelques outils d'administration snap utiles.

Cependant, le reste de cet article se concentrera sur les outils en ligne de commande propres au projet Nextcloud — des outils qui peuvent vous aider à traverser quelques sérieux tours de magie d'administration.

Vous avez déjà vu la CLI de Nextcloud à l'œuvre lorsque vous avez créé votre utilisateur administrateur et ajouté un ou deux nouveaux domaines de confiance. Une autre étape importante de configuration consiste à ajouter le chiffrement TLS à votre service web. Les chances sont que vous utiliseriez normalement l'outil [certbot](https://certbot.eff.org/) de l'Electronic Freedom Frontier pour obtenir un certificat gratuit de Let's Encrypt. Mais cela ne fonctionnera pas ici... à cause de snap. Au lieu de cela, vous exécuterez l'outil propre à Nextcloud pour demander et installer un certificat Let's Encrypt :

```
nextcloud.enable-https lets-encrypt
```

Mais pour un aperçu complet de toute la gamme des opérations CLI disponibles, exécutez _nextcloud.occ_. Vous verrez une longue liste de fonctionnalités avec leurs descriptions et quelques conseils de syntaxe. Passez quelques minutes à parcourir ce que cette commande a affiché sur votre machine.

```
nextcloud.occ
```

Vous pourriez, par exemple, lister toutes les applications actuellement disponibles pour Nextcloud, organisées par Activées ou Désactivées.

```
nextcloud.occ app:list
Enabled:
  - accessibility: 1.1.0
  - activity: 2.8.2
  - calendar: 1.6.4
  - cloud_federation_api: 0.1.0
  - comments: 1.5.0
  - dav: 1.8.1
  - federatedfilesharing: 1.5.0
  - federation: 1.5.0
[..]
```

Votre prochaine étape pourrait être de désactiver l'une des applications actuellement activées (ou vice versa) :

```
nextcloud.occ app:disable calendar
```

Vous pouvez utiliser _app:update_ pour mettre à jour manuellement toutes les applications ou des applications spécifiques :

```
nextcloud.occ app:update --all
spreed new version available: 5.0.3
spreed updated
```

Quelqu'un a oublié un mot de passe ? Vous pouvez le réinitialiser :

```
nextcloud.occ user:resetpassword admin2
Enter a new password: 
Confirm the new password: 
Successfully reset password for admin2
```

Je suis sûr que vous commencez à comprendre : vous utilisez des commandes de haut niveau — comme _app_, _user_, et _maintenance_ — et vous ajoutez un deux-points puis une commande secondaire comme _list_. Tout est bien organisé en domaines assez intuitifs. Voici quelques exemples :

```
nextcloud.occ app:list
nextcloud.occ user:add
nextcloud.occ maintenance:repair
```

Enfin, la commande _status_ imprimera quelques informations de version de base :

```
nextcloud.occ status
  - installed: true
  - version: 15.0.7.0
  - versionstring: 15.0.7
  - edition:
```

Je pense que vous avez les bases dont vous aurez besoin pour vous repérer. Le reste dépend de vous.

_Vous cherchez plus ? Vous pourriez aimer mes [livres et cours Pluralsight](https://bootstrap-it.com/) sur les sujets liés à Linux, AWS et Docker._