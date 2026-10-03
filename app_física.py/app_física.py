import streamlit as st
import streamlit.components.v1 as components

# Configuração da Página
st.set_page_config(page_title="20 Jogos de Física pro ENEM", page_icon="⚡", layout="wide")

st.title("⚡ 20 Jogos & Simuladores Interativos de Física pro ENEM")
st.write("Aprenda a Física cobrada no ENEM jogando em tempo real no seu navegador!")

# Menu Lateral com os 20 Jogos
st.sidebar.header("🕹️ Selecione o Jogo (1 a 20)")
jogo = st.sidebar.radio("Módulos Interativos:", [
    "01. Lei de Ohm & Potência (Circuito)",
    "02. Circuito Série vs Paralelo",
    "03. Consumo Elétrico (kWh & Chuveiro)",
    "04. Equação Fundamental da Onda (v = λ.f)",
    "05. Efeito Doppler (Ambulância)",
    "06. Refração de Ondas na Água",
    "07. Interferência de Ondas (Fones de Ouvido)",
    "08. Gás Ideal (P.V = n.R.T)",
    "09. Calorimetria (Q = m.c.ΔT)",
    "10. Máquina Térmica & Rendimento",
    "11. Montanha-Russa (Energia Mecânica)",
    "12. Corrida: MRU vs MRUV",
    "13. Lançamento Oblíquo (Canhão)",
    "14. Plano Inclinado & Atrito",
    "15. Colisões & Impulso (Q = m.v)",
    "16. Empuxo & Arquimedes (Flutuação)",
    "17. Prensa Hidráulica (Princípio de Pascal)",
    "18. Espelho Côncavo (Óptica de Gauss)",
    "19. Refração da Luz & Lei de Snell",
    "20. Indução Eletromagnética (Gerador)"
])

st.sidebar.divider()
st.sidebar.caption("🎯 **Dica ENEM:** Mova os botões e barras deslizantes de cada jogo para observar as transformações ao vivo!")

# =============================================================================
# 01. LEI DE OHM & POTÊNCIA
# =============================================================================
if jogo == "01. Lei de Ohm & Potência (Circuito)":
    st.subheader("💡 01. Circuito Elétrico & Potência da Lâmpada")
    st.success("🎯 **O que fazer:** Altere a Voltagem (V) e a Resistência (R). Veja os elétrons mudarem de velocidade e o brilho da lâmpada aumentar!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
        canvas { border: 2px solid #e3b341; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div>
            <div class="card">🔋 Tensão (V): <input type="range" id="v" min="1" max="60" value="12" oninput="u()"> <span id="vv">12V</span></div>
            <div class="card">🧱 Resistência (R): <input type="range" id="r" min="1" max="20" value="4" oninput="u()"> <span id="rv">4Ω</span></div>
            <div class="card">⚡ Potência: <b id="pv" style="color:#e3b341;">36W</b></div>
        </div>
        <canvas id="c" width="480" height="180"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), p=Array.from({length:15},(_,i)=>({pos:i*30}));
            function u(){
                let V=parseFloat(document.getElementById('v').value), R=parseFloat(document.getElementById('r').value);
                document.getElementById('vv').innerText=V+'V'; document.getElementById('rv').innerText=R+'Ω';
                document.getElementById('pv').innerText=(V*V/R).toFixed(1)+'W';
            }
            function d(){
                ctx.clearRect(0,0,480,180);
                let V=parseFloat(document.getElementById('v').value), R=parseFloat(document.getElementById('r').value), I=V/R, P=V*I;
                ctx.strokeStyle="#8b949e"; ctx.lineWidth=4; ctx.strokeRect(40,30,400,120);
                ctx.beginPath(); ctx.arc(240,30,18,0,Math.PI*2); ctx.fillStyle=`rgba(255,223,0,${Math.min(P/150,1)})`; ctx.fill(); ctx.stroke();
                ctx.fillStyle="#e3b341";
                p.forEach(e=>{
                    e.pos=(e.pos+I*0.5)%1040;
                    let x=40, y=30;
                    if(e.pos<400) { x=40+e.pos; y=30; }
                    else if(e.pos<520) { x=440; y=30+(e.pos-400); }
                    else if(e.pos<920) { x=440-(e.pos-520); y=150; }
                    else { x=40; y=150-(e.pos-920); }
                    ctx.beginPath(); ctx.arc(x,y,5,0,Math.PI*2); ctx.fill();
                });
                requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=270)
    st.info("💡 **Macete ENEM:** $V = R \\cdot I$ ('Quem Vê Rir') e $P = V \\cdot I$ ('Piu'). Quanto maior a potência da lâmpada ou chuveiro, mais energia consome!")

# =============================================================================
# 02. CIRCUITO SÉRIE VS PARALELO
# =============================================================================
elif jogo == "02. Circuito Série vs Paralelo":
    st.subheader("🔌 02. Comparador: Circuito Série vs Paralelo")
    st.success("🎯 **O que fazer:** Desligue a Lâmpada 1 de cada circuito. No circuito Série, tudo apaga; no Paralelo, as outras continuam ligadas!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; margin: 2px; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div>
            <button onclick="s1=!s1">Lâmpada 1 Série</button>
            <button onclick="p1=!p1">Lâmpada 1 Paralelo</button>
        </div>
        <canvas id="c" width="480" height="180" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), s1=true, p1=true;
            function d(){
                ctx.clearRect(0,0,480,180);
                // Série
                ctx.strokeStyle="#8b949e"; ctx.lineWidth=3; ctx.strokeRect(30,20,180,130);
                ctx.fillStyle=s1?"#f2cc60":"#484f58";
                ctx.beginPath(); ctx.arc(120,20,14,0,Math.PI*2); ctx.fill(); ctx.stroke();
                ctx.beginPath(); ctx.arc(120,150,14,0,Math.PI*2); ctx.fill(); ctx.stroke();
                ctx.fillStyle="#fff"; ctx.fillText("SÉRIIE (Um falha = Tudo apaga)", 25,170);

                // Paralelo
                ctx.strokeRect(270,20,180,130); ctx.beginPath(); ctx.moveTo(360,20); ctx.lineTo(360,150); ctx.stroke();
                ctx.fillStyle=p1?"#f2cc60":"#484f58"; ctx.beginPath(); ctx.arc(360,50,14,0,Math.PI*2); ctx.fill(); ctx.stroke();
                ctx.fillStyle="#f2cc60"; ctx.beginPath(); ctx.arc(360,120,14,0,Math.PI*2); ctx.fill(); ctx.stroke();
                ctx.fillStyle="#fff"; ctx.fillText("PARALELO (Independente)", 280,170);
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=260)
    st.info("💡 **Macete ENEM:** Na sua casa, os aparelhos ficam ligados em PARALELO, para que funcionem com a mesma voltagem e de maneira independente!")

# =============================================================================
# 03. CONSUMO ELÉTRICO
# =============================================================================
elif jogo == "03. Consumo Elétrico (kWh & Chuveiro)":
    st.subheader("🚿 03. Simulador de Conta de Luz do Chuveiro")
    st.success("🎯 **O que fazer:** Altere o tempo do banho e a potência do chuveiro para ver o impacto direto em Reais (R$) no final do mês.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">⏱️ Banho (min/dia): <input type="range" id="t" min="5" max="60" value="20" oninput="c()"> <span id="tv">20 min</span></div>
        <div class="card">🔥 Potência (W): <input type="range" id="p" min="2000" max="7500" step="500" value="5500" oninput="c()"> <span id="pv">5500W</span></div>
        <div class="card" style="border: 1px solid #7ee787;">💰 Custo Mensal estimado: <b id="cost" style="color:#7ee787; font-size: 1.2em;">R$ 0,00</b></div>
        <script>
            function c(){
                let t = parseFloat(document.getElementById('t').value);
                let p = parseFloat(document.getElementById('p').value);
                document.getElementById('tv').innerText = t + ' min';
                document.getElementById('pv').innerText = p + 'W';
                let kwh = (p / 1000) * (t / 60) * 30; // 30 dias
                let rs = kwh * 0.85; // R$ 0,85 por kWh
                document.getElementById('cost').innerText = 'R$ ' + rs.toFixed(2);
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** $E_{kWh} = \\frac{P(W) \\cdot t(h)}{1000}$. Converta sempre a potência para kW e o tempo para Horas!")

# =============================================================================
# 04. EQUAÇÃO FUNDAMENTAL DA ONDA
# =============================================================================
elif jogo == "04. Equação Fundamental da Onda (v = λ.f)":
    st.subheader("🌊 04. Equação Fundamental da Onda")
    st.success("🎯 **O que fazer:** Varie a frequência (f) e o comprimento de onda (λ) para calcular a velocidade de propagação (v).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div>
            <div class="card">📻 Frequência (f): <input type="range" id="f" min="1" max="8" value="2" oninput="u()"> <span id="fv">2 Hz</span></div>
            <div class="card">📏 Lambda (λ): <input type="range" id="l" min="20" max="100" value="60" oninput="u()"> <span id="lv">60 px</span></div>
            <div class="card">🚀 Velocidade: <b id="vv" style="color:#58a6ff;">120 px/s</b></div>
        </div>
        <canvas id="c" width="480" height="150"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), t=0;
            function u(){
                let f=parseFloat(document.getElementById('f').value), l=parseFloat(document.getElementById('l').value);
                document.getElementById('fv').innerText=f+' Hz'; document.getElementById('lv').innerText=l+' px';
                document.getElementById('vv').innerText=(f*l)+' px/s';
            }
            function d(){
                ctx.clearRect(0,0,480,150);
                let f=parseFloat(document.getElementById('f').value), l=parseFloat(document.getElementById('l').value);
                ctx.beginPath(); ctx.strokeStyle="#58a6ff"; ctx.lineWidth=3;
                for(let x=0; x<480; x++){
                    let y=75 + Math.sin((x/l - t*f)*Math.PI*2)*35;
                    if(x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
                }
                ctx.stroke(); t+=0.015; requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=260)
    st.info("💡 **Macete ENEM:** 'Vem Lamber Ferida' ($v = \\lambda \\cdot f$). Quando a onda muda de meio (Refração), a frequência $f$ NUNCA muda!")

# =============================================================================
# 05. EFEITO DOPPLER
# =============================================================================
elif jogo == "05. Efeito Doppler (Ambulância)":
    st.subheader("🚑 05. Efeito Doppler em Movimento")
    st.success("🎯 **O que fazer:** Aumente a velocidade da fonte e veja as frentes de onda se comprimirem na frente (som agudo) e se espaçarem atrás (som grave)!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #ff7b72; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">🏎️ Velocidade do Veículo: <input type="range" id="v" min="0" max="4" value="2"></div>
        <canvas id="c" width="480" height="170" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), x=50, waves=[];
            function d(){
                ctx.clearRect(0,0,480,170);
                let speed=parseFloat(document.getElementById('v').value);
                x+=speed; if(x>430) x=50;
                if(Math.random()<0.1) waves.push({x:x, y:85, r:5});
                ctx.strokeStyle="#ff7b72"; ctx.lineWidth=2;
                waves.forEach((w,i)=>{
                    w.r+=1.5; ctx.beginPath(); ctx.arc(w.x, w.y, w.r, 0, Math.PI*2); ctx.stroke();
                    if(w.r>150) waves.splice(i,1);
                });
                ctx.fillStyle="#fff"; ctx.fillRect(x-10,75,20,20);
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=260)
    st.info("💡 **Macete ENEM:** Aproximação = Frequência aparente maior (som Agudo). Afastamento = Frequência aparente menor (som Grave).")

# =============================================================================
# 06. REFRAÇÃO DE ONDAS
# =============================================================================
elif jogo == "06. Refração de Ondas na Água":
    st.subheader("🏊 06. Refração de Ondas na Mudança de Meio")
    st.success("🎯 **O que fazer:** Observe a onda passar do meio raso para o profundo: o comprimento de onda e a velocidade mudam, mas a frequência continua igual!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #79c0ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <canvas id="c" width="480" height="150"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), t=0;
            function d(){
                ctx.clearRect(0,0,480,150);
                ctx.fillStyle="rgba(31,107,235,0.2)"; ctx.fillRect(240,0,240,150);
                ctx.fillStyle="#fff"; ctx.fillText("Meio 1 (Raso)", 80, 20); ctx.fillText("Meio 2 (Profundo)", 300, 20);
                ctx.beginPath(); ctx.strokeStyle="#79c0ff"; ctx.lineWidth=3;
                for(let x=0; x<480; x++){
                    let l = (x < 240) ? 30 : 60;
                    let y = 75 + Math.sin((x/l - t*2)*Math.PI*2)*30;
                    if(x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
                }
                ctx.stroke(); t+=0.02; requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** Na refração: Frequência ($f$) é CONSTANTE! Se a velocidade $v$ aumenta, o comprimento de onda $\\lambda$ também aumenta.")

# =============================================================================
# 07. INTERFERÊNCIA DE ONDAS
# =============================================================================
elif jogo == "07. Interferência de Ondas (Fones de Ouvido)":
    st.subheader("🔊 07. Interferência Construtiva vs Destrutiva")
    st.success("🎯 **O que fazer:** Mude a diferença de fase entre duas ondas para observar o cancelamento total (linha reta) ou amplificação do som!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #d29922; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">🎛️ Diferença de Fase: <input type="range" id="ph" min="0" max="3.14" step="0.1" value="0"></div>
        <canvas id="c" width="480" height="150" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), t=0;
            function d(){
                ctx.clearRect(0,0,480,150);
                let ph=parseFloat(document.getElementById('ph').value);
                ctx.beginPath(); ctx.strokeStyle="#d29922"; ctx.lineWidth=3;
                for(let x=0; x<480; x++){
                    let y1 = Math.sin((x/40 - t*3)*Math.PI*2)*20;
                    let y2 = Math.sin((x/40 - t*3 + ph)*Math.PI*2)*20;
                    let y = 75 + y1 + y2;
                    if(x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
                }
                ctx.stroke(); t+=0.015; requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** Fones de ouvido com cancelamento ativo usam **Interferência Destrutiva** criando uma onda sonora invertida!")

# =============================================================================
# 08. GÁS IDEAL
# =============================================================================
elif jogo == "08. Gás Ideal (P.V = n.R.T)":
    st.subheader("🔥 08. Estudo dos Gases & Pressão")
    st.success("🎯 **O que fazer:** Diminua a largura do recipiente ou aumente a Temperatura para ver a pressão e as colisões aumentarem!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
        canvas { border: 2px solid #ff7b72; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div>
            <div class="card">🌡️ Temp (T): <input type="range" id="t" min="100" max="600" value="300" oninput="u()"> <span id="tv">300K</span></div>
            <div class="card">📦 Vol (V): <input type="range" id="v" min="150" max="420" value="350" oninput="u()"> <span id="vv">350</span></div>
        </div>
        <canvas id="c" width="450" height="150"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            let p=Array.from({length:20},()=>({x:Math.random()*200+10, y:Math.random()*120+10, vx:(Math.random()-0.5)*4, vy:(Math.random()-0.5)*4}));
            function u(){ document.getElementById('tv').innerText=document.getElementById('t').value+'K'; document.getElementById('vv').innerText=document.getElementById('v').value; }
            function d(){
                ctx.clearRect(0,0,450,150);
                let T=parseFloat(document.getElementById('t').value), V=parseFloat(document.getElementById('v').value);
                ctx.strokeStyle="#ff7b72"; ctx.lineWidth=3; ctx.strokeRect(0,0,V,150);
                let sp=Math.sqrt(T/300);
                ctx.fillStyle="#ff7b72";
                p.forEach(e=>{
                    e.x+=e.vx*sp; e.y+=e.vy*sp;
                    if(e.x<5||e.x>V-5) e.vx*=-1; if(e.y<5||e.y>145) e.vy*=-1;
                    ctx.beginPath(); ctx.arc(e.x,e.y,5,0,Math.PI*2); ctx.fill();
                });
                requestAnimationFrame(d);
            }
            u(); d();
        </script>
    </body></html>
    """
    components.html(html, height=260)
    st.info("💡 **Macete ENEM:** $P \\cdot V = n \\cdot R \\cdot T$ ('Por Você Nunca Rezei Tanto'). Temperatura é a medida direta da energia cinética das partículas!")

# =============================================================================
# 09. CALORIMETRIA
# =============================================================================
elif jogo == "09. Calorimetria (Q = m.c.ΔT)":
    st.subheader("☕ 09. Trocas de Calor & Calor Sensível")
    st.success("🎯 **O que fazer:** Forneça calor para a Água e para o Alumínio simultaneamente e veja como a substância de menor calor específico aquece mais rápido!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        button { background: #da3633; color: white; border: none; padding: 8px 16px; font-weight: bold; border-radius: 6px; cursor: pointer; }
    </style></head><body>
        <button onclick="heat()">🔥 FORNECER 1000 cal DE CALOR</button>
        <div style="margin-top:10px;">
            <div class="card">💧 Água (c = 1.0): <b id="ta" style="color:#58a6ff;">20.0 °C</b></div>
            <div class="card">0️⃣ Alumínio (c = 0.2): <b id="tal" style="color:#f0883e;">20.0 °C</b></div>
        </div>
        <script>
            let ta = 20.0, tal = 20.0;
            function heat(){
                ta += 1000 / (100 * 1.0);
                tal += 1000 / (100 * 0.2);
                document.getElementById('ta').innerText = ta.toFixed(1) + ' °C';
                document.getElementById('tal').innerText = tal.toFixed(1) + ' °C';
            }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** 'Qualamacete' ($Q = m \\cdot c \\cdot \\Delta T$). Maior calor específico ($c$) = Maior resistência a variar a temperatura!")

# =============================================================================
# 10. MÁQUINA TÉRMICA
# =============================================================================
elif jogo == "10. Máquina Térmica & Rendimento":
    st.subheader("⚙️ 10. Ciclo de Carnot & Rendimento Térmico")
    st.success("🎯 **O que fazer:** Ajuste as temperaturas Quente ($T_Q$) e Fria ($T_F$) para ver o limite teórico de rendimento ($\eta$) de uma máquina térmica.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div>
            <div class="card">🔥 Fonte Quente (Tq): <input type="range" id="tq" min="400" max="1000" value="600" oninput="c()"> <span id="tqv">600K</span></div>
            <div class="card">❄️ Fonte Fria (Tf): <input type="range" id="tf" min="100" max="390" value="300" oninput="c()"> <span id="tfv">300K</span></div>
            <div class="card">📊 Rendimento Carnot: <b id="eta" style="color:#7ee787; font-size:1.2em;">50%</b></div>
        </div>
        <script>
            function c(){
                let Tq = parseFloat(document.getElementById('tq').value);
                let Tf = parseFloat(document.getElementById('tf').value);
                document.getElementById('tqv').innerText = Tq + 'K';
                document.getElementById('tfv').innerText = Tf + 'K';
                let eta = (1 - (Tf / Tq)) * 100;
                document.getElementById('eta').innerText = eta.toFixed(1) + '%';
            }
            c();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Rendimento de Carnot: $\\eta = 1 - \\frac{T_F}{T_Q}$. Lembre-se: As temperaturas DEVEM estar em Kelvin (K = °C + 273)!")

# =============================================================================
# 11. MONTANHA-RUSSA
# =============================================================================
elif jogo == "11. Montanha-Russa (Energia Mecânica)":
    st.subheader("🛹 11. Conservação da Energia Mecânica")
    st.success("🎯 **O que fazer:** Acompanhe a conversão contínua entre Energia Potencial Gravitacional ($E_p$) no topo e Energia Cinética ($E_c$) na base.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #7ee787; background: #161b22; border-radius: 8px; }
        .bar { height: 14px; border-radius: 6px; display: inline-block; }
    </style></head><body>
        <div style="margin-bottom:6px;">
            Ep: <div id="ep" class="bar" style="background:#7ee787; width:100px;"></div>
            Ec: <div id="ec" class="bar" style="background:#58a6ff; width:0px;"></div>
        </div>
        <canvas id="c" width="480" height="150"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), t=0;
            function d(){
                ctx.clearRect(0,0,480,150);
                ctx.beginPath(); ctx.strokeStyle="#8b949e"; ctx.lineWidth=3;
                for(let x=0; x<480; x++){
                    let y=85 + Math.cos(x*0.015)*50;
                    if(x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
                }
                ctx.stroke();
                let cx = 240 + Math.sin(t)*180;
                let cy = 85 + Math.cos(cx*0.015)*50;
                let h = (140-cy)/100;
                document.getElementById('ep').style.width = (h*120)+'px';
                document.getElementById('ec').style.width = ((1-h)*120)+'px';
                ctx.fillStyle="#7ee787"; ctx.beginPath(); ctx.arc(cx,cy-8,10,0,Math.PI*2); ctx.fill();
                t+=0.03; requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** Sem atrito, a Energia Mecânica se conserva ($E_{Mec} = E_p + E_c$). No topo $v=0$, e na base a velocidade é máxima!")

# =============================================================================
# 12. CORRIDA: MRU VS MRUV
# =============================================================================
elif jogo == "12. Corrida: MRU vs MRUV":
    st.subheader("🏎️ 12. Comparativo: Velocidade Constante vs Aceleração")
    st.success("🎯 **O que fazer:** Dê a largada e observe como o veículo em MRUV começa atrás mas ultrapassa o veículo em MRU devido à Aceleração constante!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #388bfd; background: #161b22; border-radius: 8px; }
        button { background: #238636; color: white; border: none; padding: 6px 14px; font-weight: bold; border-radius: 4px; cursor: pointer; }
    </style></head><body>
        <button onclick="x1=10; x2=10; t=0; run=true">🚦 LARGADA</button>
        <canvas id="c" width="480" height="120" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), x1=10, x2=10, t=0, run=false;
            function d(){
                ctx.clearRect(0,0,480,120);
                ctx.strokeStyle="#30363d"; ctx.strokeRect(0,10,480,45); ctx.strokeRect(0,65,480,45);
                if(run && x2<440){
                    t+=0.05;
                    x1 = 10 + 3.5 * t * 10;
                    x2 = 10 + 0.5 * 1.8 * (t**2) * 10;
                }
                ctx.fillStyle="#ff4b4b"; ctx.fillRect(x1,20,25,18); ctx.fillText("MRU (v cst)",10,10);
                ctx.fillStyle="#58a6ff"; ctx.fillRect(x2,75,25,18); ctx.fillText("MRUV (Acelerado)",10,65);
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=210)
    st.info("💡 **Macete ENEM:** MRU usa 'Sorvete' ($S = S_0 + v \\cdot t$). MRUV usa 'Sorvetão' ($S = S_0 + v_0 t + \\frac{1}{2}a t^2$).")

# =============================================================================
# 13. LANÇAMENTO OBLÍQUO
# =============================================================================
elif jogo == "13. Lançamento Oblíquo (Canhão)":
    st.subheader("🎯 13. Ângulo e Alcance do Lançamento Oblíquo")
    st.success("🎯 **O que fazer:** Modifique o ângulo do canhão para disparar o projétil. O alcance máximo sempre acontece com o ângulo de 45°!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #f0883e; background: #161b22; border-radius: 8px; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
    </style></head><body>
        <div class="card">📐 Ângulo: <input type="range" id="a" min="15" max="75" value="45"> <span id="av">45°</span></div>
        <button onclick="fire()">🚀 ATIRAR</button>
        <canvas id="c" width="480" height="140" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), px=20, py=120, vx=0, vy=0, run=false;
            document.getElementById('a').oninput=function(){ document.getElementById('av').innerText=this.value+'°'; };
            function fire(){
                let rad = parseFloat(document.getElementById('a').value) * Math.PI / 180;
                px=20; py=120; vx=12*Math.cos(rad); vy=-12*Math.sin(rad); run=true;
            }
            function d(){
                ctx.clearRect(0,0,480,140);
                ctx.strokeStyle="#8b949e"; ctx.beginPath(); ctx.moveTo(0,130); ctx.lineTo(480,130); ctx.stroke();
                if(run){
                    px+=vx; py+=vy; vy+=0.4;
                    if(py>=120){ py=120; run=false; }
                }
                ctx.fillStyle="#f0883e"; ctx.beginPath(); ctx.arc(px,py,6,0,Math.PI*2); ctx.fill();
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=250)
    st.info("💡 **Macete ENEM:** Ângulos complementares (ex: 30° e 60°) têm exatamente o mesmo alcance horizontal!")

# =============================================================================
# 14. PLANO INCLINADO
# =============================================================================
elif jogo == "14. Plano Inclinado & Atrito":
    st.subheader("⛰️ 14. Decomposição de Forças no Plano Inclinado")
    st.success("🎯 **O que fazer:** Aumente a inclinação da rampa até que a componente descendente do Peso ($P_x$) supere o atrito estático!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #a371f7; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">📐 Inclinação: <input type="range" id="a" min="0" max="45" value="15"> <span id="av">15°</span></div>
        <canvas id="c" width="450" height="140" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            document.getElementById('a').oninput=function(){ document.getElementById('av').innerText=this.value+'°'; };
            function d(){
                ctx.clearRect(0,0,450,140);
                let deg=parseFloat(document.getElementById('a').value), rad=deg*Math.PI/180;
                let x2=400, y2=120 - Math.tan(rad)*300;
                ctx.strokeStyle="#8b949e"; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(50,120); ctx.lineTo(x2,y2); ctx.lineTo(x2,120); ctx.closePath(); ctx.stroke();
                ctx.fillStyle="#a371f7"; ctx.fillRect(200, 120 - Math.tan(rad)*150 - 20, 25,20);
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** $P_x = P \\cdot \\sin(\\theta)$ (para 'deXcer' o plano) e $P_y = P \\cdot \\cos(\\theta)$ ('CoCalado' no plano).")

# =============================================================================
# 15. COLISÕES & IMPULSO
# =============================================================================
elif jogo == "15. Colisões & Impulso (Q = m.v)":
    st.subheader("🎱 15. Conservação da Quantidade de Movimento")
    st.success("🎯 **O que fazer:** Lance a bola vermelha e observe a transferência de velocidade na colisão com a bola azul.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #f0883e; background: #161b22; border-radius: 8px; }
        button { background: #238636; color: white; border: none; padding: 6px 14px; border-radius: 4px; cursor: pointer; }
    </style></head><body>
        <button onclick="b1x=40; b2x=320; v1=5; v2=0;">🚀 LANCE A BOLA 1</button>
        <canvas id="c" width="450" height="110" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), b1x=40, b2x=320, v1=0, v2=0, m1=2, m2=4;
            function d(){
                ctx.clearRect(0,0,450,110);
                b1x+=v1; b2x+=v2;
                if(b2x-b1x <= 35 && v1>v2){
                    let v1f = ((m1-m2)*v1)/(m1+m2);
                    let v2f = (2*m1*v1)/(m1+m2);
                    v1=v1f; v2=v2f;
                }
                ctx.fillStyle="#ff4b4b"; ctx.beginPath(); ctx.arc(b1x,55,15,0,Math.PI*2); ctx.fill();
                ctx.fillStyle="#58a6ff"; ctx.beginPath(); ctx.arc(b2x,55,20,0,Math.PI*2); ctx.fill();
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** Teorema do Impulso ($I = F \\cdot \\Delta t = \\Delta Q$). Para amenizar impactos de batidas de carro, aumenta-se o tempo $\\Delta t$ com Airbags!")

# =============================================================================
# 16. EMPUXO & FLUTUAÇÃO
# =============================================================================
elif jogo == "16. Empuxo & Arquimedes (Flutuação)":
    st.subheader("⚓ 16. Empuxo e Princípio de Arquimedes")
    st.success("🎯 **O que fazer:** Modifique a densidade do objeto. Se for menor que a da água ($1.0\\text{ g/cm}^3$), ele flutua em equilíbrio estático!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #1f6beb; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">🪵 Densidade Bloco: <input type="range" id="d" min="0.2" max="1.8" step="0.1" value="0.5"> <span id="dv">0.5 g/cm³</span></div>
        <canvas id="c" width="450" height="140" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            document.getElementById('d').oninput=function(){ document.getElementById('dv').innerText=this.value+' g/cm³'; };
            function d(){
                ctx.clearRect(0,0,450,140);
                let den=parseFloat(document.getElementById('d').value);
                ctx.fillStyle="rgba(31,107,235,0.5)"; ctx.fillRect(0,50,450,90);
                let y = (den <= 1.0) ? 50 - 30 + (den * 30) : 100;
                ctx.fillStyle="#d29922"; ctx.fillRect(200,y,40,30); ctx.strokeRect(200,y,40,30);
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** Empuxo = Peso do Líquido Deslocado ($E = d_{líq} \\cdot V_{sub} \\cdot g$). Em objetos flutuantes, $Empuxo = Peso_{total}$!")

# =============================================================================
# 17. PRENSA HIDRÁULICA
# =============================================================================
elif jogo == "17. Prensa Hidráulica (Princípio de Pascal)":
    st.subheader("🚗 17. Multiplicação de Forças na Prensa Hidráulica")
    st.success("🎯 **O que fazer:** Empurre o pistão fino para erguer um veículo no pistão largo, aproveitando a igualdade de pressões!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        canvas { border: 2px solid #388bfd; background: #161b22; border-radius: 8px; }
        button { background: #238636; color: white; border: none; padding: 6px 14px; border-radius: 4px; cursor: pointer; }
    </style></head><body>
        <button onclick="py=Math.min(py+5,110)">Pressionar Êmbolo Menor</button>
        <canvas id="c" width="450" height="130" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), py=50;
            function d(){
                ctx.clearRect(0,0,450,130);
                let carY = 90 - (py-50)*0.2;
                ctx.fillStyle="rgba(56,139,253,0.4)";
                ctx.fillRect(50,py,40,130-py); ctx.fillRect(50,90,300,40); ctx.fillRect(250,carY,100,130-carY);
                ctx.fillStyle="#ff4b4b"; ctx.fillRect(50,py-10,40,10);
                ctx.fillStyle="#7ee787"; ctx.fillRect(250,carY-10,100,10);
                ctx.fillStyle="#fff"; ctx.fillText("🏎️ CARRO", 270, carY-20);
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=210)
    st.info("💡 **Macete ENEM:** $\\frac{F_1}{A_1} = \\frac{F_2}{A_2}$. A variação de pressão aplicada em um ponto do fluido é transmitida integralmente a todos os pontos!")

# =============================================================================
# 18. ESPELHO CÔNCAVO
# =============================================================================
elif jogo == "18. Espelho Côncavo (Óptica de Gauss)":
    st.subheader("🪞 18. Formação de Imagens em Espelhos Esféricos")
    st.success("🎯 **O que fazer:** Aproxime o objeto do espelho para observar a mudança no tamanho e na orientação da imagem formada.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #a371f7; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">🕯 Posição do Objeto: <input type="range" id="p" min="50" max="360" value="280"></div>
        <canvas id="c" width="450" height="150" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            function d(){
                ctx.clearRect(0,0,450,150);
                let ox=parseFloat(document.getElementById('p').value), F=300, C=200, E=380;
                ctx.strokeStyle="#8b949e"; ctx.beginPath(); ctx.moveTo(0,75); ctx.lineTo(450,75); ctx.stroke();
                ctx.fillStyle="#a371f7"; ctx.fillText("F",F,95); ctx.fillText("C",C,95);
                ctx.beginPath(); ctx.arc(E,75,60,Math.PI*0.7,Math.PI*1.3); ctx.stroke();
                ctx.strokeStyle="#f2cc60"; ctx.lineWidth=4; ctx.beginPath(); ctx.moveTo(ox,75); ctx.lineTo(ox,35); ctx.stroke();
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** $\\frac{1}{f} = \\frac{1}{p} + \\frac{1}{p'}$. Se o objeto está situado entre o Foco e o Espelho, a imagem é Virtual, Direita e Maior!")

# =============================================================================
# 19. REFRAÇÃO DA LUZ
# =============================================================================
elif jogo == "19. Refração da Luz & Lei de Snell":
    st.subheader("🌈 19. Desvio do Raio de Luz na Refração")
    st.success("🎯 **O que fazer:** Aumente o índice de refração do meio inferior ($n_2$) e veja o raio refratado se aproximar da linha normal!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #58a6ff; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">💎 Índice n2: <input type="range" id="n" min="1.0" max="2.4" step="0.1" value="1.5"> <span id="nv">1.5</span></div>
        <canvas id="c" width="450" height="150" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
            document.getElementById('n').oninput=function(){ document.getElementById('nv').innerText=this.value; };
            function d(){
                ctx.clearRect(0,0,450,150);
                let n2=parseFloat(document.getElementById('n').value);
                ctx.fillStyle="rgba(88,166,255,0.2)"; ctx.fillRect(0,75,450,75);
                ctx.strokeStyle="#8b949e"; ctx.setLineDash([4,4]); ctx.beginPath(); ctx.moveTo(225,0); ctx.lineTo(225,150); ctx.stroke(); ctx.setLineDash([]);
                ctx.strokeStyle="#ff7b72"; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(125,10); ctx.lineTo(225,75); ctx.stroke();
                let ang2 = Math.asin(Math.sin(45*Math.PI/180) / n2);
                let x2 = 225 + Math.sin(ang2)*80, y2 = 75 + Math.cos(ang2)*80;
                ctx.beginPath(); ctx.moveTo(225,75); ctx.lineTo(x2,y2); ctx.stroke();
                requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** Lei de Snell: $n_1 \\cdot \\sin(\\theta_1) = n_2 \\cdot \\sin(\\theta_2)$. Passando para um meio de maior índice de refração, o raio APROXIMA da normal!")

# =============================================================================
# 20. INDUÇÃO ELETROMAGNÉTICA
# =============================================================================
elif jogo == "20. Indução Eletromagnética (Gerador)":
    st.subheader("🧲 20. Lei de Faraday & Indução de Corrente")
    st.success("🎯 **O que fazer:** Arraste a barra do Ímã para dentro da espira. A variação do campo magnético induz corrente elétrica e acende a lâmpada!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
        canvas { border: 2px solid #d29922; background: #161b22; border-radius: 8px; }
    </style></head><body>
        <div class="card">🧲 Posição do Ímã: <input type="range" id="m" min="50" max="380" value="100"></div>
        <canvas id="c" width="450" height="140" style="margin-top:6px;"></canvas>
        <script>
            let canvas=document.getElementById('c'), ctx=canvas.getContext('2d'), prevX=100, sp=0;
            document.getElementById('m').oninput=function(){
                let x=parseFloat(this.value); sp=Math.abs(x-prevX); prevX=x;
            };
            function d(){
                ctx.clearRect(0,0,450,140);
                let mx=parseFloat(document.getElementById('m').value);
                ctx.strokeStyle="#d29922"; ctx.lineWidth=4;
                for(let i=0;i<5;i++){ ctx.beginPath(); ctx.ellipse(240+i*12,75,8,30,0,0,Math.PI*2); ctx.stroke(); }
                let glow=Math.min(sp/12,1);
                ctx.fillStyle=`rgba(255,223,0,${glow})`; ctx.beginPath(); ctx.arc(264,20,12,0,Math.PI*2); ctx.fill(); ctx.stroke();
                ctx.fillStyle="#ff4b4b"; ctx.fillRect(mx-30,63,30,24);
                ctx.fillStyle="#58a6ff"; ctx.fillRect(mx,63,30,24);
                sp*=0.9; requestAnimationFrame(d);
            }
            d();
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** Lei de Faraday: $\\epsilon = - \\frac{\\Delta \\Phi}{\\Delta t}$. Ímã parado = Sem variação de fluxo = Lâmpada Apagada!")