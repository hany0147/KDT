from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'nums/index.html')


def number_print(request, number):
    context = {
        'number': number
    }
    return render(request, 'nums/number_print.html', context)


def calculate(request, number1, number2):
    plus = number1 + number2
    minus = number1 - number2
    multiply = number1 * number2
    quotient = number1 // number2
    context = {
        'plus': plus,
        'minus': minus,
        'multiply': multiply,
        'quotient': quotient,
    }
    return render(request, 'nums/calculate.html', context)