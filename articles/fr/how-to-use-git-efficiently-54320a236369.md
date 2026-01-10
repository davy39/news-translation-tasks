---
title: Comment utiliser Git efficacement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-29T16:34:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-efficiently-54320a236369
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Nv1sgovc6sNy89N_
tags:
- name: Git
  slug: git
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: workflow
  slug: workflow
seo_title: Comment utiliser Git efficacement
seo_desc: 'By Aditya Sridhar


  The code was working yesterday but today it is not

  The code got deleted

  A weird bug has been introduced suddenly and no-one knows how


  If you have been in any of the above situations then this post is for you.

  Apart from knowing gi...'
---

Par Aditya Sridhar

> _Le code fonctionnait hier mais aujourd'hui il ne fonctionne plus_

> Le code a été supprimé

> _Un bug étrange a été introduit soudainement et personne ne sait comment_

Si vous vous êtes trouvé dans l'une des situations ci-dessus, alors **cet article est pour vous**.

En plus de connaître `git add`, `git commit` et `git push`, il existe de nombreuses autres techniques importantes dans Git. Les connaître vous aidera beaucoup à long terme. Ici, je vais couvrir certaines des choses qui vous permettront de faire le **meilleur usage de Git.**

### Workflows Git

Lorsque plusieurs développeurs sont impliqués dans un projet, il est nécessaire d'utiliser le bon workflow pour Git. Ici, je vais couvrir un workflow qui est très efficace dans les grands projets avec plusieurs développeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/LBct-BJctnUEC2R7MIznkdoVQ5Lh6BfhykHC)
_espérons que ce schéma de workflow que j'ai créé vous aidera à visualiser le processus :)_

#### Scénario

Tout à coup, vous êtes devenu le tech lead pour un projet dans lequel vous prévoyez de construire le prochain Facebook. L'équipe compte trois développeurs :

1. **Alice** : a un an d'expérience et connaît la programmation
2. **Bob** : a un an d'expérience et connaît la programmation
3. **John** : a 3 ans d'expérience et connaît bien la programmation
4. **Vous** : assigné en tant que tech lead pour ce projet

### Processus de développement dans Git

#### Branche Master

1. La branche Master doit toujours contenir une copie du code existant en production.
2. Personne — **y compris** le tech lead — ne doit coder directement dans la branche master puisqu'il s'agit d'une copie du code de production.
3. Le code réel est écrit dans d'autres branches.

#### Branche Release

1. Lorsque le projet commence, la première chose à faire est de créer une **branche release** pour le projet. La branche release est créée à partir de la **branche master**.
2. Tout le code relatif à ce projet sera dans la **branche release**. La branche release est simplement une branche normale avec le préfixe **release/**.
3. Appelons la branche release pour cet exemple **release/fb.**
4. Il est possible qu'il y ait plusieurs projets en cours sur la même base de code. Donc, pour chaque projet, une branche release séparée est créée. Supposons qu'il y ait un autre projet en cours en parallèle. Alors ce projet peut avoir une branche release séparée comme **release/messenger**
5. La raison d'avoir une branche release est que la même base de code peut avoir plusieurs projets en cours en parallèle — il ne devrait y avoir aucun conflit entre les projets.

#### Branche Feature

1. Pour chaque fonctionnalité construite dans l'application, une **branche feature** séparée est créée. Cela garantit que les fonctionnalités peuvent être construites indépendamment
2. La branche feature est comme n'importe quelle autre branche mais avec le préfixe **feature/**
3. Maintenant, en tant que tech lead, vous avez demandé à **Alice** de construire un écran de connexion pour Facebook. Elle crée donc une nouvelle branche feature pour cela. Appelons la branche feature **feature/login.** Alice écrirait tout le code de connexion uniquement dans cette branche feature.
4. La branche feature est généralement créée à partir de la **branche release**
5. Bob a été chargé de construire la page de demande d'"ami". Bob crée donc une branche feature appelée **feature/friendrequest**
6. La tâche de John est de construire le fil d'actualité. John crée donc une branche feature appelée **feature/newsfeed**
7. Tous les développeurs codent dans leurs branches feature individuelles. Jusqu'à présent, tout va bien.
8. Maintenant, supposons qu'Alice a terminé sa tâche et que le code de connexion est prêt. Elle doit envoyer son code à la branche release **release/fb** depuis sa branche feature **feature/login.** Cela se fait via une **pull request.**

#### Pull request

Tout d'abord, une pull request ne doit pas être confondue avec `git pull`.

Le développeur ne peut pas pousser le code directement dans la branche release. Le tech lead doit examiner le code de la **feature** avant qu'il ne soit intégré dans la branche **release**. Cela se fait via une pull request.

Alice peut créer la pull request comme suit dans GitHub — ces étapes sont spécifiques à GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/hITedlsOLA34aFDhyVV1BEISNTkaIzgrtIbE)

Juste à côté du nom de la branche, il y a une option appelée "New pull request". En cliquant dessus, un nouvel écran s'ouvre comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/qkFVwIlr3U1dIk5z86x9-Nko77ew6FGdic3I)

Ici :

* la branche **compare** doit être la branche feature d'Alice **feature/login**
* la branche **base** doit être la branche release **release/fb.**

Une fois cela fait, Alice doit entrer un titre et une description pour la pull request, et enfin cliquer sur "Create Pull Request". Alice doit également assigner un relecteur pour cette pull request. Elle entre **votre nom** en tant que relecteur puisque vous êtes le tech lead.

Le tech lead examine ensuite le code dans la pull request et fusionne le code de la branche **feature** dans la branche **release**

Ainsi, vous avez fusionné le code de la branche **feature/login** vers la branche **release/fb** et Alice est assez heureuse que son code ait été fusionné.

#### Conflits de code.

1. Bob a également terminé son code et a créé une pull request de **feature/friendrequest** vers **release/fb**.
2. Puisque la branche release contient déjà le code de connexion, des **conflits de code** se produisent. Il est de la responsabilité du relecteur de résoudre ces conflits de code et de fusionner le code. Dans ce cas, vous, en tant que tech lead, devez résoudre ces conflits de code et fusionner le code.
3. Maintenant, John a également terminé son code et souhaite ajouter son code à la branche release. Mais John est assez bon pour gérer les conflits de code. John prend le dernier code de la branche **release/fb** dans sa propre branche feature **feature/newsfeed** (soit via `git pull` ou `git merge`). John résout tous les conflits présents. Maintenant, la branche **feature/newsfeed** contient tout le code présent dans **release/fb** également.
4. Enfin, John crée une pull request. Cette fois, il n'y a pas de conflits de code dans la pull request puisque John les a déjà résolus.

Il existe donc **deux façons** de résoudre les conflits de code :

* Première méthode : le relecteur de la pull request doit résoudre les conflits de code.
* Deuxième méthode : le développeur s'assure que le dernier code de la branche release est fusionné dans la branche feature et résout les conflits lui-même.

#### Branche Master à nouveau

Une fois le projet terminé, le code de la branche **release** est fusionné dans la branche **master**. Le code est ensuite déployé en production. Ainsi, le code en production et le code dans la branche master sont toujours synchronisés. Cela garantit également que, pour tout projet futur, le code à jour est disponible dans **master**.

### Références

Plus d'informations sur les pull requests sont [ici](https://help.github.com/articles/creating-a-pull-request/).

### Félicitations ?

Vous savez maintenant comment faire le meilleur usage de Git. Git a d'autres concepts comme l'amendement des commits et le rebasage qui sont également utiles. Mais le **workflow Git** est assez important pour que les grands projets réussissent.

### À propos de l'auteur

J'aime la technologie et je suis les avancées technologiques. J'aime aussi aider les autres avec les connaissances que j'ai dans le domaine de la technologie.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

### Autres articles de moi

[Meilleures pratiques lors de l'utilisation de Git](https://adityasridhar.com/posts/how-you-can-go-wrong-with-git)

[Voici mon introduction à Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61).