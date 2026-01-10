---
title: Comment écrire un client de base de données en ligne de commande en seulement
  10 minutes en utilisant OCLIF avec TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-04T20:30:30.000Z'
originalURL: https://freecodecamp.org/news/writing-a-command-line-database-client-in-10-minutes-aa608536ae4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*34f_Ia_d5E6WZPBQdKjhBw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: TypeScript
  slug: typescript
seo_title: Comment écrire un client de base de données en ligne de commande en seulement
  10 minutes en utilisant OCLIF avec TypeScript
seo_desc: 'By Michael Hunger

  This week I came across the “OCLIF, Open Source Command Line Framework” by SalesForce/Heroku
  in a medium post by Jeff Dickey.

  I was intrigued, it looked really easy and clean (thanks to TypeScript), and I knew
  from past experience t...'
---

Par Michael Hunger

Cette semaine, je suis tombé sur le [« OCLIF, Open Source Command Line Framework »](https://engineering.salesforce.com/open-sourcing-oclif-the-cli-framework-that-powers-our-clis-21fbda99d33a) de SalesForce/Heroku dans un article de [Jeff Dickey](https://www.freecodecamp.org/news/writing-a-command-line-database-client-in-10-minutes-aa608536ae4b/undefined).

J'étais intrigué, cela semblait vraiment facile et propre (grâce à TypeScript), et je savais d'après mon expérience passée qu'il y a beaucoup de tâches et de code boilerplate impliqués dans les CLIs. La [documentation](https://oclif.io/docs/) et les exemples semblaient également très bons.

J'ai passé beaucoup de temps dans neo4j-shell et [cypher-shell](http://github.com/neo4j/cypher-shell), tous deux en Java, alors je voulais essayer JavaScript (JS).

Ayant déjà utilisé le [neo4j-javascript-driver](https://github.com/neo4j/neo4j-javscript-driver) pour la visualisation de graphes, je savais qu'il était assez simple et rapide.

Le driver envoie des requêtes Cypher via le protocole binaire Bolt à la base de données et gère également le routage intelligent, les transactions et les nouvelles tentatives.

Pour une sortie joliment formatée, j'ai choisi `ascii-table`, une bibliothèque JS pratique pour produire des tableaux pour le terminal.

En gros, vous devez fournir une **url bolt**, un **nom d'utilisateur**, un **mot de passe** et une **requête** à exécuter, donc j'imagine que notre client ressemblera à ceci.

```
boltsh -a bolt://host:port -u neo4j -p pa55w0rd \  "MATCH (n:Person) RETURN n.name, n.age LIMIT 10"
```

### Vidéo

J'ai enregistré une session de ce codage. Cela revient à 15 minutes de runtime, principalement en raison de la frappe. N'hésitez pas à la regarder à 2x :)

### Exécuter une instance Neo4j

Pour faire fonctionner Neo4j avec des données, vous avez deux options. Vous pouvez installer [Neo4j Desktop](https://neo4j.com/download), qui est une application Electron pour gérer les bases de données, et créer un projet avec une base de données locale vide. Ou vous pouvez lancer un [Neo4j Sandbox](https://neo4j.com/sandbox), et choisir un « Blank Sandbox ».

Veuillez noter l'adresse IP du serveur et le port **bolt** ainsi que le **nom d'utilisateur** et le **mot de passe** de l'onglet « Détails ».

Dans les deux cas, après avoir lancé le « Neo4j Browser », qui est simplement un frontend basé sur React (et utilise également le neo4j-javascript-driver), veuillez entrer et exécuter dans la ligne de commande du haut.

```
:play movie graph
```

Cela vous donne un diaporama, où sur la deuxième page vous voyez une grande instruction pour créer des données d'exemple. Cliquez et exécutez cela, et vous devriez voir Tom Hanks visualisé avec un ensemble de ses films et certains des réalisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YsONV_kfRt-vuECP.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*be_udZXNJUtwdVYZ.png)

### Commencer avec OCLIF

C'est très simple — il suffit de décider si vous voulez un client multi-commandes ou mono-commande et d'exécuter la commande `npx` (exécuteur de paquets npm) appropriée.

```
npx oclif single boltsh
```

Cela vous pose quelques questions sur le nom, la licence et le dépôt github, et génère un squelette, dans notre cas pour un CLI mono-commande.

Pour voir si tout a fonctionné, vous pouvez exécuter la commande `./bin/run` et devriez voir une sortie comme ceci :

```
./bin/run
```

```
hello world from /Users/mh/d/js/boltsh/src/index.ts!
```

Ok, donc nous pouvons trouver le code à éditer dans ce fichier qui est une classe [Command](https://oclif.io/docs/commands.html). En l'ouvrant dans l'éditeur, nous voyons où ajouter une description, un exemple d'utilisation et les [flags](https://oclif.io/docs/flags.html) mentionnés ci-dessus.

Nous définissons tous les flags comme requis, et fournissons des valeurs par défaut pour `address` et `user`. Ensuite, nous ajoutons également l'[argument](https://oclif.io/docs/flags.html) `query`, qui est également requis.

```
import { Command, flags } from '@oclif/command'
```

```
class Boltsh extends Command {  static description = 'Exécuter des requêtes Cypher via Bolt'
```

```
  static examples = [    `$ boltsh -a bolt://localhost -u neo4j -p test \                 "MATCH (n:Person) return n.name"n.nameKeanu ReevesTom Hanks...`,  ]
```

```
  static flags = {    version: flags.version({ char: 'v' }),    help: flags.help({ char: 'h' }),
```

```
    address: flags.string({ char: 'a', description: 'adresse bolt',                       required: true, default: 'bolt://localhost' }),    user: flags.string({ char: 'u', description: 'utilisateur neo4j',                      required: true, default: 'neo4j' }),    password: flags.string({ char: 'p', required: true,                      description: 'mot de passe utilisateur' }),  }
```

```
  static args = [{ name: 'query', required: true,                    description: 'Requête Cypher à exécuter' }]
```

```
  async run() {    const { args, flags } = this.parse(Boltsh)
```

```
    this.log(`boltsh: ${flags.address} ${flags.user}               ${args.query} from ${__filename}!`)  }}
```

```
export = Boltsh
```

Nous affichons donc nos entrées de ligne de commande et nous essayons. Comme effet secondaire agréable, la commande `run` exécute également le compilateur TypeScript, donc nous n'avons pas à le faire manuellement.

```
./bin/run -p test "MATCH (n:Person) RETURN n.name"
```

```
boltsh: bolt://localhost neo4j MATCH (n:Person) RETURN n.name from /Users/mh/d/js/boltsh/src/index.ts!
```

Super, maintenant nous pouvons ajouter le driver neo4j et envoyer notre requête au serveur :

```
yarn add neo4j-driver
```

Ajoutez les imports en haut :

```
import * as neo4j from 'neo4j-driver'
```

Vous trouverez les détails de l'[API du driver Neo4j ici](https://neo4j.com/docs/api/javascript-driver/current/).

1. Nous allons créer un driver avec notre adresse, utilisateur et mot de passe, et acquérir une session, que nous utilisons pour exécuter la requête.
2. Obtenez les résultats et affichez les clés des enregistrements de la première ligne comme en-têtes et les valeurs de tous les enregistrements comme lignes, toutes séparées par des tabulations.
3. En bas, nous affichons également le nombre total de lignes et le temps pris à partir du résumé des résultats.

(Notez que le driver Neo4j utilise son propre type Number pour les nombres, car JavaScript ne peut pas exprimer les nombres 64 bits.)

```
async run() {  const { args, flags } = this.parse(Boltsh)
```

```
  const driver = neo4j.v1.driver(flags.address,                    neo4j.v1.auth.basic(flags.user, flags.password))  const session = driver.session()  const result = await session.run(args.query)  session.close()  driver.close()  const records = result.records;  if (records.length > 0) {    // en-tête    this.log(records[0].keys.join("\t"))    // lignes    records.forEach(r => this.log(                    r.keys.map(k => r.get(k)).join("\t")))
```

```
    this.log(`Returned ${records.length} row(s) in              ${result.summary.resultAvailableAfter.toNumber() +                result.summary.resultConsumedAfter.toNumber()} ms.`)  } else {    this.log('Aucun résultat.')  }}
```

Si nous exécutons notre test à nouveau, cela « fonctionne simplement ». Super !

```
./bin/run -p test "MATCH (n:Person) RETURN n.name limit 2"
```

```
n.nameKeanu ReevesCarrie-Anne MossReturned 2 row(s) in 3 ms.
```

Maintenant, nous pouvons le rendre joli avec `[ascii-table](https://github.com/sorensen/ascii-table)`

```
yarn add ascii-table
```

Comme ASCII-table ne vient pas avec une définition TypeScript, le compilateur générerait une erreur — c'est pourquoi nous devons déclarer le module dans un fichier séparé `src/ambient.d.ts` :

```
declare module 'ascii-table';
```

Encore une fois, ajoutez les imports. Cette fois, nous ajoutons un flag non requis `-t` qui active le mode tableau.

```
import * as AsciiTable from 'ascii-table'
```

Ensuite, nous construisons et affichons l'instance `AsciiTable` au lieu du texte brut lorsque ce flag est défini.

```
static flags = {  // ...  table: flags.boolean({ char: 't', description: 'Format Tableau' })}
```

```
async run() {  const { args, flags } = this.parse(Boltsh)
```

```
  const driver = neo4j.v1.driver(flags.address,                   neo4j.v1.auth.basic(flags.user, flags.password))  const session = driver.session()  const result = await session.run(args.query)  session.close()  driver.close()  const records = result.records;
```

```
  if (records.length > 0) {    // extraire les données à rendre    const data = { heading: records[0].keys,           rows: records.map(r => r.keys.map(k => r.get(k))) }
```

```
    if (flags.table) {      const table = AsciiTable.factory(data)      this.log(table.toString())    } else {      this.log(data.heading.join("\t"))      data.rows.forEach(r => this.log(r.join("\t")))    }
```

```
    this.log(`Returned ${records.length} row(s) in              ${result.summary.resultAvailableAfter.toNumber() +                  result.summary.resultConsumedAfter.toNumber()} ms.`)  } else {    this.log('Aucun résultat.')  }}
```

Alors essayons cela et voyons à quoi ressemble notre tableau :

```
./bin/run -p test -t "MATCH (n:Person) RETURN n.name limit 10"
```

```
.--------------------.|       n.name       ||--------------------|| Keanu Reeves       || Carrie-Anne Moss   || Laurence Fishburne || Hugo Weaving       || Lilly Wachowski    || Lana Wachowski     || Joel Silver        || Emil Eifrem        || Charlize Theron    || Al Pacino          |'--------------------'Returned 10 row(s) in 25 ms.
```

De plus, une requête plus complexe a l'air bien (sauf qu'elle est trop large pour Medium, donc capture d'écran). Cela affiche le nom des personnes, leur année de naissance et trois des films auxquels elles sont liées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sR0hkTOmoblU7jRx1Tedvg.jpeg)

Ce qui est bien avec OCLIF, c'est qu'il est livré avec tout ce qu'il faut. Par exemple, nous pouvons exécuter `boltsh --help` pour obtenir une page d'aide appropriée :

```
./bin/run --helpExecute Cypher Queries via Bolt
```

```
USAGE  $ boltsh QUERY
```

```
ARGUMENTS  QUERY  Cypher Query to Run
```

```
OPTIONS  -a, --address=address    (required) [default: bolt://localhost] bolt address  -h, --help               show CLI help  -p, --password=password  (required) user password  -u, --user=user          (required) [default: neo4j] neo4j user  -v, --version            show CLI version
```

```
EXAMPLE  $ boltsh -a bolt://localhost -u neo4j -p test \           "MATCH (n:Person) return n.name"  n.name  Keanu Reeves  Tom Hanks  ...
```

Dans l'article mentionné au début, Jeff montre comment construire un CLI multi-commandes. Le code est essentiellement le même que le nôtre, la seule différence étant que vous avez plusieurs commandes.

Consultez la [documentation](https://oclif.io/docs) et les [exemples](https://github.com/oclif?utf8=%E2%9C%93&q=example&type=&language=) d'OCLIF.

Le framework dispose d'une infrastructure de plugins, et il existe déjà [quelques plugins](https://github.com/oclif?utf8=%E2%9C%93&q=plugin&type=&language=), comme l'auto-mise à jour. J'espère que nous en verrons plus.

Je pense qu'OCLIF est vraiment bien fait par les gens de Heroku, grâce à [Jeff Dickey](https://www.freecodecamp.org/news/writing-a-command-line-database-client-in-10-minutes-aa608536ae4b/undefined).

Super, mission accomplie, il ne reste plus qu'à pousser vers [GitHub](https://github.com/jexp/boltsh) et [publier sur npm](https://www.npmjs.com/package/boltsh).

![Image](https://cdn-media-1.freecodecamp.org/images/1*i-Jkaoqfh-INzSkxOUrU7A.jpeg)

Alors pourquoi ne pas essayer et construire votre propre CLI ?

Bon codage !