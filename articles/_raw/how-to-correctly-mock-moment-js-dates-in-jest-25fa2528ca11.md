---
title: How to correctly mock Moment.js/dates in Jest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T21:50:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-correctly-mock-moment-js-dates-in-jest-25fa2528ca11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W26Jdk8ZEo4QDC797b7smA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Jest
  slug: jest
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Iain Nash

  Times and dates are infamously hard to correctly implement in code. This makes testing
  date and time code correctly important. Testing allows for reasoning around logic
  in code and also to allow catching edge cases or errors before they ...'
---

By Iain Nash

Times and dates [are infamously hard](https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time) to correctly implement in code. This makes testing date and time code correctly important. Testing allows for reasoning around logic in code and also to allow catching edge cases or errors before they impact users.

A common mistake when testing date and time code is to not set the current time to a static time. If code in the UI renders today’s date and is tested properly, that test that only works until the current time changes too much. Javascript exposes the built-in `Date` object which allows for retrieving the current time through construction with no arguments or a call to the `now()` property.

[Moment.js](https://momentjs.com/) is a popular front-end date manipulation library that is commonly used to manipulate, load, format, and shift time. It uses an empty constructor to get the current time. Jest is often used in conjunction with Moment and React applications. Additionally, Jest snapshot testing introduces new dependencies on date and time that are important to consider. Below is an example problematic component that renders the current day:

An initial test for the `TodayIntro` component could look like:

However, this test will fail on any day that is not Jan 23rd. A solution to this is to override Javascript’s date function to return a known date to work against when writing tests.

This code overrides the Date constructor to set a static “current” date:

An ineffective solution is to do the date math yourself against the current time the test is run. This is an ineffective test because you’re running the same code you’re testing to test the return value. For instance, if testing by comparing formatted dates through moment, one would not catch if the moment formatting code changes `MMM` to `JAN` instead of `Jan` .

#### Ways to set a static time and timezone for Jest/JS

1. Use a library to mock out Date object to return a static date and timezone (we’d recommend [MockDate](https://github.com/boblauer/MockDate) for simple cases, but read on for a breakdown of the alternatives)
2. Mock `moment().format()` to return a static string
3. Mock the `Date` constructor and `now()` function to return a static time

Using a library in this case is preferable because these libraries are well tested, do not introduce boilerplate code and handle transparently both cases dates can be created (`Date.now()` vs `new Date()` etc.). Additionally, using a library allows for easily following test code and setting a specific time per test which allows for better testing practices.

* `[MockDate](https://github.com/boblauer/MockDate)` provides further functionality for time zones and is easy to use
* `[sinon](https://sinonjs.org/releases/v7.2.4/fake-timers/)` provides Date and timer (`setTimeout` etc.) mocks
* Manually setting the mock can be useful in limited environments, however, can become rather complicated
* `[jasmine](https://jasmine.github.io/)` (not included in jest), comes with a [jasmine.clock()](https://jasmine.github.io/api/2.6/Clock.html)

The examples below use [MockDate](https://github.com/boblauer/MockDate), which only focuses on mocking the Date object simply and handles testing time zone offsets as well for testing local time zone conversion.

A [snapshot test](https://jestjs.io/docs/en/snapshot-testing), as well, is simple to test with mocked dates:

Since [enzyme](https://airbnb.io/enzyme/) is an awesome library, an enzyme shallow example:

### How to (better) test date logic

Dates have a lot of edge cases and logic behind them. When testing dates, make sure to cover edge cases and not just set one specific date to test and move on. Dates can also vary according to locale and time zone.

Properly testing dates require reasoning around edge cases that could occur and writing tests to ensure those edge cases behave as expected and that future changes to code or libraries used in your application don’t break those assumptions. Additionally, adding code to set the current date and time to a static date and time across all test code may be easier, but prevents good reasoning around testing Dates and hides test assumptions in library code.

Here are a few incorrect and often implicit assumptions about dates:

1. Clients all exist within one time zone and daylight saving time
2. All clients exist within the developer’s time zone
3. The length of a Month name is relatively similar
4. Server clocks are always correct
5. The server knows the client’s timezone/time settings

This test assumes the server is always in the correct timezone and that timezone is set correctly. Instead, set the timezone and make sure the date matches the local timezone correctly.

It is important to ensure that when tests access the current time the “current time” is set to a static value. If the value is dynamic, either tests eventually break or a test is testing against dynamic values. Dynamic values are not effective at testing behavior since a bug will not be exposed by comparing the return value of two functions that are the same as compared to comparing to a static value that doesn’t change as the code is modified.

### Looking ahead: Date time storage and design

Having a requirement to add tests to a code base doesn’t necessarily provide any value unless those tests are reviewed, run, and reasoned about just as strictly as running code.

Date and time logic introduces a large set of possibilities in terms of behavior and output, making a strong incentive to test effectively for date and time. Beyond testing, acknowledging and keeping relevant data along with a strategy to synchronize and store date times consistently across systems early on both helps testing and makes for a better user experience.

These tips and approaches apply to more than just Javascript & Jest testing for dates and times. They also work in a NodeJS context and in a general sense around key things to test for in systems that handle date and time in general. In many cases, storing time on the server in UTC (Universal coordinated time) then converting to the local time zone based on client / browser settings is ideal. If the client is inaccessible, storing both the UTC time and user’s actual timezone is an effective way to consistently treat dates and times.

