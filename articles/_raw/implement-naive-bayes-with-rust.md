---
title: How to Implement a Naive Bayes Classifier with Rust
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-05T17:53:04.000Z'
originalURL: https://freecodecamp.org/news/implement-naive-bayes-with-rust
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/pexels-philip-ackermann-878167--1-.jpg
tags:
- name: algorithms
  slug: algorithms
- name: MathJax
  slug: mathjax
- name: Rust
  slug: rust
seo_title: null
seo_desc: "By Joshua Taylor\nI want to improve my Rust skills, and help you hone yours\
  \ as well. So I've decided to write a series of articles about the Rust programing\
  \ language. \nBy actually building stuff with Rust, we'll learn about a wide range\
  \ of technologic..."
---

By Joshua Taylor

I want to improve my Rust skills, and help you hone yours as well. So I've decided to write a series of articles about the Rust programing language. 

By actually building stuff with Rust, we'll learn about a wide range of technological concepts in the process. In this installment, we’ll learn how to implement the Naive Bayes classifier with Rust.

You may encounter a few unfamiliar terms or concepts in this article. Don’t be discouraged. Look these up if you have the time, but regardless, this article’s main ideas will not be lost on you.

## What is a Naive Bayes Classifier?

The Naive Bayes classifier is a machine learning algorithm based on Bayes’ Theorem. [Bayes’ Theorem](https://greenteapress.com/wp/think-bayes/) gives us a way to update the probability of a hypothesis \(H\), given some data \(D\). 

Expressed mathematically, we have:

$$P(H|D) = \frac{P(D|H)P(H)}{P(D)}$$

where \(P(H|D) =\) the probability of \(H\) given \(D\).

If we accumulate more data, we can update \(P(H|D)\) accordingly.

Naive Bayesian models rest on a big assumption: whether a data point is present or absent from the data set is independent from data already in that set ([source](https://www.oreilly.com/library/view/data-science-from/9781492041122/)). That is, each piece of data conveys no information about any other data points. 

We do not expect this assumption to be true – it is weak. But it’s still useful, allowing us to create efficient classifiers that work quite well ([source](https://probml.github.io/pml-book/book0.html)).

We’ll leave our description of Naive Bayes there. A lot more could be said, but the main point of this article is to practice Rust. 

If you’d like to learn more about the algorithm, here are some resources:

* I can’t say enough good things [about this video from Josh Starmer](https://www.youtube.com/watch?v=O2L2Uv9pdDA&t=657s).
* Joel Grus has [written a chapter on Naive Bayes](https://learning.oreilly.com/library/view/data-science-from/9781492041122/) in his great book _Data Science from Scratch,_ which was the main inspiration for this implementation.
* If mathematical notation is your thing, [try section 6.6.3 of _The Elements of Statisical Learning_](https://hastie.su.domains/Papers/ESLII.pdf).
* And [here's a helpful article](https://www.freecodecamp.org/news/how-naive-bayes-classifiers-work/) on the basics of how the algorithm works.

The canonical application of the Naive Bayes classifier is a spam classifier. That is what we’ll build. You can find all the code here: [https://github.com/josht-jpg/shaking-off-the-rust](https://github.com/josht-jpg/shaking-off-the-rust)

We’ll begin by creating a new library with Cargo.

```rust
cargo new naive_bayes --lib
cd naive_bayes

```

Now let's dive into it.

## Tokenization in Rust

Our classifier will take in a message as input and return a classification of spam or not spam. 

To work with the message we’re given, we’ll want to _tokenize_ it. Our tokenized representation will be a set of words in lower case where order and repeat entries are disregarded. Rust’s **`[std::collections::HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html)`** structure is a great way to achieve this.

The function we’ll write to preform tokenization will require the use of the [regex](https://docs.rs/regex/latest/regex/) crate. Make sure you include this dependency in your `Cargo.toml` file:

```rust
[dependencies]
regex = "^1.5.4"

```

And here’s the `tokenize` function:

```rust
// lib.rs

// We'll need HashMap later
use std::collections::{HashMap, HashSet};

extern crate regex;
use regex::Regex;

pub fn tokenize(lower_case_text: &str) -> HashSet<&str> {
    Regex::new(r"[a-z0-9']+")
        .unwrap()
        .find_iter(lower_case_text)
        .map(|mat| mat.as_str())
        .collect()
}
```

This function uses a regular expression to match all numbers and lowercase letters. Whenever we come across a different type of symbol (often whitespace or punctuation), we split the input and group together all numbers and letters encountered since the last split (you can [read more about regex in Rust here](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html)). That is, we're identifying and isolating words in the input text.

### Some Handy Structures

Using a `struct` to represent a message will be helpful. This `struct` will contain a _string slice_ for the message’s text, and a Boolean value to indicate whether or not the message is spam:

```rust
pub struct Message<'a> {
    pub text: &'a str,
    pub is_spam: bool,
}
```

The `'a` is a lifetime parameter annotation. If you’re unfamiliar with lifetimes, and want to learn about them, I recommend reading [section 10.3 of The Rust Programming Language Book](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html).

A `struct` will also be useful to represent our classifier. Before creating the `struct`, we need a short digression on Laplacian Smoothing.

### What is Laplace Smoothing?

Assume that – in our training data – the word _fubar_ appears in some non-spam messages, but does not appear in any spam messages. Then, the Naive Bayes classifier will assign a probability **0** of spam to any message that contains the word _fubar_ ([source](https://www.youtube.com/watch?v=nt63k3bfXS0)).

Unless we’re talking about my success with online dating, it’s not smart to assign a probability of **0** to an event just because it hasn’t happened yet.

Enter Laplace Smoothing. This is the technique of adding \(\alpha\) to the number of observations of each token ([source](https://www.youtube.com/watch?v=nt63k3bfXS0)). Let’s see this mathematically: without Laplace Smoothing, the probability of seeing a word \(w\) in a spam message is:

$$P(w|S) = \frac{number\ of\ spam\ messages\ containing\ w}{total\ number\ of\ spams}$$

With Laplace Smoothing, it’s:

$$P(w|S) = \frac{(a+number\ of\ spam\ messages\ containing\ w)}{(2a+total\ number\ of\ spams)}$$

Back to our classifier `struct`:

```rust
pub struct NaiveBayesClassifier {
    pub alpha: f64,
    pub tokens: HashSet<String>,
    pub token_ham_counts: HashMap<String, i32>,
    pub token_spam_counts: HashMap<String, i32>,
    pub spam_messages_count: i32,
    pub ham_messages_count: i32,
}

```

The implementation block for `NaiveBayesClassifier` will center around a `train` method and a `predict` method.

## How to Train Our Classifier

The `train` method will take in a slice of `Message`s and loop through each `Message`, doing the following:

* Check whether the message is spam and update `spam_messages_count` or `ham_messages_count` accordingly. We’ll create the helper function `increment_message_classifications_count` for this.
* Tokenize the message’s contents with our `tokenize` function.
* Loop through each token in the message and:
* Insert the token into the `tokens` `HashSet`, then update `token_spam_counts` or `token_ham_counts`. We’ll create the helper function `increment_token_count` for this.

Here’s the pseudocode for our `train` method. If you feel like it, try to convert the pseudocode into Rust before looking at my implementation below. Don't hesitate to send me your implementation, I’d love to see it!

```
implementation block for NaiveBayesClassifier {

	train(self, messages) {
		for each message in messages {
			self.increment_message_classifications_count(message)
			
			lowercase_text = to_lowercase(message.text)
			for each token in tokenize(lowercase_text) {
				self.tokens.insert(tokens)
				self.increment_token_count(token, message.is_spam)
			}			
		}
	}

	increment_message_classifications_count(self, message) {
		if message.is_spam {
			self.spam_messages_count = self.spam_messages_count + 1
		} else {
			self.ham_messages_count = self.ham_messages_count + 1
		}
	}

	increment_token_count(&mut self, token, is_spam) {
		if token is not a key of self.token_spam_counts {
			insert record with key=token and value=0 into self.token_spam_counts
		}

		if token is not a key of self.token_ham_counts {
			insert record with key=token and value=0 into self.token_ham_counts
		}

		if is_spam {
			self.token_spam_counts[token] = self.token_spam_counts[token] + 1
		} else {
			self.token_ham_counts[token] = self.token_ham_counts[token] + 1
		}
	}

}

```

And here’s the Rust implementation:

```rust
impl NaiveBayesClassifier {
    pub fn train(&mut self, messages: &[Message]) {
        for message in messages.iter() {
            self.increment_message_classifications_count(message);
            for token in tokenize(&message.text.to_lowercase()) {
                self.tokens.insert(token.to_string());
                self.increment_token_count(token, message.is_spam)
            }
        }
    }

    fn increment_message_classifications_count(&mut self, message: &Message) {
        if message.is_spam {
            self.spam_messages_count += 1;
        } else {
            self.ham_messages_count += 1;
        }
    }

    fn increment_token_count(&mut self, token: &str, is_spam: bool) {
        if !self.token_spam_counts.contains_key(token) {
            self.token_spam_counts.insert(token.to_string(), 0);
        }

        if !self.token_ham_counts.contains_key(token) {
            self.token_ham_counts.insert(token.to_string(), 0);
        }

        if is_spam {
            self.increment_spam_count(token);
        } else {
            self.increment_ham_count(token);
        }
    }

    fn increment_spam_count(&mut self, token: &str) {
        *self.token_spam_counts.get_mut(token).unwrap() += 1;
    }

    fn increment_ham_count(&mut self, token: &str) {
        *self.token_ham_counts.get_mut(token).unwrap() += 1;
    }
}

```

Notice that incrementing a value in a `HashMap` is pretty cumbersome. A novice Rust programmer would have difficulty understanding what

`*self.token_spam_counts.get_mut(token).unwrap() += 1` 

is doing. 

In an attempt to make the code more explicit, I’ve created the `increment_spam_count` and `increment_ham_count` functions. But I’m not happy with that – it still feels cumbersome. Reach out to me if you have suggestions for a better approach.

## How to Predict with Our Classifier

The `predict` method will take a _string slice_ and return the model’s calculated probability of spam.

We’ll create two helper functions `probabilities_of_message` and `probabilites_of_token` to do the heavy lifting for `predict`.

`probabilities_of_message` returns \(P(Message|Spam)\) and \(P(Message|ham)\).

`probabilities_of_token` returns \(P(Token|Spam)\) and \(P(Token|ham)\).

Calculating the probability that the input message is spam involves multiplying together each word’s probability of occurring in a spam message.

Since probabilities are floating point numbers between 0 and 1, multiplying many probabilities together can result in **underflow** ([source](https://learning.oreilly.com/library/view/data-science-from/9781492041122/)). This is when an operation results in a number smaller than what the computer can accurately store ([see here](https://www.techopedia.com/definition/712/underflow) and [here](https://www.amazon.ca/Numerical-Analysis-Richard-Burden/dp/1305253663/ref=asc_df_1305253663/?tag=googleshopc0c-20&linkCode=df0&hvadid=293014842916&hvpos=&hvnetw=g&hvrand=9862733826869340686&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9001551&hvtargid=pla-450666638521&psc=1)). Thus, we’ll use logarithms and exponentials to transform the task into a series of additions: 

$$\prod_{i=0}^{n}p_i = exp(\sum_{i=0}^{n} log(p_i))$$

Which we can do because for any real numbers \(a\) and \(b\),

$$ab = exp(log(ab)) = exp(log(a) + log(b))$$

Once again I’ll start with pseudocode for the predict method:

```
implementation block for NaiveBayesCalssifier {
	/*...*/

	predict(self, text) {
		lower_case_text = to_lowercase(text)
		message_tokens = tokenize(text)
		(prob_if_spam, prob_if_ham) = self.probabilities_of_message(message_tokens)
		return prob_if_spam / (prob_if_spam + prob_if_ham)
	}
	
	probabilities_of_message(self, message_tokens) {
		log_prob_if_spam = 0
		log_prob_if_ham = 0

		for each token in self.tokens {
			(prob_if_spam, prob_if_ham) = self.probabilites_of_token(token)

			if message_tokens contains token {
				log_prob_if_spam = log_prob_if_spam + ln(prob_if_spam)
				log_prob_if_ham = log_prob_if_ham + ln(prob_if_ham)
			} else {
				log_prob_if_spam = log_prob_if_spam + ln(1 - prob_if_spam)
				log_prob_if_ham = log_prob_if_ham + ln(1 - prob_if_ham)
			}
		}

		prob_if_spam = exp(log_prob_if_spam)
		prob_if_ham = exp(log_prob_if_ham)

		return (prob_if_spam, prob_if_ham)
	}

	probabilites_of_token(self, token) {
		prob_of_token_spam = (self.token_spam_counts[token] + self.alpha) 
						/ (self.spam_messages_count + 2 * self.alpha)
        
		prob_of_token_ham = (self.token_ham_counts[token] + self.alpha) 
						/ (self.ham_messages_count + 2 * self.alpha)

		return (prob_of_token_spam, prob_of_token_ham)
	}
	
	
}

```

And here’s the Rust code:

```rust
impl NaiveBayesClassifier {

		/*...*/

	pub fn predict(&self, text: &str) -> f64 {
        let lower_case_text = text.to_lowercase();
        let message_tokens = tokenize(&lower_case_text);
        let (prob_if_spam, prob_if_ham) = self.probabilities_of_message(message_tokens);

        return prob_if_spam / (prob_if_spam + prob_if_ham);
    }

    fn probabilities_of_message(&self, message_tokens: HashSet<&str>) -> (f64, f64) {
        let mut log_prob_if_spam = 0.;
        let mut log_prob_if_ham = 0.;

        for token in self.tokens.iter() {
            let (prob_if_spam, prob_if_ham) = self.probabilites_of_token(&token);

            if message_tokens.contains(token.as_str()) {
                log_prob_if_spam += prob_if_spam.ln();
                log_prob_if_ham += prob_if_ham.ln();
            } else {
                log_prob_if_spam += (1. - prob_if_spam).ln();
                log_prob_if_ham += (1. - prob_if_ham).ln();
            }
        }

        let prob_if_spam = log_prob_if_spam.exp();
        let prob_if_ham = log_prob_if_ham.exp();

        return (prob_if_spam, prob_if_ham);
    }

    fn probabilites_of_token(&self, token: &str) -> (f64, f64) {
        let prob_of_token_spam = (self.token_spam_counts[token] as f64 + self.alpha)
            / (self.spam_messages_count as f64 + 2. * self.alpha);

        let prob_of_token_ham = (self.token_ham_counts[token] as f64 + self.alpha)
            / (self.ham_messages_count as f64 + 2. * self.alpha);

        return (prob_of_token_spam, prob_of_token_ham);
    }
}

```

## How to Test Our Classifier

Let’s give our model a test. The test below goes through Naive Bayes manually, then checks that our model gives the same result. 

You may find it worth while to go through the test’s logic, or you may just want to paste the code to the bottom of your lib.rs file to check that your code works.

```rust
// ...lib.rs

pub fn new_classifier(alpha: f64) -> NaiveBayesClassifier {
    return NaiveBayesClassifier {
        alpha,
        tokens: HashSet::new(),
        token_ham_counts: HashMap::new(),
        token_spam_counts: HashMap::new(),
        spam_messages_count: 0,
        ham_messages_count: 0,
    };
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn naive_bayes() {
        let train_messages = [
            Message {
                text: "Free Bitcoin viagra XXX christmas deals 😻😻😻",
                is_spam: true,
            },
            Message {
                text: "My dear Granddaughter, please explain Bitcoin over Christmas dinner",
                is_spam: false,
            },
            Message {
                text: "Here in my garage...",
                is_spam: true,
            },
        ];

        let alpha = 1.;
        let num_spam_messages = 2.;
        let num_ham_messages = 1.;

        let mut model = new_classifier(alpha);
        model.train(&train_messages);

        let mut expected_tokens: HashSet<String> = HashSet::new();
        for message in train_messages.iter() {
            for token in tokenize(&message.text.to_lowercase()) {
                expected_tokens.insert(token.to_string());
            }
        }

        let input_text = "Bitcoin crypto academy Christmas deals";

        let probs_if_spam = [
            1. - (1. + alpha) / (num_spam_messages + 2. * alpha), // "Free"  (not present)
            (1. + alpha) / (num_spam_messages + 2. * alpha),      // "Bitcoin"  (present)
            1. - (1. + alpha) / (num_spam_messages + 2. * alpha), // "viagra"  (not present)
            1. - (1. + alpha) / (num_spam_messages + 2. * alpha), // "XXX"  (not present)
            (1. + alpha) / (num_spam_messages + 2. * alpha),      // "christmas"  (present)
            (1. + alpha) / (num_spam_messages + 2. * alpha),      // "deals"  (present)
            1. - (1. + alpha) / (num_spam_messages + 2. * alpha), // "my"  (not present)
            1. - (0. + alpha) / (num_spam_messages + 2. * alpha), // "dear"  (not present)
            1. - (0. + alpha) / (num_spam_messages + 2. * alpha), // "granddaughter"  (not present)
            1. - (0. + alpha) / (num_spam_messages + 2. * alpha), // "please"  (not present)
            1. - (0. + alpha) / (num_spam_messages + 2. * alpha), // "explain"  (not present)
            1. - (0. + alpha) / (num_spam_messages + 2. * alpha), // "over"  (not present)
            1. - (0. + alpha) / (num_spam_messages + 2. * alpha), // "dinner"  (not present)
            1. - (1. + alpha) / (num_spam_messages + 2. * alpha), // "here"  (not present)
            1. - (1. + alpha) / (num_spam_messages + 2. * alpha), // "in"  (not present)
            1. - (1. + alpha) / (num_spam_messages + 2. * alpha), // "garage"  (not present)
        ];

        let probs_if_ham = [
            1. - (0. + alpha) / (num_ham_messages + 2. * alpha), // "Free"  (not present)
            (1. + alpha) / (num_ham_messages + 2. * alpha),      // "Bitcoin"  (present)
            1. - (0. + alpha) / (num_ham_messages + 2. * alpha), // "viagra"  (not present)
            1. - (0. + alpha) / (num_ham_messages + 2. * alpha), // "XXX"  (not present)
            (1. + alpha) / (num_ham_messages + 2. * alpha),      // "christmas"  (present)
            (0. + alpha) / (num_ham_messages + 2. * alpha),      // "deals"  (present)
            1. - (1. + alpha) / (num_ham_messages + 2. * alpha), // "my"  (not present)
            1. - (1. + alpha) / (num_ham_messages + 2. * alpha), // "dear"  (not present)
            1. - (1. + alpha) / (num_ham_messages + 2. * alpha), // "granddaughter"  (not present)
            1. - (1. + alpha) / (num_ham_messages + 2. * alpha), // "please"  (not present)
            1. - (1. + alpha) / (num_ham_messages + 2. * alpha), // "explain"  (not present)
            1. - (1. + alpha) / (num_ham_messages + 2. * alpha), // "over"  (not present)
            1. - (1. + alpha) / (num_ham_messages + 2. * alpha), // "dinner"  (not present)
            1. - (0. + alpha) / (num_ham_messages + 2. * alpha), // "here"  (not present)
            1. - (0. + alpha) / (num_ham_messages + 2. * alpha), // "in"  (not present)
            1. - (0. + alpha) / (num_ham_messages + 2. * alpha), // "garage"  (not present)
        ];

        let p_if_spam_log: f64 = probs_if_spam.iter().map(|p| p.ln()).sum();
        let p_if_spam = p_if_spam_log.exp();

        let p_if_ham_log: f64 = probs_if_ham.iter().map(|p| p.ln()).sum();
        let p_if_ham = p_if_ham_log.exp();

        // P(message | spam) / (P(messge | spam) + P(message | ham)) rounds to 0.97
        assert!((model.predict(input_text) - p_if_spam / (p_if_spam + p_if_ham)).abs() < 0.000001);
    }
}
```

Now run `cargo test`. If that passes for you, well done, you’ve implemented a Naive Bayes classifier in Rust!

Thank you for coding with me, friends. Feel free to reach out if you have any questions or suggestions.

### References

1. [Grus, J. (2019). _Data Science from Scratch: First Principles with Python, 2nd edition._ O’Reilly Media.](https://learning.oreilly.com/library/view/data-science-from/9781492041122/)
2. [Downey, A. (2021). _Think Bayes: Bayesian Statistics in Python, 2nd edition._  O’Reilly Media.](https://greenteapress.com/wp/think-bayes/)
3. [Murphy, K. (2012). _Machine Learning: A Probabilistic Perspective._ MIT Press.](https://probml.github.io/pml-book/book0.html)
4. [Dhinakaran, V. (2017). _Rust Cookbook._ Packt.](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html) 
5. [Ng, A. (2018). _Stanford CS229: Lecture 5 - GDA & Naive Bayes._](https://www.youtube.com/watch?v=nt63k3bfXS0) 
6. [Burden, R. Faires, J. Burden, A. (2015). _Numerical Analysis, 10th edition._ Brooks Cole.](https://www.amazon.ca/Numerical-Analysis-Richard-Burden/dp/1305253663/ref=asc_df_1305253663/?tag=googleshopc0c-20&linkCode=df0&hvadid=293014842916&hvpos=&hvnetw=g&hvrand=9862733826869340686&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9001551&hvtargid=pla-450666638521&psc=1)
7. [_Underflow._ Technopedia.](https://www.techopedia.com/definition/712/underflow)

