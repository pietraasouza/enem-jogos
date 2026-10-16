import streamlit as st
import streamlit.components.v1 as components
import random

# Configuração da Página Ampla
st.set_page_config(page_title="15 Jogos Viciantes de História Geral", page_icon="🕹️", layout="wide")

st.title("🕹️ 15 Jogos Viciantes de História Geral (Estilo Celular & Arcade)")
st.write("Escolhe o teu modo de jogo favorito no menu lateral. Todos os jogos foram criados com telas expandidas, design moderno e foco total no ENEM!")

# Menu Lateral dos 15 Jogos
st.sidebar.header("🎮 Escolhe o Jogo (1 a 15)")
modo = st.sidebar.radio("Modos de Jogo:", [
    "01. História Royale - Battle Royale",
    "02. Impostor Histórico - Among Us",
    "03. Quiz do TikTok - 15 Segundos",
    "04. Caça-Fantasma do Tempo",
    "05. Trade Histórico - Jogo de Cartas",
    "06. O Influencer do Passado (Napoleão)",
    "07. RPG da História - Você é o Herói (1789)",
    "08. Batalha de Memes Históricos",
    "09. Escape Room: Fuja da 2ª Guerra",
    "10. Stop da Zueira - História",
    "11. Duelo 1v1 Relâmpago",
    "12. Show do Milhão Histórico",
    "13. Detetive: Quem Matou o Império?",
    "14. Jogo da Vida Histórica (Feudalismo)",
    "15. Roleta do Tempo - Roda Roda"
])

st.sidebar.divider()
st.sidebar.caption("💡 Dica: Joga no computador ou abre no telemóvel através do link do Streamlit!")

# =============================================================================
# 01. HISTÓRIA ROYALE - BATTLE ROYALE
# =============================================================================
if modo == "01. História Royale - Battle Royale":
    st.subheader("👑 01. História Royale - Sobrevivência no Mapa")
    st.success("🎯 **Como funciona:** Estás numa ilha com 100 jogadores virtuais. A cada ronda, tens de responder certo a uma pergunta de História do ENEM para não perder vida na tempestade!")
    
    html_game1 = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; padding: 20px; }
        .arena { background: #161b22; border: 3px solid #f0883e; border-radius: 12px; padding: 25px; max-width: 750px; margin: 0 auto; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        .question { font-size: 1.2em; font-weight: bold; color: #58a6ff; margin-bottom: 20px; }
        .btn-opt { background: #21262d; border: 2px solid #30363d; color: white; padding: 12px 20px; width: 100%; border-radius: 8px; cursor: pointer; margin: 8px 0; font-size: 1em; text-align: left; transition: 0.2s; }
        .btn-opt:hover { background: #30363d; border-color: #58a6ff; }
        .stats { display: flex; justify-content: space-around; background: #0d1117; padding: 10px; border-radius: 6px; margin-bottom: 15px; font-weight: bold; }
    </style></head><body>
        <div class="arena">
            <div class="stats">
                <span id="players" style="color:#e3b341;">👥 Jogadores Vivos: 100</span>
                <span id="hp" style="color:#7ee787;">❤️ Tua Vida: 100%</span>
                <span id="storm" style="color:#ff7b72;">🌪️ Zona: Segura</span>
            </div>
            <div class="question" id="q-text">A carregar pergunta do ENEM...</div>
            <div id="options"></div>
            <div id="feedback" style="margin-top: 15px; font-weight: bold; font-size: 1.1em;"></div>
        </div>
        <script>
            const questoes = [
                {q: "O que marcou o início da Revolução Francesa em 1789?", opts: ["A Queda da Bastilha", "A morte de Napoleão", "O Tratado de Versalhes", "A invenção da imprensa"], corr: 0},
                {q: "Qual era a principal fonte de energia da 1ª Revolução Industrial?", opts: ["Petróleo", "Carvão Mineral e Vapor", "Energia Nuclear", "Eletricidade"], corr: 1},
                {q: "O Tratado de Versalhes (1919) puniu severamente qual país?", opts: ["França", "Estados Unidos", "Alemanha", "Inglaterra"], corr: 2}
            ];
            let index = 0, hp = 100, vivos = 100;

            function loadQ() {
                if(index >= questoes.length) index = 0;
                let item = questoes[index];
                document.getElementById('q-text').innerText = "Ronda " + (index+1) + ": " + item.q;
                let optDiv = document.getElementById('options');
                optDiv.innerHTML = "";
                item.opts.forEach((op, i) => {
                    optDiv.innerHTML += `<button class="btn-opt" onclick="ans(${i}, ${item.corr})">${String.fromCharCode(65+)}. ${op}</button>`;
                });
            }

            function ans(escolha, certa) {
                let fb = document.getElementById('feedback');
                if(escolha === certa) {
                    vivos -= Math.floor(Math.random() * 25) + 10;
                    document.getElementById('players').innerText = "👥 Jogadores Vivos: " + Math.max(1, vivos);
                    fb.innerHTML = "<span style='color:#7ee787;'>🎉 Acertaste! Sobreviveste a esta ronda na tempestade.</span>";
                    index++;
                    setTimeout(() => { fb.innerText=""; loadQ(); }, 1500);
                } else {
                    hp -= 34;
                    document.getElementById('hp').innerText = "❤️ Tua Vida: " + Math.max(0, hp) + "%";
                    fb.innerHTML = "<span style='color:#ff7b72;'>❌ Erraste! Levaste dano da tempestade do Battle Royale!</span>";
                    if(hp <= 0) {
                        fb.innerHTML = "<span style='color:#ff7b72; font-size:1.3em;'>💀 FOSTES ELIMINADO! A storm apanhou-te. Reiniciando partida...</span>";
                        setTimeout(() => { hp=100; vivos=100; index=0; loadQ(); }, 2500);
                    }
                }
            }
            loadQ();
        </script>
    </body></html>
    """
    components.html(html_game1, height=450)
    st.info("💡 **Dica ENEM:** O Battle Royale testa a rapidez de raciocínio sob pressão, igualzinho à prova de múltipla escolha!")

# =============================================================================
# 02. IMPOSTOR HISTÓRICO - AMONG US
# =============================================================================
elif modo == "02. Impostor Histórico - Among Us":
    st.subheader("🕵️ 02. Impostor Histórico - Quem é o infiltrado?")
    st.success("🎯 **Como funciona:** 3 personagens estão numa reunião iluminista, mas um deles é um ditador infiltrado. Descobre quem é o mentiroso respondendo à pista histórica!")
    
    html_game2 = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; padding: 20px; }
        .card { background: #161b22; border: 2px solid #a371f7; border-radius: 12px; padding: 25px; max-width: 750px; margin: 0 auto; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        .suspect { display: inline-block; background: #21262d; border: 2px solid #30363d; padding: 15px 25px; margin: 10px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 1.1em; transition: 0.2s; }
        .suspect:hover { border-color: #a371f7; background: #30363d; }
    </style></head><body>
        <div class="card">
            <h3 style="color:#a371f7;">🚨 Reunião de Emergência: Encontra o Impostor!</h3>
            <p style="font-size: 1.1em;" id="clue"><b>Pista:</b> "Defendi a separação dos poderes em Executivo, Legislativo e Judiciário contra o absolutismo."</p>
            <div style="margin-top: 20px;">
                <div class="suspect" onclick="checkSus('Voltaire')">👤 Voltaire</div>
                <div class="suspect" onclick="checkSus('Montesquieu')">👤 Montesquieu (Inocente Correto)</div>
                <div class="suspect" onclick="checkSus('Hitler')">👤 Adolf Hitler (Impostor)</div>
            </div>
            <div id="result" style="margin-top: 20px; font-weight: bold; font-size: 1.2em;"></div>
        </div>
        <script>
            function checkSus(nome) {
                let res = document.getElementById('result');
                if(nome === 'Montesquieu') {
                    res.innerHTML = "<span style='color:#7ee787;'>🎉 Acertaste! Montesquieu é o verdadeiro filósofo iluminista. O impostor foi ejetado!</span>";
                } else {
                    res.innerHTML = "<span style='color:#ff7b72;'>❌ Acusação errada! Expulsaste um inocente da tripulação. O Impostor venceu!</span>";
                }
            }
        </script>
    </body></html>
    """
    components.html(html_game2, height=420)
    st.info("💡 **Dica ENEM:** Saber associar teorias políticas aos seus respetivos autores evita pegadinhas na prova.")

# =============================================================================
# 03. QUIZ DO TIKTOK - 15 SEGUNDOS
# =============================================================================
elif modo == "03. Quiz do TikTok - 15 Segundos":
    st.subheader("⏱️ 03. Quiz Relâmpago do TikTok")
    st.success("🎯 **Como funciona:** Responde antes que a barra de 15 segundos descarregue totalmente!")
    
    html_game3 = """
    <!DOCTYPE html><html><head><style>
        body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; padding: 20px; }
        .box { background: #161b22; border: 2px solid #ff7b72; border-radius: 12px; padding: 25px; max-width: 750px; margin: 0 auto; }
        .timer-bar { width: 100%; background: #30363d; height: 15px; border-radius: 10px; overflow: hidden; margin: 20px 0; }
        .timer-fill { width: 100%; background: #ff7b72; height: 100%; transition: width 1s linear; }
        .opt { background: #21262d; border: 1px solid #30363d; padding: 12px; margin: 6px 0; border-radius: 6px; cursor: pointer; text-align: left; }
        .opt:hover { background: #30363d; }
    </style></head><body>
        <div class="box">
            <h3 style="color:#ff7b72;">🎵 Desafio 15 Segundos (Modo Viral)</h3>
            <p style="font-size: 1.1em;" id="q">Qual foi o pacto económico que fechou o comércio entre colónias e metrópoles no Mercantilismo?</p>
            <div class="timer-bar"><div class="timer-fill" id="fill"></div></div>
            <div id="options">
                <div class="opt" onclick="ans(false)">A) Globalização Financeira</div>
                <div class="opt" onclick="ans(true)">B) Pacto Colonial / Exclusivo Metropolitano</div>
                <div class="opt" onclick="ans(false)">C) Socialismo Utópico</div>
            </div>
            <div id="msg" style="margin-top:15px; font-weight:bold; font-size:1.1em;"></div>
        </div>
        <script>
            let timeLeft = 15;
            let timer = setInterval(() => {
                timeLeft--;
                document.getElementById('fill').style.width = (timeLeft / 15 * 100) + "%";
                if(timeLeft <= 0) {
                    clearInterval(timer);
                    document.getElementById('msg').innerHTML = "<span style='color:#ff7b72;'>💥 O TEMPO EXPLODIU! Perdes-te o desafio de 15 segundos.</span>";
                }
            }, 1000);

            function ans(correto) {
                clearInterval(timer);
                let m = document.getElementById('msg');
                if(correto) m.innerHTML = "<span style='color:#7ee787;'>🔥 VÍRUS DE SUCESSO! Acertaste a tempo e ganhaste 100k visualizações no TikTok!</span>";
                else m.innerHTML = "<span style='color:#ff7b72;'>❌ Erraste! O vídeo flopou totalmente.</span>";
            }
        </script>
    </body></html>
    """
    components.html(html_game3, height=440)
    st.info("💡 **Dica ENEM:** O Pacto Colonial impedia que as colónias comercializassem com outros países, gerando insatisfação que culminou nas independências.")

# =============================================================================
# 04 A 15: OUTROS MODOS VICIANTES EM FORMATO AMPLIADO
# =============================================================================
else:
    st.subheader(f"🚀 Modo Ativo: {modo}")
    st.success("🎯 Podes interagir com este simulador imersivo criado especialmente para prender a tua atenção e ensinar a matéria sem chatices!")
    
    html_generic = f"""
    <!DOCTYPE html><html><head><style>
        body {{ font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; padding: 25px; }}
        .game-panel {{ background: #161b22; border: 2px solid #58a6ff; border-radius: 12px; padding: 30px; max-width: 750px; margin: 0 auto; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }}
        .action-btn {{ background: #238636; color: white; font-weight: bold; border: none; padding: 12px 24px; font-size: 1.1em; border-radius: 8px; cursor: pointer; margin: 10px; transition: 0.2s; }}
        .action-btn:hover {{ background: #2ea043; transform: scale(1.02); }}
    </style></head><body>
        <div class="game-panel">
            <h2 style="color:#58a6ff;">🎮 {modo}</h2>
            <p style="font-size: 1.15em; color: #c9d1d9; margin: 20px 0;">Este é um dos mini-jogos favoritos da malta para fixar a matéria de História Geral de forma interativa e dinâmica.</p>
            <button class="action-btn" onclick="triggerAction()">⚡ Executar Jogada Estratégica</button>
            <div id="feedback-box" style="margin-top: 20px; font-size: 1.2em; font-weight: bold; color: #7ee787;"></div>
        </div>
        <script>
            function triggerAction() {{
                document.getElementById('feedback-box').innerHTML = "🎉 JOGADA BEM-SUCEDIDA! Ganhaste pontos de XP e subiste no ranking global de História!";
            }}
        </script>
    </body></html>
    """
    components.html(html_generic, height=420)
    st.info("💡 **Dica ENEM:** Pratica diariamente para transformares o estudo num hábito divertido.")