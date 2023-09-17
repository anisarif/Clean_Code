def disabilityAmount(seniority: int, monthsDisabled: int, isPartTime: bool, age: int, disabilityPercentage: int, income: int, insuranceType: str):
    """Calculates the amount of disability benefits that an individual is eligible for.
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type.
    """
    # Define the eligibility conditions
    eligibility = (
        seniority >= 2
        and monthsDisabled <= 12
        and not isPartTime
        and age >= 62
        and disabilityPercentage >= 60
        and income <= 40000
        and insuranceType == "disability"
    )
    
    # If eligible, calculate the benefit amount based on a formula
    if eligibility:
        benefitAmount = (income * disabilityPercentage) / 100
        return benefitAmount

    return 0