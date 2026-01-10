---
title: HTTPS expliqué avec des pigeons voyageurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-10T22:07:10.000Z'
originalURL: https://freecodecamp.org/news/https-explained-with-carrier-pigeons-7029d2193351
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vHF6NNdZX9ziiW_uRYzvAA.png
tags:
- name: Cryptography
  slug: cryptography
- name: humor
  slug: humor
- name: messaging
  slug: messaging
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: HTTPS expliqué avec des pigeons voyageurs
seo_desc: 'By Andrea Zanin

  Korean translationPortuguese translationSpanish translationMongolian translationPersian
  translationVietnamese translation

  Cryptography can be a hard subject to understand. It’s full of mathematical proofs.
  But unless you are actually ...'
---

Par Andrea Zanin

[Traduction coréenne](https://www.vobour.com/%EB%B9%84%EB%91%98%EA%B8%B0%EB%A1%9C-%EC%84%A4%EB%AA%85%ED%95%98%EB%8A%94-https-https-explained-with-car)  
[Traduction portugaise](https://medium.com/inpaas/explicando-https-com-pombos-correio-68270a5b0c28)  
[Traduction espagnole](https://www.transparentcdn.com/https-explicado-palomas-mensajeras/)  
[Traduction mongole](https://medium.com/unimediasolutions/https-\u044b\u0433-\u0448\u0443\u0443\u0434\u0430\u043d\u0447-\u0442\u0430\u0433\u0442\u0430\u0430\u0433\u0430\u0430\u0440-\u0430\u0434\u0438\u043b\u0442\u0433\u0430\u043d-\u0442\u0430\u0439\u043b\u0431\u0430\u0440\u043b\u0430\u0445-\u043d\u044c-f094d38a7dc5)  
[Traduction persane](https://virgool.io/@raminpay/https-explained-hkxu4qmijmfc)  
[Traduction vietnamienne](https://blogchanhday.com/p/nhat-ky-anh-bo-cau-dua-thu-va-https/)

La cryptographie peut être un sujet difficile à comprendre. Elle est remplie de preuves mathématiques. Mais à moins que vous ne développiez réellement des systèmes cryptographiques, une grande partie de cette complexité n'est pas nécessaire pour comprendre ce qui se passe à un niveau élevé.

Si vous avez ouvert cet article en espérant créer le prochain protocole HTTPS, je suis désolé de dire que les pigeons ne suffiront pas. Sinon, préparez du café et profitez de l'article.

### Alice, Bob et ... des pigeons ?

Toute activité que vous faites sur Internet (lire cet article, acheter des choses sur Amazon, télécharger des photos de chats) revient à envoyer et recevoir des messages à et depuis un serveur.

Cela peut être un peu abstrait, alors imaginons que ces messages soient livrés par des **pigeons voyageurs**. Je sais que cela peut sembler très arbitraire, mais croyez-moi, HTTPS fonctionne de la même manière, bien que beaucoup plus rapidement.

Au lieu de parler de serveurs, de clients et de pirates, nous parlerons d'Alice, Bob et Mallory. Si ce n'est pas votre première tentative de comprendre les concepts cryptographiques, vous reconnaîtrez ces noms, car ils sont largement utilisés dans la littérature technique.

### Une première communication naïve

Si Alice veut envoyer un message à Bob, elle attache le message à la patte du pigeon voyageur et l'envoie à Bob. Bob reçoit le message, le lit et tout va bien.

Mais que se passe-t-il si Mallory intercepte le pigeon d'Alice en vol et change le message ? Bob n'aurait aucun moyen de savoir que le message envoyé par Alice a été modifié en transit.

C'est ainsi que fonctionne **HTTP**. Plutôt effrayant, n'est-ce pas ? Je n'enverrais pas mes identifiants bancaires via HTTP et vous ne devriez pas non plus.

### Un code secret

Maintenant, que se passe-t-il si Alice et Bob sont très rusés. Ils conviennent qu'ils écriront leurs messages en utilisant un code secret. Ils décaleront chaque lettre de 3 positions dans l'alphabet. Par exemple, D → A, E → B, F → C. Le message en texte clair « secret message » deviendrait « pbzobq jbppxdb ».

Maintenant, si Mallory intercepte le pigeon, elle ne pourra pas changer le message en quelque chose de significatif ni comprendre ce qu'il dit, car elle ne connaît pas le code. Mais Bob peut simplement appliquer le code à l'envers et décrypter le message où A → D, B → E, C → F. Le texte chiffré « pbzobq jbppxdb » serait décrypté en « secret message ».

Succès !

Cela s'appelle la **cryptographie à clé symétrique**, car si vous savez comment crypter un message, vous savez aussi comment le décrypter.

Le code que j'ai décrit ci-dessus est communément connu sous le nom de **chiffre de César**. Dans la vie réelle, nous utilisons des codes plus élaborés et plus complexes, mais l'idée principale est la même.

### Comment décidons-nous de la clé ?

La cryptographie à clé symétrique est très sécurisée si personne d'autre que l'expéditeur et le destinataire ne sait quelle clé a été utilisée. Dans le chiffre de César, la **clé est un décalage** du nombre de lettres dont nous décalons chaque lettre. Dans notre exemple, nous avons utilisé un décalage de 3, mais nous aurions aussi pu utiliser 4 ou 12.

Le problème est que si Alice et Bob ne se rencontrent pas avant de commencer à envoyer des messages avec le pigeon, ils n'auraient aucun moyen d'établir une clé de manière sécurisée. S'ils envoient la clé dans le message lui-même, Mallory intercepterait le message et découvrirait la clé. Cela permettrait à Mallory de lire ou de modifier le message comme elle le souhaite avant et après qu'Alice et Bob commencent à crypter leurs messages.

C'est l'exemple typique d'une **attaque de l'homme du milieu** et la seule façon de l'éviter est de changer complètement le système de cryptage.

### Des pigeons transportant des boîtes

Alice et Bob trouvent donc un système encore meilleur. Lorsque Bob veut envoyer un message à Alice, il suivra la procédure ci-dessous :

* Bob envoie un pigeon à Alice sans aucun message.
* Alice renvoie le pigeon avec une boîte portant un cadenas ouvert, mais garde la clé.
* Bob met le message dans la boîte, ferme le cadenas et envoie la boîte à Alice.
* Alice reçoit la boîte, l'ouvre avec la clé et lit le message.

De cette manière, Mallory ne peut pas changer le message en interceptant le pigeon, car elle n'a pas la clé. Le même processus est suivi lorsque Alice veut envoyer un message à Bob.

Alice et Bob viennent d'utiliser ce que l'on appelle communément la **cryptographie à clé asymétrique**. Elle est appelée asymétrique, car même si vous pouvez crypter un message (fermer la boîte), vous ne pouvez pas le décrypter (ouvrir une boîte fermée).

En termes techniques, la boîte est connue sous le nom de **clé publique** et la clé pour l'ouvrir est connue sous le nom de **clé privée**.

### Comment puis-je faire confiance à la boîte ?

Si vous avez prêté attention, vous avez peut-être remarqué que nous avons toujours un problème. Lorsque Bob reçoit cette boîte ouverte, comment peut-il être sûr qu'elle vient d'Alice et que Mallory n'a pas intercepté le pigeon et changé la boîte par une autre dont elle a la clé ?

Alice décide qu'elle signera la boîte, de cette manière, lorsque Bob reçoit la boîte, il vérifie la signature et sait que c'est Alice qui a envoyé la boîte.

Certains d'entre vous pourraient penser, comment Bob identifierait-il la signature d'Alice en premier lieu ? Bonne question. Alice et Bob ont également eu ce problème, alors ils ont décidé que, au lieu qu'Alice signe la boîte, Ted signera la boîte.

Qui est Ted ? Ted est un homme très célèbre, bien connu et dignes de confiance. Ted a donné sa signature à tout le monde et tout le monde fait confiance à ce qu'il ne signera des boîtes que pour des personnes légitimes.

Ted ne signera une boîte d'Alice que s'il est sûr que la personne demandant la signature est Alice. Ainsi, Mallory ne peut pas obtenir une boîte d'Alice signée par Ted en son nom, car Bob saura que la boîte est frauduleuse parce que Ted ne signe des boîtes pour des personnes qu'après avoir vérifié leur identité.

Ted, en termes techniques, est communément appelé **Autorité de Certification** et le navigateur avec lequel vous lisez cet article est fourni avec les signatures de diverses Autorités de Certification.

Ainsi, lorsque vous vous connectez à un site web pour la première fois, vous faites confiance à sa boîte parce que vous faites confiance à Ted et Ted vous dit que la boîte est légitime.

### Les boîtes sont lourdes

Alice et Bob ont maintenant un système fiable pour communiquer, mais ils réalisent que les pigeons transportant des boîtes sont plus lents que ceux transportant uniquement le message.

Ils décident qu'ils utiliseront la méthode de la boîte (cryptographie asymétrique) uniquement pour choisir une clé afin de crypter le message en utilisant la cryptographie symétrique (vous vous souvenez du chiffre de César ?).

De cette manière, ils obtiennent le meilleur des deux mondes. La fiabilité de la cryptographie asymétrique et l'efficacité de la cryptographie symétrique.

Dans le monde réel, il n'y a pas de pigeons lents, mais néanmoins, crypter des messages en utilisant la cryptographie asymétrique est plus lent qu'en utilisant la cryptographie symétrique, donc nous ne l'utilisons que pour échanger les clés de cryptage.

Maintenant, vous savez comment fonctionne **HTTPS** et votre café devrait également être prêt. Allez le boire, vous l'avez mérité ?