.. currentmodule:: skinport

API Reference
===============

Client
~~~~~~~

.. autoclass:: Client
    :members:

Item
~~~~~

.. autoclass:: Item
    :members:

ItemWithSales
~~~~~~~~~~~~~~

.. autoclass:: ItemWithSales
    :members:

ItemOutOfStock
~~~~~~~~~~~~~~~

.. autoclass:: ItemOutOfStock
    :members:

Sale
~~~~~

.. autoclass:: Sale
    :members:

LastXDays
~~~~~~~~~~

.. autoclass:: LastXDays
    :members:

Transaction
~~~~~~~~~~~~

.. autoclass:: Transaction
    :members:

SaleFeed
~~~~~~~~~

.. autoclass:: SaleFeed
    :members:

.. autoclass:: SaleFeedSale
    :members:

.. autoclass:: Tag
    :members:


Exceptions
~~~~~~~~~~~~

The following exceptions are thrown by the library.

.. autoexception:: SkinportException

.. autoexception:: HTTPException
    :members:

.. autoexception:: ParamRequired

.. autoexception:: ValidationError

.. autoexception:: InvalidRequest

.. autoexception:: NotFound

.. autoexception:: AuthenticationError

.. autoexception:: InsufficientFunds

.. autoexception:: InvalidScope

.. autoexception:: Forbidden

.. autoexception:: InternalServerError
