from apps.data_sheet.models import DataSheet
from apps.product.forms import ProductAdminForm


class DataSheetAdminForm(ProductAdminForm):
    class Meta:
        model = DataSheet
        fields = '__all__'
