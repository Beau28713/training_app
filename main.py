import typer
import csv
import pandas as pd

from datetime import date

today_date = date.today()

app = typer.Typer()


@app.command()
def rep_max(weight: float, reps: int):

    brycki = weight * (36 / (37 - reps))

    epley = weight * (1 + (0.0333 * reps))

    oConner = weight * (1 + (0.025 * reps))

    print(f"Weight Entered = {weight}\nReps Entered = {reps}")
    print("-----------------------------------")
    print("One rep Maxes are")
    print(f"Brycki = {brycki:.2f}\nEpley = {epley:.2f}\nOConner = {oConner:.2f}\n")

@app.command()
def calories_burned_per_min(mets_value: float, kg: float):
    """
    Takes in a MET value and body weight in KG's. Calculates how many 
    calories burned in 15, 30, and 60 mins.
    METS is a value representing how hard you are training during that time frame
    https://marathonhandbook.com/what-are-mets/
    """
    calories_burned = (mets_value * 3.5 * kg) / 200

    print(f"\nCalories burned per minute: {calories_burned}\n")
    print(f"Calories burned per 15 minutes: {calories_burned*15}\n")
    print(f"Calories burned per 30 minute: {calories_burned*30}\n")
    print(f"Calories burned per 1 hour: {calories_burned*60}\n")


@app.command()
def calories(calories: str, time: str):
    with open(f"{today_date}_calories.csv", "a", newline="") as file:
        entered_calories = csv.writer(file)
        entered_calories.writerow([time, calories])


@app.command()
def get_day_data(requested_date: str):
    total_calories = pd.read_csv(f"{requested_date}_calories.csv")

    print(total_calories.to_string())


@app.command()
def get_total_calories():
    total_calories = 0

    with open(f"{today_date}_calories.csv", "r", newline="") as file:
        heading = next(file)
        reader = csv.reader(file)

        for row in reader:
            total_calories += int((row[1]))

    print(f"Total Caolories = {total_calories}")


if __name__ == "__main__":
    app()
