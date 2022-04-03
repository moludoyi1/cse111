"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.

"""


age  = int(input("Please enter your age: "))
print()


max_rate = 220 - age
min = 0.65 * max_rate
max = 0.85 * max_rate


print("When you exercise to strengthen your heart, you should")
print(f"keep yout gear rate between {min} and {max} beats per minute.")
print()