#Modelos multimodales combinado con modelos propios

#apiGoogle=""

from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler,filters,ContextTypes
import tensorflow as tf
import numpy as np
import joblib
from google import genai


apiGoogle=""
tokenTelegram=""
#Configuracion del modelo multimodal
cliente=genai.Client(api_key=apiGoogle)

#Cargar el modelo propio
modelo=tf.keras.models.load_model("modeloRendimiento_Estudiante.h5")
escala=joblib.load("escala.pkl")

#Funcion Principal Responder

async def responder(update:Update,context:ContextTypes.DEFAULT_TYPE):
    try:
        texto=update.message.text
        datos=list(map(float,texto.split(",")))
        datosConvertidos=np.array([datos])

        #Normalizar
        datosNormalizados=escala.transform(datosConvertidos)

        #Prediccion
        prediccion=modelo.predict(datosNormalizados)[0][0]

        #Escalas
        if prediccion <-0.3:
            nivel="BAJO"
        elif prediccion<=0.3:
            nivel="MEDIO"
        else: 
            nivel="ALTO"
        
        #iNDICACION
        prompt=f"""Analiza el rendimiento de un estudiantes
            En base a estos datos de tipo variables:
            horas de estudio rango por horas
            asistencia a Clases rango de (0 a 100)
            niveles de Sueño rango (0 a 10)
            uso Celular  rango (0 a 10)
            Datos: {datos}
            Resultados: {nivel}

            Explica y da tus recomendaciones practicas al estudiante
        """
        respuesta=cliente.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=prompt
        )

        mensaje=f"""RESULTADO: {nivel}  
        RECOMENDACION: {respuesta.text}        
        """

        await update.message.reply_text(mensaje)
    except:
        await update.message.reply_text("Error al procesar")


app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(MessageHandler(filters.TEXT,responder))
app.run_polling()