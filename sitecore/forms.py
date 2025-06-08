from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

class OrcamentoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    descricao_projeto = forms.CharField(widget=forms.Textarea)
    arquivo = forms.FileField(required=False)
