---
title: Comment fonctionnent les Composables Vue – Expliqué avec des exemples de code
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2025-06-13T16:56:37.854Z'
originalURL: https://freecodecamp.org/news/how-vue-composables-work
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749830866913/e732db46-638b-42cd-aabf-ad51a54a3409.png
tags:
- name: Vue.js
  slug: vuejs
- name: vue
  slug: vue
seo_title: Comment fonctionnent les Composables Vue – Expliqué avec des exemples de
  code
seo_desc: Vue composables are a very helpful tool when developing Vue applications.
  They give developers an easy way to reuse logic across our applications. In addition
  to allowing for “stateless” logic (things like formatting or routine calculations),
  composa...
---

Les composables Vue sont un outil très utile lors du développement d'applications Vue. Ils offrent aux développeurs un moyen facile de réutiliser la logique dans nos applications. En plus de permettre une logique "sans état" (comme le formatage ou les calculs de routine), les composables nous donnent également la possibilité de réutiliser la logique avec état dans toute l'application.

Avant de plonger dans le tutoriel ci-dessous, je tiens à mentionner que la documentation pour Vue est *vraiment* bonne. [La page sur les composables](https://vuejs.org/guide/reusability/composables) explique très bien les bases et vous mènera à 90 pour cent du chemin. J'écris cet article parce que je pense que les exemples dans la documentation pourraient aller un peu plus loin dans l'explication de la manière dont les choses peuvent fonctionner à l'intérieur d'un composable. Je vais réitérer certaines des informations de la documentation, mais je vais également fournir un exemple d'un composable plus complexe.

### Voici ce que nous allons couvrir :

* [Pourquoi utiliser les Composables ?](#heading-pourquoi-utiliser-les-composables)
    
* [Exemple simple de Composable](#heading-exemple-simple-de-composable)
    
* [Exemple complexe de Composable](#heading-exemple-complexe-de-composable)
    
    * [Fonction utilitaire pour fetch](#heading-fonction-utilitaire-pour-fetch)
        
    * [Composable useAsyncState](#heading-useasyncstate-composable)
        
    * [Utilisation dans un composant](#heading-utilisation-dans-un-composant)
        
* [Conclusion](#heading-conclusion)
    

## Pourquoi utiliser les Composables ?

Les composables vous permettent de réutiliser la logique avec état dans vos applications. Chaque fois qu'il y a une logique utilisée dans plus de deux endroits, nous voulons généralement extraire cette logique dans sa propre fonction. La plupart du temps, cette logique est considérée comme "sans état", ce qui signifie qu'elle prend une entrée et retourne une sortie. La documentation mentionne le formatage de date, mais cela pourrait également inclure quelque chose comme des calculs de devise ou la validation de chaîne.

Dans les applications web modernes, il y a souvent des morceaux de logique qui nécessitent de gérer l'état au fil du temps. À l'intérieur d'un composant typique, nous avons la capacité d'adapter l'application en fonction de l'"état" de différentes variables dans le composant. Parfois, cette logique, ou au moins des morceaux de cette logique, est réutilisée dans toute l'application.

Par exemple, dans une application de commerce électronique, vous pourriez avoir une logique pour augmenter et diminuer la quantité d'un produit qu'une personne ajoute à son panier. Cette logique pourrait être utilisée à la fois sur la page du produit et à l'intérieur du panier lui-même.

L'apparence et la convivialité de ces deux endroits seront différentes, donc réutiliser un composant complet n'aurait pas de sens – mais nous voulons toujours centraliser la logique pour rendre le code plus facile à maintenir. C'est là que les composables interviennent.

(Il est utile de noter que tout n'a pas besoin d'être un composable. La logique utilisée uniquement dans un seul composant ne doit pas être refactorisée en un composable jusqu'à ce que cela soit nécessaire.)

## Exemple simple de Composable

Examinons un exemple simple de compteur. Voici du code pour un composant `Counter` très simple.

```typescript
<script setup lang="ts">
  import { ref } from 'vue'
  import type { Ref } from 'vue'

  const count: Ref<number> = ref(0)
  const increment = () => {
    count.value++
  }
  const decrement = () => {
    count.value--
  }
</script>

<template>
  <div class="bg-teal-100 border-2 border-gray-800 rounded-xl p-4 w-64">
    <div class="text-center mb-4">
      <span class="text-lg font-medium text-gray-800">Compte : {{ count }}</span>
    </div>

    <div class="flex gap-2 justify-center">
      <button
        @click="decrement"
        class="bg-red-100 border-2 border-gray-800 rounded px-4 py-0 text-gray-800 font-medium hover:bg-red-500 transition-colors"
      >
        -
      </button>

      <button
        @click="count = 0"
        class="bg-gray-100 border-2 border-gray-800 rounded px-4 py-0 text-gray-800 font-medium hover:bg-gray-300 transition-colors"
      >
        Réinitialiser
      </button>

      <button
        @click="increment"
        class="bg-green-100 border-2 border-gray-800 rounded px-4 py-0 text-gray-800 font-medium hover:bg-green-500 transition-colors"
      >
        +
      </button>
    </div>
  </div>
</template>
```

Le résultat de ce composant ressemblerait à ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748355723167/8c39759c-6fd9-4fcf-abdf-f67e672c172f.gif align="center")

Cela fonctionne très bien, mais si nous avons besoin de cette même logique de compteur dans un autre composant avec une apparence et une convivialité complètement différentes, nous finirions par répéter la logique. Nous pouvons extraire la logique dans un composable et accéder à la même logique avec état partout où nous en avons besoin.

```typescript
// counter.ts
import { ref } from 'vue'
import type { Ref } from 'vue'

export default function useCounter(): Readonly<{
  count: Ref<number>
  increment: () => void
  decrement: () => void
}> {
  const count: Ref<number> = ref(0)
  const increment = () => {
    count.value++
  }
  const decrement = () => {
    count.value--
  }
  return { count, increment, decrement }
}
```

Ensuite, nous mettons à jour la balise script dans le composant pour utiliser le composable :

```typescript
<script setup>
import { useCounter } from '@/counter.ts'

const { count, increment, decrement } = useCounter()
</script>

<template>
  ...
</template>
```

Maintenant, nous pouvons utiliser cette logique dans plusieurs composants dans toute l'application.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748355833182/d90d000e-f309-4b22-9530-8e4614b450ec.gif align="center")

Vous remarquerez que seule la logique est copiée et que chaque composant a toujours sa propre copie de l'état `count`. L'utilisation d'un composable ne signifie pas que l'état est partagé entre les composants, seulement la logique avec état.

## Exemple complexe de Composable

Dans la documentation de Vue, ils donnent un exemple d'utilisation d'un composable pour gérer la récupération de données asynchrones. Il y a quelques problèmes que j'ai avec l'exemple qu'ils donnent. Le principal est que la gestion des erreurs n'est pas robuste pour les applications réelles. Étant donné qu'ils veulent simplement montrer une utilisation simple des composables, cela est compréhensible. Mais je voulais montrer une implémentation plus réaliste.

### Fonction utilitaire pour `fetch`

Avant de passer au composable, nous devons configurer une fonction utilitaire pour l'API `fetch`. Cela est dû au fait que nous voulons nous assurer que chaque requête génère une erreur en cas d'échec. L'API `fetch` ne génère pas d'erreur si la requête répond avec un statut d'erreur. Nous devons vérifier `response.ok` afin de vérifier le statut, puis générer une erreur si nécessaire.

```typescript
// utils.ts
export async function handleFetch(url: string, options: RequestInit = {}): Promise<Response> {
  const res = await fetch(url, options)
  if (!res.ok) {
    const err = await res.text()
    throw new Error(err)
  }
  return res
}
```

### Composable useAsyncState

Lors de la gestion de l'état asynchrone, les requêtes peuvent se trouver dans quelques états différents :

* En attente
    
* Résolue
    
* Rejetée
    

En plus de ces états, nous voulons suivre les données ou l'erreur qui provient de la requête.

```typescript
// useAsyncState.ts
import { shallowRef } from 'vue'
import type { Ref } from 'vue'

// Spécifier un type pour la réponse
export type AsyncState<T> = {
  data: Ref<T | null>
  error: Ref<Error | null>
  isPending: Ref<boolean>
  isResolved: Ref<boolean>
  isRejected: Ref<boolean>
}

export default function useAsyncState<T>(promise: Promise<T>): AsyncState<T> {
  // J'ai utilisé shallowRef au lieu de ref pour éviter une réactivité profonde
  // Je ne me soucie que des propriétés de premier niveau étant réactives
  const data = shallowRef<T | null>(null)
  const error = shallowRef<Error | null>(null)
  const isPending = shallowRef(false)
  const isResolved = shallowRef(false)
  const isRejected = shallowRef(false)

  data.value = null
  error.value = null
  isPending.value = true
  isRejected.value = false
  isResolved.value = false

  promise.then((result) => {
    data.value = result
    isPending.value = false
    isResolved.value = true
  }).catch(err => {
    error.value = err
    isPending.value = false
    isRejected.value = true
  })

  return { data, error, isPending, isResolved, isRejected }
}
```

Cela donne quelques propriétés plus explicites pour les différents états, plutôt que de se fier aux valeurs dans `data` et `error`. Vous remarquerez également que ce composable prend une promesse plutôt qu'une chaîne d'URL comme le montrent les documents. Différents endpoints auront différents types de réponse et je voulais pouvoir les gérer en dehors de ce composable.

### Utilisation dans un composant

J'ai configuré un endpoint qui attendra un nombre aléatoire de secondes avant de répondre avec succès ou avec une erreur. Mon composant appelle cet endpoint en utilisant le composable et utilise les données du composable pour mettre à jour le modèle.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748364641116/304b8c08-5277-4243-b621-70a7c19edcfd.gif align="center")

Avec l'état d'erreur affiché comme ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748364674070/7d0c6923-85b9-4971-8f69-d127ffa6c1f4.png align="center")

Vous pouvez voir un exemple fonctionnel à l'adresse [https://understanding-composables.pages.dev/](https://understanding-composables.pages.dev/).

Pour faciliter l'explication et la compréhension, je divise la balise `<script>` et les sections `<template>` du composant.

#### Script

```typescript
<script lang="ts" setup>
import { ref, unref } from 'vue'
import type { Ref } from 'vue'
import { useAsyncState } from '@/composables'
import type { AsyncState } from '@/composables'
import { handleFetch } from '@/utils'

interface RandomResponse {
  msg: string
}

async function getRandomResponse(): Promise<RandomResponse> {
  const response = await handleFetch('https://briancbarrow.com/api/random')
  const text = await response.text()
  return { msg: text }
}

const randomResponseData: Ref<AsyncState<RandomResponse> | null> = ref(null)

const handleMakeRequest = async () => {
    const data = getRandomResponse()
    randomResponseData.value = useAsyncState(data)
}
</script>
```

Ici, nous avons une méthode, `getRandomResponse`, qui appelle un endpoint et retourne une promesse. Cette promesse est ensuite passée à `useAsyncState` lorsque `handleMakeRequest` est appelé. Cela place la valeur de retour complète dans la référence `randomResponseData` que nous pouvons ensuite utiliser à l'intérieur du modèle.

Plutôt que de montrer le modèle complet, je vais simplement montrer quelques parties de celui-ci.

Ici, vous pouvez voir deux boutons différents utilisés en fonction de l'état. J'utilise un élément de bouton séparé pour indiquer l'état de "chargement", mais en pratique, vous pouvez utiliser les propriétés du composable pour définir la propriété `disabled` du bouton et changer le texte.

```xml
        <button
          v-if="
            !randomResponseData?.isPending &&
            !randomResponseData?.error &&
            !randomResponseData?.data
          "
          class="px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          @click="handleMakeRequest"
        >
          Faire une requête
        </button>

        <!-- Bouton d'état de chargement -->
        <button
          v-if="randomResponseData?.isPending"
          disabled
          class="px-6 py-3 bg-blue-600 text-white font-medium rounded-lg opacity-75 cursor-not-allowed flex items-center mx-auto"
        >
          <svg
            class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
          Chargement...
        </button>
```

Voici quelques lignes du tableau :

```xml
<tr class="divide-x divide-gray-200">
  <td class="py-4 pr-4 pl-4 text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-0">
    isPending
  </td>
  <td
    class="p-4 text-sm whitespace-nowrap text-gray-500"
    :class="randomResponseData?.isPending ? 'bg-blue-500' : 'bg-gray-300'"
  ></td>
  <td class="p-4 text-sm whitespace-nowrap text-gray-500">
    {{ randomResponseData?.isPending }}
  </td>
</tr>

<tr class="divide-x divide-gray-200">
  <td class="py-4 pr-4 pl-4 text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-0">
    data
  </td>
  <td
    class="p-4 text-sm whitespace-nowrap text-gray-500"
    :class="randomResponseData?.data ? 'bg-green-500' : 'bg-gray-300'"
  ></td>
  <td class="p-4 text-sm whitespace-nowrap text-gray-500">
    {{ unref(randomResponseData?.data)?.msg }}
  </td>
</tr>
```

Dans ces balises `tr`, vous pouvez voir le modèle rendant différentes choses en fonction de l'état provenant du composable.

Pour une vue plus complète du code, vous pouvez visiter [le dépôt GitHub](https://github.com/briancbarrow/understanding-composables). Vous pouvez également voir comment VueUse, une collection de composables, gère des fonctionnalités similaires : [https://vueuse.org/core/useAsyncState/](https://vueuse.org/core/useAsyncState/)

Dans un futur article, j'explorerai leur implémentation.

## Conclusion

Les composables sont un outil incroyablement utile dans Vue 3. À mesure que les projets grandissent en taille et en portée, savoir comment et quand utiliser les composables peut améliorer la maintenabilité du projet à long terme.

La clé est d'identifier lorsque vous avez une logique avec état qui doit être réutilisée dans plusieurs composants, puis de l'extraire dans un composable bien structuré qui gère correctement les cas particuliers.

Pour plus d'exemples concrets, vous pouvez consulter la [bibliothèque VueUse](https://vueuse.org/) et le [dépôt](https://github.com/vueuse/vueuse).