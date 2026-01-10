---
title: Comment gérer plusieurs comptes GitHub sur une seule machine avec des clés
  SSH
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T13:54:24.000Z'
originalURL: https://freecodecamp.org/news/manage-multiple-github-accounts-the-ssh-way-2dadc30ccaca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OnUzsFnzyPzklZWjgRLr5g.png
tags:
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment gérer plusieurs comptes GitHub sur une seule machine avec des clés
  SSH
seo_desc: 'By Bivil M Jacob

  The need to manage multiple GitHub accounts on the same machine comes up at some
  point in time for most developers. Every single time I happen to change my Mac or
  need to Git push with a new work account, I end up surfing for the how...'
---

Par Bivil M Jacob

Le besoin de gérer plusieurs comptes GitHub sur la même machine se présente à un moment donné pour la plupart des développeurs. Chaque fois que je change mon Mac ou que j'ai besoin de faire un Git push avec un nouveau compte professionnel, je me retrouve à surfer sur le web pour trouver comment faire quelque chose que j'ai fait plus d'une demi-douzaine de fois.

Ma paresse à ne pas documenter le processus et mon incapacité à me souvenir des étapes me font perdre un temps précieux à rassembler les morceaux d'informations de partout sur le web et à essayer de les faire fonctionner.

Je suis sûr qu'il y a beaucoup d'entre vous qui ont été là, qui l'ont fait et encore plus d'entre vous qui attendent simplement la prochaine fois que la même chose se produit (moi y compris !). Cette entreprise est destinée à nous aider tous.

#### 1. Génération des clés SSH

Avant de générer une clé SSH, nous pouvons vérifier si nous avons des clés SSH existantes : `ls -al ~/.ssh` Cela listera toutes les paires de clés publiques et privées existantes, le cas échéant.

Si `~/.ssh/id_rsa` est disponible, nous pouvons le réutiliser, sinon nous pouvons d'abord générer une clé vers `~/.ssh/id_rsa` par défaut en exécutant :

```
ssh-keygen -t rsa
```

Lorsque l'on vous demande l'emplacement pour enregistrer les clés, acceptez l'emplacement par défaut en appuyant sur Entrée. Une clé privée et une clé publique `~/.ssh/id_rsa.pub` seront créées à l'emplacement SSH par défaut `~/.ssh/`.

Utilisons cette paire de clés par défaut pour notre compte personnel.

Pour les comptes professionnels, nous créerons différentes clés SSH. Le code ci-dessous générera les clés SSH et enregistrera la clé publique avec le tag « email@work_mail.com » dans `~/.ssh/id_rsa_work_user1.pub`

```bash
$ ssh-keygen -t rsa -C "email@work_mail.com" -f "id_rsa_work_user1"
```

Nous avons deux clés différentes créées :

```bash
~/.ssh/id_rsa
~/.ssh/id_rsa_work_user1
```

#### 2. Ajout de la nouvelle clé SSH au compte GitHub correspondant

Nous avons déjà les clés publiques SSH prêtes, et nous allons demander à nos comptes GitHub de faire confiance aux clés que nous avons créées. Cela permet d'éviter de devoir taper le nom d'utilisateur et le mot de passe à chaque fois que vous faites un Git push.

Copiez la clé publique `pbcopy < ~/.ssh/id_rsa.pub` puis connectez-vous à votre compte GitHub personnel :

1. Allez dans `Paramètres`
2. Sélectionnez `Clés SSH et GPG` dans le menu de gauche.
3. Cliquez sur `Nouvelle clé SSH`, donnez un titre approprié et collez la clé dans la boîte ci-dessous
4. Cliquez sur `Ajouter une clé` — et vous avez terminé !

> Pour les comptes professionnels, utilisez les clés publiques correspondantes (`pbcopy < ~/.ssh/id_rsa_work_user1.pub`) et répétez les étapes ci-dessus dans vos comptes GitHub professionnels.

#### 3. Enregistrement des nouvelles clés SSH avec l'agent ssh

Pour utiliser les clés, nous devons les enregistrer avec l'**ssh-agent** sur notre machine. Assurez-vous que l'agent ssh est en cours d'exécution en utilisant la commande `eval "$(ssh-agent -s)"`.
Ajoutez les clés à l'agent ssh comme suit :

```bash
ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/id_rsa_work_user1
```

Faites en sorte que l'agent ssh utilise les clés SSH respectives pour les différents hôtes SSH.

C'est la partie cruciale, et nous avons deux approches différentes :

Utilisation du fichier de configuration SSH (Étape 4), et avoir une seule clé SSH active dans l'agent ssh à la fois (Étape 5).

### **4. Création du fichier de configuration SSH**

Ici, nous ajoutons en réalité les règles de configuration SSH pour différents hôtes, indiquant quel fichier d'identité utiliser pour quel domaine.

Le fichier de configuration SSH sera disponible dans **~/.ssh/config**. Modifiez-le s'il existe, sinon nous pouvons simplement le créer.

```bash
$ cd ~/.ssh/
$ touch config           // Crée le fichier s'il n'existe pas
$ code config            // Ouvre le fichier dans VS code, utilisez n'importe quel éditeur
```

Faites des entrées de configuration pour les comptes GitHub pertinents similaires à celle ci-dessous dans votre fichier `~/.ssh/config` :

```bash
# Compte personnel, - la configuration par défaut
Host github.com
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa
   
# Compte professionnel-1
Host github.com-work_user1    
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_work_user1
```

« **work_user1** » est l'identifiant GitHub pour le compte professionnel.

« **github.com-work_user1** » est une notation utilisée pour différencier les multiples comptes Git. Vous pouvez également utiliser la notation « **work_user1.github.com** ». Assurez-vous d'être cohérent avec la notation d'hôte que vous utilisez. Cela est pertinent lorsque vous clonez un dépôt ou lorsque vous définissez l'origine distante pour un dépôt local.

La configuration ci-dessus demande à l'agent ssh de :

* Utiliser **id_rsa** comme clé pour toute URL Git qui utilise **@github.com**
* Utiliser la clé **id_rsa_work_user1** pour toute URL Git qui utilise **@github.com-work_user1**

### 5. Une clé SSH active dans l'agent ssh à la fois

Cette approche ne nécessite pas les règles de configuration SSH. Nous nous assurons manuellement que l'agent ssh n'a que la clé pertinente attachée au moment de toute opération Git.

`ssh-add -l` listera toutes les clés SSH attachées à l'agent ssh. Supprimez-les toutes et ajoutez la seule clé que vous êtes sur le point d'utiliser.

Si c'est vers un compte Git personnel que vous êtes sur le point de pousser :

```bash
$ ssh-add -D            // supprime toutes les entrées ssh de l'agent ssh
$ ssh-add ~/.ssh/id_rsa                 // Ajoute la clé ssh pertinente
```

L'agent ssh a maintenant la clé mappée avec le compte GitHub personnel, et nous pouvons faire un Git push vers le dépôt personnel.

Pour pousser vers votre compte GitHub professionnel-1, changez la clé SSH mappée avec l'agent ssh en supprimant la clé existante et en ajoutant la clé SSH mappée avec le compte GitHub professionnel.

```bash
$ ssh-add -D
$ ssh-add ~/.ssh/id_rsa_work_user1
```

L'agent ssh a actuellement la clé mappée avec le compte GitHub professionnel, et vous pouvez faire un Git push vers le dépôt professionnel. Cela nécessite un peu d'effort manuel, cependant.

#### Définition de l'URL distante git pour les dépôts locaux

Une fois que nous avons des dépôts Git locaux clonés/créés, assurez-vous que le nom d'utilisateur et l'email de la configuration Git sont exactement ce que vous voulez. GitHub identifie l'auteur de tout commit à partir de l'email attaché à la description du commit.

Pour lister le nom et l'email de la configuration dans le répertoire Git local, faites `_git config user.name_` et `_git config user.email_`. Si ce n'est pas trouvé, mettez à jour en conséquence.

```bash
git config user.name "User 1"   // Met à jour le nom d'utilisateur de la configuration git
git config user.email "user1@workMail.com"
```

### 6. Lors du clonage des dépôts

Remarque : l'étape 7 aidera, si nous avons le dépôt déjà disponible en local.

Maintenant que les configurations sont en place, nous pouvons procéder au clonage des dépôts correspondants. Lors du clonage, notez que nous utilisons les noms d'hôtes que nous avons utilisés dans la configuration SSH.

Les dépôts peuvent être clonés en utilisant la commande de clonage fournie par Git :

```
git clone git@github.com:personal_account_name/repo_name.git
```

Le dépôt professionnel nécessitera une modification avec cette commande :

```bash
git clone git@github.com-work_user1:work_user1/repo_name.git
```

Cette modification est faite en fonction du nom d'hôte défini dans la configuration SSH. La chaîne entre @ et : doit correspondre à ce que nous avons donné dans le fichier de configuration SSH.

### 7. Pour les dépôts existants localement

**Si nous avons déjà le dépôt cloné :**

Lister le distant Git du dépôt, `git remote -v`

Vérifiez si l'URL correspond à notre hôte GitHub à utiliser, sinon mettez à jour l'URL de l'origine distante.

```bash
git remote set-url origin git@github.com-worker_user1:worker_user1/repo_name.git
```

Assurez-vous que la chaîne entre @ et : correspond à l'hôte que nous avons donné dans la configuration SSH.

**Si vous créez un nouveau dépôt en local :**

Initialisez Git dans le dossier du projet `git init`.

Créez le nouveau dépôt dans le compte GitHub puis ajoutez-le comme distant Git au dépôt local.

```bash
git remote add origin git@github.com-work_user1:work_user1/repo_name.git 
```

Assurez-vous que la chaîne entre @ et : correspond à l'hôte que nous avons donné dans la configuration SSH.

Poussez le commit initial vers le dépôt GitHub :

```bash
git add .
git commit -m "Initial commit"
git push -u origin master
```

Nous avons terminé !

L'ajout ou la mise à jour du distant Git du répertoire Git local avec l'hôte approprié permettra de sélectionner la bonne clé SSH pour vérifier notre identité avec GitHub. Avec tout ce qui précède en place, nos `opérations git` devraient fonctionner de manière transparente.