---
title: Comment gérer les pics de trafic dans les systèmes distribués
subtitle: ''
author: Anant Chowdhary
co_authors: []
series: null
date: '2024-05-17T06:50:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-deal-with-traffic-surges-in-distributed-systems
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-pixabay-327345.jpg
tags:
- name: distributed systems
  slug: distributed-systems
seo_title: Comment gérer les pics de trafic dans les systèmes distribués
seo_desc: "Web and Distributed Systems can often get overwhelmed with traffic. \n\
  What leads to systems being overwhelmed, why does it happen, and what are some common\
  \ strategies we can use to deal with this? We'll answer these questions in this\
  \ article.\nTable of..."
---

Les systèmes Web et distribués peuvent souvent être submergés par le trafic. 

Qu'est-ce qui conduit les systèmes à être submergés, pourquoi cela se produit-il, et quelles sont certaines stratégies courantes que nous pouvons utiliser pour y faire face ? Nous répondrons à ces questions dans cet article.

## Table des matières

1. [Qu'est-ce que le trafic dans le contexte des systèmes distribués](#heading-quest-ce-que-le-trafic-dans-le-contexte-des-systemes-distribues) ?
2. [Pourquoi les pics de trafic peuvent-ils être problématiques](#heading-pourquoi-les-pics-de-trafic-peuvent-ils-etre-problematique) ?
3. [Façons de gérer les charges de trafic élevées](#heading-facons-de-gerer-les-charges-de-trafic-elevees)
4. [Retard exponentiel et nouvelles tentatives](#heading-retard-exponentiel-et-nouvelles-tentatives)
5. [Résumé](#heading-resume)

## Qu'est-ce que le trafic dans le contexte des systèmes distribués ?

Le trafic dans les systèmes distribués fait généralement référence à l'échange de données entre les utilisateurs finaux et le point d'entrée d'un système qui peut dépendre de composants distribués. 

Les modèles de trafic qu'un système voit influencent généralement plusieurs décisions de conception, car cela impacte la performance, la scalabilité et la fiabilité d'un système.

## Pourquoi les pics de trafic peuvent-ils être problématiques ?

Les pics de trafic peuvent souvent paralyser les systèmes qui ne sont pas équipés pour les gérer. 

Vous avez peut-être rencontré des cas où des services de médias sociaux tels qu'Instagram ou TikTok sont en panne. Dans certains cas, cela peut être dû à des pics de trafic.

Voici quelques problèmes courants qu'un pic de trafic peut causer : 

1. **Congestion** : À mesure que le trafic augmente, la congestion du réseau peut augmenter. Cela peut, dans certains cas, entraîner une perte de paquets, une latence accrue et impacter les performances des systèmes. 
2. **Charge déséquilibrée** : Tous les systèmes distribués ne répartissent pas bien la charge. Un pic soudain de trafic peut entraîner des défaillances dans certains sous-systèmes. Par exemple, pensons aux tweets d'une célébrité stockés sur un shard. Dans le scénario où un événement conduit des millions de personnes à accéder aux tweets de la célébrité, le shard qui stocke les tweets de la célébrité peut être submergé. 
3. **Défaillances en cascade** : Imaginez un ensemble de dominos placés les uns à côté des autres. Un domino qui tombe peut entraîner la chute de l'ensemble des dominos. Les systèmes distribués sont similaires. Si les composants ne sont pas faiblement couplés, un seul point de défaillance peut entraîner des défaillances en cascade. Il est donc important de prendre en compte les défaillances en cascade lors de la conception de systèmes distribués en gardant à l'esprit les charges de trafic élevées.

## Façons de gérer les charges de trafic élevées

Aucun système n'est à l'abri des défaillances sous une quantité non spécifiée de trafic.

Heureusement, il existe certaines décisions de conception que vous pouvez prendre pour atténuer les problèmes discutés ci-dessus et rendre les systèmes plus résilients face aux défaillances lorsqu'ils voient un pic soudain de trafic. 

Maintenant, couvrons certaines des solutions couramment utilisées qui peuvent aider à gérer les pics de trafic.

Tout d'abord, la mise à l'échelle horizontale est généralement le processus d'ajout de ressources à un système en ajoutant plus de ressources en parallèle. Par exemple, ajouter plus de serveurs ou ajouter plus de nœuds CDN. 

En effet, il s'agit d'ajouter plus de ressources au lieu d'augmenter la capacité d'un seul nœud dans le réseau. 

La distribution du trafic entre les serveurs peut conduire à une amélioration des performances, une latence réduite et des temps de réponse améliorés en général.

Ensuite, l'équilibrage de charge peut parfois être étroitement lié à la mise à l'échelle horizontale. Cependant, l'équilibrage de charge en soi peut également être très utile dans les situations où nous voyons un pic soudain de trafic. 

Les équilibreurs de charge peuvent router intelligemment les requêtes vers les serveurs de sorte que le trafic soit bien équilibré entre les systèmes et ne submerge pas un système particulier.

De plus, la mise en cache peut réduire considérablement le besoin pour le trafic (requêtes) d'aller jusqu'à un serveur pour être satisfait. Certains types de requêtes, comme celles qui accèdent à du contenu statique, sont de bons candidats pour la mise en cache. 

Similaire à un exemple que nous avons discuté dans les sections ci-dessus, supposons qu'il y a un pic soudain de personnes consultant les tweets d'une célébrité. Le contenu statique sur la page, comme la photo de profil de la célébrité, peut être facilement mis en cache. Cela empêchera une requête qui va jusqu'à la base de données de la photo de profil, et donc peut aider à prévenir les défaillances de lecture, et à son tour les défaillances en cascade. 

Enfin, considérons un scénario où un client interne à un système distribué envoie une requête au serveur et la requête échoue. Les clients réessayent souvent les requêtes, mais cela peut entraîner des nouvelles tentatives en cascade. 

C'est un scénario où plusieurs clients (celui d'origine et celui en aval) peuvent réessayer leurs requêtes, et en conséquence, un système en aval peut être inondé de requêtes et cela peut entraîner des défaillances en cascade.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/CascadingRetries.drawio.png)
_Une seule requête de nouvelle tentative peut entraîner un nombre exponentiel de nouvelles tentatives dans d'autres parties d'un système distribué_

Dans la figure ci-dessus, nous pouvons voir que deux requêtes du serveur (une nouvelle tentative en cas d'échec au niveau de la Queue) entraînent : 

1) Quatre requêtes du composant serverless vers le Notification Topic (deux requêtes vers le composant serverless et deux nouvelles tentatives)

2) Huit requêtes du Notification Topic vers la Queue (quatre requêtes vers la queue, quatre nouvelles tentatives).

Même un seul échec au niveau du composant final (la Queue dans ce cas) a entraîné un nombre exponentiel de requêtes de nouvelle tentative vers celui-ci.

Un antidote courant à ce problème est d'utiliser un retard exponentiel lors de la nouvelle tentative de requêtes.

## Retard exponentiel et nouvelles tentatives

Le retard exponentiel, comme son nom l'indique, fait référence à l'introduction d'un délai avant la prochaine tentative au lieu de réessayer immédiatement. Nous augmentons le temps de délai de manière exponentielle à chaque tentative. 

Par exemple, la première nouvelle tentative peut attendre une seconde, la deuxième nouvelle tentative attend deux secondes, la troisième quatre secondes, et ainsi de suite. 

Notez que puisque une tentative de nouvelle tentative n'est pas faite immédiatement, la probabilité de nouvelles tentatives en cascade diminue par rapport à si les nouvelles tentatives étaient faites immédiatement.

Voici un code qui illustre le retard exponentiel en action : 

```python

def exponential_backoff_retry(url, max_retries=5, initial_delay=1, backoff_factor=2):
    retry_count = 0
    while retry_count < max_retries:
        try:
            response = requests.get(url)
            # Vérifie si la réponse était réussie (code de statut 2xx)
            if response.status_code // 100 == 2:
                return response
            # Si ce n'est pas réussi, lève une exception pour déclencher une nouvelle tentative
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"La requête a échoué : {e}")
            # Calcule le délai de retard exponentiel
            delay = initial_delay * (backoff_factor ** retry_count)
            print(f"Nouvelle tentative dans {delay} secondes...")
            time.sleep(delay)
            retry_count += 1
    # Si le nombre maximal de nouvelles tentatives est atteint, lève une exception
    raise RuntimeError(f"Échec de la récupération de {url} après {max_retries} nouvelles tentatives")
```

Le code ci-dessus réessaie les requêtes HTTP GET en utilisant une stratégie de retard exponentiel.

À l'intérieur de la boucle while, nous faisons des tentatives pour faire la requête et vérifions si la réponse est réussie (les requêtes HTTP réussies ont un code de statut de 2xx). 

Notez que si la requête échoue, nous levons une exception et réessayons la requête après avoir calculé un délai exponentiel. 

Ce processus est continué jusqu'à ce qu'une requête réussisse ou que le nombre maximal de nouvelles tentatives soit atteint. Si les nouvelles tentatives maximales sont épuisées sans succès, nous levons une `RuntimeError`. 

## Résumé

Pour résumer, nous avons approfondi la signification du trafic dans les systèmes distribués, en soulignant son influence sur la performance et la résilience des systèmes. 

Nous avons examiné les complications découlant des pics de trafic, y compris la congestion du réseau, les déséquilibres de charge et les défaillances en cascade, qui peuvent rendre les systèmes vulnérables à l'effondrement. 

Pour relever ces défis, nous avons examiné certaines mesures stratégiques telles que la mise à l'échelle horizontale, l'équilibrage de charge, la mise en cache et les stratégies de nouvelle tentative. En particulier, nous avons examiné l'efficacité du retard exponentiel dans l'atténuation des nouvelles tentatives en cascade, améliorant ainsi la robustesse du système. 

En gardant à l'esprit certaines de ces solutions, les systèmes peuvent mieux gérer les pics soudains de trafic, assurant une fonctionnalité soutenue et minimisant les temps d'arrêt potentiels, renforçant ainsi la fiabilité globale du système.

Ce ne sont là que quelques-unes des nombreuses méthodes utilisées à l'échelle de l'industrie pour gérer les pics de trafic.