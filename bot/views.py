from django.shortcuts import render
from django.http import JsonResponse

from .models import ChatHistory, Question


dialog_status = True
def startChat(request):
    message = "Hello, I'm a curious bot, would you like to talk with me?"
    context = {
        "message": message
    }
    return render(request, "bot/index.html", context)

def start_dialog(message):

    agreements = ["y", "ok", "yes", "of course", "yeap",  "i do",  "true", "right", "let's go", "ok", "+"]
    disagreements = ["n", "no", "never", "not", "false", "cancel", "refuse", "nope", "don't", "-"]

    message = message.strip().lower()

    if message in agreements:
        return  "Yoo-hoo! Let's talk!", 1
    elif message in disagreements:
        return  '''It's a pity, I feel so lonely in this big digital world..\n
                   Please, let's talk?''' , -1
    else:
        return  "I don't understand. So would you like to talk with me?", 0




def get_answer(request):
    message = request.GET.get("message")
    dialog_id = int(request.GET.get("dialog_id"))

    if dialog_id == 0:
        dialog = ChatHistory.objects.create(answers = message)
        dialog.save()
    else:
        dialog = ChatHistory.objects.get(id = dialog_id)
        dialog.answers += "\n" + message
        

    questions = Question.objects.all()

    if dialog.answers_number == 0:
        answer, answer_status = start_dialog(message)
        
        if answer_status == 1:
            answer += "\n" + questions[0].question_text
            dialog.answers_number += 1

    elif 0 < dialog.answers_number < 9:
        answer = questions[dialog.answers_number].question_text
        dialog.answers_number += 1
    else:
        answer = "** Bot is offline **"

    
    dialog.save()

    response_data = {
        "message": answer,
        "id": dialog.id,
    }
    return JsonResponse(response_data)
