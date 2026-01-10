---
title: Apprendre la Programmation Orientée Objet avec Python
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-13T19:32:00.000Z'
originalURL: https://freecodecamp.org/news/learn-object-oriented-programming-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/oop.jpeg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: youtube
  slug: youtube
seo_title: Apprendre la Programmation Orientée Objet avec Python
seo_desc: "Object Oriented Programming is an important concept in software development.\
  \ \nObject Oriented Programming (OOP) is a programming paradigm that relies on the\
  \ concept of classes and objects. You can use this method of writing programs in\
  \ many programmi..."
---

La Programmation Orientée Objet est un concept important dans le développement logiciel.

La Programmation Orientée Objet (POO) est un paradigme de programmation qui repose sur le concept de classes et d'objets. Vous pouvez utiliser cette méthode d'écriture de programmes dans de nombreux langages de programmation, y compris Python.

Nous venons de publier un cours complet sur la Programmation Orientée Objet en Python sur la chaîne YouTube freeCodeCamp.org.

Jim de JimShapedCoding a développé ce cours. Jim a créé de nombreux cours populaires et est un excellent enseignant.

Dans ce tutoriel complet, vous apprendrez tout sur la POO et comment l'implémenter en utilisant Python.

Voici les sections couvertes dans ce cours :

* Commencer avec les Classes
* Constructeur, __init__
* Méthodes de Classe vs Méthodes Statiques
* Héritage
* Getters et Setters
* Principes de la POO

Regardez le cours complet ci-dessous ou sur la [chaîne YouTube freeCodeCamp.org](https://youtu.be/Ej_02ICOIgs) (2 heures de visionnage).

%[https://youtu.be/Ej_02ICOIgs]

## Transcription

(générée automatiquement)

Il est important pour les développeurs logiciels de comprendre la programmation orientée objet.

Dans ce cours, Jim de JimShapeCoding vous enseignera tout sur la programmation orientée objet et la programmation orientée objet en Python, cela pourrait être ce qui vous retient d'être un excellent développeur Python.

Et ainsi que de décrocher votre premier emploi en tant qu'ingénieur logiciel, Bienvenue à tous au cours de programmation orientée objet en Python.

Maintenant, si vous avez du mal à comprendre les concepts de la programmation orientée objet dans le passé, alors vous êtes totalement bien.

Et vous êtes entre de bonnes mains.

Parce que dans ce cours, je vais m'assurer que ce sera le dernier tutoriel que vous regarderez jamais sur les classes et les concepts complexes qui viennent avec la programmation orientée objet.

Et nous allons faire cela en développant une véritable application Python, qui sera très cool à écrire.

Et nous ajouterons à sa complexité étape par étape.

Et tout au long du chemin, nous comprendrons tout ce que nous devons savoir sur la programmation orientée objet.

Maintenant, il y aura certaines exigences pour ce cours, je m'attends à ce que tout le monde connaisse au moins les fonctions, les variables, les instructions if et ainsi que les boucles for.

Et si vous connaissez ces choses à partir d'autres langages de programmation, alors c'est aussi bien.

Alors, cela dit, commençons.

Maintenant, pour expliquer pourquoi vous devriez écrire des programmes orientés objet, je vais expliquer les concepts basés sur un système de gestion de magasin que nous commencerons à développer ensemble.

Alors, en commençant à réfléchir à la manière de faire nos premiers pas avec un tel problème, nous pourrions d'abord penser à suivre les articles que nous avons actuellement dans notre magasin.

Donc, une façon de commencer, nous pourrions créer ces quatre variables pour commencer à suivre nos articles.

Donc, comme vous pouvez le voir, nous avons notre première variable item one égale à phone.

Et puis nous avons trois variables supplémentaires qui commencent intentionnellement avec le préfixe item one, afin que nous puissions décrire que ces quatre variables sont liées les unes aux autres en suivant les conventions de nommage correctes.

Maintenant, vous pourriez penser que ces quatre variables sont liées les unes aux autres uniquement parce qu'elles utilisent le même préfixe item one.

Pour Python, ce sont juste quatre variables avec différents types de données.

Donc, si nous devions imprimer le type, pour chacune de ces quatre variables, maintenant, nous allons recevoir leurs types sans surprises, n'est-ce pas, nous allons recevoir string, et integer pour le prix, la quantité et le prix total.

Maintenant, je veux me concentrer sur ces sorties spécifiques maintenant, car comme vous pouvez le voir, pour chacun des types, nous voyons également le mot clé de classe.

Cela signifie que ces types de données sont en fait des instances de chaînes de caractères ou d'entiers.

Donc, dans le langage de programmation Python, chaque type de données est un objet qui a été instancié plus tôt par une certaine classe.

Et pour la variable item one qui a été instanciée à partir d'un type de classe string.

Et pour le prix, la quantité et le prix total, ceux-ci ont été instanciés à partir d'une classe nommée Iand, signifiant integer.

Donc, cela aurait pu être mieux.

Si nous appelons le tail Python que nous voulons créer un type de données à nous, il nous permettra d'écrire un code que nous pourrons réutiliser facilement à l'avenir si nécessaire.

Maintenant, chaque instance pourrait avoir des attributs pour décrire des informations connexes à son sujet.

Et nous pouvons penser à au moins quelques bons candidats pour les attributs que nous pourrions avoir pour notre type de données item, comme son nom, son prix ou sa quantité.

D'accord, alors allons-y et commençons à créer notre première classe.

Donc, je vais nettoyer tout ici, et nous allons continuer avec cela.

Cela va être divisé en deux parties, la première sera la création de la classe.

Et la seconde sera la partie où je vais instancier certains objets de cette classe.

Maintenant, lorsque je dis créer une instance, ou créer un objet, je veux dire essentiellement la même chose, donc vous pourriez m'entendre dire l'une de ces choses.

D'accord, alors allons-y et disons class.

Et puis cela doit être suivi par le nom de la classe que vous souhaitez créer.

Donc, nous aimerions lui donner le nom d'item.

Et puis à l'intérieur de cette classe, à l'avenir, nous allons écrire un code qui sera très bénéfique et très utile pour nous.

Donc, nous ne nous répéterons pas chaque fois que nous aimerions prendre des actions similaires.

Mais pour l'instant, temporairement, je vais dire ici un pass pour que nous ne recevions aucune flèche à l'intérieur de cette définition de classe.

D'accord, donc maintenant que nous avons créé notre classe, nous sommes autorisés à créer certaines instances de cette classe.

Donc, allons-y et disons item one est égal à item.

Et cette action est équivalente à créer une instance d'une classe, tout comme si vous deviez créer une chaîne aléatoire, alors vous diriez quelque chose comme ce qui suit.

Cela est équivalent à celui-ci également.

Donc, il est très important de comprendre comment les classes fonctionnent en Python.

Donc, je vais supprimer cette ligne car ce n'était qu'un exemple.

Et maintenant, j'ai dit que nous sommes autorisés à assigner certains attributs aux instances d'une classe.

Donc, allons-y et commençons à créer des attributs.

Et cela sera réalisable en utilisant le signe point juste après l'instance d'une classe.

Et ici, vous pouvez dire que vous voulez lui donner un attribut, comme un nom, qui sera égal à phone, et item one, ce prix pourrait être égal à 100.

Et je pense que item one dot quantity pourrait être égal à cinq, par exemple.

Maintenant, à ce stade, vous pourriez vous demander, quelle est la différence entre les variables aléatoires que nous avons créées et ces quatre lignes ? Eh bien, ici, nous avons en fait une relation entre ces quatre lignes, car chacun des attributs est assigné à une instance de la classe.

Et je pourrais probablement faire cela en allant de l'avant et en essayant d'imprimer les types de item one nil, ainsi que les types des attributs de nom, prix et quantité.

Maintenant, avec le nom, le prix et la quantité, nous n'allons pas avoir de surprises car nous assignons des attributs de type chaîne à l'objet item.

Mais si nous devions imprimer cela, puis vérifier le résultat si j'exécutais ce programme, vous pouvez voir que maintenant nous avons un type de données d'item ici.

Et c'est la grande différence entre ce que nous avons vu précédemment et cette chose que nous venons de créer.

Donc maintenant nous comprenons comment nous pouvons créer nos propres types de données.

Maintenant, allons-y et voyons quels sont les autres avantages de l'utilisation de la programmation orientée objet.

D'accord, donc jusqu'à présent, nous avons compris comment assigner des attributs aux instances, nous devrions également comprendre maintenant comment nous pouvons créer certaines méthodes et les exécuter sur nos instances.

Maintenant, si nous prenons comme exemple la classe de construction de chaîne, alors vous savez que nous avons certaines méthodes que nous pouvons aller de l'avant et exécuter pour chacune de nos chaînes.

Et pour cet exemple, vous pouvez voir que j'ai pris une instance d'une chaîne que j'ai nommée random str, puis je vais de l'avant à la ligne suivante et exécute la méthode opera, qui, si vous vous souvenez, il est possible de prendre toutes les lettres et de les transformer en majuscules.

Maintenant, la plus grande question ici est comment nous pouvons aller de l'avant et concevoir certaines méthodes qui seront autorisées à s'exécuter sur nos instances, Eh bien, la réponse est à l'intérieur de notre classe.

Donc, nous pourrions aller à l'intérieur de notre classe et écrire certaines méthodes qui seront accessibles à partir de nos instances.

Donc, nous pourrions aller de l'avant et dire cela et donner à notre méthode un nom.

Maintenant, un bon candidat pour une méthode que nous aimerions créer maintenant est en fait calculate total price, car comme nous le comprenons, cela aurait pu être bien.

Si nous avions une méthode qui irait de l'avant et calculerait le résultat, en multipliant item one dot price par item one dot quantity, afin que nous puissions obtenir le prix total pour cet item spécifique.

Maintenant, avant d'aller de l'avant et de compléter cette fonction, je vais juste créer une autre instance de cet item en supprimant également ces deux lignes, car nous avons compris l'exemple.

Donc, je vais simplement changer celles-ci en item two, comme cela.

Et je vais utiliser quelque chose comme laptop et changer le prix à 1000.

Et dire que nous en avons trois de ceux-ci.

Maintenant, juste une rapide note de côté, lorsque vous m'entendrez dire méthodes, alors je veux dire deux fonctions qui sont à l'intérieur des classes.

Parce qu'en termes de Python, ou dans n'importe quel langage de programmation, lorsque vous avez des définitions isolées avec ce mot-clé, alors celles-ci sont considérées comme étant appelées fonctions.

Mais lorsque vous allez de l'avant et créez ces fonctions à l'intérieur des classes, alors celles-ci sont appelées méthodes.

Donc, c'est un point important que vous devriez comprendre, car je vais appeler celles-ci méthodes à partir de maintenant.

D'accord, donc maintenant si j'étais continuer en ouvrant et en fermant ces parenthèses, alors vous allez voir un paramètre qui est autogénéré que Python veut que nous recevions intentionnellement.

Maintenant, la raison pour laquelle cela se produit, Python passe l'objet lui-même comme premier argument, lorsque vous allez de l'avant et appelez ces méthodes.

Maintenant, si j'étais aller ici, et dire item one dot calculate total price, alors l'action que nous faisons maintenant est d'appeler cette méthode.

Mais lorsque vous allez de l'avant et appelez une méthode à partir d'une instance, alors Python passe l'objet lui-même comme premier argument à chaque fois.

Donc, c'est pourquoi nous ne sommes pas autorisés à créer des méthodes qui ne recevront jamais de paramètres.

Maintenant, vous verrez cela si j'étais supprimer le premier paramètre, et dire quelque chose comme pass.

Maintenant, si j'étais exécuter ce programme maintenant, alors vous allez voir type zéro, calculate total price prend zéro arguments positionnels, mais un a été donné.

Donc, en termes simples, ce que cette exception dit, c'est que Python essaie de passer un argument et vous ne le recevez pas en utilisant un paramètre, donc c'est très problématique.

Et c'est pourquoi vous devez toujours recevoir au moins un paramètre lorsque vous allez de l'avant et créez vos méthodes.

Maintenant, puisque nous recevons toujours ce paramètre, alors il est juste une approche commune de l'appeler self.

C'était bien si j'étais l'appeler quelque chose comme my perm, ou je ne sais pas quelque chose d'autre.

Mais vous ne voulez jamais vous tromper avec les conventions communes entre différents développeurs Python.

Donc, c'est pourquoi assurez-vous simplement que vous le laissez comme self à chaque fois.

Maintenant, si j'étais aller de l'avant et exécuter ce programme, alors vous allez voir que nous ne allons pas recevoir d'erreurs.

Donc, cela signifie que cette méthode a été implémentée correctement.

Maintenant, voyons comment nous allons bénéficier de la création de cette méthode, car elle devrait aller de l'avant et créer un calcul pour nous en utilisant le prix et la quantité.

Donc, je vais intentionnellement recevoir ici deux paramètres supplémentaires, que nous pourrions nommer x&y pour l'instant.

Et nous pourrions simplement dire return x multiplié par y.

Et maintenant, je vais aller de l'avant et passer ici deux arguments supplémentaires.

Et ce sera item one dot price.

Le second sera quantity.

Donc, cela va fonctionner car lorsque vous appelez cette méthode en arrière-plan, Python passe cela comme un argument.

Et puis il passe le deuxième argument.

Et cela a été passé comme un troisième argument.

Donc, c'est parfait.

Et si j'étais exécuter cela, et en fait imprimer cela, donc excusez-moi pour avoir exécuté cela avant de l'imprimer, donc je vais entourer cette expression avec cette fonction intégrée print.

Et je vais exécuter cela et vous allez voir 500 comme prévu, maintenant je pourrais faire exactement la même chose pour calculer le prix total de notre deuxième item.

Donc, si j'étais prendre cela et coller cela dans cette ligne, et en fait changer cela en item two, et changer celui-ci en item two, ainsi que celui-ci, alors je vais recevoir 3000 comme prévu.

Et c'est ainsi que vous pouvez créer une méthode.

D'accord, donc jusqu'à ce point, nous avons compris que nous pouvons assigner des attributs ainsi que créer certaines méthodes que nous pouvons aller de l'avant et utiliser directement à partir de nos instances, comme ces deux exemples dans cette ligne, ainsi que dans cette ligne.

Maintenant, dans cet épisode, nous allons résoudre quelques problèmes supplémentaires que nous avons en termes de meilleures pratiques en programmation orientée objet, et des choses que vous allez voir dans chaque projet basé sur Opie.

D'accord, alors commençons.

Maintenant, l'un des premiers problèmes que nous avons ici est le fait que nous n'avons pas de ensemble de règles pour les attributs que vous aimeriez passer afin d'instancier une instance avec succès.

Et ce que cela signifie, cela signifie que pour chaque item que je veux aller de l'avant et créer, je dois coder en dur l'attribut de nom comme ceux-ci ici.

Et cela aurait pu être mieux si nous appelions d'une certaine manière la déclaration de la classe que pour instancier une instance avec succès, le nom, le prix et la quantité doivent être passés, sinon, l'instance n'aurait pas pu être créée avec succès.

Donc, ce que cela signifie, cela signifie qu'il aurait pu être une excellente option si nous pouvions d'une certaine manière exécuter quelque chose en arrière-plan.

La seconde que nous instancions une instance et il y a un moyen d'atteindre un tel comportement.

Et cela en créant une méthode spéciale avec un nom très unique, qui est appelée double underscore init double underscore.

Maintenant, vous pourriez entendre ce terme également appelé constructeur.

En gros, c'est une méthode avec un nom unique que vous devez appeler de la manière intentionnelle afin d'utiliser ses fonctionnalités spéciales.

Maintenant, la manière dont cela va fonctionner est en le créant de la manière suivante.

Donc, ce sera double underscore.

Et comme vous pouvez le voir, j'ai déjà une complétion automatique pour certaines méthodes très spéciales qui commencent et se terminent par un double underscore.

Maintenant, la collection de ces méthodes est utilisée pour être appelée Méthodes Magiques.

Et nous allons apprendre beaucoup plus de méthodes magiques que vous avez dans Opie, mais la première que nous allons commencer sera l'init double underscore, comme cela.

D'accord, donc maintenant que nous avons créé cette méthode, voyons ce que cette méthode fait en arrière-plan.

Donc, lorsque vous allez de l'avant et créez une instance d'une classe, alors Python exécute cette fonction double underscore init automatiquement.

Donc, ce que cela signifie, cela signifie que maintenant que nous avons déclaré notre classe, Python va parcourir cette ligne.

Et puis, puisque une instance a été créée, et nous avons une méthode double underscore init conçue, alors elle va appeler les actions qui sont à l'intérieur de cette méthode double underscore init double underscore.

Maintenant, afin de prouver cela, je vais commencer avec un point très basique ici qui dira I am created Comme cela.

Maintenant, nous avons ici une instance.

Et ici, nous en avons une autre.

Donc, nous devrions voir I am created deux fois.

Et afin d'éviter les confusions, je vais supprimer ces lignes d'impression d'ici pour que nous puissions voir une image plus propre.

D'accord, donc si nous devions exécuter notre programme, alors nous pouvons voir que nous avons I am created deux fois.

Et c'est parce que Python a appelé cette méthode double underscore init double underscore deux fois, grâce à ces deux instances que nous avons créées.

D'accord, donc maintenant que nous utilisons la fonction double underscore init dans cette classe, nous devrions en tirer profit et résoudre quelques problèmes supplémentaires afin d'implémenter les meilleures pratiques d'Opie.

Maintenant, si vous vous souvenez, au début de ce tutoriel, j'ai dit que l'un des problèmes que nous avons jusqu'à ce point est le fait que nous codons toujours en dur les attributs de cette manière en disant dot name, dot price dot quantity.

Et c'est quelque chose que nous pouvons certainement éviter.

Maintenant, voyons comment nous pouvons commencer à éviter de créer ces attributs codés en dur pour chacune des instances ici.

Donc, nous pouvons en fait tirer profit de la méthode double underscore init que nous avons conçue.

Et voyons comment maintenant nous comprenons que pour chaque instance que nous allons créer, elle va de l'avant et appelle cette méthode double underscore init automatiquement.

Donc, ce que cela signifie, cela signifie que non seulement nous pouvons nous permettre de recevoir le paramètre self, car c'est une chose obligatoire que nous devrions faire, car Python en arrière-plan, passe l'instance elle-même comme premier argument, nous pourrions, en plus, prendre quelques paramètres supplémentaires, et puis faire quelque chose avec eux.

Donc, comme un soldat, disons que nous aimerions recevoir un paramètre supplémentaire que nous pourrions nommer name.

Et comme vous pouvez le voir, automatiquement, Python va se plaindre de la manière dont l'argument name n'est pas rempli ici.

Donc maintenant, je pourrais aller de l'avant et passer l'argument de phone pour celui-ci.

Et pour le second, je peux aller de l'avant et passer l'argument de laptop.

Maintenant, une fois que j'ai créé cela, alors je peux en fait aller de l'avant et changer ma ligne d'impression un peu.

Donc, ce sera une ligne d'impression unique où je peux identifier d'où vient chaque ligne d'impression.

Donc, je peux aller de l'avant et dire une instance créée et utiliser une colonne ici et puis faire référence au nom comme cela.

Et maintenant que nous avons créé cela, alors si nous devions exécuter notre programme, alors vous allez voir des phrases uniques, une instance créée pour le phone, et ainsi que pour le laptop.

D'accord, donc maintenant que nous avons fait cela, alors il y a quelque chose qui n'est toujours pas tout à fait parfait, car nous passons toujours l'attribut de name ici et ici.

Donc maintenant, faites attention à la manière dont la méthode init doit recevoir le self comme paramètre également.

Et nous connaissons déjà les raisons pour cela.

Et le fait que nous ayons self comme paramètre ici pourrait en fait nous permettre d'assigner les attributs à partir de la méthode init, afin que nous n'ayons pas à aller de l'avant et à assigner l'attribut de name pour chacune des instances que nous créons.

Donc, ce que cela signifie, cela signifie que je peux assigner dynamiquement un attribut à une instance à partir de cette méthode magique, qui est appelée double underscore in it.

Donc, si j'étais dire, self, dot name, donc j'assigne l'attribut de name à chaque instance, qui va être créée ou créée, et je fais cela pour qu'il soit égal au name qui est passé de ici.

Donc, ce que cela signifie, cela signifie que maintenant je peux me permettre de supprimer cette ligne.

Et puis cette ligne.

Donc, comme vous pouvez le voir, maintenant j'ai une assignation d'attribut dynamique, grâce au self dot name equals name que nous avons écrit ici dans le to test that the attribute assignment world, alors je peux descendre ici et utiliser deux lignes supplémentaires qui ressembleront à ce qui suit.

Donc, je vais imprimer it one dot name, et je vais aussi imprimer item to that name.

Et afin d'éviter les confusions, alors je vais me débarrasser de cette ligne.

Donc, nous pourrions seulement voir les lignes d'impression d'ici.

Et maintenant, si j'étais exécuter cela, alors vous pouvez voir que nous recevons un phone et un laptop.

Donc, cela signifie que nous avons été capables d'assigner les attributs dynamiquement.

Et c'est parfait.

Et maintenant que nous avons l'idée de cela, alors nous devrions aussi faire de même pour le reste des attributs que nous aimerions recevoir.

Donc, nous avons aussi le prix et la quantité à gérer.

Donc, je vais aller à ma méthode init, et je vais recevoir à nouveau, le prix et la quantité.

Et je vais faire exactement la même chose.

Donc, je vais assigner l'attribut de prix.

Et cela sera égal au prix.

Et la quantité sera égale à la quantité.

Et vous pouvez aussi voir que Python se plaint à nouveau du prix et de la quantité qui ne sont pas passés ici.

Donc, je peux dire 100 et puis cinq, et puis je peux supprimer ceux-ci.

Et puis je peux faire la même chose ici.

Je pourrais passer In 1000, et puis trois, et supprimer ceux-ci, et pour prouver que cela va fonctionner, alors je vais me copier quelques fois et changer cela en quantité, je veux dire prix, celui-ci sera prix aussi.

Celui-ci sera quantité et celui-ci aussi.

Maintenant, si j'étais exécuter cela, alors vous pouvez voir que les résultats sont comme prévu.

Donc, c'est une façon dont vous devriez travailler avec la méthode double underscore init, vous devriez toujours prendre soin des attributs que vous voulez assigner à un objet à l'intérieur de la méthode double underscore init, c'est-à-dire à l'intérieur du constructeur.

Maintenant, quelques signes qui sont assez importants à retenir lorsque nous travaillons avec des classes.

Maintenant, lorsque nous utilisons la méthode Ws coordinate, cela ne signifie pas que nous ne pouvons pas différencier les paramètres obligatoires des paramètres non obligatoires.

Donc, disons que vous ne savez pas actuellement combien vous avez d'un article spécifique, alors vous pouvez aller de l'avant et par défaut, recevoir ce paramètre de quantité comme zéro, car c'est une situation réaliste où vous ne savez pas actuellement combien de téléphones vous avez dans votre magasin.

Donc, nous pouvons directement aller de l'avant et utiliser une valeur par défaut pour cela, par exemple, zéro, et cela signifiera que vous n'aurez pas à passer ces cinq et trois ici.

Et maintenant, pour vous montrer les résultats de cela, si j'étais exécuter notre programme, alors vous pouvez voir que nous recevons zéro deux fois pour ces deux impressions ici.

Donc, c'est quelque chose que vous voudrez retenir.

Et un autre point assez important dont je voudrais parler maintenant est le fait que vous pouvez assigner des attributs à des instances spécifiques individuellement.

Donc, disons que vous voulez savoir si le laptop a un pavé numérique ou non, car certains laptops n'ont pas le pavé numérique sur le côté droit du clavier.

Mais ce n'est pas un attribut réaliste que vous aimeriez assigner à un téléphone.

Et c'est pourquoi vous pouvez aller de l'avant et me laisser supprimer ces lignes d'impression, au fait.

Et c'est pourquoi vous pouvez aller de l'avant et dire quelque chose comme item two that has numpad equals to false comme cela.

Et c'est quelque chose que vous voulez retenir, car le fait que vous utilisiez certaines assignations d'attributs dans le constructeur ne signifie pas que vous ne pouvez pas ajouter d'autres attributs que vous aimeriez après avoir instancié les instances que vous aimeriez.

D'accord, donc maintenant que nous avons compris cela, alors il reste encore un petit problème que nous devons résoudre.

Maintenant, faites attention à la manière dont le calculate total price reçoit toujours les x et y comme paramètres.

Et la question que nous nous posons maintenant est pourquoi il reçoit toujours ces paramètres.

Eh bien, nous pourrions certainement maintenant ne pas recevoir ces paramètres.

Parce que comme nous le savons, pour chaque méthode que nous concevons dans les classes, alors l'objet lui-même est passé en argument.

Et je sais que je l'ai répété plusieurs fois.

Mais c'est là que j'ai échoué à comprendre les classes.

Donc, c'est pourquoi il est très important de comprendre ce comportement.

Et nous savons déjà que l'objet lui-même est passé comme argument.

Donc, c'est pourquoi nous recevons self.

Et donc, cela signifie que maintenant nous pourrions simplement retourner self dot price multiplié par self dot quantity.

Et cela signifiera que nous n'avons pas vraiment à recevoir ces paramètres, car nous assignons ces attributs, une fois que les instances ont été créées.

Donc, cela signifie que nous avons accès à ces attributs à travers les méthodes que nous allons ajouter ici dans cette classe à l'avenir.

Donc, pour tester que cela fonctionne, je vais supprimer cet exemple pour l'instant.

Et je vais dire print item one dot, calculate total price.

Donc, nous pourrons retourner le résultat ici.

Et je vais faire de même pour item two, désolé, seulement celui-ci.

Maintenant, pour montrer un vrai nombre autre que zéro, alors je vais passer ici, des quantités.

Donc, je vais dire un et trois, par exemple, car je ne veux pas multiplier un grand nombre qui est zéro.

Et cela pourrait venir de ici.

Donc, je vais exécuter cela.

Et vous verrez que nous recevons les résultats attendus.

Donc, maintenant nous comprenons parfaitement le tableau général, comment travailler avec les constructeurs dans les classes, et quelles sont les meilleures pratiques que vous devriez aller de l'avant et implémenter.

D'accord, donc maintenant que nous avons compris cela, alors nous pourrions penser que nous avons tout fait parfaitement.

Mais en fait, je veux vous montrer ce qui se passera si nous devions passer ici une chaîne de caractères à côté d'un entier et exécuter notre programme.

Donc, si nous devions exécuter cela, alors vous pouvez voir que nous faisons des bêtises ici.

Parce que cette fonction, par exemple, pense qu'il a choisi d'imprimer la chaîne trois fois parce que vous verrez que nous avons 1000 multiplié par trois qui est retourné ici.

Donc, il nous montre 1000 une fois, 1000 deux fois, et puis une fois de plus.

Donc, ce que cela signifie, cela signifie que nous devons valider les types de données des valeurs que nous passons.

Donc, il y a quelques façons d'y parvenir.

Et une façon est d'utiliser les typages dans les paramètres que vous déclarez à l'intérieur ici, donc un bon début sera, par exemple, de déclarer que le nom doit être une chaîne de caractères.

Maintenant, laissez-moi d'abord prendre cela et changer ceux-ci en entier et puis aller ici et concevoir ces paramètres.

Donc, pour spécifier un typage, alors vous devriez aller de l'avant et créer un signe deux-points, suivi du type du type de données que vous attendez de recevoir ici.

Donc, si j'étais passer ici, seulement la référence d'objet à la classe de str, alors cela signifiera qu'il devra accepter uniquement les chaînes de caractères.

Et je peux prouver cela en changeant cela en un entier.

Et vous allez voir que nous avons une plainte ici qui dit expected type str God int instead.

Et c'est parfait.

Donc, maintenant que nous avons fait cela, alors je vais faire de même pour le prix lui-même.

Et le prix, nous pourrions en fait faire la même chose avec lui en passant float.

Maintenant, lorsque nous passons float, il est acceptable de passer également des entiers.

Et c'est quelque chose de très unique avec les floats et les entiers ensemble.

Donc, il est acceptable d'utiliser le typage de float.

Et pour la quantité, nous n'avons pas besoin de spécifier un typage, car le fait que nous ayons passé une valeur par défaut d'entier a déjà marqué ce paramètre comme étant toujours un entier.

Donc, c'est pourquoi, par exemple, si j'étais laisser cela tel quel et changer la quantité en une chaîne de caractères, alors vous allez voir que cela va se plaindre, car la valeur par défaut est déjà un entier.

Donc, il s'attend à un entier.

D'accord, donc ces choses sont en fait de grandes configurations pour rendre notre fonction init plus puissante.

Mais nous pourrions encore vouloir valider les valeurs reçues de la manière suivante.

Donc, disons que vous ne voulez jamais recevoir un nombre négatif de quantité.

Et vous ne voulez jamais recevoir un nombre négatif de prix.

Donc, c'est quelque chose que vous ne pouvez pas atteindre par les typages ici.

Mais il y a en fait une excellente façon de contourner cela.

Et cela sera en utilisant des instructions assert.

Maintenant, assert est un mot-clé d'instruction qui est utilisé pour vérifier s'il y a une correspondance entre ce qui se passe et vos attentes.

Donc, voyons comment nous pouvons travailler avec assert.

Donc, je vais en fait supprimer cela d'ici.

Et je vais organiser notre méthode init un peu, je vais dire ici un commentaire et je vais dire assign to self object.

Et je vais dire en haut quelque chose comme run validations to the received arguments.

D'accord, donc maintenant, c'est une excellente idée de valider que le prix et la quantité sont tous deux supérieurs ou égaux à zéro, car nous ne voulons probablement pas gérer ceux-ci lorsqu'ils sont des nombres négatifs et nous voulons planter le problème.

Donc, nous pourrions dire assert et faire attention que j'utilise cela comme une instruction, pas une fonction intégrée ou quelque chose comme cela.

Et je peux dire ici, price is greater than or equal to zero.

Maintenant, une fois que j'ai dit cela, alors je peux aussi faire de même pour quantity, en fait.

Donc, laissez-moi faire cela rapidement.

De cette manière, et puis une fois que nous avons cela, alors je peux en fait aller de l'avant et exécuter notre programme.

Et vous verrez que je ne vais pas recevoir de flèches.

Mais la seconde où je change cette quantité en moins un, par exemple, et celle-ci étant moins trois, alors j'aurai des flèches qui diront, assertion error.

Maintenant, vous pouvez voir que le fait que nous voyons ici, assertion error est une exception assez générale, qui ne signifie rien.

Maintenant, ce qui est si beau avec un tiers, vous pouvez ajouter vos propres messages d'exception juste à côté de celui-ci comme deuxième argument.

Donc, allons en haut ici et retournons à ces deux lignes.

Donc, le premier argument qui est passé à l'instruction est l'instruction que nous aimerions vérifier.

Mais si nous devions dire ici une virgule, et utiliser une chaîne pour dire, en fait une chaîne formatée, et je peux dire price et puis faire référence à la valeur de celui-ci n'est pas supérieur à zéro comme cela.

Ils peuvent ajouter un point d'exclamation ici, et ils peuvent utiliser la même chose.

Copiez cela avec une virgule et collez cela ici.

Et changez cela en quantité et puis faites référence à la valeur de celle-ci et dites qu'elle n'est pas égale à je veux dire supérieure ou égale à zéro.

Donc, nous devons en fait changer pour être supérieur ou égal à, comme cela.

Et il en va de même pour ici, et j'ai un espace ici qui sera supprimé.

D'accord, donc maintenant si j'étais exécuter notre programme, alors vous pouvez voir que nous recevons assertion error quantity minus one is not greater or equal than zero.

Donc, je devrais supprimer cela, puis ici pour cela, et maintenant c'est parfait.

Donc, maintenant nous comprenons que l'utilisation de l'instruction assert pourrait nous permettre de valider les arguments que nous recevons.

Et aussi, cela nous permet de rattraper les bugs dès que possible, avant de continuer avec le reste des actions que nous aimerions prendre dans ce programme.

Donc, laissez-moi en fait changer ceux-ci en valeurs valides comme cela.

Et c'est parfait.

D'accord, donc jusqu'à ce point, nous avons appris comment travailler avec le constructeur.

Et nous avons également appris comment assigner différents attributs aux instances qui vont être uniques par instance, ce qui signifie que vous pouvez aller de l'avant et créer autant d'instances que vous voulez, et vous avez le contrôle de passer les valeurs que vous aimeriez pour le nom, le prix et la quantité.

Maintenant, envisagez une situation où vous aimeriez utiliser un attribut qui sera global, ou à travers toutes les instances maintenant sont un bon candidat, par exemple, cela pourrait être une situation où vous aimeriez appliquer une vente sur votre boutique.

Donc, cela signifie que vous voulez aller de l'avant et avoir le contrôle d'appliquer une certaine remise pour chacun des articles.

Et c'est un bon candidat pour créer un attribut qui sera partagé à travers toutes les instances.

Maintenant, nous appelons ces types d'attributs, attributs de classe, et les types d'attributs que nous avons appris jusqu'à ce point est en fait appelé en un nom complet attributs d'instance.

Donc, concernant les attributs d'instance, nous savons tout, et nous avons appris comment travailler avec eux, mais nous n'avons pas travaillé avec l'autre type d'attributs, que nous allons faire dans ce tutoriel, qui est appelé à nouveau, un attribut de classe.

Donc, un attribut de classe est un attribut qui va appartenir à la classe elle-même.

Cependant, vous pouvez également accéder à cet attribut à partir du niveau d'instance également.

Allons-y et voyons un bon candidat pour un attribut de classe que vous voulez aller de l'avant et créer.

Donc, cela va être en allant à notre classe ici.

Et juste à la première ligne à l'intérieur de notre classe, je peux aller de l'avant et créer un attribut de classe.

Donc, allons-y et créons un attribut comme pay rate equals to 0.8.

Et la raison pour laquelle je fais cela est que j'ai dit qu'il y aurait 20% de réduction.

Donc, je veux probablement stocker un attribut qui décrira combien je dois encore payer.

Donc, je vais dire ici, le pay grade après 20% de réduction comme cela.

D'accord, donc maintenant que nous avons créé cela, voyons quelles sont les façons dont nous pouvons accéder à cet attribut.

Maintenant, si j'étais descendre et en fait supprimer l'une de celles-ci, et dire quelque chose à l'intérieur de cette ligne d'impression qui ressemblerait à ce qui suit.

Donc, je vais essayer d'accéder à la référence de la classe elle-même.

Donc, je ne vais pas créer une instance comme cela, en plus, je vais simplement apporter la référence au niveau de la classe elle-même.

Et je vais essayer d'accéder à cet attribut en disant le PE underscore rate.

Maintenant, si j'étais exécuter cela, alors vous allez voir que comme prévu, nous voyons cet attribut de classe, car c'est une façon dont vous pouvez accéder à ces attributs de classe.

Maintenant, cela pourrait être déroutant, mais j'ai dit il y a une minute que vous pouvez également accéder à ces attributs de classe à partir du niveau d'instance.

Eh bien, voyons si c'est vrai.

Donc, si j'étais dupliquer ces lignes deux fois, en utilisant le raccourci Ctrl D, alors allons-y et changeons celles-ci en item one, et celle-ci en item two.

Maintenant, voyez comment j'essaie d'accéder à l'attribut pay rate à partir de l'instance, bien que nous n'ayons pas un tel attribut d'instance.

Maintenant, si j'étais exécuter cela, alors vous allez voir que nous avons toujours l'accès pour voir cet attribut de classe.

Eh bien, cela pourrait être déroutant.

Et cela pourrait être difficile à comprendre pourquoi cela se produit.

Eh bien, il y a en fait quelque chose que nous devons comprendre lorsque nous travaillons avec des instances en Python.

Donc, lorsque nous avons une instance en main, alors en premier lieu, cette instance essaie de récupérer l'attribut à partir du niveau d'instance au premier stade, mais si elle ne le trouve pas là, alors elle va essayer de récupérer cet attribut à partir du niveau de la classe.

Donc, ce que cela signifie, cela signifie que item one a fait quelque chose ici et s'est dit à lui-même, d'accord, donc je n'ai pas cet attribut ici parce que ce n'est juste pas un attribut qui m'est assigné.

Donc, je vais essayer de le rechercher à partir du niveau d'instance et puis je vais le trouver et si je le renvoie.

Donc, c'est exactement ce qui se passe ici.

Item one et item two sont des instances qui n'ont pas pu trouver l'attribut pay rate au niveau de l'instance.

Donc, les deux sont allés de l'avant et ont essayé de récupérer cet attribut à partir du niveau de la classe.

Et puisque cela existe vraiment au niveau de la classe, alors nous avons pu y accéder.

Maintenant, pour vous donner une meilleure idée de ce qui se passe ici.

Alors, je vais faire une chose supplémentaire.

Maintenant, je vais supprimer cette première ligne d'impression.

Et je vais aller de l'avant et supprimer ces attributs d'ici aussi.

Maintenant, il y a un attribut magique intégré, pas une méthode magique, que vous pouvez aller de l'avant et voir tous les attributs qui appartiennent à cet objet spécifique.

Et cela est réalisable en utilisant ce double underscore vi CT double underscore comme cela.

Donc, cela va de l'avant et essayer de vous apporter tous les attributs qui appartiennent à l'objet auquel vous appliquez cet attribut et voulez voir son contenu.

Donc, je vais aller de l'avant et copier celui-ci et le coller pour le niveau d'instance aussi.

Donc, cela va me donner tous les attributs pour le niveau de classe.

Et la deuxième ligne va faire cela pour le niveau d'instance.

D'accord, et si j'étais exécuter cela, alors explorons les résultats pendant une seconde.

Maintenant, nous pouvons voir qu'à la première ligne, nous voyons cet attribut pay rate.

Mais dans la deuxième ligne, nous ne le voyons jamais, nous voyons name, price et quantity.

Et vous pouvez aussi faire attention que cet attribut magique est en fait responsable de prendre tous les attributs et de convertir cela en un dictionnaire.

Et c'est de là que vient le mot-clé dict, c'est juste une version abrégée d'un dictionnaire.

Donc, c'est un attribut magique très utile que vous pouvez aller de l'avant et utiliser si vous voulez voir temporairement pour des raisons de débogage, tous les attributs qui appartiennent à un objet.

D'accord, donc maintenant que nous avons compris cela, alors prenons un exemple concret et venons avec une méthode qui va de l'avant et appliquer une réduction sur le prix de nos articles.

Cela sera en créant une méthode qui appartiendra à chacune de nos instances, ce qui signifie que nous pouvons aller de l'avant et venir avec une méthode que nous pourrions nommer apply discount.

Donc, allons-y et commençons à travailler sur cela.

Donc, je vais dire def apply, discount et faites attention que j'utilise une nouvelle méthode à l'intérieur d'une classe ici.

Donc, juste à l'intérieur de celle-ci, alors d'abord nous devons déterminer comment nous allons remplacer un attribut qui appartient à une instance.

Et nous savons déjà que nous pouvons faire cela avec le mot-clé self.

Donc, ce sera self dot price.

Et cela sera égal à self dot price, ce qui signifie l'ancienne valeur de cet attribut multipliée par le pay rate.

Maintenant, vous pourriez vous attendre à ce que nous puissions accéder à cela directement comme cela.

Mais si vous vous souvenez, cela appartient en fait à la classe item elle-même.

Maintenant, cela pourrait être déroutant, car cette méthode est déjà à l'intérieur de cette classe.

Donc, vous pourriez penser déjà que vous pouvez y accéder directement en disant pay rate, car il est déjà à l'intérieur de la classe.

Mais cela ne va en fait pas fonctionner.

Parce que vous pouvez soit y accéder à partir du niveau de la classe ou du niveau de l'instance comme nous l'avons compris précédemment.

Donc, nous pouvons aller de l'avant et dire item dot pay rate comme cela.

Et vous avez une méthode qui peut aller de l'avant et essentiellement remplacer l'attribut de prix pour l'un de vos articles.

Maintenant, pour vous montrer que cela fonctionne, alors je peux utiliser une seule instance pour l'instant.

Et je peux aller de l'avant et appeler cette méthode en disant apply discount.

Et je peux aussi maintenant essayer d'imprimer l'attribut de prix pour cet item one, et nous devrions voir ad right.

Donc, si nous devions exécuter cela, alors vous allez voir que nous allons recevoir at point zero comme prévu.

Maintenant, nous ne devrions pas oublier l'option que vous pourriez aussi vouloir avoir un montant de réduction différent pour un article spécifique.

Donc, disons qu'un jour vous aurez 20 articles ou seulement pour le laptop, vous voudrez avoir une réduction de 30%.

Mais ce sera une mauvaise idée de changer l'attribut de classe à 0.7 car cela affectera tous les articles que vous avez actuellement en main.

Donc, ce que vous pouvez faire à la place, c'est que vous pouvez assigner cet attribut directement à l'une des instances pour lesquelles vous aimeriez avoir un montant de réduction différent, alors allons-y et voyons un exemple pour cela.

Donc, je vais me permettre de ramener l'item ou le laptop et puis ce que je peux faire pour appliquer une réduction de 30% pour cet item est d'assigner le même attribut à l'instance.

Donc, je peux aller de l'avant et utiliser un item deux qui a le score de pay rate est égal à 0.7.

Maintenant, ce qui va se passer ici, c'est que pour item deux, il va trouver l'attribut de pay rate au niveau de l'instance.

Donc, il n'a pas vraiment à aller de l'avant au niveau de la classe et à ramener la valeur de pay rate car au premier regard, il va le trouver au niveau de l'instance.

Mais pour item one, c'est différent, il va toujours lire à partir du niveau de l'item, qui va être 0.8.

Donc maintenant, si nous devions essayer d'utiliser item deux dot apply discount, et ainsi que d'imprimer le prix maintenant, alors voyons ce qui va se passer.

Donc, je vais décommenter cette ligne pour ne pas voir cet écran pour l'instant.

Et je vais aller de l'avant et exécuter notre programme.

Maintenant, vous pouvez voir que nous recevons toujours, cependant, 800.

Et ce que cela signifie, cela signifie que la réduction qui a été appliquée est toujours de 20%.

Et d'où cela vient, eh bien, cela vient de cette méthode ici qui, quoi que nous essayions de tirer le pay rate du niveau de la classe.

Donc, une meilleure pratique ici sera de changer ces deux cellules.

Et de cette manière, si nous remplaçons le pay rate pour le niveau de l'instance, alors il va lire à partir du niveau de l'instance.

Mais pour item one, si nous essayons d'accéder au pay rate à partir du niveau de l'instance, alors cela reste toujours bien, car nous n'avons pas assigné un pay rate spécifique pour item one.

Donc, il va tirer cela du niveau de la classe.

Maintenant, si nous devions essayer d'exécuter cela, alors vous allez voir maintenant que nous avons les résultats attendus.

Et si nous devions également décommenter, la première ligne d'impression pour item one et réexécuter notre programme, alors vous pouvez voir que pour item one, nous avions 20% de réduction.

Et pour item two, nous avions 30% de réduction.

Donc, lorsqu'il s'agit d'accéder aux attributs de classe, vous pourriez vouloir reconsidérer comment vous voulez y accéder lorsque vous viendrez avec certaines méthodes.

Et spécifiquement pour créer une méthode comme apply discount, c'est une excellente idée d'y accéder à partir du niveau de l'instance.

Donc, vous permettez également l'option d'utiliser un pay rate qui est assigné au niveau de l'instance.

D'accord, donc maintenant que nous avons compris complètement les différences entre une classe et un attribut d'instance, passons à l'avant au sujet suivant.

Maintenant, vous voyez que j'ai supprimé ces lignes d'impression que j'ai en dessous.

Et je suis venu avec cinq instances que j'ai créées ici.

Donc, vous pourriez aussi vouloir créer ces cinq instances immédiatement.

Donc, c'est pourquoi je vais vous recommander d'aller ici dans mon dépôt, d'accéder à ce répertoire des attributs de classe, et puis des extraits de code, et puis d'aller de l'avant et de copier le code du fichier five underscore items.py.

D'accord, donc en considérant une situation où votre boutique va être plus grande à l'avenir, ce qui signifie que vous allez avoir plus d'articles, alors plus d'articles que vous allez avoir, plus de filtration comme des choses que vous voulez faire à l'avenir.

Mais ce qui est problématique actuellement avec notre classe est le fait que nous n'avons aucune ressource où nous pouvons simplement accéder à tous les articles que nous avons dans notre boutique en ce moment.

Maintenant, cela aurait pu être mieux si nous pouvions d'une certaine manière avoir une liste avec toutes les instances d'articles qui ont été créées jusqu'à ce point.

Mais actuellement, il n'y a pas d'approche qui nous donnera une liste avec cinq éléments où chaque élément représentera une instance d'une classe.

Donc, afin de venir avec une telle conception, alors voici un excellent candidat pour créer un attribut de classe que nous pourrions nommer all.

Et une fois que nous aurons fait cela, alors nous allons voir comment nous allons ajouter nos instances à cette liste.

Donc, je vais aller de l'avant et commencer par aller ici et utiliser dans tous les attributs.

Donc, ce sera all equals to une liste vide.

Maintenant, nous devons déterminer comment nous allons ajouter nos instances à chaque fois que nous allons de l'avant et créer une instance.

Maintenant, si vous vous souvenez, la méthode double underscore init est appelée immédiatement une fois que l'instance a été créée.

Donc, cela pourrait être une excellente idée d'aller en bas à l'intérieur de cette méthode double underscore init et d'utiliser un code qui sera responsable de l'ajout à cette liste chaque fois que nous créons une instance et cela sera aussi simple que de dire quelque chose comme ce qui suit.

Donc, premièrement, vous pourriez faire attention que j'ai en fait écrit quelques commandes dans cette fonction double underscore init comme run validations et assigned to save object.

Donc, cela pourrait être une excellente idée de commencer avec un commentaire ici qui dira actions to execute juste pour avoir une excellente séparation entre les différentes choses que nous faisons.

Maintenant, à l'intérieur de cela, je peux dire item dot all et vous pouvez voir que j'utilise d'abord l'objet de classe puis c'est une liste donc je peux utiliser dot append et puis je vais simplement ajouter l'objet self.

Maintenant, nous savons que self est en fait l'instance elle-même chaque fois qu'elle est créée.

Donc, une fois que nous allons de l'avant et lançons une telle commande à l'intérieur de l'unité, alors pour chaque instance, qui va être créée, cette liste all va être remplie avec nos instances.

Maintenant, pour vous montrer cela, je peux sauter une ligne après avoir créé les instances, et nous pouvons dire print item that all.

Et maintenant, si j'étais exécuter notre programme, alors vous allez voir que nous allons avoir une liste avec cinq instances.

Si j'étais faire défiler un peu vers la droite, alors vous pouvez voir que j'ai exactement cinq éléments.

Et c'est parfait.

Maintenant, cela va être extrêmement utile si vous voulez faire quelque chose avec seulement l'un des attributs de vos instances.

Donc, disons que vous aimeriez imprimer tous les noms pour toutes vos instances, alors vous pouvez utiliser facilement une boucle for pour accomplir une telle tâche.

Donc, nous pouvons aller de l'avant et dire, pour instance, dans item dot all et vous pouvez dire print instance, dot name.

Et une fois que nous avons fait cela, alors vous pouvez voir que nous avons tous les noms pour toutes les instances que nous avons créées.

Donc, cela va être utile ici et là, surtout si vous savez comment utiliser la fonction filter, par exemple, pour appliquer certaines choses spéciales sur certaines des instances qui correspondent à vos critères.

D'accord, donc maintenant que nous avons compris cela, alors prenons soin d'un problème que nous avons vu précédemment.

Maintenant, si j'étais utiliser un Ctrl, D quelques fois, et toujours utiliser cette impression item dot all maintenant vous pourriez voir que la manière dont l'objet est représenté n'est pas trop conviviale.

Maintenant, cela aurait pu être mieux si nous pouvions d'une certaine manière changer la manière dont l'objet est représenté dans cette liste ici.

Maintenant, il y a en fait un moyen d'y parvenir en utilisant une méthode magique à l'intérieur de notre classe.

Maintenant, il y a une méthode magique qui est appelée double underscore our EPR.

Et our EPR signifie représenter vos objets.

Donc, c'est pourquoi vous pouvez en fait aller de l'avant et utiliser cette méthode magique.

Et puis vous aurez le contrôle pour afficher vos objets lorsque vous les imprimez dans la console.

Maintenant, je recommande en fait de regarder une vidéo qui compare entre une méthode qui lui est similaire, qui est appelée double underscore str.

Et vous pouvez jeter un coup d'œil dans la description de cette série entière pour regarder en fait la vidéo dont je parle.

D'accord, donc allons-y et utilisons la méthode RPM pour comprendre comment cela va fonctionner.

Donc, je vais dire def à l'intérieur de notre classe.

Et je vais utiliser double underscore r e, PR double underscore et comme prévu, il recevra le self.

Maintenant, ce que nous pouvons faire maintenant, c'est retourner une chaîne de caractères qui sera responsable de représenter cet objet.

Maintenant, évidemment, nous ne voulons pas utiliser quelque chose qui n'est pas unique pour chacune des instances.

Parce que disons que j'étais utiliser maintenant return items, quelque chose comme cela, et exécuter notre programme, alors vous pouvez voir que je vais recevoir une liste avec cette chaîne cinq fois.

Mais cela va être difficile d'identifier quelle instance représente chaque chaîne ici.

Donc, cela pourrait être utile si nous devions retourner une chaîne qui pourrait être unique.

Donc, je vais fermer la console ici et aller de l'avant ici et utiliser une chaîne formatée.

Et afin de rendre cela unique, c'est une meilleure pratique de le représenter exactement comme nous créons l'instance comme cela.

Donc, ce que je vais faire ici, c'est de mettre l'item et d'utiliser des crochets d'ouverture et de fermeture.

Et puis je vais rendre la chaîne de retour ici aussi égale que possible à la manière dont nous créons ces instances.

Donc, je vais commencer par taper ici des guillemets simples pour échapper aux guillemets doubles qui viennent de ici.

Et je vais faire référence à la valeur de name en utilisant self dot name.

Et puis je vais laisser mes guillemets simples.

Et je vais utiliser une virgule comme cela.

Et puis je vais aller de l'avant et faire référence à la valeur de notre prix.

Je vais utiliser une virgule supplémentaire, et je vais dire self dot quantity.

Maintenant, si nous devions exécuter notre programme à nouveau, alors vous pouvez voir que maintenant nous recevons une liste qui est beaucoup plus conviviale que ce que nous avons vu précédemment.

Et vous pouvez aussi voir que ce premier élément, par exemple, est assez équivalent à cette ligne ici.

Maintenant, vous pourriez être curieux de savoir pourquoi j'ai travaillé si dur pour retourner la version représentative de nos objets de la même manière que nous les créons.

Donc, c'est juste la meilleure pratique selon les documentations de Python car cela nous aidera à créer des instances immédiatement par l'effort de copier et coller celles-ci dans la console Python.

Donc, si vous y pensez maintenant, si vous ouvrez une console Python, et que vous importez cette classe, alors ce sera aussi simple que de prendre cela et de le coller dans la console Python.

Et puis vous aurez une instance étant créée.

Donc, c'est la seule raison pour laquelle j'ai adopté cette approche.

Et aussi, bien sûr, je voulais simplement retourner une chaîne unique qui représenterait vraiment notre instance.

Et vous pouvez voir que c'est très facile d'identifier les instances de notre classe avec cette liste.

Et avec cette approche, d'accord, donc jusqu'à ce point, nous avons compris comment nous pouvons changer la manière dont nous représentons nos objets.

Et nous avons également compris comment nous pouvons accéder à toutes nos instances par cet attribut de classe que nous avons intentionnellement nommé all.

Maintenant, dans cette partie, nous allons examiner pour résoudre un problème supplémentaire que nous avons en termes de meilleures pratiques lorsque nous allons étendre cette application et ajouter plus de fonctionnalités.

Maintenant, vous pouvez voir que jusqu'à ce point, nous maintenons nos données en tant que code dans ce fichier main.py en instanciant simplement.

Ces cinq articles.

Maintenant, lorsque nous chercherons à étendre cette application et à ajouter quelques fonctionnalités supplémentaires, alors nous pourrions avoir une vie plus difficile à ajouter ces fonctionnalités car les données réelles et le code sont maintenus au même endroit, ce qui signifie dans le même fichier main.py.

Maintenant, vous pourriez penser à créer une base de données qui maintiendra cette information.

Mais je veux garder les choses plus simples pour les besoins de ce tutoriel.

Et c'est pourquoi je vais utiliser quelque chose qui s'appelle CSV que vous avez peut-être entendu parler.

csv signifie valeurs séparées par des virgules.

Donc, cela signifie que vous pourriez aller de l'avant et utiliser un fichier CSV, et vous pourriez stocker vos valeurs sous forme de valeurs séparées par des virgules où chaque ligne représentera une donnée structurée unique. CSV est une excellente option ici car il permet aux données d'être enregistrées dans un format structuré en tableau.

D'accord, alors allons-y et créons un fichier CSV.

Et je vais en fait aller de l'avant et nommer ces articles, dot c est V, comme cela, et je vais aller de l'avant et coller un peu de contenu CSV qui sera responsable à la fin de la journée de représenter les mêmes données que nous cherchons à avoir ici.

Donc, vous pouvez voir qu'à la première ligne, j'ai name, price et quantity.

Et vous pouvez voir que ceux-ci sont séparés par des virgules.

Donc, ceux-ci représentent les colonnes que nous allons avoir comme les données que nous allons maintenir.

Et dans la deuxième ligne et au-delà, nous allons avoir quelques données qui représenteront les données réelles que nous cherchons à maintenir.

Donc, si nous devions maintenant diviser les panneaux, alors vous pouvez voir que ceux-ci sont assez équivalents.

Et maintenant, nous devrions seulement chercher un moyen de lire le fichier CSV et d'instancier réellement ces objets.

Maintenant, nous pouvons voir que j'ai une suggestion de pi charm pour installer un plugin qui supportera les fichiers CSV.

Donc, je vais juste cliquer sur cela et installer ces plugins.

Et vous pouvez voir que je vais avoir un lecteur CSV ici.

Et nous verrons si nous pourrons voir ces données dans un tableau, ce qui sera beaucoup plus agréable.

Donc, allons-y et installons cela.

Et maintenant, vous pouvez voir que j'ai quelques options supplémentaires que je peux en fait aller de l'avant et utiliser à partir d'ici, je sais que c'est assez petit, mais en fait, vous avez quelques onglets que vous pouvez aller de l'avant et cliquer dessus.

Et si j'étais cliquer sur l'éditeur de tableau, et en fait donner plus de focus à ce fichier, alors vous pouvez voir que j'ai en fait la meilleure façon de lire ces données.

Maintenant, vous pouvez voir que j'ai mes colonnes, vous pouvez voir que j'ai mes lignes.

Et c'est assez bien.

Maintenant, je peux vraiment aller de l'avant et visualiser mes données de manière plus agréable.

Et c'est juste une manière plus courante de maintenir vos données.

D'accord, donc maintenant que nous avons compris comment les fichiers CSV fonctionnent, allons-y et lisons nos fichiers CSV et instancions les instances de manière générique.

Cela a du sens de supprimer ces cinq lignes.

Et je vais utiliser ces lignes sous le apply discount et utiliser une méthode que je pourrais nommer instantiate from CSV comme cela.

Maintenant, vous pouvez voir que celle-ci va également recevoir elle-même car si vous vous souvenez, j'ai dit que dans chaque méthode que nous allons concevoir, nous devons recevoir au moins un paramètre qui sera passé comme l'instance elle-même, car c'est ainsi que Python op fonctionne.

Maintenant, le problème est que nous n'allons pas avoir d'instances en main pour appeler cette méthode à partir de l'instance car cette méthode est en fait conçue pour instancier l'objet lui-même.

Donc, cela signifie que cette méthode ne pourrait pas être appelée à partir d'une instance.

Donc, la manière dont cela va être résolu est en convertissant cette méthode en une méthode de classe.

Maintenant, une méthode de classe est une méthode qui pourrait être accessible de la manière suivante.

Donc, je vais utiliser cet outil de ligne, supprimer cela, et elle pourrait être accessible à partir du niveau de la classe uniquement.

Donc, cela ressemblera à item dot instantiate from CSV, et puis ici, nous allons probablement passer notre fichier CSV.

Donc, cette méthode devrait prendre la pleine responsabilité d'instancier ces objets pour nous.

Maintenant que nous avons compris cela, voyons comment nous pouvons créer une méthode de classe.

Donc, pour sûr, nous devons supprimer le self.

Et je sais que nous avons des flèches, mais nous allons résoudre chacune d'entre elles juste dans une seconde.

Maintenant, afin de convertir cela en une méthode de classe, nous devons utiliser un décorateur qui sera responsable de convertir cette méthode en une méthode de classe.

Maintenant, les décorateurs en Python sont juste un moyen rapide de changer le comportement des fonctions que nous allons écrire en les appelant simplement avant la ligne où nous créons notre fonction.

Donc, nous pourrions utiliser le signe Add et utiliser la class method ici et puis cette méthode instantiate from CSV sera une méthode de classe.

D'accord, donc maintenant que nous avons compris cela, alors nous devrions aussi comprendre une autre information avant d'aller de l'avant et de concevoir cette méthode.

Maintenant, je veux vous montrer ce qui va se passer si j'étais supprimer le nom entier et essayer de recréer cette fonction ici.

Et je vais juste dire instantiate from CSV à nouveau, maintenant faites attention à ce qui va se passer si j'étais ouvrir et fermer les parenthèses, maintenant nous pouvons voir qu'il reçoit toujours un paramètre, mais cette fois, il est nommé CLS.

Maintenant, ce qui se passe ici, et la chose qui se passe ici est le fait que lorsque nous appelons nos méthodes de classe, alors l'objet de classe lui-même est passé comme premier argument toujours en arrière-plan.

Donc, c'est un peu comme l'instance où elle est aussi passée comme premier argument.

Mais cette fois, lorsque nous appelons une méthode de classe dans cette approche, alors la référence de classe doit être passée comme premier argument.

Donc, c'est pourquoi vous devez encore recevoir au moins un paramètre, mais nous comprenons probablement que nous ne pouvons pas nommer cela self, car cela serait juste trop confus.

D'accord, donc maintenant allons-y et écrivons un peu de code pour lire le fichier CSV et instancier quelques objets.

Maintenant, je vais aller en haut d'abord, et je vais importer une bibliothèque qui s'appelle CSV.

Donc, je vais aller ici et je vais utiliser une ligne import CSV, car cela sera la bibliothèque qui prendra la pleine responsabilité de lire le fichier CSV.

Et puis nous verrons comment nous pouvons instancier quelques objets.

D'accord, donc maintenant je peux aller de l'avant et utiliser un gestionnaire de contexte pour lire le fichier items dot CSV.

Maintenant, ces deux fichiers sont situés au même endroit.

Donc, je peux simplement dire directement, Attendez, ouvrez items dot CSV, et la permission que je vais passer ici pourrait être hour car nous cherchons seulement à lire cela.

Et je vais dire as f comme cela.

Maintenant, à l'intérieur de cette ouverture, je vais aller de l'avant et utiliser quelques métadonnées pour convertir directement le CSV, ce qui, à la fin de la journée, sera responsable de le convertir en un dictionnaire Python.

Donc, je vais dire reader est égal à CSV, dot d ICT reader comme cela.

Et je vais passer le contenu de notre fichier comme cela.

Maintenant, cette méthode devrait aller de l'avant et lire notre contenu comme une liste de dictionnaires.

Mais à la fin de la journée, nous devrions également aller de l'avant et convertir cela en une liste.

Donc, je vais aller de l'avant et créer une variable supplémentaire qui sera égale à items.

Et je vais simplement convertir le reader en une liste.

Et c'est tout.

Et maintenant que nous avons complété les actions que nous voulons compléter en lisant le fichier CSV, allons-y et utilisons un Shift Tab pour indenter.

Et maintenant, avant d'aller de l'avant et d'instancier quelques objets, allons-y et voyons les résultats de l'itération sur la liste des items.

Maintenant, je vais aller de l'avant et utiliser for item in items.

Et puis je vais simplement utiliser print items pour vous montrer le comportement de cela.

Et excusez-moi, cela devrait être item.

D'accord, donc maintenant que nous avons compris cela, alors voyons ce que nous avons dans ces lignes.

Donc, après notre définition de classe, nous allons simplement de l'avant et appelons cette méthode item dot instantiate from CSV.

Donc, si j'étais exécuter cela, alors vous pouvez voir que j'ai reçu quelques dictionnaires dans des lignes séparées.

Et c'est parce que j'itère sur une liste de dictionnaires ici, et c'est juste parfait.

D'accord, donc la seule chose qui nous manque maintenant est de créer des instances.

En plus d'imprimer ceux-ci, alors nous pourrions maintenant dire quelque chose comme item et ouvrir et fermer les parenthèses.

Et cela sera suffisant pour instancier nos instances.

Maintenant, je peux aller de l'avant et passer mes arguments ici en lisant essentiellement les clés d'un dictionnaire.

Donc, je peux dire name est égal à item dot get, et cela recevra name.

Et maintenant, je peux ajouter une virgule et dupliquer cette ligne deux fois, et changer celles-ci en conséquence.

Donc, ce sera price.

Et ce sera quantity.

Et maintenant, je dois remplacer mes noms de clés.

Donc, ce sera price ici, et puis quantity juste là.

Et maintenant, allons-y et voyons ce qui va se passer si j'étais appeler cette méthode.

Et ainsi que l'appel de l'attribut de item dot all car celui-ci stocke toutes les instances à l'intérieur de la liste.

Maintenant, si j'étais aller de l'avant et exécuter cela, alors vous pouvez voir que j'ai quelques flèches.

Maintenant, vous verrez que les flèches sont liées au prix.

Et vous pouvez voir que nous recevons is not greater than or equal to zero.

Maintenant, allons-y et corrigeons cela très rapidement.

Donc, dans le items dot CSV, vous pouvez voir que ceux-ci sont en fait des entiers qui sont supérieurs à zéro.

Donc, le problème est probablement le fait que ceux-ci sont passés comme des chaînes de caractères.

Donc, nous devons aller de l'avant et passer ceux-ci comme des entiers.

Donc, je vais convertir ceux-ci en int, comme cela.

Et maintenant, allons-y et voyons si nous aurons des problèmes comme je m'attends à en avoir, car la quantité devrait se plaindre de la même chose.

Et vous pouvez voir que c'est exactement ce qui se passe ici.

Donc, nous pouvons utiliser le même pour quantity comme cela, et travailler avec cela.

Et vous pouvez voir que maintenant nous voyons nos instances parfaitement.

Maintenant, je veux montrer un autre problème que nous pourrions avoir à l'avenir et que nous devrions éviter maintenant.

Donc, ces trois lignes vont fonctionner avec cette structure d'Aveda.

Mais si j'étais changer le prix de notre clavier en quelque chose comme 74 dot 90, quelque chose comme cela, et réexécuter notre fichier, alors vous pouvez voir que nous allons recevoir quelques problèmes.

Donc, nous devons convertir le prix non pas en un entier mais en un float comme cela.

Et c'est la seule façon de surmonter cela car nous ne voulons pas convertir le prix en un entier directement car il pourrait être float.

Donc, maintenant nous pourrions aller de l'avant et exécuter et vous pouvez voir que maintenant cela fonctionne parfaitement, bien que nous voyons les prix comme 100.0 mais c'est quelque chose que nous allons examiner à l'avenir mais pour l'instant cela fonctionne parfaitement.

Et maintenant nous sommes prêts à sauter à notre prochain sujet.

D'accord, donc maintenant que nous avons complètement compris les méthodes de classe, allons-y et comprenons également ce que sont les méthodes statiques maintenant, la méthode statique doit faire un travail pour vous, qui a une certaine connexion logique avec une classe.

Donc, par exemple, si vous voulez vérifier si un nombre est un entier ou un float, alors c'est un bon candidat pour créer une méthode statique, car cela a une certaine connexion avec la classe avec laquelle nous travaillons.

Donc, il est logique de vérifier si un prix d'un article a un point décimal et en disant a un point décimal, je compte évidemment ceux qui sont point zéro.

Maintenant, pour être honnête, les méthodes statiques et de classe pourraient vous sembler très similaires.

Mais nous allons expliquer les principales différences très bientôt.

D'accord, donc je vais utiliser ces lignes pour créer notre première méthode statique.

Maintenant, allons-y et utilisons le mot-clé def.

Et nous allons nommer cette méthode is underscore integer car nous avons dit que nous aimerions écrire une méthode statique qui vérifiera si un nombre reçu est un entier ou non.

Maintenant, si j'étais ouvrir et fermer les parenthèses, cela recevrait évidemment elle-même maintenant, je veux que vous regardiez de plus près ce qui va se passer si j'étais changer cette méthode pour qu'elle soit une méthode statique et l'approche va être à peu près la même que nous avons fait avec la méthode de classe, nous allons utiliser un décorateur qui est appelé static method et cela sera responsable de la conversion.

Donc, je vais aller de l'avant et utiliser cette ligne et je vais dire add static method comme cela.

Maintenant, faites attention à la manière dont le paramètre reçu est devenu la couleur orange régulière à laquelle nous sommes familiers car ce n'est qu'un paramètre régulier que nous recevons.

Maintenant, cela signifie que ces méthodes statiques n'envoient jamais en arrière-plan l'instance en tant que premier argument et cela contrairement aux méthodes de classe, les méthodes de classe envoient la référence de classe en tant que premier argument.

Et c'est pourquoi nous avons dû recevoir le CLS.

Et c'est pourquoi il est intentionnellement coloré en violet.

Mais avec les méthodes statiques, nous n'envoyons jamais l'objet en tant que premier argument.

Donc, c'est pourquoi nous devrions nous référer à la méthode statique, comme une fonction régulière qui reçoit simplement des paramètres comme nous sommes familiers avec les fonctions isolées.

Maintenant, je vais approfondir cela dans quelques minutes.

Mais allons-y et terminons d'abord notre méthode statique.

Donc, cela devrait recevoir num comme un paramètre car nous devrions recevoir au moins quelque chose pour vérifier si c'est un entier ou non.

D'accord, donc maintenant que nous sommes à l'intérieur de cette méthode, alors je peux aller de l'avant et utiliser quelques instructions pour vérifier si l'argument reçu est un entier ou non.

Maintenant, si vous vous souvenez, nous avons dit que nous aimerions, nous allons compter les floats qui sont décimaux qui sont point zéro, d'accord ? Ce qui signifie, par exemple, 5.0 10.0, et ainsi de suite.

D'accord, donc maintenant que nous avons compris cela, allons-y et utilisons une instruction if.

Donc, si dans nous allons appeler la fonction intégrée qui est appelée is instance.

Et cela devrait recevoir deux arguments.

Et nous pouvons comprendre ce que cette fonction va faire pour nous, elle va vérifier si le paramètre reçu est une instance d'un float ou d'un entier.

Donc, nous allons passer en tant que premier argument le num et en tant que deuxième argument, le float sans appeler ces parenthèses, donc seulement la référence au mot-clé float.

Donc, ce conditionnel devrait aller de l'avant et vérifier si le num est un nombre flottant ou non.

Maintenant, à l'intérieur de cette instruction if, je vais dire return num.is integer, donc en disant.is integer, alors je dis essentiellement compter les floats qui sont décimaux qui sont point zéro.

Donc, cela signifie que si j'étais passer ici un nombre comme 10.0, alors cela retournera false, mais rappelez-vous que cela entrera ici parce qu'il pense que c'est un défaut parce qu'il est représenté de cette manière.

Et donc l'East amisco interview devrait vérifier si le point est zéro, et vrai retourner false en conséquence.

Maintenant, je vais aussi utiliser une instruction else if ici pour vérifier essentiellement si c'est un entier par lui-même.

Donc, je vais dire l E is instance num, et vérifier si c'est une instance d'un entier, alors je vais simplement retourner true.

Et si c'est juste autre chose, alors je vais simplement dire return false comme cela.

Donc, maintenant que nous avons conçu cette méthode, alors jetons un coup d'œil à la manière dont nous pouvons l'appeler.

Donc, maintenant je vais simplement supprimer cela et cela, je ne vais pas vraiment instancier quoi que ce soit, je vais juste vous montrer comment vous pouvez accéder à la méthode statique.

Donc, je vais simplement appeler cette item.is interview et je vais simplement passer un nombre que je vais aimer vérifier s'il est un interview ou non.

Maintenant, pour sûr, nous aimerions imprimer cela.

Donc, nous verrons le résultat.

Maintenant, allons-y et passons sept.

Donc, vous pouvez voir que nous recevons true maintenant si j'étais passer 7.5 alors je recevrais false et ce qui se passe en arrière-plan, c'est le fait qu'il entre ici, mais il voit que ce n'est pas un entier donc il retourne false.

Mais si j'étais changer cela en 7.0 alors cela devrait encore retourner true parce que ce qui se passe, c'est qu'il entre à l'intérieur de ce conditionnel et puis il vérifie si c'est un entier, mais nous avons dit que cette méthode compte les floats qui sont point zéro.

Donc, elle retourne toujours true, donc c'est une conception parfaite.

D'accord.

Donc, j'ai créé un nouveau fichier, que je vais simplement expliquer ici quand utiliser une méthode de classe et quand utiliser une méthode statique.

Donc, nous pouvons complètement comprendre les différences entre celles-ci car je me souviens que j'ai eu un temps très difficile à comprendre pourquoi j'ai besoin de cela et pourquoi j'ai besoin de l'autre.

Donc, ce sera la principale question à laquelle je vais répondre dans ce fichier Python.

Donc, ne vous sentez pas comme si vous deviez copier et coller le code en suivant ce que j'explique ici en écoutant devrait être suffisant.

Donc, dans ce fichier, je vais simplement aller de l'avant et créer cette classe item que nous avons à droite et je vais utiliser pass pour ne pas recevoir de flèches.

Maintenant, quand nous allons utiliser une méthode statique.

Donc, nous allons utiliser une méthode statique lorsque nous voulons faire quelque chose qui ne devrait pas être unique par instance.

Exactement comme je l'ai fait précédemment.

Donc, his interview est une méthode qui va simplement être responsable de vérifier si un nombre est un entier ou non.

Donc, c'est pourquoi je pourrais me permettre de l'inclure sous l'item, tout comme je pourrais utiliser cette def comme une fonction isolée juste au-dessus de la classe.

Et cela était aussi acceptable.

Mais je préfère ne pas faire cela, car bien que ce soit une méthode qui n'a rien à voir avec l'instance, cela est d'une certaine manière lié à la classe item.

Donc, c'est la raison pour laquelle vous voulez créer cela comme une méthode statique, comme nous l'avons conçu précédemment.

Et la raison pour laquelle vous aimeriez créer une méthode de classe est pour instancier des instances à partir de certaines données structurées que vous possédez.

Donc, exactement comme nous l'avons fait, nous avons créé une méthode de classe qui était responsable de la lecture du fichier CSV et de la création de certaines instances.

Donc, comme je l'ai écrit ici, celles-ci sont utilisées pour manipuler différentes structures de données pour instancier des objets, comme nous l'avons fait avec le fichier CSV, nous pourrions également utiliser une méthode de classe comme instancier à partir d'un fichier JSON, ou à partir d'un fichier yamo, celles-ci sont simplement différentes façons de maintenir des données de la meilleure manière possible et c'est le code que vous chercherez à inclure à l'intérieur de vos méthodes de classe.

C'est pourquoi elles devraient exister dans toute classe, surtout si vous cherchez à instancier des centaines d'objets dans vos programmes.

Donc, c'est une excellente idée d'avoir au moins une méthode de classe, comme nous l'avons fait dans la classe item.

Maintenant, la seule différence principale entre une méthode de classe et une méthode statique est le fait que les méthodes statiques ne passent pas la référence de l'objet comme premier argument en arrière-plan, il est noticeable du fait que nous n'avons pas de surbrillance spéciale violette, dans mon cas pour le premier paramètre.

Donc, si vous vous souvenez, si j'étais aller de l'avant et utiliser ici un premier fondamental comme num, alors vous verrez que c'est le premier paramètre qui est coloré en orange, car c'est un paramètre régulier.

Mais celui-ci est violet, car c'est un paramètre obligatoire que nous devons recevoir, car ce que j'ai juste expliqué, donc ce sont les principales différences entre une méthode statique et une méthode de classe.

Maintenant, si vous vous souvenez, j'ai intentionnellement dit que les méthodes de classe et les méthodes statiques ne peuvent être appelées qu'à partir du niveau de la classe.

Cependant, celles-ci peuvent également être appelées à partir des instances.

Donc, comme vous pouvez le voir, je peux en fait instancier un objet et appeler l'entier ainsi que l'instancier à partir de quelque chose peut simplement passer ici un nombre comme cinq et je ne vais pas recevoir de flèches.

Et si j'étais exécuter l'aide, alors vous pouvez voir que je n'ai pas d'erreur.

Maintenant, je vais être honnête avec vous, je n'ai jamais vu de raison d'appeler une méthode statique, ou une méthode de classe à partir du niveau de l'instance.

Mais c'est juste une option qui existe, je sais que c'est très, très déroutant.

Mais c'est quelque chose que vous allez rarement voir.

Et comme je l'ai dit, je n'ai jamais vu de grande raison d'appeler une méthode statique ou d'appeler une méthode de classe à partir d'une instance.

Donc, ma recommandation pour ne pas vous confondre est de simplement ne pas appeler celles-ci à partir du niveau de l'instance.

D'accord, donc j'ai minimisé le code que nous avons écrit jusqu'à présent dans la classe item.

Maintenant, afin de commencer à résoudre les problèmes que nous allons résoudre dans cet épisode, alors je vais créer ici deux instances.

Donc, je vais dire form one est égal à un item.

Et donnons-lui un nom comme JC phone v 10.

Et puis utilisons simplement un prix et une quantité aléatoires.

Et je vais copier et coller cela et utiliser une autre variable comme phone two dans celle-ci, nous allons augmenter la version de 10.

Et disons que ce prix pour le phone two devrait être 700.

D'accord, donc maintenant que nous avons créé deux instances de phone, faites attention que ces deux items sont des téléphones.

Donc, nous pourrions penser à certains attributs qui pourraient représenter des téléphones dans la vie réelle.

Pensez à un attribut comme broken phones, car nous pourrions avoir certains téléphones qui pourraient avoir été cassés.

Et donc nous ne pouvons pas vraiment le marquer comme un téléphone que nous pourrions vraiment vendre.

Donc, cela signifie que nous pourrions aller de l'avant et dire phone one that broken phones, disons que nous avons malheureusement un téléphone cassé en main en ce moment.

Donc, je vais aller de l'avant et assigner le même attribut à notre deuxième téléphone.

Et maintenant que nous avons créé cet attribut réaliste, alors l'étape suivante à laquelle nous pourrions penser, pourrait être de créer une méthode qui irait de l'avant et calculerait les téléphones qui ne sont pas cassés, ce qui signifie soustraire la quantité par le montant des téléphones cassés car cela a tout à fait du sens.

Et puis nous pouvons comprendre quels sont les téléphones que nous pourrions aller et vendre à l'avenir.

Mais nous avons quelques problèmes à créer une méthode qui irait de l'avant et calculerait une telle chose car nous ne pouvons pas nous allons de l'avant à l'intérieur de notre item.

Et faire cela assez facilement, car nous n'avons pas vraiment l'attribut broken phones assigné à self.

Et nous ne pouvons pas vraiment aller de l'avant et créer cette méthode à l'intérieur de cette classe item, car cette méthode ne va pas être utile pour les centaines d'autres items que vous allez créer.

Celles-ci représentent simplement un type d'item de téléphone.

Donc, afin de résoudre ce problème en termes de meilleures pratiques en programmation orientée objet, alors nous pourrions aller de l'avant et créer une classe séparée qui héritera des fonctionnalités que la classe item apporte avec elle.

Et c'est exactement là où nous pourrions bénéficier de l'héritage.

Et nous pourrions aller de l'avant et créer une classe séparée que nous appelons phone.

Et puis cette classe phone héritera de toutes les méthodes et de tous les attributs que la classe item possède.

Donc, allons-y et simulons cela.

Donc, je ne vais pas supprimer les instances pour l'instant, mais je vais aller de l'avant ici et créer une classe que je vais nommer phone.

Maintenant, faites attention que je ne vais pas utiliser de point-virgule et je vais utiliser ces crochets et je vais spécifier quelle classe je voudrais hériter.

Donc, je vais hériter de item.

Et puis je vais simplement utiliser un pass temporairement car je ne voudrais pas utiliser de fonctionnalité supplémentaire pour l'instant à l'intérieur de cette classe.

D'accord, donc maintenant que nous avons créé cette classe, alors allons-y et exécutons d'abord notre programme, où au premier stade, les instances seront des instances d'item.

Et cela ne devrait pas poser de problèmes car nous savons que nous pouvons créer ces instances d'item et nous ne recevrons pas de flèches.

Mais si nous devions changer celles-ci en phone comme cela, alors nous ne devrions toujours pas recevoir de flèches.

Et c'est juste une manière basique dont vous pourriez utiliser l'héritage afin de représenter différents types d'objets lorsque vous voulez le faire.

Maintenant, cela pourrait également être appliqué à d'autres programmes immobiliers que vous voulez créer et acheter par vous-même.

Mais dans mon cas, cela a tout à fait du sens de créer quelques classes où chaque classe représentera un type d'article.

Et puis je pourrais aller de l'avant et hériter de la classe item dans chacune des classes enfants que je vais créer à l'avenir, je pourrais également utiliser une autre classe pour un type d'article comme laptop, et puis je pourrais aller de l'avant et utiliser la fonctionnalité séparée pour cela.

Maintenant, lorsque nous parlons de classes dont nous héritons, alors celles-ci sont considérées comme étant appelées classes parent.

Et lorsque nous utilisons plusieurs classes qui héritent de cette classe parent, alors celles-ci sont considérées comme étant appelées classes enfant.

Donc, ce sont juste des termes avec lesquels vous voulez être familier lorsque nous parlons de programmation orientée objet.

Et à partir de là, nous verrons des choses plus avancées que vous pouvez aller de l'avant et faire avec vos classes enfant.

D'accord, donc maintenant allons-y et comprenons quelques choses plus avancées sur l'héritage.

Maintenant, pour aider cette série, nous avons appris qu'il n'est pas une bonne idée d'assigner des attributs manuellement, une fois que nous avons créé ces instances.

Et la meilleure façon de faire cela est en fait d'aller de l'avant et de créer notre constructeur et de passer la valeur que nous aimerions immédiatement dans la création de l'instance exactement comme ici.

Donc, afin de résoudre cela, alors nous allons devoir déterminer comment nous allons faire cela, car créer le constructeur à l'intérieur de cette classe phone va être délicat, car nous ne voulons pas vraiment briser la logique que le score de développement apporte avec la classe parent.

Mais nous aimerions aussi passer un attribut supplémentaire comme broken phones, que nous allons gérer cet attribut et l'assigner à l'objet self exactement comme nous l'avons fait dans la deuxième partie de notre série.

Donc, afin de garder la logique identique pour cette classe enfant, et ainsi que de recevoir certains attributs supplémentaires.

Alors pour l'instant, je vais aller de l'avant et copier le code dans notre constructeur et simplement coller cela à l'intérieur de notre classe phone.

Et cela a du sens temporairement, car nous avons reçu exactement les mêmes paramètres que nous devrions recevoir lorsque nous instancions une instance.

Et nous avons aussi maintenant le contrôle de recevoir certains paramètres supplémentaires, comme nous voulons le faire avec les broken phones.

Donc, allons-y ici et disons broken.

Donc, je vais simplement faire défiler ici, et je vais dire broken phones est égal à zéro.

Laissez aussi recevoir une valeur par défaut pour cela.

Et allons-y et tapons une validation pour les broken phones.

Donc, je vais me permettre de simplement copier cela et coller cela.

Et nous allons utiliser assert quantity je veux dire broken phones est supérieur ou égal à zéro et je vais changer cela en broken phone Comme cela, en fait broken phones, et cela devrait être exactement comme nous l'avons fait avec la quantité.

Et maintenant, allons-y à la section de assigned to self object.

Et nous pouvons utiliser self dot broken phones est égal à broken phones comme cela.

Et vous pouvez voir que ici nous avons des actions à exécuter.

Maintenant, cela aurait pu être mieux si nous pouvions aussi créer un attribut de classe pour la classe phone.

Et cela signifiera que nous pourrions aller de l'avant ici et dire all est égal à une liste vide, puis nous pourrions aller de l'avant et utiliser un form dot all dot append, comme cela.

Et maintenant, si j'étais aller de l'avant et exécuter ce programme, alors vous pouvez voir que je ne vais pas recevoir de flèches.

Maintenant, pour vérifier que cela fonctionne, alors je vais aussi passer ici un.

Et je vais faire de même ici aussi.

Et je vais supprimer ceux-ci.

D'accord, je vais supprimer les attributs codés en dur, et le programme fonctionne toujours.

Maintenant, j'aimerais aussi tester cela en appliquant l'une des méthodes que nous avons écrites jusqu'à présent, ce qui sera évidemment une méthode que j'aime utiliser à partir de la classe parent, car nous héritons de celles-ci.

Donc, je peux aller de l'avant et utiliser phone one dot, calculate total price, et il est logique d'imprimer cela.

Donc, je vais aller de l'avant et imprimer cela.

Et vous pouvez voir que print phone one dot calculate total price.

Et maintenant, si j'étais exécuter cela, alors vous pouvez voir que j'ai reçu un résultat.

Donc, cela signifie que je n'ai pas de flèches.

Maintenant, je ne suis pas sûr si vous avez fait attention à cela.

Mais si j'étais faire défiler un peu vers le haut, alors vous allez voir que le constructeur dans la classe enfant se plaint de quelque chose.

Et laissez le curseur de la souris et voyez quel est l'avertissement.

Maintenant, vous pouvez voir qu'il nous dit que l'appel à double underscore in it de la super classe est manquant.

Et ce que cela signifie, cela signifie que lorsque nous initialisons la méthode double underscore init à l'intérieur de la classe enfant, alors Python s'attend à ce qu'une fonction soit appelée intentionnellement.

Maintenant, cette fonction est nommée super.

Et ce que super nous permet de faire, c'est qu'il nous permet d'avoir un accès complet à tous les attributs de la classe parent.

Et en utilisant la fonction super, nous n'avons pas vraiment besoin de coder en dur l'assignation d'attributs, comme nous l'avons fait avec le nom, le prix et la quantité.

Et ainsi que pour les autres validations que nous avons exécutées chaque fois que nous voulons créer une classe enfant.

Maintenant, imaginez à quel point cela va être difficile.

Si pour chacune des classes enfants que nous allons créer à l'avenir, nous devrons passer par la copie et le collage de assert price et quantity.

Et ainsi que faire la chose assigned to self object dans ces trois lignes.

Cela va être beaucoup de duplication de code.

Maintenant, pour nous faire gagner du temps, c'est exactement pourquoi nous avions besoin d'utiliser la fonction super, la fonction super nous permettra d'avoir l'accès aux attributs de la classe parent.

Et donc, nous serons en mesure d'implémenter pleinement les meilleures pratiques en matière d'héritage lorsqu'il s'agit de programmes orientés objet.

Maintenant, encore une fois, ce programme fonctionne parce que nous assignons les attributs de nom, prix et quantité pour l'objet self dans la classe d'essai.

Mais si j'étais supprimer ces trois lignes, et ainsi que ces deux lignes, maintenant ces lignes se trouvent être les lignes que j'ai copiées et collées et essayer d'exécuter ce programme, alors vous pouvez voir que nous recevons une erreur d'attribut phone object has no attribute price, et faites attention à la ligne d'où cela vient.

Cela vient de la ligne 21 de la classe item, car elle pense qu'elle a l'attribut de prix.

Mais nous n'avons jamais l'attribut de prix au niveau du téléphone.

Parce que nous venons de supprimer le self dot price est égal à price.

Et c'est pourquoi maintenant nous avons quelques problèmes.

Et nous allons remplacer toutes les lignes que nous avons supprimées par ce qui suit que je vais simplement exécuter maintenant.

Donc, je vais aller à la première ligne de notre constructeur, et je vais dire appel à la fonction Super pour avoir accès à tous les attributs slash méthodes.

Et puis je vais dire super, net je vais ouvrir et fermer les parenthèses.

Et puis je vais utiliser la méthode double underscore init comme cela.

Maintenant, vous pouvez voir que la seconde où j'ai complété cela, alors il n'y a plus d'avertissements concernant le constructeur dans cette classe enfant.

Et vous pouvez aussi voir que ces méthodes double underscore init attendent certains arguments spéciaux.

Maintenant, ces arguments spéciaux viennent évidemment de la classe item dont nous héritons.

Donc, si j'étais passer ici, name et aussi price et aussi quantity, alors cela devrait être bien.

Maintenant, vous pouvez aussi vous demander si ce n'est pas la duplication de code, le fait que nous avons aussi copié et collé les paramètres que nous recevons dans la classe enfant.

Et oui, c'est une question parfaite.

C'est quelque chose qui pourrait être résolu par quelque chose de plus avancé.

Si vous avez entendu parler des arguments de mot-clé, c'est quelque chose que nous pouvons résoudre de cette manière.

Et puis nous n'aurons pas à dupliquer les paramètres que nous recevrons pour le constructeur, ce n'est pas quelque chose que je vais montrer pour ce stade, je vais m'en tenir à cela.

Et je vais simplement le laisser tel quel maintenant en appelant la fonction super.

Et ainsi que la méthode init juste après cela devrait être responsable d'avoir le même comportement que nous avions précédemment.

Donc, nous devrions toujours voir 2500 pour cette ligne d'impression, et nous ne devrions pas voir de flèches.

Et si j'étais exécuter le programme, alors vous pouvez voir que nous recevons le résultat attendu.

Donc, de cette manière, nous implémentons les meilleures pratiques de la programmation orientée objet pour chaque classe enfant que nous utilisons un constructeur séparé, nous devons également appeler la fonction super afin d'avoir un accès complet à tous les attributs et méthodes qui proviennent de la classe dont nous héritons.

D'accord, donc j'ai minimisé le code pour nos classes.

Et j'ai aussi laissé avec une instance de foam ici.

Maintenant, je veux vous montrer les résultats des éléments suivants.

Donc, je vais dire print, et je vais voir ce que la liste de all dans la classe item va nous ramener.

Donc, je vais dire item dot all.

Et puis je vais aussi dire phone that all si vous vous souvenez, nous avons implémenté cet attribut de classe ici aussi.

Donc, je vais minimiser le code.

Et puis je vais exécuter notre programme.

Maintenant, vous pouvez voir quelque chose de très étrange ici, nous voyons item.

Et puis nous voyons essentiellement le résultat de la méthode array PR qui provient de la classe item.

Maintenant, la raison pour laquelle cela se produit, c'est parce que nous n'avons jamais implémenté notre méthode EPR à l'intérieur de la classe form.

Donc, c'est pourquoi nous voyons ce résultat générique de item.

Maintenant, vous pouvez aussi faire attention que nous ne créons qu'une instance de la classe phone.

Donc, ce n'est pas très bien que nous voyons item dans ces sorties.

Donc, ce que nous pouvons utiliser, au lieu de coder en dur le nom de la classe dans la méthode rppr à l'intérieur de la classe item, alors nous allons accéder au nom de la classe de manière générique.

Maintenant, si j'étais remplacer cela par un attribut magique spécial qui sera responsable de me donner le nom de la classe, alors ce sera parfait.

Donc, je vais supprimer cela.

Et je vais utiliser des accolades, et je vais dire self, dot double underscore class, dot double underscore name.

Donc, c'est une manière générique d'accéder au nom de la classe à partir de l'instance.

Et en faisant cela, alors au lieu de recevoir item, une chaîne codée en dur, alors je devrais recevoir le nom de la classe que j'ai initialisée dès le début.

Donc, cela devrait être phone, car c'est la seule instance que j'ai pour l'instant.

Et vous pouvez voir que c'est exactement le résultat que je reçois.

Donc, c'est parfait.

Maintenant, j'ai dit plus tôt qu'en utilisant la fonction super, alors nous avons essentiellement accès à tous les attributs et les méthodes qui proviennent de la classe dont nous héritons.

Donc, ce que cela signifie, cela signifie que nous aurons également l'accès à l'attribut de classe de all qui est à l'intérieur de la classe item.

Et je parle de cet attribut, à droite.

Maintenant, pour vous montrer cela, alors je vais ouvrir le code de la classe form.

Et je vais supprimer l'ancien attribut.

Et je vais juste faire cela maintenant.

Et je vais aussi supprimer les actions à exécuter où j'ai utilisé form dot all dot append, car nous n'avons plus l'ancien attribut dans la classe form.

Et si j'étais supprimer ceux-ci, et exécuter notre programme maintenant, alors vous pouvez voir que je reçois toujours le même résultat.

Donc, c'est une excellente idée de supprimer l'ancien attribut au niveau de la classe enfant, c'est une excellente idée d'utiliser uniquement l'ancien attribut au niveau de la classe parent, car en utilisant la fonction super dans la classe enfant, nous aurons accès à l'ancien attribut.

Donc, cela signifie que si un jour nous voulons avoir accès à toutes les instances d'items qui ont été initialisées, y compris les classes enfants, alors y accéder à partir de item dot all devrait également être suffisant.

Maintenant, vous pourriez être confus quant à la manière dont cette ligne est responsable de l'ajout de cette instance à l'intérieur de l'attribut all qui se trouve être une liste.

Et cela se produit parce qu'en utilisant la fonction super et ainsi que l'init, alors nous appelons essentiellement la méthode init à l'intérieur de la classe parent.

Maintenant, dans la dernière ligne à l'intérieur de cette méthode, nous utilisons également item dot all dot append, qui sera également accessible à partir de la classe form, donc c'est pourquoi l'appel de l'attribut de classe all à partir de la classe item est une meilleure idée, car il nous donnera une image complète.

D'accord, donc avant de plonger dans le sujet de cet épisode, alors nous allons devoir faire un peu d'organisation de code ici, car comme vous pouvez le voir, pour chacune des classes enfants que nous allons créer à l'avenir pour étendre ce projet, alors nous allons devoir faire cela dans le fichier main.py, car c'était le seul fichier avec lequel nous travaillions.

Et maintenant que notre projet grandit, nous devons commencer à travailler avec plusieurs fichiers.

Donc, c'est pourquoi cela pourrait être mieux de travailler avec un fichier qui représentera la classe de l'item et de travailler avec un fichier séparé qui représentera la classe enfant du téléphone.

Donc, nous aurons le fichier main.py dédié uniquement à la création d'instances de ces classes.

Donc, commençons par cela.

Donc, je vais aller dans le répertoire du projet et créer deux fichiers Python.

Le premier, nous allons le nommer item.pi.

L'autre devrait être nommé phone.pi.

Et je vais prendre le code de notre classe item.

Et je vais simplement tout prendre.

Pourquoi, pendant ce temps, et je vais couper cela et puis je vais coller cela à l'intérieur de cela.

Maintenant, faites attention que j'utilise la bibliothèque CSV.

Donc, c'est en fait l'emplacement où j'ai besoin de cette bibliothèque.

Donc, je vais simplement copier la ligne d'importation.

Et cela devrait être suffisant.

Maintenant, je vais faire le même processus pour le form dot p y, je vais copier cela dans le fichier form.py également.

Mais maintenant, ce fichier doit importer la classe item car comme vous pouvez le voir, nous avons une flèche ici.

Donc, nous devrions dire from item, import items comme ce qui suit dans les flèches devraient être parties.

Et puis dans le fichier main.py, nous pouvons essentiellement utiliser ce fichier pour instancier uniquement des instances, ce qui signifie créer des données qui représenteront quelque chose pour Python.

Donc, cela signifie que nous pouvons aller de l'avant et importer la classe à partir du fichier item, nous pouvons faire de même à partir du fichier form.

Et puis nous pouvons aller de l'avant et faire les choses que nous avons l'habitude de faire, donc nous pouvons dire item dot instantiate from CSV.

pour vérifier que cela fonctionne, nous pouvons aussi dire print, et item dot all comme cela.

Et si nous voulons exécuter ce fichier maintenant pour voir que cela fonctionne, alors nous pouvons le faire.

Et vous pouvez voir que tout fonctionne comme prévu.

Maintenant, juste une rapide note de côté, je ne vais pas trop compter sur la classe enfant que nous avons créée dans le dernier épisode, pour montrer les problèmes que nous allons résoudre dans cet épisode, je vais compter davantage sur la classe item afin que ce soit plus facile à suivre.

Et nous ne complexifierons pas trop les choses.

Maintenant, cela ne signifie pas que je ne recommande pas d'utiliser des classes enfants ou quelque chose comme cela.

Mais ce sera juste plus facile de vous montrer les cas que je vais montrer dans la classe parent.

Donc, c'est pourquoi, par exemple, j'ai temporairement supprimé la ligne d'entrée de la classe form.

Et je suis simplement venu avec une instance d'item aléatoire dont le nom est my item et le prix s'avère être ce nombre, je n'ai pas spécifié de quantité car nous avons une valeur par défaut.

Et maintenant, après cette ligne, vous pouvez voir que je remplace cet attribut par la chaîne de caractères other items.

Maintenant, le résultat attendu ne va pas surprendre qui que ce soit car nous voyons au bon moment lorsque nous imprimons cet attribut.

Mais nous pourrions nous demander si c'est le comportement que nous voulons toujours ? Et si nous voulons restreindre nos utilisateurs à changer l'attribut de nom, une fois que le nom a été configuré dans l'initialisation, ce qui signifie dans cette ligne ? Eh bien, c'est quelque chose que nous pourrions vouloir atteindre pour les attributs critiques comme le nom de vos instances, et dans notre cas, le nom de notre item.

Donc, ce que nous pourrions faire, nous pourrions en fait aller de l'avant et créer des attributs en lecture seule, ce qui signifie que nous avons seulement une opportunité de définir le nom de notre item.

Et puis nous ne pouvons plus toucher la valeur de cela.

Donc, ce que cela signifie, cela signifie que nous pouvons configurer cela dans l'initialisation.

Et nous devrions avoir des flèches si nous essayons de remplacer la valeur de cela.

Maintenant, cela est également connu sous le nom d'encapsulation lorsque nous parlons des principes de la programmation orientée objet, sur lesquels je vais me concentrer davantage dans les épisodes futurs.

Mais maintenant, allons-y et voyons comment nous pouvons créer des attributs en lecture seule, comment nous pouvons restreindre nos utilisateurs à remplacer les attributs après l'initialisation de nos instances.

D'accord, donc à gauche nous avons le fichier main.py, et à droite nous avons le fichier item.py avec lequel nous allons travailler et à l'intérieur de la classe je vais créer notre premier attribut en lecture seule.

Maintenant, la manière dont vous pouvez commencer à faire cela est d'abord en utilisant un décorateur et si vous vous souvenez des épisodes précédents, les décorateurs sont comme des fonctions que vous pouvez pré-exécuter avant une autre fonction.

Donc, je pourrais aller de l'avant et utiliser le décorateur property, et puis aller de l'avant et créer une fonction.

Et voici l'emplacement exact où je pourrais configurer le nom de notre attribut en lecture seule.

Donc, à des fins de test, allons-y et appelons cela read only name quelque chose à ce moment-là, d'accord, et puis j'ouvrirai et fermerai les parenthèses, et cela recevra évidemment self car cela va appartenir à chacune des instances.

Et maintenant, à des fins de test, allons simplement de l'avant et retournons une chaîne aléatoire comme a trois fois.

D'accord, et puis maintenant que nous avons fait cela, je peux aller à notre fichier main.php et essayer d'accéder à cette propriété.

Maintenant, faites attention que je vais appeler ces propriétés et non des attributs.

Donc, je vais aller ici, et je vais essayer d'imprimer item one, that name et maintenant que j'ai écrit name, faites attention aux différences dans cette liste déroulante pour read only name, nous recevons une icône totalement différente ici sur le côté gauche, qui représente une propriété où ici nous voyons le flutter qui représente un champ irrégulier.

Donc, si j'étais essayer d'imprimer cela et exécuter notre programme, alors évidemment nous allons recevoir le résultat attendu.

Mais si j'étais essayer de définir une nouvelle valeur, pour le read only name, disons que nous voulons changer cela en quelque chose comme cela, alors vous allez voir que Python va se plaindre de cela.

Et même si nous essayons d'exécuter cela, alors nous allons finir avec une exception qui dit attribute error can set attribute.

Donc, c'est ainsi que les attributs en lecture seule, soi-disant, fonctionnent en Python, vous pouvez créer ceux-ci en utilisant un décorateur de propriété avant vos fonctions et retourner la valeur que vous aimeriez retourner.

Maintenant, le plus grand défi ici va être de convertir l'attribut de nom que nous avons en fait, qui se trouve être exactement ici en obéissant à un attribut en lecture seule.

Et cela va être un peu difficile.

Mais allons-y et commençons à travailler sur cela.

Donc, premièrement, je vais supprimer ces trois lignes, car nous n'allons pas utiliser cette propriété plus longtemps.

Et je vais faire défiler un peu vers le haut et travailler sous ce constructeur ici.

Donc, vous pourriez penser que convertir l'attribut de nom en lecture seule, ce qui signifie une propriété, est aussi simple que de faire quelque chose comme d'abord utiliser le décorateur de propriété, et puis aller de l'avant et dire def name, puis recevoir self comme paramètre.

Et puis utiliser quelque chose comme return self dot name, car nous avons déjà le self type name assigné à l'objet self.

Mais en fait, faire quelque chose comme cela, c'est comme dire à cette classe, hé, à partir de maintenant, vous allez avoir un attribut de nom qui va être en lecture seule.

Et c'est l'effet direct du décorateur de propriété.

Donc, je vais laisser un commentaire ici qui va ressembler à ce qui suit.

Mais si vous vous souvenez, nous avons essayé de définir le self dot name dans une nouvelle valeur à l'intérieur de notre constructeur.

Donc, vous pouvez voir que cette action est illégale car nous avons une propriété en lecture seule ici.

Donc, lorsque vous allez de l'avant et créez une propriété avec le nom de nom, alors vous n'êtes normalement pas autorisé à définir cette valeur plus longtemps, vous êtes seulement autorisé à avoir accès à la voir dans n'importe quelle instance que vous allez créer.

Donc, c'est pourquoi si j'étais survoler ma souris ici, alors nous allons voir une flèche qui dit property name cannot be saved.

Donc, la manière pythonique de contourner cela pour surmonter cela est d'utiliser un underscore avant le nom de notre attribut de nom réel que nous assignons à l'objet self.

Et en faisant cela, nous gagnons quelques choses qui sont assez importantes.

Donc, premièrement, laissez-moi ajouter ici un underscore et utiliser simplement quelque chose comme cela.

Et puis maintenant, j'ai besoin d'aller à ma fonction de propriété, ce qui signifie l'attribut de propriété.

Et je vais devoir ajouter ici le double underscore également.

Parce que premièrement, je vais de l'avant et configure la valeur pour mon double underscore, excusez-moi, un seul underscore name pour qu'il soit égal à la valeur de ce paramètre ici.

Et puis je vais de l'avant et utilise un autre attribut en lecture seule que j'ai intentionnellement donné le nom de name et je et puis je retourne self dot underscore name.

Maintenant, je peux retourner à mon fichier main.py et voir quels effets ces lignes ont actuellement sur nos instances.

Donc, premièrement, je peux aller de l'avant et définir un nom pour mon item.

Et je peux accéder au nom de cet item en disant quelque chose comme je ne voulais pas ce nom.

Donc, je n'ai pas vraiment à aller de l'avant et utiliser item one dot underscore name, car cela va être un peu laid, et pas pratique.

Parce que l'accès aux attributs avec toujours un underscore avant n'est pas agréable pour chacune des instances que vous cherchez à accéder aux attributs.

Faire cela une fois à l'intérieur de la classe va être bien.

Mais essayer d'accéder à ces attributs en dehors de votre classe, ce qui signifie à partir des instances, ne va pas le rendre trop joli.

Donc, c'est la meilleure façon de surmonter une telle chose.

Et maintenant, si j'étais essayer d'imprimer cela, alors, excusez-moi, laissez-moi corriger cela rapidement par item one dot name, et exécuter notre programme, alors vous pouvez voir que cela fonctionne.

Et maintenant, allons-y et voyons aussi si nous pouvons définir notre nom pour qu'il soit égal à une autre chose comme cela, voir, si cela fonctionne, je peux voir que je ne peux pas définir cet attribut.

Mais cependant, je peux toujours voir ces underscore name à partir du niveau de l'instance.

Et c'est peut-être quelque chose que vous cherchez à éviter, cela aurait pu être beaucoup mieux si nous pouvions d'une certaine manière empêcher totalement l'accès à cet underscore naming ici.

Donc, la manière dont cela est réalisable, est en ajoutant un underscore supplémentaire au nom de l'attribut.

Maintenant, cela pourrait vous rappeler quelque chose qui s'appelle un attribut privé.

Si vous êtes familier avec les langages de programmation comme Java, ou C sharp, c'est à peu près le même comportement que l'utilisation du mot-clé private avant vos attributs dans ces types de langages de programmation, où il a différents principes lorsqu'il s'agit de programmation orientée objet.

Donc, pour résumer, si vous ajoutez un underscore supplémentaire à vos noms d'attributs, ce qui signifie que vous utilisez un double underscore, alors vous empêchez essentiellement l'accès à ces attributs totalement en dehors de la classe.

Donc, voyons une simulation de cela.

Donc, je vais minimiser le terminal, et je vais aller dans mon fichier item.py.

Et au lieu d'utiliser ici un underscore unique, je vais en ajouter un autre.

Et puis je vais changer cela en double underscore également.

Et maintenant, si nous devions aller dans notre fichier main.py, et essayons ici it one dot et essayons essentiellement d'utiliser un double underscore et d'essayer d'accéder au name maintenant, nous pouvons voir que je n'ai même pas de complétion automatique à partir de ma liste déroulante, car je n'ai pas accès pour voir cet attribut à partir du niveau de l'instance.

Et c'est quelque chose que vous cherchez à atteindre lorsque vous voulez avoir un attribut en lecture seule propre.

Et c'est la manière dont vous pouvez faire cela.

Donc, si j'étais essayer d'imprimer cela, alors cela va simplement se plaindre de la manière dont il n'a pas l'attribut de double underscore name dans cette instance.

Et encore, si j'étais supprimer ces double underscores, alors je vais simplement y accéder comme une propriété, ce qui signifie comme un attribut en lecture seule.

Et c'est exactement ce que je cherchais à avoir ici.

D'accord, donc maintenant que nous avons l'idée de cela, alors nous sommes toujours peut-être curieux de savoir comment définir une nouvelle valeur pour l'attribut de nom.

Maintenant, évidemment, utiliser le décorateur de propriété va transformer cela en un attribut en lecture seule.

Mais il existe encore certains décorateurs qui vous permettront cependant de définir une nouvelle valeur pour cette propriété de nom.

Donc, voyons comment cela est réalisable.

Donc, évidemment, cela ne va pas fonctionner.

Parce qu'il dit can't set attribute.

Donc, ce que nous pouvons faire, c'est que nous pouvons utiliser une nouvelle méthode, où nous pouvons déclarer que nous aimerions aussi définir une nouvelle valeur pour cet attribut que nous avons nommé name.

Donc, la manière dont cela va fonctionner est en allant dans notre classe ici.

Et en utilisant ici une méthode supplémentaire avec un décorateur spécial.

Maintenant, ce décorateur va ressembler à ce qui suit.

Donc, je vais me référer au nom car c'est le nom de la propriété.

Et puis je vais utiliser le dot setter.

Donc, en faisant cela, alors je dis essentiellement, hé, donc je veux toujours définir une nouvelle valeur pour ce nom, bien que ce soit une propriété, ce qui signifie un attribut en lecture seule.

Donc, maintenant, si j'étais descendre et dire quelque chose comme def name, et cela recevra self et ainsi qu'un paramètre supplémentaire car le paramètre supplémentaire devrait se référer à la nouvelle valeur que je veux définir pour ce nom.

Donc, je vais recevoir un paramètre que je pourrais nommer quelque chose comme value.

Et puis à l'intérieur de cela, je vais seulement définir la nouvelle valeur pour notre double underscore name.

Parce que si vous vous souvenez, lorsqu'une instance essaie de voir la valeur de name, alors nous retournons essentiellement self dot double underscore name.

Donc, lorsqu'un utilisateur essaiera de définir à nouveau le nom à une nouvelle valeur, alors il devrait exécuter self dot name equals to value et en faisant cela, je permets essentiellement à nos utilisateurs de définir une nouvelle valeur pour name.

Donc, maintenant, montrons quel effet ces trois lignes vont avoir dans notre main.py.

Vous pouvez voir que maintenant les flèches sont parties, je peux maintenant descendre ici et utiliser print item one dot name.

Et cela va fonctionner, je peux voir que j'ai other item.

Donc, cela signifie non seulement que je peux définir une nouvelle valeur pour mon underscore name, soi-disant dans l'initialisation, je peux aussi le faire plus tard, si j'utilise uniquement cette convention ici.

Maintenant, ces choses de getters et setters sont toujours déroutantes dans le langage de programmation normal avec lequel vous travaillez.

Donc, je vais faire un résumé final de tout ce que nous avons appris jusqu'à ce point.

D'accord.

Donc, utiliser add property vous donnera essentiellement un contrôle sur ce que vous aimeriez faire lorsque vous obtenez un attribut.

Et aussi, en utilisant cela, vous convertissez essentiellement cet attribut en lecture seule si je n'ai pas implémenté ces setters ici.

Donc, vous pouvez voir que maintenant, lorsque j'ai commenté ceux-ci, alors cette ligne va avoir quelques problèmes, car en ne faisant pas cela, alors je dis essentiellement que hey, name est en lecture seule, vous ne pouvez pas définir cela si j'étais à nouveau décommenter ceux-ci, alors j'aurai le contrôle pour définir cet attribut à n'importe quel attribut que je voudrais maintenant en utilisant cette instruction ici, en obtenant essentiellement l'attribut, alors j'exécute essentiellement le bunch de codes qui sont exécutés ici.

Donc, chaque fois que j'utilise item one dot name, alors Python se dit à lui-même, d'accord, vous essayez d'obtenir cet attribut.

Donc, je vais aller de l'avant et essayer d'exécuter toutes les lignes de codes qui sont ici.

Donc, c'est exactement ce qui se passe ici.

Et pour vous le montrer, alors je peux simplement utiliser une fonction print aléatoire ici qui dira, vous essayez d'obtenir name comme cela, alors vous devriez voir cette ligne imprimée juste avant ce qu'est la valeur réelle.

Parce qu'au début, nous imprimons vous essayez de fit le name, et puis nous retournons le self dot underscore name, donc il imprime cela par ici.

Donc, c'est ce qui se passe lorsque vous essayez d'obtenir une attitude.

Mais lorsque vous essayez de définir une attitude, alors Python se dit à lui-même, d'accord, donc ici, vous essayez de définir un attribut.

Donc, parce que vous définissez un attribut, alors je devrais aller de l'avant et exécuter le code qui est à l'intérieur de ici, car c'est le centre de cet attribut.

Donc, c'est pourquoi lorsque vous allez de l'avant et utilisez ce décorateur, alors vous devriez toujours recevoir un paramètre car l'autre item va être passé comme argument à ce paramètre, il est très important de comprendre cela.

Et c'est pourquoi je peux seulement me permettre d'utiliser une ligne de code qui dira self dot double underscore name est égal à la nouvelle valeur que vous essayez de définir.

Et pour vous le montrer à nouveau, je peux aller ici et dire print vous essayez de définir dans cette ligne devrait apparaître juste avant cette ligne d'impression car au début j'ai essayé de définir une valeur différente pour name, et puis je l'ai simplement imprimé comme cela.

D'accord, donc si j'étais exécuter cela, alors vous pouvez voir qu'au début nous voyons la ligne de vous essayez de définir puis juste après nous voyons en fait ce que item one dot name est égal.

Maintenant, la raison pour laquelle la valeur est définie est parce que nous l'avons définie ici et puis la prochaine fois que j'essaie d'obtenir la valeur, alors ces lignes sont exécutées.

Donc, c'est le cycle de vie des getters et setters.

Et c'est la manière dont cela fonctionne.

En ayant le contrôle de ce que vous aimeriez faire lorsque vous définissez une nouvelle valeur, vous pouvez également la restreindre, vous pouvez aller de l'avant et faire un peu de conditionnement, ou vous pouvez aller de l'avant et lever certaines exceptions.

Si vous n'aimez pas la valeur que vous recevez, disons que vous voulez restreindre la longueur des caractères pour le nom de cet attribut.

D'accord, donc c'est quelque chose que vous pouvez faire, vous pouvez en fait aller ici et dire si quand de la valeur est supérieur à 10, alors vous aimeriez lever une exception, qui dira quelque chose comme votre, le nom est trop long, quelque chose comme cela.

Et puis vous pouvez dire else et puis vous pouvez exécuter la ligne qui sera responsable de définir cette valeur.

Donc, intentionnellement, je vais le laisser tel quel car la longueur de cela est de neuf caractères.

Donc, nous ne devrions pas avoir de flèches.

Mais si j'étais ajouter ici, deux caractères de plus, comme cela, et exécuté, alors vous pouvez voir que nous allons recevoir une exception qui dira le nom est trop long.

Donc, c'est ainsi que les getters et setters fonctionnent en Python, vous aurez maintenant toutes les connaissances dont vous avez besoin pour jouer avec différents attributs, et les gérer de la manière que vous aimeriez.

Donc, je crois qu'après les informations que vous avez reçues dans cet épisode, vous avez tout ce dont vous avez besoin pour gérer vos attributs avec succès et jouer avec eux, ainsi que créer des classes riches qui auront plusieurs attributs.

Et puis vous pouvez configurer des comportements spéciaux pour ces attributs.

Et aussi vous pouvez décider que vous ne voulez pas forcer à recevoir ces attributs dans le constructeur, vous pouvez décider que vous pouvez supprimer certains paramètres dans votre constructeur.

Et vous pouvez dire que, vous ne voulez pas assigner ceux-ci à l'objet self immédiatement lorsque vous créez une instance.

Donc, peu importe ce que vous aimeriez, vous avez tous les outils pour jouer avec comment gérer vos attributs, la programmation orientée objet vient avec quatre principes clés dont vous devriez être conscient.

Donc, vous comprendrez comment vous devriez concevoir vos grands programmes, afin qu'il soit plus facile de continuer à les développer.

Et je vais parler de ces principes qui sont l'encapsulation, l'abstraction, l'héritage et le polymorphisme.

Donc, le premier principe sera l'encapsulation.

Et nous allons en parler un peu.

Donc, l'encapsulation fait référence à un mécanisme de restriction de l'accès direct à certains de nos attributs dans un programme.

Maintenant, faites attention à la manière dont nous avons fait un excellent travail dans la dernière partie, où nous avons implémenté le principe d'encapsulation sur notre projet.

Donc, faites attention à la manière dont l'attribut de nom n'a pas pu être défini à une nouvelle valeur, avant de passer par certaines conditions que nous avons définies ici, comme la longueur du caractère étant inférieure à 10 caractères.

Donc, restreindre la capacité de remplacer les valeurs pour vos objets dans vos selles, c'est exactement de quoi parle le principe d'encapsulation.

Maintenant, pour vous donner un meilleur exemple du principe d'encapsulation, alors nous allons appliquer des choses similaires à un attribut supplémentaire, qui sera l'attribut de prix.

Maintenant, si vous jetez un coup d'œil rapide dans ce programme que je viens d'exécuter, alors vous pouvez déjà voir que j'ai la capacité de définir directement ces objets à n'importe quel nombre que j'aime, même un négatif 900 fonctionnera ici.

Donc, c'est probablement quelque chose que nous cherchons à changer.

Et la manière dont nous pouvons changer cela est en implémentant certaines méthodes qui vont restreindre l'accès à cet attribut de prix.

Donc, cela aurait pu être bien si nous pouvions avoir deux méthodes qui seraient responsables d'incrémenter ce prix d'un certain pourcentage.

Et il en va de même pour la réduction.

Maintenant, si vous vous souvenez, nous avons déjà créé une méthode similaire qui ressemble à apply discount lorsque nous parlons des attributs de classe, car self dot pay rate multiplié par le prix réel va en fait changer cet attribut en diminuant de 20%.

Parce que pay rate est défini à 0.8, si vous vous souvenez des épisodes précédents, donc allons-y et continuons à concevoir cet attribut de prix pour supporter totalement le principe d'encapsulation.

Donc, premièrement, je vais convertir ce prix en un attribut privé.

Donc, ce sera un excellent début pour éviter de définir ce prix directement comme nous l'avons vu précédemment.

Maintenant, je ne vais pas simplement ajouter ici un double underscore, en plus je vais prendre tout cela.

Et je vais cliquer avec le bouton droit, et puis je vais dire refactor, rename, et puis je vais simplement renommer ce prix en le définissant comme cela double underscore avant cela maintenant faire cela va en fait refactoriser ce changement sur toute la classe où nous essayons d'accéder à l'attribut de prix.

Donc, c'est une excellente chose.

Donc, nous n'avons pas vraiment à changer partout.

Donc, une fois que j'ai fait cela, alors si nous allons aussi jeter un coup d'œil dans le apply discount, alors vous pouvez voir que cela est défini à un nouveau nom de variable que nous avons créé.

Donc, maintenant que nous avons fait cela, alors allons-y et créons une propriété.

Donc, nous aurons la capacité d'accéder à l'attribut de prix temporairement en étant seulement en lecture seule.

Donc, je vais dire add property.

Et puis je vais dire def price, puis je vais simplement retourner self dot price.

Donc, c'est un excellent début pour restreindre l'accès à l'attribut de prix, car maintenant nous avons toujours accès à l'attribut de prix.

Et puis nous ne pouvons pas le définir.

Donc, vous pouvez voir que si nous devions essayer d'accéder à item one dot price, nous allons avoir quelques erreurs, mais nous pouvons simplement accéder à la valeur réelle de cela où elle provient de l'initialisation.

Donc, c'est un oh en fait je vois que nous avons une erreur qui dit recursion error et c'est probablement parce que j'ai oublié d'ajouter le double underscore ici par erreur.

Donc, c'est en fait une excellente exception à laquelle nous avons été confrontés maintenant, vous pouvez voir que nous allons avoir une erreur de recursion, maximum recursion depth exceeded.

Et cela est arrivé parce que j'ai essayé de retourner le prix sans le double underscore.

Donc, si nous essayons d'appeler le self dot price, alors il va essayer d'appeler cette fonction.

Et si nous essayons de retourner cela, alors cela va simplement boucler à nouveau.

Et à un moment donné, cela va échouer avec l'erreur de recursion comme vous le voyez.

Donc, c'est en fait une excellente exception que nous voyons.

Maintenant, si vous voyez cette exception dans vos programmes orientés objet, maintenant vous savez comment la gérer.

Et si j'étais revenir maintenant à Maine et exécuter cela, alors vous pouvez voir que le résultat attendu est ici.

D'accord, donc maintenant que nous avons fait cela, alors retournons à notre classe et essayons de travailler sur nos méthodes qui vont modifier les attributs de double underscore price.

Donc, je vais en fait couper ce métal d'ici.

Et je vais simplement le mettre juste sous la propriété price que nous avons créée.

Donc, nous aurons une apparence plus propre.

Maintenant, premièrement, vous pouvez voir que nous avons le apply discount.

Et nous aimerions aussi venir avec un ply.

increment comme ce qui suit.

Et nous aimerions dire ici, self dot double underscore price est égal à self dot level underscore price plus self dot level underscore price multiplié par une certaine valeur que nous pouvons recevoir comme un paramètre.

Donc, nous pourrions en fait recevoir un paramètre que nous pourrions nommer implement value, et puis nous pourrions simplement le multiplier par ce nombre.

Donc, maintenant que nous avons créé cela, alors testons cela.

D'accord, je vais retourner à notre my main.py.

Et puis je vais l'appeler it one dot apply increment, et puis je vais simplement passer 0.2.

Donc, nous allons incrémenter la valeur de 750 de 20%.

Maintenant, la prochaine fois que j'accède à item one dot price, nous devrions être en mesure de voir la valeur réelle de price, qui devrait être 900.

Et si j'étais exécuter cela, alors vous pouvez voir que le prix a été incrémenté à 900 comme prévu.

Donc, c'est exactement l'encapsulation en action, car vous allez de l'avant et vous n'autorisez pas l'accès directement à l'attribut de prix.

En plus, vous modifiez cet attribut en utilisant des méthodes comme apply increments, ou apply discount.

Maintenant, la même chose se produira si j'étais maintenant aller de l'avant et utiliser item one dot apply, discount, et vous pouvez en fait modifier cette méthode de la manière que vous aimeriez.

Mais cela se réfère actuellement à un attribut de classe que nous utilisons ici.

Donc, cela devrait aussi, à nouveau, appliquer une réduction de 20% au prix de 900, nous devrions être en mesure de voir 720.

Et c'est exactement ce qui se passe ici.

D'accord, donc le prochain principe dont je vais parler s'appelle l'abstraction.

Maintenant, l'abstraction est le concept de la programmation orientée objet qui ne montre que les attributs nécessaires et cache les informations inutiles.

Maintenant, le but principal de l'abstraction est essentiellement de cacher les détails inutiles aux utilisateurs.

Maintenant, en disant utilisateurs, je veux dire des gens comme moi ou vous qui vont utiliser la classe item pour créer certains objets item.

Maintenant, nous pouvons voir que maintenant nous avons un nouveau programme ici qui a un objet item dont le nom est my item, le prix étant ce nombre, et nous avons six de cet item.

Maintenant, nous pouvons aussi voir que je suis venu avec une méthode qui n'existe pas vraiment, qui est appelée send email.

Donc, cette méthode, à la fin de la journée, devrait envoyer un email à quelqu'un qui aimerait décider de cet item.

Et il enverra des informations sur combien d'argent nous pouvons gagner en vendant tous les items et peut-être sur quelques informations supplémentaires qui sont liées à cet item.

Maintenant, envoyer un email n'est pas une action aussi facile que de l'appeler de cette manière.

Parce qu'en arrière-plan, l'envoi d'email doit passer par beaucoup de processus comme se connecter à un serveur SMTP.

Et ainsi que préparer le corps de l'email avec un message automatique qui affichera certaines informations sur cet item.

Donc, comme nous pouvons le comprendre, nous devons passer par beaucoup de nouvelles méthodes avant d'aller de l'avant et d'appeler simplement une méthode Send Email.

Donc, pour simuler cela, alors je peux en fait aller de l'avant et dire send email.

Donc, je vais simplement créer la méthode qui est nécessaire.

Temporairement, je vais utiliser pass.

Maintenant, comme je l'ai dit, nous devons aussi passer par beaucoup d'autres processus.

Donc, c'est une excellente idée de créer des méthodes pour chacun de ces processus, comme se connecter à un serveur SMTP, serveur SMTP comme cela.

Et je vais simplement dire pass car nous essayons seulement de simuler l'idée de l'abstraction ici, je n'envoie pas vraiment un email réel à quelqu'un, je simule simplement une idée d'envoi d'email.

Et nous devons aussi aller préparer un corps pour un mail automatique prepare body, à droite et puis je peux simplement retourner une chaîne formatée qui dira quelque chose comme hello.

Quelqu'un, nous pourrions recevoir cela comme un paramètre aussi.

Et puis nous pouvons dire, nous avons self dot name, six fois, à droite, donc cela devrait être six.

Donc, quantité fois comme cela, puis je peux dire regards à shave.

Donc, c'est juste un email très simple que nous pouvons envoyer à quelqu'un.

Maintenant, nous pouvons comprendre que nous devons appeler ces méthodes à l'intérieur du même email.

Donc, simuler cela sera self dot Connect, et puis self dot, prepare body.

Et probablement, nous devons aussi aller l'envoyer à droite, donc nous pouvons simplement dire quelque chose comme send ici, puis nous le passons.

Maintenant, vous pouvez voir que ces métaux à la fin de la journée ne seront appelés qu'à partir du Send Email.

Parce que ceux-ci sont juste des parties du processus d'envoi d'email, qui est un processus plus grand que nous avons divisé en plusieurs étapes dans cette classe.

Maintenant, le plus gros problème est que nous aurons accès à l'appel de ces méthodes à partir de l'instance.

Et c'est exactement de quoi parle le principe d'abstraction.

Le principe d'abstraction vous dit que vous devriez cacher les informations inutiles des instances.

Donc, c'est pourquoi, en convertissant ces méthodes en méthodes privées, alors nous appliquons réellement les principes d'abstraction.

Et cela est réalisable en Python d'une manière, qui, je vais être honnête, n'est pas trop pratique, mais c'est réalisable en ajoutant un double underscore.

Maintenant, encore une fois, dans d'autres langages de programmation, cela est réalisable en ayant des modificateurs d'accès pour vos méthodes, comme private ou public.

Et je parle de langages de programmation comme Java, C sharp, etc.

Donc, si nous devions convertir ces méthodes en méthodes privées, en ajoutant simplement un underscore, alors celles-ci ne pourraient être appelées qu'au niveau de la classe, ce qui signifie à l'intérieur de la classe.

Donc, si nous devions essayer d'y accéder, alors vous pouvez voir que je vais avoir une complétion automatique, ce qui signifie que j'aurai la capacité d'accéder à ces méthodes.

Et puis je vais faire de même pour les autres méthodes.

Maintenant, cette flèche vient de ici, car nous n'avons pas vraiment spécifié d'argument, je vais simplement ajouter une chaîne vide.

Maintenant, si j'étais retourner à notre fichier main.py, alors vous allez voir que nous allons avoir quelques problèmes.

Même si j'étais essayer d'y accéder avec un double underscore, je n'aurai même pas de complétion automatique.

Et la raison pour cela est que c'est une méthode privée.

Donc, vous devez vraiment réfléchir à vos méthodes si vous voulez les rendre accessibles en dehors de votre classe, ce qui signifie à partir des instances.

Et c'est exactement de quoi parle l'abstraction.

Vous voulez abstraire les informations qui sont inutiles à appeler ou à y accéder à partir de vos instances.

D'accord, donc l'héritage est le troisième principe de la programmation orientée objet.

L'héritage est un mécanisme qui nous permet de réutiliser le code à travers nos classes.

Maintenant, c'est quelque chose que nous avons totalement bien conçu tout au long de ce cours, car nous avons créé plus de classes qui sont des classes enfants de la classe item, où chaque classe enfant représente un type d'article.

Maintenant, faites attention à la manière dont je change la ligne d'importation de phone import from, et j'utilise la classe enfant de item, que nous avons créée, qui est appelée le phone, vous pouvez voir que je passe des arguments similaires, ils peuvent encore utiliser un code qui est implémenté dans la classe parent.

Si nous devions exécuter ce programme, alors nous n'allons pas recevoir de problèmes.

Parce que phone utilise toutes les méthodes et les attributs qu'il hérite de la classe item, qui est exactement ici.

Et si nous nous souvenons, nous avons conçu la méthode Send Email dans la classe parent et nous pouvons l'utiliser à partir de l'instance d'un phone et nous pouvons aussi le faire pour le reste des méthodes que nous avons créées qui affectent vraiment certains des attributs comme dans l'interview.

La partie encapsulation où nous avons appliqué la méthode apply increments qui reçoit une valeur d'incrément.

Et si nous devions tester cet incrément, le prix de 0.2, et puis imprimer item one dot price, alors nous devrions voir 1200.

Donc, si nous devions imprimer cela, alors vous pouvez voir que c'est exactement le résultat.

Donc, cela décrit principalement ce qu'est l'héritage.

Il s'agit de réutiliser le code à travers toutes les classes.

Et c'est exactement le scénario ici.

Et la beauté derrière cela est que vous pouvez créer plus de classes enfants qui représenteront les types d'articles comme laptop, keyboard, camera, tout ce à quoi vous pourriez penser.

Et puis vous pouvez simplement modifier des méthodes spécifiques que vous aimeriez appeler pour le type d'article que vous avez.

Donc, cela décrit parfaitement ce qu'est l'héritage.

D'accord, donc le dernier principe que nous avons maintenant est le polymorphisme.

Maintenant, le polymorphisme est un concept très important en programmation.

Il fait référence à l'utilisation d'une seule entité de type pour représenter différents types dans différents scénarios.

Maintenant, un exemple parfait pour cette définition, sera certaines des fonctions que nous connaissons déjà qui existent en Python.

Maintenant, juste une rapide note de côté, le polymorphisme fait référence à de nombreuses formes, Paulie étant nombreuses, et morphisme étant des formes.

Donc, encore une fois, l'idée d'appliquer le polymorphisme sur nos programmes est la capacité d'avoir différents scénarios, lorsque nous appelons exactement la même entité et une entité pourrait être une fonction que nous appelons simplement.

Maintenant, comme vous pouvez le comprendre, le polymorphisme n'est pas quelque chose qui est spécifiquement appliqué à la manière dont vous créez vos classes.

Cela est en fait quelque chose qui fait référence globalement à l'ensemble de votre projet.

Et dans les prochaines minutes, nous allons voir quelques mauvaises pratiques où le polymorphisme n'est pas appliqué.

Et nous allons aussi voir où en Python le polymorphisme est parfaitement appliqué.

Donc, un excellent exemple de l'endroit où le polymorphisme est appliqué, est dans la fonction intégrée lane.

Parce que la fonction intégrée lane en Python sait comment gérer différents types d'objets qu'elle reçoit comme argument, et elle vous retourne un résultat en conséquence.

Donc, comme vous pouvez le voir ici, si nous devions utiliser la fonction intégrée Len dans une chaîne, alors nous aurions reçu le montant total de caractères.

Mais si nous faisons cela dans une liste, alors nous ne recevrons pas la longueur des caractères de cette expression entière ici.

En plus, nous recevrons le nombre d'éléments qui sont à l'intérieur de cette liste.

Et pour vous montrer comment cela va fonctionner, alors je vais simplement exécuter ce programme et bien sûr, les résultats sont juste comme prévu.

Donc, comme la définition du polymorphisme le dit, c'est juste une seule entité qui sait comment gérer différents types d'objets, comme prévu.

D'accord.

Donc, maintenant que nous avons compris que le polymorphisme est appliqué partout en Python, surtout dans la fonction intégrée land, comprenons aussi où il est implémenté sur notre projet ici.

Maintenant, nous pouvons voir que j'ai essayé d'appeler la méthode apply discount qui n'est jamais implémentée à l'intérieur de la classe phone.

Et le fait que je puisse l'utiliser à partir de la classe item, c'est parce que nous héritons de cette classe.

Et c'est la raison de base.

Maintenant, si j'étais retourner à ce fichier main dot php et exécuter cela, alors vous pouvez voir que cela va fonctionner car le apply discount est une méthode que je peux utiliser à partir de la classe item héritée.

Maintenant, c'est exactement ce que le polymorphisme est aussi en action.

Parce que le polymorphisme, encore une fois, fait référence à une seule entité que vous pouvez utiliser pour plusieurs objets.

Maintenant, si j'étais un jour aller de l'avant et créer plus de types d'articles, ce qui signifie plus de classes qui représenteront différents types d'articles, et à partir de celles-ci appeler la méthode apply discount, cela va aussi fonctionner car la méthode apply discount est une méthode qui va être accessible à partir de tous les types d'objets, c'est exactement pourquoi vous avez peut-être entendu parler des termes d'héritage et de polymorphisme ensemble combinés.

Maintenant, pour vous le montrer, alors essayons de créer une autre classe qui va être identique à la classe phone, à droite, je vais créer un fichier keyboard.

Et puis je vais simplement dire ici, class.

Vous savez quoi, avant cela, allons dans phone et copions tout d'ici et collons cela comme cela.

Je vais me débarrasser de ces lignes.

Et je vais simplement laisser l'init tel quel, je vais changer le nom de la classe de phone à keyboard et je vais aussi supprimer cet attribut dont nous n'avons pas besoin, broken phones.

D'accord, donc maintenant que nous avons cela, alors je peux en fait aller de l'avant dans mon fichier main dot php et utiliser une autre ligne importante qui dira from key board import keyboard, et puis je vais changer cela en keyboard, je vais remplacer ce nom, juste pour le rendre plus réaliste, puis je vais exécuter le même problème, vous pouvez voir que cela fonctionne.

Donc, c'est encore exactement là où le polymorphisme est en action, car nous pouvons utiliser cette seule entité à partir de différents types d'objets, et elle saura comment la gérer correctement.

Maintenant, en disant gérer cela correctement, alors je veux dire essentiellement, vous pouvez avoir le contrôle de la quantité de réduction que vous voulez appliquer à l'intérieur de vos classes maintenant, car si nous devions aller à keyboard et utiliser des attributs de classe, exactement comme nous l'avons utilisé dans la classe item, qui était pay rate, alors nous allons avoir un contrôle total pour toutes les réductions qui vont être appliquées au keyboard.

Et pour vous le montrer, je vais tenter le typage en pay rate.

Et vous pouvez voir que j'ai même une complétion automatique car la substitution dans la classe enfant est légale, d'accord, donc je peux simplement dire pay rate est égal à 0.7.

Et ce sera tout.

Maintenant, j'ai le même montant de réduction pour tous mes claviers.

Si j'étais à nouveau exécuter le fichier main.py, alors vous pouvez voir que les résultats sont juste comme prévu, nous voyons 700.

Donc, c'est la beauté derrière l'héritage et le polymorphisme ensemble.

Et il en ira de même si nous devions décider que nous aimerions avoir 50% de réduction.

Donc, il ne me faudra que d'aller de l'avant et de dire pay rate est égal à 0.5.

Et c'est tout.

Donc, j'espère que vous comprenez un peu mieux le polymorphisme maintenant.

Maintenant, juste une rapide note de côté, le polymorphisme est parfaitement cool, nous l'avons implémenté en utilisant des classes abstraites.

Et c'est juste la manière identique d'utiliser des interfaces dans d'autres langages de programmation comme Java, une interface est une manière dont vous pouvez implémenter comment une classe devrait être conçue.

D'accord, donc c'est comme un modèle pour une classe.

Et cela est réalisable en utilisant des classes abstraites, que je ne vais pas couvrir dans cette partie.

Mais encore une fois, le polymorphisme, comme je l'ai dit, est un terme qui est implémenté dans différentes zones dans tout le langage de programmation Python.

Donc, j'espère que vous avez passé un bon moment à apprendre le cours de programmation orientée objet.

Maintenant, vous avez beaucoup d'outils que vous pouvez aller de l'avant et essayer d'implémenter par vous-même sur vos projets, ce qui vous aidera vraiment à vous emmener à l'étape suivante en tant que développeur.

À la prochaine fois.