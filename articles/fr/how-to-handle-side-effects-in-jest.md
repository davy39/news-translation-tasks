---
title: Comment gérer les effets de bord dans Jest – Un guide pour un mocking efficace
subtitle: ''
author: ِAya Nabil Othman
co_authors: []
series: null
date: '2024-09-16T21:03:08.190Z'
originalURL: https://freecodecamp.org/news/how-to-handle-side-effects-in-jest
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726038899380/6210fc66-17fb-4db9-9f91-1e7d38dc256c.png
tags:
- name: Testing
  slug: testing
- name: Node.js
  slug: nodejs
seo_title: Comment gérer les effets de bord dans Jest – Un guide pour un mocking efficace
seo_desc: Unit testing is a major topic for every developer. It is a fundamental practice
  in building software applications. Unit testing helps you to identify bugs early
  and makes code maintenance easier. By isolating and testing single units or components
  of...
---

Le test unitaire est un sujet majeur pour tout développeur. C'est une pratique fondamentale dans la construction d'applications logicielles. Les tests unitaires vous aident à identifier les bogues tôt et facilitent la maintenance du code. En isolant et en testant des unités ou des composants uniques de votre application, vous pouvez garantir leur fiabilité et leur fonctionnalité.

Lors de l'application des tests unitaires, vous devez vous concentrer sur la logique principale d'un composant sans affecter les dépendances externes ni provoquer d'effets de bord — des changements imprévus qui se produisent en dehors de la portée d'une fonction, comme des requêtes de base de données ou des requêtes réseau.

Jest est un Framework de test populaire qui offre des capacités puissantes pour aider à un test efficace. Le mocking dans Jest vous aide à tester et à gérer les dépendances externes et à manipuler les effets de bord.

Dans ce guide, vous en apprendrez davantage sur les essentiels des tests unitaires, en vous concentrant sur les mocks Jest. Que vous débutiez ou que vous cherchiez à améliorer votre stratégie de test, ce guide vous dotera des connaissances nécessaires pour écrire des tests efficaces et performants.

### **Voici ce que nous allons couvrir :**

* [Qu'est-ce que les tests unitaires ?](#heading-quest-ce-que-les-tests-unitaires)
    
* [Que sont les dépendances externes ?](#heading-que-sont-les-dependances-externes)
    
* [Que sont les effets de bord ?](#heading-que-sont-les-effets-de-bord)
    
* [Qu'est-ce que le Mocking ?](#heading-quest-ce-que-le-mocking)
    
* [Cas d'utilisation : Contrôleur de connexion Express](#heading-cas-dutilisation-controleur-de-connexion-express)
    
* [Résumé](#heading-resume)
    

## **Qu'est-ce que les tests unitaires ?**

Le test unitaire est une technique de test logiciel utilisée pour tester un seul composant de votre application de manière isolée. Ce composant peut être une classe, une méthode ou un module.

### Pourquoi devriez-vous utiliser les tests unitaires

1. Vous pourrez détecter les bogues plus tôt, cela vous aide à vérifier si un composant se comporte comme prévu.
    
2. Cela vous permet de modifier votre composant en toute sécurité. Si vous mettez à jour votre composant et que, par erreur, vous ajoutez ou modifiez quelque chose que vous ne devriez pas, le test échouera si ces changements introduisent un nouveau bogue.
    
3. Il peut servir de documentation montrant comment les unités individuelles de votre application fonctionnent.
    
4. Cela vous encourage à écrire un code plus propre. Plus votre composant est propre, plus votre test sera facile et simple.
    
5. Cela vous aide à intégrer facilement différentes parties de votre application, car vous serez sûr que chaque composant individuel fonctionne correctement.
    
6. À long terme, vous pouvez maintenir votre application plus rapidement.
    

Plongeons dans quelques utilisations pratiques :

Supposons que vous ayez une fonction de multiplication qui doit prendre deux arguments et retourner le résultat.

Voici le code :

```javascript
function multiply(a,b) {
    return a*b
}
export default multiply
```

**Note** : Pour utiliser Jest avec les modules ECMAScript de Node.js, consultez cet [article](https://ayanabilothman.hashnode.dev/configure-jest-to-use-it-with-nodejs-ecmascript-modules) pour la configuration.

Alors, comment pouvez-vous tester cette fonction en utilisant Jest ?

1. Créez un dossier ***\_\_tests\_\_*** à la racine.
    
2. Créez un fichier ***multiply.test.js*** à l'intérieur de ***\_\_tests\_\_*** .
    
    Notez que tout fichier se terminant par ***.test.js*** sera exécuté par Jest.
    
3. Commencez à écrire vos tests en appelant la méthode Jest `it("",()=>{})`.
    

Comprenons ce que fait \``it("",()=>{})`\` :

La méthode `it` est une fonction Jest utilisée pour tester certains comportements dans votre fonction.  
Le premier argument doit être le nom du test, qui peut être un texte d'assertion de ce que vous attendez de ce test.

Par exemple, si vous devez tester si la fonction `multiply` retourne le bon résultat en utilisant les arguments et s'ils sont des nombres, vous pouvez écrire `it("devrait retourner la multiplication des entrées de type nombre",()=>{})`.

Le second argument est une fonction pour votre logique de test. Elle est invoquée une fois que vous lancez votre test**.**

Pour écrire efficacement vos tests, vous devriez appliquer le modèle AAA (Arrange-Act-Assert / Initialiser-Agir-Vérifier).

1. **Arrange (Initialiser)** : Configurez les données ou configurez toutes les dépendances que vous utiliserez dans ce test.
    
2. **Act (Agir)** : Appelez la fonction que vous testez.
    
3. **Assert (Vérifier)** : Écrivez vos attentes — comment vous attendez que la fonction que vous testez se comporte. Pour l'assertion, vous utiliserez toujours la méthode Jest `expect`.
    

Pensez à chaque instruction `it("",()=>{})` comme à un scénario différent de votre fonction.

Voici un exemple :

```javascript
import multiply from './../multiply.js'

it("devrait retourner la multiplication des entrées de type nombre", () => {
  // Initialiser (Arrange)
  const testArg1 = 5;
  const testArg2 = 2;
  // Agir (Act)
  const result = multiply(testArg1, testArg2);
  // Vérifier (Assert)
  expect(result).toBe(10);
});

it("devrait retourner NaN si aucun argument n'est passé", () => {
  // Initialiser
  // Agir
  const result = multiply();
  // Vérifier
  expect(result).toBeNaN();
});

it("devrait retourner NaN si un seul argument est passé", () => {
  // Initialiser
  const arg = 5;
  // Agir
  const result = multiply(arg);
  // Vérifier
  expect(result).toBeNaN();
});

it("devrait retourner Zéro si l'un des arguments est une chaîne vide", () => {
  // Initialiser
  const testArg1 = "";
  const testArg2 = 5;
  // Agir
  const result = multiply(testArg1, testArg2);
  // Vérifier
  expect(result).toBe(0);
});
```

Ces tests sont quelques-uns des tests que vous pouvez ajouter à votre fichier. Vous pouvez en ajouter d'autres ou en supprimer certains en fonction des différents scénarios de la fonction que vous testez.

## Que sont les dépendances externes ?

Les dépendances externes sont des modules ou des fonctions dont dépend votre code, qui proviennent de l'extérieur de votre propre base de code. Celles-ci peuvent inclure des bibliothèques, des API, des bases de données, des fonctions ou tout service avec lequel votre application interagit.  
  
Tester avec des dépendances externes peut être difficile car :

* Elles peuvent ralentir les tests en raison de délais de réseau ou de traitement.
    
* Elles pourraient ne pas être disponibles pendant les tests, ce qui provoque des échecs.
    

Comme montré dans la fonction suivante, que se passe-t-il si votre fonction appelle une autre fonction ? La plupart des fonctions que vous écrivez quotidiennement appellent en réalité d'autres fonctions.

À savoir :

```javascript
function processNumbers(numbers, callback) {
    // numbers: tableau
    // callback: fonction
  return numbers.map(callback);
}

export default processNumbers;
```

Lors de l'application des tests unitaires, les unités doivent être testées de manière isolée. La fonction `processNumbers` dépend d'une autre fonction `callback`.

Alors, que devriez-vous faire dans ce cas ? Le mocking est la solution et nous en parlerons plus tard dans une section différente.

## **Que sont les effets de bord ?**

Les effets de bord (side effects) se produisent lorsqu'une fonction modifie un état en dehors de sa propre portée ou a des interactions observables avec le monde extérieur en dehors du retour d'une valeur.

Les exemples incluent la modification d'une variable globale, le changement d'un système de fichiers ou l'envoi d'une requête HTTP.

Les effets de bord peuvent rendre les tests imprévisibles et difficiles à gérer car ils :

* Peuvent interagir avec d'autres systèmes, causant l'altération d'états externes.
    
* Peuvent mener à des tests instables (flaky) s'ils ne sont pas isolés correctement.
    

Voici un exemple qui retourne un utilisateur d'une base de données à l'aide de son `id` :

```javascript
async function getUserFromDatabase(userId) {
  // Simule la récupération depuis une base de données
  return { id: userId, name: 'John' };
}

export {getUserFromDatabase}
```

Voici une autre fonction qui utilise `getUserFromDatabase` dans le code ci-dessus :

```javascript
async function getProfile(userId) {
  return await getUserFromDatabase(userId);
}

export default getProfile
```

Lors du test de cette fonction, vous ne devriez pas réellement envoyer une vraie requête ; tout ce dont vous avez besoin est de tester le comportement de la fonction `getProfile` sans solliciter de système externe.

Vous pouvez également utiliser le mocking pour résoudre cette situation.

## **Qu'est-ce que le Mocking ?**

Le mocking est une question de simulation — vous devez isoler une fonction que vous testez. Si la fonction repose sur une dépendance externe ou peut causer un effet de bord, vous devez simuler le comportement de ces aspects.

Le mocking consiste à créer une version factice d'une fonction, d'un objet ou d'un module pour contrôler son comportement pendant les tests. Cela vous permet de simuler différents scénarios et de vérifier les interactions sans dépendre des implémentations réelles.

Nous nous concentrerons sur deux approches du mocking :

1. **Mocks de fonction (également appelés Spies) :**  
    Vous pouvez utiliser `jest.fn()` pour créer une fonction mock qui peut être utilisée pour suivre une fonction ou remplacer des implémentations réelles. Ou utilisez `jest.spyOn(object, methodName)` pour suivre les appels de `object[methodName]`.
    
2. **Mocks de module** : Vous pouvez utiliser `jest.mock("chemin-de-votre-module")` pour mocker des modules entiers ou des imports spécifiques. En l'utilisant, toutes les fonctions à l'intérieur de ce module deviennent des fonctions mocks. De plus, pendant les tests, les modules que vous testez recevront une version mockée factice de ce module.
    

Toute fonction mock possède des méthodes que vous pouvez utiliser pour simuler le comportement de la fonction. Certaines des méthodes les plus utilisées sont :

* `mockFn.mockImplementation(fn)` : Utilisé pour remplacer l'implémentation réelle d'une fonction. `fn` est l'implémentation de remplacement.
    
* `mockFn.mockReturnValue(value)` : Vous pouvez l'utiliser si seul le résultat de retour d'une fonction vous importe.
    
* `mockFn.mockResolvedValue(value)` : Vous pouvez l'utiliser si la fonction mock retourne une promesse.
    

### **Exemple d'utilisation 1**

Testons `processNumbers` en utilisant des mocks de fonction. Le défi ici est que `processNumbers` prend une fonction de rappel (callback) comme argument. Et si vous deviez tester si cette fonction callback est invoquée à l'intérieur de `processNumbers` ?

Voici le code :

```javascript
import processNumbers from 'file-path';

test('processNumbers applique le callback et retourne le bon résultat', () => {
    // Initialiser (Arrange)
    const arr = [2, 3]
    const mockedCallback = jest.fn().mockImplementation(x => x + 2);
    // Agir (Act)
    const result = processNumbers(arr, mockedCallback);
    // Vérifier (Assert)
    expect(result).toEqual([4, 5]);
    expect(mockedCallback).toHaveBeenCalledTimes(arr.length);
});
```

Nous avons commencé par préparer les arguments :

* La variable `arr` est un tableau de nombres. Nous lui avons assigné un tableau avec des nombres aléatoires dans le test.
    
* La variable `callback` est une fonction de rappel. Cette fonction doit être mockée dans le test.
    

Vous pourriez vous demander pourquoi vous devriez mocker `callback`, pourquoi ne pas l'assigner comme une fonction normale ?

La réponse est que, sans mocker l'argument `callback`, vous ne pourrez pas le suivre à l'intérieur de `processNumbers` pendant que vous le testez. Parce que le mocking crée une version factice de la fonction, il crée un espion (spy) qui possède un traqueur grâce auquel vous pouvez vérifier toute action entreprise dans cette fonction mockée, qu'elle soit appelée ou que des arguments lui soient passés.

Le `jest.fn()` crée une fonction mock. Vous pouvez passer une fonction à `fn` à la place de la fonction réelle.

Ensuite, nous « agissons » en appelant la fonction que nous testons : `processNumbers`.

Enfin, nous avons écrit les assertions, qui sont des attentes sur la façon dont `processNumbers` devrait se comporter et si `processNumbers` a appliqué `callback` et retourné le résultat.

### **Exemple d'utilisation 2**

Les effets de bord sont un autre aspect que vous devez gérer dans les tests. Dans la fonction `getProfile`, un système externe est appelé, lequel appelle une base de données pour récupérer des données, et c'est un effet de bord.

Dans un autre scénario, une fonction peut se connecter à une base de données pour créer un utilisateur, et via les tests, vous n'aurez pas besoin d'ajouter ou de modifier des données réelles dans la base de données.

Pour simuler le comportement de `getUserFromDatabase` sans solliciter réellement la base de données, vous devriez mocker son module, et par défaut, `getUserFromDatabase` sera une fonction mock vide qui pourra être suivie pendant votre test.

Voici le code :

```javascript
import getProfile from 'file-path';
import { getUserFromDatabase } from 'file-path';

// Mocker le module de la méthode getUserFromDatabase
jest.mock('./../DB/databaseMethods.js');

describe('getProfile', () => {
  it('devrait appeler getUserFromDatabase avec le bon userId et retourner le résultat', async () => {
    // Initialiser (Arrange)    
    const userId = '123';
    const dummyUser = { id: userId, name: 'John' };
    getUserFromDatabase.mockResolvedValue(dummyUser);
    // Agir (Act)
    const result = await getProfile(userId);
    // Vérifier (Assert)
    expect(result).toEqual(dummyUser);
    expect(getUserFromDatabase).toHaveBeenCalledWith(userId);
    expect(getUserFromDatabase).toHaveBeenCalledTimes(1);
  });
});
```

Nous avons commencé par préparer les arguments :

* `userId` est juste un nombre.
    
* `dummyUser` est un objet qui simule des données utilisateur factices.
    
* Nous avons retourné `dummyUser` de `getUserFromDatabase` en utilisant `mockResolvedValue`.
    

Semblable au dernier exemple, nous « agissons » en appelant la fonction testée : `getProfile`.

Enfin, nous avons écrit les assertions, vos attentes sur la façon dont `getProfile` devrait se comporter et si le `getUserFromDatabase` a été appelé correctement et si le résultat a été retourné comme prévu.

## Cas d'utilisation : Contrôleur de connexion Express

Voici un contrôleur de connexion qui reçoit l'e-mail et le mot de passe d'un utilisateur via l'objet `req`, puis recherche l'utilisateur dans la base de données. Il effectue quelques vérifications, puis renvoie un `res` si tout est correct, ou appelle `next` avec un objet d'erreur.

```javascript
import User from "file-path";

export const login = async (req, res, next) => {
  const { email, password } = req.body;

  const user = await User.findOne({ email });
  if (!user) return next(new Error("Email invalide !"));

  const checkPassword = user.checkPassword(password);
  if (!checkPassword) return next(new Error("Mot de passe invalide !"));

  const token = user.generateToken();

  return res.status(200).json({ success: true, results: { token } });
};
```

Pensez aux étapes que vous pouvez utiliser pour tester la fonction login. Vous pouvez poser quelques questions qui vous aideront à trouver des idées :

Quels sont les scénarios du flux de travail de la fonction `login` ?

1. L'utilisateur n'est pas trouvé.
    
2. Le mot de passe est incorrect.
    
3. Tout est correct, et une réponse est retournée avec un jeton (token).
    

Ainsi, vous pouvez affirmer que `login` doit faire ce qui suit :

* `login` doit appeler `next` si l'utilisateur n'est pas trouvé.
    
* `login` doit appeler `next` si le mot de passe ne correspond pas.
    
* `login` doit appeler **res.json** avec le jeton et appeler **res.status** avec 200 si tout est correct.
    

Quels sont les arguments que la méthode `login` doit recevoir ?

1. Objet `req` avec la propriété `body`.
    
2. Objet `res` avec les propriétés `status` et `json`.
    
3. Fonction `next`.
    

`res.json()`, `res.status()` ou `next()` sont toutes des fonctions dont `login` a besoin pour faire son travail. Pendant le test, vous n'avez pas accès à ces arguments, vous devez donc les mocker.

* `req` peut être défini comme `{body: { email: "`[`test@foo.com`](mailto:test@foo.com)`", password: "bar" }}`
    
* `res` peut être défini comme `{json: jest.fn().mockReturnThis(), status: jest.fn().mockReturnThis()}`
    
* `next` peut être défini comme `jest.fn()`
    

Y a-t-il des interactions avec des systèmes externes ou des dépendances ?

1. `User.findOne()`
    
2. `user.checkPassword()`
    
3. `user.generateToken()`
    

Ainsi, le mocking est la solution :

* Pour `User.findOne()`, vous devriez mocker le module `User` entier et configurer le `findOne()` factice pour retourner un `user` factice. Le défi ici est que `findOne` est une méthode d'objet. Comment pouvez-vous la suivre ? `jest.spyOn(object, methodName)` est la solution.  
    La méthode `spyOn` est utilisée pour suivre les appels de `object[methodName]`, qui, dans notre cas, est `User.findOne`.
    
* `user.checkPassword()` et `user.generateToken()` doivent être des fonctions mocks.
    

Pour appliquer tous ces concepts et assembler les blocs, le test final devrait être :

```javascript
import User from "file-path";
import { login } from "file-path";

jest.mock("../DB/models/user.model.js");

let mockReq, mockRes, mockNext, dummyUser;
describe("contrôleur login", () => {
  beforeEach(() => {
    mockReq = { body: { email: "test@foo.com", password: "bar" } };
    mockRes = {
      json: jest.fn().mockReturnThis(),
      status: jest.fn().mockReturnThis(),
    };
    mockNext = jest.fn();

    dummyUser = {
      checkPassword: jest.fn(() => true),
      generateToken: jest.fn(() => "token"),
    };
  });

  it("devrait appeler next si l'utilisateur n'est pas trouvé", async () => {
    // Initialiser (Arrange)
    jest.spyOn(User, "findOne").mockResolvedValueOnce(null);
    // Agir (Act)
    await login(mockReq, mockRes, mockNext);
    // Vérifier (Assert)
    expect(mockNext).toHaveBeenCalledWith(new Error("Email invalide !"));
    expect(mockRes.json).not.toHaveBeenCalled();
  });

  it("devrait appeler next si le mot de passe ne correspond pas", async () => {
    // Initialiser (Arrange)
    dummyUser.checkPassword.mockReturnValueOnce(false);
    jest.spyOn(User, "findOne").mockResolvedValue(dummyUser);
    // Agir (Act)
    await login(mockReq, mockRes, mockNext);
    // Vérifier (Assert)
    expect(mockNext).toHaveBeenCalledWith(new Error("Mot de passe invalide !"));
    expect(dummyUser.generateToken).not.toHaveBeenCalled();
    expect(mockRes.json).not.toHaveBeenCalled();
  });

  it("devrait appeler res.json avec le token et res.status avec 200 si tout est correct", async () => {
    // Initialiser (Arrange)
    jest.spyOn(User, "findOne").mockResolvedValue(dummyUser);
    // Agir (Act)
    await login(mockReq, mockRes, mockNext);
    // Vérifier (Assert)
    expect(mockNext).not.toHaveBeenCalled();
    expect(User.findOne).toHaveBeenCalledWith({ email: mockReq.body.email });

    expect(dummyUser.checkPassword).toHaveBeenCalledWith(mockReq.body.password);
    expect(dummyUser.generateToken).toHaveBeenCalled();

    expect(mockRes.status).toHaveBeenCalledWith(200);
    expect(mockRes.json).toHaveBeenCalledWith({
      success: true,
      results: { token: "token" },
    });
  });
});
```

**Note finale** : `beforeEach` est un hook Jest, vous pouvez l'utiliser pour implémenter du code avant chaque test. À l'intérieur de la fonction `beforeEach`, vous pouvez écrire toutes les variables communes dont vos tests pourraient avoir besoin au lieu de les écrire indépendamment pour chaque test.

## Résumé

Dans ce tutoriel, vous avez appris les bases des tests unitaires avec Jest, en vous concentrant sur l'utilisation des mocks. Les tests unitaires aident à garantir que les parties individuelles de votre code fonctionnent correctement en les testant de manière isolée.  
  
Gérer les dépendances externes, manipuler les effets de bord et utiliser le mocking sont des compétences essentielles pour des tests robustes. Jest fournit des outils puissants pour relever ces défis, rendant vos tests plus fiables, plus rapides et plus faciles à maintenir.

Comprendre ces concepts vous aidera à écrire de meilleurs tests et à produire des applications plus résilientes.

Ce tutoriel a expliqué comment utiliser les fonctionnalités de mocking de Jest pour simuler des dépendances externes et gérer les effets de bord. Il inclut un exemple pratique de test d'un contrôleur de connexion Express.js, montrant comment mocker des fonctions et contrôler les scénarios de test.

Cette approche vous aide à créer des tests fiables et à maintenir la qualité du code en isolant et en gérant efficacement les dépendances.