#The constant rates used in the calculations are defined here
RATE_75 = 4.00                  #Rate for first 75 cubic meters of gas used
RATE_125 = 1.28                 #Rate for next 125 cubic meters of gas used
RATE_250 = 0.59                 #Rate for next 250 cubic meters of gas used
RATE_450 = 0.13                 #Rate for gas consumption above 450 cubic meters

#prev_gas = previous month's gas meter reading, cur_gas = current month's gas meter reading
prev_gas = input("Enter Last Month's Gas Meter Reading: ")
cur_gas = input("Enter Current Gas Meter Reading: ")

cost = 0

#Cannot have negative gas meter readings
if prev_gas < 0 or cur_gas < 0:

    print "\nInvalid Input. Gas Meter Readings Must Be Positive.\n\n"

else:

    #The monthly gas consumption (gas_used) is calculated taking the difference between the current and previous months' gas meter readings
    gas_used = cur_gas - prev_gas

    #Cannot have a negative gas consumption (current reading must be greater than previous reading)
    if gas_used < 0:

        print "\nERROR: There Must Be A Misreading. Check Gas Meter Readings Again.\n\n"

    else:

        #For the first 75 cubic meters of gas consumed, the cost is the quantity of gas used times the rate for the first 75 cubic meters
        if gas_used >= 0 and gas_used <= 75:

            cost = gas_used*RATE_75

        #The next 125 cubic meters of gas consumed after the first 75 is a quantity between 75 and 200
        elif gas_used > 75 and gas_used <= 200:

            cost = 75*RATE_75 + (gas_used - 75)*RATE_125

        #The next 250 cubic meters of gas consumed after the first 200 is a quantity between 200 and 450
        elif gas_used > 200 and gas_used <= 450:

            cost = 75*RATE_75 + 125*RATE_125 + (gas_used - 200)*RATE_250

        #Any amount of gas consumed above 450 cubic meters is split into the four rate ranges and the cost is calculated accordingly
        else:

            cost = 75*RATE_75 + 125*RATE_125 + 250*RATE_250 + (gas_used - 450)*RATE_450

        print "\n\nCustomer Bill"
        print "============="
        print "Gas Consumed: ", gas_used, "cubic meters"
        print "%0s%0.2f" % ("Cost: $", cost)
        print "\n\n"
