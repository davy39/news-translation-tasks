---
title: Comment assembler une IA à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-19T03:37:08.000Z'
originalURL: https://freecodecamp.org/news/struggling-with-a-coding-challenge-follow-these-simple-steps-a5372c6ea0f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vWwvSGP1gDBT0Uf_OXIRFQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: education
  slug: education
- name: Game Development
  slug: game-development
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment assembler une IA à partir de zéro
seo_desc: 'By Christopher Phillips

  Yesterday I started the Tic Tac Toe project from Free Code Camp.

  It’s a “programming” challenge in many ways, as it involves creating AI that responds
  intelligently to your moves. In fact, the goal is to create an AI that’s un...'
---

Par Christopher Phillips

Hier, j'ai commencé le projet Tic Tac Toe de [Free Code Camp](http://freecodecamp.com).

C'est un défi de "programmation" à bien des égards, car il implique de créer une IA qui répond intelligemment à vos mouvements. En fait, l'objectif est de créer une IA invincible.

Cela semblait un peu plus complexe que de récupérer des éléments du DOM, de les transformer en objets jQuery et d'appliquer des méthodes, comme nous le faisions avec les projets précédents. J'ai donc commencé à chercher sur Google, pour me perdre dans les théories MiniMax, les tutoriels YouTube horribles et les guides mal écrits.

J'ai décidé de me lancer directement. Et cette décision m'a permis d'apprendre tellement.

#### Sachez ce que vous ne savez pas

Il est vraiment important en programmation de reconnaître vos connaissances actuelles et leurs limites. Alors, comment aborder un défi qui implique bien plus que ce que vous savez déjà.

**1. Réfléchissez à la manière dont vous aborderez le problème.** Créez un plan d'attaque, même si vous n'êtes pas sûr de la manière dont chaque étape fonctionnera. Si c'est avec [Free Code Camp](http://freecodecamp.com), assurez-vous d'inclure les histoires utilisateur dans ce plan et comment vous inclurez chacune d'elles.

**2. Commencez par les bases.** Pour le Tic Tac Toe, cela signifiait créer le HTML et le CSS avec des boutons qui pouvaient être récupérés du DOM et utilisés en JS.

**3. Travaillez avec des méthodes que vous avez déjà utilisées.** J'ai travaillé avec des éléments du DOM à de nombreuses reprises en utilisant jQuery et JavaScript, donc obtenir un bouton, lui donner une valeur de texte innerHTML et une classe, n'était pas un problème.

**4. Créez une solution plus simple.** Pour moi, cela impliquait de créer un jeu pour 2 joueurs sans IA. Vous pouvez voir cela [ici](http://codepen.io/chris_is_phillips/full/pjYyQa/). Un simple aperçu:

* Lorsqu'un utilisateur clique sur un bouton, il ajoute un "X" à ce bouton. Ensuite, le symbole du joueur alterne avec un "O" pour le joueur suivant. Il bascule ensuite d'avant en arrière.
* Lorsqu'une ligne gagnante est créée, un message d'alerte est généré qui dit "Félicitations" + symbole du joueur + "Vous avez gagné".
* Si aucune ligne gagnante n'est créée, c'est un match nul, avec un message d'alerte approprié.

**5. Ajoutez des couches de fonctionnalité avec ce que vous savez.** J'ai ajouté des boutons qui vous permettaient de choisir quel symbole le premier joueur souhaitait être. C'était simple, juste changer une variable. La prochaine chose que j'ai dû faire était de créer une IA. J'ai essayé deux choses.

* Une boucle qui place une réponse d'ordinateur dans la case disponible suivante. Cela a créé une IA très simple qui était vraiment facile à battre. Voir cela [ici](http://codepen.io/chris_is_phillips/full/Qjomdr/).
* Une boucle qui générait un nombre aléatoire entre 1 et 9, et plaçait une valeur dans cette case si elle était libre. Plus complexe, mais finalement une IA très stupide ! Voir cela [ici](http://codepen.io/chris_is_phillips/full/jbJzKQ/).

**6. Recherchez, apprenez et perfectionnez votre solution.** Je recherche maintenant la théorie MiniMax qui est une fonction récursive pour générer des scénarios possibles basés sur des tours de joueur/ordinateur théoriques. Je vais chercher à appliquer cette fonctionnalité dès que j'aurai une bonne compréhension. Je dois également [refactoriser](http://blog.cphillips.co.uk/archives/98) mon code car il est un peu désordonné.

**Aucun problème n'est trop grand.** Commencez par de petites étapes en utilisant vos connaissances actuelles, construisez dessus, puis recherchez les tâches restantes que vous ne pouvez pas accomplir. Ce défi m'a appris le plus jusqu'à présent parmi tout le programme de [Free Code Camp](http://freecodecamp.com).

_Publié à l'origine sur [CHRIS PHILLIPS](http://blog.cphillips.co.uk/archives/323)._