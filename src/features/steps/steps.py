from behave import when, then
from nose import tools


@when('I walk up to the machine')
def walk_up_to_the_machine(context):
    pass


@then('the display says "INSERT COIN"')
def the_display_says(context):
    tools.eq_(context.vending_machine.checkDisplay(), 'INSERT COIN')
