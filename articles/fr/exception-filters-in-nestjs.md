---
title: Comment utiliser les filtres d'exception pour capturer les bugs dans Nest.js
subtitle: ''
author: Okoye Chukwuebuka Victor
co_authors: []
series: null
date: '2023-06-23T21:38:23.000Z'
originalURL: https://freecodecamp.org/news/exception-filters-in-nestjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/brett-jordan-XWar9MbNGUY-unsplash.jpg
tags:
- name: debugging
  slug: debugging
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
- name: nestjs
  slug: nestjs
seo_title: Comment utiliser les filtres d'exception pour capturer les bugs dans Nest.js
seo_desc: "It's common to find errors and bugs in your code if you're a software developer.\
  \ They might occur because of incorrect input, from passing the wrong data types,\
  \ or because of delays or response timeouts. \nAnd even though errors and bugs are\
  \ a part of..."
---

Il est courant de trouver des erreurs et des bugs dans votre code si vous êtes un développeur logiciel. Ils peuvent survenir en raison d'une entrée incorrecte, du passage de mauvais types de données, ou en raison de retards ou de délais d'attente de réponse. 

Et même si les erreurs et les bugs font partie de la vie, ils peuvent vous stresser et diminuer votre productivité. Heureusement, vous pouvez limiter le nombre de nuisances dans votre code en prenant des mesures proactives pour les prévenir et les corriger. 

Dans cet article, vous apprendrez comment utiliser au mieux les filtres d'exception pour limiter les perturbations dans vos implémentations de code.

## Qu'est-ce que les filtres d'exception ?

Les filtres d'exception sont des constructions d'un langage de programmation qui vous aident à gérer les exceptions ou les erreurs trouvées dans les services ou les classes de contrôleur. L'utilisation de ces filtres améliore l'efficacité de votre base de code et rend les erreurs plus traçables, ce qui vous aide à les résoudre.

### Qu'est-ce que les filtres d'exception dans Nest.js ?

Nest.js dispose d'une interface de filtre d'exception intégrée que vous importez depuis le package `@nestjs/common`. Cette interface vous donne des informations précises sur les exceptions que vous pouvez rencontrer afin que vous sachiez comment les corriger. 

Certains filtres d'exception intégrés incluent `NotFoundException`, `UnauthorizedException`, et `RequestTimeOutException`, parmi d'autres.

## Comment créer un filtre d'exception personnalisé

Pour créer une classe de filtre d'exception personnalisée, vous la définissez avec un décorateur `@Catch` qui prend le type d'exception que le filtre doit capturer. Cette classe implémente ensuite l'interface `ExceptionFilter`. De cette manière, vous aurez accès à la méthode `catch` que l'interface fournit. 

NestJS vous permet de créer vos propres filtres d'exception afin que vous puissiez définir quel type d'informations il doit retourner.

```typescript
@Catch(HttpException)
export class TestExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();
    const status = exception.getStatus();

    response
      .status(status)
      .json({
        statusCode: status,
        timestamp: new Date().toISOString(),
        path: request.url,
      });
  }
}
```

Comme vous pouvez le voir ci-dessus, la méthode catch prend deux arguments en entrée : `exception:HttpException` et `host:argumentsHost`. 

`HttpException` est l'exception lancée lorsqu'une requête `HTTP` échoue et retourne le message d'erreur approprié avec un code de statut en réponse au client. 

Le paramètre `argumentsHost` fournit des informations sur le cycle de requête et de réponse actuel. Ici, le code extrait les objets Response et Request de l'objet `ArgumentsHost` en utilisant la méthode `switchToHttp`. Il appelle ensuite la méthode `getStatus` de l'objet `HttpException` afin de récupérer le code de statut `HTTP` de l'erreur.

Un objet `JSON` est retourné. Il contient le code de statut, le timestamp de l'erreur et l'URL de la requête, définissant le code de statut de la réponse `HTTP` pour qu'il soit le code de statut de l'erreur.

Une autre chose passionnante à noter est que vous pouvez modifier le code de statut et le message d'erreur des filtres d'exception existants comme `NotFoundException` afin qu'ils affichent votre propre message d'erreur personnalisé et code de statut. Voici une illustration ci-dessous :

```typescript
export class NotFoundException extends HttpException {
  constructor(message: string) {
    super(message || 'Not Found', HttpStatus.NOT_FOUND);
  }
}
```

L'exemple ci-dessus montre que la classe `NotFoundException` a été modifiée pour accepter un paramètre `message` dans la méthode constructeur ou donner une valeur par défaut de 'Not Found'. 

En faisant cela, vous êtes maintenant en mesure de personnaliser un message d'erreur pour votre classe `NotFoundException` et retourner un code de statut `404`.

## Comment lier les filtres d'exception dans Nest.js

Vous vous demandez peut-être comment vous pouvez implémenter l'exception personnalisée ou modifiée que vous avez créée pour votre application. Eh bien, vous utilisez quelque chose appelé **liaison**. 

Il existe plusieurs façons de lier les filtres d'exception à votre application. Voici trois façons principales de le faire :

1. Portée globale
2. Portée du contrôleur
3. Portée de la méthode

### **Liaison utilisant la portée globale**

Comme le nom "Global" l'implique, il couvre l'intégralité d'une chose – dans ce cas, l'application. Le filtre d'exception personnalisé est **lié** à l'intégralité de votre application web en utilisant la fonction `useGlobalFilters()`. Une instance de votre filtre d'exception personnalisé est passée avant le démarrage du serveur. 

Voici un exemple de ce à quoi cela ressemble :

```typescript
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalFilters(new TestExceptionFilter());
  await app.listen(3000);
}
bootstrap();
```

Si vous liez le filtre d'exception à la portée globale, cela signifie que toute exception de type `HttpException` lancée depuis n'importe quel contrôleur ou méthode au sein de l'application sera gérée par le `TestExceptionFilter`.

### **Liaison utilisant la portée du contrôleur**

Si vous souhaitez gérer une exception qui couvre non seulement les méthodes spécifiques de votre application, mais également l'intégralité du contrôleur avec les méthodes qu'il contient, vous pouvez utiliser `@UseFilters` pour lier l'exception personnalisée au contrôleur. Consultez l'exemple ci-dessous :

```typescript
@UseFilters(TestExceptionFilter)
@Controller('users')
export class UsersController {
  @Get()
  async findUsers() {
    // ...
  }
}
```

Dans cet exemple, le filtre d'exception personnalisé est lié au contrôleur en le plaçant avant le décorateur `@Controller`. De cette manière, il gère toute erreur provenant des routes de ce contrôleur.

### **Liaison utilisant la portée de la méthode**

Dans cette forme de liaison, vous utilisez le décorateur `@UseFilters` pour appliquer le Custom ExceptionFilter que vous avez défini à une méthode dans votre application. Voici un exemple :

```typescript
@Controller()
export class UsersController {
  @Get()
  @UseFilters(TestExceptionFilter)
  async findUsers() {
    // ...
  }
}
```

Dans cet exemple, vous utilisez le décorateur `@UseFilters` pour lier le filtre d'exception `TestExceptionFilter` à la méthode `findUsers`. Cela signifie que si une exception se produit dans la méthode `findUsers()`, le `TestExceptionFilter` la capturera et la gérera.

## Débogage facilité

Dans ce tutoriel, vous avez appris les filtres d'exception dans Nest.js, et comment créer des filtres d'exception personnalisés. Vous avez également vu différentes façons de les implémenter dans vos applications.

Toutes les méthodes discutées sont de bonnes façons de gérer les exceptions. En implémentant ces techniques, vous pouvez assurer une performance plus fluide de l'application et offrir une meilleure expérience utilisateur.

Si vous avez aimé lire cet article, vous pouvez le partager et me suivre sur [Twitter](https://twitter.com/okoyevictorr) et [Linkedin](https://www.linkedin.com/in/officalrajdeepsingh/).