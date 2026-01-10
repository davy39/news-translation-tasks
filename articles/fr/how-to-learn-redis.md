---
title: Les bases de la base de données Redis – Comment fonctionne le CLI Redis, les
  commandes courantes et les projets d'exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-14T15:55:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-redis
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/image-46.png
tags:
- name: caching
  slug: caching
- name: database
  slug: database
- name: Redis
  slug: redis
seo_title: Les bases de la base de données Redis – Comment fonctionne le CLI Redis,
  les commandes courantes et les projets d'exemple
seo_desc: 'By Mehul Mohan

  Redis is a popular in-memory database used for a variety of projects, like caching
  and rate limiting.

  In this blog post, we will see how you can use Redis as an in-memory database, why
  you''d want to use Redis, and finally we''ll discuss...'
---

Par Mehul Mohan

Redis est une base de données en mémoire populaire utilisée pour une variété de projets, comme la mise en cache et la limitation de débit.

Dans cet article de blog, nous verrons comment vous pouvez utiliser Redis comme base de données en mémoire, pourquoi vous voudriez utiliser Redis, et enfin nous discuterons de quelques fonctionnalités importantes de la base de données. Commençons.

## Qu'est-ce qu'une base de données en mémoire ?

Les bases de données traditionnelles gardent une partie de la base de données (généralement les indices "chauds" ou souvent accédés) en mémoire pour un accès plus rapide, et le reste de la base de données sur disque.

Redis, en revanche, se concentre beaucoup sur la latence et la récupération et le stockage rapides des données. Il fonctionne donc complètement en mémoire (RAM) au lieu de dispositifs de stockage (SSD/HDD). La vitesse est importante !

Redis est une base de données clé-valeur. Mais ne vous laissez pas tromper en pensant qu'il s'agit d'une base de données simple. Vous avez de nombreuses façons de stocker et de récupérer ces clés et valeurs.

## Pourquoi avez-vous besoin de Redis ?

Vous pouvez utiliser Redis de nombreuses façons. Mais il y a deux raisons principales auxquelles je pense :

1. Vous créez une application où vous voulez rendre votre couche de code sans état. Pourquoi ? - Parce que si votre code est sans état, il est scalable horizontalement. Par conséquent, vous pouvez utiliser Redis comme un système de stockage central et laisser votre code gérer uniquement la logique.
2. Vous créez une application où plusieurs applications pourraient avoir besoin de partager des données. Par exemple, que se passe-t-il si quelqu'un essaie de forcer brutalement votre site à `payments.codedamn.com`, et une fois que vous le détectez, vous souhaitez également le bloquer à `login.codedamn.com` ? Redis permet à vos multiples services déconnectés/faiblement connectés de partager un espace mémoire commun.

## Les bases de Redis

Redis est relativement simple à apprendre car il n'y a qu'une poignée de commandes que vous devrez connaître. Dans les prochaines sections, nous couvrirons quelques concepts principaux de Redis et quelques commandes courantes utiles.

### Le CLI Redis

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ezgif.com-gif-maker.gif)

Redis dispose d'un CLI qui est une version REPL de la ligne de commande. Tout ce que vous écrivez sera évalué.

L'image ci-dessus vous montre comment faire un simple `PING` ou hello world dans Redis dans l'un de mes exercices de cours Redis sur codedamn (le cours est lié à la fin si vous voulez le vérifier).

Ce REPL Redis est très utile lorsque vous travaillez avec la base de données dans une application et que vous avez rapidement besoin de jeter un coup d'œil à quelques clés ou à l'état de Redis.

## Commandes Redis courantes

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ezgif.com-gif-maker--1-.gif)
_Essai des commandes courantes sur le CLI Redis dans le cours codedamn_

Voici quelques commandes très couramment utilisées dans Redis pour vous aider à en apprendre davantage sur son fonctionnement :

### SET

SET vous permet de définir une clé avec une valeur dans Redis.

Voici un exemple de son fonctionnement :

```
SET mehul "développeur d'inde"
```

Cela définit la clé `mehul` avec la valeur `développeur d'inde`.

### GET

GET vous permet de récupérer les clés que vous avez définies.

Voici la syntaxe :

```
GET mehul
```

Cela retournera la chaîne "développeur d'inde" comme nous l'avons définie ci-dessus.

### SETNX

Cette commande définira une valeur uniquement si la clé n'existe pas. Cette commande a un certain nombre de cas d'utilisation, y compris ne pas écraser accidentellement la valeur d'une clé qui pourrait déjà être présente.

Voici comment cela fonctionne :

```
SET key1 value1
SETNX key1 value2
SETNX key2 value2
```

Après avoir exécuté cet exemple, votre `key1` aura la valeur `value1` et `key2` comme `value2`. Cela est dû au fait que la deuxième commande n'aura aucun effet car `key1` était déjà présente.

### MSET

MSET est similaire à SET, mais vous pouvez définir plusieurs clés ensemble en une seule commande. Voici comment cela fonctionne :

```
MSET key1 "value1" key2 "value2" key3 "value3"
```

Actuellement, nous utilisons `key` et `value` comme préfixe pour les clés et les valeurs. Mais en réalité, lorsque vous écrivez un tel code, il est facile de perdre de vue ce qui est une clé et ce qui est une valeur dans une commande aussi longue.

Donc, une chose que vous pouvez faire est de toujours mettre votre valeur entre guillemets doubles, et de laisser vos clés sans guillemets (si elles sont des noms de clés valides sans guillemets).

### MGET

MGET est similaire à GET, mais il peut retourner plusieurs valeurs à la fois, comme ceci :

```
MGET key1 key2 key3 key4
```

Cela retournera quatre valeurs sous forme de tableau : `value1`, `value2`, `value3` et `null`. Nous avons obtenu `key4` comme null car nous ne l'avons jamais définie.

### DEL

Cette commande supprime une clé – assez simple, n'est-ce pas ?

Voici un exemple :

```
SET key value
GET key # vous donne "value"
DEL key 
GET key # null
```

### INCR et DECR

Vous pouvez utiliser ces deux commandes pour incrémenter ou décrémenter une clé qui est un nombre. Elles sont très utiles et vous les utiliserez beaucoup, car Redis peut effectuer deux opérations en une – GET key et SET key à key + 1.

Cela évite les allers-retours vers votre application parente, et rend l'opération également sûre à effectuer sans utiliser de transactions (plus sur cela plus tard).

Voici comment elles fonctionnent :

```
SET favNum 10
INCR favNum # 11
INCR favNum # 12
DECR favNum # 11
```

### EXPIRE

La commande EXPIRE est utilisée pour définir un minuteur d'expiration pour une clé. Techniquement, ce n'est pas un minuteur, mais un horodatage de suppression au-delà duquel la clé retournera toujours null à moins qu'elle ne soit définie à nouveau.

```
SET bitcoin 100
EXPIRE bitcoin 10

GET bitcoin # 100
# après 10 secondes
GET bitcoin # null
```

`EXPIRE` utilise un peu plus de mémoire pour stocker cette clé dans son ensemble (car maintenant vous devez également stocker quand cette clé doit expirer). Mais vous ne vous soucierez probablement jamais de ce surcoût.

### TTL

Cette commande peut être utilisée pour savoir combien de temps la clé a à vivre.

Exemple :

```
SET bitcoin 100
TTL bitcoin # -1
TTL somethingelse # -2

EXPIRE bitcoin 5
# attendre 2 secondes
TTL bitcoin # retourne 3
# après 1 seconde
GET bitcoin # null
TTL bitcoin # -2
```

Alors, que pouvons-nous apprendre de ce code ?

1. TTL retournera `-1` si la clé existe mais n'a pas d'expiration
2. TTL retournera `-2` si la clé n'existe pas
3. TTL retournera le temps de vie en secondes si la clé existe et expirera

### SETEX

Vous pouvez effectuer **SET** et **EXPIRE** ensemble avec `SETEX`.

Comme ceci :

```
SETEX key 10 value
```

Ici, la clé est "key", la valeur est "value", et le temps de vie (TTL) est 10. Cette clé sera supprimée après 10 secondes.

Maintenant que vous avez des connaissances fondamentales sur les commandes Redis de base et le fonctionnement du CLI, construisons quelques projets et utilisons ces outils dans la vie réelle.

## Projet 1 – Construire un système de mise en cache d'API avec Redis

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-13-at-4.20.13-AM.png)
_Aperçu du laboratoire de construction de système de mise en cache d'API sur codedamn_

Ce projet implique la mise en place d'un système de mise en cache d'API avec Redis, où vous mettez en cache les résultats d'un serveur tiers et les utilisez pendant un certain temps.

Cela est utile afin de ne pas être limité par le débit de ce tiers. De plus, la mise en cache améliore la vitesse de votre site, donc si vous l'implémentez correctement, c'est un gagnant-gagnant pour tout le monde.

Vous pouvez construire ce projet de manière interactive sur codedamn dans le navigateur en utilisant Node.js. Si vous êtes intéressé, vous pouvez [essayer le laboratoire de mise en cache d'API gratuitement](https://codedamn.com/learn/redis-caching-concepts-nodejs/2--CvP86ikcFeFUB4MTty).

Si vous êtes uniquement intéressé par la solution (et non par la construire vous-même), voici comment la logique principale fonctionnera en Node.js :

```js
app.post('/data', async (req, res) => {
	const repo = req.body.repo

	const value = await redis.get(repo)

	if (value) {
		// signifie que nous avons obtenu un cache hit
		res.json({
			status: 'ok',
			stars: value
		})

		return
	}

	const response = await fetch(`https://api.github.com/repos/${repo}`).then((t) => t.json())

	if (response.stargazers_count != undefined) {
		await redis.setex(repo, 60, response.stargazers_count)
	}

	res.json({
		status: 'ok',
		stars: response.stargazers_count
	})
})
```

Voyons ce qui se passe ici :

* Nous essayons d'obtenir le `repo` (qui est le format de repo passé - `facebook/react`) depuis notre cache Redis. Si présent, super ! Nous retournons le nombre d'étoiles depuis notre cache redis, ce qui nous évite un aller-retour vers les serveurs de GitHub.
* Si nous ne le trouvons pas dans le cache, nous faisons une requête vers les serveurs de GitHub, et obtenons le nombre d'étoiles. Nous vérifions si le nombre d'étoiles n'est pas indéfini (au cas où un repo n'existe pas/est privé). S'il a une valeur, nous définissons `setex` la valeur avec un délai d'expiration de 60 secondes.
* Nous définissons un délai d'expiration car nous ne voulons pas servir des valeurs obsolètes au fil du temps. Cela nous aide à actualiser notre nombre d'étoiles au moins une fois par minute.

Voici le code source complet :

%[https://github.com/codedamn-classrooms/redis-nodejs-classroom/tree/lab5sol]

## Projet 2 - Limitation de débit d'API avec Redis

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-13-at-4.21.31-AM.png)
_Aperçu de la limitation de débit d'API avec Redis_

Ce projet implique la limitation de débit d'un certain point de terminaison pour le protéger des mauvais acteurs, puis les bloquer pour qu'ils n'accèdent pas à cette API particulière.

Cela est très utile pour les points de terminaison de connexion et les API sensibles, où vous ne voulez pas qu'une seule personne frappe votre point de terminaison avec des milliers de requêtes.

Nous effectuons la limitation de débit par adresse IP dans ce laboratoire. Si vous souhaitez tenter ce codelab, vous pouvez l'essayer [gratuitement](https://codedamn.com/learn/redis-caching-concepts-nodejs/RapJaltQbkvVtm4_b5oYl) sur codedamn.

Si vous êtes uniquement intéressé par la solution (et non par la construire vous-même), voici comment la logique principale fonctionnera en Node.js :

```
app.post('/api/route', async (req, res) => {
	// ajouter des données ici
	const ip = req.headers['x-forwarded-for'] || req.ip

	const reqs = await redis.incr(ip)
	await redis.expire(ip, 2)

	if (reqs > 15) {
		return res.json({
			status: 'rate-limited'
		})
	} else if (reqs > 10) {
		return res.json({
			status: 'about-to-rate-limit'
		})
	} else {
		res.json({
			status: 'ok'
		})
	}
})
```

Comprenons ce bloc de code :

* Nous essayons d'extraire l'IP de l'en-tête `x-forwarded-for` (ou vous pouvez utiliser `req.ip` car nous utilisons express)
* Nous incrémentons le champ d'adresse IP. Si notre clé dans Redis n'a jamais existé, INCR la définirait automatiquement à 0 et l'incrémenterait, c'est-à-dire qu'elle la définirait finalement à 1.
* Nous définissons la clé pour qu'elle expire en 2 secondes. Idéalement, vous voudriez une valeur plus grande - mais c'est ce que le défi codedamn a spécifié ci-dessus, donc nous l'avons.
* Enfin, nous vérifions les comptes de requêtes, s'ils sont supérieurs à un certain seuil, nous bloquons la requête pour qu'elle n'atteigne pas le corps principal de la fonction.

Voici la solution complète :

%[https://github.com/codedamn-classrooms/redis-nodejs-classroom/tree/lab6sol]

## Plus sur Redis

Redis est bien plus que ce que nous avons appris jusqu'à présent. Mais la bonne chose est que nous avons appris suffisamment pour commencer à travailler avec déjà !

Dans cette section, couvrons quelques autres fondamentaux de Redis.

### Redis est mono-thread

Redis s'exécute comme un processus mono-thread, même sur un système multi-cœurs prenant en charge le multi-threading. Ce n'est pas un cauchemar de performance, mais une mesure de sécurité contre les lectures/écritures incohérentes dans un environnement multi-thread.

Si Redis était multi-thread, pour garantir la sécurité des threads lors de l'accès à une seule clé, vous auriez finalement résolu à un mécanisme de verrouillage, qui aurait probablement performé pire que l'accès mono-thread/séquentiel de toute façon.

### Transactions Redis

Bien sûr, vous ne pouvez pas tout faire dans Redis avec une seule commande. Mais vous pouvez certainement lui demander d'exécuter un bloc de commandes en une seule fois (c'est-à-dire que personne d'autre ne parle à Redis pendant qu'il exécute ce bloc). Vous pouvez faire cela en utilisant la commande `MULTI`.

Voici comment cela fonctionne :

```
MULTI
SET hello world
SET yo lo
SET number 1
INCR number
EXPIRE hello 10
EXPIRE yo 5
EXEC
```

Cela exécutera toutes ces opérations en une seule fois, c'est-à-dire qu'il **ne** exécutera rien du tout après `MULTI`, et exécutera tout à la fois au moment où il verra le mot-clé `EXEC`.

Redis inclut la prise en charge des listes et des ensembles pour des cas d'utilisation plus avancés. Vous pouvez également utiliser Redis comme un service de diffusion où vous **publiez** sur un canal et les autres qui ont **souscrit** au canal reçoivent une notification. Cela est très utile dans une architecture multi-clients.

## Conclusion

J'espère que vous avez aimé cette introduction à Redis. Cet article de blog fait partie du [nouveau cours interactif de codedamn : Redis + Node.js caching](https://codedamn.com/learn/redis-caching-concepts-nodejs), où vous n'apprenez pas seulement ces concepts, mais vous les pratiquez dans votre navigateur en déplacement.

N'hésitez pas à essayer le cours et faites-moi savoir ce que vous en pensez. Vous pouvez me trouver sur [twitter](https://twitter.com/mehulmpt) pour envoyer tout retour :)