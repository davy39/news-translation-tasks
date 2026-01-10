---
title: Comment utiliser RegEx pour correspondre aux emojis - Tutoriel sur les expressions
  régulières des emotes Discord
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2022-07-13T23:04:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-regex-to-match-emoji-including-discord-emotes
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-roman-odintsov-6898861.jpg
tags:
- name: discord
  slug: discord
- name: emoji
  slug: emoji
- name: Regex
  slug: regex
- name: unicode
  slug: unicode
seo_title: Comment utiliser RegEx pour correspondre aux emojis - Tutoriel sur les
  expressions régulières des emotes Discord
seo_desc: "Emoji are special Unicode characters that render pictographs. But these\
  \ characters can be very tricky to identify with regular expressions (RegEx). \n\
  I was recently working on a Discord bot that had to detect the number of emotes\
  \ in a given message. T..."
---

Les emojis sont des caractères Unicode spéciaux qui affichent des pictogrammes. Mais ces caractères peuvent être très difficiles à identifier avec des expressions régulières (RegEx).

Je travaillais récemment sur un bot Discord qui devait détecter le nombre d'emotes dans un message donné. Aujourd'hui, je vais partager mon processus avec vous, y compris la nouvelle fonctionnalité JavaScript RegEx qui a finalement résolu les problèmes que je rencontrais.

## Comment fonctionnent les emojis Unicode

Le Consortium Unicode définit des codes de caractères spécifiques pour chaque emoji. Ils maintiennent même un [tableau d'emojis utile](https://unicode.org/emoji/charts/full-emoji-list.html) comme référence. Par exemple, `U+1F600` correspond à l'emoji 😀.

Certains emojis se composent de plusieurs caractères Unicode. Cela est le plus courant avec les emojis de drapeaux, qui se composent des "indicateurs régionaux" formant le code de pays à deux lettres du pays.

Cela signifie que le drapeau des États-Unis, 🇺🇸, se compose des deux caractères Unicode `U+1F1FA` et `U+1F1F8`, qui correspondent aux indicateurs régionaux `U` et `S`.

> Comme anecdote amusante, c'est à l'OS de déterminer **comment** afficher un emoji. Si vous êtes sur Windows, par exemple, vous ne verrez pas un drapeau ci-dessus. Vous verrez `US`.

## Qu'est-ce que les emotes Discord ?

L'une des nombreuses fonctionnalités de Discord est de permettre aux communautés de télécharger leurs propres emotes personnalisés. Ces emotes sont identifiés par un nom et sont utilisés avec la syntaxe `:nom_emote:`.

Cependant, la manière dont ils sont identifiés par le client/API est différente. Chaque emote a un identifiant unique et ils sont envoyés dans le contenu du message sous la forme `<:nom_emote:1234567890>`, ou `<a:nom_emote:1234567890>` pour les emotes animés.

Vous pouvez voir cela dans Discord en mettant une barre oblique inverse `\` avant l'emote et en l'envoyant. Il affichera quelque chose comme ceci :

![Un message Discord montrant la valeur brute d'un emote `<:NaomiGrin:938275644092063784>`](https://www.freecodecamp.org/news/content/images/2022/07/image-162.png)

## Comment faire correspondre les emojis et les emotes avec RegEx

Mon approche initiale avait deux phrases RegEx différentes.

J'utilisais `/(<a?)?:\w+:(\d{18}>)?/g` pour capturer les emotes Discord. Cette RegEx captait avec succès les emotes Discord, ce qui était génial !

Je l'ai associée à `/:[^:\s]*(?:::[^:\s]*)*:/g` pour faire correspondre les emojis Unicode, ce qui ne fonctionnait que partiellement. Le problème ici était que je voyais certains emotes comptés deux fois – parce que la RegEx Discord les captait. Et d'autres étaient complètement manqués.

Alors, avec RegEx étant ce qu'il est, j'ai essayé de le rendre plus complexe. `<:[^:\s]+:\d+>|<a:[^:\s]+:\d+>|(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff]|\ufe0f)/g` était un peu plus réussi pour faire correspondre les emojis intégrés, mais ce n'était toujours pas parfait. Cette RegEx était conçue pour faire correspondre des caractères unicode spécifiquement.

J'ai joué avec la suppression des espaces blancs, en utilisant le caractère de limite de mot `\b`, et quelques autres ajustements, avant de finalement abandonner et de faire quelques recherches.

Et puis j'ai découvert les [Unicode Property Escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Unicode_Property_Escapes). Cette fonctionnalité RegEx vous permet d'ajouter le drapeau `u` à votre RegEx, déverrouillant les propriétés Unicode désignées par le caractère `\p`.

Avec quelques recherches supplémentaires, j'ai pu trouver les [propriétés des caractères Emoji](https://unicode.org/reports/tr51/#Emoji_Properties) – spécifiquement, la propriété `Extended_Pictograph`. Cela m'a permis de mettre à jour la RegEx à une valeur finale et fonctionnelle :

```js
/<a?:.+?:\d{18}>|\p{Extended_Pictographic}/gu
```

La propriété `\p{Extended_Pictographic}` semble correspondre aux emojis Unicode ainsi qu'aux modificateurs de caractères (souvent utilisés pour les tons de peau dans les emojis).

## Conclusion

Cette RegEx est actuellement en cours d'exécution dans mon code de production et n'a pas encore montré de problèmes.

J'espère que cet article vous a aidé. Si vous êtes intéressé à explorer davantage les Unicode Property Escapes, le Consortium Unicode offre une [liste complète](https://www.unicode.org/Public/UCD/latest/ucd/PropertyValueAliases.txt) des valeurs disponibles.

Bon codage !