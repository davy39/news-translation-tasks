---
title: Red Hat Enterprise Linux – Concepts et commandes essentiels de RHEL à connaître
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-03T15:54:20.000Z'
originalURL: https://freecodecamp.org/news/red-hat-enterprise-linux-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/red-hat-enterprise-linux-guide-cover.jpg
tags:
- name: Linux
  slug: linux
seo_title: Red Hat Enterprise Linux – Concepts et commandes essentiels de RHEL à connaître
seo_desc: 'Welcome to the fundamental world of Red Hat Enterprise Linux (RHEL)! In
  order to be an effective Linux user, you''ll need to learn and truly understand
  some essential concepts and commands.

  Let''s dive into the core aspects of RHEL administration to he...'
---

Bienvenue dans le monde fondamental de Red Hat Enterprise Linux (RHEL)! Pour être un utilisateur Linux efficace, vous devrez apprendre et vraiment comprendre certains concepts et commandes essentiels.

Plongeons dans les aspects principaux de l'administration RHEL pour vous aider à comprendre ces sujets clés qui forment l'épine dorsale des opérations quotidiennes. Les seuls prérequis sont un désir d'apprendre Linux et une volonté de coder chez vous et de compléter les exercices à la fin.

## Table des matières

Voici ce que nous couvrirons dans ce guide complet:

* [Qu'est-ce que RHEL?](#heading-quest-ce-que-rhel)
    
* [Pas besoin d'installer Linux localement](#heading-pas-besoin-dinstaller-linux-localement)
    
* [Comprendre l'amont et l'aval](#heading-comprendre-lamont-et-laval)
    
* [Outils et fonctions essentiels de la ligne de commande RHEL](#heading-outils-et-fonctions-essentiels-de-la-ligne-de-commande-rhel)
    
* [Comment fonctionne le système de fichiers Linux](#heading-comment-fonctionne-le-systeme-de-fichiers-linux)
    
* [Éditeurs de texte](#heading-editeurs-de-texte)
    
* [Exercices pratiques](#heading-exercices-pratiques)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que RHEL?

RHEL est un membre populaire de la famille des distributions Linux. Il se distingue par sa forte fiabilité, sa stabilité et ses capacités de sécurité.

Créé par Red Hat, RHEL est spécifiquement conçu pour un usage en entreprise, offrant un équilibre utile entre les technologies innovantes et un engagement envers la fiabilité, un support étendu et une compatibilité transparente.

RHEL est un choix solide pour les entreprises, les organisations et les développeurs recherchant un système d'exploitation fiable pour des tâches de haute priorité. Il offre une base robuste pour les configurations de serveurs, les centres de données, le cloud computing et les applications d'entreprise, et est souvent une option privilégiée pour les charges de travail critiques.

## Pas besoin d'installer Linux localement

Vous n'avez pas besoin d'installer Linux sur votre système pour suivre ce guide. Au lieu de cela, vous pouvez pratiquer ce que vous apprenez ici sur une plateforme interactive en ligne.

Vous pouvez visiter [ce site web](https://killercoda.com/playgrounds/scenario/ubuntu) pour accéder à un terrain de jeu Linux où vous pouvez exécuter des commandes et explorer Linux sans installation.

## Comprendre l'amont et l'aval

### Amont

L'amont représente le logiciel original ou source à partir duquel sont dérivés les dérivés ou les distributions. Pour Red Hat Enterprise Linux (RHEL), Fedora sert de source principale pour les mises à jour et les fonctionnalités.

RHEL intègre les développements de la plateforme open-source de Fedora dans sa distribution de niveau entreprise. Les changements initiés dans Fedora sont systématiquement intégrés dans RHEL dans le cadre de sa progression amont.

Le logiciel amont comprend généralement les dernières fonctionnalités expérimentales et les développements pilotés par la communauté. Il forme la base pour les projets connexes, fonctionnant comme une zone de test pour essayer de nouvelles fonctions.

### Aval

L'aval fait référence aux distributions ou versions dérivées de la source amont. Ces distributions intègrent généralement des modifications, des ajustements et des fonctionnalités supplémentaires adaptées à des besoins spécifiques.

CentOS, une version largement utilisée qui vient après RHEL, utilise le code de RHEL mais sans sa marque et ses parties exclusives, offrant une alternative sans coût.

De même, des distributions telles qu'Oracle Linux sont également construites à partir de la base de code de RHEL, mais elles apportent leurs propres modifications et ajustements de packaging.

L'aval sert différents groupes d'utilisateurs en prenant les fonctionnalités principales de la source originale et en les ajustant pour répondre à des besoins spécifiques, comme la stabilité, le support ou des utilisations particulières.

## Outils et fonctions essentiels de la ligne de commande RHEL

En apprenant les commandes fondamentales que j'explique ci-dessous, vous pouvez naviguer et gérer votre environnement Linux avec facilité. Ces commandes servent de fondement pour une compréhension plus approfondie des systèmes Linux, et elles vous donneront les moyens d'élargir votre expertise et vos connaissances.

### `echo`

La commande `echo` est utilisée pour afficher du texte ou des variables en tant que sortie. C'est un outil simple mais robuste souvent utilisé dans les scripts et le travail avec les interfaces de ligne de commande.

##### Syntaxe:

```bash
echo [OPTIONS] [STRING]
```

##### Exemples:

Affichage de texte:

```bash
echo "Bonjour, le monde!"
```

Cela imprimera le texte donné tel quel sur l'écran de l'utilisateur.

Affichage de variables:

```bash
name="John"
echo "Bonjour, $name"
```

Nous pouvons directement déclarer une variable et lui assigner une valeur. Nous pouvons utiliser `$` devant le nom de la variable pour l'imprimer en utilisant la commande `echo`.

Séquences d'échappement:

Les séquences d'échappement sont des combinaisons de caractères utilisées pour représenter certains caractères spéciaux ou actions au sein des chaînes. Ces séquences commencent généralement par une barre oblique inverse `\` suivie d'un caractère spécifique ou d'une séquence de caractères.

Lorsque le compilateur ou l'interpréteur rencontre une séquence d'échappement au sein d'une chaîne, il l'interprète comme une instruction spéciale plutôt que comme un caractère littéral.

* `\n`: Représente un caractère de nouvelle ligne. Lorsque cette séquence est rencontrée au sein d'une chaîne, elle signifie un saut de ligne.
    
* `\t`: Représente un caractère de tabulation. Il est utilisé pour créer des tabulations ou espaces horizontaux au sein d'une chaîne.
    
* `\`: Représente un seul caractère de barre oblique inverse. Puisque la barre oblique inverse est un caractère d'échappement en soi, utiliser `\` vous permet d'inclure une barre oblique inverse littérale dans une chaîne.
    
* `\"` : Représente un guillemet double ou un guillemet simple respectivement au sein d'une chaîne. Ceux-ci sont utiles lorsque vous souhaitez inclure des guillemets au sein d'une chaîne qui est elle-même enfermée dans des guillemets.
    

Nous devons utiliser l'option `-e` avec la commande `echo` pour activer les séquences d'échappement. `-e` permet l'interprétation des échappements de barre oblique inverse.

##### Exemples:

Impression d'une nouvelle phrase sur une nouvelle ligne:

```bash
echo -e "Ceci est une nouvelle ligne.\nCeci est une autre ligne."
```

Maintenant, les deux lignes seront sur une ligne séparée plutôt que de continuer l'une après l'autre. Vous pouvez essayer d'utiliser d'autres options ci-dessus.

### `whoami`

whoami est utilisé pour afficher le nom d'utilisateur de l'utilisateur actuel qui est connecté au système.

##### Exemple

```bash
whoami
```

L'exécution de `whoami` dans un terminal affichera le nom d'utilisateur de l'utilisateur actuel. Par exemple, si vous êtes connecté en tant que "Kedar", il affichera `Kedar`. Il sert un but spécifique de montrer l'identité de l'utilisateur actuel et n'a pas d'options ou de variations supplémentaires.

### `cat`

La commande cat est utilisée principalement pour lire, créer, concaténer et afficher le contenu des fichiers. Son nom est dérivé de "concaténer", ce qui signifie lier les choses ensemble.

##### Syntaxe:

```bash
cat [OPTIONS] [FILE(s)]
```

##### Exemples:

Affichage du contenu d'un fichier:

```bash
cat filename.txt
```

Cela affichera le contenu de filename.txt dans le terminal.

Concaténation de plusieurs fichiers:

```bash
cat file1.txt file2.txt > combined.txt
```

Ce code concatène file1.txt et file2.txt et redirige leur contenu vers combined.txt.

Création ou ajout à un fichier:

La sortie de `cat` peut être redirigée en utilisant `>` (créer/écraser) ou `>>` (ajouter) pour stocker le contenu dans un fichier.

Pour créer un nouveau fichier et y ajouter du contenu, essayez cette commande:

```bash
cat > newfile.txt
```

Cela vous permettra de taper du contenu dans le terminal, et appuyer sur Ctrl + D l'enregistrera dans newfile.txt.

Pour ajouter du contenu à un fichier existant, essayez ceci:

```bash
cat >> existingfile.txt
```

Similaire à la commande précédente, cela vous permet d'ajouter du contenu à existingfile.txt.

Afficher les numéros de ligne avec le contenu:

Nous pouvons afficher le numéro de ligne avec le contenu en utilisant l'option `-n` avec cat.

```bash
cat -n filename.txt
```

Afficher un signe dollar ($) à la fin de chaque ligne:

Nous pouvons afficher un `$` à la fin de chaque ligne avec le contenu en utilisant l'option `-E` avec `cat` comme ceci:

```bash
cat -E filename.txt
```

### `touch`

La commande touch est utilisée pour créer de nouveaux fichiers vides ou mettre à jour les horodatages des fichiers existants sans changer leur contenu.

##### Syntaxe:

```bash
touch [OPTIONS] [FILE(s)]
```

##### Exemples:

Création d'un nouveau fichier:

```bash
touch newfile.txt
```

Cette commande crée un nouveau fichier nommé newfile.txt. Si le fichier existe déjà, il met à jour l'horodatage à l'heure actuelle.

Création de plusieurs fichiers:

```bash
touch file1.txt file2.txt file3.txt
```

Cela crée plusieurs fichiers (file1.txt, file2.txt, file3.txt) simultanément.

De plus, nous pouvons créer des fichiers avec des nombres ou des lettres changeants dynamiquement. Nous devons donner la plage de lettres ou de nombres entre accolades:

```bash
touch file{1..3}.txt
```

Cela créera `file1.txt`, `file2.txt` et `file3.txt`.

### `ls`

La commande `ls` est utilisée pour lister les fichiers et les répertoires dans un emplacement spécifié.

##### Syntaxe:

```bash
ls [OPTIONS] [DIRECTORY/PATH_OF_DIRECTORY]
```

##### Exemples:

Lister les fichiers dans le répertoire courant:

```bash
ls
```

Cette commande liste tous les fichiers et répertoires dans le répertoire de travail courant.

Lister les fichiers dans un répertoire spécifique:

```bash
ls /custom/path
```

Remplacez /custom/path par le chemin réel pour lister les fichiers et répertoires dans ce répertoire spécifique.

Lister les fichiers cachés:

```bash
ls -a
ls -a /custom/path
```

L'option `-a` montre tous les fichiers, y compris les fichiers cachés (ceux commençant par un point, par exemple .hiddenfile).

Lister tous les détails du répertoire/fichiers:

```bash
ls -l /custom/path
```

Cela fournit un format de liste détaillé et long qui donne plus d'informations sur les répertoires et les fichiers. Vous en apprendrez plus sur les détails que `ls -l` fournit dans un prochain article.

Afficher la taille du répertoire/fichier:

```bash
ls -h /custom/path
```

Affiche les tailles de fichiers dans un format lisible par l'homme (par exemple, kilo-octets, méga-octets).

Montrer les fichiers modifiés en premier:

```bash
ls -t /custom/path
```

Cette commande trie les fichiers par temps de modification, montrant les fichiers les plus récents en premier.

Nous pouvons également utiliser ces options ensemble comme ceci:

```bash
ls -la /custom/path
```

Cela listera tous les fichiers et répertoires ainsi que les fichiers cachés (-a) et les informations détaillées des fichiers et répertoires (-l).

### `date`

La commande date est utilisée pour afficher ou définir la date et l'heure du système.

##### Syntaxe:

```bash
date [OPTIONS]
```

##### Exemples:

Affichage de la date et de l'heure actuelles:

```bash
date
```

Cela affichera la date et l'heure actuelles de votre système.

Définition de la date et de l'heure:

```bash
date MMDDhhmm[[CC]YY][.ss]
```

* MM: Mois (01-12)
    
* DD: Jour (01-31)
    
* hh: Heure (00-23)
    
* mm: Minute (00-59)
    
* CC: Siècle (optionnel, pour les années antérieures à 2000)
    
* YY: Année (optionnel, 00-99)
    
* .ss: Secondes (optionnel, 00-61)
    

Cette commande vous permettra de définir la date et l'heure que vous souhaitez sur votre système.

Personnalisation de la sortie de la date:

```bash
date +"%A, %B %d, %Y"
```

Options

* %A = Nom complet du jour de la semaine (par exemple, dimanche)
    
* %B = nom complet du mois (par exemple, janvier)
    
* %d = jour du mois (par exemple, 01)
    
* %Y = année
    

Cela affichera `samedi 16 décembre 2023`. Vous pouvez trouver plus d'options pour la date en utilisant la commande `man date`.

**Note**: Si vous souhaitez trouver des informations détaillées sur une commande, utilisez `man votre_commande` pour obtenir plus d'informations.

### `cal`

La commande `cal` est utilisée pour afficher un calendrier pour un mois ou une année spécifié.

##### Syntaxe:

```bash
cal [OPTIONS] [MONTH] [YEAR]
```

##### Exemples:

Affichage du calendrier du mois en cours:

```bash
cal
```

Cette commande affiche le calendrier pour le mois en cours.

Affichage d'un mois et d'une année spécifiques:

```bash
cal 12 2023
```

Cette commande affiche le calendrier pour décembre 2023.

Affichage d'une année spécifique:

```bash
cal 2023
```

Affichage des jours juliens:

"Jours juliens" fait référence à une manière simple de compter les jours. Au lieu d'utiliser des dates comme le 1er janvier ou le 15 février, les jours juliens comptent simplement le nombre de jours écoulés depuis un point de départ spécifique. Ce point de départ est appelé le Numéro de Jour Julien (JDN), qui a commencé le 1er janvier 4713 av. J.-C. dans le calendrier julien.

Par exemple, le 1er janvier 4713 av. J.-C. est le jour julien 0. Chaque jour après est compté comme jour julien 1, 2, 3, et ainsi de suite. C'est comme un compte continu des jours sans se soucier des mois ou des années. C'est une manière pratique pour les scientifiques, les astronomes et d'autres professionnels de suivre le temps car c'est un système direct de comptage des jours.

```bash
cal -j 12 2023
```

Cette commande affiche le calendrier pour décembre 2023 ainsi que les jours juliens correspondants.

### `mkdir`

Vous utilisez cette commande pour créer de nouveaux répertoires, organisant la structure du système de fichiers de manière efficace. `mkdir` signifie `Make Directory`.

##### Syntaxe:

```bash
mkdir [OPTIONS] DIRECTORY_NAME(s)
```

##### Exemples:

Création d'un seul répertoire:

```bash
mkdir new_directory
```

Cette commande crée un nouveau répertoire nommé new_directory dans le répertoire de travail courant.

Création de plusieurs répertoires:

```bash
mkdir dir1 dir2 dir3
```

Cette commande crée plusieurs répertoires nommés dir1, dir2 et dir3 dans le répertoire de travail courant.

Nous pouvons également rendre cette commande un peu plus intéressante. Nous pouvons créer n nombres de répertoires si vous les voulez dans une séquence de nombres (ou de lettres) – comme dir1, dir2, dir3, et ainsi de suite – avec la syntaxe suivante.

```bash
mkdir dir{1..5}
```

Maintenant, cela créera dir1 jusqu'à dir5. Nous pouvons également remplacer les nombres par des lettres.

Création de répertoires imbriqués:

```bash
mkdir -p parent/child/grandchild
```

L'option `-p` crée des répertoires imbriqués. Dans cet exemple, elle crée une structure de répertoires: parent → child → grandchild.

### `pwd`

La commande pwd signifie "print working directory". Elle affiche le chemin du répertoire courant où vous vous trouvez dans le système de fichiers.

##### Exemple:

```bash
pwd
```

### `cd`

La commande cd est utilisée pour changer le répertoire de travail courant. cd signifie `Change Directory`.

##### Syntaxe:

```bash
cd [DIRECTORY_PATH]
```

##### Exemples:

Changement vers un répertoire spécifique:

```bash
cd /path/to/directory
```

Cette commande change le répertoire courant vers le chemin donné – par exemple, /path/to/directory.

Déplacement vers un répertoire parent:

```bash
cd ..
```

`..` fait référence au répertoire parent, donc cette commande monte d'un niveau à partir du répertoire courant.

Retour au répertoire personnel:

```bash
cd
```

Taper `cd` sans aucun argument vous amène à votre répertoire personnel.

Passer au répertoire précédent:

```bash
cd -
```

Cela vous amènera au répertoire précédent sur lequel vous travailliez.

### `cp`

La commande `cp` est utilisée pour copier des fichiers et des répertoires d'un emplacement à un autre.

##### Syntaxe:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

##### Exemples:

Copie d'un fichier vers un autre emplacement:

```bash
cp file.txt /path/to/destination/
```

Cette commande copie file.txt vers le répertoire de destination spécifié (/path/to/destination/).

Copie de plusieurs fichiers vers un répertoire:

```bash
cp file1.txt file2.txt file3.txt /path/to/destination/
```

Cette commande copie plusieurs fichiers (file1.txt, file2.txt, file3.txt) vers le répertoire de destination spécifié.

Copie d'un répertoire et de son contenu:

```bash
cp -r directory1 /path/to/destination/
```

L'option `-r` (ou `-R`) est utilisée pour copier des répertoires de manière récursive. Cette commande copie directory1 et son contenu vers la destination spécifiée.

### `mv`

La commande `mv` est utilisée pour déplacer ou renommer des fichiers et des répertoires d'un emplacement à un autre.

##### Syntaxe:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

##### Exemples:

Déplacement d'un fichier vers un autre emplacement:

```bash
mv file.txt /path/to/destination/
```

Cette commande déplace file.txt vers le répertoire de destination spécifié (/path/to/destination/). Si la destination est un nom de fichier, elle renomme file.txt avec ce nom.

Renommage d'un fichier:

```bash
mv old_name.txt new_name.txt
```

Cette commande renomme old_name.txt en new_name.txt.

Options:

* `-i`: Demande avant d'écraser les fichiers existants.
    
* `-u`: Déplace uniquement lorsque la source est plus récente que le fichier de destination ou lorsque le fichier de destination est manquant.
    

### `nl`

La commande `nl` est utilisée pour ajouter des numéros de ligne aux fichiers ou au texte fourni en entrée. Elle lit le texte d'un fichier ou de l'entrée standard et numérote par défaut toutes les lignes dans la sortie, facilitant ainsi la référence et le travail avec des lignes spécifiques au sein du contenu.

##### Syntaxe:

```bash
nl [OPTIONS] [FILE]
```

##### Exemples:

Numérotation des lignes dans un fichier:

```bash
nl filename
```

Cette commande numérote toutes les lignes dans le fichier spécifié (`filename`) et produit le résultat.

Numérotation uniquement des lignes non vides:

```bash
nl -ba filename
```

Cette commande numérote uniquement les lignes non vides (l'option `-b` spécifie le style de numérotation, où `a` désigne les lignes non vides).

### `head`

La commande `head` affiche la section de début des fichiers ou des flux d'entrée.

##### Syntaxe:

```bash
head [OPTIONS] [FILE(s)]
```

##### Exemple:

Affichage des n premières lignes d'un fichier:

```bash
head -n 10 filename
```

Cette commande affiche les 10 premières lignes du fichier spécifié.

### `tail`

La commande `tail` affiche la section de fin des fichiers ou des flux d'entrée.

##### Syntaxe:

```bash
tail [OPTIONS] [FILE(s)]
```

##### Exemple:

Affichage des n dernières lignes d'un fichier:

```bash
tail -n 10 filename
```

Cette commande affiche les 10 dernières lignes du fichier spécifié.

### `grep`

La commande `grep` dans Linux est un utilitaire puissant utilisé pour rechercher des motifs de texte au sein de fichiers ou de flux d'entrée. Sa fonction principale est de scanner un fichier spécifié ou une entrée standard ligne par ligne et d'imprimer les lignes qui correspondent à un motif spécifié.

##### Syntaxe:

```bash
grep [OPTIONS] PATTERN [FILE(s)]
```

##### Exemples:

Recherche d'un motif spécifique dans un fichier:

```bash
grep "pattern" filename
```

Cette commande recherche le mot "pattern" dans le fichier spécifié (`filename`) et affiche les lignes contenant ce motif.

Recherche insensible à la casse dans un fichier:

```bash
grep -i "pattern" filename
```

Cette commande recherche "pattern" dans le fichier spécifié (`filename`) indépendamment du fait qu'il soit en majuscules ou en minuscules.

Recherche de plusieurs motifs dans un fichier:

```bash
grep -e "pattern1" -e "pattern2" filename
```

Cette commande recherche à la fois "pattern1" et "pattern2" dans le fichier spécifié (`filename`) et affiche les lignes contenant l'un ou l'autre de ces motifs. Vous pouvez également utiliser différents fichiers pour différentes correspondances de motifs.

### `wc`

La commande `wc` signifie "word count", mais sa fonctionnalité va au-delà du comptage des mots. C'est un utilitaire polyvalent en ligne de commande utilisé pour compter le nombre de lignes, de mots et de caractères dans des fichiers ou des flux d'entrée standard.

##### Syntaxe:

```bash
wc [OPTIONS] [FILE(s)]
```

##### Exemples:

Compter les lignes dans un fichier:

```bash
wc -l filename
```

Cette commande affiche le nombre de lignes dans le fichier spécifié (`filename`).

Compter les mots dans un fichier:

```bash
wc -w filename
```

Cela montre le nombre de mots dans le fichier spécifié.

Compter les lignes, les mots et les caractères simultanément:

```bash
wc filename
```

Par défaut, cette commande affiche le nombre de lignes, de mots et de caractères dans le fichier spécifié.

##### Options et indicateurs pour `wc`:

* `-l`: Affiche le nombre de lignes.
    
* `-w`: Affiche le nombre de mots.
    
* `-m`: Affiche le nombre de caractères.
    
* `-c`: Fournit le nombre d'octets (équivalent à `-m` dans la plupart des cas).
    
* `-L`: Affiche la longueur de la ligne la plus longue.
    
* `-h`: Fournit une sortie lisible par l'homme (par exemple, `1.2K` pour 1200).
    

### `cut`

La commande `cut` dans Linux est utilisée pour extraire des sections spécifiques (colonnes ou portions) de texte à partir de fichiers ou de flux d'entrée en fonction de délimiteurs comme des caractères ou des champs.

##### Syntaxe:

```bash
cut [OPTIONS] [FILE(s)]
```

##### Exemples:

Extraction de colonnes spécifiques d'un fichier:

```bash
cut -d',' -f 1,3 filename.txt
```

Cette commande extrait les première et troisième colonnes d'un fichier CSV (`filename.txt`) où les colonnes sont délimitées par une virgule (`-d','` spécifie le délimiteur).

Sélection d'une plage de caractères d'un fichier:

```bash
cut -c 1-5 filename.txt
```

Cette commande extrait les caractères 1 à 5 de chaque ligne du fichier spécifié (`filename.txt`).

Vous pouvez toujours trouver plus d'options pour une commande en utilisant `man votre_commande`. Cela donne la documentation appropriée pour cette commande spécifiée. `man` signifie manuel.

Maintenant que vous avez appris certaines commandes RHEL couramment utilisées, assurez-vous de pratiquer leur utilisation. Vous pouvez commencer par travailler sur l'exercice ci-dessous.

## Comment fonctionne le système de fichiers Linux

Dans Linux, le répertoire racine `/` agit comme le répertoire de niveau supérieur dans la hiérarchie du système. Il contient divers sous-répertoires, chacun servant une fonction spécifique et stockant les fichiers système nécessaires.

Voici un aperçu des principaux répertoires dans RHEL et leurs fonctions au sein du répertoire racine:

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Frame-1000004540.svg align="left")

*Système de fichiers Linux*

Passons en revue la fonction et le but de chacun de ces répertoires.

### `/bin` (Binaire)

* Fonction: contient des binaires exécutables essentiels (commandes) accessibles à tous les utilisateurs.
    
* But: contient des commandes système fondamentales comme `ls`, `cp`, `mv`, `rm`, et ainsi de suite.
    

### `/boot`

* Fonction: contient les fichiers nécessaires pour démarrer le système d'exploitation.
    
* But: contient les fichiers du chargeur de démarrage, les images du noyau et les fichiers de configuration requis lors du démarrage du système.
    

### `/dev` (Périphérique)

* Fonction: représente les fichiers de périphériques.
    
* But: fournit l'accès aux périphériques physiques et virtuels tels que les disques durs, les périphériques USB, les terminaux, et plus encore.
    

### `/etc` (Etcetera)

* Fonction: stocke les fichiers de configuration système.
    
* But: contient les fichiers de configuration pour diverses applications, services et paramètres système.
    

### `/home`

* Fonction: abrite les répertoires personnels des utilisateurs.
    
* But: chaque utilisateur a généralement un sous-répertoire dans `/home` qui contient ses fichiers personnels, ses paramètres et ses données.
    

### `/lib` et `/lib64`

* Fonction: contient les bibliothèques requises par les programmes à l'exécution.
    
* But: stocke les fichiers de bibliothèques partagées utilisés par les binaires système et les applications.
    

### `/mnt` (Montage)

* Fonction: fournit un point de montage pour monter temporairement des périphériques externes.
    
* But: utilisé pour monter des périphériques de stockage externes tels que des clés USB, des partages réseau ou des systèmes de fichiers supplémentaires.
    

### `/opt` (Optionnel)

* Fonction: réservé pour les logiciels optionnels ou tiers.
    
* But: souvent utilisé pour installer de grands packages logiciels autonomes qui ne se conforment pas à la hiérarchie standard du système de fichiers Linux.
    

### `/proc` (Processus)

* Fonction: système de fichiers virtuel fournissant des informations sur les processus système.
    
* But: offre un moyen d'examiner et de manipuler de manière interactive l'état interne du système.
    

### `/root`

* Fonction: répertoire personnel pour le superutilisateur (root).
    
* But: contient les fichiers, les paramètres et les fichiers de configuration de l'utilisateur root.
    

### `/sbin` (Binaire Système)

* Fonction: stocke les binaires essentiels d'administration système.
    
* But: contient des commandes cruciales pour l'administration système, nécessitant souvent des privilèges administratifs.
    

### `/srv` (Service)

* Fonction: destiné aux données liées aux services fournis par le système.
    
* But: utilisé pour stocker les données et les fichiers utilisés par divers services exécutés sur le système.
    

### `/tmp` (Temporaire)

* Fonction: répertoire pour les fichiers temporaires.
    
* But: contient les fichiers temporaires créés par divers processus système et utilisateurs. Les fichiers ici sont généralement supprimés au redémarrage du système.
    

### `/usr` (Ressources du Système Unix)

* Fonction: contient les programmes, bibliothèques et documentations liés à l'utilisateur.
    
* But: contient une grande majorité d'applications accessibles à l'utilisateur, d'utilitaires système, de bibliothèques et de documentations.
    

### `/var` (Variable)

* Fonction: stocke les données variables telles que les journaux, les fichiers spool et les fichiers temporaires.
    
* But: contient des données qui varient fréquemment, y compris les journaux système, les mails, les files d'impression, et plus encore.
    

## Éditeurs de texte

Il existe divers éditeurs de texte basés sur le terminal, chacun avec ses propres forces et fonctionnalités. Mais Vim se distingue parmi ces éditeurs grâce à sa polyvalence inégalée et à son ensemble de fonctionnalités robustes.

La force de Vim réside dans son édition modale puissante, offrant des modes distincts pour la navigation, l'insertion et l'exécution de commandes, permettant une manipulation rapide et efficace du texte.

De plus, la coloration syntaxique de Vim, le support de plusieurs langages de programmation et ses puissantes capacités de recherche et de remplacement en font un choix privilégié pour les programmeurs et les administrateurs système.

### vim

Vim est un éditeur de texte populaire parmi les utilisateurs Linux, en particulier dans l'interface de ligne de commande. Vim signifie "Vi IMproved" et est une version améliorée de l'éditeur classique `vi`. Il offre des fonctionnalités étendues pour l'édition, la visualisation et la manipulation de fichiers texte ou de code.

Dans cette section, nous allons plonger dans le monde de Vim et comment l'utiliser dans Linux. Mon objectif est de vous familiariser avec certaines commandes et fonctionnalités pratiques dans Vim pour vous aider à manipuler facilement le texte.

Voici comment ouvrir Vim dans Linux:

```bash
vim [OPTIONS] [FILE(s)]
```

### Modes dans Vim:

Dans Vim, les modes agissent comme différents états opérationnels qui dictent comment vous pouvez interagir avec l'éditeur. Les modes clés – Normal, Insertion et Visuel – jouent un rôle significatif dans votre processus d'édition.

Vous commencerez en mode Normal lorsque vous ouvrirez Vim. À partir de là, vous pouvez facilement naviguer, déplacer le curseur et exécuter des commandes. Le passage en mode Insertion vous donne un moyen direct de saisir et de modifier du texte. Et le mode Visuel vous permet de sélectionner et de manipuler des blocs de texte.

Ces modes sont cruciaux pour rationaliser diverses tâches d'édition et peuvent vous aider à devenir plus efficace et précis. Apprendre à utiliser et à passer entre ces modes vous donne un contrôle polyvalent sur l'édition de texte et vous rend beaucoup plus productif dans l'environnement Vim.

* **Mode Normal**: Mode par défaut pour la navigation et l'exécution de commandes.
    
* **Mode Insertion**: Pour taper et éditer du texte.
    
* **Mode Visuel**: Pour sélectionner et manipuler des blocs de texte.
    

### Édition en mode Insertion:

Imaginez-vous ouvrir un document dans Vim, impatient d'insérer de nouvelles informations. Appuyez simplement sur la touche `i`, et Vim saura que vous êtes prêt à taper à la position actuelle du curseur.

Une notification en bas vous alertera avec -- INSERT -- signifiant que vous êtes officiellement en mode insertion. Maintenant, vous pouvez saisir vos ajouts souhaités. Lorsque vous avez terminé, appuyez sur la touche 'Esc' pour revenir au mode par défaut où vous pouvez ensuite naviguer et exécuter des commandes.

* Appuyez sur `i` pour entrer en mode insertion et commencer à taper.
    
* Appuyez sur `Esc` pour quitter le mode insertion et revenir au mode commande.
    

### Sauvegarde et sortie de Vim:

Imaginez que vous avez apporté des modifications à votre document et que vous êtes maintenant prêt à les sauvegarder avant de quitter Vim. Tapez simplement `:wq` (qui représente "write and quit") et appuyez sur 'Entrée' pour sauvegarder vos modifications et quitter Vim en toute sécurité.

Mais que faire si vous avez apporté des modifications que vous ne souhaitez pas conserver? Dans cette situation, entrez `:q!` et appuyez sur 'Entrée' pour instruire Vim de quitter sans sauvegarder les modifications apportées depuis votre dernière sauvegarde.

En tapant `:wq` et `:q!`, selon vos besoins, vous pouvez ajouter du contenu à votre document et vous assurer que votre travail est soit sauvegardé en toute sécurité, soit jeté. Ces actions, associées à votre capacité à naviguer dans les différents modes de Vim, permettent une expérience d'édition fluide et efficace.

* Pour sauvegarder les modifications et quitter, tapez `:wq` (write and quit) et appuyez sur Entrée.
    
* Pour quitter sans sauvegarder les modifications, tapez `:q!` et appuyez sur Entrée.
    

### Comment éditer les commandes

Avant d'entrer une commande, appuyez sur `esc` pour sortir de tout mode dans lequel vous vous trouviez.

Dans l'éditeur, les commandes précédées d'un deux-points (par exemple, `:w`) sont utilisées pour effectuer diverses actions, telles que la sauvegarde de fichiers. Pour sauvegarder les modifications que vous avez apportées, tapez simplement `:w` et appuyez sur la touche 'Entrée'.

De même, des commandes comme `dd` sont conçues pour des tâches telles que l'effacement d'une ligne. Pour supprimer une ligne, assurez-vous d'être dans le mode approprié (mode Normal), puis tapez `dd` en appuyant deux fois rapidement sur la touche 'd'. Si vous vous trouvez dans un autre mode, appuyez simplement sur la touche 'esc' pour revenir au mode Normal.

#### Exemple de mode Insertion:

* `i`: Entrer en mode insertion avant le curseur.
    

```bash
vim example.txt
```

* Utilisez les touches fléchées ou 'h', 'j', 'k', 'l' pour naviguer à la fin de la première ligne.
    
* Appuyez sur 'i' pour entrer en mode insertion.
    
* Tapez votre nouvelle phrase.
    
* Appuyez sur 'Esc' pour quitter le mode insertion.
    

#### Suppression et modification de texte:

* `dw`: Supprimer du curseur à la fin du mot.
    
* `dd`: Supprimer la ligne entière.
    

```bash
vim example.txt
```

* Déplacez le curseur vers la ligne que vous souhaitez supprimer.
    
* Appuyez sur `dd`.
    

#### Copier, couper et coller:

* `yy`: Copier (yank) la ligne actuelle.
    
* `yw`: Copier du curseur à la fin du mot.
    
* `p`: Coller après le curseur.
    
* `P`: Coller avant le curseur.
    

```bash
vim example.txt
```

* Pour copier une ligne: Déplacez le curseur vers la ligne que vous souhaitez copier et appuyez sur `yy`.
    
* Pour couper (supprimer) une ligne: Déplacez le curseur vers la ligne que vous souhaitez couper et appuyez sur `dd`.
    
* Pour coller la ligne copiée ou coupée: Déplacez le curseur vers l'emplacement souhaité et appuyez sur `p` pour coller après le curseur ou `P` pour coller avant le curseur.
    

#### Recherche:

* `/pattern`: Rechercher "pattern" vers l'avant.
    
* `?pattern`: Rechercher "pattern" vers l'arrière.
    
* `n`: Aller au résultat de recherche suivant.
    
* `N`: Aller au résultat de recherche précédent.
    

```c
vim example.txt
```

* Pour rechercher un mot comme "example": Appuyez sur `/` puis tapez `example` suivi de `Entrée`.
    
* Pour aller à l'occurrence suivante: Appuyez sur `n`.
    
* Pour aller à l'occurrence précédente: Appuyez sur `N`.
    

#### Remplacement:

* `:%s/old/new/g`: Remplacer "old" par "new" globalement dans tout le fichier.
    
* `:s/old/new/g`: Remplacer "old" par "new" sur la ligne actuelle.
    
* `:s/old/new/gc`: Remplacer "old" par "new" avec confirmation.
    

```bash
vim example.txt
```

* Pour remplacer toutes les occurrences de "oldword" par "newword": Tapez `:%s/oldword/newword/g` et appuyez sur `Entrée`.
    

#### Sauvegarde:

* `:w`: Sauvegarder les modifications.
    
* `:wq` ou `ZZ`: Sauvegarder les modifications et quitter.
    
* `:x`: Sauvegarder les modifications et quitter (identique à `:wq`).
    

```bash
vim example.txt
```

* Pour sauvegarder les modifications apportées au fichier: Tapez `:w` et appuyez sur `Entrée`.
    

#### Quitter:

* `:q`: Quitter (uniquement s'il n'y a pas de modifications non sauvegardées).
    
* `:q!`: Quitter sans sauvegarder les modifications.
    

```bash
vim example.txt
```

* Pour quitter sans sauvegarder les modifications: Tapez `:q!` et appuyez sur `Entrée`.
    
* Pour sauvegarder les modifications et quitter: Tapez `:wq` ou `ZZ` et appuyez sur `Entrée`.
    

### Exercices pratiques

Maintenant, pour vous aider à pratiquer ce que vous avez appris, voici quelques exercices pour vous.

Disons que vous avez été chargé d'organiser et de manipuler des fichiers et des répertoires sur un système Red Hat Enterprise Linux nouvellement provisionné. Utilisez le terminal pour effectuer les tâches suivantes:

#### Outils et fonctions essentiels de la ligne de commande:

* Utilisez `echo` pour afficher votre nom et un message de salutation en utilisant des variables et des séquences d'échappement.
    
* Utilisez `whoami` pour imprimer le nom de l'utilisateur actuel.
    
* Créez un fichier nommé `example.txt` et affichez son contenu en utilisant `cat`.
    
* Utilisez `touch` pour créer trois fichiers: `file1.txt`, `file2.txt`, et `file3.txt`.
    
* Expérimentez avec les variations de la commande `ls`: `-a`, `-l`, `-h`, `-t`, et des combinaisons.
    
* Utilisez `date` pour afficher la date actuelle puis personnalisez la sortie dans un format spécifique.
    

#### Exploration du système de fichiers Linux:

* Utilisez `mkdir` pour créer des répertoires: `/bin`, `/boot`, `/home`, `/etc`, etc., et expliquez leurs fonctionnalités dans un document.
    
* Naviguez vers `/var` et listez son contenu.
    
* Utilisez `pwd` pour imprimer le chemin du répertoire courant.
    

#### Édition de texte avec Vim:

* Créez un fichier `sample.txt`.
    
* Ouvrez `sample.txt` en utilisant `vim`.
    
* Pratiquez l'insertion de texte, la suppression de lignes, la copie et le collage, et la sauvegarde des modifications.
    

#### Opérations sur les fichiers:

* Copiez `sample.txt` vers un répertoire nouvellement créé `/tmp` en utilisant `cp`.
    
* Déplacez `sample.txt` vers le répertoire `/var` en utilisant `mv`.
    
* Supprimez `sample.txt` du répertoire courant en utilisant `rm`.
    

#### Inspection des informations du système de fichiers:

* Utilisez `ls -l` pour voir les informations détaillées d'un fichier dans `/usr/bin`.
    
* Expliquez la sortie et les permissions de fichier dans un document.
    

#### Recherches de base et manipulation de texte:

* Utilisez `grep` pour rechercher un mot spécifique dans un fichier.
    
* Effectuez une opération de recherche et de remplacement dans `example.txt` en utilisant `sed`.
    

#### Gestion avancée des fichiers:

* Créez des répertoires imbriqués `/opt/program/scripts` en utilisant `mkdir -p`.
    
* Déplacez `file1.txt` et `file2.txt` dans le répertoire `/opt/program`.
    

#### Réflexion et documentation:

* Réfléchissez à votre expérience avec chaque commande dans un document, en expliquant son utilisation et ses résultats.
    
* Documentez les défis rencontrés et leurs solutions.
    
* Résumez l'importance de chaque concept et commande appris.
    

Rappelez-vous, lors de la réalisation de ces exercices, assurez-vous d'être dans le bon répertoire et vérifiez deux fois les commandes impliquant la suppression ou la modification de fichiers pour éviter des actions non intentionnelles.

#### Questions de révision:

1. Quelle commande crée un nouveau répertoire? Exécutez-la.
    
2. Comment créez-vous plusieurs fichiers à la fois? Démontrez cela.
    
3. Quelle commande déplace les fichiers d'un emplacement à un autre? Déplacez `file1.txt` et `file3.txt` vers `folderA`.
    
4. Comment pouvez-vous afficher la date et l'heure actuelles? Montrez la sortie.
    
5. Quelle commande liste le contenu d'un répertoire en détail? Utilisez-la pour le répertoire `RHCSA_Practice`.
    
6. Expliquez le but de la création de répertoires imbriqués.
    
7. Quelle commande renomme un fichier? Renommez `file2.txt` en `important_file.txt`.
    
8. Comment pouvez-vous afficher uniquement les fichiers cachés dans un répertoire? Montrez les fichiers cachés dans votre répertoire courant.
    

## Conclusion

Merci d'avoir exploré le monde de l'administration Red Hat Enterprise Linux (RHEL) avec moi aujourd'hui. Vous pouvez plonger plus profondément dans le domaine de l'expertise Linux et rester à l'écoute pour plus de contenu perspicace dans mes futurs tutoriels.

Vous pouvez me suivre sur:

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)