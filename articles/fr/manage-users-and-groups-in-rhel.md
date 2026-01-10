---
title: Comment gérer les utilisateurs et les groupes dans Red Hat Enterprise Linux
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-08T17:41:44.000Z'
originalURL: https://freecodecamp.org/news/manage-users-and-groups-in-rhel
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/manage-users-and-groups-in-rhel-cover.jpg
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: Comment gérer les utilisateurs et les groupes dans Red Hat Enterprise Linux
seo_desc: 'To effectively safeguard your system and regulate access when working in
  Red Hat Enterprise Linux (RHEL), you''ll need to understand user and group management.

  This is a critical component that''s significant for both individual and complex
  network env...'
---

Pour protéger efficacement votre système et réguler l'accès lors de l'utilisation de Red Hat Enterprise Linux (RHEL), vous devrez comprendre la gestion des utilisateurs et des groupes.

Ceci est un composant critique qui est significatif pour les environnements individuels et complexes, car il est clé pour gérer habilement les comptes utilisateurs et les groupes.

Dans ce guide, nous allons plonger dans les fondamentaux de la gestion des utilisateurs et des groupes dans RHEL. Vous acquerrez les connaissances et les compétences nécessaires pour créer, modifier et optimiser les comptes utilisateurs et les groupes en fonction de vos besoins spécifiques en matière de sécurité et d'exploitation.

Vous apprendrez également les tenants et aboutissants de l'octroi des permissions utilisateurs et de la mise en œuvre des contrôles d'accès basés sur les groupes, et maîtriserez les outils essentiels et les méthodes éprouvées pour garantir l'intégrité robuste du système et réguler l'accès aux ressources.

## Prérequis

* Familiarité avec les commandes Linux de base. Vous pouvez lire mon précédent [tutoriel sur les commandes RHEL et les concepts clés](https://www.freecodecamp.org/news/red-hat-enterprise-linux-guide/) si vous avez besoin de vous rafraîchir la mémoire.

## **Table des Matières**

Voici ce que nous allons couvrir dans ce guide complet :

* [useradd](#heading-la-commande-useradd)

* [Qu'est-ce que sudo ?](#heading-quest-ce-que-sudo)

* [usermod](#heading-la-commande-usermod)

* [Qu'est-ce que /etc/login.defs ?](#heading-quest-ce-que-etclogindefs)

* [Qu'est-ce que /etc/skel ?](#heading-quest-ce-que-etcskel)

* [Qu'est-ce que /etc/shadow ?](#heading-quest-ce-que-etcshadow)

* [groupadd](#heading-la-commande-groupadd)

* [groupmod](#heading-la-commande-groupmod)

* [Exercice Pratique](#heading-exercice-pratique)

* [Conclusion](#heading-conclusion)

## La commande `useradd`

La commande `useradd` est un outil essentiel dans RHEL pour créer de nouveaux comptes utilisateurs. Cette commande ajoute non seulement les informations de l'utilisateur aux fichiers système, mais configure également leur répertoire personnel et les configurations par défaut.

### Syntaxe de la commande `useradd` :

```bash
useradd [options] username
```

## Qu'est-ce que sudo ?

Dans le monde de Linux/Unix, `sudo` signifie "Superuser Do". Essentiellement, c'est une commande qui accorde aux utilisateurs réguliers la capacité d'exécuter des commandes avec des permissions administratives complètes ou root. Cela est particulièrement utile pour les commandes qui peuvent être restreintes pour les utilisateurs réguliers pour des raisons de sécurité.

### Exemples :

Un petit rappel – si vous n'êtes pas actuellement connecté en tant qu'utilisateur root, assurez-vous d'utiliser `sudo` avant d'utiliser des commandes telles que `useradd` que nous allons discuter dans ce tutoriel. Considérez `sudo` comme un outil pratique qui vous accorde certaines des capacités de l'utilisateur root. Nous approfondirons ce sujet dans les futurs tutoriels.

Pour l'instant, je suis connecté en tant qu'utilisateur root. Je n'utiliserai donc pas `sudo` avant les commandes.

#### Créer un utilisateur :

```bash
useradd kedar
```

Cette commande crée un nouvel utilisateur appelé 'kedar' et configure un dossier personnel pour lui par défaut. Plus tard, nous en apprendrons davantage sur `useradd` et comment nous pouvons changer ces valeurs par défaut.

Dans RHEL, certaines valeurs sont déjà définies lors de la création d'un utilisateur, mais nous les explorerons plus en détail dans ce tutoriel.

#### Vérifier un utilisateur nouvellement ajouté :

```bash
tail -1 /etc/passwd
```

`/etc/passwd` sert de dépôt centralisé contenant des informations essentielles sur les comptes utilisateurs. La sortie de la commande ci-dessus sera affichée de la manière suivante :

```bash
kedar:x:1001:1001:John Doe:/home/john:/bin/bash
```

Si l'utilisateur a été ajouté avec succès, vous verrez la sortie ci-dessus. Il peut y avoir quelques changements, mais elle devrait être essentiellement la même.

Décortiquons cette sortie et essayons de la comprendre :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004542.svg align="left")

*Décortication de la sortie ci-dessus*

1. Nom d'utilisateur – le nom du compte utilisateur.

2. Placeholder de mot de passe (obsolète) – historiquement, ce champ contenait un caractère 'x', indiquant que le mot de passe crypté de l'utilisateur était stocké dans le fichier `/etc/shadow`.

3. Identifiant utilisateur (UID) – identifiant numérique unique attribué à l'utilisateur.

4. Identifiant de groupe (GID) – l'identifiant numérique du groupe principal associé à l'utilisateur.

5. Informations utilisateur (GECOS) – ce champ inclut généralement des informations supplémentaires comme le nom complet de l'utilisateur, les détails de contact, etc.

6. Répertoire personnel – le chemin vers le répertoire personnel de l'utilisateur.

7. Shell de connexion – le shell ou programme par défaut exécuté à la connexion pour l'utilisateur.

Une fois l'utilisateur créé, nous pouvons définir un mot de passe pour cet utilisateur. Cela ne peut être fait que depuis un compte root.

#### Définir un mot de passe pour un compte nouvellement créé

```bash
passwd kedar
```

Cela vous demandera de taper le mot de passe pour l'utilisateur kedar. Une fois le mot de passe défini, vous pouvez vous connecter à l'utilisateur kedar en utilisant l'interface graphique. La définition d'un mot de passe est importante si vous souhaitez vous connecter via l'interface graphique.

#### Définir différentes options pour l'utilisateur lors de la création d'un nouvel utilisateur

Maintenant que nous savons quelles options sont disponibles lors de la création d'un utilisateur, nous pouvons les définir selon nos besoins.

1. Identifiant utilisateur (`-u`)

```bash
useradd -u 1234 kedar
```

La commande ci-dessus avec l'option `-u` définira l'identifiant utilisateur à 1234 lors de la création de l'utilisateur kedar.

2. Groupe principal (`-g`)

```bash
useradd -g 1232 kedar
```

Si un groupe existant est présent et que vous connaissez l'identifiant de groupe ou le nom de groupe, vous pouvez ajouter ce groupe comme groupe principal pour l'utilisateur kedar.

3. Groupe secondaire (`-G`)

```bash
useradd -G developers kedar
```

L'utilisateur kedar sera ajouté à un groupe secondaire appelé developers qui existe déjà. Nous pouvons ajouter l'utilisateur à plusieurs groupes secondaires.

Considérez un groupe secondaire dans Linux comme une adhésion convoitée à un club pour les utilisateurs. Bien qu'ils soient automatiquement inclus dans un groupe principal lors de leur travail sur l'ordinateur, rejoindre des groupes secondaires permet aux utilisateurs d'étendre leur adhésion et d'obtenir l'accès à des fichiers et fonctionnalités supplémentaires.

Essentiellement, c'est comme faire partie de plusieurs groupes simultanément, offrant aux utilisateurs des privilèges supplémentaires et la capacité d'explorer différentes parties du système.

4. Informations utilisateur

```bash
useradd -c "2 Month Intern" kedar
```

Cela ajoute plus d'informations à l'utilisateur kedar en tant que "2 Month Intern". Cela sera affiché dans le fichier `/etc/passwd`.

5. Répertoire personnel

```bash
useradd -d /etc/kedar/home kedar
```

Maintenant, cela définira le répertoire personnel à `/etc/kedar/home` pour l'utilisateur kedar. Par défaut dans RHEL, le répertoire personnel, s'il n'est pas spécifié, est `/home/kedar`.

6. Shell de connexion

```bash
useradd -s /bin/shell kedar
```

Ici, l'utilisateur kedar aura accès au shell qui se trouve dans /bin/shell. Cela donnera accès au shell à l'utilisateur kedar.

L'accès /bin/bash concerne le shell par défaut d'un utilisateur lors de la connexion au système.

Dans le monde Linux, le shell /bin/bash est communément appelé le shell Bash, abréviation de "Bourne Again SHell", et est facilement disponible sur la plupart des distributions Linux. Lorsqu'un utilisateur se voit accorder l'accès /bin/bash, cela signifie qu'à la connexion, il sera accueilli avec l'interface de ligne de commande du shell Bash.

Ce shell puissant les équipe de la capacité d'interagir avec le système, d'exécuter des commandes et de lancer des scripts spécifiques à Bash en utilisant sa syntaxe et sa fonctionnalité uniques.

Étant donné son utilisation généralisée, ses capacités avancées et sa compatibilité avec une variété de langages de script et de tâches de ligne de commande, le shell /bin/bash est une option préférée pour de nombreux utilisateurs comme leur shell par défaut.

Si vous souhaitez supprimer l'accès au shell pour un utilisateur particulier, vous pouvez définir l'accès au shell comme suit : `/sbin/nologin`. Cela restreindra l'accès à cet utilisateur pour se connecter à leur compte jusqu'à ce que l'accès au shell soit défini sur `/bin/shell`.

```bash
useradd -s /sbin/nologin kedar
```

## La commande `usermod`

La commande usermod est super importante dans Linux. Elle aide les administrateurs à changer facilement les attributs des comptes utilisateurs après leur création. Cela permet de gagner du temps car vous n'avez pas à supprimer et à recréer les comptes. C'est une manière pratique de gérer les utilisateurs sans trop de tracas.

### Syntaxe de la commande `usermod` :

```bash
usermod [options] username
```

### Exemples :

#### Changer le nom d'utilisateur :

```bash
usermod -l newusername oldusername
```

Cette commande change le nom d'utilisateur de `oldusername` à `newusername`.

#### Changer l'identifiant utilisateur (UID) :

```bash
usermod -u <newUID> username
```

Cette commande remplace `<newUID>` par le nouvel UID souhaité pour l'utilisateur.

#### Changer l'identifiant de groupe (GID) :

```bash
usermod -g <newGID> username
```

Cette commande remplace `<newGID>` par le nouvel identifiant de groupe principal souhaité pour l'utilisateur.

#### Ajouter un utilisateur à des groupes supplémentaires :

```bash
usermod -aG group1,group2 username
```

Cette commande ajoute l'utilisateur à des groupes supplémentaires (`group1`, `group2`, etc.).

#### Changer le répertoire personnel :

```bash
usermod -d /newhome username
```

Cette commande change le répertoire personnel de l'utilisateur en `/newhome`.

#### Changer le shell par défaut :

```bash
usermod -s /bin/bash username
```

Cette commande change le shell par défaut pour l'utilisateur en `/bin/bash`.

#### Définir une date d'expiration pour le compte :

```bash
usermod -e YYYY-MM-DD username
```

Cette commande définit une date d'expiration (`YYYY-MM-DD`) pour le compte de l'utilisateur.

Vous pouvez explorer davantage cette commande en utilisant `man usermod`. Vous avez les mêmes options qu'avec `useradd` pour manipuler les informations d'un utilisateur lorsque vous utilisez la commande `usermod`.

## Qu'est-ce que `/etc/login.defs` ?

Le fichier `/etc/login.defs` est un fichier de configuration crucial qui définit les paramètres par défaut pour la connexion, les politiques de mot de passe et la création de comptes utilisateurs. Il peut être trouvé à l'emplacement habituel, /etc/login.defs, et joue un rôle clé dans la détermination des valeurs par défaut à l'échelle du système pour la gestion des utilisateurs et l'authentification.

Il existe également une plage fixe pour les UID des utilisateurs, comme le montre le tableau suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004563-1.svg align="left")

*Tableau des plages d'UID - Utilisateurs privilégiés : 0-99, Utilisateurs système : 201-999, Utilisateurs normaux : 1000-60000*

Le répertoire /etc/login.defs contient une variété de configurations par défaut. En accédant à ce répertoire, nous pouvons modifier ces paramètres selon nos préférences.

Ce fichier contient plusieurs options différentes que nous pouvons ajuster, certaines d'entre elles sont listées ci-dessous :

```bash
PASS_MAX_DAYS   90
PASS_MIN_DAYS   7
PASS_WARN_AGE   14
PASS_MIN_LEN    8

UID_MIN         1000
UID_MAX         60000
GID_MIN         1000
GID_MAX         60000

LOGIN_RETRIES   5
LOGIN_TIMEOUT   60
CREATE_HOME     yes
UMASK           077

ENCRYPT_METHOD  SHA512
CHFN_AUTH       yes
CHFN_RESTRICT   rwh
DEFAULT_HOME    /home
```

Maintenant, vous savez d'où viennent les paramètres par défaut lorsque nous créons un utilisateur. Vous pouvez changer ces paramètres selon vos besoins.

## Qu'est-ce que `/etc/skel` ?

Dans Linux et les systèmes similaires, le dossier `/etc/skel/` est comme un pack de démarrage pour les nouveaux utilisateurs. Il est appelé "skel" pour "skeleton" car il configure les bases pour les nouveaux utilisateurs.

Ce dossier contient un ensemble de fichiers et de dossiers qui sont copiés dans le dossier personnel d'un nouvel utilisateur. Chaque fois qu'un nouvel utilisateur est créé, ces fichiers essentiels de /etc/skel/ sont automatiquement placés dans leur dossier personnel, s'assurant qu'il a ce dont ils ont besoin pour commencer.

Cela aide à configurer un point de départ simple pour l'utilisateur. Il leur donne des configurations de base, des paramètres par défaut et parfois des fichiers d'exemple. Cette méthode garantit que chaque nouvel utilisateur commence avec une configuration standard et les fichiers requis.

Dans le dossier /etc/skel/, vous pourriez trouver des fichiers courants comme .bashrc, .profile, et des fichiers de configuration similaires.

## Qu'est-ce que `/etc/shadow` ?

Le fichier `/etc/shadow` est un composant crucial des systèmes d'exploitation basés sur Unix (comme Linux), car il sert de dépôt pour les mots de passe utilisateurs cryptés et d'autres données liées aux mots de passe. Cette mesure de sécurité améliorée dépasse les méthodes précédentes de stockage des mots de passe dans le fichier /etc/passwd.

Le fichier /etc/shadow contient des informations cruciales concernant les mots de passe des comptes utilisateurs. Chaque ligne du fichier représente un utilisateur particulier et est divisée en plusieurs champs, chacun séparé par un deux-points (:).

Ces champs incluent généralement le nom d'utilisateur, le mot de passe crypté (haché à l'aide d'un algorithme cryptographique, pas le mot de passe réel), le nombre de jours depuis le dernier changement de mot de passe (à partir du 1er janvier 1970), des informations sur l'expiration du mot de passe telles que l'âge minimum et maximum, et une période d'avertissement. Il spécifie également le nombre de jours d'inactivité autorisés avant que le compte ne soit verrouillé, et si le compte a une date d'expiration.

### Exemple d'entrée du fichier /etc/shadow

`user:$6$PswrdHash$E7KLkQIGo7mxG5vDi7JelC5D8L0qbg38z1/WgNhAZDpCoe2GyGB6JefT9ftb/Rfm3uZOlFkktj/SkJTfSJziO.:18830:0:90:7:::`

Où :

* `user` : Nom d'utilisateur

* `$6$PswrdHash$E7KLkQIG...` : Hachage du mot de passe crypté

1. **$1$** est MD5

2. **$2a$** est Blowfish

3. **$2y$** est Blowfish

4. **$5$** est SHA-256

5. **$6$** est SHA-512

6. **$y$** est yescrypt

Ces symboles aident à identifier l'algorithme de hachage utilisé pour chaque hachage de mot de passe stocké dans le fichier `/etc/shadow`. Par exemple, si vous voyez un hachage de mot de passe commençant par `$6$`, cela indique que le cryptage SHA-512 a été utilisé pour ce mot de passe particulier.

* `18830` : Date du dernier changement de mot de passe (jours depuis le 1er janvier 1970)

* `0` : Âge minimum du mot de passe

* `90` : Âge maximum du mot de passe

* `7` : Période d'avertissement du mot de passe

* Autres champs pour l'inactivité du compte et l'expiration

Accès : Afin d'accéder et de modifier le fichier `/etc/shadow`, vous devez avoir les permissions de l'utilisateur root ou des privilèges spécialisés accordés.

Modification : Pour une sécurité renforcée, il est conseillé d'utiliser des commandes désignées telles que `passwd`, qui gère le cryptage des mots de passe et met à jour le fichier /etc/shadow efficacement.

## La commande `groupadd`

Dans RHEL, vous utilisez la commande `groupadd` pour créer de nouveaux groupes sur le système. C'est une commande fondamentale pour gérer les groupes d'utilisateurs, permettant aux administrateurs système d'ajouter des groupes, de définir leurs propriétés et de définir leur appartenance.

Tous les paramètres par défaut pour les groupes sont dans `/etc/login.defs`. Le fichier /etc/login.defs contient des paramètres importants, tels que GID_MIN, qui détermine la valeur GID minimale pour les groupes réguliers, et GID_MAX, qui définit la valeur GID maximale. De plus, SYS_GID_MIN et SYS_GID_MAX déterminent les valeurs GID minimales et maximales pour les groupes système.

Ces paramètres jouent un rôle crucial dans la gestion des groupes au sein du système.

### Syntaxe de la commande `groupadd` :

```bash
groupadd [options] groupname
```

### Exemples :

#### Créer un groupe :

```bash
groupadd developers
```

La commande ci-dessus crée un nouveau groupe nommé "developers".

#### Attribuer un GID spécifique :

```bash
groupadd -g 1001 developers
```

Cette commande crée un groupe avec un GID spécifié (par exemple, GID 1001).

Vous pouvez explorer plus d'options selon vos besoins en utilisant la commande `man groupadd`. Cela vous donnera la documentation de la commande `groupadd`.

## La commande `groupmod`

La commande `groupmod` dans RHEL est un outil précieux pour les administrateurs système, car elle leur permet de modifier facilement les attributs des groupes existants.

Avec cette commande puissante, vous pouvez modifier des groupes sans avoir besoin de les recréer, ce qui en fait un atout crucial pour la maintenance du système.

### Syntaxe de la commande `groupmod` :

```bash
groupmod [options] groupname
```

### Exemples :

#### Changer le nom du groupe :

```bash
groupmod -n newgroupname oldgroupname
```

Cette commande change le nom du groupe de `oldgroupname` à `newgroupname`.

#### Changer le GID (Identifiant de groupe) :

```bash
groupmod -g <newGID> groupname
```

Cette commande change le GID du groupe en `<newGID>`.

#### Ajouter un groupe à des groupes supplémentaires :

```bash
groupmod -aG group1,group2 groupname
```

Cette commande ajoute le groupe à des groupes supplémentaires (`group1`, `group2`, etc.).

#### Ajouter des utilisateurs à un groupe :

```bash
groupmod -m -m user1,user2 developers
```

Cela ajoutera user1 et user2 au groupe developers.

#### Supprimer des utilisateurs d'un groupe :

```bash
groupmod -M user1,user2 developers
```

Cela supprimera user1 et user2 du groupe developers.

Vous pouvez explorer plus d'options selon vos besoins en utilisant la commande `man groupmod`. Cela vous donnera la documentation de la commande `groupmod`.

## Exercice Pratique

### Exercice 1 : Gestion de base des utilisateurs et des groupes

1. **Création d'utilisateurs et de groupes**

* Utilisez `useradd` pour créer un nouvel utilisateur nommé "testuser".

* Utilisez `groupadd` pour créer un groupe nommé "testgroup".

* Assurez-vous que l'utilisateur "testuser" fait partie du groupe "testgroup".

### Exercice 2 : Modifications des utilisateurs

1. **Modification des attributs de l'utilisateur**

* Utilisez `usermod` pour changer le shell par défaut de "testuser" en `/bin/bash`.

* Modifiez le nom de connexion de l'utilisateur de "testuser" à "newuser" en utilisant `usermod`.

* Confirmez les changements en vérifiant `/etc/passwd`.

### Exercice 3 : Modifications des groupes

1. **Modifications des groupes**

* Utilisez `groupmod` pour renommer "testgroup" en "newgroup".

* Changez le GID (Identifiant de groupe) de "newgroup" en utilisant `groupmod`.

* Ajoutez "newuser" au "newgroup" en utilisant `usermod`.

### Exercice 4 : Gestion avancée des utilisateurs et des groupes

1. **Définition des limites des utilisateurs et des groupes**

* Définissez les politiques de mot de passe en utilisant les paramètres dans `/etc/login.defs`.

* Configurez les paramètres par défaut des groupes comme GID_MIN et GID_MAX dans `/etc/login.defs`.

### Exercice 5 : Comprendre `/etc/shadow` et `/etc/skel`

1. **Exploration du stockage des mots de passe et des valeurs par défaut**

* Examinez le fichier `/etc/shadow` pour comprendre le format de stockage des mots de passe.

* Créez un nouvel utilisateur et observez son entrée dans `/etc/shadow`.

* Explorez `/etc/skel` et comprenez son but en créant un nouvel utilisateur et en observant son répertoire personnel.

### Exercice 6 : Défi

1. **Gestion des permissions et du contrôle d'accès**

* Configurez les permissions du répertoire de sorte que seul "newuser" dans "newgroup" puisse lire/écrire dans un dossier spécifique.

* Expérimentez avec les commandes `chown` et `chmod` pour changer le propriétaire et les permissions.

### Exercice 7 : Scénario réel

1. **Création d'utilisateurs avec des configurations spécifiques**

* Créez un utilisateur nommé "admin" avec un répertoire personnel personnalisé (/opt/admin) et un shell par défaut spécifique.

* Définissez une politique de mot de passe qui s'applique uniquement à l'utilisateur "admin".

## **Conclusion**

Merci d'avoir exploré avec moi comment gérer les utilisateurs et les groupes dans RHEL aujourd'hui. Vous pouvez plonger plus profondément dans le domaine de l'expertise Linux et rester à l'écoute pour plus de contenu perspicace dans mes futurs tutoriels.

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)

* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)