from .models import Stock

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
    fields = ["ticker"]
    
<form method='POST'> {% csrf_token %}
  {{form.as_p}}
  <button type='submt' class= 'btn btn-primary'>Save</button>
</form>