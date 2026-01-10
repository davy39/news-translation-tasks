---
title: Apprendre l'informatique par soi-même – Concepts clés en informatique que vous
  devriez connaître
subtitle: ''
author: Tamerlan Gudabayev
co_authors: []
series: null
date: '2023-06-22T22:06:46.000Z'
originalURL: https://freecodecamp.org/news/what-every-software-engineer-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-christina-morillo-1181298--2-.jpg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: fundamentals
  slug: fundamentals
- name: software architecture
  slug: software-architecture
seo_title: Apprendre l'informatique par soi-même – Concepts clés en informatique que
  vous devriez connaître
seo_desc: 'Software development may feel like a bit of a race to keep up with new
  technologies.

  There''s always a new frontend framework to learn, or a new database or language
  that''s a variation of another language. It''s never ending and feels like you always
  h...'
---

Le développement logiciel peut sembler une course pour suivre les nouvelles technologies.

Il y a toujours un nouveau framework frontend à apprendre, ou une nouvelle base de données ou un langage qui est une variation d'un autre langage. C'est sans fin et on a l'impression de devoir toujours suivre.

Mais cela n'a pas à être ainsi.

## Tout est construit à partir des fondamentaux

Si vous apprenez les fondamentaux, alors tout le reste deviendra plus facile.

Par exemple, si vous [apprenez comment fonctionne le protocole TCP/IP](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/), alors à partir de cela, vous pourrez facilement apprendre tous les autres protocoles qui sont construits par-dessus.

Vous avez essentiellement moins de terrain à couvrir. Plus vous connaissez de fondamentaux, moins vous aurez de mal à apprendre de nouvelles choses.

Je crois qu'il y a 10 sujets principaux qui, si vous les apprenez, vous donneront une base solide.

## Pourquoi devriez-vous apprendre ces concepts clés ?

Apprendre les fondamentaux vous placera vraiment dans le top 5 % de tous les programmeurs.

Si nous regardons cela sous un angle différent, voici une excellente citation de Ras Bodik.

> Ne soyez pas un programmeur de code standard. Au lieu de cela, construisez des outils pour les utilisateurs et d'autres programmeurs. Prenez note historique des industries du textile et de l'acier : voulez-vous construire des machines et des outils, ou voulez-vous faire fonctionner ces machines ?

## Mais il y a un million de cours différents parmi lesquels choisir

Eh bien, ne cherchez pas plus loin.

Ci-dessous, j'ai compilé un ensemble de ressources utiles sur chaque sujet – avec quelques alternatives, bien sûr. Ainsi, vous pouvez vous concentrer sur l'apprentissage et non sur la recherche aveugle des meilleurs livres/vidéos/cours.

### Quelques notes

Cet article est bien adapté pour les développeurs autodidactes ou les développeurs qui ne se sentent pas tout à fait à l'aise avec certains concepts d'informatique.

Si vous apprenez à programmer pour la première fois, je vous recommande la communauté [r/learnprogramming](https://www.reddit.com/r/learnprogramming/) sur Reddit.

Cet article a été fortement inspiré par [Oz Nova](https://twitter.com/oznova_) et [Myles Byrne](https://twitter.com/quackingduck) qui ont créé le site [teachyourselfcs.com](https://teachyourselfcs.com/). Si vous aimez cet article, n'hésitez pas à consulter et partager leur site.

## Table des matières

* [Programmation](#heading-programmation)
* [Architecture des ordinateurs](#heading-architecture-des-ordinateurs)
* [Algorithmes et structures de données](#algorithmes-et-structures-de-donnees)
* [Mathématiques pour l'informatique](#heading-maths-pour-linformatique)
* [Systèmes d'exploitation](#heading-systemes-dexploitation)
* [Réseaux informatiques](#heading-reseaux-informatiques)
* [Bases de données](#heading-bases-de-donnees)
* [Langages et compilateurs](#langages-et-compilateurs)
* [Systèmes distribués](#heading-systemes-distribues)
* [Sécurité Web](https://www.freecodecamp.org/news/p/dfc9104e-85e4-4749-88dc-1859e6c643b9/web-security)
* [Conclusion](https://www.freecodecamp.org/news/p/dfc9104e-85e4-4749-88dc-1859e6c643b9/conclusion)

## Programmation

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-84.png)
_[Source](https://dabeaz.com/sicp.html)_

Je ne parle pas de syntaxe ici. Mais vraiment de programmation ou de résolution de problèmes. Des choses comme l'abstraction, les fonctions en tant que données, la récursion, et les différents types de paradigmes de programmation (orienté objet, fonctionnel et déclaratif).

Le livre que je recommande pour apprendre la programmation est [Structures et Interprétations des Programmes Informatiques](https://sarabander.github.io/sicp/html/index.xhtml) (SICP) (Il est également connu sous le nom de livre du sorcier).

Le livre est gratuit et dispose d'un ensemble de [conférences MIT](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/). Mais les conférences MIT sont un peu difficiles à regarder en raison de la mauvaise qualité de l'époque (2005). Je recommande donc les [conférences SICP de Brian Harvey](https://archive.org/details/ucberkeley-webcast-PL3E89002AA9B9879E?sort=titleSorter) (pour le cours 61A à Berkeley) à la place.

### Pourquoi ce livre ?

Parce que ce livre se concentre sur le tableau d'ensemble.

Il ne se soucie pas du langage de programmation. Il utilise une variation de Lisp appelée Scheme. Scheme est très facile à apprendre (vous pouvez probablement l'apprendre en moins d'une heure), donc il vous permet de vous concentrer sur les idées et non sur la syntaxe.

Grâce à sa simplicité, il est possible d'examiner différents paradigmes de programmation. C'est une approche fonctionnelle en premier, mais vous pouvez implémenter votre propre OOP.

Scheme est un excellent langage pour l'enseignement car il éloigne l'attention du langage et la met sur les grandes idées.

Si vous êtes inquiet qu'il ne soit pas utilisé dans l'industrie, ce n'est pas grave – vous pouvez toujours apprendre un langage de programmation plus couramment utilisé après avoir saisi ces concepts de haut niveau.

### Mais que faire si je ne veux vraiment pas apprendre Scheme ?

D'accord, vous pouvez suivre la nouvelle version du livre qui utilise Python. Le livre s'intitule [Composing Programs](http://composingprograms.com/). Il dispose également de son propre [ensemble de conférences](https://cs61a.org/).

Mais je recommande fortement d'essayer au moins la version Scheme. C'est magique une fois que vous l'avez compris.

### D'accord, je l'ai essayé mais c'est vraiment difficile

Oui, je comprends.

Certains d'entre vous trouveront SICP un peu trop difficile. Il n'est pas destiné aux programmeurs purement débutants.

Si c'est le cas, alors je recommande [How to Design Programs (HTDP)](https://htdp.org/). Il utilise un langage très similaire à Scheme et est généralement plus lent. Vous pouvez utiliser ce livre et son [cours sur edX](https://www.edx.org/course/how-to-code-simple-data).

### Conseils pour l'étude

Ne lisez pas ces livres comme une histoire.

Ils ne sont pas destinés à être lus de couverture à couverture. Au lieu de cela, **concentrez-vous sur les exercices**. Vous n'avez pas à tous les faire, mais assurez-vous simplement de savoir comment résoudre la plupart d'entre eux.

Les conférences sont facultatives et ne sont nécessaires que si elles aident. C'est vraiment à vous de voir.

### Ressources supplémentaires

* [Rencontres virtuelles qui parlent de SICP](https://www.youtube.com/playlist?list=PLVFrD1dmDdvdvWFK8brOVNL7bKHpE-9w0)
* [Racket](#https://racket-lang.org/) (IDE pour Scheme) ([Consultez cette réponse StackOverFlow pour la configuration de Scheme](https://stackoverflow.com/a/25096066))

## Architecture des ordinateurs

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-128.png)
_[Source](https://github.com/ahmeducf/computer-systems-CS-APP3e)_

Vous avez écrit du code et il s'exécute magiquement.

Comment cela fonctionne-t-il ? Eh bien, c'est ce que vous apprendrez avec l'architecture des ordinateurs. C'est de loin le sujet le plus négligé par la plupart des ingénieurs autodidactes.

En tant qu'ingénieurs, nous ne croyons pas à la magie. Nous devons démystifier la magie derrière les ordinateurs. Vous apprendrez également des choses utiles comme :

* Qu'est-ce que le cache L1, L2 ?
* Pourquoi Cyberpunk lag ?

Le livre que je recommande ici est _[Computer Systems: A Programmer's Perspective](http://csapp.cs.cmu.edu/3e/home.html)_. Je recommande également un [cours d'introduction](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f16/www/schedule.html) qui couvrira les chapitres 1-6 du livre (qui a été réalisé par les auteurs du livre).

### Mais il y a un piège

**Ce livre n'est pas destiné à être lu de couverture à couverture**. Il contient beaucoup de contenu, qui peut ne pas être présenté dans l'ordre optimal.

Je recommande donc de suivre le cours et de faire les travaux pratiques.

### Que faire si je trouve cela trop difficile ?

Beaucoup de gens trouveront le contenu un peu lourd, donc pour vous y habituer, je recommande de faire ce qui suit :

* Lire [Code: The Hidden Language of Computer Hardware and Software](https://www.amazon.com/Code-Language-Computer-Hardware-Software/dp/0735611319)
* [Lire ce manuel sur l'architecture logicielle](https://www.freecodecamp.org/news/an-introduction-to-software-architecture-patterns/)
* Regarder les 4 vidéos de [Exploring How Computers Work](https://www.youtube.com/playlist?list=PLFt_AvWsXl0dPhqVsKt1Ni_46ARyiCGSq)
* Regarder les 41 vidéos de [Crash Course: Computer Science](https://www.youtube.com/playlist?list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye)
* Suivre le cours [NAnd2Tetris](https://www.coursera.org/learn/build-a-computer)
* Apprendre un peu de C en lisant le livre : [C Programming a Modern Approach](https://www.amazon.com/C-Programming-Modern-Approach-2nd/dp/0393979504)

Une fois que vous avez terminé cela, vous pouvez revenir à Computer Systems: A Programmers Perspective.

## Algorithmes et structures de données

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-131.png)
_[Source](https://twitter.com/StevenSkiena/status/1336050368875290629)_

Tout le monde veut travailler dans une entreprise FAANG, mais personne ne veut apprendre les algorithmes et les structures de données.

Néanmoins, je ne veux pas que vous appreniez cela juste à cause des entretiens techniques. Les algorithmes et les structures de données sont importants car ils aident à développer vos compétences en résolution de problèmes.

Il existe de nombreux excellents livres et cours sur les algorithmes et les structures de données, mais celui que je recommande est un livre intitulé _[The Algorithm Design Manual](https://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202)_ par Steven Skiena. Vous pouvez également consulter son cours [ici](https://www3.cs.stonybrook.edu/~skiena/373/videos/).

### N'oubliez pas de pratiquer

Les mêmes règles s'appliquent ici. Ne vous contentez pas d'apprendre les structures de données, mais créez-les dans le langage que vous voulez. Ne mémorisez pas simplement les algorithmes, mais implémentez-les et voyez où et comment vous pouvez les utiliser.

Un bon conseil est de résoudre quelques problèmes [Leetcode](https://leetcode.com/) tout en suivant le livre/cours.

### Que faire si je trouve cela trop difficile ?

Si vous trouvez le matériel un peu lourd, alors je recommande les ressources suivantes :

* Lire le livre : [Grokking Algorithms](https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230)
* Lire le livre : [How to Solve It: A New Aspect of Mathematical Method](https://www.amazon.com/How-Solve-Mathematical-Princeton-Science/dp/069111966X#:~:text=Polya%2C%20How%20to%20Solve%20It,winning%20a%20game%20of%20anagrams.)

En général, il existe de nombreux livres/cours différents qui enseignent les algorithmes et les structures de données – voici quelques autres excellentes ressources :

* [Cours sur les algorithmes et les structures de données sur freeCodeCamp](https://www.freecodecamp.org/news/algorithms-and-data-structures-free-treehouse-course/)
* [Algorithms Illuminated](https://algorithmsilluminated.org/)
* [Cours d'algorithmes de Princeton](https://www.coursera.org/learn/algorithms-part1)
* [Cours sur les algorithmes et les structures de données de ThePrimegeans](https://frontendmasters.com/courses/algorithms/)
* [Introduction aux algorithmes du MIT](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)

## Mathématiques pour l'informatique

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-144.png)
_Ne vous inquiétez pas, c'est une photo aléatoire de mathématiques trouvée [ici](https://unsplash.com/photos/h3kuhYUCE9A)_

De nombreux nouveaux développeurs sautent cette étape.

Mais, écoutez-moi – l'informatique est essentiellement une branche des mathématiques. L'apprendre vous rendra meilleur développeur en aiguisant vos compétences en résolution de problèmes.

### Le domaine le plus pertinent pour l'informatique est les mathématiques discrètes

Les mathématiques discrètes sont la branche des mathématiques qui traite des nombres dénombrables ou finis.

Les sujets en mathématiques discrètes sont nombreux, mais ceux qui sont pertinents pour l'informatique sont :

* Logique
* Combinatoire
* Probabilité discrète
* Théorie des ensembles
* Théorie des graphes
* Théorie des nombres

### Comment étudier les mathématiques discrètes

Je suggérerais de commencer par un ensemble de [notes de cours de László Lovász](https://cims.nyu.edu/~regev/teaching/discrete_math_fall_2005/dmbook.pdf).

Les notes du professeur Lovász sont plus faciles à digérer que les textes formels et sont généralement amusantes. Il commence par un problème et le résout en utilisant les mathématiques discrètes.

Après cela, vous pouvez prendre un livre du MIT intitulé _[Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring17/mcs.pdf)_. Le livre est accompagné de conférences vidéo qui sont [librement disponibles](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/video_galleries/video-lectures/).

### Que faire si c'est trop difficile ?

Ne vous inquiétez pas – parfois, vous devez simplement accepter que **vous ne comprendrez pas toujours tout de suite**.

C'est normal.

Mais si vous avez l'impression de manquer certaines connaissances fondamentales, alors c'est une autre histoire. Les sujets préalables fondamentaux pour les mathématiques discrètes sont :

* Algèbre
* Géométrie
* Calcul

Il existe de nombreuses ressources gratuites, mais celles que je recommande sont :

* [Khan Academy](https://www.khanacademy.org/)
* [Cours d'algèbre universitaire](https://www.freecodecamp.org/news/college-algebra-course-with-python-code/)
* [Cours de Calcul 1](https://www.freecodecamp.org/news/learn-college-calculus-in-free-course/)
* [Cours de Calcul 2](https://www.freecodecamp.org/news/learn-calculus-2-in-this-free-7-hour-course/)

## Systèmes d'exploitation

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-228.png)
_[Source](https://pages.cs.wisc.edu/~remzi/OSTEP/)_

Vous souvenez-vous quand je vous ai dit que nous, en tant que développeurs, voulons éliminer la magie de l'informatique ?

La même chose s'applique ici – les systèmes d'exploitation semblent être une sorte de boîte noire magique. Mais ils ne le sont pas – c'est juste beaucoup d'ingénierie astucieuse.

Si vous savez comment ces systèmes d'exploitation sont construits et fonctionnent, alors vous serez définitivement dans une ligue à part.

Il est quelque peu difficile de trouver de bonnes ressources en ligne pour les systèmes d'exploitation, mais le livre le plus recommandé est [Operating Systems: Three Easy Pieces (OSTEP).](https://pages.cs.wisc.edu/~remzi/OSTEP/) Il n'y a pas de conférence vidéo officielle en ligne qui couvre entièrement le livre, mais j'ai trouvé cette [playlist sur YouTube](https://www.youtube.com/playlist?list=PLhtZD20ADU45ADsAIxlNpFowP3iYvGXvJ).

### Prérequis recommandés

Je suggérerais d'apprendre d'abord l'architecture des ordinateurs et un peu de C avant de se lancer dans l'aventure des systèmes d'exploitation.

### Ressources facultatives

Maintenant, je recommande de terminer OSTEP en premier, puis de consulter les autres ressources recommandées. Elles sont toutes facultatives.

* Vous voulez construire votre propre système Linux ? Consultez [Linux from Scratch](https://www.linuxfromscratch.org/).
* Vous voulez une vue d'ensemble approfondie de Linux, MacOS et Windows ? [Voici un manuel pour vous](https://www.freecodecamp.org/news/an-introduction-to-operating-systems/).
* Vous voulez construire votre propre système d'exploitation ? Consultez [OSDEV](https://wiki.osdev.org/Introduction)
* Vous voulez construire vos propres sockets ? Consultez [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)

## Réseaux informatiques

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-237.png)
_[Source](https://github.com/topics/top-down-approach)_

Depuis l'avènement de l'internet, les réseaux informatiques ont été l'un des sujets les plus importants pour les ingénieurs logiciels.

Si vous ne connaissez pas des choses comme IP, TCP, UDP, HTTP, TLS, DNS, SMTP, et ainsi de suite – alors vous devriez apprendre les réseaux informatiques (surtout si vous êtes un ingénieur backend).

Le livre recommandé ici est [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/wireshark.php). Vous pouvez également consulter les [conférences vidéo](https://www.youtube.com/playlist?list=PLByK_3hwzY3Tysh-SY9MKZhMm9wIfNOas) de l'auteur du livre lui-même.

Mais avant de commencer cela, je recommande de consulter ce [cours accéléré vidéo sur les réseaux informatiques](https://www.youtube.com/playlist?list=PLowKtXNTBypH19whXTVoG3oKSuOcw_XeW) depuis une approche ascendante. Et [voici un tutoriel utile](https://www.freecodecamp.org/news/computer-networking-how-applications-talk-over-the-internet/) qui couvre bien les bases.

## Bases de données

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-229.png)
_[Source](https://www.astera.com/type/blog/a-quick-overview-of-different-types-of-databases/)_

Les bases de données sont quelque peu nouvelles – elles sont apparues dans les années 1970 et sont depuis devenues des parties intégrantes de nombreuses applications.

Je recommande vivement les cours ci-dessous du [CMU Database Group](https://www.youtube.com/@CMUDatabaseGroup/featured). Ils sont tous librement disponibles sur YouTube. Je recommande de suivre au moins le premier.

1. [Introduction aux bases de données](https://www.youtube.com/playlist?list=PLSE8ODhjZXjaKScG3l0nuOiDTTqpfnWFf)
2. [Séminaires sur les bases de données](https://www.youtube.com/playlist?list=PLSE8ODhjZXjZKp-oX_75aBnznulk7nubu)
3. [Bases de données avancées](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYzlLMbX3cR0sxWnRM7CLFn)

De plus, [voici une excellente collection de ressources](https://www.freecodecamp.org/news/learn-sql-free-relational-database-courses-for-beginners/) pour vous aider à apprendre les bases de données SQL. Et [voici un cours gratuit sur les bases de données NoSQL](https://www.freecodecamp.org/news/learn-nosql-in-3-hours/).

## Langages et compilateurs

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-230.png)
_[Source](https://chidiwilliams.com/post/crafting-interpreters-a-review/)_

Vous savez peut-être coder dans un ou plusieurs langages de programmation.

Mais savez-vous comment en créer ou en concevoir un ? C'est ce que vous apprendrez en étudiant les langages de programmation et les compilateurs.

Le livre d'introduction recommandé s'intitule [Crafting Interpreters](https://craftinginterpreters.com/contents.html).

Après cela, vous pouvez passer à _[Compilers: Principles, Techniques & Tools](https://smile.amazon.com/Compilers-Principles-Techniques-Tools-2nd/dp/0321486811)_, également appelé "le livre du Dragon". Le livre couvre de nombreux sujets, je recommande donc vivement de suivre un cours avec lui. Celui que je recommande est de [Alex Aiken sur edX](https://www.edx.org/course/compilers).

Et [voici un tutoriel utile pour débutants](https://www.freecodecamp.org/news/what-is-a-compiler-in-c/) sur le fonctionnement du compilateur en programmation C.

## Systèmes distribués

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-231.png)
_[Source](https://vvsevolodovich.dev/designing-data-intensive-applications-by-martin-kleppmann/)_

Si vous choisissez d'étudier un seul sujet de la liste, faites-en les systèmes distribués. C'est le graal pour les entreprises technologiques, et si vous voulez obtenir un emploi de développeur, vous devriez maîtriser les systèmes distribués.

Mon parcours recommandé pour apprendre le sujet est :

1. Lire le livre : [Understanding Distributed Systems](https://www.amazon.com/gp/product/1838430202/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=utsavized0d-20&creative=9325&linkCode=as2&creativeASIN=1838430202&linkId=8f3007bbed9b958980492f5c0bb1105f)
2. Lire le livre : [Designing Data Intensive Applications](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321) également connu sous le nom de "livre rouge"
3. Pendant la lecture du "livre rouge", suivez son cours d'accompagnement [MIT sur YouTube](https://www.youtube.com/@6.824/videos).
4. Lire le livre : [Software Architecture: The Hard Parts](https://www.amazon.com/dp/1492086894?psc=1&linkCode=sl1&tag=utsavized0d-20&linkId=64e15d236bb8c1015661423e5be849ac&language=en_US&ref_=as_li_ss_tl) (Facultatif)
5. Vous pouvez également [consulter mon manuel sur les modèles de conception pour les systèmes distribués](https://www.freecodecamp.org/news/design-patterns-for-distributed-systems/).

## Sécurité Web

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-232.png)
_[Source](https://www.ifourtechnolab.com/blog/principles-of-web-security)_

Il y a eu beaucoup de violations de sécurité au cours des 2-3 dernières années.

C'est devenu dangereux – et en tant qu'ingénieur logiciel, connaître quelques fondamentaux de la sécurité web vous donnera un avantage.

Le cours que je recommande en premier est [CS253 Web Security by Stanford](https://web.stanford.edu/class/cs253/). Il donne un aperçu complet de la sécurité web. Attendez-vous donc à des sujets comme les vulnérabilités des applications web, l'injection, le déni de service, et bien d'autres.

Vous pouvez également [passer en revue ces vulnérabilités courantes](https://www.freecodecamp.org/news/technical-dive-into-owasp/) et apprendre à prévenir les attaques qui en tirent parti.

Plus tard, si vous le souhaitez, vous pourriez apprendre à pirater en utilisant [pwn.college](https://pwn.college/).

## Conclusion

Apprendre tous ces sujets vous prendra un certain temps et nécessitera un effort constant. Mais si vous aimez ce que vous faites et que vous êtes intéressé par le sujet, cela devrait sembler un jeu et non une corvée.

Quels que soient les sujets que vous choisissez d'étudier. Le conseil le plus important que je puisse vous donner est...

### Ne soyez pas un apprenant passif

Ne vous contentez pas de regarder des vidéos – faites également les exercices. Construisez les projets avec les tutoriels.

Ne vous contentez pas de lire des livres, mais engagez-vous dans le livre en posant des questions et en faisant vos propres recherches.

Vous voulez que l'information reste, pour ne pas l'oublier. Et pour la faire rester, vous devez vous engager activement dans le sujet.

J'espère sincèrement vous avoir encouragé à étudier certains de ces sujets. Comme toujours, je veux terminer en vous remerciant d'avoir lu cet article.

Je vous souhaite tout le meilleur.