# 🚗 Parking Vision AI — Real-Time Parking Space Monitor

![Parking Vision AI Banner](demo.gif)

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

## 📌 Próximos Passos & Limitações no Mundo Real

Este projeto foi desenvolvido com foco em **estudo prático e validação de conceitos de Visão Computacional**. Sabendo que em cenários reais dificilmente teremos uma câmera perfeitamente posicionada no topo com iluminação constante, o projeto serve como excelente base para evolução contínua.

### 🚀 O que pode ser aprimorado no futuro (Roadmap):

- [ ] **Suporte a Câmeras em Perspectiva:** Substituir retângulos fixos por polígonos/máscaras dinâmicas (`cv2.fillPoly`) para adaptar a detecção a câmeras em ângulos inclinados.
- [ ] **Calibração Dinâmica de Iluminação:** Implementar ajuste automático de threshold para responder a mudanças de luz (sombras de nuvens, períodos noturnos ou chuva).
- [ ] **Evolução para Aprendizado de Máquina (AI/ML):** Integrar modelos de detecção de objetos como **YOLOv8** para classificar veículos de forma independente da posição da câmera.
- [ ] **Integração com API / Painel Web:** Enviar os dados de vagas em tempo real via API (FastAPI/Flask) para consumo em dashboards web ou painéis do estacionamento.

## Contato

- LinkedIn:https://www.linkedin.com/in/arthur-kean-5458352bb/

