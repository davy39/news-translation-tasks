---
title: Comment intégrer un script shell Python/Ruby/PHP avec Node.js en utilisant
  child_process.spawn
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-a-python-ruby-php-shell-script-with-node-js-using-child-process-spawn-e26ca3268a11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mtP3Ak9ndB1jJo0mauPu5w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment intégrer un script shell Python/Ruby/PHP avec Node.js en utilisant
  child_process.spawn
seo_desc: 'By Hugo Di Francesco

  There are occasions when running a Python/Ruby/PHP shell script from Node.js is
  necessary. This post looks at best practices around leveraging child_process.spawn
  to encapsulate this call in Node.js/JavaScript.

  The goal here is t...'
---

Par Hugo Di Francesco

Il arrive que l'exécution d'un script shell Python/Ruby/PHP depuis Node.js soit nécessaire. Cet article examine les meilleures pratiques pour utiliser child_process.spawn afin d'encapsuler cet appel dans Node.js/JavaScript.

L'objectif ici est d'avoir une couche d'interopérabilité entre Node.js et un shell externe. C'est une solution rapide si une autre partie de votre système n'est pas développée en JavaScript.

Nous utiliserons `spawn` plutôt que `exec` car nous parlons de passer des données et potentiellement de grandes quantités. Pour comprendre la différence entre `child_process.spawn` et `child_process.exec`, voir « [Difference between spawn and exec of Node.js child_process](https://www.hacksparrow.com/difference-between-spawn-and-exec-of-node-js-child_process.html) ».

En bref, utilisez `exec` pour de petites quantités de données (moins de 200k) en utilisant une interface Buffer et `spawn` pour des quantités plus importantes en utilisant une interface stream.

`spawn` a une syntaxe plus verbeuse pour certains des cas d'utilisation que nous allons examiner. Il est plus adapté pour l'intégration avec Ruby/Python/PHP puisque nous pourrions obtenir plus de données que quelques lignes de texte.

Exemples complets [github.com/HugoDF/node-run-python](https://github.com/HugoDF/node-run-python).

Les exemples suivants contiennent 2 sections :

* La partie qui exécute réellement la commande shell, généralement une fonction appelée `run`, et
* une IIFE (« immediately invoked function expression ») qui l'appelle réellement, `(async () => { await run() }`)(). Cette IIFE est un bon modèle permis par async/await (voir [Async JS : histoire, modèles et pièges](https://codewithhugo.com/async-js/#async-await)), mais elle est juste là à des fins d'illustration puisqu'elle représente l'appel à l'appel `spawn` encapsulé depuis une autre partie de votre application.

### Appeler une commande shell et la logger

Utiliser `spawn` est excessif dans cette situation puisque echo ne va retourner que ce qui lui est passé.

L'exemple est assez explicite et montre comment utiliser `child_process.spawn` pour « shell out » et lire ces données en retour.

`spawn` prend l'exécutable à appeler comme premier paramètre et optionnellement un tableau d'options/paramètres pour l'exécutable comme second paramètre.

```js
const { spawn } = require('child_process');
function run() {
  const process = spawn('echo', ['foo']);
  process.stdout.on(
    'data',
    (data) => console.log(data.toString())
  );
}
(() => {
  try {
    run()
    // process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

### Appeler Python pour sa version

Nous allons passer rapidement à la manière dont nous ferions quelque chose de similaire à ce qui précède avec Python. Notez à nouveau comment `--version` est passé à l'intérieur d'un tableau.

Nous créons également un logger pour différencier entre stdout et stderr et les lier. Puisque spawn retourne une instance qui a des émetteurs d'événements `stdout` et `stderr`, nous pouvons lier notre fonction `logOutput` à l'événement `'data'` en utilisant `.on('data', () => { /* notre fonction de rappel */ })`.

Un autre détail intéressant est que `python` `--version` sortie la version vers `stderr`. Les inconsistances autour de l'utilisation des codes de sortie, stderr et stdout sur succès/erreur par les exécutables *NIX sont un trait que nous devons garder à l'esprit lors de l'intégration de Python/Ruby/autres avec Node.js.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data.toString()}`)
function run() {
  const process = spawn('python', ['--version']);
process.stdout.on(
    'data',
    logOutput('stdout')
  );
process.stderr.on(
    'data',
    logOutput('stderr')
  );
}
(() => {
  try {
    run()
    process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Sortie :

```
$ node run.js
```

```
[stderr] Python 2.7.13
```

### Appeler un script Python depuis Node

Nous allons maintenant exécuter un script Python complet (bien que cela pourrait tout aussi bien être Ruby, PHP, shell, etc.) depuis Node.js.

Voici `script.py`, il se contente de logger `argv` (le « vecteur d'arguments », c'est-à-dire `['chemin/vers/exécutable', /* arguments de la ligne de commande */]`)

```py
import sys
print(sys.argv)
```

Comme dans l'exemple précédent, nous allons simplement appeler spawn avec `python` avec le chemin vers le script Python (`./script.py`) dans le second paramètre.

Voici un autre piège de l'intégration de scripts de cette manière. Dans cet exemple, le chemin vers le script est basé sur le répertoire de travail à partir duquel `node` est appelé.

Il existe bien sûr une solution de contournement, en utilisant le module `path` et `__dirname`, qui pourrait par exemple résoudre un `other-script.py` co-localisé avec le fichier JavaScript/module Node appelant `spawn` en utilisant : `require('path').resolve(__dirname, './other-script.py')`.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data.toString()}`)
function run() {
  const process = spawn('python', ['./script.py']);
process.stdout.on(
    'data',
    logOutput('stdout')
  );
process.stderr.on(
    'data',
    logOutput('stderr')
  );
}
(() => {
  try {
    run()
    // process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Sortie :

```bash
node run.js
\[stdout\] ['./script.py']
```

### Passer des arguments à un script Python depuis Node.js en utilisant child_process.spawn

L'étape suivante de l'intégration est de pouvoir passer des données du code Node/JavaScript au script Python.

Pour ce faire, nous allons simplement passer plus d'arguments shell en utilisant le tableau d'arguments (le second paramètre de `spawn`).

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data.toString()}`)
function run() {
  const process = spawn('python', ['./script.py', 'my', 'args']);
  process.stdout.on(
    'data',
    logOutput('stdout')
  );
  process.stderr.on(
    'data',
    logOutput('stderr')
  );
}
(() => {
  try {
    run()
    // process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Notre `script.py` va également simplement logger `argv` à l'exception du premier élément (qui est le chemin vers le script).

```py
import sys
print(sys.argv)[1:]
```

Voici la sortie :

```bash
node run.js
\[stdout\] ['my', 'args']
```

### Lire la sortie de child_process.spawn depuis Node.js

Il est utile de pouvoir passer des données au script Python. Nous ne sommes toujours pas en mesure d'obtenir les données du script Python dans un format que nous pouvons utiliser dans notre application Node.js/JavaScript.

La solution à cela est d'encapsuler toute la fonction d'appel `spawn` dans une Promesse. Cela nous permet de décider quand nous voulons `resolve` ou `reject`.

Pour suivre le flux de sortie du script Python, nous mettons en mémoire tampon la sortie manuellement en utilisant des tableaux (un pour `stdout` et un autre pour `stderr`).

Nous ajoutons également un écouteur pour `'exit'` en utilisant `spawn().on('exit', (code, signal) => { /* probablement appeler resolve() */ })`. C'est ici que nous allons tendre à `resolve/reject` la valeur de la Promesse à partir du script Python/Ruby/autre.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data}`)
function run() {
  return new Promise((resolve, reject) => {
    const process = spawn('python', ['./script.py', 'my', 'args']);
    const out = []
    process.stdout.on(
      'data',
      (data) => {
        out.push(data.toString());
        logOutput('stdout')(data);
      }
    );
    const err = []
    process.stderr.on(
      'data',
      (data) => {
        err.push(data.toString());
        logOutput('stderr')(data);
      }
    );
    process.on('exit', (code, signal) => {
      logOutput('exit')(`${code} (${signal})`)
      resolve(out);
    });
  });
}
(async () => {
  try {
    const output = await run()
    logOutput('main')(output)
    process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Sortie :

```bash
node run.js
\[stdout\] ['my', 'args']
\[main\] ['my', 'args']
```

### Gérer les erreurs de child_process.spawn

Ensuite, nous devons gérer les erreurs du script Python/Ruby/shell au niveau Node.js/JavaScript.

La principale manière dont un exécutable *NIX signale qu'il a rencontré une erreur est en utilisant un code de sortie `1`. C'est pourquoi le gestionnaire `.on('exit'` effectue maintenant une vérification contre `code === 0` avant de décider de résoudre ou de rejeter avec la valeur.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data}`)
function run() {
  return new Promise((resolve, reject) => {
    const process = spawn('python', ['./script.py', 'my', 'args']);
const out = []
    process.stdout.on(
      'data',
      (data) => {
        out.push(data.toString());
        logOutput('stdout')(data);
      }
    );
const err = []
    process.stderr.on(
      'data',
      (data) => {
        err.push(data.toString());
        logOutput('stderr')(data);
      }
    );
process.on('exit', (code, signal) => {
      logOutput('exit')(`${code} (${signal})`)
      if (code === 0) {
        resolve(out);
      } else {
        reject(new Error(err.join('\n')))
      }
    });
  });
}
(async () => {
  try {
    const output = await run()
    logOutput('main')(output)
    process.exit(0)
  } catch (e) {
    console.error('Error during script execution ', e.stack);
    process.exit(1);
  }
})();
```

Sortie :

```bash
node run.js
[stderr] Traceback (most recent call last):
    File "./script.py", line 3, in <module>
    print(sy.argv)[1:]
NameError: name 'sy' is not defined
Error during script execution Error: Traceback (most recent call last):
    File "./script.py", line 3, in <module>
    print(sy.argv)[1:]
NameError: name 'sy' is not defined
at ChildProcess.process.on (/app/run.js:33:16)
    at ChildProcess.emit (events.js:182:13)
    at Process.ChildProcess._handle.onexit (internal/child_process.js:240:12)
```

### Passer des données structurées de Python/Ruby à Node.js/JavaScript

L'étape finale pour une intégration complète entre les scripts Ruby/Python/PHP/shell et notre couche d'application Node.js/JavaScript est de pouvoir passer des données structurées du script vers Node.js/JavaScript.

Le format de données structurées le plus simple qui tend à être disponible à la fois en Python/Ruby/PHP et en Node.js/JavaScript est JSON.

Dans le script Python, nous imprimons la sortie `json.dumps()` d'un dictionnaire, voir `script.py` :

```py
import sys
import json
send_message_back = {
  'arguments': sys.argv[1:],
  'message': """Hello,
This is my message.
To the world"""
}
print(json.dumps(send_message_back))
```

Dans Node, nous ajoutons une logique d'analyse JSON (en utilisant `JSON.parse`) dans le gestionnaire `'exit'`.

Un piège à ce stade est si, par exemple, `JSON.parse()` échoue en raison d'un JSON mal formé, nous devons propager cette erreur. D'où le try/catch où la clause `catch` `reject` l'erreur potentielle : `try { resolve(JSON.parse(out[0])) } catch(e) { reject(e) }`.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (message) => console.log(`[${name}] ${message}`)
function run() {
  return new Promise((resolve, reject) => {
    const process = spawn('python', ['./script.py', 'my', 'args']);
    const out = []
    process.stdout.on(
      'data',
      (data) => {
        out.push(data.toString());
        logOutput('stdout')(data);
      }
    );
    const err = []
    process.stderr.on(
      'data',
      (data) => {
        err.push(data.toString());
        logOutput('stderr')(data);
      }
    );
   process.on('exit', (code, signal) => {
      logOutput('exit')(`${code} (${signal})`)
      if (code !== 0) {
        reject(new Error(err.join('\n')))
        return
      }
      try {
        resolve(JSON.parse(out[0]));
      } catch(e) {
        reject(e);
      }
    });
  });
}
(async () => {
  try {
    const output = await run()
    logOutput('main')(output.message)
    process.exit(0)
  } catch (e) {
    console.error('Error during script execution ', e.stack);
    process.exit(1);
  }
})();
```

Sortie :

```bash
node run.js
[stdout] {"message": "Hello,\nThis is my message.\n\nTo the world", "arguments": ["my", "args"]}
[main] Hello,
This is my message.
To the world
```

C'est tout ! Merci d'avoir lu :)

J'ai des places de mentorat ouvertes sur [https://mentorcruise.com/mentor/HugoDiFrancesco/](https://mentorcruise.com/mentor/HugoDiFrancesco/). Faites-le si vous voulez du mentorat Node.js/JavaScript/carrière ou n'hésitez pas à tweeter @hugo__df [@hugo__df](https://twitter.com/hugo__df)

Et lisez plus de mes articles sur [codewithhugo.com](https://www.codewithhugo.com)