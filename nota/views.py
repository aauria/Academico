from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Notas
from .form import NotaForm
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

class lista_notas(PermissionRequiredMixin,ListView):
    model = Notas
    template_name = 'nota/consulta_nota.html'
    permission_required = 'nota.view_notas'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(Materia__nombre__contains=buscar)|Q(Estudiante__nombre__contains=buscar)|Q(Docente__nombre__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list

class crear_notas(PermissionRequiredMixin,CreateView):
    model = Notas
    form_class = NotaForm
    template_name = 'nota/formulario_nota.html'
    success_url = reverse_lazy('consulta_nota')
    permission_required = 'nota.add_notas'

class update_notas(PermissionRequiredMixin,UpdateView):
    model = Notas
    form_class = NotaForm
    template_name = 'nota/formulario_nota.html'
    success_url = reverse_lazy('consulta_nota')
    permission_required = 'nota.change_notas'

class delete_notas(PermissionRequiredMixin,DeleteView):
    model = Notas
    template_name = 'nota/verificar_nota.html'
    success_url = reverse_lazy('consulta_nota')
    permission_required = 'nota.delete_notas'

def exportarnotas(request, plantilla="nota/consulta_nota.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_notas.pdf"'

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

    nota = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Notas", styles['Heading1'])
    nota.append(header)
    headings = ('Id', 'Materia', 'Docente','Curso','Estudiante','Nota_1','Nota_2','Nota_3')
    allnota = [(d.id, d.Materia, d.Docente,d.Curso,d.Estudiante,d.nota1,d.nota2,d.nota3) for d in Notas.objects.all()]
    print
    allnota

    t = Table([headings] + allnota)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    nota.append(t)
    doc.build(nota)
    response.write(buffer.getvalue())
    buffer.close()
    return response