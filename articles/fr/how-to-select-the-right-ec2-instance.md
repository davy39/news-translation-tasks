---
title: Comment choisir la bonne instance EC2 – Un guide sur les instances EC2 et leurs
  capacités
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2022-12-15T19:08:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-select-the-right-ec2-instance
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-photo.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: ec2
  slug: ec2
seo_title: Comment choisir la bonne instance EC2 – Un guide sur les instances EC2
  et leurs capacités
seo_desc: 'EC2 (Elastic Compute Cloud) is the most widely-used compute service from
  AWS. It''s also one of the oldest services launched by AWS, as it was started in
  2006.

  In this article, I will go through some things you should consider when selecting
  an EC2 in...'
---

EC2 (Elastic Compute Cloud) est le service de calcul le plus largement utilisé d'AWS. C'est également l'un des services les plus anciens lancés par AWS, puisqu'il a été lancé en 2006.

Dans cet article, je vais passer en revue quelques éléments à considérer lors de la sélection d'une instance EC2.

Vous pouvez considérer une instance EC2 comme n'étant pas trop différente de votre ordinateur personnel. Si vous allez acheter un ordinateur, trois considérations techniques générales peuvent vous venir à l'esprit (en ignorant bien sûr toute préférence esthétique ou de design que vous pourriez avoir) :

1. Quelle quantité de traitement peut-elle gérer ?

2. Quelle quantité de mémoire possède-t-elle ?

3. Quelle quantité de stockage possède-t-elle ?

Ces trois questions devraient également vous venir à l'esprit lors de la sélection d'une instance EC2. La différence étant que vous ne louez l'instance d'AWS que temporairement, au lieu de l'acheter comme vous le feriez avec un ordinateur personnel.

Chaque instance EC2 est composée de :

1. CPU – quelle quantité de traitement peut être réalisée

2. Mémoire

3. Stockage – cela ne s'applique qu'à certaines instances qui ont un stockage physiquement attaché (appelé [instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)). Pour les autres instances EC2, vous devrez choisir un stockage réseau en utilisant EBS (Elastic Block Storage) séparément.

## Calcul, Mémoire et Stockage – Une Analogie

Une bonne analogie pour une instance EC2 est votre bureau de travail.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F44e98a5c-f6fb-4f23-8840-477a52ef0b6c_1257x690.png align="left")

Votre cerveau est le calcul, la surface de votre bureau est la mémoire, et votre tiroir de bureau est le stockage. Notez que cette analogie (comme toutes les analogies) a ses limites. Son but est de séparer clairement le rôle du calcul, de la mémoire et du stockage dans une instance EC2.

Que signifie exactement le calcul ? Le calcul concerne le *parallélisme* – la capacité à exécuter plusieurs tâches simultanément.

Les cerveaux humains peuvent gérer un certain niveau de parallélisme. Vous pourriez être capable de parler au téléphone tout en prenant des notes simultanément, par exemple. Vous ne pouvez pas, cependant, écrire deux lettres différentes simultanément, ou parler au téléphone tout en prenant des notes et en lisant un livre.

Ces activités ne peuvent pas être exécutées en parallèle parce que notre cerveau peut être grossièrement considéré comme un CPU avec un seul cœur. Pour augmenter le calcul, nous devons augmenter le parallélisme, et cela peut être réalisé en ayant plusieurs cœurs de CPU. Plus de cœurs égalent plus de parallélisme, ce qui égalent plus de puissance de calcul.

La mémoire et le stockage sont théoriquement la même chose. Nous les utilisons tous les deux pour stocker des données. Pratiquement, cependant, ils sont des pièces physiquement distinctes d'infrastructure simplement parce qu'il n'existe pas de dispositif de stockage unique qui soit à la fois rapide et non volatile.

La mémoire est rapide et volatile tandis que le stockage est lent et non volatile. Les choses gardées sur la surface de votre bureau sont rapidement et facilement accessibles, tout comme les données dans la mémoire d'un ordinateur. Mais tout ce qui est laissé sur votre bureau pendant la nuit dans un bureau occupé risque d'être déplacé, perdu ou volé. La surface de votre bureau, tout comme la mémoire d'un ordinateur, est volatile.

Le stockage, en revanche, est non volatile mais plus lent à lire/écrire. Tout comme les articles dans vos tiroirs de bureau sont moins susceptibles de disparaître mais prennent plus de temps à être récupérés.

## Comment choisir la bonne instance EC2

Ainsi, le CPU, la mémoire et parfois le stockage sont les trois leviers que vous pouvez actionner lors de la sélection d'une instance EC2. Rappelez-vous que le stockage est souvent sélectionné séparément de l'instance EC2 en utilisant des volumes EBS, sauf pour les instances optimisées pour le stockage qui ont un stockage physiquement attaché.

Lorsque vous sélectionnez un type d'instance, vous sélectionnez effectivement **le prix le plus bas par unité de la métrique la plus importante pour votre charge de travail**. Cette métrique peut être la performance CPU/GPU, la mémoire ou le stockage.

Il existe cinq types d'instances AWS :

* usage général : En choisissant une instance d'usage général, vous adoptez une approche équilibrée et n'optimisez pour aucune métrique en particulier.

* optimisées pour le calcul : En choisissant une instance optimisée pour le calcul, vous optimisez pour le prix le plus bas par unité de performance CPU (nombre de cœurs CPU).

* calcul accéléré : En choisissant une instance de calcul accéléré, vous optimisez pour le prix le plus bas par unité de performance GPU (considerez cela comme un CPU spécialisé nécessaire pour les charges de travail de calcul haute performance).

* optimisées pour le stockage : En choisissant une instance optimisée pour le stockage, vous optimisez pour le prix le plus bas par unité de capacité et d'efficacité de stockage.

* optimisées pour la mémoire : Et en choisissant une instance optimisée pour la mémoire, vous optimisez pour le prix le plus bas par unité de mémoire.

Examinons les types d'instances plus en détail.

AWS propose un excellent aperçu de cela [ici](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) que j'ai résumé ci-dessous :

1. **Usage Général** – Pour les charges de travail qui nécessitent un équilibre entre calcul, mémoire et réseau. Cas d'utilisation idéal : serveurs web.

2. **Optimisées pour le Calcul** – Pour les charges de travail qui nécessitent des processeurs haute performance. Coût le plus bas par nombre de cœurs CPU. Idéal pour les charges de travail intensives en calcul comme la modélisation scientifique et le gaming.

3. **Calcul Accéléré** – Pour les charges de travail qui nécessitent des quantités encore plus grandes de ressources de calcul que les instances optimisées pour le calcul. Ce type d'instance utilise des GPUs (unités de traitement graphique) qui sont des CPUs spécialisés conçus pour l'apprentissage automatique et les charges de travail de calcul haute performance.

4. **Optimisées pour le Stockage** - Pour les charges de travail qui nécessitent des taux élevés de lectures et d'écritures pour de grandes quantités de données, c'est-à-dire un IOPS élevé (Input/Output Operations per second).

Contrairement aux autres instances, celles-ci n'utilisent pas de volumes EBS séparés pour le stockage. Au lieu de cela, elles sont livrées avec des volumes de stockage physiquement attachés (appelés [instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)). Cela signifie que les données n'ont pas à passer par un réseau, leur permettant d'atteindre un IOPS élevé.

Cas d'utilisation idéal : les bases de données NoSQL – comme Elasticsearch, MongoDB, Cassandra et certaines applications d'entrepôt de données. Les volumes de stockage d'instance, cependant, ont un piège : toute donnée stockée là ne persiste pas au-delà de la vie de l'instance. Ainsi, si l'instance s'arrête, hiberne, se termine ou échoue, vous perdez toutes les données sur cette instance.

Le cas d'utilisation idéal pour les instances optimisées pour le stockage est donc pour les charges de travail qui nécessitent un IOPS élevé **et** peuvent tolérer la défaillance d'une instance (généralement en ayant des données répliquées sur une autre instance pour la redondance). 5. **Optimisées pour la Mémoire** – Pour les charges de travail qui nécessitent de grandes quantités de RAM. Coût le plus bas par unité de RAM. Idéal pour les bases de données en mémoire, les caches, les bases de données SQL.

## Anatomie d'un Nom d'Instance EC2

Vous avez peut-être rencontré des noms d'instances EC2 comme t2.nano, r6a.large ou i3en.6xlarge. Que signifient exactement les lettres et les chiffres ?

Prenons un nom complexe comme i3en.6xlarge comme exemple et décomposons-le.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5f1844b-80a3-4f87-b7de-1027f4c16aec_1280x720.jpeg align="left")

*Anatomie d'un nom d'instance EC2 décomposée*

### Famille d'Instance

En lisant de gauche à droite, la première lettre est la famille d'instance. Chaque famille appartient à un seul des types d'instances, c'est-à-dire usage général, optimisées pour le calcul, calcul accéléré, optimisées pour le stockage ou optimisées pour la mémoire.

Il n'est pas nécessaire de bachoter pour apprendre quelle famille d'instance appartient à quel type d'instance. À mesure que vous travaillez davantage avec AWS, cela deviendra presque une seconde nature. Vous pouvez consulter [ici](https://aws.amazon.com/ec2/instance-types/) pour référence si vous le souhaitez.

L'instance i3en.6xlarge ci-dessus appartient à la famille « i », qui est une instance optimisée pour le stockage.

### Génération d'Instance

Ceci est un nombre qui indique la génération de l'instance. Plus le nombre est élevé, plus la génération est récente.

Lorsque vous avez le choix entre différentes générations pour la même instance, vous devriez, idéalement, toujours sélectionner la dernière génération. La dernière génération d'instance est généralement livrée avec le dernier matériel. Cela signifie généralement un coût inférieur par unité de performance par rapport aux générations plus anciennes.

L'instance i3en.6xlarge dans l'exemple ci-dessus est une instance de troisième génération.

### Fonctionnalités Spéciales

Ce sont des lettres optionnelles qui viennent après la génération de l'instance. Chaque lettre désigne une fonctionnalité spéciale de l'instance.

Dans ce cas, le « **e** » signifie **capacité supplémentaire** (peut être de la RAM ou du stockage) et le « **n** » signifie que l'instance est **optimisée pour le réseau**. Cela signifie qu'elle a une bande passante réseau élevée, ce qui signifie que l'instance peut gérer un taux de transfert de données élevé, généralement mesuré en Gb par seconde.

D'autres caractères de fonctionnalités spéciales et leurs capacités sont les suivants :

* **a** – Processeurs AMD

* **g** – Processeurs AWS Graviton

* **i** – Processeurs Intel

* **d** – Volumes de stockage d'instance

* **b** – Optimisation du stockage par blocs

* **z** – Haute fréquence

Ces fonctionnalités supplémentaires ne sont pas gratuites, donc ne sélectionnez une instance avec des fonctionnalités supplémentaires que si vous en avez besoin.

### Taille de l'Instance

La taille apparaît après le point. Elle se compose de deux parties : un nombre et des lettres indiquant la taille. Les options de taille vont de nano à xlarge (extra large).

Le nombre n'apparaît qu'avec les instances xlarge. Il indique combien de fois l'instance est plus grande qu'une xlarge. Ainsi, une 2xlarge est deux fois plus grande qu'une xlarge et une 6xlarge est six fois plus grande qu'une xlarge.

Mais, que signifie vraiment deux ou six fois plus grande ?

Pour le même type d'instance, le nombre après le point agit comme un multiplicateur pour le calcul (nombre de vCPUs), la mémoire (quantité de RAM) et la taille du stockage (pas tout le temps – certaines instances utilisent des volumes EBS où le stockage peut être mis à l'échelle indépendamment de l'instance. Les instances optimisées pour le stockage, en revanche, utilisent un stockage d'instance physiquement attaché qui est mis à l'échelle en fonction de la taille de l'instance.).

Une instance i3en.xlarge a 4 vCPUs, 32 GiB de mémoire et 2500 GB de capacité de stockage. Une instance i3en.**6**xlarge est six fois plus grande puisqu'elle a **six fois** le nombre de vCPUs (24), six fois la mémoire (192 GiB) et six fois la capacité de stockage (15 000 GB).

## Mettre le Tout Ensemble – Comment Sélectionner Votre Instance

Ainsi, disons que vous devez sélectionner une instance EC2 pour votre serveur web, ou votre base de données NoSQL – quelles sont les étapes logiques à suivre ?

### Étape 1 : Sélectionner le type d'instance

Choisir entre usage général, optimisées pour le calcul, calcul accéléré, optimisées pour le stockage et optimisées pour la mémoire est la première et la plus importante décision. Toutes les décisions suivantes seront déterminées par celle-ci.

Ici, la décision que vous prenez est principalement une question de coût – vous essayez d'**optimiser pour le coût en dollars le plus bas par unité de la métrique la plus importante pour votre charge de travail**.

Si votre charge de travail est générique, comme un serveur web, choisissez une instance d'usage général. Si votre charge de travail est intensive en calcul, optez pour un type d'instance optimisée pour le calcul. La même logique s'applique si votre charge de travail est intensive en mémoire ou en stockage.

### Étape 2 : Sélectionner la famille d'instance

Un bon modèle mental pour choisir la bonne famille d'instance est de consulter la documentation technique de l'application que vous prévoyez d'exécuter sur cette instance et d'utiliser leur recommandation.

Par exemple, Elasticsearch (un moteur de base de données de recherche en texte intégral) recommande la famille d'instances « i » – spécifiquement la « i3 ». Rappelez-vous que le nombre après la famille d'instance est simplement la génération de l'instance, et que la plus récente est généralement la meilleure.

Lorsque qu'une nouvelle génération de la famille « i » arrive, Elasticsearch recommandera probablement l'instance « i4 ». Vous pouvez raisonner par analogie lors de la sélection de la famille d'instance. Regardez ce que l'application recommande, car c'est un excellent moyen de réduire les erreurs d'omission ou de commission.

L'entreprise derrière l'application aura beaucoup d'expérience dans le test de différentes familles et aura fait l'expérimentation en votre nom. Pas besoin de réinventer la roue (sauf, bien sûr, si votre charge de travail est vraiment niche et qu'aucune meilleure pratique n'existe).

### Étape 3 : Sélectionner une instance avec des fonctionnalités spéciales

Faites cela uniquement si absolument nécessaire. Vous paierez un supplément pour cela.

### Étape 4 : Sélectionner une taille d'instance

Cela est purement spécifique à votre charge de travail et est généralement un processus itératif. Vous pouvez exécuter quelques tests tout en surveillant l'utilisation du CPU et de la mémoire pour voir si la taille que vous avez sélectionnée est appropriée.

Vous essayez généralement d'avoir une certaine marge de sécurité, donc si votre charge de travail consomme, en moyenne, 90 % de la mémoire et du CPU, vous devrez peut-être choisir une instance plus grande. Une utilisation de 90 % ne laisse pas beaucoup de marge pour les erreurs d'estimation que vous avez pu faire pendant les tests.

Décider de la quantité de marge dont vous avez besoin est plus un art qu'une ingénierie, donc il n'y a pas de chiffres qualitatifs précis sur cela. Mais à titre indicatif, une utilisation dans la plage des 90 % est mauvaise, 80 % est acceptable, et 70 % et moins est bon.

Vous devez prévoir une certaine marge pour éviter tout problème de performance pendant les pics de demande.

## Conclusion

Lorsque vous sélectionnez un type d'instance, vous sélectionnez effectivement le prix le plus bas par unité de la métrique la plus importante pour votre charge de travail. Cela constitue une base importante dans tout projet sur lequel vous travaillez, car cela garantit que vous payez le montant en dollars le plus bas par unité de performance.

La sélection de la taille de l'instance est la partie la plus difficile du puzzle et est susceptible d'être un processus itératif où vous commencez petit, testez, puis augmentez l'échelle si nécessaire.