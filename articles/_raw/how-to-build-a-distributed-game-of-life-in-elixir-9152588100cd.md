---
title: How to build a distributed Game of Life in Elixir
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
seo_title: null
seo_desc: 'By Artur Trzop

  I wrote my first game in Elixir. It is a popular thing — Conway’s Game of Life —
  but it gets quite interesting when you solve it in a functional language, especially
  when you can see how the actor model works and how actors are distrib...'
---

By Artur Trzop

I wrote my first game in Elixir. It is a popular thing — Conway’s Game of Life — but it gets quite interesting when you solve it in a functional language, especially when you can see [how the actor model works](https://en.wikipedia.org/wiki/Actor_model) and how actors are distributed across servers in the network.

![Image](https://cdn-media-1.freecodecamp.org/images/3Snl82uCosun4TAqGggHfSKVUng0YPUzFheF)
_Game of Life_

**In this blog post I am going to show:**

* how to write rules for the game of life with tests in Elixir,
* parallel tasks across lightweight processes (actors) in order to utilize all CPU cores,
* how to distribute work across nodes so the game can be executed by many servers in the cluster,
* how to use GenServer behaviour, TaskSupervisor and Agents in Elixir.

This project and the full [source code can be found here](https://github.com/BeyondScheme/elixir-game_of_life).

### Demo

Let’s start with watching quick demo of how the game works.

[**GameOfLife**](https://asciinema.org/a/44233)   
[_Recorded by ArturT_asciinema.org](https://asciinema.org/a/44233)

As you can see, node1 represents running game and board on the screen. The second node was also started and connected to the first one. From the second node, we added new cells to the board. Both nodes are responsible for processing the game, but only the first node is a primary with information about the current state of the game. We can connect more nodes to the cluster so game processing can happen on all of the nodes. You are going to learn in this article how to make it happen.

### Game of Life rules

If you already know about [the game of life problem](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) just jump to [the next header](https://beyondscheme.com/2016/distributed-game-of-life-in-elixir#create-new-application-in-elixir). If not, in this section you can learn the basic concept.

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any live cell with fewer than two live neighbours dies as if caused by under-population.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by over-population.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.

### Create new application in Elixir

First things first, so we are going to create a new Elixir OTP application with supervision tree. We will use supervisor for our game server, you will learn more about it a bit later.

```
$ mix new --sup game_of_life
```

A `--sup` option is given to generate an OTP application skeleton including a supervision tree. Normally an app is generated without a supervisor and without the app callback.

In `lib/game_of_life.ex` file you will find an example of how to add child worker to supervisor.

```
# lib/game_of_life.exdefmodule GameOfLife do  use Application  # See http://elixir-lang.org/docs/stable/elixir/Application.html  # for more information on OTP Applications  def start(_type, _args) do    import Supervisor.Spec, warn: false    children = [      # Define workers and child supervisors to be supervised      # worker(GameOfLife.Worker, [arg1, arg2, arg3]),    ]    # See http://elixir-lang.org/docs/stable/elixir/Supervisor.html    # for other strategies and supported options    opts = [strategy: :one_for_one, name: GameOfLife.Supervisor]    Supervisor.start_link(children, opts)  endend
```

### Represent the board in Game of Life

We need to represent the alive cells on the board in our game. A single cell can be a tuple `{x, y}` with coordinates in the 2-dimensional board.

All alive cells on the board will be on the list `alive_cells`.

```
alive_cells = [{0, 0}, {1, 0}, {2, 0}, {1, 1}, {-1,-2}]
```

Here is an example of how this board with alive cells looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/j2utgQIL1-t1HTIR9smp5jEtsfDIbsOkS1ZE)
_Board with alive cells_

and here are proper x & y coordinates:

![Image](https://cdn-media-1.freecodecamp.org/images/FNNnkZazIb8gyyR0vg5F9R4kiXVKAUXDUx9D)
_Coordinates of alive cells_

Now when we have the idea of how we are going to store our alive cells we can jump to write some code.

### Game of Life rules with tests

We can create `GameOfLife.Cell` module with function `keep_alive?/2` responsible for determining if a particular alive cell `{x, y}` should be still alive on the next generation or not.

Here is the function with expected arguments:

```
# lib/game_of_life/cell.exdefmodule GameOfLife.Cell do  def keep_alive?(alive_cells, {x, y} = _alive_cell) do    # TODO  endend
```

Let’s write some tests to cover the first of the requirements of the Game of Life:

> Any live cell with fewer than two live neighbours dies, as if caused by under-population.

We wrote tests to ensure `GameOfLife.Cell.keep_alive?/2` function returns false in a case when the alive cell has no neighbours or has just one.

```
# test/game_of_life/cell_test.exsdefmodule GameOfLife.CellTest do  use ExUnit.Case, async: true  test "alive cell with no neighbours dies" do    alive_cell = {1, 1}    alive_cells = [alive_cell]    refute GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)  end  test "alive cell with 1 neighbour dies" do    alive_cell = {1, 1}    alive_cells = [alive_cell, {0, 0}]    refute GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)  endend
```

`GameOfLife.Cell.keep_alive?/2` function needs to return false just to pass our tests so let’s add more tests to cover other requirements.

> Any live cell with more than three live neighbours dies, as if by over-population.

```
# test/game_of_life/cell_test.exstest "alive cell with more than 3 neighbours dies" do  alive_cell = {1, 1}  alive_cells = [alive_cell, {0, 0}, {1, 0}, {2, 0}, {2, 1}]  refute GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)end
```

> _Any live cell with two or three live neighbours lives on to the next generation._

```
# test/game_of_life/cell_test.exstest "alive cell with 2 neighbours lives" do  alive_cell = {1, 1}  alive_cells = [alive_cell, {0, 0}, {1, 0}]  assert GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)endtest "alive cell with 3 neighbours lives" do  alive_cell = {1, 1}  alive_cells = [alive_cell, {0, 0}, {1, 0}, {2, 1}]  assert GameOfLife.Cell.keep_alive?(alive_cells, alive_cell)end
```

Now, we can implement our `GameOfLife.Cell.keep_alive?/2` function.

```
# lib/game_of_life/cell.exdefmodule GameOfLife.Cell do  def keep_alive?(alive_cells, {x, y} = _alive_cell) do    case count_neighbours(alive_cells, x, y, 0) do      2 -&gt; true      3 -> true      _ -> false    end  end  defp count_neighbours([head_cell | tail_cells], x, y, count) do    increment = case head_cell do      {hx, hy} when hx == x - 1 and hy == y - 1 -> 1      {hx, hy} when hx == x     and hy == y - 1 -> 1      {hx, hy} when hx == x + 1 and hy == y - 1 -> 1      {hx, hy} when hx == x - 1 and hy == y     -&gt; 1      {hx, hy} when hx == x + 1 and hy == y     ->; 1      {hx, hy} when hx == x - 1 and hy == y + 1 ->; 1      {hx, hy} when hx == x     and hy == y + 1 -&gt; 1      {hx, hy} when hx == x + 1 and hy == y + 1 -> 1      _not_neighbour -> 0    end    count_neighbours(tail_cells, x, y, count + increment)  end  defp count_neighbours([], _x, _y, count), do: countend
```

As you can see, we implemented the private function `count_neighbours/4` responsible for counting neighbours. It will be helpful to meet the next rule.

There is one more requirement we forgot about:

> Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

We are going to write a new function `GameOfLife.Cell.become_alive?/2` expecting the coordinates of the dead cell and returning if the dead cell should become alive or not.

```
# lib/game_of_life/cell.exdefmodule GameOfLife.Cell do  def become_alive?(alive_cells, {x, y} = _dead_cell) do    3 == count_neighbours(alive_cells, x, y, 0)  endend
```

And here is the test for that:

```
# test/game_of_life/cell_test.exstest "dead cell with three live neighbours becomes a live cell" do  alive_cells = [{2, 2}, {1, 0}, {2, 1}]  dead_cell = {1, 1}  assert GameOfLife.Cell.become_alive?(alive_cells, dead_cell)endtest "dead cell with two live neighbours stays dead" do  alive_cells = [{2, 2}, {1, 0}]  dead_cell = {1, 1}  refute GameOfLife.Cell.become_alive?(alive_cells, dead_cell)end
```

There is one more thing which might be helpful for us. We have the list of alive cells but we don’t know much about the dead cells. The number of dead cells is infinite so we need to cut down the number of dead cells for which we want to check if they should become alive. The simple way would be to check only dead cells with alive neighbours. Hence the `GameOfLife.Cell.dead_neighbours/1`function.

Let’s write some tests first:

```
# test/game_of_life/cell_test.exstest "find dead cells (neighbours of alive cell)" do  alive_cells = [{1, 1}]  dead_neighbours = GameOfLife.Cell.dead_neighbours(alive_cells) |&gt; Enum.sort  expected_dead_neighbours = [    {0, 0}, {1, 0}, {2, 0},    {0, 1}, {2, 1},    {0, 2}, {1, 2}, {2, 2}  ] |>; Enum.sort  assert dead_neighbours == expected_dead_neighboursendtest "find dead cells (neighbours of alive cells)" do  alive_cells = [{1, 1}, {2, 1}]  dead_neighbours = GameOfLife.Cell.dead_neighbours(alive_cells) |&gt; Enum.sort  expected_dead_neighbours = [    {0, 0}, {1, 0}, {2, 0}, {3, 0},    {0, 1}, {3, 1},    {0, 2}, {1, 2}, {2, 2}, {3, 2}  ] |> Enum.sort  assert dead_neighbours == expected_dead_neighboursend
```

and here is the implemented function:

```
# lib/game_of_life/cell.exdef dead_neighbours(alive_cells) do  neighbours = neighbours(alive_cells, [])  (neighbours |&gt; Enum.uniq) -- alive_cellsenddefp neighbours([{x, y} | cells], neighbours) do  neighbours(cells, neighbours ++ [    {x - 1, y - 1}, {x    , y - 1}, {x + 1, y - 1},    {x - 1, y    }, {x + 1, y    },    {x - 1, y + 1}, {x    , y + 1}, {x + 1, y + 1}  ])enddefp neighbours([], neighbours), do: neighbours
```

Basically, these are all rules implemented in the single module `GameOfLife.Cell`. You can see the whole [module file](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/lib/game_of_life/cell.ex) with [tests on GitHub](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/test/game_of_life/cell_test.exs).

### The architecture of distributed Game of Life

![Image](https://cdn-media-1.freecodecamp.org/images/BIrpLZBjGimv4-HlBQQt9UslBgNwam3Pr0bC)
_The architecture of distributed Game of Life in Elixir_

Our main supervisor is `GameOfLife.Supervisor` which I mentioned at the beginning of the article. Below you can see how we defined its children like `Task.Supervisor`, workers for `BoardServer` and `GamePrinter`.

```
# lib/game_of_life.exdefmodule GameOfLife do  use Application  # See http://elixir-lang.org/docs/stable/elixir/Application.html  # for more information on OTP Applications  def start(_type, _args) do    import Supervisor.Spec, warn: false    init_alive_cells = []    children = [      # Define workers and child supervisors to be supervised      # worker(GameOfLife.Worker, [arg1, arg2, arg3]),      supervisor(Task.Supervisor, [[name: GameOfLife.TaskSupervisor]]),      worker(GameOfLife.BoardServer, [init_alive_cells]),      # We will uncomment this line later      # worker(GameOfLife.GamePrinter, []),    ]    # See http://elixir-lang.org/docs/stable/elixir/Supervisor.html    # for other strategies and supported options    opts = [strategy: :one_for_one, name: GameOfLife.Supervisor]    Supervisor.start_link(children, opts)  endend
```

Let me describe what each component on the image is responsible for.

`Task.Supervisor` is an Elixir module defining a new supervisor which can be used to dynamically supervise tasks. We are going to use it to spin off tasks like determining if the particular cell should live or die. Those tasks can be run across nodes connected into the cluster.

In the above code, we gave the name `GameOfLife.TaskSupervisor` for our supervisor. We will use this name to tell the `Task.Supervisor.async` function which Task Supervisor should handle our task. You can read more about [Task.Supervisor here](http://elixir-lang.org/docs/stable/elixir/Task.Supervisor.html).

`GameOfLife.BoardServer` is our module implemented as [GenServer behaviour](http://elixir-lang.org/docs/stable/elixir/GenServer.html). It is responsible for holding the state of the game. By that I mean it keeps the list of alive cells on the board along with generation counter and TRef. TRef is a timer reference returned by the [Erlang timer module](http://erlang.org/doc/man/timer.html) and the [apply_interval](http://erlang.org/doc/man/timer.html#apply_interval-4) function.

We want to start the game and generate a new list of alive cells for the next generation with a specified time interval. With each new generation, we will update the generation counter. The other interesting thing is that `GameOfLife.BoardServer` is running only on a single node. Once another node is connected to the cluster where is already running `GameOfLife.BoardServer` then `GameOfLife.BoardServer` won’t be started just like that on the newly connected node.

Instead on the new node `GameOfLife.BoardServer` will keep the only reference to the PID of the process existing on the first node. We want to have the single source of truth about the state of our game in one primary `GameOfLife.BoardServer` process existing on the first node started in the cluster.

`GameOfLife.GamePrinter` is a simple module using [Agent](http://elixir-lang.org/docs/stable/elixir/Agent.html) in order to keep TRef (time reference) so we can print the board to STDOUT with the specified interval. We will use [Erlang timer module](http://erlang.org/doc/man/timer.html#apply_interval-4) to print the board on the screen every second.

You may wonder what’s the difference between GenServer and Agent.

A GenServer is a process like any other Elixir process and it can be used to keep state, execute code asynchronously, and so on. The advantage of using a generic server process (GenServer) is that it will have a standard set of interface functions and include functionality for tracing and error reporting. It also fits into a supervision tree as this is what we did in the `GameOfLife` module.

On the other hand, Agent is a much simpler solution than GenServer. Agents are a simple abstraction around state. Often in Elixir there is a need to share or store state that must be accessed from different processes or by the same process at different points in time. The Agent module provides a basic server implementation that allows state to be retrieved and updated via a simple API. This is what we are going to do in `GameOfLife.GamePrinter` as we only need to keep time reference to our timer interval.

### Create node manager for task supervisor

Let’s start with something simple just to see if we can distribute work across nodes in the cluster. We assume each new process created by task supervisor will be assigned randomly to one of the connected nodes. Each node should be equally overloaded with the assumption that each task is pretty similar and all nodes are machines with the same configuration and overload.

```
# lib/game_of_life/node_manager.exdefmodule GameOfLife.NodeManager do  def all_nodes do    [Node.self | Node.list]  end  def random_node do    all_nodes |&gt; Enum.random  endend
```

Our node manager has `random_node/0` function which returns the name of a random node connected to the cluster. Basically, that’s it. A simple solution should be enough for now.

### Create board helper functions

We need some helper functions for operations we can do on the board like adding and removing cells. Let’s start with tests for the module `GameOfLife.Board` and function `add_cells/2`.

```
# test/game_of_life/board_test.exsdefmodule GameOfLife.BoardTest do  use ExUnit.Case, async: true  test "add new cells to alive cells without duplicates" do    alive_cells = [{1, 1}, {2, 2}]    new_cells = [{0, 0}, {1, 1}]    actual_alive_cells = GameOfLife.Board.add_cells(alive_cells, new_cells)                          |&gt; Enum.sort    expected_alive_cells = [{0, 0}, {1, 1}, {2, 2}]    assert actual_alive_cells == expected_alive_cells  endend
```

We need to ensure we won’t allow adding the same cell twice to the board so we test that there are no duplicates. Here is the implementation for `add_cells/2` function:

```
# lib/game_of_life/board.exdefmodule GameOfLife.Board do  def add_cells(alive_cells, new_cells) do    alive_cells ++ new_cells    |&gt; Enum.uniq  endend
```

Another thing is removing cells from the list of alive cells:

```
# test/game_of_life/board_test.exstest "remove cells which must be killed from alive cells" do  alive_cells = [{1, 1}, {4, -2}, {2, 2}, {2, 1}]  kill_cells = [{1, 1}, {2, 2}]  actual_alive_cells = GameOfLife.Board.remove_cells(alive_cells, kill_cells)  expected_alive_cells = [{4, -2}, {2, 1}]  assert actual_alive_cells == expected_alive_cellsend
```

Implementation is super simple:

```
# lib/game_of_life/board.exdef remove_cells(alive_cells, kill_cells) do  alive_cells -- kill_cellsend
```

Let’s create something more advanced. We should determine which cells should still live in the next generation after the tick. Here is a test for the `GameOfLife.Board.keep_alive_tick/1` function:

```
# test/game_of_life/board_test.exstest "alive cell with 2 neighbours lives on to the next generation" do  alive_cells = [{0, 0}, {1, 0}, {2, 0}]  expected_alive_cells = [{1, 0}]  assert GameOfLife.Board.keep_alive_tick(alive_cells) == expected_alive_cellsend
```

The function `keep_alive_tick` does a few things like creating a new task with `Task.Supervisor` for each alive cell. Tasks will be created across available nodes in the cluster. We calculate if alive cells should stay alive or be removed. The `keep_alive_or_nilify/2` function returns if the cell should live or `nil` otherwise.

We wait with `Task.await/1` until all tasks across all nodes finished their work. Tasks are working in parallel but we need to wait for results from each task. We remove from the list the `nil` values so at the end we end up with only alive cells for the next generation.

```
# lib/game_of_life/board.ex@doc "Returns cells that should still live on the next generation"def keep_alive_tick(alive_cells) do  alive_cells  |&gt; Enum.map(&(Task.Supervisor.async(                {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},                GameOfLife.Board, :keep_alive_or_nilify, [alive_cells, &1])))  |>; Enum.map(&Task.await/1)  |> remove_nil_cellsenddef keep_alive_or_nilify(alive_cells, cell) do  if GameOfLife.Cell.keep_alive?(alive_cells, cell), do: cell, else: nilenddefp remove_nil_cells(cells) do  cells  |> Enum.filter(fn cell -&gt; cell != nil end)end
```

There is one more case we should handle which is a situation when dead cells should become alive. `GameOfLife.Board.become_alive_tick/1` function will be responsible for that.

```
# test/game_of_life/board_test.exstest "dead cell with three live neighbours becomes a live cell" do  alive_cells = [{0, 0}, {1, 0}, {2, 0}, {1, 1}]  born_cells = GameOfLife.Board.become_alive_tick(alive_cells)  expected_born_cells = [{1, -1}, {0, 1}, {2, 1}]  assert born_cells == expected_born_cellsend
```

This is how our function looks like:

```
# lib/game_of_life/board.ex@doc "Returns new born cells on the next generation"def become_alive_tick(alive_cells) do  GameOfLife.Cell.dead_neighbours(alive_cells)  |&gt; Enum.map(&(Task.Supervisor.async(                {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},                GameOfLife.Board, :become_alive_or_nilify, [alive_cells, &1])))  |>; Enum.map(&Task.await/1)  |> remove_nil_cellsenddef become_alive_or_nilify(alive_cells, dead_cell) do  if GameOfLife.Cell.become_alive?(alive_cells, dead_cell), do: dead_cell, else: nilend
```

It works similarly to `GameOfLife.Board.keep_alive_tick/1`. First, we are looking for the dead neighbours of alive cells. Then for each dead cell we create a new process across the nodes in the cluster to determine if the dead cell should become alive in the next generation.

You can see the full source code of [GameOfLife.Board module](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/lib/game_of_life/board.ex) and [tests on github](https://github.com/BeyondScheme/elixir-game_of_life/blob/master/test/game_of_life/board_test.exs).

### Create BoardServer

Let’s create `GameOfLife.BoardServer` generic server behaviour. We define a public interface for the server.

```
# lib/game_of_life/board_server.exdefmodule GameOfLife.BoardServer do  use GenServer  require Logger  @name {:global, __MODULE__}  @game_speed 1000 # miliseconds  # Client  def start_link(alive_cells) do    case GenServer.start_link(__MODULE__, {alive_cells, nil, 0}, name: @name) do      {:ok, pid} -&gt;        Logger.info "Started #{__MODULE__} master"        {:ok, pid}      {:error, {:already_started, pid}} ->        Logger.info "Started #{__MODULE__} slave"        {:ok, pid}    end  end  def alive_cells do    GenServer.call(@name, :alive_cells)  end  def generation_counter do    GenServer.call(@name, :generation_counter)  end  def state do    GenServer.call(@name, :state)  end  @doc """  Clears board and adds only new cells.  Generation counter is reset.  """  def set_alive_cells(cells) do    GenServer.call(@name, {:set_alive_cells, cells})  end  def add_cells(cells) do    GenServer.call(@name, {:add_cells, cells})  end  def tick do    GenServer.cast(@name, :tick)  end  def start_game(speed \\ @game_speed) do    GenServer.call(@name, {:start_game, speed})  end  def stop_game do    GenServer.call(@name, :stop_game)  end  def change_speed(speed) do    stop_game    start_game(speed)  endend
```

As you can see, we use `GenServer` behaviour in our module. The module requires also Logger as we would like to print some info to the STDOUT.

In the `start_link/1` function we start a new `GenServer`. When our generic server starts, it is as a first process in the cluster. Then it becomes the primary process. In the case when there is already a running process with a globally registered name `{:global,__MODULE__}`, we log info that our process will be a replica process with a reference to the existing PID on another node in the cluster.

We store the global name for our server in the attribute `@name`. We use another attribute `@game_speed` for default game speed which is 1000 milliseconds.

In our public interface, we have the `alive_cells/1` function which returns the list of alive cells. Basically, it is the current state of the game (alive cells on the board). This function calls `GenServer` with the registered `@name` and requests `:alive_cells`. We need to implement the `handle_call/3` function for this type of request (`:alive_cells`).

There is another public function `generation_counter/1` which returns how many generations were already processed by the board server.

The `state/1` function returns state that is held by our generic server. The state is represented as the tuple with 3 values like alive cells, TRef (time reference - we want to regenerate board every second) and generation counter. TRef is a very internal thing for the board server so we won’t return this to the outside world. That’s why we will return just alive cells and the generation counter. You will see it later in the implementation for `handle_call(:state, _from, state)`.

You can use the `set_alive_cells/1` function in the case when you want to override the current list of alive cells with a new list.

The `add_cells/1` function will be very useful as we want to be able to add new cells or figures to the board. For instance, we may want to add a blinker pattern to the existing game. You will learn more about patterns later.

![Image](https://cdn-media-1.freecodecamp.org/images/SGbjJ1XyyVP1F7u7KDrJ2mT74d6J3KBxuhw1)
_blinker pattern_

We can manually force the game to calculate the next generation of cells with the `tick/1` function.

The `start_game/1` function is responsible for starting a new timer which calls every second a `tick/1` function. Thanks to that our game will update the list of alive cells within a specified interval which is `@game_speed`.

The last 2 functions are `stop_game/1` and `change_speed/1` which just restart the game and start a new one with the provided speed.

Now you can see how the above functions are working. They are calling server callbacks.

```
# lib/game_of_life/board_server.exdefmodule GameOfLife.BoardServer do  use GenServer  # ...  # Server (callbacks)  def handle_call(:alive_cells, _from, {alive_cells, _tref, _generation_counter} = state) do    {:reply, alive_cells, state}  end  def handle_call(:generation_counter, _from, {_alive_cells, _tref, generation_counter} = state) do    {:reply, generation_counter, state}  end  def handle_call(:state, _from, {alive_cells, _tref, generation_counter} = state) do    {:reply, {alive_cells, generation_counter}, state}  end  def handle_call({:set_alive_cells, cells}, _from, {_alive_cells, tref, _generation_counter}) do    {:reply, cells, {cells, tref, 0}}  end  def handle_call({:add_cells, cells}, _from, {alive_cells, tref, generation_counter}) do    alive_cells = GameOfLife.Board.add_cells(alive_cells, cells)    {:reply, alive_cells, {alive_cells, tref, generation_counter}}  end  def handle_call({:start_game, speed}, _from, {alive_cells, nil = _tref, generation_counter}) do    {:ok, tref} = :timer.apply_interval(speed, __MODULE__, :tick, [])    {:reply, :game_started, {alive_cells, tref, generation_counter}}  end  def handle_call({:start_game, _speed}, _from, {_alive_cells, _tref, _generation_counter} = state) do    {:reply, :game_already_running, state}  end  def handle_call(:stop_game, _from, {_alive_cells, nil = _tref, _generation_counter} = state) do    {:reply, :game_not_running, state}  end  def handle_call(:stop_game, _from, {alive_cells, tref, generation_counter}) do    {:ok, :cancel} = :timer.cancel(tref)    {:reply, :game_stoped, {alive_cells, nil, generation_counter}}  end  def handle_cast(:tick, {alive_cells, tref, generation_counter}) do    keep_alive_task = Task.Supervisor.async(                      {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},                      GameOfLife.Board, :keep_alive_tick, [alive_cells])    become_alive_task = Task.Supervisor.async(                        {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},                        GameOfLife.Board, :become_alive_tick, [alive_cells])    keep_alive_cells = Task.await(keep_alive_task)    born_cells = Task.await(become_alive_task)    alive_cells = keep_alive_cells ++ born_cells    {:noreply, {alive_cells, tref, generation_counter + 1}}  endend
```

Oh, we forgot about tests. In this case, we can use [DocTest](http://elixir-lang.org/docs/stable/ex_unit/ExUnit.DocTest.html). It allows us to generate tests from the code examples existing in a module/function/macro’s documentation.

Our test file is super short:

```
# test/game_of_life/board_server_test.exsdefmodule GameOfLife.BoardServerTest do  use ExUnit.Case  doctest GameOfLife.BoardServerend
```

Let’s add `@moduledoc` to `GameOfLife.BoardServer`.

```
# lib/game_of_life/board_server.exdefmodule GameOfLife.BoardServer do  use GenServer  require Logger  @moduledoc """  ## Example      iex> GameOfLife.BoardServer.start_game      :game_started      iex> GameOfLife.BoardServer.start_game      :game_already_running      iex> GameOfLife.BoardServer.stop_game      :game_stoped      iex> GameOfLife.BoardServer.stop_game      :game_not_running      iex> GameOfLife.BoardServer.change_speed(500)      :game_started      iex> GameOfLife.BoardServer.stop_game      :game_stoped      iex> GameOfLife.BoardServer.set_alive_cells([{0, 0}])      [{0, 0}]      iex> GameOfLife.BoardServer.alive_cells      [{0, 0}]      iex> GameOfLife.BoardServer.add_cells([{0, 1}])      [{0, 0}, {0, 1}]      iex> GameOfLife.BoardServer.alive_cells      [{0, 0}, {0, 1}]      iex> GameOfLife.BoardServer.state      {[{0, 0}, {0, 1}], 0}      iex> GameOfLife.BoardServer.generation_counter      0      iex> GameOfLife.BoardServer.tick      :ok      iex> GameOfLife.BoardServer.generation_counter      1      iex> GameOfLife.BoardServer.state      {[], 1}  """end
```

As you can see we have grouped 3 examples in the `@moduledoc` attribute and they are separated by a new line. When you run tests you will see 3 separate tests.

```
$ mix test test/game_of_life/board_server_test.exsCompiled lib/game_of_life/board_server.ex20:54:30.637 [info]  Started Elixir.GameOfLife.BoardServer master...Finished in 0.1 seconds (0.1s on load, 0.00s on tests)3 tests, 0 failuresRandomized with seed 791637
```

In `GameOfLife.BoardServer` you probably noticed 2 interesting things. First is `GameOfLife.Board` which is called in:

```
# lib/game_of_life/board_server.exdef handle_call({:add_cells, cells}, _from, {alive_cells, tref, generation_counter}) do  alive_cells = GameOfLife.Board.add_cells(alive_cells, cells)  {:reply, alive_cells, {alive_cells, tref, generation_counter}}end
```

As you saw before we added some useful functions to `GameOfLife.Board` module which helps us to do operations on the list of alive cells.

Another interesting thing is how we use `Task.Supervisor` in:

```
# lib/game_of_life/board_server.exdef handle_cast(:tick, {alive_cells, tref, generation_counter}) do    keep_alive_task = Task.Supervisor.async(                      {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},                      GameOfLife.Board, :keep_alive_tick, [alive_cells])    become_alive_task = Task.Supervisor.async(                        {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},                        GameOfLife.Board, :become_alive_tick, [alive_cells])    keep_alive_cells = Task.await(keep_alive_task)    born_cells = Task.await(become_alive_task)    alive_cells = keep_alive_cells ++ born_cells    {:noreply, {alive_cells, tref, generation_counter + 1}}  end
```

What we are doing here is spinning off a new async process to run the `GameOfLife.keep_alive_tick/1` function with the argument `alive_cells`.

```
# lib/game_of_life/board_server.exkeep_alive_task = Task.Supervisor.async(                  {GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node},                  GameOfLife.Board, :keep_alive_tick, [alive_cells])
```

The tuple `{GameOfLife.TaskSupervisor, GameOfLife.NodeManager.random_node}` tells `Task.Supervisor` that we want to use task supervisor with the name `GameOfLife.TaskSupervisor` and we want to run the process on the node returned by the `GameOfLife.NodeManager.random_node` function.

### Create game printer and console presenter

`GameOfLife.GamePrinter` module is running as a worker under the supervision of the `GameOfLife` supervisor. `GameOfLife.GamePrinter` is using `Agent` to store `TRef` for timer reference as we want to print the board to the STDOUT with the specified interval.

You have already seen the example of using `Agent` so this shouldn’t be new for you. Basically, we wrote the public interface to start and stop printing the board to the screen. For tests we used [DocTest](http://elixir-lang.org/docs/stable/ex_unit/ExUnit.DocTest.html).

```
# lib/game_of_life/game_printer.exdefmodule GameOfLife.GamePrinter do  @moduledoc """  ## Example      iex> GameOfLife.GamePrinter.start_printing_board      :printing_started      iex> GameOfLife.GamePrinter.start_printing_board      :already_printing      iex> GameOfLife.GamePrinter.stop_printing_board      :printing_stopped      iex> GameOfLife.GamePrinter.stop_printing_board      :already_stopped  """  @print_speed 1000  def start_link do    Agent.start_link(fn -> nil end, name: __MODULE__)  end  def start_printing_board do    Agent.get_and_update(__MODULE__, __MODULE__, :do_start_printing_board, [])  end  def do_start_printing_board(nil = _tref) do    {:ok, tref} = :timer.apply_interval(@print_speed, __MODULE__, :print_board, [])    {:printing_started, tref}  end  def do_start_printing_board(tref), do: {:already_printing, tref}  def print_board do    {alive_cells, generation_counter} = GameOfLife.BoardServer.state    alive_counter = alive_cells |> Enum.count    GameOfLife.Presenters.Console.print(alive_cells, generation_counter, alive_counter)  end  def stop_printing_board do    Agent.get_and_update(__MODULE__, __MODULE__, :do_stop_printing_board, [])  end  def do_stop_printing_board(nil = _tref), do: {:already_stopped, nil}  def do_stop_printing_board(tref) do    {:ok, :cancel} = :timer.cancel(tref)    {:printing_stopped, nil}  endend
```

`GameOfLife.Presenters.Console` is responsible for printing the board nicely with X & Y axes, the number of alive cells, and the generation counter. Let’s start with tests. We are going to capture STDOUT and compare if data printed to the screen are looking as we expect.

```
# test/game_of_life/presenters/console_test.exsdefmodule GameOfLife.Presenters.ConsoleTest do  use ExUnit.Case  # allows to capture stuff sent to stdout  import ExUnit.CaptureIO  test "print cells on the console output" do    cell_outside_of_board = {-1, -1}    cells = [{0, 0}, {1, 0}, {2, 0}, {1, 1}, {0, 2}, cell_outside_of_board]    result = capture_io fn -&gt;      GameOfLife.Presenters.Console.print(cells, 123, 6, 0, 2, 2, 2)    end    assert result == (    "    2| O,,\n" <>    "    1| ,O,\n" <>    "    0| OOO\n" <>    "     | _ _ \n" <;&gt;    "    /  0    \n" &lt;>    "Generation: 123\n" &lt;&gt;    "Alive cells: 6\n"    )  endend
```

Here is the implementation of our print function:

```
# lib/game_of_life/presenters/console.exdefmodule GameOfLife.Presenters.Console do  @doc """  Print cells to the console output.  Board is visible only for specified size for x and y.  Start x and y are in top left corner of the board.  `x_padding` Must be a prime number. Every x divided by the prime number  will be visible on x axis.  `y_padding` Any number. Padding for numbers on y axis.  """  def print(cells, generation_counter, alive_counter, start_x \\ -10, start_y \\ 15, x_size \\ 60,            y_size \\ 20, x_padding \\ 5, y_padding \\ 5) do    end_x = start_x + x_size    end_y = start_y - y_size    x_range = start_x..end_x    y_range = start_y..end_y    for y &lt;- y_range, x <- x_range do      # draw y axis      if x == start_x do        (y        |>; Integer.to_string        |> String.rjust(y_padding)) <&gt; "| "        |&gt; IO.write      end      IO.write(if Enum.member?(cells, {x, y}), do: "O", else: ",")      if x == end_x, do: IO.puts ""    end    # draw x axis    IO.write String.rjust("| ", y_padding + 2)    x_length = (round((end_x-start_x)/2))    for x &lt;- 0..x_length, do: IO.write "_ "    IO.puts ""    IO.write String.rjust("/  ", y_padding + 2)    for x <- x_range do      if rem(x, x_padding) == 0 do        x        |&gt; Integer.to_string        |> String.ljust(x_padding)        |&gt; IO.write      end    end    IO.puts ""    IO.puts "Generation: #{generation_counter}"    IO.puts "Alive cells: #{alive_counter}"  endend
```

The board with the bigger visible part looks like this:

```
   15| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   14| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   13| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   12| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   11| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   10| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    9| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    8| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    7| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    6| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    5| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    4| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    3| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    2| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    1| ,,,,,,,,,,OO,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    0| ,,,,,,,,,,OO,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -1| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -2| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -3| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -4| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   -5| ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _    /  -10  -5   0    5    10   15   20   25   30   35   40   45   50Generation: 18Alive cells: 4
```

Last step is to uncomment the `GameOfLife.GamePrinter` worker in:

```
# lib/game_of_life.exdefmodule GameOfLife do  use Application  # See http://elixir-lang.org/docs/stable/elixir/Application.html  # for more information on OTP Applications  def start(_type, _args) do    import Supervisor.Spec, warn: false    init_alive_cells = []    children = [      # Define workers and child supervisors to be supervised      # worker(GameOfLife.Worker, [arg1, arg2, arg3]),      supervisor(Task.Supervisor, [[name: GameOfLife.TaskSupervisor]]),      worker(GameOfLife.BoardServer, [init_alive_cells]),      # This line is uncommented now      worker(GameOfLife.GamePrinter, []),    ]    # See http://elixir-lang.org/docs/stable/elixir/Supervisor.html    # for other strategies and supported options    opts = [strategy: :one_for_one, name: GameOfLife.Supervisor]    Supervisor.start_link(children, opts)  endend
```

### Add figure patterns and place them on the board

To play our game of life, it would be great to have an easy way to add figures to the board. There are many commonly known patterns like still lifes, oscillators, and spaceships. You can [learn more about them here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns).

One interesting pattern is the gun. The Gosper Glider Gun is a very popular pattern. Here it is how it looks:

![Image](https://cdn-media-1.freecodecamp.org/images/wxl-EjJX2Bn1aQ82Mp6p0hhFLMUnSjwpMyHy)
_Gosper Glider Gun_

When you run game the pattern behaves as you see. The gun is shooting.

![Image](https://cdn-media-1.freecodecamp.org/images/ROo3D4AEbeI2atC5gYBi3Snfk1-TiAsDmMdk)
_Gosper Glider Gun pattern live cycle_

Let’s write this pattern down. Imagine you want to put the pattern in a rectangle. Left bottom corner of the rectangle is at `{0,0}` position.

```
# lib/game_of_life/patterns/guns.exdefmodule GameOfLife.Patterns.Guns do  @moduledoc """  https://en.wikipedia.org/wiki/Gun_(cellular_automaton)  """  @doc """  https://en.wikipedia.org/wiki/File:Game_of_life_glider_gun.svg  """  def gosper_glider do    [      {24, 8},      {22, 7}, {24, 7},      {12, 6}, {13, 6}, {20, 6}, {21, 6}, {34, 6}, {35, 6},      {11, 5}, {15, 5}, {20, 5}, {21, 5}, {34, 5}, {35, 5},      {0, 4}, {1, 4}, {10, 4}, {16, 4}, {20, 4}, {21, 4},      {0, 3}, {1, 3}, {10, 3}, {14, 3}, {16, 3}, {17, 3}, {22, 3}, {24, 3},      {10, 2}, {16, 2}, {24, 2},      {11, 1}, {15, 1},      {12, 0}, {13, 0},    ]  endend
```

It would be also useful if we could place the pattern on the board in the position specified by us. Let’s write a pattern converter.

```
# lib/game_of_life/pattern_converter.exdefmodule GameOfLife.PatternConverter do  @doc """  ## Example      iex> GameOfLife.PatternConverter.transit([{0, 0}, {1, 3}], -1, 2)      [{-1, 2}, {0, 5}]  """  def transit([{x, y} | cells], x_padding, y_padding) do    [{x + x_padding, y + y_padding} | transit(cells, x_padding, y_padding)]  end  def transit([], _x_padding, _y_padding), do: []end
```

This is the way you can add the Gosper glider pattern to the board with the specified position.

```
GameOfLife.Patterns.Guns.gosper_glider|&gt; GameOfLife.PatternConverter.transit(-2, -3)|> GameOfLife.BoardServer.add_cells
```

You can find [more patterns in modules here](https://github.com/BeyondScheme/elixir-game_of_life/tree/master/lib/game_of_life/patterns).

### Run game across multiple nodes

Now it is time to run our game. The full [source code can be found here](https://github.com/BeyondScheme/elixir-game_of_life).

Let’s run the first node where the `GameOfLife.BoardServer` will be running.

```
$ iex --sname node1 -S mixErlang/OTP 18 [erts-7.3] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]Interactive Elixir (1.2.4) - press Ctrl+C to exit (type h() ENTER for help)16:54:08.554 [info]  Started Elixir.GameOfLife.BoardServer masteriex(node1@Artur)1> GameOfLife.BoardServer.start_game:game_startediex(node1@Artur)2> GameOfLife.GamePrinter.start_printing_board:printing_started
```

In another terminal window, you can start the second node. We will connect it with the first node.

```
$ iex --sname node2 -S mixErlang/OTP 18 [erts-7.3] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]Interactive Elixir (1.2.4) - press Ctrl+C to exit (type h() ENTER for help)16:55:17.395 [info]  Started Elixir.GameOfLife.BoardServer masteriex(node2@Artur)1> Node.connect :node1@Arturtrue16:55:17.691 [info]  Started Elixir.GameOfLife.BoardServer slaveiex(node2@Artur)2> Node.list[:node1@Artur]iex(node2@Artur)3> Node.self:node2@Arturiex(node2@Artur)4> GameOfLife.Patterns.Guns.gosper_glider |> GameOfLife.BoardServer.add_cells[{24, 8}, {22, 7}, {24, 7}, {12, 6}, {13, 6}, {20, 6}, {21, 6}, {34, 6}, {35, 6}, {11, 5}, {15, 5}, {20, 5}, {21, 5}, {34, 5}, {35, 5}, {0, 4}, {1, 4}, {10, 4}, {16, 4}, {20, 4}, {21, 4}, {0, 3}, {1, 3}, {10, 3}, {14, 3}, {16, 3}, {17, 3}, {22, 3}, {24, 3}, {10, 2}, {16, 2}, {24, 2}, {11, 1}, {15, 1}, {12, 0}, {13, 0}]
```

Both nodes are executing a calculation to determine a new state for living cells. You can run the game also across different servers in the network like this:

```
# start node1$ iex --name node1@192.168.0.101 --cookie "token_for_cluster" -S mix# start node2 on another server$ iex --name node2@192.168.0.102 --cookie "token_for_cluster" -S mixiex> Node.connect :"node1@192.168.0.101"true
```

You already saw how the game works in the demo at the beginning of the article. You can try it on your own machine, just clone the [repository](https://github.com/BeyondScheme/elixir-game_of_life).

### Summary

Finally, we managed to get to the end. It was a pretty long road but we have a working game, distributed across nodes. We learned how to write GenServer, use Agents, split processes across nodes with TaskSupervisor and connect nodes into the cluster. You also saw examples of tests in Elixir and how to use DocTest.

Hope you found something interesting in the article. Please share your thoughts in the comments.

Nowadays I work on CI parallelisation problem to run tests fast on CI servers. I built [**Knapsack Pro which splits your Ruby and JavaScript tests on parallel CI nodes to save time on testing**](https://knapsackpro.com?utm_source=medium&utm_medium=blog&utm_campaign=game_of_life_elixir&utm_content=knapsackpro). You can check one of my articles about [Cypress in JavaScript test suite parallelisation](https://medium.com/@arturtrzop/cypress-e2e-tests-split-with-ci-parallelisation-and-auto-balancing-ci-nodes-time-8c6c8b0a37f1) or [Heroku CI parallelisation](https://medium.com/datadriveninvestor/heroku-ci-parallel-test-runs-done-with-optimal-test-suite-split-how-to-run-parallel-dynos-79903d9a0ec6). Let me know how slow or fast your tests are in your Elixir projects — just leave a comment. :) I’d like to add support for CI parallelisation testing into Elixir as well.

