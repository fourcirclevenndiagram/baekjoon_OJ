n = int(input())
for i in range(n):
    my_choice_standard = list(input())
    if(my_choice_standard[0] == my_choice_standard[-1]):
        print("Do-it")
    else:
        print("Do-it-Not")