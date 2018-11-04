def convertToInches(ft, inches):
    a = ft * 12
    return a + inches


def maleBMR(weight, feet, inches, age):
    bmr = 66 + (6.3 * weight) + (12.7 * convertToInches(feet, inches)) - (6.8 * age)
    return bmr


def femaleBMR(weight, feet, inches, age):
    bmr = 655 + (4.3 * weight) + (4.7 * convertToInches(feet, inches)) - (4.7 * age)
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
    if bmr < 1200 :
        return 1200
    else:
        return bmr


def calNeedsLoss(bmr, activityLev):
    surplus = calNeedsMaint(bmr, activityLev) - 250
    if surplus < 1200:
        return 1200
    else:
        return surplus


def calNeedsGain(bmr, activityLev):
    deficit = calNeedsMaint(bmr, activityLev) + 250
    if deficit < 1200:
        return 1200
    else:
        return deficit



def person(gender,goal, weight, feet, inches, age, activityLev):
    nutrition_dict = {}
    suggested_cal_intake = 0
    fat_intake = 65
    sat_fat_intake = 20
    cholesterol_intake = 300
    sodium_intake = 2400
    carb_intake = 300
    protein_intake = 50

    if gender == 'female':
        base_bmr = femaleBMR(weight, feet, inches, age)
    elif gender == 'male':
        base_bmr = maleBMR(weight, feet, inches, age)

    if goal == 'loss':
        suggested_cal_intake = calNeedsLoss(base_bmr, activityLev)
    if goal == 'gain':
        suggested_cal_intake = calNeedsGain(base_bmr, activityLev)
    if goal == 'maintain':
        suggested_cal_intake = calNeedsMaint(base_bmr, activityLev)

    suggested_cal_intake /= 100
    suggested_cal_intake = 100 * int(round(suggested_cal_intake))

    nutrition_dict["calories"] = suggested_cal_intake
    nutrition_dict["fat"] = fat_intake
    nutrition_dict["saturatedFat"] = sat_fat_intake
    nutrition_dict["cholesterol"] = cholesterol_intake
    nutrition_dict["sodium"] = sodium_intake
    nutrition_dict["carbohydrates"] = carb_intake
    nutrition_dict["protein"] = protein_intake

    return nutrition_dict
