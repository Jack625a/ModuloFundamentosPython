#Modelos multimodales combinado con modelos propios

#apiGoogle=""

from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler,filters,ContextTypes
import tensorflow as tf
import numpy as np
import joblib
from google import genai
import logging


apiGoogle=""
tokenTelegram=""

logging.basicConfig(level=logging.INFO)

#Configuracion del modelo multimodal
cliente=genai.Client(api_key=apiGoogle)

#Cargar el modelo propio
modelo=tf.keras.models.load_model("modeloRendimiento_Estudiante.h5")
escala=joblib.load("escala.pkl")



#Funciones extra
def validar_entradaDatos(texto):
    try:
        datos=list(map(float,texto.split(",")))
        if len(datos)!=4:
            return None
        return datos
    except:
        return None

def clasificacionNiveles(prediccion):
    if prediccion<-0.3:
        return "BAJO"
    elif prediccion <=0.3:
        return "MEDIO"
    else:
        return "ALTO"

def prompt(datos,nivel):
    return f""" 
        Eres un asesor academico profesional
        Analiza el rendimiento academico de un estudiante con esto datos
        -Horas de Estudio
        -Asistencia a Clases (0 a 100)
        -Nivel de sueño(0 a 10)
        -Uso del celular(0 a 10)
    Datos: {datos}
    Nivel Detectado: {nivel}

    Responde en este formato:
    1. Diagnostico breve
    2. Problemas detectados
    3. Recomendaciones practicas

"""

#Funcion Principal Responder

async def responder(update:Update,context:ContextTypes.DEFAULT_TYPE):
    texto=update.message.text
    datos=validar_entradaDatos(texto)
    if not datos:
        await update.message.reply_text("Error formato incorrecto. \nEjemplo Valido 8,90,5,6")
        return
    
    try:
        
        
        datosConvertidos=np.array([datos])

        #Normalizar
        datosNormalizados=escala.transform(datosConvertidos)

        #Prediccion
        prediccion=modelo.predict(datosNormalizados)[0][0]
        nivel=clasificacionNiveles(prediccion)

        indicacion=prompt(datos,nivel)
        
        
        respuesta=cliente.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=indicacion
        )

        mensaje=f"""RESULTADO: {nivel}  
        RECOMENDACION: {respuesta.text}        
        """

        await update.message.reply_text(mensaje,parse_mode="Markdown")
    except Exception as error:
        logging.error(f"Error: {error}")
        await update.message.reply_text("Error al procesar")


app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(MessageHandler(filters.TEXT,responder))
app.run_polling()