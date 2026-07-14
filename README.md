# BMI Calculator

A simple **BMI (Body Mass Index) Calculator** developed using **Python** and **Tkinter** as part of the **Oasis Infobyte Python Programming Internship**.

## Features

- GUI built using Tkinter
- User enters Name, Weight, and Height
- Calculates BMI
- Displays BMI Category
- Gives Health Advice
- Input Validation
- Save BMI records to CSV file
- Clear all input fields
- Exit application

## Technologies Used

- Python 3
- Tkinter
- CSV
- OS
- Datetime

## Project Structure

```
Python-Task2-BMICalculator/
│
├── bmi_calculator.py
├── README.md
└── bmi_records.csv
```

## BMI Formula

```
BMI = Weight (kg) / Height² (m²)
```

## BMI Categories

| BMI Range | Category |
|-----------|----------|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and Above | Obese |

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this project.
3. Open the project folder.
4. Run:

```bash
python bmi_calculator.py
```

## Output

The application will:

- Calculate BMI
- Show BMI Category
- Display Health Advice
- Save the record in `bmi_records.csv`

## Future Improvements

- View BMI History
- BMI Trend Graph
- SQLite Database
- Dark Mode
- Export Report as PDF

## Author

**Prithviraj Ghosh**

Python Programming Intern

## License

This project is created for educational purposes as part of the **Oasis Infobyte Python Programming Internship**.
