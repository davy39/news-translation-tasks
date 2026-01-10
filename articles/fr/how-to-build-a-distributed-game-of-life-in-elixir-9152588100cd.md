---
title: Comment construire un Jeu de la Vie distribué en Elixir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-17T17:14:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-distributed-game-of-life-in-elixir-9152588100cd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*AfpCKR3o8T1Ie-Eq.png
tags:
- name: Elixir
  slug: elixir
- name: Erlang
  slug: erlang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Comment construire un Jeu de la Vie distribué en Elixir
seo_desc: 'By Artur Trzop

  I wrote my first game in Elixir. It is a popular thing — Conway’s Game of Life —
  but it gets quite interesting when you solve it in a functional language, especially
  when you can see how the actor model works and how actors are distrib...'
---

Par Artur Trzop

J'ai écrit mon premier jeu en Elixir. Il s'agit d'un grand classique — le Jeu de la Vie de Conway — mais cela devient très intéressant quand on le résout dans un langage fonctionnel, surtout quand on peut voir [comment fonctionne le modèle d'acteur](https://en.wikipedia.org/wiki/Actor_model) et comment les acteurs sont distribués sur les serveurs du réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/3Snl82uCosun4TAqGggHfSKVUng0YPUzFheF)
_Jeu de la Vie_

**Dans cet article de blog, je vais montrer :**

* comment écrire les règles du jeu de la vie avec des tests en Elixir,
* des tâches parallèles à travers des processus légers (acteurs) afin d'utiliser tous les cœurs du CPU,
* comment distribuer le travail sur plusieurs nœuds afin que le jeu puisse être exécuté par de nombreux serveurs dans le cluster,
* comment utiliser le comportement GenServer, TaskSupervisor et les Agents en Elixir.

Ce projet et le [code source complet peuvent être trouvés ici](https://github.com/BeyondScheme/elixir-game_of_life).

### Démo

Commençons par regarder une courte démo du fonctionnement du jeu.

[**GameOfLife**](https://asciinema.org/a/44233)   
[_Enregistré par ArturT_asciinema.org](https://asciinema.org/a/44233)

Comme vous pouvez le voir, le nœud 1 représente le jeu en cours et le plateau à l'écran. Le second nœud a également été démarré et connecté au premier. Depuis le second nœud, nous avons ajouté de nouvelles cellules au plateau. Les deux nœuds sont responsables du traitement du jeu, mais seul le premier nœud est le nœud principal détenant les informations sur l'état actuel du jeu. Nous pouvons connecter plus de nœuds au cluster afin que le traitement du jeu puisse se faire sur tous les nœuds. Vous allez apprendre dans cet article comment réaliser cela.

### Règles du Jeu de la Vie

Si vous connaissez déjà [le problème du jeu de la vie](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), passez directement à [l'en-tête suivant](https://beyondscheme.com/2016/distributed-game-of-life-in-elixir#creer-une-nouvelle-application-en-elixir). Sinon, dans cette section, vous pouvez apprendre le concept de base.

L'univers du Jeu de la Vie est une grille orthogonale bidimensionnelle infinie de cellules carrées, chacune d'entre elles étant dans l'un des deux états possibles, vivante ou morte. Chaque cellule interagit avec ses huit voisins, qui sont les cellules adjacentes horizontalement, verticalement ou diagonalement. À chaque étape temporelle, les transitions suivantes se produisent :

* Toute cellule vivante avec moins de deux voisins vivants meurt, comme par sous-population.
* Toute cellule vivante avec deux ou trois voisins vivants survit jusqu'à la génération suivante.
* Toute cellule vivante avec plus de trois voisins vivants meurt, comme par surpopulation.
* Toute cellule morte avec exactement trois voisins vivants devient une cellule vivante, comme par reproduction.

Le motif initial constitue la graine du système. La première génération est créée en appliquant les règles ci-dessus simultanément à chaque cellule de la graine — les naissances et les décès se produisent simultanément, et le moment discret auquel cela se produit est parfois appelé un tick (en d'autres termes, chaque génération est une fonction pure de la précédente). Les règles continuent d'être appliquées de manière répétée pour créer les générations suivantes.

### Créer une nouvelle application en Elixir

Tout d'abord, nous allons créer une nouvelle application Elixir OTP avec un arbre de supervision. Nous utiliserons un superviseur pour notre serveur de jeu, vous en apprendrez plus à ce sujet un peu plus tard.

```
$ mix new --sup game_of_life
```

L'option `--sup` est donnée pour générer un squelette d'application OTP incluant un arbre de supervision. Normalement, une application est générée sans superviseur et sans le callback d'application.

Dans le fichier `lib/game_of_life.ex`, vous trouverez un exemple de la façon d'ajouter un worker enfant au superviseur.

```elixir
# lib/game_of_life.ex
defmodule GameOfLife do
  use Application

  # Voir http://elixir-lang.org/docs/stable/elixir/Application.html
  # pour plus d'informations sur les applications OTP
  def start(_type, _args) do
    import Supervisor.Spec, warn: false

    children = [
      # Définir les workers et les superviseurs enfants à superviser
      # worker(GameOfLife.Worker, [arg1, arg2, arg3]),
    ]

    # Voir http://elixir-lang.org/docs/stable/elixir/Supervisor.html
    # pour d'autres stratégies et options supportées
    opts = [strategy: :one_for_one, name: GameOfLife.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

### Représenter le plateau dans le Jeu de la Vie

Nous devons représenter les cellules vivantes sur le plateau de notre jeu. Une seule cellule peut être un tuple `{x, y}` avec des coordonnées dans le plateau bidimensionnel.

Toutes les cellules vivantes sur le plateau seront dans la liste `alive_cells`.

```elixir
alive_cells = [{0, 0}, {1, 0}, {2, 0}, {1, 1}, {-1,-2}]
```

Voici un exemple de ce à quoi ressemble ce plateau avec des cellules vivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/j2utgQIL1-t1HTIR9smp5jEtsfDIbsOkS1ZE)
_Plateau avec des cellules vivantes_

et voici les coordonnées x & y correspondantes :

![Image](https://cdn-media-1.freecodecamp.org/images/FNNnkZazIb8gyyR0vg5F9R4kiXVKAUXDUx9D)
_Coordonnées des cellules vivantes_

Maintenant que nous avons une idée de la façon dont nous allons stocker nos cellules vivantes, nous pouvons passer à l'écriture du code.

### Règles du Jeu de la Vie avec des tests

Nous pouvons créer le module `GameOfLife.Cell` avec la fonction `keep_alive?/2` responsable de déterminer si une cellule vivante particulière `{x, y}` doit rester vivante à la génération suivante ou non.

Voici la fonction avec les arguments attendus :

```elixir
# lib/game_of_life/cell.ex
defmodule GameOfLife.Cell do
  def keep_alive?(alive_cells, {x, y} = _alive_cell) do
    # TODO
  end
end
```

Écrivons quelques tests pour couvrir la première exigence du Jeu de la Vie :

> Toute cellule vivante avec moins de deux voisins vivants meurt, comme par sous-population.

Nous avons écrit des tests pour nous assurer que la fonction `GameOfLife.Cell.keep_alive?/2` retourne false dans le cas où la cellule vivante n'a pas de voisins ou n'en a qu'un seul.

```elixir
# test/game_of_life/cell_test.exs
defmodule GameOfLife.CellTest do
  use ExUnit.Case, async: true

  test "une cellule vivante sans voisins meurt" do
    alive_cell = {1, 1}
    alive_cells = [alive_cell]
    refute GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)
  end

  test "une cellule vivante avec 1 voisin meurt" do
    alive_cell = {1, 1}
    alive_cells = [alive_cell, {0, 0}]
    refute GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)
  end
end
```

La fonction `GameOfLife.Cell.keep_alive?/2` doit retourner false juste pour passer nos tests, alors ajoutons plus de tests pour couvrir les autres exigences.

> Toute cellule vivante avec plus de trois voisins vivants meurt, comme par surpopulation.

```elixir
# test/game_of_life/cell_test.exs
test "une cellule vivante avec plus de 3 voisins meurt" do
  alive_cell = {1, 1}
  alive_cells = [alive_cell, {0, 0}, {1, 0}, {2, 0}, {2, 1}]
  refute GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)
end
```

> _Toute cellule vivante avec deux ou trois voisins vivants survit jusqu'à la génération suivante._

```elixir
# test/game_of_life/cell_test.exs
test "une cellule vivante avec 2 voisins survit" do
  alive_cell = {1, 1}
  alive_cells = [alive_cell, {0, 0}, {1, 0}]
  assert GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)
end

test "une cellule vivante avec 3 voisins survit" do
  alive_cell = {1, 1}
  alive_cells = [alive_cell, {0, 0}, {1, 0}, {2, 1}]
  assert GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)
end
```

Maintenant, nous pouvons implémenter notre fonction `GameOfLife.Cell.keep_alive?/2`.

```elixir
# lib/game_of_life/cell.ex
defmodule GameOfLife.Cell do
  def keep_alive?(alive_cells, {x, y} = _alive_cell) do
    case count_neighbours(alive_cells, x, y, 0) do
      2 -> true
      3 -> true
      _ -> false
    end
  end

  defp count_neighbours([head_cell | tail_cells], x, y, count) do
    increment = case head_cell do
      {hx, hy} when hx == x - 1 and hy == y - 1 -> 1
      {hx, hy} when hx == x     and hy == y - 1 -> 1
      {hx, hy} when hx == x + 1 and hy == y - 1 -> 1
      {hx, hy} when hx == x - 1 and hy == y     -> 1
      {hx, hy} when hx == x + 1 and hy == y     -> 1
      {hx, hy} when hx == x - 1 and hy == y + 1 -> 1
      {hx, hy} when hx == x     and hy == y + 1 -> 1
      {hx, hy} when hx == x + 1 and hy == y + 1 -> 1
      _not_neighbour -> 0
    end
    count_neighbours(tail_cells, x, y, count + increment)
  end

  defp count_neighbours([], _x, _y, count), do: count
end
```

Comme vous pouvez le voir, nous avons implémenté la fonction privée `count_neighbours/4` responsable du comptage des voisins. Elle sera utile pour respecter la règle suivante.

Il y a une autre exigence que nous avons oubliée :

> Toute cellule morte avec exactement trois voisins vivants devient une cellule vivante, comme par reproduction.

Nous allons écrire une nouvelle fonction `GameOfLife.Cell.become_alive?/2` attendant les coordonnées de la cellule morte et retournant si la cellule morte doit devenir vivante ou non.

```elixir
# lib/game_of_life/cell.ex
defmodule GameOfLife.Cell do
  def become_alive?(alive_cells, {x, y} = _dead_cell) do
    3 == count_neighbours(alive_cells, x, y, 0)
  end
end
```

Et voici le test pour cela :

```elixir
# test/game_of_life/cell_test.exs
test "une cellule morte avec trois voisins vivants devient une cellule vivante" do
  alive_cells = [{2, 2}, {1, 0}, {2, 1}]
  dead_cell = {1, 1}
  assert GameOfLife.Cell.become_alive?(alive_cells, dead_cell)
end

test "une cellule morte avec deux voisins vivants reste morte" do
  alive_cells = [{2, 2}, {1, 0}]
  dead_cell = {1, 1}
  refute GameOfLife.Cell.become_alive?(alive_cells, dead_cell)
end
```

Il y a une autre chose qui pourrait nous être utile. Nous avons la liste des cellules vivantes mais nous ne savons pas grand-chose sur les cellules mortes. Le nombre de cellules mortes est infini, nous devons donc réduire le nombre de cellules mortes pour lesquelles nous voulons vérifier si elles doivent devenir vivantes. Un moyen simple serait de ne vérifier que les cellules mortes ayant des voisins vivants. D'où la fonction `GameOfLife.Cell.dead_neighbours/1`.

Écrivons d'abord quelques tests :

```elixir
# test/game_of_life/cell_test.exs
test "trouver les cellules mortes (voisins d'une cellule vivante)" do
  alive_cells = [{1, 1}]
  dead_neighbours = GameOfLife.Cell.dead_neighbours(alive_cells) |> Enum.sort
  expected_dead_neighbours = [
    {0, 0}, {1, 0}, {2, 0},
    {0, 1}, {2, 1},
    {0, 2}, {1, 2}, {2, 2}
  ] |> Enum.sort
  assert dead_neighbours == expected_dead_neighbours
end

test "trouver les cellules mortes (voisins de plusieurs cellules vivantes)" do
  alive_cells = [{1, 1}, {2, 1}]
  dead_neighbours = GameOfLife.Cell.dead_neighbours(alive_cells) |> Enum.sort
  expected_dead_neighbours = [
    {0, 0}, {1, 0}, {2, 0}, {3, 0},
    {0, 1}, {3, 1},
    {0, 2}, {1, 2}, {2, 2}, {3, 2}
  ] |> Enum.sort
  assert dead_neighbours == expected_dead_neighbours
end
```

et voici la fonction implémentée :

```elixir
# lib/game_of_life/cell.ex
def dead_neighbours(alive_cells) do
  neighbours = neighbours(alive_cells, [])
  (neighbours |> Enum.uniq) -- alive_cells
end

defp neighbours([{x, y} | cells], neighbours) do
  neighbours(cells, neighbours ++ [
    {x - 1, y - 1}, {x    , y - 1}, {x + 1, y - 1},
    {x - 1, y    }, {x + 1, y    },
    {x - 1, y + 1}, {x    , y + 1}, {x + 1, y + 1}
  ])
end

defp neighbours([], neighbours), do: neighbours
```

Fondamentalement, ce sont toutes les règles implémentées dans le module unique `GameOfLife.Cell`. Vous pouvez voir le [fichier du module](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/lib/game_of_life/cell.ex) complet avec les [tests sur GitHub](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/test/game_of_life/cell_test.exs).

### L'architecture du Jeu de la Vie distribué

![Image](https://cdn-media-1.freecodecamp.org/images/BIrpLZBjGimv4-HlBQQt9UslBgNwam3Pr0bC)
_L'architecture du Jeu de la Vie distribué en Elixir_

Notre superviseur principal est `GameOfLife.Supervisor` que j'ai mentionné au début de l'article. Ci-dessous, vous pouvez voir comment nous avons défini ses enfants comme `Task.Supervisor`, les workers pour `BoardServer` et `GamePrinter`.

```elixir
# lib/game_of_life.ex
defmodule GameOfLife do
  use Application

  # Voir http://elixir-lang.org/docs/stable/elixir/Application.html
  # pour plus d'informations sur les applications OTP
  def start(_type, _args) do
    import Supervisor.Spec, warn: false
    init_alive_cells = []
    children = [
      # Définir les workers et les superviseurs enfants à superviser
      # worker(GameOfLife.Worker, [arg1, arg2, arg3]),
      supervisor(Task.Supervisor, [[name: GameOfLife.TaskSupervisor]]),
      worker(GameOfLife.BoardServer, [init_alive_cells]),
      # Nous décommenterons cette ligne plus tard
      # worker(GameOfLife.GamePrinter, []),
    ]

    # Voir http://elixir-lang.org/docs/stable/elixir/Supervisor.html
    # pour d'autres stratégies et options supportées
    opts = [strategy: :one_for_one, name: GameOfLife.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

Laissez-moi décrire la responsabilité de chaque composant sur l'image.

`Task.Supervisor` est un module Elixir définissant un nouveau superviseur qui peut être utilisé pour superviser dynamiquement des tâches. Nous allons l'utiliser pour lancer des tâches comme déterminer si une cellule particulière doit vivre ou mourir. Ces tâches peuvent être exécutées sur les nœuds connectés au cluster.

Dans le code ci-dessus, nous avons donné le nom `GameOfLife.TaskSupervisor` à notre superviseur. Nous utiliserons ce nom pour indiquer à la fonction `Task.Supervisor.async` quel Task Supervisor doit gérer notre tâche. Vous pouvez en savoir plus sur [Task.Supervisor ici](http://elixir-lang.org/docs/stable/elixir/Task.Supervisor.html).

`GameOfLife.BoardServer` est notre module implémenté comme un [comportement GenServer](http://elixir-lang.org/docs/stable/elixir/GenServer.html). Il est responsable de la conservation de l'état du jeu. Par là, je veux dire qu'il garde la liste des cellules vivantes sur le plateau ainsi que le compteur de génération et le TRef. TRef est une référence de timer retournée par le [module timer d'Erlang](http://erlang.org/doc/man/timer.html) et la fonction [apply_interval](http://erlang.org/doc/man/timer.html#apply_interval-4).

Nous voulons démarrer le jeu et générer une nouvelle liste de cellules vivantes pour la génération suivante avec un intervalle de temps spécifié. À chaque nouvelle génération, nous mettrons à jour le compteur de génération. L'autre chose intéressante est que `GameOfLife.BoardServer` ne s'exécute que sur un seul nœud. Une fois qu'un autre nœud est connecté au cluster où s'exécute déjà `GameOfLife.BoardServer`, alors `GameOfLife.BoardServer` ne sera pas démarré tel quel sur le nœud nouvellement connecté.

Au lieu de cela, sur le nouveau nœud, `GameOfLife.BoardServer` ne gardera que la référence au PID du processus existant sur le premier nœud. Nous voulons avoir une source unique de vérité sur l'état de notre jeu dans un processus `GameOfLife.BoardServer` primaire existant sur le premier nœud démarré dans le cluster.

`GameOfLife.GamePrinter` est un module simple utilisant [Agent](http://elixir-lang.org/docs/stable/elixir/Agent.html) afin de conserver le TRef (référence temporelle) pour que nous puissions imprimer le plateau sur STDOUT avec l'intervalle spécifié. Nous utiliserons le [module timer d'Erlang](http://erlang.org/doc/man/timer.html#apply_interval-4) pour imprimer le plateau à l'écran chaque seconde.

Vous vous demandez peut-être quelle est la différence entre GenServer et Agent.

Un GenServer est un processus comme n'importe quel autre processus Elixir et il peut être utilisé pour conserver l'état, exécuter du code de manière asynchrone, etc. L'avantage d'utiliser un processus serveur générique (GenServer) est qu'il disposera d'un ensemble standard de fonctions d'interface et inclura des fonctionnalités pour le traçage et le rapport d'erreurs. Il s'intègre également dans un arbre de supervision, comme nous l'avons fait dans le module `GameOfLife`.

D'un autre côté, Agent est une solution beaucoup plus simple que GenServer. Les Agents sont une simple abstraction autour de l'état. Souvent en Elixir, il est nécessaire de partager ou de stocker un état qui doit être accessible depuis différents processus ou par le même processus à différents moments. Le module Agent fournit une implémentation de serveur de base qui permet de récupérer et de mettre à jour l'état via une API simple. C'est ce que nous allons faire dans `GameOfLife.GamePrinter` car nous n'avons besoin que de garder la référence temporelle de notre intervalle de timer.

### Créer un gestionnaire de nœuds pour le superviseur de tâches

Commençons par quelque chose de simple juste pour voir si nous pouvons distribuer le travail sur les nœuds du cluster. Nous supposons que chaque nouveau processus créé par le superviseur de tâches sera assigné aléatoirement à l'un des nœuds connectés. Chaque nœud devrait être également chargé, en supposant que chaque tâche est assez similaire et que tous les nœuds sont des machines avec la même configuration et la même charge.

```elixir
# lib/game_of_life/node_manager.ex
defmodule GameOfLife.NodeManager do
  def all_nodes do
    [Node.self | Node.list]
  end

  def random_node do
    all_nodes |> Enum.random
  end
end
```

Notre gestionnaire de nœuds possède la fonction `random_node/0` qui retourne le nom d'un nœud aléatoire connecté au cluster. Fondamentalement, c'est tout. Une solution simple devrait suffire pour l'instant.

### Créer des fonctions d'aide pour le plateau

Nous avons besoin de quelques fonctions d'aide pour les opérations que nous pouvons effectuer sur le plateau, comme l'ajout et la suppression de cellules. Commençons par les tests pour le module `GameOfLife.Board` et la fonction `add_cells/2`.

```elixir
# test/game_of_life/board_test.exs
defmodule GameOfLife.BoardTest do
  use ExUnit.Case, async: true

  test "ajouter de nouvelles cellules aux cellules vivantes sans doublons" do
    alive_cells = [{1, 1}, {2, 2}]
    new_cells = [{0, 0}, {1, 1}]
    actual_alive_cells = GameOfLife.Board.add_cells(alive_cells, new_cells)
                          |> Enum.sort
    expected_alive_cells = [{0, 0}, {1, 1}, {2, 2}]
    assert actual_alive_cells == expected_alive_cells
  end
end
```

Nous devons nous assurer que nous ne permettrons pas d'ajouter deux fois la même cellule au plateau, nous testons donc qu'il n'y a pas de doublons. Voici l'implémentation de la fonction `add_cells/2` :

```elixir
# lib/game_of_life/board.ex
defmodule GameOfLife.Board do
  def add_cells(alive_cells, new_cells) do
    alive_cells ++ new_cells
    |> Enum.uniq
  end
end
```

Une autre chose est la suppression de cellules de la liste des cellules vivantes :

```elixir
# test/game_of_life/board_test.exs
test "supprimer les cellules qui doivent être tuées des cellules vivantes" do
  alive_cells = [{1, 1}, {4, -2}, {2, 2}, {2, 1}]
  kill_cells = [{1, 1}, {2, 2}]
  actual_alive_cells = GameOfLife.Board.remove_cells(alive_cells, kill_cells)
  expected_alive_cells = [{4, -2}, {2, 1}]
  assert actual_alive_cells == expected_alive_cells
end
```

L'implémentation est super simple :

```elixir
# lib/game_of_life/board.ex
def remove_cells(alive_cells, kill_cells) do
  alive_cells -- kill_cells
end
```

Créons quelque chose de plus avancé. Nous devrions déterminer quelles cellules doivent encore vivre à la génération suivante après le tick. Voici un test pour la fonction `GameOfLife.Board.keep_alive_tick/1` :

```elixir
# test/game_of_life/board_test.exs
test "une cellule vivante avec 2 voisins survit jusqu'à la génération suivante" do
  alive_cells = [{0, 0}, {1, 0}, {2, 0}]
  expected_alive_cells = [{1, 0}]
  assert GameOfLife.Board.keep_alive_tick(alive_cells) == expected_alive_cells
end
```

La fonction `keep_alive_tick` fait quelques choses comme créer une nouvelle tâche avec `Task.Supervisor` pour chaque cellule vivante. Les tâches seront créées sur les nœuds disponibles dans le cluster. Nous calculons si les cellules vivantes doivent rester vivantes ou être supprimées. La fonction `keep_alive_or_nilify/2` retourne la cellule si elle doit vivre ou `nil` sinon.

Nous attendons avec `Task.await/1` que toutes les tâches sur tous les nœuds aient terminé leur travail. Les tâches travaillent en parallèle mais nous devons attendre les résultats de chaque tâche. Nous supprimons de la liste les valeurs `nil` afin qu'à la fin nous ne nous retrouvions qu'avec les cellules vivantes pour la génération suivante.

```elixir
# lib/game_of_life/board.ex
@doc "Retourne les cellules qui doivent encore vivre à la génération suivante"
def keep_alive_tick(alive_cells) do
  alive_cells
  |> Enum.map(&(Task.Supervisor.async(
                {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},
                GameOfLife.Board, :keep_alive_or_nilify, [alive_cells, &1])))
  |> Enum.map(&Task.await/1)
  |> remove_nil_cells
end

def keep_alive_or_nilify(alive_cells, cell) do
  if GameOfLife.Cell.keep_alive?(alive_cells, cell), do: cell, else: nil
end

defp remove_nil_cells(cells) do
  cells
  |> Enum.filter(fn cell -> cell != nil end)
end
```

Il y a un cas de plus que nous devrions gérer, c'est la situation où des cellules mortes doivent devenir vivantes. La fonction `GameOfLife.Board.become_alive_tick/1` sera responsable de cela.

```elixir
# test/game_of_life/board_test.exs
test "une cellule morte avec trois voisins vivants devient une cellule vivante" do
  alive_cells = [{0, 0}, {1, 0}, {2, 0}, {1, 1}]
  born_cells = GameOfLife.Board.become_alive_tick(alive_cells)
  expected_born_cells = [{1, -1}, {0, 1}, {2, 1}]
  assert born_cells == expected_born_cells
end
```

Voici à quoi ressemble notre fonction :

```elixir
# lib/game_of_life/board.ex
@doc "Retourne les nouvelles cellules nées à la génération suivante"
def become_alive_tick(alive_cells) do
  GameOfLife.Cell.dead_neighbours(alive_cells)
  |> Enum.map(&(Task.Supervisor.async(
                {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},
                GameOfLife.Board, :become_alive_or_nilify, [alive_cells, &1])))
  |> Enum.map(&Task.await/1)
  |> remove_nil_cells
end

def become_alive_or_nilify(alive_cells, dead_cell) do
  if GameOfLife.Cell.become_alive?(alive_cells, dead_cell), do: dead_cell, else: nil
end
```

Elle fonctionne de manière similaire à `GameOfLife.Board.keep_alive_tick/1`. Tout d'abord, nous recherchons les voisins morts des cellules vivantes. Ensuite, pour chaque cellule morte, nous créons un nouveau processus sur les nœuds du cluster pour déterminer si la cellule morte doit devenir vivante à la génération suivante.

Vous pouvez voir le code source complet du [module GameOfLife.Board](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/lib/game_of_life/board.ex) et les [tests sur GitHub](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/test/game_of_life/board_test.exs).

### Créer le BoardServer

Créons le comportement de serveur générique `GameOfLife.BoardServer`. Nous définissons une interface publique pour le serveur.

```elixir
# lib/game_of_life/board_server.ex
defmodule GameOfLife.BoardServer do
  use GenServer
  require Logger

  @name {:global, __MODULE__}
  @game_speed 1000 # millisecondes

  # Client
  def start_link(alive_cells) do
    case GenServer.start_link(__MODULE__, {alive_cells, nil, 0}, name: @name) do
      {:ok, pid} ->
        Logger.info "Démarrage du maître #{__MODULE__}"
        {:ok, pid}
      {:error, {:already_started, pid}} ->
        Logger.info "Démarrage de l'esclave #{__MODULE__}"
        {:ok, pid}
    end
  end

  def alive_cells do
    GenServer.call(@name, :alive_cells)
  end

  def generation_counter do
    GenServer.call(@name, :generation_counter)
  end

  def state do
    GenServer.call(@name, :state)
  end

  @doc """
  Efface le plateau et n'ajoute que de nouvelles cellules.
  Le compteur de génération est réinitialisé.
  """
  def set_alive_cells(cells) do
    GenServer.call(@name, {:set_alive_cells, cells})
  end

  def add_cells(cells) do
    GenServer.call(@name, {:add_cells, cells})
  end

  def tick do
    GenServer.cast(@name, :tick)
  end

  def start_game(speed \\ @game_speed) do
    GenServer.call(@name, {:start_game, speed})
  end

  def stop_game do
    GenServer.call(@name, :stop_game)
  end

  def change_speed(speed) do
    stop_game
    start_game(speed)
  end
end
```

Comme vous pouvez le voir, nous utilisons le comportement `GenServer` dans notre module. Le module nécessite également Logger car nous aimerions imprimer des informations sur STDOUT.

Dans la fonction `start_link/1`, nous démarrons un nouveau `GenServer`. Lorsque notre serveur générique démarre, il est le premier processus du cluster. Il devient alors le processus primaire. Dans le cas où il y a déjà un processus en cours d'exécution avec un nom enregistré globalement `{:global,__MODULE__}`, nous enregistrons l'information que notre processus sera un processus réplique avec une référence au PID existant sur un autre nœud du cluster.

Nous stockons le nom global de notre serveur dans l'attribut `@name`. Nous utilisons un autre attribut `@game_speed` pour la vitesse de jeu par défaut qui est de 1000 millisecondes.

Dans notre interface publique, nous avons la fonction `alive_cells/1` qui retourne la liste des cellules vivantes. Fondamentalement, c'est l'état actuel du jeu (cellules vivantes sur le plateau). Cette fonction appelle `GenServer` avec le `@name` enregistré et demande `:alive_cells`. Nous devons implémenter la fonction `handle_call/3` pour ce type de requête (`:alive_cells`).

Il y a une autre fonction publique `generation_counter/1` qui retourne combien de générations ont déjà été traitées par le serveur de plateau.

La fonction `state/1` retourne l'état qui est détenu par notre serveur générique. L'état est représenté comme le tuple avec 3 valeurs comme les cellules vivantes, TRef (référence temporelle — nous voulons régénérer le plateau chaque seconde) et le compteur de génération. TRef est une chose très interne au serveur de plateau, nous ne le retournerons donc pas au monde extérieur. C'est pourquoi nous ne retournerons que les cellules vivantes et le compteur de génération. Vous le verrez plus tard dans l'implémentation de `handle_call(:state, _from, state)`.

Vous pouvez utiliser la fonction `set_alive_cells/1` dans le cas où vous voulez écraser la liste actuelle des cellules vivantes par une nouvelle liste.

La fonction `add_cells/1` sera très utile car nous voulons pouvoir ajouter de nouvelles cellules ou figures au plateau. Par exemple, nous pourrions vouloir ajouter un motif de clignotant (blinker) au jeu existant. Vous en apprendrez plus sur les motifs plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/SGbjJ1XyyVP1F7u7KDrJ2mT74d6J3KBxuhw1)
_motif clignotant (blinker)_

Nous pouvons forcer manuellement le jeu à calculer la génération suivante de cellules avec la fonction `tick/1`.

La fonction `start_game/1` est responsable du démarrage d'un nouveau timer qui appelle chaque seconde une fonction `tick/1`. Grâce à cela, notre jeu mettra à jour la liste des cellules vivantes dans un intervalle spécifié qui est `@game_speed`.

Les 2 dernières fonctions sont `stop_game/1` et `change_speed/1` qui redémarrent simplement le jeu et en lancent un nouveau avec la vitesse fournie.

Maintenant, vous pouvez voir comment les fonctions ci-dessus fonctionnent. Elles appellent les callbacks du serveur.

```elixir
# lib/game_of_life/board_server.ex
defmodule GameOfLife.BoardServer do
  use GenServer
  # ...
  # Serveur (callbacks)
  def handle_call(:alive_cells, _from, {alive_cells, _tref, _generation_counter} = state) do
    {:reply, alive_cells, state}
  end

  def handle_call(:generation_counter, _from, {_alive_cells, _tref, generation_counter} = state) do
    {:reply, generation_counter, state}
  end

  def handle_call(:state, _from, {alive_cells, _tref, generation_counter} = state) do
    {:reply, {alive_cells, generation_counter}, state}
  end

  def handle_call({:set_alive_cells, cells}, _from, {_alive_cells, tref, _generation_counter}) do
    {:reply, cells, {cells, tref, 0}}
  end

  def handle_call({:add_cells, cells}, _from, {alive_cells, tref, generation_counter}) do
    alive_cells = GameOfLife.Board.add_cells(alive_cells, cells)
    {:reply, alive_cells, {alive_cells, tref, generation_counter}}
  end

  def handle_call({:start_game, speed}, _from, {alive_cells, nil = _tref, generation_counter}) do
    {:ok, tref} = :timer.apply_interval(speed, __MODULE__, :tick, [])
    {:reply, :game_started, {alive_cells, tref, generation_counter}}
  end

  def handle_call({:start_game, _speed}, _from, {_alive_cells, _tref, _generation_counter} = state) do
    {:reply, :game_already_running, state}
  end

  def handle_call(:stop_game, _from, {_alive_cells, nil = _tref, _generation_counter} = state) do
    {:reply, :game_not_running, state}
  end

  def handle_call(:stop_game, _from, {alive_cells, tref, generation_counter}) do
    {:ok, :cancel} = :timer.cancel(tref)
    {:reply, :game_stoped, {alive_cells, nil, generation_counter}}
  end

  def handle_cast(:tick, {alive_cells, tref, generation_counter}) do
    keep_alive_task = Task.Supervisor.async(
                      {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},
                      GameOfLife.Board, :keep_alive_tick, [alive_cells])
    become_alive_task = Task.Supervisor.async(
                        {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},
                        GameOfLife.Board, :become_alive_tick, [alive_cells])
    keep_alive_cells = Task.await(keep_alive_task)
    born_cells = Task.await(become_alive_task)
    alive_cells = keep_alive_cells ++ born_cells
    {:noreply, {alive_cells, tref, generation_counter + 1}}
  end
end
```

Oh, nous avons oublié les tests. Dans ce cas, nous pouvons utiliser [DocTest](http://elixir-lang.org/docs/stable/ex_unit/ExUnit.DocTest.html). Cela nous permet de générer des tests à partir des exemples de code existant dans la documentation d'un module, d'une fonction ou d'une macro.

Notre fichier de test est super court :

```elixir
# test/game_of_life/board_server_test.exs
defmodule GameOfLife.BoardServerTest do
  use ExUnit.Case
  doctest GameOfLife.BoardServer
end
```

Ajoutons `@moduledoc` à `GameOfLife.BoardServer`.

```elixir
# lib/game_of_life/board_server.ex
defmodule GameOfLife.BoardServer do
  use GenServer
  require Logger
  @moduledoc """
  ## Exemple
      iex> GameOfLife.BoardServer.start_game
      :game_started
      iex> GameOfLife.BoardServer.start_game
      :game_already_running
      iex> GameOfLife.BoardServer.stop_game
      :game_stoped
      iex> GameOfLife.BoardServer.stop_game
      :game_not_running
      iex> GameOfLife.BoardServer.change_speed(500)
      :game_started
      iex> GameOfLife.BoardServer.stop_game
      :game_stoped
      iex> GameOfLife.BoardServer.set_alive_cells([{0, 0}])
      [{0, 0}]
      iex> GameOfLife.BoardServer.alive_cells
      [{0, 0}]
      iex> GameOfLife.BoardServer.add_cells([{0, 1}])
      [{0, 0}, {0, 1}]
      iex> GameOfLife.BoardServer.alive_cells
      [{0, 0}, {0, 1}]
      iex> GameOfLife.BoardServer.state
      {[{0, 0}, {0, 1}], 0}
      iex> GameOfLife.BoardServer.generation_counter
      0
      iex> GameOfLife.BoardServer.tick
      :ok
      iex> GameOfLife.BoardServer.generation_counter
      1
      iex> GameOfLife.BoardServer.state
      {[], 1}
  """
end
```

Comme vous pouvez le voir, nous avons regroupé 3 exemples dans l'attribut `@moduledoc` et ils sont séparés par une nouvelle ligne. Lorsque vous lancez les tests, vous verrez 3 tests distincts.

```
$ mix test test/game_of_life/board_server_test.exs
Compiled lib/game_of_life/board_server.ex
20:54:30.637 [info]  Started Elixir.GameOfLife.BoardServer master
...Finished in 0.1 seconds (0.1s on load, 0.00s on tests)
3 tests, 0 failures
Randomized with seed 791637
```

Dans `GameOfLife.BoardServer`, vous avez probablement remarqué 2 choses intéressantes. La première est `GameOfLife.Board` qui est appelé dans :

```elixir
# lib/game_of_life/board_server.ex
def handle_call({:add_cells, cells}, _from, {alive_cells, tref, generation_counter}) do
  alive_cells = GameOfLife.Board.add_cells(alive_cells, cells)
  {:reply, alive_cells, {alive_cells, tref, generation_counter}}
end
```

Comme vous l'avez vu précédemment, nous avons ajouté des fonctions utiles au module `GameOfLife.Board` qui nous aident à effectuer des opérations sur la liste des cellules vivantes.

Une autre chose intéressante est la façon dont nous utilisons `Task.Supervisor` dans :

```elixir
# lib/game_of_life/board_server.ex
def handle_cast(:tick, {alive_cells, tref, generation_counter}) do
    keep_alive_task = Task.Supervisor.async(
                      {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},
                      GameOfLife.Board, :keep_alive_tick, [alive_cells])
    become_alive_task = Task.Supervisor.async(
                        {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},
                        GameOfLife.Board, :become_alive_tick, [alive_cells])
    keep_alive_cells = Task.await(keep_alive_task)
    born_cells = Task.await(become_alive_task)
    alive_cells = keep_alive_cells ++ born_cells
    {:noreply, {alive_cells, tref, generation_counter + 1}}
  end
```

Ce que nous faisons ici, c'est lancer un nouveau processus asynchrone pour exécuter la fonction `GameOfLife.keep_alive_tick/1` avec l'argument `alive_cells`.

```elixir
# lib/game_of_life/board_server.ex
keep_alive_task = Task.Supervisor.async(
                  {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},
                  GameOfLife.Board, :keep_alive_tick, [alive_cells])
```

Le tuple `{GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node}` indique à `Task.Supervisor` que nous voulons utiliser le superviseur de tâches nommé `GameOfLife.TaskSupervisor` et que nous voulons exécuter le processus sur le nœud retourné par la fonction `GameOfLife.NodeManager.random_node`.

### Créer l'imprimeur de jeu et le présentateur console

Le module `GameOfLife.GamePrinter` s'exécute en tant que worker sous la supervision du superviseur `GameOfLife`. `GameOfLife.GamePrinter` utilise `Agent` pour stocker `TRef` pour la référence du timer car nous voulons imprimer le plateau sur STDOUT avec l'intervalle spécifié.

Vous avez déjà vu l'exemple d'utilisation d' `Agent`, donc cela ne devrait pas être nouveau pour vous. Fondamentalement, nous avons écrit l'interface publique pour démarrer et arrêter l'impression du plateau à l'écran. Pour les tests, nous avons utilisé [DocTest](http://elixir-lang.org/docs/stable/ex_unit/ExUnit.DocTest.html).

```elixir
# lib/game_of_life/game_printer.ex
defmodule GameOfLife.GamePrinter do
  @moduledoc """
  ## Exemple
      iex> GameOfLife.GamePrinter.start_printing_board
      :printing_started
      iex> GameOfLife.GamePrinter.start_printing_board
      :already_printing
      iex> GameOfLife.GamePrinter.stop_printing_board
      :printing_stopped
      iex> GameOfLife.GamePrinter.stop_printing_board
      :already_stopped
  """
  @print_speed 1000

  def start_link do
    Agent.start_link(fn -> nil end, name: __MODULE__)
  end

  def start_printing_board do
    Agent.get_and_update(__MODULE__, __MODULE__, :do_start_printing_board, [])
  end

  def do_start_printing_board(nil = _tref) do
    {:ok, tref} = :timer.apply_interval(@print_speed, __MODULE__, :print_board, [])
    {:printing_started, tref}
  end

  def do_start_printing_board(tref), do: {:already_printing, tref}

  def print_board do
    {alive_cells, generation_counter} = GameOfLife.BoardServer.state
    alive_counter = alive_cells |> Enum.count
    GameOfLife.Presenters.Console.print(alive_cells, generation_counter, alive_counter)
  end

  def stop_printing_board do
    Agent.get_and_update(__MODULE__, __MODULE__, :do_stop_printing_board, [])
  end

  def do_stop_printing_board(nil = _tref), do: {:already_stopped, nil}

  def do_stop_printing_board(tref) do
    {:ok, :cancel} = :timer.cancel(tref)
    {:printing_stopped, nil}
  end
end
```

`GameOfLife.Presenters.Console` est responsable de l'impression soignée du plateau avec les axes X & Y, le nombre de cellules vivantes et le compteur de génération. Commençons par les tests. Nous allons capturer STDOUT et comparer si les données imprimées à l'écran correspondent à ce que nous attendons.

```elixir
# test/game_of_life/presenters/console_test.exs
defmodule GameOfLife.Presenters.ConsoleTest do
  use ExUnit.Case
  # permet de capturer ce qui est envoyé sur stdout
  import ExUnit.CaptureIO

  test "imprimer les cellules sur la sortie console" do
    cell_outside_of_board = {-1, -1}
    cells = [{0, 0}, {1, 0}, {2, 0}, {1, 1}, {0, 2}, cell_outside_of_board]
    result = capture_io fn ->
      GameOfLife.Presenters.Console.print(cells, 123, 6, 0, 2, 2, 2)
    end
    assert result == (
    "    2| O,,\n" <>
    "    1| ,O,\n" <>
    "    0| OOO\n" <>
    "     | _ _ \n" <>
    "    /  0    \n" <>
    "Generation: 123\n" <>
    "Alive cells: 6\n"
    )
  end
end
```

Voici l'implémentation de notre fonction d'impression :

```elixir
# lib/game_of_life/presenters/console.ex
defmodule GameOfLife.Presenters.Console do
  @doc """
  Imprime les cellules sur la sortie console.
  Le plateau n'est visible que pour une taille spécifiée pour x et y.
  Le début de x et y se trouve dans le coin supérieur gauche du plateau.
  `x_padding` Doit être un nombre premier. Chaque x divisé par ce nombre premier
  sera visible sur l'axe x.
  `y_padding` N'importe quel nombre. Padding pour les nombres sur l'axe y.
  """
  def print(cells, generation_counter, alive_counter, start_x \\ -10, start_y \\ 15, x_size \\ 60,
            y_size \\ 20, x_padding \\ 5, y_padding \\ 5) do
    end_x = start_x + x_size
    end_y = start_y - y_size
    x_range = start_x..end_x
    y_range = start_y..end_y

    for y <- y_range, x <- x_range do
      # dessiner l'axe y
      if x == start_x do
        (y
        |> Integer.to_string
        |> String.rjust(y_padding)) <> "| "
        |> IO.write
      end

      IO.write(if Enum.member?(cells, {x, y}), do: "O", else: ",")
      if x == end_x, do: IO.puts ""
    end

    # dessiner l'axe x
    IO.write String.rjust("| ", y_padding + 2)
    x_length = (round((end_x-start_x)/2))
    for x <- 0..x_length, do: IO.write "_ "
    IO.puts ""
    IO.write String.rjust("/  ", y_padding + 2)

    for x <- x_range do
      if rem(x, x_padding) == 0 do
        x
        |> Integer.to_string
        |> String.ljust(x_padding)
        |> IO.write
      end
    end

    IO.puts ""
    IO.puts "Generation: #{generation_counter}"
    IO.puts "Alive cells: #{alive_counter}"
  end
end
```

Le plateau avec une partie visible plus grande ressemble à ceci :

```
   15| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   14| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   13| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   12| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   11| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   10| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    9| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    8| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    7| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    6| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    5| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    4| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    3| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    2| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    1| ,,,,,,,,,,OO,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    0| ,,,,,,,,,,OO,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -1| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -2| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -3| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -4| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -5| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _    /  -10  -5   0    5    10   15   20   25   30   35   40   45   50Generation: 18Alive cells: 4
```

La dernière étape consiste à décommenter le worker `GameOfLife.GamePrinter` dans :

```elixir
# lib/game_of_life.ex
defmodule GameOfLife do
  use Application

  # Voir http://elixir-lang.org/docs/stable/elixir/Application.html
  # pour plus d'informations sur les applications OTP
  def start(_type, _args) do
    import Supervisor.Spec, warn: false
    init_alive_cells = []
    children = [
      # Définir les workers et les superviseurs enfants à superviser
      # worker(GameOfLife.Worker, [arg1, arg2, arg3]),
      supervisor(Task.Supervisor, [[name: GameOfLife.TaskSupervisor]]),
      worker(GameOfLife.BoardServer, [init_alive_cells]),
      # Cette ligne est maintenant décommentée
      worker(GameOfLife.GamePrinter, []),
    ]

    # Voir http://elixir-lang.org/docs/stable/elixir/Supervisor.html
    # pour d'autres stratégies et options supportées
    opts = [strategy: :one_for_one, name: GameOfLife.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

### Ajouter des motifs de figures et les placer sur le plateau

Pour jouer à notre jeu de la vie, il serait formidable d'avoir un moyen facile d'ajouter des figures au plateau. Il existe de nombreux motifs connus comme les natures mortes, les oscillateurs et les vaisseaux spatiaux. Vous pouvez [en apprendre plus à leur sujet ici](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns).

Un motif intéressant est le canon. Le Gosper Glider Gun est un motif très populaire. Voici à quoi il ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/wxl-EjJX2Bn1aQ82Mp6p0hhFLMUnSjwpMyHy)
_Gosper Glider Gun_

Lorsque vous lancez le jeu, le motif se comporte comme vous le voyez. Le canon tire.

![Image](https://cdn-media-1.freecodecamp.org/images/ROo3D4AEbeI2atC5gYBi3Snfk1-TiAsDmMdk)
_Cycle de vie du motif Gosper Glider Gun_

Écrivons ce motif. Imaginez que vous voulez placer le motif dans un rectangle. Le coin inférieur gauche du rectangle est à la position `{0,0}`.

```elixir
# lib/game_of_life/patterns/guns.ex
defmodule GameOfLife.Patterns.Guns do
  @moduledoc """
  https://en.wikipedia.org/wiki/Gun_(cellular_automaton)
  """

  @doc """
  https://en.wikipedia.org/wiki/File:Game_of_life_glider_gun.svg
  """
  def gosper_glider do
    [
      {24, 8},
      {22, 7}, {24, 7},
      {12, 6}, {13, 6}, {20, 6}, {21, 6}, {34, 6}, {35, 6},
      {11, 5}, {15, 5}, {20, 5}, {21, 5}, {34, 5}, {35, 5},
      {0, 4}, {1, 4}, {10, 4}, {16, 4}, {20, 4}, {21, 4},
      {0, 3}, {1, 3}, {10, 3}, {14, 3}, {16, 3}, {17, 3}, {22, 3}, {24, 3},
      {10, 2}, {16, 2}, {24, 2},
      {11, 1}, {15, 1},
      {12, 0}, {13, 0},
    ]
  end
end
```

Il serait également utile de pouvoir placer le motif sur le plateau à une position spécifiée par nous. Écrivons un convertisseur de motif.

```elixir
# lib/game_of_life/pattern_converter.ex
defmodule GameOfLife.PatternConverter do
  @doc """
  ## Exemple
      iex> GameOfLife.PatternConverter.transit([{0, 0}, {1, 3}], -1, 2)
      [{-1, 2}, {0, 5}]
  """
  def transit([{x, y} | cells], x_padding, y_padding) do
    [{x + x_padding, y + y_padding} | transit(cells, x_padding, y_padding)]
  end

  def transit([], _x_padding, _y_padding), do: []
end
```

C'est ainsi que vous pouvez ajouter le motif Gosper glider au plateau avec la position spécifiée.

```elixir
GameOfLife.Patterns.Guns.gosper_glider
|> GameOfLife.PatternConverter.transit(-2, -3)
|> GameOfLife.BoardServer.add_cells
```

Vous pouvez trouver [plus de motifs dans les modules ici](https://github.com/BeyondScheme/elixir-game_of_life/tree/master/lib/game_of_life/patterns).

### Exécuter le jeu sur plusieurs nœuds

Il est maintenant temps de lancer notre jeu. Le [code source complet peut être trouvé ici](https://github.com/BeyondScheme/elixir-game_of_life).

Lançons le premier nœud où le `GameOfLife.BoardServer` sera exécuté.

```
$ iex --sname node1 -S mix
Erlang/OTP 18 [erts-7.3] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]
Interactive Elixir (1.2.4) - press Ctrl+C to exit (type h() ENTER for help)
16:54:08.554 [info]  Started Elixir.GameOfLife.BoardServer master
iex(node1@Artur)1> GameOfLife.BoardServer.start_game
:game_started
iex(node1@Artur)2> GameOfLife.GamePrinter.start_printing_board
:printing_started
```

Dans une autre fenêtre de terminal, vous pouvez démarrer le second nœud. Nous le connecterons au premier nœud.

```
$ iex --sname node2 -S mix
Erlang/OTP 18 [erts-7.3] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]
Interactive Elixir (1.2.4) - press Ctrl+C to exit (type h() ENTER for help)
16:55:17.395 [info]  Started Elixir.GameOfLife.BoardServer master
iex(node2@Artur)1> Node.connect :node1@Artur
true
16:55:17.691 [info]  Started Elixir.GameOfLife.BoardServer slave
iex(node2@Artur)2> Node.list
[:node1@Artur]
iex(node2@Artur)3> Node.self
:node2@Artur
iex(node2@Artur)4> GameOfLife.Patterns.Guns.gosper_glider |> GameOfLife.BoardServer.add_cells
[{24, 8}, {22, 7}, {24, 7}, {12, 6}, {13, 6}, {20, 6}, {21, 6}, {34, 6}, {35, 6}, {11, 5}, {15, 5}, {20, 5}, {21, 5}, {34, 5}, {35, 5}, {0, 4}, {1, 4}, {10, 4}, {16, 4}, {20, 4}, {21, 4}, {0, 3}, {1, 3}, {10, 3}, {14, 3}, {16, 3}, {17, 3}, {22, 3}, {24, 3}, {10, 2}, {16, 2}, {24, 2}, {11, 1}, {15, 1}, {12, 0}, {13, 0}]
```

Les deux nœuds exécutent des calculs pour déterminer un nouvel état pour les cellules vivantes. Vous pouvez également lancer le jeu sur différents serveurs du réseau comme ceci :

```elixir
# démarrer node1
$ iex --name node1@192.168.0.101 --cookie "token_for_cluster" -S mix
# démarrer node2 sur un autre serveur
$ iex --name node2@192.168.0.102 --cookie "token_for_cluster" -S mix
iex> Node.connect :"node1@192.168.0.101"
true
```

Vous avez déjà vu comment le jeu fonctionne dans la démo au début de l'article. Vous pouvez l'essayer sur votre propre machine, il suffit de cloner le [dépôt](https://github.com/BeyondScheme/elixir-game_of_life).

### Résumé

Enfin, nous avons réussi à arriver au bout. C'était une route assez longue mais nous avons un jeu fonctionnel, distribué sur plusieurs nœuds. Nous avons appris à écrire un GenServer, à utiliser des Agents, à répartir les processus sur les nœuds avec TaskSupervisor et à connecter les nœuds dans un cluster. Vous avez également vu des exemples de tests en Elixir et comment utiliser DocTest.

J'espère que vous avez trouvé quelque chose d'intéressant dans cet article. N'hésitez pas à partager vos réflexions dans les commentaires.

Actuellement, je travaille sur le problème de la parallélisation CI pour exécuter les tests rapidement sur les serveurs CI. J'ai construit [**Knapsack Pro qui répartit vos tests Ruby et JavaScript sur des nœuds CI parallèles pour gagner du temps sur les tests**](https://knapsackpro.com?utm_source=medium&utm_medium=blog&utm_campaign=game_of_life_elixir&utm_content=knapsackpro). Vous pouvez consulter l'un de mes articles sur la [parallélisation de la suite de tests Cypress en JavaScript](https://medium.com/@arturtrzop/cypress-e2e-tests-split-with-ci-parallelisation-and-auto-balancing-ci-nodes-time-8c6c8b0a37f1) ou la [parallélisation Heroku CI](https://medium.com/datadriveninvestor/heroku-ci-parallel-test-runs-done-with-optimal-test-suite-split-how-to-run-parallel-dynos-79903d9a0ec6). Dites-moi si vos tests sont lents ou rapides dans vos projets Elixir — laissez simplement un commentaire. :) J'aimerais également ajouter le support de la parallélisation des tests CI pour Elixir.