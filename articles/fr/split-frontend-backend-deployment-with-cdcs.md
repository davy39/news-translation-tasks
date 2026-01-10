---
title: Comment séparer le déploiement de votre front end et back end avec l'aide des
  tests de contrat pilotés par le consommateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-12T08:06:54.000Z'
originalURL: https://freecodecamp.org/news/split-frontend-backend-deployment-with-cdcs
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/simple-cdc-1.png
tags:
- name: CircleCI
  slug: circleci
- name: continuous delivery
  slug: continuous-delivery
- name: contract-testing
  slug: contract-testing
- name: Jest
  slug: jest
- name: pact
  slug: pact
seo_title: Comment séparer le déploiement de votre front end et back end avec l'aide
  des tests de contrat pilotés par le consommateur
seo_desc: 'By Mario Fernandez

  Consumer driven contract testing is a great way to improve the reliability of interconnected
  systems. Integration testing becomes way easier and more self contained. It opens
  the door for independent deployments, and leads to faste...'
---

Par Mario Fernandez

Les [tests de contrat pilotés par le consommateur](https://www.thoughtworks.com/de/radar/techniques/consumer-driven-contract-testing) sont un excellent moyen d'améliorer la fiabilité des systèmes interconnectés. Les tests d'intégration deviennent beaucoup plus faciles et plus autonomes. Cela ouvre la porte aux déploiements indépendants et conduit à des itérations plus rapides et à des retours plus granulaires. Contrairement à votre assurance, cela n'a pas de petites lignes. Cet article traite de sa mise en place dans un pipeline de livraison, dans le contexte de la réalisation de [livraison continue](https://continuousdelivery.com/).

Je veux montrer comment les _Tests de Contrat_ aident à séparer le déploiement du front end et du back end d'une petite application. J'ai un client React et un back end Spring Boot écrit en Kotlin.

## Qu'est-ce qu'un Test de Contrat ?

Je ne parle pas de [contrats intelligents](https://en.wikipedia.org/wiki/Smart_contract). Il n'y a aucune blockchain dans cet article. Désolé pour cela (les Tests de Contrat pour les Contrats Intelligents semble être une conférence dont le monde a désespérément besoin, cependant !).

En résumé, un Test de Contrat est une spécification des interactions entre un consommateur et un fournisseur. Dans notre cas, la communication se fait via REST. Le consommateur définit les actions envoyées au fournisseur et les réponses qui seront retournées. Dans notre cas, le front end est le consommateur et le back end est le fournisseur. Un _contrat_ est généré. Les deux parties testent contre ce contrat.

Ce n'est pas vraiment une question de technologie particulière. Il existe plusieurs frameworks différents, mais quelques scripts simples pourraient faire l'affaire.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/simple-cdc.png)

### Pourquoi l'avoir comme partie du pipeline de livraison ?

Tout d'abord, exécuter ces tests en continu garantit qu'ils continuent de fonctionner à tout moment. Le grand avantage, cependant, est que nous pouvons séparer le déploiement du front end et du back end. Si les deux parties respectent le contrat, il est probable qu'elles fonctionnent ensemble correctement. Ainsi, nous pouvons envisager d'éviter des tests intégrés coûteux. Ils tendent à mal fonctionner de toute façon.

## Mise en place de certains contrats

Il y a deux côtés à configurer, le consommateur et le fournisseur. Les tests s'exécuteront dans les pipelines qui construisent le front end et le back end, respectivement. Nous allons utiliser le [framework Pact](https://docs.pact.io/) pour nos exemples, qui est l'outil que je connais le mieux. Pour cette raison, j'ai tendance à utiliser pact et contrat de manière interchangeable. Nos pipelines sont écrits pour [CircleCI](https://circleci.com/), mais ils devraient être assez faciles à porter vers d'autres outils CI.

### Le côté consommateur

Comme mentionné, le consommateur mène la création du contrat. Avoir le client qui dirige cela peut sembler contre-intuitif. Souvent, les API sont créées avant les clients qui les utiliseront. Inverser cela est une bonne habitude à prendre. Cela vous force à vraiment penser en termes de ce que le client fera réellement, au lieu de perdre du temps sur une API super générique qui n'aura jamais besoin de la plupart de ses fonctionnalités. Vous devriez essayer !

Le pacte est défini à travers des interactions spécifiées dans des tests unitaires. Nous spécifions ce que nous attendons être envoyé au back end, puis utilisons le code client pour déclencher des requêtes. Pourquoi ? Nous pouvons comparer les attentes aux requêtes réelles, et échouer les tests si elles ne correspondent pas.

Regardons un exemple. Nous utilisons [Jest](https://jestjs.io/) pour exécuter les tests. Nous commençons par un peu de code d'initialisation :

```typescript
import path from 'path'
import Pact from 'pact'

const provider = () =>
  Pact({
    port: 8990,
    log: path.resolve(process.cwd(), 'logs', 'pact.log'),
    dir: path.resolve(process.cwd(), 'pacts'),
    spec: 2,
    consumer: 'frontend',
    provider: 'backend'
  })

export default provider

```

Ensuite, nous avons le code pour un test réel. Le test se compose de deux parties. D'abord, nous définissons l'interaction attendue. Cela n'est pas très différent de la simulation d'une bibliothèque http, avec quelque chose comme [axios](https://github.com/ctimmerm/axios-mock-adapter). Il spécifie la requête que nous allons envoyer (URL, en-têtes, corps, etc.), et la réponse que nous allons recevoir.

```typescript
const interaction: InteractionObject = {
  state: 'i have a list of recipes',
  uponReceiving: 'a request to get recipes',
  withRequest: {
    method: 'GET',
    path: '/rest/recipes',
    headers: {
      Accept: 'application/json',
      'X-Requested-With': 'XMLHttpRequest'
    }
  },
  willRespondWith: {
    status: 200,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
    body: [
      {
        id: 1,
        name: 'pasta carbonara',
        servings: 4,
        duration: 35
      }
    ]
  }
}

```

Ensuite, nous avons le test lui-même, où nous appelons le code client réel qui déclenchera la requête. J'aime encapsuler ces requêtes dans des services qui convertissent la réponse brute en modèle de domaine qui sera utilisé par le reste de l'application. À travers quelques assertions, nous nous assurons que les données que nous livrons depuis le service sont exactement ce que nous attendons.

```typescript
it('works', async () => {
  const response = await recipeList()

  expect(response.data.length).toBeGreaterThan(0)
  expect(response.data[0]).toEqual({
    id: 1,
    name: 'pasta carbonara',
    servings: 4,
    duration: 35
  })
})

```

Notez que même si `recipeList` est correctement typé avec `TypeScript`, cela ne nous aidera pas ici. Les types disparaissent à l'exécution, donc si la méthode retourne une `Recipe` invalide, nous ne nous en rendrons pas compte, sauf si nous le testons explicitement.

Enfin, nous devons définir quelques méthodes supplémentaires qui garantiront que les interactions sont vérifiées. Si des interactions sont manquantes, ou si elles ne ressemblent pas à ce qu'elles devraient être, le test échouera ici. Après cela, il ne reste plus qu'à écrire le pacte sur le disque.

```typescript
beforeAll(() => provider.setup())
afterEach(() => provider.verify())
afterAll(() => provider.finalize())

```

En fin de compte, le pacte est généré sous forme de fichier JSON, reflétant toutes les interactions que nous avons définies dans tous nos tests.

#### Correspondance flexible

Notre pacte jusqu'à présent spécifie les valeurs exactes qu'il recevra du back end. Cela ne sera pas maintenable à long terme. Certaines choses sont intrinsèquement plus difficiles à fixer à des valeurs exactes (par exemple, les dates).

Un pacte qui se brise constamment entraînera de la frustration. Nous passons par ce processus pour faciliter notre vie, pas pour la compliquer. Nous éviterons cela en utilisant des [matchers](https://docs.pact.io/getting_started/matching). Nous pouvons être plus flexibles et définir à quoi les choses ressembleront, sans avoir à fournir des valeurs exactes. Réécrivons notre corps précédent :

```typescript
willRespondWith: {
  status: 200,
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: Matchers.eachLike({
    id: Matchers.somethingLike(1),
    name: Matchers.somethingLike('pasta carbonara'),
    servings: Matchers.somethingLike(4),
    duration: Matchers.somethingLike(35)
  })
}

```

Vous pouvez être plus spécifique. Vous pouvez définir la longueur attendue d'une liste, utiliser des regex et plein d'autres choses.

#### Intégration dans le pipeline

Les tests de pacte reposent sur un processus externe, et avoir plusieurs tests qui l'utilisent peut entraîner un comportement non déterministe. Une solution consiste à exécuter tous les tests séquentiellement :

```bash
npm test --coverage --runInBand

```

Si vous souhaitez exécuter les tests de pacte indépendamment, nous pouvons créer notre propre tâche pour les exécuter séparément :

```json
"scripts": {
  "pact": "jest --transform '{\"^.+\\\\.ts$\": \"ts-jest\"}' --testRegex '.test.pact.ts$' --runInBand"
}

```

Ce qui deviendra une étape supplémentaire dans notre pipeline :

```yaml
jobs:
  check:
    working_directory: ~/app

    docker:
      - image: circleci/node:12.4

    steps:
      - checkout
      - run: npm
      - run: npm run linter:js
      - run: npm test --coverage --runInBand
      - run: npm pact

```

#### Stocker le pacte

Notre pacte est un fichier JSON que nous allons commiter directement dans le dépôt du front end, après avoir exécuté les tests localement. J'ai trouvé que cela tend à bien fonctionner. Faire en sorte que le pipeline lui-même commite le pacte dans `git` ne semble pas nécessaire.

Nous en viendrons à étendre le pacte dans un second temps.

### Le côté fournisseur

À ce stade, nous avons un pacte fonctionnel, qui est vérifié par le consommateur. Mais ce n'est que la moitié de l'équation. Sans une vérification du côté du fournisseur, nous n'avons rien accompli. Peut-être même moins que cela, car nous pourrions avoir un faux sentiment de sécurité !

Pour ce faire, nous allons démarrer le back end en tant que serveur de développement et exécuter le pacte contre lui. Il existe un fournisseur `gradle` qui s'en charge. Nous devons le configurer et fournir un moyen de trouver le pacte (qui est stocké dans le dépôt du front end). Vous pouvez récupérer le pacte depuis Internet ou depuis un fichier local, selon ce qui est le plus pratique.

```groovy
buildscript {
    dependencies {
        classpath 'au.com.dius:pact-jvm-provider-gradle_2.12:3.6.14'
    }
}

apply plugin: 'au.com.dius.pact'

pact {
    serviceProviders {
        api {
            port = 4003

            hasPactWith('frontend') {
                pactSource = url('https://path-to-the-pact/frontend-backend.json')
                stateChangeUrl = url("http://localhost:$port/pact")
            }
        }
    }
}

```

Il reste à démarrer le serveur et à exécuter le pacte contre lui, ce que nous faisons avec un petit script :

```bash
goal_test-pact() {
  trap "stop_server" EXIT

  goal_build
  start_server

  ./gradlew pactVerify
}

start_server() {
  artifact=app.jar
  port=4003

  if lsof -i -P -n | grep LISTEN | grep :$port > /dev/null ; then
    echo "Port[${port}] is busy. Server won't be able to start"
    exit 1
  fi

  nohup java -Dspring.profiles.active=pact -jar ./build/libs/${artifact} >/dev/null 2>&1 &

  # Wait for server to answer requests
  until curl --output /dev/null --silent --fail http://localhost:$port/actuator/health; do
    printf '.'
    sleep 3
  done
}

stop_server() {
  pkill -f 'java -Dspring.profiles.active=pact -jar'
}

```

#### Fixtures

Si vous exécutez votre back end en mode développement, il devra fournir certaines données, afin que le contrat soit rempli. Même si nous n'utilisons pas de correspondance exacte, nous devons retourner quelque chose, sinon il ne sera pas possible de le vérifier.

Vous pouvez utiliser des mocks, mais j'ai trouvé qu'éviter autant que possible conduit à des résultats plus fiables. Votre application est plus proche de ce qui se passera en production. Quelles sont les autres options ? Souvenez-vous que lorsque nous définissions des interactions, nous avions un `state`. C'est l'indice pour le fournisseur. Une façon de l'utiliser est le `stateChangeUrl`. Nous pouvons fournir un contrôleur spécial pour initialiser notre back end en fonction du `state` :

```kotlin
private const val PATH = "/pact"

data class Pact(val state: String)

@RestController
@RequestMapping(PATH, consumes = [MediaType.APPLICATION_JSON_VALUE])
@ConditionalOnExpression("\${pact.enabled:true}")
class PactController(val repository: RecipeRepository) {
    @PostMapping
    fun setup(@RequestBody body: Pact): ResponseEntity<Map<String,String>> {
        when(body.state) {
            "i have a list of recipes" -> initialRecipes()
            else -> doNothing()
        }

        return ResponseEntity.ok(mapOf())
    }
}

```

Notez que ce contrôleur n'est actif que pour un profil spécifique et n'existera pas en dehors de celui-ci.

#### Intégration dans le pipeline

Comme pour le fournisseur, nous exécuterons la vérification dans le cadre de notre pipeline

```yaml
version: 2
jobs:
  build:

    working_directory: ~/app

    docker:
      - image: circleci/openjdk:8-jdk

    steps:

      - checkout
      - run: ./go linter-kt
      - run: ./go test-unit
      - run: ./go test-pact

```

Il y a une légère différence, cependant. Notre contrat est généré par le consommateur. Cela signifie qu'un changement dans le front end pourrait conduire à un pacte qui ne vérifie plus correctement, même si aucun code n'a été changé dans le back end. Donc, idéalement, un changement dans le pacte devrait déclencher le pipeline du back end également. Je n'ai pas trouvé de moyen de représenter cela élégamment dans _CircleCI_, contrairement à [ConcourseCI](https://concourse-ci.org/).

## Comment le contrat influence la relation entre le front end et le back end

C'est bien que nous ayons mis cela en place. [Ne touchez jamais à un système en marche](https://en.wiktionary.org/wiki/never_change_a_running_system), n'est-ce pas ? Eh bien, nous pourrions ! Après tout, le changement rapide est la raison pour laquelle nous investissons dans tous ces outils. Comment introduiriez-vous un changement qui nécessite d'étendre l'API ?

1. Nous commençons par le client. Nous voulons définir ce que le client obtiendra et qui n'est pas encore là. Comme nous l'avons appris, nous le faisons via un test dans le front end qui définit l'attente pour la nouvelle route, ou les nouveaux champs. Cela créera une nouvelle version du pacte.
2. Notez qu'à ce stade, le back end _ne_ remplit _pas_ le pacte. Un nouveau déploiement du back end échouera. Mais aussi, le back end _existant_ ne remplit pas non plus le pacte pour le moment. Le changement que vous avez introduit doit être rétrocompatible. Le front end ne doit pas non plus dépendre des changements.
3. Il est maintenant temps de remplir le nouveau pacte du côté du back end. Si cela prend beaucoup de temps, vous bloquerez votre processus de déploiement, ce qui n'est pas bon. Envisagez de faire des incréments plus petits dans ce cas. De toute façon, vous devez implémenter la nouvelle fonctionnalité. Le test de pacte vérifiera que votre changement est bien ce qui est attendu.
4. Maintenant que le back end fournit la nouvelle fonctionnalité, vous pouvez l'intégrer librement dans votre front end.

Ce flux peut sembler un peu maladroit au début. Il est vraiment important de travailler avec le plus petit quantum de fonctionnalité. Vous ne voulez pas bloquer votre processus de déploiement.

## Prochaines étapes

Pour l'intégration entre votre propre front end et back end, j'ai trouvé que cette configuration est suffisante en pratique. Cependant, à mesure que la complexité augmente, la gestion des versions deviendra importante. Vous voudrez aider plusieurs équipes à collaborer plus facilement. Pour cela, nous pouvons utiliser un [broker](https://docs.pact.io/pact_broker). Cela est beaucoup plus difficile à implémenter, donc vous devriez vous demander si vous en avez vraiment besoin. Ne corrigez pas les problèmes que vous n'avez pas encore.

## Conclusion

Pour résumer, voici la configuration à laquelle nous sommes arrivés :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/pipelines-full.png)

Pensez à tout le temps que vous avez passé à écrire des tests pour vérifier que votre back end envoie les bonnes données. C'est beaucoup plus pratique à faire avec un contrat. De plus, libérer le front end et le back end indépendamment signifie être plus rapide, libérer de plus petites parties de fonctionnalité. Cela peut sembler effrayant au début, mais vous réaliserez que vous êtes en fait beaucoup plus conscient de ce qui sort de cette manière.

Une fois que vous avez adopté cela pour un service, il n'y a aucune raison de ne pas le faire pour tous. Je ne regrette vraiment pas d'exécuter des suites de tests coûteuses de bout en bout juste pour vérifier que mon back end fonctionne. Voici le code que j'ai utilisé dans les exemples pour le [front end](https://github.com/sirech/cookery2-frontend) et le [back end](https://github.com/sirech/cookery2-backend). C'est une application complète (bien que petite) en cours d'exécution. Bonne chance avec vos contrats !