---
title: Que signifient les commentaires cryptiques sur Github ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-24T15:47:38.000Z'
originalURL: https://freecodecamp.org/news/what-do-cryptic-github-comments-mean-9c1912bcc0a4
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb905740569d1a4caef63.jpg
tags:
- name: GitHub
  slug: github
- name: learning
  slug: learning
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Que signifient les commentaires cryptiques sur Github ?
seo_desc: 'By Alex Beregszaszi

  Are you new to Github and/or contributing to open source projects? Have you seen
  short messages like LGTM, ACK, NACK, etc. and wondered what they mean?

  Here you go:


  LGTM — looks good to me

  ACK — acknowledgement, i.e. agreed/accep...'
---

Par Alex Beregszaszi

Êtes-vous nouveau sur Github et/ou contribuez-vous à des projets open source ? Avez-vous vu des messages courts comme LGTM, ACK, NACK, etc. et vous êtes-vous demandé ce qu'ils signifient ?

Voici la réponse :

* LGTM — _looks good to me_ (ça me semble bien)
* ACK — _acknowledgement_, c'est-à-dire changement accepté/validé
* NACK/NAK — _negative acknowledgement_, c'est-à-dire désaccord avec le changement et/ou le concept
* RFC — _request for comments_, c'est-à-dire je pense que c'est une bonne idée, discutons-en
* WIP — _work in progress_, ne pas fusionner pour l'instant
* AFAIK/AFAICT — _as far as I know / can tell_ (autant que je sache / puisse dire)
* IIRC — _if I recall correctly_ (si je me souviens bien)
* IANAL — « _I am not a lawyer_ » (je ne suis pas avocat), _mais je sens des problèmes de licence_

De nombreux projets dans l'espace crypto utilisent également les termes suivants (_popularisés_ par [Bitcoin](https://github.com/bitcoin/bitcoin/issues/6100) et son [_jargon de hacker_](https://twitter.com/jgarzik/status/601815506291531776)) :

* Concept ACK — accord avec le concept, mais les changements n'ont pas été examinés
* utACK (aka. Untested ACK) — accord avec les changements et examen effectué, mais pas de test
* Tested ACK — accord avec les changements, examen et test effectués

Ces réponses font généralement partie du processus de révision de code et vous les trouverez dans les _issues_ ou les _pull requests_ sur Github.

_Mention honorable : **+1**_ comme forme courte de ACK (et dans de nombreux cas, Concept ACK). Après la [fameuse lettre « Dear Github »](https://github.com/dear-github/dear-github), la plateforme a introduit des [réactions appropriées](https://github.com/blog/2119-add-reactions-to-pull-requests-issues-and-comments) pour désencombrer les commentaires. Non, il ne s'agit pas de faire de Github votre prochain Facebook :)

Vous verrez également les ACK inclus dans les messages de commit, comme le fait le noyau Linux depuis l'utilisation de Git :

```
Add get_random_long().
Signed-off-by: Daniel Cashman <dcashman@android.com>
Acked-by: Kees Cook <keescook@chromium.org>
Cc: "Theodore Ts'o" <tytso@mit.edu>
Cc: Arnd Bergmann <arnd@arndb.de>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Cc: Catalin Marinas <catalin.marinas@arm.com>
Cc: Will Deacon <will.deacon@arm.com>
Cc: Ralf Baechle <ralf@linux-mips.org>
Cc: Benjamin Herrenschmidt <benh@kernel.crashing.org>
Cc: Paul Mackerras <paulus@samba.org>
Cc: Michael Ellerman <mpe@ellerman.id.au>
Cc: David S. Miller <davem@davemloft.net>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: H. Peter Anvin <hpa@zytor.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Nick Kralevich <nnk@google.com>
Cc: Jeff Vander Stoep <jeffv@google.com>
Cc: Mark Salyzyn <salyzyn@android.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
```

Consultez le guide « [How to Get Your Change Into the Linux Kernel](https://www.kernel.org/doc/Documentation/SubmittingPatches) » pour une explication approfondie.

Des réponses courtes similaires sont largement utilisées en ingénierie logicielle et dans la communauté open source, car elles rendent la communication plus efficace.

Vous avez sûrement vu les termes suivants dans le code source — TODO, FIXME, XXX et NOTE — et vous êtes peut-être demandé ce que signifie _XXX_ ?

Intéressé à voir beaucoup plus d'acronymes avec des explications et peut-être un peu d'histoire ? Consultez [The Jargon File](http://www.catb.org/jargon/html/index.html). C'est la source définitive depuis 1975.

**Bonus trivia** : d'où viennent ACK/NACK ?

Je dirais que cela vient des protocoles de réseau/interface, peut-être que la popularité de TCP a causé une utilisation généralisée.

> _SYN, SYN/ACK, ACK, FIN, ACK, FIN, ACK._