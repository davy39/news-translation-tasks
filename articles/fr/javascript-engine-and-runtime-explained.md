---
title: Moteur JavaScript et Runtime expliqués
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-01-16T19:03:02.000Z'
originalURL: https://freecodecamp.org/news/javascript-engine-and-runtime-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-2--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Moteur JavaScript et Runtime expliqués
seo_desc: 'A JavaScript engine is simply a computer program that executes JavaScript
  code. It''s responsible for translating human-readable JavaScript code into machine-readable
  instructions that the computer''s hardware can execute.

  When you write JavaScript cod...'
---

Un moteur JavaScript est simplement un programme informatique qui exécute du code JavaScript. Il est responsable de la traduction du code JavaScript lisible par l'homme en instructions lisibles par la machine que le matériel de l'ordinateur peut exécuter.

Lorsque vous écrivez du code JavaScript et que vous l'exécutez dans un navigateur, le code n'interagit pas directement avec le matériel de votre ordinateur. Au lieu de cela, il interagit avec le moteur JavaScript, qui agit comme un intermédiaire entre votre code et la machine sous-jacente.

Chaque navigateur a son propre moteur JS, mais le plus connu est le moteur v8 de Google. Ce moteur v8 alimente Google Chrome ainsi que Node.js (utilisé pour construire des applications côté serveur).

Dans cet article, vous en apprendrez davantage sur ce qu'est un moteur JS et comment il fonctionne sous le capot.

Voici ce que nous allons couvrir dans ce guide rapide :

* [Comment fonctionne le moteur JavaScript](#heading-comment-fonctionne-le-moteur-javascript)
* [Compilation vs Interprétation](#heading-compilation-vs-interpretation)
* [Qu'est-ce qu'un Runtime JavaScript](#heading-quest-ce-quun-runtime-javascript) ?

## Comment fonctionne le moteur JavaScript

Tout moteur JS contient toujours une pile d'appels et un tas.

La pile d'appels est l'endroit où notre code est exécuté à l'aide du contexte d'exécution. Et le tas est un pool de mémoire non structuré qui stocke tous les objets en mémoire dont notre application a besoin.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/js_engine.png)
_Le moteur JavaScript se compose d'une pile d'appels et d'un tas_

Vous devriez maintenant comprendre où le code est exécuté – mais la question est maintenant de savoir comment le code est compilé en code machine afin qu'il puisse être exécuté par la suite. Mais avant cela, comprenons brièvement la compilation et l'interprétation.

## Compilation vs Interprétation

Dans la compilation, l'ensemble du code est converti en code machine en une seule fois et écrit dans un fichier binaire qui peut être exécuté par un ordinateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/compilation.png)
_Le code source est compilé en code machine puis exécuté lors de l'exécution du programme_

Dans l'interprétation, l'interprète parcourt le code source et l'exécute ligne par ligne. Le code doit toujours être converti en code machine, mais cette fois-ci, cela se fait ligne par ligne lors de l'exécution du programme.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/interpretation.png)
_Le code source est converti en code machine et exécuté en même temps ligne par ligne_

JS était autrefois un langage purement interprété. Mais les moteurs JS modernes utilisent désormais un mélange de compilation et d'interprétation, connu sous le nom de compilation "just-in-time".

Dans la compilation JIT, l'ensemble du code est converti en code machine en une seule fois, puis exécuté immédiatement.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/compilation-1.png)
_Le code source est compilé en code machine et exécuté immédiatement_

Vous vous demandez peut-être quelle est la différence entre la compilation et le JIT. Eh bien, il y a une différence majeure : après la compilation, le code machine est stocké dans un fichier portable. Il peut être exécuté à tout moment – il n'est pas nécessaire de se précipiter immédiatement après le processus de compilation.

Mais dans le cas du JIT, le code machine doit être exécuté dès que la compilation se termine.

Je ne vais pas approfondir ces concepts, mais maintenant, vous comprenez probablement les bases de la compilation, de l'interprétation et du JIT.

### JIT et JavaScript

Comprenons maintenant comment le JIT fonctionne spécifiquement en JavaScript.

Ainsi, chaque fois qu'un morceau de code JavaScript entre dans le moteur, la première étape consiste à analyser le code.

Lors de ce processus d'analyse, le code est analysé dans une structure de données appelée AST (Abstract Syntax Tree). Cela fonctionne en divisant d'abord chaque ligne de code en morceaux significatifs pour le langage (comme les mots-clés const ou function), puis en enregistrant tous ces morceaux dans l'arbre de manière structurée.

Cette étape vérifie également s'il y a des erreurs de syntaxe. L'arbre résultant sera ensuite utilisé pour générer le code machine.

Par exemple, examinons un AST pour cette ligne de code `const greet = "Hello"` :

```json
{
  "type": "Program",
  "start": 0,
  "end": 201,
  "body": [
    {
      "type": "VariableDeclaration",
      "start": 179,
      "end": 200,
      "declarations": [
        {
          "type": "VariableDeclarator",
          "start": 185,
          "end": 200,
          "id": {
            "type": "Identifier",
            "start": 185,
            "end": 190,
            "name": "greet"
          },
          "init": {
            "type": "Literal",
            "start": 193,
            "end": 200,
            "value": "Hello",
            "raw": "\"Hello\""
          }
        }
      ],
      "kind": "const"
    }
  ],
  "sourceType": "module"
}
```

Vous n'avez pas besoin de savoir ou de comprendre comment fonctionnent les AST, cela est juste pour la curiosité.

Vous pouvez jouer et générer votre propre [AST ici](https://astexplorer.net/).

L'étape suivante est la compilation. Ici, le moteur prend l'AST et le compile en code machine.

Ensuite, ce code machine est exécuté immédiatement car il utilise le JIT – rappelez-vous que cette exécution se produit dans la pile d'appels.

Mais ce n'est pas la fin. Le moteur JS moderne génère un code machine inefficace juste pour exécuter le programme aussi rapidement que possible. Ensuite, le moteur prend le code déjà précompilé pour l'optimiser et le recompiler pendant l'exécution déjà en cours du programme. Toutes ces optimisations se font en arrière-plan.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/js_jit.png)
_JIT en JavaScript_

Ainsi, jusqu'à présent, vous avez appris ce qu'est le moteur JS et comment il fonctionne en coulisses. Maintenant, apprenons ce qu'est un runtime JavaScript – et en particulier le runtime du navigateur.

## Qu'est-ce qu'un Runtime JavaScript ?

Un runtime JavaScript (JS) est un environnement complet qui permet l'exécution de code JavaScript. Il se compose de divers composants travaillant ensemble pour faciliter l'exécution des applications JavaScript. Lorsque nous parlons d'un runtime JS, nous parlons généralement de tout l'écosystème qui va au-delà de l'exécution basique du code.

Selon l'endroit où JavaScript est exécuté (le navigateur web ou côté serveur avec Node.js), il peut y avoir des fonctionnalités spécifiques à l'environnement supplémentaires dans le runtime. Par exemple, dans un navigateur, il peut y avoir des fonctionnalités liées à la gestion des événements du navigateur, à l'accès au DOM et à l'interaction avec des fonctionnalités spécifiques au navigateur.

Pour l'instant, nous allons simplement apprendre le runtime JavaScript dans le navigateur.

Imaginez simplement un runtime JS comme une grande boîte qui inclut toutes les choses dont nous avons besoin pour exécuter JavaScript dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/JS_runtime_1.png)
_Runtime JavaScript_

Le cœur d'un runtime JS est le moteur JS.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/JS_runtime_2.png)
_Moteur JavaScript à l'intérieur du runtime JavaScript_

Mais le moteur seul ne suffit pas. Pour fonctionner correctement, nous avons besoin des Web APIs.

Les runtimes JS, en particulier dans le contexte des navigateurs web, sont livrés avec des Web APIs qui fournissent des fonctionnalités supplémentaires au-delà du langage JavaScript de base. Ces APIs incluent des interactions avec le Document Object Model (DOM), XMLHttpRequest (pour faire des requêtes HTTP), des minuteurs, et plus encore.

Les Web APIs étendent les capacités de JavaScript, lui permettant d'interagir avec l'environnement du navigateur et de gérer des tâches comme la manipulation de la structure de la page web, la gestion des événements utilisateur et la réalisation de requêtes réseau.

Ainsi, en gros, les Web APIs sont des fonctionnalités qui sont fournies au moteur mais qui ne font pas partie du langage JavaScript lui-même. JavaScript accède à ces APIs via l'objet `window`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/JS_runtime_3.png)
_Moteur JavaScript et Web APIs dans le runtime JavaScript_

Les opérations asynchrones en JavaScript, telles que la gestion des entrées utilisateur ou la réalisation de requêtes réseau, utilisent des fonctions de rappel. Ces fonctions sont placées dans une file d'attente connue sous le nom de file d'attente de rappel, en attendant l'exécution. La file d'attente de rappel garantit que les tâches asynchrones sont gérées de manière organisée.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/JS_runtime_4.png)
_Moteur JavaScript, Web APIs et file d'attente de rappel dans le runtime JavaScript_

Par exemple, nous attachons des fonctions de gestion d'événements aux événements DOM comme un bouton pour réagir à certains événements. Ces fonctions de gestion d'événements sont également appelées fonctions de rappel. Ainsi, lorsque l'événement de clic se produit, la fonction de rappel sera appelée.

Voici comment cela fonctionne en coulisses :

* Tout d'abord, après que l'événement se produit, la fonction de rappel est placée dans la file d'attente de rappel.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/JS_runtime_5.png)
_l'événement de clic est dans la file d'attente de rappel_

* Ensuite, lorsque la pile d'appels est vide, la file d'attente de rappel est transmise à la pile d'appels afin qu'elle puisse être exécutée et cela se fait par quelque chose appelé la boucle d'événements.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/JS_runtime_7.png)
_l'événement de clic passe maintenant dans la pile d'appels_

Ainsi, en résumé, la boucle d'événements prend les fonctions de rappel de la file d'attente de rappel et les place dans la pile d'appels, afin qu'elles puissent être exécutées.

C'est tout ! Vous connaissez maintenant les bases du fonctionnement du moteur JS et du runtime JS.

## Conclusion

Pour résumer, un moteur JavaScript est un programme conçu pour exécuter du code JavaScript. Il utilise la pile d'appels et le contexte d'exécution, avec toutes les données nécessaires stockées dans le tas.

Lors de l'examen du runtime JavaScript dans un navigateur, il se compose du moteur JS, des Web APIs, de la file d'attente de rappel et d'une boucle d'événements. La boucle d'événements joue un rôle crucial dans le transfert des fonctions de rappel de la file d'attente vers la pile d'appels, assurant l'exécution fluide des applications JavaScript.