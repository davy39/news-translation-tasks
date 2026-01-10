---
title: Limiter les opérations simultanées en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T20:37:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-limit-concurrent-operations-in-javascript-b57d7b80d573
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7F50Qc-ysFgy6tCjUyruTA.jpeg
tags:
- name: concurrency
  slug: concurrency
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Limiter les opérations simultanées en JavaScript
seo_desc: 'By Maciej Cieślar

  Usually, the machine that executes our code has limited resources. Doing everything
  at once might not only hurt, but can also hang our process and make it stop responding
  altogether.

  When we want to crawl 100 websites, we should cra...'
---

Par Maciej Cieślar

Généralement, la machine qui exécute notre code dispose de ressources limitées. Tout faire en même temps peut non seulement nuire, mais aussi bloquer notre processus et le faire cesser de répondre complètement.

Lorsque nous voulons explorer 100 sites web, nous devrions en explorer, par exemple, 5 à la fois, afin de ne pas utiliser toute la bande passante disponible. Dès qu'un site web est exploré, le suivant est prêt à être traité.

En général, toutes les opérations "lourdes" doivent être réparties dans le temps. Elles ne doivent pas être exécutées toutes en même temps, pour de meilleures performances et pour économiser des ressources.

### Installation

Si vous êtes familier avec mon précédent article sur [l'implémentation des promesses](https://medium.freecodecamp.org/how-to-implement-promises-in-javascript-1ce2680a7f51), vous allez remarquer de nombreuses similitudes.

```typescript
class Concurrently<T = any> {
  private tasksQueue: (() => Promise<T>)[] = [];
  private tasksActiveCount: number = 0;
  private tasksLimit: number;

  public constructor(tasksLimit: number) {
    if (tasksLimit < 0) {
      throw new Error('La limite ne peut pas être inférieure à 0.');
    }

    this.tasksLimit = tasksLimit;
  }

  private registerTask(handler) {
    this.tasksQueue = [...this.tasksQueue, handler];
    this.executeTasks();
  }

  private executeTasks() {
    while (this.tasksQueue.length && this.tasksActiveCount < this.tasksLimit) {
      const task = this.tasksQueue[0];
      this.tasksQueue = this.tasksQueue.slice(1);
      this.tasksActiveCount += 1;

      task()
        .then((result) => {
          this.tasksActiveCount -= 1;
          this.executeTasks();

          return result;
        })
        .catch((err) => {
          this.tasksActiveCount -= 1;
          this.executeTasks();

          throw err;
        });
    }
  }

  public task(handler: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) =>
      this.registerTask(() =>
        handler()
          .then(resolve)
          .catch(reject),
      ),
    );
  }
}

export default Concurrently;
```

Nous enregistrons une tâche donnée en l'ajoutant à notre _tasksQueue_ puis nous appelons _executeTasks_.

Maintenant, nous exécutons autant de tâches que notre limite nous le permet — une par une. Chaque fois en ajoutant 1 à notre compteur appelé _tasksActiveCount_.

Lorsque la tâche exécutée se termine, nous retirons 1 de _tasksActiveCount_ et appelons à nouveau _executeTasks_.

Ci-dessous, nous pouvons voir un exemple de son fonctionnement.

La limite est fixée à 3. Les deux premières tâches prennent très longtemps à être traitées. Nous pouvons voir le troisième "slot" s'ouvrir de temps en temps, permettant à la tâche suivante dans la file d'attente d'être exécutée.

Il y a toujours trois tâches, ni plus, ni moins.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MxACL9-7TXYJTpUTQdJIHQ.gif)
_Exécution de tâches lourdes et légères avec une limite de 3._

Vous pouvez voir le code dans le [dépôt](https://github.com/maciejcieslar/concurrently).

Merci beaucoup d'avoir lu ! Pouvez-vous penser à une autre façon d'atteindre le même effet ? Partagez-les ci-dessous.

Si vous avez des questions ou des commentaires, n'hésitez pas à les mettre dans la section des commentaires ci-dessous ou envoyez-moi un [message](https://www.mcieslar.com/contact).

Consultez mes [réseaux sociaux](https://www.maciejcieslar.com/about/) !

[Rejoignez ma newsletter](http://eepurl.com/dAKhxb) !

_Publié à l'origine sur [www.mcieslar.com](https://www.mcieslar.com/limiting-concurrent-operations-in-javascript) le 28 août 2018._