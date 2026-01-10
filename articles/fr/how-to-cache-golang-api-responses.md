---
title: Comment mettre en cache les réponses d'API Golang pour une haute performance
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2025-10-15T10:27:00.135Z'
originalURL: https://freecodecamp.org/news/how-to-cache-golang-api-responses
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760523799795/3b48a898-77fc-4983-90b5-6e21e8019f1e.png
tags:
- name: golang
  slug: golang
- name: Go Language
  slug: go
- name: caching
  slug: caching
- name: cache
  slug: cache
seo_title: Comment mettre en cache les réponses d'API Golang pour une haute performance
seo_desc: Go makes it easy to build APIs that are fast out of the box. But as usage
  grows, speed at the language level is not enough. If every request keeps hitting
  the database, crunching the same data, or serializing the same JSON over and over,
  latency cree...
---

Go facilite la création d'API rapides dès le départ. Mais à mesure que l'utilisation augmente, la vitesse au niveau du langage ne suffit plus. Si chaque requête continue de solliciter la base de données, de traiter les mêmes données ou de sérialiser le même JSON encore et encore, la latence augmente et le débit en pâtit. La mise en cache est l'outil qui maintient une performance élevée en stockant le travail déjà effectué afin que les requêtes futures puissent le réutiliser instantanément. Examinons quatre façons pratiques de mettre en cache des API en Go, chacune expliquée par une analogie et appuyée par un code simple que vous pouvez adapter.

## Table des matières

* [Mise en cache des réponses avec stockage local et Redis](#heading-mise-en-cache-des-reponses-avec-stockage-local-et-redis)
    
* [Mise en cache des résultats de requêtes de base de données](#heading-mise-en-cache-des-resultats-de-requetes-de-base-de-donnees)
    
* [Mise en cache HTTP avec ETag et Cache-Control](#heading-mise-en-cache-http-avec-etag-et-cache-control)
    
* [Stale-While-Revalidate avec rafraîchissement en arrière-plan](#heading-stale-while-revalidate-avec-rafraichissement-en-arriere-plan)
    
* [Conclusion](#heading-conclusion)
    

## Mise en cache des réponses avec stockage local et Redis

Lorsque le processus de génération d'une réponse d'API devient coûteux, la solution la plus rapide consiste à stocker l'intégralité de la réponse. Pensez à un café pendant l'heure de pointe du matin. Si chaque client commande le même latte, le barista pourrait moudre les grains et faire mousser le lait pour chaque commande, mais la file d'attente avancerait lentement. Une solution plus intelligente consiste à préparer une cafetière une seule fois et à verser à partir de celle-ci de manière répétée. Pour gérer à la fois la vitesse et l'échelle, le café garde une petite cafetière au comptoir pour un service instantané et une plus grande urne à l'arrière pour les recharges. En termes de logiciel, la cafetière du comptoir est un cache local en mémoire tel que [Ristretto](https://pkg.go.dev/github.com/dgraph-io/ristretto) ou [BigCache](https://pkg.go.dev/github.com/allegro/bigcache), et l'urne est [Redis](https://redis.io/), qui permet à plusieurs serveurs d'API de partager les mêmes réponses mises en cache.

En Go, cette configuration à deux niveaux suit généralement un modèle de cache-aside : on regarde d'abord dans la mémoire locale, on se rabat sur Redis si nécessaire, et on ne calcule le résultat que lorsque les deux couches échouent. Une fois calculée, la valeur est sauvegardée dans Redis pour tout le monde et en mémoire pour une réutilisation immédiate lors du prochain appel.

```go
val, ok := local.Get(key)
if !ok {
    val, err = rdb.Get(ctx, key).Result()
    if err == redis.Nil {
        val = computeResponse() // expensive DB or logic
        _ = rdb.Set(ctx, key, val, 60*time.Second).Err()
    }
    local.Set(key, val, 1)
}
w.Header().Set("Content-Type", "application/json")
w.Write([]byte(val))
```

Dans le code ci-dessus, la première tentative consiste à récupérer la réponse du cache local, qui renvoie instantanément si la clé ou les données existent. Si elles ne sont pas trouvées, il interroge Redis comme deuxième couche. Si Redis ne renvoie rien non plus, le calcul coûteux s'exécute et son résultat est stocké dans Redis avec une expiration de soixante secondes afin que d'autres services puissent y accéder, puis placé dans le cache local pour une réutilisation immédiate. Après quoi, la réponse est renvoyée au client sous forme de JSON.

Cela vous offre le meilleur des deux mondes : des réponses ultra-rapides pour les appels répétés et un cache cohérent sur tous vos serveurs d'API.

## Mise en cache des résultats de requêtes de base de données

Parfois, l'API elle-même est simple, mais le coût réel se cache dans la base de données. Imaginez une salle de rédaction attendant les résultats des élections. Si chaque éditeur continue d'appeler le bureau de comptage pour les mêmes chiffres, les lignes téléphoniques risquent de saturer. Au lieu de cela, un reporter appelle une fois, écrit le résultat sur un tableau, et chaque éditeur recopie à partir de là. Le tableau est le cache, et il permet d'économiser à la fois du temps et de la pression sur le bureau.

En Go, vous pouvez appliquer le même principe en mettant en cache les résultats des requêtes. Plutôt que de solliciter la base de données pour chaque requête identique, vous stockez le résultat dans Redis avec une clé qui représente l'intention de la requête. Lorsque la requête suivante arrive, vous extrayez de Redis, ignorez la base de données et répondez plus rapidement.

```go
key := fmt.Sprintf("q:UserByID:%d", id)
if b, err := rdb.Get(ctx, key).Bytes(); err == nil {
    var u User
    _ = json.Unmarshal(b, &u)
    return u
}

u, _ := repo.GetUser(ctx, id) // real DB call
bb, _ := json.Marshal(u)
_ = rdb.Set(ctx, key, bb, 2*time.Minute).Err()
return u
```

Ici, nous construisons une clé de cache qui identifie de manière unique la requête à l'aide de l'ID utilisateur, puis nous tentons de récupérer le résultat sérialisé depuis Redis. Si la clé existe, elle désérialise les octets en une structure `User` et renvoie immédiatement sans toucher à la base de données. En cas d'échec du cache, elle exécute la requête réelle de la base de données via le repository, sérialise l'objet `User` en JSON, le stocke dans Redis avec une expiration de deux minutes et renvoie le résultat.

Ce modèle réduit considérablement la charge de la base de données et le temps de réponse pour les API lourdes en lecture, mais vous devez vous rappeler d'effacer ou de rafraîchir les entrées lorsque les données changent, ou de définir des valeurs de durée de vie (TTL) courtes pour garder les résultats raisonnablement frais.

## Mise en cache HTTP avec ETag et Cache-Control

La mise en cache ne doit pas nécessairement se faire uniquement à l'intérieur du serveur. Le standard HTTP fournit déjà des outils qui permettent aux clients ou aux CDNs de réutiliser les réponses. En définissant des en-têtes comme `ETag` et `Cache-Control`, vous pouvez indiquer au client si la réponse a changé. Si rien n'est nouveau, le client conserve sa propre copie et le serveur n'envoie qu'une réponse 304 légère.

C'est semblable à un gestionnaire affichant des avis sur un tableau de bureau. Chaque feuille porte un petit tampon. Les employés comparent le tampon avec celui qu'ils possèdent déjà. S'il correspond, ils savent que leur copie est toujours valide et évitent d'en prendre une nouvelle. Ce n'est que lorsque le tampon change qu'ils la remplacent.

En Go, c'est simple. Calculez un ETag à partir du corps de la réponse, comparez-le avec ce que le client envoie, et décidez s'il faut renvoyer la charge utile complète ou simplement le code 304.

```go
etag := computeETag(responseBytes)
if match := r.Header.Get("If-None-Match"); match == etag {
    w.WriteHeader(http.StatusNotModified)
    return
}

w.Header().Set("ETag", etag)
w.Header().Set("Cache-Control", "public, max-age=60")
w.Write(responseBytes)
```

Le code ci-dessus génère un ETag, qui est une empreinte numérique ou un hash du contenu de la réponse, puis vérifie si le client a envoyé un en-tête `If-None-Match` avec un ETag correspondant d'une requête précédente. Si les ETags correspondent, le contenu n'a pas changé, le serveur répond donc avec un statut 304 Not Modified et n'envoie aucun corps, économisant ainsi de la bande passante. Lorsque les ETags ne correspondent pas ou que le client n'a pas de version mise en cache, le serveur joint le nouvel ETag et un en-tête `Cache-Control` qui autorise la mise en cache publique pendant soixante secondes, puis envoie la réponse complète.

Cette approche réduit la bande passante, diminue l'utilisation du CPU et se marie bien avec les CDNs qui peuvent mettre en cache et servir les réponses directement.

## Stale-While-Revalidate avec rafraîchissement en arrière-plan

Il existe des cas où servir des données légèrement anciennes est acceptable si cela permet de garder l'API rapide. Les tableaux de bord boursiers, les résumés analytiques ou les points de terminaison de flux (feeds) correspondent souvent à ce modèle. Au lieu de faire attendre les utilisateurs pour des données fraîches à chaque requête, vous pouvez servir la valeur mise en cache immédiatement et la rafraîchir discrètement en arrière-plan. Cette technique est appelée Stale-While-Revalidate.

Imaginez un écran de téléscripteur boursier dans un hall d'entrée. Les chiffres peuvent avoir quelques secondes de retard, mais ils sont toujours utiles pour quiconque jette un coup d'œil au tableau. Pendant ce temps, un processus en arrière-plan récupère les derniers chiffres et met à jour le téléscripteur. Le lecteur ne regarde jamais un écran vide et le système reste réactif même pendant les pics de trafic.

En Go, cela peut être construit en stockant non seulement les données mises en cache, mais aussi des horodatages qui définissent quand les données sont fraîches, quand elles peuvent encore être servies comme périmées (stale), et quand elles doivent être recalculées. Le package `singleflight` aide à garantir qu'une seule goroutine effectue le travail de rafraîchissement, évitant ainsi une accumulation de mises à jour.

```go
entry := getEntry(key) // {data, freshUntil, staleUntil}
switch {
case time.Now().Before(entry.freshUntil):
    return entry.data
case time.Now().Before(entry.staleUntil):
    go refreshSingleflight(key) // background refresh
    return entry.data
default:
    return refreshSingleflight(key) // must refresh now
}
```

Ici, le code récupère une entrée de cache contenant les données ainsi que deux horodatages marquant les limites de fraîcheur et de péremption. Si l'heure actuelle se situe avant le seuil de fraîcheur, les données sont considérées comme totalement fraîches et renvoyées immédiatement. Si le temps a dépassé le seuil de fraîcheur mais reste dans la fenêtre de péremption, le code renvoie instantanément les données légèrement obsolètes tout en lançant une goroutine en arrière-plan pour les rafraîchir de manière asynchrone, garantissant que la requête suivante recevra des informations mises à jour. Une fois que le temps dépasse même la limite de péremption, les données sont trop anciennes pour être servies, le code bloque donc et effectue un rafraîchissement synchrone avant de renvoyer le résultat.

Cela maintient une latence faible tout en garantissant que le cache se met à jour régulièrement, un équilibre entre fraîcheur et performance.

## Conclusion

La mise en cache n'est pas une tactique unique mais un ensemble de stratégies qui répondent à différents besoins. La mise en cache complète des réponses élimine le travail répétitif au niveau supérieur. La mise en cache des résultats de requêtes protège la base de données d'une charge répétée. La mise en cache HTTP exploite le protocole pour réduire le transfert de données. Stale-While-Revalidate propose un compromis qui favorise la vitesse sans laisser les données périmées trop longtemps.

En pratique, ces approches sont souvent superposées. Une API Go peut utiliser la mémoire locale et Redis pour les réponses, appliquer une mise en cache au niveau des requêtes pour les tables très sollicitées, et définir des ETags pour que les clients évitent les téléchargements inutiles. Avec le bon mélange, vous pouvez réduire la latence de plusieurs ordres de grandeur, gérer beaucoup plus de trafic et économiser à la fois les ressources de calcul et de base de données.