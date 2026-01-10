---
title: La manière facile d'obtenir des interfaces TypeScript à partir de code C#,
  Java ou Python dans n'importe quel IDE
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-19T16:13:52.000Z'
originalURL: https://freecodecamp.org/news/the-easy-way-to-get-typescript-interfaces-from-c-java-or-python-code-in-any-ide-c3acac1e366a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wTwVD_QDNfAW4BgqrXhVBA.png
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: TypeScript
  slug: typescript
seo_title: La manière facile d'obtenir des interfaces TypeScript à partir de code
  C#, Java ou Python dans n'importe quel IDE
seo_desc: 'By Leonardo Carreiro

  Who has never experienced the situation where you have to fix a bug and at the end
  you find out that the error on the server was a missing field coming from a HTTP
  request? Or an error on the client, where your Javascript code wa...'
---

Par Leonardo Carreiro

Qui n'a jamais vécu la situation où vous devez corriger un bug et à la fin vous découvrez que l'erreur sur le serveur était un champ manquant provenant d'une requête HTTP ? Ou une erreur sur le client, où votre code Javascript essayait d'accéder à un champ qui n'existe pas dans les données provenant d'une réponse HTTP du serveur ? Bien souvent, ces problèmes sont simplement causés par un nom différent pour ce champ entre le code du client et celui du serveur.

### Le problème

Tous ceux qui travaillent à la fois sur le back-end et le front-end d'une application web doivent interroger et traiter des données côté serveur, puis retourner ces données pour qu'elles soient consommées par le client de l'application. Peu importe le nombre de couches de votre architecture, vous aurez toujours l'interface entre le serveur et le client, où les requêtes et réponses HTTP transportent les données entre ces deux côtés dans les deux sens.

Et ce n'est pas seulement une question de bugs avec des noms différents — personne ne peut se souvenir de la structure de données complète de toutes les entités de l'application. Lorsque vous écrivez du code, il est courant de taper un `.` (ou `->` ou `["`). Si vous n'écrivez pas un nom incorrect là, vous vous arrêtez et vous demandez : « Quel était le nom de ce champ ? ». Après avoir passé du temps à essayer de vous en souvenir, vous abandonnez et choisissez le chemin le plus ennuyeux. Vous prenez votre souris et commencez à chercher le fichier où vous définissez tous ces champs auxquels vous devez accéder.

> La partie ennuyeuse de l'écriture de code est lorsque vous ne pouvez pas déterminer par vous-même quel est le bon code que vous devez écrire.

Parfois, ce n'est pas grave de simplement le googler et vous trouvez une réponse Stack Overflow avec le code prêt à être copié. Mais lorsque vous devez rechercher cette réponse dans votre projet, un grand projet, où le code qui définit la structure de données à laquelle vous devez accéder se trouve dans un fichier qui n'a pas été écrit par vous… le temps que vous passez sur ce chemin peut être d'un ou deux ordres de grandeur plus grand que le temps passé à simplement écrire le bon nom.

### TypeScript à la rescousse

Lorsque nous écrivions simplement du vieux Javascript, nous n'avions pas d'option pour éviter ce chemin ennuyeux dans ces situations. Mais ensuite, à la fin de 2012, [Anders Hejlsberg](https://twitter.com/ahejlsberg) (le père du langage C#) et son équipe ont créé TypeScript. Leur mission était de faciliter la création de grands projets Javascript qui évoluent.

La partie amusante est que, bien que ce nouveau langage était un **superset** de Javascript, son objectif était de vous permettre de faire seulement un **subset** des choses que vous faisiez avec Javascript. Il **a ajouté de nouvelles fonctionnalités** comme les classes, les énumérations, les interfaces, les types de paramètres et les types de retour.

Mais il a également **supprimé des possibilités**, même des choses qui n'étaient pas trop mauvaises, comme passer un nombre en tant que paramètre à `document.getElementById()`, et utiliser l'opérateur `*` avec un nombre et une chaîne numérique comme opérandes. Vous ne pouvez plus compter sur les conversions de type implicites, vous devez être explicite et utiliser `.toString()` ou `parseInt(str)` lorsque vous voulez une conversion de type. Mais la meilleure chose que vous ne pouvez plus faire **est d'accéder à un champ qui n'existe pas dans un objet.**

Ainsi, lorsqu'un problème est résolu, un nouveau prend souvent sa place. Et ici, le nouveau problème était la duplication de code. Les gens ont commencé à remplacer le principe DRY (Don't Repeat Yourself) par le principe WET (Write Everything Twice).

Il est bon de pratiquer l'utilisation de différentes classes dans différentes couches, pour différents objectifs, mais ce n'est pas le cas ici. Si vous avez trois couches (A -> B -> C), vous ne devriez pas avoir de structures de données spécifiques **pour chaque** couche (une pour A, une pour B et une pour C), mais plutôt **pour chaque interface entre celles-ci** (une entre A et B et une autre entre B et C). Ici, sauf si votre back-end est une application Node.js, nous devons dupliquer ces déclarations de structures de données car nous sommes à l'interface entre deux langages de programmation différents.

Pour éviter d'écrire tout deux fois, il ne nous reste qu'une seule option…

### Génération de code

Un jour, je travaillais sur un projet .NET avec Entity Framework. Il avait un diagramme de modèle dans un fichier .edmx, et si je modifiais ce fichier, je devais sélectionner une option pour générer les classes pour les entités POCO (Plain Old CLR Objects).

Cette génération de code était effectuée par T4, un moteur de modèle de Visual Studio qui fonctionnait avec un fichier .tt comme modèle pour une classe C#. Il exécutait le code qui lisait le fichier de modèle .edmx et produisait les classes dans des fichiers .cs. Après m'en être souvenu, j'ai pensé que cela pourrait être une solution pour générer des interfaces TypeScript et j'ai commencé à essayer de le faire fonctionner.

D'abord, j'ai essayé d'écrire mon propre modèle. Lorsque je travaillais avec cela et Entity Framework, je n'ai jamais eu à changer le modèle .tt. Ensuite, j'ai découvert que Visual Studio ne supportait pas la coloration syntaxique dans les fichiers .tt — c'était comme programmer dans le bloc-notes mais en pire.

En plus d'avoir le code C# de la logique de génération, j'avais également mélangé avec celui-ci le code TypeScript qui devait être généré, comme [celui-ci](https://gist.github.com/robfe/4583549). J'ai installé une extension Visual Studio pour obtenir le support de syntaxe, mais l'extension définissait les couleurs de syntaxe uniquement pour le thème clair de Visual Studio, et j'utilise le thème sombre. Les couleurs de syntaxe du thème clair sur le thème sombre étaient illisibles, donc j'ai dû changer également le thème de mon Visual Studio.

Maintenant, avec la coloration syntaxique, tout était bon. Il était temps de commencer à écrire du code. J'ai cherché sur Google un exemple fonctionnel. Mon idée était de le modifier pour mes besoins après l'avoir fait fonctionner, mais… ÇA N'A PAS MARCHÉ !

```
System.IO.FileNotFoundException: Impossible de charger le fichier ou l'assembly 'System.Runtime, Version=4.2.1.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a' ou l'une de ses dépendances. Le système ne trouve pas le fichier spécifié.
```

J'ai essayé beaucoup d'exemples "fonctionnels" trouvés en cherchant sur Google, mais aucun d'entre eux n'a fonctionné. J'ai pensé que peut-être le problème n'était pas avec Visual Studio ou avec le moteur T4 — peut-être que le problème était moi, qui l'utilisait mal.

Ensuite, Google m'a conduit à ce [problème](https://github.com/dotnet/core/issues/2000) dans le dépôt .NET Core et j'ai découvert que cela ne fonctionnait pas avec les projets ASP.NET Core. Mais cette erreur était une erreur courante dans le monde .NET, donc j'ai pensé que je pourrais essayer de trouver une solution de contournement. J'ai cherché cette version 4.2.1.0 de System.Runtime.dll, je l'ai trouvée, et j'ai essayé de la mettre dans différents répertoires pour voir si Visual Studio pouvait la trouver… mais rien n'a fonctionné.

Finalement, j'ai utilisé Process Explorer pour voir quelle version de System.Runtime Visual Studio avait chargée, et c'était la version 4.0.0.0. J'ai essayé d'utiliser un `bindingRedirect` pour forcer l'utilisation de la même version (comme je l'ai décrit [ici](https://github.com/dotnet/core/issues/2000#issuecomment-456413662)), et cela a fonctionné ! Je ne pouvais pas croire que je n'aurais plus à dupliquer et à synchroniser manuellement mes structures de données entre le serveur et le client.

J'ai commencé à y réfléchir davantage, et une autre pensée me tracassait…

### En valait-il la peine ?

Je travaille pour une grande compagnie pétrolière, avec beaucoup d'applications héritées. Un ami devait travailler avec une machine virtuelle parce que l'application qu'il déboguait ne fonctionnait parfois que sous Windows XP. Une autre application sur laquelle j'ai dû travailler un jour ne fonctionnait qu'avec Visual Studio 2010. Une autre qui utilisait Code Contracts ne fonctionnait qu'avec Visual Studio 2013 parce que l'extension Code Contracts ne fonctionnait pas dans Visual Studio 2015 ou 2017.

Depuis 2012, lorsque j'ai commencé à travailler là-bas jusqu'au début de 2019, je n'ai jamais eu l'occasion de développer une nouvelle application. Tout mon travail a toujours été avec les désordres d'autres développeurs. L'année dernière, j'ai commencé à étudier davantage l'architecture logicielle, et j'ai lu le livre "Clean Architecture" de l'oncle Bob.

Maintenant que j'ai commencé cette nouvelle année avec cette opportunité, pour la première fois dans cette entreprise, je crée une application web à partir de zéro et je veux faire un bon travail. J'ai choisi ASP.NET Core pour mon back-end, React pour le front-end, et ce sera l'une des premières applications de cette entreprise à fonctionner dans un conteneur Docker dans notre nouveau cluster Kubernetes.

Un autre pauvre développeur devra travailler sur ce projet à l'avenir, avec mon code et tout mon désordre, et je ne veux pas qu'ils aient à gérer du mauvais code. Je veux que tous les développeurs après moi veuillent travailler sur ce projet. Cela n'arrivera pas s'ils doivent perdre une journée de travail juste pour faire fonctionner la génération du code client à partir des structures de données du back-end. Ils me détesteraient alors (et certains me détesteraient déjà pour avoir mis du code TypeScript dans un projet lorsque TypeScript était encore en version 0.9).

> Lorsque nous écrivons du code qui n'est pas le nôtre, nous avons la responsabilité de le rendre facile pour les autres à travailler dessus.

Après avoir réfléchi à cela, je suis parvenu à une conclusion :

> **Nous devons éviter les dépendances à tout ce qui ne peut pas être géré par le gestionnaire de paquets de la technologie choisie.**

Dans ce cas, en plus des dépendances à Visual Studio et Windows, je ferais dépendre le projet d'un correctif qui devrait être corrigé par Microsoft (et [il semble que cela n'ait aucune priorité](https://developercommunity.visualstudio.com/content/problem/358905/filenotfoundexception-systemruntime-version4210-wh.html)). Il est donc préférable de dupliquer ce code et de le synchroniser manuellement plutôt que de mettre une dépendance sur ce moteur T4.

J'ai choisi d'utiliser .NET Core, mais si un développeur à l'avenir veut travailler sur ce projet en utilisant Linux, je ne peux pas l'en empêcher.

### La solution finale (TL;DR)

La duplication de code est mauvaise, mais la dépendance à des outils tiers est pire. Alors, que pouvons-nous faire pour éviter la duplication des structures de données et ne pas dépendre d'un IDE / plugin / extension / outil spécifique pour le développement ?

Il m'a fallu un certain temps pour réaliser que le seul outil dont j'avais besoin était là tout ce temps, à l'intérieur du runtime du langage : **Reflection**.

J'ai réalisé que je pouvais écrire du code qui s'exécute au démarrage de mon application back-end ASP.NET Core uniquement en mode développement. Ce code pourrait utiliser la réflexion pour lire les métadonnées sur les noms et les types de toutes les structures de données que je voulais générer des interfaces TypeScript. Je devais simplement mapper les primitives C# aux primitives TypeScript, écrire les définitions .d.ts TypeScript dans un dossier spécifique, et j'aurais terminé.

Chaque fois que je modifiais une structure de données dans le back-end, cela écraserait les définitions d'interfaces à l'intérieur des fichiers .d.ts lorsque j'exécutais le code pour le tester. Lorsque j'en arrivais à la partie de l'écriture du code client pour utiliser la structure de données modifiée, les interfaces seraient déjà mises à jour.

Cette approche peut être utilisée par des projets en .NET, Java, Python et tout autre langage qui prend en charge la réflexion de code, sans ajouter de dépendance à un IDE / plugin / extension / outil.

J'ai écrit un exemple simple en utilisant C# avec ASP.NET Core et je l'ai publié sur GitHub [ici](https://github.com/lmcarreiro/cs2ts-example). Il prend simplement toutes les classes qui héritent de `Microsoft.AspNetCore.Mvc.ControllerBase` et tous les types de paramètres et les types de retour des méthodes publiques qui ont des attributs `HttpGet` ou `HttpPost`.

Voici à quoi ressemblent les interfaces générées :

![Image](https://cdn-media-1.freecodecamp.org/images/-4fmTbfc18e-s41lvRdt0smq-f78Dma1Hrws)
_Classes C# (à gauche) vs interfaces TypeScript (à droite)_

#### Vous pouvez générer d'autres types de code également

Je l'ai utilisé pour générer des interfaces et des énumérations pour les structures de données uniquement, mais pensez au code ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/87YihvvupEwjtjXBcRj6Gpr-2oCQVRHVbp7s)
_Code TypeScript d'une API d'exemple qui pourrait être générée automatiquement_

C'est beaucoup moins pénible de garder ce code synchronisé avec tous les contrôleurs et actions MVC possibles que de garder les structures de données synchronisées. Mais dois-je écrire ce code à la main ? Ne pourrait-il pas être généré également ?

Je ne peux pas générer d'interfaces C# à partir d'implémentations concrètes C#, car j'ai besoin que le code compile et s'exécute avant de pouvoir utiliser la réflexion pour le générer. Mais avec le code client qui doit être synchronisé avec le code serveur, je peux le générer. Cette méthode de génération de code peut être utilisée au-delà des interfaces de structures de données.

#### Si vous n'aimez pas TypeScript…

Il n'est pas nécessaire de l'écrire avec TypeScript. Si vous n'aimez pas TypeScript et préférez utiliser du Javascript simple, vous pouvez écrire vos fichiers .js et utiliser TypeScript simplement comme un outil (si vous utilisez Visual Studio Code, vous l'utilisez déjà). De cette manière, vous pouvez générer des fonctions d'assistance qui convertissent vos structures de données en structures identiques. Cela semble étrange, mais cela aiderait le TypeScript Language Service à analyser votre code et à indiquer à Visual Studio Code les champs qui existent dans chaque objet, afin qu'il puisse vous aider à écrire votre code.

![Image](https://cdn-media-1.freecodecamp.org/images/FBWck84VzHqiE5gidEkthJ9eO-K86D6iIOP2)
_Utilisation d'informations de typage avec du Javascript simple_

### Conclusion

Nous, en tant que développeurs, avons une responsabilité envers les autres développeurs qui devront travailler sur notre code. Ne laissez pas un désordre pour qu'ils nettoient, car ils ne le feront pas (ou du moins ils ne voudront pas !). Ils ne feront probablement que l'empirer pour le suivant.

Vous devez éviter à tout prix toute dépendance de développement et d'exécution qui ne peut pas être gérée par le gestionnaire de paquets. Ne faites pas de votre projet celui que les autres développeurs détesteront travailler.

Merci d'avoir lu !

PS 1 : Ce [dépôt avec mon code](https://github.com/lmcarreiro/cs2ts-example) est juste un exemple. Le code qui convertit les classes C# en interfaces TypeScript n'est pas bon. Vous pouvez faire beaucoup mieux, et peut-être avons-nous déjà un package NuGet qui fait cela.

PS 2 : J'adore TypeScript. Si vous aimez aussi TypeScript, vous pourriez vouloir jeter un coup d'œil à ces liens, avant qu'il ne soit annoncé par Microsoft en 2012 :

* [**Quel est le prochain tour du père de C# chez Microsoft ?** Le Microsoft Technical Fellow Anders Hejlsberg travaille sur quelque chose en rapport avec les outils JavaScript. Voici quelques indices sur son dernier projet.](https://www.zdnet.com/article/whats-microsofts-father-of-cs-next-trick/)
* [Une discussion HackerNews : **« Anders Hejlsberg a raison : vous ne pouvez pas maintenir de grands programmes en JavaScript »**](https://news.ycombinator.com/item?id=4067696)
* [Une vidéo Channel9 : **« Anders Hejlsberg : Présentation de TypeScript »**](https://channel9.msdn.com/posts/Anders-Hejlsberg-Introducing-TypeScript)