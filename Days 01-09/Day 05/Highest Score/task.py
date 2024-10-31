student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(f"Max (using function): {max(student_scores)}")
print(f"Min (using function): {min(student_scores)}")

max_score = 0
min_score = student_scores[0]

for score in student_scores:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score

print(f"Max (using for loop): {max_score}")
print(f"Min (using for loop): {min_score}")
