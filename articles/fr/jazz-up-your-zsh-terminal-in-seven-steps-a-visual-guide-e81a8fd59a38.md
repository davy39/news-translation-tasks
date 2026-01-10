---
title: Embellissez votre terminal "ZSH" en sept étapes — Un guide visuel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T06:42:49.000Z'
originalURL: https://freecodecamp.org/news/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sk54-oKGwIS_3BRk1S4N7A.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: terminal
  slug: terminal
- name: Web Development
  slug: web-development
- name: zsh
  slug: zsh
seo_title: Embellissez votre terminal "ZSH" en sept étapes — Un guide visuel
seo_desc: 'By rajaraodv

  In this blog I’ll cover installing ITerm2, ZSH shell, “oh my ZSH”, Themes, ITerm2
  color schemes, “oh my ZSH” plugins and enable “ligature” support to help create
  a beautiful and powerful Terminal.


  If you want to just make your regular B...'
---

Par rajaraodv

Dans ce blog, je vais couvrir l'installation d'ITerm2, du shell ZSH, de "Oh My ZSH", des thèmes, des schémas de couleurs ITerm2, des plugins "Oh My ZSH" et activer la prise en charge des "ligatures" pour aider à créer un terminal à la fois beau et puissant.

> Si vous souhaitez simplement rendre votre terminal Bash régulier plus puissant, consultez mon précédent blog : "[Embellissez votre terminal Bash](https://medium.com/@rajaraodv/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22)". Mais le ZSH expliqué dans ce blog est encore plus puissant.

#### Résumé :

Nous allons couvrir beaucoup de choses. Cela peut être déroutant, alors voici un résumé de ce que nous allons faire.

1. Installer ITerm2 — C'est une meilleure alternative au Terminal par défaut
2. Installer le dernier shell ZSH — Il est plus puissant que le shell bash régulier. Nous allons configurer ITerm2 pour utiliser le shell ZSH.
3. Installer "Oh My ZSH" — C'est un outil CLI pour configurer facilement ZSH et ajouter des thèmes et des plugins à ZSH
4. Ajouter deux types de thèmes en utilisant "Oh My ZSH" — certains thèmes nécessitent des étapes supplémentaires, nous allons donc couvrir les deux
5. Installer différents schémas de couleurs ITerm2 — Ce sont simplement des schémas de couleurs pour l'interface utilisateur
6. Ajouter deux plugins différents en utilisant "Oh My ZSH" pour améliorer la productivité
7. Activer la prise en charge des "ligatures" pour que lorsque vous écrivez une flèche **=>**, elle apparaisse comme une vraie flèche [1;35m→[0m

![Image](https://cdn-media-1.freecodecamp.org/images/1*k3akUSSgJsBjjzMkAAN9tQ.gif)

### Étape 1 — Installer ITerm2

Beaucoup de programmeurs préfèrent [ITerm2](https://www.iterm2.com) au Terminal par défaut. Il est similaire au Terminal, mais possède de nombreuses fonctionnalités propres. Il peut bien sûr exécuter ZSH, Bash et d'autres shells.

La vidéo suivante montre certaines des nouvelles fonctionnalités d'ITerm2 (v3).

> Pour ce blog, nous utiliserons ITerm2. Lorsque je mentionne "Terminal", je veux dire ITerm2. Bien que les étapes soient les mêmes pour Terminal et ITerm2.

### Étape 2 — Changer le shell pour ZSH

La vidéo suivante montre pourquoi ZSH est meilleur qu'un simple shell bash.

**Option 1 — Utiliser le ZSH intégré de Mac :**

Mac est livré avec ZSH intégré, donc nous n'avons pas besoin de l'installer. Cependant, parfois c'est une version plus ancienne de ZSH. Typiquement, il est situé à /bin/zsh. Pour l'utiliser, tout ce que nous avons à faire est de changer de shell (chsh).

1. Ouvrez le Terminal (ou ITerm2) et tapez la commande suivante.

```bash
$ chsh -s $(which zsh)
```

2. Entrez le mot de passe et il changera le shell, après la déconnexion et la reconnexion.

3. **Déconnectez-vous et reconnectez-vous**

4. Pour tester, ouvrez le Terminal et tapez ce qui suit, et il devrait dire zsh.

```bash
$ echo $0
zsh //devrait retourner zsh
```

**Option 2 — Installer Homebrew et installer le dernier ZSH via Homebrew**

Cette option est assez courante parmi les utilisateurs, car certains plugins ne fonctionnent qu'avec le dernier ZSH.

Homebrew, simplement dit, est un installeur en ligne de commande pour tous types de logiciels. Installons cela d'abord.

1. Installez Homebrew en exécutant la commande suivante.

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. Si vous obtenez une erreur concernant les outils de ligne de commande pour Xcode, cela signifie que vous n'avez pas installé les outils CLI pour Xcode. *Si vous n'obtenez pas l'erreur, vous pouvez ignorer cette étape, car vous les avez déjà installés.*

Les outils de développement CLI de Xcode sont utilisés par diverses applications qui manipulent les fonctionnalités principales d'OSX. Assurez-vous donc d'installer les outils CLI de Xcode en exécutant la commande suivante.

`$ xcode-select —install`

> Note : La commande ci-dessus ouvre l'installeur de Mac et installe les outils de développement CLI de Xcode. Si cela ne fonctionne pas, essayez `_xcode-select -r_` pour réinitialiser.

3. Installez ZSH via Homebrew

Exécutez la commande suivante pour installer ZSH. Il est installé à `/usr/local/bin/zsh` PS : Le ZSH par défaut de Mac est à `/bin/zsh`

```bash
brew install zsh
```

4. Utilisez la version Homebrew de ZSH

Exécutez la commande suivante. Vous serez invité à entrer le mot de passe de Mac.

```bash
chsh -s /usr/local/bin/zsh
```

**5. Déconnectez-vous et reconnectez-vous.**

6. Testez si nous utilisons ZSH et le bon ZSH

```bash
$ echo $0
zsh   //correct

$ which zsh
/usr/local/bin/zsh   //correct
```

### Étape 3 — "Oh My ZSH"

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sk54-oKGwIS_3BRk1S4N7A.png)

"Oh My ZSH" est un plugin qui s'exécute sur ZSH. Il fournit une configuration par défaut pour ZSH (fichier ~/.zshrc) et offre également des thèmes et plus de fonctionnalités.

> D'après ce que je sais, la plupart des utilisateurs avancés qui utilisent ZSH utilisent également "Oh My ZSH".

1. **Installer "Oh My ZSH"**

Exécutez la commande suivante pour installer "Oh My ZSH".

```bash
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*9X_r8cgGVOIwS8PiPZnS7A.png)
_Oh My ZSH est installé_

2. Fermez et quittez ITerm2 et rouvrez-le.

Il devrait ressembler à quelque chose comme ci-dessous. Remarquez que l'invite a changé et que le thème est un peu différent — C'est "Oh My ZSH" en action pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Ot5gJq4R_iCXJqlkDPGow.png)
_Thème initial Oh My ZSH_

### Étape 4 — Changer les thèmes et installer les polices

Dans cette étape, nous allons ajouter deux thèmes différents "Oh My ZSH". "Oh My ZSH" est livré avec [des tonnes de thèmes](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes). *PS : Mais certains thèmes nécessitent des étapes supplémentaires comme l'installation de polices spécifiques, etc.*

Pour définir un thème, il suffit d'ouvrir le fichier ~/.zshrc (créé par "Oh My ZSH") et de changer le thème comme indiqué ci-dessous.

> PS : .zshrc est le fichier de configuration pour le shell ZSH. Les personnes qui n'utilisent pas "Oh My ZSH" devront créer manuellement ce fichier et ajouter elles-mêmes les configurations. "Oh My ZSH" crée automatiquement ce fichier s'il n'existe pas, puis ajoute son propre ensemble de configurations dans ce fichier.

#### Thème 1 — Ajoutons un thème appelé "Avit"

1. Ouvrez .zshrc

```bash
$ open ~/.zshrc
```

2. Changez le thème en "Avit"

Vous pouvez parcourir tous les thèmes "Oh My ZSH" [ici](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes). Pour changer le thème, il suffit de changer la valeur ZSH_THEME dans le fichier ~/.zshrc de **robbyrussell** à **Avit**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yzCfQpf-7oVs3SPelf1Imw.png)

3. Mettez à jour la configuration ZSH

Exécutez la commande suivante pour mettre à jour la configuration.

```bash
$ source ~/.zshrc
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*jdA_I2AykgRqAKTRVSY3Eg.png)
_Votre invite de commande dans le thème Avit_

4. Changez la couleur de fond et la taille de la police

Ouvrez ITerm2 > Préférences > Profils > Couleurs et changez la couleur noire de fond pour utiliser 20% de gris comme indiqué ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NjFS-nVNi0O8lDSoHLUleg.png)
_Utilisez un fond gris à 20%_

Ensuite, ouvrez Texte > Changer la police et modifiez la taille à 14pt.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8rl1Nc5oqqtd7RSjzo8K4w.png)
_Changer la police à 14pt_

![Image](https://cdn-media-1.freecodecamp.org/images/1*CjzxD0L9jyqK0bp5zLB8lg.png)
_Un Iterm2 propre et beau avec ZSH !_

OK, installons un thème différent qui nécessite des polices.

#### Thème 2 — Installation du thème "agnoster" Oh My ZSH

C'est un thème populaire car il émule l'application Python [Powerline](https://powerline.readthedocs.io/en/latest/overview.html#screenshots) qui améliore le terminal. L'image suivante montre à quoi il ressemble. Mais ce thème nécessite également que nous installions les thèmes Powerline.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vLlx2GBxwk1NAOa-eLOCyw.png)
_thème agnoster Oh My ZSH_

**1. Installez les [polices Powerline](https://github.com/powerline/fonts.git)**

```bash
$ git clone https://github.com/powerline/fonts.git
$ cd fonts
$ ./install.sh
```

**2. Changez le thème en "agnoster"**

```bash
$ open ~/.zshrc
Définissez ZSH_THEME="agnoster" et enregistrez le fichier
```

**3. Quittez ITerm2 et rouvrez-le.**

**4. Définissez la police Powerline**

Vous pouvez définir n'importe quelle police patchée Powerline que vous aimez. Toutes les polices se terminent par **"for Powerline"**.

Ouvrez `ITerm2 > Préférences > Profils > Texte > Changer la police` et définissez-la sur quelque chose qui contient "for Powerline". Je choisis la police **"Meslo LG DZ for Powerline"**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S9KIZotQcq4dNoBESM0v3w.png)
_**Police Meslo LG DZ for Powerline Iterm2**_

> Note — Si vous êtes confus au sujet des polices et des thèmes : les thèmes sont pour "Oh My ZSH" et le shell ZSH et les polices sont pour Iterm2 lui-même.

#### 5. Tout est fait

À ce stade, votre Terminal devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vLlx2GBxwk1NAOa-eLOCyw.png)

### Étape 5 — Installer les "schémas de couleurs" iTerm2 (Thèmes ITerm2)

Il existe de nombreux schémas de couleurs magnifiques pour iTerm2. Ces schémas changent la couleur de premier plan, la couleur de fond, la couleur du curseur, etc. Vous pouvez les trouver dans le dépôt Github [iTerm2-color-schemes](https://github.com/mbadolato/iTerm2-Color-Schemes).

> Note : Ce sont simplement des schémas de couleurs de l'interface utilisateur ITerm2 et ils ne traitent pas de l'apparence de l'invite de commande comme les thèmes de "Oh My ZSH" (autre que le simple changement de couleurs).

Suivez ces étapes pour les installer.

1. Téléchargez le [iTerm2-color-schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) sous forme de fichier zip et extrayez-le
2. Le dossier "Schemes" contient tous les fichiers de schémas de couleurs — ils se terminent par `.itermcolors`
3. Ouvrez `iTerm2 > Préférences > Profil > Couleurs > Préréglages de couleurs > Importer`
4. Dans la fenêtre d'importation, accédez au dossier "Schemes" (de l'étape 2)
5. Sélectionnez tous les fichiers afin de pouvoir importer tous les schémas de couleurs en une seule fois
6. Sélectionnez simplement le schéma de couleurs que vous préférez.

> Mes préférés sont **Batman** et **Argonaut**

![Image](https://cdn-media-1.freecodecamp.org/images/1*LHZaKiNSSp5PX0RRTS5ITw.png)
_Thème Iterm2 Batman_

Le schéma de couleurs Argonaut ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yFbKJQbBwNRbtU4dFM2UVA.png)
_schéma de couleurs Argonaut_

### Étape 6 — Installer les plugins

Les plugins ajoutent plus de fonctionnalités à votre flux de travail. Par défaut, "Oh My ZSH" a déjà le plugin "git" ! et c'est pourquoi vous avez pu voir tous ces statuts Git dans les invites des captures d'écran précédentes. Ajoutons-en un autre pour voir comment cela fonctionne.

> Note : Dans cette section, nous installerons deux plugins différents pour montrer comment ils fonctionnent.

#### Plugin 1 — Ajouter le plugin de surlignage syntaxique

Le plugin de surlignage syntaxique ajoute de belles couleurs aux commandes que vous tapez comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f_RqoUuzWvcVhATPzr2i7A.png)

1. Clonez le dépôt du plugin zsh-syntax-highlighting et copiez-le dans le répertoire des plugins "Oh My ZSH".

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

2. Activez le plugin dans `~/.zshrc` en ajoutant `zsh-syntax-highlighting` à la section Plugins comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1sGebsi0qMQMAvPLo64ARQ.png)
_Ajoutez un nouveau plugin dans une nouvelle ligne à l'intérieur de la section plugins_

3. Relisez la configuration zshrc

```bash
source ~/.zshrc
```

#### Plugin 2 — Ajouter le plugin ZSH-AutoSuggestion

Ce plugin suggère automatiquement l'une des commandes précédentes. Très pratique ! **Pour sélectionner la complétion, appuyez simplement sur la touche [1;35m→[0m.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZiTrbBVUGLWe4OwRL1Ytrg.gif)

1. Installez le plugin

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

> PS : ZSH_CUSTOM pointe vers ~/.oh-my-zsh/custom

2. Ouvrez `~/.zshrc` et ajoutez zsh-autosuggestions

![Image](https://cdn-media-1.freecodecamp.org/images/1*pshPBacVfZgHaKdlG1cajg.png)

### Étape 7 — Utiliser la prise en charge des ligatures

Il existe diverses polices qui aident à rendre les opérateurs comme inférieur à, double égal, flèche droite, non égal, etc., plus beaux. Par exemple, chaque fois que vous tapez : =>, il devient : [1;35m→[0m.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OIpApVPLobonxDMEkaAbaA.png)

Pour utiliser cela, nous avons besoin de polices qui supportent les ligatures. Nous devons également l'activer dans ITerm2. [FiraCode](https://github.com/tonsky/FiraCode) est une telle police. Suivez les étapes pour installer et activer les ligatures.

1. Téléchargez le dépôt [FiraCode](https://github.com/tonsky/FiraCode) et extrayez le fichier zip (ou clonez-le)
2. Ouvrez le dossier `dstr > ttf` et double-cliquez sur tous les fichiers `*.ttf` et sélectionnez le bouton "Installer la police" pour installer chaque variation de police.
3. Accédez à `ITerm2 | Préférences | Profils | Texte`
4. **Sélectionnez** la case à cocher **Utiliser les ligatures**
5. Cliquez sur `Changer la police` et sélectionnez la police `Fira Code Regular`

![Image](https://cdn-media-1.freecodecamp.org/images/1*kFynRP_J2Q42WA5TGtPphA.png)

### Résumé

Nous avons couvert beaucoup de choses dans ce blog, en commençant par l'installation du dernier ZSH via Homebrew, Oh My ZSH, les plugins, les thèmes, l'activation des "ligatures" pour la police FiraCode.

?? Merci !

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissement ? ci-dessous plusieurs fois pour montrer votre soutien ! [1;35m⬇⬇⬇[0m ??

### Mes autres articles

[_https://medium.com/@rajaraodv/latest_](https://medium.com/@rajaraodv/latest)

#### ECMAScript 2015+

1. _[Découvrez ces conseils et astuces utiles d'ECMAScript 2015 (ES6)](https://www.freecodecamp.org/news/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377/)_
2. [_5 parties "mauvaises" de JavaScript qui sont corrigées dans ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
3. [_Est-ce que "Class" dans ES6 est la nouvelle partie "mauvaise" ?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### Améliorations du Terminal

1. _[Comment embellir votre Terminal — Un guide étape par étape avec des images](https://www.freecodecamp.org/news/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22/)_
2. _[Embellissez votre terminal "ZSH" en sept étapes — Un guide visuel](https://www.freecodecamp.org/news/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38/)_

#### WWW

1. _[Une histoire fascinante et désordonnée du Web et de JavaScript](https://www.freecodecamp.org/news/a-fascinating-and-messy-history-of-the-web-and-javascript-video-8978dc7bda75/)_

#### DOM Virtuel

1. [_Le fonctionnement interne du DOM Virtuel_](https://medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf)

#### Performance de React

1. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)
2. [_Utiliser Preact au lieu de React_](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c#.7fzp0lyo3)

#### Programmation Fonctionnelle

1. [_JavaScript est Turing Complete — Expliqué_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Programmation Fonctionnelle en JS — Avec des exemples pratiques (Partie 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Programmation Fonctionnelle en JS — Avec des exemples pratiques (Partie 2)_](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/)
4. [_Pourquoi Redux a besoin que les réducteurs soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)

#### WebPack

1. [_Webpack — Les parties déroutantes_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(sous le capot)_
3. [_HMR de Webpack et React-Hot-Loader — Le manuel manquant_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Pourquoi Draft.js et pourquoi vous devriez contribuer_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_Comment Draft.js représente les données de texte riche_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React et Redux :

1. [_Guide étape par étape pour construire des applications React Redux_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_Un guide pour construire une application React Redux CRUD_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(application de 3 pages)_
3. [_Utilisation des Middlewares dans les applications React Redux_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Ajout d'une validation de formulaire robuste aux applications React Redux_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Sécurisation des applications React Redux avec des jetons JWT_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Gestion des e-mails transactionnels dans les applications React Redux_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_L'anatomie d'une application React Redux_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)
8. [_Pourquoi Redux a besoin que les réducteurs soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)
9. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissement ? ci-dessous plusieurs fois pour montrer votre soutien ! [1;35m⬇⬇⬇[0m ??

Si vous avez des questions, n'hésitez pas à me demander sur Twitter : [https://twitter.com/rajaraodv](https://twitter.com/rajaraodv)