---
title: Roarr! le logger JSON parfait pour Node.js et le navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-02T10:23:22.000Z'
originalURL: https://freecodecamp.org/news/roarr-the-perfect-json-logger-node-js-and-browser-935180bda529
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sa1l2KtSEr8QrEA-gdC8eQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Roarr! le logger JSON parfait pour Node.js et le navigateur
seo_desc: 'By Gajus Kuizinas

  Zero-configuration, out of process transports and adheres to the Twelve Factors

  The past 8 months I have been creating GO2CINEMA. This web application allows users
  to discover showtimes. They can also book cinema tickets across the ...'
---

Par Gajus Kuizinas

#### Configuration zéro, transports hors processus et adhère aux Twelve Factors

Les 8 derniers mois, j'ai créé [GO2CINEMA](https://go2cinema.com/). Cette application web permet aux utilisateurs de découvrir les horaires des séances. Ils peuvent également réserver des billets de cinéma dans le monde entier.

La plateforme a grandi pour inclure plus de +50 services distincts. Les services supportent l'agrégation de données, la normalisation, la validation, l'analyse, la distribution, l'invalidation, et plus encore. Certains de ces services s'exécutent dans des environnements à haute réplication, jusqu'à des centaines.

J'avais besoin de savoir quand les choses se cassent. Et j'avais besoin de pouvoir corrélier les logs à travers tous ces services pour identifier le problème.

![Image](https://cdn-media-1.freecodecamp.org/images/KlCrwwOKLnRAQA3YTJYe11857H5DuR5ltk3W)
_Exécuter des services en haute concurrence, vous devez pouvoir identifier quand et ce qui se casse._

J'avais besoin d'un logger qui n'existait pas.

#### Loggers existants

Depuis longtemps, je suis un grand fan de [debug](https://github.com/visionmedia/debug). Debug est simple à utiliser, fonctionne dans Node.js et les navigateurs, ne nécessite pas de configuration et est rapide. Cependant, des problèmes surviennent lorsque vous devez analyser les logs. Tout ce qui n'est pas des messages texte sur une seule ligne ne peut pas être analysé de manière sûre.

Pour logger des données structurées, j'ai utilisé [Winston](https://github.com/winstonjs/winston) et [Bunyan](https://github.com/trentm/node-bunyan). Ces packages sont excellents pour le logging au niveau de l'application. J'ai préféré Bunyan en raison du [programme CLI Bunyan](https://github.com/trentm/node-bunyan#cli-usage) utilisé pour imprimer joliment les logs.

Cependant, ces packages nécessitent une configuration au niveau du programme. Lorsque vous construisez une instance d'un logger, vous devez définir le transport et le niveau de log. Cela les rend inadaptés pour une utilisation dans du code conçu pour être utilisé par d'autres applications.

Ensuite, il y a [pino](https://github.com/pinojs/pino). Pino est un logger JSON rapide. Son programme CLI est équivalent à Bunyan. Il découple les transports et a une configuration par défaut saine. Pourtant, vous devez toujours instancier le logger au niveau de l'application. Cela le rend plus adapté pour le logging au niveau de l'application comme Winston et Bunyan.

J'avais besoin d'un logger qui :

* [Sépare le code de la configuration](https://12factor.net/config)
Toute la configuration est stockée dans les variables d'environnement
* Produit des données structurées
* [Découple les transports](https://github.com/gajus/roarr#transports)
* A un [programme CLI](https://github.com/gajus/roarr#cli-program)
* Fonctionne dans Node.js et le navigateur

En d'autres termes, un logger qui :

* Je peux utiliser dans un code d'application et dans des dépendances
* me permet de corrélier les logs entre le code principal de l'application et le code des dépendances
* fonctionne bien avec les transports dans des processus externes

… et il doit être **bruyant** lorsque les choses se cassent vraiment.

[Roarr](https://github.com/gajus/roarr) est ce logger.

![Image](https://cdn-media-1.freecodecamp.org/images/cTLKidw1Si4dCocEg4zzDl28oEoRc3bngOz-)
_Roarr est bruyant_

### API stricte

Un logger doit avoir une API simple à retenir et produisant des résultats prévisibles. Roarr y parvient en restreignant la surface de l'API.

#### Configuration

Le logging Roarr est désactivé par défaut. Pour activer le logging, vous devez démarrer le programme avec une variable d'environnement `ROARR_LOG` définie sur `true` :

```
ROARR_LOG=true node ./index.js
```

Toute la [configuration de Roarr](https://github.com/gajus/roarr#environment-variables) est effectuée en utilisant des variables d'environnement. Le développeur ne peut pas désactiver le logging ou définir le niveau de logging au niveau de l'application. C'est une bonne chose – le filtrage, le formatage et l'augmentation des logs appartiennent aux **transports hors processus**. Cela garantit que vous n'avez jamais besoin de toucher le code pour changer le comportement du logging.

#### La fonction logger

L'[API de Roarr](https://github.com/gajus/roarr#api) est restreinte à deux paramètres (plus les arguments de formatage [printf](https://en.wikipedia.org/wiki/Printf_format_string)).

* Le premier paramètre peut être soit une chaîne (message) soit un objet. Si le premier paramètre est un objet (contexte), le deuxième paramètre doit être une chaîne (message).
* Les arguments après le paramètre message sont utilisés pour activer le formatage de message printf. Les arguments printf doivent être d'un type primitif (`string | number | boolean | null`). Il peut y avoir jusqu'à 9 arguments printf (ou 8 si le premier paramètre est l'objet contexte).

En pratique, cela se traduit par l'utilisation suivante :

```
import log from 'roarr';log('foo');log('bar %s', 'baz');const debug = log.child({  level: 'debug'});debug('qux');debug({  quuz: 'corge'}, 'quux');
```

Le paramètre contexte contient des données arbitraires définies par l'utilisateur utilisées pour identifier le contexte dans lequel un message de log a été produit. Il peut contenir le nom de l'application, le nom du package, l'ID de la tâche, le nom de l'hôte, le nom de l'instance du programme et d'autres données.

Cela produit une sortie :

```
{"context":{},"message":"foo","sequence":0,"time":1506776210000,"version":"1.0.0"}{"context":{},"message":"bar baz","sequence":1,"time":1506776210000,"version":"1.0.0"}{"context":{"level":"debug"},"message":"quux","sequence":2,"time":1506776210000,"version":"1.0.0"}{"context":{"level":"debug","quuz":"corge"},"sequence":3,"message":"quux","time":1506776210000,"version":"1.0.0"}
```

Cette sortie est conçue pour être consommée par les transports de logs.

#### Inspection des logs

Pour inspecter les logs au moment du développement, utilisez le programme `**roarr pretty-print**`.

La sortie que le programme CLI pretty-print produit ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/8vLks-pUZ-BWLFqoc-H2kQnV0ANwlzob6kp7)
_Sortie du programme CLI._

Le programme CLI repose sur un ensemble de [conventions](https://github.com/gajus/roarr#context-property-names) pour structurer les données.

Le programme CLI Roarr a quelques autres commandes et options. Voir `roarr --help` pour plus d'informations.

### Modèles d'utilisation

Pour éviter la duplication de code, vous pouvez utiliser un [modèle singleton](https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)) pour exporter une instance de logger avec des propriétés de contexte prédéfinies. Par exemple, en décrivant l'application.

#### Utilisation de Roarr dans une application

Je recommande de créer un fichier `Logger.js` dans le répertoire de base du projet. Vous pouvez utiliser ce fichier pour créer une instance enfant de Roarr avec des paramètres de contexte décrivant le projet et l'initialisation.

```
/** * @file Exemple de contenu d'un fichier Logger.js. */
```

```
import Roarr from 'roarr';import ulid from 'ulid';
```

```
// L'ID d'instance est utile pour corrélier les logs dans un environnement à haute concurrence.//// Voir l'option `roarr augment --append-instance-id` comme une alternative pour// ajouter l'ID d'instance à tous les logs.const instanceId = ulid();
```

```
// La raison pour laquelle nous utilisons `global.ROARR.prepend` plutôt que `roarr#child`// est que nous voulons que cette information soit préfixée à tous les logs, y compris// ceux des dépendances "my-application".global.ROARR.prepend = {  ...global.ROARR.prepend,  application: 'my-application',  instanceId};
```

```
export default Roarr.child({  // La propriété .foo apparaîtra uniquement dans les logs qui sont créés en utilisant  // l'instance actuelle d'un logger Roarr.  foo: 'bar'});
```

#### Utilisation de Roarr dans une dépendance

Si vous développez un code conçu pour être consommé par d'autres applications et modules, vous devez éviter d'utiliser `global.ROARR`. Bien qu'il y ait des [cas d'utilisation valides](https://github.com/gajus/roarr#prepending-context-using-the-global-state).

Vous devriez toujours commencer le projet en définissant un fichier `Logger.js` et utiliser `log.child` à la place.

```
/** * @file Exemple de contenu d'un fichier Logger.js. */
```

```
import Roarr from 'roarr';
```

```
export default Roarr.child({  domain: 'database',  package: 'my-package'});
```

Roarr n'a pas de noms de propriétés de contexte réservés. Cependant, j'encourage l'utilisation des **conventions**.

Le programme CLI `roarr pretty-print` utilise les noms de propriétés de contexte suggérés dans les conventions. Cela imprimera joliment les logs à des fins d'inspection par le développeur.

### Filtrage des logs

Roarr est conçu pour imprimer tous les logs ou aucun. Reportez-vous à la documentation de la variable d'environnement `**ROARR_LOG**`.

Pour filtrer les logs, vous devez utiliser un processeur JSON, tel que [jq](https://stedolan.github.io/jq/).

`jq` vous permet de filtrer les messages JSON en utilisant `[select(boolean_expression)](https://stedolan.github.io/jq/manual/#select(boolean_expression))` :

```
ROARR_LOG=true node ./index.js | jq 'select(.context.logLevel == "warning" or .context.logLevel == "error")'
```

Le résultat est le seul message de log qui a soit un niveau de log "warning" soit "error". Vous pouvez combiner jq avec le programme CLI Roarr pour vous concentrer sur un message d'erreur spécifique :

```
ROARR_LOG=true node ./index.js | jq 'select(.context.package == "usus")' | roarr pretty-print
```

### Manipulation du contexte des messages de log globalement

À ce stade, vous avez probablement compris ce qu'est un "contexte" de message de log. C'est un objet clé-valeur définissant les variables d'environnement au moment de la journalisation du message.

Dans certains cas, il peut être utile de préfixer des propriétés à l'objet contexte globalement pour tous les messages à l'exécution. Par exemple, vous avez un programme d'exécution de tâches et vous souhaitez associer tous les logs qui ont été imprimés pendant le temps de l'exécution de la tâche.

Vous pouvez faire cela en utilisant `global.ROARR.prepend` :

```
import log from 'roarr';import foo from 'foo';const taskIds = [  1,  2,  3];for (const taskId of taskIds) {  global.ROARR = global.ROARR || {};  global.ROARR.prepend = {    taskId  };  log('starting task ID %d', taskId);  // Dans cet exemple, `foo` est une dépendance tierce arbitraire qui utilise  // le logger roarr.  foo(taskId);  log('successfully completed task ID %d', taskId);  global.ROARR.prepend = {};}
```

Produit la sortie :

```
{"context":{"taskId":1},"message":"starting task ID 1","sequence":0,"time":1506776210000,"version":"1.0.0"}{"context":{"taskId":1},"message":"foo","sequence":1,"time":1506776210000,"version":"1.0.0"}{"context":{"taskId":1},"message":"successfully completed task ID 1","sequence":2,"time":1506776210000,"version":"1.0.0"}[...]
```

Si vous utilisez un [aggrégateur de logs](https://fr.wikipedia.org/wiki/Gestion_des_journaux) central, vous pouvez facilement trouver tous les logs associés à une tâche particulière. Cela est utile si vous enquêtez sur une erreur qui a terminé une tâche prématurément.

### Transports

Dans la plupart des bibliothèques de logging, un transport s'exécute en processus pour effectuer une opération avec la ligne de log finalisée. Par exemple, un transport peut envoyer la ligne de log à un serveur [syslog](https://fr.wikipedia.org/wiki/Syslog) standard après l'avoir traitée et reformattée.

Roarr ne supporte pas les transports en processus car les processus Node sont des processus à thread unique. Roarr délègue la gestion des logs à des processus externes afin que les capacités de threading du système d'exploitation ou d'autres CPU puissent être utilisées.

Selon votre configuration, envisagez l'un des transports de logs suivants :

* [Beats](https://www.elastic.co/products/beats)
Pour l'agrégation au niveau du processus
Écrit en Go
* [logagent](https://github.com/sematext/logagent-js)
Pour l'agrégation au niveau du processus
Écrit en JavaScript
* [Fluentd](https://www.fluentd.org/)
Pour l'agrégation des logs au niveau de l'orchestration de conteneurs telle que Kubernetes
Écrit en Ruby

Dans le cas de Fluentd et Kubernetes, l'agrégation de tous les logs vers [ElasticSearch](https://www.elastic.co/) est aussi simple que la création d'un seul [DaemonSet](https://github.com/fluent/fluentd-kubernetes-daemonset/blob/master/fluentd-daemonset-elasticsearch.yaml).

### L'avenir de Roarr

La base de code de Roarr n'est pas compliquée. Le succès d'un projet comme Roarr dépend beaucoup de l'effet d'échelle. Plus les dépendances utilisent Roarr, plus il fournit de valeur.

Activer le logging permet de recueillir instantanément toutes les données sur les applications. Leurs composants nécessaires pour surveiller la santé de l'application et tracer les problèmes.

En un sens, j'ai de la chance. Au fil des années, j'ai développé une abstraction pour presque tous les composants qui composent mes applications Node.js et navigateur.

Celles-ci vont du [client de base de données](https://github.com/gajus/mightyql), [évaluateur DOM](https://github.com/gajus/surgeon), [gestionnaire de processus de serveur HTTP](https://github.com/gajus/express-process-manager), et ainsi de suite. Cela me permet de récolter rapidement les bénéfices d'un package comme Roarr.

Le temps montrera si le reste de la communauté adopte Roarr avec la même passion.

### Et le nom ?

J'ai reçu quelques critiques initiales sur l'utilisation d'un nom générique et "mignon" comme "roarr". La raison principale de choisir ce nom est d'identifier le package comme **bruyant**. Les logs Roarr ne peuvent pas être supprimés, tout comme le rugissement d'un tigre.

![Image](https://cdn-media-1.freecodecamp.org/images/PAvUF3-iTUPv0K8Cu491C2ILXZnaERwEwf9O)
_You're gonna hear me roar!_

D'un point de vue pratique, "ROARR" est un terme sûr à [grep](https://fr.wikipedia.org/wiki/Grep) et à réserver dans l'environnement global.

### Roarr !

Je standardise [Roarr](https://github.com/gajus/roarr) sur toutes les applications et packages Node.js que je maintiens.

Je m'attends à ce que cela améliore ma capacité à détecter rapidement les problèmes. Cela m'aidera à reconfigurer les paramètres de logging des applications existantes — sans modifier le code source pour ajuster les volumes de logs. Et cela améliorera mon expérience quotidienne de suivi des logs d'application.

![Image](https://cdn-media-1.freecodecamp.org/images/APUUTgMxzNkUqNDNLB1IYMw45XxizXx9fweh)
_Roarr!_

Le logging est l'une des parties les plus effrayantes du développement d'applications. Roarr le rend moins effrayant.

### Vous aimez lire, j'aime écrire

Vous pouvez soutenir mon [travail open-source](https://github.com/gajus) et mes articles techniques via [Buy Me A Coffee](https://www.buymeacoffee.com/gajus) et [Patreon](https://www.patreon.com/gajus). Vous aurez ma gratitude éternelle ?