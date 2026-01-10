---
title: Comment créer une expérience de recherche pilotée par l'IA avec Meilisearch
subtitle: Découvrez comment la recherche propulsée par l'IA avec Meilisearch offre
  des résultats rapides, intuitifs et hautement pertinents.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-26T22:41:43.725Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ai-driven-search-experience-using-meilisearch
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764196860843/a3dc07e2-6a90-4d4c-8b21-0f833ff41ac2.png
tags:
- name: AI
  slug: ai
- name: search
  slug: search
- name: Python
  slug: python
seo_title: Comment créer une expérience de recherche pilotée par l'IA avec Meilisearch
seo_desc: "Search is one of the most important features in modern applications. Users\
  \ expect instant answers, useful suggestions, and results that match their intent\
  \ even when they make spelling mistakes. \nMost traditional search systems struggle\
  \ to deliver thi..."
---


La recherche est l'une des fonctionnalités les plus importantes des applications modernes. Les utilisateurs attendent des réponses instantanées, des suggestions utiles et des résultats qui correspondent à leur intention, même en cas de fautes de frappe.

La plupart des systèmes de recherche traditionnels peinent à offrir cette expérience sans une infrastructure complexe et lourde.

[Meilisearch](https://github.com/meilisearch/meilisearch) est un moteur de recherche open-source qui change la donne en proposant un moteur rapide et convivial pour les développeurs, facile à configurer et à étendre.

En combinant Meilisearch avec des modèles d'IA pour la compréhension du langage naturel et la [pertinence sémantique](https://www.turingtalks.ai/p/how-to-perform-sentence-similarity-check-using-sentence-transformers), vous pouvez créer une expérience de recherche puissante et intuitive, à la fois moderne et intelligente.

Cet article explique comment fonctionne Meilisearch, comment le configurer et comment intégrer des modèles d'IA pour offrir une meilleure pertinence et un meilleur classement. Vous verrez également comment fonctionnent la recherche hybride et les embeddings sémantiques, ainsi que comment déployer Meilisearch dans le cloud avec Sevalla.

## Ce que nous allons aborder

* [Comprendre Meilisearch](#heading-comprendre-meilisearch)
    
* [Configurer Meilisearch](#heading-configurer-meilisearch)
    
* [Utiliser la recherche hybride et l'IA ensemble](#heading-utiliser-la-recherche-hybride-et-lia-ensemble)
    
* [Utiliser l'IA pour réécrire les requêtes](#heading-utiliser-lia-pour-reecrire-les-requetes)
    
* [Déployer Meilisearch dans le cloud avec Sevalla](#heading-deployer-meilisearch-dans-le-cloud-avec-sevalla)
    
* [Conclusion](#heading-conclusion)
    

## Comprendre Meilisearch

Meilisearch est un moteur de recherche ultra-rapide qui s'intègre facilement dans n'importe quelle application.

Il est construit en Rust et conçu pour fournir des résultats en moins de cinquante millisecondes. Il prend en charge la recherche sémantique, la recherche hybride, la tolérance aux fautes de frappe, le tri, la recherche géographique (geosearch) et de nombreuses langues différentes.

Meilisearch propose également une API REST propre et une large gamme de SDK qui facilitent l'intégration avec JavaScript, Python, Go, PHP, Ruby, Rust et divers autres langages.

Vous pouvez essayer Meilisearch en explorant les [démos officielles](https://saas.meilisearch.com/deals). Ces démos montrent que Meilisearch ne se limite pas à un cas d'utilisation spécifique mais peut s'adapter à de nombreux types de flux de travail.

Meilisearch est disponible en deux éditions. La Community Edition est entièrement open source sous licence MIT et peut être utilisée librement, même pour des produits commerciaux.

L'Enterprise Edition introduit des fonctionnalités telles que le [sharding](https://aws.amazon.com/what-is/database-sharding/) et est régie par une licence commerciale. Vous pouvez déployer Meilisearch vous-même ou choisir Meilisearch Cloud, qui gère l'hébergement, les mises à jour, la surveillance et les analyses sans nécessiter de maintenance de serveur.

## Configurer Meilisearch

Démarrer Meilisearch est simple. Vous pouvez télécharger le binaire et l'exécuter directement ou le lancer via Docker. L'utilisation de Docker est le moyen le plus rapide de le tester sur votre machine.

```python
docker run -it --rm -p 7700:7700 getmeili/meilisearch:latest
```

Une fois le serveur lancé, vous pouvez communiquer avec lui via HTTP. Le cas d'utilisation le plus simple consiste à indexer des documents dans un index et à les interroger. Voici un exemple en Python :

```python
import requests

docs = [
    {"id": 1, "title": "AI in Finance", "text": "How AI is changing banks"},
    {"id": 2, "title": "AI in Law", "text": "How AI helps legal teams"},
]
requests.put(
    "http://localhost:7700/indexes/articles/documents",
    json=docs
)
```

La recherche est tout aussi simple.

```python
import requests

query = "ai banks"
res = requests.post(
    "http://localhost:7700/indexes/articles/search",
    json={"q": query}
)
print(res.json())
```

Le moteur renvoie des résultats en quelques millisecondes. La tolérance aux fautes de frappe, la proximité des mots et le classement par pertinence fonctionnent nativement.

Meilisearch gère automatiquement les synonymes si vous les configurez et permet des règles de tri personnalisées pour des attributs tels que le prix ou la date. Il prend également en charge le facettage, les filtres et la recherche géographique, ce qui le rend adapté au e-commerce, aux applications de voyage, aux annonces immobilières et aux tableaux de bord riches en données.

## Utiliser la recherche hybride et l'IA ensemble

La recherche hybride combine la recherche plein texte (full-text) avec la recherche vectorielle sémantique.

Meilisearch prend en charge la recherche sémantique via des champs vectoriels et permet de combiner les deux approches. Cela vous aide à servir les utilisateurs qui saisissent des requêtes vagues ou des questions en langage naturel.

Le modèle d'IA fournit des [embeddings](https://www.ibm.com/think/topics/embedding) qui capturent le sens, tandis que Meilisearch gère la récupération rapide et le classement.

Pour ajouter la recherche sémantique, vous générez d'abord des embeddings pour vos documents à l'aide d'un modèle d'IA. Voici un exemple simple utilisant les embeddings d'OpenAI :

```python
from openai import OpenAI
import requests

client = OpenAI()
def embed(text):
    out = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return out.data[0].embedding
doc = {
    "id": 3,
    "title": "AI in Insurance",
    "text": "How AI powers underwriting",
    "vector": embed("How AI powers underwriting")
}
requests.put(
    "http://localhost:7700/indexes/articles/documents",
    json=[doc]
)
```

Lorsque l'utilisateur effectue une recherche, vous générez l'embedding de la requête et calculez la similitude. Vous pouvez mélanger cela avec les résultats de recherche par mots-clés renvoyés par Meilisearch. Le classement combiné crée une meilleure expérience que l'une ou l'autre approche seule.

## Utiliser l'IA pour réécrire les requêtes

Les utilisateurs saisissent souvent des requêtes incomplètes ou non structurées. Ils peuvent taper « Comment l'IA aide-t-elle les banques ? » au lieu de mots-clés.

Vous pouvez utiliser un modèle d'IA pour réécrire cela en quelque chose de plus adapté à la recherche. La requête réécrite produit de meilleurs résultats dans Meilisearch tout en respectant l'intention originale de l'utilisateur.

```python
from openai import OpenAI
import requests

client = OpenAI()
def rewrite_query(user_query):
    prompt = f"Rewrite this for search: {user_query}"
    out = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return out.choices[0].message.content
user_query = "how does ai help banks"
rewritten = rewrite_query(user_query)
res = requests.post(
    "http://localhost:7700/indexes/articles/search",
    json={"q": rewritten}
)
print(res.json())
```

Ce modèle améliore la précision des recherches basées sur des questions pour les blogs, les plateformes de documentation et les bases de connaissances. Vous pouvez également utiliser le modèle pour normaliser les requêtes, supprimer le texte ambigu, étendre les synonymes et corriger les fautes d'orthographe avant qu'elles n'atteignent Meilisearch.

## Déployer Meilisearch dans le cloud avec Sevalla

Vous pouvez déployer Meilisearch n'importe où. Il fonctionne sur un petit serveur, une machine locale ou dans des conteneurs.

L'auto-hébergement vous donne un contrôle total et est généralement préféré par les équipes techniques qui souhaitent conserver les données sensibles en interne. Vous pouvez choisir n'importe quel fournisseur cloud, comme AWS, DigitalOcean ou d'autres pour configurer Meilisearch. Mais je vais utiliser Sevalla.

[Sevalla](https://sevalla.com/) est un fournisseur PaaS conçu pour les développeurs et les équipes de développement qui déploient des fonctionnalités et des mises à jour en permanence de la manière la plus efficace possible. Il propose l'hébergement d'applications, de bases de données, de stockage d'objets et l'hébergement de sites statiques pour vos projets.

J'utilise Sevalla pour deux raisons :

* Chaque plateforme vous facturera la création d'une ressource cloud. Sevalla offre un crédit de 50 $ à utiliser, nous n'aurons donc aucun coût pour cet exemple.
    
* Sevalla dispose d'un [modèle pour Meilisearch](https://docs.sevalla.com/templates/overview), ce qui simplifie l'installation manuelle et la configuration de chaque ressource nécessaire à l'installation.
    

[Connectez-vous](https://app.sevalla.com/login) à Sevalla et cliquez sur Templates. Vous pouvez voir Meilisearch parmi les modèles. Cliquez sur Deploy.

![Modèle Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1764079735090/db59a275-f641-4f3a-bae9-c1cab1360cbd.png align="center")

Vous verrez les ressources en cours de provisionnement pour l'application.

![Déploiement Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1764079768294/8ca6ccbc-2b64-4a3d-984e-f4cd17e19289.png align="center")

Une fois le déploiement terminé, cliquez sur « Visit app ».

![Meilisearch en Production](https://cdn.hashnode.com/res/hashnode/image/upload/v1764079831010/98be4bbb-6e85-4572-a84e-d11114d1215d.png align="center")

Vous avez maintenant un serveur Meilisearch de qualité production fonctionnant dans le cloud. Vous pouvez l'utiliser pour configurer des index pour votre base de données et utiliser les SDK JavaScript ou autres pour interagir avec Meilisearch.

Voici la [liste complète des API](https://www.meilisearch.com/docs/reference/api/overview) fournies par Meilisearch.

## Conclusion

Meilisearch vous offre une base rapide et élégante pour la recherche. Les modèles d'IA ajoutent de la compréhension et de la personnalisation. Lorsque ces deux éléments travaillent ensemble, vous obtenez une expérience de recherche instantanée, adaptative et intelligente.

Vous pouvez commencer petit avec la recherche par mots-clés, puis ajouter la réécriture de requêtes, les embeddings, la recherche hybride et le reclassement. Vous pouvez également utiliser des suggestions, des synonymes et des filtres pour améliorer le parcours utilisateur.

Avec son API simple, son large support linguistique et son écosystème solide, Meilisearch facilite la création d'une recherche parfaitement intégrée à toute application moderne.

*J'espère que vous avez apprécié cet article. Retrouvez-moi sur* [*Linkedin*](https://linkedin.com/in/manishmshiva) *ou* [*visitez mon site web*](https://manishshivanandhan.com/)*.*