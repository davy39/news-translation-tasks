---
title: Comment configurer Git pour la première fois sur macOS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-08T20:07:30.000Z'
originalURL: https://freecodecamp.org/news/setup-git-on-mac
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template-1.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: macOS
  slug: macos
- name: version control
  slug: version-control
seo_title: Comment configurer Git pour la première fois sur macOS
seo_desc: 'If you''re setting up Git for the first time on a MacBook, you don''t have
  to struggle to get it done.

  Maybe you just got a new laptop, or you''re getting into tech for the first time
  with a MacBook. Either way, I''ve got you covered.

  This short article ...'
---

Si vous configurez Git pour la première fois sur un MacBook, vous n'avez pas à vous battre pour le faire.

Peut-être que vous venez d'avoir un nouvel ordinateur portable, ou vous vous lancez dans la technologie pour la première fois avec un MacBook. Dans les deux cas, je vous couvre.

Cet article court vous aidera à comprendre comment configurer Git sur macOS afin que vous puissiez retourner au travail immédiatement.

Je suppose que vous savez déjà ce qu'est Git et ce qu'il fait avant de lire cet article. Mais si vous ne le savez pas et avez besoin d'une introduction à Git et au contrôle de version, vous pouvez consulter [cet article sur Qu'est-ce que Git ? Un guide du débutant pour le contrôle de version Git.](https://www.freecodecamp.org/news/what-is-git-learn-git-version-control/)

*Commençons maintenant.*

## Comment installer Git sur un Mac

Il existe de nombreuses méthodes disponibles pour installer Git sur un ordinateur Mac, mais la plus facile est d'utiliser Homebrew. Vous pouvez trouver [d'autres méthodes et comment les faire fonctionner dans cette documentation](https://git-scm.com/download/mac) ou [ici](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Comment installer Git avec Homebrew

[Homebrew](https://brew.sh/) est un système de gestion de paquets logiciels gratuit et open-source qui simplifie l'installation de logiciels sur le système d'exploitation d'Apple (macOS). Vous pouvez l'utiliser pour installer tous les types de paquets dont vous aurez besoin à l'avenir, pas seulement Git. Cela le rend vraiment utile.

Vous n'avez pas besoin d'installer une application ou quoi que ce soit pour installer Homebrew. Vous devez simplement ouvrir le terminal et installer [Homebrew](https://brew.sh/) en exécutant la commande suivante :

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Note :** Une fois que vous avez entré la commande, elle demandera votre mot de passe.

Une fois que c'est réussi, vous pouvez procéder à l'installation de Git via la commande suivante dans votre terminal :

```bash
$ brew install git
```

À ce stade, si c'est réussi, vous avez installé Git sur votre Mac. Vous pouvez maintenant vérifier en exécutant la commande suivante dans votre terminal :

```bash
$ git --version
```

## Comment configurer Git dans macOS

Jusqu'à présent, vous avez appris comment installer Git – mais installer Git seul ne vous permet pas de pousser, tirer et commiter du code et d'effectuer d'autres opérations Git à partir de votre contrôle de version Git.

Pour travailler avec Git, vous devez configurer votre environnement Git en utilisant la commande `git config`. Cela vous donnera accès aux variables de configuration qui contrôlent le fonctionnement de Git sur votre système.

Deux variables de configuration git significatives dont vous avez besoin sont les variables d'identité. Celles-ci vous permettent de définir votre nom d'utilisateur et votre email. Ce sont le nom d'utilisateur et l'email que vous avez utilisés lors de la configuration de votre système de contrôle de version avec GitHub, GitLab, etc.

```bash
$ git config --global user.name "olawanlejoel"
$ git config --global user.email "mymail@gmail.com"
```

**Note :** Remplacez le nom et l'email par les vôtres. Vous devez également savoir que l'option `--global` garantit que ces valeurs sont utilisées dans tout votre système.

Une fois que vous avez fait cela, il y a quelques autres configurations que vous pouvez faire, qui consistent à configurer l'éditeur de texte par défaut et les couleurs pour votre console Git :

```bash
$ git config --global core.editor emacs
$ git config --global color.ui true
```

Vous pouvez choisir l'éditeur que vous utilisez régulièrement. J'ai choisi EMACS.

Maintenant, Git est prêt à être utilisé. Vous pouvez vérifier vos configurations Git pour vous assurer qu'elles sont correctes en utilisant cette commande :

```bash
$ git config --list
```

Cela affichera ce qui suit (avec vos propres informations) :

```bash
user.name=olawanlejoel
user.email=mymail@gmail.com
color.ui=true
```

Supposons qu'il y ait une erreur et que vous souhaitiez changer l'une des configurations. N'hésitez pas à réexécuter la commande de configuration particulière à l'erreur.

Par exemple, s'il y a une erreur avec mon email, je peux réexécuter la configuration de l'email pour la corriger :

```bash
$ git config --global user.email "mynewmail@gmail.com"
```

Maintenant, lorsque vous réexécutez la commande `--list`, vous obtiendrez la valeur mise à jour :

```bash
user.name=olawanlejoel
user.email=mynewmail@gmail.com
color.ui=true
```

## Conclusion

Dans cet article, vous avez appris comment configurer Git sur un ordinateur Mac pour la première fois.

Si vous souhaitez également voir comment le faire sur d'autres systèmes comme Windows et Linux, [consultez ce guide complet](https://www.freecodecamp.org/news/git-first-time-setup/).

De plus, si vous êtes également intéressé à apprendre quelques commandes Git de base, voici une [feuille de triche détaillée](https://www.freecodecamp.org/news/git-cheat-sheet/).

Amusez-vous bien à coder !