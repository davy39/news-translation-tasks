---
title: 'Structures de données 101 : Graphes — Une introduction visuelle pour débutants'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2019-01-21T17:58:53.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-graphs-a-visual-introduction-for-beginners-6d88f36ec768
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EBtSVCSmRvw40Bmu9vP69A.png
tags:
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Structures de données 101 : Graphes — Une introduction visuelle pour débutants'
seo_desc: 'Get to know the data structures that you use every day

  👋 Welcome! Let’s Start with Some Vital Context. Let me ask you something:✅ Do you
  use Google Search?✅ Do you use Google Maps?✅ Do you use social media sites?

  If your answer is “yes” to any of th...'
---

#### Découvrez les structures de données que vous utilisez chaque jour



👋 Bienvenue ! Commençons par un peu de contexte essentiel. Permettez-moi de vous poser une question : 
**✅ Utilisez-vous Google Search ?**   
**✅ Utilisez-vous Google Maps ?**   
**✅ Utilisez-vous les réseaux sociaux ?**

**Si vous avez répondu "oui" à l'une de ces questions, alors vous avez définitivement utilisé des graphes sans même le savoir ! Surpris ? 😲 Moi aussi !** Cet article vous donnera une introduction visuelle au monde des graphes, leur but, leurs éléments et leurs types.

**Ces structures de données ont vraiment attiré mon attention en raison de leurs capacités incroyables.** Elles sont si puissantes que vous n'imaginez même pas à quel point leurs applications dans le monde réel peuvent être diverses. **Commençons !** 😁

### 🌐 Applications dans le monde réel — La magie commence !

![Image](https://cdn-media-1.freecodecamp.org/images/7Fthyp4QpNDWIPHyw-ufGzUtNambSqhQzamA)

**Les graphes sont utilisés dans divers secteurs et domaines :**

* Les **systèmes GPS et Google Maps** utilisent des graphes pour trouver le chemin le plus court d'une destination à une autre.
* Les **réseaux sociaux** utilisent des graphes pour représenter les connexions entre les utilisateurs.
* L'**algorithme de recherche Google** utilise des graphes pour déterminer la pertinence des résultats de recherche.
* La **recherche opérationnelle** est un domaine qui utilise des graphes pour trouver le chemin optimal afin de réduire le coût du transport et de la livraison de biens et de services.
* **Même la chimie** utilise des graphes pour représenter des molécules !!! ❤️

Leurs applications sont incroyables, n'est-ce pas ?   
Commençons notre voyage à travers ce monde ! 😄

### 🔍 Rencontrez les graphes !

Maintenant que vous avez un peu de contexte, commençons par parler de leur principal objectif et de leurs éléments.

**Les graphes sont utilisés pour représenter, trouver, analyser et optimiser les connexions entre des éléments (maisons, aéroports, lieux, utilisateurs, articles, etc.).**

Voici un exemple de ce à quoi ressemble un graphe :

![Image](https://cdn-media-1.freecodecamp.org/images/vQ77VuGVlTR95GgMxzyKqydIqoRJcPcWrigy)
_Graphe._

#### 💡 Éléments de base

Je suis sûre que vous avez remarqué deux éléments principaux dans le diagramme ci-dessus : des cercles et des lignes épaisses les reliant. Ils sont appelés, respectivement, **Nœuds** et **Arêtes**.

![Image](https://cdn-media-1.freecodecamp.org/images/9KFiyFYi9bMktsJkMKLKaeJl31heUN9A-xrr)

**Examinons-les plus en détail !** 👍

* **Nœuds :** ce sont les **éléments** qui créent le réseau. Ils pourraient représenter des **maisons, des lieux, des aéroports, des ports, des arrêts de bus, des bâtiments, des utilisateurs**, essentiellement tout ce que vous pourriez représenter comme étant connecté à d'autres éléments similaires dans un réseau.
* **Arêtes :** ce sont les **connexions** entre les nœuds. Elles pourraient représenter des **rues, des vols, des itinéraires de bus, une connexion entre deux utilisateurs dans un réseau social**, ou tout ce qui pourrait représenter une connexion entre les nœuds dans le contexte dans lequel vous travaillez.

#### 😱 Que se passe-t-il s'il n'y a pas de connexion ?

Si deux nœuds ne sont pas connectés par une arête, cela signifie qu'il n'y a **pas de connexion directe entre eux.** Mais ne paniquez pas ! 😩 Vous pourriez toujours pouvoir aller d'un nœud à un autre en **suivant une séquence d'arêtes**, similaire à la conduite à travers plusieurs rues pour atteindre votre destination finale. 🚗🏎️ 🚗

Par exemple, dans le diagramme ci-dessous, même s'il n'y a pas de connexion **directe** (**arête**) entre le **nœud violet** (à gauche) et le **nœud jaune** (à droite), vous pouvez aller du nœud violet au nœud orange, au nœud rose, au nœud vert, et enfin atteindre le nœud jaune. 🏆

![Image](https://cdn-media-1.freecodecamp.org/images/5GifDfcnk5D15YwlbmewVveYhSAkMhWKCnfm)
_Pas de connexion directe entre le nœud violet et le nœud jaune._

C'est un aspect clé des graphes, que vous pouvez **rechercher l'élément que vous cherchez en suivant les chemins disponibles.**

### 🌍 Notation et terminologie

Il est très important d'apprendre le langage formel pour travailler avec les graphes :

* `**|V|**` = Nombre **total de sommets** (**nœuds**) dans le graphe.
* `**|E|**` = Nombre **total de connexions** (**arêtes**) dans le graphe.

Dans l'exemple ci-dessous, `**|V| = 6**` car il y a six nœuds (cercles) et  
`**|E| = 7**` car il y a sept arêtes (lignes).

![Image](https://cdn-media-1.freecodecamp.org/images/5vbqwpnuO8nAdj51kN4Bk8ozdpL6WYWkkQHu)
_Graphe._

### 📊 Types de graphes

Les graphes sont classés en fonction des caractéristiques de leurs arêtes (connexions). **Examinons-les en détail !** 😃

#### 1️⃣ Graphes orientés

**Dans les graphes orientés, les arêtes ont une direction.** Elles vont d'un nœud à un autre, et il n'y a pas de moyen de revenir au nœud initial par cette arête.

Comme vous pouvez le voir dans le diagramme ci-dessous, **les arêtes (connexions) ont maintenant des flèches qui pointent dans une direction spécifique.** **Pensez à ces arêtes comme à des rues à sens unique.** Vous pouvez aller dans une direction et atteindre votre destination, mais vous ne pouvez pas revenir par cette même rue, vous devez donc trouver un chemin alternatif.

![Image](https://cdn-media-1.freecodecamp.org/images/9KWaj30YcJDBhvteJvkQQ7YvOu3PVaPBaXpw)
_Graphe orienté._

🍕 Par exemple, si nous créons un graphe pour un service de livraison de pizza, représentant une ville, deux maisons (nœuds) peuvent être **connectées par une rue à sens unique (arête).** Vous pourriez aller de la maison A à la maison B par cette rue, mais vous ne pourriez pas revenir, vous devriez donc prendre un chemin alternatif.

![Image](https://cdn-media-1.freecodecamp.org/images/U7ZcYL5X54m06sKCuQ3wv8K2-Ka7ixE67nxg)

**💡 Note :** Dans un graphe orienté, **vous ne pourrez peut-être pas revenir du tout à votre emplacement initial** s'il n'y a pas de chemin avec les directions appropriées. 😞 Dans le diagramme ci-dessous, vous pouvez voir que vous pouvez aller avec succès du nœud violet au nœud vert, mais remarquez qu'il n'y a pas de moyen de revenir du nœud vert au nœud violet car les arêtes sont des "rues à sens unique".

![Image](https://cdn-media-1.freecodecamp.org/images/CPepyBE1XXy7fcXemQXQZGbncbZ4RCPH9Ezx)
_Point de non-retour._

#### 2️⃣ Graphes non orientés

**Dans ce type de graphe, les arêtes sont non orientées (elles n'ont pas de direction spécifique).** Pensez aux arêtes non orientées comme à des rues à double sens. Vous pouvez aller d'un nœud à un autre et revenir par ce même "chemin".

**💡 Note :** Lorsque vous voyez un diagramme de graphe où les arêtes n'ont pas de flèches pointant dans une direction spécifique, vous pouvez supposer que le graphe est non orienté.

![Image](https://cdn-media-1.freecodecamp.org/images/kgILL-2f3arDbAUOwFKLRFxp2khpvvZ5J9vF)

🍕 Pour notre service de livraison de pizza, cela signifierait que le scooter de livraison peut aller **de la source à la destination par la même rue ou le même chemin** (À leur soulagement ! 😇).

![Image](https://cdn-media-1.freecodecamp.org/images/ijCoLsVRLPWxVTmUI13tnv-aTOtyiHHonk11)

Dans le graphe ci-dessous, vous pourriez aller **du nœud violet au nœud vert et revenir par le même chemin**, vous n'atteignez donc pas un point de non-retour. 😌

![Image](https://cdn-media-1.freecodecamp.org/images/Fe2wHkUPwhxYxdd9LXschmm2VfNaMhiiHJrb)
_Vous pouvez revenir !_

### ⚖️ Des poids ? — Oui, des poids !

#### 1️⃣ Graphes pondérés

**Dans les graphes pondérés, chaque arête a une valeur associée (appelée poids).** Cette valeur est utilisée pour représenter une certaine relation quantifiable entre les nœuds qu'elles connectent.

Par exemple, les poids pourraient représenter la **distance, le temps, le nombre de connexions partagées entre deux utilisateurs dans un réseau social**, ou tout ce qui pourrait être utilisé pour décrire la connexion entre les nœuds dans le contexte dans lequel vous travaillez.

![Image](https://cdn-media-1.freecodecamp.org/images/H1ASU4s0MP52QUyuqo4LIjlvZcR4kn7lkq2V)
_Graphe pondéré._

Ces poids sont utilisés par l'[**algorithme de Dijkstra**](https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html) pour optimiser les routes en trouvant les chemins les plus courts ou les moins coûteux entre les nœuds dans un réseau. (Restez à l'écoute pour un article sur l'algorithme de Dijkstra ! 😃).

#### 2️⃣ Graphes non pondérés

En revanche, les graphes non pondérés **n'ont pas de poids associés à leurs arêtes.** Un exemple de ce type de graphe peut être trouvé dans les réseaux sociaux, où les arêtes représentent la connexion entre deux utilisateurs. La connexion ne peut pas être quantifiée. Par conséquent, l'arête n'a pas de poids.

![Image](https://cdn-media-1.freecodecamp.org/images/y5vDbTl6r5SZOxsjcpI1U68DuWFIe3D4zC6h)
_Graphe non pondéré._

**💡 Note :** Vous avez peut-être remarqué que, jusqu'à présent, nos graphes n'ont qu'une seule arête reliant chaque paire de nœuds. Il est naturel de se demander s'il pourrait y avoir plus d'une arête entre une paire de nœuds. **En fait, cela est possible avec les multigraphes !** Ils peuvent avoir plusieurs arêtes reliant la même paire de nœuds.

![Image](https://cdn-media-1.freecodecamp.org/images/xE-qHRQhhKaBVgPhgm2xRzk6OJj5R1G2wtyd)
_Multigraphe._

### ⚽ Nombre d'arêtes ! — Un facteur important

Il est très important de savoir si un graphe a beaucoup ou peu d'arêtes car c'est un facteur crucial pour décider comment vous allez représenter cette structure de données dans votre code. **Voyons les différents types !** 👍

#### 1️⃣ Graphes denses

**Les graphes denses ont de nombreuses arêtes. Mais, attendez ! ⚠️** Je sais ce que vous devez penser, comment pouvez-vous déterminer ce qui qualifie comme "nombreuses arêtes" ? C'est un peu trop subjectif, n'est-ce pas ? 😇 Je suis d'accord avec vous, alors quantifions un peu :

👉 **Trouvons le nombre maximum d'arêtes dans un graphe orienté.** S'il y a `**|V|**` nœuds dans un graphe orienté (dans l'exemple ci-dessous, six nœuds), cela signifie que chaque nœud peut avoir jusqu'à `**|v|**` connexions (dans l'exemple ci-dessous, six connexions).

Pourquoi ? Parce que **chaque nœud pourrait potentiellement se connecter avec tous les autres nœuds et avec lui-même** (voir "boucle" ci-dessous)**.** Par conséquent, **le nombre maximum d'arêtes que le graphe peut avoir est** `**|V|*|V|**` , qui est le nombre total de nœuds multiplié par le nombre maximum de connexions que chaque nœud peut avoir.

**Lorsque le nombre d'arêtes dans le graphe est proche du nombre maximum d'arêtes, le graphe est dense.** 😊

![Image](https://cdn-media-1.freecodecamp.org/images/vyGE1CPDiqcjBx1X8BGpFt0bUXOWpn4CZABy)
_Graphe._

💡 **Note :** Les "boucles" se produisent lorsqu'un nœud a une arête qui le relie à lui-même. Étrange et intéressant, n'est-ce pas ? 😄

![Image](https://cdn-media-1.freecodecamp.org/images/IDjXVX7CPToN73P5GO73qHdJBL1hhgS7msMV)
_Représentation d'une "boucle"._

#### 2️⃣ Graphes clairsemés

**Les graphes clairsemés ont peu d'arêtes.** Comme vous pouvez le voir dans le diagramme ci-dessous, il n'y a pas beaucoup de connexions entre les nœuds.

**Lorsque le nombre d'arêtes dans le graphe est significativement inférieur au nombre maximum d'arêtes, le graphe est clairsemé.** 😊

![Image](https://cdn-media-1.freecodecamp.org/images/i4OsBT4deG6soapNSKKTq-1DSQbV5vOFcBrN)
_Graphe clairsemé._

### ⬛ Rencontrez les cycles !

**Maintenant, voyons un concept vital pour comprendre les graphes, les cycles.**

Vous avez probablement remarqué que si vous suivez une séquence de connexions dans un graphe, vous pouvez trouver un **chemin qui vous ramènera au même nœud.** C'est comme "marcher en rond", exactement comme si vous conduisiez dans votre ville et que vous preniez un chemin qui pourrait vous ramener à votre emplacement initial.

**Dans les graphes, ces chemins "circulaires" sont appelés "cycles".** Ils sont des **chemins valides qui commencent et se terminent au même nœud.** Par exemple, dans le diagramme ci-dessous, vous pouvez voir que si vous commencez à n'importe quel nœud, vous pouvez revenir à ce même nœud en suivant les arêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/f6A1AD4qMi8BlEgralqX1tFbjkurgOTrb21K)
_Cycle d'exemple._

**Les cycles ne sont pas toujours "isolés" car ils peuvent faire partie d'un graphe plus grand.** Vous pouvez les détecter en commençant votre recherche sur un nœud spécifique et en trouvant un chemin qui vous ramène à ce même nœud.

![Image](https://cdn-media-1.freecodecamp.org/images/r2bS-ZNjPVqOXoOq3Z7OJrNoWCSLqemZzkmv)
_Cycle dans un graphe._

### 👋 En résumé...

* **Les graphes sont des structures de données incroyables** que vous utilisez chaque jour via Google Search, Google Maps, GPS et les réseaux sociaux.
* Ils sont utilisés pour **représenter des éléments qui partagent des connexions**.
* Les éléments dans le graphe sont appelés **Nœuds** et les connexions entre eux sont appelées **Arêtes**.
* Les graphes peuvent être **orientés**, lorsque leurs arêtes ont une orientation spécifique, similaire aux rues à sens unique, ou **non orientés**, lorsque leurs arêtes n'ont pas d'orientation spécifique, similaire aux rues à double sens.
* Les arêtes peuvent avoir une valeur associée, appelée **poids**.
* Si un graphe a de nombreuses arêtes, il est appelé un graphe **dense**. Sinon, s'il a peu d'arêtes, il est appelé un graphe **clairsemé**.
* Une série de connexions peut former un **cycle** si elles créent un chemin qui vous permet de revenir au même nœud.

**Continuez à apprendre sur ces structures de données incroyables !** **Cela en vaudra vraiment la peine pour votre avenir en tant que développeur.** J'apprends sur les structures de données en ce moment, et je les trouve complètement fascinantes. 😃 🎆 ❤️

> _L'important est de ne pas arrêter de questionner. La curiosité a sa propre raison d'exister. — Albert Einstein_

#### 👋 Merci !

J'espère vraiment que vous avez aimé mon article. ❤️  
Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). 😃