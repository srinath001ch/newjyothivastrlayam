from django import forms
from .models import Saree, SareeImage, Category, ContactMessage


class StyledFormMixin:
    """Applies a consistent premium dark-theme style to all form fields."""
    base_input_classes = (
        "w-full bg-black/40 border border-gold-500/30 rounded-lg px-4 py-3 "
        "text-white placeholder-gray-500 focus:outline-none focus:border-gold-500 "
        "focus:ring-1 focus:ring-gold-500 transition-all duration-300"
    )

    def style_fields(self):
        for name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({'class': 'w-5 h-5 accent-gold-500 rounded'})
            elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
                widget.attrs.update({'class': self.base_input_classes})
            elif isinstance(widget, forms.ClearableFileInput):
                widget.attrs.update({'class': 'w-full text-gray-300 file:mr-4 file:py-2 file:px-4 '
                                               'file:rounded-lg file:border-0 file:bg-gold-500 '
                                               'file:text-black file:font-semibold file:cursor-pointer'})
            elif isinstance(widget, forms.Textarea):
                widget.attrs.update({'class': self.base_input_classes, 'rows': 5})
            else:
                widget.attrs.update({'class': self.base_input_classes})


class SareeForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Saree
        fields = ['name', 'category', 'price', 'old_price', 'fabric',
                  'description', 'is_featured', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Royal Kanjivaram Silk Saree'}),
            'price': forms.NumberInput(attrs={'placeholder': 'e.g. 8999'}),
            'old_price': forms.NumberInput(attrs={'placeholder': 'Optional original price'}),
            'fabric': forms.TextInput(attrs={'placeholder': 'e.g. Pure Kanjivaram Silk'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the saree in detail...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_fields()


class SareeImageForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = SareeImage
        fields = ['image', 'is_primary']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_fields()


SareeImageFormSet = forms.inlineformset_factory(
    Saree, SareeImage, form=SareeImageForm, extra=3, can_delete=True
)


class CategoryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Kanjivaram Silk'}),
            'description': forms.TextInput(attrs={'placeholder': 'Short description (optional)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_fields()


class ContactForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Mobile Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_fields()
