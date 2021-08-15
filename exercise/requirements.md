Vending Machine Take Home
====================

In this exercise you will build the brains of a vending machine.  It will accept money, make change, maintain
inventory, and dispense products.  All the things that you might expect a vending machine to accomplish.

The point of this exercise is to provide a larger than trivial exercise that can be used to practice TDD.  A significant
portion of the effort will be in determining what tests should be written and, more importantly, written next.

Features
========

Select Product
--------------

_As a vendor_
_I want customers to select products_
_So that I can give them products_

There are three products: cola, chips, and candy.  When the respective button is pressed, the product is dispensed and the machine displays THANK YOU.

Accept Coins
------------

_As a vendor_
_I want a vending machine that accepts coins_
_So that I can collect money from the customer_

The vending machine will accept valid coins (nickels, dimes, and quarters) and reject invalid ones (pennies).  When a
valid coin is inserted the amount of the coin will be added to the current amount and the display will be updated.
When there are no coins inserted, the machine displays INSERT COIN.  Rejected coins are placed in the coin return.

NOTE: The temptation here will be to create Coin objects that know their value.  However, this is not how a real
  vending machine works.  Instead, it identifies coins by their weight and size and then assigns a value to what
  was inserted.  You will need to do something similar.  This can be simulated using strings, constants, enums,
  symbols, or something of that nature.

Pay for Product
--------------

_As a vendor_
_I want customers to pay for products_
_So that I can make money from giving them products_

There are three products: cola for $1.00, chips for $0.50, and candy for $0.65.  When the respective button is pressed
and enough money has been inserted, the product is dispensed and the machine displays THANK YOU.  If the display is
checked again, it will display INSERT COIN and the current amount will be set to $0.00.  If there is not enough money
inserted then the machine displays PRICE and the price of the item and subsequent checks of the display will display
either INSERT COIN or the current amount as appropriate.

Make Change
-----------

_As a vendor_
_I want customers to receive correct change_
_So that they will use the vending machine again_

When a product is selected that costs less than the amount of money in the machine, then the remaining amount is placed
in the coin return.
