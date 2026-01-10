---
title: Comment écrire des tests unitaires et des tests E2E pour les applications NestJS
subtitle: ''
author: Gordan Tan
co_authors: []
series: null
date: '2025-04-16T14:40:41.801Z'
originalURL: https://freecodecamp.org/news/nestjs-unit-testing-e2e-testing-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744738441654/1bb2b329-d363-46d7-b091-e0e95ad22c9e.png
tags:
- name: nestjs
  slug: nestjs
- name: Testing
  slug: testing
- name: backend
  slug: backend
- name: Node.js
  slug: nodejs
- name: E2ETesting
  slug: e2etesting
- name: JavaScript
  slug: javascript
seo_title: Comment écrire des tests unitaires et des tests E2E pour les applications
  NestJS
seo_desc: 'Recently, I have been writing unit tests and E2E tests for a NestJS project.
  This was my first time writing tests for a backend project, and I found the process
  different from my experience with frontend testing, making it challenging to begin.

  After...'
---

Récemment, j'ai écrit des tests unitaires et des tests E2E pour un projet NestJS. C'était ma première fois à écrire des tests pour un projet backend, et j'ai trouvé le processus différent de mon expérience avec les tests frontend, ce qui a rendu le début difficile.

Après avoir examiné quelques exemples, j'ai acquis une compréhension plus claire de la manière d'aborder les tests. J'ai donc écrit un article pour enregistrer et partager mon apprentissage afin d'aider les autres qui pourraient être confrontés à une confusion similaire.

En outre, j'ai rassemblé un projet de démonstration avec les tests unitaires et E2E pertinents complétés, ce qui pourrait être intéressant. J'ai [téléversé le code sur Github ici](https://github.com/woai3c/nestjs-demo).

## Table des matières

1. [Prérequis](#heading-prerequisites)
    
2. [Différence entre les tests unitaires et les tests E2E](#heading-difference-between-unit-testing-and-e2e-testing)
    
3. [Écrire des tests unitaires](#heading-writing-unit-tests)
    
    * [Le premier cas de test](#heading-the-first-test-case)
        
    * [Le deuxième cas de test](#heading-the-second-test-case)
        
    * [Couverture des tests unitaires](#heading-unit-test-coverage)
        
4. [Écrire des tests E2E](#heading-writing-e2e-tests)
    
5. [Faut-il écrire des tests](#heading-whether-to-write-tests)
    
    * [Améliorer la robustesse du système](#heading-enhancing-system-robustness)
        
    * [Améliorer la maintenabilité](#heading-enhancing-maintainability)
        
    * [Améliorer l'efficacité du développement](#heading-enhancing-development-efficiency)
        
6. [Quand ne pas écrire de tests](#heading-when-not-to-write-tests)
    
7. [Conclusion](#heading-conclusion)
    
8. [Matériel de référence](#heading-reference-materials)
    

## Prérequis

Avant de plonger dans ce tutoriel, vous devriez avoir :

* Des connaissances de base en TypeScript et Node.js
    
* Une familiarité avec les fondamentaux de NestJS
    
* Une compréhension des API RESTful
    
* MongoDB installé (car l'exemple utilise MongoDB)
    
* Node.js et npm/yarn installés sur votre système
    
* Une compréhension de base des concepts de test
    

Vous pouvez trouver les exemples de code complets dans le [dépôt de démonstration](https://github.com/woai3c/nestjs-demo). Vous pouvez le cloner pour suivre les exemples.

## Différence entre les tests unitaires et les tests E2E

Les tests unitaires et les tests E2E sont des méthodes de test de logiciels, mais ils ont des objectifs et des portées différents.

Les tests unitaires consistent à vérifier et à valider la plus petite unité testable au sein du logiciel. Une fonction ou une méthode, par exemple, peut être considérée comme une unité. Dans les tests unitaires, vous fournissez des sorties attendues pour diverses entrées d'une fonction et validez la justesse de son fonctionnement. Le but des tests unitaires est d'identifier rapidement les bugs au sein de la fonction, et ils sont faciles à écrire et à exécuter rapidement.

D'autre part, les tests E2E simulent souvent des scénarios utilisateurs réels pour tester l'ensemble de l'application. Par exemple, le frontend utilise généralement un navigateur ou un navigateur sans tête pour les tests, tandis que le backend le fait en simulant des appels d'API.

Dans un projet NestJS, les tests unitaires pourraient évaluer un service spécifique ou une méthode d'un contrôleur, comme vérifier si la méthode `update` dans le module Users met correctement à jour un utilisateur. Un test E2E, cependant, pourrait examiner un parcours utilisateur complet, de la création d'un nouvel utilisateur à la mise à jour de son mot de passe et finalement à la suppression de l'utilisateur, ce qui implique plusieurs services et contrôleurs.

## Comment écrire des tests unitaires

Écrire des tests unitaires pour une fonction utilitaire ou une méthode qui n'implique pas d'interfaces est relativement simple. Vous devez simplement considérer les différentes entrées et écrire le code de test correspondant. Mais la situation devient plus complexe une fois que les interfaces entrent en jeu. Utilisons le code comme exemple :

```typescript
async validateUser(
  username: string,
  password: string,
): Promise<UserAccountDto> {
  const entity = await this.usersService.findOne({ username });
  if (!entity) {
    throw new UnauthorizedException('User not found');
  }
  if (entity.lockUntil && entity.lockUntil > Date.now()) {
    const diffInSeconds = Math.round((entity.lockUntil - Date.now()) / 1000);
    let message = `The account is locked. Please try again in ${diffInSeconds} seconds.`;
    if (diffInSeconds > 60) {
      const diffInMinutes = Math.round(diffInSeconds / 60);
      message = `The account is locked. Please try again in ${diffInMinutes} minutes.`;
    }
    throw new UnauthorizedException(message);
  }
  const passwordMatch = bcrypt.compareSync(password, entity.password);
  if (!passwordMatch) {
    // $inc update to increase failedLoginAttempts
    const update = {
      $inc: { failedLoginAttempts: 1 },
    };
    // lock account when the third try is failed
    if (entity.failedLoginAttempts + 1 >= 3) {
      // $set update to lock the account for 5 minutes
      update['$set'] = { lockUntil: Date.now() + 5 * 60 * 1000 };
    }
    await this.usersService.update(entity._id, update);
    throw new UnauthorizedException('Invalid password');
  }
  // if validation is sucessful, then reset failedLoginAttempts and lockUntil
  if (
    entity.failedLoginAttempts > 0 ||
    (entity.lockUntil && entity.lockUntil > Date.now())
  ) {
    await this.usersService.update(entity._id, {
      $set: { failedLoginAttempts: 0, lockUntil: null },
    });
  }
  return { userId: entity._id, username } as UserAccountDto;
}
```

Le code ci-dessus est une méthode `validateUser` dans le fichier `auth.service.ts`, principalement utilisée pour vérifier si le nom d'utilisateur et le mot de passe saisis par l'utilisateur lors de la connexion sont corrects. Il contient la logique suivante :

1. Vérifier si l'utilisateur existe en fonction du `username`. Si ce n'est pas le cas, lever une exception 401 (une exception 404 est également envisageable).
    
2. Voir si l'utilisateur est verrouillé. Si c'est le cas, lever une exception 401 avec un message pertinent.
    
3. Crypter le `password` et le comparer avec le mot de passe dans la base de données. S'il est incorrect, lever une exception 401 (trois tentatives de connexion échouées consécutives verrouilleront le compte pendant 5 minutes).
    
4. Si la connexion est réussie, effacer tout compteur de tentatives de connexion échouées précédentes (le cas échéant) et retourner l'`id` et le `username` de l'utilisateur à l'étape suivante.
    

Comme vous pouvez le voir, la méthode `validateUser` inclut quatre logiques de traitement. Nous devons donc écrire un code de test unitaire correspondant pour ces quatre points afin de nous assurer que l'ensemble de la fonction `validateUser` fonctionne correctement.

### Le premier cas de test

Lorsque nous commençons à écrire des tests unitaires, nous rencontrons un problème : la méthode `findOne` doit interagir avec la base de données, et elle recherche des utilisateurs correspondants dans la base de données via `username`. Mais si chaque test unitaire doit interagir avec la base de données, les tests deviendront très fastidieux. Nous pouvons donc simuler des données fictives pour y parvenir.

Par exemple, supposons que nous avons enregistré un utilisateur nommé `woai3c`. Ensuite, lors de la connexion, les données de l'utilisateur peuvent être récupérées dans la méthode `validateUser` via `const entity = await this.usersService.findOne({ username });`. Tant que cette ligne de code peut retourner les données souhaitées, il n'y a pas de problème, même sans interaction avec la base de données. Nous pouvons y parvenir grâce à des données simulées.

Maintenant, examinons le code de test pertinent pour la méthode `validateUser` :

```typescript
import { Test } from '@nestjs/testing';
import { AuthService } from '@/modules/auth/auth.service';
import { UsersService } from '@/modules/users/users.service';
import { UnauthorizedException } from '@nestjs/common';
import { TEST_USER_NAME, TEST_USER_PASSWORD } from '@tests/constants';
describe('AuthService', () => {
  let authService: AuthService; // Utiliser le type AuthService réel
  let usersService: Partial<Record<keyof UsersService, jest.Mock>>;
  beforeEach(async () => {
    usersService = {
      findOne: jest.fn(),
    };
    const module = await Test.createTestingModule({
      providers: [        AuthService,
        {
          provide: UsersService,
          useValue: usersService,
        },
      ],
    }).compile();
    authService = module.get<AuthService>(AuthService);
  });
  describe('validateUser', () => {
    it('should throw an UnauthorizedException if user is not found', async () => {
      await expect(
        authService.validateUser(TEST_USER_NAME, TEST_USER_PASSWORD),
      ).rejects.toThrow(UnauthorizedException);
    });
    // autres tests...
  });
});
```

Nous obtenons les données de l'utilisateur en appelant la méthode `findOne` de `usersService`, nous devons donc simuler la méthode `findOne` de `usersService` dans le code de test :

```typescript
beforeEach(async () => {
    usersService = {
      findOne: jest.fn(), // simuler la méthode findOne
    };
    const module = await Test.createTestingModule({
      providers: [        AuthService, // AuthService réel, car nous testons ses méthodes
        {
          provide: UsersService, // utiliser usersService simulé au lieu de usersService réel
          useValue: usersService,
        },
      ],
    }).compile();
    authService = module.get<AuthService>(AuthService);
  });
```

Nous utilisons `jest.fn()` pour retourner une fonction afin de remplacer la vraie méthode `usersService.findOne()`. Si `usersService.findOne()` est appelé maintenant, il n'y aura pas de valeur de retour, donc le premier cas de test unitaire passera :

```typescript
it('should throw an UnauthorizedException if user is not found', async () => {
  await expect(
    authService.validateUser(TEST_USER_NAME, TEST_USER_PASSWORD),
  ).rejects.toThrow(UnauthorizedException);
});
```

Puisque `findOne` dans `const entity = await this.usersService.findOne({ username });` de la méthode `validateUser` est une fonction simulée fictive sans valeur de retour, les 2e à 4e lignes de code dans la méthode `validateUser` pourraient s'exécuter :

```typescript
if (!entity) {
  throw new UnauthorizedException('User not found');
}
```

Il lève une erreur 401, ce qui est attendu.

### Le deuxième cas de test

La deuxième logique dans la méthode `validateUser` est de déterminer si l'utilisateur est verrouillé, avec le code correspondant comme suit :

```typescript
if (entity.lockUntil && entity.lockUntil > Date.now()) {
  const diffInSeconds = Math.round((entity.lockUntil - Date.now()) / 1000);
  let message = `The account is locked. Please try again in ${diffInSeconds} seconds.`;
  if (diffInSeconds > 60) {
    const diffInMinutes = Math.round(diffInSeconds / 60);
    message = `The account is locked. Please try again in ${diffInMinutes} minutes.`;
  }
  throw new UnauthorizedException(message);
}
```

Comme vous pouvez le voir, nous pouvons déterminer que le compte actuel est verrouillé s'il y a un temps de verrouillage `lockUntil` dans les données de l'utilisateur et que le temps de fin de verrouillage est supérieur à l'heure actuelle. Nous devons donc simuler des données utilisateur avec le champ `lockUntil` :

```typescript
it('should throw an UnauthorizedException if the account is locked', async () => {
  const lockedUser = {
    _id: TEST_USER_ID,
    username: TEST_USER_NAME,
    password: TEST_USER_PASSWORD,
    lockUntil: Date.now() + 1000 * 60 * 5, // Le compte est verrouillé pendant 5 minutes
  };
  usersService.findOne.mockResolvedValueOnce(lockedUser);
  await expect(
    authService.validateUser(TEST_USER_NAME, TEST_USER_PASSWORD),
  ).rejects.toThrow(UnauthorizedException);
});
```

Dans le code de test ci-dessus, un objet `lockedUser` est d'abord défini, qui contient le champ `lockUntil` dont nous avons besoin. Ensuite, il est utilisé comme valeur de retour pour `findOne`, réalisé par `usersService.findOne.mockResolvedValueOnce(lockedUser);`. Ainsi, lorsque la méthode `validateUser` est exécutée, les données utilisateur à l'intérieur sont les données simulées, permettant au deuxième cas de test de passer avec succès.

### Couverture des tests unitaires

La couverture des tests unitaires (Code Coverage) est une métrique utilisée pour décrire combien de code de l'application a été couvert ou testé par les tests unitaires. Elle est généralement exprimée en pourcentage, indiquant combien de tous les chemins de code possibles ont été couverts par les cas de test.

La couverture des tests unitaires comprend généralement les types suivants :

* Couverture des lignes : Combien de lignes de code sont couvertes par les tests.
    
* Couverture des fonctions : Combien de fonctions ou de méthodes sont couvertes par les tests.
    
* Couverture des branches : Combien de branches de code sont couvertes par les tests (par exemple, les instructions `if/else`).
    
* Couverture des instructions : Combien d'instructions dans le code sont couvertes par les tests.
    

La couverture des tests unitaires est une métrique importante pour mesurer la qualité des tests unitaires, mais ce n'est pas la seule métrique. Un taux de couverture élevé peut aider à détecter les erreurs dans le code, mais il ne garantit pas la qualité du code. Un taux de couverture faible peut signifier qu'il y a du code non testé, potentiellement avec des erreurs non détectées.

L'image ci-dessous montre les résultats de la couverture des tests unitaires pour un projet de démonstration :

[![Aperçu de la couverture des tests unitaires montrant les résultats des tests avec des pourcentages pour les instructions, les branches, les fonctions et les lignes](https://camo.githubusercontent.com/e3de4ecc6be093ac92a514fa183f688c455b00cc15a3d003bfe2f25e31a08c4f/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f76322f726573697a653a6669743a313331302f666f726d61743a776562702f302a515a5f4d4a77774c715752314d3136652e706e67 align="left")](https://camo.githubusercontent.com/e3de4ecc6be093ac92a514fa183f688c455b00cc15a3d003bfe2f25e31a08c4f/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f76322f726573697a653a6669743a313331302f666f726d61743a776562702f302a515a5f4d4a77774c715752314d3136652e706e67)

Pour les fichiers comme les services et les contrôleurs, il est généralement préférable d'avoir une couverture de tests unitaires plus élevée, tandis que pour les fichiers comme les modules, il n'est pas nécessaire d'écrire des tests unitaires, ni même possible, car cela n'a pas de sens.

C'est parce que les modules NestJS sont principalement des fichiers de configuration qui définissent la structure de votre application en connectant des contrôleurs, des services et d'autres composants ensemble. Ils ne contiennent pas de logique métier réelle à tester, mais servent plutôt d'instructions de câblage pour le système d'injection de dépendances. Tester les modules ne vérifierait que le bon fonctionnement des fonctionnalités principales de NestJS, ce qui est déjà testé par l'équipe NestJS elle-même.

L'image ci-dessus représente les métriques globales de l'ensemble de la couverture des tests unitaires. Si vous souhaitez consulter la couverture des tests pour une fonction spécifique, vous pouvez ouvrir le fichier `coverage/lcov-report/index.html` dans le répertoire racine du projet. Par exemple, je veux voir la situation de test spécifique pour la méthode `validateUser` :

[![Couverture de test détaillée pour la méthode validateUser montrant les lignes spécifiques non couvertes mises en évidence en rouge](https://camo.githubusercontent.com/e5757001ae5bfec61c2b3ed19f7ef99cffc6c014480d7dad17ab28a2713f6aa0/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f76322f726573697a653a6669743a313430302f666f726d61743a776562702f302a4e32542d44694d754566776b332d33322e706e67 align="left")](https://camo.githubusercontent.com/e5757001ae5bfec61c2b3ed19f7ef99cffc6c014480d7dad17ab28a2713f6aa0/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f76322f726573697a653a6669743a313430302f666f726d61743a776562702f302a4e32542d44694d754566776b332d33322e706e67)

Comme vous pouvez le voir, la couverture des tests unitaires originale pour la méthode `validateUser` n'est pas de 100 %, et il y a encore deux lignes de code qui n'ont pas été exécutées. Mais cela n'a pas beaucoup d'importance, car cela n'affecte pas les quatre nœuds de traitement clés, et nous ne devrions pas poursuivre une couverture de test élevée de manière unidimensionnelle.

## Comment écrire des tests E2E

Dans la section des tests unitaires, vous avez appris comment écrire des tests unitaires pour chaque fonctionnalité de la fonction `validateUser()`, en utilisant des données simulées pour vous assurer que chaque fonctionnalité pouvait être testée.

Dans les tests E2E, nous devons simuler des scénarios utilisateurs réels, donc la connexion à une base de données pour les tests est nécessaire. Ainsi, les méthodes dans le module `auth.service.ts` que nous allons tester interagissent toutes avec la base de données.

Le module `auth` comprend principalement les fonctionnalités suivantes :

* Inscription
    
* Connexion
    
* Actualisation du token
    
* Lecture des informations utilisateur
    
* Changement de mot de passe
    
* Suppression des utilisateurs
    

Les tests E2E doivent tester ces six fonctionnalités une par une, en commençant par `l'inscription` et en terminant par `la suppression des utilisateurs`. Pendant les tests, nous pouvons créer un utilisateur de test dédié pour effectuer les tests, puis supprimer cet utilisateur de test à la fin, afin de ne pas laisser d'informations inutiles dans la base de données de test.

```typescript
beforeAll(async () => {
  const moduleFixture: TestingModule = await Test.createTestingModule({
    imports: [AppModule],
  }).compile()
  app = moduleFixture.createNestApplication()
  await app.init()
  // Effectuer une connexion pour obtenir un token
  const response = await request(app.getHttpServer())
    .post('/auth/register')
    .send({ username: TEST_USER_NAME, password: TEST_USER_PASSWORD })
    .expect(201)
  accessToken = response.body.access_token
  refreshToken = response.body.refresh_token
})
afterAll(async () => {
  await request(app.getHttpServer())
    .delete('/auth/delete-user')
    .set('Authorization', `Bearer ${accessToken}`)
    .expect(200)
  await app.close()
})
```

La fonction de crochet `beforeAll` s'exécute avant que tous les tests ne commencent, nous pouvons donc enregistrer un compte de test `TEST_USER_NAME` ici. La fonction de crochet `afterAll` s'exécute après que tous les tests se terminent, il est donc approprié de supprimer le compte de test `TEST_USER_NAME` ici. Cela teste également les fonctions d'inscription et de suppression.

Dans la section précédente des tests unitaires, nous avons écrit des tests unitaires pertinents autour de la méthode `validateUser`. En fait, cette méthode est exécutée pendant la connexion pour valider si le compte et le mot de passe de l'utilisateur sont corrects. Ce test E2E utilisera donc également le processus de connexion pour démontrer comment composer les cas de test E2E.

L'ensemble du processus de test de connexion comprend cinq petits tests :

```typescript
describe('login', () => {
    it('/auth/login (POST)', () => {
      // ...
    })
    it('/auth/login (POST) with user not found', () => {
      // ...
    })
    it('/auth/login (POST) without username or password', async () => {
      // ...
    })
    it('/auth/login (POST) with invalid password', () => {
      // ...
    })
    it('/auth/login (POST) account lock after multiple failed attempts', async () => {
      // ...
    })
  })
```

Ces cinq tests sont les suivants :

1. Connexion réussie, retour 200
    
2. Si l'utilisateur n'existe pas, lever une exception 401
    
3. Si le mot de passe ou le nom d'utilisateur n'est pas fourni, lever une exception 400
    
4. Connexion avec le mauvais mot de passe, lever une exception 401
    
5. Si le compte est verrouillé, lever une exception 401
    

Commençons maintenant à écrire les tests E2E :

```typescript
// connexion réussie
it('/auth/login (POST)', () => {
  return request(app.getHttpServer())
    .post('/auth/login')
    .send({ username: TEST_USER_NAME, password: TEST_USER_PASSWORD })
    .expect(200)
})
// si l'utilisateur n'est pas trouvé, devrait lever une exception 401
it('/auth/login (POST) with user not found', () => {
  return request(app.getHttpServer())
    .post('/auth/login')
    .send({ username: TEST_USER_NAME2, password: TEST_USER_PASSWORD })
    .expect(401) // Attendre une erreur non autorisée
})
```

Écrire du code de test E2E est relativement simple : vous appelez simplement l'interface et vérifiez ensuite le résultat. Par exemple, pour le test de connexion réussie, nous devons simplement vérifier que le résultat retourné est 200.

Les quatre premiers tests sont assez simples. Regardons maintenant un test E2E un peu plus compliqué, qui est de vérifier si un compte est verrouillé.

```typescript
it('/auth/login (POST) account lock after multiple failed attempts', async () => {
  const moduleFixture: TestingModule = await Test.createTestingModule({
    imports: [AppModule],
  }).compile()
  const app = moduleFixture.createNestApplication()
  await app.init()
  const registerResponse = await request(app.getHttpServer())
    .post('/auth/register')
    .send({ username: TEST_USER_NAME2, password: TEST_USER_PASSWORD })
  const accessToken = registerResponse.body.access_token
  const maxLoginAttempts = 3 // verrouiller l'utilisateur lorsque la troisième tentative échoue
  for (let i = 0; i < maxLoginAttempts; i++) {
    await request(app.getHttpServer())
      .post('/auth/login')
      .send({ username: TEST_USER_NAME2, password: 'InvalidPassword' })
  }
  // Le compte est verrouillé après la troisième tentative de connexion échouée
  await request(app.getHttpServer())
    .post('/auth/login')
    .send({ username: TEST_USER_NAME2, password: TEST_USER_PASSWORD })
    .then((res) => {
      expect(res.body.message).toContain(
        'The account is locked. Please try again in 5 minutes.',
      )
    })
  await request(app.getHttpServer())
    .delete('/auth/delete-user')
    .set('Authorization', `Bearer ${accessToken}`)
  await app.close()
})
```

Lorsque l'utilisateur échoue à se connecter trois fois de suite, le compte sera verrouillé. Donc, dans ce test, nous ne pouvons pas utiliser le compte de test `TEST_USER_NAME`, car si le test réussit, ce compte sera verrouillé et ne pourra pas continuer les tests suivants. Nous devons enregistrer un autre nouvel utilisateur `TEST_USER_NAME2` spécifiquement pour tester le verrouillage du compte, et supprimer cet utilisateur après que le test soit réussi.

Ainsi, comme vous pouvez le voir, le code de ce test E2E est assez substantiel, nécessitant beaucoup de travail de configuration et de nettoyage, mais le code de test réel n'est que ces quelques lignes :

```typescript
// se connecter trois fois
for (let i = 0; i < maxLoginAttempts; i++) {
  await request(app.getHttpServer())
    .post('/auth/login')
    .send({ username: TEST_USER_NAME2, password: 'InvalidPassword' })
}
// tester si le compte est verrouillé
await request(app.getHttpServer())
  .post('/auth/login')
  .send({ username: TEST_USER_NAME2, password: TEST_USER_PASSWORD })
  .then((res) => {
    expect(res.body.message).toContain(
      'The account is locked. Please try again in 5 minutes.',
    )
  })
```

Écrire du code de test E2E est relativement simple. Vous n'avez pas besoin de considérer les données simulées ou la couverture des tests. Il suffit que l'ensemble du processus système s'exécute comme prévu.

## Quand écrire des tests

Si possible, je recommande généralement d'écrire des tests. Cela peut améliorer la robustesse, la maintenabilité et l'efficacité du développement du système. Voici quelques raisons clés pour lesquelles écrire des tests est utile :

### Améliorer la robustesse du système

Lorsque vous écrivez du code, vous vous concentrez généralement sur le flux du programme sous des entrées normales pour vous assurer que la fonctionnalité principale fonctionne correctement. Mais vous pourriez souvent négliger certains cas limites, comme les entrées anormales.

Écrire des tests change cela, car cela vous oblige à considérer comment gérer ces cas et à répondre de manière appropriée, évitant ainsi les plantages. Nous pouvons donc dire que l'écriture de tests améliore indirectement la robustesse du système.

### Améliorer la maintenabilité

Prendre en charge un nouveau projet qui inclut des tests complets peut être très agréable. Ils agissent comme un guide, vous aidant à comprendre rapidement les différentes fonctionnalités. En regardant simplement le code de test, vous pouvez facilement saisir le comportement attendu et les conditions limites de chaque fonction sans avoir à parcourir chaque ligne du code de la fonction.

### Améliorer l'efficacité du développement

Imaginez un projet qui n'a pas été mis à jour depuis un certain temps et qui reçoit soudainement de nouvelles exigences. Après avoir apporté des modifications, vous pourriez craindre d'introduire des bugs. Sans tests, vous devriez tester manuellement l'ensemble du projet à nouveau, ce qui est une perte de temps et inefficace.

Avec des tests complets, une seule commande peut vous dire si les modifications de code ont impacté les fonctionnalités existantes. Même s'il y a des erreurs, vous pouvez les localiser rapidement et les corriger.

## Quand ne pas écrire de tests

Pour les projets à court terme et les projets avec des itérations de exigences très rapides, il n'est pas recommandé d'écrire des tests.

Par exemple, un projet construit pour un événement qui deviendra inutile après la fin de l'événement n'a pas besoin de tests. De plus, pour les projets qui subissent des itérations de exigences très rapides, écrire des tests pourrait améliorer l'efficacité du développement, mais cela repose sur le principe que les itérations de fonction sont lentes. Si la fonction que vous venez de terminer change en un jour ou deux, le code de test lié doit être réécrit.

Il est donc préférable de ne pas écrire de tests du tout dans ces cas et de s'appuyer sur l'équipe de test à la place, car écrire des tests est très chronophage et ne vaut pas l'effort pour ces situations.

## Conclusion

J'ai expliqué en détail comment écrire des tests unitaires et des tests E2E pour les projets NestJS. Mais je tiens à réitérer l'importance des tests. Ils peuvent améliorer la robustesse, la maintenabilité et l'efficacité du développement du système.

Si vous n'avez pas l'occasion d'écrire des tests, je vous suggère de commencer un projet de pratique vous-même ou de participer à certains projets open source et de contribuer du code à ceux-ci. Les projets open source ont généralement des exigences de code plus strictes. Contribuer du code peut nécessiter que vous écriviez de nouveaux cas de test ou que vous modifiiez ceux existants.

### Matériel de référence

* [NestJS](https://nestjs.com/) : Un framework pour construire des applications serveur Node.js efficaces et évolutives.
    
* [MongoDB](https://www.mongodb.com/) : Une base de données NoSQL utilisée pour le stockage des données.
    
* [Jest](https://jestjs.io/) : Un framework de test pour JavaScript et TypeScript.
    
* [Supertest](https://github.com/visionmedia/supertest) : Une bibliothèque pour tester les serveurs HTTP.