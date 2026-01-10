---
title: 'Comment commencer : tester une application Ruby-on-Rails / ReactJS avec RSpec,
  Jest et Enzyme'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-03T17:55:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-testing-a-ruby-on-rails-reactjs-app-with-rspec-jest-and-enzyme-d058f415894e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KnkP0HAL3iL6tyTQo7jVZw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Jest
  slug: jest
- name: React
  slug: react
- name: Ruby
  slug: ruby
- name: Testing
  slug: testing
seo_title: 'Comment commencer : tester une application Ruby-on-Rails / ReactJS avec
  RSpec, Jest et Enzyme'
seo_desc: 'By Holly Atkinson

  I recently made a simple ideas board web app using ReactJS, Ruby-on-Rails and PostgreSQL.
  Below, I’ll walk you through the initial steps I took to set up basic unit tests
  for one of the features of my app, adding a new idea.


  _Photo...'
---

Par Holly Atkinson

J'ai récemment créé une application web simple de tableau d'idées en utilisant ReactJS, Ruby-on-Rails et PostgreSQL. Ci-dessous, je vais vous guider à travers les étapes initiales que j'ai suivies pour configurer des tests unitaires de base pour l'une des fonctionnalités de mon application, l'ajout d'une nouvelle idée.

![Image](https://cdn-media-1.freecodecamp.org/images/yToemQSqCMdhO5ADFrrEyf8WwRNFKWl2Zq69)
_Photo par [Unsplash](https://unsplash.com/photos/awU3XEzdU94?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Dan DeAlmeida</a> sur <a href="https://unsplash.com/search/photos/ideas?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Note : Je ne vais pas discuter de la _portée_ des tests dans cet article ; plutôt, mon objectif est de comprendre comment installer certaines des _épendances_ afin de pouvoir commencer à écrire les tests.

### Contexte : configuration du tableau d'idées

J'ai utilisé le gestionnaire de paquets Node pour gérer les dépendances de mon projet. Si vous souhaitez coder en suivant, vous devrez vous assurer d'avoir Node installé sur votre ordinateur.

_Fonctionnalités du projet_

**Dans Rails**

Modèles : Idea

Relations : aucune

**Dans React**

Composants : Navbar, IdeasContainer, Idea

### **Commencer avec RSpec**

J'ai utilisé RSpec pour tester la partie Rails de mon application web de tableau d'idées. Pour commencer :

1. J'ai ajouté la gem 'rspec-rails', '~> 3.8' à mon gemfile.
2. J'ai ensuite exécuté `bundle` dans ma fenêtre de terminal (en m'assurant d'être dans le répertoire Rails).

3. Ensuite, dans mon répertoire Rails, j'ai créé un nouveau dossier appelé `spec`. Et puis, un autre nouveau dossier à l'intérieur de celui-ci appelé `requests`.

4. J'ai créé un nouveau fichier appelé `ideas_spec.rb`. Vous pouvez remplacer le nom `ideas_spec` par le nom du modèle que vous souhaitez tester, en veillant à inclure la partie `_spec` pour indiquer qu'il s'agit d'un fichier de test.

5. En haut de mon fichier ideas_spec.rb, j'ai ajouté le texte suivant :

`require 'rails_helper'`

6. Ensuite, dans le même fichier, j'ai inclus le code décrivant le premier test que je voulais exécuter :

```ruby
describe "ajouter une idée", :type => :request do
  before do
    post '/api/v1/ideas'
  end
  it "retourne un statut créé" do
    expect(response).to have_http_status(201)
  end
end
```

7. Pour exécuter mon test, j'ai tapé `rspec` dans ma fenêtre de terminal, en m'assurant d'être dans mon répertoire de projet rails.

Si vous avez suivi jusqu'ici, RSpec devrait s'exécuter à ce stade et votre premier test devrait réussir !

### **Commencer avec Jest**

J'ai été agréablement surpris de découvrir que le framework de test Jest est inclus avec create-react-app ! Cependant, je voulais également utiliser Enzyme, un utilitaire de test, pour lequel j'ai dû installer certaines dépendances.

1. Pour commencer, j'ai créé un nouveau dossier appelé `_tests_` dans le répertoire `src` de mon application.
2. Dans mon répertoire côté client, j'ai exécuté les commandes suivantes :

```
npm i -D react-test-renderer
```

```
npm install --save-dev jest-enzyme
```

```
npm install --save-dev enzyme enzyme-adapter-react-16
```

3. Pour configurer Enzyme, j'ai créé un fichier dans `src` appelé `setupTests.js` et j'ai inclus ce qui suit :

```js
const Enzyme = require('enzyme');
const EnzymeAdapter = require('enzyme-adapter-react-16');
Enzyme.configure({ adapter: new EnzymeAdapter() });
```

4. À l'intérieur de mon dossier `_tests_`, j'ai créé un nouveau fichier, appelé `App.tests.js`

5. J'ai inclus le texte suivant en haut de ce fichier pour importer mes composants et toutes les fonctionnalités de test que je voulais pour _tous_ mes tests :

```js
import React from 'react';
import App from '../App';
import Idea from '../components/Idea';
import IdeasContainer from '../components/IdeasContainer';
import { create, update } from 'react-test-renderer';
import '../setupTests';
import { shallow, mount, render } from 'enzyme';
import { shallowToJson } from 'enzyme-to-json';
```

6. En dessous, j'ai inclus mon _premier_ test unitaire :

```ruby
describe('Idea', () => {
  it('devrait rendre une nouvelle idée correctement', () => {
    const output = shallow(
      <Idea
      key="mockKey"
      idea={"1", "Test", "Test"}
      onClick={"mockFn"}
      delete={"mockFn2"}
      />
    );
    expect(shallowToJson(output)).toMatchSnapshot();
  });
});
```

7. J'ai exécuté `rails s` dans le répertoire côté serveur et ensuite `npm start` dans le répertoire côté client pour démarrer mon tableau d'idées sur localhost:3001.

8. Pour exécuter mon premier test, j'ai tapé ce qui suit dans ma fenêtre de terminal (en m'assurant d'être dans le répertoire client) :

```
npm run test
```

Si vous avez suivi jusqu'ici, Jest devrait s'exécuter à ce stade, votre test devrait réussir — et vous êtes maintenant dans une excellente position pour écrire plus de tests !

Pour plus d'informations sur le projet de tableau d'idées, mon dépôt peut être trouvé [ici](https://github.com/atkinsonholly/tracr).

Si vous êtes arrivé jusqu'ici, merci d'avoir lu ! J'espère que mon article vous a aidé à commencer à configurer vos tests.