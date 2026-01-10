---
title: 7 astuces Vim qui ont changé ma vie (avec démo)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-02T21:24:51.000Z'
originalURL: https://freecodecamp.org/news/7-vim-tips-that-changed-my-life
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/image_2020-04-19_16-22-44.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: editor
  slug: editor
- name: tips
  slug: tips
- name: vim
  slug: vim
seo_title: 7 astuces Vim qui ont changé ma vie (avec démo)
seo_desc: 'By Alex Kallaway

  Hi, fellow coders! You may have heard of the Vim code editor before, or even used
  it a bit.

  There are plenty of resources out there that cover the basics of Vim and I don''t
  want to just do another rewrite of those here. Instead, I wa...'
---

Par Alex Kallaway

Salut, chers codeurs ! Vous avez peut-être déjà entendu parler de l'éditeur de code Vim, ou même l'avez-vous déjà un peu utilisé.

Il existe de nombreuses ressources qui couvrent les bases de Vim et je ne veux pas simplement en faire une énième réécriture ici. Au lieu de cela, je souhaite partager quelques astuces rapides que j'ai apprises des autres en utilisant Vim à plein temps au travail.

Ce sont de petites choses que vous pouvez apprendre rapidement et qui feront une grande différence dans votre travail quotidien avec Vim. Elles m'ont définitivement facilité la vie.

Rappel : Vim est pré-installé sur Mac et Linux. Il vous suffit d'ouvrir votre terminal et de taper "vim" dans l'invite de commande pour ouvrir Vim. Si vous avez un ordinateur Windows, [suivez ces instructions pour installer Vim sur votre PC](https://www.freecodecamp.org/news/vim-windows-install-powershell/).

## Avant de commencer

Si vous êtes intéressé par Vim mais que vous n'avez pas encore commencé, voici les ressources que je recommanderais :

* [OpenVim](https://www.openvim.com) - Tutoriel Vim interactif
* vimtutor - il s'agit d'un tutoriel interactif en ligne de commande disponible et installé sur Mac et certaines distributions Linux. Tapez simplement `vimtutor` dans votre terminal
* [VimAdventures](https://vim-adventures.com/) - Les deux premiers niveaux sont gratuits, et si vous aimez le format, la licence complète coûte 25 $

Si vous aimez Vim mais que c'est trop lourd de l'exécuter seul, installez une extension Vim pour votre éditeur préféré, comme VS Code, Sublime ou tout autre. De cette façon, vous pourrez utiliser les actions rapides et les raccourcis de Vim tout en profitant d'une interface plus conviviale à laquelle vous êtes habitué.

Une prise de conscience importante que j'ai eue concernant l'apprentissage et le travail avec Vim : vous n'avez pas besoin de tout maîtriser (ce qui est de toute façon pratiquement impossible) pour commencer à l'utiliser.

Une fois que vous avez compris les bases, chaque fois que vous avez une question ou un blocage au cours de votre journée de travail, notez-le, puis parcourez cette liste et cherchez sur Internet comment faire cela dans Vim.

De cette façon, vous comblerez progressivement vos lacunes et vous vous améliorerez avec chaque petite nouveauté que vous ajouterez à votre répertoire (ces micro-améliorations seront similaires aux astuces de cet article ci-dessous).

Passons maintenant aux choses amusantes – les trucs et astuces. Vous n'avez pas besoin d'avoir de plugins Vim installés pour en profiter.

## 1. Comment commencer à écrire sur une ligne avec l'indentation correcte

Avant d'apprendre cela, j'avais l'habitude de sauter sur une nouvelle ligne, de passer en mode insertion, d'utiliser TAB jusqu'à la bonne indentation et de commencer à taper du code. Avec cette petite astuce, vous n'aurez plus à faire toutes ces tabulations supplémentaires, elle vous placera directement en mode insertion avec la bonne indentation.

RECETTE : `S` (MAJ+s)

DÉMO :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/vimtips-shift-s.gif)

## 2. Redimensionner les fenêtres automatiquement

Très souvent, nous faisons quelque chose avec les fenêtres à l'intérieur de Vim qui provoque un mauvais redimensionnement, l'une étant parfois beaucoup trop large et l'autre beaucoup trop étroite.

Le moyen le plus simple de voir cet effet est d'ouvrir 3 fenêtres dans un onglet Vim et de redimensionner la fenêtre du terminal dans laquelle vous avez ouvert Vim.

Vous voulez redimensionner les fenêtres pour qu'elles aient toutes la même taille, avec l'espace disponible uniformément réparti. La bonne nouvelle est que vous n'avez pas à le faire manuellement.

RECETTE : `CTRL+w =`

La combinaison de CTRL+w, suivie de la touche du signe égal, égalisera les fenêtres.

DÉMO :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/vimtips-equalize-3.gif)

## 3. Sauter à la parenthèse/accolade correspondante

Avec votre curseur sur un crochet [ ou une parenthèse ( ou une accolade {, appuyez sur % (MAJ+5) pour sauter à son symbole correspondant. Appuyez à nouveau pour revenir en arrière (basculer entre eux).

```
if (condition) {
  // code
}
// Si votre curseur était sur {, et que vous avez appuyé sur %, vous sauteriez à }

```

RECETTE : `%` avec votre curseur sur le caractère dont vous voulez trouver la correspondance.

DÉMO :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/vimtips-percent.gif)

## 4. Indenter/Désindenter une ligne ou plusieurs lignes

```
>> ⁠– indente une ligne
<< ⁠– désindente une ligne

```

Lorsque vous avez plusieurs lignes sélectionnées (en mode VISUAL LINE), il vous suffit d'appuyer une seule fois sur > ou < pour indenter ou désindenter les lignes (comme indiqué dans la démo ci-dessous).

L'endroit où se trouve votre curseur dans la ligne n'a pas d'importance lors de l'indentation - cela fonctionnera quand même. Une fois l'indentation terminée, le curseur est automatiquement positionné sur le premier caractère non vide de la ligne.

RECETTE : Une ligne : `>>`, `<<`. Plusieurs lignes : `>`, `<`.

DÉMO :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/vimtips-move-a-line.gif)

## 5. Corriger l'indentation dans tout le fichier

Commencez en haut d'un fichier (pour y arriver, appuyez sur `gg` n'importe où dans le fichier). Appuyez ensuite sur `=G`, et Vim corrigera l'indentation dans tout le fichier. Si vous ne commencez pas au début du fichier, il corrigera l'indentation de la ligne actuelle jusqu'au bas du fichier.

RECETTE : `=G`

Appuyez sur le signe égal, suivi de MAJ+G

DÉMO :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/vimtips-format.gif)

## 6. Les bases du travail avec les onglets

Souvent, vous voulez regarder plusieurs fichiers ou contextes en même temps. Les onglets Vim sont une fonctionnalité très pratique mais sous-utilisée pour cela. Je ne connais aucun autre éditeur qui supporte cela (mais je suis sûr qu'il existe un moyen de le faire ailleurs).

Par exemple, j'aime garder mes fichiers liés au code dans mon onglet principal, et dans un autre onglet : le README avec une liste de choses à faire (TODO) et un endroit où je peux noter d'autres idées.

Pour écrire les commandes permettant de travailler avec les onglets, vous devrez être en mode commande. Pour commencer à écrire la commande, appuyez sur `:` et tapez. La commande s'affichera dans le coin inférieur gauche de l'éditeur au fur et à mesure que vous tapez. Appuyez sur Entrée pour exécuter.

RECETTE :   
`:tabnew` crée un nouvel onglet  
`gt` - aller à l'onglet suivant  
`gT` - aller à l'onglet précédent  
`:tabo` - fermer tous les autres onglets à part l'onglet actif

DÉMO :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/vimtips-tabs.gif)

## 7. Comment revenir rapidement à un fichier précédent

Souvent, lorsque vous éditez un fichier de code, vous en ouvrez un autre dans la même fenêtre. Il n'est alors pas si facile de revenir à celui sur lequel vous veniez de travailler. Vous pourriez lister les buffers et naviguer vers le précédent, mais vous devez vous souvenir de son nom pour cela et y consacrer votre temps précieux. Les utilisateurs de Vim n'aiment pas passer trop de temps sur les actions. :) Vous pouvez donc utiliser CTRL+o pour cela.

Tout ce que cela fait, c'est trouver une position précédente de votre curseur - et s'il se trouvait dans un fichier différent (celui que vous venez de perdre en en ouvrant un nouveau), cela nous ramène directement là-bas.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/vimtips-ctrl-o.gif)

Merci de m'avoir lu et j'espère que ces astuces vous seront utiles !  
  
? Si vous voulez suivre mes aventures, [voici mon Twitter](https://twitter.com/ka11away) :)

? J'écris une newsletter hebdomadaire qui couvre des sujets comme l'apprentissage du code, le changement d'habitudes, les finances personnelles, des recommandations de livres et les points clés à retenir, le minimalisme, la création d'entreprise, la psychologie et plus encore. Pour ceux d'entre vous qui sont intéressés : rejoignez plus de 1 000 personnes partageant les mêmes idées et passionnées par l'amélioration de soi et l'apprentissage.  
[Abonnez-vous ici](https://www.dotheoppo.site/newsletter)

? En ce moment, je travaille sur mon projet secondaire - une application appelée "Zerno". Inscrivez-vous pour obtenir un accès anticipé très bientôt !   
[Application ZERNO](https://www.zerno.app)