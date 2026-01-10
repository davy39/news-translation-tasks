---
title: Pourquoi la racine d'un domaine ne peut pas être un CNAME — et autres détails
  sur le DNS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-13T23:00:07.000Z'
originalURL: https://freecodecamp.org/news/why-cant-a-domain-s-root-be-a-cname-8cbab38e5f5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YNkO-BfTsVJYxslNrNn8LA.jpeg
tags:
- name: dns
  slug: dns
- name: internet
  slug: internet
- name: programing
  slug: programing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi la racine d'un domaine ne peut pas être un CNAME — et autres détails
  sur le DNS
seo_desc: 'By Dominic Fraser

  This post will use the above question to explore DNS, dig, A records, CNAME records,
  and ALIAS/ANAME records from a beginner’s perspective. So let’s get started.

  First, some definitions


  Domain Name System (DNS): the overall system ...'
---

Par Dominic Fraser

Cet article utilisera la question ci-dessus pour explorer le `DNS`, `dig`, les enregistrements `A`, les enregistrements `CNAME` et les enregistrements `ALIAS/ANAME` du point de vue d'un débutant. Alors commençons.

### D'abord, quelques définitions

* **Système de noms de domaine** (DNS) : le système global pour convertir un nom de domaine mémorable par l'homme (example.com) en une adresse IP (93.184.216.34). L'adresse IP est celle d'un serveur, généralement un serveur web, où sont stockés les fichiers nécessaires pour afficher une page web.
* **Serveur DNS** (également connu sous le nom de serveur de noms ou nameserver) : Utilise un logiciel DNS pour stocker des informations sur les adresses de domaine. Il existe plusieurs niveaux — ceux appartenant à chaque FAI, Root (13 au total dans le monde), Top Level Domain (TLD, par exemple '.com'), et les serveurs DNS de niveau domaine.
* **Nom de domaine** : le domaine (example) combiné avec le TLD (.com). Le terme 'domaine' est souvent utilisé de manière synonyme avec le nom de domaine, [bien qu'ils soient différents](https://www.domainsherpa.com/anatomy-of-a-domain-name-and-url/). Lorsque vous achetez un 'domaine' auprès d'un registrar ou d'un revendeur, vous achetez les droits sur un nom de domaine spécifique (example.com), et sur tous les sous-domaines que vous souhaitez créer (my-site.example.com, mail.example.com, etc).

### Flux de requête de haut niveau

Le flux de haut niveau de ce qui se passe lorsque vous tapez 'example.com' dans votre navigateur peut être simplifié pour supprimer les sauts vers le FAI, Root, et les serveurs DNS TLD comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/-Yu9MR65z19xx2TDl-6phT7soy3g3KNgjArX)
_Flux de requête DNS simplifié, plus de détails peuvent être vus dans un [flux plus détaillé](http://www.uxworld.com/?p=384" rel="noopener" target="_blank" title=")_

Un domaine a généralement deux serveurs de noms ou plus, contenant des enregistrements relatifs au nom de domaine (example.com).

De nombreux types d'enregistrements peuvent être stockés, dont la plupart peuvent avoir plusieurs entrées par type :

* `A` : Enregistrements d'adresse qui mappent le nom de domaine à une adresse IP
* `CNAME` : Enregistrement de nom canonique. Utilisé pour aliaser un nom de domaine (ou un nom de sous-domaine) à un autre. Nous examinerons cela plus en détail plus tard.
* `MX` : Enregistrements Mail eXchange qui indiquent aux agents de livraison de courrier où ils doivent livrer votre courrier
* `TXT` : Enregistrements de texte flexibles, pour stocker des chaînes de caractères pour une variété d'utilisations
* `SOA` : Enregistrement unique Start of Authority conservé au niveau supérieur du domaine. Contient des informations spécifiques requises sur le domaine, par exemple son serveur de noms principal
* `NS` : Les serveurs de noms associés au domaine

Lorsque votre appareil envoie une requête qui atteint un serveur de noms, le serveur recherche dans le nœud d'enregistrement du domaine un enregistrement `A`, et l'adresse IP stockée associée (example.com : 93.184.216.34). Cela est ensuite retourné à l'appareil, pour être utilisé pour envoyer une requête au bon serveur web afin de récupérer la page web ou la ressource demandée.

### Utilisation de 'dig'

`dig` (**domain information groper**) est un outil en ligne de commande pour interroger les serveurs DNS. Cette commande est généralement utilisée pour le dépannage, ou comme maintenant pour comprendre davantage sur la configuration d'un système.

`$ dig example.com` donne une longue réponse imprimée dans le terminal, [la sortie par défaut détaillée ici](https://www.madboa.com/geek/dig/#understanding-the-default-output), dont nous nous intéressons à la section `ANSWER SECTION`.

```
;; ANSWER SECTION:
example.com.       72703      IN     A       93.184.216.34
```

Et voilà, nous pouvons voir que `example.com` retourne un enregistrement `A` de `93.184.216.34`. Parfois, les domaines auront plus d'un enregistrement `A`, si plus d'un serveur web peut fournir les informations nécessaires.

Il y a plus ! Si nous essayons d'autres exemples, nous pouvons bientôt voir qu'un autre enregistrement courant apparaît : `CNAME`.

`$ dig www.skyscanner.net`:

```
;; ANSWER SECTION:
www.skyscanner.net. 169 IN CNAME www.skyscanner.net.edgekey.net.
www.skyscanner.net.edgekey.net. 5639 IN CNAME e11316.a.akamaiedge.net.
e11316.a.akamaiedge.net. 20 IN A 23.217.6.192
```

```
www.skyscanner.net.edgekey.net. 5639 IN CNAME e11316.a.akamaiedge.net.
```

```
e11316.a.akamaiedge.net. 20 IN A 23.217.6.192
```

L'utilisation du drapeau `+short` nous permet de voir clairement le chemin formé :

`$ dig [www.skyscanner.net](http://www.skyscanner.net) +short`

```
www.skyscanner.net.edgekey.net.
e11316.a.akamaiedge.net.
23.217.6.192
```

### CNAME

Un enregistrement `CNAME` permet d'utiliser un nom de domaine comme alias pour un autre domaine canonique (vrai).

Lorsque le serveur DNS retourne un enregistrement `CNAME`, il ne le retournera pas au client. Il recherchera plutôt le nom de domaine retourné, et retournera à son tour l'adresse IP de l'enregistrement `A`. Cette chaîne peut continuer sur plusieurs niveaux de `CNAME`, mais subit alors des pertes de performance mineures dues aux multiples recherches avant que la mise en cache ne prenne place.

Un exemple simple de cela pourrait être si vous avez un serveur où vous gardez toutes vos photos. Vous y accédez normalement via `photos.example.com`. Cependant, vous pourriez aussi vouloir permettre l'accès via `photographs.example.com`. Une façon de rendre cela possible est d'ajouter un enregistrement `CNAME` qui pointe `photographs` vers `photos`. Cela signifie que lorsque quelqu'un visite `photographs.example.com`, il obtiendra le même contenu que `photos.example.com`.

En utilisant la requête `$ dig photographs.example.com`, nous verrions :

```
photographs.example.com    IN   CNAME photos.example.com
photos.example.com         IN   A     xx.xxx.x.xxx
```

Il est important de noter que le `CNAME` est la partie à droite. Le côté gauche est le nom de l'alias, ou l'étiquette.

Une autre utilisation courante est pour le sous-domaine `www`. Ayant acheté `example.com`, vous souhaitez probablement que les utilisateurs qui tapent `www.example.com` voient le même contenu.

Il est important de noter ici que `example.com` peut être appelé le sommet, la racine, ou le domaine nu.

Une option serait de configurer un autre enregistrement `A`, pointant vers la même adresse IP que pour `example.com`. Cela est complètement valide, et c'est ce que fait le vrai `example.com`, mais cela ne s'adapte pas bien. Que se passe-t-il si vous devez mettre à jour l'adresse IP vers laquelle pointe `example.com` ? Vous devriez également la mettre à jour pour le sous-domaine `www`, et tout autre que vous pourriez utiliser.

Si un enregistrement `CNAME` était utilisé pour aliaser `www.example.com` pour pointer vers `example.com`, alors seul le domaine racine devrait être mis à jour, car tous les autres nœuds pointent vers lui.

### Limites des CNAME

Au moment où les normes DNS ont été écrites, certaines règles ont été établies pour régir leur utilisation. [RFC 1912](https://tools.ietf.org/html/rfc1912) et [RFC 2181](https://tools.ietf.org/html/rfc2181) stipulent que :

* Les enregistrements `SOA` et `NS` sont obligatoires pour être présents au niveau du domaine racine
* Les enregistrements `CNAME` ne peuvent exister que sous forme d'enregistrements uniques et ne peuvent pas être combinés avec d'autres enregistrements de ressources (les enregistrements DNSSEC `SIG`, `NXT`, et `KEY RR` exceptés)

Cela exclut l'utilisation d'un `CNAME` sur le domaine racine, car les deux règles se contrediraient.

Ce qui est important ici, c'est que cela constitue une limitation contractuelle, et non technique. Il est possible d'utiliser un `CNAME` à la racine, mais cela peut entraîner des erreurs inattendues, car cela enfreint le contrat de comportement attendu.

Un exemple de cela est [raconté par Cloudflare](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/), décrivant les problèmes qu'ils ont rencontrés avec les serveurs de messagerie Microsoft Exchange après avoir utilisé un `CNAME` sur leur domaine racine :

> Les domaines désignent généralement les serveurs qui gèrent leur courrier électronique via ce que l'on appelle un enregistrement MX. Le problème était que les serveurs Exchange ... pouvaient récupérer le CNAME au niveau de l'enregistrement racine et ne pas respecter correctement le CNAME défini au niveau de l'enregistrement MX. Vous ne pouvez pas vraiment blâmer Exchange. **Ils fonctionnaient selon les hypothèses énoncées par la spécification DNS.**

Ici, vous voyez l'inconvénient qui peut apparaître dans plusieurs logiciels de serveur ou bibliothèques. Parce qu'une norme est en place pour qu'un `CNAME` soit le **seul** enregistrement à un nœud, **aucun autre enregistrement n'est recherché.** Tous les autres enregistrements seront silencieusement ignorés, sans avertissement ni message d'erreur. Même si un enregistrement `MX` était défini pour recevoir des e-mails, le `MX` sera ignoré comme s'il n'existait pas parce que le `CNAME` est évalué en premier. Il en va de même s'il y avait un enregistrement `A` : le `CNAME` aurait la priorité et l'enregistrement `A` ne serait pas lu.

### L'internet moderne

Alors pourquoi est-ce un problème ? Pourquoi voudriez-vous jamais utiliser un `CNAME` pour votre domaine racine de toute façon ? Cela ne devrait-il pas être la fin du chemin lorsque l'on recherche l'adresse IP du serveur web hébergeant votre contenu ?

Dans le paysage de l'internet moderne, ce n'est plus le cas. Le monde est très différent de celui où les normes DNS ont été écrites.

Vous pouvez choisir d'utiliser un fournisseur de Plateforme en tant que Service (PaaS) comme [Heroku](https://www.heroku.com/) et stocker du contenu sur leurs serveurs web. Vous contrôlez le contenu, mais pas l'infrastructure, et le fournisseur PaaS effectue le travail lourd de la maintenance du réseau. Ils vous fournissent généralement une URL (`my-app.herokuapp.com`) qui est un sous-domaine de leur domaine racine, et vous pouvez voir les adresses IP des serveurs web sur lesquels votre contenu est hébergé. Mais celles-ci sont entièrement sous le contrôle du fournisseur PaaS, et changeront sans avertissement.

L'échelle et la fréquence des changements backend effectués par le fournisseur PaaS peuvent rendre difficile la maintenance de votre enregistrement `A` de domaine racine pointant vers une seule adresse IP. Idéalement, vous souhaiteriez faire ceci :

```
example.com      IN   CNAME    my-app.herokuapp.com.www.example.com  IN   CNAME    my-app.herokuapp.com.example.com      IN   CNAME    my-app.herokuapp.com.
www.example.com  IN   CNAME    my-app.herokuapp.com.
```

pour permettre à Heroku (ou votre fournisseur d'hébergement choisi) de gérer la mise à jour de l'enregistrement `A` vers lequel pointe le `CNAME` sans aucun changement de votre côté. Cependant, comme nous le savons maintenant, cela enfreint la spécification DNS, donc c'est une très mauvaise idée.

Il est possible de simplement implémenter une redirection [301/302](https://www.namecheap.com/support/knowledgebase/article.aspx/9604/2237/types-of-domain-redirects--301-302-url-redirects-url-frame-and-cname) de `example.com` vers `www.example.com`. Cependant, cette instruction a lieu soit sur le serveur web (donc ayant toujours le problème de devoir utiliser un enregistrement `A` fixe dans le DNS pour pointer vers ce serveur web), soit via une redirection personnalisée du fournisseur DNS (qui [souffre de complications avec HTTPS](https://support.dnsimple.com/articles/url-record/) ).

Cela a également l'effet secondaire de changer le domaine que vous voyez dans la barre d'URL, ce que vous ne souhaitez peut-être pas. Cette méthode est destinée à être utilisée lorsque votre site web a déménagé de manière permanente, ou lorsque vous essayez de [préserver les classements SEO](https://support.google.com/webmasters/answer/93633?hl=en), plutôt que de résoudre notre problème de pointage vers un backend complexe et changeant de manière scalable.

### La solution

Plusieurs fournisseurs DNS ont maintenant développé des solutions personnalisées pour contourner ce problème, notamment :

* `ALIAS` chez DNSimple
* `ANAME` chez DNS Made Easy
* `ANAME` chez easyDNS
* `CNAME` (virtuel) chez CloudFlare

Ce sont tous des types d'enregistrements virtuels qui fournissent un comportement similaire à `CNAME`, sans aucun des inconvénients. La mise en œuvre exacte peut différer, mais à un niveau élevé, lorsque le serveur DNS voit l'un de ces types d'enregistrements virtuels, il agit comme un résolveur DNS. Il suit la chaîne créée par l'alias jusqu'à ce qu'il résolve un enregistrement `A` (ou des enregistrements) et retourne ces enregistrements `A` au serveur DNS. Cela 'aplatit' la chaîne `CNAME` dans les enregistrements `A` retournés, et est indistingable de la requête envoyée. La requête ne voit qu'un enregistrement `A` pur, qui ne viole pas la spécification DNS, et n'a aucun des inconvénients d'un `CNAME`.

Ces enregistrements virtuels peuvent coexister avec d'autres enregistrements à la racine sans aucune crainte de comportements non intentionnels. Selon la méthode de résolution DNS du fournisseur lors du suivi de la chaîne `CNAME`, ils peuvent également bénéficier de performances améliorées grâce à la mise en cache des recherches précédentes.

Pour une configuration DNSimple, nous configurerions comme suit. Cette solution présente tous les avantages de l'aliasing de noms de domaine, et aucun des risques de l'utiliser au niveau racine.

```
example.com      IN   ALIAS    my-app.herokuapp.com.www.example.com  IN   CNAME    my-app.herokuapp.com.
```

Merci d'avoir lu ! ?

_Comme toujours, ouvert à toute correction ou point supplémentaire._

### Ressources

* [Qu'est-ce qu'un serveur DNS](http://www.itpro.co.uk/domain-name-system-dns/30232/what-is-a-dns-server)
* [Configurer un serveur de noms DNS](https://www.wired.com/2010/02/Set_Up_a_DNS_Name_Server/)
* [Pages de support DNSimple](https://support.dnsimple.com/categories/dns/) et [Blog ALIAS](https://blog.dnsimple.com/2014/01/why-alias-record/)
* [Support Cloudflare](https://support.cloudflare.com/hc/en-us/articles/200169056-CNAME-Flattening-RFC-compliant-support-for-CNAME-at-the-root) et [Blog CNAME](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/)
* `[dig](https://www.madboa.com/geek/dig/)` [HowTo](https://www.madboa.com/geek/dig/)
* [Plusieurs](https://stackoverflow.com/questions/656009/how-to-overcome-root-domain-cname-restrictions/22659895#22659895) [excellents](https://stackoverflow.com/questions/16022324/how-to-setup-dns-for-an-apex-domain-no-www-pointing-to-a-heroku-app) [posts Stack Overflow](https://stackoverflow.com/questions/655235/is-root-domain-cname-to-other-domain-allowed-by-dns-rfc) ou [StackExchange](https://serverfault.com/questions/170194/why-cant-a-domains-root-be-a-cname?noredirect=1&lq=1) [posts](https://serverfault.com/questions/613829/why-cant-a-cname-record-be-used-at-the-apex-aka-root-of-a-domain/613830#613830)
* [Entrées Wikipedia bien rédigées](https://en.wikipedia.org/wiki/CNAME_record)
* [Blog Netlify](https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/) 'To www or not www'