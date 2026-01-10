---
title: 'Swift vs. Objective-C : Le nouveau venu en vogue contre le dinosaure'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T22:10:07.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-colin-gabriel-smith-swift-vs-objective-c-5b19add8e2ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2WOnhJVoWvnNt6HitAQVNg.png
tags:
- name: Apple
  slug: apple
- name: Objective C
  slug: objective-c
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: 'Swift vs. Objective-C : Le nouveau venu en vogue contre le dinosaure'
seo_desc: 'By Colin Smith

  A short history of Swift

  I remember how pivotal it was when Swift was introduced at Apple’s 2014 WWDC (Worldwide
  Developers Conference). It was the talk of the town and all the devs I worked with
  couldn’t wait to try it out. The iOS co...'
---

Par Colin Smith

### Une brève histoire de Swift

Je me souviens à quel point c'était décisif lorsque Swift a été introduit lors de la WWDC 2014 d'Apple (Worldwide Developers Conference). C'était le sujet du moment et tous les développeurs avec lesquels je travaillais ne pouvaient pas attendre pour l'essayer. La communauté iOS était en effervescence et il y avait beaucoup d'excitation autour de ce nouveau langage.

Il a été développé afin de perpétuer certains concepts que nous avons vus en Objective-C, comme la programmation extensible. Mais il a poussé vers une approche différente de la programmation avec la conception orientée protocole et une sécurité accrue avec la typage statique.

Ce fut un énorme succès et sa croissance a explosé dans les années qui ont suivi son introduction. Il était le langage de programmation [le plus aimé](https://insights.stackoverflow.com/survey/2015#tech) en 2015, le [deuxième plus aimé](https://insights.stackoverflow.com/survey/2016#technology) en 2016, le 11e langage de programmation [le plus populaire](https://insights.stackoverflow.com/survey/2017#technology) en 2017, devançant Objective-C, et il a également [devançant](https://insights.stackoverflow.com/survey/2018/#technology) Objective-C en 2018.

Swift est également un pari d'Apple pour [attirer les novices](https://www.businessinsider.com/apple-tim-cook-on-swift-2017-2) afin qu'ils deviennent développeurs iOS. L'espoir est que les nouveaux développeurs apprennent le langage et l'utilisent pour créer des applications iOS. Cela augmente alors l'écosystème de l'App Store. Puisque Swift est optimisé pour fonctionner avec les applications iOS, cela garantit que les applications écrites sont de haute qualité.

La popularité de Swift ne cesse de croître, surtout pour les petites applications et les start-ups. L'écart entre Swift et Objective-C ne fera que continuer à se creuser. L'avenir est prometteur pour ce jeune langage.

### Une brève histoire d'Objective-C

Objective-C est un langage de programmation orienté objet qui est un sur-ensemble de C, comme le nom du langage pourrait le révéler. Cela signifie que tout programme C valide sera compilé avec un compilateur Objective-C. Il tire toute sa syntaxe non orientée objet de C et sa syntaxe orientée objet de SmallTalk. Il a été développé en 1984, il a donc eu le temps de mûrir en tant que langage et est beaucoup plus stable que Swift.

La plupart des gens connaissent Objective-C comme le langage utilisé pour développer des applications pour l'iPhone, mais l'histoire va bien plus loin que cela. Je recommande de lire [cet article](https://medium.com/chmcore/a-short-history-of-objective-c-aff9d2bde8dd) pour une analyse plus approfondie.

### Les forces de Swift

Swift a gagné énormément en popularité pour quelques raisons clés. Tout d'abord, il existe de nombreux excellents outils de développement qu'Apple a fournis pour travailler en conjonction avec Swift. L'un de mes préférés est Playground, qui n'est compatible qu'avec Swift. Apple a introduit Playgrounds [en 2016](https://developer.apple.com/videos/play/wwdc2016/408/). Ils ont été introduits comme un moyen d'apprendre à coder, mais je les aimais pour une autre raison.

Le développement mobile a toujours eu plus d'obstacles que le développement web. Vous avez besoin d'un simulateur, vous avez généralement besoin d'un environnement de développement intégré (IDE) propriétaire, et vous devez configurer un projet entier juste pour tester un petit prototype. Dans le cas d'Apple, vous avez également besoin d'un compte développeur. L'avantage de Playgrounds est que vous contournez une partie de cela. Vous avez besoin de Xcode ou de l'application Playgrounds, mais c'est tout. Et vous pouvez commencer à coder et à compiler votre code immédiatement.

Pourtant, un autre énorme avantage de Swift est le fait qu'il est open source. Si vous vous êtes déjà demandé comment fonctionnait un langage de programmation sous le capot, alors vous pouvez [aller voir par vous-même](https://github.com/apple/swift)! C'est un excellent moyen de comprendre le langage de programmation que vous utilisez quotidiennement à un niveau plus profond.

Une mention honorable va à un utilitaire disponible uniquement pour Swift, le [Swift Package Manager](https://swift.org/package-manager/). Le Swift Package Manager est simplement un [gestionnaire de dépendances](https://devopedia.org/dependency-manager) qui est intégré au système de construction Swift. Ce n'est pas un changement de jeu en soi, puisque CocoaPods et Carthage faisaient ce travail depuis longtemps, mais c'est une autre solution disponible si nécessaire.

De nombreuses preuves ici soutiennent le fait qu'Apple fait beaucoup pour rendre Swift plus désirable en tant que langage de programmation de choix pour les développeurs iOS. Ils créent de beaux utilitaires et auxiliaires pour inciter les gens à commencer à utiliser le langage. Cela montre qu'Apple pousse pour Swift en pleine force.

### Fonctionnalités du langage

Plongeons dans certains détails du langage lui-même. Swift est plus sûr grâce à son typage statique et à l'utilisation des optionnels. En Swift, si votre code nécessite une chaîne, les fonctionnalités de Swift garantiront que votre code obtient une chaîne et non un autre type, comme un int. Cela dépend bien sûr de si vous utilisez le langage comme prévu et ne forcez pas le déballage de tout.

Une autre grande caractéristique de Swift est sa syntaxe. Surtout comparée à celle d'Objective-C. Le meilleur mot pour décrire la syntaxe serait "succinct". Il n'y a pas besoin de points-virgules, d'appels à self ou de parenthèses autour des instructions if. On a l'impression de sauter beaucoup de choses dont on n'a pas vraiment besoin de toute façon. Cela peut rendre le processus de saisie de beaucoup de code plus "fluide".

Certaines personnes disent que cela conduit à des améliorations de la vitesse de développement, mais je ne dirais pas exactement cela moi-même. Le besoin continu de déballer les objets pour se conformer à la sécurité des types de Swift compense les gains de développement qui viennent avec la concision.

Swift dispose également de nombreuses options de contrôle de flux avec guard, if-let, des instructions switch avancées, repeat-while et defer. J'aime toutes les différentes options car elles permettent aux gens de contrôler le flux de leur code de manière à ce qu'elle ait du sens pour eux. Beaucoup de gens détestent les defers mais adorent les guards et vice versa. Cela n'a pas vraiment d'importance ce que vous aimez ou n'aimez pas, mais les options sont là et vous pouvez coder de la manière qui vous semble la meilleure.

Je ne peux pas oublier toutes les fonctionnalités de programmation fonctionnelle telles que filter, map et reduce. C'est génial pour manipuler les collections et cela s'avère utile assez souvent.

### Les faiblesses

Swift est un jeune langage, et avec cela, vient quelques changements. Les migrations entre les versions sont simplement une douleur. Dans une petite entreprise, l'outil de migration fourni par Apple peut être utile et couvrir la plupart des cas. Il devient moins utile plus vous avez de code. C'est encore pire si votre base de code contient à la fois du code Objective-C et Swift qui interopèrent.

Dans ma dernière entreprise, l'effort de migration a pris un groupe dédié tout un week-end pour le faire. Ils ont dû le faire le week-end pour ne pas rencontrer de conflits de fusion avec d'autres développeurs poussant du code. Cela a été incroyablement douloureux pour tout le monde impliqué.

Une raison de ces migrations est le fait que Swift [n'est pas stable ABI](https://theswiftdev.com/2018/11/06/swift-5-and-abi-stability/). Cela signifie que les nouvelles versions de Swift ne peuvent pas fonctionner avec les anciennes versions de Swift. Cela signifie également que le langage ne peut pas être intégré avec le système d'exploitation. C'est un gros problème pour les entreprises avec de grandes applications qui combattent activement la taille des applications car Swift est intégré avec l'application et augmente la taille.

Un autre problème est que Swift ne fonctionne pas bien avec Xcode. Xcode semble très saccadé lors de l'utilisation de Swift et l'autocomplétion [ne fonctionne simplement pas](https://www.reddit.com/r/iOSProgramming/comments/8o1kbt/help_with_xcode_autocomplete_does_not_work/) parfois. C'est étrange étant donné à quel point Apple pousse Swift. On pourrait penser qu'ils voudraient rendre l'expérience d'utilisation de Swift avec Xcode agréable.

Swift a également des problèmes avec la gestion des chaînes, voir l'exemple de code ci-dessus. C'est très lourd. Dans votre quotidien, ce n'est pas trop grave. Là où cela entre le plus en jeu, c'est pendant les entretiens. Malheureusement pour les développeurs Swift, les intervieweurs adorent poser des questions qui impliquent la manipulation de chaînes. Cela est aggravé par le fait que la manière dont les chaînes sont gérées a changé entre les versions de Swift.

### Les forces d'Objective-C

Objective-C est un langage orienté objet hautement dynamique. Il est dynamique au point que vous pouvez échanger des invocations de méthodes à l'exécution en utilisant des techniques comme le [Swizzling](https://nshipster.com/method-swizzling/). Il est capable de faire ce genre de choses grâce à son paradigme d'envoi de messages. Cela permet aux objets d'envoyer des messages à d'autres objets à l'exécution pour déterminer l'invocation de la méthode appelée.

En pratique, que signifie cela ? Eh bien, un grand avantage est l'adaptabilité à l'exécution. Cela signifie que l'accès aux API privées ou la simulation d'objets à l'exécution deviennent possibles. Cela peut être particulièrement utile lorsqu'il s'agit de tests unitaires. Des bibliothèques comme [OCMock](http://ocmock.org/swift/) rendent cela encore plus facile et permettent des configurations de test très élaborées. Avoir de bons tests unitaires rendra votre application plus stable et fiable.

En parlant de stabilité, Objective-C existe depuis longtemps, ce qui en fait un langage très stable. Avec Swift, vous rencontrerez des bugs qui sont [assez surprenants](https://github.com/apple/swift/pull/21727) et qui pourraient perturber la stabilité de votre application. Dans l'exemple que j'ai lié ci-dessus, ce plantage serait causé par le langage lui-même que vous utilisez pour coder votre application, et non par une erreur créée par le code que vous avez écrit. Cela peut être frustrant.

Le dernier point, qui est plus important pour certaines entreprises, est la compatibilité avec les bibliothèques C et C++. Étant donné qu'Objective-C est un sur-ensemble de C, il est facile d'utiliser du code C et C++ avec Objective-C. Vous pouvez même utiliser Objective-C++ si vous en avez envie. Cela est important si vous dépendez de bibliothèques tierces C et C++.

### Les faiblesses

La première plainte principale que j'entends à propos d'Objective-C est la syntaxe. J'ai commencé ma carrière professionnelle en utilisant Objective-C, donc je n'ai aucun problème avec cela. Il est verbeux et un peu inhabituel avec l'utilisation de crochets. Mais les opinions sur la syntaxe ne sont que cela, des opinions. J'ai pensé que je devrais lister ce point cependant, car c'est l'une des premières choses qui vient à l'esprit lorsque vous mentionnez Objective-C.

Une chose avec laquelle je suis d'accord, cependant, est que la syntaxe des blocs est frustrante. [Il y a même un site web](http://goshdarnblocksyntax.com/) dédié au décodage des mystères des blocs en Objective-C. J'utilise en fait ce site web assez souvent comme référence.

Le plus gros problème auquel Objective-C est confronté en ce moment est le fait qu'un jour, Apple pourrait abandonner le support d'Objective-C avec Cocoa et d'autres bibliothèques courantes utilisées pour créer des applications iOS. Puisque Objective-C est principalement utilisé pour créer des applications iOS, ce serait un glas pour le langage. Cela signifie également que les nouveaux venus dans la communauté iOS ont peur de s'engager à apprendre Objective-C maintenant, car il pourrait ne plus être utilisé à l'avenir.

Revenons au langage lui-même. Il est sujet à des problèmes difficiles à déboguer en raison de la nature dynamique du langage. La capacité d'envoyer des messages à nil et de ne pas planter, en plus de l'absence de typage strict, sont quelques exemples de choses qui conduisent à ces problèmes difficiles à déboguer.

Objective-C ne vous tient pas la main en ce qui concerne ces choses non plus. Bien qu'il soit agréable que l'application ne plante pas lorsque vous envoyez un message à nil, cela peut mettre votre application dans un état étrange. Il est très difficile de déboguer ce genre de problèmes. Le fait que Swift ait un typage strict et l'utilisation du déballage des optionnels empêche ces choses au moment de la compilation.

### Dois-je apprendre Swift ou Objective-C ?

La réponse pour la plupart des gens sera Swift. Apple pousse clairement Swift comme le langage de choix pour sa communauté de développement d'applications iOS. Swift ne fera que continuer à devenir plus performant à mesure que la stabilité ABI sera introduite et que Swift sera intégré avec le système d'exploitation lui-même.

Si vous cherchez à obtenir un emploi en tant que développeur iOS, Swift sera le langage que vous voudrez apprendre. La plupart des start-ups aux entreprises de taille moyenne auront leurs applications iOS écrites entièrement en Swift. Cela signifie que vous pourrez postuler et passer des entretiens pour plus d'emplois si vous apprenez Swift.

Même dans les grandes entreprises où Objective-C est encore largement utilisé, les entretiens peuvent encore être réalisés en Swift. Vous pouvez donc apprendre Objective-C une fois que vous avez rejoint l'entreprise et ne pas vous soucier de vous charger de plus de choses à apprendre avant l'entretien.

Vous voudrez apprendre Objective-C si vous travaillez déjà dans une start-up ou une entreprise de taille moyenne et souhaitez passer à une plus grande entreprise. Les compétences en Objective-C vous donneront des connaissances spécialisées et un avantage sur les autres candidats à l'entretien.

_Aimé ce que vous avez lu ? Jetez un coup d'œil à certains de mes autres articles :_

[Conseils pour votre premier entretien technique.](https://medium.com/@colin.gabriel.smith/killing-it-during-your-first-tech-interview-16ce13f9d0ce)

[Démarrer une carrière technologique à partir de rien.](https://medium.freecodecamp.org/how-i-went-from-stuck-and-hopeless-to-making-my-tech-career-dreams-come-true-d1fcf52c0650)

[Devez-vous obtenir un diplôme en informatique ?](https://link.medium.com/rCnf6bajBT)