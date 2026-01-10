---
title: Comment utiliser la répétition espacée avec Anki pour apprendre à coder plus
  rapidement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-18T23:57:01.000Z'
originalURL: https://freecodecamp.org/news/use-spaced-repetition-with-anki-to-learn-to-code-faster-7c334d448c3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nhu0oiFBy4jJLlpJpRWGtA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: Web Development
  slug: web-development
seo_title: Comment utiliser la répétition espacée avec Anki pour apprendre à coder
  plus rapidement
seo_desc: 'By Steven Gilbert

  Imagine you could speed up your learning and better remember programming fundamentals,
  techniques, and commands.

  Today I tell you how to do just that, using spaced repetition and a free open source
  tool called Anki.

  Many have attest...'
---

Par Steven Gilbert

Imaginez que vous pourriez accélérer votre apprentissage et mieux mémoriser les fondamentaux de la programmation, les techniques et les commandes.

Aujourd'hui, je vous explique comment faire exactement cela, en utilisant la **répétition espacée** et un outil open source gratuit appelé **Anki**.

Beaucoup ont attesté des bénéfices de la répétition espacée :

* Le champion de Jeopardy! [Robert Craig](https://en.wikipedia.org/wiki/Roger_Craig_%28Jeopardy!_contestant%29) dit qu'il doit une partie de son succès à l'utilisation d'Anki pour mémoriser des anecdotes.
* [Googley as Heck](https://www.freecodecamp.org/news/use-spaced-repetition-with-anki-to-learn-to-code-faster-7c334d448c3c/undefined), qui a étudié à temps plein pendant 8 mois pour un [entretien chez Google](https://medium.freecodecamp.com/why-i-studied-full-time-for-8-months-for-a-google-interview-cc662ce9bb13#.3d9qfnhq5), dit : « La répétition espacée est la clé de la mémorisation... Vous devenez un expert en revisitant et en révisant au fil du temps. Si vous le faites, vous atteindrez le point où [vous] ne pouvez pas oublier les détails. »
* Et [Derek Sivers](https://sivers.org/), fondateur de CDBaby, [écrit](https://sivers.org/srs) que la répétition espacée est « la technique d'apprentissage la plus utile que j'ai trouvée en 14 ans de programmation informatique ».

Pour moi personnellement, Anki a été une partie indispensable de mes efforts pour apprendre à coder. Je l'utilise pour me souvenir des idées importantes de HTML, CSS, JavaScript, et des commandes de Git et Bash.

Je suis actuellement en report à l'école de droit de l'UC-Berkeley, et Anki fera à 100 % partie de ma stratégie pour maîtriser le droit.

Dans cet article, je vais couvrir :

* Qu'est-ce que la répétition espacée
* Comment Anki aide avec la répétition espacée
* Et comment ceux-ci peuvent accélérer votre apprentissage et améliorer votre rétention des concepts de programmation.

### Qu'est-ce que la répétition espacée ?

La [répétition espacée](https://en.wikipedia.org/wiki/Spaced_repetition) cherche à résoudre le [problème de l'oubli](https://www.supermemo.com/english/princip.htm#optimal_intervals). Elle soutient que le moment idéal pour se souvenir d'une nouvelle information est _au moment_ où vous êtes sur le point de l'oublier.

Par exemple, supposons que vous ne connaissez pas la capitale de la [Colombie](https://en.wikipedia.org/wiki/Colombia). Et supposons que je vous dise maintenant quelle est la capitale de la Colombie.

_La capitale de la Colombie est Bogotá_.

Supposons que votre mémoire est telle que vous vous souviendrez de ce nouveau fait — que la capitale de la Colombie est Bogotá — après votre toute première exposition à celui-ci, pendant un bon **20 minutes**. Après quoi vous oublierez.

Mais, si à **19 minutes et 59 secondes**, alors que nous prenons une tasse de café, je vous _rappelle_...

_La capitale de la Colombie est Bogotá_.

... la théorie de la répétition espacée dit que vous serez capable de vous souvenir que Bogotá est la capitale de la Colombie pendant, disons, **40 minutes**. Après quoi vous oublierez.

Mais, si je vous rappelle à nouveau **39 minutes et 59 secondes plus tard** que...

_La capitale de la Colombie est Bogotá_.

... vous serez capable de retenir cette information géographique en mémoire pendant une période encore plus longue, disons jusqu'à **une heure**.

Et si nous continuons à procéder de cette manière, où je vous rappelle que la capitale de la Colombie est Bogotá _précisément_ au moment où vous êtes sur le point d'oublier, le temps entre les oublis _augmente_ exponentiellement de heures à jours, puis à mois, puis à années.

Et finalement, selon la théorie, la connaissance — que Bogotá est la capitale de la Colombie — sera plus ou moins définitivement ancrée dans votre mémoire.

Cette notion de déclin de la mémoire au fil du temps est connue sous le nom de [courbe de l'oubli](https://en.wikipedia.org/wiki/Forgetting_curve), et elle a été développée par [Hermann Ebbinghaus](https://en.wikipedia.org/wiki/Hermann_Ebbinghaus) en 1885.

![Image](https://cdn-media-1.freecodecamp.org/images/lmXQiQYcqNbLyTGoAVxbKZvmbGURF20DmZxq)
_Stahl et al 2010; CNS Spectr_

Et cette idée — qu'il est plus efficace et plus efficace d'espacer l'apprentissage dans le temps plutôt que de bachoter — est connue sous le nom d'[effet d'espacement](https://en.wikipedia.org/wiki/Spacing_effect).

Ensemble, la courbe de l'oubli et l'effet d'espacement sont les concepts fondamentaux derrière la répétition espacée.

En fonction de votre courbe de l'oubli, vous déterminez l'[intervalle optimal](http://www.lac.ane.pl/pdf/5409.pdf) pour vous rappeler un élément de mémoire (signifiant toute information), et vous espacez le renforcement de l'élément de mémoire en conséquence. Piotr Woźniak, un pionnier dans la recherche sur la mémoire, [résume](https://www.supermemo.com/english/princip.htm#optimal_intervals) ces idées :

> Les intervalles optimaux sont calculés sur la base de deux critères contradictoires :

> 1. Les intervalles doivent être aussi longs que possible pour obtenir la fréquence minimale de répétitions, et pour faire le meilleur usage de l'effet d'espacement, qui dit que des intervalles plus longs entre les répétitions, jusqu'à une certaine limite, produisent des mémoires plus fortes.

> 2. Les intervalles doivent être suffisamment courts pour s'assurer que la connaissance est encore mémorisée.

À ce stade, vous pourriez vous demander : « Mais comment savez-vous _précisément_ le moment où vous êtes sur le point d'oublier que la capitale de la Colombie est Bogotá ? Comment savez-vous quel est votre intervalle optimal ? »

Bien sûr, il serait assez difficile de le savoir à la seconde près sans beaucoup d'essais et d'erreurs fastidieux et une attention aux détails de niveau Charles Darwin. Mais heureusement, nous n'avons pas besoin d'une telle diligence car un ami familier peut nous aider : **le logiciel**.

(Vous pouvez également utiliser un système non automatisé appelé le [système Leitner](https://en.wikipedia.org/wiki/Leitner_system).)

Le logiciel, construit sur une montagne de recherches sur la mémoire, peut vous aider à déterminer le moment optimal pour renforcer la mémorisation. Et spécifiquement le **logiciel de répétition espacée**.

### Qu'est-ce qu'Anki ?

[Anki](https://apps.ankiweb.net/) est un outil [open source](https://github.com/dae/anki) de logiciel de répétition espacée développé et maintenu par [Damien Elmes](https://github.com/dae/). Vous pouvez le considérer comme une sorte de « programme de flashcards intelligent » qui utilise la répétition espacée et rend la mémorisation plus efficace.

Anki est construit sur le principe que vous mémorisez mieux les connaissances avec des rappels périodiques et stratégiquement planifiés. Ce qui signifie qu'il est construit sur les pouvoirs de la répétition espacée.

![Image](https://cdn-media-1.freecodecamp.org/images/8eeD7QQ2cqKBAmq4ivMcDzQhmrNbY0uKd4HZ)
_[Crédit image](https://www.wired.com/2008/04/ff-wozniak/" rel="noopener" target="_blank" title=")_

Vous pouvez utiliser Anki pour mémoriser pratiquement tout ce qui doit être mémorisé.

Notez, cependant, qu'Anki n'est pas un remplacement pour _l'apprentissage_. Vous devez d'abord comprendre le matériel que vous apprenez, puis le commettre à Anki, qui vous aidera brillamment à retenir les connaissances que vous avez acquises. Ce qui signifie qu'Anki fait partie du processus d'apprentissage qui vient après la compréhension.

![Image](https://cdn-media-1.freecodecamp.org/images/UG2cK2im2551HZaYin9OhVyLVdWE-ip0kKx4)
_[Crédit image](https://www.gwern.net/Spaced%20repetition" rel="noopener" target="_blank" title=")_

Il existe d'autres logiciels de répétition espacée dans le monde tels que [SuperMemo](https://www.supermemo.com/english/smintro.htm), créé par le susmentionné Piotr Woźniak. Anki met en fait en œuvre une version de l'[algorithme](https://en.wikipedia.org/wiki/Anki_%28software%29) qui alimente SuperMemo.

Je me concentre ici sur Anki parce que c'est ce à quoi je me suis habitué, cela fonctionne bien, et c'est open source et gratuit. Si vous avez utilisé SuperMemo ou un autre outil SRS, faites-nous savoir votre expérience dans les commentaires.

Si vous décidez d'utiliser Anki également, je vous encourage néanmoins à [lire](https://www.wired.com/2008/04/ff-wozniak/?currentPage=all) sur Woźniak et ce qu'il a eu à dire sur la mémoire, l'apprentissage et la [créativité](https://www.supermemo.com/articles/genius.htm) car c'est très perspicace.

En ce qui concerne les appareils, Anki existe en version desktop, qui, si vous n'avez pas utilisé Anki auparavant, est recommandée pour commencer. Il y a aussi :

* Une application web compagnon gratuite, [AnkiWeb](https://apps.ankiweb.net/).
* Une application Android compagnon gratuite [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki&hl=en), entièrement compatible et synchronisable avec Anki desktop/web.
* Et pour les utilisateurs d'iPhone, une application compagnon à 24,99 $ [AnkiMobile](https://itunes.apple.com/us/app/ankimobile-flashcards/id373493387?mt=8) dans l'AppStore.

### Comment fonctionne Anki

Sachez que vous pouvez aller [en profondeur](https://apps.ankiweb.net/docs/manual.html) dans la façon dont vous utilisez et configurez Anki. Je ne vous donne qu'un aperçu de haut niveau pour que vous compreniez l'essentiel.

1. Vous créez des « **paquets** », qui sont un groupe de cartes représentant une catégorie large. Par exemple, « JavaScript » ou « Capitales » pourrait être un paquet.

Voici un exemple d'un paquet Anki dans l'application desktop. (Ne vous inquiétez pas pour « Nouveau », « Apprentissage », « À réviser » pour l'instant. Je reviendrai à ceux-ci dans un moment) :

![Image](https://cdn-media-1.freecodecamp.org/images/ZiDvGOE4JheKaajYqHONhZGSxWvO14YsOD-j)
_Exemple de paquet Anki_

2. Vous ajoutez des « **cartes** » à vos paquets, qui sont personnalisables avec HTML et CSS.

Une carte pourrait être une flashcard standard recto-verso, où vous êtes d'abord présenté avec le recto. Voici un exemple d'un paquet sur les « Capitales » :

![Image](https://cdn-media-1.freecodecamp.org/images/ryIdZ3jHPJw83npgNb9pIfwcnlHj73IMf-N3)
_Exemple de carte Anki — recto du type Basique_

Et lorsque vous êtes prêt pour la réponse, vous cliquez sur **Montrer la réponse** pour révéler la réponse au verso de la carte :

![Image](https://cdn-media-1.freecodecamp.org/images/JSE9oBdeDkYfFUobJdpbkTI-Of-Za28eot6o)
_Carte Anki — recto et verso du type Basique_

Astuce : il existe d'autres types de cartes, outre le type flashcard recto-verso, comme la [suppression cloze](https://en.wikipedia.org/wiki/Cloze_test) avec laquelle vous voudrez vous familiariser. La suppression cloze est un type de carte particulièrement utile que j'utilise tout le temps (en fait, la plupart de mes cartes utilisent la suppression cloze) car elle est simple et efficace pour organiser les informations.

Astuce : créer des cartes Anki est un art. Et plus vous pratiquez, meilleur vous deviendrez. En règle générale, vous voudrez essayer de suivre le [principe de l'information minimale](https://www.supermemo.com/en/articles/20rules), qui signifie essentiellement :

KISS — Keep it Simple Stupid. Vous voulez garder vos cartes aussi simples que possible car simple est plus facile à retenir.

3. Une fois que vous avez terminé d'ajouter des cartes, vous utilisez Anki (vous pratiquez).

Revenons à la carte Colombie-Bogotá pour voir comment fonctionne le processus.

![Image](https://cdn-media-1.freecodecamp.org/images/D4napkahfAswTdCBbFhamvi8IrQNDwQwkS11)
_Choisissez quand vous souhaitez être rappelé à nouveau_

Après avoir cliqué sur **Montrer la réponse** et être passé au verso de la carte, vous vous demandez :

_À quel point était-il difficile de trouver la réponse ?_

* Si vous ne connaissiez pas la réponse, vous pourriez choisir **À nouveau**, ce qui vous exposera à nouveau à la carte en **moins d'une minute**.
* Si vous avez trouvé la réponse après une pause et en fouillant dans votre mémoire, vous pourriez sélectionner **Bien**, ce qui vous montrera la carte à nouveau en **moins de 10 minutes**.
* Et si la réponse était facile, vous choisissez **Facile** et vous ne verrez pas la carte à nouveau avant **quatre jours**.

Le programme d'Anki suit alors l'état de votre progression : quelles cartes réviser et quand. Ce qui signifie qu'Anki fait le travail fastidieux de suivre votre courbe d'oubli pour chaque carte.

C'est le pouvoir d'automatiser la répétition espacée avec un logiciel.

Je devrais souligner que vous pouvez changer certaines des variables de l'algorithme de répétition espacée d'Anki. Vous le faites en allant dans les options de votre paquet et en personnalisant ce que vous voulez personnaliser, comme le nombre de cartes révisables par jour, les options d'intervalle de temps, parmi d'autres variables.

![Image](https://cdn-media-1.freecodecamp.org/images/xshWnFcgpmakDQP6jDl1bJt-PGcKAhTUNM4D)
_Personnalisation de vos options de paquet_

Au début, cependant, vous pourriez vouloir laisser ces paramètres tels quels et simplement utiliser les valeurs par défaut. Et à mesure que vous devenez plus à l'aise avec Anki, vous pouvez commencer à être créatif avec les options de paquet.

Pour revisiter notre paquet JavaScript :

![Image](https://cdn-media-1.freecodecamp.org/images/pvwi8XDqMFmczxQBCTLVAT04fOS93JjhhOXy)
_Exemple de paquet Anki_

* **Nouveau** signifie que vous avez ajouté 4 nouvelles cartes à votre paquet JavaScript et qu'elles sont prêtes à être révisées.
* **Apprentissage** signifie que, si vous êtes en train de travailler sur un paquet et que vous avez choisi, par exemple, **Bien <10m**, Anki stockera cette carte dans la file d'apprentissage et vous la montrera à nouveau dans 10 minutes. Voir [ici](https://apps.ankiweb.net/docs/manual.html#learning) pour plus de détails.
* **À réviser** signifie le nombre de cartes en attente de révision.

Et tout cela deviendra beaucoup plus clair à mesure que vous utiliserez Anki.

### Comment commencer avec Anki

En ce qui concerne les tutoriels et comment utiliser Anki, la [documentation](https://apps.ankiweb.net/docs/manual.html) sur le site est phénoménale et répondra probablement à la plupart de vos questions. Et il y a aussi quelques [tutoriels vidéo](https://www.youtube.com/channel/UCFt1oYUNiwkMaJTSZiFEodQ) utiles.

En attendant, je vous donne une liste de contrôle sur comment commencer avec Anki parce que les [listes de contrôle](https://www.amazon.com/Checklist-Manifesto-How-Things-Right/dp/0312430000) peuvent être utiles.

1. Lisez l'[article](https://sivers.org/srs) de Derek Sivers sur la répétition espacée car il renforce beaucoup de ce dont j'ai parlé.

2. Lisez cet [entretien](https://www.wired.com/2008/04/ff-wozniak/) de Wired avec Piotr Woźniak car il vous donne un aperçu holistique de la répétition espacée, de l'apprentissage et de la recherche sur la mémoire.

3. Lisez [Effective learning: Twenty rules of formulating knowledge](https://www.supermemo.com/en/articles/20rules) de Piotr Woźniak car il vous donne des techniques sur la façon de formuler et structurer vos cartes Anki.

Notamment, rappelez-vous que la répétition espacée n'est pas un substitut à l'apprentissage. Il est crucial que vous compreniez d'abord le matériel avant de le commettre à la répétition espacée. Comprenez d'abord, puis renforcez avec Anki. N'oubliez pas d'utiliser la méthode KISS pour créer des cartes, et d'utiliser des images dans vos cartes lorsque cela est possible.

4. Créez vos propres paquets.

5. N'oubliez pas de garder vos paquets larges et généraux. Par exemple, si vous apprenez JavaScript, ne créez pas un paquet appelé « Fermetures » et un autre appelé « Héritage prototypal ». Créez plutôt un seul paquet « JavaScript ». Consultez [Utiliser les paquets de manière appropriée](https://apps.ankiweb.net/docs/manual.html#manydecks) dans la documentation pour plus de détails.

6. Devenez un avec la [suppression cloze](https://www.youtube.com/watch?v=FnrigOzpJQo) car cela aidera énormément votre apprentissage.

7. Comprenez les inconvénients.

Il y a quelques inconvénients à la répétition espacée. L'interférence dans le rappel en est un.

Par exemple, vous pouvez imaginer rencontrer une interférence dans le rappel avec, disons, les capitales de la Martinique, de la Mauritanie et de Maurice parce qu'elles sont toutes nommées de manière similaire.

Certaines interférences sont difficiles à éviter, et vous pourriez vouloir mettre en œuvre d'autres astuces de mémoire dans de tels cas. Mais vous pouvez limiter l'inconvénient en gardant vos cartes simples.

En savoir plus sur les inconvénients [ici](https://www.gwern.net/Spaced%20repetition) (faites défiler jusqu'aux inconvénients) et [ici](https://www.supermemo.com/en/articles/20rules) (faites défiler jusqu'à combattre l'interférence).

9. N'oubliez pas de garder vos cartes et paquets synchronisés. Choisissez une « base de départ » comme la version desktop, puis synchronisez avec AnkiWeb et l'une des applications mobiles chaque fois que vous apportez une modification. Vous mettez des efforts à créer vos cartes et paquets. Évitez le casse-tête de devoir refaire votre travail.

9. Faites d'Anki une habitude. Pour voir les fruits de la magie d'Anki, vous devez prendre une décision et vous engager à passer en revue vos cartes chaque jour où elles sont dues. Associez Anki à une tasse de café. Ou le matin. Ou l'heure du déjeuner. Ou quelque chose de positif. Trouvez des moyens de faire d'Anki une habitude.

#### **Pour réviser :**

* La répétition espacée est l'idée que vous vous souvenez le plus efficacement d'une information si vous y êtes exposé au moment de l'oubli.
* Anki automatise la répétition espacée. Cela en fait un outil de mémorisation incroyablement efficace et utile.
* Anki peut vous aider à construire votre base de connaissances en programmation informatique, en techniques et en meilleures pratiques.
* En plus des connaissances en programmation informatique, vous pouvez utiliser Anki pour vous souvenir de tout ce que vous voulez ajouter à votre mémoire.
* Rappelez-vous : Anki fait partie du processus d'apprentissage, pas un remplacement. Vous devez d'abord comprendre. Et ensuite utiliser Anki.

Si vous avez des questions, vous pouvez me tweeter à [@gilbertginsberg](https://twitter.com/gilbertginsberg) ou me trouver à [GilbertIndex](https://goo.gl/DgxjEj).

#### **Lectures complémentaires :**

* [Répétition espacée](https://en.wikipedia.org/wiki/Spaced_repetition), Wikipedia
* [Courbe de l'oubli](https://en.wikipedia.org/wiki/Forgetting_curve), Wikipedia
* [Effet d'espacement](https://en.wikipedia.org/wiki/Spacing_effect), Wikipedia
* [Hermann Ebbinghaus](https://en.wikipedia.org/wiki/Hermann_Ebbinghaus), Wikipedia
* [Système Leitner](https://en.wikipedia.org/wiki/Leitner_system), Wikipedia
* [Damien Elmes](https://github.com/dae/anki), créateur d'Anki
* [Documentation Anki](https://apps.ankiweb.net/docs/manual.html)
* [Principes généraux de SuperMemo](https://www.supermemo.com/english/princip.htm) par Piotr Woźniak
* [Les racines de la créativité et du génie](https://www.supermemo.com/articles/genius.htm) par Piotr Woźniak
* [Optimisation de l'espacement des répétitions dans la pratique de l'apprentissage](http://www.lac.ane.pl/pdf/5409.pdf) par Piotr Woźniak et Edward J. Gorzelanczyk
* [Voulez-vous vous souvenir de tout ce que vous apprendrez jamais ? Rendez-vous à cet algorithme](https://www.wired.com/2008/04/ff-wozniak/?currentPage=all) par Gary Wolf dans Wired
* [Mémoriser un langage de programmation en utilisant un logiciel de répétition espacée](https://sivers.org/srs) par Derek Sivers
* [Utiliser des systèmes de répétition espacée pour apprendre et retenir des connaissances techniques.](https://www.jackkinsella.ie/articles/janki-method) par Jack Kinsella
* [Répétition espacée](https://www.gwern.net/Spaced%20repetition) par [@gwern](https://twitter.com/gwern)