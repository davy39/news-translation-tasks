---
title: Comment créer un limiteur de débit en mémoire dans Next.js
subtitle: ''
author: Orim Dominic Adah
date: '2026-01-09T19:24:26.496Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-in-memory-rate-limiter-in-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767981990510/95306973-8c9a-435b-936e-ae5476f600de.png
tags:
- name: Next.js
  slug: nextjs
- name: ratelimit
  slug: ratelimit
- name: JavaScript
  slug: javascript
seo_title: Comment créer un limiteur de débit en mémoire dans Next.js
seo_desc: An API rate limiter is a server-side component of a web service that limits
  the number of API requests a client can make to an endpoint within a period of time.
  For example, X (formerly known as Twitter) limits the number of tweets that a specific
  us...
---

Un limiteur de débit (rate limiter) d'API est un composant côté serveur d'un service web qui limite le nombre de requêtes API qu'un client peut effectuer vers un point de terminaison (endpoint) sur une période donnée. Par exemple, X (anciennement Twitter) limite le nombre de tweets qu'un utilisateur spécifique peut publier à trois cents toutes les trois heures.

Les limiteurs de débit imposent une utilisation responsable des API en bloquant les requêtes qui dépassent les limites d'utilisation définies.

En suivant cet article, vous allez :

* Apprendre comment fonctionnent les limiteurs de débit
    
* Créer un limiteur de débit en mémoire pour un projet utilisant le routeur d'application Next.js
    
* Utiliser Artillery pour tester la charge du limiteur de débit afin d'en vérifier la précision et la résilience
    

### Voici ce que nous allons aborder :

1. [Avantages des limiteurs de débit](#heading-avantages-des-limiteurs-de-debit)
    
2. [Fonctionnement des limiteurs de débit](#heading-fonctionnement-des-limiteurs-de-debit)
    
3. [Algorithmes de limitation de débit](#heading-algorithmes-de-limitation-de-debit)
    
4. [Comment créer un limiteur de débit en mémoire](#heading-comment-creer-un-limiteur-de-debit-en-memoire)
    
    * [Le limiteur de débit](#heading-le-limiteur-de-debit)
        
    * [Le gestionnaire de requêtes](#heading-le-gestionnaire-de-requetes)
        
5. [Le Front-End](#heading-le-front-end)
    
6. [Comment tester la charge du limiteur de débit pour la résilience avec Artillery](#heading-comment-tester-la-charge-du-limiteur-de-debit-pour-la-resilience-avec-artillery)
    
    * [La configuration du test de charge](#heading-la-configuration-du-test-de-charge)
        
    * [Exécuter le test de charge](#heading-executer-le-test-de-charge)
        
    * [Examiner les résultats](#heading-examiner-les-resultats)
        
7. [Conclusion](#heading-conclusion)
    

Pour tirer le meilleur parti de cet article, vous devriez avoir de l'expérience dans la création d'API avec le routeur d'application Next.js, Express ou tout autre framework backend Node.js utilisant des middlewares.

## Avantages des limiteurs de débit

Les limiteurs de débit contrôlent le nombre de requêtes autorisées dans une fenêtre de temps donnée. Ils présentent plusieurs avantages que vous devriez connaître si vous envisagez de les utiliser.

Tout d'abord, ils aident à prévenir l'abus des serveurs web. Les limiteurs de débit protègent les serveurs web contre une utilisation excessive qui augmente inutilement leur charge. Ils bloquent les requêtes excessives provenant d'attaques par déni de service (DoS) de bots afin que le service web ne plante pas à cause d'une surcharge inutile et puisse rester disponible pour les utilisateurs légitimes.

Ils aident également à gérer le coût d'utilisation des API externes. Certains points de terminaison d'API effectuent des requêtes vers des API externes pour mener à bien leurs opérations – par exemple, les points de terminaison qui envoient des e-mails via un fournisseur de services de messagerie. Lorsqu'un point de terminaison dépend d'API externes payantes et que l'accès des utilisateurs n'est pas restreint, une utilisation excessive peut entraîner des coûts élevés pour le service web. Les limiteurs de débit bloquent l'utilisation excessive de ces points de terminaison, aidant ainsi à maintenir les coûts à un minimum raisonnable.

## Fonctionnement des limiteurs de débit

Les limiteurs de débit fonctionnent selon un mécanisme en trois étapes. Le processus comprend le suivi des requêtes de clients spécifiques, la surveillance de leur utilisation et le blocage des requêtes supplémentaires une fois le seuil dépassé.

Plus en détail, les limiteurs de débit :

* **Suivent les requêtes** : Les limiteurs de débit prennent note des clients API qui effectuent des requêtes et des attributs spécifiques aux clients (par exemple, une adresse IP ou un userId). Ces attributs spécifiques sont des références ou des clés utilisées pour identifier les clients.
    
* **Surveillent l'utilisation** : Selon le mécanisme de limitation, les limiteurs de débit augmentent ou diminuent la métrique utilisée pour déterminer le seuil d'utilisation. Par exemple, sur une période de trois heures, Twitter peut suivre et augmenter le nombre de fois qu'un utilisateur effectue une requête API vers le point de terminaison `create tweet`.
    
* **Assurent la conformité au seuil** : Les limiteurs de débit vérifient le seuil d'utilisation pour chaque requête effectuée. S'il a été dépassé, ils bloquent l'accès de la requête à la fonctionnalité de l'API et répondent avec un code d'état 429.
    
    ![Interaction client-serveur dans un point de terminaison limité en débit](https://cdn.hashnode.com/res/hashnode/image/upload/v1767810794741/616acc5a-4df5-4314-ace2-d179b973874d.png align="center")
    

## Algorithmes de limitation de débit

Vous pouvez implémenter la limitation de débit en utilisant différents algorithmes basés sur vos besoins. Chaque algorithme a ses avantages et ses inconvénients. Voici quelques algorithmes populaires avec lesquels vous pouvez expérimenter.

### Algorithme de fenêtre fixe

Dans l'algorithme de fenêtre fixe (fixed window), le nombre de requêtes effectuées dans une période de temps fixe est suivi et chaque requête augmente le compteur. Si le nombre de requêtes dans ce laps de temps est dépassé, toute requête supplémentaire arrivant dans la même fenêtre est bloquée. À la fin de la période, le compteur est réinitialisé.

Son mécanisme est facile à comprendre et économe en mémoire. Son défi est que des pics de trafic proches du début ou de la fin d'une fenêtre temporelle peuvent autoriser plus de requêtes que permis.

### Algorithme de fenêtre glissante

L'algorithme de fenêtre glissante (sliding window) résout le problème de l'algorithme de fenêtre fixe où les pics de trafic aux limites de la fenêtre peuvent autoriser un surplus de requêtes.

Il fonctionne comme suit :

* Il garde une trace des horodatages (timestamps) des requêtes effectuées dans un cache.
    
* Lorsqu'une nouvelle requête arrive, il supprime tous les horodatages plus anciens que le début de la fenêtre actuelle et ajoute l'horodatage de la nouvelle requête au cache.
    
* Si le nombre de requêtes dans le cache est supérieur au seuil, la requête est bloquée. Sinon, elle est autorisée.
    

Bien que cet algorithme soit plus précis que celui de la fenêtre fixe, il consomme plus de mémoire en raison du stockage des horodatages.

### Algorithme du seau à jetons

Dans l'algorithme du seau à jetons (token bucket), un seau contenant un nombre prédéfini de jetons est attribué à un utilisateur. Des jetons sont ajoutés au seau à un rythme prédéfini, par exemple 2 jetons par seconde.

Une fois le seau plein, plus aucun jeton n'est ajouté. Chaque requête consomme un ou plusieurs jetons, et si les jetons sont épuisés, les requêtes sont bloquées jusqu'à ce que le seau en contienne à nouveau.

L'algorithme Token Bucket a l'avantage d'être économe en mémoire, facile à implémenter et suffisamment précis pour bloquer les requêtes excédentaires même lors d'une rafale de trafic.

Dans ce tutoriel, nous utiliserons l'algorithme de fenêtre fixe pour construire un limiteur de débit. Nous le testerons également pour la résilience et la précision avec Artillery.

## Comment créer un limiteur de débit en mémoire

Si vous êtes un développeur backend, vous avez peut-être remarqué que les utilisateurs abusent parfois du point de terminaison de réinitialisation du mot de passe dans votre application Next.js. C'est préoccupant car ce point de terminaison effectue une requête vers votre fournisseur de services de messagerie pour envoyer un e-mail, ce qui vous est facturé.

Pour cette raison, vous pourriez vouloir limiter les requêtes que les utilisateurs effectuent vers ce point de terminaison afin de prévenir l'abus de l'API et d'économiser des coûts. C'est là qu'intervient un limiteur de débit.

Vous pouvez obtenir le [code de ce tutoriel ici](https://github.com/orimdominic/nextjs-app-router-rate-limiter). Vous pouvez le cloner, installer les dépendances avec `npm install`, et l'exécuter en suivant les instructions du [fichier README](https://github.com/orimdominic/nextjs-app-router-rate-limiter/blob/main/README.md). Vous en aurez besoin pour suivre la suite de cet article.

J'ai construit le projet avec Next.js en utilisant le routeur d'application. J'ai également conçu le limiteur de débit que [vous pouvez trouver ici](https://github.com/orimdominic/nextjs-app-router-rate-limiter/blob/main/src/lib/server/rate-limiter.ts). Vous pouvez voir comment l'utiliser dans le [point de terminaison de réinitialisation de mot de passe ici](https://github.com/orimdominic/nextjs-app-router-rate-limiter/blob/main/src/pages/api/reset-password-init.ts).

Il possède une interface utilisateur que vous pouvez utiliser pour tester le limiteur manuellement – mais plongeons d'abord dans le code.

### Le limiteur de débit

Le fichier [src/lib/server/rate-limiter.ts](https://github.com/orimdominic/nextjs-app-router-rate-limiter/blob/main/src/lib/server/rate-limiter.ts) exporte une fonction appelée `applyRateLimiter` qui accepte trois paramètres :

* l'objet requête (request)
    
* l'objet réponse (response)
    
* `getOptsFn`
    

`getOptsFn` est une fonction qui accepte l'objet requête et, lorsqu'elle est exécutée, renvoie des propriétés spécifiques à la requête pour le suivi, la surveillance et le blocage par le limiteur de débit. `getOptsFn` est une fonction et non un objet statique afin que les propriétés spécifiques d'une requête puissent être créées dynamiquement par le gestionnaire pour chaque requête.

[src/lib/server/rate-limiter.ts](https://github.com/orimdominic/nextjs-app-router-rate-limiter/blob/main/src/lib/server/rate-limiter.ts) possède également une map en mémoire appelée `cache`. `cache` stocke la clé (ou identifiant unique) d'une requête et la lie à son utilisation. Un intervalle s'exécute chaque minute pour supprimer du cache les clés dont les valeurs `expiredAt` sont dépassées. Cela aide à gérer la quantité de mémoire utilisée par le cache.

```typescript
type GetOptionsFn = (req: NextApiRequest) => {
  key: string;
  maxTries: number;
  expiresAt: Date;
};

const cache = new Map<string, Usage>();

// effacer les clés obsolètes du cache chaque minute
setInterval(() => {
  const currentDate = new Date();
  for (const [key, usage] of cache) {
    if (!usage) continue;

    if (currentDate > usage.expiresAt) {
      cache.delete(key);
    }
  }
}, 60000);
```

Lorsque le limiteur de débit est exécuté, il utilise `getOptsFn` pour générer les éléments suivants à partir de la requête :

* `key` : L'identifiant unique de la requête utilisé pour suivre son utilisation
    
* `maxTries` : Le nombre maximum de fois qu'une requête peut être effectuée dans la fenêtre de temps spécifiée
    
* `expiresAt` : L'heure d'expiration d'une fenêtre de temps
    

selon le contexte où il a été créé.

```typescript
  const opts = getOptsFn(req);
  const usage = cache.get(opts.key);

  if (!usage) {
    cache.set(opts.key, {
      tries: 1,
      maxTries: opts.maxTries,
      expiresAt: opts.expiresAt,
    });

    return;
  }
```

Le limiteur de débit vérifie ensuite si la `key` de la requête existe dans le cache. Si ce n'est pas le cas, il l'ajoute au cache avec les valeurs suivantes :

* `tries` : Le nombre de fois que la requête a été effectuée sans être bloquée
    
* `maxTries` : Le nombre maximum de tentatives autorisées dans la fenêtre de temps
    
* `expiresAt` : L'heure d'expiration de la fenêtre de temps
    

Il permet également à la requête de continuer en sortant du limiteur via l'instruction `return`. Les valeurs définies dans `cache` seront utilisées pour déterminer si les requêtes consécutives avec la même clé doivent être bloquées ou non.

Si la clé de la requête existe dans le `cache`, le limiteur vérifie si le nombre de tentatives non bloquées (`usage.tries`) est inférieur au nombre maximum autorisé (`usage.maxTries`). Si c'est `true`, cela signifie que la requête n'a pas dépassé son quota. Il vérifie également si le temps d'expiration stocké dans le cache est écoulé.

La requête n'est pas bloquée si l'une des conditions suivantes est vraie :

* la requête n'a pas dépassé son maximum de tentatives ET sa fenêtre de temps n'est pas écoulée
    
* la fenêtre de temps actuelle de l'utilisation dans le cache (`usage.expiresAt`) est écoulée
    

```typescript
  const currentDate = new Date();
  const retryAfter = usage.expiresAt.getTime() - currentDate.getTime();
  const canProceed = usage.tries < opts.maxTries && retryAfter >= 0;

  if (canProceed) {
    cache.set(opts.key, {
      ...usage,
      tries: usage.tries + 1,
    });

    return;
  }

  if (retryAfter <= 0) { // si usage.expiresAt est écoulé
    cache.set(opts.key, {
      tries: 1,
      maxTries: opts.maxTries,
      expiresAt: opts.expiresAt,
    });

    return;
  }
```

Si la première condition est vraie, le limiteur augmente le nombre de tentatives (`usage.tries`) dans le cache et laisse la requête continuer. Si la deuxième condition est vraie, le limiteur réinitialise l'utilisation de la requête dans le cache avec les nouvelles valeurs de `getOptsFn` et laisse la requête continuer. Si les deux conditions sont fausses, la requête est bloquée avec un code d'état 429.

```typescript
  res.setHeader("Retry-After", retryAfter);
  return res.status(429).json({
    error: { message: "Too many requests" },
  });
```

Selon les spécifications REST, une réponse HTTP 429 peut inclure un en-tête [Retry-After](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After) pour indiquer aux clients combien de temps attendre avant de refaire une requête. La valeur de `Retry-After` est calculée au préalable et définie sur l'objet réponse via `res.setHeader`.

### Le gestionnaire de requêtes

Vous trouverez le gestionnaire de réinitialisation de mot de passe dans [src/pages/api/reset-password-init.ts](https://github.com/orimdominic/nextjs-app-router-rate-limiter/blob/main/src/pages/api/reset-password-init.ts). Tout d'abord, il effectue des validations sur la méthode et le corps de la requête. La validation garantit qu'il s'agit d'une requête POST et que le corps inclut une propriété `email`. Il termine la requête avec le code de réponse approprié en cas d'échec.

```typescript
  if (req.method !== "POST") {
    return res.status(405).json({
      error: { message: "Not allowed" },
    });
  }

  if (!req.body.email || typeof req.body.email != "string") {
    return res.status(400).json({
      error: { message: "'email' is required" },
    });
  }
```

`generateOptions` est la fonction passée comme `getOptsFn` au limiteur. Elle génère les propriétés spécifiques :

* `key` : Une chaîne au format `[method].[endpoint].[email]`. Pour un e-mail "Hello@me.com", la clé sera `post.reset-password.hello@me.com`. Ce format rend la clé unique et spécifique à cette requête.
    
* `expiresAt` : Le moment où la fenêtre expire. Si la requête est déjà en cache, cette valeur est ignorée au profit de celle du cache.
    
* `maxTries` : Le nombre maximum de tentatives autorisées. De même, si déjà en cache, cette valeur est ignorée.
    

```typescript
  const generateOptions = function (req: NextApiRequest) {
    const now = new Date();
    const inFiveSeconds = new Date(now.getTime() + 5000);

    return {
      expiresAt: inFiveSeconds,
      key: `post.reset-password.${req.body.email.toLowerCase()}`,
      maxTries: 1,
    };
  };
```

Pour ce gestionnaire, les requêtes sont limitées à une toutes les cinq secondes. Vous pouvez modifier `expiresAt` et `maxTries` pour tester. `applyRateLimiter` est exécuté et si la requête n'est pas bloquée, le gestionnaire peut envoyer l'e-mail et répondre au client.

## Le Front-End

Vous pouvez visiter l'interface utilisateur pour tester le limiteur manuellement. Accédez à l'URL affichée (http://localhost:3000 par défaut) après avoir lancé `npm run dev`. Vous devriez voir l'interface ci-dessous.

![Interface utilisateur pour tester le limiteur de débit manuellement](https://cdn.hashnode.com/res/hashnode/image/upload/v1767603425330/e7fd49a8-e8ce-4e76-b5f5-df094a5fa3f1.png align="center")

## Comment tester la charge du limiteur de débit pour la résilience avec Artillery

[Artillery](https://www.artillery.io/) est un outil pour tester et rapporter les performances des applications web sous une lourde charge. Dans cette section, vous utiliserez Artillery pour tester l'efficacité et la précision du limiteur que vous avez construit.

Pour utiliser Artillery, installez-le globalement via la commande `npm install -g artillery@latest` afin que la commande `artillery` soit disponible dans votre terminal.

### La configuration du test de charge

Dans le dossier `loadtest` à la racine du projet, vous trouverez le fichier `setup.yaml`. Il contient les instructions pour Artillery. Ces instructions demandent à Artillery de créer des utilisateurs virtuels qui effectueront des requêtes API vers l'application (URL `target`) en trois phases :

* **Préchauffage (Warm up)** : Requêtes pendant dix secondes, commençant à une requête par seconde jusqu'à cinq.
    
* **Montée en charge (Ramp up)** : Pendant trente secondes, de cinq à dix requêtes par seconde.
    
* **Phase de pic (Spike phase)** : Pendant vingt secondes, de dix à trente requêtes par seconde.
    

Cela porte la durée totale du test à soixante secondes.

```yaml
config:
  target: http://localhost:3000/api

  phases:
    - duration: 10
      arrivalRate: 1
      rampTo: 5
      name: Warm up

    - duration: 30
      arrivalRate: 5
      rampTo: 10
      name: Ramp up

    - duration: 20
      arrivalRate: 10
      rampTo: 30
      name: Spike phase
```

La section [`plugins`](https://www.artillery.io/docs/reference/extensions) contient des extensions pour analyser les résultats. Par exemple, le plugin [`ensure`](https://www.artillery.io/docs/reference/extensions/ensure) rapportera "OK" si au moins 99 % des réponses ont une latence de 100 ms ou moins.

```yaml
  plugins:
    ensure:
      thresholds:
        - http.response_time.p99: 100
        - http.response_time.p95: 75
```

Un [`scenario`](https://www.artillery.io/docs/reference/test-script#scenarios-section) est une séquence d'étapes décrivant une session d'utilisateur virtuel. Chaque utilisateur créé dans les `phases` effectuera une requête POST vers le point de terminaison défini dans `flow`.

```yaml
scenarios:
  - flow:
      - loop:
          - post:
              url: "/reset-password-init"
              headers:
                Content-Type: "application/json"
              json:
                email: "j.doe@email.com"

        count: 1
```

### Exécuter le test de charge

Assurez-vous que l'application tourne et lancez le test avec la commande `artillery run loadtest/setup.yaml --output loadtest/results.json`. Cela testera le point de terminaison et sauvegardera les résultats dans `loadtest/results.json`.

### Examiner les résultats

Peu importe le nombre de requêtes, notre configuration n'autorise qu'une requête toutes les cinq secondes. Sur soixante secondes, seules douze requêtes devraient être autorisées.

En regardant `loadtest/results.json`, vous verrez que seules douze requêtes ont un code d'état 200. Même si vous augmentez l'intensité du trafic, ce nombre restera à douze. Cela signifie que notre limiteur reste efficace et précis même sous forte charge.

Pour la latence, consultez le rapport du plugin `ensure` à la fin du test. Un résultat comme :

```plaintext
Checks:
ok: http.response_time.p95 < 75
ok: http.response_time.p99 < 100
```

signifie que 95 % des requêtes ont eu une latence inférieure à 75 ms et 99 % inférieure à 100 ms. Ce sont d'excellents résultats.

## Conclusion

Dans cet article, vous avez découvert les limiteurs de débit, les algorithmes associés, et comment construire un limiteur en mémoire dans Next.js.

Vous avez également eu une brève introduction aux tests de charge avec Artillery. N'hésitez pas à appliquer ces connaissances dans vos projets Next.js.

N'hésitez pas à [me contacter sur LinkedIn](https://www.linkedin.com/in/orimdominicadah/) pour toute question. Merci d'avoir lu jusqu'ici et j'espère que cela vous aidera. Partagez cet article s'il peut être utile à d'autres. Santé !