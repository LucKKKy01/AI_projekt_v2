from django.db import models
from django.core.files.storage import default_storage
from tensorflow import image as tf_image
from keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
# from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from django.core.files.base import ContentFile
import numpy as np
# Create your models here.


class ImageElement(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True, max_length=255)
    photo = models.ImageField(upload_to="mediaphoto", blank=True, null=True)


# class Imageai(models.Model): #models.Model 
#     title = models.CharField(max_length=255)
#     content = models.TextField(default="")
#     Imageai_ai = models.ImageField(upload_to="mediaai", blank=True, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            try:
                file_path = self.photo.path
                if default_storage.exists(file_path):
                    pil_image = tf_image.load_img(file_path, target_size=(299, 299))
                    img_array = tf_image.img_to_array(pil_image)
                    igm_array = np.expand_dims(img_array, axis=0)
                    igm_array = preprocess_input(igm_array)

                    model = InceptionV3(weights='imagenet')
                    predictions = model.predict(igm_array)
                    decode_predictions = decode_predictions((predictions), top=1)[0]
                    best_guess = decode_predictions[0][1]
                    self.title = best_guess
                    self.content = ', '.join([f'{pred[1]}]):{pred[2] * 100:.2f}%' for pred in decode_predictions])
                    super().save(*args, **kwargs)

            except Exception as e:
                pass


    # class Meta:
    #     verbose_name = 'Imageai'
    #     verbose_name_plural = 'Obrazy Ai'