from behave import given, when, then, use_step_matcher
from nose import tools
from changeMaker import makeChange
from coins import ONE_DOLLAR_COIN, QUARTER_DOLLAR_COIN, DIME_COIN, NICKEL_COIN


use_step_matcher("parse")


@given('I have {amount} cents credit in the machine')
def one_dollar_credit(context, amount: str):
    for coin in makeChange(int(amount)):
        context.vending_machine.insertCoin(coin)


@given('I have purchased a cola')
def purchased_a_cola(context):
    context.vending_machine.insertCoin(ONE_DOLLAR_COIN)
    context.vending_machine.orderCola()
    context.vending_machine.retrieveProduct()


@when('I order a cola')
def order_a_cola(context):
    context.vending_machine.orderCola()


@when('I walk up to the machine')
def walk_up_to_the_machine(context):
    pass


@then('the display says "{expected}"')
def the_display_says(context, expected: str):
    tools.eq_(context.vending_machine.checkDisplay(), expected)


@then('I receive my cola')
def receive_my(context):
    tools.eq_(context.vending_machine.retrieveProduct(), 'cola')


@then('there is no product to get')
def there_is_no_product(context):
    tools.eq_(context.vending_machine.retrieveProduct(), '')


@then('I receive no change')
def receive_no_change(context):
    tools.eq_(context.vending_machine.retrieveChange(), [])


@then('I receive {amount} cents change')
def receive_05_change(context, amount: str):
    tools.eq_(context.vending_machine.retrieveChange(), makeChange(int(amount)))
