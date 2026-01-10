---
title: Voici quelques astuces super secrètes pour VS Code afin d'augmenter votre productivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T22:17:21.000Z'
originalURL: https://freecodecamp.org/news/here-are-some-super-secret-vs-code-hacks-to-boost-your-productivity-20d30197ac76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Cda3VjoZXXl2KjDWhL-a-g.jpeg
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Voici quelques astuces super secrètes pour VS Code afin d'augmenter votre
  productivité
seo_desc: 'By Dylan Tientcheu

  Coding as a hobbyist, professional or even a once-in-a-month developer, you must
  know that having smart and sharp tools is vital to anyone willing to put in maximum
  productive hours while working.

  I’ve curated a little collection o...'
---

Par Dylan Tientcheu

Que vous codiez en tant qu'amateur, professionnel ou même développeur occasionnel, vous devez savoir qu'avoir des outils intelligents et performants est vital pour quiconque souhaite mettre un maximum d'heures productives dans son travail.

J'ai compilé une petite collection de conseils, astuces et extensions, et je les ai filtrés pour ne garder que les plus rares et les plus utiles pour un développeur web moderne. Comme nous le savons, l'écosystème JavaScript est très grand et continue de croître. Pour cette raison, j'essaierai d'être aussi impartial que possible.

Les conseils suivants pour Visual Studio Code vous aideront à terminer toutes vos sessions de codage en ayant l'air comme ceci :

### Le rendre beau et convivial

> S'il est vraiment beau et convivial, vous aimerez le temps passé avec lui.

#### [1. Thème Material](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme) & [Icônes](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)

C'est tout simplement le meilleur des thèmes VS Code. Je pense que le thème Material est ce qui se rapproche le plus de l'écriture avec un stylo et du papier dans l'éditeur (surtout lorsque vous utilisez le thème **variant sans contraste**). Votre éditeur semble presque plat et sans couture, passant des outils intégrés à l'éditeur de texte.

Imaginez un thème épique couplé à des icônes épiques. Les [**Material Theme Icons**](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) sont une alternative géniale pour remplacer les icônes par défaut de VSCode. Le grand catalogue d'icônes conçu s'intègre parfaitement avec le thème, le rendant encore plus beau. Cela vous aidera à trouver vos fichiers facilement dans l'explorateur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*k5PE7vEkF_9KA7oS.jpg)
_[https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme" rel="noopener" target="_blank" title=")_

#### 2. Mode Zen avec disposition centrée

Vous connaissez peut-être déjà la vue Mode Zen, également connue sous le nom de vue sans distraction (pour ceux qui viennent de Sublime Text), où tout (sauf le code) est supprimé pour vous donner une véritable intimité avec votre éditeur de code. Saviez-vous que vous pouviez centrer la disposition pour vous aider à lire votre code comme si vous étiez dans un visualiseur PDF ? Cela vous aidera vraiment à vous concentrer sur une fonction ou à étudier le code de quelqu'un d'autre.

**Mode Zen** : _[Affichage > Apparence > Basculer en mode Zen]

**Disposition centrée** : _[Affichage > Apparence > Basculer en disposition centrée]

![Image](https://cdn-media-1.freecodecamp.org/images/1*rOEqs2r32WNvXKRDRNw9qQ.gif)

#### **3. Polices avec ligatures**

Le style d'écriture rend la lecture facile et agréable. Vous pouvez rendre votre éditeur plus beau avec des polices géniales ainsi que des [ligatures](https://en.wikipedia.org/wiki/Typographic_ligature). Voici [6 des meilleures polices qui supportent les ligatures](https://www.slant.co/topics/5611/~monospace-programming-fonts-with-ligatures) (selon [www.slant.co](http://www.slant.co/))

![Image](https://cdn-media-1.freecodecamp.org/images/1*marIy0tF9nshab3_ugN6VA.gif)
_Codage avec des ligatures_

Vous pouvez essayer [Fira Code](https://github.com/tonsky/FiraCode), c'est tout simplement génial et open source. Voici comment changer la police dans VSCode après l'avoir installée.

```
"editor.fontFamily": "Fira Code","editor.fontLigatures": true
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0qjQY2qb5rJVPRILebhkxg.png)
_Source : [https://github.com/tonsky/FiraCode/blob/master/showcases/all_ligatures.png](https://github.com/tonsky/FiraCode/blob/master/showcases/all_ligatures.png" rel="noopener" target="_blank" title=")_

_La célèbre police Operator Mono ne prend pas en charge les ligatures de manière native. Cependant, si vous êtes un grand fan de ligatures, vous pouvez les ajouter en utilisant [cette bibliothèque](https://github.com/kiliman/operator-mono-lig)._

#### 4. [Rainbow Indent](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)

Indentez avec style. Cette extension colorise l'indentation devant votre texte en alternant quatre couleurs différentes à chaque étape.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dSKbn4xbVxEGPdIrnyApjA.png)
_**Rainbow Indent : [https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow" rel="noopener" target="_blank" title=""></a>**<a href="https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow" rel="noopener" target="_blank" title=")_

Le paramètre d'indentation par défaut colorise l'indentation en suivant un schéma arc-en-ciel. J'ai cependant personnalisé le mien pour suivre différentes nuances de gris. Si vous souhaitez que le vôtre ressemble à cet exemple, copiez et collez le fragment suivant dans votre `settings.json`

```
"indentRainbow.colors": [
```

```
"rgba(16,16,16,0.1)",
```

```
"rgba(16,16,16,0.2)",
```

```
"rgba(16,16,16,0.3)",
```

```
"rgba(16,16,16,0.4)",
```

```
"rgba(16,16,16,0.5)",
```

```
"rgba(16,16,16,0.6)",
```

```
"rgba(16,16,16,0.7)",
```

```
"rgba(16,16,16,0.8)",
```

```
"rgba(16,16,16,0.9)",
```

```
"rgba(16,16,16,1.0)"
```

```
],
```

#### 5. Personnalisation de la barre de titre

C'est un excellent ajustement visuel. Je l'ai copié de [Wes Bos](https://www.freecodecamp.org/news/here-are-some-super-secret-vs-code-hacks-to-boost-your-productivity-20d30197ac76/undefined) dans l'une de ses [leçons sur React & GraphQL](https://advancedreact.com/). Basiquement, il a changé les couleurs de la barre de titre sur différents projets pour les reconnaître facilement et aider le public à les distinguer également. Cela est vraiment utile si vous travaillez sur des applications qui peuvent avoir le même code ou les mêmes noms de fichiers, par exemple, une application mobile react-native et une application web react.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cG_nfe-R1aHDk-e_whFP7w.png)

Cela se fait en modifiant les paramètres de la barre de titre dans les **Paramètres de l'espace de travail** pour chaque projet dans lequel vous souhaitez des couleurs de barre de titre différentes.

### Codage plus rapide

> _L'essence même de le faire à temps_

#### 1. Enveloppement de balises

Si vous ne connaissez pas [Emmet](https://emmet.io/), alors vous êtes probablement quelqu'un qui aime tout taper. Emmet vous permet de taper un code abrégé et d'obtenir les balises correspondantes. Cela se fait en sélectionnant un ensemble de code et en tapant la commande **Envelopper avec l'abréviation** que j'ai liée à `shift+alt+.`

Regardez ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*27AU7hj5uEkYaPofK_BAUQ.gif)
_Enveloppez-le avec Emmet_

Imaginez que vous souhaitez envelopper tout cela mais en tant que lignes individuelles. Vous utiliseriez **_envelopper avec des lignes individuelles_** puis insérez * après l'abréviation, par exemple `div*`

Au cas où vous souhaiteriez vous lancer directement dans Emmet, voici le [Emmet Cheatsheet](https://docs.emmet.io/cheat-sheet/)

#### 2. Équilibrage vers l'intérieur et l'extérieur

Ce conseil a été pris sur [https://vscodecandothat.com/](https://vscodecandothat.com/) que je recommande vraiment.

Vous pouvez sélectionner une balise entière dans VS Code en utilisant les commandes Emmet `balance inward` et `balance outward`. Il est utile de lier ces commandes à des raccourcis clavier, comme `Ctrl + Shift + Flèche Haut` pour Balance Outward et `Ctrl + Shift + Flèche Bas` pour Balance Inward.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WdH9CosNx91ggCI9u246cA.gif)
_Équilibrage vers l'intérieur/l'extérieur_

#### 3. [Turbo Console.log()](https://marketplace.visualstudio.com/items?itemName=ChakrounAnas.turbo-console-log)

Personne n'aime taper de très longues instructions comme console.log(). Cela peut être vraiment irritant, surtout lorsque vous voulez simplement sortir quelque chose très rapidement, voir sa valeur, puis continuer à coder. Et si je vous disais que vous pourriez journaliser n'importe quoi aussi vite que Lucky Luke ?

Cela se fait avec une extension appelée [Turbo Console Log](https://marketplace.visualstudio.com/items?itemName=ChakrounAnas.turbo-console-log). Elle permet la journalisation de toute variable sur la ligne suivante avec un préfixage automatique suivant la structure du code. Vous êtes également en mesure de décommenter/commenter `alt+shift+u/ alt+shift+c` tous les console.log() ajoutés par cette extension.

De plus, vous pouvez également les supprimer tous avec `alt+shift+d` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C7BQj-qOFfkuvWC4Cg94bQ.gif)
_Journalisation de la console comme Lucky Luke_

#### 4. [Live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

C'est une extension géniale qui vous aide à lancer un serveur de développement local avec une fonction de rechargement en direct pour les pages statiques et dynamiques. Il offre un excellent support pour les principales fonctionnalités comme : HTTPS, CORS, adresses localhost personnalisées et port.

[Téléchargez-le ici](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CfYU3dAoc-39eAJf2hgb3A.gif)
_Source ([https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer" rel="noopener" target="_blank" title="))_

Il peut même vous permettre de partager votre localhost, s'il est utilisé avec [VSCode LiveShare](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare).

#### 5. Copier/Coller avec plusieurs curseurs

L'un des premiers "Wows" que j'ai criés en utilisant VS Code est survenu lorsque j'ai édité plusieurs lignes en ajoutant des curseurs sur différentes lignes. Longtemps après, j'ai trouvé une très bonne utilisation à cette fonctionnalité. Vous êtes en mesure de copier et coller le contenu sélectionné par ces curseurs et ils seront collés exactement dans l'ordre dans lequel ils ont été copiés.

Vérifiez ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NPW3X6Z5eugYHUp1AQ3-aw.gif)
_Copier et coller avec différents curseurs_

#### 6. Fil d'Ariane et Contours

Le Fil d'Ariane montre l'emplacement actuel et vous permet de naviguer rapidement entre les symboles et les fichiers. Pour commencer à utiliser le Fil d'Ariane, activez-le avec la commande Affichage > Basculer le Fil d'Ariane ou via le paramètre `breadcrumbs.enabled`.

La Vue Contour est une section séparée en bas de l'arborescence de l'explorateur de fichiers. Lorsqu'elle est développée, elle affichera l'arborescence des symboles de l'éditeur actuellement actif.

La vue Contour dispose de différents modes de tri, d'un suivi optionnel du curseur. Elle comprend également une zone de saisie qui filtre les symboles au fur et à mesure que vous tapez. Les erreurs et avertissements sont également affichés dans la vue Contour, vous permettant de voir d'un coup d'œil l'emplacement d'un problème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BPo_JXR94vivyMJLyI0TiQ.gif)
_Relation entre le Fil d'Ariane et le Contour_

### Divers

> _Ces petits ajustements qui changent tout_

#### 1. CLI de Code

VS Code dispose d'une interface de ligne de commande puissante qui vous permet de contrôler la manière dont vous lancez l'éditeur. Vous pouvez ouvrir des fichiers, installer des extensions, changer la langue d'affichage et sortir des diagnostics via des options de ligne de commande (commutateurs).

![Image](https://cdn-media-1.freecodecamp.org/images/1*KhG5u8EYn-aMlqwomhZq_w.png)

Imaginez que vous venez de faire un `git clone <repo-url>` d'un dépôt et que vous souhaitez remplacer l'instance actuelle de VS Code que vous utilisez. `code . -r` fera l'affaire sans que vous ayez à quitter l'interface CLI ([En savoir plus ici](https://code.visualstudio.com/docs/editor/command-line)).

#### 2. [Polacode](https://github.com/octref/polacode)

Vous tombez souvent sur des captures d'écran de code attrayantes avec des polices et des thèmes personnalisés comme celle ci-dessous. Cela a été pris dans VS Code avec l'[Extension Polacode](https://github.com/octref/polacode)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AF2kH-Hc5cR_RdSpfKFrlg.png)

Je sais que [Carbon](https://carbon.now.sh/) est également une bonne alternative et plus personnalisable. Cependant, Polacode vous permet de rester dans votre éditeur de code et d'utiliser n'importe quelle police propriétaire que vous avez achetée et qui est inutilisable dans Carbon.

#### 3. [Quokka (JS/TS ScratchPad)](https://quokkajs.com/)

Quokka est un terrain de jeu de prototypage rapide pour JavaScript et TypeScript. Il exécute votre code immédiatement au fur et à mesure que vous tapez et affiche divers résultats d'exécution et journaux de console dans votre éditeur de code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Es15d1InicXO5JxBmVAskA.gif)

Un cas d'utilisation génial pour Quokka est lorsque vous étudiez pour des entretiens techniques, vous êtes en mesure de sortir chaque étape sans avoir le stress de définir des points d'arrêt dans les débogueurs.

Il peut également vous aider à étudier les fonctions d'une bibliothèque comme Lodash ou MomentJS avant de les utiliser réellement. Il fonctionne même pour les appels asynchrones.

#### 5. [WakaTime](https://wakatime.com/)

Vos amis pensent-ils que vous passez trop de temps à coder ? Enregistrez-le et montrez-leur que 10 heures par jour n'est pas "trop". [WakaTime](https://wakatime.com/) est une extension qui aide à enregistrer et stocker des métriques et des analyses concernant votre activité de programmation.

Vous pouvez définir des objectifs, voir les langages de codage que vous utilisez souvent, vous pouvez même vous comparer à d'autres ninjas dans le monde.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bvNk2yHjrObBPeBP6otd5w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_GHqrHKRWUEmf33nIdzEVg.png)
_Tableau de bord et classements WakaTime_

#### 6. [VSCode Hacker Typer](https://marketplace.visualstudio.com/items?itemName=jevakallio.vscode-hacker-typer)

Avez-vous déjà tapé du code devant une foule ? Vous tapez souvent de manière imprudente et parlez en tapant, ce qui vous confond un peu. Imaginez un code pré-tapé qui n'apparaît que lorsque vous simulez la frappe comme dans [geektyper](http://geektyper.com/tegnio/).

[Jani Eväkallio](https://www.freecodecamp.org/news/here-are-some-super-secret-vs-code-hacks-to-boost-your-productivity-20d30197ac76/undefined) a apporté à VS Code [**cette extension**](https://marketplace.visualstudio.com/items?itemName=jevakallio.vscode-hacker-typer). Elle vous aidera à enregistrer et rejouer des macros (code écrit dans votre éditeur), vous rendant 100 % plus concentré lorsque vous tapez devant un public.

#### 7. Exclure des dossiers

J'ai appris cette astuce [sur un post StackOverFlow](https://stackoverflow.com/questions/33258543/how-can-i-exclude-a-directory-from-visual-studio-code-explore-tab/33277809#33277809). C'est un ajustement rapide pour exclure des dossiers comme node_modules ou tout autre de l'arborescence de l'explorateur pour vous aider à vous concentrer uniquement sur ce qui compte. Pour ma part, je déteste vraiment ouvrir le fastidieux dossier node_module dans mon éditeur, alors j'ai décidé de le cacher.

Par exemple, pour cacher node_modules, vous pouvez faire ceci :

1. Allez dans **Fichier > Préférences > Paramètres** (ou sur Mac **Code > Préférences > Paramètres**)
2. Recherchez `files.exclude` dans les paramètres
3. Sélectionnez ajouter un motif et tapez `**/node_modules`
4. Voila ! node_modules a disparu de l'arborescence de l'explorateur

#### 8. [Vos suggestions]

Vous pouvez toujours commenter certains de vos conseils les plus secrets sur VSCode, je serai ravi de les ajouter à la liste pour aider les autres. :)

J'espère que ces conseils augmenteront vraiment votre productivité avec VS Code. Veuillez applaudir et partager le post si vous l'avez aimé et commenter si j'ai oublié une extension.

[**Dylan Tientcheu (@DylanTientcheu) | Twitter**](http://twitter.com/dylantientcheu)  
[_Dylan Tientcheu(@DylanTientcheu). Javascript 热爱者 * #Developer & #Designer * Technical Writer *…_twitter.com](http://twitter.com/dylantientcheu)