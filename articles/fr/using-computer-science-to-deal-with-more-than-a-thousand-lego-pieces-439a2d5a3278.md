---
title: Comment j'ai utilisé la SCIENCE (informatique) pour gérer plus de mille pièces
  Lego
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T17:07:47.000Z'
originalURL: https://freecodecamp.org/news/using-computer-science-to-deal-with-more-than-a-thousand-lego-pieces-439a2d5a3278
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nnr2BTzLiLncURCANSAOqQ.png
tags:
- name: Computer Science
  slug: computer-science
- name: Life lessons
  slug: life-lessons
- name: play
  slug: play
- name: 'Science '
  slug: science
- name: 'tech '
  slug: tech
seo_title: Comment j'ai utilisé la SCIENCE (informatique) pour gérer plus de mille
  pièces Lego
seo_desc: 'By Eumir Gaspar

  Most kids absolutely LOVE Legos. My son has been playing with the Duplo ones, but
  we have since recently “upgraded” him to the normal ones. Since we didn’t have a
  collection of regular legos yet, we opted to just inherit someone else’...'
---

Par Eumir Gaspar

La plupart des enfants adorent les [Legos](https://www.lego.com). Mon fils a joué avec les [Duplo](https://www.lego.com/en-au/themes/duplo), mais nous l'avons récemment "mis à niveau" vers les versions normales. Comme nous n'avions pas encore de collection de Legos classiques, nous avons choisi d'hériter de celle de quelqu'un d'autre. Nous avons enfin eu notre chance lorsque nous avons trouvé quelqu'un qui vendait la collection de Legos de ses enfants, car ils étaient trop grands pour eux.

![Image](https://cdn-media-1.freecodecamp.org/images/LqBNo6G6BJtK7N1F6MwlWi-nSgAhrLj70NWH)
_Ce n'est que la moitié de la collection. La moitié était déjà triée par couleurs, mais pas celle-ci._

Puisque nous venions de recevoir plus de mille pièces, nous devions les trier par couleur pour les organiser. Je n'allais certainement pas [les trier par pièce ou les cataloguer](http://brickarchitect.com/guide/bricks/more/), car cela aurait pris une éternité.

Face à cette tâche insurmontable, nous avons décidé de nous y attaquer. Nous avons commencé à trier en ramassant toutes les briques vertes et en les collectant dans un bassin pour les laver. Oui, c'était une très vieille collection, donc elle était très poussiéreuse.

Le plan d'attaque initial était le suivant :

* Je trie les briques et ma femme les nettoie ainsi que les étagères incluses. Oui, l'accord incluait 3 étagères, 9 boîtes, 1 sac Lego (sur la photo) et 1 tête Lego en plus de probablement cinq à dix mille pièces.
* Ensuite, nous les rangeons — facile, non ?

Cela semblait être un bon plan, jusqu'à ce que je réalise que le tri par couleur de la manière dont je le faisais était trop lent. Je ne ramassais qu'une seule couleur à la fois. J'avais probablement trié seulement environ 30 briques et cela m'avait pris cinq minutes. Imaginez combien de temps cela aurait pris pour finir avec les autres couleurs comme le noir, le gris, le rouge et le bleu !

J'ai donc dû repenser mon plan. Je plaisantais avec quelques amis qui ont alors mentionné que je faisais probablement un [tri à bulles](https://en.wikipedia.org/wiki/Bubble_sort), qui est l'un des algorithmes de tri les plus lents (oui, il y en a d'autres encore plus lents !). J'ai ri de la blague, puis j'ai réalisé que je pourrais peut-être utiliser mes connaissances en informatique ici — du moins ce qu'il en reste ! L'université, c'était il y a longtemps, donc je savais que je devrais improviser.

### Entrée en jeu du scaling horizontal

J'ai dit à tout le monde d'arrêter ce qu'ils faisaient et de m'aider à trier le sac. Cela signifiait qu'il y avait maintenant plus de personnes qui triaient, donc j'ai essentiellement [scalé horizontalement](https://en.wikipedia.org/wiki/Scalability#Horizontal_and_vertical_scaling) en ajoutant plus de ressources pour terminer le travail.

En tant que développeur web, j'ai vu cela comme une solution courante à un problème de charge du serveur.

Lorsque votre serveur est surchargé par un grand nombre de trafic entrant, vous avez généralement deux options : le scaling vertical ou horizontal.

Le scaling vertical signifie que vous ajoutez essentiellement plus de puissance à votre serveur. Par exemple, si vous utilisez AWS, au lieu d'avoir un `t2.micro` qui n'a qu'un seul CPU et 1 Go de RAM, vous le mettez à niveau vers un `t2.xlarge` qui a 4 CPU et 16 Go de RAM.

![Image](https://cdn-media-1.freecodecamp.org/images/9DhR1m-V-piFE7y0m1-L-8notdcAfY6VLeCP)
_[Les types d'instances Amazon EC2](https://aws.amazon.com/ec2/instance-types/" rel="noopener" target="_blank" title=")_

Le scaling horizontal signifie que vous ajoutez simplement plus de ressources. Donc, au lieu de mettre à niveau votre instance `t2.micro` unique, vous en ajoutez 5 de plus pour accommoder la charge.

Les deux ont leurs cas d'utilisation, mais pour cette instance spécifique, le scaling horizontal était la solution.

Je veux dire, je n'aurais pas pu scaler verticalement en ajoutant plus de puissance cérébrale, donc le seul choix était de scaler horizontalement en ajoutant plus de personnes.

Après cinq minutes de tri, j'ai remarqué que nous avions fait un certain progrès. Ce n'était pas suffisant pour moi, cependant. Le temps passait et j'étais fatigué. Nous devions aller plus vite !

### Algorithme diviser pour régner

J'ai réfléchi. Nous étions trois avec un grand sac plein de briques devant nous. J'ai estimé qu'il y avait environ deux mille pièces à ce stade. Et bien que nous ayons fait quelques progrès au cours des cinq dernières minutes, nous étions toujours face à des heures de tri.

J'ai depuis changé ma technique initiale de simplement chercher des blocs verts. Au lieu de cela, je jetais un rapide coup d'œil à la couleur qui semblait être la majorité, et j'en prenais autant que possible avec ma main. Après avoir mis les briques dans leur panier de couleur approprié, je regardais le tas et choisissais à nouveau la « majorité ». Cela changeait généralement, car après avoir pris un tas de rouges, par exemple, il y avait moins de rouges. La majorité suivante aurait pu être bleue ou verte, par exemple.

Cela semblait bien. Mais après l'avoir analysé, je regardais essentiellement deux mille pièces, je prenais le nombre maximum d'une couleur, je prenais cette couleur et je la soustrayais du tas. Mon traitement était lent, car comment obtenir la majorité sans compter ou estimer ?

Comme je prenais trop de charge cognitive, je ralentissais. J'ai donc arrêté de chercher la couleur avec le plus de briques et j'ai simplement choisi une couleur au hasard chaque fois que je vidais la poignée de briques que je venais de collecter. Cela a accéléré un peu mon traitement, mais je pensais que nous pouvions encore améliorer.

Donc, [diviser pour régner](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) était la solution. En termes d'informatique, cela signifiait un algorithme qui décomposait un énorme problème en petits morceaux afin qu'ils soient suffisamment simples à résoudre en un temps plus rapide.

Supposons que votre site accepte des fichiers zip téléchargés par les utilisateurs avec des photos et les traite. Si votre serveur acceptait le fichier zip, le décompressait et le traitait dès que vous l'avez téléchargé, tout le monde devrait attendre qu'il termine. Bien sûr, vous pouvez scaler horizontalement ou verticalement votre serveur, mais le temps d'attente est inutile. De plus, que se passe-t-il lorsqu'un utilisateur télécharge un fichier zip avec 100 photos ?

Vous pouvez résoudre ce problème en utilisant une technique de diviser pour régner. Tout d'abord, vous déléguez le traitement à une infrastructure de travaux différés comme [ActiveJob](http://guides.rubyonrails.org/active_job_basics.html) de Rails. Ou si vous n'utilisez pas Rails, [Sidekiq](https://github.com/mperham/sidekiq). Cependant, ce travail prendrait encore beaucoup de temps s'il y avait 100 photos, et il y aurait la possibilité que votre worker meurt sous la charge de travail.

Une solution serait d'avoir un travail qui le décompresse, **puis** met en file d'attente chacune des photos à traiter en tant que travail séparé. Maintenant, au lieu que votre worker doive traiter 100 photos lui-même, il met 100 petits travaux de traitement de photos individuelles dans la file d'attente, qui peuvent ensuite être pris en charge par d'autres workers.

Avec cela en tête, j'ai fait un accord de chaîne de montage avec mon fils : il devait prendre une poignée (ou deux) de briques dans le sac et les verser dans mon coin. Cela signifiait que je n'avais qu'environ 50 briques à trier, ce qui était plus facile et plus rapide — principalement parce qu'à ce stade, je connaissais la couleur avec le plus de briques : le gris.

![Image](https://cdn-media-1.freecodecamp.org/images/nfwkLNviXS9NJzYYvlZLwoK2Ultncxb7cyoV)
_La couleur de bloc la plus courante était le gris._

Alors, qu'est-ce que cela changeait si je savais que c'était gris ? Eh bien, cela signifiait que je n'avais qu'à ramasser toutes les briques rouges, vertes, jaunes, bleues, noires et blanches. Lorsque je n'avais plus que des briques grises, je mettais les briques restantes dans la boîte grise — cela m'a évité de trier une couleur de moins que je n'aurais pas pu faire à plus grande échelle.

#### Une heure plus tard...

C'est terminé ! Maintenant, nous devions simplement les nettoyer. Le plan initial était :

* Verser une boîte de couleurs dans un bassin.
* Laver avec de l'eau et du savon
* Sécher

Quel était le problème ici ? Je vous laisse deviner.

Toujours là ? D'accord. Si nous lavions avec de l'eau et du savon, cela signifiait que nous devions rincer le savon — ce qui signifiait que nous devions les laver deux fois ! Pas question ! J'ai donc décidé de ne pas ajouter de savon mais de laver simplement à fond avec de l'eau tiède.

Le plan modifié était :

* Verser une boîte de couleurs dans un bassin
* Laver à fond avec de l'eau
* Sécher

Passons au problème suivant : sécher les Legos.

### La force centrifuge à la rescousse !

Initialement, nous avons essayé de sécher les pièces avec une serviette. Ce n'était pas très efficace. Ensuite, nous avons utilisé un sèche-cheveux et soufflé de l'air chaud sur les pièces. C'était acceptable, mais cela ne séchait toujours pas les pièces — nous étions désespérés et avons presque décidé de simplement les étaler toutes sur le sol et laisser l'eau s'évaporer.

Sauf qu'il faisait automne, donc il n'aurait pas fait assez chaud. Alors que je réfléchissais à la manière de sécher des milliers de pièces Lego, je me suis soudainement souvenu comment je séchais les feuilles de salade en utilisant une essoreuse à salade. « J'aimerais pouvoir utiliser l'essoreuse à salade », ai-je pensé. Puis cela m'est venu : une [essoreuse à salade](https://en.wikipedia.org/wiki/Salad_spinner) fonctionne en utilisant [la force centrifuge pour séparer l'eau des feuilles](https://en.wikipedia.org/wiki/Centrifugal_force). Je pourrais faire la même chose !

J'ai enveloppé les pièces Lego dans une serviette et je les ai sécurisées en transformant la serviette en un géant emballage de bonbon. J'ai marché sur une extrémité de la serviette, j'ai tiré l'autre extrémité aussi fort que possible et j'ai commencé à faire tourner la serviette.

Devinez quoi — cela a vraiment fonctionné ! J'ai pu voir la serviette soudainement devenir humide alors que l'eau des pièces s'envolait et se retrouvait dans la serviette. DE LA SCIENCE !

![Image](https://cdn-media-1.freecodecamp.org/images/HEp6MVkDlD9fjO7zFMgzQ0Wj1Xwpl4vcfFi1)
_DE LA SCIENCE !_

Les Legos n'étaient pas complètement secs, bien sûr, donc j'ai encore dû utiliser le sèche-cheveux pour aider les dernières gouttelettes à s'évaporer. Mais cela allait — la partie difficile était terminée.

Je n'aurais jamais pensé utiliser mes connaissances en informatique pour quelque chose comme trier des Legos. En tout cas, ce fut une bonne et amusante expérience de scaler horizontalement, d'utiliser une stratégie de diviser pour régner, et même de faire appel à la force centrifuge pour organiser la nouvelle collection de Legos héritée de mon fils. Je n'ai pas hâte au jour où il les mélangera toutes et où nous devrons les trier à nouveau, par contre !