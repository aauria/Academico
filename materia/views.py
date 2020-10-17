from django.urls import reverse_lazy
from .models import Materia
from .form import Materiaform
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.db.models import Q
import io
from reportlab.lib.enums import TA_RIGHT,TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph,Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from django.shortcuts import HttpResponse

# Create your views here.

class lista_materia(PermissionRequiredMixin,ListView):
    model = Materia
    template_name = 'materia/consulta_materia.html'
    permission_required = 'materia.view_materia'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(nombre__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list

class crear_materia(PermissionRequiredMixin,CreateView):
    model = Materia
    form_class = Materiaform
    template_name = 'materia/formulario_materia.html'
    success_url = reverse_lazy('consulta_materia')
    permission_required = 'materia.add_materia'

class update_materia(PermissionRequiredMixin,UpdateView):
    model = Materia
    form_class = Materiaform
    template_name = 'materia/formulario_materia.html'
    success_url = reverse_lazy('consulta_materia')
    permission_required = 'materia.change_materia'

class delete_materia(PermissionRequiredMixin,DeleteView):
    model = Materia
    template_name = 'materia/verificar_materia.html'
    success_url = reverse_lazy('consulta_materia')
    permission_required = 'materia.delete_materia'

def exportarmateria(request, plantilla="materia/consulta_materia.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_materias.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    materia = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Materias", styles['Heading1'])
    materia.append(header)
    headings = ('Id', 'Nombre')
    allmateria = [(d.id, d.nombre) for d in Materia.objects.all()]
    print
    allmateria

    t = Table([headings] + allmateria)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    materia.append(t)
    doc.build(materia)
    response.write(buffer.getvalue())
    buffer.close()
    return response
# Create your views here.
