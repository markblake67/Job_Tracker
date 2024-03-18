import os

def add_job(jobs):
    company = input("Enter company name: ")
    position = input("Enter position: ")
    location = input("Enter location: ")
    status = input("Enter status (e.g., Applied, Interview, Offer): ")
    notes = input("Enter any notes: ")

    jobs.append({
        "company": company,
        "position": position,
        "location": location,
        "status": status,
        "notes": notes,
    })
#Need to add statement to check if the file exists and if it does append instead of create. 
def export_to_text_file(jobs, filename="JobTracker.txt"):   #Need to mess wit Excel, see whether I can export to there/ more convenient. or use termcolor module to add headings and stuff
    if os.path.isfile(filename):    #if statement attempt -if var(filename(JobTracker.txt)) exists then append_write variable = 'a' if not it's 'w'
        append_write = 'a'
    else:
        append_write = 'w'
    with open(filename, append_write) as file:
            for job in jobs:
                file.write(f"Company: {job['company']}\n")
                file.write(f"Position: {job['position']}\n")
                file.write(f"Location: {job['location']}\n")
                file.write(f"Status: {job['status']}\n")
                file.write(f"Notes: {job['notes']}\n")
                file.write("\n") #Need to spend more time adding if statement to not print to file if notes is empty. 
                
def main():
    jobs = []  # Initialize an empty list to store job data

    while True:
        print("\nJob Tracker Menu:")
        print("1. Add a new job")
        print("2. Export to text file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_job(jobs)
        elif choice == "2":
            export_to_text_file(jobs)
            print("Job data exported to job_tracker.txt")
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
