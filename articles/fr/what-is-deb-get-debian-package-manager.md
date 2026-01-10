---
title: Qu'est-ce que deb-get ? Comment installer le paquet Debian avec la commande
  deb-get
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2022-09-07T18:27:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-deb-get-debian-package-manager
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Debian-deb-get.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: package
  slug: package
seo_title: Qu'est-ce que deb-get ? Comment installer le paquet Debian avec la commande
  deb-get
seo_desc: "deb-get is a new command line utility built by Martin Wimpress, an active\
  \ contributor to the Linux community. \nYou can use this utility to install third-party\
  \ packages on your Debian machine. It only works with Debian or Debian-based distros\
  \ like Ubu..."
---

`deb-get` est un nouvel utilitaire en ligne de commande développé par [Martin Wimpress](https://twitter.com/m_wimpress), un contributeur actif de la communauté Linux. 

Vous pouvez utiliser cet utilitaire pour installer des paquets tiers sur votre machine Debian. Il ne fonctionne qu'avec Debian ou les distributions basées sur Debian comme Ubuntu, Linux Mint, Kali Linux, et ainsi de suite. 

## Pourquoi devriez-vous utiliser `deb-get` ?

C'est une excellente question. Je pense que `deb-get` est plus sécurisé et plus rapide que les autres gestionnaires de paquets. 

Par exemple, le paquet snap est beaucoup plus lent, et flatpak prend beaucoup d'espace pour installer un seul paquet dans votre système Debian. 

Le gestionnaire `deb-get` n'utilise que des fichiers `.deb` provenant d'une source officielle et les installe dans votre système.

### Avantages de la commande `deb-get`

Je pense que la commande `deb-get` a plus d'avantages que les autres gestionnaires de paquets comme snap, Flatpak, et ainsi de suite. 

1. La commande `deb-get` est un utilitaire bash léger et stable.
2. Vous pouvez facilement contribuer avec l'outil CLI deb-get. Vous pouvez ajouter votre propre paquet ou d'autres paquets dans deb-get. Pour ajouter un paquet, vous avez besoin de trois à quatre lignes de code.
3. La commande `deb-get` installe des paquets officiels à partir de la source. Elle ne supporte pas les paquets construits par des tiers.

### Inconvénients de la commande `deb-get`

Encore une fois, la commande `deb-get` a plus d'avantages que d'inconvénients. Mais le principal inconvénient est que `deb-get` est un nouvel utilitaire. Pour cette raison, il supporte moins de paquets que snap ou flatpak.

## Comment installer la commande `deb-get` sur une distribution Debian

Vous pouvez installer `deb-get` avec un script bash. Pour l'installation, vous avez besoin de la commande `curl` pour installer `deb-get` dans votre distribution Debian. Si vous avez déjà installé la commande `curl` sur votre distribution, alors passez cette étape.

```
sudo apt install curl  // déjà installé, alors passez cette étape.
curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get
```

La sortie de la commande ressemble à ceci :

![Installer la commande deb-get dans la distribution debian](https://www.freecodecamp.org/news/content/images/2022/09/Install-deb-get-command-by-linux.png)
_Votre installation de deb-get ressemble à ceci._

Confirmez que `deb-get` a été installé sur votre machine, puis exécutez la commande `deb-get version` dans votre terminal.

```
> deb-get version
0.3.5

```

## Comment utiliser `deb-get`

### Comment installer le paquet Debian avec `deb-get`

Avec la commande `deb-get install`, vous pouvez installer des paquets à partir de `deb-get`.

```
✨ deb-get install    <nom-du-paquet>

```

![Installer github-cli avec la commande deb-get](https://www.freecodecamp.org/news/content/images/2022/09/install-package-from-deb-get.png)
_Installer github-cli avec la commande deb-get_

### Comment supprimer un paquet avec `deb-get`

Avec la commande `deb-get purge` ou `deb-get remove`, vous pouvez supprimer n'importe quel paquet avec `deb-get`. Je préfère la commande `deb-get purge`, mais les deux drapeaux (`purge` et `remove`) fonctionnent de la même manière. Le drapeau `purge` supprime tous les fichiers de configuration qui sont installés ou configurés avec le paquet.

```
✨ deb-get purge   <nom-du-paquet>

```

![Supprimer ou désinstaller le paquet avec la commande deb-get](https://www.freecodecamp.org/news/content/images/2022/09/Delete-github-cli.png)
_Supprimer ou désinstaller le paquet avec la commande deb-get_

### Comment vérifier quels paquets sont disponibles dans `deb-get`

Vous pouvez vérifier la disponibilité des paquets de deux manières. Tout d'abord, vous pouvez visiter la [documentation officielle de deb-get](https://github.com/wimpysworld/deb-get#supported-software) pour trouver une liste des paquets disponibles. 

La deuxième manière est un utilitaire en ligne de commande. deb-get fournit de nombreux drapeaux ou options. Mes préférés sont les deux drapeaux qui accompagnent deb-get.

1. `deb-get list`
2. `deb-get search  <nom-du-paquet>` 

### Comment utiliser deb-get list

Le drapeau `deb-get list` fournit une liste de tous les paquets disponibles dans le terminal. 

![liste des paquets disponibles dans la commande deb-get](https://www.freecodecamp.org/news/content/images/2022/09/deb-get-list.png)
_liste des paquets disponibles_

### Comment utiliser deb-get search  <nom-du-paquet>

Le drapeau `deb-get search  <nom-du-paquet>` vous aide à trouver un paquet par son nom. Si le drapeau trouve un paquet, alors il retourne le paquet. Sinon, il retourne une chaîne vide.

![Rechercher un paquet avec deb-get](https://www.freecodecamp.org/news/content/images/2022/09/deb-get-search-chrome.png)
_Rechercher un paquet avec deb-get_

Vous pouvez vérifier toutes les commandes disponibles avec `deb-get help`.

## Conclusion

Je pense que le distributeur deb-get ou le gestionnaire de paquets Debian a plus de potentiel que les autres gestionnaires de paquets.

Chaque gestionnaire de paquets a des avantages et des inconvénients. Mais je crois que deb-get est un changement de jeu dans le futur. 

Vous pouvez partager et suivre sur [Twitter](https://twitter.com/Official_R_deep) et [Linkedin](https://www.linkedin.com/in/officalrajdeepsingh/). Si vous aimez mon travail, n'hésitez pas à lire plus de contenu sur [officialrajdeepsingh.dev](https://officialrajdeepsingh.dev/) et [Medium](https://officialrajdeepsingh.medium.com/).

### Références

%[https://github.com/wimpysworld/deb-get]

%[https://github.com/wimpysworld/deb-get/blob/main/CONTRIBUTING.md]