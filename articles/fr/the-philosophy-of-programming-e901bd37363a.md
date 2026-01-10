---
title: La philosophie de la programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T16:32:17.000Z'
originalURL: https://freecodecamp.org/news/the-philosophy-of-programming-e901bd37363a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*GskYn20OaaZ4T3u6.
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: Philosophy
  slug: philosophy
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: La philosophie de la programmation
seo_desc: 'By Haoxian Chen

  Logical thinking === good software


  _Photo by [Unsplash](https://unsplash.com/@giamboscaro?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Giammarco Boscaro on <a href="https://unsplash.com?utm_source=me...'
---

Par Haoxian Chen

#### La pensée logique === un bon logiciel

![Image](https://cdn-media-1.freecodecamp.org/images/EZF4VCe2rJHLZDPrYv-sUBYvAxsRACQj6kV5)
_Photo par [Unsplash](https://unsplash.com/@giamboscaro?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Giammarco Boscaro</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

La programmation est la nouvelle littératie. Mais comment écrire de bons programmes ? Voici les questions récurrentes que nous devons résoudre :

* Comment trouver des solutions algorithmiques à un problème ?
* Ensuite, comment savoir si la solution fonctionne réellement ?
* Même si nous sommes sûrs qu'elle fonctionne, comment dire à l'ordinateur de l'exécuter ?

Fait amusant 💡 si vous avez du mal à résoudre l'une de ces questions, vous faites en réalité de la philosophie.

Pour comprendre pourquoi, examinons quelques similitudes intéressantes entre la programmation et le raisonnement philosophique.

### Le premier principe : vous devez réfléchir profondément.

Les ordinateurs ne font rien de plus intelligent que ce que nous pouvons faire — la différence est qu'ils le font plus rapidement.

Mais ils ne peuvent pas résoudre un problème réel comme « comment me rendre à mon bureau depuis chez moi ? »

> Une méthode efficace peut (en principe) être exécutée par un être humain sans aucune machinerie autre que du papier et un crayon.

> — [La thèse de Church-Turing](https://plato.stanford.edu/entries/church-turing/#ThesHist)

Le mérite de la programmation réside toujours dans la partie raisonnement. C'est-à-dire, traduire un problème du monde réel en instructions simples qu'un ordinateur peut exécuter.

Bien sûr, différents langages de programmation ont différents niveaux d'abstractions sémantiques. Un programme Python peut être plus court que son équivalent en C. Mais cela ne change que la quantité de traductions. Nous ne pouvons pas nous débarrasser du travail de traduction. Mais nous laisserons cette discussion pour plus tard.

#### Le flux de raisonnement d'un programmeur

Maintenant, nous sommes face à une description de problème. Nous pouvons d'abord chercher des exemples d'entrée-sortie à petite échelle pour comprendre le problème :

**Induction.** Nous avons besoin d'un algorithme qui peut gérer de tels exemples. Maintenant, vous faites de l'induction : généraliser des principes à partir de l'expérience.

**Déduction.** Comment savoir si cela fonctionne pour d'autres entrées inconnues ? Nous faisons de la déduction pour prouver la correction de notre algorithme.

**Ontologie.** Nous devons maintenir des données en mémoire informatique. Le but est de les rendre efficaces pour que les ordinateurs les traitent. En d'autres termes, quelle structure de données peut le mieux capturer le flux dynamique de mon information ?

**Induction à nouveau.** Ensuite, vient la toute dernière étape : le débogage. Nous induisons la partie boguée du programme en analysant les sorties inattendues.

#### Un exemple

Maintenant, examinons le processus ci-dessus en suivant cet exemple réel : trouver le chemin le plus court du sommet A au sommet E.

![Image](https://cdn-media-1.freecodecamp.org/images/Bs3KoOWL2idTBigI0y630wh78nK9Sdwtvdck)
_Une carte simple. Les nombres désignent la distance des arêtes._

Pour les problèmes à petite échelle, nous pouvons les résoudre par instinct. Par exemple, il est très simple pour nous de reconnaître la solution A-C-E juste en regardant.

Mais qu'en est-il des topologies plus complexes ? Qu'en est-il des différents poids des arêtes ?

Nous avons besoin de l'aide des ordinateurs. Pourtant, ce n'est pas simple de dire à un ordinateur quoi faire. Il y a un fossé entre la façon dont les humains pensent et la façon dont un ordinateur fonctionne.

### Le processus

#### 1. Généraliser les principes à partir de l'expérience : algorithmes

Pour dire à un ordinateur quoi faire, nous devons d'abord trouver une procédure algorithmique.

Les stratégies gloutonnes sont une façon naturelle de procéder. C'est-à-dire, en partant du sommet source A, et en allant tout le long du chemin le plus court connu. Continuer à explorer de nouveaux sommets jusqu'à ce que nous atteignions la destination E. Et en effet, cette approche satisfait notre exemple.

L'intuition est que, le long du chemin le plus court vers une destination, chaque nœud intermédiaire est visité dans le chemin le plus court également. (Bien sûr, cette intuition suppose que toutes les arêtes ont des poids positifs. Cela peut ne pas être vrai, selon les applications. Nous en discuterons en détail plus tard).

Voici donc la procédure algorithmique :

![Image](https://cdn-media-1.freecodecamp.org/images/OMYtQquoo-Owxbdgr0s8D270PknR9Ez-Zge5)
_Animation de l'algorithme de Dijkstra, par [Wikipedia](https://commons.wikimedia.org/wiki/User:Shiyu_Ji" rel="noopener" target="_blank" title="">Shiyu Ji</a> de <a href="https://commons.wikimedia.org/wiki/File:DijkstraDemo.gif" rel="noopener" target="_blank" title=")_

1. Quelques préparatifs : (1) tenir à jour les sommets que nous avons visités : un ensemble (`visited`), (2) se souvenir des distances les plus courtes connues vers chaque sommet qui **n'utilisent que des sommets découverts** : un autre ensemble `distance(u)`. La distance de chaque sommet est initialement infinie, sauf pour le sommet source qui est 0.
2. Maintenant, nous commençons à explorer : d'abord, nous **visitons** le sommet qui a le chemin le plus court connu jusqu'à présent, disons qu'il s'agit de `u`. (Initialement, ce serait le sommet source).
3. En étant au sommet `u`, nous regardons autour des arêtes sortantes. Chaque arête, disons `(u,v)`, nous donne un chemin vers le sommet `v` qui utilise le sommet `u` comme la dernière étape. Si l'une d'elles est effectivement un chemin plus court vers `v`, ou le premier chemin que nous avons trouvé vers `v`, hourra, nous pouvons mettre à jour notre ensemble de chemins les plus courts maintenant. Sinon, ignorer et continuer.
4. Nous avons terminé avec le sommet `u`, donc nous l'ajoutons à notre ensemble `visited`.
5. Retour à l'étape 2, continuer à explorer jusqu'à ce que nous ayons visité tous les sommets.

`distance` peut maintenant nous dire les distances les plus courtes globales, car il est utilisé pour garder les distances les plus courtes en utilisant uniquement les nœuds visités. Et tous les sommets sont visités lorsque l'algorithme se termine.

Nous venons de réinventer l'algorithme de Dijkstra. Bien sûr, il existe de nombreux autres algorithmes pour trouver le chemin le plus court. Mais le point est, nous avons besoin d'une procédure algorithmique pour résoudre le problème.

#### 2. Valider les principes généraux par déduction

Comment nous assurons-nous que les principes de l'algorithme sont corrects ? Nous pouvons soit augmenter notre confiance en testant le principe contre plus d'exemples d'entrée, soit, plus efficacement, trouver une preuve mathématique rigoureuse.

Comme une [proposition a priori](https://www.iep.utm.edu/apriori/) en philosophie, la correction d'un algorithme est indépendante de son exécution. En d'autres termes, les tests ne peuvent pas garantir la correction des algorithmes. Nous devons la prouver.

Voici le flux de base de la preuve :

1. Pour tous les sommets visités, nous trouvons les chemins les plus courts.

2. La destination est visitée.

3. Par conséquent, nous trouvons le chemin le plus court vers la destination.

Ne vous semblent-ils pas quelque peu familiers ? Comme ceci :

1. Tous les hommes sont mortels.

2. Socrate est un homme.

3. Par conséquent, Socrate est mortel.

En fait, ceci est le [Syllogisme](https://en.wikipedia.org/wiki/Syllogism), une forme classique de raisonnement déductif. C'est à peu près ce que font les logiciens.

Un autre fait historique intéressant : le concept formel de calcul a d'abord été proposé par des logiciens dans les années 1930. Ils devaient savoir si certains problèmes logiques étaient réellement solubles (afin qu'ils puissent éviter de perdre leur temps à résoudre quelque chose d'insoluble). Pour répondre à cela, ils ont proposé la notion de calculabilité.

Plus tard, en 1936, Alonzo Church et Alan Turing ont développé la définition formelle de la calculabilité, indépendamment, en même temps. Cet [article](https://onlinelibrary.wiley.com/doi/full/10.1002/0470018860.s00209) donne un aperçu historique du calcul.

La correction de la conclusion dépend des deux premières prémisses. Dans notre preuve, la deuxième prémisse est triviale, puisque notre algorithme visite littéralement tous les nœuds. Pourtant, prouver la première prémisse, que nous trouvons le chemin le plus court au moment où nous visitons un nœud, nécessite un certain travail.

L'**induction mathématique** peut aider. C'est en fait l'une des techniques les plus utiles pour prouver la correction de nombreux autres algorithmes.

Le flux général est le suivant. Premièrement, si un algorithme fonctionne sur l'entrée `0`, et deuxièmement, si le fait qu'il fonctionne sur l'entrée `n` implique qu'il fonctionne également sur l'entrée `n+1`, alors il fonctionne pour toutes les entrées supérieures ou égales à `0`. À ce stade, vous êtes en mesure de garantir la correction de votre algorithme.

Pour simplifier, je vous renvoie à cette [note de cours](http://www.cs.yale.edu/homes/spielman/365/shortestPaths.pdf) pour la preuve complète de cet algorithme de recherche de chemin.

Notez que nous ne devons pas confondre l'induction mathématique et l'induction philosophique. Par définition philosophique, l'induction mathématique est un processus de raisonnement déductif, car sa correction est contenue en elle-même, sans aucune observation externe.

La leçon est : lorsque nous trouvons un algorithme, il doit être capable de gérer tous les cas d'exécution possibles.

En pratique, passer par la preuve mathématique rigoureuse peut ne pas être la stratégie la plus efficace. Mais au moins, nous voulons considérer autant de cas d'exécution que possible, surtout les cas adverses. Cette pratique améliorerait la robustesse de notre code.

Vous avez peut-être remarqué que, dans notre exemple d'algorithme de recherche de chemin, il ne fonctionne pas si le poids de l'arête est négatif. Vous pouvez trouver la raison dans cette [note de cours](http://www.cs.yale.edu/homes/spielman/365/shortestPaths.pdf). Pour gérer un graphe avec des poids négatifs, vous pouvez utiliser l'[algorithme de Bellman-Ford](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm).

#### 3. Le problème ontologique : structure de données

Jusqu'à présent, nous nous sommes convaincus que nous avons un algorithme correct. Mais ce n'est que la moitié de la bataille.

La question suivante est, comment alimenter l'information dans les ordinateurs ? Les humains aiment les informations visualisées, comme les graphiques ou les histogrammes. Mais les ordinateurs d'aujourd'hui ne traitent que des bits binaires.

Nous devons trouver une structure de données qui contient l'information essentielle. Et elle doit être efficace pour qu'un programme la traite en même temps.

Continuons avec notre exemple de recherche de chemin. Un chemin est une liste ordonnée. Mais c'est irritant à gérer, comparé à un entier. Notez que dans notre algorithme, nous devons trouver le chemin le plus court à partir de notre ensemble de chemins découverts. Et puis itérer tout le long jusqu'à sa fin. Il semble que nous devons consacrer un tableau ou une mémoire pour stocker chaque chemin.

Pourrions-nous faire mieux ? Notez que dans un chemin valide, les apparitions consécutives d'éléments doivent correspondre à une arête dans le graphe. Mais, nous avons déjà l'information sur les arêtes et elles sont les mêmes pour tous les chemins. Pourquoi ne pouvons-nous pas nous débarrasser de cette information redondante ?

Eh bien, nous pouvons nous débarrasser de la liste. Il s'avère que pour rassembler le chemin le plus court, l'étape intermédiaire est de déterminer quel est le prochain saut dont vous avez besoin. Tout ce dont nous avons besoin pour récupérer le chemin le plus court de la source A à tout nœud cible est simplement le graphe lui-même, et la distance la plus courte de A à chaque nœud.

![Image](https://cdn-media-1.freecodecamp.org/images/EVYvfP6tEU3yBZanFV-m8doAre-P8wWDbBeB)
_Information pour récupérer le chemin le plus court de A à tout nœud. (Les nombres dans les sommets désignent la distance depuis A.)_

Une représentation visuelle est dans l'image ci-dessus. Cette représentation est efficace en mémoire. Elle est également plus efficace pour que le programme la traite.

Voici comment il construit le chemin le plus court en utilisant uniquement le vecteur de distance. Commencez par le sommet de destination, et un chemin vide. Recherchez les sommets intermédiaires à travers les arêtes entrantes. Choisissez celui avec la valeur la plus faible dans `distance`. Ajoutez-le à la tête du chemin. Répétez jusqu'à ce que nous atteignions la source. Ce truc a en fait une notation formelle, appelée [back-tracking](https://en.wikipedia.org/wiki/Backtracking).

Les philosophes recherchent la vérité éternelle. Et les programmeurs veulent découvrir la structure de données précise qui capture le mieux la dynamique de l'information. Comme vous le voyez dans l'exemple de recherche de chemin, tout ce dont vous avez besoin pour donner un chemin le plus court est simplement un vecteur, vous indiquant les distances les plus courtes vers chaque sommet. Cela reste vrai pour tout graphe, indépendamment du nombre de sommets ou d'arêtes.

#### 4. Proposition a posteriori : débogage

La plupart des programmeurs ont traversé ce raisonnement des tonnes de fois. Je parie que c'est l'une des parties les plus difficiles et chronophages de toute tâche de programmation.

Par exemple, les fautes de segmentation dans les programmes C sont souvent causées par des références de pointeurs nuls. J'ai appris cela après avoir traité des tonnes de fautes de segmentation C/C++. Bien sûr, il y a des cas plus subtils qui sont liés aux habitudes de programmation personnelles.

L'exemple suivant est une erreur de syntaxe commise par un programmeur. La condition if aurait dû être `is_float==1`, mais le programmeur a confondu l'opérateur d'égalité logique `==` avec un opérateur d'évaluation `=`. Cela passera toujours la vérification du compilateur, car les deux sont des syntaxes correctes.

```
if (is_float = 1) {  // faire quelque chose}
```

C'est un processus de raisonnement inductif. Votre diagnostic de débogage n'a de sens que si vous avez observé suffisamment d'exécutions de programmes.

C'est là que la valeur de la pratique entre en jeu. Peu importe le type de techniques que vous apprenez, vous devez rassembler suffisamment de données pratiques. Sinon, vous n'auriez pas assez d'expérience pour mener à bien l'induction.

**Vous devriez surveiller les schémas récurrents dans vos codes bogués.** Lorsque vous trouvez un bug, le corriger ne suffit pas. Vous avez besoin d'une analyse supplémentaire cause-effet sur votre propre pratique de programmation. Demandez-vous : cette partie de mes habitudes de programmation est-elle particulièrement vulnérable à ces types de bugs ?

### Alors pourquoi est-ce important ?

**La programmation ne consiste pas seulement à écrire du code, c'est une manière systématique de raisonner.** Parce que le code, ou les instructions, n'est qu'un moyen pour atteindre une fin. Avec le développement de la technique de synthèse de programmes, vous pourriez ne même pas avoir à vous soucier d'écrire du code et de le déboguer vous-même. Tout ce qui compte, c'est si vous pouvez dire à l'ordinateur quoi faire.

En tant que première étape vers l'amélioration de vos compétences en programmation, cet article révèle le schéma de raisonnement sous-jacent que nous ne reconnaissons peut-être même pas lorsque nous programmons. La plupart d'entre nous dépendent de la réflexion subconsciente et automatique pour terminer la plupart de nos tâches quotidiennes. Mais d'où vient l'amélioration ? Elle vient d'abord de la remarque de quelque fallacie ou erreur que nous avons commise dans notre processus de raisonnement.

Pour des conseils pratiques, je recommande cet article sur [comment penser comme un programmeur](https://medium.freecodecamp.org/how-to-think-like-a-programmer-lessons-in-problem-solving-d1d8bf1de7d2), et ce [livre](https://www.amazon.com/Think-Like-Programmer-Introduction-Creative/dp/1593274246) sur le même sujet mais avec plus de détails.

#### Références

* [Computation, Philosophical Issues about.](https://onlinelibrary.wiley.com/doi/full/10.1002/0470018860.s00209) Matthias Scheutz.
* [The Church-Turing Thesis](https://plato.stanford.edu/entries/church-turing/#ThesHist).
* [Think Like a Programmer: An Introduction to Creative Problem Solving](https://www.amazon.com/Think-Like-Programmer-Introduction-Creative/dp/1593274246). V. Anton Spraul.