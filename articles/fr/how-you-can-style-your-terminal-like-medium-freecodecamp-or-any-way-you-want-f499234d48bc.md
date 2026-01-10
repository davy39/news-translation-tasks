---
title: Comment styliser votre terminal comme Medium, freeCodeCamp, ou de n'importe
  quelle manière que vous souhaitez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-13T20:28:29.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-style-your-terminal-like-medium-freecodecamp-or-any-way-you-want-f499234d48bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7eesI0V6YMEx6E67J2HBOQ.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment styliser votre terminal comme Medium, freeCodeCamp, ou de n'importe
  quelle manière que vous souhaitez
seo_desc: 'By ryanwhocodes

  Learn how to configure your own terminal theme using Powerlevel9k for Zsh and iTerm2!

  This tutorial will show you how to personalise your terminal design by configuring
  iTerm2 with Powerlevel9k. Powerlevel9k is a popular and highly cu...'
---

Par ryanwhocodes

**Apprenez à configurer votre propre thème de terminal en utilisant Powerlevel9k pour Zsh et iTerm2 !**

Ce tutoriel vous montrera comment personnaliser la conception de votre terminal en configurant iTerm2 avec [Powerlevel9k](https://github.com/bhilburn/powerlevel9k). Powerlevel9k est un thème de terminal populaire et hautement personnalisable pour le shell Zsh. Je vais expliquer comment le configurer avec des icônes de [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts), votre choix de [schéma de couleurs](https://iterm2colorschemes.com/), et vos propres sections de prompt personnalisées.

![Image](https://cdn-media-1.freecodecamp.org/images/ug6M6AJBYTzNKyyAfbUXPKGHg7BX9Ag4xZ3w)

Voici quelques façons possibles de styliser votre terminal, en utilisant des exemples de sections de prompt personnalisées basées sur Medium et freeCodeCamp :

![Image](https://cdn-media-1.freecodecamp.org/images/N7mfF0pbY0MNMReE3VmJeiOXRjmDnJ4ZfqzJ)

![Image](https://cdn-media-1.freecodecamp.org/images/DCLseVcFoHlgOfja7tDw1w4uDHKhGdfgcLf5)

![Image](https://cdn-media-1.freecodecamp.org/images/vhx-YfOYZ8Y4zGPibWdmS7lkUiGxSZ6RIp9p)
_Exemples de schémas de couleurs | Gauche : basé sur [Solarised Dark](https://design-style-guide.freecodecamp.org/" rel="noopener" target="_blank" title="">le guide de style de freeCodeCamp</a> | Centre : <a href="https://draculatheme.com/iterm" rel="noopener" target="_blank" title="">Dracula</a> | Droite : <a href="https://iterm2colorschemes.com/" rel="noopener" target="_blank" title="). Cliquez sur les images pour voir les captures d'écran en plus grand._

#### Tutoriel

* [Prérequis : installer Homebrew, iTerm2 et Zsh](#heading-installation)
* [Choisir et définir un schéma de couleurs](#heading-schema-couleurs)
* [Télécharger Nerd Fonts et configurer iTerm2 pour l'utiliser](#heading-nerd-fonts)
* [Ajouter le thème Powerlevel9k pour Zsh](#heading-powerlevel9k)
* [Personnaliser votre prompt](#heading-personnalisation)
* [Le fichier .zshrc complet](#heading-zshrc-complet)
* [Quelques options bonus à essayer](#heading-options-bonus)
* [En savoir plus](#heading-en-savoir-plus)

### Prérequis : installer Homebrew, iTerm2 et Zsh

* Si ce n'est pas déjà fait, installez le gestionnaire de paquets mac [**Homebrew**](https://docs.brew.sh/Installation.html).
* Installez le terminal **iTerm2** [ici](https://www.iterm2.com/downloads.html) ou via homebrew en utilisant `brew cask install iterm2`
* Ensuite, installez le shell [**Zsh**](http://www.zsh.org/) (une alternative à [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))) en utilisant `brew install zsh`
* Ouvrez iTerm2. Pour changer le shell par défaut en Zsh plutôt qu'en bash, exécutez la commande de changement de shell dans votre terminal. `chsh -s /bin/zsh`

Le fichier de ressources Zsh, `~/.zshrc`, est un script qui est exécuté chaque fois que vous démarrez Zsh. Ce tutoriel ajoutera des commandes et des variables à ce fichier pour configurer votre terminal.

### Choisir et définir un schéma de couleurs

Il existe de nombreux schémas de couleurs pour iTerm. Une source est [iterm2colorschemes](https://iterm2colorschemes.com/), qui vous offre environ 175 choix. Une fois que vous les avez téléchargés, sélectionnez `iTerm -> Préférences -> Profils -> Couleurs -> Préréglages de couleurs -> Importer` puis sélectionnez le schéma de couleurs que vous aimez, comme les thèmes Dracula et Solarised Dark illustrés en haut de cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/QtBxNWJHnkv5BYnG2c86mBlZaRf9bQlRoEty)
_Thème freeCodeCamp ajouté au logo original [Powerlevel9k](https://github.com/bhilburn/powerlevel9k" rel="noopener" target="_blank" title=")_

Vous pouvez également créer votre propre schéma de couleurs en définissant les couleurs ANSI selon vos préférences, puis cliquez sur Préréglages de couleurs → Exporter pour le sauvegarder.

Si vous êtes intéressé par la découverte du schéma de couleurs utilisé par freeCodeCamp pour sa marque, vous pouvez le consulter à l'adresse [design-style-guide.freecodecamp.org](https://design-style-guide.freecodecamp.org/).

### Télécharger Nerd Fonts et configurer iTerm2 pour l'utiliser

Pour pouvoir avoir un prompt avec des icônes de programmation supplémentaires, vous devez installer un ensemble de polices spécial. Cela vous montrera comment installer et configurer [nerd-fonts](https://github.com/ryanoasis/nerd-fonts#font-installation).

> _Nerd Fonts est un projet qui patch des polices ciblant les développeurs avec un grand nombre de glyphes (icônes). Plus précisément pour ajouter un grand nombre de glyphes supplémentaires provenant de polices iconiques populaires telles que [Font Awesome ↗](https://github.com/FortAwesome/Font-Awesome), [Devicons ↗](https://vorillaz.github.io/devicons/), [Octicons ↗](https://github.com/primer/octicons), et [d'autres](https://github.com/ryanoasis/nerd-fonts#glyph-sets)._  
>  _— [Nerd Fonts sur GitHub](https://github.com/ryanoasis/nerd-fonts)_

#### Télécharger Nerd Fonts avec curl

Il existe [plusieurs options pour installer Nerd Fonts](https://github.com/ryanoasis/nerd-fonts#font-installation). Voici [l'option pour installer en utilisant homebrew](https://github.com/ryanoasis/nerd-fonts#option-4-homebrew-fonts).

```
brew tap caskroom/fontsbrew cask install font-hack-nerd-font
```

Pour en savoir plus sur l'utilisation de Nerd Fonts en détail, consultez mon article :

[**Nerd Fonts : Comment installer, configurer et supprimer des polices de programmation sur un mac**](https://medium.com/the-code-review/nerd-fonts-how-to-install-configure-and-remove-programming-fonts-on-a-mac-178833b9daf3)

![Image](https://cdn-media-1.freecodecamp.org/images/QC7uMM0W2ijqY9xIeZ2B6NMa6zCvtC8I20y6)

#### Configurer iTerm2 avec Nerd Fonts

Ensuite, configurez **iTerm2** pour utiliser la police en allant à :

```
iTerm2 -> Préférences -> Profils -> Texte -> Police -> Changer la police
```

![Image](https://cdn-media-1.freecodecamp.org/images/mAHoFMzKIMhIOnlZZ0Y6o0SmHfCVimuavG69)

Sélectionnez la police **Hack Regular Nerd Font Complete** et ajustez la taille si vous le souhaitez. Cochez également la case pour `Utiliser une police différente pour le texte non-ASCII` et sélectionnez à nouveau la police. Elle devrait afficher la nouvelle police et les icônes dans le prompt.

![Image](https://cdn-media-1.freecodecamp.org/images/GBrkB7DoD-KWTvr6M-oP2zDwF5omEEiNmwbZ)
_Powerlevel9k : Le thème Powerline le plus génial pour ZSH ! [https://github.com/bhilburn/powerlevel9k](https://github.com/bhilburn/powerlevel9k" rel="noopener" target="_blank" title=")_

### Ajouter le thème Powerlevel9k pour Zsh

Mon thème préféré pour Zsh est [Powerlevel9k](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#step-1-install-powerlevel9k). Il style votre prompt avec des segments colorés pour différents usages et peut inclure les icônes de programmation Nerd Font.

#### Installation

Vous devez indiquer à Powerlevel9k d'utiliser les Nerd Fonts dans votre `~/.zshrc`.

```
echo "POWERLEVEL9K_MODE='nerdfont-complete'" >> ~/.zshrc
```

Ensuite, installez le thème Powerleve9k depuis [GitHub](https://github.com/bhilburn/powerlevel9k) et ajoutez la commande pour le charger au démarrage de Zsh.

```
git clone https://github.com/bhilburn/powerlevel9k.git ~/powerlevel9kecho 'source  ~/powerlevel9k/powerlevel9k.zsh-theme' >> ~/.zshrc
```

**Note** : La police doit être définie avant l'initialisation de Powerlevel9k pour pouvoir l'utiliser. Si vous ouvrez votre `~/.zshrc`, il devrait avoir les commandes dans cet ordre.

```
POWERLEVEL9K_MODE='nerdfont-complete'source ~/powerlevel9k/powerlevel9k.zsh-theme
```

Powerlevel9k est hautement configurable. Par exemple, vous pouvez ajuster l'espacement et les segments de prompt — et ceux-ci ont diverses options également.

### Personnaliser votre prompt

#### Configurer les éléments et la disposition du prompt

Powerlevel9k est livré avec certains segments de prompt préconfigurés, que vous pouvez simplement ajouter à une variable d'environnement pour les utiliser. Ceux-ci couvrent de nombreux aspects différents de l'utilisation de votre terminal, du système de contrôle de version (par exemple git), et certains outils de développement logiciel, tels que pour Node.js et Ruby.

Pour changer votre configuration, ouvrez votre `~/.zshrc` et ajoutez la [configuration](https://github.com/bhilburn/powerlevel9k#prompt-customization) que vous préférez. Il est considéré comme une bonne pratique de déclarer toute la configuration avant d'appeler le script du thème Powerlevel9k. Voici un exemple de configuration de base, qui est listée dans mon `~/.zshrc`.

```
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir vcs newline status)POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()POWERLEVEL9K_PROMPT_ADD_NEWLINE=truePOWERLEVEL9K_MODE='nerdfont-complete'
```

```
source ~/powerlevel9k/powerlevel9k.zsh-theme
```

Les principales choses personnalisées ici sont les segments pour le prompt de gauche où il y a :

* Le répertoire de travail
* Le système de contrôle de version (qui affiche le statut git et la branche)
* Une nouvelle ligne
* Le code de retour de la commande précédente

Un prompt de droite est également disponible, mais je n'aime pas l'utiliser. La dernière option est d'ajouter une nouvelle ligne après chaque exécution de commande.

**Ensuite, je vais vous montrer comment créer vos propres sections de prompt personnalisées.**

![Image](https://cdn-media-1.freecodecamp.org/images/Z6LjqgHnlR2hDMj-ISRMzVWRYvGysw7H9DGj)
_Powerlevel9k vous permet d'ajouter vos propres sections de prompt qui incluent des icônes, du texte et des choix de couleurs de fond et de premier plan. Vous pourriez donc, par exemple, créer une section basée sur le style de freeCodeCamp._

#### Créer des segments de prompt personnalisés

Dans la capture d'écran en haut de l'article, j'ai montré l'icône Medium ainsi qu'un segment freeCodeCamp. Cette partie du tutoriel expliquera en détail comment ceux-ci ont été configurés et comment vous pouvez personnaliser vos propres sections de prompt.

**C'est une opportunité d'être vraiment créatif.** Vous pourriez concevoir quelque chose lié au code, comme [le langage de programmation que vous utilisez](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63), ou quelque chose de complètement différent !

Powerlevel9k vous permet d'ajouter facilement des segments de prompt personnalisés en les ajoutant à certaines variables d'environnement. Il doit suivre la syntaxe ci-dessous, où ils sont préfixés par « custom ». Voici la configuration pour les éléments personnalisés Medium et freeCodeCamp utilisés dans les captures d'écran du terminal en haut de cet article.

```
# Personnaliser les prompts Powerlevel9kPOWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(  custom_medium custom_freecodecamp dir vcs newline status)POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()POWERLEVEL9K_PROMPT_ADD_NEWLINE=true
```

```
# Ajouter le segment de prompt personnalisé de l'icône Medium MPOWERLEVEL9K_CUSTOM_MEDIUM="echo -n '\uF859'"POWERLEVEL9K_CUSTOM_MEDIUM_FOREGROUND="black"POWERLEVEL9K_CUSTOM_MEDIUM_BACKGROUND="white"
```

```
# Ajouter le segment de prompt personnalisé freeCodeCampPOWERLEVEL9K_CUSTOM_FREECODECAMP="echo -n \u2019'\uE242' freeCodeCamp"POWERLEVEL9K_CUSTOM_FREECODECAMP_FOREGROUND="white"POWERLEVEL9K_CUSTOM_FREECODECAMP_BACKGROUND="cyan"
```

#### Définir les noms de variables pour une section de prompt personnalisée

Powerlevel9k inclut du code pour créer dynamiquement des éléments de prompt basés sur des variables d'environnement. Suivez cette structure pour ajouter votre propre section de prompt personnalisée.

→ Ajoutez `custom_<NOM DE VOTRE SECTION DE PROMPT>` à POWERLEVEL9K_LEFT_PROMPT_ELEMENTS ou POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS

→ Définissez une couleur pour `POWERLEVEL9K_CUSTOM_<NOM DE VOTRE SECTION DE PROMPT>_FOREGROUND`

→ Définissez une couleur pour `POWERLEVEL9K_CUSTOM_<NOM DE VOTRE SECTION DE PROMPT>_BACKGROUND`

→ Définissez l'icône et le texte pour le contenu de la section définie à `POWERLEVEL9K_CUSTOM_<NOM DE VOTRE SECTION DE PROMPT>`

#### Ajouter votre propre choix d'icône Nerd Font et de texte

Ce qui suit imprime le code associé à l'icône Nerd Font — vous pouvez les parcourir sur le [site web de Nerd Fonts](http://nerdfonts.com/#cheat-sheet).

```
POWERLEVEL9K_CUSTOM_FREECODECAMP="echo -n \u2019'\uE242' freeCodeCamp"
```

Remplacez simplement les 4 caractères après `\u` par le code de l'icône que vous souhaitez utiliser. Suivez l'icône avec votre choix de texte.

L'option `-n` pour la commande `echo` indique à Zsh de ne pas sortir le caractère de nouvelle ligne à la fin de la chaîne, ce qui maintient les segments de prompt sur la même ligne.

#### Définir les couleurs de fond et de premier plan

Celles-ci définissent des séquences d'échappement ANSI pour utiliser certaines couleurs, ce qui explique pourquoi vous pourriez vouloir définir une couleur différente pour le vert de freeCodeCamp, par exemple « cyan », pour le différencier du vert utilisé à d'autres fins dans le terminal.

> **Les séquences d'échappement ANSI** sont une norme pour [la signalisation en bande](https://en.wikipedia.org/wiki/In-band_signaling) pour contrôler l'emplacement du curseur, la couleur et d'autres options sur les [terminaux texte](https://en.wikipedia.org/wiki/Text_terminal). Certaines séquences d'[octets](https://en.wikipedia.org/wiki/Byte), commençant principalement par [Esc](https://en.wikipedia.org/wiki/Escape_character) et « [[](https://en.wikipedia.org/wiki/Bracket) », sont intégrées dans le texte, que le terminal recherche et interprète comme des commandes, et non comme des [codes de caractères](https://en.wikipedia.org/wiki/Character_encoding).  
>  
— [ANSI Escape Code | Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)

#### Sections de prompt de langage de programmation

Une autre idée pour les sections de prompt est de les baser sur un langage de programmation que vous utilisez. Pour en savoir plus sur la création de celles-ci pour des langages tels que JavaScript, Python et Ruby, consultez [Powerlevel9k : personnalisez votre prompt pour n'importe quel langage de programmation](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63).

![Image](https://cdn-media-1.freecodecamp.org/images/Gy9iZlkWW8Zrs8O52ekrveRqN1KQU64bfhWA)

### Le fichier .zshrc complet

Voici la configuration complète pour `~/.zshrc` après avoir suivi ce tutoriel. Vous pouvez l'utiliser comme base pour créer votre configuration personnalisée.

```
# Personnaliser les prompts Powerlevel9kPOWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(  custom_medium custom_freecodecamp dir vcs newline status)POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()POWERLEVEL9K_PROMPT_ADD_NEWLINE=true
```

```
# Ajouter le segment de prompt personnalisé de l'icône Medium MPOWERLEVEL9K_CUSTOM_MEDIUM="echo -n $'\uF859'"POWERLEVEL9K_CUSTOM_MEDIUM_FOREGROUND="black"POWERLEVEL9K_CUSTOM_MEDIUM_BACKGROUND="white"
```

```
# Ajouter le segment de prompt personnalisé freeCodeCampPOWERLEVEL9K_CUSTOM_FREECODECAMP="echo -n $'\uE242' freeCodeCamp"POWERLEVEL9K_CUSTOM_FREECODECAMP_FOREGROUND="white"POWERLEVEL9K_CUSTOM_FREECODECAMP_BACKGROUND="cyan"
```

```
# Charger Nerd Fonts avec le thème Powerlevel9k pour ZshPOWERLEVEL9K_MODE='nerdfont-complete'
```

```
source ~/powerlevel9k/powerlevel9k.zsh-theme
```

### Quelques options bonus à essayer

Vous pouvez également ajouter ceci à votre .zshrc pour configurer le texte et la couleur de fond du titre de l'onglet iTerm2.

```
# Définir une couleur pour le fond du titre de l'onglet iTerm2 en utilisant des valeurs rgbfunction title_background_color {  echo -ne "\033]6;1;bg;red;brightness;$ITERM2_TITLE_BACKGROUND_RED\a"  echo -ne "\033]6;1;bg;green;brightness;$ITERM2_TITLE_BACKGROUND_GREEN\a"  echo -ne "\033]6;1;bg;blue;brightness;$ITERM2_TITLE_BACKGROUND_BLUE\a"}
```

```
ITERM2_TITLE_BACKGROUND_RED="18"ITERM2_TITLE_BACKGROUND_GREEN="26"ITERM2_TITLE_BACKGROUND_BLUE="33"
```

```
title_background_color
```

```
# Définir le texte du titre de l'onglet iTerm2function title_text {    echo -ne "\033]0;"$*"\007"}
```

```
title_text freeCodeCamp
```

Ci-dessous se trouve un terminal stylisé avec le schéma de couleurs [Dracula](https://draculatheme.com/iterm/), le [segment de prompt Powerlevel9k chruby](https://github.com/bhilburn/powerlevel9k#chruby) pour afficher la version de Ruby, ainsi que [les gems Ruby artii, lolcat et colorls pour ajouter plus de sortie colorée au terminal](https://medium.freecodecamp.org/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7) — juste quelques-unes des autres idées possibles à essayer.

![Image](https://cdn-media-1.freecodecamp.org/images/beh2vvFJN-yUmHhMfpCj3WtlcnlI8vTDzj4L)

### En savoir plus

Il existe de nombreuses autres options que vous pouvez consulter sur la page Powerlevel9k pour [Styliser Votre Prompt](https://github.com/bhilburn/powerlevel9k/wiki/Stylizing-Your-Prompt). Pour plus d'informations sur les segments de prompt personnalisés, consultez [Powerlevel9k : Commande Personnalisée](https://github.com/bhilburn/powerlevel9k#custom_command).

Si vous êtes fier de votre configuration, certaines personnes partagent la leur en ligne, par exemple sur [Show-Off-Your-Config](https://github.com/bhilburn/powerlevel9k/wiki/Show-Off-Your-Config).

**_Vous avez changé d'avis ?_** Vous pouvez toujours supprimer ce thème et revenir aux paramètres par défaut. Consultez ce guide qui explique comment faire cela étape par étape.

* [Retour à Bash : Supprimer Zsh et les thèmes de terminal sur un Mac étape par étape](https://medium.com/the-code-review/back-to-bash-remove-zsh-and-terminal-themes-on-a-mac-step-by-step-f89f69d2ec73)

#### Lire plus de [ryanwhocodes](https://www.freecodecamp.org/news/how-you-can-style-your-terminal-like-medium-freecodecamp-or-any-way-you-want-f499234d48bc/undefined)

* [Powerlevel9k : personnalisez votre prompt pour n'importe quel langage de programmation](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63)
* [Nerd Fonts : Comment installer, configurer et supprimer des polices de programmation sur un mac](https://medium.com/the-code-review/nerd-fonts-how-to-install-configure-and-remove-programming-fonts-on-a-mac-178833b9daf3)
* [Lolcat, Colorls, Catpix, et autres Ruby Gems pour ajouter de la couleur à votre terminal](https://medium.freecodecamp.org/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7)
* [Top 10 des commandes Bash du système de fichiers dont vous ne pouvez pas vous passer](https://medium.com/@RyanDavidson/top-10-bash-file-system-commands-you-cant-live-without-4cd937bd7df1)