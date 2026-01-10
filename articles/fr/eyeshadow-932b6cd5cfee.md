---
title: Ce que choisir et appliquer du fard à paupières peut nous apprendre sur la
  programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T18:56:19.000Z'
originalURL: https://freecodecamp.org/news/eyeshadow-932b6cd5cfee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aFChFIbBTgSQq2vBAwUZtg.jpeg
tags:
- name: Codelikeagirl
  slug: codelikeagirl
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: women in tech
  slug: women-in-tech
seo_title: Ce que choisir et appliquer du fard à paupières peut nous apprendre sur
  la programmation
seo_desc: 'By Code Girl

  I love eyeshadow. I have over 40 eyeshadow palettes (a palette is a container with
  any number of individual eyeshadow colors), and I don’t think my obsession diminishes
  my status as a progressive woman in technology. I am known for my sp...'
---

Par Code Girl

J'adore le fard à paupières. J'ai plus de 40 palettes de fards à paupières (une palette est un contenant avec un nombre quelconque de couleurs individuelles de fard à paupières), et je ne pense pas que mon obsession diminue mon statut de femme progressive dans la technologie. Je suis connue pour mes couleurs bleues scintillantes qui représentent ma dévotion sans fin à la maison Serdaigle dans Harry Potter.

La triste vérité, cependant, est que je suis nulle pour choisir et appliquer du fard à paupières, ce qui pourrait avoir quelque chose à voir avec le fait que :

1. J'ai trop de couleurs parmi lesquelles choisir, et
2. Je dois enlever mes lunettes pour le faire.

Pourtant, cela n'arrête pas mon besoin insatiable d'acquérir plus d'options de fards à paupières. Après avoir quitté mon magasin de maquillage de confiance la semaine dernière — ayant dépensé plus de 100 $ en produits, y compris une nouvelle palette de fards à paupières (dont je n'avais besoin d'aucun) — j'ai pensé : « Si seulement choisir et appliquer du fard à paupières était aussi facile qu'écrire une fonction. »

C'est l'origine de cet article. Utiliser le code pour résoudre des problèmes pratiques est une caractéristique du domaine de la technologie, mais cela prend de la pratique. Voici ma tentative de **pensée à voix haute** pour résoudre mon problème de fard à paupières.

Pour ceux d'entre nous sans formation en éducation, une **pensée à voix haute** est une méthode pour rendre un processus de pensée invisible, visible. Nous utilisons cette technique fréquemment dans l'instruction de lecture.

### **Bases des fonctions et ma routine de fard à paupières**

Comprendre les fonctions est un rite de passage en programmation. Lorsque vous commencez votre voyage, vous écrivez chaque ligne de code, de nombreuses fois. Entrez les fonctions. Une fonction n'est rien de plus qu'une procédure, un ensemble d'étapes pour accomplir une tâche.

Généralement, une fonction prendra certaines données d'entrée, effectuera la procédure requise avec ces données, et retournera les données résultantes. Ce qui rend les fonctions si polyvalentes dans le code, c'est que vous pouvez appeler cette fonction, ou ensemble d'étapes, encore et encore avec différentes entrées, d'où différentes sorties.

Mettre du fard à paupières, c'est comme suivre un ensemble d'étapes. Je me tiens au même ensemble d'étapes (fonction) pour choisir et appliquer du fard à paupières pratiquement tous les jours, illustré dans le diagramme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/lV50bSeGue9ldy8Sm4HIODMZuDloLdxpuwZu)
_Cette image faisait partie d'un article de blog sur BellaBox [ICI](https://bellabox.com.au/beautyguide/9-Awesome-Eyeshadow-Hacks" rel="noopener" target="_blank" title=")_

Pensons à cela en termes de programmation où nous avons une entrée, un ensemble d'étapes, et une sortie :

* **Entrée** : Je dois entrer une palette de fards à paupières. Disons la palette « Sweet Peach » de [Too Faced Cosmetics](https://www.toofaced.com/).
* **Fonction** : Ma fonction doit filtrer toutes les couleurs (18 au total) et trouver les quatre couleurs clés à utiliser : `highlighter`, `medium`, `smokey`, et `blender`.
* **Sortie** : Dites-moi spécifiquement quelles couleurs correspondent à quelle zone d'application des yeux.

### **Données d'entrée du fard à paupières**

Avez-vous deviné le premier problème ici ? Les données d'entrée ne sont pas aussi simples qu'une variable avec une valeur de chaîne ou de nombre :

![Image](https://cdn-media-1.freecodecamp.org/images/ogsP0Rg28zsy476KFN1xonARjcPlFmquj2MO)

La palette Sweet Peach a 18 couleurs. Vous pourriez penser que nous pouvons écrire chaque couleur dans un tableau (ou une liste) :

![Image](https://cdn-media-1.freecodecamp.org/images/oukf2IVZIW05VLYg1H-dKDwOyjraVbZuLERq)
_Oui, ce n'est que 6 des 18, et oui, les noms des couleurs de fard à paupières sont bizarres._

Il y a encore un problème avec la forme de ces données. Un tableau n'est qu'une liste des couleurs.

Chaque couleur a besoin d'une étiquette pour identifier de quel type de couleur il s'agit : `highlighter`, `medium`, `smokey`, et `blender`.

Une meilleure option pourrait être un tableau d'objets. Un objet est une collection de données organisée par une clé et une valeur. Dans chaque objet ici, nous avons deux paires clé-valeur, une pour le type et l'autre pour la couleur :

![Image](https://cdn-media-1.freecodecamp.org/images/OpBwu2sYa34C6CSYTa-NLgyqeHsFqCPSu8FH)

Parfait. Chaque fois que j'utilise `SweetPeachCombination` comme mon entrée, je saurai exactement quelle couleur utiliser pour quelle partie de mon œil.

### **Fonction findColor : Le paramètre et l'argument**

Maintenant que nous avons des données, nous pouvons voir ce que la fonction pourrait faire. Je veux pouvoir appeler cette fonction `findColor` avec n'importe quelle donnée d'entrée et savoir exactement quelle couleur va où. D'abord, je dois parcourir le tableau. Ensuite, je dois enregistrer le type et la couleur. Le code pourrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/nSJXXiTM16cRtrAWzJA7l45UglurqOg83K5a)
_J'utilise les littéraux de gabarit ES6 dans le console.log._

Puisque ce n'est pas du code réel, je vais simplement enregistrer les informations dans la console. Sur mon site web réel, je mets à jour les informations via le DOM. Voir le site web [**ICI**](https://fwallacephd.github.io/EyeshadowApp/).

Décortiquons le code ci-dessus.

La fonction s'appelle `findColor`, et elle **a** un **paramètre**.

Paramètre, ici, est une façon technique de dire espace réservé d'entrée — ce qui signifie que nous avons besoin des informations de `combination` pour exécuter la fonction. Souvenez-vous, cependant, que nous pouvons utiliser n'importe quelle combinaison que nous voulons, donc le paramètre n'est pas spécifique.

Comment dis-je à la fonction quelle combinaison utiliser ? Lorsque nous appelons la fonction :

![Image](https://cdn-media-1.freecodecamp.org/images/5fm017etuYohkDucn6X4MrWUL7Ka7gzQVUBA)

Nous **passons** la combinaison spécifique. Cela change le mot technique. Ce n'est plus un paramètre, c'est maintenant un **argument**. La différence étant que ceci est la vraie donnée, pas un espace réservé.

Vous pouvez voir cela clairement parce que le **paramètre** s'appelle `combination` tandis que l'**argument** s'appelle `SweetPeachCombination`.

### **Refactorisation des entrées de fard à paupières**

Cela semble être une fonction assez médiocre pour le moment, n'est-ce pas ? Je donne littéralement à la fonction les données de quelle couleur va où, puis je fais en sorte que la fonction renvoie ces informations directement (la sortie). Mais souvenez-vous que j'ai 40 palettes de fards à paupières. Je ne me souviens honnêtement pas de chaque couleur individuelle ou combinaison possible. Pour le moment, je n'ai qu'une seule combinaison pour une seule palette...

Je parie que vous voyez où je veux en venir avec cela.

Mes données d'entrée de fard à paupières ne reflètent pas la réalité — plusieurs palettes avec plusieurs couleurs signifie des possibilités infinies.

La forme des données ne doit pas changer, mais je dois ajouter plus d'informations :

![Image](https://cdn-media-1.freecodecamp.org/images/1Q1QgeaiMwd7N6EtGDHqL0Fy35fxRRJ4b7bE)
_Ceci est l'une de mes combinaisons bleues, donc je l'ai nommée en conséquence._

![Image](https://cdn-media-1.freecodecamp.org/images/JzvYDTHpVTRYm8MwSiZLp6corwZh8RPEgTVu)
_Je ne peux pas laisser de côté la maison Serpentard et la combinaison verte !_

Naturellement, nous devrons réviser la fonction en fonction de ces nouvelles informations, mais c'est la partie la plus facile :

![Image](https://cdn-media-1.freecodecamp.org/images/igGh4jRE8-mKM0wWEPcEHeQ9hosNbRQoKktC)

Théoriquement, je pourrais avoir 400 combinaisons ! Je n'ai pas ce genre de temps le matin pour chercher la bonne combinaison. C'est pourquoi ma fonction `findColor` fonctionne parfaitement. Chaque fois que j'appelle cette fonction, j'utilise un argument `combination`.

![Image](https://cdn-media-1.freecodecamp.org/images/KnRtelk6wZl5Af1WZNelDYyHXn-D3wvGbhPi)

### **La partie la plus importante**

Je dis tout le temps cela à propos de la programmation. Si vous pouvez le rêver, vous pouvez le construire.

J'ai rêvé d'un sélecteur de couleurs de fard à paupières, et je l'ai construit (capture d'écran ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/O-GrgHDBDBVK3etaB7c0f6nnuql99k47csaB)
_Découvrez-le [ICI](https://fwallacephd.github.io/EyeshadowApp/" rel="noopener" target="_blank" title="">ICI</a>. Obtenez le code <a href="https://github.com/fwallacephd/EyeshadowApp" rel="noopener" target="_blank" title=")._

Construire est le **seul** moyen de déboguer de manière réaliste (trouver vos erreurs) et de refactoriser (améliorer le code). Ce sera votre vie en tant que programmeur, il est donc crucial que vous développiez votre mémoire musculaire pour cela.

De plus, je vous mets au défi de pratiquer tout lorsque vous construisez, pas seulement la fonctionnalité (dans ce cas JavaScript), mais aussi vos bases : HTML, CSS (et ici, Bootstrap). Chaque fois que je construis, j'apprends quelque chose de nouveau même dans mes compétences de base.

Pour ce projet, j'ai appris à utiliser CSS pour créer un effet arc-en-ciel sur le titre. J'ai également saisi cette opportunité pour pratiquer l'utilisation d'une base de données, [Firebase](https://firebase.google.com/docs/database/). Il s'agit d'un système de base de données gratuit et facile à utiliser pour définir et récupérer les objets de combinaison de couleurs, mais c'est le sujet d'un autre article.

Alors, que allez-vous construire ensuite ?

Note : Si vous utilisez le fard à paupières Too Faced, et que vous souhaitez m'aider à travailler sur le développement de cette application et ensuite en faire une application mobile, veuillez m'envoyer un e-mail à fwallacephd[at]gmail[dot]com