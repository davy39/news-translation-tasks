---
title: What Are Monte Carlo Methods? How to Predict the Future with Python Simulations
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-07-16T21:42:38.000Z'
originalURL: https://freecodecamp.org/news/what-are-monte-carlo-methods
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-matej-117839-716661.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Monte Carlo methods have revolutionized programming and engineering.

  These methods use the power of randomness, which makes them effective tools that
  help developers solve difficult problems in many fields.

  Monte Carlo methods have been adopted in ph...'
---

Monte Carlo methods have revolutionized programming and engineering.

These methods use the power of randomness, which makes them effective tools that help developers solve difficult problems in many fields.

Monte Carlo methods have been adopted in physics, finance, engineering and many other areas where deterministic methods are often impractical to solve problems.

With Monte Carlo methods, simulations and very complex computations have become efficient and easy to manage.

There are many variants of Monte Carlo methods. But all of them share the idea of using randomness to approximate solutions to hard problems. In this article, you'll learn all about Monte Carlo methods.

## What we'll cover:

* [Understanding Monte Carlo Methods Through an Analogy](#heading-understanding-monte-carlo-methods-through-an-analogy)
* [What Are Monte Carlo Methods? A Plain English Guide](#heading-what-are-monte-carlo-methods-a-plain-english-guide)
* [Real-World Applications of Monte Carlo Methods](#heading-real-world-applications-of-monte-carlo-methods)
* [Different Types of Monte Carlo Methods](#heading-exploring-different-types-of-monte-carlo-methods)
* [Practical Implementation: Monte Carlo Methods in Python](#heading-practical-implementation-monte-carlo-methods-in-python)
* [The Future of Monte Carlo Methods](#heading-conclusion-the-future-of-monte-carlo-methods)

### Pre-requisites

You should have a basic knowledge of statistics to understand everything in this article.

If you need to brush up on your stats skills, I recommend checking out this freeCodeCamp course:

%[https://www.youtube.com/watch?v=xxpc-HPKN28]

<h2 id ="understanding">Understanding Monte Carlo Methods Through an Analogy</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2.jpg)
_Photo by [veeterzy on Pexels](https://www.pexels.com/photo/green-leafed-tree-38136/)_

Imagine you want to find the average height of trees in a big forest.

Measuring every tree is impossible and impractical. But with Monte Carlo methods, it's possible to randomly select a few spots in the forest and measure the height of all the trees in those spots.

By doing this many times and averaging all these measurements, we can estimate the average height of all the trees in the forest.

This way, it's possible to make great estimations in large and complex populations by finding small and manageable samples and averaging them out.

<h2 id ="what">What Are Monte Carlo Methods? A Plain English Guide</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/pexels.jpg)
_Photo by [Jonathan Petersson on Pexels](https://www.pexels.com/photo/photo-of-two-red-dices-965879/)_

Monte Carlo methods are a type of computer algorithm that uses repeated random measurements to obtain approximate results for a given problem.

They are a part of the mathematical field called [numerical analysis](https://www.freecodecamp.org/news/numerical-analysis-explained-how-to-apply-math-with-python/) – the use of approximation methods to find solutions where deterministic methods are impractical.

The main idea is to find good enough approximate solutions to solve problems that are too hard or impossible to solve directly.

These solutions are obtained by getting an average of many randomly chosen samples from the population of the problem at hand.

This way, in systems with many uncertain factors and interacting parts, Monte Carlo methods are able to provide insights into how the system behaves and performs.

They are based on the mathematical idea of the [Law of large numbers](https://www.investopedia.com/terms/l/lawoflargenumbers.asp) in probability theory:

> The average of many independent, identically distributed random variables converges to the expected value, if it exists.

The main problem of Monte Carlo methods is the lack of computer resources to make many simulations to get good results.

### Why are they called "Monte Carlo"?

Monte Carlo methods, named after the [Monte Carlo Casino in Monaco](https://www.montecarlosbm.com/en/casino-monaco/casino-monte-carlo), were coined by mathematicians during the 1940s Manhattan Project.

[Stanislaw Ulam](https://www.britannica.com/biography/Stanislaw-Ulam), [John von Neumann](https://www.britannica.com/biography/John-von-Neumann), and others were involved in this project, which developed the American nuclear bomb. 

The name reflects the randomness in their simulations, akin to the random outcomes in casino gambling.

<h2 id ="real">Real-World Applications of Monte Carlo Methods</h2>

### Circuit design in electrical engineering

![Image](https://www.freecodecamp.org/news/content/images/2024/07/circuit.jpg)
_Photo from [Pixabay](https://www.pexels.com/photo/close-up-photography-of-computer-motherboard-163125/)_

Circuits have many components. Here are some of them:

* Resistors
* Inductors
* Capacitors
* Diodes
* Transistors

Because of the temperatures of the environment they're in, sometimes the circuits may not work.

So, how do engineers design temperature-resilient circuits?

In other words: how can we test a circuit's performance at different temperatures?

Thanks to Monte Carlo methods, we can simulate many intervals of temperature conditions and see their effects on circuit components and how much they affect circuit performance.

This way, we can gather data on how the components should perform under different thermal stresses.

This way, we can optimize the circuit – whether to change the circuit design or choose different components – to work across many environmental conditions.

### Rocket design in aerospace engineering

![Image](https://www.freecodecamp.org/news/content/images/2024/07/rocket.jpg)
_Photo from [Pixabay](https://www.pexels.com/photo/white-rocket-2159/)_

Rocket design involves many different variables, such as: 

* Material properties 
* Aerodynamic forces 
* Propulsion efficiency 
* Environmental conditions. 

Monte Carlo methods allow for numerous simulations with varying material properties, propulsion efficiency, and more design variables.

This helps in deeply understanding rocket behavior under diverse conditions.

In essence, this stochastic way of solving a big problem is key in understanding the probability behavior of the rocket's performance, like:

* Trajectory
* Stability 
* Structural integrity 

By analyzing how these design variables affect the probability behavior of crucial rocket flying performance metrics, engineers can make rockets safer and more reliable.

### Financial Portfolio optimization in finance and investing

![Image](https://www.freecodecamp.org/news/content/images/2024/07/finance.jpg)
_Photo by [energepic.com](https://www.pexels.com/photo/close-up-photo-of-monitor-159888/)_

In finance portfolio optimization, what is the best mix of assets in a portfolio to maximize returns while minimizing risk?

Monte Carlo methods are used to [simulate](https://www.quantconnect.com/learning/articles/introduction-to-options/stochastic-processes-and-monte-carlo-method) how good a portfolio is at maximizing returns while minimizing risk under various market conditions.

By generating many random scenarios for asset prices and returns, banks and financial institutions can know, under different conditions, portfolio outcomes and manage risk.

This way, it's possible to make data-driven decisions to find a balance between risk and rewards.

<h2 id ="exploring">Exploring Different Types of Monte Carlo Methods</h2>

There are many variants of Monte Carlo methods. Here are some of the most important:

### Classical Monte Carlo:

Classical Monte Carlo uses random samples to estimate values and simulate systems. It's useful for tasks where direct solutions are hard to find, like numerical integration

### Bayesian Monte Carlo: 

Bayesian Monte Carlo improves estimations by using existing information with new observations to make better predictions.

It is called Bayesian Monte Carlo because it uses [Bayes' theorem](https://www.freecodecamp.org/news/bayes-rule-explained/).

Bayes' theorem was created by the mathematician Thomas Bayes and it's very important in probability theory.

The main idea of the theorem is to **revise existing beliefs with new data.**

This method is ideal when you have some existing information about the problem.

### Markov Chain Monte Carlo (MCMC): 

For large datasets, Monte Carlo methods often take too long to compute results.

One way to solve this problem is to use a smaller version of big datasets. This is kind of like how a summary **represents** the content of a book because it is quicker to read.

This smaller version is called a [Markov Chain](https://www.freecodecamp.org/news/what-is-a-markov-chain/).

In simple words, Markov Chains are models that show how a system moves between states.

A large dataset can be seen as a system and the states as patterns of data.

This way, Markov Chains are simple models that can **represent** a large dataset because they show how things change from one state to another.

This state change can represent, with fewer numbers, the important patterns in the data.

This way, from the Markov Chain, the Monte Carlo method computes its results.

Essentially, the Monte Carlo makes its predictions **indirectly** from the original data. The Markov Chain acts as a **data preprocessing** step to compute the Monte Carlo results.

In the end, MCMC is just a regular but far more computationally efficient Monte Carlo method.

### Other variants

Other methods like _Gradient, Semi-Gradient, and Quasi Monte Carlo_ focus as well on computational efficiency. But in this article, I only seek to highlight the importance of Monte Carlo methods in science, engineering, and programming.

<h2 id ="pratical">Practical Implementation: Monte Carlo Methods in Python</h2>

In the code below, you will see how to implement an MCMC variant in Python.

I'll demo a popular variant of MCMC called Hamiltonian Monte Carlo (HMC).

It is called Hamiltonian because it uses concepts from Hamiltonian mechanics to propose new states for the Markov chains in the data pre-processing step.

### What is Hamiltonian Mechanics?

To answer this, you need to know a bit about classical mechanics.

Classical mechanics uses Newton's laws of motion to explain how physical systems behave and change over time. 

Hamiltonian mechanics is another way to look at these systems. It often emphasizes the role of energy and its conservation by using different variables like generalized positions and momenta.

This unique way of describing a system's state and evolution is used in HMC.

### Main code example objective

We will create a target distribution from a 2D Gaussian distribution using TensorFlow Probability. This means that the HMC will model this target distribution.

The 2D Gaussian distribution is created with synthetic data to demonstrate the approximation process using Hamiltonian Monte Carlo.

In other words, HMC will represent this 2D Gaussian distribution accurately.

In real-life scenarios, from circuits to finance, all systems can be described as a probability distribution. 

The Monte Carlo methods approximate these complex distributions. And the MCMC makes this process far faster.

In this simple code example, I am approximating a simple target distribution so that you can understand how, in a real life scenario, this would be applied.

Here is the full code (we'll walk through it step by step below):

```
import tensorflow as tf
import tensorflow_probability as tfp

# Define the target distribution (2D Gaussian)
def target_log_prob(x, y):
    return -0.5 * (x**2 + y**2)

# Initialize the HMC transition kernel
num_results = 1000
num_burnin_steps = 500

hmc = tfp.mcmc.HamiltonianMonteCarlo(
    target_log_prob_fn=lambda x, y: target_log_prob(x, y),
    num_leapfrog_steps=3,
    step_size=0.1
)

# Define the trace function to record the state and kernel results
@tf.function
def run_chain(initial_state, kernel, num_results, num_burnin_steps):
    return tfp.mcmc.sample_chain(
        num_results=num_results,
        num_burnin_steps=num_burnin_steps,
        current_state=initial_state,
        kernel=kernel,
        trace_fn=lambda _, pkr: pkr
    )

# Run the MCMC chain
initial_state = [tf.zeros([]), tf.zeros([])]
samples, kernel_results = run_chain(initial_state, hmc, num_results, num_burnin_steps)

# Extract the samples and log
samples_ = [s.numpy() for s in samples]
samples_x, samples_y = samples_

print("Acceptance rate: ", kernel_results.is_accepted.numpy().mean())
print("Mean of x: ", samples_x.mean())
print("Mean of y: ", samples_y.mean())

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/1-3.png)
_Pratical implementation of Markov Chain Monte Carlo Method_

Let's understand how the code works step by step.

### Import the libraries

```
import tensorflow as tf
import tensorflow_probability as tfp
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2-2.png)
_Importing libraries_

In this code, we import two Python libraries: 

* [TensorFlow](https://www.tensorflow.org/): Building and training machine learning models 
* [TensorFlow Probability](https://www.tensorflow.org/probability): Probabilistic reasoning and statistical modeling

### Create a target distribution

```
def target_log_prob(x, y):
    return -0.5 * (x**2 + y**2)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-1.png)
_Creating target distribution_

In this code, we define a 2D Gaussian distribution:

![Image](https://www.freecodecamp.org/news/content/images/2024/07/output-1.png)
_2D Gaussian distribution_

This graph is defined by:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Equation Display</title>
    <style>
        .equation {
            font-family: 'Times New Roman', Times, serif;
            font-size: 24px;
            text-align: center;
            width: 100%;
            margin-top: 20px; /* Optional: Adds some space above the equation */
        }
    </style>
</head>
<body>
    <div class="equation">
        -0.5 &times; (x<sup>2</sup> + y<sup>2</sup>)
    </div>
</body>
</html>


By being a 2D Gaussian distribution, each data point is represented by two correlated variables that follow a joint Gaussian distribution. 

If this were a real-life scenario, we would be modeling a system by finding its probability distribution based on two variables.

In many practical applications, such as circuits, there can be dozens of variables involved. 

To model such systems correctly, we often use multivariate probability distributions, which generalize the concept of the Gaussian distribution to many dimensions.

### Initialize the Markov Chain Monte Carlo

```
num_results = 1000
num_burnin_steps = 500

hmc = tfp.mcmc.HamiltonianMonteCarlo(
    target_log_prob_fn=lambda x, y: target_log_prob(x, y),
    num_leapfrog_steps=3,
    step_size=0.1
)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4-1.png)
_Initializing the Markov Chain Monte Carlo_

This block of code sets up a Hamiltonian Monte Carlo (HMC) transition kernel using TensorFlow Probability. 

It first defines two variables:

* `num_results` as 1000, indicating the number of samples to generate
* `num_burnin_steps` as 500, representing the number of initial samples to discard (burn-in period).

The HMC transition kernel is set up with:

* A target log probability function that takes two inputs and returns their log probability. In our case, the target log probability function is the 2D gaussian distribution. The log probability is the likelihood of a particular set of values.
* The algorithm takes 3 steps each time.
* Each step size (Change amount) is 0.1.

### Create the trace function to record the state and kernel results

```
@tf.function
def run_chain(initial_state, kernel, num_results, num_burnin_steps):
    return tfp.mcmc.sample_chain(
        num_results=num_results,
        num_burnin_steps=num_burnin_steps,
        current_state=initial_state,
        kernel=kernel,
        trace_fn=lambda _, pkr: pkr
    )
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/5-1.png)
_Creating the trace function to record the state and kernel results_

The function is decorated with `@tf.function`, which optimizes it for performance by compiling it into a TensorFlow graph.

The function `run_chain` takes four arguments:

1. `initial_state`: The initial state of the Markov Chain.
2. `kernel`: The MCMC transition kernel to use (such as Hamiltonian Monte Carlo).
3. `num_results`: The number of samples to generate.
4. `num_burnin_steps`: The number of initial samples to discard (burn-in period).

The function calls `tfp.mcmc.sample_chain` to perform the MCMC sampling:

* `num_results`: The number of samples to draw.
* `num_burnin_steps`: The number of burn-in steps.
* `current_state`: The starting state of the Markov Chain.
* `kernel`: The transition kernel that defines the sampling process.
* `trace_fn`: A function that specifies what to trace during sampling. In this case, it returns the previous kernel results (`pkr`), effectively tracing the internal state of the MCMC algorithm.

### Run the MCMC chain

```
# Run the MCMC chain
initial_state = [tf.zeros([]), tf.zeros([])]
samples, kernel_results = run_chain(initial_state, hmc, num_results, num_burnin_steps)

# Extract the samples and log
samples_ = [s.numpy() for s in samples]
samples_x, samples_y = samples_

print("Acceptance rate: ", kernel_results.is_accepted.numpy().mean())
print("Mean of x: ", samples_x.mean())
print("Mean of y: ", samples_y.mean())

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/6.png)
_Running the MCMC chain_

Alright let's break this down as there's a lot going on here:

**Initialize the State**:

* `initial_state` is set to a list containing two zero tensors, which serves as the starting point for the Markov Chain.

**Run the MCMC Chain**:

* The `run_chain` function is called with the initial state, the HMC kernel, the number of results, and the number of burn-in steps.
* The function returns two values: `samples`, which are the generated samples, and `kernel_results`, which contain the results from the kernel (including diagnostic information).

**Extract and Convert Samples**:

* The samples are converted from TensorFlow tensors to NumPy arrays for easier manipulation and analysis.
* `samples_` is a list comprehension that converts each sample tensor to a numpy array.
* `samples_x` and `samples_y` are the extracted samples for the two dimensions.

**Print Diagnostics**:

* The acceptance rate of the MCMC sampler is calculated and printed. It shows the proportion of accepted proposals during sampling.
* The means of the samples for both dimensions (`x` and `y`) are calculated and printed to provide a summary of the sampling results.

This gives as results:

* Acceptance rate: 1.0. This means all proposals made during sampling were accepted
* Mean of x: -0.11450629 and mean of y:  -0.23079416. In a perfect 2D Gaussian distribution, the means of x and y are 0.

With this MCMC variant, we are approximating the 2D Gaussian distribution. But it's close to zero. This means that, given more computational time, it probably would go to an even smaller number until it was so small it could be considered zero.

<h2 id ="conclusion">Conclusion: The future of Monte Carlo methods</h2>

The future of Monte Carlo methods lies in the creation of variants that require fewer computational resources and save time.

With these advancements, Monte Carlo methods will find additional applications in more fields.

Thanks to Monte Carlo methods, we are able to model complex systems and phenomena that were previously impossible to do in an efficient manner.

If you want to know more, you can [read this article on Monte Carlo methods](https://www.freecodecamp.org/news/solve-the-unsolvable-with-monte-carlo-methods-294de03c80cd/).

You can also check out the full code here:

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]


