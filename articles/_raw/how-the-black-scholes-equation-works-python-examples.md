---
title: How the Black-Scholes Equation Works – Explained with Python Code Examples
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-06-17T16:42:59.000Z'
originalURL: https://freecodecamp.org/news/how-the-black-scholes-equation-works-python-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/dan-cristian-padure-h3kuhYUCE9A-unsplash.jpg
tags:
- name: finance
  slug: finance
- name: MathJax
  slug: mathjax
- name: Python
  slug: python
seo_title: null
seo_desc: 'The Black-Scholes Equation is probably one of the most influential equations
  that nobody has heard about.

  It''s particularly important in finance, especially in these areas:


  Securitized debt

  Exchange-traded options

  Credit default swaps

  Over-the-count...'
---

The Black-Scholes Equation is probably one of the most influential equations that nobody has heard about.

It's particularly important in finance, especially in these areas:

* Securitized debt
* Exchange-traded options
* Credit default swaps
* Over-the-counter derivatives securities

In this article, you'll learn why the Black-Scholes Equation is so important in finance, what problems it solves, and the industries it created.

### Here's what we'll cover:

* [Prerequisite knowledge of finance](#heading-prerequisite-knowledge-of-finance)
* [Analogy: Predict the price of a ticket for a concert](#heading-analogy-predict-the-price-of-a-ticket-for-a-concert)
* [Plain English explanation with code example](#heading-black-scholes-in-plain-english-with-a-code-example)
* [Implications in the real world](#heading-implications-in-the-real-world)

Note: In the code example, we will be working with European call and put options.

<h2 id='pre'>Prerequisite Knowledge of Finance</h2>

To get the most out of this article and understand the Black-Scholes Equation, you just need to know what **financial derivatives** and **options** are in finance.

Essentially, financial derivatives are tools investors use to manage risks and improve returns.

There are many types of financial derivatives. One of these is called options. 

Options are like financial choices. With options, you can get the right to buy or sell something at a certain time and price, but only if you want to.

The main idea is that they help manage risk so you can make future better investments.

<h2 id='analogy'> Analogy: Predict the Price of a Ticket for a Concert </h2>

Imagine you are planning to buy a ticket for a concert.

The ticket prices change depending on the popularity of the artist, demand, and time until the concert.

Depending on that, you will make the best possible decision to buy the ticket at the lowest price.

Just as you think about the **risk** of buying the thicket at a certain time, investors use the Black-Scholes Equation to estimate the fair value of financial derivatives.

This way, they make sure they make wise investment choices in ever changing markets.

<h2 id='plain'> Black-Scholes in Plain English – with a Code Example </h2>

Essentially, the Black-Scholes Equation solved the problem of [how to price options correctly in financial markets.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=500303)

This is very important, because it helps banks and financial institutions effectively manage risk.

However, it was not always like this. Before 1973, when the equation was created ([its creators won a Nobel prize](https://www.nobelprize.org/prizes/economic-sciences/1997/press-release/)), determining the price of options was much more complicated and difficult.

Before the creation of the Black–Scholes equation, there wasn't a standardized mathematical method to predict the prices of options.

Traders often relied on personal experience and market conditions, which led to unreliable option prices.

And earlier mathematical methods did not fully consider factors like volatility, time decay, and interest rates. So there was a lot of error when pricing options.

### Here is the Black-Scholes Equation:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV - r S \frac{\partial V}{\partial S}$$

While we won't look very deeply at the equation itself, we will outline its key components and implications.

Essentially, the Black-Scholes equation predicts how an option's value changes over time based on several variables:

* V - Price of option as a function of stock price _S_ and time _t_
* S – Price of the underlying asset
* t – Time
* σ – Volatility
* r – Interest rate.

The left side of the equation explains how the option's value changes over time and how market ups and downs affect it. 

The right side of the equation shows how the option's value increases due to interest rates and how changes in the asset's price impact it. 

By making these two sides equal, we figure out the fair price of the option. 

### Python Code Example

In this code example, we will find, based on many parameters, the theoretical market value of an option.

For our example, let's assume the following:

* Current stock price (S) = $100. This is the price of the stock right now.
* Strike price (K) = $105. This is the specific price at which the option holder can buy (call) or sell (put) the underlying asset.
* Time to expiration (T) = 1 year (or 1.0 when expressed in years). This is the time left until the option expires.
* Risk-free interest rate (r) = 0.05% (or 0.0005 when expressed as a decimal). This is the interest rate on a risk-free investment.
* Volatility (sigma) = 20% (or 0.2 when expressed as a decimal). This is how much the stock price is expected to fluctuate.

```
from blackscholes import BlackScholesCall, BlackScholesPut

def calculate_option_prices(S, K, T, r, sigma, q):
    """
    Calculate the Black-Scholes option prices for European call and put options using the 'blackscholes' package.

    Parameters:
    S : float - current stock price
    K : float - strike price of the option
    T : float - time to maturity (in years)
    r : float - risk-free interest rate (annual as a decimal)
    sigma : float - volatility of the underlying stock (annual as a decimal)
    q : float - annual dividend yield (as a decimal)

    Returns:
    tuple - (call price, put price)
    """
    # Creating instances of BlackScholesCall and BlackScholesPut
    call_option = BlackScholesCall(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    put_option = BlackScholesPut(S=S, K=K, T=T, r=r, sigma=sigma, q=q)

    # Get call and put prices
    call_price = call_option.price()
    put_price = put_option.price()

    return call_price, put_price


call_price, put_price = calculate_option_prices(100, 105, 1, 0.0005, 0.20, 0.0)
print("Call Price: {:.6f}, Put Price: {:.6f}".format(call_price, put_price))

```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/1.png)

Now let's examine the code more closely and see what's really going on here:

#### Step 1: Import the Library

This is the Python library we are using in this article:

%[https://pypi.org/project/blackscholes/]

```
from blackscholes import BlackScholesCall, BlackScholesPut

```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/2.png)
_Importing functions_

#### Step 2: Create the Function to Calculate Options Prices

In the below code, we are importing the function we need to calculate the options call and put prices.

```
def calculate_option_prices(S, K, T, r, sigma, q):

    call_option = BlackScholesCall(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    put_option = BlackScholesPut(S=S, K=K, T=T, r=r, sigma=sigma, q=q)

    call_price = call_option.price()
    put_price = put_option.price()

    return call_price, put_price
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/3.png)
_Function to calculate call and put prices_

The main parameters of the function are:

* S : float – current stock price
* K : float – strike price of the option
* T : float – time to maturity (in years)
* r : float – risk-free interest rate (annual as a decimal)
* sigma : float – volatility of the underlying stock (annual as a decimal)
* q : float – annual dividend yield (as a decimal)

And it returns:

* tuple – (call price, put price)

First, we calculate the call and put options. Then we extract the price from it. We can also get other characteristics like the charm or the delta of these financial contracts according to the library documentation.

#### Step 3: Calculate the Options Pricing

The call and put prices of an option are the costs to buy the respective option contracts. 

```
call_price, put_price = calculate_option_prices(100, 105, 1, 0.0005, 0.20, 0.0)
print("Call Price: {:.6f}, Put Price: {:.6f}".format(call_price, put_price))
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/4.png)
_Applying the function_

We use as examples:

* Current stock price: $100
* Strike price: $105
* Time to maturity: 1 year
* Risk-free interest rate: 0.05% (as a decimal: 0.0005)
* Volatility: 20% (as a decimal: 0.20)
* Dividend yield: 0%

Based on this factors, we price:

* Call Option Price: 5.924799
* Put Option Price: 10.872312

Which means that, given these parameters:

* The price at which you have the right, but not the obligation, to buy is 5.924799 dollars
* The price at which you have the right, but not the obligation, to sell is 10.872312 dollars

<h2 id='implications'> Implications in the Real World </h2>

The equation has had a massive impact in the world of finance.

Below are some of the industries the Black-Scholes Equation has changed greatly:

### Securitized Debt

In simple terms, securitized debt refers to turning loans into something that can be bought and sold.

The Black-Scholes equation changed the way banks price grouped-up debt, like mortgages.

Before the Black-Scholes equation, it was very hard to know the worth of these debts. But with the equation, banks can understand their value much better. This made it easier to buy and sell these debts while knowing the potential benefits and risks.

This way, the market for these mortgage debts grew. Which in turn helped grow the housing market.

### Exchange Traded Options

Trading options was a very uncertain business. There was no way of truly knowing how to correctly price them.

However, with the Black-Scholes equation, option pricing became far easier. It allowed people to calculate an option based on an underlying asset's price, volatility, time to expiration, and interest rates.

The newfound precision helped grow the options market.

### Credit Default Swaps

Credit default swaps are like insurance policies for loans. With a credit default swap, you are protected if the borrower fails to pay back.

Credit default swaps are very important in managing credit risk. But it was only after the black Scholes equation was created that they were accurately priced.

This way, credit default swaps became a very important tool for financial institutions for financial risk management.

### Over the Counter Derivatives Securities

Over-the-counter (OTC) derivatives are private deals made between two parties without a stock exchange.

Before Black-Scholes, negotiating the terms and prices of OTC derivatives was very hard. But then the Black-Scholes equation offered a standard way of finding the price of derivatives.

This allowed market participants to negotiate contracts more efficiently and accurately.

## Conclusion

The Black-Scholes equation helped create more precision in the way certain things are priced.

This precision helped create more stable institutions, which in turn helped create a more resilient economy.

If interested in learning more, see this video:

%[https://www.youtube.com/watch?v=A5w-dEgIU1M]

If you are interested in learning more about finance:

%[https://www.freecodecamp.org/news/fundamentals-of-finance-economics-for-businesses/]

## Full code

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]




