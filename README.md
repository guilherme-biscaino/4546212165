# Projeto de Transfer Learning para Reconhecimento de Imagens e Web Scraping

Este projeto utiliza o processo de Transfer Learning em um modelo convolucional para reconhecer imagens de produtos e realizar web scraping no Google para retornar os sites de produtos relacionados. O modelo foi treinado utilizando um dataset personalizado feito à mão, contendo imagens de diversos produtos.

## Objetivo

O principal objetivo deste projeto é desenvolver um sistema que consiga identificar produtos a partir de imagens enviadas e, em seguida, realizar uma pesquisa na web para encontrar sites que contenham informações sobre esses produtos. O processo é dividido em duas etapas principais:

1. **Reconhecimento de Imagens**: Utilizando Transfer Learning, um modelo pré-treinado é ajustado para identificar categorias de produtos específicas.
2. **Web Scraping**: Após a classificação da imagem, o modelo realiza uma pesquisa no Google para coletar URLs de sites relevantes que vendem ou fornecem informações sobre o produto.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **TensorFlow/Keras**: Framework utilizado para implementar o modelo convolucional e aplicar Transfer Learning.
- **Pillow**: Biblioteca utilizadas para pré-processamento e manipulação de imagens.
- **Selenium**: Bibliotecas para realizar o web scraping no Google e coletar URLs dos produtos.

## Como Funciona

1. **Pré-processamento de Imagens**:
   - As imagens são redimensionadas e normalizadas para se ajustarem ao modelo.
   - As imagens do dataset são rotuladas conforme as categorias: **ball**, **smartphone**, **teddy_bear**, **toothbrush**, **wristwatch**.

2. **Transfer Learning**:
   - Um modelo convolucional pré-treinado (por exemplo, ResNet50, VGG16, etc.) é carregado e adaptado para o novo problema, ajustando-se às categorias do dataset.
   - Nesse caso usamos o modelo MobileNetV2 por ser menor e menos custoso porém não apresentou desempenho agradável.
   - O modelo é treinado usando as imagens do dataset personalizado, permitindo a classificação de novos produtos.

3. **Web Scraping**:
   - Após a classificação de um produto a partir de uma imagem, o modelo usa o nome da categoria para realizar uma busca na web.
   - O sistema retorna uma lista de URLs de sites relacionados ao produto, que são então exibidos para o usuário.

## Dataset

O projeto utiliza o seguinte dataset, composto por imagens feitas à mão:

- **ball**: Imagens de bolas de diferentes tipos (futebol, basquete, etc.).
- **smartphone**: Imagens de smartphones variados.
- **teddy_bear**: Imagens de ursinhos de pelúcia.
- **toothbrush**: Imagens de escovas de dente.
- **wristwatch**: Imagens de relógios de pulso.

O dataset foi coletado manualmente e organizado para treinar o modelo de reconhecimento de imagens.

(i know that smartphone is wrongly misspelled as "smarthphone" in the dataset folder and i'm ashamed of it)
