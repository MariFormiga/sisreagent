from django.contrib import admin
from .models import Controle_de_Validade
from .models import Ficha_Cardex
from .models import Itens
from .models import Devolucao_de_Produtos
from .models import Livro_de_Registro
from .models import Ultimas_Compras
from .models import Fornecedores


admin.site.register(Controle_de_Validade)
admin.site.register(Ficha_Cardex)
admin.site.register(Itens)
admin.site.register(Devolucao_de_Produtos)
admin.site.register(Livro_de_Registro)
admin.site.register(Ultimas_Compras)
admin.site.register(Fornecedores)
