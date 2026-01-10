---
title: Comment fonctionne HTTP et pourquoi c'est important – Expliqué en anglais simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T21:14:32.000Z'
originalURL: https://freecodecamp.org/news/how-the-internet-works
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98f0740569d1a4ca1ced.jpg
tags:
- name: communication
  slug: communication
- name: http
  slug: http
- name: internet
  slug: internet
seo_title: Comment fonctionne HTTP et pourquoi c'est important – Expliqué en anglais
  simple
seo_desc: "By Fredrik Strand Oseberg\nImagine that your house is a huge computer.\
  \ Instead of Goodison Street or 4th Avenue, your home address consists of numbers.\
  \ For example: 112.231.31.20. \nLike in a futuristic movie, your city consists largely\
  \ of high-tech ro..."
---

Par Fredrik Strand Oseberg

Imaginez que votre maison est un énorme ordinateur. Au lieu de Goodison Street ou 4th Avenue, votre adresse se compose de chiffres. Par exemple : 112.231.31.20. 

Comme dans un film futuriste, votre ville est principalement composée de robots high-tech dans le ciel allant de maison en maison, livrant leurs messages et transportant des réponses.

Vous voyez le tableau ?

## Aperçu du fonctionnement d'Internet

Simplifié, voici ce qui se passe lorsque vous tapez une adresse web dans votre navigateur :

* Il trouve l'adresse de la « maison » où vous souhaitez envoyer la demande
* Il envoie la demande en utilisant le facteur robotique
* Il attend patiemment la réponse du facteur robotique

Tout cela est abstrait pour vous en tant qu'utilisateur final. Vous tapez l'adresse web dans le navigateur, et la page web apparaît devant vos yeux – comme par magie. 

Comme toute technologie suffisamment avancée, l'utilisateur moyen ne pourrait pas utiliser Internet sans ces abstractions.

La plupart du temps, vous n'avez pas besoin de vous soucier de savoir comment quelque chose fonctionne – vous devez simplement savoir que cela fonctionne.

Mais pour certains sujets, approfondir un peu les détails est utile, ou satisfait simplement cette curiosité.

Vous ne deviendrez pas un expert des détails techniques d'Internet en lisant cet article – cela prendra beaucoup plus de temps et d'efforts – mais vous obtiendrez une vue d'ensemble et une meilleure compréhension. 

Si vous souhaitez en savoir plus, [j'ai une playlist sur YouTube qui approfondit le sujet.](https://www.youtube.com/playlist?list=PL_kr51suci7XVVw4SJLZ0QQBAsL2K8Opy)

## Le système de messagerie

D'après la métaphore du début de cet article, nous avons appris qu'Internet consiste en des messages qui circulent. Pour la plupart, ces messages sont envoyés en utilisant ce que l'on appelle le protocole HTTP.

Protocole. C'est un mot effrayant. C'est un mot qui fait baisser les yeux et fermer le navigateur. Alors décomposons-le en termes plus simples.

> Un protocole est simplement un mot sophistiqué pour accord.

Rendons cela plus clair avec une analogie. 

Disons que vous et votre meilleur ami vous laissez des messages secrets. Lorsque vous trouvez un morceau de papier sur votre pas de porte avec le mot « ballfoot », vous savez que votre ami veut vous rencontrer pour jouer au football ce soir à 20h00. 

Vous savez cela parce que vous avez convenu que le mot « ballfoot » sur un morceau de papier livré à votre maison représente une invitation à jouer.

Maintenant, un problème survient lorsque vous commencez à laisser vos autres amis le mot « ballfoot » sans leur dire le sens secret. Ils ne sauraient pas quoi faire de cette information. 

Ils trouveraient le mot sur leur pas de porte, se gratteraient la tête pendant une minute, puis continueraient à jouer à Fortnite dans leur salon. Et vous et votre seul autre ami vous passeriez le ballon entre vous. Aller et retour. Aller et retour. Jusqu'à ce que l'ennui devienne insupportable et que vous rentriez tous les deux chez vous.

Mais cela n'a pas à être ainsi. Que se passerait-il si vous disiez à vos amis ce que signifie « ballfoot » ? Maintenant, tous vos amis sauraient et partageraient l'accord que le mot « ballfoot » signifie se présenter et jouer au football sur le terrain local à 20h00. 

Succès.

C'est – en essence – ce que représente le protocole HTTP. Nous avons convenu que si nous envoyons un message d'une certaine manière, le serveur le comprendra et donnera une réponse en retour.

### La structure du message

Examinons de plus près l'accord HTTP. Il se compose de requêtes et de réponses. En termes simples, vous demandez quelque chose et obtenez ensuite une réponse de quelque chose appelé serveur. 

Avant de continuer, modifions notre métaphore du début pour mieux comprendre les cycles de requête/réponse HTTP. 

Vous souvenez-vous des robots allant de maison en maison pour livrer des messages ? Imaginez maintenant que tous ces robots appartiennent à quelqu'un.

Vous avez votre propre robot personnel, et vous pouvez lui demander d'aller à n'importe quelle adresse (adresse IP) avec des messages. Une fois que votre robot arrive avec votre message à l'adresse donnée, il entrera et proclamera hardiment qu'il a un message à livrer. Ensuite, il pronontera le message.

Pour les besoins de la métaphore, imaginez que les portes des maisons (serveurs) sont comme l'entrée des mines de la Moria dans Le Seigneur des Anneaux. Seules les bonnes paroles ouvriront la porte et vous laisseront entrer.

Dans ce cas, seules les paroles prononcées par vos robots de manière spécifique leur permettront de recevoir un message de réponse à rapporter.

C'est le protocole HTTP en action. Il existe un ensemble de règles prédéfinies guidant l'apparence des messages de requête et de réponse.

À ce stade, vous vous demandez peut-être d'où viennent ces messages. Vous ne les écrivez certainement pas vous-même lorsque vous entrez l'adresse du site web dans votre navigateur. 

Eh bien, tout est géré automatiquement pour vous par le navigateur. Lorsque vous entrez une adresse, votre navigateur se charge de composer le message de requête HTTP pour vous et l'envoie au serveur. Le message de requête HTTP ressemble à ceci :

```
GET / HTTP/1.1
Host: google.com
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) 
Version/11.0 Mobile/15A372 Safari/604.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,
image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
...etc
```

Cela semble effrayant, n'est-ce pas ?

Heureusement, le navigateur le fait pour nous. 

Examinons de plus près la première ligne : `GET / HTTP/1.1`. Cette ligne fait en sorte que votre robot aille chez Google et dise : "Puis-je recevoir ce que vous avez à la racine de votre site ?" (Cela signifie que nous voulons récupérer ce qui se trouve à www.google.com, et non à www.google.com/home.)

Nous avons donc livré notre message à la maison de Google (le serveur) de la manière correcte. Les portes s'illuminent et s'ouvrent.

À l'intérieur, vous voyez un autre robot. Derrière lui se trouve une série de boîtes verrouillées marquées avec des textes comme `GET / HTTP/1.1` et `GET /search HTTP/1.1`. Si votre requête correspond à l'une de ces boîtes, le robot la déverrouillera et donnera à votre robot le contenu, ce qui le fera revenir rapidement vers vous avec la réponse.

### La réponse

La réponse que vous recevez ressemble à ceci :

```text
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 88
Content-Type: text/html
Connection: Closed
```

Vous ne verrez jamais cette réponse à moins de vraiment vouloir l'inspecter dans les outils de développement de votre navigateur. Mais néanmoins, vous la recevez. 

Ce qui se passe ensuite dépend du type de réponse que vous recevez et de ce qui se trouvait dans la boîte verrouillée du serveur.

Dans de nombreux cas, ce que vous recevez en retour est un document HTML. Le HTML représente la structure des pages web et définit ce que le navigateur doit afficher. 

Si vous allez sur www.google.com, vous recevrez un fichier HTML en retour qui définit comment le site google.com sera affiché dans votre navigateur.

Si vous avez un peu de temps, cette vidéo de 11 minutes approfondit les requêtes et réponses HTTP :

%[https://www.youtube.com/watch?v=8QfaJudvpmo&list=PL_kr51suci7XVVw4SJLZ0QQBAsL2K8Opy&index=3]

## Conclusion

Dans cet article, nous avons passé en revue le fonctionnement d'Internet et comment nous utilisons HTTP pour communiquer sur Internet. 

Nous avons appris que le protocole HTTP est utilisé pour communiquer entre les navigateurs et les serveurs sur Internet et consiste en une norme généralement acceptée pour l'envoi et la réception des requêtes. 

Nous avons également exploré l'importance d'avoir de telles normes de communication et les avantages d'avoir une norme généralement acceptée.

Il existe de nombreuses autres facettes pour comprendre le fonctionnement d'Internet et les types de réponses que vous pouvez recevoir.

Si vous avez un moment, cette vidéo de 18 minutes vous apprenant à créer un serveur web passera en revue de nombreux sujets abordés dans cet article et en couvrira de nouveaux :

%[https://www.youtube.com/watch?v=R5uwuG1wPR8&list=PL_kr51suci7XVVw4SJLZ0QQBAsL2K8Opy&index=6]

Vous devriez maintenant avoir une compréhension générale du fonctionnement de la communication sur Internet. 

Si vous pensez que quelqu'un d'autre pourrait bénéficier de cet article, veuillez en parler. Et si vous souhaitez savoir quand je publie plus de contenu, vous pouvez [vous abonner à ma chaîne YouTube](https://www.youtube.com/channel/UCZTeUahnA2GMoo_YpTBFo9A), ou vous pouvez me suivre [@foseberg sur Twitter](https://twitter.com/foseberg).