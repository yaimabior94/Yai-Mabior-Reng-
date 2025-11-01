def activity_selection():
    """
    2. Solves the Activity Selection Problem using two greedy strategies 
    (Finish Time and Duration) and compares the results.
    """
    print("=========================================================")
    print("📅 2. Activity Selection Program")
    print("=========================================================")
    
    # Given Activities: (Activity Name, Start Time, Finish Time)
    ACTIVITIES = [
        {'name': 'A', 'start': 1, 'finish': 4},
        {'name': 'B', 'start': 3, 'finish': 5},
        {'name': 'C', 'start': 0, 'finish': 6},
        {'name': 'D', 'start': 5, 'finish': 7},
        {'name': 'E', 'start': 8, 'finish': 9},
        {'name': 'F', 'start': 5, 'finish': 9}
    ]

    def select_activities(sorted_activities, strategy_name):
        """Implements the core non-overlapping greedy selection logic."""
        if not sorted_activities:
            return []

        # Start with the first activity in the sorted list
        selected = [sorted_activities[0]]
        last_finish_time = sorted_activities[0]['finish']

        # Iterate through the remaining activities
        for i in range(1, len(sorted_activities)):
            current_activity = sorted_activities[i]
            
            # Select the activity if its start time is >= the last finish time
            if current_activity['start'] >= last_finish_time:
                selected.append(current_activity)
                last_finish_time = current_activity['finish']
        
        selected_names = [a['name'] for a in selected]
        print(f"Strategy: **{strategy_name}**")
        print(f"Selected Activities: {', '.join(selected_names)}")
        return selected_names

    # --- Version 1: Based on Finish Time (Optimal Greedy Strategy) ---
    print("\n--- Version 1: Based on time finished (Finish Time) ---")
    activities_v1 = sorted(ACTIVITIES, key=lambda x: x['finish'])
    
    print("Sorted Activities:", [(a['name'], a['finish']) for a in activities_v1])
    selected_v1 = select_activities(activities_v1, "Finish Time (Earliest First)")
    

    # --- Version 2: Based on Duration Activity (Finish - Start) ---
    print("\n--- Version 2: Based on duration activity (Duration) ---")
    # Add duration and sort by duration (shortest first)
    activities_v2 = sorted([
        {**a, 'duration': a['finish'] - a['start']} 
        for a in ACTIVITIES
    ], key=lambda x: x['duration'])
    
    print("Sorted Activities:", [(a['name'], a['duration']) for a in activities_v2])
    selected_v2 = select_activities(activities_v2, "Duration (Shortest First)")

    # --- Comparison ---
    print("\n--- Comparison ---")
    len_v1 = len(selected_v1)
    len_v2 = len(selected_v2)
    print(f"Result V1 (Finish Time): **{len_v1}** activities selected.")
    print(f"Result V2 (Duration): **{len_v2}** activities selected.")
    
    is_same = "The same" if len_v1 == len_v2 else "Different"
    print(f"Whether amount activity selected is the same? **{is_same}**")

if __name__ == "__main__":
    activity_selection()
    