---
title: Le manuel Deno – Un tutoriel sur le runtime TypeScript avec des exemples de
  code
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2020-05-12T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-deno-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-11-at-18.55.24.png
tags:
- name: Deno
  slug: deno
seo_title: Le manuel Deno – Un tutoriel sur le runtime TypeScript avec des exemples
  de code
seo_desc: 'I explore new projects every week, and it’s rare that one grabs my attention
  as much as Deno did.

  In this post I want to get you up to speed with Deno quickly. We''ll compare it
  with Node.js, and build your first REST API with it.

  Table of contents


  W...'
---

J'explore de nouveaux projets chaque semaine, et il est rare qu'un projet attire autant mon attention que [Deno](https://deno.land/).

Dans cet article, je souhaite vous familiariser rapidement avec Deno. Nous le comparerons avec Node.js et construirons votre première API REST avec lui.

## Table des matières

* [Qu'est-ce que Deno ?](#heading-questce-que-deno)
* [Pourquoi Deno ? Pourquoi maintenant ?](#heading-pourquoi-deno-pourquoi-maintenant)
* [Devriez-vous apprendre Deno ?](#heading-devriez-vous-apprendre-deno)
* [Va-t-il remplacer Node.js ?](#heading-va-t-il-remplacer-nodejs)
* [Support de première classe pour TypeScript](#heading-support-de-premiere-classe-pour-typescript)
* [Similitudes et différences avec Node.js](#heading-similitudes-et-differences-avec-nodejs)
* [Pas de gestionnaire de paquets](#heading-pas-de-gestionnaire-de-paquets)
* [Installer Deno](#heading-installer-deno)
* [Les commandes Deno](#heading-les-commandes-deno)
* [Votre première application Deno](#heading-votre-premiere-application-deno)
* [Exemples de code Deno](#heading-exemples-de-code-deno)
* [Votre première application Deno (pour de vrai)](#heading-votre-premiere-application-deno-pour-de-vrai)
* [Le bac à sable Deno](#heading-le-bac-a-sable-deno)
* [Formater le code](#heading-formater-le-code)
* [La bibliothèque standard](#heading-la-bibliothèque-standard)
* [Un autre exemple Deno](#heading-un-autre-exemple-deno)
* [Y a-t-il un Express/Hapi/Koa/* pour Deno ?](#heading-y-a-t-il-un-expresshapikoa-pour-deno)
* [Exemple : utiliser Oak pour construire une API REST](#heading-exemple-utiliser-oak-pour-construire-une-api-rest)
* [En savoir plus](#heading-en-savoir-plus)
* [Quelques autres informations aléatoires](#heading-quelques-autres-informations-aleatoires)

Et notez : [Vous pouvez obtenir une version PDF/ePub/Mobi de ce manuel Deno ici](https://flaviocopes.com/page/deno-handbook/).

## Qu'est-ce que Deno ?

Si vous êtes familier avec Node.js, l'écosystème JavaScript côté serveur populaire, alors Deno est similaire à Node. Sauf qu'il est profondément amélioré à bien des égards.

Commençons par une liste rapide des fonctionnalités que j'aime le plus chez Deno :

* Il est basé sur les fonctionnalités modernes du langage JavaScript
* Il dispose d'une bibliothèque standard extensive
* Il a TypeScript au cœur, ce qui apporte un énorme avantage de nombreuses manières différentes, y compris un support de première classe pour TypeScript (vous n'avez pas à compiler séparément TypeScript, c'est automatiquement fait par Deno)
* Il adopte les [modules ES](https://flaviocopes.com/es-modules/)
* Il n'a pas de gestionnaire de paquets
* Il a un `await` de première classe
* Il dispose d'une fonctionnalité de test intégrée
* Il vise à être compatible avec les navigateurs autant que possible, par exemple en fournissant un `fetch` intégré et l'objet global `window`

Nous explorerons toutes ces fonctionnalités dans ce guide.

Après avoir utilisé Deno et appris à apprécier ses fonctionnalités, Node.js semblera quelque chose de _vieux_.

Surtout parce que l'API Node.js est basée sur les callbacks, car elle a été écrite bien avant les promesses et async/await. Il n'y a pas de changement disponible pour cela dans Node, car un tel changement serait monumental. Nous sommes donc coincés avec les callbacks ou avec la promisification des appels API.

Node.js est **génial** et continuera d'être la norme de facto dans le monde JavaScript. Mais je pense que nous verrons progressivement Deno être adopté de plus en plus en raison de son support de première classe pour TypeScript et de sa bibliothèque standard moderne.

Deno peut se permettre d'avoir tout écrit avec des technologies modernes, puisque qu'il n'y a pas de compatibilité ascendante à maintenir. Bien sûr, il n'y a aucune garantie que dans une décennie la même chose arrivera à Deno et qu'une nouvelle technologie émergera, mais c'est la réalité du moment.

## Pourquoi Deno ? Pourquoi maintenant ?

Deno a été annoncé il y a presque 2 ans par le créateur original de Node.js, Ryan Dahl, lors de JSConf EU. Regardez [la vidéo YouTube de la conférence](https://www.youtube.com/watch?v=M3BM9TB-8yA), c'est très intéressant et c'est un visionnage obligatoire si vous êtes impliqué dans Node.js et JavaScript en général.

Chaque gestionnaire de projet doit prendre des décisions. Ryan regrettait certaines décisions initiales dans Node. De plus, la technologie évolue, et aujourd'hui JavaScript est un langage totalement différent de ce qu'il était en 2009 lorsque Node a commencé. Pensez aux fonctionnalités modernes ES6/2016/2017, et ainsi de suite.

Il a donc commencé un nouveau projet pour créer une sorte de deuxième vague d'applications côté serveur alimentées par JavaScript.

La raison pour laquelle j'écris ce guide maintenant et non à l'époque est que les technologies ont besoin de beaucoup de temps pour mûrir. Et nous avons enfin atteint **Deno 1.0** (1.0 devrait être publié le 13 mai 2020), la première version de Deno officiellement déclarée stable.

Cela peut sembler être juste un numéro, mais 1.0 signifie qu'il n'y aura pas de changements majeurs jusqu'à Deno 2.0. C'est une grande affaire lorsque vous plongez dans une nouvelle technologie - vous ne voulez pas apprendre quelque chose et puis le voir changer trop vite.

## Devriez-vous apprendre Deno ?

C'est une grande question.

Apprendre quelque chose de nouveau comme Deno est un grand effort. Ma suggestion est que si vous commencez maintenant avec le JS côté serveur et que vous ne connaissez pas encore Node, et que vous n'avez jamais écrit de TypeScript, je commencerais par Node.

Personne n'a jamais été licencié pour avoir choisi Node.js (en paraphrasant une citation courante).

Mais si vous aimez TypeScript, ne dépendez pas d'un milliard de paquets npm dans vos projets et que vous voulez utiliser `await` partout, hey Deno pourrait être ce que vous cherchez.

## Va-t-il remplacer Node.js ?

Non. Node.js est un géant, bien établi, une technologie incroyablement bien soutenue qui va rester pendant des décennies.

## Support de première classe pour TypeScript

Deno est écrit en Rust et TypeScript, deux des langages qui croissent vraiment vite aujourd'hui.

En particulier, être écrit en TypeScript signifie que nous obtenons beaucoup des avantages de TypeScript même si nous choisissons d'écrire notre code en JavaScript simple.

Et exécuter du code TypeScript avec Deno ne nécessite pas d'étape de compilation - Deno le fait automatiquement pour vous.

Vous n'êtes pas obligé d'écrire en TypeScript, mais le fait que le cœur de Deno soit écrit en TypeScript est énorme.

Premièrement, un pourcentage de plus en plus grand de programmeurs JavaScript adorent TypeScript.

Deuxièmement, les outils que vous utilisez peuvent déduire beaucoup d'informations sur le logiciel écrit en TypeScript, comme Deno.

Cela signifie que lorsque nous codons dans VS Code, par exemple (qui a bien sûr une intégration étroite avec TypeScript puisque les deux sont développés chez MicroSoft), nous pouvons obtenir des avantages comme la vérification des types pendant que nous écrivons notre code, et des fonctionnalités avancées d'[IntelliSense](https://code.visualstudio.com/docs/editor/intellisense). En d'autres termes, l'éditeur peut nous aider de manière profondément utile.

## Similitudes et différences avec Node.js

Puisque Deno est essentiellement un remplacement de Node.js, il est utile de comparer les deux directement.

Similitudes :

* Tous deux sont développés sur le [moteur V8 Chromium](https://flaviocopes.com/v8/)
* Tous deux sont excellents pour développer côté serveur avec JavaScript

Différences :

* Node est écrit en C++ et JavaScript. Deno est écrit en Rust et TypeScript.
* Node a un gestionnaire de paquets officiel appelé `npm`. Deno n'en a pas, et permet plutôt d'importer n'importe quel module ES depuis des URLs.
* Node utilise la syntaxe CommonJS pour importer des paquets. Deno utilise les modules ES, la manière officielle.
* Deno utilise les fonctionnalités modernes d'ECMAScript dans toutes ses API et bibliothèque standard, tandis que Node.js utilise une bibliothèque standard basée sur les callbacks et n'a pas de plans pour la mettre à niveau.
* Deno offre une couche de sécurité de bac à sable à travers des permissions. Un programme ne peut accéder qu'aux permissions définies pour l'exécutable en tant que flags par l'utilisateur. Un programme Node.js peut accéder à tout ce à quoi l'utilisateur peut accéder.
* Deno a depuis longtemps envisagé la possibilité de compiler un programme en un exécutable que vous pouvez exécuter sans dépendances externes, comme Go, mais [ce n'est toujours pas une chose encore](https://github.com/denoland/deno/issues/986). Ce serait un changement de jeu.

## Pas de gestionnaire de paquets

Ne pas avoir de gestionnaire de paquets et devoir s'appuyer sur des URLs pour héberger et importer des paquets a des avantages et des inconvénients. J'aime vraiment les avantages : c'est très flexible, et nous pouvons créer des paquets sans les publier sur un dépôt comme npm.

Je pense qu'une sorte de gestionnaire de paquets émergera, mais rien d'officiel n'est encore sorti.

Le site web de Deno fournit l'hébergement de code (et ainsi la distribution via des URLs) pour les paquets tiers : [https://deno.land/x/](https://deno.land/x/)

## Installer Deno

Assez parlé ! Installons Deno.

La manière la plus simple est d'utiliser [Homebrew](https://flaviocopes.com/homebrew/) :

```sh
brew install deno
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-12.04.45.jpg)

Une fois cela fait, vous aurez accès à la commande `deno`. Voici l'aide que vous pouvez obtenir en utilisant `deno --help` :

```
flavio@mbp~> deno --help
deno 0.42.0
A secure JavaScript and TypeScript runtime

Docs: https://deno.land/std/manual.md
Modules: https://deno.land/std/ https://deno.land/x/
Bugs: https://github.com/denoland/deno/issues

To start the REPL, supply no arguments:
  deno

To execute a script:
  deno run https://deno.land/std/examples/welcome.ts
  deno https://deno.land/std/examples/welcome.ts

To evaluate code in the shell:
  deno eval "console.log(30933 + 404)"

Run 'deno help run' for 'run'-specific flags.

USAGE:
    deno [OPTIONS] [SUBCOMMAND]

OPTIONS:
    -h, --help
            Prints help information

    -L, --log-level <log-level>
            Set log level [possible values: debug, info]

    -q, --quiet
            Suppress diagnostic output
            By default, subcommands print human-readable diagnostic messages to stderr.
            If the flag is set, restrict these messages to errors.
    -V, --version
            Prints version information


SUBCOMMANDS:
    bundle         Bundle module and dependencies into single file
    cache          Cache the dependencies
    completions    Generate shell completions
    doc            Show documentation for a module
    eval           Eval script
    fmt            Format source files
    help           Prints this message or the help of the given subcommand(s)
    info           Show info about cache or info related to source file
    install        Install script as an executable
    repl           Read Eval Print Loop
    run            Run a program given a filename or url to the module
    test           Run tests
    types          Print runtime TypeScript declarations
    upgrade        Upgrade deno executable to newest version

ENVIRONMENT VARIABLES:
    DENO_DIR             Set deno's base directory (defaults to $HOME/.deno)
    DENO_INSTALL_ROOT    Set deno install's output directory
                         (defaults to $HOME/.deno/bin)
    NO_COLOR             Set to disable color
    HTTP_PROXY           Proxy address for HTTP requests
                         (module downloads, fetch)
    HTTPS_PROXY          Same but for HTTPS
```

## Les commandes Deno

Notez la section `SUBCOMMANDS` dans l'aide, qui liste toutes les commandes que nous pouvons exécuter. Quelles sous-commandes avons-nous ?

* `bundle` regrouper le module et les dépendances d'un projet en un seul fichier
* `cache` mettre en cache les dépendances
* `completions` générer des complétions shell
* `doc` montrer la documentation pour un module
* `eval` évaluer un morceau de code, par exemple `deno eval "console.log(1 + 2)"`
* `fmt` un formateur de code intégré (similaire à `gofmt` en Go)
* `help` imprime ce message ou l'aide de la/des sous-commande(s) donnée(s)
* `info` montrer des informations sur le cache ou des informations liées au fichier source
* `install` installer le script en tant qu'exécutable
* `repl` Read-Eval-Print-Loop (par défaut)
* `run` exécuter un programme donné un nom de fichier ou une URL vers le module
* `test` exécuter des tests
* `types` imprimer les déclarations TypeScript d'exécution
* `upgrade` mettre à niveau `deno` vers la version la plus récente

Vous pouvez exécuter `deno <subcommand> help` pour obtenir une documentation supplémentaire spécifique à la commande, par exemple `deno run --help`.

Comme l'aide le dit, nous pouvons utiliser cette commande pour démarrer un REPL (Read-Execute-Print-Loop) en utilisant `deno` sans aucune autre option.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-12.07.50.png)

C'est la même chose que d'exécuter `deno repl`.

Une manière plus courante d'utiliser cette commande est d'exécuter une application Deno contenue dans un fichier TypeScript.

Vous pouvez exécuter à la fois des fichiers TypeScript (`.ts`) ou JavaScript (`.js`).

Si vous n'êtes pas familier avec TypeScript, ne vous inquiétez pas : Deno est écrit en TypeScript, mais vous pouvez écrire vos applications "client" en JavaScript.

_Mon [tutoriel TypeScript](https://flaviocopes.com/typescript/) vous aidera à démarrer rapidement avec TypeScript si vous le souhaitez._

## Votre première application Deno

Exécutons une application Deno pour la première fois.

Ce que je trouve assez incroyable, c'est que vous n'avez même pas à écrire une seule ligne - vous pouvez exécuter une commande à partir de n'importe quelle URL.

Deno télécharge le programme, le compile et l'exécute :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-12.22.30.jpg)

_Bien sûr, exécuter du code arbitraire depuis Internet n'est pas une pratique que je recommanderais généralement. Dans ce cas, nous l'exécutons depuis le site officiel de Deno, de plus Deno dispose d'un bac à sable qui empêche les programmes de faire quoi que ce soit que vous ne souhaitez pas autoriser. Plus d'informations à ce sujet plus tard._

Ce programme est très simple, juste un appel à `console.log()` :

```ts
console.log('Bienvenue dans Deno 💡')

```

Si vous ouvrez l'URL [https://deno.land/std/examples/welcome.ts](https://deno.land/std/examples/welcome.ts) avec le navigateur, vous verrez cette page :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-13.50.00.png)

Bizarre, non ? Vous vous attendriez probablement à un fichier TypeScript, mais nous avons une page web. La raison est que le serveur web du site Deno sait que vous utilisez un navigateur et vous sert une page plus conviviale.

Téléchargez la même URL en utilisant `wget`, par exemple, qui demande la version `text/plain` au lieu de `text/html` :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-13.52.25.png)

Si vous voulez exécuter le programme à nouveau, il est maintenant mis en cache par Deno et n'a pas besoin d'être téléchargé à nouveau :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-12.22.47.jpg)

Vous pouvez forcer un rechargement de la source originale avec le flag `--reload` :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-12.28.57.jpg)

`deno run` a beaucoup d'options différentes qui n'étaient pas listées dans `deno --help`. Au lieu de cela, vous devez exécuter `deno run --help` pour les révéler :

```
flavio@mbp~> deno run --help
deno-run
Run a program given a filename or url to the module.

By default all programs are run in sandbox without access to disk, network or
ability to spawn subprocesses.
  deno run https://deno.land/std/examples/welcome.ts

Grant all permissions:
  deno run -A https://deno.land/std/http/file_server.ts

Grant permission to read from disk and listen to network:
  deno run --allow-read --allow-net https://deno.land/std/http/file_server.ts

Grant permission to read whitelisted files from disk:
  deno run --allow-read=/etc https://deno.land/std/http/file_server.ts

USAGE:
    deno run [OPTIONS] <SCRIPT_ARG>...

OPTIONS:
    -A, --allow-all
            Allow all permissions

        --allow-env
            Allow environment access

        --allow-hrtime
            Allow high resolution time measurement

        --allow-net=<allow-net>
            Allow network access

        --allow-plugin
            Allow loading plugins

        --allow-read=<allow-read>
            Allow file system read access

        --allow-run
            Allow running subprocesses

        --allow-write=<allow-write>
            Allow file system write access

        --cached-only
            Require that remote dependencies are already cached

        --cert <FILE>
            Load certificate authority from PEM encoded file

    -c, --config <FILE>
            Load tsconfig.json configuration file

    -h, --help
            Prints help information

        --importmap <FILE>
            UNSTABLE:
            Load import map file
            Docs: https://deno.land/std/manual.md#import-maps
            Specification: https://wicg.github.io/import-maps/
            Examples: https://github.com/WICG/import-maps#the-import-map
        --inspect=<HOST:PORT>
            activate inspector on host:port (default: 127.0.0.1:9229)

        --inspect-brk=<HOST:PORT>
            activate inspector on host:port and break at start of user script

        --lock <FILE>
            Check the specified lock file

        --lock-write
            Write lock file. Use with --lock.

    -L, --log-level <log-level>
            Set log level [possible values: debug, info]

        --no-remote
            Do not resolve remote modules

    -q, --quiet
            Suppress diagnostic output
            By default, subcommands print human-readable diagnostic messages to stderr.
            If the flag is set, restrict these messages to errors.
    -r, --reload=<CACHE_BLACKLIST>
            Reload source code cache (recompile TypeScript)
            --reload
              Reload everything
            --reload=https://deno.land/std
              Reload only standard modules
            --reload=https://deno.land/std/fs/utils.ts,https://deno.land/std/fmt/colors.ts
              Reloads specific modules
        --seed <NUMBER>
            Seed Math.random()

        --unstable
            Enable unstable APIs

        --v8-flags=<v8-flags>
            Set V8 command line options. For help: --v8-flags=--help


ARGS:
    <SCRIPT_ARG>...
            script args
```

## Exemples de code Deno

En plus de celui que nous avons exécuté ci-dessus, le site web de Deno fournit quelques autres exemples que vous pouvez consulter : [https://deno.land/std/examples/](https://deno.land/std/examples/).

Au moment de l'écriture, nous pouvons trouver :

* `cat.ts` imprime le contenu d'une liste de fichiers fournis comme arguments
* `catj.ts` imprime le contenu d'une liste de fichiers fournis comme arguments
* `chat/` une implémentation d'un chat
* `colors.ts` un exemple de
* `curl.ts` une implémentation simple de `curl` qui imprime le contenu de l'URL spécifiée comme argument
* `echo_server.ts` un serveur TCP echo
* `gist.ts` un programme pour poster des fichiers sur gist.github.com
* `test.ts` une suite de tests exemple
* `welcome.ts` une simple déclaration console.log (le premier programme que nous avons exécuté ci-dessus)
* `xeval.ts` vous permet d'exécuter n'importe quel code TypeScript pour n'importe quelle ligne d'entrée standard reçue. [Autrefois connu sous le nom de `deno xeval`](https://youtu.be/HjdJzNoT_qg?t=1932) mais depuis supprimé de la commande officielle.

## Votre première application Deno (pour de vrai)

Écrivons un peu de code.

Votre première application Deno que vous avez exécutée en utilisant `deno run https://deno.land/std/examples/welcome.ts` était une application que quelqu'un d'autre a écrite, donc vous n'avez rien vu concernant l'apparence du code Deno.

Nous commencerons par l'exemple d'application par défaut listé sur le site officiel de Deno :

```ts
import { serve } from 'https://deno.land/std/http/server.ts'
const s = serve({ port: 8000 })
console.log('http://localhost:8000/')
for await (const req of s) {
  req.respond({ body: 'Hello World\n' })
}

```

Ce code importe la fonction `serve` du module `http/server`. Vous voyez ? Nous n'avons pas à l'installer d'abord, et il n'est pas non plus stocké sur votre machine locale comme c'est le cas avec les modules Node. C'est une des raisons pour lesquelles l'installation de Deno a été si rapide.

Importer depuis `https://deno.land/std/http/server.ts` importe la dernière version du module. Vous pouvez importer une version spécifique en utilisant `@VERSION`, comme ceci :

```ts
import { serve } from 'https://deno.land/std@v0.42.0/http/server.ts'

```

La fonction `serve` est définie comme ceci dans ce fichier :

```ts
/**
 * Créer un serveur HTTP
 *
 *     import { serve } from "https://deno.land/std/http/server.ts";
 *     const body = "Hello World\n";
 *     const s = serve({ port: 8000 });
 *     for await (const req of s) {
 *       req.respond({ body });
 *     }
 */
export function serve(addr: string | HTTPOptions): Server {
  if (typeof addr === 'string') {
    const [hostname, port] = addr.split(':')
    addr = { hostname, port: Number(port) }
  }

  const listener = listen(addr)
  return new Server(listener)
}

```

Nous procédons à l'instanciation d'un serveur en appelant la fonction `serve()` en passant un objet avec la propriété `port`.

Ensuite, nous exécutons cette boucle pour répondre à chaque requête provenant du serveur.

```ts
for await (const req of s) {
  req.respond({ body: 'Hello World\n' })
}

```

Notez que nous utilisons le mot-clé `await` sans avoir à l'envelopper dans une fonction `async` car Deno implémente [top-level await](https://flaviocopes.com/javascript-await-top-level/).

Exécutons ce programme localement. J'assume que vous utilisez [VS Code](https://flaviocopes.com/vscode/), mais vous pouvez utiliser n'importe quel éditeur que vous aimez.

Je recommande d'installer l'extension Deno de `justjavac` (il y en avait une autre avec le même nom lorsque j'ai essayé, mais elle est obsolète - elle pourrait disparaître à l'avenir)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-15.28.06.png)

L'extension fournira plusieurs utilitaires et fonctionnalités à VS Code pour vous aider à écrire vos applications.

Maintenant, créez un fichier `app.ts` dans un dossier et collez le code ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-15.40.18.png)

Maintenant, exécutez-le en utilisant `deno run app.ts` :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-15.39.28.jpg)

Deno télécharge toutes les dépendances dont il a besoin, en commençant par celle que nous avons importée.

Le fichier [https://deno.land/std/http/server.ts](https://deno.land/std/http/server.ts) a plusieurs dépendances propres :

```ts
import { encode } from '../encoding/utf8.ts'
import { BufReader, BufWriter } from '../io/bufio.ts'
import { assert } from '../testing/asserts.ts'
import { deferred, Deferred, MuxAsyncIterator } from '../async/mod.ts'
import {
  bodyReader,
  chunkedBodyReader,
  emptyReader,
  writeResponse,
  readRequest,
} from './_io.ts'
import Listener = Deno.Listener
import Conn = Deno.Conn
import Reader = Deno.Reader

```

et celles-ci sont importées automatiquement.

À la fin, nous avons un problème :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-15.42.05.png)

Qu'est-ce qui se passe ? Nous avons un problème de permission refusée.

Parlons du bac à sable.

## Le bac à sable Deno

J'ai mentionné précédemment que Deno dispose d'un bac à sable qui empêche les programmes de faire quoi que ce soit que vous ne souhaitez pas autoriser.

Qu'est-ce que cela signifie ?

L'une des choses que Ryan mentionne dans la conférence d'introduction de Deno est que parfois vous voulez exécuter un programme JavaScript en dehors du navigateur Web, et pourtant ne pas lui permettre d'accéder à tout ce qu'il veut sur votre système. Ou de communiquer avec le monde extérieur en utilisant un réseau.

Il n'y a rien qui empêche une application Node.js d'obtenir vos clés SSH ou toute autre chose sur votre système et de l'envoyer à un serveur. C'est pourquoi nous installons généralement uniquement des paquets Node depuis des sources de confiance. Mais comment pouvons-nous savoir si l'un des projets que nous utilisons est piraté et à son tour tout le monde d'autre aussi ?

Deno essaie de reproduire le même modèle de permission que le navigateur implémente. Aucun JavaScript s'exécutant dans le navigateur ne peut faire des choses louches sur votre système à moins que vous ne l'autorisiez explicitement.

En revenant à Deno, si un programme veut accéder au réseau comme dans le cas précédent, alors nous devons lui donner la permission.

Nous pouvons le faire en passant un flag lorsque nous exécutons la commande, dans ce cas `--allow-net` :

```sh
deno run --allow-net app.ts
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-15.48.41.png)

L'application exécute maintenant un serveur HTTP sur le port 8000 :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-15.49.02.png)

D'autres flags permettent à Deno de débloquer d'autres fonctionnalités :

* `--allow-env` autoriser l'accès à l'environnement
* `--allow-hrtime` autoriser la mesure du temps haute résolution
* `--allow-net=<allow-net>` autoriser l'accès au réseau
* `--allow-plugin` autoriser le chargement de plugins
* `--allow-read=<allow-read>` autoriser l'accès en lecture au système de fichiers
* `--allow-run` autoriser l'exécution de sous-processus
* `--allow-write=<allow-write>` autoriser l'accès en écriture au système de fichiers
* `--allow-all` autoriser toutes les permissions (identique à `-A`)

Les permissions pour `net`, `read` et `write` peuvent être granulaires. Par exemple, vous pouvez autoriser la lecture depuis un dossier spécifique en utilisant `--allow-read=/dev`

## Formater le code

L'une des choses que j'ai vraiment aimées avec Go était la commande `gofmt` qui accompagnait le compilateur Go. Tout le code Go se ressemble. Tout le monde utilise `gofmt`.

Les programmeurs JavaScript sont habitués à exécuter [Prettier](https://flaviocopes.com/prettier/), et `deno fmt` l'exécute en fait sous le capot.

Supposons que vous avez un fichier mal formaté comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-16.06.58.png)

Vous exécutez `deno fmt app.ts` et il est automatiquement formaté correctement, en ajoutant également des points-virgules là où ils manquent :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-16.07.25.png)

## La bibliothèque standard

La bibliothèque standard de Deno est extensive malgré le jeune âge du projet.

Elle inclut :

* `archive` utilitaires d'archives tar
* `async` utilitaires asynchrones
* `bytes` aides pour manipuler les tranches d'octets
* `datetime` analyse de date/heure
* `encoding` encodage/décodage pour divers formats
* `flags` analyse des flags de ligne de commande
* `fmt` formatage et impression
* `fs` API du système de fichiers
* `hash` bibliothèque crypto
* `http` serveur HTTP
* `io` bibliothèque d'E/S
* `log` utilitaires de journalisation
* `mime` support pour les données multipart
* `node` couche de compatibilité Node.js
* `path` manipulation de chemins
* `ws` websockets

## Un autre exemple Deno

Regardons un autre exemple d'une application Deno, depuis les exemples Deno : [`cat`](https://deno.land/std/examples/cat.ts) :

```ts
const filenames = Deno.args
for (const filename of filenames) {
  const file = await Deno.open(filename)
  await Deno.copy(file, Deno.stdout)
  file.close()
}

```

Cela assigne à la variable `filenames` le contenu de `Deno.args`, qui est une variable contenant tous les arguments envoyés à la commande.

Nous les parcourons, et pour chacun nous utilisons `Deno.open()` pour ouvrir le fichier et nous utilisons `Deno.copy()` pour imprimer le contenu du fichier dans `Deno.stdout`. Enfin, nous fermons le fichier.

Si vous exécutez cela en utilisant

```sh
deno run https://deno.land/std/examples/cat.ts
```

Le programme est téléchargé et compilé, et rien ne se passe car nous n'avons pas spécifié d'argument.

Essayez maintenant

```sh
deno run https://deno.land/std/examples/cat.ts app.ts
```

en supposant que vous avez `app.ts` du projet précédent dans le même dossier.

Vous obtiendrez une erreur de permission :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-17.06.31-1.png)

Parce que Deno interdit l'accès au système de fichiers par défaut. Accordez l'accès au dossier courant en utilisant `--allow-read=./` :

```
deno run --allow-read=./ https://deno.land/std/examples/cat.ts app.ts
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-09-at-17.07.54-6.png)

## Y a-t-il un Express/Hapi/Koa/* pour Deno ?

Oui, définitivement. Consultez des projets comme

* [deno-drash](https://github.com/drashland/deno-drash)
* [deno-express](https://github.com/NMathar/deno-express)
* [oak](https://github.com/oakserver/oak)
* [pogo](https://github.com/sholladay/pogo)
* [servest](https://github.com/keroxp/servest)

## Exemple : utiliser Oak pour construire une API REST

Je veux faire un exemple simple de la construction d'une API REST en utilisant Oak. Oak est intéressant car il est inspiré par [Koa](https://github.com/koajs/koa), le middleware Node.js populaire, et grâce à cela, il est très familier si vous l'avez utilisé auparavant.

L'API que nous allons construire est très simple.

Notre serveur stockera, en mémoire, une liste de chiens avec leur nom et leur âge.

Nous voulons :

* ajouter de nouveaux chiens
* lister les chiens
* obtenir des détails sur un chien spécifique
* retirer un chien de la liste
* mettre à jour l'âge d'un chien

Nous allons faire cela en TypeScript, mais rien ne vous empêche d'écrire l'API en JavaScript - vous supprimez simplement les types.

Créez un fichier `app.ts`.

Commençons par importer les objets `Application` et `Router` depuis Oak :

```ts
import { Application, Router } from 'https://deno.land/x/oak/mod.ts'

```

ensuite, nous obtenons les variables d'environnement PORT et HOST :

```ts
const env = Deno.env.toObject()
const PORT = env.PORT || 4000
const HOST = env.HOST || '127.0.0.1'

```

Par défaut, notre application s'exécutera sur localhost:4000.

Maintenant, nous créons l'application Oak et nous la démarrons :

```ts
const router = new Router()

const app = new Application()

app.use(router.routes())
app.use(router.allowedMethods())

console.log(`Écoute sur le port ${PORT}...`)

await app.listen(`${HOST}:${PORT}`)

```

Maintenant, l'application devrait compiler correctement.

Exécutez

```sh
deno run --allow-env --allow-net app.ts
```

et Deno téléchargera les dépendances :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-10-at-16.31.11.jpg)

et écoutera ensuite sur le port 4000.

Les prochaines fois que vous exécuterez la commande, Deno ignorera la partie installation car ces paquets sont déjà mis en cache :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-10-at-16.32.40.png)

En haut du fichier, définissons une interface pour un chien, puis déclarons un tableau initial `dogs` d'objets Dog :

```ts
interface Dog {
  name: string
  age: number
}

let dogs: Array<Dog> = [
  {
    name: 'Roger',
    age: 8,
  },
  {
    name: 'Syd',
    age: 7,
  },
]

```

Maintenant, implémentons réellement l'API.

Nous avons tout en place. Après avoir créé le routeur, ajoutons quelques fonctions qui seront invoquées chaque fois qu'un de ces endpoints est atteint :

```ts
const router = new Router()

router
  .get('/dogs', getDogs)
  .get('/dogs/:name', getDog)
  .post('/dogs', addDog)
  .put('/dogs/:name', updateDog)
  .delete('/dogs/:name', removeDog)

```

Vous voyez ? Nous définissons

* `GET /dogs`
* `GET /dogs/:name`
* `POST /dogs`
* `PUT /dogs/:name`
* `DELETE /dogs/:name`

Implémentons ceux-ci un par un.

Commençons par `GET /dogs`, qui retourne la liste de tous les chiens :

```ts
export const getDogs = ({ response }: { response: any }) => {
  response.body = dogs
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-10-at-16.47.53.png)

Ensuite, voici comment nous pouvons récupérer un chien spécifique par son nom :

```ts
export const getDog = ({
  params,
  response,
}: {
  params: {
    name: string
  }
  response: any
}) => {
  const dog = dogs.filter((dog) => dog.name === params.name)
  if (dog.length) {
    response.status = 200
    response.body = dog[0]
    return
  }

  response.status = 400
  response.body = { msg: `Cannot find dog ${params.name}` }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-10-at-16.48.02.png)

Voici comment nous ajoutons un nouveau chien :

```ts
export const addDog = async ({
  request,
  response,
}: {
  request: any
  response: any
}) => {
  const body = await request.body()
  const dog: Dog = body.value
  dogs.push(dog)

  response.body = { msg: 'OK' }
  response.status = 200
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-10-at-16.47.41.png)

Remarquez que j'ai maintenant utilisé `const body = await request.body()` pour obtenir le contenu du corps, puisque les valeurs `name` et `age` sont passées en JSON.

Voici comment nous mettons à jour l'âge d'un chien :

```ts
export const updateDog = async ({
  params,
  request,
  response,
}: {
  params: {
    name: string
  }
  request: any
  response: any
}) => {
  const temp = dogs.filter((existingDog) => existingDog.name === params.name)
  const body = await request.body()
  const { age }: { age: number } = body.value

  if (temp.length) {
    temp[0].age = age
    response.status = 200
    response.body = { msg: 'OK' }
    return
  }

  response.status = 400
  response.body = { msg: `Cannot find dog ${params.name}` }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-10-at-16.48.11.png)

et voici comment nous pouvons retirer un chien de notre liste :

```ts
export const removeDog = ({
  params,
  response,
}: {
  params: {
    name: string
  }
  response: any
}) => {
  const lengthBefore = dogs.length
  dogs = dogs.filter((dog) => dog.name !== params.name)

  if (dogs.length === lengthBefore) {
    response.status = 400
    response.body = { msg: `Cannot find dog ${params.name}` }
    return
  }

  response.body = { msg: 'OK' }
  response.status = 200
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-10-at-16.48.32.png)

Voici le code complet de l'exemple :

```ts
import { Application, Router } from 'https://deno.land/x/oak/mod.ts'

const env = Deno.env.toObject()
const PORT = env.PORT || 4000
const HOST = env.HOST || '127.0.0.1'

interface Dog {
  name: string
  age: number
}

let dogs: Array<Dog> = [
  {
    name: 'Roger',
    age: 8,
  },
  {
    name: 'Syd',
    age: 7,
  },
]

export const getDogs = ({ response }: { response: any }) => {
  response.body = dogs
}

export const getDog = ({
  params,
  response,
}: {
  params: {
    name: string
  }
  response: any
}) => {
  const dog = dogs.filter((dog) => dog.name === params.name)
  if (dog.length) {
    response.status = 200
    response.body = dog[0]
    return
  }

  response.status = 400
  response.body = { msg: `Cannot find dog ${params.name}` }
}

export const addDog = async ({
  request,
  response,
}: {
  request: any
  response: any
}) => {
  const body = await request.body()
  const { name, age }: { name: string; age: number } = body.value
  dogs.push({
    name: name,
    age: age,
  })

  response.body = { msg: 'OK' }
  response.status = 200
}

export const updateDog = async ({
  params,
  request,
  response,
}: {
  params: {
    name: string
  }
  request: any
  response: any
}) => {
  const temp = dogs.filter((existingDog) => existingDog.name === params.name)
  const body = await request.body()
  const { age }: { age: number } = body.value

  if (temp.length) {
    temp[0].age = age
    response.status = 200
    response.body = { msg: 'OK' }
    return
  }

  response.status = 400
  response.body = { msg: `Cannot find dog ${params.name}` }
}

export const removeDog = ({
  params,
  response,
}: {
  params: {
    name: string
  }
  response: any
}) => {
  const lengthBefore = dogs.length
  dogs = dogs.filter((dog) => dog.name !== params.name)

  if (dogs.length === lengthBefore) {
    response.status = 400
    response.body = { msg: `Cannot find dog ${params.name}` }
    return
  }

  response.body = { msg: 'OK' }
  response.status = 200
}

const router = new Router()
router
  .get('/dogs', getDogs)
  .get('/dogs/:name', getDog)
  .post('/dogs', addDog)
  .put('/dogs/:name', updateDog)
  .delete('/dogs/:name', removeDog)

const app = new Application()

app.use(router.routes())
app.use(router.allowedMethods())

console.log(`Listening on port ${PORT}...`)

await app.listen(`${HOST}:${PORT}`)

```

## En savoir plus

Le site officiel de Deno est [https://deno.land](https://deno.land/)

La documentation de l'API est disponible à [https://doc.deno.land](https://doc.deno.land/) et [https://deno.land/typedoc/index.html](https://deno.land/typedoc/index.html)

awesome-deno [https://github.com/denolib/awesome-deno](https://github.com/denolib/awesome-deno)

## Quelques autres informations aléatoires

* Deno fournit une implémentation intégrée de `fetch` qui correspond à celle disponible dans le navigateur
* Deno a une couche de compatibilité avec la stdlib de Node.js [en cours](https://github.com/denoland/deno/tree/master/std/node)

## Mots de la fin

J'espère que vous avez apprécié ce tutoriel sur Deno !

Rappel : [Vous pouvez obtenir une version PDF/ePub/Mobi de ce manuel Deno ici](https://flaviocopes.com/page/deno-handbook/).