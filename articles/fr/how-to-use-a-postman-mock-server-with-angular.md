---
title: Comment utiliser un serveur de simulation Postman avec Angular
subtitle: ''
author: Brenda Chepkorir
co_authors: []
series: null
date: '2023-06-28T21:47:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-postman-mock-server-with-angular
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-christina-morillo-1181247.jpg
tags:
- name: Angular
  slug: angular
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser un serveur de simulation Postman avec Angular
seo_desc: "New front end features often require back end data support – especially\
  \ where new endpoints are concerned. \nFor example, an application that needs an\
  \ authenticated user experience may need a new /authenticate endpoint.\nIf for any\
  \ reason endpoint deve..."
---

Les nouvelles fonctionnalités front-end nécessitent souvent un support de données back-end, en particulier lorsqu'il s'agit de nouveaux endpoints.

Par exemple, une application nécessitant une expérience utilisateur authentifiée peut avoir besoin d'un nouvel endpoint `/authenticate`.

Si, pour une raison quelconque, le développement de l'endpoint est retardé ou en retard, malgré la planification du sprint, vous serez confronté à la question : _construisez-vous avec ou sans les données ?_

Heureusement, il existe une troisième option : construire avec des données simulées (ce qui pourrait fonctionner en fonction de votre cas d'utilisation). Cette option est particulièrement bénéfique lorsque la fonctionnalité est un must-have à la fin d'un sprint.

Certains autres avantages d'avoir des données simulées à portée de main incluent :

* Meilleure gestion des tests avec différentes données de réponse API
* Tests sécurisés avec des données dé-identifiées
* Données de test réutilisables
* Démonstrations plus fluides — au cas où le serveur réel déciderait d'être hors ligne

Il existe plusieurs outils qui peuvent aider à créer et à utiliser des données simulées, tels que [Postman](https://www.postman.com/) et ses [serveurs de simulation](https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock/). Vous pouvez également intégrer ces outils dans les applications front-end pour une utilisation en développement.

Un serveur de simulation Postman est simple à configurer et à intégrer avec une application Angular — particulièrement lorsqu'il est associé à un intercepteur Angular. Cela peut ne pas convenir à tous les cas d'utilisation, mais cela offre un moyen pratique de travailler avec des données simulées.

## Qu'est-ce qu'un serveur de simulation Postman ?

[Postman](https://www.postman.com/product/what-is-postman/) est une plateforme API collaborative conçue pour supporter le cycle de vie complet des APIs. Elle fournit des outils et des intégrations qui aident à la conception, la documentation, les tests, la surveillance, le partage et l'utilisation des APIs.

Un serveur de simulation Postman est un serveur API factice qui accepte les requêtes vers les endpoints que vous créez dans une [collection](https://learning.postman.com/docs/sending-requests/intro-to-collections/) et retourne les réponses que vous spécifiez dans des [exemples](https://learning.postman.com/docs/sending-requests/examples/). Il a sa propre [URL de base](https://www.techopedia.com/definition/4858/base-url) et une clé [API](https://www.techtarget.com/whatis/definition/API-key) optionnelle pour une sécurité supplémentaire.

Une collection Postman est un regroupement logique qui aide à organiser les requêtes liées, tandis qu'un exemple Postman est une instance d'une requête en action. Il est composé de la requête et d'une réponse attendue.

La [documentation Postman](https://learning.postman.com/docs/sending-requests/requests/) fournit des détails plus complets sur les collections et les exemples si vous souhaitez en savoir plus.

Une fois que vous avez décidé de travailler avec un serveur de simulation Postman, vous devez ensuite l'intégrer à l'application de manière à ne pas :

* Perturber le développement en cours
* Casser l'application

Deux méthodes populaires viennent à l'esprit :

1. Utiliser un [proxy](https://angular.io/guide/build#proxying-to-a-backend-server)
2. Utiliser un [HTTP Interceptor](https://angular.io/api/common/http/HttpInterceptor)

La principale différence entre ces deux options est que le proxy est appliqué au moment de la construction, tandis que l'intercepteur est appliqué à l'exécution.

### Qu'est-ce qu'un Proxy ?

Un [serveur proxy](https://www.techtarget.com/whatis/definition/proxy-server) est un outil logiciel qui agit souvent comme un intermédiaire entre un client et un serveur. Il reçoit les requêtes du client, les modifie et en redirige certaines vers d'autres serveurs.

Angular utilise le [dev-server de Webpack](https://webpack.js.org/configuration/dev-server/#devserverproxy) comme proxy. Il peut être configuré pour rediriger certaines requêtes vers un serveur différent, via l'[Angular CLI](https://angular.io/guide/build#proxying-to-a-backend-server). C'est ce qui en fait une solution viable à utiliser avec un serveur de simulation Postman en développement.

### Qu'est-ce qu'un Angular HTTP Interceptor ?

L'`HttpInterceptor` d'Angular est une classe légère qui peut intercepter une requête sortante ou une réponse entrante. Il peut être utilisé pour inspecter une requête ou transformer certaines de ses parties, comme l'URL ou les en-têtes. Si vous utilisez un intercepteur au lieu d'un proxy :

* Vous pouvez accéder aux variables d'environnement d'exécution pour déterminer si une requête doit être redirigée vers le serveur de simulation
* Vous n'aurez _pas_ besoin de relancer l'application après une modification de l'intercepteur — les modifications de code déclenchent des rechargements (si les rechargements en direct sont activés)

Le proxy et l'intercepteur peuvent essentiellement faire la même chose : intercepter et transformer les requêtes sortantes. Cependant, chaque option a ses propres avantages et inconvénients.

### Intercepteur vs Proxy

* Un intercepteur nécessitera relativement moins de configuration qu'un proxy
* Un proxy nécessitera la configuration de variables d'environnement au moment de la construction dans le système ou un fichier `.env` (un intercepteur peut en avoir besoin si une clé API est requise)
* Une modification du proxy nécessitera que l'application soit relancée, tandis qu'une modification de l'intercepteur déclenchera un rechargement
* Si vous n'êtes pas familier avec la configuration d'un proxy dans Angular, il y a une courbe d'apprentissage douce attendue. Cependant, il y a une courbe d'apprentissage encore plus douce lors de la création d'un intercepteur puisqu'il s'agit simplement d'une classe

L'utilisation d'un intercepteur semble être une option plus simple pour ce cas d'utilisation.

## Comment créer un serveur de simulation Postman

La première étape pour utiliser un serveur de simulation est d'en créer un. Tout d'abord, assurez-vous d'avoir un compte Postman et un [workspace](https://www.postman.com/product/workspaces/). Vous pouvez créer les deux depuis le [site web de la plateforme](https://www.postman.com/). Un workspace Postman est comme un tableau de bord qui organise votre travail, vos outils et vos collaborateurs.

Ensuite, créez une collection Postman pour regrouper et organiser les requêtes que vous souhaitez que le serveur de simulation gère.

Ajoutez ensuite une requête à la collection. Elle peut être de n'importe quel type de requête [CRUDL](https://developer.mozilla.org/en-US/docs/Glossary/CRUD). Utilisez l'URL de votre serveur réel — comme vous le feriez lors du test d'un endpoint réel.

Voici un aperçu d'un workspace avec une collection et une requête GET :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/create-and-send-req.png)
_Une collection avec une requête_

Ensuite, testez votre endpoint en envoyant la requête. Faites cela jusqu'à obtenir une réponse réussie, puis enregistrez la réponse comme un exemple Postman. Vous pouvez mettre à jour l'exemple en supprimant toutes les données sensibles comme les informations utilisateur ou les PII.

Voici un aperçu d'un exemple mis à jour. Certaines informations utilisateur ont été remplacées par des données simulées en utilisant des variables Postman.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/add-example.png)
_Un exemple mis à jour pour une requête_

Enfin, créez un serveur de simulation Postman à partir de la collection que vous venez de créer. Vous pouvez le faire en cliquant sur les points de suspension à côté de la collection et en sélectionnant `Mock collection` (au moins, au moment de la rédaction de cet article). Voici un aperçu de ces étapes.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/mock-collection.png)
_Comment créer un serveur de simulation à partir d'une collection_

Vous serez présenté avec un formulaire simple qui vous permettra de configurer le serveur de simulation.

Par exemple, vous pouvez renommer le serveur de simulation ou le rendre privé — cela signifie qu'il aura besoin d'une clé API.

Une fois le serveur de simulation configuré, cliquez sur `Create Mock Server`. Vous recevrez alors une URL pour le serveur. Copiez l'URL.

Pour associer le serveur de simulation à vos requêtes et exemples, allez dans la collection et mettez à jour les URLs. Remplacez les URLs de base des requêtes et exemples par l'URL de base du serveur de simulation copié. Envoyez quelques requêtes dans Postman pour vérifier que votre configuration a été réussie.

**Note :**

* Si votre API est privée, vous pouvez générer une clé API à partir des paramètres de votre compte
* Votre serveur de simulation conserve un journal des requêtes qu'il reçoit, que vous pouvez consulter dans votre workspace

Après avoir créé le serveur de simulation, créez l'intercepteur dans votre application Angular.

Pour plus d'informations, vous pouvez vous référer à la [documentation](https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock/#creating-mock-servers).

### Comment créer un Angular HTTP Interceptor

Un intercepteur est une classe injectable qui implémente l'interface `HttpInterceptor` d'Angular.

Cette interface a une méthode requise — la méthode `intercept`. Cette méthode fait principalement une chose : elle prend des arguments de requête et de gestionnaire et transmet la requête à la méthode `next` du gestionnaire. Les requêtes peuvent être modifiées avant d'être transmises au gestionnaire.

```typescript
@Injectable()
export class ApiInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<unknown>, next: HttpHandler):
    Observable<HttpEvent<unknown>>
  {
    return next.handle(req);
  }
}
```

Pour utiliser un intercepteur créé dans l'application, ajoutez-le au tableau `providers` au même niveau où le `HttpClientModule` est importé :

```typescript
[{ provide: HTTP_INTERCEPTORS, useClass: ApiInterceptor, multi: true }]
```

Cela permet à l'intercepteur d'être géré par le système d'injection de dépendances d'Angular en tant que dépendances optionnelles du service `HttpClient`. Le service `HttpClient` est utilisé pour effectuer des requêtes HTTP.

Notez que lorsqu'il s'agit d'utiliser des intercepteurs, l'ordre est important.

Par exemple, si vous fournissez un autre intercepteur qui ajoute des en-têtes d'authentification après un intercepteur API qui ajoute un en-tête de clé API, la requête peut envoyer des en-têtes inutiles au serveur de simulation.

Enfin, intégrez le serveur de simulation avec votre application.

Pour plus d'informations, consultez la [documentation](https://angular.io/guide/http-intercept-requests-and-responses).

### Comment utiliser un Angular Http Interceptor avec un serveur de simulation Postman

Tout d'abord, spécifiez une variable d'environnement pour basculer entre les données simulées et les données réelles. Les variables d'environnement dans Angular sont principalement définies comme des variables TypeScript dans des fichiers d'environnement :

```typescript
// fichier environment.ts

export const environment = {
  production: false,
  useMock: true,
  postman: {
    baseUrl: "postman-mock-server-url",
    apiKey: "optional-mock-server-api-key"
  }
};
```

Au moins pour les versions du framework <15.

Ensuite, utilisez la variable d'environnement dans l'intercepteur. Où vous pouvez cloner une requête sortante et mettre à jour son URL avant de la transmettre au gestionnaire :

```typescript
@Injectable()
export class ApiInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<unknown>, next: HttpHandler):
    Observable<HttpEvent<unknown>>
  {
    if (environment.useMock) {
      // en-têtes optionnels
      const headers = new HttpHeaders({
        "x-api-key": "my-api-key"
      });
      const cloneReq = req.clone({ url: this.getUpdatedURL(req.url), headers });
      return next.handle(cloneReq);
    }
    return next.handle(req);
  }
}
```

## Conclusion

En résumé, l'utilisation de données simulées dans les applications, en particulier celles qui sont intensives en données, peut être fastidieuse. Mais elles ont leurs mérites.

Les données simulées réutilisables aident à rendre les tests meilleurs et plus sécurisés, en particulier si les données sont variées et dé-identifiées. De plus, elles aident à faire progresser le développement lorsque les données réelles ne sont pas disponibles.

Il existe plusieurs outils qui aident à créer et à gérer des données simulées via des serveurs de simulation, comme Postman.

Ces outils ne sont pas seulement pratiques pour les ingénieurs logiciels API et back-end, mais aussi pour les ingénieurs logiciels front-end.