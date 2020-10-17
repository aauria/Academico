from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from .models import Docente,CursoDocente
from .form import Docenteform,CursoDocenteForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
import io
from reportlab.lib.enums import TA_RIGHT,TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph,Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


# relaciona la parte vista con el template home.html
def home(request, plantilla="home.html"):
    return render(request, plantilla);
def index(request, plantilla="index.html"):
    return render(request, plantilla);
def login(request, plantilla="login.html"):
    return render(request, plantilla);
def correo(request, plantilla="correo.html"):
    return render(request, plantilla);

class lista_docente(PermissionRequiredMixin,ListView):
    model = Docente
    template_name = 'docente/consulta.html'
    permission_required = 'core.view_docente'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(nombre__contains=buscar)|Q(apellido__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list

class crear_docente(PermissionRequiredMixin,CreateView):
    model = Docente
    form_class = Docenteform
    template_name = 'docente/formulario.html'
    success_url = reverse_lazy('consulta')
    permission_required = 'core.add_docente'

class update_docente(PermissionRequiredMixin,UpdateView):
    model = Docente
    form_class = Docenteform
    template_name = 'docente/formulario.html'
    success_url = reverse_lazy('consulta')
    permission_required = 'core.change_docente'

class delete_docente(PermissionRequiredMixin,DeleteView):
    model = Docente
    template_name = 'docente/verificar.html'
    success_url = reverse_lazy('consulta')
    permission_required = 'core.delete_docente'

class lista_docentecurso(PermissionRequiredMixin,ListView):
    model = CursoDocente
    template_name = 'curso/consulta_cursodocente.html'
    permission_required = 'core.view_cursodocente'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(curso__nivel__contains=buscar)|Q(Docente__apellido__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list


class crear_docentecurso(PermissionRequiredMixin,CreateView):
    model = CursoDocente
    form_class = CursoDocenteForm
    template_name = 'curso/formulario_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')
    permission_required = 'core.add_cursodocente'

class update_docentecurso(PermissionRequiredMixin,UpdateView):
    model = CursoDocente
    form_class = CursoDocenteForm
    template_name = 'curso/formulario_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')
    permission_required = 'core.change_cursodocente'

class delete_docentecurso(PermissionRequiredMixin,DeleteView):
    model = CursoDocente
    template_name = 'curso/verificar_cursodocente.html'
    success_url = reverse_lazy('consulta_cursodocente')
    permission_required = 'core.delete_cursodocente'
# Create your views here.
def exportardocente(request, plantilla="docente/consulta.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_docente.pdf"'

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

    curso = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Docentes", styles['Heading1'])
    curso.append(header)
    headings = ('Id', 'Nombre', 'Apellido','Edad','Email','Cedula')
    alldocente = [(d.id, d.nombre, d.apellido,d.edad,d.email,d.cedula) for d in Docente.objects.all()]
    print
    alldocente

    t = Table([headings] + alldocente)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    curso.append(t)
    doc.build(curso)
    response.write(buffer.getvalue())
    buffer.close()
    return response
