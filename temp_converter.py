TEMPERATURE_SCALE= {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K'
}

def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else: 
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32 ) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else: 
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value 
    else:
        return value


while True:
    # Promt the user for input
    print('Enter the input temperature value: ')
    value = float(input())
    print('Enter the input temperature scale (C, F, or K): ')
    input_scale = input().upper()
    print('Enter the output temperature scale (C, F, or K): ')
    output_scale = input().upper()

    # Convert the temperature and print the result
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

    # Prompt the user to continue or quit
    print('Enter q to quit, or any other key to continue: ')
    choice = input()
    if choice.lower() == 'q':
        break    

