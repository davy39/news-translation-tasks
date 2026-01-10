---
title: Modes de l'éditeur Vim expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-18T22:07:00.000Z'
originalURL: https://freecodecamp.org/news/vim-editor-modes-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ea2740569d1a4ca3e40.jpg
tags:
- name: editor
  slug: editor
- name: vim
  slug: vim
seo_title: Modes de l'éditeur Vim expliqués
seo_desc: 'Because Vim is focused on changing existing code just as much as writing
  new code, it is split into several modes that each have different purposes.

  Normal Mode

  By default, Vim starts in “normal” mode. Normal mode can be accessed from other
  modes by ...'
---

Parce que Vim est axé sur la modification du code existant autant que sur l'écriture de nouveau code, il est divisé en plusieurs modes, chacun ayant des objectifs différents.

### **Mode Normal**

Par défaut, Vim démarre en mode "normal". Le mode normal peut être accessible depuis d'autres modes en appuyant sur `Esc` ou `<C-[>`.

En mode normal, les pressions de touches ne fonctionnent pas comme on pourrait s'y attendre. C'est-à-dire qu'elles n'insèrent pas de texte dans le document ; à la place, certaines pressions de touches peuvent :

#### **Déplacer le curseur**

* **h** déplacer d'un caractère vers la gauche
* **j** déplacer d'une ligne vers le bas
* **k** déplacer d'une ligne vers le haut
* **l** déplacer d'un caractère vers la droite

Comme pour de nombreuses commandes Vim, le déplacement de ligne peut être précédé d'un nombre pour déplacer plusieurs lignes à la fois :

* **4j** déplacer de 4 lignes vers le bas
* **6k** déplacer de 6 lignes vers le haut

Déplacements de base par mot :

* **w** aller au début du mot suivant
* **b** aller au début du mot précédent
* **e** aller à la fin du mot
* **W** aller au début du mot suivant après un espace
* **B** aller au début du mot précédent avant un espace
* **E** aller à la fin du mot avant un espace

Déplacement au début/fin de ligne :

* **0** aller au début de la ligne
* **$** aller à la fin de la ligne

#### **Manipuler le texte**

#### **Accéder à d'autres modes**

Le **mode normal** est celui où l'on devrait passer la plupart de son temps lors de l'utilisation de Vim. N'oubliez pas, c'est ce qui rend Vim différent.

En mode normal, il existe plusieurs façons de se déplacer dans un fichier ouvert. En plus d'utiliser les touches de curseur pour se déplacer, vous pouvez utiliser `h` (gauche), `j` (bas), `k` (haut) et `l` (droite) pour vous déplacer également. Cela aide particulièrement les dactylographes qui n'aiment pas quitter la rangée de base lors des modifications.

Vous pouvez également apporter des modifications à des caractères individuels en mode normal. Par exemple, pour remplacer un seul caractère, placez votre curseur dessus et appuyez sur `r`, puis sur le caractère avec lequel vous souhaitez le remplacer. De même, vous pouvez supprimer des caractères individuels en plaçant votre curseur dessus et en appuyant sur `x`.

Pour effectuer un annuler, appuyez sur `u` en mode normal. Cela annule les modifications jusqu'à la dernière fois où vous étiez en mode normal. Si vous souhaitez rétablir (_c'est-à-dire_, annuler votre annulation), appuyez sur `Ctrl+r` en mode normal.

### **Mode Insertion**

C'est le deuxième mode le plus utilisé, et il sera le comportement le plus familier pour la plupart des gens. Une fois en mode insertion, la frappe insère des caractères comme dans un éditeur de texte classique. Vous pouvez y accéder en utilisant une commande d'insertion depuis le mode normal.

Les commandes d'insertion incluent :

* `i` pour "**i**nsérer", cela bascule immédiatement Vim en mode insertion
* `a` pour "**a**jouter", cela déplace le curseur après le caractère actuel et entre en mode insertion
* `o` insère une nouvelle ligne sous la ligne actuelle et entre en mode insertion sur la nouvelle ligne

Ces commandes ont également une variante en majuscules :

* `I` déplace le curseur au début de la ligne et entre en mode insertion
* `A` déplace le curseur à la fin de la ligne et entre en mode insertion
* `O` insère une nouvelle ligne au-dessus de la ligne actuelle et entre en mode insertion sur la nouvelle ligne

Il existe de nombreuses autres façons d'insérer du texte dans Vim qui ne peuvent pas être listées ici, mais ce sont les plus simples. De plus, méfiez-vous de rester trop longtemps en mode insertion ; Vim n'est pas conçu pour être utilisé en mode insertion tout le temps.

Pour quitter le mode insertion et revenir au mode normal, appuyez sur `Esc` ou `<C-[>`.

### **Mode Visuel**

Le mode visuel est utilisé pour effectuer des sélections de texte, de manière similaire à un clic et glisser avec une souris. Sélectionner du texte permet d'appliquer des commandes uniquement à la sélection, telles que copier, supprimer, remplacer, etc.

Pour effectuer une sélection de texte :

* Appuyez sur `v` pour entrer en mode visuel, cela marquera également un point de début de sélection
* Déplacez le curseur vers le point de fin de sélection souhaité ; Vim fournira une mise en surbrillance visuelle de la sélection de texte

Le mode visuel a également les variantes suivantes :

* `V` pour entrer en mode visuel ligne, cela effectuera des sélections de texte par ligne
* `<C-V>` pour entrer en mode visuel bloc, cela effectuera des sélections de texte par blocs ; déplacer le curseur effectuera des sélections rectangulaires du texte

Pour quitter le mode visuel et revenir au mode normal, appuyez sur `Esc` ou `<C-[>`.

Le mode visuel a en réalité plusieurs sous-types : _visuel_, _bloc-visuel_ et _ligne-visuel_

* _visuel_ : comme décrit ci-dessus. Entrez en appuyant sur `v`
* _bloc-visuel_ : sélectionnez n'importe quelle région rectangulaire. Entrez en appuyant sur `<ctrl>+v`
* _ligne-visuel_ : sélectionnez toujours des lignes complètes. Entrez en appuyant sur `<shift>+v`

### **Mode Commande**

Le mode commande dispose d'une grande variété de commandes et peut faire des choses que le mode normal ne peut pas faire aussi facilement. Pour entrer en mode commande, tapez `:` depuis le mode normal, puis tapez votre commande qui devrait apparaître en bas de la fenêtre. Par exemple, pour effectuer une recherche et un remplacement global, tapez `:%s/foo/bar/g` pour remplacer tout "foo" par "bar".

* `:` Entrez en mode commande
* `%` Signifie sur toutes les lignes
* `s` Signifie substituer
* `/foo` est l'expression régulière pour trouver les éléments à remplacer
* `/bar/` est l'expression régulière pour remplacer les éléments
* `/g` signifie global, sinon il ne s'exécuterait qu'une fois par ligne

Vim dispose d'un certain nombre d'autres méthodes que vous pouvez lire dans la documentation d'aide, `:h` ou `:help`.

### **Mode Remplacement**

Le mode remplacement vous permet de remplacer le texte existant en tapant directement par-dessus. Avant d'entrer dans ce mode, passez en mode normal et placez votre curseur sur le premier caractère que vous souhaitez remplacer. Ensuite, appuyez sur `R` (R majuscule) pour entrer en mode remplacement. Maintenant, tout ce que vous tapez remplacera le texte existant. Le curseur se déplace automatiquement vers le caractère suivant, comme en mode insertion. La seule différence est que chaque caractère que vous tapez remplacera celui existant.