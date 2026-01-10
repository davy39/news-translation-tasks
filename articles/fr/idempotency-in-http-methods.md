---
title: Idempotence dans les méthodes HTTP – Expliquée avec des exemples CRUD
subtitle: ''
author: Yemi Ojedapo
co_authors: []
series: null
date: '2023-12-22T21:19:43.000Z'
originalURL: https://freecodecamp.org/news/idempotency-in-http-methods
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/pexels-robert-lens-10382808.jpg
tags:
- name: http
  slug: http
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Idempotence dans les méthodes HTTP – Expliquée avec des exemples CRUD
seo_desc: "Idempotence refers to a program's ability to maintain a particular result\
  \ even after repeated actions. \nFor example, let's say you have a button that only\
  \ opens a door when pressed. This button does not have the ability to close the\
  \ door, so it stays..."
---

L'idempotence fait référence à la capacité d'un programme à maintenir un résultat particulier même après des actions répétées. 

Par exemple, imaginons que vous avez un bouton qui n'ouvre une porte que lorsqu'il est pressé. Ce bouton n'a pas la capacité de fermer la porte, donc elle reste ouverte même lorsqu'il est pressé à plusieurs reprises. Il reste simplement dans l'état dans lequel il a été changé par le premier appui.

Cette même logique s'applique aux méthodes HTTP qui sont idempotentes. Opérer sur des méthodes HTTP idempotentes à plusieurs reprises n'aura aucun effet supplémentaire au-delà de l'exécution initiale. 

Comprendre l'idempotence est important pour maintenir la cohérence des méthodes HTTP et la conception des API. L'idempotence a un impact significatif sur la conception des API, car elle influence la manière dont les points de terminaison des API doivent se comporter lors du traitement des requêtes des clients. 

Dans ce tutoriel, j'expliquerai le concept d'idempotence et le rôle qu'elle joue dans la construction d'API robustes et fonctionnelles. Vous apprendrez également ce que sont les méthodes sûres, comment elles se rapportent à l'idempotence, et comment implémenter l'idempotence dans les méthodes non idempotentes. 

## Prérequis

Avant de comprendre et d'implémenter l'idempotence dans la conception des API, il est essentiel d'avoir une solide fondation dans les domaines suivants :

* Principes RESTful
* Fondamentaux des méthodes HTTP
* Développement d'API 
* Codes de statut HTTP
* Bases du développement Web.

## Exemple d'idempotence  

Commençons par un exemple d'idempotence en action. Nous allons créer une fonction qui utilise la méthode DELETE pour supprimer des données d'une page web :

```python

from flask import Flask, jsonify, abort

app = Flask(__name__)

web_page_data = [
   {"id": 1, "content": "Données de la ligne 1"},
   {"id": 2, "content": "Données de la ligne 2"},
   # Ajoutez plus de lignes si nécessaire
]

@app.route('/delete_row/<int:row_id>', methods=['DELETE'])
def delete_row(row_id):
   # Trouver la ligne à supprimer
   row_to_delete = next((row for row in web_page_data if row["id"] == row_id), None)
   
   if row_to_delete:
       # Simuler la suppression
       web_page_data.remove(row_to_delete)
       return jsonify({"message": f"Ligne {row_id} supprimée avec succès."}), 200
   else:
       abort(404, description=f"Ligne {row_id} non trouvée.")

if __name__ == '__main__':
   app.run(debug=True)

```

Cette fonction est censée supprimer les lignes choisies par l'utilisateur. Grâce à la nature idempotente de la méthode DELETE, les données seront supprimées une fois, même si la fonction est appelée à plusieurs reprises. Mais les appels suivants retourneront une erreur 404 puisque les données auront déjà été supprimées par le premier appel.  

Examinons un autre exemple avec la méthode GET. La méthode GET est utilisée pour récupérer des données d'une ressource. Créons une fonction qui utilise la méthode GET pour récupérer un nom d'utilisateur :

```python
import requests

def get_username():
    url = 'https://api.example.com/get_username'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['username']
        else:
            return None
    except requests.RequestException as e:
        print(f"Erreur survenue : {e}")
        return None

# Utilisation
username = get_username()
if username:
    print(f"Le nom d'utilisateur est : {username}")
else:
    print("Échec de la récupération du nom d'utilisateur.")

```

Dans cet exemple, nous définissons la fonction `get_username()`, qui envoie une requête GET au point de terminaison de l'API pour récupérer le nom d'utilisateur. Si la requête aboutit, nous extrayons le nom d'utilisateur de la réponse JSON et le retournons. Mais si une erreur se produit pendant la requête, nous la gérons et retournons `None`.

La nature idempotente de la méthode GET garantit que même si vous appelez `get_username()` plusieurs fois, le même nom d'utilisateur sera récupéré de l'API à chaque fois. Le résultat sera toujours le même, à savoir récupérer le nom d'utilisateur de la ressource.

### Méthodes HTTP idempotentes vs non idempotentes :

Les méthodes HTTP jouent des rôles cruciaux dans la détermination de la manière dont les données sont récupérées, modifiées ou créées lors de l'interaction avec les API. Et l'idempotence est l'un des concepts importants qui influencent la cohérence et la fiabilité des données dans les méthodes utilisées.

Voici une répartition des différentes méthodes en fonction de leur idempotence.

#### Méthodes idempotentes :

* GET
* HEAD
* PUT
* DELETE
* OPTIONS
* TRACE

#### Méthodes non idempotentes :

* POST
* PATCH
* CONNECT

## Méthodes sûres

Dans notre exemple précédent, nous avons utilisé la méthode GET pour récupérer un nom d'utilisateur et cela n'a eu aucun effet secondaire sur le serveur. C'est parce qu'il s'agit d'une méthode sûre. 

Une méthode sûre est un type de méthode qui ne modifie pas l'état du serveur ou la ressource à laquelle on accède. En d'autres termes, elles effectuent des opérations en lecture seule utilisées pour récupérer des données ou pour la représentation des ressources.

Lorsque vous faites une requête en utilisant une méthode sûre, le serveur n'effectue aucune opération qui modifie l'état de la ressource. Comme dans notre exemple précédent, nous avons récupéré le nom d'utilisateur de la page web qui est la ressource sans changer quoi que ce soit sur le serveur. 

Toutes les méthodes sûres sont automatiquement idempotentes, mais toutes les méthodes idempotentes ne sont pas sûres. C'est parce que bien que les méthodes idempotentes produisent des résultats cohérents lorsqu'elles sont appelées à plusieurs reprises, certaines d'entre elles peuvent encore modifier l'état du serveur ou la ressource à laquelle on accède.

Comme dans notre premier exemple, la méthode DELETE est idempotente, car supprimer une ressource plusieurs fois aura le même effet. Mais elle n'est pas sûre, car elle change l'état du serveur en supprimant la ressource.

Voici une classification des méthodes HTTP en fonction de leur statut de sécurité :

#### Méthodes sûres :

* GET
* OPTIONS
* HEAD

#### Méthodes non sûres :

* DELETE
* POST
* PUT
* PATCH

### Pourquoi POST n'est-il pas idempotent ?

POST est une méthode HTTP qui envoie des informations à un serveur. Lorsque vous faites une requête POST, vous soumettez généralement des données pour créer une nouvelle ressource ou déclencher une action côté serveur. Par conséquent, faire la même requête plusieurs fois peut entraîner des résultats différents et des effets secondaires sur le serveur. Cela peut conduire à des données dupliquées, au démarrage des ressources du serveur et à une réduction des performances en raison de l'action répétée.

Contrairement aux méthodes idempotentes comme GET, PUT et DELETE, qui ont des résultats cohérents indépendamment de la répétition, les requêtes POST peuvent provoquer des changements dans l'état du serveur à chaque invocation. 

Les requêtes POST créent souvent de nouvelles ressources sur le serveur. Répéter la même requête POST générera plusieurs ressources identiques, ce qui pourrait entraîner une duplication.

Cela est similaire à DELETE qui est une méthode idempotente mais pas une méthode sûre. Supprimer la dernière entrée dans une collection en utilisant une seule requête DELETE serait considéré comme idempotent. Mais si un développeur crée une fonction qui supprime la dernière entrée, cela déclencherait DELETE plusieurs fois. Les appels DELETE suivants auraient des effets différents, car chacun supprime une entrée unique. Cela serait considéré comme non idempotent.

## Comment atteindre l'idempotence avec des méthodes non idempotentes

L'idempotence n'est pas seulement une propriété inhérente à certaines méthodes – elle peut également être implémentée comme une fonctionnalité d'une méthode non idempotente.  

Voici quelques techniques pour atteindre l'idempotence même avec des méthodes non idempotentes.

### Identifiants uniques

Ajouter des identifiants uniques à chaque requête est l'une des techniques les plus courantes utilisées pour implémenter l'idempotence. Cela fonctionne en suivant si l'opération a déjà été effectuée ou non. Si c'est un duplicata (une requête répétée), le serveur sait qu'il a déjà traité cette requête et l'ignore simplement, garantissant qu'aucun effet secondaire ne se produise. 

Voici un exemple de son fonctionnement :

```python
from uuid import uuid4
 
def process_order(unique_id, order_data):
    if Order.objects.filter(unique_id=unique_id).exists():
        return HttpResponse(status=409)  # Conflit
    order = Order.objects.create(unique_id=unique_id, **order_data)
    return HttpResponse(status=201, content_type="application/json")

# Exemple d'utilisation
post_data = {"products": [...]}
headers = {"X-Unique-ID": str(uuid4())}
requests.post("https://api.example.com/orders", data=post_data, headers=headers)

```

Dans cet extrait de code, nous définissons une fonction appelée `process_order` qui crée des commandes dans une API, en utilisant des identifiants uniques pour implémenter l'idempotence. 

Voici une explication du code :

#### Importation du générateur d'identifiants uniques :

`from uuid import uuid4` : L'extrait de code commence par importer la fonction `uuid4` du module `uuid`. Cette fonction génère des identifiants uniques, qui sont utilisés pour atteindre l'idempotence dans ce code.

#### Définition de la fonction `process_order` :

`def process_order(unique_id, order_data)` : Cette ligne définit une fonction nommée process_order qui prend deux arguments :

* `unique_id` : Il s'agit d'une chaîne représentant un identifiant unique pour la requête. Cela garantit qu'aucune commande en double n'est créée avec le même identifiant.
* `order_data` : Il s'agit d'un dictionnaire contenant les données réelles de la commande, comme les informations sur les produits et les détails du client.

#### Vérification des commandes existantes :

`if Order.objects.filter(unique_id=unique_id).exists()` : Cette ligne vérifie si une commande avec le même unique_id existe déjà dans la base de données.

`Order.objects.filter(unique_id=unique_id).exists()` interroge le modèle Order pour les commandes avec le unique_id correspondant et vérifie si des commandes ont été trouvées dans le résultat de la requête. Si une commande est trouvée, cela signifie que la même requête a déjà été traitée.

#### Gestion des commandes existantes :

`return HttpResponse(status=409)` : Si une commande avec le même unique_id existe déjà, la fonction retourne immédiatement une réponse HTTP avec le code de statut 409 indiquant un conflit. Cela empêche la création de commandes en double.

#### Création d'une nouvelle commande (si unique) :

`order = Order.objects.create(unique_id=unique_id, **order_data )` : Cette ligne ne s'exécute que si aucune commande existante n'est trouvée.

`Order.objects.create` : crée un nouvel objet dans le modèle Order.

`unique_id=unique_id` : définit l'attribut unique_id de la nouvelle commande sur le unique_id fourni.

`order_data` : étale le dictionnaire order_data en tant qu'arguments de mot-clé au constructeur du modèle de commande, définissant d'autres attributs pertinents comme les produits et les informations du client.

#### Envoi d'une réponse de succès :

`return HttpResponse(status=201, content_type="application/json")` : Si la création de la commande est réussie, la fonction retournera une réponse HTTP avec le code de statut 201 qui montre une création réussie. Elle spécifie également le type de contenu de la réponse comme JSON, en supposant que les données de la commande pourraient être retournées au format JSON.

`post_data = {"products": [...]}` : un exemple de requête, définit un dictionnaire contenant les données réelles de la commande, comme une liste de produits.

`headers = {"X-Unique-ID": str(uuid4())}` : Cette ligne crée un dictionnaire contenant un en-tête personnalisé nommé X-Unique-ID. Il génère une chaîne d'identifiant unique en utilisant uuid4() et l'ajoute à l'en-tête.

`requests.post("https://api.example.com/orders", data=post_data, headers=headers` : Cette ligne envoie une requête POST au point de terminaison de l'API `https://api.example.com/orders` avec les `post_data` et les en-têtes fournis.

#### Comment cela implémente-t-il l'idempotence ?

Il le fait en utilisant un identifiant unique (`unique_id`) pour chaque commande. 

Il vérifie si une commande avec le même identifiant existe déjà dans la base de données. Si c'est vrai, il retourne un statut de conflit 409. Sinon, il crée une nouvelle commande et répond avec un statut de création 201. L'identifiant unique empêche les commandes en double, rendant le système idempotent.

### Autorisation basée sur les jetons

L'autorisation basée sur les jetons est une forme d'autorisation qui attribue des jetons temporaires pour chaque action non idempotente. Une fois l'action terminée, le jeton est invalidé. Si la même requête arrive à nouveau avec le même jeton, le serveur la reconnaît comme invalide et refuse la requête, empêchant ainsi les actions en double.

```javascript
// Générer un jeton unique pour cette action
const token = generateToken();

fetch("https://api.example.com/create-user", {
    method: "POST",
    body: JSON.stringify({ username, password }),
    headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
    },
})
    .then(response => {
        // Gérer la réponse réussie
        if (response.ok) {
            // Faire quelque chose avec la réponse réussie
        } else {
            // Gérer la réponse non réussie
        }
    })
    .catch(error => {
        // Gérer l'erreur
        console.error("Erreur survenue :", error);
    })
    .finally(() => {
        // Invalider le jeton après une action réussie ou en cas d'erreur
        invalidateToken(token);
    });

// Implémentation simple pour générer un jeton
function generateToken() {
    return Math.random().toString(36).substr(2);
}

// Implémentation simple pour invalider un jeton
function invalidateToken(token) {
    // Ajoutez votre logique pour invalider le jeton, par exemple, le supprimer du stockage
}

```

Voici une explication du code :

#### Génération d'un jeton unique :

`const token = generateToken()` : Cette ligne appelle une fonction nommée `generateToken()` (qui est supposée être définie ailleurs) qui génère une chaîne de jeton unique. Ce jeton sera utilisé pour l'autorisation et l'idempotence.

#### Envoi de la requête `POST` :

`fetch("https://api.example.com/create-user", { ... })` : Cette ligne utilise l'API fetch pour envoyer une requête POST au point de terminaison de l'API `https://api.example.com/create-user`. 

`method: "POST"` : Cela spécifie la méthode HTTP comme POST, indiquant l'intention de créer un nouvel utilisateur.

`body: JSON.stringify({ username, password })` : Cela définit le corps de la requête avec les détails de l'utilisateur comme le nom d'utilisateur et le mot de passe. Les données sont converties au format JSON avant l'envoi.

`headers: { Authorization:Bearer ${token}}` : Cela définit l'en-tête Authorization dans la requête. La valeur de l'en-tête inclut le jeton généré précédé de "Bearer ".

#### Gestion de la réponse :

`.then(response => { ... })` : Ce bloc définit le code à exécuter si la requête aboutit. Vous traiterez des choses comme le stockage des informations de l'utilisateur ou la redirection de l'utilisateur après la création réussie de l'utilisateur.

`.catch(error => { ... }):` Ce bloc définit le code à exécuter si la requête rencontre une erreur. Vous traiterez ici les messages d'erreur ou les scénarios d'erreur spécifiques.

#### Invalidation du jeton :

`invalidateToken(token)` : Cette ligne appelle une fonction nommée `invalidateToken(token)` (qui est supposée être définie ailleurs) qui marquera probablement le jeton utilisé comme invalide. Cela garantit que le même jeton ne peut pas être utilisé pour des requêtes ultérieures, ajoutant à la garantie d'idempotence.

#### Comment cela implémente-t-il l'idempotence ?

Cet extrait de code utilise l'autorisation basée sur les jetons pour implémenter l'idempotence dans une requête POST afin de créer un utilisateur sur une API. Si une requête de création d'utilisateur est accidentellement envoyée plusieurs fois, un nouveau jeton unique est généré à chaque fois et utilisé dans l'en-tête Authorization.

Le serveur de l'API peut reconnaître et vérifier le jeton unique, et puisque l'action de création d'utilisateur a déjà été effectuée (en supposant qu'elle est réussie la première fois), il ne créera pas d'utilisateurs en double en raison de requêtes identiques ultérieures.

### En-tête ETag :

Un en-tête ETag (Entity Tag) est un en-tête HTTP utilisé pour la validation du cache web et les requêtes conditionnelles. Il est principalement utilisé pour les requêtes PUT, qui ne mettent à jour les ressources que si elles n'ont pas changé depuis la dernière vérification.

Lorsque vous souhaitez mettre à jour une ressource, le serveur vous envoie son ETag qui est ensuite inclus dans votre requête PUT avec les données mises à jour. Si l'ETag n'a pas changé (ce qui signifie que la ressource reste la même), le serveur accepte la mise à jour. Mais si l'ETag a changé, le serveur rejette la mise à jour, l'empêchant ainsi d'écraser les modifications de quelqu'un d'autre.

```python
def update_article(article_id, content):
    # Obtenir l'article existant et son ETag
    article = Article.objects.get(pk=article_id)
    etag = article.etag
    
    # Vérifier si l'ETag correspond à l'en-tête de la requête
    if request.headers.get("If-Match") != etag:
        return HttpResponse(status=409)  # Conflit
    
    # Mettre à jour le contenu de l'article et générer un nouvel ETag
    article.content = content
    article.save()
    new_etag = article.etag
    
    # Retourner la réponse de succès avec l'ETag mis à jour
    return HttpResponse(status=200, content_type="text/plain", content=new_etag)

```

Dans cet extrait de code, nous définissons une fonction appelée `update_article` qui vous permet de mettre à jour le contenu d'un article existant en fonction de son ID et du nouveau contenu. Elle implémente l'idempotence en utilisant la technique de l'en-tête ETag.

Voici une explication étape par étape de son fonctionnement ;

#### Obtention de l'article existant et de son ETag :

`article = Article.objects.get(pk=article_id):` Cette ligne récupère l'article avec l'article_id fourni de la base de données en utilisant le modèle Article.

`etag = article.etag:` Cette ligne extrait la valeur ETag de l'objet article récupéré. L'ETag sert d'identifiant unique pour l'état actuel de l'article.

#### Vérification de la correspondance :

`if request.headers.get("If-Match") != etag:` Cette ligne vérifie si l'en-tête ETag fourni dans la requête correspond à l'ETag de l'article récupéré.

`return HttpResponse(status=409)`: Si l'ETag ne correspond pas, cela indique que l'article a peut-être été mis à jour par une autre requête depuis que le client a récupéré ses informations. La fonction retourne une réponse 409 Conflit, ce qui empêche la corruption accidentelle des données.

#### Mise à jour du contenu de l'article et génération d'un nouvel ETag :

`article.content = content:` Cette ligne met à jour le contenu de l'article avec le nouveau contenu reçu dans la requête.

`article.save():` Cette ligne sauvegarde l'article mis à jour dans la base de données.

`new_etag = article.etag:` Cette ligne récupère le nouvel ETag généré pour l'article mis à jour après l'avoir sauvegardé.

#### Retour de la réponse de succès avec le nouvel ETag :

`return HttpResponse(status=200, content_type="text/plain", content=new_etag)`: retourne une réponse 200 OK réussie, incluant le type de contenu ("text/plain") et le nouvel ETag de l'article dans le corps de la réponse.

#### Comment cela implémente-t-il l'idempotence ?

Ce code garantit que si la même requête de mise à jour est envoyée plusieurs fois avec le même ETag, la mise à jour ne sera effectuée qu'une seule fois, empêchant ainsi les mises à jour en double et maintenant la cohérence des données. Le nouvel ETag est ensuite fourni dans la réponse pour aider le client à suivre l'état de l'article pour les interactions futures.

## Conclusion

Dans ce tutoriel, nous avons mis en évidence la différence entre les méthodes sûres comme GET, qui récupèrent des données sans effets secondaires, et les méthodes non idempotentes comme POST, qui peuvent avoir des résultats différents à chaque répétition. 

Nous avons également exploré des techniques que vous pouvez appliquer pour atteindre l'idempotence dans les méthodes non idempotentes, en soulignant l'importance de concevoir des API qui privilégient la cohérence et la fiabilité.