---
title: Apprenez la réflexion en Go et les conceptions génériques avec un exemple pratique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T19:13:41.000Z'
originalURL: https://freecodecamp.org/news/a-practical-example-go-reflections-and-generic-designs-4868b6cdb2dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nY3XI__S6O5PXrjdLIsJyQ.png
tags:
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Apprenez la réflexion en Go et les conceptions génériques avec un exemple
  pratique
seo_desc: 'By David Rieger

  Reflections allow us to inspect and modify a program’s structure at its own runtime.
  In this article we will be looking at some parts of the go reflect package API and
  applying them to a real-world use case by building a generic appli...'
---

Par David Rieger

La réflexion nous permet d'inspecter et de modifier la structure d'un programme pendant son propre temps d'exécution. Dans cet article, nous allons examiner certaines parties de l'API du paquet `reflect` de Go et les appliquer à un cas d'utilisation réel en construisant un _mécanisme de configuration d'application générique_.

### Ce que nous avons et ce que nous voulons

Nous avons implémenté une **application d'analyse de données en Go qui récupère des données d'une base de données d'inventaire d'une librairie, les traite et les transforme en modèles statistiques lisibles par l'homme** qui reflètent l'état de notre inventaire.

La sortie pourrait être, par exemple, une liste de livres publiés par un certain auteur, ou un graphique à barres illustrant le nombre de livres dans notre inventaire par décennie de publication.

**Ce que nous voulons, c'est un moyen de configurer ce que l'application génère à partir des données brutes de manière abstraite.** Il peut y avoir des centaines d'algorithmes qui traitent tous les données brutes de différentes manières et produisent des sorties différentes, mais toutes les sorties ne nous sont pas utiles à chaque exécution de l'application. Nous voulons pouvoir configurer notre application pour qu'elle réponde à nos besoins, puis la laisser faire ce qu'elle doit faire afin de nous fournir ce que nous attendons d'elle.

Nous voulons également pouvoir laisser le processus analytique **s'exécuter — avec une configuration fixe — de manière autonome et périodique sur un planificateur de tâches** (par exemple Jenkins, Rundeck ou cron) et nous rapporter les résultats qui nous intéressent, sans avoir à interagir avec lui avant chaque exécution.

Enfin, nous voulons que l'application soit **facilement extensible** afin de pouvoir ajouter de nouveaux algorithmes avec le moins d'effort possible et sans casser les flux de travail existants.

**Nos exigences fondamentales concernant l'architecture sont donc, en résumé :**

* Une configuration persistante et abstraite
* Une interface via laquelle les utilisateurs humains ainsi que d'autres logiciels (le planificateur de tâches) peuvent exécuter l'application
* Une extensibilité intuitive

#### Approche 1 : Le complaisant

La manière la plus simple d'implémenter cela est de charger d'abord les données brutes dans notre programme, d'appeler chaque algorithme analytique que nous voulons exécuter depuis la fonction principale (`main`) de l'application, et enfin de tout regrouper dans un joli rapport.

![Image](https://cdn-media-1.freecodecamp.org/images/o6Z4F4-B9Y6OK3Zms-PlTzyq7HfwcOXsgO-H)
_Application autonome. Le client et la logique métier font partie du même logiciel._

```go
package main

func main() {
    rawData := Parse("books_db.flatfile")
    
// Exécuter les algorithmes de notre choix sur les données
    bpDChart := amountOfBooksPerDecade(rawData)
    bpAList := booksPerAuthor(rawData)
    
createReport(bpDChart, bpAList)
}
```

En termes d'extensibilité intuitive, c'est probablement ce qu'il y a de mieux (intuitif n'implique pas forcément bon). Chaque fois que nous voulons ajouter un nouvel algorithme analytique, nous l'implémentons simplement et l'appelons dans la fonction `main` si nous voulons l'exécuter.

Cependant, il y a un inconvénient évident : nous devons toucher au code de base de l'application et la recompiler non seulement chaque fois que nous étendons la logique métier, mais aussi chaque fois que nous voulons changer ce qui est généré (c'est-à-dire chaque fois que nous voulons la reconfigurer).

Cette approche ne fournit aucune interface permettant à l'utilisateur de configurer l'application. Elle **ne répond pas non plus vraiment à notre exigence de définir de manière abstraite ce que fait l'application**. Le développeur du logiciel est pratiquement le seul à pouvoir configurer son comportement.

Bien sûr, nous pourrions ajouter un fichier de configuration. Cela nous permettrait de sélectionner les algorithmes à exécuter et ceux à omettre sans avoir à toucher ou recompiler le code de l'application. Cependant, cela nécessitera une certaine logique qui fait correspondre les entrées du fichier de configuration aux fonctions (potentiellement des centaines) de mon application.

Cette logique devra être ajustée chaque fois que j'étends l'application avec un nouvel algorithme analytique. Finalement, nous finirons probablement par avoir un tas d'instructions `if` exécutant ou omettant des algorithmes en fonction de la présence ou de l'absence de chaînes de caractères dans le fichier de configuration. Nous y reviendrons plus tard.

#### Approche 2 : L'approche orientée client

La manière la plus courante et peut-être la plus propre serait de fournir une belle interface — une API publiée — au-dessus du logiciel d'analyse, et un client séparé qui communique avec cette API. Le client peut alors décider de la sortie qui l'intéresse et appeler les points de terminaison d'API appropriés avec les paramètres correspondants. Du côté du serveur — notre logiciel d'analyse original — nous exécutons simplement les algorithmes pertinents sur les données brutes, produisons un rapport et le renvoyons au client.

![Image](https://cdn-media-1.freecodecamp.org/images/t4G9m0DUCL8cWZg9GE4y0vnbABPhqE5kZiCO)
_Une architecture propre avec un client communiquant avec une API publiée au-dessus de la logique métier. Souvent une excellente approche, mais elle n'est pas gratuite._

C'est probablement l'architecture la plus propre, mais il y a des cas où ce n'est tout simplement pas l'idéal.

En regardant les exigences ci-dessus et l'approche précédente, la création d'un client séparé ne fait que déplacer le problème initial d'un endroit à un autre. Supposons que je veuille exécuter l'application d'analyse périodiquement avec une certaine configuration (c'est-à-dire avec une certaine définition de la sortie qui m'intéresse) et sans avoir à interagir avec l'application ou son client à chaque exécution. J'aurai besoin d'une sorte de configuration persistante qui correspond aux fonctions de mon application. Que je fasse cela directement sur le backend ou du côté client ne m'importe pas vraiment.

De plus, l'interface supplémentaire et le client introduisent beaucoup d'inertie en termes d'extensibilité. Chaque fois que nous ajoutons un nouvel algorithme analytique qui produit un type de modèle statistique différent, nous devons adapter l'interface du service ainsi que le client qui communique avec cette interface. Selon l'identité du client, cela peut valoir l'effort, mais dans notre cas, cela pourrait n'être qu'une surcharge injustifiable.

Si mon client était un utilisateur humain qui veut appuyer sur quelques boutons pour recevoir certains résultats à certains moments, alors oui, avoir une API propre exposant mon logiciel d'analyse est indispensable. Mais dans ce cas, où le client est un planificateur de tâches que nous ne touchons que de temps en temps, autre chose pourrait être plus approprié.

#### Approche 3 : Le générique

Afin de répondre à nos exigences, nous devons faire deux choses : fournir une conception qui ne nous oblige pas à maintenir des couches d'application séparées (telles qu'une interface isolée et un client) lors de l'extension de la logique métier, tout en permettant au client de définir le comportement sans avoir à toucher au code source de l'application.

La première approche complétée par un fichier de configuration fournirait une telle conception. Écrire un fichier de configuration simple, l'analyser, puis trouver les algorithmes appropriés à exécuter est assez évident. Cependant, cela ne gère pas très bien l'extensibilité.

Étendre la logique métier en ajoutant de nouveaux algorithmes analytiques nous obligera également à faire correspondre les paramètres du fichier de configuration aux nouveaux algorithmes. Il sera nécessaire d'adapter le lecteur de configuration afin de prendre en charge la nouvelle fonctionnalité. Nous avons donc toujours cette couche supplémentaire qui rend notre logiciel plus difficile à étendre.

Il serait formidable de pouvoir faire correspondre les paramètres du fichier de configuration aux fonctions de notre logique métier sans avoir à implémenter explicitement une correspondance un à un (config vers code) pour chacun de nos (potentiellement des centaines d') algorithmes analytiques. C'est ici que la réflexion entre en scène.

![Image](https://cdn-media-1.freecodecamp.org/images/ACm908OU9Ky1E-IVL5Rb6SI6KdqCHMcscwMI)
_Dessin de Gopher par Renee French (reneefrench.blogspot.com)_

Heureusement, chacun de nos algorithmes analytiques possède un nom unique, et nous pouvons identifier celui que nous voulons exécuter en spécifiant son nom dans la configuration. Nous indiquons au programme quelles statistiques nous aimerions voir dans le rapport final en tapant les noms des algorithmes associés dans le fichier de configuration. Maintenant, nous avons seulement besoin de quelque chose qui récupère ces noms dans le fichier de configuration, trouve les fonctions portant les mêmes noms dans la logique métier et les exécute (plus un peu de code pour regrouper tous les résultats dans un rapport).

![Image](https://cdn-media-1.freecodecamp.org/images/kzepd971RqgErd7A1EV7Z6SDienQKSpteY7I)
_La réflexion fait correspondre les paramètres d'un fichier de configuration accompagnant l'application aux fonctions de la logique métier. Cela permet une extension avec peu d'effort._

La partie qui trouve les fonctions (étant donné leurs noms) est réalisée par la réflexion. La réflexion nous permet d'examiner la structure du code de la logique métier et de récupérer le type de fonction réel à partir du nom de la fonction.

Cette architecture nous permet d'étendre facilement notre logique métier sans avoir à maintenir une autre couche de notre application ou à toucher au code existant. La correspondance des paramètres de configuration avec les algorithmes d'analyse se fait de manière générique.

Elle nous permet également de reconfigurer le comportement de l'application via une interface abstraite.

Notez que nous devons toujours recompiler l'ensemble de l'application chaque fois que nous l'étendons avec un nouvel algorithme analytique. Des frameworks de plugins pourraient nous aider à éviter cela, mais cela dépasse le cadre de cet article.

Bien sûr, cette architecture n'est pas sans inconvénients. Notre couche de réflexion récupérera aveuglément des fonctions et les appellera sans savoir ce que ces fonctions requièrent ou renvoient. Nous devrons donc implémenter tous nos algorithmes analytiques de manière à ce qu'ils puissent accepter un type d'entrée générique et renvoyer un type de sortie générique.

Chaque algorithme renverra un modèle statistique différent, mais nous devons renvoyer ces modèles enveloppés dans quelque chose que l'appelant (c'est-à-dire la couche de réflexion) peut manipuler. Il peut ensuite envoyer le modèle enveloppé à la couche qui produit le rapport qui, bien sûr, doit pouvoir accéder au modèle statistique réel.

La manière dont cela est réalisé varie d'un langage à l'autre. Nous allons examiner (une façon de) résoudre ce problème en Go.

### Trouver des fonctions par leurs noms

La première étape pour passer d'un fichier de configuration YAML, JSON ou XML brut à un algorithme appelable (après avoir chargé le fichier dans l'application, bien sûr) consiste à trouver une fonction dans le logiciel qui correspond au nom de fonction donné dans le fichier de configuration.

Malheureusement, il n'existe pas vraiment de moyen intuitif de récupérer une fonction résidant dans un paquet par son nom en Go. Nous ne pouvons pas simplement fournir un nom de fonction d'un côté et récupérer quelque chose d'appelable de l'autre.

Cependant, il est possible de trouver une _méthode d'un type_ par son nom.

Une méthode en Go est une fonction qui possède un receveur, alors qu'un receveur peut être n'importe quel type défini dans le même paquet que la méthode.

```go
type Library struct {
    books []Book
}

func (l *Library) GetMostSoldBooks(startYear, endYear int) SoldStat {
    ...
}
```

Ici, nous définissons un type `Library` basé sur le type `struct`. Nous prenons maintenant la fonction `GetMostSoldBooks` définie ci-dessus, nous en extrayons le paramètre library et nous le transformons en un type receveur, ce qui transforme la fonction en une méthode du type `*Library`. D'autre part, `*Library` décrit un pointeur vers `Library`.

C'est pratique, non seulement parce que Go offre un moyen de trouver des méthodes de types par leurs noms, mais aussi parce que cela nous permet de lier tous les algorithmes statistiques au type `*Library`. Nous aurons de toute façon besoin d'une instance de celui-ci dans tous ces algorithmes, car il contient toutes les données sur la bibliothèque que nous voulons traiter.

Au lieu de passer la bibliothèque comme un simple paramètre supplémentaire à chaque fonction, nous pouvons utiliser la bibliothèque comme receveur et — en retour — obtenir un couplage plus fort. Dans ce cas, cela rend notre code plus propre. Chaque nouvel algorithme statistique à ajouter à l'application doit désormais être une méthode du type `*Library`.

Voyons maintenant comment nous pouvons réellement utiliser le paquet `reflect` pour récupérer la méthode ci-dessus si nous n'avons que son nom.

```go
import "reflect"

m := reflect.ValueOf(&Library{}).MethodByName("GetMostSoldBooks")
```

D'abord, nous devons prendre une instance du type receveur (le type receveur étant `*Library`) et la transformer en une `reflect.Value` en la passant à `reflect.ValueOf()`. Sur la valeur retournée, nous pouvons ensuite appeler `MethodByName()` avec le nom de la méthode que nous voulons récupérer.

Ce que nous obtenons en retour est une fonction appelable enveloppée dans `reflect.Value` qui acceptera exactement les paramètres tels que nous les avons définis dans la définition de la méthode. Notez que lors de l'appel de cette fonction, l'instance de `*Library` que nous avons passée à `reflect.ValueOf()` sera utilisée comme type receveur. Cela signifie qu'[il est important](https://golang.org/pkg/reflect/#Value.MethodByName) que vous ayez déjà passé la bonne instance à la fonction `reflect.ValueOf()`.

Pour rendre la valeur retournée `m` dans l'exemple ci-dessus réellement appelable, nous devrons la convertir de `reflect.Value` vers un type de fonction réel avec les signatures correctes. Cela ressemblera à ceci :

```go
mCallable := m.Interface().(func(int, int) SoldStat)
```

Notez que nous devons d'abord la transformer en un type interface et seulement ensuite la convertir vers le type fonction.

### Rendre les méthodes génériques

Très bien. Nous avons maintenant une méthode appelable que nous avons récupérée en passant le nom de la fonction à notre application et en laissant la réflexion faire le reste. Mais lorsqu'il s'agit d'appeler la fonction réelle, nous avons encore un petit problème.

Nous devons connaître la signature de la fonction pour pouvoir convertir la `reflect.Value` renvoyée par `MethodByName()` en une fonction appelable. Comme nous avons beaucoup d'algorithmes analytiques différents, il y a de fortes chances que les paramètres qu'ils acceptent diffèrent (nous ne voulons certainement pas imposer une signature de fonction spécifique aux développeurs qui souhaitent étendre l'application). Cela signifie que les signatures de méthode varient et que nous ne pouvons pas simplement convertir toutes les valeurs renvoyées par la réflexion vers le même type de fonction exact.

Ce que nous devons faire, c'est fournir une signature de fonction générique. Nous pouvons le faire en créant une méthode wrapper.

```go
func (l *Library) GetMostSoldBooksWrap(p GenericParams) Reportable {
    return l.GetMostSoldBooks(p.(*MostSoldBooksParams))
}
```

Ici, nous avons une méthode wrapper `GetMostSoldBooksWrap` pour la méthode concrète `GetMostSoldBooks`. Comme la méthode concrète, le wrapper est une méthode de type `*Library`. La différence réside dans sa signature. Elle accepte un paramètre générique `GenericParams` et renvoie une instance de type `Reportable`. Dans son corps, elle invoque la méthode analytique concrète qui traite les données de la bibliothèque. Le type `MostSoldBooksParams`, qui enveloppe les paramètres de la méthode concrète, est également nouveau.

Voyons maintenant d'où viennent ces nouveaux types.

Afin de pouvoir passer le paramètre `GenericParams` à la méthode concrète `GetMostSoldBooks()`, la méthode concrète doit également n'accepter qu'un seul paramètre vers lequel nous pouvons convertir le paramètre générique. Nous faisons cela en changeant la signature de la méthode concrète pour qu'elle accepte un paramètre `*MostSoldBooksParams`.

Cela peut sembler au premier abord comme si nous imposions finalement une signature de méthode aux algorithmes analytiques, contredisant ainsi l'affirmation faite plus haut. Et d'une certaine manière, c'est vrai. Mais d'une autre manière, ça ne l'est pas, car `MostSoldBooksParams` est de type `struct` et peut donc contenir plusieurs champs.

```go
type MostSoldBooksParams struct { 
    startYear int
    endYear int
}

func (l *Library) GetMostSoldBooks(p *MostSoldBooksParams) SoldStat {
    ...
}
```

Comme vous pouvez le voir, le paramètre de la méthode analytique intègre toujours les deux paramètres entiers `startYear` et `endYear` que nous avions définis à l'origine dans la signature de la méthode. La méthode renvoie également toujours le type concret `SoldStat`.

Revenons à la méthode wrapper.

Comme nous devons maintenant faire correspondre les chaînes du fichier de configuration aux méthodes wrapper plutôt qu'aux méthodes concrètes, nous avons besoin d'un wrapper pour chaque algorithme analytique. Il doit être nommé de manière à ce qu'il soit logique d'ajouter ce nom au fichier de configuration.

Dans cette solution, nous nommons les wrappers `<nom de la méthode concrète>Wrap`. Dans le fichier de configuration, nous pouvons alors simplement fournir le nom de la méthode concrète et la logique de réflexion ajoutera « Wrap » à la chaîne avant de chercher la méthode.

Les signatures, cependant, sont exactement les mêmes pour chaque fonction wrapper (sinon elles seraient inutiles).

```go
type GenericParams interface { 
   IsValid() (bool, string)
}
```

Le type de paramètre `GenericParam` est une interface. Nous déclarons une méthode `IsValid() (bool, string)` pour cette interface, ce qui signifie que toute structure qui définit cette méthode implémente automatiquement l'[interface](https://gobyexample.com/interfaces) `GenericParams`.

C'est important car dans notre méthode wrapper, nous convertissons l'interface `GenericParams` vers le type de structure concret `MostSoldBooksParams`. Cela ne fonctionne que si `MostSoldBooksParams` implémente l'interface `GenericParams`.
Nous fournissons donc maintenant une méthode `IsValid()` à notre type de paramètre concret.

```go
func (p *MostSoldBooksParams) IsValid() (bool, string) {
 …
 return true, ""
}
```

La fonction `IsValid()` elle-même peut être utilisée pour vérifier la validité des paramètres passés à la méthode analytique concrète. Nous pouvons l'appeler au tout début de la méthode.

```go
func (l *Library) GetMostSoldBooks(p *MostSoldBooksParams) SoldStat
{
    if isValid, reason := p.IsValid(); !isValid {
        log.Fatalf("\nParams invalid:: %s", reason)
    }
    ...
}
```

Enfin, nous avons le type `Reportable`, qui est notre valeur de retour générique.

```go
type Reportable interface { 
    Report() HTMLStatisticReport 
}
```

Comme le type de paramètre générique, `Reportable` est une interface. Elle déclare une méthode `Report()` qui renverra un rapport statistique au format HTML.

Puisque notre méthode wrapper générique renvoie directement la sortie de la méthode concrète, le type de retour de la méthode concrète doit être du type de retour de la méthode wrapper générique. Cela signifie que notre type `SoldStat`, qui est le type renvoyé par la méthode analytique concrète, doit implémenter l'interface `Reportable`.

Nous le faisons à nouveau en écrivant une implémentation de la méthode déclarée par l'interface.

```go
func (p SoldStat) Report() HTMLStatisticReport {
    ...créer le rapport...
}
```

Nous devrons implémenter ces méthodes pour tous les différents types de retour de tous les algorithmes statistiques afin que les types puissent être renvoyés par les wrappers génériques. Bien que cela puisse sembler introduire une surcharge de travail importante, la conversion de la sortie statistique de chaque algorithme en un rapport lisible par l'homme est quelque chose qui doit de toute façon être fait.

Maintenant que nous avons notre conception générique, nous pouvons revenir aux réflexions.

```go
m := reflect.ValueOf(library).MethodByName("GetMostSoldBooksWrap")
mCallable = m.Interface().(func(GenericParams) Reportable)
```

Ces deux lignes de réflexion peuvent maintenant être utilisées pour récupérer n'importe quel wrapper de méthode analytique par son nom, où `mCallable` sera la méthode wrapper appelable.

### Passage de paramètres

Ce qui manque, ce sont les paramètres de la méthode. Ceux-ci devront être extraits du fichier de configuration tout comme le nom de la méthode, puis passés à la méthode wrapper que nous avons récupérée via la réflexion. C'est là que les choses deviennent un peu complexes.

```
statistics: 
    — statsMethodName: GetMostSoldBooks 
      startYear: 1984
      endYear: 2018
```

L'exemple ci-dessus montre un fichier de configuration au format YAML. Nous avons un élément racine `statistics` qui correspond à une liste. Chaque élément de la liste est un algorithme analytique que nous voulons exécuter et dont nous voulons inclure la sortie dans le rapport. Les éléments consistent en une clé `statsMethodName`, avec le nom de la méthode analytique comme valeur, et une clé par paramètre avec leurs valeurs correspondantes. Notez que les noms des paramètres doivent correspondre aux noms des champs dans la structure de paramètres déclarée pour la méthode associée. Dans ce cas, la structure de paramètres est celle que nous avons déclarée précédemment, à savoir `MostSoldBooksParams`, avec les champs `startYear` et `endYear`, tous deux de type entier.

Ce que nous devons ajouter à notre réflexion maintenant, c'est la correspondance des chaînes (et d'autres types de valeurs) définissant les paramètres, du fichier de configuration vers les champs de la structure de paramètres de la méthode.

Comme la structure de paramètres de la méthode concrète figure dans la signature de la méthode concrète mais pas dans la signature de la méthode wrapper, nous devrons récupérer la méthode concrète via la logique de réflexion en plus de la méthode wrapper.

```go
methodName := "GetMostSoldBooks" // récupéré depuis le fichier de configuration
conreteMethod := reflect.ValueOf(library).MethodByName(methodName)

wrapperName := fmt.Sprintf("%sWrap", methodName)
wrapperMethod := reflect.ValueOf(library).MethodByName(wrapperName)
```

Ensuite, nous devons accéder au type de paramètre passé à la [méthode concrète](https://golang.org/pkg/reflect/#Type).

```go
concreteMethodParamsType := conreteMethod.Type().In(0).Elem()
```

`concreteMethodParamsType` contiendra désormais le type de la structure de paramètres de la méthode. Dans le cas de `GetMostSoldBooks`, il s'agit de `MostSoldBooksParams`.

Afin de pouvoir récupérer les champs de la structure (qui représentent les paramètres nécessaires à l'algorithme analytique) par leurs noms (qui sont donnés dans le fichier de configuration), nous devons créer une instance du type de structure de paramètres de la méthode. Nous avons besoin à la fois d'un pointeur vers l'instance et de l'instance elle-même (comme nous le verrons plus tard).

```go
concreteMethodParamsPtr := reflect.New(concreteMethodParamsType)
concreteMethodParams := concreteMethodParamsPtr.Elem()
```

À ce stade, vous pouvez itérer sur les clés de l'élément stats du fichier de configuration et faire correspondre les types de paramètres un par un aux champs du paramètre (c'est-à-dire récupérer les champs de la structure de paramètres de la méthode en fonction de leurs noms). Pour récupérer un champ d'une structure [par son nom](https://golang.org/pkg/reflect/#Value.FieldByName), nous pouvons utiliser `reflect.FieldByName()`.

```go
parameterField := concreteMethodParams.FieldByName(configParam)
```

Une fois que nous avons récupéré les champs de paramètres, nous pouvons faire correspondre la valeur donnée pour ce paramètre dans le fichier de configuration au champ réel.

```go
if configValueInt, isInt := configValue.(int); isInt {
    parameterField.SetInt(int64(configValueInt)
)
```

Ce qui précède concerne le cas des valeurs entières, mais nous pourrions faire de même pour chaque type de valeur attendu (par tâtonnements) pour chaque paramètre donné dans le fichier de configuration. Définir la valeur sur le champ de paramètre ici affectera également directement la structure de paramètres de la méthode, nous n'avons donc pas besoin de modifier explicitement `concreteMethodParams` pour stocker la valeur du paramètre récupérée du fichier de configuration.

Enfin, tout comme nous l'avons fait avec la méthode wrapper, nous allons convertir la structure `concreteMethodParams` vers un type `GenericParams`. Notez que nous devons utiliser le type pointeur ici.

```go
wrapperParams := concreteMethodParamsPtr.Interface().(GenericParams)
```

### Assembler le tout

Une fois que nous avons notre méthode wrapper et notre paramètre de méthode générique, nous pouvons appeler le wrapper comme suit.

```go
wrapperMethod(wrapperParams)
```

Comme vous pouvez le voir, il s'agit d'un appel de fonction normal. Cela fait exactement la même chose que d'appeler le wrapper sans passer par le processus de réflexion.

Enfin, vous aurez juste besoin d'une fonction qui appelle `Report()` sur toutes les valeurs de retour des fonctions wrapper des méthodes analytiques invoquées et qui regroupe les rapports de chaque statistique dans un fichier de rapport cohérent.

Maintenant, la question que vous devriez vous poser est : **Est-ce du bon code ?**

Ma réponse : **Je ne sais pas.**

Ce que je _peux_ vous dire, c'est que c'est une option qui vaut la peine d'être explorée. Surtout si vous vous retrouvez dans une situation où vous avez besoin d'une conception logicielle avec des exigences similaires à celles de cet exemple — même si ce n'est que dans le but d'en apprendre davantage sur les réflexions.

Si vous voulez voir le code complet d'une application utilisant cette conception, consultez : [https://github.com/Demonware/harbor-analytics](https://github.com/Demonware/harbor-analytics)