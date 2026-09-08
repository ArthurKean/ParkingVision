# 🚗 Parking Vision AI

![Parking Vision AI Banner](demo.gif)

Projeto em Python e OpenCV para identificar vagas livres e ocupadas em um vídeo de estacionamento.

As vagas são marcadas manualmente, e o sistema analisa essas regiões a cada frame para estimar a ocupação. O resultado aparece no próprio vídeo, com cores, etiquetas e um painel com os totais.

Desenvolvi este projeto para colocar em prática conceitos de visão computacional, desde o tratamento da imagem até a construção da interface de monitoramento.

## O que o projeto faz

- Processa o vídeo continuamente usando a CPU.
- Destaca cada vaga com uma cor e a indicação `LIVRE` ou `OCUPADO`.
- Exibe o total de vagas livres, ocupadas e a porcentagem de ocupação.
- Permite adicionar e remover vagas com o mouse.
- Salva o mapeamento para reutilizá-lo nas próximas execuções.

A interface usa um painel translúcido e preenchimentos semitransparentes para mostrar as informações sobre o vídeo.

## Tecnologias

- **Python 3.13**
- **OpenCV:** processamento dos frames e análise das vagas.
- **NumPy:** manipulação das imagens como matrizes.
- **Pillow:** renderização de textos e elementos do painel.
- **Pickle:** armazenamento das coordenadas no arquivo `CarParkPos`.

## Como funciona

A detecção usa processamento de imagem e contagem de pixels nas regiões mapeadas.

Cada frame passa pelas seguintes etapas:

```text
Frame original
    ↓
Conversão para escala de cinza
    ↓
Gaussian Blur (3×3)
    ↓
Threshold adaptativo invertido
    ↓
Filtro de mediana (5×5)
    ↓
Dilatação com kernel 3×3
    ↓
Contagem de pixels em cada vaga
    ↓
Classificação: livre ou ocupada
```

A contagem é feita com `cv2.countNonZero` na região de cada vaga. Essa informação é usada para definir o status e atualizar o painel.

## Como executar

Com o repositório baixado, abra um terminal na pasta do projeto.

### 1. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 2. Ajuste o mapeamento, se necessário

Para adicionar ou remover vagas:

```bash
python ParkingSpacePicker.py
```

- **Clique esquerdo:** adiciona uma vaga.
- **Clique direito:** remove uma vaga existente.

As coordenadas ficam salvas no arquivo `CarParkPos`.

### 3. Inicie o monitoramento

```bash
python main.py
```

## Limitações

O projeto foi desenvolvido como exercício prático de visão computacional. A abordagem atual depende do posicionamento da câmera e das condições de iluminação.

Como a classificação usa a contagem de pixels, sombras, chuva e mudanças de luz podem interferir no resultado. As vagas também são representadas por retângulos fixos, o que limita o uso com câmeras inclinadas.

Para utilizar outro vídeo ou enquadramento, pode ser necessário refazer o mapeamento e ajustar os parâmetros de detecção.

## Próximos passos

- [ ] Mapear vagas com polígonos para acompanhar melhor a perspectiva da câmera.
- [ ] Adaptar os parâmetros de detecção às mudanças de iluminação.
- [ ] Testar a detecção de veículos com YOLOv8.
- [ ] Disponibilizar os dados de ocupação por uma API.
- [ ] Criar um painel web para acompanhar o estacionamento.

## Contato

- [E-mail](mailto:Keanulisses@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/arthur-kean-5458352bb/)


