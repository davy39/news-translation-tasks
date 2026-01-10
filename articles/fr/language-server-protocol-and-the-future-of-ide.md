---
title: Comment le protocole Language Server influence l'avenir des IDE
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-02T15:19:25.000Z'
originalURL: https://freecodecamp.org/news/language-server-protocol-and-the-future-of-ide
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/screely.png
tags:
- name: ide
  slug: ide
- name: programming languages
  slug: programming-languages
- name: Visual Studio Code
  slug: vscode
seo_title: Comment le protocole Language Server influence l'avenir des IDE
seo_desc: "By Mehul Mohan\nThe release of Visual Studio Code single-handedly impacted\
  \ the developer ecosystem in such a way that there's no going back now. It's open\
  \ source, free, and most importantly, a super powerful tool. \nBut with VSCode,\
  \ Microsoft gave life..."
---

Par Mehul Mohan

La sortie de Visual Studio Code a eu un impact tel sur l'écosystème des développeurs qu'il n'y a plus de retour en arrière possible. Il est open source, gratuit, et surtout, un outil extrêmement puissant. 

Mais avec VSCode, Microsoft a donné vie à une autre chose extrêmement importante en 2016, qui est moins connue. Elle s'appelle Language Server Protocol.

# Qu'est-ce que le protocole Language Server ?

Le protocole Language Server (LSP) est un protocole ou une manière de communiquer avec les serveurs de langage (comme HTTP ou FTP). 

Les serveurs de langage sont des programmes spéciaux qui s'exécutent sur des serveurs réguliers. Ils prennent l'état méta de l'éditeur dans lequel vous codez (par exemple, où se trouve votre curseur dans l'éditeur, quel token vous survolez actuellement) et retournent un ensemble d'actions/instructions – quel token doit apparaître ensuite, ce qui doit se produire lorsque vous CMD/Ctrl-cliquez sur ce token, et ainsi de suite.

Cette communication se fait en utilisant un ensemble de règles définies par le protocole. Le protocole Language Server peut être considéré comme une version allégée de HTTP et communique uniquement via JSON-RPC.

# Pourquoi le LSP est-il nécessaire ?

Vous voyez ces suggestions automatiques et messages d'erreur qui apparaissent constamment dans VSCode ? Et comment, simplement en ajoutant une extension simple depuis le marketplace de VSCode, vous obtenez toute la puissance d'IntelliSense pour un langage complètement différent comme C, Python, Java, et ainsi de suite ? Cela vient du LSP.

Le support pour l'autocomplétion et IntelliSense pour HTML/CSS/JavaScript est intégré nativement dans VSCode (comme PyCharm est intégré avec le support pour Python). Cependant, le même support pour d'autres langages peut être implémenté en utilisant le protocole Language Server pour ces langages.

![LSP dans l'éditeur Monaco](https://dev-to-uploads.s3.amazonaws.com/i/pn5c0n3zus769e5fadbk.gif)

# Qu'est-ce que JSON-RPC ?

JSON-RPC signifie JSON Remote Procedure Call. C'est une architecture (similaire à la manière dont REST est une architecture) mais avec l'unité fondamentale étant un appel de procédure plutôt qu'un point de terminaison d'API dans le cas de REST.

Voici une charge utile simple pour JSON-RPC :

```sh
// Requête
curl -X POST —data '{
  "jsonrpc": "2.0",
  "method": "runThisFunction",
  "params": [ "some-param", 2 ],
  "id": 1
}'
// Réponse
{
  "jsonrpc": "2.0",
  "result": "codedamn",
  "id": 1
}

```

Dans cet exemple, nous envoyons une charge utile encodée en JSON suivant la spécification RPC. Si le serveur est configuré pour gérer correctement JSON-RPC, il exécutera la méthode `runThisFunction` avec les paramètres passés et retournera le résultat sous la forme indiquée.

# LSP + JSON-RPC

LSP utilise JSON-RPC pour communiquer avec le serveur distant. Il suit ce format :

```sh
Content-Length: <bytes of JSON>\r\n\r\n<json-payload>

```

Pour écrire un exemple, cela ressemblerait à ceci :

```sh
Content-Length: 78

{"jsonrpc":"2.0","method":"runThisFunction","params":["some-param",2],"id":1}

```

Le LSP vous oblige à passer l'en-tête `Content-Length` suivi de 2 jetons `CRLF` `\r\n`. Lorsque les serveurs de langage en cours d'exécution comme `ccls` reçoivent cela, ils répondent avec un message approprié :

![serveur ccls](https://dev-to-uploads.s3.amazonaws.com/i/7zxtfv0a4c15mqxdl2mr.png)

Bien sûr, dans l'exemple ci-dessus, vous pouvez voir que `ccls` indique qu'il n'y a pas de méthode appelée `runThisFunction`. Mais vous pouvez voir que le serveur distant répond également avec un en-tête `Content-Length` avec une spécification JSON-RPC.

# Pourquoi tout cela est-il important ?

Avec l'introduction d'un protocole formel LSP, Microsoft a réduit le célèbre problème `M x N` à un problème `M + N`.

M = Différents langages (C, C++, PHP, Python, Node, Swift, Go, etc.)  
N = Différents éditeurs (VSCode, Eclipse, Notepad++, Sublime Text, etc.)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-02-at-8.30.21-PM.png)

Auparavant, pour que M éditeurs supportent N langages, vous aviez besoin de M*N solutions. C'est-à-dire que chaque éditeur devait implémenter un support natif pour chaque langage différemment.

Avec l'introduction du LSP, l'éditeur n'avait besoin d'implémenter que le support pour le protocole Language Server. Une fois cela fait, toute personne qui crée un serveur de langage (en suivant les normes LSP) peut être intégrée de manière transparente avec l'éditeur, sans que l'éditeur ait jamais à "savoir" intelligemment quel langage il utilise !

# L'avenir des IDE

À mesure que de plus en plus de langages sortent avec leurs serveurs de langage, les gens auront plus de liberté pour choisir l'éditeur qu'ils préfèrent. 

Vous n'aurez plus à vous limiter à XCode pour le développement Swift, ou à PyCharm pour Python. Non seulement cela, mais les LSP peuvent également être implémentés directement en JavaScript pour supporter IntelliSense dans le navigateur comme je le fais sur [codedamn](https://codedamn.com), une plateforme pour les développeurs pour apprendre et grandir ! C'est une époque excitante pour être en vie !

Paix,  
Mehul