import streamlit as st
import streamlit.components.v1 as components

# Configuração da Página
st.set_page_config(page_title="20 Jogos de Biologia pro ENEM", page_icon="🧬", layout="wide")

st.title("🧬 20 Jogos & Simuladores Interativos de Biologia pro ENEM")
st.write("Aprenda os assuntos de Biologia mais cobrados no ENEM manipulando modelos e simulações em tempo real!")

# Menu Lateral
st.sidebar.header("🕹️ Selecione o Jogo (1 a 20)")
jogo = st.sidebar.radio("Módulos Interativos:", [
    "01. Osmose & Membrana Plasmática",
    "02. Organelas Celulares & Funções",
    "03. Síntese Proteica (DNA ➔ RNA ➔ Proteína)",
    "04. Divisão Celular (Mitose vs Meiose)",
    "05. 1ª Lei de Mendel & Quadro de Punnett",
    "06. Heredogramas & Doenças Genéticas",
    "07. Tipagem Sanguínea (ABO e Fator Rh)",
    "08. Biotecnologia (Transgênicos & Clonagem)",
    "09. Fluxo de Energia & Pirâmide Trófica",
    "10. Relações Ecológicas (Interações)",
    "11. Ciclo do Nitrogênio & Bactérias",
    "12. Impactos Ambientais (Eutrofização)",
    "13. Evolução (Seleção Natural x Lamarck)",
    "14. Anatomia Comparada (Homologia vs Analogia)",
    "15. Sistema Digestório & pH das Enzimas",
    "16. Sistema Circulatório (Grande & Pequena)",
    "17. Imunologia (Vacina vs Soro)",
    "18. Controle da Glicemia (Insulina x Glucagon)",
    "19. Botânica (Grupos Vegetais)",
    "20. Parasitologia & Doenças do ENEM"
])

st.sidebar.divider()
st.sidebar.caption("🎯 **Dica ENEM:** Interaja com as simulações e grave os conceitos-chave de cada tema!")

# =============================================================================
# 01. OSMOSE
# =============================================================================
if jogo == "01. Osmose & Membrana Plasmática":
    st.subheader("💧 01. Osmose: Comportamento Celular em Meios Diferentes")
    st.success("🎯 **O que fazer:** Aumente a salinidade (concentração) do meio extracelular e veja a água sair da célula, fazendo-a murchar (Plasmólise)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">🧂 Salinidade Externa: <input type="range" id="s" min="1" max="5" value="3" oninput="u()"> <span id="sv">Hipertônico</span></div>
        <canvas id="c" width="450" height="130" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function u(){
                let val = parseInt(document.getElementById('s').value);
                let txt = val > 3 ? "HIPERTÔNICO (Célula Murcha)" : val < 3 ? "HIPOTÔNICO (Célula Incha)" : "ISOTÔNICO (Equilíbrio)";
                document.getElementById('sv').innerText = txt;
            }
            function d(){
                ctx.clearRect(0,0,450,130);
                let val = parseInt(document.getElementById('s').value);
                let r = 50 - (val - 3) * 10;
                ctx.fillStyle="#ff4b4b"; ctx.beginPath(); ctx.arc(225,65,r,0,Math.PI*2); ctx.fill();
                ctx.fillStyle="#fff"; ctx.fillText("Hemácia", 205, 70);
                requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** Osmose é o transporte passivo da água do meio **HIPOTÔNICO** (menos concentrado) para o meio **HIPERTÔNICO** (mais concentrado) sem gastar ATP!")

# =============================================================================
# 02. ORGANELAS CELULARES
# =============================================================================
elif jogo == "02. Organelas Celulares & Funções":
    st.subheader("🔬 02. Identificador de Organelas Celulares")
    st.success("🎯 **O que fazer:** Selecione uma organela celular para entender sua função vital e como ela é cobrada na prova de Ciências da Natureza!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Organela: 
            <select id="o" onchange="u()">
                <option value="Mitocôndria ➔ Respiração Celular e produção de energia (ATP).">Mitocôndria</option>
                <option value="Ribossomo ➔ Síntese de proteínas (presente em procariontes e eucariontes).">Ribossomo</option>
                <option value="Complexo de Golgi ➔ Secreção celular, empacotamento e formação do acrossomo do espermatozoide.">Complexo de Golgi</option>
                <option value="Lisossomo ➔ Digestão intracelular e autofagia.">Lisossomo</option>
                <option value="Retículo Endoplasmático Liso ➔ Síntese de lipídios e desintoxicação celular.">Retículo Liso</option>
                <option value="Cloroplasto ➔ Fotossíntese em células vegetais e algas.">Cloroplasto</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border:1px solid #7ee787;"><b id="out" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('out').innerText = document.getElementById('o').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Células que consomem muita energia (ex: células musculares e espermatozoides) possuem uma quantidade elevadíssima de **Mitocôndrias**!")

# =============================================================================
# 03. SÍNTESE PROTEICA
# =============================================================================
elif jogo == "03. Síntese Proteica (DNA ➔ RNA ➔ Proteína)":
    st.subheader("🧬 03. Transcrição e Tradução do DNA")
    st.success("🎯 **O que fazer:** Veja o pareamento de bases nitrogenadas no RNAm: Adenina ($A$) liga com Uracila ($U$) e Citosina ($C$) liga com Guanina ($G$).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">Fita de DNA: <b>A - T - C - G</b></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b style="color:#58a6ff;">RNAm Transcrito: U - A - G - C</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** No RNA **NÃO EXISTE Timina ($T$)**, ela é substituída pela **Uracila ($U$)**! A transcrição ocorre no núcleo e a tradução ocorre no citoplasma (ribossomo).")

# =============================================================================
# 04. DIVISÃO CELULAR
# =============================================================================
elif jogo == "04. Divisão Celular (Mitose vs Meiose)":
    st.subheader("✂️ 04. Mitose vs Meiose")
    st.success("🎯 **O que fazer:** Escolha o tipo de divisão para ver o número final de células-filhas e a quantidade de cromossomos!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('out').innerText='MITOSE: 1 célula 2n ➔ 2 células 2n IDÊNTICAS (Crescimento e Regeneração)'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">Mitose</button>
            <button onclick="document.getElementById('out').innerText='MEIOSE: 1 célula 2n ➔ 4 células n COM VARIABILIDADE (Formação de Gametas)'" style="background:#da3633; color:white; border:none; padding:8px; border-radius:4px;">Meiose</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #e3b341;"><b id="out" style="color:#e3b341;">Clique acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** O *Crossing-over* (recombinação gênica) ocorre na **Prófase I da Meiose** e é a principal fonte de variabilidade genética!")

# =============================================================================
# 05. 1ª LEI DE MENDEL
# =============================================================================
elif jogo == "05. 1ª Lei de Mendel & Quadro de Punnett":
    st.subheader("🌱 05. Cruzamento Monohíbrido (Aa x Aa)")
    st.success("🎯 **O que fazer:** Veja o cruzamento genético entre dois heterozigotos e as proporções genotípicas resultantes.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            <b>Cruzamento Aa x Aa:</b><br>
            AA (25%) | Aa (50%) | aa (25%)
        </div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #7ee787;"><b style="color:#7ee787;">Proporção Fenotípica: 3 Dominantes (75%) : 1 Recessivo (25%)</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** No cruzamento entre dois heterozigotos ($Aa \\times Aa$), a proporção fenotípica clássica é sempre **3 : 1** (75% dominante e 25% recessivo).")

# =============================================================================
# 06. HEREDOGRAMAS
# =============================================================================
elif jogo == "06. Heredogramas & Doenças Genéticas":
    st.subheader("👨‍👩‍👧‍👦 06. Leitura e Análise de Heredogramas")
    st.success("🎯 **O que fazer:** Descubra o padrão de herança de uma doença analisando a descendência dos pais!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <b>Regra de Ouro:</b><br>
            Pais IGUAIS com filho DIFERENTE ➔ O filho é RECESSIVO (aa) e os pais são HETEROZIGOTOS (Aa)!
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** Quadrado = Homem, Círculo = Mulher. Símbolo pintado = Indivíduo afetado pela característica analisada.")

# =============================================================================
# 07. TIPAGEM SANGUÍNEA
# =============================================================================
elif jogo == "07. Tipagem Sanguínea (ABO e Fator Rh)":
    st.subheader("🩸 07. Transfusão de Sangue e Compatibilidade")
    st.success("🎯 **O que fazer:** Selecione o tipo de sangue do doador para verificar quem pode receber a doação com segurança!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #da3633; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Sangue Doador: 
            <select id="s" onchange="u()">
                <option value="O negativo (O-) ➔ DOADOR UNIVERSAL (Não tem aglutinogênios A, B nem Rh).">O-</option>
                <option value="AB positivo (AB+) ➔ RECEPTOR UNIVERSAL (Não possui aglutininas no plasma).">AB+</option>
                <option value="A positivo (A+) ➔ Pode doar para A+ e AB+.">A+</option>
                <option value="B positivo (B+) ➔ Pode doar para B+ e AB+.">B+</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #da3633;"><b id="out" style="color:#da3633;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('out').innerText = document.getElementById('s').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Sangue **O-** é o doador universal. Sangue **AB+** é o receptor universal. Eritroblastose fetal ocorre em mãe $Rh^-$ com feto $Rh^+$.")

# =============================================================================
# 08. BIOTECNOLOGIA
# =============================================================================
elif jogo == "08. Biotecnologia (Transgênicos & Clonagem)":
    st.subheader("🧬 08. Engenharia Genética e Biotecnologia")
    st.success("🎯 **O que fazer:** Entenda as diferenças entre Organismos Transgênicos, Clonagem e Testes de DNA por PCR.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('o').innerText='TRANSGÊNICO: Recebe um gene de OUTRA espécie usando enzimas de restrição (Ex: Soja resistente a pragas)'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">1. Transgênico</button>
            <button onclick="document.getElementById('o').innerText='CLONAGEM: Cópia geneticamente IDÊNTICA. Usa-se o núcleo de uma célula somática (Ex: Ovelha Dolly)'" style="background:#58a6ff; color:white; border:none; padding:8px; border-radius:4px;">2. Clonagem</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border:1px solid #7ee787;"><b id="o" style="color:#7ee787;">Clique acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** **Enzimas de Restrição** atuam como 'tesouras moleculares' cortando o DNA em pontos específicos para a produção de recombinantes!")

# =============================================================================
# 09. FLUXO DE ENERGIA
# =============================================================================
elif jogo == "09. Fluxo de Energia & Pirâmide Trófica":
    st.subheader("🍃 09. Perda de Energia na Cadeia Alimentar")
    st.success("🎯 **O que fazer:** Veja por que a energia DIMINUI ao longo dos níveis tróficos (apenas ~10% passa para o próximo nível!).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            🌱 Produtor (Planta): <b>10.000 kcal</b> ➔ <br>
            🦗 Consumidor 1º (Gafanhoto): <b>1.000 kcal</b> ➔ <br>
            🐸 Consumidor 2º (Sapo): <b>100 kcal</b>
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** O fluxo de energia na cadeia alimentar é **UNIDIRECIONAL e DECRESCENTE**. Já a matéria é reciclada pelos decompositores!")

# =============================================================================
# 10. RELAÇÕES ECOLÓGICAS
# =============================================================================
elif jogo == "10. Relações Ecológicas (Interações)":
    st.subheader("🐝 10. Interações Ecológicas Entre Espécies")
    st.success("🎯 **O que fazer:** Classifique as relações ecológicas em Harmônicas (sem prejuízo) ou Desarmônicas (com prejuízo).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Relação: 
            <select id="r" onchange="u()">
                <option value="Mutualismo (+/+) ➔ Ambas se beneficiam e a relação é OBRIGATÓRIA (Ex: Liquens).">Mutualismo</option>
                <option value="Protocooperação (+/+) ➔ Ambas se beneficiam, mas NÃO é obrigatória (Ex: Pássaro-palito e crocodilo).">Protocooperação</option>
                <option value="Comensalismo (+/0) ➔ Uma se beneficia em busca de alimento sem prejudicar a outra (Ex: Rêmora e tubarão).">Comensalismo</option>
                <option value="Parasitismo (+/-) ➔ Uma vive à custa do hospedeiro, prejudicando-o (Ex: Lombriga).">Parasitismo</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="o" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('o').innerText = document.getElementById('r').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** **Intraespecífica** ocorre entre indivíduos da mesma espécie (ex: Sociedades e Colônias). **Interespecífica** ocorre entre espécies diferentes!")

# =============================================================================
# 11. CICLO DO NITROGÊNIO
# =============================================================================
elif jogo == "11. Ciclo do Nitrogênio & Bactérias":
    st.subheader("🌱 11. Etapas do Ciclo do Nitrogênio")
    st.success("🎯 **O que fazer:** Veja o papel crucial das bactérias para transformar $N_2$ atmosférico em Nitrato assimilável pelas plantas.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            N2 (Gás) ➔ Fixação (Rhizobium) ➔ Amônia ➔ Nitritação ➔ Nitratação (Nitrato) ➔ Absorção vegetal
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** A rotação de culturas usando **leguminosas** (ex: feijão, soja) enriquece o solo com nitrogênio natural graças às bactérias *Rhizobium* nas suas raízes!")

# =============================================================================
# 12. EUTROFIZAÇÃO
# =============================================================================
elif jogo == "12. Impactos Ambientais (Eutrofização)":
    st.subheader("🌊 12. Etapas da Eutrofização em Lagos")
    st.success("🎯 **O que fazer:** Observe a sequência de eventos desencadeada pelo despejo de esgoto/fertilizantes na água!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            Esgoto na água ➔ Proliferação de Algas na superfície ➔ Bloqueio da Luz Solar ➔ Morte de plantas submersas ➔ Proliferação de bactérias decompositoras ➔ Queda do $O_2$ ➔ Morte de peixes.
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** A eutrofização reduz dramaticamente o oxigênio dissolvido ($O_2$) na água devido ao pico de decomposição aeróbica!")

# =============================================================================
# 13. EVOLUÇÃO
# =============================================================================
elif jogo == "13. Evolução (Seleção Natural x Lamarck)":
    st.subheader("🦒 13. Darwinismo vs Lamarckismo")
    st.success("🎯 **O que fazer:** Compare a teoria da Seleção Natural (Darwin) com a teoria do Uso e Desuso (Lamarck).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('o').innerText='DARWIN: A natureza seleciona os indivíduos MAIS APTOS já existentes (Seleção Natural)'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">1. Darwinismo</button>
            <button onclick="document.getElementById('o').innerText='LAMARCK: Lei do Uso e Desuso + Transmissão dos caracteres adquiridos (INCORRETO!)'" style="background:#da3633; color:white; border:none; padding:8px; border-radius:4px;">2. Lamarckismo</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #e3b341;"><b id="o" style="color:#e3b341;">Clique acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** O meio ambiente **NÃO MODIFICA** o indivíduo para ele se adaptar (Lamarck). O meio **SELECIONA** as variações mais vantajosas já existentes (Darwin)!")

# =============================================================================
# 14. ANATOMIA COMPARADA
# =============================================================================
elif jogo == "14. Anatomia Comparada (Homologia vs Analogia)":
    st.subheader("🦅 14. Órgãos Homólogos vs Análogos")
    st.success("🎯 **O que fazer:** Aprenda a diferença entre ancestralidade comum (Divergência) e adaptação ao mesmo meio (Convergência).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('o').innerText='HOMÓLOGOS: Mesma origem embrionária (Ex: Braço humano e asa de morcego) ➔ Divergência Evolutiva'" style="background:#58a6ff; color:white; border:none; padding:8px; border-radius:4px;">Homologia</button>
            <button onclick="document.getElementById('o').innerText='ANÁLOGOS: Mesma função, origens DIFERENTES (Ex: Asa de ave e asa de inseto) ➔ Convergência Evolutiva'" style="background:#f0883e; color:white; border:none; padding:8px; border-radius:4px;">Analogia</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border:1px solid #7ee787;"><b id="o" style="color:#7ee787;">Clique acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** **Homologia** = Mesma estrutura/origem (mesmo ancestral). **Analogia** = Mesma função adaptativa (origens diferentes).")

# =============================================================================
# 15. SISTEMA DIGESTÓRIO
# =============================================================================
elif jogo == "15. Sistema Digestório & pH das Enzimas":
    st.subheader("🍕 15. Enzimas Digestivas e pH Ideal")
    st.success("🎯 **O que fazer:** Veja o pH ideal de atuação das principais enzimas ao longo do trato digestivo!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">👄 Boca (Ptialina): pH neutro (~7.0) ➔ Digestão de Amido</div><br>
        <div class="card">🧪 Estômago (Pepsina): pH altamente ácido (~2.0) ➔ Digestão de Proteínas</div><br>
        <div class="card">🥖 Intestino Delgado (Tripsina): pH básico (~8.0) ➔ Digestão de Lipídios e Proteínas</div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** A **Bile** produzida pelo fígado e armazenada na vesícula biliar **NÃO POSSUI ENZIMAS**; ela apenas emulsifica gorduras (funciona como detergente)!")

# =============================================================================
# 16. SISTEMA CIRCULATÓRIO
# =============================================================================
elif jogo == "16. Sistema Circulatório (Grande & Pequena)":
    st.subheader("🫀 16. Pequena e Grande Circulação Sangue")
    st.success("🎯 **O que fazer:** Acompanhe o trajeto do sangue venoso (rico em $CO_2$) e arterial (rico em $O_2$).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            🔵 <b>Pequena Circulação (Pulmonar):</b> Coração ➔ Pulmões (Hematose) ➔ Coração<br><br>
            🔴 <b>Grande Circulação (Sistêmica):</b> Coração ➔ Tecidos do Corpo ➔ Coração
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** **Artérias** saem do coração levando sangue sob alta pressão. **Veias** chegam ao coração conduzindo o retorno sanguíneo!")

# =============================================================================
# 17. IMUNOLOGIA
# =============================================================================
elif jogo == "17. Imunologia (Vacina vs Soro)":
    st.subheader("💉 17. Vacina vs Soro Terapêutico")
    st.success("🎯 **O que fazer:** Descubra quando usar Vacina (Prevenção) e quando usar Soro (Tratamento de emergência)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('o').innerText='VACINA: Imunização ATIVA (Contém Antígenos atenuados/mortos) ➔ Estimula o corpo a criar anticorpos e células de memória.'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">Vacina (Preventiva)</button>
            <button onclick="document.getElementById('o').innerText='SORO: Imunização PASSIVA (Contém Anticorpos prontos) ➔ Ação rápida para emergências (Ex: Picada de cobra)'" style="background:#da3633; color:white; border:none; padding:8px; border-radius:4px;">Soro (Curativo)</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="o" style="color:#7ee787;">Clique acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Vacinas geram **memória imunológica** de longo prazo. Soros fornecem anticorpos prontos e temporários sem gerar memória!")

# =============================================================================
# 18. CONTROLE DA GLICEMIA
# =============================================================================
elif jogo == "18. Controle da Glicemia (Insulina x Glucagon)":
    st.subheader("🍬 18. Regulação do Açúcar no Sangue")
    st.success("🎯 **O que fazer:** Aumente ou diminua a taxa de glicose e veja a atuação dos hormônios pancreáticos.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            <b>Alta Glicose (Pós-refeição)</b> ➔ Pâncreas libera <b>INSULINA</b> ➔ Armazena Glicogênio no fígado.<br><br>
            <b>Baixa Glicose (Jejum)</b> ➔ Pâncreas libera <b>GLUCAGON</b> ➔ Quebra Glicogênio e libera glicose.
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** A **Insulina** coloca glicose para DENTRO das células (reduz glicemia). O **Glucagon** tira glicose do fígado para o sangue (aumenta glicemia)!")

# =============================================================================
# 19. BOTÂNICA
# =============================================================================
elif jogo == "19. Botânica (Grupos Vegetais)":
    st.subheader("🪴 19. Evolução do Reino Plantae")
    st.success("🎯 **O que fazer:** Selecione o grupo vegetal para observar a presença de vasos condutores, sementes, flores e frutos.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Grupo Vegetal: 
            <select id="p" onchange="u()">
                <option value="Briófitas (Ex: Musgos) ➔ Avasculares, pequeno porte, dependem da água para fecundação.">Briófitas</option>
                <option value="Pteridófitas (Ex: Samambaias) ➔ Vasculares (Xilema/Floema), sem sementes.">Pteridófitas</option>
                <option value="Gimnospermas (Ex: Pinheiros) ➔ Vasculares, possuem SEMENTES NUDAS (pinhão), sem frutos.">Gimnospermas</option>
                <option value="Angiospermas (Ex: Árvores frutíferas) ➔ Possuem FLORES e FRUTOS (Grupo mais diversificado).">Angiospermas</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="o" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('o').innerText = document.getElementById('p').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Gimnospermas e Angiospermas conquistaram definitivamente o ambiente terrestre por produzirem **grão de pólen** (fecundação independente da água)!")

# =============================================================================
# 20. PARASITOLOGIA
# =============================================================================
elif jogo == "20. Parasitologia & Doenças do ENEM":
    st.subheader("🦟 20. Principais Doenças Cobradas no ENEM")
    st.success("🎯 **O que fazer:** Selecione a doença para ver o agente etiológico, transmissor e formas de prevenção.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #da3633; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Doença: 
            <select id="d" onchange="u()">
                <option value="Dengue/Zika/Chikungunya (Virose) ➔ Transmitida pelo mosquito Aedes aegypti. Prevenção: Eliminar água parada.">Dengue</option>
                <option value="Doença de Chagas (Protozoose) ➔ Causada pelo Trypanosoma cruzi, transmitida pelas fezes do barbeiro.">Chagas</option>
                <option value="Esquistossomose (Platelminto) ➔ Transmitida em água doce com caramujos contendo cercárias.">Esquistossomose</option>
                <option value="Malária (Protozoose) ➔ Causada pelo Plasmodium e transmitida pelo mosquito Anopheles.">Malária</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #da3633;"><b id="o" style="color:#da3633;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('o').innerText = document.getElementById('d').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Agente **Etiológico** é quem CAUSA a doença (ex: vírus, bactéria, protozoário). **Vetor** é quem TRANSMITE a doença (ex: mosquito)!")