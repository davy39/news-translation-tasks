---
title: Comment automatiser les tests de bout en bout des API REST dans un environnement
  CI avec Postman et Newman
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-19T16:03:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-rest-api-end-to-end-tests
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0c6740569d1a4ca4aaf.jpg
tags:
- name: REST API
  slug: rest-api
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Comment automatiser les tests de bout en bout des API REST dans un environnement
  CI avec Postman et Newman
seo_desc: "By Mario Fernandez\nPostman is a great tool to explore REST APIs. You can\
  \ build requests and try them out to get quick feedback. Then you can persist them\
  \ as collections to make sure that the knowledge doesn't get lost. \nNewman, the\
  \ CLI version of Pos..."
---

Par Mario Fernandez

[Postman](https://learning.getpostman.com/) est un excellent outil pour explorer les API REST. Vous pouvez construire des requêtes et les essayer pour obtenir un retour rapide. Ensuite, vous pouvez les sauvegarder sous forme de collections pour vous assurer que les connaissances ne se perdent pas. 

[Newman](https://github.com/postmanlabs/newman), la version CLI de Postman, vous permet de passer au niveau supérieur et de transformer une collection en une suite de tests automatisés de bout en bout. Cette suite s'exécutera ensuite dans votre outil CI de choix. Dans cet article, je vais explorer les avantages de le faire et vous montrer comment le configurer.

![intro](https://www.freecodecamp.org/news/content/images/2019/08/IMG_4555.jpg)

## Qu'est-ce qu'un test de bout en bout dans le contexte d'une API ?

La nomenclature des tests est une chose délicate. En gardant à l'esprit la [pyramide des tests](https://martinfowler.com/bliki/TestPyramid.html), nous pouvons les imaginer comme des tests de très haut niveau. Ces tests confirment qu'une API REST particulière fonctionne comme prévu, en traitant les internes comme une boîte noire. Nous n'impliquons aucune UI dans le processus, ce qui aide à réduire la fragilité.

![poke-e2e](https://www.freecodecamp.org/news/content/images/2019/08/poke-e2e.png)
*par geek & poke / <a href="https://creativecommons.org/licenses/by/3.0/">CC BY</a>*

Les tests fragiles sont extrêmement ennuyeux, comme tout développeur l'a expérimenté à un moment donné. Au lieu de nous cogner la tête contre le mur en essayant de fixer l'infaisable, nous pouvons atténuer le problème en utilisant des tests de niveau inférieur.

## Pourquoi devrais-je avoir ces tests ?

Il y a deux scénarios différents que je souhaite couvrir :

Le premier est le test de vos propres API REST. Ces tests ajoutent une couche supplémentaire de confiance. Bien sûr, vous utilisez un mélange sain de différents tests (unitaires, d'intégration, fonctionnels, …). Les tests de bout en bout peuvent être la confirmation finale que tout semble correct.

Le deuxième cas est le test des API que vous ne contrôlez pas. Dans mes derniers projets, la plupart des données que nous consommons provenaient d'API servies par d'autres équipes. Plus d'une fois, j'ai passé une demi-journée à déboguer une erreur dans mon application, pour me rendre compte qu'une API en aval était défectueuse depuis le début. Les tests automatisés couvrent cette intégration et aident à isoler les problèmes.

### Documentation vivante

Une collection de tests qui sont exécutés régulièrement sert de meilleure documentation pour une API. Avez-vous recherché quelque chose dans un wiki d'entreprise récemment ? Si vous trouvez quoi que ce soit, vous devriez être heureux. Cela sera probablement incomplet. Ou tout simplement faux. Des moments amusants.

### Surveillance

Dans les deux cas, ces tests peuvent passer d'une passerelle dans le processus de construction à un outil de surveillance actif. En les exécutant constamment, vous vous assurez que l'API se comporte toujours comme vous l'attendez. Sinon, les bonnes alarmes seront déclenchées. Vous ne voulez pas réaliser que quelque chose ne va pas seulement lorsqu'un client se plaint.

### Pourquoi ne pas utiliser des tests de contrat pilotés par le consommateur à la place ?

Excellente question, si je puis me permettre. Les [CDCs](https://www.thoughtworks.com/de/radar/techniques/consumer-driven-contract-testing) sont un excellent moyen de s'assurer qu'une API est conforme à ce qu'un client attend d'elle. Si vous pouvez les configurer correctement, ils remplaceront presque complètement les tests de bout en bout. Souvenez-vous, continuez à pousser les tests à un niveau inférieur chaque fois que vous le pouvez.

Ils ne fonctionnent pas dans toutes les situations, cependant. Si vous ne contrôlez pas à la fois le fournisseur et le consommateur, vous devez dépendre d'une autre partie. Si ils ne remplissent pas leur partie du contrat, les tests seront inutiles. Certaines équipes ne sont tout simplement pas en position d'exécuter continuellement des tests contre un contrat. Exécuter vos propres tests pourrait être votre meilleur pari.

Quoi qu'il en soit, après avoir exposé la raison, il est temps pour un peu de **code**.

## Créer une collection Postman

### La collection

Nous définissons un certain nombre d'appels qui seront exécutés séquentiellement dans notre CI. Chaque appel exécute une requête contre l'API. Ensuite, il exécute quelques tests pour vérifier que la requête a réussi, en vérifiant le code de statut et le corps également.

Pour créer la collection, j'ai tendance à utiliser l'application Postman. J'aime extraire des éléments comme les URLs et les paramètres vers un [environnement](https://learning.getpostman.com/docs/postman/environments_and_globals/manage_environments/). Ensuite, la configuration devient plus facile, et vous n'avez aucune information sensible dans la collection elle-même. Votre historique est un [endroit pratique pour commencer à construire cette collection](https://learning.getpostman.com/docs/postman/collections/creating_collections/#saving-to-a-collection-from-history).

Une fois que vous êtes satisfait de la collection, vous pouvez l'exporter sous forme de fichier JSON. Ce fichier peut être validé dans le contrôle de source pour servir de base au pipeline qui exécutera les tests. Il existe une version Pro et Enterprise qui aide à gérer les collections, que je n'ai pas vraiment essayée. Cependant, un bon vieux dépôt `git` est plus que suffisant pour commencer.

![export-postman](https://www.freecodecamp.org/news/content/images/2019/08/export-postman.png)

### Exécuter la collection

Jusqu'à présent, nous avons utilisé Postman régulier et rien d'autre. Maintenant, c'est le moment pour Newman de briller. De quoi je parle, au fait ? Je vais citer directement la [documentation officielle](https://learning.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman/) :

> Newman est un exécuteur de collection en ligne de commande pour Postman. Il vous permet d'exécuter et de tester une collection Postman directement depuis la ligne de commande.

Bien que nous ayons clarifié cela ! Il est installé en tant que package npm, ce qui peut aboutir à un `package.json` aussi simple que celui-ci :

```json
{
  "name": "postman-utils",
  "version": "0.0.1",
  "private": true,
  "description": "Utilitaires Postman",
  "scripts": {
    "newman": "node_modules/.bin/newman run"
  },
  "dependencies": {
    "newman": "^4.4.1"
  }
}
```

comme mentionné précédemment, vous ne voulez pas coder en dur des variables comme les URLs, les paramètres ou, Dieu nous en préserve, les mots de passe dans cette collection. Ce n'est pas flexible, et ce n'est pas sûr. Au lieu de cela, j'aime utiliser un fichier de configuration qui inclut toutes ces valeurs. Mais si nous voulons valider ce fichier, nous devons encore trouver un moyen d'éviter d'y mettre des secrets. Je l'utilise comme un modèle et remplace les valeurs à l'exécution avec envsubst. Le fichier de configuration ressemble à ceci :

```
{
	"id": "425cf4df-d994-4d91-9efb-41eba1ead456",
	"name": "echo",
	"values": [
		{
			"key": "host",
			"value": "${HOST}",
			"enabled": true
		}
	]
}
```

Vous pouvez orchestrer cela avec un simple script bash. Le script injecte les variables dans le modèle, exécute newman, et supprime les fichiers pour éviter les fuites. Cela fonctionne très bien avec [gopass](https://hceris.com/storing-passwords-with-gopass/), où vous pouvez stocker vos secrets en toute sécurité et les récupérer via le script.

```shell
setup-newman() {
  settings=/tmp/settings.json.$$
  result=/tmp/variables.json.$$

  # shellcheck disable=SC2064
  trap "rm -f \"$settings\" \"$result\"" EXIT
}

run-newman() {
  local service=${1?Vous devez fournir le service à vérifier}

  envsubst < "$service.environment.json.template" > "$settings"

  npx newman run "$service.json" \
      -e "${settings}" \
      --export-environment "${result}"
}
```

cet assistant peut être appelé avec la collection que vous souhaitez tester. Les variables exportées seront récupérées par `envsubst`. [npx](https://www.npmjs.com/package/npx) nous donne un peu plus de flexibilité pour trouver le binaire `newman`, au cas où vous ne voulez pas utiliser un `package.json` mais l'avoir installé globalement.

```shell
goal_check-service() {
  setup

  export SERVICE_PASSWORD=${SERVICE_PASSWORD:-$(gopass store/service/password)}

  run_newman service
}
```

### Tests

Faire une requête n'est que la première étape. Souvenez-vous, nous visons à construire une suite de tests. Nous avons un onglet de test pratique dans Postman que nous pouvons utiliser pour écrire nos tests.

![test-tab](https://www.freecodecamp.org/news/content/images/2019/08/test-tab.png)

Nos tests sont écrits en _JavaScript_, en utilisant [Chai](https://www.chaijs.com/api/bdd/). Supposons que je veux tester que mon appel a livré une liste de résultats, je pourrais le faire comme ceci :

```javascript
var getResults = function() {
    var jsonData = pm.response.json();
    return jsonData['results'];
};

pm.test("La requête a réussi", function () {
    pm.response.to.have.status(200);
});

pm.test("Il y a des résultats", function () {
    pm.expect(getResults().length).to.be.above(0);
});
```

Plus de détails peuvent être trouvés [ici](https://blog.getpostman.com/2017/10/25/writing-tests-in-postman/)

### Construire des flux

Tous les appels dans une collection sont exécutés séquentiellement. Cela nous offre l'opportunité de tester des flux entiers au lieu de simples appels individuels. Un tel flux pour une ressource `/posts` est :

- Obtenir une liste de tous les `posts`
- Récupérer le premier `post` de la liste
- Mettre à jour le `post`

Nous allons construire une suite de tests paramétrés qui continueront à fonctionner dans le temps, pas seulement la première fois que vous l'avez exécutée. Une partie importante de cela est de modifier l'environnement dans une requête. C'est notre moyen de transmettre des paramètres entre les requêtes. Supposons que notre première requête a réussi, comme le confirment nos tests. Ensuite, nous stockons l'id dans une variable qui sera utilisée pour récupérer une entité particulière.

```javascript
// Premier résultat dans la liste
var post = getResults()[0];

// Passer des variables à d'autres étapes
pm.environment.set("id", post.id)
```

La prochaine requête peut utiliser ce paramètre comme n'importe quel autre que nous avons défini manuellement.

#### Ignorer les appels en fonction d'une condition

Les flux peuvent également nécessiter une logique pour ignorer certaines requêtes. Supposons que vous avez une requête qui crée une nouvelle entité via un `POST`. Vous voulez avoir cette requête, mais vous ne voulez peut-être pas l'exécuter à chaque commit. Peut-être que vous voulez le faire une fois par jour. Dans ce cas, nous allons ignorer le test en fonction d'une certaine variable.

```javascript
// Ne pas exécuter la requête de création dans la séquence, sauf si executeCreate est défini sur true
if(!pm.environment.get("executeCreate")) {
    postman.setNextRequest('Get other posts')
}
```

La variable va dans le fichier de configuration et est définie comme une variable d'environnement qui est injectée via notre script, comme je l'ai montré ci-dessus.

## Il est temps pour une intégration continue

À ce stade, vous devriez avoir une collection qui s'exécute localement. Exécuter cela une fois est bien, mais pourquoi ne pas l'exécuter pour chaque commit ? Ou peut-être toutes les heures, si vous voulez vérifier une API que vous ne contrôlez pas ? 

Votre pipeline CI est un endroit parfait pour faire cela. Je vais utiliser [CircleCI](https://circleci.com) pour mon exemple, mais n'importe quel CI fera l'affaire. J'exécute les tests à l'intérieur d'une [image docker](https://cloud.docker.com/repository/docker/sirech/newman-executor) que j'ai construite et qui inclut toutes les dépendances requises. Il existe une image Docker officielle fournie par Postman. Cependant, elle ne contient pas `envsubst` et utilise une version plus ancienne de _NodeJS_.

Le script d'assistance que nous avons construit dans l'étape précédente fonctionnera sans aucun changement à l'intérieur de CircleCI. Nous devons simplement fournir les secrets requis [en tant que variables](https://circleci.com/docs/2.0/env-vars/). Voici le travail :

```yaml
  healthcheck:

    docker:
      - image: sirech/newman-executor:12.6

    steps:
      - checkout
      - run: ./go test-e2e
```
    
qui produira un rapport similaire à celui-ci :

![output](https://www.freecodecamp.org/news/content/images/2019/08/output.png)

### Qu'en est-il des alternatives ?

De nombreux frameworks fournissent leur propre moyen d'exécuter des tests contre une API en cours d'exécution. Dans [Spring Boot](https://spring.io/projects/spring-boot), par exemple, vous pouvez utiliser [MockMvc](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/test/web/servlet/MockMvc.html) pour tester les contrôleurs. Vous pouvez utiliser les deux, à mon avis. D'abord les tests natifs, pour ainsi dire, puis superposer les tests Postman par-dessus.

Et n'oublions pas le bon vieux [curl](https://curl.haxx.se). J'avais une énorme collection de commandes curl avec lesquelles je testais une API qui était nécessaire pour mon dernier projet. Cependant, la gestion de cela devient de plus en plus fastidieuse avec le temps. Si vous voulez envoyer des requêtes complexes, comme des certificats ou des cookies, Postman est bien plus pratique à utiliser. De plus, vous pouvez utiliser JavaScript au lieu de bash, ce qui peut rendre les choses un peu plus faciles à lire et à maintenir.

## Qu'y a-t-il d'autre ?

Cela représente déjà beaucoup et ce n'est que le début. Tout ce que vous faites avec une API, vous pouvez également l'automatiser. Par exemple, dans mon projet précédent, nous avions une collection qui exécutait un [flux OAuth](https://auth0.com/docs/api-auth/which-oauth-flow-to-use). Cela nous a obtenu un jeton que nous pouvions utiliser pour faire des requêtes contre un endpoint autorisé.

## Un dépôt à utiliser comme exemple

[Voici](https://github.com/sirech/echo/blob/master/echo.json) un dépôt pour une application Kotlin qui exécute une collection Postman en tant que test de bout en bout. Il peut servir de kit de démarrage pour commencer avec des tests API de bout en bout de haute qualité.