import os
import tkinter


from factories.model import model_creator, model_save, model_load, model_predict
from helpers.datasetHandler import get_dataset
from helpers.scraping import scrape
from tkinter import filedialog


def openFile(display_text):
    filePath = filedialog.askopenfilename(title=display_text)

    return filePath


while True:
    escolha = input("""
para criar e treinar um novo modelo digite: [criar]
para carregar um modelo e fazer predições digite: [iniciar] 
para sair escreva: [sair]
""")
    match escolha:
        case "criar":
            print("você escolheu criar um novo modelo")
            train_ds, val_ds, class_names = get_dataset(
                'datasets', 224, 224, 32)

            model = model_creator(len(class_names))

            model.fit(
                train_ds,
                batch_size=32,
                epochs=3,
                validation_data=val_ds)

            model_save(model, input("digite um nome para salvar o modelo: \n"))

        case "iniciar":
            print("você escolheu carregar um modelo e fazer predições")

            model_choice = openFile("Escolha o modelo para carregar.")
            model = model_load(model_choice)
            image = openFile("Escolha a imagem.")
            classes = os.listdir("datasets")[::-1]
            item = model_predict(model, image, classes)
            scrape(item)

        case "sair":
            break
