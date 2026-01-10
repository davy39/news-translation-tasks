---
title: Comment implémenter un classificateur Naive Bayes avec Rust
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
seo_title: Comment implémenter un classificateur Naive Bayes avec Rust
seo_desc: "By Joshua Taylor\nI want to improve my Rust skills, and help you hone yours\
  \ as well. So I've decided to write a series of articles about the Rust programing\
  \ language. \nBy actually building stuff with Rust, we'll learn about a wide range\
  \ of technologic..."
---

Par Joshua Taylor

Je souhaite améliorer mes compétences en Rust et vous aider à affiner les vôtres. J'ai donc décidé d'écrire une série d'articles sur le langage de programmation Rust.

En construisant réellement des choses avec Rust, nous apprendrons une large gamme de concepts technologiques dans le processus. Dans cet article, nous apprendrons comment implémenter le classificateur Naive Bayes avec Rust.

Vous pourriez rencontrer quelques termes ou concepts peu familiers dans cet article. Ne vous découragez pas. Recherchez-les si vous avez le temps, mais quoi qu'il en soit, les idées principales de cet article ne vous échapperont pas.

## Qu'est-ce qu'un classificateur Naive Bayes ?

Le classificateur Naive Bayes est un algorithme d'apprentissage automatique basé sur le théorème de Bayes. [Le théorème de Bayes](https://greenteapress.com/wp/think-bayes/) nous donne un moyen de mettre à jour la probabilité d'une hypothèse \(H\), étant donné certaines données \(D\).

Exprimé mathématiquement, nous avons :

$$P(H|D) = \frac{P(D|H)P(H)}{P(D)}$$

où \(P(H|D) =\) la probabilité de \(H\) étant donné \(D\).

Si nous accumulons plus de données, nous pouvons mettre à jour \(P(H|D)\) en conséquence.

Les modèles bayésiens naïfs reposent sur une grande hypothèse : qu'un point de données soit présent ou absent de l'ensemble de données est indépendant des données déjà présentes dans cet ensemble ([source](https://www.oreilly.com/library/view/data-science-from/9781492041122/)). C'est-à-dire que chaque élément de données ne fournit aucune information sur les autres points de données.

Nous ne nous attendons pas à ce que cette hypothèse soit vraie – elle est faible. Mais elle est toujours utile, nous permettant de créer des classificateurs efficaces qui fonctionnent plutôt bien ([source](https://probml.github.io/pml-book/book0.html)).

Nous en resterons là pour notre description de Naive Bayes. Beaucoup plus pourrait être dit, mais le point principal de cet article est de pratiquer Rust.

Si vous souhaitez en savoir plus sur l'algorithme, voici quelques ressources :

* Je ne peux pas dire assez de bonnes choses [à propos de cette vidéo de Josh Starmer](https://www.youtube.com/watch?v=O2L2Uv9pdDA&t=657s).
* Joel Grus a [écrit un chapitre sur Naive Bayes](https://learning.oreilly.com/library/view/data-science-from/9781492041122/) dans son excellent livre _Data Science from Scratch_, qui a été la principale inspiration pour cette implémentation.
* Si la notation mathématique est votre truc, [essayez la section 6.6.3 de _The Elements of Statistical Learning_](https://hastie.su.domains/Papers/ESLII.pdf).
* Et [voici un article utile](https://www.freecodecamp.org/news/how-naive-bayes-classifiers-work/) sur les bases du fonctionnement de l'algorithme.

L'application canonique du classificateur Naive Bayes est un classificateur de spam. C'est ce que nous allons construire. Vous pouvez trouver tout le code ici : [https://github.com/josht-jpg/shaking-off-the-rust](https://github.com/josht-jpg/shaking-off-the-rust)

Nous commencerons par créer une nouvelle bibliothèque avec Cargo.

```rust
cargo new naive_bayes --lib
cd naive_bayes

```

Maintenant, plongeons dedans.

## Tokenization en Rust

Notre classificateur prendra un message en entrée et retournera une classification de spam ou non spam.

Pour travailler avec le message que nous recevons, nous voudrons le _tokenizer_. Notre représentation tokenisée sera un ensemble de mots en minuscules où l'ordre et les entrées répétées sont ignorés. La structure **`[std::collections::HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html)`** de Rust est un excellent moyen d'y parvenir.

La fonction que nous allons écrire pour effectuer la tokenization nécessitera l'utilisation de la crate [regex](https://docs.rs/regex/latest/regex/). Assurez-vous d'inclure cette dépendance dans votre fichier `Cargo.toml` :

```rust
[dependencies]
regex = "^1.5.4"

```

Et voici la fonction `tokenize` :

```rust
// lib.rs

// Nous aurons besoin de HashMap plus tard
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

Cette fonction utilise une expression régulière pour correspondre à tous les nombres et lettres minuscules. Chaque fois que nous rencontrons un type de symbole différent (souvent un espace blanc ou une ponctuation), nous divisons l'entrée et regroupons tous les nombres et lettres rencontrés depuis la dernière division (vous pouvez [en savoir plus sur regex en Rust ici](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html)). C'est-à-dire que nous identifions et isolons les mots dans le texte d'entrée.

### Quelques structures pratiques

Utiliser une `struct` pour représenter un message sera utile. Cette `struct` contiendra une _tranche de chaîne_ pour le texte du message, et une valeur booléenne pour indiquer si le message est un spam ou non :

```rust
pub struct Message<'a> {
    pub text: &'a str,
    pub is_spam: bool,
}
```

Le `'a` est une annotation de paramètre de durée de vie. Si vous n'êtes pas familier avec les durées de vie et que vous souhaitez en savoir plus, je vous recommande de lire [la section 10.3 du livre The Rust Programming Language](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html).

Une `struct` sera également utile pour représenter notre classificateur. Avant de créer la `struct`, nous avons besoin d'une courte digression sur le lissage de Laplace.

### Qu'est-ce que le lissage de Laplace ?

Supposons que – dans nos données d'entraînement – le mot _fubar_ apparaît dans certains messages non spam, mais n'apparaît dans aucun message spam. Alors, le classificateur Naive Bayes attribuera une probabilité **0** de spam à tout message contenant le mot _fubar_ ([source](https://www.youtube.com/watch?v=nt63k3bfXS0)).

Sauf si nous parlons de mon succès avec les rencontres en ligne, ce n'est pas intelligent d'attribuer une probabilité de **0** à un événement simplement parce qu'il ne s'est pas encore produit.

Entrez le lissage de Laplace. Il s'agit de la technique consistant à ajouter \(\alpha\) au nombre d'observations de chaque token ([source](https://www.youtube.com/watch?v=nt63k3bfXS0)). Voyons cela mathématiquement : sans le lissage de Laplace, la probabilité de voir un mot \(w\) dans un message spam est :

$$P(w|S) = \frac{nombre\ de\ messages\ spam\ contenant\ w}{nombre\ total\ de\ spams}$$

Avec le lissage de Laplace, c'est :

$$P(w|S) = \frac{(a+nombre\ de\ messages\ spam\ contenant\ w)}{(2a+nombre\ total\ de\ spams)}$$

Retour à notre `struct` de classificateur :

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

Le bloc d'implémentation pour `NaiveBayesClassifier` sera centré autour d'une méthode `train` et d'une méthode `predict`.

## Comment entraîner notre classificateur

La méthode `train` prendra une tranche de `Message`s et parcourra chaque `Message`, en faisant ce qui suit :

* Vérifier si le message est un spam et mettre à jour `spam_messages_count` ou `ham_messages_count` en conséquence. Nous créerons la fonction auxiliaire `increment_message_classifications_count` pour cela.
* Tokenizer le contenu du message avec notre fonction `tokenize`.
* Parcourir chaque token dans le message et :
* Insérer le token dans le `HashSet` `tokens`, puis mettre à jour `token_spam_counts` ou `token_ham_counts`. Nous créerons la fonction auxiliaire `increment_token_count` pour cela.

Voici le pseudocode pour notre méthode `train`. Si vous en avez envie, essayez de convertir le pseudocode en Rust avant de regarder mon implémentation ci-dessous. N'hésitez pas à m'envoyer votre implémentation, j'adorerais la voir !

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

Et voici l'implémentation en Rust :

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

Remarquez que l'incrémentation d'une valeur dans un `HashMap` est assez fastidieuse. Un programmeur Rust novice aurait du mal à comprendre ce que

`*self.token_spam_counts.get_mut(token).unwrap() += 1` 

fait.

Dans une tentative de rendre le code plus explicite, j'ai créé les fonctions `increment_spam_count` et `increment_ham_count`. Mais je ne suis pas satisfait de cela – cela semble toujours fastidieux. Contactez-moi si vous avez des suggestions pour une meilleure approche.

## Comment prédire avec notre classificateur

La méthode `predict` prendra une _tranche de chaîne_ et retournera la probabilité calculée par le modèle de spam.

Nous créerons deux fonctions auxiliaires `probabilities_of_message` et `probabilites_of_token` pour faire le gros du travail pour `predict`.

`probabilities_of_message` retourne \(P(Message|Spam)\) et \(P(Message|ham)\).

`probabilites_of_token` retourne \(P(Token|Spam)\) et \(P(Token|ham)\).

Le calcul de la probabilité que le message d'entrée soit un spam implique de multiplier ensemble la probabilité de chaque mot d'apparaître dans un message spam.

Puisque les probabilités sont des nombres à virgule flottante entre 0 et 1, multiplier de nombreuses probabilités ensemble peut entraîner un **underflow** ([source](https://learning.oreilly.com/library/view/data-science-from/9781492041122/)). Cela se produit lorsqu'une opération donne un nombre plus petit que ce que l'ordinateur peut stocker avec précision ([voir ici](https://www.techopedia.com/definition/712/underflow) et [ici](https://www.amazon.ca/Numerical-Analysis-Richard-Burden/dp/1305253663/ref=asc_df_1305253663/?tag=googleshopc0c-20&linkCode=df0&hvadid=293014842916&hvpos=&hvnetw=g&hvrand=9862733826869340686&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9001551&hvtargid=pla-450666638521&psc=1)). Ainsi, nous utiliserons des logarithmes et des exponentielles pour transformer la tâche en une série d'additions :

$$\prod_{i=0}^{n}p_i = exp(\sum_{i=0}^{n} log(p_i))$$

Ce que nous pouvons faire car pour n'importe quels nombres réels \(a\) et \(b\),

$$ab = exp(log(ab)) = exp(log(a) + log(b))$$

Une fois de plus, je commencerai par le pseudocode pour la méthode predict :

```
implementation block for NaiveBayesClassifier {
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

Et voici le code Rust :

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

## Comment tester notre classificateur

Donnons un test à notre modèle. Le test ci-dessous passe par Naive Bayes manuellement, puis vérifie que notre modèle donne le même résultat.

Vous pourriez trouver utile de passer par la logique du test, ou vous pourriez simplement vouloir coller le code en bas de votre fichier lib.rs pour vérifier que votre code fonctionne.

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

Maintenant, exécutez `cargo test`. Si cela passe pour vous, bien joué, vous avez implémenté un classificateur Naive Bayes en Rust !

Merci d'avoir codé avec moi, amis. N'hésitez pas à me contacter si vous avez des questions ou des suggestions.

### Références

1. [Grus, J. (2019). _Data Science from Scratch: First Principles with Python, 2nd edition._ OReilly Media.](https://learning.oreilly.com/library/view/data-science-from/9781492041122/)
2. [Downey, A. (2021). _Think Bayes: Bayesian Statistics in Python, 2nd edition._  OReilly Media.](https://greenteapress.com/wp/think-bayes/)
3. [Murphy, K. (2012). _Machine Learning: A Probabilistic Perspective._ MIT Press.](https://probml.github.io/pml-book/book0.html)
4. [Dhinakaran, V. (2017). _Rust Cookbook._ Packt.](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html) 
5. [Ng, A. (2018). _Stanford CS229: Lecture 5 - GDA & Naive Bayes._](https://www.youtube.com/watch?v=nt63k3bfXS0) 
6. [Burden, R. Faires, J. Burden, A. (2015). _Numerical Analysis, 10th edition._ Brooks Cole.](https://www.amazon.ca/Numerical-Analysis-Richard-Burden/dp/1305253663/ref=asc_df_1305253663/?tag=googleshopc0c-20&linkCode=df0&hvadid=293014842916&hvpos=&hvnetw=g&hvrand=9862733826869340686&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9001551&hvtargid=pla-450666638521&psc=1)
7. [_Underflow._ Technopedia.](https://www.techopedia.com/definition/712/underflow)