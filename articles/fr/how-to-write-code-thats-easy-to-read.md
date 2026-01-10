---
title: Comment écrire du code facile à lire – Conseils pour les développeurs
subtitle: ''
author: Orim Dominic Adah
co_authors: []
series: null
date: '2024-12-04T17:57:23.729Z'
originalURL: https://freecodecamp.org/news/how-to-write-code-thats-easy-to-read
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733334801650/9c73c253-246a-4678-8d65-6679ff7f35f2.png
tags:
- name: clean code
  slug: clean-code
seo_title: Comment écrire du code facile à lire – Conseils pour les développeurs
seo_desc: 'Programs are meant to be read by humans and only incidentally for computers
  to execute. - Donald Knuth


  Have you ever heard that programmers spend more time reading code than writing it?
  Well, I’ve found that this is often true: as a developer, you’l...'
---

> Les programmes sont destinés à être lus par les humains et seulement accessoirement à être exécutés par les ordinateurs. - Donald Knuth

Avez-vous déjà entendu dire que les programmeurs passent plus de temps à lire du code qu'à en écrire ? Eh bien, j'ai constaté que cela est souvent vrai : en tant que développeur, vous passerez souvent plus de temps à lire et à réfléchir sur le code qu'à en écrire réellement.

Cela signifie que, aussi optimal que vous souhaitiez rendre l'exécution de votre code, il est également important qu'il soit agréable et facile à lire.

Dans cet article, nous allons examiner une fonction exemple : `createOrUpdateUserOnLogin`. Elle se trouve dans une base de code JavaScript et elle mérite d'être rendue plus agréable à lire. Nous allons examiner `createOrUpdateUserOnLogin`, souligner ce qui la rend difficile à lire et pourquoi, et finalement la refactoriser pour la rendre plus facile à lire et à comprendre.

La fonction est écrite en JavaScript et utilise [JSDoc](https://jsdoc.app/) pour documenter ses paramètres. La connaissance de JavaScript n'est pas nécessairement importante car la logique de la fonction sera expliquée en détail. JSDoc est uniquement utilisé pour documenter ce que représentent les paramètres de la fonction.

## La fonction problématique

Cette fonction n'est pas inventée. Il s'agit d'une fonction réelle dans la base de code d'une application avec plus de mille utilisateurs. La voici :

```javascript
/**
 * @param {Object} dto
 * @param {string} dto.email
 * @param {string} dto.firstName
 * @param {string} dto.lastName
 * @param {string} [dto.photoUrl]
 * @param {'apple' | 'google'} [dto.loginProvider]
 * @param {string} [dto.appleId]
 * @returns {string} token - jeton d'accès
 */
async function createOrUpdateUserOnLogin(dto) {
  let user;

  if (dto.loginProvider == "apple") {
    user = await findOneByAppleId(dto.appleId);
    if (user?.isDisabled) {
      throw new Error("Impossible de se connecter");
    }

    if (user && !user.verified) {
      user = await setUserAsVerified(user.email);
    }

    if (!user) {
      user = await findOneByEmail(dto.email);

      if (user && dto.appleId) {
        user = await updateUserAppleId(user, dto.appleId);
      }

      if (user && !user.verified) {
        user = await setUserAsVerified(user.email);
      }
    }
  } else {
    user = await findOneByEmail(dto.email);
    if (user?.isDisabled) {
      throw new Error("Impossible de se connecter");
    }

    if (user && !user.photoUrl && dto.photoUrl) {
      user.photoUrl = dto.photoUrl;
      user = await updateUserDetails(user._id, user);
    }

    if (user && !user.verified) {
      user = await setUserAsVerified(user.email);
    }
  }

  if (!user) {
    user = await this.usersService.create(loginProviderDto);
  }
    
  return await this.createToken(user);
}
```

Peut-être pouvez-vous constater en lisant et en étudiant le code qu'il est assez difficile à suivre. Si vous quittez votre ordinateur pour une pause juste après avoir lu cette fonction, il y a de fortes chances que vous ne vous souveniez plus exactement de ce qu'elle fait à votre retour.

Mais ce n'est pas, et ne devrait pas être, le cas lorsque vous lisez une bonne histoire, quelle que soit sa longueur. Vous pouvez la suivre facilement et vous souvenir des détails de base après l'avoir entendue.

La fonction est exécutée lorsqu'un utilisateur tente de se connecter ou de s'inscrire. Les utilisateurs peuvent être authentifiés en utilisant leur compte Google ou leur compte Apple, et la fonction doit retourner un jeton d'accès en cas de tentative réussie.

Certains utilisateurs ont désactivé leur compte. Ces utilisateurs ne sont pas autorisés à s'authentifier avec succès. La logique de la fonction inclut également des opérations pour mettre à jour les données des utilisateurs déjà enregistrés en fonction de certaines conditions.

La fonction fait l'une des deux choses suivantes :

1. Elle crée un jeton d'authentification pour un compte existant et le retourne après avoir mis à jour les détails du compte, ou,

2. Elle crée un compte si aucun n'existe et retourne un jeton d'authentification.

Cela viole le principe de responsabilité unique – mais corriger cela est un défi pour un autre article.

L'objectif ici est de refactoriser cette fonction afin qu'elle soit si bien écrite que même un non-programmeur puisse la lire et comprendre ce qu'elle fait. Mieux encore, nous voulons également qu'ils puissent s'en souvenir après s'être éloignés un moment.

La fonction est bien testée, donc il n'y a pas de soucis à se faire concernant la rupture de fonctionnalités lors de la refactorisation. Les tests signaleront toute modification cassante.

### Qu'est-ce qui rend ce code difficile à lire ?

Plusieurs facteurs rendent ce code plus difficile à lire. Voici les principaux :

1. **Imbrication profonde** (des instructions `if` dans des instructions `if`) rend difficile le suivi des changements qui se produisent lors de l'exécution du code. Dans le cas de `createOrUpdateUserOnLogin`, il s'agit de conditionnelles imbriquées. D'autres cas peuvent inclure une logique comme une instruction `if` à l'intérieur d'une boucle `while` qui est imbriquée dans une autre instruction `if`.

L'imbrication profonde augmente la complexité de la lecture et de la compréhension du code. Son flux n'est pas agréable à l'œil et il rend l'écriture de tests plus compliquée car vous devez tenir compte des opérations à l'intérieur des blocs de code imbriqués.

2. **Conditionnelles complexes** comme `user && !user.photoUrl && dto.photoUrl` contiennent beaucoup de logique qui doit être gardée en mémoire à court terme et rappelée au fur et à mesure de la lecture.

3. **Flux désordonné** qui rend difficile de dire d'un coup d'œil ce que fait la fonction. La fonction semble faire beaucoup, mais ce n'est pas vraiment le cas. Deux opérations sont répétées : empêcher les utilisateurs désactivés de se connecter (deux fois) et mettre à jour le statut de vérification des utilisateurs (trois fois). Trouver un utilisateur par email est également répété deux fois.

## Comment refactoriser le code pour une lecture plus facile et plus agréable

Après avoir examiné la fonction pour identifier les problèmes qui la rendent difficile à lire, voici quelques changements que vous voudrez mettre en œuvre :

**Traiter les cas d'échec en premier** : Considérez les cas d'échec en premier et éliminez-les de l'histoire afin que la fonction puisse se concentrer sur les cas de succès pour une narration fluide de la logique du code.

Cela implique l'utilisation d'instructions `return` ou le lancement d'erreurs tôt dans la fonction pour les opérations qui empêchent l'objectif de la fonction d'être atteint.

**Réorganiser le flux** : Si certaines opérations peuvent se produire avant d'autres et que cela rend le flux du code mémorable et agréable à lire, tout en atteignant le but de la fonction, alors vous devriez le réorganiser en conséquence.

**Utiliser une grammaire quotidienne** : Cela implique de mettre à jour les identifiants et de compresser les conditionnelles complexes en noms d'identifiants mémorables. La grammaire quotidienne est facile à lire car elle est familière et relatable.

**Éviter les blocs de code imbriqués** : Lors du débogage mental du code ou de la tentative de le comprendre, les changements dans la valeur des identifiants dans les blocs de code imbriqués sont difficiles à suivre. Cela est dû au fait qu'avec chaque conditionnelle imbriquée, il y a au moins une augmentation de 2x du nombre de chemins que l'exécution logique peut prendre pour mettre à jour la valeur d'un identifiant – et cela s'aggrave s'il y a plus d'un identifiant qui est mis à jour.

Cela signifie que votre esprit doit suivre ces chemins, ce qui peut rapidement entraîner une surcharge de mémoire mentale, potentiellement entraînant des bugs lors de la mise à jour du code.

L'effet visuel du code imbriqué n'est également pas agréable à l'œil et il rend l'écriture de tests plus complexe que nécessaire.

Après avoir refactorisé le code en utilisant les directives ci-dessus, nous avons le snippet suivant (j'ai numéroté différentes parties du code pour référence dans les explications ci-dessous) :

```javascript
async function updateUserOnLogin(dto) {
  let user = await findUserByEmail(dto.email); // 1
  if (!user) {
    user = await createUser(dto);
  }

  if (user.isDisabled) { // 2a
    throw new Error("Impossible de se connecter"); // 2b
  }
  
  const userIsNotVerified = Boolean(user.isVerified) == false // 3a
  if (userIsNotVerified) { // 3b
    await setUserAsVerified(user.email);
  }

  const shouldUpdateAppleId = dto.loginProvider == "apple" && dto.appleId // 4a
  if (shouldUpdateAppleId) { // 4b
    await setUserAppleId(user.email, dto.appleId);
  }

  const shouldUpdatePhotoUrl = !user.photoUrl && dto.photoUrl // 5a
  if (shouldUpdatePhotoUrl) { // 5b
    await updateUserDetails(user._id, { photoUrl: dto.photoUrl });
  }

  return await this.createToken(user);
}
```

D'accord, voyons maintenant ce que nous avons fait exactement ici pour rendre le code plus agréable à lire.

### 1. Réorganiser le flux

En jugeant par le commentaire JSDoc au-dessus de la fonction, `email` est un champ d'argument requis. Les comptes existants ont une adresse email indépendamment de leur fournisseur de connexion. Nous pouvons récupérer un compte par `email` d'abord et décider de créer un nouveau si aucun n'existe (section de code 1). En faisant cela, les cas d'échec sont traités tôt.

Choisir de lancer une erreur si le compte est désactivé au début (section 2b) est également une tentative de traiter les cas d'échec tôt. Cela n'affecte pas les nouveaux comptes car les nouveaux comptes ne sont pas désactivés par défaut.

Traiter les cas d'échec tôt nous aide à comprendre le code plus facilement car nous sommes libres de considérer seulement ce qui va se passer sans avoir à suivre les cas d'erreur précédents (comme se souvenir si l'objet `user` a une valeur ou non (section 5)) au fur et à mesure de la lecture.

Le code refactorisé a également éliminé les conditionnelles imbriquées et fonctionne toujours comme prévu.

### 2. Utiliser une grammaire quotidienne

En essayant de faire en sorte que le code se lise comme une grammaire quotidienne, nous avons utilisé des noms de variables clairs et relatables (voir sections 2a, 3, 4, 5). Écrit de cette manière, même les non-programmeurs comme les chefs de produit peuvent lire le code et comprendre ce qui se passe.

La grammaire quotidienne se lit comme du pseudocode - « Si l'utilisateur n'est pas vérifié, alors définir l'utilisateur comme vérifié » et « Si doit mettre à jour l'ID Apple, alors mettre à jour l'ID Apple ».

Utiliser une grammaire quotidienne est la clé pour faire en sorte que le code se lise comme une histoire.

## Conclusion

Le code qui est agréable à lire favorise la maintenabilité et donc la longévité du logiciel. Les contributeurs peuvent le lire, le comprendre et éventuellement le mettre à jour avec facilité. Comme lire une histoire bien écrite, lire du code peut être une activité agréable.

Crédit image : [Illustrations de travail par Storyset](https://storyset.com/work)