total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to complete today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1:
        next_chore = "making your bed"
    elif chore_num == 2:
        next_chore = "feeding your pet"
    elif chore_num == 3:
        next_chore = "doing the dishes"
    else:
        next_chore = "taking out the trash"
    answer = input(f"Have you finished {next_chore}? (yes/no) ".lower())
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed.")
    else: 
        print("You must complete the chore.")
    print("Chores Remaining:", total_chores - completed_count)
    print()
print("===== ALL CHORES COMPLETED =====")
print("Great work completing all of your chores today! Keep it up.\n")
print("Now let's safely look at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("This is on purpose to stop the loop - a real infinite loop never stops on its own.")
        break
print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned:", original_count)
print("Chores Completed:", completed_count)
print("Chores Remaning:", original_count - completed_count)
print("=" * 30)