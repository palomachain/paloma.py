Keys & Wallets
==============

A **Key** is an object that provides an abstraction for the agency of signing transactions.

Key (abstract)
--------------

Implementers of Keys meant for signing should override :meth:`Key.sign()<paloma_sdk.key.Key.sign>`
or :meth:`Key.create_signature()<paloma_sdk.key.key.Key.create_signature>` methods. More details are
available in :ref:`guides/custom_key`.

Some properties such as :meth:`acc_address<paloma_sdk.key.key.Key.acc_address>` and
:meth:`val_address<paloma_sdk.key.key.Key.val_address>` are provided.

.. automodule:: paloma_sdk.key.key
    :members:

RawKey
------

.. automodule:: paloma_sdk.key.raw
    :members:


MnemonicKey
-----------

.. automodule:: paloma_sdk.key.mnemonic
    :members:

Wallet
------

.. automodule:: paloma_sdk.client.lcd.wallet
    :members: