---
title: Comment aborder n'importe quel entretien d'algorithme sans paniquer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T19:29:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-approach-any-algorithm-interview-without-panicking-b6d7ae5c050
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ltLHswL2X4LBTKWEQ2RXQw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: interview
  slug: interview
- name: jobs
  slug: jobs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment aborder n'importe quel entretien d'algorithme sans paniquer
seo_desc: 'By Sun-Li Beatteay

  Let’s be honest, algorithm problems are still very much a part of the job search.
  While there’s an ever-expanding list of companies that don’t make you jump through
  coding hoops, the average developer will encounter a live algorith...'
---

Par Sun-Li Beatteay

Soyons honnêtes, les problèmes d'algorithmes font toujours très beaucoup partie de la recherche d'emploi. Bien qu'il existe une [liste toujours croissante d'entreprises](https://github.com/poteto/hiring-without-whiteboards) qui ne vous font pas sauter à travers des cerceaux de codage, le développeur moyen rencontrera un défi d'algorithme en direct à un moment donné dans sa recherche d'emploi. Surtout si vous voulez travailler pour un Big Four ou une startup établie. Alors, à travers les cerceaux nous sautons.

Je n'ai pas besoin de parler de la façon dont les entretiens techniques peuvent être stressants. Je suis sûr que la plupart d'entre nous connaissent la frustration de sortir d'un entretien que nous venons de rater et de passer en revue toutes les façons dont nous aurions pu le retourner. Ce n'est pas une sensation agréable.

C'est pourquoi j'écris ceci. Pour ceux d'entre vous qui se retrouvent dans un défi d'algorithme, la façon dont vous l'abordez peut faire toute la différence. Êtes-vous le genre de personne qui plonge tête la première et qui comprend en cours de route ? Ou avez-vous un processus que vous suivez pour décomposer le problème en morceaux gérables ? Bien que la première méthode puisse fonctionner pour certains, je pratique la seconde.

Pour moi, avoir un ensemble d'étapes à utiliser pour décomposer un problème est crucial. Bien que cela ne me garantisse pas une solution ou une offre d'emploi, cela me permet de gérer ma réponse au stress. Garder ma panique à un niveau tolérable m'aide à me concentrer. Après tout, les entretiens techniques devraient être l'occasion de démontrer votre capacité à résoudre des problèmes — et non votre capacité à gérer plusieurs personnes qui vous jugent en silence sans vous évanouir.

Dans cet article, je veux vous montrer le processus que j'ai perfectionné à travers plusieurs écrans techniques et des dizaines d'entretiens simulés. Il est fortement influencé par le [système PEDAC de Launch School](https://medium.com/launch-school/solving-coding-problems-with-pedac-29141331f93f). Je l'utilise à chaque fois et il m'a bien servi.

> « Tombez amoureux du processus et les résultats viendront. » — Eric Thomas

La meilleure façon de montrer mon processus est de le démontrer en action. Alors, travaillons ensemble sur un problème. Et pour rendre cela aussi authentique que possible, je vais choisir un problème que je n'ai jamais résolu auparavant. Bien que vous devrez me croire sur parole.

Selon [Leetcode](https://leetcode.com/), l'algorithme [String to Integer](https://leetcode.com/problems/string-to-integer-atoi/) est une question d'entretien populaire. Il a également le taux de réussite le plus bas de tous les problèmes de niveau Moyen. Cela devrait être un bon défi.

J'ai également choisi ce problème car il est quelque peu pratique. Il s'agit d'un algorithme réel qui a été implémenté dans la plupart des langages de programmation. Contrairement à de nombreux autres défis d'entretien (je vous regarde [Coin Change](https://leetcode.com/problems/coin-change/)), les ingénieurs ont réellement utilisé cet algorithme dans la vie réelle.

Cela dit, plongeons-nous. N'hésitez pas à suivre dans le langage que vous voulez. J'utiliserai JavaScript. Vous pouvez essayer ma approche ou utiliser la vôtre. Voyez si vous pouvez même le résoudre avant moi à la fin de cet article. Vous pourriez vous retrouver à un pas de créer votre propre langage.

### Étape 1 : Reformuler le problème avec vos propres mots

![Image](https://cdn-media-1.freecodecamp.org/images/0*RLFsUv1fOvXw5omy)

Pour moi, c'est l'étape la plus importante. C'est l'occasion de poser des questions à mon interlocuteur pour clarifier les exigences et analyser toutes les informations cruciales. De plus, reformuler le problème avec mes propres mots me donne l'occasion de former un modèle mental et de digérer le problème.

Pour ce problème, une question que je poserais est de savoir si je suis autorisé à utiliser le transtypage. Bien que la description ne le précise pas, je n'utiliserai que le transtypage natif de JavaScript pour convertir un caractère à la fois. C'est le genre de restriction que je m'attendrais à trouver dans un véritable entretien.

Après avoir lu la description, voici les détails clés que j'ai identifiés.

```
// Étant donné une chaîne, retourner sa valeur numérique appropriée.
```

```
// Ignorer tous les espaces blancs au début de la chaîne.
```

```
// Le nombre peut commencer par un signe négatif ou positif.
```

```
// Tous les caractères qui viennent après le nombre doivent être ignorés.
```

```
// La chaîne est invalide si un caractère qui n'est pas un espace blanc ou un signe vient avant le nombre.
```

```
// Si la chaîne ne contient aucune valeur entière, elle est invalide.
```

```
// La valeur de retour pour toute chaîne invalide est 0.
```

```
// L'entier résultant ne peut pas être plus grand que (2^31) - 1 ou plus petit que -(2^31).
```

Rien que d'après ces exigences, je commence déjà à imaginer comment je vais créer cet algorithme. Il nécessitera probablement une boucle et beaucoup de logique conditionnelle.

Certaines personnes commenceraient probablement à coder après cette étape. Pour moi, il est encore un peu trop tôt pour formuler des plans concrets — mais mes engrenages tournent.

### Étape 2 : Types d'entrée et de sortie

Beaucoup de gens verront cela comme une étape inutile, mais je m'assure toujours de connaître les entrées et les sorties de l'algorithme. Soit sous forme de commentaire de code, soit dans le coin du tableau blanc.

Cela sert deux fonctions. Premièrement, cela solidifie les paramètres de ma fonction et à quoi ressemblera la signature. Leetcode a déjà créé la signature de la fonction pour moi, mais ce ne sera pas le cas dans un véritable entretien.

Deuxièmement, je garde un rappel des types avec lesquels je vais travailler. Il n'est pas rare qu'un candidat échoue à tous les cas de test parce qu'il a oublié de retourner une chaîne et non un tableau. Je peux ou non parler d'expérience...

Pour notre problème, les entrées et les sorties sont bien définies dans le titre.

```
Entrée : stringSortie : entier signé 32 bitsSignature : myAtoi(str)
```

### Étape 3 : Exemples et cas limites

![Image](https://cdn-media-1.freecodecamp.org/images/0*OcGarO2HdqOSlZIB.png)

Maintenant que je suis sûr des entrées et des sorties, je veux imaginer quelques cas de test. Ces exemples doivent couvrir tous les cas limites auxquels je peux penser. Je peux seulement imaginer le nombre de fois où un candidat a créé une solution fonctionnelle, pour que l'interviewer trouve un cas limite qu'il a manqué — causant l'effondrement de sa solution.

Il est possible que votre interview vous en fournisse certains, mais j'en inventerais encore plus — surtout s'ils ne sont pas exhaustifs. Par exemple, Leetcode m'a donné quelques cas de test décents.

```
Entrée : "4193 with words"Sortie : 4193
```

```
Entrée : "words and 987"Sortie : 0
```

```
Entrée : "-91283472332"Sortie : -2147483648
```

Cependant, ces exemples manquent certaines possibilités. Et si le nombre commence par un `+` ? Ou si plusieurs signes viennent avant un nombre, comme `-+-50` ?

Faisons de meilleurs exemples.

```
Entrée : "+50.890"Sortie : 50
```

```
Entrée : " -+100"Sortie : 0
```

```
Entrée : " !another invalid -10"Sortie : 0
```

### Étape 4 : Structure(s) de données

![Image](https://cdn-media-1.freecodecamp.org/images/0*RMV6tgCYXkYKvMMn.png)

La plupart, sinon tous, les défis de codage d'algorithmes impliquent l'utilisation d'une structure pour suivre vos données. Il est important de considérer quelle(s) structure(s) de données vous allez utiliser, car cela affectera votre implémentation.

Je sais d'après la description du problème que je vais traiter des chaînes et des entiers. Mais vais-je utiliser une autre structure de données pour aider à convertir de l'un à l'autre ?

Un problème que je peux déjà prévoir est de suivre les positions de chaque chiffre (dizaines, centaines, milliers, etc.). Puisque je ne connaîtrai pas la longueur de mon entier à l'avance, je vais utiliser un **tableau** pour suivre les caractères entiers. Le tableau servira de placeur intermédiaire pour chaque caractère avant qu'ils ne soient convertis en entier final.

Bien qu'il existe probablement une solution plus efficace en termes d'espace, je peux optimiser ma solution plus tard. Pour l'instant, je veux simplement choisir ce qui a le plus de sens pour moi. Il est préférable d'obtenir une solution naïve fonctionnelle que de viser la lune et de ne rien terminer.

### Étape 5 : Pseudocode

![Image](https://cdn-media-1.freecodecamp.org/images/1*88cH0lTO7R2ypVsg0FDJsw.png)

Mon avant-dernière étape consiste à passer du temps à esquisser mon algorithme en pseudocode. Les interviewers veulent voir comment vous pensez et abordez les problèmes. Le pseudocode est parfait pour cela.

Un avantage supplémentaire est que l'interviewer saura comment vous aider à l'avance. Il y a eu des fois où je me suis retrouvé bloqué sur un problème, pour que mon interview me donne des indices subtils pour me faire avancer. Si vous plongez dans le codage sans plan, vous pourriez finir par vous confondre, vous et votre interview. Faites-vous une faveur à chacun et créez un plan d'action.

Voici ce que j'ai imaginé.

```
// Commencer avec index = 0
```

```
// Tant que le caractère à l'index actuel est un espace blanc  // incrémenter l'index
```

```
// Vérifier si le caractère suivant est invalide  // retourner 0
```

```
// Vérifier si le caractère suivant est un signe positif ou négatif  // Si signe négatif, marquer le nombre comme négatif  // incrémenter l'index
```

```
// Boucler à travers les caractères en commençant à l'index actuel  // Si le caractère actuel est un entier    // Unshift au début du tableau    // Incrémenter l'index  // Sinon, sortir de la boucle
```

```
// Boucler à travers le tableau de caractères de la chaîne   // Transtyper le caractère de la chaîne en entier  // Multiplier l'entier par (10^index) et ajouter à la valeur de retour
```

```
// Si la chaîne contenait un signe négatif, multiplier la valeur du résultat par -1// Si la valeur du résultat est inférieure au minimum, réassigner au minimum// Si la valeur du résultat est supérieure au maximum, réassigner au maximum
```

```
// retourner la valeur
```

Il peut sembler que j'ai inventé cela de nulle part, mais il y a eu beaucoup de délibération et d'essais et d'erreurs derrière la scène. C'est l'étape la plus chronophage car c'est là que l'algorithme est créé.

Lisez les exigences, les entrées/sorties et les cas limites. Posez des questions, clarifiez les concepts et isolez les zones d'incertitude pour vous concentrer. Trouvez la solution la plus simple à laquelle vous pouvez penser et travaillez à partir de là.

Aurez-vous besoin d'une recherche en profondeur d'abord ? D'une fenêtre glissante ? Diviser pour mieux régner ? Autre chose ?

Si c'est l'étape qui vous pose le plus de problèmes, ne vous inquiétez pas. Cela deviendra plus facile avec la pratique. Et pratiquez-vous. Une conception d'algorithme approfondie en pseudocode rendra l'étape suivante rapide et facile.

### Étape 6 : Code !

« **Enfin !** » Vous pensez probablement. « **Cela a pris une éternité !** »

En effet, je passe beaucoup de temps en mode planification. Si un interview me donne 45 minutes pour finir, je passerai 15-30 minutes à réfléchir et à digérer mentalement.

> « Donnez-moi six heures pour abattre un arbre et je passerai les quatre premières à aiguiser la hache. » — Abraham Lincoln

En fait, le codage est l'étape la moins importante pour moi. Tout le travail difficile a déjà été fait. Maintenant, je dois simplement interpréter mon modèle mental en code.

De plus, la façon dont je code cette solution dans un cadre d'entretien ne sera pas la même que la façon dont je la code dans la vie réelle. En fait, une solution d'entretien réelle serait différente de la réponse que j'ai trouvée pour cet article. Plusieurs facteurs affectent la façon dont je code dans un entretien, comme le temps et la réactivité de l'interviewer.

Sans accès à Google ou suffisamment de temps pour refactoriser, je veux simplement écrire quelque chose qui fonctionne. Et il n'y a aucune garantie que j'y parviendrais.

Mais ce n'est pas le but de cet article. Oui, il est possible que je n'aurais pas résolu cette question dans un entretien. Mais jusqu'à présent, j'ai déstructuré le défi en ses composants clés. Je sais que je _peux_ le résoudre et je me suis mis dans la meilleure position pour le faire. Un bon interview verra cela.

Dans un écran technique ou sur place, ce n'est pas le code qui compte. C'est la façon dont vous y arrivez.

Si vous êtes intéressé à comparer les solutions, voici celle que j'ai trouvée :

Cette solution n'est pas la plus efficace. Selon Leetcode, elle ne bat que 25 % des autres soumissions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8SAs6MGc9y2xNx4j7EjJ3Q.png)

Cependant, elle passerait la plupart des entretiens techniques. Un interview pourrait me demander de l'optimiser pour l'espace ou le temps, mais ce sont des choses qui peuvent être incluses dans des itérations ultérieures si le temps le permet. Vous n'avez pas besoin de les trouver du premier coup.

Le but d'utiliser un processus est d'avoir une approche systémique pour décomposer n'importe quel défi. Cela fonctionne que vous l'utilisiez dans votre travail au quotidien ou dans un entretien technique. En l'utilisant dans un entretien, vous pouvez garder votre panique à distance en vous concentrant sur le défi et non sur vos émotions.

Si vous n'avez pas de processus, commencez à en créer un. Vous pouvez utiliser [PEDAC](https://medium.com/launch-school/solving-coding-problems-with-pedac-29141331f93f) ou développer le vôtre. Assurez-vous simplement qu'il vous aide à créer des solutions dont vous êtes confiant.

Par exemple, vous avez peut-être remarqué l'utilisation de constantes, de fonctions d'aide et de regex dans ma solution. Ce sont toutes des astuces que j'ai apprises et qui m'aident à isoler la complexité dans un entretien. Plus mon code ressemble à l'anglais, moins je suis confus en l'écrivant, et plus je travaille vite. Cela peut être un peu verbeux, mais j'aime ça. Faites ce qui fonctionne pour vous.

Si vous avez déjà une procédure que vous utilisez, pratiquez et perfectionnez-la. N'attendez pas jusqu'à votre entretien sur place pour commencer à l'affiner. Expérimentez dans des entretiens simulés. [Pramp](https://www.pramp.com/#/) et [Interviewing.io](https://interviewing.io/) sont des outils parfaits pour cela.

Rappelez-vous, si tout le reste échoue, faites confiance au processus.

Si cet article a résonné avec vous, laissez quelques applaudissements ? !

Comme toujours, bon codage !