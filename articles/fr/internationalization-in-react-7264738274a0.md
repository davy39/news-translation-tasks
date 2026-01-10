---
title: Internationalisation dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-05T15:09:41.000Z'
originalURL: https://freecodecamp.org/news/internationalization-in-react-7264738274a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hhTdD39DodXWsVl1OCdEpA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Internationalisation dans React
seo_desc: 'By Preethi Kasireddy

  Internationalization is a big problem. If you want your application to make a worldwide
  impact, you have to deal with language barriers.

  Unfortunately, the road from “Your funds will arrive by July 7th” to “Vos fonds
  arriveront l...'
---

Par Preethi Kasireddy

L'internationalisation est un grand problème. Si vous voulez que votre application ait un impact mondial, vous devez gérer les barrières linguistiques.

Malheureusement, le chemin de « Vos fonds arriveront le 7 juillet » à « Your funds will arrive by July 7th » est loin d'être simple.

Avant que votre application puisse réussir en dehors du monde anglophone, vous devrez adapter toutes vos chaînes de caractères, dates et nombres aux conventions de différentes cultures.

Les développeurs appellent cette pratique **internationalisation** (qui est souvent abrégée en « **i18n** », car il y a 18 lettres entre le 'I' et le 'n' dans le mot **I**nternationalizatio**n**.)

Une raison pour laquelle nous négligeons l'internationalisation est simplement parce qu'il est difficile de bien la faire. Chaque langue a des règles et des conventions différentes. S'adapter à ces règles et conventions prend du temps et des efforts.

### La solution : React Intl

Mais l'internationalisation n'a pas à être difficile, grâce à une nouvelle bibliothèque React. [**React Intl**](https://github.com/yahoo/react-intl) est un projet open-source de Yahoo, et fait partie de [Format.js](http://formatjs.io/), une collection de bibliothèques JavaScript pour l'internationalisation qui s'appuie sur l'API Intl intégrée de Javascript.

La bibliothèque [React Intl](https://github.com/yahoo/react-intl) rend l'internationalisation dans React simple, avec des composants prêts à l'emploi et une API qui peut gérer tout, de la mise en forme des chaînes de caractères, des dates et des nombres, à la pluralisation.

Faisons un tour d'horizon.

### Concepts de base

Voici les concepts de base que vous devrez maîtriser pour tirer le meilleur parti de React Intl :

#### API d'internationalisation de JavaScript

JavaScript dispose d'une spécification [API d'internationalisation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) qui définit l'objet **Intl** comme un objet global intégré standard.

React Intl utilise essentiellement cette API et s'appuie sur celle-ci. Tant que le navigateur supporte ces API, React Intl continuera à faire sa magie.

_Note : le seul navigateur qui ne supporte pas actuellement ces API est Safari. Nous utiliserons un polyfill pour surmonter cela dans le projet exemple ci-dessous._

#### Bundlers de modules

React Intl distribue son package via des modules ES6, CommonJS et UMD. Par conséquent, il fonctionne très bien avec des bundlers comme Webpack, Browserify et Rollup.

Dans le projet exemple, nous utiliserons Webpack comme bundler de modules.

Si vous ne prévoyez pas d'utiliser un bundler de modules pour charger React Intl dans votre application, je vous recommande de consulter la documentation pour plus d'informations sur d'autres approches (par exemple, via Node.js).

#### Chargement des données de locale

React Intl s'appuie sur ces données de locale pour supporter la mise en forme des pluriels et des temps relatifs. Les données de locale définissent les éléments suivants pour chaque locale spécifique :

* Modèles spécifiques à la locale pour la mise en forme et l'analyse des dates, heures, fuseaux horaires, nombres et valeurs monétaires
* Traductions pour les noms des monnaies, ères, mois, jours de la semaine, etc.
* Informations sur la langue et le script (cas de pluriel, caractères utilisés, genre des listes, capitalisation, direction d'écriture, etc.)
* Informations sur le pays (monnaie, préférence de calendrier, conventions de semaine, codes téléphoniques, etc.)

Si vous utilisez Browserify, Webpack ou Rollup pour bundler React Intl pour le navigateur, il ne contiendra que les données de locale pour l'anglais de base par défaut. Le reste des données de locale n'est **pas** inclus dans la bibliothèque principale. Donc dans ce projet exemple, nous allons voir comment importer les données de locale pour chaque langue que vous choisissez de supporter dans votre application.

Gardez à l'esprit que si vous utilisez React Intl via Node.js, toutes les données de locale seront chargées en mémoire, donc vous pouvez sauter cette étape.

#### Mise en forme des données en utilisant des composants React vs. l'API

La bibliothèque propose deux façons de formater les chaînes de caractères, les nombres et les dates : **les composants React** ou une **API**.

**Composant React :**

**API :**

J'adopte la première approche chaque fois que possible, en utilisant des composants React déclaratifs et idiomatiques pour formater les données plutôt que l'API impérative.

L'avantage de cette approche est qu'elle nous permet a) de composer des composants avec d'autres composants, b) de permettre un texte riche et une mise en forme des chaînes de caractères, c) de fournir des avertissements de type de prop pour les options de mise en forme, et d) d'implémenter _shouldComponentUpdate_ pour éviter des opérations de mise en forme coûteuses.

Bien sûr, il y a des moments où votre seul choix est d'utiliser l'API (par exemple : passer une chaîne de caractères comme une prop, un attribut de nom d'un élément HTML, etc.), donc elle reste utile.

### Projet exemple

La meilleure façon d'apprendre est de voir un exemple en direct. Pour cet article, j'ai créé un [projet React simple](https://github.com/iam-peekay/inbox-react-intl) qui se compose d'un composant d'en-tête principal, d'un composant de sous-en-tête et de quelques composants de widgets, chacun avec leurs propres en-têtes et corps.

Tout d'abord, nous allons passer en revue le processus de configuration de React Intl. Ensuite, nous utiliserons les composants et l'API pour convertir les chaînes de caractères, les nombres et les dates utilisés dans les composants.

### Configuration

Supposons que nous avons une application React existante sur laquelle nous travaillons. Tout d'abord, vous devrez installer le package React Intl :

Ensuite, nous devrons installer le plugin babel pour React Intl :

Pour que le plugin babel fasse réellement sa magie, nous devons configurer notre fichier **.babelrc** pour inclure ce plugin. Voici à quoi ressemble mon fichier **.babelrc** avec le plugin react-intl ajouté (lignes 6-11) :

Ce que fait ce plugin babel, c'est qu'il extrait toutes les chaînes de messages dans votre application qui sont définies en utilisant soit **defineMessages**, **<FormattedMessage>**, ou <FormattedHTMLMessage>.

(Notez que **defineMessages**, **<FormattedMessage>**, et <FormattedHTMLMessage> sont tous des exports nommés du package React Intl).

Une fois extraites, il génère des fichiers JSON qui contiennent les chaînes de messages et les place dans le répertoire que vous avez défini dans le chemin **messagesDir** ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KMLhO1bgMHip2XhcH3ZmMw.png)
_Messages extraits_

### Chargement des données

Ensuite, chargeons les données de locale appropriées pour les langues que nous devons supporter.

Comme je l'ai mentionné ci-dessus, si vous bundler pour le navigateur en utilisant Webpack, Browserify ou Rollup, React Intl est en anglais uniquement par défaut. Nous devons donc ajouter les autres données de locale manuellement.

Dans le fichier du composant racine, nous ajoutons les données de locale en utilisant l'API **addLocaleData**. Les données seront ensuite transmises au contenu du module de données de locale, qui sera ensuite enregistré dans son registre de données de locale.

Pour ce projet exemple, je vais supposer que nous supportons 4 langues : l'anglais, l'espagnol, le français et l'italien.

**Note** : Si votre application supporte beaucoup plus de langues, l'approche recommandée pour ajouter les données de locale est de charger dynamiquement les données de locale en fonction de la langue actuelle de l'utilisateur. Lisez la documentation de React Intl pour plus d'informations sur cette approche.

### Créer le contexte i18n dans votre application React

Jusqu'à présent, nous avons installé le package React Intl, configuré notre plugin **.babelrc**, et chargé les données de locale appropriées.

Une dernière étape consiste à créer un contexte **i18n** pour tous nos composants React afin que la locale de l'utilisateur actuel et le message traduit (basé sur la locale de l'utilisateur) puissent être chargés dans les composants React Intl que vous définissez dans votre application.

Pour ce faire, nous définissons d'abord les messages à passer à **IntlProvider** en fonction de la locale de l'utilisateur (voir les lignes 18-26 ci-dessous). Ensuite, nous enveloppons le composant racine React avec **IntlProvider**, qui est un export nommé fourni par React-Intl (voir les lignes 31-33) :

Dans cette configuration, nous supposons que nos données traduites résideront dans **build/locales/data.json** et que les données sont regroupées par langue, comme suit :

### Construire un script pour la traduction

Maintenant que nous avons terminé la configuration, voyons comment nous pouvons construire un script simple qui récupérera toutes les chaînes que babel extrait pour nous dans plusieurs fichiers JSON, et les combinera en un seul fichier.

Le but de ce script est d'accumuler toutes les chaînes en anglais afin que nous puissions ensuite télécharger ces chaînes vers un service de traduction, les faire traduire dans les différentes langues que nous supportons, et ensuite placer les résultats dans le fichier **build/locales/data.json** que nous avons utilisé ci-dessus. Une fois là, le composant **IntlProvider** peut enfin les charger dans notre composant racine.

Puisque nous n'avons pas besoin de faire les traductions dans cet article, nous allons sauter cette étape et simplement construire un script qui met tout dans un seul fichier. N'oubliez pas de faire appel à un fournisseur de services de traduction dans les applications réelles :)

Tout le mérite revient aux auteurs de la bibliothèque React Intl pour la génération de ce script ci-dessous :

### Étapes pour convertir les dates, les nombres et les chaînes avec React Intl

D'accord — nous sommes enfin prêts à faire un peu de mise en forme !

L'application exemple est une mise en page simple avec un **en-tête**, un **sous-en-tête** et des **widgets**, chacun contenant des chaînes de caractères, des nombres et/ou des dates :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CcUQumAeLtKuNb9BpQmp_g.png)

Rien de sophistiqué, mais c'est suffisant pour nous commencer.

#### En-tête

Tout d'abord, nous allons regarder l'en-tête qui dit : « Bienvenue sur votre tableau de bord, Preethi ! »

Pour convertir cela, nous allons utiliser le composant **FormattedMessage** :

Le composant **FormattedMessage** a des props qui correspondent à quelque chose appelé un « **Message Descriptor** » dans React Intl. Le **Message Descriptor** est le format utilisé pour définir les messages/chaînes de caractères par défaut, et est utile pour fournir les données nécessaires pour avoir les chaînes/messages traduits. Il contient les propriétés suivantes :

* **id** : Un identifiant unique et stable pour le message
* **description** : Contexte pour le traducteur sur la façon dont il est utilisé dans l'UI (optionnel)
* **defaultMessage** : Le message par défaut (en anglais)

La prop **id** doit être unique pour chaque message défini dans votre application. Ce qui est génial, c'est que le **defaultMessage** peut recevoir des données des props, comme c'est le cas pour **name** ci-dessus. (Notez que les valeurs qui sont passées en tant que données ne seront pas traduites — elles sont simplement insérées dans la chaîne traduite finale telles quelles.)

#### Sous-en-tête

Ensuite, regardons le sous-en-tête, qui est légèrement plus impliqué :

La capacité à composer des composants dans d'autres composants (c'est-à-dire avoir des éléments **Formatted*** dans un autre élément **Formatted***) est une fonctionnalité puissante de React Intl.

Vous pouvez voir dans l'exemple ci-dessus que **unreadCount** est un **FormattedNumber**, et **notifications** est un **FormattedPlural**, et que les deux sont des valeurs passées dans le **defaultMessage** de **FormattedMessages**. Magnifique !

Une autre fonctionnalité astucieuse est **FormattedRelative**, qui rendra le temps relatif formaté :

Une fois traduit et formaté, il se lira : « Vous vous êtes connecté pour la dernière fois il y a 4 heures ! » (Ou il y a combien de temps que lastLogin était.)

### Passage de chaînes formatées en tant que composants

Dans les deux extraits ci-dessus, nous avons vu comment utiliser les composants **Formatted*** pour définir des chaînes de caractères, des nombres, des dates et des pluriels.

Cependant, il y a de nombreuses instances où il est nécessaire de passer des chaînes formatées en tant que props ou d'utiliser des chaînes formatées pour nommer un composant HTML. Le composant **FormattedMessage** ne fonctionne pas bien dans des cas comme celui-ci.

Heureusement, l'API **defineMessages** de React Intl nous permet de définir de manière impérative toutes les chaînes de caractères d'un composant, puis de les passer en tant que props au composant.

Essayons cette approche pour les en-têtes et le corps des widgets. Tout d'abord, nous utilisons **defineMessages** pour définir nos chaînes de caractères :

Ensuite, en supposant que nous avons un composant Widget qui attend des props d'en-tête et de corps, nous pouvons continuer comme suit :

Une chose que vous avez peut-être remarquée dans le premier widget est que nous pouvons également passer des données aux chaînes de caractères définies dans **defineMessages**. Ici, nous avons passé la date formatée actuelle comme valeur **date**. Plutôt sympa, non ?

L'API fonctionne également bien pour la mise en forme des nombres, des dates, des heures, des temps relatifs et des pluriels (consultez leur [documentation](https://github.com/yahoo/react-intl/wiki/API) pour plus d'informations à ce sujet)

### Comment faire fonctionner dans Safari

Maintenant que nous avons presque terminé, je vais vous lancer une dernière balle courbe :

La configuration actuelle ne fonctionnera pas pour les navigateurs Safari :(

Comme mentionné ci-dessus, cela est dû au fait que Safari ne supporte pas actuellement l'API d'internationalisation de Javascript.

Heureusement, il existe encore un moyen de faire fonctionner cela pour les utilisateurs de Safari. Ce que nous devons faire, c'est utiliser le **polyfill Intl**. Il existe plusieurs façons de charger cela. Continuons à utiliser Webpack, pour l'exemple :

Tout d'abord, nous installons le package **intl** depuis npm :

Ensuite, nous allons écrire une simple instruction if pour charger le polyfill uniquement s'il n'y a pas de support natif du navigateur pour **Intl** (voir les lignes 30-57). Cela est pour éviter de charger la bibliothèque et toutes les données de locale dans votre application lorsque ce n'est pas nécessaire.

Comme vous pouvez le voir, la première chose à vérifier est si l'objet **intl** global n'est _pas_ disponible sur window. Si ce n'est pas le cas, alors nous chargeons le polyfill intl et les données de locale associées, puis nous rendons le composant. Sinon, nous rendons simplement le composant.

Et enfin, voici notre application pré-traduite (toujours en anglais bien sûr). Je vous laisse avec la dernière étape, qui consiste à trouver un fournisseur de traduction et à faire traduire ces chaînes de caractères !

![Image](https://cdn-media-1.freecodecamp.org/images/1*CcUQumAeLtKuNb9BpQmp_g.png)

### Autres conseils

J'espère que cet article est suffisant pour commencer à transformer votre application React désordonnée en une application qui est amicale avec d'autres cultures et langues.

Avant de me déconnecter, voici quelques autres conseils à considérer lors de l'internationalisation de votre application :

* **Composants flexibles** : Construisez vos composants de manière à ce qu'ils soient flexibles et permettent l'expansion et la réduction du texte. Certaines langues peuvent s'expanser beaucoup plus ou se réduire beaucoup plus que l'anglais. Si vous n'en tenez pas compte, votre mise en page peut sembler insupportable après la traduction.
* **Taille de police appropriée** : Utilisez une taille de police qui fonctionnera bien avec toutes les langues que vous supportez. Certaines langues, comme le japonais et le chinois, nécessitent des tailles de police plus grandes.
* **UTF-8** : Utilisez UTF-8 partout. Cela inclut dans votre HTML, le langage côté serveur, la base de données, etc. Contrairement à d'autres encodages, l'encodage UTF-8 gère presque toutes les langues très bien.
* **Pas de texte dans les images** : Évitez d'utiliser du texte dans les images car traduire le texte dans les graphiques est extrêmement difficile et ne vaut pas la peine.
* **Ne divisez pas vos chaînes** : Par exemple, si vous avez « Vos fonds arriveront le 7 juillet », évitez de diviser les chaînes comme « Vos fonds arriveront le » et « 7 juillet ». La combinaison peut ne fonctionner qu'en anglais en raison des variations d'ordre des mots dans d'autres langues.

### Conclusion

Comme toujours, n'hésitez pas à commenter avec des suggestions et des questions. J'adorerais en entendre parler :)

Tout le code de l'application exemple peut être trouvé sur github ici : [https://github.com/iam-peekay/inbox-react-intl](https://github.com/iam-peekay/inbox-react-intl)