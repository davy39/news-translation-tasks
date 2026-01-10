---
title: Implémentation des Promesses en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-04T19:10:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-promises-in-javascript-1ce2680a7f51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tZ9F-CYdCHLmK9Xsvg0FgA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: promises
  slug: promises
- name: 'tech '
  slug: tech
seo_title: Implémentation des Promesses en JavaScript
seo_desc: 'By Maciej Cieślar

  The thing I love most about programming is the aha! moment when you start to fully
  understand a concept. Even though it might take a long time and no small amount
  of effort to get there, it sure is worth it.

  I think that the most ef...'
---

Par Maciej Cieślar

Ce que j'aime le plus dans la programmation, c'est le moment _aha !_ où l'on commence à comprendre pleinement un concept. Même si cela peut prendre beaucoup de temps et nécessiter des efforts considérables pour y parvenir, cela en vaut vraiment la peine.

Je pense que la manière la plus efficace d'évaluer (et d'aider à améliorer) notre degré de compréhension d'un sujet donné est d'essayer d'appliquer les connaissances au monde réel. Non seulement cela nous permet d'identifier et finalement de corriger nos faiblesses, mais cela peut également éclairer le fonctionnement des choses. Une simple approche d'_essai et erreur_ révèle souvent ces détails qui étaient restés insaisissables auparavant.

Dans cette optique, je crois que l'apprentissage de l'implémentation des **promesses** a été l'un des moments les plus importants de mon parcours en programmation — cela m'a donné une compréhension inestimable du fonctionnement du code asynchrone et m'a rendu meilleur programmeur dans l'ensemble.

J'espère que cet article vous aidera à maîtriser l'implémentation des promesses en JavaScript également.

Nous allons nous concentrer sur la manière d'implémenter le cœur des promesses selon [la spécification Promises/A+](https://promisesaplus.com/) avec quelques méthodes de [l'API Bluebird](http://bluebirdjs.com/docs/api-reference.html). Nous allons également utiliser [l'approche TDD](https://en.wikipedia.org/wiki/Test-driven_development) avec [Jest](https://jestjs.io/).

[TypeScript](https://www.typescriptlang.org/) sera également utile.

Étant donné que nous allons travailler sur les compétences d'implémentation ici, je vais supposer que vous avez une compréhension de base de ce que sont les promesses et une idée vague de leur fonctionnement. Si ce n'est pas le cas, [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) est un excellent point de départ.

Maintenant que cela est réglé, allez-y et clonez le [dépôt](https://github.com/maciejcieslar/promiseq) et commençons.

### Le cœur d'une promesse

Comme vous le savez, une promesse est un objet avec les propriétés suivantes :

#### Then

Une méthode qui attache un gestionnaire à notre promesse. Elle retourne une nouvelle promesse avec la valeur de la précédente mappée par l'une des méthodes du gestionnaire.

#### Handlers

Un tableau de gestionnaires attachés par **then**. Un gestionnaire est un objet contenant deux méthodes **onSuccess** et **onFail**, toutes deux passées en arguments à **then**(**onSuccess**, **onFail**)_._

```typescript
type HandlerOnSuccess<T, U = any> = (value: T) => U | Thenable<U>;
type HandlerOnFail<U = any> = (reason: any) => U | Thenable<U>;

interface Handler<T, U> {
  onSuccess: HandlerOnSuccess<T, U>;
  onFail: HandlerOnFail<U>;
}
```

#### State

Une promesse peut être dans l'un des trois états : **resolved,** **rejected,** ou **pending**.

**Resolved** signifie que tout s'est bien passé et que nous avons reçu notre valeur, ou que nous avons attrapé et géré l'erreur.

**Rejected** signifie que nous avons rejeté la promesse, ou qu'une erreur a été lancée et que nous ne l'avons pas attrapée.

**Pending** signifie que ni la méthode **resolve** ni la méthode **reject** n'a encore été appelée et que nous attendons toujours la valeur.

Le terme « la promesse est réglée » signifie que la promesse est soit résolue, soit rejetée.

#### Value

Une valeur que nous avons soit résolue, soit rejetée.

Une fois la valeur définie, il n'y a aucun moyen de la changer.

### Testing

Selon l'approche TDD, nous voulons écrire nos tests avant que le code réel n'arrive, alors faisons exactement cela.

Voici les tests pour notre cœur :

```typescript
describe('PQ <constructor>', () => {
  test('resolves like a promise', () => {
    return new PQ<number>((resolve) => {
      setTimeout(() => {
        resolve(1);
      }, 30);
    }).then((val) => {
      expect(val).toBe(1);
    });
  });

  test('is always asynchronous', () => {
    const p = new PQ((resolve) => resolve(5));

    expect((p as any).value).not.toBe(5);
  });

  test('resolves with the expected value', () => {
    return new PQ<number>((resolve) => resolve(30)).then((val) => {
      expect(val).toBe(30);
    });
  });

  test('resolves a thenable before calling then', () => {
    return new PQ<number>((resolve) =>
      resolve(new PQ((resolve) => resolve(30))),
    ).then((val) => expect(val).toBe(30));
  });

  test('catches errors (reject)', () => {
    const error = new Error('Hello there');

    return new PQ((resolve, reject) => {
      return reject(error);
    }).catch((err: Error) => {
      expect(err).toBe(error);
    });
  });

  test('catches errors (throw)', () => {
    const error = new Error('General Kenobi!');

    return new PQ(() => {
      throw error;
    }).catch((err) => {
      expect(err).toBe(error);
    });
  });

  test('is not mutable - then returns a new promise', () => {
    const start = new PQ<number>((resolve) => resolve(20));

    return PQ.all([
      start
        .then((val) => {
          expect(val).toBe(20);
          return 30;
        })
        .then((val) => expect(val).toBe(30)),
      start.then((val) => expect(val).toBe(20)),
    ]);
  });
});
```

#### Running our tests

Je recommande vivement d'utiliser [l'extension Jest pour Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest). Elle exécute nos tests en arrière-plan pour nous et nous montre le résultat directement entre les lignes de notre code sous forme de points verts et rouges pour les tests réussis et échoués, respectivement.

Pour voir les résultats, ouvrez la console « Output » et choisissez l'onglet « Jest ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*dr7riPl5ZRkUF8lo)

Nous pouvons également exécuter nos tests en exécutant la commande suivante :

```bash
npm run test
```

Quelle que soit la manière dont nous exécutons les tests, nous pouvons voir que tous reviennent négatifs.

Changeons cela.

### Implémentation du cœur de la promesse

#### constructor

```typescript
class PQ<T> {
  private state: States = States.PENDING;
  private handlers: Handler<T, any>[] = [];
  private value: T | any;
  public static errors = errors;

  public constructor(callback: (resolve: Resolve<T>, reject: Reject) => void) {
    try {
      callback(this.resolve, this.reject);
    } catch (e) {
      this.reject(e);
    }
  }
}
```

Notre constructeur prend un **callback** comme paramètre.

Nous appelons ce callback avec **this.resolve** et **this.reject** comme arguments.

Notez que normalement nous aurions lié **this.resolve** et **this.reject** à **this**, mais ici nous avons utilisé la méthode de flèche de classe à la place.

#### setResult

Maintenant, nous devons définir le résultat. Veuillez vous rappeler que nous devons gérer le résultat correctement, ce qui signifie que, s'il retourne une promesse, nous devons la résoudre d'abord.

```typescript
class PQ<T> {

  // ...
  
  private setResult = (value: T | any, state: States) => {
    const set = () => {
      if (this.state !== States.PENDING) {
        return null;
      }

      if (isThenable(value)) {
        return (value as Thenable<T>).then(this.resolve, this.reject);
      }

      this.value = value;
      this.state = state;

      return this.executeHandlers();
    };

    setTimeout(set, 0);
  };
}
```

Tout d'abord, nous vérifions si l'état n'est pas **pending** — si c'est le cas, alors la promesse est déjà réglée et nous ne pouvons pas lui assigner de nouvelle valeur.

Ensuite, nous devons vérifier si une valeur est un **thenable**. Pour faire simple, un **thenable** est un objet avec **then** comme méthode.

Par convention, un **thenable** devrait se comporter comme une promesse. Donc, afin d'obtenir le résultat, nous allons appeler **then** et passer comme arguments **this.resolve** et **this.reject**.

Une fois que le **thenable** est réglé, il appellera l'une de nos méthodes et nous donnera la valeur non-promise attendue.

Donc maintenant, nous devons vérifier si un objet est un **thenable**.

```typescript
describe('isThenable', () => {
  test('detects objects with a then method', () => {
    expect(isThenable({ then: () => null })).toBe(true);
    expect(isThenable(null)).toBe(false);
    expect(isThenable({})).toBe(false);
  });
});
```

```typescript
const isFunction = (func: any) => typeof func === 'function';

const isObject = (supposedObject: any) =>
  typeof supposedObject === 'object' &&
  supposedObject !== null &&
  !Array.isArray(supposedObject);

const isThenable = (obj: any) => isObject(obj) && isFunction(obj.then);
```

Il est important de réaliser que notre promesse ne sera jamais synchrone, même si le code à l'intérieur du **callback** l'est.

Nous allons retarder l'exécution jusqu'à la prochaine itération de la boucle d'événements en utilisant **setTimeout**.

Maintenant, la seule chose restante à faire est de définir notre valeur et notre statut et ensuite exécuter les gestionnaires enregistrés.

#### executeHandlers

```typescript
class PQ<T> {

  // ...
  
  private executeHandlers = () => {
    if (this.state === States.PENDING) {
      return null;
    }

    this.handlers.forEach((handler) => {
      if (this.state === States.REJECTED) {
        return handler.onFail(this.value);
      }

      return handler.onSuccess(this.value);
    });

    this.handlers = [];
  };
}
```

Encore une fois, assurez-vous que l'état n'est pas **pending**.

L'état de la promesse dicte quelle fonction nous allons utiliser.

Si c'est **resolved**, nous devrions exécuter **onSuccess**, sinon — **onFail**.

Effaçons maintenant notre tableau de gestionnaires juste pour être sûr et ne pas exécuter accidentellement quoi que ce soit à l'avenir. Un gestionnaire peut être attaché et exécuté plus tard de toute façon.

Et c'est ce que nous devons discuter ensuite : une manière d'attacher notre gestionnaire.

#### attachHandler

```typescript
class PQ<T> {

  // ...
  
  private attachHandler = (handler: Handler<T, any>) => {
    this.handlers = [...this.handlers, handler];

    this.executeHandlers();
  };
}
```

C'est vraiment aussi simple que cela en a l'air. Nous ajoutons simplement un gestionnaire à notre tableau de gestionnaires et l'exécutons. C'est tout.

Maintenant, pour tout mettre ensemble, nous devons implémenter la méthode **then**.

#### then

```typescript
class PQ<T> {

  // ...
  
  public then<U>(
    onSuccess?: HandlerOnSuccess<T, U>,
    onFail?: HandlerOnFail<U>,
  ) {
    return new PQ<U | T>((resolve, reject) => {
      return this.attachHandler({
        onSuccess: (result) => {
          if (!onSuccess) {
            return resolve(result);
          }

          try {
            return resolve(onSuccess(result));
          } catch (e) {
            return reject(e);
          }
        },
        onFail: (reason) => {
          if (!onFail) {
            return reject(reason);
          }

          try {
            return resolve(onFail(reason));
          } catch (e) {
            return reject(e);
          }
        },
      });
    });
  }
}
```

Dans **then**, nous retournons une promesse, et dans le **callback** nous attachons un gestionnaire qui est ensuite utilisé pour attendre que la promesse actuelle soit réglée.

Lorsque cela se produit, soit le **onSuccess** soit le **onFail** du gestionnaire sera exécuté et nous procéderons en conséquence.

Une chose à retenir ici est que ni l'un ni l'autre des gestionnaires passés à **then** n'est requis. Il est important, cependant, que nous n'essayions pas d'exécuter quelque chose qui pourrait être **undefined**.

De plus, dans **onFail** lorsque le gestionnaire est passé, nous résolvons en réalité la promesse retournée, car l'erreur a été gérée.

#### catch

**Catch** est en fait juste une abstraction sur la méthode **then**.

```typescript
class PQ<T> {

  // ...
  
  public catch<U>(onFail: HandlerOnFail<U>) {
    return this.then<U>(identity, onFail);
  }
}
```

C'est tout.

#### **_Finally_**

**Finally** est également juste une abstraction sur **then**(**finallyCb**, **finallyCb**), car il ne se soucie pas vraiment du résultat de la promesse.

En fait, il préserve également le résultat de la promesse précédente et le retourne. Donc, peu importe ce qui est retourné par **finallyCb**, cela n'a pas vraiment d'importance.

```typescript
describe('PQ.prototype.finally', () => {
  test('it is called regardless of the promise state', () => {
    let counter = 0;
    return PQ.resolve(15)
      .finally(() => {
        counter += 1;
      })
      .then(() => {
        return PQ.reject(15);
      })
      .then(() => {
        // wont be called
        counter = 1000;
      })
      .finally(() => {
        counter += 1;
      })
      .catch((reason) => {
        expect(reason).toBe(15);
        expect(counter).toBe(2);
      });
  });
});
```

```typescript
class PQ<T> {

  // ...
  

  public finally<U>(cb: Finally<U>) {
    return new PQ<U>((resolve, reject) => {
      let val: U | any;
      let isRejected: boolean;

      return this.then(
        (value) => {
          isRejected = false;
          val = value;
          return cb();
        },
        (reason) => {
          isRejected = true;
          val = reason;
          return cb();
        },
      ).then(() => {
        if (isRejected) {
          return reject(val);
        }

        return resolve(val);
      });
    });
  }
}
```

#### toString

```typescript
describe('PQ.prototype.toString', () => {
  test('returns [object PQ]', () => {
    expect(new PQ<undefined>((resolve) => resolve()).toString()).toBe(
      '[object PQ]',
    );
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public toString() {
    return `[object PQ]`;
  }
}
```

Il retournera simplement une chaîne `[object PQ]`.

Ayant implémenté le cœur de nos promesses, nous pouvons maintenant implémenter certaines des méthodes de l'API Bluebird mentionnées précédemment, ce qui nous facilitera les opérations sur les promesses.

### Méthodes supplémentaires

#### Promise.resolve

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/promise.resolve.html)

```typescript
describe('PQ.resolve', () => {
  test('resolves a value', () => {
    return PQ.resolve(5).then((value) => {
      expect(value).toBe(5);
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public static resolve<U = any>(value?: U | Thenable<U>) {
    return new PQ<U>((resolve) => {
      return resolve(value);
    });
  }
}
```

#### Promise.reject

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/promise.reject.html)

```typescript
describe('PQ.reject', () => {
  test('rejects a value', () => {
    return PQ.reject(5).catch((value) => {
      expect(value).toBe(5);
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public static reject<U>(reason?: any) {
    return new PQ<U>((resolve, reject) => {
      return reject(reason);
    });
  }
}
```

#### Promise.all

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/promise.all.html)

```typescript
describe('PQ.all', () => {
  test('resolves a collection of promises', () => {
    return PQ.all([PQ.resolve(1), PQ.resolve(2), 3]).then((collection) => {
      expect(collection).toEqual([1, 2, 3]);
    });
  });

  test('rejects if one item rejects', () => {
    return PQ.all([PQ.resolve(1), PQ.reject(2)]).catch((reason) => {
      expect(reason).toBe(2);
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public static all<U = any>(collection: (U | Thenable<U>)[]) {
    return new PQ<U[]>((resolve, reject) => {
      if (!Array.isArray(collection)) {
        return reject(new TypeError('An array must be provided.'));
      }

      let counter = collection.length;
      const resolvedCollection: U[] = [];

      const tryResolve = (value: U, index: number) => {
        counter -= 1;
        resolvedCollection[index] = value;

        if (counter !== 0) {
          return null;
        }

        return resolve(resolvedCollection);
      };

      return collection.forEach((item, index) => {
        return PQ.resolve(item)
          .then((value) => {
            return tryResolve(value, index);
          })
          .catch(reject);
      });
    });
  }
}
```

Je crois que l'implémentation est assez simple.

En commençant par **collection.length**, nous comptons à rebours avec chaque **tryResolve** jusqu'à ce que nous arrivions à 0, ce qui signifie que chaque élément de la collection a été résolu. Nous résolvons ensuite la nouvelle collection créée.

#### Promise.any

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/promise.any.html)

```typescript
describe('PQ.any', () => {
  test('resolves the first value', () => {
    return PQ.any<number>([
      PQ.resolve(1),
      new PQ((resolve) => setTimeout(resolve, 15)),
    ]).then((val) => expect(val).toBe(1));
  });

  test('rejects if the first value rejects', () => {
    return PQ.any([
      new PQ((resolve) => setTimeout(resolve, 15)),
      PQ.reject(1),
    ]).catch((reason) => {
      expect(reason).toBe(1);
    });
  });
});
```

```typescript
class PQ<T> {

  // ...

  public static any<U = any>(collection: (U | Thenable<U>)[]) {
    return new PQ<U>((resolve, reject) => {
      return collection.forEach((item) => {
        return PQ.resolve(item)
          .then(resolve)
          .catch(reject);
      });
    });
  }
}
```

Nous attendons simplement que la première valeur soit résolue et la retournons dans une promesse.

#### Promise.props

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/promise.props.html)

```typescript
describe('PQ.props', () => {
  test('resolves object correctly', () => {
    return PQ.props<{ test: number; test2: number }>({
      test: PQ.resolve(1),
      test2: PQ.resolve(2),
    }).then((obj) => {
      return expect(obj).toEqual({ test: 1, test2: 2 });
    });
  });

  test('rejects non objects', () => {
    return PQ.props([]).catch((reason) => {
      expect(reason).toBeInstanceOf(TypeError);
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public static props<U = any>(obj: object) {
    return new PQ<U>((resolve, reject) => {
      if (!isObject(obj)) {
        return reject(new TypeError('An object must be provided.'));
      }

      const resolvedObject = {};

      const keys = Object.keys(obj);
      const resolvedValues = PQ.all<string>(keys.map((key) => obj[key]));

      return resolvedValues
        .then((collection) => {
          return collection.map((value, index) => {
            resolvedObject[keys[index]] = value;
          });
        })
        .then(() => resolve(resolvedObject as U))
        .catch(reject);
    });
  }
}
```

Nous itérons sur les clés de l'objet passé, en résolvant chaque valeur. Nous attribuons ensuite les valeurs au nouvel objet et résolvons une promesse avec celui-ci.

#### Promise.prototype.spread

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/spread.html)

```typescript
describe('PQ.protoype.spread', () => {
  test('spreads arguments', () => {
    return PQ.all<number>([1, 2, 3]).spread((...args) => {
      expect(args).toEqual([1, 2, 3]);
      return 5;
    });
  });

  test('accepts normal value (non collection)', () => {
    return PQ.resolve(1).spread((one) => {
      expect(one).toBe(1);
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public spread<U>(handler: (...args: any[]) => U) {
    return this.then<U>((collection) => {
      if (Array.isArray(collection)) {
        return handler(...collection);
      }

      return handler(collection);
    });
  }
}
```

#### Promise.delay

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/delay.html)

```typescript
describe('PQ.delay', () => {
  test('waits for the given amount of miliseconds before resolving', () => {
    return new PQ<string>((resolve) => {
      setTimeout(() => {
        resolve('timeout');
      }, 50);

      return PQ.delay(40).then(() => resolve('delay'));
    }).then((val) => {
      expect(val).toBe('delay');
    });
  });

  test('waits for the given amount of miliseconds before resolving 2', () => {
    return new PQ<string>((resolve) => {
      setTimeout(() => {
        resolve('timeout');
      }, 50);

      return PQ.delay(60).then(() => resolve('delay'));
    }).then((val) => {
      expect(val).toBe('timeout');
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public static delay(timeInMs: number) {
    return new PQ((resolve) => {
      return setTimeout(resolve, timeInMs);
    });
  }
}
```

En utilisant **setTimeout**, nous retardons simplement l'exécution de la fonction **resolve** du nombre de millisecondes donné.

#### Promise.prototype.timeout

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/timeout.html)

```typescript
describe('PQ.prototype.timeout', () => {
  test('rejects after given timeout', () => {
    return new PQ<number>((resolve) => {
      setTimeout(resolve, 50);
    })
      .timeout(40)
      .catch((reason) => {
        expect(reason).toBeInstanceOf(PQ.errors.TimeoutError);
      });
  });

  test('resolves before given timeout', () => {
    return new PQ<number>((resolve) => {
      setTimeout(() => resolve(500), 500);
    })
      .timeout(600)
      .then((value) => {
        expect(value).toBe(500);
      });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public timeout(timeInMs: number) {
    return new PQ<T>((resolve, reject) => {
      const timeoutCb = () => {
        return reject(new PQ.errors.TimeoutError());
      };

      setTimeout(timeoutCb, timeInMs);

      return this.then(resolve);
    });
  }
}
```

Celle-ci est un peu délicate.

Si le **setTimeout** s'exécute plus rapidement que **then** dans notre promesse, il rejettera la promesse avec notre erreur spéciale.

#### Promise.promisify

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/promise.promisify.html)

```typescript
describe('PQ.promisify', () => {
  test('works', () => {
    const getName = (firstName, lastName, callback) => {
      return callback(null, `${firstName} ${lastName}`);
    };

    const fn = PQ.promisify<string>(getName);
    const firstName = 'Maciej';
    const lastName = 'Cieslar';

    return fn(firstName, lastName).then((value) => {
      return expect(value).toBe(`${firstName} ${lastName}`);
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public static promisify<U = any>(
    fn: (...args: any[]) => void,
    context = null,
  ) {
    return (...args: any[]) => {
      return new PQ<U>((resolve, reject) => {
        return fn.apply(context, [
          ...args,
          (err: any, result: U) => {
            if (err) {
              return reject(err);
            }

            return resolve(result);
          },
        ]);
      });
    };
  }
}
```

Nous appliquons à la fonction tous les arguments passés, plus — comme dernier — nous donnons le **callback** error-first.

#### Promise.promisifyAll

[Comment cela devrait fonctionner.](http://bluebirdjs.com/docs/api/promise.promisifyall.html)

```typescript
describe('PQ.promisifyAll', () => {
  test('promisifies a object', () => {
    const person = {
      name: 'Maciej Cieslar',
      getName(callback) {
        return callback(null, this.name);
      },
    };

    const promisifiedPerson = PQ.promisifyAll<{
      getNameAsync: () => PQ<string>;
    }>(person);

    return promisifiedPerson.getNameAsync().then((name) => {
      expect(name).toBe('Maciej Cieslar');
    });
  });
});
```

```typescript
class PQ<T> {

  // ...
  
  public static promisifyAll<U>(obj: any): U {
    return Object.keys(obj).reduce((result, key) => {
      let prop = obj[key];

      if (isFunction(prop)) {
        prop = PQ.promisify(prop, obj);
      }

      result[`${key}Async`] = prop;

      return result;
    }, {}) as U;
  }
}
```

Nous itérons sur les clés de l'objet et **promisifions** ses méthodes et ajoutons à chaque nom de méthode le mot **Async**.

### Conclusion

Présentées ici n'étaient que quelques-unes parmi toutes les méthodes de l'API Bluebird, donc je vous encourage fortement à explorer, jouer avec et essayer d'implémenter le reste.

Cela peut sembler difficile au début, mais ne vous découragez pas — cela serait sans valeur si c'était facile.

Merci beaucoup d'avoir lu ! J'espère que vous avez trouvé cet article informatif et qu'il vous a aidé à saisir le concept des promesses, et qu'à partir de maintenant, vous vous sentirez plus à l'aise de les utiliser ou simplement d'écrire du code asynchrone.

Si vous avez des questions ou des commentaires, n'hésitez pas à les mettre dans la section des commentaires ci-dessous ou envoyez-moi un [message](https://www.mcieslar.com/contact).

Consultez mes [réseaux sociaux](https://www.maciejcieslar.com/about/) !

[Rejoignez ma newsletter](http://eepurl.com/dAKhxb) !

_Publié à l'origine sur [www.mcieslar.com](https://www.mcieslar.com/implementing-promises-in-javascript) le 4 août 2018._