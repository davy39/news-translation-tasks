---
title: Ce que j'ai appris de The Pragmatic Programmer et The Clean Coder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-24T16:38:09.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-from-the-pragmatic-programmer-and-the-clean-coder
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pragmatic_programmer_and_clean_coder_book_covers-1.jpg
tags:
- name: books
  slug: books
- name: clean code
  slug: clean-code
- name: learning
  slug: learning
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
seo_title: Ce que j'ai appris de The Pragmatic Programmer et The Clean Coder
seo_desc: "By Ramón Morcillo\nI recently finished reading The Pragmatic Programmer\
  \ 20th Anniversary Edition (2019) and The Clean Coder (2011). You'll find these\
  \ books on almost every “top 10 Software Development books” list out there. \nMy\
  \ goal was to learn, impr..."
---

Par Ramón Morcillo

J'ai récemment terminé la lecture de _The Pragmatic Programmer 20th Anniversary Edition_ (2019) et _The Clean Coder_ (2011). Vous trouverez ces livres sur presque toutes les listes des "10 meilleurs livres sur le développement logiciel".

Mon objectif était d'apprendre, de m'améliorer et d'acquérir le genre de connaissances qu'un de mes professeurs disait "ne peut pas être obtenu simplement en lisant des articles".

Lorsque vous développez un logiciel, vous pouvez vous retrouver bloqué à un point où les vidéos YouTube et les réponses StackOverflow ne vous aident pas. Vous finissez par consulter la documentation officielle ou le code source de cette technologie pour trouver la réponse.

La même chose se produit lorsque vous voulez comprendre un sujet en profondeur. **Les articles peuvent parfois être insuffisants, et la lecture de livres bien connus est souvent la meilleure approche.**

Ces livres ne se concentrent pas seulement sur la façon d'écrire du code, mais aussi sur l'enseignement des meilleures pratiques pour développer des logiciels et même des leçons de vie utiles. Je vais partager quelques leçons que j'ai apprises dans cet article.

## Table des matières

- Comment prendre ses responsabilités
- L'importance des tests
- Le travail d'équipe fait le rêve
- Comment estimer
- Développement par balles traceuses
- Comment gérer la pression
- L'importance du refactoring
- Principales différences entre ces livres
- Conclusion
- Ressources

## Comment prendre ses responsabilités

En tant que développeur logiciel, vous êtes responsable du code que vous créez. Vous devez vous assurer qu'il fonctionne non seulement maintenant, mais aussi de la meilleure façon possible pendant longtemps (rien ne dure éternellement).

La meilleure façon de s'assurer que le code ne déchouera pas est de le tester - avoir des tests automatisés que vous exécutez chaque fois que vous écrivez de nouvelles lignes pour être sûr que tout fonctionne encore.

> Prenez vos responsabilités. La responsabilité est quelque chose que vous acceptez activement.
> — The Pragmatic Programmer

La responsabilité ne se limite pas au codage. Vous devez **prendre la responsabilité de vous améliorer** et de vous améliorer en planifiant du temps pour cela.

> Les professionnels passent du temps à prendre soin de leur profession. Présumément, vous êtes devenu développeur logiciel parce que vous êtes passionné par le logiciel et votre désir d'être un professionnel est motivé par cette passion.
> — The Clean Coder

> Vos connaissances et votre expérience sont vos actifs professionnels les plus importants au quotidien.
> — The Pragmatic Programmer

![Responsabilité](https://www.freecodecamp.org/news/content/images/2021/11/responsibility.gif)

## L'importance des tests

L'importance des tests dans le développement logiciel est si grande que les deux livres se concentrent sur ce sujet.

Vous devez **considérer les tests comme les premiers utilisateurs de votre code**, ils sont donc le meilleur retour d'information qui guide votre codage.

Pratiquez le [TDD Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development). Comment cela fonctionne-t-il ? Voici ses trois étapes principales :

1. Choisissez une fonctionnalité à ajouter et écrivez un test qui passera après l'avoir implémentée. Maintenant, tous les tests sauf le nouveau doivent passer.
2. Écrivez le code nécessaire pour le faire passer.
3. Refactorisez le code et vérifiez que tous les tests passent toujours.

Cela dit, il est important de voir le tableau d'ensemble et de ne pas manquer l'objectif principal en écrivant trop de tests.

> Il est facile de se laisser séduire par le message vert "tests passés", en écrivant beaucoup de code qui ne vous rapproche pas réellement d'une solution.
> — The Pragmatic Programmer

![Tests](https://www.freecodecamp.org/news/content/images/2021/11/tests.gif)

Il existe trois façons de tester : _First, During,_ et _Never._ First (TDD) est la meilleure. During est un recours lorsque First n'est pas utile. Et Never est souvent appelé "Test Later" mais malheureusement **dans la plupart des cas, Later signifie Never.**

> Le besoin de tester d'abord vous oblige à penser à "good design".
> — The Clean Coder

Avoir des tests vous donne la confiance de refactoriser le code plus souvent car vous pouvez vérifier que les tests passent toujours après avoir fait vos modifications.

> Les tests doivent être exécutés aussi fréquemment que possible pour fournir un retour d'information maximal et pour s'assurer que le système reste continuellement propre.
> — The Clean Coder

Utilisez des tests d'acceptation pour _définir quand une exigence est terminée_ en collaborant avec les parties prenantes.

Les développeurs doivent s'assurer que les tests sont _toujours automatisés_ pour une raison simple : **coût.**

Les développeurs doivent avoir pour objectif que "QA ne trouve rien". Vous pouvez y parvenir en implémentant différents types de tests, dans différentes mesures, des tests unitaires aux tests exploratoires.

![The Test Automation Pyramid - The Clean Coder](https://www.freecodecamp.org/news/content/images/2021/11/the_test_automation_pyramid.png)

## Le travail d'équipe fait le rêve

Lorsque vous travaillez en équipe, vous devez être un "joueur d'équipe", communiquer fréquemment, surveiller vos coéquipiers et exécuter vos responsabilités de la manière la plus efficace possible.

> Une bonne communication est la clé pour éviter ces problèmes. Et par "bonne", nous entendons instantanée et sans friction. Sans friction signifie qu'il est facile et peu cérémonieux de poser des questions, de partager vos progrès, vos problèmes, vos idées et vos apprentissages, et de rester conscient de ce que font vos coéquipiers.
> — The Pragmatic Programmer

![tobias-mrzyk-iuqmGmst5Po-unsplash](https://www.freecodecamp.org/news/content/images/2021/11/tobias-mrzyk-iuqmGmst5Po-unsplash.jpg)

Les équipes doivent être **petites, moins de 10-12 membres**, où tout le monde se connaît et se fait confiance. Cet environnement d'équipe est **difficile à atteindre**, donc une fois que vous l'avez, vous devez **en prendre soin en changeant les projets sur lesquels l'équipe travaille plutôt que les membres.**

> À mesure que la taille de l'équipe augmente, les chemins de communication augmentent au rythme de O(n^2), où n est le nombre de membres de l'équipe. Dans les grandes équipes, la communication commence à se dégrader et devient inefficace.
> — The Pragmatic Programmer

> Former des équipes autour de projets est une approche stupide. Les individus ne sont sur le projet que pour une courte période et n'apprennent donc jamais à traiter les uns avec les autres. Les équipes sont plus difficiles à construire que les projets. Par conséquent, il est préférable de former des équipes persistantes qui se déplacent ensemble d'un projet à l'autre et peuvent prendre en charge plus d'un projet à la fois.
> — The Clean Coder

![tobias-mrzyk-Px3oXvVXRxc-unsplash](https://www.freecodecamp.org/news/content/images/2021/11/tobias-mrzyk-Px3oXvVXRxc-unsplash.jpg)

De plus, les grandes équipes affronteront et résoudront les problèmes ensemble où chaque individu fournira son meilleur effort. Ils _font les choses en tant qu'unité_. À la fin, ils seront connus pour leur performance et la qualité de leur travail.

> La qualité ne peut venir que des contributions individuelles de tous les membres de l'équipe. La qualité est intégrée, pas ajoutée.
> — The Pragmatic Programmer

> Une équipe soudée peut accomplir des miracles, anticiper les uns les autres, se couvrir mutuellement, se soutenir mutuellement et exiger le meilleur les uns des autres. Ils font que les choses se réalisent.
> — The Clean Coder

> Les grandes équipes de projet ont une personnalité distincte. Les gens attendent avec impatience les réunions avec eux, car ils savent qu'ils verront une performance bien préparée qui fait du bien à tout le monde. La documentation qu'ils produisent est concise, précise et cohérente.
> — The Pragmatic Programmer

![natalie-pedigo-wJK9eTiEZHY-unsplash](https://www.freecodecamp.org/news/content/images/2021/11/natalie-pedigo-wJK9eTiEZHY-unsplash.jpg)

## Comment estimer

Cette leçon, comme la majorité des deux livres, est aussi importante dans le développement logiciel que dans la vie réelle. Plus vous pratiquez et la développez, plus votre capacité à déterminer la faisabilité de toute tâche sera intuitive.

Tout d'abord, je veux clarifier ce que signifie _estimer_ en partageant la définition de The Clean Coder qui le décrit comme une _distribution de probabilité_.

> Une estimation n'est pas un nombre. Une estimation est une _distribution de probabilité_, la probabilité d'achèvement.
> — The Clean Coder

Pour vous aider à comprendre, voici une figure de la probabilité d'achèvement d'une tâche pour les 11 prochains jours.

![probability_distribution](https://www.freecodecamp.org/news/content/images/2021/11/probability_distribution.png)

L'une des bases pour faire de grandes estimations est d'**avoir une connaissance appropriée de ce que vous estimez**.

> La première partie de tout exercice d'estimation est de construire une compréhension de ce qui est demandé. Vous devez avoir une idée de l'étendue du domaine.
> — The Pragmatic Programmer

N'estimez pas seul, **communiquez avec d'autres personnes pour être aussi précis que possible**.

> La ressource d'estimation la plus importante que vous avez sont les personnes autour de vous. Elles peuvent voir des choses que vous ne voyez pas. Elles peuvent vous aider à estimer vos tâches plus précisément que vous ne pouvez le faire seul.
> — The Clean Coder

> Un truc d'estimation de base qui donne toujours de bonnes réponses : demandez à quelqu'un qui l'a déjà fait.
> — The Pragmatic Programmer

Lorsque vous êtes demandé pour une estimation, choisissez les unités qui reflètent le mieux la précision que vous souhaitez transmettre. Cette échelle de temps d'estimation de The Pragmatic Programmer peut vous aider.

| Durée      | Estimation en                    |
| ------------- |:------------------------------------:|
| 1–15 jours     | Jours                                 |
| 3–6 semaines   | Semaines                                |
| 8–20 semaines   | Mois                               |
| 20+ semaines   | Réfléchissez bien avant de donner une estimation |

Bien que les entreprises aiment considérer les estimations comme des engagements, rappelez-vous qu'**une estimation n'est qu'une supposition, donc aucun engagement n'est impliqué**.

> Un engagement est quelque chose que vous devez atteindre. Si vous vous engagez à faire quelque chose à une certaine date, alors vous devez simplement le faire à cette date. Les professionnels ne prennent pas d'engagements à moins de savoir qu'ils peuvent les atteindre. Manquer un engagement est un acte de malhonnêteté légèrement moins onéreux qu'un mensonge flagrant.
> — The Clean Coder

Ainsi, pour aider les entreprises à mesurer les exigences et à faire des plans appropriés, vous devez **supprimer l'ambiguïté des exigences avant d'estimer**. Ensuite, **tenez-les informés de la progression**.

> Le truc pour gérer les retards est la détection précoce et la transparence. Mesurez régulièrement vos progrès par rapport à votre objectif. Soyez aussi honnête que possible sur toutes les dates. N'incorporez pas l'espoir dans vos estimations !
> — The Clean Coder

Ne réinventez pas la roue, utilisez des techniques d'estimation bien connues pour les tâches. Voici un résumé de certaines techniques mentionnées dans les deux livres.

- [PERT](https://reymon359.github.io/book-sentences/#/The%20Clean%20Coder/index?id=pert)
- [Wideband Delphi](https://reymon359.github.io/book-sentences/#/The%20Clean%20Coder/index?id=wideband-delphi)
- [Flying Fingers](https://reymon359.github.io/book-sentences/#/The%20Clean%20Coder/index?id=flying-fingers)
- [Planning Poker](https://reymon359.github.io/book-sentences/#/The%20Clean%20Coder/index?id=planning-poker)
- [Affinity Estimation](https://reymon359.github.io/book-sentences/#/The%20Clean%20Coder/index?id=affinity-estimation)
- [Trivariate Estimates](https://reymon359.github.io/book-sentences/#/The%20Clean%20Coder/index?id=trivariate-estimates)
- [The Law of Large Numbers](https://reymon359.github.io/book-sentences/#/The%20Clean%20Coder/index?id=the-law-of-large-numbers)

Plus vous avez d'expérience sur un certain projet, mieux vous estimerez ses tâches. Par conséquent, ne vous inquiétez pas si les premières estimations que vous faites ne sont pas aussi précises qu'elles pourraient l'être. C'est un processus incrémental comme pour tout objectif à long terme que vous souhaitez atteindre.

Comme l'une de mes citations préférées le dit :

> Il n'y a qu'**une** façon de **manger un éléphant** : **une bouchée à la fois**.
> — Desmond Tutu

Cependant, il n'y a aucun moyen de manger une telle mignonnerie :

![Éléphant](https://www.freecodecamp.org/news/content/images/2021/11/elephant.gif)

## Développement par balles traceuses

Les balles traceuses sont un type spécial de balle utilisé dans les films pour marquer le chemin qu'elles ont pris comme retour d'information pour le tireur afin de mieux viser la prochaine fois. Par conséquent, l'objectif principal du développement par balles traceuses est de "tirer" de nouvelles fonctionnalités dans le projet et d'obtenir un retour rapide pour "viser" mieux les suivantes.

> Le développement par traceurs est cohérent avec l'idée qu'un projet n'est jamais terminé : il y aura toujours des changements nécessaires et des fonctions à ajouter. C'est une approche incrémentale.
> — The Pragmatic Programmer

![Balles traceuses. Source : The Pragmatic Programmer](https://www.freecodecamp.org/news/content/images/2021/11/tracer_bullets.png)

Cette méthode aide les développeurs à se concentrer sur les principales fonctionnalités à implémenter afin que d'autres puissent être construites.

De plus, cela sert de **preuve que l'architecture est compatible et réalisable** en fournissant un squelette fonctionnel et démontrable à partir du début du processus de développement.

> Recherchez les exigences importantes, celles qui définissent le système. Recherchez les domaines où vous avez des doutes et où vous voyez les plus grands risques. Ensuite, priorisez votre développement afin que ces domaines soient les premiers que vous codez.
> — The Pragmatic Programmer

![outer-digit-Ys78stblUyY-unsplash](https://www.freecodecamp.org/news/content/images/2021/11/outer-digit-Ys78stblUyY-unsplash.jpg)

Enfin, **le développement par balles traceuses ne doit pas être confondu avec le prototypage**. Le code des prototypes n'est pas censé faire partie du projet, alors que le code des balles traceuses n'est pas jeté. Il fonctionne et est amélioré à chaque itération avec de nouvelles fonctionnalités.

> Le prototypage génère du code jetable. Le code traceur est maigre mais complet, et fait partie du squelette du système final. Considérez le prototypage comme la reconnaissance et la collecte de renseignements qui ont lieu avant qu'une seule balle traceuse ne soit tirée.
> — The Pragmatic Programmer

## Comment gérer la pression

J'ai aimé celui-ci aussi, car il vous aide en dehors du développement logiciel. Tôt ou tard, vous serez sous pression, et les meilleurs trucs pour la gérer sont de **l'éviter quand vous pouvez, et de la supporter quand vous ne pouvez pas**.

> La meilleure façon de rester calme sous pression est d'éviter les situations qui causent la pression.
> — The Clean Coder

![Éviter](https://www.freecodecamp.org/news/content/images/2021/11/avoiding.gif)

Vous l'évitez principalement **en gérant les engagements, en restant propre et en suivant vos disciplines**.

La meilleure façon de gérer les engagements est de _dire non_ à ces délais dont vous n'êtes pas sûr de pouvoir respecter. Rester propre signifie essentiellement que vous n'avez pas de désordre dans vos systèmes, votre code et votre conception.

> La façon d'aller vite et de tenir les délais à distance est de rester propre. Les professionnels ne succombent pas à la tentation de créer un désordre pour avancer rapidement. "Rapide et sale" est un oxymore. Sale signifie toujours lent !
> — The Clean Coder

**Suivez les disciplines en lesquelles vous croyez vraiment et tenez-vous-y en tout temps**, quelle que soit la situation. Les temps de crise viendront, et c'est à ce moment-là que vous devez prêter attention à votre comportement. Si vous suivez vos disciplines, cela signifie que vous croyez en elles.

Changer votre comportement et ne pas suivre vos disciplines signifierait que vous ne croyez pas vraiment en votre comportement normal, et vous devez changer ces disciplines pour l'améliorer.

> Si vous gardez votre code propre pendant les périodes normales mais faites des désordres en cas de crise, alors vous ne croyez pas vraiment que les désordres vous ralentissent. Si vous travaillez en binôme en cas de crise mais ne le faites pas normalement, alors vous croyez que le binôme est plus efficace que le travail individuel.
> — The Clean Coder

![federico-lancellotti-YBuVjp5Mtrw-unsplash](https://www.freecodecamp.org/news/content/images/2021/11/federico-lancellotti-YBuVjp5Mtrw-unsplash.jpg)

Choisissez des disciplines avec lesquelles vous vous sentez à l'aise de suivre en cas de crise. _Ensuite, suivez-les tout le temps._ Suivre ces disciplines est la meilleure façon d'éviter de se retrouver dans une crise. Ne changez pas votre comportement lorsque la pression arrive. Si vos disciplines sont la meilleure façon de travailler, alors elles doivent être suivies même dans les profondeurs d'une crise.

Mais vous ne pouvez pas toujours éviter la pression, donc vous devez apprendre à la traverser. **Vous la supportez en restant calme, en communiquant, en suivant vos disciplines et en obtenant de l'aide.**

Pour rester calme, **ne paniquez pas**, gérez votre stress et réfléchissez au problème pour trouver la meilleure issue possible. Ensuite, allez-y à un rythme régulier, _comme manger un éléphant_. Assurez-vous de **communiquer** tout le temps avec votre équipe et vos supérieurs pour les informer lorsque vous êtes en difficulté afin que vous puissiez obtenir des conseils et des orientations. De cette façon, il n'y aura pas de surprises inattendues à la fin.

![La communication est la clé](https://www.freecodecamp.org/news/content/images/2021/11/good_communication_is_the_key_to_success.jpg)

> Évitez de créer des surprises. Rien ne rend les gens plus en colère et moins rationnels que les surprises. Les surprises multiplient la pression par dix.
> — The Clean Coder

De la même manière que vous vous êtes appuyé sur vos disciplines pour éviter la pression, vous devriez également vous appuyer sur elles lorsque le moment devient difficile. En fait, à ces moments-là, vous devez leur accorder une attention particulière et ne pas les remettre en question ni les abandonner.

Le conseil de communication inclut **demander de l'aide** à vos coéquipiers pour travailler en binôme, à vos supérieurs, ou sur des sites internet et des forums.

N'oubliez pas d'être là pour les autres aussi lorsqu'ils sont sous pression et ont besoin d'aide.

> Lorsque la pression est forte, trouvez un associé qui est prêt à programmer en binôme avec vous. Vous irez plus vite, avec moins de défauts. Votre partenaire de binôme vous aidera à maintenir vos disciplines et à éviter de paniquer.
> — The Clean Coder

![binôme](https://www.freecodecamp.org/news/content/images/2021/11/pairing.gif)

## L'importance du refactoring

Le terme _Refactoring_ est défini par Martin Fowler comme :

> Une technique disciplinée pour restructurer un corps de code existant, en modifiant sa structure interne sans changer son comportement externe.
> — Martin Fowler

Parfois, vous trouverez du code qui ne semble pas correct et qui devrait être corrigé ou amélioré. Et vous devez garder à l'esprit que le meilleur moment pour le faire est **maintenant**, lorsque vous le trouvez.

**C'est inévitable : le code d'un programme doit croître, évoluer et s'améliorer.** Pour ce faire, vous devrez reconsidérer certaines décisions, et le code devra changer. Assurez-vous donc de le couvrir avec des **tests automatisés** pour garantir que le comportement externe ne change pas.

> Plutôt que de la construction, le logiciel ressemble davantage au jardinage - il est plus organique que concret. Vous plantez de nombreuses choses dans un jardin selon un plan initial et des conditions. Vous surveillez constamment la santé du jardin et apportez des ajustements si nécessaire.
> — The Pragmatic Programmer

![Bob jardinant](https://www.freecodecamp.org/news/content/images/2021/11/bobs_burger_gardening.gif)

Quand devez-vous refactoriser le code ? Voici une liste de situations qui qualifient :

- Pour supprimer la **duplication de code**.
- Pour rendre certaines parties du code plus **orthogonales**.
- Pour **mettre à jour** le code et/ou la documentation qui est obsolète.
- Pour améliorer les **performances**.

Et voici les conseils de Martin Fowler sur la façon de refactoriser sans faire plus de mal que de bien :

1. N'essayez pas de refactoriser et d'ajouter des fonctionnalités en même temps.
2. Assurez-vous d'avoir de bons tests avant de commencer à refactoriser. Exécutez les tests aussi souvent que possible.
3. Faites des étapes courtes et délibérées : déplacez un champ d'une classe à une autre, divisez une méthode, renommez une variable. Le refactoring implique souvent de faire de nombreux changements localisés qui résultent en un changement à plus grande échelle.

La chose la plus importante à garder à l'esprit est que **le refactoring n'est pas une tâche certaine, c'est une habitude**. Et, comme pour la plupart des choses dans la vie, il est plus facile à faire lorsque les problèmes sont petits, en tant qu'activité continue pendant le codage.

**Moins vous refactorisez maintenant, plus vous devrez investir de temps pour corriger le problème plus tard.**

![Chat refactorisant](https://www.freecodecamp.org/news/content/images/2021/11/cat_refactoring.gif)

> Le refactoring comme "une croissance". Le supprimer nécessite une chirurgie invasive. Vous pouvez l'enlever tant qu'il est encore petit. Ou, vous pourriez attendre qu'il grandisse et se propage - mais le supprimer alors sera à la fois plus coûteux et plus dangereux. Attendez encore plus longtemps, et vous pourriez perdre le patient entièrement.
> — The Pragmatic Programmer

## Principales différences entre ces livres

![Différences](https://www.freecodecamp.org/news/content/images/2021/11/differences.gif)

Je ne voulais pas que cet article soit une comparaison - mais bien que ces livres se concentrent sur des sujets similaires, le contenu et la manière dont chacun est narré ne sont pas les mêmes.

Voici les principales impressions que j'ai eues d'eux qui ne sont pas liées au contenu lui-même. Ces observations peuvent vous aider à avoir une idée de ce à quoi vous attendre en les lisant.

- The Clean Coder parle du développeur de manière plus quotidienne au travail. Il fait référence à des situations courantes qui se produisent dans un tel environnement, comme la relation avec les commerciaux ou les hommes d'affaires, le travail en équipe ou le fait de dire non aux clients. Le développeur dans The Pragmatic Programmer n'est pas vraiment placé dans des situations de travail. Plutôt, il donne un aperçu du domaine, structurant le livre sur des conseils : _sujets et astuces_, pour toute situation.
- The Clean Coder fait référence à la figure du développeur logiciel en tant que _Professional Programmer_ tandis que The Pragmatic Programmer utilise le terme totalement inattendu _Pragmatic Programmer_.
- En termes généraux, The Clean Coder a un sens plus subjectif puisqu'il partage plus d'expériences personnelles de l'auteur. D'un autre côté, The Pragmatic Programmer semble plus objectif, se concentrant principalement sur les conseils eux-mêmes.
- The Pragmatic Programmer contient plus d'exemples de code dans différents langages de programmation que The Clean Coder, ce qui vous aide à comprendre les concepts discutés.

## Conclusion

Gardez à l'esprit que ce que j'ai discuté ici n'est que mes propres impressions personnelles et les leçons que j'ai tirées de la lecture de ces deux livres. Chaque livre a beaucoup plus à offrir, et la meilleure chose que vous puissiez faire est de les lire tous les deux vous-même pour vous forger votre propre opinion et vos propres conclusions.

Si vous êtes intéressé par le développement logiciel et que vous voulez vous améliorer, vous devriez lire les deux. Cela en vaut la peine - ils sont très différents et chacun mérite votre temps. Et ils vous apporteront des connaissances et des meilleures pratiques différentes pour votre carrière.

Cela dit, si vous voulez toujours prendre le chemin paresseux, j'ai créé ce [projet open-source avec les phrases principales de chaque livre](https://github.com/reymon359/book-sentences).

[![[Book Sentences Project](https://github.com/reymon359/book-sentences)](https://www.freecodecamp.org/news/content/images/2021/11/book_sentences.png)](https://github.com/reymon359/book-sentences)

## Ressources

Les principales ressources sont les deux livres, que vous pouvez facilement trouver sur internet et [le projet](https://github.com/reymon359/book-sentences/) où j'ai noté les phrases que j'ai trouvées les plus importantes.

J'espère que vous avez apprécié cet article. Vous pouvez aussi le lire [sur mon site](https://ramonmorcillo.com/7-lessons-learned-from-the-pragmatic-programmer-and-the-clean-coder/) avec d'autres ! Si vous avez des questions, des suggestions ou des commentaires en général, n'hésitez pas à me contacter sur l'un des réseaux sociaux de [mon site](https://ramonmorcillo.com/).