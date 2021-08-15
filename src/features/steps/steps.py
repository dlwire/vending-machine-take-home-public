from behave import given, when, then, use_step_matcher
from nose import tools
from coins import ONE_DOLLAR_COIN


use_step_matcher("parse")


@given('I have $1 credit in the machine')
def one_dollar_credit(context):
    context.vending_machine.insertCoin(ONE_DOLLAR_COIN)


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
