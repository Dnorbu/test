from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_pagen = None

#Visit function
NoOfVisits = int(input("Enter the number of url history: "))
print("Enter URLs tp visit:")
for i in range(NoOfVisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url

 #Display current page
 print(f"Current page: {current_page}")

#Go back
while input("Do you want to go back? (yes/no): ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page is available")

#Go forward
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page is available")
