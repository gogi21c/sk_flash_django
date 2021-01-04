from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def add(request):
    from random import randint

    if request.method == "GET":
        num_1 = randint(1,9)
        num_2 = randint(1,9)

    if request.method == "POST":
        num_1 = randint(1,9)
        num_2 = randint(1,9)
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        if not answer:
            my_answer = "Enter the answer"
            color = "dark"
            return render(request, 'add.html', { 
                'my_answer': my_answer,
                'answer': answer,
                'num_1': old_num_1,
                'num_2': old_num_2,
                'color': color,
               })
      

        correct_answer = int(old_num_1) + int(old_num_2)

        if int(answer) == correct_answer:
            my_answer = "Correct " + str(old_num_1) + " + "  + str(old_num_2) + " = " + str(correct_answer)
            color = "success"
        else:
            my_answer = "Incorrect " + str(old_num_1) + " + "  + str(old_num_2) + " is not " + str(correct_answer)
            color = "danger"

        return render(request, 'add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_1,
            'color': color,
            })

    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2':num_2,
        })

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})

