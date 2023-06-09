from django.urls import path

from .views import (
    activar_autor,
    activar_empleado,
    activar_libro,
    activar_socio,
    actualizar_autor,
    actualizar_empleado,
    actualizar_socio,
    actualizar_libro,
    actualizar_prestamo,
    desactivar_autor,
    desactivar_empleado,
    desactivar_libro,
    desactivar_socio,
    eliminar_prestamo_libro,
    listado_autores,
    listado_empleados,
    listado_libros,
    listado_prestamos,
    listado_socios,
    registrar_autores,
    registrar_libro,
    registrar_socio,
    registrar_empleado,
    registrar_prestamo,
    pagina_principal
)


urlpatterns = [
    path('empleados/listado/', listado_empleados, name='listado_empleados'),
    path('empleados/nuevo/',registrar_empleado, name='registrar_empleado'),
    path('empleados/actualizar/<int:empleado_id>', actualizar_empleado, name='actualizar_empleado'),
    path('empleados/desactivar/<int:id>', desactivar_empleado, name='desactivar_empleado'),
    path('empleados/activar/<int:id>', activar_empleado, name='activar_empleado'),
    path('autores/listado/', listado_autores, name='listado_autores'),
    path('autores/nuevo/', registrar_autores, name='nuevo_autores'),
    path('autores/actualizar/<int:autor_id>', actualizar_autor, name='actualizar_autores'),
    path('autores/desactivar/<int:autor_id>', desactivar_autor, name='desactivar_autor'),
    path('autores/activar/<int:autor_id>', activar_autor, name='activar_autor'),
    path('socios/listado/', listado_socios, name='listado_socios'),
    path('socios/nuevo/', registrar_socio, name='nuevo_socio'),
    path('socios/actualizar/<int:socio_id>',actualizar_socio,name='actualizar_datos_socio'),
    path('socios/desactivar/<int:id>',desactivar_socio,name='desactivar_socio'),
    path('socios/activar/<int:id>',activar_socio,name='activar_socio'),
    path('libros/listado/',listado_libros, name='listado_libros'),
    path('libros/nuevo/', registrar_libro, name='nuevo_libro'),
    path('libros/actualizar/<int:id>', actualizar_libro, name='actualizar_libro'),
    path('libros/desactivar/<int:id>', desactivar_libro, name='desactivar_libro'),
    path('libros/activar/<int:id>', activar_libro, name='activar_libro'),
    path('prestamos/listado/',listado_prestamos, name='listado_prestamos'),
    path('prestamos/nuevo/', registrar_prestamo, name='registrar_prestamo'),
    path('prestamos/actualizar/<int:id>',actualizar_prestamo, name='actualizar_prestamo'),
    path('prestamos/eliminar/<int:prestamo_id>', eliminar_prestamo_libro, name='eliminar_prestamo_libro'),
    path('pagina_principal/', pagina_principal, name='pagina_principal')
]
