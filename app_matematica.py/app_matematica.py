import streamlit as st
import streamlit.components.v1 as components

# Configuração da Página
st.set_page_config(page_title="20 Jogos de Matemática pro ENEM", page_icon="📐", layout="wide")

st.title("📐 20 Jogos & Simuladores Interativos de Matemática pro ENEM")
st.write("Aprenda os assuntos de Matemática mais cobrados no ENEM manipulando dados em tempo real!")

# Menu Lateral
st.sidebar.header("🕹️ Selecione o Jogo (1 a 20)")
jogo = st.sidebar.radio("Módulos Interativos:", [
    "01. Regra de Três & Proporcionalidade",
    "02. Porcentagem & Lucro/Desconto",
    "03. Estatística (Média, Moda e Mediana)",
    "04. Probabilidade no ENEM",
    "05. Análise Combinatória (Arranjo vs Combinação)",
    "06. Função do 1º Grau (Estudo da Reta)",
    "07. Função do 2º Grau (Vértice & Máximos)",
    "08. Geometria Plana (Cálculo de Áreas)",
    "09. Teorema de Pitágoras & Trigonometria",
    "10. Geometria Espacial (Prismas & Cilindros)",
    "11. Geometria Espacial (Cones & Esferas)",
    "12. Escala, Mapas & Projeção Ortogonal",
    "13. Leitura e Análise de Gráficos",
    "14. Juros Simples vs Juros Compostos",
    "15. Progressão Aritmética (PA)",
    "16. Progressão Geométrica (PG)",
    "17. Função Exponencial & Logaritmos",
    "18. Geometria Analítica (Distância e Reta)",
    "19. Ciclo Trigonométrico (Seno e Cosseno)",
    "20. Sistemas Lineares & Matrizes"
])

st.sidebar.divider()
st.sidebar.caption("🎯 **Dica ENEM:** Mova os controles e observe o resultado das fórmulas na hora!")

# =============================================================================
# 01. REGRA DE TRÊS
# =============================================================================
if jogo == "01. Regra de Três & Proporcionalidade":
    st.subheader("⚖️ 01. Regra de Três Direta vs Inversamente Proporcional")
    st.success("🎯 **O que fazer:** Aumente o número de operários e veja o tempo de obra diminuir (Grandeza Inversamente Proporcional)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">👷 Operários: <input type="range" id="op" min="1" max="20" value="4" oninput="c()"> <span id="opv">4</span></div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">Tempo necessário: 30 dias</b></div>
        </div>
        <script>
            function c(){
                let op = parseInt(document.getElementById('op').value);
                document.getElementById('opv').innerText = op;
                let dias = (120 / op).toFixed(1); // 4 op * 30 dias = 120 total
                document.getElementById('out').innerText = 'Tempo necessário: ' + dias + ' dias';
            }
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** **Diretamente proporcional:** Se um dobra, o outro dobra (multiplica cruzado). **Inversamente proporcional:** Se um dobra, o outro cai pela metade (multiplica na mesma linha!).")

# =============================================================================
# 02. PORCENTAGEM
# =============================================================================
elif jogo == "02. Porcentagem & Lucro/Desconto":
    st.subheader("🏷️ 02. Aumentos e Descontos Sucessivos")
    st.success("🎯 **O que fazer:** Aplique um desconto e depois um aumento do mesmo percentual e veja por que o preço NÃO volta ao original!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">💵 Preço Inicial: R$ 100,00</div>
        <div class="card">📉 % de Alteração: <input type="range" id="p" min="5" max="50" step="5" value="20" oninput="c()"> <span id="pv">20%</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #ff7b72;"><b id="out" style="color:#ff7b72;">-</b></div>
        </div>
        <script>
            function c(){
                let p = parseInt(document.getElementById('p').value);
                document.getElementById('pv').innerText = p + '%';
                let d = 100 * (1 - p/100);
                let final = d * (1 + p/100);
                document.getElementById('out').innerText = 'Com ' + p + '% de desconto = R$ ' + d.toFixed(2) + ' ➔ Depois com ' + p + '% de aumento = R$ ' + final.toFixed(2);
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Fator de aumento = $(1 + i)$. Fator de desconto = $(1 - i)$. Aumentar 20% e depois descontar 20% resulta em um fator total de $1,20 \\cdot 0,80 = 0,96$ (ou seja, 4% de perda!).")

# =============================================================================
# 03. ESTATÍSTICA
# =============================================================================
elif jogo == "03. Estatística (Média, Moda e Mediana)":
    st.subheader("📊 03. Medidas de Tendência Central")
    st.success("🎯 **O que fazer:** Altere as notas do aluno para calcular a Média Aritmética, Moda e Mediana instantaneamente.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">Notas: [4, 6, 8, 8, <input type="range" id="n" min="0" max="10" value="9" oninput="c()"> <span id="nv">9</span>]</div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="m" style="color:#58a6ff;">-</b></div>
        </div>
        <script>
            function c(){
                let val = parseInt(document.getElementById('n').value);
                document.getElementById('nv').innerText = val;
                let arr = [4, 6, 8, 8, val].sort((a,b)=>a-b);
                let mean = (arr.reduce((a,b)=>a+b,0)/5).toFixed(1);
                let median = arr[2];
                document.getElementById('m').innerText = 'Média = ' + mean + ' | Mediana = ' + median + ' | Moda = 8';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** **Média:** Soma de tudo dividida pela quantidade. **Mediana:** Valor central com o rol organizado em ordem crescente. **Moda:** O valor mais frequente!")

# =============================================================================
# 04. PROBABILIDADE
# =============================================================================
elif jogo == "04. Probabilidade no ENEM":
    st.subheader("🎲 04. Cálculo de Probabilidade de Eventos")
    st.success("🎯 **O que fazer:** Altere o número de casos favoráveis e o total de casos para ver a porcentagem de chance!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">🎯 Casos Favoráveis: <input type="range" id="fav" min="1" max="10" value="3" oninput="c()"> <span id="favv">3</span></div>
        <div class="card">📦 Espaço Amostral Total: <input type="range" id="tot" min="10" max="50" value="20" oninput="c()"> <span id="totv">20</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #e3b341;"><b id="out" style="color:#e3b341;">-</b></div>
        </div>
        <script>
            function c(){
                let f = parseInt(document.getElementById('fav').value);
                let t = parseInt(document.getElementById('tot').value);
                document.getElementById('favv').innerText = f; document.getElementById('totv').innerText = t;
                let prob = ((f / t) * 100).toFixed(1);
                document.getElementById('out').innerText = 'Probabilidade P(A) = ' + f + '/' + t + ' = ' + prob + '%';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** $P = \\frac{\\text{Casos Favoráveis}}{\\text{Casos Totais}}$. Em probabilidade condicional, lembre-se que o espaço amostral diminui!")

# =============================================================================
# 05. ANÁLISE COMBINATÓRIA
# =============================================================================
elif jogo == "05. Análise Combinatória (Arranjo vs Combinação)":
    st.subheader("🔢 05. Permutação, Arranjo e Combinação")
    st.success("🎯 **O que fazer:** Descubra quando a ordem dos elementos importa (Arranjo) e quando NÃO importa (Combinação)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <button onclick="document.getElementById('out').innerText='ARRANJO: A ordem IMPORTA! (Ex: Senhas de banco, Pódio de corrida).'" style="background:#238636; color:white; border:none; padding:8px; border-radius:4px;">Ordem Importa (Arranjo)</button>
            <button onclick="document.getElementById('out').innerText='COMBINAÇÃO: A ordem NÃO importa! (Ex: Comissões, Salada de frutas, Aposta na Mega-Sena).'" style="background:#da3633; color:white; border:none; padding:8px; border-radius:4px;">Ordem NÃO Importa (Combinação)</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">Clique nos botões acima</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Faça a pergunta mágica: 'Se eu mudar a ordem dos elementos, muda o resultado?' Se SIM = **Arranjo** ($A_{n,k}$). Se NÃO = **Combinação** ($C_{n,k}$).")

# =============================================================================
# 06. FUNÇÃO DO 1º GRAU
# =============================================================================
elif jogo == "06. Função do 1º Grau (Estudo da Reta)":
    st.subheader("📈 06. Estudo da Reta: $y = ax + b$")
    st.success("🎯 **O que fazer:** Altere a inclinação ($a$) e o ponto de corte no eixo Y ($b$) para ver a transformação do gráfico!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">a (Inclin.): <input type="range" id="a" min="-3" max="3" value="1" step="0.5" oninput="u()"> <span id="av">1</span></div>
        <div class="card">b (Corte Y): <input type="range" id="b" min="-40" max="40" value="0" step="10" oninput="u()"> <span id="bv">0</span></div>
        <canvas id="c" width="450" height="130" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function u(){
                document.getElementById('av').innerText = document.getElementById('a').value;
                document.getElementById('bv').innerText = document.getElementById('b').value;
            }
            function d(){
                ctx.clearRect(0,0,450,130);
                let a = parseFloat(document.getElementById('a').value);
                let b = parseFloat(document.getElementById('b').value);
                // Eixos
                ctx.strokeStyle="#484f58"; ctx.lineWidth=1;
                ctx.beginPath(); ctx.moveTo(0,65); ctx.lineTo(450,65); ctx.moveTo(225,0); ctx.lineTo(225,130); ctx.stroke();
                // Reta y = ax + b
                ctx.strokeStyle="#58a6ff"; ctx.lineWidth=3; ctx.beginPath();
                for(let px=0; px<450; px++){
                    let x = (px - 225) / 20;
                    let y = a * x + (b/10);
                    let py = 65 - (y * 20);
                    if(px===0) ctx.moveTo(px,py); else ctx.lineTo(px,py);
                }
                ctx.stroke(); requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=250)
    st.info("💡 **Macete ENEM:** O coeficiente $a$ é a **Taxa de Variação** (inclinação). O coeficiente $b$ é o **Valor Fixo** inicial (onde a reta corta o eixo Y!).")

# =============================================================================
# 07. FUNÇÃO DO 2º GRAU
# =============================================================================
elif jogo == "07. Função do 2º Grau (Vértice & Máximos)":
    st.subheader("🎯 07. Parábola e Vértice (Pontos de Máximo e Mínimo)")
    st.success("🎯 **O que fazer:** Mude o coeficiente 'a' de positivo para negativo para virar a concavidade da parábola!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #ff7b72; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">a (Concavidade): <input type="range" id="a" min="-2" max="2" value="1" step="0.5" oninput="u()"> <span id="av">1</span></div>
        <canvas id="c" width="450" height="130" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function u(){ document.getElementById('av').innerText = document.getElementById('a').value; }
            function d(){
                ctx.clearRect(0,0,450,130);
                let a = parseFloat(document.getElementById('a').value);
                ctx.strokeStyle="#484f58"; ctx.beginPath(); ctx.moveTo(0,65); ctx.lineTo(450,65); ctx.moveTo(225,0); ctx.lineTo(225,130); ctx.stroke();
                ctx.strokeStyle="#ff7b72"; ctx.lineWidth=3; ctx.beginPath();
                for(let px=0; px<450; px++){
                    let x = (px - 225) / 25;
                    let y = a * (x * x) - 1;
                    let py = 65 - (y * 20);
                    if(px===0) ctx.moveTo(px,py); else ctx.lineTo(px,py);
                }
                ctx.stroke(); requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** Se $a > 0$, concavidade para CIMA (ponto de Mínimo). Se $a < 0$, concavidade para BAIXO (ponto de Máximo). $X_v = \\frac{-b}{2a}$ e $Y_v = \\frac{-\\Delta}{4a}$.")

# =============================================================================
# 08. GEOMETRIA PLANA
# =============================================================================
elif jogo == "08. Geometria Plana (Cálculo de Áreas)":
    st.subheader("📐 08. Áreas das Figuras Planas")
    st.success("🎯 **O que fazer:** Varie o raio do Círculo ou os lados do Retângulo para calcular a área em tempo real.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">⭕ Raio do Círculo (r): <input type="range" id="r" min="1" max="10" value="4" oninput="c()"> <span id="rv">4 cm</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function c(){
                let r = parseInt(document.getElementById('r').value);
                document.getElementById('rv').innerText = r + ' cm';
                let area = (3.14 * r * r).toFixed(1);
                document.getElementById('out').innerText = 'Área do Círculo (A = π.r²) = ' + area + ' cm²';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Triângulo: $A = \\frac{b \\cdot h}{2}$. Retângulo: $A = b \\cdot h$. Círculo: $A = \\pi r^2$. Trapézio: $A = \\frac{(B+b)h}{2}$.")

# =============================================================================
# 09. PITÁGORAS & TRIGONOMETRIA
# =============================================================================
elif jogo == "09. Teorema de Pitágoras & Trigonometria":
    st.subheader("📐 09. Triângulo Retângulo & Pitágoras")
    st.success("🎯 **O que fazer:** Ajuste os catetos e veja a hipotenusa ($a^2 + b^2 = c^2$) ser calculada automaticamente.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">Cateto a: <input type="range" id="ca" min="3" max="12" value="3" oninput="c()"> <span id="cav">3</span></div>
        <div class="card">Cateto b: <input type="range" id="cb" min="4" max="16" value="4" oninput="c()"> <span id="cbv">4</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #e3b341;"><b id="out" style="color:#e3b341;">-</b></div>
        </div>
        <script>
            function c(){
                let a = parseInt(document.getElementById('ca').value);
                let b = parseInt(document.getElementById('cb').value);
                document.getElementById('cav').innerText = a; document.getElementById('cbv').innerText = b;
                let h = Math.sqrt(a*a + b*b).toFixed(2);
                document.getElementById('out').innerText = 'Hipotenusa c = √(' + a + '² + ' + b + '²) = ' + h;
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** 'SOH CAH TOA': $\\sin = \\frac{\\text{Oposto}}{\\text{Hipotenusa}}$, $\\cos = \\frac{\\text{Adjacente}}{\\text{Hipotenusa}}$, $\\tan = \\frac{\\text{Oposto}}{\\text{Adjacente}}$. Lembre-se do triângulo pitagórico clássico: 3, 4 e 5!")

# =============================================================================
# 10. GEOMETRIA ESPACIAL - PRISMAS
# =============================================================================
elif jogo == "10. Geometria Espacial (Prismas & Cilindros)":
    st.subheader("🧊 10. Volume de Cilindros e Prismas")
    st.success("🎯 **O que fazer:** Altere o raio da base e a altura do cilindro para calcular sua capacidade em Litros.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">⭕ Raio (r): <input type="range" id="r" min="1" max="5" value="2" oninput="c()"> <span id="rv">2m</span></div>
        <div class="card">📏 Altura (h): <input type="range" id="h" min="1" max="10" value="5" oninput="c()"> <span id="hv">5m</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="out" style="color:#58a6ff;">-</b></div>
        </div>
        <script>
            function c(){
                let r = parseInt(document.getElementById('r').value);
                let h = parseInt(document.getElementById('h').value);
                document.getElementById('rv').innerText = r + 'm'; document.getElementById('hv').innerText = h + 'm';
                let vol = (3.14 * r * r * h).toFixed(1);
                document.getElementById('out').innerText = 'Volume = ' + vol + ' m³ (' + (vol * 1000) + ' Litros)';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Volume de qualquer Prisma/Cilindro reto = $\\text{Área da Base} \\cdot \\text{Altura}$ ($V = A_b \\cdot h$). $1\\text{ m}^3 = 1000\\text{ Litros}$ e $1\\text{ cm}^3 = 1\\text{ mL}$.")

# =============================================================================
# 11. GEOMETRIA ESPACIAL - CONES & ESFERAS
# =============================================================================
elif jogo == "11. Geometria Espacial (Cones & Esferas)":
    st.subheader("🍦 11. Volume de Cones e Esferas")
    st.success("🎯 **O que fazer:** Mude o raio da esfera e veja como o volume cresce ao cubo ($r^3$)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">⚽ Raio da Esfera (r): <input type="range" id="r" min="1" max="6" value="3" oninput="c()"> <span id="rv">3 cm</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #a371f7;"><b id="out" style="color:#a371f7;">-</b></div>
        </div>
        <script>
            function c(){
                let r = parseInt(document.getElementById('r').value);
                document.getElementById('rv').innerText = r + ' cm';
                let vol = ((4/3) * 3.14 * r * r * r).toFixed(1);
                document.getElementById('out').innerText = 'Volume da Esfera (V = 4/3 π.r³) = ' + vol + ' cm³';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Se 'tem bico' (Cone ou Pirâmide), divide por 3 ($V = \\frac{A_b \\cdot h}{3}$). O volume da esfera é $V = \\frac{4}{3} \\pi r^3$.")

# =============================================================================
# 12. ESCALA
# =============================================================================
elif jogo == "12. Escala, Mapas & Projeção Ortogonal":
    st.subheader("🗺️ 12. Escala Cartográfica em Mapas")
    st.success("🎯 **O que fazer:** Calcule a distância real em quilômetros medindo centímetros no mapa!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">📏 Medida no Mapa: <input type="range" id="d" min="1" max="20" value="5" oninput="c()"> <span id="dv">5 cm</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">Escala 1:100.000 (1 cm = 1 km)</b></div>
        </div>
        <script>
            function c(){
                let d = parseInt(document.getElementById('d').value);
                document.getElementById('dv').innerText = d + ' cm';
                document.getElementById('out').innerText = 'Distância Real = ' + d + ' km (' + (d*100000) + ' cm na realidade)';
            }
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** $E = \\frac{d}{D}$ (Escala = distância no mapa sobre distância real na mesma unidade!). Para áreas, eleve a escala ao quadrado ($E^2$).")

# =============================================================================
# 13. ANÁLISE DE GRÁFICOS
# =============================================================================
elif jogo == "13. Leitura e Análise de Gráficos":
    st.subheader("📈 13. Interpretação de Gráficos e Tabelas")
    st.success("🎯 **O que fazer:** Analise o crescimento do gráfico de barras em tempo real.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <canvas id="c" width="450" height="130"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function d(){
                ctx.clearRect(0,0,450,130);
                let data = [30, 50, 90, 70, 110];
                data.forEach((val, i) => {
                    ctx.fillStyle="#58a6ff"; ctx.fillRect(40 + i*80, 120-val, 40, val);
                    ctx.fillStyle="#fff"; ctx.fillText("M"+(i+1), 50 + i*80, 125);
                });
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** Atente-se sempre às unidades dos eixos $X$ e $Y$ e aos títulos do gráfico antes de fazer os cálculos!")

# =============================================================================
# 14. JUROS SIMPLES VS COMPOSTOS
# =============================================================================
elif jogo == "14. Juros Simples vs Juros Compostos":
    st.subheader("💰 14. Comparativo: Juros Simples vs Compostos")
    st.success("🎯 **O que fazer:** Aumente o tempo em meses e observe os Juros Compostos (exponencial) superarem os Juros Simples (linear)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">⏱️ Tempo: <input type="range" id="t" min="1" max="24" value="12" oninput="c()"> <span id="tv">12 meses</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #7ee787;">Capital: R$ 1000 | Taxa: 10% a.m.</div>
            <div class="card" style="border: 1px solid #e3b341;"><b id="out" style="color:#e3b341;">-</b></div>
        </div>
        <script>
            function c(){
                let t = parseInt(document.getElementById('t').value);
                document.getElementById('tv').innerText = t + ' meses';
                let simples = 1000 + (1000 * 0.10 * t);
                let compostos = 1000 * Math.pow(1.10, t);
                document.getElementById('out').innerText = 'Simples: R$ ' + simples.toFixed(2) + ' | Compostos: R$ ' + compostos.toFixed(2);
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Juros Simples: $J = C \\cdot i \\cdot t$. Juros Compostos (juros sobre juros): $M = C(1 + i)^t$.")

# =============================================================================
# 15. PROGRESSÃO ARITMÉTICA
# =============================================================================
elif jogo == "15. Progressão Aritmética (PA)":
    st.subheader("🔢 15. Termo Geral e Soma da P.A.")
    st.success("🎯 **O que fazer:** Altere a razão da P.A. e veja os termos crescerem somando uma constante!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">➕ Razão (r): <input type="range" id="r" min="1" max="10" value="3" oninput="c()"> <span id="rv">3</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="out" style="color:#58a6ff;">-</b></div>
        </div>
        <script>
            function c(){
                let r = parseInt(document.getElementById('r').value);
                document.getElementById('rv').innerText = r;
                let seq = [];
                for(let i=0; i<5; i++) seq.push(2 + i*r);
                document.getElementById('out').innerText = 'P.A. (a1=2): [' + seq.join(', ') + '...]';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Termo geral da P.A.: $a_n = a_1 + (n-1)r$. Soma dos $n$ primeiros termos: $S_n = \\frac{(a_1 + a_n)n}{2}$.")

# =============================================================================
# 16. PROGRESSÃO GEOMÉTRICA
# =============================================================================
elif jogo == "16. Progressão Geométrica (PG)":
    st.subheader("🚀 16. Crescimento Exponencial da P.G.")
    st.success("🎯 **O que fazer:** Aumente a razão ($q$) da P.G. e veja os números multiplicarem rapidamente.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">✖️ Razão (q): <input type="range" id="q" min="2" max="5" value="2" oninput="c()"> <span id="qv">2</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #f0883e;"><b id="out" style="color:#f0883e;">-</b></div>
        </div>
        <script>
            function c(){
                let q = parseInt(document.getElementById('q').value);
                document.getElementById('qv').innerText = q;
                let seq = [];
                for(let i=0; i<5; i++) seq.push(3 * Math.pow(q, i));
                document.getElementById('out').innerText = 'P.G. (a1=3): [' + seq.join(', ') + '...]';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Termo geral da P.G.: $a_n = a_1 \\cdot q^{n-1}$. Se a razão $|q| < 1$, a P.G. é decrescente!")

# =============================================================================
# 17. FUNÇÃO EXPONENCIAL & LOGARITMOS
# =============================================================================
elif jogo == "17. Função Exponencial & Logaritmos":
    st.subheader("📉 17. Relação entre Exponencial e Logaritmo")
    st.success("🎯 **O que fazer:** Veja como o logaritmo é o inverso da exponenciação ($b^y = x \\iff \\log_b(x) = y$).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">Exponent (y): <input type="range" id="y" min="0" max="6" value="3" oninput="c()"> <span id="yv">3</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #a371f7;"><b id="out" style="color:#a371f7;">-</b></div>
        </div>
        <script>
            function c(){
                let y = parseInt(document.getElementById('y').value);
                document.getElementById('yv').innerText = y;
                let x = Math.pow(2, y);
                document.getElementById('out').innerText = '2^' + y + ' = ' + x + '  ⟺  log₂( ' + x + ' ) = ' + y;
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Propriedades dos Logs: $\\log(a \\cdot b) = \\log(a) + \\log(b)$ e $\\log(a^k) = k \\cdot \\log(a)$ (Regra do 'Peleco'!).")

# =============================================================================
# 18. GEOMETRIA ANALÍTICA
# =============================================================================
elif jogo == "18. Geometria Analítica (Distância e Reta)":
    st.subheader("📍 18. Distância Entre Dois Pontos no Plano Cartesiano")
    st.success("🎯 **O que fazer:** Ajuste as coordenadas do ponto B e veja a distância $d = \\sqrt{\\Delta x^2 + \\Delta y^2}$ ser calculada!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">Ponto A: (0, 0)</div>
        <div class="card">Ponto B: (<input type="range" id="xb" min="1" max="10" value="3" oninput="c()"><span id="xbv">3</span>, <input type="range" id="yb" min="1" max="10" value="4" oninput="c()"><span id="ybv">4</span>)</div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function c(){
                let x = parseInt(document.getElementById('xb').value);
                let y = parseInt(document.getElementById('yb').value);
                document.getElementById('xbv').innerText = x; document.getElementById('ybv').innerText = y;
                let dist = Math.sqrt(x*x + y*y).toFixed(2);
                document.getElementById('out').innerText = 'Distância d(A,B) = ' + dist;
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** A distância entre dois pontos é simplesmente aplicar Pitágoras na variação dos eixos: $d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.")

# =============================================================================
# 19. CICLO TRIGONOMÉTRICO
# =============================================================================
elif jogo == "19. Ciclo Trigonométrico (Seno e Cosseno)":
    st.subheader("⭕ 19. Seno no Eixo Y e Cosseno no Eixo X")
    st.success("🎯 **O que fazer:** Gire o ângulo no ciclo trigonométrico para acompanhar os valores de Seno e Cosseno.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">📐 Ângulo: <input type="range" id="a" min="0" max="360" step="30" value="30" oninput="c()"> <span id="av">30°</span></div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="out" style="color:#58a6ff;">-</b></div>
        </div>
        <script>
            function c(){
                let deg = parseInt(document.getElementById('a').value);
                document.getElementById('av').innerText = deg + '°';
                let rad = deg * Math.PI / 180;
                let sen = Math.sin(rad).toFixed(2);
                let cos = Math.cos(rad).toFixed(2);
                document.getElementById('out').innerText = 'Sen(' + deg + '°) = ' + sen + ' | Cos(' + deg + '°) = ' + cos;
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** **Seno** está 'SEM sono' (em pé, no eixo Y). **Cosseno** está 'COM sono' (deitado, no eixo X)!")

# =============================================================================
# 20. SISTEMAS LINEARES
# =============================================================================
elif jogo == "20. Sistemas Lineares & Matrizes":
    st.subheader("🔢 20. Resolução de Sistemas $2 \\times 2$")
    st.success("🎯 **O que fazer:** Encontre o ponto de interseção $(x, y)$ das duas equações lineares.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            System: <br>
            x + y = 10 <br>
            x - y = 4
        </div>
        <div style="margin-top:8px;">
            <div class="card" style="border: 1px solid #7ee787;"><b style="color:#7ee787;">Solução: x = 7, y = 3</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** Você pode resolver sistemas por **Adição** (somando as equações para cancelar uma variável) ou por **Substituição**!")