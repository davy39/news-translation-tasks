---
title: Implémentation de Async et Await avec des Générateurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T10:54:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-async-and-await-with-generators-11ab0859010f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9wHrewC1Dyf2Au_qEqwWcg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Implémentation de Async et Await avec des Générateurs
seo_desc: 'By Maciej Cieślar

  Nowadays we can write our asynchronous code in a synchronous way thanks to the async
  and await keywords. This makes it easier to read and understand. Recently I wondered,
  however, how the same effect could be achieved without using ...'
---

Par Maciej Cieślar

De nos jours, nous pouvons écrire notre code asynchrone de manière synchrone grâce aux mots-clés **async** et **await**. Cela rend le code plus facile à lire et à comprendre. Récemment, je me suis demandé comment obtenir le même effet sans utiliser ces mots-clés.

Il s'avère que c'est assez simple, car le comportement de **async** et **await** peut facilement être émulé en utilisant des générateurs. Jetons un coup d'œil !

Allez-y, clonez le [dépôt](https://github.com/maciejcieslar/asynq) et commençons.

### Générateurs

Je vais supposer que vous avez peu ou pas d'expérience avec les générateurs, car, honnêtement, la plupart du temps, ils ne sont pas particulièrement utiles et vous pouvez facilement vous en passer. Alors ne vous inquiétez pas — nous allons commencer par un rapide rappel.

Les générateurs sont des objets créés par des [fonctions génératrices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) — des fonctions avec un _*_ (astérisque) à côté de leur nom.

Ces générateurs ont une capacité incroyable qui nous permet d'arrêter l'exécution du code — quand nous le voulons — en utilisant le mot-clé **yield**.

Considérez cet exemple :

```javascript
const generator = (function*() {
  // en attente de .next()
  const a = yield 5;
  // en attente de .next()
  console.log(a); // => 15
})();

console.log(generator.next()); // => { done: false, value: 5 }
console.log(generator.next(15)); // => { done: true, value: undefined }
```

Étant donné que ce sont des bases absolues, je vous recommande, avant de faire défiler plus loin, de lire [cet article](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators) pour comprendre ce qui se passe vraiment ici.

Si vous pensez avoir une bonne compréhension des idées sous-jacentes, nous pouvons continuer.

### Attendez une minute

Ne vous êtes-vous jamais demandé comment **await** fonctionne vraiment ?

D'une manière ou d'une autre, il attend simplement que notre promesse retourne une valeur et poursuit l'exécution. Pour moi, cela semble être quelque chose qu'un générateur pourrait faire après quelques ajustements.

Ce que nous pourrions faire, c'est prendre chaque valeur retournée par **yield**, la mettre dans une promesse, puis attendre que la promesse soit résolue. Ensuite, nous la retournons simplement au générateur en appelant _generator.next(resolvedValue)._

Cela semble être un bon plan. Mais d'abord, écrivons quelques tests pour être sûr que tout fonctionne comme prévu.

Ce que notre fonction **asynq** devrait faire :

* attendre que le code asynchrone se termine avant de continuer l'exécution
* retourner une **promesse** avec la valeur retournée par la fonction
* faire fonctionner **try/catch** sur le code asynchrone

Note : parce que nous utilisons des générateurs, notre **await** devient **yield**.

```typescript
import { asynq } from '../src';

describe('asynq core', () => {
  test('Attend les valeurs (comme await le fait)', () => {
    return asynq(function*() {
      const a = yield Promise.resolve('a');
      expect(a).toBe('a');
    });
  });

  test('Attrape les erreurs', () => {
    return asynq(function*() {
      const err = new Error('Hello there');

      try {
        const a = yield Promise.resolve('a');
        expect(a).toBe('a');

        const b = yield Promise.resolve('b');
        expect(b).toBe('b');

        const c = yield Promise.reject(err);
      } catch (error) {
        expect(error).toBe(err);
      }

      const a = yield Promise.resolve(123);
      expect(a).toBe(123);
    });
  });

  test('Termine la fonction si l\'erreur n\'est pas capturée', () => {
    const err = new Error('General Kenobi!');

    return asynq(function*() {
      const a = yield Promise.reject(err);
      const b = yield Promise.resolve('b');
    }).catch((error) => {
      expect(error).toBe(err);
    });
  });

  test('Retourne une promesse avec la valeur retournée', () => {
    return asynq(function*() {
      const value = yield Promise.resolve(5);
      expect(value).toBe(5);

      return value;
    }).then((value) => {
      expect(value).toBe(5);
    });
  });
});
```

Très bien, super ! Maintenant nous pouvons parler de l'implémentation.

Notre fonction **asynq** prend en paramètre une fonction génératrice — en l'appelant, nous créons un générateur.

Pour être sûr, nous appelons [_isGeneratorLike_](https://github.com/maciejcieslar/asynq/blob/master/src/utils.ts) qui vérifie si la valeur reçue est un objet et a les méthodes **next** et **throw**.

Ensuite, de manière récursive, nous consommons chaque mot-clé **yield** en appelant _generator.next(ensuredValue)_. Nous attendons que la promesse retournée soit résolue, puis nous retournons son résultat au générateur en répétant tout le processus.

Nous devons également attacher le gestionnaire **catch**, afin que, si la fonction lance une exception, nous puissions l'attraper et retourner l'exception à l'intérieur de la fonction en appelant _generator.throw(error)_.

Maintenant, toute erreur potentielle sera gérée par **catch**. Si il n'y avait pas de bloc **try/catch** en place, une erreur arrêterait simplement l'exécution — comme le ferait toute exception non gérée — et notre fonction retournerait une promesse rejetée.

Lorsque le générateur a terminé, nous retournons la valeur de retour du générateur dans une promesse.

```typescript
import { isGeneratorLike } from './utils';

type GeneratorFactory = () => IterableIterator<any>;

function asynq(generatorFactory: GeneratorFactory): Promise<any> {
  const generator = generatorFactory();

  if (!isGeneratorLike(generator)) {
    return Promise.reject(
      new Error('La fonction fournie doit retourner un générateur.'),
    );
  }

  return (function resolve(result) {
    if (result.done) {
      return Promise.resolve(result.value);
    }

    return Promise.resolve(result.value)
      .then((ensuredValue) => resolve(generator.next(ensuredValue)))
      .catch((error) => resolve(generator.throw(error)));
  })(generator.next());
}
```

Maintenant, après avoir exécuté nos tests, nous pouvons voir que tout fonctionne comme prévu.

### Conclusion

Bien que cette implémentation ne soit probablement pas celle utilisée dans les moteurs JavaScript, il est gratifiant de pouvoir faire quelque chose comme cela par nous-mêmes.

N'hésitez pas à parcourir le code à nouveau. Plus vous comprendrez les idées sous-jacentes, plus vous pourrez apprécier le génie des créateurs des mots-clés **async** et **await**.

Merci beaucoup d'avoir lu ! J'espère que vous avez trouvé cet article informatif. J'espère également qu'il vous a aidé à voir qu'il n'y a pas de magie impliquée dans les mots-clés **async** et **await**, et qu'ils peuvent facilement être remplacés par des générateurs.

Si vous avez des questions ou des commentaires, n'hésitez pas à les mettre dans la section des commentaires ci-dessous ou à m'envoyer un [message](https://www.mcieslar.com/contact).

Consultez mes [réseaux sociaux](https://www.maciejcieslar.com/about/) !

[Rejoignez ma newsletter](http://eepurl.com/dAKhxb) !

_Publié à l'origine sur [www.mcieslar.com](https://www.mcieslar.com/implementing-async-and-await-with-generators) le 6 août 2018._