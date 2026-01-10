---
title: Principe Ouvert-Fermé – Le Concept de Développement Logiciel Expliqué en Anglais
  Simple
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2021-09-27T19:43:06.000Z'
originalURL: https://freecodecamp.org/news/open-closed-principle
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/IMG_8905.JPG
tags:
- name: software design
  slug: software-design
- name: software design patterns
  slug: software-design-patterns
- name: software development
  slug: software-development
seo_title: Principe Ouvert-Fermé – Le Concept de Développement Logiciel Expliqué en
  Anglais Simple
seo_desc: "There are many articles about the Open-Closed Principle, but I can never\
  \ find one that explains it in a way that really works for me. \nSo here, hopefully,\
  \ is a good one – with a non trivial and real life example, what changes to support,\
  \ and a descri..."
---

Il existe de nombreux articles sur le Principe Ouvert-Fermé, mais je n'ai jamais trouvé celui qui l'explique d'une manière qui me convient vraiment. 

Alors voici, espérons-le, un bon article  avec un exemple non trivial et réel, les changements à supporter, et une description des compromis.

Le Principe Ouvert-Fermé stipule que le code doit être "Ouvert pour l'extension" et "Fermé pour la modification". 

Il y a [beaucoup de confusion autour de ce terme](https://codeblog.jonskeet.uk/2013/03/15/the-open-closed-principle-in-review/), mais essentiellement cela signifie que si vous souhaitez implémenter un changement _supporté_, vous devriez pouvoir le faire sans modifier le code à de nombreux endroits. Idéalement, vous pouvez implémenter la nouvelle fonctionnalité simplement en ajoutant du nouveau code, et en modifiant peu ou pas de vieux code, ce qui rend le code plus facile à développer et à maintenir. 

Ouvert est le 'O' dans les [principes de conception SOLID](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/), qui sont probablement les guides les plus célèbres pour écrire du code de haute qualité.

Aucun code utile ne peut jamais être complètement ouvert à tous les changements possibles, nous devons donc décider quels changements nous allons _supporter_. Lors de l'écriture de notre code, nous pouvons réfléchir aux changements potentiels, décider lesquels _supporter_, et ensuite rendre le code 'ouvert' à ceux-ci. 

Nous pouvons créer une liste de ces changements potentiels en :

* Analysant le code
* Examinant les changements précédents apportés au code
* Utilisant notre expérience des changements couramment demandés
* Utilisant toute connaissance des demandes de fonctionnalités à venir

Prenez un moment pour examiner le code ci-dessous ([et sur GitHub](https://github.com/ceddlyburge/open-closed-principle/blob/master/OpenClosedPrinciple/Original/GrossToNetCalculator.cs)) et réfléchissez aux changements que nous pourrions attendre. Vous n'avez pas accès à l'historique des commits, ni à aucune connaissance des demandes de fonctionnalités à venir, mais vous pouvez probablement imaginer quelques candidats.

```csharp=
public class GrossToNetCalculator
{
    public GrossToNetCalculator(
        IGrossEnergyYield grossYield,
        double grossEnergy,
        double hysteresisLoss,
        double curtailmentLossGrid,
        double turbineLossTurbulence,
        double electricalLoss,
        double turbineLossShear,
        double turbinePerformanceExperience,
        double operationalExperienceLoss)
    {
        double dependentLoss = 
            CombinePercentages(
                grossYield.TurbineAvailability,
                grossYield.BalanceAvailability,
                grossYield.AccessibilityAvailability,
                hysteresisLoss,
                electricalLoss,
                grossYield.EnvironmentalShutdownWeather,
                grossYield.EnvironmentalSiteAccess,
                grossYield.EnvironmentTreeGrowth);

        double independentLoss = 
            CombinePercentages(
                grossYield.GridAvailability,
                turbinePerformanceExperience,
                turbineLossTurbulence,
                grossYield.EnvironmentalPerformanceDegradationIcing,
                grossYield.CurtailmentPowerPurchase,
                grossYield.SubOptimalPerformance,
                turbineLossShear,
                operationalExperienceLoss);

        GrossToNet = 
        	1 - 
            (1 - (dependentLoss + curtailmentLossGrid))
            * (1 - independentLoss);
    }

    double CombinePercentages(params double[] percentages)
    {
        double combination = 1;
        foreach (var percentage in percentages)
            combination *= 1 - percentage;
        return 1 - combination;
    }

    public double GrossToNet { get; private set; }
}
```

Ce code est relativement simple, et lorsque je le regarde, voici les changements potentiels que je vois :

* Des éléments pourraient être ajoutés ou supprimés des calculs `dependentLoss` et `independentLoss`. Les éléments pourraient également être déplacés entre `dependentLoss` et `independentLoss`, mais cela revient essentiellement au même
* Le calcul de `GrossToNet` pourrait changer
* Le calcul de `CombinePercentages` pourrait changer

Comme pour la plupart des choses en programmation informatique, il y a une tension lors de l'application du Principe Ouvert-Fermé. 

D'une part, rendre le code plus facilement extensible est une bonne chose. D'autre part, cela brise souvent l'encapsulation, ajoute de la complication et des niveaux d'abstraction inutiles. 

Nous devons donc à nouveau prendre une décision sur les changements que nous voulons supporter et rendre le code 'ouvert à' ceux-ci. Nous pouvons ainsi éviter d'ajouter des complications inutiles au code pour des changements non adaptés. 

Il est utile de se rappeler que le travail peut toujours être fait plus tard, lorsque ce sera plus facile, car nous saurons exactement ce qui est requis.

Pour prendre une décision sur les changements que nous devrions supporter et rendre le code 'ouvert à', nous devons estimer la probabilité que le changement se produise, réfléchir à des solutions de conception, puis réfléchir aux compromis.

## Nous Pourrions Ajouter ou Supprimer des Éléments des Calculs dependentLoss et independentLoss

###   
Très susceptible de changer

Le calcul de `dependentLoss` et `independentLoss` (par exemple `double dependentLoss = CombinePercentages(...)`) utilise chacun 8 paramètres (`electricalLoss`, `TurbineAvailability` et ainsi de suite).

Ces 16 paramètres constituent la majorité des 17 entrées totales du calcul entier. Donc, d'un point de vue purement statistique, un changement de l'un de ceux-ci a une probabilité de 16/17 (94%) d'affecter ces calculs.

Il est également facile d'imaginer que nous pourrions vouloir ajouter une autre "Perte" ou "Disponibilité" ou similaire à l'avenir, ou qu'une perte actuelle n'est plus pertinente, ou que différentes combinaisons seront requises dans différentes circonstances.

### Solution possible

Prenez une liste de pertes dépendantes et indépendantes dans le constructeur, au lieu de prendre chaque perte individuellement. Donc le constructeur existant :

```csharp=
public GrossToNetCalculator(
	...
    double hysteresisLoss,
    double curtailmentLossGrid,
    ...)
```

est remplacé par ceci :

```csharp=
public GrossToNetCalculator(
    IReadOnlyList<double> dependentLosses
    IReadOnlyList<double> independentLosses)
```

Cela signifie que si le changement est demandé, nous pouvons l'implémenter sans changer la classe (et simplement changer les paramètres que nous passons au constructeur). 

Par exemple, si une autre 'dependentLoss' est demandée, nous pouvons simplement l'ajouter à la liste `dependentLosses`.

(Vous pouvez voir le [code sur GitHub ici](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/ListParameters))

### Compromis

Une petite quantité d'encapsulation est perdue, et le code appelant serait maintenant responsable de décider quelles pertes passer.

Le code adhère beaucoup mieux au Principe Ouvert-Fermé et devient beaucoup plus facilement extensible et réutilisable. Si vous devez apporter une modification, vous n'aurez pas besoin de modifier les tests, ce qui est utile car ils sont compliqués. 

Les tests pour le code appelant devraient être modifiés, mais seulement pour vérifier qu'ils passent les paramètres corrects, ce qui est beaucoup plus simple. 

Il est possible que les paramètres du constructeur soient passés dans la base de code, et maintenant il n'y a que deux paramètres, au lieu des neuf précédents.

### Décision

Nous devrions implémenter cette solution pour supporter ce changement et rendre le code 'ouvert' à celui-ci. 

## Le Calcul GrossToNet Pourrait Changer

###   
Peu susceptible de changer

Le calcul GrossToNet est `GrossToNet = 1 - (1 - (dependentLoss + curtailmentLossGrid)) * (1 - independentLoss);`

Seul le paramètre `curtailmentLossGrid` est utilisé, en dehors de `dependentLoss` et `independentLoss` qui sont couverts précédemment.

Ce paramètre est une petite minorité des 17 entrées totales du calcul entier. Donc, d'un point de vue purement statistique, un changement de l'un de ceux-ci a une probabilité de 1/17 (6%) d'affecter ce calcul.

### Solutions possibles

1. Prenez un paramètre lambda dans le constructeur pour calculer `GrossToNet` et passez-lui `dependentLoss` et `independentLoss`, de sorte que le calcul devienne `GrossToNet = grossToNetCalculatorLambda(dependentLoss, independentLoss)`([code sur GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/GrossToNetLambda))
2. Supprimez `curtailmentLossGrid` du calcul, qui devient alors complètement générique et peut être renommé en `PercentageCombiner`. Exigez que le code appelant applique cet ajustement (cet ajustement est trop compliqué pour un exemple de code utile)
3. Supprimez `curtailmentLossGrid` du calcul comme ci-dessus, puis recréez le `GrossToNetCalculator` original, en utilisant le `PercentageCombiner` et en ajoutant `curtailmentLossGrid` au calcul   
([code sur GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/PercentageCombiner))

### Compromis

Une grande quantité d'encapsulation est perdue pour les options 1 et 2. L'option 3 est une quantité raisonnable de travail, et ajoute une couche d'abstraction.

### Décision

Ce changement n'est pas susceptible de se produire, il n'est donc probablement pas utile de faire l'effort nécessaire pour le supporter et rendre le code 'ouvert' à celui-ci. Mais si nous avions une autre utilisation pour le nouveau `PercentageCombiner`, cela vaudrait définitivement la peine.

## Le Calcul CombinePercentages Pourrait Changer

###   
Très peu susceptible de changer

```csharp=
CombinePercentages(params double[] percentages)
{
    double combination = 1;
    foreach (var percentage in percentages)
    combination *= 1 - percentage;
    return 1 - combination;
}
```

Le calcul CombinePercentages implémente certaines lois standard des mathématiques/statistiques, qui ne changent pas.

### Solutions possibles

1. Prenez un paramètre lambda dans le constructeur pour combiner les pourcentages, et utilisez-le au lieu de la fonction CombinePercentages. Au lieu d'avoir `double dependentLoss = CombinePercentages(...)`, vous auriez `double dependentLoss = combinePercentagesLambda(...)`.   
([code sur GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/CombinePercentagesLambda))
2. Créez une abstraction `PercentageCombiner`, prenez-la dans le constructeur pour combiner les pourcentages, et utilisez-la au lieu de la fonction CombinePercentages. Au lieu d'avoir `double dependentLoss = CombinePercentages(...)`, vous auriez `double dependentLoss = percentageCombiner.CombinePercentages(...)`.  
([code sur GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/PercentageCombinerAbstraction))

### Compromis

Combiner les pourcentages est au cœur de ce que fait ce code, donc supprimer cette logique rend le code principalement inutile. 

L'option 1 passe toute la responsabilité de cela à l'appelant, tandis que l'option 2 permet au moins des implémentations prédéfinies de l'abstraction.

### Décision

Ce changement est très peu probable, et la seule solution raisonnable (option 2) nécessite beaucoup de travail et ajoute de la complexité et de l'abstraction. 

Cela signifie qu'il ne serait judicieux de le faire que lorsque le changement est réellement requis, et même alors seulement si plusieurs algorithmes sont nécessaires. Notez que si un changement est requis pour l'algorithme, il sera plus judicieux de simplement changer l'implémentation de la fonction CombinePercentages.

## Conclusion

Décider si le code adhère au Principe Ouvert-Fermé est presque toujours une question de jugement, et il y a généralement des compromis impliqués avec l'encapsulation, la complexité et l'abstraction. 

Il est utile de réfléchir aux changements et extensions probables, et d'utiliser ceux-ci pour guider vos décisions.