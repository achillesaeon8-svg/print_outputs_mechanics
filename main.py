from print_format_configuration import PrintFormats

given_format = PrintFormats()

print(f'The first given format successfully produced the required output:')
first_format = given_format.given_first_format()

print(f'\nThe second given format did not produced the required output:')
given_format.given_second_format()

print(f'\nThe third given format successfully produced the required output:')
given_format.given_third_format()

print(f'\nThe fourth given format successfully produced the required output:')
given_format.given_fourth_format()