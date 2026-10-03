import streamlit as st
import streamlit.components.v1 as components
# Configuração da Página
st.set_page_config(page_title="20 Jogos de Química pro ENEM", page_icon="🧪", layout="wide")

st.title("🧪 20 Jogos & Simuladores Interativos de Química pro ENEM")
st.write("Aprenda Química de forma visual e interativa em tempo real!")

# Menu Lateral com os 20 Jogos de Química
st.sidebar.header("🕹️ Selecione o Jogo (1 a 20)")
jogo = st.sidebar.radio("Módulos Interativos:", [
    "01. Tabela Periódica & Eletronegatividade",
    "02. Ligações Químicas (Iônica vs Covalente)",
    "03. Funções Inorgânicas & Escala de pH",
    "04. Funções Orgânicas (Grupos Funcionais)",
    "05. Isomeria Plana & Espacial (Cis/Trans)",
    "06. Reações Orgânicas (Esterificação & Saponificação)",
    "07. Estequiometria (Massa, Mol & Relações)",
    "08. Soluções & Diluição (Concentração)",
    "09. Termoquímica (ΔH Endotérmica vs Exotérmica)",
    "10. Cinética Química (Velocidade & Catalisador)",
    "11. Equilíbrio Químico (Le Chatelier)",
    "12. pH e pOH (Indicadores Ácido-Base)",
    "13. Eletroquímica: Pilhas (Ânodo & Cátodo)",
    "14. Eletroquímica: Eletrólise",
    "15. Separação de Misturas (Destilação & Filtração)",
    "16. Química Ambiental (Efeito Estufa & Chuva Ácida)",
    "17. Radioatividade (Alfa, Beta, Gama & Meia-Vida)",
    "18. Geometria Molecular & Polaridade",
    "19. Forças Intermoleculares (Pontes de Hidrogênio)",
    "20. Polímeros & Reciclagem de Plásticos"
])

st.sidebar.divider()
st.sidebar.caption("🎯 **Dica ENEM:** Mova os botões de cada jogo e observe as reações na tela!")

# =============================================================================
# 01. TABELA PERIÓDICA
# =============================================================================
if jogo == "01. Tabela Periódica & Eletronegatividade":
    st.subheader("⚛️ 01. Tabela Periódica e Tendências Periódicas")
    st.success("🎯 **O que fazer:** Escolha dois elementos para ver quem tem maior eletronegatividade (força para puxar elétrons)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #58a6ff; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Elemento 1: 
            <select id="e1" onchange="u()">
                <option value="3.98">Flúor (F) - 3.98</option>
                <option value="3.44">Oxigênio (O) - 3.44</option>
                <option value="3.16">Cloro (Cl) - 3.16</option>
                <option value="0.93">Sódio (Na) - 0.93</option>
                <option value="0.82">Potássio (K) - 0.82</option>
            </select>
        </div>
        <div class="card">
            Elemento 2: 
            <select id="e2" onchange="u()">
                <option value="0.93">Sódio (Na) - 0.93</option>
                <option value="3.98">Flúor (F) - 3.98</option>
                <option value="3.44">Oxigênio (O) - 3.44</option>
                <option value="3.16">Cloro (Cl) - 3.16</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="res" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){
                let v1 = parseFloat(document.getElementById('e1').value);
                let v2 = parseFloat(document.getElementById('e2').value);
                let diff = Math.abs(v1 - v2).toFixed(2);
                let tipo = diff > 1.7 ? "Diferença alta: Ligação predominantemente IÔNICA!" : "Diferença baixa: Ligação COVALENTE!";
                document.getElementById('res').innerText = "Diferença de Eletronegatividade: " + diff + " -> " + tipo;
            }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** A eletronegatividade cresce para a **DIREITA e para CIMA** na Tabela Periódica (O Flúor $F$ é o elemento mais eletronegativo de todos!).")

# =============================================================================
# 02. LIGAÇÕES QUÍMICAS
# =============================================================================
elif jogo == "02. Ligações Químicas (Iônica vs Covalente)":
    st.subheader("🔗 02. Transferência vs Partilha de Elétrons")
    st.success("🎯 **O que fazer:** Veja a diferença entre a transferência definitiva de elétrons (Iônica) e o compartilhamento (Covalente).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; margin: 4px; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div>
            <button onclick="m=1">1. Ligação Iônica (NaCl)</button>
            <button onclick="m=2">2. Ligação Covalente (H2O)</button>
        </div>
        <canvas id="c" width="450" height="140" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), m=1, t=0;
            function d(){
                ctx.clearRect(0,0,450,140);
                if(m===1){
                    // Iônica
                    ctx.fillStyle="#ff4b4b"; ctx.beginPath(); ctx.arc(150,70,25,0,Math.PI*2); ctx.fill();
                    ctx.fillStyle="#58a6ff"; ctx.beginPath(); ctx.arc(300,70,35,0,Math.PI*2); ctx.fill();
                    let ex = 175 + Math.sin(t*3)*50;
                    ctx.fillStyle="#f2cc60"; ctx.beginPath(); ctx.arc(ex,70,6,0,Math.PI*2); ctx.fill();
                    ctx.fillStyle="#fff"; ctx.fillText("Na+ (Metal doou)", 110, 115); ctx.fillText("Cl- (Não-metal recebeu)", 250, 120);
                } else {
                    // Covalente
                    let ex = 225 + Math.sin(t*4)*15;
                    ctx.fillStyle="#7ee787"; ctx.beginPath(); ctx.arc(180,70,25,0,Math.PI*2); ctx.fill();
                    ctx.fillStyle="#7ee787"; ctx.beginPath(); ctx.arc(270,70,25,0,Math.PI*2); ctx.fill();
                    ctx.fillStyle="#f2cc60"; ctx.beginPath(); ctx.arc(ex,70,6,0,Math.PI*2); ctx.fill();
                    ctx.fillStyle="#fff"; ctx.fillText("Não-metal + Não-metal (Partilham elétrons)", 120, 115);
                }
                t+=0.02; requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** Metal + Ametal = **Iônica** (ganha/perde elétrons). Ametal + Ametal = **Covalente** (partilha elétrons).")

# =============================================================================
# 03. FUNÇÕES INORGÂNICAS & PH
# =============================================================================
elif jogo == "03. Funções Inorgânicas & Escala de pH":
    st.subheader("🧪 03. Ácidos, Bases e Escala de pH")
    st.success("🎯 **O que fazer:** Mova a barra de pH e observe a mudança de cor do indicador (Fenolftaleína e Papel Tornassol).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #a371f7; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">🧪 Valor do pH: <input type="range" id="ph" min="0" max="14" value="7" step="1" oninput="u()"> <span id="phv">7 (Neutro)</span></div>
        <canvas id="c" width="450" height="120" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function u(){
                let val = parseInt(document.getElementById('ph').value);
                let txt = val < 7 ? val + " (ÁCIDO)" : val > 7 ? val + " (BÁSICO)" : "7 (NEUTRO)";
                document.getElementById('phv').innerText = txt;
            }
            function d(){
                ctx.clearRect(0,0,450,120);
                let val = parseInt(document.getElementById('ph').value);
                // Cor do Indicador
                let r=0, g=0, b=0;
                if(val < 7) { r=255; g=val*30; b=50; } // Ácido -> Vermelho/Laranja
                else if(val === 7) { r=100; g=255; b=100; } // Neutro -> Verde
                else { r=val*15; g=50; b=255; } // Básico -> Azul/Roxo

                ctx.fillStyle=`rgb(${r},${g},${b})`;
                ctx.fillRect(100,20,250,80); ctx.strokeStyle="#fff"; ctx.strokeRect(100,20,250,80);
                ctx.fillStyle="#fff"; ctx.fillText("Solução com pH = " + val, 170, 65);
                requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** pH < 7 = **Ácido** (libera $H^+$ em água). pH > 7 = **Básico/Alcalino** (libera $OH^-$ em água). pH = 7 é Neutro.")

# =============================================================================
# 04. FUNÇÕES ORGÂNICAS
# =============================================================================
elif jogo == "04. Funções Orgânicas (Grupos Funcionais)":
    st.subheader("🧬 04. Identificação de Funções Orgânicas")
    st.success("🎯 **O que fazer:** Selecione uma função orgânica para ver sua estrutura química e sua aplicação no dia a dia!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Escolha a Função: 
            <select id="func" onchange="u()">
                <option value="Álcool (Ex: Etanol) | Possui hidroxila (-OH) ligada a C saturado.">Álcool (-OH)</option>
                <option value="Ácido Carboxílico (Ex: Vinagre) | Possui carboxila (-COOH).">Ácido Carboxílico (-COOH)</option>
                <option value="Éster (Ex: Aromas/Essências) | Derivado de ácido + álcool (-COO-R).">Éster (-COO-R)</option>
                <option value="Cetona (Ex: Acetona) | Possui carbonila (C=O) entre carbonos.">Cetona (C=O intermediário)</option>
                <option value="Amina (Ex: Cafeína) | Derivada da amônia contendo Nitrogênio (N).">Amina (contém N)</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="desc" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){
                document.getElementById('desc').innerText = document.getElementById('func').value;
            }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** A hidroxila ($-OH$) em carbono saturado forma **Álcool**. Se estiver ligada diretamente ao anel aromático, é um **Fenol**!")

# =============================================================================
# 05. ISOMERIA
# =============================================================================
elif jogo == "05. Isomeria Plana & Espacial (Cis/Trans)":
    st.subheader("🪞 05. Isomeria Geométrica (Cis vs Trans)")
    st.success("🎯 **O que fazer:** Alterne entre os isômeros Cis e Trans para ver a posição dos ligantes em relação à ligação dupla.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
        canvas { border: 2px solid #f0883e; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <button onclick="iso='cis'">Isômero CIS (Mesmo lado)</button>
        <button onclick="iso='trans'">Isômero TRANS (Lados opostos)</button>
        <canvas id="c" width="450" height="130" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), iso='cis';
            function d(){
                ctx.clearRect(0,0,450,130);
                ctx.strokeStyle="#fff"; ctx.lineWidth=3;
                // Dupla C=C
                ctx.beginPath(); ctx.moveTo(200,60); ctx.lineTo(250,60); ctx.moveTo(200,66); ctx.lineTo(250,66); ctx.stroke();
                ctx.fillStyle="#f0883e";
                if(iso==='cis'){
                    ctx.beginPath(); ctx.arc(170,30,12,0,Math.PI*2); ctx.arc(280,30,12,0,Math.PI*2); ctx.fill();
                    ctx.fillStyle="#fff"; ctx.fillText("Grupamentos no MESMO lado do plano", 120, 115);
                } else {
                    ctx.beginPath(); ctx.arc(170,30,12,0,Math.PI*2); ctx.arc(280,95,12,0,Math.PI*2); ctx.fill();
                    ctx.fillStyle="#fff"; ctx.fillText("Grupamentos em LADOS OPOSTOS", 130, 115);
                }
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** Isômeros **CIS** têm ligantes iguais no mesmo lado da dupla ligação. Isômeros **TRANS** têm ligantes em lados opostos!")

# =============================================================================
# 06. REAÇÕES ORGÂNICAS
# =============================================================================
elif jogo == "06. Reações Orgânicas (Esterificação & Saponificação)":
    st.subheader("🫧 06. Esterificação e Saponificação (Sabão)")
    st.success("🎯 **O que fazer:** Escolha uma reação para entender a formação de ésteres ou a produção de sabão!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('r').innerText='Ácido Carboxílico + Álcool ➔ ÉSTER + ÁGUA (Aroma/Essência)'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">1. Esterificação</button>
            <button onclick="document.getElementById('r').innerText='Éster (Gordura) + Base Forte (NaOH) ➔ SABÃO + GLICEROL'" style="background:#da3633; color:white; border:none; padding:8px; border-radius:4px;">2. Saponificação</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border:1px solid #58a6ff;"><b id="r" style="color:#58a6ff;">Clique em uma reação acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** A reação de Saponificação usa gordura + soda cáustica ($NaOH$) para formar **Sabão**, que possui uma cauda apolar e uma cabeça polar (anfifílico)!")

# =============================================================================
# 07. ESTEQUIOMETRIA
# =============================================================================
elif jogo == "07. Estequiometria (Massa, Mol & Relações)":
    st.subheader("⚖️ 07. Proporções Estequiométricas")
    st.success("🎯 **O que fazer:** Varie o número de Mols de reagente e veja a quantidade correspondente de produto gerada na reação!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">⚛️ Mols de H2: <input type="range" id="m" min="1" max="10" value="2" oninput="c()"> <span id="mv">2 mols</span></div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #e3b341;">Reação: 2 H2 + 1 O2 ➔ 2 H2O</div>
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">Gerados 2 mols de H2O (36g)</b></div>
        </div>
        <script>
            function c(){
                let v = parseInt(document.getElementById('m').value);
                document.getElementById('mv').innerText = v + ' mols';
                document.getElementById('out').innerText = 'Gerados ' + v + ' mols de H2O (' + (v*18) + 'g)';
            }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** 1 Mol de qualquer gás na CNTP ocupa **22,4 Litros**! A massa molar é calculada somando as massas da Tabela Periódica.")

# =============================================================================
# 08. SOLUÇÕES & DILUIÇÃO
# =============================================================================
elif jogo == "08. Soluções & Diluição (Concentração)":
    st.subheader("💧 08. Processo de Diluição de Soluções")
    st.success("🎯 **O que fazer:** Adicione água para diluir o recipiente. Note que a quantidade de soluto é constante, mas a concentração diminui!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">💧 Volume de Água (V): <input type="range" id="v" min="1" max="5" value="1" step="1" oninput="u()"> <span id="vv">1 L</span></div>
        <canvas id="c" width="450" height="120" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function u(){ document.getElementById('vv').innerText = document.getElementById('v').value + ' L'; }
            function d(){
                ctx.clearRect(0,0,450,120);
                let v = parseInt(document.getElementById('v').value);
                let conc = (10 / v).toFixed(1);
                // Solução
                let h = v * 20;
                ctx.fillStyle = `rgba(255, 75, 75, ${1 / v})`;
                ctx.fillRect(175, 110 - h, 100, h); ctx.strokeRect(175, 10, 100, 100);
                ctx.fillStyle="#fff"; ctx.fillText("Conc: " + conc + " mol/L", 185, 60);
                requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** Na diluição: $C_1 \\cdot V_1 = C_2 \\cdot V_2$. Ao dobrar o volume de água, a concentração cai pela metade!")

# =============================================================================
# 09. TERMOQUÍMICA
# =============================================================================
elif jogo == "09. Termoquímica (ΔH Endotérmica vs Exotérmica)":
    st.subheader("🔥 09. Reações Endotérmicas vs Exotérmicas")
    st.success("🎯 **O que fazer:** Alterne entre os tipos de reações e observe o sinal do Variação de Entalpia ($\Delta H$).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
        canvas { border: 2px solid #ff7b72; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <button onclick="t='exo'">1. Exotérmica (Libera Calor: ΔH < 0)</button>
        <button onclick="t='endo'">2. Endotérmica (Absorve Calor: ΔH > 0)</button>
        <canvas id="c" width="450" height="130" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), t='exo';
            function d(){
                ctx.clearRect(0,0,450,130);
                ctx.strokeStyle="#ff7b72"; ctx.lineWidth=3;
                if(t==='exo'){
                    ctx.beginPath(); ctx.moveTo(50,30); ctx.lineTo(150,30); ctx.lineTo(250,90); ctx.lineTo(350,90); ctx.stroke();
                    ctx.fillStyle="#fff"; ctx.fillText("Reagentes (Alta Energia) ➔ Produtos (Baixa Energia) + CALOR", 60, 115);
                } else {
                    ctx.beginPath(); ctx.moveTo(50,90); ctx.lineTo(150,90); ctx.lineTo(250,30); ctx.lineTo(350,30); ctx.stroke();
                    ctx.fillStyle="#fff"; ctx.fillText("Reagentes + CALOR ➔ Produtos (Alta Energia)", 80, 115);
                }
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** Reação **Exotérmica** libera calor ($\Delta H < 0$, ex: combustão). Reação **Endotérmica** absorve calor ($\Delta H > 0$, ex: fotossíntese).")

# =============================================================================
# 10. CINÉTICA QUÍMICA
# =============================================================================
elif jogo == "10. Cinética Química (Velocidade & Catalisador)":
    st.subheader("⚡ 10. Fatores que Aceleram Reações Química")
    st.success("🎯 **O que fazer:** Adicione um catalisador para diminuir a Energia de Ativação e acelerar drasticamente a reação!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
        canvas { border: 2px solid #e3b341; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <button onclick="cat=!cat">Alternar Catalisador</button>
        <canvas id="c" width="450" height="130" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), cat=false;
            function d(){
                ctx.clearRect(0,0,450,130);
                ctx.strokeStyle="#8b949e"; ctx.lineWidth=3;
                // Sem catalisador
                ctx.beginPath(); ctx.moveTo(50,80); ctx.quadraticCurveTo(200,-20,350,80); ctx.stroke();
                if(cat){
                    ctx.strokeStyle="#e3b341";
                    ctx.beginPath(); ctx.moveTo(50,80); ctx.quadraticCurveTo(200,30,350,80); ctx.stroke();
                    ctx.fillStyle="#e3b341"; ctx.fillText("Com Catalisador: Menor Energia de Ativação!", 100, 115);
                } else {
                    ctx.fillStyle="#fff"; ctx.fillText("Sem Catalisador: Alta barreira de energia!", 110, 115);
                }
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** O **Catalisador** acelera a reação porque reduz a energia de ativação, sem ser consumido durante o processo!")

# =============================================================================
# 11. EQUILÍBRIO QUÍMICO
# =============================================================================
elif jogo == "11. Equilíbrio Químico (Le Chatelier)":
    st.subheader("⚖️ 11. Princípio de Le Chatelier")
    st.success("🎯 **O que fazer:** Aumente a pressão ou temperatura e veja para qual lado o equilíbrio químico se desloca.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
    </style></head><body>
        <div class="card">Reação: N2(g) + 3 H2(g) ⇌ 2 NH3(g) (Exotérmica)</div>
        <div style="margin-top:6px;">
            <button onclick="document.getElementById('out').innerText='Aumento de Pressão ➔ Desloca para a DIREITA (Menor volume de gás)'">Aumentar Pressão</button>
            <button onclick="document.getElementById('out').innerText='Aumento de Temp ➔ Desloca para a ESQUERDA (Sentido Endotérmico)'">Aumentar Temperatura</button>
        </div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">Clique nos botões acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** 'Perturbou o equilíbrio, ele reage no sentido oposto para anular a perturbação' (Aumento de pressão favorece o lado com menor número de mols de gás!).")

# =============================================================================
# 12. PH E POH
# =============================================================================
elif jogo == "12. pH e pOH (Indicadores Ácido-Base)":
    st.subheader("💧 12. Relação entre pH e pOH")
    st.success("🎯 **O que fazer:** Altere o pH e calcule o valor correspondente do pOH sabendo que $pH + pOH = 14$!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">🧪 pH: <input type="range" id="ph" min="1" max="13" value="3" oninput="c()"> <span id="phv">3</span></div>
        <div class="card" style="border:1px solid #58a6ff;">💧 pOH correspondente: <b id="poh" style="color:#58a6ff;">11</b></div>
        <script>
            function c(){
                let val = parseInt(document.getElementById('ph').value);
                document.getElementById('phv').innerText = val;
                document.getElementById('poh').innerText = 14 - val;
            }
        </script>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** $pH + pOH = 14$. Se uma solução tem $[H^+] = 10^{-3}\\text{ mol/L}$, seu $pH = 3$ e o $pOH = 11$!")

# =============================================================================
# 13. ELETROQUÍMICA: PILHAS
# =============================================================================
elif jogo == "13. Eletroquímica: Pilhas (Ânodo & Cátodo)":
    st.subheader("🔋 13. Funcionamento da Pilha de Daniell")
    st.success("🎯 **O que fazer:** Veja os elétrons fluírem espontaneamente do Ânodo (Oxidação) para o Cátodo (Redução).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #e3b341; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <canvas id="c" width="450" height="140"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), t=0;
            function d(){
                ctx.clearRect(0,0,450,140);
                // Eletrodos
                ctx.fillStyle="#ff4b4b"; ctx.fillRect(80,30,20,80); // Ânodo (Zn)
                ctx.fillStyle="#58a6ff"; ctx.fillRect(350,30,20,80); // Cátodo (Cu)
                ctx.strokeStyle="#8b949e"; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(90,30); ctx.lineTo(90,10); ctx.lineTo(360,10); ctx.lineTo(360,30); ctx.stroke();
                // Elétrons
                let ex = 90 + (t*3 % 270);
                ctx.fillStyle="#e3b341"; ctx.beginPath(); ctx.arc(ex,10,5,0,Math.PI*2); ctx.fill();
                ctx.fillStyle="#fff"; ctx.fillText("ÂNOODO (-) Oxida", 50, 125); ctx.fillText("CÁTUDO (+) Reduz", 320, 125);
                t+=0.5; requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** 'CÃO' e 'CROA': **Vogal com Vogal** (Anodo Oxida), **Consoante com Consoante** (Catodo Reduz). O elétron flutua do Ânodo para o Cátodo!")

# =============================================================================
# 14. ELETRÓLISE
# =============================================================================
elif jogo == "14. Eletroquímica: Eletrólise":
    st.subheader("⚡ 14. Eletrólise (Processo Não Espontâneo)")
    st.success("🎯 **O que fazer:** Aplique corrente elétrica de uma fonte externa para forçar uma reação química que não ocorreria sozinha!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #da3633; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <canvas id="c" width="450" height="130"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function d(){
                ctx.clearRect(0,0,450,130);
                ctx.fillStyle="rgba(218,54,51,0.3)"; ctx.fillRect(100,40,250,80);
                ctx.fillStyle="#fff"; ctx.fillRect(140,20,15,80); ctx.fillRect(295,20,15,80);
                ctx.fillText("Gerador Externo (Bateria) Forçando a Reação", 110, 115);
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=210)
    st.info("💡 **Macete ENEM:** Enquanto a Pilha gera energia elétrica espontaneamente, a **Eletrólise** consome energia elétrica para realizar reações químicas!")

# =============================================================================
# 15. SEPARAÇÃO DE MISTURAS
# =============================================================================
elif jogo == "15. Separação de Misturas (Destilação & Filtração)":
    st.subheader("🧪 15. Métodos de Separação de Misturas")
    st.success("🎯 **O que fazer:** Selecione o tipo de mistura para descobrir o método ideal de separação cobrado no ENEM!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Mistura: 
            <select id="m" onchange="u()">
                <option value="Água + Sal (Homogênea) ➔ Destilação Simples">Água + Sal</option>
                <option value="Água + Álcool (Homogênea) ➔ Destilação Fracionada (Pontos de ebulição diferentes)">Água + Álcool</option>
                <option value="Água + Areia (Heterogênea) ➔ Filtração ou Decantação">Água + Areia</option>
                <option value="Água + Óleo (Heterogênea) ➔ Funil de Decantação">Água + Óleo</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border:1px solid #7ee787;"><b id="out" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('out').innerText = document.getElementById('m').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** O refino do petróleo usa a **Destilação Fracionada**, separando os componentes pelos seus pontos de ebulição!")

# =============================================================================
# 16. QUÍMICA AMBIENTAL
# =============================================================================
elif jogo == "16. Química Ambiental (Efeito Estufa & Chuva Ácida)":
    st.subheader("🌍 16. Impactos Ambientais & Química")
    st.success("🎯 **O que fazer:** Veja os principais gases poluentes e suas consequências ecológicas diretas.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('o').innerText='CO2 e CH4 (Metano) ➔ Aquecimento Global & Efeito Estufa Intensificado'" style="background:#da3633; color:white; border:none; padding:8px; border-radius:4px;">1. Efeito Estufa</button>
            <button onclick="document.getElementById('o').innerText='SO2 e NOx + Água ➔ Ácido Sulfúrico/Nítrico (Chuva Ácida)'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">2. Chuva Ácida</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #f0883e;"><b id="o" style="color:#f0883e;">Clique em um problema acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Os óxidos de enxofre ($SO_2, SO_3$) resultantes da queima do diesel geram $H_2SO_4$ (Ácido Sulfúrico), responsável pela chuva ácida!")

# =============================================================================
# 17. RADIOATIVIDADE
# =============================================================================
elif jogo == "17. Radioatividade (Alfa, Beta, Gama & Meia-Vida)":
    st.subheader("☢️ 17. Decaimento Radioativo & Meia-Vida")
    st.success("🎯 **O que fazer:** Veja a quantidade de massa radioativa cair pela metade a cada período de Meia-Vida ($t_{1/2}$).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">⏱️ Meias-Vidas decorridas: <input type="range" id="p" min="0" max="5" value="0" oninput="c()"> <span id="pv">0</span></div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #a371f7;"><b id="m" style="color:#a371f7;">Massa restante: 100g (100%)</b></div>
        </div>
        <script>
            function c(){
                let p = parseInt(document.getElementById('p').value);
                document.getElementById('pv').innerText = p;
                let mass = 100 / Math.pow(2, p);
                document.getElementById('m').innerText = 'Massa restante: ' + mass.toFixed(1) + 'g (' + mass.toFixed(1) + '%)';
            }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Partícula **Alfa** ($_{2}^{4}\\alpha$) tem massa 4. Partícula **Beta** ($_{-1}^{0}\\beta$) tem massa 0. Radiação **Gama** ($_{0}^{0}\\gamma$) é onda eletromagnética pura!")

# =============================================================================
# 18. GEOMETRIA MOLECULAR
# =============================================================================
elif jogo == "18. Geometria Molecular & Polaridade":
    st.subheader("📐 18. Geometria das Moléculas")
    st.success("🎯 **O que fazer:** Selecione uma molécula para entender sua geometria espacial e polaridade.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #58a6ff; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Molécula: 
            <select id="mol" onchange="u()">
                <option value="H2O (Água) ➔ Geometria ANGULAR | POLAR (Pares de elétrons sobram no Oxigênio)">H2O (Água)</option>
                <option value="CO2 (Dióxido de Carbono) ➔ Geometria LINEAR | APOLAR (Vetores se anulam)">CO2</option>
                <option value="NH3 (Amônia) ➔ Geometria PIRAMIDAL | POLAR">NH3 (Amônia)</option>
                <option value="CH4 (Metano) ➔ Geometria TETRAÉDRICA | APOLAR">CH4 (Metano)</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="o" style="color:#58a6ff;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('o').innerText = document.getElementById('mol').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** A molécula da água ($H_2O$) é **Angular e POLAR**, por isso dissolve substâncias polares ('Semelhante dissolve semelhante').")

# =============================================================================
# 19. FORÇAS INTERMOLECULARES
# =============================================================================
elif jogo == "19. Forças Intermoleculares (Pontes de Hidrogênio)":
    st.subheader("🧲 19. Atrações Intermoleculares")
    st.success("🎯 **O que fazer:** Veja a intensidade das forças que mantêm as moléculas unidas no estado líquido e sólido.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('o').innerText='Ligação de Hidrogênio (MAIS FORTE): Hidrogênio ligado a F, O, N!'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">1. Ligação de Hidrogênio</button>
            <button onclick="document.getElementById('o').innerText='Dipolo Induzido / London (MAIS FRACA): Ocorre entre moléculas Apolares (ex: O2, CH4)'" style="background:#da3633; color:white; border:none; padding:8px; border-radius:4px;">2. Dipolo Induzido</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="o" style="color:#7ee787;">Clique acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** **Ligação de Hidrogênio** é a força intermolecular mais forte e só ocorre quando o Hidrogênio está ligado diretamente ao **FON** (Flúor, Oxigênio ou Nitrogênio)!")

# =============================================================================
# 20. POLÍMEROS
# =============================================================================
elif jogo == "20. Polímeros & Reciclagem de Plásticos":
    st.subheader("♻️ 20. Polímeros Sintéticos & Meio Ambiente")
    st.success("🎯 **O que fazer:** Conheça os principais polímeros cobrados no ENEM e suas aplicações diárias.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Polímero: 
            <select id="p" onchange="u()">
                <option value="PET (Poliálcool + Poliácido) ➔ Polímero de Condensação usado em garrafas plásticas">PET</option>
                <option value="Polietileno (Mônomero: Eteno) ➔ Polímero de Adição usado em sacolas plásticas">Polietileno (PE)</option>
                <option value="PVC (Policloreto de Vinila) ➔ Usado em tubos e conexões de encanamento">PVC</option>
                <option value="Teflon (PTFE) ➔ Antiaderente para panelas resistente ao calor">Teflon</option>
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
    st.info("💡 **Macete ENEM:** Polímeros **Termoplásticos** podem ser derretidos e reciclados várias vezes. Polímeros **Termofixos** não derretem (desintegram-se no calor).")