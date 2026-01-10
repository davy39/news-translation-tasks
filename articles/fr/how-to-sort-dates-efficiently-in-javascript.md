---
title: Comment trier les dates efficacement en JavaScript
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2025-05-30T13:41:38.871Z'
originalURL: https://freecodecamp.org/news/how-to-sort-dates-efficiently-in-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748612402734/7124a95d-0a33-4ab6-93d2-d94fc354ae12.png
tags:
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: datetime
  slug: datetime
seo_title: Comment trier les dates efficacement en JavaScript
seo_desc: 'Recently, I was working on a PowerApps Component Framework (PCF) project
  that required sorting an array of objects by date. The dates were in ISO 8601 format
  but without a time zone – for example, "2025-05-01T15:00:00.00".

  Without much thought, I wro...'
---

Récemment, je travaillais sur un projet PowerApps Component Framework (PCF) qui nécessitait de trier un tableau d'objets par date. Les dates étaient au format ISO 8601 mais sans fuseau horaire – par exemple, `"2025-05-01T15:00:00.00"`.

Sans trop réfléchir, j'ai écrit quelque chose de similaire à :

```JavaScript
const sorted = data.sort((a, b) => {
  return new Date(a.date) - new Date(b.date);
})
```

Cela fonctionnait bien sur de petits ensembles de données. Mais le tableau que je triais contenait près de **30 000 objets**. Sur une machine de développement rapide, le temps de traitement était d'environ **100–150 ms** – déjà perceptible lorsqu'il est combiné avec d'autres travaux d'interface utilisateur. Lorsque j'ai testé avec **4× CPU throttling** dans le navigateur, le délai a augmenté à près de **400 ms**, ce qui simule plus précisément un appareil bas de gamme. C'est une approche raisonnable pour s'assurer que votre application fonctionne toujours bien pour les utilisateurs sur des machines plus lentes.

Résultats dans le navigateur :

```Bash
sort_with_date_conversion: 397.955078125 ms
```

Sortie avec une réduction de performance de 4x

Dans cet article, vous apprendrez comment trier les dates efficacement en JavaScript. Nous allons passer en revue ce qui rend la méthode ci-dessus inefficace, ainsi qu'un meilleur modèle – surtout lorsque vous traitez de grandes quantités de données.

### Table des matières

1. [Pourquoi 400 ms semblent lents](#heading-pourquoi-400-ms-semblent-lents)

2. [Mise en place de notre expérience](#heading-mise-en-place-de-notre-experience)

3. [Le coût de la conversion de date](#heading-le-cout-de-la-conversion-de-date)

4. [Le superpouvoir lexicographique de l'ISO 8601](#heading-le-superpouvoir-lexicographique-de-liso-8601)

5. [Et si vos dates ne sont pas au format ISO ?](#heading-et-si-vos-dates-ne-sont-pas-au-format-iso)

6. [Points clés à retenir](#heading-points-cles-a-retenir)

## Pourquoi 400 ms *semblent* lents

Selon le classique de Jakob Nielsen, *"Usability Engineering"* (1993), les délais inférieurs à 100 millisecondes sont perçus comme instantanés. Entre 100 ms et 1 000 ms, les utilisateurs commencent à remarquer un décalage – même si cela ne nécessite pas de retour d'interface utilisateur. Dans mon cas, 400 ms semblaient **saccadés**, surtout puisque le composant PCF traitait déjà d'autres tâches. Cela ne allait pas suffire.

## Mise en place de notre expérience

Simulons cela avec une simple expérience qui teste notre tri sous pression. Nous allons créer un tableau de 100 000 dates au format ISO, et **nous allons simuler un ralentissement de performance de 4x dans le navigateur pour tous les scénarios :**

```JavaScript
// Créer un tableau de 100 000 dates au format ISO
const isoArray = [];
let currentDate = new Date(2023, 9, 1); // 1er octobre 2023

for (let i = 0; i < 100000; i++) {
  const year = currentDate.getFullYear();
  const month = String(currentDate.getMonth() + 1).padStart(2, '0');
  const day = String(currentDate.getDate()).padStart(2, '0');

  isoArray.push({ date: `${year}-${month}-${day}`, value: i });
  currentDate.setDate(currentDate.getDate() + 1); // avancer d'un jour
}

// Mélanger le tableau pour simuler une entrée non triée
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

shuffle(isoArray);
```

## Le coût de la conversion de date

Maintenant, trions en utilisant la méthode `new Date()`, où chaque nouvelle date est instanciée directement dans la méthode de tri.

```JavaScript
console.time('sort_with_date_conversion');

// Tri en convertissant chaque chaîne en objet Date à chaque comparaison
const sortedByDate = isoArray.sort((a, b) => {
  return new Date(a.date) - new Date(b.date);
});

console.timeEnd('sort_with_date_conversion');
```

Résultat dans le navigateur :

```Bash
sort_with_date_conversion: 1629.466796875 ms
```

Le tri de 100 000 dates a pris presque 2 secondes.

Presque 2 secondes. Aïe.

## Le superpouvoir lexicographique de l'ISO 8601

Voici la réalisation cruciale : **les chaînes de dates ISO 8601 sont déjà triables lexicographiquement**. Cela signifie que nous pouvons sauter l'objet `Date` entièrement :

```JavaScript
console.time('sort_by_iso_string');

// Comparer les chaînes directement – grâce au format ISO 8601
const sorted = isoArray.sort((a, b) => 
  a.date > b.date ? 1 : -1
);

console.timeEnd('sort_by_iso_string');
console.log(sorted.slice(0, 10));
```

Sortie dans la console :

```Bash
sort_by_iso_string: 10.549072265625 ms
[
  { date: '2023-10-01', value: 0 },
  { date: '2023-10-02', value: 1 },
  { date: '2023-10-03', value: 2 },
  { date: '2023-10-04', value: 3 },
  { date: '2023-10-05', value: 4 },
  { date: '2023-10-06', value: 5 },
  { date: '2023-10-07', value: 6 },
  { date: '2023-10-08', value: 7 },
  { date: '2023-10-09', value: 8 },
  { date: '2023-10-10', value: 9 }
]
```

De 1600 ms à ~10 ms. C'est une accélération de 160x.

Pourquoi est-ce plus rapide ? Parce que l'utilisation de new Date() à l'intérieur de .sort() entraîne la création de deux nouveaux objets Date **par comparaison**. Avec 100 000 éléments et le fonctionnement interne du tri, cela représente **des millions** d'instanciations d'objets. En revanche, lorsque nous trions lexicographiquement, nous trions simplement des chaînes, ce qui est bien moins coûteux.

## Et si vos dates *ne sont pas* au format ISO ?

Supposons que vos dates soient au format `MM/JJ/AAAA`. Ces chaînes ne sont pas triables lexicographiquement, vous devrez donc les transformer d'abord.

### Transformer *puis* trier

```JavaScript
console.time('sort_with_iso_conversion_first');

const sortedByISO = mdyArray
  .map((item) => { // D'abord convertir au format ISO
    const [month, day, year] = item.date.split('/');
    return { date: `${year}-${month}-${day}`, value: item.value };
  })
  .sort((a, b) => (a.date > b.date ? 1 : -1)); // puis trier

console.timeEnd('sort_with_iso_conversion_first');
```

Sortie :

```Bash
sort_with_iso_conversion_first: 58.8779296875 ms
```

Toujours perçu comme instantané.

### Conserver les objets originaux

Si vous souhaitez conserver vos objets originaux (avec des dates non-ISO), vous pouvez utiliser des tuples :

```JavaScript
console.time('sort_and_preserve_original');

// Créer des tuples : [sortableDate, originalObject]
const sortedWithOriginal = mdyArray
  .map((item) => {
    const [month, day, year] = item.date.split('/');
    return [`${year}-${month}-${day}`, item]; // retourner les éléments du tuple
  })
  .sort((a, b) => a[0] > b[0] ? 1 : -1) // trier en fonction du premier élément
  .map(([, item]) => item); // Retourner l'objet original

console.timeEnd('sort_and_preserve_original');
```

Sortie :

```Bash
sort_and_preserve_original: 73.733154296875 ms
```

Toujours dans les limites de ce qui est perçu comme instantané.

Les données originales sont conservées et la performance reste bien dans ce qui est perçu comme instantané.

## Points clés à retenir

* **Évitez la création d'objets à l'intérieur de .sort()**, surtout pour les grands tableaux.

* **Les chaînes ISO 8601 sont triables lexicographiquement.** Utilisez la comparaison de chaînes lorsque vous le pouvez.

* Si vos chaînes de dates ne sont pas triables, **transformez-les d'abord en une forme triable**, triez, et éventuellement transformez-les à nouveau.

* Des ajustements mineurs dans le tri peuvent donner **d'énormes gains de performance** – surtout dans les composants d'interface utilisateur ou les visualisations en temps réel.

**Trouvé cela utile ?** Je travaille à l'intersection du développement low-code et pro-code, en me concentrant sur la création d'applications performantes et en vous aidant à récupérer votre temps grâce à une automatisation réfléchie. Explorez plus sur [scriptedbytes.com](https://scriptedbytes.com).