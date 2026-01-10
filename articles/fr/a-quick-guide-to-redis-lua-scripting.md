---
title: Un guide rapide pour le scripting Lua dans Redis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-25T18:34:46.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-redis-lua-scripting
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/lua_script-1.jpg
tags:
- name: Lua
  slug: lua
- name: Redis
  slug: redis
- name: Scripting
  slug: scripting
seo_title: Un guide rapide pour le scripting Lua dans Redis
seo_desc: 'By Andrei Chernikov

  Redis is a popular in-memory grid used for interprocess communication and data storage.
  You might’ve heard that it lets you run Lua scripts, but you are still not sure
  why. If this sounds like you, read on.


  Prerequisites

  You shou...'
---

Par Andrei Chernikov

Redis est une grille en mémoire populaire utilisée pour la communication interprocessus et le stockage de données. Vous avez peut-être entendu dire qu'il permet d'exécuter des scripts Lua, mais vous n'êtes toujours pas sûr de savoir pourquoi. Si cela vous ressemble, continuez à lire.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/lua_script.jpg)

## Prérequis

Vous devez avoir [Redis installé sur votre système](https://redis.io/topics/quickstart) pour suivre ce guide. Il peut être utile de consulter la [référence des commandes Redis](https://redis.io/commands) pendant la lecture.

## Pourquoi ai-je besoin de scripts Lua ?

En bref : pour un gain de performance. La plupart des tâches que vous effectuez dans Redis impliquent de nombreuses étapes. Au lieu d'effectuer ces étapes dans le langage de votre application, vous pouvez les effectuer directement dans Redis avec Lua.

* Cela peut entraîner de meilleures performances.
* De plus, toutes les étapes d'un script sont exécutées de manière atomique. Aucune autre commande Redis ne peut s'exécuter pendant qu'un script est en cours d'exécution.

Par exemple, j'utilise des scripts Lua pour modifier des chaînes JSON stockées dans Redis. Je décris cela en détail plus près de la fin de cet article.

## Mais je ne connais pas Lua

![Image](https://www.freecodecamp.org/news/content/images/2019/09/dont-know-s.png)
_Une personne qui ne connaît pas Lua_

Ne vous inquiétez pas, Lua n'est pas très difficile à comprendre. Si vous connaissez [un langage de la famille C](https://en.wikipedia.org/wiki/List_of_C-family_programming_languages), vous devriez vous en sortir avec Lua. De plus, je fournis des exemples fonctionnels dans cet article.

## Montrez-moi un exemple

Commençons par exécuter des scripts via **redis-cli**. Lancez-le avec :

```shell
redis-cli
```

Exécutez maintenant la commande suivante :

```redis
eval "redis.call('set', KEYS[1], ARGV[1])" 1 key:name value
```

La commande **EVAL** indique à Redis d'exécuter le script qui suit. La chaîne `"redis.call('set', KEYS[1], ARGV[1])"` est notre script, qui est fonctionnellement identique à la commande `set` de Redis. Trois paramètres suivent le texte du script :

1. Le nombre de clés fournies
2. Le nom de la clé
3. Le premier argument

Les arguments du script se divisent en deux groupes : **KEYS** et **ARGV**.

Nous spécifions le nombre de clés dont le script a besoin avec le nombre qui suit immédiatement. Dans notre exemple, c'est **1**. Immédiatement après ce nombre, nous devons fournir ces clés, une après l'autre. Elles sont accessibles sous forme de tableau **KEYS** dans le script. Dans notre cas, il contient une seule valeur `key:name` à l'index **1**.

*Notez que les tableaux indexés Lua commencent à l'index* **_1,_** *et non* **_0_**_.*

Nous pouvons fournir n'importe quel nombre d'arguments après les clés, qui seront disponibles dans Lua sous forme de tableau **ARGV**. Dans cet exemple, nous fournissons un seul argument **ARGV** : la chaîne `value`. Comme vous l'avez déjà deviné, la commande ci-dessus définit la clé `key:name` avec la valeur `value`.

Il est considéré comme une bonne pratique de fournir les clés utilisées par le script en tant que **KEYS**, et tous les autres arguments en tant que **ARGV**. Vous ne devriez donc pas spécifier **KEYS** comme 0 et ensuite fournir toutes les clés dans le tableau **ARGV**.

Vérifions maintenant si le script s'est exécuté avec succès. Nous allons le faire en exécutant un autre script qui récupère la clé de Redis :

eval "return redis.call('get', KEYS[1])" 1 key:name

Le résultat devrait être `"value"`, ce qui signifie que le script précédent a correctement défini la clé `"key:name"`.

## Pouvez-vous expliquer le script ?

![Image](https://miro.medium.com/max/465/1*Utfw9sl2XFHDpyulDvoIvA.jpeg)
_Doge après avoir vu le script ci-dessus_

Notre premier script se compose d'une seule instruction : la fonction `redis.call` :

```lua
redis.call('set', KEYS[1], ARGV[1])
```

Avec `redis.call`, vous pouvez exécuter n'importe quelle commande Redis. Le premier argument est le nom de cette commande, suivi de ses paramètres. Dans le cas de la commande `set`, ces arguments sont **key** et **value**. Toutes les commandes Redis sont supportées. [Selon la documentation](https://redis.io/commands/eval) :

> _Redis utilise le même interpréteur Lua pour exécuter toutes les commandes_

Notre deuxième script fait un peu plus que simplement exécuter une seule commande — il retourne également une valeur :

```redis
eval "return redis.call('get', KEYS[1])" 1 key:name
```

Tout ce qui est retourné par le script est envoyé au processus appelant. Dans notre cas, ce processus est **redis-cli** et vous verrez le résultat dans votre fenêtre de terminal.

## Quelque chose de plus complexe ?

![Image](https://www.freecodecamp.org/news/content/images/2019/09/man-looking-at-board.jpg)
_Une personne planifiant de construire un script Redis complexe_

J'ai déjà utilisé des scripts Lua pour retourner des éléments d'une table de hachage dans un ordre particulier. L'ordre lui-même était spécifié par des clés de hachage stockées dans un ensemble trié.

Commençons par configurer nos données en exécutant ces commandes dans **redis-cli** :

```redis
hmset hkeys key:1 value:1 key:2 value:2 key:3 value:3 key:4 value:4 key:5 value:5 key:6 value:6
zadd order 1 key:3 2 key:1 3 key:2
```

Ces commandes créent une table de hachage à la clé `hkeys` et un ensemble trié à la clé `order` qui contient des clés sélectionnées de `hkeys` dans un ordre spécifique.

*Vous pourriez vouloir consulter la référence des commandes* [_hmset_](https://redis.io/commands/hmset) *et* [_zadd_](https://redis.io/commands/zadd) *pour plus de détails.*

Exécutons le script suivant :

```redis
eval "local order = redis.call('zrange', KEYS[1], 0, -1); return redis.call('hmget',KEYS[2],unpack(order)); 2 order hkeys
```

Vous devriez voir le résultat suivant :

```redis
"value:3"
"value:1"
"value:2"
```

Ce qui signifie que nous avons obtenu les valeurs des clés que nous voulions et dans le bon ordre.

## Dois-je spécifier le texte complet du script pour l'exécuter ?

Non ! Redis vous permet de précharger un script en mémoire avec la commande **SCRIPT LOAD** :

```redis
script load "return redis.call('get', KEYS[1])"
```

Vous devriez voir un résultat comme ceci :

```redis
"4e6d8fc8bb01276962cce5371fa795a7763657ae"
```

Il s'agit du hash unique du script que vous devez fournir à la commande **EVALSHA** pour exécuter le script :

```redis
evalsha 4e6d8fc8bb01276962cce5371fa795a7763657ae 1 key:name
```

*Note : vous devez utiliser le hash* **_SHA1_** *réel retourné par la commande* **_SCRIPT LOAD_**_, le hash ci-dessus n'est qu'un exemple.*

## Que disiez-vous à propos de la modification de JSON ?

Parfois, les gens stockent des objets JSON dans Redis. Que ce soit une bonne idée ou non est une autre histoire, mais en pratique, cela arrive souvent.

Si vous devez modifier une clé dans cet objet JSON, vous devez le récupérer de Redis, le parser, modifier la clé, puis le sérialiser et le renvoyer à Redis. Il y a quelques problèmes avec cette approche :

1. Concurrence. Un autre processus peut modifier ce JSON entre nos opérations de récupération et de définition. Dans ce cas, la modification sera perdue.
2. Performance. Si vous effectuez ces modifications suffisamment souvent et si l'objet est plutôt grand, cela peut devenir le goulot d'étranglement de votre application. Vous pouvez gagner en performance en implémentant cette logique en Lua.

Ajoutons une chaîne JSON de test à Redis sous la clé `obj` :

```redis
set obj '{"a":"foo","b":"bar"}'
```

Exécutons maintenant notre script :

```redis
EVAL 'local obj = redis.call("get",KEYS[1]); local obj2 = string.gsub(obj,"(" .. ARGV[1] .. "\")(:)([^,}]+)", "%1" .. ARGV[2]); return redis.call("set",KEYS[1],obj2);' 1 obj b bar2
```

Maintenant, nous aurons l'objet suivant sous la clé `obj` :

```
{"a":"foo","b":"bar2"}
```

Vous pouvez également charger ce script avec la commande **SCRIPT LOAD** :

```redis
SCRIPT LOAD 'local obj = redis.call("get",KEYS[1]); local obj2 = string.gsub(obj,"(" .. ARGV[1] .. "\")(:)([^,}]+)", "%1" .. ARGV[2]); return redis.call("set",KEYS[1],obj2);'
```

 et ensuite l'exécuter comme ceci :

```redis
EVALSHA <your_script_sha> 1 obj b bar2
```

**Quelques notes :**

* Le `..` est l'opérateur de concaténation de chaînes en Lua.
* Nous utilisons un motif RegEx pour faire correspondre la clé et remplacer sa valeur. Si vous ne comprenez pas cette expression régulière, [vous pouvez consulter mon guide récent](https://medium.freecodecamp.org/simple-regex-tricks-for-beginners-3acb3fa257cb).
* Une différence entre la version Lua de RegEx et la plupart des autres versions est que nous utilisons `%` comme marque de référence arrière et caractère d'échappement pour les symboles spéciaux RegEx.
* Nous échappons toujours `"` avec `\` et non `%` car nous échappons le délimiteur de chaîne Lua, et non le symbole spécial RegEx.

## Dois-je toujours utiliser des scripts Lua ?

Non. Je recommande de les utiliser uniquement lorsque vous pouvez prouver que cela entraîne de meilleures performances. Exécutez toujours des benchmarks d'abord.

Si tout ce que vous voulez est l'atomicité, alors [vous devriez vérifier les transactions Redis à la place](https://redis.io/topics/transactions).

De plus, votre script ne devrait pas être trop long. N'oubliez pas que pendant qu'un script est en cours d'exécution, tout le reste attend qu'il se termine. Si votre script prend beaucoup de temps, il peut causer des goulots d'étranglement au lieu d'améliorer les performances. Le script s'arrête après avoir atteint un timeout (5 secondes par défaut).

![Image](https://miro.medium.com/max/940/1*KuCJoYrILg1eaBYHpEhQhg.jpeg)
_Les scripts Redis ne doivent pas prendre trop de temps_

## Dernier mot

Pour plus d'informations sur Lua, consultez [lua.org](http://www.lua.org/start.html).

Vous pouvez consulter [ma bibliothèque node.js sur GitHub](https://github.com/aikei/redis-json) pour quelques exemples de scripts Lua (voir le dossier `src/lua`). Vous pouvez également utiliser cette bibliothèque dans node.js pour modifier des objets JSON sans écrire de scripts Lua vous-même.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

**Merci d'avoir lu cet article. Les questions et commentaires sont grandement appréciés. Vous êtes également les bienvenus pour me suivre** [**sur Twitter**](https://twitter.com/aikei_en)**.**