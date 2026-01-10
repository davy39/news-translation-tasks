---
title: 'Pourquoi j''adore Vim : ce sont les fonctionnalités méconnues qui le rendent
  si incroyable'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-22T01:41:40.000Z'
originalURL: https://freecodecamp.org/news/learn-linux-vim-basic-features-19134461ab85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*w9dLy2njrrkNUQVugpF-6g.jpeg
tags:
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: vim
  slug: vim
seo_title: 'Pourquoi j''adore Vim : ce sont les fonctionnalités méconnues qui le rendent
  si incroyable'
seo_desc: 'By Amit Kulkarni

  Since I started using Vim in 2016, I’ve discovered several lesser-known features
  that Vim offers out of the box without any plugins.

  Can you cover some basics before you start rambling about these new things?

  Oh sure! Before I copy p...'
---

Par Amit Kulkarni

Depuis que j'ai commencé à utiliser Vim en 2016, j'ai découvert plusieurs fonctionnalités méconnues que Vim offre dès la sortie de la boîte, sans aucun plugin.

#### Pouvez-vous couvrir quelques bases avant de commencer à parler de ces nouvelles choses ?

Oh bien sûr ! Avant de copier-coller quelques commandes depuis un aide-mémoire, je vais faire une supposition audacieuse : vous ne seriez pas en train de lire ceci si vous vouliez un aide-mémoire et que vous connaissiez déjà les bases de Vim.

Vous avez peut-être juste entendu dire que les distributions Linux sont livrées avec un éditeur de texte en ligne de commande par défaut appelé Vim, et vous souhaitez peut-être simplement l'essayer.

Alors, supposons que vous êtes complètement nouveau dans ce domaine et commençons par ce dont nous avons besoin comme bases (sans histoire/théorie ennuyeuse).

> NOTE : Si vous connaissez les bases, [cliquez ici pour les dépasser](#9b6b)

#### Quelle est votre approche ici par rapport à des tonnes d'autres articles sur Vim ?

La plupart des articles d'introduction sur Vim commencent par les modes de Vim, l'insertion, la sauvegarde et la sortie. Si vous êtes vraiment d'humeur à apprendre la théorie de manière parfaite, n'hésitez pas à lire ce qui vous aide dans [wikibooks](https://en.wikibooks.org/wiki/Learning_the_vi_Editor/Vim/Modes).

Il existe également de grands livres et articles qui vous disent qu'il y a une philosophie derrière la façon dont Vim fonctionne et que les commandes dans VI/Vim sont destinées à être combinées. Absolument vrai et je suis sûr que vous l'apprécierez une fois que vous serez habitué à l'éditeur et à la puissance qu'il fournit.

#### J'ai entendu des histoires drôles et vu des images drôles sur la courbe d'apprentissage de Vim. Est-ce vrai ? Est-ce vraiment si mauvais ?

Eh bien, les haters vont hater ? Cependant, selon moi, l'image qui donne une représentation assez correcte de Vim est :

![Image](https://cdn-media-1.freecodecamp.org/images/Le5-7y1AbXwwi-v8er3RHhUluWGEHseACWyJ)
_Courtoisie : [https://pascalprecht.github.io/2014/03/18/why-i-use-vim/](https://pascalprecht.github.io/2014/03/18/why-i-use-vim/" rel="noopener" target="_blank" title=")_

La majorité des articles sur Vim font référence à la courbe d'apprentissage comme un mur d'apprentissage, mais hé, il y a un côté positif : regardez de l'autre côté du mur !

Pour les débutants, c'est littéralement un mur puisqu'ils n'ont jamais fait quelque chose comme ça auparavant pour utiliser un éditeur en ligne de commande. Ce qui m'a le plus plu lorsque j'ai commencé en tant que débutant était l'ubiquité de Vim.

Connectez-vous à n'importe quelle machine (non-Windows) depuis n'importe quel terminal et vous pouvez littéralement obtenir un éditeur en tapant *vi* les yeux fermés. L'éditeur apparaîtra devant vous !

Une autre chose qui m'a plu est la possibilité de travailler sans souris et sans perdre de temps productif sur le pavé tactile ou à chercher une souris pour l'ordinateur portable.

Je sais, je sais, je peux vous entendre crier « Emacs ! Emacs ! » Je comprends. Mais une fois que j'ai été accro à Vim, je n'ai jamais vraiment eu d'intérêt pour emacs (peut-être à cause de l'installation requise). Donc, oui, emacs est aussi génial, je suppose. N'hésitez pas à sauter dans ce bateau avant de commencer à naviguer sur ce beau voyage avec VI(m).

#### Je viens d'ouvrir mon terminal et j'ai tapé **vi** puis j'ai appuyé sur la touche Entrée. Tout ce que je vois est un écran de bienvenue. Je ne peux pas taper et je ne sais pas comment en sortir. Êtes-vous sûr que c'est un éditeur puissant avec des capacités ?

100% sûr. Le comportement que vous venez de constater est le *mur* que nous avons vu plus tôt. Faites-moi confiance, VI(m) peut faire beaucoup d'autres choses. Il a juste ses propres façons de l'utiliser. Vous pouvez éditer des fichiers, ouvrir des onglets, diviser l'écran horizontalement ou verticalement, naviguer dans le système de fichiers, exécuter des commandes linux sans quitter votre fichier, déclencher des builds make depuis votre code source sans quitter le fichier, marquer des répertoires, encore mieux : marquer des lignes d'un fichier, trouver et remplacer des mots, bien sûr copier-coller et bien plus encore.

#### Oui ! Comme si c'était un gros problème pour un éditeur de supporter cela. Meh ! Tout le monde fait ça. Quel est le gros problème ?

Il n'y a pas de gros problème, le seul problème que je vois est la capacité de se concentrer sur votre fichier/code sans quitter le clavier. Vraiment, si vous n'avez pas de problème à utiliser une souris, alors allez-y et ouvrez votre MS Word/Éditeur GUI et faites toutes les éditions que vous souhaitez faire.

#### D'accord, mais sérieusement, pourquoi pas un IDE pour certains travaux ?

D'accord, donc vous êtes un développeur et vous avez eu un certain penchant/amour pour un IDE. Non, VI(m) n'est pas un remplacement pour votre IDE brillant. VI(m) n'a pas les capacités géniales prêtes à l'emploi de votre IDE. VI(m) est juste petit en taille (package et installation) par rapport aux IDEs volumineux et est disponible à utiliser sans aucune configuration et installations. Sérieusement, VI(m) n'est pas à la hauteur de certaines grandes choses que votre IDE fournit.

#### Assez parlé, montrez-moi les bases ?

Bien sûr, avant de commencer, gardez à l'esprit que tout utilisateur de Vim doit essentiellement gérer le mode commande et le mode insertion. Il n'y a pas d'échappatoire (littéralement, pas la touche Esc).

Disons que vous utilisez un éditeur et que vous voulez supprimer une longue fonction en langage C. Les étapes simples que vous faites sont : Positionnez votre curseur au début de la ligne, puis appuyez sur Maj + Flèche bas jusqu'à la fin ou utilisez la souris. Cette action que vous avez dû faire pour sélectionner ces lignes vous a obligé à *arrêter* de taper et à appuyer sur des touches. N'est-ce pas ? Ne me dites pas que vous tapiez quelque chose et que vous avez simultanément appuyé sur des touches pour sélectionner magiquement le corps de votre fonction.

> Soyez raisonnable. Vous avez arrêté de taper et fait le travail de sélection pour dire à votre éditeur que vous voulez faire quelque chose avec ce texte (copier/couper/gras/italique/quoi que ce soit).

Cette pause que vous avez prise est équivalente à être en mode commande dans VI(m). C'est le moment où vous dites à VI(m) que vous voulez faire certaines actions sur certaines lignes/mot/quoi que ce soit et que vous n'allez pas taper. Maintenant, VI(m) vous sort du mode insertion et vous êtes bloqué hors de la saisie de texte dans votre fichier. Évidemment, l'autre mode dans lequel vous pouvez réellement taper dans votre fichier est le mode insertion.

Au fait, si vous vous demandiez comment sélectionner le corps d'une fonction sans sélectionner de texte ou utiliser la souris, j'y parviens en plaçant le curseur sur les accolades ouvrantes et en utilisant les touches : `d%`

Oui, cela supprime le contenu du corps de votre fonction. Non, ce n'est pas une combinaison de touches bizarre à retenir ! `d` indique que vous voulez supprimer quelque chose. `%` va déplacer le curseur à la fin de l'accolade correspondante.

Maintenant que nous avons établi les modes de base, plongeons dans le VI(m) de base.

Si vous connaissez le nom du fichier que vous écrivez :

```bash
$ vi myfile.c
```

Si vous n'êtes pas sûr du nom du fichier et que vous voulez commencer à taper :

```bash
$ vi
```

Dès que vous ouvrez vi, vous serez en mode commande. Pour entrer en mode **i**nsertion, appuyez sur `i`. Tapez ce que vous voulez. Appuyez sur `Esc` pour revenir en mode commande. Maintenant, vous avez quelques options pour sortir selon la manière dont vous avez ouvert vi.

Si vous avez donné un nom de fichier : `:w` **é**crira ces changements en toute sécurité sur le disque. `:q` **q**uittera l'éditeur. Vous pouvez combiner ces actions avec : `:wq` et la touche `Return`

Si vous n'avez pas donné de nom de fichier : `:wq filename.c` **é**crira le contenu dans le fichier `filename.c` et **q**uittera l'éditeur. Si vous n'êtes pas intéressé par le texte que vous avez écrit et souhaitez sortir sans sauvegarder quoi que ce soit : `:q!` et vous êtes sorti ! Le `!` est requis à la fin pour dire : « Oui, je suis sûr de ne pas vouloir sauvegarder le contenu et je veux sortir de toute urgence »

[**[DEMO] Utilisation basique de vim**](https://asciinema.org/a/wLpVX8lUuaK5mfG4tyVCk61qD)  
[_Pour démarrer l'éditeur vim : Utilisez la commande vim sur le shell Pour commencer à éditer un fichier en utilisant vim, utilisez : vim filename_asciinema.org](https://asciinema.org/a/wLpVX8lUuaK5mfG4tyVCk61qD)

Vous y êtes ! Vous venez de créer, éditer et sauvegarder (ou peut-être pas) votre premier fichier vi. Félicitations ?

Comme je l'ai mentionné plus tôt, ceci n'est pas une introduction pour débutants à VI(m). Il existe de nombreux autres articles (je fournirai des références à la fin de l'article) pour commencer. J'ai juste inséré cette introduction pour que vous ne soyez pas déçu après être arrivé sur cette page et n'avoir rien trouvé à apprendre ?

> C'est la ligne où les débutants disent au revoir aux utilisateurs intermédiaires et se dirigent vers la section de référence pour plus d'articles d'introduction brillants.

Bienvenue aux utilisateurs intermédiaires. Voici quelques capacités cool de VI(m) dont je n'avais pas connaissance. Mais maintenant, je les utilise quotidiennement pour être plus productif.

Pour ceux d'entre vous qui préfèrent TL;DR :

* onglets
* sessions
* numéros de ligne (+ marques) et copier/coller
* plis
* indentation avec `=`
* insertion-complétion
* netrw
* splits/fenêtres
* `:!` et un peu sur `:make`

#### Onglets de Vim

#### Avez-vous mentionné les onglets dans Vim ? Je ne savais pas que cela existait !

Je sais, n'est-ce pas ! Une [page d'onglet](http://vimdoc.sourceforge.net/htmldoc/tabpage.html#tab-page-intro) est une page avec une ou plusieurs fenêtres avec une étiquette (aka onglet) en haut.

Si vous êtes intéressé à en savoir plus sur les fenêtres, les buffers, les pages d'onglets : [détails techniques](http://vimdoc.sourceforge.net/htmldoc/windows.html#windows-intro)

Jetez un coup d'œil :

![Image](https://cdn-media-1.freecodecamp.org/images/2iMvCsKGk8iMrERGtswmB-s59dhc6A5soBD0)

![Image](https://cdn-media-1.freecodecamp.org/images/ec7MggpObT5GhBjZS9-XtZ4bDzjj5SUxhtlj)

![Image](https://cdn-media-1.freecodecamp.org/images/Hvd4DnXCni865974XxISsJuQlkMVCAPclhxk)
_Onglets de Vim en action_

Étapes :

* Ouvrez Vim avec n'importe quel fichier ou juste Vim : `$ vim file1`
* Tapez le contenu du fichier et passez en mode commande (Appuyez sur `Esc`)
* `:tabedit file2`, ouvrira un nouvel onglet et vous emmènera éditer `file2`
* `:tabedit file3`, ouvrira un nouvel onglet et vous emmènera éditer `file3`
* Pour naviguer entre ces onglets, vous pouvez être en mode normal et taper : `gt` ou `gT` pour aller à l'onglet suivant ou précédent respectivement. Vous pouvez également naviguer vers un onglet d'index particulier (indexé à partir de 1) en utilisant `{i}gt` où, i est l'index de votre onglet. Exemple : `2gt` vous emmène au 2ème onglet
* Pour vous déplacer directement vers le premier onglet ou le dernier onglet, vous pouvez entrer ce qui suit en mode commande : `:tabfirst` ou `:tablast` pour le premier ou le dernier onglet respectivement. Pour aller et venir : `:tabn` pour l'onglet suivant et `:tabp` pour l'onglet précédent
* Vous pouvez lister tous les onglets ouverts en utilisant : `:tabs`
* Pour ouvrir plusieurs fichiers dans des onglets : `$ vim -p source.c source.h`
* Pour fermer un seul onglet : `:tabclose` et pour fermer tous les autres onglets sauf celui en cours : `:tabonly`. Utilisez le suffixe `!` pour ignorer les changements des fichiers non sauvegardés

[**[DEMO] Onglets dans VIM**](https://asciinema.org/a/ZMUyM27ZTc04yctzH7S9JyNLo)  
[_VIM supporte les onglets pour ouvrir plusieurs fichiers et travailler avec eux_asciinema.org](https://asciinema.org/a/ZMUyM27ZTc04yctzH7S9JyNLo)

Je pense que cette fonctionnalité nous permet d'économiser du temps en partageant le buffer entre les onglets et en nous permettant de copier-coller entre les onglets et de garder plusieurs sessions de différents ensembles d'onglets pour des catégories de travail. Exemple : Vous pouvez avoir un onglet terminal avec tous les onglets Vim des fichiers source C uniquement et vous pouvez avoir un autre onglet terminal avec tous les onglets Vim des fichiers d'en-tête (.h).

#### Les onglets offrent tant de commodité pour garder tous mes fichiers ouverts et y accéder quand je veux. Cependant, n'est-ce pas une corvée d'ouvrir tous les onglets chaque fois que je redémarre ou ferme et ouvre le terminal ?

Exact ! Nous aimons tous avoir nos propres sessions de travail dans lesquelles nous travaillons avec un ensemble de fichiers et aimerions que Vim restaure cette session d'onglets telle que nous l'avons laissée. 
Vim nous permet de sauvegarder et restaurer ces sessions d'onglets ! ✍️

Étapes :

* Ouvrez autant d'onglets que vous souhaitez utiliser
* Depuis n'importe quel onglet, appuyez sur `Esc` et entrez en mode commande
* Tapez `:mksession header-files-work.vim` et appuyez sur Entrée
* Votre session actuelle d'onglets ouverts sera stockée dans un fichier `header-files-work.vim`
* Pour voir la restauration en action, fermez tous les onglets et Vim
* Soit démarrez vim avec votre session en utilisant : `$ vim -S header-files-work.vim` ou ouvrez vim avec n'importe quel autre fichier et entrez en mode commande pour taper : `:source header-files-work.vim` et BOOM ! Tous vos onglets sont ouverts pour vous exactement comme vous les avez sauvegardés !
* Si vous changez des onglets de session (fermer/ouvrir de nouveaux), vous pouvez sauvegarder cela en utilisant : `:mks!` pendant que vous êtes dans la session

[**[DEMO] Sessions dans VIM**](https://asciinema.org/a/NLn3NjxfBavV4mnURQWF2GlUg)  
[_VIM permet aux utilisateurs de stocker leurs sessions de travail séparément en fonction des projets sur lesquels ils travaillent. Les utilisateurs peuvent facilement..._asciinema.org](https://asciinema.org/a/NLn3NjxfBavV4mnURQWF2GlUg)

#### Puis-je copier/couper coller sans avoir à connaître les numéros de ligne ?

Oh oui ! Auparavant, je regardais les numéros de ligne ( `:set nu` ) des fonctions que je voulais copier/couper. Disons que je veux copier/couper les lignes 34 à 65. J'utilisais `:34,65y` (Copier/**Y**ank) ou `:34,65d` (Couper/**D**elete).

> Bien sûr, compter les lignes et utiliser `{n}yy` ou `{n}dd` (où `n` est le nombre de lignes) n'est pas une option pour des centaines de lignes ?

Il peut y avoir des fonctions qui s'étendent sur plusieurs pages et vous ne voulez pas descendre seulement pour oublier quel était le premier numéro de ligne. Il y a un moyen simple d'y parvenir sans se soucier des numéros de ligne !

Étapes :

* Entrez en mode normal, allez à la ligne de début
* Tapez `mk` (Marquer le point avec l'alphabet 'k' ou utilisez une autre lettre)
* Descendez (page down ou autre) et allez à la ligne de fin
* `y'k` **y**ank/copiera toutes les lignes du début à la fin
* `d'k` coupera/**d**élètera toutes les lignes du début à la fin

#### J'ai quelques fonctions longues et ennuyeuses en haut de mon fichier et je ne veux pas perdre mon temps à faire défiler ou à sauter aux lignes. Cela peut être beaucoup demander parce que ce n'est pas un IDE, mais par hasard, pouvons-nous plier les blocs de code ?

Absolument ! Disons que vous voulez éviter de mémoriser ces numéros de ligne et vous promener avec votre nouvel amour *les marqueurs*. Allez au début du corps de la fonction et tapez `mb`. Maintenant, allez simplement à la fin du corps de la fonction en utilisant `%` (correspondance des accolades) ou toute autre technique pratique et appuyez sur `zf'b` et vous avez terminé !

Avant et après :

![Image](https://cdn-media-1.freecodecamp.org/images/pQwngYKhoq7uH095IKSfMJnhsupztCrys20q)

![Image](https://cdn-media-1.freecodecamp.org/images/Rs9pkL4XAD5wiAOgWZlN8enMjeWXICv54R67)
_Avant-Après_

Si vous êtes à l'aise avec les numéros de ligne, la commande est encore plus facile à retenir : `:5,16fo` (fo signifie **fo**ld). Une fois que vous avez plié votre code, il est facile de basculer entre les vues ouvertes et fermées en utilisant `zo` (Ouvrir le pli de code) et `zc` (Fermer le pli de code). Ne stressez pas trop. Utilisez simplement `za` pour basculer entre les plis ouverts et fermés ?

Disons que vous avez passé un temps considérable à plier vos fonctions dans un grand fichier, vous voudriez évidemment conserver ces plis chaque fois que vous ouvrez ce fichier, n'est-ce pas ? (Sinon, pourquoi avez-vous gaspillé votre énergie à les plier !?), donc il y a une solution directement dans votre `~/.vimrc`. Insérez les lignes suivantes dans `~/.vimrc` et vos plis de code sont sauvegardés et restaurés :

```bash
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview
```

#### Je suis généralement prudent avec mon indentation, mais parfois, je dois éditer le code source d'un autre idiot et cela m'ennuie de modifier son code sans indentation. Y a-t-il des combinaisons de touches magiques pour que cela se produise ?

Bien sûr ! C'est aussi simple que : `=i{`. Vraiment, c'est tout ! ( **_i_** est [objet interne](http://vimdoc.sourceforge.net/htmldoc/motion.html#text-objects))

[**[DEMO] Indentation dans VIM**](https://asciinema.org/a/34MuR5ZxuRTWNmSZBuce1mwRK)  
[_VIM permet aux blocs de code d'être indentés avec quelques touches. Tout ce que vous avez à faire est de placer le curseur dans un bloc de..._asciinema.org](https://asciinema.org/a/34MuR5ZxuRTWNmSZBuce1mwRK)

Avant-après :

![Image](https://cdn-media-1.freecodecamp.org/images/eTijXdqLGj8P4sipH3Sa7t5Kf8-rR6Ea7vik)

![Image](https://cdn-media-1.freecodecamp.org/images/V8qnKIyQxly71eRewU4tcruxI-UCF1w-3G8F)
_Avant-Après_

Tout ce que vous avez à faire est de placer le curseur n'importe où dans un bloc que vous voulez indenter, appuyez sur `Esc` pour entrer en mode normal et ensuite : `=i{`. Boom ! Votre corps de fonction entier (y compris les blocs internes) est indenté.

> NOTE : Ne vous attendez pas à l'indentation de vos fichiers python ?. Cela ne fonctionne que lorsque Vim peut identifier le début et la fin en utilisant les parenthèses ouvrantes et fermantes)

Vous pouvez également augmenter/diminuer l'indentation dans un bloc en utilisant : `>`;i{ pour augmenter et `<i{` pour diminuer en mode normal.

#### Je peux rêver, mais (*voix tremblante*), je veux dire, je veux juste essayer, Uhmm, je peux pousser vraiment loin avec celle-ci, mais (*pause de 5 secondes*)... peu importe, passons à ma prochaine question

Vim est assez ouvert d'esprit pour accepter les critiques ou faire face au fait qu'il n'est pas un IDE, allez-y, voyons ce que vous avez.

#### Uhmmm, désolé, mais par hasard (*haletant*) avec un plugin ou quelque chose, vim a-t-il une complétion automatique comme un IDE ?

? Vous pourriez être surpris, mais oui, c'est le cas ! ? et devinez quoi...
* roulements de tambour *
* roulements de tambour *
* roulements de tambour *
* roulements de tambour *

**Sans plugin !**

Vous m'avez bien entendu ! La seule condition pour que Vim vous montre des options est « Vim doit savoir de quoi vous parlez. » Cela pourrait être par le biais d'un fichier source inclus ou de fonctions ou variables définies.

Tout ce que vous avez à faire est de commencer à taper, puis d'appuyer sur `Ctrl+n` en mode insertion.

![Image](https://cdn-media-1.freecodecamp.org/images/bpqE5V4PSocJYzVCra5QVFD6WpWQgdKyHcw-)

![Image](https://cdn-media-1.freecodecamp.org/images/OBwyMT5rKu2tqTiEYbG-ZiUGdyZQ-J0hKdhJ)

![Image](https://cdn-media-1.freecodecamp.org/images/PtWzDrYGUVKQKHZrX7sNd8PkYQKV54qhXjRf)
_Exemples en C, Python et Java_

Imaginez simplement les utilisations ! Surtout si vous écrivez du code C et que vous ne pouvez pas vous rappeler l'appel exact de la bibliothèque OpenSSL, tout ce que vous avez à faire est d'inclure l'en-tête !

[**[DEMO] Fonctionnalité de complétion automatique dans VIM**](https://asciinema.org/a/NXJIU6fNkCz2Lk2uKYBhcv5Fi)  
[_VIM a des suggestions de complétion automatique pour les mots-clés, les noms de fonctions si les fichiers d'en-tête appropriés sont inclus ou si..._asciinema.org](https://asciinema.org/a/NXJIU6fNkCz2Lk2uKYBhcv5Fi)

![Image](https://cdn-media-1.freecodecamp.org/images/ATclZNHrZU8b2kesTWFlGAcXVlDp2A6KCklC)
_Vim auto-complete aidant avec les fonctions OpenSSL_

Permettez-moi de vous rappeler à nouveau : aucun plugin requis ?

> NOTE : Les fichiers d'en-tête peuvent être à d'autres emplacements sur Mac et Vim peut ne pas être en mesure de les trouver. J'utilise simplement un Mac pour me connecter à une machine linux. Donc, si vous utilisez Mac, désolé pour cela.

#### Je comprends que Vim est juste un éditeur de texte, mais si vous voulez que je travaille sans perdre le focus et sans quitter Vim toutes les cinq minutes, quelles options ai-je si je ne peux pas me souvenir de tous les noms de fichiers ?

Simple, utilisez l'explorateur de fichiers fourni par VIM ? Oui, Vim fournit un explorateur de fichiers simple (*sans aucun plugin*). Il suffit de taper : :`Explore` depuis n'importe quelle fenêtre Vim et vous verrez un explorateur de fichiers facile à naviguer qui peut être parcouru en utilisant les touches fléchées ⬆️ et ⬇️. Appuyez sur la touche Entrée/Retour pour ouvrir un fichier/répertoire. Utilisez :`q` pour quitter l'explorateur et v im. Si vous ne souhaitez pas quitter vim et continuer à travailler avec un fichier ouvert, vous avez 3 options :

1. Ouvrez l'explorateur dans une division horizontale ( `:Sexplore` ) ou verticale ( `:Vexplore` ) et quittez l'explorateur en utilisant `:q`
2. Ouvrez l'explorateur dans une autre [page d'onglet](http://vimdoc.sourceforge.net/htmldoc/tabpage.html) en utilisant `:Texplore` et quittez en utilisant `:q`
3. Ouvrez l'explorateur de fichiers dans votre fenêtre actuelle, puis déchargez le buffer actuel et supprimez-le de la liste des buffers en utilisant `:bdel` (suppression de buffer).

![Image](https://cdn-media-1.freecodecamp.org/images/GImb6qQyAyyLoE4unQ1gelPBDz8A2gbizZW9)
_:Explore depuis n'importe quelle fenêtre vim montre l'explorateur de fichiers_

> NOTE : Vous pouvez également utiliser la commande courte `:Ex` pour ouvrir l'explorateur de fichiers

#### Parfois, je dois répéter les mêmes étapes sur certaines lignes pour éditer quelque chose. Je suis presque sûr que Vim aura une fonctionnalité qui me permet de faire cela. Ai-je raison ?

100% correct ! Vous parlez de macros et Vim supporte les macros. Répéter la dernière commande exécutée est simple et peut accomplir des tâches répétitives simples. Cependant, si le traitement de texte est composé de plusieurs étapes pour obtenir un résultat, les macros sont pratiques.

Considérez un exemple de fichier d'en-tête C :

```c
void encrypt_text(char *text, int bytes)
void decrypt_text(char *text, int bytes)
void process_text(char *text, int bytes)
void another_important_function(int bytes, double precision)
```

Oups ! Vous avez oublié de mettre un point-virgule à la fin de chaque ligne et vous venez de réaliser que toutes ces fonctions retournent un code d'erreur entier au lieu de void.

Les étapes que vous devez effectuer pour faire un changement sur une ligne sont :

* Placez le curseur au début du mot `void`
* Appuyez sur `cw` en mode normal pour supprimer le mot `void` et tapez `int`
* Appuyez sur `Esc`, déplacez-vous à la fin de la ligne en utilisant `Shift+a` pour insérer `;`
* Appuyez sur `Esc` et appuyez sur `^` pour revenir au début de la ligne éditée

Résultant en :

```c
int encrypt_text(char *text, int bytes);
void decrypt_text(char *text, int bytes)
void process_text(char *text, int bytes)
void another_important_function(int bytes, double precision)
```

Vous pouvez simplement enregistrer cette séquence d'étapes et la rejouer sur les 4 lignes.

Tout ce que vous avez à faire, avant de commencer la séquence, commencez à enregistrer la macro dans n'importe quelle lettre (disons `a`) en appuyant sur `qa` en mode normal. Maintenant, vos étapes sont enregistrées dans `a`. Une fois que vous avez terminé toutes vos étapes, appuyez simplement sur `q` en mode normal. Cela mettra fin à l'enregistrement. Pour rejouer ces étapes, placez simplement le curseur au même endroit où il était placé pendant la macro. Appuyez sur `@a` et c'est fait ! BOOM ! Vim répétera les mêmes étapes pour vous sur cette ligne ! Pour le répéter sur plusieurs lignes, vous pouvez également utiliser `@@` après avoir utilisé la commande `@a` une fois

#### Je sais que Vim n'est pas du tout un IDE et que je peux avoir des espoirs déraisonnables, mais juste une question rapide : l'édition à distance de fichiers est-elle possible avec Vim ?

Si vous y pensez en tenant compte des ressources disponibles : 
[1] Vim 
[2] openssh-client (Installé avec la plupart des distributions Linux)

Vous avez de la chance, mon ami ! Oui, Vim supporte l'édition à distance de fichiers ? 
Vim utilise simplement la connexion sécurisée établie par scp (copie sécurisée) fournie par openssh-client. Il arrive que vous travailliez avec des fichiers sur plusieurs machines distantes et que ce soit une perte de temps de se connecter à une machine juste pour éditer un seul fichier ! Vous pouvez vous détendre sur votre machine actuelle si vous connaissez simplement les identifiants de votre machine distante et le chemin.

```bash
vim scp://remoteuser@remote_IP_or_hostname/relative/path/of/file
```

Par exemple : Je dois éditer un fichier sur 10.0.18.12 stocké dans `/home/dev-john/project/src/main.c` et j'ai les identifiants de connexion pour `dev-john`, je peux accéder à `main.c` en utilisant :

```
$ vim scp://dev-john@10.0.18.12/project/src/main.c
```

Je peux utiliser le chemin relatif parce que je peux commencer à chercher le fichier depuis le répertoire personnel de `dev-john`

ASTUCE : Si vous accédez fréquemment à une machine distante, vous pouvez créer un fichier de configuration ssh pour créer un raccourci pour la connexion. Créez un fichier `~/.ssh/config` avec

```bash
Host remote-dev-machine
    Hostname 10.0.18.12
    User dev-john
    IdentityFile ~/.ssh/id_rsa
```

Maintenant, vous pouvez accéder à votre fichier en utilisant :

```bash
$ vim scp://remote-dev-machine/project/src/main.c
```

Si c'est confus de se souvenir du chemin relatif et peu intuitif, vous pouvez également le spécifier avec une alternative :

```bash
$ vim scp://remote-dev-machine/~dev-john/project/src/main.c
```

#### Génial ! Je suis déjà ravi des capacités prêtes à l'emploi de Vim. On dirait que vous avez une solution à beaucoup de problèmes d'édition courants. Voyons voir. J'ai un fichier avec plus de 2000 lignes et les fonctions qui m'intéressent sont situées à la ligne 9, ligne 768 et ligne 1898. Je sais que je peux sauter à une ligne en utilisant le numéro de ligne, mais je ne suis pas très bon pour me souvenir de ces numéros. Avez-vous quelque chose pour moi ?

Bien sûr ! Ce que vous cherchez est une solution de signets locaux dans Vim en utilisant des lettres. Tout ce que vous avez à faire est :

* Placez votre curseur sur n'importe quelle ligne à n'importe quelle position
* Appuyez sur `Esc` pour vous assurer que vous êtes en mode normal
* Appuyez sur `m{lettre minuscule}` où `{lettre minuscule}` est n'importe quelle lettre de `a-z`
* Vous venez de créer un signet local pour naviguer dans votre fichier

Pour voir tous vos signets : Appuyez sur `Esc` et entrez en mode commande, tapez `:marks` et appuyez sur `Entrée/Retour`. Vous verrez une liste de vos signets. Pour visiter n'importe quel signet à n'importe quel moment, appuyez simplement sur `Esc` et tapez ``{lettre minuscule}`. Kaboom ! Vous arriverez à l'emplacement exact avec le curseur où vous avez marqué. Exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/IqGeVQdTLQSrCFzKVqa9-eVswnzGT2SkDy8H)
_Signets dans Vim_

J'ai créé un signet local à la ligne 21, colonne 18 en utilisant `a`. Si je suis en train d'éditer quelque chose à la ligne 1783, je n'aurais qu'à appuyer sur `Esc` et taper ``a` :

![Image](https://cdn-media-1.freecodecamp.org/images/rpK-WeLKT0ESw1RIL80EEgrfBQwy1wWwKnIj)

Pour résoudre votre problème, tout ce que vous avez à faire est de créer 3 signets locaux et de sauter rapidement entre eux en regardant `:marks`.

Problème résolu ?

Et si je vous disais que vous pouvez également créer des signets globaux ?! ? Oui, il est possible de créer des signets globaux également ! Ceux-ci sont équivalents à vos raccourcis Windows ou GUI (ou liens symboliques/durs Linux) sauf que vous n'avez pas besoin de créer un lien réel. Vous m'avez bien entendu ! Vous pouvez littéralement sauter de l'édition d'un fichier dans /`dir1` à un autre fichier et ligne dans /`project/src/` depuis votre Vim sans quitter ! ?

Ne vous inquiétez pas, ce n'est pas une grosse nouvelle chose à retenir. Tout ce que vous avez à faire est : 
Utilisez une lettre majuscule au lieu d'une lettre minuscule pour créer un signet global. C'est tout ! Vraiment ! Vous naviguez vers le signet global en utilisant le même processus. Exemple : Si vous avez créé un signet en utilisant `mP`, tout ce que vous avez à faire est d'appuyer sur `Esc` et de taper ``P` et BAM ! Vous sautez à votre signet global (Vim se souvient du chemin, donc vous n'avez pas à taper quoi que ce soit sur le chemin)

Vous pouvez accéder aux signets globaux de la même manière que les locaux : `:marks`

```bash
:marks
mark line  col file/text
 P     53    4 ~/project/src/large-file.c
 A     11    0 ~/project/README.md
```

NOTE : Si vous n'êtes pas intéressé par la position du curseur et que vous voulez simplement être au début de votre ligne marquée, utilisez `'P` au lieu de ``P` (Utilisez une apostrophe simple au lieu d'une apostrophe inversée pour être positionné au début de la ligne)

#### J'ai entendu dire que Vim supporte la division de fenêtre ainsi que les onglets ! Je comprends que les onglets sont géniaux et que vous pouvez travailler avec plusieurs fichiers ouverts à la fois. Mais, qu'en est-il de la division ? Pourquoi voudrais-je cela ?

Scénarios :

* Vous pouvez vouloir éditer un fichier en regardant un autre fichier simultanément (Peut-être que vous définissez une fonction C en regardant sa déclaration dans un fichier d'en-tête)
* Vous pouvez vouloir éditer une partie d'un fichier en regardant la partie supérieure/inférieure du même fichier simultanément
* Votre travail peut vous obliger à éditer un fichier en regardant différentes parties de différents fichiers simultanément

Vim supporte la division de l'écran à la fois horizontalement et verticalement. Encore mieux, vous pouvez même naviguer dans le système de fichiers pour ouvrir un fichier lorsque vous divisez votre écran.

Voici les options disponibles :

```
:split filename  - divise la fenêtre horizontalement et charge le fichier
:vsplit file     - division verticale et ouvre le fichier
ctrl-w flèche haut  - déplace le curseur vers le haut d'une fenêtre
ctrl-w ctrl-w    - déplace le curseur vers une autre fenêtre (cycle)
ctrl-w _         - maximise la fenêtre actuelle verticalement
ctrl-w |         - maximise la fenêtre actuelle horizontalement
ctrl-w =         - rend toutes les tailles égales
:sview file      - même que split, mais en lecture seule
:close           - ferme la fenêtre actuelle
```

![Image](https://cdn-media-1.freecodecamp.org/images/wj-bKJhdZ0ZJpjs3ryZGa9vGat9nkn6PoZB6)

![Image](https://cdn-media-1.freecodecamp.org/images/4fwUNCFGZHMpC9NgLN34JGK1JFMOSpSwRANi)
_Fenêtre normale (en haut à gauche), :split <file> (en haut à droite), :vsplit <file> (en bas)_

![Image](https://cdn-media-1.freecodecamp.org/images/E1ewlYcq9bHjEW1sXhSpt1LaKlqNPH81jWw4)

Maximisation d'une fenêtre pour le travail :

![Image](https://cdn-media-1.freecodecamp.org/images/6ojjo1cyuKPSotf19qxtRcksAKoamYpx3mgz)
_Le panneau doit être maximisé verticalement et horizontalement pour occuper toute la fenêtre_

**Redimensionnement :**

```
CTRL-W [N] -	Diminue la hauteur de la fenêtre actuelle de N (par défaut 1)
CTRL-W [N] +	Augmente la hauteur de la fenêtre actuelle de N (par défaut 1)
CTRL-W [N] <	Diminue la largeur de la fenêtre actuelle de N (par défaut 1)
CTRL-W [N} >	Augmente la largeur de la fenêtre actuelle de N (par défaut 1)
```

**Y a-t-il un moyen d'utiliser l'explorateur de fichiers lorsque je divise les panneaux ? (Je ne peux pas me souvenir et taper les noms de fichiers toujours !)**

Bien sûr, tout ce que vous avez à faire est de taper : `:Sexplore` pour l'explorateur de fichiers horizontal et `:Vexplore` pour l'explorateur de fichiers vertical. Vous pouvez également utiliser `:Vexplore!` pour ouvrir l'explorateur de fichiers du côté droit (au lieu du côté gauche par défaut)

Encore une fois, tout cela fonctionne *sans aucun plugin supplémentaire* ?

#### Je suis en train d'éditer du code et j'ai rapidement besoin d'exécuter une commande shell. Dois-je sauvegarder mon travail, quitter Vim et exécuter mes commandes ? Je parie qu'il y a une meilleure façon avec Vim

Vous pariez ! Vim ne veut tout simplement pas que vous quittiez Vim et veut que vous continuiez à vous concentrer sur votre travail. D'où l'option d'exécuter des commandes shell depuis votre Vim. Ne vous inquiétez pas, tout votre travail non sauvegardé n'est pas rejeté, vous exécutez simplement votre commande et BAM ! vous êtes de retour dans votre fichier sauvegardé/non sauvegardé en toute sécurité !

Disons que vous êtes en train d'une session de codage et que vous avez rapidement besoin de consulter la page man des opérations de fichier parce que vous avez oublié la signature ! Vous n'avez pas besoin de sauvegarder votre travail, de quitter Vim et de vérifier les pages man, ou vous n'avez pas besoin d'ouvrir un autre onglet juste pour la page man. Vous pouvez émettre la commande directement depuis l'éditeur Vim.

[**[DEMO] Commandes Unix depuis VIM**](https://asciinema.org/a/vZgdxBb0slZG3cB9ZXqNFpgpi)  
[_VIM permet aux utilisateurs d'exécuter des commandes shell depuis VIM sans quitter. Tout ce que vous avez à faire est d'entrer la commande..._asciinema.org](https://asciinema.org/a/vZgdxBb0slZG3cB9ZXqNFpgpi)

![Image](https://cdn-media-1.freecodecamp.org/images/AdheBhI32Ti3bOsjH-FUPuqugongB41XMJ-k)

![Image](https://cdn-media-1.freecodecamp.org/images/PbN-40zw3dLd-ADaoSlY9j4r1CPveMmCdy5Q)

![Image](https://cdn-media-1.freecodecamp.org/images/QR57vMytkwfcB3eNbz2UDIRAS6hxw3T7j5nJ)
_De gauche à droite (Exécuter des commandes shell depuis Vim et revenir à l'éditeur)_

Devinez quoi ! Préparez-vous à être émerveillé. Vim supporte également la commande `make` depuis votre fichier ! Tout ce que vous avez à faire est de naviguer vers un répertoire avec `Makefile`. Ouvrez n'importe quel fichier (pourrait être votre code source) et faites toutes les modifications et sauvegardez-le. Attendez, il n'y a pas besoin de quitter pour voir le résultat de la compilation. Vous pouvez déclencher votre build make directement depuis Vim :

[**[DEMO] Déclencher des builds make depuis vim**](https://asciinema.org/a/148687)  
[_VIM permet aux utilisateurs de déclencher des builds make sans quitter VIM. Tout ce que nous avons à faire est d'entrer en mode commande et de taper :make_asciinema.org](https://asciinema.org/a/148687)

![Image](https://cdn-media-1.freecodecamp.org/images/X5Fc1RFaV6cmQNbfBZx-mk0SORNL6vt7ZhKj)

![Image](https://cdn-media-1.freecodecamp.org/images/RtDOq--CU522ri03TzCNsfXXsvZ5k8bnU0QY)

![Image](https://cdn-media-1.freecodecamp.org/images/KbeSb0lbsalK-wXV7JLnLuf1kiRLYP-qQQt7)
_Déclencher des builds make depuis Vim_

De même, vous pouvez construire d'autres cibles dans votre Makefile !

Exemple : Nettoyage du répertoire

![Image](https://cdn-media-1.freecodecamp.org/images/et4iHMv7ucgX9wwpKF9q3tv6EItczICVobsz)

![Image](https://cdn-media-1.freecodecamp.org/images/ERlbwxBamwe-f6OIU3i5pypZdBCKTJvlxNt1)

![Image](https://cdn-media-1.freecodecamp.org/images/6hcFG2Kp9MZ0YhswQDNdIBfduX9NICQNpvx3)
_Nettoyage du répertoire en utilisant la commande make depuis VIM_

J'espère que ces fonctionnalités cool vous aideront à utiliser Vim de manière plus productive.

Vos commentaires sont toujours les bienvenus.

N'hésitez pas à commenter, critiquer ou applaudir ?

#### Références :

* [http://www.openvim.com/tutorial.html](http://www.openvim.com/tutorial.html)
* [https://linuxconfig.org/vim-tutorial](https://linuxconfig.org/vim-tutorial)
* [ftp://ftp.vim.org/pub/vim/doc/book/vimbook-OPL.pdf](ftp://ftp.vim.org/pub/vim/doc/book/vimbook-OPL.pdf)
* [http://vim.wikia.com/wiki/Tutorial](http://vim.wikia.com/wiki/Tutorial)
* [http://www.viemu.com/a-why-vi-vim.html](http://www.viemu.com/a-why-vi-vim.html)
* [http://robertames.com/files/vim-editing.html](http://robertames.com/files/vim-editing.html)
* [https://www.youtube.com/watch?v=wlR5gYd6um0](https://www.youtube.com/watch?v=wlR5gYd6um0)