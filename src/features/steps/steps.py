from behave import given, when, then, use_step_matcher
from nose import tools
from changeMaker import makeChange
from coins import ONE_DOLLAR_COIN


use_step_matcher("parse")


@given('I insert {amount} cents in the coin slot')
def one_dollar_credit(context, amount: str):
    for coin in makeChange(int(amount)):
        context.vending_machine.insertCoin(coin)


@given('I have purchased a {product}')
def purchased_a_cola(context, product: str):
    context.vending_machine.insertCoin(ONE_DOLLAR_COIN)
    context.vending_machine.order(product)
    context.vending_machine.retrieveProduct()


@when('I order {product}')
def order_a_cola(context, product: str):
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
    tools.eq_(context.vending_machine.retrieveChange(), makeChange(int(amount)))
