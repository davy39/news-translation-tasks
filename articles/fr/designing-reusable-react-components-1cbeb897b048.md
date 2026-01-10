---
title: Concevoir des composants React réutilisables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-30T17:10:37.000Z'
originalURL: https://freecodecamp.org/news/designing-reusable-react-components-1cbeb897b048
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CByHyzJRQR6G8aiAkdFwcQ.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Concevoir des composants React réutilisables
seo_desc: 'By Cory House

  What Legos Can Teach Us About Reuse in React Apps

  React is a component library. So React makes it easy to break your UI down into
  composable pieces. The question is, how granular should the pieces be?

  Let’s consider a specific example t...'
---

Par Cory House

#### Ce que les Legos peuvent nous apprendre sur la réutilisation dans les applications React

React est une bibliothèque de composants. Ainsi, React facilite la décomposition de votre interface utilisateur en pièces composables. La question est, [à quel niveau de granularité ces pièces doivent-elles être](http://sethgodin.typepad.com/seths_blog/2017/12/granularity.html) ?

Considérons un exemple spécifique que j'ai exploré dans un [précédent article](https://medium.freecodecamp.org/reusable-web-application-strategies-d51517ea68c8).

Imaginez que votre équipe vient de déployer une application ToDo, construite en React. Un mois plus tard, une autre équipe de votre entreprise souhaite exécuter votre application ToDo dans leur application de facturation, également construite en React.

Ainsi, vous devez maintenant exécuter votre application ToDo dans deux endroits :

1. Seule
2. Intégrée dans l'application de facturation

Quelle est la meilleure façon de gérer cela ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*S3wRzzFKKlls9bTlSpFfKA.png)

Pour exécuter votre application React dans plusieurs endroits, vous avez trois options :

1. **iframe** — Intégrez l'application todo dans l'application de facturation via une balise <iframe>.
2. **Composant d'application réutilisable** — Partagez l'ensemble de l'application todo via npm.
3. **Composant d'interface utilisateur réutilisable** — Partagez le balisage de l'application todo via npm.

Discutons des mérites de chaque approche.

### Approche 1 : iFrame

L'approche la plus facile et la plus évidente est d'utiliser une [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) pour intégrer l'application ToDo dans l'application de facturation.

Mais cela conduit à plusieurs problèmes :

1. Si les deux applications affichent les mêmes données, elles risquent de se désynchroniser.
2. Si les deux applications utilisent les mêmes données, vous finissez par faire des appels API redondants pour récupérer les mêmes données.
3. Vous ne pouvez pas personnaliser le comportement de l'application intégrée dans l'iframe.
4. Si une équipe différente possède l'application intégrée, lorsque cette équipe déploie en production, vous êtes instantanément affecté.

En résumé : Évitez les iframes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w0YcpMhPGBRBeQ25G9g-iA.jpeg)
_Non._

### Approche 2 : Composant d'application réutilisable

Partager votre application via npm au lieu d'une iframe évite le problème #4 ci-dessus, mais les autres problèmes persistent. L'API, l'authentification et le comportement sont tous intégrés. Je ne recommande donc pas non plus de partager des applications complètes via npm. Le niveau de granularité est trop élevé, ce qui nuit à l'expérience utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tjvQ8XV65JcxIETD53CNDg.jpeg)
_Comme les blocs Lego, les composants React réutilisables doivent être granulaires et composables._

### Approche 3 : Composants d'interface utilisateur réutilisables

Je recommande une approche plus granulaire utilisant deux blocs de construction flexibles :

1. Des composants React "stupides" (uniquement l'interface utilisateur. Pas d'appels API à l'intérieur.)
2. Des enveloppes d'API

Les composants React "stupides" sont configurables, non opinés et composables. Ils sont réutilisables dans l'interface utilisateur. Lorsque vous consommez un composant "stupide" comme celui-ci, vous êtes libre de fournir les données pertinentes ou de spécifier les appels API que l'application doit effectuer.

Cependant, si vous allez composer des composants "stupides", vous devez configurer les mêmes appels API pour plusieurs applications. C'est là que les enveloppes d'API deviennent utiles. Qu'est-ce qu'une enveloppe d'API ? C'est un fichier JavaScript rempli de fonctions qui effectuent des appels HTTP à votre API. Mon équipe crée des enveloppes d'API. Nous utilisons [Axios](https://github.com/axios/axios) en arrière-plan pour effectuer les appels HTTP.

Imaginez que vous avez une API utilisateur. Voici comment créer une enveloppe d'API utilisateur :

1. Créez un fichier JS avec des fonctions publiques comme getUserById, saveUser, etc. Chaque fonction accepte les paramètres pertinents et utilise Axios/Fetch pour effectuer des appels HTTP à votre API.
2. Partagez l'enveloppe en tant que package npm appelé userApi.

Voici un exemple.

```js
/* Cette enveloppe d'API est utile car elle :
   1. Centralise notre configuration par défaut d'Axios.
   2. Abstrait la logique pour déterminer la baseURL.
   3. Fournit une liste claire et facilement consommable de fonctions JavaScript
      pour interagir avec l'API. Cela garde les appels API courts et cohérents. 
*/
import axios from 'axios';

let api = null;

function getInitializedApi() {
  if (api) return api; // retourne l'API initialisée si déjà initialisée.
  return (api = axios.create({
    baseURL: getBaseUrl(),
    responseType: 'json',
    withCredentials: true
  }));
}

// Fonctions d'aide
function getBaseUrl() {
  // Insérez la logique ici pour obtenir la baseURL en soit :
  // 1. En analysant l'URL pour déterminer l'environnement dans lequel nous exécutons.
  // 2. En cherchant une variable d'environnement dans le cadre du processus de construction.
}

function get(url) {
  return getInitializedApi().get(url);
}

function post(url, data) {
  return getInitializedApi().post(url, data);
}

// Fonctions publiques
// Remarquez à quel point celles-ci sont courtes grâce à la configuration centralisée et aux helpers ci-dessus. ?
export function getUserById(id) {
  return get(`user/${id}`);
}

export function saveUser(user) {
  return post(`user/${user.id}`, {user: user});
}
```

Dans mon équipe, nous partageons nos composants React et nos enveloppes d'API en tant que [packages privés sur npm](https://www.npmjs.com/pricing), mais [Artifactory](https://jfrog.com/artifactory/) est une bonne alternative.

Ces blocs Lego nous donnent la base pour construire rapidement de nouvelles solutions à partir de pièces réutilisables.

> Un système hautement composable fournit des composants qui peuvent être sélectionnés et assemblés dans diverses combinaisons pour satisfaire des exigences utilisateur spécifiques. — [Wikipedia](https://en.wikipedia.org/wiki/Composability)

Ainsi, idéalement, votre composant d'interface utilisateur réutilisable "stupide" est composé [d'autres composants réutilisables, également partagés sur npm](https://app.pluralsight.com/library/courses/react-creating-reusable-components/table-of-contents) !

Avec des composants React réutilisables et des enveloppes d'API publiés sur npm, il est trivial de construire quelque chose d'extraordinaire.

C'est comme assembler des pièces Lego. ?

%[https://www.youtube.com/watch?v=Ki2C05my2K4&feature=youtu.be]

J'explore les mérites et les inconvénients des approches ci-dessus plus en détail [ici](https://medium.freecodecamp.org/reusable-web-application-strategies-d51517ea68c8). Et j'ai récemment publié un cours complet sur [Créer une bibliothèque de composants React réutilisables sur Pluralsight](http://bit.ly/legoreactps). ?

Avez-vous une approche différente que vous préférez ? Partagez-la via les commentaires.

### Vous cherchez plus d'informations sur React ? ⚒️

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight ([essai gratuit](http://bit.ly/pstrialimmutablepost)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel, MVP Microsoft, et forme des développeurs logiciels à l'international sur les pratiques de développement front-end. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).