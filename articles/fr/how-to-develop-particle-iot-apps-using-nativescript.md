---
title: Comment développer des applications IoT Particle en utilisant NativeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T17:42:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-particle-iot-apps-using-nativescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/NativeScript
seo_title: Comment développer des applications IoT Particle en utilisant NativeScript
---

Particle.png
étiquettes:
- name: iot
  slug: iot
- name: mobile
  slug: mobile
- name: NativeScript
  slug: nativescript
- name: particle
  slug: particle
seo_title: null
seo_desc: 'Par Jared Wolff

Si vous développez un produit IoT, vous aurez inévitablement besoin d'une application mobile. Bien qu'il existe des moyens faciles, ils ne sont pas adaptés à une utilisation en production.

Dans ce tutoriel, nous allons parler des bases du développement d'applications Particle. Vous apprendrez quelques-uns des nombreux frameworks d'applications que vous pouvez utiliser. De plus, il y a des bibliothèques, des astuces et des outils pour vous faciliter la vie.

## Frameworks d'applications

Parfois, il est vraiment irritant de programmer plusieurs applications nativement. Vous voyez, Swift (ou Objective C ?) et Java ne sont pas si terribles à première vue (bien, peut-être sauf pour Obj-C ?). Mais lorsque vous êtes limité en ressources, vous devez trouver un nouveau plan. C'est là que les frameworks d'applications entrent en jeu.

Ces frameworks permettent à un développeur d'applications d'écrire, de construire et de tester des applications multiplateformes. Dans certains cas, les frameworks convertissent votre application en code natif. Cela signifie qu'ils s'exécutent aussi rapidement et aussi bien qu'une application écrite en Swift ou Java.

J'ai fait des recherches et, en janvier 2020, voici quelques-uns des frameworks les plus supportés :

* [Framework7](https://github.com/framework7io/framework7)
* [Flutter](https://flutter.dev/)
* [NativeScript](https://www.nativescript.org/)
* [ReactNative](https://github.com/facebook/react-native)
* [Ionic](https://github.com/ionic-team/ionic)
* [Cordova](https://cordova.apache.org/) / [PhoneGap](https://phonegap.com/)
* [Meteor](https://github.com/meteor/meteor)
* [Xamarin](https://dotnet.microsoft.com/apps/xamarin)

La liste est longue.

J'ai utilisé quelques-uns de ces frameworks par le passé. J'ai construit une application Meteor qui (étonnamment) a fonctionné. À la fin, j'ai dû en choisir un. Lequel ai-je choisi ?

**NativeScript.**

Pour la plupart, la documentation et l'expérience d'intégration de NativeScript sont fantastiques. Non seulement vous pouvez prévisualiser votre application dans un émulateur, mais vous pouvez également la charger directement sur votre téléphone !

![images/Apple_iPhone_6s_Gold_-__status-b1ad9325-8e81-4ee0-b72a-687b62adec29.png](https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/images/Apple_iPhone_6s_Gold_-__status-b1ad9325-8e81-4ee0-b72a-687b62adec29.png)

L'une des choses intéressantes à propos de NativeScript est qu'il supporte TypeScript. TypeScript est un sur-ensemble de JavaScript avec quelques fonctionnalités supplémentaires. 

Contrairement à d'autres langages, JavaScript n'a techniquement pas de types. Si vous avez fait du développement Particle, vous savez probablement ce qu'est un type. Nous parlons de `int`, `String`, `float` et plus. C'est-à-dire qu'ils sont des directives pour s'assurer que votre code JavaScript reste cohérent.

NativeScript est également compatible avec la plupart des principaux frameworks web JavaScript. Cela inclut [Vue.Js](https://vuejs.org/) et [Angular](https://angular.io/).

J'ai remarqué un inconvénient majeur jusqu'à présent : le mode de prévisualisation mobile (`tns preview`) ne fonctionne pas bien avec les bibliothèques natives. Si vous avez des bibliothèques spécifiques à une plateforme native, vous devrez utiliser l'émulateur ou un appareil (si vous en avez un).

Si vous êtes déterminé et que vous voulez construire plusieurs applications dans leurs langages respectifs, alors tant mieux pour vous. Il y a un avantage par rapport aux frameworks ci-dessus : les SDK Particle éprouvés.

## Bibliothèques et SDK disponibles

Particle a fait des efforts pour faciliter le développement d'applications. Cela est dû au travail de développement massif qui a été effectué sur leurs propres SDK. Oui, les jours où vous deviez écrire des gestionnaires de requêtes HTTP manuels sont révolus.

Voici un lien vers les SDK iOS et Android :

* [iOS](https://docs.particle.io/reference/SDKs/ios/)
* [Android](https://docs.particle.io/reference/SDKs/android/)

Bien que nous ne les couvrirons pas ici, ils reflètent tous les appels potentiels que vous pouvez faire en utilisant l'[API Cloud](https://docs.particle.io/reference/device-cloud/api/).

En parlant de l'API Cloud, Particle a également développé une bibliothèque [Node.js](https://docs.particle.io/reference/device-cloud/api/). Comme vous pouvez l'imaginer, vous pouvez l'utiliser pour votre code côté serveur ou vos frameworks d'applications basés sur JavaScript. Malheureusement, elle ne fonctionne pas avec NativeScript. Les frameworks qui utilisent un [WebView](https://www.tutorialspoint.com/android/android_webview_layout.htm) devraient être plus compatibles.

Dans le cas de ce tutoriel, nous nous concentrerons principalement sur l'API Cloud. Ainsi, vous aurez une bonne compréhension du système global. Cela peut sembler intimidant, mais si vous le faites correctement, vous vous y habituerez rapidement.

## Faire des appels API

Dans NativeScript, vous ne pouvez pas utiliser de bibliothèques comme `[request](https://github.com/request/request)`. (Ce qui se trouve être la bibliothèque que le propre [DMC](https://github.com/dmiddlecamp) de Particle a utilisée dans le [CLI](https://github.com/particle-iot/particle-cli) — DMC, si vous lisez ceci, salut !) Vous devrez utiliser le module [HTTP](https://docs.nativescript.org/ns-framework-modules/http) fourni. 

Si vous faites défiler jusqu'en bas de [cette page](https://docs.nativescript.org/ns-framework-modules/http#http-post), vous verrez un exemple complet de `POST`. Je vais le reproduire ici mais avec quelques modifications spécifiques à Particle :

```typescript
// Créer des données de formulaire
var data = new FormData();
data.append("name", "update");
data.append("data", "It's hammer time!");
data.append("private", "true");
data.append("access_token", _token);

// Configurer le module http
return httpModule
    .request({
        url: `https://api.particle.io/v1/devices/events`,
        method: "POST",
        content: data
    })
    .then(
        response => {
            const result = response.content.toJSON();
            console.log(result);
        },
        e => {
            if (e) console.log(e);
        }
    );

```

L'exemple ci-dessus est équivalent à `Particle.publish` dans DeviceOS. Décomposons les parties.

Tout d'abord, l'un des principaux pièges de l'API Web de Particle est le format des données. Je m'attendais d'abord à ce qu'ils utilisent JSON, mais j'avais tort. Après avoir lu la documentation, j'ai réalisé que la plupart des requêtes POST étaient en fait `application/x-www-form-urlencoded`. Cela signifie que lorsque vous soumettez des données, c'est l'équivalent d'appuyer sur le bouton de soumission d'un formulaire HTML.

Heureusement, il existe un moyen facile d'assembler les données de formulaire en Node/JavaScript. Nous pouvons utiliser l'objet `FormData()`. Jetez un œil à l'exemple ci-dessus. Il devrait y avoir quelques noms de paramètres familiers dans les appels `data.append`.

`"name"` fait référence au nom de l'événement que vous publiez.

`"data"` fait référence aux données formatées en chaîne que vous publiez.

`"private"` dicte si vous voulez diffuser ces données à tout le monde Particle ou juste à votre petit coin.

`"access_token"` est un jeton que vous pouvez générer afin de faire ces appels API. Sans jeton, vous êtes dans l'impasse.

### Obtenir un jeton

Où obtenons-nous ce `access_token` insaisissable ?

Au début, je n'en avais aucune idée.

J'ai créé un utilisateur OAuth et un secret dans la console. Cela a conduit à une impasse. J'ai bidouillé avec différents appels API et paramètres. Rien. Puis cela m'a frappé comme une tonne de briques. Il y a un `access_token` attaché à la requête curl sur chaque page de périphérique !

Ouvrez n'importe quel périphérique, cliquez sur le petit bouton de console près de _Events_. Une fenêtre contextuelle avec des instructions et une URL apparaîtra. Copiez le texte après `access_token=`. C'est votre `access_token` ! Voir ci-dessous :

![images/Screen_Shot_2020-01-25_at_8.55.21_AM.png](https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/images/Screen_Shot_2020-01-25_at_8.55.21_AM.png)

Vous pouvez utiliser ce jeton pour faire des appels à l'API Particle. Cela peut être pour vous abonner, publier, écrire dans une fonction, lire des variables et plus.

### Via la ligne de commande

C'est bien et tout, mais comment pouvez-vous générer un jeton de manière _programmatique_ ? Une façon est via la ligne de commande.

`particle token create` est le nom de la commande que vous devez connaître. Lorsque vous l'exécutez, vous serez invité à vous connecter. (Entrez également votre code d'authentification si vous en utilisez un.) Ensuite, la ligne de commande générera un tout nouveau `access_token` que vous pouvez utiliser avec l'API !

### Via l'API elle-même

Si vous ne l'aviez pas deviné, `particle token create` est un [frontend pour un appel API brut](https://github.com/particle-iot/particle-cli/blob/20d02afc7b72ade0e79d4f4ec724ec6cce9fff1b/src/lib/api-client.js#L192). Vous pouvez faire ces appels API directement aussi. Voici à quoi cela ressemble dans NativeScript.

```typescript
// Créer des données de formulaire
var data = new FormData();
data.append("username", "jaredwolff");
data.append("password", "this is not my password");
data.append("grant_type", "password");
data.append("client_name", "user");
data.append("client_secret", "client_secret_here");

// Configurer le module http
return httpModule
    .request({
        url: `https://api.particle.io/v1/oauth/token`,
        method: "POST",
        content: data
    })
    .then(
        response => {
            const result = response.content.toJSON();
            console.log(result);
        },
        e => {
            if (e) console.log(e);
        }
    );

```

Cet appel _peut_ devenir plus compliqué. Principalement dans le cas où vous avez une authentification à deux facteurs. Cela en vaut la peine lorsque vous avez tout compris. Après tout, personne ne veut créer manuellement des jetons d'authentification s'il n'y est pas obligé !

Maintenant, vous êtes prêt à écrire et à lire depuis vos périphériques. Il y a une chose cependant qui pourrait vous poser problème. S'abonner à des événements peut être problématique avec un client HTTP régulier. Tellement que si vous essayez de le faire avec le client HTTP de NativeScript, il se bloquera et ne retournera jamais. Heureusement, il existe un moyen de gérer ces appels HTTP spéciaux.

## Server Sent What?

Les événements envoyés par le serveur (SSE pour Server Sent Events) sont une fonctionnalité d'abonnement HTTP/S. Ils vous permettent de vous connecter à un point de terminaison SSE et d'écouter en continu les mises à jour. C'est une technologie web similaire à celle utilisée par les entreprises pour les notifications push. Cela nécessite cependant quelques fonctionnalités supplémentaires sous le capot...

### Bibliothèque SSE

Après beaucoup de grattements de tête et de recherches, je suis tombé sur `nativescript-sse`. Cela semblait suffisamment simple pour que je puisse commencer à l'utiliser immédiatement. Plus de problèmes sont apparus lorsque j'ai essayé de l'utiliser.

Tout d'abord, il s'avère que vous ne pouvez pas utiliser la bibliothèque en mode `tns preview`. L'alternative est d'utiliser `tns run ios --emulator` ou d'utiliser `tns run ios` avec votre iPhone connecté à votre ordinateur. La commande non-émulateur livrera automatiquement votre application prototype.

**Note de côté :** J'avais déjà configuré mon téléphone dans Xcode. Vous devrez peut-être faire cela vous-même avant que `tns run ios` puisse trouver et déployer sur votre téléphone.

Deuxièmement, une fois que j'ai fait fonctionner la bibliothèque, j'ai remarqué que j'obtenais des erreurs très désagréables. Les erreurs semblaient se produire chaque fois qu'un nouveau message de Particle arrivait. 

Il s'avère que la bibliothèque Swift sous-jacente pour iOS [avait corrigé cela l'année dernière](https://github.com/inaka/EventSource/issues/89). J'ai donc pris sur moi de comprendre comment mettre à niveau le plugin NativeScript. Je vous épargne le temps de dire que cela peut être un casse-tête et qu'il y a une courbe d'apprentissage !

Heureusement, après quelques bidouillages, j'ai obtenu quelque chose qui fonctionne. Plus d'instructions sur la façon de compiler le plugin sont dans le [README](https://github.com/jaredwolff/nativescript-sse). Alternativement, vous pouvez télécharger une version pré-compilée sur la [page des versions du dépôt](https://github.com/jaredwolff/nativescript-sse/releases/tag/v4.0.3).

Téléchargez le fichier `.tgz` où vous le souhaitez. Ensuite, vous pouvez l'ajouter en utilisant `tns plugin add`. La commande complète ressemble à ceci :

```
tns plugin add path/to/plugin/file.tgz

```

Vous pouvez vérifier que la bibliothèque est installée en exécutant `tns plugin list`

```
**jaredwolff$ tns plugin list
Dependencies:
[38;5;208m┌─────────────────────────────────────────────────────────────────────────────┐
[39m[38;5;208m│ Plugin              │ Version                                                                          │
[39m[38;5;208m├─────────────────────────────────────────────────────────────────────────────┤
[39m[38;5;208m│ @nativescript/theme │ ~2.2.1                                                                           │
[39m[38;5;208m│ nativescript-sse    │ file:../../Downloads/nativescript-sse/publish/package/nativescript-sse-4.0.3.tgz │
[39m[38;5;208m│ tns-core-modules    │ ~6.3.0                                                                           │
[39m[38;5;208m└─────────────────────────────────────────────────────────────────────────────┘
Dev Dependencies:
[38;5;208m┌─────────────────────────────────────────────────────────────────────────────┐
[39m[38;5;208m│ Plugin                   │ Version │
[39m[38;5;208m├─────────────────────────────────────────────────────────────────────────────┤
[39m[38;5;208m│ nativescript-dev-webpack │ ~1.4.0  │
[39m[38;5;208m│ typescript               │ ~3.5.3  │
[39m[38;5;208m└─────────────────────────────────────────────────────────────────────────────┘
NOTE:
If you want to check the dependencies of installed plugin use npm view <pluginName> grep dependencies
If you want to check the dev dependencies of installed plugin use npm view <pluginName> grep devDependencies**

```

Une fois installée, l'invocation de la bibliothèque prend quelques étapes. Voici un exemple :

```typescript
import { SSE } from "nativescript-sse";

sse = new SSE(
            "https://api.particle.io/v1/events/blob?access_token=<votre jeton d'accès>",
            {}

// Ajouter un écouteur d'événement
sse.addEventListener("blob");

// Ajouter un rappel
sse.events.on("onMessage", data=>{
	// TODO: faire des choses avec vos données d'événement ici !
	console.log(data);
});

// Se connecter si ce n'est pas déjà fait
sse.connect();

```

Tout d'abord, vous devez importer et créer une instance de la bibliothèque. Lorsque vous créez l'instance, vous devrez entrer l'URL que vous souhaitez utiliser. 

Dans ce cas, nous ferons l'équivalent de `Particle.subscribe()`. Cela devrait ressembler à quelque chose comme ceci : `https://api.particle.io/v1/events/<nom de votre événement>?access_token=<votre jeton d'accès>`. 

Remplacez `<nom de votre événement>` et `<votre jeton d'accès>` par le nom de votre événement et votre jeton nouvellement créé !

Ensuite, vous configurez la bibliothèque pour écouter l'événement qui vous intéresse. Dans ce cas, `blob` est l'événement qui m'intéresse le plus.

Ensuite, assurez-vous de configurer un rappel ! Ainsi, vous pouvez accéder aux données lorsque `blob` arrive. J'ai fait une note `TODO` où vous pouvez accéder auxdites données.

Enfin, vous pouvez vous connecter en utilisant la méthode `.connect()`. Si vous ne vous connectez pas, SSE n'ouvrira pas de session et vous ne recevrez aucune donnée de Particle.

Le placement du code vous appartient, mais d'après les exemples, il semble que dans le `constructor()` de votre modèle soit un bon endroit.([https://github.com/jaredwolff/nativescript-sse/blob/master/demo/app/main-view-model.ts](https://github.com/jaredwolff/nativescript-sse/blob/master/demo/app/main-view-model.ts))

### Autres exemples

Si vous êtes curieux de savoir comment utiliser SSE dans d'autres endroits, j'ai un autre excellent exemple : le CLI de Particle.

Particle utilise la bibliothèque `[request](https://github.com/request/request)` pour gérer les événements SSE dans l'application. Chaque fois que vous appelez `particle subscribe blob`, cela invoque un `getStreamEvent` plus loin dans le code. Vous pouvez [le vérifier ici](https://github.com/particle-iot/particle-cli/blob/master/src/lib/api-client.js#L862). La bibliothèque `request` a plus d'informations sur le streaming [ici](https://github.com/request/request#streaming).

## Plus de ressources

Ce n'est que la partie émergée de l'iceberg en ce qui concerne la connexion à l'API de Particle. Particle a une excellente documentation (comme toujours) que vous pouvez consulter. Voici quelques liens importants :

* [Documentation de l'API](https://docs.particle.io/reference/device-cloud/api/)
* [SDK JavaScript](https://docs.particle.io/reference/SDKs/javascript/)
* [SDK iOS](https://docs.particle.io/reference/SDKs/ios/)
* [SDK Android](https://docs.particle.io/reference/SDKs/android/)

## Conclusion

Dans cet article, nous avons parlé des frameworks d'applications, de NativeScript, des plugins NativeScript et des événements envoyés par le serveur. Plus toutes les choses liées à Particle afin que vous puissiez connecter votre application NativeScript à l'API de Particle. 

J'espère que vous avez trouvé ce tutoriel rapide utile. Si vous avez des questions, n'hésitez pas à laisser un commentaire ou [m'envoyer un message](https://www.jaredwolff.com/contact/). Assurez-vous également de consulter mon [guide nouvellement publié](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh/). Il contient du contenu comme celui-ci sur l'écosystème de Particle.

À la prochaine !

**Cet article provient à l'origine de** [**https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/**](https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/)