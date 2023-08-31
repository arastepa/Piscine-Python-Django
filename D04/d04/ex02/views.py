from datetime import datetime
from django.shortcuts import render

from django.conf import settings
from .forms import TextInputForm
from django.utils import timezone
import pytz
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            yerevan_timezone = pytz.timezone('Asia/Yerevan')
            current_time_in_yerevan = timezone.now().astimezone(yerevan_timezone)
            # Save input_text to log file
            with open(settings.HISTORY_LOG_FILE, 'a') as log_file:
                log_file.write(f"{input_text} - {current_time_in_yerevan}\n")
    else:
        form = TextInputForm()

    # Read the log file and prepare input history
    input_history = []
    try:
        with open(settings.HISTORY_LOG_FILE, 'r') as log_file:
            input_history = log_file.readlines()
    except FileNotFoundError:
        pass

    context = {
        'form': form,
        'input_history': input_history,
    }
    return render(request, 'ex02.html', context)
