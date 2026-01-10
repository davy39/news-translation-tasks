---
title: Comment améliorer vos compétences en débogage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-24T15:51:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-debugging-skills
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fb8cb2d49c47664ed823f4b.jpg
tags:
- name: bugs
  slug: bugs
- name: debugging
  slug: debugging
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
seo_title: Comment améliorer vos compétences en débogage
seo_desc: 'By Ogundiran Ayobami

  ‌‌Whether you are a beginner or expert software developer, you probably find bugs
  in your code.

  ‌‌We all have bugs in our applications because no one knows everything about coding,
  and we sometimes make mistakes. After all, there...'
---

Par Ogundiran Ayobami

Que vous soyez un développeur logiciel débutant ou expert, vous trouvez probablement des bugs dans votre code.

Nous avons tous des bugs dans nos applications parce que personne ne sait tout sur la programmation, et nous faisons parfois des erreurs. Après tout, il n'y a pas moyen de cesser d'être humain.

Ou pouvez-vous me montrer comment développer un superpouvoir ? Ah, très bien, peu importe. :)

Nous pouvons seulement nous étudier nous-mêmes, nos outils et nos bugs pour trouver des solutions qui peuvent nous aider à être plus efficaces dans la réduction des bugs que nous créons.

## Comment pouvons-nous gérer les bugs ?

Il existe trois principales façons de gérer les bugs :

1. Pré-débogage : la réduction des bugs avant qu'ils ne soient créés
2. Débogage : identification, correction et suppression des bugs une fois que vous les trouvez
3. Post-débogage : anticipation des bugs inattendus ou inconnus

Examinons chacun d'eux en détail.

# Qu'est-ce que le pré-débogage ?

Le regretté informaticien [Edsger W. Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) a dit,

> « Si le débogage est le processus de suppression des bugs, alors la programmation doit être le processus de les introduire. »

Si nous introduisons des bugs dans un programme par la programmation, cela signifie que nous devons nous guider pour réduire le nombre de bugs que nous introduisons. J'appelle ce processus de guidage de soi « pré-débogage ».

J'ai recherché « define: debugging » sur Google et la définition que j'ai vue du dictionnaire Oxford m'a fait réfléchir.

Voici la définition :

> « [Le débogage est] le processus d'identification et de suppression des erreurs du matériel ou des logiciels informatiques. »

Quoi ? Est-ce la seule chose que nous faisons ?

La définition m'a fait réfléchir parce que je suis sûr que beaucoup de développeurs logiciels sont proactifs concernant le débogage. Ils améliorent leurs outils et eux-mêmes pour réduire le nombre de bugs qu'ils créent en premier lieu.

Quelques façons de le faire :

1. Écrire des spécifications de programme.
2. Apprendre à vraiment comprendre les outils que vous utilisez.
3. Apprendre à taper avec précision.
4. Vous familiariser avec les messages d'erreur et leurs solutions probables.
5. Toujours vous assurer que vous avez des configurations stables pour la plupart des outils que vous utilisez.

Et bien plus encore !

La définition ne reflète pas tous ces aspects du débogage, et cela m'a forcé à penser « Oh, non ! Quelqu'un doit partager toutes les choses que les développeurs logiciels font pour réduire les bugs. »

Bien que la définition soit acceptable pour le débogage, elle minimise toutes les autres choses que les développeurs logiciels font pour réduire la création de bugs. Alors, passons en revue ces choses maintenant.

### 💡 Apprendre les bases des outils que vous utilisez souvent

Il est important d'apprendre les bases de tout outil que vous utilisez souvent, car cela vous aide à réduire le nombre de bugs que vous créez en codant.

Il n'y a pas moyen d'éviter complètement la création de bugs, mais vous pouvez éviter de créer certains bugs si votre connaissance des bases des outils que vous utilisez est très solide.

Par exemple, de nombreux utilisateurs de JavaScript ne peuvent pas se souvenir de ce que `splice()` retourne. Et certains ne peuvent pas se souvenir de la différence entre les méthodes de tableau `map()` et `forEach()`. Quelle est la différence, de toute façon ? Peu importe ! Nous sommes tous coupables de cela de temps en temps.

Si vous n'êtes pas un utilisateur de JavaScript, choisissez simplement une méthode ou une fonction intégrée du langage que vous utilisez et demandez-vous :

Quel type d'argument cela prend-il ?
Que retourne cela ?
Que se passe-t-il si un argument invalide est fourni ?

Se poser les questions ci-dessus sur chacune des parties intégrées de l'outil que vous utilisez souvent peut vous influencer à apprendre davantage et à rester à jour.

C'est ainsi que vous pouvez vous tenir au courant des bases des outils que vous utilisez souvent, surtout si vous n'avez pas beaucoup de temps pour lire activement.

### 💡 Planifier avant de coder

La programmation peut sembler être un sport d'essai et d'erreur où vous le faites jusqu'à ce que vous obteniez le bon résultat.

De nombreux développeurs logiciels débutants ne comprennent pas vraiment les programmes sur lesquels ils travaillent et certains d'entre eux n'essaient pas vraiment de comprendre les messages d'erreur avant de les rechercher sur Google.

Tout le monde semble maintenant penser que la programmation est toujours une question de « Code, Code, code, Recherche, Débogage ».

Mais il est nécessaire de vraiment comprendre ce que vous faites afin de pouvoir écrire rapidement :

* Ce que nous attendons comme entrées ainsi que la structure et les caractéristiques de telles entrées.
* Ce que nous attendons faire avec les entrées.
* Ce que nous attendons retourner ou faire à la fin en relation avec les entrées ou d'autres choses.
* Ce que nous attendons faire si les entrées attendues ne sont pas données.

En bref, planifier les entrées, les processus et les sorties d'une fonction ou d'un programme n'aide pas seulement à réduire les bugs mais aide également à écrire des tests efficaces.

### 💡 Familiarisez-vous avec les messages d'erreur courants

Il est souvent très facile de corriger une erreur ou un bug si vous vous êtes familiarisé avec ce bug.

C'est pourquoi il est important de prendre le temps d'étudier certaines erreurs courantes et d'apprendre comment les corriger. Parlons de quelques erreurs courantes maintenant :

#### 1. Erreurs de syntaxe

Chaque langage de programmation a ses propres règles, et les développeurs sont susceptibles de violer ces règles.

Les langages de programmation sont stricts quant à leurs règles et ils lanceront des erreurs chaque fois que ces règles sont violées.

Imaginez, par exemple, que vous omettez les parenthèses d'une fonction ou d'une méthode comme ceci :

`function {}`

Une erreur sera lancée.

Se familiariser avec le message d'erreur d'une erreur de syntaxe et comment la corriger vous donnera un avantage lors de son débogage.

Personnellement, j'ai remarqué que la plupart des erreurs de syntaxe mentionnent toujours certains mots-clés qui aident à identifier la partie de votre code qui est défectueuse.

```
let school = { 
name: "Harvard", 
location: "Heaven On Earth", admit: function() { return "weeew! You are admitted" } 
} 
console.log(school.names); // undefined
```

Le « undefined » qui est retourné nous indique si l'objet ou la propriété que nous essayons d'accéder n'est pas disponible. Nous pouvons identifier où se trouve le problème si nous prêtons une attention particulière au message d'erreur.

Maintenant, prenons l'exemple un peu plus loin.

`console.log(school.locations.address);` // Uncaught TypeError: Cannot read property 'address' of undefined.

Si nous prêtons une attention particulière au message d'erreur, nous pouvons facilement identifier où se trouve le bug.

D'après le message d'erreur ci-dessus, « Cannot read property 'address' of undefined » signifie que address est une propriété et qu'une propriété est connue pour être dans un objet (en JavaScript). Mais dans ce cas, l'objet est dit « undefined ».

Plus vous codez, mieux vous devenez pour éviter les erreurs de syntaxe. Vous pouvez également simplement utiliser des éditeurs de code, des linters ou des IDE qui mettent en évidence les erreurs de syntaxe. L'utilisation de ces outils peut vous aider beaucoup.

**Vous pouvez consulter ces linters de code pour voir lequel fonctionne le mieux pour votre cas d'utilisation :**

[ESLint](https://eslint.org/docs/user-guide/getting-started) pour JavaScript

[PyLint](https://www.pylint.org/) pour Python

[Checkstyle](https://github.com/checkstyle/checkstyle) pour Java

[PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) pour PHP

De plus, la plupart des éditeurs de code populaires comme VSCode peuvent être configurés pour utiliser les linters de code ci-dessus.

#### 2. Erreurs de logique/sémantique

Les erreurs de logique sont très difficiles à gérer car elles semblent toujours ne pas avoir d'erreur – mais vous n'obtenez toujours pas le résultat attendu.

Par exemple, une façon simple de confirmer ce type d'erreur est de vérifier le code ci-dessous dans la console du navigateur.

`prompt("enter number") + 3;`

Vous pouvez vous attendre à un nombre comme sortie, mais il retournera une chaîne. En bref, vous n'obtiendrez pas le résultat attendu.

Planifier avant de coder et comprendre les bases du langage de programmation que vous utilisez peut vous aider à gérer les erreurs logiques – à condition de comprendre les exigences du programme qui vous sont données.

#### 3. Erreurs de compilation

Votre programme peut ne pas compiler car vous avez peut-être violé certaines règles que le compilateur s'attend à ce que vous respectiez. Ainsi, le programme sur lequel vous travaillez peut ne pas compiler.

Par exemple, écrire une chaîne sans les guillemets habituels, comme dans `const name = Ayobami`, entraînera une erreur de compilation car une chaîne doit être entre guillemets. Ainsi, le code ne compilera pas.

Cela est similaire aux erreurs de syntaxe, et plus vous codez, mieux vous devenez pour gérer les erreurs de compilation.

Vous pouvez être plus efficace et réduire ces erreurs en compilant ou en testant votre code souvent.

#### 4. Erreurs de ressources

Parfois, votre programme peut dépasser sa limite de mémoire ou utiliser toutes les ressources disponibles. Cela peut entraîner la mise hors service ou le dysfonctionnement de votre application.

Le code ci-dessous est un exemple réel de code qui conduit à des erreurs de ressources.

```javascript
function factorial(num) {
  var result = 1;
  for(var i = num; i > 0; i--){
    result = num * factorial(num-1);
  }
  return result;
}

factorial(5);
factorial(10);
factorial(20);
factorial(0);

```

La fonction `factorial()` plante ou ralentit le navigateur car l'espace de pile, c'est-à-dire la mémoire que le navigateur alloue à la chaîne d'appels de fonctions, est utilisé. L'erreur, dans ce cas, est une erreur de ressources car elle se produit à la suite de l'utilisation de la mémoire allouée (ressources).

#### 5. Erreurs d'interface

Parfois, nous concevons des API de programme pour être utilisées de certaines manières, mais les utilisateurs utilisent les programmes différemment et causent des erreurs. De telles erreurs sont appelées erreurs d'interface.

Par exemple, disons que la méthode `go(string)` attend une chaîne mais que nous l'appelons avec un nombre à la place. Cela entraînera une erreur si le créateur du programme ne prévoit pas et ne gère pas la manière dont le programme doit répondre dans un tel cas.

La plupart des choses dans les logiciels suivent des normes. Si vos normes définies ne sont pas suivies, vous devez fournir à vos utilisateurs des messages d'erreur ou des guides pour les aider à comprendre qu'ils utilisent l'application de manière incorrecte.

Documenter vos API peut beaucoup aider dans ce cas.

### 💡 Assurez-vous que vos configurations sont adaptées à vos outils

Il est important d'avoir une configuration adaptée à vos outils. Parfois, votre système d'exploitation peut ne pas être compatible avec vos applications – peut-être parce qu'il nécessite une version plus récente du système d'exploitation ou qu'il nécessite un certain logiciel.

Par exemple, WampServer peut ne pas fonctionner correctement sur Windows OS si certains Microsoft VC runtimes sont manquants sur l'ordinateur. Des choses similaires peuvent également se produire avec Linux et macOS.

Vous devez simplement être sûr que votre configuration est adaptée à ce que vous faites.

### 💡 Soyez déterministe sur les fonctions de votre programme

> « En mathématiques, en informatique et en physique, un système déterministe est un système dans lequel aucun hasard n'est impliqué dans le développement des états futurs du système.
> 
> Un modèle déterministe produira ainsi toujours la même sortie à partir d'une condition de départ ou d'un état initial donné. » - [Source](https://en.m.wikipedia.org/wiki/Deterministic_system)

La question est alors, comment faire un programme déterministe ? Vous devez être certain du type de données acceptable dans votre programme et rejeter toute donnée qui ne correspond pas.

En bref, vous devez prendre les données attendues et rejeter les données inattendues ou notifier vos utilisateurs sur les données attendues.

### 💡 Ne l'utilisez pas si vous ne le comprenez pas

L'une des meilleures façons de réduire la création de bugs est d'utiliser uniquement les approches, méthodes et classes que vous comprenez. Si vous devez utiliser une approche ou un style que vous ne comprenez pas, recherchez-le et soyez sûr de ce que vous allez faire avant de le faire.

Il est facile d'introduire des bugs inutiles dans votre application chaque fois que vous utilisez des choses que vous ne comprenez pas.

### 💡 Apprenez à taper avec précision

Taper avec précision est sous-estimé, car la programmation est plus une question de réflexion que de frappe. Mais être précis en tapant peut vous aider à réduire certaines erreurs syntaxiques, erreurs de type ou fautes de frappe.

De nombreux bugs de programmation sont causés par de simples erreurs typographiques. Votre capacité à taper avec précision vous donne un avantage dans la réduction des bugs.

### 💡 Observez d'autres développeurs pendant le débogage

Une autre façon intéressante d'améliorer vos compétences en débogage est d'observer d'autres développeurs pendant qu'ils déboguent. Cela aide à voir différentes méthodes de débogage, surtout à travers leurs perspectives.

Il y aura toujours des outils ou des approches que nous ne connaissons pas ou que nous n'utilisons pas pour le débogage. Observer les autres nous donne la chance de découvrir les outils ou les approches dont nous n'avons peut-être pas conscience.

Ou même si vous êtes conscient de ces différentes approches, vous ne savez peut-être pas pourquoi ou comment les utiliser.

Observer les autres peut nous influencer à revisiter ces approches et outils qui peuvent éventuellement améliorer nos compétences en débogage.

# Qu'est-ce que le débogage ?

Le débogage est au cœur de la programmation, car il prend la plus grande partie de votre temps lors du codage.

Il y a trois phases majeures impliquées dans le débogage :

1. Trouver des bugs.
2. Analyser et comprendre pourquoi les bugs se produisent.
3. Corriger ou supprimer les bugs.

### Comment trouver des bugs

Trouver des bugs commence par la compréhension des messages d'erreur que vous voyez.

Il va sans dire qu'un message d'erreur est un indicateur d'un bug. Si vous comprenez le message d'erreur, vous pouvez localiser le bug avec précision.

Mais certaines erreurs peuvent être fatigantes car elles peuvent ne pas avoir de messages d'erreur explicites. Nous n'obtenons peut-être pas le résultat attendu.

Pour trouver des bugs, vous devez :

* Être clair sur vos attentes.
* Vérifier les résultats que vous obtenez.
* Comparer vos attentes et le résultat réel pour voir ce qui manque.

Vous pouvez utiliser un débogueur ou d'autres outils utiles pour trouver ces erreurs rapidement.

Vous pouvez ensuite vérifier différentes parties de votre code par rapport à vos hypothèses et effectuer des essais et erreurs pour trouver le bug.

### Comment comprendre pourquoi les bugs se produisent

Après avoir trouvé un bug, vous devez comprendre pourquoi le code se comporte de cette manière. Faire cela vous aide à construire un système efficace.

Au lieu de cela, de nombreux développeurs se contentent de rechercher sur Google et d'utiliser les réponses qu'ils obtiennent directement de StackOverflow.

Cela est acceptable dans certaines circonstances, mais il est préférable de comprendre la cause d'un bug et pourquoi la solution fonctionne.

Comprendre la cause d'un bug est une étape importante sur le chemin de sa correction ou de la suppression du bug.

### Comment corriger ou supprimer les bugs

Après avoir trouvé et compris la cause d'un bug, nous devons corriger ce bug. Parfois, une fois que vous comprenez ce qu'est le bug, vous trouverez simplement une solution sans stress.

Cependant, il arrive que notre compréhension ne donne aucune solution, peu importe nos efforts.

Au lieu de perdre du temps, il est acceptable de rechercher le message d'erreur ou ce que vous jugez approprié sur Google.

Vous pouvez également demander à une autre personne car les autres ont tendance à voir les choses différemment. Ils sont neutres et cette neutralité aide à corriger certains bugs.

Alors, recherchez sur Google !

Posez des questions sur StackOverflow, Twitter ou là où vous êtes connecté à d'autres développeurs.

C'est acceptable ! Nous faisons tous ces choses un million de fois.

Corriger un bug préoccupant apporte toujours une grande excitation. Mais ne vous laissez pas trop emporter par l'excitation, car corriger un bug peut en causer un autre. Assurez-vous d'abord de ne pas avoir introduit un autre problème dans le programme. C'est pourquoi les tests automatisés sont importants.

# Qu'est-ce que le post-débogage ?

Le « post-débogage » consiste à anticiper les bugs inattendus dans les programmes que vous avez déjà écrits.

Il fait référence à tous les mécanismes que vous pourriez utiliser pour garantir que les bugs inconnus sont facilement suivis ou gérés avant qu'ils ne nuisent au système ou à l'entreprise.

La question maintenant est de savoir comment faire cela ? Eh bien, avec un système de suivi des erreurs.

Vous devriez avoir un système de suivi des erreurs en production afin de pouvoir découvrir facilement les bugs dès qu'ils apparaissent après avoir poussé votre application en production.

Il existe de nombreux systèmes de suivi des erreurs et ils ne sont qu'à quelques recherches sur Google. Mais en voici quelques-uns que vous pouvez consulter :

* www.sentry.io
* www.honeybadger.io
* www.pypi.org
* www.airbrake.io
* www.logrocket.com

Il existe de nombreux systèmes de suivi des erreurs, vous devrez simplement faire des recherches pour découvrir ce qui est le mieux pour vous.

## Conclusion

Le débogage est une compétence majeure que tous les développeurs logiciels doivent cultiver. Il est au cœur du codage, et si vous le faites bien, cela peut faire de vous un meilleur développeur.

Pour être excellent en débogage, vous devez apprendre autant que possible sur diverses méthodes de débogage, dont beaucoup ont été discutées ici dans cet article.

Il est temps de devenir un excellent développeur logiciel et le débogage peut vous aider en cours de route.

Maintenant, vous devez simplement mettre tout en pratique pour être excellent en débogage et vos compétences en développement logiciel ne seront plus jamais les mêmes.

## À propos de l'auteur

**[Ayobami](https://twitter.com/codingnninja)** aime écrire l'histoire avec le développement logiciel et aide actuellement ceux qui ont du mal à comprendre et à construire des projets avec JavaScript à travers **[You Too Can Code](https://bit.ly/3o3TMyg)**.