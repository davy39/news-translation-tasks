---
title: Comment choisir une bibliothèque pour traduire vos applications JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T08:25:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-a-library-for-translating-your-javascript-apps-10f68de6a1d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IklbYvLxPek-M3vr2wTmoA.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: translation
  slug: translation
seo_title: Comment choisir une bibliothèque pour traduire vos applications JavaScript
seo_desc: 'By Anastasia

  In the previous articles, we have seen how to perform localization on the back-end.
  Specifically, we’ve covered Rails and Phoenix frameworks. Today, however, we are
  going to talk about libraries for translating JavaScript apps and briefl...'
---

Par Anastasia

Dans les articles précédents, nous avons vu comment effectuer la localisation côté serveur. Plus précisément, nous avons couvert les frameworks [Rails](https://blog.lokalise.co/rails-i18n/) et [Phoenix](https://blog.lokalise.co/localization-of-phoenix-applications/). Aujourd'hui, cependant, nous allons parler des bibliothèques pour traduire les applications JavaScript et voir brièvement comment elles fonctionnent.

Il semble qu'il existe de nombreuses solutions disponibles, vous pourriez donc demander : « Laquelle devrais-je utiliser ? ». La réponse la plus évidente (et peut-être la plus sensée) serait : « Cela dépend ». Idéalement, vous devriez vérifier chaque bibliothèque puis décider laquelle vous préférez.

Par conséquent, dans cet article, je vais vous donner une introduction générale aux solutions suivantes :

* Globalize
* I18next
* jQuery.I18n
* Polyglot.js

Notez que nous allons parler de la localisation des applications JS vanilla, et non d'un framework côté client spécifique. De plus, nous n'approfondirons pas chaque bibliothèque car l'article deviendrait beaucoup, beaucoup plus long. Je ne vous donnerai qu'une introduction douce à chaque outil. Ensuite, nous essaierons de les comparer et de tirer une conclusion générale.

Commençons-nous ?

### Globalize

[Globalize](https://github.com/globalizejs/globalize) est une bibliothèque JS complexe de traduction et de localisation initialement introduite par l'équipe jQuery. Cette bibliothèque utilise le [dépôt de données locales communes Unicode](http://cldr.unicode.org/) (CLDR) et possède de nombreuses fonctionnalités, notamment :

* Formatage des messages
* Analyse des dates/heures et capacité à travailler avec le temps relatif
* Support de la pluralisation
* Analyse des nombres et formatage des devises
* Capacité à travailler avec des unités (jours, minutes, secondes, miles par heure, etc.)

Globalize fonctionne de manière cohérente dans le navigateur et NodeJS, a un code modulaire et permet de ne charger que les modules nécessaires. Bien qu'elle s'appuie sur les données CLDR, elle ne les héberge ni ne les code en dur directement. Les développeurs peuvent choisir quelles données charger. Cela signifie également que vous pouvez mettre à jour les données CLDR vous-même, sans attendre qu'une nouvelle version de Globalize soit publiée. Vous pouvez lire un peu plus sur les fonctionnalités de Globalize [ici](https://github.com/globalizejs/globalize#features).

Maintenant, voyons cette bibliothèque en action. Il existe un [guide de démarrage](https://github.com/globalizejs/globalize#getting-started) qui explique comment installer tous les modules requis sur votre machine à l'aide d'un gestionnaire de paquets. Cependant, nous allons choisir une méthode plus complexe de chargement manuel de tout.

#### Obtenir les données CLDR

CLDR est vraiment énorme et il n'y a donc aucune raison de télécharger tout son contenu. Heureusement, la documentation de Globalize [résume ce que vous devez charger](https://github.com/globalizejs/globalize#2-cldr-content) lors de l'utilisation de modules spécifiques. De plus, il existe un [outil en ligne](https://johnnyreilly.github.io/globalize-so-what-cha-want/#/?currency=true&date=true&message=true&number=true&plural=true&relativeTime=true&unit=true) où vous sélectionnez simplement les modules qui seront utilisés, puis voyez quels fichiers JSON vous devez charger. Dans cette démonstration, je n'utiliserai que les modules « core », « message » et « plural », donc nous avons besoin des fichiers suivants :

Pour en savoir plus sur l'organisation de CLDR, [consultez cette documentation](https://github.com/unicode-cldr/cldr-json#package-organization). Cela peut sembler complexe au premier abord, mais en réalité, les choses sont assez simples : vous sélectionnez simplement les fichiers requis, les téléchargez et les utilisez dans votre projet.

J'ai placé les fichiers mentionnés ci-dessus dans le dossier `cldr/supplemental` de mon projet, mais vous pouvez bien sûr les organiser différemment.

La question suivante est : comment chargeons-nous réellement ces données ? Eh bien, [il existe deux alternatives](https://github.com/globalizejs/globalize/blob/master/doc/cldr.md#how-do-i-load-cldr-data-into-globalize) : en les intégrant dans la fonction `Globalize.load` ou en utilisant une méthode asynchrone [`$.get()`](https://api.jquery.com/jQuery.get/). La deuxième option est beaucoup plus robuste, alors créons un nouveau fichier JS avec le contenu suivant :

```
// i18n.js $.when( $.get("cldr/supplemental/likelySubtags.json"), $.get("cldr/supplemental/ordinals.json"), $.get("cldr/supplemental/plurals.json"), ).then(function() { // Normaliser les résultats de $.get, nous avons seulement besoin du JSON, pas des statuts de requête. return [].slice.apply(arguments, [0]).map(function(result) { return result[0]; }); }).then(Globalize.load).then(function() { // votre code Globalize ici });
```

Dans cet exemple, nous chargeons les données JSON et les fournissons à Globalize. Nous utilisons des promesses, donc le code personnalisé doit être placé dans le deuxième `then` et sera exécuté dès que tout sera chargé avec succès. N'hésitez pas à refactoriser ce code sans utiliser jQuery.

#### Charger d'autres fichiers

Après avoir chargé les fichiers JSON CLDR, vous avez besoin d'un [ensemble d'autres scripts](https://github.com/globalizejs/globalize#1-dependencies) :

* jQuery (notez au passage que Globalize lui-même n'est pas basé sur jQuery)
* [CLDR JS](https://github.com/rxaviers/cldrjs)
* Module principal Globalize JS
* Tout autre module que vous souhaitez utiliser dans votre application

jQuery et Cldr.js sont des dépendances externes et vous pouvez les charger depuis un CDN (par exemple, depuis [cdnjs.com](https://cdnjs.com/)).

Ensuite, téléchargez Globalize depuis la section Releases. Ouvrez le dossier `dist`. Sélectionnez tous les fichiers dont vous avez besoin et placez-les sous le répertoire `globalize`.

Après cela, chargez tous les scripts dans le bon ordre :

```
<!-- index.html --> <!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/cldrjs/0.5.1/cldr.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/cldrjs/0.5.1/cldr/event.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/cldrjs/0.5.1/cldr/supplemental.min.js"></script> <script src="globalize/globalize.js"></script> <script src="globalize/plural.js"></script> <script src="globalize/message.js"></script> <script src="i18n.js"></script> </body> </html>
```

En résumé, c'est tout. Maintenant, vous pouvez vous référer à la [section API](https://github.com/globalizejs/globalize#api) de la documentation de Globalize et voir quelles fonctions vous pouvez utiliser.

#### Utilisation

Vous pouvez fournir des messages de traduction à l'aide de la fonction [`loadMessages`](https://github.com/globalizejs/globalize/blob/master/doc/api/message/load-messages.md) :

```
$.when( // ... }).then(Globalize.load).then(function() { Globalize.loadMessages({ "en": { 'welcome': 'Welcome, {name}!' } }); });
```

Ensuite, instanciez Globalize avec la locale souhaitée et effectuez les traductions réelles :

```
// loadMessages... var globalize = new Globalize("en"); console.log(globalize.messageFormatter('welcome')({name: 'Username'}));
```

[`messageFormatter`](https://github.com/globalizejs/globalize/blob/master/doc/api/message/message-formatter.md) retourne une traduction formatée. Comme vous pouvez le voir dans cet exemple, il supporte l'interpolation, mais ce n'est pas tout. Vous voulez introduire la pluralisation ? C'est simple !

Ajoutez un nouveau message :

```
Globalize.loadMessages({ "en": { 'welcome': 'Welcome, {name}!', 'messages': [ "You have {count, plural,", " one {one message}", " other {{count} messages}", "}" ] } });
```

Notez que le message peut s'étendre sur plusieurs lignes, mais dans ce cas, il doit être défini comme un tableau. Ici, nous utilisons la pluralisation et fournissons deux formes : singulier et pluriel. `count` est une interpolation.

Maintenant, affichez ce message :

```
taskFormatter = globalize.messageFormatter("messages"); console.log(taskFormatter({ count: 10 }));
```

Vous pouvez utiliser d'autres modules de manière assez similaire.

Pour résumer, Globalize est une solution puissante avec une bonne documentation et un bon support. Il peut nécessiter un certain temps pour le configurer, mais travailler avec lui est pratique et intuitif.

### I18next

I18next est un framework de localisation JavaScript fournissant tous les outils nécessaires pour traduire vos applications. Il possède de nombreuses fonctionnalités variées, notamment :

* [Support des frameworks front-end](https://www.i18next.com/overview/supported-frameworks) incluant React, Angular, Vue, etc.
* Support de divers formats (y compris Polyglot que nous discuterons plus tard)
* Formatage des messages
* Pluralisation
* Retours en arrière
* Capacité à charger les données de traduction à partir de diverses ressources
* ...et bien d'autres [utilitaires et plugins](https://www.i18next.com/overview/plugins-and-utils)

#### Charger les fichiers requis

Pour commencer avec I18next, vous pouvez simplement le charger depuis un CDN, par exemple :

```
<!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/i18next/14.0.1/i18next.min.js"></script> </body> </html>
```

Bien sûr, il peut également être installé avec NPM ou Yarn comme expliqué [ici](https://www.i18next.com/overview/getting-started).

#### Configuration

Comme je l'ai déjà mentionné ci-dessus, I18next vous permet de charger les traductions depuis le backend. Vous pouvez également les fournir de la manière suivante :

```
i18next.init({ lng: 'en', resources: { en: { translation: { "hi": "Welcome" } } } }).then(function(t) { // prêt à partir ! });
```

Notez que je définis également l'anglais comme locale par défaut.

Il existe de nombreuses autres options de configuration qui sont listées sur la [page correspondante](https://www.i18next.com/overview/configuration-options).

#### Utilisation

Vous pouvez effectuer des traductions de la manière suivante :

```
// ... init .then(function(t) { // initialisé et prêt à partir ! console.log(i18next.t('hi')); });
```

[`t`](https://www.i18next.com/overview/api#t) est une fonction pour rechercher une traduction basée sur la clé fournie. Elle peut également fonctionner avec l'interpolation, par exemple :

```
i18next.t('hi', {name: 'Username'});
```

La [pluralisation](https://www.i18next.com/translation-function/plurals) est également supportée. Pour commencer à l'utiliser, définissez les formes singulière et plurielle de la manière suivante :

```
{ "msg": "one message", "msg_plural": "{{count}} messages" }
```

Notez la partie `_plural` qui doit être fournie pour les formes plurielles. Certaines langues nécessitent [plusieurs formes](https://www.i18next.com/translation-function/plurals#languages-with-multiple-plurals). Dans ce cas, utilisez `_0`, `_1`, et d'autres suffixes, par exemple :

```
{ "key_0": "zero", "key_1": "singular", "key_2": "two", "key_3": "few", "key_4": "many", "key_5": "other" }
```

Ensuite, utilisez simplement la fonction `t` à nouveau :

```
i18next.t('msg', {count: 10});
```

I18next vous permet de fournir un [contexte pour la traduction](https://www.i18next.com/translation-function/context). Cela est particulièrement important lorsque vous travaillez avec des informations de genre :

```
{ "friend": "A friend", "friend_male": "A boyfriend", "friend_female": "A girlfriend" }
```

`_male` et `_female` ici sont des contextes que vous pouvez définir de la manière suivante :

```
i18next.t('friend'); // ==> Pas de contexte ici, donc retourne "A friend" i18next.t('friend', { context: 'male' }); // -> Un contexte est présent, donc retourne "A boyfriend"
```

N'hésitez pas à parcourir d'autres exemples dans la documentation d'I18next sur la façon d'[activer la imbrication dans les traductions](https://www.i18next.com/translation-function/nesting), de [travailler avec des objets](https://www.i18next.com/translation-function/objects-and-arrays), ou de [configurer les retours en arrière](https://www.i18next.com/principles/fallback).

Pour résumer, I18next est un excellent framework avec une gamme de divers plugins et utilitaires. Ce framework est assez grand et lourd, mais vous recevez tous les outils de localisation nécessaires qui peuvent être étendus si nécessaire. De plus, la configuration de ce framework est simple et nécessite très peu de temps. Donc, je dirais que c'est un excellent candidat pour les applications complexes !

### jQuery.I18n

[jQuery.I18n](https://github.com/wikimedia/jquery.i18n) est une autre solution populaire présentée par l'équipe [Wikimedia Engineering](https://www.mediawiki.org/wiki/Wikimedia_Language_engineering) permettant de traduire vos applications JavaScript. Wikimedia, à son tour, est une entreprise derrière le [projet Wikipedia](http://en.wikipedia.org/), l'un des sites web les plus populaires au monde. jQuery.I18n est utilisé en interne dans Wikipedia, vous pouvez donc être sûr que cette bibliothèque ne sera pas abandonnée du jour au lendemain. Elle utilise un format de localisation basé sur JSON et supporte les fonctionnalités suivantes :

* Capacité à ajouter des métadonnées et documenter vos messages
* Supporte la pluralisation à l'aide de CLDR
* Informations de genre
* Support des formes grammaticales
* Chaînes de retour en arrière
* Capacité à personnaliser l'analyseur de messages
* A un code modulaire

Voyons maintenant jQuery.I18n en action.

#### Charger les fichiers requis

Tout d'abord, téléchargez la bibliothèque elle-même et initialisez ses dépendances :

```
$ git clone https://github.com/wikimedia/jquery.i18n.git $ cd jquery.i18n $ git submodule update --init
```

Le dossier `jquery.i18n/src` contient les fichiers de la bibliothèque. Sélectionnez les modules dont vous avez besoin (au minimum, vous aurez besoin du cœur `jquery.i18n.js`) et placez-les dans votre application. L'idée ici est similaire à celle de Globalize. Le dossier `languages` contient quelques aides pour diverses locales. Si vous supportez l'une d'entre elles, n'oubliez pas de copier le fichier correspondant également.

Si votre application travaille avec des formes plurielles, alors le fichier `CLDRPluralRuleParser.js` est également nécessaire (il peut être trouvé sous le chemin `jquery.i18n\libs\CLDRPluralRuleParser\src`).

Une fois que vous êtes prêt, chargez les fichiers dans le bon ordre, par exemple :

```
<!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script> <script src="lib/CLDRPluralRuleParser.js"></script> <script src="lib/jquery.i18n.js"></script> <script src="lib/jquery.i18n.messagestore.js"></script> <script src="lib/jquery.i18n.fallbacks.js"></script> <script src="lib/jquery.i18n.language.js"></script> <script src="lib/jquery.i18n.parser.js"></script> <script src="lib/jquery.i18n.emitter.js"></script> <script src="lib/jquery.i18n.emitter.bidi.js"></script> </body> </html>
```

#### Fournir des traductions

Comme mentionné ci-dessus, les [traductions pour la bibliothèque jQuery.I18n](https://github.com/wikimedia/jquery.i18n#message-file-format) sont stockées dans des fichiers JSON. Vous pouvez séparer les données de traduction pour différentes langues, ou tout stocker dans un seul fichier. Créez un fichier `i18n/i18n.json` avec le contenu suivant :

```
{ "@metadata": { "authors": [ "Ilya" ], "last-updated": "2019-01-29", "message-documentation": "qqq" }, "welcome": "Hi!" }
```

[Pour charger ce fichier](https://github.com/wikimedia/jquery.i18n#message-loading), utilisez le code suivant (notez que je fournis également une locale par défaut) :

```
// main.js jQuery(document).ready(function() { $.i18n({locale: 'en'}).load({ en: 'i18n/i18n.json' }).done(function() { // succès }) });
```

Incluez ce script sur votre page principale et vous êtes prêt à partir !

#### Utilisation

Par exemple, vous pouvez afficher un message de bienvenue de la manière suivante :

```
console.log($.i18n('welcome', 'Username'));
```

La [pluralisation](https://github.com/wikimedia/jquery.i18n#plurals) est effectuée de la manière suivante :

```
{ "msg": "You have $1 {{PLURAL:$1|message|messages}}" }
```

Ainsi, vous avez une clé qui liste toutes les formes disponibles, à la fois plurielles et singulières. `$1` est un [espace réservé](https://github.com/wikimedia/jquery.i18n#placeholders) pour l'interpolation. Vous pouvez avoir autant d'espaces réservés que nécessaire, et ils doivent être nommés de manière séquentielle : `$2`, `$3`, etc.

Ensuite, utilisez simplement cette nouvelle clé :

```
$.i18n('msg', 10); // l'espace réservé $1 aura une valeur de 10
```

Le contexte de la traduction est défini de manière assez similaire. Par exemple, vous pouvez travailler avec les [informations de genre](https://github.com/wikimedia/jquery.i18n#gender) :

```
"friend": "Some text... {{GENDER:$1|A boyfriend|A girlfriend}}"
```

Fournissez le contexte :

```
$.i18n('friend', 'female');
```

Une fonctionnalité intéressante est le support des [attributs HTML5 `data-*`](https://github.com/wikimedia/jquery.i18n#data-api). Vous devez simplement ajouter un attribut `data-i18n` à vos balises, fournir la clé comme valeur, puis appliquer la fonction `.i18n()` directement à ces éléments ou à leur parent. Par exemple :

```
<body> <p data-i18n="translation-key">Fallback text goes here</p> <p data-i18n="another-key">Fallback text goes here</p> </body>
```

Maintenant, dans votre code, dites simplement :

```
$('body').i18n();
```

Le script va parcourir tous les éléments à l'intérieur de `body` et remplacer leur contenu par les messages sous les clés de traduction fournies. Si la clé ne peut pas être trouvée, le contenu initial sera affiché comme retour en arrière.

jQuery.I18n est une bibliothèque puissante et assez facile à utiliser. En fait, vous pouvez l'appeler un concurrent direct de Globalize, car ces deux solutions ont des fonctionnalités similaires. Pour certaines personnes, Globalize peut sembler plus favorable car il ne dépend pas de jQuery. D'un autre côté, de nombreux sites nécessitent jQuery, donc ce n'est peut-être pas un critère d'exclusion. Si vous souhaitez rester éloigné de CLDR, alors jQuery.I18n est bien sûr une meilleure option. Cette bibliothèque permet également de stocker des métadonnées dans vos fichiers de traduction, supporte l'API des [attributs `data-*`](https://github.com/wikimedia/jquery.i18n#data-api), supporte les soi-disant ["mots magiques"](https://github.com/wikimedia/jquery.i18n#magic-word-support), et plus encore. Donc, comme vous le voyez, il y a vraiment beaucoup de fonctionnalités !

### Polyglot

La dernière solution dont nous parlerons est [Polyglot.js](https://github.com/airbnb/polyglot.js) créée par Airbnb. Puisque le service Airbnb est mondial, il est essentiel pour eux d'avoir une localisation appropriée. Polyglot, contrairement aux bibliothèques discutées précédemment, est une solution très petite. Elle n'a que les fonctionnalités suivantes :

* Fonctionnalités de traduction de base
* Interpolation
* Pluralisation

Elle peut devenir un excellent candidat pour des applications plus petites et moins complexes qui ne nécessitent pas toutes les complexités de, par exemple, Globalize. Maintenant, voyons comment commencer avec Polyglot !

#### Charger les fichiers

Polyglot n'a aucune dépendance externe, donc tout ce que vous avez à faire est de connecter le fichier principal :

```
<!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/polyglot.js/2.2.2/polyglot.min.js"></script> </body> </html>
```

#### Fournir des traductions et l'utiliser

Maintenant, nous pouvons fournir des traductions (alias "phrases") et définir la locale par défaut :

```
var polyglot = new Polyglot({ locale: 'en', phrases: { "message_count": "%{smart_count} message |||| %{smart_count} messages" } });
```

Dans cet exemple, la locale par défaut est l'anglais. De plus, il y a une clé `message_count` qui fournit des formes singulière et plurielle séparées par 4 pipelines (pour d'autres langues, il peut y avoir plus de formes). Étrangement, [la pluralisation repose sur la valeur interpolée `smart_count`](https://github.com/airbnb/polyglot.js#pluralization), vous devez donc la fournir de la manière suivante :

```
console.log(polyglot.t('message_count', {smart_count: 2}));
```

C'est tout ! Il n'y a pas grand-chose à dire sur le processus de traduction, car il repose uniquement sur la fonction `t`. Vous pouvez trouver d'autres exemples d'utilisation de Polyglot dans la [documentation officielle](https://github.com/airbnb/polyglot.js#translation).

### Résumé

Potentiellement, il y a beaucoup de fonctionnalités différentes à comparer (certaines peuvent être plus ou moins pertinentes pour votre configuration), mais voici un bref résumé des solutions discutées :

![Image](https://cdn-media-1.freecodecamp.org/images/hj2GuNOKjpR8g-pZMcqoHPf9FegIwkGZDXEK)

Quelques points à noter :

* I18next [supporte divers formats](https://github.com/i18next/i18next-gitbook/blob/master/translation-function/formatting.md) mais cela nécessite des dépendances externes comme [moment.js](https://momentjs.com/)
* jQuery.I18n nécessite le parseur CLDR uniquement pour la pluralisation
* I18next fournit de nombreux plugins pour se connecter au framework côté client, mais d'autres solutions peuvent également bien fonctionner avec les frameworks (vous devrez peut-être passer plus de temps à tout intégrer)
* Vous pouvez travailler avec des informations de genre (et, plus largement, avec des contextes) dans n'importe quelle bibliothèque — cela peut simplement être moins pratique et présenter plus de complexités

D'après mon expérience, I18next est un outil très puissant et riche en fonctionnalités avec lequel vous pouvez facilement commencer. En même temps, l'approche modulaire de Globalize et sa relation avec CLDR peuvent être pratiques, surtout pour les applications plus grandes et plus complexes. Je n'ai pas utilisé jQuery.I18n autant, mais tant que l'équipe Wikimedia l'utilise, on peut conclure que c'est également un outil faisable avec une fonctionnalité vaste. Et, Polyglot est un petit assistant sympa pour les applications plus simples qui fonctionne également très bien avec les frameworks côté serveur comme Rails.

### Facilitez-vous la vie avec Lokalise

Supporter plusieurs langues sur un grand site web peut devenir un vrai casse-tête. Vous devez vous assurer que toutes les clés sont traduites pour chaque locale. Heureusement, il existe une solution à ce problème : la plateforme Lokalise qui [rend le travail avec les fichiers de localisation beaucoup plus simple](https://lokalise.co/features). Laissez-moi vous guider à travers la configuration initiale qui n'est vraiment pas complexe.

* Pour commencer, [obtenez votre essai gratuit](https://lokalise.co/signup)
* Créez un nouveau projet, donnez-lui un nom et définissez l'anglais comme langue de base
* Cliquez sur « Upload Language Files »
* Téléchargez les fichiers de traduction pour toutes vos langues
* Passez au projet et modifiez vos traductions selon vos besoins
* Vous pouvez également contacter un traducteur professionnel pour faire le travail à votre place
* Ensuite, téléchargez simplement vos fichiers
* Profitez !

Lokalise a beaucoup plus de fonctionnalités, y compris le support de dizaines de plateformes et de formats, et même la possibilité de télécharger des captures d'écran pour en lire les textes. Donc, restez avec Lokalise et facilitez-vous la vie !

### Conclusion

Dans cet article, nous avons parlé des outils disponibles utilisés pour traduire les applications JavaScript. Nous avons couvert Globalize, I18next et jQuery.I18n (solutions plus grandes et plus complexes), ainsi que Polyglot qui s'est avéré être une bibliothèque beaucoup plus simple et plus petite. Nous avons comparé ces bibliothèques et tiré quelques conclusions à leur sujet. Espérons que maintenant vous serez en mesure de choisir une solution I18n qui vous convient entièrement. N'ayez pas peur de rechercher, d'expérimenter et, finalement, de choisir l'outil qui fonctionne pour vous ! Après tout, il sera plus compliqué de passer à une autre bibliothèque de localisation lorsque votre application est à moitié terminée.

Je vous remercie de rester avec moi, et à la prochaine fois !

*Initialement publié sur [blog.lokalise.co](https://blog.lokalise.co/comparing-libraries-translating-js-apps/) le 31 janvier 2019.*