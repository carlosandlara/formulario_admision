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
    nrofono = PhoneNumberField(help_text="Los 8 dígitos luego del +56", default='9')
    email = models.EmailField()

    """Ciudades"""
    ARI = 'Arica'
    IQQ = 'Iquique'
    CHILL = 'Chillan'
    SANT = 'Santiago'
    CONCE = 'Concepcion'
    OTRA = 'Otra'
    CIUDAD_CHOICES = (
        ('', 'Escoge una ciudad...'),
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
        ('', 'Escoge un curso...'),
        (PRIMERO, '1° medio'),
        (SEGUNDO, '2° medio'),
        (TERCERO, '3° medio'),
        (CUARTO, '4° medio'),
        (OTRO, 'Ya egresé'),
    )
    anioegreso = models.CharField(max_length=4, blank=True)
    aniopost = models.CharField(max_length=15, choices=ANIO_POSTULANTE_CHOICES)
    """anioegreso = models.SmallIntegerField(
        default=2015,
        blank=True,
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(3000)
    ]
    )"""
    """ColegiosAdventistas"""
    COADAR = 'Arica'
    CAI = 'Iquique'
    CADECAL = 'Calama'
    COADAN = 'Antofagasta'
    CADECOP = 'Copiapó'
    CADELSE = 'La Serena'
    CADEQUI = 'Quilpué'
    CABU = 'Buenaventura'
    CAP = 'Porvenir'
    COALC = 'La Cisterna'
    CALC = 'Las Condes'
    CASAN = 'Santiago Norte'
    CASS = 'Santiago Sur'
    CASAP = 'Santiago Poniente'
    CAM = 'Molina'
    COADET = 'Talca'
    CACH = 'Chillan'
    CAL = 'Lota'
    CATCE = 'Talcahuano Centro'
    CADET = 'Talcahuano'
    CADEC = 'Concepción'
    CEALA = 'Los Angeles'
    COADVAN = 'Angol'
    COADTE = 'Temuco'
    COADPI = 'Pitrufquén'
    CADVI = 'Villarrica'
    CADVA = 'Valdivia'
    COADPA = 'Punta Arenas'
    COLEGIOS_ADV_CHOICES = (
        ('', 'Escoge un colegio...'),
        (COADAR, 'Colegio Adventista de Arica'),
        (CAI, 'Colegio Adventista de Iquique'),
        (CADECAL, 'Colegio Adventista de Calama'),
        (COADAN, 'Colegio Adventista de Antofagasta'),
        (CADECOP, 'Colegio Adventista de Copiapó'),
        (CADELSE, 'Colegio Adventista de La Serena'),
        (CADEQUI, 'Colegio Adventista de Quilpué'),
        (CABU, 'Colegio Adventista de Buenaventura'),
        (CAP, 'Colegio Adventista Porvenir'),
        (COALC, 'Colegio Adventista La Cisterna'),
        (CALC, 'Colegio Adventista Las Condes'),
        (CASAN, 'Colegio Adventista Santiago Norte'),
        (CASS, 'Colegio Adventista Santiago Sur'),
        (CASAP, 'Colegio Adventista Santiago Poniente'),
        (CAM, 'Colegio Adventista de Molina'),
        (COADET, 'Colegio Adventista de Talca'),
        (CACH, 'Colegio Adventista de Chile'),
        (CAL, 'Colegio Adventista de Lota'),
        (CATCE, 'Colegio Adventista Talcahuano Centro'),
        (CADET, 'Colegio Adventista de Talcahuano'),
        (CADEC, 'Colegio Adventista de Concepción'),
        (CEALA, 'Centro Educacional Adventista Los Angeles'),
        (COADVAN, 'Colegio Adventista de Angol'),
        (COADTE, 'Colegio Adventista de Temuco'),
        (COADPI, 'Colegio Adventista de Pitrufquén'),
        (CADVI, 'Colegio Adventista de Villarrica'),
        (CADVA, 'Colegio Adventista de Valdivia'),
        (COADPA, 'Colegio Adventista de Punta Arenas'),
    )
    colegioadv = models.CharField(max_length=40, choices=COLEGIOS_ADV_CHOICES, blank=True)
    """Colegios"""
    SANVICENTE = 'Colegio San Vicente de Paul'
    PURISIMA = 'Colegio Purísima Concepción'
    SANBUENA = 'Colegio San Buenaventura'
    SANESTEB = 'Colegio San Esteban'
    CHILLAN = 'Colegio Chillán'
    CREACION = 'Colegio Creación'
    BICENTEP = 'Liceo Bicentenario E.P.'
    SAGRADOCOR = 'Colegio Sagrado Corazón de J.'
    CESB = 'CESB-Colegio Tecnico Profesional P. Enrique'
    SYDNEY = 'Colegio Sydney College'
    DARIOSAL = 'Colegio Tecnológico Darío Salas'
    DAVINCI = 'Colegio Da Vinci'
    SANFERNANDO = 'Colegio San Fernando'
    DINABEC = 'Dinabec College'
    SANAGUST = 'Colegio San Agustín'
    POLIVPHURT = 'C. Polivalente Padre A. Hurtado'
    ALCAZARES = 'Colegio Alcázares de Ñuble'
    LICNARCISO = 'Liceo Narciso Tondreau'
    DIEGOPORT = 'Liceo Diego Portales Palazuelos'
    CIUDADEDUC = 'Colegio Ciudad Educativa'
    MARTABRUNET = 'Liceo Bicentenario Marta Brunet'
    COMEWEALTH = 'Comewealth School'
    FRANCISOASIS = 'Colegio Francisco de Asis'
    JORGEALESSANDRI = 'Liceo Jorge Alessandri Rodríguez'
    POLIVCARLOS = 'Liceo Polivalente Carlos Montane C.'
    POLIVJUVENAL = 'Liceo Polivalente Juvenal Hernández Jaque'
    COYAM = 'Colegio Coyam'
    INSUCO = 'INSUCO- Instituto Superior de Comercio Insuco'
    ARTPRAT = 'Liceo Arturo Prat Chacón'
    SANTACRUZLARQUI = 'Liceo Santa Cruz de Larqui'
    A17YUNGAY = 'Liceo A-17 Yungay'
    POLITJOSEMANUEL = 'Liceo Politécnico José Manuel P.'
    PUENTENUBLE = 'Liceo Técnico Puente Ñuble'
    DARIOSALAS = 'Colegio Polivalente Darío Salas'
    CHILLANA8 = 'Liceo Agrícola de Chillán A-8'
    PUEBLOSECO = 'Liceo Pueblo Seco'
    POLITCIGN = 'Liceo Politécnico C. Ignacio C.'
    SENORACARMEN = 'Colegio Nuestra Señora del Carmen'
    CLAUDIOARRAU = 'Liceo Claudio Arrau Leon'
    MABELCONDEMARIN = 'Liceo Técnico Mabel Condemarín'
    ALTAZOR = 'Colegio Altazor'
    YIRE = 'Liceo Politécnico Yiré'
    HISPANRIOVIEJO = 'Colegio Hispanoamericano Río Viejo'
    INTECH = 'Intech'
    ARBOLVIDA = 'Colegio El Árbol de la Vida'
    REPUBITALIA = 'Liceo República de Italia'
    ARAUCANA = 'Centro de Estudios la Araucana'
    SENORAMERCED = 'Liceo Nuestra Señora de la Merced'
    SEBASTIANSCHOOL = 'Sebastian School'
    ARTUROPACHECO = 'Liceo Arturo Pacheco Altamirano'
    COLEGIOCONCE = 'Colegio Concepción'
    COLCHOLGUAN = 'Colegio Cholguán'
    INSTSANTMARIA = 'Instituto Santa María'
    SANTTERESALOSANDES = 'Colegio Santa Teresa de los Andes'
    SEMINALBERTOHURT = 'Colegio Seminario Padre Alberto Hurtado'
    COLEGIOS_CHOICES = (
        ('', 'Escoge un colegio...'),
        (SANVICENTE, 'Colegio San Vicente de Paul'),
        (PURISIMA, 'Colegio Purísima Concepción'),
        (SANBUENA, 'Colegio San Buenaventura'),
        (SANESTEB, 'Colegio San Esteban'),
        (CHILLAN, 'Colegio Chillán'),
        (CREACION, 'Colegio Creación'),
        (BICENTEP, 'Liceo Bicentenario E.P.'),
        (SAGRADOCOR, 'Colegio Sagrado Corazón de J.'),
        (CESB, 'CESB-Colegio Tecnico Profesional P. Enrique'),
        (SYDNEY, 'Colegio Sydney College'),
        (DARIOSAL, 'Colegio Tecnológico Darío Salas'),
        (DAVINCI, 'Colegio Da Vinci'),
        (SANFERNANDO, 'Colegio San Fernando'),
        (DINABEC, 'Dinabec College'),
        (SANAGUST, 'Colegio San Agustín'),
        (POLIVPHURT, 'C. Polivalente Padre A. Hurtado'),
        (ALCAZARES, 'Colegio Alcázares de Ñuble'),
        (LICNARCISO, 'Liceo Narciso Tondreau'),
        (DIEGOPORT, 'Liceo Diego Portales Palazuelos'),
        (CIUDADEDUC, 'Colegio Ciudad Educativa'),
        (MARTABRUNET, 'Liceo Bicentenario Marta Brunet'),
        (COMEWEALTH, 'Comewealth School'),
        (FRANCISOASIS, 'Colegio Francisco de Asis'),
        (JORGEALESSANDRI, 'Liceo Jorge Alessandri Rodríguez'),
        (POLIVCARLOS, 'Liceo Polivalente Carlos Montane C.'),
        (POLIVJUVENAL, 'Liceo Polivalente Juvenal Hernández Jaque'),
        (COYAM, 'Colegio Coyam'),
        (INSUCO, 'INSUCO- Instituto Superior de Comercio Insuco'),
        (ARTPRAT, 'Liceo Arturo Prat Chacón'),
        (SANTACRUZLARQUI, 'Liceo Santa Cruz de Larqui'),
        (A17YUNGAY, 'Liceo A-17 Yungay'),
        (POLITJOSEMANUEL, 'Liceo Politécnico José Manuel P.'),
        (PUENTENUBLE, 'Liceo Técnico Puente Ñuble'),
        (DARIOSALAS, 'Colegio Polivalente Darío Salas'),
        (CHILLANA8, 'Liceo Agrícola de Chillán A-8'),
        (PUEBLOSECO, 'Liceo Pueblo Seco'),
        (POLITCIGN, 'Liceo Politécnico C. Ignacio C.'),
        (SENORACARMEN, 'Colegio Nuestra Señora del Carmen'),
        (CLAUDIOARRAU, 'Liceo Claudio Arrau Leon'),
        (MABELCONDEMARIN, 'Liceo Técnico Mabel Condemarín'),
        (ALTAZOR, 'Colegio Altazor'),
        (YIRE, 'Liceo Politécnico Yiré'),
        (HISPANRIOVIEJO, 'Colegio Hispanoamericano Río Viejo'),
        (INTECH, 'Intech'),
        (ARBOLVIDA, 'Colegio El Árbol de la Vida'),
        (REPUBITALIA, 'Liceo República de Italia'),
        (ARAUCANA, 'Centro de Estudios la Araucana'),
        (SENORAMERCED, 'Liceo Nuestra Señora de la Merced'),
        (SEBASTIANSCHOOL, 'Sebastian School'),
        (ARTUROPACHECO, 'Liceo Arturo Pacheco Altamirano'),
        (COLEGIOCONCE, 'Colegio Concepción'),
        (COLCHOLGUAN, 'Colegio Cholguán'),
        (INSTSANTMARIA, 'Instituto Santa María'),
        (SANTTERESALOSANDES, 'Colegio Santa Teresa de los Andes'),
        (SEMINALBERTOHURT, 'Colegio Seminario Padre Alberto Hurtado'),
    )
    colegio = models.CharField(max_length=40, choices=COLEGIOS_CHOICES, blank=True)
    """Carreras"""
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
        ('', 'Escoge una carrera...'),
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
