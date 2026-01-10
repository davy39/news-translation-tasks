---
title: 'Comment fonctionne la gestion des événements dans Vue 3 : un guide pour les
  développeurs'
subtitle: ''
author: Asfak Ahmed
co_authors: []
series: null
date: '2024-09-11T17:21:14.903Z'
originalURL: https://freecodecamp.org/news/how-event-handling-works-in-vue-3-guide-for-devs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725980520061/87728aa1-f3c5-451d-9f11-5163f527d029.png
tags:
- name: Vue.js
  slug: vuejs
- name: Vue3
  slug: vue3
- name: event handling
  slug: event-handling
seo_title: 'Comment fonctionne la gestion des événements dans Vue 3 : un guide pour
  les développeurs'
seo_desc: 'Event handling in Vue 3 allows developers to respond to user interactions
  like clicks, key presses, form submissions, and more.

  Vue provides simple and flexible ways to manage these interactions, enabling you
  to build dynamic and engaging application...'
---

La gestion des événements dans Vue 3 permet aux développeurs de répondre aux interactions des utilisateurs telles que les clics, les pressions sur les touches, les soumissions de formulaires, et bien plus encore.

Vue offre des moyens simples et flexibles de gérer ces interactions, vous permettant de créer des applications dynamiques et attrayantes.

### Dans ce guide, nous aborderons :

* La gestion de base des événements (par exemple, les événements `click`)
    
* Les modificateurs d'événements comme `.prevent`, `.once` et `.stop`
    
* Les événements personnalisés entre les composants parents et enfants
    
* La gestion des événements dans les formulaires
    
* Les événements clavier
    
* Les bases d'`emit`
    
* Les bases de `v-model`
    

À la fin, vous serez en mesure de gérer un large éventail d'événements et d'améliorer l'interaction utilisateur dans vos applications Vue.

### Gestion de base des événements

Vue facilite la gestion d'événements de base comme `click`, `input` et `submit` directement dans votre template. Vous pouvez utiliser le symbole `@` (raccourci pour `v-on`) pour écouter les événements sur les éléments du DOM.

#### Exemple : Gérer un événement de clic

```xml
<template>
  <div>
    <button @click="handleClick">Cliquez-moi</button>
    <p>{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const message = ref('Bonjour, Vue 3 !');

function handleClick() {
  message.value = 'Bouton cliqué !';
}
</script>
```

#### Explication du code :

* `@click="handleClick"` : Le symbole `@` est un raccourci pour `v-on`. Il écoute l'événement `click` et appelle la méthode `handleClick` lorsque le bouton est cliqué.
    
* `message.value = 'Bouton cliqué !'` : Dans l'API Composition de Vue 3, `ref` crée des variables réactives. Lorsque le bouton est cliqué, le `message` réagit aux mises à jour de la variable, et le changement est reflété automatiquement dans le DOM.
    

Ce mécanisme simple d'écoute des événements et de liaison des méthodes est fondamental pour gérer les interactions utilisateur dans Vue.

### Modificateurs d'événements

Les modificateurs d'événements Vue vous permettent de contrôler la manière dont les événements sont gérés, en empêchant le comportement par défaut ou en arrêtant la propagation, par exemple. Les modificateurs d'événements courants incluent `.prevent`, `.stop`, `.once`, `.capture` et `.passive`.

#### 1\. Le modificateur `.prevent`

Le modificateur `.prevent` appelle `event.preventDefault()`, empêchant le comportement par défaut d'événements tels que la soumission de formulaire.

##### Exemple : Utiliser `.prevent` pour gérer la soumission d'un formulaire

```xml
<template>
  <form @submit.prevent="handleSubmit">
    <input type="text" v-model="inputValue" />
    <button type="submit">Envoyer</button>
  </form>
  <p>{{ output }}</p>
</template>

<script setup>
import { ref } from 'vue';

const inputValue = ref('');
const output = ref('');

function handleSubmit() {
  output.value = `Formulaire soumis avec la valeur : ${inputValue.value}`;
}
</script>
```

#### Explication du code :

* `@submit.prevent` : Empêche le formulaire de recharger la page lors de la soumission, permettant à la fonction `handleSubmit` de traiter les données du formulaire à la place.
    
* `v-model="inputValue"` : Liaison de données bidirectionnelle entre l'entrée du formulaire et la variable réactive `inputValue`. Elle se met à jour en temps réel au fur et à mesure que l'utilisateur tape.
    

**Quand utiliser** `.prevent` **:** Utilisez `.prevent` lors de la gestion de formulaires ou d'autres éléments où vous souhaitez empêcher le comportement par défaut, comme empêcher les liens de naviguer.

#### 2\. Le modificateur `.stop`

Le modificateur `.stop` appelle `event.stopPropagation()`, empêchant l'événement de remonter vers les éléments parents.

##### Exemple : Empêcher la propagation d'événement

```xml
<template>
  <div @click="handleDivClick">
    <button @click.stop="handleButtonClick">Cliquez-moi</button>
  </div>
  <p>{{ message }}</p>
</template>

<script setup>
import { ref } from 'vue';

const message = ref('');

function handleDivClick() {
  message.value = 'Div cliquée !';
}

function handleButtonClick() {
  message.value = 'Bouton cliqué !';
}
</script>
```

#### Explication du code :

* `.stop` : Cliquer sur le bouton déclenche uniquement `handleButtonClick` et empêche le clic de se propager à la `div` parente. Sans `.stop`, cliquer sur le bouton déclencherait également `handleDivClick`.
    

**Quand utiliser** `.stop` **:** Utilisez-le pour empêcher les éléments parents de réagir aux événements des éléments enfants.

#### 3\. Le modificateur `.once`

Le modificateur `.once` garantit que l'écouteur d'événement n'est appelé qu'une seule fois.

##### Exemple : Gérer un événement de clic une seule fois

```xml
<template>
  <button @click.once="handleClickOnce">Cliquez-moi une fois</button>
  <p>{{ message }}</p>
</template>

<script setup>
import { ref } from 'vue';

const message = ref('');

function handleClickOnce() {
  message.value = 'Bouton cliqué une fois !';
}
</script>
```

#### Explication du code :

* `.once` : La méthode `handleClickOnce` est déclenchée la première fois que le bouton est cliqué. Les clics suivants ne font rien car l'écouteur d'événement est supprimé après la première exécution.
    

**Quand utiliser** `.once` **:** Utilisez-le pour des actions qui ne devraient se produire qu'une seule fois, comme une soumission de formulaire unique.

#### 4\. Le modificateur `.capture`

Le modificateur `.capture` permet de déclencher le gestionnaire d'événement pendant la phase de capture plutôt que pendant la phase de bouillonnement (bubbling).

##### Exemple : Gérer un événement dans la phase de capture

```xml
<template>
  <div @click.capture="handleClickCapture">
    <button @click="handleClickButton">Cliquez-moi</button>
  </div>
  <p>{{ message }}</p>
</template>

<script setup>
import { ref } from 'vue';

const message = ref('');

function handleClickCapture() {
  message.value = 'Événement de clic capturé !';
}

function handleClickButton() {
  message.value = 'Bouton cliqué !';
}
</script>
```

#### Explication du code :

* `.capture` : Le clic sur la `div` parente est géré en premier, avant l'événement de clic du bouton enfant, car la phase de `capture` se produit avant la phase de bouillonnement.
    

**Quand utiliser** `.capture` **:** Utile lorsque vous avez besoin d'intercepter un événement avant qu'il n'atteigne sa cible.

### Événements personnalisés

Dans Vue, les composants enfants peuvent émettre des événements personnalisés pour communiquer avec les composants parents. Ce modèle est couramment utilisé pour transmettre des données ou déclencher des méthodes dans les composants parents.

#### Exemple : Émettre et gérer des événements personnalisés

`ParentComponent.vue` :

```xml
<template>
  <ChildComponent @custom-event="handleCustomEvent" />
  <p>{{ parentMessage }}</p>
</template>

<script setup>
import { ref } from 'vue';
import ChildComponent from './ChildComponent.vue';

const parentMessage = ref('');

function handleCustomEvent(payload) {
  parentMessage.value = `Événement personnalisé reçu avec la charge utile : ${payload}`;
}
</script>
```

`ChildComponent.vue` :

```xml
<template>
  <button @click="emitCustomEvent">Émettre un événement personnalisé</button>
</template>

<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits();

function emitCustomEvent() {
  emit('custom-event', 'Bonjour de ChildComponent');
}
</script>
```

#### Explication du code :

* `defineEmits()` : Ceci est utilisé dans le composant enfant pour définir des événements personnalisés. Ici, l'enfant émet un `custom-event` avec une charge utile de `'Bonjour de ChildComponent'`. ([vous pouvez en apprendre plus sur emit ici](https://asfakahmedsblog.hashnode.dev/understanding-vuejs-emit-a-complete-guide))
    
* **Gestion des événements dans le parent** : Le composant parent écoute `custom-event` et répond en mettant à jour son `parentMessage` avec la charge utile de l'événement.
    

**Quand utiliser des événements personnalisés :** Utilisez-les pour la communication entre les composants parents et enfants, en particulier pour transmettre des données de l'enfant au parent.

### Gestion des événements dans les formulaires

Le `v-model` de Vue simplifie la gestion des entrées de formulaire en créant une liaison de données bidirectionnelle entre le champ du formulaire et une variable de données.

#### Exemple : Gestion de la saisie et de la soumission de formulaire

```xml
<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="formData.name" placeholder="Nom" />
    <input v-model="formData.email" placeholder="E-mail" />
    <button type="submit">Envoyer</button>
  </form>
  <p>{{ formOutput }}</p>
</template>

<script setup>
import { ref } from 'vue';

const formData = ref({ name: '', email: '' });
const formOutput = ref('');

function handleSubmit() {
  formOutput.value = `Nom soumis : ${formData.value.name}, E-mail : ${formData.value.email}`;
}
</script>
```

#### Explication du code :

* `v-model="`[`formData.name`](http://formData.name)`"` : Cela lie directement le champ de saisie à la variable [`formData.name`](http://formData.name), permettant des mises à jour automatiques au fur et à mesure que l'utilisateur tape. ([vous pouvez en apprendre plus sur v-model ici](https://asfakahmedsblog.hashnode.dev/understanding-vuejs-v-model-a-complete-guide))
    
* La méthode `handleSubmit` traite les données du formulaire et les affiche dans le paragraphe sous le formulaire.
    

### Événements clavier

Vue facilite également la gestion des événements clavier tels que `keydown`, `keyup` et `keypress`.

#### Exemple : Gérer les événements clavier

```xml
<template>
  <input @keydown.enter="handleEnterKey" placeholder="Appuyez sur Entrée" />
  <p>{{ message }}</p>
</template>

<script setup>
import { ref } from 'vue';

const message = ref('');

function handleEnterKey() {
  message.value = 'Touche Entrée pressée !';
}
</script>
```

#### Explication du code :

* `@keydown.enter` : Écoute la pression sur la touche `entrée` et déclenche la fonction `handleEnterKey` lorsqu'elle est pressée. Ceci est utile pour les soumissions de formulaires ou d'autres actions qui devraient être déclenchées par une touche spécifique.
    

### Conclusion

La gestion des événements dans Vue 3 est assez simple et flexible. Des événements de clic de base aux événements personnalisés et à la gestion des formulaires, le système d'événements de Vue vous permet de créer des applications interactives et dynamiques.

En utilisant des modificateurs d'événements et des événements personnalisés, vous pouvez affiner la manière dont les événements sont gérés dans votre application. La compréhension de ces techniques vous permettra de créer des interfaces réactives et conviviales.