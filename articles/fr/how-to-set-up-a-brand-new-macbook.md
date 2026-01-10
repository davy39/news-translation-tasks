---
title: Comment configurer votre nouveau MacBook pour le codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-03T13:30:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-brand-new-macbook
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/spring-2019-25.jpg
tags:
- name: Computers
  slug: computers
- name: Productivity
  slug: productivity
seo_title: Comment configurer votre nouveau MacBook pour le codage
seo_desc: 'By Amber Wilkie

  I started a new job on Monday (it''s going awesome, thanks for asking) and that
  means a brand new, blank-slate MacBook Pro. Fortunately, I still have my old work
  computer (my last job maybe wasn''t so wonderful, as I had to bring my own...'
---

Par Amber Wilkie

J'ai commencé un nouveau travail lundi (c'est génial, merci de demander) et cela signifie un tout nouveau MacBook Pro vierge. Heureusement, j'ai toujours mon ancien ordinateur de travail (mon dernier emploi n'était peut-être pas si merveilleux, car je devais apporter le mien tous les jours...). Mais la prochaine fois, je devrai probablement rendre mon nouvel ordinateur de travail, alors je voulais créer un enregistrement de ma configuration. Peut-être que cela sera utile pour les autres aussi ! Au fait, presque tous ces programmes sont G-R-A-T-U-I-T-S.

# Le Terminal

Il est absolument essentiel de configurer votre terminal pour pouvoir travailler efficacement. Si vous utilisez le terminal par défaut sans aucun ajustement, ces conseils pourraient vous faire économiser beaucoup de temps et de frustration.

## iTerm2

Allez-y et téléchargez [iTerm2](https://iterm2.com/) puis soyez très satisfait de toutes les fonctionnalités. Mes préférées sont :

* Faites défiler (touches fléchées) vers le haut et vers le bas pour parcourir les commandes. Tapez des commandes partielles pour filtrer, puis faites défiler.
* Auto-copie - il suffit de surligner le texte dans iTerm et il sera automatiquement copié dans le presse-papiers.

## oh my zsh

Si vous, comme moi, voulez faire en sorte que votre terminal travaille pour vous, procurez-vous [oh my zsh](https://github.com/robbyrussell/oh-my-zsh). Voici à quoi ressemble mon invite de terminal :

![démo de configuration oh-my-zsh](https://www.freecodecamp.org/news/content/images/2019/08/iterm-demo.png)
_démo zsh dans le terminal_

Lorsque j'ai des changements non validés, j'obtiens un x jaune à gauche de mon curseur. C'est vraiment pratique pour reconnaître que j'ai des changements en attente.

Vous pouvez faire beaucoup de choses avec oh my zsh - il y a une bibliothèque de différentes façons de styliser votre terminal. J'utilise le thème "robbyrussel". Notez que vous voudrez également utiliser `.zshrc` au lieu de `.bashrc` pour les alias et autres modifications des paramètres du terminal.

Tant que nous y sommes, donnons un énorme coup de projecteur aux alias de terminal. J'adore le langage "insider" que j'ai avec mon terminal. En voici quelques-uns que je mets dans `.zshrc`. Je n'ai plus besoin de tous, mais je les ai laissés ici pour montrer quelques-unes des commandes ridiculement longues qui peuvent être aliasées en quelque chose de très court.

```
alias j-u='jest --updateSnapshot'
alias ytu='yarn test-update'
alias dcu='docker-compose up'
alias dcd='docker-compose down'
alias lint-front='docker-compose exec front yarn gulp lint'
alias back-bash='docker-compose exec back bash'

```

## .gitconfig

Vous avez probablement un `.gitconfig` sur votre ordinateur, mais vous n'utilisez peut-être pas les alias git pour vous économiser quelques frappes. Le mien est le suivant :

```
# Ce fichier est le fichier de configuration par utilisateur de Git.
[user]
    name = amberwilkie
    email = amber@amberwilkie.com
[alias]
    co = checkout
    st = status
    ci = commit
    lp = log --oneline
    poh = push origin head
    rc = rebase --continue
    prom = pull --rebase origin master

```

Sous cet en-tête `[alias]`, vous pouvez mettre ce que vous voulez, y compris des commandes git compliquées particulières à votre organisation. C'est super pratique.

## .gitignore_global

Saviez-vous que vous pouvez automatiquement ignorer des fichiers dans _tous les dépôts git_ de votre ordinateur ? Mettez-les dans `.gitignore_global` et vous n'aurez plus jamais à vous soucier de `.DS_Store` dans votre `.gitignore`. J'y ai également mis `.idea`, car mon éditeur de choix génère des profils dans chaque dépôt.

## Clés SSH Github

Nouvel ordinateur, nouvelles clés SSH. Suivez les [instructions de Github](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) pour ne plus avoir à taper vos identifiants.

## Trash

Avez-vous déjà pensé que `rm -rf folder` était un peu trop définitif ? Avec ce simple [package npm Trash](https://github.com/sindresorhus/trash), vous pouvez appeler `trash file/folder` pour le déplacer littéralement dans la corbeille de votre ordinateur au lieu de le supprimer de la mémoire. Il peut être restauré ou autrement géré. Cela m'a sauvé plusieurs fois.

Conseil pro : Exécutez toujours `rm -rf node_modules` au lieu de `trash node_modules` (vous n'aurez jamais besoin de restaurer votre ancien `node_modules`).

## Homebrew & Cask

Si vous avez un Mac, vous savez déjà que vous avez besoin de [Homebrew](https://brew.sh/) et [Cask](https://github.com/Homebrew/homebrew-cask). Le premier pour installer des packages, le second pour les applications distribuées en binaire.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install cask

```

# Programmes

Mon éditeur de choix est Webstorm, bien que j'essaie de créer un flux de travail avec VS Code en ce moment. Je vais sauter toutes les choses liées à l'éditeur, car elles sont bien couvertes dans de nombreux autres endroits. Voici le reste de ce que j'installe dès le premier jour.

## TimeOut

[TimeOut](https://www.dejal.com/timeout/) bloque votre écran à intervalles réguliers, vous forçant à faire une pause. Je garde le mien à 2 minutes toutes les heures et 15 secondes toutes les 15 minutes. Cela peut devenir ennuyeux, mais c'est bon pour ma santé. Nous savons que rester assis pendant de longues périodes est mauvais pour nous, mais il est beaucoup trop facile de laisser passer quatre heures alors que nous corrigeons simplement ce petit problème. Heureusement, ma pause est apparue pendant que j'écrivais ce paragraphe. (Normalement, l'image et le minuteur sont alignés, je ne sais pas ce qui se passe.)

![démo du générateur de pause timeout](https://www.freecodecamp.org/news/content/images/2019/08/timeout.png)
_TimeOut en cours d'exécution sur un Mac_

Vous pouvez définir l'image pour qu'elle soit ce que vous voulez et ajouter du texte.

## gitx

J'adorerais installer [gitx](http://gitx.frim.nl/) car je l'utilisais abondamment sur mon ancien ordinateur. Malheureusement, il n'est plus maintenu ! J'ai expérimenté avec d'autres interfaces utilisateur git, mais aucune ne répond encore à mes besoins. Davantage d'investigation est nécessaire. Si vous avez une version plus ancienne de Mac, vous pourriez peut-être mettre la main sur cet outil original et extrêmement utile. Et si vous pouvez écrire nativement, envisagez de contribuer !
GitX est extrêmement utile pour examiner rapidement les changements dans votre commit actuel et modifier ces changements.

## Alfred

Je installe toujours Alfred, bien que je n'aie pas encore pris le temps de tomber amoureux. Je suis consciente qu'il y a mille fonctionnalités que les développeurs utilisent tous les jours. C'est sur ma liste d'améliorations de productivité à découvrir ! Je suis susceptible d'acheter le power pack pour pouvoir accéder au presse-papiers amélioré, qui semble génial.

![Alfred presse-papiers](https://www.alfredapp.com/help/features/clipboard/clipboard-viewer.png)

J'utilisais [Clipy](https://github.com/Clipy/Clipy) auparavant, mais l'aperçu visuel de ce que vous allez coller semble incroyablement utile.

Mais quoi que vous fassiez, procurez-vous une extension de presse-papiers ! N'avoir qu'un seul emplacement de presse-papiers est impossible. Combien de fois avez-vous dû aller et venir entre les choses en copiant et collant ? Avoir un meilleur gestionnaire de presse-papiers a considérablement amélioré mon efficacité en tant que développeur.

## Spectacle

[Ce programme](https://www.spectacleapp.com/) vous permet de faire glisser des fenêtres vers diverses parties de l'écran. Mon nouveau lieu de travail m'a fourni un écran 4k génial, mais ce truc est si énorme que, lorsque je le branche, mes fenêtres flottent dans un océan de bureau. Spectacle me permet de les faire glisser là où elles appartiennent avec des raccourcis clavier. Magique !

## Giphy Capture

Cela peut sembler idiot, mais en tant que développeur web qui travaille sur le front-end (parfois), je me retrouve souvent à devoir créer de courts gifs pour expliquer les fonctionnalités. [Giphy Capture](https://giphy.com/apps/giphycapture) est le meilleur outil que j'ai trouvé pour cela - il est intuitif et fait tout ce dont vous avez besoin.

Et c'est tout ce que je considère comme essentiel pour commencer à travailler en tant que développeur web sur un Mac ! Naturellement, mille autres programmes suivent, selon les besoins, mais ce sont les paramètres et les programmes que je trouve indispensables pour commencer. Si vous avez des conseils sur d'autres outils de productivité qui pourraient être utiles, j'adorerais les entendre.

_Cet article est initialement paru sur [wilkie.tech](https://wilkie.tech/tech/set-up-a-new-computer/). Ce serait génial de discuter sur Twitter. Je suis [@heyamberwilkie](https://twitter.com/heyamberwilkie)._