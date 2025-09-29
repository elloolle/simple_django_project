from simple_django_project.celery import app




@app.task
def moderateImage(image):
    pass


@app.task
def moderateText(text):
    pass


@app.task
def moderateVideo(video):
    pass
