.. quickstart:

Quickstart
==========


.. note:: All code starting with a ``$`` is meant to run on your terminal.
    All code starting with a ``>>>`` is meant to run in a python interpreter,
    like `ipython <https://pypi.org/project/ipython/>`_.

Installation
------------

Paloma SDK can be installed (preferably in a :ref:`virtualenv <setup_environment>`)
using ``pip`` as follows:

.. code-block:: shell

   $ pip install paloma-sdk


.. note:: If you run into problems during installation, you might have a
    broken environment. See the troubleshooting guide to :ref:`setting up a
    clean environment <setup_environment>`.


Using Paloma SDK
---------------

In order to interact with the Paloma blockchain, you'll need a connection to a Paloma node.
This can be done through setting up an LCDClient:


.. code-block:: python

    from paloma_sdk.client.lcd import LCDClient

    paloma = LCDClient(chain_id="columbus-5", url="https://lcd.paloma.dev")
    print(paloma.tendermint.node_info())


Getting Blockchain Info
-----------------------

It's time to start using Paloma SDK! Once properly configured, the ``LCDClient`` instance will allow you
to interact with the Paloma blockchain. Try getting the latest block height:

.. code-block:: python

    >>> paloma.tendermint.block_info()['block']['header']['height']
    '1687543'

Paloma SDK can help you read block data, sign and send transactions, deploy and interact with contracts,
and a number of other features.
