import typer
import csv
import pandas as pd

from datetime import date

today_date = date.today()

app = typer.Typer()


@app.command()
def rep_max(weight: int, reps: int):
    weight = int(weight)
    reps = int(reps)

    brycki = weight * (36 / (37 - reps))

    epley = weight * (1 + (0.0333 * reps))

    oConner = weight * (1 + (0.025 * reps))

    print(f"Weight Entered = {weight}\nReps Entered = {reps}")
    print("-----------------------------------")
    print("One rep Maxes are")
    print(f"Brycki = {brycki:.2f}\nEpley = {epley:.2f}\nOConner = {oConner:.2f}\n")


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
