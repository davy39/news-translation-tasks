---
title: Programmer le génome avec CRISPR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-18T18:19:25.000Z'
originalURL: https://freecodecamp.org/news/programming-the-genome-with-crispr-bd567a214e2a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jEBmdQVQvOeQba3Msz5f5g.jpeg
tags:
- name: coding
  slug: coding
- name: Genetics
  slug: genetics
- name: 'Science '
  slug: science
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: Programmer le génome avec CRISPR
seo_desc: 'By Josh McMenemy

  How scientists edit genomes with the help of computers


  CRISPR (pronounced “crisper”) is part of a bacterial immune system evolved to ‘remember’
  and remove invading viral DNA.

  Its name is short for ‘Clustered Regularly Interspaced Sh...'
---

Par Josh McMenemy

#### Comment les scientifiques éditent les génomes à l'aide d'ordinateurs

![Image](https://cdn-media-1.freecodecamp.org/images/1*jEBmdQVQvOeQba3Msz5f5g.jpeg)

CRISPR (prononcé « crisper ») fait partie d'un système immunitaire bactérien évolué pour « se souvenir » et éliminer l'ADN viral envahissant.

Son nom est l'abréviation de « Clustered Regularly Interspaced Short Palindromic Repeats ». Mais malgré son acronyme complexe et ses origines biologiques, son application en ingénierie est simple. Pour commencer, il n'y a qu'une seule protéine à comprendre — Cas9.

Cas9 recherche une séquence d'ADN spécifiée et la coupe en brisant les deux brins de la molécule d'ADN. Cette protéine est utile aux chercheurs car ils peuvent la « programmer » pour cibler n'importe quelle séquence d'ADN. Une molécule d'ARNsg (ARN « single guide ») détermine la séquence à laquelle Cas9 se lie. L'ARN est une molécule biologique similaire à l'ADN, qui peut se lier aux protéines et à l'ADN.

Les ARNsg sont des séquences courtes avec une région constante et une région variable. La région constante attache l'ARNsg à la protéine Cas9. La région variable fait en sorte que Cas9 se lie à la séquence d'ADN qui lui est complémentaire (voir le diagramme ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/1*HatelyoaNAjVo1jR4KWQtw.jpeg)
_La protéine Cas9 liée à l'ADN lorsque la séquence PAM est sur le brin direct (haut). La séquence en gras est la séquence cible, la séquence verte est l'ARNsg, et les trois caractères bleus sont le PAM. Les triangles montrent où Cas9 va couper l'ADN._

La fabrication d'ARNsg est bon marché et rapide. Cela permet aux chercheurs de mettre en place rapidement une expérience Cas9 qui coupe n'importe quelle séquence d'ADN. Enfin, pas vraiment n'importe quelle séquence. Il y a une petite contrainte : la séquence cible doit être flanquée du PAM (protospacer adjacent motif) correct — une courte séquence d'ADN.

[_Streptococcus pyogenes_](https://en.wikipedia.org/wiki/Streptococcus_pyogenes) est une espèce infectieuse de bactérie. Dans la version de Cas9 qu'elle produit, le motif PAM est « NGG », où N est n'importe quel nucléotide (les « lettres » qui composent l'ADN).

Heureusement, le motif « NGG » apparaît environ une fois tous les 42 paires de bases dans le génome humain. Cela signifie que les chercheurs peuvent trouver un site cible près de presque toutes les séquences d'intérêt.

Selon la configuration expérimentale, ces coupures dans l'ADN peuvent soit causer un **changement aléatoire**, soit un **changement précis** de la séquence d'ADN (plus d'informations à ce sujet plus tard).

Avant de plonger dans l'écriture de ce programme, je recommande d'étudier le diagramme Cas9 ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bkb6hf7coqumUDNdxJ3CsQ.jpeg)
_La protéine Cas9 liée à une séquence d'ADN lorsque la séquence PAM est sur le brin inverse (bas)._

Notez que l'ADN et l'ARN ont une directionnalité basée sur leur structure chimique. Une extrémité de la molécule est appelée extrémité 5' (« five-prime »), et l'autre est appelée extrémité 3' (« three-prime »). Cela est important, car les séquences 5'— AGG — 3' ne sont pas les mêmes que 3' — AGG — 5'.

Par convention, les séquences d'ADN et d'ARN sont supposées être écrites de 5' à 3' sauf indication contraire. Les séquences lues dans la direction 5' — 3' sont appelées séquences « directes ». Les séquences lues dans l'autre sens (3' — 5') sont appelées séquences « inverses ». Il s'agit d'une convention arbitraire.

Le diagramme ci-dessus montre un exemple de Cas9 lié lorsque le PAM est sur le brin inverse (bas).

### Votre premier programme CRISPR

#### Le scénario

Un scientifique a une séquence d'ADN d'intérêt et souhaite une liste de toutes les cibles CRISPR contenues dans la séquence. Trouver chaque cible à la main est fastidieux et sujet aux erreurs.

Le scientifique souhaite un programme simple où il peut entrer une séquence d'ADN et obtenir tous les sites cibles possibles de Cas9. Le scientifique aimerait également avoir la position de coupure et la séquence PAM pour chaque site cible.

```
ENTRÉE EXEMPLE (de la Figure 1) : 'CCACGGTTTCTGTAGCCCCATACTTTGGATG'
```

```
SORTIE EXEMPLE : [{    'cut_pos': 6,    'pam_seq': 'TGG',    'target_seq': 'GTATGGGGCTACAGAAACCG',    'strand': 'reverse'  }, {    'cut_pos': 22,    'pam_seq': 'TGG',    'target_seq': 'GTTTCTGTAGCCCCATACTT',    'strand': 'forward'  }]
```

Tout d'abord, comment trouver les cibles CRISPR dans la séquence ? Rappelez-vous que la protéine Cas9 peut se lier partout où il y a un motif « NGG ».

La première étape consiste à parcourir la séquence à la recherche de correspondances. Lorsque le programme trouve une correspondance « NGG », nous voulons soustraire trois positions du début du site PAM, car c'est là que Cas9 coupe l'ADN.

Ensuite, nous voulons enregistrer les vingt paires de bases avant le PAM comme séquence cible. Cela semble bien ?

Eh bien, l'algorithme décrit ci-dessus manquerait en réalité environ la moitié de tous les sites CRISPR — parce que l'ADN est double brin. Cela signifie que si un « CCN » est la séquence sur le brin direct, alors « NGG » est la séquence sur le brin inverse.

Le programme doit également rechercher « CCN » en utilisant une logique similaire pour le brin inverse.

#### Exemple de programme

### Toutes les cibles CRISPR ne sont pas égales

Lorsque CRISPR a commencé à se populariser, les chercheurs sélectionnaient souvent des cibles à la main sur leur ordinateur. La conception de l'ARNsg optimal est désormais devenue beaucoup plus complexe. Voici de brèves introductions à cette complexité.

#### Cibles hors cible

Les chercheurs ont rapidement réalisé que Cas9 pouvait parfois se lier et couper à des loci qui ne correspondaient pas exactement à la séquence cible. Ces [coupures hors cible](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4320661/) pourraient causer des changements non intentionnels dans l'expérience d'un chercheur (ou potentiellement dans le génome d'un patient dans le cas d'une thérapie !)

Pour concevoir un bon guide, un programme doit examiner l'ensemble du génome (qui est d'environ 3 milliards de nucléotides pour les humains) afin de calculer un score hors cible. Les chercheurs ont également récemment [modifié la protéine Cas9](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4714946/) pour réduire l'activité hors cible.

#### Knockout

Lorsque Cas9 se lie, il crée une coupure en provoquant une cassure double brin de la molécule d'ADN. La plupart du temps, une cellule peut réparer cette cassure par une voie biochimique (appelée jonction d'extrémités non homologues, ou NHEJ).

Cette voie n'est pas toujours parfaite, et parfois lorsque Cas9 coupe, le processus de réparation provoque une petite insertion ou délétion dans la séquence d'ADN. Dans une région codante pour une protéine de l'ADN, ces petites insertions et délétions provoquent une mutation par décalage du cadre de lecture — ce qui perturbera souvent la fonction de la protéine.

Les chercheurs provoquent souvent un knockout d'un gène pour comprendre comment une protéine affecte une fonction cellulaire spécifique ou un phénotype. Créer une édition knockout [ajoute des contraintes supplémentaires à la conception de l'ARNsg](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4262738/), car maintenant le guide doit se situer dans la région codante du gène.

#### Édition

Au lieu de provoquer un knockout d'un gène, il y a de nombreuses fois où un scientifique souhaite faire une édition de précision. Cela est particulièrement utile lorsqu'on essaie de corriger une mutation causant une maladie. La meilleure façon de faire cela est encore à l'étude. La plupart des méthodes impliquent l'ajout [d'un morceau donneur supplémentaire d'ADN](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5363683/).

#### Score sur cible

Certaines séquences d'ARNsg feront en sorte que Cas9 coupe mieux que d'autres. Les chercheurs ont [comparé l'efficacité de coupure](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4744125/) sur des milliers de cibles Cas9 pour créer des modèles prédictifs de l'efficacité de coupure d'un ARNsg.

Microsoft soutient même un [dépôt open source](https://github.com/MicrosoftResearch/Azimuth) pour la « Modélisation Prédictive Basée sur l'Apprentissage Automatique de l'Efficacité des Guides CRISPR/Cas9 ».

#### Autres systèmes CRISPR-Cas

Les chercheurs ont [découvert des systèmes CRISPR-Cas dans d'autres bactéries](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4638220/). Ces autres systèmes ont différents PAM.

### Notes finales

J'espère que vous avez appris quelque chose de nouveau ! Si vous souhaitez en savoir plus sur la biologie, les applications médicales, les applications commerciales ou les implications éthiques de l'ingénierie génomique CRISPR-Cas, je vous recommande de lire [A Crack in Creation](http://www.acrackincreation.com/) de Jennifer Doudna et Samuel Sternberg. Jennifer Doudna est l'une des premières découvreurs des fondements de CRISPR.

#### À propos de l'auteur

J'étais auparavant chercheur de premier cycle dans le [laboratoire Gersbach](http://gersbach.bme.duke.edu/) à l'Université Duke, et je suis actuellement ingénieur logiciel chez [Synthego](http://www.synthego.com/).