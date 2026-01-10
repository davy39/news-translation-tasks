---
title: Ce que chaque développeur doit savoir sur le traitement du langage naturel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T08:26:00.000Z'
originalURL: https://freecodecamp.org/news/natural-language-processing-basics-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/patrick-tomasso-Oaqk7qqNh_c-unsplash.jpg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
seo_title: Ce que chaque développeur doit savoir sur le traitement du langage naturel
seo_desc: 'By Tal Perry

  Developers have always had to work with text. So why does it suddenly feel like
  everyone is talking about NLP, GPT, and BERT all day?

  In this article I''d like to give you a high level overview of what''s been going
  on in the world of Natu...'
---

Par Tal Perry

Les développeurs ont toujours dû travailler avec du texte. Alors pourquoi a-t-on soudainement l'impression que tout le monde parle de NLP, GPT et BERT toute la journée ?

Dans cet article, je souhaite vous donner un aperçu de haut niveau de ce qui se passe dans le monde du traitement du langage naturel et de l'apprentissage automatique, pourquoi les gens sont si enthousiastes, et ce que cela signifie pour nous en tant que développeurs.

## Un peu de contexte

Au fait, je m'appelle Tal. J'ai commencé comme cuisinier avant de devenir développeur backend et j'ai somehow fini par faire du traitement du langage naturel (NLP) pour des startups et des banques. Aujourd'hui, je dirige ma propre entreprise de outils NLP.

Ce que je vais partager ci-dessous est basé sur ce que j'ai appris en tant que développeur, scientifique des données, et aujourd'hui en tant que PDG travaillant avec d'autres entreprises qui font du NLP.

Pour comprendre le NLP aujourd'hui, vous devez comprendre ce qu'il était avant. Et la ligne de démarcation entre maintenant et avant est l'apprentissage profond. Nous commencerons donc par ce qui est venu avant l'apprentissage profond, puis nous parlerons de ce que l'apprentissage profond a changé.

Dans la phase d'apprentissage profond du NLP, il y a eu un autre grand changement que nous appellerons la modélisation du langage.

Néanmoins, cela n'a aucun sens sans une vue d'ensemble de ce qu'est réellement l'apprentissage profond. Nous expliquerons donc les bases de l'apprentissage profond très rapidement, puis nous passerons à l'époque actuelle, ce qui s'est passé et ce qui est sur le point de se produire.

## Ce qui est difficile avec le langage

Voici quelque chose à réfléchir : Qu'est-ce qui a quatre lettres, n'a jamais cinq lettres, mais a parfois 9 lettres.

Ce n'est pas une question, c'est une déclaration.

Le mot "What" a quatre lettres, w-h-a-t. La plupart des gens trébuchent là-dessus, parce que :

1. Lorsque nous voyons une phrase commençant par le mot "What", nous nous attendons à ce que ce soit une question

2. Le point à la fin de la phrase a changé le sens de la plupart des mots

3. Nous n'avons pas vu le point jusqu'à la fin.

L'une des parties les plus difficiles du langage est que lorsque nous, les humains, l'utilisons, nous faisons beaucoup d'inférences de manière miraculeuse. C'est plus difficile pour les ordinateurs. Laissez-moi expliquer.

### Inférence

Peter Norvig, directeur de la recherche chez Google, a écrit sa thèse de doctorat en 1987. Elle s'intitulait [A Unified Theory of Inference for Text Understanding](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1987/CSD-87-339.pdf). Sa thèse entière est essentiellement sur ce qu'est l'inférence et pourquoi c'est difficile et comment l'aborder.

Il ouvre la thèse avec une grande observation :

> Les gens sont très bons pour interpréter les textes et faire des inférences. Ils ne remarquent généralement **pas lorsque le texte est sous-spécifié** et qu'ils doivent faire des inférences pour résoudre les ambiguïtés, ou pour obtenir une compréhension plus complète du texte.

En tant qu'êtres humains, nous sommes habitués à faire ces inférences, comme inférer (incorrectement) que le *What* dans ma phrase d'exemple indiquait une question.

Les humains sont vraiment bons pour faire des inférences. Les ordinateurs, cependant, sont terribles à cela. Laissez-moi vous donner un autre exemple de la thèse de Norvig.

### Chang le pêcheur

> Dans un pauvre village de pêcheurs construit sur une île non loin de la côte de la Chine, un jeune garçon nommé Chang Lee vivait avec sa mère veuve. Chaque jour, le petit Chang partait courageusement avec son filet, espérant attraper quelques poissons de la mer...

Pour vous, il est évident qu'il y a une mer qui entoure l'île, forme la côte de la Chine, et que les villageois utilisent pour pêcher.

Mais aucune de ces informations n'est indiquée dans le texte. Allez-y, relisez-le. Et une fois que vous êtes satisfait que ce n'est pas là, réfléchissez à ceci : Comment vous attendez-vous à ce qu'un ordinateur comprenne ces faits à partir du texte ? En un mot, c'est ce qui est difficile avec le NLP.

## Ce que l'apprentissage profond a changé

Lorsque je suis devenu développeur, au milieu des années 2000, "Machine Learning" et "Big Data" sont devenus des mots à la mode. Et les systèmes que nous, développeurs, connaissons et aimons, comme Elasticsearch et Google, ont vu le jour.

Pensez à l'interface de recherche de Google. Tout ce qu'elle a à faire est de prendre l'entrée de texte de l'utilisateur et d'inférer ce que l'utilisateur voulait. Plus Google fait bien cela, plus ils gagnent d'argent.

Il y a beaucoup de choses difficiles dans le travail de Google, mais je veux me concentrer sur deux d'entre elles.

La première est que, pour un ordinateur, un "mot" n'est qu'un symbole et n'a aucune signification.

La seconde est qu'un mot ne suffit pas - parfois l'intention de l'utilisateur est exprimée dans une phrase entière, et traiter cela de manière tractable est difficile.

Par exemple, recherchons sur Google la mère de Mère Teresa

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-139.png align="left")

Google a dû inférer que "Mother Teresa" est une seule entité, est une personne particulière, et qu'elle a une "mother", qui est une personne liée à elle. Cela signifie qu'ils devaient traiter la requête de l'utilisateur dans son ensemble et déterminer le sens correct de chaque mot et phrase.

Comment feriez-vous cela ? Ce n'était pas impossible avant l'apprentissage profond, mais c'était quelque chose que seuls les docteurs pouvaient faire. Mais aujourd'hui, c'est assez facile, alors voyons ce qui a changé.

### Signification

En 2013, l'algorithme Word2Vec a été publié par une équipe de Google. Le principe était essentiellement :

* Nous avons besoin d'un moyen d'associer la signification des mots

* Les ordinateurs sont nuls pour traiter des symboles comme les mots

* Mais ils sont excellents pour traiter des nombres

* Peut-on représenter la signification d'un mot avec un ensemble de nombres ?

Word2Vec est un algorithme qui détermine les significations des mots et les représente à un ordinateur comme un ensemble de nombres.

Une manière plus formelle de dire "un ensemble de nombres" est un *vecteur* (Le vec dans Word2**Vec**). Lorsque vous pensez à "un ensemble de nombres" comme à des "vecteurs", vous pouvez utiliser toutes sortes de maths kung-fu pour faire faire aux vecteurs ce que vous voulez.

La grande percée technique avec Word2Vec était qu'il donnait un "kata de kung-fu" spécifique, c'est-à-dire un algorithme, pour capturer les significations des mots de manière efficace et utilisable.

L'autre percée, non moins significative, était que les démonstrations étaient époustouflantes à l'époque.

Par exemple, vous pouviez additionner et soustraire ces vecteurs, car ils étaient des choses mathématiques, et le résultat aurait un sens intuitif. Comme "King - Man + Woman = Queen"

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-144.png align="left")

*Mots représentés comme des vecteurs. Ces démonstrations ont rendu Word2Vec convaincant pour un large public*

### APIs

Word2Vec a ouvert la voie pour travailler avec la signification des mots individuels, mais l'apprentissage profond a apporté un autre changement dans la manière dont nous travaillons avec le langage. L'apprentissage profond nous a donné des APIs pratiques pour travailler avec des séquences arbitrairement longues comme des phrases, des phrases et des paragraphes.

Avant l'apprentissage profond, lorsque les développeurs voulaient analyser des mots dans leur contexte, ils écrivaient des fonctions pour analyser le mot précédent, le mot avant celui-ci, le mot qui suivait, et ainsi de suite.

Ils pouvaient écrire plusieurs fonctions pour chaque mot, comme "Le mot suivant commence-t-il par une majuscule" et "Le mot qui est venu deux mots avant celui-ci est-il un verbe".

Non seulement ce processus était laborieux et difficile à maintenir, mais il avait des implications de performance surprenantes.

Chris Manning a une vidéo (que je ne peux pas trouver) où il déclare que la principale barrière de performance pour un analyseur pré-apprentissage profond était le chargement de toutes les fonctionnalités (les résultats de ces fonctions) dans le cache CPU. Il y en avait simplement trop pour que vous n'ayez jamais un cache hit.

Alors, qu'est-ce que l'apprentissage profond a changé ? Il a supprimé le besoin de décrire et de programmer manuellement les interactions entre les mots dans une séquence.

Au lieu de cela, nous avons maintenant des APIs qui prennent une séquence de mots (ou de vecteurs) en entrée et retournent une séquence qui a été traitée de la manière dont nous le voulons.

Les jours où nous devions écrire 1000 fonctions et stocker un million de colonnes pour chaque mot juste pour analyser du texte sont révolus. Aujourd'hui, une séquence entre et une séquence sort avec ce que nous voulions.

Mais comment cela se passe-t-il ? Nous aurons besoin de quelques paragraphes sur l'apprentissage profond pour comprendre.

## L'apprentissage profond en 3 minutes

Pour faciliter l'apprentissage de quelque chose sur les données par un ordinateur, nous devons représenter ces données de manière à ce qu'elles soient faciles à analyser pour l'ordinateur.

Word2Vec était une grande étape dans cette direction, car il nous permettait de passer des représentations symboliques d'un mot à une représentation vectorielle, un ensemble de nombres sur lesquels l'ordinateur peut faire des maths.

Un modèle d'apprentissage profond est simplement un pipeline d'opérations mathématiques que nous effectuons sur des vecteurs d'entrée. La partie cool est que nous allons de l'avant et de l'arrière dans le pipeline.

Pour faire apprendre un modèle d'apprentissage profond, nous mettons notre entrée au début du pipeline et nous l'exécutons jusqu'à la fin. Le modèle aura fait des maths et calculé un résultat.

Ensuite, nous revenons en arrière, nous comparons le résultat du modèle à ce qu'était la vérité, et nous calculons un score de la manière dont le modèle avait tort (appelé la perte). La partie apprentissage de l'apprentissage profond consiste à utiliser des algorithmes d'optimisation pour rendre la perte aussi petite que possible.

Alors, qu'est-ce qui change dans notre pipeline pour optimiser le score ? Imaginez que nous avions une entrée X et que notre pipeline était "Multiplier X par *a* puis ajouter *b*.* À chaque étape du processus d'optimisation, nous modifierions *a* et *b* pour réduire la perte et ainsi obtenir une meilleure prédiction.

Le problème est que nous aurions des milliers, voire des millions de \_a'\_s et *b's*, et nous pouvons faire des choses plus sophistiquées que simplement multiplier et ajouter. Nous appelons ces *a's* et *b's* des paramètres et plus nous en avons, plus notre modèle est "expressif", et plus il peut apprendre.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-145.png align="left")

*Un "pipeline" d'apprentissage profond montrant comment une séquence est traitée de gauche à droite et de droite à gauche*

Maintenant, si vous vous demandez comment trouver le meilleur pipeline ou modèle à utiliser, j'ai une bonne nouvelle pour vous. L'apprentissage automatique est un domaine très ouvert, et la plupart des modèles de pointe sont disponibles en open source et peuvent être exécutés en quelques lignes de code.

Cela semble incroyable, n'est-ce pas ? Alors, quel est le piège ?

## Les données étiquetées sont le coût caché de l'apprentissage profond

Les modèles d'apprentissage profond apprennent en regardant des exemples avec une étiquette indiquant ce que nous voulons qu'ils prédisent.

Si nous voulons créer un modèle qui prédit le sentiment d'un avis sur un produit, nous devrions entraîner le modèle en lui montrant un avis et le score de sentiment qu'un humain lui a donné.

Le piège est que les modèles d'apprentissage profond ont besoin de beaucoup de données étiquetées, et ces données doivent être bonnes. Plus un modèle est expressif et plus il a de paramètres, plus il aura besoin de données étiquetées pour l'entraînement.

C'est un problème si important que j'ai personnellement fait la transition de scientifique des données à fondateur d'une entreprise d'[outils d'annotation de texte](https://www.lighttag.io/).

Particulièrement en NLP (par opposition à la vision), les personnes qui font les annotations doivent être des experts du domaine, et elles sont chères et ne considèrent pas l'annotation comme leur activité préférée.

Nous leur donnons des outils pour étiqueter leurs données en interne et efficacement. Bien que nous servions une niche, le marché des annotations externalisées est encore plus grand avec une dépense annuelle estimée à des milliards.

Cela veut dire que les données étiquetées sont un goulot d'étranglement, un centre de coût, et souvent une barrière à l'entrée pour l'apprentissage profond. Réduire cette barrière et diminuer les coûts humains de l'apprentissage profond pour le NLP est ce qui s'est passé récemment et ce dont nous parlerons ensuite.

## Le NLP de 2018 à 2020

Je suis en train d'apprendre à mon fils à aller sur le pot. Nous en sommes à un point où il peut nous signaler quand il a fait un numéro un et le plan est que, une fois qu'il maîtrisera le numéro un, il pourra transférer cette maîtrise au numéro deux. Je pense que ce sera plus facile et plus propre de l'apprendre à aller sur le pot dans cet ordre.

Les grandes tendances des deux dernières années en NLP sont comme l'apprentissage de la propreté de mon fils, nous pouvons entraîner le modèle sur une tâche plus simple et transférer cette connaissance à une tâche plus avancée.

Mais comme je l'ai dit avant, obtenir des données étiquetées est coûteux, donc nous ne voudrions pas entraîner un modèle sur une tâche qui ne nous intéresse pas, car nous devrions encore payer pour l'annotation.

Et si je vous disais qu'il existe des tâches sur lesquelles nous pouvons pré-entraîner notre modèle, où nous pouvons obtenir des données étiquetées illimitées gratuitement ?

### Modélisation du langage

Vous savez comment certaines personnes sont si proches qu'elles peuvent compléter les phrases de l'autre ? Elles peuvent le faire parce qu'elles connaissent bien cette personne et la langue.

Si bien, en fait, qu'elles ont un modèle mental des pensées et du style de parole de l'autre personne dans leur propre tête.

Si nous avions un modèle d'apprentissage profond pour le NLP qui savait déjà comment les gens parlent et écrivent, et qui pouvait compléter leurs phrases pour eux, il aurait beaucoup plus de facilité à apprendre une tâche linguistique spécifique comme déterminer le sentiment d'un avis.

Un modèle d'apprentissage profond qui commencerait avec une compréhension de la manière dont les gens parlent serait capable d'utiliser cette connaissance lorsqu'il apprend une nouvelle tâche. Tout comme mon fils sera meilleur pour le numéro deux après avoir maîtrisé le numéro un.

Comment faire pour qu'un modèle apprenne comment les gens parlent et écrivent ? Facile, nous prenons un texte, et nous demandons au modèle de prédire quel mot vient ensuite.

Cette tâche s'appelle "modélisation du langage", et la faire correctement présuppose de nombreuses capacités auxquelles vous n'auriez pas pensé, comme comprendre la grammaire, compter et suivre la relation entre les mots qui sont éloignés.

Un article de blog qui m'a vraiment excité sur le NLP était "The Unreasonable Effectiveness of Recurrent Neural Networks" qui a été écrit en 2015 par Andrej Karpathy (maintenant responsable de l'IA chez Tesla).

Dans l'article, Karpathy a construit un modèle de langage du code source de Linux. Il a pris tout le code du github de Linux, a fait en sorte que le modèle regarde quelques mots, puis lui a fait prédire le suivant.

Ma mâchoire est tombée quand il a pris ce modèle et l'a utilisé dans une boucle pour générer un nouveau texte. Il a fait en sorte que le modèle fasse une prédiction de la lettre suivante, puis a réinjecté cela dans le modèle encore et encore. Le modèle a produit du code qui ressemblait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-142.png align="left")

*Code généré par un modèle de langage en 2015. Remarquez l'indentation et l'utilisation des commentaires*

Bien que le code ci-dessus ne compile pas et ne fasse rien d'utile, il montre qu'un modèle de langage peut apprendre beaucoup sur la manière dont le langage est utilisé. Et ce n'est pas juste un gadget - certains des outils de complétion de code alimentés par l'IA que vous avez vus fonctionnent exactement comme cela.

### Modélisation du langage sur stéroïdes

Entre 2015 et aujourd'hui, le NLP a poussé l'idée de la modélisation du langage à son plein potentiel.

En 2018, un [article a été publié](https://arxiv.org/abs/1801.06146) qui montrait comment vous pouviez utiliser de manière cohérente un modèle de langage pré-entraîné pour améliorer considérablement les performances d'un modèle avec une quantité donnée de données étiquetées.

Peu de temps après, le monde du NLP a vu un déluge de nouveaux modèles pré-entraînés sortir, chacun surpassant le précédent. Vous avez peut-être entendu parler de modèles appelés BERT, XLNet, GPT 1, 2 et 3, et ainsi de suite.

Tous ces modèles suivaient le concept de base de la modélisation du langage, chacun avec quelques variantes techniques modifiées. Mais leur véritable signification venait de deux facteurs.

Premièrement, ils ont été entraînés sur des ensembles de données de plus en plus grands en tant que modèles de plus en plus grands. BERT, qui est sorti en 2018, a [coûté 6 800 $](https://syncedreview.com/2019/06/27/the-staggering-cost-of-training-sota-ai-models/#:~:text=Google%20BERT%20%E2%80%94%20estimated%20total%20training,11%20natural%20language%20processing%20tasks.) à entraîner, tandis que GPT3, qui n'a pas encore été publié publiquement, a coûté 12 millions de dollars à entraîner.

Deuxièmement, ces modèles pré-entraînés ont été publiés en tant que logiciels open source (GPT3, n'étant pas publié, est l'exception à la règle). La plupart de ces modèles pré-entraînés ont été publiés publiquement et enveloppés derrière des bibliothèques open source pratiques comme [Huggingface's transformers](https://huggingface.co/transformers/).

Pour les développeurs qui voulaient simplement utiliser le dernier état de l'art du NLP et obtenir des résultats sans étiqueter des tonnes de données, l'ouverture et la disponibilité de ces modèles ont changé la manière dont nous travaillons.

## Que va-t-il se passer ensuite ?

L'une des démonstrations de NLP les plus convaincantes qui circulent est GPT3 générant du code React à partir de texte libre.

%[https://www.youtube.com/watch?v=RyiWFbSdk78]

Cela signifie-t-il que certains d'entre nous vont bientôt être au chômage ? Quelles autres choses ces nouveaux modèles de NLP peuvent-ils automatiser et quelles nouvelles choses vont-elles apparaître grâce à eux ?

Je ne sais pas, et l'[histoire du NLP est de 60 ans](http://www.hutchinsweb.me.uk/Nutshell-2005.pdf) de prédictions erronées sur les percées et les limitations.

Lorsque je travaillais en tant que scientifique des données, je partageais souvent les résultats de mon travail avec nos parties prenantes commerciales non techniques - les personnes qui financaient mon salaire.

En tant que junior, je partageais souvent des résultats qui étaient techniquement époustouflants, mais mes parties prenantes ne s'en souciaient pas. Si elles voyaient une seule erreur stupide, elles concluaient que le modèle était stupide et inutilisable.

Nous appelions ces erreurs "Howlers" parce qu'elles faisaient hurler nos parties prenantes.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-143.png align="left")

*Google Translate donnant un Howler*

Pour les entreprises et les développeurs qui travaillent dans des entreprises, la valeur de ces nouveaux modèles de NLP est conditionnée par la capacité de l'entreprise à faire confiance au modèle pour faire ce qui est nécessaire.

C'est incroyable que GPT3 puisse créer du code React, mais lui feriez-vous confiance pour générer votre passerelle de paiement ou même générer un formulaire sécurisé pour la connexion ?

Je pense que les progrès du NLP l'ont rendu plus accessible aux personnes et aux entreprises, plus facile à utiliser et moins coûteux.

Mais le NLP n'est pas un déjeuner gratuit, ni une panacée. Vous devrez toujours travailler dur pour formuler votre tâche, obtenir des [données étiquetées pour le NLP](https://www.lighttag.io/how-to-label-data/), et vérifier que votre modèle fait ce que vous vouliez qu'il fasse.

## Comment en savoir plus

Si vous êtes arrivé jusqu'ici, je suis flatté, et vous devez être vraiment curieux à propos du NLP et de l'apprentissage profond.

Même si cet article était entièrement consacré à l'apprentissage profond et au NLP, je pense que les méthodes qui sont venues avant valent la peine d'être connues. Souvent, elles sont plus faciles à utiliser que les méthodes plus modernes et font le travail.

Même lorsqu'elles ne le font pas, un peu comme mon fils qui est entraîné à la propreté, je pense qu'il est plus facile de commencer par le simple et d'aller de là. Je voudrais donc partager certaines de mes ressources préférées dans cet esprit.

* Les cinq premiers chapitres de Dan Jurafsky et [James Martin's Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) sont des introductions fantastiques aux méthodes classiques.

* [Scikit-Learn's Text Analytics Tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) propose des exercices pratiques qui vous donneront une victoire rapide et une sensation pour la mécanique du NLP de base

* Je pense que la moitié des problèmes de NLP auxquels les développeurs sont confrontés avec le texte peuvent être résolus avec une expression régulière. Si vous n'êtes pas encore un ninja des regex, [RegexOne](https://regexone.com/) est un tutoriel incroyable.

* [Natural Language Processing with Deep Learning](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/) est rigoureux, complet et pratique et une manière incroyable de se familiariser avec les sujets avancés que nous avons discutés ici. C'est un gros investissement en temps mais cela en vaut vraiment la peine.

Merci d'avoir lu ! Vous pouvez consulter mon entreprise [LightTag](https://www.freecodecamp.org/news/p/3c94d59f-9169-42ef-b4fd-4d2feb9e51dd/lighttag.io) et me suivre sur [twitter](https://twitter.com/thetalperry).

## Liens

* [Thèse de Peter Norvig](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1987/CSD-87-339.pdf)

* L'article académique original [Word2Vec](https://arxiv.org/abs/1301.3781)

* [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146)

* [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

* [Huggingface Transformers](https://huggingface.co/transformers/)

* [The Staggering Cost of Training SOTA AI Models](https://syncedreview.com/2019/06/27/the-staggering-cost-of-training-sota-ai-models/#:~:text=Google%20BERT%20%E2%80%94%20estimated%20total%20training,11%20natural%20language%20processing%20tasks.)

* [The history of machine translation in a nutshell](http://www.hutchinsweb.me.uk/Nutshell-2005.pdf)

* [How to label data](https://www.lighttag.io/how-to-label-data/)