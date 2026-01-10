---
title: Une introduction à l'étiquetage des parties du discours et au modèle de Markov
  caché
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T19:31:14.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-part-of-speech-tagging-and-the-hidden-markov-model-953d45338f24
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f6e0uf5PX17pTceYU4rbCA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction à l'étiquetage des parties du discours et au modèle de
  Markov caché
seo_desc: 'By Divya Godayal

  by Sachin Malhotra and Divya Godayal


  _Source: [https://english.stackexchange.com/questions/218058/parts-of-speech-and-functions-bob-made-a-book-collector-happy-the-other-day](https://english.stackexchange.com/questions/218058/parts-...'
---

Par Divya Godayal

_par [Sachin Malhotra](https://medium.com/@sachinmalhotra) et [Divya Godayal](https://medium.com/@divyagodayal)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*f6e0uf5PX17pTceYU4rbCA.jpeg)
_Source : [https://english.stackexchange.com/questions/218058/parts-of-speech-and-functions-bob-made-a-book-collector-happy-the-other-day](https://english.stackexchange.com/questions/218058/parts-of-speech-and-functions-bob-made-a-book-collector-happy-the-other-day" rel="noopener" target="_blank" title=")_

Retournons à l'époque où nous n'avions pas de langage pour communiquer. La seule façon dont nous disposions était le langage des signes. C'est ainsi que nous communiquons généralement avec notre chien à la maison, n'est-ce pas ? Lorsque nous lui disons : « Nous t'aimons, Jimmy », il répond en remuant la queue. Cela ne signifie pas qu'il sait ce que nous disons réellement. Au contraire, sa réponse est simplement parce qu'il comprend le langage des émotions et des gestes plus que les mots.

En tant qu'êtres humains, nous avons développé une compréhension de nombreuses nuances de la langue naturelle plus que tout autre animal sur cette planète. C'est pourquoi lorsque nous disons « Je t'AIME, chéri » ou « Faisons l'AMOUR, chéri », nous voulons dire des choses différentes. Puisque nous comprenons la différence de base entre les deux phrases, nos réponses sont très différentes. Ce sont ces mêmes intrications dans la compréhension du langage naturel que nous voulons enseigner à une machine.

Ce que cela pourrait signifier, c'est que lorsque votre futur chien robot entendra « Je t'aime, Jimmy », il saura que AIME est un verbe. Il réalisera également que c'est une émotion que nous exprimons et à laquelle il répondra d'une certaine manière. Et peut-être que lorsque vous direz à votre partenaire « Faisons l'AMOUR », le chien restera simplement en dehors de vos affaires ?.

Ce n'est qu'un exemple de la façon dont enseigner à un robot à communiquer dans une langue connue de nous peut faciliter les choses.

Le cas d'utilisation principal mis en avant dans cet exemple est l'importance de comprendre la différence dans l'utilisation du mot AIME, dans différents contextes.

### Étiquetage des parties du discours

Dès notre plus jeune âge, nous avons été habitués à identifier les étiquettes des parties du discours. Par exemple, lire une phrase et être capable d'identifier quels mots agissent comme des noms, des pronoms, des verbes, des adverbes, etc. Tous ceux-ci sont appelés les étiquettes des parties du discours.

Regardons la définition de Wikipedia pour eux :

> En linguistique de corpus, **l'étiquetage des parties du discours** (**étiquetage POS** ou **étiquetage PoS** ou **POST**), également appelé **étiquetage grammatical** ou **désambiguïsation de la catégorie de mots**, est le processus de marquage d'un mot dans un texte (corpus) comme correspondant à une partie particulière du discours, basée à la fois sur sa définition et son contexte — c'est-à-dire, sa relation avec les mots adjacents et liés dans une phrase, une phrase ou un paragraphe. Une forme simplifiée de ceci est couramment enseignée aux enfants d'âge scolaire, dans l'identification des mots comme des noms, des verbes, des adjectifs, des adverbes, etc.

Identifier les étiquettes des parties du discours est beaucoup plus compliqué que de simplement mapper les mots à leurs étiquettes de parties du discours. Cela est dû au fait que l'étiquetage POS n'est pas quelque chose de générique. Il est tout à fait possible qu'un seul mot ait une étiquette de partie du discours différente dans différentes phrases en fonction de différents contextes. C'est pourquoi il est impossible d'avoir une cartographie générique pour les étiquettes POS.

Comme vous pouvez le voir, il n'est pas possible de trouver manuellement différentes étiquettes de parties du discours pour un corpus donné. De nouveaux types de contextes et de nouveaux mots continuent d'apparaître dans les dictionnaires de diverses langues, et l'étiquetage POS manuel n'est pas évolutif en soi. C'est pourquoi nous nous appuyons sur l'étiquetage POS basé sur la machine.

Avant de continuer et de voir comment l'étiquetage des parties du discours est effectué, nous devrions examiner pourquoi l'étiquetage POS est nécessaire et où il peut être utilisé.

### Pourquoi l'étiquetage des parties du discours ?

L'étiquetage des parties du discours en soi peut ne pas être la solution à un problème particulier de NLP. C'est cependant quelque chose qui est fait comme un prérequis pour simplifier de nombreux problèmes différents. Considérons quelques applications de l'étiquetage POS dans diverses tâches de NLP.

#### Conversion de texte en parole

Regardons la phrase suivante :

```
Ils refusent de nous permettre d'obtenir le permis de refuser.
```

Le mot `refuser` est utilisé deux fois dans cette phrase et a deux significations différentes ici. _refUSER (/_rɘˈfyoʊz/) est un verbe signifiant « nier », tandis que _REFuser (/_ˈrefjʊoʊs/) est un nom signifiant « déchets » (c'est-à-dire qu'ils ne sont pas des homophones). Ainsi, nous devons savoir quel mot est utilisé afin de prononcer correctement le texte. (Pour cette raison, les systèmes de texte à parole effectuent généralement l'étiquetage POS.)

Jetez un coup d'œil aux étiquettes de parties du discours générées pour cette phrase par le package [NLTK](https://www.nltk.org/).

```
>>> text = word_tokenize("Ils refusent de nous permettre d'obtenir le permis de refuser")
>>> nltk.pos_tag(text)
[('Ils', 'PRP'), ('refusent', 'VBP'), ('de', 'TO'), ('nous', 'PRP'), ('permettre', 'VB'), ('d\', 'TO'), ('obtenir', 'VB'), ('le', 'DT'), ('permis', 'NN'), ('de', 'IN'), ('refuser', 'VB')]
```

Comme nous pouvons le voir à partir des résultats fournis par le package NLTK, les étiquettes POS pour _refUSER_ et _REFuser_ sont différentes. L'utilisation de ces deux étiquettes POS différentes pour notre convertisseur de texte en parole peut donner un ensemble différent de sons.

De même, regardons une autre application classique de l'étiquetage POS : la désambiguïsation du sens des mots.

#### Désambiguïsation du sens des mots

Parlons de cet enfant appelé Peter. Puisque sa mère est une scientifique en neurologie, elle ne l'a pas envoyé à l'école. Sa vie était dépourvue de science et de mathématiques.

Un jour, elle a mené une expérience et l'a fait s'asseoir pour un cours de mathématiques. Même s'il n'avait aucune connaissance préalable du sujet, Peter a pensé qu'il avait réussi son premier test. Sa mère a ensuite pris un exemple du test et l'a publié comme suit. (Chapeau à elle !)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nHkemiTJp9FJV-wjxBlGrA.png)
_Exemple de désambiguïsation du sens des mots — Le premier problème de maths de mon fils Peter._

Les mots apparaissent souvent dans différents sens en tant que différentes parties du discours. Par exemple :

* Elle a vu un **ours.**
* Vos efforts **porteront** leurs fruits.

Le mot **ours** dans les phrases ci-dessus a des sens complètement différents, mais surtout, l'un est un nom et l'autre est un verbe. Une désambiguïsation rudimentaire du sens des mots est possible si vous pouvez étiqueter les mots avec leurs étiquettes POS.

La désambiguïsation du sens des mots (WSD) consiste à identifier quel sens d'un mot (c'est-à-dire quelle signification) est utilisé dans une phrase, lorsque le mot a plusieurs significations.

Essayez de penser aux multiples significations de cette phrase :

**Le temps passe comme une flèche**

Voici les diverses interprétations de la phrase donnée. La signification et donc la partie du discours peuvent varier pour chaque mot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rOL82uvp5WPXtlhnFZEHKA.jpeg)
_Les étiquettes des parties du discours définissent la signification d'une phrase en fonction du contexte_

Comme nous pouvons le voir clairement, il existe plusieurs interprétations possibles pour la phrase donnée. Différentes interprétations donnent différents types d'étiquettes de parties du discours pour les mots. Ces informations, si elles sont disponibles pour nous, peuvent nous aider à trouver la version exacte / l'interprétation de la phrase et ensuite nous pouvons procéder à partir de là.

L'exemple ci-dessus nous montre qu'une seule phrase peut avoir trois séquences d'étiquettes POS différentes qui lui sont attribuées et qui sont également probables. Cela signifie qu'il est très important de savoir quelle signification spécifique est transmise par la phrase donnée chaque fois qu'elle apparaît. **C'est la désambiguïsation du sens des mots, car nous essayons de trouver LA séquence.**

Ce ne sont là que deux des nombreuses applications où nous aurions besoin de l'étiquetage POS. Il existe d'autres applications qui nécessitent également l'étiquetage POS, comme la réponse aux questions, la reconnaissance vocale, la traduction automatique, etc.

Maintenant que nous avons une connaissance de base des différentes applications de l'étiquetage POS, examinons comment nous pouvons procéder pour attribuer réellement des étiquettes POS à tous les mots de notre corpus.

### Types d'étiqueteurs POS

Les algorithmes d'étiquetage POS se divisent en deux groupes distincts :

* **Étiqueteurs POS basés sur des règles**
* **Étiqueteurs POS stochastiques**

L'étiqueteur [E. Brill](https://en.wikipedia.org/wiki/Brill_tagger), l'un des premiers et des plus largement utilisés pour l'anglais, emploie des algorithmes basés sur des règles. Examinons d'abord un très bref aperçu de ce qu'est l'étiquetage basé sur des règles.

#### Étiquetage basé sur des règles

L'étiquetage automatique des parties du discours est un domaine du traitement du langage naturel où les techniques statistiques ont été plus réussies que les méthodes basées sur des règles.

Les approches typiques basées sur des règles utilisent des informations contextuelles pour attribuer des étiquettes aux mots inconnus ou ambigus. La désambiguïsation est effectuée en analysant les caractéristiques linguistiques du mot, de son mot précédent, de son mot suivant et d'autres aspects.

Par exemple, si le mot précédent est un article, alors le mot en question doit être un nom. Cette information est codée sous forme de règles.

Exemple de règle :

> Si un mot ambigu/inconnu X est précédé d'un déterminant et suivi d'un nom, étiquetez-le comme un adjectif.

Définir un ensemble de règles manuellement est un processus extrêmement fastidieux et n'est pas du tout évolutif. Nous avons donc besoin d'une méthode automatique pour le faire.

L'étiqueteur de Brill est un étiqueteur basé sur des règles qui parcourt les données d'entraînement et découvre l'ensemble des règles d'étiquetage qui définissent le mieux les données et minimisent les erreurs d'étiquetage POS. Le point le plus important à noter ici concernant l'étiqueteur de Brill est que les règles ne sont pas artisanales, mais sont plutôt découvertes en utilisant le corpus fourni. La seule ingénierie de caractéristiques requise est un **ensemble de modèles de règles** que le modèle peut utiliser pour créer de nouvelles caractéristiques.

Passons maintenant à l'étiquetage POS stochastique.

#### Étiquetage stochastique des parties du discours

Le terme « étiqueteur stochastique » peut faire référence à un certain nombre d'approches différentes du problème de l'étiquetage POS. Tout modèle qui intègre d'une manière ou d'une autre la fréquence ou la probabilité peut être correctement étiqueté stochastique.

Les étiqueteurs stochastiques les plus simples désambiguïsent les mots uniquement sur la base de la probabilité qu'un mot se produise avec une étiquette particulière. En d'autres termes, l'étiquette rencontrée le plus fréquemment dans l'ensemble d'entraînement avec le mot est celle attribuée à une instance ambiguë de ce mot. Le problème avec cette approche est que, bien qu'elle puisse produire une étiquette valide pour un mot donné, elle peut également produire des séquences d'étiquettes inadmissibles.

Une alternative à l'approche de la fréquence des mots consiste à calculer la probabilité qu'une séquence donnée d'étiquettes se produise. Cela est parfois appelé l'approche _n-gram_, faisant référence au fait que la meilleure étiquette pour un mot donné est déterminée par la probabilité qu'elle se produise avec les n étiquettes précédentes. Cette approche a beaucoup plus de sens que celle définie précédemment, car elle considère les étiquettes pour les mots individuels en fonction du contexte.

Le niveau suivant de complexité qui peut être introduit dans un étiqueteur stochastique combine les deux approches précédentes, utilisant à la fois les probabilités de séquence d'étiquettes et les mesures de fréquence des mots. Cela est connu sous le nom de **Modèle de Markov Caché (HMM)**.

Avant de procéder à ce qu'est un **Modèle de Markov Caché**, examinons d'abord ce qu'est un Modèle de Markov. Cela aidera mieux à comprendre la signification du terme **Caché** dans les HMM.

#### Modèle de Markov

Supposons qu'il n'y ait que trois types de conditions météorologiques, à savoir

* Pluvieux
* Ensoleillé
* Nuageux

Maintenant, puisque notre jeune ami que nous avons présenté ci-dessus, Peter, est un petit enfant, il adore jouer dehors. Il adore quand le temps est ensoleillé, car tous ses amis sortent jouer dans des conditions ensoleillées.

Il déteste le temps pluvieux pour des raisons évidentes.

Chaque jour, sa mère observe le temps le matin (c'est à ce moment-là qu'il sort généralement jouer) et, comme toujours, Peter vient la voir juste après s'être levé et lui demande de lui dire à quoi ressemblera le temps. Puisqu'elle est un parent responsable, elle veut répondre à cette question aussi précisément que possible. Mais la seule chose qu'elle a est un ensemble d'observations prises sur plusieurs jours quant à la météo.

Comment fait-elle une prédiction de la météo pour aujourd'hui en fonction de ce qu'a été la météo au cours des N derniers jours ?

Supposons que vous avez une séquence. Quelque chose comme ceci :

`Ensoleillé, Pluvieux, Nuageux, Nuageux, Ensoleillé, Ensoleillé, Ensoleillé, Pluvieux`

Ainsi, la météo pour un jour donné peut être dans l'un des trois états.

Disons que nous décidons d'utiliser un modèle de chaîne de Markov pour résoudre ce problème. Maintenant, en utilisant les données que nous avons, nous pouvons construire le diagramme d'état suivant avec les probabilités étiquetées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BW3GyPvHOg0zWbBb8VWaXA.png)

Afin de calculer la probabilité de la météo d'aujourd'hui étant donné N observations précédentes, nous utiliserons la propriété markovienne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mpCRGnxgzke50mjL0loOcw.png)

La chaîne de Markov est essentiellement le modèle de Markov le plus simple connu, c'est-à-dire qu'elle obéit à la propriété de Markov.

La propriété de Markov suggère que la distribution pour une variable aléatoire dans le futur dépend uniquement de sa distribution dans l'état actuel, et aucun des états précédents n'a d'impact sur les états futurs.

Pour une explication beaucoup plus détaillée du fonctionnement des chaînes de Markov, consultez ce [lien](https://towardsdatascience.com/introduction-to-markov-chains-50da3645a50d).

De plus, jetez un coup d'œil à l'exemple suivant juste pour voir comment la probabilité de l'état actuel peut être calculée en utilisant la formule ci-dessus, en tenant compte de la propriété markovienne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gymjj1jZJHkwQXMf7rsNYw.png)

Appliquez la propriété de Markov dans l'exemple suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FdMUaqeTj8dAsqJF2yAjQg.png)

Nous pouvons clairement voir que, selon la propriété de Markov, la probabilité que la météo de « demain » soit ensoleillée dépend uniquement de la météo « d'aujourd'hui » et non de celle « d'hier ».

Passons maintenant à ce qui est caché dans les modèles de Markov cachés.

### Modèle de Markov caché

C'est encore le petit Peter, et cette fois-ci, il va importuner son nouveau gardien — qui est vous. (Oupsy !!!)

En tant que gardien, l'une des tâches les plus importantes pour vous est de border Peter et de vous assurer qu'il est profondément endormi. Une fois que vous l'avez bordé, vous voulez vous assurer qu'il est réellement endormi et non en train de faire des bêtises.

Vous ne pouvez cependant pas entrer à nouveau dans la pièce, car cela réveillerait sûrement Peter. Donc, tout ce que vous avez à décider, ce sont les bruits qui pourraient provenir de la pièce. Soit la pièce est **silencieuse**, soit il y a du **bruit** qui provient de la pièce. Ce sont vos états.

La mère de Peter, avant de vous laisser à ce cauchemar, a dit :

> Que le son soit avec vous :)

Sa mère vous a donné le diagramme d'état suivant. Le diagramme comporte certains états, observations et probabilités.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_i4JqwAZ9DdjO5Kt.)
_Bonjour Gardien, cela pourrait aider. ~La mère de Peter. Amusez-vous !_

Notez qu'il n'y a pas de corrélation directe entre le son provenant de la pièce et le fait que Peter soit endormi.

Il y a deux types de probabilités que nous pouvons voir à partir du diagramme d'état.

* L'une est les probabilités d'**émission**, qui représentent les probabilités de faire certaines observations étant donné un état particulier. Par exemple, nous avons `P(bruit | éveillé) = 0,5`. Il s'agit d'une probabilité d'émission.
* Les autres sont les probabilités de **transition**, qui représentent la probabilité de passer à un autre état étant donné un état particulier. Par exemple, nous avons `P(endormi | éveillé) = 0,4`. Il s'agit d'une probabilité de transition.

La propriété markovienne s'applique également dans ce modèle. Donc, ne compliquez pas trop les choses. Markov, votre sauveur, a dit :

> Ne vous plongez pas trop dans l'histoire...

La propriété de Markov, telle qu'elle serait applicable à l'exemple que nous avons considéré ici, serait que la probabilité que Peter soit dans un état dépend UNIQUEMENT de l'état précédent.

Mais il y a un défaut clair dans la propriété de Markov. Si Peter est éveillé depuis une heure, alors la probabilité qu'il s'endorme est plus élevée que s'il est éveillé depuis seulement 5 minutes. Donc, l'histoire compte. Par conséquent, le modèle basé sur la machine à états de Markov n'est pas complètement correct. Il s'agit simplement d'une simplification.

La propriété de Markov, bien qu'erronée, rend ce problème très traitable.

Nous observons généralement des périodes plus longues où l'enfant est éveillé et endormi. Si Peter est éveillé maintenant, la probabilité qu'il reste éveillé est plus élevée que celle qu'il aille dormir. D'où le 0,6 et le 0,4 dans le diagramme ci-dessus. `P(éveillé | éveillé) = 0,6 et P(endormi | éveillé) = 0,4`

![Image](https://cdn-media-1.freecodecamp.org/images/1*mJNBB5gdLR_Z6AlUKRfN6A.png)
_La matrice des probabilités de transition._

![Image](https://cdn-media-1.freecodecamp.org/images/1*YkEuELs83MGtCz2v_uEVXw.png)
_La matrice des probabilités d'émission._

Avant d'essayer de résoudre le problème en utilisant les HMM, relions ce modèle à la tâche d'étiquetage des parties du discours.

#### HMM pour l'étiquetage des parties du discours

Nous savons que pour modéliser un problème en utilisant un modèle de Markov caché, nous avons besoin d'un ensemble d'observations et d'un ensemble d'états possibles. Les états dans un HMM sont cachés.

Dans le problème d'étiquetage des parties du discours, les **observations** sont les mots eux-mêmes dans la séquence donnée.

Quant aux **états**, qui sont cachés, ceux-ci seraient les étiquettes POS pour les mots.

Les **probabilités de transition** seraient quelque chose comme `P(VP | NP)`, c'est-à-dire, quelle est la probabilité que le mot actuel ait une étiquette de phrase verbale étant donné que l'étiquette précédente était une phrase nominale.

Les **probabilités d'émission** seraient `P(john | NP) ou P(will | VP)`, c'est-à-dire, quelle est la probabilité que le mot soit, par exemple, John étant donné que l'étiquette est une phrase nominale.

Notez que ceci n'est qu'une modélisation informelle du problème pour fournir une compréhension très basique de la manière dont le problème d'étiquetage des parties du discours peut être modélisé en utilisant un HMM.

#### Comment résoudre cela ?

Revenons à notre problème de prendre soin de Peter.

Nous sommes irrités ? ?.

Notre problème ici était que nous avons un état initial : Peter était éveillé lorsque vous l'avez bordé. Après cela, vous avez enregistré une séquence d'observations, à savoir **bruit** ou **silence**, à différents pas de temps. En utilisant cet ensemble d'observations et l'état initial, vous voulez découvrir si Peter serait éveillé ou endormi après, disons, N pas de temps.

Nous traçons toutes les transitions possibles à partir de l'état initial. Il y a un nombre exponentiel de branches qui apparaissent à mesure que nous continuons à avancer. Ainsi, le modèle **croît de manière exponentielle** après quelques pas de temps. Même sans tenir compte des observations. Jetez un coup d'œil au modèle qui se développe de manière exponentielle ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pOOd-g0iFsLbjBIw1Fit2w.png)
_S0 est Éveillé et S1 est Endormi. Croissance exponentielle à travers le modèle en raison des transitions._

Si nous avions un ensemble d'états, nous pourrions calculer la probabilité de la séquence. Mais nous n'avons pas les états. Tout ce que nous avons est une séquence d'observations. C'est pourquoi ce modèle est appelé le modèle de **Markov Caché** — parce que les états réels au fil du temps sont cachés.

Alors, gardien, si vous êtes arrivé jusqu'ici, cela signifie que vous avez au moins une assez bonne compréhension de la manière dont le problème doit être structuré. Il ne reste plus qu'à utiliser un algorithme ou une technique pour résoudre réellement le problème. Pour l'instant, **Félicitations pour avoir monté de niveau !**

Dans le [prochain article](https://medium.freecodecamp.org/a-deep-dive-into-part-of-speech-tagging-using-viterbi-algorithm-17c8de32e8bc) de cette série en deux parties, nous verrons comment nous pouvons utiliser un algorithme bien défini connu sous le nom d'**algorithme de Viterbi** pour décoder la séquence donnée d'observations étant donné le modèle. À bientôt !