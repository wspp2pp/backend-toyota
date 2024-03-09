from django import forms
from PIL import Image
import io
from apps.product.models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)

        if 'photo' in self.changed_data:
            image_data = self.cleaned_data['photo']
            if image_data:
                try:
                    image = Image.open(image_data)
                    image = image.convert('RGB')
                    compressed_image = image.copy()
                    compressed_image.thumbnail((300, 300))

                    buffer = io.BytesIO()
                    compressed_image.save(buffer, format='JPEG', quality=60)

                    filename = f"{instance.name}.jpg"
                    instance.photo.save(filename, buffer, save=True)

                except Exception as e:
                    print(f"Error al procesar la imagen: {e}")

        if commit:
            instance.save()
        return instance
