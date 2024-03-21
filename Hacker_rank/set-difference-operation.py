no_english = int(input())
english_students = set(map(int, input().split()))

no_french = int(input())
french_students = set(map(int, input().split()))

common_students = set()
for roll_no in english_students:
    if roll_no in french_students:
        common_students.add(roll_no)

unique_english_students = len(english_students.difference(common_students))
print(unique_english_students)
