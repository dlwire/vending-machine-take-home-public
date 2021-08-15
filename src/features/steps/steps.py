from behave import *
from nose import tools

@when('I walk up to the machine')
def step_impl(context):
    pass

@then('the display says "INSERT COIN"')
def step_impl(context):
    tools.eq_(context.vending_machine.checkDisplay(), 'INSERT COIN')
