---
title: Comment écrire des tests pour votre futur vous rendra vos tests meilleurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-20T16:06:42.000Z'
originalURL: https://freecodecamp.org/news/how-writing-tests-for-your-future-self-will-make-your-tests-better-3311a57e07c4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2nJH6LyvnsfIcB3e.
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Comment écrire des tests pour votre futur vous rendra vos tests meilleurs
seo_desc: 'By Eumir Gaspar

  When practicing test driven development (TDD), we sometimes tend to focus on testing
  everything. This 100% coverage mentality can sometimes lead us to overcomplicate
  things.

  Before, I was the one leading the charge to make tests DRY-e...'
---

Par Eumir Gaspar

Lorsque l'on pratique le développement piloté par les tests (TDD), nous avons parfois tendance à nous concentrer sur le test de **tout**. Cette mentalité de couverture à 100 % peut parfois nous amener à compliquer les choses.

Auparavant, j'étais celui qui menait la charge pour rendre les tests plus DRY, car je détestais voir du code répétitif. J'étais nouveau dans la métaprogrammation en Ruby à l'époque, et je voulais toujours simplifier les choses en écrasant le code répétitif et en créant un monstre. En voici un exemple :

```ruby
describe 'quand on reçoit les détails du héros' do
  it 'devrait avoir les clés de premier niveau comme méthodes' do
    top_level_keys = %w{id name gender level paragonLevel hardcore skills items followers stats kills progress dead last-updated}

    top_level_keys.each do |tl_key|
      @my_hero.send(tl_key).must_equal @my_hero.response[tl_key.camelize(:lower)]
    end
  end
```

D'accord, c'était [il y a longtemps en 2012](https://github.com/corroded/covetous/blob/master/spec/covetous/profile/hero_spec.rb#L20-L32). Pour contexte, il s'agissait d'un [Ruby gem](https://rubygems.org/) (similaire à un [package npm](https://www.npmjs.com/)) pour l'API [Diablo 3 de Blizzard](https://dev.battle.net/io-docs). Alors, que testais-je ici ? En lisant le code, cela semble assez simple : il indique que les clés de premier niveau peuvent être des méthodes. Donc, si l'API renvoyait quelque chose comme :

```js
{
  paragonLevel: 10,
  hardcore: true,
  kills: 1234
}
```

Alors, étant donné une instance de héros, je peux simplement les appeler comme des méthodes et cela devrait les retourner comme suit :

```
> hero = Covetous::Profile::Hero.new 'user#1234', '1234'
> hero.paragon_level # 10
> hero.kills # 1234
```

D'accord, je vais être honnête. Lorsque j'écrivais cet article, je parcourais mes anciens projets open source comme exemple et j'ai vu cela. Cela semblait assez simple comme je l'ai dit, mais en l'analysant réellement, j'ai réalisé que c'était bien pire que je ne le pensais. Il m'a fallu quinze minutes pour comprendre ce qu'il fait, même si la spécification dit ce qu'il devrait faire. Avant de taper le bloc ci-dessus, je voulais vérifier que je l'avais bien compris. Bien que je l'aie fait, la manière dont j'ai écrit les tests a tout rendu confus. Pourquoi ?

### Le problème

Comme je l'ai dit, j'étais nouveau dans la métaprogrammation à l'époque et j'ai vu une opportunité de l'utiliser. À cette époque, cela semblait très intelligent, mais maintenant que j'ai plus d'expérience, je sais que faire cela dans les tests est plus un handicap qu'un avantage.

Vous voyez, l'une des choses que j'ai apprises est que **le code de test est un code non testé**. Laissez cela couler un peu.

[**Le code de test est un code non testé.**](https://twitter.com/corrodedlotus/status/982741953308700672)

[**LE CODE DE TEST EST UN CODE NON TESTÉ.**](https://github.com/ericboehs/talk-notes/blob/master/2015-11-15-1040-rubyconf-how-to-stop-hating-your-test-suite.md#test-structre)

Ce sont deux liens différents, soit dit en passant. Cela signifie essentiellement que TOUT code que votre test exécute peut potentiellement avoir ses propres erreurs. Vous n'avez pas réellement de tests pour le code de test, donc il n'y a aucune garantie qu'il fonctionne. La seule garantie que vous pouvez avoir est de faire échouer le test lorsque vous commentez les lignes réelles dans le code et de le faire passer lorsque vous les décommentez. Parfois, cependant, même avec ce test rouge-vert, vous pouvez toujours obtenir des faux positifs. Donc, la meilleure façon d'éviter cela est de garder vos tests **aussi simples que possible** et **aussi explicites que possible**.

Donc, revenons à mon test. Si je me souviens bien, j'ai initialement fait les méthodes une par une. J'ai ensuite vu un motif qui m'a fait penser que ce serait le même motif pour toutes les méthodes au moins, alors pourquoi ne pas rendre le code plus [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) ?

J'ai fait un tableau de toutes les méthodes possibles, j'ai bouclé à travers elles, et j'ai fait une assertion que l'appel de la méthode devrait être le même que de regarder la réponse et d'obtenir la valeur. Assez facile, mais la principale chose qui m'a dérangé était ceci :

```
@my_hero.send(tl_key).must_equal @my_hero.response[tl_key.camelize(:lower)]
```

En Ruby, `send` appelle la chaîne passée comme une méthode. Donc si la valeur de `tl_key` était `paragonLevel` (du tableau), cette ligne dit essentiellement :

```
@my_hero.paragonLevel.must_equal @my_hero.response['paragonLevel']
```

Vous voyez, c'est là que je continue à douter de moi-même. Mon `README` dit que cela devrait être `@my_hero.paragon_level`, mais en regardant le test, ce n'est pas le cas. Qui dois-je croire maintenant ? Mes tests qui passent, ou mon `README` ? C'est la raison exacte pour laquelle la métaprogrammation dans les tests est dangereuse — vous ne savez jamais vraiment si vos tests passent parce qu'ils sont corrects ou parce que vous les avez mal configurés d'une certaine manière. C'est presque la même chose que de NE PAS écrire de tests !

### Faire mieux

Alors, comment réécrirais-je cela ? J'ai depuis appris qu'écrire des tests pour **mon moi de dix ans** suffirait. Cela signifie, moi-même il y a dix ans. Je me demande toujours : « Dans dix ans, serais-je encore capable de comprendre cela, sans contexte ? » Si ce n'est pas le cas, cela signifie que je dois soit écrire une note dans les commentaires, soit mon test est trop compliqué.

Essayons de réécrire cela. Comme je l'ai dit, nous devrions être aussi simples et aussi explicites que possible. Voici une solution :

```
# Étant donné que j'ai interrogé mon héros auprès de l'API :
let(:my_hero) { Covetous::Profile::Hero.new 'corroded-6950', '12345678' }
it 'devrait avoir les clés de premier niveau comme méthodes' do
  expect(my_hero.id).to eq 12345
  expect(my_hero.name).to eq 'corrodeath'
  expect(my_hero.gender).to eq 'female'
  expect(my_hero.level).to eq 70
  ...
end
```

Vous voyez à quel point c'est explicite ? C'est répétitif, c'est sûr, mais dans dix ans, je suis assez sûr que je comprendrai toujours quelles étaient mes attentes. Je n'ai pas à « compiler et interpréter » le code dans mon cerveau. Je lis simplement les spécifications !

De plus, avec cela, je n'ai même pas eu à me rappeler ce que `camelize(:lower)` fait réellement (confession : j'ai dû le chercher en lisant mon ancien code).

Et un autre exemple ? Supposons que nous avons un modèle :

```ruby
class Something < ActiveRecord::Base
  VALID_THINGS = %w(yolo swag)
  OTHER_VALID_THINGS = %w(thing another_thing)
  def valid_things_ids
    where(group: group).pluck(:id)
  end
end
```

Ce qui précède est juste un exemple artificiel basé sur une vraie classe que nous avons dans mon entreprise actuelle. La spécification que j'ai vue était celle-ci :

```ruby
subject(:valid_things_ids) { described_class.valid_things_ids(group) }

let(:group) { 'example' }

before do
  described_class::VALID_THINGS.each do |thing|
    FactoryGirl.create(:something, group: 'example', name: thing)
  end
end

described_class::VALID_THINGS.each do |thing|
  it "contient des choses avec le nom #{thing}" do
    the_thing = described_class.find_by_group_and_name('example', thing)
    expect(valid_things_ids).to include the_thing.id
  end
end
```

D'accord. Premièrement, c'est un test correct, en ce sens que, étant donné un certain nombre de `somethings`, nous pouvons appeler la méthode et elle nous retourne tous les ids de `somethings` avec ce groupe (par exemple, `example`).

Mon problème avec cela, cependant, est de savoir si nous devons tester toutes les choses valides ? Qu'en est-il de `OTHER_VALID_THINGS` ? Si nous voulons tester toutes les valeurs possibles de `VALID_THINGS`, alors nous devrions également tester toutes les valeurs possibles de `OTHER_VALID_THINGS`. Si nous ne voulons PAS tester toutes les valeurs possibles, alors pourquoi utiliser `VALID_THINGS` ? Pourquoi ne pas simplement créer un échantillon aléatoire et prouver que la méthode fonctionne ?

Que diriez-vous de quelque chose comme ceci ?

```ruby
subject(:valid_things_ids) { described_class.valid_things_ids(group) }

let(:group) { 'blurb' }

let!(:random_thing) { FactoryGirl.create(:something, group: 'blurb', id: 111) }
let!(:another_thing) { FactoryGirl.create(:something, group: 'blurb', id: 222) }
let!(:not_included) { FactoryGirl.create(:something, group: 'shrug', id: 333) }

it do
  expect(valid_things_ids).to include 111
  expect(valid_things_ids).to include 222
  expect(valid_things_ids).not_to include 333
end
```

Ici, je crée 3 `somethings` et je leur donne des ids. Je fais en sorte que le troisième ait un groupe différent. Maintenant, si j'exécute la méthode avec `blurb` comme argument, je peux m'attendre à ce qu'elle inclue les deux premiers et pas le dernier.

En le lisant quelques mois plus tard, je ne serai pas confus quant à ce qui est testé puisque c'est simple, et je n'ai même pas à me demander pourquoi je ne teste qu'une certaine partie du code et pas tout.

Notez également l'explicité du test. Je m'attends à ce qu'il inclue les ids `111` et `222`. Normalement, les gens le testeraient comme suit :

```
expect(valid_things_ids).to include random_thing.id
```

Je n'aime pas vraiment ces tests, car ils dépendent toujours du code à ce stade. Si pour une raison quelconque l'id est `nil`, et que le code avait aussi un bug où il retournait `nil`, alors ce test passerait toujours. Pas avec des ids et des attentes explicites, cependant. Bien sûr, il y aura des réserves, mais je pense que je préférerais traiter avec celles-ci plutôt qu'avec l'incertitude des faux positifs possibles.

### Conclusion

Comme vous pouvez le voir à partir des deux exemples ci-dessus, des tests simples à lire vous aideront à long terme. Être très explicite aide beaucoup à comprendre les tests et à avoir moins de bugs.

N'oubliez pas, votre couverture de test à 100 % n'aura pas d'importance si la moitié de ceux-ci sont des faux positifs. Souvenez-vous toujours de votre moi passé lorsque vous testez. Essayez de penser loin dans le futur et demandez-vous ce que signifient vos tests.