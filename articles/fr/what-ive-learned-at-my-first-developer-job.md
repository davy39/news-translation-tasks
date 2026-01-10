---
title: J'ai obtenu mon premier emploi de développeur – voici ce que j'ai appris jusqu'à
  présent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-18T00:08:02.000Z'
originalURL: https://freecodecamp.org/news/what-ive-learned-at-my-first-developer-job
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/things-learned-at-first-job-image.jpeg
tags:
- name: career advice
  slug: career-advice
- name: 'Junior developer '
  slug: junior-developer
- name: 'self-improvement '
  slug: self-improvement
seo_title: J'ai obtenu mon premier emploi de développeur – voici ce que j'ai appris
  jusqu'à présent
seo_desc: "By Leonardo Brombilla Antunes\nIn this article, I'm going to share with\
  \ you what I've learned so far at my first programming job as a junior full-stack\
  \ developer. \nEver since my developer career began in July, 2021 I've been learning\
  \ constantly. And I..."
---

Par Leonardo Brombilla Antunes

Dans cet article, je vais partager avec vous ce que j'ai appris jusqu'à présent lors de mon premier emploi de programmeur en tant que développeur full-stack junior. 

Depuis que ma carrière de développeur a commencé en juillet 2021, j'apprends constamment. Et je vais partager quelques conseils tirés de mes expériences afin que vous puissiez apprendre également. 

Dans mon entreprise, je travaille sur des tâches de bout en bout, du front-end au back-end, sur un service qui compte de nombreux utilisateurs.

Très bien, voici les compétences et les conseils que j'ai tirés de cette expérience jusqu'à présent.

## Compétences techniques

J'ai appris beaucoup de compétences techniques (ce que certains pourraient appeler des "compétences techniques") lors de mes premiers mois de travail. Voici les points forts :

### Architecture et modèles de conception

La première chose qui m'a ouvert les yeux était l'architecture avec laquelle je travaille dans mon emploi. Lorsque nous travaillons sur de petits projets, nous pensons rarement à l'architecture – et c'est normal, car nous sommes au début. 

Mais il y a beaucoup à apprendre sur les modèles architecturaux les plus couramment utilisés (comme les [microservices](https://www.freecodecamp.org/news/microservices-architecture-for-humans/), le [modèle MVC](https://www.freecodecamp.org/news/the-model-view-controller-pattern-mvc-architecture-and-frameworks-explained/), l'[architecture serverless](https://www.freecodecamp.org/news/how-to-get-started-with-serverless-architecture/)... la liste est longue). 

Un modèle vraiment intéressant que j'ai appris récemment est le modèle de dépôt (repository pattern). Ce modèle aide à séparer votre application de vos données. 

Pourquoi est-ce utile ? Parce que cela vous permet de changer facilement votre technologie de base de données. Regardez l'exemple ci-dessous pour voir comment cela fonctionne :

```typescript
import {takeLatest, put, call, select} from 'redux-saga/effects';

import {authError, signIn, signOut, signUpSuccess} from '../actions';

import {
  signInWithEmailPasswordFirebase,
  signOutFirebase,
  signUpWithEmailPasswordFirebase,
} from '../repository';

import {
  AuthAction,
  AuthSignInInput,
  AuthSignUpInput,
  AuthTypes,
} from '../types';

import * as authSelectors from '../selectors/index';

export function* requestSignInEmailPasswordSaga(
  props: AuthAction<AuthSignInInput>,
): any {
  const email = props.payload.email;
  const password = props.payload.password;

  try {
    if (email && password) {
      const userCredentials = yield call(
        signInWithEmailPasswordFirebase,
        email,
        password,
      );

      yield put(signIn(userCredentials._user));
    }
  } catch (err: any) {
    yield put(authError('cannot sign In'));
  }
}

export function* requestSignOutSaga(): any {
  try {
    const isLogged = yield select(authSelectors.isLogged);

    if (isLogged) {
      yield call(signOutFirebase);
    }
    yield put(signOut());
  } catch {
    yield put(signOut());
  }
}

export function* requestSignUpEmailPasswordSaga(
  props: AuthAction<AuthSignUpInput>,
): any {
  const email = props.payload.email;
  const password = props.payload.password;

  try {
    if (email && password) {
      yield call(signUpWithEmailPasswordFirebase, email, password);
    }

    yield put(signUpSuccess());
  } catch (err) {
    yield put(authError('cannot sign Up'));
  }
}

export default [
  takeLatest(
    AuthTypes.REQUEST_SIGNIN_EMAIL_PASSWORD,
    requestSignInEmailPasswordSaga,
  ),
  takeLatest(AuthTypes.REQUEST_SIGNOUT, requestSignOutSaga),
  takeLatest(
    AuthTypes.REQUEST_SIGNUP_EMAIL_PASSWORD,
    requestSignUpEmailPasswordSaga,
  ),
];
```

Dans mes sagas, j'appelle certains services mais je ne le fais pas directement à l'intérieur. Je les appelle depuis le dépôt comme vous pouvez le voir :

```typescript
import {firebase} from '@react-native-firebase/auth';

export const signUpWithEmailPasswordFirebase = async (
  email: string,
  password: string,
) => {
  return firebase
    .auth()
    .createUserWithEmailAndPassword(email, password)
    .then(user => console.log(user + 'signed Up'))
    .catch(err => {
      throw new Error(err);
    });
};

export const signOutFirebase = () => {
  firebase.auth().signOut();
};

export const signInWithEmailPasswordFirebase = async (
  email: string,
  password: string,
) => {
  return firebase
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then(user => user.user)
    .catch(err => {
      throw new Error(err);
    });
};
```

Mon dépôt gère tout le contact avec le service Firebase qui récupère mes utilisateurs. Si je décidais de changer Firebase pour une raison quelconque, je n'aurais qu'à changer ce fichier et mes sagas seraient en sécurité. 

Si, en revanche, je décidais d'utiliser un service Firebase dans une autre partie de mon code, je pourrais simplement appeler le service depuis le dépôt sans passer par d'autres endroits. Cette séparation des préoccupations est super utile à long terme. 

Voici le lien vers le projet complet si vous souhaitez explorer davantage :

%[https://github.com/LeoAntunesBrombilla/waterPlant]

Et cet article peut vous aider à en apprendre davantage sur ce modèle :

%[https://medium.com/@erickwendel/generic-repository-with-typescript-and-node-js-731c10a1b98e]

### Gestion de l'état global

Lorsque je travaillais sur mes projets React, je ne connaissais pas la gestion de l'état global et l'architecture Flux. Mais j'ai appris que cela peut être une chose importante à connaître. Vous pouvez en lire plus à ce sujet **[dans cette introduction à l'architecture Flux](https://www.freecodecamp.org/news/an-introduction-to-the-flux-architectural-pattern-674ea74775c9/).**

Redux vous aidera à implémenter cette architecture, mais de nombreuses autres bibliothèques peuvent vous aider à gérer l'architecture Flux – comme Mobx, par exemple. Si vous voulez comprendre l'idée générale de Redux, lisez [ici](https://medium.com/@antunes.b.leonardo/redux-understanding-the-general-idea-cf1d8bda3f0)! Vous pouvez essayer d'apprendre l'une de ces bibliothèques et de construire un projet sur celle-ci. 

Un exemple serait le problème que Facebook a eu il y a quelques années. Ce problème est mieux expliqué dans l'article ci-dessous :

%[https://medium.com/@grover.vinayak0611/what-is-flux-architecture-why-facebook-used-it-and-the-comparison-with-mvc-architecture-49c01ed5d2e1]

### Code propre

Il est vraiment important de livrer un code propre et lisible. Donc si vous pouvez faire cela, vous êtes en avance. 

Il existe de nombreux dépôts qui montrent les meilleures pratiques pour chaque langage, donc vous pouvez rechercher les vôtres et essayer d'écrire votre code comme cela. 

Voici un exemple simple mais important. N'utilisez pas ceci :

```
const a = "Leonardo"
```

Qu'est-ce que `a` ? Le nom de l'auteur ? Le nom de quelqu'un qui vit au Brésil ? Vous ne savez pas parce que personne, à part la personne qui a créé cette variable, ne saura quel est le contexte de cette variable. Et après un certain temps, même la personne qui l'a écrite ne le saura plus. 

Faites donc quelque chose comme ceci à la place :

```
const freeCodeCampColaborator = "Leonardo"
```

Maintenant, vous connaissez le contexte même si je n'écris aucun commentaire. Et il est beaucoup plus facile de rechercher quelque chose comme cela lorsque vous êtes dans un grand monorepo avec plus de 1000 fichiers, par exemple. 

Vous pouvez voir plus d'exemples de bonnes pratiques et de code propre en JavaScript dans le dépôt suivant :

%[https://github.com/ryanmcdermott/clean-code-javascript]

et vérifiez ici pour TypeScript :

%[https://github.com/labs42io/clean-code-typescript]

### Comment apprendre toutes ces compétences ? 

J'ai appris ces compétences en construisant des projets et en demandant des retours à mes collègues. Mais je suggérerais que, même si vous n'avez pas de collègues, vous devriez lire de bons tutoriels et ensuite essayer de construire les projets qui y sont proposés. 

Assurez-vous d'utiliser les technologies que vous essayez d'apprendre. Si vous ne faites que lire et ne construisez pas, vous ne les comprendrez pas pleinement. 

J'ai un projet avec cette approche si vous avez besoin d'une idée plus générale de la façon de le faire :

%[https://github.com/LeoAntunesBrombilla/projetoHitss]

## Compétences non techniques

### Soyez proactif

Si vous travaillez à distance, il est souvent difficile de montrer que vous êtes proactif et productif. Si vous travaillez dans votre premier emploi de développeur, comme moi, demander des choses à faire peut sembler effrayant – mais c'est très gratifiant lorsque vous êtes capable de le faire. 

Même si vous ne pouvez pas le faire ou ne comprenez pas la tâche, demandez de l'aide. C'est normal et super utile également. 

Voici un bon exemple : supposons que vous venez de terminer une tâche et que vous devez maintenant attendre une revue de code ou quelque chose. En attendant, vous pouvez offrir votre aide aux autres, parler à des personnes autres que des développeurs pour en apprendre davantage sur le côté commercial, et documenter certaines difficultés environnementales que vous avez rencontrées lors de votre première tâche afin que les autres puissent en apprendre également. 

### Apprenez à demander de l'aide

L'une des compétences que vous apprendrez en tant que développeur est de savoir poser de meilleures questions. Avant d'être programmeur, j'ai étudié les mathématiques, et en faisant ma thèse de licence, j'ai appris à poser de bonnes questions à mon conseiller. 

Voici l'un de mes principaux conseils : essayez de préciser votre question. 

Si vous posez une question comme : "Je ne connais pas React Native, pouvez-vous m'aider ?" Que pouvez-vous attendre comme réponse ? Si vous ne savez rien, commencez par le googler et trouvez quelques ressources sur le sujet. 

Ensuite, vous pouvez demander à vos collègues qui connaissent la technologie : "Hey, j'essaie d'apprendre React Native et j'ai trouvé ces matériaux – avez-vous des suggestions ? Sont-ils bons ?" 

Un autre exemple : supposons que vous avez reçu une tâche pour centrer une div. Après un certain temps, vous n'avez pas pu le faire et vous voulez demander à quelqu'un de vous aider. Ne demandez pas comme ceci : 

"Hey, j'ai essayé de centrer cette div et je n'ai pas pu le faire – comment cela fonctionne-t-il ?"

Demandez plutôt comme ceci :

"Hey, pour centrer cette div, j'ai essayé cette méthode et cela n'a pas fonctionné à cause de cela, et ensuite j'ai essayé cela .... et ainsi de suite, donc... avez-vous une meilleure approche ?"

Sur le chemin pour poser une bonne question, parfois vous trouverez votre réponse. Les questions génériques et abstraites ne sont pas si bonnes parce qu'elles donnent l'impression que vous abandonnez et demandez de l'aide avant même d'avoir essayé. Si vous avez essayé et que vous ne connaissez toujours pas la réponse, alors allez-y – demandez de l'aide. À mesure que vous gagnez en expérience, vous deviendrez meilleur pour poser des questions. 

### Restez organisé

Si vous n'êtes pas du type Notion, prenez simplement des notes sur ce que vous faites pendant votre journée. Créez un système pour vous souvenir des réunions ou des choses stupides que vous oublierez probablement si vous les laissez uniquement à votre mémoire. 

Si quelqu'un vous demande de faire quelque chose de simple, comme changer une description de tâche de ceci en cela et que vous oubliez parce que vous avez fait confiance à votre esprit déjà occupé, cela ne sera pas bon pour vous. 

Il est donc non seulement important d'avoir un système de notes organisé, mais aussi de s'y tenir. Cela montrera à votre équipe et à votre patron que vous pouvez faire des choses sans que quelqu'un vous surveille 24h/24 et 7j/7. 

La chaîne YouTube de Thomas Frank regorge de conseils utiles pour rester organisé et accomplir les choses. 

%[https://www.youtube.com/watch?v=ODXV-fb_c-I]

## Conclusion

Lorsque vous êtes à votre premier emploi de développeur, vous apprendrez beaucoup de choses qui ne sont pas uniquement liées au code – soyez donc ouvert à cela. Apprenez à utiliser Google et à demander de l'aide ! 

C'est tout ! J'espère que mon expérience vous aide et bon codage :)

Si vous voulez me contacter, vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/leonardo-brombilla/).