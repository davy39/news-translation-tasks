---
title: 'How I Built My One-Person Project: A Chess Engine for a Popular Game Dev Engine'
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2020-09-08T23:23:46.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-one-person-open-source-project
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98ca740569d1a4ca1c15.jpg
tags:
- name: open source
  slug: open-source
- name: projects
  slug: projects
- name: side project
  slug: side-project
seo_title: null
seo_desc: 'I recently finished one of my summer projects: a chess GUI engine built
  using the Ren’Py Visual Novel Game Development Engine and the python-chess library.

  This engine will be integrated into a kinetic novel game, The Wind at Dawn, at that
  game’s com...'
---

I recently finished one of my summer projects: [a chess GUI engine](https://github.com/RuolinZheng08/renpy-chess) built using the [Ren’Py Visual Novel Game Development Engine](http://renpy.org/) and the [python-chess](https://github.com/niklasf/python-chess) library.

This engine will be integrated into a kinetic novel game, [*The Wind at Dawn*](https://madeleine-chai.itch.io/the-wind-at-dawn), at that game’s completion.

In this post, I’d like to share some key learnings, technical and non-technical, that I gathered from pushing this one-person project from start to finish in a month.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/foolsmate.gif align="left")

\_\[My Chess Engine Project on GitHub\](https://github.com/RuolinZheng08/renpy-chess" data-href="https://github.com/RuolinZheng08/renpy-chess" class="markup--anchor markup--figure-anchor" rel="noopener" target="*blank)*

## Appreciate the Value of Rewriting Old Code

For CS projects at school, I seldom have the opportunity or experience the need to revisit my code.

However, this is not the case when I work on my passion projects: I love to take every opportunity to improve their usability and reusability in the hope that my code will be of value to other developers.

This chess engine is based on [a chess engine I created in Ren’Py and vanilla Python](https://github.com/RuolinZheng08/renpy-chess-engine) while teaching myself Python during my first summer break in college.

That old chess engine is, in turn, based on a project in my college Intro to CS class (a chess GUI game written in Racket, a functional programming language). That is to say, I’ve rewritten my code twice to produce this final chess engine.

For my first rewrite, I simply “translated” the chess logic (for determining whether a move is legal, endgame conditions, and so on.) from Racket to Python. I also experimented with Object-Oriented Programming, wrote a minimax chess AI following online tutorials, and implemented the GUI in Ren’Py.

Since I only knew the very basics of chess and wrote my chess logic per my school project grading spec, my first chess engine didn’t support special moves like en passant, castling, or promotion.

To address this issue in my second rewrite, I researched open-source Python libraries and found [python-chess](https://github.com/niklasf/python-chess), a library with full support for chess moves and endgame conditions like claiming a draw when threefold repetition occurs.

On top of that, it has also integrated [Stockfish](https://stockfishchess.org/), a chess AI, and this integration will enable my chess engine to configure the strength of the chess AI.

These two features added great value to my chess engine version 2.0 and allowed me to focus on the more important aspects of my rewrite, which I will describe below.

## Read the Documentation and Keep Compatibility in Mind

It has become my habit to skim through the documentation of the libraries that I need for my project before jumping into the design and the code. This helps me evaluate any issue with dependency and compatibility that might arise.

[This Ren’Py GitHub issue](https://github.com/renpy/renpy/issues/2003) points to the fact that Ren’Py uses Python 2 and hasn’t yet been ported to Python 3. So I recognized that I needed a version of python-chess that supports Python 2, [as the latest version only supports Python 3.7+](https://python-chess.readthedocs.io/en/latest/#features).

Fortunately, [version 0.23.10](https://python-chess.readthedocs.io/en/v0.23.10/index.html#features) supports both Python 2.7 and Python 3.4+. I ultimately settled on version 0.23.11 as it is the last version that still supports Python 2.7.

Having sorted through dependency and compatibility issues, I was ready to move on to design and coding.

## Follow Software Engineering Best Practices

Note: A lot of terms mentioned in this section are from [Agile/Scrum](https://en.wikipedia.org/wiki/Scrum_%28software_development%29).

### Gather Feature Requirements for Project Design

While it is tempting to jump straight into coding, I cannot stress enough the importance of design.

Think about design as a high-level roadmap that clearly delineates the starting point, milestones, and ending points of the project. This lets developers refer to when they are waist-deep in intricate implementation details.

This is especially important for extracurricular projects as they don’t usually have a detailed, highly-technical spec, whereas most school projects do.

For my chess engine, I identified the following rewrites/additional features:

* Integrate the chess logic from python-chess
    
* In my Ren’Py GUI code, replace the chess logic and chess AI I wrote with the chess logic and Stockfish APIs from python-chess
    
* Support various gameplay modes: Player vs. Player, Player vs. Computer (where Player can choose to play as black or white), adjustable strength of the chess AI via adjustments to Stockfish’s configuration parameters
    
* Develop a Ren’Py GUI for pawn promotion
    
* Develop a Ren’Py GUI for claiming a draw in the case of threefold repetition or the fifty-move rule
    

### Develop a Proof of Concept Prototype

A Proof of Concept (POC) prototype helps me gauge the time and effort needed to implement the required features.

For my chess engine POC, I integrated python-chess with my original Ren’Py GUI code. I made sure its set of features was minimum yet readily extensible:

* I integrated python-chess with my original Ren’Py GUI code and was able to move pieces around
    
* I only implemented Player vs. Player in order to postpone integrating Stockfish for chess AI
    
* I only allowed non-promotion moves so as to postpone developing the GUI for pawn promotion
    

### Identify the Project’s Definition of Ready and Definition of Done

My project’s Definition of Ready (DoR) naturally follows from my initial investigation about library version compatibility and my POC.

In parallel, my project’s Definition of Done (DoD) follows from the feature requirements I identified from my design phase.

### Deliver a Minimum Viable Product, or better yet, a Minimum Lovable Product

![Image](https://www.freecodecamp.org/news/content/images/2020/09/promotion.gif align="left")

*Promotion UI*

When I was in the design phase gathering requirements, I knew that there were a lot of stretch goals to my project — perhaps even more than I could ever accomplish.

So it was important for me to implement the very basic set of required features, deliver a Minimum Viable Product (MVP), and gather feedback to iterate on it.

Better yet, I’d like to deliver a Minimum Lovable Product (MLP) on my first iteration. The minute difference is that whereas an MVP requires nothing more than functional features, an MLP has a lovable user experience by design.

For instance, to implement pawn promotion moves, for an MVP I could ask users to press different keys to select the piece type they want to promote to (like B for bishop and K for knight).

For an MLP, I would implement a UI with piece-type-shaped buttons that change colors when hovered or selected.

## Be Your Own Project Manager

If you find keeping track of the list of features (plus the ever-growing list of bugs and fixes) overwhelming, you are not alone. It’s time to be your own project manager.

I found [Trello](https://trello.com/) to be an amazing tool both for single-person projects and large-team projects.

This is how I usually organize my Trello board for a coding project:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/board.png align="left")

*The Trello Board for My Chess Engine Project*

Have four lists: **Backlog** (for features to be triaged), **TODO**, **Doing**, and **Done.**

Have color-coded labels:

* **Ready for QA:** A red label to get the attention of my teammates
    
* **Impact:** low (yellow) vs. high (orange), determined by the amount of impact a feature or a bug fix will generate. For example, a slightly misaligned UI panel is of low impact where a deterministically crashing bug is of high impact.
    
* **An estimate of the time it will take to implement:** trivial (&lt; 1 hour, teal), medium (1–2 hours, light blue), and difficult (2–4 hours, dark blue).  
    My other rule of thumb is, if I estimate that a card will take more than 4 hours to implement, I should probably break it down into several finer-grained cards.
    
* Color serves as a great visual cue: I always tackle cards with orange and teal tags (high impact and low time commitment) before tackling those with yellow and difficult tags (low impact but high time commitment).
    

## Write Documentation and Reflect on Your Learning

Having pushed every single Trello card from TODO to Doing to Done and fixed every nasty bug, is it finally time to call a project done? Yes and no.

To maximize my learning from a project, I find it immensely worthwhile to reflect on my takeaways, technical or soft skills:

1. Write a clear, concise README in the GitHub project repository. This helps other developers understand and become interested in the project.
    
2. Write a blog post (like the one I’m writing now) about the higher-level aspects, for example, architecture overview, feature design, challenges and solutions, and so on.
    

![Image](https://www.freecodecamp.org/news/content/images/2020/09/README-1.png align="left")

*My README Section about Integrating My Chess Engine into Other Game Projects*

![Image](https://www.freecodecamp.org/news/content/images/2020/09/-readme1-1.png align="left")

*My README Section Comparing the Two Versions of My Chess Engine*

### Credits & Links

Many thanks to Tim Min for prompting me to work on this project, for his contributions (new feature ideas + QA) on the Trello board, and for holding me accountable. Tim is the writer of the kinetic novel game, [*The Wind at Dawn*](https://madeleine-chai.itch.io/the-wind-at-dawn)*.*

* [My chess engine GitHub repository](https://github.com/RuolinZheng08/renpy-chess)
    
* [The public Trello board for this chess engine project](https://trello.com/b/ip9YLSPa/renpy-chess)
    
* [Ren’Py: a Visual Novel Game Development Engine](https://www.renpy.org/)
    
* [python-chess: a pure Python chess library](https://python-chess.readthedocs.io/en/latest/)
    

Let's stay in touch! Connect with me on [LinkedIn](https://www.linkedin.com/in/ruolin-zheng/), [GitHub](https://github.com/RuolinZheng08), [Medium](https://medium.com/@ruolinzheng), or check out [my personal website](https://ruolinzheng08.github.io/).
