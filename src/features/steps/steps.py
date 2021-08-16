from behave import given, when, then, use_step_matcher
from nose import tools
from changeMaker import makeChange
from coins import ONE_DOLLAR_COIN


use_step_matcher("parse")


PENNY = (
    'Copper Plated Zinc',
    2.500,
    19.05,
    1.52,
)


@given('I insert {amount} cents in the coin slot')
def insert_coints(context, amount: str):
    amount = int(amount)

    coins, value = makeChange(amount)
    coins.extend([PENNY] * (amount - value))

    for coin in coins:
        context.vending_machine.insertCoin(coin)


@given('I have purchased a {product}')
def purchased_a_cola(context, product: str):
    context.vending_machine.insertCoin(ONE_DOLLAR_COIN)
    context.vending_machine.order(product)
    context.vending_machine.retrieveProduct()


@when('I order {product}')
def order_product(context, product: str):
    context.vending_machine.order(product)


@when('I walk up to the machine')
def walk_up_to_the_machine(context):
    pass


@then('the display says "{expected}"')
def the_display_says(context, expected: str):
    tools.eq_(context.vending_machine.checkDisplay(), expected)


@then('I receive my {product}')
def receive_my(context, product: str):
    tools.eq_(context.vending_machine.retrieveProduct(), product)


@then('there is no product to get')
def there_is_no_product(context):
    tools.eq_(context.vending_machine.retrieveProduct(), '')


@then('I receive no change')
def receive_no_change(context):
    tools.eq_(context.vending_machine.retrieveChange(), [])


@then('I receive {amount} cents change')
def receive_05_change(context, amount: str):
    amount = int(amount)

    coins, value = makeChange(amount)
    if value < amount:
        coins = ([PENNY] * (amount - value)) + coins

    tools.eq_(context.vending_machine.retrieveChange(), coins)
