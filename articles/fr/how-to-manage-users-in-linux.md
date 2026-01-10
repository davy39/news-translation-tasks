---
title: Comment gérer les utilisateurs dans Linux
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2023-09-06T00:08:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-users-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/gabriel-heinzer-xbEVM6oJ1Fs-unsplash-1.jpg
tags:
- name: Linux
  slug: linux
- name: management
  slug: management
- name: Security
  slug: security
seo_title: Comment gérer les utilisateurs dans Linux
seo_desc: Linux is an open-source operating system that is widely used in various
  applications due to its flexibility, stability, and security. One of the fundamental
  aspects of Linux is user management, which enables administrators to control access
  to resour...
---

Linux est un système d'exploitation open-source largement utilisé dans diverses applications en raison de sa flexibilité, de sa stabilité et de sa sécurité. L'un des aspects fondamentaux de Linux est la gestion des utilisateurs, qui permet aux administrateurs de contrôler l'accès aux ressources et de maintenir la sécurité du système.

Dans le monde rapide de la technologie, une gestion efficace des utilisateurs est cruciale pour maintenir un environnement Linux sécurisé et bien organisé. Cet article sert de guide complet pour la gestion des utilisateurs dans Linux, en se concentrant sur les besoins de CTechCo, une entreprise technologique hypothétique.

En comprenant les divers aspects de la gestion des utilisateurs, qui inclut la création, la modification et la suppression de comptes utilisateurs, la mise en œuvre de l'authentification des utilisateurs. En suivant les meilleures pratiques de gestion des utilisateurs, CTechCo peut assurer la sécurité et la productivité de ses systèmes Linux.

# Table des matières

* [Qu'est-ce que les utilisateurs dans Linux ?](#heading-quest-ce-que-les-utilisateurs-dans-linux)
* [Types d'utilisateurs dans Linux](#heading-types-dutilisateurs-dans-linux)
* [Propriétés des comptes utilisateurs](#heading-proprietes-des-comptes-utilisateurs)
* [Comment créer des utilisateurs](#heading-comment-creer-des-utilisateurs)
* [Comment supprimer des utilisateurs](#heading-comment-supprimer-des-utilisateurs)
* [Comment modifier les comptes utilisateurs](#heading-comment-modifier-les-comptes-utilisateurs)
* [Gestion des mots de passe](#heading-gestion-des-mots-de-passe)
* [Gestion des groupes](#heading-gestion-des-groupes)
* [Authentification des utilisateurs](#heading-authentification-des-utilisateurs)
* [Meilleures pratiques pour la gestion des utilisateurs dans Linux](#heading-meilleures-pratiques-pour-la-gestion-des-utilisateurs-dans-linux)
* [Principe du moindre privilège](#heading-principe-du-moindre-privilege)
* [Permissions des utilisateurs](#heading-permissions-des-utilisateurs)
* [Surveillance et audit](#heading-surveillance-et-audit)
* [Formation des utilisateurs](#heading-formation-des-utilisateurs)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que les utilisateurs dans Linux ?

Dans un système Linux, les utilisateurs désignent des individus ou des entités qui interagissent avec le système d'exploitation en se connectant et en effectuant diverses tâches. La gestion des utilisateurs joue un rôle crucial dans la garantie d'un contrôle d'accès sécurisé, l'allocation des ressources et l'administration du système.

Un utilisateur dans Linux est associé à un compte utilisateur, qui se compose de plusieurs propriétés définissant son identité et ses privilèges au sein du système. Ces propriétés sont un nom d'utilisateur, un UID (User ID), un GID (Group ID), un répertoire personnel, un shell par défaut et un mot de passe.

Chaque compte utilisateur possède ces propriétés uniques listées ci-dessus.

## Types d'utilisateurs dans Linux

Linux prend en charge deux types d'utilisateurs : les utilisateurs système et les utilisateurs réguliers.

**Les utilisateurs système** sont créés par le système lors de l'installation et sont utilisés pour exécuter les services et applications système.

**Les utilisateurs réguliers** sont créés par l'administrateur et peuvent accéder au système et à ses ressources en fonction de leurs permissions.

Rencontrons la main-d'œuvre diversifiée de CTechCo, composée d'individus qui interagissent avec le système Linux par le biais de comptes utilisateurs. Rencontrons John, un développeur ; Lisa, une administratrice système ; et Sarah, une responsable marketing. Ils ont chacun des noms d'utilisateur uniques tels que "johndoe", "lisasmith" et "sarahsmith", respectivement. Ces noms d'utilisateur servent d'identification au sein du système Linux.

## Comment créer des utilisateurs

L'administrateur système de CTechCo, Alex, doit créer des comptes utilisateurs pour John, Lisa et Sarah. Alex lance le processus en utilisant la commande `useradd`. Par exemple, pour créer le compte de John, Alex exécute la commande suivante :

```bash
useradd -u 1002 -d /home/john -s /bin/bash john
```

Cette commande crée le compte de John avec l'uid (`-u`) 1002, le répertoire personnel (`-d`) **/home/john** et définit (`-s`) **/bin/bash** comme son shell par défaut.

De même, Alex créera un compte utilisateur pour Lisa et Sarah en utilisant le même format.

Alex peut vérifier le nouveau compte utilisateur en exécutant la commande `id` :

```bash
id john
```

Cela affichera l'ID utilisateur et les appartenances aux groupes pour l'utilisateur "john".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/id-john.png)
_informations uid, gid et groupes pour l'utilisateur john_

## Propriétés des comptes utilisateurs

Au sein de l'environnement Linux de CTechCo, les comptes utilisateurs possèdent diverses propriétés qui définissent leurs caractéristiques et leurs privilèges d'accès. Explorons ces propriétés dans le contexte de notre cas d'utilisation.

1. **Nom d'utilisateur** : Chaque utilisateur se voit attribuer un nom d'utilisateur unique qui sert d'identifiant au sein du système Linux. Par exemple, le nom d'utilisateur de John est "john".
2. **UID (User ID) et GID (Group ID)** : Chaque compte utilisateur est associé à un UID et un GID. L'UID est une valeur numérique attribuée à l'utilisateur, tandis que le GID représente le groupe principal auquel l'utilisateur appartient. Par exemple, l'UID de John peut être `1002`, et le GID de son groupe principal est également `1002`.
3. **Répertoire personnel** : Chaque utilisateur dispose d'un répertoire personnel désigné où résident ses fichiers et paramètres personnels. Le répertoire personnel de John est **/home/john**.
4. **Shell par défaut** : Le shell par défaut détermine l'interpréteur de commandes utilisé lorsqu'un utilisateur se connecte. Il définit l'environnement interactif de l'utilisateur. Dans notre cas, le shell par défaut de John est défini sur **/bin/bash**, qui est un shell populaire dans Linux.
5. **Mot de passe** : Les comptes utilisateurs nécessitent des mots de passe pour s'authentifier et accéder au système. Les utilisateurs de CTechCo, y compris John, doivent créer des mots de passe forts pour garantir la sécurité.
6. **Groupe** : L'appartenance à un groupe détermine quelles ressources système l'utilisateur peut accéder, ainsi que quels utilisateurs peuvent accéder aux fichiers de l'utilisateur.

Alex pourrait examiner les utilisateurs sur leur Linux en exécutant la commande `cat /etc/passwd`. Les utilisateurs seront affichés dans ce format :

```bash
john:x:1002:1002:,,,:/home/john:/bin/bash
```

Voici ce que représente chacun des champs dans le format ci-dessus :

* `john` : Il s'agit du nom d'utilisateur du compte utilisateur.
* `x` : Ce champ contient le mot de passe chiffré de l'utilisateur. Il est remplacé par un caractère 'x' pour indiquer que le mot de passe est stocké dans le fichier `/etc/shadow` pour des raisons de sécurité.
* `1002` : Il s'agit de l'UID (User ID) du compte utilisateur, qui est un identifiant numérique unique attribué à l'utilisateur par le système.
* `1002` : Il s'agit du GID (Group ID) du compte utilisateur, qui représente l'appartenance au groupe principal de l'utilisateur.
* `,,,` : Il s'agit du champ GECOS, qui signifie "General Electric Comprehensive Operating System". Ce champ est utilisé pour stocker des informations supplémentaires sur l'utilisateur, telles que son nom complet ou ses coordonnées. Dans ce cas, le champ est vide, car aucune information supplémentaire n'a été fournie lors de la création du compte utilisateur.
* `/home/john` : Il s'agit du répertoire personnel du compte utilisateur, qui est l'emplacement où sont stockés les fichiers et les données personnelles de l'utilisateur.
* `/bin/bash` : Il s'agit du shell par défaut pour le compte utilisateur, qui est l'interpréteur de commandes utilisé pour traiter les commandes saisies par l'utilisateur dans le terminal. Dans ce cas, le shell par défaut est Bash, qui est le shell le plus couramment utilisé dans Linux.

## Comment supprimer des utilisateurs

Supposons que Lisa ait quitté CTechCo. Pour supprimer son compte et les fichiers associés, Alex doit utiliser la commande `userdel`. Par exemple, pour supprimer le compte de Lisa, Alex exécute :

```bash
sudo userdel lisa
```

Cela supprimera le compte utilisateur pour `lisa`, ainsi que son répertoire personnel et tous les fichiers ou répertoires appartenant à l'utilisateur.

## Comment modifier les comptes utilisateurs

À mesure que la main-d'œuvre de CTechCo évolue, l'équipe informatique peut avoir besoin d'apporter des ajustements aux comptes utilisateurs. Explorons comment ils peuvent modifier les comptes utilisateurs pour répondre aux besoins et permissions changeants.

Par exemple, John (le développeur) se voit confier des responsabilités supplémentaires au sein de l'entreprise. Pour refléter ce changement, l'équipe informatique peut modifier le compte de John en utilisant la commande `usermod`. Considérons le scénario suivant :

### Comment modifier les groupes d'utilisateurs dans Linux

CTechCo crée un nouveau groupe appelé `development` pour gérer l'accès aux ressources liées au développement. Pour ajouter John au groupe `development`, la commande suivante peut être utilisée :

`sudo usermod -aG development john`

Cette commande ajoute John au groupe `development`, lui accordant les privilèges d'accès nécessaires.

### Comment changer le shell par défaut dans Linux

Dans le cas où John préfère utiliser un shell différent du shell par défaut **/bin/bash**. L'équipe informatique peut modifier son compte en conséquence. Par exemple, pour changer le shell par défaut de John en **/bin/zsh**, la commande suivante peut être utilisée :

`sudo usermod -s /bin/zsh john`

Cette commande met à jour le compte de John pour utiliser le nouveau shell par défaut — **/bin/zsh**.

Vous pouvez exécuter à nouveau la commande `cat /etc/passwd` pour voir que le shell pour john a changé de **/bin/bash** à **/bin/zsh**.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/zsh.png)

## Gestion des groupes

Une gestion efficace des groupes est cruciale pour contrôler l'accès aux ressources au sein de l'environnement Linux de CTechCo. Explorons comment l'équipe informatique peut créer et gérer des groupes pour garantir un contrôle d'accès approprié.

### Comment créer un nouveau groupe dans Linux

Pour créer un nouveau groupe, tel que le groupe `marketing`, la commande suivante peut être utilisée :

`sudo groupadd marketing`

La commande ci-dessus crée le groupe `marketing`, qui peut être utilisé pour accorder des permissions spécifiques et un accès aux ressources liées au marketing.

Pour afficher le groupe que vous venez d'ajouter, exécutez la commande suivante :

```bash
cat /etc/group
```

Cela retourne tous les groupes sur votre machine Linux et lorsque vous faites défiler vers le bas, vous pouvez trouver les groupes les plus récents.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/linux-group.png)

Vous pouvez également utiliser la commande pour retourner un groupe spécifique (`marketing` dans notre cas) :

```bash
cat /etc/group | grep marketing
```

### Comment assigner des utilisateurs à des groupes dans Linux

Une fois un groupe créé, des utilisateurs peuvent y être ajoutés. Par exemple, pour ajouter Sarah (la responsable marketing) au groupe `marketing`, la commande suivante peut être utilisée :

`sudo usermod -aG marketing sarahsmith`

Cette commande ajoute Sarah au groupe `marketing`, lui permettant d'accéder aux ressources associées à ce groupe.

## Gestion des mots de passe

Assurer des pratiques de gestion des mots de passe est essentiel pour maintenir la sécurité des comptes utilisateurs au sein de l'environnement Linux de CTechCo. Explorons comment l'équipe informatique peut imposer des politiques de mots de passe et gérer efficacement les mots de passe des utilisateurs.

**Définition des politiques de mots de passe :** L'équipe informatique peut établir des politiques de mots de passe pour imposer des mots de passe forts, y compris des exigences de complexité, l'expiration des mots de passe et le verrouillage des comptes. Ces politiques peuvent être configurées dans le fichier **/etc/login.defs**.

**Changement des mots de passe des utilisateurs :** Les utilisateurs doivent être encouragés à changer leurs mots de passe périodiquement. Ils peuvent le faire en utilisant la commande `passwd`. Par exemple, John peut changer son mot de passe avec la commande suivante :

`sudo passwd john`

Cette commande invite John à entrer son mot de passe actuel, puis lui permet de définir un nouveau mot de passe sécurisé.

## Authentification des utilisateurs

L'authentification des utilisateurs est un aspect crucial de la gestion des utilisateurs dans Linux, garantissant que seuls les utilisateurs autorisés peuvent accéder au système. CTechCo peut employer divers mécanismes d'authentification pour sécuriser leur environnement Linux.

### Authentification basée sur le mot de passe

L'authentification basée sur le mot de passe est la méthode la plus courante pour l'authentification des utilisateurs dans Linux. Lorsque les utilisateurs se connectent, ils fournissent leur nom d'utilisateur et leur mot de passe correspondant pour authentifier leur identité.

Par exemple, John se connecte au système en entrant son nom d'utilisateur et son mot de passe à l'invite de connexion. Le système vérifie ensuite le mot de passe fourni par rapport au hachage du mot de passe stocké associé au compte de John.

### Authentification basée sur les clés SSH

L'authentification basée sur les clés SSH (Secure Shell) offre une alternative plus sécurisée à l'authentification basée sur le mot de passe. Les utilisateurs génèrent une paire de clés publique-privée, où la clé publique est stockée sur le serveur et la clé privée est conservée en sécurité sur l'appareil de l'utilisateur.

Avec l'authentification basée sur les clés SSH, des utilisateurs comme Lisa, une administratrice système chez CTechCo, peuvent s'authentifier sans entrer de mot de passe. Au lieu de cela, le serveur vérifie l'identité de l'utilisateur en fonction de la possession de la clé privée.

Pour configurer l'authentification basée sur les clés SSH pour Lisa, les étapes suivantes peuvent être suivies :

1. Générer une paire de clés SSH sur la machine de Lisa en utilisant la commande `ssh-keygen`.
2. Copier la clé publique dans le fichier **/home/lisasmith/.ssh/authorized_keys** du serveur.
3. Configurer le serveur pour permettre l'authentification basée sur les clés SSH.

## Meilleures pratiques pour la gestion des utilisateurs dans Linux

Pour garantir la sécurité et l'efficacité de la gestion des utilisateurs dans Linux, CTechCo peut suivre plusieurs meilleures pratiques. Ces pratiques minimisent les risques de sécurité et améliorent le processus de gestion global.

### Principe du moindre privilège

Le principe du moindre privilège (PoLP) est un concept fondamental dans la gestion des utilisateurs. Il stipule que les utilisateurs ne doivent se voir accorder que les privilèges minimaux nécessaires pour accomplir leurs tâches efficacement.

CTechCo peut appliquer le PoLP pour limiter l'accès des utilisateurs et atténuer l'impact des éventuelles violations de sécurité. Par exemple, John se voit accorder des privilèges administratifs en utilisant la commande `sudo` uniquement lorsque cela est requis pour des tâches spécifiques. En exécutant la commande suivante, John peut exécuter des commandes avec des permissions élevées :

`sudo command`

### Permissions des utilisateurs

L'équipe informatique de CTechCo peut attribuer des permissions appropriées aux utilisateurs et aux groupes pour contrôler l'accès aux fichiers, répertoires et ressources. Ils peuvent utiliser la commande `chmod` pour définir les permissions pour les fichiers et répertoires, telles que les permissions de lecture, d'écriture et d'exécution pour le propriétaire, le groupe et les autres.

Par exemple, pour accorder des permissions de lecture et d'écriture au propriétaire et des permissions de lecture seule au groupe et aux autres, la commande suivante peut être utilisée :

`chmod 640 filename`

Pour afficher les permissions du fichier, vous pouvez utiliser la commande `ls -l`. Cela affichera les permissions du fichier dans le format suivant :

```bash
-rw-r--r-- 1 username username 0 Apr 5 11:24 filename.txt
```

Dans le format ci-dessus, les trois premiers caractères représentent les permissions du fichier pour le propriétaire du fichier.

Les trois caractères suivants représentent les permissions pour les membres du groupe du fichier.

Les trois derniers caractères représentent les permissions pour tous les autres utilisateurs.

Dans ce cas, le propriétaire du fichier a les permissions de **lecture** et d'**écriture**, tandis que les membres du groupe et tous les autres utilisateurs n'ont que les permissions de lecture.

### Surveillance et audit

CTechCo peut mettre en œuvre des mécanismes de surveillance et d'audit pour suivre les activités des utilisateurs et identifier les éventuelles violations de sécurité. Ils utilisent des outils comme auditd pour collecter et analyser les journaux système, leur permettant de détecter les activités suspectes et de prendre des mesures appropriées.

Par exemple, l'équipe informatique peut configurer auditd pour surveiller les fichiers et répertoires système critiques, ainsi que les connexions des utilisateurs et les commandes administratives.

De plus, pour afficher les journaux système dans Linux, Alex peut utiliser la commande `tail`. Par exemple, pour afficher les 10 dernières lignes du fichier journal système, vous pouvez utiliser la commande suivante :

```bash
sudo tail /var/log/syslog
```

### Formation des utilisateurs

CTechCo reconnaît l'importance de la formation des utilisateurs pour maintenir un environnement Linux sécurisé. Ils peuvent organiser des sessions de formation régulières pour éduquer les utilisateurs sur la sécurité des mots de passe, les meilleures pratiques de gestion des données et la sensibilisation aux attaques d'ingénierie sociale.

De plus, ils peuvent encourager les utilisateurs à signaler rapidement toute activité suspecte ou incident de sécurité, favorisant ainsi une culture de sensibilisation et de responsabilité en matière de sécurité.

En adhérant à ces meilleures pratiques, CTechCo peut garantir un processus de gestion des utilisateurs robuste et minimiser les risques de sécurité dans leur environnement Linux.

## Conclusion

Gérer les utilisateurs dans un environnement Linux est essentiel pour maintenir un système sécurisé et organisé. Dans le contexte de CTechCo, nous avons exploré divers aspects de la gestion des utilisateurs et de l'authentification, tels que :

* Le concept des utilisateurs dans Linux, leurs types et leurs rôles au sein du système.
* Les propriétés des comptes utilisateurs, telles que les noms d'utilisateur, les UID, les GID, les répertoires personnels, les shells par défaut et les mots de passe.
* Les tâches de gestion des utilisateurs, y compris la création, la suppression et la modification de comptes utilisateurs avec l'utilisation de commandes comme `useradd`, `userdel` et `usermod`.
* Le fonctionnement de la gestion des groupes en utilisant les commandes `groupadd` et `usermod`.
* Les mécanismes d'authentification des utilisateurs, y compris l'authentification basée sur le mot de passe et l'authentification basée sur les clés SSH.
* Les meilleures pratiques pour la gestion des utilisateurs, telles que le suivi du principe du moindre privilège.
* L'utilisation de la commande `sudo` pour les permissions élevées.
* Les permissions des utilisateurs et le contrôle d'accès configurés via la commande `chmod`.
* La surveillance et l'audit des activités des utilisateurs en utilisant des outils comme `auditd`.
* Les programmes de formation et de sensibilisation des utilisateurs pour promouvoir la sécurité des mots de passe et les meilleures pratiques de gestion des données.

Nous avons commencé par comprendre le concept des utilisateurs dans Linux, y compris leurs rôles et leur importance au sein du système. Nous avons discuté des différents types d'utilisateurs, tels que les utilisateurs réguliers et les utilisateurs système, et de leurs propriétés de compte respectives, y compris les noms d'utilisateur, les UID, les GID, les répertoires personnels, les shells par défaut et les mots de passe.

Passant à la gestion des utilisateurs, nous avons couvert le processus de création, de suppression et de modification de comptes utilisateurs. Nous avons vu comment les commandes `useradd`, `userdel` et `usermod` peuvent être utilisées pour effectuer ces opérations. De plus, nous avons exploré la gestion des groupes, où la commande `groupadd` est utilisée pour créer des groupes et la commande `usermod` est utilisée pour assigner des utilisateurs à des groupes.

Les mécanismes d'authentification des utilisateurs ont également été discutés. Nous avons examiné l'authentification basée sur le mot de passe, où les utilisateurs fournissent leur nom d'utilisateur et leur mot de passe pour vérification. De plus, nous avons exploré l'authentification basée sur les clés SSH, plus sécurisée, qui repose sur des paires de clés publique-privée.

Nous avons mis en avant certaines meilleures pratiques que CTechCo pourrait suivre, comme le principe du moindre privilège, accordant aux utilisateurs uniquement les privilèges nécessaires pour leurs tâches. Ils peuvent utiliser la commande `sudo` pour des permissions élevées lorsque cela est requis. Les permissions des utilisateurs, configurées via la commande `chmod`, sont mises en œuvre pour contrôler l'accès aux fichiers et répertoires. Les mécanismes de surveillance et d'audit, tels que l'utilisation de l'outil `auditd`, sont employés pour suivre les activités des utilisateurs et détecter les éventuelles violations de sécurité. De plus, des programmes de formation et de sensibilisation des utilisateurs peuvent être menés pour éduquer les utilisateurs sur la sécurité des mots de passe, les meilleures pratiques de gestion des données et la sensibilisation à l'ingénierie sociale.

En incorporant ces meilleures pratiques, l'équipe informatique de CTechCo peut garantir un processus de gestion des utilisateurs sécurisé, minimisant les risques de sécurité et maintenant un environnement Linux bien structuré.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).