---
title: Une introduction au système de noms de domaine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-23T09:14:51.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-domain-name-servers-46c6bcf9afa3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DlTgMe5CZ5BfICp6i42f-g.jpeg
tags:
- name: computer network
  slug: computer-network
- name: dns
  slug: dns
- name: internet
  slug: internet
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction au système de noms de domaine
seo_desc: 'By Sumedh Nimkarde

  You all might have heard about or know about the Domain Name System (DNS) if you
  understand how the internet works or how computer networks work. If you aren’t familiar
  with DNS, I would recommend that you go and check out my previ...'
---

Par Sumedh Nimkarde

Vous avez probablement tous entendu parler ou connaissez le système de noms de domaine (DNS) si vous comprenez comment fonctionne Internet ou comment fonctionnent les réseaux informatiques. Si vous n'êtes pas familier avec le DNS, je vous recommande d'aller consulter mon précédent article de blog qui est axé sur les réseaux informatiques [ici](https://medium.freecodecamp.org/computer-networks-and-how-to-actually-understand-them-c1401908172d).

Les noms d'hôte seuls ne peuvent pas nous indiquer où se trouve la machine/le matériel particulier avec lequel nous essayons de communiquer dans le monde. Par conséquent, toute communication se fait avec des adresses IP.

Les serveurs de noms de domaine sont les dispositifs qui mappent le nom d'hôte aux adresses IP de la machine/du matériel sur lequel vos services sont en cours d'exécution.

Dans cet article, je vais expliquer en détail les types de requêtes DNS, les types de serveurs DNS et les types d'enregistrements DNS.

### Résolveur DNS

Les résolveurs DNS sont les ordinateurs utilisés par les fournisseurs de services Internet (FAI) pour effectuer des recherches dans leur base de données pour le nom d'hôte particulier demandé par l'utilisateur. Ils redirigent ensuite cet utilisateur vers l'adresse IP mappée. Ils jouent un rôle vital dans la résolution DNS.

Les résolveurs DNS mettent également en cache les données. Par exemple, mon site web `example.com` est actuellement hébergé sur une machine avec l'adresse IP `35.195.226.230`. Ainsi, les caches des résolveurs DNS dans le monde entier ont mappé ce qui suit :

`example.com` -> `35.195.226.230`

Supposons que, dans le futur, je souhaite héberger mon site web sur un autre serveur dans le monde avec une IP de, disons, `35.192.247.235`. Les caches DNS de tous les résolveurs DNS dans le monde auront toujours l'ancienne adresse IP pendant un certain temps. Cela peut entraîner une indisponibilité du site web par des moyens conventionnels jusqu'à ce que la propagation DNS se produise complètement.

L'enregistrement dans le cache du résolveur DNS y reste pendant un certain temps, ce qui est appelé temps de vie (TTL pour Time To Live).

C'est le temps pendant lequel un enregistrement est mis en cache dans le résolveur DNS. Cela peut être défini dans le tableau de bord du bureau d'enregistrement auprès duquel vous avez acheté le domaine.

Note : à partir de maintenant, je ferai référence au résolveur DNS simplement par Résolveur dans cet article de blog.

### Types de serveurs DNS

#### **Serveur DNS racine**

Les serveurs DNS racine sont ceux qui ont les adresses de tous les serveurs de domaines de premier niveau (TLD). Une requête rencontre d'abord les serveurs DNS racine lors de son parcours pour obtenir l'adresse IP à partir du nom d'hôte.

Il existe 13 serveurs de noms de domaine racine dans le monde en 2016. Cela ne signifie pas qu'il n'y a que 13 machines gérant la charge des requêtes provenant du monde entier — il y a plusieurs serveurs au niveau local gérant la charge.

Différentes organisations gèrent les serveurs DNS racine :

![Image](https://cdn-media-1.freecodecamp.org/images/B3BTLHU-knwsZx4JFN91eiiBt-vlJvaepjeS)
_Crédits : https://iana.org_

#### **Serveur de domaine TLD**

Ce sont ceux classés selon le domaine de premier niveau. Ils sont généralement les suivants que la requête itérative atteint après le serveur DNS racine. Ils stockent les enregistrements spécifiques au TLD pour le nom d'hôte.

Supposons que nous demandons une adresse IP pour `medium.com`, alors les serveurs de domaine TLD pour le TLD « .com » sont interrogés. Les serveurs de domaine TLD renvoient l'adresse des serveurs DNS autoritaires au Résolveur.

![Image](https://cdn-media-1.freecodecamp.org/images/dY2lnrWhjllbEIQl9Wy7TwUxtwYLi7AsGX-R)
_Fig. Serveurs de noms TLD pointant vers les serveurs de noms autoritaires_

Maintenant, la question se pose : comment le serveur de noms TLD connaît-il l'adresse du serveur de noms autoritaire ? La réponse est simple : lorsque vous achetez un domaine auprès de registraires comme Godaddy ou Namecheap, les registraires communiquent également les domaines au serveur de noms TLD. Ainsi, il est en mesure de contacter les serveurs de noms autoritaires.

De nos jours, certains registraires offrent la possibilité d'utiliser des serveurs de noms autoritaires tiers. Comme le montre la figure ci-dessus, vous pouvez configurer les serveurs de noms autoritaires dans le tableau de bord du registraire.

#### **Serveur DNS autoritaire**

Ce sont ceux qui sont interrogés de manière itérative à la fin par le Résolveur. Ils stockent les enregistrements réels pour les types A, NS, CNAME, TXT, etc.

Ainsi, ils renvoient l'adresse IP du nom d'hôte si elle est disponible. Si elle n'est pas disponible même dans le serveur DNS autoritaire, ils renvoient une erreur avec un message particulier et le processus de recherche d'adresses IP dans le serveur de noms se termine.

### Types de requêtes DNS

Il existe trois types de requêtes DNS :

**Récursives** : Les requêtes récursives sont faites par les utilisateurs au Résolveur. C'est en fait la première requête faite lors de toute recherche DNS.

Les Résolveurs peuvent être votre FAI ou votre administrateur réseau, mais généralement, c'est le FAI dans presque tous les cas.

**Non récursives** : dans les requêtes non récursives, le Résolveur connaît la réponse et répond immédiatement sans faire de requêtes supplémentaires à d'autres serveurs de noms. Cela se produit parce que le serveur DNS local a l'adresse IP stockée dans son cache local ou il interroge directement les serveurs de noms autoritaires. Ils se trouvent définitivement à détenir l'enregistrement et cela évite finalement les requêtes récursives.

**Itératives** : Les requêtes itératives se produisent lorsque le Résolveur ne peut pas retourner les résultats car ils peuvent ne pas l'avoir mis en cache. Il fait donc une demande au serveur DNS racine. Et les serveurs DNS racine savent où trouver le serveur de domaine TLD particulier.

Par exemple, si nous essayons d'obtenir l'adresse IP pour, disons, `medium.com`, alors le serveur de domaine racine aura l'adresse du serveur TLD `.com` stockée et l'enverra au Résolveur. Le Résolveur demande ensuite au serveur TLD l'adresse IP. Le serveur de domaine TLD peut ne pas la connaître, mais il connaît l'adresse du serveur DNS autoritaire pour `medium.com`.

D'accord, assez de théorie. Comprenons-le par un diagramme de flux :

![Image](https://cdn-media-1.freecodecamp.org/images/5U6XICe32XPfFiNDXob5e6tM1EzcIJE7tV7i)
_Fig. Résolution DNS_

Décomposons le diagramme ci-dessus en étapes :

1. L'utilisateur fait une demande au Résolveur avec le nom d'hôte pour lequel il veut l'adresse IP. Il s'agit d'une requête récursive.
2. Le Résolveur effectue une recherche dans son cache pour voir s'il est présent.
3. S'il est présent, il le renvoie à l'utilisateur.
4. S'il ne l'a pas en cache, il fait une demande itérative aux serveurs DNS racine présents dans le monde entier. En 2016, il y a 13 serveurs DNS racine nommés de A à M. Maintenant, le serveur DNS racine recherche le TLD du domaine demandé. Par exemple, si le nom d'hôte est `medium.com`, alors le TLD devient « .com » et le serveur DNS racine a l'entrée pour les serveurs de domaine « .com » et renvoie les résultats au Résolveur. Le Résolveur doit avoir les adresses de tous les serveurs de noms de domaine racine. S'il ne les a pas, la recherche DNS peut échouer dès le début.
5. Maintenant, le Résolveur fait à nouveau une demande itérative au serveur de domaine TLD demandant l'adresse IP du domaine. Le serveur de domaine TLD renvoie ensuite l'adresse du serveur autoritaire pour le domaine demandé.
6. À partir de maintenant, je crois que vous pouvez comprendre ce que sont les serveurs DNS autoritaires. Ils contiennent les enregistrements réels où le nom d'hôte est mappé à l'adresse IP et donc l'adresse IP est renvoyée au Résolveur (qui à son tour la renvoie à l'utilisateur).
7. Si aucun enregistrement correspondant n'est trouvé dans les serveurs de noms autoritaires, une erreur avec un message indiquant « DNS_PROBE_FINISHED_NXDOMAIN » est renvoyée, indiquant qu'il n'y a pas d'enregistrement pour le nom d'hôte demandé.
8. Dans tous les serveurs de noms que la requête traverse, les résultats pour le nom d'hôte demandé sont mis en cache afin que, lorsqu'un autre utilisateur demande le même domaine, l'enregistrement sera déjà présent dans le cache DNS.
9. En résumé, il faut au maximum quatre requêtes pour effectuer la recherche DNS. Mais cela prend à peine quelques millisecondes pour effectuer la recherche.

#### **Le concept de propagation DNS**

Supposons que vous avez votre site web hébergé chez un fournisseur comme Digital Ocean sur une machine avec l'IP « x », et que vous souhaitez transférer l'hébergement du site web vers une autre machine avec une adresse IP différente, disons « y ». Vous devrez changer l'adresse IP dans les enregistrements autoritaires afin que le trafic soit dirigé vers la nouvelle adresse IP.

Même si vous mettez à jour les enregistrements dans le tableau de bord de votre registraire/serveur de noms, cela prend un certain temps pour se refléter dans tous les caches des Résolveurs dans le monde. La propagation DNS peut prendre de 24 à 72 heures, mais généralement, cela se produit plus tôt car la plupart des FAI gardent le TTL bas.

Et c'est tout !

Merci d'avoir lu l'article. Si vous avez des questions, n'hésitez pas à les poser dans les commentaires ci-dessous et partagez cet article avec qui vous voulez.

À la prochaine. Passez un bon moment. Merci.

Vous pouvez consulter mon autre article sur les réseaux informatiques qui les explique en détail :

[**Ce que sont les réseaux informatiques et comment les comprendre réellement**](https://medium.freecodecamp.org/computer-networks-and-how-to-actually-understand-them-c1401908172d)
[_Que vous soyez nouveau dans le monde du développement, ou que vous construisiez des choses depuis longtemps, ou même si vous êtes un..._medium.freecodecamp.org](https://medium.freecodecamp.org/computer-networks-and-how-to-actually-understand-them-c1401908172d)

Si vous aimez mon travail, vous pouvez m'offrir un café à :

[**Offrir un café à Sumedh Nimkarde - BuyMeACoffee.com**](http://buymeacoffee.com/lunaticmonk)
[_Bonjour, je suis Sumedh et mon travail est de construire, casser et reconstruire des choses._buymeacoffee.com](http://buymeacoffee.com/lunaticmonk)

N'hésitez pas à me contacter sur [Twitter](https://twitter.com/lunatic_monk).