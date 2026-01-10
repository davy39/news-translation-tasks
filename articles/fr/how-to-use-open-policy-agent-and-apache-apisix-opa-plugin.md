---
title: Comment créer une meilleure politique avec Open Policy Agent et le plugin OPA
  d'Apache APISIX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-24T19:28:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-open-policy-agent-and-apache-apisix-opa-plugin
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-357514.jpg
tags:
- name: apache
  slug: apache
- name: 'Back end development '
  slug: back-end-development
- name: backend
  slug: backend
- name: Policy
  slug: policy
seo_title: Comment créer une meilleure politique avec Open Policy Agent et le plugin
  OPA d'Apache APISIX
seo_desc: "By Njoku Samson Ebere\nOne common thing in every organisation is policy.\
  \ Policies define how an organisation operates. \nThey are essential to the long-term\
  \ success of an organisation. They preserve significant knowledge about how to comply\
  \ with matter..."
---

Par Njoku Samson Ebere

Une chose courante dans toute organisation est la [politique](https://www.openpolicyagent.org/docs/latest/philosophy/#policy). Les politiques définissent comment une organisation fonctionne. 

Elles sont essentielles pour le succès à long terme d'une organisation. Elles préservent des connaissances significatives sur la manière de se conformer à des questions telles que les exigences légales, le travail dans des contraintes techniques et l'éviter de répéter des erreurs.   
  
Les logiciels suivent le même schéma en adhérant à des règles qui gouvernent leur comportement. Ces règles (ou politiques) peuvent spécifier les environnements de l'application, les routes réseau autorisées, les versions de dépendances autorisées et quand les micro-services reçoivent des requêtes API. Habituellement, les développeurs les créent manuellement en utilisant des documents comme des feuilles de calcul.   
  
Le problème avec cette méthode est qu'elle devient progressivement volumineuse. Si chaque partie d'une application a sa propre politique, des choses comme l'autorisation seront difficiles à gérer dans toute l'application. Il peut également y avoir une répétition inutile des politiques dans différentes parties de l'application. 

En dehors de cela, la mise à jour de toute politique nécessitera le redéploiement de toute l'application. Heureusement, **Open Policy Agent** (OPA) a trouvé un moyen de résoudre ces problèmes.  
  
Cet article expliquera ce qu'est OPA, comment il fonctionne, ce que le plugin OPA implique et comment l'utiliser.   
  
Commençons !

## Qu'est-ce que OPA ?

[OPA](https://www.openpolicyagent.org/docs/latest/) est un moteur de politique généraliste open-source. Il peut remplacer les modules de fonction de politique intégrés dans les logiciels et aider les utilisateurs à découpler les services du moteur de politique.

OPA fournit un moyen de construire des applications séparées de leurs politiques et pour qu'elles soient réutilisables dans de nombreuses applications.   
  
La méthode de gestion des politiques d'OPA réduit les complexités et donne plus de contrôle au propriétaire de l'application. OPA permet aux utilisateurs de l'intégrer avec d'autres services, tels que les bibliothèques de programmes et les API HTTP.

## Comment fonctionne OPA

OPA sert d'intermédiaire entre les applications et les politiques pour décider de la règle à appliquer lors du traitement d'une requête. L'image ci-dessous décrit son fonctionnement :

![Image](https://paper-attachments.dropboxusercontent.com/s_EFDBAAA4A6A8765E2C2CBACA1FE670A8A1A3C4F3B2852B5E7907B18C06560424_1662070285391_opa-service.svg)

Voici une explication de l'image ci-dessus :

1. Un service (disons qu'il s'agit d'un micro-service d'authentification) reçoit une requête (comme une requête de connexion). Pour que le service décide comment traiter la requête, il doit obtenir la politique guidant l'authentification. Cela nous amène à l'étape suivante.
2. Le service envoie une requête (cela peut être dans n'importe quel format JSON) à OPA demandant la politique à respecter pour traiter la requête reçue.
3. OPA compare maintenant les données et les politiques auxquelles il a accès et prend la bonne décision.
4. Enfin, OPA retourne la décision de politique (cela peut être dans n'importe quel format JSON) atteinte au service.

C'est un résumé de comment OPA fonctionne. Vous pouvez imaginer de nombreux services attachés à OPA et OPA les aidant à décider comment traiter les requêtes ou les événements au lieu que chaque service gère ses propres politiques. Cela fournit un système plus robuste qui est facile à maintenir. 

[Apache APISIX](https://dev.to/ebereplenty/introduction-to-apache-apisix-5b4) a décidé de s'intégrer avec OPA en fournissant le plugin OPA. C'est ce que nous allons discuter maintenant.

## Plugin OPA d'Apache APISIX

Le plugin permet aux utilisateurs d'[Apache APISIX](https://apisix.apache.org/) d'introduire facilement les capacités de politique fournies par OPA lors de l'utilisation d'Apache APISIX. Il permet des fonctionnalités d'authentification et de contrôle d'accès flexibles.

### Comment cela fonctionne

Le plugin OPA d'Apache APISIX suit deux étapes principales pour accomplir sa tâche :

Tout d'abord, APISIX reconstruit toute donnée de requête qu'il reçoit en données JSON acceptables et fait une requête de politique à OPA avec. La requête est généralement appelée une requête de **service APISIX à OPA**. Voir l'exemple suivant :

```

{
    "type": "http",
    "request": {
        "scheme": "http",
        "path": "\/get",
        "headers": {
            "user-agent": "curl\/7.68.0",
            "accept": "*\/*",
            "host": "127.0.0.1:9080"
        },
        "query": {},
        "port": 9080,
        "method": "GET",
        "host": "127.0.0.1"
    },
    "var": {
        "timestamp": 1701234567,
        "server_addr": "127.0.0.1",
        "server_port": "9080",
        "remote_port": "port",
        "remote_addr": "ip address"
    },
    "route": {},
    "service": {},
    "consumer": {}
}
```

Les données JSON ci-dessus indiquent à OPA qu'un utilisateur a fait une requête HTTP en utilisant la méthode GET via `127.0.0.1:9080/get` à l'horodatage `1701234567` (mercredi 29 novembre 2023 05:09:27).  
  
OPA doit maintenant aider Apache APISIX à décider comment traiter la requête.

Ensuite, OPA vérifie les politiques et les données disponibles, les compare et prend la décision au format JSON ci-dessous :

```json
{
    "result": {
        "allow": true,
        "reason": "test",
        "headers": {
            "an": "header"
        },
        "status_code": 401
    }
}
```

La décision de politique ci-dessus est une réponse **du service OPA à APISIX**. Elle indique à APISIX d'accepter la requête en raison de la raison (test) donnée. Lorsque allow est false, Apache APISIX la rejette.  
  
Voici une explication de certaines des clés dans la requête et la réponse ci-dessus :

* `type` indique le type de requête (`HTTP` ou `stream`).
* `request` est utilisé lorsque le `type` est `HTTP` et contient les informations de base de la requête comme l'URL et les en-têtes.
* `var` contient les informations de base sur la connexion demandée (IP, port, détails du serveur et horodatage de la requête).
* `route`, `service` et `consumer` contiennent les mêmes données stockées dans APISIX. Ils nécessitent une configuration pour qu'un utilisateur puisse les voir après une transaction.
* `allow` est requis et indique si la requête est autorisée à passer par APISIX.
* `reason`, `headers` et `status_code` sont optionnels et sont retournés lorsque vous configurez une réponse personnalisée.

### Comment utiliser le plugin

Cette section vous présentera certaines des fonctionnalités du plugin. Vous verrez comment utiliser Docker pour construire des services OPA, créer des politiques, créer des données utilisateurs, créer une route personnalisée, tester des requêtes, et activer et désactiver le plugin.

#### Comment utiliser [docker](https://www.docker.com/) pour construire des services OPA

Utilisez la commande ci-dessous pour lancer l'environnement OPA sur le port `8181`

```
docker run -d --name opa -p 8181:8181 openpolicyagent/opa:0.35.0 run -s
```

Nous utiliserons [CURL](https://curl.se/) pour le reste de cet article. Si vous êtes nouveau ou venez d'autres langages de programmation, copiez les requêtes ou le code de réponse et [collez le code ici](https://curlconverter.com/) pour le convertir dans votre langage préféré.

Nous utiliserons également les drapeaux `-H` et `-d` au lieu de `--header` et `--data-raw` respectivement.

#### Comment créer une politique

La création d'une politique suit le format ci-dessous :

```
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
    -H 'Content-Type: text/plain' \
    -d 'package example

import input.request

default allow = false

allow {
    # La méthode HTTP doit être GET
    request.method == "GET"
}'
```

Le code ci-dessus est le résultat des étapes suivantes :

* Indiquez la route : 127.0.0.1:8181/v1/policies/example1.
* Importez la requête : import input.request.
* Indiquez qu'aucune requête n'est autorisée : default allow = false.
* Spécifiez ce qui est permis :

```

allow {
    # La méthode HTTP doit être GET
    request.method == "GET"
}
```

Le code ci-dessus indique que la seule méthode HTTP acceptable est GET. Chaque ligne dans l'objet allow est implémentée en tant que politiques, à l'exception des lignes qui commencent par un # car ce sont des commentaires.   
  
Vous pouvez ajouter autant de règles que vous le souhaitez en fonction des politiques que vous avez en tête. Par exemple, le code ci-dessous contient cinq règles qui doivent être respectées :

```
# Créer une politique
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
    -H 'Content-Type: text/plain' \
    -d 'package example

import input.request
import data.users

default allow = false

allow {
    # a le nom test-header avec la valeur only-for-test request header
    request.headers["test-header"] == "only-for-test"

    # La méthode de requête est GET
    request.method == "GET"

    # Le chemin de la requête commence par /get
    startswith(request.path, "/get")

    # Le paramètre GET test existe et n'est pas égal à abcd
    request.query["test"] != "abcd"

    # Le paramètre GET user existe
    request.query["user"]
}'
```

Avec la configuration que nous avons faite jusqu'à présent, tout fonctionnera bien. Mais que se passe-t-il lorsque nos utilisateurs se trompent et qu'une erreur qu'ils ne comprennent pas est retournée ? Ils deviendront frustrés et auront une mauvaise expérience utilisateur. Nous pouvons éviter cela en ajoutant une **réponse personnalisée.**  
  
Une réponse personnalisée fournit des détails supplémentaires (corps, en-tête et code d'état) sur le résultat d'une transaction. Notre requête devient maintenant :

```

# Créer une politique
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
    -H 'Content-Type: text/plain' \
    -d 'package example

import input.request
import data.users

default allow = false

allow {
    # a le nom test-header avec la valeur only-for-test request header
    request.headers["test-header"] == "only-for-test"
    # La méthode de requête est GET
    request.method == "GET"
    # Le chemin de la requête commence par /get
    startswith(request.path, "/get")
    # Le paramètre GET test existe et n'est pas égal à abcd
    request.query["test"] != "abcd"
    # Le paramètre GET user existe
    request.query["user"]
}

# corps de réponse personnalisé (Accepte une chaîne ou un objet, l'objet répondra au format JSON)
reason = users[request.query["user"]].reason {
    not allow
    request.query["user"]
}

# en-tête de réponse personnalisé (Les données de l'objet peuvent être écrites de cette manière)
headers = users[request.query["user"]].headers {
    not allow
    request.query["user"]
}

# code d'état de réponse personnalisé
status_code = users[request.query["user"]].status_code {
    not allow
    request.query["user"]
}'
```

Lorsque l'utilisateur obtient une erreur, il devient plus facile de la déboguer car l'erreur vient avec une `reason`, des détails `headers` et un `status_code`.

#### Comment créer les données des utilisateurs

Les données des utilisateurs sont un objet d'objets. Chaque donnée utilisateur est un objet de détails personnalisés (corps, en-tête et code d'état) qui aident à l'autorisation des utilisateurs. 

Le code ci-dessous est un exemple de données utilisateurs contenant quatre (4) utilisateurs avec des détails différents :

```
# Créer des données utilisateurs de test
curl -X PUT '127.0.0.1:8181/v1/data/users' \
    -H 'Content-Type: text/plain' \
    -d '{

    "alice": {
        "headers": {
            "Location": "http://example.com/auth"
        },
        "status_code": 302
    },

    "bob": {
        "headers": {
            "test": "abcd",
            "abce": "test"
        }
    },

    "carla": {
        "reason": "Give you a string reason"
    },

    "dylon": {
        "headers": {
            "Content-Type": "application/json"
        },
        "reason": {
            "code": 40001,
            "desc": "Give you a object reason"
        }
    }
}'
```

Remarquez que chaque détail personnalisé de l'utilisateur est facultatif et peut différer pour chaque utilisateur.

#### Comment créer une route personnalisée et activer le plugin

La flexibilité du plugin OPA d'APISIX permet aux utilisateurs de personnaliser leur route comme dans le code ci-dessous :

```
curl -X PUT 'http://127.0.0.1:9080/apisix/admin/routes/r1' \
    -H 'X-API-KEY: <api-key>' \
    -H 'Content-Type: application/json' \
    -d '{
    "uri": "/*",
    "methods": [
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "plugins": {},
    "upstream": {
        "nodes": {
            "httpbin.org:80": 1
        },
        "type": "roundrobin"
    }
}'
```

Pour que cela fonctionne, le plugin doit être activé. Entrez la configuration nécessaire dans l'objet `plugins` pour l'activer. Nous avons donc :

```

curl -X PUT 'http://127.0.0.1:9080/apisix/admin/routes/r1' \
    -H 'X-API-KEY: <api-key>' \
    -H 'Content-Type: application/json' \
    -d '{
    "uri": "/*",
    "methods": [
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "plugins": {
        "opa": {
            "host": "http://127.0.0.1:8181",
            "policy": "example1"
        }
    },
    "upstream": {
        "nodes": {
            "httpbin.org:80": 1
        },
        "type": "roundrobin"
    }
}'
```

Maintenant que le plugin est activé, vous pouvez utiliser votre route comme bon vous semble.

#### Comment tester les requêtes

Nous avons pu créer des politiques, des données utilisateurs et des routes personnalisées, et activer le plugin OPA d'Apache APISIX jusqu'à présent. Testons maintenant ces configurations et voyons la réponse que nous obtenons pour différents scénarios :

Voici un test pour lorsqu'une requête est autorisée :

Requête :

```

curl -XGET '127.0.0.1:9080/get?test=none&user=dylon' \
    --header 'test-header: only-for-test'
```

  
Réponse :

```
{
    "args": {
        "test": "abcd1",
        "user": "dylon"
    },
    "headers": {
        "Test-Header": "only-for-test",
        "with": "more"
    },
    "origin": "127.0.0.1",
    "url": "http://127.0.0.1/get?test=abcd1&user=dylon"
}
```

Voici un test pour lorsqu'une requête est rejetée et que le code d'état et les en-têtes de réponse sont réécrits :

Requête :

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=alice' \
    --header 'test-header: only-for-test'
```

Réponse :

```

HTTP/1.1 302 Moved Temporarily
Date: Mon, 20 Dec 2021 09:37:35 GMT
Content-Type: text/html
Content-Length: 142
Connection: keep-alive
Location: http://example.com/auth
Server: APISIX/2.11.0
```

Voici un test pour lorsqu'une requête est rejetée et qu'un en-tête de réponse personnalisé est retourné :

Requête :

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=bob' \
    --header 'test-header: only-for-test'

```

Réponse :

```

HTTP/1.1 403 Forbidden
Date: Mon, 20 Dec 2021 09:38:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 150
Connection: keep-alive
abce: test
test: abcd
Server: APISIX/2.11.0

```

Voici un test pour lorsqu'une requête est rejetée et qu'une réponse personnalisée (chaîne) est retournée :

Requête :

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=carla' \
    --header 'test-header: only-for-test'
```

Réponse :

```

HTTP/1.1 403 Forbidden
Date: Mon, 20 Dec 2021 09:38:58 GMT
Content-Type: text/plain; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Server: APISIX/2.11.0

Give you a string of reason
```

Et voici un test pour lorsqu'une requête est rejetée et qu'une réponse personnalisée (JSON) est retournée :

Requête :

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=dylon' \
    --header 'test-header: only-for-test'
```

Réponse :

```

HTTP/1.1 403 Forbidden
Date: Mon, 20 Dec 2021 09:42:12 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
Server: APISIX/2.11.0

{"code":40001,"desc":"Give you a object reason"}
```

#### Comment désactiver le plugin

Pour désactiver le plugin OPA d'APISIX, supprimez toutes les configurations que nous avons ajoutées lors de la configuration d'une route personnalisée et de l'activation du plugin. Nous avons maintenant :

```

curl -X PUT 'http://127.0.0.1:9080/apisix/admin/routes/r1' \
    -H 'X-API-KEY: <api-key>' \
    -H 'Content-Type: application/json' \
    -d '{
    "uri": "/*",
    "methods": [
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "plugins": {},
    "upstream": {
        "nodes": {
            "httpbin.org:80": 1
        },
        "type": "roundrobin"
    }
}'
```

L'objet `plugins` étant vide indique que le plugin ne peut pas fonctionner. C'est aussi simple grâce à la nature dynamique d'Apache APISIX.

## **Conclusion**

Cet article visait à vous présenter le plugin OPA d'Apache APISIX et à vous guider à travers certaines de ses fonctionnalités. 

Nous avons commencé par examiner ce qu'est OPA et pourquoi APISIX l'a adopté en utilisant un plugin. Ensuite, nous avons discuté de comment le plugin fonctionne et comment nous pouvons l'utiliser.  
  
Apache APISIX dispose actuellement de plus de dix plugins liés à l'authentification et à l'autorisation qui prennent en charge l'interface avec les services d'authentification/autorisation principaux de l'industrie.  

Si vous devez interfacer avec d'autres autorités d'authentification, vous pouvez visiter [Apache APISIX's GitHub](https://github.com/apache/apisix/issues) et laisser vos suggestions via un problème ou vous abonner à la [liste de diffusion d'Apache APISIX](https://apisix.apache.org/zh/docs/general/subscribe-guide) pour exprimer vos idées.  
  
J'espère que cet article vous aide à comprendre comment utiliser OPA dans Apache APISIX afin que vous puissiez commencer à l'adopter vous-même. Je vous encourage également à prendre le temps de visiter la [documentation du plugin OPA d'Apache APISIX](https://apisix.apache.org/docs/apisix/plugins/opa/) pour voir d'autres cas d'utilisation du plugin. Plus vous pratiquez avec, mieux vous devenez à l'utiliser.  
  
Bonne création de politiques !