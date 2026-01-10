---
title: Leçons apprises en 10 ans en tant que développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T17:08:23.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-in-my-10-years-as-a-developer-3d33c8702828
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_6Q3e7_NMGteVQbGbKEZy5g.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Leçons apprises en 10 ans en tant que développeur
seo_desc: 'By Huseyin Polat Yuruk

  12 months.

  That’s the time we wasted while rewriting our software from scratch.

  Twelve long months in the software market.

  Without innovation.

  Without moving forward.

  Really, I cannot stop asking this question to myself.


  What ...'
---

Par Huseyin Polat Yuruk

### 12 mois.

C'est le temps que nous avons perdu en réécrivant notre logiciel à partir de zéro.

Douze longs mois sur le marché du logiciel.

Sans innovation.

Sans avancer.

Vraiment, je ne peux pas m'empêcher de me poser cette question.

> Que pourrions-nous accomplir dans ce monde en constante évolution en 12 mois ?

« Mardi 20 janvier 2015, 17h10, le produit AntiMalware passe enfin en bêta publique. »

Après des heures sans dormir, la première note de version qui donnerait le coup d'envoi à notre nouveau voyage a été publiée sur le site web.

Je travaillais pour l'une des petites entreprises de cybersécurité qui fournissent des logiciels de sécurité pour les utilisateurs finaux et les entreprises. Notre logiciel protège les utilisateurs contre les logiciels malveillants. Il nettoie leur ordinateur s'ils sont infectés. Notre AntiMalware en faisait partie.

Les retours et impressions de la première version bêta étaient prometteurs. Nous étions quatre développeurs, travaillant sur ce produit et corrigeant constamment les bugs, itérant de nouvelles versions en améliorant le produit.

#### **Première version stable**

Après deux mois de travail sur la correction de bugs, l'amélioration et le codage, nous avons publié la première version stable d'AntiMalware.

Que disaient les utilisateurs ?

La plupart des retours de nos utilisateurs étaient excellents, et ils aimaient le produit. Cela maintenait notre équipe motivée. Nous travaillions activement sur le produit pour améliorer nos fonctionnalités principales.

#### **L'avion décolle.**

2016-2017.

Nos années dorées avant la grande tempête.

AntiMalware vivait ses meilleurs moments. Il devenait notre produit phare. Les utilisateurs le recommandaient à leurs amis. Chaque blog et forum lié à la sécurité recommandait notre logiciel. C'était la première option lorsqu'il s'agissait de sauver les utilisateurs infectés.

Téléchargements, installations, ventes.

Chaque métrique était en hausse, la base d'utilisateurs grandissait rapidement sur plusieurs mois. Les fondateurs étaient heureux, l'équipe aussi. C'était le grand succès que l'entreprise recherchait. Tout le monde pensait : « Nous l'avons fait ! Comme les autres grandes entreprises, nous pensions avoir créé notre propre histoire de succès. »

#### **Nouvelles opportunités (du moins, nous le pensions) : Entrée sur le marché de l'entreprise**

L'entreprise a décidé de se lancer sur le marché de l'entreprise. Nous constituions une nouvelle équipe pour le produit corporate. Le propriétaire du produit AntiMalware quittait l'équipe. Notre CTO prenait la responsabilité et devenait le nouveau propriétaire. (Grosse erreur. Je vais expliquer pourquoi).

Certains développeurs quittaient l'entreprise, mais ce n'était pas grave. Nous gérions tout bien et AntiMalware était toujours la meilleure option sur le marché.

#### **Les bons jours étaient derrière nous. Affrontons la réalité.**

Comme je vous l'ai dit, notre CTO s'occupait de tout ce qui concernait AntiMalware. Il était le développeur principal, publiant constamment de nouvelles mises à jour et améliorant les capacités du produit. Cependant, en raison de sa position, il devait également gérer d'autres affaires de l'entreprise.

Bien sûr, au début, tout se passait bien. Comme dans tout processus de développement, dans notre cas aussi, nous devions continuer à maintenir et à améliorer notre logiciel.

Comme nous aurions dû nous y attendre (ce qui n'était clairement pas le cas), d'une manière ou d'une autre, le processus de développement a commencé à ralentir.

Les jours où nous publiions de nouvelles mises à jour étaient derrière nous. À ce moment-là, nous vivions la réalité des mises à jour tardives et bientôt plus de mises à jour du tout. Cela m'a beaucoup énervé et un jour j'ai demandé à notre CTO :

> « Qu'est-ce qui ne va pas avec ce produit ? 
> Pourquoi les mises à jour prennent-elles trop de temps et le développement ralentit-il ? »

Il a pris une profonde inspiration et a commencé à parler :

« La base de code est vraiment compliquée. Elle n'est pas bien structurée et n'est pas faiblement couplée. L'architecture a été conçue de manière totalement erronée. L'interface utilisateur et la logique principale interfèrent l'une avec l'autre. Chaque fois que je corrige un bug ou que je change quelque chose, cela affecte d'autres parties du logiciel. Même les petits changements sont difficiles à faire. Avec chaque nouvelle mise à jour, quelque chose de nouveau apparaît. 

Il y a des méthodes qui prennent 20 paramètres, elles font deux pages de long ! Pouvez-vous imaginer ? Il y a beaucoup de choses qui n'auraient pas dû être implémentées mais qui l'ont été quand même. 

C'est pourquoi chaque mise à jour prend trop de temps et je ne peux pas implémenter une nouvelle fonctionnalité. Si nous publions une nouvelle mise à jour, j'ai peur que nous introduisions de nouveaux bugs et que nous cassions la fonctionnalité principale du programme qui fonctionne bien maintenant. C'est pourquoi il est trop risqué pour nous de publier une nouvelle mise à jour. Nous pouvons perdre nos utilisateurs. Nous pouvons perdre notre produit aussi. »

Une bouffée de réalité est sortie de sa part et nous le savions tous. En fait, nous attendions cette réponse de sa part.

Mais il y avait une autre chose à demander. Il avait dirigé le précédent développeur principal qui avait dirigé le produit pendant un an, alors comment le code pouvait-il être aussi désordonné ?

« Je ne voulais pas briser sa motivation. Nous devions entrer sur le marché des anti-malwares le plus rapidement possible et il était bon dans ce domaine. C'est pourquoi je ne voulais pas l'arrêter. »

En gros, nous avons sacrifié la base de code pour entrer sur le marché le plus rapidement possible, mais cela a détruit l'avenir de notre produit.

**Leçon apprise** : N'hésitez pas à dire « c'est de la m*** » si quelque chose est vraiment de la m***. L'avenir de votre produit est plus important que votre code spaghetti. Concentrez-vous sur avoir un produit durable.

#### **Comment pouvons-nous corriger ce code terrible ?**

> « Nous sommes des programmeurs. Les programmeurs sont, dans leur cœur, des architectes, et la première chose qu'ils veulent faire lorsqu'ils arrivent sur un site est de raser l'endroit et de construire quelque chose de grand. Nous ne sommes pas excités par la rénovation incrémentale : bricoler, améliorer, planter des parterres de fleurs. » 
> 
— [Joel Spolsky](https://www.joelonsoftware.com/about-me/), PDG de Stackoverflow

Les développeurs ont toujours tendance à jeter le code et à recommencer. Il y a une raison à cela. La raison est qu'ils pensent que l'ancien code est inutile et désordonné. Mais encore une fois, nous pensons simplement ! Cependant, lorsque nous essayons de découvrir quelle est la vraie raison derrière cela, nous pouvons faire face au fait :

_Nous avons probablement tort !_

La raison pour laquelle l'ancien code peut sembler désordonné et doit être réécrit à partir de zéro n'est pas en fait à cause du code, mais plutôt à cause d'une loi cardinale, fondamentale de la programmation :

**Il est plus difficile de lire du code que d'en écrire.**

C'est pourquoi il est si difficile de réutiliser du code. C'est pourquoi nous pensons « C'est un gros gâchis ». C'est pourquoi notre subconscient murmure à nos oreilles « Jetez-le et recommencez » lorsque nous lisons le code d'un autre développeur.

Comme tout développeur, nous sommes tombés dans ce piège. Vérifier notre code désordonné une fois suffisait pour penser à le réécrire à partir de zéro.

Après une série de réunions, même si notre CTO était réticent à la réécriture du code (comportement correct), il a été convaincu à la fin et nous avons commencé la réécriture.

**Cependant, cette décision n'a pas duré trop longtemps…**

C'était un week-end. Dimanche. Je buvais mon café du matin et lisais quelques articles. Comme si mon fil d'actualité savait quoi me montrer, je suis tombé sur l'article le plus connu sur la réécriture du code. C'était [l'histoire de la réécriture de Netscape](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) écrite par [Joel Spolsky](https://www.joelonsoftware.com/about-me/).

Partager cet article avec le reste de l'équipe AntiMalware, y compris notre CTO, a été mon action immédiate après l'avoir lu.

Une autre discussion a commencé.

Il était déjà difficile de convaincre notre CTO de réécrire le code, mais après avoir lu cet article, il a changé d'avis. Il ne voulait pas exécuter cette décision. Les autres membres de l'équipe me criaient dessus :

« Pourquoi as-tu envoyé cet article ? Nous l'avions déjà convaincu. Ce produit doit être réécrit à partir de zéro. C'est la seule solution. »

Ainsi, notre première tentative a été finalisée et nous avons clos ce sujet de réécriture. Notre CTO croyait qu'il pouvait gérer ce code pourri et qu'il pouvait publier une nouvelle mise à jour. Ce sujet a été clos jusqu'à ce que la réalité nous frappe durement.

**Un an sans aucune mise à jour…**

**Vraiment, ce n'est pas une blague. Cela s'est produit !**

« Pourquoi pas de mise à jour ? »

« Cela fait des mois depuis la dernière mise à jour. »

Ces commentaires négatifs de nos utilisateurs sont devenus notre réalité. En tant que petite entreprise, nous avions trop de produits à gérer, et en plus, nous sommes entrés sur le marché de l'entreprise, ce qui nous a conduits à ce point.

Mélangez tout cela et vous obtenez un point : nous avons oublié nos utilisateurs.

Alors, imaginez. Nous ne voulions pas publier une nouvelle mise à jour parce que nous ne voulions pas perdre nos utilisateurs.

En fait, cela aurait dû être l'inverse : si nous ne publions pas de nouvelle mise à jour, nous allons définitivement perdre nos utilisateurs parce que nous ne leur avons pas donné de mise à jour depuis plus d'un an et demi.

Après que la réalité nous ait giflé au visage, nous avons décidé de revenir en arrière et pour nous, réécrire le logiciel était la seule option, alors nous l'avons fait.

**Aujourd'hui.**

« Lundi 17 décembre 2018, 21h40. L'e-mail était préparé pour être envoyé à notre groupe bêta privé. »

Après 12 mois épuisants, nous avons terminé notre processus de réécriture. Nous avons préparé la première note de version bêta, tout comme le premier jour où notre produit a rencontré le marché.

Nous voilà de nouveau…

La version réécrite du produit est toujours en bêta. Cela fait presque un mois. Nous corrigeons les bugs, écoutons nos utilisateurs, examinons les retours… Comme nous l'avons fait il y a 4 ans…

Qu'avons-nous manqué pendant ces 12 longs mois ? Qui sait ce que nous aurions pu faire au lieu de réécrire ?!

De nombreuses questions peuvent être posées à ce stade. Tout ce que je sais, c'est que la réécriture était la seule option pour nous ou nous ne voyions pas d'autre solution.

Si vous tombez dans ce piège et commencez à penser « Je devrais réécrire le logiciel à partir de zéro », envisagez de poser ces questions que je crois que tout développeur devrait poser avant de faire le premier pas vers la réécriture du code.

### 1. Êtes-vous prêt à jeter toute cette connaissance ?

Je demande sérieusement ! Soyez honnête avec vous-même et répondez à cette question : Êtes-vous vraiment prêt à jeter toute cette connaissance, toutes ces corrections de bugs collectées, des années de programmation. C'est ce à quoi vous vous attendez lorsque vous jetez le code et commencez à partir de zéro. Lorsque vous regardez la réécriture du code sous cet angle, c'est douloureux, n'est-ce pas ? Toutes ces nuits sans sommeil à essayer de corriger des bugs vous passent devant les yeux. Croyez-moi, je sais.

Vous avez dû parler à beaucoup d'utilisateurs pour trouver le problème qui a empêché votre logiciel de fonctionner correctement. Ensuite, vous avez dû trouver ce bug dans votre logiciel. Ensuite, vous avez dû reproduire le problème, puis trouver la correction, puis… et ainsi de suite.

### 2. Pouvez-vous garantir que vous allez faire un meilleur travail que la première fois ?

Il est important de garder à l'esprit que lorsque vous commencez à partir de zéro, il n'y a **aucune** **garantie** que vous allez faire un meilleur travail que la première fois.

Puisque vous avez choisi de jeter toute cette connaissance, les corrections de bugs collectées, il y a une forte possibilité que les mêmes bugs puissent réapparaître.

Probablement, l'équipe de réécriture sera différente de l'équipe qui a travaillé sur la première version. Donc vous n'avez pas réellement « plus d'expérience ». Vous allez simplement refaire la plupart des anciennes erreurs et introduire de nouveaux problèmes qui n'étaient pas dans la version originale.

Si vous ne planifiez pas bien le processus de réécriture, il y a un grand risque que la nouvelle version puisse être pire que la version originale pour résoudre le problème de votre client. Avec cette décision de réécriture, vous allez prendre ce risque qui peut vous faire perdre vos clients.

### 3. Êtes-vous prêt à offrir des mois/années à vos concurrents ?

Savez-vous exactement combien de temps vous avez besoin pour réécrire votre logiciel ?

Cela demande beaucoup d'efforts, de planification, de préparations. Vous allez planifier chaque tâche et sprint une par une et vous allez exactement connaître votre date limite pour terminer ce processus douloureux. Ou vous allez manquer la date limite. Qui sait ? Il y a une forte possibilité que vous ne terminiez pas ce processus à temps.

Vous allez être dans une position extrêmement dangereuse où vous devrez expédier une ancienne version du code pendant des mois ou des années, complètement incapable de faire des changements stratégiques ou de réagir aux nouvelles fonctionnalités que le marché exige parce que vous n'avez pas de code expédiable.

Vos clients pourraient bien vous abandonner parce que vous ne donnez rien de nouveau et que vous continuez à expédier votre ancien produit sans aucun changement.

Avez-vous pensé à cela ?!

### Leçons apprises en réécrivant le logiciel

> Réécrire un système à partir de zéro est essentiellement une admission d'échec en tant que concepteur. C'est faire la déclaration, « Nous avons échoué à concevoir un système maintenable et devons donc recommencer. » — [Max Kanat-Alexander](http://www.oreillynet.com/pub/au/5113), [Code Simplicity](http://shop.oreilly.com/product/0636920022251.do)

Ainsi, comme d'autres concepteurs, nous avons admis que nous avions échoué à concevoir notre logiciel et nous avons beaucoup appris de ce processus épuisant. Voici les leçons qui sont restées avec moi.

#### **Réécrire le code est une illusion de développeur, pas la solution dans la plupart des cas.**

Lorsque vous avez des problèmes avec votre code, il est important de diagnostiquer quel est exactement le problème. Comme tout développeur le ferait, votre première pensée ne devrait pas être la réécriture. Ce n'est qu'une illusion. C'est une illusion parce que vous avez du mal à lire le code de quelqu'un d'autre et vous pensez que vous feriez un meilleur travail si vous le réécriviez à partir de zéro. Dans ce cas, souvenez-vous toujours de la loi fondamentale de la programmation.

#### **Envisagez le refactoring avant de faire un pas vers la réécriture du code**

Les réécritures ciblées sont utiles pour traiter les pires offenses dans votre base de code. Ne faites pas une réécriture complète si vous pouvez limiter la portée et traiter la majorité de vos problèmes. Par exemple, le chargement de votre logiciel est trop lent. Mais cela n'affecte qu'une petite partie du projet. Ces problèmes peuvent être résolus, un à la fois, en déplaçant soigneusement le code, en le refactorant, en changeant les interfaces. Vous n'avez pas à tout réécrire.

#### **Attention. C'est un chemin plus long, plus difficile, plus sujet aux échecs que vous ne le pensez.**

Il y a un fait que les développeurs réalisent généralement après avoir manqué la date limite : _tout prend plus de temps que vous ne le pensez_. Soyez très pessimiste dans vos estimations sur le coût d'une réécriture. Cela coûte presque toujours plus et prend plus de temps que vous ne le pensez. Il y aura toujours beaucoup de complexité qui rendra le processus de réécriture plus difficile et plus douloureux. À la fin, la possibilité d'échec est difficile à manquer.

#### **Assurez-vous que le nouveau produit est meilleur pour résoudre le problème de l'utilisateur (ou au moins le même). Pire ne peut pas être acceptable.**

Les réécritures n'ont aucun effet/avantage direct pour le client. Vos utilisateurs ne se soucient pas de votre code. Ils veulent simplement résoudre leur propre problème. C'est tout. À leurs yeux, vous êtes réussi si votre produit résout leur problème. Sinon, ils n'utilisent pas le produit. Ils ne se soucient pas de votre décision de réécriture, donc la version réécrite doit au moins fonctionner aussi efficacement que l'ancienne.

#### **Continuez à maintenir et à supporter le produit existant.**

Dans notre cas, nous n'avons donné aucune mise à jour aux utilisateurs pendant un an. C'est trop long dans le monde dans lequel nous vivons aujourd'hui. Notre produit était toujours assez bon, mais les utilisateurs se plaignaient de l'absence de mises à jour. Ne cessez jamais de maintenir un système qui est actuellement en utilisation afin que les programmeurs puissent le réécrire. Pendant le processus de réécriture, l'ancien code doit encore être maintenu. Les petites mises à jour et les corrections de bugs doivent être données aux utilisateurs pendant que vous réécrivez l'ancien code. Sinon, vous risquez de perdre vos clients.

#### **Impliquez les utilisateurs dans le processus de conception dès que possible.**

Montrez toujours votre progression actuelle à vos utilisateurs finaux à intervalles réguliers afin qu'ils puissent vous aider à attraper les pires offenses. Il est important de rencontrer vos utilisateurs dès que possible. Leurs retours vous aideront à concevoir un nouveau produit basé sur leurs besoins. N'implémentez aucune fonctionnalité inutile. Cela vous évitera d'avoir une base de code compliquée.

#### **Gardez les équipes travaillant sur le produit synchronisées.**

Le produit ne concerne pas seulement l'équipe de programmation. Marketing, support, programmation, design… De nombreuses équipes travaillent dessus. Gardez-les synchronisées en leur donnant des mises à jour régulières sur le processus de réécriture.

Dans notre cas, nous avons traité de nombreux problèmes. Par exemple, l'équipe marketing préparait notre campagne bêta de produit et ils devaient savoir exactement ce qui se passait côté produit afin qu'ils puissent préparer les clients aux changements de produit à venir. Parfois, nous avons fait des changements sans les informer. Et cela les a obligés à préparer leur campagne à partir de zéro. Ne gaspillez le temps de personne de manière inefficace.

#### **Ne faites pas de changements dramatiques au produit.**

Il est important de connaître les points faibles et forts de votre produit. Ne changez pas les points forts, ceux aimés par les utilisateurs. Si les utilisateurs sont satisfaits de votre interface utilisateur, ne la changez pas. Faites des changements minimaux et de petites améliorations UX. Lorsque vous remplacez votre logiciel existant par le nouveau, vos utilisateurs ne doivent pas être confus avec les nouveaux changements dramatiques. Il y a de nombreux cas où les utilisateurs ont abandonné les nouveaux produits parce qu'ils n'ont pas trouvé la même fonctionnalité que celle fournie par le produit précédent. Ne laissez pas la même chose vous arriver.

#### **Ne faites pas dépendre votre produit d'un seul développeur.**

Dans notre cas, notre CTO était le développeur responsable de notre logiciel. En raison de sa position, le développement de notre produit avançait lentement. Même les petits changements prenaient plusieurs semaines, parfois des mois. Le point est de toujours continuer à avancer. Ne vous arrêtez jamais.

#### **Les migrations doivent être lentes et régulières.**

Remplacez votre logiciel original par le nouveau lorsque vous êtes sûr que le nouveau est prêt. Faites-le étape par étape.

Tout d'abord, commencez par un petit groupe bêta privé et expédiez votre produit à ce groupe. Collectez continuellement les retours et les rapports de plantage, corrigez les bugs, itérez de nouvelles versions et encore la même chose. Suivez ce cycle jusqu'à ce que vous soyez sûr que votre produit est prêt pour la bêta publique.

Lorsque vous passez en bêta publique, les retours vont être votre meilleur ami. Votre premier objectif ici devrait être de vous assurer que votre produit résout les problèmes des utilisateurs. Lorsque vous êtes sûr que vous fournissez la même fonctionnalité ou meilleure que l'ancien logiciel, le remplacement peut avoir lieu. Publiez le nouveau logiciel pour les nouveaux utilisateurs, et migrez vos utilisateurs existants vers le nouveau.

Ce sont les leçons clés que j'ai apprises de notre processus de réécriture. La réécriture est presque [_jamais_](http://www.joelonsoftware.com/articles/fog0000000069.html) la réponse. Plus souvent qu'autrement, le refactoring est un meilleur pari. Je conseille fortement l'approche lente de l'utilisation du refactoring. C'est moins risqué et vous gardez vos clients heureux.

### Quand réécrire le code

Il y a des moments où il est approprié de faire une réécriture. Si je pouvais faire une liste sur quand réécrire le code, ce serait ma liste :

**Passage à un autre langage ou plateforme (comme dans notre cas) :** Le langage est si ancien. Il est difficile de trouver un développeur ou vous devez payer beaucoup d'argent pour en obtenir un. Dans les deux cas, trop d'efforts.

**La base de code existante n'est plus maintenable (comme dans notre cas) :** Comment décidez-vous que votre code n'est pas maintenable ? C'est difficile à déterminer, mais si même les petits changements sont difficiles à faire, si les nouvelles mises à jour prennent plus de temps que d'habitude, si tout nouveau changement affecte d'autres parties du logiciel et introduit de nouveaux bugs, votre logiciel n'est pas maintenable.

**Vous avez les ressources disponibles pour maintenir le système existant et concevoir un nouveau système en même temps :** Ne cessez jamais de maintenir un système qui est actuellement en utilisation afin que les programmeurs puissent le réécrire. Les systèmes doivent toujours être maintenus s'ils sont en utilisation. Et n'oubliez pas que votre attention personnelle est également une ressource qui doit être prise en compte ici — avez-vous assez de temps disponible chaque jour pour être concepteur à la fois sur le nouveau système et l'ancien système simultanément, si vous allez travailler sur les deux ?

**Les développeurs de l'équipe sont un goulot d'étranglement pour le logiciel (comme dans notre cas) :** Cela ne devrait pas être une raison pour réécrire le code à partir de zéro. Vous pouvez toujours changer de développeurs au sein de l'équipe ou vous pouvez embaucher de nouveaux développeurs pour éliminer la situation de goulot d'étranglement.

Cependant, parfois, comme dans notre cas, il peut y avoir des moments où vous devez choisir l'option de réécriture. Notre logiciel était écrit avec une ancienne technologie et notre CTO était la seule personne responsable de son développement. Nous avons essayé de trouver un nouveau développeur, mais c'était difficile en raison de l'âge de cette plateforme de codage. Même si nous avions pu en trouver un nouveau, cela aurait été très coûteux pour nous. Donc, avec d'autres conditions, cela faisait partie de notre liste pour décider de réécrire le code.

**Le logiciel est de longue durée (je parle de 10 à 20 ans ou plus) :** La maintenance devient de plus en plus coûteuse avec le temps. Cela est dû au fait que le code devient de plus en plus spaghetti à mesure que l'architecture originale est sacrifiée pour des correctifs de maintenance rapides. De plus, les développeurs pour les technologies plus anciennes deviennent plus rares et plus chers. Enfin, le matériel commence à vieillir et il devient de plus en plus difficile de trouver du nouveau matériel, des systèmes d'exploitation, des frameworks, etc. pour faire fonctionner l'ancienne application. De plus, les entreprises évoluent, et il est probable qu'un système plus ancien ne répondra pas aux besoins commerciaux de l'organisation.

Vous devez donc peser tous les coûts de maintenance en cours, ainsi que les avantages potentiels d'un nouveau système, par rapport au coût de sa réécriture à partir de zéro.

Si votre cas correspond à un ou plusieurs des points ci-dessus, vous pouvez être dans une situation où il est acceptable de réécrire. Sinon, la bonne chose à faire est de gérer la complexité du système existant sans réécriture, en améliorant la conception du système dans une série d'étapes simples.

Réécrire votre code à partir de zéro pourrait être la plus grosse erreur que vous faites, mais de même, ne pas réécrire votre code pourrait conduire au même résultat. Voici un conseil. Le refactoring devrait être la première option.

Certains développeurs continueront à croire que tous les systèmes doivent éventuellement être réécrits. Gardez toujours à l'esprit que ce n'est pas vrai. Il est possible de concevoir un système qui n'a jamais besoin d'être jeté. Il y aura toujours un concepteur de logiciels autour de vous disant « Nous devrons tout jeter un jour de toute façon ». Mais si le logiciel est bien construit dès le départ et ensuite correctement maintenu, pourquoi devrait-il être jeté ?

_Publié à l'origine sur [huseyinpolatyuruk.com](https://huseyinpolatyuruk.com/lessons-learned-from-rewriting-code-in-my-10-years-as-a-developer/)._

**Chaque ? est le bienvenu si vous avez aimé cet article !**

**J'écris sur la programmation, la technologie, l'IA, les startups et le développement personnel. Si vous [me suivez sur Twitter](https://twitter.com/h_polatyuruk), je ne gaspillerai pas votre temps avec des publications inutiles. ?**