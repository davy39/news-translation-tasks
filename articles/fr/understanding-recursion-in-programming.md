---
title: Comprendre la récursivité en programmation
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-19T13:56:48.000Z'
originalURL: https://freecodecamp.org/news/understanding-recursion-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/recursion.png
tags:
- name: Recursion
  slug: recursion
- name: youtube
  slug: youtube
seo_title: Comprendre la récursivité en programmation
seo_desc: 'In one sense, recursion is simple.

  In fact, most of what you need to know about recursion can be summed up in this
  gif:


  But the deeper you go, the harder it is to fully grasp. But it doesn''t have to
  be.

  We just published a full course on the freeCod...'
---

Dans un sens, la récursivité est simple.

En fait, la plupart de ce que vous devez savoir sur la récursivité peut être résumé dans ce gif :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/n4xUtpn---Imgur.gif)

Mais plus vous allez loin, plus il est difficile de tout comprendre. Mais cela n'a pas à être le cas.

Nous venons de publier un cours complet sur la chaîne YouTube freeCodeCamp.org qui vous aidera à comprendre la récursivité à un niveau conceptuel.

The Simple Engineer a développé ce cours. Il a créé de nombreux cours et est excellent pour expliquer des concepts complexes de manière facile à comprendre.

La récursivité est une technique puissante qui nous aide à combler le fossé entre des problèmes complexes résolus avec du code élégant. Ce cours décompose ce qu'est la récursivité, pourquoi vous voudriez et ne voudriez pas l'utiliser, et montre une variété d'exemples de la manière dont elle peut être utilisée.

Le cours explique la récursivité avec toutes sortes de structures de données, des animations, du débogage et une analyse de la pile d'appels pour obtenir une compréhension plus approfondie de ces principes.

Le code est écrit en Java, mais les principes s'appliquent à n'importe quel langage.

Voici tous les sujets abordés dans ce cours :

* Qu'est-ce que la récursivité ?
* Expliquer la récursivité via l'analogie du distributeur automatique de billets
* Expliquer la récursivité via l'analogie de la révision de dissertation
* Résumer ce qu'est la récursivité
* Pourquoi et pourquoi pas la récursivité
* Comprendre la pile d'appels
* Analogie de la pile d'appels
* Introduction à la récursivité avec les chaînes de caractères
* Explication de l'inversion de chaîne
* Animation de la pile d'appels pour l'inversion de chaîne
* Explication des palindromes
* Animation de la pile d'appels pour les palindromes
* Récursivité avec les nombres
* Explication de la conversion décimale en binaire
* Code et débogage de la conversion décimale en binaire
* Explication de la somme des nombres naturels
* Code et débogage de la somme des nombres naturels
* Algorithmes de division et conquête
* Animation et explication de la recherche binaire
* Explication de Fibonacci
* Animation de Fibonacci
* Explication et animation du tri fusion
* Code et débogage du tri fusion
* Listes chaînées
* Animation de l'inversion de liste chaînée
* Code et débogage de la liste chaînée
* Animation de la fusion de deux listes chaînées triées
* Code et débogage de la fusion de deux listes chaînées triées
* Arbres
* Animation de l'insertion d'une valeur dans un arbre binaire de recherche
* Parcours du code pour l'insertion d'une valeur dans un arbre binaire de recherche
* Animation de la pile d'appels pour l'insertion d'une valeur dans un arbre binaire de recherche
* Explication de l'impression de tous les nœuds feuilles
* Code et débogage de l'impression de tous les nœuds feuilles
* Graphes
* Animation de la recherche en profondeur
* Parcours du code pour la recherche en profondeur
* Optimisations de la récursivité
* Mémoïsation et mise en cache
* Récursivité en fin de appel
* Conclusion

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=IJDJ0kBx2LM) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=IJDJ0kBx2LM]

## Transcription

(générée automatiquement)

Lorsque vous apprenez la récursivité, cela peut sembler que vous revenez toujours au début.

Dans ce cours, l'ingénieur simple vous aidera à comprendre la récursivité en utilisant des animations, des processus de pensée, et plus encore.

Hey, les gars, et bienvenue dans une autre vidéo présentée par l'ingénieur simple.

Dans la vidéo d'aujourd'hui, nous allons plonger profondément dans les profondeurs de la récursivité, et renforcer votre modèle mental algorithmique autour de ce paradigme de programmation en examinant une variété d'exemples et d'animations différents.

Alors, commençons tout de suite.

La première question à laquelle nous devons répondre sur la récursivité est : qu'est-ce que la récursivité ? Et je pense que la meilleure façon d'en parler est à travers cette analogie, et imaginons que vous êtes assis en ligne en attendant de retirer de l'argent d'un distributeur automatique de billets.

Et pour les besoins de cet exemple, supposons que ceci est vous et vous avez cette question, cette question sous-jacente.

Et vous voulez savoir combien de personnes se tiennent devant vous dans cette ligne.

Et cette sorte de version itérative brute force de vous dit, eh bien, ce que je peux faire, c'est sortir de la ligne, je pourrais courir à l'avant, et je pourrais peut-être compter un par un.

Et peut-être que je stocke ces comptes dans un carnet auxiliaire, vous savez, une variable externe que vous pouvez imaginer, et ensuite vous parcourez cette ligne, et vous revenez et vous dites, d'accord, j'ai ma réponse.

Mais j'ai fait beaucoup de travail.

Et nous voulons changer ce paradigme, nous voulons penser, comment puis-je être paresseux ? Quel est le moins de travail que je peux faire, et diviser ce problème en une sorte de sous-structure ? Et donc ce que je fais bien, je tape sur l'épaule de cette fille devant moi, et je lui pose une question très simple, je dis, hey, quel est ton numéro ? Et elle se retourne et me regarde et dit, vous savez, je suis désolée, je ne sais pas vraiment.

Mais ce que je vais faire, c'est que je vais demander à la femme devant moi.

Et ce qui se passe, c'est que ce processus continue, et il continue jusqu'à ce que nous atteignions une certaine condition d'arrêt.

Et cette condition à laquelle nous nous arrêtons est lorsque nous atteignons cette femme, et elle tape sur l'épaule de ce gars.

Et il dit, elle dit, hey, quel est ton numéro dans la ligne ? Et il donne cette réponse.

Et il est le numéro un.

Et c'est intéressant, n'est-ce pas ? Parce que c'est une sorte de condition d'arrêt à ce problème que nous résolvions.

Et ce qu'elle fait, c'est qu'elle prend ce numéro, et elle dit, eh bien, s'il était le numéro un, alors je suis essentiellement un plus un, parce que je me compte.

Et ce gars dit, eh bien, si elle était le numéro deux, alors je suis un plus ce qu'elle était, et cette idée se déroule en arrière jusqu'à la personne qui a posé la question à l'origine.

Et cette femme dit essentiellement au gars, hey, il y avait, vous savez, 10 personnes devant moi, je me compte.

Et maintenant je suis à 11.

Et il s'avère que nous pouvons modéliser ce problème avec ce plan simple, nous posons la première question, quel est le moins de travail que je peux faire ? Comment puis-je diviser ce problème en un sous-problème ? Et la deuxième question que j'ai est, quand le processus serait-il terminé ? Comme, quelle est ma condition d'arrêt.

Et dans ce cas, c'est lorsque nous atteignons la première personne dans la ligne, qui est le gentleman qui retire de l'argent du distributeur automatique, il se trouve que nous pouvons écrire ce problème dans un code très simplifié, minimal et beau.

Et la fonction que nous avons est simplement cette fonction get my position in line.

Et nous avons cette sorte d'abstraction d'une personne que nous avons.

Et remarquez les valeurs de retour en entier.

Et, encore une fois, si nous réfléchissons à ces deux questions que nous avons pour ce plan, nous disons si la personne suivante dans la ligne est nulle, alors nous devons être la première personne dans la ligne.

N'est-ce pas ? C'est une sorte de cas de base, imaginez que personne n'est dans la ligne, eh bien, alors vous êtes probablement la première personne dans la ligne.

Maintenant, si nous ne satisfaisons pas cette condition, alors que faisons-nous, nous faisons juste un peu de travail, nous disons, je vais me compter comme quelqu'un qui contribue au nombre de personnes dans la ligne.

Et je vais ajouter cet appel récursif, et j'appelle moi-même.

Et c'est la propriété intéressante de la récursivité, nous nous appelons nous-mêmes.

Mais le paramètre sur lequel nous conditionnons nous fait en réalité progresser vers le problème que nous essayons de résoudre.

Et donc je ne passe pas le même objet personne dans la fonction à nouveau, je passe en réalité une personne qui me fait progresser un peu plus près de la question que je pose, qui est, combien de personnes sont devant moi.

Et c'est vraiment tout ce qu'est la récursivité, comment puis-je prendre un grand problème et le diviser en un tas de sous-problèmes de sorte que chaque invocation de ma méthode me rapproche un peu plus du problème que j'essaie de résoudre ? Pensons à un autre exemple.

Revenons aux jours d'école où vous écriviez un tas de dissertations et typiquement ce processus, au moins pour moi, c'est vous savez, vous écrivez donc vous l'avez soumis à votre professeur et il dit, hey, vous savez, cette dissertation était terrible, je veux que vous alliez faire des révisions.

Et la dissertation est renvoyée à l'étudiant.

Et ce processus peut en fait continuer encore et encore, vous écrivez une dissertation, vous faites des révisions, vous la soumettez, elle est refusée, et vous recommencez.

Et vous faites cela jusqu'à ce que le professeur dise, d'accord, c'était bien, je vais la mettre dans ma serviette et commencer à la noter.

Et il se trouve que cela, encore une fois, est une sorte de stratégie récursive qui peut être développée.

Si nous regardons un simple morceau de code.

Et ce que nous faisons, nous regardons une dissertation, nous la révisons, nous la lisons, nous obtenons des commentaires dessus, nous y apportons des modifications.

Et puis remarquez, nous nous appelons simplement nous-mêmes à nouveau, n'est-ce pas.

Et il y a un cas de base unique caché ici.

Et nous le faisons jusqu'à ce que la dissertation soit complète.

Et remarquez que chaque invocation est le même objet de dissertation.

Mais ce que nous avons fait, c'est que nous avons avancé un peu plus vers cet objectif, cet objectif de ne plus avoir besoin de révisions sur la dissertation.

Donc, tout le processus, encore une fois, juste pour le ré-emphasiser, est que nous faisons un peu de travail à chaque invocation de notre appel de méthode Intel, nous atteignons un cas de base, une condition d'arrêt qui dit, hey, vous n'avez plus besoin de continuer.

Donc, encore une fois, comme quoi est la récursivité, la récursivité n'est rien de plus qu'une méthode qui s'appelle elle-même et pour être plus précis, c'est généralement une méthode qui retourne une valeur, peut-être qu'elle ne le fait pas.

Mais elle est conditionnée par un paramètre, de sorte que lorsque vous atteignez une condition à un moment donné, vous pouvez en fait arrêter la récursivité, un cas de base, n'est-ce pas.

Et nous considérons ce morceau comme le cas de base, c'est la condition d'arrêt, de sorte que nous n'augmentons plus le nombre d'appels récursifs que nous stockons en mémoire.

Et ce morceau ici, c'est l'appel récursif.

C'est là que je fais une unité de travail, un petit sous-problème qui me rapproche ou me fait progresser vers l'objectif ou la question que j'essaie de résoudre.

Avant de plonger dans les intrications techniques de la récursivité, il est important que nous discutions de certains compromis.

Pourquoi voudrions-nous utiliser la récursivité ? Et pourquoi voudrions-nous éviter la récursivité ?

Et je pense qu'il y a des exemples valables pour les deux.

Et cela dépend vraiment de la situation.

Le premier avantage que je donnerai est qu'elle comble vraiment le fossé entre l'élégance et la complexité, nous allons examiner une variété de problèmes différents où nous parcourons des structures de données complexes comme les arbres et les graphes.

Et cela se résume vraiment à trois ou quatre lignes de code.

Et cela est très différent de faire quelque chose comme cela, dans cette approche impérative, où nous regardons les choses avec beaucoup de boucles et beaucoup de variables.

Et cela peut devenir très désordonné très rapidement, avec des structures de données qui sont intrinsèquement récursives.

Maintenant, du côté négatif, vous savez, ajouter un tas d'appels de méthode sur la pile d'appels entraîne une certaine surcharge du CPU, n'est-ce pas, il y a une certaine lenteur, avec l'appel de méthodes dans votre code par rapport à l'itération à travers une boucle.

Et cela, encore une fois, est un autre compromis que vous devez faire, cela peut être un compromis temps ou espace que vous devez considérer.

Maintenant, j'ai brièvement abordé cela, mais encore une fois, comme la récursivité peut réduire le besoin de boucles complexes et de structures de données auxiliaires.

La récursivité a cette sorte de pile implicite, qui est une structure de données couramment utilisée dans beaucoup d'algorithmes.

Et donc avoir cette sorte de pile implicite et une sorte de structure de boucle auto-gérée, elle vous est donnée comme une partie des appels récursifs, vous pouvez exploiter cette propriété pour vraiment simplifier votre code et vous concentrer sur le problème que vous résolvez.

Maintenant, l'inconvénient est que lorsque vous augmentez le nombre d'invocations de méthode dans la mémoire de votre ordinateur, vous pouvez en fait manquer de mémoire.

Et nous allons examiner de nombreux exemples pour comprendre pourquoi c'est le cas, et nous allons commencer à explorer cette idée d'une exception de dépassement de pile.

Et c'est là que nous commençons à manquer de la mémoire tampon pré-allouée que nous avons pour notre programme, ce qui peut en fait faire planter votre programme.

Il y a beaucoup d'avantages en matière de récursivité lorsqu'il s'agit d'optimisation, de réduction de la complexité temporelle.

Et c'est ce que cette idée de mémoïsation, et nous allons examiner quelques exemples de mémoïsation et de mise en cache, pour aider à accélérer les appels redondants.

Et c'est une propriété magnifique de la récursivité.

Maintenant, l'inconvénient, encore une fois, comme pour tout morceau de code, est que si la récursivité est trop utilisée, vous pouvez tomber dans cette sorte d'habitude où vous commencez à développer un code vraiment complexe, si ce n'est pas bien instruit, et vous voulez vous assurer que et ce que nous allons devenir beaucoup meilleurs à cela au fur et à mesure que nous allons avancer dans ce tutoriel, c'est lorsque vous regardez des problèmes, vous voulez vous demander, est-ce un bon cas d'utilisation ? Pour la récursivité ? Puis-je vraiment le diviser en sous-problèmes qui ont du sens pour la récursivité ? Si vous ne pouvez pas, alors vous pouvez tomber dans cet inconvénient où vous avez un code inutilement complexe.

Maintenant, la dernière chose, comme je l'ai mentionné auparavant, est que la récursivité fonctionne vraiment bien pour les structures de données définies de manière récursive, les objets JSON, les arbres, les graphes, des choses qui vous permettent de vous concentrer sur une minuscule unité de la structure de données à la fois.

Et il se trouve que nous allons examiner un tas d'exemples différents pour comprendre pourquoi cela est vrai.

Mais ce n'est qu'un petit ensemble de pros et de cons, des choses à considérer lorsque vous pensez à utiliser la récursivité.

Cela nous amène à un sujet que je pense souvent négligé lors de l'enseignement de la récursivité, que je pense être l'un des concepts fondamentaux que vous devez vraiment comprendre pour comprendre ce que les gens appellent citation, magique à propos de la récursivité.

C'est juste magique avec la façon dont cela fonctionne.

Et après avoir examiné cet exemple, nous commencerons à réaliser à quel point la récursivité est logique et pourquoi ce n'est pas nécessairement une chose si magique.

Imaginons que vous alliez travailler un jour, et la première chose que vous voulez faire est de vérifier vos e-mails.

Et en vérifiant vos e-mails, vous êtes interrompu par votre patron, et votre patron dit, hé, j'ai besoin que vous alliez assister à une réunion.

Et vous devez en fait vous écarter de votre tâche.

Donc vous ne terminez pas de vérifier vos e-mails, vous êtes interrompu.

Et avant de pouvoir vérifier vos e-mails, maintenant vous devez assister à cette réunion.

Maintenant, disons que votre patron, eh bien, entrez dans cette réunion, votre patron vous interrompt à nouveau.

Et il dit, hé, nos investisseurs visitent, j'aimerais que vous alliez à cette réunion du conseil et que vous les impressionniez avec toutes vos connaissances.

Et donc encore une fois, nous allons entrer dans cette réunion, vous êtes interrompu, vous devez aller impressionner les investisseurs.

Oui, c'est votre prochaine tâche.

Et donc avant de pouvoir assister à la réunion, avant de pouvoir vérifier vos e-mails, vous devez impressionner ces investisseurs.

Et enfin, votre patron, il vous interrompt à nouveau.

Et il dit, hé, vous savez, je suis désolé.

Mais j'ai besoin que vous alliez aider Jake avec son code, son code échoue.

Et nous devons pousser vers la production.

Donc maintenant vous devez essentiellement éviter la réunion des investisseurs, éviter la réunion initiale, vous ne pouvez pas vérifier vos e-mails jusqu'à ce que vous aidiez le code de j.

Une fois que vous l'avez aidé, cette chose est en quelque sorte retirée de votre liste de choses à faire, vous savez, vous allez à la réunion du conseil, vous assistez à cette réunion originale.

Et puis enfin, vous pouvez vérifier vos e-mails.

Et vous vous demandez peut-être, comme, pourquoi est-ce que cela est pertinent pour la récursivité.

Et il se trouve que cette sorte d'idée est exactement comment la pile d'appels fonctionne lorsque nous parlons d'invoquer des méthodes dans nos programmes.

Jetons un coup d'œil à ce simple programme ici.

Remarquez que nous avons trois appels de méthode.

Et ils sont en quelque sorte enchaînés ensemble.

Le premier retourne une chaîne, mais il dépend de B, B retourne une chaîne, mais il dépend de C.

Et c juste retourne une chaîne.

Donc rien de fantaisiste du tout.

Maintenant, la pile d'appels va être cette sorte d'abstraction que notre système d'exploitation utilise pour stocker les invocations de méthode dans notre programme.

Elle nous permet de comprendre à quelles adresses mémoire nous retournons les données, et elle stocke les informations des variables locales, comme quels sont les paramètres qui m'ont été passés.

Donc si nous exécutons a, la première chose qui va sur la pile d'appels est cette sorte d'idée connue sous le nom de cadre de pile.

Et il dit essentiellement, hé, je veux appeler Hello, et je veux concaténer le résultat de B.

Mais pour que je puisse concaténer le résultat de B, je dois en fait maintenant appeler B.

Donc cela pousse B sur la pile d'appels.

Maintenant je suis dans le même scénario, où je veux maintenant retourner de B, mais j'ai une dépendance sur C.

Donc maintenant j'appelle C et je le mets sur la pile d'appels.

Et remarquez que c'est le même type de processus que nous avons vu dans l'analogie précédente.

Je ne peux pas retourner ou retirer ces choses de la pile jusqu'à ce que je suive l'ordre dans lequel ces choses ont été appelées.

Donc je retourne friends, n'est-ce pas.

Et maintenant friends remplace cette invocation de see.

Et donc maintenant cela a été complètement évalué.

Et donc maintenant puisque B est complètement évalué, je peux retourner cette valeur à l'invocation de la méthode B.

Et maintenant ce cadre de pile B est retiré de la pile.

Et ce n'est qu'à ce moment-là que j'ai maintenant évalué toute cette chaîne d'appels de méthode.

Donc maintenant je peux retourner cette valeur de chaîne.

Et obtenir ma sortie attendue.

Maintenant, vous vous demandez peut-être, comme pourquoi encore ? Pourquoi est-ce pertinent pour la pensée récursive.

Et regardons un exemple.

Regardons une pile d'appels lorsque nous appelons ces appels récursifs, n'est-ce pas ? Ce n'est qu'un programme qui s'appelle lui-même et il s'exécutera pour toujours, n'est-ce pas ? Donc la première fois que j'invoque a, maintenant j'ai besoin d'invoquer a, mais il appelle a à nouveau.

Et cela continue, n'est-ce pas ? Il n'y a pas de condition d'arrêt.

Et finalement, il y aura ce point, ce point dans le temps où j'essaie d'invoquer a à nouveau, et j'obtiens, j'obtiens une erreur, et cette erreur est un dépassement de pile.

Et cette exception se produit lorsque nous dépassons le tampon de mémoire pré-alloué que notre programme a.

Oui, nous avons essentiellement épuisé la mémoire, nous avons dépassé la pile, et nos invocations ont débordé, et nous ne pouvons plus les gérer.

Et c'est toute l'histoire avec la récursivité, pourquoi nous avons besoin d'un cas de base, nous devons retourner une valeur.

Donc, comme nous l'avons vu précédemment, pour les méthodes qui ne sont pas récursives, nous avons remarqué que les cadres continuent de croître et de croître et de croître.

Et la seule façon pour que ces cadres diminuent en taille est qu'ils retournent une valeur, qu'ils cessent d'invoquer des méthodes.

Et il en va de même pour la récursivité.

La seule différence est que nous avons une sorte de cas de base, quelque chose qui dit, hé, c'est la seule chose sur laquelle je veux conditionner pour nous éviter de continuer à récurser.

Je veux commencer la première composante technique de cette présentation en regardant la récursivité avec les chaînes de caractères.

Et cela va nous donner une très bonne idée de la manipulation des paramètres d'entrée sur la pile d'appels de manière récursive.

Et le premier problème que je veux examiner est cette idée d'inversion de chaîne.

Et donc ce que nous faisons, c'est que nous avons une chaîne d'entrée comme le symbole ingénieur.

Et l'idée est que la sortie serait l'entrée dans l'ordre inverse, n'est-ce pas ? Et donc la question est, comment faisons-nous pour construire une fonction récursive vraiment concise qui nous donne quelque chose comme cela.

Et comme nous regardons, comme nous regardons la structure squelettique de ce code, nous allons bien sûr avoir une sorte d'entrée, n'est-ce pas ? Donc l'entrée va être une chaîne, et la sortie va être la version inversée de celle-ci.

Et donc nous posons toujours ces deux questions.

La première est, quel est le cas de base ? Et cela demande vraiment, quand puis-je ne plus continuer dans mon algorithme ? Et la ligne de code suivante va être tout sur la plus petite quantité de travail que je peux contribuer ? Donc dans ce cas, cela va être essentiellement entre chaque invocation, quelle est la petite unité que je peux modifier ou manipuler pour progresser un peu plus près de l'objectif ? Alors regardons la première question.

La première question est de dire, quand puis-je ne plus continuer ? Et je pense que lorsque vous pensez à ce genre de scénario, il y a deux écoles de pensée.

Et lorsque j'aime construire des cas de base, je pense généralement si je devais simplement passer une très petite entrée, comme quelle est la plus petite entrée que je pourrais simplement passer pour commencer cette fonction, où je devrais essentiellement retourner immédiatement.

Et il pourrait y avoir deux écoles de pensée avec cette approche, n'est-ce pas ? Et les deux écoles de pensée pourraient être, eh bien, une lettre inversée est elle-même, n'est-ce pas.

Et cela pourrait être un très, très bon cas de base pour l'inversion de chaîne.

Mais nous voulons être encore plus paresseux.

Comme, quelle est la chose la plus paresseuse, la plus petite quantité de travail que je pourrais même considérer penser.

Et ce serait la chaîne vide, la chaîne vide inversée, est à nouveau, juste la chaîne vide.

Et donc si je passais la chaîne vide à cette fonction, il serait logique de ne recevoir que la chaîne vide en retour.

Et donc si nous, si nous modifions le code, et que nous regardons cela, nous avons juste un simple cas de base où nous évaluons si la chaîne d'entrée est la chaîne vide, alors retournons simplement la chaîne vide.

Mais maintenant nous devons considérer comment puis-je même arriver à ce point ? Quelle est la plus petite quantité de travail que je peux contribuer ? N'est-ce pas ? Et c'est la question que nous posons ici.

J'ai besoin de faire quelque chose qui réduit l'espace de décision dans chaque appel récursif.

Et donc nous posons cette question, quelle est la plus petite unité avec laquelle je peux traiter dans une chaîne ? Une chaîne est juste un tas de caractères, n'est-ce pas ? Et donc peut-être que je peux modifier un seul caractère.

Et c'est là que nous arrivons à cette question.

Laissez-moi choisir un seul caractère dans cette chaîne.

Et peut-être que là où je le positionne permettra qu'il soit concaténé depuis la pile d'appels dans l'ordre inverse.

Et il s'avère que lorsque nous écrivons ce code, nous obtenons un appel récursif où nous prenons ce premier caractère de la chaîne d'entrée et nous le concaténons après l'appel récursif, et vous pouvez regarder cela et dire, d'accord, eh bien, le paramètre d'entrée a changé.

Et il a changé parce que nous avons en fait réduit l'espace de décision, nous avons réduit cette chaîne d'entrée, parce que notre objectif entier est de nous rapprocher de ce cas de base, n'est-ce pas.

Et donc nous avons pris tout ce qui est directement après le premier caractère jusqu'à la fin.

Et l'idée est que si nous faisons cela suffisamment de fois, nous pouvons réduire notre espace de recherche à chaque invocation et atteindre l'objectif, qui est la chaîne inversée.

Donc cette première partie est entièrement axée sur la réduction de l'espace du problème.

Et la deuxième partie reflète vraiment le travail que nous faisons pour contribuer à nous rapprocher de l'objectif.

Et je pense qu'il est utile d'analyser ce qui se passe sur la pile d'appels.

Donc disons que nous passons Hello.

Et nous ne rencontrons pas le cas de base, à la ligne deux, nous allons immédiatement à la ligne six, qui est essentiellement l'invocation récursive avec la sous-chaîne réduite.

Et puis nous concaténons le H.

Et comme nous l'avons discuté avec les piles d'appels, nous ne pouvons pas retirer cela de la pile d'appels jusqu'à ce que cet appel récursif ait également été complété, ce qui ajoute un cadre de pile supplémentaire à la pile d'appels.

Et vous remarquez, encore une fois, nous ne rencontrons pas le cas de base, et nous réduisons cette chaîne d'entrée, mais nous concaténons le premier caractère.

Et nous continuons à faire cela.

Et c'est bien, car je n'ai pas besoin de garder une trace du H, je n'ai pas besoin de garder une trace du E.

C'est tout géré automatiquement pour moi dans le cadre de la pile sur la pile d'appels.

Et donc j'invoque à nouveau la chaîne inversée.

Et maintenant j'obtiens Oh.

Et maintenant, cela devient assez intéressant, car lorsque je passe Oh, j'arrive à un point où ma chaîne d'entrée a été réduite à juste la chaîne vide.

Et il se trouve que pour ce cas d'utilisation, c'est le cas de base.

Donc je retourne la chaîne vide.

Donc cette chaîne inversée est évaluée à la chaîne vide à partir de ce cas de base, et je finis par simplement retourner la chaîne vide plus Oh.

Et maintenant cet appel récursif est évalué.

Et maintenant j'ajoute L.

Et cela devient simplement o l, n'est-ce pas.

Et donc maintenant je peux retourner cela.

Et cela est retiré de la pile d'appels.

Et maintenant vous pouvez voir que je retourne essentiellement ces valeurs au cadre de pile qui m'a précédé.

Et je retire les choses de la pile d'appels.

Cette fonction est évaluée en ADS II.

Donc je la retourne et je la retire de la pile d'appels.

Cette fonction est évaluée à o Ll E.

Donc je la retourne, elle est évaluée.

Et puis cela est retiré de la pile d'appels.

Et comme vous pouvez le voir, c'est l'objectif, n'est-ce pas ? C'est la chaîne inversée.

Et c'est le pouvoir de la pile d'appels, le pouvoir de ces appels récursifs qui nous permettent de retourner des valeurs vers le bas de la pile.

Et c'est une très bonne propriété que nous pouvons exploiter lorsque nous utilisons la récursivité.

Regardons les palindromes, ces mots uniques où nous pouvons épeler le même mot en avant et en arrière.

Regardons ce mot.

La manière mécanique dont nous analysons si un mot est un palindrome ou non, est que nous regardons les deux extrémités.

Et nous disons essentiellement, d'accord, ces lettres correspondent-elles ? Oui, elles le font.

Donc nous réduisons le mot, nous disons, ces lettres correspondent-elles ? Oui, elles le font.

Donc nous réduisons le mot.

Et maintenant ce n'est qu'un seul caractère.

Et cela prouve que nous avons réussi à faire correspondre.

Donc cela serait effectivement un palindrome.

Maintenant, regardons un extrait de code pour voir comment nous pourrions penser à quelque chose comme cela de manière récursive.

Maintenant, évidemment, nous allons avoir une fonction booléenne, car c'est soit oui, c'est un palindrome, soit non, ce n'est pas.

Et nous allons évaluer une chaîne d'entrée.

Et bien sûr, la première chose que nous considérons toujours est, quel est ce cas de base, la chose qui nous empêche de récurser ? Maintenant, rappelez-vous ce que j'ai dit dans l'exemple précédent, j'aime toujours considérer mes cas de base, quelle est la plus petite entrée que je pourrais simplement passer à cette fonction ? Et il s'avère très souvent, pas très souvent, pour la récursivité de chaîne, vous pouvez généralement réduire votre espace de recherche et évaluer la longueur de l'entrée.

Donc si vous passiez un palindrome de taille zéro, alors c'est un palindrome, n'est-ce pas ? Parce qu'il n'y a rien qui prouve que ce n'est pas un palindrome.

Il n'y a pas de caractères à comparer.

Et dans la même veine, si nous passons juste un seul caractère, avec un seul caractère, avant et arrière est le même caractère.

Donc c'est aussi un palindrome.

Donc ce sont de très bons cas d'utilisation, ou cas de base pour évaluer cette condition, qui est de savoir si une chaîne est un palindrome ou non.

Mais continuons, nous devons considérer la petite quantité de travail que nous pouvons faire.

Et dans l'animation que nous venons de regarder, vous remarquez que nous avions deux pointeurs, un à gauche et un à droite, et nous comparions ces chaînes, ces caractères, nous disions qu'ils devaient être les mêmes.

S'ils ne sont pas les mêmes à un moment donné, alors nous avons violé la propriété d'un palindrome.

Et si nous violons la propriété du palindrome, alors nous allons simplement à ce faux.

C'est une sorte de cas de base de repli.

Donc à tout moment dans l'algorithme, si les caractères ne correspondent pas à leurs indices opposés respectifs, alors nous pouvons terminer, nous retournons false et le false se propage à travers la pile d'appels.

Et la fonction de couleur initiale retournerait le false.

Mais si ce n'est pas le cas, alors nous arrivons à cette chose intéressante, où nous appelons cet appel récursif, et il réduit ou soustrait notre sous-chaîne.

Donc regardons la pile d'appels pour comprendre ce qui se passe.

Nous passons race car comme chaîne d'entrée.

Et cela, bien sûr, est un palindrome, vous pouvez voir race car avant et arrière, c'est juste race car.

Et la première chose que nous faisons est que nous évaluons cette condition, ce cas de base, la longueur est-elle zéro ou un ? Eh bien, ce n'est définitivement pas le cas.

Donc nous continuons.

Et maintenant nous comparons le premier caractère et le dernier caractère pour cette chaîne d'entrée.

Et s'ils sont égaux, alors nous nous appelons simplement à nouveau, mais nous réduisons cette chaîne d'entrée.

Et puisque ces, puisque R et R sont égaux, nous ajoutons un autre cadre de pile à la pile d'appels.

Et nous avons réduit notre chaîne d'entrée, nous regardons à nouveau le cas de base, nous ne le satisfaisons pas.

Donc nous comparons le premier et le dernier caractère.

Et nous remarquons dans ce cas, qu'ils sont aussi égaux.

Donc nous nous appelons à nouveau, n'est-ce pas, et nous ne retirons pas le cadre de pile de la pile d'appels, car nous avons encore du travail à faire.

Et donc nous réduisons notre chaîne d'entrée, nous n'avons toujours pas satisfait le cas de base.

Et nos caractères aux première et dernière positions sont toujours les mêmes.

Donc nous faisons juste un peu plus de travail.

Et maintenant nous sommes au dernier caractère.

Et nous sommes déjà arrivés à cette conclusion que si la longueur de l'entrée est zéro ou un, alors nous retournons simplement vrai.

Donc pour ce sous-problème particulier, cet élément particulier, c'est effectivement un palindrome.

Donc que faisons-nous, nous disons, oui, c'était un palindrome et nous le retirons de la pile d'appels.

Et puisque nous retournons vrai, et que toutes ces autres conditions ont été satisfaites, nous pouvons simplement propager le booléen vrai à travers la pile d'appels.

Donc nous retournons vrai ici et nous retirons cela.

Nous allons au cadre de pile suivant et nous retournons vrai ici et nous retirons cela.

Et maintenant nous arrivons au cadre de pile final, qui est évalué à vrai.

Et cela est retiré de la pile.

Maintenant, je veux regarder la récursivité avec les nombres.

Et la chose que vous allez commencer à réaliser lorsque nous passerons en revue ces types de problèmes, c'est que le même plan s'applique à tous.

Et le premier problème que je veux examiner est cette idée de convertir des valeurs décimales de base 10 en binaire, qui est un format de nombre de base deux, des uns et des zéros.

Donc la question est, comment pouvons-nous convertir un nombre comme 25 en son équivalent binaire.

Et il s'avère qu'il y a une manière très mécanique de faire cela.

Donc prenons le nombre 233.

Et la formule ici, comme nous allons le découvrir, est que nous pouvons faire une division par deux et cela fait essentiellement l'opérateur de plancher.

Donc cela nous donne un entier au lieu d'une valeur à virgule flottante.

Et nous obtenons une sortie, qui est 116.

Et nous avons un reste, et ce reste est un.

Et le processus mécanique que nous pouvons suivre pour convertir le décimal en binaire est que nous prenons les résultats de cette opération, qui est 116.

Et nous le divisons par deux.

Et nous continuons simplement à évaluer, et cela donne 58, reste zéro, puis nous prenons 58.

Et nous le divisons par deux, et cela donne 29, reste zéro.

Et nous prenons essentiellement le résultat dans la sortie et nous le divisons par deux.

Et remarquez que nous gardons une trace des restes ici.

Et la propriété intéressante en faisant ces opérations nous amène à un point où nous pouvons prendre tous ces restes.

Donc remarquez, nous sommes arrivés à ce cas de base, qui est zéro.

Et cela arrête en quelque sorte cette progression.

Donc maintenant nous avons terminé.

Et si nous prenons tous ces restes, dans l'ordre où ils ont été essentiellement poussés sur la pile, nous pouvons les évaluer et c'est le résultat en chaîne binaire pour 233.

Et la question est, comment pouvons-nous, ce processus mécanique, vous savez, très formulaire ? Comment pouvons-nous le convertir en une sorte d'opération récursive ? Regardons un peu de ce code.

Maintenant, remarquez, nous avons dit la première chose est que nous avons pris 233 divisé par deux, nous avons obtenu une sortie, le reste était un.

Et donc il y a en fait de nombreuses façons de faire ce problème.

Et nous allons le garder très simple.

Donc remarquez que nous traitons avec des chaînes.

Comme les résultats de sortie, nous allons simplement concaténer des chaînes.

Et donc ce que nous considérons ici, c'est que nous pensons à ce cas de base, n'est-ce pas ? Si j'atteins zéro, alors il n'y a plus de raison pour moi de diviser davantage, n'est-ce pas, je retourne mon résultat.

Maintenant, si je n'ai pas encore atteint zéro, cela signifie que j'ai encore plus de divisions à faire.

Et donc la première chose que nous faisons est que nous obtenons ce reste.

Donc lorsque nous regardons 233, divisé par deux, nous voulons stocker ce reste car il représente l'un des chiffres binaires qui nous intéressent, il nous indique essentiellement si la valeur est paire ou impaire.

Et c'est le binaire, c'est le reste qui contribuera au résultat.

Et c'est pourquoi nous le stockons dans le résultat.

Et remarquez, nous le plaçons simplement au début du résultat.

Et maintenant, ce que je fais, c'est que je fais simplement un appel à find binary et je réduis mon espace de problème de moitié.

Et je propage simplement le résultat à travers.

Maintenant, regardons la pile d'appels.

En codant cela.

Et en voyant à quoi cela ressemble, je veux prendre le code que nous venons de regarder, mais le regarder du point de vue de la pile d'appels et comprendre comment ces cadres de pile se construisent au fil du temps.

Maintenant, il y a de nombreuses façons de coder cette fonction find binary.

Et beaucoup de gens le font en retournant un entier.

Et c'est complètement bien.

Et si vous voulez le faire de cette manière, vous pouvez en fait suivre avec n'importe quelle modification de cela et analyser la pile d'appels avec moi.

Donc, lorsque nous exécutons en mode débogage, la pile d'appels va apparaître ici.

Donc ce sont tous les cadres de pile que nous pouvons voir grandir.

Et les variables du cadre de pile actuel vont apparaître ici dans local.

Et donc, lorsque nous plongeons dans cette fonction, vous remarquez que c'est le premier cadre de pile pour find binary.

Et pour que cela se termine, nous devons retourner une valeur.

Nous n'avons pas encore atteint notre cas de base.

Donc nous sautons dans notre travail.

Et nous faisons simplement un autre appel récursif.

Donc le premier cadre de pile ne peut pas encore être retiré, car nous allons invoquer nous-mêmes à nouveau.

Et une fois que nous le faisons, vous remarquez que nous ajoutons un autre cadre de pile.

Et remarquez également que les paramètres d'entrée ont changé.

Nous avons réduit notre espace de décision, et nous avons ajouté le premier chiffre à notre résultat binaire.

Nous n'avons pas encore atteint notre cas de base.

Et nous continuons.

Et encore, nous faisons une opération récursive.

Et notre espace de décision continue de diminuer.

Et c'est le même processus mécanique que nous avons vu dans l'animation, nous divisons par deux et enregistrons le reste, nous divisons par deux et enregistrons le reste.

Et nous faisons cela jusqu'à ce que nous atteignions une sorte de condition de base.

Oui.

Et lorsque nous réduisons notre espace de problème, remarquez que nous arrivons à ce point où le décimal est un.

Et ce n'est toujours pas notre cas de base.

Donc nous passons par là, nous obtenons le résultat.

Et cette chaîne binaire a l'air assez bien.

Dans l'appel récursif final, vous remarquez que le décimal est maintenant zéro.

Et c'est un très bon cas maintenant, car maintenant nous pouvons simplement retourner.

Donc nous venons ici et nous retournons cette valeur.

Et cette valeur vient et dit d'accord, find binary pour cette invocation a retourné ce résultat.

Et donc maintenant nous disons simplement, d'accord, continuez.

Et remarquez que lorsque je passe à travers, les cadres de pile ont grandi.

Mais maintenant ils devraient diminuer de la pile d'appels.

Donc je passe à travers.

Et remarquez qu'ils ont tous diminué, donc ils ont tous retourné, ils ont tous retourné une valeur.

Et maintenant, une fois que je passe par ici, nous avons remarqué que la valeur binaire a été évaluée, vous pouvez venir dans cette console de débogage et la regarder.

Et c'est la chaîne binaire résultante.

Et c'est bien de regarder comment la pile d'appels fonctionne pour comprendre.

D'accord, combien de cadres de pile construisons-nous pour obtenir notre résultat ? Et comment se déroulent-ils une fois que nous atteignons notre cas de base ici, nous avons simplement propagé le résultat à travers tous les cadres de pile, et ils retournent tous la même chose.

Et nous allons regarder beaucoup d'exemples différents où tous les cadres de pile travaillent ensemble.

Et ils attendent le résultat pour faire un peu plus de travail.

Et donc il y a beaucoup de versions différentes de cela.

Le problème suivant que je veux examiner avec les nombres est la somme des nombres naturels.

Et l'idée de ce problème est que vous prenez un nombre d'entrée comme 10, et ensuite vous additionnez toutes les valeurs jusqu'à 10.

Et ce que nous faisons ici, c'est que nous les additionnons toutes, et nous obtenons une sortie et la sortie dans ce cas serait 55.

Et la question est, comment pouvons-nous construire une fonction succincte qui fait cela de manière récursive ? Regardons un petit extrait de code et essayons de comprendre ce qui se passe en coulisses.

Donc, la somme récursive, encore une fois, nous prenons une valeur d'entrée.

Et la première question que nous devons poser est, quelle est la plus petite valeur d'entrée que je pourrais passer.

Donc si je passe un, par exemple, la somme de un à un est simplement elle-même.

Un, n'est-ce pas.

Et donc c'est un bon, c'est un bon endroit pour le cas de base.

Et encore une fois, gardez à l'esprit, nous simplifions ces fonctions.

Donc, vous savez, les cas limites, nous ne nous concentrons pas vraiment sur cela.

Oui, maintenant nous nous concentrons sur l'objectif principal, qui est de construire une fonction succincte.

Donc si je passe un, je retournerais un.

Maintenant, si je passe un nombre plus grand, comme 55, j'ai encore beaucoup de travail à faire, je dois additionner tous les nombres précédents jusqu'à 55 à partir de un.

Et donc ce que je peux faire, c'est que je peux prendre n'importe quelle valeur que je suis actuellement.

Et je peux l'ajouter à moi-même à nouveau, mais en soustrayant un de ce nombre, n'est-ce pas.

Donc cela me rapproche de ce cas de base.

Regardons à nouveau un peu de code et comprenons comment la pile d'appels fonctionne avec ce type de code.

Donc j'ai pris le même code de la diapositive.

Et maintenant nous voulons regarder la pile d'appels et comprendre ce qui se passe lorsque nous faisons ces appels récursifs.

La première chose que nous allons regarder est le nombre cinq, donc nous voulons additionner toutes les valeurs de un à cinq.

Mettons un point d'arrêt ici et déboguons dans la pile d'appels.

Donc lorsque je plonge dans cette opération, nous évaluons d'abord le cas de base, qui n'a pas encore été atteint.

Et donc maintenant ce que je veux faire, c'est que je veux prendre cinq, et je veux l'ajouter à un autre appel récursif, mais cette récursion réduit l'espace d'entrée à nouveau.

Et donc lorsque je plonge, remarquez que ce nombre d'entrée change.

Donc je fais l'appel récursif, et le nombre d'entrée a été réduit à quatre, et un autre cadre de pile a été ajouté à la pile d'appels.

Et donc nous continuons à évaluer, le conditionnel a-t-il été atteint ? Non, ce n'est pas le cas.

Donc je viens ici et cela se réduit à trois.

Et je continue à faire cela, et je viens ici.

Je viens ici.

Et maintenant le nombre d'entrée est un, le cas de base a-t-il été atteint ? Oui, c'est le cas.

Et donc si je plonge dans cela, vous remarquez que nous retournons un ici.

Et ce un retourne cette valeur au cadre de pile juste en dessous.

Et donc remarquez que lorsque je continue, ce cadre de pile est retiré.

Et vous pouvez voir que l'invocation de cette méthode a retourné un ici.

Et donc maintenant ce que je fais, c'est que je prends deux plus un, et je retourne cette valeur et cette valeur va continuer à se dérouler à travers ces cadres de pile.

Donc remarquez, tous ceux-ci sont retirés.

Et voici l'invocation finale, le nombre d'entrée est 10 ici.

Et lorsque nous continuons, cela évalue la somme récursive de 10.

Et donc maintenant encore, pour 10, nous arrivons à un cas de base.

Et ce cas de base est un.

Et si nous regardons, donc je vais mettre un point d'arrêt ici.

Et nous continuons, nous pouvons voir que nous avons les résultats de 15 et 55.

Et ceux-ci sont imprimés.

Et donc encore une fois, ce n'est qu'un exemple pour montrer que lorsque nous regardons les cadres de pile, comment un cadre de pile peut retourner une valeur au cadre de pile précédent pour terminer l'opération.

Et c'est la clé ici pour la récursivité.

Et nous allons continuer à faire cela pour beaucoup des problèmes que nous allons examiner pour nous familiariser avec le fonctionnement de la pile d'appels, et comment les cadres de pile grandissent.

Je veux parler des algorithmes de division et conquête, qui sont de très bonnes démonstrations de récursivité.

Et le plan que nous pensons pour diviser et conquérir tient bon, donc nous divisons un grand problème en plusieurs petits problèmes.

Mais diviser et conquérir consiste à les diviser en sous-problèmes.

Nous les résolvons indépendamment.

Et ensuite, nous fusionnons en fait les résultats pour résoudre un problème holistique, n'est-ce pas ? Nous les fusionnons ensemble et disons, hé, c'est la solution.

Et ils sont généralement récursifs.

Et regardons le premier, qui est la recherche binaire.

Et le but entier de la recherche binaire est que nous regardons une liste triée de nombres.

Et le point clé ici est qu'ils sont triés.

Et appelons cela un tableau.

Et la première chose que nous disons est que nous disons d'accord, je vais commencer avec les index gauche et droit, donc l'index le plus à gauche est zéro et l'index le plus à droite est la longueur du tableau moins un.

Et le but entier de la recherche binaire est de trouver une valeur, nous voulons trouver une valeur dans ce tableau.

Donc nous savons que zéro est inférieur à la longueur du tableau.

Donc nous n'avons pas encore atteint notre cas de base et nous calculons le point médian.

Donc le point médian est l'index gauche et droit additionnés ensemble et divisés par deux.

Et donc nous vérifions, nous disons, d'accord, est-ce que ce point médian est la réponse que nous cherchons ? Donc c'est une autre sorte de cas de base, avons-nous atteint ou trouvé le nombre 10 ? Ici ? Et la réponse est non.

Donc nous posons l'une de ces deux questions, la première question que nous posons est, est-ce que le nombre que nous cherchons est dans la moitié gauche du tableau, ou est-ce que le nombre que nous cherchons est dans la moitié droite du tableau.

Et rappelez-vous, nous venons de trouver le point médian, donc nous considérons tout à gauche et le point médian et tout à droite du point médian parce que les données d'entrée sont triées.

Maintenant, si c'est dans la moitié gauche, ce que nous regardons ici, alors nous rejetons complètement la moitié droite.

Et remarquez, la façon dont nous faisons cela est que nous changeons les limites du problème.

Donc la moitié gauche reste la même.

Donc notre point de départ à gauche reste le même, mais nous ne considérons que jusqu'au point médian moins un.

Et donc c'est notre capacité à réduire notre espace de décision et à rejeter complètement la moitié droite dans chaque récursion, ou chaque invocation récursive.

Maintenant, si nous arrivons à cette autre évaluation, cela signifie essentiellement que la valeur que nous cherchons est dans la moitié droite.

Et ce que cela nous permet de faire, c'est que nous ne considérons que notre point de départ pour être le point médian plus un jusqu'à la fin.

Donc nous rejetons complètement la moitié gauche pour le reste de ce problème.

Et cela est effectivement aussi un appel récursif.

Donc regardons le premier cadre de pile dans la pile d'appels à droite, nous commençons avec zéro, notre index de limite supérieure pour la variable droite est neuf.

Et le nombre que nous recherchons est 10.

Donc voici notre point médian, c'est trois.

Et nous avons posé cette question, est-ce la valeur que nous cherchons ? Est-ce 10 ? Et la réponse est non, ce n'est pas le cas.

Donc ce que nous pouvons faire, c'est que nous pouvons rejeter toute la moitié gauche de l'espace de recherche parce que 10 est supérieur au point médian.

Et il s'avère que nous ajoutons un autre cadre de pile à la pile d'appels et remarquez comment les paramètres ont changé.

Maintenant pour la gauche, la limite de départ, qui est la gauche est cinq, qui est l'index où se trouve quatre, et la limite supérieure est neuf, qui est la longueur originale du tableau avec lequel nous travaillons.

Et encore une fois, nous calculons le point médian, le point médian sur ce sous-tableau est neuf, et nous disons est-ce que 10 est supérieur à neuf ou inférieur à neuf.

Et bien sûr, nous savons que 10 est supérieur à neuf.

Et donc ce que nous pouvons faire, c'est rejeter complètement la moitié gauche de ce sous-tableau et continuer.

Et nous ajoutons un autre cadre de pile.

Et le cadre de pile, la limite de départ est huit et la limite supérieure est neuf.

Et nous recalculons le point médian.

Et le point médian à ce moment-là s'avère à la ligne sept, nous avons atteint ce cas de base, le cas de base ici est que nous avons trouvé le nombre que nous cherchions.

Et c'est la solution.

Et donc ce que nous pouvons faire, c'est simplement retourner cette valeur.

Mais nous n'avons pas encore terminé, car nous devons encore considérer la pile d'appels.

Et donc cette valeur est 10.

Et donc ce que nous faisons à partir de ce cadre de pile, c'est que nous retournons 10.

Et dans ce cas, nous retournons l'index auquel 10 est app.

Donc 10 est à l'index huit du tableau, et cela est retiré de la pile.

Et maintenant cette invocation de recherche binaire a été complétée, et elle obtient huit.

Donc elle retourne simplement huit.

Et cela est retiré de la pile.

Et maintenant enfin, nous retournons huit.

Et nous avons terminé.

Et le cadre de pile final est retiré de la pile.

Et c'est ainsi que fonctionne la recherche binaire.

Regardons Fibonacci, un problème mathématique et informatique classique qui démontre souvent la puissance de la récursivité.

Et nous allons examiner la version non optimisée ici.

Et nous ajouterons quelques optimisations à la fin.

Et regardons l'expression mathématique.

Tout d'abord, nous disons essentiellement que pour une certaine entrée à l'index n, elle sera composée de la somme des deux valeurs aux deux index qui la précèdent.

Regardons la page Wikipedia pour Fibonacci.

Et voici la séquence, la séquence de Fibonacci.

Et si nous prenons l'un de ces nombres comme 55, c'est la somme des deux nombres qui le précèdent, donc 34 et 21.

Et si nous regardons 34, c'est la somme de 21 et 13.

Et si nous regardons 13, c'est la somme de huit et cinq, etc.

Et cette formule est vraie pour toutes les valeurs de un à l'infini.

Et donc c'est la séquence de Fibonacci.

Donc si nous regardons cette expression à nouveau, maintenant nous avons ces cas de base en rose, et cela dit essentiellement que pour les valeurs aux index zéro et un, les cas de base sont zéro et un, effectivement, et nous pouvons simplement retourner à ce point.

Donc ce serait là où nous arrêterions cette récursion.

Et la pièce en jaune dit simplement que cela est vrai pour toutes les valeurs de un à l'infini.

Donc regardons cela et comprenons pourquoi cela diffère du précédent.

Maintenant, nous divisons et conquérons, n'est-ce pas, nous divisons ce problème, nous avons fib de n moins un qui doit se produire, nous l'ajoutons à fib de n moins deux.

Et ce sont deux appels récursifs.

Et comme nous y réfléchissons, comment fonctionne la pile d'appels, nous savons que la récursion à gauche doit se terminer avant même que nous envisagions de commencer l'appel récursif à droite.

Donc fib de n moins un pourrait avoir une tonne d'appels différents qui doivent se terminer avant même que nous fassions l'opérateur plus à fib de n moins deux.

Donc regardons comment cela s'animerait.

Donc nous voulons trouver le Fibonacci de cinq.

Et comme je l'ai dit, nous n'évaluons pas encore le côté droit de l'expression, car nous devons satisfaire cet appel récursif en premier.

Donc cela nous donne F, fib de cinq moins un, qui est quatre.

Et cela nous donne quatre moins un, qui est trois.

Et ce processus continue F de deux.

Et rappelez-vous notre cas de base, f de un est juste un, donc nous retournerions de ici.

Et maintenant, nous pouvons évaluer le côté droit de son opération récursive.

Rappelez-vous, nous appelons la même fonction encore et encore.

Donc maintenant nous avons atteint un cas de base, nous avons évalué le côté gauche, qui est fib de n moins deux, ou fib de n moins un.

Et maintenant nous pouvons faire fib de n moins deux pour cette valeur, qui est f de zéro.

Cela est à nouveau un cas de base.

Donc nous pouvons retourner de ici.

Maintenant, la somme de ces deux valeurs retourne et est transmise à F de trois.

Et maintenant F de trois peut évaluer son appel récursif sur le côté droit de cet opérateur plus.

Et encore une fois, nous faisons f de un, c'est un cas de base, donc nous le retournons simplement.

Oui ? Maintenant, ces F de deux, f de un s'additionnent pour retourner de F de trois, et cela est transmis à f de quatre.

Et maintenant F de quatre peut évaluer le côté droit de son expression, qui est f de n moins deux.

Donc ici nous obtenons F de deux.

Et encore une fois, cette propriété récursive est vraie, c'est un cas de base, nous le retournons, nous évaluons le côté droit, c'est un cas de base, nous le retournons.

Et maintenant cela se propage en arrière à F de quatre.

Et ces valeurs se propagent en arrière à F de cinq.

Et c'est à partir de là.

Maintenant, c'est le tout premier, vous savez, appel de la fonction, nous pouvons maintenant évaluer le côté droit de cet opérateur plus.

Et encore une fois, nous arrivons à f de trois, nous arrivons à f de deux, et puis c'est f de un.

Et c'est un cas de base.

Donc nous le retournons et c'est f de zéro, c'est un cas de base, nous le retournons.

Et remarquez, comme nous faisons la même chose encore et encore, cela est retourné.

Maintenant nous allons du côté droit, cela est retourné, cela est transmis.

Et maintenant nous pouvons additionner ces deux valeurs.

Et c'est ainsi que nous trouvons le Fibonacci.

Maintenant, nous allons regarder les optimisations pour cela plus tard.

Mais je veux juste souligner une chose, comme nous évaluons cela, remarquez, nous avons f de trois ici, nous avons f de trois ici.

C'est redondant, n'est-ce pas ? Tous les nœuds en dessous de F de trois sont exactement les mêmes.

Et donc il semble extrêmement gaspilleur, que nous recalculons ces valeurs.

Et donc comme nous allons le réaliser, il existe des optimisations que nous pouvons considérer pour éviter de recalculer quelque chose pour lequel nous avons déjà fait le travail.

Donc si vous regardez, nous avons f de deux, f deux et f de deux.

Et c'est trois nœuds.

Et vous pouvez imaginer pour des nombres vraiment grands, il s'avère que pour Fibonacci, vous savez, la plupart des ordinateurs modernes ne peuvent pas exécuter Fibonacci pour cette fonction avec une entrée très élevée.

Et c'est parce que les appels récursifs sont si intensifs.

Donc nous devons examiner certaines techniques d'optimisation connues sous le nom de mémoïsation.

Le tri fusion est cet enfant poster de la division et de la conquête lorsqu'il s'agit d'expliquer cela dans de nombreux cours d'informatique.

Et l'idée est que nous prenons un tas de valeurs non triées, comme les suivantes.

Et l'idée est que nous divisons ce tableau de telle sorte que nous continuons à diviser.

Et ensuite nous fusionnons les résultats triés pour trier ce tableau dans l'ordre croissant.

Et cela ressemble un peu à ceci.

Donc nous divisons le tableau en deux et nous disons, d'accord, je vais me concentrer sur le côté gauche.

Et rappelez-vous, avant même de faire le côté droit, je dois d'abord terminer le côté gauche, n'est-ce pas ? C'est l'ordre dans lequel la récursivité va opérer ici.

Et ce processus se maintient simplement.

Donc c'est le tableau de gauche et que fais-je, je le divise en deux.

Et maintenant je le décompose en deux parties.

Mais encore une fois, je dois d'abord me concentrer sur cette moitié.

Et ensuite je peux me concentrer sur cette moitié.

Donc je regarde, vous savez, je divise ceux-ci, et je regarde l'étranger un.

Et le cas de base ici est que vous ne pouvez pas vraiment trier une seule valeur.

Et donc je peux arrêter de diviser lorsque je n'ai qu'une seule valeur.

Et je compare ces deux, et je les fusionne et les trie ensemble avec un simple opérateur de comparaison.

Maintenant je peux regarder le côté droit, et je divise essentiellement ceux-ci.

Donc j'ai un entier ici, et je prends deux et zéro, et deux et zéro se divise encore plus.

Et encore une fois, je suis à ce cas où j'ai juste des chiffres, et donc zéro à comparer, ils sont fusionnés.

Maintenant trois a une comparaison linéaire, encore une fois, zéro et deux, et ceux-ci sont fusionnés ensemble.

Et maintenant nous prenons un et 402, et trois, ceux-ci sont fusionnés ensemble.

Et maintenant j'ai résolu la moitié gauche de ce tableau.

Mais rappelez-vous, maintenant je dois faire la moitié droite, nous évaluons dans l'ordre que la récursivité considérerait cela.

Donc lorsque nous divisons cela, j'obtiens la moitié droite du tableau.

Et je fais la même chose de ce côté.

Donc je prends ce tableau, je le divise, j'obtiens moins un et sept.

Cela se divise, je les compare.

Et il se trouve qu'ils étaient déjà dans l'ordre trié.

Donc ceux-ci sont remis à la même place.

Maintenant je prends la moitié droite du tableau, à droite, et je le divise encore plus.

Et donc lorsque cela se divise, j'ai 10, neuf et 20 se divise, neuf et 20 sont des chiffres individuels.

Et lorsque je les compare, ils sont déjà dans l'ordre trié.

Et puis je compare tous les chiffres ici, et ils sont fusionnés dans l'ordre trié.

Et puis encore, enfin, je compare ces chiffres, et ils sont fusionnés dans l'ordre trié.

Et cela nous amène à la fusion finale, rappelez-vous que diviser et conquérir consiste à diviser votre problème en sous-problèmes.

Et ensuite à fusionner les résultats ensemble.

Donc ce que nous avons fait, c'est que nous avons simplement fusionné de manière récursive tous les résultats ensemble à partir des sous-appels récursifs.

Et c'est la fusion finale.

Et juste pour souligner comment fonctionne cette comparaison pour s'assurer que ces choses sont remises dans l'ordre trié, nous faisons une comparaison linéaire.

Et ce que cela signifie, c'est que nous avons essentiellement deux pointeurs, en commençant par le côté gauche et nous disons d'accord, quel nombre est le plus petit, et nous savons que moins un est plus petit, donc nous le mettons à sa place et incrémentons le pointeur.

Et puis nous comparons ces deux valeurs, zéro est plus petit ici.

Donc nous le mettons à sa place et incrémentons le pointeur.

Et nous continuons à faire cela lorsque nous comparons les valeurs.

Et remarquez ici, nous avons en fait épuisé les valeurs dans le tableau de gauche.

Et puisque nous savons déjà que le tableau de droite est trié, nous plaçons simplement ceux-ci dans les positions qui leur appartiennent.

Et lorsque nous regardons le tableau résultant, nous remarquons que le tri fusion a trié l'entrée complètement.

Et donc voici la solution.

Et maintenant la question est, comment construisons-nous quelque chose comme cela ? Comment concevons-nous un algorithme récursif qui pourrait construire une solution de tri, vous savez, une solution à un problème comme celui-ci, nous allons regarder un peu de code pour faire cela.

Donc nous avons une ardoise vierge ici.

Et nous voulons considérer comment le tri fusion fonctionnerait pour satisfaire les propriétés que nous avons examinées.

Maintenant, la première chose que je veux faire est de construire l'appel récursif.

Et donc rappelez-vous, le tri fusion prend un tableau et le trie.

Et nous allons le faire en place.

Donc je vais construire une fonction qui est publique et statique.

Et elle sera simplement vide.

Donc nous allons modifier le tableau d'entrée original.

Et ce que je vais prendre ici sera appelé merge sort.

Et il va prendre un tableau d'entiers à une dimension, et nous l'appellerons data.

Et il aura un début et une fin, qui représenteront les indices avec lesquels nous travaillons.

Maintenant, pour le tri fusion, cela va être un appel récursif, nous devons considérer les cas de base.

Rappelez-vous, nous travaillons du début à la fin.

Et si ces valeurs se chevauchent, alors nous avons atteint notre cas de base.

Donc nous posons cette question, si le début est inférieur à la fin, et nous pouvons continuer à faire du travail.

Mais si le début dépasse le pointeur de fin, alors il n'y a plus de travail à continuer.

Nous avons déjà trié les données.

Et donc rappelez-vous, nous sommes tout à fait pour prendre le tableau et le diviser en deux moitiés, nous voulons diviser le problème en deux moitiés et les résoudre indépendamment.

Et donc la première chose que nous pouvons faire est que nous pouvons calculer le point médian.

Et donc ce que nous faisons, c'est que nous disons que le milieu va être essentiellement l'index de début du tableau plus l'index de fin, et nous divisons cela par deux, et cela va être le point médian avec lequel nous travaillons.

Et que voulons-nous faire ? Ici, eh bien, ce que nous voulons faire, c'est que nous voulons diviser le tableau en deux parties.

Et donc il serait logique pour nous de simplement appeler merge sort.

Nous traitons avec le même tableau de données.

Mais nos limites sont ce qui a changé.

Et donc le début est à nouveau, pour la première moitié, va commencer à la même position, mais la fin va se terminer au point médian.

Et cela va être la moitié gauche.

Maintenant, si nous pensons à la moitié droite, le début va changer, n'est-ce pas ? Le début va être le point médian plus un, jusqu'à la fin.

Et c'est ainsi que nous pouvons considérer la division de ce tableau en deux moitiés différentes.

Mais la question est, comment faisons-nous pour fusionner ces données, n'est-ce pas, ce que nous faisons, c'est que nous divisons et divisons et divisons continuellement, mais je veux pouvoir fusionner les données au format trié.

Donc construisons une fonction appelée merge.

Et ce que merge va faire, c'est qu'elle va prendre le tableau de données original, et elle va commencer à prendre le début, le point médian et l'index de fin.

Et rappelez-vous cette dernière animation que nous venons de regarder fait cette sorte de comparaison en temps linéaire pour remplacer les valeurs à la bonne place lorsqu'elle regarde les deux sous-tableaux triés, donc je construis une fonction ici, elle va être publique, statique vide.

Et je vais simplement appeler cela merge.

Et encore une fois, cela va prendre un tableau d'entiers appelé data, un point de départ, un point médian et un point de fin.

Et maintenant rappelez-vous, nous devons essentiellement fusionner ces valeurs, mais je ne veux pas modifier le tableau d'entrée pour l'instant.

Donc je vais construire un tableau temporaire.

Donc il serait logique de construire un tableau temporaire pour éviter de modifier, ne peut pas taper pour éviter de modifier le contenu original.

Et donc pour faire cela, je peux simplement construire un tableau temporaire simple ici.

Et ce sera un nouveau tableau int.

Et la taille dépendra des indices, n'est-ce pas, donc j'ai n moins start, plus un.

Donc cela va me construire un tampon de mémoire pré-alloué pour contenir toutes les données des sous-tableaux avec lesquels je travaille, du début à l'index de fin.

Et maintenant ce que je vais faire, c'est que je vais simplement copier les valeurs.

Donc je ne veux pas perdre une référence au début ou au point médian.

Donc je vais dire int i est égal à start, nous allons dire j est égal à mid plus un, et k est égal à zéro.

et k va être cette variable de suivi que nous utilisons pour garder une trace des valeurs que nous mettons dans ce temporaire.

Donc continuons.

Maintenant, rappelez-vous lorsque nous fusionnions les données ensemble dans cet appel de sous-fonction final, c'est une bonne façon de réaliser comment cela fonctionne.

Donc nous faisons essentiellement une comparaison en temps linéaire, aux valeurs dans le tableau de gauche, et le pointeur sur le tableau de droite, et nous disons lequel est le plus petit, celui qui est le plus petit sera placé en premier dans ce temporaire.

Et donc je dis essentiellement, tant que i est inférieur ou égal à mid, qui sera le sous-tableau de gauche.

Et nous voulons dire, eh bien, j est inférieur ou égal à la fin, alors nous pouvons continuer.

Et qu'est-ce que cela dit ? Ce que cela dit, c'est que tant que les deux sous-tableaux ont des valeurs, alors essayez de les fusionner dans l'ordre trié.

Oui, et c'est ce que nous voulons faire.

Donc nous commençons avec I, qui est le sous-tableau de gauche jusqu'au point médian, et puis j, qui commence du point médian à la fin, va être le sous-tableau de droite.

Et nous voulons simplement comparer ces valeurs.

Et donc nous posons une question, nous disons, d'accord, eh bien, si data sub i est inférieur ou égal à data sub j, alors nous savons ce que nous savons que la valeur dans le sous-tableau de gauche est inférieure à la valeur dans le sous-tableau de droite.

Donc ce que nous pouvons faire, c'est que nous pouvons dire, d'accord, dans ce tampon temporaire, je vais mettre à l'index k data sub i.

Donc la valeur la plus petite est mise ensuite dans le temporaire.

Et maintenant ce que je veux faire, c'est que je veux incrémenter i, puisque je l'ai déjà placé dans le tableau, et je veux incrémenter K, pour ne pas écraser cette valeur.

Maintenant, si cette condition ne tient pas, alors ce que je peux dire, c'est bien, d'accord, donc cela impliquerait le contraire.

Donc je dirais simplement temp de K est égal à data sub J.

Et puis ce que nous ferions, c'est que nous dirions k plus plus, et j plus plus.

Et vous pouvez aussi vous amuser, vous pouvez venir ici et faire quelque chose comme k plus plus ici.

Et vous pouvez faire quelque chose comme j plus plus ici, c'est les deux, c'est la même chose.

Donc si vous voulez simplifier votre code de cette manière, vous pouvez utiliser l'opérateur de post-incrémentation pour réduire la quantité de code.

Et cela gère essentiellement la comparaison entre les sous-tableaux.

Mais rappelez-vous la condition ici, la condition dit que nous ne faisons cela que tant que les deux valeurs ont des valeurs à comparer.

Et l'exemple que nous avons regardé, nous avons en fait épuisé les données dans le sous-tableau de gauche.

Et nous avons simplement dû placer toutes les données dans le sous-tableau de droite dans le tableau original.

Et donc nous devons satisfaire ce cas ici.

Et pour ce faire, nous pouvons simplement dire, tant que i est inférieur ou égal au point médian, donc tant qu'il y a des données à parcourir, nous allons simplement les placer dans la position du tableau temporaire où elles appartiennent.

Cela serait data, donc I, et encore une fois, nous ferions k plus plus n i plus plus.

Et cela gère l'épuisement du sous-tableau de gauche, si le sous-tableau de droite a épuisé ses valeurs, donc nous disons, ajoutez le reste des valeurs du sous-tableau de gauche dans le résultat.

Maintenant, de l'autre côté, si le sous-tableau de gauche a épuisé ses valeurs, mais que nous avons encore des données dans le sous-tableau de droite, alors nous avons simplement besoin de la condition inverse et nous disons, tant que j est inférieur ou égal à la fin, alors nous allons simplement dire temp sub k est égal à data sub j.

Et puis encore une fois, nous incrémentons simplement K.

Et nous incrémentons J.

Et c'est la même chose, nous ajoutons le reste des valeurs du sous-tableau de droite dans le résultat.

Vous pourriez demander, avons-nous terminé ? Et nous avons presque terminé.

Mais nous devons nous rappeler que nous avons construit ce tableau temporaire, et cela est vide.

Et donc nous n'avons pas vraiment fait de travail pour l'instant.

Et donc la question que nous devons poser est, comment modifions-nous le tableau de données original en mémoire.

Maintenant, nous ne voulons pas modifier tout le tableau, nous voulons seulement modifier la sous-section avec laquelle nous travaillons actuellement, dans n'importe quel appel récursif dans lequel nous nous trouvons.

Et cela nous amène à la phase de copie, comment copions-nous ces données de temp dans les bonnes positions de data, qui est la donnée originale.

Et il s'avère que nous pouvons simplement avoir une simple boucle for où nous disons i est égal à start.

Et tant que i est inférieur à end, n'est-ce pas, donc nous ne prenons que la sous-section avec laquelle nous travaillons.

Donc de start à end, n'est-ce pas, ce qui peut être n'importe quelle limite à n'importe quel point de la récursion.

Donc tant que I est égal à start n est inférieur ou égal à end, nous allons simplement incrémenter i.

Et à chaque itération, nous allons charger le tableau de données original à l'index i pour qu'il soit égal à ce qu'il y a dans le tableau temporaire à la valeur de i moins start.

Donc si le tableau de données avec lequel nous travaillons, si le start est 12, alors ce que nous ferions, c'est que nous dirions, d'accord, eh bien, I est égal à 12.

Donc 12 moins star est zéro.

Donc nous allons charger data set 12, avec ce qu'il y a à temp sub zéro.

Et c'est la phase de copie.

C'est ainsi que nous écrasons en fait les valeurs à chaque sous-tableau.

Regardons en fait une entrée ici, je vais avoir un nouveau tableau d'entrée, nous allons dire, vous savez, data est égal à new int.

Et nous allons simplement le charger avec quelques valeurs, nous allons dire moins cinq, vous savez, 2010 320.

Et ce que je veux faire, c'est que je veux trier cela.

Donc je vais appeler merge sort.

Et je vais lui donner le tableau de données, le début sera l'index zéro.

Et la fin sera la longueur moins un.

Et donc cela devrait trier le tableau en place.

Et donc ce que je peux faire, c'est que je peux mettre un point d'arrêt pour regarder le tableau une fois qu'il a été trié.

Et puis nous allons regarder la pile d'appels pour voir ce qui se passe réellement en coulisses.

Donc je vais déboguer et nous allons remarquer que je suis ici et merge sort est terminé.

Et ce que je peux faire, c'est que je peux regarder ce cadre de pile et regarder les données.

Et vous remarquez que nous avons à l'index zéro, moins 5023 10 et 20.

Et donc c'est la sortie dans l'ordre trié.

Mais cela ne nous est pas vraiment utile à moins que nous comprenions ce qui se passe au niveau de la pile d'appels.

Donc regardons cela.

En mettant un point d'arrêt dans la fonction merge sort.

Regardons un peu et voyons ce qui se passe.

Si je plonge ici, le premier cadre de pile est ajouté à la pile d'appels pour merge sort.

Et je me demande essentiellement si le début est inférieur à la fin ? Et la réponse est non, nous avons encore du travail à faire.

Et donc lorsque je vais ici, je calcule le point médian.

Et je dis que je veux diviser ce tableau en deux moitiés.

Et le point médian ici est deux.

Et donc ce que je fais, c'est que je dis, d'accord, je vais diviser tout de zéro à deux en son propre ensemble de sous-tableaux, et ensuite je vais gérer la moitié droite.

Et rappelez-vous, je ne peux même pas aller à la moitié droite jusqu'à ce que la moitié gauche soit terminée.

Donc je plonge dans cela.

Et maintenant je regarde tout de zéro à deux.

Et je dois le diviser encore plus.

Et donc maintenant je suis à cette position où le point médian est un.

Et encore une fois, je fais grandir la pile d'appels, et je suis toujours seulement sur le côté gauche.

Et je calcule le point médian à nouveau, et je vais encore.

Et maintenant nous ne satisfaisons pas cela, n'est-ce pas, parce que zéro et zéro sont égaux.

Et donc nous retirons en fait cela de la pile d'appels.

Et maintenant nous retournons à l'appel récursif suivant.

Et l'appel récursif suivant dit, d'accord, maintenant je veux gérer le côté droit de cela, n'est-ce pas.

Et lorsque je plonge dans cela, je fais à nouveau grandir la pile d'appels.

Et encore une fois, nous retirons, n'est-ce pas, nous ne satisfaisons pas ce cas de base, et nous continuons simplement cette opération.

Et donc maintenant j'ai atteint le cas de base sur le côté gauche le plus éloigné de la première moitié gauche de ce tableau.

Et ce qu'il me demande de faire, c'est qu'il me demande maintenant de fusionner ces valeurs dans l'ordre trié.

Donc si je plonge ici, et que nous regardons le merge, analysons le début, le milieu et la fin.

Rappelez-vous, je ne traite qu'avec deux valeurs ici.

Et donc si je vais ici, nous avons un tableau temporaire, et il n'est que de taille deux.

Et c'est parce que mon cas de base ici pour le tri fusion ne compare vraiment que deux valeurs.

Et donc nous allons ici, et nous disons, d'accord, laquelle est la plus petite, la valeur de gauche, ou la valeur de droite.

Et je viens ici, et je dis, d'accord, eh bien, ici, la valeur de gauche est plus petite.

Donc je charge K, je charge temp, et je mets moins cinq.

Et puis j'ai une autre boucle while.

Et rappelez-vous, parce que j'ai épuisé les valeurs à comparer dans le sous-tableau de gauche, je dois essentiellement prendre toutes les valeurs dans le sous-tableau de droite et les mettre dans les positions qui leur appartiennent.

Donc je viens ici et je charge les valeurs, j'incrémente les compteurs.

Et maintenant nous avons terminé, parce que nous avons atteint ce cas de base.

Donc maintenant, j'ai ce sous-tableau trié, moins cinq et 20.

Et ce que je dois faire, c'est que je dois les mettre dans l'emplacement original, n'est-ce pas ? Si nous regardons ces valeurs, j'ai, vous savez, I, J et K.

Qu'est-ce que cela signifie ? Eh bien, cela signifie que de la position avec laquelle je traite, dans le tableau original, je dois remplacer ces valeurs.

Donc c'est ce que ce remplacement va faire.

Donc en venant ici, je remplace la valeur un, je remplace la valeur deux.

Et maintenant j'ai terminé.

Et c'est le processus que nous suivons pour une seule itération du tri fusion.

Et ce processus va essentiellement continuer lorsque nous traitons des sous-tableaux de plus en plus grands lorsque nous remontons de manière récursive, n'est-ce pas, et maintenant nous fusionnons à nouveau.

Et remarquez, comme, puisque nous avons fait la moitié gauche, qui était juste deux valeurs, maintenant nous traitons la moitié droite, n'est-ce pas.

Et maintenant nous avons trois valeurs, et la moitié droite d'un autre sous-problème.

Et donc nous continuons simplement à comparer et à monter et à monter.

Maintenant, nous ne passerons pas par chaque cadre de pile.

Dans cet appel.

Il y en a assez comme nous l'avons vu dans l'animation.

Mais je vous encourage à revoir cette animation car c'est l'ordre dans lequel la pile d'appels sera évaluée.

Et c'est l'ordre dans lequel les choses vont remonter de manière récursive des sous-problèmes pour être fusionnées en une solution globale.

Et c'est l'un des composants clés de la division et de la conquête.

Les listes chaînées sont des structures de données très courantes utilisées pour stocker des données qui ne sont pas nécessairement stockées de manière contiguë en mémoire.

Et il s'avère que vous pouvez faire beaucoup de choses intéressantes avec la récursivité sur ces types de structures.

Nous allons examiner l'inversion de liste chaînée.

Et nous allons regarder une animation pour parcourir ce code.

Maintenant, l'idée est que nous avons une sorte de liste chaînée.

Disons que nous avons des valeurs dans l'ordre trié comme ceci.

Et nous allons simplement avoir un tas de pointeurs.

Et l'idée est que le nœud de tête change de un pointant vers deux pointant vers 345.

Au lieu de cela, nous voulons que six pointe vers cinq, cinq pointe vers quatre, et ainsi de suite.

Et lorsque nous regardons ce code, ce code d'inversion, nous avons posé cette question, d'accord, si le nœud de tête est nul, n'est-ce pas, si nous passons une valeur nulle, ou la valeur suivante de la tête est nulle, alors nous retournons simplement la tête.

Et cela nous ramène à cette idée de considérer les cas de base.

Quelle est la plus petite chose que je pourrais passer ? Si je passais ? Non, alors je pourrais simplement retourner nul.

Et ce serait une liste inversée.

N'est-ce pas ? Et dans la même veine, si je passais un seul nœud, où il n'y avait pas de nœud suivant, alors je pourrais simplement retourner la tête à nouveau.

Et ce sont de bons cas de base pour cette solution.

Mais la question est, comment commencer l'inversion ? Quelle est l'unité de travail que je dois faire et c'est ce que nous allons examiner.

Donc nous commençons avec un, le nœud de tête que nous passons à la première itération est un.

Et nous ne rencontrons pas le cas de base.

Et donc à la ligne trois, nous voyons que nous appelons reverse list head dot next.

Et cela nous pousse immédiatement au nœud suivant.

Et nous avons un cadre de pile sur la pile d'appels.

Maintenant nous regardons deux et cela n'est pas non plus, et il n'a pas non plus de pointeur pointant vers nul.

Et donc nous exécutons la ligne trois, encore un autre cadre de pile sur la pile d'appels.

Et cela nous amène à trois.

Et ce processus continue jusqu'à ce que nous arrivions à six.

Et lorsque six est passé en tant que paramètre, nous disons est-ce nul ? Et la réponse est non, mais la valeur suivante est nulle.

Et donc que retournons-nous, ce que nous faisons, c'est que nous retournons head, qui est simplement six, et six est retourné en tant que nœud à la valeur précédente.

Donc c'est le cas de base.

Et nous retournons cela à cinq.

Et donc maintenant P a été évalué au nombre six.

Et ce que nous disons, puisque le nombre cinq est le nœud de tête actuel, nous disons cinq dot next dot next, est égal à cinq.

Et il s'avère que ce que cela signifie, c'est que nous disons essentiellement, d'accord, eh bien, ce que je veux que vous fassiez, c'est prendre six et le faire pointer vers cinq, parce que head next est six, et head dot next, qui est six dot next, va pointer vers cinq.

Et si cela n'a pas de sens, je vous encourage à vraiment ralentir et à lire ce code.

Et à penser que cinq est le nœud de tête.

Et nous voulons dire que les pointeurs suivants, la position suivante pointe simplement vers nous-mêmes.

Maintenant, le problème ici est que cinq est aussi pointé vers six.

Et si nous devions tracer cela, cela serait une dépendance cyclique.

Et cela ne se terminerait jamais, n'est-ce pas.

Et donc ce que nous pouvons faire, c'est que nous pouvons simplement dire que le point suivant de cinq peut pointer vers rien, n'est-ce pas, c'est non, et donc cela est abandonné.

Et ce que nous retournons, c'est que nous retournons six, parce que nous voulons que six soit la nouvelle tête.

Et donc six va simplement se propager dans la pile d'appels jusqu'à l'appel original pour être le nouveau nœud de tête.

Et c'est pourquoi nous retournons p ici.

Et donc maintenant nous retournons et nous arrivons à quatre.

Et lorsque nous regardons quatre, nous savons que P est six.

Et ce que nous demandons ici, c'est que nous disons que le nœud suivant de quatre est cinq, et je veux que cinq soit égal à quatre.

Et donc encore une fois, nous faisons la même chose, nous prenons cinq, huit points vers quatre.

Et pour éviter la dépendance cyclique, nous abandonnons ce pointeur ici, cette connexion.

Et ce que nous retournons ? Que retournerons-nous six, parce que encore une fois, six se propage à travers, et six sera toujours P dans ce cas.

Et donc maintenant je retourne.

Et je sais que six est P, mais head dot next est quatre.

Et donc je veux que quatre soit égal à trois.

Donc je dis head dot next dot next est égal à trois.

Donc je dessine un pointeur.

Et encore une fois, j'abandonne la dépendance cyclique et je me débarrasse de cette connexion.

Et maintenant je retourne, P est toujours six, je retourne à deux et je dis que la valeur suivante de deux, qui est trois, je veux que trois dot next pointe vers deux.

Donc nous faisons cela, j'abandonne le pointeur et je retourne.

Et puis enfin nous faisons cela à nouveau.

J'abandonne le pointeur et maintenant nous avons terminé.

Donc prenons l'opportunité de regarder la pile d'appels et de vraiment comprendre comment cela fonctionne un peu plus en détail.

Pour gagner du temps, j'ai écrit un peu de code.

Le premier morceau de code que je veux regarder est cette idée de nœud.

Maintenant, ce nœud est juste une abstraction qui contient une valeur et un pointeur vers le nœud suivant.

Et donc c'est la manière la plus simple de construire une liste chaînée simplement.

Maintenant, j'ai aussi fait une méthode appelée print link list.

Et cela imprimera simplement toutes les valeurs.

Et c'est une vérification que nous pouvons utiliser pour nous assurer que nous avons inversé correctement la liste chaînée.

Et la dernière chose que je veux regarder est le code réel.

Donc c'est le même code que celui de la diapositive.

Et je veux regarder la pile d'appels lorsque nous déboguons cela.

Donc j'ai une liste chaînée simple ici 12345, comme nous l'avons regardé, et ils sont tous liés ensemble.

Et ce que nous voulons faire, c'est que nous voulons voir comment fonctionne l'inversion.

Donc si je l'exécute et que je le débogue, nous allons regarder la pile d'appels.

Donc la première chose que je rencontre est cet appel.

Et vous remarquerez dans le cadre de pile, lorsque je plonge dans cette fonction, c'est le cadre de pile initial qui est mis sur la pile d'appels.

Et je me demande, est-ce que le nœud que je regarde, qui est un, est-ce que c'est non, et la réponse est non.

est-ce que la valeur suivante est non, la réponse est non, c'est deux, n'est-ce pas.

Et nous pouvons le voir ici.

Donc je continue.

Et je viens d'appeler reverse list à nouveau, ce qui est un appel récursif.

Et lorsque je plonge dans cela, j'ajoute un autre cadre de pile à la pile d'appels.

Et maintenant vous voyez mes valeurs deux.

Et ma valeur suivante n'est toujours pas non.

Donc je continue.

Et j'ajoute un autre appel récursif, ce qui ajoute un autre cadre de pile à la pile d'appels.

Et je continue.

Et ce processus va continuer.

Maintenant, remarquez ici, la valeur est cinq, mais ma valeur suivante est en fait nulle.

Et cela satisfait ce cas de base ici.

Donc si nous continuons, vous remarquez que je retourne simplement nul ici.

Et cela arrête la récursion.

Donc remarquez que ce cadre de pile devrait être retiré.

Donc lorsque je continue, ce cadre de pile est retiré.

Et maintenant je regarde quatre.

Et il montre en fait ce qu'était le résultat de cet appel récursif pour P.

Donc lorsque je passe par-dessus, nous pouvons regarder p et voir que P est simplement cinq.

Et donc je dis essentiellement node dot next, donc évaluons cela.

Donc node dot next a une valeur de cinq.

Et je dis essentiellement que je veux que cinq pointe vers.

Donc je veux que cinq dot next soit égal à deux, quelle que soit ma valeur actuelle, qui est quatre, n'est-ce pas ? Donc nous savons que no dot Val est quatre.

Donc je change les pointeurs ici.

Donc lorsque je passe par-dessus, maintenant j'ai quatre pointant vers no lorsque je l'exécute, donc nous passons par-dessus une fois de plus.

Donc lorsque je regarde@no.val.no dot next, il devrait y avoir no ce qui est le cas.

Et maintenant la valeur P qui était cinq devrait pointer vers quatre maintenant.

Donc P dot next, dot Val est quatre.

Oui.

Et donc toute l'idée ici est que maintenant nous retournons le dernier nœud à nouveau, et nous le retirons de la pile d'appels.

Et le nœud que nous regardons à ce moment-là est trois.

Et en ce moment, trois pointe vers quatre, n'est-ce pas ? Donc si nous regardons no dot Val, qui est trois, nous pouvons dire no dot next dot Val, et c'est quatre.

Mais c'est faux, n'est-ce pas ? Parce que nous voulons que quatre pointe vers trois, pas trois pointant vers quatre.

Et donc c'est ce que fait cette ligne.

Je dis que je veux que quatre pointe vers trois.

Et donc je fais cela, et puis j'abandonne la connexion.

Et donc maintenant si j'évalue cela, et que nous regardons p, nous pouvons en fait voir les progrès que nous avons faits, cinq pointe vers quatre, et quatre pointe vers trois.

D'accord, donc nous n'avons pas encore terminé.

Mais nous faisons des progrès.

Et lorsque nous retournons d'ici, nous remontons la pile d'appels.

Et nous continuons simplement ce processus.

Nous retournons, nous remontons la pile d'appels, nous venons ici, nous retournons et nous remontons la pile d'appels.

Et maintenant nous sommes de retour à l'appel original.

Et rappelez-vous comment nous avons propagé la toute dernière valeur à travers tous ces appels.

Donc lorsque nous regardons la valeur inverse, reverse dot Val, c'est cinq et c'est notre nouveau nœud de tête, qui était l'objectif de ce problème.

Et donc si nous venons ici, nous regardons reverse, nous disons d'accord, nous avons cinq, la valeur suivante est quatre, la valeur suivante, il y a trois, la valeur suivante, il y a deux et une valeur x.

Il y a un, et puis nous avons terminé.

Et donc c'est ainsi que fonctionne la pile d'appels pour une inversion de liste chaînée.

Un problème vraiment amusant à considérer avec les listes chaînées est comment fusionner deux listes chaînées triées de manière récursive.

Nous allons regarder comment fonctionne la pile d'appels pour cela. Analysons ce petit extrait de code et voyons si nous pouvons conceptualiser ce qui se passe sur la pile d'appels.

Nous prenons deux nœuds de tête.

L'un est une liste de valeurs, et l'autre est également une liste chaînée simple de valeurs.

Et nous posons cette question, la première question est, quelle est la plus petite entrée que je pourrais passer ? Et c'est une bonne considération pour notre cas de base, la même formule que nous avons appliquée.

Si je passe un nœud de tête pour a, qui est non, alors je peux simplement retourner b, car B serait fusionné avec non, ce qui serait simplement lui-même.

Et dans la même veine, si b est nul, et que je fusionne cela avec a, alors je peux simplement retourner a.

Et s'ils sont tous les deux non, alors non fusionné avec non est également simplement la valeur nulle.

Donc cela tient.

Et c'est le cas de base.

Mais considérons l'autre côté des choses.

Et c'est une comparaison similaire à celle que nous avons vue avec le tri fusion.

Maintenant, nous considérons, d'accord, tout d'abord, le cas de base.

Mais deuxièmement, quelle est l'unité de travail que nous devons faire pour la récursivité.

Et je pense que cela aidera si nous regardons deux listes.

Donc nous avons deux listes triées de valeurs.

Et nous voulons passer par cet appel récursif.

Et la première chose que nous faisons est que nous ajoutons un cadre de pile à la pile d'appels.

Et il dit essentiellement, les nœuds de tête que j'ai sont un et quatre, donc aucun d'eux n'est nul.

Et ce que je veux faire, c'est que je veux dire, d'accord, quelle valeur est la plus petite, la valeur dans le premier nœud ou la valeur dans le second nœud A ou B, la donnée de A est un et la donnée de B est quatre.

Donc la première conditionnelle est celle qui sera récursive.

Et je dis essentiellement que un dot next va pointer vers sorted sorted merge.

Et le nœud A va être incrémenté d'une valeur, donc j'ajoute un autre cadre de pile à la pile d'appels.

Et donc maintenant je passe en huit.

Et maintenant, il est comparé avec quatre.

Et nous n'avons toujours pas atteint notre cas de base, n'est-ce pas.

Et donc je regarde l'instruction L.

Et je compare huit et quatre et quatre est évidemment plus petit.

Et donc ce sera le prochain nœud que je vais considérer.

Et je continue simplement ce processus.

Donc maintenant huit et 11 sont comparés, huit est plus petit, et je passe en 22.

Et j'ajoute un autre cadre de pile.

Et maintenant 22 et 11 sont comparés.

Et puisque 11 est plus petit, je passe au nœud juste après 11.

Et ceux-ci sont comparés.

Et remarquez dans les appels, la récursion doit se terminer, mais je définis en fait ces résultats comme la valeur suivante.

Et donc lorsque nous comparons 22 et 16, 16 est plus petit, donc je passe en 20.

Et maintenant 20 est plus petit.

Mais c'est intéressant car il n'y a pas de nœud après 20.

Et donc maintenant je suis à ce point où j'ai non.

Et maintenant nous considérons le cas de base, si nous avons une valeur nulle, qui est B dans ce cas, alors je retourne simplement a.

Et si je retourne a alors je retourne simplement la référence au nœud de 22.

Donc voici le cas de base.

Et ce que je peux faire, c'est que je peux simplement retourner 22 ici, et cela est retiré de la pile d'appels.

Et c'est là que le dénouement commence.

Donc lorsque je retourne 22 ici, je modifie en fait le pointeur 20s dot next, n'est-ce pas, parce que je dis 20 dot next, est égal au résultat de sorted merge.

Et puisque sorted merge a retourné 22, je peux maintenant modifier ce pointeur.

Et à partir de là, je retourne a.

Et lorsque je retourne a, je retourne simplement 20.

Et cela est retiré de la pile d'appels.

Et maintenant, vous savez que nous regardons 16.

Et nous disons, à quoi devrait pointer le pointeur suivant de 16 ? Eh bien, 16 devrait pointer vers 20.

Mais il pointe déjà vers 20.

Donc nous n'avons pas vraiment besoin de faire quoi que ce soit.

Et donc je suis retourné d'ici 16.

Et cela est retiré de la pile d'appels.

Et encore une fois, dans le même cas, 11 pointe déjà vers 16.

Donc nous n'avons pas besoin de modifier quoi que ce soit.

Mais nous retournons 11 d'ici et cela est retiré de la pile d'appels.

Et maintenant nous avons cette question, huit pointait vers 22.

Mais puisque nous avons retourné à 11, nous pouvons maintenant dire que huit va pointer vers 11.

Et cela signifie que nous modifions le pointeur, ce que nous avons fait.

Oui, et maintenant nous retournons huit de ce cadre de pile, une valeur plus petite, et cela est retiré de la pile d'appels.

Maintenant nous comparons huit et quatre, quatre pointait vers 11.

Mais puisque huit a été retourné de l'appel récursif, et nous prenons quatre et nous le faisons pointer vers huit maintenant, nous retournons la valeur la plus petite du cadre de pile.

Et que faisons-nous ici ? Eh bien, ce qui se passe ici, c'est que nous retirons cela de la pile d'appels, et quatre est la valeur la plus petite.

Et donc maintenant ce que nous voulons, c'est que un pointe vers le nœud quatre.

Et c'est notre dernier cadre de pile.

Et à partir de là, nous retournons simplement un, qui est le nœud de tête, qui est la plus petite valeur des deux listes triées.

Et à partir de là, cela est retiré du cadre de pile.

Et si nous suivons ces arêtes, ou ces pointeurs, nous remarquons que un va vers quatre, qui va vers huit, qui va vers 11, vers 16, vers 20, vers 22, vers 40.

Et cela finit par être notre liste triée.

Et même pour cela, nous pouvons prendre une seconde pour regarder le code et comprendre la pile d'appels.

D'accord, donc j'ai pris les devants et j'ai en fait construit quelques listes chaînées.

Donc nous en avons une ici.

Donc un, 513 14, et 550.

Et nous avons une autre liste chaînée complètement indépendante, deux 15 130 203 50.

Et l'idée ici est de savoir comment prendre celles-ci et les fusionner dans leur ordre trié.

Et donc nous prenons le même code que celui que nous venons de regarder, mais maintenant nous voulons l'analyser du point de vue de la pile d'appels.

Et donc je vais venir ici, et je vais mettre un point d'arrêt sur l'appel initial.

Et nous allons déboguer cette fonction.

Donc lorsque je plonge dans cette fonction, vous remarquerez que la pile d'appels grandit.

Et maintenant nous avons deux listes, ce serait a et b de l'exemple.

Donc nous avons un et deux.

Et cela correspond aux deux nœuds initiaux que nous avons ici, deux et un.

Et ce que nous faisons, c'est que nous vérifions si vous savez, la première liste est nulle, alors nous retournons la deuxième liste.

Et si la deuxième liste est nulle, nous retournons la première liste.

Cela, bien sûr, ne tient pas encore.

Donc nous continuons et comparons les valeurs.

Puisque un est inférieur à deux, nous sautons ici et faisons un autre appel récursif.

Et remarquez que les cadres de pile grandissent simplement.

Ils grandissent simplement.

Et ce cadre de pile dépend du résultat de ce cadre de pile.

Et lorsque je continue et fais ces comparaisons, j'ai un autre cadre de pile.

Et chaque cadre de pile subséquent a une dépendance sur les résultats de celui qui est au-dessus.

Et donc nous continuons à faire cela.

Et nous faisons cela jusqu'à ce que nous atteignions l'un de ces cas de base.

Donc je continue.

Et maintenant j'ai atteint un cas de base, la valeur que nous avons est list one, qui est 550.

Et je vais simplement retourner cela.

Et lorsque je le retourne, que se passe-t-il ? Eh bien, c'est le résultat de cette fonction.

Donc je dis l to Next est 550.

Et lorsque cela est évalué, je retourne simplement ici.

Et vous remarquez que les cadres de pile vont commencer à diminuer maintenant parce que nous avons atteint un cas de base.

Et donc lorsque je continue et que je retourne ces valeurs, vous remarquerez que notre pile d'appels diminue en taille.

Et nous réattribuons essentiellement les pointeurs au nœud suivant.

Et cela diminue et diminue et diminue.

Et maintenant enfin, nous arrivons à un point où l'opération triée est complète.

Et donc si nous regardons sorted merge, si nous regardons cette valeur, nous remarquons que la première valeur est un, la valeur suivante est deux 513.

Et elle est maintenant dans l'ordre trié.

Donc nous avons pris deux listes triées et les avons fusionnées dans l'ordre croissant, ce qui est la sortie attendue.

Et ce n'est qu'un exemple de prise de deux listes chaînées et de démonstration du fonctionnement de l'opération de fusion sur la pile d'appels.

Cela m'amène à l'un de mes sujets préférés, qui est les arbres.

Et les arbres sont l'une des structures de données vraiment fantastiques qui fonctionnent très bien avec la récursivité.

Et la première question que nous allons examiner est l'insertion d'une valeur dans un arbre binaire de recherche.

Maintenant, un arbre, en particulier un arbre binaire de recherche, sera une série de nœuds et nous allons essentiellement partir du haut vers le bas, nous allons avoir un tas de connexions, et le nombre d'enfants au maximum que nous pouvons avoir à partir d'un seul nœud est deux et le nombre minimum de nœuds que vous pouvez avoir est zéro.

Et donc ce que nous allons faire, c'est que nous allons ajouter un tas de nombres ici et analyser les propriétés de cet arbre.

Remarquez que tout ce qui est à gauche du nœud racine 100 est inférieur à 100.

Et tout ce qui est à droite est supérieur à 100.

Maintenant, cette propriété, il s'avère qu'elle est vraie de manière récursive.

Donc si nous regardons tout ce qui est à gauche est inférieur à 80.

Tout ce qui est à droite est supérieur à huit, mais c'est intéressant car tout ce qui est à droite est supérieur à 80, mais aussi toujours inférieur à 100.

Et donc si vous regardez, la plus grande valeur sur le sous-arbre de 80, sur le sous-arbre droit est 95.

Et 95 est toujours inférieur à 100.

Et donc si vous n'êtes pas familier avec les propriétés des arbres binaires de recherche, je vous encourage à faire une recherche rapide et à regarder les règles pour cela.

Mais c'est à peu près l'ensemble des règles pour un arbre binaire de recherche.

Et nous sommes confrontés à cette tâche et la tâche est d'ajouter ce nœud, et le nœud est 108.

Et si nous regardons cette valeur, nous disons essentiellement, d'accord, je vais commencer au sommet de cet arbre, et je vais déterminer où je peux placer 108.

Et je compare, je dis, est-ce que 108 est supérieur à 100, ou inférieur à 100 ? ou égal à 100 ? Et je dis qu'il est supérieur, donc je vais à droite.

Et je demande si 108 est supérieur à 120, ou inférieur ou égal à 120 ? Et nous voyons qu'il est inférieur, donc je vais à la sous-moitié gauche.

Et je pose la même question, est-ce que 100 est supérieur à 110 ou inférieur à 110.

Et je vois qu'il est inférieur, et donc maintenant je descends ici.

Et je dessine une connexion.

Et c'est le point où 108 appartient.

Et ici vous pouvez voir qu'il satisfait toujours l'ensemble des règles, n'est-ce pas ? 108 est supérieur à 100.

Donc il satisfait cette propriété, il est inférieur à 120.

Il est inférieur à 110.

Donc c'est la position valide pour 108.

Et donc regardons le code.

Il s'avère que le code pour cela est extrêmement simple.

Et comme je l'ai dit, avant de considérer le cas de base, quelle est la plus petite chose que je peux passer ? Eh bien, que se passe-t-il s'il n'y a pas de racine ? N'est-ce pas ? Que se passe-t-il si c'est la première valeur que nous insérons dans l'arbre ? Eh bien, si c'est le cas, alors ce que je fais, c'est que je crée simplement un nouveau nœud, je définis les données, et je retourne cette valeur.

N'est-ce pas ? Et il s'avère que c'est un cas de base assez bon.

Maintenant, si nous considérons l'autre cas, maintenant nous devons commencer à penser, d'accord, eh bien, que se passe-t-il si je dois faire quelques comparaisons ? Et c'est là que je commence à comparer les données.

Donc regardons ce qui se passe.

La première question dit, si j'atteins null, j'ai récursé jusqu'à mon objectif final, selon les propriétés de l'arbre de recherche de l'arbre binaire de recherche.

Maintenant, rappelez-vous, les insertions de nœuds d'arbre binaire de recherche se feront toujours au niveau des feuilles.

Donc elles se feront toujours à la fin.

Donc si vous avez fait toutes vos comparaisons jusqu'à la toute fin, alors vous avez atteint une position valide pour insérer les données.

N'est-ce pas ? Et cette position valide serait lorsque vous n'avez plus de comparaisons à faire, ce qui est impliqué par le nœud de tête B, non.

Maintenant, l'autre conditionnelle que je regarde est essentiellement en train de dire, d'accord, je suis à un nœud, et je veux le comparer à mon nœud actuel.

Donc rappelez-vous, lorsque nous comparions 108 à 100, je posais cette question, je dis, est-ce que le nœud que je veux insérer est supérieur ou inférieur à cette valeur.

S'il est supérieur, je dis, head dot right est égal, et puis je fais simplement un autre appel récursif.

Et je progresse vers la moitié gauche ou droite du sous-arbre.

L'autre côté est simplement l'opposé.

Donc si je suis inférieur au nœud actuel, alors je veux descendre du côté gauche du sous-arbre.

Maintenant, ce dernier morceau ici, une fois que j'ai fait tout ce travail, j'ai fait toutes les insertions, je veux simplement retourner le nœud racine original.

Et ce nœud racine original dit simplement, voici l'arbre avec lequel vous avez commencé.

Regardons la pile d'appels.

Pendant ce processus d'insertion.

J'appelle insert node.

Et je compare 100 et 108.

Et je sais que 108 est supérieur à 100.

Donc je récurse du côté droit.

Maintenant, lorsque j'arrive à ce point, j'ajoute un autre cadre de pile.

Et je compare 120 et 108.

Et je sais que 108 est maintenant inférieur à cela.

Donc je récurse du côté gauche.

Maintenant ici, je compare 108 et 110.

J'ajoute un autre cadre de pile, je compare ces valeurs.

Et parce qu'il est inférieur, je vais du côté gauche.

Et c'est intéressant, car maintenant ma valeur que je compare est non.

Et rappelez-vous, lorsque nous regardons le code ici, non est simplement le cas de base.

C'est ce que nous considérons lorsque nous insérons un nœud.

Et donc je crée simplement ce nœud 108 et je le retourne, n'est-ce pas.

Et donc ici, je dirais, d'accord, new node had died data est égal à 108.

Et je retournerais ce nœud.

Et donc à partir de ce cadre de pile, je retournerais en fait le nœud 108 et je le retirerais de la pile.

Et ce que je ferais ici, c'est que puisque je disais 110 dot left, est égal à la valeur que c'était.

Maintenant je peux dessiner une connexion à 108 et simplement commencer à retourner ces valeurs vers le haut de la pile.

Et c'est le processus d'insertion d'une valeur dans un arbre binaire de recherche.

Regardons un autre problème amusant, qui est aussi une sorte de problème amusant de renversement d'arbre en profondeur.

Et le but ici est d'imprimer tous les nœuds feuilles.

Donc nous regardons le même arbre.

Mais nous voulons construire une fonction qui imprime tous les nœuds que nous voyons ici dans l'ordre de gauche à droite.

Donc 30 60 80 5 90-5 10-8 115 et 150.

Maintenant, si nous réfléchissons à la récursivité de la manière dont cela fonctionne, mécaniquement, nous commençons au nœud racine, et nous allons tout en bas.

Et nous atteignons un nœud feuille ici, donc nous l'imprimerions.

Et ce que je ferais, c'est que je retirerais essentiellement la pile d'appels et irais à ce nœud.

Mais je passerais immédiatement au sous-arbre droit de ce nœud.

Et ce serait un autre nœud feuille car il n'a pas d'enfants.

Et je l'imprimerais et récurserais vers le haut de la pile.

Et puis je remonterais à 80.

Et maintenant je descends, c'est sa moitié droite.

Et ici, je descendrai sa moitié gauche, trouverai un nœud feuille, retournerai, descendrai la moitié droite, trouverai un nœud feuille, retournerai.

Et ce processus continue simplement.

Et l'ordre d'exécution est vraiment important à comprendre ici.

Rappelez-vous, si je descends la moitié gauche, je ne peux même pas considérer la moitié droite jusqu'à ce que la moitié gauche ait été entièrement explorée.

Et c'est une partie de la propriété que la recherche en profondeur suit.

Et nous allons regarder un autre exemple de DFS avec un graphe dans un instant.

Donc maintenant je descends, je récurse vers le bas de la moitié gauche, je trouve le nœud feuille, je l'imprime, je récurse vers le haut et je fais tout cela jusqu'à ce que je sois essentiellement à court de nœuds feuilles à trouver, ce qui nous amène ici.

Et maintenant nous avons terminé.

Donc voici le code pour cela.

Et nous allons regarder cela pour comprendre comment les choses sont ajoutées sur la pile d'appels ainsi que dans le code.

Mais encore une fois, nos cas de base, que se passe-t-il si nous passons une valeur nulle, c'est un assez bon cas de base, n'est-ce pas ? Parce que alors nous retournerions simplement, il n'y a rien à imprimer si vous passez simplement un nul.

Mais nous devons aussi penser à l'objectif, l'objectif est d'imprimer le nœud feuille.

Et donc nous voulons continuer à récurser jusqu'à ce que nous atteignions un nœud feuille.

Et les propriétés d'un nœud étant un nœud feuille est qu'il n'y a pas d'enfants.

Et donc c'est là que nous commençons à demander, d'accord, s'il n'y a pas d'enfants à gauche, s'il n'y a pas d'enfants à droite, alors je peux en fait évaluer la valeur sous-jacente de ce nœud et simplement retourner.

Maintenant, si nous ne sommes pas un nœud feuille, alors nous devons récurser vers le bas de la moitié gauche de l'arbre, ce que nous faisons ici.

Et si nous avons une moitié droite à récurser, alors nous descendons la moitié droite après que la moitié gauche ait été explorée.

Cela nous permet encore une fois, c'est pourquoi nous évaluons d'abord le côté gauche.

Et puis nous descendons le côté droit de manière récursive.

Et nous faisons cela pour tous les sous-arbres récursifs jusqu'à ce que nous ayons terminé.

Donc regardons la pile d'appels et voyons comment cela s'exécute, ou nous regardons ici est le même programme.

Donc nous avons un peu de code ici, print leaves, et c'est le même code que nous avons regardé avant.

Donc si le nœud racine d'entrée est nul, nous retournons simplement, nous évaluons la gauche et la droite.

Et cela vérifie essentiellement si un nœud donné est une feuille.

Et nous l'imprimons, et puis nous nous retirons de la pile d'appels.

Maintenant, si nous ne satisfaisons pas cela, alors nous descendons la moitié gauche et droite du sous-arbre.

Donc en utilisant le même code que nous avons regardé pour l'insertion, j'ai en fait construit un arbre à utiliser.

Donc j'ai une entrée avec un tas de nombres.

Ce sont tous les nombres que nous regardions avant, je crois.

Et c'est juste un ensemble aléatoire de nombres.

Donc rien de spécial.

Et nous les insérons simplement.

Donc j'ai une fonction ici de l'exemple précédent appelée insert node.

Et elle construit simplement un arbre pour nous.

Et donc maintenant ce que je veux faire, c'est que je veux imprimer toutes les feuilles ici.

Donc ce que je vais faire, c'est que je vais ajouter un point d'arrêt ici.

Et nous allons déboguer directement.

Et la première question que je pose est, est-ce que le nœud racine est nul ?

Et la réponse est non, ce n'est pas nul.

N'est-ce pas ? Donc cette première valeur.

Et donc que fais-je ? Eh bien, je récurse vers le bas de toute la moitié gauche du sous-arbre.

Donc rappelez-vous, cela commence à 100.

Et maintenant je descends à gauche.

Et puisque ce n'est pas nul, je saute par-dessus cela.

Et maintenant je récurse simplement vers le bas de la moitié gauche de l'arbre.

Et pour ce nœud, encore une fois, ce n'est pas nul.

Et pour ce nœud spécifique, je récurse vers le bas de sa moitié gauche du sous-arbre.

Et je continue simplement à descendre la moitié gauche, je n'explore même pas la moitié droite jusqu'à ce niveau.

Et vous remarquez que nous venons d'imprimer le premier nœud feuille, qui est 30.

Et ce n'est que lorsque j'ai exploré toute la moitié gauche de ce sous-arbre que je peux maintenant aller à l'autre moitié droite de ce sous-arbre.

Donc je plonge ici.

Et maintenant je descends la moitié droite.

Il s'avère que la moitié droite est à nouveau un autre nœud feuille.

Et donc je peux simplement imprimer cette valeur.

Et si je mets un point d'arrêt ici, vous remarquerez que nous continuons simplement à imprimer.

Vous savez, nous atteignons les nœuds nuls, nous atteignons les nœuds nuls, et nous imprimons les feuilles.

Et vous pouvez voir ici, c'est l'évaluation du nœud feuille que nous faisons.

Et la raison pour laquelle je voulais parcourir cette animation est de souligner davantage que lorsque nous pensons à la pile d'appels, je ne peux même pas envisager d'évaluer cette expression jusqu'à ce que chaque appel récursif, et chaque sous-appel ait été entièrement évalué.

Une fois que cela est vrai, alors je peux commencer à dénouer les sous-arbres droits et je travaille de bas en haut.

Et c'est l'idée pour ces types de parcours DFS avec lesquels nous traitons.

Cela nous amène à notre dernière section d'algorithmes que nous allons examiner.

Et nous allons regarder un exemple simple avec des graphes.

Et nous allons simplement voir à quel point travailler avec des graphes est similaire à quelque chose comme les arbres.

Et nous allons regarder un algorithme très populaire connu sous le nom de recherche en profondeur.

Et l'idée est que nous commençons à un nœud comme a, et nous disons essentiellement que nous recherchons un nœud, disons que le nœud que nous recherchons est H.

Et donc je commence par a et je dis, d'accord, laissez-moi obtenir tous les voisins et voir si c'est ma valeur, donc a n'est pas ma valeur.

Donc je vais à mon voisin, et je dis B, B n'est pas ma valeur, je vais à C, D n'est pas ma valeur, mais j'obtiens tous mes voisins.

Et c'est un point intéressant, car je recherche H, n'est-ce pas, qui est dans la moitié éloignée.

Mais lorsque j'obtiens mes voisins, disons que le premier voisin que j'obtiens est E.

Et donc je dois en fait explorer les profondeurs de E avant même d'envisager d'aller à H.

Et donc je descends, et je vois E.

Et maintenant je vais à F.

Et maintenant je dois regarder tous les voisins de F.

Donc le premier voisin auquel je vais est K.

Et si k avait des voisins, j'explorerais tous ces voisins.

Mais ce n'est pas le cas, donc je peux simplement me retirer.

Et maintenant je vais à J et je retourne à F.

Maintenant je vais à I, je suis de retour à F, et je récurse en quelque sorte vers le haut de la pile d'appels.

Donc maintenant que j'ai exploré tous les voisins de droite, j'ai exploré un voisin de D, il ne me reste qu'un voisin non visité à explorer.

Et c'est g, donc je vais à G et je dis, est-ce la valeur que je cherche ? Et ce n'est pas le cas.

Donc je regarde les voisins de G et je dis, est-ce la valeur que je cherche ? Et c'est le cas.

Et c'est l'idée de la recherche en profondeur.

Et donc nous allons regarder un morceau de code et le parcourir ligne par ligne et voir comment quelque chose comme cela fonctionnerait de manière récursive.

Nous regardons un morceau de code comme celui-ci, et nous avons le nœud d'entrée.

Et pour éviter les cycles, qui peuvent se produire dans les graphes, ce qui est différent des arbres, nous garderons un ensemble de valeurs visitées.

Donc nous ne voulons jamais visiter le même nœud plus d'une fois.

Et donc c'est ce que l'ensemble visité va faire.

Et l'entier objectif ici est simplement le nœud que nous recherchons.

Donc je sais que le graphe que nous venons de regarder était des lettres, mais nous allons supposer que nous travaillons avec un graphe avec des valeurs entières.

Et nous posons nos questions de cas de base à nouveau.

Donc pensez à la plus petite chose que vous pourriez passer, si vous passez un nœud vide, un nœud normal, alors il n'y a aucun moyen que vous puissiez jamais trouver l'objectif, car l'objectif est une valeur entière.

Et donc ici, nous retournerions simplement false.

Donc c'est un cas de base.

L'autre cas de base est si nous avons en fait trouvé le nœud.

Donc supposons que le nœud que vous passez est le nœud d'or, alors ici nous avons trouvé le nœud.

Et donc nous retournerions simplement true ici, et cela impliquerait que nous avons trouvé la valeur que nous recherchions.

Mais supposons que nous n'avons pas trouvé la valeur, comme dans l'exemple.

La première chose que nous devons faire est que nous devons agréger tous les voisins d'un nœud donné.

Et donc nous allons supposer que l'API de nœud a une fonction d'appel qui vous permet d'agréger tous les voisins.

Et la première question que nous posons est, avons-nous visité ce nœud auparavant ? Rappelez-vous, nous voulons éviter les cycles.

Et donc nous ne voulons jamais visiter un nœud plus d'une fois.

Et donc si cela a été visité, nous l'ignorons simplement et nous continuons.

Mais si cela n'a pas été visité, alors nous l'ajoutons à l'ensemble visité.

Et nous commençons l'exploration.

Et nous posons cette question, avons-nous trouvé le nœud avec lequel nous avons travaillé avec ce voisin particulier.

Si nous avons trouvé la solution, alors nous pouvons simplement retourner tout de suite.

Maintenant, si nous n'avons pas trouvé la solution à partir de ce voisin particulier, alors nous continuerons à récurser à travers le reste des voisins, et c'est à ce moment-là, si nous l'avons trouvé, nous retournerions true.

Et cela nous amène à notre dernier cas de base, supposons que nous avons parcouru tous les voisins.

Et nous n'avons jamais trouvé la solution.

Cela signifierait que la valeur cible que nous recherchions n'était tout simplement jamais dans le graphe pour commencer.

Et cela nous amène à notre dernier cas de base de simplement retourner false.

Et c'est une façon de dire, hé, j'ai recherché ce nœud, mais il n'existait pas dans le graphe.

C'est faux, il n'est pas apparu dans la recherche.

Et c'est là que nous pouvons terminer l'algorithme.

Je pense qu'il est important de passer juste un peu de temps à parler des optimisations que vous pouvez faire lorsque vous utilisez la récursivité.

Et la première que nous allons examiner est la mémoïsation.

Et la mise en cache, dont nous avons brièvement parlé lors de l'écriture de Fibonacci.

Et la question à laquelle nous essayons de répondre ici est, comment pouvons-nous accélérer notre programme en stockant essentiellement des choses que nous avons déjà recalculées ou calculées pour la première fois.

Donc si j'ai calculé une opération très coûteuse, et que je dois la recalculer à nouveau, dans un appel récursif ultérieur, je veux vérifier si j'ai déjà fait ce travail.

Et si c'est le cas, je vais simplement retourner le résultat au lieu de recalculer cette opération à nouveau.

Et la meilleure façon de conceptualiser cela est de regarder la séquence de l'arbre de Fibonacci.

Ici, nous voyons que je fais F de trois deux fois, et je recalcule F de deux, trois fois.

Et la question est, pourquoi ne puis-je pas simplement calculer f de deux une fois, et ensuite simplement réutiliser cette valeur, pour que je ne fasse pas pousser ces sous-arbres.

Et il s'avère que vous pouvez faire cela très facilement.

Regardons le code Fibonacci modifié.

Remarquez que j'ai une hashmap ici et les hashmaps ont cette propriété, de sorte que nous pouvons récupérer des valeurs de la map en temps d'accès constant, donc big O de un.

Et la raison est que les données que nous mettons dans la hashmap sont hachées.

Et donc nous avons un accès en temps constant aux adresses mémoire où ces données sont stockées.

Et donc lorsque j'appelle la fonction Fibonacci, la première chose que je fais toujours est de dire, hé, est-ce que le cache a cette valeur.

Et vous pouvez aussi remarquer que j'ai pré-rempli le cache avec les cas de base également.

Maintenant, dans le cas où le cache n'a pas la valeur, je continue l'appel récursif, comme je l'ai fait précédemment.

Mais je m'assure que une fois que cet appel récursif a été évalué, je mets le résultat dans le cache.

Et puis je retourne mon résultat.

Et c'est un composant vraiment clé car le cache est global, n'est-ce pas.

Et donc tous les appels récursifs ultérieurs mettent leurs résultats dans le cache.

Et à mesure que les choses sont ajoutées et retirées de la pile, je peux simplement continuer à référencer le cache pour voir si je fais un travail redondant ou non.

Et cela me fait économiser beaucoup de puissance de calcul.

Donc c'est l'idée de la mémoïsation et de la mise en cache.

Et vous pouvez faire beaucoup de cela dans beaucoup de situations différentes.

La prochaine optimisation que je veux discuter est cette idée d'optimisation de l'appel en fin de fonction.

Et les gens se réfèrent généralement à cela comme l'optimisation de l'appel en fin de fonction, ou la récursivité en fin de fonction.

Et l'idée ici est que, essentiellement, le compilateur dans certains langages, surtout les langages de programmation fonctionnelle, optimisera le nombre de cadres de pile qui sont ajoutés à la pile d'appels pour essentiellement éliminer cette idée de débordements de pile dans de nombreux scénarios.

Maintenant, la manière dont le compilateur fait cette analyse est qu'il regarde vraiment le dernier appel de fonction.

Et il doit être un appel récursif.

Et nous allons regarder une idée de comparaison de ces deux choses.

Et il y avait en fait une réponse sur le Stack Exchange d'informatique par cet utilisateur, et il a donné deux exemples.

Le premier est cette simple fonction factorielle récursive.

Et remarquez que la valeur de retour finale est une valeur multipliée par un appel récursif.

Maintenant, cela n'est pas récursif en fin de fonction, car la valeur de retour n'est pas simplement l'appel récursif.

Et donc pour que cela soit optimisé en récursivité en fin de fonction, nous devons modifier pour que cela ressemble à ceci.

Maintenant, si vous passez une seconde à regarder ce code, vous réaliserez que fonctionnellement, il fait exactement la même chose.

Mais nous avons dû modifier les paramètres pour arriver à un point où nous pouvons construire une fonction qui est optimisée pour l'appel récursif en fin de fonction.

Et la raison pour laquelle elle est optimisée avec cette propriété récursive en fin de fonction est que la valeur de retour finale est en elle-même simplement un appel récursif.

Et il s'avère que dans certains systèmes d'exploitation, dans certains langages, dans leurs compilateurs, ils ont mis en œuvre certaines techniques d'optimisation pour exploiter cette propriété et réduire les débordements de pile.

Maintenant, je veux juste faire quelques remarques à ce sujet.

La règle générale est de toujours faire en sorte que vos appels récursifs soient la dernière instruction. Rien n'est ajouté à cela, juste l'appel récursif.

Et l'autre chose à considérer est que cela est principalement supporté par les langages fonctionnels.

Mais ce n'est pas inhérent aux langages comme Python et Java et même JavaScript.

Il y a certains navigateurs pour ies 2016.

Ils supportent l'optimisation de la récursivité en fin de fonction pour des choses comme JavaScript, mais ce n'est pas supporté partout.

Et donc lorsque vous considérez cette technique d'optimisation, pensez au langage que vous utilisez.

Et pensez, vous savez, au compilateur que vous utilisez et où votre code est exécuté pour voir si ce type d'optimisation est supporté ou non.

Cela nous amène à notre dernière diapositive.

Qu'est-ce qui suit ? Et lorsque nous posons cette question, c'est vraiment pour considérer jusqu'où vous voulez aller dans votre voyage de la récursivité.

Et cela nous amène à une autre vidéo que nous allons publier, connue sous le nom de modèles mentaux algorithmiques pour le backtracking.

Et c'est toute la notion que nous résolvons des problèmes encore plus complexes en regardant un espace de décision et en passant récursivement pour voir si notre décision était bonne ou mauvaise, et en revenant en arrière pour voir si nous pouvons résoudre la solution d'une autre manière.

Et c'est la prochaine phase que je pense importante pour comprendre la récursivité.

Donc merci beaucoup à tous pour avoir regardé.

Assurez-vous de consulter ma chaîne youtube.com slash the symbol engineer et de me connecter sur youtube ou Twitter ou LinkedIn.

Et je serais ravi de discuter avec vous et de répondre à toutes les questions que vous pourriez avoir.

Donc merci, les gars, pour avoir regardé et passez une bonne journée.