# Αυτό το αρχείο (Custom Module) περιέχει τη μοντελοποίηση των φοιτητών με βάση τον Αντικειμενοστρεφή Προγραμματισμό (OOP).

class Student:
    def __init__(self, name, student_id, grade):
        # Ιδιότητες: ονοματεπώνυμο, Α.Μ., βαθμός[cite: 2]
        self.name = name
        self.student_id = student_id
        self.grade = float(grade)

    def is_passing(self):
        # Ελέγχει αν ο βαθμός είναι μεγαλύτερος του 5[cite: 2]
        return self.grade > 5

    def to_dict(self):
        # Μετατρέπει τις ιδιότητες σε λεξικό για JSON serialization[cite: 2]
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grade": self.grade
        }


class GraduateStudent(Student):
    # Κληρονομεί από την Student[cite: 2]
    def __init__(self, name, student_id, grade, thesis_name):
        # Κάνει override τον constructor χρησιμοποιώντας τη συνάρτηση super()[cite: 2]
        super().__init__(name, student_id, grade)
        # Διαθέτει επιπλέον ιδιότητα: θέμα διπλωματικής[cite: 2]
        self.thesis_name = thesis_name

    def to_dict(self):
        # Κάνει override τη μέθοδο to_dict() χρησιμοποιώντας τη super()[cite: 2]
        data = super().to_dict()
        data["thesis_name"] = self.thesis_name
        return data