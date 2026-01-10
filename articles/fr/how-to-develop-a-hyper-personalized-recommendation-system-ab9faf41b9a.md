---
title: Comment développer un système de recommandation hyper-personnalisé
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T00:35:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-a-hyper-personalized-recommendation-system-ab9faf41b9a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*49XRS70Wt6F5-Wwo7JghNQ.jpeg
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Comment développer un système de recommandation hyper-personnalisé
seo_desc: 'By Mariya Yao

  Interview with Jack Chua of Expedia


  As part of our AI For Growth executive education series, we interview top executives
  at leading global companies who have successfully applied AI to grow their enterprises.
  Today, we sit down with Ja...'
---

Par Mariya Yao

#### Interview avec Jack Chua d'Expedia

![Image](https://cdn-media-1.freecodecamp.org/images/1*49XRS70Wt6F5-Wwo7JghNQ.jpeg)

Dans le cadre de notre série de formation exécutive [AI For Growth](https://www.topbots.com/ai-for-growth), nous interviewons des cadres supérieurs de grandes entreprises mondiales qui ont appliqué avec succès l'IA pour développer leurs entreprises. Aujourd'hui, nous nous entretenons avec [Jack Chua](https://www.linkedin.com/in/jackchua/), Directeur de la Science des Données chez Expedia.

Jack a construit des systèmes de trading automatisés pour des portefeuilles d'investissement de plusieurs millions de dollars, des systèmes de recommandation à l'échelle du téraoctet pour Amazon, et du marketing personnalisé pour une marque emblématique de boissons américaines. Auparavant, il dirigeait les applications industrielles de l'apprentissage automatique pour les clients mondiaux de Boston Consulting Group (BCG). Maintenant, il dirige l'équipe de science des données chez Expedia, où il applique son expertise approfondie en optimisation des produits et des prix.

Regardez l'épisode (ou lisez la transcription ci-dessous) pour apprendre :

1. Un bref historique sur l'évolution du système de recommandation
2. Comment choisir la bonne métrique KPI pour obtenir le bon mélange de recommandations
3. Les pièges à éviter lors de la construction de votre propre système de recommandation
4. Les sujets brulants dans l'application de l'IA au commerce de détail dans les trois à cinq prochaines années

**Marlene Jia :** Merci à tous de rejoindre notre série exécutive AI for Growth. Dans cette série d'interviews, nous apprenons des cadres de grandes entreprises mondiales qui ont appliqué avec succès l'IA à leur entreprise et à leur équipe.

Je m'appelle Marlene — vous pouvez m'appeler MJ — et aujourd'hui nous allons discuter avec Jack Chua, qui est le Directeur de la Science des Données chez Expedia. Il a également travaillé chez Amazon et BCG, donc je pense que nous aurons beaucoup de choses très intéressantes à apprendre de Jack aujourd'hui.

Jack, merci de nous rejoindre. Pour notre première question, nous aimerions en savoir plus sur vous, votre histoire, et comment vous vous êtes d'abord intéressé à l'IA.

**Jack Chua :** C'est un domaine dans lequel beaucoup d'entre nous atterrissent involontairement. Évidemment, c'est super intéressant et très impactant.

Mon parcours a été un peu inhabituel. J'ai commencé à étudier les mathématiques théoriques à l'Université de Chicago. Peut-être deux ou trois ans plus tard, je me suis dit : « Que vais-je faire avec ce diplôme ? »

J'ai regardé ce qui était tendance à l'époque. C'était en 2006. Beaucoup de mes pairs se dirigeaient vers la banque d'investissement, les fonds spéculatifs, ce genre de domaine. Je me suis dit : « Y a-t-il un moyen d'appliquer les mathématiques théoriques que j'ai apprises et de les fusionner avec le domaine sexy de la banque M&A ? », et je suis tombé dans le domaine de la finance quantitative.

J'ai commencé à lire voracement des livres sur la tarification des options, le trading de volatilité, des choses où vous pouvez essentiellement déterminer le processus stochastique sous-jacent de l'instrument et trader, étant donné ses dynamiques.

J'ai eu de la chance. Je suis entré avant que la crise financière des subprimes ne frappe, mais je dirais que c'est ainsi que j'ai commencé à combler le fossé entre les mathématiques théoriques et l'industrie.

Un autre moment est venu lorsque j'ai commencé à faire du trading haute fréquence. C'est un domaine où non seulement les éléments statistiques du trading sont nécessaires, mais aussi les éléments d'ingénierie, et j'ai réalisé le fossé entre connaître la théorie et être capable de l'implémenter, que ce soit en C++ ou en Python ou autre.

À l'époque, venant d'un milieu académique et professionnel très théorique, j'ai dû m'asseoir et apprendre à coder à partir de zéro. C'est ce qui m'a conduit à retourner à l'école supérieure à Georgia Tech en mathématiques appliquées, et c'est là que l'apprentissage automatique commençait vraiment à fleurir. J'ai commencé à suivre des cours d'analyse de données computationnelles, j'ai appris de certains des meilleurs professeurs du monde là-bas. Quelques années plus tard, nous en sommes là aujourd'hui.

**MJ :** Vous avez travaillé chez Amazon, et vous avez travaillé sur de nombreux projets dans le domaine des moteurs de recommandation. Comment avez-vous commencé là-bas et où cela vous a-t-il conduit ? Évidemment, vous êtes chez Expedia maintenant.

**JC :** Les moteurs de recommandation ne représentent qu'une petite partie de ce que je fais, mais c'est une partie très importante. La façon dont j'aime le décrire est « présenter le bon contenu au bon client au bon moment et dans le bon canal ». En plus du contenu, c'est tout un écosystème de la façon dont ce contenu est affiché et quel est le contexte.

Peut-être que cela anticipe d'autres choses que vous pourriez me demander, mais lorsque vous pensez à recommander quelque chose à quelqu'un, il y a une vraie raison commerciale pour laquelle vous pourriez vouloir faire cela, que ce soit pour encourager la vente croisée de produits, ou augmenter la fréquence de retour de quelqu'un sur votre site web parce que vous avez de grandes informations et ainsi de suite. Je pense que les moteurs de recommandation ont un excellent lien avec le KPI sous-jacent de ce que vous voulez stimuler.

Je pense que c'est ce qui a poussé Amazon à investir dans des scientifiques de données et des ingénieurs pour travailler sur les systèmes de recommandation, car le contexte sous-jacent de la raison pour laquelle quelqu'un achète quelque chose est si complexe. Cela pourrait être le fait que c'est saisonnier, peut-être qu'il y a une grosse réduction qui va avoir lieu, ou peut-être que c'est utilitaire, donc ils ont simplement pensé à quelque chose comme « Hé, je veux cette clé USB », donc ils vont sur notre site web et l'achètent.

Tous ces indices contextuels se combinent de manière que l'intelligence commerciale classique ou les règles commerciales ne peuvent pas capturer. C'est comme un problème d'IA pur, c'est quelque chose que l'utilisation de règles commerciales ou de règles humaines serait sous-optimale.

**MJ :** Avant de plonger dans tous les détails, j'aimerais que vous nous expliquiez exactement ce qu'est un moteur de recommandation, que vous nous guidiez à travers la manière dont vous iriez pour le construire, et quels sont les facteurs de considération, dont vous avez commencé à parler.

**JC :** En commençant par une définition purement axiomatique, un système de recommandation est un espace sur un canal de quelque sorte, qu'il s'agisse d'un email, d'un site web ou d'une application mobile, etc. Vous l'avez probablement vu sur Amazon, c'est un ruban qui contient plusieurs produits. Cela pourrait être un email qui contient plusieurs composants avec différents produits. Il y a des blocs de construction qui composent ces emails ou ces matériaux marketing, et c'est le travail de l'humain de déterminer ce qui devrait y aller.

Ce qui alimente le système est généralement un écosystème de flux de travail d'ingénierie qui se retrouve dans un simple email qui tombe dans votre boîte mail. Cela pourrait inclure des designers UX qui conçoivent l'apparence de l'email, qu'il ait l'air festif d'été ou peut-être quelque chose qui semble plus transactionnel.

Cela pourrait également être piloté par les données — ce que les sciences des données tendent à faire — cela s'appelle [un processus par lots](https://en.wikipedia.org/wiki/Batch_processing). Ils entraîneront les modèles en backend, et les modèles pourraient examiner les données de transactions historiques, ils pourraient examiner les données démographiques des clients, ils pourraient examiner les métadonnées des produits eux-mêmes, [comme] la différence entre une clé USB ou une télévision ou un jouet, prendre toutes ces informations et fournir aux marketeurs une liste d'IDs de clients pour tous les produits qu'ils pensent être pertinents.

Il y a aussi des [processus en temps réel](https://en.wikipedia.org/wiki/Real-time_computing) où littéralement, dès que quelqu'un clique sur l'email, cela envoie un signal aux scientifiques des données, [qui] l'incorporent immédiatement dans le prochain point de contact. Là où j'ai vu cela fait de la meilleure manière est probablement Amazon, ou en fait sur des sites de voyage comme Booking.com et Expedia.

Le commerce de détail est un domaine où les marges [sont] si serrées que pour vraiment innover dans ce domaine, vous devez penser à différents contextes et façons de comprendre ce que le client essaie d'acheter qui est hors du commun.

**MJ :** Vous avez parlé d'Amazon qui le fait le mieux. Évidemment, ils travaillent sur cela depuis longtemps. Qu'est-ce qui a déclenché le développement initial de cela ? Cela nous semble logique aujourd'hui, mais Amazon et Google étaient parmi les premières entreprises à le faire.

Pouvez-vous nous parler du processus de réflexion et de son évolution depuis que vous y étiez ?

**JC :** L'évolution pourrait être le point de départ le plus naturel. Toutes ces choses dans l'industrie sont généralement motivées par un objectif commercial. Les systèmes de recommandation pour le commerce de détail [centrent autour de cette idée de] « Hé, nous avons cette propriété dynamique qui n'est plus limitée aux panneaux ou aux panneaux d'affichage, et elle peut changer chaque seconde ou même chaque fois que quelqu'un atterrit sur le site web. » C'est maintenant une propriété dynamique, et pour capturer la dynamique de la propriété, il doit y avoir un moyen d'incorporer des données de manière transparente pour la mettre à jour.

Généralement, c'est ainsi que cela a commencé. Il y a beaucoup de choses en pratique qui pourraient être appelées systèmes de recommandation, mais nous pouvons nous concentrer sur les sites web pour l'instant.

Si vous atterrissez sur Amazon, vous avez plusieurs rubans, et un bon exemple de la manière dont différents KPI peuvent être ciblés est que chaque ruban a un objectif différent. L'un d'eux pourrait être « ce sont des choses que vous avez recherchées auparavant » ou « ce sont des choses que nous pensons que vous aimez » basées sur ce que vous avez acheté auparavant. Amazon est généralement assez bon pour expliquer ce qu'est le ruban, donc vous atterrissez dessus, et il y a un ancrage contextuel, donc vous voyez exactement à quoi sert la recommandation.

Historiquement, ces rubans ont été régis par des règles commerciales, donc une règle commerciale très simple pourrait être « montrer des choses que vous avez achetées auparavant pour que vous les rachetiez ». Étonnamment, cela a conduit à une grande augmentation lorsque Amazon a implémenté le module Buy-It-Again, donc c'est quelque chose qui ne nécessite aucune intelligence, il suffit de regarder ce que quelqu'un a acheté auparavant en insérant exactement la même chose. Cela peut fonctionner pour des choses que les clients achètent de manière irrégulière comme de la nourriture pour animaux ou divers produits de beauté, mais cela tend à ne pas fonctionner pour des choses comme la mode, où si vous achetez une chemise, vous n'allez probablement pas racheter exactement la même chemise.

C'est ce qui pousse l'évolution du système de recommandation, comme, quel est le produit [et] quel est le KPI pour le produit, qu'essaiez-vous d'inciter à acheter la même chose ou quelque chose de similaire ? Sur cette base, vous pouvez adapter votre algorithme.

Un algorithme simple basé sur des règles commerciales pour la vente croisée pourrait être [l'extraction de règles d'association](https://mapr.com/blog/association-rule-mining-not-your-typical-data-science-algorithm/) : regarder les choses qui tendent à être achetées dans le même panier.

Dans un contexte de magasin d'alimentation, il y a des produits de base et des choses qui sont souvent vendues ensemble parce qu'elles ont une marge plus élevée, peut-être du lait, du pain et des œufs. Quelqu'un va dans le magasin d'alimentation pour acheter du lait, peut-être que la chose naturelle à obtenir ensuite est du pain.

C'est quelque chose qui ne nécessite pas d'analytique prédictive. C'est vraiment juste l'extraction des données pour voir quels motifs émergent.

Une autre façon de le faire est basée sur quelque chose appelé [filtrage collaboratif](http://recommender-systems.org/collaborative-filtering/). Cela est [avant] les modèles prédictifs... en fait, je dirais que ce n'est pas dépassé parce que c'est plus récent que certains modèles prédictifs... mais c'est une approche relativement simple.

L'idée est de regarder les personnes qui vous sont similaires dans les transactions.

Marlene et moi sommes assez similaires sur Amazon, donc peut-être que nous avons tous les deux acheté exactement les mêmes choses sauf pour un article. Une chose naturelle à faire est de dire, « D'accord, parce que Marlene et Jack ont été presque exactement les mêmes jusqu'à cet article, recommandons simplement cet article à Marlene et Jack et voyons ce qui se passe. »

Ce n'est pas aussi simple que cela, car la similarité peut aller de plusieurs façons. Cela pourrait être que je suis 10 % de Marlene et 10 % de quelqu'un d'autre et 80 % de quelqu'un d'autre, et cela se combine en une combinaison linéaire de différentes personnes. Ce score qui est extrait pour chaque produit pour moi est une combinaison des poids de différentes personnes. C'était une percée, et Netflix et le problème de recommandation de films ont stimulé le développement du filtrage collaboratif.

Ensuite, cela a évolué vers, « Pouvez-nous rendre le filtrage collaboratif encore meilleur ? » Y a-t-il des moyens de commencer à incorporer des variables dans le filtrage collaboratif afin que [non seulement] nous sachions que Jack et Marlene sont similaires, Jack et Marlene sont similaires parce que ces produits sont similaires ? Ou, peut-être que Jack et Marlene sont similaires parce qu'ils vivent tous les deux dans la même ville et qu'ils sont tous les deux dans la même démographie ? Cela a supprimé l'un des inconvénients du filtrage collaboratif traditionnel, qui n'avait pas de variables.

Une autre chose qui est apparue était l'idée des réseaux de neurones, et évidemment cela a été une grande chose avec l'apprentissage profond et ainsi de suite. Parce que l'apprentissage profond permet à quelqu'un de prendre les transactions brutes, vous pouvez incorporer beaucoup plus d'informations et laisser l'algorithme faire des choses a priori.

Avec un réseau de neurones, vous pouvez prendre des transactions, vous pouvez prendre des informations sur les produits, vous pouvez prendre des informations sur les clients... Tout cela peut simplement circuler sous sa forme brute. Il n'y a pas besoin de créer de nouvelles variables, et l'algorithme déterminera simplement l'ordre de classement des produits que vous aimez acheter.

**MJ :** L'apprentissage profond est un terme et une méthode si populaires que les gens commencent à les explorer. J'aimerais en entendre davantage.

**JC :** La façon traditionnelle de penser aux réseaux de neurones est qu'ils sont un peu comme des [approximateurs fonctionnels](https://www.cse.unsw.edu.au/~billw/cs9414/notes/ml/04fn/04fn.html). En fait, une régression linéaire est un réseau de neurones, juste avec une couche et un ensemble de poids. Repensons à l'arithmétique du collège ou du lycée, lorsque vous faites la règle de la chaîne, vous avez un f(g(h)) égal à quelque chose. C'est essentiellement ce qu'est un réseau de neurones, mais il découvre en fait le f, g et h corrects qui modélisent le plus précisément vos données.

La forme la plus générique du réseau de neurones profond est un [réseau de neurones feed-forward multicouche](https://towardsdatascience.com/deep-learning-feedforward-neural-network-26a6705dbdc7). Vous pouvez créer plusieurs couches appelées couches denses. C'est dense parce que chaque nœud, qui représente une variable, se connectera à un autre nœud dans la couche suivante.

Le nœud pourrait être les types de produit que vous achetez, ou un nœud peut être un client. Un réseau de neurones pourrait comporter des dizaines de milliers de nœuds. Avec les avancées de la [rétropropagation](https://medium.com/datathings/neural-networks-and-backpropagation-explained-in-a-simple-way-f540a3611f5e) et toutes les nouvelles techniques d'inférence, il est maintenant beaucoup plus facile d'entraîner un réseau de neurones profond qu'auparavant.

Je ne suis pas un expert dans la technologie sous-jacente, mais définitivement un praticien avancé.

**MJ :** Vous avez mentionné plus tôt que certaines de ces méthodes ne sont en fait pas prédictives. Quelles sont les méthodes prédictives, alors ? Quelles sont les méthodes actuelles que des entreprises comme Netflix et Amazon utilisent ?

**JC :** Le filtrage collaboratif, je pense qu'il pourrait peut-être être prédictif, mais la plupart du temps, les gens ne l'utilisent pas de manière prédictive. C'est historiquement ainsi que Netflix l'a utilisé, et c'est simplement une limitation du filtrage collaboratif et de la famille d'algorithmes de factorisation de matrices.

La raison est que la façon dont vous y pensez est en fait un problème de complétion de matrice. Si vous pensez à une matrice, chaque client représenterait une ligne, et chaque colonne représenterait le produit, et chaque cellule d'une matrice est un score qui représente à quel point un client aime ce produit. Dans le cas de Netflix, [ce serait] à quel point un client aime ce film. Comme vous pouvez l'imaginer, cette matrice est probablement assez clairsemée, car tous les clients n'ont pas vu tous les films.

C'est l'un des inconvénients du filtrage collaboratif : non seulement il n'est pas prédictif, mais souvent vous avez une matrice très clairsemée.

La façon d'initialiser cette matrice est d'utiliser une figure historique. Peut-être que c'est le classement de Jack sur le film, parce qu'il a regardé le film la semaine dernière et qu'il lui a donné un 5. Ce n'est pas prédictif dans le sens où peut-être que je donnerais au film un cinq la semaine prochaine.

Je pense qu'une partie de Netflix a décidé que c'était bien parce que la préférence pour les films est généralement assez stable dans le temps. Si vous avez regardé un film il y a un an, il y a de bonnes chances que vous l'aimiez toujours maintenant, donc le composant prédictif n'est pas aussi important pour ce problème.

Dans les transactions ou le commerce de détail, il est tout à fait possible que votre préférence change rapidement, ou dès que vous achetez quelque chose, cela n'a plus le même pouvoir de recommandation.

C'est là que les éléments prédictifs entrent en jeu, et vous pouvez structurer les systèmes de recommandation de manière similaire à la façon dont vous structurez d'autres problèmes comme la détection de désabonnement ou la détection d'anomalies. Vous avez une matrice X qui contient toutes vos variables, et ces variables X sont historiques. Vous savez que si vous êtes à un moment T, ce sont des choses qui sont au moment T moins un avant, et votre variable Y est la chose qui est prédictive, donc c'est en fait le moment t+1, ou t plus un mois, ou quelle que soit la période de prévision que vous avez.

C'est ainsi que la plupart des problèmes de classification et de régression sont structurés. Si vous entraînez un réseau de neurones profond, c'est à peu près exactement l'information qui entre dans l'entraînement de votre réseau de neurones.

Je ne parle pas de tenseurs ou de quoi que ce soit de plus dimensionnel que cela, mais en général, vous aurez un ensemble de données qui contient vos données historiques, vous aurez une fonction objectif ou une variable Y qui contient l'information future que vous voulez prédire.

Ce qui se passe, c'est que lorsque vous essayez de prédire quelque chose étant donné votre point actuel dans le temps, vous ne fuyez pas l'information. Vous n'utilisez que l'information que vous connaissez au moment t pour prédire le moment t+1.

**MJ :** À votre point sur tous ces cas d'utilisation que vous avez mentionnés, comme le commerce de détail, les films, tant de marques (petites et grandes) parlent de construire un moteur de recommandation de quelque sorte. Qu'est-ce qui le rend vraiment puissant ?

Avec Amazon, évidemment, vous pouvez dire qu'ils ont un grand ensemble de données, mais quels sont certains des autres variables qui permettent à un moteur de recommandation d'être meilleur que le suivant ?

**JC :** Les données sont le numéro un, [comme] les actifs de données que votre entreprise a abrités. Si c'est Amazon, évidemment, c'est le nombre incroyable de clients et de transactions qu'ils ont, l'incroyable diversité de produits qu'ils ont, non seulement dans les produits populaires mais même dans la longue traîne.

Après les données, l'algorithme est ce qui peut aider à différencier. Si vous êtes une entreprise qui utilise des règles commerciales simples par rapport aux réseaux de neurones profonds ou quelque chose de similaire, cela fait également une grande différence.

Une autre chose que beaucoup de gens sous-estiment mais qui est super importante est l'expérience client. Au lieu de simplement jeter un ruban avec un tas de recommandations, réfléchir à tout un écosystème avec des choses comme « quels sont tous les points de contact que les clients reçoivent », « est-ce que je fatigue le client avec trop de points de contact », « est-ce une surcharge d'informations », « est-ce que je représente correctement l'intention » ?

Amazon, par exemple, a historiquement été utilitaire. Un bon nombre de clients [vont] chez Amazon avec un agenda explicite en tête, comme ils voulaient acheter des choses spécifiques, [donc] ils le tapent et l'achètent. [Amazon] a essayé très fort de tirer parti de cela, car c'est une bonne chose, c'est bien que les gens viennent chez Amazon pour le but. Tirer parti de cela, s'appuyer dessus pour voir comment nous pouvons mieux vendre en croix, vendre des choses dans différents canaux [comme] les médias numériques, vendre du matériel [comme] les Kindles.

**MJ :** Je ne sais pas si vous avez vu le [rapport de Mary Meeker](https://www.recode.net/2018/5/30/17385116/mary-meeker-slides-internet-trends-code-conference-2018). Elle avait dit que 49 % des personnes qui vont sur Amazon commencent et finissent essentiellement avec Amazon. Ils recherchent sur Amazon puis achètent sur Amazon.

À votre point, je pense que vous avez raison, la plupart des gens viennent avec l'intention d'acheter là-bas. C'est très utilitaire.

**JC :** Un autre exemple vraiment excellent que j'aime donner est Starbucks. Si vous faites partie du programme de fidélité Starbucks, plus souvent qu'autrement, vous avez vu des jeux qui apparaissent soit par email soit sur votre application.

C'est un jeu donc c'est un medium différent de votre système de recommandation traditionnel, mais sous-jacent à ce jeu se trouve en fait un moteur de recommandation basé sur les données clients, qui détermine quels produits vous aimez, quel est le type d'engagement dont vous avez besoin pour être un client plus précieux, et ainsi de suite.

Le point principal est que les scientifiques des données doivent travailler en étroite collaboration avec des designers, des marketeurs ou des analystes d'affaires afin de concevoir l'expérience optimale.

Sinon, quelque chose comme un jeu nécessite tant de lignes de pensée transversales que je ne pense pas qu'un scientifique des données ou un marketeur aurait pu le faire seul. Les scientifiques des données auraient simplement essayé de résoudre le problème de recommandation sans penser à l'expérience, tandis que les marketeurs n'auraient même pas réalisé que la science des données pouvait être utilisée pour optimiser quelque chose. Littéralement, pour autant de clients qu'ils peuvent avoir, vous pouvez tirer autant de leviers. Si vous avez 15 millions de clients, vous pourriez littéralement avoir 15 millions de variantes en utilisant la science des données.

**MJ :** Nous avons déjà parlé de certains exemples où [les entreprises ont] construit un moteur de recommandation vraiment solide. Pouvez-vous donner d'autres exemples de bons moteurs de recommandation que vous avez vus, que ce soit des marques ou des cas d'utilisation spécifiques au sein des entreprises ?

**JC :** Il y en a tellement. J'adore Spotify. Je pense qu'ils font un excellent travail avec le système de recommandation basé sur les clients, c'est-à-dire trouver quelles autres personnes vous ressemblent et ce qu'elles aiment écouter...

**MJ :** Ils écrasent SoundCloud à ce stade, à mon avis. J'utilisais SoundCloud avant Spotify...

**JC :** Moi aussi, en fait. Mais oui, Spotify est définitivement — en termes d'ingénierie et de la sophistication de ce qu'ils recommandent — ils font tellement plus.

La chose intéressante — très probablement, je ne sais pas avec certitude parce que je ne travaille pas là-bas — ils regardent en fait la musique elle-même. Que ce soit les tags de la musique, comme quel genre de genre c'est, qui est l'artiste... ils regardent probablement aussi quel est le tempo, quels sont les instruments, et ils creusent en fait dans l'ADN de la musique, similaire à ce que faisait Pandora et l'utilisent pour déterminer quels types de musique vous aimeriez. Donc, aller au-delà du genre également.

J'ai remarqué que parfois Spotify me recommande des choses que je ne pensais pas aimer écouter, mais plus je les écoute, plus je réalise qu'elles sont en fait similaires à des choses que j'aime.

Un autre exemple est YouTube. Ils ont des KPI légèrement différents dans le commerce de détail — dans le sens où la plupart de vos KPI ne sont pas basés sur les transactions, ils se concentrent sur l'engagement — donc ils sont conçus pour vous garder sur le site web plus longtemps.

Je pense que leur processus commence probablement par la conception, donc quel est le UX réel que nous voulons permettre à quelqu'un qui est actuellement sur la plateforme de faire, donc un peu comme la cartographie du parcours client et déterminer à ce stade du parcours, quelle est la bonne expérience pour le client.

Un exemple pourrait être lorsque vous venez de terminer de regarder une vidéo, c'est un excellent morceau de propriété pour intervenir et déterminer en fonction de ce qui vient d'être regardé, donc contextuel sur Marlene ou Jack finissant cette vidéo sur les chats flous, quelle est la prochaine chose que nous pensons qu'ils aimeront regarder ?

Souvent, ces indices contextuels apparaissent [à] des moments opportuns dans un parcours client, et je pense que YouTube détermine quels sont ces parcours et quels sont ces points optimaux, puis construit des bouteilles autour de cela.

**MJ :** Maintenant, vous avez suscité une question différente, qui est comment les gens s'y prennent exactement pour créer ces moteurs ? Vous avez mentionné qu'avec différents cas d'utilisation, vous devez commencer par différentes questions et différents points. Par exemple, vous avez dit qu'avec YouTube, vous pourriez commencer par une question de conception et d'engagement, mais avec Spotify, cela pourrait être différent.

Quelles sont les différentes façons dont vous commenceriez même à concevoir ce moteur pour une bonne expérience client ?

**JC :** C'est une bonne question. Je souhaite qu'il y ait une réponse universelle, mais je ne pense pas qu'il y en ait. C'est un peu une zone grise car il y a plusieurs façons dont YouTube ou Spotify pourraient avoir conçu leur expérience, mais je pense que c'est généralement juste travailler de manière transversale et déterminer ce que c'est, quel est l'ordre de classement des choses qui intéressent les clients.

Pour Amazon, c'était, « Hé, nos clients sont vraiment utilitaires, vendons-leur un peu plus en croix. Pour Expedia ou les entreprises de voyage, c'est « Déterminons les segments de clients. » Peut-on déterminer si quelqu'un est un voyageur de luxe ou un voyageur d'affaires ? Sont-ils [à] la fin du cycle de vie du client, où ils sont sur le point de se désabonner et d'aller sur un autre site web, ou sont-ils au début, donc c'est plus une question d'éducation ?

Il y a tellement de façons de caractériser un client, mais je pense que cela commence généralement par une meilleure compréhension du client, comme les segments dans lesquels ils se trouvent, comment ils s'engagent. Parmi les personnes qui abandonnent, quels sont les indicateurs avancés qui pourraient nous dire que vous abandonnez ? Parmi les personnes qui commencent, quels sont les indicateurs si quelqu'un grandit réellement dans une trajectoire stable ? Ce sont simplement vos modèles typiques de cycle de vie client, et à partir de là, concevoir la bonne expérience pour maximiser le cycle de vie.

**MJ :** J'imagine que les KPI sont similaires. Les KPI pour Spotify, par exemple, ou pour Amazon sont probablement différents de ceux de YouTube, à votre point autour de [savoir si] vous visez l'achat ou la prochaine chanson ou l'engagement.

Quels seraient, selon vous, certains KPI de base que vous suivez pour ces moteurs ?

**JC :** C'est une très bonne question. La conversion, qu'il s'agisse de convertir en une transaction ou de convertir en un clic, c'est généralement la norme de facto pour un système de recommandation. J'ai également vu des systèmes de recommandation optimisés pour d'autres choses comme le chiffre d'affaires et le profit et peut-être même des choses plus ésotériques, comme le chiffre d'affaires sur les articles qui ont une marge plus élevée que 30 % net des retours, donc cet objectif serait « Je veux recommander des choses qui ont une marge élevée et que les gens ne retournent pas simplement. » Vous pouvez donc être très précis avec ces KPI.

La chose à réaliser, en choisissant entre ceux-ci, est ce que je permets ? En choisissant ce KPI, qu'est-ce qui arrive réellement aux choses que je recommande ?

Pour celui de la marge, ce qui est le plus susceptible de se produire est que si nous construisons un modèle de science des données qui optimise le profit, naturellement vous allez commencer à recommander des choses qui ont une marge élevée. Cela ne correspond peut-être pas nécessairement à ce que le client veut. Même si cela ne dit pas profit élevé, comme vous n'appelez pas explicitement cela sur votre site web, cela biaise toujours votre algorithme pour choisir des choses qui ne sont pas représentatives d'un ensemble plus large.

Un autre KPI intéressant dans le système de recommandation est la diversité. Dans la plupart des modèles, le modèle aura une conviction assez forte du type de client que vous êtes. Il ne tient pas compte de la corrélation croisée entre les choses que je recommande. Peut-être qu'en allant sur Amazon, il détermine que j'aime vraiment les chaussettes. Très probablement dans le top dix, vous verrez des chaussettes, peut-être que vous verrez des sous-vêtements, peut-être que vous verrez plus de chaussettes. Bien que cela puisse être vrai que j'aime les chaussettes, un emplacement suffit pour cette chaussette. Il doit y avoir un moyen de prendre des choses qui ont obtenu un score inférieur dans l'algorithme et de les faire remonter pour le bien de la diversité.

Il existe ces fonctions objectives [hybrides](http://kronosapiens.github.io/blog/2017/03/28/objective-functions-in-machine-learning.html) où vous voulez maximiser la conversion, mais vous devez également prendre en compte l'expérience client. Si vous leur donnez de la diversité, alors ils explorent les produits à longue traîne, et [peut-être] à long terme [cela] pourrait augmenter la valeur client.

**MJ :** J'ai tellement de questions, mais je pense que nous manquons de temps. Je veux juste poser cette dernière question : quels sont vos derniers conseils pour construire un bon moteur de recommandation ? Comment éviter les pièges ? Quelles sont les choses à surveiller ?

**JC :** Le conseil numéro un : vous connaissez votre produit mieux qu'un fournisseur. Le fournisseur peut vous donner des conseils sur l'algorithme et ce qu'il faut utiliser, mais [ne] branchez pas un système de recommandation dans votre site web sans vraiment comprendre votre entreprise et ce qui la motive. Est-ce comme du lait, des œufs et du pain, ou est-ce une question de mode où vous ne voulez pas recommander des choses trop similaires, ou si c'est une question de cycle de vie où vous devez recommander des choses qui correspondent au cycle de vie, seul vous le savez. Si un fournisseur prétend connaître cela mieux que vous, je pense que c'est un signe clair de rester à l'écart.

Numéro deux, vous devez considérer la maturité de votre entreprise pour réellement adopter quelque chose d'aussi compliqué qu'un réseau de neurones profond. Évidemment, un réseau de neurones profond vous donnera des performances de pointe, [mais] votre entreprise n'en a peut-être pas besoin en fonction de sa situation.

Une chose que j'ai trouvée est que si vous regardez tous les articles de recherche sur les [forêts aléatoires](https://medium.com/@williamkoehrsen/random-forest-simple-explanation-377895a60d2d) par rapport aux [arbres de décision boostés par gradient](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) par rapport aux [réseaux de neurones](http://news.mit.edu/2017/explained-neural-networks-deep-learning-0414), la différence dans la pointe une fois que vous avez dépassé l'arbre boosté par gradient est vraiment petite. Vous verrez généralement une amélioration de cinq à dix pour cent de votre précision en passant à quelque chose de pointe. Ce que cela signifie, c'est que vous pouvez obtenir 80 % de ce dont vous avez besoin avec quelque chose de relativement simple. Prenez cela en compte.

Une autre chose à prendre en compte est la ressource. Si vous décidez de construire quelque chose en interne, il est difficile de trouver un expert en apprentissage profond ou un expert en apprentissage automatique qui peut le maintenir au fil du temps. Ce que cela signifie, c'est que votre entreprise doit être suffisamment mature pour soutenir ces ingénieurs, car je pense que beaucoup de gens ont une notion que une fois qu'ils l'ont construit pour moi, c'est fait, j'ai la capacité.

En réalité, c'est quelque chose qui doit être maintenu au fil du temps, amélioré, des bugs peuvent apparaître. Aucun pipeline d'apprentissage automatique n'est parfait. D'un point de vue stratégique ou technique, vous devez y penser comme un investissement à long terme plutôt que comme une construction et le jeter par-dessus la clôture, ce qui nous ramène à pourquoi il est plus important de construire une capacité en interne plutôt que de faire appel à un fournisseur, car le fournisseur n'est pas investi à long terme dans votre entreprise comme vous l'êtes.

**MJ :** En y réfléchissant, je pense que vous êtes probablement le meilleur moteur de recommandation. Que pensez-vous serait un bon sujet pour nous de couvrir dans une autre de nos séries AI for Growth ?

**JC :** Eh bien, en le branchant sur le réseau de neurones humain, je pense que quelque chose autour de la tarification serait intéressant [comme] la tarification dynamique et la capacité à tarifer à la volée est quelque chose que, surtout pour les entreprises qui s'éloignent des canaux physiques ou sur commande, des entreprises comme Uber où la tarification des choses est faite sur le moment, c'est quelque chose que l'apprentissage automatique a vraiment juste effleuré dans l'industrie.

Une autre chose vraiment intéressante est l'intersection entre la tarification et la personnalisation. Non seulement servir le bon contenu, mais aussi servir le bon prix en conjonction avec ce contenu pour donner des promotions personnalisées qui sont dynamiques et adaptées à chaque client. Cela semble être la prochaine frontière pour le commerce de détail au cours des trois à cinq prochaines années. Je pense que cela va se produire assez rapidement, car il y a tellement de valeur associée. Je suis heureux de venir et de discuter davantage, en fonction du nombre de ceux-ci que vous avez.

**MJ :** Merci beaucoup, Jack. Ce fut une conversation merveilleuse, et je suis sûre que nous vous aurons simplement dans une autre série une autre fois, donc merci. Et merci à tous d'avoir suivi AI for Growth. Nous vous verrons à notre prochain épisode !

![Image](https://cdn-media-1.freecodecamp.org/images/0*teA74RZe1k3nGCS7.png)

#### Vous avez appris quelque chose ? Cliquez sur le ? pour dire « merci ! » et aider les autres à trouver cet article.

_La transcription complète de cet entretien a été publiée pour la première fois sur [TopBots](https://www.topbots.com/developing-hyperpersonalized-recommendation-systems-interview-jack-chua-expedia/?utm_medium=article&utm_source=Medium&utm_campaign=Hyperpersonalized)._