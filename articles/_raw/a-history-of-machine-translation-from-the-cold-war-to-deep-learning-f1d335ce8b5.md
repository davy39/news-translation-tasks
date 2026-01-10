---
title: A history of machine translation from the Cold War to deep learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T12:12:26.000Z'
originalURL: https://freecodecamp.org/news/a-history-of-machine-translation-from-the-cold-war-to-deep-learning-f1d335ce8b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d-iF6wcVYCWFDLkghpJvkw.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ilya Pestov

  I open Google Translate twice as often as Facebook, and the instant translation
  of the price tags is not a cyberpunk for me anymore. That’s what we call reality.
  It’s hard to imagine that this is the result of a centennial fight to bui...'
---

By Ilya Pestov

I open Google Translate twice as often as Facebook, and the instant translation of the price tags is not a cyberpunk for me anymore. That’s what we call reality. It’s hard to imagine that this is the result of a centennial fight to build the algorithms of machine translation and that there has been no visible success during half of that period.

The precise developments I’ll discuss in this article set the basis of all modern language processing systems — from search engines to voice-controlled microwaves. I’m talking about the evolution and structure of online translation today.

![Image](https://cdn-media-1.freecodecamp.org/images/rprYZbDrYxFKrq8uSJmNnr4rld9jmUf6ffSZ)
_The translating machine of P. P. Troyanskii (Illustration made from descriptions. No photos left, unfortunately.)_

### In the beginning

The story begins in 1933. Soviet scientist Peter Troyanskii presented “the machine for the selection and printing of words when translating from one language to another” to the Academy of Sciences of the USSR. The invention was super simple — it had cards in four different languages, a typewriter, and an old-school film camera.

The operator took the first word from the text, found a corresponding card, took a photo, and typed its morphological characteristics (noun, plural, genitive) on the typewriter. The typewriter’s keys encoded one of the features. The tape and the camera’s film were used simultaneously, making a set of frames with words and their morphology.

![Image](https://cdn-media-1.freecodecamp.org/images/d6EZXLmcj0m-0ILBEBafviYN9ITSLJmXum-F)

Despite all this, as often happened in the USSR, the invention was considered “useless”. Troyanskii died of Stenocardia after trying to finish his invention for 20 years. No one in the world knew about the machine until two Soviet scientists found his patents in 1956.

It was at the beginning of the Cold War. On January 7th 1954, at IBM headquarters in New York, the [Georgetown–IBM experiment](https://en.wikipedia.org/wiki/Georgetown%E2%80%93IBM_experiment) started. The IBM 701 computer automatically translated 60 Russian sentences into English for the first time in history.

> _“A girl who didn’t understand a word of the language of the Soviets punched out the Russian messages on IBM cards. The “brain” dashed off its English translations on an automatic printer at the breakneck speed of two and a half lines per second,”_ — reported the IBM press release.

![Image](https://cdn-media-1.freecodecamp.org/images/1MJctJSHzUaYpUNIhvQdQtz4RKFq06nN7FJ9)
_IBM 701_

However, the triumphant headlines hid one little detail. No one mentioned the translated examples were carefully selected and tested to exclude any ambiguity. For everyday use, that system was no better than a pocket phrasebook. Nevertheless, this sort of arms race launched: Canada, Germany, France, and especially Japan, all joined the race for machine translation.

### The race for machine translation

The vain struggles to improve machine translation lasted for forty years. In 1966, the US ALPAC committee, in its famous report, called machine translation expensive, inaccurate, and unpromising. They instead recommended focusing on dictionary development, which eliminated US researchers from the race for almost a decade.

Even so, a basis for modern Natural Language Processing was created only by the scientists and their attempts, research, and developments. All of today’s search engines, spam filters, and personal assistants appeared thanks to a bunch of countries spying on each other.

![Image](https://cdn-media-1.freecodecamp.org/images/l6Av1jJRcgtfL5n9vEvrspxpEJJalwHAusRx)

### Rule-based machine translation (RBMT)

The first ideas surrounding rule-based machine translation appeared in the 70s. The scientists peered over the interpreters’ work, trying to compel the tremendously sluggish computers to repeat those actions. These systems consisted of:

* Bilingual dictionary (RU -> EN)
* A set of linguistic rules for each language (For example, nouns ending in certain suffixes such as -heit, -keit, -ung are feminine)

That’s it. If needed, systems could be supplemented with hacks, such as lists of names, spelling correctors, and transliterators.

![Image](https://cdn-media-1.freecodecamp.org/images/fDCtcK15iABLixdZslASHztO0H3033UHjQm5)

PROMPT and Systran are the most famous examples of RBMT systems. Just take a look at the Aliexpress to feel the soft breath of this golden age.

But even they had some nuances and subspecies.

#### Direct Machine Translation

This is the most straightforward type of machine translation. It divides the text into words, translates them, slightly corrects the morphology, and harmonizes syntax to make the whole thing sound right, more or less. When the sun goes down, trained linguists write the rules for each word.

The output returns some kind of translation. Usually, it’s quite crappy. It seems that the linguists wasted their time for nothing.

Modern systems do not use this approach at all, and modern linguists are grateful.

![Image](https://cdn-media-1.freecodecamp.org/images/gfF1OTGY1E6QQBDW6l6kh1Daa4iingQmt86V)

#### Transfer-based Machine Translation

In contrast to direct translation, we prepare first by determining the grammatical structure of the sentence, as we were taught at school. Then we manipulate whole constructions, not words, afterwards. This helps to get quite decent conversion of the word order in translation. In theory.

In practice, it still resulted in verbatim translation and exhausted linguists. On the one hand, it brought simplified general grammar rules. But on the other, it became more complicated because of the increased number of word constructions in comparison with single words.

![Image](https://cdn-media-1.freecodecamp.org/images/AfcjFhnoMFmb8koHf42YQeE6WfKdFNjqpkGL)

#### Interlingual Machine Translation

In this method, the source text is transformed to the intermediate representation, and is unified for all the world’s languages (interlingua). It’s the same interlingua Descartes dreamed of: a meta-language, which follows the universal rules and transforms the translation into a simple “back and forth” task. Next, interlingua would convert to any target language, and here was the singularity!

Because of the conversion, Interlingua is often confused with transfer-based systems. The difference is the linguistic rules specific to every single language and interlingua, and not the language pairs. This means, we can add a third language to the interlingua system and translate between all three. We can’t do this in transfer-based systems.

![Image](https://cdn-media-1.freecodecamp.org/images/jE7o846MC7p596-VFd0akSV99i90aSvrq1dY)

It looks perfect, but in real life it’s not. It was extremely hard to create such universal interlingua — a lot of scientists have worked on it their whole lives. They’ve not succeeded, but thanks to them we now have morphological, syntactic, and even semantic levels of representation. But the only [Meaning-text theory](https://en.wikipedia.org/wiki/Meaning-text_theory) costs a fortune!

The idea of intermediate language will be back. Let’s wait awhile.

![Image](https://cdn-media-1.freecodecamp.org/images/vEPJYMmjDV0LLXIy07LksIiOsecXdlHcs8nI)

As you can see, all RBMT are dumb and terrifying, and that’s the reason they are rarely used unless for specific cases (like the weather report translation, and so on). Among the advantages of RBMT, often mentioned are its morphological accuracy (it doesn’t confuse the words), reproducibility of results (all translators get the same result), and the ability to tune it to the subject area (to teach economists or terms specific to programmers, for example).

Even if anyone were to succeed in creating an ideal RBMT, and linguists enhanced it with all the spelling rules, there would always be some exceptions: all the irregular verbs in English, separable prefixes in German, suffixes in Russian, and situations when people just say it differently. Any attempt to take into account all the nuances would waste millions of man hours.

And don’t forget about homonyms. The same word can have a different meaning in a different context, which leads to a variety of translations. How many meanings can you catch here: _I saw a man on a hill with a telescope_?

Languages did not develop based on a fixed set of rules — a fact which linguists love. They were much more influenced by the history of invasions in past three hundred years. How could you explain that to a machine?

Forty years of the Cold War didn’t help in finding any distinct solution. RBMT was dead.

### Example-based Machine Translation (EBMT)

Japan was especially interested in fighting for machine translation. There was no Cold War, but there were reasons: very few people in the country knew English. It promised to be quite an issue at the upcoming globalization party. So the Japanese were extremely motivated to find a working method of machine translation.

Rule-based English-Japanese translation is extremely complicated. The language structure is completely different, and almost all words have to be rearranged and new ones added. In 1984, Makoto Nagao from Kyoto University came up with the idea of **using ready-made phrases instead of repeated translation**.

Let’s imagine that we have to translate a simple sentence — “I’m going to the cinema.” And let’s say we’ve already translated another similar sentence — “I’m going to the theater” — and we can find the word “cinema” in the dictionary.

All we need is to figure out the difference between the two sentences, translate the missing word, and then not screw it up. The more examples we have, the better the translation.

I build phrases in unfamiliar languages exactly the same way!

![Image](https://cdn-media-1.freecodecamp.org/images/H-VtzpHN02SMIhwYjqmn04Uyd-nGWLwLmBwW)

EBMT showed the light of day to scientists from all over the world: it turns out, you can just feed the machine with existing translations and not spend years forming rules and exceptions. Not a revolution yet, but clearly the first step towards it. The revolutionary invention of statistical translation would happen in just five years.

### Statistical Machine Translation (SMT)

In early 1990, at the IBM Research Center, a machine translation system was first shown which knew nothing about rules and linguistics as a whole. It analyzed similar texts in two languages and tried to understand the patterns.

![Image](https://cdn-media-1.freecodecamp.org/images/5qBpooShbY6xVngSotA6KINHyHP7NKeTJryb)

The idea was simple yet beautiful. An identical sentence in two languages split into words, which were matched afterwards. This operation repeated about 500 million times to count, for example, how many times the word “Das Haus” translated as “house” vs “building” vs “construction”, and so on.

If most of the time the source word was translated as “house”, the machine used this. Note that we did not set any rules nor use any dictionaries — all conclusions were done by machine, guided by stats and the logic that “if people translate that way, so will I.” And so statistical translation was born.

![Image](https://cdn-media-1.freecodecamp.org/images/jG95Sgc2W4VJbwi4LFlJeMHnjLZbdGydCCzI)

The method was much more efficient and accurate than all the previous ones. And no linguists were needed. The more texts we used, the better translation we got.

![Image](https://cdn-media-1.freecodecamp.org/images/uF96He1UZaLMkC1TEuBGzoHAhw3PAvF8mgam)
_Google’s statistical translation from the inside. It shows not only the probabilities but also counts the reverse statistics._

There was still one question left: how would the machine correlate the word “Das Haus,” and the word “building” — and how would we know these were the right translations?

The answer was that we wouldn’t know. At the start, the machine assumed that the word “Das Haus” equally correlated with any word from the translated sentence. Next, when “Das Haus” appeared in other sentences, the number of correlations with the “house” would increase. That’s the “word alignment algorithm,” a typical task for university-level machine learning.

The machine needed millions and millions of sentences in two languages to collect the relevant statistics for each word. How did we get them? Well, we decided to take the abstracts of the European Parliament and the United Nations Security Council meetings — they were available in the languages of all member countries and were now available for download at [UN Corpora](https://catalog.ldc.upenn.edu/LDC2013T06) and [Europarl Corpora](http://www.statmt.org/europarl/).

#### Word-based SMT

In the beginning, the first statistical translation systems worked by splitting the sentence into words, since this approach was straightforward and logical. IBM’s first statistical translation model was called Model one. Quite elegant, right? Guess what they called the second one?

**_Model 1: “the bag of words”_**

![Image](https://cdn-media-1.freecodecamp.org/images/4dBTKxFLuXkmeALMuxILitzmBd0zVOQVrhnP)

Model one used a classical approach — to split into words and count stats. The word order wasn’t taken into account. The only trick was translating one word into multiple words. For example, “Der Staubsauger” could turn into “Vacuum Cleaner,” but that didn’t mean it would turn out vice versa.

Here’re some simple implementations in Python: [shawa/IBM-Model-1](https://github.com/shawa/IBM-Model-1).

**_Model 2: considering the word order in sentences_**

![Image](https://cdn-media-1.freecodecamp.org/images/AWurqrK2Zag9dIZSgYVGZCFxklsrZot7WLZ2)

The lack of knowledge about languages’ word order became a problem for Model 1, and it’s very important in some cases.

Model 2 dealt with that: it memorized the usual place the word takes at the output sentence and shuffled the words for the more natural sound at the intermediate step. Things got better, but they were still kind of crappy.

**_Model 3: extra fertility_**

![Image](https://cdn-media-1.freecodecamp.org/images/aPxpW2ssFd2wDio9C51Zbb0sIdXLBAV8DoYP)

New words appeared in the translation quite often, such as articles in German or using “do” when negating in English. “Ich will keine Persimonen” → “I **do** not want Persimmons.” To deal with it, two more steps were added to Model 3.

* The NULL token insertion, if the machine considers the necessity of a new word
* Choosing the right grammatical particle or word for each token-word alignment

**_Model 4: word alignment_**

Model 2 considered the word alignment, but knew nothing about the reordering. For example, adjectives would often switch places with the noun, and no matter how good the order was memorized, it wouldn’t make the output better. Therefore, Model 4 took into account the so-called “relative order” — the model learned if two words always switched places.

**_Model 5: bugfixes_**

Nothing new here. Model 5 got some more parameters for the learning and fixed the issue with conflicting word positions.

Despite their revolutionary nature, word-based systems still failed to deal with cases, gender, and homonymy. Every single word was translated in a single-true way, according to the machine. Such systems are not used anymore, as they’ve been replaced by the more advanced phrase-based methods.

#### Phrase-based SMT

This method is based on all the word-based translation principles: statistics, reordering, and lexical hacks. Although, for the learning, it split the text not only into words but also phrases. These were the n-grams, to be precise, which were a contiguous sequence of n words in a row.

Thus, the machine learned to translate steady combinations of words, which noticeably improved accuracy.

![Image](https://cdn-media-1.freecodecamp.org/images/lGJNqYGZOJMjs23F8-xf6E4buXptvm2IBzjg)

The trick was, the phrases were not always simple syntax constructions, and the quality of the translation dropped significantly if anyone who was aware of linguistics and the sentences’ structure interfered. Frederick Jelinek, the pioneer of the computer linguistics, joked about it once: “Every time I fire a linguist, the performance of the speech recognizer goes up.”

Besides improving accuracy, the phrase-based translation provided more options in choosing the bilingual texts for learning. For the word-based translation, the exact match of the sources was critical, which excluded any literary or free translation. The phrase-based translation had no problem learning from them. To improve the translation, researchers even started to parse the news websites in different languages for that purpose.

![Image](https://cdn-media-1.freecodecamp.org/images/Y9xbp5BnvnRGFuAlJOamXjfYEcAYVr9lVJDA)

Starting in 2006, everyone began to use this approach. Google Translate, Yandex, Bing, and other high-profile online translators worked as phrase-based right up until 2016. Each of you can probably recall the moments when Google either translated the sentence flawlessly or resulted in complete nonsense, right? The nonsense came from phrase-based features.

The good old rule-based approach consistently provided a predictable though terrible result. The statistical methods were surprising and puzzling. Google Translate turns “three hundred” into “300” without any hesitation. That’s called a statistical anomaly.

Phrase-based translation has become so popular, that when you hear “statistical machine translation” that is what is actually meant. Up until 2016, all studies [lauded](http://www.aclweb.org/anthology/D16-1161) phrase-based translation as the state-of-the-art. Back then, no one even thought that Google was already stoking its fires, getting ready to change our whole image of machine translation.

### Syntax-based SMT

This method should also be mentioned, briefly. Many years before the emergence of neural networks, syntax-based translation was considered “the future or translation,” but the idea did not take off.

The proponents of syntax-based translation believed it was possible to merge it with the rule-based method. It’s necessary to do quite a precise syntax analysis of the sentence — to determine the subject, the predicate, and other parts of the sentence, and then to build a sentence tree. Using it, the machine learns to convert syntactic units between languages and translates the rest by words or phrases. That would have solved the word alignment issue once and for all.

![Image](https://cdn-media-1.freecodecamp.org/images/JKfKjepj-r-NgsmX7A1qipPF7Jb1LEJYghAQ)
_Example taken from the [great slide show](http://www.aclweb.org/anthology/P01-1067" rel="noopener" target="_blank" title="">Yamada and Knight [2001]</a> and this <a href="http://homepages.inf.ed.ac.uk/pkoehn/publications/esslli-slides-day5.pdf" rel="noopener" target="_blank" title=")._

The problem is, the syntactic parsing works terribly, despite the fact that we consider it solved a while ago (as we have the ready-made libraries for many languages). I tried to use syntactic trees for tasks a bit more complicated than to parse the subject and the predicate. And every single time I gave up and used another method.

Let me know in the comments if you succeed using it at least once.

### Neural Machine Translation (NMT)

A quite amusing [paper](https://arxiv.org/abs/1406.1078) on using neural networks in machine translation was published in 2014. The Internet didn’t notice it at all, except Google — they took out their shovels and started to dig. Two years later, in November 2016, Google made a game-changing [announcement](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html).

The idea was close to transferring the style between photos. Remember apps like [Prisma](https://prisma-ai.com/), which enhanced pictures in some famous artist’s style? There was no magic. The neural network [was taught](https://harishnarayanan.org/writing/artistic-style-transfer/) to recognize the artist’s paintings. Next, the last layers containing the network’s decision were removed. The resulting stylized picture was just the intermediate image that network got. That’s the network’s fantasy, and we consider it beautiful.

![Image](https://cdn-media-1.freecodecamp.org/images/BzkZsyBq0kWiBKdPvt41ZPhyL-vecimThXod)

If we can transfer the style to the photo, what if we try to impose another language to a source text? The text would be that precise “artist’s style,” and we would try to transfer it while keeping the essence of the image (in other words, the essence of the text).

Imagine I’m trying to describe my dog — average size, sharp nose, short tail, always barks. If I gave you this set of the dog’s features, and if the description was precise, you could draw it, even though you have never seen it.

![Image](https://cdn-media-1.freecodecamp.org/images/6oDjU1XWlLo1313uKFsTLN43bv5FbVTTC5Oh)

Now, imagine the source text is the set of specific features. Basically, it means that you encode it, and let the other neural network decode it back to the text, but, in another language. The decoder only knows its language. It has no idea about of the features’ origin, but it can express them in, for example, Spanish. Continuing the analogy, it doesn’t matter how you draw the dog — with crayons, watercolor or your finger. You paint it as you can.

Once again — one neural network can only encode the sentence to the specific set of features, and another one can only decode them back to the text. Both have no idea about the each other, and each of them knows only its own language. Recall something? Interlingua is back. Ta-da.

![Image](https://cdn-media-1.freecodecamp.org/images/2TRCJS9nG0g1YVZPzbeg3DKvZLgsMEEiBXRs)

The question is, how do we find those features? It’s obvious when we’re talking about the dog, but how to deal with the text? Thirty years ago scientists already tried to create the universal language code, and it ended in a total failure.

Nevertheless, we have deep learning now. And that’s its essential task! The primary distinction between the deep learning and classic neural networks lays precisely in the ability to search for those specific features, without any idea of their nature. If the neural network is big enough, and there are a couple of thousand video cards at hand, it’s possible to find those features in the text as well.

Theoretically, we can pass the features gotten from the neural networks to the linguists, so that they can open brave new horizons for themselves.

The question is, what type of neural network should be used for encoding and decoding? Convolutional Neural Networks (CNN) fit perfectly for pictures since they operate with independent blocks of pixels.

But there are no independent blocks in the text — every word depends on its surroundings. Text, speech, and music are always consistent. So recurrent neural networks (RNN) would be the best choice to handle them, since they remember the previous result — the prior word, in our case.

Now RNNs are used everywhere — Siri’s speech recognition (it’s parsing the sequence of sounds, where the next depends on the previous), keyboard’s tips (memorize the prior, guess the next), music generation, and even chatbots.

![Image](https://cdn-media-1.freecodecamp.org/images/DD6GvRmtxZGhC9toN1CHXUBWLhUXLpJSiJF5)

> **For the nerds like me:** in fact, the neural translators’ architecture varies widely. The regular RNN was used at the beginning, then upgraded to bi-directional, where the translator considered not only words before the source word, but also the next word. That was much more effective. Then it followed with the hardcore multilayer RNN with LSTM-units for long-term storing of the translation context.

In two years, neural networks surpassed everything that had appeared in the past 20 years of translation. Neural translation contains 50% fewer word order mistakes, 17% fewer lexical mistakes, and 19% fewer grammar mistakes. The neural networks even learned to harmonize gender and case in different languages. And no one taught them to do so.

The most noticeable improvements occurred in fields where direct translation was never used. Statistical machine translation methods always worked using English as the key source. Thus, if you translated from Russian to German, the machine first translated the text to English and then from English to German, which leads to a double loss.

Neural translation doesn’t need that — only a decoder is required so it can work. That was the first time that direct translation between languages with no сommon dictionary became possible.

![Image](https://cdn-media-1.freecodecamp.org/images/9RYJB0uToAIdePWQ3ZDqO392eXNJqKA46C6S)

#### Google Translate (since 2016)

In 2016, Google turned on neural translation for [nine languages](https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation). They developed their system named Google Neural Machine Translation (GNMT). It consists of 8 encoder and 8 decoder layers of RNNs, as well as attention connections from the decoder network.

![Image](https://cdn-media-1.freecodecamp.org/images/9ZNTL9njX6FZP3zKlE7q5fnOgedwQGi6H6Ws)

They not only divided sentences, but also words. That was how they dealt with one of the major NMT issues — rare words. NMTs are helpless when the word is not in their lexicon. Let’s say, “Vas3k”. I doubt anyone taught the neural network to translate my nickname. In that case, GMNT tries to break words into word pieces and recover the translation of them. Smart.

> Hint: Google Translate used for website translation in the browser still uses the old phrase-based algorithm. Somehow, Google hasn’t upgraded it, and the differences are quite noticeable compared to the online version.

Google uses a crowdsourcing mechanism in the online version. People can choose the version they consider the most correct, and if lots of users like it, Google will always translate this phrase that way and mark it with a special badge. This works fantastically for short everyday phrases such as, “Let’s go to the cinema,” or, “I’m waiting for you.” Google knows conversational English better than I do :(

Microsoft’s Bing works exactly like Google Translate. But Yandex is different.

#### Yandex Translate (since 2017)

Yandex launched its neural translation system in 2017. Its main feature, as declared, was hybridity. Yandex combines neural and statistical approaches to translate the sentence, and then it choose the best one with its favorite CatBoost algorithm.

The thing is, neural translation often fails when translating short phrases, since it uses context to choose the right word. It would be hard if the word appeared very few times in a training data. In such cases, a simple statistical translation finds the right word quickly and simply.

![Image](https://cdn-media-1.freecodecamp.org/images/-7nyvsxkdMVtSkHOErvs4fINwnbg9shky24U)

Yandex doesn’t share the details. It fends us off with marketing [press-releases](https://yandex.com/company/blog/one-model-is-better-than-two-yu-yandex-translate-launches-a-hybrid-machine-translation-system/). OKAY.

> It looks like Google uses SMT for the translation of words and short phrases. They don’t mention that in any articles, but it’s quite noticeable if you look at the difference between the translation of short and long expressions. Besides, SMT is used for displaying the word’s stats.

### The conclusion and the future

Everyone’s still excited about the idea of “Babel fish” — instant speech translation. Google has made steps towards it with its Pixel Buds, but in fact, it’s still not what we were dreaming of. The instant speech translation is different from the usual translation. You need to know when to start translating and when to shut up and listen. I haven’t seen suitable approaches to solve this yet. Unless, maybe, Skype…

And here’s one more empty area: all the learning is limited to the set of parallel text blocks. The deepest neural networks still learn at parallel texts. We can’t teach the neural network without providing it with a source. People, instead, can complement their lexicon with reading books or articles, even if not translating them to their native language.

If people can do it, the neural network can do it too, in theory. I found [only one](https://arxiv.org/abs/1710.04087) prototype attempting to incite the network, which knows one language, to read the texts in another language in order to gain experience. I’d try it myself, but I’m silly. Ok, that’s it.

> This story originally was written in Russian and then translated into English on [**Vas3k.com**](http://vas3k.com/blog/machine_translation/) by Vasily Zubarev. He is my pen-friend and I’m pretty sure that his blog should be spread.

### Useful links

* [Philipp Koehn: Statistical Machine Translation](https://www.amazon.com/dp/0521874157/). Most complete collection of the methods I’ve found.
* [Moses](http://www.statmt.org/moses/) — popular library for creating own statistical translations
* [OpenNMT](http://opennmt.net/) — one more library, but for the neural translators
* The article from one of my favorite bloggers [explaining RNN and LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* A video [“How to Make a Language Translator”](https://www.youtube.com/watch?v=nRBnh4qbPHI), funny guy, neat explanation. Still not enough.
* Text guide from TensorFlow about [creation of your own neural translator](https://www.tensorflow.org/tutorials/seq2seq), for those who want more examples and to try the code.

#### Others articles from Vas3k.com

[**How Ethereum and Smart Contracts Work**](http://vas3k.com/blog/ethereum/)  
[_Distributed Turing Machine with Blockсhain Protection_vas3k.com](http://vas3k.com/blog/ethereum/)[**Blockchain Inside Out: How Bitcoin Works**](http://vas3k.com/blog/blockchain/)  
[_Once and for all in simple words_vas3k.com](http://vas3k.com/blog/blockchain/)

#### One last thing…

_If you liked this article, click the_? _below, and share it with other people so they can enjoy it as well._

