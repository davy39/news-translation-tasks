---
title: Comment obtenir des certificats SSL valides pour le développement local
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-25T14:51:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-valid-ssl-certificates-for-local-development-ca228240fad2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1iaTVIFNnW0CVKg4.png
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: SSL
  slug: ssl
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment obtenir des certificats SSL valides pour le développement local
seo_desc: 'By Alex Nadalin

  A few weeks ago I bumped into mkcert, a tool written by Filippo. He is the same
  guy behind the popular heartbleed test tool.

  The tool in question answers one simple need:


  By creating a local root CA file that gets installed in your s...'
---

Par Alex Nadalin

Il y a quelques semaines, je suis tombé sur [mkcert](https://github.com/FiloSottile/mkcert), un outil écrit par [Filippo](https://github.com/FiloSottile). C'est le même gars derrière le populaire [outil de test heartbleed](https://filippo.io/Heartbleed/).

L'outil en question répond à un besoin simple :

![Image](https://cdn-media-1.freecodecamp.org/images/a8JOFa6GmZeaIcFSW4JfMoYzng0RzdPqqGUo)

En créant un fichier de certificat racine local qui est installé dans votre système, il rend tous les certificats émis par `mkcert` dignes de confiance.

![Image](https://cdn-media-1.freecodecamp.org/images/ctZ7Wp94F3ICQ2g5C-1QUjWj9S9NRzLpUWuH)

Après avoir téléchargé la dernière version depuis GitHub, vous pouvez simplement l'installer en exécutant `mkcert -install`. Une fois cela fait, vous pouvez créer votre premier certificat, digne de confiance (par votre propre système) :

```bash
$ mkcert somedomain.local

Using the local CA at "/home/alex/.local/share/mkcert" ✨

Created a new certificate valid for the following names ?
 - "somedomain.local"
 
The certificate is at "./somedomain.local.pem" and the key at "./somedomain.local-key.pem" ✅
```

Par exemple, voici à quoi cela ressemblerait si vous deviez démarrer un serveur Node avec support SSL :

```js
const fs = require('fs')

const options = {
  key: fs.readFileSync(__dirname + '/somedomain.local-key.pem'),
  cert: fs.readFileSync(__dirname + '/somedomain.local.pem')
};

require('https').createServer(options, (req, res) => {
  res.writeHead(200)
  res.end(`Got SSL?`)
}).listen(443)
```

Plutôt sympa, hein ?

Ce que fait `mkcert`, c'est simplement ajouter un autre fichier CA dans votre système. (Je suppose sous `/etc/ssl/certs/ca-certificates.crt`, mais je ne suis pas entièrement sûr). Les navigateurs considèrent ces certificats comme dignes de confiance — une belle astuce pour tromper n'importe quel client HTTP.

C'est tout pour aujourd'hui ! Adios !

_Publié à l'origine sur [odino.org](https://odino.org/valid-ssl-certificates-for-local-development/) (1er septembre 2018)._
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) — les rants sont les bienvenus !_ ?