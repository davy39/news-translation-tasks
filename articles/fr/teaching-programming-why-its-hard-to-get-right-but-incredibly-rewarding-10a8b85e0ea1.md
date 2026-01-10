---
title: 'Enseigner la programmation : pourquoi c''est difficile à bien faire, mais
  incroyablement gratifiant'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-08T17:58:03.000Z'
originalURL: https://freecodecamp.org/news/teaching-programming-why-its-hard-to-get-right-but-incredibly-rewarding-10a8b85e0ea1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UvcfCAdCIgssSYCSSykrMw.jpeg
tags:
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Enseigner la programmation : pourquoi c''est difficile à bien faire, mais
  incroyablement gratifiant'
seo_desc: 'By Kristian Freeman

  Over the past year, I’ve had the opportunity to teach programming in a couple of
  different contexts. Towards the beginning of this year, I ran a few sessions of
  a small meetup in Los Angeles, and spoke at a larger, more organized ...'
---

Par Kristian Freeman

Au cours de l'année dernière, j'ai eu l'opportunité d'enseigner la programmation dans plusieurs contextes différents. Au début de cette année, j'ai animé quelques sessions d'un petit meetup à Los Angeles et j'ai parlé lors d'un [meetup plus grand et mieux organisé](https://www.meetup.com/socal-react/events/240559282/).

Dans la seconde moitié de l'année, à travers ma société de formation [Bytesized,](https://bytesized.xyz/) j'ai enseigné quelques cours complets de deux et quatre jours, spécifiquement sur React et JavaScript. Ces expériences ont été incroyablement enrichissantes, et la raison principale est que _voir les gens apprendre est vraiment excitant_.

Si vous êtes intéressé par l'enseignement de la programmation, que ce soit en tant qu'enseignant à temps plein, ou lors de meetups et de groupes d'utilisateurs, je souhaite partager certaines de mes stratégies que j'ai utilisées pour enseigner la programmation. La plupart de ces stratégies sont évidentes. Selon mon expérience, elles sont souvent négligées lorsque les gens commettent des erreurs faciles pendant leur instruction.

#### Équilibrer le temps de cours et de codage

Ma règle générale pour les instructions de programmation plus longues est de diviser le temps que vous passez à faire des cours et le temps que les étudiants passent à écrire du code, à 50/50. C'est-à-dire, si vous parlez pendant une demi-heure, en introduisant de nouveaux concepts avec des diapositives ou des démonstrations en direct, la demi-heure suivante devrait être dédiée à l'écriture de code par les étudiants.

Si vous avez déjà été étudiant dans un cours de programmation, vous savez que ce ratio est super important et souvent ignoré. J'ai suivi de nombreux cours de programmation de huit heures. L'enseignant passe la plupart du temps à chercher dans ses diapositives et à montrer du code, mais rarement à vous donner l'occasion d'écrire du code.

Notez que ce ratio, et cet accent sur les exercices, est différent de _suivre le cours_. Certains étudiants motivés le feront, mais la plupart des étudiants n'écriront pas de code à moins que vous ne leur donniez explicitement le temps de le faire. C'est une distinction importante. De nombreux étudiants (et enseignants) semblent ignorer que l'engagement se produit lorsque les étudiants ont le "contrôle" sur leur situation dans le cours. Même l'étudiant le plus motivé s'ennuiera dans un cours où il n'a pas réellement l'occasion de construire des choses.

Ce ratio est une suggestion. Si quoi que ce soit, je trouve que 50/50 est rare : à mesure qu'un cours s'allonge, je trouve que c'est une excellente idée de le faire passer à 66/33, en faveur des exercices. Lors d'un récent engagement de formation, j'ai travaillé avec un certain nombre de développeurs seniors. Ils préféraient être pratiques, en écrivant eux-mêmes du code.

Dans cette situation, ils ne posaient pas de questions pendant le cours, mais avaient souvent des questions de suivi lorsqu'ils travaillaient sur les exercices. Dans cette session particulière, le ratio était plus déséquilibré que 50/50 ou 66/33 : il était probablement plus proche de 80/20 !

#### Guider les étudiants vers la solution, mais les laisser la découvrir eux-mêmes

Les exercices peuvent être délicats à rédiger. Ils doivent faire référence au contenu que vous avez enseigné. Mais aussi être "compliqués" suffisamment pour que les étudiants doivent réfléchir au sujet et résoudre en conséquence.

Ma règle générale pour rédiger des exercices est d'essayer de pousser les étudiants à environ 10 % en dehors de leur zone de confort. Bien sûr, cela est difficile à mesurer. La manière dont cela fonctionne habituellement est que je vais faire référence à un exemple de code ou à une idée du cours, et la modifier légèrement (ou l'approfondir). Les étudiants doivent la comprendre _au-delà_ du cours ou de l'exemple fourni.

Par exemple, dans une formation React, je vais démontrer le passage de props à un composant React, en montrant une valeur de chaîne simple et une valeur booléenne :

```
<MyComponent myStringProp="Bonjour !" /><MyComponent myBoolProp={true} />
```

Dans l'exercice, je vais ensuite demander aux étudiants de passer d'autres types en tant que props, tels que des nombres, des tableaux, des booléens et des objets. Puisqu'ils ont vu deux exemples de types _simples_ passés dans un composant, ils peuvent extrapoler comment passer, par exemple, un nombre. D'abord, ils pourraient essayer de passer le nombre dans un format similaire à la chaîne :

```
<MyComponent myNumValue=3 />
```

Ce code retournera une erreur, car le nombre est "inattendu".

À ce stade, l'étudiant est dans une situation où il doit extrapoler ce qu'il doit faire, en fonction des informations données. La solution ne lui est pas donnée — au lieu de cela, les outils pour **trouver** la solution sont ce qui a été fourni. C'est là que l'apprentissage se produit, et je trouve que cela se traduit souvent par un changement littéral d'expression sur le visage des étudiants. Au lieu d'être ennuyés, ils sont profondément concentrés sur le problème qui leur est donné.

Étant donné le deuxième exemple, de nombreux étudiants tenteront alors d'envelopper le nombre dans des accolades.

Ainsi, en écrivant la solution correcte :

```
<MyComponent myNumValue={3} />
```

#### Offrir des opportunités pour des "crédits supplémentaires"

Un exercice bien rédigé indique clairement quand un étudiant l'a terminé. Dans ma formation, je fournis une suite de tests pour chaque exercice. Les étudiants ouvrent le répertoire de l'exercice et exécutent `make` pour confirmer qu'ils ont réussi les exercices. Ce flux fonctionne bien pour les étudiants, car il est cohérent : ils ont une indication claire de ce à quoi ressemble le succès dans l'exercice.

Tout aussi importantes sont les exercices où les étudiants peuvent aller au-delà des exigences énoncées et explorer des choses qui les intéressent. Récemmment, un étudiant a terminé un exercice avec des composants React et était intéressé à ajouter une personnalisation supplémentaire au composant, comme passer une police et une couleur de texte.

Cette idée, à laquelle je n'avais pas pensé dans le cadre de l'exercice original, était un moyen parfait d'explorer davantage les composants React. J'ai depuis ajouté cela dans la section des crédits supplémentaires de cette tâche.

Pour chaque exercice, réfléchissez à une ou deux idées de crédits supplémentaires que les étudiants peuvent faire pour démontrer leur compréhension du contenu.

Je suis toujours surpris que de nombreux étudiants _adorent_ la partie des crédits supplémentaires des devoirs. De nombreux ingénieurs logiciels sont auto-motivés et aiment avoir ce défi supplémentaire.

#### Créer un exercice "à partir de zéro"

Selon mon expérience d'enseignement de React, je trouve que je dois souvent revenir en arrière et enseigner les bases de JavaScript. Parfois même HTML. Cela signifie que les exercices dans un engagement de formation couvrent souvent un large éventail de sujets. À cause de cela, j'ai récemment introduit un exercice "à partir de zéro". Cela a été un énorme succès. Je lui attribue le fait que mon dernier engagement de formation ait été un succès retentissant.

Prenons un cours de formation React. Nous couvrirons les fondamentaux de JavaScript, l'écriture de composants React en JSX. Vers la fin du cours, la récupération de données depuis Internet.

Chacun de ces exercices est différent. Au troisième ou quatrième jour, lorsque nous sommes plongés dans le code React, les étudiants oublient souvent certaines des choses que nous avons couvertes les premiers jours. Par exemple, utiliser `.map` ou `.find`, ou gérer les erreurs de portée.

L'exercice "à partir de zéro" est conçu pour reprendre une partie de chaque exercice. Donner aux étudiants une période prolongée de temps vers la fin du dernier jour pour _écrire du code_.

Pour de nombreux développeurs, c'est le moment "déclic". C'est là que toutes les pièces que nous avons couvertes, certaines semblant inutiles ou ennuyeuses, se rassemblent.

Dans mon cours React, l'exercice "à partir de zéro" est un blog : une application React complète. D'abord, nous récupérons des données via JSON (en utilisant fetch), les analysons et les affichons à travers une arborescence de composants profondément imbriquée. Cela couvre toutes les bases de ce sur quoi nous avons travaillé dans la formation : non seulement les fondamentaux de JavaScript, mais aussi le travail dans une application React dans un exemple concret.

Mon moment préféré de mon temps de formation des étudiants a été de voir à quel point cet exercice a été réussi. Alors que nous terminions le dernier jour d'un engagement de formation, j'ai tenté de donner ma dernière conférence de "clôture", couvrant quelques ressources supplémentaires pour apprendre React, et des liens pour me contacter si les étudiants avaient d'autres questions. Au lieu de donner cette conférence, les étudiants ont demandé plus de temps pour l'exercice : ils voulaient simplement continuer à construire.

C'était génial !

#### Rester en contact

J'essaie de créer des opportunités pour que les étudiants posent des questions pendant les sessions de formation. Je m'arrête pour les questions à la fin de chaque cours. Je fais une pause pendant les exemples de code particulièrement compliqués, pour demander si les gens ont besoin d'explications différentes sur un sujet.

Pour certains étudiants, ils ne sont pas à l'aise de parler en classe. Ce n'est pas grave ! Je vous encourage à ne pas forcer les gens à parler en classe, s'ils ne veulent pas.

Au lieu de cela, assurez-vous de donner à vos étudiants la possibilité de vous contacter après la formation. Que ce soit par e-mail ou via un forum en ligne. J'ai eu un certain nombre de grandes conversations avec des étudiants, que ce soit sous forme de feedback (assurez-vous de collecter des feedbacks !) ou de questions supplémentaires sur ce qu'il faut étudier ensuite ou comment. Ces conversations ont conduit à des améliorations concrètes dans mes supports de formation et mes présentations.

Partagez toujours vos diapositives, et si possible, votre code. Mes exercices de formation sont disponibles pour tous les étudiants, non seulement pendant le cours, mais chaque fois qu'ils en ont besoin à l'avenir.

Puisqu'il s'agit d'un [dépôt open-source,](https://gitlab.com/bytesizedxyz/react-training) ils peuvent également pratiquer de nouveaux exercices qui ont été développés après leur session de formation, ou essayer des exercices pour lesquels nous n'avons pas eu le temps. Dans le cas de ma formation React, en particulier, le projet lui-même est open-source, donc il serait étrange de fermer les supports. Je vous lance le défi de faire quelque chose de similaire, si vos engagements de formation sont basés sur des projets open-source.

Il y a eu peu d'expériences professionnelles qui ont été aussi excitantes et gratifiantes pour moi que d'enseigner aux gens comment coder. Si vous pensez que vous êtes un communicateur efficace et que vous pourriez être un bon enseignant, trouvez un meetup local et proposez une conférence de vingt minutes ! Les organisateurs de meetups recherchent souvent des intervenants, et quelque chose d'aussi simple que _"Leçons apprises en construisant mon récent projet <x>"_ peut faire une conférence vraiment intéressante et mémorable.

Si la formation en programmation vous intéresse, vous ou votre équipe, consultez [Bytesized,](https://bytesized.xyz/) ma société de formation. Bytesized propose des formations dans plusieurs langages et frameworks de programmation, avec un accent sur le développement web — React, Redux et JavaScript. Vous pouvez également me suivre sur [Twitter](https://twitter.com/imkmf) !