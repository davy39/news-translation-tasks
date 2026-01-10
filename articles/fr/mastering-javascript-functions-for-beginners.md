---
title: Maîtriser les fonctions JavaScript pour les débutants
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-08-09T16:40:40.000Z'
originalURL: https://freecodecamp.org/news/mastering-javascript-functions-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/functions.png
tags:
- name: JavaScript
  slug: javascript
- name: youtube
  slug: youtube
seo_title: Maîtriser les fonctions JavaScript pour les débutants
seo_desc: 'Are you new to the world of programming? Are you eager to unlock the potential
  of JavaScript to create more readable and maintainable code? If so, we have an excellent
  course for you.

  We just posted a course on the freeCodeCamp.org YouTube channel th...'
---

Êtes-vous nouveau dans le monde de la programmation ? Êtes-vous impatient de libérer le potentiel de JavaScript pour créer un code plus lisible et maintenable ? Si c'est le cas, nous avons un excellent cours pour vous.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra tout ce que vous devez savoir sur les fonctions en JavaScript. Tapas Adhikary a développé ce cours. Tapas a plus de 18 ans d'expérience en codage et a une passion pour l'enseignement et la création de communautés open source.

Les fonctions sont la pierre angulaire de la programmation. Elles vous permettent d'encapsuler des blocs de code en modules réutilisables, rendant votre code plus organisé, lisible et maintenable. Dans ce cours, vous acquerrez une base solide dans la compréhension, la création et la mise en œuvre des fonctions en JavaScript.

Le cours couvre les sujets suivants :

* Qu'est-ce que les fonctions JavaScript et pourquoi les utiliser
* Clarification des terminologies (fonction vs méthodes, paramètre vs arguments, et plus encore !)
* Déclarations de fonctions
* Exécutions de fonctions
* Paramètre par défaut
* Paramètre rest
* Pile d'appels
* Fonction fléchée
* Fonction imbriquée
* Portée des fonctions
* Fermeture
* Fonction de rappel
* Fonction d'ordre supérieur
* Fonction pure
* IIFE
* Récursivité

Que vous soyez un développeur en herbe, un étudiant faisant ses premiers pas en codage, ou même un programmeur expérimenté cherchant à rafraîchir vos connaissances de base, ce cours est créé pour répondre à vos besoins d'apprentissage.

Vous pouvez regarder le cours complet [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/j1laALb8OVM) (1,5 heure de visionnage).

%[https://youtu.be/j1laALb8OVM]

### Transcription

Dans ce cours, vous apprendrez tout sur les fonctions JavaScript.

En tant que l'un des piliers fondamentaux de la programmation, comprendre les fonctions est crucial pour chaque développeur en herbe.

Ce cours vous fournira un aperçu complet des fonctions et de JavaScript, en décomposant des concepts complexes en modules digestes, des bases de ce que sont les fonctions et pourquoi elles sont indispensables à une plongée profonde dans les terminologies, les portées, les fermetures et les motifs avancés comme les fonctions d'ordre supérieur et la récursivité.

Cette vidéo vous aidera à devenir un expert des fonctions.

Tapas a plus de 18 ans d'expérience en codage et a une passion pour l'enseignement et la création de communautés open source.

Il est l'enseignant de ce cours.

Alors, commençons.

Bonjour, les amis.

Comment allez-vous ? De quoi parle ce cours intensif ? Le cours intensif porte sur les fonctions JavaScript.

Nous allons donc passer en revue de nombreux détails sur les fonctions JavaScript et essayer de comprendre avec beaucoup de code comment cela fonctionne fondamentalement.

Une chose que je ne cesse de dire, c'est que le concept est beaucoup, beaucoup plus grand que les syntaxes. Bien que nous allons écrire du code, nous voulons d'abord approfondir le concept, puis le compléter avec les syntaxes.

J'espère que vous apprécierez ce cours entier.

Et si c'est le cas, n'oubliez pas de liker et de partager cette vidéo.

Si vous avez des doutes, commentez ci-dessous.

Je vais vous répondre à tous vos doutes et clarifications, soyez-en assurés.

D'accord, donc quelques choses avant de commencer, comment suivre ce cours.

C'est une vidéo plus longue car, bien sûr, c'est un cours intensif, nous devons inclure beaucoup de choses dans une seule vidéo.

Mais si vous suivez certains schémas, vous allez apprécier tout le voyage de passer en revue chaque sujet que nous discutons dans cette vidéo.

D'accord, donc première chose, prenez des pauses, n'essayez pas de consommer tout le contenu d'un coup, prenez des pauses adéquates, puis essayez de vous rappeler ce que vous avez appris il y a quelques secondes.

Deuxième chose, après chaque chapitre logique dans ce cours, essayez de comprendre si vous avez complètement saisi le concept ou non.

Si ce n'est pas le cas, revenez en arrière et essayez de réapprendre.

Aucun problème, à tout moment, revenez et essayez de réapprendre.

Je vais enseigner beaucoup d'exercices.

Donc, vous devez faire ces exercices avec moi, mais ne les tapez pas comme je les enseigne.

D'accord, d'abord, essayez de comprendre ce que j'enseigne, essayez de bien l'assimiler.

Et après cela, mettez la vidéo en pause, essayez de faire cela, vous savez, ces parties citées, par vous-même.

Tous les exemples de code sont déjà sur GitHub.

Et le lien est dans la section des commentaires ou la section de description de cette vidéo, vous pouvez le consulter à tout moment et essayer de voir à quoi ressemble le code. Donc, pas de soucis à ce sujet.

Mais ne tapez pas le code comme je l'enseigne, car alors vous ne vous concentrerez pas sur ce que j'enseigne, concentrez-vous plutôt sur l'apprentissage, puis essayez le code.

Donc, allez, répétez, revenez, apprenez et tout.

Et au cas où quelque chose n'est pas clair, n'hésitez pas à commenter.

Je vais vous répondre.

Alors, sans plus tarder, commençons.

Parlons rapidement des concepts que nous allons couvrir dans ce cours intensif.

Donc, la première chose dont nous allons parler, ce sont les fondamentaux des fonctions JavaScript, qu'est-ce qu'une fonction, à quoi sert-elle, à un niveau très, très basique, n'est-ce pas ? Je considère un débutant lorsqu'il regarde ce cours intensif, il sera capable de comprendre ce que sont les fonctions et pourquoi elles sont utilisées.

Ensuite, nous allons clarifier quelques terminologies, il y a quelques terminologies qui sont un peu déroutantes lorsque vous apprenez les fonctions, par exemple, fonctions versus méthodes, paramètres versus arguments, et il y a beaucoup d'autres terminologies que nous voulons clarifier.

Ensuite, nous voulons parler des déclarations de fonctions, nous allons parler des exécutions de fonctions, puis nous aborderons la pile d'appels, nous parlerons des fonctions fléchées, des fonctions imbriquées, de la portée des fonctions, nous parlerons des fermetures, nous parlerons des fonctions de rappel, des fonctions d'ordre supérieur, des fonctions pures, nous parlerons des IIFE, nous parlerons de la récursivité.

Il y a donc beaucoup, beaucoup, beaucoup à apprendre, il y a beaucoup à dire.

C'est pourquoi je vous ai dit que lorsque nous passerons à chaque chapitre de ce cours, essayez de comprendre un chapitre avant de passer au suivant, et pratiquez le chapitre avant de passer au suivant.

D'accord, donc prenez votre temps et commençons l'apprentissage.

La première chose sur les fonctions JavaScript et leurs fondamentaux.

Donc, qu'est-ce qu'une fonction JavaScript ? Avant d'en arriver là, laissez-moi vous raconter une histoire.

C'est l'histoire de deux amies.

L'une des amies essaie de cuisiner un plat, mais elle ne connaît pas la recette pour le cuisiner.

Donc, elle a appelé son amie qui est à l'étranger par téléphone, pour demander la recette.

L'amie à l'autre bout du fil a reçu l'appel et a donné la recette ligne par ligne en disant que, hé, si vous voulez cuisiner ce plat, vous devez suivre cette recette, comme vous devez mettre ceci en premier, puis vous devez mettre celui-ci, puis vous devez le cuisiner pendant si longtemps.

Et enfin, votre plat est prêt.

Super.

L'amie a cuisiné le plat en suivant la recette qu'elle avait reçue.

Mais après une semaine, lorsqu'elle a essayé de le cuisiner à nouveau, elle s'est dit, bon, laissez-moi rappeler mon amie et essayer de demander la recette.

Et la même chose s'est produite.

L'amie a donné la recette par téléphone.

Elle a suivi les instructions, cuisiné le plat préféré.

Le mois suivant, l'histoire reste la même.

Elle rappelle son amie, obtient à nouveau la recette, cuisine le plat pendant quelques mois.

Cela a continué comme ça.

Mais après cela, même si elles sont très bonnes amies, l'amie qui est à l'étranger a vraiment été frustrée et a simplement dit, hé, je te donne cette recette depuis quatre ou cinq mois maintenant.

Pourquoi ne pas l'écrire quelque part pour que tu n'aies pas à me le demander encore et encore.

Et je n'aurai pas à effectuer cette tâche de te le dire encore et encore.

Plutôt, où que tu l'écrives, tu pourras probablement la récupérer de là.

Les fonctions JavaScript sont un peu comme ça.

Cela vous évite de répéter la même tâche encore et encore.

Plutôt, vous placez la tâche quelque part, et ensuite vous réutilisez cela chaque fois que vous devez effectuer la même chose.

De manière similaire à l'histoire de l'amie, qui voulait cuisiner le plat, mais finalement, au lieu de donner la tâche à son amie de le dire encore et encore de manière répétée, elle l'a récupéré du journal, l'amie n'a plus jamais eu à effectuer la tâche.

D'accord, donc avec cette analogie en tête, comme réduire la tâche, effectuer la tâche encore et encore, plutôt, nous allons créer quelque chose afin que nous puissions réellement le réutiliser chaque fois que nécessaire dans notre programmation.

C'est l'aspect très, très fondamental des fonctions.

Maintenant, vous allez obtenir une représentation graphique à travers laquelle le même genre d'histoire sera mise en code de manière visuelle et essayer de comprendre ce que fait exactement la fonction en programmation.

La boîte jaune que vous voyez à l'écran, considérez que c'est un programme.

Et dans celui-ci, vous avez un ensemble de lignes de code.

Maintenant, regardez-le un peu plus attentivement, il y a un codage couleur, il y a un ensemble de lignes noires, puis il y a une ligne verte, à nouveau, un ensemble de lignes noires, puis il y a une ligne rouge, orange, bleue, à nouveau, un ensemble de lignes noires, et puis il y a une ligne blanche, n'est-ce pas ? Donc ce que j'essaie de dire ici, ces lignes noires sont le genre de code, le même code a été répété plusieurs fois.

Donc trois lignes noires, puis un autre code, puis à nouveau, les mêmes trois lignes noires ont été répétées, puis un autre code, puis à nouveau, les mêmes trois lignes noires ont été répétées comme ça, n'est-ce pas ? Donc il y a une répétition qui existe.

Maintenant, nous voulons introduire le concept des fonctions JavaScript ici, afin que nous puissions réduire cette répétition.

Donc ce que nous faisons essentiellement dans ce cas, vous savez, en allant de l'avant, c'est que nous marquons d'abord quelles sont ces lignes qui se répètent.

Donc vous voyez ici, nous avons marqué ces lignes qui se répètent.

Et la prochaine chose que nous faisons, c'est comme, comment pouvons-nous rendre ce code meilleur, afin que nous ne répétions pas la même tâche, n'est-ce pas, les mêmes lignes, plutôt que cela, nous prenons ces lignes quelque part, leur donnons un nom, dans ce cas, un nom est comme si vous et fun.

Et ensuite, ce que nous faisons, c'est comme le même code que nous avons obtenu, le changer de telle manière qu'au lieu de ces lignes, nous allons utiliser la même entité, celle que nous avons créée avant.

Donc voyez-vous cela, le nombre de lignes de code a considérablement diminué.

Donc ce que nous avons fait, au lieu de répéter la même tâche dans votre code, la première, nous avons maintenant mis le code dans quelque chose que nous appelons une fonction, lui avons donné un nom, appelez-le si vous et fun, et ensuite utilisez ce si vous et fun dans notre code, au lieu de répéter ces lignes à chaque fois.

Donc nous ne réduisons pas seulement le nombre de lignes de code dans, vous savez, dans notre code source total, mais ce que nous faisons aussi, c'est que nous réutilisons quelque chose encore et encore.

Maintenant, réfléchissez au cas, comme pourquoi, pourquoi en avons-nous besoin, le meilleur cas probablement est, disons qu'il y a un problème dans ces trois lignes, il y a un bug dans ces trois lignes.

Donc dans le cas précédent, s'il y a un bug, et que vous devez corriger ce bug, ou que vous devez corriger ce problème, vous devez corriger ce problème au moins trois fois.

Donc vous devez le corriger dans le premier ensemble de lignes, puis à nouveau, le deuxième ensemble de lignes, puis à nouveau, le troisième ensemble de lignes.

Mais comme nous avons mis cette chose dans une fonction en un seul endroit, et ensuite réutilisé la même avec son nom dans les différents endroits multiples, si vous devez corriger le bug maintenant, vous devez le corriger en un seul endroit, juste à l'intérieur du corps de cette fonction, juste à l'intérieur de cette fonction, et ensuite le reste fonctionnera.

Donc les fonctions sont un ensemble de blocs que vous gardez ensemble pour effectuer quelque chose qui sinon serait très, très répété dans votre code. Une fonction devrait idéalement avoir un nom, mais elle peut aussi être sans nom, dans la plupart des cas, vous aurez une fonction avec un nom, afin que vous puissiez appeler la fonction avec ce nom.

Donc vous et moi, chaque être humain a un nom.

Et le but du nom est comme, nous serons appelés par ce nom.

Et quand quelqu'un nous appellera par ce nom, nous répondrons et dirons, hé, je suis ici.

Je suis la personne.

De même, pour la fonction, quand nous appelons la fonction par le nom, la fonction dira comme, hé, je suis ici.

Et à l'intérieur de cela, j'ai ce groupe de code, allez-y et exécutez ce code.

D'accord, donc c'est la beauté de la fonction JavaScript.

J'espère que vous l'avez compris.

Je sais que cette infographie et s'il vous plaît gardez-la dans votre cerveau.

Parce que, vous savez, le reste du cours intensif, nous allons utiliser cette terminologie encore et encore, vous savez, pour une meilleure compréhension en programmation, parfois, les terminologies sont beaucoup plus difficiles que la programmation elle-même.

Et quand un développeur se bloque sur ces terminologies, ils se sentent si découragés d'apprendre ce langage de programmation particulier, cela arrive.

C'est pourquoi, lorsque nous apprenons un langage de programmation ou un aspect d'un langage de programmation, nous devons nous assurer que nous comprenons certaines terminologies très bien.

Lorsque vous apprenez les fonctions JavaScript, il y a quelques terminologies que vous devez également connaître, et vous devez bien différencier entre elles.

Donc certaines des terminologies sont les fonctions et les méthodes, quelles sont les différences, nous allons en parler, puis les déclarations et les définitions, quelle est la différence, y a-t-il une différence entre elles, les arguments et les paramètres, nous allons en parler aussi.

Et puis les fonctions de rappel et les fonctions d'ordre supérieur, vous serez souvent confus avec ces deux, nous allons en parler aussi en profondeur lorsque vous irez dans le cours lui-même.

Donc ces terminologies, gardez-les à l'esprit, comme lorsque nous en parlons, assurez-vous que dans votre tête, ces terminologies et les différences ou les similitudes sont complètement tracées, complètement clarifiées.

Si ce n'est pas le cas, revenez en arrière et essayez de voir où je l'ai expliqué.

Si vous avez encore des questions, posez-les dans votre section de commentaires, je vous répondrai.

Commençons maintenant à créer des fonctions et essayons d'apprendre comment créer des fonctions.

D'accord, je pense qu'avant cela, vous pouvez utiliser n'importe quel éditeur comme Visual Studio Code ou un autre éditeur de votre choix lors du codage.

Ce que j'utilise maintenant, j'utilise les outils de développement du navigateur et l'onglet console, afin que je puisse écrire le programme ici et les exécuter là.

Si vous voulez un autre mécanisme comme écrire sur Visual Studio Code et utiliser le serveur live pour exécuter votre programme, bienvenue, ou vous pouvez les pratiquer sur les outils de développement du navigateur.

Il suffit d'appuyer sur F12, d'ouvrir les outils de développement, d'aller dans l'onglet console et de commencer à écrire votre programme et de l'exécuter car vous pratiquez simplement à ce moment-là.

Donc, première chose à faire, ce que nous allons faire maintenant, c'est créer une fonction.

Nous avons dit qu'une fonction est quelque chose qui va vous aider à garder un ensemble d'instructions et de code dans un endroit afin que vous puissiez le réutiliser encore et encore lorsque vous en avez besoin.

Maintenant, pour déclarer ou définir une fonction.

Donc notre première terminologie, bang, déclaration versus définition.

Donc ces deux choses sont exactement les mêmes lorsqu'il s'agit de fonction.

Déclaration de fonction, définitions de fonction, définir une fonction est un peu la même chose.

Si quelqu'un dit que je déclare une fonction ou une autre personne dit que je définis une fonction, ils parlent en fait de la même chose, qui n'est rien d'autre que la création d'une fonction avec une logique.

Donc ce que nous allons faire maintenant, c'est d'abord créer une fonction.

Pour ce faire, je dois utiliser un mot-clé appelé fonction.

C'est le mot-clé, puis je dois donner un nom à la fonction.

Je viens de dire que la fonction peut ou non avoir un nom, mais la plupart du temps la fonction aura un nom afin que nous puissions appeler la fonction par son nom, comme un être humain a un nom.

Il y a des situations où la fonction peut ne pas avoir de nom et nous en parlerons dans le cours.

D'accord, donc donnons d'abord un nom.

Donnons un nom appelé print me et puis donnez, vous savez, des accolades et puis fermez ces accolades.

Donc c'est ce que vous avez déclaré ou défini une fonction.

D'accord, donc maintenant la fonction a un mot-clé, un nom, un ensemble de parenthèses, puis des accolades ouvertes et fermées.

À l'intérieur de ces accolades, vous allez écrire toute la logique que vous voulez que cette fonction ait afin que vous puissiez réutiliser cette logique où vous voulez.

Par exemple, cette fonction particulière peut simplement journaliser certaines choses dans cette console.

Donc vous faites console dot log console dot log console est comme un, vous savez, quelque chose que vous avez déjà avec JavaScript sur ce débogueur particulier afin que vous puissiez l'utiliser à des fins de codage pour vos besoins de débogage.

Et sur la console, vous avez des variétés de méthodes.

L'une des méthodes est log à travers laquelle vous pouvez journaliser quelque chose dans la console afin que vous sachiez que vous pouvez réellement les lire ou c'est plus pour le débogage que vous pouvez utiliser.

D'accord, donc faisons quelque chose comme imprimer quelque chose comme ceci.

D'accord, donc j'ai créé une fonction avec un mot-clé de fonction et le nom appelé print me et l'instruction que la fonction a est un log que je veux imprimer dans la console et ce log dit printing.

C'est tout.

Donc c'est ma définition de fonction ou déclaration de fonction.

Maintenant, comme je l'ai déclarée cette fonction avec un nom, la prochaine chose que je peux faire magnifiquement est d'appeler cette fonction.

Donc pour appeler cette fonction, tapez simplement le nom de la fonction, vous savez, print me ici, il y a déjà une complétion automatique.

Et puis pour l'appeler, vous devez donner cette parenthèse.

Sinon, vous imprimez simplement le nom de cette fonction particulière.

Et si vous faites simplement cela, la fonction va imprimer son corps complet lui-même.

Donc si vous faites simplement print me le nom lui-même, il va vous donner une version chaîne de la définition ou déclaration entière de la fonction que vous avez faite il y a un instant.

Mais pour l'exécuter pour l'appeler spécifiquement, vous devez donner cette parenthèse, vous devez donner cette parenthèse, et puis vous appuyez sur entrer, il donnera sa sortie.

C'est juste log printing, parce que c'est exactement ce que nous avons demandé à cette fonction particulière de faire.

Donc notre fonction a fonctionné.

C'est super.

Maintenant, comme la fonction a fonctionné, je veux juste faire quelque chose de plus avec cela.

D'accord, donc c'est là que je vais introduire quelque chose appelé paramètre.

D'accord, donc écrivons la même fonction fonction.

Et nous dirons que le nom est print this.

Et nous allons passer quelque chose ici, que nous appelons paramètre, je vais y venir dans une minute.

Et puis je vais fermer le corps de cette fonction.

Et à l'intérieur de cela, ce que je vais faire, je vais écrire comme console dot log, param.

Donc qu'est-ce que c'est ? Que signifie-t-il ? Qu'est-ce que j'ai fait ici ? D'accord, donc j'ai d'abord créé une fonction de manière similaire avec le mot-clé fonction et le nom de la fonction.

Ici, je n'ai rien fait entre ces deux parenthèses.

Mais dans ce cas, j'ai fait quelque chose dans la parenthèse.

Donc tout ce que vous mettez à l'intérieur de cette parenthèse d'une fonction, c'est ce qu'on appelle des paramètres.

D'accord, tout ce que vous mettez à l'intérieur de cette parenthèse s'appelle des paramètres, vous pouvez mettre autant de paramètres que vous le souhaitez, tant que vous en avez besoin dans votre logique de programmation.

Donc si je passe param, c'est juste, vous savez, je peux utiliser ce param n'importe où à l'intérieur de cette fonction, afin que je puisse faire quelque chose avec.

Donc par exemple, je peux simplement faire print this et passer cela va imprimer la chose que je viens de donner ici.

Donc cela signifie que je peux passer une valeur à une fonction, et que cette valeur est en fait mappée au paramètre.

Et c'est quelque chose que je peux utiliser, vous savez, à l'intérieur de la fonction pour faire tout ce que nous voulons.

Donc encore une fois, il y a une chose que je veux souligner ici, il y a une logique de terminal, un paramètre versus un argument, tout ce qui est dans la définition de la fonction que vous passez à l'intérieur de cette parenthèse est un paramètre.

Mais lorsque vous appelez cette fonction, invoquez cette fonction, la valeur réelle que vous passez à cette fonction est appelée argument.

D'accord, donc c'est la différence.

Parfois, ce qui s'est passé, c'est que nous appelons cela aussi un paramètre que je passe le paramètre, nous appelons cela un argument que je passe l'argument, ce n'est pas le cas.

Donc le paramètre est quelque chose que vous passez à une fonction lors de la déclaration ou de la définition de la fonction, qui est comme ceci.

Mais lorsque vous appelez ou invoquez cette fonction, la valeur réelle que vous lui passez, c'est ce qu'on appelle les arguments.

Donc j'espère que cela est clair pour vous le paramètre versus l'argument.

D'accord, super.

Donc nous avons défini la fonction.

Et nous savons maintenant ce qu'est un paramètre, nous savons maintenant ce qu'est exactement, vous savez, un argument et des choses comme ça.

D'accord, donc la prochaine chose, nous avons défini la fonction, mais il y a une autre façon dont nous pouvons réellement déclarer ou définir la fonction.

C'est ce qu'on appelle l'utilisation des expressions de fonction.

D'accord, donc qu'est-ce qu'une expression, apprenons.

Mais avant cela, laissez-moi simplement clarifier tout cela que j'ai fait, parce que je n'en ai pas besoin.

Donc si je dis const count equals 200, c'est une expression, ce que cette expression a, elle a un nom de variable appelé count.

Elle a comme, vous savez, comment nous avons défini cette variable, nous disons que cette variable est une constante, et puis est une valeur de cette variable particulière.

D'accord, donc const count equals 200 est une expression.

Exactement.

De même, nous pouvons réellement définir une fonction.

Donc prenons la fonction print me elle-même.

Donc dans la fonction print me, le print me n'est rien d'autre que le nom de la fonction, que nous pouvons réellement mettre comme une variable ici.

Et puis ce que nous pouvons faire ici, au lieu de cette valeur 100, nous pouvons donner la fonction elle-même est une valeur.

Et puis nous donnons le corps de la fonction.

Et à l'intérieur de ce corps de fonction, nous pouvons donner ce dont nous avons besoin.

Désolé, cela s'est exécuté, c'est de ma faute, je vais juste le mettre ici.

Vous pouvez donner console dot log, ils impriment, n'est-ce pas.

Donc c'est ce que j'ai fait.

Donc j'ai const print me equals to function et puis cette chose.

Auparavant, ce que j'ai fait, j'ai fait cette fonction, print me.

D'accord, et puis j'ai fait ici console dot log, disons, impression.

Donc maintenant, j'ai simplement défini la fonction, mais j'ai défini la fonction de la manière de l'expression de fonction.

Donc cela signifie que le nom que j'ai utilisé pour la fonction auparavant, maintenant c'est une variable en fait.

Et puis la variable que j'ai assignée n'est rien d'autre qu'une fonction, j'ai assigné cela comme une fonction.

Donc cela signifie que print me n'est rien d'autre qu'une fonction.

Maintenant, si j'ai fait const print me equals to 100, print me n'est rien d'autre qu'un nombre, dont la valeur est 100.

Maintenant, j'ai fait const print me equals to function, cela signifie que print me est une fonction.

Et puis je devrais être capable d'exécuter cette fonction.

Donc d'abord, je vais la définir, d'accord, print me est déjà déclaré, parce que j'ai utilisé cela, utilisons un autre nom pour l'instant, disons print me again.

D'accord, donc c'est le nom, et puis je fais print me again.

Et je dois m'exécuter, donc je dois faire cette parenthèse, et j'ai obtenu l'impression.

Donc c'est une autre façon dont je peux réellement définir et déclarer une fonction, n'est-ce pas.

Maintenant, dans la même chose dans print me again, disons print me again, et disons avec param, ce que je peux faire maintenant, je peux réellement mettre n'importe quel paramètre ici, n'est-ce pas, ou cette fois je vais mettre deux paramètres a et b.

Et ici après être venu, je vais en fait faire a et b.

J'ai fait maintenant déclaré cela.

Maintenant, disons print me again avec param, si je fais 10 et 20 comme argument, cela va imprimer 10 10 10 et 20.

Donc j'espère que c'est clair.

Et maintenant, vous savez comment nous pouvons réellement définir une fonction ou déclarer une fonction.

Il y a deux façons que nous avons faites.

D'accord, donc l'une est avec expression et l'autre est sans expression.

Apprenons comment retourner d'une fonction.

Donc return est quelque chose que vous allez utiliser très souvent lorsque vous travaillez avec des fonctions.

Jusqu'à présent, ce que nous avons fait, nous avons créé une fonction, mais à l'intérieur de celle-ci, nous avons simplement fait une instruction console dot lock, ce qui n'est pas suffisant.

Habituellement, ce qui se passe, c'est que lorsque vous créez une fonction, disons fonction x, et vous avez quelque chose ici, n'est-ce pas.

Et puis vous aurez disons une autre fonction, y.

D'accord, et vous avez quelque chose ici.

Et puis chacune de ces fonctions est censée faire sa propre tâche, n'est-ce pas.

Et dans tout le programme, notre application entière n'est pas comme cela, vous aurez seulement une fonction, vous aurez plusieurs fonctions.

Et ce que nous allons faire, c'est que, si la fonction x, ce qu'elle est censée faire, ce que vous pouvez utiliser, c'est essentiellement que vous pouvez l'utiliser comme la valeur de sortie de la fonction x, et prendre cela dans une variable comme disons let p equals to this, et essentiellement pouvez utiliser ce p quelque part à l'intérieur d'une autre fonction ou n'importe où ailleurs dans cette matière.

Donc essentiellement, quelle que soit la valeur de cette fonction x qui retourne, vous pouvez utiliser cette valeur n'importe où ailleurs, peut-être dans une autre fonction ou n'importe où dans votre programmation, n'est-ce pas.

Donc pour que cela se produise, si vous voyez cette expression, laissez-moi supprimer tout ici.

Et juste pour le mettre à votre disposition, cette expression particulière, ce que nous faisons, nous avons une variable appelée p.

Et la valeur de p est ce qui n'est pas la fonction, mais la valeur que nous obtenons de l'exécution d'une fonction, parce que nous avons dit qu'un nom de fonction avec une parenthèse signifie l'exécution, l'appel, l'invocation d'une fonction, un nom de fonction sans parenthèse signifie simplement la représentation en chaîne de la définition de la fonction elle-même.

C'est une différence que vous devez garder à l'esprit.

Donc dans ce cas, nous avons une parenthèse signifie que la fonction sera exécutée, la fonction sera appelée ou la fonction sera invoquée.

Et à l'intérieur de cela, si la fonction retourne une valeur, si la fonction retourne une valeur, cette valeur sera assignée à cette variable.

Que se passe-t-il si la fonction ne retourne aucune valeur ? Que se passe-t-il si elle a simplement une console.log comme nous l'avons vu dans la fonction jusqu'à présent, dans ce cas, simplement l'exécution de la fonction retournera quelque chose de très spécial, qui est appelé indéfini.

D'accord, cela signifie que quelque chose qui n'est pas encore défini est quelque chose appelé indéfini.

D'accord, donc maintenant, créons une fonction qui retourne quelque chose.

Pour cela, nous allons créer une fonction, disons sum, et nous allons faire une somme d'addition de deux choses.

Donc nous allons prendre a et b comme deux paramètres, la terminologie compte.

Et ce que nous allons faire, c'est comme nous allons faire le retour de a plus b, simple, ce qui signifie que c'est une fonction dont le nom est sum prend deux paramètres a et b, elle additionne ces deux paramètres avec cette opération arithmétique, et le résultat qu'elle retourne, vous savez, en arrière.

Donc exécutons sum, elle prend deux arguments.

Maintenant, mettons deux et trois.

Cela signifie que nous attendons un cinq, elle retourne un cinq.

La même méthode, nous pouvons en fait écrire un peu différemment comment écrivons la même méthode fonction, sum, nous allons faire à nouveau a virgule b.

Et dans ce cas, nous avons simplement fait le retour de a plus b, au lieu de cela, parfois, vous pourriez vouloir faire cela aussi, comme let return une variable a plus b, et puis retourner cette variable particulière elle-même.

C'est aussi la même chose, comme vous le savez, nous avons fait ce que nous avons fait avant comme retourner a plus b directement, n'est-ce pas.

Donc si c'est juste un simple calcul, le retourner directement lui-même sera une quantité plus courte de code que les gens font.

Donc s'il vous plaît suivez cela.

C'est à propos de retourner de retourner d'une fonction, cela signifie tout ce que vous faites à l'intérieur d'une fonction, toutes les tâches, toute la logique, toutes les opérations, et à la fin de cela, si vous voulez que la fonction retourne une valeur, afin que cette valeur puisse être utilisée ailleurs, vous devez utiliser une instruction return, suivie de ce que vous voulez retourner.

J'espère que c'est clair.

Qu'est-ce qu'un paramètre par défaut ? Lorsque vous définissez une fonction, nous savons comment définir une fonction.

Donc définissons une fonction, fonction prendra la même chose.

D'accord, une fonction un peu différente, disons calc est une fonction, et elle prend deux paramètres a et b.

Et ce que nous faisons, nous allons retourner une valeur et la valeur que nous voulons retourner est quelque chose comme deux fois a plus b.

D'accord, c'est la valeur que nous prévoyons de retourner.

Donc ce que fait cette fonction, une fonction simple, une fonction dont le nom est calc, prend deux paramètres a et b, ce qu'elle retourne est la somme de ces deux valeurs de paramètres, puis la multiplie par deux, et retourne une valeur.

Donc exécutons cela, appelons cette fonction avec deux virgules trois.

D'accord, donc ce qu'elle vous donne, elle vous donne 10.

Oui, bien sûr, parce que deux plus trois est cinq, cinq fois deux est 10.

De même, vous pouvez faire trois fois trois, ce qui va vous donner 12, trois plus trois est six fois deux est 12.

Maintenant, disons que quelqu'un dans l'équipe a oublié de passer ce deuxième argument, ce que vous obtenez, vous obtenez un nombre non valide.

Pourquoi obtenez-vous un nombre non valide ? Parce que lorsque vous ne passez pas d'argument pour un paramètre pour la fonction, la valeur du paramètre sera indéfinie.

Nous en avons parlé.

Donc cela signifie que dans ce cas, vous ne passez pas le deuxième argument.

Donc la valeur de base, donc alors b sera indéfini.

Maintenant, a plus indéfini sur a sera trois, b est indéfini, trois plus indéfini n'est pas un nombre, bien sûr, il retourne non un nombre.

Maintenant, dans une situation comme celle-ci, au lieu d'obtenir un nombre non valide, vous pourriez vouloir le protéger avec une sorte de valeur par défaut, n'est-ce pas, une sorte de valeur par défaut de ces paramètres, afin qu'au moins cette défaillance comme celle-ci, plutôt, vous pouvez les protéger avec certaines valeurs que vous aimez.

D'accord, donc ce que nous allons faire, c'est la même fonction, je vais la ramener.

Et maintenant, je peux en fait la définir par défaut à zéro.

D'accord, c'est une valeur par défaut ou une valeur par défaut pour ce paramètre que je mets.

Donc cela signifie que si quelqu'un ne passe pas de valeur pour ce paramètre en utilisant l'argument, la valeur zéro sera utilisée à la place.

D'accord, donc faisons cela.

Maintenant, je vais faire Calc trois à nouveau, si vous voyez cela maintenant au lieu de non n, non un nombre, il retourne en fait une valeur qui est six, ce qui est faisons le calcul a est trois b est zéro trois plus zéro est trois trois fois deux est six.

D'accord, donc vous pouvez faire une valeur de paramètre par défaut pour votre fonction si nécessaire.

Et dans ce cas, vous pouvez la protéger d'une valeur de retour non naturelle de la fonction comme non un nombre.

Et vous pouvez en fait remplacer la valeur indéfinie au lieu d'avoir indéfini, vous pouvez maintenant définir une certaine valeur avec le paramètre par défaut.

Paramètres rest.

Qu'est-ce qu'un paramètre rest ? Le paramètre rest est quelque chose qui permet à une fonction d'accepter un nombre quelconque d'arguments sous forme de tableau, un nombre quelconque d'arguments.

D'accord, maintenant la théorie est une chose, faisons-le avec un exemple, créons une fonction, disons donner un nom de fonction, nous allons donner un nom d'appel disons collect things. D'accord.

Et nous aurons deux paramètres, le premier est x et le second est y.

Maintenant, nous parlons de paramètres rest, un type spécial de paramètres, n'est-ce pas, nous connaissons les paramètres par défaut.

Maintenant, nous apprenons les paramètres rest.

Et je viens de dire que le paramètre rest permet à une fonction d'accepter un nombre infini d'arguments sous forme de tableau.

Maintenant, pour s'assurer que le paramètre rest accepte un nombre infini d'arguments, ce que nous devons faire, vous devez lui donner une syntaxe spéciale, la syntaxe est avec trois points.

Donc lorsque nous donnons trois points, ce qui se passe, c'est comme ceci, ce paramètre particulier devient un paramètre rest.

Maintenant, voici deux choses que je veux souligner : une définition de fonction ne peut avoir qu'un seul paramètre rest.

Donc cela signifie que vous ne pouvez pas faire x virgule paramètre rest y virgule paramètre rest z, vous ne pouvez pas faire cela.

Donc il ne peut avoir qu'un seul paramètre rest.

Et le paramètre rest doit être le dernier paramètre que vous définissez pour la fonction.

Ces deux règles, s'il vous plaît, gardez-les à l'esprit, je vais répéter à nouveau, une définition de fonction ne peut avoir qu'un seul paramètre rest comme nous l'avons ici avec y.

Le paramètre rest doit être le dernier paramètre comme nous l'avons ici.

Donc vous ne pouvez pas avoir comme vous savez, en faisant de ce x un paramètre rest et puis y comme un paramètre normal, vous ne pouvez pas avoir cela plutôt vous devez avoir comme ceci, bien sûr, le nom le suggère, cela signifie le reste, le reste signifie le reste, le reste signifie ce qui reste.

Donc c'est là qu'il va à la fin.

D'accord, maintenant ce que je vais faire, je vais faire un console dot log de x.

Et puis je vais faire un console dot log de y, afin que je puisse réellement imprimer et voir ce qu'il imprime exactement.

Maintenant, j'ai défini, faisons simplement collect things, désolé, faisons simplement collect things, et puis passons quelques arguments, n'importe quel nombre 5, 6, 7, 8, 9, d'accord, 9 suffit.

Maintenant, ce que je vais faire, je vais appeler collect things avec neuf arguments, je peux en passer 100, 1000, des millions si j'ai le temps.

D'accord, donc testons-le avec 9.

Donc ce qui va se passer, le premier argument qui est mappé au premier paramètre, donc la valeur x sera 1, et le reste de 2 à 9 va au paramètre rest.

Donc cela signifie que y va maintenant accepter de 2 à 9, mais dans un tableau.

D'accord, donc si je l'imprime simplement, donc si vous voyez, le premier imprime x est 1, et le reste des 8 va à l'intérieur d'un tableau de 2 à 9, ce sous-script est une notation de tableau de 2 à 9, et puis cet ensemble entier est assigné, ce tableau entier est assigné à ce paramètre y, c'est pourquoi il est appelé paramètre rest.

J'espère que c'était à nouveau facile pour vous de comprendre, et vous allez essayer de pratiquer beaucoup le paramètre rest.

Apprenons la fonction fléchée ou la syntaxe de la flèche grasse.

D'accord, donc nous savons comment définir une fonction, n'est-ce pas ? Faisons-le à nouveau.

Mais cette fois, répétons celle que nous avons faite avec l'expression de fonction, const add equals to a function.

Et puis nous avons deux paramètres ici.

Et puis nous avons return de x plus y.

Et enfin, nous fermons cette parenthèse particulière.

Cela fonctionne, c'est super, n'est-ce pas ? Maintenant, ce que nous pouvons faire ici pour convertir celle-ci en une fonction fléchée ou une syntaxe de flèche grasse, c'est quelques ajustements que vous devez faire.

Au début, la fonction fléchée ou la syntaxe de la flèche grasse semble un peu étrange.

Mais comment j'ai essayé de m'en souvenir en l'écrivant.

Et maintenant, ce qui s'est passé, c'est que je n'écris presque jamais une fonction de la manière traditionnelle de déclaration ou de définition, il s'agit toujours d'écrire la fonction avec la syntaxe de la flèche grasse ou la syntaxe de la flèche.

D'accord, donc convertissons-la, si vous êtes nouveau, vous mettrez un certain temps à vous y habituer.

Mais une fois que vous vous y habituez, je suis sûr que vous allez écrire la fonction fléchée encore et encore.

Parce que maintenant je vais parler de son utilisation, car les meilleurs usages, vous allez écrire moins de code, vous allez écrire une quantité moindre de code.

Et que ce soit dans n'importe quel framework ou n'importe quelle bibliothèque aujourd'hui dans le développement web moderne, je pense que le de facto, la syntaxe de codage très normale pour les fonctions est l'utilisation de la fonction fléchée.

Cela ne signifie pas que vous ne pouvez pas aller avec la manière traditionnelle de déclarer et de définir une fonction ou de déclarer différentes fonctions en utilisant des expressions comme celle que nous voyons à l'écran, vous pouvez toujours aller avec cela.

Mais si vous utilisez la fonction fléchée, ou vous utilisez la syntaxe de la flèche grasse, c'est comme, vous savez, beaucoup plus moderne, c'est beaucoup moins de code.

Et bien sûr, il y a une autre chose qui est là, que je ne couvrirai pas dans ce cours intensif, mais dans le suivant, la relation avec ce mot-clé et la fonction fléchée, les fonctions fléchées n'ont pas de liaison avec ce mot-clé, c'est ce qui est un autre cas spécial qui vient, mais cela sera couvert dans la vidéo sur ce mot-clé, la vidéo sur ce mot-clé que je vais faire ensuite.

D'accord, mais concentrons-nous maintenant sur la conversion de celle-ci en fonction fléchée.

D'accord, donc pour convertir celle-ci, ce que je dois faire, c'est simple, une chose, je vais supprimer ce mot-clé de fonction.

Donc vous n'avez pas besoin du mot-clé de fonction du tout pour faire une fonction fléchée.

Ensuite, nous parlons de sa fonction fléchée.

Donc vous avez besoin d'une flèche.

Donc la flèche est une combinaison de cette touche égale et de cette touche de flèche.

Donc si vous avez un supérieur à et l'égalité et la touche supérieure à sans aucun espace côte à côte, vous avez en fait une syntaxe de type flèche.

Et c'est ce qui fait que c'est une fonction fléchée.

Donc c'est une fonction fléchée, d'accord, const add, c'est le paramètre que nous prenons.

Et puis ce qui se passe, en fait, j'ai une flèche et puis la définition de la fonction.

C'est tout ce qu'il y a à savoir sur la fonction fléchée.

Donc je n'utilise pas le mot-clé de fonction du tout.

Donc assurons-nous simplement qu'elle fonctionne à deux virgules trois, elle fonctionne à cinq.

D'accord, très bien.

Mais une autre chose que je peux faire, si le corps de la fonction fléchée, la déclaration de la fonction fléchée, n'a qu'une seule instruction, juste une ligne et retourne quelque chose, vous n'avez même pas besoin de donner ces accolades.

Donc celle-ci vous pouvez très bien définir, comme, vous n'avez pas besoin de cela, débarrassez-vous simplement.

Et puis vous vous en débarrassez, c'est tout.

Donc cette syntaxe par rapport à celle-ci, vous savez, avec le mot-clé de fonction, celle-ci est beaucoup, beaucoup plus simple, n'est-ce pas ? Donc si vous avez une syntaxe comme celle-ci, c'est beaucoup, beaucoup plus facile pour vous.

Et si c'est quelque chose comme, vous savez, vous avez une dépendance avec juste un paramètre ici, vous n'avez pas besoin de donner cette parenthèse, vous pouvez en fait faire des choses comme ceci.

Donc si vous avez, vous savez, juste une ligne de code ici, c'est beaucoup, beaucoup plus simple.

Donc c'est la raison pour laquelle la fonction fléchée est très bien appréciée, très bien appréciée par la communauté des développeurs, elle est très bien reçue par la communauté des développeurs, car vous allez écrire très peu de syntaxe, c'est très peu de code.

Et dans tous les domaines du développement web moderne, vous savez, la fonction fléchée est très largement utilisée.

Donc s'il vous plaît, pratiquez l'écriture de la fonction fléchée.

Et j'espère que vous continuerez à écrire de plus en plus de fonctions fléchées dans votre code, plutôt que d'écrire la fonction de manière plus traditionnelle.

D'accord, donc les fonctions imbriquées, que signifie l'imbrication ? Nous savons comment créer une fonction, disons que nous créons une fonction appelée outer.

Et cette fonction a un corps.

Et elle peut avoir certaines instructions, comme à quoi sert cette fonction ? Peut-être que dans ce cas, une fonction est censée imprimer quelque chose appelé outer dans le journal.

Maintenant, JavaScript vous permet de créer une fonction pour définir une fonction à l'intérieur d'une autre fonction.

D'accord, cela peut sembler un peu étrange si vous êtes nouveau dans ce domaine.

Mais c'est une fonctionnalité très, très puissante.

Et c'est la première chose de base pour comprendre le concept de fermeture, le concept de fermeture dans les fonctions en JavaScript est égal à la compréhension des fonctions imbriquées, plus la portée des fonctions.

Donc si vous voulez comprendre la fermeture en profondeur, je veux votre attention ici d'abord comprendre ce qu'est une fonction imbriquée, comment fonctionne-t-elle ? Ensuite, nous parlerons de la portée des fonctions.

Et puis nous parlerons de la fermeture afin que tout soit très, très clair pour vous et soit très simple pour vous.

D'accord, donc les fonctions imbriquées.

Donc une fonction à l'intérieur d'une fonction, cela signifie que je peux créer une autre fonction ici, lui donner un nom, peut-être pour simplifier, je lui donne un nom inner.

Et je peux donner une console.log.

Comme je l'ai définie cette fonction en utilisant la fonction outer, cette fonction est appelée une fonction imbriquée.

Et cette fonction imbriquée, comme je l'ai définie à l'extérieur, vous savez, à l'intérieur de cette fonction outer, je dois appeler celle-ci à l'intérieur de la fonction outer elle-même.

D'accord, comme ceci.

Donc maintenant, si je l'ai définie de cette manière, et si j'appelle la fonction outer, que se passera-t-il ? La fonction outer sera invoquée, elle imprimera cette console.log, puis elle verra que cette fonction inner a été définie, la définition a eu lieu.

Et après cela, elle invoquera également la fonction inner.

Donc quel sera le résultat si je fais cela outer ici ? D'accord, donc le résultat est outer et puis inner.

Donc il imprime d'abord le log outer, puis la définition a eu lieu, inner s'exécute, et ce inner s'imprime.

Donc vous pouvez avoir une imbrication à n'importe quel niveau dans les fonctions JavaScript.

Cependant, vous ne verrez pas en pratique, vous savez, trop de niveaux d'imbrication, mais vous verrez définitivement maintenant si vous revenez et regardez le code, les différents codes JavaScript, vous verrez définitivement un certain niveau d'imbrication, un certain niveau de définition d'une fonction, une autre à l'intérieur d'une autre fonction.

Et c'est une fonctionnalité très puissante, nous allons pouvoir le voir dans un instant.

Nous venons de voir ce qu'est une fonction imbriquée.

Et maintenant nous passons à la compréhension de la portée des fonctions.

D'accord, ces deux concepts sont un peu interdépendants, car vous devez comprendre le concept de fonction imbriquée, vous pouvez définir une fonction à l'intérieur d'une autre fonction.

Et ensuite, la portée des fonctions est importante pour comprendre qui peut accéder à quoi, d'accord.

Maintenant, il y a certaines règles générales.

Mais pour comprendre ces règles, j'ai pensé qu'une image graphique serait beaucoup plus importante.

Donc s'il vous plaît, portez attention à ce graphique ici.

Donc disons qu'il y a un fichier JavaScript, vous savez, et une fonction est définie à l'intérieur.

Donc la fonction s'exécute globalement, cela signifie que la fonction n'est pas à l'intérieur d'une autre fonction.

Donc cette boîte bleue est une fonction, cette fonction particulière n'est pas à l'intérieur d'une autre fonction, d'accord, la fonction est simplement définie globalement.

Maintenant, ce qui s'est passé, il y a en fait deux règles, deux règles primaires que vous devez garder à l'esprit.

Et ces deux règles sont très importantes si vous comprenez, je veux comprendre la fermeture. D'accord.

Donc la première règle ici est que les variables définies à l'intérieur d'une fonction, les variables définies à l'intérieur d'une fonction ne peuvent pas être accessibles de n'importe où à l'extérieur de la fonction.

D'accord, donc la variable que celle-ci est définie à l'intérieur de cette fonction ne peut pas être accessible de n'importe où à l'extérieur de la fonction.

D'accord, donc tout ce qui est défini dans cette boîte bleue ne peut pas être accessible à l'extérieur de la boîte bleue.

Compris le premier principe, d'accord, des variables définies à l'intérieur d'une fonction ne peuvent pas être accessibles de n'importe où à l'extérieur de la fonction.

Deuxième principe, l'inverse de cela, une fonction peut accéder à toutes les variables à l'intérieur de la portée où elle est définie.

Une fonction peut accéder à toutes les variables à l'intérieur de la portée où elle est définie.

Donc cela signifie que cette fonction bleue peut accéder à toutes les variables définies, vous savez, dans la portée, la fonction est définie dans la portée globale.

Donc à l'intérieur de la portée globale, si je définis, j'ai une variable, je serai en mesure d'y accéder à partir de cette fonction, mais l'inverse n'est pas vrai.

De l'extérieur, vous ne pouvez pas accéder à ce qui est à l'intérieur.

Compris cette règle, répétons cette règle à nouveau car elle est très importante pour nous de comprendre la fermeture.

Les variables définies à l'intérieur d'une fonction ne peuvent pas être accessibles de n'importe où à l'extérieur de la fonction.

Première règle.

Deuxièmement, une fonction peut accéder à toutes les variables à l'intérieur de la portée où elle est définie.

Donc cette boîte bleue est définie dans la portée globale.

Dans la portée globale, s'il y a des variables, à partir de cette boîte bleue, à partir de la fonction bleue, je devrais être en mesure d'y accéder.

Super.

Maintenant, nous avons appris à propos des fonctions imbriquées, non ? Donc remplacez simplement cette portée globale par une fonction et cette fonction par une fonction imbriquée, d'accord, une fonction interne.

Donc la portée globale est la fonction externe et cette fonction est une fonction interne.

Dans ce cas également, la formule reste la même.

La règle applicable ici aussi.

Donc cela signifie que votre fonction externe ne peut pas accéder à quoi que ce soit de la fonction interne, car la fonction interne est définie dans cette fonction externe.

Donc cela signifie que la fonction interne sera en mesure d'accéder à quoi que ce soit qui est défini dans cette fonction externe, car la fonction interne est définie dans la portée de la fonction externe.

Très simple, n'est-ce pas ? Donc maintenant, si cela continue à s'imbriquer, comme s'il y a une autre fonction à l'intérieur, il y a une autre fonction à l'intérieur.

La même règle s'applique.

Nous avons la même règle appliquée là.

Donc c'est ainsi que cela fonctionne.

Donc vous devez garder cela à l'esprit.

Maintenant, nous allons voir avec un exemple de code ici, d'accord.

Nous allons voir un exemple de code ici.

Mais vous devez vraiment vous souvenir de cette règle qu'une variable définie à l'intérieur d'une fonction ne peut pas être accessible de n'importe où à l'extérieur de la fonction, vous savez, de l'extérieur de la fonction.

Une fonction peut accéder à toutes les variables à l'intérieur de la portée où elle est définie.

Donc ces flèches et ces choses, si vous les gardez à l'esprit, je pense que les choses seront très claires.

D'accord, donc passons à autre chose et essayons de voir comment les choses fonctionnent en termes de code, nous allons faire un peu de codage maintenant.

Donc, en fonction des règles que nous avons apprises jusqu'à présent, nous allons écrire le code afin que nous comprenions clairement cette chose, n'est-ce pas ? Créons une fonction, créons une fonction appelée a do something. D'accord.

Et qu'est-ce que cette fonction fait ? Elle crée essentiellement quelques variables à l'intérieur.

Donc faisons let x equals to 10, const y equals to 20.

Et puis let const, d'accord, faisons var z equals to 30. D'accord.

Et puis simplement nous allons faire un console dot log de x virgule y virgule z. D'accord.

Donc nous savons que si je fais maintenant do something, j'appelle simplement cette fonction, je sais que le résultat sera 10 20 30, des choses très, très simples que nous avons créées ici. D'accord.

Mais c'est là que notre règle numéro un entre en jeu, quelle était la règle numéro un, les variables définies à l'intérieur d'une fonction ne peuvent pas être accessibles de l'extérieur. Exact.

Donc cela signifie que j'ai défini let x const y var z à l'intérieur de la fonction do something et j'ai exécuté do something, il a exécuté cette console dot log x y z.

Maintenant, si j'essaie de prendre cette console dot log et d'essayer de l'exécuter à l'extérieur, que va-t-il se passer ? Vous voyez cela ? Il dit x n'est pas défini.

D'accord, x n'est pas défini, peut-être que x est en retard, donc il n'est pas capable de définir.

Pourquoi aussi est-ce que la cause n'est pas capable, comment est-ce qu'une var ? Non, même si c'est une var, et qu'elle est définie dans une fonction, vous ne pouvez pas accéder à cette variable à l'extérieur d'une portée à l'extérieur de cette fonction, vous ne pouvez pas accéder à cela, c'est le premier principe que nous avons appris il y a un instant. Exact.

Maintenant, le deuxième principe, de quoi s'agissait le deuxième principe ? Vous vous en souvenez ? Le deuxième principe concernait le fait que la fonction peut maintenant accéder à tout et à tout de sa portée, c'est-à-dire la portée où elle est définie.

D'accord, donc voyons la deuxième règle.

Maintenant, ce que nous allons faire ? Nous allons définir var x equals to 10, const y equals to 20, let z equals to 30. D'accord.

Maintenant, si je fais fonction, do something et fais un console dot log de x virgule y virgule z, que pensez-vous qu'il va se passer ? Si je fais simplement do something, que va-t-il se passer ? Pensez-vous que cela va donner une erreur ou va-t-il imprimer avec succès ? Pourquoi ? Parce que notre deuxième règle dit, où que la fonction, quelle que soit la portée dans laquelle la fonction est définie, si des variables sont déclarées dans cette portée, la fonction peut accéder à cette variable, cette fonction est déclarée dans la portée globale, cela signifie que la fonction n'est pas à l'intérieur d'une autre fonction.

Donc cela signifie que si la portée globale a des variables, la fonction sera en mesure d'accéder à ces variables à l'intérieur de la fonction elle-même.

Mais lorsque nous avons fait l'inverse, nous avons déclaré toutes ces choses à l'intérieur de la fonction et avons essayé d'y accéder de l'extérieur, cela ne fonctionne pas.

Donc ces deux règles définissent la portée fonctionnelle, la portée dont nous parlons est la portée fonctionnelle, vous devez vous souvenir de ce qui est accessible où, chose simple si c'est dans la portée externe, si c'est si c'est défini dans la même portée où la fonction est définie, elle est accessible à l'intérieur de la fonction.

Mais si elle est définie à l'intérieur de la fonction, elle n'est pas accessible de l'extérieur, même si c'est une var qui est déclarée et définie à l'intérieur de la fonction.

C'est clair.

Super.

Donc demandez à un développeur un sujet complexe sur JavaScript.

Il y a de fortes chances que nous entendions parler de fermetures.

C'est parce que les fermetures ne sont pas comprises fondamentalement en reliant les points.

D'accord, du point de vue de la connexion des points.

Si vous ne connaissez pas la connexion des points et la création d'une carte mentale pour apprendre un sujet complexe, j'ai créé une vidéo sur la façon d'apprendre JavaScript en reliant les points, veuillez aller de l'avant et y jeter un coup d'œil.

Maintenant, en revenant aux fermetures, si vous apprenez les fermetures en reliant les points, vous trouverez la compréhension des fermetures beaucoup plus facile, si vous sautez directement dans la fermeture et essayez de la comprendre, vous ne pourrez peut-être pas bien la comprendre.

Mais si vous venez de l'arrière-plan des fonctions imbriquées, puis de la portée des fonctions, vous serez en mesure de comprendre la fermeture très facilement.

D'accord, donc entrons dans la compréhension des fermetures, afin que nous puissions réellement la ressentir, c'est facile.

Jetez un coup d'œil à cette image sur votre écran.

Donc il y a une boîte à l'intérieur de laquelle il y a une autre boîte, considérons celle-ci comme une fonction externe, et celle-ci comme une fonction interne, nous avons déjà appris à propos des fonctions imbriquées, n'est-ce pas ? Donc donnons-leur un nom.

Par exemple, je vais leur donner, donner à celle-ci comme f one comme fonction one, ou je vais lui donner comme un nom, l'externe, pour être très sûr qu'ils sont à l'extérieur, celle-ci est externe, et celle-ci, bien sûr, interne.

Maintenant, vous savez, si je définis une variable ici, disons a, cette variable n'est pas accessible de l'extérieur.

Mais si je définis une variable ici, disons b, cette variable est accessible de l'intérieur de la fonction interne.

Donc nous avons appris cela dans la fonction imbriquée et la portée de la fonction très clairement. D'accord.

Maintenant, qu'est-ce qu'une fermeture ? La fonction imbriquée est une fermeture, cette fonction interne n'est rien d'autre qu'une fermeture, d'accord, aussi simple que cela.

Donc si quelqu'un vous demande une définition de fermeture, vous pouvez dire que cette fonction imbriquée est une fermeture.

Maintenant, si vous allez chercher une définition plus formelle, vous savez, la fermeture et par exemple, si vous allez sur MDN, et essayez de chercher ce qu'est une fermeture, vous obtiendrez une définition comme une fermeture est une fonction qui peut avoir des variables libres avec un environnement qui peut exécuter cette variable, d'accord, ce qui signifie que l'environnement n'est rien d'autre que cette fonction interne.

Et les variables signifient toutes les variables qui sont définies à l'intérieur de cette fonction interne.

Et il y a une capacité à travers laquelle vous serez en mesure d'exécuter des choses qui sont dans cette fonction interne.

Donc cette fonction interne est essentiellement une fermeture.

D'accord, c'est ainsi que nous devrions comprendre la fermeture.

Maintenant, laissez-moi résumer.

La fonction interne ne peut être accessible que depuis les instructions de la fonction externe, correct, nous le verrons aussi dans le code.

Et la fonction interne forme une fermeture, cela signifie que la fonction interne peut utiliser les variables, les arguments, tout de la fonction externe, tandis que la fonction externe ne peut pas utiliser les arguments et la variable de la fonction interne ici.

Avec cela, si nous comprenons ce qu'est une fermeture, la fermeture n'est rien d'autre que la fonction imbriquée, car elle fournit un environnement, vous savez, au monde extérieur.

Donc cette fonction imbriquée peut vivre plus longtemps, la fonction imbriquée peut vivre plus longtemps pour l'exécution.

Et elle peut en fait effectuer toutes les opérations requises.

Bien, donc écrivons une fonction, nous donnerons le nom d'équipe comme outer.

Et prenons un paramètre de cette fonction outer.

Et puis prenons une autre fonction, une fonction imbriquée, qui est comme inner, nous prendrons aussi un paramètre ici.

Et ce que nous pouvons faire ici, c'est la beauté de cela, la fonction interne peut accéder aux variables et aux arguments de la fonction externe.

Donc je peux faire return x plus y, correct, la fonction interne peut accéder à l'argument de la fonction externe ou à toute variable déclarée à l'intérieur de la fonction externe.

Donc je peux faire return x plus y très bien ici. D'accord.

Et puis enfin, ce que je peux faire, je peux faire return inner.

D'accord, je retourne cette fonction interne également. D'accord.

Maintenant, puisque la fonction interne, la fonction interne est celle-ci, celle-ci forme la fermeture, c'est ce qu'est la fermeture. D'accord.

Maintenant, ce que je peux faire, c'est essentiellement appeler cette fonction externe.

D'accord, et spécifier l'argument, puis tirer parti à la fois de outer et inner ensemble.

C'est l'avantage. D'accord.

Donc laissez-moi voir, comment puis-je faire cela ? Je vais simplement appuyer sur entrer.

Maintenant, premièrement, ce que je peux faire, c'est const outer return equals to outer, donnons 10.

Que pensez-vous qu'il sera retourné ici ? C'est la partie la plus intéressante, ce qui sera retourné.

Donc une fois que nous appelons cette fonction externe, la fonction externe retourne rien d'autre qu'une fonction, qui est comme une fonction interne.

Maintenant, lorsque l'exécution de la fonction est terminée, l'appel est terminé, cette fonction est terminée, n'est-ce pas ? Cette fonction n'est nulle part dans l'image.

Donc si j'appuie sur entrer ici, outer est simplement terminé, il n'est nulle part dans l'image.

Mais la beauté de cela, la beauté de cela, c'est que l'argument que j'ai passé à outer est toujours présent, où est-il toujours présent à l'intérieur de inner parce que ce 10 a été passé ici, ce 10 est toujours utilisé ici et il est toujours présent, même après l'exécution de outer parce que outer retourne inner, inner est en fait ici outer return.

Donc laissez-moi simplement si je fais outer return pour vous, si je fais simplement cela et imprime cela pour vous, ce qu'il retourne, c'est inner y return x plus y, qui est écrit cette fonction, où x n'est rien d'autre que ce 10 que j'ai passé.

Donc bien que l'exécution de outer soit terminée, mais la valeur que nous avons passée par outer est toujours présente dans inner.

Donc cela signifie, cela signifie que si je fais simplement outer outer return maintenant, oh, vous à votre outer return maintenant, avec un paramètre de 2, cela va me donner le résultat de 12.

Pourquoi ? Parce que outer return n'est rien d'autre que cette fonction interne, la fonction interne attend un paramètre ici, le paramètre que j'ai passé n'est pas passé l'argument ici.

Mais ce qu'elle a fait, c'est qu'elle a en fait utilisé ce 2 avec une variable que j'ai passée il y a longtemps et l'exécution est terminée.

C'est pourquoi cela s'appelle une fermeture.

Cela a créé une fermeture, une fermeture n'est rien d'autre que les variables et un environnement que vous pouvez exécuter librement.

Que voulez-vous dire par librement ? Cela signifie que généralement dans les fonctions, lorsque l'exécution de la fonction est complètement terminée, c'est fait, toute variable qui est en fait créée à l'intérieur de cela, c'est tout, c'est essentiellement que vous n'allez plus l'obtenir.

Mais dans ce cas, bien que outer ait été exécuté il y a longtemps, mais l'argument du paramètre que nous avons passé par outer est toujours présent dans inner parce que inner est une fermeture, et je peux en fait l'utiliser, vous savez, à un moment ultérieur.

Donc c'est le concept de fermeture que vous devez comprendre.

C'est ce que vous devez comprendre, comme pourquoi la fermeture est une méthode vraiment pratique, pourquoi la fermeture est vraiment utile.

Donc vous pouvez utiliser la fermeture pour divers cas d'utilisation.

L'un des cas d'utilisation que j'ai vus ici est comme la préservation de la variable.

Donc j'ai passé 10 bien que l'exécution de la fonction soit terminée, mais 10 est toujours préservé ici.

Et comme il est préservé ici, il peut être utilisé avec une autre valeur pour calculer quelque chose et retourner, n'est-ce pas ? C'est pourquoi la fermeture est utile.

Dans la vidéo que je vais créer en me concentrant uniquement sur la fermeture, je vais parler de beaucoup plus d'exemples concrets et de cas d'utilisation que vous pouvez réellement construire avec la fermeture.

Donc, comme vous comprenez fondamentalement la fermeture maintenant, commencez à pratiquer, commencez à créer ce genre de petit exemple où vous avez une fonction externe, une fonction interne, les deux prennent un argument, vous retournez la fonction interne de la fonction externe et voyez après l'exécution de la fonction externe comment la valeur que vous passez par la fonction externe peut encore être utilisée à l'intérieur de la fonction interne à un moment ultérieur.

Donc ce genre de chose, l'exemple que vous voyez ici, essayez de trouver cet exemple sur internet ou essayez de cuisiner quelque chose par vous-même et essayez de le pratiquer plus de cas d'utilisation orientés exemple comme des exemples de cas d'utilisation de la vie réelle de la fermeture qui viendront dans une vidéo dédiée.

J'espère que cela clarifie votre concept.

Maintenant, juste pour récapituler une fois, la compréhension de la fermeture dépend de votre compréhension de la fonction imbriquée plus la portée de la fonction.

Nous savons par la fonction imbriquée qu'une fonction peut en définir une autre à l'intérieur.

Nous savons pourquoi la portée de la fonction est telle que la fonction externe ne peut pas accéder à une variable à l'intérieur de la fonction interne.

Cependant, la fonction interne peut accéder à une variable et à l'argument de la fonction externe.

Cette capacité nous donne une fonctionnalité très puissante appelée fermeture, grâce à laquelle, même si l'exécution de la fonction externe est terminée, nous pouvons persister certaines valeurs qui ont été passées à la fonction externe à l'intérieur de la fonction interne et les calculer à un moment ultérieur.

Cela devient une fonctionnalité puissante en soi, un motif de conception puissant en soi en JavaScript, qui est appelé fermeture.

J'espère que c'est clair pour vous.

Maintenant, nous apprenons les fonctions de rappel.

Qu'est-ce qu'un rappel ? D'accord, donc tout est dans le nom lui-même, rappel.

Cela signifie le rappeler à un moment donné.

Mais comprenons avec un exemple.

Maintenant, en JavaScript, la fonction est un citoyen de première classe.

Que voulez-vous dire par là ? Cela signifie que nous pouvons créer une fonction, nous avons vu la définition de la fonction, nous pouvons assigner une fonction, nous avons vu comme lorsque vous faites const x equals to function et puis essentiellement nous pouvons assigner cette fonction à une variable.

Nous pouvons assigner une fonction, nous pouvons retourner, nous pouvons définir une fonction à l'intérieur d'une autre fonction.

Nous avons vu cela à partir de la fonction imbriquée.

Maintenant, la prochaine chose que nous allons voir, c'est comme nous pouvons passer une fonction comme paramètre à une autre fonction.

D'accord, c'est là que la fonction de rappel entre en jeu et nous verrons quels sont les cas d'utilisation.

D'accord, d'abord, définissons une fonction appelée foo.

D'accord, et c'est la fonction foo.

Qu'est-ce que cette fonction foo fait ici ? Supposons que la fonction foo peut prendre une autre fonction comme paramètre.

Passons une autre fonction, fonction comme paramètre appelé foo ou appelons-le bar parce que ce sont les choses que nous utilisons habituellement pour ces noms d'exemple.

Maintenant, comme cette fonction prend un argument qui n'est rien d'autre qu'une autre fonction.

Donc cela signifie que je peux le capturer comme un paramètre bar et supposer que ce bar n'est rien d'autre qu'une autre fonction.

Donc cela signifie qu'à l'intérieur de cela, je devrais être capable d'exécuter cette fonction.

Très simple.

Si c'était une chaîne, j'aurais pu imprimer la chaîne ou la concaténer avec autre chose ou faire quelque chose avec l'écran.

Si c'est un nombre, j'aurais fait quelque chose avec un nombre.

Si c'est une fonction, je vais simplement l'exécuter.

Maintenant, pour exécuter cette fonction, nous savons que nous devons donner cette parenthèse pour appeler cette fonction ou exécuter cette fonction.

Cette fonction particulière est appelée un rappel.

Cette fonction particulière est appelée un rappel.

Mais pourquoi ? Nous y viendrons.

Mais d'abord, je veux l'exécuter.

Comment exécutons-nous cela ? Je l'ai définie.

Maintenant, si je dois exécuter cela, je sais que foo prend une fonction.

Donc je peux en fait lui passer une fonction.

Et faisons quelque chose comme ceci.

Donc qu'est-ce que j'ai fait ? foo prend une fonction.

Bien sûr, nous avons dit que foo prend une fonction.

Le bar est une fonction.

Et nous l'exécutons à l'intérieur.

Cela signifie que je peux passer une fonction comme argument à foo.

Donc j'ai passé une fonction.

Vous les gars, vous réalisez une chose ici ? J'ai créé une fonction qui n'a pas de nom.

Donc cette fonction est appelée une fonction anonyme.

La fonction qui n'a pas de nom est appelée une fonction anonyme parce qu'elle n'a pas de nom.

Et comme je vais utiliser cette fonction instantanément ici, je ne me suis pas soucié de la créer à nouveau.

Donc si je l'exécute simplement.

Cette fonction est passée ici et ensuite elle est exécutée dans cette ligne.

Une fois qu'elle est exécutée dans cette ligne, cette console.log est exécutée et elle imprime bar.

La même chose que je peux faire au lieu de faire cette ligne pour que vous compreniez mieux, je peux créer une fonction avec un nom.

Par exemple, une fonction nommée et au lieu de cela, je peux en fait dire console.log de bar à nouveau.

La même chose que la fonction précédente au lieu de la passer directement.

Maintenant, je peux faire foo de named. Exactement.

C'est exactement la même chose que ce que j'ai fait au lieu de déclarer à nouveau la fonction avec un nom de fonction et puis de passer la fonction ici, je passe simplement la fonction directement là.

C'est la seule différence mais la sortie est la même.

Donc maintenant vous savez qu'une fonction peut prendre une fonction comme argument et que je peux en fait le faire.

Et la fonction qui est passée comme paramètre et que j'utilise, vous savez, à l'intérieur à un moment ultérieur est appelée fonction de rappel.

Mais pourquoi est-elle appelée fonction de rappel.

C'est la chose.

Revenons au début pour comprendre pourquoi elle est appelée fonction de rappel.

Donc nous allons à nouveau définir la fonction foo qui prend une autre fonction bar et disons que j'ai une certaine condition.

La condition est si c'est la nuit, considérons que c'est la nuit est une variable booléenne, elle peut être vraie ou fausse.

Dans ce cas, vous appelez bar.

Habituellement, seulement la nuit, comme vous le savez, les bars seront en pleine effervescence partout ou disons qu'il y a une autre condition, si les boissons sont terminées, vérifiez en ligne dans ce cas seulement, d'accord.

Erreur de frappe, vérifiez en ligne dans ce cas même, vous appelez bar.

Donc nous avons deux conditions où nous voulons appeler cette fonction particulière, appelez bar.

La première condition est si c'est la nuit, alors appelez la fonction bar ou peut-être faites un appel en ligne ou un appel réseau pour vérifier si les boissons sont terminées, puis appelez bar.

Donc cela signifie que le rappel de bar est basé sur certaines conditions qui se produisent dans cette fonction.

C'est un cas où vous voulez réellement appeler cette fonction en tant que fonction de rappel.

Vous l'appelez en fonction de certaines conditions, en fonction de certaines choses.

C'est tellement puissant car vous pouvez passer n'importe quelle fonction à une autre fonction et appeler cette fonction passée en fonction de n'importe quelle condition à un moment ultérieur.

C'est pourquoi on l'appelle un rappel.

Maintenant, si vous voulez comprendre ce concept avec un exemple beaucoup plus approfondi.

J'ai créé un exemple avec le hub de pizza ou l'histoire du petit garçon et du hub de pizza.

C'est comme une narration afin que tout le monde puisse comprendre.

Cette vidéo est déjà disponible.

Allez-y et regardez cette vidéo.

Le lien de cette vidéo est dans la description de cette vidéo.

Vous pouvez la consulter et découvrir comment, dans une application réelle, vous pouvez utiliser le rappel, vous savez, sans effort.

Donc j'espère que les fonctions de rappel sont claires pour vous maintenant.

Maintenant, nous apprenons la fonction d'ordre supérieur, la fonction d'ordre supérieur ou HOF.

Qu'est-ce qu'une fonction d'ordre supérieur.

Une fonction d'ordre supérieur par définition est une fonction régulière, une fonction normale qui prend une ou plusieurs fonctions comme argument et/ou retourne une fonction comme valeur.

Écrivons-le.

C'est un peu complexe de cette manière.

Donc une condition est comme elle prend une ou plusieurs fonctions comme argument.

C'est la première chose.

Et puis la deuxième chose.

Elle peut retourner une fonction.

Donc pas nécessairement les deux conditions doivent être remplies pour une fonction d'ordre supérieur.

Si l'une des conditions est remplie, c'est en fait une fonction d'ordre supérieur.

Nous venons de parler d'une fonction de rappel.

Qu'est-ce qu'on a dit sur la fonction de rappel.

Une fonction de rappel est une fonction qui prend une fonction comme argument en fonction de certaines conditions ou autre chose.

Quelle que soit la fonction que nous passons comme argument, elle va invoquer cette fonction à l'intérieur.

Maintenant, dans le premier cas de la HOF, la fonction d'ordre supérieur, il s'agit de prendre une ou plusieurs fonctions comme argument.

Donc cela signifie qu'il y a une relation entre une fonction d'ordre supérieur et une fonction de rappel.

Et c'est là que parfois, lors des entretiens, les interviewers posent des questions pièges : HOF et rappel sont-ils identiques.

Non, HOF et rappel ne sont pas exactement identiques car pour les fonctions de rappel, il n'est pas obligatoire que la fonction principale retourne une fonction.

Elle peut accepter la fonction comme argument.

Faire quelque chose avec.

Mais il n'est pas nécessaire qu'elle doive retourner une fonction.

Alors que dans la fonction d'ordre supérieur, si la fonction retourne une autre fonction, elle est appelée fonction d'ordre supérieur.

Dans ce cas aussi, elle est appelée fonction d'ordre supérieur.

Donc cela signifie que si je prends simplement une fonction.

Prenons une fonction.

Donnons-lui le nom de get capture et prenons un paramètre appelé camera.

Maintenant, si je fais comme ceci.

C'est une fonction d'ordre supérieur.

Pourquoi, parce que camera est une fonction et je l'exécute ici.

Donc je peux en fait appeler get capture ici.

Je peux appeler.

Désolé pour cela.

Je peux appeler get capture ici.

Et lui passer une fonction.

Je peux dire fonction.

Faire une console console dot log.

Dites can on.

Donc il exécute.

C'est ce que nous avons vu lorsque nous avons compris une fonction de rappel.

Maintenant, nous pouvons aussi faire l'autre partie comme une fonction retournant une autre fonction qui est aussi appelée une fonction d'ordre supérieur.

Donc comment cela se fera-t-il.

Nous pouvons en fait faire comme fonction return the f n et elle peut retourner une fonction avec disons une console dot log de returning something we are printing over here to prove that it works.

Maintenant, comment vais-je exécuter cela, plusieurs façons de l'exécuter.

Par exemple.

Const.

Disons f n equals to I can do return f n.

To return f n.

Lorsque je retourne f n, ce qu'il fait, il retourne une fonction maintenant.

Donc si je fais cela.

Donc f n n'est maintenant rien d'autre qu'une fonction.

Si vous voyez que le moment où je tape f n, il donne f.

Si je fais simplement une impression ici.

Il exécute une fonction pour exécuter celle-ci.

Cela signifie que j'ai besoin de la parenthèse.

Donc il exécutera celle-ci.

Donc c'est une façon dont je peux en fait exécuter cette chose.

Donc j'espère que c'est assez clair.

Maintenant, si vous travaillez sur JavaScript depuis un certain temps, vous utilisez déjà certaines des fonctions d'ordre supérieur.

Vous le savez déjà.

Et la fonction d'ordre supérieur est extrêmement utile pour vos aspects de fiabilité et de prévisibilité.

Vous utilisez déjà certaines de ces choses appelées fonctions de tableau comme map filter reduce find toutes ces méthodes que vous avez sur les tableaux sont toutes des fonctions d'ordre supérieur car elles sont aussi vous écrivez un code comme vous savez un si je prends comme un deux trois et sur ce tableau vous faites quelque chose comme filter et ici vous passez une fonction votre condition de filtre que vous passez ici si vous utilisez déjà un tableau vous saurez que et c'est là que vous mettez en fait votre condition comme sur quelle condition vous voulez filtrer celui-ci vous obtenez ce comme élément et si l'élément est supérieur à deux supérieur à trois vous savez vous écrivez des conditions comme cela et sur cette base vous filtrez les choses.

Donc c'est un exemple de fonction d'ordre supérieur comme pourquoi exactement pour la fonction d'ordre supérieur et où vous utilisez le supérieur.

Maintenant, si vous voulez obtenir un très très bon aperçu de la fonction d'ordre supérieur, car c'est un cours intensif, nous n'allons pas trop en profondeur, mais vous voulez obtenir un très bon aperçu de la fonction d'ordre supérieur.

J'ai déjà créé une vidéo à ce sujet.

Veuillez y jeter un coup d'œil.

Je suis sûr que vous allez aimer apprendre la fonction d'ordre supérieur et essayer de comprendre quels sont les différents cas d'utilisation en dehors des fonctions JavaScript intégrées lorsque vous codez dans quels cas vous allez utiliser les fonctions d'ordre supérieur.

Veuillez y jeter un coup d'œil.

Voyons ce qu'est une fonction pure.

En JavaScript, lorsque vous traitez avec des fonctions, vous traitez avec beaucoup de fonctions pures, vous traitez aussi avec beaucoup de fonctions impures.

Par définition, une fonction pure est une fonction qui produit la même sortie pour la même entrée.

Donc la fonction disons greeting input est name et ce qu'elle va faire, c'est retourner un message de salutation.

Donc return hello et ce genre de message de salutation va retourner.

Très bien.

Donc si j'appelle disons greeting et que je passe mon nom, cela va retourner hello tapas.

Donc pour la même entrée, cela va retourner la même sortie.

Si je passe tapas autant de fois, autant de fois cela va retourner hello tapas.

Si je fais hello YouTube, cela va retourner hello YouTube.

Autant de fois que je vais entrer YouTube, autant de fois cela va sortir hello YouTube.

Fonction pure.

C'est une fonction pure.

La fonction pure aide à la prévisibilité.

Cela signifie que si l'entrée est la même, la sortie sera toujours la même.

Donc c'est très, très prévisible.

Qu'est-ce qu'une fonction impure ? Juste l'inverse de cela.

Cela signifie que pour la même entrée, elle ne va pas créer la même sortie.

Donc la même fonction si je fais juste un peu différemment.

Par exemple, laissez-moi créer une variable appelée greeting et ce que j'ai fait maintenant initialisée avec hello.

Maintenant, j'ai une fonction comme fonction vous savez ce gars.

Je vais simplement copier cela afin que je puisse l'utiliser.

Mais je vais changer un peu.

Ce que je vais changer au lieu de ce hello.

Heartcoding hello.

Maintenant, je prends ce greeting d'ici.

D'accord, donc si je fais maintenant greeting tapas, cela donnera hello tapas.

Très bien.

Si je donne tapas à nouveau, cela donnera hello tapas.

Très bien.

Mais si je change la valeur de cette variable greeting de hello à hola.

Hello à hola.

Et puis je le fais à nouveau pour la même entrée tapas, la sortie devient hola tapas.

Donc de hello tapas, cela devient hola tapas.

Cela signifie que say greeting ne produit pas la même sortie pour la même entrée. Exact.

Non.

Parce qu'elle dépend de quelque chose et que ce quelque chose est appelé effet secondaire.

Qu'est-ce qu'un effet secondaire ? L'effet secondaire n'est rien d'autre qu'une variable qui est en dehors de la portée de la fonction say greeting et say greeting ne peut pas contrôler cette variable particulière.

N'importe qui peut la changer, ce qui peut créer un effet secondaire tel que cette fonction particulière n'est plus une fonction pure.

Elle ne retourne plus la même sortie pour la même entrée.

Donc c'est la différence entre les fonctions pures et impures.

Pouvez-vous écrire toutes les fonctions comme des fonctions pures dans votre application, peut-être pas, vous ne pourrez peut-être pas écrire, vous savez, toutes les fonctions comme des fonctions pures car il y aura des effets secondaires, vous aurez besoin de choses comme cela, vous devrez faire un appel réseau, vous devrez probablement écrire quelque chose sur la console log, tout est un effet secondaire.

Mais autant que possible, si vous pouvez rendre certaines choses pures, vous avez plus de prévisibilité pour ces cas.

Donc surveillez cela.

Encore une fois, si vous voulez approfondir la fonction pure, vous voulez apprendre comme le cas d'utilisation réel de la fonction pure, où exactement nous l'utilisons, où pouvons-nous l'utiliser.

J'ai créé une vidéo extensive pour la fonction pure.

Jetez-y un coup d'œil afin que vous puissiez apprendre et la pratiquer beaucoup plus.

D'accord.

Donc j'espère que vous avez maintenant une compréhension fondamentale de base d'une fonction pure et impure.

D'accord, les amis.

Donc apprenons l'IFE.

Qu'est-ce que l'IFE.

C'est l'abréviation du terme immediately invoked function expressions I pour immediately puis I pour invoked puis if pour function if ou expression immediately invoked function expression qu'est-ce que cela signifie.

Cela signifie que c'est une expression de fonction, c'est là que le code à l'intérieur de la fonction est exécuté immédiatement après avoir été défini.

Maintenant, prenons une fonction par exemple, la fonction X est la fonction, n'est-ce pas, qui a un nom X.

Maintenant, si je dois exécuter cette fonction à un moment ultérieur lorsque je veux dans mon code, ce que je vais faire, c'est simplement utiliser ce nom avec la parenthèse et exécuter cette fonction.

D'accord, c'est super.

Maintenant, la seule raison pour laquelle ce nom existe, le X pour cette fonction, c'est parce que je peux utiliser ce nom pour exécuter cette fonction à un moment ultérieur.

Peut-être là où j'ai défini cette fonction après deux cents lignes après cela, en fonction d'une certaine logique, je l'exécute, je l'appelle, je l'invoque cette fonction.

D'accord.

Mais IFE dit que l'utilisation de IFE est d'exécuter la fonction immédiatement après qu'elle a été définie.

Donc si je dois faire cela, je n'ai pas besoin du nom de la fonction parce que le moment où je définis, juste après avoir défini la fonction, je veux l'exécuter.

Donc je n'ai pas besoin d'un nom.

Donc commençons par quelque chose qui n'a pas de nom.

J'ai fait la fonction X avant, je ne donne aucun X maintenant, plutôt j'ai créé quelque chose comme ceci.

Mais si j'essaie de l'exécuter, cela va me donner un problème en disant que l'instruction de fonction nécessite un nom de fonction.

Donc maintenant, je ne peux pas créer une fonction anonyme comme celle-ci et la laisser simplement comme elle est parce qu'elle nécessite un nom de fonction.

Maintenant, laissez-moi vous présenter un opérateur appelé opérateur de groupe qui n'est rien d'autre qu'un ensemble de parenthèses.

Maintenant, si je mets cette fonction anonyme, la fonction sans nom à l'intérieur de ce groupe, vous savez, l'opérateur, que se passe-t-il si je donne simplement une entrée, elle donne en fait la représentation en chaîne de cette fonction particulière elle-même.

La représentation en chaîne de cette fonction elle-même.

Correct.

Sans aucun nom, mais la représentation en chaîne.

Dans les chapitres précédents, nous avons vu que lorsque nous obtenons une représentation en chaîne de cette fonction elle-même, cela signifie que c'est une fonction.

Donc cela signifie que je peux en fait donner la parenthèse après cela pour l'exécuter.

Donc cela signifie que si je prends ce gars et que je mets simplement une parenthèse autour de cela, cela signifie qu'il sera exécuté.

Oui.

Donc j'ai obtenu une fonction correcte qui a été exécutée.

Donc c'est ce qu'est l'IIFE.

Donc maintenant, laissez-moi écrire quelques codes à l'intérieur de cela afin que vous sachiez qu'il est exécuté.

Donc console dot log IIFP.

Si j'essaie simplement de l'exécuter, vous voyez que IIFE a été imprimé.

Donc la fonction, lorsque je la définis, au même moment, j'exécute également cette fonction, c'est ce qu'est l'IIFE, c'est ce que sont les expressions de fonction immédiatement invoquées.

Maintenant, si vous demandez pourquoi cela existe, il y a quelques raisons pour lesquelles cela existe.

Avant ES6, je veux dire avant que nous ayons comme late const toutes ces meilleures façons de gérer l'accessibilité d'une variable comme où elle, où ce qui peut être accessible où, où les choses ne peuvent pas être polluées, où vous avez, vous savez, avant ES6 où vous aviez seulement var comme la chance que votre variable globale soit polluée, vous n'aviez pas d'autre option que d'utiliser IIFE pour les protéger.

Une autre raison est comme une raison très normale, c'est que lorsque vous créez une fonction avec un nom de fonction, cela signifie que le nom de la fonction, à moins qu'il ne soit comme une fonction imbriquée ou une fonction interne, le nom de la fonction existe essentiellement dans le contexte global et globalement, il n'est pas à l'intérieur d'une autre fonction.

Donc cela signifie qu'il y a des chances que quelqu'un d'autre puisse utiliser le même nom de fonction quelque part ailleurs, il pourrait y avoir une chance de conflit ou un nom de variable avec le même nom que le nom de la fonction et la chance de le polluer.

Donc pour que cela ne se produise pas, l'IIFE peut être utilisé.

Donc l'IIFE peut être utilisé pour divers cas d'utilisation différents, mais le concept de l'IIFE est celui-ci, lorsque vous définissez effectivement la fonction, immédiatement après cela, vous voulez l'exécuter.

Seulement dans ce cas, vous utilisez la syntaxe et utilisez cet IIFE.

J'espère que la décomposition de la syntaxe a aussi du sens pour vous, car elle n'a pas besoin de nom.

Donc nous avons commencé avec une fonction anonyme, puis nous avons en fait utilisé un opérateur de groupe autour de celle-ci afin que nous obtenions une définition de fonction et puis la dernière parenthèse, essentiellement une paire de parenthèses utilisée toujours pour appeler ou invoquer la fonction, nous l'utilisons avec elle et nous avons obtenu un résultat IIFE sur-le-champ.

J'espère que cela a été utile.

Merci d'avoir regardé.

Nous allons comprendre la pile d'appels, mais avant de comprendre la pile d'appels, nous devons bien comprendre les exécutions de fonctions.

Donc d'abord, nous allons comprendre ce qu'est la pile d'appels et aussi nous allons comprendre ce qu'est l'exécution de fonctions afin que vous obteniez une image complète et claire à ce sujet.

L'élément qui entre dans la pile en premier en sort en dernier. Exact.

Donc ici, considérons qu'il y a trois éléments comme F1 F2 F3.

Ils sont entrés comme F1 puis F2 puis F3, mais lorsqu'ils ont dû sortir, F3 est sorti en premier, puis F2 et puis F1.

C'est ainsi que fonctionne la pile.

Maintenant, au lieu d'une variable normale, si une fonction entre dans une pile, ce sera de la même manière, comme F1 F2 F3 entrent et puis F3 F2 F1 sortent dans cette séquence.

Donc lorsqu'une fonction est exécutée, il y a une pile que le moteur JavaScript maintient.

Et dans cette pile, il définit comment l'exécution de cette fonction particulière a lieu.

Chaque fois que l'interpréteur JavaScript va ligne par ligne et rencontre un appel de fonction ou une invocation de fonction, il met cette fonction dans une pile, l'exécute et une fois l'exécution terminée, il la retire de la pile.

La raison de faire cela, il y a une séquence appropriée de la manière dont les fonctions sont exécutées peut être maintenue à travers la structure de données de la pile.

Nous allons voir cela avec un exemple.

D'accord.

Donc le premier exemple que nous allons prendre, il y a trois fonctions F1 F2 F3 que vous pouvez voir à l'écran.

Chacune de ces fonctions a un ensemble de code qui peut être exécuté lorsque nous invoquons ou appelons cette fonction.

Nous appelons ces fonctions d'abord F1 puis F2 puis F3.

À droite, nous avons une pile d'exécution de fonctions ou une pile d'appels.

Donc la pile d'appels et la pile d'exécution de fonctions sont les mêmes.

Ce que nous allons voir, c'est lorsque ces fonctions sont exécutées, comme F1 est appelée, ce qui arrive à la pile d'appels, puis F2, ce qui arrive à la pile d'appels, puis F3, ce qui arrive à la pile d'appels.

C'est ce que nous voulons apprendre.

Donc s'il vous plaît, portez une attention à cette pile d'appels et aussi à la manière dont le code est exécuté.

La première chose, F1 est exécutée, F1 entre dans la pile d'appels ou la pile d'exécution de fonctions, à l'intérieur de F1, un ensemble de code.

D'accord, tout est fait, exécuté, exécuté, exécuté.

Il n'y a pas de fonction à l'intérieur.

Donc rien d'autre à mettre à ce moment-là dans la pile.

Puis l'exécution de F1 est terminée.

Sortez F1 de celle-ci.

Ensuite, F2 est exécutée.

Mettez F2 de manière similaire là.

Il n'y a pas de fonction à l'intérieur, mais exécutez tout le code.

Exécutez F2, sortez-la.

Puis va à F3.

Mettez à nouveau F3 à l'intérieur de la pile.

L'exécution est terminée.

Il n'y a pas de fonction, un ensemble de code.

Obtenez-le, exécutez-le.

C'est sorti.

C'est très simple, F1 F2 F3 ont été exécutées.

Maintenant, prenons un scénario un peu plus complexe avec ce code.

Donc ce qui se passe ici, vous avez F1, votre ensemble de code.

Il n'y a pas de fonction dedans.

Puis vous avez F2, un ensemble de code, mais il y a une fonction F1 que vous avez définie avant, nous l'invoquons ici.

Vous vous souvenez qu'une fonction peut avoir une autre fonction dedans.

Une fonction peut invoquer une autre fonction dedans.

Oui.

C'est un exemple.

Donc F2 invoque essentiellement F1 ou appelle F1 dedans avec un ensemble de code.

F3, il n'y a pas d'autre code que l'exécution de F2.

C'est comme une chaîne. Exact.

Donc n'importe quel appel F3, il invoque en fait F2.

F2 exécute un ensemble de code et invoque F1.

F1 exécute un ensemble de code, mais pas d'invocation de fonction dedans.

Maintenant, comment cela peut être représenté dans la pile d'appels ou la pile d'exécution de fonctions.

C'est ce que vous allez voir.

Donc encore une fois, portez attention au côté droit.

D'abord, ce qui s'est passé lorsque F3 s'exécute.

Lorsque F3 s'exécute, il trouve F2.

Mais avant cela, F3 doit entrer dans la pile d'appels, car la fonction doit entrer dans la pile d'appels pour être exécutée.

Donc maintenant, F3 est exécuté, il trouve F2.

Oh oui.

F2, une autre fonction.

Donc avant de sortir F3, car F3 ne sera sorti que lorsque l'exécution de F3 sera terminée.

Mais ce n'est pas terminé maintenant, le curseur est à F2.

Donc il doit mettre F2 dedans.

F2 est entré.

L'exécution de F2 commence, mais F3 est toujours dans la pile d'appels.

Donc l'exécution de F2, un ensemble de code est exécuté, cette ligne est exécutée, cette ligne est exécutée.

Oh maintenant, il a rencontré F1 qui est aussi une fonction.

Il est temps de le mettre dans la pile d'appels.

F1 est entré dans la pile d'appels.

Maintenant, si vous voyez dans la pile d'appels ou la pile d'exécution de fonctions, vous avez F1 F2 F3.

Mais dans l'ordre inverse de la manière dont ils sont entrés, n'est-ce pas.

Maintenant, nous sommes à F1.

F1, un ensemble de lignes de code sont là.

Exécutons-les une par une.

Mais il n'y a pas de fonction.

Donc rien d'autre à mettre dans la pile d'appels.

Mais lorsque l'exécution est terminée pour F1, nous devons le sortir de la pile d'appels, F1 est terminé.

Maintenant, notre curseur est ici.

Donc l'exécution de F1 est terminée.

Cela signifie que l'exécution de F2 est également terminée maintenant, sortez F2.

Donc le curseur est ici.

L'exécution de F2 est terminée.

La ligne suivante, il n'y a plus de code.

Cela signifie qu'il est temps de sortir F3.

N'est-ce pas génial.

Donc c'est exactement ce qu'est la pile d'exécution de fonctions ou la pile d'appels.

C'est ainsi que cela fonctionne.

C'est ainsi que le moteur JavaScript maintient dans quelle séquence votre fonction doit être exécutée.

J'espère que c'est très clair pour vous maintenant.

Maintenant, ce concept particulier est très, très important si vous voulez apprendre la programmation asynchrone JavaScript en profondeur.

J'ai créé une série complète pour la programmation asynchrone JavaScript.

Si vous êtes intéressé, allez-y et prenez cette série.

Je suis sûr que vous serez en mesure de maîtriser ce concept très, très rapidement.

D'accord.

Merci d'avoir regardé.

Bonjour les amis.

Parlons de récursivité.

Qu'est-ce que la récursivité.

La récursivité signifie une fonction qui se réfère ou s'appelle elle-même.

Que signifie-t-il.

Créons une fonction.

Disons fonction foo.

Et à l'intérieur de cela, nous faisons, nous faisons une console dot log.

Disons foo.

Et puis nous disons que la récursivité est quelque chose où la fonction peut se référer ou s'appeler elle-même.

Dans ce cas, nous allons nous appeler nous-mêmes.

Que se passe-t-il lorsque nous invoquons cela.

Donc nous invoquons foo.

Êtes-vous avec moi.

Que va-t-il se passer.

Voyez-vous ce qui s'est passé.

La fonction continue à appeler, à appeler, à appeler, à appeler et après un certain temps, elle va dire que la taille maximale de la pile d'appels est dépassée.

Donc si vous connaissez la pile d'appels de fonction maintenant, cela signifie que foo va se mettre plusieurs fois dans la pile d'appels, la pile d'appels, la pile d'appels plusieurs fois et une fois que cela se produira, la pile d'appels a une taille maximale définie lorsque la limite de taille maximale, la limite de seuil est atteinte, elle va donner l'erreur d'appel de la pile d'appels maximale dépasse.

C'est l'erreur que nous obtenons.

Mais si vous obtenez une erreur, à quoi sert la récursivité.

Nous y viendrons.

Juste une seconde.

Mais avant cela, c'est une façon dont nous pouvons définir la récursivité, comme une fonction qui s'invoque elle-même.

Faisons une autre façon.

C'est ainsi que la récursivité peut être faite.

Par exemple, const foo equals to function bus et puis à l'intérieur de cela, ce que je vais faire, je peux appeler foo comme ceci.

Que se passera-t-il.

Donc dans ce cas, j'ai créé une fonction et la fonction est assignée à une variable appelée foo.

Donc cela signifie que foo lui-même est une fonction.

Donc dans ce cas, foo et bus sont presque identiques.

Donc que vous appeliez foo ici ou que vous appeliez bus ici, quoi qu'il en soit, vous créez en fait une récursivité ici parce que maintenant vous faites référence à cette fonction particulière soit avec foo soit avec bus, quel que soit le nom, c'est la même fonction.

Donc c'est une autre façon de créer la récursivité.

Donc dans ce cas aussi, il va simplement OK, foo existe déjà parce que j'ai utilisé ce nom avant.

Donc si vous l'utilisez en fait, il va en fait créer la récursivité pour vous.

Les deux cas sont identiques.

Maintenant, nous avons vu ce qui se passait avec la récursivité.

Cela se contentait de se créer, de s'appeler elle-même, de s'appeler elle-même, puis de heurter la taille maximale du tas et de provoquer une erreur.

Alors pourquoi devrions-nous utiliser la récursivité.

D'accord, donc une chose, c'est que chaque fois que vous utilisez la récursivité, vous devez vous assurer que vous avez quelque chose appelé condition de base.

C'est très important.

Donc la récursivité sans condition de base n'est pas très utile, la condition de base signifie sous quelle condition vous devez arrêter la récursivité.

Vous devez arrêter la récursivité à un moment donné, car vous voulez arrêter l'exécution de cette fonction pour qu'elle s'exécute elle-même à un moment donné afin que vous puissiez en sortir ou faire autre chose.

Donc cette condition est appelée condition de base.

Donc habituellement, comment vous allez écrire les choses dans un programme récursif, dans un programme récursif.

Donc vous allez écrire quelque chose comme fonction recurse fonction recurse si c'est une condition de base si la condition de base dans ce cas, vous faites probablement quelque chose et après cela, vous retournez sinon continuez à récurser.

Donc c'est ainsi que vous faites en fait la récursivité.

Vous devez avoir une condition de base et s'il y a une condition de base, vous faites quelque chose et puis vous retournez.

Sinon, vous continuez à récurser.

Écrivons un programme afin que nous puissions comprendre de manière beaucoup plus claire.

Donc le programme que nous allons écrire concerne, disons, nous allons chercher de l'eau plusieurs fois.

Donc appelons une fonction.

Créons une fonction appelée fetch water et prenons un paramètre appelé count comme combien de fois vous voulez chercher de l'eau et nous disons si le count est zéro, c'est notre condition de base.

Nous avons écrit la condition de base.

Dans ce cas, vous faites quelque chose.

Peut-être que je vais faire comme console dot log et dire comme plus d'eau.

Si triste.

Fait.

Et puis je vais retourner.

Sinon, continuez à chercher de l'eau et je vais faire comme count moins un et nous pouvons faire une console dot log ici aussi en disant console dot log fetching water.

Nous allons voir le code d'entrée et puis après avoir cherché de l'eau, nous allons faire que la ligne a été supprimée d'une manière ou d'une autre.

Fetch water count moins un.

D'accord.

Donc lisons ce code une fois de plus.

Ce que nous faisons.

Nous avons un fetch water.

Nous appelons fetch water à nouveau.

Ici, il y a une récursivité bien sûr, mais nous avons aussi une condition de base.

La condition de base est lorsque nous allons sortir de la récursivité.

Notre condition de base dit lorsque le count est zéro, alors je dis plus d'eau et je sors de cette récursivité, mais jusqu'à ce que le count soit zéro, je récurse simplement, je cherche simplement de l'eau.

Correct.

Donc maintenant, si je dis fetch water cinq fois, que va-t-il se passer.

Il va aller count est cinq est égal à zéro non, il n'ira pas à l'intérieur de cette condition de base ne se rencontre pas.

Fetch l'eau devient count quatre.

Donc count quatre signifie appeler à nouveau la même fonction avec count quatre.

Donc count quatre vient ici est quatre est égal à zéro non, à nouveau la condition de base ne se rencontre pas.

À nouveau fetch l'eau.

Maintenant, appelez le même fetch water avec quatre moins un, c'est-à-dire trois.

Continuez à faire cela jusqu'à ce que le count soit zéro.

Une fois que le count est zéro, plus d'eau et vous sortez de la récursivité. Exact.

Nous allons faire.

Donc fetching water fetching water fetching water fetching water fetching water et puis plus d'eau.

Donc nous avons écrit un programme en utilisant la récursivité et nous avons aussi la condition de base grâce à laquelle nous sortons de cette récursivité. Exact.

Maintenant, la même chose, vous auriez pu le faire avec une boucle for, n'est-ce pas.

La même fonction, la même fonctionnalité, vous auriez pu le faire avec une boucle for.

Donc il y a toujours un certain débat sur le fait de savoir si vous devriez utiliser la récursivité ou la boucle for.

Là où la boucle for est applicable, peut-être devriez-vous utiliser la boucle for.

Mais dans certains cas, par exemple, vous voulez créer la factorielle d'un nombre, la factorielle signifie la factorielle de n ou la factorielle de cinq signifie cinq fois quatre fois deux trois fois deux fois un. Exact.

Donc si vous voulez faire une factorielle, peut-être que la récursivité est la bonne façon de procéder, car elle rend le code beaucoup plus lisible que de faire une factorielle en utilisant une boucle for. Exact.

Donc la lisibilité est l'un des facteurs que vous voulez probablement prendre en compte lorsque vous utilisez la récursivité plutôt que la boucle for, là où la récursivité est applicable.

C'est tout ce qu'il y a à savoir sur la récursivité.

Chaque fois que quelqu'un vous demande à propos de votre récursivité, veuillez également mentionner que vous avez une meilleure condition où vous pouvez sortir de la récursivité.

J'espère que cela a été utile.

C'est bon, les amis.

Tout doit avoir une fin.

Donc notre cours intensif doit aussi avoir une fin.

J'espère que vous avez apprécié apprendre tout sur les fonctions, toutes les choses sur les fonctions.

Certaines d'entre elles à un niveau très élevé.

Certaines d'entre elles en profondeur.

Mais le but de ce cours était de faire un cours intensif où nous pouvons passer en revue tous les aspects des fonctions JavaScript et vous donner une idée, vous donner la confiance que vous pouvez apprendre certains de ces concepts si vous apprenez de manière incrémentale, si vous apprenez en reliant les points.

Donc nous avons commencé par des choses très basiques comme comment créer une fonction et nous avons terminé par la récursivité, entre-temps nous avons abordé la fonction imbriquée, la portée de la fonction, la fermeture, la fonction de rappel, toutes ces différentes facettes.

Mais votre apprentissage ne doit pas s'arrêter là.

Vous devez continuer à pratiquer chacun de ces concepts beaucoup plus en profondeur avec vos mains.

Et j'ai des vidéos pour certains de ces concepts pour enseigner de manière beaucoup plus approfondie.

Par exemple, le rappel, la fonction pure, HOF, vous savez, beaucoup de ces choses ont des vidéos de cas d'utilisation en profondeur dans la vie réelle.

Veuillez aller les regarder si vous êtes intéressé ou si vous voulez les lire quelque part ou sur une autre chaîne YouTube.