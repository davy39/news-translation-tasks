---
title: Comment lister toutes les URLs associées à un site web rapidement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T22:22:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-list-out-all-urls-associated-with-awebsite-fast-ish-d6056401ad85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L9q9fUiFwwYYJ49EzTH65g.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: terminal
  slug: terminal
- name: Web Development
  slug: web-development
seo_title: Comment lister toutes les URLs associées à un site web rapidement
seo_desc: 'By Ty Irvine

  So you need a list containing all the URLs for a website? Are you doing some redirects
  perhaps? Hit the limit on XML Sitemaps? Cool, me too. I’ve got just the tool for
  you that’ll get it done at about the same speed as XML Sitemaps, but ...'
---

Par Ty Irvine

Vous avez besoin d'une liste contenant toutes les URLs d'un site web ? Vous faites peut-être des redirections ? Vous avez atteint la limite sur [XML Sitemaps](https://www.xml-sitemaps.com/) ? Cool, moi aussi. J'ai juste l'outil qu'il vous faut qui fera le travail à peu près à la même vitesse que XML Sitemaps, mais vous aurez l'air bien plus cool en le faisant.

### Où le tutoriel commence vraiment

Pour obtenir votre liste d'URLs, nous allons utiliser Wget !

### Qu'est-ce que Wget ?

> _"Wget est un logiciel libre pour récupérer des fichiers en utilisant HTTP, HTTPS et FTP, les protocoles Internet les plus largement utilisés." — [Brew Formulas](https://brewformulas.org/wget)_

Et vous pouvez également l'utiliser pour demander une grande liste d'URLs associées à un domaine.

### 1. Installation de Wget

Pour installer Wget si ce n'est pas déjà fait, vous devrez d'abord installer [HomeBrew](https://brew.sh/) ; aka Brew. Brew est un gestionnaire de paquets, ce qui signifie qu'il installe et gère des logiciels pour vous. Vous pouvez consulter les instructions sur leur site web ou simplement suivre celles ci-dessous.

#### Installer Brew

Collez ceci dans un terminal et appuyez deux fois sur entrée (il peut vous demander un mot de passe.)

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Installer Wget

Maintenant que vous avez Brew installé, il est temps d'installer Wget. Collez ceci dans un terminal et appuyez sur entrée

```
brew install wget
```

### 2. Temps d'obtenir ces URLs

Maintenant que Wget est installé, nous téléchargeons simplement le site web puis affichons toutes ses URLs. Commencez par télécharger le site web que vous souhaitez avec

```
wget -r www.shutterandcode.com
```

Une fois le téléchargement terminé, nous listerons les URLs avec

```
find www.shutterandcode.com
```

(Assurez-vous d'utiliser le même nom de domaine que celui téléchargé).

![Image](https://cdn-media-1.freecodecamp.org/images/9ikDkfbIscUaE5AuL01lIhNmIYWZ5YWXqUKV)
_Temps de téléchargement : 3,7s_

#### Conclusion

Après une série de tests occasionnels opposant Wget à XML Sitemaps en utilisant des sites web plus petits, j'ai trouvé qu'ils étaient tous les deux à peu près au même niveau. Parfois l'un était plus rapide que l'autre, mais globalement ils avaient des vitesses similaires.

Si vous souhaitez en savoir plus sur les commandes Wget, tapez simplement ceci dans votre terminal

```
wget --help
```

J'espère que vous avez aimé lire ceci ! N'oubliez pas de liker, commenter et vous abonner ! 😉

p.s. ne vous sentez pas obligé de liker, commenter ou vous abonner car c'est simplement une blague pour les YouTubeurs :)

> **_MISE À JOUR : si vous ne voulez pas que le site soit réellement téléchargé sur votre ordinateur, ajoutez '--spider' après 'wget' comme ceci_**

```
wget -r --spider www.example.com
```

_Découvrez le post original et le reste de la série Snippets ! sur_

[_Shutter&Code — Le Blog_](https://www.shutterandcode.com/post/snippets-list-out-all-urls-associated-with-a-website-fast)