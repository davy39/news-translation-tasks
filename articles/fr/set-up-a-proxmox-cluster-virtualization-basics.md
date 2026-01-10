---
title: Comment configurer un cluster Proxmox gratuitement – Les bases de la virtualisation
subtitle: ''
author: Shamsuddoha Ranju
co_authors: []
series: null
date: '2025-04-14T13:49:54.511Z'
originalURL: https://freecodecamp.org/news/set-up-a-proxmox-cluster-virtualization-basics
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744488492225/62339e66-50ae-4546-8845-f5c86c415511.png
tags:
- name: proxmox
  slug: proxmox
- name: clustering
  slug: clustering
- name: virtualization
  slug: virtualization
- name: KVM
  slug: kvm
seo_title: Comment configurer un cluster Proxmox gratuitement – Les bases de la virtualisation
seo_desc: Virtualization is a game-changer for developers, hobbyists, and IT enthusiasts.
  It lets you run multiple operating systems on one machine, which is perfect for
  testing apps, hosting servers, or learning new tech. If you want to take it further,
  clust...
---

La virtualisation est un changement de jeu pour les développeurs, les passionnés et les enthousiastes de l'informatique. Elle permet d'exécuter plusieurs systèmes d'exploitation sur une seule machine, ce qui est parfait pour tester des applications, héberger des serveurs ou apprendre de nouvelles technologies. Si vous souhaitez aller plus loin, le clustering relie plusieurs machines pour plus de puissance et de flexibilité. Et vous pouvez utiliser Proxmox Virtual Environment (VE) pour construire un cluster gratuitement – aucune licence coûteuse n'est requise.

Dans ce tutoriel, vous allez configurer un cluster Proxmox à 3 nœuds en utilisant trois ordinateurs (ou machines virtuelles pour la pratique). À la fin, vous aurez un cluster fonctionnel prêt à héberger des machines virtuelles (VM) et à expérimenter des fonctionnalités intéressantes comme la migration des invités et la réplication des VM, etc.

Plongeons-nous dans le sujet !

## Prérequis : Ce que vous devez savoir

Ce guide est adapté aux débutants pour le clustering, mais vous aurez besoin de quelques compétences de base pour suivre. Vous devez être à l'aise avec :

* L'installation d'un système d'exploitation à partir d'une clé USB (ne vous inquiétez pas, je vous guiderai à travers les étapes).

* L'utilisation d'un terminal pour des commandes simples comme `ping` ou `nano`.

* La configuration d'un réseau domestique avec des IP statiques (par exemple, connaître la plage d'IP de votre routeur). Aucune expérience avancée en virtualisation ou en clustering n'est requise – je vous expliquerai les concepts clés au fur et à mesure.

## Ce dont vous aurez besoin

* **Trois ordinateurs (ou VM) :** Commencez avec au moins 8 Go de RAM et 100 Go de stockage par machine, plus un CPU capable de virtualisation (la plupart des modèles modernes fonctionnent). Ces spécifications sont une base – la RAM et le stockage réels dépendent du nombre de VM que vous souhaitez héberger (par exemple, plus de VM nécessitent plus de ressources).

* **Proxmox VE :** Gratuit et open-source. Téléchargez l'ISO depuis [proxmox.com](http://proxmox.com).

* **Connexion réseau :** Les trois machines doivent être sur le même réseau et pouvoir se pinguer mutuellement.

* **Un navigateur web :** Pour l'interface web de Proxmox.

* **30–60 minutes :** Selon votre rythme de configuration.

## Pourquoi Proxmox et le clustering ?

Proxmox VE est une plateforme de virtualisation gratuite et open-source construite sur Debian Linux. Elle utilise KVM pour les VM (systèmes entièrement virtualisés) et LXC pour les conteneurs (environnements d'applications légers), le tout géré via une interface web élégante.

Le clustering signifie lier plusieurs machines Proxmox – appelées nœuds – afin qu'elles agissent comme un seul système. Pensez à cela comme à une équipe : chaque nœud partage la charge de travail, et vous les contrôlez depuis un seul tableau de bord. Cette configuration vous permet de déplacer (migrer) des VM entre les nœuds, d'augmenter la fiabilité et d'expérimenter la haute disponibilité (HA) – où les VM redémarrent automatiquement (sur un nœud sain) si un nœud tombe en panne.

De plus, Proxmox offre une fonctionnalité de réplication pratique : elle peut synchroniser les données des VM entre les nœuds automatiquement, gardant des sauvegardes prêtes en cas de problème.

C'est une compétence indispensable pour le DevOps, les tests d'applications ou le bricolage informatique.

## 2 Nœuds vs. 3 Nœuds : Lequel choisir ?

Avant de construire votre cluster à 3 nœuds, explorons vos options. Le clustering peut commencer avec 2 nœuds ou aller jusqu'à 3 (ou plus). Voici pourquoi vous pourriez choisir l'un plutôt que l'autre :

* **Cluster à 2 Nœuds :**

  * **Avantages :** Configuration plus facile avec seulement deux machines. Idéal pour apprendre les bases ou pour de petits projets. Utilise moins de matériel.

  * **Inconvénients :** Pas de quorum – une majorité de votes pour maintenir le cluster en fonctionnement si un nœud tombe en panne – donc la HA n'est pas fiable. Vous auriez besoin d'un truc supplémentaire (comme un dispositif de quorum) pour éviter les blocages.

  * **Idéal pour :** L'apprentissage, les tests de clustering, ou les ressources limitées.

* **Cluster à 3 Nœuds :**

  * **Avantages :** Quorum intégré – deux nœuds sur trois maintiennent les choses en marche si l'un tombe en panne. Idéal pour la pratique de la HA. Plus stable et évolutif.

  * **Inconvénients :** Nécessite une machine supplémentaire et un peu plus de temps de configuration.

  * **Idéal pour :** Les apprenants sérieux ou les petites configurations de production.

Nous opterons pour 3 nœuds – c'est le juste milieu pour la stabilité et les compétences du monde réel.

## Étape 1 : Installer Proxmox VE sur les trois machines

Tout d'abord, téléchargez l'ISO de Proxmox VE depuis [proxmox.com](http://proxmox.com). Créez une clé USB bootable avec Rufus (Windows), `dd` (Linux/macOS), ou Raspberry Pi Imager (disponible pour toutes les plateformes).

Pour `dd`, utilisez cette commande (remplacez les espaces réservés par votre ISO et votre périphérique USB) :

```plaintext
sudo dd if=proxmox-ve.iso of=/dev/sdX bs=1M status=progress oflag=sync
```

![Écran d'installation de Proxmox VE montrant le disque cible pour la configuration du stockage.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744492694669/777f8642-67dd-4f5f-8e78-b98c0d77ccca.png align="center")

Démarrez chaque machine à partir de la clé USB et suivez l'installateur. Restez avec le schéma de partitionnement par défaut (il utilise le système de fichiers EXT4) et définissez des IP statiques et des noms d'hôte comme suit (ou vous pouvez utiliser vos propres IP en connaissant la plage d'IP de votre routeur) :

* Nœud 1 : `172.20.1.101` [nom d'hôte : `node01.local`]

* Nœud 2 : `172.20.1.102` [nom d'hôte : `node02.local`]

* Nœud 3 : `172.20.1.103` [nom d'hôte : `node03.local`]

![Écran d'installation de Proxmox VE montrant la configuration réseau avec le nom d'hôte et l'IP saisis pour le Nœud 1.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744491592723/4b793ada-e21a-4da1-92f1-dd05ad130980.png align="center")

Après l'installation, chaque nœud affiche son IP sur la console (par exemple, [https://172.20.1.101:8006](https://192.168.10.101:8006)). Testez-le en ouvrant un navigateur, en visitant chaque IP et en vous connectant avec root et votre mot de passe. Vous verrez le tableau de bord Proxmox.

## Étape 2 : Préparer vos nœuds

Maintenant, préparons vos nœuds à communiquer entre eux – une étape cruciale pour le clustering. Sans cela, ils ne se reconnaîtront pas correctement.

Mettez à jour `/etc/hosts` sur les trois nœuds pour mapper les IP aux noms d'hôte (puisque nous n'utilisons pas de serveur DNS). Ouvrez le fichier avec :

`nano /etc/hosts`

Ajoutez ces lignes (IP et noms d'hôte) sur chaque nœud :

```plaintext
172.20.1.101 node01.local node01
172.20.1.102 node02.local node02
172.20.1.103 node03.local node03
```

![Fenêtre de terminal affichant le fichier /etc/hosts dans l'éditeur nano avec les entrées IP et nom d'hôte pour trois nœuds Proxmox.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744492087833/bb9cb873-f107-4fcd-b53f-25408531975e.png align="center")

Enregistrez et quittez (`Ctrl+O`, `Entrée`, `Ctrl+X`). Cela garantit que les nœuds peuvent résoudre les noms des autres (par exemple, node01 ping node02.local).

Ensuite, vérifiez la connectivité. Depuis la console du Nœud 1 (ou SSH), pinguez les autres :

`ping 172.20.1.102`

`ping 172.20.1.103`

Répétez depuis le Nœud 2 et le Nœud 3. Si les pings échouent, vérifiez votre réseau ou votre pare-feu.

Enfin, synchronisez leurs horloges – les clusters ont besoin d'un temps précis pour se coordonner. Sur chaque nœud, exécutez :

`ntpdate pool.ntp.org`

Les trois nœuds sont maintenant prêts pour le clustering.

## Étape 3 : Créer le cluster sur le Nœud 1

Configurons le cluster en commençant par le Nœud 1. Connectez-vous à son interface web à l'adresse [https://172.20.1.101:8006](https://192.168.10.101:8006). Dans la barre latérale de gauche, cliquez sur Datacenter, puis sur Cluster. Cliquez sur le bouton Créer un cluster, et une boîte de dialogue s'affiche. Nommez votre cluster – appelons-le **MonCluster** et cliquez sur Créer. Une fenêtre de tâche apparaîtra, montrant le processus. Attendez quelques secondes jusqu'à ce que vous voyiez « TÂCHE OK » – cela signifie que votre cluster est actif et que le Nœud 1 est son premier membre. Nous pouvons maintenant ajouter les autres nœuds !

![Interface web de Proxmox montrant la boîte de dialogue Créer un cluster avec 'MonCluster' saisi.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744493528337/b5fb8aa1-e9b6-4028-b129-10d2c665f1b5.png align="center")

## Étape 4 : Ajouter le Nœud 2 et le Nœud 3 au cluster

Avec le cluster créé, ajoutons le Nœud 2 et le Nœud 3. Sur la page du cluster du Nœud 1, cliquez sur Informations de jointure, puis sur Copier les informations – cela copie une clé dont vous aurez besoin.

Ouvrez l'interface web du Nœud 2 ([https://172.20.1.102:8006](https://192.168.10.102:8006)), allez dans Datacenter > Cluster > Rejoindre le cluster, collez la clé dans le champ Informations, entrez le mot de passe root du Nœud 1, et cliquez sur Rejoindre **MonCluster**.

![Interface web de Proxmox montrant la boîte de dialogue Rejoindre le cluster avec les 'informations de jointure' saisies.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744494140010/d1f60b51-480c-44f1-84a1-bb37f79b6bc7.png align="center")

Répétez ce processus sur l'interface du Nœud 3 ([https://172.20.1.103:8006](https://192.168.10.103:8006)). Actualisez le tableau de bord du Nœud 1 – sous Datacenter, vous verrez les trois nœuds avec des cochette verte.

![Interface web de Proxmox affichant la vue Datacenter avec trois nœuds (node01, node02, node03) montrant des icônes de statut vertes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744495739410/4ce5c263-318d-4a21-94f4-324d30b0fc94.png align="center")

Votre cluster à 3 nœuds est opérationnel !

## Étape 5 : Tester votre cluster

Vérifions son fonctionnement en créant et en déplaçant une VM de test. Sur le Nœud 1, cliquez sur Créer une VM, nommez-la TestVM, ignorez l'ISO, et terminez avec les paramètres par défaut (aucun contenu de disque nécessaire). Cliquez sur le bouton Démarrer pour la démarrer.

Maintenant, migrons-la – la migration signifie déplacer la VM d'un nœud à un autre pour tester la flexibilité de votre cluster. Faites un clic droit sur TestVM, sélectionnez Migrer, choisissez le Nœud 2, et cliquez sur Migrer. La VM s'arrête brièvement, se copie sur le Nœud 2, et redémarre (normal sans stockage partagé).

Répétez cela, en la migrant du Nœud 2 au Nœud 3. Si elle passe entre les nœuds avec succès, votre cluster est au top ! Avec trois nœuds, vous avez un quorum – essayez d'éteindre le Nœud 3 pour voir les autres rester actifs.

## Quelles sont les prochaines étapes ?

Vous avez construit un cluster Proxmox à 3 nœuds gratuitement – félicitations ! Allez plus loin avec :

* **Stockage partagé :** Ajoutez NFS ou un disque de rechange pour la migration en direct des VM (aucun arrêt/arrêt nécessaire).

* **Haute disponibilité :** Activez la HA – les VM redémarrent automatiquement sur un nœud sain si l'un tombe en panne.

* **Réplication des VM :** Configurez la réplication – synchronisez les données des VM entre les nœuds automatiquement, gardant des sauvegardes prêtes en cas de problème.

* **Montée en charge :** Ajoutez plus de nœuds ou essayez les conteneurs LXC.

Vérifiez l'état de santé de votre cluster à tout moment (depuis la console) avec :

`pvecm status`

## Conclusion

Vous venez de configurer un cluster Proxmox à 3 nœuds sans frais. C'est un terrain de jeu pour la virtualisation, la pratique du DevOps, ou même l'hébergement de petits projets. Partagez vos réflexions avec moi – j'adorerais savoir ce que vous en avez pensé.