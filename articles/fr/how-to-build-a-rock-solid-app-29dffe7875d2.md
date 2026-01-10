---
title: Comment construire une application ultra-fiable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-03T16:18:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-rock-solid-app-29dffe7875d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4ZdfWIIB1rwY8wjXMkfb0g.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment construire une application ultra-fiable
seo_desc: 'By Simone Di Maulo

  An overview of different app design options

  When we design software, we constantly think about error cases. Errors have a huge
  impact on the way we design and architecture a solution. So much so, in fact, that
  there is a philosophy...'
---

Par Simone Di Maulo

#### Aperçu des différentes options de conception d'applications

Lorsque nous concevons des logiciels, nous pensons constamment aux cas d'erreur. Les erreurs ont un impact énorme sur la manière dont nous concevons et architecturons une solution. Tellement, en fait, qu'il existe une philosophie connue sous le nom de [Let It Crash](http://wiki.c2.com/?LetItCrash).

**Let it crash** est la manière Erlang de traiter les échecs en laissant simplement l'application planter et en permettant à un superviseur de redémarrer le processus planté à partir d'un état propre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lVLik3M6m33YZ52n0iHclQ.png)
_Les superviseurs redémarrent le processus planté_

Les erreurs peuvent être partout, et plus votre application grandit, plus il y aura de points de défaillance que vous devez garder sous contrôle. Les appels de services externes, l'envoi d'e-mails, les requêtes de base de données sont toutes des opérations qui peuvent échouer.

#### Types de défaillances

Une défaillance peut avoir différentes origines qui entraînent différents impacts sur la disponibilité de votre service. Imaginez un scénario où nous exécutons trop de requêtes SQL et le serveur de base de données va limiter l'application. Dans ce cas, nous pourrions réessayer la requête ou ajouter un catch dans le code pour identifier les requêtes échouées et fournir une réponse sensée à l'utilisateur.

Ces types d'erreurs sont appelés **Erreurs transitoires**, ce qui signifie que le serveur de base de données est temporairement surchargé mais qu'il va revenir bientôt.

**Les erreurs transitoires** ne sont pas liées à un problème dans l'application. Elles sont généralement causées par des conditions externes telles que des défaillances réseau, des serveurs surchargés ou des limites de taux de service. Pour cette raison, il est sûr pour un client de l'ignorer et de réessayer l'opération échouée après un certain temps.

Ces erreurs sont beaucoup plus fréquentes dans les applications cloud natives, car les applications sont divisées en différents services et déployées sur différents serveurs qui communiquent via le réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SjWLLvJNhNtqAjuGviDYBQ.png)

#### Identification des erreurs transitoires

Les erreurs transitoires peuvent généralement être détectées de manière automatique.   
Nous pouvons reconnaître les erreurs en inspectant les métadonnées de la couche de transport (par exemple, les erreurs HTTP, les erreurs réseau, les délais d'attente) ou lorsqu'elles sont explicitement marquées comme transitoires (telles que les limites de taux).

#### Traitement des erreurs

Il existe différentes actions que nous pouvons effectuer en cas d'erreur. Une approche triviale pourrait être de simplement réessayer la requête, l'appel d'API ou la requête.

Bien que cette solution puisse être acceptable dans de nombreux cas, il existe de nombreux cas où elle peut entraîner une diminution des performances de l'application.

Prenons le cas d'une défaillance réseau. Réessayer indéfiniment certains appels d'API à un service déconnecté entraînerait des délais d'attente réseau continus, et l'application resterait bloquée en attendant une réponse pendant très longtemps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KaOlLRtoOIQXgxnIXVZzcQ.png)

Avant de passer à des implémentations complexes, évaluons les avantages et les inconvénients de l'option "just-retry".

**AVANTAGES**

* Implémentation triviale.
* Sans état (chaque requête de réessai est isolée et vous n'avez besoin d'aucune information supplémentaire).

**INCONVÉNIENTS**

* Pour les applications fortement chargées, l'appelant enverra continuellement des requêtes au serveur dégradé, entraînant un déni de service.
* Ne peut pas fournir de réponse jusqu'à ce que le serveur revienne.

Cette simple stratégie de réessai peut être considérée comme une première approche très basique pour résoudre le problème. Pour les applications à faible trafic, cela fonctionnerait, mais si vous avez une architecture plus complexe, cela n'est définitivement pas suffisant.

Discutons donc d'une approche plus résiliente.

#### Emprunter une idée à l'IEEE

La prochaine étape de votre voyage pour une application fiable est d'éviter le temps perdu et de rendre l'application plus réactive. L'algorithme de repli exponentiel pourrait être l'outil idéal pour cette tâche.

Le concept de **repli exponentiel** vient directement du protocole réseau [Ethernet](https://en.m.wikipedia.org/wiki/Exponential_backoff#Example_exponential_backoff_algorithm) (IEEE 802.3) où il est utilisé pour la résolution des collisions de paquets.

Pour nos besoins, le repli exponentiel peut être utilisé pour éviter de perdre du temps entre des appels en délai d'attente ou pour éviter de saturer un serveur surchargé avec un flux continu de requêtes qui ne peuvent pas être résolues.

Le repli exponentiel binaire pour les collisions de paquets peut être résumé avec l'aide de la définition suivante :

> Après *c* collisions, un nombre aléatoire de temps de slot entre 0 et 2*c* - 1 est choisi. Pour la première collision, chaque expéditeur attendra 0 ou 1 temps de slot. Après la deuxième collision, les expéditeurs attendront de 0 à 3 temps de slot. Après la troisième collision, les expéditeurs attendront de 0 à 7 temps de slot (inclus), et ainsi de suite. À mesure que le nombre de tentatives de retransmission augmente, le nombre de possibilités de retard augmente de manière exponentielle - [Exponential backoff - Wikipedia](https://en.m.wikipedia.org/wiki/Exponential_backoff)

![Image](https://cdn-media-1.freecodecamp.org/images/1*y1jkyHboflo5rqixjfh7Kw.png)

Cet algorithme peut être rapidement adapté à de nombreux cas d'utilisation. L'exemple suivant est une classe de gestionnaire de messages PHP qui attend de manière exponentielle une réponse d'un point de terminaison d'API.

```php
<?php
/**
 * Supposons que nous utilisons un bus de messages capable de
 * réessayer les messages échoués avec un délai de réessai personnalisé.
 */
class FetchCarMessageHandler
{
  public function handle(Message $msg)
  {
    try {
      $id = (int)$msg->getContent();
      $cars = $client->get('/car/'.$id);
  
      return Result::success($cars);
    } catch (TimeoutException $e) {
      $lastBackoff = $msg->getLastBackoff();
      // La couche infrastructure va automatiquement réessayer le message après XYZ secondes
      return Result::retryAfter($lastBackoff * 2, $msg);
    }
  }
}
```

#### Réessai vs Repli exponentiel

Les deux stratégies précédentes sont toutes deux sous-optimales. Elles garantissent que vous pourrez éventuellement générer une réponse à renvoyer au client, mais elles reposent sur l'appel continu du service externe jusqu'à ce qu'une réponse réussie soit reçue.

Nous pouvons avoir de la chance et recevoir une réponse après quelques réessais, ou nous pouvons tomber dans la boucle infinie réessai-attente-réessai-attente... et ne jamais recevoir la réponse.  
Vous savez, la loi de Murphy est toujours là : "Tout ce qui peut mal tourner tournera mal."

Comme vous pouvez l'imaginer, mettre à l'échelle une infrastructure orientée services qui, en cas de défaillance, réessaie continuellement la requête vers les services dépendants est la recette parfaite pour l'effondrement de l'application.

Nous avons besoin d'une stratégie plus robuste pour maintenir la résilience de l'infrastructure.

#### L'électronique peut nous aider

![Image](https://cdn-media-1.freecodecamp.org/images/1*qnvQ3GiF27TlIZbFCr2omA.jpeg)
_[Source : https://pixabay.com/en/circuit-breakers-rcds-fault-current-1167327/](https://pixabay.com/en/circuit-breakers-rcds-fault-current-1167327/" rel="noopener" target="_blank" title=")_

En cas d'erreurs continues, la chose facile à faire est claire. Nous ne voulons pas boucler et réessayer d'appeler un service externe. Le point est que nous allons simplement **arrêter** de le faire, en prenant le concept de **Disjoncteurs** de l'électronique.

#### De l'électronique à l'informatique

Un disjoncteur est un composant qui enveloppe un appel protégé à un service externe et peut surveiller les réponses en vérifiant la santé du service. Exactement comme un composant électronique, un disjoncteur logiciel peut être **ouvert** ou **fermé**. Un statut **ouvert** signifierait que le service derrière le circuit est hors service, et un statut **fermé** signifierait que le service est opérationnel.

Ainsi, le disjoncteur peut contrôler de manière autonome le statut du service et décider d'**ouvrir** ou de **fermer** le circuit, de sorte qu'en cas de déconnexion ou de surcharge du serveur, le client arrête d'envoyer de nouvelles connexions et le service dégradé peut utiliser plus de ressources pour revenir à un état sain.

En cas de circuit **ouvert**, nous pourrions décider de répondre rapidement au client avec une réponse de repli. Par exemple, des données en cache, des données par défaut, ou tout ce qui a du sens pour l'application particulière.

Regardons un exemple réel du monde du commerce électronique. Nous allons utiliser la méthode du disjoncteur pour protéger l'appel d'API de liste de produits.

```php
<?php
class CircuitBreaker
{
  private $maxFailures;
  private $service;
  private $redisClient;
  
  public function __construct(int $maxFailures, callable $service)
  {
    $this->maxFailures = $maxFailures;
    $this->service = $service;
    $this->redisClient = new RedisClient();
  }
  private function isUp(string $key)
  {
    return (int)$this->redisClient->get($key) < $this->maxFailures;
  }
  private function fail(string $key, int $ttl)
  {
    $this->redisClient->incr($key, 1);
    $this->redisClient->expire($key, $ttl);
  }
  
  public function __invoke()
  {
    [$arguments, $defaultResponse] = func_get_args();
    $key = md5($arguments);
    if (!$this->isUp($key)) {
        return $defaultResponse;
    }
    try {
      $result = call_user_func_array($this->service, $arguments);
      
      return $result;
    } catch (\Throwable $e) {
      $this->fail($key, 10);
      
      return $defaultResponse;
    }
  }
}
```

Le disjoncteur gérera de manière transparente toutes les erreurs et affichera la réponse par défaut en cas d'échec d'un appel d'API. Il permet également de définir un nombre maximal de réessais pour éviter trop d'appels échoués.

Dans ce cas, protéger un appel d'API de service tiers est une tâche très simple : nous devons simplement fournir le callback et le nombre maximal d'échecs autorisés, après quoi le **disjoncteur** sera ouvert pendant 10 secondes et la réponse par défaut sera renvoyée au client, comme dans l'exemple ci-dessous.

```php
<?php
$productListing = new CircuitBreaker(
    10, 
    function($searchKey) {
        // $result est donné par l'appel d'API
        return $result;
    }
);
$productsToShow = $productListing(['t-shirt'], []);
```

#### Conclusion

Que vous conceviez une SOA, des microservices ou une application cloud native, vous devez être prêt à gérer les cas de défaillance de la bonne manière. Les erreurs et les défaillances sont dans la même pièce depuis le jour où vous lancez votre application.

Voici quelques-unes des tactiques bien connues pour construire une application vraiment ultra-fiable :

* [https://docs.microsoft.com/en-us/azure/architecture/patterns/retry](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry)
* [https://en.m.wikipedia.org/wiki/Exponential_backoff](https://en.m.wikipedia.org/wiki/Exponential_backoff)
* [https://martinfowler.com/bliki/CircuitBreaker.html](https://martinfowler.com/bliki/CircuitBreaker.html)