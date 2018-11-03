def convertToInches(ft, inches):
    a = ft * 12
    return a + inches


def maleBMR(weight, feet, inches, age):
    bmr = 66 + (63 * weight) + (12.9 * convertToInches(feet, inches)) - (6.8 * age)
    return bmr


def femaleBMR(weight, feet, inches, age):
    bmr = 655 + (4.3 * weight) + (12.9 * convertToInches(feet, inches)) - (4.7 * age)
    return bmr


def calNeedsMaint(bmr, activityLev):
    if activityLev == 'sedentary':
        bmr = bmr * 1.2
    elif activityLev == 'lightly active':
        bmr = bmr * 1.375
    elif activityLev == 'moderately active':
        bmr = bmr * 1.55
    elif activityLev == 'very active':
        bmr = bmr * 1.725
    elif activityLev == 'constantly active':
        bmr = bmr * 1.9
    return bmr

