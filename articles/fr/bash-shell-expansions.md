---
title: 'Bash et les expansions de shell : création paresseuse de listes'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-11-21T15:14:00.000Z'
originalURL: https://freecodecamp.org/news/bash-shell-expansions
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/cover-1.png
tags:
- name: Bash
  slug: bash
- name: Productivity
  slug: productivity
- name: shell script
  slug: shell-script
- name: terminal
  slug: terminal
seo_title: 'Bash et les expansions de shell : création paresseuse de listes'
seo_desc: It’s that time of year again! When stores start putting up colourful sparkly
  lit-up plastic bits, we all begin to feel a little festive, and by festive I mean
  let’s go shopping. Specifically, holiday gift shopping! (Gifts for yourself are
  still gifts...
---

C'est cette période de l'année encore ! Quand les magasins commencent à installer des morceaux de plastique colorés et scintillants, nous commençons tous à nous sentir un peu festifs, et par festifs, je veux dire faisons du shopping. Plus précisément, le shopping de cadeaux de vacances ! (Les cadeaux pour soi-même sont toujours des cadeaux, techniquement.)

Pour que cela ne devienne pas complètement fou, vous devriez faire quelques listes de cadeaux. Bash peut aider.

## Expansion d'accolades

Ce ne sont pas des accolades : `()`

Ce ne sont pas non plus des accolades : `[]`

_Ce sont_ des accolades : `{}`

Les accolades indiquent à Bash de faire quelque chose avec la ou les chaînes arbitraires qu'il trouve entre elles. Plusieurs chaînes sont séparées par des virgules : `{a,b,c}`. Vous pouvez également ajouter un préambule et un post-script optionnels à attacher à chaque résultat développé. Principalement, cela peut économiser quelques frappes, comme avec les chemins de fichiers et les extensions courants.

Faisons quelques listes pour chaque personne à qui nous voulons offrir des cadeaux. Les commandes suivantes sont équivalentes :

```sh
touch /home/me/gift-lists/Amy.txt /home/me/gift-lists/Bryan.txt /home/me/gift-lists/Charlie.txt
```

```sh
touch /home/me/gift-lists/{Amy,Bryan,Charlie}.txt
```

```sh
tree gift-lists

/home/me/gift-lists
├── Amy.txt
├── Bryan.txt
└── Charlie.txt
```

Oh zut, « Bryan » écrit son nom avec un « i ». Je peux corriger cela.

```sh
mv /home/me/gift-lists/{Bryan,Brian}.txt

renamed '/home/me/gift-lists/Bryan.txt' -> '/home/me/gift-lists/Brian.txt'
```

## Expansions de paramètres de shell

[L'expansion de paramètres de shell](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html) nous permet d'apporter toutes sortes de modifications aux paramètres enfermés dans des accolades, comme manipuler et substituer du texte.

Il y a quelques petits cadeaux que tous nos destinataires méritent. Faisons-en une variable :

```sh
STUFF=$'socks\nlump of coal\nwhite chocolate'

echo "$STUFF"
socks
lump of coal
white chocolate
```

Maintenant, ajoutons ces articles à chacune de nos listes avec un peu d'aide de [la commande `tee`](https://en.wikipedia.org/wiki/Tee_(command)) pour faire en sorte que `echo` et les expansions fonctionnent bien ensemble.

```sh
echo "$STUFF" | tee {Amy,Brian,Charlie}.txt

cat {Amy,Brian,Charlie}.txt

socks
lump of coal
white chocolate
socks
lump of coal
white chocolate
socks
lump of coal
white chocolate
```

### Substitution de correspondance de motif

En y repensant, peut-être que le morceau de charbon n'est pas un si beau cadeau. Vous pouvez le remplacer par quelque chose de mieux en utilisant une substitution de correspondance de motif sous la forme `${parameter/pattern/string}` :

```sh
echo "${STUFF/lump of coal/candy cane}" | tee {Amy,Brian,Charlie}.txt

cat {Amy,Brian,Charlie}.txt

socks
candy cane
white chocolate
socks
candy cane
white chocolate
socks
candy cane
white chocolate
```

Cela remplace la première instance de « lump of coal » par « candy cane ». Pour remplacer toutes les instances (s'il y en avait plusieurs), utilisez `${parameter//pattern/string}`. Cela ne change pas notre variable `$STUFF`, donc nous pouvons toujours réutiliser la liste originale pour quelqu'un de méchant plus tard.

### Sous-chaînes

Tandis que nous améliorons les choses, nos destinataires n'aiment peut-être pas tous le chocolat blanc. Nous ferions mieux d'ajouter un peu de chocolat ordinaire à nos listes au cas où. Puisque je suis super paresseux, je vais simplement appuyer sur la flèche vers le haut et modifier une commande Bash précédente. Heureusement, le dernier mot dans la variable `$STUFF` est « chocolate », qui fait neuf caractères de long, donc je vais dire à Bash de garder juste cette partie en utilisant `${parameter:offset}`. J'utiliserai le drapeau `-a` de `tee` pour `a`jouter à mes listes existantes :

```sh
echo "${STUFF: -9}" | tee -a {Amy,Brian,Charlie}.txt

cat {Amy,Brian,Charlie}.txt

socks
candy cane
white chocolate
chocolate
socks
candy cane
white chocolate
chocolate
socks
candy cane
white chocolate
chocolate
```

Vous pouvez aussi :

| Faire ceci                                          | Avec ceci          |
| ---------------------------------------------------- | ------------------ |
| Obtenir une sous-chaîne à partir du n-ième caractère | `${parameter:n}`   |
| Obtenir une sous-chaîne de x caractères à partir de n | `${parameter:n:x}` |

Voilà ! Maintenant nos listes de base sont terminées. Prenons un peu de lait de poule.

### Tester les variables

Vous savez, c'est peut-être le lait de poule, mais je pense avoir commencé une liste pour Amy hier et l'avoir stockée dans une variable que j'aurais pu appeler `amy`. Voyons si je l'ai fait. J'utiliserai l'expansion `${parameter:?word}`. Elle écrira `word` sur la sortie d'erreur standard et quittera s'il n'y a pas de paramètre `amy`.

```sh
echo "${amy:?no such}"

bash: amy: no such
```

Je suppose que non. Peut-être que c'était Brian à la place ?

```sh
echo "${brian:?no such}"

Lederhosen
```

Vous pouvez aussi :

| Faire ceci                                                      | Avec ceci            |
| ---------------------------------------------------------------- | -------------------- |
| Substituer `word` si `parameter` n'est pas défini ou est nul     | `${parameter:-word}` |
| Substituer `word` si `parameter` n'est pas non défini ou nul     | `${parameter:+word}` |
| Assigner `word` à `parameter` si `parameter` n'est pas défini ou est nul | `${parameter:=word}` |

### Changer la casse

C'est ça ! Brian a dit qu'il voulait des lederhosen et donc je me suis fait une note. C'est assez important, donc je vais l'ajouter à la liste de Brian en lettres majuscules avec l'expansion `${parameter^^pattern}`. La partie `pattern` est optionnelle. Nous n'écrivons que dans la liste de Brian, donc j'utiliserai simplement `>>` au lieu de `tee -a`.

```sh
echo "${brian^^}" >> Brian.txt

cat Brian.txt

socks
candy cane
white chocolate
chocolate
LEDERHOSEN
```

Vous pouvez aussi :

| Faire ceci                     | Avec ceci               |
| ------------------------------- | ----------------------- |
| Mettre en majuscule la première lettre | `${parameter^pattern}`  |
| Mettre en minuscule la première lettre  | `${parameter,pattern}`  |
| Mettre en minuscules toutes les lettres       | `${parameter,,pattern}` |

### Développer les tableaux

Vous savez quoi, toute cette affaire de liste de cadeaux est un travail énorme. Je vais simplement faire [un tableau](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Arrays) des choses que j'ai vues au magasin :

```sh
gifts=(sweater gameboy wagon pillows chestnuts hairbrush)
```

Je peux utiliser l'expansion de sous-chaîne sous la forme `${parameter:offset:length}` pour simplifier cela. J'ajouterai les deux premiers à la liste d'Amy, les deux du milieu à celle de Brian, et les deux derniers à celle de Charlie. J'utiliserai `printf` pour aider avec les nouvelles lignes.

```sh
printf '%s\n' "${gifts[@]:0:2}" >> Amy.txt
printf '%s\n' "${gifts[@]:2:2}" >> Brian.txt
printf '%s\n' "${gifts[@]: -2}" >> Charlie.txt
```

```sh
cat Amy.txt

socks
candy cane
white chocolate
chocolate
sweater
gameboy

cat Brian.txt

socks
candy cane
white chocolate
chocolate
LEDERHOSEN
wagon
pillows

cat Charlie.txt

socks
candy cane
white chocolate
chocolate
chestnuts
hairbrush
```

Voilà ! Maintenant nous avons un ensemble complet de listes de cadeaux super personnalisées. Merci Bash ! Dommage qu'il ne puisse pas faire les achats pour nous aussi.