class Employee:
    def __init__(self, is_deceased=False, is_separated=False, is_retired=False):
        self.is_deceased = is_deceased
        self.is_separated = is_separated
        self.is_retired = is_retired

    def get_pay_amount(self):
        if self.is_deceased:
            return self.calculate_dead_amount()
        elif self.is_separated:
            return self.calculate_separated_amount()
        elif self.is_retired:
            return self.calculate_retired_amount()
        else:
            return self.calculate_normal_pay_amount()

    def calculate_dead_amount(self):
        # Imagine there is code here for calculating the pay amount for a deceased employee
        return 0

    def calculate_separated_amount(self):
        # Imagine there is code here for calculating the pay amount for a separated employee
        return 0

    def calculate_retired_amount(self):
        # Imagine there is code here for calculating the pay amount for a retired employee
        return 0

    def calculate_normal_pay_amount(self):
        # Imagine there is code here for calculating the normal pay amount for an active employee
        return 0
