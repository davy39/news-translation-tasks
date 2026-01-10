---
title: Comment ajouter Sentry à votre projet Node.js avec TypeScript
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2021-09-28T16:24:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-sentry-to-your-node-js-project-with-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-pixabay-366283.jpg
tags:
- name: error handling
  slug: error-handling
- name: logging
  slug: logging
- name: node js
  slug: node-js
- name: TypeScript
  slug: typescript
seo_title: Comment ajouter Sentry à votre projet Node.js avec TypeScript
seo_desc: "Sentry.io is an external monitoring and logging service which can help\
  \ you identify and triage errors in your code. \nThese logs provide information\
  \ such as a trace stack, breadcrumbs, and (assuming this is a web application) browser\
  \ data. This can he..."
---

Sentry.io est un service externe de surveillance et de journalisation qui peut vous aider à identifier et à trier les erreurs dans votre code. 

Ces journaux fournissent des informations telles qu'une trace de pile, des breadcrumbs et (en supposant que ce soit une application web) des données de navigateur. Cela peut vous aider à trier les problèmes et à résoudre les bugs plus rapidement, avec moins de frais généraux d'investigation.

## Comment préparer votre compte Sentry

Commencez par naviguer vers [Sentry](https://sentry.io) et cliquez sur "Get Started". Vous serez redirigé vers l'écran de création de compte :

![Écran de création de compte de Sentry.](https://www.freecodecamp.org/news/content/images/2021/09/image-83.png)

Vous pouvez soit vous inscrire avec OAuth, soit créer des identifiants séparés pour Sentry. Si vous choisissez de créer des identifiants séparés, vous devrez entrer un nom d'organisation maintenant (celui-ci peut être changé plus tard). J'ai utilisé mon nom d'utilisateur comme nom d'organisation.  
  
Une fois votre compte créé, Sentry vous guidera à travers un tutoriel pour configurer votre premier projet. Cliquez sur "I'm Ready" pour passer à la première étape.

![Écran "Choisissez la plateforme de votre projet" de Sentry](https://www.freecodecamp.org/news/content/images/2021/09/image-84.png)

Pour nos besoins, l'option `NODE.JS` est la plateforme que vous devez sélectionner. Ensuite, cliquez sur "Create Project".

Cela vous amène aux instructions pour préparer le SDK à intégrer avec votre base de code. Laissez cette page ouverte car vous aurez besoin de votre valeur `dsn`.

## Comment utiliser Sentry dans votre code

Votre prochaine étape consiste à installer les packages Sentry nécessaires :

```bash
npm install @sentry/node @sentry/integrations
```

Le package `@sentry/node` est le SDK principal pour votre projet Node.js, et le package `@sentry/integrations` contient un outil que vous utiliserez pour mapper le chemin du fichier.

Vos outils Sentry doivent être chargés le plus tôt possible dans le flux de votre code. Idéalement, cela signifie que vous devez l'initialiser dans le point d'entrée de votre application (c'est-à-dire `index.ts`). 

Commencez par importer les packages :

```ts
import * as Sentry from "@sentry/node";
import { RewriteFrames } from "@sentry/integrations";
```

La première importation charge les outils Sentry-Node, et la seconde vous donne accès à l'intégration `RewriteFrames`. Cette intégration vous permet d'ajuster le chemin de la trace de pile, ce qui est nécessaire pour pointer correctement vers vos fichiers JavaScript compilés.

Maintenant, vous devez instancier le moniteur Sentry et fournir la configuration :

```ts
Sentry.init({
  dsn: process.env.SENTRY_DSN,
  tracesSampleRate: 1.0,
  integrations: [
    new RewriteFrames({
      root: global.__dirname,
    }),
  ],
});
```

Ici, vous avez passé un objet de configuration à la méthode `Sentry.init()` (qui est utilisée pour instancier et initialiser le processus Sentry). Pour décomposer ces options :

* `dsn` est une URL unique utilisée pour connecter votre instance Sentry à votre tableau de bord. Nous explorerons cela un peu plus tard.
* `tracesSampleRate` détermine le pourcentage d'événements que le moniteur doit envoyer au tableau de bord. Une valeur de `1.0` envoie 100 % des événements capturés – mais si vous trouvez cela trop bruyant, vous pouvez réduire ce nombre.
* `integrations` charge les intégrations que vous souhaitez utiliser. Dans ce cas, vous chargez l'option `RewriteFrames` et définissez le chemin `root` pour vos traces de pile sur `global.__dirname` (qui se résout au répertoire à partir duquel vous exécutez votre application).

Ensuite, n'importe où dans votre base de code où vous journalisez des erreurs (comme un bloc `try / catch` ou une chaîne `.catch()`), ajoutez `Sentry.captureException(error)` (en remplaçant `error` par la variable qui représente votre objet d'erreur) pour transmettre cette erreur à votre moniteur Sentry. 

## Comment connecter votre code à votre tableau de bord

De retour sur la page de configuration du projet, vous verrez une valeur d'URL pour l'option `dsn` dans la configuration.

![Exemple d'option sentry, montrant une URL dsn valide.](https://www.freecodecamp.org/news/content/images/2021/09/image-85.png)

**Votre `dsn` doit être traité comme un secret et ne doit pas être partagé avec qui que ce soit.** Vous pouvez y parvenir en l'ajoutant à votre fichier `.env` (attribuez-le à `SENTRY_DSN` pour correspondre à notre configuration de l'étape précédente).

Le `dsn` indique à Sentry où envoyer les erreurs capturées, et le tableau de bord l'utilise pour lier ces erreurs à votre nouveau projet.

> Une note pour les projets front-end :  
> Parce que vous n'avez pas accès à un `.env` sur le front-end, vous devrez exposer votre `dsn` publiquement. Nous verrons comment gérer cela dans la prochaine étape.

Une fois cela configuré, vous pouvez cliquer sur "View a sample event for this SDK" dans les petits caractères en bas de la page Sentry. Cela générera un faux événement d'erreur et vous amènera au tableau de bord.

## Comment configurer votre tableau de bord Sentry

Le site web de Sentry vous proposera une visite rapide du tableau de bord, que vous pouvez suivre si vous le souhaitez, ou vous pouvez la sauter et continuer avec cet article.

![La moitié supérieure du tableau de bord Sentry](https://www.freecodecamp.org/news/content/images/2021/09/image-86.png)

![La moitié inférieure du tableau de bord Sentry](https://www.freecodecamp.org/news/content/images/2021/09/image-87.png)

Cette vue vous montre les détails spécifiques d'un événement d'erreur capturé. Dans ce cas, il s'agit de l'événement d'exemple généré par Sentry à l'étape précédente.

La moitié supérieure offre des informations telles que les données du navigateur de l'utilisateur qui a déclenché l'erreur, le message d'erreur et le type d'erreur. La moitié inférieure fournit la trace de pile et les breadcrumbs (actions qui ont eu lieu pour déclencher cette erreur) – tous deux utiles pour reproduire cette erreur lors du triage.

Tout en haut, vous devriez voir le nom de votre projet (qui par défaut est le nom de votre organisation) et un engrenage. Cliquez sur cet engrenage pour accéder aux paramètres de votre projet.

![Les paramètres du projet Sentry](https://www.freecodecamp.org/news/content/images/2021/09/image-89.png)

Ici, vous voyez certaines configurations pour votre projet. Le "Nom" détermine le nom de votre projet. Changer la "Plateforme" affecte la manière dont les traces de pile sont rendues. Vous êtes libre d'expérimenter avec les autres paramètres selon vos besoins.

> Pour les projets front-end :  
> Comme mentionné précédemment, vous devrez exposer votre DSN publiquement. Vous pouvez définir l'URL de votre page web dans les "Domaines autorisés" pour empêcher l'envoi de données depuis toute autre source.

Dans la barre latérale se trouvent quelques options supplémentaires. La sélection de "Client Keys(DSN)" vous amènera à une page où vous pourrez copier votre DSN à nouveau, si nécessaire. Vous pouvez également le supprimer et le régénérer si vous l'avez accidentellement exposé.

La sélection de "Alertes" vous permettra de configurer la manière dont vous recevez les notifications pour les événements d'erreur. J'ai configuré les miennes pour les envoyer à un [Discord Webhook](https://github.com/nhcarrigan/discord-integrations), mais vous pouvez configurer un certain nombre d'options d'intégration pour recevoir vos alertes.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-91.png)

Enfin, vous avez la barre latérale principale. Ici, vous pouvez configurer les paramètres de votre organisation, y compris le renommage de votre organisation ou la création d'organisations et de projets supplémentaires.

## Conclusion

Vous avez maintenant intégré avec succès Sentry à votre projet Node.js-TypeScript. Vous êtes maintenant prêt à commencer à recevoir des informations sur les erreurs, à trier les problèmes et à améliorer la stabilité de votre projet. 

N'hésitez pas à expérimenter avec les paramètres et les fonctionnalités de Sentry pour personnaliser votre expérience selon vos besoins. Bon codage !