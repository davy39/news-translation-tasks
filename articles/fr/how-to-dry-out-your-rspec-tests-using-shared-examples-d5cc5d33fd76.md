---
title: Comment assécher vos tests RSpec en utilisant des exemples partagés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-04T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-dry-out-your-rspec-tests-using-shared-examples-d5cc5d33fd76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5Cb4TjFan4h4eM3JsCqrbA.jpeg
tags:
- name: '#rspec'
  slug: rspec
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: TDD (Test-driven development)
  slug: tdd
- name: Web Development
  slug: web-development
seo_title: Comment assécher vos tests RSpec en utilisant des exemples partagés
seo_desc: 'By Parth Modi


  “Give me six hours to chop down a tree and I will spend the first four sharpening
  the axe.” — Abraham Lincoln


  When I refactored a project a few weeks ago, I spent most of my time writing specs.
  After writing several similar test cases...'
---

Par Parth Modi

> _Donnez-moi six heures pour abattre un arbre et je passerai les quatre premières à aiguiser la hache.  Abraham Lincoln_

Lorsque j'ai refactorisé un projet il y a quelques semaines, j'ai passé la plupart de mon temps à écrire des spécifications. Après avoir écrit plusieurs cas de test similaires pour certaines API, j'ai commencé à me demander si je pourrais me débarrasser de beaucoup de cette duplication.

J'ai donc plongé dans la lecture des meilleures pratiques pour assécher les tests (Don't Repeat Yourself). Et c'est ainsi que j'ai découvert les `exemples partagés` et les `contexte partagés`.

Dans mon cas, j'ai fini par utiliser des exemples partagés. Et voici ce que j'ai appris jusqu'à présent en les appliquant.

Lorsque vous avez plusieurs spécifications qui décrivent un comportement similaire, il peut être préférable d'extraire les exemples redondants dans des `exemples partagés` et de les utiliser dans plusieurs spécifications.

Supposons que vous avez deux modèles _User_ et _Post_, et qu'un utilisateur peut avoir plusieurs posts. Les utilisateurs doivent pouvoir voir la liste des utilisateurs et des posts. Créer une action index dans les contrôleurs des utilisateurs et des posts servira cet objectif.

Tout d'abord, écrivez des spécifications pour votre action index pour le contrôleur des utilisateurs. Elle aura la responsabilité de récupérer les utilisateurs et de les rendre avec la mise en page appropriée. Ensuite, écrivez suffisamment de code pour faire passer les tests.

```
# users_controller_spec.rb
describe "GET #index" do  before do     5.times do      FactoryGirl.create(:user)     end    get :index  end  it {  expect(subject).to respond_with(:ok) }  it {  expect(subject).to render_template(:index) }  it {  expect(assigns(:users)).to match(User.all) }end
```

```
# users_controller.rb
class UsersController < ApplicationController  ....  def index    @users = User.all  end  ....end
```

Typiquement, l'action index de n'importe quel contrôleur récupère et agrège des données à partir de quelques ressources selon les besoins. Elle ajoute également la pagination, la recherche, le tri, le filtrage et la portée.

Enfin, toutes ces données sont présentées aux vues via HTML, JSON ou XML en utilisant des API. Pour simplifier mon exemple, les actions index des contrôleurs se contenteront de récupérer des données, puis de les afficher via des vues.

Il en va de même pour l'action index dans le contrôleur des posts :

```
describe "GET #index" do   before do     5.times do      FactoryGirl.create(:post)    end    get :index  end  it {  expect(subject).to respond_with(:ok) }  it {  expect(subject).to render_template(:index) }  it {  expect(assigns(:posts)).to match(Post.all) }end
```

```
# posts_controller.rb
class PostsController < ApplicationController  ....  def index    @posts = Post.all  end  ....end
```

Les tests RSpec écrits pour les contrôleurs des utilisateurs et des posts sont très similaires. Dans les deux contrôleurs, nous avons :

* Le code de réponse  doit être OK
* Les deux actions index doivent rendre le partial ou la vue appropriée  dans notre cas `index`
* Les données que nous voulons rendre, telles que les posts ou les utilisateurs

Asséchons les spécifications pour notre action index en utilisant des `exemples partagés`.

### Où placer vos exemples partagés

J'aime placer les exemples partagés dans le répertoire _specs/support/shared_examples_ afin que tous les fichiers liés aux `exemples partagés` soient chargés automatiquement.

Vous pouvez lire sur d'autres conventions couramment utilisées pour localiser vos `exemples partagés` ici : [documentation des exemples partagés](https://www.relishapp.com/rspec/rspec-core/docs/example-groups/shared-examples)

### Comment définir un exemple partagé

Votre action index doit répondre avec le code de succès 200 (OK) et rendre votre template index.

```
RSpec.shared_examples "index examples" do   it { expect(subject).to respond_with(:ok) }  it { expect(subject).to render_template(:index) }end
```

En plus de vos blocs `it`  et avant et après vos hooks  vous pouvez ajouter des blocs `let`, des contextes et des blocs describe, qui peuvent également être définis à l'intérieur des `exemples partagés`.

Je préfère personnellement garder les exemples partagés simples et concis, et je n'ajoute pas de contextes et de blocs let. Le bloc `exemples partagés` accepte également des paramètres, que je couvrirai ci-dessous.

### Comment utiliser les exemples partagés

Ajouter `include_examples "index examples"` à vos spécifications de contrôleurs d'utilisateurs et de posts inclut index examples à vos tests.

```
# users_controller_spec.rb
describe "GET #index" do  before do     5.times do      FactoryGirl.create(:user)     end    get :index  end  include_examples "index examples"  it {  expect(assigns(:users)).to match(User.all) }end
```

```
# de même, dans posts_controller_spec.rb
describe "GET #index" do  before do     5.times do      FactoryGirl.create(:post)     end    get :index  end  include_examples "index examples"  it {  expect(assigns(:posts)).to match(Post.all) }end
```

Vous pouvez également utiliser `it_behaves_like` ou `it_should_behaves_like` au lieu de `include_examples` dans ce cas. `it_behaves_like` et `it_should_behaves_like` sont en fait des alias et fonctionnent de la même manière, ils peuvent donc être utilisés de manière interchangeable. Mais `include_examples` et `it_behaves_like` sont différents.

Comme indiqué dans la documentation officielle :

* `include_examples`  inclut des exemples dans le contexte actuel
* `it_behaves_like` et `it_should_behave_like` incluent les exemples dans un contexte imbriqué

#### Pourquoi cette distinction est-elle importante ?

La documentation de RSpec donne une réponse appropriée :

> _Lorsque vous incluez des exemples paramétrés dans le contexte actuel plusieurs fois, vous pouvez remplacer les définitions de méthodes précédentes et la dernière déclaration l'emporte._

Ainsi, lorsque vous êtes confronté à une situation où des exemples paramétrés contiennent des méthodes qui entrent en conflit avec d'autres méthodes dans le même contexte, vous pouvez remplacer `include_examples` par la méthode `it_behaves_like`. Cela créera un contexte imbriqué et évitera ce genre de situations.

Consultez la ligne suivante dans vos spécifications de contrôleur d'utilisateurs et de posts :

```
it { expect(assigns(:users)).to match(User.all) }it { expect(assigns(:posts)).to match(Post.all) }
```

Maintenant, vos spécifications de contrôleur peuvent être refactorisées davantage en passant des paramètres à l'exemple partagé comme suit :

```
# specs/support/shared_examples/index_examples.rb
```

```
# ici assigned_resource et resource_class sont des paramètres passés au bloc index examples RSpec.shared_examples "index examples" do |assigned_resource, resource_class|   it { expect(subject).to respond_with(:ok) }  it { expect(subject).to render_template(:index) }  it {  expect(assigns(assigned_resource)).to match(resource_class.all)   }end
```

Maintenant, apportez les modifications suivantes à vos spécifications de contrôleurs d'utilisateurs et de posts :

```
# users_controller_spec.rb
describe "GET #index" do  before do     ...  end  include_examples "index examples", :users, User.allend
```

```
# posts_controller_spec.rb
describe "GET #index" do  before do     ...  end  include_examples "index examples", :posts, Post.allend
```

Maintenant, les spécifications des contrôleurs semblent propres, moins redondantes et surtout, DRY. De plus, ces exemples d'index peuvent servir de structures de base pour concevoir l'action index d'autres contrôleurs.

### Conclusion

En déplaçant les exemples communs dans un fichier séparé, vous pouvez éliminer la duplication et améliorer la cohérence de vos actions de contrôleur dans toute votre application. Cela est très utile dans le cas de la conception d'API, car vous pouvez utiliser la structure existante des tests RSpec pour concevoir des tests et créer des API qui adhèrent à votre structure de réponse commune.

La plupart du temps, lorsque je travaille avec des API, j'utilise des `exemples partagés` pour me fournir une structure commune afin de concevoir des API similaires.

N'hésitez pas à partager comment vous asséchez vos spécifications en utilisant des `exemples partagés`.