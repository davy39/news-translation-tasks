---
title: 'Le guide du débutant pour écraser les bugs : comment utiliser votre débogueur
  et autres outils pour trouver et corriger les bugs'
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-12-05T15:46:00.000Z'
originalURL: https://freecodecamp.org/news/the-beginner-bug-squashing-guide
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/bug.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: bugs
  slug: bugs
- name: debugging
  slug: debugging
- name: 'Junior developer '
  slug: junior-developer
seo_title: 'Le guide du débutant pour écraser les bugs : comment utiliser votre débogueur
  et autres outils pour trouver et corriger les bugs'
seo_desc: 'As web developers, it often feels like we spend more time fixing bugs and
  trying to solve problems than we do writing code. In this guide we''ll look at some
  common debugging techniques, so let''s get stuck in.

  "Fail to prepare, prepare to fail"

  What b...'
---

En tant que développeurs web, nous avons souvent l'impression de passer plus de temps à corriger des bugs et à essayer de résoudre des problèmes qu'à écrire du code. Dans ce guide, nous allons examiner quelques techniques de débogage courantes, alors plongeons-nous dans le sujet.

### "Échouer à préparer, c'est préparer à échouer"

Quelle meilleure façon de commencer un article qu'avec un vieux cliché ! Les bugs et les problèmes vont surgir. Il n'y a tout simplement aucun moyen d'y échapper (désolé). Avec une planification simple, il existe des moyens de minimiser la complexité et le nombre de problèmes auxquels nous sommes confrontés.

## Divisez la tâche en tâches plus petites

Maintenant, je comprends, nous sommes tous enthousiastes et plongeons directement dans nos projets de codage. Le problème est que, sans une sorte de plan, nous créons des problèmes pour nous-mêmes avant même de commencer !

Si je vous disais : "vous devez créer une application de liste de courses", et que vous commenciez à coder immédiatement, que se passerait-il ? Vous vous retrouveriez à fixer un curseur clignotant en vous demandant comment ou quoi faire en premier, en maudissant mon nom sous votre souffle pour vous avoir demandé de faire une telle tâche.

Il est toujours plus facile de prendre un grand problème et de le diviser en plusieurs petits problèmes. Par exemple, nous pouvons diviser le projet de liste de courses en tâches plus petites :

* Créer un formulaire pour ajouter un article à la liste
* Permettre à un utilisateur de supprimer un article de la liste
* Afficher un nombre total d'articles dans la liste

Vous pouvez même diviser ces tâches en tâches plus détaillées. Par exemple, pour la première tâche de notre liste, notre première "petite mini-tâche" (devrais-je déposer cette marque ?) pourrait être :

1) Créer un champ de saisie pour capturer le nom de l'article

2) Créer un bouton qui appelle une fonction `addToList()` lorsqu'il est cliqué

3) Écrire la logique dans la fonction `addToList()` qui ajoute l'article à la liste

Et ainsi de suite. Vous voyez l'idée. Je préfère diviser le travail comme cela car cela me fait vraiment réfléchir aux problèmes que je rencontrerai tôt et aux solutions ([J'ai écrit un article approfondi à ce sujet ici](https://www.freecodecamp.org/news/a-walk-through-the-developer-thought-process/)) avant d'avoir écrit du code. Cela m'aide également à comprendre ce que j'essaie de faire, et me met dans la "zone". Il est beaucoup plus facile de résoudre les problèmes qui surviennent lorsque vous comprenez ce que vous essayez d'accomplir.

## Soyez prêt à purger votre code

Pour faire une omelette, il faut casser quelques œufs. Cela signifie être prêt à réécrire complètement notre code pour le faire fonctionner.

Je parie que vous pensez : "oh, il m'a fallu des jours/semaines/millénaires pour en arriver là avec mon code, et maintenant je dois le supprimer ?!" Eh bien, oui. Parfois. Désolé. La réalité avec le développement web est que le code changera tout le temps, pour diverses raisons - bugs, revues de code, changements de exigences, ennui, etc.

Parfois, nous nous sentons si précieux à propos de notre code et ne supportons pas de le supprimer, que nous essayons de surmonter les problèmes en essayant de "faire entrer un pieu rond dans un trou carré". Nous pensons "NON ! Je ne peux pas supprimer cette méthode. Cela m'a pris une éternité. Il doit y avoir un moyen !" Ce blocage mental cause nos propres problèmes - car en réécrivant simplement ce que nous avons actuellement, nous pourrions trouver la solution à nos problèmes.

Maintenant que nous sommes bien préparés, examinons ce qui se passe lorsque les choses tournent mal.

## Les messages d'erreur sont bons

Quoi de pire que de voir un message d'erreur lorsque quelque chose ne va pas ? Ne pas voir de message d'erreur lorsque quelque chose ne va pas. Même si c'est un sentiment intimidant de voir une grande trace de pile rouge lorsque nous exécutons notre code soigneusement élaboré, les messages d'erreur sont là pour dire "oui, les choses sont en désordre en ce moment, mais voici quelques endroits où vous pouvez commencer à le réparer".

Si nous jetons un coup d'œil à cet exemple :

```javascript
let animals;

function addAnimal(){
	animals.push('elephant');
}

addAnimal();
```

Maintenant, regardons l'erreur :

```
TypeError: Cannot read property 'push' of undefined
at addAnimal (https://vanilla.csb.app/src/index.js:8:11) 
at evaluate (https://vanilla.csb.app/src/index.js:11:1) 
at $n (https://codesandbox.io/static/js/sandbox.acff3316.js:1:148704)
```

J'ai omis une partie de la trace de pile car la plupart est, eh bien, du charabia. Selon la manière dont votre projet frontend gère les messages d'erreur, vous pouvez même voir l'erreur dans votre navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-20-at-17.00.45.png)
_Regardez cette beauté d'erreur !_

Les parties importantes de la trace de pile sont généralement en haut - le message, la fonction et le numéro de ligne, et notre navigateur nous montre cela également. Donc l'interpréteur fait de son mieux pour nous dire ce qui ne va pas. Dommage qu'il ne puisse pas résoudre le problème pour nous, hein ?

Alors, nous avons fini d'avoir notre crise de panique en voyant l'erreur et avons recueilli quelques informations à partir du message d'erreur. Si nous le décomposons, nous pouvons voir cette ligne :

```
Cannot read property 'push' of undefined
```

Cela signifie généralement qu'il y a une variable non définie ou non initialisée quelque part. MAIS OÙ ?!?

Si nous continuons à lire la trace de pile, nous voyons que l'erreur se produit dans la fonction `addAnimal()`. Nous pouvons voir que nous essayons de pousser un nouvel animal dans un tableau - ah ! J'ai oublié d'initialiser le tableau `animals`. Doh ! Notre code corrigé ressemble à ceci :

```javascript
let animals = [];

function addAnimal() {
	animals.push("elephant");
}

addAnimal();
```

L'erreur lancée dans le navigateur vous montrera le problème plus rapidement, mais tous les projets frontend ne seront pas configurés pour le faire, et les développeurs backend n'ont pas ce luxe. C'est pourquoi je recommande d'apprendre à lire la trace de pile.

## Pour vaincre le bug, vous devez penser comme le bug

La trace de pile vous donne une idée de ce qu'est l'erreur. Eh bien, parfois oui et parfois non. Et si vous voyez un message d'erreur qui ressemble plus à des glyphes de grotte qu'à de l'anglais ? Ou s'il n'y a pas d'erreur, mais que votre code ne se comporte tout simplement pas comme vous le pensiez ?

Il est temps de sortir le débogueur. Passons en revue un autre exemple. Mais d'abord un peu de contexte !

M. Bob CEO (qui est un PDG, qui l'aurait cru ?!) s'approche de vous et dit :

"Hey, j'ai une idée géniale pour un produit.

* Je veux une application web qui permet à l'utilisateur d'entrer un nombre.
* Si le nombre est inférieur à 5, le message doit indiquer "INFÉRIEUR".
* Si le nombre est égal ou supérieur à 5, le message doit indiquer "SUPÉRIEUR".

C'est une idée de million de dollars et je veux que vous la construisiez pour moi".

"D'ACCORD !" Dites-vous, et vous vous mettez au travail.

**_*Montage de codage avec musique dramatique pendant que le temps avance rapidement*_**

Vous avez terminé le code de votre application web. Hourra !

```html
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>My super awesome number app</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

</head>

<body>
    <input id="number-input"></input> <button id="number-input-submit-button">Submit</button>
    <div id="number-display">0</div>
    <script src="./index.js" type="text/javascript"></script>
</body>
</html>
```



```javascript
(function () {
    const numberInputSubmitButton = document.getElementById("number-input-submit-button")

    numberInputSubmitButton.addEventListener("click", function () {

        const numberInputValue = document.getElementById("number-input").value;

        let text;
        if(numberInputValue > 5) {
            text = "OVER";
        } else {
            text = "UNDER";
        }

        document.getElementById("number-display").innerHTML = text
    });
})();


```

(Note : Vous avez peut-être déjà repéré le bug. Si c'est le cas, faisons semblant que non. Si vous n'avez pas remarqué le bug, ce n'est pas grave.)

Il est temps de commencer les tests. Passons en revue quelques cas d'utilisation pour notre logique métier.

1) L'utilisateur entre 3 :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-20-at-17.18.36.png)

2) L'utilisateur entre 7

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-09.38.25.png)

Jusqu'à présent, tout va bien ! Mais que se passe-t-il si nous entrons 5 ?

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-09.38.35.png)

OH NON ! Un bug ! Le texte affiché est incorrect, il devrait afficher "**SUPÉRIEUR**" mais affiche plutôt "**INFÉRIEUR**". Hmm, pas de messages d'erreur, et je ne semble pas voir dans le code ce qui ne va pas. **Utilisons le débogueur et passons en revue le code.**

### Utilisation du débogueur

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-09.39.41.png)
_Remarquez le panneau "variables" à gauche - cela peut être un sauveur de vie_

Un bon point de départ est de placer un **point d'arrêt aussi près que possible du code bogué.** Vous pouvez déterminer cela en lisant le code, les messages d'erreur, ou si vous avez ce moment "_ah-ha ! Je sais quelle méthode cause cela_ ". À partir de là, il s'agit de passer en revue le code, d'inspecter les variables et de vérifier si les bonnes branches de code sont exécutées.

Dans notre exemple, j'ai placé un point d'arrêt au début de mon `if statement` - car c'est là que se trouve la logique défaillante.

Une fois que je commence le débogage, Chrome s'ouvre et je peux reproduire le problème en entrant "5" et en cliquant sur submit. Cela atteint le point d'arrêt, et immédiatement il y a quelques choses à noter :

* Le débogueur s'arrête au point d'arrêt, donc cela signifie que je suis sur la bonne voie
* Cela signifie également que la fonction est appelée correctement, et que les gestionnaires d'événements fonctionnent comme prévu
* Je peux également voir que la saisie de l'utilisateur est capturée correctement (à partir du panneau "variables" sur le côté gauche, je peux voir que "5" a été entré)

Jusqu'à présent, tout va bien, pas de problèmes immédiats à craindre. Enfin, pas de problèmes liés au code en tout cas. Ensuite, j'appuierai sur **F10 pour passer en revue le code**. Cela exécute chaque instruction individuellement, nous permettant d'inspecter les éléments, les variables et autres choses à notre propre rythme. La technologie n'est-elle pas fabuleuse ?

Rappelez-vous que puisque je m'attends à ce que le message "SUPÉRIEUR" apparaisse lorsque l'utilisateur entre "5", je m'attends à ce que le débogueur m'emmène dans la première branche de l'instruction if...

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-09.39.58.png)

MAIS NON ! Je suis amené dans la deuxième branche. Pourquoi ? Je dois modifier la condition pour qu'elle lise "**supérieur ou égal à**" au lieu de "**supérieur à**".

```javascript
if(numberInputValue >= 5) {
	text = "OVER";
} else {
	text = "UNDER";
}
```

Succès ! Notre bug est corrigé. Espérons que cela vous donne une idée de la manière de parcourir le code, en utilisant les outils de débogage géniaux de VSCodes.

## Plus de conseils de débogage

* Si vos points d'arrêt ne sont pas atteints, cela pourrait faire partie du problème. Assurez-vous que les fonctions ou gestionnaires d'événements corrects sont appelés de la manière dont vous l'attendez
* Vous pouvez "sauter" les fonctions que vous souhaitez ignorer. Si vous souhaitez déboguer les fonctions que vous rencontrez, utilisez la commande "entrer dans"
* Surveillez les variables, paramètres et arguments lorsque vous parcourez votre code. Les valeurs sont-elles celles que vous attendez ?
* Écrivez du code de manière à ce qu'il soit plus facile à lire/déboguer. Cela peut sembler cool d'avoir votre code sur une seule ligne, mais cela rend le débogage plus difficile

### Google est votre ami

D'accord, nous avons examiné la trace de pile, essayé le débogage, et nous sommes toujours coincés avec ce bug. La seule chose à faire maintenant est de faire un sacrifice aux dieux du codage et espérer que les choses se réparent toutes seules !

Ou je suppose que nous pourrions utiliser Google.

Google est une mine d'or de problèmes et de solutions de développement logiciel, tous à portée de main. Il peut être difficile d'accéder à ces informations, car vous devez savoir comment rechercher les bonnes choses pour obtenir les bonnes informations ! Alors, comment utiliser efficacement Google ?

Revenons à notre premier exemple - vous avez lu la trace de pile, regardé le code, mais le message `Cannot read property 'push' of undefined` vous rend toujours fou. Désorienté, vous vous tournez vers Google dans l'espoir de trouver une réponse. Voici quelques choses à essayer :

**Copiez et collez le message d'erreur.** Parfois, cela fonctionne, selon le degré de "généricité" du message d'erreur. Par exemple, si vous obtenez une **exception de pointeur nul** (qui n'aime pas cela ?), rechercher "Null pointer exception" sur Google ne renverra peut-être pas de résultats très utiles.

**Recherchez ce que vous essayez de faire.** Par exemple, _"Comment créer un tableau et ajouter un élément à la fin"_. Vous pourriez trouver qu'un développeur généreux a posté une solution utilisant les meilleures pratiques sur StackOverflow, par exemple. Vous pourriez également constater que cette solution est complètement différente de la vôtre - rappelez-vous ce que j'ai dit sur le fait d'être à l'aise avec la purge de votre code ?

Une note à propos de l'utilisation du code de quelqu'un d'autre - essayez d'éviter de copier et coller aveuglément, assurez-vous de comprendre ce que le code fait d'abord !

### Demander de l'aide de la bonne manière

Espérons qu'après un mélange de débogage, d'investigation de la trace de pile et de recherche sur Google, vous avez vu la lumière au bout du tunnel et résolu votre problème. Malheureusement, selon ce que vous essayez de faire, vous pourriez encore être un peu bloqué. C'est un bon moment pour demander conseil à d'autres personnes.

Maintenant, avant de courir dans la rue en criant "mon code est cassé, aidez-moi !", il est important de savoir la meilleure façon de demander de l'aide. Demander de l'aide de la bonne manière facilite la compréhension du problème et vous aide à le résoudre. Examinons quelques exemples :

**Mauvais** - "Mon code est cassé et je ne sais pas ce qui ne va pas."

**Bon** - "J'essaie d'ajouter un élément à la fin d'un tableau en JavaScript, et j'obtiens ce message d'erreur : Cannot read property 'push' of undefined. Voici mon code jusqu'à présent."

Vous voyez comment l'exemple "Bon" est beaucoup plus informatif ? Plus d'informations facilitent l'aide des autres développeurs bienveillants. C'est une bonne habitude à prendre car cela vous bénéficie non seulement lorsque vous apprenez à coder, mais aussi dans votre premier emploi lorsque vous devez demander de l'aide.

Alors, où pouvez-vous demander de l'aide ?

* StackOverflow
* Twitter
* Groupes Slack
* Collègues ou amis développeurs

Conseil rapide : Vous pouvez utiliser un outil comme [CodeSandbox.io](https://www.freecodecamp.org/news/the-beginner-bug-squashing-guide/codesandbox.io) ou [CodePen.io](https://www.freecodecamp.org/news/the-beginner-bug-squashing-guide/codepen.io) pour recréer votre problème et le partager avec les gens.

### Pratiquez, pratiquez, pratiquez

Tout comme Rome ne s'est pas construite en un jour (enfin, pour ce que j'en sais), vous ne deviendrez pas le roi de l'écrasement de bugs du jour au lendemain. Au fur et à mesure que votre carrière avance et que votre expérience grandit, vous serez armé d'une richesse de connaissances qui vous aide à résoudre les bugs et les problèmes plus rapidement. Je me surprends régulièrement à dire "ah, j'ai déjà résolu cela" ou "oh oui, j'ai un lien StackOverflow qui m'aide ici" et tout devient beaucoup plus facile. Alors continuez à pratiquer, et cette compétence se développera naturellement.

Merci d'avoir lu ! Si vous avez aimé cet article, [pourquoi ne pas vous abonner à ma newsletter](https://subscribe.chrisblakely.dev/) ?

Chaque semaine, j'envoie une **liste de 10 choses** que je pense valoir la peine d'être partagées - mes derniers articles, tutoriels, conseils et liens intéressants pour les développeurs en herbe comme vous. Je donne également des trucs gratuits de temps en temps :)