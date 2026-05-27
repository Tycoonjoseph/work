# question game for people 
# what is the name of the user 
name = str(input("What is your name? ")).capitalize().strip()
# question their age
age = int(input("How old are you? "))
# ask which degree their parting in 
degree = str(input("What degree are you pursuing? ")).capitalize().strip()
# ask when they will graduate and the date their joined the university
graduation_year = int(input("When will you graduate? "))
join_year = int(input("When did you join the university? "))
# What is you view on the coming future of yourself and the world like the next phase of lifes after graduation
future_view = str(input("What is your view on the coming future of yourself and the world like the next phase of life after graduation? ")).capitalize().strip()
# ask the user about their parents
parents = str(input("What do your parents do for a living? ")).capitalize().strip()
#Ask the user about their hobbies and interests
hobbies = str(input("What are you hobbies and interests? ")).capitalize().strip()
# ask the user about their favorite food and drink
favorite_food = str(input("What is your favorite food? ")).capitalize().strip()
favorite_drink = str(input("What is your favorite drink? ")).capitalize().strip()
# what are you looking to being doing in your daily life graduation
daily_life = str(input("What are you looking to being doing in your daily life after graduation? ")).capitalize().strip()
#print the report of the user
print(f"{name} is {age} years old and is pursuing a degree in {degree}. They will graduate in {graduation_year} and joined the university in {join_year}. They view the future as {future_view}. Their parents work as {parents}. Their hobbies and interests include {hobbies}. Their favorite food is {favorite_food} and their favorite drink is {favorite_drink}. After graduation, they are looking to being doing {daily_life} in their daily life.")