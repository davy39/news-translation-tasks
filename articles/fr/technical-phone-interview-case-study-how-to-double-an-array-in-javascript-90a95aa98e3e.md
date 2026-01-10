---
title: 'Étude de cas d''entretien téléphonique technique : Comment doubler un tableau
  en JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-17T17:17:24.000Z'
originalURL: https://freecodecamp.org/news/technical-phone-interview-case-study-how-to-double-an-array-in-javascript-90a95aa98e3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aAXkqX-3cNpp0EGaXCplFg.jpeg
tags:
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: jobs
  slug: jobs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Étude de cas d''entretien téléphonique technique : Comment doubler un
  tableau en JavaScript'
seo_desc: 'By Jane Philipps

  Technical phone screens are a crucial step in the technical interview process. Often,
  whether or not you pass the technical phone screen will dictate whether you’ll be
  invited for an on-site interview.

  Technical phone screens can be ...'
---

Par Jane Philipps

Les entretiens téléphoniques techniques sont une étape cruciale dans le processus d'entretien technique. Souvent, le fait de réussir ou non l'entretien téléphonique technique déterminera si vous serez invité à un entretien sur place.

Les entretiens téléphoniques techniques peuvent être difficiles car vous devez réfléchir à voix haute tout en travaillant sur un problème sans avoir l'avantage d'être présent en personne avec votre interlocuteur. Lorsque vous passez un entretien avec quelqu'un par téléphone ou vidéo, il peut être difficile de faire passer toute votre présence. Habituellement, vous travaillerez dans un éditeur partagé, donc pendant que vous travaillez sur un problème, l'interviewer ne pourra que vous entendre et voir ce que vous tapez. Beaucoup de gens trouvent plus difficile de communiquer de cette manière que en personne.

La bonne nouvelle est que les entretiens téléphoniques techniques sont quelque chose que vous pouvez pratiquer et améliorer. Comme toute compétence, plus vous les faites, meilleur vous devenez. Finalement, vous commencerez à voir des résultats, car vous serez invité à des entretiens sur place avec de plus en plus d'entreprises.

Bien que tous les entretiens téléphoniques techniques soient différents, la plupart vous demanderont de réfléchir rapidement. Le meilleur moyen de se préparer est donc simplement de pratiquer en travaillant sur des questions. Vous pouvez les parcourir seul en les expliquant à voix haute, et vous pouvez également vous entraîner avec un ami. Si vous vous entraînez seul, vous pourriez même vous enregistrer pour écouter ensuite l'enregistrement et voir si votre explication de votre processus de réflexion avait du sens.

Enfin, vous pouvez vous entraîner en passant des entretiens avec des entreprises ! Lorsque j'ai passé des entretiens pour un nouveau rôle, j'ai commencé par trouver des entreprises qui m'intéressaient, mais pour lesquelles je ne serais pas déçu si je ne passais pas l'entretien téléphonique technique. Ainsi, je me sentais toujours sous pression pour me préparer, mais je m'attendais à échouer quelques fois au début. Cela a été moins décevant lorsque je n'ai pas passé à l'étape suivante.

Dans cet article, je vais parcourir une question que j'ai reçue lors d'un entretien téléphonique technique pour vous donner un cadre pour aborder ce type d'entretiens. J'espère que cela sera utile, et je suis ouverte à vos commentaires et retours !

Commençons.

### La question

Il s'agissait d'une question réelle que j'ai reçue d'un interviewateur. J'aime cette question, car il existe plusieurs façons de la résoudre. La manière dont vous la résolvez reflète votre style de programmation et aide l'interviewer à évaluer si vous seriez adapté au poste.

Voici la question d'exemple pour l'entretien :

```
Étant donné un tableau, écrivez une fonction qui double le tableau.Exemple : étant donné [1,2,3,4,5], votre fonction doit retourner [1,2,3,4,5,1,2,3,4,5].Vous pourriez l'appeler comme ceci : myArray.double().
```

### Répondre à la question

Voici mes cinq étapes pour aborder un problème lors d'un entretien téléphonique technique :

**1. Clarifier la question**

**2. Penser à de petits cas de test, y compris les cas limites**

**3. Pseudo-coder votre solution (optionnel)**

**4. Traduire votre pseudo-code en code réel**

**5. Tester votre solution en utilisant les cas de test que vous avez imaginés précédemment**

#### 1. Clarifier la question

La première chose à faire lorsque l'on vous pose une question d'entretien comme celle-ci est de poser des questions de clarification.

Dans ce cas, la question est relativement simple : je comprends que je dois écrire une fonction qui prend un tableau en entrée et retourne un tableau qui a été manipulé. Comprendre l'entrée et la sortie d'une fonction aboutit à ce qui est souvent considéré comme une [signature de fonction](https://developer.mozilla.org/en-US/docs/Glossary/Signature/Function).

#### 2. Penser à de petits cas de test, y compris les cas limites

Ensuite, vous voudrez penser à quelques exemples plus petits, qui serviront de cas de test plus tard :

```
// Que se passe-t-il lorsque le tableau donné est vide ?[] => []
```

```
// Que se passe-t-il lorsque le tableau donné n'a qu'un seul élément ?[1] => [1,1]
```

```
// Que se passe-t-il lorsque le tableau donné n'a que 2 éléments ?[1,2] => [1,2,1,2]
```

```
// Que se passe-t-il lorsque le tableau donné a N éléments ?[1...N] => [1,2,3,4,5...N,1,2,3,4,5...N]
```

Penser à ces cas avant de commencer à coder vous aidera à rechercher et à établir des motifs pour ce que vous essayez de résoudre. Cela vous aidera également à réfléchir à la complexité spatiale ou temporelle, ce qui pourrait faire l'objet d'une question de suivi plus tard. Cela aide également à s'assurer que vous avez bien compris la question, car cela donne à votre interlocuteur l'occasion de corriger toute idée fausse.

#### 3. Pseudo-coder votre solution (optionnel)

Maintenant que vous avez clarifié le problème et pensé à quelques cas de test exemples, il est temps de réfléchir à la solution réelle. C'est là que le pseudo-code peut être utile. Si vous n'êtes pas familier avec le pseudo-code, il s'agit de l'idée d'écrire ce que vous voulez faire en langage clair ou en syntaxe de code simplifiée avant d'écrire le code fonctionnel. C'est un moyen de vous aider à organiser vos pensées avant de vous lancer directement dans le code.

Le pseudo-code peut être incroyablement efficace pour vous aider à rester sur la bonne voie pendant votre entretien. Personnellement, j'aime le faire, car cela m'aide à rester organisée. Si je suis bloquée, je peux me référer aux étapes que j'ai écrites en pseudo-code pour me remettre sur la bonne voie.

J'ai déjà eu un entretien téléphonique où j'ai écrit les étapes en pseudo-code avant d'écrire le code réel. L'interviewer a pu me guider en pointant l'étape dans mon pseudo-code que je devais suivre ensuite. Dans ce cas, l'interviewer a également mentionné qu'il n'avait jamais vu personne faire cela auparavant et a été incroyablement impressionné. Ainsi, le pseudo-code a également l'avantage de montrer à votre interlocuteur que vous êtes organisée et de l'impressionner avec ces compétences !

Revenons donc à la question en cours, voici un pseudo-code que vous pourriez écrire :

```
// Définir une fonction qui prend un tableau en entrée// Boucler sur le tableau// Pousser chaque élément du tableau à la fin du tableau// Retourner le tableau
```

#### 4. Traduire votre pseudo-code en code réel

Maintenant que vous avez écrit du pseudo-code, il est temps de faire du codage. Pour cette question, la première (incorrecte) solution à laquelle j'ai pensé ressemblait à ceci :

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {
```

```
  for (var i = 0; i < array.length; i++) {    array.push(array[i]);  }
```

```
  return array;
```

```
}
```

```
double(array);
```

Maintenant, cela semble assez simple, n'est-ce pas ? Cependant, il y a un petit piège à cette question que j'ai seulement découvert en codant ma solution et en essayant de l'exécuter. Cela m'amène à l'étape finale !

#### 5. Tester votre solution en utilisant les cas de test que vous avez imaginés précédemment

Si vous êtes un programmeur expérimenté, vous pourriez facilement repérer le bug dans ma solution ci-dessus. Mais ce n'est que lorsque j'ai exécuté mon code que j'ai réalisé que j'avais créé une redoutable [boucle infinie](https://en.wikipedia.org/wiki/Infinite_loop) !

Pourquoi cela crée-t-il une boucle infinie ? La longueur `array.length` que j'utilisais pour savoir quand ma boucle `for` s'arrêterait augmentait dynamiquement à mesure que je poussais de nouveaux éléments dans le tableau ! Ainsi, lorsque la boucle `for` a commencé, `array.length` était égal à 5. Mais après la première itération de la boucle `for`, `array.length` était égal à 6, et ainsi de suite à l'infini.

Cependant, il existe une modification simple qui rendra cette solution fonctionnelle :

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {
```

```
  var length = array.length;
```

```
  for (var i = 0; i < length; i++) {    array.push(array[i]);  }
```

```
  return array;
```

```
}
```

```
double(array);=> [1,2,3,4,5,1,2,3,4,5]
```

TEMPS D'EXÉCUTION : O(n) = linéaire

Avec cette modification, je déclare une variable appelée `length` dans la portée de la fonction, puis je l'utilise comme délimiteur pour ma boucle `for`. Même si la taille de mon tableau change maintenant, la boucle `for` s'arrête toujours après la 5ème itération, car la variable de longueur ne change pas lorsque `array.length` change.

Maintenant, je peux tester mon code avec les cas limites que j'ai imaginés précédemment et voir que les résultats sont ceux attendus :

```
// Passer un tableau vide donne un tableau vide correctement :[] => []
```

```
// Passer un tableau avec un seul élément donne le tableau correct avec 2 éléments :[1] => [1,1]
```

```
// Passer un tableau avec seulement 2 éléments donne le tableau correct avec 4 éléments :[1,2] => [1,2,1,2]
```

```
// Passer un tableau avec 10 éléments donne le tableau correct avec 20 éléments :[1,2,3,4,5,6,7,8,9,10] => [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
```

### Solutions alternatives

Ce qui précède est une façon de résoudre cette question, mais il existe également quelques autres alternatives. Vous vous souvenez lorsque j'ai introduit la question ci-dessus avec la suggestion d'appeler la fonction en écrivant quelque chose comme `myArray.double()` ? Si vous êtes familier avec la programmation orientée objet, vous reconnaîtrez peut-être cette syntaxe. Dans ce cas, l'idée générale est que vous ajouteriez en réalité une méthode de tableau appelée `double` en utilisant la chaîne de prototypes, que vous pourriez ensuite appeler.

Voici un exemple de la façon dont je pourrais faire cela en utilisant la structure de boucle `for` de ma solution originale :

```
Array.prototype.double = function() {  var length = this.length;
```

```
  for (var i = 0; i < length; i++) {    this.push(this[i]);  }
```

```
  return this;}
```

```
var myArray = [1,2,3,4,5];
```

```
myArray.double();=> [1,2,3,4,5,1,2,3,4,5]
```

En définissant la fonction en utilisant la chaîne de prototypes JavaScript, je n'ai pas réellement besoin de lui passer quoi que ce soit car j'ai accès au tableau sur lequel la méthode est appelée avec `this`. Pour en savoir plus sur le mot-clé `this`, lisez la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this).

Maintenant, ces solutions sont excellentes, mais que dire de répondre à cette question sans utiliser de boucle `for` ? Une façon est d'utiliser la méthode intégrée JavaScript `forEach`. C'est la même idée qu'une boucle `for`, mais au lieu de dire au programme comment exécuter notre code (programmation impérative), nous allons lui dire quel est le résultat (programmation déclarative). Vous pouvez en savoir plus sur la programmation impérative vs déclarative [ici](https://tylermcginnis.com/imperative-vs-declarative-programming/).

Voici un exemple de la même solution utilisant `forEach` :

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {
```

```
  array.forEach(function(value) {    array.push(value);  });
```

```
  return array;}
```

```
double(array);=> [1,2,3,4,5,1,2,3,4,5]
```

TEMPS D'EXÉCUTION : O(n) = linéaire

Enfin, voici une autre solution à ce problème, que j'ai trouvée avec quelques recherches rapides sur Google.

Il existe également une méthode de tableau intégrée appelée `concat` que vous pouvez utiliser :

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {  var doubled = array.concat(array);
```

```
  return doubled;}
```

```
double(array);=> [1,2,3,4,5,1,2,3,4,5]
```

TEMPS D'EXÉCUTION : O(n) = linéaire

**NOTE :** Si vous vous demandez si vous pouvez faire des recherches sur Google pendant votre entretien téléphonique, voici mon avis après avoir participé à plus d'une douzaine d'entretiens téléphoniques techniques : généralement, c'est complètement acceptable.

Les entretiens téléphoniques techniques sont souvent programmés pour 45 minutes à 1 heure. Une partie de ce temps est réservée à l'interviewer pour poser des questions sur votre expérience, tandis qu'une autre partie est réservée pour que vous posiez des questions. Le temps que vous passez à coder peut varier de 30 à 45 minutes selon l'entreprise et l'interviewer.

Dans de nombreux cas, votre interviewer pourra vous aider avec des conseils rapides et de petits indices si vous avez une idée générale de la manière de faire quelque chose mais que vous devez chercher les détails. Par exemple, j'ai déjà eu un interviewer qui connaissait l'expression régulière dont j'avais besoin pour effectuer une fonction spécifique, donc je n'ai pas eu besoin de passer du temps à la trouver. Cela a permis à l'entretien de se dérouler plus facilement.

Cependant, j'ai également eu des expériences où un interviewer m'a demandé de refactoriser ma solution originale d'une autre manière et a explicitement dit qu'il était acceptable de consulter la documentation. C'est généralement le cas, car de nombreux développeurs passent du temps quotidiennement à lire ou à référencer des documents. Être capable de suivre ce même schéma lors d'un entretien téléphonique technique est un bon signe.

Cependant, chercher une solution sur Google pendant votre entretien peut également être une perte de temps, surtout si vous ne cherchez pas avec la bonne phrase (c'est là que plus vous cherchez, meilleur vous deviendrez).

Pour cet exemple spécifique, si j'avais déjà connu la méthode concat de JavaScript, elle aurait pu me venir à l'esprit lorsque j'ai été confrontée à ce problème. Ensuite, chercher sur Google pour me rappeler comment concat fonctionnait aurait été acceptable.

Mais si j'avais passé du temps à chercher sur Google comment doubler un tableau avant même d'essayer de réfléchir au problème moi-même, cela aurait pu être un signal d'alarme pour l'interviewer. Les entretiens téléphoniques techniques sont un bon moyen pour un interviewer de se faire une idée de votre façon de penser, et cela dépend vraiment de ce qu'ils recherchent en termes de poste pour lequel ils recrutent.

D'un autre côté, certaines entreprises vous diront explicitement que vous n'êtes pas autorisé à utiliser Google pour obtenir de l'aide, donc dans ces cas, il est préférable de ne pas le faire. Bien sûr, si vous n'êtes pas sûr, demandez à votre interviewer.

### Conclusion

Pourquoi je vous montre tous ces exemples ? Comme vous pouvez le voir, il n'y a pas qu'une seule façon d'aborder ce problème. Il existe plusieurs approches que vous pouvez adopter, et la manière dont vous abordez le problème dépend d'une combinaison de votre formation et de votre façon de penser à la résolution de problèmes. Pour moi, je penche souvent pour les boucles puisque les boucles `for` étaient l'un des premiers concepts de programmation que j'ai appris. Mais quelqu'un qui a déjà utilisé `concat` pourrait y penser immédiatement.

Je pensais que ce problème était un bon exemple, car il semble relativement simple au premier abord. Cependant, il existe des moyens de se tromper (comme vous l'avez vu avec ma boucle infinie ci-dessus), et il existe plusieurs solutions qui démontrent divers niveaux de connaissances spécifiques. Pourtant, vous pourriez également résoudre cela avec une idée solide écrite en pseudo-code et quelques recherches sur Google.

Gardez à l'esprit que vous ne réussirez pas toujours les entretiens téléphoniques techniques, mais plus vous en ferez, meilleur vous deviendrez. Et, si vous avez appris quelque chose de l'entretien, même si c'était quelque chose de petit, cela valait probablement la peine.

### Un dernier conseil

N'oubliez jamais de remercier votre interviewer par e-mail, de préférence avant la fin du même jour ouvrable où vous avez passé l'entretien avec eux. Même si l'entreprise n'est pas votre premier choix, quelqu'un a pris du temps dans son emploi du temps chargé pour vous interviewer, il est donc important de les remercier. Et, si vous avez appris quelque chose de nouveau, un rapide e-mail de remerciement est un excellent moyen de le réitérer.

Quelle a été votre expérience avec les entretiens téléphoniques techniques ? Les aimez-vous ? Les détestez-vous ? Quel a été le problème le plus intéressant que vous avez eu à résoudre ? Laissez un commentaire ci-dessous ou faites-le moi savoir en m'envoyant un e-mail à [jane [at ] fullstackinterviewing [dot ] com](mailto:jane@fullstackinterviewing.com).

Avez-vous aimé cet article ? Êtes-vous intéressé à décrocher l'emploi de vos rêves en développement logiciel ? [Inscrivez-vous à ma liste de diffusion](https://www.fullstackinterviewing.com/fcc-case-study.html).