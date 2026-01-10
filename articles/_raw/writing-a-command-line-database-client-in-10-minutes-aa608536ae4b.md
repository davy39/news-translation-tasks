---
title: How to write a command-line database client in just 10 minutes using OCLIF
  with TypeScript
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
seo_title: null
seo_desc: 'By Michael Hunger

  This week I came across the “OCLIF, Open Source Command Line Framework” by SalesForce/Heroku
  in a medium post by Jeff Dickey.

  I was intrigued, it looked really easy and clean (thanks to TypeScript), and I knew
  from past experience t...'
---

By Michael Hunger

This week I came across the [“OCLIF, Open Source Command Line Framework](https://engineering.salesforce.com/open-sourcing-oclif-the-cli-framework-that-powers-our-clis-21fbda99d33a)” by SalesForce/Heroku in a medium post by [Jeff Dickey](https://www.freecodecamp.org/news/writing-a-command-line-database-client-in-10-minutes-aa608536ae4b/undefined).

I was intrigued, it looked really easy and clean (thanks to TypeScript), and I knew from past experience that there is a lot of chores and boilerplate involved in CLIs. The [documentation](https://oclif.io/docs/) and examples also looked really good.

I spent a good amount of time in both neo4j-shell and [cypher-shell](http://github.com/neo4j/cypher-shell), both in Java, so I wanted to give JavaScript (JS) a try.

Having used the [neo4j-javascript-driver](https://github.com/neo4j/neo4j-javscript-driver) before for graph visualization, I knew it was quite straightforward and fast.

The driver sends Cypher queries via the binary Bolt protocol to the database and also handles smart routing, transactions, and retries.

For a pretty output, I chose `ascii-table` , a neat JS library to produce pretty tables for the terminal.

Basically, you have to provide a **bolt-url**, **username,** and **password** and a **query** to run, so I imagine our client to look like this.

```
boltsh -a bolt://host:port -u neo4j -p pa55w0rd \  "MATCH (n:Person) RETURN n.name, n.age LIMIT 10"
```

### Video

I recorded a session of doing this coding. It comes down to 15-minute runtime, mostly due to the typing. Feel free to watch it at 2x :)

### Running a Neo4j Instance

To get Neo4j running with some data, you have two options. You can install [Neo4j Desktop](https://neo4j.com/download), which is an electron app for managing databases, and create a project with a local, empty database. Or you can launch a [Neo4j Sandbox](https://neo4j.com/sandbox), and chose a “Blank Sandbox.”

Please note the server-IP address and the **bolt** port as well as **username** and **password** from the “Details” tab.

In both cases, after launching the “Neo4j Browser”, which is just a nice React-based frontend (and also uses the neo4j-javascript-driver), please enter and run in the top command-line.

```
:play movie graph
```

This gives you a slideshow, where on the second page you see a huge statement to create sample data. Click and run that, and you should see Tom Hanks visualized with a bunch of his movies and some of the directors.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YsONV_kfRt-vuECP.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*be_udZXNJUtwdVYZ.png)

### Getting started with OCLIF

It’s very straightforward — just decide if you want a multi- or single-command client and run the appropriate `npx` (npm package runner) command.

```
npx oclif single boltsh
```

This asks you a few questions about the name, license, and github-repo, and generates a skeleton, in our case for a single-command CLI.

To see if everything worked, you can run the `./bin/run` command and should see an output like this:

```
./bin/run
```

```
hello world from /Users/mh/d/js/boltsh/src/index.ts!
```

Ok, so we can find the code to edit in that file which is a [Command](https://oclif.io/docs/commands.html) class. Opening it in the editor, we see where to add a description, a usage example, and the [flags](https://oclif.io/docs/flags.html) mentioned above.

We set all flags to required, and provide defaults for `address` and `user`. Then we also add the `query` [argument](https://oclif.io/docs/flags.html), which is also required.

```
import { Command, flags } from '@oclif/command'
```

```
class Boltsh extends Command {  static description = 'Execute Cypher Queries via Bolt'
```

```
  static examples = [    `$ boltsh -a bolt://localhost -u neo4j -p test \                 "MATCH (n:Person) return n.name"n.nameKeanu ReevesTom Hanks...`,  ]
```

```
  static flags = {    version: flags.version({ char: 'v' }),    help: flags.help({ char: 'h' }),
```

```
    address: flags.string({ char: 'a', description: 'bolt address',                       required: true, default: 'bolt://localhost' }),    user: flags.string({ char: 'u', description: 'neo4j user',                      required: true, default: 'neo4j' }),    password: flags.string({ char: 'p', required: true,                      description: 'user password' }),  }
```

```
  static args = [{ name: 'query', required: true,                    description: 'Cypher Query to Run' }]
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

So we output our command line inputs and give it a go. As a nice side-effect, the `run` command also runs the TypeScript compiler, so we don’t have to do that manually.

```
./bin/run -p test "MATCH (n:Person) RETURN n.name"
```

```
boltsh: bolt://localhost neo4j MATCH (n:Person) RETURN n.name from /Users/mh/d/js/boltsh/src/index.ts!
```

Cool, now we can add the neo4j-driver and send our query to the server:

```
yarn add neo4j-driver
```

Add imports on top:

```
import * as neo4j from 'neo4j-driver'
```

You’ll find the details of the [Neo4j Driver API here](https://neo4j.com/docs/api/javascript-driver/current/).

1. We’ll create a driver with our address, user, and password, and acquire a session, which we use to run the query.
2. Get the results and output the record-keys of the first row as headers and the values of all records as rows, all tab-separated.
3. At the bottom, we also output the total number of rows and the time taken from the result-summary.

(Note that the Neo4j driver uses it’s own Number type for Numbers, as Javascript can’t express 64-bit numbers.)

```
async run() {  const { args, flags } = this.parse(Boltsh)
```

```
  const driver = neo4j.v1.driver(flags.address,                    neo4j.v1.auth.basic(flags.user, flags.password))  const session = driver.session()  const result = await session.run(args.query)  session.close()  driver.close()  const records = result.records;  if (records.length > 0) {    // header    this.log(records[0].keys.join("\t"))    // rows    records.forEach(r => this.log(                    r.keys.map(k => r.get(k)).join("\t")))
```

```
    this.log(`Returned ${records.length} row(s) in              ${result.summary.resultAvailableAfter.toNumber() +                result.summary.resultConsumedAfter.toNumber()} ms.`)  } else {    this.log('No Results.')  }}
```

If we run our test again, it “just works.” Cool!

```
./bin/run -p test "MATCH (n:Person) RETURN n.name limit 2"
```

```
n.nameKeanu ReevesCarrie-Anne MossReturned 2 row(s) in 3 ms.
```

Now we can make it pretty with `[ascii-table](https://github.com/sorensen/ascii-table)`

```
yarn add ascii-table
```

As ASCII-table doesn’t come with TypeScript definition, the compiler would error — that’s why we have to declare the module in a separate file `src/ambient.d.ts`:

```
declare module 'ascii-table';
```

Again, add the imports. This time we add a non-required flag `-t` that switches on table mode.

```
import * as AsciiTable from 'ascii-table'
```

Then we construct and output the `AsciiTable` instance instead of plain text when that flag is set.

```
static flags = {  // ...  table: flags.boolean({ char: 't', description: 'Table Format' })}
```

```
async run() {  const { args, flags } = this.parse(Boltsh)
```

```
  const driver = neo4j.v1.driver(flags.address,                   neo4j.v1.auth.basic(flags.user, flags.password))  const session = driver.session()  const result = await session.run(args.query)  session.close()  driver.close()  const records = result.records;
```

```
  if (records.length > 0) {    // extract data to be rendered    const data = { heading: records[0].keys,           rows: records.map(r => r.keys.map(k => r.get(k))) }
```

```
    if (flags.table) {      const table = AsciiTable.factory(data)      this.log(table.toString())    } else {      this.log(data.heading.join("\t"))      data.rows.forEach(r => this.log(r.join("\t")))    }
```

```
    this.log(`Returned ${records.length} row(s) in              ${result.summary.resultAvailableAfter.toNumber() +                  result.summary.resultConsumedAfter.toNumber()} ms.`)  } else {    this.log('No Results.')  }}
```

So let’s give this a try and see what our table looks like:

```
./bin/run -p test -t "MATCH (n:Person) RETURN n.name limit 10"
```

```
.--------------------.|       n.name       ||--------------------|| Keanu Reeves       || Carrie-Anne Moss   || Laurence Fishburne || Hugo Weaving       || Lilly Wachowski    || Lana Wachowski     || Joel Silver        || Emil Eifrem        || Charlize Theron    || Al Pacino          |'--------------------'Returned 10 row(s) in 25 ms.
```

Also, a more complex query looks good (except, it’s too wide for Medium, so screenshot). This renders people’s name, birth-year, and three of the movies they are related to.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sR0hkTOmoblU7jRx1Tedvg.jpeg)

What’s nice about OCLIF is that it comes with batteries included. For example, we can run `boltsh --help` to get a proper help page:

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

In the article mentioned at the beginning, Jeff shows how to build a multi-command CLI. The code is basically the same as ours, the only difference being that you have multiple Commands.

Check out the OCLIF [documentation](https://oclif.io/docs) and [examples](https://github.com/oclif?utf8=%E2%9C%93&q=example&type=&language=).

The framework has a plugin infrastructure, and there are already [a few plugins](https://github.com/oclif?utf8=%E2%9C%93&q=plugin&type=&language=), like self-update. I hope we’ll see more.

I think OCLIF is really nicely done by the folks at Heroku, thanks to [Jeff Dickey](https://www.freecodecamp.org/news/writing-a-command-line-database-client-in-10-minutes-aa608536ae4b/undefined).

Cool, mission accomplished, now all that remains is to push to [GitHub](https://github.com/jexp/boltsh) and [publish to npm](https://www.npmjs.com/package/boltsh).

![Image](https://cdn-media-1.freecodecamp.org/images/1*i-Jkaoqfh-INzSkxOUrU7A.jpeg)

So why don’t you give it a try and built a CLI of your own?

Happy Hacking!

