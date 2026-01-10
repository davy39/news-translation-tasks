---
title: How to get valid SSL certificates for local development
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
seo_title: null
seo_desc: 'By Alex Nadalin

  A few weeks ago I bumped into mkcert, a tool written by Filippo. He is the same
  guy behind the popular heartbleed test tool.

  The tool in question answers one simple need:


  By creating a local root CA file that gets installed in your s...'
---

By Alex Nadalin

A few weeks ago I bumped into [mkcert](https://github.com/FiloSottile/mkcert), a tool written by [Filippo](https://github.com/FiloSottile). He is the same guy behind the popular [heartbleed test tool](https://filippo.io/Heartbleed/).

The tool in question answers one simple need:

![Image](https://cdn-media-1.freecodecamp.org/images/a8JOFa6GmZeaIcFSW4JfMoYzng0RzdPqqGUo)

By creating a local root CA file that gets installed in your system, it makes all certificates issued by `mkcert` trusted.

![Image](https://cdn-media-1.freecodecamp.org/images/ctZ7Wp94F3ICQ2g5C-1QUjWj9S9NRzLpUWuH)

After downloading the latest release from GitHub, you can simply “install” it by running `mkcert -install`. Once that is done, you can create your first, trusted (by your own system) certificate:

```bash
$ mkcert somedomain.local

Using the local CA at "/home/alex/.local/share/mkcert" ✨

Created a new certificate valid for the following names ?
 - "somedomain.local"
 
The certificate is at "./somedomain.local.pem" and the key at "./somedomain.local-key.pem" ✅
```

For example, here’s how it would look like if you had to boot a Node server with SSL support:

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

Pretty neat, eh?

What `mkcert` does is to simply add another CA file in your system.(I guess under `/etc/ssl/certs/ca-certificates.crt`, but I’m not entirely sure). Browsers consider these certificates trusted — a nice workaround to trick any HTTP client.

That’s it for today! Adios!

_Originally published at [odino.org](https://odino.org/valid-ssl-certificates-for-local-development/) (_1st September 2018_)._  
_You can follow me on [Twitter](https://twitter.com/_odino_) — rants are welcome!_ ?

