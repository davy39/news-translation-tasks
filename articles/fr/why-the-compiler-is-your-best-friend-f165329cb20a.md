---
title: Pourquoi le compilateur est votre meilleur ami
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T18:18:14.000Z'
originalURL: https://freecodecamp.org/news/why-the-compiler-is-your-best-friend-f165329cb20a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C9CScad4P6wtLj8H_3AhqA.jpeg
tags:
- name: Game Development
  slug: game-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Pourquoi le compilateur est votre meilleur ami
seo_desc: 'By Richard Taylor

  Between projects I spent time researching the root causes of high-cost bugs in large
  game teams. The findings lead us to question basic C++ language features and patterns.
  This post covers obfuscation issues from a technical leaders...'
---

Par Richard Taylor

Entre les projets, j'ai passé du temps à rechercher les causes profondes des bugs coûteux dans les grandes équipes de développement de jeux. Les résultats nous ont amenés à remettre en question les fonctionnalités et les modèles de base du langage C++. Cet article traite des problèmes d'obfuscation d'un point de vue de leadership technique. Les recherches préliminaires à ces idées sont couvertes dans [Comment écrire moins de bugs](https://medium.freecodecamp.org/how-to-write-fewer-bugs-tips-for-game-developers-82e3d742f6f7).

### Principes de codage

À quoi ressemblent les normes de codage de votre équipe ? Peut-être sont-elles basées sur une norme commune ou ouverte ? Peut-être définissent-elles des noms de variables en camelCase pour la lisibilité ? Peut-être définissent-elles la mise en forme de la documentation doxy pour la maintenance ? Peut-être que rien de tout cela n'a d'importance ? Aident-elles réellement ? Avez-vous moins de bugs ou moins de malentendus ? Vos normes de codage peuvent cocher toutes les cases de votre OCD de codage, mais aident-elles réellement l'équipe à fonctionner de manière démontrablement meilleure ?

Lorsque j'ai écrit la norme de codage pour Onrush, nous avions une feuille blanche. Aucun code précédent à prendre en compte. La norme ne comprenait rien sur l'emplacement de nos accolades. Rien sur le camelCase ou les conventions de nommage avec des underscores. Rien sur la mise en forme de la documentation. En fait, nous ne l'avons même pas appelée une norme de codage. Nous nous sommes assis et avons discuté de ce qui nous importait vraiment dans notre code. Nous voulions une qualité supérieure. Pour nous et nos jeux, cela signifiait plus de temps pour l'itération, moins de temps pour la rectification. De meilleures performances et un nombre de bugs réduit.

> Nous avons écrit nos **Principes de Codage**. _Les principes de codage qui nous tiennent le plus à cœur._

Les Principes de Codage contenaient des déclarations comme : Les temps de compilation et de liaison sont une fonction de la qualité du code. Écrivez du code assertif et non défensif. La surcharge est une obfuscation. Nommez les fonctions et les classes de sorte que le code de haut niveau se lise comme du pseudocode. Étant donné un code lisible, la documentation est largement inutile. Documentez les concepts, les idées et le raisonnement, ne documentez pas le code. Le compilateur est un outil pour valider les hypothèses.

Nous avons permis aux gens d'avoir leur propre style de codage tant qu'il ne contredisait aucun des Principes de Codage. Cela a abouti à une base de code très uniforme dans l'approche fonctionnelle et flexible dans le style. Ce style flexible n'avait pas d'importance. Il n'affectait pas la lisibilité ou la compréhension car les principes de base sous-tendaient tout.

Si vous ne l'avez pas essayé, arrêtez d'écrire Physics::Simulation.Update(dt) et commencez à écrire updateThePhysicsSimulationForThisTimeStep(dt). Lorsque j'ai commencé à écrire des noms de fonctions descriptifs, j'ai commencé à réfléchir aux données et aux transformations appliquées. Le premier est obscurément orienté objet. Le second est le choix d'un nom de fonction qui décrit les opérations et des noms de données qui décrivent l'information. Visez un code de haut niveau qui décrit clairement les opérations fonctionnelles. Qui montre clairement les dépendances des données. Visez un code de haut niveau qui n'a pas besoin de documentation.

### Le compilateur est un outil pour vérifier les hypothèses

_Lorsque je code en C++, le compilateur est mon meilleur ami. Il scrute chaque ligne de code. Il encode mes pensées en code exécutable. Il me montre mes hypothèses et mes malentendus. Il expose mes faiblesses humaines. Mais le compilateur n'est pas un lecteur de pensées. Il ne possède pas de pouvoirs psychiques. Seulement une diligence inébranlable pour produire un code correct._

Le compilateur applique les règles strictes du langage C++ pour vérifier la correction de mon code. Bien que, à cet égard, le langage C++ ne soit pas exact. C++ a de nombreuses façons d'être inexact. De nombreuses façons de demander au compilateur de faire des hypothèses. Si j'ai appris une chose au fil des ans, c'est celle-ci : faire des hypothèses vous attirera toujours des ennuis.

Alors que C++ continue de croître et de gonfler jusqu'à la taille d'une étoile naine, il est facile de négliger les fondamentaux. Ces concepts de programmation de base travaillent-ils pour ou contre votre équipe ? Les exemples et commentaires ci-dessous concernent spécifiquement C++, mais s'appliquent à de nombreux langages modernes.

### Le coût <vrai> du polymorphisme

Commençons donc par le début avec le polymorphisme. Introduit en 1983 lorsque 'C avec classes' a été renommé C++. Le polymorphisme permet à de nombreuses fonctions ou méthodes d'avoir le même nom. Le compilateur sélectionnera la fonction correcte en utilisant les types des paramètres. Il y a cependant un problème fondamental ici. Quand est-il bon d'avoir des choses différentes avec le même nom ?

Considérons cet exemple typique de C++ 101 où nous avons des variantes d'une fonction ou méthode FileWrite.

```h
// Fonctions polymorphes simples d'écriture de fichier pour int, short et char 

bool FileWrite(int i);
bool FileWrite(short f);
bool FileWrite(char c);
```

Cela semble pratique. Je peux simplement appeler FileWrite avec n'importe quel type et le compilateur s'en chargera. Le compilateur a une connaissance parfaite du code et choisira les fonctions nécessaires pour compiler sans erreurs. Le processus est déterministe et infaillible.

Malheureusement, ce n'est pas le cas. Le compilateur peut avoir une connaissance parfaite du code, mais le compilateur n'a aucune connaissance de l'intention. Je dis au compilateur de supposer que le code que je tape implémente correctement mon intention. Maintenant, je sais pertinemment que je n'ai pas toujours raison, 20 ans de programmation m'ont appris cela. Avec cette commodité, j'ai perdu une opportunité importante pour le compilateur de trouver des erreurs dans mon code et cela finira par conduire à une erreur d'exécution difficile à trouver.

En tant que Directeur Technique ou Responsable Technique, ma principale préoccupation est de faire en sorte que l'équipe de programmation travaille efficacement ensemble. Plus l'équipe est grande, plus ce problème devient difficile. Voici une situation de développement typique utilisant le code simple ci-dessus.

```h
// Structure d'exemple simple avec trois membres int.

struct Brain 
{
 int humor;
 int intelligence;
 int empathy;
}
```

ai_brain.cpp:

```h

// Exemple d'utilisation utilisant des fonctions de fichier polymorphes 

void SaveGame(Brain& brain) 
{
  FileWrite(brain.humor);
  FileWrite(brain.intelligence);
  FileWrite(brain.empathy);
}

void LoadGame(Brain& brain) 
{
  FileRead(brain.humor);
  FileRead(brain.intelligence);
  FileRead(brain.empathy);
}
```



D'accord, toujours du C++ 101. Dans l'équipe de programmation, Tom travaille sur l'IA et Jerry travaille sur la sauvegarde du jeu. Tout le monde dans l'équipe est occupé à travailler pour la prochaine version de milestone. Soudain, le jeu plante pendant la phase de chargement et l'équipe est bloquée. Le milestone approche et tout le monde regarde Jerry pour corriger le plantage.

Le problème est que Jerry n'a pas soumis de code aujourd'hui. Jerry commence à enquêter sur le problème. Le contrôle de source montre qu'aucun changement n'a été apporté aux fichiers du module de sauvegarde du jeu aujourd'hui. Le débogueur montre le plantage dans le code de Pickup. Une autre recherche dans le SCM montre aucun changement dans le module Pickup aujourd'hui. Le flux de fichier d'entrée pour les données de sauvegarde du jeu semble être corrompu. Jerry soupire, prend une gorgée de café et continue à enquêter.

Après un certain temps, Jerry trouve le changement qui a causé les problèmes dans le code de l'IA et va parler à Tom.

```h
// Changements cassants causant une **action à distance**

struct Brain 
{
<< old
  int humor;
  int intelligence;
  int empathy;
>>> new
  short humor;
  short intelligence;
  short empathy;
=====
}
```

Jerry explique à Tom que le changement ci-dessus a causé le plantage du jeu lors de la création de pickups ! Le changement de la taille des membres a causé le désalignement du flux d'entrée. Le premier code à générer une erreur fatale due à des données incorrectes était le module Pickup.

Il s'avère que Tom a eu un plantage unique lors de la phase de chargement. Tom a supprimé la sauvegarde du jeu et les erreurs ont disparu. Comme Tom ne travaillait pas près du code de chargement, il a supposé qu'il s'agissait d'une erreur préexistante et a continué à travailler. Tom a entièrement testé son code avant de le soumettre et tous les tests ont réussi.

### **Comment cette situation aurait-elle pu être évitée ?**

> Le polymorphisme permet l'Action à Distance dans le code.

Dans l'exemple simple ci-dessus, le compilateur a commencé à générer un code exécutable différent dans les fonctions LoadGame et SaveGame. Le code dans les fonctions LoadGame et SaveGame n'a pas changé. Aucun du code dans le module de sauvegarde du jeu n'a changé. Le changement de code dans le module IA a fait que le code dans la fonction LoadGame signifiait quelque chose de différent. Ensuite, le compilateur a compilé silencieusement le nouveau code LoadGame et SaveGame sans erreur. Le code est techniquement correct mais ne satisfait plus l'intention originale.

**Considérez cette alternative.**

```h
// Fonctions d'écriture de fichier avec nom fort et typage sûr

bool FileWriteInt(int i);
bool FileWriteShort(float s);
bool FileWriteChar(char c);
```

```h
// Exemple d'utilisation utilisant des fonctions avec nom fort et typage sûr

void SaveGame(Brain& brain) 
{
  FileWriteInt(brain.humor);
  FileWriteInt(brain.intelligence);
  FileWriteInt(brain.empathy);
}
```

Dans cet exemple, les données à écrire sont explicitement définies par le code. Il n'y a pas d'hypothèses à combler par le compilateur. Si les types passés à la fonction sont incorrects, le compilateur générera une erreur.

> Nous avons transformé une erreur d'exécution intermittente dépendante des données en une erreur de compilation répétable à 100 %.

Maintenant, réévaluons notre scénario avec le nouveau code. Tom apporte ses modifications à ai/brain.h et le code échoue à la compilation. Il est immédiatement évident pour Tom que ses modifications ont causé l'erreur. Tom est en mesure de corriger le code avant de soumettre les modifications. Le compilateur découvre maintenant l'erreur à la compilation, plutôt que QA ou l'équipe trouve le bug plus tard.

Vous vous demandez peut-être pourquoi c'est un problème ? Et cela mérite une explication.

### Échelle

En tant que développeur seul dans mon propre projet, j'ai une compréhension approfondie et détaillée de mon code. Je peux tester et itérer à faible coût. Cet exemple simple de polymorphisme montre la commodité avec un très faible coût d'erreurs.

Ma carrière de développeur de jeux s'est déroulée dans de grandes équipes. À l'université, mes professeurs m'ont enseigné la POO, le polymorphisme et d'autres astuces de programmation intelligentes.

Lorsque j'étais programmeur junior, j'écrivais une méthode surchargée comme ci-dessus. Les astuces sont utiles pour moi et je vais les utiliser dans mon code. En tant que programmeur senior, je suis devenu responsable des bugs dans mon code. Je suis plus conscient du coût temporel de la maintenance du code.

En tant que Responsable Technique, je suis responsable des bugs dans le code des autres. Je suis impliqué dans la planification du travail des autres et les estimations de temps pour rendre mon équipe la meilleure. En tant que Directeur Technique, je suis responsable de l'efficacité de toute l'équipe de programmation. Je veux que l'équipe produise des fonctionnalités, PAS qu'elle corrige des bugs.

Dans une grande équipe de développement de jeux de 25, 50, 100 programmeurs ou plus, la connaissance de l'ensemble de la base de code variera. Je connais mon code en détail. Je connais le reste du code avec une certitude variable ou plutôt, une incertitude. Dans une grande équipe de programmation, je dois écrire du code en faisant des hypothèses au mieux de mes connaissances. Dans un projet plus grand, je **ferai** plus d'erreurs que dans mon propre projet solo et le coût de ces erreurs sera plus élevé.

Dans l'exemple avec Tom et Jerry, le choix de Jerry de surcharge polymorphe a rendu très facile pour Tom d'introduire un bug. Ce bug a empêché plus de la moitié de l'équipe de développement de travailler pendant près de 4 heures. Dans une équipe de 100 développeurs, cela représente environ 200 heures de travail perdues. Cela équivaut à une personne travaillant à temps plein pendant 5 semaines ! La commodité du polymorphisme pour économiser une petite quantité d'efforts de développement est complètement disproportionnée par rapport à l'impact des bugs d'_action à distance_ qui peuvent être introduits.

Pour être clair, la faute incombe à Jerry pour avoir créé une interface qui a une forte probabilité d'être utilisée incorrectement. Lorsque Tom a soumis ses modifications, tous les tests ont réussi. Tom a fait une quantité raisonnable de tests et a d'autres tâches à accomplir. Tom est tombé dans le trou, il ne l'a pas creusé.

### Portées et Espaces de Noms

Les espaces de noms ont été introduits dans The Annotated C++ Reference Manual  livre de 1990. Bien que non largement implémentés avant environ 1995.

Auparavant, tous les objets nommés dans un programme étaient globalement uniques. Cela causait des problèmes lors du partage de code entre différents projets. Si les noms dans le code partagé entraient en conflit avec l'application hôte, alors quelque chose devait être renommé. Dans un grand projet, cela pouvait avoir un impact temporel significatif.

Les espaces de noms qui délimitent l'application des bibliothèques externes sont complètement valides et un choix de développement sensé.

Il y a cependant une tendance pour les programmeurs à utiliser des espaces de noms excessifs dans une base de code de projet.

> Dans un projet, les espaces de noms permettent à la fois

>  plusieurs noms pour le même objet.

>  plusieurs objets avec le même nom.

Par base de code de projet, je veux dire spécifiquement le code tapé pour ce projet par l'équipe. Pas les bibliothèques tierces ou le code d'autres équipes distinctes dans la même entreprise.

Plusieurs alias pour le même objet rendent le code plus difficile à lire. Plusieurs objets avec le même nom augmentent les hypothèses. Nous demandons à nouveau au compilateur de supposer l'intention et de sélectionner la fonction ou la variable 'correcte'. Encore une fois, à mesure que la taille des équipes augmente, la probabilité que les hypothèses mènent à des erreurs augmente et dans les grandes équipes, il y a probablement un coût élevé d'échec.

Le schéma des espaces de noms excessifs est facile à adopter. STL et les bibliothèques populaires comme Boot sont fortement espacés. Ces projets sont fortement espacés car en réalité, ils sont des collections de micro-projets dans une seule bibliothèque. Dans ces cas, les espaces de noms sont utilisés comme prévu pour isoler le code de différents contributeurs où le refactoring des noms globaux serait inutilement difficile à orchestrer.

Cependant, ce schéma est si répandu qu'il est couramment copié par les développeurs dans leur propre code. Lors de l'écriture de nouveau code, garantir des noms uniques est facile, le compilateur vous dira immédiatement qu'il y a un problème. Dans la base de code de l'équipe, le nommage unique est bon car il évite les hypothèses. L'utilisation d'espaces de noms dans le propre code de l'équipe crée des hypothèses évitables. Ce qui permet au compilateur de choisir la classe, la fonction ou la variable _correcte_ mais avec la mauvaise intention/résultat.

> math::fast::fpow(2,10)

> math::emulation::fpow(2,10)

Lors de l'utilisation d'espaces de noms, il existe plusieurs façons de référencer la fonction et il y a la possibilité de plusieurs fonctions avec le même nom.

> fpow(2,10)

Lors de la lecture du code, le programmeur doit faire une hypothèse sur la fonction fpow() spécifique que l'auteur avait l'intention d'appeler et la fonction fpow() spécifique que le compilateur choisira réellement. Il n'y aura pas d'erreur de compilation si le code généré ne correspond pas à l'intention. Ces erreurs devront être découvertes à l'exécution.

Cela augmente la charge cognitive. Je dois maintenant suivre mentalement les espaces de noms actuels qui s'appliquent à un bloc de code donné. C'est un problème qui ne s'adapte pas bien aux grandes équipes et aux grandes bases de code.

> MathEmuFpow(2,10)

> MathFastFpow(2,10)

Il n'y a qu'une seule façon de référencer chacune de ces fonctions Fpow. Peu importe où je suis dans le code, ces fonctions ont toujours le même nom unique. Cela rend le code plus facile à lire et à comprendre en réduisant la charge cognitive sur le programmeur. Je connais l'intention de l'auteur et je connais le code que le compilateur générera.

Les espaces de noms ont des _cas d'utilisation_ valides pour contenir du code externe que vous n'aurez pas besoin de modifier et dans de nombreux cas ne pourrez pas modifier. En tant que tel, je mettrai toujours mes projets dans un espace de noms conteneur. C'est une courtoisie pour les autres équipes et programmeurs qui pourraient avoir besoin d'utiliser ce code à l'avenir. Dans les projets, les espaces de noms permettent un mauvais nommage et des hypothèses et doivent être utilisés avec parcimonie.

### Auto

La norme C++11 a introduit auto ainsi qu'une série d'autres fonctionnalités de commodité. Malheureusement, auto est _une autre fonctionnalité d'hypothèse du compilateur_ qui dit au compilateur de supposer que le code que j'ai écrit est correct. Le compilateur doit maintenant choisir les types qui permettent au code de compiler. Le problème avec cela est que je fais toujours des erreurs.

Auto prend les problèmes ci-dessus des fonctions polymorphes et les applique aux variables. Pour les fonctions polymorphes, le compilateur ne peut choisir qu'entre des fonctions avec des noms correspondants. L'utilisation de auto demande au compilateur de sélectionner N'IMPORTE QUEL type qui permettra au code de compiler !

> Auto vous permet d'écrire du code sans comprendre les types de données.

> Auto permet l'action à distance pour les variables.

La raison la plus courante que j'entends pour utiliser auto en C++ est de rendre le code plus simple et plus facile à lire. Les longs noms de types STL complexes sont souvent donnés comme justification pour utiliser auto. Il est courant de typedef les longs noms de types STL en noms abrégés pratiques. Pourquoi ne pas sauter cette étape et utiliser auto ?

Rendre le code plus simple est un argument de soutien erroné. La complexité conduit toujours à plus de complexité. Si un autre système est compliqué et difficile à comprendre, cette complexité n'est pas supprimée par l'utilisation de auto. L'utilisation de auto masque la complexité en faisant des hypothèses abrégées. (La seule façon de s'attaquer à la complexité qui s'échappe des API est de refactoriser l'API.)

Si je **ne** connais **pas** le type que auto résoudra, alors je ne considère pas tous les cas d'échec possibles. Si je **connais** le type que auto résoudra, alors je devrais utiliser ce type à la place. L'utilisation du type spécifique encode mieux mon intention. Si le compilateur me donne une erreur, alors j'ai appris que mes hypothèses sur les types utilisés sont incorrectes. L'utilisation du type spécifique protège également le code contre le refactoring ultérieur et l'action à distance.

Le coût de l'utilisation de auto dans un projet personnel est probablement nul. Le coût de l'utilisation de auto dans une grande équipe de développement est potentiellement élevé et disproportionné par rapport à tout bénéfice.

### Le compilateur est mon ami

Le compilateur est mon ami et mon allié pour affirmer mes hypothèses pendant le développement. Les bugs trouvés par le compilateur doivent par définition être corrigés avant de soumettre les modifications.

> En concevant mon code pour générer des erreurs de compilation lorsqu'il est utilisé incorrectement, j'aide les autres programmeurs de mon équipe.

Cela correspond à la façon dont nous, programmeurs, travaillons. Je tape du code puis je compile dans une boucle d'itération courte et rapide. Je peux même utiliser un IDE qui compile en continu en arrière-plan pendant que je tape. Si le compilateur trouve mon erreur rapidement après la frappe, le coût de correction est presque nul.

Les grandes équipes de développement de jeux amplifient l'impact des bugs. Si une équipe de centaines de personnes ne peut pas travailler, les heures de développement sont perdues à un rythme vraiment effrayant. Les grands projets de développement de jeux auront généralement de grandes équipes d'assurance qualité pour trouver les bugs. Cela introduit des retards de temps significatifs et des coûts de découverte, de correction et de vérification des bugs une fois que le bug a été soumis dans la build.

En tant que Directeur Technique, je dois mettre un coût sur la commodité des fonctions polymorphes, des espaces de noms, de auto et d'autres fonctionnalités de commodité de base du langage. En comparant cela à l'impact et au coût des bugs supplémentaires provenant d'hypothèses non vérifiées.

À l'université, on m'a enseigné que le compilateur est un outil pour traduire le code source en code machine exécutable. Pendant longtemps dans ma carrière de programmeur, je me suis concentré sur la technologie et l'optimisation. Je pensais savoir comment utiliser le compilateur pour générer le meilleur code, mais je passais à côté du tableau d'ensemble.

Écrire du code source qui utilise le compilateur pour valider l'intention de l'auteur est tout aussi important que de générer un code exécutable optimal.

> Le compilateur est en fait un outil pour traduire l'intention en code machine exécutable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C9CScad4P6wtLj8H_3AhqA.jpeg)