


def format_locators(locator_a, num):
    method, locator = locator_a
    locator = locator.format(num)
    return method, locator

