def interest_rate():
    print("This is a monthly loan calculator")
    print("")

    principal =float(input("type the principal: "))
    apr = float(input("type your apr: "))
    years = int(input("type the amount of years: "))

    monthly_interest_rate = apr/1200
    amount_of_month = years * 12
    monthly_payment = principal * monthly_interest_rate /(1 - (1 + monthly_interest_rate) ** (-amount_of_month))

    print("the monthly payment for this loan is: %.2f" % monthly_payment)


interest_rate()
