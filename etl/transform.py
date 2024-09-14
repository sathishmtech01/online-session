def check_temperature_and_humidity(temperature, humidity):
    """

    :param temperature: in Celsius
    :param humidity: in percentage
    :return:
    """
    # Temperature conditions
    if temperature < 0:
        temp_condition = 'Freezing'
    elif 0 <= temperature < 15:
        temp_condition = 'Cold'
    elif 15 <= temperature < 25:
        temp_condition = 'Comfortable'
    else:
        temp_condition = 'Hot'

    # Humidity conditions
    if humidity < 30:
        humidity_condition = 'Dry'
    elif 30 <= humidity <= 60:
        humidity_condition = 'Comfortable'
    else:
        humidity_condition = 'Humid'

    # Combine temperature and humidity into one word
    combined_condition = temp_condition +" "+ humidity_condition
    return combined_condition

# Example usage
temperature = 20  # in Celsius
humidity = 65     # in percentage

# result = check_temperature_and_humidity(temperature, humidity)
# print(result)
