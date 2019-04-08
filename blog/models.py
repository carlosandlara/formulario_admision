from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Formulario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nrofono = models.IntegerField()
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
        (CHILL, 'Chillan'),
        (SANT, 'Santiago'),
        (CONCE, 'Concepcion'),
        (OTRA, 'Otra ciudad'),
    )
    ciudad = models.CharField(max_length=20, choices=CIUDAD_CHOICES, blank=True)
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
        (AGRONOMIA, 'Agronomia'),
        (CONTADOR_AUDITOR, 'Contador Auditor'),
        (ED_PARVULARIA, 'Educacion Parvularia'),
        (ENFERMERIA, 'Enfermeria'),
        (ING_CIVIL_INFORMATICA, 'Ing. Civil en Informatica'),
        (ING_INFORMATICA, 'Ing. Informatica'),
        (ING_COMERCIAL, 'Ing. Comercial'),
        (ING_ELECTRONICA, 'Ing. en Electronica y Telecomunicaciones'),
        (ING_CIVIL_INDUSTRIAL, 'Ingenieria Civil Industrial'),
        (NUTRICION, 'Nutricion y Dietetica'),
        (OBSTETRICIA, 'Obstetricia y Puericultura'),
        (PED_BIO, 'Ped. en Biologia'),
        (PED_ED_DIFERENCIAL, 'Ped. en Educ. Diferencial m/DEA'),
        (PED_ED_FISICA, 'Ped. en Educacion Fisica'),
        (PED_ED_GEN_BASICA, 'Ped. en Educacion General Basica'),
        (PED_HISTORIA, 'Ped. en Historia y Geografia'),
        (PED_INGLES, 'Ped. en Ingles'),
        (PED_LENGUAJE, 'Ped. en Lengua Castellana y Comunicacion'),
        (PED_MATEMATICA, 'Ped. en Matematica y Computacion'),
        (PED_MUSICA, 'Ped. en Musica m/ Educacion Extraescolar'),
        (PSICOLOGIA, 'Psicologia'),
        (TEOLOGIA, 'Teologia'),
        (TNS_ENFERMERIA, 'TNS en Enfermeria'),
        (TRABAJO_SOCIAL, 'Trabajo Social'),
    )
    carrera_post_1 = models.CharField(max_length=50, choices=CARRERAPOST_CHOICES, blank=True)
    carrera_post_2 = models.CharField(max_length=50, choices=CARRERAPOST_CHOICES, blank=True)
    carrera_post_3 = models.CharField(max_length=50, choices=CARRERAPOST_CHOICES, blank=True)
