Date: 2015-05-13
Title: Technology Bandwagons (a.k.a. "New Idea Fatigue")
Category: technology
Tags: python, salt, docker, elixir, ruby

The topic came up at work today when I posted a quote in our software room in HipChat.

> I also would argue that we need to recognize fashions and trends in the computing world that don't always correlate to efficiency, practicality, or necessity. If we remember the last twenty times we jumped onto a bandwagon that went nowhere, we might be more cautious next time. In short, we need to understand the past in order to cope with the present and create the future.
>> via http://www.informit.com/articles/article.aspx?p=2350703

I was asked:

> @kmwhite please list the last 20 bandwagons you jumped on that went nowhere

It was a perfectly valid response. My simple reaction was:

> Every JS framework that gets replaced the next day by "New Hotness". (troll)

It elicited a laugh and people moved on. However, it wasn't an actual answer. This got me thinking.

Can I count 20 bandwagons? No, I cannot. Can I count some? Yes. Have I been burned multiple times? Yes.

## Inherent Aversions
The on-and-off work I have done in operations through my career has made me more hesitant to adopt new technologies/frameworks off the bat. I have seen a lot of people do it and the results are nothing more than an overly complicated ecosystem that yielded little gain besides increased cognitive load on both Dev and Operations. While I fully believe in "using the right tool for the job", sometimes the "Right Tool&#153;" is really the "Acceptable Tool&#153;"[^1]. Did cleaning up after other people make me a little curmudgeon-y? Probably. But as I find articles like "Programming is Not a Craft"[^2], "Choose Boring Technology"[^3], and "On Ruby"[^4], I realize I am not alone in these thoughts. I have an immediate aversion to new technology.

The major difficulty with this inherent aversion to things is that I can too quickly rule out a valid tool. Let's take the troll-y example of JS libraries I used. Where JS frameworks are an easy target, since they change every other day ![zombie-happy](/images/happy.gif), what about Node? It was forked to IOjs. Thankfully, they have valid reasoning:

> This project aims to continue development of io.js under an "open governance model" as opposed to corporate stewardship.[^5]

This was the only reason I read that I agreed with. The migration to Semver[^6] also was a sane idea given the changes that went on. However, I still ask "Why are we using Javascript on the server anyway?!" Is that me being adverse to so called *progress*, or simply questioning the lack of learning a new language (Java? Python? Ruby? Perl? ASP? Should I keep going?) that already runs server side. Existing server-side languages and tools have had evented frameworks for a LONG time. [Twisted](https://twistedmatrix.com/trac/) for Python? [EventMachine](http://rubyeventmachine.com/) for Ruby? Hell, even [Event](http://cpansearch.perl.org/src/JPRIT/Event-1.20/Tutorial.pdf) for Perl! What did Node and/or IOjs really provide besides the ability to bypass learning a new language?

Now, before someone goes "But Kristofer, what about the 'adequate tool for the job'? Maybe learning something else would create additional complexity!" This is true, but aren't our languages really just tools for processing data? The operational complexity of these existing frameworks are Known Entities. Building a new toolset to port a language from a browser to a server side application is NOT a Known Entity. It's the epitome of "doing something cool" rather than "doing something pragmatic". I'd **love** for an opportinuty to hear the rationalization of NodeJS' inception.

Additionally, learning the language should be an expectation of an engineer in our industry. That would be like me showing up to a construction site with a hammer going "NO WORRIES. I GOT THIS." One trick ponies are unacceptable. If you're a "${LANGUAGE} Developer", you're doing it wrong. Learning the language isn't the increase in complexity, but changing the ecosystem of your infrastructure is. You should always be learning languages and paradigms[^7].

## Technological Depressions
I wanted to say "I'm depressed about the state of industy" (I really did), but it doesn't properly express the sentiment. As I sit here typing this, I think about the global communities created through applications like Facebook, Twitter, and GitHub. I'm happy to see that these "modern" tools are a great way to further connect users with businesses. Where BBSes existed in the days of yore, we have an instant connection to share and create with others. It's not revolutionary, but evolutionary.

On the hardware side, we have smartphones and tablets. I can't be depressed about the state of the Technology industry as a whole when we have created devices that link us to the global community and information ANYWHERE IN THE WORLD WE ARE. I remember having to wait for the opportunity to use the internet at school before we got it at home, much less having dial up or the transition to any of the N number of devices on me that can connect at a given time. Our industry is actually pretty freaking awesome.

I wanted to say, that I'm "Depressed that the 'quintessentail books' of our industry are from many decades ago". Well, this one is still kinda' true. The software engineering bible, **"The Mythical Man Month"**, was published in 1975[^8]. The most recent edition includes a preface that explains why, even after all these years, that book is still relevant. Compilers? The **"Dragon Book"**[^9] was published first in 1986. If we look at the **"Gang of Four" Design Patterns**[^10] book, it was published in 1994. That's two decades ago, and I have yet to find a better book discussing design patterns. "The Practice of Programming" came out a mere five years later in 1999[^11].

Since 2000, though, most content I find is purely about putting content on a website. Granted, websites have evolved a great deal to something that is FAR more interactive than they every used to be, but is that interaction always needed? This page doesn't feature any fancy javascript interactions besides loading Disqus for comments. Even that is entirely optional when it comes to gathering the content. Was that the end? Have we stopped with the revolutions in tech and moved on to a purely evolutionary standpoint?

## Inspired Futures
So how do I break the cycle of cyncism? Frankly put, I don't entirely know that I should. Why? Let's be honest with ourselves, not every idea is a good idea. Why should I use [blessed-contrib](https://github.com/yaronn/blessed-contrib) instead of something like emitting data via [Diamond](https://github.com/python-diamond/Diamond) to a [Graphite](http://graphite.readthedocs.org/en/latest/)? Why should I adopt [Rocket/Appc](https://coreos.com/blog/appc-gains-new-support/) instead of [Docker](https://docker.com) (If you say because there's a spec that can be supported by multiple implementations in a generic fashion, I return with "Why the hell are you reading this; you clearly get 'it'...")? Why containers instead of virtual machines? What does the new tech offer? Sometimes, it's a hell of a lot of nothing. We, as engineers, don't need to grab the new and shiny. We should roll with what works until it doesn't work and demand pragmatism over "Cool Factors".

I guess the trick is finding things that inspire you. For me, it obviously isn't growning more pages on the internet. I remember the change in attitude the first day I found [Elixir](http://elixir-lang.org/). The functional programming paradigm seems like a pleasant shift forward from the day-to-day drag of Object-Oriented, MVC web frameworks. After all, isn't forward the only sane direction to travel in?

[^1]: http://www.monkeysnatchbanana.com/2015/02/24/an-acceptable-tool/
[^2]: http://dannorth.net/2011/01/11/programming-is-not-a-craft/
[^3]: http://mcfunley.com/choose-boring-technology
[^4]: http://hawkins.io/2015/03/on-ruby/
[^5]: https://iojs.org/en/faq.html
[^6]: https://github.com/iojs/io.js/blob/v1.x/CHANGELOG.md#summary-of-changes-from-nodejs-v01035-to-iojs-v100
[^7]: If you're looking for a language or paradigm, I'd highly suggest [Elixir](http://elixir-lang.org/). It's a fantastic entry to Functional Programming for people familiar with Ruby, Python, etc.
[^8]: https://en.wikipedia.org/wiki/The_Mythical_Man-Month
[^9]: https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools
[^10]: https://en.wikipedia.org/wiki/Design_Patterns
[^11]: https://en.wikipedia.org/wiki/The_Practice_of_Programming
