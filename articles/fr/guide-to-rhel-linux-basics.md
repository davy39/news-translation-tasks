---
title: 'Prise en main de RHEL : Un guide pour débutants sur les bases de Linux'
subtitle: ''
author: Tanishka Makode
co_authors: []
series: null
date: '2025-01-10T15:42:49.433Z'
originalURL: https://freecodecamp.org/news/guide-to-rhel-linux-basics
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738685031729/c2dbcf09-c903-4eeb-b97a-0deb3a50385b.png
tags:
- name: Linux
  slug: linux
seo_title: 'Prise en main de RHEL : Un guide pour débutants sur les bases de Linux'
seo_desc: Imagine an operating system so reliable that it powers the world’s biggest
  servers, the fastest supercomputers, and even the cloud infrastructure of leading
  tech companies. Welcome to Red Hat Enterprise Linux (RHEL) — the backbone of modern
  IT system...
---

Imaginez un système d'exploitation si fiable qu'il alimente les plus grands serveurs du monde, les supercalculateurs les plus rapides et même l'infrastructure cloud des principales entreprises technologiques. Bienvenue dans Red Hat Enterprise Linux (RHEL) — l'épine dorsale des systèmes informatiques modernes.

Que vous soyez un novice complet explorant Linux pour la première fois ou un professionnel expérimenté cherchant à rafraîchir vos bases, vous êtes au bon endroit. Ce tutoriel est votre point de départ pour découvrir la puissance, la stabilité et la polyvalence de RHEL.

Mais qu'est-ce qui distingue RHEL dans l'écosystème Linux encombré ? Pourquoi des entreprises comme Google, Amazon et la NASA s'appuient-elles sur lui ? Plongeons et explorons tout ce que vous devez savoir pour commencer votre voyage avec Red Hat Enterprise Linux.

### Ce que nous allons couvrir :

1. [Un peu d'histoire](#heading-un-peu-dhistoire)

2. [Qu'est-ce qui rend Linux spécial ?](#heading-quest-ce-qui-rend-linux-special)

3. [Pourquoi Red Hat Enterprise Linux ?](#heading-pourquoi-red-hat-enterprise-linux)

4. [Comment configurer votre environnement de pratique pour les commandes Linux](#heading-comment-installer-votre-environnement-de-pratique-pour-les-commandes-linux)

5. [Introduction aux commandes Linux de base](#heading-introduction-aux-commandes-linux-de-base)

## Un peu d'histoire

Vous êtes-vous déjà demandé où tout a commencé ? Avant Linux, il y avait **UNIX**, un système d'exploitation révolutionnaire créé dans les années 1970 qui a changé la façon dont les ordinateurs fonctionnaient. Conçu pour la stabilité, le multitâche et la scalabilité, UNIX est devenu la fondation sur laquelle les systèmes d'exploitation modernes ont été construits.

Avance rapide jusqu'en 1991, lorsqu'un étudiant finlandais en informatique de 21 ans nommé Linus Torvalds à l'Université d'Helsinki a décidé de créer son propre noyau de système d'exploitation comme projet de loisir. Peu savait-il que ce passe-temps évoluerait en Linux, un système d'exploitation open-source révolutionnaire qui redéfinirait le monde de la technologie.

Maintenant, voici la partie amusante : comment Linux a-t-il obtenu son nom ? À l'origine, Linus voulait l'appeler « Freax » (une combinaison de « free », « freak » et « Unix »). Mais lorsqu'il a téléchargé les fichiers du projet sur un serveur géré par son ami Ari Lemmke, Ari a pensé que « Freax » ne sonnait pas assez bien. Ainsi, sans en informer Linus, Ari a nommé le répertoire « Linux » à la place — un mélange astucieux de **Linus + Unix**. Et le reste, comme on dit, est de l'histoire.

## Qu'est-ce qui rend Linux spécial ?

Contrairement aux systèmes d'exploitation traditionnels, Linux était open-source, ce qui signifie que n'importe qui pouvait consulter, modifier et distribuer le code librement. Cela a déclenché une vague d'innovation, permettant aux développeurs du monde entier de créer leurs propres versions de Linux, adaptées à différents besoins.

Ce qui distingue vraiment Linux, c'est la communauté mondiale de développeurs et d'enthousiastes qui améliorent et innovent constamment. Cette approche collaborative garantit que Linux reste à la pointe de la technologie, évoluant avec les besoins de ses utilisateurs.

Aujourd'hui, Linux n'est pas seulement un système d'exploitation — c'est toute une famille de distributions (ou distros). Des versions conviviales comme Ubuntu et Fedora aux solutions de niveau entreprise comme RHEL, il y a un Linux pour tout le monde. Dans cet article, nous nous concentrerons sur RHEL et pourquoi c'est un excellent choix pour certains projets.

Si vous souhaitez explorer la variété fascinante des distributions Linux, vous pouvez consulter cette [page Wikipedia sur les distributions Linux](https://en.wikipedia.org/wiki/Linux_distribution) pour voir à quel point l'écosystème Linux est diversifié.

### Pourquoi Red Hat Enterprise Linux ?

Red Hat Enterprise Linux (RHEL) est comme l'ami fiable et sans détour que vous appelez lorsque vous organisez un grand événement important.

Bien sûr, vous pourriez demander à vos amis amusants mais imprévisibles (comme les distributions Linux open-source) de vous aider, mais il y a toujours une chance qu'ils oublient les chaises ou plantent en plein milieu de la fête.

RHEL, en revanche, est conçu pour la stabilité et est livré avec une équipe de support professionnelle disponible 24h/24 et 7j/7 pour résoudre tout problème qui pourrait survenir. Il est rigoureusement testé pour garantir qu'il fonctionne parfaitement avec tous les outils et gadgets utilisés par les grandes entreprises, afin qu'il n'y ait pas de surprises.

Le mélange de fiabilité, de sécurité, de performance et de support de RHEL en fait le système d'exploitation de choix pour les entreprises, consolidant son importance dans le paysage informatique.

Voici un résumé des avantages et fonctionnalités de RHEL :

#### **1. Stabilité et fiabilité de niveau entreprise**

RHEL est conçu pour répondre aux exigences des charges de travail critiques, garantissant que les systèmes fonctionnent de manière cohérente et prévisible. Son support de cycle de vie long permet aux entreprises de s'appuyer sur lui sans s'inquiéter des mises à jour fréquentes ou des problèmes de compatibilité. Cela en fait un choix idéal pour les applications où les temps d'arrêt sont inacceptables.

#### **2. Fonctionnalités de sécurité complètes**

La sécurité est primordiale dans les environnements d'entreprise, et RHEL excelle avec des fonctionnalités robustes telles que SELinux (Security-Enhanced Linux) et des mises à jour de sécurité régulières. L'approche proactive pour identifier et résoudre les vulnérabilités aide les organisations à se conformer aux réglementations de l'industrie et à maintenir l'intégrité de leurs systèmes.

#### **3. Optimisation de la scalabilité et des performances**

RHEL est optimisé pour offrir des performances élevées pour une large gamme d'architectures matérielles et de charges de travail, y compris les configurations cloud, sur site et hybrides. Sa capacité à évoluer efficacement le rend adapté aux applications à petite échelle ainsi qu'aux grands centres de données et charges de travail de niveau entreprise.

#### **4. Écosystème étendu et support professionnel**

RHEL bénéficie de l'écosystème étendu de Red Hat de matériel, logiciels et fournisseurs cloud certifiés. Les entreprises ont accès à une multitude de solutions testées et certifiées, ainsi qu'à un support 24h/24 de Red Hat. Cela garantit que tout problème technique est résolu rapidement, minimisant les temps d'arrêt et améliorant la productivité.

## Comment installer votre environnement de pratique pour les commandes Linux

Avant de nous lancer dans l'apprentissage et la pratique des commandes Linux, vous devrez configurer un environnement où vous pourrez exécuter ces commandes. Voici trois excellentes options à considérer :

### 1. **Utilisation du terminal sur votre machine Linux**

Si vous utilisez déjà Linux, le terminal est votre interface de prédilection pour interagir avec le système. Toutes les commandes Linux sont exécutées ici, et c'est l'environnement idéal pour commencer à pratiquer.

Vous pouvez ouvrir le terminal et taper directement vos commandes pour les voir en action.

### 2. Utilisation de **VMware ou Oracle VirtualBox**

Si vous ne souhaitez pas installer Linux directement sur votre machine principale, l'utilisation d'une machine virtuelle (VM) est une excellente solution. Les outils de virtualisation comme VMware ou Oracle VirtualBox vous permettent d'exécuter une distribution Linux complète en tant que système d'exploitation invité sans affecter votre système principal. Ainsi, vous pouvez expérimenter librement dans un environnement isolé.

**Comment utiliser une VM :**

* Installez [VMware Workstation Player](https://blogs.vmware.com/workstation/2024/05/vmware-workstation-pro-now-available-free-for-personal-use.html) ou [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads?) sur votre ordinateur.

* Téléchargez l'image ISO de RHEL. Vous pouvez obtenir l'ISO de RHEL en suivant ces étapes :

  1. Inscrivez-vous pour un compte développeur Red Hat (c'est gratuit) :

     * Allez sur le programme développeur Red Hat.

     * Créez un compte (c'est gratuit pour les développeurs individuels).

     * Après vous être inscrit, connectez-vous à votre compte Red Hat.

  2. Téléchargez l'ISO :

     * Visitez la page de téléchargement de RHEL après vous être connecté.

     * Choisissez l'image ISO pour RHEL (vous pouvez sélectionner la dernière version).

     * Cliquez sur Télécharger et enregistrez le fichier ISO sur votre système local.

Une fois votre VM en cours d'exécution, vous pouvez l'utiliser pour pratiquer les commandes et explorer Linux.

### 3. **KillerCoda : Un environnement Linux en ligne**

Si vous cherchez une solution entièrement en ligne, KillerCoda est une option fantastique. Il fournit un terminal Linux interactif directement dans votre navigateur, vous n'avez donc pas besoin d'installer quoi que ce soit sur votre machine locale.

Visitez le site [KillerCoda](https://killercoda.com/pawelpiwosz/course/linuxFundamentals) et vous verrez des leçons basées sur des scénarios.

Vous devriez maintenant être prêt.

## Introduction aux commandes Linux de base

L'une des caractéristiques clés qui rend Linux si polyvalent est son interface en ligne de commande (CLI). C'est ici que vous pouvez interagir avec le système en tapant des commandes. Ces commandes vous permettent d'effectuer une variété de tâches comme la gestion de fichiers, de répertoires, de ressources système, et bien plus encore.

Maintenant, nous allons explorer quelques commandes Linux essentielles que tout débutant devrait connaître. Ces commandes sont des outils simples mais puissants qui peuvent vous aider à naviguer et à gérer votre environnement Linux efficacement.

### Commandes Linux de base

**1.** `echo`

La commande `echo` est utilisée pour afficher du texte ou des variables dans le terminal. C'est l'une des commandes les plus couramment utilisées dans Linux et elle est utile pour afficher des messages, des valeurs de variables, et même des informations système.

Syntaxe de `echo` :

```bash
echo [OPTION] [CHAINE]
```

Exemple :

```bash
echo Bonjour # Affiche 'Bonjour' sur le terminal
echo -n Hey # N'affiche pas de saut de ligne à la fin

nom="Tanishka"
echo "Bonjour, $nom" # Affiche les variables
```

L'option `-e` permet aux commandes echo d'activer les séquences d'échappement.

Voici quelques autres options que vous pouvez utiliser avec `echo` :

1. `\n` – Nouvelle ligne : Passe l'affichage à la ligne suivante.

2. `\t` – Tabulation : Ajoute un espace de tabulation.

3. `\v` – Tabulation verticale : Ajoute une tabulation lorsque le curseur se déplace vers la position verticale suivante.

4. `\b` – Retour arrière : Supprime le dernier caractère.

5. `\\` – Barre oblique inverse : Affiche une barre oblique inverse.

Exemple :

```bash
echo -e "Bonjour le monde\nCeci est une nouvelle ligne."
# Bonjour le monde
# Ceci est une nouvelle ligne.

echo -e "Bonjour le monde\tCeci est tabulé."
# Bonjour le monde    Ceci est tabulé.

echo -e "Bonjour\vMonde\vCeci est espacé verticalement."
# Bonjour
#       Monde
#             Ceci est espacé verticalement.

echo -e "Ceci est une barre oblique inverse : \\"
# Ceci est une barre oblique inverse : \
```

**2. whoami**

La commande `whoami` est utilisée pour afficher le nom d'utilisateur de l'utilisateur actuellement connecté.

Syntaxe de `whoami` :

```bash
whoami
```

Exemple :

```bash
whoami #tanishkamakode
```

**3.** `pwd`

La commande `pwd` est utilisée pour afficher le répertoire de travail actuel.

Syntaxe de `pwd` :

```bash
pwd [OPTION]
```

Exemple :

```bash
pwd # /home/tanishkamakode
pwd -L # Affiche le répertoire de travail actuel logique, c'est-à-dire montre les liens symboliques (chemin raccourci, s'il existe)
pwd -P # Affiche le répertoire de travail actuel physique, c'est-à-dire montre le chemin résolu (chemin original du raccourci, s'il existe)
```

**4.** `ls`

La commande `ls` est utilisée pour lister les fichiers et répertoires dans le répertoire de travail actuel ou le répertoire spécifié.

Syntaxe de `ls` :

```bash
ls [OPTION] [CHEMIN]
```

Exemple :

```bash
ls # Liste les fichiers et répertoires dans le répertoire de travail actuel
```

Voici quelques options que vous pouvez utiliser avec `ls` :

* `ls -l` : Liste des informations détaillées sur les fichiers et répertoires

* `ls -lh` : Liste des informations détaillées sur les fichiers et répertoires avec la taille dans un format lisible par l'homme

* `ls -a` : Liste tous les fichiers cachés

* `ls -R` : Liste le contenu récursif du répertoire

**5.** `date`

La commande `date` est utilisée pour afficher ou définir la date et l'heure du système.

Syntaxe de `date` :

```bash
date [OPTION] [SPECIFICATEUR_DE_FORMAT]
```

Exemple :

```bash
date # Affiche la date et l'heure actuelles
date +"%d/%m/%Y" # Affiche le jour, le mois et l'année
date +"%H:%M:%S" # Affiche les heures, minutes et secondes
date -u # Affiche la date en temps UTC
date --set "2024-06-05" # Définit la date au format AAAA-MM-JJ donné
date -d "yesterday" # Affiche la date d'hier
date -d "tomorrow" # Affiche la date de demain
date -d "7 days" # Affiche la date dans 7 jours à partir d'aujourd'hui
```

Options que vous pouvez utiliser avec la commande date :

1. `-u` : Affiche la date et l'heure en UTC.

2. `-d` : Affiche ou définit la date/heure selon une chaîne spécifique (par exemple, "yesterday", "7 days ago").

3. `%d` : Jour du mois (01 à 31).

4. `%m` : Mois de l'année (01 à 12).

5. `%y` : Les deux derniers chiffres de l'année (00 à 99).

6. `%Y` : Année complète (par exemple, 2025).

```bash
date -u # Affiche la date en temps UTC
date -d "yesterday" # Affiche la date d'hier
date -d "tomorrow" # Affiche la date de demain
date -d "7 days" # Affiche la date dans 7 jours à partir d'aujourd'hui
date +"%d/%m/%Y" # Affiche le jour, le mois et l'année
date +"%H:%M:%S" # Affiche les heures, minutes et secondes
```

**6.** `cal`

La commande `cal` est utilisée pour afficher les détails du calendrier. Si aucune option n'est donnée, le mois en cours est affiché.

Syntaxe de `cal` :

```bash
cal [OPTIONS]
```

Exemple :

```bash
cal # Affiche le calendrier du mois en cours
cal --highlight # Met en évidence la date actuelle
```

Options que vous pouvez utiliser avec la commande `cal` :

1. `--highlight` : Met en évidence la date actuelle dans le calendrier.

2. `-3` : Affiche le mois précédent, le mois en cours et le mois suivant.

3. `-m` : Affiche le mois en cours dans un format multi-lignes.

4. `-y` : Affiche le calendrier pour toute l'année.

5. `-A [N]` : Affiche N mois après le mois en cours.

6. `-B [N]` : Affiche N mois avant le mois en cours.

7. `cal [année]` : Affiche le calendrier pour toute l'année.

8. `cal [mois] [année]` : Affiche le calendrier pour le mois et l'année spécifiés.

```bash
cal 2024 # Affiche le calendrier pour tous les mois de 2024
cal 06 2024 # Affiche le calendrier pour le 6ème mois (juin) de 2024
cal -m # Affiche le mois en cours dans un format multi-lignes
cal -A 3 # Affiche les 3 mois après le mois en cours
cal -B 2 # Affiche les 2 mois avant le mois en cours
```

**7.** `nl`

La commande `nl` est utilisée pour ajouter des numéros de ligne au contenu d'un fichier.

Syntaxe de `nl` :

```bash
nl [OPTIONS] [NOM_DE_FICHIER]
```

Exemple :

```bash
nl fichier.txt # Affiche le contenu du fichier avec des numéros de ligne
nl -b a fichier.txt # Numérote toutes les lignes
nl -b t fichier.txt # Numérote uniquement les lignes non vides
nl -s ') ' fichier.txt # Ajoute un séparateur entre le numéro de ligne et le contenu
# 1) Première ligne
# 2) Deuxième ligne
```

Comme vous pouvez le voir dans le code ci-dessus, il existe d'autres options que vous pouvez utiliser avec la commande `nl`.

### Commandes de création et de gestion de fichiers

**1.** `touch`

La commande `touch` est utilisée pour créer un fichier vide ou mettre à jour l'heure de la dernière modification si un fichier existe.

Syntaxe de `touch` :

```bash
touch [OPTIONS] [NOM_DE_FICHIER]
```

Exemple :

```bash
touch fichier.txt # Crée un seul fichier - fichier.txt
touch fichier1.txt fichier2.txt fichier3.txt # Crée plusieurs fichiers
touch fichier{1..10}.txt # Crée des fichiers avec les noms de plage donnés (fichier1.txt fichier2.txt jusqu'à fichier10.txt)
```

**2.** `cat`

La commande `cat` concatène les fichiers et affiche également le contenu des fichiers.

Syntaxe de `cat` :

```bash
cat [OPTIONS] [NOM_DE_FICHIER]
```

Exemple :

```bash
cat fichier.txt # Affiche le contenu de fichier.txt
cat fichier1.txt fichier2.txt > fusionne.txt # Remplace le contenu de deux fichiers dans fusionne.txt
cat fichier1.txt >> fichier2.txt # Ajoute le contenu du premier fichier au deuxième fichier
cat -n fichier.txt # Affiche le contenu avec les numéros de ligne

cat > fichier.txt OU cat >> fichier.txt # > pour remplacer, >> pour ajouter
# Cela vous permet de créer un nouveau fichier avec une invite pour entrer le contenu
# Si le fichier existe déjà, le terminal lira le contenu que vous entrez.
# Une fois que vous avez terminé d'écrire le contenu,
# appuyez sur Ctrl + D (détacher).
# Ou Ctrl + C mais assurez-vous de l'entrer sur une nouvelle ligne
# sinon le contenu de la ligne actuelle ne sera pas ajouté au fichier.
```

### Création et gestion de répertoires

**1.** `mkdir`

La commande `mkdir` est utilisée pour créer un répertoire.

Syntaxe de `mkdir` :

```bash
mkdir [OPTIONS] [NOM_DE_REPERTOIRE]
```

Exemple :

```bash
mkdir dossier # Crée un seul répertoire
mkdir fol1 fol2 fol3 # Crée plusieurs répertoires
mkdir fol{1..10} # Crée des répertoires avec les noms de plage donnés
mkdir -p /mesDonnees/donnees # Crée des répertoires imbriqués
ls -R /mesDonnees # Vérifie si les répertoires imbriqués ont été créés
mkdir -v fol1 fol2 fol3 # Mode verbeux, c'est-à-dire confirmation de la création du répertoire sur le terminal
```

**2.** `cd`

La commande `cd` est utilisée pour changer de répertoire — c'est-à-dire pour naviguer entre les répertoires.

Syntaxe de `cd` :

```bash
cd [REPERTOIRE]
```

Exemple :

```bash
cd monDossier # Chemin relatif, commençant depuis le répertoire actuel
cd /home/monDossier # Chemin absolu, commençant depuis la racine /
cd .. # Remonte d'un niveau par rapport au répertoire actuel
cd ../.. # Remonte de deux niveaux par rapport au répertoire actuel
cd OU cd ~ # Va au répertoire personnel
cd - # Passe au répertoire dans lequel vous étiez précédemment
```

### Copier, déplacer et supprimer des fichiers et répertoires

**1.** `cp`

La commande `cp` est utilisée pour copier des fichiers et des répertoires d'un emplacement à un autre.

Syntaxe de `cp` :

```bash
cp [OPTIONS] [SOURCE] [DESTINATION]
```

Exemple :

```bash
cp monFichier.txt /home/nouveauDossier # Copie monFichier.txt dans nouveauDossier
cp monFichier1.txt monFichier2.txt /home/nouveauDossier # Copie plusieurs fichiers dans nouveauDossier
cp -r anciennesDonnees /home/nouvellesDonnees # Copie récursivement le contenu du répertoire anciennesDonnees dans le répertoire nouvellesDonnees
cp -i fichier.txt /home/Dossier # Demande confirmation lors du remplacement de fichier.txt qui existe déjà dans Dossier
cp -v anciennesDonnees /home/nouvellesDonnees # Sortie verbeuse, c'est-à-dire confirmation de la copie du répertoire
cp -f fichier.txt /nouveauDossier # Copie le fichier de force
```

**2.** `mv`

La commande `mv` est utilisée pour déplacer des fichiers et des répertoires d'un emplacement à un autre. Elle est également utilisée pour renommer un fichier ou un répertoire.

Syntaxe de `mv` :

```bash
mv [OPTIONS] [SOURCE] [DESTINATION]
```

Exemple :

```bash
mv monFichier.txt /home/nouveauDossier # Déplace monFichier dans nouveauDossier
mv monFichier1.txt monFichier2.txt /home/nouveauDossier # Déplace plusieurs fichiers dans nouveauDossier
mv -i fichier.txt /home/echantillon # Demande avant de remplacer le fichier.txt qui existe déjà dans echantillon
mv -v anciennesDonnees /home/echantillon # Mode verbeux, c'est-à-dire confirmation du déplacement du répertoire anciennesDonnees dans le répertoire echantillon
mv ancienFichier.txt nouveauFichier.txt # Renomme le fichier
```

**3.** `rm`

La commande `rm` est utilisée pour supprimer des fichiers et des répertoires.

Syntaxe de `rm` :

```bash
rm [OPTIONS] [NOM_DE_FICHIER_OU_DE_REPERTOIRE]
```

Exemple :

```bash
rm fichier.txt # Supprime un seul fichier
rm fichier1.txt fichier2.txt # Supprime plusieurs fichiers
rm dossierVide # Ne fonctionnera pas pour un répertoire vide (La commande suivante gérera ce cas !)
rm -r mesDonnees # Supprime un répertoire non vide de manière récursive
rm -r -i mesDonnees # Demande confirmation avant de supprimer chaque fichier
rm -r -f mesDonnees # Supprime un répertoire non vide de manière récursive sans confirmation
rm -r -f -v mesDonnees # Supprime un répertoire non vide de manière récursive sans confirmation en mode verbeux
```

**4.** `rmdir`

La commande `rmdir` est utilisée pour supprimer uniquement les répertoires vides.

Syntaxe de `rmdir` :

```bash
rmdir [OPTIONS] [NOM_DE_FICHIER_OU_DE_REPERTOIRE]
```

Exemple :

```bash
rmdir dossierVide # Supprime le répertoire vide dossierVide
rmdir monDossier1 monDossier2 monDossier3 # Supprime plusieurs répertoires vides
rmdir monDossier # Ne fonctionnera pas pour les répertoires non vides (Utilisez 'rm -r nom_du_dossier' pour ce cas !)
```

## Mots de la fin

Félicitations ! Vous avez réussi à apprendre les bases de Red Hat Enterprise Linux (RHEL) et les commandes essentielles qui forment la base des systèmes Linux.

Continuez à pratiquer ces commandes, et bientôt elles deviendront une seconde nature pour vous. La maîtrise vient avec la répétition, alors continuez à expérimenter et à appliquer ces fondamentaux dans des scénarios réels.

Restez à l'écoute pour plus d'articles. Préparez-vous à faire passer vos compétences RHEL au niveau supérieur.

[Connectons-nous !](https://linktr.ee/tanishkamakode)