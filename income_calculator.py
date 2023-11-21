import locale


locale.setlocale(locale.LC_ALL, '')


def compensation_generator(annual_base_salary, commission_percentage, list_of_deals_by_revenue):
    commission_earned_counter = 0
    for deal in list_of_deals_by_revenue:
        earnings = deal * commission_percentage
        commission_earned_counter += earnings
    ote = (annual_base_salary/12) + commission_earned_counter
    print(f'You earned: {locale.currency(ote, grouping=True)} this month.')


compensation_generator(60000, .03, [38000, 42000, 55000, 20000, 34000])
