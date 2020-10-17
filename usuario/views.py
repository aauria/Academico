from django.contrib.auth.models import User,Group
from usuario.forms import RegistroForms,GroupForms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
import io
from reportlab.lib.enums import TA_RIGHT,TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph,Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from django.shortcuts import HttpResponse




class registro_usuario(PermissionRequiredMixin,CreateView):
    model = User
    template_name = "usuario/registrar_usuario.html"
    form_class = RegistroForms
    success_url = reverse_lazy("consulta_usuario")
    permission_required = 'user.add_user'

class lista_usuario(PermissionRequiredMixin,ListView):
    model = User
    template_name = "usuario/consulta_usuario.html"
    permission_required = 'user.view_user'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(first_name__contains=buscar)|Q(last_name__contains=buscar)|Q(username__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list

class update_usuario(PermissionRequiredMixin,UpdateView):
    model = User
    template_name = 'usuario/registrar_usuario.html'
    form_class = RegistroForms
    success_url = reverse_lazy('consulta_usuario')
    permission_required = 'user.change_user'

class delete_usuario(PermissionRequiredMixin,DeleteView):
    model = User
    template_name = 'usuario/verificar_usuario.html'
    success_url = reverse_lazy('consulta_usuario')
    permission_required = 'user.delete_user'

class registro_grupo(PermissionRequiredMixin,CreateView):
    model = Group
    template_name = "usuario/registro_grupo.html"
    form_class = GroupForms
    success_url = reverse_lazy("home")
    permission_required =  'group.add_group'

class lista_grupo(PermissionRequiredMixin,ListView):
    model = Group
    template_name = "usuario/consulta_grupo.html"
    permission_required = 'group.view_group'
    def get_queryset(self):
        try:
            buscar=self.request.GET.get('buscar')
        except KeyError:
            buscar=None
        if buscar:
            object_list=self.model.objects.filter(Q(name__contains=buscar))
        else:
            object_list=self.model.objects.all()
        return object_list

class update_grupo(PermissionRequiredMixin,UpdateView):
    model = Group
    template_name = 'usuario/registro_grupo.html'
    form_class = GroupForms
    success_url = reverse_lazy('consulta_grupo')
    permission_required = 'group.change_group'

class delete_grupo(PermissionRequiredMixin,DeleteView):
    model = Group
    template_name = 'usuario/verificar_grupo.html'
    success_url = reverse_lazy('consulta_grupo')
    permission_required = 'group.delete_group'

def exportarusuario(request, plantilla="usuario/consulta_usuario.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_usuarios.pdf"'

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

    usuario = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Usuarios", styles['Heading1'])
    usuario.append(header)
    headings = ('Id', 'Usuario', 'Nombre','Apellido','Email')
    allusuario = [(d.id, d.username, d.first_name,d.last_name,d.email) for d in User.objects.all()]
    print
    allusuario

    t = Table([headings] + allusuario)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    usuario.append(t)
    doc.build(usuario)
    response.write(buffer.getvalue())
    buffer.close()
    return response


