---
title: Qu'est-ce qu'ANAME ? Tutoriel DNS sur les enregistrements ANAME
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-05-02T18:02:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-aname-aname-record-dns-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/alias-1.png
tags:
- name: dns
  slug: dns
- name: domain names
  slug: domain-names
seo_title: Qu'est-ce qu'ANAME ? Tutoriel DNS sur les enregistrements ANAME
seo_desc: 'If you’ve ever had to make a domain name work with a website, you’ve probably
  seen ANAME as some record – just like the popular Canonical name record type or
  simply CNAME.

  CNAME and ANAME are both solutions for pointing a hostname to your website. Fo...'
---

Si vous avez déjà dû faire fonctionner un nom de domaine avec un site web, vous avez probablement vu ANAME comme un type d'enregistrement – tout comme le type d'enregistrement de nom canonique populaire ou simplement CNAME.

CNAME et ANAME sont deux solutions pour pointer un nom d'hôte vers votre site web. Par exemple, `yourapp.netlify.com` vers `yourwebsite.com`.

Vous avez probablement utilisé CNAME pour faire pointer des noms de domaine vers des sites web. Mais au lieu de cela, vous pouvez utiliser un ANAME qui présente certains avantages supplémentaires car il vous offre plus de flexibilité.

Dans cet article, vous apprendrez ce qu'est ANAME, les avantages qu'il présente par rapport à CNAME, et quand l'utiliser.

## Qu'est-ce qu'ANAME ?
ANAME, également appelé ALIAS, est un type d'enregistrement de domaine qui peut être utilisé à la place d'un enregistrement CNAME. Il est disponible auprès de sociétés de noms de domaine telles que Namecheap, GoDaddy, Hostinger, Google Domain, et bien d'autres.

ANAME est né de la combinaison de CNAME et d'un autre type d'enregistrement appelé A. Ainsi, ANAME est un CNAME et un enregistrement A en un seul package.

ANAME n'est pas un enregistrement DNS réel mais un moyen de le simuler. Et c'est pourquoi il est appelé Alias name, ou ANAME en abrégé.

Lorsque vous achetez un nom de domaine et que vous vous connectez à son panneau de gestion, vous verrez toujours une option pour utiliser ANAME.

N.B. : Certains fournisseurs de noms de domaine l'appellent ALIAS au lieu de ANAME

Ci-dessous se trouve le panneau Namecheap pour la gestion des domaines et ils l'appellent ALIAS.
![alias](https://www.freecodecamp.org/news/content/images/2022/04/alias.png)

## Comment fonctionne ANAME ?

Tout comme CNAME, ANAME mappe un nom de domaine à un autre. Ainsi, un ANAME est configuré pour pointer vers un autre domaine.

Lorsque le nom de domaine vers lequel un ANAME pointe est interrogé par le navigateur client, il répond avec une adresse IP. Un CNAME, en revanche, ne peut pas pointer vers une adresse IP, mais un ANAME le peut. C'est l'un des avantages d'ANAME sur CNAME.

De plus, un autre avantage d'ANAME sur CNAME est qu'il peut coexister avec d'autres enregistrements sur ce nom de domaine. Donc, si vous souhaitez avoir des sous-domaines, vous devriez utiliser ANAME au lieu de CNAME.

## Réflexions finales

Cet article a expliqué ce qu'est ANAME et l'a comparé avec CNAME afin que vous puissiez connaître les avantages qu'il présente par rapport à CNAME.

Vous vous demandez peut-être aussi lequel utiliser entre ANAME et CNAME, ou quand utiliser l'un plutôt que l'autre.

Voici la logique :
- si vous savez que vous ne pouvez pas avoir d'autres enregistrements sur un nom de domaine, utilisez CNAME. Cela est dû au fait qu'il ne peut pas coexister avec d'autres données sur l'enregistrement pour un nom de domaine.
- Si vous aurez d'autres enregistrements comme des sous-domaines sur ce nom de domaine, utilisez alors ANAME. Et si vous ne savez pas si vous aurez encore un sous-domaine ou non, utilisez ANAME.

Merci d'avoir lu.