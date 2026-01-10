---
title: 'Groupes d''utilisateurs Linux expliqués : comment ajouter un nouveau groupe,
  un nouveau membre de groupe et changer de groupes'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-12-13T17:57:00.000Z'
originalURL: https://freecodecamp.org/news/linux-user-groups-explained-how-to-add-a-new-group-a-new-group-member-and-change-groups
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eba740569d1a4ca3ebb.jpg
tags:
- name: Linux
  slug: linux
seo_title: 'Groupes d''utilisateurs Linux expliqués : comment ajouter un nouveau groupe,
  un nouveau membre de groupe et changer de groupes'
seo_desc: Linux allows multiple users to have access to the system at one time. Setting
  permissions protects users from each other. Users can be assigned to groups that
  are created for users who share privilege, security, and access. Files and devices
  may be g...
---

Linux permet à plusieurs utilisateurs d'avoir accès au système en même temps. La définition des permissions protège les utilisateurs les uns des autres. Les utilisateurs peuvent être assignés à des groupes qui sont créés pour des utilisateurs partageant des privilèges, une sécurité et un accès communs. Les fichiers et les périphériques peuvent se voir accorder un accès basé sur un utilisateur spécifique ou un groupe d'utilisateurs.

Les groupes sont souvent utilisés pour donner à leurs membres certaines permissions de modifier un fichier ou un répertoire.

Les deux principaux types de groupes sont les groupes primaires et les groupes secondaires. Le groupe primaire d'un utilisateur est le groupe par défaut associé au compte. Les répertoires et fichiers créés par l'utilisateur auront cet identifiant de groupe. Un groupe secondaire est tout groupe dont un utilisateur est membre, autre que le groupe primaire.

## **Création de groupes**

Créons deux groupes appelés "writers" et "editors". Utilisez la commande `groupadd` comme ceci (vous devrez peut-être utiliser `sudo` au début pour avoir la permission appropriée de créer un groupe) :

```
groupadd writers
groupadd editors
```

## **Création d'utilisateurs**

Vous avez peut-être déjà des utilisateurs à ajouter à votre groupe. Sinon, voici la syntaxe de base pour créer un utilisateur avec la commande `useradd` :

`useradd [options] username`

Voici la commande pour créer un utilisateur nommé "quincy". L'option `-m` créera le répertoire personnel de l'utilisateur pour correspondre au nom d'utilisateur. L'option `-p p4ssw0rd` crée un mot de passe pour l'utilisateur "p4ssw0rd".

`useradd -m quincy -p password`

L'utilisateur pourra changer son mot de passe avec la commande `passwd`. Il devra entrer son mot de passe actuel puis son nouveau mot de passe.

## **Ajout d'un utilisateur à un groupe**

Vous pouvez utiliser la commande `usermod` pour ajouter un utilisateur à un groupe. Voici comment ajouter l'utilisateur "quincy" au groupe "writers". Le paramètre `-a` signifie "ajouter" et le paramètre `-G` ajoute un groupe en tant que groupe secondaire.

`usermod -a -G writers quincy`

Lorsqu'un utilisateur est créé avec la commande `adduser`, l'utilisateur est automatiquement assigné à un groupe primaire portant le même nom que le nom d'utilisateur. Ainsi, actuellement, l'utilisateur "quincy" a un groupe primaire "quincy" et un groupe secondaire "writers".

Vous pouvez également ajouter un utilisateur à plusieurs groupes à la fois en séparant les noms de groupes par des virgules. `-G group1,group2,group3`.

La commande suivante change le groupe primaire de l'utilisateur quincy en "editors" :

`usermod -g editors quincy`

## **Retirer un utilisateur d'un groupe secondaire**

Pour retirer un utilisateur d'un groupe secondaire, vous devez écraser les groupes actuels de l'utilisateur avec un nouvel ensemble de groupes qui ne contient pas le groupe à retirer.

Tout d'abord, utilisez la commande `id` pour vérifier à quels groupes secondaires un utilisateur appartient :

`id -nG quincy`

Supposons que cela retourne `editors writers`, indiquant que quincy fait partie des groupes "editors" et "writers". Si vous souhaitez retirer le groupe "writers", utilisez cette commande :

`usermod -G editors quincy`

Cette commande définit le groupe secondaire de quincy comme "editors". Puisque le drapeau `-a` n'a pas été utilisé, l'ensemble précédent de groupes a été écrasé.

## **Conclusion**

Vous devriez maintenant être prêt à commencer à gérer les utilisateurs et les groupes. La prochaine étape consiste à déterminer quels privilèges chaque groupe aura.