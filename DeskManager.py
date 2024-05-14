from queue import Queue

def register_patient(patient_name, patient_queue):
    patient_queue.put(patient_name)
    print(f"Patient {patient_name} registered.")

def remove_patient(patient_queue):
    if patient_queue.empty():
        print("No patients in the queue.")
    else:
        next_patient = patient_queue.get()
        print(f"Patient {next_patient} removed after meeting the doctor.")

def display_patient_queue(patient_queue):
    if patient_queue.empty():
        print("No patients in the queue.")
    else:
        print("Current Patient Queue:")
        for index, patient in enumerate(list(patient_queue.queue), start=1):
            print(f"{index}. {patient}")

def main():
    patient_queue = Queue()

    while True:
        print("\nPatient Registration and Appointment Scheduling System")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = input("Enter patient's name: ")
            register_patient(patient_name, patient_queue)
        elif choice == '2':
            remove_patient(patient_queue)
        elif choice == '3':
            display_patient_queue(patient_queue)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
