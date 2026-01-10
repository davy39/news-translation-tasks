---
title: Ne pas utiliser le Ruby système de Mac – Utilisez ceci à la place
subtitle: ''
author: Daniel Kehoe
co_authors: []
series: null
date: '2021-02-10T17:27:03.000Z'
originalURL: https://freecodecamp.org/news/do-not-use-mac-system-ruby-do-this-instead
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/photo-1522776851755-3914469f0ca2.jpeg
tags:
- name: best practices
  slug: best-practices
- name: mac
  slug: mac
- name: Ruby
  slug: ruby
seo_title: Ne pas utiliser le Ruby système de Mac – Utilisez ceci à la place
seo_desc: 'Someone may have once told you, "Don''t use the system Ruby." It''s good
  advice, but why? Let''s find out.

  Which Ruby do you have?

  MacOS comes with a "system Ruby" pre-installed.

  Use the which command to see where Ruby is installed:

  $ which ruby

  /usr/bi...'
---

Quelqu'un vous a peut-être déjà dit : "Ne pas utiliser le Ruby système." C'est un bon conseil, mais pourquoi ? Découvrons-le.

## Quel Ruby avez-vous ?

MacOS est livré avec un "Ruby système" préinstallé.

Utilisez la commande `which` pour voir où Ruby est installé :

```bash
$ which ruby
/usr/bin/ruby
```

Si vous voyez `/usr/bin/ruby`, il s'agit du Ruby système macOS préinstallé.

Il est acceptable d'utiliser le Ruby système pour exécuter des scripts d'administration système, tant que vous ne modifiez pas le Ruby système en tentant de le mettre à jour ou d'ajouter des gems.

Mais vous ne voulez pas l'utiliser lorsque vous développez des projets en Ruby.

## Ruby pour le développement

Pour développer des projets avec Ruby, vous devriez [Installer Ruby avec Homebrew](https://mac.install.guide/ruby/12.html) ou utiliser un gestionnaire de versions tel que asdf, chruby, rbenv ou rvm.

Un gestionnaire de versions est utile si vous jonglez avec plusieurs projets et ne pouvez pas tout mettre à jour en même temps. Pour un guide qui compare les gestionnaires de versions et montre la meilleure façon d'installer Ruby, consultez mon article [Installer Ruby sur un Mac](https://mac.install.guide/ruby/index.html).

Mais pourquoi ne pas utiliser le Ruby par défaut de macOS ? Examinons les raisons pour lesquelles il est mauvais d'utiliser le Ruby par défaut de Mac pour le développement.

### Problèmes d'installation des gems

Les RubyGems sont des bibliothèques logicielles prêtes à l'emploi qui rendent le développement facile et amusant en Ruby. La plupart des projets Ruby utilisent au moins quelques gems.

Si vous utilisez le Ruby système de Mac, l'exécution de `gem install` tentera d'enregistrer les gems dans le répertoire du système Ruby `/Library/Ruby/Gems/2.6.0`. Ce répertoire est possédé par `root`, le superutilisateur du système. Les utilisateurs ordinaires n'ont pas le droit d'y écrire (et vous ne devriez vraiment pas modifier ce dossier).

Si vous essayez d'installer une gem, par exemple `gem install rails`, vous obtiendrez une erreur de permissions :

```bash
ERROR: While executing gem ... (Gem::FilePermissionError)
You don't have write permissions for the /Library/Ruby/Gems/2.6.0 directory
```

### Cela viole la sécurité du système

Les systèmes basés sur Unix sont puissants, il existe donc une solution de contournement. Vous pouvez installer des gems en tant que superutilisateur pour outrepasser la restriction des permissions. Mais ne faites pas cela !

```bash
$ sudo gem install rails
```

Chaque fois que vous êtes sur le point d'exécuter `sudo`, vous devriez vous arrêter et vous demander si vous êtes sur le point de vous tirer une balle dans le pied.

Dans ce cas, vous avez besoin de `sudo` parce que vous modifiez des fichiers système gérés par le système d'exploitation. Ne le faites pas ! Vous pourriez laisser le système dans un état endommagé ou compromis. Pire encore, une gem pourrait contenir un code malveillant qui manipule votre ordinateur.

### Gestion des gems

Les développeurs expérimentés utilisent [Bundler](https://bundler.io/) pour installer des gems et gérer leurs dépendances.

Imaginez que vous avez des projets qui utilisent différentes versions d'une gem (peut-être qu'une nouvelle version de gem est sortie entre vos projets). Ou peut-être que deux gems différentes dans votre projet dépendent de différentes versions d'une gem dépendante.

Bundler utilise un Gemfile dans votre répertoire de projet pour suivre les gems dont vous avez besoin. Si vous utilisiez `sudo` pour installer des gems avec le Ruby système, vous vous retrouveriez avec un désordre de gems incompatibles dans le répertoire du système Ruby.

Vous pouvez contourner le problème des permissions du système en [installant Bundler](https://bundler.io/doc/troubleshooting.html) avec une commande qui utilise votre répertoire personnel pour les gems. Mais il est plus facile d'installer Ruby avec Homebrew ou d'utiliser un gestionnaire de versions et d'utiliser le Bundler qui est installé, ce qui configurera correctement votre environnement de développement local.

### Utilisez la dernière version de Ruby

Lorsque vous commencez un projet, utilisez la dernière version de Ruby (c'est la 3.0 au moment où ceci a été écrit).

Le Ruby système dans macOS Catalina ou Big Sur est Ruby 2.6.3, qui est ancien. Si vous commencez tout juste avec Ruby, installez-le avec Homebrew et travaillez sur un projet avec Ruby 3.0. Lorsque vous commencez à construire un autre projet, il peut être temps d'installer un gestionnaire de versions afin de pouvoir jongler avec des projets utilisant différentes versions de Ruby.

## MacOS après Big Sur

MacOS Big Sur est maintenant la version actuelle. [Apple dit](https://developer.apple.com/documentation/macos-release-notes/macos-catalina-10_15-release-notes) :

> _"Les environnements d'exécution des langages de script tels que Python, Ruby et Perl sont inclus dans macOS pour la compatibilité avec les logiciels hérités. Les futures versions de macOS n'incluront pas d'environnements d'exécution de langages de script par défaut et pourraient nécessiter l'installation de packages supplémentaires."_

Si vous lisez ceci à la fin de 2021, le Ruby système a peut-être déjà disparu. Si ce n'est pas le cas, préparez-vous en installant Ruby avec Homebrew ou un gestionnaire de versions.

## Profitez de Ruby

Pour les développeurs prévoyant de construire des applications web avec Rails, j'ai écrit un guide, [Installer Rails sur un Mac](https://learn-rails.com/install-rails-mac/index.html), qui va au-delà de [Installer Ruby sur un Mac](https://mac.install.guide/ruby/index.html) pour montrer comment choisir un gestionnaire de versions qui fonctionnera avec Node ainsi qu'avec Ruby.

Profitez du plaisir de coder en Ruby ! Après tout, il est connu comme un langage dédié au bonheur des programmeurs. Mais n'oubliez pas, le Ruby système est là pour macOS, pas pour vous.