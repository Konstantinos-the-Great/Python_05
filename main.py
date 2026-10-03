# Το κύριο πρόγραμμα διαχειρίζεται το μενού, τις αυτόνομες συναρτήσεις ελέγχου, την αποθήκευση/ανάγνωση αρχείων JSON και την ασφαλή διαχείριση σφαλμάτων.

import json
from models import Student, GraduateStudent

def add_student():
    # Αυτόνομη συνάρτηση για την καταχώρηση[cite: 3]
    name = input("Όνοματεπώνυμο: ")
    student_id = input("Α.Μ.: ")
    
    while True:
        try:
            # Έλεγχος ValueError αν ο χρήστης εισάγει κείμενο αντί για αριθμό στο βαθμό[cite: 3]
            grade = float(input("Βαθμός: "))
            break
        except ValueError:
            print("Σφάλμα: Παρακαλώ εισάγετε αριθμητική τιμή για τον βαθμό.")
            
    is_grad = input("Είναι μεταπτυχιακός φοιτητής; (ν/ο): ")
    
    if is_grad.lower() == 'ν':
        thesis_name = input("Θέμα διπλωματικής: ")
        student = GraduateStudent(name, student_id, grade, thesis_name)
    else:
        student = Student(name, student_id, grade)
        
    # Ασφαλές άνοιγμα αρχείου με πρόληψη FileNotFoundError[cite: 3]
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []
        
    students.append(student.to_dict())
    
    # Εγγραφή στο αρχείο students.json[cite: 3]
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
        
    print("Ο φοιτητής καταχωρήθηκε επιτυχώς!")


def view_students():
    # Αυτόνομη συνάρτηση για την προβολή[cite: 3]
    try:
        # Ανάγνωση από το αρχείο students.json[cite: 3]
        with open("students.json", "r", encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        print("Δεν βρέθηκε αρχείο δεδομένων (students.json).")
        return
        
    if not students:
        print("Η λίστα φοιτητών είναι κενή.")
        return
        
    total_grade = 0
    print("\n--- Λίστα Φοιτητών ---")
    
    for s in students:
        # Επαναδημιουργία αντικειμένων για να κληθεί σωστά η is_passing()
        if "thesis_name" in s:
            obj = GraduateStudent(s["name"], s["student_id"], s["grade"], s["thesis_name"])
            thesis_info = f" | Θέμα: {obj.thesis_name}"
        else:
            obj = Student(s["name"], s["student_id"], s["grade"])
            thesis_info = ""
            
        status = "Προβιβάστηκε" if obj.is_passing() else "Απορρίφθηκε"
        print(f"Α.Μ.: {obj.student_id} | {obj.name} | Βαθμός: {obj.grade} ({status}){thesis_info}")
        
        total_grade += obj.grade
        
    # Υπολογισμός μέσου όρου τμήματος[cite: 1]
    avg = total_grade / len(students)
    print(f"\nΜέσος Όρος Τμήματος: {avg:.2f}")


def main():
    # Χρήση επαναληπτικού βρόχου (while True) για να παραμένει η εφαρμογή ανοιχτή[cite: 1]
    while True:
        # Εμφάνιση επιλογών στο χρήστη με την input()[cite: 1]
        print("\n=== Ηλεκτρονική Γραμματεία ===")
        print("1: Καταχώρηση νέου φοιτητή & βαθμολογίας")
        print("2: Προβολή όλων των φοιτητών & υπολογισμός μέσου όρου")
        print("3: Τερματισμός / Έξοδος από την εφαρμογή")
        
        choice = input("Επιλέξτε (1-3): ")
        
        # Κλήση συναρτήσεων ανάλογα με την επιλογή στο μενού[cite: 3]
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Τερματισμός εφαρμογής...")
            break  # Τερματισμός / Έξοδος από την εφαρμογή (break)[cite: 1]
        else:
            print("Λάθος επιλογή, παρακαλώ προσπαθήστε ξανά.")


if __name__ == "__main__":
    main()