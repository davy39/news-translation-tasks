---
title: Qu'est-ce que la signature de commit dans Git ?
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-06-02T23:14:01.000Z'
originalURL: https://freecodecamp.org/news/what-is-commit-signing-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/cover-1.jpg
tags:
- name: Cryptography
  slug: cryptography
- name: Git
  slug: git
- name: Security
  slug: security
seo_title: Qu'est-ce que la signature de commit dans Git ?
seo_desc: 'Git has a feature to "sign" commits, but what is signing, and what are
  the benefits?

  TL;DR: If you don''t care for the details, and just need to get commit signing setup
  quickly, skip to How to Sign Commits.

  Signing, or code signing specifically, is t...'
---

[Git](https://git-scm.com/) dispose d'une fonctionnalité pour "signer" les commits, mais qu'est-ce que la signature et quels sont ses avantages ?

**TL;DR :** Si vous ne vous intéressez pas aux détails et souhaitez simplement configurer rapidement la signature de commit, passez à [Comment signer les commits](#heading-comment-signer-les-commits-dans-git).

La signature, ou plus précisément la signature de code, est le processus d'utilisation de la cryptographie pour ajouter numériquement une signature aux données. Le destinataire des données peut vérifier que la signature est authentique et qu'elle provient donc du signataire.

C'est comme les signatures physiques, mais en version numérique et plus fiable.

# Comportement par défaut de Git

Tout d'abord, notons que tous les commits ont les propriétés suivantes :

* Auteur – Le contributeur qui a effectué le travail, ceci est *informatif*.

* Committer – L'utilisateur qui a validé le changement.

Dans la plupart des cas, ils seront identiques, mais ils peuvent être remplacés lors de la validation, il est donc important de noter la différence.

Lorsque vous avez installé Git pour la première fois, vous avez probablement dû configurer quelques paramètres, notamment `user.email` et `user.name`. Cela peut avoir été géré pour vous selon votre client Git.

Dans la ligne de commande, cela nécessite l'exécution des commandes suivantes :

```shell
git config --global user.email "seth@example.org"
git config --global user.name "Seth Falco"
```

Les commits Git sont basés sur la confiance, donc il supposera que vous avez entré votre vrai email et votre vrai nom. Vous pouvez ensuite valider et pousser vers des fournisseurs distants comme GitHub et GitLab avec les détails fournis.

Que se passe-t-il lorsque quelqu'un d'autre utilise votre adresse email, puis pousse des changements à distance ?

```shell
git config --global user.email "seth@example.org"
git commit -m "Jen a fait cela."
git push origin main
```

![Jen a fait un commit, mais cela montre mon nom et des liens vers mon profil GitHub.](https://www.freecodecamp.org/news/content/images/2021/05/figure-1-c.png align="left")

Le résultat semble normal, mais ce n'est pas moi qui ai fait ce commit. Jen a validé dans son dépôt, s'authentifiant avec ses identifiants GitHub, mais cela montre mon nom et un lien vers mon profil. Le comportement par défaut définit à la fois l'auteur et le committer avec les détails dans `git config`.

Sur GitHub, le commit est déjà indiscernable du mien. Si un utilisateur a défini `user.email` et `user.name` comme les miens, qu'il peut obtenir en faisant `git log` sur l'un de mes commits, alors même localement cela semblerait identique.

Cela signifie que n'importe qui peut définir son `user.email` avec votre adresse email, et cela semblerait comme si vous aviez fait le commit.

# Pourquoi Git fait-il cela ?

Vous pourriez vous demander pourquoi cela est possible. Après tout, vous vous authentifiez à votre compte lorsque vous poussez vers le dépôt, ne devrait-il pas utiliser cet email ? Cela ne semble-t-il pas un peu défectueux ?

Lorsque vous vous authentifiez pour pousser vers des dépôts distants, vous vous authentifiez pour faire exactement cela – pousser des changements. Les commits ne nécessitent pas d'authentification, quel que soit l'auteur ou le committer.

Si les commits nécessitaient une authentification par défaut, il serait impossible de migrer ou de miroir des projets vers d'autres plateformes. L'historique des commits inclura des anciens employés, des utilisateurs décédés, des comptes inactifs ou des adresses email qui ne sont pas sur d'autres plateformes.

La seule solution serait de réécrire l'historique pour supprimer qu'ils ont déjà travaillé sur le projet, ce qui n'est pas idéal.

Un autre scénario serait si je forkais un projet sur GitHub, mais que je souhaite maintenir mon fork sur GitLab. Mon premier push inclurait tous les commits des précédents committers. Pour un grand projet, il n'est pas réaliste d'authentifier chaque committer.

L'auteur d'un commit signifie l'attribution de qui a fait le travail, et non la preuve de qui a fait le travail.

En fait, vous pouvez toujours remplacer l'auteur lors de la validation, juste pour cette raison. En utilisant l'argument `--author`, vous pouvez spécifier un nom et un email différents de vos paramètres globaux, même des détails qui ne sont pas associés à un compte où le dépôt est hébergé.

Sur les dépôts publics, soyez prudent lorsque vous validez au nom de quelqu'un sans compte, cependant. Les noms et adresses email deviennent des informations publiques une fois poussés, et sont accessibles à quiconque utilise `git log` !

```shell
git commit -m "Jen n'a même pas écrit cela." --author "Jen <jen@example.org>"
git push origin main
```

Cela a un comportement différent de l'utilisation d'un autre email dans `git config`. Cela fait de l'auteur ce que nous avons spécifié dans `--author`, mais le committer ce que nous avons spécifié dans `git config`.

![GitHub affiche que Jen est l'auteur et que je suis le committer.](https://www.freecodecamp.org/news/content/images/2021/05/figure-2-c.png align="left")

Les plateformes de traduction comme [Weblate](https://weblate.org/) s'appuient sur cette fonctionnalité pour garantir que les traducteurs obtiennent toujours une attribution, même si un utilisateur automatisé valide et ouvre les demandes de tirage, et non le traducteur.

# Comment prouver que vous êtes le committer dans Git

[GNU Privacy Guard](https://gnupg.org/) (GnuPG ou GPG) vous permet de créer des paires de clés cryptographiques asymétriques qui peuvent être utilisées pour le chiffrement et la signature des données. Elles se composent d'une clé publique et d'une clé privée.

Vous pouvez partager la clé publique avec n'importe qui – vous pouvez télécharger cela sur vos comptes GitHub et GitLab, ou le mettre sur internet pour que n'importe qui puisse y accéder.

La clé privée, comme son nom l'indique, est privée. Vous devriez traiter cela comme un mot de passe, et en aucun cas vous ne devriez partager votre clé privée avec qui que ce soit.

Nous allons générer une paire de clés, puis télécharger la clé publique sur GitHub et GitLab. En utilisant votre clé privée, vous pouvez signer vos commits, et les serveurs avec la clé publique l'utiliseront pour confirmer que c'était bien vous.

# Comment signer les commits dans Git

Je ne couvrirai que comment faire cela dans le terminal, car cela fournit une expérience uniforme sur les systèmes d'exploitation. Si vous n'êtes pas à l'aise avec le terminal, vous devez simplement copier les commandes.

## Prérequis

Le seul prérequis, autre que Git lui-même, est d'installer l'utilitaire de ligne de commande GPG.

Vous pouvez vérifier s'il est installé avec `gpg --version`.

### Windows

#### Git BASH

Si vous avez installé Git BASH (optionnellement inclus avec [Git pour Windows](https://gitforwindows.org/)), alors vous avez déjà accès à GPG. Il suffit de lancer une instance de Git BASH, et il sera disponible immédiatement.

#### Gpg4win

Si vous n'avez pas Git BASH, alors il n'est pas nécessaire de l'installer. Vous pouvez installer [Gpg4win](https://gpg4win.org/download.html), qui fournira GPG globalement, afin que vous puissiez l'utiliser simplement depuis PowerShell.

Lors de l'installation de Gpg4win, vous pouvez décocher tous les composants supplémentaires, car nous n'en aurons pas besoin puisque nous prévoyons d'utiliser le terminal.

![L'écran de choix des composants sur l'installation de Gpg4win avec tous les composants supplémentaires décochés.](https://www.freecodecamp.org/news/content/images/2021/05/figure-3-1.png align="left")

Si vous aviez déjà PowerShell ouvert, vous devrez le redémarrer avant de pouvoir utiliser GPG.

### Linux

Votre distribution inclut probablement déjà GPG. Si ce n'est pas le cas, vous pouvez l'installer via votre gestionnaire de paquets.

#### apt (Debian / Ubuntu)

`sudo apt install gnupg`

#### pacman (Arch / Manjaro)

`sudo pacman -S gnupg`

## Comment générer des clés GPG

Si vous avez déjà une clé GPG, vous pouvez sauter cette étape. Il est tout à fait acceptable de réutiliser les clés GPG. Lisez simplement ce qui suit et vérifiez que votre clé est compatible avec Git et GitHub.

Vous pouvez obtenir une liste de vos clés GPG avec :

```shell
gpg --list-keys
```

Tout d'abord, nous devons générer une paire de clés RSA. La commande suivante lancera un script interactif qui posera des questions afin que nous puissions fournir les informations nécessaires.

```shell
gpg --full-gen-key
```

1. Pour le type de clé que vous souhaitez, entrez `1` qui est "RSA et RSA".

2. Pour la taille de la clé, entrez `4096`. C'est la taille minimale pour GitHub et GitLab, et la taille maximale que GPG nous permettra de générer.

3. Pour la durée de validité de la clé, utilisez ce qui vous convient. Par défaut, c'est `0`, ce qui signifie qu'elle n'expirera jamais.

4. Vérifiez que les informations sont correctes en entrant `y`.

GPG demandera des informations personnelles qui sont stockées dans votre clé.

1. Votre nom, cela peut être n'importe quoi d'au moins 5 caractères de long.

2. Votre adresse email, utilisez un email avec lequel vous prévoyez de commiter. Vous devez avoir vérifié cet email sur le compte distant avec lequel vous allez pousser.

3. Un commentaire, vous pouvez taper ce que vous voulez, ou appuyer sur entrée pour le laisser vide.

4. Vérifiez que les informations sont correctes en entrant `o`.

```plaintext
root@799d1cc3c99c:/# gpg --full-gen-key
gpg (GnuPG) 2.2.19; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
  (14) Existing key from card
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 0
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: Seth Falco
Email address: seth@example.org
Comment: 
You selected this USER-ID:
    "Seth Falco <seth@example.org>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
```

GPG demandera une phrase de passe pour protéger la clé. Vous pouvez la définir à n'importe quoi, ou la laisser vide pour aucune phrase de passe. Bien sûr, il est idéal d'utiliser une bonne phrase de passe, faites confiance à votre gestionnaire de mots de passe si vous en utilisez un.

L'invite de mot de passe dépend de l'environnement, donc cette étape aura un aspect différent pour différents utilisateurs, mais ce qu'elle demande est effectivement le même.

Il commencera à générer la clé, ce qui nécessite beaucoup de données générées aléatoirement. Effectuer des actions sur votre PC aidera à la rendre plus aléatoire, donc je recommande de déplacer votre souris pendant la génération de la clé.

## Comment exporter vos clés

Ensuite, vous devez obtenir l'identifiant de la nouvelle clé générée afin de pouvoir y faire référence lors de l'exportation de votre clé et de la configuration de Git.

Les clés GPG peuvent être référencées de plusieurs manières. Il est bon de prendre l'habitude d'utiliser et de partager l'empreinte complète, pour minimiser le risque d'ambiguïté lorsque les utilisateurs la demandent à partir d'un serveur de clés. Les IDs longs (64 bits) sont bien *pour l'instant*, mais les IDs courts (32 bits) sont à éviter, car il est facile de produire une collision. ([Plus d'informations](https://evil32.com/))

Nous utiliserons l'empreinte complète de GPG, que nous pouvons obtenir avec la commande :

```shell
gpg --list-keys
```

Vous obtiendrez une sortie comme celle-ci :

```shell
pub   rsa4096 2021-05-23 [SC]
      C6656513A0F9B7B7F4E76389EF39187D04795745
uid           [ultimate] Seth Falco <seth@example.org>
sub   rsa4096 2021-05-23 [E]
```

Pour moi, c'est `C6656513A0F9B7B7F4E76389EF39187D04795745`. Assurez-vous d'utiliser votre empreinte au lieu de la mienne lorsque vous exécutez le reste des commandes.

Vous devez exporter la clé publique afin de pouvoir la télécharger sur GitHub. Nous utilisons l'argument `--armor` pour indiquer que nous voulons l'exporter dans un format [ASCII armored](https://en.wikipedia.org/wiki/Binary-to-text_encoding) au lieu de binaire. Cela écrit la clé publique dans un fichier nommé `gpg-key.pub`.

```shell
gpg --export --armor C6656513A0F9B7B7F4E76389EF39187D04795745 > ./gpg-key.pub
```

### Comment sauvegarder vos clés

Il est utile d'avoir une sauvegarde à distance de vos clés GPG car vous les utiliserez probablement sur plusieurs services. Si vous la perdez, il serait pénible de tout mettre à jour.

Vous pouvez exporter votre clé privée de la même manière que nous avons exporté la clé publique, cela écrit la clé privée dans un fichier nommé `gpg-key.asc` :

```shell
gpg --export-secret-keys --armor C6656513A0F9B7B7F4E76389EF39187D04795745 > ./gpg-key.asc
```

Vous pouvez maintenant sauvegarder vos clés publique et privée, mais n'oubliez pas que vous ne devez jamais envoyer la copie non chiffrée de la clé privée dans le cloud. Utilisez toujours un stockage cloud chiffré de bout en bout, ou un gestionnaire de mots de passe comme [Bitwarden](https://bitwarden.com/) pour sauvegarder les données sensibles.

## Comment activer la signature de commit

Ensuite, pour activer la signature de tous les commits, définissez le paramètre `commit.gpgsign` en utilisant `git config`. Cela fera en sorte que `git commit` signe les commits par défaut.

```shell
git config --global commit.gpgsign true
```

Si vous avez plusieurs clés GPG, ou simplement pour référence future, vous pouvez également définir `user.signingkey`. Cela indiquera spécifiquement quelle clé Git doit utiliser pour la signature afin d'éviter toute ambiguïté.

```shell
git config --global user.signingkey C6656513A0F9B7B7F4E76389EF39187D04795745
```

## Comment utiliser votre clé

Enfin, vous devez télécharger votre clé publique. Vous pouvez utiliser la même clé GPG pour GitHub et GitLab, ou tout autre fournisseur Git.

Nous aurons besoin de la clé publique exportée pour les étapes suivantes, alors ouvrez le fichier `gpg-key.pub` dans n'importe quel éditeur comme Visual Studio Code, et copiez le contenu dans votre presse-papiers.

Sur GitHub, vous pouvez aller dans vos [paramètres](https://github.com/settings/profile), sous "[SSH et clés GPG](https://github.com/settings/keys)", puis cliquez sur "[Nouvelle clé GPG](https://github.com/settings/gpg/new)". Collez le contenu de `gpg-key.pub` dans le champ Clé sur GitHub, et cliquez sur "Ajouter une clé GPG".

![Ajout d'une clé GPG dans les paramètres de GitHub.](https://www.freecodecamp.org/news/content/images/2021/05/figure-4-c-1.png align="left")

Sur GitLab, les étapes sont presque identiques, allez simplement dans vos [préférences](https://gitlab.com/-/profile/preferences), puis "[Clés GPG](https://gitlab.com/-/profile/gpg_keys)". Collez le contenu de `gpg-key.pub` dans le champ Clé sur GitLab, et cliquez sur "Ajouter une clé".

Vous êtes maintenant en mesure de faire des commits signés dans vos dépôts ! Le prochain commit demandera votre mot de passe de clé GPG, puisque c'est la première fois que vous l'utilisez. Les commits suivants seront transparents.

# Comment vérifier les commits dans Git

GitHub et GitLab afficheront un badge "Vérifié" à côté de vos nouveaux commits.

![Un commit signé sur GitHub, il montre un badge vérifié sur le côté.](https://www.freecodecamp.org/news/content/images/2021/05/figure-5-c.png align="left")

![Un commit signé sur GitLab, il montre un badge vérifié sur le côté.](https://www.freecodecamp.org/news/content/images/2021/05/figure-6-c-2.png align="left")

La dernière chose à retenir est que la signature de commit ne vérifie que le committer, et non l'auteur. Cela signifie que lorsque vous voyez un commit vérifié, l'auteur n'a rien à voir avec le statut vérifié.

![Un commit signé avec le badge vérifié, mais Jen n'est pas l'auteur de ce commit.](https://www.freecodecamp.org/news/content/images/2021/05/figure-7-c-1.png align="left")

## Mode Vigilant

En bonus, sur GitHub spécifiquement, il existe un paramètre appelé [mode vigilant](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/displaying-verification-statuses-for-all-of-your-commits).

Vous pouvez optionnellement activer cela si vous souhaitez que tous les commits non signés indiquent explicitement "Non vérifié". Cela peut être activé dans vos [paramètres](https://github.com/settings/profile), sous "[SSH et clés GPG](https://github.com/settings/keys)", puis cochez "Marquer les commits non signés comme non vérifiés".

![Le paramètre de mode vigilant sur GitHub.](https://www.freecodecamp.org/news/content/images/2021/05/figure-8-c-2.png align="left")

Maintenant, le commit que Jen a fait avec mon adresse email montre "Non vérifié" à côté, pour indiquer qu'il n'a pas été signé avec une clé associée à mon compte.

![Le commit que Jen a fait avec mes détails plus tôt, montrant maintenant un badge non vérifié à côté.](https://www.freecodecamp.org/news/content/images/2021/05/figure-9-c.png align="left")