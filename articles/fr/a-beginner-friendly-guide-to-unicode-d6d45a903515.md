---
title: Un guide pour débutants sur Unicode en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T23:51:28.000Z'
originalURL: https://freecodecamp.org/news/a-beginner-friendly-guide-to-unicode-d6d45a903515
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2TiN1yOMlCq2fyqQTqgt-w.jpeg
tags:
- name: emoji
  slug: emoji
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
- name: unicode
  slug: unicode
seo_title: Un guide pour débutants sur Unicode en Python
seo_desc: 'By Jimmy Zhang

  I once spent a couple of frustrating days at work learning how to properly deal
  with Unicode strings in Python. During those two days, I ate a lot of snacks — roughly
  one bag of goldfish per one of these errors encountered, which shoul...'
---

Par Jimmy Zhang

J'ai déjà passé quelques jours frustrants au travail à apprendre comment gérer correctement les chaînes Unicode en Python. Pendant ces deux jours, j'ai mangé beaucoup de snacks — environ un sac de goldfish par erreur rencontrée, ce qui devrait être trop familier pour ceux qui programment avec Python :

```
UnicodeDecodeError: le codec 'ascii' ne peut pas décoder le byte 0xf0 en position 0 : ordinal not in range(128)
```

En résolvant mon problème, j'ai fait beaucoup de recherches sur Google, ce qui m'a dirigé vers [quelques](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) [articles](https://nedbatchelder.com/text/unipain.html) [indispensables](https://betterexplained.com/articles/unicode/) [sur le sujet](http://www.pgbovine.net/unicode-python.htm). Mais aussi excellents soient-ils, ils ont tous été écrits sans l'aide d'un aspect crucial de la communication à l'ère moderne.

C'est-à-dire : ils ont tous été écrits sans l'aide des emojis.

Ainsi, pour tirer parti de cette situation, j'ai décidé d'écrire mon propre guide pour comprendre Unicode, avec plein de visages et d'icônes rendus tout au long du chemin ?f44b?.

Avant de plonger dans les détails techniques, commençons par une question amusante. Quel est votre emoji préféré ?

Le mien est le « [visage avec la bouche ouverte](https://emojipedia.org/face-with-open-mouth/) », qui ressemble à ceci ? — avec une réserve majeure. Ce que vous voyez dépend en réalité de la plateforme que vous utilisez pour lire cet article !

Vu sur mon Mac, l'emoji ressemble à une boule de bowling jaune. Sur ma tablette Samsung, les yeux sont noirs et circulaires, accentués par un point blanc qui trahit une plus grande profondeur d'émotion.

Copiez et collez l'emoji (?) dans Twitter, et vous verrez quelque chose de complètement différent. Copiez et collez-le dans messenger.com, cependant, et vous verrez pourquoi c'est mon préféré.

???? Pourquoi sont-ils tous différents ?

![Image](https://cdn-media-1.freecodecamp.org/images/xcqApm6uLo00aEV6quvQz5hbv0SMFnrxJwPc)

![Image](https://cdn-media-1.freecodecamp.org/images/xBNeNbexzlYavyagf0TqljD-3nGKVgBSqdtD)

![Image](https://cdn-media-1.freecodecamp.org/images/hj38DT5kCCXEAlXuor1E1JLjTtPBQtVKlaun)
_De gauche à droite : Apple, Samsung, messenger.com ([source](https://emojipedia.org/face-with-open-mouth/" rel="noopener" target="_blank" title="))._

Note : À partir du 9 juillet 2018, Messenger semble avoir mis à jour ses icônes d'emoji, donc l'icône en haut à droite ne s'applique plus. ?

Ce petit mystère amusant est notre transition vers le monde d'Unicode, car les emojis font partie du [Standard Unicode](https://emojipedia.org/unicode-6.0/) depuis 2010. En plus de nous donner des emojis, Unicode est important car c'est le choix préféré d'Internet pour l'encodage, la représentation et la gestion cohérents du texte.

### Unicode et Encodage : Un Bref Aperçu

Comme pour de nombreux sujets, la meilleure façon de comprendre Unicode est de connaître le contexte entourant sa création — et pour cela, l'article de Joel Spolsky est une lecture obligatoire.

#### Points de Code

Maintenant que nous sommes entrés dans le monde d'Unicode, nous devons d'abord dissocier les emojis des icônes merveilleusement expressives qu'ils sont, et les associer à quelque chose de beaucoup moins excitant. Ainsi, au lieu de penser aux emojis en termes des choses ou des émotions qu'ils représentent, nous penserons plutôt à chaque emoji comme un simple nombre. Ce nombre est connu sous le nom de **point de code**.

Les points de code sont le [concept clé d'Unicode](https://www.unicode.org/standard/standard.html), qui a été « conçu pour soutenir l'échange, le traitement et l'affichage mondiaux des textes écrits des diverses langues... du monde moderne. » Il le fait en associant pratiquement chaque caractère imprimable à un point de code unique. Ensemble, ces caractères constituent le **jeu de caractères** Unicode.

Les points de code sont généralement écrits en hexadécimal et préfixés avec `U+` pour désigner la connexion à Unicode, représentant des caractères provenant de :

* langues exotiques telles que le [Telugu](https://en.wikipedia.org/wiki/Telugu_(Unicode_block)) [f44b | point de code : U+0C0B]
* [symboles d'échecs](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) [f44b | point de code : U+2656]
* et, bien sûr, [emojis](https://en.wikipedia.org/wiki/Emoticons_(Unicode_block)) [? | point de code : U+1F64C]

#### Les Glyphes sont Ce que Vous Voyez

La représentation réelle à l'écran des points de code est appelée **glyphe** (la cartographie complète des points de code aux glyphes est connue sous le nom de **police**).

Par exemple, prenez cette lettre A, qui est le point de code `U+0041` dans Unicode. Le « A » que vous voyez avec vos yeux est un glyphe — il a cette apparence parce qu'il est rendu avec la police de Medium. Si vous changiez la police pour, par exemple, Times New Roman, seul le glyphe de « A » changerait — le point de code sous-jacent ne changerait pas.

![Image](https://cdn-media-1.freecodecamp.org/images/TUckLVh6eCihRLcdZhfa3l8qIE6IuxmCvLxY)
_Les polices mappent le même point de code à différents glyphes_

Les glyphes sont la réponse à notre petit mystère de rendu. Sous le capot, toutes les variations de l'emoji « visage avec la bouche ouverte » pointent vers le même point de code, `U+1F62E`, mais le **glyphe** qui le représente varie selon la plateforme ?.

#### Les Points de Code sont des Abstractions

Parce qu'ils ne disent rien sur la façon dont ils sont rendus visuellement (nécessitant une police et un glyphe pour les « donner vie »), les points de code sont considérés comme une abstraction.

Mais tout comme les points de code sont une abstraction pour les utilisateurs finaux, ils sont également des abstractions pour les ordinateurs. Cela est dû au fait que les points de code nécessitent un **encodage de caractères** pour les convertir en la seule chose que les ordinateurs peuvent interpréter : les octets. Une fois convertis en octets, les points de code peuvent être enregistrés dans des fichiers ou envoyés sur le réseau à un autre ordinateur ?f680?.

UTF-8 est actuellement l'[encodage de caractères le plus populaire au monde](https://en.wikipedia.org/wiki/UTF-8#/media/File:Utf8webgrowth.svg). UTF-8 utilise un ensemble de règles pour convertir un point de code en une séquence unique de (1 à 4) octets, et vice versa. Les points de code sont dits **encodés** en une séquence d'octets, et les séquences d'octets sont **décodées** en points de code. [Ce post Stack Overflow](https://stackoverflow.com/questions/1543613/how-does-utf-8-variable-width-encoding-work) explique comment fonctionne l'algorithme d'encodage UTF-8.

Cependant, même si UTF-8 est l'encodage de caractères prédominant dans le monde, il est loin d'être le seul. Par exemple, UTF-16 est un encodage de caractères alternatif du jeu de caractères Unicode. L'image ci-dessous compare les encodages UTF-8 et UTF-16 de notre emoji ?.

![Image](https://cdn-media-1.freecodecamp.org/images/k1TgNZ8m7zeByOT1BLyLSD8F7NBESOp7WLQO)

Des problèmes surviennent lorsqu'un ordinateur encode des points de code en octets avec un encodage, et qu'un autre ordinateur (ou un autre processus sur le même ordinateur) décode ces octets avec un autre encodage.

Heureusement, UTF-8 est suffisamment omniprésent pour que, dans la plupart des cas, nous n'ayons pas à nous soucier des encodages de caractères incompatibles. Mais lorsqu'ils se produisent, une familiarité avec les concepts mentionnés ci-dessus est nécessaire pour se sortir du pétrin.

#### Récapitulatif

* Unicode est une collection de **points de code**, qui sont des nombres simples généralement écrits en hexadécimal et préfixés avec `U+`. Ces points de code mappent à pratiquement tous les caractères imprimables des langues écrites du monde entier.
* Les **glyphes** sont la manifestation physique d'un caractère. Ce gars ? est un glyphe. Une **police** est une cartographie des points de code aux glyphes.
* Afin de les envoyer sur le réseau ou de les enregistrer dans un fichier, les caractères et leurs points de code sous-jacents doivent être encodés en octets. Un **encodage de caractères** contient les détails de la manière dont un point de code est intégré dans une séquence d'octets.
* **UTF-8** est actuellement l'encodage de caractères le plus populaire au monde. Étant donné un point de code, UTF-8 l'**encode** en une séquence d'octets. Étant donné une séquence d'octets, UTF-8 la **décode** en un point de code.

### Un Exemple Pratique

Le rendu correct des caractères Unicode implique de parcourir une chaîne, allant des octets aux points de code jusqu'aux glyphes.

![Image](https://cdn-media-1.freecodecamp.org/images/4EWd0DC-ca2Xc-KykyfW7iVAHJhe6SjGG2Vx)

Utilisons maintenant un éditeur de texte pour voir un exemple pratique de cette chaîne — ainsi que les types de problèmes qui peuvent survenir lorsque les choses tournent mal. Les éditeurs de texte sont parfaits, car ils impliquent les trois parties de la chaîne de rendu montrée ci-dessus.

Note : L'exemple suivant a été réalisé sur mon MacOS en utilisant Sublime Text 3. Et pour donner crédit là où il est dû : le début de cet exemple est fortement inspiré de [cet article](http://pgbovine.net/unicode-python.htm) de Philip Guo, qui m'a introduit à la commande `hexdump` (et bien plus encore).

Nous commencerons avec un fichier texte contenant un seul caractère — mon emoji préféré « visage avec la bouche ouverte ». Pour ceux qui veulent suivre, j'ai hébergé ce fichier dans un Github [gist](https://gist.githubusercontent.com/jzhang621/d7d9eb167f25084420049cb47510c971/raw/e35f9669785d83db864f9d6b21faf03d9e51608d/emoji.txt), que vous pouvez obtenir localement avec `curl`.

```
curl https://gist.githubusercontent.com/jzhang621/d7d9eb167f25084420049cb47510c971/raw/e35f9669785d83db864f9d6b21faf03d9e51608d/emoji.txt > emoji.txt
```

Comme nous l'avons appris, pour qu'il soit enregistré dans un fichier, l'emoji a été encodé en octets en utilisant un encodage de caractères. Ce fichier particulier a été encodé en utilisant UTF-8, et nous pouvons utiliser la commande `hexdump` pour examiner le contenu réel des octets du fichier.

```
j|encoding: hexdump emoji.txt0000000 f0 9f 98 ae 0000004
```

La sortie de `hexdump` nous indique que le fichier contient 4 octets au total, chacun étant écrit en hexadécimal. La séquence d'octets réelle `f0 9f 98 ae` correspond à la séquence d'octets encodée en UTF-8 attendue, comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/zRTpkcw12y2aFQOJyfTARuWgucf0CobcaKzf)
_Source : [http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input=%F0%9F%98%AE&amp;mode=char](http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input=%F0%9F%98%AE&amp;mode=char" rel="noopener" target="_blank" title=")_

Maintenant, ouvrons notre fichier dans Sublime Text, où nous devrions voir notre seul caractère ?. Puisque nous voyons le glyphe attendu, nous pouvons supposer que Sublime Text a utilisé le bon encodage de caractères pour décoder ces octets en points de code. Confirmons en ouvrant la console `Affichage -> Afficher la Console`, et en inspectant l'objet `view` que Sublime Text expose dans le cadre de son API Python.

```
>>> view<sublime.View object at 0x1112d7310>
```

```
# retourne l'encodage actuellement associé au fichier>>> view.encoding()'UTF-8'
```

Avec un peu de connaissances en Python, nous pouvons également trouver le point de code Unicode associé à notre emoji :

```
# Retourne le caractère à la position donnée>>> view.substr(0)'?' 
```

```
# ord retourne un entier représentant le point de code Unicode du caractère (docs)>>> ord(view.substr(0))128558
```

```
# convertir le point de code en hexadécimal, et formater avec U+>>> print('U+%x' % ord(view.substr(0)))U+1f62e
```

Encore une fois, comme nous l'attendions. Cela illustre un parcours complet de la chaîne de rendu Unicode, qui a impliqué :

* la lecture du fichier comme une séquence d'octets encodés en UTF-8.
* le décodage des octets en un point de code Unicode.
* le rendu du glyphe associé au point de code.

![Image](https://cdn-media-1.freecodecamp.org/images/tgfnKyW9kpVCBK4tkSwTiDncDR9-COPmFpw5)
_Le glyphe réel que vous voyez dépend de la plateforme._

Jusqu'à présent, tout va bien ?.

#### Différents Octets, Même Emoji

En plus d'être mon éditeur de texte préféré, j'ai choisi Sublime Text pour cet exemple car il permet une expérimentation facile avec les encodages de caractères.

Nous pouvons maintenant enregistrer le fichier en utilisant un encodage de caractères différent. Pour ce faire, cliquez sur `Fichier -> Enregistrer avec Encodage -> UTF-16 BE`. (Très brièvement, UTF-16 est un encodage de caractères alternatif du jeu de caractères Unicode. Au lieu d'encoder les caractères les plus courants en utilisant un octet, comme UTF-8, UTF-16 encode chaque point de 1 à 65536 en utilisant deux octets. Les points de code supérieurs à 65536, comme notre emoji, sont encodés en utilisant des paires de substitution. BE signifie Big Endian).

Lorsque nous utilisons `hexdump` pour inspecter le fichier à nouveau, nous voyons que le contenu des octets a changé.

```
# (avant : UTF-8)j|encoding: hexdump emoji.txt0000000 f0 9f 98 ae 0000004
```

```
# (après : UTF-16 BE)j|encoding: hexdump emoji.txt0000000 d8 3d de 2e0000004
```

De retour dans Sublime Text, nous voyons toujours le même caractère ? qui nous regarde. Enregistrer le fichier avec un encodage de caractères différent a peut-être changé le contenu réel du fichier, mais cela a également mis à jour la représentation interne de Sublime Text de la manière d'interpréter ces octets. Nous pouvons confirmer en ouvrant à nouveau la console.

```
>>> view.encoding()'UTF-16 BE'
```

À partir de là, tout le reste est identique.

```
>>> view.substr(0)'?' 
```

```
>>> ord(view.substr(0))128558
```

```
>>> print('U+%x' % ord(view.substr(0)))U+1f62e
```

Les octets ont peut-être changé, mais le point de code n'a pas changé — et l'emoji reste le même.

#### Même Octets, Mais Qu'est-ce que f44bf44bf44bf44b

Il est temps de s'amuser un peu avec l'encodage. D'abord, ré-encodons notre fichier en utilisant UTF-8, car cela fait un meilleur exemple.

Allons-y et utilisons Sublime Text pour rouvrir un fichier existant en utilisant un encodage de caractères différent. Sous `Fichier -> Rouvrir avec Encodage`, cliquez sur Vietnamien (Windows 1258), ce qui transforme notre caractère emoji en les quatre caractères suivants qui n'ont pas de sens : f44bf44bf44bf44b.

Lorsque nous cliquons sur « Rouvrir avec Encodage », nous ne changeons pas le contenu réel des octets du fichier, mais plutôt la manière dont Sublime Text interprète ces octets. Hexdump confirme que les octets sont les mêmes :

```
j|encoding: hexdump emoji.txt0000000 f0 9f 98 ae0000004
```

Pour comprendre pourquoi nous voyons ces caractères qui n'ont pas de sens, nous devons consulter la [page de code Windows-1258](https://en.wikipedia.org/wiki/Windows-1258), qui est une cartographie des octets vers un jeu de caractères de la langue vietnamienne. (Pensez à une page de code comme la table produite par un encodage de caractères). Comme cette page de code contient un jeu de caractères de moins de 255 caractères, chaque point de code de caractère peut être exprimé comme un nombre décimal entre 0 et 255, qui à son tour peut tous être encodé en utilisant 1 octet.

![Image](https://cdn-media-1.freecodecamp.org/images/fvczjUIBIrUtsDTPr08NIdXLJqb9hjn6Hdd0)
_La page de code Windows-1258, qui mappe les points de code décimaux aux caractères de la langue vietnamienne. Tiré de Wikipedia, avec un style personnalisé appliqué pour montrer les 4 points de code pertinents pour cet exemple._

Parce que notre seul emoji ? nécessite 4 octets pour être encodé en utilisant UTF-8, nous voyons maintenant 4 caractères lorsque nous interprétons le fichier avec l'encodage Windows-1258.

![Image](https://cdn-media-1.freecodecamp.org/images/04v6iTqdJ7XiQfOMQxUtJMwto3JPS8gWcRZk)

Un mauvais choix d'encodage de caractères a un impact direct sur ce que nous pouvons voir et comprendre en brouillant les caractères en un méli-mélo incompréhensible.

![Image](https://cdn-media-1.freecodecamp.org/images/lYN9Y31uDX5NwCb3ihQLoplb7e19gCepIxKf)

Maintenant, passons à la partie « amusante », que j'inclus pour ajouter un peu de couleur à Unicode et à la raison de son existence. Avant Unicode, il existait de nombreuses pages de code différentes telles que Windows-1258, chacune avec une manière différente de mapper 1 octet de données en 255 caractères. **Unicode a été créé afin d'incorporer tous les différents caractères de toutes les différentes pages de code en un seul système**. En d'autres termes, Unicode est un sur-ensemble de Windows-1258, et chaque caractère de la page de code Windows-1258 a un [équivalent Unicode](https://stackoverflow.com/a/3441690/1586242).

![Image](https://cdn-media-1.freecodecamp.org/images/PzRE5GqbSr6PLTSxNg2I3B5zeeRFfgVFCOBT)
_Les équivalents Unicode pour chaque caractère sont listés sur la ligne du milieu de chaque cellule ([Wikipedia](https://en.wikipedia.org/wiki/Windows-1258" rel="noopener" target="_blank" title="))_

En fait, ces équivalents Unicode sont ce qui permet à Sublime Text de convertir entre différents encodages de caractères d'un simple clic de bouton. En interne, Sublime Text représente toujours chacun de nos caractères « décodés Windows-1258 » comme un point de code Unicode, comme nous le voyons ci-dessous lorsque nous ouvrons la console :

```
>>> view.encoding()'Vietnamese (Windows 1258)'
```

```
# Les chaînes Python 3 sont des "séquences immuables de points de code Unicode">>> type(view.substr(0))<class 'str'>
```

```
>>> view.substr(0)'f44b'>>> view.substr(1)'f44b'>>> view.substr(2)'f44b'>>> view.substr(3)'f44b'
```

```
>>> ['U+%04x' % ord(view.substr(x)) for x in range(0, 4)]['U+0111', 'U+0178', 'U+02dc', 'U+00ae']
```

Cela signifie que nous pouvons réenregistrer nos 4 caractères qui n'ont pas de sens en utilisant UTF-8. Je vous laisse faire cela — si vous le faites, et que vous pouvez prédire correctement le `hexdump` résultant du fichier, alors vous avez réussi à comprendre les concepts clés derrière Unicode, les points de code et les encodages de caractères. ([Utilisez cette page de code UTF-8](https://www.utf8-chartable.de/unicode-utf8-table.pl?number=512). La réponse peut être trouvée à la toute fin de cet article. ).

### Conclusion

Travailler efficacement avec Unicode implique de toujours savoir à quel niveau de la chaîne de rendu vous opérez. Cela signifie toujours se demander : qu'est-ce que j'ai ? Sous le capot, les glyphes ne sont rien d'autre que des points de code. Si vous travaillez avec des points de code, sachez que ces points de code doivent être encodés en octets avec un encodage de caractères. Si vous avez une séquence d'octets représentant du texte, sachez que ces octets sont sans signification sans connaître l'encodage de caractères qui a été utilisé pour créer ces octets.

Comme pour tout sujet en informatique, la meilleure façon d'apprendre Unicode est d'expérimenter. Saisissez des caractères, jouez avec les encodages de caractères et faites des prédictions que vous vérifiez en utilisant `hexdump`. Bien que j'espère que cet article explique tout ce que vous devez savoir sur Unicode, je serai plus que ravi s'il vous prépare simplement à mener vos propres expériences.

Merci d'avoir lu ! ?

#### Réponse :

```
j|encoding: $ hexdump emoji.txt0000000 c4 91 c5 b8 cb 9c c2 ae0000008
```