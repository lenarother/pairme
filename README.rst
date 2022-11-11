======
pairme
======


Facilitate mob programming

* pull random pairs (each person appears 2 times, once as a driver and once as a navigator)
* reminds to change pair after some time interval (default 15 minutes)


Usage
-----


.. code-block:: shell

    $ git clone git@github.com:lenarother/pairme.git
    $ cd pairme
    $ python -m venv venv
    $ pip install -r requirements_dev.txt

    $ Configure mob session
    $ src/pairme/cli.py --mobteam John,Jane,Bob
    $ src/pairme/cli.py --mobtime 600

    $ Start mob session
    $ src/pairme/cli.py


TODO
----

* test properly
* proper config path handling
* move README.rst to md
* option to just draw pairs
* sound config
* make command line tool (like e.g. black)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
