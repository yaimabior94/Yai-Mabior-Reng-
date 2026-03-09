def sjf_scheduling():
    """
    3. Solves Customer Service Scheduling using Shortest Job First (SJF) 
    to minimize average system time.
    """
    print("=========================================================")
    print("⏱️ 3. Customer Service Scheduling (SJF)")
    print("=========================================================")
    
    # Given time service customer
    schedule_times = [5, 10, 3, 8, 2]
    num_customers = len(schedule_times)

    # Instruction: Sort customer based on time shortest service more first (SJF)
    sorted_schedule = sorted(schedule_times)
    
    print(f"Original Service Times: {schedule_times}")
    print(f"Sorted Service Times (SJF): {sorted_schedule}")

    # --- Calculation (Time in System) ---
    start_time = 0
    total_time_in_system = 0
    time_in_system_list = []
    
    # Table data for clean display
    results_table = []

    for service_time in sorted_schedule:
        # Finish Time = Start Time + Service Time
        finish_time = start_time + service_time
        
        # Time in System for this customer is the Finish Time (Completion Time)
        time_in_system_list.append(finish_time)
        total_time_in_system += finish_time
        
        # Record data for display
        results_table.append({
            'ST': service_time, 
            'Start': start_time, 
            'Finish': finish_time
        })
        
        # The next customer starts when the previous one finishes
        start_time = finish_time

    # Calculate Average Time in the System
    average_time = total_time_in_system / num_customers
    
    # --- Output ---
    print("\nProcessing Steps:")
    print("{:<10} {:<10} {:<10} {:<10}".format("Job (ST)", "Start Time", "Finish Time", "Time in System"))
    print("-" * 40)
    for i, row in enumerate(results_table):
        print("{:<10} {:<10} {:<10} {:<10}".format(
            row['ST'], row['Start'], row['Finish'], row['Finish']
        ))

    print("\n✅ SJF Scheduling Results:")
    print(f"Total Time in the System: **{total_time_in_system}**")
    print(f"Average Time in the System: **{average_time:.1f}**")
    

if __name__ == "__main__":
    sjf_scheduling()
    