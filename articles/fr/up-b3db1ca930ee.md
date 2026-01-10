---
title: 'UP : déployez des applications serverless en quelques secondes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-11T00:20:34.000Z'
originalURL: https://freecodecamp.org/news/up-b3db1ca930ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8KijrYCm1j0_XvrACQD_fQ.png
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'UP : déployez des applications serverless en quelques secondes'
seo_desc: 'By TJ Holowaychuk

  Last year I wrote Blueprints for Up, describing how most of the building blocks
  are available to create a great serverless experience on AWS with minimal effort.
  This post talks about the initial alpha release of Up.

  Why focus on se...'
---

Par TJ Holowaychuk

L'année dernière, j'ai écrit [Blueprints for Up](https://medium.com/@tjholowaychuk/blueprints-for-up-1-5f8197179275), décrivant comment la plupart des éléments de base sont disponibles pour créer une excellente expérience serverless sur AWS avec un effort minimal. Cet article parle de la première version alpha de [**Up**](https://github.com/apex/up).

Pourquoi se concentrer sur le serverless ? Pour commencer, c'est rentable puisque vous payez à la demande, uniquement pour ce que vous utilisez. Les options serverless sont auto-réparatrices, car chaque requête est isolée et considérée comme "sans état". Et enfin, cela s'adapte indéfiniment avec facilité — il n'y a pas de machines ou de clusters à gérer. Déployez votre code et vous avez terminé.

Il y a environ un mois, j'ai décidé de commencer à travailler dessus sur [**apex/up**](https://github.com/apex/up), et j'ai écrit la première petite application serverless d'exemple [**tj/gh-polls**](https://github.com/tj/gh-polls) pour des sondages GitHub SVG en direct. Cela a bien fonctionné et coûte moins de 1 $/mois pour servir des millions de sondages, alors j'ai pensé continuer avec le projet et voir si je peux offrir des variantes open-source et commerciales.

L'objectif à long terme est de fournir un "Bring your own Heroku" de sorte, supportant de nombreuses plateformes. Bien que la Plateforme-en-tant-que-Service ne soit pas nouvelle, l'écosystème serverless rend ce type de programme de plus en plus trivial. Cela dit, AWS et autres souffrent souvent en termes d'UX en raison de la flexibilité qu'ils offrent. Up abstrait la complexité, tout en vous fournissant une solution pratiquement sans ops.

### Installation

Vous pouvez installer Up avec la commande suivante, et consulter la [documentation temporaire](https://github.com/apex/up/tree/master/docs) pour commencer. Ou si vous êtes méfiant à l'égard des scripts d'installation, téléchargez une [version binaire](https://github.com/apex/up/releases). (Gardez à l'esprit que ce projet est encore en développement.)

```
curl -sfL https://raw.githubusercontent.com/apex/up/master/install.sh | sh
```

Pour mettre à jour vers la dernière version à tout moment, exécutez simplement :

```
up upgrade
```

Vous pouvez également installer via NPM :

```
npm install -g up
```

### Fonctionnalités

Quelles fonctionnalités offre la première alpha ? Examinons cela ! Gardez à l'esprit qu'Up n'est pas un service hébergé, donc vous aurez besoin d'un compte AWS et de [certificats AWS](https://github.com/apex/up/blob/master/docs/aws-credentials.md). Si vous n'êtes pas du tout familier avec AWS, vous voudrez peut-être attendre jusqu'à ce que ce processus soit simplifié.

La première question que je reçois toujours est : comment up(1) diffère-t-il de [apex(1)](https://github.com/apex/apex) ? Apex se concentre sur le déploiement de fonctions, pour les pipelines et le traitement d'événements, tandis qu'Up se concentre sur les applications, les API et les sites statiques, c'est-à-dire des unités déployables uniques. Apex ne provisionne pas API Gateway, les certificats SSL ou DNS pour vous, ni ne fournit la réécriture d'URL, l'injection de scripts, etc.

#### Applications serverless en une seule commande

Up vous permet de déployer des applications, des API et des sites statiques avec une seule commande. Pour créer une application, tout ce dont vous avez besoin est un seul fichier, dans le cas de Node.js, un `./app.js` écoutant sur `PORT` qui est fourni par Up. Notez que si vous utilisez un `package.json`, Up détectera et utilisera les scripts `start` et `build`.

```
const http = require('http')const { PORT = 3000 } = process.env
```

```
http.createServer((req, res) => {  res.end('Hello World\n')}).listen(PORT)
```

Des [runtimes](https://github.com/apex/up/blob/master/docs/runtimes.md) supplémentaires sont supportés dès le départ, comme `main.go` pour Golang, donc vous pouvez déployer des applications Golang, Python, Crystal ou Node.js en quelques secondes.

```
package main
```

```
import ( "fmt" "log" "net/http" "os")
```

```
func main() { addr := ":" + os.Getenv("PORT") http.HandleFunc("/", hello) log.Fatal(http.ListenAndServe(addr, nil))}
```

```
func hello(w http.ResponseWriter, r *http.Request) { fmt.Fprintln(w, "Hello World from Go")}
```

Pour déployer l'application, tapez `up` pour créer les ressources nécessaires et déployer l'application elle-même. Il n'y a pas de fumée et de miroirs ici, une fois qu'il dit "complet", vous avez terminé, l'application est immédiatement disponible — il n'y a pas de processus de construction à distance.

![Image](https://cdn-media-1.freecodecamp.org/images/hoOnj34LXHHf6PPjMazQisygkQcz1zFLU8Og)

Les déploiements suivants seront encore plus rapides puisque la pile est déjà provisionnée :

![Image](https://cdn-media-1.freecodecamp.org/images/iX366ZZKvrJKWmj9PkBNeLxvwxO02RMIv1B1)

Testez votre application avec `up url --open` pour la voir dans le navigateur, `up url --copy` pour sauvegarder l'URL dans le presse-papiers, ou essayez-la avec curl :

```
curl `up url`Hello World
```

Pour supprimer l'application et ses ressources, tapez simplement `up stack delete` :

![Image](https://cdn-media-1.freecodecamp.org/images/oi9CiCIWCzMRlIhqvv2hea679FezY1N-VnRA)

Déployez dans les environnements de staging ou de production en utilisant `up staging` ou `up production`, et `up url --open production` par exemple. Notez que les domaines personnalisés ne sont pas encore disponibles, [ils le seront bientôt](https://github.com/apex/up/issues/166). Plus tard, vous pourrez également "promouvoir" une version vers d'autres étapes.

#### Reverse proxy

Une fonctionnalité qui rend Up unique est qu'il ne se contente pas simplement de déployer votre code, il place un reverse proxy Golang devant votre application. Cela fournit de nombreuses fonctionnalités telles que la réécriture d'URL, la redirection, l'injection de scripts et plus encore, que nous examinerons plus loin dans l'article.

#### Infrastructure as code

Up suit les meilleures pratiques modernes en termes de configuration, car toutes les modifications de l'infrastructure peuvent être prévisualisées avant d'être appliquées, et l'utilisation de politiques IAM peut également restreindre l'accès des développeurs pour prévenir les erreurs. Un avantage supplémentaire est qu'il aide à auto-documenter votre infrastructure.

Voici un exemple de configuration de certains enregistrements DNS (factices) et de certificats SSL gratuits via AWS ACM qui utilise Let's Encrypt.

```
{  "name": "app",  "dns": {    "myapp.com": [      {        "name": "myapp.com",        "type": "A",        "ttl": 300,        "value": ["35.161.83.243"]      },      {        "name": "blog.myapp.com",        "type": "CNAME",        "ttl": 300,        "value": ["34.209.172.67"]      },      {        "name": "api.myapp.com",        "type": "A",        "ttl": 300,        "value": ["54.187.185.18"]      }    ]  },  "certs": [    {      "domains": ["myapp.com", "*.myapp.com"]    }  ]}
```

Lorsque vous déployez l'application pour la première fois via `up`, toutes les permissions requises, API Gateway, la fonction Lambda, les certificats ACM, les enregistrements DNS Route53 et autres sont créés pour vous.

Les [ChangeSets](https://github.com/apex/up/issues/115) ne sont pas encore implémentés, mais vous pourrez prévisualiser les modifications ultérieures avec `up stack plan` et les valider avec `up stack apply`, un peu comme vous le feriez avec Terraform.

Consultez la [documentation de configuration](https://github.com/apex/up/blob/master/docs/configuration.md) pour plus d'informations.

#### Déploiements globaux

Le tableau `regions` vous permet de spécifier les régions cibles pour votre application. Par exemple, si vous n'êtes intéressé que par une seule région, vous utiliseriez :

```
{  "regions": ["us-west-2"]}
```

Si vos clients sont concentrés en Amérique du Nord, vous pouvez utiliser toutes les régions US et CA :

```
{  "regions": ["us-*", "ca-*"]}
```

Enfin, vous pouvez cibler les 14 régions actuellement supportées :

```
{  "regions": ["*"]}
```

La prise en charge multi-région est encore en cours de développement, car quelques nouvelles fonctionnalités AWS sont nécessaires pour lier les choses ensemble.

#### Service de fichiers statiques

Up prend en charge le service de fichiers statiques dès le départ, avec la prise en charge du cache HTTP, afin que vous puissiez utiliser CloudFront ou tout autre CDN devant votre application pour réduire considérablement la latence.

Par défaut, le répertoire de travail est servi (`.`) lorsque `type` est "static", cependant vous pouvez également fournir un `static.dir` :

```
{  "name": "app",  "type": "static",  "static": {    "dir": "public"  }}
```

#### Hooks de construction

Les hooks de construction vous permettent de définir des actions personnalisées lors du déploiement ou de l'exécution d'autres opérations. Un exemple courant serait de bundler les applications Node.js en utilisant Webpack ou Browserify, réduisant considérablement la taille du fichier, car node_modules est _énorme_.

```
{  "name": "app",  "hooks": {    "build": "browserify --node server.js > app.js",    "clean": "rm app.js"  }}
```

#### Injection de scripts et de feuilles de style

Up vous permet d'injecter des scripts et des styles, soit en ligne, soit des chemins de manière déclarative. Il prend même en charge un certain nombre de scripts "prêts à l'emploi" pour Google Analytics et [Segment](https://segment.com), il vous suffit de copier et coller votre clé d'écriture.

```
{  "name": "site",  "type": "static",  "inject": {    "head": [      {        "type": "segment",        "value": "API_KEY"      },      {        "type": "inline style",        "file": "/css/primer.css"      }    ],    "body": [      {        "type": "script",        "value": "/app.js"      }    ]  }}
```

#### Réécritures et redirections

Up prend en charge les redirections et la réécriture d'URL via l'objet `redirects`, qui mappe les motifs de chemin vers un nouvel emplacement. Si `status` est omis (ou 200), alors c'est une réécriture, sinon c'est une redirection.

```
{  "name": "app",  "type": "static",  "redirects": {    "/blog": {      "location": "https://blog.apex.sh/",      "status": 301    },    "/docs/:section/guides/:guide": {      "location": "/help/:section/:guide",      "status": 302    },    "/store/*": {      "location": "/shop/:splat"    }  }}
```

Un cas d'utilisation courant pour les réécritures est pour les SPAs (Single Page Apps), où vous souhaitez servir le fichier `index.html` indépendamment du chemin. À moins, bien sûr, que le fichier n'existe.

```
{  "name": "app",  "type": "static",  "redirects": {    "/*": {      "location": "/",      "status": 200    }  }}
```

Si vous souhaitez forcer la règle indépendamment de l'existence d'un fichier, ajoutez simplement `"force": true`.

#### Variables d'environnement

Les secrets seront dans la prochaine version, mais pour l'instant, les variables d'environnement en texte brut sont supportées :

```
{  "name": "api",  "environment": {    "API_FEATURE_FOO": "1",    "API_FEATURE_BAR": "0"  }}
```

#### Prise en charge CORS

La prise en charge [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) vous permet de spécifier quels domaines (le cas échéant) peuvent accéder à votre API depuis le navigateur. Si vous souhaitez permettre à n'importe quel site d'accéder à votre API, activez-le simplement :

```
{  "cors": {    "enable": true  }}
```

Vous pouvez également personnaliser l'accès, par exemple en restreignant l'accès à l'API à votre front-end ou SPA uniquement.

```
{  "cors": {    "allowed_origins": ["https://myapp.com"],    "allowed_methods": ["HEAD", "GET", "POST", "PUT", "DELETE"],    "allowed_headers": ["Content-Type", "Authorization"]  }}
```

#### Journalisation

Pour le prix modique de 0,5 $/Go, vous pouvez utiliser les journaux CloudWatch pour l'interrogation et le suivi des journaux structurés. Up implémente un langage de requête personnalisé [query language](https://github.com/apex/up/blob/master/internal/logs/parser/grammar.peg) utilisé pour améliorer ce que CloudWatch fournit, conçu spécialement pour l'interrogation des journaux JSON structurés.

![Image](https://cdn-media-1.freecodecamp.org/images/ofhAPQCmNmY5oEBkZrARay6DVwAgkNaiANxv)

Vous pouvez interroger les journaux existants :

```
up logs
```

Suivre les journaux en direct :

```
up logs -f
```

Ou filtrer sur l'un ou l'autre, par exemple en ne montrant que les requêtes GET / HEAD 200 qui prennent plus de 5 millisecondes à compléter :

```
up logs 'method in ("GET", "HEAD") status = 200 duration >= 5'
```

![Image](https://cdn-media-1.freecodecamp.org/images/kcVRNot18HGouxIaGWdUMK-4yF8nNgEiL495)

Le langage de requête est assez flexible, voici quelques exemples supplémentaires de `up help logs`

```
Show logs from the past 5 minutes.$ up logs
```

```
Show logs from the past 30 minutes.$ up logs -s 30m
```

```
Show logs from the past 5 hours.$ up logs -s 5h
```

```
Show live log output.$ up logs -f
```

```
Show error logs.$ up logs error
```

```
Show error and fatal logs.$ up logs 'error or fatal'
```

```
Show non-info logs.$ up logs 'not info'
```

```
Show logs with a specific message.$ up logs 'message = "user login"'
```

```
Show 200 responses with latency above 150ms.$ up logs 'status = 200 duration > 150'
```

```
Show 4xx and 5xx responses.$ up logs 'status >= 400'
```

```
Show emails containing @apex.sh.$ up logs 'user.email contains "@apex.sh"'
```

```
Show emails ending with @apex.sh.$ up logs 'user.email = "*@apex.sh"'
```

```
Show emails starting with tj@.$ up logs 'user.email = "tj@*"'
```

```
Show errors from /tobi and /loki$ up logs 'error and (path = "/tobi" or path = "/loki")'
```

```
Show the same as above with 'in'$ up logs 'error and path in ("/tobi", "/loki")'
```

```
Show logs with a more complex query.$ up logs 'method in ("POST", "PUT") ip = "207.*" status = 200 duration >= 50'
```

```
Pipe JSON error logs to the jq tool.$ up logs error | jq
```

Notez que le mot-clé `and` est implicite, bien que vous puissiez l'utiliser si vous préférez.

#### Temps de démarrage à froid

Ceci est une propriété d'AWS Lambda en tant que plateforme, mais les temps de démarrage à froid sont généralement bien inférieurs à 1 seconde, et à l'avenir, je prévois de fournir une option pour les maintenir au chaud.

#### Validation de la configuration

La commande `up config` affiche la configuration résolue, complète avec les paramètres par défaut et les paramètres d'exécution déduits — elle sert également le double objectif de valider la configuration, car toute erreur entraînera une sortie > 0.

#### Récupération après crash

Un autre avantage de l'utilisation d'Up en tant que reverse proxy est la récupération après crash — redémarrer votre serveur en cas de crash et réessayer la requête avant de répondre au client avec une erreur.

Par exemple, supposons que votre application Node.js plante avec une exception non capturée en raison d'un problème de base de données intermittent, Up peut réessayer cette requête avant de répondre au client. Plus tard, ce comportement sera plus personnalisable.

#### Compatible avec l'intégration continue

Il est difficile d'appeler cela une fonctionnalité, mais grâce aux binaires relativement petits et isolés de Golang, vous pouvez installer Up dans un CI en une ou deux secondes.

#### HTTP/2

Up prend en charge HTTP/2 dès le départ via API Gateway, réduisant la latence pour servir des applications et des sites avec de nombreux actifs. Je ferai des tests plus complets contre de nombreuses plateformes à l'avenir, mais la latence d'Up est déjà favorable :

![Image](https://cdn-media-1.freecodecamp.org/images/BeFu8CeylOCLKo1ivwQawmTWgH3A1nmtGew2)

#### Pages d'erreur

Up fournit une page d'erreur par défaut que vous pouvez personnaliser avec `error_pages` si vous souhaitez fournir une adresse e-mail de support ou ajuster la couleur.

```
{  "name": "site",  "type": "static",  "error_pages": {    "variables": {      "support_email": "support@apex.sh",      "color": "#228ae6"    }  }}
```

Par défaut, cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/s92GEApBB6rPdVA4yHBhhON9pgPx3Tk2ZGat)

Si vous souhaitez fournir des modèles personnalisés, vous pouvez créer un ou plusieurs des fichiers suivants. Le fichier le plus spécifique prend le pas.

* `error.html` — Correspond à n'importe quelle erreur 4xx ou 5xx
* `5xx.html` — Correspond à n'importe quelle erreur 5xx
* `4xx.html` — Correspond à n'importe quelle erreur 4xx
* `CODE.html` — Correspond à un code spécifique tel que 404.html

Consultez les [docs](https://github.com/apex/up/blob/master/docs/configuration.md#error-pages) pour en savoir plus sur les modèles.

### Évolutivité et coût

Vous avez donc lu jusqu'ici, mais à quel point Up est-il évolutif ? Actuellement, API Gateway et AWS sont la plateforme cible, donc vous n'êtes pas obligé de faire des changements pour évoluer, il suffit de déployer votre code et c'est fait. Vous ne payez que pour ce que vous utilisez réellement, à la demande, et aucune intervention manuelle n'est requise pour l'évolutivité.

AWS offre 1 000 000 de requêtes par mois gratuitement, mais vous pouvez utiliser [http://serverlesscalc.com](http://serverlesscalc.com/) pour entrer votre trafic prévu. À l'avenir, Up fournira des plateformes supplémentaires, afin que si l'une devient trop chère, vous puissiez migrer vers une autre !

### L'avenir

C'est tout pour l'instant ! Cela peut ne pas sembler beaucoup, mais cela dépasse déjà les 10 000 lignes de code, et je viens de commencer le développement. Jetez un coup d'œil à la file d'attente des problèmes pour un petit aperçu de ce à quoi s'attendre à l'avenir, en supposant que le projet devienne durable.

Si vous trouvez la version gratuite utile, envisagez de faire un don sur [OpenCollective](https://opencollective.com/apex-up), car je ne gagne pas d'argent en travaillant dessus. Je travaillerai bientôt sur l'accès anticipé à la version Pro, avec un prix annuel réduit pour les premiers adopteurs. Les éditions Pro ou Enterprise fourniront également le code source, afin que des correctifs internes et des personnalisations puissent être effectués.

Assurez-vous de suivre le [dépôt GitHub](https://github.com/apex/up) pour les mises à jour. Santé !