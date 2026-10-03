import streamlit as st
import streamlit.components.v1 as components

# Configuração da Página
st.set_page_config(page_title="20 Jogos de Redação pro ENEM", page_icon="✍️", layout="wide")

st.title("✍️ 20 Jogos & Simuladores de Redação pro ENEM")
st.write("Aprenda a estrutura da dissertação-argumentativa e garanta a Nota 1000 praticando em tempo real!")

# Menu Lateral
st.sidebar.header("🕹️ Selecione o Módulo (1 a 20)")
jogo = st.sidebar.radio("Módulos Interativos:", [
    "01. As 5 Competências do ENEM",
    "02. Anatomia do Parágrafo de Introdução",
    "03. Tese Perfeita (Problematização)",
    "04. Repertório Legítimo & Produtivo",
    "05. Projeto de Texto & Esquema Diretor",
    "06. Desenvolvimento 1: Causa e Efeito",
    "07. Desenvolvimento 2: Argumentação por Contraste",
    "08. Conectivos Interparágrafos (Coesão)",
    "09. Conectivos Intraparágrafos",
    "10. Elementos Obrigatórios da Proposta de Intervenção",
    "11. Agentes da Proposta (GOMIFES)",
    "12. Detalhamento Nota 200 na Proposta",
    "13. Marcas de Impessoalidade (Norma Culta)",
    "14. Paralelismo Sintático e Gramática",
    "15. Evitando Clichês e Palavras-Valise",
    "16. Repertórios Coringa para Eixos Temáticos",
    "17. Análise de Temas Anteriores do ENEM",
    "18. Alinhamento entre Tese e Conclusão",
    "19. Gestão do Tempo na Prova (Rascunho x Folha Definitiva)",
    "20. Checklist do Texto Nota 1000"
])

st.sidebar.divider()
st.sidebar.caption("🎯 **Dica ENEM:** Interaja com as simulações e treine a construção dos elementos da sua redação!")

# =============================================================================
# 01. AS 5 COMPETÊNCIAS
# =============================================================================
if jogo == "01. As 5 Competências do ENEM":
    st.subheader("📊 01. Calculadora de Pontuação pelas 5 Competências")
    st.success("🎯 **O que fazer:** Ajuste a pontuação (0 a 200) de cada competência para ver o cálculo da sua nota total!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">C1 (Gramática): <input type="range" id="c1" min="0" max="200" step="40" value="160" oninput="u()"> <span id="c1v">160</span></div>
        <div class="card">C2 (Tema/Repertório): <input type="range" id="c2" min="0" max="200" step="40" value="200" oninput="u()"> <span id="c2v">200</span></div>
        <div class="card">C3 (Projeto de Texto): <input type="range" id="c3" min="0" max="200" step="40" value="160" oninput="u()"> <span id="c3v">160</span></div><br>
        <div class="card">C4 (Coesão/Conectivos): <input type="range" id="c4" min="0" max="200" step="40" value="200" oninput="u()"> <span id="c4v">200</span></div>
        <div class="card">C5 (Proposta/5 Elementos): <input type="range" id="c5" min="0" max="200" step="40" value="200" oninput="u()"> <span id="c5v">200</span></div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="total" style="color:#7ee787; font-size:1.3em;">Nota Total: 920 pontos</b></div>
        </div>
        <script>
            function u(){
                let c1=parseInt(document.getElementById('c1').value); document.getElementById('c1v').innerText=c1;
                let c2=parseInt(document.getElementById('c2').value); document.getElementById('c2v').innerText=c2;
                let c3=parseInt(document.getElementById('c3').value); document.getElementById('c3v').innerText=c3;
                let c4=parseInt(document.getElementById('c4').value); document.getElementById('c4v').innerText=c4;
                let c5=parseInt(document.getElementById('c5').value); document.getElementById('c5v').innerText=c5;
                let tot = c1+c2+c3+c4+c5;
                document.getElementById('total').innerText = 'Nota Total: ' + tot + ' pontos';
            }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=250)
    st.info("💡 **Macete ENEM:** Cada competência vale de 0 a 200 pontos (com saltos de 40 em 40). O texto final é a soma das 5 competências (máximo 1000 pontos)!")

# =============================================================================
# 02. ANATOMIA DA INTRODUÇÃO
# =============================================================================
elif jogo == "02. Anatomia do Parágrafo de Introdução":
    st.subheader("🏗️ 02. Montador do Parágrafo de Introdução")
    st.success("🎯 **O que fazer:** Clique nas partes da introdução para ver a estrutura padrão: Contextualização ➔ Problematização ➔ Tese com 2 Argumentos.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        button { background: #238636; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; margin: 2px; }
    </style></head><body>
        <div>
            <button onclick="document.getElementById('o').innerText='1. CONTEXTUALIZAÇÃO: Alusão histórica, citação filosófica ou obra literária para apresentar o assunto.'">1. Repertório/Contexto</button>
            <button onclick="document.getElementById('o').innerText='2. PROBLEMATIZAÇÃO: Conectar o repertório ao tema concreto do ENEM usando um conectivo adversativo (ex: Contudo, Todavia).'">2. Apresentação do Tema</button>
            <button onclick="document.getElementById('o').innerText='3. TESE: Apresentar explicitamente os 2 problemas (Argumento A e Argumento B) que serão desenvolvidos no texto.'">3. Tese Dual</button>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="o" style="color:#58a6ff;">Clique nos botões acima para ver a função de cada frase!</b></div>
        </div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Uma boa introdução tem entre 5 e 7 linhas e é dividida estrategicamente em 3 períodos (frases)!")

# =============================================================================
# 03. TESE PERFEITA
# =============================================================================
elif jogo == "03. Tese Perfeita (Problematização)":
    st.subheader("🎯 03. Formulador de Tese Dual (A1 + A2)")
    st.success("🎯 **O que fazer:** Selecione duas causas do problema para gerar uma tese pronta e alinhada ao padrão ENEM!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Causa 1 (D1): 
            <select id="a1" onchange="u()">
                <option value="a omissão governamental">Omissão Governamental</option>
                <option value="a negligência educacional">Negligência Educacional</option>
                <option value="a falta de informação da sociedade">Falta de Informação</option>
            </select>
        </div>
        <div class="card">
            Causa 2 (D2): 
            <select id="a2" onchange="u()">
                <option value="a perpetuação de estigmas históricos">Estigmas Históricos</option>
                <option value="a busca desenfreada pelo lucro">Capitalismo Selvagem</option>
                <option value="a passividade social">Passividade Social</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="out" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){
                let a1 = document.getElementById('a1').value;
                let a2 = document.getElementById('a2').value;
                document.getElementById('out').innerText = 'Tese: "...torna-se imperioso analisar não apenas ' + a1 + ', mas também ' + a2 + '."';
            }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** A tese antecipa exatamente o que virá no Desenvolvimento 1 (Causa 1) e no Desenvolvimento 2 (Causa 2).")

# =============================================================================
# 04. REPERTÓRIO LEGÍTIMO
# =============================================================================
elif jogo == "04. Repertório Legítimo & Produtivo":
    st.subheader("📚 04. Validador de Repertório Sociocultural")
    st.success("🎯 **O que fazer:** Veja o que transforma um repertório em Nota 200 na Competência 2!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
    </style></head><body>
        <div class="card">
            <b>1. LEGÍTIMO:</b> Pertence a uma área do conhecimento (Filosofia, Sociologia, História, Literatura, Filmes).<br>
            <b>2. PERTINENTE:</b> Relaciona-se diretamente com o tema cobrado.<br>
            <b>3. PRODUTIVO:</b> É usado para fundamentar o seu argumento (não fica "solto" no texto).
        </div>
    </body></html>
    """
    components.html(html, height=170)
    st.info("💡 **Macete ENEM:** Citou o repertório? Sempre explique o significado dele e conecte explicitamente com a realidade do problema abordado!")

# =============================================================================
# 05. PROJETO DE TEXTO
# =============================================================================
elif jogo == "05. Projeto de Texto & Esquema Diretor":
    st.subheader("🗺️ 05. Simulador do Esquema do Texto (Competência 3)")
    st.success("🎯 **O que fazer:** Acompanhe a estrutura ideal de 4 parágrafos e 30 linhas.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 2px; }
    </style></head><body>
        <div class="card" style="border:1px solid #58a6ff;"><b>Parágrafo 1:</b> Introdução (~6 linhas)</div><br>
        <div class="card" style="border:1px solid #7ee787;"><b>Parágrafo 2:</b> Desenvolvimento 1 (~8 linhas)</div><br>
        <div class="card" style="border:1px solid #e3b341;"><b>Parágrafo 3:</b> Desenvolvimento 2 (~8 linhas)</div><br>
        <div class="card" style="border:1px solid #ff7b72;"><b>Parágrafo 4:</b> Conclusão/Intervenção (~8 linhas)</div>
    </body></html>
    """
    components.html(html, height=200)
    st.info("💡 **Macete ENEM:** Manter a simetria no tamanho dos parágrafos demonstra excelente planejamento prévio de texto!")

# =============================================================================
# 06. DESENVOLVIMENTO 1
# =============================================================================
elif jogo == "06. Desenvolvimento 1: Causa e Efeito":
    st.subheader("🔥 06. Estruturação do Parágrafo de Argumentação")
    st.success("🎯 **O que fazer:** Veja as 4 frases indispensáveis para construir um Desenvolvimento Nota 200.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            <b>1. Tópico Frasal:</b> Apresenta a causa central do parágrafo.<br>
            <b>2. Repertório:</b> Insere o embasamento teórico.<br>
            <b>3. Aprofundamento Argumentativo:</b> Explica a relação de causa/efeito na sociedade.<br>
            <b>4. Fechamento:</b> Conclui o raciocínio reforçando o impacto do problema.
        </div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** O segredo do desenvolvimento é dedicar a maior parte do parágrafo ao **Aprofundamento Argumentativo** (suas próprias palavras)!")

# =============================================================================
# 07. DESENVOLVIMENTO 2
# =============================================================================
elif jogo == "07. Desenvolvimento 2: Argumentação por Contraste":
    st.subheader("⚖️ 07. Construindo o Segundo Desenvolvimento")
    st.success("🎯 **O que fazer:** Inicie o D2 com um conectivo de adição interparágrafo para dar continuidade lógica ao texto.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card" style="border: 1px solid #7ee787;">
            <b>Conectivo Obrigatório de Início do D2:</b><br>
            "Ademais...", "Outrossim...", "Além disso...", "Paralelamente a isso..."
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** Para fechar 200 na Competência 4, é OBRIGATÓRIO começar o D2 e a Conclusão com conectivos interparágrafos válidos!")

# =============================================================================
# 08. CONECTIVOS INTERPARÁGRAFOS
# =============================================================================
elif jogo == "08. Conectivos Interparágrafos (Coesão)":
    st.subheader("🔗 08. Conectores Interparágrafos (Competência 4)":
    st.success("🎯 **O que fazer:** Selecione o parágrafo para escolher o conector de transição ideal.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #58a6ff; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Início do Parágrafo: 
            <select id="p" onchange="u()">
                <option value="D2 (Adição) ➔ Ademais, Outrossim, Além disso">Desenvolvimento 2</option>
                <option value="Conclusão (Fechamento) ➔ Portanto, Depreende-se, portanto, Assim">Conclusão</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="o" style="color:#58a6ff;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('o').innerText = document.getElementById('p').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Nunca use 'Em primeiro lugar' no D1 se não for usar 'Em segundo lugar' no D2! Prefira conectivos de adição como 'Ademais'.")

# =============================================================================
# 09. CONECTIVOS INTRAPARÁGRAFOS
# =============================================================================
elif jogo == "09. Conectivos Intraparágrafos":
    st.subheader("🧩 09. Operadores Argumentativos Internos")
    st.success("🎯 **O que fazer:** Conheça as conjunções que ligam as frases DENTRO do mesmo parágrafo.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 2px; }
    </style></head><body>
        <div class="card"><b>Oposição:</b> Entretanto, Contudo, Todavia, No entanto</div><br>
        <div class="card"><b>Causa/Explicação:</b> Porquanto, Visto que, Haja vista que</div><br>
        <div class="card"><b>Consequência:</b> De modo que, Em decorrência disso, Por conseguinte</div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Varie os conectivos ao longo do texto. A repetição excessiva de 'porém' ou 'pois' perde pontos na C4!")

# =============================================================================
# 10. ELEMENTOS DA PROPOSTA
# =============================================================================
elif jogo == "10. Elementos Obrigatórios da Proposta de Intervenção":
    st.subheader("🛠️ 10. Os 5 Elementos da Proposta de Intervenção")
    st.success("🎯 **O que fazer:** Marque os 5 elementos essenciais na Conclusão para garantir 200 pontos automáticos na Competência 5!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card" style="text-align:left;">
            1. <b>AGENTE:</b> Quem fará a ação? (40 pts)<br>
            2. <b>AÇÃO:</b> O que será feito? (40 pts)<br>
            3. <b>MEIO/MODO:</b> Como será feito? (40 pts)<br>
            4. <b>EFEITO:</b> Para que será feito? (40 pts)<br>
            5. <b>DETALHAMENTO:</b> Informação extra sobre um dos elementos acima. (40 pts)
        </div>
    </body></html>
    """
    components.html(html, height=190)
    st.info("💡 **Macete ENEM:** Cada elemento presente na proposta vale exatamente **40 pontos**. Faltou 1 elemento = nota máxima 160 na C5!")

# =============================================================================
# 11. AGENTES DA PROPOSTA (GOMIFES)
# =============================================================================
elif jogo == "11. Agentes da Proposta (GOMIFES)":
    st.subheader("🏛️ 11. Seleção do Agente Social (GOMIFES)")
    st.success("🎯 **O que fazer:** Escolha o agente social ideal para atuar na solução do problema abordado.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #7ee787; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Agente: 
            <select id="a" onchange="u()">
                <option value="Governo (Ministérios) ➔ Ações de infraestrutura, leis e verbas públicas.">G - Governo</option>
                <option value="ONGs ➔ Campanhas de conscientização e apoio comunitário.">O - ONGs</option>
                <option value="Mídia ➔ Difusão de informação e debates públicos.">M - Mídia</option>
                <option value="Instituições de Ensino / Família ➔ Educação de base e valores éticos.">I/F - Escola e Família</option>
                <option value="Sociedade ➔ Engajamento e cobrança de direitos.">S - Sociedade</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #7ee787;"><b id="o" style="color:#7ee787;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('o').innerText = document.getElementById('a').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Especifique o Ministério responsável (ex: 'Ministério da Educação', 'Ministério da Saúde') em vez de usar apenas a palavra vaga 'Governo'!")

# =============================================================================
# 12. DETALHAMENTO NOTA 200
# =============================================================================
elif jogo == "12. Detalhamento Nota 200 na Proposta":
    st.subheader("🔍 12. Como Fazer o Detalhamento Perfeito")
    st.success("🎯 **O que fazer:** Veja como adicionar uma explicação extra (geralmente entre travessões ou vírgulas) para garantir o detalhamento.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            Exemplo de Detalhamento do Agente:<br>
            "...cabe ao Ministério da Educação <b>— órgão responsável pelas diretrizes pedagógicas nacionais —</b> criar workshops..."
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** O jeito mais simples e seguro de fazer detalhamento é usar um **aposto explicativo** sobre o Agente entre travessões!")

# =============================================================================
# 13. IMPESSOALIDADE
# =============================================================================
elif jogo == "13. Marcas de Impessoalidade (Norma Culta)":
    st.subheader("🚫 13. Eliminando a 1ª Pessoa do Texto")
    st.success("🎯 **O que fazer:** Mude expressões em 1ª pessoa ('eu acho', 'nosso país') para a 3ª pessoa impessoal.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            ❌ <s>"Eu acho que no nosso Brasil..."</s><br><br>
            ✅ <b>"Notadamente, no cenário brasileiro hodierno, constata-se que..."</b>
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** O texto dissertativo deve ser estritamente impessoal. Use verbos na 3ª pessoa do singular acompanhados do pronome 'se' (ex: *observa-se*, *evidencia-se*)!")

# =============================================================================
# 14. PARALELISMO SINTÁTICO
# =============================================================================
elif jogo == "14. Paralelismo Sintático e Gramática":
    st.subheader("📏 14. Correção Gramatical e Paralelismo")
    st.success("🎯 **O que fazer:** Mantenha a mesma estrutura gramatical ao listar elementos na frase.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            ❌ Sem Paralelismo: É preciso investir em <b>educação</b> (substantivo) e <b>reciclar</b> (verbo).<br><br>
            ✅ Com Paralelismo: É preciso investir na <b>educação</b> (substantivo) e na <b>reciclagem</b> (substantivo).
        </div>
    </body></html>
    """
    components.html(html, height=160)
    st.info("💡 **Macete ENEM:** Falhas repetidas de crase, regência e quebra de paralelismo reduzem pontos na Competência 1!")

# =============================================================================
# 15. EVITANDO CLICHÊS
# =============================================================================
elif jogo == "15. Evitando Clichês e Palavras-Valise":
    st.subheader("🧹 15. Substituindo Termos Desgastados")
    st.success("🎯 **O que fazer:** Elimine clichês e expressões genéricas da sua escrita.")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 2px; }
    </style></head><body>
        <div class="card">❌ "Nos dias de hoje" ➔ ✅ <b>"Na contemporaneidade" / "Hodiernamente"</b></div><br>
        <div class="card">❌ "Fechar os olhos para o problema" ➔ ✅ <b>"Invisibilizar a problemática"</b></div><br>
        <div class="card">❌ "Lugar ao sol" ➔ ✅ <b>"Cidadania e inclusão social"</b></div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Evite ditados populares, metáforas excessivas ou jargões informais na dissertação acadêmica!")

# =============================================================================
# 16. REPERTÓRIOS CORINGA
# =============================================================================
elif jogo == "16. Repertórios Coringa para Eixos Temáticos":
    st.subheader("🃏 16. Repertórios Curinga Adaptáveis")
    st.success("🎯 **O que fazer:** Selecione o eixo temático para ver um repertório filosófico ou sociológico aplicável!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; margin: 4px; }
        select { padding: 6px; background: #161b22; color: white; border: 1px solid #58a6ff; border-radius: 4px; }
    </style></head><body>
        <div class="card">
            Eixo Temático: 
            <select id="e" onchange="u()">
                <option value="Constituição de 1988 ➔ Garante direitos fundamentais (saúde, educação, segurança) negados na prática.">Direitos & Cidadania</option>
                <option value="Thomas Hobbes (Contrato Social) ➔ O Estado falha em garantir o bem-estar e a segurança dos cidadãos.">Sociedade & Estado</option>
                <option value="Zygmunt Bauman (Modernidade Líquida) ➔ Relações frágeis e fluidez nas instituições sociais.">Tecnologia & Comportamento</option>
                <option value="Gilberto Dimenstein (Cidadãos de Papel) ➔ Direitos garantidos na lei, mas ineficazes na prática.">Desigualdade Social</option>
            </select>
        </div>
        <div style="margin-top:10px;">
            <div class="card" style="border: 1px solid #58a6ff;"><b id="o" style="color:#58a6ff;">-</b></div>
        </div>
        <script>
            function u(){ document.getElementById('o').innerText = document.getElementById('e').value; }
            u();
        </script>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** O conceito de 'Cidadãos de Papel' de Dimenstein encaixa-se na maioria dos temas de eixos sociais e direitos vulnerados!")

# =============================================================================
# 17. TEMAS ANTERIORES
# =============================================================================
elif jogo == "17. Análise de Temas Anteriores do ENEM":
    st.subheader("📜 17. Padrão de Temas Cobrados pelo ENEM")
    st.success("🎯 **O que fazer:** Observe como todos os temas focam em recortes de problemas sociais de minorias ou vulnerabilidades no Brasil!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            • <b>2023:</b> Desafios para o enfrentamento da invisibilidade do trabalho de cuidado realizado pela mulher.<br>
            • <b>2022:</b> Desafios para a valorização de comunidades e povos tradicionais no Brasil.<br>
            • <b>2021:</b> Invisibilidade e registro civil: garantia de acesso à cidadania no Brasil.
        </div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** A palavra 'Desafios', 'Caminhos' ou 'Invisibilidade' quase sempre aparece na frase temática do ENEM para indicar a necessidade de solução!")

# =============================================================================
# 18. ALINHAMENTO TESE E CONCLUSÃO
# =============================================================================
elif jogo == "18. Alinhamento entre Tese e Conclusão":
    st.subheader("🔄 18. Coerência entre Argumentos e Proposta")
    st.success("🎯 **O que fazer:** Certifique-se de que a sua proposta de intervenção resolve EXATAMENTE os problemas apresentados na tese!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 10px; border-radius: 8px; display: inline-block; }
    </style></head><body>
        <div class="card">
            Tese: Causa 1 (Omissão do Estado) + Causa 2 (Falta de Informação)<br>
            ⬇️<br>
            Proposta 1: Ação do Governo/Ministério (Resolve Causa 1)<br>
            Proposta 2/Detalhamento: Ação da Mídia/Escola (Resolve Causa 2)
        </div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Se você citou falta de educação no D1, a sua proposta DEVE ter uma ação focada em escolas ou campanhas educativas!")

# =============================================================================
# 19. GESTÃO DO TEMPO
# =============================================================================
elif jogo == "19. Gestão do Tempo na Prova (Rascunho x Folha Definitiva)":
    st.subheader("⏱️ 19. Divisão do Tempo de Prova (1h30m)")
    st.success("🎯 **O que fazer:** Veja a cronometragem perfeita para planejar, rascunhar e passar a limpo sem correria!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; margin: 2px; }
    </style></head><body>
        <div class="card"><b>1. Projeto de Texto / Tempestade de Ideias:</b> 15 minutos</div><br>
        <div class="card"><b>2. Rascunho Completo:</b> 45 minutos</div><br>
        <div class="card"><b>3. Transcrição para a Folha Definitiva:</b> 30 minutos</div>
    </body></html>
    """
    components.html(html, height=180)
    st.info("💡 **Macete ENEM:** Comece a prova lendo o tema de redação, faça o projeto de texto e depois vá resolver algumas questões antes de passar a limpo!")

# =============================================================================
# 20. CHECKLIST NOTA 1000
# =============================================================================
elif jogo == "20. Checklist do Texto Nota 1000":
    st.subheader("✅ 20. Validação Final do Texto Antes da Entrega")
    st.success("🎯 **O que fazer:** Verifique se o seu texto cumpre todos os requisitos antes de entregar a prova!")
    
    html = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; }
        .card { background: #21262d; padding: 8px; border-radius: 8px; display: inline-block; text-align: left; }
    </style></head><body>
        <div class="card">
            [ ] Texto entre 25 e 30 linhas?<br>
            [ ] Dividido em exatamente 4 parágrafos?<br>
            [ ] Possui repertório sociocultural produtivo?<br>
            [ ] Presença de conectivos no início do D2 e da Conclusão?<br>
            [ ] Proposta de intervenção com os 5 elementos (Agente, Ação, Meio, Efeito e Detalhamento)?
        </div>
    </body></html>
    """
    components.html(html, height=190)
    st.info("💡 **Macete ENEM:** Respeite a margem e não ultrapasse as 30 linhas oficiais da folha de resposta!")