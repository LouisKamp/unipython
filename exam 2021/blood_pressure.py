def blood_pressure(systolic: int, diastolic: int):
    if systolic < 90 or diastolic < 60:
        category = "Low"
    if systolic >= 90 or diastolic >= 60:
        category = "Normal"
    if systolic >= 120 or diastolic >= 80:
        category = "Prehigh"
    if systolic >= 140 or diastolic >= 90:
        category = "Stage 1 high"
    if systolic >= 160 or diastolic >= 100:
        category = "Stage 2 high"

    return category
