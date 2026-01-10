---
title: Comment gérer vos versions de Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-15T22:26:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-your-ruby-versions
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c91740569d1a4ca32f1.jpg
tags:
- name: Ruby
  slug: ruby
- name: toothbrush
  slug: toothbrush
seo_title: Comment gérer vos versions de Ruby
seo_desc: 'Ruby has changed over time

  Ruby has been in constant development since the 1990s. And like many languages,
  there have been syntax changes across versions. This means that it is important
  to be clear about which Ruby version your code expects.

  Probabl...'
---

## **Ruby a évolué au fil du temps**

Ruby est en développement constant depuis les années 1990. Et comme beaucoup de langages, il y a eu des changements de syntaxe entre les versions. Cela signifie qu'il est important d'être clair sur la version de Ruby que votre code attend.

Probablement le changement le plus visible est venu avec Ruby 1.9. Auparavant, nous écrivions les hashes comme ceci :

```ruby
  { :one => 1, :two => 2, :three => 3 }
```

Cette utilisation de l'opérateur "hashrocket" (`=>`) était si courante que Ruby 1.9 a fourni un raccourci :

```text
  { one: 1, two: 2, three: 3 }
```

Ce code plus ancien fonctionnera sur n'importe quelle version, mais la nouvelle syntaxe ne fonctionnera que sur Ruby 1.9+.

## **Comment cela pose-t-il des problèmes ?**

Par exemple, vous avez peut-être décidé d'utiliser un Gem qui repose en interne sur des fonctionnalités de Ruby 1.9. Cela signifie que votre projet repose également sur des fonctionnalités de Ruby 1.9.

Si vous ne spécifiez pas quelle version de Ruby votre projet nécessite, cela peut être très confus lorsque le code fonctionne sur une machine, mais pas sur une autre.

Comme pour la plupart des langages, il est considéré comme une bonne pratique de spécifier la version de Ruby que votre code attend. Cela facilite grandement la gestion de plusieurs projets sur votre machine de développement, chacun attendant une version différente de Ruby.

## **Comment spécifier ma version de Ruby ?**

Il existe quelques outils populaires pour cela, mais tous ont convenu de partager un fichier commun. De nombreux projets Ruby (ou Rails) incluront un simple fichier `.ruby-version`, qui spécifie simplement un numéro de version, par exemple :

```text
2.4.2
```

Les outils populaires pour vous aider à gérer votre version de Ruby sont :

* [Ruby Version Manager (RVM)](https://rvm.io/)
* [rbenv](https://github.com/rbenv/rbenv)

Examinons RVM.

### **Utilisation de RVM**

RVM est généralement installé ([lien](https://rvm.io/)) sur une machine Linux, Unix ou MacOS. Il est très pratique car il s'intègre à la commande `cd` (changer de répertoire). Ainsi, lorsque vous passez à un nouveau projet, votre fichier `.ruby-version` est lu automatiquement, et vous êtes automatiquement basculé vers la version correcte de Ruby avant de commencer à travailler.

Par exemple, vous pourriez avoir cette séquence :

```shell
% cd ~/projects/older-project
% ruby --version

ruby 2.3.5p376 (2017-09-14 revision 59905) [x86_64-darwin16]

% cd ~/projects/newer-project
% ruby --version

ruby 2.4.2p198 (2017-09-14 revision 59899) [x86_64-darwin16]
```

(Ces exemples proviennent d'une machine MacOS).

## Autres informations sur Ruby :

* [Une introduction à la programmation orientée objet avec Ruby](https://www.freecodecamp.org/news/introduction-to-object-oriented-programming-with-ruby-d594e1c6eebe/)
* [Les méthodes de tableau Ruby les plus courantes que vous devriez connaître](https://www.freecodecamp.org/news/p/62edc7d6-1ec8-4e6b-ab42-51136a3b7073/)