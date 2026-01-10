---
title: "Comment votre téléphone ouvre medium.com\n\x14\nJe vais laisser un portier\
  \ et un bibliothécaire expliquer."
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-25T12:29:40.000Z'
originalURL: https://freecodecamp.org/news/how-can-your-phone-open-medium-com-62ec36b1429f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*53k-kW_pi3-Ai382HAH8Ow.jpeg
tags:
- name: internet
  slug: internet
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: "Comment votre téléphone ouvre medium.com\n\x14\nJe vais laisser un portier\
  \ et un bibliothécaire expliquer."
seo_desc: 'By Andrea Zanin

  Hey did you notice what just happened? You clicked a link, and now here you are
  reading this article. But did you think about how your browser knew that the link
  you clicked referred to this article, and that this article contained th...'
---

Par Andrea Zanin

Hé, avez-vous remarqué ce qui vient de se passer ? Vous avez cliqué sur un lien, et maintenant vous êtes ici en train de lire cet article. Mais avez-vous pensé à la façon dont votre navigateur savait que le lien sur lequel vous avez cliqué faisait référence à cet article, et que cet article contenait ces mots ?

C'est quelque chose de si courant que nous l'oublions, mais le mécanisme derrière est fascinant. Dans cet article, nous allons l'explorer en utilisant des analogies du monde réel.

### Comment les ordinateurs communiquent

Lorsque vous ouvrez un site web, votre navigateur demande à un autre ordinateur quelque part dans le monde les données qui lui permettront d'afficher la page (par exemple, le texte que vous êtes en train de lire maintenant).

Cet acte de demander à un autre ordinateur n'est pas sans rappeler l'envoi d'un courrier (courrier physique, pas un email) à un ami et l'attente de sa réponse.

Si John veut envoyer du courrier à Brittany, il doit connaître son adresse. Dans le monde d'Internet, au lieu d'avoir des adresses physiques, nous avons des adresses IP. Elles fonctionnent de la même manière, sauf qu'il s'agit d'un ordinateur au lieu d'une boîte aux lettres.

### Parlez-moi davantage de cette chose IP

Avant de plonger dans les détails sur les adresses IP, je veux que vous imaginiez que vous séjournez dans un hôtel de luxe avec des centaines de chambres et un portier élégant (pas mal, non ?).

Revenons maintenant aux adresses IP : votre adresse IP standard ressemble à ceci : 102.134.122.234. Les 9 premiers chiffres sont l'adresse de l'hôtel virtuel dans lequel vous séjournez, tandis que les 3 derniers sont votre chambre. Alors que l'adresse de l'hôtel virtuel est fixe, la chambre dans laquelle vous séjournez est choisie par l'hôtel.

Si quelqu'un veut vous envoyer un message, il doit connaître l'adresse de l'hôtel et votre numéro de chambre. Il envoie donc le message à l'hôtel et le portier le livre directement à vous.

L'hôtel virtuel est comme votre réseau WiFi domestique. Son adresse est décidée par votre fournisseur d'accès à Internet, tandis que votre numéro de chambre est décidé par votre routeur domestique.

### Les nombres sont compliqués

Vous avez peut-être remarqué que si vous voulez ouvrir medium.com, vous n'avez pas besoin de connaître son adresse IP. C'est là que l'Internet devient plus intelligent que le service postal.

En plus des adresses IP, il existe un système pour associer des noms faciles à retenir aux IP : le Domain Name System.

Enfin, voici ce qui se passe lorsque votre téléphone veut ouvrir medium.com

* Le téléphone envoie la demande au portier (routeur) et lui demande de l'envoyer à medium.com
* le routeur demande à une agence de confiance (votre fournisseur d'accès à Internet) l'IP de medium.com
* cette agence de confiance fait alors référence à une organisation mondiale (le Root Server) qui reconnaît le Top Level Domain (.com, .us, .org, 

)
* le Root Server demande alors au bibliothécaire numérique responsable de ce TLD
* enfin, le bibliothécaire ouvre son registre principal, cherche le site web que nous avons demandé, et répond avec l'IP

![Image](https://cdn-media-1.freecodecamp.org/images/9WfzmmiTuw5U2o4YwfFGfM4U2frg8OXY4k08)

Enfin, votre téléphone peut envoyer la demande directement à l'adresse (IP) de Medium. Tout cela en moins d'un dixième de seconde.

### Allons-nous manquer d'adresses ?

Oui, nous allons manquer d'adresses IP 

 et bientôt. Mais ne paniquez pas, une solution est déjà en cours de mise en œuvre.

D'abord, nous devons faire un pas en arrière : jusqu'à présent, j'ai parlé des adresses IP, mais j'aurais dû dire IP version 4. La solution est IP version 6, et elle est encore plus laide : 2001:0db8:0000:0042:0000:8a2e:0370:7334

Cette monstruosité alphanumérique conduit à une quantité astronomique d'IP possibles, donc le problème est résolu ??.

### Avant de partir

Dans cet article, nous avons analysé comment votre téléphone comprend ce qu'est medium.com, mais qu'en est-il de la partie HTTPS du lien ? J'ai écrit un autre article à ce sujet : [https expliqué avec des pigeons voyageurs](https://medium.freecodecamp.org/https-explained-with-carrier-pigeons-7029d2193351).

Si vous avez aimé l'article, n'oubliez pas que vous pouvez ? jusqu'à 50 fois.