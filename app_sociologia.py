import streamlit as st
import streamlit.components.v1 as components

# Configuração da Página
st.set_page_config(page_title="23 Jogos Gigantes de Sociologia pro ENEM", page_icon="👥", layout="wide")

st.title("👥 23 Jogos & Simuladores de Sociologia pro ENEM (Versão Expandida)")
st.write("Aprenda os temas mais cobrados em Ciências Humanas com jogos maiores, caça-palavras gigante e dinâmicas interativas!")

# Menu Lateral com os 23 Jogos
st.sidebar.header("🕹️ Selecione o Módulo (1 a 23)")
jogo = st.sidebar.radio("Módulos Interativos:", [
    "01. Jogo da Memória Expandido (6 Pares)",
    "02. Desafio V ou F: As Formas de Ação Social (Weber)",
    "03. Termômetro de Capital Cultural (Bourdieu)",
    "04. Simulador do Panóptico e Sociedade de Controle",
    "05. Roleta de Desafios: Etnocentrismo vs Relativismo",
    "06. Caixa de Dilemas: Movimentos Sociais no Brasil",
    "07. Linha do Tempo Viva: As 3 Dimensões da Cidadania",
    "08. Quiz de Fixação: A Indústria Cultural (Adorno)",
    "09. Radar das Mudanças no Mundo do Trabalho",
    "10. Teste do Consumidor: Modernidade Líquida (Bauman)",
    "11. Laboratório da Desigualdade Social e Estratificação",
    "12. Batalha de Ideias: Instituições Sociais",
    "13. Palavra-Chave Oculta: Direitos Humanos",
    "14. Quiz Dinâmico: A Relação Indivíduo e Sociedade",
    "15. Mosaico da Diversidade e Patrimônio Cultural",
    "16. Conexão de Conceitos: Democracia e Estado",
    "17. Simulador de Fake News e Pós-Verdade",
    "18. Teste Rápido: Racismo Estrutural no Brasil",
    "19. Caça-Erros: Teorias do Positivismo de Auguste Comte",
    "20. Desafio do Trabalho: Taylorismo, Fordismo e Toyotismo",
    "21. Roleta do Conhecimento: Globalização e Exclusão",
    "22. Quiz de Competência: Sociologia da Violência",
    "23. Checklist do Conhecimento Nota 1000"
])

st.sidebar.divider()
st.sidebar.caption("🎯 **Dica ENEM:** Mova os controles, jogue e revise os conceitos essenciais da prova!")

# =============================================================================
# 01. JOGO DA MEMÓRIA EXPANDIDO (12 CARTAS / 6 PARES)
# =============================================================================
if jogo == "01. Jogo da Memória Expandido (6 Pares)":
    st.subheader("🃏 01. Jogo da Memória Gigante: 6 Pares da Sociologia")
    st.success("🎯 **O que fazer:** Encontre os 6 pares associando cada sociólogo ao seu conceito principal!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; max-width: 700px; margin: 15px auto; }
        .card { background: #21262d; border: 2px solid #58a6ff; border-radius: 8px; height: 90px; display: flex; align-items: center; justify-content: center; font-weight: bold; cursor: pointer; padding: 8px; font-size: 0.85em; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        .flipped { background: #238636 !important; border-color: #7ee787 !important; }
    </style></head><body>
        <div class="grid" id="board"></div>
        <div id="status" style="margin-top:15px; font-weight:bold; font-size:1.2em; color:#7ee787;"></div>
        <script>
            const items = [
                {id:1, txt:"Émile Durkheim", pair:10}, {id:10, txt:"Fato Social e Anomia", pair:1},
                {id:2, txt:"Karl Marx", pair:20}, {id:20, txt:"Mais-Valia e Luta de Classes", pair:2},
                {id:3, txt:"Max Weber", pair:30}, {id:30, txt:"Ação Social e Tipo Ideal", pair:3},
                {id:4, txt:"Pierre Bourdieu", pair:40}, {id:40, txt:"Capital Cultural e Habitus", pair:4},
                {id:5, txt:"Zygmunt Bauman", pair:50}, {id:50, txt:"Modernidade Líquida", pair:5},
                {id:6, txt:"Michel Foucault", pair:60}, {id:60, txt:"Biopoder e Panóptico", pair:6}
            ];
            let first = null, matched = 0;
            const board = document.getElementById('board');
            items.sort(() => Math.random() - 0.5);
            items.forEach(it => {
                let div = document.createElement('div');
                div.className = 'card'; div.innerText = '❓ Virar Carta';
                div.onclick = () => {
                    if(div.classList.contains('flipped') || (first && first.elem === div)) return;
                    div.innerText = it.txt; div.classList.add('flipped');
                    if(!first) { first = {it, elem: div}; }
                    else {
                        if(first.it.pair === it.id) {
                            matched++; first = null;
                            if(matched === 6) document.getElementById('status').innerText = '🎉 SUCESSO TOTAL! Você encontrou todos os 6 pares da Sociologia!';
                        } else {
                            setTimeout(() => {
                                div.innerText = '❓ Virar Carta'; div.classList.remove('flipped');
                                first.elem.innerText = '❓ Virar Carta'; first.elem.classList.remove('flipped');
                                first = null;
                            }, 1100);
                        }
                    }
                };
                board.appendChild(div);
            });
        </script>
    </body></html>
    """
    components.html(html, height=400)
    st.info("💡 **Macete ENEM:** Durkheim (Fato Social), Marx (Classes/Luta), Weber (Ação Social), Bourdieu (Capital Cultural), Bauman (Relações Líquidas) e Foucault (Poder Disciplinar) formam o núcleo duro de Humanas!")

# =============================================================================
# 02. V OU F: AÇÃO SOCIAL (WEBER)
# =============================================================================
elif jogo == "02. Desafio V ou F: As Formas de Ação Social (Weber)":
    st.subheader("⚡ 02. Classificador de Ação Social de Max Weber")
    st.success("🎯 **O que fazer:** Escolha a opção correta para classificar a intenção da ação humana!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 15px; border-radius: 8px; margin: 10px auto; max-width: 520px; border: 1px solid #30363d; }
        button { background: #1f6beb; color: white; font-weight: bold; border: none; padding: 10px 14px; border-radius: 6px; cursor: pointer; margin: 4px; display: inline-block; width: 48%; }
    </style></head><body>
        <div class="card">
            <b>Cenário Prático:</b> Um estudante passa 8 horas diárias estudando e fazendo simulados com a meta clara de passar em Medicina no ENEM.<br><br>
            <b>Qual é o tipo de Ação Social predominante?</b><br><br>
            <button onclick="f(false)">Ação Afetiva</button>
            <button onclick="f(false)">Ação Tradicional</button>
            <button onclick="f(true)">Ação Racional c/ Fins</button>
            <button onclick="f(false)">Ação Racional c/ Valores</button>
        </div>
        <div id="feedback" style="font-weight:bold; font-size:1.1em; margin-top:10px;"></div>
        <script>
            function f(correct){
                let fb = document.getElementById('feedback');
                if(correct) fb.innerHTML = "<span style='color:#7ee787;'>✅ CORRETO! Ação Racional com relação a Fins (cálculo consciente de meios e metas).</span>";
                else fb.innerHTML = "<span style='color:#ff7b72;'>❌ Incorreto! Quando há planejamento de meios para atingir uma meta clara, a ação é focada em FINS!</span>";
            }
        </script>
    </body></html>
    """
    components.html(html, height=310)
    st.info("💡 **Macete ENEM:** Max Weber divide a Ação Social em: **Tradicional** (costumes), **Afetiva** (emoções), **Racional com Relação a Valores** (princípios/ética) e **Racional com Relação a Fins** (cálculo estratégico).")

# =============================================================================
# 03. TERMÔMETRO DE CAPITAL CULTURAL
# =============================================================================
elif jogo == "03. Termômetro de Capital Cultural (Bourdieu)":
    st.subheader("🌡️ 03. Simulador de Capital Cultural e Habitus (Bourdieu)")
    st.success("🎯 **O que fazer:** Selecione os elementos para entender como o Capital Cultural é acumulado!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 5px auto; max-width: 500px; text-align: left; border: 1px solid #30363d; }
    </style></head><body>
        <div class="card">
            <input type="checkbox" id="c1" onchange="calc()"> <b>Estado Incorporado:</b> Leitura habitual, domínio da linguagem erudita e repertório.<br><br>
            <input type="checkbox" id="c2" onchange="calc()"> <b>Estado Objetivado:</b> Posse de livros, obras de arte, instrumentos e acervo cultural.<br><br>
            <input type="checkbox" id="c3" onchange="calc()"> <b>Estado Institucionalizado:</b> Diplomas, títulos acadêmicos e certificados formais.
        </div>
        <div style="margin-top:12px; font-size: 1.2em;" id="res"><b>Capital Cultural acumulado: 0%</b></div>
        <script>
            function calc(){
                let pts = 0;
                if(document.getElementById('c1').checked) pts += 33;
                if(document.getElementById('c2').checked) pts += 33;
                if(document.getElementById('c3').checked) pts += 34;
                document.getElementById('res').innerHTML = "<b>Capital Cultural acumulado: " + pts + "%</b><br><small style='color:#7ee787;'>Para Bourdieu, a escola tende a reproduzir o capital cultural das classes dominantes!</small>";
            }
        </script>
    </body></html>
    """
    components.html(html, height=260)
    st.info("💡 **Macete ENEM:** Pierre Bourdieu mostra como o **Capital Cultural** é convertido em privilégios e reprodução de desigualdade social no ambiente escolar.")

# =============================================================================
# 04. PANÓPTICO E SOCIEDADE DE CONTROLE
# =============================================================================
elif jogo == "04. Simulador do Panóptico e Sociedade de Controle":
    st.subheader("👁️ 04. O Panóptico de Bentham & Foucault")
    st.success("🎯 **O que fazer:** Ative a torre de vigilância e observe a mudança no comportamento disciplinar!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .box { border: 2px dashed #e3b341; padding: 18px; border-radius: 8px; background: #161b22; display: inline-block; max-width: 500px; }
        button { background: #238636; color: white; font-weight: bold; border: none; padding: 10px 18px; border-radius: 6px; cursor: pointer; }
    </style></head><body>
        <div class="box">
            🏰 <b>TORRE CENTRAL DE VIGILÂNCIA</b><br><br>
            <button onclick="document.getElementById('txt').innerHTML='<b style=color:#e3b341;>VIGILÂNCIA ATIVA:</b> O indivíduo adestra seu próprio corpo e conduta por saber que pode estar sendo vigiado a qualquer segundo!'">Ativar Vigilância Panóptica</button>
            <p id="txt" style="margin-top:12px;">Clique no botão para ver o efeito do Poder Disciplinar.</p>
        </div>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** Michel Foucault analisa o **Panóptico** como o modelo da Sociedade Disciplinar, onde a vigilância contínua torna a coerção física desnecessária.")

# =============================================================================
# 05. ROLETA DE DESAFIOS: ETNOCENTRISMO VS RELATIVISMO
# =============================================================================
elif jogo == "05. Roleta de Desafios: Etnocentrismo vs Relativismo":
    st.subheader("🎡 05. Sorteador de Casos Culturais do ENEM")
    st.success("🎯 **O que fazer:** Sorteie cenários reais de provas para analisar a atitude cultural!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 14px; border-radius: 8px; margin: 12px auto; border: 1px solid #79c0ff; max-width: 520px; font-size: 1em; }
        button { background: #f0883e; color: white; font-weight: bold; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-size: 1em; }
    </style></head><body>
        <button onclick="spin()">🎰 SORTEAR CASO CULTURAL</button>
        <div class="card" id="out">Clique no botão para sortear um cenário!</div>
        <script>
            const cases = [
                "<b>Cenário A:</b> Considerar os hábitos de um povo indígena 'atrasados' tomando a cultura ocidental como régua de perfeição. ➔ <b>ETNOCENTRISMO!</b>",
                "<b>Cenário B:</b> Compreender que os rituais e costumes de um grupo fazem sentido dentro do seu próprio contexto histórico. ➔ <b>RELATIVISMO CULTURAL!</b>",
                "<b>Cenário C:</b> Impor a visão europeia como a única forma legítima de civilização e progresso humano. ➔ <b>EUROCENTRISMO!</b>"
            ];
            function spin(){
                let idx = Math.floor(Math.random() * cases.length);
                document.getElementById('out').innerHTML = cases[idx];
            }
        </script>
    </body></html>
    """
    components.html(html, height=240)
    st.info("💡 **Macete ENEM:** O **Etnocentrismo** gera intolerância ao colocar a própria cultura no centro do mundo. O **Relativismo Cultural** busca compreender a alteridade sem pré-julgamentos.")

# =============================================================================
# 06. CAIXA DE DILEMAS: MOVIMENTOS SOCIAIS
# =============================================================================
elif jogo == "06. Caixa de Dilemas: Movimentos Sociais no Brasil":
    st.subheader("📦 06. Painel de Movimentos Sociais")
    st.success("🎯 **O que fazer:** Compare as diferenças entre movimentos tradicionais e novos movimentos sociais!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #a371f7; max-width: 520px; }
        button { background: #a371f7; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="m(1)">Movimentos Tradicionais (Trabalho/Terra)</button>
        <button onclick="m(2)">Novos Movimentos Sociais (Identidades)</button>
        <div class="card" id="out">Clique em um dos botões para explorar as pautas de luta.</div>
        <script>
            function m(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Movimentos Tradicionais:</b> Foco em pautas econômicas, classe social, salários, distribuição de renda e acesso à terra (ex: sindicatos e MST).";
                if(n===2) o.innerHTML = "<b>Novos Movimentos Sociais:</b> Foco em pautas identitárias, igualdade de gênero, antirracismo, direitos LGBTQIA+ e preservação ambiental.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** Os movimentos sociais impulsionam transformações legislativas e garantem o exercício pleno da cidadania ativa no Brasil.")

# =============================================================================
# 07. LINHA DO TEMPO: CIDADANIA
# =============================================================================
elif jogo == "07. Linha do Tempo Viva: As 3 Dimensões da Cidadania":
    st.subheader("⏳ 07. A Tríade da Cidadania (T. H. Marshall)")
    st.success("🎯 **O que fazer:** Acompanhe a conquista gradual dos Direitos na história!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #7ee787; max-width: 520px; }
        button { background: #238636; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="c(1)">Séc. XVIII: Direitos Civis</button>
        <button onclick="c(2)">Séc. XIX: Direitos Políticos</button>
        <button onclick="c(3)">Séc. XX: Direitos Sociais</button>
        <div class="card" id="out">Selecione o século para explorar a dimensão da cidadania!</div>
        <script>
            function c(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>1. Direitos Civis (Séc. XVIII):</b> Liberdade individual, liberdade de expressão, de propriedade e igualdade perante a lei.";
                if(n===2) o.innerHTML = "<b>2. Direitos Políticos (Séc. XIX):</b> Direito de votar, ser votado, organizar partidos e participar do governo.";
                if(n===3) o.innerHTML = "<b>3. Direitos Sociais (Séc. XX):</b> Saúde, educação, trabalho, aposentadoria e segurança garantidos pelo Estado de Bem-Estar.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** No Brasil, o historiador José Murilo de Carvalho destaca que a trajetória foi atípica ('Cidadania Invertida'), pois direitos sociais vieram antes de direitos políticos plenamente consolidados.")

# =============================================================================
# 08. QUIZ DE FIXAÇÃO: INDÚSTRIA CULTURAL
# =============================================================================
elif jogo == "08. Quiz de Fixação: A Indústria Cultural (Adorno)":
    st.subheader("❓ 08. Quiz da Escola de Frankfurt")
    st.success("🎯 **O que fazer:** Selecione a resposta correta sobre o conceito de Indústria Cultural!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 14px; border-radius: 8px; margin: 5px auto; max-width: 520px; border: 1px solid #30363d; }
        button { background: #388bfd; color: white; font-weight: bold; border: none; padding: 10px; border-radius: 6px; cursor: pointer; margin: 4px 0; display: block; width: 100%; text-align: left; }
    </style></head><body>
        <div class="card">
            <b>Qual é a principal consequência da Indústria Cultural na visão de Adorno e Horkheimer?</b><br><br>
            <button onclick="ans(false)">A) Estimular o pensamento crítico e a diversidade nas artes.</button>
            <button onclick="ans(true)">B) Padronizar a arte como mercadoria para gerar lucro e passividade social.</button>
            <button onclick="ans(false)">C) Garantir o acesso gratuito do povo às grandes produções musicais.</button>
        </div>
        <div id="res" style="font-weight:bold; margin-top:10px; font-size:1.05em;"></div>
        <script>
            function ans(ok){
                document.getElementById('res').innerHTML = ok ? 
                    "<span style='color:#7ee787;'>✅ CORRETO! A arte é produzida em série como mercadoria comercial.</span>" : 
                    "<span style='color:#ff7b72;'>❌ Incorreto. A Indústria Cultural foca na padronização comercial e na apatia.</span>";
            }
        </script>
    </body></html>
    """
    components.html(html, height=290)
    st.info("💡 **Macete ENEM:** A **Indústria Cultural** transforma o bem cultural em mercadoria de consumo rápido, inibindo a autonomia e o senso crítico da população.")

# =============================================================================
# 09. RADAR DO TRABALHO
# =============================================================================
elif jogo == "09. Radar das Mudanças no Mundo do Trabalho":
    st.subheader("🏭 09. O Trabalho Contemporâneo e a Precarização")
    st.success("🎯 **O que fazer:** Analise os novos fenômenos do mercado de trabalho flexível!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 8px auto; border: 1px solid #da3633; max-width: 520px; }
        button { background: #da3633; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="t(1)">Uberização / Gig Economy</button>
        <button onclick="t(2)">Pejotização e Perda de CLT</button>
        <div class="card" id="out">Clique em um conceito para ver a definição sociológica.</div>
        <script>
            function t(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Uberização:</b> Trabalho sob demanda por plataformas digitais, sem contrato formal, sem proteção de saúde e com transferência total de custos para o trabalhador.";
                if(n===2) o.innerHTML = "<b>Pejotização:</b> Contratação de funcionários como Pessoa Jurídica (PJ) para eliminar custos trabalhistas e direitos garantidos pela CLT.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=230)
    st.info("💡 **Macete ENEM:** A reorganização do trabalho no século XXI combina tecnologias avançadas com a transferência do risco produtivo diretamente para a figura do 'trabalhador autônomo'.")

# =============================================================================
# 10. TESTE DO CONSUMIDOR: MODERNIDADE LÍQUIDA
# =============================================================================
elif jogo == "10. Teste do Consumidor: Modernidade Líquida (Bauman)":
    st.subheader("💧 10. Simulador de Fluidez Social (Zygmunt Bauman)")
    st.success("🎯 **O que fazer:** Arraste a barra para alterar a rigidez das instituições e laços sociais!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin-top: 10px; max-width: 520px; margin-left:auto; margin-right:auto; }
    </style></head><body>
        <input type="range" id="r" min="0" max="100" value="85" style="width:75%;" oninput="u()">
        <div class="card" id="out"><b style="color:#58a6ff;">MODERNIDADE LÍQUIDA:</b> Relações humanas voláteis, fragilidade dos laços afetivos e lógica do consumo descartável.</div>
        <script>
            function u(){
                let v = document.getElementById('r').value;
                let o = document.getElementById('out');
                if(v < 50) o.innerHTML = "<b>MODERNIDADE SÓLIDA:</b> Instituições duradouras, estabilidade profissional, valores rígidos e projeção de longo prazo.";
                else o.innerHTML = "<b style='color:#58a6ff;'>MODERNIDADE LÍQUIDA:</b> Relações humanas voláteis, fragilidade dos laços afetivos e lógica do consumo descartável.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** Para Bauman, a metáfora da **liquidez** demonstra como nada é feito para durar na sociedade contemporânea, incluindo empregos, valores e relacionamentos.")

# =============================================================================
# 11. LABORATÓRIO DA DESIGUALDADE SOCIAL
# =============================================================================
elif jogo == "11. Laboratório da Desigualdade Social e Estratificação":
    st.subheader("📊 11. Comparativo de Sistemas de Estratificação Social")
    st.success("🎯 **O que fazer:** Analise a possibilidade de mobilidade social em cada modelo histórico!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #7ee787; max-width: 520px; }
        button { background: #238636; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="s(1)">Sistema de Castas</button>
        <button onclick="s(2)">Sistema Estamental</button>
        <button onclick="s(3)">Classes Sociais</button>
        <div class="card" id="out">Clique nos botões para verificar o grau de abertura social.</div>
        <script>
            function s(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Castas:</b> Mobilidade social PRATICAMENTE NULA. Posição hereditária e rígida determinada pelo nascimento e normas religiosas.";
                if(n===2) o.innerHTML = "<b>Estamentos:</b> Mobilidade social MUITO BAIXA. Posição vinculada a honra, privilégios de sangue e obrigações jurídicas (ex: Feudalismo).";
                if(n===3) o.innerHTML = "<b>Classes Sociais:</b> Mobilidade social POSSÍVEL. Posição determinada por fatores econômicos e propriedade dos meios de produção.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** As **Classes Sociais** no capitalismo permitem mobilidade aberta na lei, mas o acúmulo de capital econômico e cultural gera barreiras práticas de ascensão.")

# =============================================================================
# 12. BATALHA DE IDEIAS: INSTITUIÇÕES SOCIAIS
# =============================================================================
elif jogo == "12. Batalha de Ideias: Instituições Sociais":
    st.subheader("🏛️ 12. Socialização Primária e Secundária")
    st.success("🎯 **O que fazer:** Identifique as etapas de internalização das normas culturais no indivíduo!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #e3b341; max-width: 520px; }
    </style></head><body>
        <div class="card">
            👨‍👩‍👧 <b>Socialização Primária:</b> Ocorre na infância, mediada pela Família. Absorção inicial do mundo, regras e valores afetivos.<br><br>
            🏫 <b>Socialização Secundária:</b> Ocorre ao longo da vida (Escola, Igreja, Trabalho, Redes Sociais). Adaptação a papéis sociais específicos.
        </div>
    </body></html>
    """
    components.html(html, height=190)
    st.info("💡 **Macete ENEM:** As **Instituições Sociais** transmitem normas de geração em geração, garantindo a reprodução e a ordem social.")

# =============================================================================
# 13. PALAVRA-CHAVE OCULTA: DIREITOS HUMANOS
# =============================================================================
elif jogo == "13. Palavra-Chave Oculta: Direitos Humanos":
    st.subheader("🗝️ 13. Pilares da Declaração Universal dos Direitos Humanos")
    st.success("🎯 **O que fazer:** Veja as 3 características fundamentais cobradas na prova!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #7ee787; max-width: 520px; text-align: left; }
    </style></head><body>
        <div class="card">
            • <b>UNIVERSALIDADE:</b> Valem para todas as pessoas, sem distinção de raça, cor, gênero ou religião.<br><br>
            • <b>INALIENABILIDADE:</b> Não podem ser doados, comprados ou renunciados.<br><br>
            • <b>INDIVISIBILIDADE:</b> Direitos civis, políticos e sociais dependem um do outro para existir.
        </div>
    </body></html>
    """
    components.html(html, height=210)
    st.info("💡 **Macete ENEM:** A Declaração de 1948 foi criada no contexto pós-Segunda Guerra Mundial para barrar os horrores do totalitarismo e garantir a dignidade humana.")

# =============================================================================
# 14. QUIZ: INDIVÍDUO E SOCIEDADE
# =============================================================================
elif jogo == "14. Quiz Dinâmico: A Relação Indivíduo e Sociedade":
    st.subheader("🧩 14. O Dilema: Quem molda quem?")
    st.success("🎯 **O que fazer:** Veja o foco metodológico de cada pensador clássico!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; max-width: 520px; }
        button { background: #1f6beb; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="q(1)">Visão de Durkheim</button>
        <button onclick="q(2)">Visão de Weber</button>
        <button onclick="q(3)">Visão de Marx</button>
        <div class="card" id="out">Clique em um autor para ver como ele analisa essa relação.</div>
        <script>
            function q(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Durkheim:</b> A Sociedade se sobrepõe ao Indivíduo através de coerção dos Fatos Sociais.";
                if(n===2) o.innerHTML = "<b>Weber:</b> A Sociedade é o resultado das Ações Sociais praticadas pelos Indivíduos.";
                if(n===3) o.innerHTML = "<b>Marx:</b> A Sociedade e as escolhas do Indivíduo são condicionadas pelas Relações Materiais de Produção.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=210)
    st.info("💡 **Macete ENEM:** Durkheim é o pai do **Holismo Metodológico** (Coletivo explica a parte). Weber é o pai do **Individualismo Metodológico** (Ação do indivíduo constrói o todo).")

# =============================================================================
# 15. MOSAICO DA DIVERSIDADE E PATRIMÔNIO
# =============================================================================
elif jogo == "15. Mosaico da Diversidade e Patrimônio Cultural":
    st.subheader("🎨 15. Patrimônio Material e Imaterial (IPHAN)")
    st.success("🎯 **O que fazer:** Classifique os exemplos de preservação da memória e identidade cultural do Brasil!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; max-width: 520px; }
        button { background: #238636; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="p(1)">Patrimônio Material</button>
        <button onclick="p(2)">Patrimônio Imaterial</button>
        <div class="card" id="out">Clique nos botões para conferir as categorias do patrimônio.</div>
        <script>
            function p(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Patrimônio Material:</b> Bens físicos e tangíveis (Cidades históricas, igrejas barrocas, acervos e sítios arqueológicos).";
                if(n===2) o.innerHTML = "<b>Patrimônio Imaterial:</b> Saberes, celebrações e expressões vivas (Samba de Roda, Frevo, Capoeira, Círio de Nazaré).";
            }
        </script>
    </body></html>
    """
    components.html(html, height=210)
    st.info("💡 **Macete ENEM:** A preservação do **Patrimônio Imaterial** garante a continuidade das raízes culturais e da diversidade da identidade nacional brasileira.")

# =============================================================================
# 16. DEMOCRACIA E ESTADO
# =============================================================================
elif jogo == "16. Conexão de Conceitos: Democracia e Estado":
    st.subheader("🏛️ 16. Exercício da Democracia no Brasil")
    st.success("🎯 **O que fazer:** Diferencie Democracia Representativa de mecanismos Participativos Diretos!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #7ee787; max-width: 520px; }
    </style></head><body>
        <div class="card">
            🗳️ <b>Democracia Representativa:</b> O cidadão elege representantes para tomarem decisões políticas em seu nome.<br><br>
            ✋ <b>Mecanismos Diretos:</b> Plebiscito (consulta prévia), Referendo (consulta posterior) e Lei de Iniciativa Popular.
        </div>
    </body></html>
    """
    components.html(html, height=190)
    st.info("💡 **Macete ENEM:** A Constituição Federal de 1988 estabelece uma democracia semi-direta, combinando a eleição de representantes com instrumentos populares diretos.")

# =============================================================================
# 17. SIMULADOR DE FAKE NEWS E PÓS-VERDADE
# =============================================================================
elif jogo == "17. Simulador de Fake News e Pós-Verdade":
    st.subheader("📱 17. A Pós-Verdade na Sociedade em Rede")
    st.success("🎯 **O que fazer:** Entenda o impacto da desinformação e das bolhas digitais!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #f0883e; max-width: 520px; }
    </style></head><body>
        <div class="card">
            🔥 <b>Pós-Verdade:</b> Contexto em que os fatos objetivos têm menos poder de persuasão do que crenças e sentimentos pessoais.<br><br>
            🫧 <b>Bolhas Digitais:</b> Algoritmos de redes sociais que filtram o conteúdo para mostrar apenas o que confirma as ideias prévias do usuário.
        </div>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** A proliferação das **Fake News** afeta a esfera pública ao substituir o debate racional embasado em evidências por confrontos passionais.")

# =============================================================================
# 18. RACISMO ESTRUTURAL
# =============================================================================
elif jogo == "18. Teste Rápido: Racismo Estrutural no Brasil":
    st.subheader("✊🏿 18. As Níveis do Racismo (Silvio Almeida)")
    st.success("🎯 **O que fazer:** Veja a diferença entre as 3 manifestações de racismo!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; max-width: 520px; }
        button { background: #a371f7; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="r(1)">Racismo Individual</button>
        <button onclick="r(2)">Racismo Institucional</button>
        <button onclick="r(3)">Racismo Estrutural</button>
        <div class="card" id="out">Clique em uma dimensão para visualizar a análise sociológica.</div>
        <script>
            function r(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Individual:</b> Ação discriminatória cometida por uma pessoa contra outra por conduta interpessoal isolada.";
                if(n===2) o.innerHTML = "<b>Institucional:</b> Vantagens e desvantagens desiguais geradas pelo funcionamento de instituições e empresas.";
                if(n===3) o.innerHTML = "<b>Estrutural:</b> Processo histórico em que o racismo organiza as próprias relações econômicas e políticas da sociedade.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** O **Racismo Estrutural** mostra que as desigualdades raciais não são anomalias, mas sim um padrão social histórico acumulado desde o período colonial.")

# =============================================================================
# 19. POSITIVISMO DE AUGUSTE COMTE
# =============================================================================
elif jogo == "19. Caça-Erros: Teorias do Positivismo de Auguste Comte":
    st.subheader("📐 19. A Lei dos Três Estados Positivista")
    st.success("🎯 **O que fazer:** Acompanhe os estágios de evolução do pensamento humano!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin: 4px auto; max-width: 520px; }
    </style></head><body>
        <div class="card" style="border: 1px solid #ff7b72;">1. <b>Estado Teológico:</b> Explicação da realidade baseada em deuses e entidades sobrenaturais.</div>
        <div class="card" style="border: 1px solid #e3b341;">2. <b>Estado Metafísico:</b> Explicação baseada em forças abstratas e filosofia especulativa.</div>
        <div class="card" style="border: 1px solid #7ee787;">3. <b>Estado Positivo:</b> Explicação baseada no método científico, observação e leis dos fatos.</div>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** Auguste Comte é considerado o pai do **Positivismo** e da Sociologia enquanto 'Física Social', buscando ordem e progresso pela ciência.")

# =============================================================================
# 20. MODELOS DE PRODUÇÃO
# =============================================================================
elif jogo == "20. Desafio do Trabalho: Taylorismo, Fordismo e Toyotismo":
    st.subheader("🚗 20. Os Modelos de Organização Industrial")
    st.success("🎯 **O que fazer:** Compare as lógicas de produção no mundo do trabalho!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; max-width: 520px; }
        button { background: #388bfd; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="m(1)">Taylorismo</button>
        <button onclick="m(2)">Fordismo</button>
        <button onclick="m(3)">Toyotismo</button>
        <div class="card" id="out">Clique nos botões para conferir as características do modelo.</div>
        <script>
            function m(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Taylorismo:</b> Divisão rigorosa de tarefas, cronometragem do tempo e separação entre planejamento e execução.";
                if(n===2) o.innerHTML = "<b>Fordismo:</b> Linhas de montagem com esteiras rolantes, padronização de produtos e produção massiva em estoque.";
                if(n===3) o.innerHTML = "<b>Toyotismo:</b> Produção flexível e sob demanda (<i>Just-in-Time</i>), automação e trabalhador multifuncional.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** O **Toyotismo** reestrutura a fábrica no pós-Segunda Guerra, trocando os grandes estoques rígidos do Fordismo pela produção flexível sob demanda.")

# =============================================================================
# 21. GLOBALIZAÇÃO E EXCLUSÃO
# =============================================================================
elif jogo == "21. Roleta do Conhecimento: Globalização e Exclusão":
    st.subheader("🌐 21. As Faces da Globalização (Milton Santos)")
    st.success("🎯 **O que fazer:** Explore a análise do geógrafo sobre as contradições do mundo globalizado!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; max-width: 520px; }
        button { background: #238636; color: white; font-weight: bold; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; margin: 3px; }
    </style></head><body>
        <button onclick="g(1)">Globalização como Fábula</button>
        <button onclick="g(2)">Globalização como Perversidade</button>
        <button onclick="g(3)">Outra Globalização</button>
        <div class="card" id="out">Clique em uma tese para visualizar a análise.</div>
        <script>
            function g(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = "<b>Fábula (Como nos contam):</b> O mito da aldeia global sem fronteiras, onde todos desfrutam das mesmas oportunidades de consumo.";
                if(n===2) o.innerHTML = "<b>Perversidade (Como ela é):</b> Concentração de capital nas redes, aumento da pobreza e aprofundamento das desigualdades.";
                if(n===3) o.innerHTML = "<b>Outra Globalização (Como pode ser):</b> Construção de um mundo solidário baseado nas periferias e saberes locais.";
            }
        </script>
    </body></html>
    """
    components.html(html, height=220)
    st.info("💡 **Macete ENEM:** Milton Santos enfatiza que a **globalização perversa** intensifica as assimetrias no meio técnico-científico-informacional.")

# =============================================================================
# 22. SOCIOLOGIA DA VIOLÊNCIA
# =============================================================================
elif jogo == "22. Quiz de Competência: Sociologia da Violência":
    st.subheader("🛡️ 22. Violência Física vs Violência Simbólica")
    st.success("🎯 **O que fazer:** Entenda as manifestações visíveis e invisíveis de coerção!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; border: 1px solid #da3633; max-width: 520px; }
    </style></head><body>
        <div class="card">
            💥 <b>Violência Física/Direta:</b> Agressão ostensiva e do uso da força corporal sobre a integridade física.<br><br>
            🧠 <b>Violência Simbólica:</b> Coerção sutil exercida com o consentimento tácito do dominado (ex: estigmas e preconceito linguístico).
        </div>
    </body></html>
    """
    components.html(html, height=190)
    st.info("💡 **Macete ENEM:** A **Violência Simbólica** opera através de estruturas sociais assimiladas pelo indivíduo como 'naturais', mantendo assimetrias sem necessidade de agressão física.")

# =============================================================================
# 23. CHECKLIST FINAL
# =============================================================================
elif jogo == "23. Checklist do Conhecimento Nota 1000":
    st.subheader("✅ 23. Checklist Final de Sociologia pro ENEM")
    st.success("🎯 **O que fazer:** Confira os tópicos revisados no aplicativo!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin: 10px auto; text-align: left; max-width: 520px; }
    </style></head><body>
        <div class="card">
            [ ] Clássicos: Durkheim (Fato Social), Marx (Classes) e Weber (Ação Social)<br>
            [ ] Bourdieu (Capital Cultural) e Bauman (Modernidade Líquida)<br>
            [ ] Cultura: Etnocentrismo, Relativismo e Patrimônio IPHAN<br>
            [ ] Cidadania, Direitos Humanos e Movimentos Sociais<br>
            [ ] Trabalho: Taylorismo, Fordismo, Toyotismo e Uberização
        </div>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** As questões de Sociologia do ENEM frequentemente utilizam textos de apoio, letras de música e charges para testar a sua capacidade de relacionar o conceito teórico com a realidade social brasileira!")