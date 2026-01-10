---
title: Make your complex scheduling simple with timeboard, a Python library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-06T14:42:11.000Z'
originalURL: https://freecodecamp.org/news/introducing-timeboard-a-python-business-calendar-package-a2335898c697
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yr9qoXFRXXNOeiZK.
tags:
- name: business
  slug: business
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Maxim Mamaev

  timeboard is a Python library that creates schedules of work periods and performs
  calendar calculations over them. You can build standard business day calendars as
  well as a variety of other schedules, simple or complex.

  You can find ...'
---

By Maxim Mamaev

`timeboard` is a Python library that creates schedules of work periods and performs calendar calculations over them. You can build standard business day calendars as well as a variety of other schedules, simple or complex.

**You can find the Documentation [here](http://timeboard.readthedocs.io/en/latest/).**

**Check out the GitHub repo [here](https://github.com/mmamaev/timeboard).**

**Find it on PyPI [here](https://pypi.python.org/pypi/timeboard).**

### The story

It started with the headcount case. Our company introduced KPIs involving the revenue per employee, so we needed to know the average annual headcount of each team. I had already been writing Python scripts, so I was not intimidated.

To obtain a headcount I had to calculate the number of business days each employee has spent with the company within the year. Pandas would handle it in a sec, I thought. But it came out that Pandas could not.

The Russian business calendar is cumbersome. They swap weekdays with Saturdays or Sundays to fill gaps between holidays and weekends. For example, you have to come to work on a Saturday in February to be reimbursed with a free Monday preceding a holiday Tuesday somewhere in May.

The scheme for each year is unique. Pandas’s business day calendar supports only one-way amendments for holiday observations. So, I could turn a business day into a day off, but not the other way round.

Then there were operators in the call center, and my anxiety swung the other way. They work in shifts of varying length, and one shift in followed by three shifts out. To get the call center statistics, I did not need the business day calendar. Yet I had to count the number of particular operator’s shifts in a period of time.

And finally, an offbeat problem. In my local Honda dealership, the mechanics work on alternate weekly schedules: Monday, Tuesday, Saturday and Sunday this week, and Wednesday through Friday the next week. I wanted to always be served by a particular mechanic, because the other one had once messed up the brakes. I wanted a simple way to determine the next shift of “my” mechanic.

These cases have a common foundation. Their solutions would rely upon a schedule of “on-duty” and “off-duty” periods of time. We should be able to construct variously structured schedules suitable for different business cases. Queries and calculations run over the schedule must distinguish between “on-duty” and “off-duty” periods.

I could not find a Python package that provided the means for building and querying such schedules. As it happened, I had some free time to write it myself.

![Image](https://cdn-media-1.freecodecamp.org/images/i7RmM4xORdvi4kS1KEjvqxeq5lZT9OI9KAjo)

### The concept

`timeboard` is a Python library that creates schedules of work periods and performs calendar calculations over them. These objects themselves are called timeboards.

There are three major steps in reasoning about a timeboard.

You start with an interval of time which sets the bounds of your calendar. Everything will be confined to this interval. It is called the (reference) frame. The frame consists of base units. A base unit is the smallest period of time you need for gauging your calendar. For example, if you reason in terms of business days, then the base unit is a day. Alternatively, if you build a schedule of multiple-hour shifts, then the base unit is one hour.

![Image](https://cdn-media-1.freecodecamp.org/images/sI-5OZ10OfBSQP2EOH3I738uzuJA1bXjHufU)

On the next step, you define the rules of marking up the frame into workshifts. Workshifts are periods of time that you care about. They make up your calendar. It is workshifts that you want to schedule or to count. In a standard business days calendar, workshift is a day (and base unit is a day too, so they coincide).

In a call center, workshift is a period of several hours when a particular shift of operators is on duty. The base unit is likely to be one hour, and each workshift comprises a (probably varying) number of base units.

The sequence of workshifts filling the frame is called the timeline.

Finally, you create one or more schedules. A schedule is like a stencil laid over the timeline. Its purpose is to tell on-duty workshifts from off-duty ones.

A schedule needs something to work with in order to declare a workshift on duty or off duty. This is why you provide a label for each workshift, or rather a rule for labeling them while the frame is marked up into the timeline. Each schedule defines a selector function which inspects the workshift’s label and returns True for the on-duty workshifts and False otherwise. Unless you override it, a timeline is accompanied by the default schedule whose selector returns the boolean value of the label.

Sometimes you want to define several schedules for the same timeline. For example, in a call center, there will be the schedule for the call center as a whole, and a separate schedule for each team of operators. The same workshift may be found on duty under some schedules and off duty under the others.

![Image](https://cdn-media-1.freecodecamp.org/images/MlUNZdQm8rr9PwqqoqCm5YLfoeXz99sR6i-q)

Timeboard = timeline + schedules. More precisely, _timeboard_ is a collection of work _schedules_ based on a specific _timeline_ of _workshifts_ built upon a reference _frame_.

Once you have got a timeboard, you may carry out the useful work: do calendar calculations in order to solve the problems like those described in the prologue.

Every computation performed with timeboard is duty-aware. The invoked method “sees” only workshifts with the specified duty and ignores the others. In order to reveal the duty of the workshifts, the method needs to be given a schedule. Therefore, each computation on the timeboard is parametrized with a duty and a schedule.

By default, the duty is “on” and the schedule is the default schedule of the timeboard. For example, if you call `count()` without arguments on some interval of a timeboard, you will get the number of workshifts in the interval that are declared on duty under the default schedule. These defaults make life easier because in practice you will want to deal mostly with on-duty workshifts.

### The API

The full timeboard documentation is available on [Read the Docs](https://timeboard.readthedocs.io/).

The package can be installed with the usual `pip install timeboard`.

#### Set up a timeboard

The simplest way to get started is to use a preconfigured calendar which is shipped with the package. Let’s take a regular business day calendar for the United States.

```
 >>> import timeboard.calendars.US as US >>> clnd = US.Weekly8x5()
```

`clnd` object is a timeboard (an instance of `timeboard.Timeboard` class). It has only one default schedule which selects weekdays as on-duty workshifts while weekends, as well as observations of US federal holidays, are declared off duty.

The tools for building your own timeboard will be briefly reviewed later on after we look at what you can do with a timeboard.

#### Play with workshifts

Calling a timeboard instance `clnd()` with a single point in time retrieves the workshift that contains this point. How that you have a workshift you can query its duty:

**Is a certain date a business day?**

```
>>> ws = clnd('27 May 2017')>>> ws.is_on_duty()False
```

Indeed, it was a Saturday.

You can also look into the future or in the past from the current workshift:

**When was the next business day?**

```
>>> ws.rollforward()Workshift(6359) of 'D' at 2017–05–30
```

The returned workshift has the sequence number of 6359 and represents the day of 30 May 2017, which, by the way, was the Tuesday after the Memorial Day holiday.

**If we were to finish the project in 22 business days starting on 01 May 2017, when would be our deadline?**

```
>>> clnd('01 May 2017') + 22Workshift(6361) of 'D' at 2017–06–01
```

This is the same as:

```
>>> clnd('01 May 2017').rollforward(22)Workshift(6361) of 'D' at 2017–06–01
```

#### Play with intervals

Calling `clnd()` with a different set of parameters produces an object representing an interval on the calendar. The interval below contains all workshifts of the month of May 2017:

```
>>> may2017 = clnd('May 2017', period='M')
```

**How many business days were there in May?**

```
>>> may2017.count()22
```

**How many days off?**

```
>>> may2017.count(duty='off')9
```

**How many working hours?**

```
>>> may2017.worktime()176
```

An employee was on the staff from April 3, 2017, to May 15, 2017. **What portion of April’s salary did the company owe them?**

Note that calling `clnd()` with a tuple of two points in time produces an interval containing all workshifts between these points, inclusively.

```
>>> time_in_company = clnd(('03 Apr 2017','15 May 2017'))>>> time_in_company.what_portion_of(clnd('Apr 2017', period='M'))1.0
```

Indeed, the 1st and the 2nd of April in 2017 fell on the weekend, therefore, having started on the 3rd, the employee checked out all the working days in the month.

**And what portion of May’s?**

```
>>> time_in_company.what_portion_of(may2017)0.5
```

**How many days had the employee worked in May?**

The multiplication operator returns the intersection of two intervals.

```
>>> (time_in_company * may2017).count()11
```

**How many hours?**

```
>>> (time_in_company * may2017).worktime()88
```

An employee was on the staff from 01 Jan 2016 to 15 Jul 2017. **How many years had this person worked for the company?**

```
>>> clnd(('01 Jan 2016', '15 Jul 2017')).count_periods('A')1.5421686746987953
```

![Image](https://cdn-media-1.freecodecamp.org/images/jsj2ogpaBTEwK2iz4RVJmVLuwBi4jyp1cPvW)

#### Build your own timeboard

For the purpose of introduction, I will just plunge into two examples. If it seems too steep, please, find the thorough discussion of the construction tools in the [project documentation](https://timeboard.readthedocs.io/en/latest/making_a_timeboard.html).

The import statement for this section:

```
>>> import timeboard as tb
```

Let me return to a schedule of workshifts in the car dealership which I mentioned in the prologue. A mechanic works on Monday, Tuesday, Saturday, and Sunday this week, and on Wednesday, Thursday, and Friday next week; then the bi-weekly cycle repeats. The timeboard is created by the following code:

```
>>> biweekly = tb.Organizer(marker='W',...     structure=[[1,1,0,0,0,1,1], [0,0,1,1,1,0,0]])>>> clnd = tb.Timeboard(base_unit_freq='D', ...     start='01 Oct 2017', end='31 Dec 2018', ...     layout=biweekly)
```

It makes sense to look into the last statement first. It creates a timeboard named `clnd`. The first three parameters define the frame to be a sequence of days (‘`D`’) from 01 Oct 2017 to 31 Dec 2018. The `layout` parameter tells how to organize the frame into the timeline of workshifts. This job is commissioned to an `Organizer` named `biweekly`.

The first statement creates this `Organizer` which takes two parameters: `marker` and `structure`. We use a`marker` to place marks on the frame. The marks are kind of milestones which divide the frame into subframes, or “spans”. In the example `marker=’W’` puts a mark at the beginning of each calendar week. Therefore, each span represents a week.

The `structure` parameter tells how to create workshifts within each span. The first element of `structure`, the list `[1,1,0,0,0,1,1]`, is applied to the first span (i.e. to the first week of our calendar). Each base unit (that is, each day) within the span becomes a workshift. The workshifts receive labels from the list, in order.

The second element of `structure`, the list `[0,0,1,1,1,0,0]`, is analogously applied to the second span (the second week). After this, since we’ve gotten no more elements, a `structure` is replayed in cycles. Hence, the third week is serviced by the first element of `structure`, the fourth week by the second, and so on.

As a result, our timeline becomes the sequence of days labeled with the number `1` when the mechanic is on duty and with the number `0` when he or she is not. We have not specified any schedule, because the schedule which is built by default suits us fine. The default schedule considers the boolean value of the label, so `1` translates into ‘on duty’, and zero into ‘off duty’.

With this timeboard, we can do any type of calculations that we have done earlier with the business calendar. For example, if a person was employed to this schedule from November 4, 2017, and salary is paid monthly, what portion of November’s salary has the employee earned?

```
>>> time_in_company = clnd(('4 Nov 2017', None))>>> nov2017 = clnd('Nov 2017', period='M')>>> time_in_company.what_portion_of(nov2017)0.8125
```

In the second example we will build a timeboard for a call center. The call center operates round-the-clock in shifts of varying length: 08:00 to 18:00 (10 hours), 18:00 to 02:00 (8 hours), and 02:00 to 08:00 (6 hours). An operator’s schedule consists of one on-duty shift followed by three off-duty shifts. Hence, four teams of operators are needed. They are designated as ‘A’, ‘B’, ‘C’, and ‘D’.

```
>>> day_parts = tb.Marker(each='D', ...     at=[{'hours':2}, {'hours':8}, {'hours':18}])>>> shifts = tb.Organizer(marker=day_parts, ...     structure=['A', 'B', 'C', 'D'])>>> clnd = tb.Timeboard(base_unit_freq='H', ...     start='01 Jan 2009 02:00', end='01 Jan 2019 01:59',...     layout=shifts)>>> clnd.add_schedule(name='team_A', ...    selector=lambda label: label=='A')
```

There are four key differences from the dealership case. We will examine them one by one.

First, the frame’s base unit is now a one-hour period (`base_unit_freq='H'`) instead of a one-day period of the dealership’s calendar.

Second, the value of the `marker` parameter of the Organizer is now a complex object instead of a single calendar frequency it was before. This object is an instance of `Marker` class. It is used to define rules for placing marks on the frame when the simple division of the frame into uniform calendar units is not sufficient. The signature of the Marker above is almost readable — it says: place a mark on _each day (‘D’) at 02:00 hours, 08:00 hours, and 18:00 hours_.

Third, the value of the `structure` is now simpler: it is a one-level list of teams’ labels. When an element of the `structure` is not an iterable of labels but just one label, its application to a span produces a single workshift which, literally, spans the span.

In our example, the very first span comprises six one-hour base units starting at 2, 3, 4 … 7 o’clock in the morning of 01 Jan 2009. All these base units are combined into the single workshift with label ‘A’. The second span comprises ten one-hour base units starting at 8, 9, 10 … 17 o’clock. These base units are combined into the single workshift with label ‘B’, and so on. When all labels have been taken, the structure is replayed, so the fifth span (08:00:00–17:59:59 on 01 Jan 2009) becomes a workshift with label ‘A’.

To recap, if an element of `structure` is a list of labels, each base unit of the span becomes a workshift and receives a label from the list. If an element of `structure` is a single label, all base units of the span are combined to form a single workshift which receives this label.

And finally, we explicitly created a schedule for team A. The default schedule does not serve our purpose as it returns “always on duty”. This is true for the call center as a whole but not so for a particular team. For the new schedule, we supply the name and the selector function which returns True for all workshifts labeled with ‘A’. For the practical use, you will want to create the schedules for the other teams as well.

This timeboard is as good to work with as any other. However, this time we will have to explicitly specify the schedule we want to use.

```
>>> schedule_A = clnd.schedules['team_A']
```

**How many shifts did the operators of team A sit in November 2017?**

```
>>> nov2017 = clnd('Nov 2017', period='M', schedule=schedule_A)>>> nov2017.count()22
```

**And how many hours were there in total?**

```
>>> nov2017.worktime()176
```

A person was employed as an operator in team A from November 4, 2017. Salary is paid monthly. **What portion of November’s salary has the employee earned?**

```
>>> time_in_company = clnd(('4 Nov 2017',None), schedule=schedule_A)>>> time_in_company.what_portion_of(nov2017)0.9090909090909091
```

#### More use cases

You can find more use cases (taken almost from real life) in the [jupyter notebook](https://timeboard.readthedocs.io/en/latest/_downloads/use_cases.ipynb) which is the part of the [project documentation](https://timeboard.readthedocs.io/en/latest/use_cases.html).

Please feel free to use `timeboard` and do not hesitate to leave feedback or open issues on [GitHub](https://github.com/mmamaev/timeboard/issues) .

