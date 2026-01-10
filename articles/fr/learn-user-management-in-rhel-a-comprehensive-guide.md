---
title: 'Apprendre la gestion des utilisateurs dans RHEL : Un guide complet'
subtitle: ''
author: Tanishka Makode
co_authors: []
series: null
date: '2025-02-19T13:18:02.159Z'
originalURL: https://freecodecamp.org/news/learn-user-management-in-rhel-a-comprehensive-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739971027992/d19c4616-4c2e-4cc4-ac45-384e6520d1a8.png
tags:
- name: Linux
  slug: linux
- name: RHEL
  slug: rhel
- name: user management
  slug: user-management
seo_title: 'Apprendre la gestion des utilisateurs dans RHEL : Un guide complet'
seo_desc: 'Imagine you''re throwing a house party. You wouldn’t hand out keys to every
  guest, right? Some friends can roam freely, some should probably stick to the living
  room, and a few—well, let’s just say they need supervision.

  Managing users in RHEL is kind...'
---

Imaginez que vous organisez une fête chez vous. Vous ne donneriez pas les clés à chaque invité, n'est-ce pas ? Certains amis peuvent se déplacer librement, d'autres devraient probablement rester dans le salon, et quelques-uns—eh bien, disons qu'ils ont besoin de supervision.

Gérer les utilisateurs dans RHEL est un peu comme cela. Vous décidez qui entre, ce qu'ils peuvent faire et combien de contrôle ils ont. Sans une gestion appropriée, les choses peuvent rapidement devenir chaotiques—comme cet ami qui se met à faire le DJ sans que personne ne le demande.

Alors, plongeons dans la gestion des utilisateurs et assurons-nous que votre système Linux reste organisé, sécurisé et sans drame ! 🚀

## Table des matières

1. [Qu'est-ce qu'un utilisateur dans Linux ?](#heading-quest-ce-quun-utilisateur-dans-linux)
    
    * [Comprendre sudo dans la gestion des utilisateurs](#heading-comprendre-sudo-dans-la-gestion-des-utilisateurs)
        
2. [Commandes de gestion des utilisateurs dans Linux](#heading-commandes-de-gestion-des-utilisateurs-dans-linux)
    
    * [Comment ajouter un utilisateur](#heading-comment-ajouter-un-utilisateur)
        
    * [Comment vérifier si un utilisateur est créé](#heading-comment-verifier-si-un-utilisateur-est-cree)
        
    * [Comment attribuer un mot de passe](#heading-comment-attribuer-un-mot-de-passe)
        
    * [Comment changer d'utilisateur](#heading-comment-changer-dutilisateur)
        
    * [Comprendre les groupes dans Linux](#heading-comprendre-les-groupes-dans-linux)
        
    * [Comment modifier les utilisateurs](#heading-comment-modifier-les-utilisateurs)
        
3. [Mots de la fin](#heading-mots-de-la-fin)
    

## **Qu'est-ce qu'un utilisateur dans Linux ?**

Un utilisateur dans Linux est un compte qui permet à quelqu'un (ou à un processus) d'interagir avec le système. Puisque Linux est un système d'exploitation multi-utilisateurs, plusieurs utilisateurs peuvent exister sur le même système, chacun avec ses propres paramètres, fichiers et permissions. Les utilisateurs peuvent avoir différents niveaux de permissions, qui déterminent ce qu'ils peuvent accéder ou modifier sur le système.

Linux catégorise les utilisateurs en trois types principaux en fonction de leurs rôles et privilèges :

1. Utilisateurs privilégiés : Ces utilisateurs ont un accès illimité à l'ensemble du système. Ils ont le niveau de permissions le plus élevé et peuvent effectuer toute opération sur le système. Ils peuvent installer/supprimer des logiciels, modifier des fichiers système, créer/gérer des utilisateurs, et même tout supprimer. Ces utilisateurs sont également appelés utilisateurs root.
    
2. Utilisateurs système : Le système crée ces utilisateurs pour exécuter des processus ou services en arrière-plan. Ils ne peuvent pas se connecter comme un utilisateur normal. Leur seul but est de gérer les opérations système comme les bases de données, les serveurs web et les tâches planifiées.
    
3. Utilisateurs normaux : Ce sont les utilisateurs quotidiens créés par les administrateurs ou lors de l'installation du système. Ils ont leur répertoire personnel et peuvent stocker des fichiers et paramètres personnels. Ils ne peuvent pas modifier les fichiers système mais peuvent exécuter des tâches dans leur champ de permissions.
    

### Comprendre `sudo` dans la gestion des utilisateurs

La commande `sudo` (Superuser Do) permet à un utilisateur régulier d'exécuter des tâches administratives avec des privilèges élevés. Puisque les tâches de gestion des utilisateurs—comme l'ajout, la modification ou la suppression d'utilisateurs—nécessitent un accès root, les utilisateurs normaux doivent utiliser `sudo` avant ces commandes.

Notez que les commandes suivantes sont exécutées en tant qu'utilisateur root. Si vous utilisez un compte utilisateur normal, vous devez les précéder de `sudo` pour effectuer des tâches de gestion des utilisateurs.

Maintenant, voyons comment nous gérons les utilisateurs sur RHEL.

## Commandes de gestion des utilisateurs dans Linux

### Comment ajouter un utilisateur

Pour créer un nouveau compte utilisateur, utilisez la commande suivante :

Syntaxe :

```bash
useradd [nom_utilisateur]
```

Exemple :

```bash
useradd Tanishka # Utilisateur root
sudo useradd Tanishka # Utilisateur normal
```

Une fois que vous avez créé un utilisateur, vous pouvez vérifier son existence dans le fichier `/etc/passwd`. Ce fichier stocke les informations essentielles du compte utilisateur (mais **pas les mots de passe**, malgré le nom).

#### Comment vérifier si un utilisateur est créé

Pour confirmer l'entrée de l'utilisateur dans `/etc/passwd`, utilisez l'une des méthodes suivantes :

1. Afficher le fichier en utilisant `cat` ou `grep`
    

```bash
cat /etc/passwd # Affiche tout le contenu du fichier
grep Tanishka /etc/passwd # Affiche les informations sur l'utilisateur Tanishka uniquement
```

2. Utiliser la commande id :
    

La commande `id` est utilisée pour afficher l'**UID (Identifiant d'utilisateur), le GID (Identifiant de groupe) et les groupes auxquels l'utilisateur appartient**. Elle aide à vérifier les informations de l'utilisateur et à vérifier les permissions.

```bash
id Tanishka
# Affiche l'identifiant de l'utilisateur Tanishka,
# confirmant ainsi que l'utilisateur a été créé
```

Comprenons ce qui se passe dans les champs de /etc/password. Chaque ligne dans `/etc/passwd` représente un compte utilisateur et contient sept champs séparés par des deux-points (`:`):

```bash
nom_utilisateur:x:UID:GID:commentaire:repertoire_personnel:shell
```

| **Champ** | **Description** |
| --- | --- |
| nom_utilisateur | Nom de l'utilisateur (par exemple, john, admin). |
| x | Espace réservé pour le mot de passe (le mot de passe réel est stocké dans /etc/shadow). |
| UID | Identifiant d'utilisateur (par exemple, 1001 pour un utilisateur normal, 0 pour root). |
| GID | Identifiant de groupe (groupe principal de l'utilisateur). |
| commentaire | Description optionnelle de l'utilisateur (par exemple, nom complet ou autres infos). |
| repertoire_personnel | Répertoire personnel de l'utilisateur (par exemple /home/john). |
| shell | Le shell par défaut attribué à l'utilisateur (par exemple, /bin/bash, /bin/sh, /usr/sbin/nologin). |

### Comment attribuer un mot de passe

Une fois un compte créé, il est essentiel d'attribuer un mot de passe au compte. Sinon, ce compte ne peut pas se connecter via une interface de connexion graphique. Pour donner un mot de passe à un compte utilisateur, utilisez cette commande :

Syntaxe :

```bash
passwd [nom_utilisateur]
```

Exemple :

```bash
passwd Tanishka
```

Vous serez invité à entrer le mot de passe. Entrez le mot de passe et vous êtes prêt ! Même si les informations de l'utilisateur sont stockées dans le fichier /etc/passwd, les informations réelles sur le mot de passe sont stockées dans le fichier /etc/shadow (bizarre, je sais...).

Pour voir le contenu du fichier /etc/shadow, utilisez cette commande :

```bash
cat /etc/shadow
```

Chaque ligne dans `/etc/shadow` représente un mot de passe de compte utilisateur et contient neuf champs séparés par des deux-points (`:`):

```bash
nom_utilisateur:mot_de_passe:derniere_modif:min:max:avertissement:inactif:expiration:reserve
```

| Champ | Description |
| --- | --- |
| nom_utilisateur | Nom de connexion de l'utilisateur |
| mot_de_passe | Mot de passe chiffré ou état du mot de passe (par exemple, verrouillé) |
| derniere_modif | Dernière modification du mot de passe (jours depuis le 1er janvier 1970) |
| min | Jours minimum entre les changements de mot de passe |
| max | Jours maximum avant que le changement de mot de passe soit requis |
| avertissement | Période d'avertissement avant l'expiration du mot de passe |
| inactif | Période d'inactivité après l'expiration du mot de passe |
| expiration | Date d'expiration du compte (jours depuis le 1er janvier 1970) |
| reserve | Réservé pour une utilisation future |

Pour changer les informations de vieillissement du mot de passe, vous utilisez la commande `chage` (abréviation de change age) comme ceci :

Syntaxe :

```bash
chage [OPTIONS] [nom_utilisateur]
```

Exemple :

```bash
chage -l tanishka # Liste les informations actuelles de vieillissement du mot de passe
chage -m 10 tanishka # Définit le nombre minimum de jours pour changer le mot de passe
chage -M 10 tanishka # Définit le nombre maximum de jours avant que le mot de passe doive être changé
chage -W 7 tanishka # Définit le nombre de jours avant l'expiration du mot de passe où l'utilisateur sera averti de changer le mot de passe
chage -I 10 tanishka # Définit le nombre de jours après l'expiration du mot de passe où le compte sera désactivé si non connecté
chage -E 2025-12-31 tanishka # Définit la date à laquelle le compte utilisateur expirera
chage -d 2024-12-25 tanishka # Définit la date de la dernière modification du mot de passe
```

Maintenant que vous avez appris à créer des utilisateurs et à attribuer des mots de passe, vous devez savoir comment changer d'utilisateur. Voyons cela maintenant.

### Comment changer d'utilisateur

La commande `su` (Substitute User) vous permet de **changer d'un utilisateur à un autre** sans vous déconnecter de la session actuelle.

Syntaxe :

```bash
su - [nom_utilisateur]
```

Exemple :

```bash
su - Tanishka # Passe à l'utilisateur Tanishka
```

* `su` signifie "substitute user" (ou "switch user").
    
* Le `-` (tiret) charge l'environnement complet de l'utilisateur cible, y compris son shell, son chemin et ses paramètres de profil (similaire à une connexion en tant que cet utilisateur).
    
* Si aucun nom d'utilisateur n'est fourni, il passe à l'utilisateur root par défaut.
    

Pour revenir à l'utilisateur d'origine ou root, entrez simplement 'exit'.

### Comprendre les groupes dans Linux

Tout comme dans une fête où les invités peuvent appartenir à différents cercles sociaux, les groupes Linux permettent aux utilisateurs de faire partie de différents niveaux de permissions. Les groupes aident à gérer l'accès aux fichiers, les privilèges système et les contrôles administratifs de manière efficace.

Linux a deux types de groupes :

**1. Groupe principal :**

* Chaque utilisateur a un groupe principal.
    
* Lorsqu'un utilisateur crée un nouveau fichier, il appartient à son groupe principal.
    
* Il est généralement nommé de la même manière que le nom d'utilisateur.
    

**2. Groupes secondaires :**

* Un utilisateur peut appartenir à plusieurs groupes secondaires.
    
* Ces groupes fournissent des permissions supplémentaires au-delà du groupe principal.
    
* Les utilisateurs peuvent être assignés à divers groupes secondaires pour accéder à des ressources partagées.
    

Pour vérifier l'appartenance à un groupe d'un utilisateur :

```bash
id [nom_utilisateur]
```

Cela affiche l'UID de l'utilisateur, le groupe principal (GID) et tous les groupes secondaires auxquels il appartient.

Pour ajouter un nouveau groupe :

```bash
groupadd [nom_groupe]
```

### Comment modifier un utilisateur

Parfois, vous devrez peut-être mettre à jour les détails d'un utilisateur, comme changer les noms d'utilisateur, les identifiants d'utilisateur, les appartenances à des groupes, les répertoires personnels ou les shells de connexion. Vous utilisez la commande `usermod` pour modifier les comptes utilisateurs existants tout en préservant leurs fichiers et configurations.

Syntaxe :

```bash
usermod [OPTIONS] [nom_utilisateur]
```

Décomposons les différentes options disponibles pour modifier les comptes utilisateurs.

1. **Changer le nom d'utilisateur**
    

Si vous souhaitez renommer un utilisateur existant, utilisez l'option `-l` :

Syntaxe :

```bash
usermod -l nouveau_nom_utilisateur ancien_nom_utilisateur
```

Exemple :

```bash
usermod -l tanishkamakode tanishka
```

Cela renomme `tanishka` en `tanishkamakode`. Gardez simplement à l'esprit que le répertoire personnel reste le même (`/home/tanishka`), vous devrez donc peut-être le renommer manuellement.

Pour renommer également le répertoire personnel, utilisez :

```bash
mv /home/tanishka /home/tanishkamakode
```

2. **Changer l'identifiant d'utilisateur :**
    

Chaque utilisateur a un identifiant d'utilisateur (UID) unique. Si vous devez le changer, utilisez `-u`.

Syntaxe :

```bash
usermod -u nouvel_UID nom_utilisateur
```

Exemple :

```bash
usermod -u 2001 tanishka
```

Cela change l'UID de `tanishka` en `2001`. Avant de faire cela, vous voudrez **vous assurer qu'aucun autre utilisateur n'a le même UID**. C'est important.

Si l'utilisateur possède des fichiers sous l'ancien UID, vous devriez les mettre à jour après avoir changé l'UID.

3. **Changer le groupe principal**
    

Chaque utilisateur appartient à un groupe principal. Pour le changer, utilisez `-g`.

Syntaxe :

```bash
usermod -g nouveau_groupe nom_utilisateur
```

Exemple :

```bash
usermod -g developers tanishka
```

Cela change le groupe principal de `tanishka` en `developers`. Gardez simplement à l'esprit que `usermod -g developers tanishka` **supprime** l'utilisateur de tous les groupes secondaires. Pour éviter cela, assurez-vous simplement de vérifier et de réajouter les groupes secondaires si nécessaire.

De plus, le groupe doit exister au préalable. Pour créer un groupe, exécutez cette commande :

Syntaxe :

```bash
groupadd [nom_groupe]
```

Exemple :

```bash
groupadd developers
```

Maintenant, pour vérifier le groupe de tanishka, faites ce qui suit :

```bash
id tanishka
```

4. **Ajouter à un groupe secondaire**
    

Un utilisateur peut appartenir à plusieurs groupes secondaires. Utilisez `-G` pour les assigner.

Syntaxe :

```bash
usermod -G groupe1,groupe2 nom_utilisateur
```

Exemple :

```bash
usermod -G linux,docker tanishka
```

Cela ajoute `tanishka` aux groupes `sudo` et `docker`. Gardez simplement à l'esprit que cela **remplace** tous les groupes secondaires existants auxquels l'utilisateur pourrait déjà appartenir. Pour ajouter des groupes sans supprimer les groupes actuels, utilisez `-aG` (ajouter aux groupes) comme ceci :

```bash
usermod -aG linux,docker tanishka
```

5. **Changer le répertoire personnel :**
    

Vous pouvez changer le répertoire personnel par défaut d'un utilisateur en utilisant `-d`.

Syntaxe :

```bash
usermod -d /nouveau/repertoire_personnel nom_utilisateur
```

Exemple :

```bash
usermod -d /home/tani tanishka
```

Cela définit le répertoire personnel de `tanishka` à `/home/tani`, mais **il ne déplace pas les fichiers existants**. Pour les déplacer, ajoutez l'option `-m` :

```bash
usermod -d /home/tani -m tanishka
```

Après avoir déplacé le répertoire personnel, assurez-vous simplement d'avoir mis à jour la propriété des fichiers.

6. **Changer le shell de connexion :**
    

Le shell par défaut pour un utilisateur peut être changé en utilisant `-s`.

Syntaxe :

```bash
usermod -s /nouveau/shell nom_utilisateur
```

Exemple :

```bash
usermod -s /bin/zsh tanishka
```

Cela change le shell par défaut de `tanishka` en `zsh`. Les shells courants incluent :

* `/bin/bash` (par défaut)
    
* `/bin/sh`
    
* `/bin/zsh`
    
* `/usr/sbin/nologin` (pour désactiver la connexion)
    

Avec `usermod`, vous pouvez ajuster les paramètres utilisateur pour correspondre aux exigences du système. Vérifiez toujours les changements en utilisant :

```bash
id tanishka
grep tanishka /etc/passwd
```

## Mots de la fin

Dans cet article, nous avons exploré les fondamentaux de la gestion des utilisateurs dans RHEL, un aspect crucial de l'administration système. Nous avons commencé par la création et la gestion des utilisateurs, puis nous sommes passés à la gestion des groupes.

Si vous êtes nouveau dans Linux et que vous souhaitez construire une base solide, consultez mon premier tutoriel sur les [Commandes de base de Linux](https://www.freecodecamp.org/news/guide-to-rhel-linux-basics/), où je couvre les commandes essentielles que tout débutant devrait connaître. Vous pouvez également lire mon deuxième tutoriel sur [Vim](https://www.freecodecamp.org/news/how-to-use-the-vim-text-editor-intro-for-devs/) pour apprendre à naviguer et à éditer du texte efficacement dans cet éditeur puissant. Ces articles compléteront ce que vous avez appris sur la gestion des utilisateurs ici.

Continuez à pratiquer ces commandes, et bientôt elles deviendront une seconde nature pour vous. La maîtrise vient avec la répétition, alors continuez à expérimenter et à appliquer ces fondamentaux dans des scénarios réels.

Restez à l'écoute pour plus d'articles. Préparez-vous à faire passer vos compétences RHEL au niveau supérieur.

[Connectons-nous !](https://linktr.ee/tanishkamakode)