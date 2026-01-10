---
title: Comment personnaliser votre terminal Bash — Un guide étape par étape avec des
  images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T17:41:49.000Z'
originalURL: https://freecodecamp.org/news/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QRJ9_60oCmcwRGfYqCbqSw.png
tags:
- name: Bash
  slug: bash
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
seo_title: Comment personnaliser votre terminal Bash — Un guide étape par étape avec
  des images
seo_desc: 'By rajaraodv

  In this blog I’ll go over the steps to add Themes, Powerline, fonts, and powerline-gitstatus
  to make your regular Bash Terminal look beautiful and useful as shown in the picture
  above.

  It turns out, if you are using Mac, you’ll need to j...'
---

Par rajaraodv

Dans ce blog, je vais passer en revue les étapes pour ajouter des thèmes, Powerline, des polices et powerline-gitstatus afin de rendre votre terminal Bash régulier beau et utile comme montré dans l'image ci-dessus.

Il s'avère que si vous utilisez un Mac, vous devrez sauter à travers de nombreux cerceaux pour que cela fonctionne, car de nombreuses instructions sont pour Linux ou sont obsolètes. J'ai donc pensé en bloguer - espérons que cela vous aidera.

> Notes :  
>   
> 1. Suivez les étapes avec soin car toute erreur causera beaucoup de maux de tête.  
>   
> 2. Ceci est pour MacOS et pour bash régulier dans Terminal.app. Je n'utilise pas ZSH ou Hyper dans ce blog — je prévois d'écrire différents blogs pour eux.  
>   
> 3. Mes versions : Mac High Sierra ; version git 2.14.3 (Apple Git-98) ; Python 2.7.10

D'accord, par défaut, lorsque vous avez un nouveau Mac, votre Terminal.app ressemblera à quelque chose comme ci-dessous. Allons-y et ajoutons des thèmes, des polices, et ainsi de suite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A2RjRAGXHeUQtIIy5XIBwQ.png)

### Étape 1 — Ajouter un nouveau thème

La première étape évidente est d'améliorer le thème. Terminal ne fournit pas tous les thèmes cool et fantaisistes que vous voyez d'autres développeurs utiliser. Téléchargeons un thème et ajoutons-le au Terminal.

Dans ce blog, j'ajouterai le thème Solarized-Dark à notre Terminal.

> Note : Vous pouvez télécharger divers thèmes (fichiers .terminal) depuis [ce dépôt git](https://github.com/lysyi3m/osx-terminal-themes/tree/master/schemes). Ouvrez simplement le fichier `_*.terminal_` pour l'installer, c'est-à-dire `_clic droit sur le fichier *.terminal > « ouvrir avec » > Terminal_.

1. Allez sur [http://ethanschoonover.com/solarized](http://ethanschoonover.com/solarized)
2. Faites défiler vers le bas et téléchargez le thème (solarized.zip)
3. Extrayez le fichier solarized.zip
4. Ouvrez le dossier **osx-terminal.app-colors-solarized**. Ce dossier contient le thème pour le terminal.
5. Double-cliquez sur le fichier **« Solarized Dark ansi.terminal »** — C'est le fichier de thème spécifique pour Terminal.app. _Note : Si vous obtenez un avertissement indiquant que cela provient d'un développeur non identifié, cliquez avec le bouton droit sur le fichier et sélectionnez « Ouvrir avec » > Terminal._
6. À ce stade, vous avez installé le thème dans votre Terminal. Nous devons simplement en faire un thème par défaut.
7. Ouvrez Terminal > Préférences > Texte et sélectionnez le thème « Solarized Dark … » et cliquez sur « Par défaut ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*0hPqERUbwhdAXVQfdQih1A.png)

Désormais, votre Terminal devrait ressembler à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hvkwX_GZIXHQxuYY2987GQ.png)

### Étape 2 — Installer Powerline

Powerline est une application Python et est un plugin de ligne d'état pour vim, et fournit des lignes d'état et des invites pour plusieurs autres applications, y compris zsh, bash, tmux, IPython, Awesome et Qtile.

Il fait en sorte que l'invite du Terminal ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7SLVI9-_IBwEcmZpGaDvmw.png)

#### 2.1 Installer Python

Parce que Powerline est une application Python, nous devons avoir Python et une version appropriée de Python.

* MacOS est livré avec Python déjà installé. **Assurez-vous que la version de Python est 2.7.x en tapant** `python -V` dans le Terminal.
* Si ce n'est pas 2.7, installez [Homebrew](https://brew.sh/) qui nous permet d'installer divers logiciels depuis la CLI, en exécutant : `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* Exécutez `brew install python` pour installer la dernière version de Python via Homebrew

#### 2.2 Installer pip — Un gestionnaire de paquets pour Python (similaire à npm)

Installez pip en exécutant la commande suivante

`$ sudo easy_install pip`

#### 2.3 Installer les outils CLI de XCode Developer

Les outils CLI de XCode Developer sont utilisés par Powerline et d'autres applications qui manipulent les fonctionnalités principales d'OSX. Assurez-vous donc d'installer les outils CLI de XCode en exécutant la commande suivante.

`$ xcode-select —install`

> Note : La commande ci-dessus ouvre l'installateur de Mac et installe les outils CLI de XCode Developer. Si cela ne fonctionne pas, essayez `_xcode-select -r_` pour réinitialiser.

#### 2.4 Installer Powerline

Enfin, installez Powerline (version stable) via pip en exécutant la commande suivante.

```bash
$ pip install --user powerline-status
```

Si vous souhaitez installer la dernière branche de développement, utilisez :

```bash
$ pip install --user git+git://github.com/powerline/powerline  //dev
```

#### 2.5 Ajouter le démon Powerline à bash

Nous devons maintenant ajouter le démon Powerline à bash afin qu'il puisse surveiller l'invite du Terminal et apporter des modifications.

**2.5.1 Copier l'emplacement d'installation de Powerline**

Vous pouvez trouver l'emplacement de Powerline en exécutant ce qui suit : `pip show powerline-status` Copiez la valeur du champ `Location`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Hi5bB475XFf-Iu43tAFvA.png)

**2.5.2 Ajouter le démon avec un emplacement approprié à .bash_profile**

1. Assurez-vous d'avoir un fichier `.bash_profile` dans votre répertoire racine. Si ce n'est pas le cas, créez-en un en faisant : `cd ~ && touch ~/.bash_profile`

2. Ouvrez `.bash_profile` et ajoutez ce qui suit :

```bash
export PATH=$PATH:$HOME/Library/Python/2.7/bin
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /Users/rupa/Library/Python/2.7/lib/python/site-packages/powerline/bindings/bash/powerline.sh
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QY-1dEQtAn6SUOpgOTQcsg.png)
_Quelques détails sur bash_profile_

> _Note : L'emplacement /Users/rupa/Library/Python/2.7/lib/python/site-packages/ provient de l'étape précédente (2.5.1). Changez-le pour qu'il corresponde à l'emplacement de votre ordinateur._

**2.5.3. Redémarrer le Terminal**

Quittez complètement le Terminal s'il est ouvert (Terminal > Quitter Terminal). Et rouvrez-le.

> Vous devriez pouvoir simplement utiliser `_$ source ~/.bash_profile_` pour mettre à jour les paramètres. Mais j'ai obtenu un étrange message d'erreur `_powerline-config_` fichier est manquant ! Typiquement, vous obtenez cette erreur si vous n'avez pas $HOME/Library/Python/2.7/bin dans votre PATH.

**2.5.4 Votre nouveau Terminal**

Votre nouveau Terminal devrait ressembler à ceci. Il devrait utiliser le thème « Solarized Dark ansi » et devrait afficher Powerline dans l'invite de commande. Mais remarquez également qu'il y a des caractères « ? » ! Cela est dû au fait que Powerline utilise diverses icônes et polices qui ne sont pas disponibles par défaut. Nous devons donc installer les polices.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fVqgdIqo7AIw7EJdcHZZxw.png)

### Étape 3 — Installer les polices Powerline

Pour installer les polices Powerline, rendez-vous simplement sur [https://github.com/powerline/fonts](https://github.com/powerline/fonts). Vous y verrez un tas de dossiers. Chacun est une police, alias « polices patchées ».

> On les appelle « polices patchées » car des personnes ont pris des polices régulières et y ont ajouté/patché des icônes et polices spécifiques à Powerline.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sYBQZYzxe37bkmtBUw_Oww.png)

#### 3.1 Télécharger le dépôt entier et le décompresser

* Cliquez sur le bouton « Clone or download » et téléchargez le dépôt entier afin de pouvoir essayer diverses polices.
* Décompressez le fichier fonts-master.zip

#### 3.2 Installer quelques polices

Ouvrons le dossier des polices **Meslo dotted**. Il ressemblera à ceci. Vous verrez un tas de fichiers .ttf. Chacun d'eux est une police, mais certains sont des versions « bold » de la police, d'autres sont des versions « regular », etc.

Double-cliquez simplement sur le fichier .ttf et appuyez sur « Installer la police » pour installer la police sur votre ordinateur.

Pour notre cas, installons « Meslo LG L DZ Regular for Powerline.ttf » et « Meslo LG L DZ Italic for Powerline.ttf ». Cela ajoutera une version **regular** et une version **Italic** de la police **Meslo**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zmoF1ksmDJfRH0lGK00GKg.png)

#### 3.3 Sélectionner la police dans le thème du Terminal

Vous souvenez-vous que nous avons ajouté le thème « Solarized Dark » à l'étape 1 ? Celui-ci n'avait aucune police et MacOS avait une police par défaut. Tout ce que nous devons faire est de définir notre police **Meslo dotted** pour ce thème et c'est tout !

1. Ouvrez Terminal > Préférences > Texte
2. Sélectionnez le thème **Solarized Dark ansi**
3. Cliquez sur le bouton « Police » — Cela ouvre la boîte de dialogue « Polices »
4. Dans la boîte de dialogue « Polices », sélectionnez « Meslo LG L DZ for Powerline » dans la famille et sélectionnez également la taille de police 14 (pour qu'elle soit plus facile à lire).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SbKUVJxHJ_PR8yh2cbSESw.png)

#### 3.4 Redémarrer le Terminal

Quittez complètement le Terminal (Terminal > Quitter Terminal) puis rouvrez-le.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5pfC372U2Uz9Q5SQJSqKzA.png)

### Étape 4 — Ajouter des informations Git à l'invite

Afin d'afficher divers statuts Git à l'invite, nous devons installer [powerline-gitstatus](https://github.com/jaspernbrouwer/powerline-gitstatus). Il s'agit d'un simple module complémentaire à Powerline qui ajoute plusieurs couleurs et thèmes pour afficher diverses informations de statut git.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NKRx9-fVCZIiWKW_Tb0lhA.png)
_PS : Nous allons manipuler des fichiers dans les dossiers « color schemes » et « themes »_

#### 4.1 Installer powerline-gitstatus

```bash
pip install --user powerline-gitstatus
```

> Note : La commande « — user » est requise pour l'installer dans le profil de l'utilisateur.

#### 4.2 Ajouter les schémas de couleurs powerline-gitstatus à Powerline

4.2.1 Ouvrir le dossier suivant `colorschemes/shell/default.json`

```bash
${powerline-install-directory}/powerline/config_files/colorschemes/shell/default.json

//Par exemple:
/Users/rupa/Library/Python/2.7/lib/python/site-packages/powerline/config_files/colorschemes/shell/default.json
```

4.2.2 Ajouter les couleurs suivantes :

Comme mentionné dans le [readme](https://github.com/jaspernbrouwer/powerline-gitstatus#installation) de powerline-gitstatus. PS : Copiez simplement les couleurs à l'intérieur de « groups » puis ajoutez-les au default.json comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*shKgrO87LFrjoGMb2uOEVg.png)
_Cliquez pour zoomer_

Voici mon schéma de couleurs default.json (vous pouvez copier et coller ceci à la place) :

```json
{
	"name": "Schéma de couleurs par défaut pour les invites shell",
	"groups": {
		"hostname": {
			"fg": "brightyellow",
			"bg": "mediumorange",
			"attrs": []
		},
		"environment": {
			"fg": "white",
			"bg": "darkestgreen",
			"attrs": []
		},
		"mode": {
			"fg": "darkestgreen",
			"bg": "brightgreen",
			"attrs": ["bold"]
		},
		"attached_clients": {
			"fg": "white",
			"bg": "darkestgreen",
			"attrs": []
		},

		"gitstatus": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch_clean": {
			"fg": "green",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch_dirty": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch_detached": {
			"fg": "mediumpurple",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_tag": {
			"fg": "darkcyan",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_behind": {
			"fg": "gray10",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_ahead": {
			"fg": "gray10",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_staged": {
			"fg": "green",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_unmerged": {
			"fg": "brightred",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_changed": {
			"fg": "mediumorange",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_untracked": {
			"fg": "brightestorange",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_stashed": {
			"fg": "darkblue",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus:divider": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		}
	},
	"mode_translations": {
		"vicmd": {
			"groups": {
				"mode": {
					"fg": "darkestcyan",
					"bg": "white",
					"attrs": ["bold"]
				}
			}
		}
	}
}
```

#### 4.3 Activer le thème

4.3.1 Ouvrir le fichier default.json du thème

```bash
${powerline-install-directory}/powerline/config_files/themes/shell/default.json

//Par exemple:
/Users/rupa/Library/Python/2.7/lib/python/site-packages/powerline/config_files/themes/shell/default.json
```

4.3.2 Ajouter ce qui suit au default.json

```json
{
    "function": "powerline_gitstatus.gitstatus",
    "priority": 40
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QJIvX5hfNpUWZgoHTQ_nbQ.png)

Voici mon fichier default.json du thème Powerline (vous pouvez copier et coller ceci à la place) :

> Note : J'ai supprimé tout de la section « right » et également supprimé le « numéro de travail » (« jobnum ») pour garder les choses propres. Sinon, vous verrez un petit artefact sur le bord droit de l'invite.

```json
{
	"segments": {
		"left": [{
				"function": "powerline.segments.shell.mode"
			},
			{
				"function": "powerline.segments.common.net.hostname",
				"priority": 10
			},
			{
				"function": "powerline.segments.common.env.user",
				"priority": 30
			},
			{
				"function": "powerline.segments.shell.cwd",
				"priority": 10
			}, {
				"function": "powerline_gitstatus.gitstatus",
				"priority": 40
			}
		],
		"right": []
	}
}
```

#### 4.4 Redémarrer le démon

Enregistrez le fichier et exécutez ce qui suit : `_powerline-daemon —replace_` _dans le Terminal._

> **Note importante :** Chaque fois que vous apportez des modifications à la configuration de Powerline, en plus de redémarrer le Terminal, vous devrez également **redémarrer** **le démon pour voir les modifications reflétées** en exécutant : `_powerline-daemon —replace_`.

#### 4.5 Redémarrer le Terminal

Quittez le Terminal (Terminal > Quitter Terminal) et rouvrez-le.

À ce stade, nous avons terminé ! Ouah ! Si vous ouvrez le Terminal et naviguez vers un dépôt git, et que vous jouez un peu, cela devrait ressembler à ce qui suit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QRJ9_60oCmcwRGfYqCbqSw.png)

Voici à quoi cela ressemble avec le thème Solarized-Light :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8yii2h-RBMX3j5dtMagr2Q.png)

Voici à quoi cela ressemble avec le [thème Cobalt2](https://raw.githubusercontent.com/lysyi3m/osx-terminal-themes/master/schemes/Cobalt2.terminal) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hYHwy__bxYoA8cji8E3plQ.png)

?? Merci !

Si vous avez des questions, n'hésitez pas à me demander sur Twitter : [https://twitter.com/rajaraodv](https://twitter.com/rajaraodv)

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissements ? ci-dessous plusieurs fois pour montrer votre soutien ! f44ff44ff44f ??

### Mes autres articles

[_https://medium.com/@rajaraodv/latest_](https://medium.com/@rajaraodv/latest)

#### ECMAScript 2015+

1. _[Découvrez ces conseils et astuces utiles d'ECMAScript 2015 (ES6)](https://www.freecodecamp.org/news/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377/)_
2. [_5 parties "mauvaises" de JavaScript qui sont corrigées dans ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
3. [_Est-ce que "Class" dans ES6 est la nouvelle partie "mauvaise" ?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### Améliorations du Terminal

1. _[Comment personnaliser votre terminal Bash — Un guide étape par étape avec des images](https://www.freecodecamp.org/news/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22/)_
2. _[Personnalisez votre terminal "ZSH" en sept étapes — Un guide visuel](https://www.freecodecamp.org/news/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38/)_

#### WWW

1. _[Une histoire fascinante et désordonnée du Web et de JavaScript](https://www.freecodecamp.org/news/a-fascinating-and-messy-history-of-the-web-and-javascript-video-8978dc7bda75/)_

#### DOM virtuel

1. [_Fonctionnement interne du DOM virtuel_](https://medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf)

#### Performance de React

1. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)
2. [_Utiliser Preact au lieu de React_](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c#.7fzp0lyo3)

#### Programmation fonctionnelle

1. [_JavaScript est Turing Complete — Expliqué_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Programmation fonctionnelle en JS — Avec des exemples pratiques (Partie 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Programmation fonctionnelle en JS — Avec des exemples pratiques (Partie 2)_](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/)
4. [_Pourquoi Redux a besoin que les reducers soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)

#### WebPack

1. [_Webpack — Les parties confuses_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(sous le capot)_
3. [_Webpack's HMR et React-Hot-Loader — Le manuel manquant_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Pourquoi Draft.js et pourquoi vous devriez contribuer_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_Comment Draft.js représente les données de texte riche_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React et Redux :

1. [_Guide étape par étape pour construire des applications React Redux_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_Un guide pour construire une application CRUD React Redux_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(application de 3 pages)_
3. [_Utilisation des Middlewares dans les applications React Redux_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Ajout d'une validation de formulaire robuste aux applications React Redux_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Sécurisation des applications React Redux avec des jetons JWT_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Gestion des e-mails transactionnels dans les applications React Redux_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_L'anatomie d'une application React Redux_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)
8. [_Pourquoi Redux a besoin que les reducers soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)
9. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)

#### Si cela vous a été utile, veuillez le partager ! Merci !! ??