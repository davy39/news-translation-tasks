---
title: Comment créer des graphismes réalistes de Grand Theft Auto 5 avec le Deep Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-01T20:37:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-realistic-grand-theft-auto-5-graphics-with-deep-learning-cc092c4a69f0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BgjLO87og9PUnDNtU7Ip7Q.gif
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: gaming
  slug: gaming
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: Comment créer des graphismes réalistes de Grand Theft Auto 5 avec le Deep
  Learning
seo_desc: 'By Chintan Trivedi

  This project is a continuation of my previous article. In it, I explained how we
  can use CycleGANs for image style transfer, and apply it to convert Fortnite graphics
  and make it look like PUBG.

  CycleGAN is a type of Generative Adv...'
---

Par Chintan Trivedi

Ce projet est une continuation de mon [article précédent](https://towardsdatascience.com/turning-fortnite-into-pubg-with-deep-learning-cyclegan-2f9d339dcdb0). Dans cet article, j'ai expliqué comment nous pouvons utiliser les CycleGANs pour le transfert de style d'image, et l'appliquer pour convertir les graphismes de Fortnite et les faire ressembler à ceux de PUBG.

CycleGAN est un type de réseau antagoniste génératif capable d'imiter le style visuel d'une image et de le transférer sur une autre. Nous pouvons l'utiliser pour faire ressembler les graphismes d'un jeu à ceux d'un autre jeu ou du monde réel.

Dans cet article, je voulais partager quelques résultats supplémentaires en utilisant le même [algorithme CycleGAN](https://junyanz.github.io/CycleGAN/) que j'ai couvert dans mon travail précédent. Tout d'abord, j'essaierai d'améliorer les graphismes de GTA 5 en les adaptant pour qu'ils ressemblent au monde réel. Ensuite, je couvrirai comment nous pouvons obtenir les mêmes résultats photoréalistes, sans avoir à rendre des graphismes GTA très détaillés en premier lieu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EZ0j8XVuf30B-ar3GXCIzg.png)
_Les deux ensembles de données que j'ai utilisés pour cela sont disponibles à [ce lien](https://junyanz.github.io/CycleGAN/" rel="noopener" target="_blank" title=") sur la page du projet de l'auteur original._

Pour la première tâche, j'ai pris des captures d'écran du jeu comme notre domaine source que nous voulons convertir en quelque chose de photoréaliste. Le domaine cible provient de l'ensemble de données cityscapes qui représente le monde réel (que nous visons à faire ressembler à notre jeu).

### Résultats de CycleGAN

![Image](https://cdn-media-1.freecodecamp.org/images/1*3ZD4OtDtLVqQWExjydt6OA.gif)

Sur la base d'environ trois jours d'entraînement pour environ 100 époques, le modèle Cyclegan semble faire un très bon travail d'adaptation de GTA au domaine du monde réel. J'aime vraiment comment les petits détails ne sont pas perdus dans cette traduction et l'image conserve sa netteté même à une si basse résolution.

Le principal inconvénient est que ce réseau de neurones s'est avéré assez matérialiste : il hallucine un logo Mercedes partout, gâchant la conversion presque parfaite de GTA au monde réel. (C'est parce que l'ensemble de données cityscapes a été collecté par un propriétaire de Mercedes.)

### Comment obtenir les mêmes graphismes photoréalistes avec moins d'efforts

Bien que cette approche puisse sembler très prometteuse pour améliorer les graphismes de jeu, je ne pense pas que le vrai potentiel réside dans le suivi de ce pipeline. Par là, je veux dire qu'il semble peu pratique de rendre une image aussi hautement détaillée puis de la convertir en autre chose.

Ne serait-il pas préférable de synthétiser une image de qualité similaire mais avec beaucoup moins de temps et d'efforts dans la conception du jeu en premier lieu ? Je pense que le vrai potentiel réside dans le rendu d'objets avec peu de détails et laisser le réseau de neurones synthétiser l'image finale à partir de ce rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1DZl_0oqSQzKhUuL5GUh5g.png)

Ainsi, sur la base des étiquettes sémantiques disponibles dans l'ensemble de données cityscapes, j'ai segmenté des objets dans une capture d'écran de GTA, nous donnant une représentation de graphismes à faible détail. Considérez cela comme un rendu de jeu de seulement quelques objets, comme la route, la voiture, les maisons, le ciel, et ainsi de suite sans les concevoir en détail. Cela servira d'entrée à notre modèle de transfert de style d'image au lieu de la capture d'écran très détaillée du jeu.

Voyons quelle qualité d'images finales peut être générée à partir de telles cartes sémantiques à faible détail en utilisant les CycleGANs.

### Résultats de la synthèse d'image à partir de cartes sémantiques

![Image](https://cdn-media-1.freecodecamp.org/images/1*kNx9TrAXmaGHUeivjwQReg.gif)
_Recréation de scènes photoréalistes à partir des cartes sémantiques de GTA 5._

Voici quelques exemples de l'apparence lorsque nous recréons les graphismes de GTA à partir de cartes sémantiques. Notez que je n'ai pas créé ces cartes à la main. Cela semblait vraiment fastidieux, alors j'ai simplement laissé un autre modèle CycleGAN le faire (il est formé pour effectuer la segmentation d'image en utilisant l'ensemble de données cityscapes).

Cela semble être une bonne conversion de loin, mais en regardant de près, il est assez évident que l'image est fausse et manque de tout type de détails.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XqPMGvpKwd4U7uN93dk6yQ.png)

Maintenant, ces résultats sont en 256p et ont été générés sur un GPU avec 8 Go de mémoire. Cependant, les auteurs de l'article original ont montré qu'il est possible de créer une image beaucoup plus détaillée de 2048 x 1024p en utilisant un GPU avec plus de 24 Go de mémoire. Il utilise la version supervisée de CycleGAN, appelée [pix2pixHD](https://github.com/NVIDIA/pix2pixHD), qui est formée pour effectuer la même tâche. Et l'image fausse semble assez convaincante !

![Image](https://cdn-media-1.freecodecamp.org/images/1*SJ09ZfgwAUw52XoL07jDGA.png)
_[Voici la vidéo complète](https://www.youtube.com/watch?v=3AIpPlzM_qs&amp;t=23s" rel="noopener" target="_blank" title=") téléchargée par les auteurs de cet article._

### Conclusion

Les GANs ont un grand potentiel pour changer la façon dont l'industrie du divertissement produira du contenu à l'avenir. Ils sont capables de produire des résultats bien meilleurs que les humains et en beaucoup moins de temps.

La même chose est applicable à l'industrie du jeu également. Je suis sûr que dans quelques années, cela révolutionnera la façon dont les graphismes de jeu sont générés. Il sera beaucoup plus facile de simplement imiter le monde réel que de tout recréer à partir de zéro.

Une fois que nous aurons atteint cela, le lancement de nouveaux jeux sera également beaucoup plus rapide. Des temps passionnants nous attendent avec ces avancées en Deep Learning !

#### Plus de résultats en format vidéo

Tous les résultats ci-dessus et plus encore peuvent être trouvés sur ma [chaîne YouTube](https://www.youtube.com/c/DeepGamingAI) et dans la vidéo intégrée ci-dessous. Si vous avez aimé, n'hésitez pas à [vous abonner](http://www.youtube.com/subscription_center?add_user=DeepGamingAI) à ma chaîne pour suivre plus de mon travail.

Merci d'avoir lu ! Si vous avez aimé cet article, veuillez me suivre sur [Medium](https://medium.com/@chintan.t93), [GitHub](https://github.com/ChintanTrivedi), ou abonnez-vous à ma [chaîne YouTube](http://youtube.com/c/DeepGamingAI).