import csv
import random

CSV_FILENAME = "mi_kviz_teljes_12het_220kerdes.csv"  # A letöltött CSV fájl neve

def load_questions(csv_filename):
    """
    Betölti a kérdéseket a CSV fájlból.
    Feltételezi az oszlopokat: 'ID', 'Téma', 'Kérdés', 'A', 'B', 'C', 'D', 'Helyes'
    """
    questions = []
    with open(csv_filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row)
    return questions

def ask_questions(questions, num=20):
    """
    Véletlenszerűen lekérdez num darab kérdést.
    Visszaadja a helyes válaszok számát.
    """
    selected = random.sample(questions, num)
    score = 0
    for i, q in enumerate(selected, 1):
        print(f"\n{i}. Kérdés {q['ID']} – {q['Téma']}:")
        print(q['Kérdés'])
        print(f"A) {q['A']}")
        print(f"B) {q['B']}")
        print(f"C) {q['C']}")
        print(f"D) {q['D']}")
        answer = input("Válaszod (A/B/C/D): ").strip().upper()
        if answer == q['Helyes'].upper():
            print("Helyes válasz!")
            score += 1
        else:
            print(f"Helytelen. A helyes válasz: {q['Helyes']}")
    return score

def main():
    questions = load_questions(CSV_FILENAME)
    print(f"\n--- Teszt: 20 véletlenszerű kérdés (CSV: {CSV_FILENAME}) ---")
    score = ask_questions(questions, num=20)
    print(f"\nAz összpontszámod: {score} / 20")

if __name__ == "__main__":
    main()
