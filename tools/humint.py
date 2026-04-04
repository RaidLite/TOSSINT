from pystyle import Colorate, Colors

def gradient(text):
    print(Colorate.Vertical(Colors.red_to_yellow, text))

def humint_manual():
    gradient("""
================================================================================
[!] PROTOCOLO HUMINT: EL FACTOR HUMANO - MANUAL DE CAMPO (MODO SOMBRA)
================================================================================
"El cifrado de 256 bits es inútil si puedes convencer al administrador de que 
 te abra la puerta por un café y una sonrisa. El hardware se rompe, el software
 se parchea, pero el ADN humano... ese siempre tiene la misma vulnerabilidad."

0. LA FILOSOFÍA DEL RECONOCIMIENTO
--------------------------------------------------------------------------------
El HUMINT (Human Intelligence) no es solo hablar; es el arte de la infiltración 
psicológica. En un mundo de firewalls, el humano es el eslabón más débil. 
Tu objetivo no es hackear la máquina, es hackear la percepción de la víctima.

1. INGENIERÍA SOCIAL ESTRATÉGICA (THE PRETEXT)
--------------------------------------------------------------------------------
* Creación de Identidades Sintéticas: No mientas, construye una verdad paralela.
  Si vas como técnico de sistemas, conoce el modelo exacto de los servidores.
* El Principio de Invisibilidad: No te vistas para destacar, vístete para ser 
  ignorado. Un chaleco reflectante y una caja de herramientas te dan acceso al 
  90% de los edificios del mundo. Nadie cuestiona al hombre que viene a arreglar
  algo que está roto.
* Mimetismo Cultural: Aprende la jerga interna. No digas "la oficina de arriba", 
  di "la planta 4, sección de logística".

2. TÉCNICAS DE ELICITACIÓN (EXTRACCIÓN INVISIBLE)
--------------------------------------------------------------------------------
* La Técnica de la Corrección: La gente tiene una necesidad patológica de 
  corregir a los demás. Di algo erróneo deliberadamente ("Escuché que vuestro 
  servidor principal es un Windows 2012..."). La víctima te corregirá con 
  detalles técnicos reales para demostrar su conocimiento.
* El Quid Pro Quo Silencioso: Ofrece una confidencia falsa ("Mi jefe es un idiota, 
  me tiene aquí revisando cables...") para que el otro baje la guardia y 
  te cuente sus propias frustraciones laborales.
* Escucha Activa Reflejada: Repite las últimas tres palabras de lo que diga el 
  objetivo. Eso los incita a seguir hablando y dando detalles sin que preguntes.

3. INFILTRACIÓN FÍSICA (ESTILO MR. ROBOT)
--------------------------------------------------------------------------------
* Tailgating (Seguimiento): Espera en la zona de fumadores. Entra justo detrás 
  de alguien con las manos ocupadas. Por cortesía social, te aguantarán la puerta. 
  La cortesía es tu exploit.
* Shoulder Surfing Pro: No mires solo el teclado. Mira las fotos en los 
  escritorios (nombres de hijos/perros = posibles contraseñas), notas 
  adhesivas bajo el teclado y el nivel de acceso en las tarjetas de identificación.
* Dumpster Diving (Buceo de basura): Los post-its, las agendas viejas y las 
  guías telefónicas internas suelen terminar en la basura sin triturar. 
  Ahí reside el mapa de la infraestructura humana.

4. DISPARADORES PSICOLÓGICOS (THE HACKS)
--------------------------------------------------------------------------------
* Autoridad: Una voz firme, un portapapeles y una mirada de "estoy ocupado" 
  anulan el pensamiento crítico de la seguridad básica.
* Urgencia Artificial: "Si no arreglo esto en 10 minutos, toda la red se cae". 
  El miedo al fracaso hace que la gente ignore los protocolos de seguridad.
* Simpatía/Validación: Haz que se sientan importantes. A la gente que se siente 
  infravalorada (guardias, recepcionistas) le encanta ayudar a quien los trata 
  como expertos.

5. EXFILTRACIÓN Y BORRADO DE HUELLAS
--------------------------------------------------------------------------------
* Nunca salgas corriendo. Sal con la misma calma con la que entraste.
* Si te interceptan: Mantén tu 'Pretext'. Una buena historia de cobertura tiene 
  una salida lógica ("Me equivoqué de planta, el de mantenimiento me dijo 
  que era aquí").
* Pivotaje a OSINT: Cada nombre, marca de impresora o versión de software 
  obtenida debe ser cruzada con LinkedIn, Shodan y GitHub.

"No estás aquí para destruir. Estás aquí para demostrar que nada es seguro."
================================================================================
""")