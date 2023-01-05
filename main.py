from supporting_functions import discrete_distribution, random_route, route_length, write_to_file, calculate_delay_sum
from variables import cities_elements, transfer_probabilities, \
    transfer_elements, total_time, cities_probabilities

# Funkcja fitująca - wbudowana funkcja gaus
# Parametry:
# 1) NAME: Constant VALUE: 2.11578e+02
# 2) NAME: Mean VALUE: 9.51199e+02
# 3) NAME: Sigma VALUE: 6.07385e+02

if __name__ == '__main__':

    size = 5000
    for x in range(size):
        transfers = discrete_distribution(transfer_elements, transfer_probabilities)
        random_route(transfers, cities_elements, cities_probabilities)
        travel_time = route_length()
        delay_sum = calculate_delay_sum(transfers)
        total_time.append(travel_time + delay_sum)

    write_to_file(total_time)
