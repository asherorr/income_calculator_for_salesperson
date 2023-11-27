import locale


locale.setlocale(locale.LC_ALL, '')


def compensation_generator(annual_base_salary, commission_percentage, list_of_deals_by_revenue, state_tax, federal_tax):
    commission_earned_counter = 0
    for deal in list_of_deals_by_revenue:
        earnings = deal * commission_percentage
        commission_earned_counter += earnings
    ote_before_tax = (annual_base_salary/12) + commission_earned_counter
    ote_after_tax = ote_before_tax - (ote_before_tax * (state_tax + federal_tax))
    print(f'You earned: {locale.currency(ote_after_tax, grouping=True)} this month.')


compensation_generator(65000, .03, [38000, 42000, 55000, 20000, 34000], .057, .22)
