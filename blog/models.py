from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Formulario(models.Model):
    rut = models.CharField(max_length=10, help_text="Tu RUT sin puntos y con guión")
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nrofono = PhoneNumberField(help_text="Los 8 dígitos luego del +569")
    email = models.EmailField()
    colegio = models.CharField(max_length=20)
    ARI = 'Arica'
    IQQ = 'Iquique'
    CHILL = 'Chillan'
    SANT = 'Santiago'
    CONCE = 'Concepcion'
    OTRA = 'Otra'
    CIUDAD_CHOICES = (
        (ARI, 'Arica'),
        (IQQ, 'Iquique'),
        (CHILL, 'Chillán'),
        (SANT, 'Santiago'),
        (CONCE, 'Concepción'),
        (OTRA, 'Otra ciudad'),
    )
    ciudad = models.CharField(max_length=20, choices=CIUDAD_CHOICES)
    PRIMERO = 'PRIMERO'
    SEGUNDO = 'SEGUNDO'
    TERCERO = 'TERCERO'
    CUARTO = 'CUARTO'
    OTRO = 'OTRO'
    ANIO_POSTULANTE_CHOICES = (
        (PRIMERO, '1° medio'),
        (SEGUNDO, '2° medio'),
        (TERCERO, '3° medio'),
        (CUARTO, '4° medio'),
        (OTRO, 'Ya egresé'),
    )
    """anioegreso = models.SmallIntegerField(
        default=2015,
        blank=True,
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(3000)
    ]
    )"""
    anioegreso = models.CharField(max_length=4, blank=True)
    aniopost = models.CharField(max_length=15, choices=ANIO_POSTULANTE_CHOICES)
    AGRONOMIA = 'AGRO'
    CONTADOR_AUDITOR = 'CON_AUD'
    ED_PARVULARIA = 'ED_PARV'
    ENFERMERIA = 'ENF'
    ING_CIVIL_INFORMATICA = 'ING_CIV_INF'
    ING_INFORMATICA = 'ING_INF'
    ING_COMERCIAL = 'ING_COM'
    ING_ELECTRONICA = 'ING_ELEC'
    ING_CIVIL_INDUSTRIAL = 'ING_CIV_IND'
    NUTRICION = 'NUT'
    OBSTETRICIA = 'OBS'
    PED_BIO = 'PED_BIO'
    PED_ED_DIFERENCIAL = 'PED_ED_DIF'
    PED_ED_FISICA = 'PED_ED_FIS'
    PED_ED_GEN_BASICA = 'PED_ED_GEN_BAS'
    PED_HISTORIA = 'PED_HIS'
    PED_INGLES = 'PED_ING'
    PED_LENGUAJE = 'PED_LENG'
    PED_MATEMATICA = 'PED_MAT'
    PED_MUSICA = 'PED_MUS'
    PSICOLOGIA = 'PSICO'
    TEOLOGIA = 'TEO'
    TNS_ENFERMERIA = 'TNS_ENF'
    TRABAJO_SOCIAL = 'TRAB_SOC'
    CARRERAPOST_CHOICES = (
        (AGRONOMIA, 'Agronomía'),
        (CONTADOR_AUDITOR, 'Contador Auditor'),
        (ED_PARVULARIA, 'Educación Parvularia'),
        (ENFERMERIA, 'Enfermería'),
        (ING_COMERCIAL, 'Ingeniería Comercial'),
        (ING_INFORMATICA, 'Ingeniería Informática'),
        (ING_ELECTRONICA, 'Ingeniería en Electrónica y Telecomunicaciones'),
        (ING_CIVIL_INDUSTRIAL, 'Ingeniería Civil Industrial'),
        (ING_CIVIL_INFORMATICA, 'Ingeniería Civil Informática'),
        (NUTRICION, 'Nutrición y Dietética'),
        (OBSTETRICIA, 'Obstetricia y Puericultura'),
        (PED_BIO, 'Pedagogía en Biología'),
        (PED_ED_DIFERENCIAL, 'Pedagogía en Educación Diferencial'),
        (PED_ED_FISICA, 'Pedagogía en Educación Física'),
        (PED_ED_GEN_BASICA, 'Pedagogía en Educación General Básica'),
        (PED_HISTORIA, 'Pedagogía en Historia y Geografia'),
        (PED_INGLES, 'Pedagogía en Inglés'),
        (PED_LENGUAJE, 'Pedagogía en Lengua Castellana y Comunicacion'),
        (PED_MATEMATICA, 'Pedagogía en Matemática y Computacion'),
        (PED_MUSICA, 'Pedagogía en Música'),
        (PSICOLOGIA, 'Psicología'),
        (TEOLOGIA, 'Teología'),
        (TNS_ENFERMERIA, 'TENS en Enfermería'),
        (TRABAJO_SOCIAL, 'Trabajo Social'),
    )

    carrera_post_1 = models.CharField(max_length=50, choices=CARRERAPOST_CHOICES)
    carrera_post_2 = models.CharField(max_length=50, choices=CARRERAPOST_CHOICES, blank=True)
    carrera_post_3 = models.CharField(max_length=50, choices=CARRERAPOST_CHOICES, blank=True)
