---
title: 'Comment fonctionnent les Microfrontends : des iframes à la Fédération de Modules'
subtitle: ''
author: Rahul gupta
co_authors: []
series: null
date: '2025-05-30T14:46:01.285Z'
originalURL: https://freecodecamp.org/news/how-microfrontends-work-iframes-to-module-federation
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748613557891/39037981-d514-4f26-8a48-be0cdd9ca29b.png
tags:
- name: frontend
  slug: frontend
- name: architecture
  slug: architecture
- name: JavaScript
  slug: javascript
- name: Microfrontend
  slug: microfrontend
- name: Web Development
  slug: web-development
- name: Frontend Development
  slug: frontend-development
seo_title: 'Comment fonctionnent les Microfrontends : des iframes à la Fédération
  de Modules'
seo_desc: 'Microfrontends are transforming how teams build and deploy frontend applications
  at scale. This tutorial explores the architectural landscape, from traditional approaches
  to modern Module Federation implementations.

  By the end, you''ll be equipped to ...'
---

Les microfrontends transforment la manière dont les équipes construisent et déploient des applications frontend à grande échelle. Ce tutoriel explore le paysage architectural, des approches traditionnelles aux implémentations modernes de la Fédération de Modules.

À la fin, vous serez équipé pour évaluer si les microfrontends sont la bonne solution pour les besoins spécifiques de votre équipe.

### **Je couvrirai les points suivants :**

* [Qu'est-ce que les Microfrontends ?](#heading-quest-ce-que-les-microfrontends)
    
* [Modèles Traditionnels de Microfrontends](#heading-modeles-traditionnels-de-microfrontends)
    
    * [Composition Côté Serveur](#heading-composition-cote-serveur)
        
    * [iframes](#heading-iframes)
        
    * [Intégration à la Construction – Packages](#heading-integration-a-la-construction-packages)
        
* [Modèles Modernes de Microfrontends](#heading-modeles-modernes-de-microfrontends)
    
    * [Fédération de Modules](#heading-federation-de-modules)
        
    * [Single SPA](#heading-single-spa)
        
* [Comparaison Détaillée](#heading-comparaison-detaillée)
    
* [Compromis et Défis avec la Fédération de Modules](#heading-compromis-et-defis-avec-la-federation-de-modules)
    
    * [Complexité de Configuration](#heading-complexite-de-configuration)
        
    * [Défis d'Exécution](#heading-defis-dexecution)
        
    * [Préoccupations Opérationnelles](#heading-preoccupations-operationnelles)
        
* [Conclusions](#heading-conclusions)
    
    * [Qu'est-ce qui suit ?](#heading-quest-ce-qui-suit)
        

## Qu'est-ce que les Microfrontends ?

Si vous avez entendu parler des microservices côté backend, les microfrontends représentent une approche similaire dans le monde du frontend, avec de nombreux avantages similaires.

Votre équipe pourrait adopter une approche de microfrontend pour permettre l'autonomie de l'équipe, réduire les risques de déploiement et mettre à l'échelle le développement entre plusieurs équipes. Chaque équipe possède sa propre stack technologique, son rythme de déploiement et ses flux de travail. Pourtant, elles livrent toujours une seule interface utilisateur cohésive.

L'idée générale est de s'éloigner d'une grande UI monolithique vers des bases de code UI découplées qui peuvent être possédées, gérées et déployées par des équipes séparées de manière indépendante.

La manière la plus simple de penser aux Microfrontends est la suivante :

> Intégrer une partie de l'UI dans une autre

Que peut être cette **partie** d'UI, pourriez-vous demander ? Voici quelques exemples :

* **Pages** – parties d'un site web possédées par des équipes spécifiques. Par exemple, l'équipe Auth peut posséder les pages de connexion/inscription, tandis que l'équipe engagement peut posséder les pages marketing, et ainsi de suite.
    
* **Composants** – Les composants comme l'en-tête et le pied de page sont de bons candidats pour une approche de microfrontend. Ils sont relativement statiques mais doivent rester cohérents sur l'ensemble du site web et peuvent s'intégrer avec des équipes qui possèdent différents ensembles de pages.
    
* **Widgets** – Un widget de recommandation peut être possédé par une équipe de recommandations, par exemple, et il peut être intégré dans différentes parties de la page en fonction du contexte. Cela est différent d'un composant statique, car, étant donné le contexte, le widget de recommandation peut également récupérer des données pertinentes via des APIs (également possédées par les équipes de recommandations).
    

## Modèles Traditionnels de Microfrontends

Après avoir lu la définition d'un microfrontend, vous pourriez penser, oh, attendez, qui construit une UI avec un gros monolithe de nos jours de toute façon (sauf les géants comme Google) ? Si c'est le cas, votre équipe utilise probablement l'une de ces approches traditionnelles pour construire des Microfrontends :

### **Composition Côté Serveur**

C'est l'approche la plus courante que j'ai rencontrée dans diverses organisations. L'idée est de diviser votre site web en fonction des motifs de route ou des pages. Par exemple, vous pourriez router les utilisateurs vers l'équipe des comptes pour toute route commençant par `/account/*` (`/account/login` ou `/account/signup` peuvent tomber sous ce motif). Ou vous pouvez avoir un préfixe de route similaire pour d'autres parties de votre application web, comme `/blog/*` pour la section marketing de votre application.

Cela est généralement implémenté au niveau du reverse proxy (comme l'utilisation de NGINX), qui route le trafic vers le service UI en aval approprié en fonction de la correspondance de chemin.

![Diagramme montrant une configuration de reverse proxy avec nginx. Le proxy route les requêtes `/blog/*` vers l'UI Marketing et les requêtes `/account/*` vers l'UI des Comptes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747496226912/fda979cd-c95c-4d48-a7dc-87956672b24d.png align="center")

### **iframes**

Une autre approche courante consiste à utiliser des iframes, bien que cette méthode présente des limitations significatives.

Contrairement à la composition côté serveur, qui fonctionne au niveau de la page, les iframes peuvent s'intégrer en tant que widgets au sein des pages. En utilisant des iframes, vous pouvez charger un autre site web en tant que partie du site web dans lequel vous souhaitez l'intégrer en utilisant la balise [&lt;iframe&gt;](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe).

![Diagramme illustrant l'intégration d'iframe, montrant website.com/blog intégrant un 'Widget' en utilisant une iframe avec la source 'website.com/widget'.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747496936962/7c24a43a-80d4-45f4-a2df-3de0e0e0bc1c.png align="center")

Certains exemples de cette approche, que vous avez peut-être vus, sont des sites web qui intègrent des flux Twitter, Google Maps, et ainsi de suite. Bien que ce soient des exemples d'intégrations de widgets externes avec des iframes, les entreprises peuvent intégrer certains widgets qui sont alimentés par des iframes.

### **Intégration à la Construction – Packages**

Cette approche implique la publication de composants en tant que bibliothèque UI que d'autres applications peuvent intégrer.

Cela est utile si vous souhaitez intégrer des applications complètes avec plusieurs pages, widgets ou composants statiques comme des en-têtes et pieds de page, où cette approche est assez courante.

Typiquement, cette approche signifie qu'une équipe publie ses composants en tant que package, tandis que d'autres équipes intègrent une version spécifique de ce package.

![Diagramme illustrant l'intégration à la construction via des packages, montrant website.com/blog intégrant un composant 'Widget', version 1.0.0, récupéré depuis un registre NPM de l'entreprise.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747497485861/70385841-28c6-441e-ae4d-c977b3563ecf.png align="center")

Dans cet exemple, il est important de noter que le composant Widget est intégré lors de la phase d'installation des dépendances de l'application. L'application web peut utiliser ce widget comme son propre composant, qui est construit ensemble en tant qu'un seul module et livré aux utilisateurs.

## Modèles Modernes de Microfrontends

### Fédération de Modules

La Fédération de Modules vous permet d'intégrer des morceaux d'UI distants au sein d'une application hôte à l'exécution. Ces morceaux peuvent être des pages complètes, des widgets ou des composants.

La Fédération de Modules a été introduite en tant que [fonctionnalité de Webpack 5](https://webpack.js.org/concepts/module-federation/), étendant les capacités du bundler pour charger du code JavaScript à partir de sources distantes à l'exécution.

[Module Federation 2.0](https://module-federation.io/) est l'évolution/amélioration de la fonctionnalité originale de Webpack 5, avec des implémentations disponibles pour d'autres bundlers populaires comme RSPack et Vite également.

Même si vous utilisez Webpack 5, je recommanderais d'utiliser Module Federation 2.0 car il prend en charge certains pièges courants qui existent dans l'implémentation originale de Webpack 5.

![Diagramme illustrant la Fédération de Modules, montrant une application hôte sur website.com/blog chargeant un composant 'Widget' à l'exécution depuis une application distante sur Recommendation.com via 'remotes: recommendation/remoteEntry'.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748011963774/fae404c6-efc9-4e0f-8667-4427dbcdfc0f.png align="center")

Prenons un exemple pour comprendre certains des éléments courants de la Fédération de Modules.

Imaginons que nous avons une application de blog, possédée par l'Équipe de Contenu & un Widget, qui est possédé par l'Équipe de Recommandations.

Maintenant, supposons que l'équipe de contenu souhaite intégrer un widget de recommandation au sein de leur application. Supposons que ces équipes ont des bases de code séparées hébergées sur différents domaines. L'équipe de contenu est sur `website.com` & l'équipe de recommandations est sur `recommendation.com`

Voici comment vous pouvez réaliser cette intégration MFE via la Fédération de Modules :

#### **Remote**

Responsable de l'exposition de fichiers JavaScript en tant que distant (par exemple, utilitaires, composants, etc.).

Dans notre exemple, ce serait l'équipe des Recommandations agissant en tant que distant & nécessitant une configuration pour "exposer" le Widget.

```typescript
new ModuleFederationPlugin({
  name: 'recommendation',
  exposes: {
    './Widget': './src/Widget.js',
  }
})
```

#### **Remote Entry**

Remote entry est l'URL du point d'entrée pour un distant. Un distant peut exposer plusieurs fichiers JavaScript, & le fichier remoteEntry serait conscient de tous.

La Fédération de Modules héberge par défaut le fichier remote entry à la racine. Dans notre exemple, les équipes de recommandation peuvent héberger leur remote entry sur `https://recommendation.com/remoteEntry.js`

#### **Host**

Un site web indépendant qui consomme du JavaScript à partir d'un ou plusieurs distants via **Remote Entry.** Considérez remote entry comme un espace de noms pour votre application sous lequel il peut exporter plusieurs éléments comme des composants, des utilitaires, etc., tels qu'exposés par un distant particulier.

Dans notre exemple, l'Équipe de Contenu agirait en tant qu'Hôte & ils définiront le remote entry de l'équipe de recommandation au sein de la configuration des distants.

```typescript
new ModuleFederationPlugin({
  name: 'content-blog',
  remotes: {
    "recommendation": 'recommendation@https://recommendation.com/remoteEntry.js',
  },
  // ... autres configs
})
```

#### **Shared**

Les hôtes et les distants peuvent spécifier des dépendances en tant que SemVer qui sont automatiquement négociées et partagées lors de l'exécution. Cela peut inclure des dépendances de framework communes, telles que React, qui peuvent nécessiter d'être un singleton, ou d'autres bibliothèques tierces qui peuvent être potentiellement partagées.

Avoir la bonne configuration partagée garantit que le client ne télécharge pas de bibliothèques ou de code déjà disponibles sur l'hôte lors de la récupération de morceaux d'UI à partir d'un emplacement distant, ce qui est essentiel pour des performances optimales lors de l'intégration de la Fédération de Modules.

```typescript
const deps = require("./package.json").dependencies;

new ModuleFederationPlugin({
  shared: {
    ...deps,
    react: {
      singleton: true,
      requiredVersion: deps.react,
    }
  },
  // ... autres configs
})
```

#### **Imports et Utilisation**

L'intégration de la Fédération de Modules vous permet d'utiliser des imports comme si ces fichiers JS étaient disponibles localement. La Fédération de Modules fait tout l'assemblage en coulisses à l'exécution, en termes de récupération du remote entry et des dépendances appropriées pour le rendre disponible lorsque vous l'utilisez.

```typescript
// Import est au format - <remote>/<expose-from-remote>
import Widget from 'recommendation/Widget';

// Rendu quelque part, en veillant à gérer le chargement via Suspense
// & les erreurs via la frontière d'erreur dans React
<ErrorBoundary>
  <Suspense fallback={<Loading />}
    <Widget />
  </Suspense>
</ErrorBoundary>
```

En résumé, le concept de fédération de modules est aussi simple que cela :

> Récupérer du code JS (composants, utilitaires, etc.) à partir d'un serveur distant à l'exécution et pouvoir partager des dépendances et être performant tout en le faisant.

### Single SPA

Lorsque vous recherchez des microfrontends, [Single SPA](https://single-spa.js.org) apparaît souvent comme une solution populaire. Mais son cas d'utilisation principal est assez spécifique : intégrer des composants à travers plusieurs frameworks (par exemple, React + Angular + Vue dans la même application). Voici comment cela fonctionne en pratique :

Single SPA agit comme un routeur JavaScript qui monte et démonte des applications entières en fonction des routes URL. Chaque "application single-spa" est une application spécifique à un framework qui est chargée lorsque sa route devient active.

```typescript
// Enregistrer des applications avec Single SPA
registerApplication({
 name: '@mycompany/react-app',
 app: () => System.import('@mycompany/react-app'),
 activeWhen: ['/react-app']
});

registerApplication({
 name: '@mycompany/angular-app', 
 app: () => System.import('@mycompany/angular-app'),
 activeWhen: ['/angular-app']
});
```

Single SPA gère la partie "orchestration" – décider quelle application doit être active et gérer leurs cycles de vie. Il ne résout pas le problème "comment charger du code distant" – vous devez toujours le coupler avec l'une des approches que nous avons discutées (Fédération de Modules, packages à la construction, etc.).

Si vos applications utilisent le même framework (comme React), vous pouvez sauter Single SPA entièrement et utiliser directement la Fédération de Modules. Single SPA ajoute une complexité qui n'est justifiée que lorsque vous avez vraiment besoin d'une intégration multi-framework.

## Comparaison Détaillée

| **Critères** | **Fédération de Modules** | **Composition côté serveur** | **iframe** | **Intégration à la construction (package)** |
| --- | --- | --- | --- | --- |
| **Déploiements indépendants** | 💚 Les microfrontends sont chargés à l'exécution sur le client. Cela signifie que les équipes peuvent effectuer des déploiements indépendants et apporter des modifications qui se reflètent immédiatement. | 💚 Les déploiements restent indépendants, car chaque motif de route pointe vers les déploiements indépendants d'une application individuelle | 💚 Puisque les iframes sont également chargées à l'exécution, les déploiements peuvent être indépendants. | 💔 Les déploiements sont couplés à partir de l'application hôte. Une modification du package nécessiterait de publier une nouvelle version et de l'augmenter dans l'application hôte. |
| **Performance** | 💚 Permet le partage de dépendances et le chargement optimisé, maintenant les performances SPA. | 💔 Nécessite des rechargements complets de page lors de la navigation entre les applications, perdant les avantages SPA. | 💔 Complètement isolé et charge toutes les dépendances du site web dans une iframe, ce qui signifie un chargement global de page plus lent. | 💚 Possible de partager les dépendances des packages dans une certaine mesure en [deduping](https://yarnpkg.com/cli/dedupe) les dépendances lors de l'intégration d'un package, mais cela nécessite un outil de développement approprié. Sinon, des dépendances dupliquées peuvent s'introduire pour le même package. |
| **Évolutivité et maintenance** | 💚 Fonctionne bien à grande échelle. Une page peut être entièrement composée de composants fédérés, avec les plus petits blocs de construction étant intégrés à partir de différents distants. | 💔 Nécessite généralement de dupliquer des éléments comme l'en-tête/pied de page, pour faire "sembler" que l'utilisateur est dans la même application, mais est servi par deux serveurs/bases de code différents. L'approche est limitée à la ségrégation basée sur les routes des points d'entrée des applications – donc, une intégration granulaire n'est pas possible. | 💔 Typiquement bon pour alimenter des pages entières et non des portions de pages, peut vraiment ralentir l'application à grande échelle et peut rencontrer des problèmes lors de l'optimisation de l'application pour le SEO ou la construction de mises en page dynamiques réactives. | 💔 Nécessite la maintenance de la publication des packages, des mises à jour et des conflits de version à grande échelle. Cela peut être simplifié dans une certaine mesure par l'outil CI, mais les développeurs devraient encore nécessiter un effort significatif pour augmenter les versions, vérifier l'impact d'un point de vue fonctionnel/performance. |
| **Effort de configuration** | 💔 Peut être élevé en fonction de la manière dont votre application est construite actuellement. Un niveau de compréhension plus profond de votre outil de construction peut être nécessaire pour faire fonctionner votre intégration souhaitée, ou lorsque vous rencontrez des problèmes. Cela est couvert en détail dans la section suivante. | 💚 Plus simple à implémenter, car il n'y a pas de couplage en dehors de la couche reverse proxy, qui est responsable de la redirection du trafic vers le service approprié. | 💔 Plus facile à intégrer mais nécessite la gestion de nombreux cas limites, ce qui peut prendre un temps significatif. Certains exemples sont la communication entre l'iframe/l'application hôte, les problèmes de mise en page, le rendu au-delà des limites de l'iframe (par exemple, les toasts), les restrictions de l'iframe cross-domain et la garantie de la sécurité, l'impact sur le SEO et l'accessibilité. | 💔 Nécessite un effort significatif pour stabiliser le pipeline de développement pour la publication d'un nouveau package, la maintenance d'un ensemble de modifications, l'augmentation d'une nouvelle version et la résolution des conflits de version. Chaque modification nécessite de s'assurer qu'il n'y a pas d'impact non intentionnel sur les dépendances transitives de l'application hôte en raison de l'augmentation du package. |
| **Authentification et Autorisation** | 💚 Selon la configuration de votre application, les composants fédérés de modules peuvent appeler le serveur de l'application distante pour tout besoin de récupération de données. Peut nécessiter la gestion du CORS si votre distant est sur un domaine différent de l'hôte, et pour que le navigateur envoie les cookies d'authentification pour de telles requêtes. | 💚 Chaque application peut s'intégrer indépendamment avec un service d'authentification central. | 💔 Il peut être difficile pour les iframes d'accéder aux détails du navigateur du site web parent comme les cookies d'authentification, etc. Cela peut également nécessiter quelques astuces pour faire fonctionner l'authentification, surtout si l'URL de l'iframe est sur un domaine/sous-domaine différent de celui de l'application. | 💚 Les composants de package peuvent choisir d'appeler des APIs via une API proxy au sein de l'application hôte ou s'intégrer directement avec les points de terminaison d'un service indépendant. |
| **Devloop** | 💚 Devloop mature avec Module Federation 2.0, vous pouvez afficher les source maps avec rechargement à chaud entre ces applications. Une intégration transparente dès la sortie de la boîte. Vous pouvez également pointer vers n'importe quel endpoint fédéré depuis le local pour pouvoir intégrer et vérifier l'intégration de bout en bout. | 💔 Nécessite la configuration des deux services et d'un reverse proxy localement pour vérifier les points de contact d'intégration, ce qui peut être non trivial. | 💔 Les tests locaux ne reproduisent pas avec précision les problèmes que vous pourriez rencontrer en raison des défis cross-domain avec les iframes. | 💔 Un flux de travail de développement approprié est nécessaire pour tester les modifications de package en développement au sein de l'application hôte localement. Cela est généralement fait avec la pré-publication du package ou en [liant](https://classic.yarnpkg.com/lang/en/docs/cli/link/) les packages locaux ou en utilisant un outil comme [yalc](https://github.com/wclr/yalc). |
| **Recommandation Globale 💚** | Adapté aux applications composées d'intégrations avec différentes équipes qui souhaitent posséder leurs déploiements et cycles de publication avec un faible couplage. | Adapté aux applications plutôt isolées (sous-domaines) au sein d'un domaine commercial plus large. Une question à poser est, à quelle fréquence l'utilisateur aurait-il besoin de naviguer entre ces applications ? Si la réponse est "pas souvent", alors cette approche peut être appropriée. | Non recommandé en raison des limitations qui l'accompagnent. Cela peut être adapté à certaines intégrations tierces, par exemple, Twitter expose une partie de son flux qui peut être intégrée dans un site web via une iframe. Cela est plutôt plus pratique que l'une des autres approches. | Adapté aux applications où les modifications doivent être plus contrôlées, avec l'application hôte mettant à niveau le package, et peut effectuer des vérifications appropriées avant de le publier pour leurs utilisateurs finaux. |

## Compromis et Défis avec la Fédération de Modules

Le compromis principal dans l'utilisation de la Fédération de Modules est l'effort de configuration initial, que j'ai brièvement discuté dans le tableau de comparaison précédent.

Voici quelques autres défis à anticiper lors de l'intégration via la Fédération de Modules :

### **Complexité de Configuration**

1. **Défis spécifiques au bundler** – Certaines choses peuvent nécessiter que vous connaissiez les détails internes de votre bundler pour faire fonctionner l'intégration pour votre application. Par exemple, avec Webpack 5, si votre distant expose non seulement des composants fédérés mais sert également une expérience utilisateur, vous aurez besoin de la configuration de chunk appropriée pour que cela fonctionne. Cela est dû au fait que la Fédération de Modules s'attend par défaut à une certaine stratégie d'optimisation des chunks et expose le remoteEntry à partir de la racine de l'application.
    
2. **Dépendances partagées** – Vous devrez passer en revue vos dépendances pour vous assurer de partager autant de dépendances que possible afin d'optimiser la taille du bundle et les performances de chargement. Vous devrez également marquer les bibliothèques critiques (comme React) comme singletons pour éviter les conflits d'exécution.
    

### **Défis d'Exécution**

1. **Cross domain** – si votre distant est sur un sous-domaine différent, par exemple `remote.website.com` et est chargé à partir de `host.website.com`, vous aurez besoin d'une gestion appropriée du CORS sur votre serveur pour permettre la récupération de données à partir du sous-domaine de l'hôte. Vous aurez également besoin d'une configuration de récupération `credentials` appropriée pour vous assurer que le navigateur envoie les cookies d'authentification dans les requêtes de récupération de données vers vos endpoints distants.
    
2. **Conflits de style** – Vous voudrez vous assurer que les styles du distant ne remplacent pas les styles de l'hôte et que les composants distants n'héritent pas de styles non intentionnels de l'hôte. Il existe plusieurs stratégies ici, allant de l'utilisation de composants stylisés à un DOM virtuel.
    

### **Préoccupations Opérationnelles**

1. **Observabilité et Analytics** – En fonction de vos exigences, vous pouvez souhaiter soit partager une instance de vos scripts d'observabilité, par exemple, un service de surveillance des erreurs, soit en instancier un complètement différent dans le contexte de votre MFE. Cela devient difficile, car il n'y a pas de fichier "index" rendu, mais plutôt des composants qui sont exposés à partir des distants.
    
2. **Déploiement & Mise en cache** – Il est recommandé que les bundles distants MFE soient hébergés sur des buckets S3 pour une haute fiabilité plutôt que de les charger à partir d'un serveur distant. Vous pouvez nécessiter une mise en cache à long terme appropriée pour les fichiers autres que le `remoteEntry.js` qui est généralement non haché et contient le lien vers d'autres dépendances à charger.
    

## Conclusion

Les microfrontends offrent une solution convaincante pour mettre à l'échelle le développement frontend entre plusieurs équipes, avec la Fédération de Modules émergent comme l'approche moderne la plus flexible.

Bien que les méthodes traditionnelles comme la composition côté serveur restent précieuses pour des cas d'utilisation spécifiques, la Fédération de Modules fournit la flexibilité d'exécution et les caractéristiques de performance nécessaires pour les applications complexes.

La décision dépend en fin de compte de la structure de votre équipe, des exigences techniques et de la tolérance à la complexité de mise en œuvre. Commencez par des approches plus simples si vous êtes nouveau dans les microfrontends, puis envisagez la Fédération de Modules à mesure que vos besoins évoluent.

### Qu'est-ce qui suit ?

Cet article était plus une vue d'ensemble du paysage. J'écrirai davantage sur la Fédération de Modules et irai au-delà des bases ensuite. Je couvrirai les défis techniques plus en détail, ainsi que les solutions possibles. Restez à l'affût !