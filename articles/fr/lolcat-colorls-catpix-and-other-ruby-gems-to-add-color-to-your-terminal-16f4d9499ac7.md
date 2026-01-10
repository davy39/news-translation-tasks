---
title: Lolcat, Colorls, Catpix et autres Ruby Gems pour ajouter de la couleur à votre
  terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T20:43:09.000Z'
originalURL: https://freecodecamp.org/news/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U5qJqhlGM-xDL18zyKz0Sg.png
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Lolcat, Colorls, Catpix et autres Ruby Gems pour ajouter de la couleur
  à votre terminal
seo_desc: 'As well as making your terminal more colorful and productive through the
  prompt theme, font, and plugins, you can add even more features by using Ruby Gems,
  such as lolcat, colorls, and catpix.

  To use them, ensure you have Ruby installed on your comp...'
---

En plus de rendre votre [terminal plus coloré et productif grâce au thème de l'invite, à la police et aux plugins](https://hackernoon.com/make-your-terminal-more-colourful-and-productive-with-iterm2-and-zsh-11b91607b98c), vous pouvez ajouter encore plus de fonctionnalités en utilisant des [Ruby](https://www.ruby-lang.org/en/) Gems, tels que lolcat, colorls et catpix.

Pour les utiliser, assurez-vous d'avoir Ruby installé sur votre ordinateur, puis vous pouvez installer chacun d'eux en utilisant la commande `gem install <GEM_NAME>`.

### [lolcat](https://github.com/busyloop/lolcat)

Ce Gem ajoute un dégradé arc-en-ciel à tout ce que vous passez à travers lui. L'image en haut de l'article passe du texte ASCII généré avec le [Gem aarti](https://github.com/miketierney/artii) à travers lolcat pour créer un en-tête coloré dans le terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/ZwzujfO4aOxwBN3avPlNgnXSGBmxUAqV1f6v)

Vous pouvez combiner des commandes bash supplémentaires pour l'animer, dans ce cas `echo` pour imprimer la chaîne passée, `-a` pour animer et `-d` pour la durée.

```
echo I \u2764  Ruby | lolcat -a -d 500
```

![Image](https://cdn-media-1.freecodecamp.org/images/8lb5t0cCU554GFCZcVe91P7uVNPPpVgOoUxr)

Il existe un Gem basé sur lolcat appelé [lolize](https://github.com/miaout17/lolize), qui ajoute la couleur arc-en-ciel à la sortie Ruby. Une utilisation de celui-ci est de générer des logs plus colorés pour vos projets [Ruby on Rails](https://rubyonrails.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/pKwAQSBPggUMey2gLt7spU2vBsvgGbxTtcDQ)
_Le Gem lolize en action colorant les logs Ruby on Rails_

### [Artii](https://github.com/miketierney/artii)

Le Gem Artii génère de l'art ASCII basé sur le texte que vous lui passez en tant qu'arguments. Vous pouvez voir cela démontré dans l'image d'en-tête en haut de ce tutoriel. Si vous passez la sortie à lolcat, vous obtenez un texte d'art ASCII avec plusieurs couleurs.

```
artii 'Ruby Gems' --font slant | lolcat
```

Il est basé sur la bibliothèque [Figlet](http://www.figlet.org/), que vous pouvez également installer sur un Mac avec `brew install figlet`.

### [Colorls](https://github.com/athityakumar/colorls)

Cela améliore la commande terminal `[ls](https://en.wikipedia.org/wiki/Ls)` avec des couleurs et des icônes. Ci-dessous, une capture d'écran de son [dépôt Github](https://github.com/athityakumar/colorls). Cette configuration est un terminal [iTerm2](https://www.iterm2.com/) (Mac OS), avec `[oh-my-zsh](http://ohmyz.sh/)` avec le thème `[powerlevel9k](https://github.com/bhilburn/powerlevel9k)` et la police `powerline [nerd-font](https://github.com/ryanoasis/nerd-fonts) + awesome-config` avec le thème de couleur `Solarized Dark`.

![Image](https://cdn-media-1.freecodecamp.org/images/de2yPYFDVt2GAKcxSJNKV0vDjSjb9VWe7OfW)

Vous pouvez le rendre aussi facile à utiliser que `ls` en ajoutant un alias pour `lc` à votre fichier `~/.bashrc` ou `~/.zshrc`.

```
alias lc="colorls"
```

### [Catpix](https://github.com/pazdera/catpix)

Cela convertit les images dans un format qui peut être rendu sur un écran de terminal. Vous pouvez essayer d'avoir une image chargée dans votre terminal lorsqu'il démarre ou lorsqu'il y a un événement — par exemple lorsque vos tests passent.

![Image](https://cdn-media-1.freecodecamp.org/images/GX76uyNuda8nxxdfB-L5WLcjosfmmyjkcVh1)

### En savoir plus

Ce ne sont que quelques-uns des Ruby Gems qui peuvent améliorer votre terminal, et apprendre comment ils fonctionnent signifie que vous pouvez personnaliser votre ligne de commande. Vous pourriez même aller plus loin en ajoutant une configuration spéciale pour [irb](http://ruby-doc.org/stdlib-2.0.0/libdoc/irb/rdoc/IRB.html) et [pry](https://github.com/pry/pry/wiki/Customization-and-configuration), comme [irbtools](https://github.com/janlelis/irbtools).

#### En savoir plus sur les Gems sur Github

* [lolcat](https://github.com/busyloop/lolcat)
* [lolize](https://github.com/miaout17/lolize)
* [colorls](https://github.com/athityakumar/colorls)
* [catpix](https://github.com/pazdera/catpix)
* [artii](https://github.com/miketierney/artii)

#### Lire plus de [ryanwhocodes](https://www.freecodecamp.org/news/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7/undefined)

* [Rendez votre terminal plus coloré et productif avec iTerm2 et Zsh !](https://medium.com/the-code-review/make-your-terminal-more-colourful-and-productive-with-iterm2-and-zsh-11b91607b98c)
* [Powerlevel9k : personnalisez votre invite pour tout langage de programmation](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63)
* [Top 10 des commandes Bash du système de fichiers dont vous ne pouvez pas vous passer](https://medium.com/the-code-review/top-10-bash-file-system-commands-you-cant-live-without-4cd937bd7df1)
* [Comment vous pouvez ajouter Bootstrap à votre projet Ruby on Rails](https://medium.freecodecamp.org/add-bootstrap-to-your-ruby-on-rails-project-8d76d70d0e3b)