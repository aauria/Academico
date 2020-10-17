from django.urls import reverse_lazy
from .models import Estudiante,EstudianteMateriaDocente,EstudianteMateriaCurso
from .form import Estudianteform,EstudianteMateriaDocenteform,EstudianteMateriaCursoform
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
from django.shortcuts import HttpResponse



# relaciona la parte vista con el template home.html

class lista_estudiante(PermissionRequiredMixin,ListView):
    model = Estudiante
    template_name = 'estudiante/consulta_estudiante.html'
    permission_required = 'estudiante.view_estudiante'
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

class crear_estudiante(PermissionRequiredMixin,CreateView):
    model = Estudiante
    form_class = Estudianteform
    template_name = 'estudiante/formulario_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')
    permission_required = 'estudiante.add_estudiante'

class update_estudiante(PermissionRequiredMixin,UpdateView):
    model = Estudiante
    form_class = Estudianteform
    template_name = 'estudiante/formulario_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')
    permission_required = 'estudiante.change_estudiante'

class delete_estudiante(PermissionRequiredMixin,DeleteView):
    model = Estudiante
    template_name = 'estudiante/verificar_estudiante.html'
    success_url = reverse_lazy('consulta_estudiante')
    permission_required = 'estudiante.delete_estudiante'



class lista_estudiantedocentemateria(PermissionRequiredMixin,ListView):
    model = EstudianteMateriaDocente
    template_name = 'estudiante/consulta_estudiantedocentemateria.html'
    permission_required = 'estudiante.view_estudiantemateriadocente'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(estudiante__apellido__contains=buscar)|Q(docente__apellido__contains=buscar)|Q(materia__nombre__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list

class crear_estudiantedocentemateria(PermissionRequiredMixin,CreateView):
    model = EstudianteMateriaDocente
    form_class = EstudianteMateriaDocenteform
    template_name = 'estudiante/formulario_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')
    permission_required = 'estudiante.add_estudiantemateriadocente'

class update_estudiantedocentemateria(PermissionRequiredMixin,UpdateView):
    model = EstudianteMateriaDocente
    form_class = EstudianteMateriaDocenteform
    template_name = 'estudiante/formulario_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')
    permission_required = 'estudiante.change_estudiantemateriadocente'


class delete_estudiantedocentemateria(PermissionRequiredMixin,DeleteView):
    model = EstudianteMateriaDocente
    template_name = 'estudiante/verificar_estudiantedocentemateria.html'
    success_url = reverse_lazy('consulta_estudiante_doc_mat')
    permission_required = 'estudiante.delete_estudiantemateriadocente'

class lista_estudiantemateriacurso(PermissionRequiredMixin,ListView):
    model = EstudianteMateriaCurso
    template_name = 'estudiante/consulta_estudiantemateriacurso.html'
    permission_required = 'estudiante.view_estudiantemateriacurso'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(estudiante__apellido__contains=buscar)|Q(curso__nivel__contains=buscar)|Q(materia__nombre__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list

class crear_estudiantemateriacurso(PermissionRequiredMixin,CreateView):
    model = EstudianteMateriaCurso
    form_class = EstudianteMateriaCursoform
    template_name = 'estudiante/formulario_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')
    permission_required = 'estudiante.add_estudiantemateriacurso'


class update_estudiantemateriacurso(PermissionRequiredMixin,UpdateView):
    model = EstudianteMateriaCurso
    form_class = EstudianteMateriaCursoform
    template_name = 'estudiante/formulario_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')
    permission_required = 'estudiante.change_estudiantemateriacurso'

class delete_estudiantemateriacurso(PermissionRequiredMixin,DeleteView):
    model = EstudianteMateriaCurso
    template_name = 'estudiante/verificar_estudiantemateriacurso.html'
    success_url = reverse_lazy('consulta_estudiante_mat_curso')
    permission_required = 'estudiante.delete_estudiantemateriacurso'

def exportarestudiante(request, plantilla="estudiante/consulta_estudiante.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_estudiante.pdf"'

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

    estudiante = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Estudiante", styles['Heading1'])
    estudiante.append(header)
    headings = ('Id', 'Nombre', 'Apellido','Edad','Email','Cedula','Curso')
    allestudiante = [(d.id, d.nombre, d.apellido,d.edad,d.email,d.cedula,d.curso) for d in Estudiante.objects.all()]
    print
    allestudiante

    t = Table([headings] + allestudiante)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    estudiante.append(t)
    doc.build(estudiante)
    response.write(buffer.getvalue())
    buffer.close()
    return response
