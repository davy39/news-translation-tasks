---
title: Code Calligraph VS Code Gribouillis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-13T12:25:06.000Z'
originalURL: https://freecodecamp.org/news/what-is-shitty-code-handwriting-ae7c00708b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D9KCF2ipzxxvUXGu1ya9GA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Code Calligraph VS Code Gribouillis
seo_desc: 'By Alex Ewerlöf

  Over the past 17 years I’ve worked on over 90 projects with many teams. But it wasn’t
  until I came across Git’s blame feature that I learned about each coder’s “handwriting.”
  This simple curiosity soon became a habit. Whenever I saw n...'
---

Par Alex Ewerlöf

Au cours des 17 dernières années, j'ai travaillé sur plus de 90 projets avec de nombreuses équipes. Mais ce n'est qu'en découvrant la fonction `blame` de Git que j'ai appris à connaître l'« écriture » de chaque codeur. Cette simple curiosité est rapidement devenue une habitude. Chaque fois que je voyais un nouveau code, j'essayais de deviner qui l'avait écrit. Ensuite, je vérifiais ma supposition avec un `git blame`.

(À propos, si vous n'êtes pas encore familier avec [git](https://en.wikipedia.org/wiki/Git_%28software%29), c'est un moyen populaire pour les développeurs de collaborer sur du code, et sa fonction « [blame](https://help.github.com/articles/using-git-blame-to-trace-changes-in-a-file/) » vous montre qui a écrit une ligne de code source donnée.)

Après quelques années, j'ai commencé à voir des schémas, tout comme [un expert en écriture](http://www.dailymail.co.uk/sciencetech/article-2380858/What-does-handwriting-say-Study-finds-5-000-personality-traits-linked-write.html) pourrait détecter un sociopathe à la façon dont ils dessinent leurs W. L'écriture du code révèle beaucoup de choses sur le programmeur qui l'a écrit.

Vous pouvez apprendre presque tout de l'écriture d'un programmeur : combien d'expérience il a, combien il se soucie de la lisibilité de son code (et par extension, combien il se soucie de ses coéquipiers).

Le code parle. [Le mauvais code](https://en.wikipedia.org/wiki/Code_smell) crie ! Alors, le code que vous lisez est-il de la calligraphie ou du gribouillis ?

Un petit avertissement : ce que vous allez lire est basé purement sur mon intuition subjective. À ma connaissance, il n'y a pas eu d'études académiques évaluées par des pairs. Mes compétences en analyse d'écriture de code m'ont bien servi dans le passé et pourraient vous aider également, mais — comme pour tout ce que vous lisez sur Internet — les résultats peuvent varier.

### Insight #1 : Code gonflé = lutte

Habituellement, lorsque je découvre un code qui est devenu gonflé et bien plus grand qu'il ne devrait l'être, cela montre un programmeur qui avait du mal à terminer une tâche qui dépassait ses capacités. Ils n'avaient soit pas les connaissances, soit pas le temps pour terminer le travail correctement.

Dans la vraie vie, les gens qui _font_ moins tendent à _parler_ plus. C'est la même chose dans le monde du code : ceux qui ne peuvent pas faire le travail élégamment tendent à écrire beaucoup de code.

Malheureusement, les bugs se nourrissent de code, et plus il y a de code, plus l'habitat pour les bugs est grand.

> « Je déteste le code, et je veux le moins possible dans notre produit » — Jack Diederich

![Image](https://cdn-media-1.freecodecamp.org/images/1*geAN2yrvAR4mfd8C9Uqq6w.jpeg)

### Insight #2 : Code mort = négligence

Vous avez déjà vu d'énormes blocs de code commenté commis dans le dépôt ? Ou pire encore : du code qui ne fait rien de spécial mais qui est là pour des raisons historiques ?

Intéressamment, cela a une corrélation directe avec le désordre du bureau du programmeur qui l'a écrit. Vous avez déjà vu des commentaires ou des tests obsolètes ? Oui, vous avez trouvé un programmeur négligent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WwxpH0REH0QGkwycpDRDhQ.jpeg)

### Insight #3 : Code complexe = stupidité ou avidité

J'adore cette citation de [Schumacher](https://en.wikiquote.org/wiki/E._F._Schumacher) :

> « Tout idiot intelligent peut rendre les choses plus grandes, plus complexes et plus violentes. Il faut un peu de génie — et beaucoup de courage pour aller dans la direction opposée. » — Fritz Schumacher

Si vous trouvez un code difficile à suivre ou à comprendre, soyez assuré qu'il a été écrit soit par quelqu'un qui n'a aucune idée de ce qu'il fait, soit par quelqu'un qui cherche une sécurité d'emploi en prenant « possession » de cette partie du code.

### Insight #4 : Commentaires = un joueur d'équipe (sauf…)

Tous les langages de haut niveau permettent d'écrire du code suffisamment lisible pour ne pas avoir besoin de commentaires. Mais parfois, la complexité est inévitable en raison d'un manque de connaissances, de temps ou de cadre élégant.

J'adore vraiment quand les programmeurs mettent un lien vers une référence d'API ou une question pertinente de Stack Overflow lorsqu'ils réalisent que leurs pairs (ou leur futur moi) vont questionner une ligne de code particulière.

Cela dit, l'utilisation excessive de commentaires montre un manque de confiance en soi (ou, comme je l'ai mentionné précédemment, essayer d'expliquer le « code gonflé »).

### Insight #5 : Noms = compétence en communication

Noms de variables, noms de fonctions, noms de paramètres, noms de classes. Ce sont les niveaux de base de la communication avec les mainteneurs de code.

Si vous tombez sur des noms à une seule lettre (sauf pour `i`, qui est la valeur par défaut dans les boucles `for`), vous avez trouvé un programmeur manquant de compétences en communication ou d'empathie pour les autres.

Sauf s'il s'agit d'un projet temporaire qui ne sera montré à personne d'autre ou maintenu, chaque seconde passée à choisir un nom approprié résulte en un bon karma.

Et si la fonctionnalité d'une entité change, il est important de refactoriser son nom en conséquence.

Certains programmeurs prétendent que les noms ne sont pas importants, puisque les machines ne s'en soucient pas. Eh bien, sauf si vous écrivez du code littéralement en zéros et en uns, vous écrivez aussi du code pour les humains !

### Insight #6 : Mauvaise lisibilité = manque de fluidité

Parfois, les programmeurs sont fluides dans une langue, mais ils essaient de tordre et de plier une autre langue pour qu'elle se comporte comme leur langue favorite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IqL4tmjw8DiMvHT5Q9wGOg.jpeg)

JavaScript est l'une de ces pauvres langues cibles.

La plupart des programmeurs back-end ont le luxe de choisir leur « langue maternelle ». Et beaucoup sont assez courageux pour assembler quelques lignes de code front-end. Mais comme le monde du navigateur est principalement en JavaScript (qui est une langue flexible), ils essaient d'imiter les schémas qui leur sont familiers de leur « langue maternelle ».

Tout cela est bien et bon jusqu'à ce qu'un vrai programmeur JavaScript voie le code et s'arrache les cheveux !

### Insight #7 : Hacks = personnalité superficielle ou manque de discipline

Vous avez déjà passé beaucoup de temps à nettoyer une base de code pour ensuite voir votre pair [verser de l'essence sur votre beau code](http://blog.codinghorror.com/code-smells/) en l'utilisant comme plateforme pour des corrections rapides et sales ?

Félicitations : vous avez rencontré un hacker !

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Oxwskpp6ntXreTWOflWGQ.jpeg)

Les hackers sont excellents pour faire des corrections rapides sans se soucier de comprendre l'architecture de manière holistique (généralement en bidouillant avec un débogueur, ou par essai et erreur).

Alors, quel est le problème ? Ils corrigent un problème et en créent 10 autres.

Les consultants ont tendance à montrer ce comportement (puisque leur temps est précieux, et ils ne vont pas vivre avec les conséquences de leurs changements). De plus, ils peuvent être payés pour corriger ces 10 autres problèmes et semer la sécurité de l'emploi en créant 100 nouveaux.

Néanmoins, j'ai vu des programmeurs internes qui font paraître même les consultants les plus négligents comme des stars du rock. Vous avez déjà estimé qu'un problème prendrait 8 heures, mais qu'un chef de produit réduit votre estimation à seulement 1 heure ? C'est généralement à ce moment-là que les hacks naissent.

Cela dit, parfois vous avez besoin d'une livraison rapide (comme pendant la phase de prototypage dans une start-up pour valider l'idée) et il est acceptable de couper les coins en raison de ressources limitées. Personne ne se soucie d'un beau code qui ne résout aucun problème. Mais il y a quand même une différence entre couper avec des ciseaux ou hacher avec une machette !

### Insight #8 : Incohérence = fierté et fanatisme

> À Rome, fais comme les Romains. — un proverbe

Il existe tant de conventions de codage. Cela n'a pas vraiment d'importance laquelle est choisie. Mais une fois que votre équipe a choisi certaines conventions, il est crucial qu'ils s'y tiennent.

Si les contributeurs ignorent certaines ou toutes les conventions, ils sont soit en train de bidouiller, soit trop fiers pour changer leur style pour correspondre à votre base de code.

Le pire de tout est lorsqu'ils poussent pour leurs propres conventions à la place. C'est du pur fanatisme. Et vous pouvez être sûr que le programmeur est étriqué dans d'autres domaines également.

### Insight #9 : Code WET = mauvaise mémoire

L'opposé de [Dry](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (« Ne vous répétez pas ») est WET (« Nous aimons taper » ou « Écrivez tout deux fois »).

Eh bien, les bugs se reproduisent par un processus désordonné appelé « copier » et « coller ».

Il existe surprenamment de nombreux types de code WET. Par exemple :

1. Une fonction ou une classe écrite deux fois, avec seulement des différences mineures
2. Une variable qui contient la valeur d'une autre variable
3. Un ensemble d'instructions répétitives qui pourraient résider dans une fonction

Cela est différent du code gonflé, en ce sens que plutôt que d'être simplement complexe ou tordu, le code WET est littéralement répété.

Habituellement, le code répétitif est un signe qu'un programmeur ne peut pas se rappeler (ou pire, n'a pas vu) l'autre code similaire. L'une des principales tâches du cerveau humain est de détecter des schémas. Lorsqu'un programmeur est incapable de repérer un code similaire, c'est un signe d'inexpérience ou d'inattention aux détails.

### Insight #10 : Solutions temporaires = manque de discipline

Parfois, les développeurs injectent une solution rapide et sale comme solution temporaire, espérant qu'un jour ils auront le temps de la refactoriser. Cela se produit généralement en raison d'une date limite serrée ou d'un manque de connaissances. Mais comme nous le savons tous, les solutions temporaires sont là pour rester.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-G0N_d5G6zCDxcExo8qafQ.jpeg)

Les solutions temporaires indiquent un ingénieur pragmatique qui manque de goût ou de fierté dans son travail. Elles peuvent également être un signe de faible estime de soi, car ils ne veulent pas décevoir quelqu'un d'autre (patron, client, etc.).

La seule fois où une solution temporaire est acceptable est pour un projet d'apprentissage ou de prototypage (preuve de concept). Et même dans ces cas, il est préférable de la refactoriser dès que vous savez comment le faire correctement.

### Insight #11 : Beaucoup de dépendances = négligence pour l'avenir du projet

Les dépendances doivent être maintenues à jour. Lorsqu'un projet a trop de dépendances, c'est un signe de négligence.

Il est difficile de dire ce qui est « trop », mais la règle générale est : si le projet peut facilement survivre sans une dépendance, elle est redondante.

Une autre mesure est que s'il n'y a pas d'exigence nécessaire pour le problème sous-jacent que la dépendance résout, elle est probablement inutile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MfKP9AjNFtlQUdxU8_8R_g.jpeg)

### Il existe trois motivations pour les dépendances inutiles :

#### Raison #1 : Le développeur est trop impatient d'apprendre de nouvelles choses.

En important de nouvelles dépendances, ils obtiennent la chance de faire cet apprentissage dans un projet réel.

La curiosité est bonne, mais il devrait y avoir d'autres plateformes pour apprendre, comme des projets parallèles, des tâches à court terme ou des hackathons.

Vous ne voulez pas perdre un bon développeur parce qu'il pense qu'il ne peut pas évoluer dans son travail, mais vous ne voulez pas non plus qu'il traite votre produit comme son projet personnel.

#### Raison #2 : C'est fait par un développeur junior trop ambitieux.

Les nouveaux venus dans un domaine ont tendance à être submergés par tous les nouveaux mots à la mode, et par frustration ou ignorance (ou sur recommandation d'un « pro »), ils peuvent décider de « sauter dans la piscine » et d'apprendre tout à la fois. Ne les laissez pas faire. [Choisissez votre technologie](https://medium.com/@alexewerlof/how-i-learn-new-tech-cb79db19c818).

#### Raison #3 : Le développeur a des bagages d'un autre travail (ou d'un projet parallèle)

Ils veulent avoir un avantage sur leurs pairs en apportant quelque chose que seuls ils connaissent très bien.

Malheureusement, il n'y a pas de solution facile à cela, mais des compétences douces : l'équipe doit remettre en question le choix de chaque dépendance, et s'il y a un processus de révision et de fusion de code en place, il est difficile de faire passer du terrible code sans que quelqu'un le remarque.

Parfois, le codeur cowboy en question peut faire une refactorisation massive, puis mettre l'équipe dans une position d'accepter l'ensemble du changement parce qu'il est déjà fait. Eh bien, ne le faites pas ! Demandez-leur de diviser leur demande de tirage en parties plus petites et soyez sceptique quant à l'ajout de nouvelles dépendances. Oui, c'est plus de travail, mais cela va économiser beaucoup plus de temps et d'énergie à long terme.

Les bons développeurs se soucient de l'avenir de leur projet parce qu'ils ont passé leur ressource la plus finite et précieuse à le créer : leur temps !

![Image](https://cdn-media-1.freecodecamp.org/images/1*kco_a6noe_ekN5aRq_vPCw.jpeg)

D'ailleurs, beaucoup de dépendances et de mots à la mode peuvent aussi être un signe que le développeur construit un CV et se prépare déjà pour son prochain emploi.

### Calligraphie de code

Maintenant que nous avons discuté du gribouillis de code, parlons de l'autre côté : le code qui est un vrai plaisir à lire.

Certains disent même que « [le code est de la poésie](https://www.smashingmagazine.com/2010/05/the-poetics-of-coding/) ».

Le code source de [jQuery](https://github.com/jquery/jquery) ou [lodash](https://github.com/lodash/lodash) en sont de bons exemples, mais presque toutes les bibliothèques populaires sur Github, avec beaucoup de contributeurs, convergent finalement vers la beauté. Cela, mes amis, est une merveilleuse _calligraphie de code_.

Essentiellement, un grand code est :

1. Facile à lire, suivre et déboguer
2. Flexible, configurable et extensible
3. Intelligent avec l'utilisation des ressources
4. Haute performance

Notez que certains projets demandent un ordre différent. Par exemple, [le code source de Linux](https://github.com/torvalds/linux) peut ne pas être très facile à lire parce que la performance est plus importante pour un système d'exploitation. Ou une humble application IoT embarquée peut sacrifier la configuration en faveur de l'optimisation des ressources.

En tout cas, il y a beaucoup plus de choses que vous pouvez découvrir sur vos pairs simplement en analysant leur code. Le code parle plus fort que les mots ! Alors, la prochaine fois que vous lisez du code, essayez la commande `git blame` et commencez à reconnaître l'écriture du code.

_⚠️ Aimez ce que vous avez lu ? **Suivez**-moi pour être notifié lorsque j'écris quelque chose de nouveau._

Vous pourriez aussi vouloir découvrir pourquoi [la programmation est le meilleur travail au monde](https://medium.com/p/what-s-cool-about-being-a-programmer-5a1e58efeee6).