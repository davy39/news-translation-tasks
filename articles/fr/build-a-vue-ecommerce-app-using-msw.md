---
title: Comment créer une application e-commerce Vue en utilisant MSW
subtitle: ''
author: Abhijeet Dave
co_authors: []
series: null
date: '2024-07-08T18:49:45.000Z'
originalURL: https://freecodecamp.org/news/build-a-vue-ecommerce-app-using-msw
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/build-a-Vue-eCommerce-App-using-MSW.png
tags:
- name: ecommerce
  slug: ecommerce
- name: vue
  slug: vue
seo_title: Comment créer une application e-commerce Vue en utilisant MSW
seo_desc: Building an e-commerce app can be a time-consuming task, but with the right
  tools, it becomes much more manageable. In this guide, we'll explore how to create
  a robust Vue.js e-commerce application using Mock Service Worker (MSW) to simulate
  backend ...
---

Créer une application e-commerce peut être une tâche chronophage, mais avec les bons outils, cela devient beaucoup plus gérable. Dans ce guide, nous explorerons comment créer une application e-commerce robuste en Vue.js en utilisant Mock Service Worker (MSW) pour simuler les interactions backend. 

Que vous soyez un développeur expérimenté ou que vous débutiez, ce tutoriel pas à pas vous aidera à comprendre les bases de l'intégration de MSW dans votre projet Vue, vous permettant de construire et de tester votre application plus efficacement sans dépendre d'un vrai backend. 

Plongeons-nous et donnons vie à votre vision e-commerce !

## Table des matières

<ul>
<li><a href="#quest-ce-quun-serveur-mock">Qu'est-ce qu'un serveur mock ?</a></li>
<li><a href="#comment-installer-une-application-ecommerce-vue">Comment installer une application e-commerce Vue</a></li>
<li><a href="#demarrage-avec-lapplication-ecommerce-vue">Démarrage avec l'application e-commerce Vue</a></li>
<li><a href="#comment-construire-une-application-ecommerce-en-utilisant-vue-3">Comment construire une application e-commerce en utilisant Vue 3</a></li>
<li><a href="#comment-construire-linterface-utilisateur">Comment construire l'interface utilisateur</a></li>
<li><a href="#conclusion">Conclusion</a></li>
</ul>

Dans cet article, nous allons parcourir le processus de création d'une application e-commerce à partir de zéro en utilisant [Vue.js](https://vuejs.org/) et la puissance de MSW pour simuler les appels API.

Avant de commencer le projet, prenons un aperçu des pages e-commerce que nous allons construire pour l'application. Elle aura principalement deux pages :

* Page boutique.
* Page détails du produit.

**Page boutique** : Cette page affichera tous les produits du magasin.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/eCommerce-Products-Page.png)
_Maquette créée en utilisant Pika Style_

**Page détails du produit** : Cette page affiche tous les détails concernant le produit.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/eCommerce-product-details-page.png)

Avant de construire une application e-commerce, clarifions quelques bases sur le serveur mock.

## Qu'est-ce qu'un serveur mock ?

Un serveur mock imite simplement un serveur réel en fournissant des réponses prédéfinies pour une requête API. Un serveur mock est utile pour les tests et le développement car il peut générer différents cas de test sans risquer l'intégrité des données réelles. Vous pouvez configurer un serveur mock pour retourner des réponses spécifiques, des messages d'erreur et des timeouts.

Il existe divers outils/bibliothèques que vous pouvez utiliser pour configurer un serveur mock. Dans cet article, nous utiliserons MSW (Mock Service Worker) pour configurer un serveur mock. Vous pouvez en apprendre davantage sur MSW à partir de sa [documentation officielle](https://mswjs.io/).

Maintenant, configurons un serveur mock (en utilisant MSW) pour notre application e-commerce Vue.

## Comment installer une application e-commerce Vue

Pour notre application e-commerce, nous aurons besoin de deux points de terminaison API. Voici une brève description des points de terminaison API.

1. `/api/apps/ecommerce/products` : Cela récupérera les données de tous les produits que nous avons en magasin.
2. `/api/apps/ecommerce/product/:id` : Cela récupérera les détails du produit d'un produit spécifique par son ID.

Nous utiliserons un tableau de bord d'administration Vue gratuit qui offre des fonctionnalités essentielles telles que :

* Des composants soigneusement conçus
* Des capacités d'importation automatique
* Une mise en page préconçue, et ainsi de suite.

Ces fonctionnalités rendront le développement de l'application e-commerce Vue plus facile et plus rapide.

## Démarrage avec l'application e-commerce Vue

Il existe de nombreux [thèmes Vue.js](https://vuejs.org/ecosystem/themes) disponibles que vous pouvez considérer pour créer une application e-commerce. 

Ici, nous utiliserons le modèle d'administration Materio Vue.js gratuit. Tout d'abord, allez sur le [dépôt GitHub](https://github.com/themeselection/materio-vuetify-vuejs-admin-template-free).

Pour le cloner, ouvrez simplement votre terminal. Naviguez jusqu'au répertoire où vous souhaitez cloner le projet et exécutez la commande suivante :

```bash
git clone <https://github.com/themeselection/materio-vuetify-vuejs-admin-template-free.git>

```

Ouvrez le projet dans votre IDE préféré et exécutez la commande ci-dessous dans le terminal pour installer toutes les dépendances. 

Nous utiliserons le gestionnaire de paquets [`pnpm`](https://pnpm.io/) comme recommandé par le tableau de bord que nous utilisons. Cependant, vous êtes libre d'utiliser votre gestionnaire de paquets préféré comme npm ou yarn.

```bash
pnpm install
# npm install
# yarn

```

Ensuite, installez MSW dans votre répertoire de projet :

```bash
pnpm add -D msw@latest
# npm install msw@latest --save-dev
# yarn install -D msw@latest

```

Exécutez le thème en utilisant la commande suivante :

```bash
pnpm run dev
# npm run dev
# yarn run dev

```

Ensuite, initialisez MSW en utilisant la commande ci-dessous. L'exécution de cette commande créera un fichier **mockServiceWorker.js** dans un répertoire public.

```bash
npx msw init public

```

Pour gérer tous les points de terminaison API et les fausses données, créez un nouveau dossier appelé **fake-server** à l'intérieur du répertoire **plugins**. Nous configurerons notre serveur mock dans ce répertoire **fake-server**. Créez un fichier **index.ts** et collez le code ci-dessous pour enregistrer `MSW`.

```tsx
// fichier : src/plugins/fake-server/index.ts

import { setupWorker } from 'msw/browser'

const worker = setupWorker()

export default function () {
  const workerUrl = `${import.meta.env.BASE_URL ?? '/'}mockServiceWorker.js`

  worker.start({
    serviceWorker: {
      url: workerUrl,
    },
    onUnhandledRequest: 'bypass',
  })
}


```

Félicitations, vous avez maintenant configuré avec succès `MSW` dans le projet. Maintenant, nous pouvons commencer à construire une application e-commerce.

## Comment construire une application e-commerce en utilisant Vue 3

Dans le répertoire **fake-server**, créez un répertoire **handlers** pour maintenir les gestionnaires. À l'intérieur du répertoire **handlers**, créez un répertoire **ecommerce** pour les gestionnaires de l'application e-commerce. Ensuite, créez un fichier **db.ts** à l'intérieur de **ecommerce** pour stocker les fausses données.

Votre structure de dossiers devrait ressembler à ceci :

```tsx
.
 fake-server/
     handlers/
         ecommerce/
             db.ts

```

J'ai généré quelques fausses données pour afficher les produits. Placions ces fausses données dans **db.ts** :

```tsx
// fichier : src/plugins/fake-server/handlers/ecommerce/db.ts

import product5 from '@images/eCommerce/1.png'
import product3 from '@images/eCommerce/11.png'
import product6 from '@images/eCommerce/18.png'
import product1 from '@images/eCommerce/27.png'
import product4 from '@images/eCommerce/5.png'
import product2 from '@images/eCommerce/7.png'

export const db = {
  products: [
    {
      id: 1,
      productName: 'Souris de jeu',
      category: 'Électronique',
      price: '999 $',
      image: product1,
      rating: 5,
      productDescription: 'Une souris spécialement conçue pour les joueurs.',
    },
    {
      id: 2,
      productName: 'Google Home',
      category: 'Électronique',
      price: '25,50 $',
      image: product2,
      rating: 4,
      productDescription: 'Un haut-parleur intelligent avec Google Assistant.',
    },
    {
      id: 3,
      productName: 'Chaussures de course INZCOU',
      category: 'Chaussures',
      price: '36,98 $',
      image: product3,
      rating: 5,
      productDescription: 'Chaussures de tennis légères antidérapantes pour la salle de sport',
    },
    {
      id: 4,
      productName: 'MacBook Pro 16',
      category: 'Électronique',
      price: '2648,95 $',
      image: product4,
      rating: 5,
      productDescription: 'Ordinateur portable avec puce M2 Pro avec CPU 12 cœurs et GPU 19 cœurs',
    },
    {
      id: 5,
      productName: 'Apple Watch Series 7',
      category: 'Bureau',
      price: '799 $',
      image: product5,
      rating: 5,
      productDescription: 'Boîtier en aluminium Starlight avec bracelet sport Starlight.',
    },
    {
      id: 6,
      productName: 'Meta Quest 2',
      category: 'Bureau',
      price: '299 $',
      image: product6,
      rating: 5,
      productDescription: 'Casque de réalité virtuelle tout-en-un avancé',
    },
  ],
}

```

Comme discuté dans la structure de cette application, nous devons définir deux points de terminaison. Créez un fichier **index.ts** dans votre gestionnaire e-commerce et définissez vos points de terminaison dans celui-ci :

```tsx
// fichier : src/plugins/fake-server/handlers/ecommerce/index.ts

import { HttpResponse, http } from 'msw'
import { db } from './db'

export const handlerEcommerce = [
  http.get('/api/ecommerce/products', () => {
    const products = db.products

    return HttpResponse.json(products, { status: 200 })
  }),

  http.get('/api/ecommerce/products/:id', ({ params }) => {
    const id = Number(params.id)

    const product = db.products.find(item => item.id === id)

    if (!product)
      return HttpResponse.error()

    return HttpResponse.json(product, { status: 200 })
  }),
]

```

Enregistrez le gestionnaire dans le fichier **index.ts** dans le répertoire **fake-server**. Le fichier **index.ts** mis à jour devrait ressembler à ceci :

```tsx
// fichier : src/plugins/fake-server/index.ts

import { setupWorker } from 'msw/browser'

import { handlerEcommerce } from './handlers/ecommerce'

const worker = setupWorker(...handlerEcommerce)

export default function () {
  const workerUrl = `${import.meta.env.BASE_URL ?? '/'}mockServiceWorker.js`

  worker.start({
    serviceWorker: {
      url: workerUrl,
    },
    onUnhandledRequest: 'bypass',
  })
}

```

La configuration du serveur mock est terminée. Chaque fois que vous faites un appel API à votre point de terminaison, MSW intercepta la requête HTTP en utilisant le service worker et fournira une réponse prédéfinie à partir des gestionnaires.

Félicitations, vous avez configuré avec succès le serveur mock👍🏻.

## Comment construire l'interface utilisateur

Passons à la partie interface utilisateur de l'application e-commerce. Créez un répertoire **apps** dans le répertoire **pages**. À l'intérieur de **apps**, créez un nouveau répertoire appelé **ecommerce**. Nous placerons l'application e-commerce dans ce répertoire.

La structure des dossiers devrait ressembler à ceci :

```tsx
.
 pages/
     apps/
         ecommerce

```

La première page est une page de liste de produits. Créez un nouveau répertoire **products** à l'intérieur de **ecommerce**. Créez un fichier **index.vue** dans le répertoire **products** et collez le code suivant :

```tsx
// fichier : src/pages/apps/ecommerce/products/index.vue

<script setup lang="ts">
const router = useRouter()
const { data: products } = await useFetch('/api/ecommerce/products').json()
</script>

<template>
  <div>
    <div class="d-flex flex-wrap gap-6 justify-center">
      <template
        v-for="(product, index) in products"
        :key="index"
      >
        <VCard width="300">
          <VImg
            :src="product.image"
            cover
          />
          <VCardItem>
            <VCardTitle>{{ product.productName }}</VCardTitle>
            <VCardSubtitle>Prix : {{ product.price }}</VCardSubtitle>
          </VCardItem>
          <VCardText>
            <p class="mb-0">
              {{ product.productDescription }}
            </p>
            <VRating
              :model-value="product.rating"
              readonly
              density="compact"
              class="my-3"
            />
            <VBtn
              block
              @click="() => router.push({ path: `/apps/ecommerce/products/${product.id}` })"
            >
              Acheter maintenant
            </VBtn>
          </VCardText>
        </VCard>
      </template>
    </div>
  </div>
</template>

```

Sur cette page de liste de produits, nous avons fait un appel API au point de terminaison `'/api/ecommerce/products'`. Ce point de terminaison retourne le tableau de tous les produits. Nous utiliserons ces données pour afficher les produits sur la page.

La deuxième page de cette application est la page d'affichage du produit. Sur cette page, nous afficherons tous les détails du produit. Pour ce faire, créez un nouveau fichier **[id].vue** à l'intérieur du répertoire **products**. Voici le code pour la page des détails du produit.

Notez que j'ai utilisé Lorem ipsum pour le garder générique. Vous pouvez le remplacer par la description de votre choix. 

```tsx
// fichier : src/pages/apps/ecommerce/products/[id].vue

<script setup lang="ts">
const route = useRoute()
const router = useRouter()

const { data: product } = await useFetch(`/api/ecommerce/products/${route.params.id}`).json()
const quantity = ref(0)
</script>

<template>
  <VCard class="pa-10">
    <VRow>
      <VCol
        md="4"
        cols="12"
      >
        <div class="py-10 bg-background d-flex justify-center">
          <VImg
            :src="product.image"
            width="auto"
            max-height="40vh"
          />
        </div>
      </VCol>

      <VCol
        md="8"
        cols="12"
      >
        <div>
          <div class="text-h3 mb-4">
            {{ product.productName }}
          </div>

          <div class="text-h4 mb-4">
            {{ product.price }}
          </div>

          <div>
            <p>
              {{ product.productDescription }}
              Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolor eum quam dolore ratione aspernatur nobis. Assumenda dicta voluptatibus reiciendis repudiandae?
            </p>
            <VRating
              :model-value="product.rating"
              readonly
              density="compact"
              class="mb-2 d-block"
            />

            <VList>
              <VListItem>
                <template #prepend>
                  <VIcon
                    icon="ri-circle-fill"
                    size="10"
                  />
                </template>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Culpa, deserunt!
              </VListItem>
              <VListItem>
                <template #prepend>
                  <VIcon
                    icon="ri-circle-fill"
                    size="10"
                  />
                </template>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Culpa, deserunt!
              </VListItem>
              <VListItem>
                <template #prepend>
                  <VIcon
                    icon="ri-circle-fill"
                    size="10"
                  />
                </template>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Culpa, deserunt!
              </VListItem>
              <VListItem>
                <template #prepend>
                  <VIcon
                    icon="ri-circle-fill"
                    size="10"
                  />
                </template>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Culpa, deserunt!
              </VListItem>
            </VList>

            <VBtn
              prepend-icon="ri-shopping-cart-line"
              class="text-center"
              size="large"
              @click="quantity += 1"
            >
              Ajouter au panier
            </VBtn>
          </div>
        </div>
      </VCol>
    </VRow>
  </VCard>
  <div class="text-center">
    <VBtn
      class="my-6 text-center"
      @click="() => router.push({ path: '/apps/ecommerce/products' })"
    >
      Continuer les achats
    </VBtn>
  </div>
</template>

```

Sur cette page, nous avons fait une requête API à notre deuxième point de terminaison : `/api/ecommerce/products/:id`. Ce point de terminaison retourne les détails du produit liés à un ID de produit donné. Nous utiliserons ces données sur notre page pour afficher les détails du produit.

Ajoutons des routes pour l'application e-commerce. Toutes les routes sont situées dans le fichier **src/plugins/router/routes.ts**. Dans le fichier, ajoutez les routes de l'application e-commerce.

```tsx
// fichier : src/plugins/router/routes.ts
{
  path: '/apps/ecommerce/products',
  component: () => import('@/pages/apps/ecommerce/products/index.vue'),
},
{
  name: 'apps-ecommerce-products-id',
  path: '/apps/ecommerce/products/:id',
  component: () => import('@/pages/apps/ecommerce/products/[id].vue'),
},

```

Maintenant, ajoutons une application e-commerce à notre menu de navigation. Nous listerons tous nos éléments de menu et groupes dans les composants `NavItems.vue`. Nous utiliserons un composant `VerticalNavGroup` pour ajouter un groupe de navigation et un composant `VerticleNavLink` pour ajouter un élément de navigation. Pour ajouter une application e-commerce dans le menu de navigation, ajoutez le code ci-dessous dans la section `Apps & Pages`.

```tsx
//fichier : src/layouts/components/NavItems.vue

<VerticalNavGroup
    :item="{
      title: 'e-commerce',
      icon: 'ri-shopping-cart-line',
    }"
  >
    <VerticalNavLink
      :item="{
        title: 'Boutique',
        to: '/apps/ecommerce/products',
      }"
    />
    <VerticalNavLink
      :item="{
        title: 'Produit',
        to: { name: 'apps-ecommerce-products-id', params: { id: 1 } },
      }"
    />
</VerticalNavGroup>

```

Félicitations, vous avez construit une application e-commerce Vue en utilisant Vue.js et MSW. Vous pouvez visiter le serveur de développement pour voir l'application e-commerce que nous venons de créer.

## Conclusion

Dans cet article, vous avez construit une application e-commerce en utilisant Vue.js et MSW pour simuler les appels API. Nous avons créé deux pages principales : la page boutique pour afficher les produits et la page détails du produit pour montrer les informations sur le produit.

La configuration du serveur mock nous a aidés à créer un environnement de développement réaliste sans construire un backend réel. À la fin de ce guide, vous aviez un prototype d'application e-commerce fonctionnelle. Cette configuration fournit une base solide pour une personnalisation et un développement ultérieurs.

Pour l'implémentation complète de l'application e-commerce construite dans cet article, veuillez vous référer à ce dépôt GitHub : [https://github.com/themeselection/e-commerce-app](https://github.com/themeselection/e-commerce-app).

J'espère que vous trouverez tous cet article utile. Au cas où vous souhaiteriez développer une application e-commerce complète, vous pouvez utiliser le modèle d'administration [Vuejs pré-construit](https://themeselection.com/item/category/vuejs-admin-templates/) car il offre de nombreux composants et fonctionnalités qui peuvent être utiles pour créer une application e-commerce professionnelle.

J'ai préparé cet article avec l'aide de [Jayendrasinh Solanki](https://x.com/me_jd_solanki). Il est expert en VueJS avec plus de 7 ans d'expérience. Au fait, il est suivi par le créateur de Vue, Evan You ! N'est-ce pas génial ?

### Quelques guides utiles pour le développement de produits e-commerce :

* [Comment développer une plateforme eCommerce réutilisable (freecodecamp.org)](https://www.freecodecamp.org/news/develop-a-reusable-ecommerce-platform/).
* [Comment créer un site eCommerce en utilisant WooCommerce (freecodecamp.org)](https://www.freecodecamp.org/news/how-to-create-an-ecommere-website-using-woocomerce/).