#tokenTelegram= 

#Paso 1. Importar las librerias

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import numpy as np
import tensorflow as tf
import joblib

tokenTelegram=""
#Paso 2. Cargar Modelo 
modelo=tf.keras.models.load_model("modeloRendimiento_Estudiante.h5")
escalamiento=joblib.load("escala.pkl")

#Paso 3. funcion para responder mensajes
async def responder(update:Update, context:ContextTypes.DEFAULT_TYPE):
    try:
        texto=update.message.text
        datos=list(map(float, texto.split(",")))
        #Validacion de la cantidad de datos
        if len(datos) !=4:
            raise ValueError("Los datos estan imcompletos")
        datos=np.array([datos])
        #normalizacion
        datos=escalamiento.transform(datos)

        #PRedicir 
        prediccion=modelo.predict(datos)[0][0]

        #Predicciones
        if prediccion<-0.3:
            resultado="/Rendimiento bajo/"
        elif -0.3<= prediccion<=0.3:
            resultado="/Rendimiento Medio/"
        else:
            resultado="/Rendimiento Alto/"
            
        await(update.message.reply_text(
            f"Resultado {prediccion:.3f} - {resultado}"
            ))
    except Exception as Error:
        await update.message.reply_text("Error en los datos ")

async def iniciar(update:Update, context:ContextTypes.DEFAULT_TYPE):
    mensaj4=("Bienvenido al bot de rendimiento estudiantil - envia en este formmato HORAS, ASISTENCIA,SUEÑO,CELULAR")
    await update.message.reply_text(mensaj4)


#Paso 5. Armar el bot

app=ApplicationBuilder().token(tokenTelegram).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,responder))
app.add_handler(MessageHandler(filters.COMMAND, iniciar))

print("Bot funcionando")
app.run_polling()

