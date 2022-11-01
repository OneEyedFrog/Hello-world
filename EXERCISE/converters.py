def main():
    print("This is a montly loan payment calculator")
    print("")

    apr = float(input("type your apr"))
    principal = float(input("type your principal"))
    years = int(input("type loan years: "))

    monthly_interest_rate = apr / 12
    total_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1 + monthly_interest_rate) ** (-total_months))
    print("the monthly payment of this loan is:%.3f" % monthly_payment)

main()


