.. currentmodule:: skinport

API Reference
===============

Client
-------

.. autoclass:: Client
    :members:

Item
-----

.. autoclass:: Item
    :members:

ItemWithSales
--------------

.. autoclass:: ItemWithSales
    :members:

ItemOutOfStock
---------------

.. autoclass:: ItemOutOfStock
    :members:

LastXDays
----------

.. autoclass:: LastXDays
    :members:

Transaction
------------

.. autoclass:: Transaction
    :members:

SaleFeed
---------

.. autoclass:: SaleFeed
    :members:

.. autoclass:: SaleFeedSale
    :members:

.. autoclass:: Tag
    :members:

Color
------

.. autoclass:: Color
    :members:

Enumerations
-------------

The API provides some enumerations for certain types of strings to avoid the API
from being stringly typed in case the strings change in the future.

All enumerations are subclasses of :class:`enum.Enum`.

.. class:: Currency

    Specifies the currency of a sale.

    .. attribute:: aud

        Australian dollar.
    .. attribute:: brl

        Brazilian real.
    .. attribute:: cad
    
        Canadian dollar.
    .. attribute:: chf
    
        Swiss franc.
    .. attribute:: cny
        
        Chinese yuan.
    .. attribute:: czk
            
        Czech koruna.
    .. attribute:: dkk
                
        Danish krone.
    .. attribute:: eur
    
        Euro.
    .. attribute:: gbp
        
        British pound.
    .. attribute:: hrk
        
        Croatian kuna.
    .. attribute:: nok
            
        Norwegian krone.
    .. attribute:: pln
                
        Polish zloty.
    .. attribute:: rub
                
        Russian rouble.
    .. attribute:: sek
                    
        Swedish krona.
    .. attribute:: try_
                    
        Turkish lira.
    .. attribute:: usd
                        
        United States dollar.

.. class:: AppID

    Specifies the id of a game.

    .. attribute:: csgo
        
        Counter-Strike: Global Offensive.
    .. attribute:: dota2
            
        Dota 2.
    .. attribute:: rust
                    
        Rust.
    .. attribute:: tf2
                        
        Team Fortress 2.

.. class:: Locale

    Specifies the locale of a sale. This affects the name of the item.

    .. attribute:: en
            
        English.
    .. attribute:: de
                    
        German.
    .. attribute:: ru
                                
        Russian.
    .. attribute:: fr

        French.
    .. attribute:: zh

        Chinese.
    .. attribute:: nl

        Dutch.
    .. attribute:: fi

        Finnish.
    .. attribute:: es

        Spanish.
    .. attribute:: tr

        Turkish.

.. class:: SaleType

    Specifies the type of a sale.

    .. attribute:: public
    
        Public sale.
    .. attribute:: private
            
        Private sale.

Exceptions
------------

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

.. autoexception:: InternalServerError
