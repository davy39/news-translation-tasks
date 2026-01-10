---
title: La stabilité de l'API est bon marché et facile, avec les Compat Patchers !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-28T21:00:40.000Z'
originalURL: https://freecodecamp.org/news/api-stability-is-cheap-and-easy
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/windowsserver_article_012-1.jpg
tags:
- name: api
  slug: api
- name: best practices
  slug: best-practices
- name: Compatibility
  slug: compatibility
- name: patching
  slug: patching
- name: Python
  slug: python
- name: stability
  slug: stability
- name: versioning
  slug: versioning
seo_title: La stabilité de l'API est bon marché et facile, avec les Compat Patchers
  !
seo_desc: 'By Pakal de Bonchamp

  Why backwards compatibility matters

  (If you''re already convinced that API stability is a crucial concern, not the whim
  of a few conservative mummies, save yourself some time and rush to the following
  chapter.)


  "WE DO NOT BREAK U...'
---

Par Pakal de Bonchamp

## Pourquoi la compatibilité ascendante est importante

_(Si vous êtes déjà convaincu que la stabilité de l'API est une préoccupation cruciale, et non le caprice de quelques momies conservatrices, économisez-vous du temps et précipitez-vous vers le chapitre suivant.)_

> "NOUS NE CASSONS PAS L'ESPACE UTILISATEUR !"

Ce [fameux coup de gueule de Linus Torvalds](https://lkml.org/lkml/2012/12/23/75) est, hélas, plus pertinent que jamais.

> Si un changement entraîne la rupture des programmes utilisateurs, c'est un bug dans le noyau. Nous ne blâmons JAMAIS les programmes utilisateurs. Comment peut-on ne pas comprendre ça ?

> Si les applications ne se souciaient pas des valeurs d'erreur spécifiques, alors il n'aurait pas de sens d'en avoir plus d'une dès le début, et vous ne devriez pas vous soucier de celle qui était utilisée. Mais puisque les applications s'en soucient, et puisque nous avons plusieurs valeurs d'erreur, nous nous en tenons aux anciennes, sauf s'il y a de très bonnes raisons de ne pas le faire. Et ces raisons doivent vraiment être très bonnes, et explicitées et expliquées.

Remplaçons "noyau" par n'importe quel framework/bibliothèque, et "valeur d'erreur" par "signature d'API", et nous obtenons un commandement inestimable de la bonne programmation. Nous pouvons vivre très bien avec quelques petits bugs et des fonctionnalités imparfaites, mais lorsque nos applications livrent des segfaults ou des tracebacks interminables après une simple mise à jour de version, il y a un problème. Un vrai problème.

Et il y a un paradoxe ici. Concernant les distributions OS, les pilotes, libc/gtk/Qt et autres bibliothèques de bas niveau, statiquement typées, nous attendons - et sommes heureux d'expérimenter - des mises à jour indolores, apportant uniquement de nouvelles fonctionnalités et des corrections de bugs. Alors que pour nos frameworks web de haut niveau, principalement codés en langages dynamiques, nous nous sommes résignés au fait que chaque mise à jour pourrait devenir un travail de 3 jours pour comprendre les ruptures, trouver des versions compatibles des dépendances, et forker ou monkey-patcher jusqu'à ce que les suites de tests soient à nouveau vertes. Logiquement, ne devrait-ce pas être l'inverse ? Pourquoi la plupart des freewares win32 de 1995 fonctionnent-ils encore, pourquoi la migration x32/x64 a-t-elle été si transparente pour la plupart des utilisateurs, si une application serveur pluggable publiée il y a 2 ans est cassée sur de multiples aspects ?

Je vais vous dire pourquoi.

La stabilité de l'API était autrefois un engagement très prisé. Le versionnage sémantique était un must-have. Des projets comme Qt détaillaient fièrement les mesures qu'ils prenaient pour garantir que leur C/C++ évoluerait sans rupture. Certains remplissaient même leurs paramètres de fonction avec des valeurs NULL "réservées pour les usages futurs". Et les changements incompatibles n'étaient évoqués que lorsque aucune solution ne pouvait être trouvée.

Heureusement, cette mentalité est encore valable dans de larges domaines de la programmation. Mais maintenant une philosophie différente a contaminé les esprits, surtout dans l'industrie du web. Cette façon de penser spartiate pourrait être appelée "Marche ou meurs", "Pas de paradis pour les faibles", ou "Tant que je préviens, je peux tirer la balle". Parfois cachée derrière des concepts mignons comme "calendar versioning", ou "applications evergreen", cette façon de penser est en réalité cristalline : la plus mineure des mises à jour logicielles peut introduire des changements cassants - documentés ou non, fièrement assumés ou non - il suffit de s'en accommoder.

Pourquoi ? Pourquoi ne pas simplement laisser les alias, les adaptateurs, et autres shims de compatibilité, lors du déplacement de modules, lors du renommage d'objets, lors du changement de signatures de fonction ? Avec la nature dynamique et introspective de la plupart des langages modernes, n'est-ce pas une brise ? Parfois les ressources de développement sont si rares que c'est déjà trop. Mais le reste du temps ? Mon intuition est que lorsque ce n'est pas un problème de compétence technique, ou de paresse, cela pourrait être un problème culturel.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/meme_bill.png)

Connaissez-vous ce coup de dopamine que vous ressentez lorsque vous cochez une case dans une liste de tâches, surtout la dernière ? Cette satisfaction qui vous fait parfois écrire une tâche déjà accomplie juste pour pouvoir la cocher ? Vous pourriez ressentir la même excitation lorsque vous refactorisez brutalement du code vers une architecture plus propre, ou effacez des shims de compatibilité "_conformément à la politique de dépréciation_". C'est le rush de bonheur du devoir bien accompli, du retour à la pureté.

Mais ce sentiment précis est un énorme mensonge. Une absorption de soi aveuglante. Un biais psychologique nuisible.

Les shims de compatibilité ne sont pas une dette technique ; ni un ensemble de verrues. Au contraire, ce sont des actifs inestimables. Avec ces quelques morceaux de code source, notre logiciel étend sa compatibilité à des dizaines, des centaines, des milliers de bibliothèques et d'applications diverses réparties sur le web, dans des dépôts publics et privés, allant de petits utilitaires à de grandes applications d'entreprise. Ces bases de code étrangères, remplies de logique métier, de fonctionnalités génératrices de revenus, de code hautement spécifique, sont ce qui rend leurs fondations dignes d'exister.

Mais cet écosystème est d'une diversité extraordinaire. Certains dépôts reçoivent des commits tous les jours de la part de plusieurs contributeurs, certains reçoivent une mise à jour massive de temps en temps lorsque leurs mainteneurs ont un peu de temps libre, et certains n'ont pas été touchés depuis des années (parce que leur créateur a perdu intérêt, ou n'a tout simplement pas pu trouver quoi que ce soit à améliorer). Certains ont des tests multi-versions de type Tox et une intégration continue, certains n'ont même pas un seul test unitaire.

Alors, que se passe-t-il lorsque les développeurs suivent cette philosophie tendance "Marche ou meurs" ? L'écosystème, déjà fortement fragmenté par le langage (python2vs3, ruby, go, php... juste pour les langages dynamiques), par le format de fichier et le protocole réseau, par le framework et le style d'exécution (sync vs async), se fragmente encore plus. De la manière la plus silencieuse et mortelle. En gros, si nous considérons les bases de code dépendant d'un framework ou d'une bibliothèque (ici appelé "le logiciel") :

* Les dépôts qui n'ont pas été mis à jour depuis quelques années sont cassés par défaut.
* Les dépôts qui sont activement maintenus, mais ne ciblent pas la même version du logiciel que nous, ne fonctionnent pas non plus.
* Les trackers de bugs se remplissent de tickets inutiles "Plz ajoutez le support pour la version X.Y.Z" ou "Plz restaurez le support pour la version X.Y.Z".
* Les forks fleurissent autour de dépôts légèrement renommés ; des forks qui ne peuvent pas être fusionnés, puisque chacune de leurs modifications est très susceptible de casser les choses pour d'autres versions du logiciel ; et les améliorations ultérieures apportées par chaque forkeur, étant enchaînées à des bases de code divergentes, continuent de se propager sans jamais être fusionnées ; naturellement, elles sont refaites par plusieurs développeurs chacun de son côté, puisque peu d'entre eux prennent le temps de revoir le graphe des forks et de cherry-picker les commits intéressants.
* Les plus grands projets reçoivent parfois assez de gentillesse pour fournir une matrice de compatibilité, ou des "ensembles de travail connus" épinglés à leur numéro de version de patch. Mais dès que vous avez plus de quelques dépendances, vous entrez dans un enfer de dépendances qu'aucun algorithme de résolution de conflits ne peut aborder ; vous devez simplement forker, forker, forker, et monkey-patcher, jusqu'à ce que vos dépendances trouvent un accord.
* Les exigences du projet se remplissent de liens vers des dépôts git et des hachages de commit ; des données sans sémantique qui rendront les prochaines mises à jour encore plus expérimentalement maladroites ; ou qui disparaîtront en raison d'un "force-push" inattendu.
* Sans surprise, de nombreux mainteneurs de ces applications pluggables ne veulent pas prendre sur eux le fardeau supplémentaire de remplir leur code de cas spéciaux, pour contourner la frénésie de rupture des développeurs du logiciel principal. En conséquence, l'enfer des dépendances continue de s'étendre sans retenue.

Alors, lorsque nous pluralisons fièrement le nom d'un sous-module, lorsque nous supprimons une classe utilitaire prétendument peu utilisée, lorsque nous faisons d'un argument optionnel un argument obligatoire, nous n'améliorons rien. Nous tuons simplement la praticité au nom de la pureté esthétique. Nous détruisons sans réfléchir des régions entières de l'écosystème logiciel, transformant des gazillions de suites de tests en cauchemars rougeâtres. Mais nous ne saurons jamais dans quelle mesure ; surtout si nous ne vérifions pas. L'ignorance est un bonheur.

Les écosystèmes biologiques peuvent atteindre les profondeurs de l'abysse ou d'autres planètes s'ils ont suffisamment de temps ; lorsque les choses changent trop rapidement, c'est l'extinction de masse. Les écosystèmes logiciels ne sont pas différents. Profiter de la propreté d'une API "refait à partir de zéro" est comme profiter de la stérilité microbienne d'une forêt vitrifiée par une explosion nucléaire.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/meme_cant_break_compat.png)

Certes, c'est une fausseté de penser que parce que nous utilisons un logiciel open-source, nous avons droit aux corrections de bugs et aux fonctionnalités que nous demandons. Mais c'est également faux de penser que parce que les utilisateurs de notre framework/bibliothèque ne sont pas des clients payants, nous ne leur devons rien. Ils nous ont fait confiance, ont construit leur propre code contre le nôtre, ont suivi nos conventions et nos meilleures pratiques, alors qu'ils auraient pu choisir un autre langage/framework/bibliothèque. Comment pouvons-nous justifier de piétiner leurs propres efforts, de leur faire perdre des jours ou des semaines de développement, juste parce que nous avons soudainement ressenti l'irrésistible envie de changer un schéma de nommage, ou de supprimer du code parfaitement fonctionnel ? Nous sommes tous interdépendants dans un écosystème logiciel, et une petite dose de conscience, de prudence et de rationalité peut aller très loin. "_Mais vous n'êtes jamais sûr qu'un changement ne casse pas les choses_", diront certains en haussant les épaules. Certes. Personne ne demande la perfection. Mais ne pas être délibérément nuisible est déjà un très bon début.

Il y a comme une humeur paternaliste derrière certains défenseurs de l'approche "marche ou meurs". "_Si nous nous en tenons à la stabilité de l'API, les contributeurs deviendront paresseux et ne mettront jamais à jour leurs modules, l'écosystème pourrira sur place au lieu d'avancer_". Oh, que c'est dangereux, de faire le bien des gens contre leur gré. Si nous voulons que les utilisateurs mettent à jour leur base de code, au contraire, nous devrions commencer par ne pas casser brutalement les choses. Nous devrions apporter de nouvelles fonctionnalités brillantes, pas juste un pistolet sur leur tempe. Nous devrions les laisser corriger les avertissements de "dépréciation" légèrement ennuyeux lorsqu'ils en ont envie et peuvent le faire, pas **maintenant**. Nous devrions les laisser passer leur temps sur des contributions utiles, pas sur la réparation de ce que nous avons cassé avec l'obsolescence programmée que nous osons appeler "progrès".

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Compatibility-of-Hardware-and-Software.png)

Faits amusants : annoncer des changements cassants dans les notes de version ne leur confère pas de légitimité ; et lorsqu'une API privée est si pratique qu'elle est utilisée par plusieurs projets, peut-être est-ce un signe qu'elle devrait être rendue publique et documentée, et non qu'elle devrait être détruite au premier caprice.

Alors, gravons-le dans le marbre de nos bureaux : la stabilité de l'API est, doit être, en haut de notre liste de préoccupations ; avec la robustesse et l'adéquation avec les besoins des utilisateurs finaux ; mais infiniment au-dessus de toute considération esthétique. Seule la compatibilité à long terme peut permettre à nos écosystèmes logiciels de croître d'une petite élite d'applications constamment mises à jour, à une énorme et diverse galaxie de modules ; certains mis à jour hier, d'autres mis à jour il y a dix ans, mais tous **faisant avancer les choses**. Parce que c'est de cela qu'il s'agit avec le logiciel, et c'est pour cela que les gens sont payés, à la fin de la journée. Pas pour perdre du temps à réparer la roue qui fonctionnait hier, et ne fonctionnera plus jamais demain, parce que nous avons entendu l'appel du vide.

## Le concept de Compat Patcher

Est-ce que je demande aux mainteneurs de logiciels (open source) de faire plus d'efforts, afin d'atteindre cette stabilité de l'API à long terme si cruciale ? Non. Je n'oserais pas. Au contraire, je leur demande d'être plus paresseux. Mais le bon, le sensé, le genre de paresse à la fois égoïste et bienveillante.

Plus de compatibilité signifie moins de demandes de support, moins de temps à justifier des changements controversés, et plus de contributions de fonctionnalités/corrections de bugs de notre communauté. Plus de compatibilité ne signifie même pas plus de frappe au clavier. Sauf si nous ne faisons que des projets jouets, nous avons déjà mis en place des shims de compatibilité pendant un certain temps. Une seule chose à faire : **les laisser tranquilles**. Ils ne nous font pas de mal. Ils ne gaspillent pas d'espace disque. Ils valent probablement des milliers de dollars par caractère. Évitons simplement un commit sauvage "Suppression du shim de compatibilité XYZ", et passons à des objectifs plus grands.

Et si la simple vue d'un shim de compatibilité nous donne envie de vomir (une pathologie pas si inhabituelle, je suppose), il y a une excellente nouvelle : avec les langages de haut niveau, nous n'avons plus besoin de shims dans notre code. Nous devons simplement adopter le concept de **Compatibility Patcher** (ou "compatcher" pour les amateurs de néologismes).

Wat-iz-dat ? Juste une bibliothèque compagne, vivant souvent sa propre vie dans son propre dépôt, qui se connecte au logiciel réel au moment du démarrage, et restaure sa compatibilité avec une décennie de ses versions précédentes. Ainsi, nous pouvons garder notre base de code entièrement ignorante de ce que pourrait être une "dépréciation", tout en maintenant une coexistence symbiotique avec les milliers de modules vivant dans notre écosystème.

Le monkey-patching est laid, quelqu'un a dit ? Peut-être, mais jamais aussi laid que de passer des heures à rétro-ingénier une architecture de plugin entière, juste pour réaliser qu'un "S" supplémentaire dans les conventions de nommage suffisait à tout ruiner. Les seigneurs de la programmation pourraient préférer tisser leur code avec des shims externes en utilisant la [programmation orientée aspect](https://en.wikipedia.org/wiki/Aspect-oriented_programming), mais pour la plupart d'entre nous, simples mortels, la simplicité et le pragmatisme sont largement suffisants. Un peu de documentation, de journalisation et d'avertissements de console sont "explicites" suffisamment pour que tout le monde garde le contrôle sur la base de code.

Ne sous-estimons pas le pouvoir des langages de haut niveau. Exemples avec Python. Nous renommons un sous-module ? Très bien, grâce aux hooks d'importation, "_from framework import oldmodule_" et "_from framework import newmodule_" retourneront le même objet exact. Nous changeons la signature d'une fonction ? Une petite injection plus tard, l'ancien ensemble de paramètres d'appel sera automatiquement adapté et transféré à la nouvelle signature. Nous déplaçons un groupe entier d'utilitaires hors du dépôt principal ? Très bien, mais tant que nécessaire, le patcher de compatibilité les récupérera depuis leur nouvel emplacement, et les réinjectera là où ils appartenaient autrefois si bien. Nous renommons des constantes, des classes, des fonctions ? Laisser un alias ne coûtait qu'une seule ligne de code, maintenant avec les patchers de compatibilité, cette ligne n'a même plus à blesser nos yeux et nos cœurs.

Veuillez noter, les Compat Patchers agissent comme des voyageurs dans le temps. Ils fonctionnent même lorsque les développeurs suppriment une fonction, la réajoutent sous une forme différente, puis la suppriment à nouveau. Ils fonctionnent même lorsque les développeurs modifient de manière imprudente les comportements des fonctions, par exemple en échangeant des arguments similaires en place. Alors imaginez lorsque les développeurs coopèrent avec ce système, et découplent proprement les préoccupations de programmation afin que le patch soit minimal !

Cerise sur le gâteau, en séparant le code "de l'art" et les shims de compatibilité, les Compat Patchers facilitent l'**activation sélective des ensembles de compatibilité**. Votre projet est tout neuf et ne repose que sur des bibliothèques de pointe ? Très bien, désactivez l'ensemble du patcher. Vous avez juste besoin de la compatibilité avec les deux dernières versions majeures du framework ? Activez simplement les familles de shims correspondantes. Vous avez besoin du support pour des packages très anciens ? Laissez la configuration du patcher en mode maximal.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/unicorn-deviant.PNG)
_Ce sentiment lorsque les 30 dépendances fonctionnent sans problème dès la première installation_

Maintenant vient la partie anxiogène : quels sont les inconvénients des Compat Patchers ? Réponse : jusqu'à quelques secondes de retard au démarrage (lorsque tous les shims sont activés), et quelques opérations logiques et vérifications de type ici et là à l'exécution. C'est tout. Dans le monde web moderne, où la plupart des processus serveur fonctionnent pendant des heures sans interruption, traitent les formats les moins optimisés (basés sur du texte) concevables, et où les performances dépendent beaucoup plus de l'optimisation de la base de données et de la mise en cache appropriée que de la vitesse d'exécution brute, cela semble être une dépense légitime, n'est-ce pas ?

_Edit_ : une autre limitation des Compat Patchers est qu'ils nécessitent une toute petite coopération de la part des développeurs principaux. En effet, nous savons tous implicitement la règle de la compatibilité ascendante : "**Ajoutez uniquement des options**". Ajoutez de nouveaux arguments optionnels, ajoutez de nouvelles fonctions, ajoutez de nouveaux modules ; ne supprimez pas d'éléments et de comportements, ne rendez pas les anciennes options obligatoires. Mais il y a une règle supplémentaire, en or : **ne changez jamais, jamais, la sémantique des choses en place**. Si nous changeons la signification d'un argument, le format d'une sortie, l'action d'un appelable, sans aucun indicateur supplémentaire, alors la mise en place de shims devient (presque) irréalisable ; dans ce cas, même les Compat Patchers ne pourront pas résoudre cette ambiguïté, et deviner le comportement que nos utilisateurs demandaient lorsqu'ils utilisaient notre API. Bannissons à jamais ces types de changements [brutaux](https://docs.djangoproject.com/en/2.2/releases/2.2/#admin-actions-are-no-longer-collected-from-base-modeladmin-classes) et [inamicaux](https://serverfault.com/questions/829754/why-did-the-format-of-nginx-ssl-client-i-dn-suddenly-change).

## Passons à la pratique !

Les patchers de compatibilité ne sont pas que des vœux pieux.

[En voici un](https://github.com/pakal/django-compat-patcher) pour le célèbre framework web Django. Avec quelques dizaines de petits correctifs, il permet d'utiliser des applications pluggables ciblant les versions 1.6 à 2.2 du framework. Et ce n'est qu'un début - les demandes de fonctionnalités et les commentaires sont les bienvenus.

Ce patcher est utilisé en production sur quelques sites, y compris le portail [Pychronia](https://github.com/ChrysalisTeam/pychronia) et son écosystème CMS/Blog. Il fonctionne sur [CompatPatcherCore](https://github.com/pakal/compat-patcher-core), un micro-framework Python pour créer de telles applications compagnes en un clin d'œil (une [recette cookiecutter](https://compat-patcher-core.readthedocs.io/en/latest/startup.html) est même incluse).

Sans surprise, je vous encourage vivement à démarrer un Compat Patcher pour le framework/bibliothèque que vous pourriez maintenir, sauf si vous êtes l'un des rares esprits vaillants déjà fortement engagés dans la stabilité de l'API.

Ce concept devrait également être facile à porter vers Ruby, PHP, Javascript, et autres langages à haute malléabilité. Avec des langages de bas niveau et statiques, la tâche pourrait être beaucoup plus difficile (et nécessiter des processeurs de macros et similaires), mais qui sait.

**Nous y voilà. Les ruptures de mise à jour ne sont pas une fatalité. Juste une mauvaise habitude que nous devons _briser_, grâce à un peu de réflexion et quelques finesse techniques. Nous pouvons ainsi profiter des délices des écosystèmes logiciels en constante croissance et en constante évolution, ceux qui rendent le développement amusant et excitant !**

_Edit 2019/07/05 : Évoquer la "rareté des ressources" comme une raison possible du manque de shims, et ajuster le ton de cette partie._

_Edit 2019/07/14 : Corriger les fautes de frappe, et avertir contre les changements sémantiques en place._

![Image](https://www.freecodecamp.org/news/content/images/2019/06/windowsserver_article_012.jpg)