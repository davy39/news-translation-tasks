---
title: Quelle est la différence entre JavaScript et ECMAScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-28T17:51:16.000Z'
originalURL: https://freecodecamp.org/news/whats-the-difference-between-javascript-and-ecmascript-cba48c73a2b5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*zdzWJW4DiWkFjDnY.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Quelle est la différence entre JavaScript et ECMAScript ?
seo_desc: 'By Michael Aranda

  I’ve tried googling “the difference between JavaScript and ECMAScript.”

  I ended up having to wade through a sea of ambiguous and seemingly conflicting results:

  “ECMAScript is a standard.”

  “JavaScript is a standard.”

  “ECMAScript is a...'
---

Par Michael Aranda

J'ai essayé de chercher sur Google « la différence entre JavaScript et ECMAScript ».

J'ai fini par devoir traverser une mer de résultats ambigus et apparemment contradictoires :

« ECMAScript est une norme. »

« JavaScript est une norme. »

« ECMAScript est une spécification. »

« JavaScript est une implémentation de la norme ECMAScript. »

« ECMAScript est du JavaScript standardisé. »

« ECMAScript est un langage. »

« JavaScript est un dialecte de ECMAScript. »

« ECMAScript **est** JavaScript. »

![Image](https://cdn-media-1.freecodecamp.org/images/M484XDZ0RUsuBCsMGdAfeyMscLf0t9Z2L39I)

Réprimant l'envie de pleurer, je me suis repris et j'ai décidé de m'engager dans une recherche douloureuse mais productive.

Cet article représente ma compréhension actuelle des différences entre JavaScript et ECMAScript. Il s'adresse aux personnes qui sont familières avec JavaScript mais qui souhaitent une compréhension plus claire de sa relation avec ECMAScript, les navigateurs web, [Babel](https://babeljs.io/), et plus encore. Vous apprendrez également les langages de script, les moteurs JavaScript et les environnements d'exécution JavaScript pour faire bonne mesure.

Alors, préparez-vous.

### Un glossaire JavaScript/ECMAScript

Ci-dessous se trouve une liste de définitions, conçues avec un accent sur la cohérence et la clarté. Les définitions ne sont pas complètes à 100 %. Elles sont construites de manière à fournir une compréhension de haut niveau de la connexion et de la relation entre JavaScript et ECMAScript.

Sans plus tarder, commençons.

### Ecma International

**Une organisation qui crée des normes pour les technologies.**

![Image](https://cdn-media-1.freecodecamp.org/images/9hTL9XKeWeDKV7iP1ozAHfRAZ6sKpKOYFOIZ)

Pour illustrer un exemple de « norme » (bien que ce ne soit pas une norme créée par Ecma), pensez à tous les claviers que vous avez utilisés. La grande majorité avait-elle des lettres dans le même ordre, une barre d'espace, une touche Entrée, des touches fléchées, avec des nombres affichés en rangée en haut ? C'est parce que la plupart des fabricants de claviers basent la conception de leur clavier sur la norme de disposition [QWERTY](https://en.wikipedia.org/wiki/QWERTY).

### ECMA-262

**Il s'agit d'une norme publiée par Ecma International. Elle contient la spécification pour un langage de script à usage général.**

![Image](https://cdn-media-1.freecodecamp.org/images/1EV9EoLmaB-icJYqpu7rYSxeyJAvA-drQQl5)

ECMA-262 est une norme comme QWERTY, mais au lieu de représenter une spécification de disposition de clavier, elle représente une spécification de langage de script appelée ECMAScript.

Pensez à ECMA-262 comme au numéro de référence d'ECMAScript.

![Image](https://cdn-media-1.freecodecamp.org/images/BLfQVsprp9JKHuRPcS0kLp8LFWHTFUfTk9-f)
_ECMA-260, ECMA-261, ECMA-262. Il y a ECMAScript._

### Un langage de script

**Un langage de programmation conçu spécifiquement pour agir sur une entité ou un système existant**

Pour avoir une idée générale de ce qui fait qu'un langage de programmation est un langage de script, considérez les commandes « marcher », « courir » et « sauter ». Ces actions nécessitent quelque chose pour les exécuter, peut-être une personne, un chien ou un personnage de jeu vidéo. Sans un acteur pour effectuer ces commandes, « marcher », « courir » et « sauter » n'auraient pas de sens. Cet ensemble d'actions est analogue à un langage de script qui se concentre sur la manipulation d'une entité externe.

### ECMAScript

**La spécification définie dans ECMA-262 pour créer un langage de script à usage général.**  
**Synonyme :** Spécification ECMAScript

![Image](https://cdn-media-1.freecodecamp.org/images/p-RbJhYkrEKUnojlVs7RoXoVE7Qxz1QXozVQ)
_Photo credit: [code.tutsplus.com](https://code.tutsplus.com/tutorials/ecmascript-6-power-tutorial-class-and-inheritance--cms-24117" rel="noopener" target="_blank" title=")_

Alors qu'ECMA-262 est le nom de la norme, il représente la spécification du langage de script ECMAScript.

ECMAScript fournit les règles, les détails et les directives qu'un langage de script doit observer pour être considéré comme conforme à ECMAScript.

![Image](https://cdn-media-1.freecodecamp.org/images/6ZDYS8oka3qX9aep2SaxSaLfFXwIFG-8ljW5)
_Un extrait de la [Spécification du langage ECMAScript 2017](https://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf" rel="noopener" target="_blank" title="). Le document ne fait qu'environ 900 pages, si vous cherchez une lecture légère._

#### **JavaScript**

**Un langage de script à usage général qui se conforme à la spécification ECMAScript.**

![Image](https://cdn-media-1.freecodecamp.org/images/dbnmtPdU02XbZ41M74SLaIPbLUeG3zMJa5UV)
_Photo credit: [Udemy](https://www.udemy.com/javascript-from-basic-fundamentals-to-advanced/" rel="noopener" target="_blank" title=")_

JavaScript est le langage au goût de café avec lequel j'aime programmer. ECMAScript est la spécification sur laquelle il est basé. En lisant la [spécification ECMAScript](https://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf), vous apprenez comment **créer** un langage de script. En lisant la [documentation JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), vous apprenez comment **utiliser** un langage de script.

Lorsque les gens appellent JavaScript un « dialecte du langage ECMAScript », ils le veulent dans le même sens que lorsqu'ils parlent des dialectes anglais, français ou chinois. Un dialecte tire la plupart de son lexique et de sa syntaxe de son langage parent, mais s'en écarte suffisamment pour mériter une distinction.

JavaScript implémente principalement la spécification ECMAScript telle que décrite dans ECMA-262, mais quelques différences existent. Mozilla décrit les fonctionnalités de JavaScript qui ne font pas partie d'ECMAScript [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/New_in_JavaScript/ECMAScript_Next_support_in_Mozilla) :

![Image](https://cdn-media-1.freecodecamp.org/images/wZx36dAL-wYWFA8weITyQfErv8YzkjQDNuVl)
_Une capture d'écran du 3 septembre 2017. Il s'agit d'une liste des fonctionnalités expérimentales de JavaScript qui ne font pas partie d'ECMAScript (du moins pas encore)._

#### **Un moteur JavaScript**

**Un programme ou un interpréteur qui comprend et exécute le code JavaScript.**

**Synonymes** : Interpréteur JavaScript, Implémentation JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/suYku9Y4XZ-DMt1b9eGxv39vil2OA3wmAlHg)
_Photo credit: [translatemedia.com](https://www.translatemedia.com/translation-blog/exploring-the-source-of-language-comprehension/" rel="noopener" target="_blank" title=")_

Les moteurs JavaScript se trouvent couramment dans les navigateurs web, notamment V8 dans Chrome, SpiderMonkey dans Firefox et Chakra dans Edge. Chaque moteur est comme un module de langage pour son application, lui permettant de supporter un certain sous-ensemble du langage JavaScript.

Un moteur JavaScript pour un navigateur est comme la compréhension du langage pour une personne. Si nous revisitons notre exemple des actions « marcher », « courir », « sauter », un moteur JavaScript est la partie d'une « entité » qui comprend réellement ce que ces actions signifient.

Cette analogie aide à expliquer quelques choses sur les navigateurs :

![Image](https://cdn-media-1.freecodecamp.org/images/bOGBPwrH1u-nqxgkgh37q61h9rj8vduA0tUZ)
_Photo credit: [datavizcatalogue.com](https://datavizcatalogue.com/methods/line_graph.html" rel="noopener" target="_blank" title=")_

#### **Différences de performance des navigateurs**

Deux personnes peuvent reconnaître la commande « sauter », mais l'une peut réagir à la commande plus rapidement parce que la personne peut comprendre et traiter la commande plus rapidement que l'autre personne. De même, deux navigateurs peuvent comprendre le code JavaScript, mais l'un l'exécute plus rapidement parce que son moteur JavaScript est implémenté plus efficacement.

![Image](https://cdn-media-1.freecodecamp.org/images/a2oywyaVJoD4vLyas60zOd8CYnwKyqlnltqS)
_Photo credit: [vcsolutions.com](http://vcsolutions.com/battle-of-the-browsers-the-best-web-browser-is/" rel="noopener" target="_blank" title=")_

#### **Différences de support des navigateurs**

Considérez les différences qui existent entre les personnes qui parlent la même langue. Même si beaucoup de gens parlent anglais, certains peuvent connaître certains mots, expressions et règles de syntaxe que d'autres ne connaissent pas, et vice versa. Les navigateurs sont de la même manière. Même si les moteurs JavaScript des navigateurs comprennent tous JavaScript, certains navigateurs ont une meilleure compréhension du langage que d'autres. Il existe des différences dans la manière dont les navigateurs supportent le langage.

En ce qui concerne le support des navigateurs, les gens parlent généralement de « compatibilité ECMAScript » plutôt que de « compatibilité JavaScript », même si les moteurs JavaScript analysent et exécutent... eh bien, JavaScript. Cela peut être un peu confus, mais il y a une explication.

![Image](https://cdn-media-1.freecodecamp.org/images/YbOZFdJwH-qPCcnnDyKD6mzlQdEw0NcN8EsB)
_Ce tableau fait partie d'un tableau de support des navigateurs dans la page [ECMAScript Wikipedia](https://en.wikipedia.org/wiki/ECMAScript" rel="noopener" target="_blank" title="). Les versions de JavaScript ne sont pas mentionnées ici._

Si vous vous en souvenez, ECMAScript est une spécification de ce à quoi un langage de script **pourrait** ressembler. La publication d'une nouvelle édition d'ECMAScript ne signifie pas que tous les moteurs JavaScript existants ont soudainement ces nouvelles fonctionnalités. Il appartient aux groupes ou organisations responsables des moteurs JavaScript d'être à jour sur la dernière spécification ECMAScript et d'adopter ses changements.

Par conséquent, les développeurs ont tendance à poser des questions comme « Quelle version d'ECMAScript ce navigateur supporte-t-il ? » ou « Quelles fonctionnalités d'ECMAScript ce navigateur supporte-t-il ? ». Ils veulent savoir si Google, Mozilla et Microsoft ont mis à jour les moteurs JavaScript de leurs navigateurs — par exemple [V8](https://en.wikipedia.org/wiki/Chrome_V8), [SpiderMonkey](https://en.wikipedia.org/wiki/Spider_monkey) et [Chakra](https://en.wikipedia.org/wiki/Chakra_(JScript_engine)), respectivement — avec les fonctionnalités décrites dans la dernière spécification ECMAScript.

Le [tableau de compatibilité ECMAScript](http://kangax.github.io/compat-table/es6/) est une bonne ressource pour répondre à ces questions.

Si une nouvelle édition d'ECMAScript sort, les moteurs JavaScript n'intègrent pas toute la mise à jour en une seule fois. Ils incorporent les nouvelles fonctionnalités d'ECMAScript de manière incrémentielle, comme on peut le voir dans cet extrait du journal des modifications de JavaScript de Firefox :

![Image](https://cdn-media-1.freecodecamp.org/images/C9trDMdtG4QldUnxltoT9-whAG4gMXkhpkzq)
_Dans Firefox 50, des parties de ES2015 et ES2017 ont été implémentées dans le moteur JavaScript de Firefox, SpiderMonkey. D'autres parties de ES2015 et ES2017 ont été implémentées avant et continueront à être implémentées à l'avenir._

#### Un environnement d'exécution JavaScript

**L'environnement dans lequel le code JavaScript s'exécute et est interprété par un moteur JavaScript. L'environnement d'exécution fournit les objets hôtes que JavaScript peut manipuler et avec lesquels il peut travailler.**

**Synonymes** : Environnement hôte

![Image](https://cdn-media-1.freecodecamp.org/images/5l8SuhHU3K19bMXLUeDUliu8HKvEupgZtNOM)
_Photo credit: [Emuparadise](https://www.emuparadise.me/Nintendo_DS_ROMs/New_Super_Mario_Bros._(U)(Psyfer)/46505" rel="noopener" target="_blank" title=")_

L'environnement d'exécution JavaScript est « l'entité ou le système existant » mentionné dans la définition du langage de script. Le code passe par le moteur JavaScript, et une fois analysé et compris, une entité ou un système effectue les actions interprétées. Un chien marche, une personne court, un personnage de jeu vidéo saute (ou, dans le cas de l'image ci-dessus, se crashe).

Les applications se rendent disponibles pour le scripting JavaScript en fournissant des « objets hôtes » à l'exécution. Pour le côté client, l'environnement d'exécution JavaScript serait le navigateur web, où des objets hôtes comme les fenêtres et les documents HTML sont mis à disposition pour la manipulation.

Avez-vous déjà travaillé avec les objets hôtes window ou document ? Les objets window et document ne font pas réellement partie du langage JavaScript de base. Ce sont des API Web, des objets fournis par un navigateur agissant comme environnement hôte de JavaScript. Pour le côté serveur, l'environnement d'exécution JavaScript est Node.js. Des objets hôtes liés au serveur tels que le système de fichiers, les processus et les requêtes sont fournis dans Node.js.

Un point intéressant : différents environnements d'exécution JavaScript peuvent partager le même moteur JavaScript. V8, par exemple, est le moteur JavaScript utilisé à la fois dans Google Chrome et Node.js — deux environnements très différents.

#### ECMAScript 6

**Il s'agit de la sixième édition de la norme ECMA-262, et elle présente des changements et des améliorations majeurs de la spécification ECMAScript.**

**Synonymes** : ES6, ES2015 et ECMAScript 2015

![Image](https://cdn-media-1.freecodecamp.org/images/wtwD646nQf8w2gV0QDDxpf5zDHOL43j6xWT-)

Cette édition d'ECMAScript a changé son nom de ES6 à ES2015 parce qu'en 2015, Ecma International a décidé de passer à des publications annuelles d'ECMAScript. En conséquence, Ecma International a également commencé à nommer les nouvelles éditions de la spécification ECMAScript en fonction de l'année de leur publication. En bref, ES6 et ES2015 sont deux noms différents pour la même chose.

#### Babel

**Un transpileur qui peut convertir le code ES6 en code ES5.**

![Image](https://cdn-media-1.freecodecamp.org/images/fzmf2hHXlv5dgoQ178bSp-oGPkSISGwiAKLa)
_Photo credit: [HTML5Hive.org](https://html5hive.org/es6-and-babel-tutorial/" rel="noopener" target="_blank" title=")_

Les développeurs peuvent utiliser les [nouvelles fonctionnalités qui accompagnent ES6](http://es6-features.org/), mais peuvent être préoccupés par la compatibilité multi-navigateurs pour leurs applications web. Au moment de la rédaction de cet article, Edge et Internet Explorer ne supportent pas pleinement les fonctionnalités de la spécification ES6.

Les développeurs concernés peuvent utiliser Babel pour convertir leur code ES6 en une version fonctionnellement équivalente qui n'utilise que des fonctionnalités ES5. Tous les principaux navigateurs supportent pleinement ES5, donc ils peuvent exécuter le code sans aucun problème.

### Une dernière information intéressante

J'espère que vous avez trouvé ces informations sur JavaScript et ECMAScript utiles. Avant de conclure, je voudrais partager une dernière information qui doit être clarifiée pour les développeurs web débutants comme moi.

#### L'œuf ou la poule

Un détail historique confus est que JavaScript a été créé en 1996. Il a ensuite été soumis à Ecma International en 1997 pour standardisation, ce qui a abouti à ECMAScript. En même temps, parce que JavaScript se conformait à la spécification ECMAScript, JavaScript est un exemple d'implémentation d'ECMAScript.

Cela nous laisse avec ce fait amusant : ECMAScript est basé sur JavaScript, et JavaScript est basé sur ECMAScript.

Je sais.

Cela ressemble exactement au trope du voyage dans le temps où les personnes sont leurs propres parents — un peu bizarre, mais assez amusant à penser.

### Toutes les bonnes choses

Je sais que nous nous sommes tous amusés ici, mais c'était beaucoup d'informations à digérer. Je vais profiter de cette occasion pour dire au revoir.

N'hésitez pas à laisser des questions, commentaires, suggestions ou préoccupations ci-dessous.

Merci beaucoup d'avoir lu !