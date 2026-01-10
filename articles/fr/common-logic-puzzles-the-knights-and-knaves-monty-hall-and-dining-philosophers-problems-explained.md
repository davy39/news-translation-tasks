---
title: Énigmes logiques courantes – Les Chevaliers et les Valets, Monty Hall, et le
  Problème des Philosophes Dînant Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/common-logic-puzzles-the-knights-and-knaves-monty-hall-and-dining-philosophers-problems-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d11740569d1a4ca35b6.jpg
tags:
- name: logic
  slug: logic
- name: puzzles
  slug: puzzles
- name: toothbrush
  slug: toothbrush
seo_title: Énigmes logiques courantes – Les Chevaliers et les Valets, Monty Hall,
  et le Problème des Philosophes Dînant Expliqués
seo_desc: 'While not strictly related to programming, logic puzzles are a good warm
  up to your next coding session. You may encounter a logic puzzle in your next technical
  interview as a way to judge your problem solving skills, so it''s worth being prepared.

  In...'
---

Bien que non strictement liées à la programmation, les énigmes logiques sont un bon échauffement pour votre prochaine session de codage. Vous pourriez rencontrer une énigme logique lors de votre prochain entretien technique comme moyen de juger vos compétences en résolution de problèmes, il est donc utile d'être préparé.

Dans cet article, nous avons rassemblé quelques énigmes logiques célèbres et leurs solutions. Pouvez-vous les résoudre sans regarder la réponse ?

## Chevaliers et Valets

Pour cette énigme logique, imaginez qu'il existe deux types de personnes, les chevaliers et les valets. Les chevaliers ne disent que la vérité, tandis que les valets ne mentent que des mensonges.

Il existe de nombreuses variations de cette énigme, mais la plupart impliquent de poser une question pour déterminer qui est le chevalier et qui est le valet.

### Rouge et Bleu

Il y a deux personnes devant vous, Rouge et Bleu. Bleu dit : "Nous sommes tous les deux des valets." Qui est vraiment le chevalier et qui est le valet ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/photo-1556549957-f41c6fcc4210-4.jpeg)

**Solution**  
Il est impossible que Bleu soit le chevalier. Si Bleu était un chevalier, l'énoncé "Nous sommes tous les deux des valets" serait en réalité un mensonge. Par conséquent, Bleu est un valet car son énoncé est un mensonge, et Rouge doit être un chevalier.

### Deux Chemins

Vous arrivez à un embranchement et devez choisir le bon chemin qui mène à votre destination. Il y a deux personnes debout à l'embranchement, et vous savez que l'une doit être un chevalier et l'autre doit être un valet.

Quelle question unique pourriez-vous poser à l'une des personnes pour déterminer le bon chemin, A ou B ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/photo-1519401706-5cf17f6e70de.jpeg)

**Solution**  
La question que vous pouvez poser à l'une ou l'autre personne est : "Quel chemin l'autre personne me dirait être le bon ?" La réponse sera toujours le mauvais chemin à prendre, et vous pouvez prendre l'autre chemin en toute sécurité.

Imaginez que le bon chemin est A.

Si vous demandez directement "Quel est le bon chemin ?", le valet dira que B est correct tandis que le chevalier dira A.

Cependant, lorsqu'on demande quel chemin l'_autre_ personne dirait être correct, le valet mentira et dira que le chevalier vous dirait que le chemin B est correct. Pendant ce temps, le chevalier dira la vérité sur la réponse du valet, et dira que le valet vous dira que le chemin B est le bon.

Dans les deux cas, vous savez que la réponse, le chemin B, est en réalité un mensonge, vous devriez donc prendre l'autre chemin.

## Le Problème de Monty Hall

Le problème de Monty Hall est une énigme sur la probabilité nommée d'après l'animateur de l'émission de jeu des années 70 sur laquelle elle est basée, _Let's Make a Deal_. Ce problème particulier est un [paradoxe véridique](https://en.wikipedia.org/wiki/Paradox), ce qui signifie qu'il existe une solution qui semble contre-intuitive, mais prouvée vraie.

Imaginez que vous êtes dans une émission de jeu et qu'il y a 3 portes, chacune avec un prix différent derrière elles. Derrière l'une des trois portes se trouve une voiture. Derrière les deux autres portes se trouvent des chèvres.

Vous devez choisir l'une des 3 portes pour sélectionner votre prix.

Disons que vous décidez d'ouvrir la Porte 1. L'animateur, qui sait où se trouve la voiture, ouvre une autre porte, la Porte 2, qui révèle une chèvre. Il vous demande ensuite si vous souhaitez ouvrir la Porte 3 à la place.

Devriez-vous choisir la Porte 3 plutôt que votre choix initial ? Est-ce que cela a même de l'importance ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/zachary-anderson-ceYJ1HKt9Rk-unsplash.jpg)

**Solution**  
Il s'avère que votre choix compte vraiment, et il est en fait à votre avantage de choisir la Porte 3 plutôt que la Porte 1. Voici pourquoi.

Lorsque vous avez choisi la Porte 1 parmi les 3 portes fermées, vous aviez 1 chance sur 3 d'avoir choisi la bonne. Les Portes 2 et 3 ont également 1 chance sur 3 d'avoir une voiture derrière elles.

Une autre façon de voir les choses est que les Portes 2 et 3 ont une chance combinée de 2 sur 3 d'avoir une voiture derrière elles.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/8EsVvZk-1.png)

Mais lorsque l'animateur ouvre la Porte 2 et révèle la chèvre, vous avez soudainement plus d'informations sur le problème.

Rappelez-vous que les Portes 2 et 3 ont une probabilité combinée de cacher la voiture 2/3 du temps. Lorsque la Porte 2 a été ouverte, vous savez qu'il n'y avait pas de voiture derrière elle.

Mais cette révélation ne change pas la probabilité combinée des deux portes. C'est le point clé à retenir ici !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/V2JzAka-1.png)

Puisque vous savez que la Porte 2 a 0 chance sur 3 de cacher la voiture, vous pouvez maintenant dire qu'il y a 2 chances sur 3 que la voiture soit derrière la Porte 3. La Porte 1 reste inchangée – il n'y a qu'1 chance sur 3 que la voiture soit derrière elle.

Ainsi, si vous décidez de changer, vous passez d'environ 33,33 % de chances à 66,67 % de chances de trouver la voiture. En d'autres termes, vous doublez vos chances de succès en ouvrant la Porte 3 à la place !

Oui, il est possible que la Porte 1 ait caché la voiture tout du long et que l'animateur vous ait trompé. Cela n'a pas d'importance. Vous prenez un risque en acceptant l'offre, mais vous pariez intelligemment. Vous devez prendre la meilleure décision avec les informations que vous avez et laisser les dés rouler.

À long terme, vous vous en sortirez mieux en changeant qu'un concurrent qui décide de rester sur son premier choix. Bien que ce ne soit pas immédiatement évident, l'animateur vous rend en fait service en vous offrant une meilleure offre.

## **Le Problème des Philosophes Dînant**

Le problème des philosophes dînant est un exemple classique en informatique pour illustrer les problèmes de synchronisation. Il a été créé à l'origine par Edsger Dijkstra en 1965, qui l'a présenté à ses étudiants comme une poignée d'ordinateurs en compétition pour l'accès à des lecteurs de bandes partagés.

Imaginez cinq philosophes silencieux assis autour d'une table, chacun avec un bol de spaghetti. Il y a des fourchettes sur la table entre chaque paire de philosophes adjacents.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/at_the_table.png)
_Image courtesy of [adit.io](http://adit.io/posts/2013-05-11-The-Dining-Philosophers-Problem-With-Ron-Swanson.html)._

Chaque philosophe ne peut faire qu'une seule chose à la fois : penser et manger. Cependant, un philosophe ne peut manger des spaghetti que lorsqu'il a à la fois les fourchettes de gauche et de droite. Une fourchette ne peut être tenue que par un philosophe à la fois.

Après qu'un philosophe a fini de manger, il doit poser les fourchettes de gauche et de droite pour qu'elles soient disponibles pour les autres. Un philosophe peut prendre une fourchette dès qu'elle est disponible, mais ne peut commencer à manger que lorsqu'il a les deux fourchettes.

Les philosophes sont célèbres pour leurs appétits – ils peuvent tous manger sans fin et ne jamais être rassasiés. En plus de cela, les bols de spaghetti se remplissent magiquement peu importe la quantité mangée.

Le problème est, comment pouvez-vous vous assurer qu'aucun philosophe ne mourra de faim, et qu'ils peuvent continuer à manger et à penser pour toujours ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mae-mu-Pvclb-iHHYY-unsplash.jpg)

### Synchronisation et Interblocage

En termes simples, le problème des philosophes dînant est une illustration de la manière dont l'accès synchronisé à une ressource partagée peut entraîner la création d'une situation d'interblocage.

La **synchronisation** est utilisée pour contrôler l'accès concurrent à une ressource partagée. Cela est nécessaire dans toute situation où plusieurs acteurs indépendants peuvent être en compétition pour l'utilisation d'une ressource comme les fourchettes. Puisqu'il n'y a qu'une seule ressource disponible, nous utilisons la synchronisation pour prévenir la confusion et le chaos.

Un **interblocage** est un état du système où aucun progrès n'est possible. Cette situation peut se produire lorsque la synchronisation est imposée, et que de nombreux processus finissent par attendre une ressource partagée qui est détenue par un autre processus. Comme avec les philosophes qui sont soit bloqués en train de manger ou de penser, les processus continuent simplement d'attendre et n'exécutent rien de plus.

### Solutions

À première vue, il semble qu'il ne serait pas possible d'avoir un interblocage où tous les philosophes sont bloqués soit en train de manger ou de penser. Par exemple, le schéma que chaque philosophe pourrait suivre pourrait être :

> 1 : penser jusqu'à ce que la fourchette de gauche soit disponible ; lorsqu'elle l'est, la prendre ;  
>   
> 2 : penser jusqu'à ce que la fourchette de droite soit disponible ; lorsqu'elle l'est, la prendre ;  
>   
> 3 : lorsque les deux fourchettes sont tenues, manger pendant un temps fixe ;  
>   
> 4 : ensuite, poser la fourchette de droite ;  
>   
> 5 : ensuite, poser la fourchette de gauche ;  
>   
> 6 : répéter depuis le début.  
>   
> Source : [Wikipedia](https://en.wikipedia.org/wiki/Dining_philosophers_problem)

Il existe de nombreuses solutions possibles pour prévenir l'interblocage. Si nous regardons de près, un problème dans l'algorithme ci-dessus est que tous les philosophes ont une chance égale (ont la même priorité) d'acquérir une fourchette. Cela empêche quiconque d'acquérir deux fourchettes et tout le système s'arrête.

Voici quelques solutions possibles :

1. **Priorité** : Certains philosophes se voient attribuer une priorité plus élevée, afin d'augmenter les chances d'acquérir les deux fourchettes.
2. **Préemption** (Politesse) : Les philosophes renoncent à la fourchette acquise sans manger, au cas où l'autre fourchette ne serait pas disponible.
3. **Arbitrage** : Un médiateur attribue les fourchettes en veillant à ce que deux fourchettes soient données à une personne, au lieu d'une à plusieurs.

Maintenant que vous savez comment résoudre ces énigmes logiques, offrez-vous un bol sans fin de spaghetti. Vous l'avez mérité.