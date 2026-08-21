# 🚗 Parking Vision AI — Real-Time Parking Space Monitor

![Parking Vision AI Banner](example_no_overlap_hud.png)

Um sistema de **Visão Computacional em Tempo Real** desenvolvido em Python com OpenCV para monitoramento e detecção automática de vagas livres e ocupadas em estacionamentos.

---

## 🌟 Funcionalidades

- **Monitoramento em Tempo Real:** Processamento contínuo de vídeo com taxa de atualização em alta performance rodando 100% em CPU.
- **Interface Gráfica Glassmorphism:** Painel superior no estilo HUD translúcido exibindo total de vagas livres, ocupadas, taxa de ocupação (%) e barra de progresso.
- **Destaque Visual Dinâmico:** Preenchimento semi-transparente (Alpha Blending) e etiquetas de status (`LIVRE` / `OCUPADO`) em cada vaga.
- **Ferramenta de Mapeamento Interativa:** Script dedicado (`ParkingSpacePicker.py`) para cadastrar/remover vagas com cliques do mouse.
- **Persistência de Dados:** Salva as coordenadas das vagas em arquivo binário (`CarParkPos`) para reuso.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **OpenCV (`cv2`):** Processamento Digital de Imagens (Escala de Cinza, Gaussian Blur, Adaptive Threshold, Dilação).
- **Pillow (PIL):** Renderização de tipografia em alta definição (TrueType) e componentes gráficos HUD.
- **NumPy:** Manipulação eficiente de matrizes de imagens.
- **Pickle:** Serialização e persistência de dados das vagas.

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/ParkingSpaces.git
cd ParkingSpaces
```

### 2. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 3. Mapear as vagas de estacionamento (Opcional)
Se desejar adicionar ou remover vagas:
```bash
python ParkingSpacePicker.py
```
- **Botão Esquerdo do Mouse:** Adiciona uma nova vaga.
- **Botão Direito do Mouse:** Remove uma vaga existente.
- **Tecla `q`:** Salva e sai da ferramenta.

### 4. Executar o Monitoramento em Tempo Real
```bash
python main.py
```
- **Tecla `q`:** Encerra a aplicação.

---

## 🔬 Pipeline de Processamento de Imagem

```
Frame Original (BGR)
   │
   ▼
1. cv2.cvtColor ───────► Escala de Cinza
   │
   ▼
2. cv2.GaussianBlur ────► Redução de ruído (3x3)
   │
   ▼
3. cv2.adaptiveThreshold ► Binarização Adaptativa (THRESH_BINARY_INV)
   │
   ▼
4. cv2.medianBlur ──────► Remoção de ruído sal e pimenta (5x5)
   │
   ▼
5. cv2.dilate ──────────► Dilação de bordas (Kernel 3x3)
   │
   ▼
6. cv2.countNonZero ────► Contagem de pixels por Região de Interesse (ROI)
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
