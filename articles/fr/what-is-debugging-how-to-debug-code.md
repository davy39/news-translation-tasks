---
title: Qu'est-ce que le débogage ? Comment déboguer votre code pour les débutants
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-03-16T21:31:29.000Z'
originalURL: https://freecodecamp.org/news/what-is-debugging-how-to-debug-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-mike-198101.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: clean code
  slug: clean-code
- name: debugging
  slug: debugging
seo_title: Qu'est-ce que le débogage ? Comment déboguer votre code pour les débutants
seo_desc: 'In this article we''ll talk about what debugging is, how to debug your
  code, and how you can get better at it.

  Table of contents


  How Debugging Started


  Why Should You Learn About Debugging?


  How to Debug Your Code


  How to Get in a Debugging Mindset


  ...'
---

Dans cet article, nous allons parler de ce qu'est le débogage, de la manière de déboguer votre code et de la façon dont vous pouvez vous améliorer.

## Table des matières

* [Comment le débogage a commencé](#heading-comment-le-debogage-a-commence)
    
* [Pourquoi devriez-vous apprendre le débogage ?](#heading-pourquoi-devriez-vous-apprendre-le-debogage)
    
* [Comment déboguer votre code](#heading-comment-deboguer-votre-code)
    
* [Comment adopter un état d'esprit de débogage](#heading-comment-adopter-un-etat-desprit-de-debogage)
    
    * [Prêtez attention aux messages d'erreur](#heading-pretez-attention-aux-messages-derreur)
        
    * [Recherchez sur Google](#heading-recherchez-sur-google)
        
    * [Expliquez votre logique à une autre personne ou à un canard](#heading-expliquez-votre-logique-a-une-autre-personne-ou-a-un-canard)
        
    * [Réduisez votre problème et comprenez où l'erreur est générée](#reduisezvotreproblemeetcomprenezoulerreurestgeneree)
        
    * [Faites une pause et pensez à autre chose](#heading-faites-une-pause-et-pensez-a-autre-chose)
        
    * [Cherchez de l'aide](#heading-cherchez-de-laide)
        
    * [Assurez-vous que le bug est mort](#heading-assurez-vous-que-le-bug-est-mort)
        
    * [Écrivez du code propre](#heading-ecrivez-du-code-propre)
        
        * [Écrivez du code DRY](#heading-ecrivez-du-code-dry)
            
        * [Écrivez du code simple quand c'est possible](#heading-ecrivez-du-code-simple-quand-cest-possible)
            
        * [Utilisez les principes SOLID](#heading-utilisez-les-principes-solid)
            
* [Outils techniques de débogage](#heading-outils-techniques-de-debogage)
    
    * [Comment TypeScript aide à écrire du code propre](#heading-comment-typescript-aide-a-ecrire-du-code-propre)
        
    * [Comment utiliser console.log pour déboguer du code](#heading-comment-utiliser-consolelog-pour-deboguer-du-code)
        
    * [Comment utiliser le débogueur de Visual Studio](#heading-comment-utiliser-le-debogueur-de-visual-studio)
        
    * [Débogueur Chrome](#heading-debogueur-chrome)
        
* [Conclusion](#heading-conclusion)
    

# Comment le débogage a commencé

Les mots "*bug*" et "*debugging*" (débogage) dans le logiciel sont populairement attribués à l'[Admiral Grace Hopper](https://es.wikipedia.org/wiki/Grace_Murray_Hopper). Véritable légende, elle a écrit le premier compilateur qui ait jamais existé.

Dans les années 1940, alors qu'elle travaillait sur un ordinateur développé pour la marine américaine à l'université de Harvard, ses associés ont découvert un papillon de nuit (un véritable insecte) coincé dans un relais qui a fait planter l'ordinateur.

En résolvant ce problème, elle a fait remarquer qu'ils étaient en train de "déboguer" (debugging) le système.

Si vous êtes fan d'étymologie cependant, vous pourriez être intéressé par le fait que le mot "debugging" semble avoir été utilisé comme terme en aéronautique avant d'entrer dans le monde de l'informatique.

Et apparemment, il existe une sorte de preuve que même Thomas Edison l'utilisait dans le sens d'"erreur technique" dès 1878.

Mais ce n'est pas le sujet de cet article. Le point important est que le débogage est une partie centrale du développement logiciel. Cela l'a toujours été et le sera probablement toujours.

Heureusement, cependant, les cas où nous devons retirer de véritables insectes des ordinateurs sont plutôt rares aujourd'hui.

# Pourquoi devriez-vous apprendre le débogage ?

Les bugs et les erreurs sont si susceptibles de se produire dans le développement de logiciels parce qu'il s'agit d'une activité très conceptuelle et abstraite.

En tant que développeurs, nous travaillons avec de l'information. Nous l'organisons, la déplaçons, la mettons à jour et l'éditons, l'envoyons à certains endroits puis la recevons à nouveau.

Nous travaillons tout le temps avec l'information, mais pas directement avec elle. L'information n'est pas "réellement" là à l'intérieur de l'ordinateur, du moins pas dans le format que les utilisateurs imaginent.

À l'intérieur de l'ordinateur, il n'y a que des impulsions électriques, qui sont ensuite abstraites en 1 et 0, puis à nouveau abstraites dans n'importe quelle information avec laquelle nous travaillons.

Pour interagir avec les ordinateurs et les utiliser, nous utilisons des langages de programmation. Ceux-ci fournissent des niveaux d'abstraction par rapport aux tâches réelles que l'ordinateur effectue, et des représentations de l'information que nous gérons.

La programmation peut être une activité très abstraite, et il est très facile de perdre rapidement de vue la tâche réelle que l'ordinateur effectue, ou l'information sur laquelle nous agissons dans une certaine ligne de code. Et à partir de là, il est facile de donner les mauvaises instructions à l'ordinateur et de manquer la cible que nous visons.

Une blague interne dans le monde du développement logiciel est que les développeurs passent normalement 5 minutes à écrire du code et 5 heures à essayer de comprendre pourquoi les choses ne fonctionnent pas comme elles le devraient.

En tant que développeurs, peu importe notre niveau, nous allons passer d'innombrables heures à déboguer notre code, nous devrions donc essayer de devenir meilleurs et plus rapides dans cet exercice.

# Comment déboguer votre code

Le débogage peut être défini comme le processus consistant à trouver la racine d'un problème dans une base de code et à le corriger.

Habituellement, nous commençons par réfléchir à toutes les causes possibles, puis nous testons chacune de ces hypothèses (en commençant par les plus probables), jusqu'à ce que la cause profonde ultime soit trouvée. Ensuite, nous la corrigeons et nous nous assurons qu'elle ne se reproduira plus.

Il n'y a pas de solution magique pour les bugs. En général, cela nécessite une combinaison de recherches sur Google, de journalisation (logging) de notre code et de vérification de notre logique par rapport à ce qui se passe réellement.

Bien qu'il existe de nombreux outils qui peuvent vous aider dans le débogage, l'utilisation de ces outils n'est pas nécessairement la partie la plus difficile. Ce qui est difficile, c'est de comprendre véritablement les erreurs que vous obtenez, et de comprendre réellement quelle est la meilleure solution pour les résoudre.

Commençons donc par parler d'abord de l'"état d'esprit de débogage", puis explorons quelques outils utiles que nous pouvons utiliser pour déboguer notre code.

# Comment adopter un état d'esprit de débogage

## Prêtez attention aux messages d'erreur

![G-Wn7Seyn](https://www.freecodecamp.org/news/content/images/2022/03/G-Wn7Seyn.gif align="left")

Dans presque tous les environnements de développement, si votre code échoue, un message d'erreur vous sera probablement affiché, expliquant (dans une certaine mesure) pourquoi votre code échoue.

Prenons ce code par exemple :

```js
mickTheBug('Je suis un bug effrayant !')

const mickTheBug = message => console.log(message)
```

Ce code génère l'erreur suivante :

```js
ReferenceError: Cannot access 'mickTheBug' before initialization
    at Object.<anonymous> (/home/German/Desktop/ger/code/projects/test.js:4:1)
```

Comme vous pouvez le voir, le message d'erreur pointe clairement vers le problème et déclare même à quelle ligne il se produit ( `test.js:4:1` ).

Cela peut sembler être un conseil idiot, mais vous seriez surpris de voir combien de programmeurs ne lisent pas attentivement les messages d'erreur et réagissent simplement au bug avec la première idée qui leur vient à l'esprit.

Les messages d'erreur sont là pour une raison, et c'est pour nous donner au moins une première idée de l'origine du problème.

## Recherchez sur Google

![ddqvW2927](https://www.freecodecamp.org/news/content/images/2022/03/ddqvW2927.png align="left")

Si le message d'erreur que vous obtenez n'est pas clair pour vous, ou si vous ne comprenez pas pourquoi vous l'obtenez, une bonne première étape serait de le rechercher sur Google.

L'une des nombreuses choses formidables à propos du code est que la communauté en ligne est immense. Il est presque certain que des tonnes de personnes ont déjà été confrontées au même bug que vous, et qu'elles l'ont résolu et expliqué afin que d'autres n'aient pas à lutter eux aussi.

Lors de vos recherches sur Google, une bonne idée est d'être aussi détaillé que possible dans la recherche. En suivant l'exemple précédent, j'utiliserais "*javascript ReferenceError: Cannot access before initialization*". J'ai remarqué que mentionner la technologie que vous utilisez dans la recherche donne des résultats plus précis.

J'ai également appris qu'il est important de supprimer les éléments qui ne sont propres qu'à mon code et non une erreur que tout le monde obtiendrait, comme le nom de ma fonction (*'mickTheBug'*).

Une autre bonne idée est d'essayer d'**utiliser des sources fiables et récentes**. Fiable signifie soit la documentation officielle, soit des solutions qui ont été validées par d'autres. Récente signifie des solutions qui ont été implémentées le plus récemment possible, car quelque chose qui fonctionnait il y a cinq ans n'est peut-être pas la meilleure façon de résoudre le problème aujourd'hui.

La documentation officielle devrait toujours être la première chose à vérifier, que vous appreniez quelque chose de nouveau ou que vous traitiez une erreur.

Les docs officielles sont généralement la source d'information la plus complète et la plus à jour pour n'importe quel outil. Il peut parfois sembler fastidieux ou accablant de parcourir autant d'informations techniques, mais à long terme, je pense que cela fait gagner du temps.

Le problème avec les docs officielles est qu'elles contiennent parfois tellement d'informations et sont expliquées à un niveau de détail tel que c'est plus déroutant qu'explicatif.

Pour cette raison, je pense que c'est une bonne idée de toujours utiliser plus d'une source pour un sujet particulier, et d'"entendre différentes voix" expliquer la même chose. Généralement, ce n'est qu'après avoir lu la doc, quelques articles et regardé quelques vidéos YouTube que j'ai l'impression de bien comprendre l'outil avec lequel je travaille.

## Expliquez votre logique à une autre personne ou à un canard

![lwjv2jUhM](https://www.freecodecamp.org/news/content/images/2022/03/lwjv2jUhM.png align="left")

J'ai mentionné plus tôt à quel point la programmation peut être une activité abstraite, ce qui facilite la perte de vue des choses, les fausses suppositions et la mauvaise interprétation de l'information avec laquelle nous travaillons.

Une bonne solution à cela est de parcourir votre code ligne par ligne, en le lisant et en l'expliquant à haute voix au fur et à mesure. La [technique du canard en plastique](https://en.wikipedia.org/wiki/Rubber_duck_debugging) est une façon populaire de le faire, mais vous pouvez choisir votre animal de compagnie préféré ou un ami imaginaire. =P

L'idée est de vous forcer à lire réellement votre code au lieu de simplement supposer que vous savez ce qu'il fait. De cette façon, vous pouvez vérifier la logique dans votre esprit par rapport à ce qui se passe réellement dans votre code.

Le fait que nous ayons tendance à supposer des choses et à ne pas prêter une attention détaillée à chaque ligne de code est simplement la nature humaine. C'est un mécanisme qui nous aide à économiser de l'énergie et à faire les choses plus rapidement.

Mais lors du débogage, nous devons forcer notre cerveau à travailler avec nous et à être aussi présent que possible sur chaque ligne de code.

## Réduisez votre problème et comprenez où l'erreur est générée

![aEKNV-Iju](https://www.freecodecamp.org/news/content/images/2022/03/aEKNV-Iju.gif align="left")

À mesure que votre base de code s'agrandit, il sera difficile d'analyser chaque ligne de code à la recherche de votre bug. C'est donc une bonne idée de diviser pour régner, en commençant votre recherche dans les endroits les plus susceptibles de générer le problème.

Voyons cet exemple. J'ai une fonction qui prend un nombre et le renvoie multiplié par deux, et une autre qui affiche un firstName, un lastName et le résultat de la fonction de multiplication.

```js
const multiply = num => num*2

const mickTheBug = async (firstName, lastName, age) => {
  console.log(`Mon nom est ${firstName} ${lastName} et le double de mon âge est ${multiply(age)}`)
}

mickTheBug('Mick', 10)
```

Le code semble logique et s'exécute sans générer d'erreur, mais le résultat que j'obtiens est `Mon nom est Mick 10 et le double de mon âge est NaN`, ce qui n'est pas ce que je veux.

Ici, je peux voir que `10` s'affiche là où `lastName` devrait être. Et comme les paramètres sont définis dans la ligne où la fonction est appelée.

C'est probablement une bonne idée de commencer par vérifier si les paramètres ont été passés de la bonne manière. Et en effet, nous pouvons voir que lorsque j'ai appelé la fonction, je lui ai passé deux paramètres, `Mick` et `10`, alors que la fonction attend trois paramètres `firstName, lastName, age`.

> TypeScript nous aurait facilement empêchés de commettre cette erreur. Plus d'informations à ce sujet plus tard. ;)

Encore une fois, c'est un exemple simple, mais il illustre comment nous pouvons déduire d'où vient un problème, même si nous n'avons pas de message d'erreur pour nous aider.

Dans ces moments-là, essayez de vous poser les questions suivantes :

* Comment savoir que je vois une erreur ?
    
* Quelle entrée (input) est-ce que je fournis ? D'où vient-elle ? Cette entrée est-elle la même que celle attendue par la fonction ?
    
* Quelle sortie (output) est-ce que je reçois ? Comment l'entrée a-t-elle changé ?
    
* Y a-t-il d'autres entités qui interagissent avec ce morceau de code ?
    
* Ai-je changé quelque chose récemment qui aurait pu casser le code ?
    

## Faites une pause et pensez à autre chose

![Ly_kXFJop](https://www.freecodecamp.org/news/content/images/2022/03/Ly_kXFJop.gif align="left")

Les bugs comme les exemples que nous avons vus jusqu'à présent sont un jeu d'enfant à résoudre. Mais beaucoup d'autres ne le sont pas, et à de nombreuses occasions, vous devrez lutter contre des bugs pendant plusieurs heures (ou jours) jusqu'à ce que vous arriviez à une solution.

Dans ces occasions, je trouve qu'il est vraiment important de prêter attention à votre état d'esprit. La programmation est une activité très mentale. Ainsi, la façon dont votre cerveau travaille à un certain moment ou la façon dont vous vous sentez affectera directement l'apparence de votre code et votre capacité à résoudre les problèmes de manière efficace.

Si vous passez des heures à lire, à répéter à haute voix les mêmes lignes de code, à chercher sur Google, à parcourir les questions de Stack Overflow, et que votre code échoue toujours, tôt ou tard vous serez frustré et commencerez à vous mettre la pression.

Au fur et à mesure que vous essayez différentes solutions et que vous échouez encore et encore, votre attention aux détails va probablement se diluer et vous commencerez à sauter sur différentes idées et à essayer plusieurs choses à la fois.

Une fois arrivé à ce point, la chose sage à faire est d'aller se promener ou de simplement laisser tomber jusqu'au lendemain.

Si vous continuez alors que vous êtes dans cet état mental stressé et fatigué, vous n'allez probablement pas trouver de solution. Et qui plus est, vous pourriez même aggraver le bug en touchant à des choses qui ne lui sont pas vraiment liées.

En laissant les choses de côté pendant un moment et en pensant à autre chose, notre cerveau continuera à travailler sur le problème en arrière-plan et à connecter les idées de manière "subconsciente" et créative.

À de nombreuses reprises, il m'est arrivé qu'une solution toute fraîche me vienne à l'esprit quand je suis sous la douche ou dès que je revois le problème le lendemain matin. C'est l'un de ces moments "*Eurêka !*". Elle était probablement juste là, sous vos yeux, mais parce que vous étiez fatigué et stressé, vous n'étiez pas capable de la voir.

Être concentré, bien reposé et détendu est essentiel pour écrire du code de qualité et corriger les bugs de manière efficace. La frontière entre travailler dur et épuiser son esprit est mince, mais il est important d'y prêter attention et de s'accorder du repos dès que nous en avons besoin.

Habituellement, je trouve qu'un bon moment pour faire une pause est quand je suis à court d'idées, ou quand je commence à perdre ma concentration et à essayer différentes approches de manière impulsive et non systématique.

Gardez également à l'esprit que les bugs font partie intégrante du développement logiciel. Cela ne signifie pas que vous êtes un mauvais développeur. Tout le monde a des bugs, même les meilleurs programmeurs. Alors détendez-vous et profitez de la situation pour apprendre quelque chose de nouveau.

## Cherchez de l'aide

J'ai mentionné précédemment l'importance des communautés en ligne et à quel point il est génial de pouvoir trouver facilement de l'aide pour presque n'importe quel sujet en quelques secondes.

Avoir accès aux bonnes communautés, où vous pouvez poser des questions et parler à des personnes expérimentées dans les outils que vous utilisez, est vraiment, vraiment, vraiment utile.

Cela variera selon le domaine dans lequel vous travaillez et les outils que vous utilisez, mais pour moi, des sites comme [freecodecamp](https://www.freecodecamp.org/), [stackoverflow](https://stackoverflow.com/), et des communautés Slack ou Discord comme [meetupjs](https://meetupjs.com.ar/) ont fait une énorme différence.

Lorsque vous posez des questions au sein de ces communautés, je trouve qu'il est important de garder à l'esprit les points suivants :

* Essayez d'être aussi **détaillé que possible**. Il n'est pas toujours facile de comprendre le code de quelqu'un d'autre en le lisant simplement, alors essayez d'expliquer sur quoi vous travaillez, ce que vous essayez d'accomplir et quel est le problème auquel vous êtes confronté.
    
* Montrez l'**erreur exacte** que vous obtenez.
    
* Montrez le **code associé** que vous pensez être à l'origine de l'erreur.
    
* Mentionnez **quelles solutions vous avez essayées** jusqu'à présent et pourquoi elles n'ont pas fonctionné.
    
* Enquêtez et montrez que vous avez fait des **recherches** sur le problème. Même s'il est tout à fait acceptable de demander de l'aide, je pense que vous devez d'abord épuiser les pistes les plus évidentes et les plus faciles avant de demander à quelqu'un d'autre de réfléchir à votre place. Cela signifie que vous avez analysé votre code, cherché le problème sur Google, lu d'autres solutions et la documentation officielle, essayé plusieurs approches et qu'aucune n'a fonctionné. Ce n'est qu'alors qu'il est acceptable de demander de l'aide à quelqu'un d'autre. Je pense que c'est une question de capacité à apprendre et à résoudre des problèmes de manière indépendante, mais aussi de respect du temps des autres.
    
* Mentionnez la **documentation** que vous avez consultée sur ce sujet et ce que cette documentation en dit.
    
* Donnez accès à votre **base de code complète** dans un dépôt en ligne.
    

Cela facilitera la compréhension de votre problème par une autre personne et, espérons-le, lui permettra de vous proposer des idées de solutions.

Si vous obtenez des réponses, il est important d'y **répondre**, soit en confirmant que la solution a fonctionné, soit en expliquant pourquoi elle n'a pas fonctionné.

N'oubliez pas que la question que vous avez posée sera probablement stockée et disponible la prochaine fois que quelqu'un cherchera le même bug. L'idée ici est de **construire la connaissance** et de la rendre **accessible à tous**, pas seulement de résoudre ce bug particulier.

De plus, si vous finissez par trouver la solution vous-même, c'est une excellente idée de **répondre à votre propre question** et de partager la solution avec tout le monde.

Dans le même ordre d'idées, si vous participez à ces communautés en posant des questions, il serait agréable que vous participiez également en répondant à des questions. Chaque fois que vous le pouvez et que vous constatez que vous avez les connaissances nécessaires, il est bon de donner en retour. ;)

Ma dernière réflexion à ce sujet est que la plupart des gens dans ce genre de communautés sont gentils, ouverts et très disposés à aider et à partager leurs connaissances. Mais comme dans tout autre domaine de la vie, vous rencontrez de temps en temps des gens impolis, arrogants ou même agressifs.

Mon conseil ici est de ne pas laisser les autres vous intimider, même s'ils semblent avoir plus de connaissances que vous.

Personne n'est né en sachant tout, et si vous avez fait vos recherches et travaillé sur le problème, vous avez tout à fait le droit de demander ce que vous voulez. Si d'autres personnes sont arrogantes ou impolies, cela parle mal d'elles, pas de vous.

## Assurez-vous que le bug est mort

![xOmnh7_G7](https://www.freecodecamp.org/news/content/images/2022/03/xOmnh7_G7.gif align="left")

La seule chose plus frustrante que de lutter contre un bug difficile est de le corriger pour découvrir plus tard qu'il est toujours là. Ou pire encore, que d'autres bugs ont été introduits dans votre code à cause de la "solution".

Pour éviter ce genre de situation, il est essentiel de tester votre code. Et si vous pouvez le faire avec des tests unitaires automatisés, c'est encore mieux.

Idéalement, chaque section ou composant de votre base de code devrait avoir ses propres tests. Et ces tests devraient être exécutés chaque fois qu'une modification est apportée à la base de code. De cette façon, et si les tests sont correctement écrits, nous pouvons remarquer un nouveau bug dès qu'il est introduit. Ce qui, bien sûr, facilite la recherche de sa cause et sa résolution.

Si vous n'avez pas de tests automatisés (vous devriez vraiment en avoir si vous voulez créer des logiciels de qualité), testez au moins votre code manuellement, en reproduisant toutes les interactions possibles que l'utilisateur pourrait avoir avec lui, et assurez-vous que le bug a été effectivement éliminé.

## Écrivez du code propre

![Y4PKO37NS](https://www.freecodecamp.org/news/content/images/2022/03/Y4PKO37NS.png align="left")

La meilleure façon de combattre les bugs est d'éviter de les insérer en premier lieu. Écrire du code garanti sans bug est impossible pour n'importe quel programmeur, mais il y a quelques choses que vous pouvez faire pour réduire les chances d'insertion de bugs.

Un bon point de départ sont les principes classiques DRY, KISS et SOLID.

Des livres entiers ont été écrits sur ces sujets, mais pour faire court, ce sont des principes qui visent à rendre le logiciel facile à développer, facile à comprendre et à maintenir, et aussi proche que possible de l'absence de bug.

### Écrivez du code DRY

Le principe **DRY** signifie **"Don't repeat yourself"** (Ne vous répétez pas). Cela signifie essentiellement que nous devrions éviter la répétition du même code chaque fois que possible.

Par exemple, si vous voyez que vous effectuez la même opération encore et encore dans différentes parties de votre code, une bien meilleure approche serait d'abstraire cette logique dans une fonction et d'appeler la fonction au lieu d'effectuer directement les opérations dans différentes parties de votre code.

De cette façon, si un bug ou un comportement inattendu se produit dans cette opération, nous savons qu'il n'y a qu'un seul morceau de code responsable, et non plusieurs dispersés dans la base de code.

### Écrivez du code simple quand c'est possible

Le principe **KISS** signifie **"Keep it simple stupid"** (Garde ça simple, idiot). À mesure qu'un projet logiciel se développe, il commence inévitablement à devenir de plus et plus complexe. Au fur et à mesure que de nouvelles fonctionnalités non planifiées sont ajoutées et que différents développeurs commencent à y travailler, différentes logiques et manières d'exécuter des tâches peuvent être implémentées au sein du même projet.

Cela rend le code plus difficile à comprendre, à maintenir et à manipuler. Et quand le code est difficile à comprendre, il devient très facile de faire de fausses suppositions et d'insérer des bugs.

Nous devrions toujours viser un logiciel facile à lire et à comprendre, avec une logique limpide qui est explicite pour tout le monde et pas seulement pour nous.

Gardez à l'esprit que quelqu'un d'autre à l'avenir devra peut-être travailler avec le code que vous avez écrit, alors facilitez la compréhension de ce que vous faites pour cette personne. Même vous, après quelques mois, pourriez ne plus vous souvenir de ce que vous avez essayé de faire avec cette fonction.

Gardez également à l'esprit qu'aucun logiciel ne reste identique éternellement. La nature du logiciel est de changer et d'être amélioré par de nouvelles fonctionnalités, votre code doit donc être facile à modifier si nécessaire.

Et pour aller plus loin, vous **devriez** modifier votre code chaque fois que vous trouvez un moyen plus simple d'exécuter les mêmes tâches.

Peut-être qu'après avoir inclus quelques nouvelles fonctionnalités, la conception que vous aviez en tête au début n'est plus la meilleure option. Une autre chose cool à propos du code est que rien n'est gravé dans le marbre, et les choses peuvent être facilement inversées en cas de besoin. Profitez-en et prenez l'habitude de refactoriser constamment votre code à la recherche de l'approche la plus simple.

Certains concepts pratiques qui aident à cela consistent à utiliser des noms de fonctions et de variables explicites, à séparer les préoccupations dans différentes fonctions et modules de code, et à écrire de courts commentaires pour expliquer votre code lorsque votre tâche est inévitablement complexe.

### Utilisez les principes SOLID

**SOLID** est un ensemble de principes qui s'appliquent principalement à la [POO](https://en.wikipedia.org/wiki/Object-oriented_programming) (Programmation Orientée Objet). Ils ont été établis par [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin) (qui se trouve également être l'auteur du [manifeste agile](https://en.wikipedia.org/wiki/Agile_software_development#The_Agile_Manifesto)) dans [ce livre](https://www.amazon.com/-/es/Robert-Martin/dp/0135974445) sur la conception orientée objet.

* **S** signifie "Single Responsibility" (Responsabilité Unique), ce qui signifie qu'une classe doit avoir un, et un seul travail.
    
* **O** signifie "Open Closed Principle" (Principe Ouvert/Fermé), ce qui signifie que vous devriez pouvoir étendre le comportement d'une classe sans la modifier.
    
* **L** signifie "Liskov Substitution Principle" (Principe de Substitution de Liskov), ce qui signifie que les classes dérivées doivent pouvoir être substituées à leurs classes de base.
    
* **I** signifie "Interface Segregation" (Ségrégation des Interfaces), ce qui signifie qu'un client ne devrait jamais être forcé d'implémenter une interface qu'il n'utilise pas, ou que les clients ne devraient pas être forcés de dépendre de méthodes qu'ils n'utilisent pas.
    
* **D** signifie "Dependency Inversion Principle" (Principe d'Inversion de Dépendance), ce qui signifie que les entités doivent dépendre d'abstractions, pas de concrétions. Il stipule que le module de haut niveau ne doit pas dépendre du module de bas niveau, mais qu'ils doivent tous deux dépendre d'abstractions.
    

Comme mentionné, SOLID est plus applicable à la POO qu'à la programmation générale. Nous n'allons pas approfondir la POO dans cet article, mais il est tout de même bon de connaître ces principes et de les garder à l'esprit.

Apprenons maintenant quelques outils que vous pouvez utiliser pour vous aider à déboguer votre code.

# Outils techniques de débogage

Il existe de nombreux outils que nous pouvons utiliser soit pour réduire les chances d'insérer des bugs dans notre code, soit pour combattre plus efficacement les bugs existants.

À cet égard, nous allons jeter un coup d'œil à **TypeScript**, au populaire (et très utile) **console.log**, et aux **débogueurs** intégrés à **VS Code** et **Chrome**.

Ces outils et exemples seront centrés sur JavaScript, mais les principes s'appliquent à n'importe quel langage de programmation.

Vous devez également savoir que la plupart des éditeurs de code et des navigateurs Web disposent aujourd'hui de débogueurs intégrés, mais nous allons passer en revue VS Code et Chrome car ce sont les plus populaires.

Enfin, vous devez également savoir qu'il existe des outils de débogage spécifiques que vous pouvez utiliser pour déboguer des types d'applications spécifiques, comme les outils de développement [React](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=es) et [Redux](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?hl=es), qui sont des extensions de navigateur que vous pouvez installer pour vous aider à déboguer votre code plus efficacement.

Mais nous les passerons en revue à l'avenir dans un article séparé sur la façon de déboguer une application React. ;)

## Comment TypeScript aide à écrire du code propre

Je mentionne TypeScript comme premier outil car il est étroitement lié à la section précédente sur l'écriture de code propre.

TypeScript ne vous fournit pas seulement un système de typage robuste pour JavaScript. Il ajoute également un compilateur qui vous aide à identifier les bugs et les erreurs de conception dans votre code avant même de l'exécuter. Il fournit une autocomplétion incroyable et peut être considéré comme un outil de documentation automatique.

Pour voir juste un aperçu de ses avantages, revisitons l'exemple précédent dans lequel nous n'avions pas fourni les bons arguments à notre appel de fonction.

![TYPESCRIPT1](https://www.freecodecamp.org/news/content/images/2022/03/TYPESCRIPT1.png align="left")

Comme vous pouvez le voir ici, avant même d'exécuter le programme, TypeScript détecte immédiatement qu'il nous manque un argument et nous donne l'erreur suivante :

```js
Expected 3 arguments, but got 2.ts(2554)
index.ts(6, 64): An argument for 'age' was not provided.
```

Ce genre de notifications est extrêmement utile, surtout lorsqu'on travaille sur de gros projets dans lesquels on doit interagir avec de nombreuses API ou différentes sections de code.

Ainsi, si vous êtes habitué au JavaScript pur, TypeScript peut sembler être du code superflu (boilerplate) au début. Mais à long terme, il vous fera sûrement gagner du temps et vous empêchera d'insérer des bugs idiots dans votre code.

## Comment utiliser console.log pour déboguer du code

Journaliser votre code dans la console est la manière la plus basique de déboguer et la première que nous apprenons à utiliser en tant que développeurs.

L'idée est d'afficher la valeur des variables, des fonctions, des entrées et des sorties pour vérifier la logique que nous avons en tête par rapport à ce qui se passe réellement dans notre code. Cela nous aide également à voir quelles fausses suppositions nous faisons.

Bien que ce soit un outil basique, nous pouvons faire des choses sympas avec. Laissez-moi vous montrer.

Si nous appelons `console.log`, nous obtiendrons n'importe quel objet que nous passons en paramètre affiché dans notre console.

```js
const arr = []
console.log(arr) // []

const populateArr = (elem1, elem2, elem3) => arr.push(elem1, elem2, elem3)
console.log(populateArr) // [Fonction : populateArr]

populateArr('John', 'Jake', 'Jill')
console.log(arr) // [ 'John', 'Jake', 'Jill' ]
```

`console.table` est idéal pour travailler avec des tableaux ou des objets, car il place les informations dans un tableau où vous pouvez facilement voir les clés/index et les propriétés/valeurs.

```js
const arr = ['John', 'Jake', 'Jill']
console.table(arr)

//┌─────────┬────────┐
//│ (index) │ Valeurs│
//├─────────┼────────┤
//│    0    │ 'John' │
//│    1    │ 'Jake' │
//│    2    │ 'Jill' │
//└─────────┴────────┘

const obj1 = {
  name: 'John',
  age: 30,
  job: 'Programmer'
}

const obj2 = {
  name: 'Jason',
  age: 32,
  job: 'Designer',
  faveColor: 'Blue'
}

const arr2 = [obj1, obj2]

console.table( arr2 )
// ┌─────────┬─────────┬─────┬──────────────┬─────────────┐
// │ (index) │  nom    │ age │     métier   │couleurPreferee│
// ├─────────┼─────────┼─────┼──────────────┼─────────────┤
// │    0    │ 'John'  │ 30  │ 'Programmer' │             │
// │    1    │ 'Jason' │ 32  │  'Designer'  │  'Blue'     │
// └─────────┴─────────┴─────┴──────────────┴─────────────┘
```

Lorsque vous journalisez plusieurs choses en même temps, `console.group` nous donne une manière organisée de voir les choses.

```js
const arr1 = [22, 23, 24]
const arr2 = [25, 26, 27]

console.group('mesTableaux')
console.log(arr1)
console.log(arr2)
console.groupEnd()


const obj1 = {
  name: 'John',
  age: 30,
  job: 'Programmer'
}

const obj2 = {
  name: 'Jason',
  age: 32,
  job: 'Designer',
  faveColor: 'Blue'
}

console.group('mesObjets')
console.log(obj1)
console.log(obj2)
console.groupEnd()

// mesTableaux
//   [ 22, 23, 24 ]
//   [ 25, 26, 27 ]
// mesObjets
//  { name: 'John', age: 30, job: 'Programmer' }
//  { name: 'Jason', age: 32, job: 'Designer', faveColor: 'Blue' }
```

`console.assert` est utile pour tester des conditions dans notre code. Il prend deux arguments : le premier est une condition et le second est le message qui s'affiche si la condition est fausse.

```js
const arr1 = [22, 23, 24]

console.assert(arr1.indexOf(20) !== -1, '20 n\'est pas dans mon tableau')
// L'assertion a échoué : 20 n'est pas dans mon tableau
```

`console.warn` et `console.error` sont utiles lors du débogage d'erreurs dans notre code. Le premier affichera l'erreur avec un fond jaune et le second avec un fond rouge.

```js
console.warn('Pas de problème') // Pas de problème
console.error(new Error('Erreur détectée'))

// Error: Erreur détectée
//     at Object.<anonymous> (/home/German/Desktop/ger/code/projects/test.js:6:15)
//     at Module._compile (node:internal/modules/cjs/loader:1101:14)
//     at Object.Module._extensions..js (node:internal/modules/cjs/loader:1153:10)
//     at Module.load (node:internal/modules/cjs/loader:981:32)
//     at Function.Module._load (node:internal/modules/cjs/loader:822:12)
//     at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:79:12)
//     at node:internal/main/run_main_module:17:47
```

## Comment utiliser le débogueur de Visual Studio

À mesure que nos applications se développent et commencent à devenir plus complexes, utiliser `console.log` partout devient une pratique peu efficace.

Pour nous aider dans notre lutte contre les bugs, des débogueurs ont été développés. Ce ne sont rien d'autre que des programmes capables de lire d'autres programmes et de les parcourir ligne par ligne, en vérifiant toutes les informations que nous voulons en cours de route (telles que la valeur des variables, par exemple).

Le premier exemple que nous allons voir est le **débogueur de Visual Studio**.

Pour déboguer une application Node.js, nous n'avons pas besoin d'installer quoi que ce soit de supplémentaire (en supposant que VS Code et Node soient installés sur notre ordinateur), car le débogueur Node est intégré à VS Code.

Si vous déboguez dans un autre langage comme Python ou Java, vous devrez peut-être installer une extension VS spécifique avant de lancer le débogueur.

Pour commencer, nous sélectionnons simplement le fichier que nous voulons déboguer et appuyons sur l'icône du bug.

![vsc1](https://www.freecodecamp.org/news/content/images/2022/03/vsc1.png align="left")

Après cela, l'écran suivant nous sera présenté :

![vsc2](https://www.freecodecamp.org/news/content/images/2022/03/vsc2.png align="left")

Nous sélectionnerons "Run and debug", ce qui lancera simplement le programme dans l'éditeur pour nous.

Tenez compte du fait que vous pourriez également créer un fichier `launch.json`, qui est un fichier que VS Code utilise pour "savoir" comment lancer votre programme. Pour cet exemple simple, ce ne sera pas nécessaire, mais sachez que cette possibilité existe.

Après avoir cliqué sur le bouton "Run and debug", notre programme s'exécutera et nous arriverons à l'écran suivant :

![vsc3](https://www.freecodecamp.org/news/content/images/2022/03/vsc3.png align="left")

En haut à gauche, nous avons toutes les variables disponibles dans le programme, tant au niveau local que global.

![vsc4](https://www.freecodecamp.org/news/content/images/2022/03/vsc4.png align="left")

En dessous, nous aurons un espace où nous pouvons déclarer des expressions particulières que nous aimerions surveiller. Les expressions peuvent être n'importe quoi, comme des variables ou des fonctions particulières que vous aimeriez garder à l'œil pour évaluer comment elles changent au fil de votre programme.

Par exemple, j'ai ajouté ma variable `arr` et VS Code me montre la valeur de cette variable :

![vsc5](https://www.freecodecamp.org/news/content/images/2022/03/vsc5.png align="left")

Et en dessous de cela, nous pouvons voir la pile d'appels (call stack) (si vous ne savez pas ce que c'est, [voici](https://www.youtube.com/watch?v=8aGhZQkoFbQ) une excellente vidéo qui l'explique), les scripts qui sont chargés et les points d'arrêt (breakpoints) que nous avons définis dans notre code (nous verrons ce que c'est dans un instant).

![vsc6](https://www.freecodecamp.org/news/content/images/2022/03/vsc6.png align="left")

Les **points d'arrêt** (breakpoints) constituent une grande partie de ce qui rend les débogueurs utiles. Comme leur nom l'indique, ce sont des points que vous pouvez déclarer dans votre code où le débogueur arrêtera l'exécution du programme. Lorsque le programme s'arrête, vous pourrez vérifier toutes les informations que nous avons mentionnées précédemment telles qu'elles sont à ce moment précis.

Ainsi, les points d'arrêt nous permettent de voir les informations réelles avec lesquelles le programme travaille, sans avoir besoin de rien journaliser dans la console. Plutôt cool !

Vous pouvez identifier un point d'arrêt par les petits points rouges qui apparaissent à gauche des numéros de ligne dans votre code (ou en regardant dans la section mentionnée ci-dessus).

Par défaut, lorsque vous lancez le débogueur, un point d'arrêt sera inséré à la dernière ligne de votre code. Pour insérer de nouveaux points d'arrêt, cliquez simplement à gauche du numéro de ligne où vous aimeriez que le débogueur s'arrête.

![vsc7](https://www.freecodecamp.org/news/content/images/2022/03/vsc7.png align="left")

Maintenant, lorsque vous lancez le débogueur, vous verrez qu'il y a une petite flèche à gauche sur le premier point d'arrêt, indiquant que c'est là que l'exécution du programme s'est arrêtée.

![vsc8](https://www.freecodecamp.org/news/content/images/2022/03/vsc8.png align="left")

En haut de l'écran, nous avons les **contrôles**, qui nous permettront de parcourir le programme en passant de point d'arrêt en point d'arrêt.

![vsc9](https://www.freecodecamp.org/news/content/images/2022/03/vsc9.jpg align="left")

* Le bouton **Continue** lance le programme et ne s'arrête que sur les points d'arrêt définis par l'utilisateur.
    
* Avec **Step Over**, s'il y a un appel de fonction, il l'exécute et renvoie le résultat. Vous ne rentrez pas dans les lignes qui sont à l'intérieur de la fonction. Vous allez directement à la valeur de retour de la fonction.
    
* **Step Into** entre dans la fonction ligne par ligne jusqu'à ce qu'elle se termine, puis vous revenez à la ligne suivante juste après l'appel de la fonction.
    
* Avec le bouton **Step Out**, si vous êtes entré dans une fonction, vous pouvez ignorer le reste de l'exécution de la fonction et aller directement à la valeur de retour.
    
* **Restart** relance le débogueur depuis le début et **Stop** quitte le débogueur.
    

Et voilà, c'est un débogueur très puissant intégré à votre éditeur de code. Comme vous pouvez le voir, avec cet outil, nous pouvons vérifier beaucoup d'informations en même temps, simplement en définissant des points d'arrêt où nous voulons et sans avoir besoin de `console.log`.

## Débogueur Chrome

Pour déboguer dans Chrome, nous commençons par ouvrir notre application dans le navigateur. Dans mon cas, j'ai créé un fichier HTML simple où mon fichier JS est lié (le même fichier que l'exemple précédent).

Ensuite, nous ouvrons les **outils de développement** (ctrl+maj+i ou clic droit -&gt; inspecter) et allons dans l'onglet "**Sources**".

Nous devrions voir quelque chose comme ceci :

![chrome1](https://www.freecodecamp.org/news/content/images/2022/03/chrome1.png align="left")

Sur le côté gauche, nous pouvons voir les fichiers disponibles dans notre application (dans mon cas, il n'y a qu'un fichier HTML et le fichier JS). Au milieu, nous pouvons voir le code de notre fichier sélectionné, et sur le côté droit, nous avons un ensemble d'informations très similaires à ce que nous avions dans VS Code.

Pour définir un point d'arrêt, nous devons cliquer sur le numéro de la ligne où nous voulons nous arrêter. Dans Chrome, les points d'arrêt sont identifiés par des flèches bleues sur le numéro de ligne.

![chrome2](https://www.freecodecamp.org/news/content/images/2022/03/chrome2.png align="left")

Ensuite, si nous rafraîchissons notre page, le script s'arrêtera au premier point d'arrêt et nous serons autorisés à naviguer à travers lui en utilisant les contrôles, qui fonctionnent exactement de la même manière que dans VS Code.

![chrome3](https://www.freecodecamp.org/news/content/images/2022/03/chrome3.png align="left")

Comme nous l'avons vu, les débogueurs de Chrome et de VS Code fonctionnent de manière très similaire, et celui que vous décidez d'utiliser n'est qu'une question de préférence.

# Conclusion

Le débogage est une partie centrale de ce que nous faisons en tant que développeurs. Pour cette raison, je pense que c'est une bonne idée d'y réfléchir et de le faire de manière efficace, au lieu de simplement réagir aux bugs au fur et à mesure qu'ils surviennent.

Comme nous l'avons vu, il y a énormément de choses que nous pouvons faire, tant d'un point de vue mental que technique, pour devenir de meilleurs débogueurs.

J'espère que cela vous a aidé et à la prochaine !

Vous pouvez également me suivre sur [Twitter](https://twitter.com/CoccaGerman) et [LinkedIn](https://www.linkedin.com/in/germancocca/).