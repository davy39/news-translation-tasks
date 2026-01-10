---
title: Concepts de codage difficiles expliqués avec des analogies simples de la vie
  réelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-08T19:12:40.000Z'
originalURL: https://freecodecamp.org/news/hard-coding-concepts-explained-with-simple-real-life-analogies-280635e98e37
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_vKRQ66IBIliuqjqkQBLUQ.png
tags:
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Concepts de codage difficiles expliqués avec des analogies simples de la
  vie réelle
seo_desc: 'By Samer Buna

  How to explain coding concepts like streams, promises, linting, and declarative
  programming to a 5-year-old

  I love thinking about coding concepts by comparing them to familiar things we know
  in life. There are so many analogies out ther...'
---

Par Samer Buna

#### Comment expliquer des concepts de codage comme les flux, les promesses, le linting et la programmation déclarative à un enfant de 5 ans

J'adore réfléchir aux concepts de codage en les comparant à des choses familières que nous connaissons dans la vie. Il existe de nombreuses analogies sur les concepts de codage. Certaines sont bonnes tandis que d'autres sont confuses, principalement parce qu'elles se concentrent sur des aspects partiels d'un concept tout en ignorant beaucoup d'autres. Cet article résumera certaines des analogies que je pense être les mieux adaptées à quelques concepts de codage de manière complète.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_vKRQ66IBIliuqjqkQBLUQ.png)
_Avertissement : ne lisez pas cet article l'estomac vide_

> **Mise à jour :** Cet article fait maintenant partie de mon livre « The Professional Programmer ».

> Lisez la version mise à jour de ce contenu et d'autres conseils de programmation sur [**jscomplete.com/pro-programmer**](https://jscomplete.com/g/coding-analogies).

Je vais commencer par des concepts simples et passer à des concepts plus difficiles. Commençons par le codage lui-même. Le codage peut être comparé à l'écriture de recettes de cuisine. Une recette dans cette analogie est le programme et le cuisinier est l'ordinateur. Une recette est une liste d'instructions pour un cuisinier à suivre et un programme est une liste d'instructions pour un ordinateur à exécuter.

C'est une analogie très simple étant donné qu'une recette est écrite dans une langue humaine et qu'un programme est écrit dans une langue informatique et que ces langues sont très différentes (sauf si vos recettes ont des fermetures et des promesses !). Il n'y a également pas beaucoup de choses inattendues à prévoir dans une recette tandis qu'un programme informatique en aura beaucoup. Malgré sa simplicité, c'est une bonne façon de montrer comment un ordinateur exécute une liste d'instructions séquentiellement. Cela montre également comment une ligne d'instruction peut utiliser n'importe quel résultat de l'exécution des lignes d'instruction précédentes.

Certaines recettes auront même des [instructions conditionnelles](https://medium.com/@samerbuna/coding-tip-try-to-code-without-if-statements-d06799eed231) : si vous cuisinez pour 2, 4 ou 8 personnes ! Certaines recettes auront des [boucles](https://medium.com/@samerbuna/coding-tip-try-to-code-without-loops-18694cf06428) : continuez à battre ce mélange jusqu'à...

J'aime aussi cette analogie à cause de tous les ingrédients et outils prêts à l'emploi que vous pouvez utiliser dans vos recettes — comme le mélange pour gâteau que vous pouvez utiliser pour faire des cupcakes et ce moule spécialement conçu qui rend la création de cupcakes tellement plus facile.

L'utilisation d'ingrédients et d'outils prêts à l'emploi est comme inclure et utiliser un paquet de code écrit par d'autres dans votre propre code.

```
// La fabrication d'un cupcake// Premières étapes :
```

```
$ npm install cake-mix$ npm install cupcake-pan
```

[_NPM_](https://www.npmjs.com/) est le gestionnaire de paquets pour [_Node.js_](https://nodejs.org/en/), qui est un _framework_ très populaire pour écrire des applications JavaScript. Dans cette analogie, Node.js est comme la cuisine elle-même. Il vous permet d'exécuter des lignes dans vos recettes en utilisant des modules intégrés comme votre four et votre évier.

En parlant de nourriture malsaine, cette prochaine analogie est pour apprendre à coder et est comparée aux habitudes alimentaires. J'adore particulièrement cette analogie et ce qu'elle convey car elle m'aide à rester sur la bonne voie dans mon parcours d'apprentissage du code. Pour moi, cela a commencé au lycée et continuera jusqu'à ce que mon cerveau atteigne sa dernière instruction : die();

#### Apprendre à coder

Apprendre à coder est comme essayer de perdre du poids. Cette analogie s'applique à l'apprentissage de n'importe quoi, vraiment, mais apprendre à coder est un cas spécial ici.

"Perdre du poids" est un terme négatif. Nous devrions vraiment l'appeler "Gagner de la santé". En ce sens, il est très comparable à "Gagner des connaissances". Les ressources éducatives que vous avez à votre disposition sont comme vos options alimentaires. Certaines sont juste correctes, certaines sont excellentes, et certaines sont complètement mauvaises pour vous. Manger sainement et faire de l'exercice sont les deux activités principales qui vous aideront à gagner en santé. De même, consommer de bonnes ressources éducatives et pratiquer le codage manuellement sont les deux activités principales qui vous aideront à gagner de bonnes connaissances en codage.

Alors, comment apprenez-vous "sainement" ? Lorsque vous vous engagez à manger sainement, vous utilisez des filtres comme _biologique_, _local_, _réduit en gras_, _nourri à l'herbe_, et _non-OGM_. C'est exactement la même chose avec les ressources éducatives saines sauf que ces étiquettes ne sont pas encore aussi claires. J'espère que les ressources éducatives auront un jour des étiquettes vérifiables et pertinentes également. Peut-être des étiquettes comme "non-sponsorisé", "sans-marketing", "approuvé-par-des-experts", "édité-de-manière-stricte", et "attention-aux-dragons".

Pourtant, au lieu de filtrer par le contenu, vous pouvez facilement filtrer par les bonnes marques. Je fais cela avec la nourriture aussi. Je connais et fais confiance à quelques marques et j'utilise principalement celles-ci. C'est plus facile. Avec les ressources éducatives, il y a certaines marques (publications et personnes) que vous devriez simplement suivre tout le temps.

Après avoir filtré votre consommation de connaissances pour ne garder que les bonnes ressources, vous devez simplement faire de l'exercice ! Pratiquez tout ce que vous apprenez, mais pas seulement en refaisant exactement ce que vous avez appris. Challengez-vous également à faire quelque chose de légèrement différent autour des sujets que vous avez appris. Si vous avez de la chance, vous serez bloqué ! Ensuite, vous apprendrez définitivement autre chose lorsque vous serez débloqué.

L'exercice est bon pour le corps et l'esprit.

#### Variables

_Les variables sont utilisées dans les programmes informatiques pour contenir des données_. C'est une déclaration très simplifiée et elle est, à bien des égards, simplement fausse.

Les variables ne contiennent pas de données. Elles pointent simplement vers elles. Les données sont stockées dans la mémoire de l'ordinateur. Vous pouvez comparer les variables aux étiquettes que vous placez sur vos messages électroniques (ou notes, ou fichiers).

_Tous les exemples de code dans cet article sont écrits en JavaScript. [JavaScript est un langage informatique très facile à apprendre](https://medium.com/@samerbuna/lets-learn-coding-introduction-and-basics-65e31414a197)._

Dans Gmail, une étiquette est un pointeur vers un e-mail ou une liste d'e-mails. De nombreuses étiquettes peuvent pointer vers le même e-mail. Cela est similaire à l'assignation d'une autre variable à une variable existante :

```
let work = [email1, email2, email3];let important = work;
```

Work et important sont maintenant des étiquettes qui pointent vers la même liste exacte d'e-mails.

Certaines variables représentent des _références constantes_. Elles ne peuvent pas être changées. Cela est comme l'étiquette "envoyé" dans Gmail. Bien que nous puissions changer l'étiquette work ci-dessus et la faire pointer vers une liste différente d'e-mails, nous ne pouvons pas changer l'étiquette envoyé. Vous ne pouvez pas faire pointer l'étiquette _envoyé_ vers une liste différente d'e-mails. Vous ne pouvez que la faire pointer vers plus d'e-mails.

```
const sent = [];
```

```
// Vous ne pouvez pas changer la signification de sent maintenant// Mais vous pouvez ajouter plus de valeurs à celle-ci :
```

```
sent.push(new Email());
```

#### Erreurs et exceptions

L'expertise d'un programmeur est largement liée à la manière de gérer les erreurs. [Les programmeurs experts](https://medium.com/@samerbuna/software-engineering-is-different-from-programming-b108c135af26) adorent les erreurs car, pour eux, les erreurs signifient des progrès.

Parfois, nous nous attendons à voir ces merveilleux messages rouges et si nous ne les voyons pas, nous savons que le code est simplement faux !

J'adore la phrase "écouter votre code" car je pense que le code évolue en communiquant avec nous à travers des erreurs.

C'est exactement comme élever des enfants.

Le concept parental le plus important que j'ai réalisé, avec la pratique, est la manière dont les enfants communiquent en se comportant mal. C'est parce qu'ils n'ont pas encore un cerveau logique. Je pense que les programmes font exactement la même chose. Ils communiquent également en se comportant mal (en produisant des erreurs) parce que les programmes ne sont pas complètement logiques. Votre tâche en tant que programmeur est d'ajouter plus de logique dans le code pour gérer les cas qui ont initialement produit des erreurs. C'est exactement comme la tâche d'un parent qui est d'enseigner à l'enfant mal élevé ce qui ne va pas avec ce mauvais comportement et quoi faire différemment la prochaine fois.

Certaines erreurs ne sont pas récupérables et un programme rencontrant celles-ci devrait simplement quitter (et être redémarré). C'est comme si votre cœur s'arrêtait. Il n'y a pas grand-chose à faire sauf le redémarrer avec un choc électrique. C'est pourquoi nous surveillons nos programmes et les redémarrons lorsqu'ils atteignent cet état. Heureusement, le processus de redémarrage d'un programme n'est pas aussi dramatique.

La plupart des erreurs qui se produisent pendant le développement précoce des programmes aident à améliorer ces programmes afin que les erreurs ne se produisent plus. C'est ainsi que les bons enfants sont élevés. Ils ne répètent pas les mauvais comportements parce qu'ils ont maintenant une bonne logique pour les guider dans une bonne direction.

Certaines erreurs évoluent pour devenir des exceptions. Les exceptions sont des erreurs attendues. Des erreurs pour lesquelles nous pouvons planifier et nous en remettre. Le meilleur exemple de codage ici est une erreur de connexion réseau pendant que nous faisons un programme, par exemple, télécharger des données. C'est très attendu car nous savons que les connexions réseau peuvent être peu fiables, donc nous planifions cette erreur. Lorsque cette erreur se produit, étiquetons la tâche de téléchargement de ces données comme incomplète. Mettons-la en file d'attente quelque part, et réessayons plus tard (voir ci-dessous pour une analogie de la mise en file d'attente).

Ce que nous avons fait avec cette exception planifiée est de donner à l'ordinateur un ensemble différent d'instructions (une recette différente) à faire lorsque cette erreur se produit. Nous faisons exactement cela avec nos enfants également. Nous leur donnons des instructions sur ce qu'il faut faire dans certains scénarios futurs que nous attendons (ou craignons dans ce cas).

```
// Hey les enfantsif (stranger.offersYou(chocolate)) {  doNotAccept();  doNotTalkTo(stranger);  walkAway();}
```

```
if (stranger.triesToForceYouToDoSomething()) {  screamFor(help);  runAway();  call(911);}
```

#### Programmation réactive et flux

La programmation réactive est une méthode populaire pour écrire du code basée sur la _réaction aux changements_. Elle est inspirée de notre vie quotidienne et de la manière dont nous agissons et communiquons avec les autres. Lorsque nous effectuons des activités de la vie quotidienne, nous essayons de faire plusieurs choses à la fois lorsque nous le pouvons, mais le cerveau ne peut pas faire plusieurs choses à la fois, peu importe nos efforts. La seule façon pour les humains de faire plusieurs choses à la fois est de _changer de tâches_ et de les diviser efficacement pendant leur durée de vie. Cela a plus de sens lorsque les tâches que nous devons faire nécessitent une certaine quantité d'_attente_, ce qui est presque toujours le cas. En fait, nous changeons toujours de tâches, même lorsque nous n'en sommes pas conscients.

La programmation réactive consiste simplement à programmer en utilisant et en s'appuyant sur des _événements_ plutôt que sur l'ordre des lignes dans le code. Habituellement, cela implique plus d'un événement, et ces événements se produisent dans une séquence au fil du temps. Nous appelons cette séquence d'événements un "flux".

Pensez aux événements comme à tout ce qui pourrait se produire dans le futur. Par exemple, vous savez que Jane (une propriétaire de magasin) tweete toujours des choses intéressantes sur Twitter. Chaque fois qu'elle tweete quelque chose, nous appelons cela un "événement". Si vous regardez le fil Twitter de Jane, vous avez une séquence d'"événements" qui se produisent au fil du temps (un flux d'événements). La programmation réactive est ainsi nommée car nous pouvons "réagir" à ces événements. Par exemple, imaginez que vous attendez que Jane tweete un code promotionnel sur quelque chose de cool qu'elle vend dans son magasin. Vous voulez "réagir" à ce tweet et acheter la chose cool en utilisant le code promotionnel. Dans une image simplifiée, c'est exactement ce qu'est la programmation réactive.

Pour pouvoir réagir à un événement, nous devons le _surveiller_. Si nous ne suivons pas l'événement, nous ne saurons jamais quand réagir. Sur Twitter, pour surveiller les événements de Jane qui tweete, nous suivons Jane et configurons notre téléphone pour nous notifier chaque fois qu'elle tweete. Lorsqu'elle le fait, nous regardons le tweet et prenons une décision sur le fait de réagir davantage ou non.

En programmation réactive, le processus de surveillance d'un événement est connu sous le nom d'écoute ou d'_abonnement_ à l'événement. Cela est, en fait, très similaire à l'abonnement à une newsletter. Lorsque vous vous abonnez à une newsletter sur le Web, vous fournissez votre adresse e-mail. Chaque fois qu'il y a un nouveau numéro de la newsletter, votre adresse e-mail sera utilisée comme moyen pour vous de recevoir une copie du numéro. De même, nous nous abonnons à un flux d'événements avec une fonction. Chaque fois qu'il y a un nouvel événement, le flux utilisera la fonction pour permettre à notre code de réagir à l'événement. Dans cette analogie, la plateforme de newsletter est le flux d'événements. Chaque numéro de la newsletter est un événement et votre e-mail est la fonction que vous utilisez pour vous abonner au flux d'événements.

Maintenant, imaginez une newsletter dynamique qui vous permet de sélectionner des sujets et de vous envoyer uniquement les articles qui correspondent à vos sujets. Vous filtrez essentiellement les numéros de la newsletter selon vos préférences et c'est quelque chose que nous pouvons également faire sur les flux d'événements. De plus, imaginez que vous vous êtes abonné à plusieurs newsletters en utilisant différentes adresses e-mail. Vous avez ensuite décidé que vous voulez que tous les numéros des newsletters soient envoyés à une nouvelle adresse e-mail unique. Une chose facile que vous pouvez faire est de configurer une règle de messagerie qui transfère tout numéro de toute newsletter à la nouvelle adresse e-mail. Vous fusionnez essentiellement plusieurs numéros de newsletters en une seule adresse e-mail, ce qui est une autre chose que nous pouvons faire avec les flux d'événements.

Une autre façon de penser aux flux d'événements est de les comparer à des tableaux réguliers. Ils sont en fait très similaires. Les tableaux sont une séquence de valeurs dans l'espace tandis que les flux d'événements sont une séquence de valeurs dans le temps. En programmation réactive, toutes les opérations fonctionnelles que nous pouvons faire sur un tableau. Le filtrage, la réduction, la cartographie, la combinaison, le pipelining peuvent tous être faits sur des flux d'événements. Nous pouvons filtrer un flux d'événements, réduire les valeurs d'un flux d'événements, mapper un flux d'événements à un autre, combiner des flux et faire d'un flux une entrée pour un autre. Ce sont toutes des options qui produisent de nouveaux flux de valeurs dans le temps.

#### Callbacks et promesses

Imaginez que vous demandez à quelqu'un de vous donner quelque chose qui nécessite un certain temps pour être préparé. Ils prennent votre commande et votre nom et vous disent d'attendre qu'on vous appelle lorsque votre commande est prête. Après un certain temps, ils appellent votre nom et vous donnent ce que vous avez demandé.

Le nom que vous leur avez initialement donné est la fonction de _callback_ ici. Ils l'ont appelée avec l'objet qui était demandé.

C'est comme lorsque vous commandez un latte chez Starbucks (dans le magasin, pas au drive-in). Ils enregistrent votre commande et votre nom de manière synchrone, puis vous attendez qu'on appelle votre nom. Lorsque cela se produit, vous recevez votre latte :

```
starbucks.makeMeALatte({ type: 'Vanilla', size: 'Grande' }, Samer);
```

```
// "Samer" ici est la fonction de callback.// Lorsque le Latte est prêt, le barista appellera Samer // avec l'objet prêt// Nous définissons une fonction Samer pour traiter l'objet prêt
```

```
function Samer(readyLatte) {  // boire readyLatte}
```

Maintenant, imaginez que vous demandez à quelqu'un de vous donner quelque chose, mais qu'il vous donne autre chose. Appelons cela un objet mystère. Ils vous promettent que cet objet mystère pourrait éventuellement se transformer en la chose que vous avez initialement demandée.

Cette promesse d'objet mystère peut se transformer en l'une des deux formes possibles. Une forme est associée au succès et l'autre à l'échec.

C'est comme lorsque nous demandons à une poule un poussin et que la poule nous donne un œuf. Cet œuf pourrait se transformer avec succès en un poussin ou il pourrait mourir et être inutile.

```
const egg = chicken.makeChick();   // C'est une promesse !
```

```
egg.then(chick => raiseChick())    // Résultat de succès   .catch(badEgg => throwBadEgg()) // Résultat d'échec
```

#### Files d'attente et piles

Lorsque nous travaillons avec des éléments de données, il existe deux structures de données populaires pour stocker et utiliser ces éléments : une pile _LIFO_ et une file d'attente _FIFO_.

LIFO signifie _Last In First Out_ et FIFO signifie _First In First Out_.

L'analogie la plus simple d'une pile de données est la pile de vaisselle sale dans votre évier. Lorsque vous avez fini d'utiliser une assiette, vous l'empilez sur le dessus de la vaisselle sale existante jusqu'à ce que vous soyez prêt à la laver.

Lorsque vous êtes prêt à la laver, vous prenez la dernière assiette sale que vous avez empilée et vous la lavez. En termes informatiques, nous disons que vous avez "dépilé" une assiette.

La _dernière_ assiette que vous avez empilée est la _première_ assiette que vous avez lavée. C'est LIFO.

L'analogie la plus simple d'une file d'attente de données est la file de personnes qui se forme devant une caisse ou un poste de commande. Lorsque vous êtes prêt à payer pour vos courses et à les emporter chez vous, vous devrez peut-être vous mettre en file d'attente jusqu'à ce que ce soit votre tour.

La première personne à arriver à cette file d'attente sera la première personne à en finir. C'est FIFO.

#### Programmation en binôme

Vous pouvez conduire votre voiture seul lorsque vous allez dans des endroits familiers, mais lorsque vous devez aller quelque part loin pour la première fois, vous utilisez un GPS. Si vous avez quelqu'un d'autre dans la voiture avec vous, une meilleure option serait de le faire naviguer en vous donnant les instructions sur où tourner ensuite. Si vous ne suivez pas les instructions et finissez par prendre un mauvais tournant, ils vous le feront savoir immédiatement et vous conseilleront sur la manière de le corriger.

Avoir un navigateur à côté de vous lorsque vous conduisez est comme avoir un partenaire de programmation. Vous ne conduisez pas seul. Vous êtes une équipe avec le même objectif : arriver à destination en toute sécurité, sans aucun problème, et avec le moins de temps et d'efforts possibles.

Vous pouvez probablement le faire vous-même sans un navigateur humain ou un GPS sophistiqué en utilisant la méthode à l'ancienne et en vérifiant une carte avant de partir. Si nécessaire, vous pouvez vérifier la carte à nouveau. Si vous vérifiez la carte en conduisant, vous pourriez accidentellement heurter un trottoir ou mettre un coup dans la voiture. Si vous vous arrêtez pour vérifier la carte, vous perdrez du temps. Sans ce partenaire navigateur, vous n'êtes pas aussi en sécurité et/ou le voyage prendra beaucoup plus de temps.

L'expérience de votre partenaire navigateur pourrait également vous apprendre de nouvelles choses. Ils pourraient connaître un nouveau raccourci que vous ne connaissez pas et qui n'est pas sur la carte. Vous apprenez de leur expérience pertinente, et cela est au-delà de la valeur.

Si vous devez aller à deux destinations et que vous avez deux voitures. Vous pourriez être tenté de penser qu'il serait plus rapide de conduire seul et de faire les destinations en parallèle. Cela pourrait être plus rapide à court terme, mais toutes choses considérées, le temps pourrait ne pas être le facteur le plus important ici. En ce qui concerne les programmes informatiques, utiliser une voiture et s'assurer qu'elle est sans bosses à la fin des deux trajets pourrait être un facteur bien plus important. C'est pourquoi nous aimons la programmation en binôme.

#### Linting et automatisation des tâches

Si vous devez conduire seul lors de ce long voyage, vous pouvez toujours rendre votre trajet plus sûr en vous appuyant sur des outils. Une carte est un outil. Le GPS est un meilleur outil. Le régulateur de vitesse est un autre outil.

Les outils qui vous avertissent automatiquement si vous faites quelque chose de mal en conduisant sont similaires aux outils de _linting_ pour le codage. En JavaScript, le meilleur outil de linting aujourd'hui est ESLint. Il vous avertira de nombreuses choses incorrectes que vous ne devriez pas faire en codant. Le meilleur de tout, il peut le faire même avant que vous n'exécutiez votre programme.

Les exemples d'outils qui vous avertissent pendant que vous conduisez évoluent dans les voitures modernes. Les voitures peuvent maintenant vous avertir lorsque vous franchissez une ligne de voie de manière inattendue, ou lorsque vous essayez de tourner ou de changer de voie sans voir cette voiture cachée dans votre angle mort. De plus, elles vous avertissent lorsque vous dépassez la limite de vitesse, ou lorsque vous êtes sur le point de heurter quelque chose en essayant de vous garer dans un endroit étroit.

Les outils de linting évoluent également pour fournir des avertissements plus précis et utiles. ESlint me surprend toujours avec des avertissements très précis. De plus, ses recommandations par défaut s'améliorent avec chaque mise à jour.

Une autre analogie que j'adore dans les voitures modernes est l'automatisation. Toute tâche que vous répétez souvent devrait être automatisée une fois que son but et sa valeur sont clairs. Au lieu de redémarrer ce programme chaque fois que vous enregistrez le fichier, avez un processus de surveillance qui automatise cela. Plutôt que d'exécuter une commande de formatage sur votre code avant de le partager avec d'autres, avez une commande qui le fait automatiquement chaque fois que vous validez votre code dans le contrôle de source.

Les voitures modernes automatisent également tant de choses. L'exemple évident ici est le régulateur de vitesse adaptatif, mais d'autres exemples subtils incluent les essuie-glaces automatiques et les phares automatiques la nuit (mon préféré !).

#### Programmation impérative vs déclarative

Lorsque vous devez faire quelque chose, il y a toujours les aspects _quoi_ et _comment_. Qu'est-ce qui doit exactement être fait et comment le faire.

La programmation impérative concerne le _comment_. La programmation déclarative concerne le _quoi_.

_Quoi ? Comment ? Et pourquoi devriez-vous vous en soucier ?_

Une approche impérative représente une liste d'étapes. Faites ceci d'abord, puis faites cela, et après cela faites autre chose. Par exemple : _Passez en revue une liste de nombres un par un et pour chacun ajoutez sa valeur à une somme en cours._

Une approche déclarative représente ce que nous avons et ce dont nous avons besoin. Par exemple : _Nous avons une liste de nombres et nous avons besoin de la somme de ces nombres._ Le langage impératif est plus proche des ordinateurs d'aujourd'hui car ils ne savent exécuter que des instructions. Le langage déclaratif est plus proche de notre façon de penser et de commander. Faites-le, s'il vous plaît. D'une manière ou d'une autre !

La bonne nouvelle est que les langages informatiques ont évolué. Les langages informatiques offrent des moyens déclaratifs de faire les instructions informatiques impératives nécessaires. Tout comme les voitures ont évolué des changements de vitesse manuels vers les automatiques et les voitures autonomes !

La programmation impérative est comme conduire une voiture à changement de vitesse manuel. Vous devez faire des étapes manuelles (appuyer sur l'embrayage, le relâcher lentement, changer les vitesses progressivement, etc.). La programmation déclarative est comme conduire une voiture automatique — vous spécifiez simplement le "quoi" : Park ou Drive.

Vous ne pouvez pas programmer de manière déclarative à moins d'avoir les outils qui vous permettent de le faire. Bien que vous puissiez conduire une voiture automatique de manière impérative (en passant en mode manuel), vous ne pouvez pas conduire une voiture à changement de vitesse manuel de manière déclarative. Si tout ce que vous avez est une voiture à changement de vitesse manuel, la programmation impérative est votre seul choix évident. À moins que vous ne preniez le temps d'installer un changement de vitesse automatique, ce qui pourrait en valoir la peine à long terme. Si vous pouvez vous permettre une nouvelle voiture, vous opterez probablement pour une automatique à moins que vous ne soyez ce vrai nerd qui aime encore programmer en Assembleur !

[_Assembleur_](https://en.wikipedia.org/wiki/Assembly_language) _est le langage informatique impératif original de bas niveau avec des instructions pures qui se traduisent directement en code machine._

Notez que la programmation impérative peut produire des programmes plus rapides. De plus, la programmation déclarative nécessite moins d'efforts de votre part. En général, elle nécessitera également moins d'efforts pour être maintenue. Le codage n'a pas à être d'une manière ou d'une autre. Tout programme informatique non trivial aura probablement un peu des deux approches. De plus, savoir coder de manière déclarative est génial, mais cela ne signifie pas que vous n'avez pas besoin d'apprendre les méthodes impératives également. Vous devriez simplement être confiant en utilisant les deux.

Les outils qui vous permettent de programmer de manière déclarative évoluent vers de meilleures et plus rapides façons de vous amener là où vous allez. L'expérience déclarative ultime avec les voitures modernes est celle des voitures autonomes. Le "quoi" devient la destination et la voiture fera le reste. C'est probablement, d'une certaine manière, l'avenir de la programmation également. Nous aurons des programmes qui comprennent tous les objectifs et ils peuvent simplement travailler leur magie pour générer une logique pour nous amener à ces objectifs.

_Quelle est votre analogie préférée ? Faites-le moi savoir dans la section des réponses ci-dessous._

Merci d'avoir lu !