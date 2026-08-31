class PrintFormats:

    def __init__(self):
        self.text_1 = 'hello'
        self.text_2 = 'world'

    def given_first_format(self):
        print(self.text_1, end='')  
        print(self.text_2)

    def given_second_format(self):
        print(self.text_1, self.text_2)

    def given_third_format(self):
        print(self.text_1, self.text_2, sep='')

    def given_fourth_format(self):
        print(self.text_1 + self.text_2)