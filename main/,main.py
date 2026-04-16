# 37. Fitness kaloriya kuzatuvchisi

class FitnessTracker:
    def __init__(self, exercise_type, duration_minutes, calories_per_minute):
        self.exercise_type = exercise_type
        self.duration = duration_minutes          # daqiqa
        self.cal_per_min = calories_per_minute    # kcal / daqiqa

    def total_calories(self):
        """Sarflangan kaloriya = vaqt × daqiqadagi sarf"""
        return self.duration * self.cal_per_min

    def __str__(self):
        kcal = self.total_calories()
        return f"{self.exercise_type:14} | {self.duration:3} daq | {self.cal_per_min:5.1f} kcal/min | {kcal:6.1f} kcal"


# -----------------------------------------------
# Voris sinflar (emoji va chiroyli format bilan)
# -----------------------------------------------

class RunningTracker(FitnessTracker):
    def __str__(self):
        kcal = self.total_calories()
        return f"🏃‍♂️ {self.exercise_type:12} → {self.duration:3} daq | {kcal:5.1f} kcal"


class SwimmingTracker(FitnessTracker):
    def __str__(self):
        kcal = self.total_calories()
        return f"🏊 {self.exercise_type:12} → {self.duration:3} daq | {kcal:5.1f} kcal"


# --------------------------------------------------
# Kunlik / mashq natijalarini chiqarish
# --------------------------------------------------

def show_fitness_calories(exercises):
    print("\n" + "═" * 70)
    print("     FITNESS KALORIYA KUZATUVCHISI — SARF HISOBI     ".center(70))
    print("═" * 70)
    print("Mashq turi          Vaqt (daq)   Sarflangan kaloriya")
    print("─" * 70)

    total_kcal = 0

    for ex in exercises:
        print(ex)
        total_kcal += ex.total_calories()

    print("─" * 70)
    print(f"JAMI SARFLANGAN KALORIYA:                        {total_kcal:7.1f} kcal")
    print("═" * 70 + "\n")


# Test ma'lumotlari
mashqlar = [
    RunningTracker("Yugurish (o'rtacha tezlik)", 38, 9.8),
    SwimmingTracker("Suzish (erkin uslub)", 25, 11.5),
    RunningTracker("Interval yugurish", 22, 13.2),
    SwimmingTracker("Suvda yurish", 40, 6.8),
]

show_fitness_calories(mashqlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol mashqlaringiz:\n")
misol_mashqlar = [
    RunningTracker("Yugurish", 30, 10),
    SwimmingTracker("Suzish", 20, 12),
]

show_fitness_calories(misol_mashqlar)
