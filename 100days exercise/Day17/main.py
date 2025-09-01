from OOPS_con import *
question=Question()
flag=True
while flag:
    answer=question.answer
    user_input=bool(input(f"{question.question}"))










# import random
# def random_questions():
#     q=random.choice(questions)
#     answer=q['answer']
#     user_input=bool(input(f"Question: {q['question']}"))
#     return user_input,answer
#
#
# def check_answer(answer,user_input):
#     global score,attemt,flag
#     if answer == user_input:
#         print("Correct")
#         score+=1
#     else:
#         print("Incorrect")
#         flag=True
#     attemt += 1
# score=0
# attemt=0
# flag=False
# while flag is False:
#     user_input,answer=random_questions()
#     check_answer(answer,user_input)
#     print(score,"/",attemt)


# def is_palindrome(s):
#     s = str(s)
#     return s == s[::-1]
#
# # Example usage:
# test_str = input("Enter a string or number to check for palindrome: ")
# if is_palindrome(test_str):
#     print(f"{test_str} is a palindrome.")
# else:
#     print(f"{test_str} is not a palindrome.")
