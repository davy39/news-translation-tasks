---
title: Comment partitionner les files d'attente pour les charges de travail distribuées
subtitle: ''
author: Okoye Chukwuebuka Victor
co_authors: []
series: null
date: '2024-05-23T20:57:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-partition-queues-for-distributed-workloads
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Networks-small.jpeg
tags:
- name: distributed systems
  slug: distributed-systems
- name: queue
  slug: queue
seo_title: Comment partitionner les files d'attente pour les charges de travail distribuées
seo_desc: "Technology, like human lives, evolves, and with this evolution comes the\
  \ use of better solutions to existing problems. You might wonder: does this complicate\
  \ systems or make them more efficient? \nIn this article, we will discuss some measures\
  \ you can..."
---

La technologie, comme les vies humaines, évolue, et avec cette évolution viennent de meilleures solutions aux problèmes existants. Vous pourriez vous demander : cela complique-t-il les systèmes ou les rend-il plus efficaces ?

Dans cet article, nous allons discuter de certaines mesures que vous pouvez prendre pour rendre les systèmes beaucoup plus efficaces et fiables.

## Qu'est-ce qu'un système distribué ?

De manière très simple, un système distribué est un groupe ou une collection de nœuds informatiques indépendants connectés via une unité centrale qui partagent et utilisent des ressources de calcul.

Imaginez cela comme un réseau de systèmes qui peuvent interagir et partager des tâches qu'ils peuvent traiter collectivement comme une seule unité. Par conséquent, les charges de travail distribuées font référence aux processus ou tâches qui s'exécutent dans ces systèmes.

Pour que ces systèmes interagissent efficacement, vous pouvez utiliser certains protocoles ou conceptions. L'un d'eux est une file d'attente, que vous apprendrez dans la section suivante.

## Qu'est-ce qu'une file d'attente ?

Une file d'attente est une structure de données qui modélise le principe Premier-Entré-Premier-Sorti (FIFO).

Pour comprendre cela, imaginez un poste de caisse dans un supermarché. La première personne à rejoindre la file sera la première à être servie. Ensuite, la personne suivante est servie. C'est à peu près ainsi que fonctionnent les files d'attente, mais maintenant en tant que structure de données, ce qui est traité peut être différents événements ou messages que nous identifierons comme des charges de travail.

Typiquement, dans un système de file d'attente, vous avez le _producteur_ et le _consommateur_. Le producteur est le service qui envoie un événement ou, dans ce contexte, une charge de travail dans la file d'attente. Et le consommateur est le service qui écoute et le traite.

![Une image montrant un Producteur, une File d'attente et un Consommateur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1716417641517/d81577d0-d57a-457b-b92f-817481a7b863.png)
_Optimisation des flux de travail : les producteurs alimentent la file d'attente, les consommateurs traitent le flux._

Avec la nature même de ces systèmes, l'exécution de files d'attente sur ce réseau peut être exigeante et parfois vous devez faire face à certains défis qui seront discutés brièvement.

## **Défis des files d'attente** de **longue durée** dans un **système distribué**

L'objectif d'une file d'attente de tâches est principalement de gérer efficacement les tâches asynchrones ou de longue durée.

Cependant, dans le contexte des systèmes distribués, l'exécution de charges de travail sur un réseau peut parfois s'avérer difficile car elles deviennent accablantes pour ces files d'attente. Cela peut entraîner des problèmes tels que les suivants :

* **Augmentation de la latence du réseau** : Les systèmes distribués reposent principalement sur les communications via les réseaux pour coordonner efficacement les charges de travail sur les différents nœuds informatiques. Les tâches retardées ou de longue durée peuvent entraîner des temps de réponse imprévisibles (latence).
* **Difficulté de suivi et de surveillance** : Il peut devenir très complexe de suivre chaque charge de travail, surtout maintenant qu'elles sont partagées entre différents systèmes en cours d'exécution sur le réseau. Pour gérer efficacement celles-ci, vous devrez utiliser des outils spécialisés tels que la pile ELK.
* **Coordination distribuée** : S'assurer que les charges de travail transmises à différentes files d'attente sur le réseau sont exécutées correctement et dans l'ordre où elles devraient l'être est un défi. Le manque de cette coordination entraîne davantage d'incohérences de données.
* **Tolérance aux pannes et résilience** : Les processus s'exécutant dans un système distribué devront certainement faire face à des points de rupture et à des défaillances de nœuds. Avoir des charges de travail dans des files d'attente de longue durée peut augmenter ces points de défaillance, ce qui peut entraîner une augmentation des arriérés de files d'attente, une perte de données ou une incohérence.

La question est de savoir comment combattre au mieux ces problèmes, ou quelles mesures prendre pour réduire la possibilité de défaillances du système ou d'incohérences de données. Une approche pour résoudre cela est d'utiliser des files d'attente de tâches partitionnées.

## Que signifie partitionner une file d'attente ?

Le partitionnement peut être défini comme la division d'un composant en sous-sections plus petites. En utilisant cela, vous pouvez dériver une définition pour le partitionnement de file d'attente comme la division d'un système de file d'attente en parties plus petites et plus gérables pour décharger les charges de travail de manière plus rapide et plus efficace.

Imaginez une file d'attente centralisée avec diverses charges de travail arrivant avec différents types de tâches ou même des priorités.

Lorsque le trafic ou les charges de travail sont à un taux très élevé, cette file d'attente finira par être submergée et continuera à accumuler des arriérés.

Pour soulager le fardeau, vous pouvez diviser la file d'attente en différentes parties pour gérer différents types de tâches. Par exemple, vous pouvez avoir une file d'attente pour gérer les tâches prioritaires ou même pour traiter différents types d'événements, comme les notifications.

![Une image montrant des Clients (Producteurs) utilisant une technique d'équilibrage de charge pour assigner des charges de travail aux files d'attente et ensuite des travailleurs traitant les charges de travail.](https://cdn.hashnode.com/res/hashnode/image/upload/v1716416776358/32a2fd40-6c2f-4d9e-8031-f32a356cc6e3.png)
_Files d'attente partitionnées dans les systèmes distribués : Optimisation de la gestion des charges de travail entre les nœuds._

L'objectif principal du partitionnement d'une file d'attente est d'améliorer les performances du système et de réduire les temps d'arrêt ou les incohérences de données. Pour ce faire, vous devez examiner différentes stratégies de partitionnement des files d'attente afin de connaître celle qui convient le mieux à votre système.

## Stratégies efficaces de partitionnement des files d'attente de tâches

Il existe diverses façons de diviser une file d'attente en sous-sections, mais pour le faire efficacement, vous pouvez employer certaines stratégies testées telles que le partitionnement basé sur la plage, le partitionnement basé sur le hachage, etc.

### Partitionnement basé sur le hachage

Cette forme de partitionnement permet la sélection d'une file d'attente à l'aide d'une valeur de hachage assignée.

Tout d'abord, un paramètre dans la charge de travail est utilisé pour obtenir une valeur de hachage. Ensuite, vous prenez le _modulo_ de cette valeur avec le nombre de partitions (files d'attente), ce qui donne un index de partition. Cet index est ensuite utilisé pour déterminer la file d'attente à laquelle la tâche sera assignée.

```javascript
const numPartitions = 4;

const queues = Array.from({ length: numPartitions }, (_, i) => ({
    name: `Queue ${i + 1}`,
    partitionIndex: i + 1,
}));

function getPartitionIndex(hash) {
    const partitionIndex = hash % numPartitions;
    return partitionIndex + 1;
}

function hashCode(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
        const char = str.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
    }
    return Math.abs(hash);
}

const tasks = [
    { id: 1, value: "Emails Task" },
    { id: 2, value: "Transactions Tasks"},
    { id: 3, value: "Orders Tasks" },
    { id: 4, value: "Update Tasks" },
];

tasks.forEach(task => {
    const hash = hashCode(task.value);
    const partitionIndex = getPartitionIndex(hash);
    const assignedQueue = queues.find(queue => queue.partitionIndex === partitionIndex);
    console.log(`Task with ID: ${task.id} (content: ${task.value}) assigned to ${assignedQueue ? assignedQueue.name : "no queue"}`);
});
```

L'exemple ci-dessus implique le hachage d'une valeur ou d'un champ particulier dans la charge de travail ou l'événement à assigner. Dans ce cas, le champ de contenu a été haché, et sa valeur de hachage a ensuite été utilisée pour déterminer à quelle file d'attente la charge de travail sera assignée. Cette valeur de hachage peut sembler aléatoire, mais en vérité, elle est constante, ce qui signifie que la même entrée produira toujours la même valeur de hachage.

```bash
Task with ID: 1 (content: Emails Task) assigned to Queue 3
Task with ID: 2 (content: Transactions Tasks) assigned to Queue 4
Task with ID: 3 (content: Orders Tasks) assigned to Queue 4
Task with ID: 4 (content: Update Tasks) assigned to Queue 2
```

En voyant la sortie, si vous deviez changer le contenu de l'une de ces tâches, vous verrez qu'elles obtiendront une autre valeur de hachage et pourraient être assignées à une file d'attente différente.

Dans un scénario réel, si vous voulez que les charges de travail soient distribuées parmi différentes files d'attente, vous devez vous assurer que la valeur de hachage est quelque chose d'unique parmi les tâches, comme son identifiant. Vous pouvez utiliser un UUID.

### **Partitionnement basé sur la plage**

Cette stratégie vous permet de répartir les tâches ou les charges de travail provenant d'une charge de travail centralisée en sous-sections en fonction d'une plage d'identifiants de tâches. Par exemple, la file d'attente A peut ne permettre qu'un identifiant de tâche qui se situe dans la plage de 1 à 50, tandis que la file d'attente B gère la tâche avec un identifiant allant de 51 à 100.

Cette stratégie garantit que les tâches sont distribuées dans chaque partition afin d'utiliser efficacement les ressources disponibles et de s'assurer que les charges de travail sont distribuées.

Jetez un coup d'œil à cet exemple de code ci-dessous qui montre comment les tâches sont assignées à une partition en fonction de la plage dans laquelle leurs identifiants se situent :

```javascript
const { v4: uuidv4 } = require("uuid");

const numPartitions = 4;
const partitionRanges = Array.from({ length: numPartitions }, (_, i) => ({
    start: i * 250,
    end: (i + 1) * 250,
}));

const queues = Array.from({ length: numPartitions }, (_, i) => ({
    name: `Queue ${i + 1}`,
    partitionIndex: i + 1,
}));

function getPartitionIndex(hash) {
    return Math.floor(hash / 250) + 1;
}

const hashCode = (str) => {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
        const char = str.charCodeAt(i);
        hash = (hash << 5) - hash + char;
    }
    return Math.abs(hash) % 1000;
};

const tasks = Array.from({ length: 4 }, () => ({ id: uuidv4() }));

tasks.forEach((task) => {
    const hash = Math.abs(hashCode(task.id));
    const partitionIndex = getPartitionIndex(hash);
    const assignedQueue = queues.find(
        (queue) => queue.partitionIndex === partitionIndex,
    );
    console.log(
        `Task with ID: ${task.id} assigned to ${assignedQueue ? assignedQueue.name : "no queue"}`,
    );
});

```

Dans cet exemple de code, le `taskId` est un UUID. Pour les faire correspondre à une plage de file d'attente partitionnée (chaque file d'attente a une plage de 250), vous commencez par les hacher et ensuite les convertir en une valeur absolue.

Ensuite, vous appelez la fonction `PartitionIndex()` avec cette valeur de hachage.

À partir de là, elle trouve la file d'attente partitionnée dans laquelle le `taskId` s'inscrit dans la plage.

Voici un exemple de sortie ci-dessous :

```bash
Task with ID: 493fbf04-2f4f-43c0-9486-f5c99313d4e6 assigned to Queue 2
Task with ID: 9bad272f-3369-408e-bb37-5ef00c68b0b6 assigned to Queue 3
Task with ID: e0ec2d06-d66b-4e0e-8e85-04e4755a42be assigned to Queue 1
Task with ID: 960f415b-2e64-4169-b4ee-59b11c33b451 assigned to Queue 4
```

### **Partitionnement Round-Robin**

Pour cette stratégie de partitionnement, les tâches sont assignées aux files d'attente selon un motif cyclique. Cela signifie que si une tâche est assignée à la file d'attente 1, la tâche suivante sera assignée à la file d'attente 2, jusqu'à ce que toutes les files d'attente reçoivent une tâche avant de recommencer à partir de la file d'attente 1, ce qui permet une distribution équilibrée entre les files d'attente.

```javascript
const numPartitions = 4;
let currentPartition = 0;

function getRoundRobinPartitionIndex() {
    const partitionIndex = (currentPartition % numPartitions) + 1;
    currentPartition++;
    return partitionIndex;
}

const tasks = [1, 2, 3, 4, 5]; 
tasks.forEach(task => {
    const partitionIndex = getRoundRobinPartitionIndex();
    console.log(`Task with ID: ${task} assigned to Queue ${partitionIndex}`);
});
```

Pour cet exemple, une fonction `getRoundRobinPartitionIndex()` a été définie et elle détermine l'index de la file d'attente suivante en utilisant une stratégie round-robin.

Elle calcule d'abord l'index de la file d'attente en prenant la valeur modulaire de `currentPartition` et `numPartitions`. Elle ajoute 1 pour s'assurer que l'index initial commence à 1, puis incrémente le `currentPartition` pour s'assurer que la file d'attente suivante à assigner est supérieure à la précédente. Si la valeur modulaire est 0, elle revient à la file d'attente avec l'index 1.

```bash
Task with ID: 1 assigned to Queue 1
Task with ID: 2 assigned to Queue 2
Task with ID: 3 assigned to Queue 3
Task with ID: 4 assigned to Queue 4
Task with ID: 5 assigned to Queue 1
```

Comme vous pouvez le voir, la sortie ci-dessus montre que les tâches ont été distribuées à chacune des files d'attente, puis ont recommencé à partir de la première file d'attente.

### Partitionnement dynamique

Ce type de stratégie de partitionnement implique l'assignation de tâches aux files d'attente en fonction des charges de travail changeantes ou des conditions du système.

Par exemple, un système a 3 files d'attente actives et 1 qui est libre. Il vérifie celle qui a le moins de tâches assignées et lui assigne une nouvelle tâche. En faisant cela, il s'assure que les files d'attente ne sont pas submergées et que les ressources du système sont utilisées efficacement.

```javascript
const { v4: uuidv4 } = require('uuid');
let numPartitions = 4;
let queues = Array.from({ length: numPartitions }, (_, i) => ({
    name: `Queue ${i + 1}`,
    tasks: [],
}));

function dynamicPartitioning(task) {
    let minLoadQueue = queues[0];
    for (let queue of queues) {
        if (queue.tasks.length < minLoadQueue.tasks.length) {
            minLoadQueue = queue;
        }
    }
    minLoadQueue.tasks.push(task);
    console.log(`Task with ID: ${task.id} assigned to ${minLoadQueue.name}`);
}

const tasks = Array.from({ length: 5 }, () => ({ id: uuidv4(), value: `Task content` }));

tasks.forEach(task => {
    dynamicPartitioning(task);
});

function addPartition() {
    numPartitions++;
    queues.push({ name: `Queue ${numPartitions}`, tasks: [] });
    console.log(`Added new partition: Queue ${numPartitions}`);
}

setTimeout(() => {
    addPartition();
    // Assign new tasks to demonstrate dynamic partitioning with the new queue
    const newTasks = Array.from({ length: 5 }, () => ({ id: uuidv4(), value: `New task content` }));
    newTasks.forEach(task => {
        dynamicPartitioning(task);
    });
}, 5000);
```

Dans ce code ci-dessus, il commence par créer trois files d'attente et assigne dynamiquement des tâches à la file d'attente la moins chargée.

Après un délai simulé, une nouvelle file d'attente est ajoutée pour gérer la charge de travail accrue et de nouvelles obligations sont distribuées parmi toutes les files d'attente disponibles.

Cette technique garantit que la charge est équilibrée entre toutes les files d'attente, et que la file d'attente n'est pas surchargée, rendant la machine plus efficace et réactive aux ajustements de la charge de travail.

```bash
Task with ID: 396d4fde-830b-4443-b59b-c089f3a1db49 assigned to Queue 1
Task with ID: aa85af19-e46a-4b13-9a9c-2eb3ec535af0 assigned to Queue 2
Task with ID: f93d4cbb-0cad-4b71-a424-4c27a77ed38a assigned to Queue 3
Task with ID: c7e0cc7e-f055-4a38-9869-466406a33ca8 assigned to Queue 4
Task with ID: b49fe153-73e8-45d1-85b3-a5873f836dc9 assigned to Queue 1
Added new partition: Queue 5
Task with ID: a8a5f78e-da7e-4c65-9d74-8cef57f271f3 assigned to Queue 5
Task with ID: 00ce47b0-6098-49d6-ad06-820733ffe16e assigned to Queue 2
Task with ID: 7b1a5dcf-c42c-46dc-8e29-bae1cc5408c1 assigned to Queue 3
Task with ID: 3e31ad34-1a19-4d3c-a8f3-08f765a45f13 assigned to Queue 4
Task with ID: 73d55243-27da-44a4-9192-532a20889373 assigned to Queue 5
```

Il existe d'autres stratégies, comme le partitionnement basé sur le contenu, le partitionnement aléatoire ou même un type personnalisé défini par l'utilisateur.

Toutes ces stratégies sont bonnes mais peuvent encore poser certains problèmes si elles ne sont pas correctement gérées.

Par exemple, si vous utilisez la stratégie de partitionnement basée sur la plage et que vous sélectionnez un identifiant qui se situe dans la plage définie d'une file d'attente, cette partition de file d'attente finira par être submergée. Il vous appartient de déterminer celle qui convient le mieux aux exigences de votre système.

## Conclusion

Le traitement des charges de travail dans les systèmes distribués peut être complexe et inefficace s'il n'est pas correctement géré.

Le partitionnement des files d'attente dans le système et la distribution des charges de travail entre elles en fonction d'une stratégie est un moyen d'améliorer les performances de votre système.

Dans cet article, certains défis liés aux files d'attente de longue durée ont été soulignés, et certaines stratégies pour les atténuer ont été données. J'ai fait des recherches sur les systèmes distribués dans les environnements d'exécution et les bases de données, et c'était l'une de mes découvertes.

J'espère que vous avez apprécié la lecture de cet article, car j'ai apprécié l'écrire. Vous pouvez me suivre sur [Twitter(X)](https://x.com/OkoyeVictorr).