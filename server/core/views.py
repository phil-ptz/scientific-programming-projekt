from django.shortcuts import render, get_object_or_404
from collections import defaultdict
from core.models import Bild
from core.classifier.classifier import classify_image
import os
from django.http import FileResponse

# Create your views here.

def home(request):
    """
    Render the introduction page.
    """
    return render(request, 'core/index.html')

def introduction(request):
    """
    Render the introduction page.
    """
    return render(request, 'core/intro.html')

def training(request):
    """
    Render the training page.
    """
    return render(request, 'core/training.html')

def classify(request):
    """
    Render the classification page.
    """
    label = None
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        try:
            label = classify_image(image_file)
        except Exception as e:
            label = f"Fehler bei der Klassifikation: {e}"
    return render(request, 'core/classify.html', {'label': label})

def classify_existing_image(request, bild_id):
    bild = get_object_or_404(Bild, id=bild_id)
    label = classify_image(bild.bild.path)
    return render(request, 'core/classify.html', {
        'label': label,
        'image_url': bild.bild.url
    })

def database(request):
    """
    Render the database page.
    """
    bilder = Bild.objects.all().order_by('label')
    gruppen = defaultdict(list)
    for bild in bilder:
        gruppen[bild.label].append(bild)
    context = {
        'gruppen': dict(gruppen)
    }
    return render(request, 'core/database.html', context)

def classify_notebook(request):

    """
    Render the classification notebook page.
    """
    return render(request, 'core/classify_nb.html')

def pflichtenheft(request):

    """ Render a PDF file.
    """

    pdf_path = os.path.join('core', 'templates', 'core', 'pflichtenheft.pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')