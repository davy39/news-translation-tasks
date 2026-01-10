---
title: Une manière sans stress pour tester les appels de méthodes statiques frustrants
  en Kotlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T18:48:29.000Z'
originalURL: https://freecodecamp.org/news/a-stress-free-way-to-test-frustrating-static-method-calls-in-kotlin-81db43e7ed82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fylN7XB0FWB7vVVF8yfoqQ.png
tags:
- name: development
  slug: development
- name: Kotlin
  slug: kotlin
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Une manière sans stress pour tester les appels de méthodes statiques frustrants
  en Kotlin
seo_desc: 'By Oleksii Fedorov

  Let me make a wild guess… You have encountered some code in Kotlin that is using
  some third-party library. The API that the library provides is one or a few static
  methods. And you want to test some code using these static methods....'
---

Par Oleksii Fedorov

Permettez-moi de faire une supposition audacieuse… Vous avez rencontré du code en Kotlin qui utilise une bibliothèque tierce. L'API que la bibliothèque fournit est composée d'une ou de quelques méthodes statiques. Et vous voulez tester du code utilisant ces méthodes statiques. C'est douloureux.

Vous n'êtes pas sûr de la manière d'aborder ce problème.

Peut-être vous demandez-vous, « Quand les auteurs de bibliothèques tierces cesseront-ils d'utiliser des méthodes statiques ? »

En tout cas, qui suis-je pour vous dire comment tester les appels de méthodes statiques en Kotlin ?

Je suis un fanatique des tests et un évangéliste du développement piloté par les tests depuis les cinq dernières années — ils m'appellent [TDD Fellow](http://tddfellow.com/) pour une raison. J'ai travaillé avec Kotlin en production pendant environ deux ans au moment d'écrire ceci.

En avant !

Voici ce que je ressens lorsque je vois de telles API horribles :

![Image](https://cdn-media-1.freecodecamp.org/images/VqR1mKMGNy9Q80UjC7KRGAB3I4WVgDA428t6)
_(source : pexels.com)_

Permettez-moi de vous montrer ce que je veux dire avec un exemple approximatif que j'ai dû gérer récemment. La bibliothèque était un client `newrelic`. Pour l'utiliser, je devais appeler une méthode statique sur une certaine classe. Si simplifié, cela ressemble à ceci :

```kotlin
NewRelicClient.addAttributesToCurrentRequest("orderId", order.id)
```

Je devais changer ce que nous envoyions exactement, et j'ai dû ajouter plus d'attributs. Comme je voulais avoir confiance que mon changement ne cassait rien et faisait exactement ce que je voulais, j'ai dû écrire un test. Il n'y avait pas encore de test pour ce code.

Si vous lisez toujours, je suppose que vous êtes dans la même situation. Ou vous l'avez été dans le passé.

Je suis d'accord que c'est une situation douloureuse.

Comment suis-je censé mock ces appels dans le test ?

Je sais, c'est frustrant que la plupart des bibliothèques de mocking soient incapables de mock les appels de méthodes statiques. Et même celles qui fonctionnent en Java ne fonctionnent pas toujours en Kotlin.

Il existe des bibliothèques qui pourraient le faire, comme `powermock`, par exemple. Mais vous savez quoi ? Peut-être utilisez-vous déjà `mockito` ou une autre bibliothèque. Ajouter un autre outil de mocking au projet rendra les choses plus confuses et frustrantes.

Je sais à quel point il est ennuyeux d'avoir plusieurs outils pour le même travail dans la même base de code. Cela cause beaucoup de confusion pour tout le monde.

Eh bien, ce problème a déjà été résolu il y a environ deux décennies !

Intéressé ? Venez faire un tour.

### Refactoring vers l'Objet Modeste

Jetons un coup d'œil au code avec lequel nous travaillons ici :

```kotlin
class FulfilOrderService {

    fun fulfil(order: Order) {
    
        // .. faire diverses choses ..
        
        NewRelicClient.addAttributesToCurrentRequest(
                "orderId", order.id)
        NewRelicClient.addAttributesToCurrentRequest(
                "orderAmount", order.amount.toString())
                
    }
    
}
```

Il fait diverses choses avec la commande pour la remplir, puis il attribue quelques attributs à la requête actuelle pour `newrelic`.

La première chose que nous allons faire ensemble ici est d'extraire la méthode `addAttributesToRequest`. Nous voulons également la paramétrer avec les arguments `key` et `value`. Vous pouvez le faire manuellement, ou, si vous avez la chance d'utiliser IntelliJ IDEA, vous pouvez faire ce refactoring automatiquement.

Voici comment :

1. Sélectionnez `"orderId"` et extrayez une variable locale. Nommez-la `key`.
2. Sélectionnez `order.id` et extrayez une variable locale. Nommez-la `value`.
3. Sélectionnez `NewRelicClient.addAttributesToCurrentRequest(key, value)` et extrayez une méthode. Nommez-la `addAttributesToRequest`.
4. IntelliJ mettra en évidence cet deuxième appel à `NewRelicClient` comme un duplicata et vous dira que vous pouvez le remplacer par l'appel à la nouvelle méthode privée. IntelliJ vous demandera si vous voulez le faire. Faites-le.
5. Inline les variables `key` et `value`.
6. Enfin, rendez la méthode `protected` au lieu de `private`. Je vous montrerai dans un instant pourquoi la méthode doit être protégée.
7. Vous remarquerez qu'IntelliJ met en évidence `protected` avec un avertissement. C'est parce que toutes les classes en Kotlin sont `final` par défaut. Comme les classes finales ne sont pas extensibles, `protected` est inutile. L'une des solutions qu'IntelliJ propose est de rendre la classe `open`. Faites-le. La méthode `addAttributesToRequest` devrait également devenir open.

Voici ce que vous devriez obtenir à la fin :

```kotlin
open class FulfilOrderService {

    fun fulfil(order: Order) {
    
        // .. faire diverses choses ..
        
        addAttributesToRequest("orderId", order.id)
        addAttributesToRequest("orderAmount",
                               order.amount.toString())
                               
    }
    
    protected open fun addAttributesToRequest(key: String,
                                              value: String) {
                                              
        NewRelicClient.addAttributesToCurrentRequest(key, value)
        
    }
    
}
```

Remarquez comment tous ces refactorings étaient complètement automatiques et donc sûrs à exécuter. Nous n'avons pas besoin de tests pour cela. Avoir cette méthode en tant que protégée nous donnera l'opportunité d'écrire un test :

```kotlin
private val attributesAdded = mutableListOf<Pair<String, String>>()

private val subject = FulfilOrderService()

@Test
fun `ajoute l'identifiant de commande à la requête actuelle dans newrelic`() {

    val order = Order(id = "some-id", amount = 142)
    
    subject.fulfil(order)
    
    val expectedAttributes = listOf(
            Pair("orderId", "some-id"),
            Pair("orderAmount", "142"))
    assertEquals(expectedAttributes, attributesAdded)
    
}
```

En parlant de tests et de refactoring...

Voulez-vous apprendre à écrire un test d'acceptation en Kotlin ? Peut-être comment utiliser la puissance d'IntelliJ IDEA à votre avantage ?

Peut-être voulez-vous apprendre à construire des applications en Kotlin correctement ? — qu'il s'agisse d'applications en ligne de commande, web ou android ?

Il y a ce tutoriel e-book ultime que j'ai ACCIDENTELLEMENT écrit sur la prise en main de Kotlin. 350 pages de tutoriel pratique que vous pouvez suivre.

Vous aurez l'impression que je suis assis avec vous et que nous passons un bon moment, tout en construisant une application en ligne de commande complète.

Intéressé ?

Téléchargez le [tutoriel ultime ici](https://iwillteachyoukotlin.com/). D'ailleurs, il est gratuit et le restera toujours !

Revenons à notre test.

Tout cela semble correct, mais cela ne fonctionne pas parce que personne n'ajoute d'éléments à la liste `attributesAdded`. Puisque nous avons cette petite méthode protégée, nous pouvons « pirater » :

```kotlin
private val subject: FulfilOrderService = object :
                                          FulfilOrderService() {
                                          
    override fun addAttributesToRequest(key: String,
                                        value: String) {
                                        
        attributesAdded.add(Pair(key, value))
        
    }
    
}
```

Si vous exécutez le test, il passe. Vous pouvez changer les valeurs dans le test ou le code de production pour voir l'échec et vous assurer qu'il teste bien ce que vous pensez.

Regardons le code de test complet :

```kotlin
import org.junit.Assert.*
import org.junit.Test

@Suppress("FunctionName")
class FulfilOrderServiceTest {

    private val attributesAdded = 
            mutableListOf<Pair<String, String>>()
            
    private val subject: FulfilOrderService = object :
                                      FulfilOrderService() {
                                      
        override fun addAttributesToRequest(key: String,
                                            value: String) {
                                            
            attributesAdded.add(Pair(key, value))
            
        }
        
    }
    
    @Test
    fun `ajoute l'identifiant de commande à la requête actuelle dans newrelic`() {
    
        val order = Order(id = "some-id", amount = 142)
        
        subject.fulfil(order)
        
        val expectedAttributes = listOf(
                Pair("orderId", "some-id"),
                Pair("orderAmount", "142"))
        assertEquals(expectedAttributes, attributesAdded)
        
    }
    
}
```

Alors, que vient-il de se passer ici ?

Voyez-vous, j'ai fait une version légèrement différente de la classe `FulfilOrderService` — une version testable. La seule faiblesse de cette méthode de test est que si quelqu'un se trompe avec la fonction `addAttributesToRequest`, aucun test ne se cassera.

D'un autre côté, cette fonction n'aura jamais à contenir plus d'une ligne de code simple et ne changera probablement pas souvent. Cela n'arrivera que dans le cas où les auteurs de la bibliothèque tierce que nous utilisons vont introduire un changement cassant dans cette méthode unique.

C'est peu probable. Cela arrivera probablement tous les quelques années.

Et vous savez quoi ?

Même si vous testez cela de manière plus « boîte noire » que ce que je propose ici, lorsqu'un tel changement cassant arrive, vous devrez toujours revisiter toutes les utilisations et les corriger. Probablement, vous devrez jeter ou réécrire tous les tests associés aussi.

Oh, et en cas de tel changement cassant, je recommanderais toujours de tester manuellement au moins une fois pour voir si vous avez bien compris la nouvelle API et qu'elle interagit avec le système tiers de la manière que vous pensez.

Étant donné toutes ces informations, je suppose qu'il devrait être acceptable de laisser cette ligne non testée.

Mais si un tel changement arrive, devez-vous chasser tous les endroits où nous appelons `NewRelicClient` ?

Réponse courte — oui.

Réponse longue : dans la conception actuelle — oui. Mais avez-vous pensé que nous avons terminé ici ?

Non.

La conception est terrible telle qu'elle est maintenant. Corrigons cela via l'extraction de l'Objet Modeste. Une fois que nous aurons fait cela, il n'y aura qu'un seul endroit dans toute la base de code qui nécessitera un changement — cet objet modeste.

Malheureusement, IntelliJ ne supporte pas encore les refactorings `Move method` ou `Extract method object` pour Kotlin, donc nous devrons effectuer celui-ci manuellement.

Mais vous savez quoi ? — C'est OK parce que nous avons déjà des tests associés pour nous soutenir !

Pour faire le refactoring `Extract method object`, nous devrons remplacer l'implémentation à l'intérieur de la méthode par la création d'un objet, et un appel immédiat à la méthode de cet objet avec les mêmes arguments que la méthode refactorée :

```kotlin
protected open fun addAttributesToRequest(key: String,
                                          value: String) {
                                          
//   NewRelicClient.addAttributesToCurrentRequest(key, value)
    NewRelicHumbleObject().addAttributesToRequest(key, value)
    
}
```

Ensuite, nous devrons créer cette classe et créer la méthode dessus. Enfin, nous mettrons le contenu de la méthode refactorée, celle que nous avons commentée, dans la méthode nouvellement créée ; n'oubliez pas de supprimer le commentaire car nous n'en avons plus besoin :

```kotlin
class NewRelicHumbleObject {
    
    fun addAttributesToRequest(key: String, value: String) {
        
        NewRelicClient.addAttributesToCurrentRequest(key, value)
        
    }
    
}
```

Nous avons terminé cette étape de refactoring, et nous devrions exécuter nos tests maintenant. Ils devraient tous passer si nous n'avons pas fait d'erreurs — et ils passent !

L'étape suivante de ce refactoring est de déplacer la création de l'objet modeste dans le champ. Ici, nous pouvons effectuer un refactoring automatisé pour extraire le champ de l'expression `NewRelicHumbleObject()`. Voici ce que vous devriez obtenir après le refactoring :

```kotlin
private val newRelicHumbleObject = NewRelicHumbleObject()

protected open fun addAttributesToRequest(key: String,
                                          value: String) {
                                          
    newRelicHumbleObject.addAttributesToRequest(key, value)
    
}
```

Maintenant, parce que nous avons cette valeur dans le champ, nous pouvons la déplacer dans le constructeur. Il y a aussi un refactoring automatisé pour cela ! Il s'appelle `Move to constructor`. Vous devriez obtenir le résultat suivant :

```kotlin
open class FulfilOrderService(
        private val newRelicHumbleObject: NewRelicHumbleObject =
                                          NewRelicHumbleObject()) {
                                          
    fun fulfil(order: Order) {
    
        // .. faire diverses choses ..
        
        addAttributesToRequest("orderId", order.id)
        addAttributesToRequest("orderAmount",
                               order.amount.toString())
                               
    }
    
    protected open fun addAttributesToRequest(key: String,
                                              value: String) {
                                              
        newRelicHumbleObject.addAttributesToRequest(key, value)
        
    }
    
}
```

Cela rendra super simple l'injection de la dépendance depuis le test. Et remarquez, c'est un objet ordinaire avec une méthode non statique.

Savez-vous ce que cela signifie ?

Oui ! Vous pouvez utiliser votre outil de mocking préféré pour mock cela. Faisons exactement cela maintenant. J'utiliserai `mockito` pour cet exemple.

Tout d'abord, nous devrons créer le mock dans notre test :

```kotlin
private val newRelicHumbleObject =
        Mockito.mock(NewRelicHumbleObject::class.java)
```

Pour pouvoir mock notre objet modeste, nous devrons rendre sa classe `open` et la méthode `addAttributesToRequest` open aussi :

```kotlin
open class NewRelicHumbleObject {

    open fun addAttributesToRequest(key: String, value: String) {
        // ...
        
    }
    
}
```

Ensuite, nous devrons fournir ce mock en tant qu'argument au constructeur de `FulfilOrderService` :

```kotlin
private val subject = FulfilOrderService(newRelicHumbleObject)
```

Enfin, nous voulons remplacer notre assertion par la vérification de `mockito` :

```kotlin
Mockito.verify(newRelicHumbleObject)
        .addAttributesToRequest("orderId", "some-id")
Mockito.verify(newRelicHumbleObject)
        .addAttributesToRequest("orderAmount", "142")
Mockito.verifyNoMoreInteractions(newRelicHumbleObject)
```

Ici, nous vérifions que la méthode `addAttributesToRequest` de notre objet modeste a été appelée avec les arguments appropriés deux fois et rien d'autre. Et nous n'avons plus besoin du champ `attributesAdded`, alors débarrassons-nous de cela.

Voici ce que vous devriez obtenir maintenant :

```kotlin
class FulfilOrderServiceTest {

    private val newRelicHumbleObject =
            Mockito.mock(NewRelicHumbleObject::class.java)
            
    private val subject = FulfilOrderService(newRelicHumbleObject)
    
    @Test
    fun `ajoute l'identifiant de commande à la requête actuelle dans newrelic`() {
    
        val order = Order(id = "some-id", amount = 142)
        
        subject.fulfil(order)
        
        Mockito.verify(newRelicHumbleObject)
                .addAttributesToRequest("orderId", "some-id")
        Mockito.verify(newRelicHumbleObject)
                .addAttributesToRequest("orderAmount", "142")
        Mockito.verifyNoMoreInteractions(newRelicHumbleObject)
        
    }
    
}
```

Maintenant que nous ne remplaçons plus cette méthode protégée, nous pouvons l'inliner. D'ailleurs, la classe n'a plus besoin d'être `open`. Notre classe `FulfilOrderService` est maintenant prête à accepter les changements que nous voulions faire, car elle est testable maintenant (au moins en ce qui concerne les attributs de requête `newrelic`) :

```kotlin
class FulfilOrderService(
        private val newRelicHumbleObject: NewRelicHumbleObject = 
                                          NewRelicHumbleObject()) {
                                          
    fun fulfil(order: Order) {
    
        // .. faire diverses choses ..
        
        newRelicHumbleObject.addAttributesToRequest(
                "orderId", order.id)
        newRelicHumbleObject.addAttributesToRequest(
                "orderAmount", order.amount.toString())
                
    }
    
}
```

Exécutons tous les tests à nouveau, juste pour être sûr ! — ils passent tous.

Super, je pense que nous avons terminé ici.

### Partagez ce que vous pensez de l'Objet Modeste !

Merci d'avoir lu !

Cela me rendrait heureux si vous partagez ce que vous pensez de ce refactoring dans les commentaires. Connaissez-vous une manière plus simple de refactorer cela ? — partagez !

De plus, si vous aimez ce que vous voyez, envisagez de me donner un applaudissement sur Medium et de partager l'article sur les réseaux sociaux.

Si vous êtes intéressé par l'apprentissage de Kotlin et que vous aimez mon style d'écriture, [prenez mon tutoriel ultime pour commencer avec Kotlin](https://iwillteachyoukotlin.com/).

### Mes articles liés

[**Comment le "@Deprecated" de Kotlin soulage la douleur du refactoring colossal ?**](https://hackernoon.com/how-kotlins-deprecated-relieves-pain-of-colossal-refactoring-8577545aaed)  
[_Je vais vous raconter une histoire vraie sur la façon dont nous nous sommes économisé des tonnes de temps. La puissance du refactoring @Deprecated de Kotlin…_](https://hackernoon.com/how-kotlins-deprecated-relieves-pain-of-colossal-refactoring-8577545aaed)  
[hackernoon.com](https://hackernoon.com/how-kotlins-deprecated-relieves-pain-of-colossal-refactoring-8577545aaed)

[**Comment la calamité Kotlin dévore vos applications Java comme un éclair ?**](https://hackernoon.com/how-kotlin-calamity-devours-your-java-apps-like-cancer-f3ce9500a028)  
[_J'entends ce que vous dites. Il y a ce buzz autour d'Android adoptant activement Kotlin comme langage de programmation principal…_](https://hackernoon.com/how-kotlin-calamity-devours-your-java-apps-like-cancer-f3ce9500a028)  
[hackernoon.com](https://hackernoon.com/how-kotlin-calamity-devours-your-java-apps-like-cancer-f3ce9500a028)

[**Refactoring par Changement Parallèle**](https://medium.com/@oleksii_f/parallel-change-refactoring-b83a2993ef26)  
[_Le Changement Parallèle est la technique de refactoring qui permet d'implémenter des changements rétro-incompatibles à une API de manière sûre…_](https://medium.com/@oleksii_f/parallel-change-refactoring-b83a2993ef26)  
[medium.com](https://medium.com/@oleksii_f/parallel-change-refactoring-b83a2993ef26)