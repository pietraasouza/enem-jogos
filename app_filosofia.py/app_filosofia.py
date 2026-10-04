import streamlit as st
import streamlit.components.v1 as components

# Configuração da Página
st.set_page_config(page_title="20 Jogos de Filosofia pro ENEM", page_icon="🏛️", layout="wide")

st.title("🏛️ 20 Jogos & Simuladores de Filosofia pro ENEM")
st.write("Aprenda os principais pensadores, conceitos e correntes filosóficas praticando em tempo real!")

# Menu Lateral
st.sidebar.header("🕹️️ Selecione o Módulo (1 a 20)")
jogo = st.sidebar.radio("Módulos Interativos:", [
    "01. Arraste o Pensador até a Frase (Drag & Drop)",
    "02. Mito da Caverna de Platão (Simulador)",
    "03. O Mundo das Idéias x Mundo Sensível",
    "04. Ética da Virtude de Aristóteles (Meio-Termo)",
    "05. Filosofia Helenista (Epicurismo x Estoicismo)",
    "06. Patrística: Santo Agostinho e a Fé/Razão",
    "07. Escolástica: São Tomás de Aquino e as 5 Vias",
    "08. Maquiavel e a Política Real (O Príncipe)",
    "09. Contratualismo: Hobbes x Locke x Rousseau",
    "10. Racionalismo de Descartes (Penso, Logo Existo)",
    "11. Empirismo Inglês: Bacon, Locke e Hume",
    "12. O Iluminismo e a Autonomia Humana",
    "13. Imperativo Categórico de Immanuel Kant",
    "14. Dialética em Hegel e Karl Marx",
    "15. Utilitarismo: Bentham e John Stuart Mill",
    "16. Friedrich Nietzsche e a Crítica à Moral",
    "17. Existencialismo: Sartre e a Liberdade",
    "18. Escola de Frankfurt e a Indústria Cultural",
    "19. Hannah Arendt e a Banalidade do Mal",
    "20. Michel Foucault e o Biopoder / Vigiar e Punir"
])

st.sidebar.divider()
st.sidebar.caption("🎯 **Dica ENEM:** Interaja com as simulações e grave os conceitos-chave de cada pensador!")

# =============================================================================
# 01. ARRASTE O PENSADOR (DRAG AND DROP)
# =============================================================================
if jogo == "01. Arraste o Pensador até a Frase (Drag & Drop)":
    st.subheader("🧩 01. Desafio: Associe o Filósofo à sua Frase!")
    st.success("🎯 **O que fazer:** Arraste o bloco com o nome do filósofo e solte-o no espaço ao lado da frase correspondente!")
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body { font-family: sans-serif; background: #0e1117; color: white; margin: 0; padding: 10px; text-align: center; }
        .container { display: flex; justify-content: space-around; flex-wrap: wrap; }
        .box { background: #161b22; border: 2px dashed #58a6ff; border-radius: 8px; padding: 10px; margin: 5px; min-width: 200px; }
        .drag-item { background: #238636; color: white; padding: 8px 15px; margin: 5px; border-radius: 5px; cursor: grab; font-weight: bold; display: inline-block; }
        .drop-zone { background: #21262d; border: 2px dashed #8b949e; border-radius: 6px; padding: 12px; margin: 8px 0; min-height: 40px; }
        .correct { background: #1f6beb !important; border-color: #388bfd !important; }
        .phrase { font-style: italic; color: #c9d1d9; font-size: 0.95em; }
        #feedback { margin-top: 15px; font-weight: bold; font-size: 1.1em; }
    </style>
    </head>
    <body>

        <h3> Filósofos Disponíveis (Arraste daqui):</h3>
        <div id="sources">
            <div class="drag-item" draggable="true" id="marx" ondragstart="drag(event)">Karl Marx</div>
            <div class="drag-item" draggable="true" id="descartes" ondragstart="drag(event)">René Descartes</div>
            <div class="drag-item" draggable="true" id="socrates" ondragstart="drag(event)">Sócrates</div>
            <div class="drag-item" draggable="true" id="sartre" ondragstart="drag(event)">Jean-Paul Sartre</div>
            <div class="drag-item" draggable="true" id="nietzsche" ondragstart="drag(event)">Friedrich Nietzsche</div>
        </div>

        <hr style="border: 0.5px solid #30363d; margin: 15px 0;">

        <h3> Frases (Solte no local certo):</h3>
        <div style="text-align: left; max-width: 700px; margin: 0 auto;">
            
            <div class="phrase">1. "Os filósofos apenas interpretaram o mundo de diferentes maneiras; o que importa é transformá-lo."</div>
            <div class="drop-zone" id="target-marx" ondrop="drop(event, 'marx')" ondragover="allowDrop(event)"></div>

            <div class="phrase">2. "Penso, logo existo." (Cogito, ergo sum)</div>
            <div class="drop-zone" id="target-descartes" ondrop="drop(event, 'descartes')" ondragover="allowDrop(event)"></div>

            <div class="phrase">3. "Só sei que nada sei."</div>
            <div class="drop-zone" id="target-socrates" ondrop="drop(event, 'socrates')" ondragover="allowDrop(event)"></div>

            <div class="phrase">4. "A existência precede a essência."</div>
            <div class="drop-zone" id="target-sartre" ondrop="drop(event, 'sartre')" ondragover="allowDrop(event)"></div>

            <div class="phrase">5. "Aquele que tem um 'porquê' para viver pode suportar quase qualquer 'como'."</div>
            <div class="drop-zone" id="target-nietzsche" ondrop="drop(event, 'nietzsche')" ondragover="allowDrop(event)"></div>

        </div>

        <div id="feedback"></div>

        <script>
            let acertos = 0;

            function allowDrop(ev) {
                ev.preventDefault();
            }

            function drag(ev) {
                ev.dataTransfer.setData("text", ev.target.id);
            }

            function drop(ev, expectedId) {
                ev.preventDefault();
                var data = ev.dataTransfer.getData("text");
                
                if (data === expectedId && ev.target.classList.contains('drop-zone') && ev.target.children.length === 0) {
                    var element = document.getElementById(data);
                    ev.target.appendChild(element);
                    ev.target.classList.add('correct');
                    element.setAttribute('draggable', 'false');
                    element.style.cursor = 'default';
                    acertos++;

                    if (acertos === 5) {
                        document.getElementById('feedback').innerHTML = '<span style="color: #7ee787;">🎉 Excelente! Você acertou todas as frases dos pensadores!</span>';
                    }
                } else if (data !== expectedId) {
                    document.getElementById('feedback').innerHTML = '<span style="color: #ff7b72;">❌ Tente novamente! Esse filósofo não disse essa frase.</span>';
                    setTimeout(() => { document.getElementById('feedback').innerText = ''; }, 2000);
                }
            }
        </script>
    </body>
    </html>
    """
    components.html(html, height=520)
    st.info("💡 **Macete ENEM:** Karl Marx criticou a filosofia contemplativa alemã na sua famosa Tese 11 sobre Feuerbach, defendendo a **práxis** (transformação prática do mundo através da ação histórica)!")

# =============================================================================
# 02. MITO DA CAVERNA
# =============================================================================
elif jogo == "02. Mito da Caverna de Platão (Simulador)":
    st.subheader("🕯️ 02. Simulador do Mito da Caverna de Platão")
    st.success("🎯 **O que fazer:** Clique para avançar os estágios da libertação do prisioneiro!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 12px; border-radius: 8px; margin-top: 10px; display: inline-block; min-width: 80%; }
        button { background: #238636; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin: 4px; }
    </style></head><body>
        <button onclick="p(1)">1. Prisioneiro na Caverna</button>
        <button onclick="p(2)">2. Saída e Cegueira da Luz</button>
        <button onclick="p(3)">3. Contemplação do Sol (Verdade)</button>
        <button onclick="p(4)">4. O Retorno para Libertar os Outros</button>
        
        <div class="card" id="box"><b style="color:#58a6ff;">Estágio 1: As Sombras</b><br>Os homens acorrentados tomam sombras projetadas na parede pela fogueira como a única realidade existente (Mundo Sensível).</div>

        <script>
            function p(s){
                let b = document.getElementById('box');
                if(s===1) b.innerHTML = '<b style="color:#58a6ff;">Estágio 1: As Sombras</b><br>Os homens acorrentados tomam sombras projetadas na parede como a única realidade existente (Mundo Sensível).';
                if(s===2) b.innerHTML = '<b style="color:#e3b341;">Estágio 2: A Subida Dolorosa</b><br>Ao sair da caverna, a luz do Sol ofusca a visão. Conhecer a verdade causa desconforto inicial e exige esforço racional.';
                if(s===3) b.innerHTML = '<b style="color:#7ee787;">Estágio 3: O Sol (Ideia do Bem)</b><br>O filósofo contempla as coisas como elas realmente são fora da caverna (Mundo Inteligível / Conhecimento Verdadeiro).';
                if(s===4) b.innerHTML = '<b style="color:#ff7b72;">Estágio 4: O Retorno Trágico</b><br>Ao voltar para avisar os outros, o filósofo é ridicularizado e ameaçado de morte. Metáfora sobre a condenação de Sócrates.';
            }
        </script>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** A caverna representa o **senso comum** e o **Mundo Sensível**, enquanto o exterior representa a **Filosofia** e o **Mundo das Ideias**.")

# =============================================================================
# 03. MUNDO DAS IDEIAS X MUNDO SENSÍVEL
# =============================================================================
elif jogo == "03. O Mundo das Idéias x Mundo Sensível":
    st.subheader("💡 03. O Dualismo Platônico")
    st.success("🎯 **O que fazer:** Selecione o mundo para entender a diferença entre Opinião (Doxa) e Ciência (Episteme).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <select id="m" onchange="u()">
            <option value="Mundo Sensível (Matéria) ➔ Captado pelos sentidos. É mutável, imperfeito e ilusório (Opinião / Doxa).">Mundo Sensível</option>
            <option value="Mundo Inteligível (Ideias) ➔ Captado pela razão. É imutável, perfeito e eterno (Ciência / Episteme).">Mundo Inteligível</option>
        </select>
        <div class="card" id="out" style="border: 1px solid #7ee787;">Mundo Sensível (Matéria) ➔ Captado pelos sentidos. É mutável, imperfeito e ilusório (Opinião / Doxa).</div>
        <script>
            function u(){ document.getElementById('out').innerText = document.getElementById('m').value; }
        </script>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** Para Platão, aprender é **recordar** (*Reminiscência*). A alma já conhecia as Ideias perfeitas antes de se prender ao corpo!")

# =============================================================================
# 04. ÉTICA DE ARISTÓTELES
# =============================================================================
elif jogo == "04. Ética da Virtude de Aristóteles (Meio-Termo)":
    st.subheader("⚖️ 04. A justa medida (Mediedade) em Aristóteles")
    st.success("🎯 **O que fazer:** Ajuste o controle deslizante do comportamento para encontrar a **Virtude (Ajuste Perfeito)** entre o vício por falta e por excesso!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <input type="range" id="v" min="0" max="100" value="50" style="width:70%;" oninput="u()">
        <div class="card" id="out"><b style="color:#7ee787;">VIRTUDE: CORAGEM</b><br>O meio-termo ideal entre a covardia e a imprudência.</div>
        <script>
            function u(){
                let val = document.getElementById('v').value;
                let out = document.getElementById('out');
                if(val < 35) out.innerHTML = '<b style="color:#ff7b72;">VÍCIO POR DEFICIÊNCIA: COVARDIA</b><br>Falta de ação por medo excessivo.';
                else if(val > 65) out.innerHTML = '<b style="color:#ff7b72;">VÍCIO POR EXCESSO: TEMERIDADE / IMPRUDÊNCIA</b><br>Ação inconsequente sem medir os riscos.';
                else out.innerHTML = '<b style="color:#7ee787;">VIRTUDE (JUSTA MEDIDA): CORAGEM</b><br>Equilíbrio racional orientado para a Felicidade (Eudaimonia).';
            }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Para Aristóteles, o objetivo final da vida humana é a **Eudaimonia** (Felicidade), alcançada através da prática contínua das virtudes pela razão!")

# =============================================================================
# 05. FILOSOFIA HELENISTA
# =============================================================================
elif jogo == "05. Filosofia Helenista (Epicurismo x Estoicismo)":
    st.subheader("🌿 05. Comparador do Helenismo: Epicurismo x Estoicismo")
    st.success("🎯 **O que fazer:** Escolha a escola helenística para comparar as fórmulas da paz de espírito (Ataraxia).")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
        button { background: #1f6beb; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; margin: 2px; }
    </style></head><body>
        <button onclick="u(1)">Epicurismo (Epicuro)</button>
        <button onclick="u(2)">Estoicismo (Zenão / Sêneca)</button>
        <button onclick="u(3)">Ceticismo (Pirro)</button>
        <div class="card" id="out"><b style="color:#58a6ff;">Clique nos botões acima para analisar cada corrente!</b></div>
        <script>
            function u(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = '<b style="color:#7ee787;">EPICURISMO:</b> Busca do prazer moderado (Aponia) e ausência de dores na alma. Evitar desejos desnecessários e o medo da morte.';
                if(n===2) o.innerHTML = '<b style="color:#58a6ff;">ESTOICISMO:</b> Aceitação do destino (Amor Fati) e autocontrole emocional das paixões diante daquilo que não podemos controlar.';
                if(n===3) o.innerHTML = '<b style="color:#e3b341;">CETICISMO:</b> Suspensão de julgamento (Epoché). Impossibilidade de alcançar uma verdade absoluta na realidade.';
            }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** O período Helenista surge após a crise das Polis gregas (Império de Alexandre O Grande), deslocando o foco da Política para a **Ética e Felicidade Individual**.")

# =============================================================================
# 06. PATRÍSTICA
# =============================================================================
elif jogo == "06. Patrística: Santo Agostinho e a Fé/Razão":
    st.subheader("✝️ 06. Santo Agostinho (Neoplatonismo e Livre-Arbítrio)")
    st.success("🎯 **O que fazer:** Veja como Agostinho uniu a filosofia de Platão ao Cristianismo Medieval.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 5px; text-align: left; }
    </style></head><body>
        <div class="card">
            <b>1. Teoria da Iluminação Divina:</b> A razão humana precisa da luz de Deus para alcançar as verdades eternas (adaptação do Mito da Caverna).<br><br>
            <b>2. Problema do Mal:</b> O mal não é uma 'criação', mas sim a **ausência do bem** (privatio boni) resultante do mau uso do **Livre-Arbítrio** humano.<br><br>
            <b>3. Lema:</b> <i>"Crer para compreender, compreender para crer."</i> (Fé e Razão juntas).
        </div>
    </body></html>
    """
    components.html(html, height=210)
    st.info("💡 **Macete ENEM:** Lembre-se: **A**gostinho = **A**dam = Platão. Ele cristianizou a filosofia de Platão no início da Idade Média!")

# =============================================================================
# 07. ESCOLÁSTICA
# =============================================================================
elif jogo == "07. Escolástica: São Tomás de Aquino e as 5 Vias":
    st.subheader("🏰 07. São Tomás de Aquino (Aristotelismo e as 5 Vias)")
    st.success("🎯 **O que fazer:** Clique nos botões para explorar as 5 Vias Racionais que provam a existência de Deus.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
        button { background: #238636; color: white; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; margin: 2px; }
    </style></head><body>
        <button onclick="v(1)">1. Primeiro Motor</button>
        <button onclick="v(2)">2. Causa Eficiente</button>
        <button onclick="v(3)">3. Contingente e Necessário</button>
        <button onclick="v(4)">4. Graus de Perfeição</button>
        <button onclick="v(5)">5. Causa Final (Ordem)</button>
        <div class="card" id="out"><b style="color:#7ee787;">Selecione uma Via para ver a prova lógica de Deus!</b></div>
        <script>
            function v(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = '<b>1ª Via (Primeiro Motor Imóvel):</b> Tudo que se move é movido por algo. É preciso haver um primeiro motor que não seja movido por nada: Deus.';
                if(n===2) o.innerHTML = '<b>2ª Via (Causa Eficiente):</b> Tudo no mundo tem uma causa. Para não ir ao infinito, deve haver uma causa primeira não causada: Deus.';
                if(n===3) o.innerHTML = '<b>3ª Via (Contingência):</b> As coisas do mundo deixam de existir. Deve haver um ser absolutamente necessário que garanta a existência das coisas: Deus.';
                if(n===4) o.innerHTML = '<b>4ª Via (Graus de Perfeição):</b> Há coisas mais ou menos perfeitas, belas ou boas. Deve haver um padrão máximo e absoluto de perfeição: Deus.';
                if(n===5) o.innerHTML = '<b>5ª Via (Governo das Coisas):</b> Os seres sem inteligência agem com uma finalidade perfeita na natureza. Deve haver um Arquiteto Inteligente ordenando tudo: Deus.';
            }
        </script>
    </body></html>
    """
    components.html(html, height=190)
    st.info("💡 **Macete ENEM:** Lembre-se: **T**omás de Aquino = **T**udo = Aristóteles. Ele usou a lógica de Aristóteles para harmonizar Fé e Razão na Baixa Idade Média!")

# =============================================================================
# 08. MAQUIAVEL
# =============================================================================
elif jogo == "08. Maquiavel e a Política Real (O Príncipe)":
    st.subheader("🦊 08. Simulador Político de Maquiavel: Virtù x Fortuna")
    st.success("🎯 **O que fazer:** Ajuste a postura do Governante para manter o poder do Estado!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
        button { background: #238636; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; margin: 4px; }
    </style></head><body>
        <button onclick="m(1)">Apostar apenas na Sorte (Fortuna)</button>
        <button onclick="m(2)">Usar a Astúcia e Habilidade (Virtù)</button>
        <div class="card" id="out"><b style="color:#58a6ff;">Escolha a postura do Príncipe!</b></div>
        <script>
            function m(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = '<b style="color:#ff7b72;">QUEDA DO GOVERNO!</b><br>A Fortuna (imprevistos/acaso) é como um rio violento. Se o Príncipe não construir diques com sua habilidade, será destruído!';
                if(n===2) o.innerHTML = '<b style="color:#7ee787;">SUCESSO E MANUTENÇÃO DO PODER!</b><br>A Virtù é a capacidade de moldar as circunstâncias e agir estrategicamente para preservar a estabilidade do Estado ("Os fins justificam os meios").';
            }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Maquiavel inaugura a **Ciência Política Moderna** ao separar a Política da Moral Religiosa e da Ética Utópica!")

# =============================================================================
# 09. CONTRATUALISMO
# =============================================================================
elif jogo == "09. Contratualismo: Hobbes x Locke x Rousseau":
    st.subheader("📜 09. Quadro Comparativo do Contrato Social")
    st.success("🎯 **O que fazer:** Selecione o contratualista para ver a sua visão sobre o Estado de Natureza e o Papel do Governo.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #58a6ff; border-radius: 4px; }
    </style></head><body>
        <select id="c" onchange="u()">
            <option value="Thomas Hobbes ➔ Estado de Natureza: 'O homem é o lobo do homem' (guerra de todos contra todos). Solução: Estado Absolutista forte (Leviatã) para garantir a segurança.">Thomas Hobbes</option>
            <option value="John Locke ➔ Estado de Natureza: Homens têm Direitos Naturais (Vida, Liberdade, Propriedade). Solução: Estado Liberal para proteger a Propriedade Privada.">John Locke</option>
            <option value="Jean-Jacques Rousseau ➔ Estado de Natureza: 'O homem nasce bom, a sociedade o corrompe' (Bom Selvagem). Solução: Democracia Direta e Vontade Geral.">Jean-Jacques Rousseau</option>
        </select>
        <div class="card" id="out" style="border: 1px solid #58a6ff;">Thomas Hobbes ➔ Estado de Natureza: 'O homem é o lobo do homem' (guerra de todos contra todos). Solução: Estado Absolutista forte (Leviatã) para garantir a segurança.</div>
        <script>
            function u(){ document.getElementById('out').innerText = document.getElementById('c').value; }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Locke é o pai do **Liberalismo**, Hobbes do **Absolutismo** e Rousseau da **Democracia Popular** e crítica à propriedade privada!")

# =============================================================================
# 10. RACIONALISMO DE DESCARTES
# =============================================================================
elif jogo == "10. Racionalismo de Descartes (Penso, Logo Existo)":
    st.subheader("🔍 10. O Caminho da Dúvida Metódica")
    st.success("🎯 **O que fazer:** Dvide as camadas da dúvida cartesiana até chegar na primeira certeza indubitável!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; margin: 2px; }
    </style></head><body>
        <button onclick="d(1)">1. Duvidar dos Sentidos</button>
        <button onclick="d(2)">2. Hipótese do Sonho / Gênio Maligno</button>
        <button onclick="d(3)">3. Primeira Certeza (O Cogito)</button>
        <div class="card" id="out"><b style="color:#58a6ff;">Clique nos passos para aplicar a dúvida hiperbólica!</b></div>
        <script>
            function d(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = '<b>Passo 1:</b> Os sentidos costumam nos enganar (ex: ilusões de ótica). Logo, não podemos confiar neles para fundamentar a ciência.';
                if(n===2) o.innerHTML = '<b>Passo 2:</b> Como saber se não estou sonhando agora? E se um Gênio Maligno engana minha mente até nas equações matemáticas?';
                if(n===3) o.innerHTML = '<b style="color:#7ee787;">Passo 3: COGITO ERGO SUM!</b><br>Se eu duvido de tudo, estou pensando. Se penso, eu existo! Primeira verdade inquestionável da filosofia cartesiana.';
            }
        </script>
    </body></html>
    """
    components.html(html, height=190)
    st.info("💡 **Macete ENEM:** Descartes é o pai do **Racionalismo Moderno** e defende a existência de **ideias inatas** na razão humana.")

# =============================================================================
# 11. EMPIRISMO INGLÊS
# =============================================================================
elif jogo == "11. Empirismo Inglês: Bacon, Locke e Hume":
    st.subheader("🧼 11. A Mente como Tábula Rasa")
    st.success("🎯 **O que fazer:** Experimente a teoria empirista de que todo conhecimento vem das sensações e da experiência prática.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <div class="card">
            <b>John Locke:</b> A mente humana nasce como uma <i>'Folha em Branco' / 'Tábula Rasa'</i>. Não existem ideias inatas!<br><br>
            <b>David Hume:</b> O hábito e a repetição geram a nossa crença em Causa e Efeito (Crítica ao Princípio de Causalidade).
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** Racionalismo = Razão em 1º lugar. Empirismo = Experiência sensível (Sentidos) em 1º lugar!")

# =============================================================================
# 12. ILUMINISMO
# =============================================================================
elif jogo == "12. O Iluminismo e a Autonomia Humana":
    st.subheader("☀️ 12. Esclarecimento (Aufklärung) de Kant")
    st.success("🎯 **O que fazer:** Veja o significado da expressão *Sapere Aude* (Ouse Saber) no Iluminismo.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <div class="card" style="border: 1px solid #e3b341;">
            <b>Maioridade Intelectual:</b> Sair da 'Menoridade' é parar de deixar que autoridades (Igreja, Estado) pensem por você.<br><br>
            <b style="color:#e3b341;">"Sapere Aude! Tenha a coragem de fazer uso do teu próprio entendimento!"</b>
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** O Iluminismo defende a razão, a ciência, o laicismo (separação Igreja/Estado) e a liberdade individual.")

# =============================================================================
# 13. IMPERATIVO CATEGÓRICO DE KANT
# =============================================================================
elif jogo == "13. Imperativo Categórico de Immanuel Kant":
    st.subheader("📐 13. Testador da Moral Kantiana (Dever pelo Dever)")
    st.success("🎯 **O que fazer:** Teste se uma ação pode se tornar uma Lei Universal!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
        button { background: #238636; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; margin: 4px; }
    </style></head><body>
        <button onclick="k(1)">Ação: 'Vou mentir só desta vez para me salvar'</button>
        <button onclick="k(2)">Ação: 'Vou dizer a verdade porque é o dever de todos'</button>
        <div class="card" id="out"><b style="color:#58a6ff;">Escolha a conduta moral para testar no Imperativo Categórico!</b></div>
        <script>
            function k(n){
                let o = document.getElementById('out');
                if(n===1) o.innerHTML = '<b style="color:#ff7b72;">REPROVADO NA MORAL KANTIANA!</b><br>Se a mentira virasse uma lei universal para todos, a confiança na humanidade seria destruída. Não é uma ação ética!';
                if(n===2) o.innerHTML = '<b style="color:#7ee787;">APROVADO! IMPERATIVO CATEGÓRICO!</b><br>"Age de tal modo que a máxima da tua ação possa ser tomada como norma universal." Ação deontológica (por dever)!';
            }
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Kant propõe uma ética **Deontológica** (baseada no dever moral incondicional), independente de interesses ou consequências praticas!")

# =============================================================================
# 14. DIALÉTICA
# =============================================================================
elif jogo == "14. Dialética em Hegel e Karl Marx":
    st.subheader("🔄 14. O Movimento Dialético (Tese, Antítese e Síntese)")
    st.success("🎯 **O que fazer:** Acompanhe a transformação das ideias e das lutas materiais na história.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; margin: 3px; display: inline-block; width: 80%; }
    </style></head><body>
        <div class="card" style="border: 1px solid #58a6ff;"><b>Tese:</b> Afirmação inicial / Situação posta.</div><br>
        <div class="card" style="border: 1px solid #ff7b72;"><b>Antítese:</b> Negação da tese / Contradição / Conflito.</div><br>
        <div class="card" style="border: 1px solid #7ee787;"><b>Síntese:</b> Superação das contradições (Nova realidade que gera uma nova Tese).</div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Para **Hegel**, a dialética ocorre nas ideias (Idealismo). Para **Karl Marx**, ocorre na infraestrutura material da sociedade (**Materialismo Histórico Dialético** / Luta de Classes)!")

# =============================================================================
# 15. UTILITARISMO
# =============================================================================
elif jogo == "15. Utilitarismo: Bentham e John Stuart Mill":
    st.subheader("📊 15. Calculadora Utilitarista das Consequências")
    st.success("🎯 **O que fazer:** Avalie a moralidade de uma decisão com base no Princípio da Máxima Felicidade.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <div class="card" style="border: 1px solid #7ee787;">
            <b>Princípio da Utilidade:</b> Uma ação é moralmente correta se produzir a **maior quantidade de bem-estar / felicidade para o maior número possível de pessoas**.
        </div>
    </body></html>
    """
    components.html(html, height=150)
    st.info("💡 **Macete ENEM:** Ao contrário de Kant, o Utilitarismo é uma ética **Consequencialista**: o que importa não é a intenção, mas o **resultado prático** da ação!")

# =============================================================================
# 16. NIETZSCHE
# =============================================================================
elif jogo == "16. Friedrich Nietzsche e a Crítica à Moral":
    st.subheader("🔨 16. O Filosofar com o Martelo")
    st.success("🎯 **O que fazer:** Conheça os conceitos centrais da desconstrução da filosofia tradicional feita por Nietzsche.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; margin: 2px; text-align: left; }
    </style></head><body>
        <div class="card">
            • <b>Moral de Rebanho / dos Escravos:</b> Moral do ressentimento que prega a passividade e nega a vida terrestre.<br>
            • <b>Morte de Deus:</b> A queda dos valores metafísicos tradicionais na modernidade.<br>
            • <b>Amor Fati:</b> Amar o destino e desejar viver a própria vida infinitas vezes (Eterno Retorno).
        </div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Nietzsche critica o Racionalismo grego (Socrático) e a moral judaico-cristã por reprimirem os impulsos vitais e criativos do ser humano!")

# =============================================================================
# 17. EXISTENCIALISMO
# =============================================================================
elif jogo == "17. Existencialismo: Sartre e a Liberdade":
    st.subheader("☕ 17. Existencialismo É um Humanismo")
    st.success("🎯 **O que fazer:** Entenda por que o ser humano está 'condenado a ser livre'.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <div class="card" style="border: 1px solid #58a6ff;">
            <b>"A existência precede a essência"</b><br><br>
            Primeiro o homem existe no mundo, se encontra e surge. Só depois ele se define através de suas escolhas e ações.<br>
            Fugir dessa responsabilidade culpando o destino é agir com <b>Má-Fé</b>!
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Uma cadeira é criada com uma finalidade prévia (essência precede existência). O ser humano não tem um 'destino pronto': ele se constrói livremente!")

# =============================================================================
# 18. ESCOLA DE FRANKFURT
# =============================================================================
elif jogo == "18. Escola de Frankfurt e a Indústria Cultural":
    st.subheader("📺 18. Adorno e Horkheimer: Indústria Cultural")
    st.success("🎯 **O que fazer:** Veja como a arte é transformada em mercadoria de massa para gerar alienação e passividade.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <div class="card" style="border: 1px solid #ff7b72;">
            <b>Indústria Cultural:</b> Padronização dos produtos culturais (filmes, músicas, entretenimento) para consumo fácil e rápido.<br>
            <b>Efeito:</b> Adestramento dos sentidos, perda do senso crítico e manutenção do sistema capitalista.
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** A Escola de Frankfurt faz uma **Teoria Crítica** da razão instrumental e da transformação da cultura em produto mercantilizado!")

# =============================================================================
# 19. HANNAH ARENDT
# =============================================================================
elif jogo == "19. Hannah Arendt e a Banalidade do Mal":
    st.subheader("⚖️ 19. A Banalidade do Mal e o Julgamento de Eichmann")
    st.success("🎯 **O que fazer:** Reflita sobre o perigo do abandono da capacidade de pensar por si mesmo.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <div class="card" style="border: 1px solid #e3b341;">
            <b>Banalidade do Mal:</b> O mal nem sempre é praticado por monstros perversos, mas muitas vezes por burocratas comuns que **deixam de pensar criticamente** e apenas 'cumprem ordens' sem questionar as leis injustas.
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Arendt defende a **Ação Política** e o debate público no espaço da *Pólis* como antidotos contra governos Totalitários!")

# =============================================================================
# 20. FOUCAULT
# =============================================================================
elif jogo == "20. Michel Foucault e o Biopoder / Vigiar e Punir":
    st.subheader("👁️ 20. Sociedade Disciplinar e o Panóptico")
    st.success("🎯 **O que fazer:** Descubra como o poder se micro-propaga no corpo e nas instituições da sociedade moderna.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style></head><body>
        <div class="card" style="border: 1px solid #58a6ff;">
            <b>Biopoder / Microfísica do Poder:</b> O poder não vem apenas do Estado, mas está espalhado em redes por toda a sociedade (escolas, hospitais, prisões, fábrica).<br><br>
            <b>Panóptico:</b> Arquitetura de vigilância onde as pessoas se comportam bem porque sentem que estão sendo observadas o tempo todo.
        </div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Foucault analisa a transição do poder soberano (punição física pública) para a **Sociedade Disciplinar** (adestramento do corpo e controle das mentes)!")