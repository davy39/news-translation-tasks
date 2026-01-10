---
title: Comment écrire du code testable | Méthodologie de Khalil
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T17:53:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-testable-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/testable-code.png
tags:
- name: professionalism
  slug: professionalism
- name: React
  slug: reactjs
- name: TypeScript
  slug: typescript
seo_title: Comment écrire du code testable | Méthodologie de Khalil
seo_desc: 'By Khalil Stemmler

  Understanding how to write testable code is one of the biggest frustrations I had
  when I finished school and started working at my first real-world job.

  Today, while I was working on a chapter in solidbook.io, I was breaking down s...'
---

Par Khalil Stemmler

Comprendre comment écrire du code testable est l'une des plus grandes frustrations que j'ai eues lorsque j'ai terminé mes études et que j'ai commencé à travailler à mon premier emploi dans le monde réel.

Aujourd'hui, alors que je travaillais sur un chapitre de [solidbook.io](https://solidbook.io), je décomposais du code et analysais tout ce qui n'allait pas avec lui. Et j'ai réalisé que plusieurs principes régissent la manière dont j'écris du code pour qu'il soit testable.

Dans cet article, je souhaite vous présenter une méthodologie simple que vous pouvez appliquer à la fois au code front-end et back-end pour savoir comment écrire du code testable.

## Lectures préalables

Vous voudrez peut-être lire les articles suivants au préalable. ?

- [Injection de dépendances et inversion expliquées | Node.js avec TypeScript](https://khalilstemmler.com/articles/tutorials/dependency-injection-inversion-explained/)
- [La règle de dépendance](https://khalilstemmler.com/wiki/dependency-rule/)
- [Le principe de dépendance stable - SDP](https://khalilstemmler.com/wiki/stable-dependency-principle/)

## Les dépendances sont des relations

Vous le savez peut-être déjà, mais la première chose à comprendre est que lorsque nous importons ou même mentionnons le nom d'une autre classe, fonction ou variable depuis une classe (appelons cela la classe source), ce qui a été mentionné devient une dépendance pour la classe source.

Dans l'article sur l'inversion et l'injection de dépendances, nous avons examiné un exemple de `UserController` qui avait besoin d'accéder à un `UserRepo` pour obtenir tous les utilisateurs.

```typescript
// controllers/userController.ts

import { UserRepo } from '../repos' // Mauvais

/**
 * @class UserController
 * @desc Responsable de la gestion des requêtes API pour la
 * route /user.
 **/

class UserController {
  private userRepo: UserRepo;

  constructor () {
    this.userRepo = new UserRepo(); // Aussi mauvais.
  }

  async handleGetUsers (req, res): Promise<void> {
    const users = await this.userRepo.getUsers();
    return res.status(200).json({ users });
  }
}
```

Le problème avec cette approche était que lorsque nous faisons cela, nous créons une dépendance de code source difficile.

La relation ressemble à ce qui suit :

![](https://khalilstemmler.com/img/blog/di-container/before-dependency-inversion.svg)

*UserController dépend directement de UserRepo.*

Cela signifie que si nous voulons tester `UserController`, nous devrons également emmener `UserRepo` avec nous. Le problème avec `UserRepo`, cependant, est qu'il apporte également une connexion de base de données complète avec lui. Et ce n'est pas bon.

Si nous devons démarrer une base de données pour exécuter des tests unitaires, cela rend tous nos tests unitaires lents.

En fin de compte, nous pouvons corriger cela en utilisant l'inversion de dépendance, en plaçant une abstraction entre les deux dépendances.

> Les abstractions qui peuvent inverser le flux des dépendances sont soit des interfaces, soit des classes abstraites.

<img style="width: 100%" src="https://khalilstemmler.com/img/blog/di-container/after-dependency-inversion.svg" />

*Utilisation d'une interface pour implémenter l'inversion de dépendance.*


Cela fonctionne en plaçant une abstraction (interface ou classe abstraite) entre la dépendance que vous souhaitez importer et la classe source. La classe source importe l'abstraction et reste testable car nous pouvons passer n'importe quoi qui a adhéré au contrat de l'abstraction, même s'il s'agit d'un objet mock.

```typescript
// controllers/userController.ts

import { IUserRepo } from '../repos' // Bien ! Référence à l'abstraction.

/**
 * @class UserController
 * @desc Responsable de la gestion des requêtes API pour la
 * route /user.
 **/

class UserController {
  private userRepo: IUserRepo; // abstraction ici

  constructor (userRepo: IUserRepo) { // et ici
    this.userRepo = userRepo;
  }

  async handleGetUsers (req, res): Promise<void> {
    const users = await this.userRepo.getUsers();
    return res.status(200).json({ users });
  }
}
```

Dans notre scénario avec `UserController`, il fait maintenant référence à une interface `IUserRepo` (qui ne coûte rien) plutôt qu'à la `UserRepo` potentiellement lourde qui transporte une connexion de base de données partout où elle va.

Si nous souhaitons tester le contrôleur, nous pouvons satisfaire le besoin de `UserController` pour un `IUserRepo` en substituant notre `UserRepo` soutenu par une base de données par une implémentation en mémoire. Nous pouvons en créer une comme ceci :

```typescript
class InMemoryMockUserRepo implements IUserRepo { 
  ... // implémenter les méthodes et propriétés
}
```

## La méthodologie

Voici mon processus de réflexion pour garder le code testable. Tout commence lorsque vous souhaitez créer une relation d'une classe à une autre.

> Début : Vous souhaitez importer ou mentionner le nom d'une classe depuis un autre fichier.

Question : vous souciez-vous de pouvoir écrire des tests contre la classe source à l'avenir ?

Si non, allez-y et importez ce que vous voulez car cela n'a pas d'importance.

Si oui, considérz les restrictions suivantes. Vous pouvez dépendre de la classe uniquement si elle est au moins l'une de ces catégories :

- La dépendance est une abstraction (interface ou classe abstraite).
- La dépendance provient de la même couche ou d'une couche interne (voir [La règle de dépendance](https://khalilstemmler.com/wiki/dependency-rule/)).
- Il s'agit d'une [dépendance stable](https://khalilstemmler.com/wiki/stable-dependency-principle/).

> Si au moins l'une de ces conditions est remplie, importez la dépendance - sinon, ne le faites pas.

L'importation de la dépendance introduit la possibilité qu'il soit difficile de tester le composant source à l'avenir.

Encore une fois, vous pouvez corriger les scénarios où la dépendance enfreint l'une de ces règles en utilisant [l'inversion de dépendance](https://khalilstemmler.com/articles/tutorials/dependency-injection-inversion-explained/).

## Exemple front-end (React avec TypeScript)

Qu'en est-il du développement front-end ?

Les mêmes règles s'appliquent !

Prenons ce composant React (pré-hooks) impliquant un composant conteneur (préoccupation de la couche interne) qui dépend d'un `ProfileService` (couche externe - infra).

```typescript
// containers/ProfileContainer.tsx

import * as React from 'react'
import { ProfileService } from './services'; // dépendance de code source difficile
import { IProfileData } from './models'      // dépendance stable

interface ProfileContainerProps {}

interface ProfileContainerState {
  profileData: IProfileData | {};
}

export class ProfileContainer extends React.Component<
  ProfileContainerProps, 
  ProfileContainerState
> {

  private profileService: ProfileService;

  constructor (props: ProfileContainerProps) {
    super(props);
    this.state = {
      profileData: {}
    }
    this.profileService = new ProfileService(); // Mauvais.
  }

  async componentDidMount () {
    try {
      const profileData: IProfileData = await this.profileService.getProfile();

      this.setState({
        ...this.state,
        profileData
      })
    } catch (err) {
      alert("Ooops")
    }
  }

  render () {
    return (
      <div>Je suis un conteneur de profil</div>
    )
  }
}
```

Si `ProfileService` est quelque chose qui fait des appels réseau à une API RESTful, il n'y a aucun moyen pour nous de tester `ProfileContainer` et de l'empêcher de faire de vrais appels API.

Nous pouvons corriger cela en faisant deux choses :

### 1. Placer une interface entre `ProfileService` et `ProfileContainer`

Tout d'abord, nous créons l'abstraction puis nous nous assurons que `ProfileService` l'implémente.

```typescript
// services/index.tsx
import { IProfileData } from "../models";

// Créer une abstraction
export interface IProfileService { 
  getProfile: () => Promise<IProfileData>;
}

// Implémenter l'abstraction
export class ProfileService implements IProfileService {
  async getProfile(): Promise<IProfileData> {
    ...
  }
}
```

<p class="caption">Une abstraction pour ProfileService sous la forme d'une interface.</p>

Ensuite, nous mettons à jour `ProfileContainer` pour qu'il dépende de l'abstraction à la place.

```typescript
// containers/ProfileContainer.tsx
import * as React from 'react'
import { 
  ProfileService, 
  IProfileService 
} from './services'; // importer l'interface
import { IProfileData } from './models' 

interface ProfileContainerProps {}

interface ProfileContainerState {
  profileData: IProfileData | {};
}

export class ProfileContainer extends React.Component<
  ProfileContainerProps, 
  ProfileContainerState
> {

  private profileService: IProfileService;

  constructor (props: ProfileContainerProps) {
    super(props);
    this.state = {
      profileData: {}
    }
    this.profileService = new ProfileService(); // Toujours mauvais cependant
  }

  async componentDidMount () {
    try {
      const profileData: IProfileData = await this.profileService.getProfile();

      this.setState({
        ...this.state,
        profileData
      })
    } catch (err) {
      alert("Ooops")
    }
  }

  render () {
    return (
      <div>Je suis un conteneur de profil</div>
    )
  }
}
```

### 2. Composer un `ProfileContainer` avec un HOC qui contient un `IProfileService` valide.

Maintenant, nous pouvons créer des HOC qui utilisent n'importe quel type de `IProfileService` que nous souhaitons. Il pourrait s'agir de celui qui se connecte à une API comme suit :

```typescript
// hocs/withProfileService.tsx

import React from "react";
import { ProfileService } from "../services";

interface withProfileServiceProps {}

function withProfileService(WrappedComponent: any) {
  class HOC extends React.Component<withProfileServiceProps, any> {
    private profileService: ProfileService;

    constructor(props: withProfileServiceProps) {
      super(props);
      this.profileService = new ProfileService();
    }

    render() {
      return (
        <WrappedComponent
          profileService={this.profileService}
          {...this.props}
        />
      );
    }
  }
  return HOC;
}

export default withProfileService;
```

Ou il pourrait s'agir d'un mock qui utilise également un service de profil en mémoire.

```typescript
// hocs/withMockProfileService.tsx

import * as React from "react";
import { MockProfileService } from "../services";

interface withProfileServiceProps {}

function withProfileService(WrappedComponent: any) {
  class HOC extends React.Component<withProfileServiceProps, any> {
    private profileService: MockProfileService;

    constructor(props: withProfileServiceProps) {
      super(props);
      this.profileService = new MockProfileService();
    }

    render() {
      return (
        <WrappedComponent
          profileService={this.profileService}
          {...this.props}
        />
      );
    }
  }
  return HOC;
}

export default withProfileService;

```

Pour que notre `ProfileContainer` utilise le `IProfileService` d'un HOC, il doit s'attendre à recevoir un `IProfileService` en tant que prop dans `ProfileContainer` plutôt que d'être ajouté à la classe en tant qu'attribut.

```typescript
// containers/ProfileContainer.tsx

import * as React from "react";
import { IProfileService } from "./services";
import { IProfileData } from "./models";

interface ProfileContainerProps {
  profileService: IProfileService;
}

interface ProfileContainerState {
  profileData: IProfileData | {};
}

export class ProfileContainer extends React.Component<
  ProfileContainerProps,
  ProfileContainerState
> {
  constructor(props: ProfileContainerProps) {
    super(props);
    this.state = {
      profileData: {}
    };
  }

  async componentDidMount() {
    try {
      const profileData: IProfileData = await this.props.profileService.getProfile();

      this.setState({
        ...this.state,
        profileData
      });
    } catch (err) {
      alert("Ooops");
    }
  }

  render() {
    return <div>Je suis un conteneur de profil</div>
  }
}

```

Enfin, nous pouvons composer notre `ProfileContainer` avec le HOC de notre choix - celui contenant le vrai service, ou celui contenant le faux service pour les tests.

```typescript
import * as React from "react";
import { render } from "react-dom";
import withProfileService from "./hocs/withProfileService";
import withMockProfileService from "./hocs/withMockProfileService";
import { ProfileContainer } from "./containers/profileContainer";

// Le vrai service
const ProfileContainerWithService = withProfileService(ProfileContainer);
// Le service mock
const ProfileContainerWithMockService = withMockProfileService(ProfileContainer);

class App extends React.Component<{}, IState> {
  public render() {
    return (
      <div>
        <ProfileContainerWithService />
      </div>
    );
  }
}

render(<App />, document.getElementById("root"));

```

---

Je suis Khalil. Je suis un Developer Advocate @ [Apollo GraphQL](https://www.apollographql.com/docs/?utm_source=khalil&utm_medium=khalil_post_footer&utm_campaign=how_to_write_testable_code). Je crée également des cours, des livres et des articles pour les développeurs en herbe sur Enterprise Node.js, Domain-Driven Design et l'écriture de JavaScript testable et flexible.

Ceci a été initialement publié sur mon blog @ [khalilstemmler.com](https://khalilstemmler.com) et apparaît dans le Chapitre 11 de [solidbook.io - Une introduction à la conception et à l'architecture de logiciels avec Node.js & TypeScript](https://solidbook.io).

Vous pouvez me contacter et me poser des questions sur [Twitter](https://twitter.com/stemmlerjs) !