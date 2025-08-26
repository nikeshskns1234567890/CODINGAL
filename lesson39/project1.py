# Exam Eligibility Test

# student details
attendance = 85    # percentage
marks = 42        # internal marks out of 100
age = 12        # student age

print("---- Exam Eligibility Test ----")

# Step 1: Check attendance
if attendance < 75:
    print("❌ Not Eligible - Attendance too low!")
else:
    print("✔ Attendance Requirement Passed")

    # Step 2: Check internal marks
    if marks < 35:
        print("❌ Not Eligible - Marks too low!")
    else:
        print("✔ Marks Requirement Passed")

        # Step 3: Check age criteria
        if age < 14:
            print("❌ Not Eligible - Too young for exam")
        elif age > 18:
            print("❌ Not Eligible - Age exceeds limit")
        else:
            print("✔ Age Requirement Passed")
            print("🎉 Congratulations! You are Eligible for the Exam ✅")
