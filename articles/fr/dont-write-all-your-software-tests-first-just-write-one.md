---
title: Ne pas écrire tous vos tests logiciels en premier – écrivez-en simplement un
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-11T05:31:23.000Z'
originalURL: https://freecodecamp.org/news/dont-write-all-your-software-tests-first-just-write-one
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a5c740569d1a4ca252b.jpg
tags:
- name: 'automation testing '
  slug: automation-testing
- name: Quality Assurance
  slug: quality-assurance
seo_title: Ne pas écrire tous vos tests logiciels en premier – écrivez-en simplement
  un
seo_desc: 'By Alex Bunardzic

  Test Driven Development (TDD) is sometimes described as “writing tests first”. The
  TDD mantra states that we should not write code before we have written automated
  tests that exercise that code. Writing code first is considered subo...'
---

Par Alex Bunardzic

Le développement piloté par les tests (TDD) est parfois décrit comme « écrire les tests en premier ». Le mantra du TDD stipule que nous ne devrions pas écrire de code avant d'avoir écrit des tests automatisés qui exerceront ce code. Écrire le code en premier est considéré comme sous-optimal.

Et bien sûr, écrire le code en premier est la manière dont nous développons des logiciels en suivant le modèle dit en cascade. Dans ce modèle, nous divisons les activités de développement logiciel en étapes. Par exemple, nous avons une étape de « collecte des exigences », nous avons une étape de « construction de l'application », nous avons une étape de « test de l'application », nous avons une étape de « déploiement de l'application », et ainsi de suite.

Mais en quoi cela est-il différent de la méthodologie agile ? N'avons-nous pas exactement les mêmes étapes en agile ? 

### Méthodologie Agile vs Méthodologie en Cascade

Bien sûr que si. La différence cruciale est que dans l'agile, ces étapes ne sont pas verrouillées. 

Dans le modèle en cascade, nous verrouillons les étapes et les exécutons dans une séquence stricte. Cela signifie que nous ne commencerons pas à construire l'application de livraison tant que les exigences n'auront pas été recueillies, complétées, signées et gelées. Une fois les exigences gelées (et contrôlées par nos politiques de gestion des changements), nous passons à l'étape suivante (ou phase) – la construction de l'application. 

Et de manière similaire, nous ne passerons pas à l'étape de test tant que l'ensemble de l'application n'aura pas été construite et que nous n'aurons pas atteint le jalon de code complet, à partir duquel les changements de code ont été gelés. 

Une fois le code gelé (et le gel du code est alors contrôlé par nos politiques de gestion des changements), nous le transmettons aux testeurs. La phase de test commence, et seulement une fois que tous les tests ont été complétés (et à condition qu'aucun défaut significatif n'ait été détecté), nous passons à la phase de déploiement.

Dans l'agile, nous effectuons toutes les activités ci-dessus en parallèle. En même temps. Nous continuons à travailler sur les histoires utilisateur (spécifications) tout en construisant simultanément l'application de livraison. Alors que nous construisons l'application, nous la testons également. Et alors que nous construisons et testons l'application, nous la déployons également. 

Nous apprenons de l'application de livraison déployée en production et utilisons cet apprentissage validé comme le retour d'information qui informera les nouvelles histoires utilisateur. De cette manière, la boucle est fermée, et nous itérons, améliorant la valeur de manière incrémentielle.

La seule manière de permettre une telle livraison itérative de flux de valeur est de s'appuyer sur des tests automatisés. Et comme nous l'avons décrit, ces tests sont écrits très tôt dans le jeu. En fait, les tests doivent être écrits avant que nous écrivions le code de livraison.

Pourquoi alors le titre de cet article est-il « Ne pas écrire tous vos tests en premier, écrivez-en simplement un » ? Cela semble un peu confus. Déballons le sens de ce titre. Mais d'abord, voici un aperçu de la technologie que nous allons utiliser :

### La pile technologique utilisée pour cet exercice

Dans le but de garder l'exercice simple et facile à suivre, j'ai choisi la plateforme **[.NET Core](https://dotnet.microsoft.com/)** avec la plateforme de test **[xUnit.net](https://xunit.net/)**. Pour suivre les exemples de code, veuillez installer `.NET Core` et `xUnit.net`.

Afin de pouvoir exécuter le code exemple, veuillez ouvrir le fichier `./tests/tests.csproj` et ajouter cette ligne à l'`ItemGroup` :

```c#
<ProjectReference Include="../app/app.csproj" />
```

Vous êtes maintenant prêt à suivre les exercices de codage.

## Un exemple simple

Pour comprendre la différence entre écrire tous les tests en premier et écrire un test en premier, il est peut-être préférable de montrer plutôt que de simplement dire. 

Alors essayons de construire un exemple simple – pour cet exercice, j'ai choisi un cas trivial de calcul d'un pourboire dans un restaurant. Souvent, nous nous trouvons dans une situation où nous voulons donner un pourboire au restaurant pour le service, mais il est difficile de calculer les pourcentages dans notre tête. Donc, un petit `Calculateur de Pourboire` pourrait être utile.

Voici les attentes :

**En tant que client  
Je veux calculer la note totale (total plus le pourboire)  
Parce que je veux complimenter le restaurant pour le service**

### Scénario #1 : Le client calcule le total pour un service terrible

Étant donné que le total du restaurant est de 100,00 $  
Et que le service était terrible  
Lorsque le calculateur de pourboire calcule le total à payer  
Alors le calculateur de pourboire affiche un total de 100,00 $

### Scénario #2 : Le client calcule le total pour un service médiocre

Étant donné que le total du restaurant est de 100,00 $  
Et que le service était médiocre  
Lorsque le calculateur de pourboire calcule le total à payer  
Alors le calculateur de pourboire affiche un total de 105,00 $

### Scénario #3 : Le client calcule le total pour un bon service

Étant donné que le total du restaurant est de 100,00 $  
Et que le service était bon  
Lorsque le calculateur de pourboire calcule le total à payer  
Alors le calculateur de pourboire affiche un total de 110,00 $

### Scénario #4 : Le client calcule le total pour un excellent service

Étant donné que le total du restaurant est de 100,00 $  
Et que le service était excellent  
Lorsque le calculateur de pourboire calcule le total à payer  
Alors le calculateur de pourboire affiche un total de 115,00 $

### Scénario #5 : Le client calcule le total pour un service exceptionnel

Étant donné que le total du restaurant est de 100,00 $  
Et que le service était exceptionnel  
Lorsque le calculateur de pourboire calcule le total à payer  
Alors le calculateur de pourboire affiche un total de 120,00 $

Mettons maintenant en œuvre l'histoire utilisateur ci-dessus.

Nous voyons que l'histoire a 5 critères d'acceptation (c'est-à-dire des scénarios). Nous passons maintenant à la phase d'analyse – réfléchissons à la première fonctionnalité que notre application `Calculateur de Pourboire` devrait implémenter. Mais d'abord, ouvrons le terminal de ligne de commande et créons le nouveau répertoire :

```
md TipCalculator
cd TipCalculator
```

et créons les répertoires `app` et `tests` à l'intérieur du répertoire `TipCalculator`.

Maintenant, `cd tests` et exécutez : 

```.net
dotnet new xunit
```

Ensuite, `cd ..` et `cd app`, puis exécutez : 

```
dotnet new classlib
```

Nous sommes maintenant prêts à commencer !

Ouvrez votre éditeur de texte préféré (le mien est [Visual Studio Code](https://code.visualstudio.com/)) et concentrez-vous sur les attentes. Quel comportement attendons-nous du `Calculateur de Pourboire` ?

Pour réduire la portée de nos attentes, il est généralement utile de prendre un critère d'acceptation (c'est-à-dire un scénario) et de se concentrer d'abord sur celui-ci. Prenons le scénario #1 :

### Scénario #1 : Le client calcule le total pour un service terrible

Étant donné que le total du restaurant est de 100,00 $  
Et que le service était terrible  
Lorsque le calculateur de pourboire calcule le total à payer  
Alors le calculateur de pourboire affiche un total de 100,00 $

Dans le cas où le service était terrible, nous n'ajoutons aucun pourboire, et le `Calculateur de Pourboire` calcule un pourboire de 0,00 $. Alors, comment automatiser ce scénario ?

Ma première attente serait que nous devons d'une manière ou d'une autre informer le `Calculateur de Pourboire` que le service était terrible. Nous tapons soit le mot « Terrible » dans le champ de saisie, soit nous sélectionnons « Terrible » dans la liste des évaluations de service disponibles. 

La première chose à faire ici est donc d'articuler certaines attentes concernant la capacité du `Calculateur de Pourboire` à être notifié que le service était terrible.

J'aime toujours commencer par l'attente que ce que l'utilisateur saisit est valide. Je commencerais donc par écrire un test qui vérifie si l'évaluation « Terrible » est reconnue par le `Calculateur de Pourboire` comme une évaluation valide. 

Allez dans le répertoire `tests`, renommez le fichier `UnitTest1.cs` autogénéré en `TipCalculatorTests.cs` et ajoutez le test suivant :

```c#
[Fact]
public void CheckIfRatingTerribleIsValid(){	
  var expectedResponseForValidRating = true;	
  var actualResponseForValidRating = false;	
  Assert.Equal(expectedResponseForValidRating, 
  actualResponseForValidRating);
}
```

Maintenant, allez à la ligne de commande, `cd tests`, et exécutez : 

```
dotnet test
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-21.png)

Bien sûr, le test trivial ci-dessus échouera, car nous avons codé en dur les valeurs. Mais il est toujours bon de s'assurer que nous voyons nos tests échouer avant de continuer. Ne pas observer un test échouer peut nous donner un faux sentiment de sécurité plus tard, si aucun test n'échoue et que nous finissons par penser que tout fonctionne comme prévu.

Quelques observations supplémentaires sur le test ci-dessus :

* Il est utile que le nom du test soit descriptif. J'ai choisi `CheckIfRatingTerribleIsValid` pour communiquer le fait que nous devons nous assurer que notre application est capable de reconnaître nos commandes.
* Il est également utile que les noms des variables attendues et réelles soient descriptifs. J'ai choisi `expectedResponseForValidRating` et `actualResponseForValidRating` comme étant assez indicatifs de ce que nous attendons dans ce test, et aussi de la valeur réelle que le `Calculateur de Pourboire` produira.
* Le test est un code source de première classe et doit être abordé avec le même soin que le code de production.

## Première décision de conception

À ce stade, nous sommes obligés de prendre une décision – comment notre `Calculateur de Pourboire` naissant saura-t-il si l'évaluation du service fournie par l'utilisateur est valide ou non ? 

La décision de conception qui vient à l'esprit est que le `Calculateur de Pourboire` doit être capable de stocker et de récupérer certaines données. Dans ce cas, les données qui nous intéressent sont l'évaluation du service.

Si nous revenons à l'histoire utilisateur et examinons les cinq critères d'acceptation, nous verrons que les attentes sont que le `Calculateur de Pourboire` doit être capable de reconnaître cinq évaluations de service différentes :

1. Terrible
2. Médiocre
3. Bon
4. Excellent
5. Exceptionnel

Le moyen le plus simple de faire en sorte que le `Calculateur de Pourboire` stocke ces informations serait de le doter d'un tableau ou d'une liste. 

Mais plutôt que de nous précipiter pour implémenter cette liste, nous devrions examiner à nouveau les attentes, pour voir s'il y a autre chose que nous aurions pu manquer. Et il y en a – non seulement le `Calculateur de Pourboire` doit être capable de reconnaître les évaluations de service valides, mais il doit également être capable d'associer chaque évaluation à une valeur de pourcentage. 

Notre analyse montre les associations suivantes :

1. Terrible => 0%
2. Médiocre => 5%
3. Bon => 10%
4. Excellent => 15%
5. Exceptionnel => 20%

Dans ce cas, un simple tableau ou une simple liste ne suffira pas pour contenir les associations ci-dessus. Quelle est la structure de données suivante la plus simple qui nous permettra d'implémenter ces associations ? Après avoir fait un peu de recherche, nous découvrons que `Hashtable` est probablement la structure de données la plus adaptée qui peut couvrir nos besoins avec le moins de formalités.

Nous naviguons maintenant vers le répertoire `app` et renommons le fichier `Class1.cs` autogénéré en `TipCalculator.cs`. Nous voulons maintenant ajouter une `Hashtable` qui contiendra les évaluations de service et les valeurs de pourcentage associées :

```c#
System.Collections.Hashtable ratingPercentages = new System.Collections.Hashtable();
```

C'est le bon moment pour rappeler que le TDD se concentre sur le couplage des attentes au comportement de l'application, et non à la structure de l'application. Sachant cela, nous devons modifier notre test pour faire en sorte que le `Calculateur de Pourboire` exhibe un certain comportement. Le test codifie certaines attentes concernant la manière dont l'application doit se comporter, et l'application en cours d'exécution fournit la preuve du comportement attendu.

Mais quelle est la preuve du comportement de l'application ? Il n'y a pas d'autre moyen pour nous d'évaluer et de juger le comportement de l'application autre que par l'examen des valeurs que l'application en cours d'exécution produit. 

Dans ce cas, nous attendons de l'application en cours d'exécution qu'elle produise les valeurs `true` ou `false` (valeurs booléennes) après avoir demandé à l'application si une certaine valeur (c'est-à-dire l'évaluation du service) est valide.

Pour apprendre à l'application à se comporter de la manière attendue, nous devons la doter d'une API. Dans ce cas, nous concevons l'API comme suit :

```c#
public bool CheckIfRatingIsValid(string rating)
```

Dans notre test, nous allons modifier la valeur attendue réelle pour exercer l'application en cours d'exécution et collecter la valeur de sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image001--1-.jpg)

Comme vous pouvez le voir sur la capture d'écran ci-dessus, nous avons instancié `TipCalculator`, mais lorsque nous tentons de demander à l'instance de vérifier si l'évaluation fournie (« Terrible ») est valide, l'éditeur se plaint de ne pas trouver cette méthode.

Bien sûr, la méthode n'a pas encore été implémentée. C'est maintenant le moment d'aller de l'avant et de le faire :

```c#
public bool CheckIfRatingIsValid(string rating) {	
  return false;
}
```

Maintenant que la méthode est implémentée, le test fonctionne ; voici la liste complète :

```c#
using Xunit;
using app;

namespace tests {	
  public class TipCalculatorTests {		
    TipCalculator tipCalculator = new TipCalculator();		

    [Fact]		
    public void CheckIfRatingTerribleIsValid(){			
      var expectedResponseForValidRating = true;			
      var actualResponseForValidRating = 
      tipCalculator.CheckIfRatingIsValid("Terrible");			      
      Assert.Equal(expectedResponseForValidRating, 
      actualResponseForValidRating);		
    }	
  }
}
```

Nous voyons dans l'exemple ci-dessus que nous trichons à nouveau (nous avons codé en dur return false; dans notre méthode nouvellement créée). Quel est l'intérêt de tourner autour du pot et de simplement créer des squelettes et des échafaudages au lieu de retrousser nos manches et de faire du vrai codage ? Discutons de ce sujet important.

### Discussion sur notre première décision de conception

Nous illustrons ici comment faire du TDD étape par étape. Le côté amusant est que cette illustration étape par étape est en fait la manière exacte de faire du TDD : étape par étape. Il n'y a pas d'autre manière de faire du TDD qu'en le faisant étape par étape. Une étape à la fois.

En quoi cela est-il différent de toute autre manière de faire du développement logiciel ? Ne faisons-nous pas aussi tout étape par étape même lorsque nous ne suivons pas la méthodologie TDD ? Eh bien, pas vraiment. Laissez-moi expliquer :

Le TDD me donne l'impression de monter un cheval au galop. Nous nous déplaçons rapidement vers notre objectif, mais nous touchons fréquemment le sol (le cheval au galop touche le sol de temps en temps pour rebondir et courir vite). 

En comparaison, lorsque je fais du développement logiciel sans TDD, cela me donne l'impression de faire voler un cerf-volant. Je fais des mouvements rapides avec le cerf-volant, mais je ne touche jamais le sol, pas même une fois. Au moment où j'atterris le cerf-volant, l'endroit d'atterrissage peut ne pas être là où je voulais que le cerf-volant aille (il est très difficile de contrôler la direction d'un cerf-volant s'il vole dans un vent fort).

Avec le TDD, chaque fois que nous apportons une modification au code (à la fois le code de test et le code de l'application de livraison), nous exécutons les tests et touchons ainsi le sol. Nous galopons, mais en même temps, nous avons besoin de ce contact fréquent avec le sol. Nous devons voir si nous allons dans la bonne direction et aussi si nous avons cassé quelque chose pendant notre galop. Nos tests sont l'Oracle qui nous dit continuellement si tout fonctionne comme prévu ou si quelque chose a commencé à mal se comporter.

Apporter des modifications au code est une entreprise risquée. Le TDD fournit un bon harnais qui guide nos décisions de conception et garantit que nous ne gâchons pas quelque chose que nous avons déjà confirmé fonctionner selon nos attentes.

## Remplacer la valeur codée en dur par une logique de traitement réelle

Remplaçons maintenant la valeur codée en dur par un code réel en cours d'exécution. Nous apprenons d'abord à notre `Calculateur de Pourboire` qu'il existe une évaluation de service appelée « Terrible » et que le pourcentage de pourboire associé à cette évaluation est de 0 :

```c#
public bool CheckIfRatingIsValid(string rating) {	  
  ratingPercentages.Add("Terrible", 0);	
  return false;
}
```

Notre `Calculateur de Pourboire` sait maintenant qu'il existe une évaluation de service étiquetée « Terrible » et que le pourcentage de pourboire associé à un service terrible est de 0 %. Super, mais nous retournons toujours la valeur codée en dur `false`. Il est temps de la remplacer par un calcul réel :

```c#
public bool CheckIfRatingIsValid(string rating) {	
  ratingPercentages.Add("Terrible", 0);	
  return ratingPercentages.ContainsKey(rating);
}
```

Exécutez à nouveau le test :  


![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-22.png)

Super, mais le code semble toujours artificiel. Nous chargeons la valeur « Terrible » dans l'instance de `Hashtable ratingPercentages` puis vérifions immédiatement si cette valeur existe dans le `Hashtable`. Maintenant que nous sommes passés du test échoué (Rouge) au test réussi (Vert), il est temps d'effectuer la troisième étape de la boucle TDD – Refactoriser.

La refactorisation est essentiellement l'activité de modification de la structure du code sans affecter le comportement du code. Notre tâche ici est simple : extraire le code responsable du peuplement du `Hashtable ratingPercentages` dans un bloc de code séparé. 

L'endroit le plus naturel pour ce chargement est dans le bloc de code qui effectue l'initialisation du `Calculateur de Pourboire` – la méthode `constructeur`. Après la refactorisation, le code source de notre application de livraison ressemble à ceci :

```c#
using System.Collections;

namespace app {	
  public class TipCalculator {		
    private Hashtable ratingPercentages = new Hashtable();		
    public TipCalculator() {			
      ratingPercentages.Add("Terrible", 0);		
    }		
    
    public bool CheckIfRatingIsValid(string rating) {			
      return ratingPercentages.ContainsKey(rating);		
    }	
  }
}
```

Exécutez à nouveau le test, et il réussit (nous sommes au vert). Nous avons modifié la structure du code sans modifier son comportement ! Bon travail.

## Retourner la situation

Chaque fois que nous satisfaisons une attente positive, il est prudent de retourner les choses et de décrire l'attente négative. 

À ce stade, puisque nous avons satisfait qu'une valeur d'évaluation de service légitime est trouvée dans le `Calculateur de Pourboire`, nous voulons nous assurer que les valeurs non légitimes ne sont pas trouvées dans le `Calculateur de Pourboire`. 

Que voulons-nous dire par valeurs non légitimes ? Toute valeur autre que « Terrible », « Médiocre », « Bon », « Excellent » et « Exceptionnel ». Il est temps d'écrire la nouvelle attente (c'est-à-dire le test) :

```c#
[Fact]
public void CheckIfRatingWhateverIsValid() {	
  var expectedResponseForValidRating = true;	
  var actualResponseForValidRating = 			           
  tipCalculator.CheckIfRatingIsValid("Whatever");
  Assert.Equal(expectedResponseForValidRating, 
  actualResponseForValidRating);
}
```

Exécutez les tests :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-23.png)

Échec. Comme prévu. (Nous avons spécifié que notre attente lorsque nous fournissons l'évaluation de service comme « Whatever » devrait être `true`. En réalité, elle est `false`, car notre `Calculateur de Pourboire` ne contient pas la valeur « Whatever ».)

Corrigez le test (changez `expectedResponseForValidRating` de `true` à `false`) et exécutez-le à nouveau :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-24.png)

Un moment de réflexion : pourquoi avons-nous simulé la première exécution du test et l'avons fait échouer ? Parce que nous voulons toujours nous assurer d'observer notre nouveau test échouer. De cette manière, nous saurons qu'à l'avenir, tout passage réussi du test n'est pas simplement un faux positif.

## Éloge de l'état stable

L'ingénierie logicielle est un acte d'équilibre entre l'état stable et les périodes d'état instable. Que voulons-nous dire par état stable ? 

Si nous avons un système (une application en cours d'exécution) qui se comporte de la manière dont nous nous attendons à ce qu'il se comporte (c'est-à-dire qu'il produit des valeurs que nous avons spécifiées comme valeurs attendues), nous déclarons que le système est dans un état stable. Il fonctionne et fournit une certaine valeur. 

Cette livraison de valeur est encore partielle. Dans notre cas, la seule valeur pour les utilisateurs que ce `Calculateur de Pourboire` fournit est sa capacité à reconnaître l'évaluation de service « Terrible » comme une évaluation légitime. En outre, il est capable de nous informer que l'évaluation de service « Whatever » n'est pas une évaluation légitime.

Ce n'est pas grand-chose, mais c'est mieux que rien. Et bonne nouvelle – notre application en cours d'exécution est actuellement dans un état stable. Nous voulons maintenant voir comment ajouter un comportement plus précieux à notre `Calculateur de Pourboire`. Et la seule manière d'ajouter plus de valeur est d'effectuer certains changements.

Chaque fois que nous apportons un changement à notre application, nous perturbons son état stable. Cette perturbation est risquée. Cela peut signifier que nos changements pourraient casser quelque chose qui fonctionne déjà. En raison de cette préoccupation, nous nous efforçons de rendre la durée de cet état instable aussi courte que possible. 

Vous souvenez-vous de la comparaison du TDD à la montée d'un cheval au galop ? Lorsque le cheval est en vol (c'est-à-dire qu'il ne touche pas le sol), il avance vers notre objectif, mais il n'est pas dans un état stable. Ce n'est que lorsque le cheval touche le sol que son état se stabilise.

Le TDD encourage à apporter des changements mineurs (en vol) et à stabiliser immédiatement le système en vérifiant qu'il est de retour dans l'état stable. Nous valorisons l'état stable malgré le fait que nous embrassons volontiers les changements. Sans changements, nous ne serons pas en mesure de fournir de la valeur, mais nous devons le faire de manière très délibérée et prudente. 

Lorsque nous faisons du TDD, nous traitons les changements d'état stable comme si nous marchions sur des œufs. Peu importe à quel point nous pouvons être sûrs de savoir ce que nous faisons et comment nous faisons de l'ingénierie logicielle, il est prudent de laisser les tests échoués guider nos décisions.

## Vérifier si le bon pourcentage de pourboire est associé à l'évaluation du service

Introduisons maintenant un autre changement dans notre application – un test pour vérifier si le bon pourcentage de pourboire est associé à l'évaluation de service « Terrible ». Rappelez-vous que nous avons peuplé l'instance de `Hashtable ratingPercentages` avec les valeurs suivantes :

```c#
ratingPercentages.Add("Terrible", 0);
```

Nous avons écrit un test qui vérifie que notre `Hashtable ratingPercentages` contient bien l'évaluation de service légitime « Terrible ». Maintenant, nous avons besoin d'un test qui vérifie que l'évaluation de service « Terrible » signifie que le pourcentage de pourboire pour cette évaluation est de 0.

```c#
[Fact]
public void CheckIfRatingTerribleHasZeroPercentTip() {	
  var expectedZeroPercentForTerribleRating = 0;	
  var actualZeroPercentForTerribleRating = 10;	
  Assert.Equal(expectedZeroPercentForTerribleRating, 
  actualZeroPercentForTerribleRating);
}
```

Le nouveau test `CheckIfRatingTerribleHasZeroPercentTip` devrait échouer :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-25.png)

Encore une fois, nous codons en dur des valeurs réelles incorrectes juste pour pouvoir observer notre tout nouveau test échouer. Maintenant, nous devons remplacer la valeur codée en dur par l'appel réel à la méthode du `Calculateur de Pourboire` qui retourne le pourcentage de pourboire pour l'évaluation du service :

```c#
[Fact]
public void CheckIfRatingTerribleHasZeroPercentTip() {	
  var expectedZeroPercentForTerribleRating = 0;	
  var actualZeroPercentForTerribleRating = 			    
  tipCalculator.GetPercentageTipForRating("Terrible");
  Assert.Equal(expectedZeroPercentForTerribleRating, 
  actualZeroPercentForTerribleRating);
}
```

  
Comme dans le cas précédent, nous avons inventé une nouvelle API pour le `Calculateur de Pourboire`. Nous appelons cette nouvelle capacité `GetPercentageTipForRating("Terrible")`. Elle prend la valeur de l'évaluation du service et retourne le pourcentage de pourboire pour cette évaluation.

Passez à `app/TipCalculator.cs` et ajoutez le squelette codé en dur de la nouvelle méthode :

```c#
public int GetPercentageTipForRating(string rating) {	
  return 10;
}
```

L'exécution du test échoue à nouveau, car nous avons codé en dur la valeur de retour. Remplaçons-la par un traitement réel :

```c#
public int GetPercentageTipForRating(string rating) {	
  int tipPercentage = Int32.Parse(ratingPercentages[rating].ToString());
  return tipPercentage;
}
```

Exécutez à nouveau le test :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-26.png)

Les trois tests réussissent – nous sommes au vert, nous sommes de retour à l'état stable !

## Quel pourcentage de pourboire attendons-nous pour les évaluations de service non légitimes ?

De nombreuses années d'expérience dans le domaine m'ont appris à être un peu pessimiste. Maintenant que nous avons notre application de retour à l'état stable et qu'elle fournit de la valeur (répondant aux questions sur les évaluations de service légitimes et nous donnant également le bon pourcentage de pourboire pour l'évaluation « Terrible »), nous devons voir ce qui se passe lorsque nous exécutons notre application en lui donnant une valeur d'évaluation de service non légitime (par exemple, en lui donnant une évaluation de service « Whatever »).

Il est temps de quitter à nouveau l'état stable. Nous allons écrire un autre test :

```c#
[Fact]
public void CheckIfRatingWhateverHasNegativeOnePercentTip() {	
  var expectedZeroPercentForWhateverRating = -1;	
  var actualZeroPercentForWhateverRating = 	  
  tipCalculator.GetPercentageTipForRating("Whatever");
  Assert.Equal(expectedZeroPercentForWhateverRating, 
  actualZeroPercentForWhateverRating);
}
```

Nous décrivons notre attente lorsque le `Calculateur de Pourboire` est invité à retourner le pourcentage de pourboire pour l'évaluation de service « Whatever ». Parce que l'évaluation de service « Whatever » est une évaluation non légitime, nous attendons que le `Calculateur de Pourboire` retourne un pourcentage de pourboire de valeur -1.

Ce test précipite maintenant une amélioration de notre code de livraison. Nous devons ajouter une logique pour vérifier d'abord si l'évaluation de service fournie est légitime ou non. Ce n'est que si elle est légitime que nous demandons à `Hashtable ratingPercentages` de nous dire quelle est la valeur associée du pourcentage de pourboire. Si l'évaluation de service fournie est non légitime (par exemple, si elle est « Whatever »), nous contournons la communication avec `Hashtable ratingPercentages` et retournons simplement -1.

```c#
public int GetPercentageTipForRating(string rating) {	
  int tipPercentage = -1;	
  if(CheckIfRatingIsValid(rating)) {		
    tipPercentage = Int32.Parse(ratingPercentages[rating].ToString());	
  }	
  return tipPercentage;
}
```

Exécutez les tests, et les 4 tests réussissent :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-27.png)

Nous sommes de retour à l'état stable. Une autre courte excursion dans la zone volatile, et une autre victoire rapide et un retour sûr à l'état stable et imperturbable.

## Peupler les autres pourcentages de pourboire des évaluations de service

C'est maintenant le bon moment pour faire une pause et apporter des changements moins risqués, en suivant le modèle déjà établi. Quittez la sécurité de l'état stable et faites de courts voyages dans le territoire volatile en ajoutant un nouveau test pour vérifier si l'évaluation de service « Médiocre » est une évaluation valide et légitime :

```c#
[Fact]
public void CheckIfRatingPoorIsValid() {	
  var expectedResponseForValidRating = true;	
  var actualResponseForValidRating = 	  
  tipCalculator.CheckIfRatingIsValid("Poor");
  Assert.Equal(expectedResponseForValidRating, 
  actualResponseForValidRating);
}
```

L'exécution de ce test échouera :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-28.png)

L'évaluation de service « Médiocre » n'a pas encore été implémentée. Pour faire passer le test, implémentez l'évaluation de service « Médiocre » en ajoutant cette ligne au constructeur `TipCalculator` :

```c#
ratingPercentages.Add("Poor", 5);
```

Exécutez les tests, et nous sommes de retour en sécurité :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-29.png)

Nous profitons de l'état stable avec 6 tests réussissant avec succès.

Maintenant que nous avons ajouté l'évaluation de service « Médiocre » associée à un pourboire de 5 %, écrivons un test qui décrira cette attente :

```c#
[Fact]
public void CheckIfRatingPoorHasFivePercentTip() {	
  var expectedZeroPercentForPoorRating = 5;	
  var actualZeroPercentForPoorRating = 	  
  tipCalculator.GetPercentageTipForRating("Poor");
  Assert.Equal(expectedZeroPercentForPoorRating, 
  actualZeroPercentForPoorRating);
}
```

Les tests s'exécutent avec succès, et nous sommes de retour en sécurité dans l'état stable.  
Je laisse au lecteur le soin d'apporter les modifications qui conduiront à l'implémentation des évaluations de service « Bon », « Excellent » et « Exceptionnel ». À la fin de l'exercice, vous devriez avoir votre système de retour à l'état stable avec 12 tests réussissant avec succès :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-35.png)

## Calculer le total général étant donné le total et l'évaluation du service

Nous sommes maintenant prêts pour l'étape finale – étant donné le total de la facture et l'évaluation du service, nous attendons du `Calculateur de Pourboire` qu'il calcule le pourcentage de pourboire et l'ajoute au total, produisant le total général à payer au restaurant.

Comme nous le faisons toujours, nous décrivons d'abord l'attente :

```c#
[Fact]
public void CalculateTotalWithTip() {	
  var expectedTotalWithTip = 135.7;	
  var actualTotalWithTip = 200.0;	
  Assert.Equal(expectedTotalWithTip, actualTotalWithTip);
}
```

Comme d'habitude, nous codons d'abord en dur certaines attentes que nous savons être vouées à l'échec. C'est pour que nous observions notre nouveau test échouer :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-36.png)

Il est temps d'implémenter la logique de traitement qui calculera le total correct avec le pourboire. Étant donné le total de 118,0 $ et l'évaluation de service « Excellent » (15 % de pourboire), nous attendons que le total soit de 135,7 $ :

```c#
[Fact]
public void CalculateTotalWithTip() {	
  var rating = "Great";	
  var total = 118;	
  var expectedTotalWithTip = 135.7;	
  var actualTotalWithTip = tipCalculator.CalculateTotalWithTip(total, 
  rating);	
  Assert.Equal(expectedTotalWithTip, actualTotalWithTip);
}
```

Nous avons conçu une nouvelle API pour le `Calculateur de Pourboire` – une méthode appelée `CalculateTotalWithTip(total, rating)`. Elle prend la valeur totale et l'évaluation du service et retourne le total avec le pourboire. L'implémentation de la méthode ressemble à ceci :

```c#
public double CalculateTotalWithTip(double total, string rating) {	
  double totalWithTip = -1;	
  if(CheckIfRatingIsValid(rating)) {		
    int percentage = GetPercentageTipForRating(rating);		
    totalWithTip = total + ((total/100) * percentage);	
  }	
  return totalWithTip;
}
```

Exécutez les tests, et nous sommes de retour à l'état stable :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-37.png)

## Avons-nous terminé ici ?

Non, pas encore. Même lorsque tous les tests sont au vert et que nous sommes de retour à l'état stable, il reste encore quelques choses à faire. 

Pour commencer, nous devons ajouter une attente pessimiste pour notre calcul du `Calculateur de Pourboire` du total avec le pourboire basé sur l'évaluation du service :

```c#
[Fact]
public void CalculateTotalWithTipForNonlegitimateRating() {	
  var rating = "Meh";	
  var total = 118;	
  var expectedTotalWithTip = 135.7;	
  var actualTotalWithTip = tipCalculator.CalculateTotalWithTip(total, 
  rating);	
  Assert.Equal(expectedTotalWithTip, actualTotalWithTip);
}
```

L'exécution des tests produit un test échoué :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-38.png)

Notre attente pour une évaluation de service non légitime (« Meh ») était incorrecte. Le total réel est -1, nous devons donc ajuster notre attente en remplaçant 135.7 par -1. Exécutez à nouveau les tests, et nous sommes de retour à l'état stable !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-39.png)

Nous avons maintenant 14 tests, ils réussissent tous, et notre _Calculateur de Pourboire_ fonctionne selon nos attentes et satisfait les critères d'acceptation.

Nous avons presque terminé. Une dernière vérification de bon sens avant de pouvoir livrer en toute confiance notre tout nouveau `Calculateur de Pourboire` – nous devons exécuter le _[test de mutation](https://opensource.com/article/19/9/mutation-testing-example-definition)_. 

Notre framework de test de mutation va muter le code de livraison, une ligne à la fois, et exécutera tous les tests pour chaque mutation individuelle. 

Si les tests se plaignent du code muté, tout va bien, nous avons tué le mutant. Si les tests ne se plaignent pas, nous sommes dans l'embarras. Nous avons un mutant survivant dans notre base de code, ce qui signifie qu'il y a des lignes de code dans notre dépôt qui font quelque chose pour lequel nous n'avons fourni aucune attente.

Exécutons le test de mutation pour voir à quel point notre solution est solide. Bonne nouvelle – notre solution a tué 100 % des mutants !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-40.png)

Le test de mutation a donné à notre application de livraison un bon état de santé. Notre `Calculateur de Pourboire` semble être en bonne forme.

## Rouge-Vert-Refactoriser-Réfléchir

Revue de notre exercice de construction du `Calculateur de Pourboire`. Nous avons commencé le processus en décrivant nos attentes en utilisant le format classique de l'histoire utilisateur. L'histoire utilisateur (comme son nom l'indique) est axée sur la description de scénarios qui remplissent les objectifs de l'utilisateur final. 

Dans ce cas, l'objectif simple est de calculer le montant du pourboire à partir de l'évaluation du service fournie et du total de la facture du restaurant. Le montant du pourboire calculé est ensuite automatiquement ajouté au total.

De là, nous avons procédé à la construction de notre application de livraison en suivant la méthodologie TDD. Comme nous l'avons démontré, la méthodologie consiste à écrire un test échoué, à observer son échec (la phase Rouge du TDD), puis à apporter immédiatement des modifications au code qui garantissent que le test passe (la phase Verte du TDD). Une fois que le test passe, nous passons à la phase de Refactorisation (nous restructurons le code sans affecter son comportement). De cette manière, nous nous assurons que notre code n'est pas coûteux à changer.

Une bonne pratique du TDD exige également des rétrospectives fréquentes – nous l'appelons réflexion. Nous nous arrêtons et réfléchissons aux choses que nous avons accomplies jusqu'à présent, pour voir si nous pouvons apprendre de nos expériences récentes. Cette réflexion renforce le processus, car elle repose sur des retours fréquents et serrés fournis par les tests qui échouent, puis réussissent.

J'ai déjà comparé le développement piloté par les tests à l'expérience de monter un cheval au galop. En montant un cheval, nous alternons entre le vol dans les airs (c'est-à-dire la vitesse atteinte lorsque le cheval saute du sol) et le guidage du cheval. Il est impossible de diriger le cheval lorsque nous sommes hors du sol, en l'air. À ce moment-là, nous gagnons de la vitesse, mais nous ne pouvons apporter aucun changement de direction. Ce n'est que lorsque le cheval touche le sol que nous pouvons apporter un changement de direction.

En TDD, nous nous efforçons de toucher le sol aussi fréquemment que possible. Plus les sauts que nous faisons sans toucher le sol sont longs, moins nous avons de chances de corriger le cap.

J'ai également comparé les pratiques de développement logiciel qui ne suivent pas les principes du TDD à l'expérience de faire voler un cerf-volant. Lorsque nous faisons voler un cerf-volant, nous ne touchons jamais le sol. C'est une sensation exaltante de laisser le vent soulever le cerf-volant et le faire rebondir dans les airs. Nous pouvons atteindre une vitesse considérable de cette manière. Mais nous luttons dans de telles situations pour maintenir le cap souhaité. Et après avoir finalement atterri le cerf-volant, il n'atterrit généralement pas à l'endroit où nous voulions initialement qu'il atterrisse.

Pourquoi l'accent de cet article est-il mis sur « ne pas écrire les tests en premier » ? De nombreux ingénieurs logiciels qui ne sont pas familiers avec les pratiques agiles telles qu'implémentées dans le TDD affirment généralement soit que l'écriture de tests automatisés n'est pas nécessaire, soit que les tests automatisés doivent être écrits après que le code est complet. 

Une fois qu'ils commencent à apprendre l'agile et le TDD, ils peuvent reconsidérer leurs pratiques et décider que l'écriture de tests avant l'écriture du code d'implémentation peut avoir plus de sens. Cependant, en raison de la mentalité en cascade ancrée, certains de ces ingénieurs commettent l'erreur d'écrire tous les tests en premier, puis passent à l'écriture du code.

Cette approche est complètement erronée. Elle est équivalente à l'approche traditionnelle en cascade où nous passons par le processus de développement en respectant des phases verrouillées. 

Tout d'abord, nous écrivons les exigences (dans ce cas, les exigences seraient des attentes écrites sous forme de tests automatisés). Ce n'est que lorsque toutes les exigences (c'est-à-dire les tests automatisés) ont été écrites, signées et gelées, que nous passons à la phase verrouillée suivante – écrire le code pour l'application de livraison.

Le TDD est l'exact opposé de l'approche « écrire les tests en premier ». En TDD, nous écrivons toujours un seul test. Ce test décrit un comportement souhaité. Le comportement souhaité n'existe pas encore (c'est pourquoi il est souhaité), et le test échoue. 

Nous passons ensuite immédiatement à l'apport de modifications au code dans le but de créer le comportement souhaité. Une fois le comportement souhaité créé, il est validé par le test, et si les attentes du test sont satisfaites, nous passons à la refactorisation du code (pour satisfaire les exigences non fonctionnelles, telles que le coût de changement).

Nous pratiquons une discipline rigoureuse pour ne jamais succomber à la tentation d'écrire plus d'un test à la fois. De cette manière, nous nous assurons de toucher le sol aussi fréquemment que possible. 

Nous préférons rester « en vol » pendant la période la plus courte possible. Nous sommes « en vol » pendant cette période où le comportement souhaité décrit dans le test ne s'est pas encore matérialisé. Plus le comportement attendu et souhaité est petit, plus notre trajectoire « en vol » sera courte. De cette manière, nous touchons souvent le sol, ce qui nous donne une chance d'ajuster la direction.

## Conclusion

Construire un simple `Calculateur de Pourboire` est un problème de taille jouet, et utiliser cet exercice pour illustrer la méthodologie TDD ne fournit pas nécessairement un argument convaincant en faveur du TDD. Cependant, dans le cadre des contraintes d'un article technique, cet exercice pratique peut fournir des informations précieuses sur les avantages de l'adoption du TDD.

Nous soutiendrions toujours que les véritables avantages du TDD ne deviennent apparents que lorsque l'on traite de projets logiciels beaucoup plus grands et plus complexes. La capacité de rester ancré tout en apportant des changements potentiellement risqués à un système complexe et volumineux est souvent un sauveur de vie. 

En plus de cela, la construction de logiciels en utilisant la méthodologie TDD entraîne beaucoup moins de retravail. Le TDD favorise un haut degré de modularisation, ce qui entraîne une forte cohésion des modules et un faible couplage entre les modules. 

Toutes ces caractéristiques produisent une application de livraison dont la base de code est facile et peu coûteuse à modifier. Et la réduction du coût de changement s'est avérée être la meilleure façon sur le chemin de l'adoption des changements et de l'abandon du concept connu sous le nom de « dérive des objectifs ». 

En résumé, le TDD permet aux équipes d'ingénierie logicielle de fournir un haut degré de flexibilité à l'entreprise.