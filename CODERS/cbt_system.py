import mysql.connector as sql
class CBTSystem:

    def __init__(self, db_config):
        self.connection = sql.connect(**db_config)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        create_student_table_query = """
            CREATE TABLE IF NOT EXISTS student_table (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                First_name VARCHAR(30),
                Last_name VARCHAR(30),
                Address VARCHAR(100),
                Phone VARCHAR(11) UNIQUE,
                Username VARCHAR(30) UNIQUE,
                Password VARCHAR(30)
            )
        """
        create_result_table_query = """
            CREATE TABLE IF NOT EXISTS result_table (
                result_id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT(5),
                student_name VARCHAR(30),
                subject VARCHAR(25),
                score INT(3)
            )
        """
        create_cbt_table_query = """
            CREATE TABLE IF NOT EXISTS cbt (
                Subject VARCHAR(25),
                question_text TEXT,
                option_a VARCHAR(100),
                option_b VARCHAR(100),
                option_c VARCHAR(100),
                option_d VARCHAR(100),
                correct_answer VARCHAR(1)
            )
        """
        self.cursor.execute(create_student_table_query)
        self.cursor.execute(create_result_table_query)
        self.cursor.execute(create_cbt_table_query)
        self.connection.commit()

    def register_student(self):
        print("Student Registration")
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        address = input("Enter your address: ")

        while True:
            phone_number = input("Enter your phone number (11 digits): ")
            if len(phone_number) == 11 and phone_number.isdigit():
                if not self.phone_number_exists(phone_number):
                    break
                else:
                    print("Phone number already registered. Please enter a different one.")
            else:
                print("Invalid phone number format. Please enter an 11-digit number.")

        username = input("Enter your unique username: ")
        password = input("Enter your password: ")

        insert_query = """
            INSERT INTO student_table (First_name, Last_name, Address, Phone, Username, Password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (firstname, lastname, address, phone_number, username, password)

        try:
            self.cursor.execute(insert_query, values)
            self.connection.commit()
            print("Student registered successfully.")
        except sql.IntegrityError as e:
            if "1062 (23000)" in str(e):
                print("Error: This username is already registered.")
            else:
                print(f"Database error: {e}")
            self.connection.rollback()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def phone_number_exists(self, phone_number):
        check_query = "SELECT COUNT(*) FROM student_table WHERE Phone = %s"
        self.cursor.execute(check_query, (phone_number,))
        count = self.cursor.fetchone()[0]
        return count > 0

    def question_upload(self):
        print("Question Upload")
        question_details = []
        question_num = int(input("Enter the number of questions to set: "))
        for question in range(question_num):
            Subject = input("Enter the subject: ")[:25]  # Limit subject to 25 characters
            Question = input("Enter question: ")
            option_a = input("Enter the first option: ")
            option_b = input("Enter the second option: ")
            option_c = input("Enter the third option: ")
            option_d = input("Enter the fourth option: ")
            correct_option = input("Enter the correct option (A, B, C, or D): ").upper()

            question_tuple = (Subject, Question, option_a, option_b, option_c, option_d, correct_option)
            question_details.append(question_tuple)

        question_update = "INSERT INTO cbt (Subject, question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = question_details

        try:
            self.cursor.executemany(question_update, val)
            self.connection.commit()
            print(f"{self.cursor.rowcount} records inserted successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def login(self):
        print("Login")
        while True:
            user = input("Enter your username: ")
            password = input("Enter your password: ")
            query = "SELECT Username, Password FROM student_table WHERE Username = %s AND Password = %s"
            val = (user, password)
            self.cursor.execute(query, val)
            validate = self.cursor.fetchone()

            if validate:
                print(f"Welcome {validate[0]}")
                return validate[0]  # Return the student's username
            else:
                print("Invalid login, try again")

    def test_taking(self, student_username):
        print("Test Taking")
        
        # Get available subjects
        self.cursor.execute("SELECT DISTINCT Subject FROM cbt")
        subjects = [subject[0] for subject in self.cursor.fetchall()]

        if not subjects:
            print("No subjects available for testing.")
            return

        print("Available Subjects:")
        for i, subject in enumerate(subjects, start=1):
            print(f"{i}. {subject}")

        subject_choice = input("Enter the number of the subject you want to take (comma-separated for multiple subjects): ")

        selected_subjects = []
        for choice in subject_choice.split(","):
            index = int(choice.strip()) - 1
            if 0 <= index < len(subjects):
                selected_subjects.append(subjects[index])
            else:
                print(f"Invalid subject choice: {choice}")

        if not selected_subjects:
            print("No valid subjects selected.")
            return

        score = 0

        for subject in selected_subjects:
            # Retrieve questions for the specified subject
            query = "SELECT question_text, option_a, option_b, option_c, option_d, correct_answer FROM cbt WHERE Subject = %s"
            self.cursor.execute(query, (subject,))
            questions = self.cursor.fetchall()

            if not questions:
                print(f"No questions found for the subject: {subject}")
                continue

            for question_num, question in enumerate(questions, start=1):
                print(f"Subject: {subject}, Question {question_num}:")
                print(question[0])  # Display the question text
                print("Options:")
                print("A. " + question[1])
                print("B. " + question[2])
                print("C. " + question[3])
                print("D. " + question[4])

                answer = input("Enter your answer (A, B, C, or D): ").upper()

                if answer == question[5]:
                    print("Correct!")
                    score += 2
                else:
                    print("Wrong!")
                    
        insert_result_query = "INSERT INTO result_table (student_name, subject, score) VALUES (%s, %s, %s)"
        result_values = (student_username, ",".join(selected_subjects), score)

        try:
            self.cursor.execute(insert_result_query, result_values)
            self.connection.commit()
            print("Test results stored successfully.")
        except Exception as e:
            print(f"An error occurred while storing results: {e}")
            self.connection.rollback()

        print(f"Your total score is {score} out of {len(selected_subjects)} subjects.")


    def view_results(self, student_username):
        print("View Results")
        query = "SELECT subject, score FROM result_table WHERE student_name = %s"
        self.cursor.execute(query, (student_username,))
        results = self.cursor.fetchall()

        if results:
            print(f"Results for {student_username}:")
            for result in results:
                print(f"Subject: {result[0]}, Score: {result[1]}")
        else:
            print("No results found for this username.")

    def close(self):
        self.connection.close()

def main():
    db_config = {
        "host": "localhost",
        "user": "root",
        "passwd": "enter your database password",
        #create this database before running this code
        "database": "reg_db",
    }

    cbt_system = CBTSystem(db_config)

    while True:
        print("CBT System Menu:")
        print("1. Register Students")
        print("2. Set New Questions")
        print("3. Take a Test")
        print("4. View Results")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cbt_system.register_student()
        elif choice == "2":
            cbt_system.question_upload()
        elif choice == "3":
            student_username = cbt_system.login()
            if student_username:
                cbt_system.test_taking(student_username)
        elif choice == "4":
            student_username = input("Enter your username to view results: ")
            cbt_system.view_results(student_username)
        elif choice == "5":
            cbt_system.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
