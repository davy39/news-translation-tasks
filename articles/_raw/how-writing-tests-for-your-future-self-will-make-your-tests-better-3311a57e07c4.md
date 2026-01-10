---
title: How writing tests for your future self will make your tests better
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
seo_title: null
seo_desc: 'By Eumir Gaspar

  When practicing test driven development (TDD), we sometimes tend to focus on testing
  everything. This 100% coverage mentality can sometimes lead us to overcomplicate
  things.

  Before, I was the one leading the charge to make tests DRY-e...'
---

By Eumir Gaspar

When practicing test driven development (TDD), we sometimes tend to focus on testing **everything.** This 100% coverage mentality can sometimes lead us to overcomplicate things.

Before, I was the one leading the charge to make tests DRY-er, because I hated seeing repetitive code. I was new to metaprogramming in Ruby back then, and I always wanted to make things “simpler” by mashing up the repetitive code and coming up with a monster. Case in point:

```ruby
describe 'when receiving the hero details' do
  it 'should have the top level keys as methods' do
    top_level_keys = %w{id name gender level paragonLevel hardcore skills items followers stats kills progress dead last-updated}

    top_level_keys.each do |tl_key|
      @my_hero.send(tl_key).must_equal @my_hero.response[tl_key.camelize(:lower)]
    end
  end
```

Okay, so that [was way back in 2012.](https://github.com/corroded/covetous/blob/master/spec/covetous/profile/hero_spec.rb#L20-L32) As a background, this was a [Ruby gem](https://rubygems.org/) (similar to an [npm package](https://www.npmjs.com/)) for Blizzard’s [Diablo 3 API](https://dev.battle.net/io-docs). So what was I testing here? Upon reading the code, it seems pretty straightforward: it says the top level keys can be methods. So if the API was returning something like:

```js
{
  paragonLevel: 10,
  hardcore: true,
  kills: 1234
}
```

Then given a hero instance, I can just call the them as methods and it should return them like so:

```
> hero = Covetous::Profile::Hero.new 'user#1234', '1234'
> hero.paragon_level # 10
> hero.kills # 1234
```

Okay, I’ll be honest. When I was writing this article, I was looking through my old open source projects as an example and saw this. It looked pretty straightforward as I said, but while actually analyzing it, I realised it was much worse than I thought. It took me fifteen minutes to just get what it does, even if the spec says what it should be doing. Before I typed the above block, I wanted to double check I understood it correctly. While I did, the way I wrote the tests made everything confusing. Why?

### The problem

As I said, I was new to metaprogramming back then and saw an opportunity to use it. At that time, it seemed very clever, but now that I have more experience, I know that doing this in tests is a liability more than a boon.

You see, one of the things I learned is that **test code is untested code**. Let that sink in for a bit.

[**Test code is untested code.**](https://twitter.com/corrodedlotus/status/982741953308700672)

[**TEST CODE IS UNTESTED CODE.**](https://github.com/ericboehs/talk-notes/blob/master/2015-11-15-1040-rubyconf-how-to-stop-hating-your-test-suite.md#test-structre)

Those are two different links by the way. It basically means that ANY code that your test runs can potentially have it’s own errors. You don’t actually have tests for test code, so there’s no guarantee that it works. The only guarantee you can do is have the test fail when you comment out the actual lines in the code and have it pass when you uncomment it. Sometimes though, even with this red-green testing, you can still get false positives. So the best way to avoid this is to keep your tests **as simple as possible** and **as explicit as possible**.

So back to my test. If I remember correctly, I initially did the methods one by one. I then saw a pattern which made me think that it was going to be the same pattern for all the methods at least, so why not make the code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)-er?

I made an array of all the possible methods, looped through them, and did an assertion that calling the method should be the same as looking at the response and getting the value. Easy enough, but the main thing that put me off was this:

```
@my_hero.send(tl_key).must_equal @my_hero.response[tl_key.camelize(:lower)]
```

In Ruby, `send` calls the passed string as a method. So if `tl_key`'s value was `paragonLevel` (from the array), this line basically says:

```
@my_hero.paragonLevel.must_equal @my_hero.response['paragonLevel']
```

See, this is where I keep doubting myself again. My `README` says it should be `@my_hero.paragon_level`, but looking at the test, it isn’t. Who should I trust now? My tests that are passing, or my `README`? This is the exact reason why metaprogramming in tests is dangerous — you never truly know if your tests are passing, either because they are correct or you misconfigured it somehow. It’s almost the same as NOT writing tests!

### Doing it a better way

So how would I re-write this? I have since learned that writing tests for **my ten year old self** would suffice. Meaning, myself ten years ago. I always ask myself: “Ten years from now, would I still be able to understand this, without context?” If not, then that means I either need to write a note in the comments **or** my test is too complicated.

Let’s try re-writing this. As I said, we should be as simple and as explicit as possible. Here’s one solution:

```
# Given I queried my hero against the API:
let(:my_hero) { Covetous::Profile::Hero.new 'corroded-6950', '12345678' }
it 'should have the top level keys as methods' do
  expect(my_hero.id).to eq 12345
  expect(my_hero.name).to eq 'corrodeath'
  expect(my_hero.gender).to eq 'female'
  expect(my_hero.level).to eq 70
  ...
end
```

See how explicit it is? It’s repetitive, sure, but 10 years from now I am pretty sure I would still understand what my expectations were. I don’t have to ‘compile and interpret’ the code in my brain. I just read the specs!

Also, with this, I didn’t even have to recall what `camelize(:lower)` actually does (confession: I had to look it up while I was reading through my old code).

How about another example? So given we have a model:

```ruby
class Something < ActiveRecord::Base
  VALID_THINGS = %w(yolo swag)
  OTHER_VALID_THINGS = %w(thing another_thing)
  def valid_things_ids
    where(group: group).pluck(:id)
  end
end
```

The above is just a contrived example based off a real class we have in my current company. The spec I saw was this:

```ruby
subject(:valid_things_ids) { described_class.valid_things_ids(group) }

let(:group) { 'example' }

before do
  described_class::VALID_THINGS.each do |thing|
    FactoryGirl.create(:something, group: 'example', name: thing)
  end
end

described_class::VALID_THINGS.each do |thing|
  it "contains things with the name #{thing}" do
    the_thing = described_class.find_by_group_and_name('example', thing)
    expect(valid_things_ids).to include the_thing.id
  end
end
```

Okay. First, this is a correct test, in that given a number of `somethings`, we can call the method and it returns us all the ids of `somethings` with that group (e.g. `example`).

My issue with this, however, is do we need to test all the valid things? What about `OTHER_VALID_THINGS`? If we want to test all the possible values of `VALID_THINGS` , then we should also test all the possible values of `OTHER_VALID_THINGS`. If we DON’T want to test all possible values, then why use `VALID_THINGS`? Why not just contrive a random sample and just prove that the method works?

How about something like this?

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

So here, I create 3 `somethings` and give them ids. I make the third one have a different group. Now if I run the method with `blurb` as the argument, I can expect that it includes the first two and not the last one.

Reading it a few months from now, I won’t be confused as to what is being tested since it is straightforward, and I don’t even have to ask why I am only testing a certain part of the code and not all.

Also take note of the explicitness of the test. I am expecting it to include the ids `111` and `222`. Normally, people would test it like so:

```
expect(valid_things_ids).to include random_thing.id
```

I don’t really like these tests, because they still rely on the code at this point. If for some reason the id is `nil`, and the code also had a bug where it returned `nil`, then this test would still pass. Not with explicit ids and expectations, though. Of course there will be caveats, but I think I would like to deal with those rather than the uncertainty of possible false positives.

### Wrapping up

As you can see from both the examples above, simple to read tests will help you in the long run. Being very explicit helps a lot in understanding tests and having fewer bugs.

Remember, your 100% test coverage won’t matter if half of those are false positives. Always remember your past self when testing. Try to think far ahead into the future and ask yourself what your tests mean.

