---
title: Comment Pretty Good Privacy fonctionne et comment vous pouvez l'utiliser pour
  une communication sécurisée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-08T15:51:16.000Z'
originalURL: https://freecodecamp.org/news/how-does-pretty-good-privacy-work-3f5f75ecea97
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LpV5okf8ByND-ClSQZ7-aA.png
tags:
- name: privacy
  slug: privacy
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment Pretty Good Privacy fonctionne et comment vous pouvez l'utiliser
  pour une communication sécurisée
seo_desc: 'By Radu Raicea

  Sending sensitive information through the internet is always nerve-racking. What
  if somebody else sees the bank information I’m sending? Or even those dank memes
  that should not be spoken of?

  Fortunately, there’s a pretty good solution...'
---

Par Radu Raicea

Envoyer des informations sensibles via Internet est toujours stressant. Et si quelqu'un d'autre voyait les informations bancaires que j'envoie ? Ou même ces memes compromettants dont on ne devrait pas parler ?

Heureusement, il existe une solution assez efficace à ce problème : **Pretty Good Privacy (PGP)**.

Un ingénieur logiciel nommé [Phil Zimmermann](https://en.wikipedia.org/wiki/Phil_Zimmermann) a créé PGP en 1991. Il était un militant anti-nucléaire et voulait un moyen de transférer des informations de manière sécurisée sur Internet.

Zimmermann a eu des ennuis avec le gouvernement américain en 1993 parce que PGP a traversé les eaux internationales et a atteint un grand nombre de pays à travers le globe, violant ainsi les restrictions américaines à l'exportation de logiciels cryptographiques.

Aujourd'hui, PGP est "détenu" par [Symantec](https://en.wikipedia.org/wiki/Symantec), mais **OpenPGP**, une norme de chiffrement de courrier électronique, est implémentée par [plusieurs logiciels](http://openpgp.org/software/).

Vous pourriez également entendre parler de [**GPG**](https://gnupg.org). Il s'agit d'un autre outil logiciel qui implémente la norme OpenPGP.

### Comment fonctionne réellement PGP ?

PGP est très facile à comprendre, en surface. Imaginez que vous souhaitez envoyer les informations de votre carte de crédit à un ami et que vous les écrivez sur un morceau de papier. Vous mettez ensuite le papier dans une boîte et l'envoyez par la poste.

Un voleur peut facilement voler la boîte et regarder le papier qui contient les informations de votre carte de crédit. Que pourriez-vous faire à la place ?

Vous décidez de mettre un cadenas sur la boîte, mais vous réalisez que vous devez envoyer la clé avec la boîte. Ce n'est pas bon.

Et si vous rencontriez votre ami en personne pour partager la clé à l'avance ? Cela pourrait fonctionner, non ? Cela pourrait, mais alors vous avez tous les deux une clé qui permet de déverrouiller la boîte. Vous, en tant qu'expéditeur, n'aurez plus jamais besoin d'ouvrir la boîte après l'avoir fermée. En gardant une copie d'une clé qui peut déverrouiller la boîte, vous créez une vulnérabilité.

Enfin, vous avez trouvé la solution idéale : vous aurez deux clés. La première clé ne pourra que verrouiller la boîte. La deuxième clé ne pourra que l'ouvrir. Ainsi, seule la personne qui doit obtenir le contenu de la boîte a la clé qui lui permet de la déverrouiller.

C'est ainsi que fonctionne PGP. Vous avez une **clé publique** (pour verrouiller/chiffrer le message) et une **clé privée** (pour déverrouiller/déchiffrer le message). Vous enverriez la clé publique à tous vos amis afin qu'ils puissent chiffrer des messages sensibles qu'ils veulent vous envoyer. Une fois que vous recevez un message chiffré, vous utilisez votre clé privée pour le déchiffrer.

![Image](https://cdn-media-1.freecodecamp.org/images/PJQnKUtmLBNrqukE5njpoe5BodFDw9CLkjNP)
_Crédit image : [OpenPGP](https://www.goanywhere.com/managed-file-transfer/encryption/open-pgp" rel="noopener" target="_blank" title=")_

### Un bref exemple

Il existe de nombreux [outils logiciels](http://openpgp.org/software/) qui implémentent la norme OpenPGP. Ils ont tous des méthodes différentes pour configurer le chiffrement PGP. Un outil particulier qui fonctionne très bien est _Apple Mail_.

Si vous utilisez un ordinateur Mac, vous pouvez télécharger [GPGTools](https://gpgtools.org). Cette application générera et gérera vos clés publiques et privées. Elle s'intègre également automatiquement avec Apple Mail.

Une fois les clés générées, vous verrez une icône de _cadenas_ dans la ligne d'objet, lors de la composition d'un nouveau message dans Apple Mail. Cela signifie que le message sera chiffré avec la clé publique que vous avez générée.

![Image](https://cdn-media-1.freecodecamp.org/images/a-OLDy3k9r4tQHBcrkE0Y3h6z4cMyh3sFc0v)
_Composer un e-mail chiffré PGP avec Apple Mail_

Après avoir envoyé l'e-mail à quelqu'un, il ressemblera à ceci. Ils ne pourront pas voir le contenu de l'e-mail jusqu'à ce qu'ils le déchiffrent en utilisant la clé privée.

Notez que **le chiffrement PGP ne chiffre pas la ligne d'objet d'un e-mail**. Ne mettez jamais d'informations sensibles dans la ligne d'objet.

![Image](https://cdn-media-1.freecodecamp.org/images/4is77S-O5Wdl1-ECq0H4acxkb-UTleTwsjpp)
_Recevoir un e-mail chiffré PGP_

Si vous utilisez un logiciel qui déchiffre automatiquement le message en utilisant votre clé privée, comme Apple Mail, cela ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/pWv57ExdqsNs-pEaGKbyyH3pBg6MiyO30HIF)
_E-mail PGP déchiffré_

### En résumé...

* **Pretty Good Privacy** (PGP) vous permet d'envoyer des fichiers et des messages de manière sécurisée sur Internet
* PGP génère une **clé publique** (pour chiffrer les messages) et une **clé privée** (pour déchiffrer les messages)
* [OpenPGP](http://openpgp.org) est une norme de chiffrement de courrier électronique
* [**GPG**](https://gnupg.org) est une implémentation open-source d'OpenPGP
* Vous pouvez trouver une liste de logiciels ayant la capacité PGP [**ici**](http://openpgp.org/software/)

### Références

* [http://philzimmermann.com/EN/background/index.html](http://philzimmermann.com/EN/background/index.html)
* [https://gnupg.org/index.html](https://gnupg.org/index.html)
* [https://gpgtools.org](https://gpgtools.org)
* [http://openpgp.org](http://openpgp.org)
* [Diagramme du flux de travail PGP](https://www.goanywhere.com/managed-file-transfer/encryption/open-pgp)

Pour plus de mises à jour, suivez-moi sur [Twitter](https://twitter.com/radu_raicea).