date: 2013-03-14
Title: A PyCon Special Post - Artisan Testing
Category: testing
Tags: testing, python, tdd

Being at PyCon, I was inspired to do something. At work, I am typically writing CFEngine3 policy and not writing a lot of code. I should be filling my free time with more projects. Being around all the other great Python developers and getting to talk to them about their work (I cannot rave about [BreakfastSerial](https://github.com/theycallmeswift/BreakfastSerial) enough), I was inspired to pick up where I left off with a project of mine. That project was 'artisan'. A library for generating complete instances for testing, rather than stubbing.

Why create a library when there are copious amounts of them already in PyPI? Well, I didn't want to use stubs. I don't like stubs. When testing, I like to use the logic already in existence for my instances.

### Artisan Testing

#### Installing Artisan
Installing is nice and simple:

    pip install --user artisan

As an aside, I do not understand why there are individuals who DON'T use the '--user' flag for all their pip commands... Seriously. Why the system-wide installs, people?

#### Using Artisan
Let's assume there is a simple app you need to test with the Foo class. The Foo class looks a lot like:

    class Foo(object):
        ''' This is a simple object '''
    
        def __init__(self):
            self.name = None

Before you can use artisan, you need to setup blueprints. Blueprints are simply dictionaries that contain lambdas used to generate the random data. In my example, I use the great [python-faker](https://github.com/redneckbeard/python-faker) library (it is available on PyPI, but I find the git repo is far more current).

In 'blueprints.py':

    import faker
    
    Foo = {
      'name': lambda: faker.name.name(),
    }

In your tests, you then do:

    import blueprints
    import artisan
    
    artisan.prepare(blueprints)
    
    artisan.craft(Foo)                # Creates an instance of the Foo class with a randomly generated name
    artisan.craft(Foo, name='BarBaz') # Creates an instance of the Foo class with the name BarBaz

### A Complete Example

    Python 3.3.0 (default, Mar 13 2013, 18:04:53) 
    [GCC 4.2.1 20070719 ] on openbsd5
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import blueprints
    >>> import artisan
    >>> 
    >>> class Foo(object):
    ...     def __init__(self):
    ...         self.name = None
    ... 
    >>> 
    >>> artisan.prepare(blueprints)
    >>> artisan.craft(Foo).name
    'Mrs. Savion Kuhn'
    >>> artisan.craft(Foo).name
    'Ms. Pearlie Collier'
    >>> type(artisan.craft(Foo))    
    <class '__main__.Foo'>

### Miscellaneous
I've been trying to keep artisan Python3 and Python2.X compatible. Also, Artisan in no way replaces your testing library, but helps to craft better data to test with. 

### Disclaimer
Artisan is very much a Work In Progress. It will likely change. I am more than happy to accept Pull Requests, complaints, or general criticisms. Feel free to submit them on the GitHub repo.


### References
* [Artisan Github Repo](http://github.com/kmwhite/artisan)
* [Artisan on PyPI](https://pypi.python.org/pypi/artisan)
