---
title: Comment choisir les meilleurs langages de programmation, bibliothèques et patterns
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2025-08-10T17:13:37.689Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-best-programming-languages-libraries-and-patterns
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754846007203/c9db729e-ebed-4726-8e3e-5414c8e2714d.png
tags:
- name: Programming Blogs
  slug: programming-blogs
- name: software development
  slug: software-development
- name: programming languages
  slug: programming-languages
seo_title: Comment choisir les meilleurs langages de programmation, bibliothèques
  et patterns
seo_desc: In my first few years learning software development and building applications,
  I was quite interested in finding the best programming language, platform, libraries,
  frameworks, patterns, and architectures available. I thought that by finding the
  best...
---

Au cours de mes premières années d'apprentissage du développement logiciel et de création d'applications, j'étais très intéressé par la recherche du meilleur langage de programmation, de la meilleure plateforme, des meilleures bibliothèques, des meilleurs Frameworks, patterns et architectures disponibles. Je pensais qu'en trouvant les *meilleures* choses et en me concentrant sur ces sujets à l'exclusion des autres, je pourrais éviter de perdre un temps précieux.

Bien que j'aie compris assez tôt qu'il était important de restreindre mon champ d'action en utilisant une approche d'apprentissage par projet (par opposition à l'approche par liste de sujets), trouver les meilleurs outils pour le travail était une autre affaire.

Si vous êtes justement à la recherche de certaines de ces choses, alors cet article est pour vous. Après plus d'une décennie passée à programmer des produits, à créer des applications clientes, à répondre à des milliers de questions de développeurs juniors et intermédiaires, et à me débattre moi-même avec ces questions, je ferai de mon mieux pour expliquer comment trouver les meilleures *choses*.

Cet article est destiné aux développeurs de niveau junior à intermédiaire qui cherchent des réponses pratiques à des problèmes difficiles. Vous n'aurez pas besoin d'une expérience approfondie de la programmation pour le parcourir et vous pourrez sauter les discussions techniques spécifiques. Celles-ci sont destinées à être des informations utiles, mais le cœur de cet article porte sur la manière de prendre ces décisions en général en utilisant ce que j'appelle : La Loi de l'Adéquation.

Les sujets que je vais aborder sont :

* [Comment trouver le meilleur de tout](#heading-comment-trouver-le-meilleur-de-tout)
    
    * [Comment trouver la meilleure gourde](#heading-comment-trouver-la-meilleure-gourde)
        
* [Comment trouver le meilleur langage de programmation](#heading-comment-trouver-le-meilleur-langage-de-programmation)
    
    * [Naviguer entre les opinions publiques et d'experts](#heading-naviguer-entre-les-opinions-publiques-et-dexperts)
        
    * [Bas niveau vs Haut niveau](#heading-bas-niveau-vs-haut-niveau)
        
    * [Structure stricte (statique) vs Structure souple (dynamique)](#heading-structure-stricte-statique-vs-structure-souple-dynamique)
        
    * [La popularité n'est qu'un facteur parmi d'autres](#heading-la-popularite-nest-quun-facteur-parmi-dautres)
        
    * [La popularité n'est pas une garantie d'emploi](#heading-la-popularite-nest-pas-une-garantie-demploi)
        
    * [Matériel et faire avec ce que l'on a](#heading-materiel-et-faire-avec-ce-que-lon-a)
        
    * [Et si je veux que l'IA code pour moi ?](#heading-et-si-je-veux-que-lia-code-pour-moi)
        
    * [Éviter le biais des coûts irrécupérables](#heading-eviter-le-biais-des-couts-irrecuperables)
        
* [Comment trouver les meilleures bibliothèques et Frameworks](#heading-comment-trouver-les-meilleures-bibliotheques-et-frameworks)
    
    * [Que sont les bibliothèques et les Frameworks ?](#heading-que-sont-les-bibliotheques-et-les-frameworks)
        
    * [Comment choisir des bibliothèques et des Frameworks](#heading-comment-choisir-des-bibliotheques-et-des-frameworks)
        
* [Comment trouver les meilleurs principes et pratiques de programmation](#heading-comment-trouver-les-meilleurs-principes-et-pratiques-de-programmation)
    
    * [D.R.Y – Don’t Repeat Yourself](#heading-dry-dont-repeat-yourself)
        
    * [Et les autres principes de programmation ?](#heading-et-les-autres-principes-de-programmation)
        
* [Une note sur les patterns et les architectures](#heading-une-note-sur-les-patterns-et-les-architectures)
    
    * [Comment trouver la meilleure architecture logicielle](#heading-comment-trouver-la-meilleure-architecture-logicielle)
        
    * [Le piège des design patterns](#heading-le-piege-des-design-patterns)
        
* [Résumé](#heading-resume)
    

## Comment trouver le meilleur de tout

Je vous invite à suivre quelques exemples basiques non techniques qui posent les bases du reste de cet article. Les exemples peuvent sembler idiots pour certains, mais j'y ai intégré des schémas conceptuels que vous pouvez appliquer aux langages de programmation, aux outils et aux concepts – ainsi qu'à presque tout ce à quoi les termes bon, mauvais, meilleur ou pire peuvent s'appliquer.

### Comment trouver la meilleure gourde

Supposons que vous cherchiez à résoudre le problème de l'hydratation et que vous souhaitiez acheter une gourde.

Vous considérez que pour trouver la meilleure gourde, il faudrait examiner :

* Les opinions et avis du public
    
* Les opinions et avis d'experts
    
* Les descriptions et la réputation du fabricant
    
* L'achat et le test de gourdes (bien que de préférence pas toutes, car cela coûte généralement trop de temps et d'argent)
    

Tous ces éléments sont à prendre en considération. Quelque chose qui n'est pas bien testé par le public présente une incertitude. Les avis d'experts peuvent aider à éclairer votre décision, mais vous devez tenir compte des biais et des motivations de ces experts. Vous devriez également vous demander si le fabricant a un historique de qualité, de design et de support client, ou s'il cherche simplement à maximiser ses profits.

Après quelques recherches, vous arrivez à ces options :

* Une bouteille d'eau en plastique provenant d'un distributeur automatique
    
* Une bouteille métallique high-tech dans laquelle on peut même faire bouillir des choses !
    
* Une gourde en plastique simple, mais de source éthique, réutilisable et sans BPA
    

Cependant, vous remarquez que personne ne semble s'accorder universellement sur l'option la meilleure. Il y avait généralement des opinions communes, mais il n'est jamais arrivé que chaque expert ait la même évaluation ou recommandation.

Après réflexion, il est devenu évident que vous deviez considérer comment, quand et où vous utiliserez cette gourde. En d'autres termes, vous devez **considérer le contexte ou la situation** de son utilisation.

Supposons trois contextes différents dans lesquels vous devez prendre cette décision :

* Vous vous trouvez dans une aire de repos dans la Vallée de la Mort en Californie (souvent considérée comme l'endroit le plus chaud de la Terre en été) et il y a devant vous un distributeur rempli de vieilles bouteilles d'eau en plastique génériques, bon marché et pleines de micro-plastiques. Mais vous n'avez pas d'autres options et vous avez très soif.
    
* Vous êtes dans un magasin de camping en train de préparer un voyage en Nouvelle-Zélande avec beaucoup de randonnées et peu d'accès à l'eau filtrée.
    
* Vous cherchez sur votre site de shopping préféré quelque chose que vous pouvez apporter au travail chaque jour pour éviter les maux de tête dus à la déshydratation.
    

En résumé, vous ne devriez pas ignorer les connaissances de seconde main, les opinions d'experts, la popularité, les notes, les avis, les témoignages et même l'expérience directe. Mais vous ne trouverez jamais la meilleure gourde pour chaque situation dans laquelle vous vous trouverez. Le meilleur de \"n'importe quoi\" dépend du problème que vous essayez de résoudre et du contexte (les termes exigences ou situation s'appliquent également ici) de ce problème.

En d'autres termes, aucune de ces choses n'a une valeur absolue ou fixe – leur valeur est toujours relative. J'appelle cela la **Loi de l'Adéquation**.

Discutons maintenant de quelques exemples directement liés à la conception et au développement de logiciels.

## Comment trouver le meilleur langage de programmation

La Loi de l'Adéquation s'applique tout autant aux langages de programmation qu'aux gourdes – même si les détails et les contextes sont différents. Le meilleur langage de programmation pour chaque personne, équipe, problème ou fonctionnalité n'existe pas.

Mais j'ai des détails et des contextes spécifiques à proposer qui pourraient vous aider à répondre vous-même à cette question. Cette section couvrira des détails concrets et quelques idées générales sur la manière de choisir un langage de programmation. Ces schémas s'appliquent également aux Frameworks, aux bibliothèques et à la plupart des autres aspects de la programmation.

Si vous n'êtes pas intéressé par le sujet du choix d'un langage de programmation, n'hésitez pas à passer aux sections suivantes sur des sujets comme les bibliothèques, les principes et les patterns.

### Naviguer entre les opinions publiques et d'experts

Premièrement, vous devez être sceptique quant à la popularité et aux opinions des experts et des \"influenceurs\".

Mon conseil général ici est d'être extrêmement prudent avec toute personne qui avance l'une de ces affirmations :

* Le langage \"X\" est le meilleur (bien que dire \"le langage X est mon préféré\" soit parfaitement acceptable)
    
* Le langage \"X\" est le pire, est terrible, est mort, est une ordure, est inutile, et ainsi de suite.
    

Trois groupes de personnes font généralement ce genre de déclarations :

* Des experts réels qui expriment leurs préférences personnelles mais les présentent comme des faits immuables (comme je regrette que ce soit si courant dans cette industrie)
    
* Des non-experts répétant les opinions du groupe ci-dessus ou qui n'ont pas encore compris la Loi de l'Adéquation
    
* Des chasseurs d'engagement (engagement farmers)
    

Il convient également de noter que les gens peuvent être experts sur un sous-ensemble de problèmes, mais cela ne garantit pas que leurs opinions sur tous les problèmes soient d'un niveau expert.

Cela ne signifie pas que vous devriez rejeter par réflexe les opinions d'experts en général. Considérez à la fois les antécédents de la personne et le degré d'attention qu'elle porte au contexte de sa déclaration.

Regardons deux exemples :

* *L'expert A* dit : \"Python possède les meilleurs outils, le meilleur support et le meilleur écosystème pour le développement ML (Machine Learning)\"
    
* *L'expert B* dit : \"Python est le meilleur langage de programmation\"
    

Alors que *l'expert B* fait manifestement preuve d'un manque de précision (délibéré ou non) si vous m'avez suivi jusqu'ici, *l'expert A* est un cas différent. Que les affirmations de *l'expert A* soient vraies ou non (pour mémoire, j'ai écrit un peu de Python mais pas de code ML), vous pouvez dire qu'il tient compte des détails et du contexte. Recherchez des personnes comme *l'expert A* !

### Bas niveau vs Haut niveau

En termes simples, les langages de programmation de bas niveau sont difficiles à lire et à écrire pour les humains. De plus, ils ont tendance à être plus rapides et à avoir une empreinte mémoire plus faible que les langages de haut niveau. À l'inverse, les langages de haut niveau sont plus proches du langage humain, ce qui les rend généralement plus faciles à manipuler pour les humains.

Je dois toutefois confesser que j'ai vu de nombreux exemples de personnes écrivant du code inintelligible dans des langages de haut niveau – ne faites pas cela, s'il vous plaît.

Quelqu'un travaillant sur un système embarqué pourrait vouloir le faire dans un langage comme C ou C++ pour optimiser les performances ou contourner les limitations de mémoire et de puissance de calcul.

Mais dans les systèmes d'entreprise, qui doivent fonctionner sur une variété de plateformes et qui se mêlent étroitement aux exigences commerciales, aux règles et aux objets du monde réel (pensez aux produits, aux utilisateurs, etc.), les langages de bas niveau ne sont pas si populaires. Après tout, les cadres supérieurs et moyens ne se soucient généralement des optimisations de bas niveau que dans la mesure où elles affectent l'expérience utilisateur.

J'adore l'optimisation en général, mais n'oubliez jamais que tout est rapide avec de petits ensembles de données (c'est-à-dire quand *n* est petit) ou une puissance de calcul élevée. En termes plus simples, les préoccupations humaines comme la lisibilité sont parfois nettement plus importantes que des optimisations insignifiantes sur l'efficacité.

### Structure stricte (statique) vs Structure souple (dynamique)

Ironiquement, les principaux inconvénients et avantages d'un langage comme Java (très structuré et verbeux) par rapport à un langage comme JavaScript (plutôt l'inverse, selon la façon dont vous l'utilisez) sont les mêmes selon le contexte.

En parlant de systèmes d'entreprise, l'utilisation de structures, de types, d'interfaces, de classes, de threading, de primitives de concurrence et de constructions de programmation similaires peut présenter divers avantages. Cela peut vous protéger tout en offrant une certaine flexibilité via les hiérarchies de types, les interfaces, les protocoles, les abstractions, etc.

De plus, l'étude des design patterns peut vous apprendre des solutions reproductibles à des problèmes rencontrés depuis l'aube de l'ordinateur polyvalent – ou peu après.

Mais la Loi de l'Adéquation s'applique toujours ici. Peut-être avez-vous juste besoin d'écrire un script rapide pour migrer des données d'une base SQL à une autre. Peut-être savez-vous comment aborder les problèmes avec une approche plus fonctionnelle qui ne nécessite pas ou décourage l'utilisation d'objets, de classes ou de structs. Peut-être réalisez-vous un jour que le fait d'essayer d'appliquer des design patterns, des architectures, des hiérarchies et des constructions similaires dans chaque situation a en fait créé autant de problèmes qu'ils n'en résolvaient. Nous y reviendrons plus tard.

Il convient également de mentionner que la plupart des concepteurs et mainteneurs de langages modernes ont compris que nous, les développeurs, aimons la flexibilité. Beaucoup d'entre nous veulent éviter l'optimisation prématurée et une structure inutile, mais ne veulent pas non plus que notre code explose parce que nous avons accidentellement dit au programme d'additionner 1.23356 + \"Rhinocéros\".

Le point principal est que la structure ou l'absence de structure est à la fois une bénédiction et une malédiction, selon l'endroit où elle est utilisée.

### La popularité n'est qu'un facteur parmi d'autres

Je ne vais pas dire que la popularité n'est pas pertinente et que vous devriez commencer par le langage de programmation de hipster le moins populaire que vous puissiez trouver. Loin de moi l'idée de critiquer les langages de programmation de hipster, mais l'impopularité n'est généralement pas une bonne chose en soi non plus.

Le point clé est que beaucoup de gens qui s'expriment sur les langages de programmation (probablement la plupart) n'ont pas une expérience abondante sur une variété de plateformes, de langages et de contextes. Si quelqu'un n'a jamais écrit que du Python et aime cela, il aura naturellement tendance à le considérer comme supérieur aux autres.

Nous, les humains, avons tendance à trouver la première chose qui fonctionne pour nous et à nous battre jusqu'au bout pour la défendre. Mais pour prendre une approche plus anecdotique, je connais quelques douzaines de développeurs de niveau intermédiaire à senior qui ont une vaste expérience en Java et dans d'autres langages. Bien que Java soit toujours classé comme l'un des langages les plus populaires au monde, un seul de ces développeurs que je connais préfère réellement écrire en Java s'il a le choix.

Ne commettez pas l'erreur de supposer que la première chose qui fonctionne pour beaucoup de gens sera la dernière chose que vous aurez besoin d'essayer. J'ai de temps en temps expérimenté des langages tels que Haskell, qui m'a enseigné de nombreuses leçons précieuses sur les avantages de rendre mon code plus fonctionnel (et fonctionnellement pur) par nature.

Mais je n'ai absolument aucune intention d'utiliser Haskell comme solution de prédilection pour créer des applications GUI.

### La popularité n'est pas une garantie d'emploi

L'une des choses les plus courantes que vous devriez considérer est de savoir si le langage que vous choisissez vous aidera à trouver un emploi – en supposant que ce soit une préoccupation. Les influenceurs adorent dire aux gens de choisir un langage particulier parce qu'il a le plus de Commits publics sur GitHub, ou un autre parce qu'il a le plus grand nombre de programmeurs l'utilisant (ce qui est, en pratique, impossible à affirmer avec certitude).

Laissez-moi renverser la situation : supposons que la combinaison de langage de programmation et de plateforme la plus courante soit JavaScript et le web. Supposons ensuite que nous ayons des données assez concrètes sur le nombre d'offres d'emploi sur le web qui confirment que le plus grand volume d'emplois disponibles concerne cette combinaison. Supposons enfin que, pour une raison quelconque, vous détestiez JavaScript et que vous ayez aimé créer un site web en utilisant PHP.

Vous trouverez des voix qui vous diront que PHP est un langage mort et une impasse pour la recherche d'emploi.

Mais si vous cherchez bien, vous remarquerez qu'il existe une bonne offre d'emplois à la recherche de développeurs PHP capables d'étendre et de maintenir des bases de code existantes. Vous pourriez également avoir de bien meilleures chances d'obtenir un entretien parce que *le ratio entre les offres d'emploi et les candidatures est nettement meilleur pour les développeurs PHP* que pour les développeurs JavaScript. En fait, mon équipe a récemment embauché un développeur PHP !

### Matériel et faire avec ce que l'on a

Cette section est largement hors de propos pour les développeurs web, mais peut être extrêmement importante pour ceux qui cherchent à cibler du matériel ou des systèmes d'exploitation spécifiques. En termes simples, si vous n'avez pas d'ordinateur sous Mac OS avec XCode, vous aurez beaucoup de mal à développer une application iOS, par exemple. Dans mon cas, en 2014, j'ai choisi le développement Android en partie parce que j'avais étudié un peu de Java – bien qu'une considération majeure ait été que j'avais un téléphone Android.

Il existe des moyens de contourner cela en payant pour utiliser un appareil à distance (comme un Mac distant via un service en ligne), mais d'après mon expérience d'il y a quelques années, ces services n'étaient pas géniaux.

Réfléchissez aux ressources dont vous disposez et à la manière dont cela s'inscrit dans ce que vous voulez construire ou pour qui vous voulez travailler. Si vous n'avez pas grand-chose d'autre qu'un ordinateur bon marché avec un navigateur web et que vous voulez quand même créer des applications GUI, le développement web peut être un excellent choix.

### Et si je veux que l'IA code pour moi ?

Bien que ce sujet mérite un article séparé, je ne pense pas que ce soit une question déraisonnable à poser. Il y a un an, je vous aurais dit qu'au mieux, l'IA pouvait écrire du code de base et vous aider à apprendre des choses qui pourraient être vraies ou fausses.

Comme les choses ont changé ! Bien que je ferais mal mon travail si je copiais-collais du code que je ne comprenais pas ou que je ne testais pas, l'IA est absolument devenue un multiplicateur de force pour moi en tant que développeur.

Pour revenir au sujet en question, quel est le rapport avec le choix d'un langage de programmation ? Eh bien, après vous avoir dit que la popularité n'est pas toujours cruciale, par la nature même du fonctionnement des LLM, la popularité est un facteur. En termes d'utilisation générale, des langages comme Python, JavaScript et Java sont susceptibles d'avoir la plus grande quantité de données d'entraînement. Mon expérience a été que les langages que j'utilise habituellement, tels que Kotlin, TypeScript et Swift, s'en sortent également bien.

Mais il existe un effet secondaire curieux du développement d'applications Android ou iOS que je ne ressens pas autant dans le développement web. La nature de ces plateformes et SDK en constante évolution, avec des dizaines de milliers de bibliothèques tierces, des douzaines d'architectures et des opinions infinies sur les meilleures pratiques et les anti-patterns, signifie que les LLM peuvent avoir de sérieux problèmes de complexité ou de spécificité.

Je m'attends à ce que ce problème soit résolu à mesure que les services de LLM améliorent la vérification de l'exactitude ou d'autres méthodes pour réduire les hallucinations.

### Éviter le biais des coûts irrécupérables

Le point le plus important que je puisse faire dans le choix d'un langage de programmation est sans doute d'éviter le biais des coûts irrécupérables. Pendant les premières années de mes études à temps partiel, je n'imaginais pas apprendre une deuxième langue vu la difficulté que j'avais eue à apprendre Java.

Environ 12 ans plus tard, j'ai écrit du code non trivial en Java, Kotlin, Swift, C++, TypeScript et SQL. De plus, j'ai touché au code en C, Python, JavaScript, Racket, Haskell, Objective C, Visual Basic et C#.

Ce n'est pas que j'ai cherché à apprendre toutes ces choses artificiellement – je n'ai pas tendance à apprendre des choses en dehors des problèmes qui se présentent à moi. C'est que ces opportunités d'apprentissage se sont naturellement présentées au fil de mes intérêts personnels et professionnels.

Apprendre les fondamentaux ou approcher la maîtrise de n'importe quel langage de programmation polyvalent aura des retombées sur les autres. Il est vrai que quelqu'un qui apprend Python ou JavaScript sans les bases de l'informatique (CS fundamentals) n'aura pas vraiment d'idée sur le fonctionnement des choses au niveau de l'OS ou plus bas.

Il est également vrai que j'ai rencontré plusieurs personnes qui pourraient probablement coder bien mieux que moi en C/C++/Assembly mais qui n'ont jamais dépassé le stade de la création de petits programmes d'entraînement à l'université ou à l'école.

Continuez simplement à apprendre et essayez de trouver un équilibre entre intérêt personnel et objectifs professionnels.

## Comment trouver les meilleures bibliothèques et Frameworks

Les quelques sujets suivants tournent autour d'une question que nous revisiterons plusieurs fois avant la fin de cet article : « *Est-ce que cela résout plus de problèmes que cela n'en crée ?* »

### Que sont les bibliothèques et les Frameworks ?

Avant de poursuivre, voici une définition utile mais non définitive de la relation entre les bibliothèques et les Frameworks. Vous trouverez d'autres définitions, mais il y a remarquablement peu de consensus sur des sujets comme celui-ci dans cette industrie.

Pour moi, une bibliothèque est du code que vous pouvez prendre quelque part et utiliser pour construire des choses. Cela peut aller d'une seule ligne à un sous-système vaste et complexe – généralement quelque chose entre les deux. Je pourrais vous donner une définition longue et pédante, mais ce n'est pas approprié pour ce contexte (adéquation !).

Un exemple pourrait être la bibliothèque Math de Java (java.lang.Math), qui vous fournit ceci : « *La classe Math contient des méthodes pour effectuer des opérations numériques de base telles que les fonctions exponentielles, logarithmiques, racine carrée et trigonométriques élémentaires.* »

Certaines personnes utilisent le terme Framework de manière interchangeable avec bibliothèque, et cela ne me pose aucun problème. Quand je pense à un Framework, je pense à quelque chose autour duquel on construit des choses et qui n'est pas nécessairement lié à la résolution d'un domaine de problème spécifique (comme les mathématiques).

Un exemple en serait RxJava, qui est un Framework plutôt complexe que vous pouvez utiliser pour lier et gérer les flux de données dans toute une application. J'ai utilisé ce Framework dans presque une douzaine d'applications qui faisaient des choses très différentes sur le principe.

Je considère fondamentalement un Framework comme une bibliothèque – ils ont juste un ensemble d'objectifs différents et souvent une empreinte plus large.

### Comment choisir des bibliothèques et des Frameworks

Quand je pense à choisir des bibliothèques et des Frameworks, je me pose ces questions :

* Est-ce que cela résout plus de problèmes que cela n'en crée par rapport à l'écriture de ma propre solution ?
    
* Est-elle bien maintenue (travail régulier, auteurs réactifs, soutenue par des entreprises technologiques) ?
    
* A-t-elle une bonne documentation (moins un problème maintenant que nous pouvons exploiter l'IA à cette fin) ?
    
* Quel type d'empreinte a-t-elle ?
    

Prenons deux exemples. Je ne citerai pas la plateforme spécifique ni le nom de ces bibliothèques pour éviter de froisser qui que ce soit. Mais elles étaient/sont toutes deux utilisées dans le développement mobile (bien qu'elles résolvent des problèmes GUI courants sur n'importe quelle plateforme).

Premièrement, l'une de mes bibliothèques préférées n'avait qu'une seule tâche : charger des images dans l'interface utilisateur.

Bien que les appareils soient plus puissants qu'auparavant, le chargement de grandes images sur smartphone pour l'affichage peut toujours poser problème. Les systèmes d'exploitation mobiles peuvent être agressifs pour arrêter les programmes (c'est-à-dire les processus) qui utilisent trop de ressources système.

Cette bibliothèque gère tous les aspects du chargement d'images qui me préoccupent :

* Chargement de l'image dans un widget particulier
    
* Affichage d'un indicateur de chargement approprié
    
* Affichage d'un état d'erreur ou de repli optionnel qui indique à l'utilisateur que quelque chose s'est mal passé
    
* Gestion de la complexité du chargement asynchrone (via URL/URI), du traitement et de la compression de flux de bits potentiellement volumineux (c'est-à-dire les données d'image)
    
* Ne gonfle pas inutilement la taille de l'application packagée
    
* Ne modifie pas fréquemment son API publique (pensez aux changements de noms de fonctions qui cassent les implémentations lors de la mise à jour des versions)
    
* Elle résout des problèmes que je ne suis pas intéressé à résoudre
    

Deuxièmement, l'une de mes bibliothèques les moins aimées n'avait également qu'une tâche : la pagination. La pagination, ou paging, désigne ici le chargement de données par *blocs* dans une application. C'est un schéma extrêmement courant dans les applications de panier d'achat ou de réseaux sociaux.

La bibliothèque à laquelle je pense aborde ce problème ainsi :

* Couple étroitement chaque couche de votre application cliente (du front-end au back-end) à ses dépendances
    
* Ce couplage étroit rend les tests difficiles sans passer par quelques contorsions
    
* Gère bien le problème central de la pagination sauf si vous avez besoin de personnalisation ou de cas spécialisés
    
* Modifiait fréquemment son API publique
    
* Résolvait (en général) un problème pour lequel je suis tout à fait disposé à écrire ma propre solution
    
* Ne fonctionnait pas bien avec d'autres Frameworks en raison d'un ensemble restrictif de types et d'un manque de flexibilité
    
* A été constamment mise à jour pendant quelques années puis abandonnée et marquée comme dépréciée (deprecated)
    
* Ne gonflait pas trop la taille de l'application packagée, mais certainement plus que ma propre solution
    

Comme vous pouvez le voir, même quelque chose qui résout raisonnablement bien un problème central peut échouer à ce test simple : cela résout-il plus de problèmes que cela n'en crée ? Ayant écrit moi-même du code de pagination à plusieurs reprises maintenant, il faudrait me convaincre très sérieusement de ne pas le faire.

## Comment trouver les meilleurs principes et pratiques de programmation

Il existe plus de meilleures pratiques et de principes que je n'ai le courage de décrire en détail. Ce que je vais faire, c'est expliquer pourquoi je traite les principes de programmation comme étant distincts de lois immuables/incassables. De la même manière que pour mon objectif de trouver le meilleur langage de programmation, je voulais trouver les meilleurs principes afin d'écrire le meilleur code.

Le problème est que tout principe de programmation que j'ai rencontré a également été soumis à la Loi de l'Adéquation. Je vais discuter d'un exemple tiré de mon expérience personnelle et souligner que la question que nous avons posée plus haut, « est-ce que cela résout plus de problèmes qu'il n'en crée », s'applique également ici.

### D.R.Y – Don’t Repeat Yourself

Ce principe peut être résumé par l'idée que si vous trouvez du code dupliqué, vous devriez l'extraire dans un module séparé (fichier, fonction, classe, bibliothèque, etc.). Sans entrer dans les détails, l'acte d'extraire le code dupliqué dans un module séparé peut être considéré comme un processus d'abstraction.

Pour être juste envers les créateurs et les partisans de cette idée, elle est plus nuancée que cela. Mais beaucoup de développeurs ne prennent jamais la peine de creuser ces nuances – et ils ne devraient pas avoir à le faire. Je suis tombé sur ces nuances simplement en appliquant cette idée plus que je n'aurais dû.

Il existe quelques cas où la duplication de code est parfois préférable :

* Vous avez un ensemble de modules similaires (par exemple, des widgets ou des règles de gestion similaires) mais ils sont utilisés à différents endroits pour des raisons différentes
    
* Vous avez un ensemble de modules similaires qui pourraient changer pour des raisons différentes (par exemple, des demandes changeant rapidement de la part des équipes produit et des clients ayant des priorités différentes)
    
* Vous regroupez délibérément certains modules qui fonctionnent ensemble dans des paquets, fichiers ou répertoires distincts pour isoler les modules/groupements et éviter qu'ils ne s'affectent mutuellement
    
* Vous constatez que vous devez ajouter des détails sur une implémentation particulière dans votre abstraction, mais que ces détails ne s'appliquent pas aux autres implémentations (c'est-à-dire qu'il s'agit d'une mauvaise abstraction)
    

Tout ce que j'ai listé ci-dessus sont des résumés de situations que j'ai rencontrées par le passé. Le point essentiel à retenir est que je suis globalement d'accord avec l'idée d'éviter la duplication de code. Je connais aussi des cas où je la préfère. Adéquation !

### Et les autres principes de programmation ?

En général, vous pouvez considérer tous les principes de programmation comme YAGNI, DRY, SRP (et d'autres aspects de SOLID), et même les méthodologies de développement logiciel comme AGILE et Waterfall de la même manière. Contextuellement, vous pouvez les utiliser comme des directives pour aider à éviter certains problèmes courants. Mais une personne dotée d'une créativité et d'une expérience suffisantes peut imaginer une situation où le respect de l'un de ces principes crée plus de problèmes qu'il n'en résout.

Dans de nombreux cas, vous devez appliquer ces choses à l'excès pour comprendre ce que signifie \"trop\" en termes pratiques. Veillez simplement à ne pas basculer trop loin dans l'autre direction lorsque l'un de ces principes s'effondre réellement devant vous. J'ai aussi fait cette erreur et j'ai dû me réajuster.

À ce jour, je n'ai pas rencontré de principe de programmation qui soit universellement vrai. Il y en a certains qui s'en approchent, mais je peux toujours imaginer une situation où ils ne sont pas la meilleure approche. Prenez-en un bon comme : \"Écrivez toujours le code le plus simple possible\". En d'autres termes, n'ajoutez pas de complexité supplémentaire sans raison.

Eh bien, supposez que vous ayez un système de valeurs médiocre ou une structure d'incitation qui encourage à gonfler artificiellement votre travail. Dois-je en dire plus ?

## Une note sur les patterns et les architectures

Je vais maintenant aborder le sujet des patterns et des architectures dans les systèmes logiciels sous l'angle de la Loi de l'Adéquation. L'architecture logicielle est la seule chose dans laquelle je me considère comme un expert, et j'ai lu de nombreux ouvrages sur les design patterns. J'essaie toujours de fournir quelques informations utiles sur ces sujets quand j'en ai l'occasion.

### Comment trouver la meilleure architecture logicielle

Pour résumer des articles entiers, des cours et des conférences publiques que j'ai donnés sur ce sujet : la meilleure architecture logicielle dépend du projet et des exigences personnelles.

Une façon de saisir l'idée principale est de se demander si la meilleure architecture pour un hôpital convient également à un appartement de deux chambres. La réponse évidente est que nous pourrions nous attendre à quelques points communs (portes, fenêtres, salles de bains d'un certain type, etc.) entre ces différents ensembles d'exigences. Mais l'architecture idéale, ou même simplement une bonne architecture pour un appartement de deux chambres ne peut pas être la même pour un hôpital.

En bref, vous ne trouverez jamais une architecture qui fonctionne bien pour tous les projets et toutes les exigences.

Voici une liste d'architectures avec lesquelles j'ai une certaine familiarité :

* Model-View-Controller
    
* Model-View-Presenter
    
* Model-View-ViewModel
    
* VIPER
    
* Clean Architecture (style Robert C. Martin)
    
* Model-View-Intent
    

Pour rendre les choses encore plus confuses, il existe plusieurs façons différentes d'implémenter ces architectures – presque autant de façons qu'il y a de développeurs pour les implémenter ! M-V-VM est l'une des architectures les plus courantes dans le développement mobile, et je peux penser à au moins cinq variations différentes sur la manière de réaliser ce que certains considèrent comme une architecture unique.

Voici mes suggestions générales pour travailler avec ces architectures :

* Méfiez-vous de l'ajout d'une complexité inutile avec les architectures plus complexes (particulièrement la Clean Architecture, car beaucoup de gens se trompent lourdement là-dessus)
    
* N'essayez pas de faire entrer les exigences du projet dans l'architecture – travaillez dans l'autre sens (le meilleur indicateur pour cela est de remarquer que quelque chose que vous essayez d'implémenter est rendu inutilement difficile à cause de l'architecture que vous utilisez)
    
* N'ayez pas peur d'appliquer des approches différentes dans des fonctionnalités différentes de la même application au lieu d'appliquer aveuglément le même pattern juste par souci de cohérence
    

### Le piège des design patterns

L'une des tactiques de chasse à l'engagement les plus courantes que je vois sur les réseaux sociaux consiste à publier des listes de design patterns \"que vous devez connaître\" pour obtenir un emploi ou pour effrayer les programmeurs juniors afin qu'ils achètent votre contenu de basse qualité, copié-collé de chaque pattern.

Ne vous méprenez pas, j'ai adoré étudier les design patterns et j'utilise quelques patterns clés dans la plupart des applications GUI que je construis. Le pattern Observer (alias Publisher-Subscriber ou Pub-Sub) brille vraiment lorsque vous avez besoin de coller ensemble un tas de sources de données asynchrones. J'aime voir des développeurs de bibliothèques me proposer un beau pattern Builder pour travailler avec leurs API. Je pense que comprendre les bases de patterns comme le Bridge ou la Facade peut vous apprendre à cacher des détails derrière des abstractions, ce qui est en fait plus simple que ce que les grands mots effrayants décrivant ces choses laissent paraître.

Mais je passe très peu de temps dans mon travail quotidien à penser en termes de design patterns. Au lieu de cela, je pense toujours aux types d'attitudes et de principes qui donnent naissance à ces patterns :

* Promouvoir un code lâchement couplé (séparer la création et l'utilisation des dépendances et des paramètres, utilisation raisonnable de l'abstraction)
    
* Écrire des classes, des interfaces, des protocoles et des fonctions qui font une seule chose (bien que cette \"seule chose\" puisse être un objectif macroscopique plutôt qu'une opération microscopique)
    
* Éviter la complexité autant que possible (une source courante de cette complexité est l'utilisation excessive des abstractions)
    
* Ne pas prétendre que chaque problème complexe a une solution simple (c'est-à-dire, aussi simple que possible, mais pas plus)
    
* Éviter l'optimisation prématurée
    

Encore une fois, je n'appliquerai ces principes et attitudes que dans la mesure où je trouve qu'ils résolvent plus de problèmes qu'ils n'en créent. Les design patterns, lorsqu'ils sont appliqués de manière trop rigoureuse, peuvent briser nombre de ces principes – particulièrement lorsqu'il s'agit d'éviter la complexité et l'optimisation prématurée.

N'essayez pas de faire entrer les exigences de votre projet dans vos patterns. Réfléchissez plutôt aux patterns qui pourraient convenir aux exigences de votre projet et déviez-en si nécessaire.

## Résumé

Mon but avec cet article était de fournir trois choses :

* Un aperçu pratique du choix d'un langage de programmation et de la manière d'éviter les pièges dans lesquels on peut tomber en naviguant dans ce genre de sujets
    
* Un cadre philosophique mais pragmatique que vous pouvez utiliser pour évaluer l'adéquation de n'importe quoi – avec un accent sur l'apprentissage et le développement de logiciels
    
* Une décomposition de la manière dont j'aborde d'autres sujets comme les outils, les architectures et les patterns
    

Bien qu'il puisse être important de prendre en compte des choses comme les opportunités d'emploi et votre matériel actuel, ne négligez pas l'intérêt personnel comme facteur moteur. D'après le peu de souvenirs que j'ai de l'étude de la cognition (apprendre comment apprendre), l'intérêt est étroitement lié à la motivation et à la mémoire. Nous ne pouvons pas toujours faire exclusivement ce qui nous intéresse, mais je vous suggère de chercher des intersections entre préoccupations personnelles et pratiques aussi souvent que vous le pouvez.

En conclusion, je vous encourage à réfléchir à d'autres domaines où vous pourriez explorer les principes d'adéquation et les problèmes de la pensée tribaliste. Le changement est constant et la valeur est relative.