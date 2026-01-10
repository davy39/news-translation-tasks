---
title: Comment « Gravity Falls » peut vous aider à enseigner les bases de la cryptographie
  à vos enfants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-06T12:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-gravity-falls-can-help-you-teach-your-kids-basics-of-cryptography-18e1c6f9ac39
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i1wUMam8Rgkq-XMwmu7YlA.png
tags:
- name: children
  slug: children
- name: Cryptography
  slug: cryptography
- name: life
  slug: life
- name: 'self-improvement '
  slug: self-improvement
- name: technology
  slug: technology
seo_title: Comment « Gravity Falls » peut vous aider à enseigner les bases de la cryptographie
  à vos enfants
seo_desc: 'By Kamil Tustanowski

  It’s Wednesday evening. My two sons and daughter are ready. I press play and we
  start a journey that takes us all farther than we ever anticipated.

  We watched the first episode of Gravity Falls. The visuals, characters, plot and
  ...'
---

Par Kamil Tustanowski

C'est un mercredi soir. Mes deux fils et ma fille sont prêts. J'appuie sur lecture et nous commençons un voyage qui nous emmène tous plus loin que nous ne l'avions jamais anticipé.

Nous avons regardé le premier épisode de [Gravity Falls](http://www.imdb.com/title/tt1865718/). Les visuels, les personnages, l'intrigue et l'humour sont de premier ordre et nous voulions définitivement plus, mais... nous avons repéré quelque chose à la fin des crédits. Quelque chose que nous n'attendions pas. Quelque chose qui a rendu le visionnage de cette série bien plus intéressante et captivante.

Un `message chiffré`.

Voici comment nous avons décrypté les codes. Et nous nous sommes bien amusés à le faire par nous-mêmes. Sans vérifier quoi que ce soit sur internet. Si j'ai attiré votre attention, je vous recommande d'arrêter de lire et d'essayer de le faire vous-même. Ensuite, vous pourrez revenir et lire mes solutions et explications ci-dessous.

#### **ZHOFRPH WR JUDYLWB IDOOV**

Nous étions certains que c'était un message. À première vue, je pensais qu'il était chiffré avec une sorte de chiffre de substitution.

> Le chiffrement utilisant un chiffre de substitution remplace essentiellement les lettres par d'autres lettres selon une règle générale. Le déchiffrement est effectué en appliquant cette règle à l'envers au texte chiffré. Ces types de chiffres ne sont plus utilisés car ils sont faciles à casser, par exemple avec [la cryptanalyse](http://practicalcryptography.com/ciphers/simple-substitution-cipher/#cryptanalysis). Vous pouvez trouver plus de détails sur cette [page wiki](https://en.wikipedia.org/wiki/Substitution_cipher).

Au début, nous étions trop excités par l'histoire pour nous concentrer sur les chiffres tout de suite. Nous avons simplement reconnu que les chiffres existaient et nous ne savions pas comment les déchiffrer. Je pensais que nous les casserions plus tard, mais...

Après un épisode, mon fils a eu une idée. Il voulait regarder l'introduction du spectacle à l'envers. J'ai pensé `pourquoi pas` ? Devinez quoi ! Lorsque vous le regardez à l'envers, à un moment donné, vous pouvez entendre un message caché :

**Trois lettres en arrière**

Hmm... `trois lettres en arrière`. Normalement, cela n'aurait aucun sens. Mais nous avions des chiffres que nous ne savions pas comment décoder. Pour nous, cela avait un sens parfait.

#### Bonjour Monsieur César

> Le chiffre de César est l'un des plus anciens et des plus simples chiffres connus. Il s'agit d'un type de chiffre de substitution dans lequel chaque lettre du texte en clair est « décalée » d'un certain nombre de places dans l'alphabet. Par exemple, avec un décalage de 1, A serait remplacé par B, B deviendrait C, et ainsi de suite. La méthode porte le nom de Jules César, qui l'utilisait apparemment pour communiquer avec ses généraux. Lisez plus [ici](http://practicalcryptography.com/ciphers/classical-era/caesar/).

J'ai imprimé l'alphabet anglais pour tout le monde depuis [ici](https://en.wikipedia.org/wiki/English_alphabet) et le déchiffrement a commencé :

`Z` → `W` parce que si nous reculons de `3` lettres à partir de `Z`, nous obtenons `W`
`H` → `E`
...
`B` → `Y` parce que si nous reculons de `1` lettre, nous obtenons `A` et les `2` suivantes, nous devons les `compter` à partir de la fin de l'alphabet, donc à la fin c'est `Y`

Après un moment, nous avons su que **ZHOFRPH WR JUDYLWB IDOOV** est en réalité **WELCOME TO GRAVITY FALLS.**

Mes enfants ont adoré.

Quand ils `déchiffraient` manuellement les messages suivants, j'ai pensé que c'était une grande opportunité de leur montrer ce que je fais au travail. D'une manière qui leur est plus facile à comprendre.

J'ai commencé un nouveau `Swift Playground` car il offre une excellente façon de travailler avec du code. Et j'ai commencé à coder. Je l'ai écrit juste pour le plaisir, alors s'il vous plaît ne jugez pas ?:

Quand le décodage manuel était terminé, je me suis assis avec mes enfants devant un ordinateur. J'ai expliqué que mon code faisait les mêmes choses qu'eux lorsqu'ils déchiffraient les messages. Mais au lieu de le faire manuellement, c'est automatique et peut être utilisé plusieurs fois. Ils n'ont pas compris le code, je serais surpris s'ils l'avaient fait, mais je suis presque sûr qu'ils ont compris `l'idée`.

#### KZKVI QZN WRKKVI HZBH : « ZFFTSDCJTSTZWHZWFS ! »

Tout allait bien jusqu'à l'épisode `7`. Nous avons commencé à décoder le premier mot et :
`KZKVI` → `HWHSF`
Oh-oh, notre chance venait de s'épuiser. Il était clair que le chiffre avait changé. Heureusement, il y avait un `indice` dans le message que nous avions déchiffré pour l'épisode `6` :

M. **CEASAR**IAN SERA ABSENT LA SEMAINE PROCHAINE M. **ATBASH** LE REMPLACERA

`Chiffre de César` → `Chiffre d'Atbash`

#### Bonjour Monsieur Atbash

> Le chiffre d'Atbash est un chiffre de substitution avec une clé spécifique où les lettres de l'alphabet sont inversées. C'est-à-dire que tous les `A` sont remplacés par des `Z`, tous les `B` sont remplacés par des `Y`, et ainsi de suite. Il était à l'origine utilisé pour l'alphabet hébreu, mais peut être utilisé pour n'importe quel alphabet. Lisez plus [ici](http://practicalcryptography.com/ciphers/classical-era/atbash-cipher/). Les chaînes chiffrées Atbash peuvent même être trouvées dans une Bible. Vous pouvez lire un peu plus à ce sujet [ici](https://www.gotquestions.org/Atbash-code.html).

Cette fois, c'était un peu plus long car nous devions vérifier l'index du caractère à partir du début, puis trouver la lettre avec cet index compté à partir de la fin de l'alphabet. Encore une fois, mes enfants déchiffraient cela manuellement :
`K` → `P` parce que l'index de `K` est `11` et lorsque nous comptons `11` à partir de la fin de l'alphabet, nous obtenons `P`
`Z` → `A`
`K` → `P`
`V` → `E`
`I` → `R`
`KZKVI` → `PAPER` Cela avait à nouveau du sens.

Après quelques minutes, ma fille s'est approchée de moi et m'a demandé si elle avait correctement déchiffré le message. Elle l'avait fait. Mais ce n'était pas le plus intéressant. J'ai remarqué qu'elle avait écrit quelque chose sur la page de l'alphabet imprimé. Au-dessus des index de l'alphabet `1, 2, 3, ..., 26`, elle a ajouté les numéros d'index inversés `26, 25, 24, ..., 1`.

Grâce à cela, elle n'a plus eu à compter à partir de la fin de l'alphabet. Nous, programmeurs, appelons cela `optimisation`. J'ai été impressionné qu'elle ait déjà commencé à améliorer son ensemble d'outils pour faciliter le travail. Encore une fois, j'ai préparé un petit morceau de code qui était capable de décoder les messages :

#### 14–5–24–20 21–16 : « 6–15–15–20–2–15–20 20–23–15 : 7–18–21–14–11–12–5'19 7–18–5–22–5–14–7–5 »

Tout allait bien jusqu'à l'épisode `14`. Ensuite, sans prévenir, le chiffre a changé à nouveau. Nous n'avons pas eu d'indice cette fois. Ou peut-être l'avons-nous simplement manqué ?

Eh bien... peut-être pas exactement sans aucun `indice`. Le plus grand nombre dans le texte chiffré était `24`, le plus petit était `2`. Les lettres de l'alphabet ont des index de `1` à `26`. Sur cette base, nous avons fait une supposition éclairée que :
`1` → `A`
`2` → `B`
...
`26` → `Z`

Quand `14–5–24–20` a été décodé en `NEXT`, nous avons su que notre supposition était correcte.

C'était un peu plus ennuyeux car je ne voulais pas supprimer de caractères du message une fois décodé. Si cela ne fonctionne pas pour vous, veuillez supprimer les caractères `non-alphanumériques` non pris en charge ou ajouter les caractères actuellement non pris en charge à `.replacingOccurrences`. Comme je l'ai dit. Ne jugez pas ?

#### 5–19–23–6–21–16 18–9–6 4–16–19 22–12–15–10–20–19–25–19

Nous avons échoué à nouveau lorsque nous avons essayé de déchiffrer le premier mot du message de l'épisode `20`.
`5–19–23–6–21–16` → `ESWFUP`

Le chiffre a changé. Mais nous n'avons pas abandonné facilement. Il y a un `indice` chiffré qui dit comment décoder ce message. Mais je vous laisse cela. C'est juste trop amusant de travailler sur ce genre de choses.

Veuillez noter que cette série compte `deux saisons` remplies de `mystères et de messages chiffrés`. Vous ne vous ennuierez pas.

#### La fin ?

Maintenant que je sais que mes enfants aiment jouer avec la cryptographie, j'ai quelques idées pour la `prochaine étape`. Ce n'est définitivement pas la dernière fois qu'ils travailleront avec des chiffres et des messages chiffrés.

Merci d'avoir lu ! J'espère avoir réussi à vous intéresser un peu avec cela. Si vous essayez vraiment cela avec vos enfants, ajoutez un commentaire à ce sujet. Je suis très curieux de savoir si c'était aussi amusant pour vous que pour nous.